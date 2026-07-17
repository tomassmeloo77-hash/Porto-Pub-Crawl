// /api/stripe-webhook.js
// Vercel serverless function — Stripe calls this automatically the instant a
// payment succeeds. We verify it's really Stripe (via a signing secret), then:
//   1. send a branded confirmation email to the customer (via Resend),
//   2. send an internal sale notification to our inbox, and
//   3. fire a server-side "Purchase" event to the Meta Conversions API so Meta
//      Ads campaigns can actually see and optimise for real bookings.
//
// Why the server-side Purchase matters: the browser Pixel's Purchase only fires
// if the buyer lands back on /?booking=success — which fails on ad-blockers,
// iOS/Safari tracking prevention, or if they close the tab after paying. The
// webhook always runs, so this is the reliable source of truth. Both carry the
// same event_id (the Stripe session id), so Meta deduplicates them and never
// double-counts a sale.
//
// SETUP (do this once):
//
// 1. Create a free account at resend.com
// 2. Settings → API Keys → create one → copy it
// 3. Domains → Add Domain → add porto-pubcrawl.com → add the DNS records
//    they give you (at your domain registrar) → wait for it to verify
//    (usually a few minutes to a few hours). Until it's verified, emails
//    will fail to send from your own domain.
// 4. In Vercel → Settings → Environment Variables, add:
//      RESEND_API_KEY = re_xxxxxxxx
// 5. In Stripe dashboard → Developers → Webhooks → Add endpoint
//      Endpoint URL: https://porto-pubcrawl.com/api/stripe-webhook
//      Events to send: checkout.session.completed
//    After creating it, Stripe shows a "Signing secret" (starts whsec_) —
//    copy it and add to Vercel env vars as:
//      STRIPE_WEBHOOK_SECRET = whsec_xxxxxxxx
// 6. For the Meta Conversions API, in Meta Events Manager → your Pixel
//    (1729899044988200) → Settings → Conversions API → "Generate access token",
//    then add to Vercel env vars:
//      META_CAPI_ACCESS_TOKEN = EAAxxxxxxxx
//    (optional) META_PIXEL_ID  = 1729899044988200  — only if the Pixel changes.
//    Without META_CAPI_ACCESS_TOKEN the webhook still works; it just skips the
//    server-side Purchase event and logs a warning.
// 7. Redeploy so the new env vars are picked up.
//
// Do this once in test mode first (use a test-mode webhook + test Resend
// send) before repeating steps 5 for live mode with your live keys.

const Stripe = require('stripe');
const crypto = require('crypto');

// Meta Pixel this site loads in index.html. Kept in sync so the browser Pixel
// and the server-side Conversions API report to the same asset.
const META_PIXEL_ID = process.env.META_PIXEL_ID || '1729899044988200';
const META_GRAPH_VERSION = 'v19.0';

// Meta requires PII (email) to be SHA-256 hashed, normalised to lowercase and
// trimmed first. fbp/fbc, IP and user-agent are sent raw (not hashed).
function hashSha256(value) {
  return crypto.createHash('sha256').update(String(value).trim().toLowerCase()).digest('hex');
}

// Fire a server-side "Purchase" to the Meta Conversions API. Never throws — a
// tracking failure must not break the webhook (Stripe would just retry it and
// the customer would get a duplicate email), so all errors are logged only.
async function sendMetaPurchaseEvent(session) {
  const token = process.env.META_CAPI_ACCESS_TOKEN;
  if (!token) {
    console.warn('META_CAPI_ACCESS_TOKEN not set — skipping server-side Meta Purchase event');
    return;
  }

  const meta = session.metadata || {};
  const email = session.customer_details && session.customer_details.email;
  const name = session.customer_details && session.customer_details.name;
  const value = (session.amount_total || 0) / 100;

  // Match keys — the more we send, the better Meta attributes the sale.
  const userData = {};
  if (email) userData.em = [hashSha256(email)];
  if (name) userData.fn = [hashSha256(name.split(' ')[0])];
  if (meta.fbp) userData.fbp = meta.fbp;
  if (meta.fbc) userData.fbc = meta.fbc;
  if (meta.client_ip) userData.client_ip_address = meta.client_ip;
  if (meta.client_ua) userData.client_user_agent = meta.client_ua;

  const payload = {
    data: [{
      event_name: 'Purchase',
      event_time: Math.floor(Date.now() / 1000),
      // Same id the browser Pixel sends as `eventID` → Meta dedupes the two.
      event_id: session.id,
      action_source: 'website',
      event_source_url: meta.event_source_url || 'https://www.porto-pubcrawl.com/',
      user_data: userData,
      custom_data: {
        currency: (session.currency || 'eur').toUpperCase(),
        value: value,
        content_name: PACKAGE_NAMES[meta.package] || 'Porto Pub Crawl',
        content_type: 'product',
        num_items: parseInt(meta.quantity, 10) || 1
      }
    }]
  };

  try {
    const url = `https://graph.facebook.com/${META_GRAPH_VERSION}/${META_PIXEL_ID}/events?access_token=${encodeURIComponent(token)}`;
    const capiRes = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    if (!capiRes.ok) {
      const errBody = await capiRes.text();
      console.error('Meta CAPI Purchase failed:', capiRes.status, errBody);
    }
  } catch (err) {
    console.error('Error sending Meta CAPI Purchase event:', err);
  }
}

