import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';

const html = readFileSync(new URL('../index.html', import.meta.url), 'utf8');
const css = readFileSync(new URL('../minimal-ui.css', import.meta.url), 'utf8');
const developmentCss = readFileSync(new URL('../development.css', import.meta.url), 'utf8');

function tagWithId(id) {
  const match = html.match(new RegExp(`<([a-z]+)\\b[^>]*\\bid="${id}"[^>]*>`, 'i'));
  assert.ok(match, `Falta el elemento ${id}`);
  return match[0];
}

test('La interfaz carga los estilos y conserva enunciado, respuesta, MathJax e historial', () => {
  assert.ok(html.indexOf('href="minimal-ui.css"') > html.indexOf('href="attempt-flow.css"'));
  assert.ok(html.indexOf('href="development.css"') > html.indexOf('href="minimal-ui.css"'));
  for (const id of ['prompt', 'question', 'submit', 'retry', 'give-up', 'next', 'history-toggle', 'history-panel', 'feedback']) tagWithId(id);
  assert.match(html, /src="vendor\\/mathjax\\/tex-chtml\\.js"/);
  assert.doesNotMatch(html, /cdn\\.jsdelivr\\.net/);
});

test('Elo y política permanecen plegados; el desarrollo matemático se muestra por defecto', () => {
  assert.match(tagWithId('rating-details'), /^<details\b/);
  assert.match(tagWithId('elo-rules'), /^<details\b/);
  assert.match(tagWithId('trace-disclosure'), /^<details\b/);
  assert.match(tagWithId('trace-disclosure'), /\sopen(?:\s|>)/);
  assert.ok(html.indexOf('id="rating-list"') < html.indexOf('Elo personal y experimental'));
  assert.match(html, /un error inicial cuenta como fallo/);
  assert.match(html, /id="review-return"/);
});

test('Un solo desarrollo integra ecuación, pasos y consulta antes de la decisión', () => {
  for (const id of ['trace-title', 'trace-count', 'trace', 'review']) {
    assert.equal((html.match(new RegExp(`id="${id}"`, 'g')) ?? []).length, 1);
  }
  const prompt = html.indexOf('id="prompt"');
  const development = html.indexOf('class="worked-development"');
  const trace = html.indexOf('id="trace"');
  const review = html.indexOf('id="review"');
  const divider = html.indexOf('class="decision-divider"');
  const question = html.indexOf('id="question"');
  assert.ok(prompt < development && development < trace && trace < review && review < divider && divider < question);
  assert.doesNotMatch(html, /<aside\b[^>]*class="card tracebox"/);
  assert.match(html, /<summary class="trace-toggle">[\s\S]*?id="trace-title"[\s\S]*?id="trace-count"[\s\S]*?<\/summary>/);
  assert.match(developmentCss, /#trace-disclosure:has\(#trace > li\.muted\)\s*\{\s*display:\s*none/);
  assert.match(developmentCss, /\.workspace-grid\s*\{\s*display:\s*block/);
});

test('El tratamiento móvil conserva el ejercicio, desarrollo, controles y fórmulas legibles', () => {
  assert.match(css, /@media\s*\(max-width:\s*790px\)/);
  assert.match(css, /\.intro\s*\{[^}]*clip-path:\s*inset\(50%\)/);
  assert.match(css, /\.workspace-grid\s*\{[^}]*flex-direction:\s*column/);
  assert.match(developmentCss, /@media\s*\(max-width:\s*430px\)/);
  assert.match(developmentCss, /\.trace-summary\s*\{[^}]*overflow-x:\s*auto/);
  assert.doesNotMatch(developmentCss, /(?:\.exercise|\.question|\.actions|#submit|#feedback)\s*\{[^}]*display:\s*none/);
  assert.match(css, /#elo-rules\s*>\s*summary/);
});
