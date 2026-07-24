const {chromium}=require('playwright-core');
(async()=>{
  const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox','--autoplay-policy=no-user-gesture-required']});
  for(const page of ['index.html','index-b.html']){
    const p=await b.newPage({viewport:{width:390,height:800},deviceScaleFactor:2});
    const errs=[]; const reqs=[];
    p.on('pageerror',e=>errs.push('PAGEERROR: '+e.message));
    p.on('console',m=>{if(m.type()==='error'&&!/Failed to load resource|net::ERR|status of [45]|ERR_/.test(m.text()))errs.push('CONSOLE: '+m.text());});
    p.on('request',r=>reqs.push(r.url()));
    const t0=Date.now();
    await p.goto('http://localhost:8099/'+page,{waitUntil:'load',timeout:30000});
    const loadMs=Date.now()-t0;
    await p.waitForTimeout(2500);
    const perf=await p.evaluate((pageName)=>{
      const nav=performance.getEntriesByType('navigation')[0]||{};
      let lcp=0; try{ const e=performance.getEntriesByType('largest-contentful-paint'); if(e.length) lcp=Math.round(e[e.length-1].startTime);}catch(x){}
      const paints=performance.getEntriesByType('paint');
      const fcp=Math.round((paints.find(x=>x.name==='first-contentful-paint')||{}).startTime||0);
      const res=performance.getEntriesByType('resource');
      let transfer=0,decoded=0; res.forEach(r=>{transfer+=r.transferSize||0;decoded+=r.decodedBodySize||0;});
      const htmlEntry=res.find(r=>r.name.endsWith(pageName))||{};
      return { domContentLoaded: Math.round(nav.domContentLoadedEventEnd||0), loadEvent: Math.round(nav.loadEventEnd||0), fcp, lcp, resources:res.length, transferKB: Math.round(transfer/1024), decodedKB: Math.round(decoded/1024), htmlKB: Math.round((htmlEntry.decodedBodySize||0)/1024) };
    }, page);
    const mt0=Date.now();
    await p.evaluate(()=>document.querySelector('.js-book-crawl') && document.querySelector('.js-book-crawl').click());
    await p.waitForFunction(()=>{const o=document.getElementById('bookOverlay');const c=o&&getComputedStyle(o);return c&&c.opacity==='1'&&c.display!=='none';},{timeout:5000}).catch(()=>{});
    const modalMs=Date.now()-mt0;
    await p.evaluate(()=>{ const d=document.querySelector('#dateScroller > *'); if(d) d.click(); });
    const ct0=Date.now();
    await p.evaluate(()=>document.getElementById('bookSubmit') && document.getElementById('bookSubmit').click());
    await p.waitForTimeout(4000);
    const checkout=await p.evaluate(()=>{
      const mount=document.getElementById('checkoutMount');
      const loading=document.getElementById('checkoutLoading');
      const cs=document.getElementById('bookCheckoutStep');
      return { checkoutStepVisible: cs?getComputedStyle(cs).display!=='none':null, mountChildren: mount?mount.children.length:0, loadingHidden: loading?loading.classList.contains('hide'):null };
    });
    const checkoutMs=Date.now()-ct0;
    const stripeReq=reqs.filter(u=>/stripe|create-checkout-session/.test(u)).map(u=>{try{return new URL(u).host+new URL(u).pathname;}catch(e){return u;}});
    console.log('==================== '+page+' ====================');
    console.log(' LOAD: goto '+loadMs+'ms | DOMContentLoaded '+perf.domContentLoaded+'ms | loadEvent '+perf.loadEvent+'ms | FCP '+perf.fcp+'ms | LCP '+perf.lcp+'ms');
    console.log(' WEIGHT: html '+perf.htmlKB+'KB | '+perf.resources+' resources | transfer '+perf.transferKB+'KB | decoded '+perf.decodedKB+'KB');
    console.log(' MODAL: opened in '+modalMs+'ms');
    console.log(' CHECKOUT: continue -> '+checkoutMs+'ms | stepVisible='+checkout.checkoutStepVisible+' mountChildren='+checkout.mountChildren+' | stripe/api calls: '+(stripeReq.length?[...new Set(stripeReq)].join(' , '):'none (local backend absent -> fallback path)'));
    console.log(' JS ERRORS: '+(errs.length?errs.join(' | '):'NONE'));
    await p.close();
  }
  await b.close();
})().catch(e=>{console.error(e);process.exit(1)});
