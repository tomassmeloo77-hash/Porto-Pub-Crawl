#!/usr/bin/env python3
import base64, pathlib
base = pathlib.Path("/home/user/Porto-Pub-Crawl/scratch-preview")
fdir = base/"fonts"/"node_modules"; adir = base.parent/"assets"
def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()
def font_uri(p): return "data:font/woff2;base64," + b64(p)
def img(p): return "data:image/webp;base64," + b64(adir/p)
ANTON=font_uri(fdir/"@fontsource/anton/files/anton-latin-400-normal.woff2")
MAN400=font_uri(fdir/"@fontsource/manrope/files/manrope-latin-400-normal.woff2")
MAN700=font_uri(fdir/"@fontsource/manrope/files/manrope-latin-700-normal.woff2")
MAN800=font_uri(fdir/"@fontsource/manrope/files/manrope-latin-800-normal.woff2")
MONO400=font_uri(fdir/"@fontsource/space-mono/files/space-mono-latin-400-normal.woff2")
VID="data:video/mp4;base64,"+b64(base/"evo-desktop.mp4")
POSTER="data:image/webp;base64,"+b64(base/"hero-poster.webp")
MEGA=img("photo-megaphone.webp");SHOTS=img("photo-shots-friends.webp");BOAT=img("photo-partyboat.webp")
CLUB=img("photo-clubfloor.webp");GROUP=img("photo-groupfriends.webp");KISS=img("photo-kiss.webp");VODKA=img("photo-vodka.webp")
AV={n:img("avatar-%s.webp"%n) for n in ["marco","haley","pauline","matheus"]}
PATH='M25 0Q48 14 62.0 40.0Q76 66 76 96V605Q76 634 62.5 659.0Q49 684 25 698H611Q694 698 761.0 676.5Q828 655 867.0 605.0Q906 555 906 471Q906 395 869.0 337.5Q832 280 766.5 247.5Q701 215 615 215H358V90Q358 63 371.5 38.5Q385 14 409 0ZM358 358H505Q549 358 574.0 373.0Q599 388 609.0 411.5Q619 435 619 459Q619 513 584.5 532.5Q550 552 500 552H358Z'
PM='<svg class="pmark" viewBox="0 0 1021 838"><g transform="translate(45,768) scale(1,-1)"><path d="'+PATH+'" fill="currentColor"/></g></svg>'
GOOGLE='<svg viewBox="0 0 18 18"><path fill="#4285F4" d="M17.64 9.2c0-.637-.057-1.251-.164-1.84H9v3.481h4.844c-.209 1.125-.843 2.078-1.796 2.717v2.258h2.908c1.702-1.567 2.684-3.874 2.684-6.615z"/><path fill="#34A853" d="M9 18c2.43 0 4.467-.806 5.956-2.18l-2.908-2.259c-.806.54-1.837.86-3.048.86-2.344 0-4.328-1.584-5.036-3.711H.957v2.332C2.438 15.983 5.482 18 9 18z"/><path fill="#FBBC05" d="M3.964 10.71c-.18-.54-.282-1.117-.282-1.71s.102-1.17.282-1.71V4.958H.957C.348 6.173 0 7.548 0 9s.348 2.827.957 4.042l3.007-2.332z"/><path fill="#EA4335" d="M9 3.58c1.321 0 2.508.454 3.44 1.345l2.582-2.58C13.463.891 11.426 0 9 0 5.482 0 2.438 2.017.957 4.958L3.964 7.29C4.672 5.163 6.656 3.58 9 3.58z"/></svg>'
TP='<svg viewBox="0 0 24 24"><path fill="#00B67A" d="M12 1.5l3.09 6.26 6.91 1-5 4.87 1.18 6.87L12 17.25l-6.18 3.25L7 13.63l-5-4.87 6.91-1L12 1.5z"/></svg>'
CRAWL_URL="https://book.stripe.com/cNi8wReAZ8di9m29LI4AU02";PACK_URL="https://book.stripe.com/4gM28takJ8di7dU8HE4AU03";WA="https://wa.me/351910694984"

