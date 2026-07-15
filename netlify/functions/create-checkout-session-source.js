// /netlify/functions/create-checkout-session.js
// Netlify Function — creates a Stripe Checkout Session in "embedded" mode
// and returns its client_secret, so the payment form mounts directly
// inside the popup on your own site (no redirect to a separate page).
//
// The frontend calls this via /api/create-checkout-session — see the
// redirect rule in netlify.toml that maps that path to this function.
//
// NOTE: this file is the readable SOURCE. The file that actually gets
// deployed is the bundled version (same filename) which has the "stripe"
// package inlined, because Netlify's drag-and-drop / manual deploys don't
// run "npm install". If you edit this file, ask Claude to re-bundle it
// with esbuild before deploying, or just push through Git (which does
// run npm install and would work with this unbundled version too).
//
// SETUP (Netlify dashboard, one-time, all free on the Netlify Free plan):
// 1. Site configuration → Environment variables → Add STRIPE_SECRET_KEY
//    (sk_test_xxxxxxxx to test, sk_live_xxxxxxxx once you go live)
// 2. Add SITE_URL = https://your-site-name.netlify.app, no trailing slash
// 3. Trigger a new deploy after saving (env vars are only picked up then)
//
// For the checkout page to look "on brand", set your logo and colors in
// the Stripe Dashboard → Settings → Branding — Stripe applies that
// automatically to embedded and hosted Checkout, there's no CSS override
// available from code for this UI mode.
//
// If this function isn't reachable for any reason, the website automatically
// falls back to your Stripe Payment Links — booking still works either way.

const Stripe = require('stripe');

const PRICES_EUR = { crawl: 17, pack: 44 };
const MAX_QTY = 100;

exports.handler = async (event) => {
  const jsonHeaders = { 'Content-Type': 'application/json' };

  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, headers: jsonHeaders, body: JSON.stringify({ error: 'Method not allowed' }) };
  }
  if (!process.env.STRIPE_SECRET_KEY) {
    return { statusCode: 500, headers: jsonHeaders, body: JSON.stringify({ error: 'Payments not configured yet.' }) };
  }

  let body;
  try {
    body = JSON.parse(event.body || '{}');
  } catch (e) {
    return { statusCode: 400, headers: jsonHeaders, body: JSON.stringify({ error: 'Invalid request.' }) };
  }

  const { package: pkg, packageName, date, quantity } = body;

  if (!PRICES_EUR[pkg]) {
    return { statusCode: 400, headers: jsonHeaders, body: JSON.stringify({ error: 'Invalid package.' }) };
  }
  const qty = parseInt(quantity, 10);
  if (!qty || qty < 1 || qty > MAX_QTY) {
    return { statusCode: 400, headers: jsonHeaders, body: JSON.stringify({ error: 'Invalid quantity.' }) };
  }
  if (!date || !/^\d{4}-\d{2}-\d{2}$/.test(date)) {
    return { statusCode: 400, headers: jsonHeaders, body: JSON.stringify({ error: 'Invalid date.' }) };
  }

  try {
    const stripe = Stripe(process.env.STRIPE_SECRET_KEY);
    const siteUrl = process.env.SITE_URL || 'https://porto-pubcrawl.com';
    const niceDate = new Date(date + 'T00:00:00Z').toLocaleDateString('en-GB', {
      weekday: 'long', day: 'numeric', month: 'long', timeZone: 'UTC'
    });

    const session = await stripe.checkout.sessions.create({
      ui_mode: 'embedded',
      payment_method_types: ['card'],
      mode: 'payment',
      line_items: [
        {
          price_data: {
            currency: 'eur',
            unit_amount: PRICES_EUR[pkg] * 100,
            tax_behavior: 'exclusive',
            product_data: {
              name: (packageName || pkg) + ' — Saturday ' + niceDate,
              description: 'Porto Pub Crawl · Praça de Carlos Alberto · 22:30–02:30'
            }
          },
          quantity: qty
        },
        {
          price_data: {
            currency: 'eur',
            unit_amount: 190,
            tax_behavior: 'exclusive',
            product_data: {
              name: 'Book with Confidence (Recommended)',
              description: 'Cancel or reschedule up to 3 hours before the event. No questions asked.'
            }
          },
          quantity: qty,
          adjustable_quantity: { enabled: true, minimum: 0, maximum: MAX_QTY }
        }
      ],
      metadata: { package: pkg, event_date: date, quantity: String(qty) },
      return_url: siteUrl + '/?booking=success&session_id={CHECKOUT_SESSION_ID}'
    });

    return { statusCode: 200, headers: jsonHeaders, body: JSON.stringify({ clientSecret: session.client_secret }) };
  } catch (err) {
    console.error('Stripe embedded checkout error:', err);
    return { statusCode: 500, headers: jsonHeaders, body: JSON.stringify({ error: 'Could not start checkout.' }) };
  }
};
