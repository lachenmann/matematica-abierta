(() => {
'use strict';
const $ = id => document.getElementById(id);
const gcd=(a,b)=>{a=Math.abs(a);b=Math.abs(b);while(b){[a,b]=[b,a%b];}return a;};
const frac=(n,d)=>{const g=gcd(n,d);return g===0?'0':d/g===1?String(n/g):`${n/g}/${d/g}`;};
const inputs={p:$('p'),q:$('q'),radius:$('radius'),multiple:$('multiple')};
let stage='geometry';
const read=()=>{
  const vals={};for(const [key,node] of Object.entries(inputs)){
    const raw=node.value.trim();if(!/^\d+$/.test(raw))return {error:`${key}: introduce un entero positivo.`};
    vals[key]=Number(raw);if(!Number.isSafeInteger(vals[key]))return {error:`${key}: entero fuera de rango.`};
  }
  if(vals.p<2||vals.p>30||vals.q<1||vals.q>=vals.p)return {error:'Se requiere 2 ≤ p ≤ 30 y 1 ≤ q < p.'};
  if(vals.radius<1||vals.radius>12||vals.multiple<1||vals.multiple>8)return {error:'Radio entre 1 y 12; factor k entre 1 y 8.'};
  return vals;
};
function calculate({p,q,radius,multiple:k}){
  const d=p*p+q*q,a=2*p*q,b=p*p-q*q;
  const X=2*radius*p*q,Y=radius*b;
  const A=k*a,B=k*b,C=k*d;
  return {p,q,radius,k,d,a,b,A,B,C,X,Y,primitive:gcd(gcd(A,B),C)===1,parameterGcd:gcd(p,q),tripleGcd:gcd(gcd(A,B),C)};
}
function circle(m){
  const {p,q,radius:c,d,X,Y}=m;
  const px=210+145*(X/d)/c,py=175-145*(Y/d)/c;
  $('chord').setAttribute('d',`M210 320 L${px} ${py}`);
  $('found').setAttribute('cx',px);$('found').setAttribute('cy',py);
  $('found-label').setAttribute('x',Math.min(390,px+10));$('found-label').setAttribute('y',py-9);
  $('circle-desc').textContent=`Circunferencia de radio ${c}. Recta de pendiente ${p}/${q} desde (0, -${c}) hasta (${frac(X,d)}, ${frac(Y,d)}).`;
  $('geom-line').textContent=`y = (${frac(p,q)})x − ${c}`;
  $('known-coord').textContent=`(0, −${c})`; $('slope').textContent=`m = ${frac(p,q)}`;
  $('new-point').textContent=`(${frac(X,d)}, ${frac(Y,d)})`;
  $('geom-check').textContent=`(${frac(X,d)})² + (${frac(Y,d)})² = ${c*c}`;
  $('derivation').textContent=`x[(1 + (${p}/${q})²)x − 2·(${p}/${q})·${c}] = 0. La raíz nueva es x = ${frac(X,d)}; al sustituir en la recta, y = ${frac(Y,d)}. Multiplicando: ${X}² + ${Y}² = ${c*c}·${d}².`;
}
function triangle(m){
  const {p,q,k,A,B,C,primitive,parameterGcd,tripleGcd}=m;
  const s=235/Math.max(A,B),w=A*s,h=B*s,x=85,y=255;
  $('triangle-shape').setAttribute('points',`${x},${y} ${x+w},${y} ${x},${y-h}`);
  const r=Math.min(16,w/4,h/4);
  $('right-angle').setAttribute('points',`${x},${y-r} ${x+r},${y-r} ${x+r},${y}`);
  $('a-label').setAttribute('x',x+w/2);$('a-label').textContent=A;
  $('b-label').setAttribute('y',y-h/2);$('b-label').textContent=B;
  $('c-label').setAttribute('x',x+w/2+14);$('c-label').setAttribute('y',y-h/2-12);$('c-label').textContent=C;
  $('tri-desc').textContent=`Triángulo a escala con catetos ${A} y ${B} e hipotenusa ${C}.`;
  $('triple-identity').textContent=`${A}² + ${B}² = ${C}²`;
  $('triple-params').textContent=`p=${p}, q=${q}, k=${k}`;
  $('param-gcd').textContent=parameterGcd;
  $('parity').textContent=(p-q)%2?'Distinta':'Igual (ambos impares o pares)';
  $('triple-gcd').textContent=tripleGcd;
  $('primitive-tag').textContent=primitive?'Terna primitiva':'Terna no primitiva';
  $('primitive-tag').className=`tag${primitive?'':' warn'}`;
  const failures=[];
  if(parameterGcd!==1)failures.push(`mcd(p,q)=${parameterGcd}, por lo que los parámetros comparten un factor`);
  if((p-q)%2===0)failures.push('p y q tienen la misma paridad');
  if(k!==1)failures.push(`k=${k} multiplica los tres lados`);
  $('reasoning').textContent=primitive?'Los parámetros son coprimos y de distinta paridad, y k=1. Por el criterio demostrado en el artículo, la terna es primitiva.':`No es primitiva: ${failures.join('; ')}. El mcd efectivo de los tres lados es ${tripleGcd}.`;
}
function refresh(){
  const values=read();$('params-error').textContent=values.error||'';
  if(values.error){$('check-prediction').disabled=true;return;}
  $('check-prediction').disabled=false;
  const m=calculate(values);circle(m);triangle(m);
  $('feedback').textContent='';$('feedback').className='feedback';
  document.querySelectorAll('input[name=prediction]').forEach(el=>el.checked=false);
}
function switchStage(to){
  stage=to;document.body.dataset.stage=to;
  for(const name of ['geometry','triples']){
    $(`tab-${name}`).setAttribute('aria-selected',String(to===name));
    $(name).classList.toggle('hidden',to!==name);
    $(`tab-${name}`).tabIndex=to===name?0:-1;
  }
  $('yes-label').textContent=to==='geometry'?'Sí, ambas enteras':'Sí, primitiva';
  $('no-label').textContent=to==='geometry'?'No, alguna no es entera':'No primitiva';
  $('challenge').textContent=to==='geometry'?'¿La segunda intersección tiene ambas coordenadas enteras? Predice y comprueba.':'¿La terna construida con los valores introducidos es primitiva? Selecciona «Sí» o «No» y comprueba.';
  $('feedback').textContent='';document.querySelectorAll('input[name=prediction]').forEach(el=>el.checked=false);
}
Object.values(inputs).forEach(el=>el.addEventListener('input',refresh));
document.querySelectorAll('[data-preset]').forEach(button=>button.addEventListener('click',()=>{const [p,q]=button.dataset.preset.split(',');inputs.p.value=p;inputs.q.value=q;refresh();}));
$('reset').addEventListener('click',()=>{inputs.p.value=2;inputs.q.value=1;inputs.radius.value=4;inputs.multiple.value=1;switchStage('geometry');refresh();});
document.querySelectorAll('[data-tab]').forEach(button=>{
 button.addEventListener('click',()=>switchStage(button.dataset.tab));
 button.addEventListener('keydown',event=>{
  if(!['ArrowRight','ArrowLeft','Home','End'].includes(event.key))return;
  event.preventDefault();const next=(event.key==='ArrowRight'||event.key==='End')?'triples':'geometry';
  switchStage(next);$(`tab-${next}`).focus();
 });
});
$('check-prediction').addEventListener('click',()=>{
 const choice=document.querySelector('input[name=prediction]:checked');const feedback=$('feedback');
 if(!choice){feedback.textContent='Selecciona una predicción antes de comprobar.';feedback.className='feedback bad';return;}
 const m=calculate(read());const correct=stage==='geometry'?m.X%m.d===0&&m.Y%m.d===0:m.primitive;
 const success=(choice.value==='yes')===correct;
 feedback.textContent=stage==='geometry'?(success?'Correcto. ':'Revisa tu predicción. ')+`El punto (${frac(m.X,m.d)}, ${frac(m.Y,m.d)}) tiene ${correct?'dos coordenadas enteras':'al menos una coordenada no entera'}. Que sean racionales no significa que deban ser enteras.`:(success?'Correcto. ':'Revisa el mcd y la paridad. ')+`mcd(${m.A}, ${m.B}, ${m.C}) = ${m.tripleGcd}. ${correct?'La terna es primitiva.':'La terna no es primitiva.'}`;
 feedback.className=`feedback ${success?'good':'bad'}`;
});
refresh();switchStage('geometry');
})();
