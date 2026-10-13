---
content-id: MA-BCH-0317
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-028-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 28
date-modified: '2026-10-13'
provenance:
  type: original
  sources:
  - ANM-C28_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 28](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html) · [Ejercicios](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §28.1 — Fijar una fila para conservar continuidad

### Microcontrol 001

[]{#MA-MIC-ANM-01-028-001}

[]{#MA-MSOL-ANM-01-028-001}

[]{#MA-SEC-ANM-01-028-001}

**Pregunta.** ¿Qué se fija antes de obtener el radio de continuidad?

**Solución.** Para una tolerancia $\varepsilon>0$, se elige primero una fila $f_N$ de la cola cuyo error respecto del límite sea menor que $\varepsilon/3$ en toda entrada. Después se usa la continuidad de esa fila fija en el centro para obtener un radio. Ese orden permite controlar la aproximación también en las entradas que el radio admite.

### Microcontrol 002

[]{#MA-MIC-ANM-01-028-002}

[]{#MA-MSOL-ANM-01-028-002}

**Pregunta.** ¿Cuántos errores controla la prueba de R1?

**Solución.** La triangular separa $|f(x)-f(x_0)|$ en el error entre $f$ y la fila escogida en $x$, la variación de esa fila entre $x$ y $x_0$, y el error de aproximación en $x_0$. Pedir a cada término una cota estricta $\varepsilon/3$ hace la suma menor que $\varepsilon$.

### Microcontrol 003

[]{#MA-MIC-ANM-01-028-003}

[]{#MA-MSOL-ANM-01-028-003}

**Pregunta.** ¿La fila fijada necesita una cota global de valores?

**Solución.** Basta que la fila escogida sea continua en el centro y esté uniformemente próxima al destino. Una barrera global de sus valores no interviene en la triangular de tres errores. La familia $x+1/(n+1)$ sobre la recta conserva continuidad aunque todas las funciones sean no acotadas.

### Microcontrol 004

[]{#MA-MIC-ANM-01-028-004}

[]{#MA-MSOL-ANM-01-028-004}

**Pregunta.** ¿Los radios de continuidad deben ser comunes a todas las filas?

**Solución.** Para cada tolerancia se fija una sola fila y se utiliza su radio de continuidad. Las otras filas pueden tener radios diferentes. La uniformidad controla las dos aproximaciones al destino y evita necesitar un radio común para toda la familia.

### Microcontrol 005

[]{#MA-MIC-ANM-01-028-005}

[]{#MA-MSOL-ANM-01-028-005}

**Pregunta.** ¿Qué hipótesis de filas conserva continuidad uniforme?

**Solución.** Si las filas son uniformemente continuas, el radio de la fila escogida sirve para cualquier par de entradas próximas. Los dos errores de aproximación ya son globales, así la triangular prueba continuidad uniforme del límite. No se exige un radio previo compartido por todas las filas.

### Microcontrol 006

[]{#MA-MIC-ANM-01-028-006}

[]{#MA-MSOL-ANM-01-028-006}

**Pregunta.** ¿Un destino continuo obliga convergencia uniforme?

**Solución.** Las potencias en $[0,1)$ convergen puntualmente a la función cero, que es continua. Sin embargo, para cada $n\ge1$ el supremo de su error es uno por las entradas próximas al extremo ausente. La continuidad de la candidata no obliga al control uniforme de todas las filas posteriores.

### Microcontrol 007

[]{#MA-MIC-ANM-01-028-007}

[]{#MA-MSOL-ANM-01-028-007}

**Pregunta.** ¿Qué continuidad se usa en bordes del dominio?

**Solución.** Se usa continuidad relativa al mismo dominio $X$. Las entradas próximas consideradas deben pertenecer a $X$, también en un extremo. El argumento de la fila fija no necesita prolongar las funciones fuera del dominio.

### Microcontrol 008

[]{#MA-MIC-ANM-01-028-008}

[]{#MA-MSOL-ANM-01-028-008}

**Pregunta.** ¿Qué ocurre en un dominio vacío?

**Solución.** En el dominio vacío sólo existe la función vacía y no hay centros en los que comprobar continuidad. Tanto el contrato uniforme como la conclusión de continuidad se satisfacen vacuamente. El caso no requiere escoger una fila para una entrada inexistente.

## §28.2 — Dos límites con un presupuesto común

### Microcontrol 009

[]{#MA-MIC-ANM-01-028-009}

[]{#MA-MSOL-ANM-01-028-009}

[]{#MA-SEC-ANM-01-028-002}

**Pregunta.** ¿Por qué el centro de R2 debe acumular?

**Solución.** La condición de acumulación asegura entradas de $X$ distintas del centro y arbitrariamente próximas a él. Así los límites relativos perforados tienen contenido efectivo y son únicos. Sin ella, las condiciones de ventana podrían ser vacuas y no determinar un destino real.

### Microcontrol 010

[]{#MA-MIC-ANM-01-028-010}

[]{#MA-MSOL-ANM-01-028-010}

**Pregunta.** ¿Qué se construye primero en R2?

**Solución.** Primero se demuestra que los destinos $p_n$ de las filas forman una sucesión real de Cauchy. Completitud produce su límite $p$. Sólo después se combina una fila próxima a $f$, su límite local y su destino próximo a $p$ para demostrar que $f(x)\to p$.

### Microcontrol 011

[]{#MA-MIC-ANM-01-028-011}

[]{#MA-MSOL-ANM-01-028-011}

**Pregunta.** ¿Qué cota queda al pasar una entrada al límite?

**Solución.** Si las diferencias de filas están controladas por $\eta/2$ en las entradas cercanas, al pasar $x$ al centro se obtiene $|p_n-p_m|\le\eta/2$. El límite conserva una cota superior no estricta. Como $\eta/2<\eta$, queda el margen necesario para Cauchy de los destinos.

### Microcontrol 012

[]{#MA-MIC-ANM-01-028-012}

[]{#MA-MSOL-ANM-01-028-012}

**Pregunta.** ¿Qué construye el destino de una sucesión de Cauchy real?

**Solución.** Una sucesión real de Cauchy tiene un límite real por el criterio de C10, basado en completitud de $\mathbb R$. Ese paso construye el destino de los $p_n$ antes de afirmar que el límite de funciones tiene un límite local.

### Microcontrol 013

[]{#MA-MIC-ANM-01-028-013}

[]{#MA-MSOL-ANM-01-028-013}

**Pregunta.** ¿El valor de la función en el centro participa?

**Solución.** El límite relativo perforado sólo utiliza entradas de $X$ distintas de $a$. El valor en el centro, si $a\in X$, puede cambiar sin alterar esos límites. R2 compara destinos de ventanas perforadas y no exige que coincidan con $f(a)$.

### Microcontrol 014

[]{#MA-MIC-ANM-01-028-014}

[]{#MA-MSOL-ANM-01-028-014}

**Pregunta.** ¿Basta uniformidad en una ventana fija?

**Solución.** Si hay uniformidad en $Y=X\cap\{x:0<|x-a|<r\}$ para un $r>0$ fijo, se aplica R2 a ese dominio común. Conserva la acumulación en $a$ y los límites de las filas. El límite obtenido también vale en $X$ porque toda entrada suficientemente próxima y distinta del centro pertenece a $Y$.

### Microcontrol 015

[]{#MA-MIC-ANM-01-028-015}

[]{#MA-MSOL-ANM-01-028-015}

**Pregunta.** ¿Qué valor conserva la ruta racional $x_n=1/(n+1)$?

**Solución.** En $x_n=1/(n+1)$, el producto $(n+1)x_n$ es uno y la capa racional vale $1/2$ en toda etapa. Sus límites iterados son uno y cero según el orden. La ruta dada muestra un comportamiento conjunto que la convergencia puntual sola no determina.

### Microcontrol 016

[]{#MA-MIC-ANM-01-028-016}

[]{#MA-MSOL-ANM-01-028-016}

**Pregunta.** ¿Se escoge una ruta por cada escala en la prueba?

**Solución.** La prueba de R2 obtiene cortes y ventanas para entradas arbitrarias. No construye una sucesión de entradas por selección de testigos. Cuando compara diagonales, la ruta está dada de antemano, como $1/(n+1)$ en el contraejemplo racional.

## §28.3 — Compacidad y monotonía: el mecanismo de Dini

### Microcontrol 017

[]{#MA-MIC-ANM-01-028-017}

[]{#MA-MSOL-ANM-01-028-017}

[]{#MA-SEC-ANM-01-028-003}

**Pregunta.** ¿Qué error es no negativo en Dini decreciente?

**Solución.** Si $f_n$ decrece por columnas hacia $f$, para cada entrada todos sus términos están por encima del límite. Así $e_n=f_n-f\ge0$, y esos errores decrecen a cero. La no negatividad convierte su control directo en control del error absoluto.

### Microcontrol 018

[]{#MA-MIC-ANM-01-028-018}

[]{#MA-MSOL-ANM-01-028-018}

**Pregunta.** ¿Qué hace abiertos los conjuntos de error pequeño?

**Solución.** La diferencia $e_n=f_n-f$ es continua cuando lo son la fila y el destino. Por tanto $U_n=\{x:e_n(x)<\varepsilon/2\}$ es abierto relativo al dominio. Esos conjuntos forman la cubierta de errores pequeños que usa Dini.

### Microcontrol 019

[]{#MA-MIC-ANM-01-028-019}

[]{#MA-MSOL-ANM-01-028-019}

**Pregunta.** ¿Qué permite obtener una subcubierta finita?

**Solución.** La convergencia puntual hace que los abiertos $U_n$ cubran el dominio compacto. Compacidad proporciona una subcubierta finita. La información de esa lista finita permite reunir índices en un único corte sin escoger uno por cada entrada del compacto.

### Microcontrol 020

[]{#MA-MIC-ANM-01-028-020}

[]{#MA-MSOL-ANM-01-028-020}

**Pregunta.** ¿Qué convierte los índices finitos en una cola común?

**Solución.** Los errores decrecen, así $U_n\subseteq U_{n+1}$. Si una subcubierta finita tiene índices $n_1,\ldots,n_k$, el máximo $N$ contiene en $U_N$ todos sus conjuntos. Por tanto todo el dominio está en $U_N$ y sigue estando en $U_n$ para $n\ge N$.

### Microcontrol 021

[]{#MA-MIC-ANM-01-028-021}

[]{#MA-MSOL-ANM-01-028-021}

**Pregunta.** ¿Dini entrega una tasa numérica general?

**Solución.** Dini asegura que para cada tolerancia existe un corte uniforme, mediante una subcubierta finita. Ese razonamiento no proporciona una fórmula general de velocidad para todas las familias. Una tasa numérica requiere información cuantitativa adicional sobre la familia concreta.

### Microcontrol 022

[]{#MA-MIC-ANM-01-028-022}

[]{#MA-MSOL-ANM-01-028-022}

**Pregunta.** ¿Qué falta en las potencias sobre $(0,1)$?

**Solución.** En $(0,1)$ las potencias son continuas, decrecen por columnas y tienen límite continuo cero. Su error supremo permanece uno, así no hay uniformidad. El dominio no es compacto y falla el paso que debería reducir la cubierta de errores pequeños a una subcubierta finita.

### Microcontrol 023

[]{#MA-MIC-ANM-01-028-023}

[]{#MA-MSOL-ANM-01-028-023}

**Pregunta.** ¿Qué falta en las indicadoras decrecientes del intervalo pequeño?

**Solución.** Para $s_n=\mathbf1_{(0,1/(n+1))}$, el dominio es compacto, las columnas decrecen y el límite cero es continuo. Pero las filas tienen saltos y no son continuas. Sus errores alcanzan uno en cada etapa, así la hipótesis de regularidad de filas no puede omitirse.

### Microcontrol 024

[]{#MA-MIC-ANM-01-028-024}

[]{#MA-MSOL-ANM-01-028-024}

**Pregunta.** ¿Qué falta en las tiendas continuas de altura uno?

**Solución.** Las tiendas son continuas en $[0,1]$ y convergen puntualmente a cero continuo, pero sus columnas no forman una familia monótona. El pico se desplaza y conserva altura uno. La monotonía que en Dini prolonga un control de etapa a toda la cola falta aquí.

## §28.4 — La integral soporta un error global pequeño

### Microcontrol 025

[]{#MA-MIC-ANM-01-028-025}

[]{#MA-MSOL-ANM-01-028-025}

[]{#MA-SEC-ANM-01-028-004}

**Pregunta.** ¿Qué debe probarse antes de escribir la integral del destino?

**Solución.** Antes de comparar valores integrales se prueba que $f$ está acotada usando una fila integrable próxima. La comparación de brechas de Darboux con esa fila proporciona después particiones de brecha arbitrariamente pequeña para $f$. Sólo entonces se escribe la integral del destino.

### Microcontrol 026

[]{#MA-MIC-ANM-01-028-026}

[]{#MA-MSOL-ANM-01-028-026}

**Pregunta.** ¿Cómo cambia la brecha Darboux con error global $\delta$?

**Solución.** Si $|f-f_n|\le\delta$, en cada pieza la oscilación de $f$ es a lo sumo la de $f_n$ más $2\delta$. Multiplicar por anchuras y sumar da $G(f,P)\le G(f_n,P)+2\delta(b-a)$. Esta cota permite transferir particiones buenas antes de comparar integrales.

### Microcontrol 027

[]{#MA-MIC-ANM-01-028-027}

[]{#MA-MSOL-ANM-01-028-027}

**Pregunta.** ¿Por qué aparecen dos contribuciones de error en la brecha?

**Solución.** La cota $|f-f_n|\le\delta$ permite que el supremo local de $f$ suba hasta $\delta$ respecto del de $f_n$ y que su ínfimo baje hasta $\delta$. Al restar extremos se suman esos dos errores. Por eso la brecha recibe $2\delta$ por la longitud total.

### Microcontrol 028

[]{#MA-MIC-ANM-01-028-028}

[]{#MA-MSOL-ANM-01-028-028}

**Pregunta.** ¿Qué error controla el valor integral?

**Solución.** Una vez existentes ambas integrales, $|I_n-I|\le\int_a^b|f_n-f|\le(b-a)E_n$. La longitud fija multiplica la envolvente global de la cola. Como $E_n\to0$, los valores integrales convergen al del destino.

### Microcontrol 029

[]{#MA-MIC-ANM-01-028-029}

[]{#MA-MSOL-ANM-01-028-029}

**Pregunta.** ¿Debe alcanzarse la envolvente para integrar su cota?

**Solución.** Por definición, cada error es a lo sumo el supremo $E_n$, aunque ningún punto lo alcance. Esa desigualdad universal basta para integrar la constante $E_n$ y obtener la cota de error. El argumento no necesita un punto de máxima discrepancia.

### Microcontrol 030

[]{#MA-MIC-ANM-01-028-030}

[]{#MA-MSOL-ANM-01-028-030}

**Pregunta.** ¿Cómo se trata un segmento de longitud cero?

**Solución.** En un segmento degenerado se declara la integral cero. Todas las comparaciones de valores integrales son entonces directas y no se dividen por una longitud nula. Las pruebas por particiones de longitud positiva se realizan bajo $a<b$.

### Microcontrol 031

[]{#MA-MIC-ANM-01-028-031}

[]{#MA-MSOL-ANM-01-028-031}

**Pregunta.** ¿Qué conserva la integral de las tiendas normalizadas?

**Solución.** Si $b_n=(n+3)t_n$, cada fila es continua e integra uno, porque la altura compensa la anchura del soporte. El límite puntual es cero y su integral vale cero. Las dos operaciones existen y sus valores difieren; la familia no converge uniformemente.

### Microcontrol 032

[]{#MA-MIC-ANM-01-028-032}

[]{#MA-MSOL-ANM-01-028-032}

**Pregunta.** ¿Qué falla para el destino Dirichlet?

**Solución.** Los indicadores de conjuntos finitos de racionales tienen integral cero y límite puntual Dirichlet. Ese destino no es integrable propiamente por C25. Falta una de las operaciones para formar la igualdad de intercambio, a diferencia de un caso con dos valores existentes distintos.

## §28.5 — Acumulaciones, pesos y extremos variables

### Microcontrol 033

[]{#MA-MIC-ANM-01-028-033}

[]{#MA-MSOL-ANM-01-028-033}

[]{#MA-SEC-ANM-01-028-005}

**Pregunta.** ¿Qué corte controla todas las acumulaciones?

**Solución.** En un segmento de longitud $\ell$, el error de la acumulación desde $c$ hasta cualquier $x$ está acotado por $|x-c|E_n\le\ell E_n$. Un corte de las integrandas que haga pequeña esta cota sirve simultáneamente para todos los destinos de acumulación.

### Microcontrol 034

[]{#MA-MIC-ANM-01-028-034}

[]{#MA-MSOL-ANM-01-028-034}

**Pregunta.** ¿Qué se hace si el destino de acumulación precede al anclaje?

**Solución.** Si $x<c$, se escribe $\int_c^x(f_n-f)=-\int_x^c(f_n-f)$ y se estima la magnitud en el segmento ordenado. Se obtiene la misma cota $|x-c|E_n$. En $x=c$ ambas acumulaciones son cero.

### Microcontrol 035

[]{#MA-MIC-ANM-01-028-035}

[]{#MA-MSOL-ANM-01-028-035}

**Pregunta.** ¿Qué hipótesis permite identificar la derivada de toda acumulación?

**Solución.** La integrabilidad garantiza acumulaciones continuas, pero para recuperar la tasa al derivar en un centro hace falta continuidad de la integranda allí. Si todas las integrandas son continuas y convergen uniformemente, R1 conserva continuidad del destino y C24 identifica también la derivada de su acumulada.

### Microcontrol 036

[]{#MA-MIC-ANM-01-028-036}

[]{#MA-MSOL-ANM-01-028-036}

**Pregunta.** ¿Qué debe acreditarse para un peso integrable fijo?

**Solución.** El peso $w$ y las integrandas deben ser integrables para que sus productos existan como integrandos de Riemann. Luego $|w(f_n-f)|\le E_n|w|$ da error ponderado a lo sumo $E_n\int|w|$. Una barrera $|w|\le M$ proporciona además la cota $M\ell E_n$.

### Microcontrol 037

[]{#MA-MIC-ANM-01-028-037}

[]{#MA-MSOL-ANM-01-028-037}

**Pregunta.** ¿Cuántos errores hay al mover ambos extremos?

**Solución.** Se separa primero el cambio de integranda con los extremos móviles fijos. Después se corrigen el extremo inicial y el final usando la integranda límite. La triangular suma los tres costes: $\ell E_n$, $B|u_n-u|$ y $B|v_n-v|$ si $|f|\le B$.

### Microcontrol 038

[]{#MA-MIC-ANM-01-028-038}

[]{#MA-MSOL-ANM-01-028-038}

**Pregunta.** ¿Dónde deben permanecer los extremos móviles?

**Solución.** Todos los extremos deben permanecer en un mismo segmento cerrado $[a,b]$, con longitud finita. Eso asegura las restricciones integrables, una barrera de distancias y los destinos de extremos dentro del marco. Si la longitud crece sin límite, puede compensar un error de integranda que tiende a cero.

### Microcontrol 039

[]{#MA-MIC-ANM-01-028-039}

[]{#MA-MSOL-ANM-01-028-039}

**Pregunta.** ¿Cuánto integra $1/(n+1)$ sobre $[0,n+1]$?

**Solución.** La tasa constante $1/(n+1)$ integra sobre $[0,n+1]$ su altura por la longitud: $(1/(n+1))(n+1)=1$. Es uniforme hacia cero sobre la recta, pero los intervalos crecen. No hay una longitud fija que haga tender a cero la cota integral.

### Microcontrol 040

[]{#MA-MIC-ANM-01-028-040}

[]{#MA-MSOL-ANM-01-028-040}

**Pregunta.** ¿Uniformidad es necesaria para igualdad de límites integrales?

**Solución.** Las tiendas de altura uno no convergen uniformemente hacia cero, pues su máximo de error sigue siendo uno. Sin embargo integran $1/(n+3)\to0$, igual a la integral del límite puntual. Uniformidad es una condición suficiente para el intercambio general, pero no necesaria para cada igualdad concreta.

## §28.6 — Derivadas uniformes y un valor de anclaje

### Microcontrol 041

[]{#MA-MIC-ANM-01-028-041}

[]{#MA-MSOL-ANM-01-028-041}

[]{#MA-SEC-ANM-01-028-006}

**Pregunta.** ¿Qué dato fija la constante aditiva en R6?

**Solución.** La derivada sólo determina variaciones, dejando una constante aditiva. El dato $f_n(c)\to\lambda$ fija esa constante en el límite. Junto con el control uniforme de derivadas, permite estimar todos los valores por su distancia al anclaje.

### Microcontrol 042

[]{#MA-MIC-ANM-01-028-042}

[]{#MA-MSOL-ANM-01-028-042}

**Pregunta.** ¿En qué dominio se controlan uniformemente las derivadas?

**Solución.** En R6 se supone $g_n=f_n'$ uniformemente convergente en $(a,b)$, el interior del mismo segmento donde las filas son continuas hasta los bordes. Las cotas de derivadas se usan allí para aplicar Lagrange a segmentos con extremos en $[a,b]$.

### Microcontrol 043

[]{#MA-MIC-ANM-01-028-043}

[]{#MA-MSOL-ANM-01-028-043}

**Pregunta.** ¿Qué herramienta convierte derivadas en cotas de incrementos?

**Solución.** Lagrange y su consecuencia de C19 dicen que una cota $|H'|\le M$ en el interior limita $|H(y)-H(x)|\le M|y-x|$. Se aplica a diferencias de filas continuas en el segmento y derivables dentro. No exige continuidad de la derivada.

### Microcontrol 044

[]{#MA-MIC-ANM-01-028-044}

[]{#MA-MSOL-ANM-01-028-044}

**Pregunta.** ¿Qué se fija antes de pasar una etapa al límite en incrementos?

**Solución.** Para pasar una etapa al límite en la comparación de incrementos, se fijan la fila $n$ y las entradas $x,y$. Sólo se hace crecer el otro índice $m$. Así los valores de sus dos columnas convergen y la cota de error de derivadas $E_m$ tiende a cero.

### Microcontrol 045

[]{#MA-MIC-ANM-01-028-045}

[]{#MA-MSOL-ANM-01-028-045}

**Pregunta.** ¿Se supone derivabilidad del destino para obtener esa cota?

**Solución.** La estimación de incrementos de $f-f_n$ se obtiene pasando al límite desigualdades de diferencias entre filas derivables. Todavía no se deriva $f$. Después, dividir por la distancia y comparar con una fila fija proporciona la prueba de derivabilidad del destino.

### Microcontrol 046

[]{#MA-MIC-ANM-01-028-046}

[]{#MA-MSOL-ANM-01-028-046}

**Pregunta.** ¿Cómo se divide la cota de incrementos?

**Solución.** Si $x\ne x_0$, la distancia $|x-x_0|$ es positiva. La cota de incrementos proporcional a esa distancia permite dividir y controlar en $E_n$ la magnitud de la diferencia de cocientes. El signo del incremento no altera esa estimación de magnitudes.

### Microcontrol 047

[]{#MA-MIC-ANM-01-028-047}

[]{#MA-MSOL-ANM-01-028-047}

**Pregunta.** ¿R6 necesita derivadas continuas?

**Solución.** R6 pide derivabilidad de las filas y convergencia uniforme de sus derivadas, pero no continuidad de ellas. La prueba usa Lagrange, cotas de incrementos y la definición de derivada de una fila fija. No necesita integrar la función límite de derivadas.

### Microcontrol 048

[]{#MA-MIC-ANM-01-028-048}

[]{#MA-MSOL-ANM-01-028-048}

**Pregunta.** ¿Qué factor limita la uniformidad de valores en dominios no acotados?

**Solución.** La cota de valores contiene $|x-c|E_n$, además del error en el anclaje. En un segmento fijo, $|x-c|$ tiene una barrera finita. En toda la recta puede crecer sin límite, de modo que uniformidad de derivadas no obliga a uniformidad global de valores.

## §28.7 — Lo que la convergencia de valores no controla

### Microcontrol 049

[]{#MA-MIC-ANM-01-028-049}

[]{#MA-MSOL-ANM-01-028-049}

[]{#MA-SEC-ANM-01-028-007}

**Pregunta.** ¿Qué envolvente tienen las raíces suavizadas frente a $|x|$?

**Solución.** Para $q_n(x)=\sqrt{x^2+(n+1)^{-2}}$, la diferencia con $|x|$ está entre cero y $1/(n+1)$. La cota se alcanza en cero, así es la envolvente exacta. Tiende a cero uniformemente aunque el destino tenga una esquina.

### Microcontrol 050

[]{#MA-MIC-ANM-01-028-050}

[]{#MA-MSOL-ANM-01-028-050}

**Pregunta.** ¿Por qué $|x|$ no deriva en cero?

**Solución.** En cero, el cociente de $|x|$ es $|h|/h$: vale menos uno cuando $h<0$ y uno cuando $h>0$. Los dos lados tienen límites distintos, así no existe una derivada bilateral. La convergencia uniforme de valores no impide esa pérdida de derivabilidad.

### Microcontrol 051

[]{#MA-MIC-ANM-01-028-051}

[]{#MA-MSOL-ANM-01-028-051}

**Pregunta.** ¿Qué valor tienen $h_n^{\prime}$ en cero?

**Solución.** La fórmula $h_n'(x)=(1-(n+1)x^2)/(1+(n+1)x^2)^2$ da $h_n'(0)=1$ en todo índice. Esa columna de derivadas conserva el valor uno mientras las funciones originales tienden uniformemente a cero.

### Microcontrol 052

[]{#MA-MIC-ANM-01-028-052}

[]{#MA-MSOL-ANM-01-028-052}

**Pregunta.** ¿Qué derivada tiene el destino cero de $h_n$?

**Solución.** El destino de $h_n$ es la función cero, cuya derivada vale cero en todos los centros. El límite puntual de las derivadas, en cambio, vale uno en cero. Ambas operaciones existen y no coinciden en esa entrada.

### Microcontrol 053

[]{#MA-MIC-ANM-01-028-053}

[]{#MA-MSOL-ANM-01-028-053}

**Pregunta.** ¿Qué no detecta la operación de derivar?

**Solución.** Sumar una constante a una función no cambia su derivada. En un dominio con componentes separadas pueden escogerse constantes diferentes en cada una. El control de derivadas necesita datos de valores que fijen esas constantes.

### Microcontrol 054

[]{#MA-MIC-ANM-01-028-054}

[]{#MA-MSOL-ANM-01-028-054}

**Pregunta.** ¿Una ancla controla otra componente separada?

**Solución.** Lagrange compara entradas unidas por un segmento contenido en el dominio. Si dos componentes están separadas por un hueco, una ancla en la primera no determina la constante de la segunda. Hace falta un dato de anclaje por componente que se quiera controlar.

### Microcontrol 055

[]{#MA-MIC-ANM-01-028-055}

[]{#MA-MSOL-ANM-01-028-055}

**Pregunta.** ¿Dónde convergen uniformemente los valores $x/(n+1)$?

**Solución.** En $[-M,M]$, la envolvente de $x/(n+1)$ respecto de cero es $M/(n+1)\to0$. En toda la recta el error de cada fila es no acotado, y $x=n+1$ mantiene error uno. El control es uniforme en cada segmento acotado, sin serlo globalmente.

### Microcontrol 056

[]{#MA-MIC-ANM-01-028-056}

[]{#MA-MSOL-ANM-01-028-056}

**Pregunta.** ¿La sola norma de valores controla la derivada?

**Solución.** La familia $h_n$ tiene error global $1/(2\sqrt{n+1})\to0$ en sus valores. Sus derivadas conservan altura uno en cero y tienden a cero fuera, dando un destino discontinuo. El control de valores no aporta por sí solo la uniformidad de derivadas requerida por R6.

## §28.8 — Certificar varias operaciones a la vez

### Microcontrol 057

[]{#MA-MIC-ANM-01-028-057}

[]{#MA-MSOL-ANM-01-028-057}

[]{#MA-SEC-ANM-01-028-008}

**Pregunta.** ¿Qué envolvente tiene la capa de derivadas del paquete polinómico?

**Solución.** Para $f_n=x^2+(1-2^{-n})x$ y $f=x^2+x$, las derivadas difieren por la constante $-2^{-n}$. Su magnitud es $2^{-n}$ en toda entrada, así ésa es la envolvente exacta de la capa de derivadas.

### Microcontrol 058

[]{#MA-MIC-ANM-01-028-058}

[]{#MA-MSOL-ANM-01-028-058}

**Pregunta.** ¿Qué anclaje del paquete es exacto?

**Solución.** Todas las filas del paquete y su destino valen cero en $x=0$. El anclaje no tiene error y fija exactamente la constante aditiva. La cota de valores de R6 queda entonces reducida a $|x|2^{-n}$.

### Microcontrol 059

[]{#MA-MIC-ANM-01-028-059}

[]{#MA-MSOL-ANM-01-028-059}

**Pregunta.** ¿Qué envolvente tiene su error de acumulación?

**Solución.** Con acumulación desde cero, la diferencia es $A_n(x)-A(x)=-2^{-n}x^2/2$. En $[-1,1]$ su magnitud máxima es $2^{-n}/2$, alcanzada en los dos extremos. La cota describe todas las acumulaciones, incluso las orientadas hacia entradas negativas.

### Microcontrol 060

[]{#MA-MIC-ANM-01-028-060}

[]{#MA-MSOL-ANM-01-028-060}

**Pregunta.** ¿El error integral firmado en el segmento simétrico es igual a esa envolvente?

**Solución.** El error de integrandas es $-2^{-n}x$, que es impar. Su integral en $[-1,1]$ es cero por cancelación de los dos lados. Eso no anula el error de cada acumulación desde cero, cuya envolvente es $2^{-n}/2$.

### Microcontrol 061

[]{#MA-MIC-ANM-01-028-061}

[]{#MA-MSOL-ANM-01-028-061}

**Pregunta.** ¿Sirve $n=3$ para error estrictamente menor que $1/8$?

**Solución.** En $n=3$, el error de derivadas vale $2^{-3}=1/8$, igual a la tolerancia y no estrictamente menor. En $n=4$ vale $1/16$ y sigue disminuyendo en toda la cola. Los índices anteriores tampoco sirven, así cuatro es el corte mínimo.

### Microcontrol 062

[]{#MA-MIC-ANM-01-028-062}

[]{#MA-MSOL-ANM-01-028-062}

**Pregunta.** ¿Qué dos capas suma la norma $C^1$?

**Solución.** La norma $C^1$ suma $\|u\|_\infty$ y $\|u'\|_\infty$. La segunda capa usa la extensión continua de la derivada interior al cerrado. Las dos imágenes son acotadas por compacidad y controlan, respectivamente, alturas y pendientes.

### Microcontrol 063

[]{#MA-MIC-ANM-01-028-063}

[]{#MA-MSOL-ANM-01-028-063}

**Pregunta.** ¿Qué anclas se necesitan para controlar órdenes hasta $r$?

**Solución.** Si se controla uniformemente la derivada de orden $r$, se necesitan datos convergentes en un mismo anclaje para los órdenes $0,1,\ldots,r-1$. Cada descenso de orden utiliza el dato correspondiente para fijar su constante. La inducción tiene un número finito de pasos.

### Microcontrol 064

[]{#MA-MIC-ANM-01-028-064}

[]{#MA-MSOL-ANM-01-028-064}

**Pregunta.** ¿Cuál es la única puerta siguiente?

**Solución.** C29 aplica estos resultados a sucesiones de sumas parciales para estudiar series de funciones y de potencias. El trabajo de C28 termina con los contratos de intercambio y sus certificados, que quedan disponibles para ese desarrollo siguiente.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 28](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html) · [Ejercicios](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones-microcontroles.html)
