import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { runInNewContext } from 'node:vm';

const script = readFileSync(new URL('../js/diofanto-triples.js', import.meta.url), 'utf8');
const html = readFileSync(new URL('../blog/el-metodo-de-diofanto-y-las-ternas-pitagoricas.qmd', import.meta.url), 'utf8');
const keys = [...html.matchAll(/\sdata-([a-z-]+)(?=[\s=>])/g)].map(m => m[1]);

function createWidget() {
  const nodes = Object.fromEntries(keys.map(key => [key, {
    value: key === 'p' ? '2' : key === 'q' ? '1' : undefined,
    textContent: '', hidden: false, attributes: {}, listeners: {},
    setAttribute(name,value) { this.attributes[name] = String(value); },
    addEventListener(name,fn) { (this.listeners[name] ??= []).push(fn); },
    fire(name) { for (const fn of this.listeners[name] ?? []) fn(); }
  }]));
  const root = { dataset: {}, querySelector(selector) {
    const match = selector.match(/^\[data-([a-z-]+)\]$/);
    return match ? (nodes[match[1]] ?? null) : null;
  }};
  return { root, nodes };
}

function gcd(a,b) { while(b) [a,b] = [b,a % b]; return a; }

test('HTML exposes every selector required by the standalone script', () => {
  const required = script.match(/const outputKeys = \[([\s\S]*?)\];/)[1].match(/'[^']+'/g).map(v => v.slice(1,-1));
  for(const key of ['p','q',...required]) assert.ok(keys.includes(key), `Missing data-${key}`);
});

test('initializes each instance, clamps q and checks every parameter pair', () => {
  const first = createWidget();
  const second = createWidget();
  const listeners = {};
  const document = { readyState: 'complete', querySelectorAll: () => [first.root,second.root],
    addEventListener(name,fn) { listeners[name] = fn; } };
  runInNewContext(script,{document});
  for(const {root,nodes} of [first,second]) {
    assert.equal(root.dataset.diofantoInitialized, 'true');
    assert.equal(nodes.fallback.hidden,true);
    assert.equal(nodes.identity.textContent,'4² + 3² = 5²');
    assert.equal(nodes.q.max,'1');
    assert.equal(nodes.p.listeners.input.length,1);
    for(let p=2;p<=20;p++) {
      nodes.p.value=String(p); nodes.p.fire('input');
      assert.equal(nodes.q.max,String(p-1));
      for(let q=1;q<p;q++) {
        nodes.q.value=String(q); nodes.q.fire('input');
        const a=2*p*q,b=p*p-q*q,c=p*p+q*q;
        assert.equal(nodes.identity.textContent,`${a}² + ${b}² = ${c}²`);
        assert.equal(nodes.status.textContent.startsWith('Terna primitiva'),gcd(gcd(a,b),c)===1);
        assert.equal(nodes.triangle.attributes['aria-label'],`Triángulo rectángulo de catetos ${a} y ${b} e hipotenusa ${c}`);
      }
    }
    nodes.p.value='2';nodes.p.fire('input');
    assert.equal(nodes.q.value,'1');
  }
  listeners.pageshow();
  assert.equal(first.nodes.p.listeners.input.length,1,'Must not attach duplicate listeners');
});
