---
content-id: MA-BCH-0327
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-031-EJERCICIOS
book-id: MA-BOK-0010
status: published
solution-status: complete
date-created: '2026-10-11'
areas:
- analisis
level: universitario
topics:
- analisis-real
prerequisites: []
related:
- MA-BOK-0010
license: GFDL-1.3-or-later
title: Ejercicios — Capítulo 31
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C31_EJERCICIOS.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 31](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html) · [Ejercicios](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-microcontroles.html)

Cinco problemas por sección. Las soluciones están en ANM-C31_SOLUCIONES.md.

## 31.1. Dar destino a todas las sucesiones de Cauchy

### Ejercicio 1

[]{#MA-EX-ANM-01-031-001}

Prueba que un espacio métrico finito es completo, sin suponer que su métrica sea discreta.

### Ejercicio 2

[]{#MA-EX-ANM-01-031-002}

Decide si $(0,1]$ con distancia usual es completo, y acredita todos los pasos del contraejemplo.

### Ejercicio 3

[]{#MA-EX-ANM-01-031-003}

Sea $X$ completo y $a\in X$. Prueba que la bola cerrada $C(a,r)$, $r\ge0$, es completa.

### Ejercicio 4

[]{#MA-EX-ANM-01-031-004}

Sea $T\ne\varnothing$ y $(f_n)$ Cauchy en $\mathcal B(T)$. Explica por qué no es legítimo escribir primero $D_\infty(f_n,f)$ sin acreditar que $f$ es acotada, y completa la prueba.

### Ejercicio 5

[]{#MA-EX-ANM-01-031-005}

Sea $Y$ un subespacio completo de $X$. Demuestra que es cerrado declarando exactamente la selección requerida.

## 31.2. Encerrar un destino y construirlo por iteración

### Ejercicio 6

[]{#MA-EX-ANM-01-031-006}

En $\mathbb R$ considera $F_n=[1-2^{-n},1+2^{-n}]$, $n\ge0$. Encuentra la intersección y acredita el teorema de recintos.

### Ejercicio 7

[]{#MA-EX-ANM-01-031-007}

Con $T(x)=(x+1)/2$ en $[0,1]$ y $x_0=0$, calcula la iteración y el primer corte para error estrictamente menor que $1/16$.

### Ejercicio 8

[]{#MA-EX-ANM-01-031-008}

Para una contracción de razón $q\in[0,1)$, prueba la cota a posteriori $d(x_n,a)\le d(x_n,x_{n+1})/(1-q)$.

### Ejercicio 9

[]{#MA-EX-ANM-01-031-009}

Muestra que la misma contracción $T(x)=(x+1)/2$ en $(0,1)$ no tiene punto fijo, aunque lleve el espacio a sí mismo.

### Ejercicio 10

[]{#MA-EX-ANM-01-031-010}

Verifica que $T(x)=x+1/x$ en $[1,\infty)$ reduce estrictamente las distancias de pares distintos y carece de punto fijo.

## 31.3. Cubrir con pocas bolas a cada escala

### Ejercicio 11

[]{#MA-EX-ANM-01-031-011}

Construye para $(0,1)$ una red de radio $\varepsilon>0$ con centros interiores.

### Ejercicio 12

[]{#MA-EX-ANM-01-031-012}

Prueba que en un espacio discreto la acotación total equivale a finitud.

### Ejercicio 13

[]{#MA-EX-ANM-01-031-013}

Sea $A\subset X$ y $X$ totalmente acotado. Justifica una red para $A$ con centros en $A$.

### Ejercicio 14

[]{#MA-EX-ANM-01-031-014}

En $[-1,1]^2$ con $d_\infty$, construye una red de radio $1/3$ usando una malla explícita.

### Ejercicio 15

[]{#MA-EX-ANM-01-031-015}

Prueba que una sucesión con $d(x_n,x_m)\ge\eta>0$ para índices distintos impide acotación total.

## 31.4. Compacidad: reducir cualquier cobertura

### Ejercicio 16

[]{#MA-EX-ANM-01-031-016}

Prueba que una unión finita de compactos en un espacio métrico es compacta.

### Ejercicio 17

[]{#MA-EX-ANM-01-031-017}

En la discreta sobre $\mathbb N$, exhibe una cobertura abierta que refute compacidad.

### Ejercicio 18

[]{#MA-EX-ANM-01-031-018}

Deduce la propiedad de intersección finita de la compacidad usando complementos.

### Ejercicio 19

[]{#MA-EX-ANM-01-031-019}

Prueba directamente que un compacto métrico es completo usando clausuras de colas.

### Ejercicio 20

[]{#MA-EX-ANM-01-031-020}

Sea $K\ne\varnothing$ compacto y $a\notin K$. Prueba que $\inf_{k\in K}d(a,k)>0$ sin suponer un mínimo alcanzado.

## 31.5. La equivalencia métrica y sus elecciones

### Ejercicio 21

[]{#MA-EX-ANM-01-031-021}

Explica por qué una extracción en redes de radios $2^{-j}$ produce una subsucesión de Cauchy y qué selecciones emplea.

### Ejercicio 22

[]{#MA-EX-ANM-01-031-022}

Supón que ninguna red finita de radio $\varepsilon$ cubre $X$. Construye una sucesión separada, declarando la regla de selección.

### Ejercicio 23

[]{#MA-EX-ANM-01-031-023}

Prueba que un espacio secuencialmente compacto es completo sin fabricar otra sucesión.

### Ejercicio 24

[]{#MA-EX-ANM-01-031-024}

Para la cobertura de $[0,1]$ por $U=(-1,3/4)$ y $V=(1/4,2)$, verifica un número de Lebesgue en forma de bolas relativas.

### Ejercicio 25

[]{#MA-EX-ANM-01-031-025}

En un compacto, ¿toda sucesión converge? Da una refutación y dos subsucesiones.

## 31.6. Transportar compacidad por continuidad

### Ejercicio 26

[]{#MA-EX-ANM-01-031-026}

Sea $f:K\to Y$ continua y $K$ compacto. Prueba compacidad de $f(K)$ conservando los índices de una cobertura.

### Ejercicio 27

[]{#MA-EX-ANM-01-031-027}

Una función continua $f:K\to\mathbb R$ sobre un compacto no vacío alcanza supremo. Prueba el paso de supremo a valor alcanzado.

### Ejercicio 28

[]{#MA-EX-ANM-01-031-028}

Reconstruye la continuidad uniforme de una continua sobre un compacto sin elegir una función de radios sobre todos los puntos.

### Ejercicio 29

[]{#MA-EX-ANM-01-031-029}

Sea $f:K\to Y$ una biyección continua, $K$ compacto y $Y$ métrico. Prueba continuidad de su inversa.

### Ejercicio 30

[]{#MA-EX-ANM-01-031-030}

Clasifica $K=\{(x,y):\max(|x|,|y|)\le1\}$ en $\mathbb R^2$ con $d_\infty$: completitud, compacidad y conexidad por caminos.

## 31.7. Conexidad: impedir una separación

### Ejercicio 31

[]{#MA-EX-ANM-01-031-031}

Prueba que conexidad equivale a que los únicos subconjuntos abiertos y cerrados sean el vacío y el espacio.

### Ejercicio 32

[]{#MA-EX-ANM-01-031-032}

En $A=[-2,-1]\cup[1,2]$ usual, acredita compacidad y una separación relativa.

### Ejercicio 33

[]{#MA-EX-ANM-01-031-033}

Sea $X$ conexo y $f:X\to\{0,1\}$ continua con codominio discreto. Prueba que $f$ es constante.

### Ejercicio 34

[]{#MA-EX-ANM-01-031-034}

Prueba que la imagen real de una función continua sobre un conexo contiene todos los valores entre dos de sus valores.

### Ejercicio 35

[]{#MA-EX-ANM-01-031-035}

Prueba que una unión de conjuntos conexos con un punto común es conexa.

## 31.8. Comparar lo que sobrevive y cerrar la ruta

### Ejercicio 36

[]{#MA-EX-ANM-01-031-036}

Clasifica $(\mathbb R,d_*)$, $d_*(x,y)=\min(|x-y|,1)$: acotación, completitud, compacidad y conexidad.

### Ejercicio 37

[]{#MA-EX-ANM-01-031-037}

Con esa métrica truncada en el dominio, refuta continuidad uniforme de $f(x)=x^2$ hacia la recta usual.

### Ejercicio 38

[]{#MA-EX-ANM-01-031-038}

Clasifica la métrica $e(x,y)=|\phi(x)-\phi(y)|$ en $\mathbb R$, $\phi(x)=x/(1+|x|)$, sin confundir topología y completitud.

### Ejercicio 39

[]{#MA-EX-ANM-01-031-039}

Supón $c d\le e\le C d$ con $c,C>0$. Prueba preservación de acotación total y completitud.

### Ejercicio 40

[]{#MA-EX-ANM-01-031-040}

¿Qué propiedades conserva necesariamente un homeomorfismo entre espacios métricos? Justifica compacidad y conexidad y refuta completitud.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 31](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html) · [Ejercicios](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-microcontroles.html)