ACTS=[("01","22:30","The Meet","Find the pink umbrellas","Praça de Carlos Alberto. A welcome shot is in your hand before you even catch anyone's name.",["Free welcome shots","Licensed local guides","Your crew for the night"],MEGA),
("02","23:00","The Bars","Four bars, zero waiting","Skip every line. Nine drinks across the night — beer, sangria, shots — with games and deals that get the whole room talking.",["9 free drinks","VIP skip-the-line","Wild games all night"],SHOTS),
("03","00:30","The Boat","Add the Douro cruise","Upgrade to the Party Boat pack: two hours on the river with a live DJ, then straight off the deck into the crawl.",["2-hour night cruise","Live DJ on deck","One ticket, two parties"],BOAT),
("04","01:00","The Club","VIP into the main room","Straight past the queue into Porto's late-night club. Lasers, the whole crew, and no plan except staying out.",["VIP club entry","No line, ever","One room, one crew"],CLUB),
("05","02:30","Sunrise","Home is optional","The night doesn't end — it just runs out of dark. Your photos and video land the next day as proof.",["Free photos & video","Friends from 60+ countries","Zero regrets (mostly)"],GROUP)]
REVIEWS=[("Best night of my life, thank you guys.","Haley","Australia","haley"),
("Guides showed us the real Porto nightlife — 10/10.","Pauline","United Kingdom","pauline"),
("Solo trip, made so many friends. Such a good time.","Matheus","Brazil","matheus"),
("The vibe was fun and friendly the whole night.","Marco","Germany","marco")]
FAQ=[("Where & when do we meet?","Every Saturday at 22:30 at Praça de Carlos Alberto — look for the pink umbrellas. Doors close 15 minutes after start."),
("What's included?","9 drinks, free welcome shots, VIP entry to 4 bars + 1 club, photos & video, drink deals and non-stop games."),
("Coming alone?","Most crawlers show up solo — the whole night is built around meeting people. You won't be alone for long."),
("Can I cancel?","Yes — full refund if you cancel at least 24 hours before start. No questions.")]

