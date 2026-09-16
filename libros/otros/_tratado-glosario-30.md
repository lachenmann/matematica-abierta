## Intervalos acotados {#gl-intervalos-acotados}

**Idea.** Un intervalo acotado recoge los elementos de un cuerpo ordenado situados entre dos extremos, incluyendo o excluyendo cada extremo según la notación utilizada.

**En este tratado.** Para $a,b$ en un cuerpo ordenado $F$ se definen

$$
[a,b]=\{x\in F:a\leq x\leq b\},
$$

$$
(a,b)=\{x\in F:a<x<b\},
$$

$$
[a,b)=\{x\in F:a\leq x<b\},
\qquad
(a,b]=\{x\in F:a<x\leq b\}.
$$

No se exige previamente $a\leq b$; la propia condición de pertenencia determina cuándo el intervalo posee elementos.

**En el Tratado:** [Definición 4.3.1 — Intervalos acotados](../capitulos/tratado-de-analisis-capitulo-4-cuerpos-ordenados-y-el-problema-de-la-completitud.md#ta-intervalos-acotados) y [Proposición 4.3.2 — Habitabilidad y no vaciedad de intervalos](../capitulos/tratado-de-analisis-capitulo-4-cuerpos-ordenados-y-el-problema-de-la-completitud.md#ta-habitabilidad-intervalos).

**Véase también:** [Cuerpo ordenado](#gl-cuerpo-ordenado), [Intervalos centrados](#gl-intervalos-centrados).

---

## Intervalos centrados {#gl-intervalos-centrados}

**Idea.** Un intervalo centrado describe los elementos cuya distancia algebraica a un centro no supera un radio dado.

**En este tratado.** Si $a\in F$ y $r\geq0$, el intervalo cerrado de centro $a$ y radio $r$ satisface

$$
x\in[a-r,a+r]
\iff
|x-a|\leq r.
$$

Esta equivalencia enlaza directamente la notación de intervalos con el valor absoluto y será reutilizada posteriormente en formulaciones de proximidad.

**En el Tratado:** [Proposición 4.3.3 — Intervalos centrados y valor absoluto](../capitulos/tratado-de-analisis-capitulo-4-cuerpos-ordenados-y-el-problema-de-la-completitud.md#ta-intervalos-centrados-valor-absoluto).

**Véase también:** [Intervalos acotados](#gl-intervalos-acotados), [Valor absoluto](#gl-valor-absoluto).

---
