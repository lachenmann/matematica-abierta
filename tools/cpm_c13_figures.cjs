// Exact diagrams for visible chapter 13 (canonical T1-C14).
// Run with @resvg/resvg-js installed: node tools/cpm_c13_figures.cjs
const fs=require('fs'),path=require('path');
const {Resvg}=require('@resvg/resvg-js');
const root=path.resolve(__dirname,'..'),out=path.join(root,'assets/books/cpm-tomo-i');
const blue='#176b91',orange='#b95418',ink='#243746',green='#287c66';
const esc=s=>String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;');
const text=(x,y,s,size=19,color=ink,anchor='start')=>`<text x="${x}" y="${y}" font-size="${size}" fill="${color}" text-anchor="${anchor}">${esc(s)}</text>`;
const line=(x1,y1,x2,y2,color=ink,dash='')=>`<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${color}" stroke-width="2" ${dash?'stroke-dasharray="'+dash+'"':''}/>`;
const rect=(x,y,w,h,color)=>`<rect x="${x}" y="${y}" width="${w}" height="${h}" fill="${color}" fill-opacity=".2" stroke="${color}" stroke-width="1.5"/>`;
const circle=(x,y,color,open=false)=>`<circle cx="${x}" cy="${y}" r="5" fill="${open?'white':color}" stroke="${color}" stroke-width="2"/>`;
function graph(ox,oy,w,h,xmax,ymin,ymax){
 const X=x=>ox+x/xmax*w,Y=y=>oy+h-(y-ymin)/(ymax-ymin)*h;
 return {X,Y,axes:line(ox,Y(0),ox+w+12,Y(0))+line(ox,oy+h,ox,oy-8)+text(ox+w+15,Y(0)+6,'x',17)+text(ox-15,oy-10,'y',17),curve:(f)=>`<polyline points="${Array.from({length:101},(_,i)=>{let x=xmax*i/100;return X(x)+','+Y(f(x))}).join(' ')}" fill="none" stroke="${ink}" stroke-width="3"/>`};
}
function bounds(n,ox,oy,w,h,kind='both',cuts=null){
 let g=graph(ox,oy,w,h,1,0,1.15),p=cuts||Array.from({length:n+1},(_,i)=>i/n),s='';
 for(let k=1;k<p.length;k++){
  let a=p[k-1],b=p[k];
  if(kind!=='lower')s+=rect(g.X(a),g.Y(b),g.X(b)-g.X(a),g.Y(0)-g.Y(b),orange);
  if(kind!=='upper')s+=rect(g.X(a),g.Y(a),g.X(b)-g.X(a),g.Y(0)-g.Y(a),blue);
 }
 for(const x of p.slice(1,-1))if(cuts)s+=line(g.X(x),g.Y(0),g.X(x),g.Y(0)+7)+text(g.X(x),g.Y(0)+26,x===.25?'1/4':'3/4',17,ink,'middle');
 return s+g.axes+g.curve(x=>x)+text(g.X(0),g.Y(0)+26,'0',17,'#243746','middle')+text(g.X(1),g.Y(0)+26,'1',17,ink,'middle')+text(g.X(.08),g.Y(1.07),'f(x) = x',18);
}
const figures=[];
function save(i,title,body,foot,height=490){
 const svg=`<svg xmlns="http://www.w3.org/2000/svg" width="800" height="${height}" viewBox="0 0 800 ${height}" role="img"><title>${esc(title)}</title><rect width="800" height="${height}" fill="white"/><g font-family="Arial, sans-serif">${text(34,42,title,25)}${body}${text(34,height-28,foot,19)}</g></svg>`;
 let file=`t1-c14-fig-${String(i).padStart(2,'0')}`;
 fs.writeFileSync(path.join(out,file+'.svg'),svg);
 fs.writeFileSync(path.join(out,file+'.png'),new Resvg(svg,{fitTo:{mode:'width',value:1600}}).render().asPng());
 figures.push({file,title,height});
}
save(1,'Encerrar el área entre dos sumas',text(75,83,'Rectángulos inferiores',20,blue)+text(455,83,'Rectángulos superiores',20,orange)+bounds(4,75,110,270,250,'lower')+bounds(4,455,110,270,250,'upper')+text(210,418,'L₄ = 3/8',22,blue,'middle')+text(590,418,'U₄ = 5/8',22,orange,'middle'),'Para f(x) = x: 3/8 ≤ área del triángulo ≤ 5/8.');
let body='';
for(const [label,p,y,col] of [['P',[0,.25,.75,1],130,blue],['Q',[0,.5,1],235,orange],['P ∪ Q',[0,.25,.5,.75,1],340,green]]){
 body+=text(35,y+6,label,21,col)+line(145,y,740,y,col);
 for(const x of p)body+=line(145+595*x,y-10,145+595*x,y+10,col)+text(145+595*x,y+36,({0:'0',.25:'1/4',.5:'1/2',.75:'3/4',1:'1'})[x],19,ink,'middle');
}
save(2,'El refinamiento común conserva todos los cortes',body,'P y Q no se refinan entre sí; P ∪ Q refina a ambas.');
let g=graph(80,90,640,310,4,0,11),s='';
for(const [a,b,c] of [[0,1,2],[1,3,1],[3,4,3]])s+=rect(g.X(a),g.Y(c),g.X(b)-g.X(a),g.Y(0)-g.Y(c),blue)+line(g.X(a),g.Y(c),g.X(b),g.Y(c),blue)+circle(g.X(a),g.Y(c),blue,true)+circle(g.X(b),g.Y(c),blue,true)+text((g.X(a)+g.X(b))/2,g.Y(c)-14,'altura '+c,18,blue,'middle');
for(const [x,y] of [[0,7],[1,5],[3,10],[4,0]])s+=circle(g.X(x),g.Y(y),orange)+text(g.X(x)+(x===4?-12:12),g.Y(y)-9,'s('+x+') = '+y,18,orange,x===4?'end':'start');
save(3,'Escalones y valores aislados son datos distintos',s+g.axes+text(150,438,'Anchuras: 1, 2, 1. Suma rectangular: 2·1 + 1·2 + 3·1 = 7.',19),'Los puntos naranjas no añaden franjas de anchura positiva.',520);
save(4,'Subdividir una franja conserva su contribución',rect(75,135,280,180,blue)+line(455,315,735,315)+rect(455,135,100,180,blue)+rect(555,135,180,180,blue)+text(210,113,'Altura c',21,blue,'middle')+text(595,113,'La misma altura c',21,blue,'middle')+text(210,350,'b − a',21,ink,'middle')+text(505,350,'t − a',20,ink,'middle')+text(645,350,'b − t',20,ink,'middle')+text(75,402,'c(b − a)',23)+text(455,402,'c(t − a) + c(b − t)',23),'La identidad de anchuras explica la invariancia de la suma.');
g=graph(100,95,600,285,2,-1.4,1.4);
s=rect(g.X(0),g.Y(1),g.X(1)-g.X(0),g.Y(0)-g.Y(1),blue)+rect(g.X(1),g.Y(0),g.X(2)-g.X(1),g.Y(-1)-g.Y(0),orange)+g.axes;
for(const [a,b,c] of [[0,1,1],[1,2,-1]])s+=line(g.X(a),g.Y(c),g.X(b),g.Y(c),c>0?blue:orange)+circle(g.X(a),g.Y(c),ink,true)+circle(g.X(b),g.Y(c),ink,true);
s+=text(g.X(.5),g.Y(.5),'+1',25,blue,'middle')+text(g.X(1.5),g.Y(-.5),'−1',25,orange,'middle');
for(let x=0;x<=2;x++)s+=text(g.X(x),g.Y(0)+25,String(x),18,ink,'middle');
save(5,'Integral con signo y área geométrica total',s+text(100,427,'Integral: 1 − 1 = 0',23)+text(445,427,'Área total: 1 + 1 = 2',23),'Los valores en 0, 1 y 2 pueden asignarse arbitrariamente.');
save(6,'Cotas en una partición no uniforme',bounds(3,130,95,540,260,'both',[0,.25,.75,1])+text(160,410,'L(f,P) = 5/16',23,blue)+text(450,410,'U(f,P) = 11/16',23,orange),'P = {0, 1/4, 3/4, 1}: las anchuras son 1/4, 1/2 y 1/4.');
save(7,'Refinar estrecha la brecha',text(75,85,'P: cuatro piezas',21)+text(455,85,'Q: ocho piezas',21)+bounds(4,75,110,270,250)+bounds(8,455,110,270,250)+text(210,418,'U − L = 1/4',22,ink,'middle')+text(590,418,'U − L = 1/8',22,ink,'middle'),'P ⊆ Q: la suma inferior sube y la superior baja.');
g=graph(100,100,600,260,1,0,1.15);s='';
const cuts=[0,.25,.75,1],tags=[.125,.5,.875];
for(let k=0;k<3;k++){
 let a=cuts[k],b=cuts[k+1],t=tags[k];
 s+=rect(g.X(a),g.Y(t),g.X(b)-g.X(a),g.Y(0)-g.Y(t),green)+line(g.X(t),g.Y(0),g.X(t),g.Y(t),green,'5 5')+circle(g.X(t),g.Y(t),green)+text(g.X(t),g.Y(0)+29,['ξ₁ = 1/8','ξ₂ = 1/2','ξ₃ = 7/8'][k],18,green,'middle');
}
save(8,'Una etiqueta fija la altura de cada rectángulo',s+g.axes+g.curve(x=>x)+text(100,425,'R = (1/8)(1/4) + (1/2)(1/2) + (7/8)(1/4) = 1/2',21),'Las etiquetas son los puntos medios de las tres piezas.');
// Contact sheet for visual verification; not a publication asset.
let sheet='<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="2080">';
for(let i=0;i<figures.length;i++){let f=figures[i],png=fs.readFileSync(path.join(out,f.file+'.png')).toString('base64');sheet+=`<image x="${i%2*800}" y="${Math.floor(i/2)*520}" width="800" height="${f.height}" href="data:image/png;base64,${png}"/>`;}
sheet+='</svg>';
fs.writeFileSync(path.join(root,'c13-figures-preview.png'),new Resvg(sheet).render().asPng());
console.log('Generated eight exact figures and visual preview.');
