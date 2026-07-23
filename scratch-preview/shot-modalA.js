const {chromium}=require('playwright-core');
(async()=>{
  const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
  const p=await b.newPage({viewport:{width:900,height:1000},deviceScaleFactor:1});
  const errs=[];
  p.on('pageerror',e=>errs.push('PAGEERROR: '+e.message));
  p.on('console',m=>{if(m.type()==='error'&&!/Failed to load resource|net::ERR|status of [45]/.test(m.text()))errs.push('CONSOLE: '+m.text());});
  await p.goto('http://localhost:8099/index.html',{waitUntil:'load',timeout:30000});
  await p.waitForTimeout(1500);
  const trig = await p.evaluate(()=>{ const el=document.querySelector('.js-book-crawl'); if(!el) return 'NO .js-book-crawl trigger'; el.click(); return 'clicked'; });
  await p.waitForTimeout(1200);
  const state = await p.evaluate(()=>{ const ov=document.getElementById('bookOverlay'); const cs=ov?getComputedStyle(ov):null; return { overlayExists:!!ov, display:cs?cs.display:null, visible: cs? (cs.display!=='none' && cs.visibility!=='hidden' && cs.opacity!=='0'):null, opacity:cs?cs.opacity:null, hasOpenClass: ov?ov.className:null }; });
  await p.screenshot({path:'scratch-preview/modalA.png'});
  console.log('trigger:', trig);
  console.log('modal state:', JSON.stringify(state));
  console.log('JS ERRORS:', errs.length?errs.join(' | '):'none');
  await b.close();
})().catch(e=>{console.error(e);process.exit(1)});
