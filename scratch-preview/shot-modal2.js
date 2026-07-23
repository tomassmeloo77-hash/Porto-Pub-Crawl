const {chromium}=require('playwright-core');
(async()=>{
  const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
  for(const page of ['index.html','index-b.html']){
    const p=await b.newPage({viewport:{width:900,height:1000},deviceScaleFactor:1});
    const errs=[];
    p.on('pageerror',e=>errs.push('PAGEERROR: '+e.message));
    await p.goto('http://localhost:8099/'+page,{waitUntil:'load',timeout:30000});
    await p.waitForTimeout(1500);
    const trig=await p.evaluate(()=>{const el=document.querySelector('.js-book-crawl');if(!el)return 'no trigger';el.click();return 'clicked';});
    await p.waitForTimeout(1000);
    const st=await p.evaluate(()=>{const ov=document.getElementById('bookOverlay');const cs=ov?getComputedStyle(ov):null;return {display:cs&&cs.display,opacity:cs&&cs.opacity,visible:cs?(cs.display!=='none'&&cs.opacity!=='0'):null};});
    console.log(page,'| trigger:',trig,'| modal visible:',st.visible,'(opacity '+st.opacity+')','| errors:',errs.length?errs.join(' | '):'none');
    await p.close();
  }
  await b.close();
})().catch(e=>{console.error(e);process.exit(1)});
