## Principio de definición binaria sobre clases {#gl-definicion-binaria-clases}

**Idea.** Una regla de dos variables definida sobre representantes puede descender a pares de clases si su valor no cambia al sustituir cualquiera de los representantes por otro equivalente.

**En este tratado.** Si $\sim$ es una relación de equivalencia sobre $A$ y

$$
\psi:A\times A\to B
$$

satisface

$$
a\sim a',\quad b\sim b'
\Longrightarrow
\psi(a,b)=\psi(a',b'),
$$

entonces existe una única función

$$
\overline{\psi}:(A/{\sim})\times(A/{\sim})\to B
$$

con

$$
\overline{\psi}([a],[b])=\psi(a,b).
$$

**En el Tratado:** [Teorema 2.3.1 — Principio de definición binaria sobre clases](../capitulos/tratado-de-analisis-capitulo-2-los-numeros-enteros.md#ta-principio-definicion-binaria-clases).

**Véase también:** [Principio de definición sobre clases](#gl-definicion-sobre-clases), [Clase de equivalencia](#gl-clase-equivalencia), [Representante](#gl-representante).

---

## Suma entera {#gl-suma-entera}

**Idea.** La operación aditiva de $\mathbb Z$, obtenida haciendo descender a clases la suma componente a componente de diferencias formales.

**En este tratado.** Para clases enteras definimos

$$
[(a,b)]+_{\mathbb Z}[(c,d)]
=
[(a+c,b+d)].
$$

La fórmula representa una operación genuina sobre $\mathbb Z$ porque se demuestra previamente que el resultado no depende de los representantes elegidos.

**En el Tratado:** [Definición 2.3.4 — Suma en $\mathbb Z$](../capitulos/tratado-de-analisis-capitulo-2-los-numeros-enteros.md#ta-suma-enteros), apoyada en [Proposición 2.3.3 — Compatibilidad de la suma con $\sim_{\mathbb Z}$](../capitulos/tratado-de-analisis-capitulo-2-los-numeros-enteros.md#ta-compatibilidad-suma-enteros).

**Véase también:** [Clase entera](#gl-clase-entera), [Diferencia formal](#gl-diferencia-formal), [Relación de equivalencia entera](#gl-relacion-equivalencia-entera).
