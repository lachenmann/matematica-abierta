---
content-id: MA-BCH-0293
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-022-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 22
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C22_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 22](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html) · [Ejercicios](analisis-para-matematicos-capitulo-22-partir-refinar-acumular-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-22-partir-refinar-acumular-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-22-partir-refinar-acumular-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §22.1 — Un intervalo convertido en datos finitos

### Microcontrol 001

[]{#MA-MIC-ANM-01-022-001}

[]{#MA-MSOL-ANM-01-022-001}

[]{#MA-SEC-ANM-01-022-001}

**Pregunta.** ¿Qué datos exige una partición de $[a,b]$?

**Solución.** Una lista finita estrictamente creciente con primer nodo $a$, último $b$ y al menos una pieza, bajo $a<b$.

### Microcontrol 002

[]{#MA-MIC-ANM-01-022-002}

[]{#MA-MSOL-ANM-01-022-002}

**Pregunta.** ¿Son reales los índices?

**Solución.** No: son naturales. Los nodos y las anchuras son reales; cuando se multiplica por un índice se usa su copia real.

### Microcontrol 003

[]{#MA-MIC-ANM-01-022-003}

[]{#MA-MSOL-ANM-01-022-003}

**Pregunta.** ¿Por qué una anchura es positiva?

**Solución.** Porque $x_{i-1}<x_i$, por lo que $x_i-x_{i-1}>0$.

### Microcontrol 004

[]{#MA-MIC-ANM-01-022-004}

[]{#MA-MSOL-ANM-01-022-004}

**Pregunta.** ¿Cuánto suman las anchuras?

**Solución.** $b-a$, por telescopía finita: cada nodo interior aparece una vez positivo y otra negativo.

### Microcontrol 005

[]{#MA-MIC-ANM-01-022-005}

[]{#MA-MSOL-ANM-01-022-005}

**Pregunta.** ¿Son disjuntos los intervalos cerrados vecinos?

**Solución.** No: comparten su nodo. Sus interiores sí son disjuntos.

### Microcontrol 006

[]{#MA-MIC-ANM-01-022-006}

[]{#MA-MSOL-ANM-01-022-006}

**Pregunta.** ¿Cómo se localiza una entrada $t<b$?

**Solución.** Con el menor $j$ que cumple $t<x_j$; entonces $x_{j-1}\le t<x_j$.

### Microcontrol 007

[]{#MA-MIC-ANM-01-022-007}

[]{#MA-MSOL-ANM-01-022-007}

**Pregunta.** ¿Cuáles son las anchuras de $(0,1/4,1)$?

**Solución.** $1/4$ y $3/4$; suman1 y no son iguales.

### Microcontrol 008

[]{#MA-MIC-ANM-01-022-008}

[]{#MA-MSOL-ANM-01-022-008}

**Pregunta.** ¿Admite el contrato inicial $a=b$?

**Solución.** No. Exige $a<b$; una convención degenerada se debe declarar separadamente.

## §22.2 — Refinar conservando los cortes

### Microcontrol 009

[]{#MA-MIC-ANM-01-022-009}

[]{#MA-MSOL-ANM-01-022-009}

[]{#MA-SEC-ANM-01-022-002}

**Pregunta.** ¿Qué significa $P\preceq Q$?

**Solución.** $V(P)\subseteq V(Q)$: $Q$ conserva todos los nodos de $P$.

### Microcontrol 010

[]{#MA-MIC-ANM-01-022-010}

[]{#MA-MSOL-ANM-01-022-010}

**Pregunta.** ¿Es una partición refinamiento de sí misma?

**Solución.** Sí. La inclusión permite igualdad; sólo el refinamiento propio exige un nodo nuevo.

### Microcontrol 011

[]{#MA-MIC-ANM-01-022-011}

[]{#MA-MSOL-ANM-01-022-011}

**Pregunta.** ¿Por qué la relación es transitiva?

**Solución.** La inclusión de nodos es transitiva.

### Microcontrol 012

[]{#MA-MIC-ANM-01-022-012}

[]{#MA-MSOL-ANM-01-022-012}

**Pregunta.** ¿Dónde se inserta un punto nuevo $t$?

**Solución.** Entre $x_{j-1}$ y $x_j$, donde $j$ es el menor índice con $t<x_j$.

### Microcontrol 013

[]{#MA-MIC-ANM-01-022-013}

[]{#MA-MSOL-ANM-01-022-013}

**Pregunta.** ¿Qué sucede si el punto ya era nodo?

**Solución.** No se modifica la partición. Repetirlo violaría crecimiento estricto.

### Microcontrol 014

[]{#MA-MIC-ANM-01-022-014}

[]{#MA-MSOL-ANM-01-022-014}

**Pregunta.** ¿Cuántas piezas añade una inserción propia?

**Solución.** Una: reemplaza una pieza por dos.

### Microcontrol 015

[]{#MA-MIC-ANM-01-022-015}

[]{#MA-MSOL-ANM-01-022-015}

**Pregunta.** ¿Qué nodos tiene el menor refinamiento común?

**Solución.** La unión finita $V(P)\cup V(Q)$, ordenada sin repeticiones.

### Microcontrol 016

[]{#MA-MIC-ANM-01-022-016}

[]{#MA-MSOL-ANM-01-022-016}

**Pregunta.** ¿Reemplazar $1/2$ por $1/3$ es refinar?

**Solución.** No en general: se pierde el nodo antiguo $1/2$.

## §22.3 — La malla mide el peor intervalo

### Microcontrol 017

[]{#MA-MIC-ANM-01-022-017}

[]{#MA-MSOL-ANM-01-022-017}

[]{#MA-SEC-ANM-01-022-003}

**Pregunta.** ¿Qué mide la malla?

**Solución.** La máxima anchura de las piezas, no la anchura media ni su número.

### Microcontrol 018

[]{#MA-MIC-ANM-01-022-018}

[]{#MA-MSOL-ANM-01-022-018}

**Pregunta.** ¿Por qué existe ese máximo?

**Solución.** Es el máximo de una lista finita no vacía de reales, construido por comparaciones sucesivas.

### Microcontrol 019

[]{#MA-MIC-ANM-01-022-019}

[]{#MA-MSOL-ANM-01-022-019}

**Pregunta.** ¿Qué pasa con la malla al refinar?

**Solución.** No aumenta: cada pieza hija está contenida en un padre.

### Microcontrol 020

[]{#MA-MIC-ANM-01-022-020}

[]{#MA-MSOL-ANM-01-022-020}

**Pregunta.** ¿Un refinamiento propio reduce estrictamente la malla?

**Solución.** No. Puede dejar intacta una pieza de anchura máxima.

### Microcontrol 021

[]{#MA-MIC-ANM-01-022-021}

[]{#MA-MSOL-ANM-01-022-021}

**Pregunta.** ¿Cuál es la malla uniforme de $n$ piezas?

**Solución.** $(b-a)/n$, con $n\ge1$ y copia real positiva.

### Microcontrol 022

[]{#MA-MIC-ANM-01-022-022}

[]{#MA-MSOL-ANM-01-022-022}

**Pregunta.** ¿Cómo se logra malla menor que $\delta$?

**Solución.** Arquimedianidad: elegir $n>(b-a)/\delta$ y usar la partición uniforme.

### Microcontrol 023

[]{#MA-MIC-ANM-01-022-023}

[]{#MA-MSOL-ANM-01-022-023}

**Pregunta.** ¿Por qué muchas piezas no bastan?

**Solución.** Se puede conservar una pieza de anchura1/2 y subdividir sólo el resto; la malla sigue siendo1/2.

### Microcontrol 024

[]{#MA-MIC-ANM-01-022-024}

[]{#MA-MSOL-ANM-01-022-024}

**Pregunta.** ¿Cómo se conserva una partición dada y se reduce su malla?

**Solución.** Se toma su refinamiento común con una uniforme suficientemente fina.

## §22.4 — Etiquetas y acumulación firmada

### Microcontrol 025

[]{#MA-MIC-ANM-01-022-025}

[]{#MA-MSOL-ANM-01-022-025}

[]{#MA-SEC-ANM-01-022-004}

**Pregunta.** ¿Qué es una etiqueta?

**Solución.** Un punto dado $\xi_i\in[x_{i-1},x_i]$ para cada índice de pieza.

### Microcontrol 026

[]{#MA-MIC-ANM-01-022-026}

[]{#MA-MSOL-ANM-01-022-026}

**Pregunta.** ¿Pueden repetirse etiquetas?

**Solución.** Sí: un nodo compartido puede etiquetar las dos piezas vecinas.

### Microcontrol 027

[]{#MA-MIC-ANM-01-022-027}

[]{#MA-MSOL-ANM-01-022-027}

**Pregunta.** ¿Cuál es la suma etiquetada?

**Solución.** $S(f;P,\xi)=\sum_i f(\xi_i)\Delta_i$, una suma real finita.

### Microcontrol 028

[]{#MA-MIC-ANM-01-022-028}

[]{#MA-MSOL-ANM-01-022-028}

**Pregunta.** ¿Una suma finita requiere que $f$ sea acotada?

**Solución.** No para existir; sí se necesitan hipótesis adicionales para controlar uniformemente todas las sumas.

### Microcontrol 029

[]{#MA-MIC-ANM-01-022-029}

[]{#MA-MSOL-ANM-01-022-029}

**Pregunta.** ¿Qué suma produce la constante $c$?

**Solución.** $c(b-a)$, cualquiera sea la partición y sus etiquetas.

### Microcontrol 030

[]{#MA-MIC-ANM-01-022-030}

[]{#MA-MSOL-ANM-01-022-030}

**Pregunta.** ¿Qué significa una contribución negativa?

**Solución.** Altura negativa por anchura positiva: acumulación firmada, no área geométrica negativa.

### Microcontrol 031

[]{#MA-MIC-ANM-01-022-031}

[]{#MA-MSOL-ANM-01-022-031}

**Pregunta.** ¿Qué datos se fijan al comparar $S(f)$ y $S(g)$?

**Solución.** La misma partición y las mismas etiquetas; $f\le g$ en el intervalo da el orden de sus sumas.

### Microcontrol 032

[]{#MA-MIC-ANM-01-022-032}

[]{#MA-MSOL-ANM-01-022-032}

**Pregunta.** ¿Qué cota da $|f|\le M$?

**Solución.** $|S|\le M\sum_i\Delta_i=M(b-a)$, sin máximo alcanzado.

## §22.5 — Lo que un cambio de etiquetas puede alterar

### Microcontrol 033

[]{#MA-MIC-ANM-01-022-033}

[]{#MA-MSOL-ANM-01-022-033}

[]{#MA-SEC-ANM-01-022-005}

**Pregunta.** ¿Cómo se controla cambiar sólo etiquetas?

**Solución.** Por $\sum_i |f(\xi_i)-f(\eta_i)|\Delta_i$, usando resta y triangular.

### Microcontrol 034

[]{#MA-MIC-ANM-01-022-034}

[]{#MA-MSOL-ANM-01-022-034}

**Pregunta.** ¿Qué exige una cota local $d_i$?

**Solución.** Que controle todos los pares de entradas de la pieza, no sólo los dos valores muestreados.

### Microcontrol 035

[]{#MA-MIC-ANM-01-022-035}

[]{#MA-MSOL-ANM-01-022-035}

**Pregunta.** ¿Qué cota da Lipschitz para dos etiquetas de una pieza?

**Solución.** $L\Delta_i$, porque ambas distan a lo sumo su anchura.

### Microcontrol 036

[]{#MA-MIC-ANM-01-022-036}

[]{#MA-MSOL-ANM-01-022-036}

**Pregunta.** ¿Por qué $\sum_i\Delta_i^2\le\|P\|(b-a)$?

**Solución.** Cada $\Delta_i\le\|P\|$ y es positiva; multiplicar por $\Delta_i$ y sumar.

### Microcontrol 037

[]{#MA-MIC-ANM-01-022-037}

[]{#MA-MSOL-ANM-01-022-037}

**Pregunta.** ¿Qué controla comparar con un refinamiento?

**Solución.** $L\|P\|(b-a)$, por reescribir cada contribución antigua en las piezas hijas.

### Microcontrol 038

[]{#MA-MIC-ANM-01-022-038}

[]{#MA-MSOL-ANM-01-022-038}

**Pregunta.** ¿Cómo se comparan particiones diferentes?

**Solución.** Por su refinamiento común y triangular; cota $L(b-a)(\|P\|+\|Q\|)$.

### Microcontrol 039

[]{#MA-MIC-ANM-01-022-039}

[]{#MA-MSOL-ANM-01-022-039}

**Pregunta.** ¿Refinar ordena las sumas etiquetadas?

**Solución.** No. Para $x$, una suma1/2 puede dar1/4 o3/4 en el mismo refinamiento, según etiquetas.

### Microcontrol 040

[]{#MA-MIC-ANM-01-022-040}

[]{#MA-MSOL-ANM-01-022-040}

**Pregunta.** ¿Independencia de etiquetas ya prueba existencia de integral?

**Solución.** No por sí sola; todavía se necesita un número que cumpla el contrato universal.

## §22.6 — Escalones: exactitud finita y nodos excepcionales

### Microcontrol 041

[]{#MA-MIC-ANM-01-022-041}

[]{#MA-MSOL-ANM-01-022-041}

[]{#MA-SEC-ANM-01-022-006}

**Pregunta.** ¿Cómo se calcula la acumulación de un escalón?

**Solución.** $A=\sum_j c_j(z_j-z_{j-1})$ con constantes interiores dadas.

### Microcontrol 042

[]{#MA-MIC-ANM-01-022-042}

[]{#MA-MSOL-ANM-01-022-042}

**Pregunta.** ¿Por qué insertar un corte conserva $A$?

**Solución.** Se copia la altura y las dos anchuras suman la original.

### Microcontrol 043

[]{#MA-MIC-ANM-01-022-043}

[]{#MA-MSOL-ANM-01-022-043}

**Pregunta.** ¿Cómo se comparan dos representaciones del mismo escalón?

**Solución.** En el refinamiento común las constantes interiores coinciden; sumar allí da el mismo $A$.

### Microcontrol 044

[]{#MA-MIC-ANM-01-022-044}

[]{#MA-MSOL-ANM-01-022-044}

**Pregunta.** ¿Un valor aislado añade anchura a $A$?

**Solución.** No. Un nodo es un punto sin intervalo de anchura positiva.

### Microcontrol 045

[]{#MA-MIC-ANM-01-022-045}

[]{#MA-MSOL-ANM-01-022-045}

**Pregunta.** ¿Cualquier suma etiquetada coincide exactamente con $A$?

**Solución.** No. Puede usar etiquetas en nodos excepcionales o piezas que cruzan un salto.

### Microcontrol 046

[]{#MA-MIC-ANM-01-022-046}

[]{#MA-MSOL-ANM-01-022-046}

**Pregunta.** ¿Cuántas piezas cerradas contienen un punto fijo?

**Solución.** A lo sumo dos; en extremos a lo sumo una.

### Microcontrol 047

[]{#MA-MIC-ANM-01-022-047}

[]{#MA-MSOL-ANM-01-022-047}

**Pregunta.** ¿Qué cota da modificar $k$ puntos por diferencias de tamaño $D$?

**Solución.** Diferencia de sumas $\le2kD\|P\|$ para la misma partición y etiquetas.

### Microcontrol 048

[]{#MA-MIC-ANM-01-022-048}

[]{#MA-MSOL-ANM-01-022-048}

**Pregunta.** ¿Qué certificado universal obtuvo el escalón?

**Solución.** $|S-A|\le4B(m+1)\|P\|$, contando padres que tocan sus nodos.

## §22.7 — Un límite que todas las etiquetas deben compartir

### Microcontrol 049

[]{#MA-MIC-ANM-01-022-049}

[]{#MA-MSOL-ANM-01-022-049}

[]{#MA-SEC-ANM-01-022-007}

**Pregunta.** ¿En qué orden se eligen los datos del límite?

**Solución.** Primero $I$, después cada tolerancia $\varepsilon$, luego $\delta$, y sólo entonces todas las particiones y etiquetas.

### Microcontrol 050

[]{#MA-MIC-ANM-01-022-050}

[]{#MA-MSOL-ANM-01-022-050}

**Pregunta.** ¿Puede $\delta$ depender de las etiquetas?

**Solución.** No. Debe servir para todas las etiquetas de todas las particiones de malla menor.

### Microcontrol 051

[]{#MA-MIC-ANM-01-022-051}

[]{#MA-MSOL-ANM-01-022-051}

**Pregunta.** ¿Por qué el contrato no es vacío?

**Solución.** Existen particiones uniformes con malla menor que cualquier radio positivo.

### Microcontrol 052

[]{#MA-MIC-ANM-01-022-052}

[]{#MA-MSOL-ANM-01-022-052}

**Pregunta.** ¿Cómo se prueba unicidad?

**Solución.** Si $d=|I-J|>0$, una suma dentro de $d/3$ de ambos daría $d<2d/3$ por triangular.

### Microcontrol 053

[]{#MA-MIC-ANM-01-022-053}

[]{#MA-MSOL-ANM-01-022-053}

**Pregunta.** ¿Qué radio sirve si $|S-I|\le C\|P\|$ y $C>0$?

**Solución.** $\delta=\varepsilon/C$; malla estrictamente menor da error estrictamente menor que $\varepsilon$.

### Microcontrol 054

[]{#MA-MIC-ANM-01-022-054}

[]{#MA-MSOL-ANM-01-022-054}

**Pregunta.** ¿Qué ocurre si $C=0$?

**Solución.** Todas las sumas valen $I$; cualquier radio positivo sirve.

### Microcontrol 055

[]{#MA-MIC-ANM-01-022-055}

[]{#MA-MSOL-ANM-01-022-055}

**Pregunta.** ¿Qué implica integrabilidad para una sucesión dada de mallas que tienden a cero?

**Solución.** Sus sumas etiquetadas tienden a $I$ para cualquier familia dada de etiquetas.

### Microcontrol 056

[]{#MA-MIC-ANM-01-022-056}

[]{#MA-MSOL-ANM-01-022-056}

**Pregunta.** ¿Ya se probó integrabilidad de toda continua?

**Solución.** No. Aquí se probaron escalones y ejemplos con certificados; C23 construirá resultados generales.

## §22.8 — Certificados antes de fórmulas de integración

### Microcontrol 057

[]{#MA-MIC-ANM-01-022-057}

[]{#MA-MSOL-ANM-01-022-057}

[]{#MA-SEC-ANM-01-022-008}

**Pregunta.** ¿Qué suma media da $x$ en $[a,b]$?

**Solución.** $(b^2-a^2)/2$ exactamente, por telescopía de cuadrados.

### Microcontrol 058

[]{#MA-MIC-ANM-01-022-058}

[]{#MA-MSOL-ANM-01-022-058}

**Pregunta.** ¿Qué cota controla otras etiquetas para $x$?

**Solución.** $(b-a)\|P\|/2$, pues la distancia al punto medio es a lo sumo media anchura.

### Microcontrol 059

[]{#MA-MIC-ANM-01-022-059}

[]{#MA-MSOL-ANM-01-022-059}

**Pregunta.** ¿Qué valor tiene $\alpha x+\beta$?

**Solución.** $\alpha(b^2-a^2)/2+\beta(b-a)$, por álgebra finita y el certificado del caso lineal.

### Microcontrol 060

[]{#MA-MIC-ANM-01-022-060}

[]{#MA-MSOL-ANM-01-022-060}

**Pregunta.** ¿Qué identidad local controla $x^2$?

**Solución.** $(v^3-u^3)/3=(v-u)(u^2+uv+v^2)/3$.

### Microcontrol 061

[]{#MA-MIC-ANM-01-022-061}

[]{#MA-MSOL-ANM-01-022-061}

**Pregunta.** ¿Qué cota universal certifica $1/3$?

**Solución.** $|S(x^2)-1/3|\le2\|P\|$ en $[0,1]$.

### Microcontrol 062

[]{#MA-MIC-ANM-01-022-062}

[]{#MA-MSOL-ANM-01-022-062}

**Pregunta.** ¿Cuáles son las sumas izquierda y derecha para $n=4$?

**Solución.** $7/32$ y $15/32$, respectivamente.

### Microcontrol 063

[]{#MA-MIC-ANM-01-022-063}

[]{#MA-MSOL-ANM-01-022-063}

**Pregunta.** ¿La etiqueta media es exacta para $x^2$?

**Solución.** No. La suma uniforme es $1/3-1/(12n^2)$.

### Microcontrol 064

[]{#MA-MIC-ANM-01-022-064}

[]{#MA-MSOL-ANM-01-022-064}

**Pregunta.** ¿Qué se requiere para error menor que $1/100$ mediante $2\|P\|$?

**Solución.** Malla menor que1/200; en uniforme, un natural $n>200$.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 22](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html) · [Ejercicios](analisis-para-matematicos-capitulo-22-partir-refinar-acumular-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-22-partir-refinar-acumular-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-22-partir-refinar-acumular-microcontroles.html)
