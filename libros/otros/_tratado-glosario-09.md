## Asociatividad del producto {#gl-asociatividad-producto}

**Idea.** Al multiplicar tres naturales, la forma de agrupar los factores no modifica el resultado.

**En este tratado.** Para $a,b,c\in\mathbb N$,

$$
(ab)c=a(bc).
$$

La propiedad se demuestra por inducción a partir de la definición recursiva del producto y de la distributividad.

**En el Tratado:** [Teorema 1.5.6 — Asociatividad del producto](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-asociatividad-producto).

**Véase también:** [Multiplicación natural](#gl-multiplicacion-natural), [Distributividad](#gl-distributividad-producto), [Principio de inducción](#gl-principio-induccion).

---

## Conmutatividad del producto {#gl-conmutatividad-producto}

**Idea.** El orden de los factores no altera el producto.

**En este tratado.** Para $a,b\in\mathbb N$,

$$
ab=ba.
$$

Como en la suma, la conmutatividad no forma parte de la definición recursiva: se obtiene después como teorema.

**En el Tratado:** [Teorema 1.5.7 — Conmutatividad del producto](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-conmutatividad-producto).

**Véase también:** [Multiplicación natural](#gl-multiplicacion-natural), [Asociatividad del producto](#gl-asociatividad-producto), [Principio de inducción](#gl-principio-induccion).

---

## Distributividad {#gl-distributividad-producto}

**Idea.** Multiplicar una suma equivale a distribuir el factor sobre cada uno de sus sumandos.

**En este tratado.** Para $a,b,c\in\mathbb N$,

$$
a(b+c)=ab+ac,
\qquad
(a+b)c=ac+bc.
$$

Primero se demuestra la distributividad en el segundo factor mediante inducción; la otra forma se obtiene después usando la conmutatividad del producto.

**En el Tratado:** [Teorema 1.5.5 — Distributividad en el segundo factor](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-distributividad-producto-segundo-factor) y [Corolario 1.5.8 — Distributividad en ambos lados](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-distributividad-ambos-lados).

**Véase también:** [Multiplicación natural](#gl-multiplicacion-natural), [Adición natural](#gl-adicion-natural), [Conmutatividad del producto](#gl-conmutatividad-producto).

---

## Multiplicación natural {#gl-multiplicacion-natural}

**Idea.** La operación que, fijado un natural $m$, acumula una copia adicional de $m$ cada vez que avanzamos un paso en el segundo argumento.

**En este tratado.** El producto se define por recursión con parámetros como la única función

$$
\cdot:\mathbb N\times\mathbb N\to\mathbb N
$$

que satisface

$$
m\cdot0=0,
\qquad
m\cdot S(n)=m\cdot n+m.
$$

La recursión se realiza en el segundo argumento; las leyes de unidad, distributividad, asociatividad y conmutatividad se demuestran posteriormente.

**En el Tratado:** [Definición 1.5.1 — Multiplicación](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-multiplicacion-naturales).

**Véase también:** [Adición natural](#gl-adicion-natural), [Recursión con parámetros](#gl-recursion-parametros), [Números naturales](#gl-numeros-naturales).

---

## Producto nulo {#gl-producto-nulo}

**Idea.** Un producto de naturales es cero exactamente cuando alguno de sus factores es cero.

**En este tratado.** Para $a,b\in\mathbb N$,

$$
ab=0\iff a=0\text{ o }b=0.
$$

**En el Tratado:** [Proposición 1.5.9 — Producto nulo](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-producto-nulo).

**Véase también:** [Multiplicación natural](#gl-multiplicacion-natural), [Suma nula](#gl-suma-nula), [Cero](#gl-cero).

---

## Unidad multiplicativa {#gl-unidad-multiplicativa}

**Idea.** El natural $1$ no altera ningún natural al multiplicarlo, por cualquiera de los dos lados.

**En este tratado.** Para todo $m\in\mathbb N$,

$$
m\cdot1=m,
\qquad
1\cdot m=m.
$$

**En el Tratado:** [Proposición 1.5.4 — Leyes de la unidad](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-unidad-producto).

**Véase también:** [Multiplicación natural](#gl-multiplicacion-natural), [Uno](#gl-uno).

---
