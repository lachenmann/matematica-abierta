// Browser QA for La demostración admirable; validates the rendered candidate without publishing it.
const {chromium}=require('playwright');
const fs=require('node:fs');
const path=require('node:path');

(async()=>{
  const out='browser-evidence-fda';
  fs.mkdirSync(out,{recursive:true});
  const browser=await chromium.launch({headless:true});
  const page=await browser.newPage();
  const findings=[];
  const names=[
    'index','preambulo','01-problema-detras-leyenda','02-diofanto-ii8',
    '03-horizonte-matematico-fermat','04-descenso-biquadratico','05-cubo-perdido',
    '06-grafos-descenso','07-unica-formula-no-basta','08-demostracion-general',
    '09-limites-conocimiento','apendice-a-cronologia','apendice-b-anatomia-descenso',
    'apendice-c-controles-p5-p7','apendice-d-escala-evidencia','apendice-e-observatio',
    'bibliografia'
  ];
  const screenshotNames=new Set(['index','04-descenso-biquadratico','05-cubo-perdido','apendice-a-cronologia','apendice-c-controles-p5-p7','apendice-e-observatio','bibliografia']);
  try {
    for(const theme of ['dark','light']){
      for(const width of [390,1280]){
        await page.setViewportSize({width,height:900});
        for(const name of names){
          const errors=[];
          const localResourceErrors=[];
          const pageError=e=>errors.push(e.message);
          const responseError=r=>{
            if(r.url().startsWith('http://127.0.0.1:8765/')&&r.status()>=400)
              localResourceErrors.push({url:r.url(),status:r.status()});
          };
          page.on('pageerror',pageError);
          page.on('response',responseError);
          const response=await page.goto(`http://127.0.0.1:8765/libros/otros/la-demostracion-admirable/${name}.html`,{waitUntil:'networkidle'});
          const toggle=page.locator('a.quarto-color-scheme-toggle').first();
          const currentTheme=await page.locator('body').evaluate(body=>body.classList.contains('quarto-dark')?'dark':'light');
          if(currentTheme!==theme && await toggle.count()) await toggle.click();
          await page.evaluate(async()=>{
            if(window.MathJax?.startup?.promise) await window.MathJax.startup.promise;
            await document.fonts.ready;
          });
          const data=await page.evaluate(()=>({
            bodyWidth:document.documentElement.scrollWidth,
            viewport:innerWidth,
            heading:document.querySelector('h1')?.textContent?.trim()||'',
            h1Count:document.querySelectorAll('h1').length,
            theme:document.body.classList.contains('quarto-dark')?'dark':'light',
            mathSources:document.querySelectorAll('.math').length,
            mathRendered:document.querySelectorAll('mjx-container').length,
            mathErrors:document.querySelectorAll('mjx-merror,[data-mjx-error]').length,
            visibleMathMissing:[...document.querySelectorAll('.math')].filter(x=>x.getClientRects().length&&!x.querySelector('mjx-container')).map(x=>x.textContent.slice(0,120)),
            privateLinks:document.querySelectorAll('a[href*="drive.google.com"]').length,
            visibleInternalIds:(document.body.innerText.match(/FDA-[A-Z0-9-]+/g)||[]).slice(0,10),
            sourceMatrixVisible:document.body.innerText.includes('SOURCE_MATRIX'),
            footnotes:document.querySelectorAll('section.footnotes li,.footnotes li').length,
            callouts:document.querySelectorAll('.callout').length,
            indexLinks:[...document.querySelectorAll('a')].filter(a=>a.textContent.trim()==='Índice').length,
            tables:[...document.querySelectorAll('table')].map(t=>{
              const r=t.getBoundingClientRect();
              let scrollable=false;
              for(let p=t.parentElement;p&&p!==document.body;p=p.parentElement){
                const ov=getComputedStyle(p).overflowX;
                if(['auto','scroll'].includes(ov)){scrollable=true;break;}
              }
              return {width:r.width,right:r.right,scrollable};
            }),
            overflowing:[...document.querySelectorAll('body *')].filter(x=>{
              if(x.getBoundingClientRect().right<=innerWidth+2)return false;
              for(let p=x.parentElement;p&&p!==document.body;p=p.parentElement){
                if(['auto','scroll','hidden'].includes(getComputedStyle(p).overflowX)&&p.getBoundingClientRect().right<=innerWidth+2)return false;
              }
              return true;
            }).slice(0,12).map(x=>({tag:x.tagName,id:x.id,classes:String(x.className||''),right:x.getBoundingClientRect().right,text:(x.textContent||'').slice(0,120)}))
          }));
          const finding={name,width,expectedTheme:theme,status:response?.status(),errors,localResourceErrors,...data};
          findings.push(finding);
          console.log(`${theme} ${width}px ${name}: status=${finding.status} width=${data.bodyWidth}/${data.viewport} math=${data.mathRendered} errors=${errors.length}`);
          page.off('pageerror',pageError);
          page.off('response',responseError);
          if(screenshotNames.has(name))
            await page.screenshot({path:path.join(out,`${name}-${width}-${theme}.png`),fullPage:true});
          if(data.bodyWidth>data.viewport+2){
            console.log(JSON.stringify(finding,null,2));
            throw new Error(`Horizontal overflow: ${name} ${width}px ${theme}`);
          }
        }
      }
    }
  } finally {
    await browser.close();
    fs.writeFileSync(path.join(out,'report.json'),JSON.stringify(findings,null,2));
  }
  const failed=findings.filter(x=>
    x.status!==200 || !x.heading || x.h1Count!==1 ||
    x.theme!==x.expectedTheme || x.errors.length || x.localResourceErrors.length ||
    x.bodyWidth>x.viewport+2 || x.mathErrors || x.visibleMathMissing.length ||
    (x.mathSources>0&&x.mathRendered===0) || x.privateLinks ||
    x.visibleInternalIds.length || x.sourceMatrixVisible
  );
  const mobile=findings.filter(x=>x.width===390);
  const mobileTables=mobile.flatMap(x=>x.tables.map(t=>({page:x.name,...t})));
  const summary={
    checks:findings.length,
    expectedChecks:17*2*2,
    failed,
    footnoteTotalAt390Light:findings.filter(x=>x.width===390&&x.expectedTheme==='light').reduce((n,x)=>n+x.footnotes,0),
    mobileTables,
    mobileTableFailures:mobileTables.filter(t=>t.width>390+2&&!t.scrollable),
    screenshots:fs.readdirSync(out).filter(x=>x.endsWith('.png')).length
  };
  fs.writeFileSync(path.join(out,'summary.json'),JSON.stringify(summary,null,2));
  console.log(JSON.stringify(summary,null,2));
  if(findings.length!==68 || failed.length || summary.footnoteTotalAt390Light!==14 || summary.mobileTableFailures.length) process.exitCode=1;
})().catch(e=>{console.error(e);process.exitCode=1});
