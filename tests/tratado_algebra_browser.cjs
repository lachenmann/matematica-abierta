const {chromium}=require('playwright');
const fs=require('node:fs');
const path=require('node:path');
const out='talg-browser-evidence';
const chapters=fs.readdirSync('libros/capitulos').filter(n=>/^tratado-de-algebra-capitulo-(0|21|27|28|30|34|37|39|40)-.*\.md$/.test(n));
const pages=['libros/otros/tratado-de-algebra.html','libros/tratados/index.html','libros/index.html',...chapters.map(n=>'libros/capitulos/'+n.replace(/\.md$/,'.html'))];
(async()=>{
 fs.mkdirSync(out,{recursive:true});
 let ready=false;
 for(let attempt=0;attempt<50;attempt++){
  try{const response=await fetch('http://127.0.0.1:8789/'+pages[0],{signal:AbortSignal.timeout(1000)});if(response.ok){ready=true;break;}}catch{}
  await new Promise(resolve=>setTimeout(resolve,100));
 }
 if(!ready)throw new Error('The review server did not become ready');
 const browser=await chromium.launch({headless:true});
 const page=await browser.newPage();
 page.setDefaultTimeout(90000);
 const findings=[];
 try{
  for(const theme of ['dark','light'])for(const width of [390,1280]){
   await page.setViewportSize({width,height:900});
   for(const file of pages){
    const errors=[],resources=[];
    const onError=e=>errors.push(e.message);
    const onResponse=r=>{if(r.url().startsWith('http://127.0.0.1:8789/')&&r.status()>=400)resources.push({url:r.url(),status:r.status()});};
    page.on('pageerror',onError);page.on('response',onResponse);
    await page.mouse.move(0,0);
    const response=await page.goto('http://127.0.0.1:8789/'+file,{waitUntil:'networkidle'});
    if(!await page.locator('body').evaluate((body,t)=>body.classList.contains('quarto-'+t),theme))
      await page.locator('a.quarto-color-scheme-toggle').first().click();
    await page.evaluate(async()=>{if(window.MathJax?.startup?.promise)await window.MathJax.startup.promise;await document.fonts.ready;});
    const data=await page.evaluate(()=>({
     documentWidth:document.documentElement.scrollWidth,viewport:innerWidth,
     h1:[...document.querySelectorAll('main h1')].filter(x=>x.getClientRects().length&&getComputedStyle(x).visibility!=='hidden').length,
     mathSources:document.querySelectorAll('main .math').length,
     mathRendered:document.querySelectorAll('main mjx-container').length,
     mathErrors:document.querySelectorAll('main mjx-merror,main [data-mjx-error]').length,
     missingMath:[...document.querySelectorAll('main .math')].filter(x=>x.getClientRects().length&&!x.querySelector('mjx-container')).map(x=>x.textContent.slice(0,100)),
     theme:document.body.classList.contains('quarto-dark')?'dark':'light',
     privateLinks:document.querySelectorAll('main a[href*="drive.google.com"]').length,
     oversized:[...document.querySelectorAll('main *')].filter(x=>{
      if(x.getBoundingClientRect().right<=innerWidth+2)return false;
      for(let p=x.parentElement;p&&p!==document.body;p=p.parentElement){
       if(['auto','scroll','hidden','clip'].includes(getComputedStyle(p).overflowX)&&p.getBoundingClientRect().right<=innerWidth+2)return false;
      }
      return true;
     }).slice(0,10).map(x=>({tag:x.tagName,id:x.id,text:x.textContent.slice(0,80),right:x.getBoundingClientRect().right}))
    }));
    const row={file,width,expectedTheme:theme,status:response?.status(),errors,resources,...data};
    findings.push(row);
    console.log(JSON.stringify(row));
    const name=file.replace(/\.html$/,'').replaceAll('/','__');
    await page.screenshot({path:path.join(out,name+'-'+width+'-'+theme+'.png')});
    if(file==='libros/otros/tratado-de-algebra.html'){
     const locations=[
      ['edition',page.getByRole('heading',{name:/^Edición web completa/})],
      ['contents',page.locator('#parte-0')],
      ['closure',page.locator('#parte-viii')]
     ];
     for(const [label,location] of locations){
      await location.evaluate(el=>window.scrollTo({top:el.getBoundingClientRect().top+window.scrollY-100,behavior:'instant'}));
      await page.screenshot({path:path.join(out,name+'-'+label+'-'+width+'-'+theme+'.png')});
     }
    }
    if(file.endsWith('capitulo-21-dominios-integros.html')){
     await page.locator('#cierre-deductivo').evaluate(el=>window.scrollTo({top:el.getBoundingClientRect().top+window.scrollY-100,behavior:'instant'}));
     await page.screenshot({path:path.join(out,name+'-closure-'+width+'-'+theme+'.png')});
    }
    if(file.endsWith('capitulo-40-infraestructura-tensorial-minima.html')){
     for(const id of ['talg-def-00081','talg-thm-00044','talg-thm-00046']){
      await page.locator('#'+id).evaluate(el=>window.scrollTo({top:el.getBoundingClientRect().top+window.scrollY-100,behavior:'instant'}));
      await page.screenshot({path:path.join(out,name+'-'+id+'-'+width+'-'+theme+'.png')});
     }
    }
    if(file.endsWith('tratado-de-algebra.html')||file.endsWith('capitulo-40-infraestructura-tensorial-minima.html')){
     const before=await page.locator('main').evaluate(el=>parseFloat(getComputedStyle(el).fontSize));
     await page.getByRole('button',{name:'Aumentar tamaño de letra',exact:true}).click();
     const after=await page.locator('main').evaluate(el=>parseFloat(getComputedStyle(el).fontSize));
     row.readerControls=after>before;
     await page.getByRole('button',{name:'Restablecer tamaño de letra',exact:true}).click();
    }
    page.off('pageerror',onError);page.off('response',onResponse);
   }
  }
 }finally{
  await browser.close();
  fs.writeFileSync(path.join(out,'report.json'),JSON.stringify(findings,null,2));
 }
 const failures=findings.filter(r=>r.status!==200||r.h1!==1||r.errors.length||r.resources.length||r.documentWidth>r.viewport+2||r.theme!==r.expectedTheme||r.mathErrors||r.missingMath.length||r.privateLinks||r.readerControls===false);
 const summary={status:failures.length?'FAIL':'PASS',pages:pages.length,checks:findings.length,failures};
 fs.writeFileSync(path.join(out,'summary.json'),JSON.stringify(summary,null,2));
 console.log(JSON.stringify(summary,null,2));
 if(failures.length)process.exitCode=1;
})().catch(e=>{console.error(e);process.exitCode=1;});
