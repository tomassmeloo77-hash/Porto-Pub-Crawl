#!/usr/bin/env python3
import pathlib

base = pathlib.Path("/home/user/Porto-Pub-Crawl/scratch-preview")
def uri(name): return (base / name).read_text().strip()

HERO = uri("img_hero.txt")
BOAT = uri("img_boat.txt")
CLUB = uri("img_club.txt")
FRIENDS = uri("img_friends.txt")
VODKA = uri("img_vodka.txt")

html = r"""<style>
:root{
  --void:#08070a; --void-2:#0e0c10;
  --pink:#ff173f; --pink-soft:#ff5468;
  --violet:#7a0a1f; --violet-deep:#3c0512;
  --gold:#ffc466; --cream:#f5f4f2;
  --muted:#a3a0a1; --muted-2:#7e7b7c;
  --line:rgba(245,244,242,0.09); --line-strong:rgba(245,244,242,0.16);
  --disp:'Anton', Impact, 'Haettenschweiler', 'Arial Narrow Bold', sans-serif;
  --grote:'Helvetica Neue', Arial, sans-serif;
  --body:'Manrope', system-ui, -apple-system, sans-serif;
  --mono:'Space Mono', ui-monospace, 'SF Mono', Menlo, monospace;
}
*{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;}
body{background:#050406;color:var(--cream);font-family:var(--body);-webkit-font-smoothing:antialiased;line-height:1.5;}
img{display:block;max-width:100%;}
a{color:inherit;text-decoration:none;}

/* ===== showcase chrome ===== */
.page-head{
  position:sticky;top:0;z-index:50;backdrop-filter:blur(14px);
  background:rgba(5,4,6,0.82);border-bottom:1px solid var(--line);
  padding:18px clamp(18px,5vw,60px);display:flex;flex-wrap:wrap;gap:16px 26px;align-items:center;
}
.page-head .brand{font-family:var(--mono);font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);}
.page-head .brand b{color:var(--pink);}
.page-head h1{font-family:var(--grote);font-weight:800;font-size:clamp(15px,2.4vw,19px);letter-spacing:-0.01em;}
.page-head .jump{margin-left:auto;display:flex;gap:8px;flex-wrap:wrap;}
.page-head .jump a{
  font-family:var(--mono);font-size:11px;letter-spacing:.08em;color:var(--muted);
  border:1px solid var(--line-strong);border-radius:100px;padding:6px 12px;transition:.2s;
}
.page-head .jump a:hover{color:var(--cream);border-color:var(--pink);background:rgba(255,23,63,.1);}

.intro{padding:clamp(30px,6vw,64px) clamp(18px,5vw,60px) 8px;max-width:820px;}
.intro p{color:var(--muted);font-size:15px;line-height:1.7;}
.intro .note{margin-top:14px;font-family:var(--mono);font-size:11.5px;letter-spacing:.03em;color:var(--muted-2);
  border-left:2px solid var(--pink);padding-left:12px;}

.variant{padding:clamp(30px,5vw,58px) clamp(18px,5vw,60px);}
.variant + .variant{border-top:1px solid var(--line);}
.v-label{display:flex;flex-wrap:wrap;align-items:baseline;gap:12px 18px;margin-bottom:20px;}
.v-num{font-family:var(--disp);font-size:clamp(30px,5vw,46px);line-height:.8;color:var(--pink);letter-spacing:.02em;}
.v-name{font-family:var(--grote);font-weight:800;font-size:clamp(17px,2.6vw,23px);letter-spacing:-0.01em;}
.v-desc{color:var(--muted);font-size:13.5px;max-width:640px;flex-basis:100%;}

/* frame that holds each hero mock */
.frame{
  position:relative;border-radius:20px;overflow:hidden;border:1px solid var(--line-strong);
  box-shadow:0 40px 90px -40px rgba(0,0,0,.9);
  aspect-ratio:16/10;min-height:520px;background:var(--void);
}
@media(max-width:720px){ .frame{aspect-ratio:9/15;min-height:600px;} }

.hero{position:absolute;inset:0;overflow:hidden;}
.hbg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;}
.hcontent{position:relative;z-index:5;height:100%;}
.btn{
  display:inline-flex;align-items:center;gap:9px;font-family:var(--body);font-weight:800;
  font-size:13.5px;letter-spacing:.01em;padding:15px 26px;border-radius:100px;cursor:pointer;
  transition:transform .25s, box-shadow .25s;white-space:nowrap;
}
.btn:hover{transform:translateY(-2px);}
.btn-primary{background:linear-gradient(135deg,var(--pink),#ff5a8f 55%,var(--violet));color:#fff;
  box-shadow:0 14px 34px -12px rgba(255,23,63,.75);}
.btn-ghost{border:1.5px solid var(--line-strong);color:var(--cream);background:rgba(255,255,255,.04);backdrop-filter:blur(8px);}
.btn-ghost:hover{border-color:var(--pink);background:rgba(255,23,63,.1);}
.btn svg{width:16px;height:16px;}
.stars{color:var(--gold);letter-spacing:2px;}

/* ============================================================
   V1 — CINEMATIC BOTTOM-WEIGHTED
   ============================================================ */
.v1 .hbg{object-position:center 40%;filter:brightness(.82) saturate(1.1);}
.v1 .grad{position:absolute;inset:0;z-index:1;
  background:linear-gradient(180deg,rgba(5,4,6,.55) 0%,transparent 28%,transparent 46%,rgba(5,4,6,.72) 78%,rgba(5,4,6,.96) 100%);}
.v1 .hcontent{display:flex;flex-direction:column;justify-content:flex-end;padding:clamp(26px,4vw,56px);}
.v1 .kicker{font-family:var(--mono);font-size:12px;letter-spacing:.28em;text-transform:uppercase;color:var(--pink-soft);margin-bottom:18px;}
.v1 h2{font-family:var(--disp);text-transform:uppercase;font-weight:400;
  font-size:clamp(46px,8.5vw,118px);line-height:.88;letter-spacing:.005em;color:#fff;
  text-shadow:0 6px 40px rgba(0,0,0,.5);text-wrap:balance;}
.v1 h2 em{font-style:normal;color:var(--pink);}
.v1 .sub{margin-top:20px;max-width:480px;font-size:15.5px;color:#e9e7e8;line-height:1.55;}
.v1 .row{display:flex;flex-wrap:wrap;align-items:center;gap:16px;margin-top:28px;}
.v1 .rate{display:flex;align-items:center;gap:9px;font-size:13px;color:#fff;}
.v1 .rate b{font-family:var(--disp);font-weight:400;font-size:19px;letter-spacing:.02em;}
.v1 .chip{position:absolute;top:clamp(20px,3vw,34px);right:clamp(20px,3vw,34px);z-index:6;
  display:flex;align-items:center;gap:9px;background:rgba(8,7,10,.5);backdrop-filter:blur(10px);
  border:1px solid var(--line-strong);border-radius:100px;padding:9px 15px;font-size:12px;color:var(--cream);}
.v1 .dot{width:8px;height:8px;border-radius:50%;background:#22ff7a;box-shadow:0 0 12px #22ff7a;animation:pulse 1.8s infinite;}
@keyframes pulse{0%,100%{opacity:1;transform:scale(1);}50%{opacity:.45;transform:scale(.7);}}

/* ============================================================
   V2 — SPLIT EDITORIAL POSTER
   ============================================================ */
.v2 .hero{display:grid;grid-template-columns:1.05fr .95fr;background:var(--void);}
@media(max-width:720px){.v2 .hero{grid-template-columns:1fr;grid-template-rows:1fr 1fr;}}
.v2 .left{position:relative;padding:clamp(26px,3.5vw,52px);display:flex;flex-direction:column;justify-content:space-between;
  background:radial-gradient(ellipse 80% 60% at 15% 10%,rgba(255,23,63,.16),transparent 60%),var(--void);}
.v2 .tag{font-family:var(--mono);font-size:11.5px;letter-spacing:.2em;text-transform:uppercase;color:var(--muted);
  display:inline-flex;align-items:center;gap:8px;}
.v2 .tag::before{content:"";width:26px;height:1px;background:var(--pink);}
.v2 h2{font-family:var(--disp);text-transform:uppercase;font-weight:400;color:#fff;
  font-size:clamp(44px,7vw,96px);line-height:.86;letter-spacing:.01em;margin:22px 0;text-wrap:balance;}
.v2 h2 span{display:block;color:var(--pink);
  -webkit-text-stroke:1.4px var(--pink);color:transparent;}
.v2 .sub{color:var(--muted);font-size:14.5px;max-width:340px;line-height:1.6;margin-bottom:26px;}
.v2 .cta{display:flex;gap:12px;flex-wrap:wrap;}
.v2 .facts{margin-top:auto;display:flex;gap:26px;flex-wrap:wrap;padding-top:26px;border-top:1px solid var(--line);}
.v2 .fact b{font-family:var(--disp);font-weight:400;font-size:26px;color:var(--gold);display:block;line-height:1;}
.v2 .fact span{font-size:11px;color:var(--muted-2);letter-spacing:.04em;}
.v2 .right{position:relative;overflow:hidden;}
.v2 .right img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:saturate(1.12) contrast(1.03);}
.v2 .right::after{content:"";position:absolute;inset:0;background:linear-gradient(200deg,transparent 55%,rgba(8,7,10,.5));}
.v2 .badge{position:absolute;z-index:3;bottom:22px;left:22px;background:var(--pink);color:#fff;
  font-family:var(--mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase;padding:8px 14px;border-radius:100px;
  box-shadow:0 10px 30px -8px rgba(255,23,63,.8);}

/* ============================================================
   V3 — NEON GLASS FLYER
   ============================================================ */
.v3 .hbg{filter:brightness(.42) saturate(1.2) blur(1px);object-position:center 45%;}
.v3 .grad{position:absolute;inset:0;z-index:1;
  background:radial-gradient(ellipse 60% 55% at 50% 42%,rgba(255,23,63,.28),transparent 62%),rgba(5,4,6,.55);}
.v3 .hcontent{display:flex;align-items:center;justify-content:center;padding:clamp(22px,4vw,50px);}
.v3 .card{
  position:relative;max-width:640px;width:100%;text-align:center;padding:clamp(30px,4vw,52px);
  border-radius:22px;background:linear-gradient(180deg,rgba(20,16,22,.66),rgba(8,7,10,.6));
  border:1px solid rgba(255,84,104,.4);backdrop-filter:blur(18px);
  box-shadow:0 0 0 1px rgba(255,255,255,.03),0 30px 80px -30px rgba(0,0,0,.9),0 0 60px -18px rgba(255,23,63,.5);}
.v3 .eye{display:inline-flex;align-items:center;gap:8px;font-family:var(--mono);font-size:11.5px;letter-spacing:.16em;
  text-transform:uppercase;color:var(--pink-soft);border:1px solid rgba(255,84,104,.35);border-radius:100px;padding:6px 14px;margin-bottom:22px;}
.v3 .eye .dot{width:7px;height:7px;border-radius:50%;background:#22ff7a;box-shadow:0 0 10px #22ff7a;animation:pulse 1.8s infinite;}
.v3 h2{font-family:var(--disp);text-transform:uppercase;font-weight:400;color:#fff;
  font-size:clamp(42px,7vw,88px);line-height:.9;letter-spacing:.01em;text-wrap:balance;}
.v3 h2 em{font-style:normal;
  background:linear-gradient(100deg,var(--pink),#fff 50%,var(--pink));-webkit-background-clip:text;background-clip:text;color:transparent;}
.v3 .sub{margin:20px auto 0;max-width:400px;color:#e2dfe0;font-size:14.5px;}
.v3 .cta{margin-top:28px;display:flex;justify-content:center;gap:14px;flex-wrap:wrap;}
.v3 .meta{margin-top:24px;display:flex;justify-content:center;gap:22px;flex-wrap:wrap;font-size:12px;color:var(--muted);}
.v3 .meta b{color:var(--cream);}

/* ============================================================
   V4 — OVERSIZED TYPE + MARQUEE
   ============================================================ */
.v4 .hero{background:radial-gradient(ellipse 70% 60% at 80% 15%,rgba(255,23,63,.2),transparent 55%),var(--void);
  display:flex;flex-direction:column;}
.v4 .top{flex:1;position:relative;display:flex;flex-direction:column;justify-content:center;padding:clamp(24px,4vw,54px);}
.v4 .type{position:relative;z-index:3;}
.v4 .type .l{font-family:var(--disp);text-transform:uppercase;font-weight:400;line-height:.82;letter-spacing:.01em;color:#fff;
  font-size:clamp(52px,13vw,190px);}
.v4 .type .l.out{color:transparent;-webkit-text-stroke:1.6px rgba(245,244,242,.55);}
.v4 .type .l.fill{color:var(--pink);}
.v4 .photo{position:absolute;z-index:2;right:clamp(20px,4vw,70px);top:50%;transform:translateY(-50%);
  width:clamp(180px,30vw,380px);aspect-ratio:3/4;border-radius:14px;overflow:hidden;
  border:1px solid var(--line-strong);box-shadow:0 30px 70px -25px rgba(0,0,0,.9);}
.v4 .photo img{width:100%;height:100%;object-fit:cover;filter:saturate(1.15) contrast(1.05);}
@media(max-width:720px){.v4 .photo{position:static;transform:none;margin:20px 0 0;width:100%;aspect-ratio:16/10;}}
.v4 .lead{position:relative;z-index:3;margin-top:24px;max-width:420px;color:var(--muted);font-size:15px;}
.v4 .lead .cta{margin-top:20px;}
.v4 .marquee{overflow:hidden;border-top:1px solid var(--line);border-bottom:1px solid var(--line);
  background:var(--pink);padding:12px 0;}
.v4 .track{display:flex;gap:34px;white-space:nowrap;width:max-content;animation:scroll-x 22s linear infinite;}
.v4 .track span{font-family:var(--disp);text-transform:uppercase;font-weight:400;font-size:19px;letter-spacing:.05em;color:#fff;display:inline-flex;align-items:center;gap:34px;}
.v4 .track span::after{content:"●";color:rgba(255,255,255,.6);font-size:10px;}
@keyframes scroll-x{from{transform:translateX(0);}to{transform:translateX(-50%);}}

/* ============================================================
   V5 — EVENT TICKET / WRISTBAND
   ============================================================ */
.v5 .hero{background:
  radial-gradient(ellipse 60% 50% at 20% 90%,rgba(122,10,31,.4),transparent 60%),
  radial-gradient(ellipse 50% 45% at 85% 10%,rgba(255,23,63,.18),transparent 60%),var(--void);
  display:flex;align-items:center;justify-content:center;padding:clamp(24px,4vw,50px);}
.v5 .ticket{display:grid;grid-template-columns:1.5fr 1fr;max-width:820px;width:100%;
  background:var(--void-2);border:1px solid var(--line-strong);border-radius:20px;overflow:hidden;
  box-shadow:0 40px 100px -40px rgba(0,0,0,.95);}
@media(max-width:720px){.v5 .ticket{grid-template-columns:1fr;}}
.v5 .main{padding:clamp(26px,3.5vw,46px);position:relative;}
.v5 .top-row{display:flex;justify-content:space-between;align-items:center;font-family:var(--mono);font-size:11px;
  letter-spacing:.16em;text-transform:uppercase;color:var(--muted);margin-bottom:26px;}
.v5 .top-row .adm{color:var(--pink);}
.v5 h2{font-family:var(--disp);text-transform:uppercase;font-weight:400;color:#fff;
  font-size:clamp(40px,6.5vw,82px);line-height:.86;letter-spacing:.01em;text-wrap:balance;}
.v5 h2 em{font-style:normal;color:var(--gold);}
.v5 .sub{margin-top:18px;color:var(--muted);font-size:14px;max-width:360px;}
.v5 .detail{margin:26px 0;display:flex;gap:28px;flex-wrap:wrap;}
.v5 .detail .d b{display:block;font-family:var(--disp);font-weight:400;font-size:20px;color:var(--cream);line-height:1;}
.v5 .detail .d span{font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted-2);}
.v5 .stub{position:relative;background:var(--void);overflow:hidden;display:flex;flex-direction:column;
  border-left:2px dashed var(--line-strong);}
.v5 .stub img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:brightness(.7) saturate(1.15);}
.v5 .stub .ov{position:absolute;inset:0;background:linear-gradient(180deg,rgba(8,7,10,.2),rgba(8,7,10,.85));}
.v5 .stub .inner{position:relative;z-index:2;margin-top:auto;padding:22px;text-align:center;}
.v5 .stub .price{font-family:var(--disp);font-size:38px;color:#fff;line-height:1;}
.v5 .stub .price s{color:var(--muted-2);font-size:18px;-webkit-text-decoration-color:var(--pink);text-decoration-color:var(--pink);}
.v5 .perf-top,.v5 .perf-bot{position:absolute;left:-9px;width:18px;height:18px;border-radius:50%;background:#08070a;z-index:5;}
.v5 .perf-top{top:-9px;} .v5 .perf-bot{bottom:-9px;}
.v5 .cta{margin-top:10px;}
.v5 .barcode{margin-top:16px;height:34px;width:100%;
  background:repeating-linear-gradient(90deg,var(--cream) 0 2px,transparent 2px 4px,var(--cream) 4px 5px,transparent 5px 9px);
  opacity:.85;border-radius:3px;}

@media(prefers-reduced-motion:reduce){
  *{animation:none!important;}
}
.foot{padding:40px clamp(18px,5vw,60px) 70px;color:var(--muted-2);font-size:12.5px;font-family:var(--mono);letter-spacing:.02em;text-align:center;border-top:1px solid var(--line);}
.foot b{color:var(--pink);}
</style>

<header class="page-head">
  <span class="brand">PORTO <b>PUB CRAWL</b></span>
  <h1>Hero — 5 New Directions</h1>
  <nav class="jump">
    <a href="#v1">01 Cinematic</a>
    <a href="#v2">02 Poster</a>
    <a href="#v3">03 Flyer</a>
    <a href="#v4">04 Typo</a>
    <a href="#v5">05 Ticket</a>
  </nav>
</header>

<section class="intro">
  <p>Five fresh takes on the homepage hero — each keeps your existing brand (void-black ground, the <b style="color:var(--pink)">#ff173f</b> pink-red, gold accents, party energy) but explores a different layout, mood and structure. All are static mockups — <b style="color:var(--cream)">nothing on the live site was changed.</b></p>
  <p class="note">Note: real fonts (Anton / Manrope) can't load inside this sandbox, so display type falls back to a condensed system face. Colours, layout, spacing and motion are accurate to how it would ship.</p>
</section>

<!-- ===================== V1 ===================== -->
<section class="variant" id="v1">
  <div class="v-label">
    <span class="v-num">01</span>
    <span class="v-name">Cinematic — bottom-weighted</span>
    <span class="v-desc">Full-bleed film still with the headline anchored bottom-left like a movie poster. A live "spots left" chip floats top-right. Feels premium and editorial rather than centred.</span>
  </div>
  <div class="frame v1">
    <div class="hero">
      <img class="hbg" src="__HERO__" alt="">
      <div class="grad"></div>
      <div class="chip"><span class="dot"></span> 7 spots left · tonight</div>
      <div class="hcontent">
        <div class="kicker">Porto · Nightlife · Since 2025</div>
        <h2>The <em>Craziest</em><br>Porto Pub Crawl</h2>
        <p class="sub">Five venues, one legendary night, zero chance you make it to breakfast. From the producers of The Hangover &amp; Project X.</p>
        <div class="row">
          <a class="btn btn-primary">Reserve My Spot <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
          <a class="btn btn-ghost">Watch the reel</a>
          <span class="rate"><span class="stars">★★★★★</span> <b>4.9</b> · 1,327+ reviews</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ===================== V2 ===================== -->
<section class="variant" id="v2">
  <div class="v-label">
    <span class="v-num">02</span>
    <span class="v-name">Split poster — type meets photo</span>
    <span class="v-desc">A 50/50 magazine split: outlined display type and hard facts on the left, a saturated crowd photo with a "book tonight" badge on the right. Confident and structured.</span>
  </div>
  <div class="frame v2">
    <div class="hero">
      <div class="left">
        <span class="tag">Porto's #1 Pub Crawl</span>
        <h2>Get<br>Loud.<br><span>Get Lost.</span></h2>
        <p class="sub">One wristband. Five venues. A crew from 60+ countries and a night nobody quite remembers.</p>
        <div class="cta">
          <a class="btn btn-primary">Reserve My Spot</a>
          <a class="btn btn-ghost">See the night</a>
        </div>
        <div class="facts">
          <div class="fact"><b>10K+</b><span>Guests hosted</span></div>
          <div class="fact"><b>4.9★</b><span>Avg rating</span></div>
          <div class="fact"><b>5</b><span>Venues / night</span></div>
        </div>
      </div>
      <div class="right">
        <img src="__FRIENDS__" alt="">
        <span class="badge">● Book tonight</span>
      </div>
    </div>
  </div>
</section>

<!-- ===================== V3 ===================== -->
<section class="variant" id="v3">
  <div class="v-label">
    <span class="v-num">03</span>
    <span class="v-name">Neon glass flyer</span>
    <span class="v-desc">A blurred club backdrop behind a glowing glass card — like a nightclub flyer. Focus lands on one headline and one action. Great for conversion.</span>
  </div>
  <div class="frame v3">
    <div class="hero">
      <img class="hbg" src="__CLUB__" alt="">
      <div class="grad"></div>
      <div class="hcontent">
        <div class="card">
          <span class="eye"><span class="dot"></span> Live every night · 9PM</span>
          <h2>Porto's <em>Craziest</em> Night Out</h2>
          <p class="sub">Guided bar-hop, free shots, skip-the-line club entry, and a host who makes sure it never gets boring.</p>
          <div class="cta">
            <a class="btn btn-primary">Reserve My Spot <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
          </div>
          <div class="meta"><span><b>4.9★</b> Google &amp; Trustpilot</span><span><b>1,327+</b> reviews</span><span><b>€25</b> from</span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ===================== V4 ===================== -->
<section class="variant" id="v4">
  <div class="v-label">
    <span class="v-num">04</span>
    <span class="v-name">Oversized type + marquee</span>
    <span class="v-desc">Type-forward and loud: a giant outline/fill headline with a tall photo tucked to the side, capped by a scrolling pink ticker. The most "brand statement" of the five.</span>
  </div>
  <div class="frame v4">
    <div class="hero">
      <div class="top">
        <div class="type">
          <div class="l out">Porto</div>
          <div class="l fill">Never</div>
          <div class="l">Sleeps</div>
        </div>
        <div class="photo"><img src="__VODKA__" alt=""></div>
        <div class="lead">
          <p>The guided pub crawl locals warn you about. Five venues, one host, endless shots.</p>
          <div class="cta"><a class="btn btn-primary">Reserve My Spot →</a></div>
        </div>
      </div>
      <div class="marquee">
        <div class="track">
          <span>Craziest Night in Porto</span><span>5 Venues</span><span>Free Shots</span><span>Skip The Line</span>
          <span>Craziest Night in Porto</span><span>5 Venues</span><span>Free Shots</span><span>Skip The Line</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ===================== V5 ===================== -->
<section class="variant" id="v5">
  <div class="v-label">
    <span class="v-num">05</span>
    <span class="v-name">Event ticket / wristband</span>
    <span class="v-desc">The hero <em>is</em> the product: a tear-off event ticket with an ADMIT ONE stub, price and barcode. Playful, unmistakably an event, and it makes booking the obvious next move.</span>
  </div>
  <div class="frame v5">
    <div class="hero">
      <div class="ticket">
        <div class="main">
          <div class="top-row"><span class="adm">● Admit One</span><span>Porto · PT</span></div>
          <h2>The Craziest<br><em>Pub Crawl</em></h2>
          <p class="sub">Your all-access pass to Porto after dark — bars, clubs, shots and a crew you haven't met yet.</p>
          <div class="detail">
            <div class="d"><b>Nightly</b><span>Doors 9:00 PM</span></div>
            <div class="d"><b>5 Stops</b><span>Bars + Club</span></div>
            <div class="d"><b>4.9★</b><span>1,327+ reviews</span></div>
          </div>
          <a class="btn btn-primary">Reserve My Spot →</a>
        </div>
        <div class="stub">
          <span class="perf-top"></span><span class="perf-bot"></span>
          <img src="__BOAT__" alt="">
          <div class="ov"></div>
          <div class="inner">
            <div class="price"><s>€35</s> €25</div>
            <div class="barcode"></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<footer class="foot">
  5 hero concepts · Porto Pub Crawl · <b>preview only — live site untouched</b>
</footer>
"""

html = (html
  .replace("__HERO__", HERO)
  .replace("__FRIENDS__", FRIENDS)
  .replace("__CLUB__", CLUB)
  .replace("__VODKA__", VODKA)
  .replace("__BOAT__", BOAT))

out = base / "hero-preview.html"
out.write_text(html)
print("wrote", out, len(html), "bytes")
