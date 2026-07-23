#!/usr/bin/env python3
import base64, pathlib, re
root = pathlib.Path("/home/user/Porto-Pub-Crawl")
base = root/"scratch-preview"; fdir = base/"fonts"/"node_modules"
def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()
def fu(p): return "data:font/woff2;base64," + b64(p)
ANTON=fu(fdir/"@fontsource/anton/files/anton-latin-400-normal.woff2")
MAN400=fu(fdir/"@fontsource/manrope/files/manrope-latin-400-normal.woff2")
MAN700=fu(fdir/"@fontsource/manrope/files/manrope-latin-700-normal.woff2")
MAN800=fu(fdir/"@fontsource/manrope/files/manrope-latin-800-normal.woff2")
MONO=fu(fdir/"@fontsource/space-mono/files/space-mono-latin-400-normal.woff2")
PATH='M25 0Q48 14 62.0 40.0Q76 66 76 96V605Q76 634 62.5 659.0Q49 684 25 698H611Q694 698 761.0 676.5Q828 655 867.0 605.0Q906 555 906 471Q906 395 869.0 337.5Q832 280 766.5 247.5Q701 215 615 215H358V90Q358 63 371.5 38.5Q385 14 409 0ZM358 358H505Q549 358 574.0 373.0Q599 388 609.0 411.5Q619 435 619 459Q619 513 584.5 532.5Q550 552 500 552H358Z'
PM='<svg class="xb-pmark" viewBox="0 0 1021 838"><g transform="translate(45,768) scale(1,-1)"><path d="'+PATH+'" fill="currentColor"/></g></svg>'
GOOGLE='<svg viewBox="0 0 18 18"><path fill="#4285F4" d="M17.64 9.2c0-.637-.057-1.251-.164-1.84H9v3.481h4.844c-.209 1.125-.843 2.078-1.796 2.717v2.258h2.908c1.702-1.567 2.684-3.874 2.684-6.615z"/><path fill="#34A853" d="M9 18c2.43 0 4.467-.806 5.956-2.18l-2.908-2.259c-.806.54-1.837.86-3.048.86-2.344 0-4.328-1.584-5.036-3.711H.957v2.332C2.438 15.983 5.482 18 9 18z"/><path fill="#FBBC05" d="M3.964 10.71c-.18-.54-.282-1.117-.282-1.71s.102-1.17.282-1.71V4.958H.957C.348 6.173 0 7.548 0 9s.348 2.827.957 4.042l3.007-2.332z"/><path fill="#EA4335" d="M9 3.58c1.321 0 2.508.454 3.44 1.345l2.582-2.58C13.463.891 11.426 0 9 0 5.482 0 2.438 2.017.957 4.958L3.964 7.29C4.672 5.163 6.656 3.58 9 3.58z"/></svg>'
TP='<svg viewBox="0 0 24 24"><path fill="#00B67A" d="M12 1.5l3.09 6.26 6.91 1-5 4.87 1.18 6.87L12 17.25l-6.18 3.25L7 13.63l-5-4.87 6.91-1L12 1.5z"/></svg>'
CRAWL="https://book.stripe.com/cNi8wReAZ8di9m29LI4AU02"

