import fs from 'node:fs';
import path from 'node:path';
import {createRequire} from 'node:module';
const require=createRequire(import.meta.url);
const {chromium}=require('playwright');
const root=path.resolve(path.dirname(new URL(import.meta.url).pathname),'..');
const chapters=JSON.parse(fs.readFileSync(path.join(root,'data/cpm-tome-i-manifest.json'))).chapters;
const rows=chapters.flatMap(row=>[row,...(row.pages??[]).map(p=>({...p,chapter:row.chapter+'-'+path.basename(p.path,'.md')}))]);
const expectedChecks=rows.length*5;
const base=process.env.CPM_QA_URL??'http://127.0.0.1:8788';
const output=path.join(root,'cpm-browser-qa');
fs.mkdirSync(output,{recursive:true});
const browser=await chromium.launch({headless:true});
const checks=[];
let phase={name:'launch',chapter:null,width:null};
function checkpoint(name,chapter,width=null) {
  phase={name,chapter,width,time:new Date().toISOString()};
  fs.writeFileSync(path.join(output,'progress.json'),JSON.stringify({phase,checks},null,2));
  console.log(JSON.stringify({phase}));
}
try {
  for(const row of rows) {
    checkpoint('open-page',row.chapter);
    // Independent Node timer also fires if Chromium's rendering thread stalls.
    const watchdog=setTimeout(()=>{
      fs.writeFileSync(path.join(output,'results.json'),JSON.stringify({status:'FAIL',complete:false,exception:'Chapter exceeded five minutes',phase,checks},null,2));
      console.error('Chapter watchdog expired: '+JSON.stringify(phase));
      process.exit(1);
    },300000);
    const page=await browser.newPage({viewport:{width:320,height:900}});
    const errors=[];
    page.on('pageerror',e=>errors.push(e.message));
    let response,loadError;
    try {
      checkpoint('navigate',row.chapter);
      response=await page.goto(base+'/'+row.path.replace(/\.md$/,'.html'),{waitUntil:'networkidle',timeout:120000});
      checkpoint('mathjax-startup',row.chapter);
      await page.waitForFunction(()=>!!window.MathJax?.startup?.promise,{timeout:120000});
      await page.evaluate(async()=>{await Promise.race([Promise.all([window.MathJax.startup.promise,document.fonts.ready]),new Promise((_,reject)=>setTimeout(()=>reject(new Error('MathJax/font startup exceeded 120 seconds')),120000))]);});
    } catch(e) {loadError=e.message;}
    for(const width of [320,390,600,768,1440]) {
      const check={chapter:row.chapter,width,pass:false};
      try {
        if(loadError)throw new Error(loadError);
        checkpoint('resize',row.chapter,width);
        await page.setViewportSize({width,height:900});
        await page.evaluate(()=>new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve))));
        checkpoint('inspect',row.chapter,width);
        Object.assign(check,await page.evaluate(()=>{
          const main=document.querySelector('main');
          // Quarto clones its TOC for responsive navigation; audit manuscript IDs.
          const ids=[...main.querySelectorAll('[id]')].map(e=>e.id);
          return {pageWidth:document.documentElement.scrollWidth,mathjax:window.MathJax.version,
            math:main.querySelectorAll('mjx-container').length,
            sourceMath:main.querySelectorAll('.math').length,
            mathErrors:main.querySelectorAll('mjx-merror,merror,[data-mjx-error]').length,
            // noUndefined renders unknown commands as red mtext, not merror.
            undefinedCommands:[...main.querySelectorAll('mjx-container')].filter(e=>
              e.querySelector('[mathcolor="red"]') ||
              [...e.querySelectorAll('mjx-mtext')].some(n=>n.style.color==='red') ||
              /\\[A-Za-z]+/.test(e.textContent)
            ).map(e=>e.textContent.slice(0,300)),
            failedImages:[...main.querySelectorAll('img')].filter(e=>!e.complete||!e.naturalWidth).map(e=>e.src),
            missingAlt:[...main.querySelectorAll('img')].filter(e=>!e.alt).length,
            unresolved:main.querySelectorAll('.quarto-unresolved-ref').length,
            duplicateIds:ids.filter((e,i)=>ids.indexOf(e)!==i),
            overflowing:[...main.querySelectorAll('*')].filter(e=>!e.closest('.math,table,pre,[style*="overflow"]')).filter(e=>e.getBoundingClientRect().right>innerWidth+2).slice(0,10).map(e=>({tag:e.tagName,text:e.textContent.slice(0,100)}))};
        }));
        check.status=response.status();check.errors=[...errors];
        check.pass=check.status===200&&check.pageWidth<=width+2&&check.math>0&&check.math===check.sourceMath&&check.mathErrors===0&&check.undefinedCommands.length===0&&check.failedImages.length===0&&check.missingAlt===0&&check.unresolved===0&&check.duplicateIds.length===0&&check.overflowing.length===0&&errors.length===0;
        const height=await page.evaluate(()=>document.documentElement.scrollHeight);
        for(const [part,y] of [['start',0],['middle',height/2],['end',height]]) {
          checkpoint('capture-'+part,row.chapter,width);
          await page.evaluate(y=>window.scrollTo(0,y),y);
          await page.screenshot({path:path.join(output,`${row.chapter}-${width}-${part}.png`),timeout:20000,animations:'disabled'});
        }
      } catch(e) {check.pass=false;check.exception=e.message;}
      checks.push(check);
      fs.writeFileSync(path.join(output,'results.json'),JSON.stringify({complete:checks.length===expectedChecks,checks},null,2));
      console.log(JSON.stringify(check));
    }
    checkpoint('close-page',row.chapter);
    await page.close();
    clearTimeout(watchdog);
  }
} finally {await browser.close();}
const pass=checks.length===expectedChecks&&checks.every(e=>e.pass);
fs.writeFileSync(path.join(output,'results.json'),JSON.stringify({status:pass?'AUTOMATED_PASS_VISUAL_REVIEW_REQUIRED':'FAIL',browser:'Chromium',checks},null,2));
process.exitCode=pass?0:1;

