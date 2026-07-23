const {chromium}=require('playwright-core');
(async()=>{
  const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
  const p=await b.newPage({viewport:{width:900,height:1000},deviceScaleFactor:1});
  const errs=[];
  p.on('pageerror',e=>errs.push('PAGEERROR: '+e.message));
  p.on('console',m=>{if(m.type()==='error'&&!/Failed to load resource|net::ERR|status of 4|status of 5/.test(m.text()))errs.push('CONSOLE: '+m.text());});
  await p.goto('http://localhost:8099/index-b.html',{waitUntil:'load',timeout:30000});
  await p.waitForTimeout(1500);
  // open modal via first book-crawl trigger
  const opened = await p.evaluate(()=>{ const el=document.querySelector('.js-book-crawl'); if(!el) return false; el.click(); return true; });
  await p.waitForTimeout(1200);
  await p.screenshot({path:'scratch-preview/modal.png'});
  // read visible modal fields
  const fields = await p.evaluate(()=>{ const labs=[...document.querySelectorAll('#bookSelectStep .book-field label')].map(l=>l.textContent.trim()).filter(Boolean); const total=document.getElementById('bookTotal')?.textContent; const pkgs=document.querySelectorAll('.pkg-opt').length; return {opened_labels:labs, total, pkgOptCount:pkgs}; });
  console.log('opened trigger:', opened);
  console.log('modal fields:', JSON.stringify(fields));
  console.log('JS ERRORS:', errs.length?errs.join(' | '):'none');
  await b.close();
})().catch(e=>{console.error(e);process.exit(1)});
