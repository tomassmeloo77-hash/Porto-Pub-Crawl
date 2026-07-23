const {chromium}=require('playwright-core');
(async()=>{
  const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
  for(const v of ['A','B','C']){
    const p=await b.newPage({viewport:{width:390,height:788},deviceScaleFactor:2});
    await p.goto('http://localhost:8099/index-b-'+v+'.html',{waitUntil:'load',timeout:30000});
    await p.waitForTimeout(1300);
    await p.screenshot({path:'scratch-preview/opt-'+v+'-hero.png'});
    await p.evaluate(()=>window.scrollTo(0, Math.round(window.innerHeight*0.62)));
    await p.waitForTimeout(600);
    await p.screenshot({path:'scratch-preview/opt-'+v+'-card.png'});
    await p.close();
  }
  await b.close();
})().catch(e=>{console.error(e);process.exit(1)});
