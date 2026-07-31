// /api/bookings.js
// Vercel serverless function — the "reservations memory" behind /reservas-3838c6284f.html.
//
// Stripe is already the reliable source of truth for every booking: each paid
// Checkout Session stores the crawl date, package and quantity in its metadata
// (see create-checkout-session.js). Instead of building a separate database we
// simply read those sessions back from Stripe and group them by crawl date, so
// you can see — at a glance — how many reservations (and how many spots) you
// have for each crawl night, without digging through the email inbox.
//
// This endpoint is READ-ONLY and password-protected: it never exposes booking
// data unless the caller sends the correct ADMIN_TOKEN.
//
// SETUP (Vercel dashboard, one-time):
//   1. Project → Settings → Environment Variables
//   2. Add ADMIN_TOKEN = <choose a long private password>
//      (this is the password you'll type into /reservas-3838c6284f.html)
//   3. Redeploy so it's picked up.
//   STRIPE_SECRET_KEY is the same key the checkout already uses — nothing new.

const Stripe = require('stripe');
const crypto = require('crypto');

const PACKAGE_NAMES = {
  crawl: 'Porto Pub Crawl',
  pack: 'Party Boat + Pub Crawl Pack'
};

// Manual corrections, keyed by Stripe Checkout Session id. Some bookings reach
// Stripe with no usable date — e.g. Payment Link bookings carry no event_date —
// or a customer is later moved to a different Saturday. Rather than guess, we
// record the correct values here so the dashboard groups them properly. Each
// entry may set event_date (YYYY-MM-DD), package ('crawl' | 'pack') and/or
// quantity; only the fields present are overridden.
const BOOKING_OVERRIDES = {
  // Gurnoor Gill (noorgill19@gmail.com) — Payment Link booking with no date;
  // confirmed by the organiser as Saturday 25 Jul 2026.
  'cs_live_b1I3ulzzECkg1xUNXlksXGfczkCLd69Z5RDNNx4bDDgo9LdYDNKqHRVXzy': { event_date: '2026-07-25' }
};

// Constant-time compare so the token can't be guessed by timing the response.
function tokensMatch(a, b) {
  if (typeof a !== 'string' || typeof b !== 'string') return false;
  const ba = Buffer.from(a);
  const bb = Buffer.from(b);
  if (ba.length !== bb.length) return false;
  return crypto.timingSafeEqual(ba, bb);
}

// Recover package / event_date / quantity from a session. Embedded checkout
// stores them in metadata; the Payment-Link fallback carries none, so we parse
// the "pkg_date_qty" client_reference_id instead — same logic the webhook uses.
function extractBooking(session) {
  const meta = Object.assign({}, session.metadata || {});
  if (!meta.event_date && session.client_reference_id) {
    const ref = String(session.client_reference_id).split('_');
    if (ref.length >= 3) {
      if (!meta.package && PACKAGE_NAMES[ref[0]]) meta.package = ref[0];
      if (/^\d{4}-\d{2}-\d{2}$/.test(ref[1])) meta.event_date = ref[1];
      if (!meta.quantity && /^\d+$/.test(ref[2])) meta.quantity = ref[2];
    }
  }
  // Apply any manual correction for this session (takes precedence over the
  // above, since it's a deliberate fix by the organiser).
  const override = BOOKING_OVERRIDES[session.id];
  if (override) {
    if (override.event_date) meta.event_date = override.event_date;
    if (override.package) meta.package = override.package;
    if (override.quantity) meta.quantity = String(override.quantity);
  }
  const details = session.customer_details || {};
  const qty = parseInt(meta.quantity, 10);
  const pi = typeof session.payment_intent === 'string'
    ? session.payment_intent
    : (session.payment_intent && session.payment_intent.id) || null;
  return {
    date: /^\d{4}-\d{2}-\d{2}$/.test(meta.event_date || '') ? meta.event_date : null,
    package: meta.package || null,
    packageName: PACKAGE_NAMES[meta.package] || 'Porto Pub Crawl',
    quantity: qty > 0 ? qty : 1,
    name: details.name || '',
    email: details.email || '',
    phone: details.phone || '',
    amount: (session.amount_total || 0) / 100,
    currency: (session.currency || 'eur').toUpperCase(),
    bookedAt: session.created ? new Date(session.created * 1000).toISOString() : null,
    sessionId: session.id,
    paymentIntent: pi,
    // set later once we know which payments were refunded
    refunded: false
  };
}

// Build the set of payment_intent ids that have a succeeded refund since the
// cutoff. Stripe keeps a Checkout Session's payment_status as "paid" even after
// the money is refunded, so without this a cancelled-and-refunded booking would
// keep being counted. One or two list calls total (100 refunds/page), no matter
// how many bookings there are, so it stays cheap as volume grows.
async function fetchRefundedPaymentIntents(stripe, since) {
  const refunded = new Set();
  let startingAfter;
  let guard = 0;
  while (guard < 20) {
    guard++;
    const params = { limit: 100, created: { gte: since } };
    if (startingAfter) params.starting_after = startingAfter;
    const page = await stripe.refunds.list(params);
    for (const r of page.data) {
      if (r.status === 'succeeded' && r.payment_intent) {
        refunded.add(typeof r.payment_intent === 'string' ? r.payment_intent : r.payment_intent.id);
      }
    }
    if (!page.has_more || !page.data.length) break;
    startingAfter = page.data[page.data.length - 1].id;
  }
  return refunded;
}

