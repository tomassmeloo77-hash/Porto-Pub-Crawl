const {chromium}=require('playwright-core');
(async()=>{
  const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
  const p=await b.newPage({viewport:{width:390,height:788},deviceScaleFactor:2});
  await p.goto('http://localhost:8099/index-b.html',{waitUntil:'load',timeout:30000});
  await p.waitForTimeout(1000);
  // measure natural width of "NIGHT IN PORTO" at various font sizes with Anton
  const res=await p.evaluate(()=>{
    const span=document.createElement('span');
    span.style.cssText="font-family:'Anton',sans-serif;text-transform:uppercase;letter-spacing:.005em;white-space:nowrap;position:absolute;visibility:hidden;";
    span.textContent="NIGHT IN PORTO";
    document.body.appendChild(span);
    const out={};
    for(const fs of [55,58,60,62,64,66]){span.style.fontSize=fs+'px';out[fs]=Math.round(span.getBoundingClientRect().width);}
    // also with tighter letter-spacing
    span.style.letterSpacing="-0.01em";
    const tight={};
    for(const fs of [58,60,62,64,66]){span.style.fontSize=fs+'px';tight[fs]=Math.round(span.getBoundingClientRect().width);}
    document.body.removeChild(span);
    return {viewport:window.innerWidth, normal:out, tight:tight};
  });
  console.log(JSON.stringify(res,null,1));
  await b.close();
})().catch(e=>{console.error(e);process.exit(1)});
