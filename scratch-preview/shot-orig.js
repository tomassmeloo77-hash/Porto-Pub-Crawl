const {chromium}=require('playwright-core');
(async()=>{
  const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
  const p=await b.newPage({viewport:{width:1100,height:1000},deviceScaleFactor:2});
  await p.goto('http://localhost:8099/scratch-preview/hero-p3-mobile-preview.html',{waitUntil:'load',timeout:30000});
  await p.waitForTimeout(1500);
  await p.screenshot({path:'scratch-preview/orig-m5-single.png'});
  await p.goto('http://localhost:8099/scratch-preview/hero-p3-mobile-multi.html',{waitUntil:'load',timeout:30000});
  await p.waitForTimeout(1500);
  await p.evaluate(()=>{document.querySelectorAll('.switch button').forEach(b=>{if(b.dataset.m==='5')b.click();});});
  await p.waitForTimeout(600);
  await p.screenshot({path:'scratch-preview/orig-m5-topo.png'});
  await b.close();
})().catch(e=>{console.error(e);process.exit(1)});
