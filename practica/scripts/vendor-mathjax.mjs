// SPDX-License-Identifier: GPL-3.0-or-later
// Prepara copias locales e inmutables de MathJax 4.0.0 y su fuente NewCM.
// El código y las fuentes copiadas conservan sus licencias de terceros.
import { cp, mkdir, readFile, rm, stat } from 'node:fs/promises';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const practica = fileURLToPath(new URL('../', import.meta.url));

async function verifyPackage(source, expectedName) {
  const metadata = JSON.parse(await readFile(resolve(source, 'package.json'), 'utf8'));
  if (metadata.name !== expectedName || metadata.version !== '4.0.0') {
    throw new Error(`Se esperaba ${expectedName}@4.0.0 y se obtuvo ${metadata.name}@${metadata.version}`);
  }
  if (metadata.license !== 'Apache-2.0') {
    throw new Error(`Licencia inesperada para ${expectedName}: ${metadata.license}`);
  }
  await stat(resolve(source, 'LICENSE'));
}

async function replaceTree(source, target) {
  await rm(target, { recursive: true, force: true });
  await mkdir(dirname(target), { recursive: true });
  await cp(source, target, { recursive: true, dereference: true });
}

const mathjaxSource = resolve(practica, 'node_modules', 'mathjax');
const fontSource = resolve(practica, 'node_modules', '@mathjax', 'mathjax-newcm-font');
const mathjaxTarget = resolve(practica, 'vendor', 'mathjax');
const fontTarget = resolve(practica, 'vendor', 'mathjax-newcm-font');

await verifyPackage(mathjaxSource, 'mathjax');
await verifyPackage(fontSource, '@mathjax/mathjax-newcm-font');
await stat(resolve(mathjaxSource, 'tex-chtml.js'));
await stat(resolve(fontSource, 'chtml', 'woff2'));

await replaceTree(mathjaxSource, mathjaxTarget);
await replaceTree(fontSource, fontTarget);

console.log('MathJax 4.0.0 y mathjax-newcm-font 4.0.0 preparados localmente (Apache-2.0).');
