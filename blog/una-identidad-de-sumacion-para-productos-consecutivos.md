---
title: "Una identidad de sumación para productos consecutivos: dos demostraciones"
description: "Una identidad finita para productos consecutivos, demostrada por inducción y por telescopaje mediante diferencias finitas."
content-id: MA-ART-0001
content-type: article
status: published
date-created: 2026-09-07
date-modified: 2026-09-07
areas:
  - calculo
  - matematica-discreta
level: introductorio
topics:
  - sumas-finitas
  - productos-consecutivos
  - factoriales
  - induccion-matematica
  - sumas-telescopicas
  - diferencias-finitas
prerequisites: []
related: []
provenance:
  type: synthesis
  sources:
    - cite: pan2023measure
      locator: "Appendix A.1, Proposition A.1, pp. 905–906"
      role: statement
      note: "Fuente de la identidad."
    - cite: pan2023measure
      locator: "Appendix A.1, Proposition A.1, pp. 905–906"
      role: proof
      note: "La primera demostración reconstruye en redacción propia el argumento inductivo de Pan."
license: GFDL-1.3-or-later
---

Hay identidades cuya primera demostración confirma que una fórmula es cierta, mientras que una segunda demostración permite entender **por qué tiene precisamente esa forma**. Éste es un ejemplo especialmente limpio.

::: {.ma-block .ma-enunciado}
**Identidad de sumación**

Para $n,m\in\mathbb Z_{\ge 0}$,

$$
\boxed{
\sum_{i=0}^{n}\prod_{j=1}^{m}(i+j)
=
\frac{1}{m+1}\frac{(n+m+1)!}{n!}
}
$$

con la convención usual de que un producto vacío vale $1$ cuando $m=0$.
:::

El producto del sumando tiene una forma muy concreta:

$$
\prod_{j=1}^{m}(i+j)
=(i+1)(i+2)\cdots(i+m)
=
\frac{(i+m)!}{i!}.
$$

Por tanto, la identidad también puede escribirse como

$$
\sum_{i=0}^{n}\frac{(i+m)!}{i!}
=
\frac{(n+m+1)!}{(m+1)n!}.
$$

::: {.ma-block .ma-fuente}
**Fuente y procedencia**

La identidad y una demostración por inducción aparecen en la Proposition A.1 del Appendix A.1 de Zigang Pan, *Measure-Theoretic Calculus in Abstract Spaces*, pp. 905–906 [@pan2023measure, pp. 905–906].

La primera demostración que sigue reconstruye ese argumento en redacción propia y desarrolla los pasos algebraicos. La segunda demostración, mediante diferencias finitas y telescopaje, es una elaboración independiente de **Matemática Abierta**.
:::

## Antes de demostrar: un caso familiar

Si $m=1$, entonces

$$
\prod_{j=1}^{1}(i+j)=i+1,
$$

y la identidad se reduce a

$$
\sum_{i=0}^{n}(i+1)
=
\frac12\frac{(n+2)!}{n!}
=
\frac{(n+1)(n+2)}2.
$$

Es decir,

$$
1+2+\cdots +(n+1)
=
\frac{(n+1)(n+2)}2.
$$

La fórmula general puede verse, por tanto, como una extensión de la suma de los primeros enteros a sumas de **productos consecutivos**.

## Primera demostración: inducción sobre $n$

Fijemos $m\in\mathbb Z_{\ge0}$ y demostremos la identidad por inducción en $n$.

### Caso base

Para $n=0$,

$$
\sum_{i=0}^{0}\prod_{j=1}^{m}(i+j)
=
\prod_{j=1}^{m}j
=
m!.
$$

Por otro lado,

$$
\frac{1}{m+1}\frac{(m+1)!}{0!}
=
m!.
$$

La fórmula vale para $n=0$.

### Hipótesis inductiva

Supongamos que para cierto $k\in\mathbb Z_{\ge0}$ se cumple

$$
\sum_{i=0}^{k}\prod_{j=1}^{m}(i+j)
=
\frac{1}{m+1}\frac{(k+m+1)!}{k!}.
$$

### Paso de $k$ a $k+1$

Separamos el último término:

$$
\sum_{i=0}^{k+1}\prod_{j=1}^{m}(i+j)
=
\sum_{i=0}^{k}\prod_{j=1}^{m}(i+j)
+
\prod_{j=1}^{m}(k+1+j).
$$

Aplicando la hipótesis inductiva y escribiendo el producto mediante factoriales,

$$
=
\frac{1}{m+1}\frac{(k+m+1)!}{k!}
+
\frac{(k+m+1)!}{(k+1)!}.
$$

