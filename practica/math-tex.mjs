/** Capa editorial de presentación: los enunciados y respuestas del motor permanecen intactos.
 * Solo se convierten fragmentos conocidos del banco demostrativo, nunca HTML ni entradas del usuario.
 */
const EXPRESSIONS = [
  ['f′(x) = 3(x² + 1)² · 2x = 6x(x² + 1)²', String.raw`f'(x)=3(x^2+1)^2\cdot 2x=6x(x^2+1)^2`],
  ['f(x) = (x² + 1)³', String.raw`f(x)=(x^2+1)^3`],
  ['u(x) = (x² + 1)³', String.raw`u(x)=(x^2+1)^3`],
  ['u(x) = x² + 1', String.raw`u(x)=x^2+1`],
  ['u(x) = 3x²', String.raw`u(x)=3x^2`],
  ['u′(x) = 2x', String.raw`u'(x)=2x`],
  ['6x(x² + 1)³', String.raw`6x(x^2+1)^3`],
  ['6x(x² + 1)²', String.raw`6x(x^2+1)^2`],
  ['3(x² + 1)²', String.raw`3(x^2+1)^2`],
  ['g(u)=u³', String.raw`g(u)=u^3`],
  ['2x + 1', String.raw`2x+1`],
  ['3x²', String.raw`3x^2`],
  ['x² + 1', String.raw`x^2+1`],
  ['u³', String.raw`u^3`],
  ['u′', String.raw`u'`],
  ['x²', String.raw`x^2`],
  ['2x', String.raw`2x`],
  ['m.c.m.(2, 3) = 6', String.raw`\operatorname{mcm}(2,3)=6`],
  ['1/2 = 3/6; 1/3 = 2/6', String.raw`\frac12=\frac36;\quad\frac13=\frac26`],
  ['3/6 + 2/6 = 5/6', String.raw`\frac36+\frac26=\frac56`],
  ['3/6 + 2/6', String.raw`\frac36+\frac26`],
  ['2/6 + 2/6', String.raw`\frac26+\frac26`],
  ['1/6 + 1/6', String.raw`\frac16+\frac16`],
  ['1/2 + 1/3', String.raw`\frac12+\frac13`],
  ['5/12', String.raw`\frac5{12}`],
  ['2/5', String.raw`\frac25`],
  ['5/6', String.raw`\frac56`],
  ['3/6', String.raw`\frac36`],
  ['2/6', String.raw`\frac26`],
  ['1/2', String.raw`\frac12`],
  ['1/3', String.raw`\frac13`],
  ['2(x − 3) = x + 5', String.raw`2(x-3)=x+5`],
  ['2x − 6 = x + 5', String.raw`2x-6=x+5`],
  ['x − 6 = 5', String.raw`x-6=5`],
  ['2(11−3)=16', String.raw`2(11-3)=16`],
  ['11+5=16', String.raw`11+5=16`],
  ['2(x − 3)', String.raw`2(x-3)`],
  ['2x − 6', String.raw`2x-6`],
  ['x = −1', String.raw`x=-1`],
  ['x = 11', String.raw`x=11`],
  ['x = 5', String.raw`x=5`],
  ['n² impar ⇒ n impar', String.raw`n^2\text{ impar}\Rightarrow n\text{ impar}`],
  ['n par ⇒ n² par', String.raw`n\text{ par}\Rightarrow n^2\text{ par}`],
  ['n² = 4k² = 2(2k²)', String.raw`n^2=4k^2=2(2k^2)`],
  ['n² = 2k²', String.raw`n^2=2k^2`],
  ['n² = 4k + 2', String.raw`n^2=4k+2`],
  ['n = 2k + 1', String.raw`n=2k+1`],
  ['n = k/2', String.raw`n=\frac{k}{2}`],
  ['n = 2k', String.raw`n=2k`],
  ['k ∈ ℤ', String.raw`k\in\mathbb Z`],
  ['¬Q⇒¬P', String.raw`\neg Q\Rightarrow\neg P`],
  ['P⇒Q', String.raw`P\Rightarrow Q`],
  ['2k²', String.raw`2k^2`],
  ['n²', String.raw`n^2`]
];
const escapePattern = value => value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
const texByFragment = new Map(EXPRESSIONS);
const fragments = new RegExp(EXPRESSIONS.map(([source]) => escapePattern(source)).sort((a, b) => b.length - a.length).join('|'), 'g');

/** Conserva la prosa original y delimita solamente fragmentos matemáticos conocidos. */
export function toMathText(source) {
  if (typeof source !== 'string') throw new TypeError('Se esperaba texto');
  return source.replace(fragments, match => String.raw`\(${texByFragment.get(match)}\)`);
}
