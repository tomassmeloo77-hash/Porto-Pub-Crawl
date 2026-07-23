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

# real Project P mark (from the site favicon), fill=currentColor
PMARK='<svg class="pmark" viewBox="0 0 1021 838" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><g transform="translate(45,768) scale(1,-1)"><path d="M25 0Q48 14 62.0 40.0Q76 66 76 96V605Q76 634 62.5 659.0Q49 684 25 698H611Q694 698 761.0 676.5Q828 655 867.0 605.0Q906 555 906 471Q906 395 869.0 337.5Q832 280 766.5 247.5Q701 215 615 215H358V90Q358 63 371.5 38.5Q385 14 409 0ZM358 358H505Q549 358 574.0 373.0Q599 388 609.0 411.5Q619 435 619 459Q619 513 584.5 532.5Q550 552 500 552H358Z" fill="currentColor"/></g></svg>'

# shared booking panel
PANEL=r"""<aside class="panel">
  <div class="ptop"><div class="brandmark">__PMARK__</div>
    <div class="rate"><span class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span><br><b>4.9</b> · 1,327+</div></div>
  <div class="price"><span><s>&euro;20</s>&euro;17</span><small>per person · tonight</small></div>
  <ul class="plist">
    <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>9 free drinks — beer, sangria &amp; shots</li>
    <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>VIP entry · 4 bars + 1 nightclub</li>
    <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>Free photos &amp; video next day</li>
  </ul>
  <div class="spots"><span class="live"></span> Only 7 spots left tonight</div>
  <a class="btn btn-primary btn-block">Reserve My Spot &mdash; &euro;17</a>
  <p class="rea">1-min checkout · Free cancellation up to 24h</p>
</aside>""".replace("__PMARK__",PMARK)

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
.veil{position:absolute;inset:0;z-index:1;background:linear-gradient(90deg,rgba(8,7,10,.55),rgba(8,7,10,.12) 42%,rgba(8,7,10,.66));}
.btn{position:relative;display:inline-flex;align-items:center;justify-content:center;gap:10px;padding:16px 30px;border-radius:100px;
  font-family:var(--body);font-weight:800;font-size:14.5px;text-transform:uppercase;letter-spacing:.05em;cursor:pointer;overflow:hidden;
  transition:transform .25s var(--ease-spring),box-shadow .3s;white-space:nowrap;}
