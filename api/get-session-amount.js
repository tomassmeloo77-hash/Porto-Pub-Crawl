// /api/get-session-amount.js
// Vercel serverless function — after a customer returns from a successful
// payment, the success page calls this to find out exactly how much was
// paid (including any optional add-ons they chose), so the Google Ads
// conversion tag reports an accurate value instead of a guess.
//
// Safe to call publicly: it only returns the amount/currency for a specific
// session ID that the browser already has (from the return_url) — no raw
// sensitive data, and it can't be used to look up sessions you don't
// already know the ID of. The email/phone are returned only as one-way
// SHA-256 hashes (for Google Ads enhanced conversions), never in the clear.

const Stripe = require('stripe');
const crypto = require('crypto');

function sha256(value) {
  return crypto.createHash('sha256').update(value).digest('hex');
}

// Normalize + hash an email for Google Ads enhanced conversions:
// trim and lowercase, then SHA-256. Returns null for empty/invalid input.
function hashEmail(email) {
  if (!email || typeof email !== 'string') return null;
  const normalized = email.trim().toLowerCase();
  if (!normalized) return null;
  return sha256(normalized);
}

// Normalize + hash a phone number to E.164 shape (digits with a leading +),
// then SHA-256. Returns null when there is no usable number.
function hashPhone(phone) {
  if (!phone || typeof phone !== 'string') return null;
  let normalized = phone.trim().replace(/[^0-9+]/g, '');
  if (normalized && normalized[0] !== '+') normalized = '+' + normalized;
  if (normalized.replace(/\D/g, '').length < 6) return null;
  return sha256(normalized);
}

module.exports = async (req, res) => {
  if (req.method !== 'GET') {
    res.status(405).json({ error: 'Method not allowed' });
    return;
  }
  if (!process.env.STRIPE_SECRET_KEY) {
    res.status(500).json({ error: 'Not configured' });
    return;
  }

  const sessionId = req.query.session_id;
  if (!sessionId || typeof sessionId !== 'string' || !sessionId.startsWith('cs_')) {
    res.status(400).json({ error: 'Invalid session_id' });
    return;
  }

  try {
    const stripe = Stripe(process.env.STRIPE_SECRET_KEY);
    const session = await stripe.checkout.sessions.retrieve(sessionId);
    // Only treat the session as a real sale when Stripe says it's paid — a
    // session id alone (e.g. an abandoned/open checkout whose success URL was
    // shared or bookmarked) must not fire conversion pixels for money that
    // never actually came in.
    const paid = session.payment_status === 'paid';
    const details = session.customer_details || {};
    res.status(200).json({
      paid: paid,
      amount: paid ? (session.amount_total || 0) / 100 : 0,
      currency: (session.currency || 'eur').toUpperCase(),
      // Hashed customer identifiers for enhanced conversions — only for a
      // genuinely paid session, and only ever as irreversible SHA-256 digests.
      email_sha256: paid ? hashEmail(details.email) : null,
      phone_sha256: paid ? hashPhone(details.phone) : null
    });
  } catch (err) {
    console.error('get-session-amount error:', err);
    res.status(500).json({ error: 'Could not retrieve session' });
  }
};
