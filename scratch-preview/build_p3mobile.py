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
VID_M="data:video/mp4;base64,"+b64(base/"evo-mobile.mp4")
POSTER="data:image/webp;base64,"+b64(base/"hero-poster.webp")
PATH='M25 0Q48 14 62.0 40.0Q76 66 76 96V605Q76 634 62.5 659.0Q49 684 25 698H611Q694 698 761.0 676.5Q828 655 867.0 605.0Q906 555 906 471Q906 395 869.0 337.5Q832 280 766.5 247.5Q701 215 615 215H358V90Q358 63 371.5 38.5Q385 14 409 0ZM358 358H505Q549 358 574.0 373.0Q599 388 609.0 411.5Q619 435 619 459Q619 513 584.5 532.5Q550 552 500 552H358Z'
PM='<svg class="pmark" viewBox="0 0 1021 838"><g transform="translate(45,768) scale(1,-1)"><path d="'+PATH+'" fill="currentColor"/></g></svg>'
GOOGLE_C='<svg viewBox="0 0 18 18"><path fill="#4285F4" d="M17.64 9.2c0-.637-.057-1.251-.164-1.84H9v3.481h4.844c-.209 1.125-.843 2.078-1.796 2.717v2.258h2.908c1.702-1.567 2.684-3.874 2.684-6.615z"/><path fill="#34A853" d="M9 18c2.43 0 4.467-.806 5.956-2.18l-2.908-2.259c-.806.54-1.837.86-3.048.86-2.344 0-4.328-1.584-5.036-3.711H.957v2.332C2.438 15.983 5.482 18 9 18z"/><path fill="#FBBC05" d="M3.964 10.71c-.18-.54-.282-1.117-.282-1.71s.102-1.17.282-1.71V4.958H.957C.348 6.173 0 7.548 0 9s.348 2.827.957 4.042l3.007-2.332z"/><path fill="#EA4335" d="M9 3.58c1.321 0 2.508.454 3.44 1.345l2.582-2.58C13.463.891 11.426 0 9 0 5.482 0 2.438 2.017.957 4.958L3.964 7.29C4.672 5.163 6.656 3.58 9 3.58z"/></svg>'
TP='<svg viewBox="0 0 24 24"><path fill="#00B67A" d="M12 1.5l3.09 6.26 6.91 1-5 4.87 1.18 6.87L12 17.25l-6.18 3.25L7 13.63l-5-4.87 6.91-1L12 1.5z"/></svg>'

