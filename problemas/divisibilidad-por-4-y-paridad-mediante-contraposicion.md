---
title: "Divisibilidad por 4 y paridad mediante contraposición"
description: "Demostrar que si 4 divide el cuadrado de un entero, entonces ese entero es par, eligiendo la contraposición como estrategia."
content-id: MA-PRB-0003
content-type: problem
collection: PM-PRB
status: published
date-created: 2026-09-07
date-modified: 2026-09-07
areas:
  - fundamentos
  - teoria-de-numeros
level: fundamental
difficulty: 2
topics:
  - divisibilidad
  - paridad
  - demostraciones
  - contraposicion
techniques:
  - contraposicion
  - abrir-definiciones
prerequisites:
  - MA-BCH-0001
related: []
solution-status: complete
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

## Enunciado

Sea $n\in\mathbb Z$. Demuestra que

$$
4\mid n^2
\quad\Longrightarrow\quad
n\text{ es par}.
$$

## Análisis

Una tentación sería interpretar informalmente $4\mid n^2$ como si pudiéramos «extraer raíces» en una relación de divisibilidad. Esa maniobra no está justificada.

Conviene mirar la forma lógica. La conclusión es «$n$ es par». Su negación dentro de los enteros es «$n$ es impar», y esa negación tiene una representación algebraica muy concreta:

$$
n=2k+1
$$

para algún $k\in\mathbb Z$.

Por eso resulta natural utilizar la técnica de [contraposición](../libros/capitulos/leer-y-escribir-matematicas-proposiciones-cuantificadores-y-demostraciones.md#met-ma-bch-0001-directa-contraposicion).

La contrapositiva es:

> Si $n$ es impar, entonces $4\nmid n^2$.

## Solución

Supongamos que $n$ es impar. Entonces existe $k\in\mathbb Z$ tal que

$$
n=2k+1.
$$

Elevando al cuadrado,

$$
\begin{aligned}
n^2
&=(2k+1)^2\\
&=4k^2+4k+1\\
&=4(k^2+k)+1.
\end{aligned}
$$

Como $k^2+k\in\mathbb Z$, el número $n^2$ tiene la forma

$$
4q+1
$$

para algún $q\in\mathbb Z$. En particular, no puede ser divisible por $4$.

Hemos demostrado

$$
n\text{ impar}
\quad\Longrightarrow\quad
4\nmid n^2.
$$

Ésta es la contrapositiva del enunciado original. Por tanto,

$$
\boxed{
4\mid n^2
\quad\Longrightarrow\quad
n\text{ es par}.
}
$$

## Comprobación

La prueba hace visible el mecanismo. Si $n$ es impar, su cuadrado siempre puede escribirse como

$$
4q+1,
$$

de modo que deja una unidad después de retirar un múltiplo de $4$.

Por ejemplo,

$$
3^2=9=4\cdot2+1,
\qquad
5^2=25=4\cdot6+1.
$$

Los ejemplos no reemplazan la demostración, pero confirman la estructura obtenida.

::: {.ma-block .ma-comprobacion}
**Técnica reutilizable**

Cuando la conclusión de una implicación tiene una negación que puede parametrizarse de forma útil, la contraposición puede convertir una prueba difícil en un cálculo estructurado.
:::

## Relaciones

- **Capítulo:** [Leer y escribir matemáticas](../libros/capitulos/leer-y-escribir-matematicas-proposiciones-cuantificadores-y-demostraciones.md) (`MA-BCH-0001`).
- **Técnica principal:** contraposición.