Llevamos ambos términos al denominador común $(m+1)(k+1)!$:

$$
\begin{aligned}
&\frac{(k+1)(k+m+1)!}{(m+1)(k+1)!}
+
\frac{(m+1)(k+m+1)!}{(m+1)(k+1)!}\\[2mm]
&=
\frac{(k+m+2)(k+m+1)!}{(m+1)(k+1)!}\\[2mm]
&=
\frac{1}{m+1}\frac{(k+m+2)!}{(k+1)!}.
\end{aligned}
$$

Ésta es exactamente la fórmula con $n=k+1$. Por inducción, la identidad vale para todo $n\in\mathbb Z_{\ge0}$.

::: {.ma-block .ma-metodo}
**Qué hace funcionar la inducción**

Al pasar de la suma hasta $k$ a la suma hasta $k+1$, sólo aparece un término nuevo. La forma factorial de ese término encaja exactamente con la expresión dada por la hipótesis inductiva.
:::

## Segunda demostración: una antiderivada discreta

La segunda prueba cambia completamente de punto de vista.

Definamos

$$
F(i)
=
\frac{1}{m+1}\,i(i+1)\cdots(i+m).
$$

Calculemos su diferencia finita:

$$
\Delta F(i):=F(i+1)-F(i).
$$

Tenemos

$$
F(i+1)
=
\frac{1}{m+1}(i+1)(i+2)\cdots(i+m+1),
$$

y

$$
F(i)
=
\frac{1}{m+1}i(i+1)\cdots(i+m).
$$

Factorizando los términos comunes,

$$
\begin{aligned}
F(i+1)-F(i)
&=
\frac{(i+1)\cdots(i+m)}{m+1}
\bigl[(i+m+1)-i\bigr]\\[1mm]
&=
(i+1)(i+2)\cdots(i+m)\\[1mm]
&=
\prod_{j=1}^{m}(i+j).
\end{aligned}
$$

Por tanto,

$$
\boxed{
\prod_{j=1}^{m}(i+j)=F(i+1)-F(i).
}
$$

Ahora la suma completa se convierte en

$$
\sum_{i=0}^{n}\prod_{j=1}^{m}(i+j)
=
\sum_{i=0}^{n}\bigl(F(i+1)-F(i)\bigr).
$$

Al desarrollar,

$$
[F(1)-F(0)]+[F(2)-F(1)]+\cdots+[F(n+1)-F(n)],
$$

todos los términos interiores se cancelan. Queda

$$
F(n+1)-F(0).
$$

Como $F(0)=0$,

$$
\begin{aligned}
\sum_{i=0}^{n}\prod_{j=1}^{m}(i+j)
&=F(n+1)\\[1mm]
&=
\frac{1}{m+1}(n+1)(n+2)\cdots(n+m+1)\\[1mm]
&=
\frac{1}{m+1}\frac{(n+m+1)!}{n!}.
\end{aligned}
$$

Y obtenemos de nuevo la identidad.

::: {.ma-block .ma-intuicion}
**La estructura que revela la segunda prueba**

La expresión

$$
\prod_{j=1}^{m}(i+j)
$$

es la **diferencia finita** de otra expresión más simple:

$$
\Delta F(i)=F(i+1)-F(i).
$$

Sumar diferencias finitas juega un papel análogo al de integrar una derivada. Por eso la suma telescopa: estamos realizando una forma de **integración discreta**.
:::

## Comprobación numérica

Tomemos $n=2$ y $m=2$. El lado izquierdo es

$$
(1\cdot2)+(2\cdot3)+(3\cdot4)
=2+6+12
=20.
$$

El lado derecho es

$$
\frac13\frac{5!}{2!}
=
\frac13\frac{120}{2}
=20.
$$

::: {.ma-block .ma-comprobacion}
**Control**

Ambas demostraciones llegan al mismo resultado, pero aportan información diferente:

- la **inducción** muestra cómo la fórmula se propaga de $n$ a $n+1$;
- el **telescopaje** explica la forma cerrada encontrando una antiderivada discreta del sumando.
:::

## Una idea reutilizable

Cuando aparezca una suma finita de la forma

$$
\sum_{i=a}^{b}u_i,
$$

vale la pena preguntarse si existe una sucesión $F$ tal que

$$
u_i=F(i+1)-F(i).
$$

Si existe, entonces

$$
\sum_{i=a}^{b}u_i
=
F(b+1)-F(a).
$$

Ésta es una de las formas fundamentales de las **sumas telescópicas** y constituye el análogo discreto del teorema fundamental del cálculo.
