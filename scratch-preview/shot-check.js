const {chromium}=require('playwright-core');
(async()=>{
  const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
  const p=await b.newPage({viewport:{width:390,height:788},deviceScaleFactor:2});
  const errs=[];
  p.on('pageerror',e=>errs.push('PAGEERROR: '+e.message));
  p.on('console',m=>{if(m.type()==='error')errs.push('CONSOLE: '+m.text());});
  await p.goto('http://localhost:8099/index-b.html',{waitUntil:'load',timeout:30000});
  await p.waitForTimeout(2000);
  await p.evaluate(()=>window.scrollTo(0, document.body.scrollHeight*0.35));
  await p.waitForTimeout(800);
  await p.screenshot({path:'scratch-preview/afterexp.png'});
  console.log('JS ERRORS:', errs.length? errs.join('\n') : 'none');
  await b.close();
})().catch(e=>{console.error(e);process.exit(1)});
