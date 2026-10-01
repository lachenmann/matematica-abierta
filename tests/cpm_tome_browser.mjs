import fs from 'node:fs';
import path from 'node:path';
import {createRequire} from 'node:module';
const require=createRequire(import.meta.url);
const {chromium}=require('playwright');
const root=path.resolve(path.dirname(new URL(import.meta.url).pathname),'..');
const rows=JSON.parse(fs.readFileSync(path.join(root,'data/cpm-tome-i-manifest.json'))).chapters;
const base=process.env.CPM_QA_URL??'http://127.0.0.1:8788';
const output=path.join(root,'cpm-browser-qa');
fs.mkdirSync(output,{recursive:true});
const browser=await chromium.launch({headless:true});
const checks=[];
try {
  for(const row of rows) {
    const page=await browser.newPage({viewport:{width:320,height:900}});
    const errors=[];
    page.on('pageerror',e=>errors.push(e.message));
    let response,loadError;
    try {
      response=await page.goto(base+'/'+row.path.replace(/\.md$/,'.html'),{waitUntil:'networkidle',timeout:120000});
      await page.waitForFunction(()=>!!window.MathJax?.startup?.promise,{timeout:120000});
      await page.evaluate(async()=>{await Promise.race([Promise.all([window.MathJax.startup.promise,document.fonts.ready]),new Promise((_,reject)=>setTimeout(()=>reject(new Error('MathJax/font startup exceeded 120 seconds')),120000))]);});
    } catch(e) {loadError=e.message;}
    for(const width of [320,390,600,768,1440]) {
      const check={chapter:row.chapter,width,pass:false};
      try {
        if(loadError)throw new Error(loadError);
        await page.setViewportSize({width,height:900});
        await page.evaluate(()=>new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve))));
        Object.assign(check,await page.evaluate(()=>{
          const main=document.querySelector('main');
          // Quarto clones its TOC for responsive navigation; audit manuscript IDs.
          const ids=[...main.querySelectorAll('[id]')].map(e=>e.id);
          return {pageWidth:document.documentElement.scrollWidth,mathjax:window.MathJax.version,
            math:main.querySelectorAll('mjx-container').length,
            sourceMath:main.querySelectorAll('.math').length,
            mathErrors:main.querySelectorAll('mjx-merror,merror,[data-mjx-error]').length,
            failedImages:[...main.querySelectorAll('img')].filter(e=>!e.complete||!e.naturalWidth).map(e=>e.src),
            missingAlt:[...main.querySelectorAll('img')].filter(e=>!e.alt).length,
            unresolved:main.querySelectorAll('.quarto-unresolved-ref').length,
            duplicateIds:ids.filter((e,i)=>ids.indexOf(e)!==i),
            overflowing:[...main.querySelectorAll('*')].filter(e=>!e.closest('.math,table,pre,[style*="overflow"]')).filter(e=>e.getBoundingClientRect().right>innerWidth+2).slice(0,10).map(e=>({tag:e.tagName,text:e.textContent.slice(0,100)}))};
        }));
        check.status=response.status();check.errors=[...errors];
        check.pass=check.status===200&&check.pageWidth<=width+2&&check.math>0&&check.math===check.sourceMath&&check.mathErrors===0&&check.failedImages.length===0&&check.missingAlt===0&&check.unresolved===0&&check.duplicateIds.length===0&&check.overflowing.length===0&&errors.length===0;
        const height=await page.evaluate(()=>document.documentElement.scrollHeight);
        for(const [part,y] of [['start',0],['middle',height/2],['end',height]]) {
          await page.evaluate(y=>window.scrollTo(0,y),y);
          await page.screenshot({path:path.join(output,`${row.chapter}-${width}-${part}.png`),timeout:20000,animations:'disabled'});
        }
      } catch(e) {check.pass=false;check.exception=e.message;}
      checks.push(check);
      fs.writeFileSync(path.join(output,'results.json'),JSON.stringify({complete:checks.length===100,checks},null,2));
      console.log(JSON.stringify(check));
    }
    await page.close();
  }
} finally {await browser.close();}
const pass=checks.length===100&&checks.every(e=>e.pass);
fs.writeFileSync(path.join(output,'results.json'),JSON.stringify({status:pass?'AUTOMATED_PASS_VISUAL_REVIEW_REQUIRED':'FAIL',browser:'Chromium',checks},null,2));
process.exitCode=pass?0:1;
