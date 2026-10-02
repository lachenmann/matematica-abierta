// Browser evidence for the rendered draft; does not publish the site.
const {chromium}=require('playwright');
const fs=require('node:fs');
const path=require('node:path');
(async()=>{
 const out='browser-evidence'; fs.mkdirSync(out,{recursive:true});
 const browser=await chromium.launch({headless:true});
 const page=await browser.newPage(); const findings=[];
 const names=fs.readdirSync('libros/otros/tratado-funciones').filter(x=>x.endsWith('.qmd')).map(x=>x.slice(0,-4));
 try {
  for(const theme of ['dark','light'])for(const width of [390,1280]){
   await page.setViewportSize({width,height:900});
   for(const name of names){
    const errors=[];const localResourceErrors=[];
    const handler=e=>errors.push(e.message);page.on('pageerror',handler);
    const resourceHandler=r=>{if(r.url().startsWith('http://127.0.0.1:8765/')&&r.status()>=400)localResourceErrors.push({url:r.url(),status:r.status()});};
    page.on('response',resourceHandler);
    const response=await page.goto(`http://127.0.0.1:8765/libros/otros/tratado-funciones/${name}.html`,{waitUntil:'networkidle'});
    if(!await page.locator('body').evaluate((body,t)=>body.classList.contains('quarto-'+t),theme))
     await page.locator('a.quarto-color-scheme-toggle').first().click();
    await page.evaluate(async()=>{if(window.MathJax?.startup?.promise)await window.MathJax.startup.promise;await document.fonts.ready;});
    const data=await page.evaluate(()=>({
     bodyWidth:document.documentElement.scrollWidth,viewport:innerWidth,
     mathSources:document.querySelectorAll('.math').length,
     mathRendered:document.querySelectorAll('mjx-container').length,
     mathErrors:document.querySelectorAll('mjx-merror, [data-mjx-error]').length,
     unrenderedMath:[...document.querySelectorAll('.math')].filter(x=>!x.querySelector('mjx-container')).map(x=>x.textContent.slice(0,100)),
     visibleMathMissing:[...document.querySelectorAll('.math')].filter(x=>x.getClientRects().length&&!x.querySelector('mjx-container')).map(x=>x.textContent.slice(0,100)),
     theme:document.body.classList.contains('quarto-dark')?'dark':'light',
     overflowing:[...document.querySelectorAll('body *')].filter(x=>{
      if(x.getBoundingClientRect().right<=innerWidth+2)return false;
      for(let p=x.parentElement;p&&p!==document.body;p=p.parentElement){if(['auto','scroll','hidden'].includes(getComputedStyle(p).overflowX)&&p.getBoundingClientRect().right<=innerWidth+2)return false;}
      return true;
     }).slice(0,12).map(x=>({tag:x.tagName,id:x.id,classes:x.className,right:x.getBoundingClientRect().right,text:x.textContent.slice(0,120)})),
     tableRegions:[...document.querySelectorAll('.tf-table')].map(x=>({tabindex:x.getAttribute('tabindex'),role:x.getAttribute('role')})),
     heading:document.querySelector('h1')?.textContent,
     h1Count:document.querySelectorAll('h1').length,
     privateLinks:document.querySelectorAll('a[href*="drive.google.com"]').length
    }));
    findings.push({name,width,expectedTheme:theme,status:response?.status(),errors,localResourceErrors,...data});
    console.log(`${width}px ${name}: width=${data.bodyWidth}, math=${data.mathRendered}, errors=${errors.length}`);
    page.off('pageerror',handler);
    page.off('response',resourceHandler);
    if(['index','capitulo-01','capitulo-16','matriz-hipotesis','apendice-b','apendice-d','bibliografia'].includes(name))
     await page.screenshot({path:path.join(out,`${name}-${width}-${theme}.png`),fullPage:true});
    if(data.bodyWidth>data.viewport+2){
     const diagnostics=await page.evaluate(()=>({scrollX,rootWidth:document.documentElement.clientWidth,
      wide:[...document.querySelectorAll('body *')].filter(x=>x.getBoundingClientRect().right>innerWidth+2).slice(0,15).map(x=>({tag:x.tagName,classes:x.className,right:x.getBoundingClientRect().right,parent:x.parentElement?.className,text:x.textContent.slice(0,100)})),
      regions:[...document.querySelectorAll('.tf-table,.sourceCode,pre,main,#quarto-content')].map(x=>({tag:x.tagName,classes:x.className,display:getComputedStyle(x).display,overflow:getComputedStyle(x).overflowX,width:x.clientWidth,scroll:x.scrollWidth,right:x.getBoundingClientRect().right}))}));
     console.log(JSON.stringify({finding:findings.at(-1),diagnostics},null,2));throw new Error(`Horizontal overflow: ${name} ${width}px ${theme}`);
    }
   }
  }
 } finally {await browser.close();fs.writeFileSync(path.join(out,'report.json'),JSON.stringify(findings,null,2));}
 const failed=findings.filter(x=>x.status!==200||!x.heading||x.h1Count!==1||x.privateLinks||x.errors.length||x.localResourceErrors.length||x.bodyWidth>x.viewport+2||x.theme!==x.expectedTheme||x.mathErrors||x.visibleMathMissing.length||(x.mathSources>0&&x.mathRendered===0)||x.tableRegions.some(t=>t.tabindex!=='0'||t.role!=='region'));
 console.log(JSON.stringify({checks:findings.length,failed},null,2));
 if(failed.length)process.exitCode=1;
})().catch(e=>{console.error(e);process.exitCode=1});
