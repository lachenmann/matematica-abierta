---
content-id: MA-BCH-0249
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-011-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 11
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C11_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 11](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html) · [Ejercicios](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §11.1 — De los términos a las sumas parciales

### Microcontrol 001

[]{#MA-MIC-ANM-01-011-001}

[]{#MA-MSOL-ANM-01-011-001}

[]{#MA-SEC-ANM-01-011-001}

**Pregunta.** ¿Cuántos términos contiene $s_n=\sum_{k=0}^n a_k$?

**Solución.** $n+1$, porque los índices van de cero a $n$ inclusive.

### Microcontrol 002

[]{#MA-MIC-ANM-01-011-002}

[]{#MA-MSOL-ANM-01-011-002}

**Pregunta.** ¿Cuál es el término inicial de $\operatorname{PS}(a)$?

**Solución.** $s_0=a_0$; no es automáticamente cero.

### Microcontrol 003

[]{#MA-MIC-ANM-01-011-003}

[]{#MA-MSOL-ANM-01-011-003}

**Pregunta.** ¿Qué condición permite llamar suma real a $\sum_{n=0}^{\infty}a_n$?

**Solución.** Que la sucesión de sumas parciales converja a un real $S$; entonces el símbolo de suma designa ese límite único.

### Microcontrol 004

[]{#MA-MIC-ANM-01-011-004}

[]{#MA-MSOL-ANM-01-011-004}

**Pregunta.** ¿Cómo se recupera $a_{n+1}$ a partir de dos totales?

**Solución.** $a_{n+1}=s_{n+1}-s_n$, por la recursión.

### Microcontrol 005

[]{#MA-MIC-ANM-01-011-005}

[]{#MA-MSOL-ANM-01-011-005}

**Pregunta.** ¿Tener la misma suma implica tener los mismos términos?

**Solución.** No. $(1,0,0,\ldots)$ y $(1/2,1/2,0,\ldots)$ tienen suma uno y distintos términos y procesos.

### Microcontrol 006

[]{#MA-MIC-ANM-01-011-006}

[]{#MA-MSOL-ANM-01-011-006}

**Pregunta.** ¿Qué totales produce $a_n=(-1)^n$?

**Solución.** $s_{2k}=1$ y $s_{2k+1}=0$, al cancelar parejas consecutivas.

### Microcontrol 007

[]{#MA-MIC-ANM-01-011-007}

[]{#MA-MSOL-ANM-01-011-007}

**Pregunta.** ¿La acotación de esos totales garantiza convergencia?

**Solución.** No. Después de cualquier corte hay totales separados por uno, de modo que falla Cauchy.

### Microcontrol 008

[]{#MA-MIC-ANM-01-011-008}

[]{#MA-MSOL-ANM-01-011-008}

**Pregunta.** ¿Son $a$, $\operatorname{PS}(a)$ y su suma el mismo tipo de objeto?

**Solución.** No. $a$ y $\operatorname{PS}(a)$ son funciones $\mathbb N\to\mathbb R$ con papeles diferentes; su suma, si existe, es un número real.

## §11.2 — Cauchy mide bloques completos

### Microcontrol 009

[]{#MA-MIC-ANM-01-011-009}

[]{#MA-MSOL-ANM-01-011-009}

[]{#MA-SEC-ANM-01-011-002}

**Pregunta.** ¿Por qué el bloque $s_p-s_q$ empieza en $q+1$?

**Solución.** Porque $s_q$ ya contiene $a_q$; los nuevos términos son $a_{q+1},\ldots,a_p$.

### Microcontrol 010

[]{#MA-MIC-ANM-01-011-010}

[]{#MA-MSOL-ANM-01-011-010}

**Pregunta.** ¿En qué orden se eligen tolerancia, corte y extremos de bloque?

**Solución.** Primero $\varepsilon>0$, después un único $N$ que puede depender de ella, y luego todos $p>q\ge N$.

### Microcontrol 011

[]{#MA-MIC-ANM-01-011-011}

[]{#MA-MSOL-ANM-01-011-011}

**Pregunta.** ¿Puede el corte depender de la longitud del bloque?

**Solución.** No en el criterio: debe controlar simultáneamente todas las longitudes.

### Microcontrol 012

[]{#MA-MIC-ANM-01-011-012}

[]{#MA-MSOL-ANM-01-011-012}

**Pregunta.** ¿Cómo se cubre el caso $p=q$ al recuperar Cauchy?

**Solución.** La distancia entre el mismo total y sí mismo es cero, menor que cualquier tolerancia positiva.

### Microcontrol 013

[]{#MA-MIC-ANM-01-011-013}

[]{#MA-MSOL-ANM-01-011-013}

**Pregunta.** ¿Dónde se usa completitud en el criterio de bloques?

**Solución.** En pasar de Cauchy de $s$ a existencia de un límite real, mediante C10; no en la identidad de sumas finitas.

### Microcontrol 014

[]{#MA-MIC-ANM-01-011-014}

[]{#MA-MSOL-ANM-01-011-014}

**Pregunta.** ¿Por qué convergencia de la serie implica $a_n\to0$?

**Solución.** Para $n\ge N+1$, el bloque de un término entre $n-1$ y $n$ da $|a_n|<\varepsilon$.

### Microcontrol 015

[]{#MA-MIC-ANM-01-011-015}

[]{#MA-MSOL-ANM-01-011-015}

**Pregunta.** ¿Qué pares de cortes niegan Cauchy en la armónica?

**Solución.** Para cualquier $N$, tomar $m=N+1$, $q=m-1$ y $p=2m-1$ da una diferencia al menos $1/2$.

### Microcontrol 016

[]{#MA-MIC-ANM-01-011-016}

[]{#MA-MSOL-ANM-01-011-016}

**Pregunta.** ¿El término nulo es una condición suficiente?

**Solución.** No. $1/(n+1)\to0$, pero sus bloques largos anteriores mantienen suma al menos $1/2$ después de cada corte.

## §11.3 — Fórmulas finitas y restos exactos

### Microcontrol 017

[]{#MA-MIC-ANM-01-011-017}

[]{#MA-MSOL-ANM-01-011-017}

[]{#MA-SEC-ANM-01-011-003}

**Pregunta.** ¿Qué total produce $a_n=c_n-c_{n+1}$?

**Solución.** $s_n=c_0-c_{n+1}$ por cancelación finita, demostrable por inducción.

### Microcontrol 018

[]{#MA-MIC-ANM-01-011-018}

[]{#MA-MSOL-ANM-01-011-018}

**Pregunta.** ¿Cuál es el resto telescópico si $c_n\to C$?

**Solución.** La suma es $c_0-C$ y $R_n=c_{n+1}-C$.

### Microcontrol 019

[]{#MA-MIC-ANM-01-011-019}

[]{#MA-MSOL-ANM-01-011-019}

**Pregunta.** ¿Cuál es la suma de $1/((n+1)(n+2))$?

**Solución.** Uno: $s_n=1-1/(n+2)\to1$.

### Microcontrol 020

[]{#MA-MIC-ANM-01-011-020}

[]{#MA-MSOL-ANM-01-011-020}

**Pregunta.** ¿Qué identidad geométrica es válida antes de cualquier límite?

**Solución.** $(1-r)\sum_{k=0}^nr^k=1-r^{n+1}$, para todo real $r$ y natural $n$.

### Microcontrol 021

[]{#MA-MIC-ANM-01-011-021}

[]{#MA-MSOL-ANM-01-011-021}

**Pregunta.** ¿Para qué razones reales converge la geométrica?

**Solución.** Exactamente para $|r|<1$; fuera de ese intervalo los términos no tienden a cero.

### Microcontrol 022

[]{#MA-MIC-ANM-01-011-022}

[]{#MA-MSOL-ANM-01-011-022}

**Pregunta.** ¿Qué ocurre con la geométrica de razón cero?

**Solución.** Con $r^0=1$, sus términos son uno y luego ceros, así que su suma es uno.

### Microcontrol 023

[]{#MA-MIC-ANM-01-011-023}

[]{#MA-MSOL-ANM-01-011-023}

**Pregunta.** ¿Cuál es el resto exacto cuando $|r|<1$?

**Solución.** $R_n=r^{n+1}/(1-r)$, después de probar $S=1/(1-r)$.

### Microcontrol 024

[]{#MA-MIC-ANM-01-011-024}

[]{#MA-MSOL-ANM-01-011-024}

**Pregunta.** ¿Es correcto dividir por $1-r$ para estudiar $r=1$?

**Solución.** No. Para $r=1$, $s_n=n+1$ y la condición del término nulo ya descarta convergencia.

## §11.4 — Acumulación positiva y barreras

### Microcontrol 025

[]{#MA-MIC-ANM-01-011-025}

[]{#MA-MSOL-ANM-01-011-025}

[]{#MA-SEC-ANM-01-011-004}

**Pregunta.** ¿Qué hipótesis hace crecientes las sumas parciales?

**Solución.** $a_n\ge0$: el incremento $s_{n+1}-s_n=a_{n+1}$ es no negativo.

### Microcontrol 026

[]{#MA-MIC-ANM-01-011-026}

[]{#MA-MSOL-ANM-01-011-026}

**Pregunta.** ¿Qué cota basta para una serie no negativa?

**Solución.** Una cota superior real común a todas sus sumas parciales.

### Microcontrol 027

[]{#MA-MIC-ANM-01-011-027}

[]{#MA-MSOL-ANM-01-011-027}

**Pregunta.** ¿Qué conjunto se usa para construir el destino por supremo?

**Solución.** $\{s_n:n\in\mathbb N\}$, no vacío y acotado superiormente.

### Microcontrol 028

[]{#MA-MIC-ANM-01-011-028}

[]{#MA-MSOL-ANM-01-011-028}

**Pregunta.** ¿Cómo se encuentra un total cercano por debajo del supremo?

**Solución.** $S-\varepsilon$ no es cota superior, por lo que existe $N$ con $s_N>S-\varepsilon$.

### Microcontrol 029

[]{#MA-MIC-ANM-01-011-029}

[]{#MA-MSOL-ANM-01-011-029}

**Pregunta.** ¿Por qué todos los totales posteriores siguen cerca?

**Solución.** La no negatividad da $s_N\le s_n\le S$ para $n\ge N$.

### Microcontrol 030

[]{#MA-MIC-ANM-01-011-030}

[]{#MA-MSOL-ANM-01-011-030}

**Pregunta.** ¿Qué conclusión da $0\le a_n\le b_n$ si la serie de $b$ converge?

**Solución.** La serie de $a$ converge y $0\le S_a\le S_b$ si la comparación vale desde el inicio.

### Microcontrol 031

[]{#MA-MIC-ANM-01-011-031}

[]{#MA-MSOL-ANM-01-011-031}

**Pregunta.** ¿Una comparación eventual conserva automáticamente el orden de sumas completas?

**Solución.** No. Los prefijos pueden modificar esas sumas; la comparación garantiza convergencia de las colas.

### Microcontrol 032

[]{#MA-MIC-ANM-01-011-032}

[]{#MA-MSOL-ANM-01-011-032}

**Pregunta.** ¿Qué resto garantiza la comparación para $a_n=1/(n+2)^2$?

**Solución.** $0\le S_a-s_n\le1/(n+2)$, comparando el bloque posterior con la serie telescópica.

## §11.5 — Control absoluto de la acumulación

### Microcontrol 033

[]{#MA-MIC-ANM-01-011-033}

[]{#MA-MSOL-ANM-01-011-033}

[]{#MA-SEC-ANM-01-011-005}

**Pregunta.** ¿Qué significa convergencia absoluta?

**Solución.** Que converge la serie de términos $|a_n|$.

### Microcontrol 034

[]{#MA-MIC-ANM-01-011-034}

[]{#MA-MSOL-ANM-01-011-034}

**Pregunta.** ¿Qué condición adicional exige llamar condicional a una convergencia?

**Solución.** La original converge, mientras la serie de magnitudes diverge.

### Microcontrol 035

[]{#MA-MIC-ANM-01-011-035}

[]{#MA-MSOL-ANM-01-011-035}

**Pregunta.** ¿Qué desigualdad domina un bloque con signos?

**Solución.** $|\sum_{k=q+1}^pa_k|\le\sum_{k=q+1}^p|a_k|$ por triangular finita.

### Microcontrol 036

[]{#MA-MIC-ANM-01-011-036}

[]{#MA-MSOL-ANM-01-011-036}

**Pregunta.** ¿Por qué un corte para las magnitudes sirve para la original?

**Solución.** La suma del bloque de magnitudes es no negativa y domina la distancia de los totales originales; el mismo corte prueba Cauchy.

### Microcontrol 037

[]{#MA-MIC-ANM-01-011-037}

[]{#MA-MSOL-ANM-01-011-037}

**Pregunta.** ¿Se necesita sumar primero la original para aplicar control absoluto?

**Solución.** No. Se dominan bloques finitos y se obtiene existencia del límite mediante C10.

### Microcontrol 038

[]{#MA-MIC-ANM-01-011-038}

[]{#MA-MSOL-ANM-01-011-038}

**Pregunta.** ¿Qué relación hay entre las sumas $S$ y $A$ de la original y las magnitudes?

**Solución.** $|S|\le A$, al pasar al límite en $|s_n|\le u_n$.

### Microcontrol 039

[]{#MA-MIC-ANM-01-011-039}

[]{#MA-MSOL-ANM-01-011-039}

**Pregunta.** ¿Qué cota de error proporciona $u_n\to A$?

**Solución.** $|S-s_n|\le A-u_n$, tomando el límite del extremo posterior del bloque.

### Microcontrol 040

[]{#MA-MIC-ANM-01-011-040}

[]{#MA-MSOL-ANM-01-011-040}

**Pregunta.** ¿Qué error asegura $|a_n|\le C\rho^n$ con $0<\rho<1$?

**Solución.** $|S-s_n|\le C\rho^{n+1}/(1-\rho)$; para $C=0$ el error es cero.

## §11.6 — Alternancia: encerrar sin sumar magnitudes

### Microcontrol 041

[]{#MA-MIC-ANM-01-011-041}

[]{#MA-MSOL-ANM-01-011-041}

[]{#MA-SEC-ANM-01-011-006}

**Pregunta.** ¿Qué tres condiciones se imponen a la alternancia?

**Solución.** Los términos son $(-1)^nb_n$, las magnitudes son no negativas y decrecientes, y $b_n\to0$.

### Microcontrol 042

[]{#MA-MIC-ANM-01-011-042}

[]{#MA-MSOL-ANM-01-011-042}

**Pregunta.** ¿Qué cota tiene un bloque alternado que empieza en $q+1$?

**Solución.** $|s_p-s_q|\le b_{q+1}$ para $p>q$, por el lema de emparejamiento.

### Microcontrol 043

[]{#MA-MIC-ANM-01-011-043}

[]{#MA-MSOL-ANM-01-011-043}

**Pregunta.** ¿Qué hipótesis permite emparejar diferencias no negativas?

**Solución.** El decrecimiento $b_{n+1}\le b_n$.

### Microcontrol 044

[]{#MA-MIC-ANM-01-011-044}

[]{#MA-MSOL-ANM-01-011-044}

**Pregunta.** ¿Qué hipótesis hace pequeño el control del bloque?

**Solución.** $b_n\to0$ permite un único corte con $b_{q+1}<\varepsilon$ para todos los bloques tardíos.

### Microcontrol 045

[]{#MA-MIC-ANM-01-011-045}

[]{#MA-MSOL-ANM-01-011-045}

**Pregunta.** ¿Qué error y signo tiene el resto?

**Solución.** $0\le(-1)^{n+1}(S-s_n)\le b_{n+1}$, así que el resto tiene el signo del próximo término salvo que sea cero.

### Microcontrol 046

[]{#MA-MIC-ANM-01-011-046}

[]{#MA-MSOL-ANM-01-011-046}

**Pregunta.** ¿Qué intervalo contiene la suma entre los cortes $2k$ y $2k+1$?

**Solución.** $[s_{2k+1},s_{2k}]$, de anchura $b_{2k+1}$.

### Microcontrol 047

[]{#MA-MIC-ANM-01-011-047}

[]{#MA-MSOL-ANM-01-011-047}

**Pregunta.** ¿Por qué la armónica alternada es condicional?

**Solución.** La alternancia decreciente prueba convergencia, mientras la serie de magnitudes es la armónica divergente.

### Microcontrol 048

[]{#MA-MIC-ANM-01-011-048}

[]{#MA-MSOL-ANM-01-011-048}

**Pregunta.** ¿Qué falla si se alternan $2/(k+1)$ y $1/(k+1)$ por parejas?

**Solución.** Las magnitudes tienden a cero, pero no decrecen globalmente y cada pareja aporta $1/(k+1)$; los totales de fin de pareja son armónicos no acotados.

## §11.7 — Agrupar términos y conservar el recorrido

### Microcontrol 049

[]{#MA-MIC-ANM-01-011-049}

[]{#MA-MSOL-ANM-01-011-049}

[]{#MA-SEC-ANM-01-011-007}

**Pregunta.** ¿Qué son las sumas parciales de la serie agrupada?

**Solución.** $t_k=s_{\phi(k)}$: los totales originales en los extremos de los grupos consecutivos.

### Microcontrol 050

[]{#MA-MIC-ANM-01-011-050}

[]{#MA-MSOL-ANM-01-011-050}

**Pregunta.** ¿Por qué convergencia original implica convergencia agrupada?

**Solución.** $\phi(k)\ge k$ por inducción, de modo que el mismo control eventual alcanza los extremos de grupo y conserva el límite.

### Microcontrol 051

[]{#MA-MIC-ANM-01-011-051}

[]{#MA-MSOL-ANM-01-011-051}

**Pregunta.** ¿Puede fallar la recíproca?

**Solución.** Sí. Parejas $(1,-1)$ dan grupos cero, pero los totales originales alternan uno y cero.

### Microcontrol 052

[]{#MA-MIC-ANM-01-011-052}

[]{#MA-MSOL-ANM-01-011-052}

**Pregunta.** ¿Qué índices deja de mostrar la agrupación?

**Solución.** Los índices interiores entre dos extremos sucesivos, donde pueden producirse excursiones.

### Microcontrol 053

[]{#MA-MIC-ANM-01-011-053}

[]{#MA-MSOL-ANM-01-011-053}

**Pregunta.** ¿Qué condición interior recupera la convergencia completa?

**Solución.** Que las distancias de todos los totales de cada grupo a su extremo tiendan uniformemente a cero, además de convergencia de los extremos.

### Microcontrol 054

[]{#MA-MIC-ANM-01-011-054}

[]{#MA-MSOL-ANM-01-011-054}

**Pregunta.** ¿Qué dos hipótesis bastan para ese control interior?

**Solución.** $a_n\to0$ y una cota natural común $M$ para la longitud de cada grupo.

### Microcontrol 055

[]{#MA-MIC-ANM-01-011-055}

[]{#MA-MSOL-ANM-01-011-055}

**Pregunta.** ¿Cómo se usa la cota $M$?

**Solución.** Se hacen los términos menores que $\varepsilon/M$; cualquier distancia interior suma a lo sumo $M$ magnitudes y resulta menor que $\varepsilon$.

### Microcontrol 056

[]{#MA-MIC-ANM-01-011-056}

[]{#MA-MSOL-ANM-01-011-056}

**Pregunta.** ¿Qué muestra el bloque de $m$ aportes $1/m$ y $m$ aportes $-1/m$?

**Solución.** Términos que tienden a cero y extremos de grupo cero pueden coexistir con totales interiores uno; sin controlar longitud o excursión, la agrupación oculta divergencia.

## §11.8 — Elegir un control y certificar el error

### Microcontrol 057

[]{#MA-MIC-ANM-01-011-057}

[]{#MA-MSOL-ANM-01-011-057}

[]{#MA-SEC-ANM-01-011-008}

**Pregunta.** ¿Basta $E_n\le\varepsilon$ para certificar error estrictamente menor que $\varepsilon$?

**Solución.** No. Si sólo sabemos $|S-s_n|\le E_n$, es suficiente exigir $E_n<\varepsilon$.

### Microcontrol 058

[]{#MA-MIC-ANM-01-011-058}

[]{#MA-MSOL-ANM-01-011-058}

**Pregunta.** ¿Qué error tiene el punto medio de un intervalo certificado?

**Solución.** Si $L_n\le S\le U_n$, su punto medio tiene error a lo sumo $(U_n-L_n)/2$.

### Microcontrol 059

[]{#MA-MIC-ANM-01-011-059}

[]{#MA-MSOL-ANM-01-011-059}

**Pregunta.** ¿Debe ese punto medio ser una suma parcial?

**Solución.** No. Es un real construido como promedio de dos fronteras y puede no coincidir con ningún total.

### Microcontrol 060

[]{#MA-MIC-ANM-01-011-060}

[]{#MA-MSOL-ANM-01-011-060}

**Pregunta.** ¿Qué intervalo se obtiene con $s_4$ y $s_5$ en la armónica alternada?

**Solución.** $[37/60,47/60]$, cuyo punto medio es $7/10$ y cuyo semiancho es $1/12$.

### Microcontrol 061

[]{#MA-MIC-ANM-01-011-061}

[]{#MA-MSOL-ANM-01-011-061}

**Pregunta.** ¿Ese cálculo demuestra que la suma vale $7/10$?

**Solución.** No. Demuestra $|S-7/10|\le1/12$, una aproximación con error certificado.

### Microcontrol 062

[]{#MA-MIC-ANM-01-011-062}

[]{#MA-MSOL-ANM-01-011-062}

**Pregunta.** ¿Qué permite sumar linealmente dos series convergentes?

**Solución.** La identidad de sumas finitas y el álgebra de límites de C06 dan suma $\alpha A+\beta B$.

### Microcontrol 063

[]{#MA-MIC-ANM-01-011-063}

[]{#MA-MSOL-ANM-01-011-063}

**Pregunta.** ¿Qué suma tiene la cola reindexada que elimina $m$ términos?

**Solución.** $S-P_m$, con $P_m=\sum_{j=0}^{m-1}a_j$ y $P_0=0$.

### Microcontrol 064

[]{#MA-MIC-ANM-01-011-064}

[]{#MA-MSOL-ANM-01-011-064}

**Pregunta.** ¿Una muestra finita de totales demuestra convergencia?

**Solución.** No. La prueba debe controlar todos los bloques después de un corte; la muestra sólo ilustra valores seleccionados.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 11](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html) · [Ejercicios](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia-microcontroles.html)
