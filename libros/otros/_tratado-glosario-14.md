## Cero entero {#gl-cero-entero}

**Idea.** El elemento neutro para la suma en el sistema de los números enteros construido como cociente.

**En este tratado.** Definimos

$$
0_{\mathbb Z}:=[(0,0)].
$$

Este objeto pertenece a $\mathbb Z$ y todavía no se identifica literalmente con el natural $0$.

**En el Tratado:** [Notación 2.4.1 — Cero entero](../capitulos/tratado-de-analisis-capitulo-2-los-numeros-enteros.md#ta-cero-entero).

**Véase también:** [Número entero](#gl-numero-entero), [Suma entera](#gl-suma-entera), [Clase entera](#gl-clase-entera).

---

## Opuesto entero {#gl-opuesto-entero}

**Idea.** El entero que, sumado a otro entero, produce el cero entero.

**En este tratado.** La operación de opuesto se obtiene haciendo descender a clases el intercambio de componentes de una diferencia formal:

$$
\boxed{-[(a,b)]=[(b,a)].}
$$

La fórmula es legítima porque el intercambio respeta la relación de equivalencia entera.

**En el Tratado:** [Definición 2.4.2 — Opuesto](../capitulos/tratado-de-analisis-capitulo-2-los-numeros-enteros.md#ta-opuesto-enteros) y [Proposición 2.4.3 — Buena definición del opuesto](../capitulos/tratado-de-analisis-capitulo-2-los-numeros-enteros.md#ta-buena-definicion-opuesto).

**Véase también:** [Cero entero](#gl-cero-entero), [Suma entera](#gl-suma-entera), [Principio de definición sobre clases](#gl-definicion-sobre-clases).

---

## Grupo abeliano {#gl-grupo-abeliano}

**Idea.** Una estructura con una operación asociativa y conmutativa, elemento neutro y opuesto para cada elemento.

**En este tratado.** Con la suma ya construida, el cero $0_{\mathbb Z}$ y la operación de opuesto, se demuestra que para todo $x,y,z\in\mathbb Z$ se cumplen asociatividad, conmutatividad, existencia de neutro y existencia de inverso aditivo. Por ello $(\mathbb Z,+)$ es un grupo abeliano.

**En el Tratado:** [Proposición 2.4.4 — Leyes del grupo aditivo](../capitulos/tratado-de-analisis-capitulo-2-los-numeros-enteros.md#ta-grupo-aditivo-enteros).

**Véase también:** [Suma entera](#gl-suma-entera), [Cero entero](#gl-cero-entero), [Opuesto entero](#gl-opuesto-entero).

---

## Sustracción entera {#gl-sustraccion-entera}

**Idea.** Restar un entero equivale a sumar su opuesto.

**En este tratado.** Una vez construida la operación de opuesto, definimos para $x,y\in\mathbb Z$

$$
\boxed{x-y:=x+(-y).}
$$

Desde este punto la sustracción es una operación total sobre $\mathbb Z$, y toda ecuación $x+y=z$ posee la solución única $y=z-x$.

**En el Tratado:** [Definición 2.4.5 — Sustracción en $\mathbb Z$](../capitulos/tratado-de-analisis-capitulo-2-los-numeros-enteros.md#ta-sustraccion-enteros) y [Proposición 2.4.6 — Resolución universal de ecuaciones aditivas](../capitulos/tratado-de-analisis-capitulo-2-los-numeros-enteros.md#ta-resolucion-ecuaciones-aditivas-enteros).

**Véase también:** [Opuesto entero](#gl-opuesto-entero), [Grupo abeliano](#gl-grupo-abeliano), [Suma entera](#gl-suma-entera).

---

::: {.callout-note title="Glosario vivo"}
Con **§2.4 — Cero, opuesto y sustracción** se incorporan el cero entero, el opuesto, la estructura de grupo abeliano y la sustracción total en $\mathbb Z$. La siguiente ampliación acompañará **§2.5 — Multiplicación de enteros**.
:::
