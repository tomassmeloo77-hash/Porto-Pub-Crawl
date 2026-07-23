#!/usr/bin/env python3
import base64, pathlib

base = pathlib.Path("/home/user/Porto-Pub-Crawl/scratch-preview")
VIDEO = "data:video/mp4;base64," + base64.b64encode((base/"hero-video.mp4").read_bytes()).decode()
POSTER = "data:image/webp;base64," + base64.b64encode((base/"hero-poster.webp").read_bytes()).decode()

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
html,body{height:100%;}
body{background:#000;color:var(--cream);font-family:var(--body);-webkit-font-smoothing:antialiased;line-height:1.5;overflow:hidden;}
img{display:block;max-width:100%;}
a{color:inherit;text-decoration:none;}

/* ===== full-window deck ===== */
.deck{position:fixed;inset:0;}
.slide{position:absolute;inset:0;opacity:0;visibility:hidden;transition:opacity .5s ease;z-index:1;}
.slide.active{opacity:1;visibility:visible;z-index:2;}

.hero{position:absolute;inset:0;overflow:hidden;background:var(--void);}
.hbg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;}
/* base darkening on every clip so it always sits into the dark brand */
.hbg{filter:brightness(.5) saturate(1.05) contrast(1.02);}

.btn{
  display:inline-flex;align-items:center;gap:9px;font-family:var(--body);font-weight:800;
  font-size:15px;letter-spacing:.01em;padding:17px 30px;border-radius:100px;cursor:pointer;
  transition:transform .25s, box-shadow .25s;white-space:nowrap;
}
.btn:hover{transform:translateY(-2px);}
.btn-primary{background:linear-gradient(135deg,var(--pink),#ff5a8f 55%,var(--violet));color:#fff;
  box-shadow:0 16px 40px -12px rgba(255,23,63,.8);}
.btn-ghost{border:1.5px solid var(--line-strong);color:var(--cream);background:rgba(255,255,255,.05);backdrop-filter:blur(8px);}
.btn-ghost:hover{border-color:var(--pink);background:rgba(255,23,63,.12);}
.btn svg{width:17px;height:17px;}
.stars{color:var(--gold);letter-spacing:2px;}

.container{width:100%;max-width:1200px;margin:0 auto;padding:0 clamp(22px,5vw,72px);}

/* ============================================================
   V1 — CINEMATIC BOTTOM-WEIGHTED
   ============================================================ */
.v1 .hbg{object-position:center 38%;}
.v1 .veil{position:absolute;inset:0;z-index:1;
  background:
    linear-gradient(180deg,rgba(5,4,6,.72) 0%,rgba(5,4,6,.28) 26%,rgba(5,4,6,.35) 50%,rgba(5,4,6,.82) 80%,rgba(5,4,6,.97) 100%),
    radial-gradient(ellipse 90% 70% at 20% 100%,rgba(255,23,63,.18),transparent 60%);}
.v1 .hcontent{position:relative;z-index:5;height:100%;display:flex;flex-direction:column;justify-content:flex-end;padding-bottom:clamp(50px,9vh,120px);}
.v1 .kicker{font-family:var(--mono);font-size:13px;letter-spacing:.3em;text-transform:uppercase;color:var(--pink-soft);margin-bottom:22px;}
.v1 h2{font-family:var(--disp);text-transform:uppercase;font-weight:400;
  font-size:clamp(52px,10vw,150px);line-height:.86;letter-spacing:.005em;color:#fff;
  text-shadow:0 8px 50px rgba(0,0,0,.7);text-wrap:balance;}
.v1 h2 em{font-style:normal;color:var(--pink);}
.v1 .sub{margin-top:24px;max-width:540px;font-size:clamp(15px,1.6vw,19px);color:#eceaeb;line-height:1.55;text-shadow:0 2px 14px rgba(0,0,0,.6);}
.v1 .row{display:flex;flex-wrap:wrap;align-items:center;gap:18px;margin-top:34px;}
.v1 .rate{display:flex;align-items:center;gap:9px;font-size:14px;color:#fff;}
.v1 .rate b{font-family:var(--disp);font-weight:400;font-size:21px;letter-spacing:.02em;}
.v1 .chip{position:absolute;top:clamp(80px,12vh,110px);right:clamp(22px,5vw,72px);z-index:6;
  display:flex;align-items:center;gap:9px;background:rgba(8,7,10,.62);backdrop-filter:blur(12px);
  border:1px solid var(--line-strong);border-radius:100px;padding:11px 17px;font-size:13px;color:var(--cream);}
.v1 .dot{width:8px;height:8px;border-radius:50%;background:#22ff7a;box-shadow:0 0 12px #22ff7a;animation:pulse 1.8s infinite;}
@keyframes pulse{0%,100%{opacity:1;transform:scale(1);}50%{opacity:.45;transform:scale(.7);}}

/* ============================================================
   V2 — SPLIT EDITORIAL POSTER
   ============================================================ */
.v2 .hero{display:grid;grid-template-columns:1.05fr .95fr;}
@media(max-width:820px){.v2 .hero{grid-template-columns:1fr;grid-template-rows:1.05fr .95fr;}}
.v2 .left{position:relative;padding:clamp(40px,6vw,96px);display:flex;flex-direction:column;justify-content:center;gap:26px;
  background:radial-gradient(ellipse 90% 70% at 12% 8%,rgba(255,23,63,.2),transparent 60%),var(--void);}
.v2 .tag{font-family:var(--mono);font-size:12.5px;letter-spacing:.22em;text-transform:uppercase;color:var(--muted);
  display:inline-flex;align-items:center;gap:10px;}
.v2 .tag::before{content:"";width:30px;height:1px;background:var(--pink);}
.v2 h2{font-family:var(--disp);text-transform:uppercase;font-weight:400;color:#fff;
  font-size:clamp(54px,8vw,124px);line-height:.84;letter-spacing:.01em;text-wrap:balance;}
.v2 h2 span{display:block;-webkit-text-stroke:1.6px var(--pink);color:transparent;}
.v2 .sub{color:var(--muted);font-size:clamp(14px,1.4vw,17px);max-width:400px;line-height:1.6;}
.v2 .cta{display:flex;gap:14px;flex-wrap:wrap;}
.v2 .facts{display:flex;gap:34px;flex-wrap:wrap;padding-top:30px;border-top:1px solid var(--line);}
.v2 .fact b{font-family:var(--disp);font-weight:400;font-size:32px;color:var(--gold);display:block;line-height:1;}
.v2 .fact span{font-size:12px;color:var(--muted-2);letter-spacing:.04em;}
.v2 .right{position:relative;overflow:hidden;}
.v2 .right .veil{position:absolute;inset:0;z-index:1;
  background:linear-gradient(240deg,transparent 40%,rgba(8,7,10,.55)),linear-gradient(0deg,rgba(8,7,10,.4),transparent 40%);}
.v2 .badge{position:absolute;z-index:3;bottom:30px;left:30px;background:var(--pink);color:#fff;
  font-family:var(--mono);font-size:12px;letter-spacing:.14em;text-transform:uppercase;padding:10px 16px;border-radius:100px;
  box-shadow:0 12px 34px -8px rgba(255,23,63,.85);}

/* ============================================================
   V3 — NEON GLASS FLYER
   ============================================================ */
.v3 .hbg{filter:brightness(.34) saturate(1.15) blur(3px);object-position:center 45%;transform:scale(1.06);}
.v3 .veil{position:absolute;inset:0;z-index:1;
  background:radial-gradient(ellipse 70% 60% at 50% 45%,rgba(255,23,63,.3),transparent 62%),rgba(5,4,6,.62);}
.v3 .hcontent{position:relative;z-index:5;height:100%;display:flex;align-items:center;justify-content:center;padding:clamp(24px,5vw,60px);}
.v3 .card{
  position:relative;max-width:720px;width:100%;text-align:center;padding:clamp(38px,5vw,68px);
  border-radius:26px;background:linear-gradient(180deg,rgba(20,16,22,.68),rgba(8,7,10,.62));
  border:1px solid rgba(255,84,104,.42);backdrop-filter:blur(20px);
  box-shadow:0 0 0 1px rgba(255,255,255,.03),0 40px 100px -30px rgba(0,0,0,.95),0 0 80px -18px rgba(255,23,63,.55);}
.v3 .eye{display:inline-flex;align-items:center;gap:9px;font-family:var(--mono);font-size:12.5px;letter-spacing:.16em;
  text-transform:uppercase;color:var(--pink-soft);border:1px solid rgba(255,84,104,.35);border-radius:100px;padding:8px 16px;margin-bottom:26px;}
.v3 .eye .dot{width:7px;height:7px;border-radius:50%;background:#22ff7a;box-shadow:0 0 10px #22ff7a;animation:pulse 1.8s infinite;}
.v3 h2{font-family:var(--disp);text-transform:uppercase;font-weight:400;color:#fff;
  font-size:clamp(48px,7.5vw,104px);line-height:.9;letter-spacing:.01em;text-wrap:balance;}
.v3 h2 em{font-style:normal;
  background:linear-gradient(100deg,var(--pink),#fff 50%,var(--pink));-webkit-background-clip:text;background-clip:text;color:transparent;}
.v3 .sub{margin:24px auto 0;max-width:440px;color:#e2dfe0;font-size:clamp(14px,1.5vw,17px);}
.v3 .cta{margin-top:32px;display:flex;justify-content:center;gap:14px;flex-wrap:wrap;}
.v3 .meta{margin-top:28px;display:flex;justify-content:center;gap:26px;flex-wrap:wrap;font-size:13px;color:var(--muted);}
.v3 .meta b{color:var(--cream);}

/* ============================================================
   V4 — OVERSIZED TYPE + MARQUEE
   ============================================================ */
.v4 .hero{background:radial-gradient(ellipse 70% 60% at 82% 12%,rgba(255,23,63,.22),transparent 55%),var(--void);
  display:flex;flex-direction:column;}
.v4 .top{flex:1;position:relative;display:flex;flex-direction:column;justify-content:center;padding:clamp(30px,5vw,80px);}
.v4 .type{position:relative;z-index:3;}
.v4 .type .l{font-family:var(--disp);text-transform:uppercase;font-weight:400;line-height:.8;letter-spacing:.01em;color:#fff;
  font-size:clamp(60px,15vw,230px);}
.v4 .type .l.out{color:transparent;-webkit-text-stroke:1.8px rgba(245,244,242,.5);}
.v4 .type .l.fill{color:var(--pink);}
.v4 .photo{position:absolute;z-index:2;right:clamp(30px,5vw,90px);top:50%;transform:translateY(-50%);
  width:clamp(210px,24vw,360px);aspect-ratio:9/16;border-radius:18px;overflow:hidden;
  border:1px solid var(--line-strong);box-shadow:0 40px 90px -25px rgba(0,0,0,.95);}
.v4 .photo .hbg{filter:brightness(.72) saturate(1.15) contrast(1.05);}
.v4 .photo .veil{position:absolute;inset:0;z-index:1;background:linear-gradient(0deg,rgba(8,7,10,.55),transparent 55%);}
@media(max-width:820px){.v4 .photo{position:static;transform:none;margin:26px 0 0;width:100%;max-width:320px;aspect-ratio:16/12;}}
.v4 .lead{position:relative;z-index:3;margin-top:30px;max-width:440px;color:#d7d4d5;font-size:clamp(14px,1.5vw,17px);}
.v4 .lead .cta{margin-top:24px;}
.v4 .marquee{overflow:hidden;border-top:1px solid rgba(0,0,0,.2);background:var(--pink);padding:16px 0;}
.v4 .track{display:flex;gap:40px;white-space:nowrap;width:max-content;animation:scroll-x 22s linear infinite;}
.v4 .track span{font-family:var(--disp);text-transform:uppercase;font-weight:400;font-size:23px;letter-spacing:.05em;color:#fff;display:inline-flex;align-items:center;gap:40px;}
.v4 .track span::after{content:"●";color:rgba(255,255,255,.6);font-size:11px;}
@keyframes scroll-x{from{transform:translateX(0);}to{transform:translateX(-50%);}}

/* ============================================================
   V5 — EVENT TICKET / WRISTBAND
   ============================================================ */
.v5 .hero{background:
  radial-gradient(ellipse 60% 50% at 18% 92%,rgba(122,10,31,.45),transparent 60%),
  radial-gradient(ellipse 50% 45% at 86% 8%,rgba(255,23,63,.2),transparent 60%),var(--void);
  display:flex;align-items:center;justify-content:center;padding:clamp(30px,5vw,70px);}
.v5 .ticket{display:grid;grid-template-columns:1.5fr 1fr;max-width:940px;width:100%;
  background:var(--void-2);border:1px solid var(--line-strong);border-radius:24px;overflow:hidden;
  box-shadow:0 50px 120px -40px rgba(0,0,0,.97);}
@media(max-width:820px){.v5 .ticket{grid-template-columns:1fr;max-width:460px;}}
.v5 .main{padding:clamp(34px,4vw,60px);position:relative;}
.v5 .top-row{display:flex;justify-content:space-between;align-items:center;font-family:var(--mono);font-size:12px;
  letter-spacing:.16em;text-transform:uppercase;color:var(--muted);margin-bottom:30px;}
.v5 .top-row .adm{color:var(--pink);}
.v5 h2{font-family:var(--disp);text-transform:uppercase;font-weight:400;color:#fff;
  font-size:clamp(46px,7vw,98px);line-height:.84;letter-spacing:.01em;text-wrap:balance;}
.v5 h2 em{font-style:normal;color:var(--gold);}
.v5 .sub{margin-top:20px;color:var(--muted);font-size:15px;max-width:380px;}
.v5 .detail{margin:30px 0;display:flex;gap:32px;flex-wrap:wrap;}
.v5 .detail .d b{display:block;font-family:var(--disp);font-weight:400;font-size:23px;color:var(--cream);line-height:1;}
.v5 .detail .d span{font-family:var(--mono);font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted-2);}
.v5 .stub{position:relative;background:var(--void);overflow:hidden;display:flex;flex-direction:column;
  border-left:2px dashed var(--line-strong);min-height:280px;}
.v5 .stub .hbg{filter:brightness(.62) saturate(1.15);}
.v5 .stub .ov{position:absolute;inset:0;z-index:1;background:linear-gradient(180deg,rgba(8,7,10,.25),rgba(8,7,10,.9));}
.v5 .stub .inner{position:relative;z-index:2;margin-top:auto;padding:26px;text-align:center;}
.v5 .stub .price{font-family:var(--disp);font-size:44px;color:#fff;line-height:1;}
.v5 .stub .price s{color:var(--muted-2);font-size:20px;-webkit-text-decoration-color:var(--pink);text-decoration-color:var(--pink);}
.v5 .perf-top,.v5 .perf-bot{position:absolute;left:-10px;width:20px;height:20px;border-radius:50%;background:#000;z-index:5;}
.v5 .perf-top{top:-10px;} .v5 .perf-bot{bottom:-10px;}
.v5 .cta{margin-top:12px;}
.v5 .barcode{margin-top:18px;height:38px;width:100%;
  background:repeating-linear-gradient(90deg,var(--cream) 0 2px,transparent 2px 4px,var(--cream) 4px 5px,transparent 5px 9px);
  opacity:.85;border-radius:3px;}

/* ===== controls ===== */
.switch{position:fixed;left:50%;bottom:clamp(18px,3vh,32px);transform:translateX(-50%);z-index:30;
  display:flex;align-items:center;gap:8px;background:rgba(8,7,10,.7);backdrop-filter:blur(16px);
  border:1px solid var(--line-strong);border-radius:100px;padding:8px 10px;max-width:calc(100vw - 24px);}
.switch button{font-family:var(--mono);font-size:12px;letter-spacing:.04em;color:var(--muted);background:transparent;
  border:0;border-radius:100px;padding:9px 15px;cursor:pointer;transition:.2s;white-space:nowrap;}
.switch button:hover{color:var(--cream);}
.switch button.on{background:var(--pink);color:#fff;box-shadow:0 8px 22px -8px rgba(255,23,63,.9);}
.arrow{position:fixed;top:50%;transform:translateY(-50%);z-index:30;width:46px;height:46px;border-radius:50%;
  background:rgba(8,7,10,.55);backdrop-filter:blur(10px);border:1px solid var(--line-strong);color:var(--cream);
  display:flex;align-items:center;justify-content:center;cursor:pointer;transition:.2s;}
.arrow:hover{background:rgba(255,23,63,.25);border-color:var(--pink);}
.arrow.prev{left:clamp(12px,2vw,26px);} .arrow.next{right:clamp(12px,2vw,26px);}
.arrow svg{width:20px;height:20px;}
.tagline{position:fixed;top:16px;left:50%;transform:translateX(-50%);z-index:30;
  font-family:var(--mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted-2);
  background:rgba(8,7,10,.55);backdrop-filter:blur(10px);border:1px solid var(--line);border-radius:100px;padding:7px 15px;
  white-space:nowrap;max-width:calc(100vw - 24px);overflow:hidden;text-overflow:ellipsis;}
.tagline b{color:var(--pink);}
@media(max-width:600px){.arrow{display:none;} .switch button{padding:9px 12px;}}
@media(prefers-reduced-motion:reduce){*{animation:none!important;}}
</style>

<div class="tagline">Porto Pub Crawl · Hero — <b id="tl">01 / Cinematic</b> · preview only</div>

<div class="deck">
  <!-- V1 -->
  <section class="slide active v1" data-name="01 / Cinematic">
    <div class="hero">
      <video class="hbg herovid" muted loop autoplay playsinline></video>
      <div class="veil"></div>
      <div class="chip"><span class="dot"></span> 7 spots left · tonight</div>
      <div class="hcontent"><div class="container">
        <div class="kicker">Porto · Nightlife · Since 2025</div>
        <h2>The <em>Craziest</em><br>Porto Pub Crawl</h2>
        <p class="sub">Five venues, one legendary night, zero chance you make it to breakfast. From the producers of The Hangover &amp; Project X.</p>
        <div class="row">
          <a class="btn btn-primary">Reserve My Spot <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
          <a class="btn btn-ghost">Watch the reel</a>
          <span class="rate"><span class="stars">★★★★★</span> <b>4.9</b> · 1,327+ reviews</span>
        </div>
      </div></div>
    </div>
  </section>

  <!-- V2 -->
  <section class="slide v2" data-name="02 / Split poster">
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
        <video class="hbg herovid" muted loop autoplay playsinline></video>
        <div class="veil"></div>
        <span class="badge">● Book tonight</span>
      </div>
    </div>
  </section>

  <!-- V3 -->
  <section class="slide v3" data-name="03 / Neon flyer">
    <div class="hero">
      <video class="hbg herovid" muted loop autoplay playsinline></video>
      <div class="veil"></div>
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
  </section>

  <!-- V4 -->
  <section class="slide v4" data-name="04 / Oversized type">
    <div class="hero">
      <div class="top">
        <div class="type">
          <div class="l out">Porto</div>
          <div class="l fill">Never</div>
          <div class="l">Sleeps</div>
        </div>
        <div class="photo"><video class="hbg herovid" muted loop autoplay playsinline></video><div class="veil"></div></div>
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
  </section>

  <!-- V5 -->
  <section class="slide v5" data-name="05 / Event ticket">
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
          <video class="hbg herovid" muted loop autoplay playsinline></video>
          <div class="ov"></div>
          <div class="inner">
            <div class="price"><s>€35</s> €25</div>
            <div class="barcode"></div>
          </div>
        </div>
      </div>
    </div>
  </section>
</div>

<button class="arrow prev" aria-label="Previous"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M15 18l-6-6 6-6"/></svg></button>
<button class="arrow next" aria-label="Next"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M9 6l6 6-6 6"/></svg></button>

<nav class="switch">
  <button class="on" data-i="0">01 Cinematic</button>
  <button data-i="1">02 Poster</button>
  <button data-i="2">03 Flyer</button>
  <button data-i="3">04 Typo</button>
  <button data-i="4">05 Ticket</button>
</nav>

<script>
  var HEROVID = "__VIDEO__", POSTER = "__POSTER__";
  var slides = Array.prototype.slice.call(document.querySelectorAll('.slide'));
  var btns = Array.prototype.slice.call(document.querySelectorAll('.switch button'));
  var tl = document.getElementById('tl');
  var cur = 0;

  document.querySelectorAll('video.herovid').forEach(function(v){
    v.poster = POSTER; v.src = HEROVID; v.muted = true;
    v.setAttribute('playsinline','');
  });

  function playActive(){
    slides.forEach(function(s,i){
      s.querySelectorAll('video').forEach(function(v){
        if(i===cur){ var p=v.play(); if(p&&p.catch)p.catch(function(){}); }
        else { try{v.pause();}catch(e){} }
      });
    });
  }
  function go(i){
    cur = (i+slides.length)%slides.length;
    slides.forEach(function(s,k){ s.classList.toggle('active',k===cur); });
    btns.forEach(function(b,k){ b.classList.toggle('on',k===cur); });
    tl.textContent = slides[cur].dataset.name;
    playActive();
  }
  btns.forEach(function(b){ b.addEventListener('click',function(){ go(+b.dataset.i); }); });
  document.querySelector('.arrow.prev').addEventListener('click',function(){ go(cur-1); });
  document.querySelector('.arrow.next').addEventListener('click',function(){ go(cur+1); });
  document.addEventListener('keydown',function(e){
    if(e.key==='ArrowRight') go(cur+1);
    else if(e.key==='ArrowLeft') go(cur-1);
    else if(e.key>='1'&&e.key<='5') go(+e.key-1);
  });
  playActive();
</script>
"""

html = html.replace("__VIDEO__", VIDEO).replace("__POSTER__", POSTER)
out = base / "hero-preview.html"
out.write_text(html)
print("wrote", out, round(len(html)/1024), "KB")