CSS=r"""<style>
@font-face{font-family:'Anton';src:url(__ANTON__) format('woff2');font-weight:400;font-display:swap;}
@font-face{font-family:'Manrope';src:url(__MAN400__) format('woff2');font-weight:400;font-display:swap;}
@font-face{font-family:'Manrope';src:url(__MAN700__) format('woff2');font-weight:700;font-display:swap;}
@font-face{font-family:'Manrope';src:url(__MAN800__) format('woff2');font-weight:800;font-display:swap;}
@font-face{font-family:'Space Mono';src:url(__MONO400__) format('woff2');font-weight:400;font-display:swap;}
:root{--void:#08070a;--void-2:#0e0c10;--pink:#ff173f;--pink-soft:#ff5468;--violet:#7a0a1f;--gold:#ffc466;--lime:#22ff7a;
  --cream:#f5f4f2;--muted:#a3a0a1;--muted-2:#7e7b7c;--line:rgba(245,244,242,.09);--line-strong:rgba(245,244,242,.16);
  --ease-spring:cubic-bezier(.34,1.56,.64,1);--disp:'Anton',Impact,sans-serif;--body:'Manrope',system-ui,sans-serif;--mono:'Space Mono',monospace;}
*{box-sizing:border-box;margin:0;padding:0;}html{scroll-behavior:smooth;}
body{background:var(--void);color:var(--cream);font-family:var(--body);-webkit-font-smoothing:antialiased;line-height:1.55;overflow-x:hidden;}
img,video{display:block;max-width:100%;}a{color:inherit;text-decoration:none;}
.wrap{width:100%;max-width:1280px;margin:0 auto;padding:0 clamp(20px,5vw,64px);}
h1,h2,h3{font-family:var(--disp);font-weight:400;text-transform:uppercase;letter-spacing:.005em;line-height:.88;}
.stars{color:var(--gold);letter-spacing:2px;}.pmark{display:inline-block;height:1em;width:auto;}
.live{width:8px;height:8px;border-radius:50%;background:var(--pink);box-shadow:0 0 12px var(--pink);animation:pd 1.6s infinite;flex:none;}
@keyframes pd{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.4;transform:scale(.7)}}
.btn{position:relative;display:inline-flex;align-items:center;justify-content:center;gap:10px;padding:16px 30px;border-radius:100px;
  font-family:var(--body);font-weight:800;font-size:14.5px;text-transform:uppercase;letter-spacing:.05em;cursor:pointer;overflow:hidden;
  transition:transform .25s var(--ease-spring),box-shadow .3s;white-space:nowrap;}
.btn:hover{transform:translateY(-2px);}.btn-block{width:100%;}
.btn-primary{background:linear-gradient(135deg,var(--pink),#ff5a8f 45%,var(--violet));background-size:200% 200%;color:#fff;box-shadow:0 12px 40px -8px rgba(255,23,63,.55);animation:gshift 6s ease infinite;}
@keyframes gshift{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
.btn-ghost{border:1.5px solid var(--line-strong);color:var(--cream);background:rgba(255,255,255,.04);backdrop-filter:blur(10px);}
.btn-ghost:hover{border-color:var(--pink);background:rgba(255,23,63,.1);}
.btn svg{width:16px;height:16px;}

/* strip + nav */
.strip{background:linear-gradient(90deg,var(--pink),var(--violet));color:#fff;font-weight:700;font-size:11px;letter-spacing:.05em;text-transform:uppercase;padding:8px 0;overflow:hidden;white-space:nowrap;position:relative;z-index:40;}
.strip .tr{display:inline-flex;gap:26px;animation:sx 26s linear infinite;padding-left:100%;}
@keyframes sx{from{transform:translateX(0)}to{transform:translateX(-100%)}}
.nav{position:sticky;top:0;z-index:50;backdrop-filter:blur(14px);background:rgba(8,7,10,.72);border-bottom:1px solid var(--line);}
.nav .in{display:flex;align-items:center;justify-content:space-between;height:62px;}
.logo{display:inline-flex;align-items:center;gap:9px;font-family:var(--disp);font-size:21px;color:#fff;}.logo .pmark{height:21px;color:var(--pink);}
.nav .links{display:flex;gap:24px;font-size:13px;color:var(--muted);}.nav .links a:hover{color:var(--cream);}
@media(max-width:820px){.nav .links{display:none;}}

/* HERO (P3 / M5) */
.hero{position:relative;min-height:calc(100svh - 62px);overflow:hidden;background:var(--void);}
.hbg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:0;filter:brightness(.5) saturate(1.15);}
.veil{position:absolute;inset:0;z-index:1;background:linear-gradient(90deg,rgba(8,7,10,.55),rgba(8,7,10,.12) 42%,rgba(8,7,10,.66));}
.hc{position:relative;z-index:5;min-height:calc(100svh - 62px);display:grid;grid-template-columns:1fr 400px;align-items:center;gap:44px;padding:clamp(40px,7vh,90px) clamp(20px,5vw,64px);max-width:1280px;margin:0 auto;}
.pbig{position:absolute;top:50%;transform:translateY(-50%);color:var(--pink);z-index:2;pointer-events:none;filter:drop-shadow(0 18px 46px rgba(255,23,63,.4));height:clamp(240px,32vw,440px);left:clamp(20px,3vw,58px);}
.pbig .pmark{height:100%;}
.hero .left{position:relative;z-index:5;padding-left:clamp(40px,9vw,170px);}
.hero h1{font-size:clamp(46px,6.2vw,100px);color:#fff;line-height:.84;text-shadow:0 6px 30px rgba(0,0,0,.55);}
.hero .sub{margin-top:22px;max-width:440px;font-size:clamp(15px,1.5vw,18px);color:#eceaeb;}
.card{background:linear-gradient(180deg,rgba(20,16,23,.93),rgba(8,7,10,.96));border:1px solid var(--line-strong);border-radius:20px;padding:26px;backdrop-filter:blur(16px);box-shadow:0 40px 100px -35px rgba(0,0,0,.95);justify-self:end;width:100%;display:flex;flex-direction:column;}
.chead{display:flex;align-items:center;justify-content:space-between;gap:12px;}
.badges{display:inline-flex;align-items:center;gap:16px;}.badges .bg{display:inline-flex;align-items:center;gap:6px;font-size:12.5px;font-weight:700;color:var(--cream);}.badges .bg svg{height:16px;width:auto;}
.crate{display:inline-flex;align-items:center;gap:7px;}.crate .stars{font-size:12px;}.crate .rnum{font-family:var(--disp);font-size:17px;color:var(--cream);}
.revline{font-size:11.5px;color:var(--muted-2);margin-top:8px;}.revline b{color:var(--muted);}
.hr{height:1px;background:var(--line);margin:16px 0 18px;}
.price{font-family:var(--disp);font-size:48px;color:#fff;line-height:.9;margin-bottom:18px;}
.price s{font-family:var(--body);font-weight:700;font-size:18px;color:var(--muted-2);margin-right:8px;}
.price small{display:block;font-family:var(--mono);font-size:10px;letter-spacing:.08em;color:var(--muted);text-transform:uppercase;margin-top:6px;}
.plist{list-style:none;display:flex;flex-direction:column;gap:11px;margin:0 0 18px;}
.plist li{display:flex;align-items:center;gap:10px;font-size:14px;color:#e2dfe0;}.plist svg{width:16px;height:16px;color:var(--lime);flex:none;}
.spots{display:inline-flex;align-items:center;gap:8px;font-size:12.5px;color:var(--gold);margin-bottom:16px;}
.rea{text-align:center;font-size:11px;color:var(--muted-2);margin-top:12px;}
@media(max-width:920px){.hc{grid-template-columns:1fr;justify-items:center;text-align:center;padding-top:92px;}
  .pbig{height:150px;left:50%;top:13%;transform:translate(-50%,-50%);}.hero .left{padding-left:0;}.hero h1{font-size:52px;}.hero .sub{margin-inline:auto;}.card{justify-self:stretch;max-width:440px;text-align:left;}}

/* ===== THE NIGHT — timeline ===== */
.night{position:relative;padding:clamp(70px,9vw,120px) 0 60px;}
.night-intro{text-align:center;max-width:720px;margin:0 auto clamp(30px,5vw,70px);}
.night-intro .k{font-family:var(--mono);font-size:12px;letter-spacing:.28em;text-transform:uppercase;color:var(--pink-soft);}
.night-intro h2{font-size:clamp(40px,6.5vw,96px);color:#fff;margin-top:14px;}
.night-intro p{margin-top:16px;color:var(--muted);font-size:clamp(15px,1.6vw,18px);}
.act{display:grid;grid-template-columns:1fr 1fr;gap:clamp(24px,4vw,64px);align-items:center;min-height:78vh;padding:40px 0;position:relative;}
.act:nth-child(even) .act-media{order:2;}
@media(max-width:900px){.act{grid-template-columns:1fr;min-height:0;gap:26px;}.act:nth-child(even) .act-media{order:0;}}
.act-media{position:relative;border-radius:20px;overflow:hidden;aspect-ratio:4/5;border:1px solid var(--line-strong);box-shadow:0 40px 90px -40px rgba(0,0,0,.9);}
.act-media img{width:100%;height:100%;object-fit:cover;}
.act-media::after{content:"";position:absolute;inset:0;background:linear-gradient(0deg,rgba(8,7,10,.55),transparent 55%);}
.act-media .tstamp{position:absolute;left:18px;bottom:16px;z-index:3;font-family:var(--disp);font-size:clamp(30px,4vw,52px);color:#fff;text-shadow:0 4px 20px rgba(0,0,0,.6);}
.act-body .num{font-family:var(--disp);font-size:clamp(60px,9vw,150px);line-height:.8;color:transparent;-webkit-text-stroke:1.5px rgba(255,23,63,.6);}
.act-body .kick{font-family:var(--mono);font-size:12px;letter-spacing:.22em;text-transform:uppercase;color:var(--pink-soft);margin:16px 0 10px;}
.act-body h3{font-size:clamp(32px,4.4vw,64px);color:#fff;}
.act-body p{margin-top:16px;color:var(--muted);font-size:clamp(15px,1.5vw,18px);max-width:440px;}
.act-body ul{list-style:none;display:flex;flex-wrap:wrap;gap:10px;margin-top:22px;}
.act-body li{font-size:12.5px;color:var(--cream);border:1px solid var(--line-strong);border-radius:100px;padding:8px 14px;display:inline-flex;align-items:center;gap:8px;}
.act-body li::before{content:"";width:6px;height:6px;border-radius:50%;background:var(--lime);}
/* connecting line */
.night .rail{position:absolute;left:50%;top:0;bottom:0;width:1px;background:linear-gradient(var(--line-strong),transparent);z-index:0;}
@media(max-width:900px){.night .rail{display:none;}}

/* ===== BENTO proof ===== */
.bento-wrap{padding:clamp(60px,8vw,110px) 0;}
.bento{display:grid;grid-template-columns:repeat(4,1fr);grid-auto-rows:minmax(120px,auto);gap:14px;}
@media(max-width:900px){.bento{grid-template-columns:repeat(2,1fr);}}
.b{background:var(--void-2);border:1px solid var(--line-strong);border-radius:18px;padding:24px;display:flex;flex-direction:column;justify-content:center;}
.b .big{font-family:var(--disp);font-size:clamp(34px,4vw,52px);color:#fff;line-height:.9;}
.b .lbl{font-size:12px;color:var(--muted-2);text-transform:uppercase;letter-spacing:.06em;margin-top:6px;}
.b.accent{background:linear-gradient(135deg,rgba(255,23,63,.9),rgba(122,10,31,.9));grid-column:span 2;grid-row:span 2;color:#fff;justify-content:space-between;}
.b.accent .rk{font-family:var(--disp);font-size:clamp(56px,8vw,96px);line-height:.85;}
.b.accent .rv{font-size:14px;opacity:.9;}
.b.accent .btn{align-self:flex-start;background:#fff;color:var(--void);}
.b.q{grid-column:span 2;}
.b.q p{font-size:16px;color:#e2dfe0;line-height:1.5;}
.b.q .who{display:flex;align-items:center;gap:10px;margin-top:14px;}.b.q .who img{width:34px;height:34px;border-radius:50%;object-fit:cover;}
.b.q .nm{font-weight:800;font-size:13px;}.b.q .lc{font-size:11px;color:var(--muted);}
.b .brand{display:inline-flex;align-items:center;gap:8px;font-weight:700;font-size:13px;color:var(--cream);}
.b .brand svg{height:18px;}

/* ===== ticket pick ===== */
.pick{padding:clamp(60px,8vw,110px) 0;}
.pick .head{text-align:center;max-width:640px;margin:0 auto 44px;}
.pick .head .k{font-family:var(--mono);font-size:12px;letter-spacing:.24em;text-transform:uppercase;color:var(--pink-soft);}
.pick .head h2{font-size:clamp(34px,5vw,64px);color:#fff;margin-top:12px;}
.tix{display:grid;grid-template-columns:1fr 1fr;gap:20px;max-width:900px;margin:0 auto;}
@media(max-width:760px){.tix{grid-template-columns:1fr;}}
.tix .t{background:var(--void-2);border:1px solid var(--line-strong);border-radius:20px;padding:30px;display:flex;flex-direction:column;}
.tix .t.feat{border-color:var(--pink);box-shadow:0 0 0 1px var(--pink),0 30px 80px -40px rgba(255,23,63,.6);}
.tix .tag2{font-family:var(--mono);font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:var(--pink);margin-bottom:10px;}
.tix h3{font-size:26px;color:#fff;}
.tix .pr{font-family:var(--disp);font-size:46px;color:#fff;margin:14px 0 4px;}.tix .pr s{font-family:var(--body);font-weight:700;font-size:18px;color:var(--muted-2);margin-right:8px;}
.tix .pp{font-family:var(--mono);font-size:10px;letter-spacing:.08em;color:var(--muted);text-transform:uppercase;margin-bottom:18px;}
.tix ul{list-style:none;display:flex;flex-direction:column;gap:9px;margin-bottom:22px;flex:1;}
.tix li{font-size:13.5px;color:#e2dfe0;display:flex;gap:9px;}.tix li svg{width:15px;height:15px;color:var(--lime);flex:none;margin-top:3px;}

/* ===== faq strip ===== */
.faq2{padding:clamp(60px,8vw,110px) 0;}
.faq2 .grid{display:grid;grid-template-columns:.8fr 1.2fr;gap:clamp(24px,4vw,60px);align-items:start;}
@media(max-width:820px){.faq2 .grid{grid-template-columns:1fr;}}
.faq2 h2{font-size:clamp(32px,4.5vw,58px);color:#fff;}
.faq2 .sub{margin-top:16px;color:var(--muted);font-size:15px;}
.faq2 .sub a{color:var(--pink);}
.fi{border-bottom:1px solid var(--line);}
.fq{width:100%;display:flex;justify-content:space-between;gap:16px;padding:22px 2px;background:none;border:0;color:var(--cream);font-family:var(--body);font-weight:700;font-size:17px;text-align:left;cursor:pointer;}
.fq .pl{position:relative;width:20px;height:20px;border:1px solid var(--line-strong);border-radius:50%;flex:none;}
.fq .pl::before,.fq .pl::after{content:'';position:absolute;left:50%;top:50%;background:var(--cream);transition:transform .35s var(--ease-spring);}
.fq .pl::before{width:10px;height:1.5px;transform:translate(-50%,-50%);}.fq .pl::after{width:1.5px;height:10px;transform:translate(-50%,-50%);}
.fi.open .pl{background:var(--pink);border-color:var(--pink);}.fi.open .pl::before,.fi.open .pl::after{background:#fff;}.fi.open .pl::after{transform:translate(-50%,-50%) rotate(90deg);opacity:0;}
.fa{max-height:0;overflow:hidden;transition:max-height .5s var(--ease-spring);}.fa p{padding:0 2px 24px;color:var(--muted);font-size:14.5px;line-height:1.7;}
.fi.open .fa{max-height:200px;}

/* ===== sticky booking bar ===== */
.dock{position:fixed;left:50%;bottom:16px;transform:translateX(-50%) translateY(140%);z-index:60;width:min(720px,calc(100vw - 24px));
  background:rgba(14,12,16,.92);border:1px solid var(--line-strong);border-radius:100px;backdrop-filter:blur(16px);box-shadow:0 30px 70px -30px rgba(0,0,0,.9);
  display:flex;align-items:center;gap:16px;padding:10px 10px 10px 24px;transition:transform .4s var(--ease-spring);}
.dock.show{transform:translateX(-50%) translateY(0);}
.dock .d-price{font-family:var(--disp);font-size:26px;color:#fff;}.dock .d-price s{font-family:var(--body);font-weight:700;font-size:14px;color:var(--muted-2);margin-right:6px;}
.dock .d-meta{font-size:12px;color:var(--gold);display:inline-flex;align-items:center;gap:7px;}
.dock .d-sep{flex:1;}
.dock .btn{padding:14px 26px;}
@media(max-width:600px){.dock{padding:8px 8px 8px 18px;gap:10px;}.dock .d-meta{display:none;}.dock .d-price{font-size:22px;}.dock .btn{padding:12px 18px;font-size:12.5px;}}

/* footer */
footer{border-top:1px solid var(--line);padding:56px 0 40px;}
.ftop{display:grid;grid-template-columns:1.4fr 2fr;gap:40px;}@media(max-width:820px){.ftop{grid-template-columns:1fr;}}
.flogo{display:inline-flex;align-items:center;gap:9px;font-family:var(--disp);font-size:24px;color:#fff;}.flogo .pmark{height:24px;color:var(--pink);}
.fdesc{max-width:280px;color:var(--muted);font-size:14px;margin-top:14px;line-height:1.6;}
.flinks{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;}@media(max-width:560px){.flinks{grid-template-columns:repeat(2,1fr);}}
.fcol h4{font-size:13px;text-transform:uppercase;letter-spacing:.06em;color:var(--cream);margin-bottom:14px;font-weight:800;}
.fcol a{display:block;color:var(--muted);font-size:13.5px;margin-bottom:10px;}.fcol a:hover{color:var(--cream);}
.fbot{border-top:1px solid var(--line);margin-top:40px;padding-top:24px;color:var(--muted-2);font-size:12.5px;}
.pvnote{position:fixed;top:52px;left:14px;z-index:70;font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted-2);background:rgba(8,7,10,.8);border:1px solid var(--line);border-radius:100px;padding:6px 13px;backdrop-filter:blur(8px);}
.pvnote b{color:var(--pink);}
@media(prefers-reduced-motion:reduce){*{animation:none!important;}}
</style>"""

