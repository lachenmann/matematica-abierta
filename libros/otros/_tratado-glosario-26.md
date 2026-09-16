## Densidad del orden racional {#gl-densidad-orden-racional}

**Idea.** Un orden es denso cuando entre dos elementos distintos siempre puede encontrarse un tercero estrictamente intermedio.

**En este tratado.** Para el orden construido sobre $\mathbb Q$, si

$$
x<_{\mathbb Q}y,
$$

existe $z\in\mathbb Q$ tal que

$$
x<_{\mathbb Q}z<_{\mathbb Q}y.
$$

La demostración utiliza representantes de denominador positivo y, para

$$
x=\frac ab,
\qquad
y=\frac cd,
$$

construye explícitamente

$$
z=\frac{a+c}{b+d}.
$$

**En el Tratado:** [Teorema 3.8.3 — Densidad del orden racional](../capitulos/tratado-de-analisis-capitulo-3-los-numeros-racionales.md#ta-densidad-orden-racional).

**Véase también:** [Orden racional](#gl-orden-racional), [Orden estricto](#gl-orden-estricto), [Número racional](#gl-numero-racional).

---

## Propiedad arquimediana {#gl-propiedad-arquimediana}

**Idea.** Expresa que los numerales naturales canónicos no quedan acotados superiormente dentro del cuerpo ordenado: por grande que sea un elemento dado, algún numeral natural lo supera.

**En este tratado.** Sea $F$ un cuerpo ordenado y sea

$$
\nu_F:\mathbb N\to F
$$

su aplicación canónica de numerales naturales. Diremos que $F$ es **arquimediano** si

$$
\forall x\in F\;
\exists n\in\mathbb N
\quad
x<\nu_F(n).
$$

En la lógica clásica del tratado esto equivale a que $\nu_F[\mathbb N]$ no esté acotada superiormente. Además, se demuestra la caracterización equivalente

$$
\forall \varepsilon>0\;
\exists n\in\mathbb N,
\quad n\neq0,
\qquad
0<\nu_F(n)^{-1}<\varepsilon.
$$

El caso $F=\mathbb Q$ recupera exactamente la propiedad arquimediana demostrada previamente para la incrustación canónica $\nu_{\mathbb N}^{\mathbb Q}$.

**En el Tratado:** [Definición 4.4.1 — Cuerpo ordenado arquimediano](../capitulos/tratado-de-analisis-capitulo-4-cuerpos-ordenados-y-el-problema-de-la-completitud.md#ta-cuerpo-ordenado-arquimediano), [Proposición 4.4.2 — Caracterización por recíprocos pequeños](../capitulos/tratado-de-analisis-capitulo-4-cuerpos-ordenados-y-el-problema-de-la-completitud.md#ta-arquimedianidad-reciprocos) y [Teorema 3.8.5 — $\mathbb Q$ es arquimediano](../capitulos/tratado-de-analisis-capitulo-3-los-numeros-racionales.md#ta-q-arquimediano).

**Véase también:** [Aplicación canónica de numerales naturales](#gl-numerales-naturales-cuerpo-ordenado), [Cuerpo ordenado](#gl-cuerpo-ordenado), [Orden racional](#gl-orden-racional).

---
