// /api/stripe-webhook.js
// Vercel serverless function — Stripe calls this automatically the instant a
// payment succeeds. We verify it's really Stripe (via a signing secret),
// then send a branded confirmation email to the customer through Resend.
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
// 6. Redeploy so the new env vars are picked up.
//
// Do this once in test mode first (use a test-mode webhook + test Resend
// send) before repeating steps 5 for live mode with your live keys.

const Stripe = require('stripe');

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

function buildEmailHtml({ name, packageName, niceDate, qty }) {
  return `
  <div style="background:#08070a;padding:40px 20px;font-family:Arial,Helvetica,sans-serif;">
    <div style="max-width:480px;margin:0 auto;background:#131314;border-radius:20px;overflow:hidden;border:1px solid #232325;">
      <div style="background:linear-gradient(135deg,#ff173f,#ff5a8f 45%,#3c0512);padding:32px 28px;text-align:center;">
        <div style="font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:rgba(255,255,255,.85);font-weight:700;">Project P</div>
        <div style="font-size:26px;font-weight:800;color:#fff;margin-top:6px;">You're on the list! 🎉</div>
      </div>
      <div style="padding:28px;">
        <p style="color:#f5f4f2;font-size:15px;line-height:1.6;margin:0 0 22px;">
          ${name ? 'Hey ' + name + ',' : 'Hey,'} your spot on the Porto Pub Crawl is confirmed. Here's everything you need for Saturday:
        </p>
        <table style="width:100%;border-collapse:collapse;margin-bottom:22px;">
          <tr>
            <td style="padding:10px 0;border-bottom:1px solid #232325;color:#a3a0a1;font-size:12px;text-transform:uppercase;letter-spacing:.04em;">Package</td>
            <td style="padding:10px 0;border-bottom:1px solid #232325;color:#f5f4f2;font-size:14px;text-align:right;font-weight:700;">${packageName}</td>
          </tr>
          <tr>
            <td style="padding:10px 0;border-bottom:1px solid #232325;color:#a3a0a1;font-size:12px;text-transform:uppercase;letter-spacing:.04em;">Date</td>
            <td style="padding:10px 0;border-bottom:1px solid #232325;color:#f5f4f2;font-size:14px;text-align:right;font-weight:700;">${niceDate}</td>
          </tr>
          <tr>
            <td style="padding:10px 0;border-bottom:1px solid #232325;color:#a3a0a1;font-size:12px;text-transform:uppercase;letter-spacing:.04em;">Spots</td>
            <td style="padding:10px 0;border-bottom:1px solid #232325;color:#f5f4f2;font-size:14px;text-align:right;font-weight:700;">${qty}</td>
          </tr>
          <tr>
            <td style="padding:10px 0;border-bottom:1px solid #232325;color:#a3a0a1;font-size:12px;text-transform:uppercase;letter-spacing:.04em;">Meeting point</td>
            <td style="padding:10px 0;border-bottom:1px solid #232325;color:#f5f4f2;font-size:14px;text-align:right;font-weight:700;">Praça de Carlos Alberto</td>
          </tr>
          <tr>
            <td style="padding:10px 0;color:#a3a0a1;font-size:12px;text-transform:uppercase;letter-spacing:.04em;">Time</td>
            <td style="padding:10px 0;color:#f5f4f2;font-size:14px;text-align:right;font-weight:700;">22:30 — look for the pink umbrellas</td>
          </tr>
        </table>
        <p style="color:#a3a0a1;font-size:13px;line-height:1.6;margin:0 0 6px;">
          Questions before Saturday? Message us on WhatsApp: <a href="https://wa.me/351910694984" style="color:#ff5468;">+351 910 694 984</a>
        </p>
        <p style="color:#7e7b7c;font-size:12px;line-height:1.6;margin:22px 0 0;">
          Free cancellation up to 24h before your start time — just reply to this email or WhatsApp us.
        </p>
      </div>
      <div style="padding:18px 28px;background:#0d0d0e;text-align:center;">
        <p style="color:#7e7b7c;font-size:11px;margin:0;">Project P · Porto's most talked-about night out, every Saturday since 2025.</p>
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

    if (email && process.env.RESEND_API_KEY) {
      const packageName = PACKAGE_NAMES[meta.package] || 'Porto Pub Crawl';
      const qty = meta.quantity || '1';
      let niceDate = meta.event_date || '';
      if (meta.event_date) {
        niceDate = new Date(meta.event_date + 'T00:00:00Z').toLocaleDateString('en-GB', {
          weekday: 'long', day: 'numeric', month: 'long', timeZone: 'UTC'
        });
      }

      try {
        const resendRes = await fetch('https://api.resend.com/emails', {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${process.env.RESEND_API_KEY}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            from: 'Porto Pub Crawl <bookings@porto-pubcrawl.com>',
            to: email,
            bcc: 'contact@porto-pubcrawl.com',
            subject: `You're on the list! Saturday, ${niceDate}`,
            html: buildEmailHtml({ name, packageName, niceDate, qty })
          })
        });
        if (!resendRes.ok) {
          const errBody = await resendRes.text();
          console.error('Resend send failed:', resendRes.status, errBody);
        }
      } catch (err) {
        console.error('Error sending confirmation email:', err);
      }
    }
  }

  res.status(200).json({ received: true });
};
