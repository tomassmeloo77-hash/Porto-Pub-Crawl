#!/usr/bin/env python3
import base64, pathlib
base = pathlib.Path("/home/user/Porto-Pub-Crawl/scratch-preview")
fdir = base/"fonts"/"node_modules"
def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()
def font_uri(p): return "data:font/woff2;base64," + b64(p)
ANTON=font_uri(fdir/"@fontsource/anton/files/anton-latin-400-normal.woff2")
MAN400=font_uri(fdir/"@fontsource/manrope/files/manrope-latin-400-normal.woff2")
MAN700=font_uri(fdir/"@fontsource/manrope/files/manrope-latin-700-normal.woff2")
MAN800=font_uri(fdir/"@fontsource/manrope/files/manrope-latin-800-normal.woff2")
MONO400=font_uri(fdir/"@fontsource/space-mono/files/space-mono-latin-400-normal.woff2")
MONO700=font_uri(fdir/"@fontsource/space-mono/files/space-mono-latin-700-normal.woff2")
VID="data:video/mp4;base64,"+b64(base/"evo-desktop.mp4")
POSTER="data:image/webp;base64,"+b64(base/"hero-poster.webp")

html=r"""<style>
@font-face{font-family:'Anton';src:url(__ANTON__) format('woff2');font-weight:400;font-display:swap;}
@font-face{font-family:'Manrope';src:url(__MAN400__) format('woff2');font-weight:400;font-display:swap;}
@font-face{font-family:'Manrope';src:url(__MAN700__) format('woff2');font-weight:700;font-display:swap;}
@font-face{font-family:'Manrope';src:url(__MAN800__) format('woff2');font-weight:800;font-display:swap;}
@font-face{font-family:'Space Mono';src:url(__MONO400__) format('woff2');font-weight:400;font-display:swap;}
@font-face{font-family:'Space Mono';src:url(__MONO700__) format('woff2');font-weight:700;font-display:swap;}
:root{--void:#08070a;--void-2:#0e0c10;--pink:#ff173f;--pink-soft:#ff5468;--violet:#7a0a1f;--violet-deep:#3c0512;
  --lime:#22ff7a;--gold:#ffc466;--cream:#f5f4f2;--muted:#a3a0a1;--muted-2:#7e7b7c;
  --line:rgba(245,244,242,.09);--line-strong:rgba(245,244,242,.16);--ease-spring:cubic-bezier(.34,1.56,.64,1);
  --disp:'Anton',Impact,sans-serif;--body:'Manrope',system-ui,sans-serif;--mono:'Space Mono',monospace;}
*{box-sizing:border-box;margin:0;padding:0;}
html,body{height:100%;}
body{background:#000;color:var(--cream);font-family:var(--body);-webkit-font-smoothing:antialiased;line-height:1.5;overflow:hidden;}
img,video{display:block;max-width:100%;}a{color:inherit;text-decoration:none;}
.deck{position:fixed;inset:0;}
.slide{position:absolute;inset:0;opacity:0;visibility:hidden;transition:opacity .5s ease;z-index:1;}
.slide.active{opacity:1;visibility:visible;z-index:2;}
.hero{position:absolute;inset:0;overflow:hidden;background:var(--void);}
.hbg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:0;filter:brightness(.5) saturate(1.15);}
.container{width:100%;max-width:1240px;margin:0 auto;padding:0 clamp(22px,5vw,64px);}
.btn{position:relative;display:inline-flex;align-items:center;justify-content:center;gap:10px;padding:17px 34px;border-radius:100px;
  font-family:var(--body);font-weight:800;font-size:15px;text-transform:uppercase;letter-spacing:.05em;cursor:pointer;overflow:hidden;
  transition:transform .25s var(--ease-spring),box-shadow .3s;white-space:nowrap;}
.btn:hover{transform:translateY(-2px);}
.btn-primary{background:linear-gradient(135deg,var(--pink),#ff5a8f 45%,var(--violet));background-size:200% 200%;color:#fff;
  box-shadow:0 12px 40px -8px rgba(255,23,63,.55);animation:gshift 6s ease infinite;}
@keyframes gshift{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
.btn-ghost{border:1.5px solid var(--line-strong);color:var(--cream);background:rgba(255,255,255,.04);backdrop-filter:blur(10px);}
.btn-ghost:hover{border-color:var(--pink);background:rgba(255,23,63,.1);}
.btn svg{width:16px;height:16px;}
.stars{color:var(--gold);letter-spacing:2px;}
.accent{background:linear-gradient(100deg,var(--pink) 0%,var(--pink) 38%,#fff 50%,var(--pink) 62%,var(--pink) 100%);
  background-size:280% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;animation:shine 6.5s linear infinite;}
@keyframes shine{0%{background-position:140% 0}100%{background-position:-140% 0}}
.live{width:8px;height:8px;border-radius:50%;background:var(--lime);box-shadow:0 0 12px var(--lime);animation:pd 1.6s infinite;flex:none;}
@keyframes pd{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.4;transform:scale(.7)}}
.eyebrow{display:inline-flex;align-items:center;gap:10px;padding:8px 16px;border-radius:100px;background:rgba(255,255,255,.05);
  border:1px solid var(--line-strong);backdrop-filter:blur(10px);font-family:var(--mono);font-size:12px;letter-spacing:.05em;color:var(--muted);}
.eyebrow strong{color:var(--cream);}
h1{font-family:var(--disp);font-weight:400;text-transform:uppercase;letter-spacing:.005em;color:#fff;text-shadow:0 4px 24px rgba(0,0,0,.4);}
.gsvg{display:block;}

/* ===== V1 — CENTER + VALUE BAR ===== */
.v1 .veil{position:absolute;inset:0;z-index:1;background:linear-gradient(180deg,rgba(8,7,10,.6),rgba(8,7,10,.05) 24%,rgba(8,7,10,.05) 52%,rgba(8,7,10,.85) 100%);}
.v1 .hc{position:relative;z-index:5;height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;}
.v1 h1{font-size:clamp(46px,7vw,104px);line-height:1.0;margin-top:24px;}
.v1 .sub{margin-top:20px;font-size:clamp(15px,1.7vw,20px);color:#fff;max-width:560px;font-weight:500;}
.v1 .cta{margin-top:32px;}
.v1 .valuebar{display:inline-flex;align-items:stretch;gap:0;margin-top:26px;border:1px solid var(--line-strong);border-radius:16px;
  overflow:hidden;background:rgba(8,7,10,.5);backdrop-filter:blur(12px);}
.v1 .valuebar .cell{display:flex;flex-direction:column;gap:3px;padding:12px 22px;border-right:1px solid var(--line);text-align:center;}
.v1 .valuebar .cell:last-child{border-right:none;}
.v1 .valuebar .t{font-size:11px;text-transform:uppercase;letter-spacing:.06em;color:var(--muted-2);font-weight:700;}
.v1 .valuebar .v{font-family:var(--disp);font-size:20px;color:var(--cream);display:inline-flex;align-items:center;gap:7px;justify-content:center;}
.v1 .valuebar .v.gold{color:var(--gold);}
@media(max-width:640px){.v1 .valuebar{flex-wrap:wrap;}.v1 .valuebar .cell{flex:1;min-width:33%;}}

/* ===== V2 — LEFT CINEMATIC ===== */
.v2 .veil{position:absolute;inset:0;z-index:1;background:linear-gradient(90deg,rgba(8,7,10,.85),rgba(8,7,10,.2) 55%,transparent),linear-gradient(0deg,rgba(8,7,10,.9),transparent 45%);}
.v2 .hc{position:relative;z-index:5;height:100%;display:flex;flex-direction:column;justify-content:flex-end;padding-bottom:clamp(46px,8vh,96px);}
.v2 .kick{font-family:var(--mono);font-size:13px;letter-spacing:.28em;text-transform:uppercase;color:var(--pink-soft);margin-bottom:18px;}
.v2 h1{font-size:clamp(52px,9vw,140px);line-height:.86;text-align:left;}
.v2 h1 em{font-style:normal;color:var(--pink);}
.v2 .sub{margin-top:22px;max-width:460px;font-size:clamp(15px,1.6vw,19px);color:#eceaeb;}
.v2 .row{display:flex;align-items:center;gap:16px;margin-top:30px;flex-wrap:wrap;}
.v2 .rate{display:inline-flex;align-items:center;gap:8px;font-size:13px;color:#fff;}
.v2 .rate b{font-family:var(--disp);font-size:18px;}
.v2 .pricetag{position:absolute;top:clamp(78px,12vh,110px);right:clamp(22px,5vw,64px);z-index:6;text-align:center;
  background:rgba(8,7,10,.55);border:1px solid var(--line-strong);border-radius:16px;padding:14px 20px;backdrop-filter:blur(12px);}
.v2 .pricetag .from{font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);}
.v2 .pricetag .amt{font-family:var(--disp);font-size:34px;color:#fff;line-height:1;}
.v2 .pricetag .amt s{font-size:16px;color:var(--muted-2);}

/* ===== V3 — CENTER + BOOKING CHIP ===== */
.v3 .veil{position:absolute;inset:0;z-index:1;background:radial-gradient(ellipse 70% 60% at 50% 40%,rgba(8,7,10,.35),rgba(8,7,10,.8)),linear-gradient(0deg,rgba(8,7,10,.85),transparent 60%);}
.v3 .hc{position:relative;z-index:5;height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;}
.v3 .eyebrow{margin-bottom:22px;}
.v3 h1{font-size:clamp(46px,7.2vw,108px);line-height:.96;}
.v3 h1 em{font-style:normal;color:var(--pink);}
.v3 .sub{margin-top:18px;font-size:clamp(15px,1.6vw,19px);color:#fff;max-width:520px;}
.v3 .chip{display:flex;align-items:center;gap:0;margin-top:30px;background:rgba(14,12,16,.7);border:1px solid var(--line-strong);
  border-radius:100px;padding:8px 8px 8px 24px;backdrop-filter:blur(16px);box-shadow:0 24px 60px -24px rgba(0,0,0,.9);flex-wrap:wrap;justify-content:center;}
.v3 .chip .p{font-family:var(--disp);font-size:28px;color:#fff;line-height:1;}
.v3 .chip .p s{font-size:15px;color:var(--muted-2);margin-right:6px;}
.v3 .chip .p small{font-family:var(--body);font-weight:700;font-size:12px;color:var(--muted);text-transform:uppercase;letter-spacing:.04em;margin-left:6px;}
.v3 .chip .sep{width:1px;height:34px;background:var(--line-strong);margin:0 20px;}
.v3 .chip .meta{font-size:12.5px;color:var(--cream);text-align:left;margin-right:18px;}
.v3 .chip .meta .g{display:inline-flex;align-items:center;gap:6px;}
.v3 .chip .btn{padding:14px 26px;font-size:13px;}
@media(max-width:640px){.v3 .chip .sep,.v3 .chip .meta{display:none;}}

/* ===== V4 — SPLIT PANEL ===== */
.v4 .veil{position:absolute;inset:0;z-index:1;background:linear-gradient(90deg,rgba(8,7,10,.5),rgba(8,7,10,.15) 45%,rgba(8,7,10,.65));}
.v4 .hc{position:relative;z-index:5;height:100%;display:grid;grid-template-columns:1fr 420px;align-items:center;gap:40px;
  padding:clamp(80px,10vh,120px) clamp(22px,5vw,64px) clamp(40px,6vh,70px);}
@media(max-width:900px){.v4 .hc{grid-template-columns:1fr;align-content:center;}}
.v4 .left h1{font-size:clamp(48px,7vw,110px);line-height:.9;margin-top:20px;}
.v4 .left .sub{margin-top:20px;max-width:440px;font-size:clamp(15px,1.5vw,18px);color:#eceaeb;}
.v4 .panel{background:linear-gradient(180deg,rgba(20,16,23,.9),rgba(8,7,10,.94));border:1px solid var(--line-strong);
  border-radius:20px;padding:26px;backdrop-filter:blur(16px);box-shadow:0 40px 100px -35px rgba(0,0,0,.95);justify-self:end;width:100%;}
@media(max-width:900px){.v4 .panel{justify-self:stretch;max-width:460px;margin:0 auto;}}
.v4 .panel .top{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:18px;}
.v4 .panel .price{font-family:var(--disp);font-size:44px;color:#fff;line-height:.9;}
.v4 .panel .price s{font-family:var(--body);font-weight:700;font-size:17px;color:var(--muted-2);margin-right:7px;}
.v4 .panel .price small{display:block;font-family:var(--mono);font-size:10px;letter-spacing:.08em;color:var(--muted);text-transform:uppercase;margin-top:4px;}
.v4 .panel .rate{text-align:right;font-size:12px;color:var(--muted);}.v4 .panel .rate b{color:var(--cream);}
.v4 .plist{list-style:none;display:flex;flex-direction:column;gap:9px;margin:0 0 16px;}
.v4 .plist li{display:flex;align-items:center;gap:10px;font-size:13.5px;color:#d9d6d7;}
.v4 .plist svg{width:16px;height:16px;color:var(--lime);flex:none;}
.v4 .spots{display:inline-flex;align-items:center;gap:8px;font-size:12.5px;color:var(--gold);margin-bottom:14px;}
.v4 .panel .btn{width:100%;}
.v4 .rea{text-align:center;font-size:11px;color:var(--muted-2);margin-top:10px;}

/* ===== V5 — SCARCITY POSTER ===== */
.v5 .strip{position:absolute;top:0;left:0;right:0;z-index:7;background:linear-gradient(90deg,var(--pink),var(--violet));
  color:#fff;font-weight:700;font-size:12px;letter-spacing:.02em;padding:9px 0;overflow:hidden;white-space:nowrap;}
.v5 .strip .tr{display:inline-flex;gap:30px;animation:sx 20s linear infinite;padding-left:100%;}
.v5 .strip b{font-weight:800;}
@keyframes sx{from{transform:translateX(0)}to{transform:translateX(-100%)}}
.v5 .veil{position:absolute;inset:0;z-index:1;background:linear-gradient(180deg,rgba(8,7,10,.6),rgba(8,7,10,.1) 30%,rgba(8,7,10,.1) 50%,rgba(8,7,10,.88));}
.v5 .hc{position:relative;z-index:5;height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;}
.v5 .meta{font-family:var(--mono);font-size:clamp(11px,1.4vw,14px);letter-spacing:.22em;text-transform:uppercase;color:var(--pink-soft);margin-bottom:20px;
  display:inline-flex;gap:14px;flex-wrap:wrap;justify-content:center;}
.v5 .meta .d{color:var(--muted-2);}
.v5 h1{font-size:clamp(50px,8.5vw,132px);line-height:.86;}
.v5 h1 em{font-style:normal;color:var(--pink);}
.v5 .sub{margin-top:22px;font-size:clamp(15px,1.7vw,20px);color:#fff;max-width:600px;font-weight:500;}
.v5 .cta{margin-top:32px;display:flex;gap:14px;flex-wrap:wrap;justify-content:center;}
.v5 .rating{margin-top:24px;display:inline-flex;align-items:center;gap:9px;font-size:13.5px;color:#fff;flex-wrap:wrap;justify-content:center;}
.v5 .rating b{font-family:var(--disp);font-size:18px;}

/* ===== controls ===== */
.switch{position:fixed;left:50%;bottom:clamp(16px,2.6vh,28px);transform:translateX(-50%);z-index:30;display:flex;gap:6px;
  background:rgba(8,7,10,.72);backdrop-filter:blur(16px);border:1px solid var(--line-strong);border-radius:100px;padding:7px 9px;max-width:calc(100vw - 20px);}
.switch button{font-family:var(--mono);font-size:11.5px;letter-spacing:.03em;color:var(--muted);background:transparent;border:0;border-radius:100px;
  padding:9px 13px;cursor:pointer;transition:.2s;white-space:nowrap;}
.switch button:hover{color:var(--cream);}
.switch button.on{background:var(--pink);color:#fff;}
.arrow{position:fixed;top:50%;transform:translateY(-50%);z-index:30;width:44px;height:44px;border-radius:50%;background:rgba(8,7,10,.55);
  backdrop-filter:blur(10px);border:1px solid var(--line-strong);color:var(--cream);display:flex;align-items:center;justify-content:center;cursor:pointer;}
.arrow:hover{background:rgba(255,23,63,.25);border-color:var(--pink);}
.arrow.prev{left:clamp(10px,2vw,22px);}.arrow.next{right:clamp(10px,2vw,22px);}.arrow svg{width:20px;height:20px;}
.tagline{position:fixed;top:14px;left:50%;transform:translateX(-50%);z-index:30;font-family:var(--mono);font-size:11px;letter-spacing:.12em;
  text-transform:uppercase;color:var(--muted-2);background:rgba(8,7,10,.6);backdrop-filter:blur(10px);border:1px solid var(--line);
  border-radius:100px;padding:7px 15px;white-space:nowrap;max-width:calc(100vw - 20px);overflow:hidden;text-overflow:ellipsis;}
.tagline b{color:var(--pink);}
@media(max-width:640px){.arrow{display:none;}.v4 .hc{padding-top:70px;}}
@media(prefers-reduced-motion:reduce){*{animation:none!important;}}
</style>

<div class="tagline">Hero refinado · <b id="tl">V1 · Centro + value bar</b> · preview local (não publicado)</div>
<div class="deck">

  <!-- V1 -->
  <section class="slide active v1" data-name="V1 · Centro + value bar">
   <div class="hero"><video class="hbg hv" muted loop autoplay playsinline></video><div class="veil"></div>
    <div class="container hc">
      <div class="eyebrow"><span class="live"></span> Porto's #1 Pub Crawl · <strong>from &euro;17</strong></div>
      <h1>The <span class="accent">Craziest</span><br>Porto Pub Crawl</h1>
      <p class="sub">From the producers of The Hangover and Project X.</p>
      <div class="cta"><a class="btn btn-primary">Reserve My Spot &mdash; &euro;17 <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a></div>
      <div class="valuebar">
        <div class="cell"><span class="t">Rated</span><span class="v gold"><span class="stars">&#9733;</span>4.9 · 1,327+</span></div>
        <div class="cell"><span class="t">Tonight</span><span class="v"><span class="live"></span>7 left</span></div>
        <div class="cell"><span class="t">From</span><span class="v">&euro;17</span></div>
        <div class="cell"><span class="t">Booking</span><span class="v">Free cancel</span></div>
      </div>
    </div>
   </div>
  </section>

  <!-- V2 -->
  <section class="slide v2" data-name="V2 · Esquerda cinematográfica">
   <div class="hero"><video class="hbg hv" muted loop autoplay playsinline></video><div class="veil"></div>
    <div class="pricetag"><div class="from">From</div><div class="amt"><s>&euro;20</s> &euro;17</div></div>
    <div class="container hc">
      <div class="kick">Porto · Nightlife · Since 2025</div>
      <h1>Get Loud.<br><em>Get Lost.</em></h1>
      <p class="sub">One wristband, five venues and a crew from 60+ countries. Free shots, skip-the-line club, zero planning.</p>
      <div class="row">
        <a class="btn btn-primary">Reserve My Spot <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        <a class="btn btn-ghost">Watch the reel</a>
        <span class="rate"><span class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span> <b>4.9</b> · 1,327+</span>
      </div>
    </div>
   </div>
  </section>

  <!-- V3 -->
  <section class="slide v3" data-name="V3 · Centro + chip de reserva">
   <div class="hero"><video class="hbg hv" muted loop autoplay playsinline></video><div class="veil"></div>
    <div class="container hc">
      <div class="eyebrow"><span class="live"></span> Live tonight · 9PM · Porto</div>
      <h1>Porto's <em>Craziest</em><br>Night Out</h1>
      <p class="sub">Guided bar-hop, free shots, VIP club entry and an instant crew.</p>
      <div class="chip">
        <div class="p"><s>&euro;20</s>&euro;17<small>/ person</small></div>
        <div class="sep"></div>
        <div class="meta"><div class="g"><span class="stars">&#9733;</span> 4.9 · 1,327+ reviews</div><div class="g"><span class="live"></span> 7 spots left tonight</div></div>
        <a class="btn btn-primary">Reserve <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
      </div>
    </div>
   </div>
  </section>

  <!-- V4 -->
  <section class="slide v4" data-name="V4 · Split com painel">
   <div class="hero"><video class="hbg hv" muted loop autoplay playsinline></video><div class="veil"></div>
    <div class="hc">
      <div class="left">
        <div class="eyebrow"><span class="live"></span> Porto's #1 Pub Crawl</div>
        <h1>The <span class="accent">Craziest</span><br>Night in Porto</h1>
        <p class="sub">Five venues, one legendary night — from the producers of The Hangover &amp; Project X.</p>
      </div>
      <aside class="panel">
        <div class="top">
          <div class="price"><span><s>&euro;20</s>&euro;17</span><small>per person</small></div>
          <div class="rate"><span class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span><br><b>4.9</b> · 1,327+</div>
        </div>
        <ul class="plist">
          <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>9 free drinks — beer, sangria &amp; shots</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>VIP entry · 4 bars + 1 nightclub</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>Free photos &amp; video next day</li>
        </ul>
        <div class="spots"><span class="live"></span> Only 7 spots left tonight</div>
        <a class="btn btn-primary">Reserve My Spot &mdash; &euro;17</a>
        <p class="rea">1-min checkout · Free cancellation up to 24h</p>
      </aside>
    </div>
   </div>
  </section>

  <!-- V5 -->
  <section class="slide v5" data-name="V5 · Scarcity poster">
   <div class="hero"><video class="hbg hv" muted loop autoplay playsinline></video>
    <div class="strip"><div class="tr"><span>🔥 Tonight's crawl is filling up — <b>7 spots left</b></span><span>·</span><span>Free cancellation up to 24h</span><span>·</span><span>From <b>€17</b></span><span>·</span><span>🔥 Tonight's crawl is filling up — <b>7 spots left</b></span><span>·</span><span>From <b>€17</b></span></div></div>
    <div class="veil"></div>
    <div class="container hc">
      <div class="meta"><span>5 Venues</span><span class="d">/</span><span>9PM Start</span><span class="d">/</span><span>Porto</span></div>
      <h1>One Wristband.<br><em>Zero Memory.</em></h1>
      <p class="sub">Porto's craziest guided pub crawl — bars, boat, club and a crew you haven't met yet.</p>
      <div class="cta"><a class="btn btn-primary">Reserve My Spot &mdash; &euro;17 <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a></div>
      <div class="rating"><span class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span> <b>4.9</b> · 1,327+ Positive Hangover Reviews</div>
    </div>
   </div>
  </section>
</div>

<button class="arrow prev" aria-label="Previous"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M15 18l-6-6 6-6"/></svg></button>
<button class="arrow next" aria-label="Next"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M9 6l6 6-6 6"/></svg></button>
<nav class="switch">
  <button class="on" data-i="0">V1 Value bar</button>
  <button data-i="1">V2 Cinematic</button>
  <button data-i="2">V3 Chip</button>
  <button data-i="3">V4 Split</button>
  <button data-i="4">V5 Scarcity</button>
</nav>

<script>
  var VID="__VID__",POSTER="__POSTER__";
  document.querySelectorAll('video.hv').forEach(function(v){v.poster=POSTER;v.src=VID;v.muted=true;v.setAttribute('playsinline','');});
  var slides=[].slice.call(document.querySelectorAll('.slide')),btns=[].slice.call(document.querySelectorAll('.switch button')),tl=document.getElementById('tl'),cur=0;
  function pa(){slides.forEach(function(s,i){s.querySelectorAll('video').forEach(function(v){if(i===cur){var p=v.play();if(p&&p.catch)p.catch(function(){});}else{try{v.pause();}catch(e){}}});});}
  function go(i){cur=(i+slides.length)%slides.length;slides.forEach(function(s,k){s.classList.toggle('active',k===cur);});btns.forEach(function(b,k){b.classList.toggle('on',k===cur);});tl.textContent=slides[cur].dataset.name;pa();}
  btns.forEach(function(b){b.addEventListener('click',function(){go(+b.dataset.i);});});
  document.querySelector('.arrow.prev').addEventListener('click',function(){go(cur-1);});
  document.querySelector('.arrow.next').addEventListener('click',function(){go(cur+1);});
  document.addEventListener('keydown',function(e){if(e.key==='ArrowRight')go(cur+1);else if(e.key==='ArrowLeft')go(cur-1);else if(e.key>='1'&&e.key<='5')go(+e.key-1);});
  pa();
</script>
"""
for k,v in {"__ANTON__":ANTON,"__MAN400__":MAN400,"__MAN700__":MAN700,"__MAN800__":MAN800,
  "__MONO400__":MONO400,"__MONO700__":MONO700,"__VID__":VID,"__POSTER__":POSTER}.items():
    html=html.replace(k,v)
out=base/"hero-more-preview.html";out.write_text(html)
print("wrote",out,round(len(html)/1024),"KB")
