---
title: "Existencia y unicidad en una ecuación lineal con parámetros"
description: "Separar existencia y unicidad al resolver una ecuación lineal dependiente de dos parámetros y localizar la hipótesis decisiva."
content-id: MA-PRB-0005
content-type: problem
collection: PM-PRB
status: published
date-created: 2026-09-07
date-modified: 2026-09-07
areas:
  - fundamentos
  - algebra
level: fundamental
difficulty: 2
topics:
  - existencia-y-unicidad
  - ecuaciones-lineales
  - parametros
  - demostraciones
  - control-de-hipotesis
techniques:
  - existencia-y-unicidad
  - factorizacion
  - control-de-hipotesis
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

Sean $a,b\in\mathbb R$ con

$$
a\ne b.
$$

Demuestra que existe un único $x\in\mathbb R$ tal que

$$
ax+b=bx+a.
$$

## Análisis

El enunciado contiene dos tareas independientes:

1. demostrar que existe al menos una solución;
2. demostrar que cualquier solución posible coincide con ella.

Antes de despejar, conviene probar valores estructuralmente simples. El candidato

$$
x=1
$$

hace que ambos miembros sean $a+b$.

Esto resuelve inmediatamente la existencia. La condición $a\ne b$ aparecerá al estudiar la unicidad.

## Solución

### Existencia

Tomemos

$$
x=1.
$$

Entonces

$$
a(1)+b=a+b=b+a=b(1)+a.
$$

Por tanto, $x=1$ es una solución.

### Unicidad

Sea $y\in\mathbb R$ una solución cualquiera. Entonces

$$
ay+b=by+a.
$$

Reordenamos:

$$
ay-by=a-b.
$$

Factorizando,

$$
(a-b)y=a-b.
$$

La hipótesis $a\ne b$ implica

$$
a-b\ne0.
$$

Podemos dividir ambos miembros por $a-b$ y obtener

$$
y=1.
$$

Toda solución coincide con el candidato ya encontrado. En consecuencia,

$$
\boxed{x=1}
$$

es la única solución.

## Comprobación

La hipótesis $a\ne b$ merece un control específico.

Si la eliminamos y tomamos $a=b$, la ecuación queda

$$
ax+a=ax+a,
$$

que es verdadera para **todo** $x\in\mathbb R$.

Por tanto:

- $a\ne b$ no era necesaria para encontrar la solución $x=1$;
- sí era necesaria para garantizar que esa solución fuese única.

::: {.ma-block .ma-comprobacion}
**Técnica reutilizable**

En una prueba de existencia y unicidad, las hipótesis pueden desempeñar papeles distintos. Conviene registrar exactamente en cuál de las dos partes se utiliza cada una.
:::

## Relaciones

- **Capítulo:** [Leer y escribir matemáticas](../libros/capitulos/leer-y-escribir-matematicas-proposiciones-cuantificadores-y-demostraciones.md) (`MA-BCH-0001`).
- **Técnica principal:** existencia y unicidad.