def chk(): return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>'
def acts_html():
    out=""
    for num,time,kick,title,copy,tags,photo in ACTS:
        chips="".join("<li>%s</li>"%t for t in tags)
        out+='''<div class="act">
          <div class="act-media"><img src="%s" alt="%s"><div class="tstamp">%s</div></div>
          <div class="act-body"><div class="num">%s</div><div class="kick">%s</div><h3>%s</h3><p>%s</p><ul>%s</ul></div>
        </div>'''%(photo,title,time,num,kick,title,copy,chips)
    return out
def rev_q(i):
    txt,name,loc,av=REVIEWS[i]
    return '<p>“%s”</p><div class="who"><img src="%s" alt=""><div><div class="nm">%s</div><div class="lc">%s</div></div></div>'%(txt,AV[av],name,loc)
def faq_html():
    out=""
    for i,(q,a) in enumerate(FAQ):
        op=" open" if i==0 else ""
        out+='<div class="fi%s"><button class="fq">%s<span class="pl"></span></button><div class="fa"><p>%s</p></div></div>'%(op,q,a)
    return out

BODY=r"""
<div class="strip"><div class="tr"><span>PORTO · EVERY SATURDAY · 22:30</span><span>·</span><span>RATED 4.9 BY 1,327+ CRAWLERS</span><span>·</span><span>FREE CANCELLATION 24H</span><span>·</span><span>PORTO · EVERY SATURDAY · 22:30</span><span>·</span><span>RATED 4.9 BY 1,327+ CRAWLERS</span><span>·</span></div></div>
<nav class="nav"><div class="wrap in">
  <a href="#top" class="logo">__PM__ Project&nbsp;P</a>
  <div class="links"><a href="#night">The Night</a><a href="#proof">Proof</a><a href="#tickets">Tickets</a><a href="#faq">FAQ</a></div>
  <a href="__CRAWL_URL__" target="_blank" rel="noopener" class="btn btn-primary" style="padding:11px 20px;font-size:12.5px;">Book Now →</a>
</div></nav>

<header class="hero" id="top">
  <video class="hbg" muted loop autoplay playsinline poster="__POSTER__" src="__VID__"></video>
  <div class="veil"></div>
  <div class="hc">
    <div class="pbig">__PM__</div>
    <div class="left"><h1>The Craziest<br>Night in Porto</h1>
      <p class="sub">The guided pub crawl locals warn you about — bars, boat, club, sunrise.</p></div>
    <aside class="card">
      <div class="chead"><div class="badges"><span class="bg">__GOOGLE__ <span>Google</span></span><span class="bg">__TP__ <span>Trustpilot</span></span></div><div class="crate"><span class="stars">★★★★★</span><span class="rnum">4.9</span></div></div>
      <div class="revline">Rated <b>excellent</b> by <b>1,327+</b> crawlers</div>
      <div class="hr"></div>
      <div class="price"><span><s>€20</s>€17</span><small>per person</small></div>
      <ul class="plist"><li>__CHK__ 9 free drinks — beer, sangria &amp; shots</li><li>__CHK__ VIP entry · 4 bars + 1 nightclub</li><li>__CHK__ Free photos &amp; video next day</li></ul>
      <div class="spots"><span class="live"></span> Only 7 spots left tonight</div>
      <a href="__CRAWL_URL__" target="_blank" rel="noopener" class="btn btn-primary btn-block">Reserve My Spot — €17</a>
      <p class="rea">1-min checkout · Free cancellation up to 24h</p>
    </aside>
  </div>
</header>

<section class="night" id="night"><div class="rail"></div><div class="wrap">
  <div class="night-intro"><div class="k">One night · Five acts</div><h2>Follow the night,<br>hour by hour</h2>
    <p>This isn't a list of features — it's the actual run of a Saturday with us. From the first shot to sunrise, here's exactly how it goes.</p></div>
  __ACTS__
</div></section>

<section class="bento-wrap" id="proof"><div class="wrap">
  <div class="bento">
    <div class="b accent">
      <div><div class="rk">4.9</div><div class="rv"><span class="stars">★★★★★</span><br>from 1,327+ crawlers worldwide</div></div>
      <a href="__CRAWL_URL__" target="_blank" rel="noopener" class="btn">Join them — €17</a>
    </div>
    <div class="b"><div class="big">10K+</div><div class="lbl">Guests hosted</div></div>
    <div class="b"><div class="big">60+</div><div class="lbl">Countries repped</div></div>
    <div class="b q">__REV0__</div>
    <div class="b"><div class="brand">__TP__ Trustpilot</div><div class="big" style="font-size:28px;margin-top:8px;">857</div><div class="lbl">reviews</div></div>
    <div class="b"><div class="brand">__GOOGLE__ Google</div><div class="big" style="font-size:28px;margin-top:8px;">470</div><div class="lbl">reviews</div></div>
    <div class="b q">__REV1__</div>
    <div class="b"><div class="big" style="font-size:24px;">Verified</div><div class="lbl">Licensed operator · Porto CM</div></div>
    <div class="b"><div class="big" style="font-size:22px;">Since 2025</div><div class="lbl">Every Saturday</div></div>
  </div>
</div></section>

<section class="pick" id="tickets"><div class="wrap">
  <div class="head"><div class="k">Pick your night</div><h2>Two tickets,<br>one legendary night</h2></div>
  <div class="tix">
    <div class="t feat">
      <div class="tag2">★ Most booked</div>
      <h3>Porto Pub Crawl</h3>
      <div class="pr"><s>€20</s>€17</div><div class="pp">per person · worth €45+</div>
      <ul><li>__CHK__ 9 free drinks — beer, sangria &amp; shots</li><li>__CHK__ VIP skip-the-line · 4 bars + 1 club</li><li>__CHK__ Wild games &amp; drink deals all night</li><li>__CHK__ Free photos &amp; video next day</li></ul>
      <a href="__CRAWL_URL__" target="_blank" rel="noopener" class="btn btn-primary btn-block">Reserve My Spot — €17</a>
    </div>
    <div class="t">
      <div class="tag2">Two parties, one night</div>
      <h3>Party Boat + Crawl</h3>
      <div class="pr"><s>€55</s>€44</div><div class="pp">per person</div>
      <ul><li>__CHK__ 2-hour Douro night cruise + live DJ</li><li>__CHK__ Drinks &amp; dancing on deck</li><li>__CHK__ Straight into the full pub crawl</li><li>__CHK__ Free shots on boat &amp; crawl</li></ul>
      <a href="__PACK_URL__" target="_blank" rel="noopener" class="btn btn-ghost btn-block">Book The Pack — €44</a>
    </div>
  </div>
</div></section>

<section class="faq2" id="faq"><div class="wrap"><div class="grid">
  <div><h2>Good to<br>know</h2><p class="sub">Anything else? <a href="__WA__" target="_blank" rel="noopener">Message us on WhatsApp</a> — we reply fast.<br><br>Meet: Praça de Carlos Alberto, 22:30 every Saturday.</p></div>
  <div>__FAQ__</div>
</div></div></section>

<footer><div class="wrap">
  <div class="ftop">
    <div><a href="#top" class="flogo">__PM__ Project&nbsp;P</a>
      <p class="fdesc">Porto's most talked-about night out, running every Saturday since 2025.</p></div>
    <div class="flinks">
      <div class="fcol"><h4>The Night</h4><a href="#night">Run of night</a><a href="#proof">Proof</a><a href="#tickets">Tickets</a></div>
      <div class="fcol"><h4>Support</h4><a href="#faq">FAQ</a><a href="__WA__" target="_blank" rel="noopener">WhatsApp</a><a href="mailto:contact@porto-pubcrawl.com">Email</a></div>
      <div class="fcol"><h4>Work with us</h4><a href="#">Become a Partner</a><a href="#">Become a Guide</a></div>
      <div class="fcol"><h4>Book</h4><a href="__CRAWL_URL__" target="_blank" rel="noopener">Pub Crawl — €17</a><a href="__PACK_URL__" target="_blank" rel="noopener">Boat + Crawl — €44</a></div>
    </div>
  </div>
  <div class="fbot">© 2026 Project P — All rights reserved. · Concept preview (A/B test candidate)</div>
</div></footer>

<div class="dock" id="dock">
  <div class="d-price"><s>€20</s>€17</div>
  <div class="d-meta"><span class="live"></span> 7 spots left · this Saturday</div>
  <div class="d-sep"></div>
  <a href="__CRAWL_URL__" target="_blank" rel="noopener" class="btn btn-primary">Reserve My Spot →</a>
</div>
<div class="pvnote">Preview · <b>Landing B — conceito novo</b> · site atual intacto</div>

<script>
  document.querySelectorAll('.fq').forEach(function(q){q.addEventListener('click',function(){
    var it=q.parentElement,open=it.classList.contains('open');
    document.querySelectorAll('.fi').forEach(function(i){i.classList.remove('open');});
    if(!open)it.classList.add('open');});});
  var v=document.querySelector('.hero video');if(v){v.muted=true;var p=v.play();if(p&&p.catch)p.catch(function(){});}
  var dock=document.getElementById('dock'),hero=document.querySelector('.hero');
  var io=new IntersectionObserver(function(es){es.forEach(function(e){dock.classList.toggle('show',!e.isIntersecting);});},{threshold:0.15});
  io.observe(hero);
</script>
"""
page=CSS+BODY
repl={"__ANTON__":ANTON,"__MAN400__":MAN400,"__MAN700__":MAN700,"__MAN800__":MAN800,"__MONO400__":MONO400,
  "__VID__":VID,"__POSTER__":POSTER,"__PM__":PM,"__GOOGLE__":GOOGLE,"__TP__":TP,"__CHK__":chk(),
  "__CRAWL_URL__":CRAWL_URL,"__PACK_URL__":PACK_URL,"__WA__":WA,
  "__ACTS__":acts_html(),"__REV0__":rev_q(0),"__REV1__":rev_q(1),"__FAQ__":faq_html()}
for k,val in repl.items(): page=page.replace(k,val)
out=base/"landing-b-preview.html";out.write_text(page)
print("wrote",out,round(len(page)/1024),"KB")