# ===== CSS copied verbatim from the P3 (desktop) and M5 (mobile) previews, scoped to .hero.xb =====
CSS = """
@font-face{font-family:'Anton';src:url(%s) format('woff2');font-weight:400;font-display:swap;}
@font-face{font-family:'Manrope';src:url(%s) format('woff2');font-weight:400;font-display:swap;}
@font-face{font-family:'Manrope';src:url(%s) format('woff2');font-weight:700;font-display:swap;}
@font-face{font-family:'Manrope';src:url(%s) format('woff2');font-weight:800;font-display:swap;}
@font-face{font-family:'Space Mono';src:url(%s) format('woff2');font-weight:400;font-display:swap;}
/* hide site chrome so the hero is exactly like the previews */
.strip{display:none!important;}
#nav{display:none!important;}
/* ===== P3 DESKTOP (verbatim values) ===== */
.hero.xb{padding-top:0;}
.hero.xb .xb-hbg{position:absolute;inset:0;width:100%%;height:100%%;object-fit:cover;z-index:0;filter:brightness(.5) saturate(1.15);}
.hero.xb .xb-m{display:none;}
.hero.xb .xb-veil{position:absolute;inset:0;z-index:1;background:linear-gradient(90deg,rgba(8,7,10,.55),rgba(8,7,10,.12) 42%%,rgba(8,7,10,.66));}
.hero.xb .xb-hc{position:relative;z-index:5;min-height:100svh;display:grid;grid-template-columns:1fr 400px;align-items:center;gap:44px;padding:clamp(80px,10vh,120px) clamp(24px,5vw,70px) clamp(40px,6vh,70px);}
.hero.xb .xb-stage{display:contents;}
.hero.xb .xb-pbig{position:absolute;top:50%%;transform:translateY(-50%%);color:var(--pink);z-index:2;filter:drop-shadow(0 18px 46px rgba(255,23,63,.4));pointer-events:none;height:clamp(240px,32vw,440px);left:clamp(20px,3vw,58px);}
.hero.xb .xb-pmark{display:block;height:100%%;width:auto;}
.hero.xb .xb-left{position:relative;z-index:5;padding-left:clamp(58px,10vw,180px);text-align:left;}
.hero.xb .xb-left h1{font-family:'Anton',sans-serif;font-weight:400;text-transform:uppercase;letter-spacing:.005em;color:#fff;line-height:.84;font-size:clamp(46px,6.4vw,104px);text-shadow:0 6px 30px rgba(0,0,0,.55);margin:0;}
.hero.xb .xb-left .xb-sub{margin-top:24px;max-width:440px;font-size:clamp(15px,1.5vw,18px);color:#eceaeb;font-weight:500;}
.hero.xb .xb-card{background:linear-gradient(180deg,rgba(20,16,23,.93),rgba(8,7,10,.96));border:1px solid var(--line-strong);border-radius:20px;padding:26px;backdrop-filter:blur(16px);box-shadow:0 40px 100px -35px rgba(0,0,0,.95);justify-self:end;width:100%%;display:flex;flex-direction:column;}
.hero.xb .xb-chead{display:flex;align-items:center;justify-content:space-between;gap:12px;}
.hero.xb .xb-badges{display:inline-flex;align-items:center;gap:16px;}
.hero.xb .xb-badges .b{display:inline-flex;align-items:center;gap:6px;font-size:12.5px;font-weight:700;color:var(--cream);}
.hero.xb .xb-badges .b svg{height:16px;width:auto;display:block;}
.hero.xb .xb-crate{display:inline-flex;align-items:center;gap:7px;}
.hero.xb .xb-crate .stars{font-size:12px;color:var(--gold);}
.hero.xb .xb-crate .rn{font-family:'Anton',sans-serif;font-size:17px;color:var(--cream);}
.hero.xb .xb-revl{font-size:11.5px;color:var(--muted-2);margin-top:8px;}.hero.xb .xb-revl b{color:var(--muted);}
.hero.xb .xb-hr{height:1px;background:var(--line);margin:16px 0 18px;}
.hero.xb .xb-price{font-family:'Anton',sans-serif;font-size:48px;color:#fff;line-height:.9;margin-bottom:18px;}
.hero.xb .xb-price s{font-family:'Manrope',sans-serif;font-weight:700;font-size:18px;color:var(--muted-2);margin-right:8px;}
.hero.xb .xb-price small{display:block;font-family:'Space Mono',monospace;font-size:10px;letter-spacing:.08em;color:var(--muted);text-transform:uppercase;margin-top:6px;}
.hero.xb .xb-plist{list-style:none;display:flex;flex-direction:column;gap:11px;margin:0 0 18px;padding:0;}
.hero.xb .xb-plist li{display:flex;align-items:center;gap:10px;font-size:14px;color:#e2dfe0;}
.hero.xb .xb-plist svg{width:16px;height:16px;color:var(--lime);flex:none;}
.hero.xb .xb-spots{display:inline-flex;align-items:center;gap:8px;font-size:12.5px;color:var(--gold);margin-bottom:16px;}
.hero.xb .xb-dot{width:8px;height:8px;border-radius:50%%;background:var(--pink);box-shadow:0 0 12px var(--pink);animation:xbpd 1.6s infinite;flex:none;}
@keyframes xbpd{0%%,100%%{opacity:1;transform:scale(1)}50%%{opacity:.4;transform:scale(.7)}}
.hero.xb .xb-rea{text-align:center;font-size:11px;color:var(--muted-2);margin-top:12px;}
.hero.xb .xb-card .btn{width:100%%;}
/* ===== M5 MOBILE (verbatim values) ===== */
@media(max-width:920px){
  .hero.xb .xb-d{display:none;} .hero.xb .xb-m{display:block;}
  .hero.xb .xb-veil{background:linear-gradient(180deg,rgba(8,7,10,.5),rgba(8,7,10,.08) 30%%,rgba(8,7,10,.86));}
  .hero.xb .xb-hbg{height:100%%;bottom:0;}
  .hero.xb .xb-stage{display:contents;}
  .hero.xb .xb-hc{display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;min-height:100svh;padding:0 16px;position:relative;gap:0;}
  .hero.xb .xb-pbig{position:absolute;left:50%%;top:50%%;height:216px;margin:0;transform:translate(-50%%,-262px);z-index:4;filter:drop-shadow(0 16px 44px rgba(255,23,63,.45));}
  .hero.xb .xb-left{width:100%%;box-sizing:border-box;padding:0;margin:0;position:relative;z-index:5;display:block;text-align:center;transform:translateY(-8px);}
  .hero.xb .xb-left h1{font-size:58px;line-height:.85;text-shadow:0 6px 30px rgba(0,0,0,.65);}
  .hero.xb .xb-left .xb-sub{margin:12px auto 0;max-width:300px;font-size:12.5px;}
  .hero.xb .xb-card{position:absolute;left:16px;right:16px;bottom:20px;z-index:5;flex:none;justify-self:auto;margin:0;max-width:none;width:auto;padding:16px 16px 18px;text-align:left;}
  .hero.xb .xb-hr{display:block;margin:12px 0 12px;}
  .hero.xb .xb-price{display:none;}
  .hero.xb .xb-plist{display:none;}
  .hero.xb .xb-spots{margin:2px 0 12px;justify-content:flex-start;}
  .hero.xb .xb-chead{gap:9px;}
  .hero.xb .xb-badges{gap:12px;}
  .hero.xb .xb-badges .b{gap:5px;font-size:11px;}
  .hero.xb .xb-badges .b svg{height:14px;}
  .hero.xb .xb-crate{gap:6px;}
  .hero.xb .xb-crate .stars{letter-spacing:1.5px;font-size:10.5px;}
  .hero.xb .xb-crate .rn{font-size:15px;}
  .hero.xb .xb-revl{font-size:10.5px;margin-top:6px;}
  .hero.xb .xb-hr{margin:11px 0;}
  .hero.xb .xb-price{font-size:38px;margin-bottom:11px;}
  .hero.xb .xb-price s{font-size:15px;margin-right:7px;}
  .hero.xb .xb-price small{font-size:9px;margin-top:4px;}
  .hero.xb .xb-plist{gap:8px;margin:0 0 11px;}
  .hero.xb .xb-plist li{gap:8px;font-size:12.5px;}
  .hero.xb .xb-plist svg{width:14px;height:14px;}
  .hero.xb .xb-spots{font-size:11.5px;margin-bottom:11px;}
  .hero.xb .xb-rea{font-size:10px;margin-top:8px;}
  .hero.xb .xb-card .btn{padding:14px;font-size:13.5px;}
}
""" % (ANTON,MAN400,MAN700,MAN800,MONO)

