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
VID_D="data:video/mp4;base64,"+b64(base/"evo-desktop.mp4")
VID_M="data:video/mp4;base64,"+b64(base/"evo-mobile.mp4")
POSTER="data:image/webp;base64,"+b64(base/"hero-poster.webp")
PATH='M25 0Q48 14 62.0 40.0Q76 66 76 96V605Q76 634 62.5 659.0Q49 684 25 698H611Q694 698 761.0 676.5Q828 655 867.0 605.0Q906 555 906 471Q906 395 869.0 337.5Q832 280 766.5 247.5Q701 215 615 215H358V90Q358 63 371.5 38.5Q385 14 409 0ZM358 358H505Q549 358 574.0 373.0Q599 388 609.0 411.5Q619 435 619 459Q619 513 584.5 532.5Q550 552 500 552H358Z'
PM='<svg class="pmark" viewBox="0 0 1021 838"><g transform="translate(45,768) scale(1,-1)"><path d="'+PATH+'" fill="currentColor"/></g></svg>'
GOOGLE_C='<svg viewBox="0 0 18 18"><path fill="#4285F4" d="M17.64 9.2c0-.637-.057-1.251-.164-1.84H9v3.481h4.844c-.209 1.125-.843 2.078-1.796 2.717v2.258h2.908c1.702-1.567 2.684-3.874 2.684-6.615z"/><path fill="#34A853" d="M9 18c2.43 0 4.467-.806 5.956-2.18l-2.908-2.259c-.806.54-1.837.86-3.048.86-2.344 0-4.328-1.584-5.036-3.711H.957v2.332C2.438 15.983 5.482 18 9 18z"/><path fill="#FBBC05" d="M3.964 10.71c-.18-.54-.282-1.117-.282-1.71s.102-1.17.282-1.71V4.958H.957C.348 6.173 0 7.548 0 9s.348 2.827.957 4.042l3.007-2.332z"/><path fill="#EA4335" d="M9 3.58c1.321 0 2.508.454 3.44 1.345l2.582-2.58C13.463.891 11.426 0 9 0 5.482 0 2.438 2.017.957 4.958L3.964 7.29C4.672 5.163 6.656 3.58 9 3.58z"/></svg>'
TP='<svg viewBox="0 0 24 24"><path fill="#00B67A" d="M12 1.5l3.09 6.26 6.91 1-5 4.87 1.18 6.87L12 17.25l-6.18 3.25L7 13.63l-5-4.87 6.91-1L12 1.5z"/></svg>'

