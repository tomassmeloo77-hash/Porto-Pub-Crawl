const {chromium}=require('playwright-core');
(async()=>{
  const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
  const m=await b.newPage({viewport:{width:390,height:844},deviceScaleFactor:1,isMobile:true});
  await m.goto('http://localhost:8099/index-b.html',{waitUntil:'load',timeout:30000});
  await m.waitForTimeout(1500);
  const r=await m.evaluate(()=>{
    const hc=document.querySelector('.xb-hc');
    const csHc=getComputedStyle(hc);
    const kids=[...hc.children].map(e=>{const b=e.getBoundingClientRect();const cs=getComputedStyle(e);
      return {tag:e.tagName,cls:e.className,top:Math.round(b.top),bottom:Math.round(b.bottom),pos:cs.position,disp:cs.display,mt:cs.marginTop,alignSelf:cs.alignSelf};});
    return {hcGap:csHc.rowGap+'/'+csHc.gap,hcJustify:csHc.justifyContent,kids};
  });
  console.log(JSON.stringify(r,null,1));
  await b.close();
})().catch(e=>{console.error(e);process.exit(1)});
