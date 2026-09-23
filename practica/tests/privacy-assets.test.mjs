import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync, readdirSync, existsSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { resolve } from 'node:path';

const root = fileURLToPath(new URL('../', import.meta.url));
const html = readFileSync(resolve(root, 'index.html'), 'utf8');

test('Aviso visible distingue progreso local de conexiones técnicas al CDN', () => {
  assert.match(html, /class="privacy-disclosure"/);
  assert.match(html, /Las respuestas, el historial y el Elo se guardan en este navegador/);
  assert.match(html, /jsDelivr, que puede recibir datos técnicos de conexión/);
  assert.match(html, /https:\/\/www\.jsdelivr\.com\/terms\/privacy-policy/);
  assert.match(html, /target="_blank" rel="noopener noreferrer"/);
  assert.match(html, /mathjax@4\.0\.0\/tex-chtml\.js" referrerpolicy="no-referrer"/);
});

test('Rutas estáticas resuelven y la portada es un derivado de Quarto', () => {
  for (const [, localPath] of html.matchAll(/(?:href|src)="([^."#:][^"#]*|\.{1,2}\/[^"#]*)"/g)) {
    if (/^(?:https?:|data:|mailto:)/.test(localPath)) continue;
    if (localPath === '../index.html') {
      assert.ok(existsSync(resolve(root, '../index.qmd')), 'Falta la fuente de la portada que Quarto renderiza como index.html');
      continue;
    }
    assert.ok(existsSync(resolve(root, localPath)), `Recurso local ausente: ${localPath}`);
  }
});

test('Los módulos de la aplicación no contienen llamadas explícitas de red', () => {
  for (const file of readdirSync(root).filter(name => name.endsWith('.mjs'))) {
    const code = readFileSync(resolve(root, file), 'utf8');
    assert.doesNotMatch(code, /\b(?:fetch\s*\(|XMLHttpRequest\b|WebSocket\b|EventSource\b|sendBeacon\s*\()/,
      `Revisar aviso de privacidad antes de agregar comunicaciones: ${file}`);
  }
});


test('La distribución incluye las licencias GNU declaradas', () => {
  const rootDir = resolve(root, '..');
  const gpl = readFileSync(resolve(rootDir, 'COPYING.GPL'), 'utf8');
  const general = readFileSync(resolve(rootDir, 'LICENSE'), 'utf8');
  const local = readFileSync(resolve(root, 'LICENSE.md'), 'utf8');
  assert.match(gpl, /^GNU GENERAL PUBLIC LICENSE\nVersion 3, 29 June 2007/);
  assert.match(gpl, /END OF TERMS AND CONDITIONS/);
  assert.match(general, /GPL-3\.0-or-later/);
  assert.match(local, /GPL-3\.0-or-later/);
  assert.match(local, /COPYING\.GPL/);
});