def hero_doc(video_uri):
    doc=r"""<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><style>
@font-face{font-family:'Anton';src:url(__ANTON__) format('woff2');font-weight:400;font-display:swap;}
@font-face{font-family:'Manrope';src:url(__MAN400__) format('woff2');font-weight:400;font-display:swap;}
@font-face{font-family:'Manrope';src:url(__MAN700__) format('woff2');font-weight:700;font-display:swap;}
@font-face{font-family:'Manrope';src:url(__MAN800__) format('woff2');font-weight:800;font-display:swap;}
@font-face{font-family:'Space Mono';src:url(__MONO400__) format('woff2');font-weight:400;font-display:swap;}
:root{--void:#08070a;--pink:#ff173f;--pink-soft:#ff5468;--violet:#7a0a1f;--gold:#ffc466;--lime:#22ff7a;
  --cream:#f5f4f2;--muted:#a3a0a1;--muted-2:#7e7b7c;--line:rgba(245,244,242,.09);--line-strong:rgba(245,244,242,.16);
  --ease-spring:cubic-bezier(.34,1.56,.64,1);--disp:'Anton',Impact,sans-serif;--body:'Manrope',system-ui,sans-serif;--mono:'Space Mono',monospace;}
*{box-sizing:border-box;margin:0;padding:0;}html,body{height:100%;}
body{background:var(--void);color:var(--cream);font-family:var(--body);-webkit-font-smoothing:antialiased;line-height:1.5;overflow:hidden;}
img,video{display:block;max-width:100%;}a{color:inherit;text-decoration:none;}
.hero{position:relative;height:100%;min-height:100svh;overflow:hidden;background:var(--void);}
.hbg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:0;filter:brightness(.5) saturate(1.15);}
.veil{position:absolute;inset:0;z-index:1;background:linear-gradient(90deg,rgba(8,7,10,.55),rgba(8,7,10,.12) 42%,rgba(8,7,10,.66));}
.btn{position:relative;display:inline-flex;align-items:center;justify-content:center;gap:10px;padding:16px 30px;border-radius:100px;
  font-family:var(--body);font-weight:800;font-size:14.5px;text-transform:uppercase;letter-spacing:.05em;cursor:pointer;overflow:hidden;transition:transform .25s var(--ease-spring),box-shadow .3s;white-space:nowrap;}
.btn:hover{transform:translateY(-2px);}.btn-block{width:100%;}
.btn-primary{background:linear-gradient(135deg,var(--pink),#ff5a8f 45%,var(--violet));background-size:200% 200%;color:#fff;box-shadow:0 12px 40px -8px rgba(255,23,63,.55);animation:gshift 6s ease infinite;}
@keyframes gshift{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
.stars{color:var(--gold);letter-spacing:2px;}
.live{width:8px;height:8px;border-radius:50%;background:var(--lime);box-shadow:0 0 12px var(--lime);animation:pd 1.6s infinite;flex:none;}
@keyframes pd{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.4;transform:scale(.7)}}
.pmark{display:inline-block;height:1em;width:auto;}
.hc{position:relative;z-index:5;height:100%;display:grid;grid-template-columns:1fr 400px;align-items:center;gap:44px;
  padding:clamp(80px,10vh,120px) clamp(24px,5vw,70px) clamp(40px,6vh,70px);}
@media(max-width:920px){.hc{grid-template-columns:1fr;align-content:center;}}
.left{position:relative;z-index:5;padding-left:clamp(58px,10vw,180px);}
h1{font-family:var(--disp);font-weight:400;text-transform:uppercase;letter-spacing:.005em;color:#fff;line-height:.84;font-size:clamp(46px,6.4vw,104px);text-shadow:0 6px 30px rgba(0,0,0,.55);}
.sub{margin-top:24px;max-width:440px;font-size:clamp(15px,1.5vw,18px);color:#eceaeb;}
/* P3 geometry */
.pbig{position:absolute;top:50%;transform:translateY(-50%);color:var(--pink);z-index:2;pointer-events:none;
  filter:drop-shadow(0 18px 46px rgba(255,23,63,.4));height:clamp(240px,32vw,440px);left:clamp(20px,3vw,58px);}
.pbig .pmark{height:100%;}
.panel{background:linear-gradient(180deg,rgba(20,16,23,.93),rgba(8,7,10,.96));border:1px solid var(--line-strong);
  border-radius:20px;padding:26px;backdrop-filter:blur(16px);box-shadow:0 40px 100px -35px rgba(0,0,0,.95);justify-self:end;width:100%;display:flex;flex-direction:column;}
@media(max-width:920px){.panel{justify-self:stretch;max-width:440px;margin:0 auto;}}
.phead{display:flex;align-items:center;justify-content:space-between;gap:12px;}
.badges{display:inline-flex;align-items:center;gap:16px;}
.badges .bg{display:inline-flex;align-items:center;gap:6px;font-size:12.5px;font-weight:700;color:var(--cream);}
.badges .bg svg{height:16px;width:auto;display:block;}
.rate{display:inline-flex;align-items:center;gap:7px;}.rate .stars{font-size:12px;}.rate .rnum{font-family:var(--disp);font-size:17px;color:var(--cream);}
.revline{font-size:11.5px;color:var(--muted-2);margin-top:8px;}.revline b{color:var(--muted);}
.hr{height:1px;background:var(--line);margin:16px 0 18px;}
.price{font-family:var(--disp);font-size:48px;color:#fff;line-height:.9;margin-bottom:18px;}
.price s{font-family:var(--body);font-weight:700;font-size:18px;color:var(--muted-2);margin-right:8px;}
.price small{display:block;font-family:var(--mono);font-size:10px;letter-spacing:.08em;color:var(--muted);text-transform:uppercase;margin-top:6px;}
.plist{list-style:none;display:flex;flex-direction:column;gap:11px;margin:0 0 18px;}
.plist li{display:flex;align-items:center;gap:10px;font-size:14px;color:#e2dfe0;}
.plist svg{width:16px;height:16px;color:var(--lime);flex:none;}
.spots{display:inline-flex;align-items:center;gap:8px;font-size:12.5px;color:var(--gold);margin-bottom:16px;}
.spots .live{background:var(--pink);box-shadow:0 0 12px var(--pink);}
.rea{text-align:center;font-size:11px;color:var(--muted-2);margin-top:12px;}
@media(max-width:920px){.pbig{opacity:.14;left:50%;transform:translate(-50%,-50%);height:min(80vw,460px);}
  .left{padding-left:0;text-align:center;}.sub{margin-left:auto;margin-right:auto;}}
@media(max-width:640px){h1{font-size:52px;}.hc{padding-top:76px;}}
@media(prefers-reduced-motion:reduce){*{animation:none!important;}}
</style></head><body>
<div class="hero">
  <video class="hbg" muted loop autoplay playsinline poster="__POSTER__" src="__VIDEO__"></video>
  <div class="veil"></div>
  <div class="hc">
    <div class="pbig">__PM__</div>
    <div class="left"><h1>The Craziest<br>Night in Porto</h1>
      <p class="sub">The guided pub crawl locals warn you about — bars, boat, club, sunrise.</p></div>
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
      <a class="btn btn-primary btn-block">Reserve My Spot &mdash; &euro;17</a>
      <p class="rea">1-min checkout · Free cancellation up to 24h</p>
    </aside>
  </div>
</div></body></html>"""
    doc=doc.replace("__PM__",PM).replace("__GOOGLE__",GOOGLE_C).replace("__TP__",TP).replace("__VIDEO__",video_uri).replace("__POSTER__",POSTER)
    for k,v in {"__ANTON__":ANTON,"__MAN400__":MAN400,"__MAN700__":MAN700,"__MAN800__":MAN800,"__MONO400__":MONO400}.items():
        doc=doc.replace(k,v)
    return doc

