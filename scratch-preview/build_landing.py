#!/usr/bin/env python3
import base64, pathlib
base = pathlib.Path("/home/user/Porto-Pub-Crawl/scratch-preview")
fdir = base/"fonts"/"node_modules"
adir = base.parent/"assets"
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
CRAWL=img("photo-crawl-club.webp"); BOAT=img("photo-partyboat.webp")
G1=img("photo-shots-friends.webp");G2=img("photo-groupfriends.webp");G3=img("photo-clubfloor.webp")
G4=img("photo-megaphone.webp");G5=img("photo-vodka.webp");G6=img("photo-kiss.webp")
AV={n:img("avatar-%s.webp"%n) for n in ["marco","xavimeneres","haley","pauline","angelique","matheus","aleksandra"]}
PATH='M25 0Q48 14 62.0 40.0Q76 66 76 96V605Q76 634 62.5 659.0Q49 684 25 698H611Q694 698 761.0 676.5Q828 655 867.0 605.0Q906 555 906 471Q906 395 869.0 337.5Q832 280 766.5 247.5Q701 215 615 215H358V90Q358 63 371.5 38.5Q385 14 409 0ZM358 358H505Q549 358 574.0 373.0Q599 388 609.0 411.5Q619 435 619 459Q619 513 584.5 532.5Q550 552 500 552H358Z'
PM='<svg class="pmark" viewBox="0 0 1021 838"><g transform="translate(45,768) scale(1,-1)"><path d="'+PATH+'" fill="currentColor"/></g></svg>'
GOOGLE='<svg viewBox="0 0 18 18"><path fill="#4285F4" d="M17.64 9.2c0-.637-.057-1.251-.164-1.84H9v3.481h4.844c-.209 1.125-.843 2.078-1.796 2.717v2.258h2.908c1.702-1.567 2.684-3.874 2.684-6.615z"/><path fill="#34A853" d="M9 18c2.43 0 4.467-.806 5.956-2.18l-2.908-2.259c-.806.54-1.837.86-3.048.86-2.344 0-4.328-1.584-5.036-3.711H.957v2.332C2.438 15.983 5.482 18 9 18z"/><path fill="#FBBC05" d="M3.964 10.71c-.18-.54-.282-1.117-.282-1.71s.102-1.17.282-1.71V4.958H.957C.348 6.173 0 7.548 0 9s.348 2.827.957 4.042l3.007-2.332z"/><path fill="#EA4335" d="M9 3.58c1.321 0 2.508.454 3.44 1.345l2.582-2.58C13.463.891 11.426 0 9 0 5.482 0 2.438 2.017.957 4.958L3.964 7.29C4.672 5.163 6.656 3.58 9 3.58z"/></svg>'
TP='<svg viewBox="0 0 24 24"><path fill="#00B67A" d="M12 1.5l3.09 6.26 6.91 1-5 4.87 1.18 6.87L12 17.25l-6.18 3.25L7 13.63l-5-4.87 6.91-1L12 1.5z"/></svg>'
CRAWL_URL="https://book.stripe.com/cNi8wReAZ8di9m29LI4AU02"
PACK_URL="https://book.stripe.com/4gM28takJ8di7dU8HE4AU03"
WA="https://wa.me/351910694984"
def chk(): return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>'

REVIEWS=[("Marco","Germany","marco","Absolutely perfect night out, great choice of bars and clubs, the vibe was fun and friendly, guides made sure everyone had a great time."),
("Xavi","Portugal","xavimeneres","I've done this pub crawl twice and it's always amazing! Great vibe, awesome people, and so much fun every time."),
("Haley","Australia","haley","This pub crawl is maaddddd — best night of my life, thank you guys &lt;3"),
("Pauline","United Kingdom","pauline","10/10 great night's craic, great company, guides showed us the nightlife of Porto which is also 10/10."),
("Angelique","France","angelique","I didn't know where to go out in Porto so I joined the pub crawl — best decision ever! Can't wait to do it again. ❤️"),
("Matheus","Brazil","matheus","Did this during my solo trip to Porto and it was great!! Made so many friends and such a good time."),
("Aleksandra","Poland","aleksandra","Very nice way to get to know the Porto nightlife — got the money's worth in alcohol and memories. Super fun.")]
FAQ=[("Where and when do we meet?","Every Saturday at 22:30, at Praça de Carlos Alberto — look for our guides holding pink umbrellas near the statue. Doors close 15 minutes after start, so don't be fashionably late."),
("Do you run every night, or just Saturdays?","Just Saturdays — one night a week, done properly, rather than a rushed version every night. That's also why spots are genuinely limited."),
("What's actually included?","9 drinks total across the night, free welcome shots, beer and sangria, VIP entry to 4 bars plus one late-night club, photos and video, drink deals, and non-stop wild games."),
("Is there a Party Boat option?","Yes — the Party Boat + Pub Crawl pack (€44) is both in one night: the boat first from Cais de Gaia (boards 22:00, sails until 00:00), then straight into the full pub crawl at Praça de Carlos Alberto from 00:30."),
("How long does the night run?","Around 4 hours, wrapping around 02:30 — though most crews keep the party going long after we officially call it."),
("I'm coming alone — is that weird?","Not even a little. Most of our crawlers show up solo. The whole night is built around meeting people, so you'll never be standing alone for long."),
("Can I cancel if plans change?","Yes — full refund if you cancel at least 24 hours before your start time. No questions, no hassle.")]

