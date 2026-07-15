// /api/create-checkout-session.js
// Vercel serverless function — creates a Stripe Checkout Session in
// "embedded" mode and returns its client_secret, so the payment form
// can be mounted directly inside a popup on your own site (no redirect
// to a separate Stripe-hosted page).
//
// SETUP (Vercel dashboard, one-time):
// 1. Project → Settings → Environment Variables
// 2. Add STRIPE_SECRET_KEY = sk_live_xxxxxxxx (use sk_test_xxxxxxxx to test)
// 3. Add SITE_URL = https://porto-pubcrawl.com (no trailing slash)
// 4. Redeploy after saving (env vars are only picked up on a new deploy)
//
// If this function isn't reachable (e.g. deployed on plain static
// hosting with no serverless functions), the website automatically
// falls back to your Stripe Payment Links instead — booking still works
// either way.

const Stripe = require('stripe');

const PRICES_EUR = { crawl: 17, pack: 44 };
const MAX_QTY = 100;

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
    const { package: pkg, packageName, date, quantity } = body;

    if (!PRICES_EUR[pkg]) { res.status(400).json({ error: 'Invalid package.' }); return; }
    const qty = parseInt(quantity, 10);
    if (!qty || qty < 1 || qty > MAX_QTY) { res.status(400).json({ error: 'Invalid quantity.' }); return; }
    if (!date || !/^\d{4}-\d{2}-\d{2}$/.test(date)) { res.status(400).json({ error: 'Invalid date.' }); return; }

    const siteUrl = process.env.SITE_URL || 'https://porto-pubcrawl.com';
    const niceDate = new Date(date + 'T00:00:00Z').toLocaleDateString('en-GB', {
      weekday: 'long', day: 'numeric', month: 'long', timeZone: 'UTC'
    });

    const session = await stripe.checkout.sessions.create({
      ui_mode: 'embedded',
      mode: 'payment',
      line_items: [{
        price_data: {
          currency: 'eur',
          unit_amount: PRICES_EUR[pkg] * 100,
          product_data: {
            name: (packageName || pkg) + ' — Saturday ' + niceDate,
            description: 'Porto Pub Crawl · Praça de Carlos Alberto · 22:30–02:30'
          }
        },
        quantity: qty
      }],
      metadata: { package: pkg, event_date: date, quantity: String(qty) },
      return_url: siteUrl + '/?booking=success&session_id={CHECKOUT_SESSION_ID}'
    });

    res.status(200).json({ clientSecret: session.client_secret });
  } catch (err) {
    console.error('Stripe embedded checkout error:', err);
    res.status(500).json({ error: 'Could not start checkout.' });
  }
};
