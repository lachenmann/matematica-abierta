const fs=require('fs');
const m=JSON.parse(fs.readFileSync('data/cpm-tome-i-manifest.json'));
const rows=m.chapters.map(r=>{
 const c=fs.readFileSync(r.path,'utf8'),blocks=[...c.matchAll(/\$\$([\s\S]*?)\$\$/g)].map(x=>x[1]);
 return {chapter:r.visible,id:r.chapter,title:r.title,figures:(c.match(/!\[/g)||[]).length,display:blocks.length,complex:blocks.filter(x=>/aligned|cases|matrix|\\frac|\\sum|\\int/.test(x)).length,callouts:(c.match(/::: .*callout/g)||[]).length};
});
fs.writeFileSync('cpm-layout-inventory.json',JSON.stringify(rows,null,2));console.log(JSON.stringify(rows,null,2));
