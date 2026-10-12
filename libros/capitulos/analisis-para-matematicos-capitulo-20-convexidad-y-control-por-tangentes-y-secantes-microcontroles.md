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
date-modified: '2026-10-12'
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

Para $0\le t\le1$, la combinación se sitúa entre los extremos y debe ser una entrada admisible. No basta que existan sólo las dos evaluaciones de borde. Intervalaridad garantiza todas las evaluaciones que exige la desigualdad. Así se comprueba el dominio antes de comparar las alturas.

### Microcontrol 002

[]{#MA-MIC-ANM-01-020-002}

[]{#MA-MSOL-ANM-01-020-002}

**Pregunta.** ¿Qué procedimientos compara la desigualdad de convexidad?

**Solución.** Evaluar la función en la combinación de entradas y combinar las dos salidas con los mismos pesos.

Ambos procedimientos usan los mismos pesos, pero en distinto orden: en uno se combina antes de evaluar y en el otro después. Convexidad afirma que la primera altura no supera la segunda. No equivale a comparar simplemente $f(a)$ con $f(b)$, que sería una pregunta de monotonía.

### Microcontrol 003

[]{#MA-MIC-ANM-01-020-003}

[]{#MA-MSOL-ANM-01-020-003}

**Pregunta.** ¿Por qué se excluyen pesos extremos y entradas iguales al exigir convexidad estricta?

**Solución.** En esos casos ambos lados coinciden necesariamente, así que no pueden satisfacer una desigualdad estricta.

Un peso cero o uno devuelve una entrada de borde y su salida exacta en ambos lados. Si las entradas coinciden, todos los pesos devuelven el mismo punto. La condición estricta sólo puede pedirse cuando hay una entrada interior entre extremos distintos. La definición separa por ello los casos triviales.

### Microcontrol 004

[]{#MA-MIC-ANM-01-020-004}

[]{#MA-MSOL-ANM-01-020-004}

**Pregunta.** ¿Qué diferencia de convexidad tiene el cuadrado?

**Solución.** $t(1-t)(b-a)^2$, no negativa siempre y positiva para entradas distintas y pesos interiores.

La diferencia es la altura interpolada menos la salida en la entrada combinada. Sus tres factores son no negativos en el rango de pesos permitido. Para una combinación interior entre puntos distintos ninguno se anula. Esta identidad prueba también todos los casos de igualdad, sin criterios diferenciales.

### Microcontrol 005

[]{#MA-MIC-ANM-01-020-005}

[]{#MA-MSOL-ANM-01-020-005}

**Pregunta.** ¿Puede una función ser convexa y cóncava?

**Solución.** Sí. Toda función afín satisface igualdad en todas las combinaciones.

Una afín tiene forma $A+Bx$ y evaluar la combinación produce exactamente la combinación de sus salidas. Por ello cumple a la vez la comparación convexa y la inversa cóncava. La igualdad no aporta convexidad estricta en un segmento no degenerado. La pendiente puede tener cualquier signo.

### Microcontrol 006

[]{#MA-MIC-ANM-01-020-006}

[]{#MA-MSOL-ANM-01-020-006}

**Pregunta.** ¿El valor absoluto es estrictamente convexo?

**Solución.** No: aunque es convexo por la desigualdad triangular, tiene segmentos afines, por ejemplo entre dos entradas positivas.

En entradas positivas el valor absoluto coincide con la identidad y toda combinación permanece allí. Las dos alturas son iguales aunque los extremos sean distintos y el peso interior. Un solo par así basta para refutar convexidad estricta. La triangular sigue probando convexidad débil para todos los pares.

### Microcontrol 007

[]{#MA-MIC-ANM-01-020-007}

[]{#MA-MSOL-ANM-01-020-007}

**Pregunta.** ¿La convexidad exige derivabilidad?

**Solución.** No. El valor absoluto es convexo y no derivable en cero; la definición sólo compara valores.

La definición sólo utiliza evaluaciones y orden de alturas. Una esquina puede cumplir todas esas desigualdades sin tener un límite bilateral de secantes. El valor absoluto acredita ambos hechos mediante triangular y pendientes laterales opuestas. Los criterios por derivadas posteriores tienen hipótesis adicionales.

### Microcontrol 008

[]{#MA-MIC-ANM-01-020-008}

[]{#MA-MSOL-ANM-01-020-008}

**Pregunta.** ¿Qué signo permite sumar desigualdades de convexidad con coeficientes?

**Solución.** Coeficientes no negativos. Un coeficiente negativo invierte la desigualdad y no conserva el argumento.

Multiplicar una desigualdad por un coeficiente positivo conserva su sentido; por cero la convierte en igualdad. Por ello la suma no negativa conserva convexidad. Un coeficiente negativo invierte el sentido y no ofrece la misma garantía. El negativo del cuadrado refuta una conservación universal sin esa condición.

## §20.2 — Tres pendientes y una rigidez

### Microcontrol 009

[]{#MA-MIC-ANM-01-020-009}

[]{#MA-MSOL-ANM-01-020-009}

[]{#MA-SEC-ANM-01-020-002}

**Pregunta.** ¿Qué coeficiente expresa $v$ entre $u<v<w$?

**Solución.** $t=(v-u)/(w-u)$ en $v=(1-t)u+tw$, con $0<t<1$.

Los dos incrementos que forman el cociente son positivos y el numerador es menor que el denominador. Así el peso pertenece estrictamente a $(0,1)$. Sustituirlo en la combinación recupera exactamente $v$. Esta traducción permite pasar de una desigualdad de alturas a una de secantes.

### Microcontrol 010

[]{#MA-MIC-ANM-01-020-010}

[]{#MA-MSOL-ANM-01-020-010}

**Pregunta.** ¿Cuál es el orden de las tres pendientes para una función convexa?

**Solución.** $S(u,v)\le S(u,w)\le S(v,w)$.

Cada secante tiene denominador positivo porque sus extremos están ordenados. Convexidad en la entrada intermedia se reorganiza para colocar las dos cortas en orden. La secante larga es una media positiva de ellas y queda entre ambas. El orden se refiere a pendientes, no necesariamente a alturas crecientes.

### Microcontrol 011

[]{#MA-MIC-ANM-01-020-011}

[]{#MA-MSOL-ANM-01-020-011}

**Pregunta.** ¿Por qué la secante larga queda entre las cortas?

**Solución.** Es su media ponderada con pesos positivos $(v-u)/(w-u)$ y $(w-v)/(w-u)$; además las cortas están ordenadas.

La diferencia total se descompone en la suma de los incrementos de las dos piezas. Dividir por la longitud total convierte sus longitudes en pesos positivos de suma uno. Una media así queda entre dos valores ordenados. Si éstos son distintos, queda estrictamente entre ellos.

### Microcontrol 012

[]{#MA-MIC-ANM-01-020-012}

[]{#MA-MSOL-ANM-01-020-012}

**Pregunta.** ¿Basta el orden $S(u,v)\le S(v,w)$ para todos los triples?

**Solución.** Sí. Multiplicar por los denominadores positivos y reorganizar recupera la desigualdad de convexidad en cada entrada interior.

Cada combinación interior puede escribirse como el centro de un triple ordenado. La desigualdad entre sus secantes cortas se multiplica por longitudes positivas y se convierte en la comparación de cuerda. Los pesos extremos se resuelven por igualdad. Así la condición para todos los triples recupera toda la definición.

### Microcontrol 013

[]{#MA-MIC-ANM-01-020-013}

[]{#MA-MSOL-ANM-01-020-013}

**Pregunta.** ¿Qué ocurre en el orden de pendientes si la convexidad es estricta?

**Solución.** Las dos comparaciones son estrictas para cada triple de entradas distintas.

La comparación de cuerda es estricta en la entrada intermedia. Al reorganizarla sólo se multiplica o divide por distancias positivas, conservando estrictitud. Las secantes cortas resultan distintas y la larga queda estrictamente entre ellas. Los triples deben tener tres entradas distintas para que las divisiones estén definidas.

### Microcontrol 014

[]{#MA-MIC-ANM-01-020-014}

[]{#MA-MSOL-ANM-01-020-014}

**Pregunta.** ¿Qué fuerza una igualdad interior con una cuerda de una función convexa?

**Solución.** Que la función coincida con esa recta en todo el segmento de la cuerda.

La convexidad ya sitúa la función debajo de la cuerda en todo el segmento. Si toca la cuerda en un punto interior, concavidad de la diferencia impide que exista una altura positiva restante. El argumento se realiza a ambos lados del contacto. La afinidad forzada se limita a ese segmento y no a todo el dominio.

### Microcontrol 015

[]{#MA-MIC-ANM-01-020-015}

[]{#MA-MSOL-ANM-01-020-015}

**Pregunta.** ¿Cómo se excluye un punto elevado de $h=\ell-f$ al tener $h(z)=0$ interior?

**Solución.** Se expresa $z$ entre ese punto y el borde opuesto; concavidad de $h$ y no negatividad fuerzan que el valor del punto sea cero.

Si el punto está a la izquierda de $z$, se combina con el borde derecho; si está a la derecha, con el izquierdo. El peso del punto es positivo en ambos casos. La desigualdad cóncava obligaría al cero de $h(z)$ a dominar una cantidad positiva si aquel punto tuviera altura positiva. Como $h$ no es negativa, sólo queda altura cero.

### Microcontrol 016

[]{#MA-MIC-ANM-01-020-016}

[]{#MA-MSOL-ANM-01-020-016}

**Pregunta.** ¿Cómo se caracteriza convexidad estricta sin derivadas?

**Solución.** Una función convexa es estrictamente convexa si y sólo si no es afín en ningún subsegmento con extremos distintos.

Una pieza afín daría igualdad para una combinación interior y refutaría estrictitud. Recíprocamente, para una función ya convexa, cualquier fallo de estrictitud interior debe ser una igualdad. La rigidez de cuerda convierte esa igualdad en una pieza afín. La caracterización utiliza valores y secantes, sin exigir derivabilidad.

## §20.3 — La convexidad fabrica continuidad

### Microcontrol 017

[]{#MA-MIC-ANM-01-020-017}

[]{#MA-MSOL-ANM-01-020-017}

[]{#MA-SEC-ANM-01-020-003}

**Pregunta.** ¿Qué margen se necesita para una constante Lipschitz en $[c,d]$?

**Solución.** Entradas exteriores $a<c<d<b$ en el dominio, para encerrar las pendientes interiores entre $S(a,c)$ y $S(d,b)$.

Las entradas exteriores aportan secantes fijas a ambos lados de todas las parejas de $[c,d]$. El orden de triples las convierte en barreras de pendientes. Sus denominadores positivos hacen finitos los valores de las barreras. En un borde sin margen exterior no puede suponerse este mismo control.

### Microcontrol 018

[]{#MA-MIC-ANM-01-020-018}

[]{#MA-MSOL-ANM-01-020-018}

**Pregunta.** ¿Qué constante construye la banda de secantes?

**Solución.** $L=\max\{|S(a,c)|,|S(d,b)|\}$; entonces $|f(y)-f(x)|\le L|y-x|$ en $[c,d]$.

Las secantes interiores quedan entre dos números reales fijos, aunque alguno sea negativo. El máximo de sus magnitudes domina cualquier número de esa banda. Multiplicar por la distancia de entrada da la cota de valores. Los pares iguales se tratan sin formar secantes y los invertidos por simetría.

### Microcontrol 019

[]{#MA-MIC-ANM-01-020-019}

[]{#MA-MSOL-ANM-01-020-019}

**Pregunta.** ¿Qué radio sirve cuando $L>0$?

**Solución.** $\delta=\varepsilon/L$; el incremento es menor que $\varepsilon$ si la distancia es menor que ese radio.

La barrera Lipschitz se ha demostrado primero para todos los pares del segmento. Para una precisión dada el radio se fija antes de conocerlos. La distancia estricta bajo $\varepsilon/L$ convierte la cota no estricta en error estricto. Esa misma escala prueba uniformidad de la restricción, además de continuidad.

### Microcontrol 020

[]{#MA-MIC-ANM-01-020-020}

[]{#MA-MSOL-ANM-01-020-020}

**Pregunta.** ¿Qué hacer si $L=0$?

**Solución.** La banda obliga a todas las pendientes a ser cero en ese segmento, así la función es constante y cualquier radio positivo sirve.

Si ambas magnitudes exteriores tienen máximo cero, las barreras de secantes son cero. Toda secante interior debe entonces valer cero y las alturas son iguales. No se utiliza la fórmula de radio que dividiría por $L$. Cualquier radio positivo satisface cualquier desafío porque el error de salida es cero.

### Microcontrol 021

[]{#MA-MIC-ANM-01-020-021}

[]{#MA-MSOL-ANM-01-020-021}

**Pregunta.** ¿La convexidad finita garantiza continuidad en un borde incluido?

**Solución.** No. En $[0,1]$, valor1 en cero y0 en las entradas positivas define una función convexa discontinua en cero.

La altura excepcional del borde está por encima de la constante interior y no viola las comparaciones de cuerda. Sin embargo, entradas positivas próximas tienen salidas cero frente al valor central uno. La continuidad interior permanece verdadera porque la función es localmente constante allí. Convexidad finita no protege automáticamente un extremo incluido.

### Microcontrol 022

[]{#MA-MIC-ANM-01-020-022}

[]{#MA-MSOL-ANM-01-020-022}

**Pregunta.** ¿Qué límites laterales de pendientes existen en un centro interior?

**Solución.** $f\prime_-(c)=A=\sup_{x<c}S(x,c)$ y $f\prime_+(c)=B=\inf_{y>c}S(c,y)$, ambos reales finitos y con $A\le B$.

Una secante fija del lado contrario acota las pendientes de cada lado. La interioridad garantiza que ambos conjuntos no sean vacíos y sus cotas óptimas sean reales finitas. La monotonía de secantes convierte esas cotas en límites laterales. El orden entre ellos expresa la posible esquina de una función convexa.

### Microcontrol 023

[]{#MA-MIC-ANM-01-020-023}

[]{#MA-MSOL-ANM-01-020-023}

**Pregunta.** ¿Qué dato del supremo construye el radio del límite izquierdo?

**Solución.** Una entrada $x_0<c$ cuya secante supera $A-\varepsilon$; las entradas entre $x_0$ y $c$ quedan entre esa cota y $A$.

El umbral $A-\varepsilon$ no es cota superior porque es menor que el supremo. Por ello existe un testigo cuya pendiente lo supera. Las secantes más próximas conservan esa cota inferior y no superan $A$. El radio $c-x_0>0$ acredita el límite sin construir una sucesión seleccionada.

### Microcontrol 024

[]{#MA-MIC-ANM-01-020-024}

[]{#MA-MSOL-ANM-01-020-024}

**Pregunta.** ¿Cuándo existe la derivada bilateral de una función convexa en un centro interior?

**Solución.** Exactamente cuando $A=B$. Para $|x|$ en cero son−1 y1, así hay continuidad pero no derivabilidad.

Si ambos límites coinciden, el mínimo de sus radios controla todas las entradas perforadas del centro, de ambos lados. Si la derivada bilateral existiera, sus restricciones laterales tendrían el mismo límite por unicidad. La igualdad de $A$ y $B$ es por tanto necesaria y suficiente. La continuidad del valor absoluto no obliga a esa igualdad.

## §20.4 — Rectas que sostienen y una envolvente

### Microcontrol 025

[]{#MA-MIC-ANM-01-020-025}

[]{#MA-MSOL-ANM-01-020-025}

[]{#MA-SEC-ANM-01-020-004}

**Pregunta.** ¿Qué pendientes sostienen una función convexa desde un centro interior?

**Solución.** Exactamente los números del intervalo $[f\prime_-(c),f\prime_+(c)]$.

Una recta de soporte debe quedar debajo en ambas direcciones desde el centro. Las entradas derechas acotan su pendiente por arriba y las izquierdas por abajo. Los supremos e ínfimos laterales convierten esas condiciones en el intervalo cerrado de pendientes permitido. La interioridad hace disponibles ambos controles.

### Microcontrol 026

[]{#MA-MIC-ANM-01-020-026}

[]{#MA-MSOL-ANM-01-020-026}

**Pregunta.** ¿Qué cambia al multiplicar una comparación de pendientes por $x-c<0$?

**Solución.** Se invierte la desigualdad; esto transforma $S(x,c)\le p$ en $f(x)-f(c)\ge p(x-c)$.

La secante izquierda tiene el mismo valor que el cociente centrado, pero su incremento $x-c$ es negativo. Multiplicar invierte la comparación de pendientes y produce la desigualdad de alturas correcta. Omitir esa inversión daría una recta por encima en el lado equivocado. El centro se verifica por igualdad directa.

### Microcontrol 027

[]{#MA-MIC-ANM-01-020-027}

[]{#MA-MSOL-ANM-01-020-027}

**Pregunta.** ¿Qué pendiente de soporte queda si la función es derivable?

**Solución.** Sólo $f\prime(c)$, porque coinciden las dos derivadas laterales.

Derivabilidad hace coincidir las dos cotas laterales en un único número. El intervalo de pendientes de soporte se reduce por ello a un singleton. Su recta es la tangente y sostiene globalmente la función convexa. Una esquina puede tener varias pendientes de soporte sin ninguna derivada bilateral.

### Microcontrol 028

[]{#MA-MIC-ANM-01-020-028}

[]{#MA-MSOL-ANM-01-020-028}

**Pregunta.** ¿Qué familia de rectas sostiene $|x|$ en cero?

**Solución.** $px$ para $-1\le p\le1$; no hay una tangente bilateral única.

Las entradas positivas exigen $p\le1$ y las negativas $p\ge-1$ al dividir con el signo correspondiente. En cero todas las rectas de esa familia coinciden con la función. Las dos pendientes laterales son sus extremos. El soporte no tiene que ser una secante límite bilateral única.

### Microcontrol 029

[]{#MA-MIC-ANM-01-020-029}

[]{#MA-MSOL-ANM-01-020-029}

**Pregunta.** ¿Qué identidad verifica el soporte de la tangente del cuadrado?

**Solución.** $x^2-(2cx-c^2)=(x-c)^2\ge0$.

El cuadrado restante es no negativo para toda entrada real. Por tanto la recta de pendiente $2c$ y valor central $c^2$ queda debajo globalmente. Sólo hay igualdad cuando $x=c$. La identidad acredita soporte y contacto sin recurrir a una interpretación visual de la tangente.

### Microcontrol 030

[]{#MA-MIC-ANM-01-020-030}

[]{#MA-MSOL-ANM-01-020-030}

**Pregunta.** ¿Por qué el supremo de todos los soportes recupera $f(x)$ en un intervalo abierto?

**Solución.** Todos están debajo de $f(x)$ y alguno con centro $c=x$ alcanza ese valor; la familia es no vacía y acotada superiormente.

Para un $x$ fijado, todas las rectas están acotadas por la salida finita $f(x)$. Al usar el propio $x$ como centro interior se obtiene un soporte que tiene igualdad allí. Esa pertenencia demuestra que el supremo es exactamente la salida. No hace falta escoger un soporte preferido para cada centro simultáneamente.

### Microcontrol 031

[]{#MA-MIC-ANM-01-020-031}

[]{#MA-MSOL-ANM-01-020-031}

**Pregunta.** ¿Debe alcanzarse el supremo de una familia de rectas para que sea convexo?

**Solución.** No. Basta que la familia sea no vacía y su supremo sea finito en cada entrada; se toma el supremo de sus desigualdades afines.

Cada recta tiene igualdad afín y sus valores en los bordes no superan el supremo allí. La combinación de esos dos supremos es una cota superior común de todas las alturas en la entrada intermedia. Tomar el supremo conserva esa cota. La demostración necesita finitud y no vacuidad, pero no un índice maximizador.

### Microcontrol 032

[]{#MA-MIC-ANM-01-020-032}

[]{#MA-MSOL-ANM-01-020-032}

**Pregunta.** ¿En qué dirección controla una cuerda y en cuál un soporte?

**Solución.** En una función convexa, la cuerda queda arriba dentro de su segmento y el soporte queda abajo en todo el intervalo.

La cuerda interpola dos evaluaciones y controla desde arriba sólo entre sus extremos. El soporte pasa por un punto central y controla desde abajo en todo el intervalo. Son comparaciones con regiones y sentidos diferentes. En una función afín ambas coinciden; para una convexa estricta los contactos tienen restricciones adicionales.

## §20.5 — Derivadas ordenadas, curvas convexas

### Microcontrol 033

[]{#MA-MIC-ANM-01-020-033}

[]{#MA-MSOL-ANM-01-020-033}

[]{#MA-SEC-ANM-01-020-005}

**Pregunta.** ¿Qué orden tiene $f\prime$ cuando $f$ es convexa y derivable en un intervalo abierto?

**Solución.** Es no decreciente; para $x<y$, $f\prime(x)\le S(x,y)\le f\prime(y)$.

La tangente de soporte en $x$ obliga a la secante hacia $y$ a ser al menos su pendiente. El soporte en $y$ da la cota opuesta. Así una secante queda entre las dos derivadas y éstas están ordenadas. No se presupone continuidad de la función derivada.

### Microcontrol 034

[]{#MA-MIC-ANM-01-020-034}

[]{#MA-MSOL-ANM-01-020-034}

**Pregunta.** ¿Dónde quedan los dos centros de Lagrange usados para probar convexidad?

**Solución.** Uno en $(u,v)$ y otro en $(v,w)$; por ello el primero es menor que el segundo y sus derivadas pueden compararse.

Cada aplicación de Lagrange corresponde a una secante corta diferente. El orden de los segmentos fuerza $c<v<d$, aun si los testigos no están predeterminados. Si la derivada no decrece, eso permite comparar sus valores. El orden de secantes resultante recupera convexidad.

### Microcontrol 035

[]{#MA-MIC-ANM-01-020-035}

[]{#MA-MSOL-ANM-01-020-035}

**Pregunta.** ¿Se exige continuidad de $f\prime$ en esa prueba?

**Solución.** No. Se usa el orden de sus valores y Lagrange para $f$, cuya continuidad procede de su derivabilidad.

Derivabilidad de $f$ aporta su continuidad en cada segmento para aplicar Lagrange. La propiedad utilizada de $f\prime$ es sólo su orden entre los dos testigos. No se toma un límite de derivadas ni un máximo de ellas. Separar esas funciones evita imponer regularidad adicional.

### Microcontrol 036

[]{#MA-MIC-ANM-01-020-036}

[]{#MA-MSOL-ANM-01-020-036}

**Pregunta.** ¿Qué cancela los términos de pendiente en la prueba por soporte en $z$?

**Solución.** La identidad $(1-t)(a-z)+t(b-z)=0$ al sumar los dos soportes con los pesos correspondientes.

El centro es precisamente $z=(1-t)a+tb$. Al comparar las dos salidas con su tangente y ponderarlas, los incrementos dirigidos suman cero. Así desaparece la pendiente y queda la desigualdad convexa. Los pesos no negativos conservan el sentido al sumar las comparaciones.

### Microcontrol 037

[]{#MA-MIC-ANM-01-020-037}

[]{#MA-MSOL-ANM-01-020-037}

**Pregunta.** ¿Qué implica $f\prime(x)=f\prime(y)$ para $x<y$ si $f\prime$ no decrece?

**Solución.** Que $f\prime$ es constante entre ambos; C19 aplicado a $f(t)-kt$ hace afín ese tramo.

El orden encierra toda derivada intermedia entre dos valores iguales $k$, forzando igualdad. La función $f(t)-kt$ tiene entonces derivada cero y es constante en el segmento por C19. De ahí la regla afín. Una convexa estricta no puede contener ese tramo no degenerado.

### Microcontrol 038

[]{#MA-MIC-ANM-01-020-038}

[]{#MA-MSOL-ANM-01-020-038}

**Pregunta.** ¿La derivada creciente obliga a que la propia función crezca?

**Solución.** No. Para $x^2$, la derivada $2x$ crece en toda la recta mientras la función decrece a la izquierda de cero.

Ordenar la derivada describe cómo cambian las pendientes entre centros. El signo de esas pendientes determina si las alturas suben o bajan. En el cuadrado las pendientes aumentan pero son negativas a la izquierda y positivas a la derecha. Por eso la convexidad global convive con dos direcciones de monotonía.

### Microcontrol 039

[]{#MA-MIC-ANM-01-020-039}

[]{#MA-MSOL-ANM-01-020-039}

**Pregunta.** ¿Una función estrictamente creciente es necesariamente convexa?

**Solución.** No. El cubo crece estrictamente, pero $3x^2$ decrece en el semieje negativo, así el cubo no es convexo en toda la recta.

La diferencia de cubos es positiva para cualquier par ordenado, acreditando crecimiento de valores. En el lado negativo, sus derivadas disminuyen al acercarse a cero y no satisfacen el criterio convexo. También puede refutarse convexidad con una cuerda explícita. Crecimiento y convexidad son obligaciones distintas.

### Microcontrol 040

[]{#MA-MIC-ANM-01-020-040}

[]{#MA-MSOL-ANM-01-020-040}

**Pregunta.** ¿Qué hipótesis adicional extiende el criterio a los extremos de $[a,b]$?

**Solución.** Continuidad de $f$ incluyendo ambos bordes, además de derivabilidad interior y orden de la derivada.

El criterio abierto controla todas las combinaciones cuyos puntos están en el interior. Para incluir un borde se aproximan sus evaluaciones desde dentro y se pasa al límite de la desigualdad. La continuidad de $f$ allí legitima ese paso. Cambiar un valor de borde sin continuidad puede conservar las derivadas interiores y romper convexidad.

## §20.6 — La segunda derivada y sus límites

### Microcontrol 041

[]{#MA-MIC-ANM-01-020-041}

[]{#MA-MSOL-ANM-01-020-041}

[]{#MA-SEC-ANM-01-020-006}

**Pregunta.** ¿Qué significa que exista $f\prime\prime(c)$?

**Solución.** Que la función derivada está definida alrededor de $c$ y es derivable allí; no basta una derivada aislada de $f$.

La segunda derivada es una derivada de otra función, $f\prime$, con su propio dominio. En el criterio de intervalo se exige que esa primera derivada exista en todos los centros pertinentes. Una derivada puntual aislada de $f$ no aporta una función de pendientes en una vecindad. Debe verificarse ese dominio antes de volver a derivar.

### Microcontrol 042

[]{#MA-MIC-ANM-01-020-042}

[]{#MA-MSOL-ANM-01-020-042}

**Pregunta.** ¿Qué condición caracteriza convexidad cuando $f$ es dos veces derivable en todo un intervalo abierto?

**Solución.** $f\prime\prime(x)\ge0$ en todos sus puntos.

La segunda derivada no negativa hace no decreciente a la primera mediante C19. El criterio de primera derivada produce entonces convexidad. A la inversa, convexidad ordena la primera derivada y cualquier derivada existente de una no decreciente es no negativa. Los dos sentidos conservan la hipótesis en todo el intervalo.

### Microcontrol 043

[]{#MA-MIC-ANM-01-020-043}

[]{#MA-MSOL-ANM-01-020-043}

**Pregunta.** ¿Por qué puede aplicarse C19 a $f\prime$ sin pedir continuidad de $f\prime\prime$?

**Solución.** La existencia de $f\prime\prime$ da derivabilidad y por ello continuidad de $f\prime$ en cada segmento; no pide continuidad de su derivada.

La existencia de la segunda derivada implica que la primera es continua en cada centro. Esa continuidad basta en los bordes de cualquier segmento interior al aplicar valor medio a $f\prime$. La segunda derivada sólo necesita existir con su signo declarado. No se exige continuidad de ella como una tercera premisa.

### Microcontrol 044

[]{#MA-MIC-ANM-01-020-044}

[]{#MA-MSOL-ANM-01-020-044}

**Pregunta.** ¿Es necesaria $f\prime\prime>0$ en todos los puntos para convexidad estricta?

**Solución.** No. $x^4$ es estrictamente convexa y tiene segunda derivada cero en el origen.

La primera derivada del cuarto poder es $4x^3$, estrictamente creciente. Ese orden estricto acredita convexidad estricta aunque $12x^2$ se anule en cero. La positividad de la segunda derivada en todo centro es suficiente para estrictitud, pero este ejemplo muestra que no es necesaria.

### Microcontrol 045

[]{#MA-MIC-ANM-01-020-045}

[]{#MA-MSOL-ANM-01-020-045}

**Pregunta.** ¿Cómo puede $1/x$ ser decreciente y estrictamente convexa en $(0,\infty)$?

**Solución.** Su primera derivada es negativa y su segunda derivada es positiva: controlan propiedades distintas.

La primera derivada $-1/x^2$ es negativa y hace disminuir las alturas. La segunda $2/x^3$ es positiva y hace aumentar las pendientes, produciendo convexidad estricta. Ambas evaluaciones están definidas en el semieje positivo. No hay contradicción porque los signos controlan funciones y comparaciones diferentes.

### Microcontrol 046

[]{#MA-MIC-ANM-01-020-046}

[]{#MA-MSOL-ANM-01-020-046}

**Pregunta.** ¿Qué certifica $f\prime(c)=0$ en una función convexa derivable?

**Solución.** Un mínimo global mediante el soporte horizontal; si la convexidad es estricta, ese mínimo es único.

La tangente de pendiente cero es horizontal y el soporte global da $f(x)\ge f(c)$ para todas las entradas. La existencia del minimizador ya está aportada por el centro estacionario. Si hubiera dos minimizadores distintos en una convexa estricta, su combinación interior tendría menor salida, contradicción. Se concluye unicidad sin imponer existencia de un centro nuevo.

### Microcontrol 047

[]{#MA-MIC-ANM-01-020-047}

[]{#MA-MSOL-ANM-01-020-047}

**Pregunta.** ¿Qué decide por sí solo el valor $f\prime\prime(c)=0$?

**Solución.** No decide extremo, cambio de convexidad ni falta de convexidad estricta; $x^3$ y $x^4$ distinguen esas posibilidades.

Una sola evaluación nula de curvatura no describe el signo en una vecindad. El cubo cambia ese signo al cruzar cero y no tiene extremo allí. El cuarto poder conserva convexidad y tiene mínimo estricto. Los ejemplos separan las conclusiones que no pueden deducirse de esa cifra puntual.

### Microcontrol 048

[]{#MA-MIC-ANM-01-020-048}

[]{#MA-MSOL-ANM-01-020-048}

**Pregunta.** ¿La convexidad estricta garantiza un mínimo alcanzado en un intervalo abierto?

**Solución.** No. $x^2$ sobre $(0,1)$ tiene ínfimo cero sin entrada que lo alcance.

Todas las entradas de $(0,1)$ tienen cuadrado positivo y cualquier una admite otra menor, por ejemplo su mitad. El ínfimo cero queda fuera de la imagen porque la entrada cero falta. Convexidad estricta puede asegurar unicidad si un mínimo existe, pero no proporciona por sí sola un argumento que lo alcance.

## §20.7 — Jensen: combinar sin perder el control

### Microcontrol 049

[]{#MA-MIC-ANM-01-020-049}

[]{#MA-MSOL-ANM-01-020-049}

[]{#MA-SEC-ANM-01-020-007}

**Pregunta.** ¿Qué condiciones tienen los pesos de Jensen finito?

**Solución.** Son no negativos, suman1 y se usan con un número finito no nulo de entradas del intervalo.

La no negatividad permite combinar desigualdades sin invertir su sentido. La suma uno conserva una media de entradas y de salidas. La lista finita no vacía permite la inducción y excluye una suma vacía de pesos que valdría cero. Los pesos nulos no tienen que ser estrictamente positivos.

### Microcontrol 050

[]{#MA-MIC-ANM-01-020-050}

[]{#MA-MSOL-ANM-01-020-050}

**Pregunta.** ¿Qué hacer si la suma $s$ de los primeros pesos es cero?

**Solución.** Todos esos pesos son cero; la combinación sólo tiene la última entrada y hay igualdad, sin normalizar ni dividir.

Una suma finita de no negativos sólo puede ser cero si cada término lo es. Entonces el último peso vale uno y tanto la media como su evaluación se reducen a una entrada. Se verifica igualdad directamente. Dividir por ese grupo nulo introduciría una expresión que no corresponde al caso.

### Microcontrol 051

[]{#MA-MIC-ANM-01-020-051}

[]{#MA-MSOL-ANM-01-020-051}

**Pregunta.** ¿Por qué la media normalizada de un grupo sigue en el dominio?

**Solución.** Sus pesos no negativos suman1 y, por inducción, toda combinación finita de entradas de un intervalo permanece en él.

Al dividir por un peso total positivo, las proporciones resultantes siguen siendo no negativas y suman uno. La inducción de combinaciones de un intervalo garantiza pertenencia de la media al mismo dominio. Esa pertenencia permite aplicar la función en ella. No se asume sólo que el resultado sea un real.

### Microcontrol 052

[]{#MA-MIC-ANM-01-020-052}

[]{#MA-MSOL-ANM-01-020-052}

**Pregunta.** ¿Cuándo hay igualdad en Jensen para una función estrictamente convexa?

**Solución.** Exactamente cuando todas las entradas con peso positivo son iguales; las entradas con peso cero no importan.

Los pesos cero no contribuyen a ninguna de las dos alturas y pueden retirarse. Si dos entradas activas difieren, se agrupa la mínima con las restantes y la estrictitud produce una comparación estricta. Si todas las activas coinciden, la media es esa entrada y hay igualdad. Así la condición ignora correctamente las muestras inactivas.

### Microcontrol 053

[]{#MA-MIC-ANM-01-020-053}

[]{#MA-MSOL-ANM-01-020-053}

**Pregunta.** ¿Qué identidad da la diferencia de Jensen para el cuadrado?

**Solución.** $\sum_i\lambda_i x_i^2-\mu^2=\sum_i\lambda_i(x_i-\mu)^2$, donde $\mu=\sum_i\lambda_i x_i$.

Expandir las desviaciones introduce un término cruzado que se cancela porque la media es $\mu$ y los pesos suman uno. Queda exactamente la diferencia de Jensen del cuadrado. Cada sumando es no negativo y muestra cuantitativamente la dispersión. Un peso positivo con entrada distinta de $\mu$ aporta una contribución estrictamente positiva.

### Microcontrol 054

[]{#MA-MIC-ANM-01-020-054}

[]{#MA-MSOL-ANM-01-020-054}

**Pregunta.** ¿Qué media resulta de pesos $(1/4,1/2,1/4)$ y entradas $(0,1,3)$?

**Solución.** $\mu=5/4$; la media de cuadrados es $11/4$ y la diferencia es $19/16$.

La media usa los valores ponderados $0$, medio y tres cuartos, que suman cinco cuartos. La media de cuadrados usa medio y nueve cuartos, que suman once cuartos. Restar veinticinco dieciseisavos da diecinueve dieciseisavos. La cuenta distingue cuadrar después de combinar de combinar después de cuadrar.

### Microcontrol 055

[]{#MA-MIC-ANM-01-020-055}

[]{#MA-MSOL-ANM-01-020-055}

**Pregunta.** ¿Por qué puede invertirse la media en Jensen para $1/x$?

**Solución.** Todas las entradas son positivas y al menos un peso es positivo, así la media también es positiva.

Al menos un peso es positivo porque todos suman uno. Su entrada positiva aporta una contribución positiva y las demás no son negativas. Por tanto la media está en el dominio positivo del recíproco y puede invertirse. Las multiplicaciones posteriores por esa media o por la suma de entradas conservan el orden.

### Microcontrol 056

[]{#MA-MIC-ANM-01-020-056}

[]{#MA-MSOL-ANM-01-020-056}

**Pregunta.** ¿Basta que los pesos sumen1 si alguno es negativo?

**Solución.** No. Pesos2 y−1 con entradas0 y1 violan Jensen para el cuadrado:1 no es menor o igual que−1.

La combinación de entradas con esos pesos vale menos uno, aunque las dos entradas estén entre cero y uno. El cuadrado de la combinación es uno y la combinación de cuadrados menos uno. Se pierde tanto la interpretación de media dentro del segmento como la conservación de desigualdades al ponderar. Jensen declaraba no negatividad como premisa.

## §20.8 — Bandas cuadráticas y mínimos certificados

### Microcontrol 057

[]{#MA-MIC-ANM-01-020-057}

[]{#MA-MSOL-ANM-01-020-057}

[]{#MA-SEC-ANM-01-020-008}

**Pregunta.** ¿Qué función auxiliar convierte $f\prime\prime\ge m$ en convexidad?

**Solución.** $q_m(x)=f(x)-(m/2)x^2$, cuya segunda derivada es $f\prime\prime-m\ge0$.

Restar el cuadrado ajusta la segunda derivada exactamente por la constante $m$. El criterio diferencial vuelve convexa la auxiliar y su soporte proporciona la cota inferior del resto. La misma operación con $M$ produce una auxiliar cóncava para la cota superior. Así se obtienen bandas mediante orden y soportes.

### Microcontrol 058

[]{#MA-MIC-ANM-01-020-058}

[]{#MA-MSOL-ANM-01-020-058}

**Pregunta.** ¿Qué banda encierra la diferencia respecto de una tangente?

**Solución.** Entre $(m/2)(x-c)^2$ y $(M/2)(x-c)^2$ si $m\le f\prime\prime\le M$ en todo el intervalo.

Las dos constantes controlan todas las segundas derivadas del intervalo. Reorganizar las desigualdades de las auxiliares deja el error respecto de la tangente y un cuadrado de distancia. El centro da igualdad de ambos lados cuando la distancia es cero. No se obtiene la banda sólo de evaluar la segunda derivada en ese centro.

### Microcontrol 059

[]{#MA-MIC-ANM-01-020-059}

[]{#MA-MSOL-ANM-01-020-059}

**Pregunta.** ¿Debe ser $m$ positivo para la banda firmada?

**Solución.** No. Cualquier par real $m\le M$ sirve; si sólo $|f\prime\prime|\le K$, se toman−K yK.

La convexidad de $q_m$ depende de $f\prime\prime-m\ge0$, no del signo propio de $m$. Lo mismo sucede con la concavidad de $q_M$. Si $m=-K$ y $M=K$, las bandas opuestas dan una cota absoluta de resto. Un margen positivo será una condición adicional para los certificados de mínimo.

### Microcontrol 060

[]{#MA-MIC-ANM-01-020-060}

[]{#MA-MSOL-ANM-01-020-060}

**Pregunta.** ¿Qué factor aparece en el error de una cuerda?

**Solución.** $t(1-t)(b-a)^2/2$, multiplicado por $m$ y por $M$ como cotas inferior y superior.

La diferencia de cuadrados ponderados se calcula exactamente como $t(1-t)(b-a)^2$. El ajuste cuadrático de la auxiliar aporta el factor medio. Las dos bandas multiplican ese factor por sus respectivas constantes. En pesos extremos el factor es cero y no se divide por él.

### Microcontrol 061

[]{#MA-MIC-ANM-01-020-061}

[]{#MA-MSOL-ANM-01-020-061}

**Pregunta.** ¿Qué añade $m>0$ al control cualitativo?

**Solución.** Una separación cuadrática positiva entre tangente y función para entradas distintas y, si existe un centro estacionario, unicidad del mínimo.

El término $(m/2)(x-c)^2$ es estrictamente positivo si $x\ne c$. Una tangente horizontal queda entonces estrictamente por debajo de toda otra salida. Esto acredita un mínimo único en ese centro y además cuantifica su separación. La mera estrictitud convexa no ofrece necesariamente una constante común así.

### Microcontrol 062

[]{#MA-MIC-ANM-01-020-062}

[]{#MA-MSOL-ANM-01-020-062}

**Pregunta.** ¿Qué certificado de posición da una pendiente residual?

**Solución.** Si existe $r$ con $f\prime(r)=0$ y $f\prime\prime\ge m>0$, entonces $|x-r|\le|f\prime(x)|/m$.

Se aplica la cota de incrementos de C19 a la primera derivada, cuya derivada es la segunda. El cambio entre $x$ y $r$ tiene magnitud al menos $m|x-r|$, y la salida en $r$ es cero. Dividir por $m>0$ da el certificado de posición. La existencia de ese centro estacionario sigue siendo una premisa.

### Microcontrol 063

[]{#MA-MIC-ANM-01-020-063}

[]{#MA-MSOL-ANM-01-020-063}

**Pregunta.** ¿Qué certificado de pérdida de valor acompaña al de posición?

**Solución.** $0\le f(x)-f(r)\le f\prime(x)^2/(2m)$, demostrado desde la banda inferior y completando un cuadrado.

La banda inferior centrada en $x$ se evalúa en el minimizador $r$ y se reorganiza para acotar la pérdida de valor. El producto lineal con la distancia se domina completando un cuadrado, dando el cociente por $2m$. La no negatividad procede de que $r$ es mínimo. Se distinguen error de posición y diferencia de valores.

### Microcontrol 064

[]{#MA-MIC-ANM-01-020-064}

[]{#MA-MSOL-ANM-01-020-064}

**Pregunta.** ¿La convexidad estricta permite siempre dividir por una constante uniforme $m>0$?

**Solución.** No. Para $x^4$ cerca de cero, $f\prime\prime(0)=0$ y $|f\prime(x)|/|x|=4x^2\to0$; la hipótesis cuantitativa falta.

El cuarto poder es estricto, pero su curvatura vale cero en el origen y se aproxima a cero en centros próximos. No hay barrera positiva común para justificar las divisiones de los certificados. El cociente de pendiente residual por distancia también tiende a cero. Esa tasa cuantitativa es más fuerte que estrictitud cualitativa.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 20](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes.html) · [Ejercicios](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes-microcontroles.html)
