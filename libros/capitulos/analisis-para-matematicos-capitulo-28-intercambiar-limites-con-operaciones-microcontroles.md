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
date-modified: '2026-10-11'
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

**Solución.** Una fila posterior al corte de error uniforme.

### Microcontrol 002

[]{#MA-MIC-ANM-01-028-002}

[]{#MA-MSOL-ANM-01-028-002}

**Pregunta.** ¿Cuántos errores controla la prueba de R1?

**Solución.** Tres: aproximación en ambas entradas y variación de la fila fija.

### Microcontrol 003

[]{#MA-MIC-ANM-01-028-003}

[]{#MA-MSOL-ANM-01-028-003}

**Pregunta.** ¿La fila fijada necesita una cota global de valores?

**Solución.** No; la prueba sólo usa error uniforme y continuidad.

### Microcontrol 004

[]{#MA-MIC-ANM-01-028-004}

[]{#MA-MSOL-ANM-01-028-004}

**Pregunta.** ¿Los radios de continuidad deben ser comunes a todas las filas?

**Solución.** No; basta el radio de la fila escogida para la tolerancia dada.

### Microcontrol 005

[]{#MA-MIC-ANM-01-028-005}

[]{#MA-MSOL-ANM-01-028-005}

**Pregunta.** ¿Qué hipótesis de filas conserva continuidad uniforme?

**Solución.** Continuidad uniforme de las filas, además de convergencia uniforme.

### Microcontrol 006

[]{#MA-MIC-ANM-01-028-006}

[]{#MA-MSOL-ANM-01-028-006}

**Pregunta.** ¿Un destino continuo obliga convergencia uniforme?

**Solución.** No; las potencias en $[0,1)$ tienen destino cero y envolvente uno.

### Microcontrol 007

[]{#MA-MIC-ANM-01-028-007}

[]{#MA-MSOL-ANM-01-028-007}

**Pregunta.** ¿Qué continuidad se usa en bordes del dominio?

**Solución.** Continuidad relativa al mismo dominio común.

### Microcontrol 008

[]{#MA-MIC-ANM-01-028-008}

[]{#MA-MSOL-ANM-01-028-008}

**Pregunta.** ¿Qué ocurre en un dominio vacío?

**Solución.** La conclusión no tiene puntos que comprobar.

## §28.2 — Dos límites con un presupuesto común

### Microcontrol 009

[]{#MA-MIC-ANM-01-028-009}

[]{#MA-MSOL-ANM-01-028-009}

[]{#MA-SEC-ANM-01-028-002}

**Pregunta.** ¿Por qué el centro de R2 debe acumular?

**Solución.** Para que las ventanas perforadas tengan entradas y los límites sean únicos.

### Microcontrol 010

[]{#MA-MIC-ANM-01-028-010}

[]{#MA-MSOL-ANM-01-028-010}

**Pregunta.** ¿Qué se construye primero en R2?

**Solución.** El límite numérico de los destinos de las filas.

### Microcontrol 011

[]{#MA-MIC-ANM-01-028-011}

[]{#MA-MSOL-ANM-01-028-011}

**Pregunta.** ¿Qué cota queda al pasar una entrada al límite?

**Solución.** Una cota débil, por ejemplo $|p_n-p_m|\le\eta/2$.

### Microcontrol 012

[]{#MA-MIC-ANM-01-028-012}

[]{#MA-MSOL-ANM-01-028-012}

**Pregunta.** ¿Qué construye el destino de una sucesión de Cauchy real?

**Solución.** La completitud numérica de C10.

### Microcontrol 013

[]{#MA-MIC-ANM-01-028-013}

[]{#MA-MSOL-ANM-01-028-013}

**Pregunta.** ¿El valor de la función en el centro participa?

**Solución.** No en el límite relativo perforado.

### Microcontrol 014

[]{#MA-MIC-ANM-01-028-014}

[]{#MA-MSOL-ANM-01-028-014}

**Pregunta.** ¿Basta uniformidad en una ventana fija?

**Solución.** Sí, tras restringir el dominio a esa ventana perforada.

### Microcontrol 015

[]{#MA-MIC-ANM-01-028-015}

[]{#MA-MSOL-ANM-01-028-015}

**Pregunta.** ¿Qué valor conserva la ruta racional $x_n=1/(n+1)$?

**Solución.** $1/2$ en toda etapa, frente a iterados uno y cero.

### Microcontrol 016

[]{#MA-MIC-ANM-01-028-016}

[]{#MA-MSOL-ANM-01-028-016}

**Pregunta.** ¿Se escoge una ruta por cada escala en la prueba?

**Solución.** No; la prueba es por ventanas y las rutas usadas son dadas explícitamente.

## §28.3 — Compacidad y monotonía: el mecanismo de Dini

### Microcontrol 017

[]{#MA-MIC-ANM-01-028-017}

[]{#MA-MSOL-ANM-01-028-017}

[]{#MA-SEC-ANM-01-028-003}

**Pregunta.** ¿Qué error es no negativo en Dini decreciente?

**Solución.** $e_n=f_n-f$, por orden de cada columna al límite.

### Microcontrol 018

[]{#MA-MIC-ANM-01-028-018}

[]{#MA-MSOL-ANM-01-028-018}

**Pregunta.** ¿Qué hace abiertos los conjuntos de error pequeño?

**Solución.** Continuidad de las filas y del destino.

### Microcontrol 019

[]{#MA-MIC-ANM-01-028-019}

[]{#MA-MSOL-ANM-01-028-019}

**Pregunta.** ¿Qué permite obtener una subcubierta finita?

**Solución.** Compacidad del dominio.

### Microcontrol 020

[]{#MA-MIC-ANM-01-028-020}

[]{#MA-MSOL-ANM-01-028-020}

**Pregunta.** ¿Qué convierte los índices finitos en una cola común?

**Solución.** Monotonía de los errores y el máximo finito de índices.

### Microcontrol 021

[]{#MA-MIC-ANM-01-028-021}

[]{#MA-MSOL-ANM-01-028-021}

**Pregunta.** ¿Dini entrega una tasa numérica general?

**Solución.** No; garantiza un corte para cada tolerancia.

### Microcontrol 022

[]{#MA-MIC-ANM-01-028-022}

[]{#MA-MSOL-ANM-01-028-022}

**Pregunta.** ¿Qué falta en las potencias sobre $(0,1)$?

**Solución.** Compacidad, aunque el destino cero sea continuo.

### Microcontrol 023

[]{#MA-MIC-ANM-01-028-023}

[]{#MA-MSOL-ANM-01-028-023}

**Pregunta.** ¿Qué falta en las indicadoras decrecientes del intervalo pequeño?

**Solución.** Continuidad de las filas.

### Microcontrol 024

[]{#MA-MIC-ANM-01-028-024}

[]{#MA-MSOL-ANM-01-028-024}

**Pregunta.** ¿Qué falta en las tiendas continuas de altura uno?

**Solución.** Monotonía por columnas.

## §28.4 — La integral soporta un error global pequeño

### Microcontrol 025

[]{#MA-MIC-ANM-01-028-025}

[]{#MA-MSOL-ANM-01-028-025}

[]{#MA-SEC-ANM-01-028-004}

**Pregunta.** ¿Qué debe probarse antes de escribir la integral del destino?

**Solución.** Acotación e integrabilidad del destino.

### Microcontrol 026

[]{#MA-MIC-ANM-01-028-026}

[]{#MA-MSOL-ANM-01-028-026}

**Pregunta.** ¿Cómo cambia la brecha Darboux con error global $\delta$?

**Solución.** Aumenta a lo sumo $2\delta(b-a)$.

### Microcontrol 027

[]{#MA-MIC-ANM-01-028-027}

[]{#MA-MSOL-ANM-01-028-027}

**Pregunta.** ¿Por qué aparecen dos contribuciones de error en la brecha?

**Solución.** Una en la suma superior y otra en la inferior.

### Microcontrol 028

[]{#MA-MIC-ANM-01-028-028}

[]{#MA-MSOL-ANM-01-028-028}

**Pregunta.** ¿Qué error controla el valor integral?

**Solución.** La longitud del segmento multiplicada por la envolvente de error.

### Microcontrol 029

[]{#MA-MIC-ANM-01-028-029}

[]{#MA-MSOL-ANM-01-028-029}

**Pregunta.** ¿Debe alcanzarse la envolvente para integrar su cota?

**Solución.** No; basta que sea una cota real para todos los valores.

### Microcontrol 030

[]{#MA-MIC-ANM-01-028-030}

[]{#MA-MSOL-ANM-01-028-030}

**Pregunta.** ¿Cómo se trata un segmento de longitud cero?

**Solución.** La integral es cero por convención, sin dividir por la longitud.

### Microcontrol 031

[]{#MA-MIC-ANM-01-028-031}

[]{#MA-MSOL-ANM-01-028-031}

**Pregunta.** ¿Qué conserva la integral de las tiendas normalizadas?

**Solución.** Uno en cada etapa, frente a integral cero del destino.

### Microcontrol 032

[]{#MA-MIC-ANM-01-028-032}

[]{#MA-MSOL-ANM-01-028-032}

**Pregunta.** ¿Qué falla para el destino Dirichlet?

**Solución.** La integral del destino no existe en Riemann.

## §28.5 — Acumulaciones, pesos y extremos variables

### Microcontrol 033

[]{#MA-MIC-ANM-01-028-033}

[]{#MA-MSOL-ANM-01-028-033}

[]{#MA-SEC-ANM-01-028-005}

**Pregunta.** ¿Qué corte controla todas las acumulaciones?

**Solución.** El corte uniforme de integrandas y una longitud común finita.

### Microcontrol 034

[]{#MA-MIC-ANM-01-028-034}

[]{#MA-MSOL-ANM-01-028-034}

**Pregunta.** ¿Qué se hace si el destino de acumulación precede al anclaje?

**Solución.** Se orienta la integral invirtiendo sus límites.

### Microcontrol 035

[]{#MA-MIC-ANM-01-028-035}

[]{#MA-MSOL-ANM-01-028-035}

**Pregunta.** ¿Qué hipótesis permite identificar la derivada de toda acumulación?

**Solución.** Continuidad de la integranda en el centro pertinente.

### Microcontrol 036

[]{#MA-MIC-ANM-01-028-036}

[]{#MA-MSOL-ANM-01-028-036}

**Pregunta.** ¿Qué debe acreditarse para un peso integrable fijo?

**Solución.** Integrabilidad de productos y una barrera o integral del absoluto del peso.

### Microcontrol 037

[]{#MA-MIC-ANM-01-028-037}

[]{#MA-MSOL-ANM-01-028-037}

**Pregunta.** ¿Cuántos errores hay al mover ambos extremos?

**Solución.** Tres: integranda, extremo inicial y extremo final.

### Microcontrol 038

[]{#MA-MIC-ANM-01-028-038}

[]{#MA-MSOL-ANM-01-028-038}

**Pregunta.** ¿Dónde deben permanecer los extremos móviles?

**Solución.** En un mismo segmento cerrado de longitud finita.

### Microcontrol 039

[]{#MA-MIC-ANM-01-028-039}

[]{#MA-MSOL-ANM-01-028-039}

**Pregunta.** ¿Cuánto integra $1/(n+1)$ sobre $[0,n+1]$?

**Solución.** Uno; la longitud compensa el error pequeño.

### Microcontrol 040

[]{#MA-MIC-ANM-01-028-040}

[]{#MA-MSOL-ANM-01-028-040}

**Pregunta.** ¿Uniformidad es necesaria para igualdad de límites integrales?

**Solución.** No; las tiendas sin normalizar integran $1/(n+3)\to0$.

## §28.6 — Derivadas uniformes y un valor de anclaje

### Microcontrol 041

[]{#MA-MIC-ANM-01-028-041}

[]{#MA-MSOL-ANM-01-028-041}

[]{#MA-SEC-ANM-01-028-006}

**Pregunta.** ¿Qué dato fija la constante aditiva en R6?

**Solución.** Convergencia de valores en un anclaje.

### Microcontrol 042

[]{#MA-MIC-ANM-01-028-042}

[]{#MA-MSOL-ANM-01-028-042}

**Pregunta.** ¿En qué dominio se controlan uniformemente las derivadas?

**Solución.** En el interior del mismo segmento.

### Microcontrol 043

[]{#MA-MIC-ANM-01-028-043}

[]{#MA-MSOL-ANM-01-028-043}

**Pregunta.** ¿Qué herramienta convierte derivadas en cotas de incrementos?

**Solución.** Valor medio y su consecuencia de C19.

### Microcontrol 044

[]{#MA-MIC-ANM-01-028-044}

[]{#MA-MSOL-ANM-01-028-044}

**Pregunta.** ¿Qué se fija antes de pasar una etapa al límite en incrementos?

**Solución.** La fila comparada y las dos entradas.

### Microcontrol 045

[]{#MA-MIC-ANM-01-028-045}

[]{#MA-MSOL-ANM-01-028-045}

**Pregunta.** ¿Se supone derivabilidad del destino para obtener esa cota?

**Solución.** No; se deduce después mediante cocientes.

### Microcontrol 046

[]{#MA-MIC-ANM-01-028-046}

[]{#MA-MSOL-ANM-01-028-046}

**Pregunta.** ¿Cómo se divide la cota de incrementos?

**Solución.** Por la distancia positiva entre entradas distintas.

### Microcontrol 047

[]{#MA-MIC-ANM-01-028-047}

[]{#MA-MSOL-ANM-01-028-047}

**Pregunta.** ¿R6 necesita derivadas continuas?

**Solución.** No, sólo derivabilidad de filas y convergencia uniforme de sus derivadas.

### Microcontrol 048

[]{#MA-MIC-ANM-01-028-048}

[]{#MA-MSOL-ANM-01-028-048}

**Pregunta.** ¿Qué factor limita la uniformidad de valores en dominios no acotados?

**Solución.** La distancia al anclaje, que puede carecer de barrera global.

## §28.7 — Lo que la convergencia de valores no controla

### Microcontrol 049

[]{#MA-MIC-ANM-01-028-049}

[]{#MA-MSOL-ANM-01-028-049}

[]{#MA-SEC-ANM-01-028-007}

**Pregunta.** ¿Qué envolvente tienen las raíces suavizadas frente a $|x|$?

**Solución.** $1/(n+1)$, alcanzada en cero.

### Microcontrol 050

[]{#MA-MIC-ANM-01-028-050}

[]{#MA-MSOL-ANM-01-028-050}

**Pregunta.** ¿Por qué $|x|$ no deriva en cero?

**Solución.** Sus cocientes laterales son menos uno y uno.

### Microcontrol 051

[]{#MA-MIC-ANM-01-028-051}

[]{#MA-MSOL-ANM-01-028-051}

**Pregunta.** ¿Qué valor tienen $h_n^{\prime}$ en cero?

**Solución.** Uno en todas las etapas.

### Microcontrol 052

[]{#MA-MIC-ANM-01-028-052}

[]{#MA-MSOL-ANM-01-028-052}

**Pregunta.** ¿Qué derivada tiene el destino cero de $h_n$?

**Solución.** Cero en todos los centros.

### Microcontrol 053

[]{#MA-MIC-ANM-01-028-053}

[]{#MA-MSOL-ANM-01-028-053}

**Pregunta.** ¿Qué no detecta la operación de derivar?

**Solución.** Las constantes aditivas de cada componente.

### Microcontrol 054

[]{#MA-MIC-ANM-01-028-054}

[]{#MA-MSOL-ANM-01-028-054}

**Pregunta.** ¿Una ancla controla otra componente separada?

**Solución.** No; falta un segmento del dominio que las una.

### Microcontrol 055

[]{#MA-MIC-ANM-01-028-055}

[]{#MA-MSOL-ANM-01-028-055}

**Pregunta.** ¿Dónde convergen uniformemente los valores $x/(n+1)$?

**Solución.** En cada segmento acotado, aunque no en toda la recta.

### Microcontrol 056

[]{#MA-MIC-ANM-01-028-056}

[]{#MA-MSOL-ANM-01-028-056}

**Pregunta.** ¿La sola norma de valores controla la derivada?

**Solución.** No; $h_n$ tiende uniformemente a cero y sus derivadas no.

## §28.8 — Certificar varias operaciones a la vez

### Microcontrol 057

[]{#MA-MIC-ANM-01-028-057}

[]{#MA-MSOL-ANM-01-028-057}

[]{#MA-SEC-ANM-01-028-008}

**Pregunta.** ¿Qué envolvente tiene la capa de derivadas del paquete polinómico?

**Solución.** $2^{-n}$.

### Microcontrol 058

[]{#MA-MIC-ANM-01-028-058}

[]{#MA-MSOL-ANM-01-028-058}

**Pregunta.** ¿Qué anclaje del paquete es exacto?

**Solución.** El valor cero en $x=0$.

### Microcontrol 059

[]{#MA-MIC-ANM-01-028-059}

[]{#MA-MSOL-ANM-01-028-059}

**Pregunta.** ¿Qué envolvente tiene su error de acumulación?

**Solución.** $2^{-n}/2$ en $[-1,1]$.

### Microcontrol 060

[]{#MA-MIC-ANM-01-028-060}

[]{#MA-MSOL-ANM-01-028-060}

**Pregunta.** ¿El error integral firmado en el segmento simétrico es igual a esa envolvente?

**Solución.** No; es cero por imparidad del error de integrandas.

### Microcontrol 061

[]{#MA-MIC-ANM-01-028-061}

[]{#MA-MSOL-ANM-01-028-061}

**Pregunta.** ¿Sirve $n=3$ para error estrictamente menor que $1/8$?

**Solución.** No; está en la frontera. El corte mínimo es cuatro.

### Microcontrol 062

[]{#MA-MIC-ANM-01-028-062}

[]{#MA-MSOL-ANM-01-028-062}

**Pregunta.** ¿Qué dos capas suma la norma $C^1$?

**Solución.** Norma suprema de valores y de derivadas extendidas al cerrado.

### Microcontrol 063

[]{#MA-MIC-ANM-01-028-063}

[]{#MA-MSOL-ANM-01-028-063}

**Pregunta.** ¿Qué anclas se necesitan para controlar órdenes hasta $r$?

**Solución.** Valores de órdenes cero hasta $r-1$ en un anclaje común.

### Microcontrol 064

[]{#MA-MIC-ANM-01-028-064}

[]{#MA-MSOL-ANM-01-028-064}

**Pregunta.** ¿Cuál es la única puerta siguiente?

**Solución.** C29: series de funciones y series de potencias, aún sin abrir.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 28](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html) · [Ejercicios](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones-microcontroles.html)
