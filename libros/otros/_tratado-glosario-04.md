## Transitividad {#gl-transitividad}

**Idea.** Dos pasos consecutivos de la relación pueden comprimirse en uno.

**En este tratado.** Una relación $R$ sobre $A$ es **transitiva** si

$$
(aRb\land bRc)\Longrightarrow aRc.
$$

**En el Tratado:** [Definición 0.4.6 — Propiedades de una relación](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-propiedades-relacion).

**Véase también:** [Reflexividad](#gl-reflexividad), [Simetría](#gl-simetria), [Relación de equivalencia](#gl-relacion-equivalencia).

---

## Tupla finita {#gl-tupla-finita}

**Idea.** Una lista ordenada de un número finito de componentes.

**En este tratado.** Las tuplas de longitud mayor que dos se codifican mediante pares ordenados anidados. Salvo indicación contraria,

$$
\langle a,b,c\rangle
:=
\langle a,\langle b,c\rangle\rangle.
$$

La forma concreta de anidación es representacional y no se considera contenido matemático adicional.

**En el Tratado:** [Convención 0.3.5 — Tuplas finitas](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-tuplas-finitas).

**Véase también:** [Par ordenado](#gl-par-ordenado), [Par de Kuratowski](#gl-par-kuratowski).

---

## Unión {#gl-union}

**Idea.** El conjunto formado por los elementos que pertenecen a uno u otro de dos conjuntos.

**En este tratado.**

$$
A\cup B:=\bigcup\{A,B\},
$$

de modo que

$$
x\in A\cup B
\iff
(x\in A\lor x\in B).
$$

**En el Tratado:** [Definición 0.2.9 — Unión binaria](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-union-binaria).

**Véase también:** [Intersección](#gl-interseccion), [Par no ordenado](#gl-par-no-ordenado).

---

## ZF {#gl-zf}

**Idea.** La teoría axiomática de conjuntos de Zermelo–Fraenkel que sirve como suelo conjuntista del tratado.

**En este tratado.** ZF, junto con lógica clásica de primer orden con igualdad, constituye el fundamento ambiente. Los axiomas no se cuentan como teoremas internos. El axioma de elección no se presupone ni se utiliza silenciosamente.

**En el Tratado:** [§0.1.1 — Inventario axiomático](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-zf).

**Véase también:** [Lógica clásica](#gl-logica-clasica), [Separación restringida](#gl-separacion-restringida), [Extensionalidad](#gl-extensionalidad).

---

## Acotado inferiormente {#gl-acotado-inferiormente}

**Idea.** Un conjunto posee algún elemento del ambiente que queda por debajo de todos sus elementos.

**En este tratado.** Si $(A,\leq)$ es parcialmente ordenado y $S\subseteq A$, diremos que $S$ está **acotado inferiormente** cuando existe una cota inferior de $S$.

**En el Tratado:** [Definición 0.7.4 — Cotas superiores e inferiores](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-cotas).

**Véase también:** [Cota inferior](#gl-cota-inferior), [Ínfimo](#gl-infimo).

---

## Acotado superiormente {#gl-acotado-superiormente}

**Idea.** Un conjunto posee algún elemento del ambiente que queda por encima de todos sus elementos.

**En este tratado.** Si $(A,\leq)$ es parcialmente ordenado y $S\subseteq A$, diremos que $S$ está **acotado superiormente** cuando existe una cota superior de $S$.

**En el Tratado:** [Definición 0.7.4 — Cotas superiores e inferiores](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-cotas).

**Véase también:** [Cota superior](#gl-cota-superior), [Supremo](#gl-supremo).

---

## Cota inferior {#gl-cota-inferior}

**Idea.** Un elemento del ambiente que no supera a ningún elemento del subconjunto considerado.

**En este tratado.** Si $(A,\leq)$ es parcialmente ordenado y $S\subseteq A$, un elemento $\ell\in A$ es una **cota inferior** de $S$ si

$$
\forall s\in S,\quad \ell\leq s.
$$

**En el Tratado:** [Definición 0.7.4 — Cotas superiores e inferiores](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-cotas).

**Véase también:** [Acotado inferiormente](#gl-acotado-inferiormente), [Mínimo](#gl-minimo), [Ínfimo](#gl-infimo).

---

## Cota superior {#gl-cota-superior}

**Idea.** Un elemento del ambiente que no queda por debajo de ningún elemento del subconjunto considerado.

**En este tratado.** Si $(A,\leq)$ es parcialmente ordenado y $S\subseteq A$, un elemento $u\in A$ es una **cota superior** de $S$ si

$$
\forall s\in S,\quad s\leq u.
$$

**En el Tratado:** [Definición 0.7.4 — Cotas superiores e inferiores](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-cotas).

**Véase también:** [Acotado superiormente](#gl-acotado-superiormente), [Máximo](#gl-maximo), [Supremo](#gl-supremo).

---

## Ínfimo {#gl-infimo}

**Idea.** La mayor de todas las cotas inferiores de un subconjunto.

**En este tratado.** Si $S\subseteq A$, un elemento $\ell\in A$ es el **ínfimo** de $S$ si es cota inferior de $S$ y toda cota inferior $v$ satisface

$$
v\leq \ell.
$$

La definición no garantiza existencia. Sólo cuando ésta haya sido demostrada escribiremos $\inf S$.

**En el Tratado:** [Definición 0.7.7 — Supremo e ínfimo](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-supremo-infimo) y [Corolario 0.7.9 — Notación legítima](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-notacion-sup-inf).

**Véase también:** [Cota inferior](#gl-cota-inferior), [Mínimo](#gl-minimo), [Supremo](#gl-supremo).

---

## Máximo {#gl-maximo}

**Idea.** El mayor elemento de un subconjunto, cuando tal elemento pertenece al propio subconjunto.

**En este tratado.** Si $S\subseteq A$, un elemento $m\in S$ es el **máximo** de $S$ si

$$
\forall s\in S,\quad s\leq m.
$$

La pertenencia $m\in S$ es parte de la definición y distingue al máximo de una cota superior exterior.

**En el Tratado:** [Definición 0.7.5 — Máximo y mínimo](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-maximo-minimo).

**Véase también:** [Cota superior](#gl-cota-superior), [Supremo](#gl-supremo), [Mínimo](#gl-minimo).

---

## Mínimo {#gl-minimo}

**Idea.** El menor elemento de un subconjunto, cuando tal elemento pertenece al propio subconjunto.

**En este tratado.** Si $S\subseteq A$, un elemento $n\in S$ es el **mínimo** de $S$ si

$$
\forall s\in S,\quad n\leq s.
$$

La pertenencia $n\in S$ es parte de la definición y distingue al mínimo de una cota inferior exterior.

**En el Tratado:** [Definición 0.7.5 — Máximo y mínimo](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-maximo-minimo).

**Véase también:** [Cota inferior](#gl-cota-inferior), [Ínfimo](#gl-infimo), [Máximo](#gl-maximo).

---

## Orden estricto {#gl-orden-estricto}

**Idea.** La versión estricta de un orden no estricto: compara sin admitir igualdad.

**En este tratado.** Si $\leq$ es un orden parcial sobre $A$, definimos

$$
a<b
\quad\Longleftrightarrow\quad
(a\leq b\ \text{y}\ a\neq b).
$$

Este orden estricto asociado es irreflexivo y transitivo.

**En el Tratado:** [Definición 0.7.2 — Orden estricto asociado](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-orden-estricto) y [Proposición 0.7.3](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-propiedades-orden-estricto).

**Véase también:** [Orden parcial](#gl-orden-parcial), [Orden total](#gl-orden-total).

---

## Orden parcial {#gl-orden-parcial}

**Idea.** Un orden en el que no es necesario que todos los pares de elementos sean comparables.

**En este tratado.** Una relación $\leq$ sobre $A$ es un **orden parcial** si es reflexiva, antisimétrica y transitiva.

**En el Tratado:** [Definición 0.7.1 — Preorden, orden parcial y orden total](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-preorden-orden-parcial-total).

**Véase también:** [Preorden](#gl-preorden), [Orden total](#gl-orden-total), [Antisimetría](#gl-antisimetria).

---

## Orden total {#gl-orden-total}

**Idea.** Un orden parcial en el que cualesquiera dos elementos pueden compararse.

**En este tratado.** Una relación $\leq$ sobre $A$ es un **orden total** si es reflexiva, antisimétrica y transitiva, y además para cualesquiera $a,b\in A$,

$$
a\leq b\quad\text{o}\quad b\leq a.
$$

**En el Tratado:** [Definición 0.7.1 — Preorden, orden parcial y orden total](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-preorden-orden-parcial-total).

**Véase también:** [Orden parcial](#gl-orden-parcial), [Totalidad (conexidad)](#gl-totalidad), [Orden estricto](#gl-orden-estricto).

---

## Preorden {#gl-preorden}

**Idea.** La estructura de orden más débil considerada aquí: permite reflexividad y transitividad, sin exigir antisimetría.

**En este tratado.** Una relación $\leq$ sobre $A$ es un **preorden** si es reflexiva y transitiva.

**En el Tratado:** [Definición 0.7.1 — Preorden, orden parcial y orden total](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-preorden-orden-parcial-total).

**Véase también:** [Orden parcial](#gl-orden-parcial), [Reflexividad](#gl-reflexividad), [Transitividad](#gl-transitividad).

---
