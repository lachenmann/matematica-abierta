---
content-id: MA-BCH-0313
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-027-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 27
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C27_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 27](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez.html) · [Ejercicios](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §27.1 — Una cola que sirve para todas las entradas

### Microcontrol 001

[]{#MA-MIC-ANM-01-027-001}

[]{#MA-MSOL-ANM-01-027-001}

[]{#MA-SEC-ANM-01-027-001}

**Pregunta.** ¿Qué dato recibe primero el contrato uniforme?

**Solución.** Una tolerancia positiva; después se elige un corte que debe funcionar para toda entrada y toda la cola.

### Microcontrol 002

[]{#MA-MIC-ANM-01-027-002}

[]{#MA-MSOL-ANM-01-027-002}

**Pregunta.** ¿Puede el corte uniforme depender de la entrada?

**Solución.** No. Debe elegirse antes de la entrada que habrá que controlar.

### Microcontrol 003

[]{#MA-MIC-ANM-01-027-003}

[]{#MA-MSOL-ANM-01-027-003}

**Pregunta.** ¿Qué anchura tiene la banda de tolerancia $\varepsilon$?

**Solución.** Anchura vertical2ε, entre f(x)−ε y f(x)+ε, con fronteras excluidas.

### Microcontrol 004

[]{#MA-MIC-ANM-01-027-004}

[]{#MA-MSOL-ANM-01-027-004}

**Pregunta.** ¿Implica uniformidad convergencia puntual?

**Solución.** Sí; el mismo corte simultáneo sirve en cualquier entrada que fijemos.

### Microcontrol 005

[]{#MA-MIC-ANM-01-027-005}

[]{#MA-MSOL-ANM-01-027-005}

**Pregunta.** ¿Qué entrada puede variar en una refutación uniforme?

**Solución.** La entrada infractora puede depender del corte y del índice tardío elegido.

### Microcontrol 006

[]{#MA-MIC-ANM-01-027-006}

[]{#MA-MSOL-ANM-01-027-006}

**Pregunta.** ¿Qué error tiene $x+1/(n+1)$ respecto de $x$?

**Solución.** Exactamente1/(n+1) en toda la recta, aunque los valores de ambas funciones sean no acotados.

### Microcontrol 007

[]{#MA-MIC-ANM-01-027-007}

[]{#MA-MSOL-ANM-01-027-007}

**Pregunta.** ¿Qué testigo refuta uniformidad de $x/(n+1)$ en la recta?

**Solución.** En la fila n se toma x=n+1, con error1 respecto de cero.

### Microcontrol 008

[]{#MA-MIC-ANM-01-027-008}

[]{#MA-MSOL-ANM-01-027-008}

**Pregunta.** ¿Qué ocurre en un dominio vacío?

**Solución.** Hay una única función y el contrato uniforme se satisface vacuamente.

## §27.2 — La envolvente de error y sus fronteras

### Microcontrol 009

[]{#MA-MIC-ANM-01-027-009}

[]{#MA-MSOL-ANM-01-027-009}

[]{#MA-SEC-ANM-01-027-002}

**Pregunta.** ¿Qué se comprueba antes de formar una envolvente real?

**Solución.** Que la imagen de errores sea no vacía y acotada; el vacío se trata por una convención aparte.

### Microcontrol 010

[]{#MA-MIC-ANM-01-027-010}

[]{#MA-MSOL-ANM-01-027-010}

**Pregunta.** ¿Se exige envolvente real para todas las filas iniciales?

**Solución.** No. Basta una cola con errores acotados y supremos tendentes a cero.

### Microcontrol 011

[]{#MA-MIC-ANM-01-027-011}

[]{#MA-MSOL-ANM-01-027-011}

**Pregunta.** ¿Qué margen convierte control puntual estricto en supremo estricto?

**Solución.** Usar toleranciaε/2: el supremo es≤ε/2<ε.

### Microcontrol 012

[]{#MA-MIC-ANM-01-027-012}

[]{#MA-MSOL-ANM-01-027-012}

**Pregunta.** ¿Puede cada error ser menor que1 y su supremo ser1?

**Solución.** Sí; e(x)=x en(0,1) lo muestra sin que haya máximo.

### Microcontrol 013

[]{#MA-MIC-ANM-01-027-013}

[]{#MA-MSOL-ANM-01-027-013}

**Pregunta.** ¿Qué diferencia entre vacío y convención de error cero se conserva?

**Solución.** El error de la función vacía se define0; no se afirma que el conjunto vacío tenga supremo real0.

### Microcontrol 014

[]{#MA-MIC-ANM-01-027-014}

[]{#MA-MSOL-ANM-01-027-014}

**Pregunta.** ¿Qué son los conjuntos $B_n(\eta)$?

**Solución.** Las entradas cuyo error en la fila n es al menosη.

### Microcontrol 015

[]{#MA-MIC-ANM-01-027-015}

[]{#MA-MSOL-ANM-01-027-015}

**Pregunta.** ¿Qué dice uniformidad sobre esos conjuntos?

**Solución.** Para cadaη>0, todos son vacíos desde un único corte en adelante.

### Microcontrol 016

[]{#MA-MIC-ANM-01-027-016}

[]{#MA-MSOL-ANM-01-027-016}

**Pregunta.** ¿Qué dice puntualidad sobre una entrada fija y esos conjuntos?

**Solución.** Que esa entrada deja de pertenecer a ellos eventualmente, con un corte que puede depender de ella.

## §27.3 — Calcular la peor discrepancia

### Microcontrol 017

[]{#MA-MIC-ANM-01-027-017}

[]{#MA-MSOL-ANM-01-027-017}

[]{#MA-SEC-ANM-01-027-003}

**Pregunta.** ¿Cuál es la envolvente de las potencias en $[0,1]$ para $n\ge1$?

**Solución.** Uno; el error no lo alcanza porque en1 vale0 y antes de1 es menor que1.

### Microcontrol 018

[]{#MA-MIC-ANM-01-027-018}

[]{#MA-MSOL-ANM-01-027-018}

**Pregunta.** ¿Qué controla las potencias en $[0,c]$ con $c<1$?

**Solución.** La cota y máximo c^n, que tiende a cero por Bernoulli.

### Microcontrol 019

[]{#MA-MIC-ANM-01-027-019}

[]{#MA-MSOL-ANM-01-027-019}

**Pregunta.** ¿Qué ocurre si $c=0$?

**Solución.** La única entrada es cero y el error de las potencias vale0 desde n=1.

### Microcontrol 020

[]{#MA-MIC-ANM-01-027-020}

[]{#MA-MSOL-ANM-01-027-020}

**Pregunta.** ¿Dónde alcanza su error máximo la tienda $t_n$?

**Solución.** En x=2/(n+3), donde vale1.

### Microcontrol 021

[]{#MA-MIC-ANM-01-027-021}

[]{#MA-MSOL-ANM-01-027-021}

**Pregunta.** ¿Qué envolvente tiene la tienda normalizada?

**Solución.** k=n+3, alcanzada en el mismo centro móvil.

### Microcontrol 022

[]{#MA-MIC-ANM-01-027-022}

[]{#MA-MSOL-ANM-01-027-022}

**Pregunta.** ¿Qué cuadrado produce la cota global de $h_n$?

**Solución.** (√k|x|−1)^2≥0, con k=n+1.

### Microcontrol 023

[]{#MA-MIC-ANM-01-027-023}

[]{#MA-MSOL-ANM-01-027-023}

**Pregunta.** ¿Dónde alcanza $h_n$ su máximo de magnitud?

**Solución.** En x=±1/√k, con valor1/(2√k).

### Microcontrol 024

[]{#MA-MIC-ANM-01-027-024}

[]{#MA-MSOL-ANM-01-027-024}

**Pregunta.** ¿Decide un dominio no acotado que la convergencia falle?

**Solución.** No. h_n converge uniformemente a cero en toda la recta mediante una cota global.

## §27.4 — Restringir el dominio y seguir rutas

### Microcontrol 025

[]{#MA-MIC-ANM-01-027-025}

[]{#MA-MSOL-ANM-01-027-025}

[]{#MA-SEC-ANM-01-027-004}

**Pregunta.** ¿Qué corte sirve después de restringir el dominio?

**Solución.** El mismo corte de uniformidad en el dominio mayor.

### Microcontrol 026

[]{#MA-MIC-ANM-01-027-026}

[]{#MA-MSOL-ANM-01-027-026}

**Pregunta.** ¿Cómo se reúnen finitariamente los cortes de piezas?

**Solución.** Con su máximo, que domina todas las obligaciones para la tolerancia fijada.

### Microcontrol 027

[]{#MA-MIC-ANM-01-027-027}

[]{#MA-MSOL-ANM-01-027-027}

**Pregunta.** ¿Hace falta que las piezas sean abiertas o cerradas?

**Solución.** No; el argumento de reunión finita sólo usa pertenencia a alguna pieza.

### Microcontrol 028

[]{#MA-MIC-ANM-01-027-028}

[]{#MA-MSOL-ANM-01-027-028}

**Pregunta.** ¿Qué puede fallar en una unión infinita?

**Solución.** Los cortes de las piezas pueden no tener una barrera común.

### Microcontrol 029

[]{#MA-MIC-ANM-01-027-029}

[]{#MA-MSOL-ANM-01-027-029}

**Pregunta.** ¿Qué error controla uniformidad para cualquier ruta $x_n$?

**Solución.** |f_n(x_n)−f(x_n)|, sin exigir que las entradas converjan.

### Microcontrol 030

[]{#MA-MIC-ANM-01-027-030}

[]{#MA-MSOL-ANM-01-027-030}

**Pregunta.** ¿Qué dato adicional permite comparar con $f(x)$?

**Solución.** Que x_n→x∈X y que f sea continua en x.

### Microcontrol 031

[]{#MA-MIC-ANM-01-027-031}

[]{#MA-MSOL-ANM-01-027-031}

**Pregunta.** ¿Qué cota de índices tiene una subsucesión estrictamente creciente?

**Solución.** n_j≥j, por inducción en naturales; permite heredar el corte uniforme.

### Microcontrol 032

[]{#MA-MIC-ANM-01-027-032}

[]{#MA-MSOL-ANM-01-027-032}

**Pregunta.** ¿Basta una subsucesión uniforme para afirmar uniformidad de la familia?

**Solución.** No; las filas constantes alternantes tienen una subsucesión par constante y la familia no converge.

## §27.5 — Operar bajo un presupuesto común

### Microcontrol 033

[]{#MA-MIC-ANM-01-027-033}

[]{#MA-MSOL-ANM-01-027-033}

[]{#MA-SEC-ANM-01-027-005}

**Pregunta.** ¿Qué permite la suma de dos errores uniformes?

**Solución.** Repartir la tolerancia y tomar el máximo de dos cortes independientes de la entrada.

### Microcontrol 034

[]{#MA-MIC-ANM-01-027-034}

[]{#MA-MSOL-ANM-01-027-034}

**Pregunta.** ¿Qué desigualdad controla el valor absoluto?

**Solución.** La triangular inversa: ||u|−|v||≤|u−v|.

### Microcontrol 035

[]{#MA-MIC-ANM-01-027-035}

[]{#MA-MSOL-ANM-01-027-035}

**Pregunta.** ¿Qué hipótesis suficiente se declara para una composición exterior?

**Solución.** Una constante Lipschitz común en un dominio que contenga todos los valores utilizados.

### Microcontrol 036

[]{#MA-MIC-ANM-01-027-036}

[]{#MA-MSOL-ANM-01-027-036}

**Pregunta.** ¿Qué barrera obtiene la prueba del producto para $f_n$?

**Solución.** |f_n|≤A+1 en una cola, desde |f|≤A y error uniforme menor que1.

### Microcontrol 037

[]{#MA-MIC-ANM-01-027-037}

[]{#MA-MSOL-ANM-01-027-037}

**Pregunta.** ¿Por qué el producto con $x$ puede perder uniformidad?

**Solución.** No hay una barrera de |x| en la recta que permita convertir el pequeño error del otro factor en uno global.

### Microcontrol 038

[]{#MA-MIC-ANM-01-027-038}

[]{#MA-MSOL-ANM-01-027-038}

**Pregunta.** ¿Basta continuidad del cuadrado para conservar uniformidad en valores no acotados?

**Solución.** No; el error de cuadrar x+1/(n+1) crece sin cota al variar x.

### Microcontrol 039

[]{#MA-MIC-ANM-01-027-039}

[]{#MA-MSOL-ANM-01-027-039}

**Pregunta.** ¿Qué margen uniforme evita ceros en denominadores?

**Solución.** |g|≥m>0 y error|g_n−g|<m/2 garantizan |g_n|>m/2 en toda la cola.

### Microcontrol 040

[]{#MA-MIC-ANM-01-027-040}

[]{#MA-MSOL-ANM-01-027-040}

**Pregunta.** ¿Qué debe revisarse para recíprocos desde el índice inicial?

**Solución.** Que las filas iniciales no tengan ceros en el dominio, o que se declare su reparación.

## §27.6 — Una distancia entre funciones acotadas

### Microcontrol 041

[]{#MA-MIC-ANM-01-027-041}

[]{#MA-MSOL-ANM-01-027-041}

[]{#MA-SEC-ANM-01-027-006}

**Pregunta.** ¿Qué funciones pertenecen a $\mathcal B(X)$?

**Solución.** Las funciones reales sobre X cuyos valores tienen una barrera de magnitud válida para toda entrada.

### Microcontrol 042

[]{#MA-MIC-ANM-01-027-042}

[]{#MA-MSOL-ANM-01-027-042}

**Pregunta.** ¿Qué principio asegura existencia de la norma cuando $X$ no es vacío?

**Solución.** Completitud de C03 aplicada a la imagen no vacía acotada de |u|.

### Microcontrol 043

[]{#MA-MIC-ANM-01-027-043}

[]{#MA-MSOL-ANM-01-027-043}

**Pregunta.** ¿Qué valor de norma se declara en el dominio vacío?

**Solución.** Cero, por convención para la función única, no por un supremo real del vacío.

### Microcontrol 044

[]{#MA-MIC-ANM-01-027-044}

[]{#MA-MSOL-ANM-01-027-044}

**Pregunta.** ¿Qué dice norma cero sobre la función?

**Solución.** Que todos sus valores son0 y por tanto es la función cero.

### Microcontrol 045

[]{#MA-MIC-ANM-01-027-045}

[]{#MA-MSOL-ANM-01-027-045}

**Pregunta.** ¿Cómo se trata el escalar cero en homogeneidad?

**Solución.** Por verificación directa; no se divide por su magnitud.

### Microcontrol 046

[]{#MA-MIC-ANM-01-027-046}

[]{#MA-MSOL-ANM-01-027-046}

**Pregunta.** ¿Qué identidad da la distancia triangular?

**Solución.** u−w=(u−v)+(v−w), junto con la desigualdad triangular de la norma.

### Microcontrol 047

[]{#MA-MIC-ANM-01-027-047}

[]{#MA-MSOL-ANM-01-027-047}

**Pregunta.** ¿Puede una gráfica estar en una banda abierta sin quedar en la bola estricta del mismo radio?

**Solución.** Sí; los errores pueden ser menores que el radio y tener supremo exactamente igual a él.

### Microcontrol 048

[]{#MA-MIC-ANM-01-027-048}

[]{#MA-MSOL-ANM-01-027-048}

**Pregunta.** ¿Qué permite una clase $f_0+\mathcal B(X)$?

**Solución.** Medir diferencias acotadas aunque la base y sus traslaciones sean no acotadas.

## §27.7 — Cauchy uniforme y completitud

### Microcontrol 049

[]{#MA-MIC-ANM-01-027-049}

[]{#MA-MSOL-ANM-01-027-049}

[]{#MA-SEC-ANM-01-027-007}

**Pregunta.** ¿Cuántos índices universales controla Cauchy uniforme?

**Solución.** Dos, m y n, ambos posteriores a un único corte que también sirve en toda entrada.

### Microcontrol 050

[]{#MA-MIC-ANM-01-027-050}

[]{#MA-MSOL-ANM-01-027-050}

**Pregunta.** ¿Qué dirección del criterio no usa completitud?

**Solución.** Uniformemente convergente⇒uniformemente de Cauchy, mediante la triangular y dos errores.

### Microcontrol 051

[]{#MA-MIC-ANM-01-027-051}

[]{#MA-MSOL-ANM-01-027-051}

**Pregunta.** ¿Dónde interviene completitud en la vuelta?

**Solución.** En C10, al dar un límite real a cada columna de Cauchy.

### Microcontrol 052

[]{#MA-MIC-ANM-01-027-052}

[]{#MA-MSOL-ANM-01-027-052}

**Pregunta.** ¿Qué se mantiene fijo al llevar $m$ al límite?

**Solución.** El índice n≥N y la entrada x; el corte común ya se eligió antes de ambos.

### Microcontrol 053

[]{#MA-MIC-ANM-01-027-053}

[]{#MA-MSOL-ANM-01-027-053}

**Pregunta.** ¿Qué sentido tiene la desigualdad tras ese límite?

**Solución.** |f_n(x)−f(x)|≤ε/3; el límite conserva la cota superior, sin invertirla.

### Microcontrol 054

[]{#MA-MIC-ANM-01-027-054}

[]{#MA-MSOL-ANM-01-027-054}

**Pregunta.** ¿Qué fila demuestra acotación del límite en $\mathcal B(X)$?

**Solución.** Una fila de referencia f_N, con barrera final‖f_N‖∞+1 para todas las entradas.

### Microcontrol 055

[]{#MA-MIC-ANM-01-027-055}

[]{#MA-MSOL-ANM-01-027-055}

**Pregunta.** ¿Qué significa completitud secuencial para esa distancia?

**Solución.** Que toda sucesión de Cauchy tiene límite dentro de$\mathcal B(X)$ en distancia suprema.

### Microcontrol 056

[]{#MA-MIC-ANM-01-027-056}

[]{#MA-MSOL-ANM-01-027-056}

**Pregunta.** ¿Por qué no basta que las diferencias de vecinos tiendan a cero?

**Solución.** Los pares lejanos de una cola pueden seguir separados, como H_(2m)−H_m≥1/2.

## §27.8 — Certificar una aproximación completa

### Microcontrol 057

[]{#MA-MIC-ANM-01-027-057}

[]{#MA-MSOL-ANM-01-027-057}

[]{#MA-SEC-ANM-01-027-008}

**Pregunta.** ¿Qué suma usa el presupuesto geométrico de incrementos?

**Solución.** Una suma finita entre las etapas m y n−1; no se presupone una serie de funciones.

### Microcontrol 058

[]{#MA-MIC-ANM-01-027-058}

[]{#MA-MSOL-ANM-01-027-058}

**Pregunta.** ¿Qué cota común se obtiene para dos etapas con $n>m$?

**Solución.** Cq^m/(1−q), válida para toda entrada.

### Microcontrol 059

[]{#MA-MIC-ANM-01-027-059}

[]{#MA-MSOL-ANM-01-027-059}

**Pregunta.** ¿Qué error se certifica después de construir el límite?

**Solución.** |f−f_m|≤Cq^m/(1−q) en todo el dominio.

### Microcontrol 060

[]{#MA-MIC-ANM-01-027-060}

[]{#MA-MSOL-ANM-01-027-060}

**Pregunta.** ¿Qué ocurre si $C=0$?

**Solución.** Todos los incrementos son0 y todas las filas coinciden.

### Microcontrol 061

[]{#MA-MIC-ANM-01-027-061}

[]{#MA-MSOL-ANM-01-027-061}

**Pregunta.** ¿Cómo se evita ambigüedad si se permite $q=0$?

**Solución.** Se declara cota inicialC y cotas posteriores0; desde la etapa1 la familia es constante.

### Microcontrol 062

[]{#MA-MIC-ANM-01-027-062}

[]{#MA-MSOL-ANM-01-027-062}

**Pregunta.** ¿Cuándo se concluye que el límite es acotado?

**Solución.** Cuando una fila de referencia está acotada; el presupuesto sólo acota diferencias si la base es arbitraria.

### Microcontrol 063

[]{#MA-MIC-ANM-01-027-063}

[]{#MA-MSOL-ANM-01-027-063}

**Pregunta.** ¿Qué refuta $s_n=\mathbf1_{(0,1/(n+1))}$?

**Solución.** Que monotonía por columnas y límite continuo basten sin otros datos: el error máximo sigue siendo1.

### Microcontrol 064

[]{#MA-MIC-ANM-01-027-064}

[]{#MA-MSOL-ANM-01-027-064}

**Pregunta.** ¿Qué única puerta sigue a este capítulo?

**Solución.** C28: demostrar con sus hipótesis cuándo continuidad, integración y diferenciación pueden atravesar los límites.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 27](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez.html) · [Ejercicios](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez-microcontroles.html)
