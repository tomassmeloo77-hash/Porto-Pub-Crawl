// /functions/api/create-checkout-session.js
// Cloudflare Pages Function equivalent of /api/create-checkout-session.js —
// same embedded-checkout behaviour, for projects deployed on Cloudflare
// Pages with Functions enabled (Git-connected deploy, not a plain static
// "Workers assets only" upload — that mode can't run this file or accept
// environment variables, and the site will fall back to Payment Links
// automatically in that case).
//
// SETUP (Cloudflare dashboard, one-time):
// 1. Workers & Pages → your project → Settings → Environment variables
// 2. Add STRIPE_SECRET_KEY = sk_live_xxxxxxxx (use sk_test_xxxxxxxx to test)
// 3. Add SITE_URL = https://your-project.pages.dev
// 4. Settings → Functions → Compatibility flags → add: nodejs_compat
// 5. Deployments → Retry deployment

import Stripe from 'stripe';

const PRICES_EUR = { crawl: 17, pack: 44 };
const MAX_QTY = 100;

export async function onRequestPost({ request, env }) {
  const jsonHeaders = { 'Content-Type': 'application/json' };

  if (!env.STRIPE_SECRET_KEY) {
    return new Response(JSON.stringify({ error: 'Payments not configured yet.' }), { status: 500, headers: jsonHeaders });
  }

  let body;
  try { body = await request.json(); }
  catch (e) { return new Response(JSON.stringify({ error: 'Invalid request.' }), { status: 400, headers: jsonHeaders }); }

  const { package: pkg, packageName, date, quantity } = body || {};

  if (!PRICES_EUR[pkg]) return new Response(JSON.stringify({ error: 'Invalid package.' }), { status: 400, headers: jsonHeaders });
  const qty = parseInt(quantity, 10);
  if (!qty || qty < 1 || qty > MAX_QTY) return new Response(JSON.stringify({ error: 'Invalid quantity.' }), { status: 400, headers: jsonHeaders });
  if (!date || !/^\d{4}-\d{2}-\d{2}$/.test(date)) return new Response(JSON.stringify({ error: 'Invalid date.' }), { status: 400, headers: jsonHeaders });

  try {
    const stripe = new Stripe(env.STRIPE_SECRET_KEY, { httpClient: Stripe.createFetchHttpClient() });
    const siteUrl = env.SITE_URL || new URL(request.url).origin;
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

    return new Response(JSON.stringify({ clientSecret: session.client_secret }), { status: 200, headers: jsonHeaders });
  } catch (err) {
    console.error('Stripe embedded checkout error:', err);
    return new Response(JSON.stringify({ error: 'Could not start checkout.' }), { status: 500, headers: jsonHeaders });
  }
}
