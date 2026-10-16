const {chromium}=require('playwright');
const fs=require('fs'),path=require('path'),http=require('http');
(async()=>{
const root=path.resolve('_site'),out='.ma-build/spivak-qa';fs.mkdirSync(out,{recursive:true});
const server=http.createServer((req,res)=>{let p=path.resolve(root,decodeURIComponent(req.url.split('?')[0]).replace(/^\//,''));if(!p.startsWith(root+path.sep)){res.writeHead(403);return res.end();}fs.readFile(p,(err,data)=>{if(err){res.writeHead(404);return res.end();}const type={'.html':'text/html','.js':'application/javascript','.css':'text/css','.svg':'image/svg+xml','.png':'image/png'}[path.extname(p)]||'application/octet-stream';res.writeHead(200,{'Content-Type':type});res.end(data);});});
await new Promise(r=>server.listen(8741,'127.0.0.1',r));const browser=await chromium.launch({headless:true});const page=await browser.newPage();const results=[];
try{
for(let n=1;n<=30;n++){
 await page.setViewportSize({width:1280,height:900});await page.goto(`http://127.0.0.1:8741/problemas/colecciones/spivak-calculus/capitulo-${String(n).padStart(2,'0')}.html`,{waitUntil:'networkidle',timeout:90000});
 await page.waitForFunction(()=>window.MathJax?.startup?.promise!==undefined,{timeout:60000});await page.evaluate(async()=>await window.MathJax.startup.promise);
 const r=await page.evaluate(()=>({title:document.title,math:document.querySelectorAll('mjx-container').length,errors:[...document.querySelectorAll('mjx-merror')].map(x=>x.getAttribute('data-mjx-error')||x.textContent),broken:[...document.querySelectorAll('main img')].filter(x=>!x.complete||!x.naturalWidth).map(x=>x.src)}));
 await page.setViewportSize({width:390,height:844});r.mobile=await page.evaluate(()=>({width:document.documentElement.scrollWidth,viewport:innerWidth}));
 if([1,4,19,24,29,30].includes(n))await page.screenshot({path:`${out}/mobile-${n}.png`});results.push({chapter:n,...r});
}
fs.writeFileSync(`${out}/report.json`,JSON.stringify(results,null,2));
const bad=results.filter(r=>r.errors.length||r.broken.length||r.mobile.width>r.mobile.viewport+2);
console.log(JSON.stringify(results));if(bad.length)throw Error('Math, images or mobile overflow: '+JSON.stringify(bad));
}finally{await browser.close();server.close();}
})().catch(e=>{console.error(e);process.exit(1)});
