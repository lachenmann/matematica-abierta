// EDC publication QA: each page in desktop/phone, light/dark samples, MathJax and assets.
const { chromium } = require('playwright');
const fs=require('fs'),path=require('path');
const output='.ma-build/edc-browser';fs.mkdirSync(output,{recursive:true});
const folder='libros/otros/elementos-del-calculo';
const pages=fs.readdirSync(folder).filter(x=>/\.(md|qmd)$/.test(x)).map(x=>x.replace(/\.(md|qmd)$/,'.html'));
const base=process.env.EDC_QA_URL||'http://127.0.0.1:8767';
(async()=>{
 const browser=await chromium.launch();const results=[],darkChecks=[];
 for(const width of [390,1440]){
  const context=await browser.newContext({viewport:{width,height:1000}});
  for(const filename of pages){
   const page=await context.newPage();const errors=[];page.on('pageerror',e=>errors.push(String(e)));
   const response=await page.goto(`${base}/${folder}/${filename}`,{waitUntil:'networkidle',timeout:90000});
   if(!await page.locator('body').evaluate(body=>body.classList.contains('quarto-light')))
    await page.locator('a.quarto-color-scheme-toggle').first().click();
   if(await page.locator('main .math').count()){
    await page.waitForFunction(()=>!!window.MathJax?.startup?.promise,null,{timeout:90000});
    await page.evaluate(async()=>{await MathJax.startup.promise;});
   }
   await page.evaluate(async()=>{await document.fonts.ready;});
   const check=await page.evaluate(()=>{
    const main=document.querySelector('main.content');const ids=[...main.querySelectorAll('[id]')].map(e=>e.id);
    return {width:innerWidth,pageWidth:document.documentElement.scrollWidth,theme:document.body.classList.contains('quarto-light')?'light':'dark',
     sourceMath:main.querySelectorAll('.math').length,renderedMath:main.querySelectorAll('mjx-container').length,
     mathErrors:main.querySelectorAll('mjx-merror,merror,[data-mjx-error],[mathcolor="red"]').length,
     failedImages:[...main.querySelectorAll('img')].filter(e=>!e.complete||!e.naturalWidth).map(e=>e.src),
     emptyAlt:main.querySelectorAll('img:not([alt]),img[alt=""]').length,
     duplicateIds:ids.filter((x,i)=>ids.indexOf(x)!==i),
     privateReferences:/EDC_M00_AUDITORIA|DECISIONES_ARQUITECTURA|INVENTARIO_EDC|\[\[|drive\.google\.com/.test(main.innerText),
     titleCount:main.querySelectorAll('h1').length,
     missingFragments:[...main.querySelectorAll('a[href^="#"]')].filter(a=>a.hash.length>1&&!document.getElementById(decodeURIComponent(a.hash.slice(1)))).map(a=>a.hash)};
   });
   Object.assign(check,{filename,status:response.status(),errors});
   check.pass=check.status===200&&check.theme==='light'&&check.pageWidth<=width+2&&check.sourceMath===check.renderedMath&&!check.mathErrors&&!check.failedImages.length&&!check.emptyAlt&&!check.duplicateIds.length&&!check.privateReferences&&!check.missingFragments.length&&!errors.length&&check.titleCount===1;
   results.push(check);console.log(JSON.stringify({filename,width,math:check.renderedMath,pass:check.pass}));
   if(['index.html','capitulo-00-notas.html','capitulo-03-notas.html','capitulo-02.html','capitulo-05.html','capitulo-09-soluciones.html','figuras.html','edicion.html'].includes(filename)){
    await page.screenshot({path:path.join(output,filename.replace('.html',`-${width}.png`))});
    if(filename==='capitulo-02.html'||filename==='figuras.html'){
     const image=page.locator('main img').first();if(await image.count()){await image.scrollIntoViewIfNeeded();await page.screenshot({path:path.join(output,`figure-${filename}-${width}.png`)});}
    }
    await page.locator('a.quarto-color-scheme-toggle').first().click();
    await page.evaluate(async()=>{await document.fonts.ready;});
    const dark=await page.evaluate(()=>({theme:document.body.classList.contains('quarto-dark')?'dark':'light',width:innerWidth,pageWidth:document.documentElement.scrollWidth,mathErrors:document.querySelectorAll('mjx-merror,merror,[data-mjx-error],[mathcolor="red"]').length}));
    dark.pass=dark.theme==='dark'&&dark.pageWidth<=width+2&&!dark.mathErrors;dark.filename=filename;darkChecks.push(dark);
    await page.screenshot({path:path.join(output,filename.replace('.html',`-${width}-dark.png`))});
   }
   fs.writeFileSync(path.join(output,'results.json'),JSON.stringify({complete:results.length===pages.length*2,checks:results,darkChecks},null,2));await page.close();
  }
  await context.close();
 }
 await browser.close();
 if(!results.every(x=>x.pass)||!darkChecks.every(x=>x.pass))throw new Error(JSON.stringify({failed:results.filter(x=>!x.pass),darkFailed:darkChecks.filter(x=>!x.pass)}));
 console.log(`EDC: ${results.length}/${pages.length*2} desktop/phone pages and ${darkChecks.length} dark-theme samples PASS`);
})().catch(e=>{console.error(e);process.exit(1);});