def review_cards():
    out=""
    for name,loc,av,txt in REVIEWS*2:
        out+='<div class="tcard"><span class="stars">★★★★★</span><p>%s</p><div class="who"><img src="%s" alt=""><div><div class="nm">%s</div><div class="lc">%s</div></div></div></div>'%(txt,AV[av],name,loc)
    return out
def faq_items():
    out=""
    for i,(q,a) in enumerate(FAQ):
        op=" open" if i==0 else ""
        out+='<div class="faq-item%s"><button class="faq-q">%s<span class="plus"></span></button><div class="faq-a"><p>%s</p></div></div>'%(op,q,a)
    return out
def gallery():
    imgs=[G2,G1,G3,CRAWL,G4,BOAT,G5,G6]
    return "".join('<div class="g-cell"><img src="%s" alt="Porto pub crawl" loading="lazy"></div>'%s for s in imgs)

CSS = r"""<style>
@font-face{font-family:'Anton';src:url(__ANTON__) format('woff2');font-weight:400;font-display:swap;}
@font-face{font-family:'Manrope';src:url(__MAN400__) format('woff2');font-weight:400;font-display:swap;}
@font-face{font-family:'Manrope';src:url(__MAN700__) format('woff2');font-weight:700;font-display:swap;}
@font-face{font-family:'Manrope';src:url(__MAN800__) format('woff2');font-weight:800;font-display:swap;}
@font-face{font-family:'Space Mono';src:url(__MONO400__) format('woff2');font-weight:400;font-display:swap;}
:root{--void:#08070a;--void-2:#0e0c10;--pink:#ff173f;--pink-soft:#ff5468;--violet:#7a0a1f;--violet-deep:#3c0512;
  --gold:#ffc466;--lime:#22ff7a;--cream:#f5f4f2;--muted:#a3a0a1;--muted-2:#7e7b7c;
  --line:rgba(245,244,242,.09);--line-strong:rgba(245,244,242,.16);--ease-spring:cubic-bezier(.34,1.56,.64,1);
  --disp:'Anton',Impact,sans-serif;--body:'Manrope',system-ui,sans-serif;--mono:'Space Mono',monospace;}
*{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;}
body{background:var(--void);color:var(--cream);font-family:var(--body);-webkit-font-smoothing:antialiased;line-height:1.55;overflow-x:hidden;}
img,video{display:block;max-width:100%;}a{color:inherit;text-decoration:none;}
.container{width:100%;max-width:1240px;margin:0 auto;padding:0 clamp(20px,5vw,64px);}
h1,h2,h3{font-family:var(--disp);font-weight:400;text-transform:uppercase;letter-spacing:.005em;line-height:.9;}
.stars{color:var(--gold);letter-spacing:2px;}
.pmark{display:inline-block;height:1em;width:auto;}
.live{width:8px;height:8px;border-radius:50%;background:var(--pink);box-shadow:0 0 12px var(--pink);animation:pd 1.6s infinite;flex:none;}
@keyframes pd{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.4;transform:scale(.7)}}
.btn{position:relative;display:inline-flex;align-items:center;justify-content:center;gap:10px;padding:16px 30px;border-radius:100px;
  font-family:var(--body);font-weight:800;font-size:14.5px;text-transform:uppercase;letter-spacing:.05em;cursor:pointer;overflow:hidden;
  transition:transform .25s var(--ease-spring),box-shadow .3s;white-space:nowrap;}
.btn:hover{transform:translateY(-2px);}.btn-block{width:100%;}
.btn-primary{background:linear-gradient(135deg,var(--pink),#ff5a8f 45%,var(--violet));background-size:200% 200%;color:#fff;
  box-shadow:0 12px 40px -8px rgba(255,23,63,.55);animation:gshift 6s ease infinite;}
@keyframes gshift{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
.btn-ghost{border:1.5px solid var(--line-strong);color:var(--cream);background:rgba(255,255,255,.04);backdrop-filter:blur(10px);}
.btn-ghost:hover{border-color:var(--pink);background:rgba(255,23,63,.1);}
.btn svg{width:16px;height:16px;}
section{position:relative;padding:clamp(70px,10vw,120px) 0;}
.shead{max-width:680px;margin-bottom:clamp(36px,5vw,60px);}
.shead.center{margin:0 auto clamp(36px,5vw,60px);text-align:center;}
.tag{font-family:var(--mono);font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--pink);display:inline-flex;align-items:center;gap:10px;margin-bottom:16px;}
.shead h2{font-size:clamp(34px,5vw,64px);color:#fff;}
.shead p{margin-top:16px;color:var(--muted);font-size:clamp(15px,1.6vw,18px);}

/* strip */
.strip{background:linear-gradient(90deg,var(--pink),var(--violet));color:#fff;font-weight:700;font-size:11px;letter-spacing:.04em;
  text-transform:uppercase;padding:8px 0;overflow:hidden;white-space:nowrap;position:relative;z-index:40;}
.strip .tr{display:inline-flex;gap:26px;animation:sx 26s linear infinite;padding-left:100%;}
@keyframes sx{from{transform:translateX(0)}to{transform:translateX(-100%)}}
/* nav */
.nav{position:sticky;top:0;z-index:50;backdrop-filter:blur(14px);background:rgba(8,7,10,.72);border-bottom:1px solid var(--line);}
.nav .in{display:flex;align-items:center;justify-content:space-between;height:64px;}
.logo{display:inline-flex;align-items:center;gap:9px;font-family:var(--disp);font-size:22px;color:#fff;letter-spacing:.02em;}
.logo .pmark{height:22px;color:var(--pink);}
.nav .links{display:flex;gap:26px;font-size:13.5px;color:var(--muted);}
.nav .links a:hover{color:var(--cream);}
@media(max-width:820px){.nav .links{display:none;}}

/* ===== HERO (P3 desktop / M5 mobile) ===== */
.hero{position:relative;min-height:calc(100svh - 64px);overflow:hidden;background:var(--void);}
.hbg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:0;filter:brightness(.5) saturate(1.15);}
.veil{position:absolute;inset:0;z-index:1;background:linear-gradient(90deg,rgba(8,7,10,.55),rgba(8,7,10,.12) 42%,rgba(8,7,10,.66));}
.hero .hc{position:relative;z-index:5;min-height:calc(100svh - 64px);display:grid;grid-template-columns:1fr 400px;align-items:center;gap:44px;
  padding:clamp(40px,7vh,90px) clamp(20px,5vw,64px);max-width:1240px;margin:0 auto;}
.pbig{position:absolute;top:50%;transform:translateY(-50%);color:var(--pink);z-index:2;pointer-events:none;
  filter:drop-shadow(0 18px 46px rgba(255,23,63,.4));height:clamp(240px,32vw,440px);left:clamp(20px,3vw,58px);}
.pbig .pmark{height:100%;}
.hero .left{position:relative;z-index:5;padding-left:clamp(40px,9vw,170px);}
.hero h1{font-size:clamp(46px,6.2vw,100px);color:#fff;line-height:.84;text-shadow:0 6px 30px rgba(0,0,0,.55);}
.hero .sub{margin-top:22px;max-width:440px;font-size:clamp(15px,1.5vw,18px);color:#eceaeb;}
/* booking card */
.card{background:linear-gradient(180deg,rgba(20,16,23,.93),rgba(8,7,10,.96));border:1px solid var(--line-strong);border-radius:20px;
  padding:26px;backdrop-filter:blur(16px);box-shadow:0 40px 100px -35px rgba(0,0,0,.95);justify-self:end;width:100%;display:flex;flex-direction:column;}
.chead{display:flex;align-items:center;justify-content:space-between;gap:12px;}
.badges{display:inline-flex;align-items:center;gap:16px;}
.badges .bg{display:inline-flex;align-items:center;gap:6px;font-size:12.5px;font-weight:700;color:var(--cream);}
.badges .bg svg{height:16px;width:auto;display:block;}
.crate{display:inline-flex;align-items:center;gap:7px;}.crate .stars{font-size:12px;}.crate .rnum{font-family:var(--disp);font-size:17px;color:var(--cream);}
.revline{font-size:11.5px;color:var(--muted-2);margin-top:8px;}.revline b{color:var(--muted);}
.hr{height:1px;background:var(--line);margin:16px 0 18px;}
.price{font-family:var(--disp);font-size:48px;color:#fff;line-height:.9;margin-bottom:18px;}
.price s{font-family:var(--body);font-weight:700;font-size:18px;color:var(--muted-2);margin-right:8px;}
.price small{display:block;font-family:var(--mono);font-size:10px;letter-spacing:.08em;color:var(--muted);text-transform:uppercase;margin-top:6px;}
.plist{list-style:none;display:flex;flex-direction:column;gap:11px;margin:0 0 18px;}
.plist li{display:flex;align-items:center;gap:10px;font-size:14px;color:#e2dfe0;}
.plist svg{width:16px;height:16px;color:var(--lime);flex:none;}
.spots{display:inline-flex;align-items:center;gap:8px;font-size:12.5px;color:var(--gold);margin-bottom:16px;}
.rea{text-align:center;font-size:11px;color:var(--muted-2);margin-top:12px;}
@media(max-width:920px){
  .hero .hc{grid-template-columns:1fr;justify-items:center;text-align:center;padding-top:96px;}
  .pbig{height:150px;left:50%;top:14%;transform:translate(-50%,-50%);}
  .hero .left{padding-left:0;}
  .hero h1{font-size:52px;}.hero .sub{margin-left:auto;margin-right:auto;}
  .card{justify-self:stretch;max-width:440px;text-align:left;}
}

/* trust stats */
.stats{border-top:1px solid var(--line);border-bottom:1px solid var(--line);background:rgba(20,16,25,.4);}
.stats .g{display:grid;grid-template-columns:repeat(4,1fr);}
.stats .it{padding:30px 16px;text-align:center;border-right:1px solid var(--line);}
.stats .it:last-child{border-right:none;}
.stats .n{font-family:var(--disp);font-size:clamp(26px,3.4vw,38px);color:var(--cream);}
.stats .l{font-size:11.5px;text-transform:uppercase;letter-spacing:.08em;color:var(--muted-2);font-weight:700;margin-top:4px;}
@media(max-width:640px){.stats .g{grid-template-columns:repeat(2,1fr);}.stats .it:nth-child(2){border-right:none;}.stats .it:nth-child(1),.stats .it:nth-child(2){border-bottom:1px solid var(--line);}}

/* experiences */
.avail{display:flex;align-items:center;justify-content:center;gap:14px;flex-wrap:wrap;margin-bottom:40px;font-size:13.5px;color:var(--cream);
  background:rgba(255,23,63,.08);border:1px solid rgba(255,23,63,.25);border-radius:100px;padding:12px 22px;width:max-content;margin-left:auto;margin-right:auto;}
.avail b{color:var(--gold);}
.offers{display:grid;grid-template-columns:1fr 1fr;gap:28px;}
@media(max-width:880px){.offers{grid-template-columns:1fr;}}
.offer{background:var(--void-2);border:1px solid var(--line-strong);border-radius:22px;overflow:hidden;display:flex;flex-direction:column;box-shadow:0 30px 70px -40px rgba(0,0,0,.9);}
.offer .media{position:relative;aspect-ratio:16/10;overflow:hidden;}
.offer .media img{width:100%;height:100%;object-fit:cover;transition:transform .6s var(--ease-spring);}
.offer:hover .media img{transform:scale(1.05);}
.offer .pricetag{position:absolute;bottom:14px;right:14px;background:rgba(8,7,10,.75);backdrop-filter:blur(8px);border:1px solid var(--line-strong);
  border-radius:14px;padding:8px 14px;text-align:right;}
.offer .pricetag .o{font-size:13px;color:var(--muted-2);text-decoration:line-through;}
.offer .pricetag .n{font-family:var(--disp);font-size:26px;color:#fff;margin-left:6px;}
.offer .pricetag .pp{display:block;font-family:var(--mono);font-size:9px;letter-spacing:.08em;color:var(--muted);text-transform:uppercase;}
.offer .body{padding:26px;display:flex;flex-direction:column;flex:1;}
.offer h3{font-size:26px;color:#fff;}
.offer .worth{color:var(--muted);font-size:13.5px;margin:8px 0 16px;}.offer .worth b{color:var(--gold);}
.offer ul{list-style:none;display:flex;flex-direction:column;gap:10px;margin-bottom:22px;flex:1;}
.offer li{display:flex;align-items:flex-start;gap:10px;font-size:14px;color:#e2dfe0;}
.offer li svg{width:16px;height:16px;color:var(--lime);flex:none;margin-top:3px;}
.offer .foot{font-size:11px;color:var(--muted-2);text-align:center;margin-top:10px;}.offer .foot b{color:var(--lime);}

/* gallery */
.gal{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;}
@media(max-width:860px){.gal{grid-template-columns:repeat(2,1fr);}}
.g-cell{aspect-ratio:3/4;overflow:hidden;border-radius:14px;border:1px solid var(--line);}
.g-cell img{width:100%;height:100%;object-fit:cover;transition:transform .6s var(--ease-spring);}
.g-cell:hover img{transform:scale(1.07);}
.g-cell:nth-child(1),.g-cell:nth-child(6){grid-row:span 1;}

/* reviews */
.rev-head{display:flex;align-items:flex-end;justify-content:space-between;gap:24px;flex-wrap:wrap;}
.bigrate{text-align:right;}
.bigrate .sc{font-family:var(--disp);font-size:56px;color:var(--gold);line-height:1;}
.bigrate .mt{font-size:13px;color:var(--muted);}
.marq{overflow:hidden;margin-top:44px;-webkit-mask-image:linear-gradient(90deg,transparent,#000 5%,#000 95%,transparent);mask-image:linear-gradient(90deg,transparent,#000 5%,#000 95%,transparent);}
.marq .track{display:flex;gap:20px;width:max-content;animation:mscroll 70s linear infinite;}
@keyframes mscroll{from{transform:translateX(0)}to{transform:translateX(-50%)}}
.tcard{width:340px;flex:none;background:var(--void-2);border:1px solid var(--line-strong);border-radius:18px;padding:24px;}
.tcard p{margin:12px 0 18px;color:#e2dfe0;font-size:14.5px;line-height:1.6;}
.tcard .who{display:flex;align-items:center;gap:12px;}
.tcard .who img{width:42px;height:42px;border-radius:50%;object-fit:cover;}
.tcard .nm{font-weight:800;font-size:14px;color:#fff;}.tcard .lc{font-size:12px;color:var(--muted);}

/* verified */
.vrow{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;}
@media(max-width:820px){.vrow{grid-template-columns:1fr;}}
.vcard{display:flex;align-items:center;gap:14px;background:var(--void-2);border:1px solid var(--line-strong);border-radius:16px;padding:20px 22px;}
.vcard .vt{display:flex;align-items:center;gap:8px;}.vcard .vt strong{font-family:var(--disp);font-size:22px;color:#fff;}
.vcard .vb{font-size:12.5px;color:var(--muted);margin-top:2px;}
.partners{margin-top:40px;text-align:center;}
.partners .pl{font-family:var(--mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted-2);}
.partners .row{display:flex;flex-wrap:wrap;gap:30px;justify-content:center;margin-top:18px;}
.partners .row span{font-family:var(--disp);font-size:20px;color:var(--muted);opacity:.7;}

/* faq */
.faq-wrap{max-width:820px;margin:0 auto;}
.faq-item{border-bottom:1px solid var(--line);}
.faq-q{width:100%;display:flex;align-items:center;justify-content:space-between;gap:16px;padding:24px 4px;background:none;border:0;color:var(--cream);
  font-family:var(--body);font-weight:700;font-size:clamp(16px,2vw,19px);text-align:left;cursor:pointer;}
.faq-q .plus{position:relative;width:22px;height:22px;border:1px solid var(--line-strong);border-radius:50%;flex:none;}
.faq-q .plus::before,.faq-q .plus::after{content:'';position:absolute;background:var(--cream);left:50%;top:50%;transition:transform .35s var(--ease-spring);}
.faq-q .plus::before{width:11px;height:1.5px;transform:translate(-50%,-50%);}
.faq-q .plus::after{width:1.5px;height:11px;transform:translate(-50%,-50%);}
.faq-item.open .plus{background:var(--pink);border-color:var(--pink);}
.faq-item.open .plus::before,.faq-item.open .plus::after{background:#fff;}
.faq-item.open .plus::after{transform:translate(-50%,-50%) rotate(90deg);opacity:0;}
.faq-a{max-height:0;overflow:hidden;transition:max-height .5s var(--ease-spring);}
.faq-a p{padding:0 4px 26px;color:var(--muted);font-size:15px;line-height:1.7;max-width:680px;}
.faq-item.open .faq-a{max-height:240px;}

/* book */
.book{background:radial-gradient(ellipse 70% 60% at 15% 10%,rgba(255,23,63,.14),transparent 55%),var(--void-2);
  border:1px solid var(--line-strong);border-radius:26px;padding:clamp(30px,5vw,60px);display:grid;grid-template-columns:1.3fr .7fr;gap:40px;align-items:center;}
@media(max-width:880px){.book{grid-template-columns:1fr;}}
.book h2{font-size:clamp(30px,4vw,52px);color:#fff;}
.book p{margin:16px 0 26px;color:var(--muted);max-width:440px;}
.book .row{display:flex;gap:14px;flex-wrap:wrap;}
.contact{background:rgba(8,7,10,.6);border:1px solid var(--line);border-radius:18px;padding:24px;display:flex;flex-direction:column;gap:18px;}
.cline{display:flex;gap:12px;align-items:flex-start;}
.cline .ic{width:34px;height:34px;border-radius:10px;background:rgba(255,23,63,.12);color:var(--pink);display:grid;place-items:center;flex:none;}
.cline .ic svg{width:17px;height:17px;}
.cline .t{font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted-2);}
.cline .v{font-size:14px;color:var(--cream);}

/* footer */
footer{border-top:1px solid var(--line);padding:60px 0 40px;}
.ftop{display:grid;grid-template-columns:1.4fr 2fr;gap:40px;}
@media(max-width:820px){.ftop{grid-template-columns:1fr;}}
.flogo{display:inline-flex;align-items:center;gap:9px;font-family:var(--disp);font-size:24px;color:#fff;}
.flogo .pmark{height:24px;color:var(--pink);}
.fdesc{max-width:280px;color:var(--muted);font-size:14px;margin-top:14px;line-height:1.6;}
.fsocial{display:flex;gap:12px;margin-top:20px;}
.fsocial a{width:38px;height:38px;border-radius:50%;border:1px solid var(--line-strong);display:grid;place-items:center;color:var(--cream);}
.fsocial a:hover{border-color:var(--pink);color:var(--pink);}
.flinks{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;}
@media(max-width:560px){.flinks{grid-template-columns:repeat(2,1fr);}}
.fcol h4{font-size:13px;text-transform:uppercase;letter-spacing:.06em;color:var(--cream);margin-bottom:14px;font-family:var(--body);font-weight:800;}
.fcol a{display:block;color:var(--muted);font-size:13.5px;margin-bottom:10px;}.fcol a:hover{color:var(--cream);}
.fbot{border-top:1px solid var(--line);margin-top:40px;padding-top:24px;color:var(--muted-2);font-size:12.5px;}
.pvnote{position:fixed;bottom:14px;left:14px;z-index:60;font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;
  color:var(--muted-2);background:rgba(8,7,10,.75);border:1px solid var(--line);border-radius:100px;padding:7px 14px;backdrop-filter:blur(8px);}
.pvnote b{color:var(--pink);}
@media(prefers-reduced-motion:reduce){*{animation:none!important;}}
</style>"""

