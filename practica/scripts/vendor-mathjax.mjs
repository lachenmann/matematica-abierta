// SPDX-License-Identifier: GPL-3.0-or-later
// Prepara una copia local e inmutable de la distribución de MathJax 4.0.0.
// El código copiado conserva la licencia Apache-2.0 de MathJax.
import { cp, mkdir, readFile, rm, stat } from 'node:fs/promises';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const practica = fileURLToPath(new URL('../', import.meta.url));
const source = resolve(practica, 'node_modules', 'mathjax');
const target = resolve(practica, 'vendor', 'mathjax');

const packageFile = resolve(source, 'package.json');
const metadata = JSON.parse(await readFile(packageFile, 'utf8'));

if (metadata.name !== 'mathjax' || metadata.version !== '4.0.0') {
  throw new Error(`Se esperaba mathjax@4.0.0 y se obtuvo ${metadata.name}@${metadata.version}`);
}
if (metadata.license !== 'Apache-2.0') {
  throw new Error(`Licencia de MathJax inesperada: ${metadata.license}`);
}

await stat(resolve(source, 'tex-chtml.js'));
await stat(resolve(source, 'LICENSE'));
await rm(target, { recursive: true, force: true });
await mkdir(dirname(target), { recursive: true });
await cp(source, target, { recursive: true, dereference: true });

console.log('MathJax 4.0.0 preparado en practica/vendor/mathjax (Apache-2.0).');
