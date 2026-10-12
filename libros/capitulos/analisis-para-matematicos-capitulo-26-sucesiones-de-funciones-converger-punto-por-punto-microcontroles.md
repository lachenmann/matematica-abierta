---
content-id: MA-BCH-0309
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-026-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 26
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C26_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 26](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html) · [Ejercicios](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §26.1 — Dos índices, dos maneras de mirar

### Microcontrol 001

[]{#MA-MIC-ANM-01-026-001}

[]{#MA-MSOL-ANM-01-026-001}

[]{#MA-SEC-ANM-01-026-001}

**Pregunta.** ¿Qué queda fijo al mirar una columna?

**Solución.** La entrada $x\in X$; sólo varía el índice $n$, y los valores forman una sucesión real.

### Microcontrol 002

[]{#MA-MIC-ANM-01-026-002}

[]{#MA-MSOL-ANM-01-026-002}

**Pregunta.** ¿Qué objeto es una fila?

**Solución.** Una función $f_n:X\to\mathbb R$, obtenida al fijar el índice y dejar variar la entrada.

### Microcontrol 003

[]{#MA-MIC-ANM-01-026-003}

[]{#MA-MSOL-ANM-01-026-003}

**Pregunta.** ¿Por qué se declara un dominio común?

**Solución.** Para que toda columna esté definida en cada etapa y las comparaciones entre filas tengan el mismo tipo.

### Microcontrol 004

[]{#MA-MIC-ANM-01-026-004}

[]{#MA-MSOL-ANM-01-026-004}

**Pregunta.** ¿En qué producto vive el grafo de una fila?

**Solución.** En $X\times\mathbb R$. El índice ordena las filas, pero no es la variable horizontal de esa gráfica.

### Microcontrol 005

[]{#MA-MIC-ANM-01-026-005}

[]{#MA-MSOL-ANM-01-026-005}

**Pregunta.** ¿Qué garantiza salida única en el grafo del límite?

**Solución.** La unicidad del límite numérico de C06 para cada entrada donde converge la columna.

### Microcontrol 006

[]{#MA-MIC-ANM-01-026-006}

[]{#MA-MSOL-ANM-01-026-006}

**Pregunta.** ¿Debe converger toda columna de una familia dada?

**Solución.** No. En $(-1)^n x$, sólo la entrada0 tiene columna convergente.

### Microcontrol 007

[]{#MA-MIC-ANM-01-026-007}

[]{#MA-MSOL-ANM-01-026-007}

**Pregunta.** ¿Qué sucede si el dominio es vacío?

**Solución.** Existe una única función vacía y el contrato para todas las entradas es vacuo.

### Microcontrol 008

[]{#MA-MIC-ANM-01-026-008}

[]{#MA-MSOL-ANM-01-026-008}

**Pregunta.** ¿Bastan tres columnas dibujadas para probar convergencia en un intervalo?

**Solución.** No; hay que responder al contrato para una entrada arbitraria del intervalo.

## §26.2 — Una cola para cada entrada

### Microcontrol 009

[]{#MA-MIC-ANM-01-026-009}

[]{#MA-MSOL-ANM-01-026-009}

[]{#MA-SEC-ANM-01-026-002}

**Pregunta.** ¿De qué datos puede depender el corte puntual?

**Solución.** De la entrada fija $x$ y la tolerancia positiva $\varepsilon$, recibidas antes de construirlo.

### Microcontrol 010

[]{#MA-MIC-ANM-01-026-010}

[]{#MA-MSOL-ANM-01-026-010}

**Pregunta.** ¿Qué cuantificador sigue a la elección del corte?

**Solución.** El de todos los índices $n\ge N$; el error debe ser menor que la tolerancia en toda esa cola.

### Microcontrol 011

[]{#MA-MIC-ANM-01-026-011}

[]{#MA-MSOL-ANM-01-026-011}

**Pregunta.** ¿Qué debe permanecer fijo al refutar convergencia hacia una candidata?

**Solución.** Una entrada y una tolerancia; para cada corte se produce un índice tardío infractor.

### Microcontrol 012

[]{#MA-MIC-ANM-01-026-012}

[]{#MA-MSOL-ANM-01-026-012}

**Pregunta.** ¿Qué demuestra una entrada infractora que cambia con el corte?

**Solución.** Puede refutar un corte simultáneo para todas las entradas; por sí sola no refuta convergencia puntual.

### Microcontrol 013

[]{#MA-MIC-ANM-01-026-013}

[]{#MA-MSOL-ANM-01-026-013}

**Pregunta.** ¿Por qué dos funciones límite puntuales coinciden?

**Solución.** En cada entrada, dos cortes para un tercio de la distancia entre supuestos destinos contradicen la desigualdad triangular.

### Microcontrol 014

[]{#MA-MIC-ANM-01-026-014}

[]{#MA-MSOL-ANM-01-026-014}

**Pregunta.** ¿Cómo se reúnen los cortes de un conjunto finito de entradas?

**Solución.** Tomando su máximo finito, que domina todas las obligaciones de cola para la tolerancia fijada.

### Microcontrol 015

[]{#MA-MIC-ANM-01-026-015}

[]{#MA-MSOL-ANM-01-026-015}

**Pregunta.** ¿Cómo se define el umbral mínimo $\tau(x,\varepsilon)$?

**Solución.** Como el mínimo natural del conjunto no vacío de cortes que controlan toda la cola en esa entrada y tolerancia.

### Microcontrol 016

[]{#MA-MIC-ANM-01-026-016}

[]{#MA-MSOL-ANM-01-026-016}

**Pregunta.** ¿Qué ocurre con $\tau$ al disminuir la tolerancia?

**Solución.** No puede disminuir: cada corte válido para el desafío más exigente es válido para el menos exigente.

## §26.3 — Lo que se transporta columna por columna

### Microcontrol 017

[]{#MA-MIC-ANM-01-026-017}

[]{#MA-MSOL-ANM-01-026-017}

[]{#MA-SEC-ANM-01-026-003}

**Pregunta.** ¿Qué cota usa la prueba del producto?

**Solución.** Una cota eventual $|f_n(x)|\le|f(x)|+1$ en la entrada fijada; puede depender de ella.

### Microcontrol 018

[]{#MA-MIC-ANM-01-026-018}

[]{#MA-MSOL-ANM-01-026-018}

**Pregunta.** ¿Qué barrera necesita el recíproco?

**Solución.** $|g_n(x)|>|g(x)|/2$ en una cola, después de declarar $g(x)\ne0$.

### Microcontrol 019

[]{#MA-MIC-ANM-01-026-019}

[]{#MA-MSOL-ANM-01-026-019}

**Pregunta.** ¿Garantiza un denominador límite no nulo que todas las filas del cociente estén definidas?

**Solución.** No. Pueden tener ceros en índices iniciales distintos según la entrada; hace falta dominio común o reparación declarada.

### Microcontrol 020

[]{#MA-MIC-ANM-01-026-020}

[]{#MA-MSOL-ANM-01-026-020}

**Pregunta.** ¿Se hereda una desigualdad estricta eventual?

**Solución.** No necesariamente: números positivos pueden tender a cero. El orden débil sí pasa al límite.

### Microcontrol 021

[]{#MA-MIC-ANM-01-026-021}

[]{#MA-MSOL-ANM-01-026-021}

**Pregunta.** ¿Qué exige componer con una función exterior continua?

**Solución.** Que los valores de cada fila y el límite pertenezcan a su dominio, y continuidad en cada valor límite utilizado.

### Microcontrol 022

[]{#MA-MIC-ANM-01-026-022}

[]{#MA-MSOL-ANM-01-026-022}

**Pregunta.** ¿Qué acotación produce una columna convergente?

**Solución.** Una barrera para todos sus términos, formada por una cola acotada y el máximo de su prefijo finito.

### Microcontrol 023

[]{#MA-MIC-ANM-01-026-023}

[]{#MA-MSOL-ANM-01-026-023}

**Pregunta.** ¿Puede un límite puntual de filas acotadas ser no acotado?

**Solución.** Sí: $\min(n,x)$ en $[0,\infty)$ converge a $x$, sin cota global.

### Microcontrol 024

[]{#MA-MIC-ANM-01-026-024}

[]{#MA-MSOL-ANM-01-026-024}

**Pregunta.** ¿Qué sucede si todas las filas tienen una misma barrera de magnitud?

**Solución.** El límite la hereda entrada por entrada mediante preservación del orden.

## §26.4 — Potencias y una discontinuidad nueva

### Microcontrol 025

[]{#MA-MIC-ANM-01-026-025}

[]{#MA-MSOL-ANM-01-026-025}

[]{#MA-SEC-ANM-01-026-004}

**Pregunta.** ¿Cómo se define la etapa inicial de las potencias en cero?

**Solución.** Se declara $p_0=1$ en todo el dominio y se usa la recurrencia $p_{n+1}(x)=xp_n(x)$; no queda un símbolo ambiguo.

### Microcontrol 026

[]{#MA-MIC-ANM-01-026-026}

[]{#MA-MSOL-ANM-01-026-026}

**Pregunta.** ¿Cuál es el límite de las potencias en una entrada $0<x<1$?

**Solución.** Cero, pues con $t=1/x-1>0$ se tiene $x^n\le1/(1+nt)$.

### Microcontrol 027

[]{#MA-MIC-ANM-01-026-027}

[]{#MA-MSOL-ANM-01-026-027}

**Pregunta.** ¿Qué ocurre exactamente en uno?

**Solución.** Toda etapa vale1, por lo que el límite allí es1.

### Microcontrol 028

[]{#MA-MIC-ANM-01-026-028}

[]{#MA-MSOL-ANM-01-026-028}

**Pregunta.** ¿Dónde falla continuidad del límite en $[0,1]$?

**Solución.** En1: cualquier ventana relativa contiene entradas menores que1 con valor límite0, frente al valor central1.

### Microcontrol 029

[]{#MA-MIC-ANM-01-026-029}

[]{#MA-MSOL-ANM-01-026-029}

**Pregunta.** ¿Qué prueba Bernoulli para $x_n=1-1/[2(n+1)]$?

**Solución.** Que $x_n^n\ge1-n/[2(n+1)]>1/2$, con error grande respecto del límite en esa entrada.

### Microcontrol 030

[]{#MA-MIC-ANM-01-026-030}

[]{#MA-MSOL-ANM-01-026-030}

**Pregunta.** ¿Por qué esa ruta no refuta convergencia puntual?

**Solución.** Porque la entrada cambia con el índice; cada entrada fija menor que1 sí tiene error tendente a cero.

### Microcontrol 031

[]{#MA-MIC-ANM-01-026-031}

[]{#MA-MSOL-ANM-01-026-031}

**Pregunta.** ¿Qué facilita restringir a $[0,c]$ con $c<1$?

**Solución.** Una barrera $x^n\le c^n$ que entrega un corte para todas las entradas mediante el mismo $t_c>0$.

### Microcontrol 032

[]{#MA-MIC-ANM-01-026-032}

[]{#MA-MSOL-ANM-01-026-032}

**Pregunta.** ¿Qué nueva columna debe examinarse en $[-1,1]$?

**Solución.** La de−1: alterna1 y−1, así no tiene límite real.

## §26.5 — Cambiar la entrada mientras cambia el índice

### Microcontrol 033

[]{#MA-MIC-ANM-01-026-033}

[]{#MA-MSOL-ANM-01-026-033}

[]{#MA-SEC-ANM-01-026-005}

**Pregunta.** ¿Por qué cada fila de la capa racional está definida?

**Solución.** En $[0,1]$, su denominador $1+(n+1)x$ es al menos1.

### Microcontrol 034

[]{#MA-MIC-ANM-01-026-034}

[]{#MA-MSOL-ANM-01-026-034}

**Pregunta.** ¿Qué error prueba el destino1 en entradas positivas?

**Solución.** $1/[1+(n+1)x]$, que es como máximo $1/[(n+1)x]$ y tiende a cero para $x$ fijo.

### Microcontrol 035

[]{#MA-MIC-ANM-01-026-035}

[]{#MA-MSOL-ANM-01-026-035}

**Pregunta.** ¿Cuál es la salida en la ruta $1/(n+1)$?

**Solución.** Exactamente1/2 en toda etapa, porque el producto $(n+1)x$ vale1.

### Microcontrol 036

[]{#MA-MIC-ANM-01-026-036}

[]{#MA-MSOL-ANM-01-026-036}

**Pregunta.** ¿Cuál es la salida en la ruta $1/(n+1)^2$?

**Solución.** $1/(n+2)$, que converge a cero.

### Microcontrol 037

[]{#MA-MIC-ANM-01-026-037}

[]{#MA-MSOL-ANM-01-026-037}

**Pregunta.** ¿A qué destino llevan las entradas $1/\sqrt{n+1}$?

**Solución.** A1, pues la salida es $\sqrt{n+1}/(1+\sqrt{n+1})$.

### Microcontrol 038

[]{#MA-MIC-ANM-01-026-038}

[]{#MA-MSOL-ANM-01-026-038}

**Pregunta.** ¿Qué precaución exige la ruta $c/(n+1)$ con $c>1$?

**Solución.** Reparar su prefijo para permanecer en $[0,1]$, por ejemplo tomando el mínimo con1.

### Microcontrol 039

[]{#MA-MIC-ANM-01-026-039}

[]{#MA-MSOL-ANM-01-026-039}

**Pregunta.** ¿Qué valor da tomar primero el límite de entrada hacia cero?

**Solución.** Cero en cada fila y después cero al llevar el índice a infinito.

### Microcontrol 040

[]{#MA-MIC-ANM-01-026-040}

[]{#MA-MSOL-ANM-01-026-040}

**Pregunta.** ¿Qué valor da tomar primero el límite del índice en entradas positivas?

**Solución.** Uno en cada entrada positiva y después uno al acercarla al origen.

## §26.6 — Picos que ninguna entrada fija retiene

### Microcontrol 041

[]{#MA-MIC-ANM-01-026-041}

[]{#MA-MSOL-ANM-01-026-041}

[]{#MA-SEC-ANM-01-026-006}

**Pregunta.** ¿Qué región tiene valores positivos en $t_n$?

**Solución.** $(1/k,3/k)$ con $k=n+3$; en los extremos vale0 y en el centro $2/k$ vale1.

### Microcontrol 042

[]{#MA-MIC-ANM-01-026-042}

[]{#MA-MSOL-ANM-01-026-042}

**Pregunta.** ¿Por qué se eligió $k=n+3$?

**Solución.** Para que el soporte $[1/k,3/k]$ permanezca en $[0,1]$ desde la etapa inicial.

### Microcontrol 043

[]{#MA-MIC-ANM-01-026-043}

[]{#MA-MSOL-ANM-01-026-043}

**Pregunta.** ¿Qué pasa en una entrada positiva fija?

**Solución.** Desde un corte con $n+3>3/x$, queda a la derecha del soporte y todos sus valores posteriores son0.

### Microcontrol 044

[]{#MA-MIC-ANM-01-026-044}

[]{#MA-MSOL-ANM-01-026-044}

**Pregunta.** ¿Qué ruta sigue siempre el pico?

**Solución.** $z_n=2/(n+3)$, que converge al origen y produce salidas1.

### Microcontrol 045

[]{#MA-MIC-ANM-01-026-045}

[]{#MA-MSOL-ANM-01-026-045}

**Pregunta.** ¿Qué integral tiene la tienda de altura1?

**Solución.** $1/k$: dos ramas afines de anchura1/k tienen integral1/(2k) cada una.

### Microcontrol 046

[]{#MA-MIC-ANM-01-026-046}

[]{#MA-MSOL-ANM-01-026-046}

**Pregunta.** ¿Qué cambia al multiplicar la altura por $k$?

**Solución.** La integral pasa a1, mientras cada columna sigue quedando eventualmente en cero.

### Microcontrol 047

[]{#MA-MIC-ANM-01-026-047}

[]{#MA-MSOL-ANM-01-026-047}

**Pregunta.** ¿Tiene $b_n$ una barrera de valores común entre etapas?

**Solución.** No: su valor en el centro es $k=n+3$, arbitrariamente grande.

### Microcontrol 048

[]{#MA-MIC-ANM-01-026-048}

[]{#MA-MSOL-ANM-01-026-048}

**Pregunta.** ¿Por qué no hay una constante Lipschitz común para $t_n$?

**Solución.** Entre $1/k$ y $2/k$ la salida cambia1 en distancia1/k; toda constante válida debe ser al menos $k$.

## §26.7 — Tres intercambios que pueden fallar

### Microcontrol 049

[]{#MA-MIC-ANM-01-026-049}

[]{#MA-MSOL-ANM-01-026-049}

[]{#MA-SEC-ANM-01-026-007}

**Pregunta.** ¿Cuál es el límite puntual de $\mathbf1_{E_{n+1}}$?

**Solución.** Dirichlet: cada racional de denominadorq aparece desde $n+1\ge q$, mientras los irracionales nunca aparecen.

### Microcontrol 050

[]{#MA-MIC-ANM-01-026-050}

[]{#MA-MSOL-ANM-01-026-050}

**Pregunta.** ¿Existe su integral de Riemann?

**Solución.** No; C25 demostró la obstrucción de oscilación persistente en todo intervalo.

### Microcontrol 051

[]{#MA-MIC-ANM-01-026-051}

[]{#MA-MSOL-ANM-01-026-051}

**Pregunta.** ¿Qué integral tiene cada indicadora finita?

**Solución.** Cero, por los resultados de C25 para modificaciones y soportes finitos.

### Microcontrol 052

[]{#MA-MIC-ANM-01-026-052}

[]{#MA-MSOL-ANM-01-026-052}

**Pregunta.** ¿Qué valor tienen las derivadas $h_n^{\prime}(0)$?

**Solución.** Uno para toda etapa; el límite de los valores $h_n$ es cero y su derivada en0 vale0.

### Microcontrol 053

[]{#MA-MIC-ANM-01-026-053}

[]{#MA-MSOL-ANM-01-026-053}

**Pregunta.** ¿Qué ocurre con $h_n^{\prime}(x)$ si $x\ne0$?

**Solución.** Su magnitud es como máximo $1/[1+(n+1)x^2]$, que tiende a cero.

### Microcontrol 054

[]{#MA-MIC-ANM-01-026-054}

[]{#MA-MSOL-ANM-01-026-054}

**Pregunta.** ¿Dónde se alcanza el máximo de $|h_n|$?

**Solución.** En $x=\pm1/\sqrt{n+1}$; el valor máximo es $1/[2\sqrt{n+1}]$.

### Microcontrol 055

[]{#MA-MIC-ANM-01-026-055}

[]{#MA-MSOL-ANM-01-026-055}

**Pregunta.** ¿Qué término queda sin control en la prueba triangular de continuidad?

**Solución.** $|f(y)-f_n(y)|$ para entradas variables $y$ de una ventana con una sola fila ya escogida.

### Microcontrol 056

[]{#MA-MIC-ANM-01-026-056}

[]{#MA-MSOL-ANM-01-026-056}

**Pregunta.** ¿Qué debe comprobarse antes de comparar dos operaciones de límite?

**Solución.** La existencia y el dominio de cada operación interior y exterior, o de cada integral y derivada utilizadas.

## §26.8 — Certificados que recuperan control

### Microcontrol 057

[]{#MA-MIC-ANM-01-026-057}

[]{#MA-MSOL-ANM-01-026-057}

[]{#MA-SEC-ANM-01-026-008}

**Pregunta.** ¿Qué cota común de proximidad pasa al límite puntual?

**Solución.** $|f_n(x)-f_n(y)|\le L|x-y|$ con el mismo $L\ge0$ para todas las filas y pares.

### Microcontrol 058

[]{#MA-MIC-ANM-01-026-058}

[]{#MA-MSOL-ANM-01-026-058}

**Pregunta.** ¿Qué radio prueba continuidad del límite bajo esa cota?

**Solución.** $\delta=\varepsilon/(L+1)>0$, que incluye el caso $L=0$.

### Microcontrol 059

[]{#MA-MIC-ANM-01-026-059}

[]{#MA-MSOL-ANM-01-026-059}

**Pregunta.** ¿Qué dos errores controlan una diagonal bajo la misma hipótesis?

**Solución.** $L|x_n-x|$ y el error puntual $|f_n(x)-f(x)|$ en la entrada fija de destino.

### Microcontrol 060

[]{#MA-MIC-ANM-01-026-060}

[]{#MA-MSOL-ANM-01-026-060}

**Pregunta.** ¿Qué condición de monotonía se refiere al índice?

**Solución.** $f_n(x)\le f_{n+1}(x)$ para cada entrada fija; no describe el orden de una fila respecto de $x$.

### Microcontrol 061

[]{#MA-MIC-ANM-01-026-061}

[]{#MA-MSOL-ANM-01-026-061}

**Pregunta.** ¿Qué objeto produce el límite de una columna creciente acotada?

**Solución.** El supremo de su imagen no vacía acotada, existente por completitud de C03.

### Microcontrol 062

[]{#MA-MIC-ANM-01-026-062}

[]{#MA-MSOL-ANM-01-026-062}

**Pregunta.** ¿Por qué hay un término mayor que el supremo menos $\varepsilon$?

**Solución.** Si no lo hubiera, ese número menor sería una cota superior, contradiciendo la minimalidad del supremo.

### Microcontrol 063

[]{#MA-MIC-ANM-01-026-063}

[]{#MA-MSOL-ANM-01-026-063}

**Pregunta.** ¿Cómo se corrige la desigualdad para columnas decrecientes?

**Solución.** Debe ser $f_{n+1}(x)\le f_n(x)$; invertirla describiría columnas crecientes.

### Microcontrol 064

[]{#MA-MIC-ANM-01-026-064}

[]{#MA-MSOL-ANM-01-026-064}

**Pregunta.** ¿Qué pregunta entrega este capítulo a C27?

**Solución.** Cómo formular y medir una sola cola que controle todas las entradas, y qué consecuencias permite ese contrato.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 26](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html) · [Ejercicios](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto-microcontroles.html)