BODY = r"""
<div class="strip"><div class="tr">
  <span>RATED 4.9 BY 1,327+ CRAWLERS</span><span>·</span><span>FREE CANCELLATION UP TO 24H</span><span>·</span><span>BOOK NOW &amp; GET FREE DRINKS</span><span>·</span>
  <span>RATED 4.9 BY 1,327+ CRAWLERS</span><span>·</span><span>FREE CANCELLATION UP TO 24H</span><span>·</span><span>BOOK NOW &amp; GET FREE DRINKS</span><span>·</span>
</div></div>

<nav class="nav"><div class="container in">
  <a href="#top" class="logo">__PM__ Project&nbsp;P</a>
  <div class="links"><a href="#experiences">Experiences</a><a href="#gallery">Gallery</a><a href="#reviews">Reviews</a><a href="#faq">FAQ</a></div>
  <a href="__CRAWL_URL__" target="_blank" rel="noopener" class="btn btn-primary" style="padding:12px 22px;font-size:13px;">Book Now →</a>
</div></nav>

<header class="hero" id="top">
  <video class="hbg" muted loop autoplay playsinline poster="__POSTER__" src="__VID__"></video>
  <div class="veil"></div>
  <div class="hc">
    <div class="pbig">__PM__</div>
    <div class="left">
      <h1>The Craziest<br>Night in Porto</h1>
      <p class="sub">The guided pub crawl locals warn you about — bars, boat, club, sunrise.</p>
    </div>
    <aside class="card">
      <div class="chead"><div class="badges"><span class="bg">__GOOGLE__ <span>Google</span></span><span class="bg">__TP__ <span>Trustpilot</span></span></div>
        <div class="crate"><span class="stars">★★★★★</span><span class="rnum">4.9</span></div></div>
      <div class="revline">Rated <b>excellent</b> by <b>1,327+</b> crawlers</div>
      <div class="hr"></div>
      <div class="price"><span><s>€20</s>€17</span><small>per person</small></div>
      <ul class="plist">
        <li>__CHK__ 9 free drinks — beer, sangria &amp; shots</li>
        <li>__CHK__ VIP entry · 4 bars + 1 nightclub</li>
        <li>__CHK__ Free photos &amp; video next day</li>
      </ul>
      <div class="spots"><span class="live"></span> Only 7 spots left tonight</div>
      <a href="__CRAWL_URL__" target="_blank" rel="noopener" class="btn btn-primary btn-block">Reserve My Spot — €17</a>
      <p class="rea">1-min checkout · Free cancellation up to 24h</p>
    </aside>
  </div>
</header>

<section class="stats" style="padding:0;"><div class="container"><div class="g">
  <div class="it"><div class="n">10K+</div><div class="l">Guests Hosted</div></div>
  <div class="it"><div class="n">4.9★</div><div class="l">Average Rating</div></div>
  <div class="it"><div class="n">60+</div><div class="l">Countries Repped</div></div>
  <div class="it"><div class="n">2025</div><div class="l">Crawling Since</div></div>
</div></div></section>

<section id="experiences"><div class="container">
  <div class="shead center"><div class="tag">Choose your night</div><h2>Two ways to<br>lose track of time</h2>
    <p>Hit the streets or hit the river — either way, you're not going home before sunrise.</p></div>
  <div class="avail"><span class="live"></span> This Saturday is filling up — <b>7 spots left</b> · 41 already booked</div>
  <div class="offers">
    <div class="offer">
      <div class="media"><img src="__CRAWL__" alt="Porto Pub Crawl"><div class="pricetag"><span class="o">€20</span><span class="n">€17</span><span class="pp">per person</span></div></div>
      <div class="body">
        <h3>Porto Pub Crawl</h3>
        <p class="worth"><b>Worth €45+</b> · skip the planning, just show up.</p>
        <ul>
          <li>__CHK__ 9 free drinks — beer, sangria &amp; shots</li>
          <li>__CHK__ VIP skip-the-line entry to 4 bars + 1 nightclub</li>
          <li>__CHK__ Wild games and drink deals all night long</li>
          <li>__CHK__ Solo? Not for long — instant crew, all night</li>
          <li>__CHK__ Free photos &amp; video next day</li>
        </ul>
        <a href="__CRAWL_URL__" target="_blank" rel="noopener" class="btn btn-primary btn-block">Reserve My Spot — €17</a>
        <p class="foot">1-min checkout · Free cancellation · <b>41 booked this week</b></p>
      </div>
    </div>
    <div class="offer">
      <div class="media"><img src="__BOAT__" alt="Party Boat + Pub Crawl"><div class="pricetag"><span class="o">€55</span><span class="n">€44</span><span class="pp">per person</span></div></div>
      <div class="body">
        <h3>Party Boat + Pub Crawl</h3>
        <p class="worth">One night, two parties — river cruise straight into the crawl.</p>
        <ul>
          <li>__CHK__ 2-hour night cruise on the Douro, city lights all around</li>
          <li>__CHK__ Live DJ, drinks &amp; dancing on deck</li>
          <li>__CHK__ Straight off the boat into the crawl — 4 bars + 1 nightclub</li>
          <li>__CHK__ Free shots &amp; drink deals on boat and crawl</li>
          <li>__CHK__ One ticket, zero planning</li>
        </ul>
        <a href="__PACK_URL__" target="_blank" rel="noopener" class="btn btn-ghost btn-block">Book The Pack — €44</a>
        <p class="foot">1-min checkout · Free cancellation · <b>27 booked this week</b></p>
      </div>
    </div>
  </div>
</div></section>

<section id="gallery"><div class="container">
  <div class="shead"><div class="tag">Proof, not promises</div><h2>Straight off<br>last weekend's cards</h2></div>
  <div class="gal">__GALLERY__</div>
</div></section>

<section id="reviews"><div class="container">
  <div class="rev-head">
    <div class="shead" style="margin-bottom:0;"><div class="tag">What crawlers say</div><h2>Here's what<br>they still remember</h2></div>
    <div class="bigrate"><div class="sc">4.9</div><div class="mt"><span class="stars">★★★★★</span><br>from 1,327+ crawlers worldwide</div></div>
  </div>
  <div class="marq"><div class="track">__REVIEWS__</div></div>
</div></section>

<section id="trust"><div class="container">
  <div class="vrow">
    <div class="vcard">__TP__<div><div class="vt"><strong>4.9</strong><span class="stars" style="font-size:12px;">★★★★★</span></div><div class="vb">857 reviews on Trustpilot</div></div></div>
    <div class="vcard">__GOOGLE__<div><div class="vt"><strong>4.9</strong><span class="stars" style="font-size:12px;">★★★★★</span></div><div class="vb">470 reviews on Google</div></div></div>
    <div class="vcard"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#22ff7a" stroke-width="2"><path d="M12 2l3 6.5L22 10l-5 5 1.2 7L12 18.5 5.8 22 7 15l-5-5 7-1.5z"/></svg><div><div class="vt"><strong>Verified</strong></div><div class="vb">Licensed tour operator, Porto CM</div></div></div>
  </div>
  <div class="partners"><div class="pl">Recognized by leading travel platforms</div>
    <div class="row"><span>GetYourGuide</span><span>Viator</span><span>TripAdvisor</span><span>Eventbrite</span><span>Hostelworld</span><span>Booking</span></div>
  </div>
</div></section>

<section id="faq"><div class="container">
  <div class="shead center"><div class="tag">Before you book</div><h2>Questions,<br>answered</h2></div>
  <div class="faq-wrap">__FAQ__</div>
</div></section>

<section id="book"><div class="container">
  <div class="book">
    <div>
      <div class="tag">Lock in Saturday</div>
      <h2>Your night in<br>Porto starts here</h2>
      <p>Pick Saturday, grab your spot, and show up. The bars, the shots, the door-skipping, the strangers who become friends — we've got it covered.</p>
      <div class="row">
        <a href="__CRAWL_URL__" target="_blank" rel="noopener" class="btn btn-primary">Book The Porto Pub Crawl — €17</a>
        <a href="__WA__" target="_blank" rel="noopener" class="btn btn-ghost">Ask us on WhatsApp</a>
      </div>
    </div>
    <div class="contact">
      <div class="cline"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg></div><div><div class="t">Meeting point</div><div class="v">Praça de Carlos Alberto, 4050-157 Porto</div></div></div>
      <div class="cline"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg></div><div><div class="t">Start time</div><div class="v">22:30, every Saturday</div></div></div>
      <div class="cline"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M4 5h16v14H4z"/><path d="M4 8h16"/></svg></div><div><div class="t">Contact</div><div class="v">contact@porto-pubcrawl.com</div></div></div>
      <div class="cline"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M3 5a2 2 0 012-2h3l2 5-2.5 1.5a11 11 0 005 5L14 14l5 2v3a2 2 0 01-2 2A16 16 0 013 5z"/></svg></div><div><div class="t">WhatsApp</div><div class="v">+351 910 694 984</div></div></div>
    </div>
  </div>
</div></section>

<footer><div class="container">
  <div class="ftop">
    <div>
      <a href="#top" class="flogo">__PM__ Project&nbsp;P</a>
      <p class="fdesc">Porto's most talked-about night out, running every Saturday since 2025.</p>
      <div class="fsocial">
        <a href="https://www.instagram.com/pubcrawlporto/" target="_blank" rel="noopener" aria-label="Instagram"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="3.5"/><circle cx="17.5" cy="6.5" r="1"/></svg></a>
        <a href="__WA__" target="_blank" rel="noopener" aria-label="WhatsApp"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 5a2 2 0 012-2h3l2 5-2.5 1.5a11 11 0 005 5L14 14l5 2v3a2 2 0 01-2 2A16 16 0 013 5z"/></svg></a>
      </div>
    </div>
    <div class="flinks">
      <div class="fcol"><h4>Explore</h4><a href="#experiences">Experiences</a><a href="#gallery">Gallery</a><a href="#reviews">Reviews</a></div>
      <div class="fcol"><h4>Support</h4><a href="#faq">FAQ</a><a href="#book">Contact</a><a href="#">Privacy</a><a href="#">Terms</a></div>
      <div class="fcol"><h4>Work with us</h4><a href="#">Become a Partner</a><a href="#">Become a Guide</a></div>
      <div class="fcol"><h4>Book</h4><a href="__CRAWL_URL__" target="_blank" rel="noopener">Porto Pub Crawl — €17</a><a href="__PACK_URL__" target="_blank" rel="noopener">Party Boat + Pub Crawl — €44</a></div>
    </div>
  </div>
  <div class="fbot">© 2026 Project P — All rights reserved. · Concept preview (A/B test candidate)</div>
</div></footer>

<div class="pvnote">Preview local · <b>NOVA landing (A/B)</b> · site atual intacto</div>

<script>
  document.querySelectorAll('.faq-q').forEach(function(q){
    q.addEventListener('click',function(){
      var it=q.parentElement, open=it.classList.contains('open');
      document.querySelectorAll('.faq-item').forEach(function(i){i.classList.remove('open');});
      if(!open) it.classList.add('open');
    });
  });
  var v=document.querySelector('.hero video'); if(v){v.muted=true;var p=v.play();if(p&&p.catch)p.catch(function(){});}
</script>
"""

page = CSS + BODY
repl={"__ANTON__":ANTON,"__MAN400__":MAN400,"__MAN700__":MAN700,"__MAN800__":MAN800,"__MONO400__":MONO400,
  "__VID__":VID,"__POSTER__":POSTER,"__PM__":PM,"__GOOGLE__":GOOGLE,"__TP__":TP,"__CHK__":chk(),
  "__CRAWL__":CRAWL,"__BOAT__":BOAT,"__CRAWL_URL__":CRAWL_URL,"__PACK_URL__":PACK_URL,"__WA__":WA,
  "__GALLERY__":gallery(),"__REVIEWS__":review_cards(),"__FAQ__":faq_items()}
for k,val in repl.items(): page=page.replace(k,val)
out=base/"landing-preview.html"; out.write_text(page)
print("wrote",out,round(len(page)/1024),"KB")
