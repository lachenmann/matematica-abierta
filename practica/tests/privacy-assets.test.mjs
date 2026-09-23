import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync, readdirSync, existsSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { resolve } from 'node:path';

const root = fileURLToPath(new URL('../', import.meta.url));
const html = readFileSync(resolve(root, 'index.html'), 'utf8');

test('Aviso visible confirma datos locales y MathJax servido por el mismo origen', () => {
  assert.match(html, /class="privacy-disclosure"/);
  assert.match(html, /Las respuestas, el historial y el Elo se guardan en este navegador/);
  assert.match(html, /no los transmite/);
  assert.match(html, /MathJax se sirve desde la misma copia de la aplicación/);
  assert.match(html, /src="vendor\/mathjax\/tex-chtml\.js"/);
  assert.doesNotMatch(html, /cdn\.jsdelivr\.net|www\.jsdelivr\.com/);
});

test('Rutas estáticas resuelven y la dependencia generada está declarada', () => {
  for (const [, localPath] of html.matchAll(/(?:href|src)="([^."#:][^"#]*|\.{1,2}\/[^"#]*)"/g)) {
    if (/^(?:https?:|data:|mailto:)/.test(localPath)) continue;
    if (localPath === '../index.html') {
      assert.ok(existsSync(resolve(root, '../index.qmd')), 'Falta la fuente de la portada que Quarto renderiza como index.html');
      continue;
    }
    if (localPath === 'vendor/mathjax/tex-chtml.js') {
      assert.ok(existsSync(resolve(root, 'package.json')), 'Falta package.json para preparar MathJax');
      assert.ok(existsSync(resolve(root, 'scripts/vendor-mathjax.mjs')), 'Falta el paso reproducible de MathJax');
      assert.ok(existsSync(resolve(root, 'vendor/README.md')), 'Falta documentación del artefacto local de MathJax');
      continue;
    }
    assert.ok(existsSync(resolve(root, localPath)), `Recurso local ausente: ${localPath}`);
  }
});

test('MathJax queda fijado en 4.0.0 y no ejecuta scripts de instalación propios', () => {
  const pkg = JSON.parse(readFileSync(resolve(root, 'package.json'), 'utf8'));
  assert.equal(pkg.dependencies.mathjax, '4.0.0');
  assert.equal(pkg.overrides['@mathjax/mathjax-newcm-font'], '4.0.0');
  const vendor = readFileSync(resolve(root, 'scripts/vendor-mathjax.mjs'), 'utf8');
  assert.match(vendor, /metadata\.version !== '4\.0\.0'/);
  assert.match(vendor, /metadata\.license !== 'Apache-2\.0'/);
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
