const {chromium}=require('playwright-core');
(async()=>{
  const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
  const p=await b.newPage({viewport:{width:1440,height:900},deviceScaleFactor:2});
  await p.goto('http://localhost:8099/index-b.html',{waitUntil:'load',timeout:30000});
  // reveal all animated content + settle
  await p.addStyleTag({content:'.reveal,.reveal-scale{opacity:1!important;transform:none!important;}'});
  await p.waitForTimeout(1500);
  const H=await p.evaluate(()=>document.body.scrollHeight);
  const vh=900, step=820; let y=0, i=0;
  while(y < H){
    await p.evaluate(sy=>window.scrollTo(0,sy), y);
    await p.waitForTimeout(500);
    await p.screenshot({path:`scratch-preview/sec-${String(i).padStart(2,'0')}.png`});
    y+=step; i++;
    if(i>14) break;
  }
  await b.close();
  console.log('pageHeight',H,'shots',i);
})().catch(e=>{console.error(e);process.exit(1)});