module.exports = async (req, res) => {
  if (req.method !== 'GET') {
    res.status(405).json({ error: 'Method not allowed' });
    return;
  }
  if (!process.env.STRIPE_SECRET_KEY) {
    res.status(500).json({ error: 'Payments not configured.' });
    return;
  }
  if (!process.env.ADMIN_TOKEN) {
    res.status(503).json({
      error: 'Not configured',
      detail: 'Set an ADMIN_TOKEN environment variable in Vercel to enable the reservations page.'
    });
    return;
  }

  // Accept the token from an Authorization: Bearer header or a ?token= query.
  const authHeader = req.headers['authorization'] || '';
  const bearer = authHeader.startsWith('Bearer ') ? authHeader.slice(7) : '';
  const provided = bearer || (typeof req.query.token === 'string' ? req.query.token : '');
  if (!tokensMatch(provided, process.env.ADMIN_TOKEN)) {
    res.status(401).json({ error: 'Unauthorized' });
    return;
  }

  // How far back to look. Bookings are made in the weeks before an event, so a
  // few months easily covers every upcoming weekend; default 180 days, capped
  // at ~2 years to protect the Stripe API and the function timeout.
  let days = parseInt(req.query.days, 10);
  if (!days || days < 1) days = 180;
  if (days > 730) days = 730;
  const since = Math.floor(Date.now() / 1000) - days * 24 * 60 * 60;

  const stripe = Stripe(process.env.STRIPE_SECRET_KEY);

  try {
    // Page through completed sessions since the cutoff. Cap the number of pages
    // so a huge history can never hang the function (100 sessions/page).
    const bookings = [];
    let startingAfter;
    let guard = 0;
    while (guard < 40) {
      guard++;
      const params = { limit: 100, created: { gte: since } };
      if (startingAfter) params.starting_after = startingAfter;
      const page = await stripe.checkout.sessions.list(params);
      for (const session of page.data) {
        if (session.payment_status === 'paid') bookings.push(extractBooking(session));
      }
      if (!page.has_more || !page.data.length) break;
      startingAfter = page.data[page.data.length - 1].id;
    }

    // Flag bookings whose payment was refunded — Stripe leaves payment_status
    // "paid" after a refund, so we cross-reference the refunds list and mark
    // them so they can be excluded from the active counts.
    const refundedPIs = await fetchRefundedPaymentIntents(stripe, since);
    for (const b of bookings) {
      if (b.paymentIntent && refundedPIs.has(b.paymentIntent)) b.refunded = true;
    }

    const round2 = (n) => Math.round(n * 100) / 100;

    // Group by crawl date. Refunded bookings stay in the list (so they're visible)
    // but never count towards the active spots / bookings / revenue. Sessions
    // with no recoverable date go in their own bucket so nothing is dropped.
    const byDate = new Map();
    const unknown = { spots: 0, bookings: 0, revenue: 0, refundedBookings: 0, refundedSpots: 0, items: [] };

    for (const b of bookings) {
      const bucket = b.date ? null : unknown;
      if (bucket) {
        bucket.items.push(b);
        if (b.refunded) { bucket.refundedBookings += 1; bucket.refundedSpots += b.quantity; }
        else { bucket.spots += b.quantity; bucket.bookings += 1; bucket.revenue += b.amount; }
        continue;
      }
      if (!byDate.has(b.date)) {
        byDate.set(b.date, {
          date: b.date,
          spots: 0,
          bookings: 0,
          revenue: 0,
          refundedBookings: 0,
          refundedSpots: 0,
          packages: {},
          items: []
        });
      }
      const g = byDate.get(b.date);
      g.items.push(b);
      if (b.refunded) {
        g.refundedBookings += 1;
        g.refundedSpots += b.quantity;
        continue; // refunded → excluded from active spots/bookings/revenue/packages
      }
      g.spots += b.quantity;
      g.bookings += 1;
      g.revenue += b.amount;
      const pk = b.package || 'crawl';
      if (!g.packages[pk]) g.packages[pk] = { name: b.packageName, spots: 0, bookings: 0 };
      g.packages[pk].spots += b.quantity;
      g.packages[pk].bookings += 1;
    }

    const weekends = Array.from(byDate.values()).sort((a, b) => a.date.localeCompare(b.date));
    for (const w of weekends) {
      w.label = new Date(w.date + 'T00:00:00Z').toLocaleDateString('en-GB', {
        weekday: 'long', day: 'numeric', month: 'long', year: 'numeric', timeZone: 'UTC'
      });
      w.revenue = round2(w.revenue);
      w.items.sort((a, b) => (b.bookedAt || '').localeCompare(a.bookedAt || ''));
    }
    unknown.revenue = round2(unknown.revenue);
    unknown.items.sort((a, b) => (b.bookedAt || '').localeCompare(a.bookedAt || ''));

    const active = bookings.filter((b) => !b.refunded);
    const refundedList = bookings.filter((b) => b.refunded);
    const totals = {
      weekends: weekends.length,
      bookings: active.length,
      spots: active.reduce((s, b) => s + b.quantity, 0),
      revenue: round2(active.reduce((s, b) => s + b.amount, 0)),
      refundedBookings: refundedList.length,
      refundedSpots: refundedList.reduce((s, b) => s + b.quantity, 0)
    };

    // No caching — this is live booking data behind a token.
    res.setHeader('Cache-Control', 'no-store');
    res.status(200).json({
      generatedAt: new Date().toISOString(),
      lookbackDays: days,
      currency: 'EUR',
      totals,
      weekends,
      unknown
    });
  } catch (err) {
    console.error('bookings endpoint error:', err);
    res.status(500).json({ error: 'Could not load bookings.' });
  }
};

// Exposed for unit testing only. Vercel invokes the default export (the handler
// function above); attaching helpers as properties on it changes nothing at
// runtime but lets the grouping/refund logic be verified against real data.
module.exports.extractBooking = extractBooking;
