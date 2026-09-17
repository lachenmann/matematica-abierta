import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { runInNewContext } from 'node:vm';

// Minimal deterministic DOM harness: executes the actual browser script, not a copied formula.
class Element {
  constructor() { this.value=''; this.textContent=''; this.style={}; this.dataset={}; this.attrs={}; this.children=[]; this.handlers={}; this.checked=false; this.hidden=false; this.tabIndex=0; }
  addEventListener(type,fn) { (this.handlers[type]??=[]).push(fn); }
  emit(type,extra={}) { for(const fn of this.handlers[type]??[]) fn({target:this,key:'',pointerId:1,...extra,preventDefault(){}}); }
  setAttribute(name,value) { this.attrs[name]=String(value); }
  getAttribute(name) { return this.attrs[name]??null; }
  appendChild(child) { this.children.push(child); return child; }
  replaceChildren(...children) { this.children=children; }
  focus() { this.focused=true; }
  getScreenCTM(){return {inverse(){return {};}};}
  setPointerCapture(){this.captured=true;}
  hasPointerCapture(){return Boolean(this.captured);}
  releasePointerCapture(){this.captured=false;}
}
const ids=new Map();
const get=id=>{if(!ids.has(id))ids.set(id,new Element());return ids.get(id);};
const modes=new Element();
const prediction=Array.from({length:3},()=>new Element());
const toProof=Array.from({length:2},()=>new Element());
const doc={getElementById:get,createElementNS:()=>new Element(),querySelector:q=>q==='.modes'?modes:null,querySelectorAll:q=>q==='[name=prediction]'?prediction:q==='.to-proof'?toProof:[]};
const script=readFileSync(new URL('../teoria/resultados/interactive/desigualdad-triangular.js',import.meta.url),'utf8');
runInNewContext(script,{document:doc,Intl,Math,Number,DOMPoint:class{constructor(x,y){this.x=x;this.y=y;}matrixTransform(){return this;}}},{filename:'desigualdad-triangular.js'});
function preset(name){get('plane-preset').value=name;get('plane-preset').emit('change');return [get('plane-d').textContent,get('plane-r').textContent,get('plane-gap').textContent];}
function real(name){get('real-preset').value=name;get('real-preset').emit('change');return [get('real-d').textContent,get('real-r').textContent,get('real-gap').textContent];}

test('M01–M06: six geometric examples and certified equality',()=>{
  assert.deepEqual(preset('triangle'),['5','7','2']);
  assert.deepEqual(preset('inside'),['5','5','0']);
  assert.match(get('plane-message').textContent,/Igualdad certificada/);
  assert.deepEqual(preset('outside'),['5','9','4']);
  assert.match(get('plane-message').textContent,/retroceso/);
  assert.deepEqual(preset('endpoint'),['5','5','0']);
  assert.deepEqual(preset('same-ends'),['0','2','2']);
  assert.deepEqual(preset('same-all'),['0','0','0']);
});
test('M07–M09: signs, cancellation and zero in real line',()=>{
  assert.deepEqual(real('same'),['5','5','0']);
  assert.deepEqual(real('cancel'),['2','8','6']);
  assert.deepEqual(real('zero'),['4','4','0']);
  assert.deepEqual(real('negative'),['5','5','0']);
  assert.deepEqual(real('opposite'),['0','2','2']);
});
test('U01: invalid/empty numeric input does not alter geometry',()=>{
  preset('inside');get('bx').value='';get('bx').emit('change');
  assert.equal(get('bx').getAttribute('aria-invalid'),'true');
  assert.equal(get('plane-input-error').hidden,false);
  assert.equal(get('plane-r').textContent,'5');
  get('bx').value='7';get('bx').emit('change');
  assert.equal(get('plane-r').textContent,'9');
  assert.equal(get('plane-input-error').hidden,true);
  get('plane-reset').emit('click');
  assert.deepEqual([get('plane-d').textContent,get('plane-r').textContent,get('plane-gap').textContent],['5','7','2']);
});
test('U02: keyboard-accessible slider and navigation update state',()=>{
  get('tab-real').emit('click');
  assert.equal(get('tab-real').getAttribute('aria-selected'),'true');
  real('same');get('real-y').value='-3';get('real-y').emit('input');
  assert.deepEqual([get('real-d').textContent,get('real-r').textContent,get('real-gap').textContent],['1','5','4']);
  modes.emit('keydown',{key:'ArrowRight'});
  assert.equal(get('tab-proof').getAttribute('aria-selected'),'true');
});
test('P01–P03: seven ordered proof stages and generality notice',()=>{
  get('proof-reset').emit('click');
  assert.equal(get('proof-count').textContent,'Paso 0 de 7');
  for(let i=1;i<=7;i++){
    get('proof-next').emit('click');
    assert.equal(get('proof-count').textContent,`Paso ${i} de 7`);
    assert.ok(get('proof-reason').textContent.length>20);
  }
  assert.match(get('proof-content').textContent,/cualesquiera A, B y C/);
  get('proof-next').emit('click');
  assert.match(get('proof-reason').textContent,/Mover puntos sólo permitió explorar ejemplos/);
  get('proof-prev').emit('click');
  assert.equal(get('proof-count').textContent,'Paso 6 de 7');
});
test('M10: exact small-grid geometry satisfies numeric triangular bound',()=>{
  for(let ax=-2;ax<=2;ax++)for(let ay=-2;ay<=2;ay++)for(let bx=-2;bx<=2;bx++)for(let by=-2;by<=2;by++)for(let cx=-2;cx<=2;cx++)for(let cy=-2;cy<=2;cy++){
    const d=Math.hypot(cx-ax,cy-ay),r=Math.hypot(bx-ax,by-ay)+Math.hypot(cx-bx,cy-by);
    assert.ok(d<=r+1e-12*Math.max(1,d,r));
  }
});
