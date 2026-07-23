const {chromium}=require('playwright-core');
(async()=>{
  const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
  const m=await b.newPage({viewport:{width:390,height:844},deviceScaleFactor:1,isMobile:true});
  await m.goto('http://localhost:8099/index-b.html',{waitUntil:'load',timeout:30000});
  await m.waitForTimeout(1500);
  const r=await m.evaluate(()=>{
    const q=s=>{const e=document.querySelector(s);if(!e)return null;const b=e.getBoundingClientRect();const cs=getComputedStyle(e);return {top:Math.round(b.top),bottom:Math.round(b.bottom),h:Math.round(b.height),mt:cs.marginTop,mb:cs.marginBottom,pb:cs.paddingBottom};};
    return {left:q('.xb-left'),sub:q('.xb-sub'),card:q('.xb-card'),pbig:q('.xb-pbig'),hc:q('.xb-hc')};
  });
  console.log(JSON.stringify(r,null,1));
  await b.close();
})().catch(e=>{console.error(e);process.exit(1)});
