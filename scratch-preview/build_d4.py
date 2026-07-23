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
VID_D="data:video/mp4;base64,"+b64(base/"evo-desktop.mp4")
VID_M="data:video/mp4;base64,"+b64(base/"evo-mobile.mp4")
POSTER="data:image/webp;base64,"+b64(base/"hero-poster.webp")
PATH='M25 0Q48 14 62.0 40.0Q76 66 76 96V605Q76 634 62.5 659.0Q49 684 25 698H611Q694 698 761.0 676.5Q828 655 867.0 605.0Q906 555 906 471Q906 395 869.0 337.5Q832 280 766.5 247.5Q701 215 615 215H358V90Q358 63 371.5 38.5Q385 14 409 0ZM358 358H505Q549 358 574.0 373.0Q599 388 609.0 411.5Q619 435 619 459Q619 513 584.5 532.5Q550 552 500 552H358Z'
PM='<svg class="pmark" viewBox="0 0 1021 838" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><g transform="translate(45,768) scale(1,-1)"><path d="'+PATH+'" fill="currentColor"/></g></svg>'

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
  font-family:var(--body);font-weight:800;font-size:14.5px;text-transform:uppercase;letter-spacing:.05em;cursor:pointer;overflow:hidden;
  transition:transform .25s var(--ease-spring),box-shadow .3s;white-space:nowrap;}