.btn:hover{transform:translateY(-2px);}
.btn-block{width:100%;}
.btn-primary{background:linear-gradient(135deg,var(--pink),#ff5a8f 45%,var(--violet));background-size:200% 200%;color:#fff;
  box-shadow:0 12px 40px -8px rgba(255,23,63,.55);animation:gshift 6s ease infinite;}
@keyframes gshift{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
.stars{color:var(--gold);letter-spacing:2px;}
.live{width:8px;height:8px;border-radius:50%;background:var(--lime);box-shadow:0 0 12px var(--lime);animation:pd 1.6s infinite;flex:none;}
@keyframes pd{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.4;transform:scale(.7)}}
.accent{background:linear-gradient(100deg,var(--pink) 0%,var(--pink) 38%,#fff 50%,var(--pink) 62%,var(--pink) 100%);
  background-size:280% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;animation:shine 6.5s linear infinite;}
@keyframes shine{0%{background-position:140% 0}100%{background-position:-140% 0}}
.pmark{display:inline-block;height:1em;width:auto;vertical-align:middle;}

/* shared split layout */
.split .hc{position:relative;z-index:5;height:100%;display:grid;grid-template-columns:1fr 400px;align-items:center;gap:44px;
  padding:clamp(80px,10vh,120px) clamp(24px,5vw,70px) clamp(40px,6vh,70px);}
@media(max-width:920px){.split .hc{grid-template-columns:1fr;align-content:center;}}
.split .left{position:relative;}
.eyebrow{display:inline-flex;align-items:center;gap:10px;padding:8px 15px;border-radius:100px;background:rgba(255,255,255,.05);
  border:1px solid var(--line-strong);backdrop-filter:blur(10px);font-family:var(--mono);font-size:12px;letter-spacing:.05em;color:var(--muted);margin-bottom:24px;}
.eyebrow strong{color:var(--cream);}
.left h1{font-family:var(--disp);font-weight:400;text-transform:uppercase;letter-spacing:.005em;color:#fff;line-height:.9;
  font-size:clamp(46px,6.6vw,104px);text-shadow:0 4px 24px rgba(0,0,0,.4);}
.left .sub{margin-top:22px;max-width:440px;font-size:clamp(15px,1.5vw,18px);color:#eceaeb;}
/* panel */
.panel{background:linear-gradient(180deg,rgba(20,16,23,.92),rgba(8,7,10,.95));border:1px solid var(--line-strong);
  border-radius:20px;padding:24px;backdrop-filter:blur(16px);box-shadow:0 40px 100px -35px rgba(0,0,0,.95);justify-self:end;width:100%;}
@media(max-width:920px){.panel{justify-self:stretch;max-width:440px;margin:0 auto;}}
.panel .ptop{display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;}
.panel .brandmark{color:var(--pink);height:30px;display:flex;align-items:center;}
.panel .brandmark .pmark{height:30px;}
.panel .rate{text-align:right;font-size:12px;color:var(--muted);line-height:1.35;}.panel .rate b{color:var(--cream);}
.panel .price{font-family:var(--disp);font-size:44px;color:#fff;line-height:.9;margin-bottom:16px;}
.panel .price s{font-family:var(--body);font-weight:700;font-size:17px;color:var(--muted-2);margin-right:7px;}
.panel .price small{display:block;font-family:var(--mono);font-size:10px;letter-spacing:.08em;color:var(--muted);text-transform:uppercase;margin-top:5px;}
.plist{list-style:none;display:flex;flex-direction:column;gap:9px;margin:0 0 16px;}
.plist li{display:flex;align-items:center;gap:10px;font-size:13.5px;color:#d9d6d7;}
.plist svg{width:16px;height:16px;color:var(--lime);flex:none;}
.spots{display:inline-flex;align-items:center;gap:8px;font-size:12.5px;color:var(--gold);margin-bottom:14px;}
.rea{text-align:center;font-size:11px;color:var(--muted-2);margin-top:10px;}

/* ---- P treatments ---- */
/* s1 watermark */
.s1 .watermark{position:absolute;z-index:2;left:-8%;top:50%;transform:translateY(-50%);height:150%;color:var(--pink);opacity:.1;pointer-events:none;}
.s1 .watermark .pmark{height:100%;}
.s1 .left{z-index:5;}
/* s2 wordmark P as letter */
.s2 .word{display:flex;align-items:center;line-height:.82;}
.s2 .word .pmark{height:.92em;color:var(--pink);margin-right:.02em;filter:drop-shadow(0 4px 18px rgba(255,23,63,.4));}
/* s3 stroke title */
.s3 .left h1 .stroke{-webkit-text-stroke:2px var(--pink);color:transparent;}
.s3 .seal{display:inline-flex;align-items:center;justify-content:center;width:34px;height:34px;border-radius:50%;background:var(--pink);color:#fff;margin-right:2px;}
.s3 .seal .pmark{height:17px;}
/* s4 monogram lockup */
.s4 .lock{display:flex;align-items:center;gap:14px;margin-bottom:20px;}
.s4 .lock .badge{width:52px;height:52px;border-radius:14px;background:var(--pink);color:#fff;display:grid;place-items:center;box-shadow:0 12px 30px -10px rgba(255,23,63,.7);}
.s4 .lock .badge .pmark{height:26px;}
.s4 .lock .txt{font-family:var(--mono);font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);line-height:1.5;}
.s4 .lock .txt b{color:var(--cream);display:block;font-family:var(--body);font-weight:800;font-size:14px;letter-spacing:.02em;}
.s4 .ghostP{position:absolute;right:-4%;bottom:-18%;height:120%;color:#fff;opacity:.04;z-index:2;pointer-events:none;}
.s4 .ghostP .pmark{height:100%;}
/* s5 numbers + P on seam */
.s5 .left h1 .n{color:var(--gold);}
.s5 .seam{position:absolute;z-index:6;left:calc(100% - 400px - 22px);top:50%;transform:translate(-50%,-50%);color:var(--pink);
  height:120px;filter:drop-shadow(0 10px 30px rgba(255,23,63,.5));}
.s5 .seam .pmark{height:120px;}
@media(max-width:920px){.s5 .seam{display:none;}}
.s5 .left .kick{font-family:var(--mono);font-size:12px;letter-spacing:.24em;text-transform:uppercase;color:var(--pink-soft);margin-bottom:18px;display:inline-flex;align-items:center;gap:9px;}

/* controls */
.switch{position:fixed;left:50%;bottom:clamp(16px,2.6vh,28px);transform:translateX(-50%);z-index:30;display:flex;gap:6px;
  background:rgba(8,7,10,.72);backdrop-filter:blur(16px);border:1px solid var(--line-strong);border-radius:100px;padding:7px 9px;max-width:calc(100vw - 20px);}
.switch button{font-family:var(--mono);font-size:11.5px;letter-spacing:.03em;color:var(--muted);background:transparent;border:0;border-radius:100px;
  padding:9px 13px;cursor:pointer;transition:.2s;white-space:nowrap;}
.switch button:hover{color:var(--cream);}.switch button.on{background:var(--pink);color:#fff;}
.arrow{position:fixed;top:50%;transform:translateY(-50%);z-index:30;width:44px;height:44px;border-radius:50%;background:rgba(8,7,10,.55);
  backdrop-filter:blur(10px);border:1px solid var(--line-strong);color:var(--cream);display:flex;align-items:center;justify-content:center;cursor:pointer;}
.arrow:hover{background:rgba(255,23,63,.25);border-color:var(--pink);}
.arrow.prev{left:clamp(10px,2vw,22px);}.arrow.next{right:clamp(10px,2vw,22px);}.arrow svg{width:20px;height:20px;}
.tagline{position:fixed;top:14px;left:50%;transform:translateX(-50%);z-index:30;font-family:var(--mono);font-size:11px;letter-spacing:.12em;
  text-transform:uppercase;color:var(--muted-2);background:rgba(8,7,10,.6);backdrop-filter:blur(10px);border:1px solid var(--line);
  border-radius:100px;padding:7px 15px;white-space:nowrap;max-width:calc(100vw - 20px);overflow:hidden;text-overflow:ellipsis;}
.tagline b{color:var(--pink);}
@media(max-width:640px){.arrow{display:none;}}
@media(prefers-reduced-motion:reduce){*{animation:none!important;}}
</style>

<div class="tagline">V4 · split + painel · brincar com título &amp; ícone <b id="tl">P1 · Watermark P</b> · preview local</div>
<div class="deck">

  <!-- P1 watermark -->
  <section class="slide active split s1" data-name="P1 · Watermark P">
   <div class="hero"><video class="hbg hv" muted loop autoplay playsinline></video><div class="veil"></div>
    <div class="watermark">__PMARK__</div>
    <div class="hc">
      <div class="left">
        <div class="eyebrow"><span class="live"></span> Porto's #1 Pub Crawl</div>
        <h1>The <span class="accent">Craziest</span><br>Night in Porto</h1>
        <p class="sub">Five venues, one legendary night — from the producers of The Hangover &amp; Project X.</p>
      </div>
      __PANEL__
    </div>
   </div>
  </section>

  <!-- P2 wordmark -->
  <section class="slide split s2" data-name="P2 · P dentro de PORTO">
   <div class="hero"><video class="hbg hv" muted loop autoplay playsinline></video><div class="veil"></div>
    <div class="hc">
      <div class="left">
        <div class="eyebrow"><span class="live"></span> The Original Since 2025</div>
        <h1><span class="word">__PMARK__ORTO</span><span>Pub Crawl</span></h1>
        <p class="sub">Skip the planning. One wristband, five venues, free shots and an instant crew.</p>
      </div>
      __PANEL__
    </div>
   </div>
  </section>

  <!-- P3 stroke -->
  <section class="slide split s3" data-name="P3 · Título stroke + selo">
   <div class="hero"><video class="hbg hv" muted loop autoplay playsinline></video><div class="veil"></div>
    <div class="hc">
      <div class="left">
        <div class="eyebrow"><span class="seal">__PMARK__</span> Project P · Porto</div>
        <h1>Get Loud.<br><span class="stroke">Get Lost.</span></h1>
        <p class="sub">The guided pub crawl locals warn you about. Bars, boat, club — home before sunrise, optional.</p>
      </div>
      __PANEL__
    </div>
   </div>
  </section>

  <!-- P4 monogram lockup -->
  <section class="slide split s4" data-name="P4 · Lockup monograma">
   <div class="hero"><video class="hbg hv" muted loop autoplay playsinline></video><div class="veil"></div>
    <div class="ghostP">__PMARK__</div>
    <div class="hc">
      <div class="left">
        <div class="lock"><div class="badge">__PMARK__</div><div class="txt">Project P presents<b>Porto Pub Crawl</b></div></div>
        <h1>Porto,<br><span class="accent">After Dark</span></h1>
        <p class="sub">Five venues, free shots, VIP club entry and a crowd from 60+ countries.</p>
      </div>
      __PANEL__
    </div>
   </div>
  </section>

  <!-- P5 numbers + seam P -->
  <section class="slide split s5" data-name="P5 · Números + P na costura">
   <div class="hero"><video class="hbg hv" muted loop autoplay playsinline></video><div class="veil"></div>
    <div class="hc">
      <div class="left">
        <div class="kick"><span class="live"></span> 5 Venues · 9PM · Porto</div>
        <h1><span class="n">5</span> Bars. <span class="n">1</span> Club.<br><span class="n">0</span> Regrets.</h1>
        <p class="sub">Porto's craziest guided pub crawl — one wristband does it all.</p>
      </div>
      __PANEL__
    </div>
    <div class="seam">__PMARK__</div>
   </div>
  </section>
</div>

<button class="arrow prev" aria-label="Previous"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M15 18l-6-6 6-6"/></svg></button>
<button class="arrow next" aria-label="Next"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M9 6l6 6-6 6"/></svg></button>
<nav class="switch">
  <button class="on" data-i="0">P1 Watermark</button>
  <button data-i="1">P2 PORTO</button>
  <button data-i="2">P3 Stroke</button>
  <button data-i="3">P4 Lockup</button>
  <button data-i="4">P5 Números</button>
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
html=html.replace("__PANEL__",PANEL).replace("__PMARK__",PMARK)
for k,v in {"__ANTON__":ANTON,"__MAN400__":MAN400,"__MAN700__":MAN700,"__MAN800__":MAN800,
  "__MONO400__":MONO400,"__MONO700__":MONO700,"__VID__":VID,"__POSTER__":POSTER}.items():
    html=html.replace(k,v)
out=base/"hero-v4-preview.html";out.write_text(html)
print("wrote",out,round(len(html)/1024),"KB")
