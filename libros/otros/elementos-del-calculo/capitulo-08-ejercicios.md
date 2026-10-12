---
title: Capítulo 8 — Ejercicios
status: published
draft: false
book-id: MA-BOK-0015
editorial-project: EDC
date-modified: '2026-10-12'
license: GFDL-1.3-or-later
areas:
  - calculo
  - analisis
  - fundamentos
level: intermedio
topics:
  - calculo-de-una-variable
  - historia-de-las-matematicas
number-sections: false
provenance:
  type: original
  sources:
    - role: idea
      note: 'Inspiración metodológica: Gabor Toth, Elements of Mathematics (2021); obra independiente.'
source-id: EDC-C08-EJERCICIOS
source-sha256: 06a5403f08f94fd265886f3197ccaafc601f29e0cddfa34246d6941d3d246018
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-08.html) · [Ejercicios](capitulo-08-ejercicios.html) · [Soluciones](capitulo-08-soluciones.html) · [Notas históricas](capitulo-08-notas.html)

Se utilizarán únicamente C00–C08. No se invocará un desarrollo de Taylor aún no probado (C09), ni se extrapolarán identidades válidas para $|x|<R$ a los puntos fronterizos sin una prueba adicional. Cada ejercicio posee una solución razonada independiente con idéntico número.

## A. El significado de sumar infinitamente

**Ejercicio 8.1 (`EDC-C08-EXR-001`).** Para $a_n=(-1)^n$, determine $S_0,S_1,S_2,S_3$ y explique por qué $\sum_{n=0}^{\infty}a_n$ no converge, aunque se pueda escribir la identidad geométrica finita para $q=-1$.

**Ejercicio 8.2 (`EDC-C08-EXR-002`).** Reformule el criterio de Cauchy para la serie $\sum_{n=1}^{\infty}a_n$. ¿Por qué controlar un solo sumando $a_n$ no equivale a controlar todas las colas $\sum_{k=p}^{q}a_k$?

**Ejercicio 8.3 (`EDC-C08-EXR-003`).** Demuestre que $a_n\to0$ es condición necesaria pero no suficiente para que $\sum a_n$ converja. Elija un ejemplo y pruebe la divergencia de su serie.

**Ejercicio 8.4 (`EDC-C08-EXR-004`).** Calcule $\sum_{n=0}^{\infty}(-1/2)^n$ y el error absoluto al detenerse en $n=N$. Indique qué hipótesis hace legítimo usar el Teorema 8.2.

**Ejercicio 8.5 (`EDC-C08-EXR-005`).** Refute el uso de la fórmula $\sum_{n\ge0}q^n=1/(1-q)$ para $q=1$ y $q=-1$. En cada caso exhiba las sumas parciales.

**Ejercicio 8.6 (`EDC-C08-EXR-006`).** Para $\sum_{n=0}^{\infty}3^{-n}=3/2$, determine el menor entero $N\ge0$ para el cual la suma hasta $n=N$ tiene error menor que $1/1000$.

## B. Comparación y convergencia de series numéricas

**Ejercicio 8.7 (`EDC-C08-EXR-007`).** Pruebe mediante bloques diádicos que $\sum_{n=1}^{\infty}1/n^2$ converge. Obtenga además una cota sencilla para el bloque de índices $2^k\le n<2^{k+1}$.

**Ejercicio 8.8 (`EDC-C08-EXR-008`).** Determine si $\sum_{n=1}^{\infty}n^{-3/4}$ converge y justifique por comparación con una serie estudiada.

**Ejercicio 8.9 (`EDC-C08-EXR-009`).** Calcule exactamente $\sum_{n=1}^{\infty}1/[n(n+1)]$ por sumas telescópicas y justifique el paso al límite.

**Ejercicio 8.10 (`EDC-C08-EXR-010`).** Pruebe que $\sum_{n=1}^{\infty}1/(n^2+1)$ converge sin hallar su suma. Señale explícitamente la serie de comparación.

**Ejercicio 8.11 (`EDC-C08-EXR-011`).** Estudie la convergencia absoluta de $\sum_{n=1}^{\infty}(-1)^n/n^2$ y explique por qué ello permite reordenar sus términos.

**Ejercicio 8.12 (`EDC-C08-EXR-012`).** Para la serie armónica alternante $\sum_{n=1}^{\infty}(-1)^{n-1}/n$, demuestre convergencia condicional y encuentre una cota numérica del error tras sumar los primeros cien términos.

**Ejercicio 8.13 (`EDC-C08-EXR-013`).** Pruebe $\sum_{n=0}^{\infty}(-1)^n/(2n+1)=\pi/4$ integrando una identidad geométrica **finita**, y estime el error del procedimiento con $N+1$ términos.

**Ejercicio 8.14 (`EDC-C08-EXR-014`).** Explique por qué una reordenación de la serie armónica alternante puede cambiar su suma. Diseñe el procedimiento de sobrepasos que permita aproximar el valor objetivo $L=1$ y justifique que consume todos los términos.

