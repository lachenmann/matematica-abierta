---
content-id: MA-BCH-0297
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-023-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 23
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C23_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 23](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html) · [Ejercicios](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §23.1 — Cotas de valores y oscilación

### Microcontrol 001

[]{#MA-MIC-ANM-01-023-001}

[]{#MA-MSOL-ANM-01-023-001}

[]{#MA-SEC-ANM-01-023-001}

**Pregunta.** ¿Qué hipótesis permite extremos locales reales?

**Solución.** Imagen no vacía y acotada; completitud da ínfimo y supremo, sin pedir continuidad.

### Microcontrol 002

[]{#MA-MIC-ANM-01-023-002}

[]{#MA-MSOL-ANM-01-023-002}

**Pregunta.** ¿La oscilación es una derivada?

**Solución.** No: $\omega=M-m$, diferencia de cotas del conjunto de valores.

### Microcontrol 003

[]{#MA-MIC-ANM-01-023-003}

[]{#MA-MSOL-ANM-01-023-003}

**Pregunta.** ¿Deben alcanzarse $m$ y $M$?

**Solución.** No. Pueden ser límites de valores sin ser valores efectivos.

### Microcontrol 004

[]{#MA-MIC-ANM-01-023-004}

[]{#MA-MSOL-ANM-01-023-004}

**Pregunta.** ¿Qué ocurre al restringir a $J\subseteq K$?

**Solución.** El ínfimo no baja, el supremo no sube y la oscilación no aumenta.

### Microcontrol 005

[]{#MA-MIC-ANM-01-023-005}

[]{#MA-MSOL-ANM-01-023-005}

**Pregunta.** ¿Qué cota da $|f|\le B$ para la oscilación?

**Solución.** $0\le\omega\le2B$.

### Microcontrol 006

[]{#MA-MIC-ANM-01-023-006}

[]{#MA-MSOL-ANM-01-023-006}

**Pregunta.** ¿Cómo se obtiene una altura cercana al supremo?

**Solución.** Para η>0 existe $s$ con $f(s)>M-\eta$; si no, $M-\eta$ sería cota superior menor.

### Microcontrol 007

[]{#MA-MIC-ANM-01-023-007}

[]{#MA-MSOL-ANM-01-023-007}

**Pregunta.** ¿Cuál es la oscilación de $x^2$ en $[u,v]\subseteq[0,1]$?

**Solución.** $v^2-u^2$, por monotonía del cuadrado no negativo.

### Microcontrol 008

[]{#MA-MIC-ANM-01-023-008}

[]{#MA-MSOL-ANM-01-023-008}

**Pregunta.** ¿Dos muestras determinan la oscilación?

**Solución.** No. Una entrada no muestreada puede tener otro valor; hacen falta cotas para toda la pieza.

## §23.2 — Dos sumas que el refinamiento sí ordena

### Microcontrol 009

[]{#MA-MIC-ANM-01-023-009}

[]{#MA-MSOL-ANM-01-023-009}

[]{#MA-SEC-ANM-01-023-002}

**Pregunta.** ¿Cómo se define $L$?

**Solución.** Como $\sum_i m(f,I_i)\Delta_i$.

### Microcontrol 010

[]{#MA-MIC-ANM-01-023-010}

[]{#MA-MSOL-ANM-01-023-010}

**Pregunta.** ¿Cómo se define $U$?

**Solución.** Como $\sum_i M(f,I_i)\Delta_i$.

### Microcontrol 011

[]{#MA-MIC-ANM-01-023-011}

[]{#MA-MSOL-ANM-01-023-011}

**Pregunta.** ¿Dónde queda una suma etiquetada?

**Solución.** En $[L(f,P),U(f,P)]$ para la misma partición.

### Microcontrol 012

[]{#MA-MIC-ANM-01-023-012}

[]{#MA-MSOL-ANM-01-023-012}

**Pregunta.** ¿Qué expresa la brecha?

**Solución.** $G=U-L=\sum_i\omega(f,I_i)\Delta_i$.

### Microcontrol 013

[]{#MA-MIC-ANM-01-023-013}

[]{#MA-MSOL-ANM-01-023-013}

**Pregunta.** ¿Qué significa brecha cero sobre piezas cerradas?

**Solución.** Todas las oscilaciones son cero; constantes vecinas coinciden en nodos, luego la función es constante globalmente.

### Microcontrol 014

[]{#MA-MIC-ANM-01-023-014}

[]{#MA-MSOL-ANM-01-023-014}

**Pregunta.** ¿Qué sumas ordena el refinamiento?

**Solución.** Las inferiores no bajan y las superiores no suben; las etiquetadas arbitrarias no tienen esa monotonía.

### Microcontrol 015

[]{#MA-MIC-ANM-01-023-015}

[]{#MA-MSOL-ANM-01-023-015}

**Pregunta.** ¿Cómo se comparan $L(P)$ y $U(Q)$ con cortes distintos?

**Solución.** Por refinamiento común $R$: $L(P)\le L(R)\le U(R)\le U(Q)$.

### Microcontrol 016

[]{#MA-MIC-ANM-01-023-016}

[]{#MA-MSOL-ANM-01-023-016}

**Pregunta.** ¿Cuál es la brecha uniforme de $x^2$ en $[0,1]$?

**Solución.** $1/n$, positiva para cada n finito.

## §23.3 — Completitud y criterio de Darboux

### Microcontrol 017

[]{#MA-MIC-ANM-01-023-017}

[]{#MA-MSOL-ANM-01-023-017}

[]{#MA-SEC-ANM-01-023-003}

**Pregunta.** ¿Por qué los conjuntos de sumas son no vacíos?

**Solución.** La partición trivial es un elemento y proporciona ambas sumas.

### Microcontrol 018

[]{#MA-MIC-ANM-01-023-018}

[]{#MA-MSOL-ANM-01-023-018}

**Pregunta.** ¿Qué define la integral inferior?

**Solución.** $\ell_f=\sup\mathcal L_f$.

### Microcontrol 019

[]{#MA-MIC-ANM-01-023-019}

[]{#MA-MSOL-ANM-01-023-019}

**Pregunta.** ¿Qué define la integral superior?

**Solución.** $u_f=\inf\mathcal U_f$.

### Microcontrol 020

[]{#MA-MIC-ANM-01-023-020}

[]{#MA-MSOL-ANM-01-023-020}

**Pregunta.** ¿Por qué $\ell_f\le u_f$?

**Solución.** Cada suma superior acota todas las inferiores; tomar supremo y después ínfimo da el orden.

### Microcontrol 021

[]{#MA-MIC-ANM-01-023-021}

[]{#MA-MSOL-ANM-01-023-021}

**Pregunta.** ¿Cuál es el criterio de Darboux?

**Solución.** Para cada ε>0 existe una partición con brecha menor que ε, equivalente a $\ell_f=u_f$.

### Microcontrol 022

[]{#MA-MIC-ANM-01-023-022}

[]{#MA-MSOL-ANM-01-023-022}

**Pregunta.** ¿Cómo se aproxima a ambos extremos a la vez?

**Solución.** Se obtienen dos particiones por supremo/ínfimo y se toma su refinamiento común.

### Microcontrol 023

[]{#MA-MIC-ANM-01-023-023}

[]{#MA-MSOL-ANM-01-023-023}

**Pregunta.** ¿Una partición buena conserva su precisión al refinar?

**Solución.** Sí: la brecha no aumenta; la recíproca del criterio persistente usa reflexividad.

### Microcontrol 024

[]{#MA-MIC-ANM-01-023-024}

[]{#MA-MSOL-ANM-01-023-024}

**Pregunta.** ¿Qué error certifica $(L+U)/2$?

**Solución.** A lo sumo $(U-L)/2$ respecto de una integral ya existente.

## §23.4 — El puente hacia todas las sumas de Riemann

### Microcontrol 025

[]{#MA-MIC-ANM-01-023-025}

[]{#MA-MSOL-ANM-01-023-025}

[]{#MA-SEC-ANM-01-023-004}

**Pregunta.** ¿El contrato de Riemann obliga acotación?

**Solución.** Sí: fijar una partición fina y variar una etiqueta acota $f(t)$ en esa pieza; máximo finito cubre todo el dominio.

### Microcontrol 026

[]{#MA-MIC-ANM-01-023-026}

[]{#MA-MSOL-ANM-01-023-026}

**Pregunta.** ¿Se necesitan máximos alcanzados para aproximar $U$ con etiquetas?

**Solución.** No: se aproximan los supremos por η/(b−a) y se suman los errores finitos.

### Microcontrol 027

[]{#MA-MIC-ANM-01-023-027}

[]{#MA-MSOL-ANM-01-023-027}

**Pregunta.** ¿Una familia finita de testigos exige elección infinita?

**Solución.** No. La inducción finita añade un testigo para cada índice.

### Microcontrol 028

[]{#MA-MIC-ANM-01-023-028}

[]{#MA-MSOL-ANM-01-023-028}

**Pregunta.** ¿Qué prueba Riemann⇒Darboux?

**Solución.** Todos los errores menores que ε/4 y etiquetas próximas a extremos dan $U-L<\varepsilon$.

### Microcontrol 029

[]{#MA-MIC-ANM-01-023-029}

[]{#MA-MSOL-ANM-01-023-029}

**Pregunta.** ¿Por qué no basta refinar sólo la partición buena?

**Solución.** Riemann exige todas las particiones de malla pequeña, incluidas las que omiten sus nodos.

### Microcontrol 030

[]{#MA-MIC-ANM-01-023-030}

[]{#MA-MSOL-ANM-01-023-030}

**Pregunta.** ¿Qué cuenta $q$ en el puente inverso?

**Solución.** Los nodos interiores de la partición buena; a lo sumo q piezas de la nueva partición son divididas.

### Microcontrol 031

[]{#MA-MIC-ANM-01-023-031}

[]{#MA-MSOL-ANM-01-023-031}

**Pregunta.** ¿Qué cota conecta las brechas?

**Solución.** $G(Q)\le G(P_*)+4Bq\|Q\|$.

### Microcontrol 032

[]{#MA-MIC-ANM-01-023-032}

[]{#MA-MSOL-ANM-01-023-032}

**Pregunta.** ¿Qué se hace si $Bq=0$?

**Solución.** El término adicional es cero; cualquier radio positivo sirve, sin dividir por Bq.

## §23.5 — Clases integrables y radios útiles

### Microcontrol 033

[]{#MA-MIC-ANM-01-023-033}

[]{#MA-MSOL-ANM-01-023-033}

[]{#MA-SEC-ANM-01-023-005}

**Pregunta.** ¿Por qué una monótona en un cerrado está acotada?

**Solución.** Sus valores están entre los de los dos extremos.

### Microcontrol 034

[]{#MA-MIC-ANM-01-023-034}

[]{#MA-MSOL-ANM-01-023-034}

**Pregunta.** ¿Qué cota de brecha tiene una no decreciente?

**Solución.** $G\le\|P\|(f(b)-f(a))$, por diferencias no negativas y telescopía.

### Microcontrol 035

[]{#MA-MIC-ANM-01-023-035}

[]{#MA-MSOL-ANM-01-023-035}

**Pregunta.** ¿Qué cota da Lipschitz L?

**Solución.** $G\le L\|P\|(b-a)$.

### Microcontrol 036

[]{#MA-MIC-ANM-01-023-036}

[]{#MA-MSOL-ANM-01-023-036}

**Pregunta.** ¿Qué herramienta adicional usa el caso continuo?

**Solución.** Compacidad de C16 y escala uniforme de C17, reconstruida por un subcubrimiento finito.

### Microcontrol 037

[]{#MA-MIC-ANM-01-023-037}

[]{#MA-MSOL-ANM-01-023-037}

**Pregunta.** ¿Por qué continuidad en el cerrado da cota global?

**Solución.** Un subcubrimiento finito de vecindades con error1 da máximo finito de $|f(c_j)|+1$.

### Microcontrol 038

[]{#MA-MIC-ANM-01-023-038}

[]{#MA-MSOL-ANM-01-023-038}

**Pregunta.** ¿Cómo se fabrica un radio uniforme?

**Solución.** Cubrir con bolas de radios r_j/2 y tomar mínimo finito positivo r_j/2; dos puntos cercanos caen en una vecindad de control común.

### Microcontrol 039

[]{#MA-MIC-ANM-01-023-039}

[]{#MA-MSOL-ANM-01-023-039}

**Pregunta.** ¿Por qué se pide η=ε/(2(b−a))?

**Solución.** La oscilación puede quedar≤η al tomar extremos; la brecha≤ε/2 conserva margen estricto.

### Microcontrol 040

[]{#MA-MIC-ANM-01-023-040}

[]{#MA-MSOL-ANM-01-023-040}

**Pregunta.** ¿La continuidad es necesaria para integrar?

**Solución.** No. Monótonas con saltos, escalones y modificaciones finitas pueden ser integrables.

## §23.6 — Álgebra de funciones e integrales

### Microcontrol 041

[]{#MA-MIC-ANM-01-023-041}

[]{#MA-MSOL-ANM-01-023-041}

[]{#MA-SEC-ANM-01-023-006}

**Pregunta.** ¿Qué cota tiene la oscilación de una suma?

**Solución.** $\omega(f+g,J)\le\omega(f,J)+\omega(g,J)$.

### Microcontrol 042

[]{#MA-MIC-ANM-01-023-042}

[]{#MA-MSOL-ANM-01-023-042}

**Pregunta.** ¿Qué sucede con un múltiplo negativo?

**Solución.** Supremo e ínfimo intercambian su papel; $\omega(\alpha f)=|\alpha|\omega(f)$.

### Microcontrol 043

[]{#MA-MIC-ANM-01-023-043}

[]{#MA-MSOL-ANM-01-023-043}

**Pregunta.** ¿Qué controla el valor absoluto?

**Solución.** $\omega(|f|,J)\le\omega(f,J)$ por triangular inversa.

### Microcontrol 044

[]{#MA-MIC-ANM-01-023-044}

[]{#MA-MSOL-ANM-01-023-044}

**Pregunta.** ¿Qué cota controla un producto?

**Solución.** $\omega(fg,J)\le B_f\omega(g,J)+B_g\omega(f,J)$ con cotas absolutas universales.

### Microcontrol 045

[]{#MA-MIC-ANM-01-023-045}

[]{#MA-MSOL-ANM-01-023-045}

**Pregunta.** ¿Por qué se necesita un refinamiento común en álgebra?

**Solución.** Las particiones buenas de f y g pueden ser distintas; el refinamiento conserva ambas precisiones.

### Microcontrol 046

[]{#MA-MIC-ANM-01-023-046}

[]{#MA-MSOL-ANM-01-023-046}

**Pregunta.** ¿Cómo se identifica el valor de una combinación lineal?

**Solución.** Álgebra finita de sumas, radios comunes y unicidad del límite de Riemann.

### Microcontrol 047

[]{#MA-MIC-ANM-01-023-047}

[]{#MA-MSOL-ANM-01-023-047}

**Pregunta.** ¿Siempre $I_{fg}=I_f I_g$?

**Solución.** No: $f=g=x$ en[0,1] da1/3 frente a1/4.

### Microcontrol 048

[]{#MA-MIC-ANM-01-023-048}

[]{#MA-MSOL-ANM-01-023-048}

**Pregunta.** ¿Qué desigualdad integral da el valor absoluto?

**Solución.** $|I_f|\le I_{|f|}$, que puede ser estricta.

## §23.7 — Restringir, pegar y orientar

### Microcontrol 049

[]{#MA-MIC-ANM-01-023-049}

[]{#MA-MSOL-ANM-01-023-049}

[]{#MA-SEC-ANM-01-023-007}

**Pregunta.** ¿Cómo se restringe una función integrable?

**Solución.** Se inserta el corte y se divide la brecha total en dos no negativas; cada restricción cumple el criterio.

### Microcontrol 050

[]{#MA-MIC-ANM-01-023-050}

[]{#MA-MSOL-ANM-01-023-050}

**Pregunta.** ¿Cómo se pegan dos restricciones integrables?

**Solución.** Se concatenan particiones con brechas menores que ε/2; la brecha total es su suma.

### Microcontrol 051

[]{#MA-MIC-ANM-01-023-051}

[]{#MA-MSOL-ANM-01-023-051}

**Pregunta.** ¿Qué ocurre con el valor del nodo común?

**Solución.** Debe ser el mismo de la función en ambas restricciones; no se pegan dos valores incompatibles.

### Microcontrol 052

[]{#MA-MIC-ANM-01-023-052}

[]{#MA-MSOL-ANM-01-023-052}

**Pregunta.** ¿Cómo se prueba aditividad del valor?

**Solución.** Las sumas concatenadas son aditivas y sus errores controlados por brechas dan igualdad de integrales por tolerancia arbitraria.

### Microcontrol 053

[]{#MA-MIC-ANM-01-023-053}

[]{#MA-MSOL-ANM-01-023-053}

**Pregunta.** ¿Se probó aditividad numerable?

**Solución.** No: sólo finita, por inducción.

### Microcontrol 054

[]{#MA-MIC-ANM-01-023-054}

[]{#MA-MSOL-ANM-01-023-054}

**Pregunta.** ¿Cambiar valores en finitos puntos conserva la integral?

**Solución.** Sí por C22 y la equivalencia, aunque cambien sumas Darboux de una partición fija.

### Microcontrol 055

[]{#MA-MIC-ANM-01-023-055}

[]{#MA-MSOL-ANM-01-023-055}

**Pregunta.** ¿Qué significa orientación inversa?

**Solución.** Una convención $\int_b^a f=-\int_a^b f$ cuando existe integral ordenada, no piezas de anchura negativa.

### Microcontrol 056

[]{#MA-MIC-ANM-01-023-056}

[]{#MA-MSOL-ANM-01-023-056}

**Pregunta.** ¿Qué vale el intervalo degenerado?

**Solución.** Se declara $\int_a^a f=0$; no se usa una partición estricta de longitud cero.

## §23.8 — Certificar un valor y reconocer el alcance

### Microcontrol 057

[]{#MA-MIC-ANM-01-023-057}

[]{#MA-MSOL-ANM-01-023-057}

[]{#MA-SEC-ANM-01-023-008}

**Pregunta.** ¿Qué necesitan las cotas numéricas $a_i,b_i$?

**Solución.** Valer para todas las entradas de la pieza, no sólo las muestreadas.

### Microcontrol 058

[]{#MA-MIC-ANM-01-023-058}

[]{#MA-MSOL-ANM-01-023-058}

**Pregunta.** ¿Una brecha pequeña una sola vez prueba integrabilidad?

**Solución.** No. El criterio exige particiones buenas para cada tolerancia.

### Microcontrol 059

[]{#MA-MIC-ANM-01-023-059}

[]{#MA-MSOL-ANM-01-023-059}

**Pregunta.** ¿Cuál es el encierro de $x^2$ con n4?

**Solución.** $[7/32,15/32]$.

### Microcontrol 060

[]{#MA-MIC-ANM-01-023-060}

[]{#MA-MSOL-ANM-01-023-060}

**Pregunta.** ¿Cuál es su punto medio y error certificado?

**Solución.** Punto medio11/32; error certificado1/8 y error real1/96 frente a1/3.

### Microcontrol 061

[]{#MA-MIC-ANM-01-023-061}

[]{#MA-MSOL-ANM-01-023-061}

**Pregunta.** ¿Qué n certifica error medio menor que1/100?

**Solución.** n>50 mediante1/(2n); es el aproximante medio de cotas, no toda suma etiquetada.

### Microcontrol 062

[]{#MA-MIC-ANM-01-023-062}

[]{#MA-MSOL-ANM-01-023-062}

**Pregunta.** ¿Qué brecha tiene el pico con nodos1/2±r?

**Solución.** 2r; las dos piezas que contienen el pico tienen supremo1 y anchuras r.

### Microcontrol 063

[]{#MA-MIC-ANM-01-023-063}

[]{#MA-MSOL-ANM-01-023-063}

**Pregunta.** ¿El pico integrable tiene alguna partición de brecha cero?

**Solución.** No. Su valor integral es0, pero toda partición lo contiene en una pieza de anchura positiva con oscilación1.

### Microcontrol 064

[]{#MA-MIC-ANM-01-023-064}

[]{#MA-MSOL-ANM-01-023-064}

**Pregunta.** ¿Qué impide integrar una función que toma0 y1 en toda pieza?

**Solución.** Todas las brechas son b−a>0; integral inferior0 y superior b−a.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 23](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html) · [Ejercicios](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux-microcontroles.html)
