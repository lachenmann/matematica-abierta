## Aplicación canónica de numerales naturales {#gl-numerales-naturales-cuerpo-ordenado}

**Idea.** En un cuerpo ordenado, los naturales pueden representarse internamente sumando repetidamente la unidad multiplicativa.

**En este tratado.** Para todo cuerpo ordenado $F$ se define por recursión una única función

$$
\nu_F:\mathbb N\to F
$$

con

$$
\nu_F(0)=0_F,
\qquad
\nu_F(S(n))=\nu_F(n)+1_F.
$$

No se identifica silenciosamente $n\in\mathbb N$ con $\nu_F(n)\in F$: la función $\nu_F$ es el puente explícito entre ambos sistemas. Se demuestra que preserva suma, producto y orden y que es inyectiva.

**En el Tratado:** [Definición 4.1.5 — Aplicación de numerales naturales en un cuerpo ordenado](../capitulos/tratado-de-analisis-capitulo-4-cuerpos-ordenados-y-el-problema-de-la-completitud.md#ta-numerales-naturales-cuerpo-ordenado) y [Proposición 4.1.6 — Aritmética y orden de los numerales naturales](../capitulos/tratado-de-analisis-capitulo-4-cuerpos-ordenados-y-el-problema-de-la-completitud.md#ta-aritmetica-orden-numerales).

**Véase también:** [Números naturales](#gl-numeros-naturales), [Recursión](#gl-recursion), [Inyectividad](#gl-inyectividad).

---

## Cuerpo ordenado {#gl-cuerpo-ordenado}

**Idea.** Un cuerpo ordenado combina las operaciones de un cuerpo con un orden total compatible con la suma y con el producto de elementos no negativos.

**En este tratado.** Un cuerpo

$$
(F,+,\cdot,0_F,1_F)
$$

es ordenado cuando está provisto de un orden total $\leq_F$ tal que

$$
x\leq_F y\Longrightarrow x+z\leq_F y+z
$$

y

$$
0_F\leq_F x,\quad0_F\leq_F y
\Longrightarrow
0_F\leq_F xy.
$$

Las reglas usuales de signos, la positividad de $1_F$ y la inversión del orden al tomar recíprocos positivos se demuestran a partir de estas condiciones; no se añaden como axiomas separados.

**En el Tratado:** [Definición 4.1.1 — Cuerpo ordenado](../capitulos/tratado-de-analisis-capitulo-4-cuerpos-ordenados-y-el-problema-de-la-completitud.md#ta-cuerpo-ordenado).

**Véase también:** [Cuerpo](#gl-cuerpo), [Orden total](#gl-orden-total), [Orden estricto](#gl-orden-estricto), [Cuerpo ordenado completo](#gl-cuerpo-ordenado-completo).

---

## Cuerpo ordenado completo {#gl-cuerpo-ordenado-completo}

**Idea.** Un cuerpo ordenado es completo, en el sentido de orden usado en esta parte del tratado, cuando los subconjuntos no vacíos que tienen cotas superiores no dejan «fronteras faltantes»: cada uno posee una menor cota superior dentro del propio cuerpo.

**En este tratado.** Un cuerpo ordenado $F$ es **completo** si tiene la propiedad del supremo, es decir, si todo subconjunto no vacío $A\subseteq F$ acotado superiormente posee $\sup A\in F$.

De esta propiedad se deduce también la existencia de ínfimos para subconjuntos no vacíos acotados inferiormente. En §4.7 se demuestra además que, en el desarrollo actual, esta condición es equivalente a la propiedad de separación y al principio de intersección de intervalos cerrados. Todo cuerpo ordenado completo es arquimediano y, en consecuencia, su subcuerpo primo es denso. El cuerpo ordenado $\mathbb Q$ no es completo.

**En el Tratado:** [Definición 4.6.1 — Propiedad del supremo y cuerpo ordenado completo](../capitulos/tratado-de-analisis-capitulo-4-cuerpos-ordenados-y-el-problema-de-la-completitud.md#ta-propiedad-supremo-cuerpo-completo), [Proposición 4.6.2 — La propiedad del supremo implica la propiedad del ínfimo](../capitulos/tratado-de-analisis-capitulo-4-cuerpos-ordenados-y-el-problema-de-la-completitud.md#ta-supremo-implica-infimo), [Teorema 4.6.3 — Todo cuerpo ordenado completo es arquimediano](../capitulos/tratado-de-analisis-capitulo-4-cuerpos-ordenados-y-el-problema-de-la-completitud.md#ta-completo-implica-arquimediano) y [Corolario 4.7.5 — Cuatro formulaciones de completitud disponibles en esta etapa](../capitulos/tratado-de-analisis-capitulo-4-cuerpos-ordenados-y-el-problema-de-la-completitud.md#ta-cuatro-formulaciones-completitud).

**Véase también:** [Propiedad del supremo](#gl-propiedad-supremo), [Propiedad de separación](#gl-propiedad-separacion), [Principio de intersección de intervalos cerrados](#gl-principio-interseccion-intervalos-cerrados), [Supremo](#gl-supremo), [Ínfimo](#gl-infimo), [Propiedad arquimediana](#gl-propiedad-arquimediana), [Incompletitud de $\mathbb Q$](#gl-incompletitud-racionales).

---

## Propiedad del supremo {#gl-propiedad-supremo}

**Idea.** La propiedad del supremo afirma que todo conjunto no vacío que esté acotado por arriba posee dentro del sistema una frontera superior óptima: la menor de sus cotas superiores.

**En este tratado.** Un cuerpo ordenado $F$ tiene la **propiedad del supremo** cuando todo subconjunto $A\subseteq F$ que sea no vacío y acotado superiormente posee un supremo en $F$.

La definición cuantifica sobre subconjuntos arbitrarios de $F$. En la base ZF del tratado es una afirmación de existencia, no un procedimiento computacional $A\mapsto\sup A$. En §4.7 se demuestra que esta propiedad es equivalente, en el desarrollo actual, a la propiedad de separación y al principio de intersección de intervalos cerrados.

**En el Tratado:** [Definición 4.6.1 — Propiedad del supremo y cuerpo ordenado completo](../capitulos/tratado-de-analisis-capitulo-4-cuerpos-ordenados-y-el-problema-de-la-completitud.md#ta-propiedad-supremo-cuerpo-completo) y [Teorema 4.7.2 — Equivalencia entre propiedad del supremo y separación](../capitulos/tratado-de-analisis-capitulo-4-cuerpos-ordenados-y-el-problema-de-la-completitud.md#ta-supremo-equivale-separacion).

**Véase también:** [Cuerpo ordenado completo](#gl-cuerpo-ordenado-completo), [Propiedad de separación](#gl-propiedad-separacion), [Principio de intersección de intervalos cerrados](#gl-principio-interseccion-intervalos-cerrados), [Supremo](#gl-supremo), [Cota superior](#gl-cota-superior), [Acotado superiormente](#gl-acotado-superiormente), [Incompletitud de $\mathbb Q$](#gl-incompletitud-racionales).

---

## Propiedad de separación {#gl-propiedad-separacion}

**Idea.** Dos subconjuntos ordenados uno completamente a la izquierda del otro admiten un elemento del cuerpo situado entre ambos.

**En este tratado.** Un cuerpo ordenado $F$ tiene la **propiedad de separación** cuando, para cualesquiera subconjuntos no vacíos $A,B\subseteq F$ tales que

$$
a\leq b
\qquad
\text{para todo }a\in A,\ b\in B,
$$

existe $c\in F$ con

$$
a\leq c\leq b
\qquad
\text{para todo }a\in A,\ b\in B.
$$

En esta etapa no se llama todavía «cortadura» a la pareja $(A,B)$. La propiedad es equivalente a la propiedad del supremo.

**En el Tratado:** [Definición 4.7.1 — Propiedad de separación](../capitulos/tratado-de-analisis-capitulo-4-cuerpos-ordenados-y-el-problema-de-la-completitud.md#ta-propiedad-separacion) y [Teorema 4.7.2 — Equivalencia entre propiedad del supremo y separación](../capitulos/tratado-de-analisis-capitulo-4-cuerpos-ordenados-y-el-problema-de-la-completitud.md#ta-supremo-equivale-separacion).

**Véase también:** [Cuerpo ordenado completo](#gl-cuerpo-ordenado-completo), [Propiedad del supremo](#gl-propiedad-supremo), [Principio de intersección de intervalos cerrados](#gl-principio-interseccion-intervalos-cerrados).

---

## Principio de intersección de intervalos cerrados {#gl-principio-interseccion-intervalos-cerrados}

**Idea.** Si todos los extremos izquierdos de una familia de intervalos cerrados quedan a la izquierda de todos sus extremos derechos, existe al menos un punto común a toda la familia.

**En este tratado.** Un cuerpo ordenado $F$ satisface este principio si, para todo conjunto no vacío $I$ y familias $(a_i)_{i\in I}$, $(b_i)_{i\in I}$ con

$$
a_i\leq b_j
\qquad
\text{para todos }i,j\in I,
$$

se tiene

$$
\bigcap_{i\in I}[a_i,b_i]\neq\varnothing.
$$

La hipótesis cruzada es esencial en esta formulación. En §4.7 se demuestra que este principio es equivalente a la completitud de orden.

**En el Tratado:** [Definición 4.7.3 — Principio de intersección de intervalos cerrados](../capitulos/tratado-de-analisis-capitulo-4-cuerpos-ordenados-y-el-problema-de-la-completitud.md#ta-principio-interseccion-intervalos-cerrados) y [Teorema 4.7.4 — Equivalencia con el principio de intersección de intervalos](../capitulos/tratado-de-analisis-capitulo-4-cuerpos-ordenados-y-el-problema-de-la-completitud.md#ta-completitud-equivale-interseccion-intervalos).

**Véase también:** [Cuerpo ordenado completo](#gl-cuerpo-ordenado-completo), [Propiedad del supremo](#gl-propiedad-supremo), [Propiedad de separación](#gl-propiedad-separacion), [Intervalos acotados](#gl-intervalos-acotados), [Intersección](#gl-interseccion).

---

## Subcuerpo {#gl-subcuerpo}

**Idea.** Un subcuerpo es una parte de un cuerpo que contiene los elementos neutros y permanece cerrada bajo todas las operaciones necesarias para seguir siendo un cuerpo.

**En este tratado.** Un subconjunto $K\subseteq F$ es subcuerpo de un cuerpo $F$ cuando contiene $0_F$ y $1_F$, es cerrado bajo suma, producto y opuestos, y contiene $x^{-1}$ siempre que $x\in K$ sea no nulo. Con las operaciones restringidas, $K$ es entonces un cuerpo.

Si además $F$ es un cuerpo ordenado arquimediano, todo subcuerpo $K\subseteq F$ es **denso en $F$**: para cualesquiera $x<y$ existe $q\in K$ con $x<q<y$.

**En el Tratado:** [Definición 4.1.7 — Subcuerpo](../capitulos/tratado-de-analisis-capitulo-4-cuerpos-ordenados-y-el-problema-de-la-completitud.md#ta-subcuerpo) y [Corolario 4.5.2 — Todo subcuerpo de un cuerpo arquimediano es denso](../capitulos/tratado-de-analisis-capitulo-4-cuerpos-ordenados-y-el-problema-de-la-completitud.md#ta-todo-subcuerpo-denso-arquimediano).

**Véase también:** [Cuerpo](#gl-cuerpo), [Subconjunto](#gl-subconjunto), [Subcuerpo primo](#gl-subcuerpo-primo), [Propiedad arquimediana](#gl-propiedad-arquimediana).

---

## Subcuerpo primo {#gl-subcuerpo-primo}

**Idea.** El subcuerpo primo es la parte mínima de un cuerpo que está forzada por las propias operaciones y los elementos $0$ y $1$.

**En este tratado.** Si $\mathcal S_F$ es el conjunto de todos los subcuerpos de $F$, se define

$$
P_F:=\bigcap_{K\in\mathcal S_F}K.
$$

Se demuestra que $P_F$ es un subcuerpo de $F$ y que está contenido en todo subcuerpo de $F$. En un cuerpo ordenado, todos los numerales $\nu_F(n)$ pertenecen a $P_F$. Si el cuerpo ordenado es además arquimediano, $P_F$ es denso: entre cualesquiera $x<y$ en $F$ existe $q\in P_F$ con $x<q<y$.

Si $F$ es completo, la arquimedianidad se obtiene como teorema y, por tanto, esta densidad del subcuerpo primo también vale en todo cuerpo ordenado completo.

**En el Tratado:** [Definición 4.1.8 — Subcuerpo primo](../capitulos/tratado-de-analisis-capitulo-4-cuerpos-ordenados-y-el-problema-de-la-completitud.md#ta-subcuerpo-primo), [Proposición 4.1.9 — Minimalidad del subcuerpo primo](../capitulos/tratado-de-analisis-capitulo-4-cuerpos-ordenados-y-el-problema-de-la-completitud.md#ta-minimalidad-subcuerpo-primo), [Teorema 4.5.1 — Densidad del subcuerpo primo en un cuerpo arquimediano](../capitulos/tratado-de-analisis-capitulo-4-cuerpos-ordenados-y-el-problema-de-la-completitud.md#ta-densidad-subcuerpo-primo-arquimediano) y [Corolario 4.6.4 — El subcuerpo primo es denso en todo cuerpo ordenado completo](../capitulos/tratado-de-analisis-capitulo-4-cuerpos-ordenados-y-el-problema-de-la-completitud.md#ta-subcuerpo-primo-denso-completo).

**Véase también:** [Subcuerpo](#gl-subcuerpo), [Aplicación canónica de numerales naturales](#gl-numerales-naturales-cuerpo-ordenado), [Propiedad arquimediana](#gl-propiedad-arquimediana), [Cuerpo ordenado completo](#gl-cuerpo-ordenado-completo).

---
