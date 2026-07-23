import { next, rewrite } from '@vercel/edge';

// A/B test: split homepage traffic 50/50 between the current site (variant A =
// index.html) and the new hero (variant B = index-b.html). The assignment is
// sticky per visitor via the `pp_variant` cookie, so returning users always see
// the same version. PostHog tags every event with the variant (see the snippet
// in index.html / index-b.html) so conversions can be compared per variant.
export const config = { matcher: '/' };

export default function middleware(request) {
  const cookieHeader = request.headers.get('cookie') || '';
  const match = cookieHeader.match(/(?:^|;\s*)pp_variant=(a|b)\b/);
  let variant = match ? match[1] : null;
  const assignedNow = !variant;

  if (assignedNow) {
    variant = Math.random() < 0.5 ? 'a' : 'b';
  }

  const response =
    variant === 'b'
      ? rewrite(new URL('/index-b.html', request.url))
      : next();

  if (assignedNow) {
    response.headers.append(
      'set-cookie',
      `pp_variant=${variant}; Path=/; Max-Age=15552000; SameSite=Lax; Secure`
    );
  }
  // Never let the CDN serve one variant's HTML to everyone — decision is per-cookie.
  response.headers.set('cache-control', 'private, no-store');
  response.headers.set('x-pp-variant', variant);
  return response;
}
