const {chromium}=require('playwright-core');
(async()=>{
  const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
  // desktop
  let p=await b.newPage({viewport:{width:1440,height:900},deviceScaleFactor:2});
  await p.goto('http://localhost:8099/index-b.html',{waitUntil:'load',timeout:30000});
  await p.waitForTimeout(2500);
  await p.screenshot({path:'scratch-preview/shot-desktop-hero.png'});
  // desktop full page (long)
  await p.screenshot({path:'scratch-preview/shot-desktop-full.png',fullPage:true});
  await p.close();
  // mobile
  let m=await b.newPage({viewport:{width:390,height:844},deviceScaleFactor:3,isMobile:true});
  await m.goto('http://localhost:8099/index-b.html',{waitUntil:'load',timeout:30000});
  await m.waitForTimeout(2500);
  await m.screenshot({path:'scratch-preview/shot-mobile-hero.png'});
  await m.close();
  await b.close();
  console.log('done');
})().catch(e=>{console.error(e);process.exit(1)});
