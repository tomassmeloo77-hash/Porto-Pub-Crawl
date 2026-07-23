#!/usr/bin/env python3
import base64, pathlib

base = pathlib.Path("/home/user/Porto-Pub-Crawl/scratch-preview")
fdir = base/"fonts"/"node_modules"
def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()
def font_uri(p): return "data:font/woff2;base64," + b64(p)

ANTON   = font_uri(fdir/"@fontsource/anton/files/anton-latin-400-normal.woff2")
MAN400  = font_uri(fdir/"@fontsource/manrope/files/manrope-latin-400-normal.woff2")
MAN700  = font_uri(fdir/"@fontsource/manrope/files/manrope-latin-700-normal.woff2")
MAN800  = font_uri(fdir/"@fontsource/manrope/files/manrope-latin-800-normal.woff2")
MONO400 = font_uri(fdir/"@fontsource/space-mono/files/space-mono-latin-400-normal.woff2")
MONO700 = font_uri(fdir/"@fontsource/space-mono/files/space-mono-latin-700-normal.woff2")
VID_D = "data:video/mp4;base64," + b64(base/"evo-desktop.mp4")
VID_M = "data:video/mp4;base64," + b64(base/"evo-mobile.mp4")

# ---- faithful hero doc (their real CSS + video bg + price/urgency) ----
def hero_doc(video_uri):
    return r"""<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<style>
@font-face{font-family:'Anton';src:url(__ANTON__) format('woff2');font-weight:400;font-display:swap;}
@font-face{font-family:'Manrope';src:url(__MAN400__) format('woff2');font-weight:400;font-display:swap;}
@font-face{font-family:'Manrope';src:url(__MAN700__) format('woff2');font-weight:700;font-display:swap;}
@font-face{font-family:'Manrope';src:url(__MAN800__) format('woff2');font-weight:800;font-display:swap;}
@font-face{font-family:'Space Mono';src:url(__MONO400__) format('woff2');font-weight:400;font-display:swap;}
@font-face{font-family:'Space Mono';src:url(__MONO700__) format('woff2');font-weight:700;font-display:swap;}
:root{
  --void:#08070a;--surface-3:#232325;--pink:#ff173f;--pink-soft:#ff5468;--violet:#7a0a1f;--violet-deep:#3c0512;
  --lime:#22ff7a;--gold:#ffc466;--cream:#f5f4f2;--muted:#a3a0a1;--muted-2:#7e7b7c;
  --line:rgba(245,244,242,0.09);--line-strong:rgba(245,244,242,0.16);
  --ease:cubic-bezier(.16,.84,.44,1);--ease-spring:cubic-bezier(.34,1.56,.64,1);
}
*{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{background:var(--void);color:var(--cream);font-family:'Manrope',sans-serif;overflow-x:hidden;-webkit-font-smoothing:antialiased;}
h1,h2,h3{font-family:'Anton',sans-serif;font-weight:400;text-transform:uppercase;letter-spacing:.01em;line-height:.92;}
.container{max-width:1240px;margin:0 auto;padding:0 24px;}
a{color:inherit;text-decoration:none;}
.noise{position:fixed;inset:0;pointer-events:none;z-index:9998;opacity:.035;mix-blend-mode:overlay;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");}
.btn{position:relative;display:inline-flex;align-items:center;justify-content:center;gap:10px;
  padding:18px 38px;border-radius:100px;font-weight:800;font-size:15px;text-transform:uppercase;letter-spacing:.05em;
  overflow:hidden;isolation:isolate;transition:transform .25s var(--ease-spring),box-shadow .3s;}
.btn-primary{background:linear-gradient(135deg,var(--pink),#ff5a8f 45%,var(--violet));background-size:200% 200%;
  color:#fff;box-shadow:0 12px 40px -8px rgba(255,23,63,.55);animation:gradient-shift 6s ease infinite;}
@keyframes gradient-shift{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
.btn svg{width:16px;height:16px;}

/* ===== hero (their CSS) ===== */
.hero{position:relative;min-height:100svh;display:flex;flex-direction:column;justify-content:center;overflow:hidden;padding-top:70px;}
.hero-video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:0;filter:brightness(0.5) saturate(1.15);}
.hero-video-overlay{position:absolute;inset:0;z-index:1;
  background:linear-gradient(180deg,rgba(8,7,10,0.55) 0%,rgba(8,7,10,0.05) 22%,rgba(8,7,10,0.05) 52%,rgba(8,7,10,0.82) 100%);}
.hero-content{position:relative;z-index:5;display:flex;flex-direction:column;align-items:center;text-align:center;}

/* NEW — eyebrow with price */
.eyebrow{display:inline-flex;align-items:center;gap:10px;padding:8px 16px;border-radius:100px;
  background:rgba(255,255,255,0.05);border:1px solid var(--line-strong);backdrop-filter:blur(10px);
  font-family:'Space Mono',monospace;font-size:12px;letter-spacing:.05em;color:var(--muted);margin-bottom:26px;}
.eyebrow strong{color:var(--cream);}
.eyebrow .live{width:8px;height:8px;border-radius:50%;background:var(--lime);box-shadow:0 0 12px var(--lime);animation:pulse-dot 1.6s infinite;}
@keyframes pulse-dot{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.4;transform:scale(.7)}}

.hero h1{font-family:'Anton',sans-serif;font-weight:400;text-transform:uppercase;
  font-size:clamp(44px,6.8vw,100px);line-height:1.02;letter-spacing:.005em;color:#fff;text-shadow:0 4px 24px rgba(0,0,0,.35);}
.hero h1 .accent{background:linear-gradient(100deg,var(--pink) 0%,var(--pink) 38%,#fff 50%,var(--pink) 62%,var(--pink) 100%);
  background-size:280% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;animation:accent-shine 6.5s linear infinite;}
@keyframes accent-shine{0%{background-position:140% 0}100%{background-position:-140% 0}}
.hero-sub{margin-top:22px;font-size:clamp(15px,2vw,20px);color:#fff;max-width:560px;font-weight:500;line-height:1.5;}
.hero-cta-row{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:16px;margin-top:34px;}

/* NEW — urgency line */
.hero-urgency{display:inline-flex;align-items:center;gap:14px;margin-top:18px;flex-wrap:wrap;justify-content:center;
  font-family:'Manrope',sans-serif;font-size:13px;font-weight:600;color:var(--cream);}
.hero-urgency .sp{display:inline-flex;align-items:center;gap:7px;color:var(--gold);}
.hero-urgency .sp .live{width:7px;height:7px;border-radius:50%;background:var(--lime);box-shadow:0 0 10px var(--lime);animation:pulse-dot 1.6s infinite;}
.hero-urgency .div{width:4px;height:4px;border-radius:50%;background:var(--muted-2);}
.hero-urgency .fc{color:var(--muted);}

.hero-rating-block{display:flex;align-items:center;justify-content:center;gap:9px;margin-top:26px;flex-wrap:wrap;}
.hero-rating-block .stars{color:var(--gold);font-size:15px;letter-spacing:2px;}
.hero-rating-block .num{font-family:'Anton',sans-serif;font-size:18px;color:var(--cream);}
.hero-rating-block svg{display:block;}
.hero-rating-block .dotsep{color:#fff;font-size:14px;margin:0 -2px;}
.hero-rating-caption{font-family:'Manrope',sans-serif;font-size:13.5px;font-weight:600;color:#fff;}

/* trust strip */
.trust{border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:30px 0;position:relative;z-index:3;background:rgba(20,16,25,0.4);}
.trust-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;text-align:center;}
.trust-item{display:flex;flex-direction:column;gap:4px;border-right:1px solid var(--line);}
.trust-item:last-child{border-right:none;}
.trust-item .num{font-family:'Anton',sans-serif;font-size:clamp(24px,3vw,34px);color:var(--cream);}
.trust-item .lbl{font-size:11.5px;text-transform:uppercase;letter-spacing:.08em;color:var(--muted-2);font-weight:700;}

@media(max-width:640px){
  .hero{padding-top:70px;padding-bottom:30px;}
  .hero h1{font-size:56px;line-height:1.03;}
  .hero-sub{margin-top:14px;font-size:13px;max-width:none;}
  .hero-cta-row{margin-top:24px;}
  .hero-urgency{font-size:12px;gap:10px;}
  .trust{padding:22px 0;}
  .trust-grid{grid-template-columns:repeat(2,1fr);gap:18px 10px;}
  .trust-item:nth-child(2){border-right:none;}
  .btn{padding:16px 30px;font-size:14px;}
}
@media(prefers-reduced-motion:reduce){*{animation-duration:.01ms!important;transition-duration:.01ms!important;}}
</style></head>
<body>
<div class="noise"></div>
<header class="hero">
  <video class="hero-video" muted loop autoplay playsinline poster="" src="__VIDEO__"></video>
  <div class="hero-video-overlay"></div>
  <div class="container hero-content">
    <div class="eyebrow"><span class="live"></span> Porto's #1 Pub Crawl · <strong>from &euro;17</strong></div>
    <h1>The <span class="accent">Craziest</span><br>Porto Pub Crawl</h1>
    <p class="hero-sub">From the producers of The Hangover and Project X</p>
    <div class="hero-cta-row">
      <a class="btn btn-primary">Reserve My Spot &mdash; &euro;17
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
    </div>
    <div class="hero-urgency">
      <span class="sp"><span class="live"></span> Only 7 spots left tonight</span>
      <span class="div"></span>
      <span class="fc">1-min checkout &middot; Free cancellation 24h</span>
    </div>
    <div class="hero-rating-block">
      <span class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span>
      <span class="num">4.9</span>
      <svg width="15" height="15" viewBox="0 0 18 18"><path fill="#4285F4" d="M17.64 9.2c0-.637-.057-1.251-.164-1.84H9v3.481h4.844c-.209 1.125-.843 2.078-1.796 2.717v2.258h2.908c1.702-1.567 2.684-3.874 2.684-6.615z"/><path fill="#34A853" d="M9 18c2.43 0 4.467-.806 5.956-2.18l-2.908-2.259c-.806.54-1.837.86-3.048.86-2.344 0-4.328-1.584-5.036-3.711H.957v2.332C2.438 15.983 5.482 18 9 18z"/><path fill="#FBBC05" d="M3.964 10.71c-.18-.54-.282-1.117-.282-1.71s.102-1.17.282-1.71V4.958H.957C.348 6.173 0 7.548 0 9s.348 2.827.957 4.042l3.007-2.332z"/><path fill="#EA4335" d="M9 3.58c1.321 0 2.508.454 3.44 1.345l2.582-2.58C13.463.891 11.426 0 9 0 5.482 0 2.438 2.017.957 4.958L3.964 7.29C4.672 5.163 6.656 3.58 9 3.58z"/></svg>
      <span class="dotsep">&middot;</span>
      <svg width="14" height="14" viewBox="0 0 24 24"><path fill="#00B67A" d="M12 1.5l3.09 6.26 6.91 1-5 4.87 1.18 6.87L12 17.25l-6.18 3.25L7 13.63l-5-4.87 6.91-1L12 1.5z"/></svg>
      <span class="hero-rating-caption">1,327+ Positive Hangover Reviews</span>
    </div>
  </div>
</header>
<section class="trust"><div class="container"><div class="trust-grid">
  <div class="trust-item"><span class="num">10K+</span><span class="lbl">Guests Hosted</span></div>
  <div class="trust-item"><span class="num">4.9&#9733;</span><span class="lbl">Average Rating</span></div>
  <div class="trust-item"><span class="num">60+</span><span class="lbl">Countries Repped</span></div>
  <div class="trust-item"><span class="num">2025</span><span class="lbl">Crawling Since</span></div>
</div></div></section>
</body></html>""".replace("__ANTON__",ANTON).replace("__MAN400__",MAN400).replace("__MAN700__",MAN700)\
    .replace("__MAN800__",MAN800).replace("__MONO400__",MONO400).replace("__MONO700__",MONO700)\
    .replace("__VIDEO__",video_uri)