HERO=r"""<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><style>
@font-face{font-family:'Anton';src:url(__ANTON__) format('woff2');font-weight:400;font-display:swap;}
@font-face{font-family:'Manrope';src:url(__MAN400__) format('woff2');font-weight:400;font-display:swap;}
@font-face{font-family:'Manrope';src:url(__MAN700__) format('woff2');font-weight:700;font-display:swap;}
@font-face{font-family:'Manrope';src:url(__MAN800__) format('woff2');font-weight:800;font-display:swap;}
@font-face{font-family:'Space Mono';src:url(__MONO400__) format('woff2');font-weight:400;font-display:swap;}
:root{--void:#08070a;--pink:#ff173f;--violet:#7a0a1f;--gold:#ffc466;--lime:#22ff7a;--cream:#f5f4f2;--muted:#a3a0a1;--muted-2:#7e7b7c;
  --line:rgba(245,244,242,.09);--line-strong:rgba(245,244,242,.16);--ease-spring:cubic-bezier(.34,1.56,.64,1);
  --disp:'Anton',Impact,sans-serif;--body:'Manrope',system-ui,sans-serif;--mono:'Space Mono',monospace;}
*{box-sizing:border-box;margin:0;padding:0;}html,body{height:100%;}
body{background:var(--void);color:var(--cream);font-family:var(--body);-webkit-font-smoothing:antialiased;line-height:1.5;overflow:hidden;}
video{display:block;}
.hero{position:relative;height:100%;min-height:100svh;overflow:hidden;display:flex;flex-direction:column;justify-content:center;padding:74px 20px 26px;}
.hbg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:0;filter:brightness(.5) saturate(1.15);}
.veil{position:absolute;inset:0;z-index:1;background:linear-gradient(180deg,rgba(8,7,10,.5),rgba(8,7,10,.08) 30%,rgba(8,7,10,.85));}
.pbig{position:absolute;left:50%;top:38%;transform:translate(-50%,-50%);height:min(82vw,440px);color:var(--pink);opacity:.16;z-index:2;}
.pbig .pmark{height:100%;width:auto;display:block;}
.hc{position:relative;z-index:5;text-align:center;display:flex;flex-direction:column;align-items:center;}
h1{font-family:var(--disp);font-weight:400;text-transform:uppercase;letter-spacing:.005em;color:#fff;line-height:.86;font-size:54px;text-shadow:0 6px 30px rgba(0,0,0,.6);}
.sub{margin:16px auto 0;max-width:300px;font-size:14px;color:#eceaeb;}
.panel{margin:26px auto 0;width:100%;max-width:400px;background:linear-gradient(180deg,rgba(20,16,23,.95),rgba(8,7,10,.97));
  border:1px solid var(--line-strong);border-radius:20px;padding:22px;backdrop-filter:blur(16px);box-shadow:0 30px 70px -30px rgba(0,0,0,.95);text-align:left;}
.phead{display:flex;align-items:center;justify-content:space-between;gap:10px;}
.badges{display:inline-flex;align-items:center;gap:13px;}
.badges .bg{display:inline-flex;align-items:center;gap:5px;font-size:11.5px;font-weight:700;color:var(--cream);}
.badges .bg svg{height:15px;width:auto;display:block;}
.rate{display:inline-flex;align-items:center;gap:6px;}.rate .stars{color:var(--gold);letter-spacing:1.5px;font-size:11px;}.rate .rnum{font-family:var(--disp);font-size:16px;}
.revline{font-size:11px;color:var(--muted-2);margin-top:7px;}.revline b{color:var(--muted);}
.hr{height:1px;background:var(--line);margin:14px 0;}
.price{font-family:var(--disp);font-size:42px;color:#fff;line-height:.9;margin-bottom:14px;}
.price s{font-family:var(--body);font-weight:700;font-size:16px;color:var(--muted-2);margin-right:7px;}
.price small{display:block;font-family:var(--mono);font-size:9.5px;letter-spacing:.08em;color:var(--muted);text-transform:uppercase;margin-top:5px;}
.plist{list-style:none;display:flex;flex-direction:column;gap:9px;margin:0 0 14px;}
.plist li{display:flex;align-items:center;gap:9px;font-size:13px;color:#e2dfe0;}
.plist svg{width:15px;height:15px;color:var(--lime);flex:none;}
.spots{display:inline-flex;align-items:center;gap:8px;font-size:12px;color:var(--gold);margin-bottom:14px;}
.spots .live{width:8px;height:8px;border-radius:50%;background:var(--pink);box-shadow:0 0 12px var(--pink);animation:pd 1.6s infinite;flex:none;}
@keyframes pd{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.4;transform:scale(.7)}}
.btn{display:flex;width:100%;align-items:center;justify-content:center;gap:9px;padding:16px;border-radius:100px;font-family:var(--body);
  font-weight:800;font-size:14px;text-transform:uppercase;letter-spacing:.05em;color:#fff;
  background:linear-gradient(135deg,var(--pink),#ff5a8f 45%,var(--violet));background-size:200% 200%;box-shadow:0 12px 40px -8px rgba(255,23,63,.55);animation:gshift 6s ease infinite;}
@keyframes gshift{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
.rea{text-align:center;font-size:10.5px;color:var(--muted-2);margin-top:10px;}
@media(prefers-reduced-motion:reduce){*{animation:none!important;}}
</style></head><body>
<div class="hero">
  <video class="hbg" muted loop autoplay playsinline poster="__POSTER__" src="__VIDEO__"></video>
  <div class="veil"></div>
  <div class="pbig">__PM__</div>
  <div class="hc">
    <h1>The Craziest<br>Night in Porto</h1>
    <p class="sub">The guided pub crawl locals warn you about — bars, boat, club, sunrise.</p>
    <aside class="panel">
      <div class="phead"><div class="badges"><span class="bg">__GOOGLE__ <span>Google</span></span><span class="bg">__TP__ <span>Trustpilot</span></span></div>
        <div class="rate"><span class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span><span class="rnum">4.9</span></div></div>
      <div class="revline">Rated <b>excellent</b> by <b>1,327+</b> crawlers</div>
      <div class="hr"></div>
      <div class="price"><span><s>&euro;20</s>&euro;17</span><small>per person</small></div>
      <ul class="plist">
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>9 free drinks — beer, sangria &amp; shots</li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>VIP entry · 4 bars + 1 nightclub</li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>Free photos &amp; video next day</li>
      </ul>
      <div class="spots"><span class="live"></span> Only 7 spots left tonight</div>
      <a class="btn">Reserve My Spot &mdash; &euro;17</a>
      <p class="rea">1-min checkout · Free cancellation up to 24h</p>
    </aside>
  </div>
</div></body></html>"""
HERO=HERO.replace("__PM__",PM).replace("__GOOGLE__",GOOGLE_C).replace("__TP__",TP).replace("__VIDEO__",VID_M).replace("__POSTER__",POSTER)
for k,v in {"__ANTON__":ANTON,"__MAN400__":MAN400,"__MAN700__":MAN700,"__MAN800__":MAN800,"__MONO400__":MONO400}.items():
    HERO=HERO.replace(k,v)
