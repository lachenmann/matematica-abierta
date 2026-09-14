## Anillo {#gl-anillo}

**Idea.** Una estructura con suma y multiplicación en la que la suma forma un grupo abeliano, la multiplicación es asociativa y distribuye sobre la suma, y existe una unidad multiplicativa.

**En este tratado.** Un anillo $R$ viene provisto de $+$, $\cdot$, $0_R$ y $1_R$; $(R,+,0_R)$ es un grupo abeliano, la multiplicación es asociativa, $1_R$ es unidad y se cumplen ambas leyes distributivas. **Por convención, todos los anillos del tratado tienen unidad.** La palabra «anillo» no implica por sí sola conmutatividad de la multiplicación.

**En el Tratado:** [Convención 2.6.2 — Terminología algebraica](../capitulos/tratado-de-analisis-capitulo-2-los-numeros-enteros.md#ta-terminologia-algebraica).

**Véase también:** [Grupo abeliano](#gl-grupo-abeliano), [Anillo conmutativo](#gl-anillo-conmutativo), [Unidad entera](#gl-unidad-entera).

---

## Anillo conmutativo {#gl-anillo-conmutativo}

**Idea.** Un anillo en el que el orden de los factores no altera el producto.

**En este tratado.** Un anillo conmutativo es un anillo cuya multiplicación satisface

$$
xy=yx
$$

para todos sus elementos. En §2.6 se demuestra que

$$
(\mathbb Z,+,\cdot,0_{\mathbb Z},1_{\mathbb Z})
$$

posee esta estructura.

**En el Tratado:** [Convención 2.6.2 — Terminología algebraica](../capitulos/tratado-de-analisis-capitulo-2-los-numeros-enteros.md#ta-terminologia-algebraica) y [Teorema 2.6.3 — Primera estructura de anillo de $\mathbb Z$](../capitulos/tratado-de-analisis-capitulo-2-los-numeros-enteros.md#ta-anillo-conmutativo-enteros).

**Véase también:** [Anillo](#gl-anillo), [Multiplicación entera](#gl-multiplicacion-entera), [Dominio de integridad](#gl-dominio-integridad).

---

## Dominio de integridad {#gl-dominio-integridad}

**Idea.** Un anillo conmutativo no trivial en el que un producto sólo puede ser cero si alguno de sus factores es cero.

**En este tratado.** Un dominio de integridad es un anillo conmutativo $R$ tal que

$$
0_R\neq1_R
$$

y

$$
xy=0_R\Longrightarrow x=0_R\ \text{o}\ y=0_R.
$$

La noción queda fijada en §2.6. La demostración de que $\mathbb Z$ satisface estas condiciones se realizará posteriormente, una vez establecida la forma normal con signo y la ausencia de divisores de cero.

**En el Tratado:** [Convención 2.6.2 — Terminología algebraica](../capitulos/tratado-de-analisis-capitulo-2-los-numeros-enteros.md#ta-terminologia-algebraica).

**Véase también:** [Anillo](#gl-anillo), [Anillo conmutativo](#gl-anillo-conmutativo), [Producto nulo](#gl-producto-nulo).

---

::: {.callout-note title="Glosario vivo"}
Con **§2.6 — Estructura algebraica** se fijan las convenciones de anillo, anillo conmutativo y dominio de integridad. La siguiente ampliación acompañará **§2.7 — Incrustación canónica de $\mathbb N$**.
:::