CHK='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>'
HERO = '''<header class="hero xb" id="top">
  <video class="xb-hbg xb-d" autoplay muted loop playsinline poster="assets/hero-video-poster.webp"><source src="assets/hero-video-desktop.mp4" type="video/mp4"></video>
  <video class="xb-hbg xb-m" autoplay muted loop playsinline poster="assets/hero-video-poster.webp"><source src="assets/hero-video-mobile.mp4" type="video/mp4"></video>
  <div class="xb-veil"></div>
  <div class="xb-hc">
    <div class="xb-pbig">__PM__</div>
    <div class="xb-left">
      <h1>The Craziest<br>Night in Porto</h1>
      <p class="xb-sub">The guided pub crawl locals warn you about — bars, boat, club, sunrise.</p>
    </div>
    <aside class="xb-card">
      <div class="xb-chead"><div class="xb-badges"><span class="b">__GOOGLE__ <span>Google</span></span><span class="b">__TP__ <span>Trustpilot</span></span></div>
        <div class="xb-crate"><span class="stars">★★★★★</span><span class="rn">4.9</span></div></div>
      <div class="xb-revl">Rated <b>excellent</b> by <b>1,327+</b> crawlers</div>
      <div class="xb-hr"></div>
      <div class="xb-price"><span><s>€20</s>€17</span><small>per person</small></div>
      <ul class="xb-plist"><li>__CHK__ 9 free drinks — beer, sangria &amp; shots</li><li>__CHK__ VIP entry · 4 bars + 1 nightclub</li><li>__CHK__ Free photos &amp; video next day</li></ul>
      <div class="xb-spots"><span class="xb-dot"></span> Only 7 spots left tonight</div>
      <a href="__CRAWL__" target="_blank" rel="noopener" class="btn btn-primary magnetic js-book-crawl"><span class="shine"></span>Reserve My Spot — €17</a>
      <p class="xb-rea">1-min checkout · Free cancellation up to 24h</p>
    </aside>
  </div>
</header>'''
HERO=HERO.replace("__PM__",PM).replace("__GOOGLE__",GOOGLE).replace("__TP__",TP).replace("__CHK__",CHK).replace("__CRAWL__",CRAWL)

src = root/"index.html"; out = root/"index-b.html"
html = src.read_text()
start = html.index('<header class="hero" id="top">')
end = html.index('</header>', start) + len('</header>')
html = html[:start] + HERO + html[end:]
# version B drops the experiences (offer cards) section entirely
try:
    es = html.index('<section id="experiences">'); ee = html.index('<section id="gallery">')
    html = html[:es] + html[ee:]
except ValueError:
    pass
i = html.index('</style>')
html = html[:i] + CSS + html[i:]
out.write_text(html)
print("index-b.html regenerated (verbatim P3/M5);", round(len(html)/1024), "KB")
