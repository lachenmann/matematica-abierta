import test from 'node:test';
import assert from 'node:assert/strict';
import { EXERCISES } from '../exercises.mjs';
import { toMathText } from '../math-tex.mjs';

const raw = String.raw;

test('Fracciones: estructura LaTeX y no barras tipográficas planas', () => {
  assert.equal(toMathText('Calcula 1/2 + 1/3.'), `Calcula ${raw`\(\frac12+\frac13\)`}.`);
  assert.equal(toMathText('3/6 + 2/6 = 5/6'), raw`\(\frac36+\frac26=\frac56\)`);
  assert.equal(toMathText('5/12'), raw`\(\frac5{12}\)`);
});

test('Ecuaciones: agrupación, signo negativo y solución se conservan', () => {
  assert.equal(toMathText('Resuelve 2(x − 3) = x + 5.'), `Resuelve ${raw`\(2(x-3)=x+5\)`}.`);
  assert.equal(toMathText('x = −1'), raw`\(x=-1\)`);
  assert.equal(toMathText('Comprobación: 2(11−3)=16 y 11+5=16.'), `Comprobación: ${raw`\(2(11-3)=16\)`} y ${raw`\(11+5=16\)`}.`);
});

test('Derivadas: potencias, prima y multiplicación en TeX', () => {
  const formatted = toMathText("f′(x) = 3(x² + 1)² · 2x = 6x(x² + 1)²");
  assert.equal(formatted, raw`\(f'(x)=3(x^2+1)^2\cdot 2x=6x(x^2+1)^2\)`);
  assert.equal(toMathText("La función exterior es g(u)=u³."), `La función exterior es ${raw`\(g(u)=u^3\)`}.`);
});

test('Demostración: pertenencia, implicación y fracción de distractor', () => {
  assert.equal(toMathText('n = 2k, con k ∈ ℤ.'), `${raw`\(n=2k\)`}, con ${raw`\(k\in\mathbb Z\)`}.`);
  assert.equal(toMathText('n² impar ⇒ n impar. ∎'), `${raw`\(n^2\text{ impar}\Rightarrow n\text{ impar}\)`}. ∎`);
  assert.equal(toMathText('n = k/2 para algún k impar'), `${raw`\(n=\frac{k}{2}\)`} para algún k impar`);
});

test('Texto ordinario y avisos Elo no sufren transformación', () => {
  for (const source of ['Regla de la cadena', 'Una decisión matemática a la vez.', 'Elo experimental: +12', '✓ Correcto.']) {
    assert.equal(toMathText(source), source);
  }
  assert.throws(() => toMathText(null), TypeError);
});

test('El banco del motor y su primera elección nunca se modifican por el formateador', () => {
  const before = structuredClone(EXERCISES);
  for (const exercise of EXERCISES) {
    toMathText(exercise.prompt);
    for (const step of exercise.steps) {
      toMathText(step.question);
      toMathText(step.notation);
      toMathText(step.explanation);
      step.options.forEach(toMathText);
    }
  }
  assert.deepEqual(EXERCISES, before);
});