// Vercel-specific: we need the RAW request body to verify the Stripe
// signature, so we turn off Vercel's automatic JSON body parsing.
module.exports.config = { api: { bodyParser: false } };

function readRawBody(req) {
  return new Promise((resolve, reject) => {
    const chunks = [];
    req.on('data', (chunk) => chunks.push(chunk));
    req.on('end', () => resolve(Buffer.concat(chunks)));
    req.on('error', reject);
  });
}

const PACKAGE_NAMES = {
  crawl: 'Porto Pub Crawl',
  pack: 'Party Boat + Pub Crawl Pack'
};

// The buyer fully controls the name (and email) they type into Stripe Checkout.
// Those land in the confirmation email and — more importantly — the admin
// notification delivered to our own inbox. Escaping them before interpolation
// stops a booking name like `<a href="evil">…</a>` from injecting HTML/links.
function escapeHtml(value) {
  if (value === null || value === undefined) return '';
  return String(value)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function buildEmailHtml({ name, packageName, niceDate, qty }) {
  name = escapeHtml(name);
  packageName = escapeHtml(packageName);
  niceDate = escapeHtml(niceDate);
  qty = escapeHtml(qty);
  const MAPS_LINK = 'https://maps.app.goo.gl/gw6wz2S7iKU7eybL7';
  return `
  <div style="background:#08070a;padding:40px 20px;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;">
    <div style="max-width:480px;margin:0 auto;background:#131314;border-radius:20px;overflow:hidden;border:1px solid #232325;box-shadow:0 30px 80px -20px rgba(255,23,63,0.25);">
      <div style="background:linear-gradient(135deg,#ff173f,#ff5a8f 45%,#3c0512);padding:36px 28px 30px;text-align:center;">
        <img src="https://www.porto-pubcrawl.com/assets/logo-email.png" alt="Project P" width="180" style="display:block;margin:0 auto 18px;height:auto;">
        <div style="display:inline-block;background:rgba(255,255,255,0.16);border-radius:100px;padding:8px 18px;">
          <span style="font-size:15px;font-weight:800;color:#fff;">You're on the list! 🎉</span>
        </div>
      </div>
      <div style="padding:32px 28px 28px;">
        <p style="color:#f5f4f2;font-size:15px;line-height:1.6;margin:0 0 24px;">
          ${name ? 'Hey ' + name + ',' : 'Hey,'} your spot on the Porto Pub Crawl is confirmed. Here's everything you need for Saturday:
        </p>
        <table style="width:100%;border-collapse:collapse;margin-bottom:24px;">
          <tr>
            <td style="padding:12px 0;border-bottom:1px solid #232325;color:#a3a0a1;font-size:11.5px;text-transform:uppercase;letter-spacing:.06em;font-weight:700;">Package</td>
            <td style="padding:12px 0;border-bottom:1px solid #232325;color:#f5f4f2;font-size:14.5px;text-align:right;font-weight:700;">${packageName}</td>
          </tr>
          <tr>
            <td style="padding:12px 0;border-bottom:1px solid #232325;color:#a3a0a1;font-size:11.5px;text-transform:uppercase;letter-spacing:.06em;font-weight:700;">Date</td>
            <td style="padding:12px 0;border-bottom:1px solid #232325;color:#f5f4f2;font-size:14.5px;text-align:right;font-weight:700;">${niceDate}</td>
          </tr>
          <tr>
            <td style="padding:12px 0;border-bottom:1px solid #232325;color:#a3a0a1;font-size:11.5px;text-transform:uppercase;letter-spacing:.06em;font-weight:700;">Spots</td>
            <td style="padding:12px 0;border-bottom:1px solid #232325;color:#f5f4f2;font-size:14.5px;text-align:right;font-weight:700;">${qty}</td>
          </tr>
          <tr>
            <td style="padding:12px 0;border-bottom:1px solid #232325;color:#a3a0a1;font-size:11.5px;text-transform:uppercase;letter-spacing:.06em;font-weight:700;">Meeting point</td>
            <td style="padding:12px 0;border-bottom:1px solid #232325;text-align:right;">
              <a href="${MAPS_LINK}" style="color:#ff5468;font-size:14.5px;font-weight:700;text-decoration:none;">📍 Praça de Carlos Alberto</a>
            </td>
          </tr>
          <tr>
            <td style="padding:12px 0;color:#a3a0a1;font-size:11.5px;text-transform:uppercase;letter-spacing:.06em;font-weight:700;">Time</td>
            <td style="padding:12px 0;color:#f5f4f2;font-size:14.5px;text-align:right;font-weight:700;">22:30 — look for the pink umbrellas</td>
          </tr>
        </table>
        <a href="${MAPS_LINK}" style="display:block;text-align:center;background:linear-gradient(135deg,#ff173f,#ff5a8f);color:#fff;font-size:14px;font-weight:800;text-decoration:none;padding:14px 20px;border-radius:100px;margin-bottom:24px;">📍 Open meeting point in Maps</a>
        <p style="color:#a3a0a1;font-size:13px;line-height:1.6;margin:0 0 6px;">
          Questions before Saturday? Message us on WhatsApp: <a href="https://wa.me/351910694984" style="color:#ff5468;">+351 910 694 984</a>
        </p>
        <p style="color:#7e7b7c;font-size:12px;line-height:1.6;margin:20px 0 0;">
          Free cancellation up to 24h before your start time — just reply to this email or WhatsApp us.
        </p>
      </div>
      <div style="padding:20px 28px;background:#0d0d0e;text-align:center;border-top:1px solid #232325;">
        <p style="color:#7e7b7c;font-size:11px;margin:0;">Project P · Porto's most talked-about night out, every Saturday since 2025.</p>
      </div>
    </div>
  </div>`;
}

function buildAdminNotificationHtml({ name, email, packageName, niceDate, qty, amount, currency, sessionId, purchasedAt }) {
  name = escapeHtml(name);
  email = escapeHtml(email);
  packageName = escapeHtml(packageName);
  niceDate = escapeHtml(niceDate);
  qty = escapeHtml(qty);
  amount = escapeHtml(amount);
  const row = (label, value) => `
    <tr>
      <td style="padding:11px 0;border-bottom:1px solid #232325;color:#a3a0a1;font-size:11.5px;text-transform:uppercase;letter-spacing:.06em;font-weight:700;white-space:nowrap;">${label}</td>
      <td style="padding:11px 0 11px 16px;border-bottom:1px solid #232325;color:#f5f4f2;font-size:14.5px;text-align:right;font-weight:700;">${value}</td>
    </tr>`;
  return `
  <div style="background:#08070a;padding:40px 20px;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;">
    <div style="max-width:480px;margin:0 auto;background:#131314;border-radius:20px;overflow:hidden;border:1px solid #232325;box-shadow:0 30px 80px -20px rgba(34,255,122,0.18);">
      <div style="background:linear-gradient(135deg,#1a1a1c,#232325);padding:26px 28px;text-align:center;border-bottom:2px solid #22ff7a;">
        <img src="https://www.porto-pubcrawl.com/assets/logo-email.png" alt="Project P" width="140" style="display:block;margin:0 auto 12px;height:auto;">
        <div style="display:inline-block;background:rgba(34,255,122,0.14);border-radius:100px;padding:7px 16px;">
          <span style="font-size:13px;font-weight:800;color:#22ff7a;">💰 New booking received</span>
        </div>
      </div>
      <div style="padding:28px;">
        <table style="width:100%;border-collapse:collapse;margin-bottom:6px;">
          ${row('Customer', name || '—')}
          ${row('Email', `<a href="mailto:${email}" style="color:#ff5468;text-decoration:none;">${email}</a>`)}
          ${row('Package', packageName)}
          ${row('Crawl date', niceDate)}
          ${row('Spots', qty)}
          ${row('Amount paid', `${amount}`)}
          ${row('Purchased', purchasedAt)}
        </table>
        <p style="color:#7e7b7c;font-size:11.5px;line-height:1.6;margin:20px 0 0;word-break:break-all;">
          Stripe session: ${sessionId}
        </p>
      </div>
      <div style="padding:18px 28px;background:#0d0d0e;text-align:center;border-top:1px solid #232325;">
        <p style="color:#7e7b7c;font-size:11px;margin:0;">Internal notification · Porto Pub Crawl bookings</p>
      </div>
    </div>
  </div>`;
}

module.exports = async (req, res) => {
  if (req.method !== 'POST') {
    res.status(405).send('Method not allowed');
    return;
  }
  if (!process.env.STRIPE_SECRET_KEY || !process.env.STRIPE_WEBHOOK_SECRET) {
    console.error('Missing STRIPE_SECRET_KEY or STRIPE_WEBHOOK_SECRET');
    res.status(500).send('Not configured');
    return;
  }

  const stripe = Stripe(process.env.STRIPE_SECRET_KEY);
  const rawBody = await readRawBody(req);
  const sig = req.headers['stripe-signature'];

  let event;
  try {
    event = stripe.webhooks.constructEvent(rawBody, sig, process.env.STRIPE_WEBHOOK_SECRET);
  } catch (err) {
    console.error('Webhook signature verification failed:', err.message);
    res.status(400).send(`Webhook Error: ${err.message}`);
    return;
  }

  if (event.type === 'checkout.session.completed') {
    const session = event.data.object;
    const email = session.customer_details && session.customer_details.email;
    const name = session.customer_details && session.customer_details.name;
    const meta = session.metadata || {};

    // Report the sale to Meta first (independent of whether email is configured)
    // so ad campaigns can attribute and optimise for it.
    await sendMetaPurchaseEvent(session);

    if (email && process.env.RESEND_API_KEY) {
      const packageName = PACKAGE_NAMES[meta.package] || 'Porto Pub Crawl';
      const qty = meta.quantity || '1';
      let niceDate = meta.event_date || '';
      if (meta.event_date) {
        niceDate = new Date(meta.event_date + 'T00:00:00Z').toLocaleDateString('en-GB', {
          weekday: 'long', day: 'numeric', month: 'long', timeZone: 'UTC'
        });
      }
      const amount = ((session.amount_total || 0) / 100).toFixed(2) + ' ' + (session.currency || 'eur').toUpperCase();
      const purchasedAt = new Date().toLocaleString('en-GB', {
        dateStyle: 'medium', timeStyle: 'short', timeZone: 'Europe/Lisbon'
      }) + ' (Lisbon time)';

      // 1) confirmation email to the customer
      // Idempotency-Key: Stripe can and does redeliver the same webhook event
      // (e.g. if our response is slow or a network blip drops the ack), so we
      // key on the session id — Resend dedupes retries of the same key within
      // 24h instead of sending the customer two confirmation emails.
      try {
        const resendRes = await fetch('https://api.resend.com/emails', {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${process.env.RESEND_API_KEY}`,
            'Content-Type': 'application/json',
            'Idempotency-Key': `booking-confirmation-${session.id}`
          },
          body: JSON.stringify({
            from: 'Porto Pub Crawl <bookings@porto-pubcrawl.com>',
            to: email,
            subject: `You're on the list! Saturday, ${niceDate}`,
            html: buildEmailHtml({ name, packageName, niceDate, qty })
          })
        });
        if (!resendRes.ok) {
          const errBody = await resendRes.text();
          console.error('Resend send failed (customer email):', resendRes.status, errBody);
        }
      } catch (err) {
        console.error('Error sending confirmation email:', err);
      }

      // 2) internal sale notification to your personal inbox
      try {
        const adminRes = await fetch('https://api.resend.com/emails', {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${process.env.RESEND_API_KEY}`,
            'Content-Type': 'application/json',
            'Idempotency-Key': `booking-admin-notice-${session.id}`
          },
          body: JSON.stringify({
            from: 'Porto Pub Crawl <bookings@porto-pubcrawl.com>',
            to: 'tomasmelo002@gmail.com',
            subject: `💰 New booking — ${packageName} — ${amount}`,
            html: buildAdminNotificationHtml({ name, email, packageName, niceDate, qty, amount, sessionId: session.id, purchasedAt })
          })
        });
        if (!adminRes.ok) {
          const errBody = await adminRes.text();
          console.error('Resend send failed (admin notification):', adminRes.status, errBody);
        }
      } catch (err) {
        console.error('Error sending admin notification email:', err);
      }
    }
  }

  res.status(200).json({ received: true });
};
