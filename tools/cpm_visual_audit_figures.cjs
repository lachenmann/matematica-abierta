// Exact mathematical diagrams; requires @resvg/resvg-js.
const fs=require('fs'),path=require('path'),{Resvg}=require('@resvg/resvg-js');
const out=path.resolve(__dirname,'../assets/books/cpm-tomo-i'),blue='#176b91',orange='#b95418',green='#287c66',ink='#243746';
const esc=s=>String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;');
const T=(x,y,s,size=19,color=ink,anchor='start')=>`<text x="${x}" y="${y}" font-size="${size}" fill="${color}" text-anchor="${anchor}">${esc(s)}</text>`;
const L=(x1,y1,x2,y2,col=ink,dash='')=>`<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${col}" stroke-width="2" ${dash?'stroke-dasharray="'+dash+'"':''}/>`;
const C=(x,y,col=blue,open=false)=>`<circle cx="${x}" cy="${y}" r="5" stroke="${col}" stroke-width="2" fill="${open?'white':col}"/>`;
const R=(x,y,w,h,col=blue)=>`<rect x="${x}" y="${y}" width="${w}" height="${h}" fill="${col}" fill-opacity=".2" stroke="${col}"/>`;
const P=(points,col=blue)=>`<polygon points="${points.map(p=>p.join(',')).join(' ')}" fill="${col}" fill-opacity=".2"/>`;
function G(ox,oy,w,h,xmin,xmax,ymin,ymax){
 const X=x=>ox+(x-xmin)/(xmax-xmin)*w,Y=y=>oy+h-(y-ymin)/(ymax-ymin)*h;
 const curve=(f,a=xmin,b=xmax,col=ink)=>`<polyline points="${Array.from({length:151},(_,i)=>{let x=a+(b-a)*i/150;return X(x)+','+Y(f(x))}).join(' ')}" fill="none" stroke="${col}" stroke-width="3"/>`;
 const shade=(f,a,b,col=blue)=>P([[X(a),Y(0)],...Array.from({length:151},(_,i)=>{let x=a+(b-a)*i/150;return [X(x),Y(f(x))]}),[X(b),Y(0)]],col);
 const axes=L(X(xmin),Y(0),X(xmax)+10,Y(0))+L(X(0),Y(ymin),X(0),Y(ymax)-8)+T(X(xmax)+15,Y(0)+5,'x',17)+T(X(0)-14,Y(ymax)-10,'y',17);
 return {X,Y,curve,shade,axes};
}
const defs=[];
function save(ch,id,title,body,foot){
 const name=`t1-c${String(ch).padStart(2,'0')}-fig-${String(id).padStart(2,'0')}`;
 const svg=`<svg xmlns="http://www.w3.org/2000/svg" width="800" height="490" viewBox="0 0 800 490"><title>${esc(title)}</title><rect width="800" height="490" fill="white"/><g font-family="Arial, sans-serif">${T(32,42,title,25)}${body}${T(32,463,foot,18)}</g></svg>`;
 fs.writeFileSync(path.join(out,name+'.svg'),svg);fs.writeFileSync(path.join(out,name+'.png'),new Resvg(svg,{fitTo:{mode:'width',value:1600}}).render().asPng());defs.push({ch,id,name,title});
}
let g,s;
// Absolute value as a distance, with open endpoints for a strict inequality.
s=L(85,250,715,250)+L(400,145,400,265,ink,'5 5')+L(220,250,580,250,blue);
for(const [x,label] of [[220,'a − r'],[400,'a'],[580,'a + r']])s+=C(x,250,blue,x!==400)+T(x,290,label,22,ink,'middle');
s+=T(400,115,'|x − a| < r',29,blue,'middle')+L(220,340,400,340)+L(400,340,580,340)+T(310,370,'distancia r',20,ink,'middle')+T(490,370,'distancia r',20,ink,'middle');
save(2,1,'Valor absoluto: pertenecer a un intervalo',s,'La desigualdad estricta excluye los dos extremos.');
g=G(100,95,580,290,0,2.1,0,2.1);s=g.axes+g.curve(x=>x*x,0,Math.sqrt(2.1),blue)+g.curve(x=>Math.sqrt(x),0,2.1,orange)+g.curve(x=>x,0,2.1,ink);
s+=C(g.X(.7),g.Y(.49),blue)+C(g.X(.49),g.Y(.7),orange)+L(g.X(.7),g.Y(.49),g.X(.49),g.Y(.7),green,'5 5')+T(395,95,'f(x) = x², x ≥ 0',20,blue)+T(475,340,'f⁻¹(x) = √x',20,orange)+T(350,260,'y = x',18);
save(3,1,'La inversa refleja la gráfica respecto de y = x',s,'Restringir x² a x ≥ 0 permite que la inversa sea una función.');
g=G(95,100,620,280,0,15,0,1.05);s=R(g.X(0),g.Y(.2),g.X(15)-g.X(0),g.Y(0)-g.Y(.2),blue)+g.axes;
for(let n=1;n<=15;n++)s+=C(g.X(n),g.Y(1/n),n>5?green:orange);
s+=L(g.X(5),g.Y(0),g.X(5),g.Y(1.02),ink,'5 5')+T(g.X(5),g.Y(0)+28,'N = 5',20,ink,'middle')+T(390,110,'aₙ = 1/n → 0',23)+T(410,g.Y(.2)-12,'ε = 1/5',20,blue);
save(4,1,'Convergencia: una cola dentro de la banda',s,'Para todo n > 5 se cumple |aₙ − 0| < 1/5.');
g=G(100,90,600,300,0,1.5,0,2.25);s=R(g.X(0),g.Y(1.5),g.X(1.5)-g.X(0),g.Y(.5)-g.Y(1.5),blue)+R(g.X(.8),g.Y(2.25),g.X(1.2)-g.X(.8),g.Y(0)-g.Y(2.25),orange)+g.axes+g.curve(x=>x*x);
s+=C(g.X(1),g.Y(1),green)+T(110,100,'f(x) = x²',20)+T(g.X(.8),g.Y(0)+27,'0.8',18,ink,'middle')+T(g.X(1.2),g.Y(0)+27,'1.2',18,ink,'middle')+T(435,88,'ε = 0.5; δ = 0.2',21);
save(5,1,'Límite: una ventana horizontal controla una banda',s,'Si 0 < |x − 1| < 0.2, entonces |x² − 1| < 0.5.');
let a=G(75,110,270,245,-1,1,-.2,1.4),b=G(455,110,270,245,-1,1,-.2,1.4);
s=T(75,83,'Continuidad',22,blue)+T(455,83,'Salto',22,orange)+a.axes+a.curve(x=>x*x,-1,1,blue)+C(a.X(0),a.Y(0),blue)+b.axes+L(b.X(-1),b.Y(0),b.X(0),b.Y(0),orange)+L(b.X(0),b.Y(1),b.X(1),b.Y(1),orange)+C(b.X(0),b.Y(0),orange,true)+C(b.X(0),b.Y(1),orange)+T(75,410,'f(x) = x²',22)+T(455,410,'g(x) = 0 si x < 0; 1 si x ≥ 0',18);
save(6,1,'Continuidad y salto: controlar el valor central',s,'En el salto, los límites laterales son distintos.');
g=G(100,95,600,290,0,1.8,-1.1,3.3);s=g.axes+g.curve(x=>x*x,0,1.8,ink)+g.curve(x=>2*x-1,0,1.8,green);
for(const [h,col] of [[.6,orange],[.2,blue]])s+=g.curve(x=>(2+h)*x-(1+h),.3,1.7,col)+C(g.X(1+h),g.Y((1+h)**2),col);
s+=C(g.X(1),g.Y(1),green)+T(110,82,'f(x) = x²',20)+T(380,110,'Secantes: pendientes 2.6 y 2.2',19)+T(395,420,'Tangente: pendiente 2',21,green);
save(7,1,'La tangente como límite de las secantes',s,'En x = 1, el cociente incremental es 2 + h.');
s='';for(const [x,w,t,col] of [[55,150,'x = 1',ink],[320,160,'u = x²',blue],[595,155,'v = u³',green]])s+=R(x,180,w,95,col)+T(x+w/2,236,t,24,col,'middle');
s+=L(205,227,310,227,blue)+T(257,160,'u′(1) = 2',20,blue,'middle')+L(480,227,585,227,green)+T(530,160,'v′(1) = 3',20,green,'middle')+T(400,365,'(v ∘ u)′(1) = 3 · 2 = 6',28,ink,'middle');
save(8,1,'Regla de la cadena: multiplicar cambios locales',s,'La composición v(u(x)) = x⁶ tiene derivada 6 en x = 1.');
g=G(100,100,580,280,0,2.1,0,2.1);s=g.axes+g.curve(x=>x*x,0,Math.sqrt(2.1),blue)+g.curve(x=>Math.sqrt(x),0,2.1,orange)+g.curve(x=>2*x-1,.5,1.5,blue)+g.curve(x=>.5*x+.5,0,2.1,orange)+C(g.X(1),g.Y(1),green)+T(420,97,'f′(1) = 2',22,blue)+T(420,405,'(f⁻¹)′(1) = 1/2',22,orange);
save(9,1,'Las pendientes de una función y su inversa',s,'Las pendientes son recíprocas donde la derivada no se anula.');
a=G(75,110,270,245,0,2,0,1.2);b=G(455,110,270,245,0,2,0,4.4);
s=T(75,82,'Rolle',22)+T(455,82,'Valor medio',22)+a.axes+a.curve(x=>x*(2-x))+a.curve(x=>1,.35,1.65,green)+C(a.X(1),a.Y(1),green)+b.axes+b.curve(x=>x*x)+b.curve(x=>2*x,0,2,orange)+b.curve(x=>2*x-1,.5,2,green)+C(b.X(1),b.Y(1),green)+T(75,407,'f(x) = x(2 − x); c = 1',19)+T(455,407,'f(x) = x²; c = 1',19);
save(10,1,'Tangentes horizontales y tangentes paralelas',s,'En [0,2], Rolle da pendiente 0 y el valor medio da pendiente 2.');
g=G(100,100,600,290,0,2,-1.1,4.4);s=g.axes+g.curve(x=>x*x)+g.curve(x=>2*x,0,2,orange)+g.curve(x=>2*x-1,0,2,green)+C(g.X(1),g.Y(1),green)+T(360,90,'Cuerda: y = 2x',20,orange)+T(405,420,'Tangente: y = 2x − 1',20,green);
save(11,1,'Convexidad: la curva entre cuerda y tangente',s,'Para 0 ≤ x ≤ 2: 2x − 1 ≤ x² ≤ 2x.');
g=G(100,100,600,285,-.6,.6,0,2.6);s=g.axes+g.curve(x=>1/(1-x),-.6,.6,ink)+g.curve(x=>1+x,-.6,.6,orange)+g.curve(x=>1+x+x*x,-.6,.6,blue)+C(g.X(0),g.Y(1),green)+T(420,105,'f(x) = 1/(1 − x)',20)+T(420,340,'T₁(x) = 1 + x',19,orange)+T(420,370,'T₂(x) = 1 + x + x²',19,blue);
save(12,1,'Taylor: mejorar el modelo local con más datos',s,'El dibujo sugiere la mejora; la fórmula del resto controla el error.');
g=G(100,95,600,290,0,2.2,-2.3,3.1);s=g.axes+g.curve(x=>x*x-2,0,2.2);
for(const [x,col] of [[2,orange],[1.5,blue]]){let next=x-(x*x-2)/(2*x);s+=g.curve(t=>2*x*(t-x)+x*x-2,next,2.15,col)+C(g.X(x),g.Y(x*x-2),col)+C(g.X(next),g.Y(0),col);}
s+=T(110,83,'f(x) = x² − 2',20)+T(400,420,'x₀ = 2 → x₁ = 3/2 → x₂ = 17/12',21,ink,'middle');
save(13,1,'Newton: la tangente determina el paso siguiente',s,'El método aproxima una raíz; la convergencia exige hipótesis.');
g=G(100,100,600,290,0,1.15,0,1.2);s=g.shade(x=>x*x,0,1,blue)+g.axes+g.curve(x=>x*x,0,1.08)+L(g.X(1),g.Y(0),g.X(1),g.Y(1),blue)+T(g.X(.68),g.Y(.2),'S_f',27,blue)+T(105,88,'f(x) = x² ≥ 0',22)+T(g.X(0),g.Y(0)+26,'a = 0',19,ink,'middle')+T(g.X(1),g.Y(0)+26,'b = 1',19,ink,'middle');
save(14,9,'La imagen clásica: el área bajo una curva',s,'La región sombreada motiva el problema; todavía no define la integral.');
s='';for(const [n,ox] of [[4,75],[8,455]]){g=G(ox,110,270,245,0,1,0,1.15);for(let k=1;k<=n;k++){let lo=((k-1)/n)**2,hi=(k/n)**2;s+=R(g.X((k-1)/n),g.Y(hi),270/n,g.Y(0)-g.Y(hi),orange)+R(g.X((k-1)/n),g.Y(lo),270/n,g.Y(0)-g.Y(lo),blue)}s+=g.axes+g.curve(x=>x*x)+T(ox,83,n+' piezas uniformes',21)+T(ox+135,413,'U − L = 1/'+n,22,ink,'middle');}
save(14,10,'Rectángulos que se ajustan a un borde curvo',s,'Para f(x) = x², la diferencia de estas dos sumas es 1/n.');
g=G(100,100,600,285,-1,1,-1.15,1.15);s=g.shade(x=>x*x*x,-1,0,orange)+g.shade(x=>x*x*x,0,1,blue)+g.axes+g.curve(x=>x*x*x,-1,1)+T(120,103,'f(x) = x³',21)+T(170,355,'Contribución negativa',19,orange)+T(445,155,'Contribución positiva',19,blue)+T(150,418,'La simetría permite cancelación de las contribuciones con signo.',19);
save(14,11,'Más allá del área positiva: contribuciones con signo',s,'El área geométrica total suma las dos regiones; la integral distingue signos.');
// A planar profile and circular sections of the corresponding cone.
a=G(75,115,270,235,0,1.1,0,1.2);s=T(75,84,'Perfil y radio',22)+a.axes+a.shade(x=>x,0,1,blue)+a.curve(x=>x,0,1,blue)+L(a.X(.7),a.Y(0),a.X(.7),a.Y(.7),orange)+T(a.X(.7)+10,a.Y(.35),'r = x',19,orange)+T(455,84,'Secciones perpendiculares al eje',20);
s+=L(455,275,725,275,ink);for(const x of [.25,.5,.75,1]){let cx=455+270*x,rad=95*x;s+=`<ellipse cx="${cx}" cy="275" rx="${18*x}" ry="${rad}" fill="${blue}" fill-opacity=".1" stroke="${blue}" stroke-width="2"/>`;}
s+=L(455,275,725,180,blue)+L(455,275,725,370,blue)+T(75,410,'y = x; 0 ≤ x ≤ 1',20)+T(475,410,'A(x) = πr² = πx²',22,blue);
save(20,1,'Volumen por secciones: del radio al área del disco',s,'Al girar el perfil alrededor del eje x, cada sección es un disco.');
fs.writeFileSync(path.resolve(__dirname,'../data/cpm-visual-audit-figures.json'),JSON.stringify(defs,null,2)+'\n');
for(let group=0;group<4;group++){let svg='<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="980">';for(let j=0;j<4;j++){const f=defs[group*4+j];const data=fs.readFileSync(path.join(out,f.name+'.png')).toString('base64');svg+=`<image x="${j%2*800}" y="${Math.floor(j/2)*490}" width="800" height="490" href="data:image/png;base64,${data}"/>`;}svg+='</svg>';fs.writeFileSync(path.resolve(__dirname,`../cpm-visual-preview-${group+1}.png`),new Resvg(svg).render().asPng());}
console.log('Generated sixteen figures for fourteen chapters.');
