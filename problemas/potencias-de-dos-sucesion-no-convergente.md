---
title: "Una sucesión que vale uno en las potencias de dos no converge"
description: "Prueba directa mediante la definición épsilon-N, con dos índices consecutivos arbitrariamente grandes."
content-id: MA-PRB-0008
content-type: problem
collection: PM-PRB
status: published
date-created: 2026-09-18
date-modified: 2026-09-18
areas:
  - analisis
level: fundamental
difficulty: 2
topics:
  - convergencia
  - sucesiones
  - definicion-epsilon-N
techniques:
  - contradiccion
  - abrir-definiciones
prerequisites: []
related:
  - MA-PRB-0007
solution-status: complete
provenance:
  type: adapted
  sources:
    - "W. T. Gowers, Analysis 1 Examples Sheet 1 (Lent 2015), problema 2, p. 1; https://dec41.user.srcf.net/notes/IA_L/analysis_i_eg.pdf (archivo de Dexter Chua)."
license: GFDL-1.3-or-later
---

## Enunciado

Sea $(a_n)$ una sucesión que toma valor $1$ en los índices que son potencias positivas de $2$ y valor $0$ en los demás. Demuestra directamente, utilizando la definición de convergencia, que $(a_n)$ no tiene límite real.

*Fuente del problema:* hoja 1, n.º 2, p. 1 de las [hojas de Analysis I](https://dec41.user.srcf.net/notes/IA_L/analysis_i_eg.pdf). La posible convención para el primer término no afecta al argumento.

## Análisis

Decir que la sucesión alcanza tanto $0$ como $1$ infinitas veces es una intuición correcta, pero la petición exige trabajar con los cuantificadores de la definición. Si existiera un límite $L$, desde un índice $N$ suficientemente grande todos los términos tendrían que distar menos de $1/3$ de $L$. Mostraremos que siempre hay después de $N$ dos términos que distan exactamente $1$ entre sí.

## Solución

Supongamos, en busca de una contradicción, que $a_n\to L$ para algún $L\in\mathbb R$.

Por la definición de convergencia, con $\varepsilon=1/3$ existe $N\in\mathbb N$ tal que

$$
n\ge N\quad\Longrightarrow\quad |a_n-L|<\frac13.
$$

Elijamos $k\ge1$ de manera que $2^k\ge N$. Tanto $2^k$ como $2^k+1$ son, entonces, mayores o iguales que $N$. Además,

$$
2^k<2^k+1<2^{k+1},
$$

por lo que $2^k+1$ no es una potencia de $2$. Así,

$$
a_{2^k}=1,\qquad a_{2^k+1}=0.
$$

Aplicando la desigualdad triangular y la condición de convergencia a los dos índices, obtenemos

$$
\begin{aligned}
1
&=|a_{2^k}-a_{2^k+1}|\\
&\le |a_{2^k}-L|+|a_{2^k+1}-L|\\
&<\frac13+\frac13=\frac23.
\end{aligned}
$$

Esto es imposible. En consecuencia, **la sucesión no converge**.

## Comprobación

Los dos índices empleados pueden elegirse después de cualquier umbral $N$. La contradicción expresa que dos valores separados por distancia $1$ no pueden encontrarse simultáneamente a menos de $1/3$ de un mismo número real.

Otra prueba posible consiste en observar que $a_{2^k}=1$ y $a_{2^k+1}=0$ son subsucesiones con límites distintos; la demostración anterior, sin embargo, satisface la exigencia de partir directamente de la definición.

::: {.ma-block .ma-comprobacion}
**Técnica reutilizable.** Para probar que una sucesión no converge con la definición, identifica un $\varepsilon>0$ que ninguna cola pueda satisfacer respecto de un único límite hipotético.
:::

## Procedencia

Problema inspirado en W. T. Gowers, *Analysis 1 Examples Sheet 1*, n.º 2 (2015), disponible en el archivo de Dexter Chua. El análisis, la formulación de trabajo y la solución son propios de Matemática Abierta; no se reproduce la hoja completa.
