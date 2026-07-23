#!/usr/bin/env python3
import base64, pathlib

base = pathlib.Path("/home/user/Porto-Pub-Crawl/scratch-preview")
fdir = base/"fonts"/"node_modules"

def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()
def font_uri(p): return "data:font/woff2;base64," + b64(p)

VIDEO = "data:video/mp4;base64," + b64(base/"hero-video.mp4")
POSTER = "data:image/webp;base64," + b64(base/"hero-poster.webp")

ANTON   = font_uri(fdir/"@fontsource/anton/files/anton-latin-400-normal.woff2")
MAN400  = font_uri(fdir/"@fontsource/manrope/files/manrope-latin-400-normal.woff2")
MAN700  = font_uri(fdir/"@fontsource/manrope/files/manrope-latin-700-normal.woff2")
MAN800  = font_uri(fdir/"@fontsource/manrope/files/manrope-latin-800-normal.woff2")
MONO400 = font_uri(fdir/"@fontsource/space-mono/files/space-mono-latin-400-normal.woff2")
MONO700 = font_uri(fdir/"@fontsource/space-mono/files/space-mono-latin-700-normal.woff2")

html = r"""<style>
@font-face{font-family:'Anton';src:url(__ANTON__) format('woff2');font-weight:400;font-display:swap;}
@font-face{font-family:'Manrope';src:url(__MAN400__) format('woff2');font-weight:400;font-display:swap;}
@font-face{font-family:'Manrope';src:url(__MAN700__) format('woff2');font-weight:700;font-display:swap;}
@font-face{font-family:'Manrope';src:url(__MAN800__) format('woff2');font-weight:800;font-display:swap;}
@font-face{font-family:'Space Mono';src:url(__MONO400__) format('woff2');font-weight:400;font-display:swap;}
@font-face{font-family:'Space Mono';src:url(__MONO700__) format('woff2');font-weight:700;font-display:swap;}

:root{
  --void:#08070a; --void-2:#0e0c10; --void-3:#141017;
  --pink:#ff173f; --pink-soft:#ff5468;
  --violet:#7a0a1f; --violet-deep:#3c0512;
  --gold:#ffc466; --lime:#22ff7a; --cream:#f5f4f2;
  --muted:#a3a0a1; --muted-2:#7e7b7c;
  --line:rgba(245,244,242,0.09); --line-strong:rgba(245,244,242,0.16);
  --disp:'Anton', Impact, sans-serif;
  --body:'Manrope', system-ui, sans-serif;
  --mono:'Space Mono', ui-monospace, monospace;
}
*{box-sizing:border-box;margin:0;padding:0;}
html,body{height:100%;}
body{background:#000;color:var(--cream);font-family:var(--body);-webkit-font-smoothing:antialiased;line-height:1.5;overflow:hidden;}
img{display:block;max-width:100%;}
a{color:inherit;text-decoration:none;}

.deck{position:fixed;inset:0;}
.slide{position:absolute;inset:0;opacity:0;visibility:hidden;transition:opacity .55s ease;z-index:1;}
.slide.active{opacity:1;visibility:visible;z-index:2;}
.hero{position:absolute;inset:0;overflow:hidden;background:var(--void);}
.hbg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;}
/* cinematic grade so phone footage reads as intentional */
.hbg{filter:brightness(.56) saturate(1.12) contrast(1.06);}
.grain{position:absolute;inset:0;z-index:2;pointer-events:none;opacity:.5;mix-blend-mode:overlay;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.55'/%3E%3C/svg%3E");}

.btn{display:inline-flex;align-items:center;justify-content:center;gap:9px;font-family:var(--body);font-weight:800;
  font-size:15px;letter-spacing:.01em;padding:16px 28px;border-radius:100px;cursor:pointer;
  transition:transform .25s, box-shadow .25s, background .25s;white-space:nowrap;}
.btn:hover{transform:translateY(-2px);}
.btn-primary{background:linear-gradient(135deg,var(--pink),#ff5a8f 55%,var(--violet));color:#fff;
  box-shadow:0 16px 40px -12px rgba(255,23,63,.8);}
.btn-primary:hover{box-shadow:0 20px 48px -12px rgba(255,23,63,.95);}
.btn-ghost{border:1.5px solid var(--line-strong);color:var(--cream);background:rgba(255,255,255,.05);backdrop-filter:blur(8px);}
.btn-ghost:hover{border-color:var(--pink);background:rgba(255,23,63,.12);}
.btn svg{width:17px;height:17px;}
.stars{color:var(--gold);letter-spacing:2px;}
.container{width:100%;max-width:1240px;margin:0 auto;padding:0 clamp(22px,5vw,72px);}
.dot{width:8px;height:8px;border-radius:50%;background:var(--lime);box-shadow:0 0 12px var(--lime);animation:pulse 1.8s infinite;flex:none;}
@keyframes pulse{0%,100%{opacity:1;transform:scale(1);}50%{opacity:.4;transform:scale(.65);}}
.gsvg{width:15px;height:15px;flex:none;}

/* ============================================================
   A — CONVERSION SPLIT (video + live booking panel)
   ============================================================ */
.vA .hero{display:grid;grid-template-columns:1fr;}
.vA .hbg{object-position:center 40%;}
.vA .veil{position:absolute;inset:0;z-index:1;background:
  linear-gradient(90deg,rgba(5,4,6,.9) 0%,rgba(5,4,6,.55) 42%,rgba(5,4,6,.25) 70%,rgba(5,4,6,.55) 100%),
  linear-gradient(0deg,rgba(5,4,6,.7),transparent 45%);}
.vA .wrap{position:relative;z-index:5;height:100%;display:grid;grid-template-columns:1.15fr .85fr;align-items:center;
  gap:40px;padding:clamp(80px,10vh,120px) clamp(24px,5vw,80px) clamp(40px,6vh,70px);}
@media(max-width:900px){.vA .wrap{grid-template-columns:1fr;align-content:center;gap:26px;}}
.vA .eyebrow{display:inline-flex;align-items:center;gap:9px;font-family:var(--mono);font-size:12px;letter-spacing:.12em;
  text-transform:uppercase;color:var(--cream);background:rgba(8,7,10,.5);border:1px solid var(--line-strong);
  padding:8px 14px;border-radius:100px;backdrop-filter:blur(8px);width:max-content;}
.vA h2{font-family:var(--disp);text-transform:uppercase;font-size:clamp(52px,7.5vw,118px);line-height:.86;
  letter-spacing:.005em;color:#fff;margin:22px 0 0;text-shadow:0 6px 40px rgba(0,0,0,.6);}
.vA h2 em{font-style:normal;color:var(--pink);}
.vA .sub{margin-top:22px;max-width:440px;font-size:clamp(15px,1.5vw,18px);color:#e9e7e8;line-height:1.55;}
.vA .socialrow{display:flex;align-items:center;gap:14px;margin-top:26px;flex-wrap:wrap;font-size:13.5px;color:#e9e7e8;}
.vA .socialrow .av{display:flex;}
.vA .socialrow .av span{width:30px;height:30px;border-radius:50%;border:2px solid var(--void);margin-left:-10px;
  background:linear-gradient(135deg,var(--pink),var(--violet));display:grid;place-items:center;font-size:11px;font-weight:800;color:#fff;}
.vA .socialrow .av span:first-child{margin-left:0;}
/* booking panel */
.vA .panel{background:linear-gradient(180deg,rgba(20,16,23,.86),rgba(8,7,10,.9));border:1px solid var(--line-strong);
  border-radius:22px;padding:26px;backdrop-filter:blur(18px);box-shadow:0 40px 100px -35px rgba(0,0,0,.95);max-width:420px;justify-self:end;width:100%;}
@media(max-width:900px){.vA .panel{justify-self:stretch;}}
.vA .panel .ptop{display:flex;justify-content:space-between;align-items:flex-start;gap:12px;}
.vA .panel .price{font-family:var(--disp);font-size:46px;line-height:.9;color:#fff;}
.vA .panel .price s{font-family:var(--body);font-weight:700;font-size:18px;color:var(--muted-2);margin-right:8px;}
.vA .panel .price small{display:block;font-family:var(--mono);font-size:11px;letter-spacing:.08em;color:var(--muted);text-transform:uppercase;margin-top:4px;}
.vA .panel .rate{text-align:right;font-size:12px;color:var(--muted);}
.vA .panel .rate b{color:var(--cream);}
.vA .nights{display:flex;gap:8px;margin:20px 0;}
.vA .nights button{flex:1;font-family:var(--mono);font-size:12px;padding:11px 0;border-radius:12px;border:1px solid var(--line-strong);
  background:transparent;color:var(--muted);cursor:pointer;transition:.2s;}
.vA .nights button.on{background:var(--pink);border-color:var(--pink);color:#fff;}
.vA .plist{list-style:none;display:flex;flex-direction:column;gap:9px;margin:4px 0 18px;}
.vA .plist li{display:flex;align-items:center;gap:10px;font-size:13.5px;color:#d9d6d7;}
.vA .plist svg{width:16px;height:16px;color:var(--lime);flex:none;}
.vA .spots{display:flex;align-items:center;gap:9px;font-size:12.5px;color:var(--gold);margin-bottom:14px;}
.vA .panel .btn{width:100%;}
.vA .reassure{text-align:center;font-size:11px;color:var(--muted-2);margin-top:10px;}

/* ============================================================
   B — TYPE MASK (video shows THROUGH giant letters)
   ============================================================ */
.vB .hero{background:var(--void);display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;
  padding:clamp(70px,10vh,120px) 16px clamp(50px,7vh,90px);}
.vB .kick{font-family:var(--mono);font-size:clamp(11px,1.4vw,14px);letter-spacing:.34em;text-transform:uppercase;color:var(--pink-soft);}
.vB .maskwrap{position:relative;width:100%;}
.vB .mask{font-family:var(--disp);text-transform:uppercase;line-height:.8;letter-spacing:.01em;
  font-size:clamp(96px,26vw,420px);margin:0;
  background-image:url(__POSTER__);background-size:cover;background-position:center 35%;
  -webkit-background-clip:text;background-clip:text;color:transparent;-webkit-text-fill-color:transparent;
  filter:brightness(1.15) contrast(1.05);}
.vB .maskvid{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:-1;} /* fallback layer hidden; poster drives clip */
.vB .maskline2{color:#fff;-webkit-text-fill-color:#fff;background:none;}
.vB .maskline2 span{color:var(--pink);-webkit-text-fill-color:var(--pink);}
.vB .sub{margin:26px auto 0;max-width:560px;font-size:clamp(15px,1.6vw,19px);color:#d9d6d7;}
.vB .cta{margin-top:30px;display:flex;gap:14px;justify-content:center;flex-wrap:wrap;}
.vB .trust{margin-top:26px;display:flex;gap:22px;justify-content:center;flex-wrap:wrap;font-size:13px;color:var(--muted);}
.vB .trust b{color:var(--cream);}
.vB .trust .g{display:inline-flex;align-items:center;gap:7px;}

/* ============================================================
   C — EDITORIAL MASTHEAD (curated culture magazine)
   ============================================================ */
.vC .hero{background:var(--void);display:flex;flex-direction:column;}
.vC .masthead{display:flex;justify-content:space-between;align-items:center;padding:clamp(74px,11vh,104px) clamp(24px,5vw,64px) 0;
  font-family:var(--mono);font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);gap:16px;flex-wrap:wrap;}
.vC .masthead .r{display:flex;gap:26px;flex-wrap:wrap;}
.vC .masthead b{color:var(--cream);}
.vC .rule{height:1px;background:var(--line-strong);margin:16px clamp(24px,5vw,64px) 0;}
.vC .grid{flex:1;display:grid;grid-template-columns:1.1fr .9fr;gap:clamp(20px,3vw,48px);
  padding:clamp(20px,3.5vh,40px) clamp(24px,5vw,64px) clamp(30px,5vh,56px);align-items:center;}
@media(max-width:900px){.vC .grid{grid-template-columns:1fr;}}
.vC .lead{position:relative;}
.vC .idx{font-family:var(--mono);font-size:13px;color:var(--pink);letter-spacing:.1em;}
.vC h2{font-family:var(--disp);text-transform:uppercase;font-size:clamp(56px,8.2vw,140px);line-height:.82;color:#fff;margin:14px 0 0;letter-spacing:.004em;}
.vC h2 em{font-style:normal;-webkit-text-stroke:1.6px var(--gold);color:transparent;}
.vC .dek{margin-top:24px;max-width:440px;color:var(--muted);font-size:clamp(14px,1.5vw,17px);line-height:1.6;
  border-left:2px solid var(--pink);padding-left:16px;}
.vC .cta{margin-top:28px;display:flex;gap:14px;flex-wrap:wrap;align-items:center;}
.vC .cta .meta{font-family:var(--mono);font-size:12px;color:var(--muted);}
.vC .cta .meta b{color:var(--gold);}
.vC .frame{position:relative;aspect-ratio:4/5;border-radius:6px;overflow:hidden;border:1px solid var(--line-strong);
  box-shadow:0 40px 90px -30px rgba(0,0,0,.9);}
.vC .frame .cap{position:absolute;left:0;right:0;bottom:0;z-index:3;padding:16px;font-family:var(--mono);font-size:11px;
  letter-spacing:.08em;text-transform:uppercase;color:var(--cream);
  background:linear-gradient(0deg,rgba(8,7,10,.9),transparent);display:flex;justify-content:space-between;gap:10px;}
.vC .frame .cap .live{color:var(--lime);display:inline-flex;align-items:center;gap:6px;}

/* ============================================================
   D — SOCIAL REEL (story-native, phone-frame)
   ============================================================ */
.vD .hero{background:
  radial-gradient(ellipse 55% 45% at 78% 12%,rgba(255,23,63,.22),transparent 60%),
  radial-gradient(ellipse 50% 50% at 15% 90%,rgba(122,10,31,.4),transparent 60%),var(--void);
  display:grid;grid-template-columns:1fr auto;align-items:center;gap:clamp(24px,5vw,70px);
  padding:clamp(80px,11vh,120px) clamp(24px,5vw,80px) clamp(40px,6vh,70px);}
@media(max-width:900px){.vD .hero{grid-template-columns:1fr;justify-items:center;text-align:center;}}
.vD .copy{max-width:560px;}
.vD .badge{display:inline-flex;align-items:center;gap:8px;font-family:var(--mono);font-size:12px;letter-spacing:.1em;
  text-transform:uppercase;color:var(--pink-soft);border:1px solid rgba(255,84,104,.4);border-radius:100px;padding:7px 14px;}
.vD h2{font-family:var(--disp);text-transform:uppercase;font-size:clamp(52px,7.5vw,122px);line-height:.85;color:#fff;margin:22px 0 0;}
.vD h2 em{font-style:normal;color:var(--pink);}
.vD .sub{margin-top:22px;font-size:clamp(15px,1.5vw,18px);color:#d9d6d7;max-width:440px;}
@media(max-width:900px){.vD .sub{margin-inline:auto;}}
.vD .cta{margin-top:28px;display:flex;gap:14px;flex-wrap:wrap;}
@media(max-width:900px){.vD .cta{justify-content:center;}}
.vD .trust{margin-top:24px;font-size:13px;color:var(--muted);display:flex;gap:18px;flex-wrap:wrap;}
@media(max-width:900px){.vD .trust{justify-content:center;}}
.vD .trust b{color:var(--cream);}
/* phone */
.vD .phone{position:relative;width:clamp(240px,26vw,320px);aspect-ratio:9/19.5;border-radius:38px;
  border:2px solid rgba(255,255,255,.14);overflow:hidden;box-shadow:0 50px 120px -35px rgba(0,0,0,.95),0 0 0 8px rgba(20,16,23,.6);
  background:#000;}
@media(max-width:520px){.vD .phone{width:74vw;}}
.vD .phone .hbg{filter:brightness(.8) saturate(1.15) contrast(1.05);}
.vD .phone .bars{position:absolute;top:14px;left:14px;right:14px;z-index:4;display:flex;gap:5px;}
.vD .phone .bars i{flex:1;height:3px;border-radius:2px;background:rgba(255,255,255,.35);overflow:hidden;}
.vD .phone .bars i.on{background:rgba(255,255,255,.35);}
.vD .phone .bars i.on::after{content:"";display:block;height:100%;width:60%;background:#fff;}
.vD .phone .handle{position:absolute;top:30px;left:16px;z-index:4;display:flex;align-items:center;gap:8px;font-size:12px;font-weight:800;color:#fff;}
.vD .phone .handle span{width:24px;height:24px;border-radius:50%;background:linear-gradient(135deg,var(--pink),var(--violet));display:grid;place-items:center;font-size:11px;}
.vD .phone .ov{position:absolute;inset:0;z-index:3;background:linear-gradient(0deg,rgba(8,7,10,.85),transparent 42%);}
.vD .phone .cap{position:absolute;left:16px;right:16px;bottom:64px;z-index:4;text-align:left;}
.vD .phone .cap b{font-family:var(--disp);font-size:24px;color:#fff;line-height:1;text-transform:uppercase;}
.vD .phone .cap p{font-size:12px;color:#e0dddd;margin-top:6px;}
.vD .phone .like{position:absolute;right:14px;bottom:96px;z-index:4;display:flex;flex-direction:column;gap:16px;align-items:center;color:#fff;font-size:11px;}
.vD .phone .like svg{width:26px;height:26px;filter:drop-shadow(0 2px 6px rgba(0,0,0,.5));}
.vD .phone .tap{position:absolute;left:14px;right:14px;bottom:16px;z-index:4;background:#fff;color:var(--void);
  text-align:center;font-weight:800;font-size:13px;padding:12px;border-radius:100px;}

/* ===== controls ===== */
.switch{position:fixed;left:50%;bottom:clamp(16px,2.6vh,30px);transform:translateX(-50%);z-index:30;
  display:flex;align-items:center;gap:6px;background:rgba(8,7,10,.72);backdrop-filter:blur(16px);
  border:1px solid var(--line-strong);border-radius:100px;padding:7px 9px;max-width:calc(100vw - 20px);}
.switch button{font-family:var(--mono);font-size:11.5px;letter-spacing:.03em;color:var(--muted);background:transparent;
  border:0;border-radius:100px;padding:9px 14px;cursor:pointer;transition:.2s;white-space:nowrap;}
.switch button:hover{color:var(--cream);}
.switch button.on{background:var(--pink);color:#fff;box-shadow:0 8px 22px -8px rgba(255,23,63,.9);}
.arrow{position:fixed;top:50%;transform:translateY(-50%);z-index:30;width:46px;height:46px;border-radius:50%;
  background:rgba(8,7,10,.55);backdrop-filter:blur(10px);border:1px solid var(--line-strong);color:var(--cream);
  display:flex;align-items:center;justify-content:center;cursor:pointer;transition:.2s;}
.arrow:hover{background:rgba(255,23,63,.25);border-color:var(--pink);}
.arrow.prev{left:clamp(10px,2vw,24px);} .arrow.next{right:clamp(10px,2vw,24px);}
.arrow svg{width:20px;height:20px;}
.tagline{position:fixed;top:14px;left:50%;transform:translateX(-50%);z-index:30;
  font-family:var(--mono);font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted-2);
  background:rgba(8,7,10,.6);backdrop-filter:blur(10px);border:1px solid var(--line);border-radius:100px;padding:7px 15px;
  white-space:nowrap;max-width:calc(100vw - 20px);overflow:hidden;text-overflow:ellipsis;}
.tagline b{color:var(--pink);}
@media(max-width:640px){.arrow{display:none;}}
@media(prefers-reduced-motion:reduce){*{animation:none!important;}}
</style>

<div class="tagline">Porto Pub Crawl · <b id="tl">A · Conversion split</b> · research-driven preview</div>

<div class="deck">
  <!-- ===== A ===== -->
  <section class="slide active vA" data-name="A · Conversion split">
    <div class="hero">
      <video class="hbg herovid" muted loop autoplay playsinline></video>
      <div class="veil"></div>
      <div class="grain"></div>
      <div class="wrap">
        <div class="copy">
          <span class="eyebrow"><span class="dot"></span> Live tonight · Porto's #1 rated crawl</span>
          <h2>Porto's<br><em>Craziest</em><br>Night Out</h2>
          <p class="sub">5 venues, free shots, skip-the-line club entry and an instant crew — one wristband, zero planning.</p>
          <div class="socialrow"><span class="av"><span>MJ</span><span>AL</span><span>PK</span><span>+</span></span> Joined by 10,000+ crawlers from 60+ countries</div>
        </div>
        <aside class="panel">
          <div class="ptop">
            <div class="price"><span><s>€20</s>€17</span><small>per person</small></div>
            <div class="rate"><span class="stars">★★★★★</span><br><b>4.9</b> · 1,327+ reviews</div>
          </div>
          <div class="nights">
            <button class="on">Tonight</button><button>Fri</button><button>Sat</button>
          </div>
          <ul class="plist">
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>9 free drinks — beer, sangria &amp; shots</li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>VIP entry · 4 bars + 1 nightclub</li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>Free photos &amp; video next day</li>
          </ul>
          <div class="spots"><span class="dot"></span> Only 7 spots left for tonight</div>
          <a class="btn btn-primary">Reserve My Spot — €17 <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
          <p class="reassure">1-min checkout · Free cancellation up to 24h</p>
        </aside>
      </div>
    </div>
  </section>

  <!-- ===== B ===== -->
  <section class="slide vB" data-name="B · Type-mask">
    <div class="hero">
      <span class="kick">Porto · Nightlife · Since 2025</span>
      <h1 class="mask">Crawl</h1>
      <h1 class="mask maskline2">till <span>dawn</span></h1>
      <p class="sub">The guided pub crawl locals warn you about — 5 venues, free shots and a crew you haven't met yet.</p>
      <div class="cta">
        <a class="btn btn-primary">Reserve My Spot — €17 <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        <a class="btn btn-ghost">Watch the reel</a>
      </div>
      <div class="trust">
        <span class="g"><span class="stars">★★★★★</span> <b>4.9</b></span>
        <span class="g"><b>1,327+</b> reviews</span>
        <span class="g"><span class="dot"></span> <b>7</b> spots left tonight</span>
      </div>
    </div>
  </section>

  <!-- ===== C ===== -->
  <section class="slide vC" data-name="C · Editorial masthead">
    <div class="hero">
      <div class="masthead">
        <span>Porto Pub Crawl</span>
        <div class="r"><span>Est. <b>2025</b></span><span>41.14°N 8.61°W</span><span><b>4.9★</b> / 1,327 reviews</span></div>
      </div>
      <div class="rule"></div>
      <div class="grid">
        <div class="lead">
          <div class="idx">Nº 01 — The Night Programme</div>
          <h2>Get Loud.<br><em>Get Lost.</em></h2>
          <p class="dek">Five venues, one licensed local host and a crowd from sixty countries. Off the streets, onto the river, into the club — home before sunrise, optional.</p>
          <div class="cta">
            <a class="btn btn-primary">Reserve My Spot</a>
            <span class="meta">from <b>€17</b> · free cancellation</span>
          </div>
        </div>
        <div class="frame">
          <video class="hbg herovid" muted loop autoplay playsinline></video>
          <div class="grain"></div>
          <div class="cap"><span class="live"><span class="dot"></span> Filmed last Saturday</span><span>Porto, PT</span></div>
        </div>
      </div>
    </div>
  </section>

  <!-- ===== D ===== -->
  <section class="slide vD" data-name="D · Social reel">
    <div class="hero">
      <div class="copy">
        <span class="badge"><span class="dot"></span> As seen on your For You page</span>
        <h2>The Night<br>That Breaks<br>The <em>Internet</em></h2>
        <p class="sub">1.4M views can't be wrong. Come see why Porto's craziest pub crawl is all over your feed — then star in the next clip.</p>
        <div class="cta">
          <a class="btn btn-primary">Reserve My Spot — €17 <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
          <a class="btn btn-ghost">See the reel</a>
        </div>
        <div class="trust"><span><span class="stars">★★★★★</span> <b>4.9</b></span><span><b>10K+</b> crawlers</span><span><b>60+</b> countries</span></div>
      </div>
      <div class="phone">
        <video class="hbg herovid" muted loop autoplay playsinline></video>
        <div class="bars"><i class="on"></i><i></i><i></i></div>
        <div class="handle"><span>P</span> portopubcrawl</div>
        <div class="ov"></div>
        <div class="like">
          <div><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 21s-8-4.5-8-11a4.5 4.5 0 0 1 8-3 4.5 4.5 0 0 1 8 3c0 6.5-8 11-8 11z"/></svg>83.4K</div>
          <div><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>2.1K</div>
        </div>
        <div class="cap"><b>Craziest night in Porto 🇵🇹</b><p>#portopubcrawl · original sound</p></div>
        <div class="tap">Reserve my spot →</div>
      </div>
    </div>
  </section>
</div>

<button class="arrow prev" aria-label="Previous"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M15 18l-6-6 6-6"/></svg></button>
<button class="arrow next" aria-label="Next"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M9 6l6 6-6 6"/></svg></button>

<nav class="switch">
  <button class="on" data-i="0">A Split</button>
  <button data-i="1">B Type</button>
  <button data-i="2">C Editorial</button>
  <button data-i="3">D Reel</button>
</nav>

<script>
  var HEROVID="__VIDEO__", POSTER="__POSTER__";
  var slides=[].slice.call(document.querySelectorAll('.slide'));
  var btns=[].slice.call(document.querySelectorAll('.switch button'));
  var tl=document.getElementById('tl');
  var cur=0;
  document.querySelectorAll('video.herovid').forEach(function(v){
    v.poster=POSTER; v.src=HEROVID; v.muted=true; v.setAttribute('playsinline','');
  });
  function playActive(){
    slides.forEach(function(s,i){
      s.querySelectorAll('video').forEach(function(v){
        if(i===cur){var p=v.play();if(p&&p.catch)p.catch(function(){});}
        else{try{v.pause();}catch(e){}}
      });
    });
  }
  function go(i){
    cur=(i+slides.length)%slides.length;
    slides.forEach(function(s,k){s.classList.toggle('active',k===cur);});
    btns.forEach(function(b,k){b.classList.toggle('on',k===cur);});
    tl.textContent=slides[cur].dataset.name;
    playActive();
  }
  btns.forEach(function(b){b.addEventListener('click',function(){go(+b.dataset.i);});});
  document.querySelector('.arrow.prev').addEventListener('click',function(){go(cur-1);});
  document.querySelector('.arrow.next').addEventListener('click',function(){go(cur+1);});
  document.addEventListener('keydown',function(e){
    if(e.key==='ArrowRight')go(cur+1);
    else if(e.key==='ArrowLeft')go(cur-1);
    else if(e.key>='1'&&e.key<='4')go(+e.key-1);
  });
  playActive();
</script>
"""

repl = {
  "__ANTON__":ANTON,"__MAN400__":MAN400,"__MAN700__":MAN700,"__MAN800__":MAN800,
  "__MONO400__":MONO400,"__MONO700__":MONO700,"__VIDEO__":VIDEO,"__POSTER__":POSTER,
}
for k,v in repl.items(): html=html.replace(k,v)

out=base/"hero-preview.html"
out.write_text(html)
print("wrote",out,round(len(html)/1024),"KB")
