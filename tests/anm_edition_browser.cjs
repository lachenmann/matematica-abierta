const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');
const manifest = JSON.parse(fs.readFileSync('data/anm-edition-v01-manifest.json', 'utf8'));
const base = process.env.ANM_BASE_URL || 'http://127.0.0.1:8766/';
const out = process.env.ANM_QA_OUTPUT || '.ma-build/anm-browser';
fs.mkdirSync(out, {recursive:true});
const rows = []; const failures = [];
const sample = new Set(['ANM-C00.md','ANM-C03_SOLUCIONES.md','ANM-C04_MICROCONTROLES_SOLUCIONES.md','ANM-C10.md','ANM-C17.md','ANM-C21.md','ANM-C23.md','ANM-C30.md','ANM-C31.md','ANM-EPILOGO.md','ANM-PREFACIO.md']);
(async()=>{
 const options = {headless:true,args:['--no-sandbox','--disable-dev-shm-usage']};
 if(process.env.ANM_CHROME_PATH) options.executablePath=process.env.ANM_CHROME_PATH;
 const browser=await chromium.launch(options);
 try {
  const context=await browser.newContext({viewport:{width:1365,height:900},colorScheme:'light'});
  const page=await context.newPage();
  for(const item of manifest.pages){
   const url=new URL(item.path.replace(/\.md$/,'.html'),base).href;
   const response=await page.goto(url,{waitUntil:'networkidle',timeout:120000});
   if(!response || response.status()!==200)throw Error('Missing page: '+url);
   const math=await page.locator('main .math').count();
   if(math){
    await page.waitForFunction(()=>!!window.MathJax?.startup?.promise,null,{timeout:90000});
    await page.evaluate(async()=>{await MathJax.startup.promise;if(MathJax.typesetPromise)await MathJax.typesetPromise([document.querySelector('main')]);if(MathJax.whenReady)await MathJax.whenReady(()=>{});});
    const diagnostic=await page.evaluate(()=>({
     total:document.querySelectorAll('main .math').length,
     spans:document.querySelectorAll('main span.math').length,
     rendered:document.querySelectorAll('main mjx-container').length,
     missing:[...document.querySelectorAll('main span.math')].filter(x=>!x.querySelector('mjx-container')).slice(0,20).map(x=>({tag:x.tagName,text:x.textContent,html:x.outerHTML.slice(0,1500)})),
     errors:[...document.querySelectorAll('main mjx-merror,main [data-mjx-error]')].map(x=>x.textContent),
     config:MathJax.config?.loader
    }));
    fs.writeFileSync(path.join(out,item.source.replace('.md','')+'-math-diagnostic.json'),JSON.stringify(diagnostic,null,2));
    console.log('Math diagnostics',item.source,diagnostic.total,diagnostic.spans,diagnostic.rendered,diagnostic.missing.length);
    if(diagnostic.missing.length)throw Error('Unrendered math: '+JSON.stringify(diagnostic));
   }
   const result=await page.evaluate(()=>({
    math:document.querySelectorAll('main .math').length,
    rendered:document.querySelectorAll('main mjx-container').length,
    mathErrors:[...document.querySelectorAll('main mjx-merror,main [data-mjx-error]')].map(x=>x.getAttribute('data-mjx-error')||x.textContent),
    undefinedCommands:[...document.querySelectorAll('main mjx-mtext,main [mathcolor="red"]')].filter(x=>(x.style.color==='red'||x.getAttribute('mathcolor')==='red')&&/\\[A-Za-z]+/.test(x.textContent)).map(x=>x.textContent),
    brokenImages:[...document.querySelectorAll('main img')].filter(x=>!x.complete||x.naturalWidth===0).map(x=>x.src),
    duplicateIds:[...document.querySelectorAll('main [id]')].map(x=>x.id).filter((x,i,a)=>a.indexOf(x)!==i),
    overflow:document.documentElement.scrollWidth>window.innerWidth+2
   }));
   rows.push({source:item.source,url,...result});
   if(result.mathErrors.length||result.undefinedCommands.length||result.brokenImages.length||result.duplicateIds.length||result.overflow)failures.push(rows.at(-1));
   if(sample.has(item.source)){
    for(const theme of ['light','dark']){
     await page.setViewportSize({width:393,height:852});
     await page.evaluate(t=>{const toggle=document.querySelector('.quarto-color-scheme-toggle');const dark=document.body.classList.contains('quarto-dark');if((t==='dark')!==dark && toggle)toggle.click();},theme);
     await page.waitForTimeout(250);
     const overflow=await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth+2);
     if(overflow){
      const wide=await page.evaluate(()=>[...document.querySelectorAll('body *')].filter(x=>{
       if(x.getBoundingClientRect().right<=innerWidth+2)return false;
       for(let p=x.parentElement;p&&p!==document.body;p=p.parentElement)if(['auto','scroll','hidden'].includes(getComputedStyle(p).overflowX)&&p.getBoundingClientRect().right<=innerWidth+2)return false;
       return true;
      }).slice(0,12).map(x=>({tag:x.tagName,classes:String(x.className),right:x.getBoundingClientRect().right,text:x.textContent.slice(0,160)})));
      console.log('Mobile overflow',item.source,theme,JSON.stringify(wide));
      failures.push({source:item.source,kind:'mobile-overflow',theme,wide});
     }
     await page.screenshot({path:path.join(out,item.source.replace('.md','')+'-'+theme+'.png'),fullPage:false});
    }
    await page.setViewportSize({width:1365,height:900});
    await page.evaluate(()=>{if(document.body.classList.contains('quarto-dark'))document.querySelector('.quarto-color-scheme-toggle')?.click();});
   }
   fs.writeFileSync(path.join(out,'report.json'),JSON.stringify({pages:rows.length,rows,failures},null,2));
   if(rows.length%10===0)console.log('ANM browser:',rows.length,'/130');
  }
  await context.close();
 }finally{await browser.close();}
 if(failures.length)throw Error('ANM browser failures: '+failures.length);
 console.log('ANM browser PASS:',rows.length,'pages, zero formula/image/ID/overflow failures');
})().catch(e=>{fs.writeFileSync(path.join(out,'fatal.txt'),e.stack);console.error(e);process.exit(1)});