def esc(s): return s.replace("&","&amp;").replace('"',"&quot;")
DOC_D=esc(hero_doc(VID_D)); DOC_M=esc(hero_doc(VID_M))
page=r"""<style>
:root{--pink:#ff173f;--cream:#f5f4f2;--muted:#a3a0a1;--line:rgba(245,244,242,.12);}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:#050406;color:var(--cream);font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;-webkit-font-smoothing:antialiased;padding:26px clamp(16px,4vw,48px) 70px;}
.head{max-width:1200px;margin:0 auto 24px;}.head .k{font-family:ui-monospace,monospace;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);}.head .k b{color:var(--pink);}
.head h1{font-size:clamp(19px,3vw,26px);font-weight:800;letter-spacing:-.02em;margin:8px 0 6px;}.head p{color:var(--muted);font-size:14px;max-width:760px;line-height:1.6;}
.wrap{max-width:1200px;margin:0 auto;display:grid;grid-template-columns:1fr 400px;gap:30px;align-items:start;}
@media(max-width:1000px){.wrap{grid-template-columns:1fr;justify-items:center;}}
.col{width:100%;}.col h2{font-family:ui-monospace,monospace;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin-bottom:12px;display:flex;align-items:center;gap:8px;}
.col h2::before{content:"";width:20px;height:1px;background:var(--pink);}
.desk-frame{width:100%;border-radius:14px;overflow:hidden;border:1px solid var(--line);box-shadow:0 30px 70px -30px rgba(0,0,0,.9);background:#000;}
.desk-frame .bar{height:34px;background:#141017;display:flex;align-items:center;gap:7px;padding:0 14px;border-bottom:1px solid var(--line);}
.desk-frame .bar i{width:11px;height:11px;border-radius:50%;background:#3a3540;}
.desk-frame iframe{width:100%;height:620px;border:0;display:block;}
.phone{width:390px;max-width:88vw;}.phone .device{position:relative;border-radius:44px;padding:12px;background:#141017;border:1px solid var(--line);box-shadow:0 40px 90px -30px rgba(0,0,0,.95);}
.phone .device::before{content:"";position:absolute;top:16px;left:50%;transform:translateX(-50%);width:120px;height:26px;background:#000;border-radius:0 0 16px 16px;z-index:3;}
.phone .screen{position:relative;border-radius:34px;overflow:hidden;background:#000;}.phone iframe{width:100%;height:780px;border:0;display:block;}
.note{max-width:1200px;margin:32px auto 0;font-size:12.5px;color:var(--muted);line-height:1.7;border-top:1px solid var(--line);padding-top:20px;}.note b{color:var(--cream);}
</style>
<div class="head"><div class="k">PORTO <b>PUB CRAWL</b> · versão final P3 · preview local (não publicado)</div>
<h1>Hero final — P3 (P mais pequeno + margem), selos reais, luz vermelha</h1>
<p>Desktop e mobile da versão que fixámos. No mobile o P passa a marca de água subtil e o card fica a toda a largura.</p></div>
<div class="wrap">
  <div class="col"><h2>Desktop</h2><div class="desk-frame"><div class="bar"><i></i><i></i><i></i></div><iframe srcdoc="__DOC_D__" title="Desktop"></iframe></div></div>
  <div class="col phone"><h2>Mobile</h2><div class="device"><div class="screen"><iframe srcdoc="__DOC_M__" title="Mobile"></iframe></div></div></div>
</div>
<p class="note"><b>Preview local — nada publicado nem alterado no site.</b> Vídeos comprimidos para o preview; no site real ficam em alta qualidade com poster.</p>
"""
page=page.replace("__DOC_D__",DOC_D).replace("__DOC_M__",DOC_M)
out=base/"hero-p3-final-preview.html";out.write_text(page)
print("wrote",out,round(len(page)/1024),"KB")
