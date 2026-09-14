## Alcanzabilidad aditiva {#gl-alcanzabilidad-aditiva}

**Idea.** Comparar dos naturales preguntando si el segundo puede alcanzarse desde el primero mediante la suma de algún natural.

**En este tratado.** Para $m,n\in\mathbb N$,

$$
m\leq n\iff\exists k\in\mathbb N\;(n=m+k).
$$

Esta caracterización permite construir el orden sin presuponer previamente una relación de comparación sobre $\mathbb N$.

**En el Tratado:** [Definición 1.6.1 — Orden aritmético](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-orden-natural).

**Véase también:** [Orden natural](#gl-orden-natural), [Adición natural](#gl-adicion-natural), [Orden total](#gl-orden-total).

---

## Buen orden {#gl-buen-orden}

**Idea.** Un orden en el que todo subconjunto no vacío posee un elemento mínimo.

**En este tratado.** El orden natural de $\mathbb N$ satisface el principio

$$
A\subseteq\mathbb N,\ A\neq\varnothing
\quad\Longrightarrow\quad
A\text{ tiene mínimo}.
$$

Este resultado permite, entre otras consecuencias, obtener la inducción fuerte mediante un argumento por mínimo contraejemplo.

**En el Tratado:** [Teorema 1.6.12 — Principio de buen orden](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-principio-buen-orden-naturales).

**Véase también:** [Mínimo](#gl-minimo), [Orden natural](#gl-orden-natural), [Inducción fuerte](#gl-induccion-fuerte).

---

## Inducción fuerte {#gl-induccion-fuerte}

**Idea.** Para demostrar una propiedad en $n$, se permite suponerla para todos los naturales estrictamente menores que $n$.

**En este tratado.** Si para todo $n\in\mathbb N$

$$
[\forall m<n,\ P(m)]\Rightarrow P(n),
$$

entonces $P(n)$ vale para todo $n\in\mathbb N$.

La demostración utiliza el principio de buen orden: si hubiera contraejemplos, el menor de ellos contradice la hipótesis inductiva fuerte.

**En el Tratado:** [Corolario 1.6.13 — Inducción fuerte](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-induccion-fuerte).

**Véase también:** [Principio de inducción](#gl-principio-induccion), [Buen orden](#gl-buen-orden), [Orden estricto](#gl-orden-estricto).

---

## Orden natural {#gl-orden-natural}

**Idea.** El orden de los números naturales construido a partir de la propia aritmética de $\mathbb N$.

**En este tratado.** Se define por alcanzabilidad aditiva:

$$
m\leq n\iff\exists k\in\mathbb N\;(n=m+k).
$$

Después se demuestra que esta relación es un orden total y que, en la representación de von Neumann,

$$
m\leq n\iff m\subseteq n,
\qquad
m<n\iff m\in n.
$$

Así, el orden aritmético y la estructura conjuntista de los naturales coinciden.

**En el Tratado:** [Definición 1.6.1 — Orden aritmético](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-orden-natural), [Teorema 1.6.5 — Orden total](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-orden-natural-total), [Proposición 1.6.8 — El orden coincide con la inclusión](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-orden-natural-inclusion) y [Teorema 1.6.11 — Orden estricto y pertenencia](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-orden-estricto-pertenencia).

**Véase también:** [Alcanzabilidad aditiva](#gl-alcanzabilidad-aditiva), [Orden total](#gl-orden-total), [Orden estricto](#gl-orden-estricto), [Subconjunto](#gl-subconjunto).

---

::: {.callout-note title="Glosario vivo"}
Con **§1.6 — Orden natural** quedó incorporado el último vocabulario nuevo del Capítulo 1. **§§1.7–1.9** reutilizan nociones ya definidas, y **§2.0 — Por qué necesitamos los enteros** presenta sólo la motivación y el programa de construcción. El glosario volverá a ampliarse con **§2.1 — Diferencias formales**, cuando los nuevos objetos reciban definición matemática explícita.
:::
