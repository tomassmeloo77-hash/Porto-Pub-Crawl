const {chromium}=require('playwright-core');
(async()=>{
  const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
  const p=await b.newPage({viewport:{width:900,height:600},deviceScaleFactor:1});
  await p.goto('http://localhost:8099/index-b.html',{waitUntil:'load',timeout:30000});
  await p.waitForTimeout(1200);
  await p.evaluate(()=>{const el=document.querySelector('.trust'); if(el) el.scrollIntoView({block:'center'});});
  await p.waitForTimeout(500);
  await p.screenshot({path:'scratch-preview/trust.png'});
  await b.close();
})().catch(e=>{console.error(e);process.exit(1)});