.btn:hover{transform:translateY(-2px);}.btn-block{width:100%;}
.btn-primary{background:linear-gradient(135deg,var(--pink),#ff5a8f 45%,var(--violet));background-size:200% 200%;color:#fff;
  box-shadow:0 12px 40px -8px rgba(255,23,63,.55);animation:gshift 6s ease infinite;}
@keyframes gshift{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
.stars{color:var(--gold);letter-spacing:2px;}
.live{width:8px;height:8px;border-radius:50%;background:var(--lime);box-shadow:0 0 12px var(--lime);animation:pd 1.6s infinite;flex:none;}
@keyframes pd{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.4;transform:scale(.7)}}
.pmark{display:inline-block;height:1em;width:auto;}
.hc{position:relative;z-index:5;height:100%;display:grid;grid-template-columns:1fr 400px;align-items:center;gap:44px;
  padding:clamp(80px,10vh,120px) clamp(24px,5vw,70px) clamp(40px,6vh,70px);}
@media(max-width:920px){.hc{grid-template-columns:1fr;align-content:center;}}
/* P bleeding from left — a bit smaller */
.bleed{position:absolute;left:calc(-1*(clamp(24px,5vw,70px) + clamp(6px,1.5vw,26px)));top:50%;transform:translateY(-50%);
  height:clamp(210px,32vw,430px);color:var(--pink);filter:drop-shadow(0 18px 46px rgba(255,23,63,.4));z-index:2;}
.bleed .pmark{height:100%;}
.left{position:relative;z-index:5;padding-left:clamp(66px,9vw,150px);}
.eyebrow{display:inline-flex;align-items:center;gap:10px;padding:8px 15px;border-radius:100px;background:rgba(255,255,255,.05);
  border:1px solid var(--line-strong);backdrop-filter:blur(10px);font-family:var(--mono);font-size:12px;letter-spacing:.05em;color:var(--muted);margin-bottom:24px;}
h1{font-family:var(--disp);font-weight:400;text-transform:uppercase;letter-spacing:.005em;color:#fff;line-height:.84;
  font-size:clamp(46px,6.4vw,104px);text-shadow:0 4px 24px rgba(0,0,0,.4);}
.sub{margin-top:24px;max-width:440px;font-size:clamp(15px,1.5vw,18px);color:#eceaeb;}
/* clean panel — no wordmark */
.panel{background:linear-gradient(180deg,rgba(20,16,23,.92),rgba(8,7,10,.95));border:1px solid var(--line-strong);
  border-radius:20px;padding:24px;backdrop-filter:blur(16px);box-shadow:0 40px 100px -35px rgba(0,0,0,.95);justify-self:end;width:100%;}
@media(max-width:920px){.panel{justify-self:stretch;max-width:440px;margin:0 auto;}}
.rateline{display:flex;align-items:center;gap:9px;font-size:12.5px;color:var(--muted);margin-bottom:16px;}
.rateline b{color:var(--cream);}
.price{font-family:var(--disp);font-size:46px;color:#fff;line-height:.9;margin-bottom:18px;}
.price s{font-family:var(--body);font-weight:700;font-size:17px;color:var(--muted-2);margin-right:8px;}
.price small{display:block;font-family:var(--mono);font-size:10px;letter-spacing:.08em;color:var(--muted);text-transform:uppercase;margin-top:5px;}
.plist{list-style:none;display:flex;flex-direction:column;gap:9px;margin:0 0 16px;}
.plist li{display:flex;align-items:center;gap:10px;font-size:13.5px;color:#d9d6d7;}
.plist svg{width:16px;height:16px;color:var(--lime);flex:none;}
.spots{display:inline-flex;align-items:center;gap:8px;font-size:12.5px;color:var(--gold);margin-bottom:14px;}
.rea{text-align:center;font-size:11px;color:var(--muted-2);margin-top:10px;}
@media(max-width:640px){
  .bleed{height:clamp(320px,80vw,460px);opacity:.14;left:50%;transform:translate(-50%,-50%);top:42%;}
  .left{padding-left:0;text-align:center;}
  .eyebrow{margin-left:auto;margin-right:auto;}
  h1{font-size:56px;}
  .sub{margin-left:auto;margin-right:auto;}
  .hc{padding-top:76px;}
}
@media(prefers-reduced-motion:reduce){*{animation:none!important;}}
</style></head><body>
<div class="hero">
  <video class="hbg" muted loop autoplay playsinline poster="__POSTER__" src="__VIDEO__"></video>
  <div class="veil"></div>
  <div class="hc">
    <div class="bleed">__PM__</div>
    <div class="left">
      <div class="eyebrow"><span class="live"></span> Project P · Porto</div>
      <h1>The Craziest<br>Night in Porto</h1>
      <p class="sub">The guided pub crawl locals warn you about — bars, boat, club, sunrise.</p>
    </div>
    <aside class="panel">
      <div class="rateline"><span class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span> <b>4.9</b> · 1,327+ reviews</div>
      <div class="price"><span><s>&euro;20</s>&euro;17</span><small>per person · tonight</small></div>
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
</div>
</body></html>"""
    doc=doc.replace("__PM__",PM).replace("__VIDEO__",video_uri).replace("__POSTER__",POSTER)
    for k,v in {"__ANTON__":ANTON,"__MAN400__":MAN400,"__MAN700__":MAN700,"__MAN800__":MAN800,
      "__MONO400__":MONO400,"__MONO700__":MONO700}.items():
        doc=doc.replace(k,v)
    return doc

def esc(s): return s.replace("&","&amp;").replace('"',"&quot;")
DOC_D=esc(hero_doc(VID_D)); DOC_M=esc(hero_doc(VID_M))

page=r"""<style>
:root{--pink:#ff173f;--cream:#f5f4f2;--muted:#a3a0a1;--line:rgba(245,244,242,.12);}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:#050406;color:var(--cream);font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;-webkit-font-smoothing:antialiased;padding:26px clamp(16px,4vw,48px) 70px;}
.head{max-width:1200px;margin:0 auto 24px;}
.head .k{font-family:ui-monospace,monospace;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);}
.head .k b{color:var(--pink);}
.head h1{font-size:clamp(19px,3vw,26px);font-weight:800;letter-spacing:-.02em;margin:8px 0 6px;}
.head p{color:var(--muted);font-size:14px;max-width:760px;line-height:1.6;}
.wrap{max-width:1200px;margin:0 auto;display:grid;grid-template-columns:1fr 400px;gap:30px;align-items:start;}
@media(max-width:1000px){.wrap{grid-template-columns:1fr;justify-items:center;}}
.col{width:100%;}.col h2{font-family:ui-monospace,monospace;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin-bottom:12px;display:flex;align-items:center;gap:8px;}
.col h2::before{content:"";width:20px;height:1px;background:var(--pink);}
.desk-frame{width:100%;border-radius:14px;overflow:hidden;border:1px solid var(--line);box-shadow:0 30px 70px -30px rgba(0,0,0,.9);background:#000;}
.desk-frame .bar{height:34px;background:#141017;display:flex;align-items:center;gap:7px;padding:0 14px;border-bottom:1px solid var(--line);}
.desk-frame .bar i{width:11px;height:11px;border-radius:50%;background:#3a3540;}
.desk-frame iframe{width:100%;height:620px;border:0;display:block;}
.phone{width:390px;max-width:88vw;}
.phone .device{position:relative;border-radius:44px;padding:12px;background:#141017;border:1px solid var(--line);box-shadow:0 40px 90px -30px rgba(0,0,0,.95);}
.phone .device::before{content:"";position:absolute;top:16px;left:50%;transform:translateX(-50%);width:120px;height:26px;background:#000;border-radius:0 0 16px 16px;z-index:3;}
.phone .screen{position:relative;border-radius:34px;overflow:hidden;background:#000;}
.phone iframe{width:100%;height:780px;border:0;display:block;}
.note{max-width:1200px;margin:32px auto 0;font-size:12.5px;color:var(--muted);line-height:1.7;border-top:1px solid var(--line);padding-top:20px;}
.note b{color:var(--cream);}
</style>
<div class="head">
  <div class="k">PORTO <b>PUB CRAWL</b> · D4 afinada · preview local (não publicado)</div>
  <h1>Hero D4 — P vermelho a sangrar (mais pequeno) · cartão limpo</h1>
  <p>Tirei o “Porto Pub Crawl” do cartão (agora só rating + preço + perks) e reduzi o P do hero, mantendo-o na mesma posição a sangrar pela esquerda.</p>
</div>
<div class="wrap">
  <div class="col"><h2>Desktop</h2>
    <div class="desk-frame"><div class="bar"><i></i><i></i><i></i></div><iframe srcdoc="__DOC_D__" title="Desktop"></iframe></div>
  </div>
  <div class="col phone"><h2>Mobile</h2>
    <div class="device"><div class="screen"><iframe srcdoc="__DOC_M__" title="Mobile"></iframe></div></div>
  </div>
</div>
<p class="note"><b>Preview local — nada publicado nem alterado no site.</b> No mobile, o P passa a marca de água subtil por trás (para o texto ficar legível). Vídeos comprimidos para o preview; no site real ficam em alta qualidade.</p>
"""
page=page.replace("__DOC_D__",DOC_D).replace("__DOC_M__",DOC_M)
out=base/"hero-d4-preview.html";out.write_text(page)
print("wrote",out,round(len(page)/1024),"KB")
