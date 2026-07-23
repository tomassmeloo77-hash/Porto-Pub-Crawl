const {chromium}=require('playwright-core');
(async()=>{
  const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox','--autoplay-policy=no-user-gesture-required']});
  for(const [name,w,h] of [['vid-mobile',390,668],['vid-desktop',1280,760]]){
    const p=await b.newPage({viewport:{width:w,height:h},deviceScaleFactor:1});
    const errs=[]; p.on('pageerror',e=>errs.push(e.message));
    await p.goto('http://localhost:8099/index-b.html',{waitUntil:'load',timeout:30000});
    await p.waitForTimeout(2500);
    const info=await p.evaluate(()=>{const v=document.querySelector('.hero.xb .xb-hbg'); return v?{currentSrc:v.currentSrc.split('/').pop(), readyState:v.readyState, w:v.videoWidth, h:v.videoHeight, paused:v.paused}:null;});
    await p.screenshot({path:'scratch-preview/'+name+'.png'});
    console.log(name, JSON.stringify(info), 'errs:', errs.length?errs.join('|'):'none');
    await p.close();
  }
  await b.close();
})().catch(e=>{console.error(e);process.exit(1)});
