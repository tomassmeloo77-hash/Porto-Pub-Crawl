const {chromium}=require('playwright-core');
(async()=>{
  const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
  const p=await b.newPage({viewport:{width:1440,height:900},deviceScaleFactor:1});
  await p.goto('file:///home/user/Porto-Pub-Crawl/scratch-preview/page-b-selfcontained.html',{waitUntil:'load',timeout:30000});
  await p.waitForTimeout(1800);
  await p.screenshot({path:'scratch-preview/verify-hero.png'});
  const okVid=await p.evaluate(()=>{const v=document.querySelector('.hero video');return v&&v.currentSrc.startsWith('data:');});
  const imgs=await p.evaluate(()=>[...document.querySelectorAll('img')].filter(i=>i.src.startsWith('assets/')).map(i=>i.src));
  console.log('heroVideoInlined',okVid,'brokenImgRefs',imgs.length);
  await b.close();
})().catch(e=>{console.error(e);process.exit(1)});