## C. Tests de razón y raíz

**Ejercicio 8.15 (`EDC-C08-EXR-015`).** Estudie $\sum_{n=1}^{\infty}n/2^n$ mediante el criterio de razón. Después calcule su suma a partir de una función racional obtenida por derivación de una serie de potencias.

**Ejercicio 8.16 (`EDC-C08-EXR-016`).** Determine la convergencia de $\sum_{n=1}^{\infty}n!/3^n$ usando los cocientes consecutivos; compruebe también la condición necesaria sobre sus términos.

**Ejercicio 8.17 (`EDC-C08-EXR-017`).** Muestre que tanto $1/n$ como $1/n^2$ producen límite de razón igual a $1$, pero que sus series tienen comportamientos diferentes. ¿Qué informa realmente un resultado $L=1$?

## D. Radios y fronteras

**Ejercicio 8.18 (`EDC-C08-EXR-018`).** Encuentre radio, intervalo completo de convergencia y función suma de $\sum_{n=0}^{\infty}(2x)^n$.

**Ejercicio 8.19 (`EDC-C08-EXR-019`).** Determine el radio de $\sum_{n=0}^{\infty}n!x^n$ y analice qué sucede en su centro.

**Ejercicio 8.20 (`EDC-C08-EXR-020`).** Demuestre que $\sum_{n=0}^{\infty}x^n/n!$ converge absolutamente para todo $x\in\mathbb R$ y determine su radio. No utilice C09 para demostrar la respuesta.

**Ejercicio 8.21 (`EDC-C08-EXR-021`).** Determine con prueba independiente la convergencia de $\sum_{n=1}^{\infty}x^n/n$ en $|x|<1$, en $x=1$ y en $x=-1$.

**Ejercicio 8.22 (`EDC-C08-EXR-022`).** Determine la convergencia absoluta de $\sum_{n=1}^{\infty}x^n/n^2$ en $[-1,1]$ y la divergencia para $|x|>1$. Explique qué permite concluir sobre las fronteras.

## E. Operar correctamente dentro del radio

**Ejercicio 8.23 (`EDC-C08-EXR-023`).** Para $F(x)=\sum_{n\ge0}x^n$ sobre $|x|<1$, use la cota del Teorema 8.8 con $r=1/2$, $s=3/4$ para dar un límite explícito al error de truncamiento en $|x|\le1/2$. Compárelo con el error geométrico exacto.

**Ejercicio 8.24 (`EDC-C08-EXR-024`).** Justifique desde el Teorema 8.9, **no** por manipulación formal, la igualdad $\sum_{n=1}^{\infty}nx^{n-1}=1/(1-x)^2$ para $|x|<1$.

**Ejercicio 8.25 (`EDC-C08-EXR-025`).** Integre término a término la serie geométrica de razón $-x$ para demostrar $\ln(1+x)=\sum_{n=1}^{\infty}(-1)^{n-1}x^n/n$ en $|x|<1$. ¿Por qué esta prueba no decide por sí sola la igualdad en $x=1$?

**Ejercicio 8.26 (`EDC-C08-EXR-026`).** Obtenga la serie de $\arctan x$ en $|x|<1$, y luego pruebe el valor especial en $x=1$ controlando el resto integrado de la fórmula geométrica finita.

**Ejercicio 8.27 (`EDC-C08-EXR-027`).** Multiplique dos veces la serie geométrica $\sum_{n\ge0}x^n$ usando el producto de Cauchy y demuestre $\sum_{k=0}^{\infty}(k+1)x^k=(1-x)^{-2}$, especificando el dominio.

**Ejercicio 8.28 (`EDC-C08-EXR-028`).** Una serie de potencias centrada en cero tiene radio positivo y representa $F(x)=x/(1-x)$ cerca de cero. Determine todos sus coeficientes y justifique su unicidad.

**Ejercicio 8.29 (`EDC-C08-EXR-029`).** Integre la serie geométrica en $[0,1/2]$ y pruebe $\sum_{n=1}^{\infty}1/(n2^n)=\ln 2$. Indique por qué el intervalo de integración está estrictamente dentro del radio.

## F. Problema de síntesis

**Ejercicio 8.30 (`EDC-C08-EXR-030`).** Defina $H(x)=\sum_{n=1}^{\infty}(-1)^{n-1}x^n/n$ para $|x|<1$. (a) Demuestre que $H'(x)=1/(1+x)$ y $H(0)=0$. (b) Identifique $H$ sin acudir a un desarrollo de Taylor de una función previamente dada. (c) Justifique que

$$
\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n(n+1)2^{n+1}}
=\frac32\ln\frac32-\frac12.
$$

Indique qué estimación asegura la legalidad de integrar el desarrollo en el intervalo $[0,1/2]$.

---

**Correspondencia:** los identificadores `EDC-C08-EXR-001--030` remiten a las resoluciones independientes `EDC-C08-SOL-001--030` en [EDC-C08-SOLUCIONES](capitulo-08-soluciones.html).
