const {chromium}=require('playwright-core');
(async()=>{
  const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
  const p=await b.newPage({viewport:{width:390,height:788},deviceScaleFactor:2});
  await p.goto('http://localhost:8099/index-b.html',{waitUntil:'load',timeout:30000});
  await p.waitForTimeout(1400);
  await p.screenshot({path:'scratch-preview/phone-indexb.png'});
  await b.close();
})().catch(e=>{console.error(e);process.exit(1)});
