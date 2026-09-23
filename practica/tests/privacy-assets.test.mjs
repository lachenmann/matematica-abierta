import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync, readdirSync, existsSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { resolve, dirname } from 'node:path';

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

test('Rutas estáticas del prototipo resuelven a archivos del repositorio', () => {
  for (const [, localPath] of html.matchAll(/(?:href|src)="([^."#:][^"#]*|\.{1,2}\/[^"#]*)"/g)) {
    if (/^(?:https?:|data:|mailto:)/.test(localPath)) continue;
    assert.ok(existsSync(resolve(root, localPath)), `Recurso local ausente: ${localPath}`);
  }
  assert.ok(existsSync(resolve(root, '../index.qmd')), 'La portada canónica del sitio debe existir');
});

test('Los módulos de la aplicación no contienen llamadas explícitas de red', () => {
  for (const file of readdirSync(root).filter(name => name.endsWith('.mjs'))) {
    const code = readFileSync(resolve(root, file), 'utf8');
    assert.doesNotMatch(code, /\b(?:fetch\s*\(|XMLHttpRequest\b|WebSocket\b|EventSource\b|sendBeacon\s*\()/,
      `Revisar aviso de privacidad antes de agregar comunicaciones: ${file}`);
  }
});
