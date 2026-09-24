import test from 'node:test';
import assert from 'node:assert/strict';
import { renderRating } from '../rating-panel.mjs';

class FakeNode {
  constructor(tag) {
    this.tagName = tag;
    this.dataset = {};
    this.children = [];
    this.className = '';
    this.open = false;
    this.ownText = '';
  }
  set textContent(value) { this.ownText = String(value); this.children = []; }
  get textContent() { return this.ownText + this.children.map(child => typeof child === 'string' ? child : child.textContent).join(''); }
  append(...children) { this.children.push(...children); }
  replaceChildren(...children) { this.ownText = ''; this.children = [...children]; }
  setAttribute(name, value) { this[name] = String(value); }
  querySelectorAll(selector) {
    const descendants = this.children.filter(child => child instanceof FakeNode).flatMap(child => [child, ...child.querySelectorAll(selector)]);
    if (selector === 'details[open]') return descendants.filter(node => node.tagName === 'details' && node.open);
    return descendants;
  }
}

function withDocument(check) {
  const prior = globalThis.document;
  const nodes = new Map();
  globalThis.document = {
    getElementById(id) {
      if (!nodes.has(id)) nodes.set(id, new FakeNode('div'));
      return nodes.get(id);
    },
    createElement: tag => new FakeNode(tag),
    createElementNS: (_namespace, tag) => new FakeNode(tag)
  };
  try { return check(nodes); }
  finally {
    if (prior === undefined) delete globalThis.document;
    else globalThis.document = prior;
  }
}

const deltas = node => node.querySelectorAll('*').filter(child => child.className?.split(' ').includes('rating-delta'));

 test('Marcador: +n verde y -n rojo, en cabecera, área e historial sin alterar datos', () => withDocument(nodes => {
  const progress = {
    ratings: { algebra: 1183, calculo: 1214 },
    history: [
      { area: 'algebra', mode: 'challenge', title: 'Ecuación', ratingBefore: 1200, ratingAfter: 1183, delta: -17 },
      { area: 'calculo', mode: 'challenge', title: 'Derivada', ratingBefore: 1200, ratingAfter: 1214, delta: 14 }
    ]
  };
  const before = structuredClone(progress);
  renderRating(progress, 'algebra');
  const header = deltas(nodes.get('rating-current'));
  assert.equal(header.length, 1);
  assert.equal(header[0].textContent, '-17');
  assert.match(header[0].className, /rating-down/);
  const changes = deltas(nodes.get('rating-list'));
  assert.deepEqual(changes.map(node => node.textContent), ['-17', '-17', '+14', '+14']);
  assert.deepEqual(changes.map(node => node.className.includes('rating-up')), [false, false, true, true]);
  assert.ok(changes.slice(0, 2).every(node => node.className.includes('rating-down')));
  assert.deepEqual(progress, before);
}));

 test('Marcador: delta cero no se presenta como ganancia ni pérdida', () => withDocument(nodes => {
  renderRating({ ratings: { algebra: 1200 }, history: [
    { area: 'algebra', mode: 'challenge', title: 'Empate', ratingBefore: 1200, ratingAfter: 1200, delta: 0 }
  ] }, 'algebra');
  const header = deltas(nodes.get('rating-current'));
  assert.equal(header[0].textContent, '0');
  assert.match(header[0].className, /rating-neutral/);
}));
