const {chromium}=require('playwright-core');
(async()=>{
  const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox','--autoplay-policy=no-user-gesture-required']});
  for(const page of ['index.html','index-b.html']){
    const p=await b.newPage({viewport:{width:390,height:800},deviceScaleFactor:1});
    const errs=[];
    p.on('pageerror',e=>errs.push('PAGEERROR: '+e.message));
    p.on('console',m=>{if(m.type()==='error'&&!/Failed to load resource|net::ERR|status of [45]|ERR_/.test(m.text()))errs.push('CONSOLE: '+m.text());});
    await p.goto('http://localhost:8099/'+page,{waitUntil:'load',timeout:30000});
    await p.waitForTimeout(2000);
    const info=await p.evaluate(()=>{
      const heroVid=document.querySelector('.hero .xb-hbg, .hero-video, video');
      const bookBtns=document.querySelectorAll('.js-book-crawl').length;
      return { heroVideo: !!heroVid, bookTriggers: bookBtns };
    });
    // open modal
    const opened=await p.evaluate(()=>{const el=document.querySelector('.js-book-crawl'); if(!el) return 'no trigger'; el.click(); return 'clicked';});
    await p.waitForTimeout(1000);
    const modal=await p.evaluate(()=>{
      const ov=document.getElementById('bookOverlay'); const cs=ov?getComputedStyle(ov):null;
      const visible = cs? (cs.display!=='none'&&cs.opacity!=='0'&&cs.visibility!=='hidden'):false;
      const labels=[...document.querySelectorAll('#bookSelectStep .book-field label')].map(l=>l.textContent.trim());
      const total=document.getElementById('bookTotal')?.textContent;
      const pkgs=document.querySelectorAll('.pkg-opt').length;
      return { visible, fields:labels, total, pkgOptions:pkgs };
    });
    // close and check phog booted (register worked)
    const ph=await p.evaluate(()=> (window.posthog && typeof window.posthog.capture==='function') ? (window.__ppVariant||'?') : 'posthog NOT booted');
    console.log('== '+page+' ==');
    console.log('  hero video el:', info.heroVideo, '| book triggers:', info.bookTriggers);
    console.log('  modal opens:', modal.visible, '| fields:', JSON.stringify(modal.fields), '| total:', modal.total, '| pkgOptions:', modal.pkgOptions);
    console.log('  posthog booted / variant:', ph);
    console.log('  JS errors:', errs.length?errs.join(' | '):'NONE');
    await p.close();
  }
  await b.close();
})().catch(e=>{console.error(e);process.exit(1)});
