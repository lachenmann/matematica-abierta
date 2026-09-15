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

**Véase también:** [Cuerpo](#gl-cuerpo), [Orden total](#gl-orden-total), [Orden estricto](#gl-orden-estricto).

---

## Subcuerpo {#gl-subcuerpo}

**Idea.** Un subcuerpo es una parte de un cuerpo que contiene los elementos neutros y permanece cerrada bajo todas las operaciones necesarias para seguir siendo un cuerpo.

**En este tratado.** Un subconjunto $K\subseteq F$ es subcuerpo de un cuerpo $F$ cuando contiene $0_F$ y $1_F$, es cerrado bajo suma, producto y opuestos, y contiene $x^{-1}$ siempre que $x\in K$ sea no nulo. Con las operaciones restringidas, $K$ es entonces un cuerpo.

**En el Tratado:** [Definición 4.1.7 — Subcuerpo](../capitulos/tratado-de-analisis-capitulo-4-cuerpos-ordenados-y-el-problema-de-la-completitud.md#ta-subcuerpo).

**Véase también:** [Cuerpo](#gl-cuerpo), [Subconjunto](#gl-subconjunto), [Subcuerpo primo](#gl-subcuerpo-primo).

---

## Subcuerpo primo {#gl-subcuerpo-primo}

**Idea.** El subcuerpo primo es la parte mínima de un cuerpo que está forzada por las propias operaciones y los elementos $0$ y $1$.

**En este tratado.** Si $\mathcal S_F$ es el conjunto de todos los subcuerpos de $F$, se define

$$
P_F:=\bigcap_{K\in\mathcal S_F}K.
$$

Se demuestra que $P_F$ es un subcuerpo de $F$ y que está contenido en todo subcuerpo de $F$. En un cuerpo ordenado, todos los numerales $\nu_F(n)$ pertenecen a $P_F$.

**En el Tratado:** [Definición 4.1.8 — Subcuerpo primo](../capitulos/tratado-de-analisis-capitulo-4-cuerpos-ordenados-y-el-problema-de-la-completitud.md#ta-subcuerpo-primo) y [Proposición 4.1.9 — Minimalidad del subcuerpo primo](../capitulos/tratado-de-analisis-capitulo-4-cuerpos-ordenados-y-el-problema-de-la-completitud.md#ta-minimalidad-subcuerpo-primo).

**Véase también:** [Subcuerpo](#gl-subcuerpo), [Aplicación canónica de numerales naturales](#gl-numerales-naturales-cuerpo-ordenado).

---
