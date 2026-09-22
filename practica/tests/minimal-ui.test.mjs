import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';

const html = readFileSync(new URL('../index.html', import.meta.url), 'utf8');
const css = readFileSync(new URL('../minimal-ui.css', import.meta.url), 'utf8');

function tagWithId(id) {
  const match = html.match(new RegExp(`<([a-z]+)\\b[^>]*\\bid="${id}"[^>]*>`, 'i'));
  assert.ok(match, `Falta el elemento ${id}`);
  return match[0];
}

test('La interfaz carga sus estilos al final y conserva enunciado, respuesta, MathJax e historial', () => {
  assert.ok(html.indexOf('href="minimal-ui.css"') > html.indexOf('href="attempt-flow.css"'));
  for (const id of ['prompt', 'question', 'submit', 'retry', 'give-up', 'next', 'history-toggle', 'history-panel', 'feedback']) tagWithId(id);
  assert.match(html, /mathjax@4\.0\.0\/tex-chtml\.js/);
});

test('Elo, política de evaluación y planilla están disponibles bajo controles desplegables', () => {
  assert.match(tagWithId('rating-details'), /^<details\b/);
  assert.match(tagWithId('elo-rules'), /^<details\b/);
  assert.match(tagWithId('trace-disclosure'), /^<details\b/);
  assert.doesNotMatch(tagWithId('trace-disclosure'), /\sopen(?:\s|>)/);
  assert.ok(html.indexOf('id="rating-list"') < html.indexOf('Elo personal y experimental'));
  assert.match(html, /un error inicial cuenta como fallo/);
  assert.match(html, /id="review-return"/);
});

test('La planilla tiene un solo título y sigue indicando el número de pasos', () => {
  assert.equal((html.match(/id="trace-title"/g) ?? []).length, 1);
  assert.equal((html.match(/id="trace-count"/g) ?? []).length, 1);
  assert.match(html, /<aside\b[^>]*aria-labelledby="trace-title"/);
  assert.match(html, /<summary class="trace-toggle">[\s\S]*?id="trace-title"[\s\S]*?id="trace-count"[\s\S]*?<\/summary>/);
});

test('El tratamiento móvil prioriza el ejercicio y no oculta las acciones ni la matemática', () => {
  assert.match(css, /@media\s*\(max-width:\s*790px\)/);
  assert.match(css, /\.intro\s*\{[^}]*clip-path:\s*inset\(50%\)/);
  assert.match(css, /\.workspace-grid\s*\{[^}]*flex-direction:\s*column/);
  assert.doesNotMatch(css, /(?:\.exercise|\.question|\.actions|#submit|#feedback)\s*\{[^}]*display:\s*none/);
  assert.match(css, /#elo-rules\s*>\s*summary/);
});
