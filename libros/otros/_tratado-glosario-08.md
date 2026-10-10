## Adición natural {#gl-adicion-natural}

**Idea.** La operación que, fijado un natural $m$, parte de $m$ y aplica el sucesor tantas veces como indique un segundo natural.

**En este tratado.** La suma se define por recursión con parámetros como la única función

$$
+:\mathbb N\times\mathbb N\to\mathbb N
$$

que satisface

$$
m+0=m,
\qquad
m+S(n)=S(m+n).
$$

La definición recursa en el segundo argumento; la conmutatividad no forma parte de la definición y se demuestra después.

**En el Tratado:** [Definición 1.4.1 — Adición](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-adicion-naturales).

**Véase también:** [Recursión con parámetros](#gl-recursion-parametros), [Sucesor](#gl-sucesor), [Números naturales](#gl-numeros-naturales).

---

## Asociatividad de la suma {#gl-asociatividad-suma}

**Idea.** Al sumar tres naturales, la forma de agrupar los sumandos no altera el resultado.

**En este tratado.** Para $a,b,c\in\mathbb N$,

$$
(a+b)+c=a+(b+c).
$$

Esta propiedad es un teorema obtenido por inducción a partir de la definición recursiva de la suma.

**En el Tratado:** [Teorema 1.4.4 — Asociatividad de la suma](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-asociatividad-suma).

**Véase también:** [Adición natural](#gl-adicion-natural), [Conmutatividad de la suma](#gl-conmutatividad-suma), [Principio de inducción](#gl-principio-induccion).

---

## Cancelación aditiva {#gl-cancelacion-aditiva}

**Idea.** Un mismo sumando puede cancelarse de ambos lados de una igualdad.

**En este tratado.** Para $a,b,c\in\mathbb N$,

$$
a+c=b+c\Rightarrow a=b.
$$

La demostración reduce por inducción el caso sucesor a la inyectividad de $S$.

**En el Tratado:** [Proposición 1.4.6 — Cancelación aditiva](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-cancelacion-aditiva).

**Véase también:** [Adición natural](#gl-adicion-natural), [Sucesor](#gl-sucesor), [Inyectividad](#gl-inyectividad).

---

## Conmutatividad de la suma {#gl-conmutatividad-suma}

**Idea.** El orden de los dos sumandos no modifica la suma.

**En este tratado.** Para $a,b\in\mathbb N$,

$$
a+b=b+a.
$$

La conmutatividad no se incorpora a la definición de $+$: se demuestra después por inducción.

**En el Tratado:** [Teorema 1.4.5 — Conmutatividad de la suma](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-conmutatividad-suma).

**Véase también:** [Adición natural](#gl-adicion-natural), [Asociatividad de la suma](#gl-asociatividad-suma), [Principio de inducción](#gl-principio-induccion).

---

## Suma nula {#gl-suma-nula}

**Idea.** Dos naturales sólo pueden sumar cero cuando ambos son cero.

**En este tratado.** Para $a,b\in\mathbb N$,

$$
a+b=0\iff a=0\text{ y }b=0.
$$

**En el Tratado:** [Proposición 1.4.7 — Suma nula](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-suma-nula).

**Véase también:** [Adición natural](#gl-adicion-natural), [Cero](#gl-cero), [Predecesor](#gl-predecesor).

---
