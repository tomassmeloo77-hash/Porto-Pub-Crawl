// /api/get-session-amount.js
// Vercel serverless function — after a customer returns from a successful
// payment, the success page calls this to find out exactly how much was
// paid (including any optional add-ons they chose), so the Google Ads
// conversion tag reports an accurate value instead of a guess.
//
// Safe to call publicly: it only returns the amount/currency for a specific
// session ID that the browser already has (from the return_url) — no
// sensitive data, and it can't be used to look up sessions you don't
// already know the ID of.

const Stripe = require('stripe');

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
    res.status(200).json({
      amount: (session.amount_total || 0) / 100,
      currency: (session.currency || 'eur').toUpperCase()
    });
  } catch (err) {
    console.error('get-session-amount error:', err);
    res.status(500).json({ error: 'Could not retrieve session' });
  }
};
