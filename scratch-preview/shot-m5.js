const {chromium}=require('playwright-core');
(async()=>{
  const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
  const p=await b.newPage({viewport:{width:900,height:1000},deviceScaleFactor:2});
  await p.goto('http://localhost:8099/scratch-preview/hero-m5-preview.html',{waitUntil:'load',timeout:30000});
  await p.waitForTimeout(1200);
  await p.screenshot({path:'scratch-preview/m5file-default.png'});
  await b.close();
})().catch(e=>{console.error(e);process.exit(1)});
