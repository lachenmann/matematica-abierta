---
content-id: MA-BCH-0285
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-020-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 20
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C20_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 20](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes.html) · [Ejercicios](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §20.1 — Un segmento impone un orden

### Microcontrol 001

[]{#MA-MIC-ANM-01-020-001}

[]{#MA-MSOL-ANM-01-020-001}

[]{#MA-SEC-ANM-01-020-001}

**Pregunta.** ¿Qué debe contener el dominio para comparar dos entradas por convexidad?

**Solución.** Todo el segmento entre ellas, pues se evalúan todas las combinaciones $(1-t)a+tb$. Un intervalo conserva esas entradas.

### Microcontrol 002

[]{#MA-MIC-ANM-01-020-002}

[]{#MA-MSOL-ANM-01-020-002}

**Pregunta.** ¿Qué procedimientos compara la desigualdad de convexidad?

**Solución.** Evaluar la función en la combinación de entradas y combinar las dos salidas con los mismos pesos.

### Microcontrol 003

[]{#MA-MIC-ANM-01-020-003}

[]{#MA-MSOL-ANM-01-020-003}

**Pregunta.** ¿Por qué se excluyen pesos extremos y entradas iguales al exigir convexidad estricta?

**Solución.** En esos casos ambos lados coinciden necesariamente, así que no pueden satisfacer una desigualdad estricta.

### Microcontrol 004

[]{#MA-MIC-ANM-01-020-004}

[]{#MA-MSOL-ANM-01-020-004}

**Pregunta.** ¿Qué diferencia de convexidad tiene el cuadrado?

**Solución.** $t(1-t)(b-a)^2$, no negativa siempre y positiva para entradas distintas y pesos interiores.

### Microcontrol 005

[]{#MA-MIC-ANM-01-020-005}

[]{#MA-MSOL-ANM-01-020-005}

**Pregunta.** ¿Puede una función ser convexa y cóncava?

**Solución.** Sí. Toda función afín satisface igualdad en todas las combinaciones.

### Microcontrol 006

[]{#MA-MIC-ANM-01-020-006}

[]{#MA-MSOL-ANM-01-020-006}

**Pregunta.** ¿El valor absoluto es estrictamente convexo?

**Solución.** No: aunque es convexo por la desigualdad triangular, tiene segmentos afines, por ejemplo entre dos entradas positivas.

### Microcontrol 007

[]{#MA-MIC-ANM-01-020-007}

[]{#MA-MSOL-ANM-01-020-007}

**Pregunta.** ¿La convexidad exige derivabilidad?

**Solución.** No. El valor absoluto es convexo y no derivable en cero; la definición sólo compara valores.

### Microcontrol 008

[]{#MA-MIC-ANM-01-020-008}

[]{#MA-MSOL-ANM-01-020-008}

**Pregunta.** ¿Qué signo permite sumar desigualdades de convexidad con coeficientes?

**Solución.** Coeficientes no negativos. Un coeficiente negativo invierte la desigualdad y no conserva el argumento.

## §20.2 — Tres pendientes y una rigidez

### Microcontrol 009

[]{#MA-MIC-ANM-01-020-009}

[]{#MA-MSOL-ANM-01-020-009}

[]{#MA-SEC-ANM-01-020-002}

**Pregunta.** ¿Qué coeficiente expresa $v$ entre $u<v<w$?

**Solución.** $t=(v-u)/(w-u)$ en $v=(1-t)u+tw$, con $0<t<1$.

### Microcontrol 010

[]{#MA-MIC-ANM-01-020-010}

[]{#MA-MSOL-ANM-01-020-010}

**Pregunta.** ¿Cuál es el orden de las tres pendientes para una función convexa?

**Solución.** $S(u,v)\le S(u,w)\le S(v,w)$.

### Microcontrol 011

[]{#MA-MIC-ANM-01-020-011}

[]{#MA-MSOL-ANM-01-020-011}

**Pregunta.** ¿Por qué la secante larga queda entre las cortas?

**Solución.** Es su media ponderada con pesos positivos $(v-u)/(w-u)$ y $(w-v)/(w-u)$; además las cortas están ordenadas.

### Microcontrol 012

[]{#MA-MIC-ANM-01-020-012}

[]{#MA-MSOL-ANM-01-020-012}

**Pregunta.** ¿Basta el orden $S(u,v)\le S(v,w)$ para todos los triples?

**Solución.** Sí. Multiplicar por los denominadores positivos y reorganizar recupera la desigualdad de convexidad en cada entrada interior.

### Microcontrol 013

[]{#MA-MIC-ANM-01-020-013}

[]{#MA-MSOL-ANM-01-020-013}

**Pregunta.** ¿Qué ocurre en el orden de pendientes si la convexidad es estricta?

**Solución.** Las dos comparaciones son estrictas para cada triple de entradas distintas.

### Microcontrol 014

[]{#MA-MIC-ANM-01-020-014}

[]{#MA-MSOL-ANM-01-020-014}

**Pregunta.** ¿Qué fuerza una igualdad interior con una cuerda de una función convexa?

**Solución.** Que la función coincida con esa recta en todo el segmento de la cuerda.

### Microcontrol 015

[]{#MA-MIC-ANM-01-020-015}

[]{#MA-MSOL-ANM-01-020-015}

**Pregunta.** ¿Cómo se excluye un punto elevado de $h=\ell-f$ al tener $h(z)=0$ interior?

**Solución.** Se expresa $z$ entre ese punto y el borde opuesto; concavidad de $h$ y no negatividad fuerzan que el valor del punto sea cero.

### Microcontrol 016

[]{#MA-MIC-ANM-01-020-016}

[]{#MA-MSOL-ANM-01-020-016}

**Pregunta.** ¿Cómo se caracteriza convexidad estricta sin derivadas?

**Solución.** Una función convexa es estrictamente convexa si y sólo si no es afín en ningún subsegmento con extremos distintos.

## §20.3 — La convexidad fabrica continuidad

### Microcontrol 017

[]{#MA-MIC-ANM-01-020-017}

[]{#MA-MSOL-ANM-01-020-017}

[]{#MA-SEC-ANM-01-020-003}

**Pregunta.** ¿Qué margen se necesita para una constante Lipschitz en $[c,d]$?

**Solución.** Entradas exteriores $a<c<d<b$ en el dominio, para encerrar las pendientes interiores entre $S(a,c)$ y $S(d,b)$.

### Microcontrol 018

[]{#MA-MIC-ANM-01-020-018}

[]{#MA-MSOL-ANM-01-020-018}

**Pregunta.** ¿Qué constante construye la banda de secantes?

**Solución.** $L=\max\{|S(a,c)|,|S(d,b)|\}$; entonces $|f(y)-f(x)|\le L|y-x|$ en $[c,d]$.

### Microcontrol 019

[]{#MA-MIC-ANM-01-020-019}

[]{#MA-MSOL-ANM-01-020-019}

**Pregunta.** ¿Qué radio sirve cuando $L>0$?

**Solución.** $\delta=\varepsilon/L$; el incremento es menor que $\varepsilon$ si la distancia es menor que ese radio.

### Microcontrol 020

[]{#MA-MIC-ANM-01-020-020}

[]{#MA-MSOL-ANM-01-020-020}

**Pregunta.** ¿Qué hacer si $L=0$?

**Solución.** La banda obliga a todas las pendientes a ser cero en ese segmento, así la función es constante y cualquier radio positivo sirve.

### Microcontrol 021

[]{#MA-MIC-ANM-01-020-021}

[]{#MA-MSOL-ANM-01-020-021}

**Pregunta.** ¿La convexidad finita garantiza continuidad en un borde incluido?

**Solución.** No. En $[0,1]$, valor1 en cero y0 en las entradas positivas define una función convexa discontinua en cero.

### Microcontrol 022

[]{#MA-MIC-ANM-01-020-022}

[]{#MA-MSOL-ANM-01-020-022}

**Pregunta.** ¿Qué límites laterales de pendientes existen en un centro interior?

**Solución.** $f\prime_-(c)=A=\sup_{x<c}S(x,c)$ y $f\prime_+(c)=B=\inf_{y>c}S(c,y)$, ambos reales finitos y con $A\le B$.

### Microcontrol 023

[]{#MA-MIC-ANM-01-020-023}

[]{#MA-MSOL-ANM-01-020-023}

**Pregunta.** ¿Qué dato del supremo construye el radio del límite izquierdo?

**Solución.** Una entrada $x_0<c$ cuya secante supera $A-\varepsilon$; las entradas entre $x_0$ y $c$ quedan entre esa cota y $A$.

### Microcontrol 024

[]{#MA-MIC-ANM-01-020-024}

[]{#MA-MSOL-ANM-01-020-024}

**Pregunta.** ¿Cuándo existe la derivada bilateral de una función convexa en un centro interior?

**Solución.** Exactamente cuando $A=B$. Para $|x|$ en cero son−1 y1, así hay continuidad pero no derivabilidad.

## §20.4 — Rectas que sostienen y una envolvente

### Microcontrol 025

[]{#MA-MIC-ANM-01-020-025}

[]{#MA-MSOL-ANM-01-020-025}

[]{#MA-SEC-ANM-01-020-004}

**Pregunta.** ¿Qué pendientes sostienen una función convexa desde un centro interior?

**Solución.** Exactamente los números del intervalo $[f\prime_-(c),f\prime_+(c)]$.

### Microcontrol 026

[]{#MA-MIC-ANM-01-020-026}

[]{#MA-MSOL-ANM-01-020-026}

**Pregunta.** ¿Qué cambia al multiplicar una comparación de pendientes por $x-c<0$?

**Solución.** Se invierte la desigualdad; esto transforma $S(x,c)\le p$ en $f(x)-f(c)\ge p(x-c)$.

### Microcontrol 027

[]{#MA-MIC-ANM-01-020-027}

[]{#MA-MSOL-ANM-01-020-027}

**Pregunta.** ¿Qué pendiente de soporte queda si la función es derivable?

**Solución.** Sólo $f\prime(c)$, porque coinciden las dos derivadas laterales.

### Microcontrol 028

[]{#MA-MIC-ANM-01-020-028}

[]{#MA-MSOL-ANM-01-020-028}

**Pregunta.** ¿Qué familia de rectas sostiene $|x|$ en cero?

**Solución.** $px$ para $-1\le p\le1$; no hay una tangente bilateral única.

### Microcontrol 029

[]{#MA-MIC-ANM-01-020-029}

[]{#MA-MSOL-ANM-01-020-029}

**Pregunta.** ¿Qué identidad verifica el soporte de la tangente del cuadrado?

**Solución.** $x^2-(2cx-c^2)=(x-c)^2\ge0$.

### Microcontrol 030

[]{#MA-MIC-ANM-01-020-030}

[]{#MA-MSOL-ANM-01-020-030}

**Pregunta.** ¿Por qué el supremo de todos los soportes recupera $f(x)$ en un intervalo abierto?

**Solución.** Todos están debajo de $f(x)$ y alguno con centro $c=x$ alcanza ese valor; la familia es no vacía y acotada superiormente.

### Microcontrol 031

[]{#MA-MIC-ANM-01-020-031}

[]{#MA-MSOL-ANM-01-020-031}

**Pregunta.** ¿Debe alcanzarse el supremo de una familia de rectas para que sea convexo?

**Solución.** No. Basta que la familia sea no vacía y su supremo sea finito en cada entrada; se toma el supremo de sus desigualdades afines.

### Microcontrol 032

[]{#MA-MIC-ANM-01-020-032}

[]{#MA-MSOL-ANM-01-020-032}

**Pregunta.** ¿En qué dirección controla una cuerda y en cuál un soporte?

**Solución.** En una función convexa, la cuerda queda arriba dentro de su segmento y el soporte queda abajo en todo el intervalo.

## §20.5 — Derivadas ordenadas, curvas convexas

### Microcontrol 033

[]{#MA-MIC-ANM-01-020-033}

[]{#MA-MSOL-ANM-01-020-033}

[]{#MA-SEC-ANM-01-020-005}

**Pregunta.** ¿Qué orden tiene $f\prime$ cuando $f$ es convexa y derivable en un intervalo abierto?

**Solución.** Es no decreciente; para $x<y$, $f\prime(x)\le S(x,y)\le f\prime(y)$.

### Microcontrol 034

[]{#MA-MIC-ANM-01-020-034}

[]{#MA-MSOL-ANM-01-020-034}

**Pregunta.** ¿Dónde quedan los dos centros de Lagrange usados para probar convexidad?

**Solución.** Uno en $(u,v)$ y otro en $(v,w)$; por ello el primero es menor que el segundo y sus derivadas pueden compararse.

### Microcontrol 035

[]{#MA-MIC-ANM-01-020-035}

[]{#MA-MSOL-ANM-01-020-035}

**Pregunta.** ¿Se exige continuidad de $f\prime$ en esa prueba?

**Solución.** No. Se usa el orden de sus valores y Lagrange para $f$, cuya continuidad procede de su derivabilidad.

### Microcontrol 036

[]{#MA-MIC-ANM-01-020-036}

[]{#MA-MSOL-ANM-01-020-036}

**Pregunta.** ¿Qué cancela los términos de pendiente en la prueba por soporte en $z$?

**Solución.** La identidad $(1-t)(a-z)+t(b-z)=0$ al sumar los dos soportes con los pesos correspondientes.

### Microcontrol 037

[]{#MA-MIC-ANM-01-020-037}

[]{#MA-MSOL-ANM-01-020-037}

**Pregunta.** ¿Qué implica $f\prime(x)=f\prime(y)$ para $x<y$ si $f\prime$ no decrece?

**Solución.** Que $f\prime$ es constante entre ambos; C19 aplicado a $f(t)-kt$ hace afín ese tramo.

### Microcontrol 038

[]{#MA-MIC-ANM-01-020-038}

[]{#MA-MSOL-ANM-01-020-038}

**Pregunta.** ¿La derivada creciente obliga a que la propia función crezca?

**Solución.** No. Para $x^2$, la derivada $2x$ crece en toda la recta mientras la función decrece a la izquierda de cero.

### Microcontrol 039

[]{#MA-MIC-ANM-01-020-039}

[]{#MA-MSOL-ANM-01-020-039}

**Pregunta.** ¿Una función estrictamente creciente es necesariamente convexa?

**Solución.** No. El cubo crece estrictamente, pero $3x^2$ decrece en el semieje negativo, así el cubo no es convexo en toda la recta.

### Microcontrol 040

[]{#MA-MIC-ANM-01-020-040}

[]{#MA-MSOL-ANM-01-020-040}

**Pregunta.** ¿Qué hipótesis adicional extiende el criterio a los extremos de $[a,b]$?

**Solución.** Continuidad de $f$ incluyendo ambos bordes, además de derivabilidad interior y orden de la derivada.

## §20.6 — La segunda derivada y sus límites

### Microcontrol 041

[]{#MA-MIC-ANM-01-020-041}

[]{#MA-MSOL-ANM-01-020-041}

[]{#MA-SEC-ANM-01-020-006}

**Pregunta.** ¿Qué significa que exista $f\prime\prime(c)$?

**Solución.** Que la función derivada está definida alrededor de $c$ y es derivable allí; no basta una derivada aislada de $f$.

### Microcontrol 042

[]{#MA-MIC-ANM-01-020-042}

[]{#MA-MSOL-ANM-01-020-042}

**Pregunta.** ¿Qué condición caracteriza convexidad cuando $f$ es dos veces derivable en todo un intervalo abierto?

**Solución.** $f\prime\prime(x)\ge0$ en todos sus puntos.

### Microcontrol 043

[]{#MA-MIC-ANM-01-020-043}

[]{#MA-MSOL-ANM-01-020-043}

**Pregunta.** ¿Por qué puede aplicarse C19 a $f\prime$ sin pedir continuidad de $f\prime\prime$?

**Solución.** La existencia de $f\prime\prime$ da derivabilidad y por ello continuidad de $f\prime$ en cada segmento; no pide continuidad de su derivada.

### Microcontrol 044

[]{#MA-MIC-ANM-01-020-044}

[]{#MA-MSOL-ANM-01-020-044}

**Pregunta.** ¿Es necesaria $f\prime\prime>0$ en todos los puntos para convexidad estricta?

**Solución.** No. $x^4$ es estrictamente convexa y tiene segunda derivada cero en el origen.

### Microcontrol 045

[]{#MA-MIC-ANM-01-020-045}

[]{#MA-MSOL-ANM-01-020-045}

**Pregunta.** ¿Cómo puede $1/x$ ser decreciente y estrictamente convexa en $(0,\infty)$?

**Solución.** Su primera derivada es negativa y su segunda derivada es positiva: controlan propiedades distintas.

### Microcontrol 046

[]{#MA-MIC-ANM-01-020-046}

[]{#MA-MSOL-ANM-01-020-046}

**Pregunta.** ¿Qué certifica $f\prime(c)=0$ en una función convexa derivable?

**Solución.** Un mínimo global mediante el soporte horizontal; si la convexidad es estricta, ese mínimo es único.

### Microcontrol 047

[]{#MA-MIC-ANM-01-020-047}

[]{#MA-MSOL-ANM-01-020-047}

**Pregunta.** ¿Qué decide por sí solo el valor $f\prime\prime(c)=0$?

**Solución.** No decide extremo, cambio de convexidad ni falta de convexidad estricta; $x^3$ y $x^4$ distinguen esas posibilidades.

### Microcontrol 048

[]{#MA-MIC-ANM-01-020-048}

[]{#MA-MSOL-ANM-01-020-048}

**Pregunta.** ¿La convexidad estricta garantiza un mínimo alcanzado en un intervalo abierto?

**Solución.** No. $x^2$ sobre $(0,1)$ tiene ínfimo cero sin entrada que lo alcance.

## §20.7 — Jensen: combinar sin perder el control

### Microcontrol 049

[]{#MA-MIC-ANM-01-020-049}

[]{#MA-MSOL-ANM-01-020-049}

[]{#MA-SEC-ANM-01-020-007}

**Pregunta.** ¿Qué condiciones tienen los pesos de Jensen finito?

**Solución.** Son no negativos, suman1 y se usan con un número finito no nulo de entradas del intervalo.

### Microcontrol 050

[]{#MA-MIC-ANM-01-020-050}

[]{#MA-MSOL-ANM-01-020-050}

**Pregunta.** ¿Qué hacer si la suma $s$ de los primeros pesos es cero?

**Solución.** Todos esos pesos son cero; la combinación sólo tiene la última entrada y hay igualdad, sin normalizar ni dividir.

### Microcontrol 051

[]{#MA-MIC-ANM-01-020-051}

[]{#MA-MSOL-ANM-01-020-051}

**Pregunta.** ¿Por qué la media normalizada de un grupo sigue en el dominio?

**Solución.** Sus pesos no negativos suman1 y, por inducción, toda combinación finita de entradas de un intervalo permanece en él.

### Microcontrol 052

[]{#MA-MIC-ANM-01-020-052}

[]{#MA-MSOL-ANM-01-020-052}

**Pregunta.** ¿Cuándo hay igualdad en Jensen para una función estrictamente convexa?

**Solución.** Exactamente cuando todas las entradas con peso positivo son iguales; las entradas con peso cero no importan.

### Microcontrol 053

[]{#MA-MIC-ANM-01-020-053}

[]{#MA-MSOL-ANM-01-020-053}

**Pregunta.** ¿Qué identidad da la diferencia de Jensen para el cuadrado?

**Solución.** $\sum_i\lambda_i x_i^2-\mu^2=\sum_i\lambda_i(x_i-\mu)^2$, donde $\mu=\sum_i\lambda_i x_i$.

### Microcontrol 054

[]{#MA-MIC-ANM-01-020-054}

[]{#MA-MSOL-ANM-01-020-054}

**Pregunta.** ¿Qué media resulta de pesos $(1/4,1/2,1/4)$ y entradas $(0,1,3)$?

**Solución.** $\mu=5/4$; la media de cuadrados es $11/4$ y la diferencia es $19/16$.

### Microcontrol 055

[]{#MA-MIC-ANM-01-020-055}

[]{#MA-MSOL-ANM-01-020-055}

**Pregunta.** ¿Por qué puede invertirse la media en Jensen para $1/x$?

**Solución.** Todas las entradas son positivas y al menos un peso es positivo, así la media también es positiva.

### Microcontrol 056

[]{#MA-MIC-ANM-01-020-056}

[]{#MA-MSOL-ANM-01-020-056}

**Pregunta.** ¿Basta que los pesos sumen1 si alguno es negativo?

**Solución.** No. Pesos2 y−1 con entradas0 y1 violan Jensen para el cuadrado:1 no es menor o igual que−1.

## §20.8 — Bandas cuadráticas y mínimos certificados

### Microcontrol 057

[]{#MA-MIC-ANM-01-020-057}

[]{#MA-MSOL-ANM-01-020-057}

[]{#MA-SEC-ANM-01-020-008}

**Pregunta.** ¿Qué función auxiliar convierte $f\prime\prime\ge m$ en convexidad?

**Solución.** $q_m(x)=f(x)-(m/2)x^2$, cuya segunda derivada es $f\prime\prime-m\ge0$.

### Microcontrol 058

[]{#MA-MIC-ANM-01-020-058}

[]{#MA-MSOL-ANM-01-020-058}

**Pregunta.** ¿Qué banda encierra la diferencia respecto de una tangente?

**Solución.** Entre $(m/2)(x-c)^2$ y $(M/2)(x-c)^2$ si $m\le f\prime\prime\le M$ en todo el intervalo.

### Microcontrol 059

[]{#MA-MIC-ANM-01-020-059}

[]{#MA-MSOL-ANM-01-020-059}

**Pregunta.** ¿Debe ser $m$ positivo para la banda firmada?

**Solución.** No. Cualquier par real $m\le M$ sirve; si sólo $|f\prime\prime|\le K$, se toman−K yK.

### Microcontrol 060

[]{#MA-MIC-ANM-01-020-060}

[]{#MA-MSOL-ANM-01-020-060}

**Pregunta.** ¿Qué factor aparece en el error de una cuerda?

**Solución.** $t(1-t)(b-a)^2/2$, multiplicado por $m$ y por $M$ como cotas inferior y superior.

### Microcontrol 061

[]{#MA-MIC-ANM-01-020-061}

[]{#MA-MSOL-ANM-01-020-061}

**Pregunta.** ¿Qué añade $m>0$ al control cualitativo?

**Solución.** Una separación cuadrática positiva entre tangente y función para entradas distintas y, si existe un centro estacionario, unicidad del mínimo.

### Microcontrol 062

[]{#MA-MIC-ANM-01-020-062}

[]{#MA-MSOL-ANM-01-020-062}

**Pregunta.** ¿Qué certificado de posición da una pendiente residual?

**Solución.** Si existe $r$ con $f\prime(r)=0$ y $f\prime\prime\ge m>0$, entonces $|x-r|\le|f\prime(x)|/m$.

### Microcontrol 063

[]{#MA-MIC-ANM-01-020-063}

[]{#MA-MSOL-ANM-01-020-063}

**Pregunta.** ¿Qué certificado de pérdida de valor acompaña al de posición?

**Solución.** $0\le f(x)-f(r)\le f\prime(x)^2/(2m)$, demostrado desde la banda inferior y completando un cuadrado.

### Microcontrol 064

[]{#MA-MIC-ANM-01-020-064}

[]{#MA-MSOL-ANM-01-020-064}

**Pregunta.** ¿La convexidad estricta permite siempre dividir por una constante uniforme $m>0$?

**Solución.** No. Para $x^4$ cerca de cero, $f\prime\prime(0)=0$ y $|f\prime(x)|/|x|=4x^2\to0$; la hipótesis cuantitativa falta.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 20](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes.html) · [Ejercicios](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes-microcontroles.html)
