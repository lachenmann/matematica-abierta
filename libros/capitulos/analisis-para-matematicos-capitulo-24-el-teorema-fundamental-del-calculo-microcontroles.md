---
content-id: MA-BCH-0301
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-024-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 24
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C24_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 24](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html) · [Ejercicios](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §24.1 — Construir una función de acumulación

### Microcontrol 001

[]{#MA-MIC-ANM-01-024-001}

[]{#MA-MSOL-ANM-01-024-001}

[]{#MA-SEC-ANM-01-024-001}

**Pregunta.** ¿Qué debe existir antes de definir $A_f(x)$?

**Solución.** La integral de cada restricción $f|_{[a,x]}$, garantizada por integrabilidad y restricción de C23.

### Microcontrol 002

[]{#MA-MIC-ANM-01-024-002}

[]{#MA-MSOL-ANM-01-024-002}

**Pregunta.** ¿Cuánto vale $A_f(a)$?

**Solución.** Cero por la convención degenerada; no se usa una partición estricta del singleton.

### Microcontrol 003

[]{#MA-MIC-ANM-01-024-003}

[]{#MA-MSOL-ANM-01-024-003}

**Pregunta.** ¿Por qué la fórmula determina una función?

**Solución.** Cada entrada tiene una integral existente y única; su grafo se separa en $[a,b]\times\mathbb R$.

### Microcontrol 004

[]{#MA-MIC-ANM-01-024-004}

[]{#MA-MSOL-ANM-01-024-004}

**Pregunta.** ¿Qué expresa $A_f(y)-A_f(x)$?

**Solución.** La integral orientada sobre el tramo de $x$ a $y$, por aditividad.

### Microcontrol 005

[]{#MA-MIC-ANM-01-024-005}

[]{#MA-MSOL-ANM-01-024-005}

**Pregunta.** ¿Qué ocurre si $x=y$?

**Solución.** Ambos miembros del incremento son cero; no se divide por esa anchura.

### Microcontrol 006

[]{#MA-MIC-ANM-01-024-006}

[]{#MA-MSOL-ANM-01-024-006}

**Pregunta.** ¿Qué cambia al mover el origen a $c$?

**Solución.** Se resta la constante $A_f(c)$; todos los incrementos se conservan.

### Microcontrol 007

[]{#MA-MIC-ANM-01-024-007}

[]{#MA-MSOL-ANM-01-024-007}

**Pregunta.** ¿Debe ser no negativa la acumulación?

**Solución.** No. La integral es firmada; para $2t-1$, $A_f(x)=x^2-x$ es negativa dentro de $[0,1]$.

### Microcontrol 008

[]{#MA-MIC-ANM-01-024-008}

[]{#MA-MSOL-ANM-01-024-008}

**Pregunta.** ¿Se ha usado una primitiva en R1?

**Solución.** No. La fórmula afín proviene del cálculo por sumas de C22 y la construcción de C23.

## §24.2 — Incrementos, cotas y continuidad

### Microcontrol 009

[]{#MA-MIC-ANM-01-024-009}

[]{#MA-MSOL-ANM-01-024-009}

[]{#MA-SEC-ANM-01-024-002}

**Pregunta.** ¿Qué encierra el cociente medio?

**Solución.** Cotas de todos los valores de la integranda en el segmento entre las entradas.

### Microcontrol 010

[]{#MA-MIC-ANM-01-024-010}

[]{#MA-MSOL-ANM-01-024-010}

**Pregunta.** ¿Deben alcanzarse las cotas extremas locales?

**Solución.** No. Ínfimo y supremo existen por imagen no vacía acotada.

### Microcontrol 011

[]{#MA-MIC-ANM-01-024-011}

[]{#MA-MSOL-ANM-01-024-011}

**Pregunta.** ¿Qué da una cota $|f|\le B$?

**Solución.** $|A_f(y)-A_f(x)|\le B|y-x|$ para todos los pares.

### Microcontrol 012

[]{#MA-MIC-ANM-01-024-012}

[]{#MA-MSOL-ANM-01-024-012}

**Pregunta.** ¿Qué radio evita dividir por $B=0$?

**Solución.** $\delta=\varepsilon/(B+1)>0$; si $B=0$, el incremento es exactamente cero.

### Microcontrol 013

[]{#MA-MIC-ANM-01-024-013}

[]{#MA-MSOL-ANM-01-024-013}

**Pregunta.** ¿Se necesita continuidad de $f$ para continuidad de $A_f$?

**Solución.** No. Integrabilidad y acotación bastan para Lipschitz.

### Microcontrol 014

[]{#MA-MIC-ANM-01-024-014}

[]{#MA-MSOL-ANM-01-024-014}

**Pregunta.** ¿Qué signo garantiza acumulación no decreciente?

**Solución.** $f\ge0$ en todo el intervalo, por orden de integrales.

### Microcontrol 015

[]{#MA-MIC-ANM-01-024-015}

[]{#MA-MSOL-ANM-01-024-015}

**Pregunta.** ¿Un pico positivo garantiza crecimiento estricto?

**Solución.** No. Un valor aislado puede tener todas las integrales cero.

### Microcontrol 016

[]{#MA-MIC-ANM-01-024-016}

[]{#MA-MSOL-ANM-01-024-016}

**Pregunta.** ¿Cuál es la acumulada del escalón con corte $1/2$?

**Solución.** Cero para $x\le1/2$ y $x-1/2$ para $x\ge1/2$.

## §24.3 — La tasa reaparece en un punto

### Microcontrol 017

[]{#MA-MIC-ANM-01-024-017}

[]{#MA-MSOL-ANM-01-024-017}

[]{#MA-SEC-ANM-01-024-003}

**Pregunta.** ¿Qué controla el lema del promedio local?

**Solución.** Si $|f(t)-f(x)|\le\eta$ en todo el tramo, el error del cociente respecto de $f(x)$ es a lo sumo $\eta$.

### Microcontrol 018

[]{#MA-MIC-ANM-01-024-018}

[]{#MA-MSOL-ANM-01-024-018}

**Pregunta.** ¿Cómo se trata un incremento negativo?

**Solución.** Se usa el tramo ordenado inverso y se cambian ambos signos del cociente.

### Microcontrol 019

[]{#MA-MIC-ANM-01-024-019}

[]{#MA-MSOL-ANM-01-024-019}

**Pregunta.** ¿Qué continuidad usa R3?

**Solución.** Sólo continuidad de la integranda en el centro interior donde se deriva.

### Microcontrol 020

[]{#MA-MIC-ANM-01-024-020}

[]{#MA-MSOL-ANM-01-024-020}

**Pregunta.** ¿Por qué aplicar continuidad a $\varepsilon/2$?

**Solución.** Al pasar a una cota no estricta del integral se conserva error $\le\varepsilon/2<\varepsilon$.

### Microcontrol 021

[]{#MA-MIC-ANM-01-024-021}

[]{#MA-MSOL-ANM-01-024-021}

**Pregunta.** ¿Quién precede a toda entrada cercana?

**Solución.** El radio $\delta$, elegido después de la tolerancia y antes de cualquier $y$.

### Microcontrol 022

[]{#MA-MIC-ANM-01-024-022}

[]{#MA-MSOL-ANM-01-024-022}

**Pregunta.** ¿Se escoge un punto de valor medio integral?

**Solución.** No. El encierro controla todos los valores de cada segmento corto.

### Microcontrol 023

[]{#MA-MIC-ANM-01-024-023}

[]{#MA-MSOL-ANM-01-024-023}

**Pregunta.** ¿Qué cota fina da Lipschitz $L$ para el residuo?

**Solución.** A lo sumo $L|y-x|^2/2$, al integrar la cota afín del error de la tasa.

### Microcontrol 024

[]{#MA-MIC-ANM-01-024-024}

[]{#MA-MSOL-ANM-01-024-024}

**Pregunta.** ¿Cuál es la derivada de la acumulada de $t^2$ en $1/2$?

**Solución.** $1/4$, porque la integranda es continua allí.

## §24.4 — Bordes, saltos y valores aislados

### Microcontrol 025

[]{#MA-MIC-ANM-01-024-025}

[]{#MA-MSOL-ANM-01-024-025}

[]{#MA-SEC-ANM-01-024-004}

**Pregunta.** ¿Qué derivada se afirma en $a$?

**Solución.** La relativa desde la derecha, de valor $f(a)$ si hay continuidad relativa.

### Microcontrol 026

[]{#MA-MIC-ANM-01-024-026}

[]{#MA-MSOL-ANM-01-024-026}

**Pregunta.** ¿Y en $b$?

**Solución.** La relativa desde la izquierda, de valor $f(b)$ bajo la misma hipótesis local.

### Microcontrol 027

[]{#MA-MIC-ANM-01-024-027}

[]{#MA-MSOL-ANM-01-024-027}

**Pregunta.** ¿Se afirma una derivada bilateral de una prolongación?

**Solución.** No. No se han dado valores fuera de $[a,b]$.

### Microcontrol 028

[]{#MA-MIC-ANM-01-024-028}

[]{#MA-MSOL-ANM-01-024-028}

**Pregunta.** ¿Qué ocurre con la acumulada de un salto?

**Solución.** Es continua, pero puede tener una esquina sin derivada en el corte.

### Microcontrol 029

[]{#MA-MIC-ANM-01-024-029}

[]{#MA-MSOL-ANM-01-024-029}

**Pregunta.** ¿Qué cocientes tiene el escalón en su corte?

**Solución.** Cero a la izquierda y uno a la derecha.

### Microcontrol 030

[]{#MA-MIC-ANM-01-024-030}

[]{#MA-MSOL-ANM-01-024-030}

**Pregunta.** ¿Qué acumulada tiene el pico aislado?

**Solución.** La función cero, por invariancia de todas las integrales ante cambios finitos.

### Microcontrol 031

[]{#MA-MIC-ANM-01-024-031}

[]{#MA-MSOL-ANM-01-024-031}

**Pregunta.** ¿En el pico existe la derivada de la acumulada?

**Solución.** Sí, vale cero; no recupera el valor excepcional uno de la integranda.

### Microcontrol 032

[]{#MA-MIC-ANM-01-024-032}

[]{#MA-MSOL-ANM-01-024-032}

**Pregunta.** ¿Continuidad local se probó necesaria para que exista la derivada?

**Solución.** No. Se probó suficiente para recuperar el valor; el pico diferencia ambas afirmaciones.

## §24.5 — De una primitiva a la integral

### Microcontrol 033

[]{#MA-MIC-ANM-01-024-033}

[]{#MA-MSOL-ANM-01-024-033}

[]{#MA-SEC-ANM-01-024-005}

**Pregunta.** ¿Qué exige una primitiva sobre el cerrado?

**Solución.** Continuidad en todo $[a,b]$, derivabilidad interior e igualdad $H'=f$ allí.

### Microcontrol 034

[]{#MA-MIC-ANM-01-024-034}

[]{#MA-MSOL-ANM-01-024-034}

**Pregunta.** ¿La definición de primitiva incluye integrabilidad de $f$?

**Solución.** No. Es una hipótesis separada para Newton–Leibniz.

### Microcontrol 035

[]{#MA-MIC-ANM-01-024-035}

[]{#MA-MSOL-ANM-01-024-035}

**Pregunta.** ¿Qué herramienta controla el incremento en cada pieza?

**Solución.** Lagrange de C19, con continuidad en la pieza cerrada y derivabilidad dentro.

### Microcontrol 036

[]{#MA-MIC-ANM-01-024-036}

[]{#MA-MSOL-ANM-01-024-036}

**Pregunta.** ¿Qué se suma tras eliminar el testigo de Lagrange?

**Solución.** Las desigualdades $m_i\Delta_i\le H(x_i)-H(x_{i-1})\le M_i\Delta_i$.

### Microcontrol 037

[]{#MA-MIC-ANM-01-024-037}

[]{#MA-MSOL-ANM-01-024-037}

**Pregunta.** ¿Por qué telescopa la suma central?

**Solución.** Los valores en nodos interiores aparecen una vez con cada signo y se cancelan finitamente.

### Microcontrol 038

[]{#MA-MIC-ANM-01-024-038}

[]{#MA-MSOL-ANM-01-024-038}

**Pregunta.** ¿Qué convierte el encierro en igualdad con la integral?

**Solución.** El criterio de Darboux: brechas arbitrariamente pequeñas encierran ambos números.

### Microcontrol 039

[]{#MA-MIC-ANM-01-024-039}

[]{#MA-MSOL-ANM-01-024-039}

**Pregunta.** ¿Se usa continuidad de $f$ en la segunda parte?

**Solución.** No. Basta integrabilidad y una primitiva con las condiciones declaradas.

### Microcontrol 040

[]{#MA-MIC-ANM-01-024-040}

[]{#MA-MSOL-ANM-01-024-040}

**Pregunta.** ¿Por qué conservar continuidad de $H$ en los bordes?

**Solución.** Sin ella falla Lagrange en las piezas de borde y puede fallar la evaluación.

## §24.6 — Normalización, cálculo y signo

### Microcontrol 041

[]{#MA-MIC-ANM-01-024-041}

[]{#MA-MSOL-ANM-01-024-041}

[]{#MA-SEC-ANM-01-024-006}

**Pregunta.** ¿En qué difieren dos primitivas sobre el mismo intervalo?

**Solución.** En una constante, por derivada cero de la diferencia y C19.

### Microcontrol 042

[]{#MA-MIC-ANM-01-024-042}

[]{#MA-MSOL-ANM-01-024-042}

**Pregunta.** ¿Cómo se fija esa constante?

**Solución.** Evaluando la diferencia en una entrada, por ejemplo en $a$.

### Microcontrol 043

[]{#MA-MIC-ANM-01-024-043}

[]{#MA-MSOL-ANM-01-024-043}

**Pregunta.** ¿Qué primitiva de una continua está normalizada?

**Solución.** $A_f$, única entre las primitivas con valor cero en $a$.

### Microcontrol 044

[]{#MA-MIC-ANM-01-024-044}

[]{#MA-MSOL-ANM-01-024-044}

**Pregunta.** ¿Qué solución corresponde al dato inicial $H(a)=c_0$?

**Solución.** $H(x)=c_0+A_f(x)$, para tasa continua dada.

### Microcontrol 045

[]{#MA-MIC-ANM-01-024-045}

[]{#MA-MSOL-ANM-01-024-045}

**Pregunta.** ¿Qué primitiva tiene $t^n$ para entero $n\ge0$?

**Solución.** $t^{n+1}/(n+1)$, usando la regla de potencias enteras de C18.

### Microcontrol 046

[]{#MA-MIC-ANM-01-024-046}

[]{#MA-MSOL-ANM-01-024-046}

**Pregunta.** ¿Una integral firmada cero obliga a función cero?

**Solución.** No. $2t-1$ tiene integral cero en $[0,1]$ y no es la función cero.

### Microcontrol 047

[]{#MA-MIC-ANM-01-024-047}

[]{#MA-MSOL-ANM-01-024-047}

**Pregunta.** ¿Cuánto integra $|2t-1|$ en $[0,1]$?

**Solución.** $1/2$, suma de dos contribuciones $1/4$.

### Microcontrol 048

[]{#MA-MIC-ANM-01-024-048}

[]{#MA-MSOL-ANM-01-024-048}

**Pregunta.** ¿Todo punto estacionario de la acumulada es extremo?

**Solución.** No. Para tasa $3t^2$, la acumulada $t^3+1$ crece atravesando el centro cero.

## §24.7 — Partes y cambio de variable

### Microcontrol 049

[]{#MA-MIC-ANM-01-024-049}

[]{#MA-MSOL-ANM-01-024-049}

[]{#MA-SEC-ANM-01-024-007}

**Pregunta.** ¿Qué regla diferencial produce integración por partes?

**Solución.** La regla del producto, seguida de Newton–Leibniz y linealidad.

### Microcontrol 050

[]{#MA-MIC-ANM-01-024-050}

[]{#MA-MSOL-ANM-01-024-050}

**Pregunta.** ¿Qué condición extra se pide a las derivadas en esa fórmula?

**Solución.** Extensiones integrables al cerrado; existencia puntual sola no certifica los integrales.

### Microcontrol 051

[]{#MA-MIC-ANM-01-024-051}

[]{#MA-MSOL-ANM-01-024-051}

**Pregunta.** ¿Importan los valores de esas extensiones en los bordes?

**Solución.** Cambios finitos no modifican las integrales; las igualdades de derivadas se exigen dentro.

### Microcontrol 052

[]{#MA-MIC-ANM-01-024-052}

[]{#MA-MSOL-ANM-01-024-052}

**Pregunta.** ¿Qué primitiva prueba el cambio de variable?

**Solución.** $A_f\circ g$, cuya derivada es $f(g(t))g'(t)$ por la cadena relativa.

### Microcontrol 053

[]{#MA-MIC-ANM-01-024-053}

[]{#MA-MSOL-ANM-01-024-053}

**Pregunta.** ¿Debe ser monótono $g$ en la versión probada?

**Solución.** No. Los recorridos se cancelan con el signo de la derivada.

### Microcontrol 054

[]{#MA-MIC-ANM-01-024-054}

[]{#MA-MSOL-ANM-01-024-054}

**Pregunta.** ¿Qué pasa si $g(\alpha)=g(\beta)$?

**Solución.** La integral transformada vale cero bajo todas las hipótesis de la fórmula.

### Microcontrol 055

[]{#MA-MIC-ANM-01-024-055}

[]{#MA-MSOL-ANM-01-024-055}

**Pregunta.** ¿Puede la cadena dividir siempre por el incremento de $g$?

**Solución.** No. C18 usa una versión que admite incrementos interiores nulos.

### Microcontrol 056

[]{#MA-MIC-ANM-01-024-056}

[]{#MA-MSOL-ANM-01-024-056}

**Pregunta.** ¿Reemplazar $g'$ por $|g'|$ conserva la misma identidad?

**Solución.** No. Elimina la orientación que permite cancelación y define otra expresión.

## §24.8 — Qué invierte el teorema y qué conserva

### Microcontrol 057

[]{#MA-MIC-ANM-01-024-057}

[]{#MA-MSOL-ANM-01-024-057}

[]{#MA-SEC-ANM-01-024-008}

**Pregunta.** ¿Qué recupera integrar y luego derivar una continua?

**Solución.** Sus valores interiores y sus valores de borde mediante derivadas relativas.

### Microcontrol 058

[]{#MA-MIC-ANM-01-024-058}

[]{#MA-MSOL-ANM-01-024-058}

**Pregunta.** ¿Qué recupera derivar e integrar una primitiva admisible?

**Solución.** $H(x)-H(a)$; hace falta reponer el dato inicial para recuperar $H$.

### Microcontrol 059

[]{#MA-MIC-ANM-01-024-059}

[]{#MA-MSOL-ANM-01-024-059}

**Pregunta.** ¿Qué certificado da $|f-g|\le\eta$?

**Solución.** $|A_f(x)-A_g(x)|\le\eta(x-a)$, y por tanto cota global $\eta(b-a)$.

### Microcontrol 060

[]{#MA-MIC-ANM-01-024-060}

[]{#MA-MSOL-ANM-01-024-060}

**Pregunta.** ¿Qué término agrega un error en el dato inicial?

**Solución.** La distancia $|c_0-d_0|$ se suma al certificado acumulado de la tasa.

### Microcontrol 061

[]{#MA-MIC-ANM-01-024-061}

[]{#MA-MSOL-ANM-01-024-061}

**Pregunta.** ¿Cambios finitos de tasas alteran sus acumuladas?

**Solución.** No. Todas las restricciones conservan sus integrales por C23.

### Microcontrol 062

[]{#MA-MIC-ANM-01-024-062}

[]{#MA-MSOL-ANM-01-024-062}

**Pregunta.** ¿Qué asegura un promedio integral alcanzado?

**Solución.** Continuidad en un cerrado, extremos de C16 y valor intermedio de C15; no mera integrabilidad.

### Microcontrol 063

[]{#MA-MIC-ANM-01-024-063}

[]{#MA-MSOL-ANM-01-024-063}

**Pregunta.** ¿El escalón alcanza su promedio integral?

**Solución.** No. Su promedio en $[0,1]$ es $1/2$ y sus únicos valores son cero y uno.

### Microcontrol 064

[]{#MA-MIC-ANM-01-024-064}

[]{#MA-MSOL-ANM-01-024-064}

**Pregunta.** ¿Se ha probado que toda derivada es integrable?

**Solución.** No. La integrabilidad de la extensión sigue siendo una hipótesis explícita.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 24](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html) · [Ejercicios](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo-microcontroles.html)
