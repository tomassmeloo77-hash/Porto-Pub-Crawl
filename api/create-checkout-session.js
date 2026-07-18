// /api/create-checkout-session.js
// Vercel serverless function — creates a Stripe Checkout Session in
// "embedded" mode and returns its client_secret, so the payment form
// can be mounted directly inside a popup on your own site (no redirect
// to a separate Stripe-hosted page).
//
// SETUP (Vercel dashboard, one-time):
// 1. Project → Settings → Environment Variables
// 2. Add STRIPE_SECRET_KEY = sk_live_xxxxxxxx (use sk_test_xxxxxxxx to test)
// 3. Add SITE_URL = https://www.porto-pubcrawl.com (no trailing slash)
// 4. Redeploy after saving (env vars are only picked up on a new deploy)
//
// If this function isn't reachable (e.g. deployed on plain static
// hosting with no serverless functions), the website automatically
// falls back to your Stripe Payment Links instead — booking still works
// either way.

const Stripe = require('stripe');

const PRICES_EUR = { crawl: 17, pack: 44 };
const MAX_QTY = 100;
// Per-package checkout subtitle — the pack has its own itinerary (boat first at
// Cais de Gaia, then the crawl), so it must not reuse the crawl's line.
const DESCRIPTIONS = {
  crawl: 'Porto Pub Crawl · Praça de Carlos Alberto · 22:30–02:30',
  pack: 'Party Boat · Cais de Gaia · 22:00, then Pub Crawl · Praça de Carlos Alberto · 00:30'
};

module.exports = async (req, res) => {
  if (req.method !== 'POST') {
    res.status(405).json({ error: 'Method not allowed' });
    return;
  }
  if (!process.env.STRIPE_SECRET_KEY) {
    res.status(500).json({ error: 'Payments not configured yet.' });
    return;
  }

  const stripe = Stripe(process.env.STRIPE_SECRET_KEY);

  try {
    const body = typeof req.body === 'string' ? JSON.parse(req.body) : (req.body || {});
    const { package: pkg, packageName, date, quantity, flex, fbp, fbc, event_source_url } = body;

    if (!PRICES_EUR[pkg]) { res.status(400).json({ error: 'Invalid package.' }); return; }
    const qty = parseInt(quantity, 10);
    if (!qty || qty < 1 || qty > MAX_QTY) { res.status(400).json({ error: 'Invalid quantity.' }); return; }
    if (!date || !/^\d{4}-\d{2}-\d{2}$/.test(date)) { res.status(400).json({ error: 'Invalid date.' }); return; }
    const parsedDate = new Date(date + 'T00:00:00Z');
    if (isNaN(parsedDate.getTime())) { res.status(400).json({ error: 'Invalid date.' }); return; }
    // Bookable until ~03:00 (Lisbon) the day AFTER the Saturday crawl, so tickets
    // still sell during and just after the event. parsedDate is the Saturday at
    // 00:00 UTC; + 27h ≈ Sunday 03:00 UTC (≈ 03:00–04:00 Lisbon depending on DST —
    // we err a touch late rather than cut sales off early).
    if (Date.now() > parsedDate.getTime() + 27 * 60 * 60 * 1000) {
      res.status(400).json({ error: 'That date has already passed.' }); return;
    }
    if (parsedDate.getUTCDay() !== 6) { res.status(400).json({ error: 'The crawl only runs on Saturdays.' }); return; }

    const siteUrl = process.env.SITE_URL || 'https://www.porto-pubcrawl.com';
    const niceDate = new Date(date + 'T00:00:00Z').toLocaleDateString('en-GB', {
      weekday: 'long', day: 'numeric', month: 'long', timeZone: 'UTC'
    });

    // Base ticket line item — always present.
    const lineItems = [
      {
        price_data: {
          currency: 'eur',
          unit_amount: PRICES_EUR[pkg] * 100,
          tax_behavior: 'exclusive',
          product_data: {
            name: (packageName || pkg) + ' — ' + niceDate,
            description: DESCRIPTIONS[pkg] || DESCRIPTIONS.crawl
          }
        },
        quantity: qty
      }
    ];

    // "Book with Confidence" is now an explicit opt-in on the booking modal — we
    // only add it here when the customer ticked it, so the Stripe total always
    // matches the total they saw in the modal (no surprise add-on at payment).
    // Offered on the Pub Crawl only, never on the Party Boat + Pub Crawl pack.
    if (flex === true && pkg === 'crawl') {
      lineItems.push({
        price_data: {
          currency: 'eur',
          unit_amount: 190,
          tax_behavior: 'exclusive',
          product_data: {
            name: 'Book with Confidence',
            description: 'Cancel or reschedule up to 3 hours before the event. No questions asked.'
          }
        },
        quantity: qty
      });
    }

    const session = await stripe.checkout.sessions.create({
      ui_mode: 'embedded',
      payment_method_types: ['card'],
      mode: 'payment',
      line_items: lineItems,
      // We stash Meta's match identifiers (fbp/fbc) plus the visitor's IP and
      // user-agent here so the Stripe webhook can fire a server-side Meta
      // Conversions API "Purchase" event that Meta can attribute back to the ad.
      // Stripe caps each metadata value at 500 chars — the user-agent is sliced
      // to stay safely under that.
      metadata: {
        package: pkg,
        event_date: date,
        quantity: String(qty),
        fbp: fbp || '',
        fbc: fbc || '',
        event_source_url: event_source_url || '',
        client_ip: (req.headers['x-forwarded-for'] || '').split(',')[0].trim(),
        client_ua: (req.headers['user-agent'] || '').slice(0, 480)
      },
      return_url: siteUrl + '/?booking=success&session_id={CHECKOUT_SESSION_ID}'
    });

    res.status(200).json({ clientSecret: session.client_secret });
  } catch (err) {
    console.error('Stripe embedded checkout error:', err);
    res.status(500).json({ error: 'Could not start checkout.' });
  }
};
