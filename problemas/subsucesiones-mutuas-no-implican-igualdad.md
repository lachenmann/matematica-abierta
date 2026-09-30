---
title: "¿Pueden dos sucesiones distintas ser subsucesiones una de otra?"
description: "Un contraejemplo muestra que la condición de subsucesiones mutuas no implica igualdad término a término."
content-id: MA-PRB-0007
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
  - sucesiones
  - subsucesiones
  - contraejemplos
techniques:
  - construir-contraejemplos
  - verificar-definiciones
prerequisites: []
related:
  - MA-PRB-0008
solution-status: complete
provenance:
  type: adapted
  sources:
    - "W. T. Gowers, Analysis 1 Examples Sheet 1 (Lent 2015), problema 1, p. 1; https://dec41.user.srcf.net/notes/IA_L/analysis_i_eg.pdf (archivo de Dexter Chua)."
license: GFDL-1.3-or-later
---

## Enunciado

Considera dos sucesiones reales tales que cada una es una subsucesión de la otra. ¿Deben coincidir término a término? Razona tu respuesta.

*Fuente del problema:* hoja 1, n.º 1, p. 1 de las [hojas de Analysis I](https://dec41.user.srcf.net/notes/IA_L/analysis_i_eg.pdf). Se presenta una formulación breve propia; la fuente contiene el enunciado original.

## Análisis

La relación «ser subsucesión» exige una aplicación de índices estrictamente creciente, pero no exige conservar todos los índices. Por tanto, conviene buscar un contraejemplo insertando un término repetido en una sucesión periódica y verificar **ambas** relaciones con funciones de índices explícitas.

## Solución

Tomemos

$$
(a_n)=(0,1,0,1,0,1,\ldots),
\qquad
(b_n)=(0,0,1,0,1,0,1,\ldots).
$$

Definamos

$$
\phi(1)=1,\qquad \phi(n)=n+1\quad(n\ge2).
$$

La aplicación $\phi:\mathbb N\to\mathbb N$ es estrictamente creciente: $\phi(1)=1<3=\phi(2)$, y para $n\ge2$ se cumple $\phi(n+1)=n+2>n+1=\phi(n)$.

Al seleccionar de $(b_n)$ los índices $1,3,4,5,\ldots$, obtenemos

$$
(b_{\phi(n)})_{n\ge1}=(0,1,0,1,\ldots)=(a_n)_{n\ge1}.
$$

Por consiguiente, $(a_n)$ es una subsucesión de $(b_n)$. En sentido inverso, los mismos índices en $(a_n)$ dan

$$
(a_{\phi(n)})_{n\ge1}=(0,0,1,0,1,\ldots)=(b_n)_{n\ge1}.
$$

Luego $(b_n)$ también es una subsucesión de $(a_n)$. Sin embargo,

$$
a_2=1\ne0=b_2.
$$

Por tanto, **dos sucesiones pueden ser subsucesiones una de otra sin ser idénticas**.

## Comprobación

No basta comprobar que ambos conjuntos de valores son $\{0,1\}$: lo exigido es conservar el orden y usar índices estrictamente crecientes. La construcción verifica exactamente esas dos condiciones en ambas direcciones.

::: {.ma-block .ma-comprobacion}
**Técnica reutilizable.** Para refutar una implicación entre propiedades de sucesiones, construye un contraejemplo y verifica explícitamente las funciones que seleccionan los índices. Encontrar dos sucesiones «parecidas» no es suficiente.
:::

## Procedencia

Problema inspirado en W. T. Gowers, *Analysis 1 Examples Sheet 1*, n.º 1 (2015), disponible en el archivo de Dexter Chua. El análisis, la formulación de trabajo y la solución son propios de Matemática Abierta; no se reproduce la hoja completa.