def esc(s): return s.replace("&","&amp;").replace('"',"&quot;")
DOC=esc(HERO)
page=r"""<style>
:root{--pink:#ff173f;--cream:#f5f4f2;--muted:#a3a0a1;--line:rgba(245,244,242,.12);}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:#050406;color:var(--cream);font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;-webkit-font-smoothing:antialiased;
  min-height:100vh;padding:30px 16px 60px;display:flex;flex-direction:column;align-items:center;}
.head{text-align:center;max-width:640px;margin-bottom:24px;}
.head .k{font-family:ui-monospace,monospace;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);}.head .k b{color:var(--pink);}
.head h1{font-size:clamp(18px,3vw,24px);font-weight:800;letter-spacing:-.02em;margin:8px 0 6px;}
.head p{color:var(--muted);font-size:13.5px;line-height:1.6;}
.phone{width:400px;max-width:92vw;}
.phone .device{position:relative;border-radius:48px;padding:13px;background:#141017;border:1px solid var(--line);box-shadow:0 50px 110px -35px rgba(0,0,0,.96);}
.phone .device::before{content:"";position:absolute;top:17px;left:50%;transform:translateX(-50%);width:126px;height:28px;background:#000;border-radius:0 0 17px 17px;z-index:3;}
.phone .screen{position:relative;border-radius:36px;overflow:hidden;background:#000;}
.phone iframe{width:100%;height:850px;border:0;display:block;}
.note{max-width:640px;margin:26px auto 0;font-size:12px;color:var(--muted);line-height:1.7;text-align:center;}
.note b{color:var(--cream);}
</style>
<div class="head"><div class="k">PORTO <b>PUB CRAWL</b> · P3 · mobile</div>
<h1>Mobile do hero P3</h1>
<p>A mesma versão P3 que aprovaste, agora no telemóvel: P como marca de água subtil por trás do título centrado, e o card de reserva a toda a largura.</p></div>
<div class="phone"><div class="device"><div class="screen"><iframe srcdoc="__DOC__" title="Mobile P3"></iframe></div></div></div>
<p class="note"><b>Preview local — nada publicado nem alterado no site.</b> Vídeo comprimido para o preview; no site real fica em alta qualidade com poster.</p>
"""
page=page.replace("__DOC__",DOC)
out=base/"hero-p3-mobile-preview.html";out.write_text(page)
print("wrote",out,round(len(page)/1024),"KB")