def esc(s):  # for srcdoc attribute (double-quote delimited)
    return s.replace("&","&amp;").replace('"',"&quot;")

DOC_D = esc(hero_doc(VID_D))
DOC_M = esc(hero_doc(VID_M))

page = r"""<style>
:root{--void:#08070a;--pink:#ff173f;--cream:#f5f4f2;--muted:#a3a0a1;--line:rgba(245,244,242,.12);}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:#050406;color:var(--cream);font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;-webkit-font-smoothing:antialiased;padding:26px clamp(16px,4vw,48px) 70px;}
.head{max-width:1200px;margin:0 auto 26px;}
.head .k{font-family:ui-monospace,monospace;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);}
.head .k b{color:var(--pink);}
.head h1{font-size:clamp(20px,3vw,28px);font-weight:800;letter-spacing:-.02em;margin:8px 0 6px;}
.head p{color:var(--muted);font-size:14px;max-width:760px;line-height:1.6;}
.wrap{max-width:1200px;margin:0 auto;display:grid;grid-template-columns:1fr 400px;gap:30px;align-items:start;}
@media(max-width:1000px){.wrap{grid-template-columns:1fr;justify-items:center;}}
.col h2{font-family:ui-monospace,monospace;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin-bottom:12px;display:flex;align-items:center;gap:8px;}
.col h2::before{content:"";width:20px;height:1px;background:var(--pink);}
.desk-frame{width:100%;border-radius:14px;overflow:hidden;border:1px solid var(--line);box-shadow:0 30px 70px -30px rgba(0,0,0,.9);background:#000;}
.desk-frame .bar{height:34px;background:#141017;display:flex;align-items:center;gap:7px;padding:0 14px;border-bottom:1px solid var(--line);}
.desk-frame .bar i{width:11px;height:11px;border-radius:50%;background:#3a3540;}
.desk-frame iframe{width:100%;height:600px;border:0;display:block;}
/* phone */
.phone{width:390px;max-width:88vw;}
.phone .device{position:relative;border-radius:44px;padding:12px;background:#141017;border:1px solid var(--line);box-shadow:0 40px 90px -30px rgba(0,0,0,.95);}
.phone .device::before{content:"";position:absolute;top:16px;left:50%;transform:translateX(-50%);width:120px;height:26px;background:#000;border-radius:0 0 16px 16px;z-index:3;}
.phone .screen{position:relative;border-radius:34px;overflow:hidden;background:#000;}
.phone iframe{width:100%;height:780px;border:0;display:block;}
.note{max-width:1200px;margin:34px auto 0;font-size:12.5px;color:var(--muted);line-height:1.7;border-top:1px solid var(--line);padding-top:20px;}
.note b{color:var(--cream);}
</style>

<div class="head">
  <div class="k">PORTO <b>PUB CRAWL</b> · preview local (não publicado)</div>
  <h1>Hero “Evolução” — o vosso hero atual + vídeo real + preço/urgência</h1>
  <p>Mantém a estrutura, a tipografia e os selos do hero atual. Só muda: fundo em <b>vídeo real</b> (em vez da foto estática), um <b>eyebrow com “from €17”</b>, o preço no botão, e uma linha de <b>urgência</b> (spots left + free cancellation) acima da dobra.</p>
</div>

<div class="wrap">
  <div class="col" style="width:100%;">
    <h2>Desktop</h2>
    <div class="desk-frame">
      <div class="bar"><i></i><i></i><i></i></div>
      <iframe srcdoc="__DOC_D__" title="Desktop hero"></iframe>
    </div>
  </div>
  <div class="col phone">
    <h2>Mobile</h2>
    <div class="device"><div class="screen">
      <iframe srcdoc="__DOC_M__" title="Mobile hero"></iframe>
    </div></div>
  </div>
</div>

<p class="note"><b>Preview local — nada foi publicado nem alterado no site.</b> Os vídeos aqui vão comprimidos para o preview carregar; no site real ficam na qualidade alta que enviaste, servidos de <b>assets/</b> com poster. O mobile é renderizado num iframe a 390px, por isso vês as regras responsivas reais a atuar.</p>
"""

page = page.replace("__DOC_D__", DOC_D).replace("__DOC_M__", DOC_M)
out = base/"hero-evolution-preview.html"
out.write_text(page)
print("wrote", out, round(len(page)/1024), "KB")
