---
content-id: MA-BCH-0305
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-025-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 25
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C25_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 25](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html) · [Ejercicios](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §25.1 — El presupuesto de oscilación

### Microcontrol 001

[]{#MA-MIC-ANM-01-025-001}

[]{#MA-MSOL-ANM-01-025-001}

[]{#MA-SEC-ANM-01-025-001}

**Pregunta.** ¿Qué presupuesto define la brecha?

**Solución.** La brecha es $G(f,P)=\sum_i\omega(f,I_i)\Delta_i$, con $\Delta_i>0$. Cada pieza aporta su amplitud de alturas multiplicada por su anchura. Una oscilación grande puede aportar poco si está confinada en piezas cortas; una amplitud pequeña extendida sobre todo el intervalo también necesita control.

### Microcontrol 002

[]{#MA-MIC-ANM-01-025-002}

[]{#MA-MSOL-ANM-01-025-002}

**Pregunta.** ¿Cómo se define una pieza mala para nivel $\eta>0$?

**Solución.** Para un nivel fijo $\eta>0$, llamamos mala a una pieza con $\omega(f,I_i)\ge\eta$ y buena a una con oscilación menor. El caso de igualdad pertenece al grupo malo. La cantidad $\lambda_P(\eta)$ suma las anchuras de ese grupo y permite estimar su contribución total.

### Microcontrol 003

[]{#MA-MIC-ANM-01-025-003}

[]{#MA-MSOL-ANM-01-025-003}

**Pregunta.** ¿Qué cota inferior usa las piezas malas?

**Solución.** En cada pieza mala, $\omega_i\Delta_i\ge\eta\Delta_i$. Al sumar esos términos y conservar la no negatividad de los demás, queda $G(f,P)\ge\eta\sum_{i\text{ mala}}\Delta_i=\eta\lambda_P(\eta)$. Una brecha pequeña obliga a que la longitud mala sea pequeña para el nivel fijado.

### Microcontrol 004

[]{#MA-MIC-ANM-01-025-004}

[]{#MA-MSOL-ANM-01-025-004}

**Pregunta.** ¿Qué cota superior da $|f|\le B$?

**Solución.** La cota absoluta da $\omega_i\le2B$ en todas las piezas. Las buenas aportan a lo sumo $\eta$ por su longitud total; las malas, a lo sumo $2B\lambda_P(\eta)$. Por tanto $G\le\eta(b-a)+2B\lambda_P(\eta)$. Controlar nivel y longitud mala controla la brecha.

### Microcontrol 005

[]{#MA-MIC-ANM-01-025-005}

[]{#MA-MSOL-ANM-01-025-005}

**Pregunta.** ¿La oscilación puntual exige un radio mínimo?

**Solución.** Ponemos $V_r(x)=[a,b]\cap(x-r,x+r)$ y $\Omega_f(x)=\inf_{r>0}\omega(f,V_r(x))$. Cada vecindad contiene el centro y su imagen es acotada, así las oscilaciones forman un conjunto no vacío de reales no negativos. El ínfimo existe por completitud, aunque ningún radio lo realice exactamente.

### Microcontrol 006

[]{#MA-MIC-ANM-01-025-006}

[]{#MA-MSOL-ANM-01-025-006}

**Pregunta.** ¿Qué equivale a continuidad en un punto?

**Solución.** Si $f$ es continua en $x$, una vecindad con errores de altura menores que $\varepsilon/3$ respecto del centro tiene oscilación a lo sumo $2\varepsilon/3$, forzando $\Omega_f(x)=0$. Recíprocamente, un ínfimo cero proporciona para cada $\varepsilon>0$ una vecindad de oscilación menor que ella. Como contiene el centro, todos sus valores están a distancia menor que $\varepsilon$ de $f(x)$.

### Microcontrol 007

[]{#MA-MIC-ANM-01-025-007}

[]{#MA-MSOL-ANM-01-025-007}

**Pregunta.** ¿Por qué $D_\eta$ es cerrado relativo?

**Solución.** Si $\Omega_f(x)<\eta$, algún $r>0$ tiene $\omega(f,V_r(x))<\eta$. Para $|y-x|<r/2$, la vecindad $V_{r/2}(y)$ está dentro de $V_r(x)$ y su oscilación no supera la de ésta. Luego $\Omega_f(y)<\eta$. El complemento de $D_\eta$ es abierto relativo y el nivel es cerrado relativo.

### Microcontrol 008

[]{#MA-MIC-ANM-01-025-008}

[]{#MA-MSOL-ANM-01-025-008}

**Pregunta.** ¿Qué hace compacto a $D_\eta$?

**Solución.** El intervalo $[a,b]$ es compacto y $D_\eta$ es cerrado en él. La herencia de compacidad de C16 permite reducir cualquier cobertura abierta del nivel a una subcobertura finita. Esto incluye el nivel vacío, que admite la subcobertura vacía.

## §25.2 — Discontinuidades que caben en collares

### Microcontrol 009

[]{#MA-MIC-ANM-01-025-009}

[]{#MA-MSOL-ANM-01-025-009}

[]{#MA-SEC-ANM-01-025-002}

**Pregunta.** ¿Basta un número finito de discontinuidades para integrar?

**Solución.** Una función acotada y continua fuera de un conjunto finito es integrable: cubrimos las entradas excepcionales con collares cortos y controlamos la oscilación en el resto por compacidad. La acotación limita la amplitud dentro de los collares. Sin ella, $1/x$ para $x>0$, completada por cero en $x=0$, falla integrabilidad propia aunque sólo sea discontinua en ese punto.

### Microcontrol 010

[]{#MA-MIC-ANM-01-025-010}

[]{#MA-MSOL-ANM-01-025-010}

**Pregunta.** ¿Qué se controla con los collares?

**Solución.** Dentro de los collares puede persistir una oscilación de hasta $2B$. Su contribución se limita mediante la longitud total de las piezas contenidas allí. Fuera de ellos se fabrica una escala que hace pequeña la oscilación. La brecha resulta de sumar esos dos presupuestos.

### Microcontrol 011

[]{#MA-MIC-ANM-01-025-011}

[]{#MA-MSOL-ANM-01-025-011}

**Pregunta.** ¿Dónde se obtiene la escala común de las piezas buenas?

**Solución.** Para los centros fuera de los collares, la continuidad da vecindades de oscilación menor que el nivel. Para los centros dentro, la apertura da vecindades contenidas en ellos. Las vecindades de radios medios forman una cubierta del cerrado; un subcubrimiento finito permite tomar un mínimo positivo de radios y controlar todas las piezas de una partición fina.

### Microcontrol 012

[]{#MA-MIC-ANM-01-025-012}

[]{#MA-MSOL-ANM-01-025-012}

**Pregunta.** ¿Por qué usar todos los pares centro/radio válidos?

**Solución.** En cada centro existe al menos un radio válido. Tomar el conjunto de todos los pares $(x,r)$ válidos produce directamente una cobertura, sin asignar un radio particular a cada entrada. Compacidad extrae después una lista finita de pares, que basta para construir la escala común.

### Microcontrol 013

[]{#MA-MIC-ANM-01-025-013}

[]{#MA-MSOL-ANM-01-025-013}

**Pregunta.** ¿Qué garantiza malla menor que el mínimo radio medio?

**Solución.** Si una pieza de malla menor que $\delta$ tiene un punto $t$ en una vecindad de radio $r/2$, cualquier punto $s$ de la pieza satisface $|s-c|\le|s-t|+|t-c|<\delta+r/2\le r$. La pieza entera queda en la vecindad grande. Ésta tiene oscilación pequeña o está contenida en los collares.

### Microcontrol 014

[]{#MA-MIC-ANM-01-025-014}

[]{#MA-MSOL-ANM-01-025-014}

**Pregunta.** ¿Qué justifica sumar longitudes dentro de una unión?

**Solución.** Se corta la unión en los extremos de los finitísimos intervalos que la cubren y en los extremos de las piezas. Cada celda de longitud positiva ocupada por una pieza queda en al menos un intervalo de cobertura. Las piezas tienen interiores disjuntos, así su longitud se cuenta una vez y queda acotada por la suma de longitudes de la cobertura.

### Microcontrol 015

[]{#MA-MIC-ANM-01-025-015}

[]{#MA-MSOL-ANM-01-025-015}

**Pregunta.** ¿Qué cota de brecha da el collar del escalón con cortes $c-r,c,c+r$?

**Solución.** Con valor nodal uno, sólo la pieza $[c-r,c]$ tiene alturas cero y uno; su contribución a la brecha es $r$. La pieza $[c,c+r]$ es constante uno. Por tanto la brecha exacta es $r$, aunque la longitud total de las dos piezas que tocan el corte sea $2r$ y dé una cota válida.

### Microcontrol 016

[]{#MA-MIC-ANM-01-025-016}

[]{#MA-MSOL-ANM-01-025-016}

**Pregunta.** ¿El nodo compartido afecta una sola pieza?

**Solución.** El nodo $x_i$ pertenece a las dos piezas cerradas adyacentes. Un valor excepcional puede cambiar sus dos supremos o ínfimos. Las anchuras siguen siendo $x_i-x_{i-1}$ y $x_{i+1}-x_i$; el nodo compartido no añade un término de longitud a la suma.

## §25.3 — La obstrucción densa de Dirichlet

### Microcontrol 017

[]{#MA-MIC-ANM-01-025-017}

[]{#MA-MSOL-ANM-01-025-017}

[]{#MA-SEC-ANM-01-025-003}

**Pregunta.** ¿Qué debe probarse para las cotas de Dirichlet?

**Solución.** La función de Dirichlet vale uno en racionales y cero en irracionales. Para concluir que el ínfimo de cada pieza es cero y el supremo uno, hay que probar que ambos tipos de entradas existen en toda pieza de longitud positiva. Las dos pruebas de densidad proporcionan esos testigos.

### Microcontrol 018

[]{#MA-MIC-ANM-01-025-018}

[]{#MA-MSOL-ANM-01-025-018}

**Pregunta.** ¿Cómo se obtiene un racional entre $u<v$?

**Solución.** Elegimos $n\ge1$ con $n(v-u)>1$. Tras trasladar $nu$ por un natural $M$ para hacerlo no negativo, el mínimo natural $j>nu+M$ cumple $j-1\le nu+M$. El entero $k=j-M$ satisface $nu<k\le nu+1<nv$, y por tanto $u<k/n<v$.

### Microcontrol 019

[]{#MA-MIC-ANM-01-025-019}

[]{#MA-MSOL-ANM-01-025-019}

**Pregunta.** ¿Cómo se obtiene un irracional después de un racional interior?

**Solución.** Sea $r$ un racional interior de $(u,v)$. Arquimedianidad permite elegir $n\ge1$ con $\sqrt2/n<v-r$. Entonces $z=r+\sqrt2/n$ sigue en el intervalo. Si $z$ fuera racional, $n(z-r)=\sqrt2$ también lo sería, contradiciendo su irracionalidad.

### Microcontrol 020

[]{#MA-MIC-ANM-01-025-020}

[]{#MA-MSOL-ANM-01-025-020}

**Pregunta.** ¿Cuál es la suma inferior de Dirichlet?

**Solución.** Cada pieza contiene una entrada irracional de altura cero y todas las alturas son no negativas. Su ínfimo es entonces cero. La suma inferior pondera esos ceros por las anchuras y vale $L(d,P)=0$ para cualquier partición.

### Microcontrol 021

[]{#MA-MIC-ANM-01-025-021}

[]{#MA-MSOL-ANM-01-025-021}

**Pregunta.** ¿Cuál es su suma superior en $[a,b]$?

**Solución.** En cada pieza hay una entrada racional de altura uno y ninguna altura mayor, así el supremo es uno. Por tanto $U(d,P)=\sum_i\Delta_i=b-a$. El valor depende de la longitud del intervalo y no del número de piezas.

### Microcontrol 022

[]{#MA-MIC-ANM-01-025-022}

[]{#MA-MSOL-ANM-01-025-022}

**Pregunta.** ¿Qué nivel puntual de oscilación tiene Dirichlet?

**Solución.** Toda vecindad relativa de radio positivo contiene un segmento de longitud positiva, también en los bordes porque $a<b$. La densidad racional e irracional da ambas alturas cero y uno. Su oscilación es uno para todos los radios, así $\Omega_d(x)=1$ en todo el dominio.

### Microcontrol 023

[]{#MA-MIC-ANM-01-025-023}

[]{#MA-MSOL-ANM-01-025-023}

**Pregunta.** ¿Refinar reduce su brecha?

**Solución.** Cada nueva pieza de un refinamiento mantiene ambas alturas por densidad y tiene oscilación uno. Por ello $G(d,P)=\sum_i\Delta_i=b-a$ para todas las particiones. La brecha fija positiva no puede satisfacer el criterio de Darboux.

### Microcontrol 024

[]{#MA-MIC-ANM-01-025-024}

[]{#MA-MSOL-ANM-01-025-024}

**Pregunta.** ¿Un dibujo de racionales certifica densidad?

**Solución.** Una figura contiene una colección finita de puntos y deja intervalos pequeños sin entradas representadas. Las cotas de Dirichlet requieren testigos en un intervalo arbitrario, por pequeño que sea. Las construcciones aritméticas de racionales e irracionales cubren ese cuantificador; el dibujo sólo ilustra el resultado.

## §25.4 — Thomae: alturas pequeñas y picos finitos

### Microcontrol 025

[]{#MA-MIC-ANM-01-025-025}

[]{#MA-MSOL-ANM-01-025-025}

[]{#MA-SEC-ANM-01-025-004}

**Pregunta.** ¿Qué valor tiene Thomae en una fracción reducida $p/q$?

**Solución.** Para $x=p/q\in[0,1]$ en forma reducida y con $q>0$, se define $T(x)=1/q$. La forma reducida tiene denominador único, así la definición no cambia con otra escritura de la misma fracción. En las entradas irracionales se define $T(x)=0$.

### Microcontrol 026

[]{#MA-MIC-ANM-01-025-026}

[]{#MA-MSOL-ANM-01-025-026}

**Pregunta.** ¿Cuánto vale en cero?

**Solución.** La representación reducida de cero es $0/1$, así $T(0)=1$. Escribir cero como $0/q$ con $q>1$ no cambia ese valor, porque primero se reduce la fracción. De igual forma $T(1)=1$ por la forma $1/1$.

### Microcontrol 027

[]{#MA-MIC-ANM-01-025-027}

[]{#MA-MSOL-ANM-01-025-027}

**Pregunta.** ¿Por qué es finito $E_N$?

**Solución.** Para $1\le q\le N$, una fracción de $[0,1]$ tiene numerador entero $0\le p\le q$, dando a lo sumo $q+1$ candidatos. La suma finita es $\sum_{q=1}^N(q+1)=N(N+3)/2$. Reducir y quitar repeticiones sólo disminuye el número, de modo que $E_N$ es finito.

### Microcontrol 028

[]{#MA-MIC-ANM-01-025-028}

[]{#MA-MSOL-ANM-01-025-028}

**Pregunta.** ¿Qué cota vale fuera de $E_N$?

**Solución.** Una entrada racional fuera de $E_N$ tiene denominador reducido entero $q>N$, luego $q\ge N+1$ y $T(x)=1/q\le1/(N+1)$. En una entrada irracional el valor cero cumple la misma cota. Así el control vale para todas las entradas omitidas.

### Microcontrol 029

[]{#MA-MIC-ANM-01-025-029}

[]{#MA-MSOL-ANM-01-025-029}

**Pregunta.** ¿Por qué es continua en un irracional?

**Solución.** Para un irracional $x$ y $\varepsilon>0$, elegimos $N$ con $1/(N+1)<\varepsilon$. Las distancias de $x$ al conjunto finito $E_N$ tienen mínimo positivo. Un radio menor que ese mínimo evita todos los picos grandes y deja $|T(t)-T(x)|=T(t)\le1/(N+1)<\varepsilon$.

### Microcontrol 030

[]{#MA-MIC-ANM-01-025-030}

[]{#MA-MSOL-ANM-01-025-030}

**Pregunta.** ¿Por qué falla continuidad en un racional?

**Solución.** Si $x=p/q$ está reducido, su altura es $1/q>0$. Cada vecindad relativa contiene un irracional $t$ con altura cero, por lo que $|T(t)-T(x)|=1/q$. Con tolerancia $1/(2q)$ ningún radio cumple continuidad. El argumento cubre también cero y uno relativamente.

### Microcontrol 031

[]{#MA-MIC-ANM-01-025-031}

[]{#MA-MSOL-ANM-01-025-031}

**Pregunta.** ¿Cuál es la oscilación puntual en $p/q$?

**Solución.** Toda vecindad del racional contiene su altura $1/q$ y una altura irracional cero, así oscila al menos $1/q$. Un radio que evite el conjunto finito $E_q\setminus\{x\}$ deja las demás alturas a lo sumo $1/(q+1)$. En esa vecindad el supremo es $1/q$ y el ínfimo cero, así el ínfimo de oscilaciones es exactamente $1/q$.

### Microcontrol 032

[]{#MA-MIC-ANM-01-025-032}

[]{#MA-MSOL-ANM-01-025-032}

**Pregunta.** ¿Qué integral tiene Thomae?

**Solución.** Los irracionales de cada pieza hacen que todas las sumas inferiores de $T$ sean cero. Para controlar las superiores, se cubren los finitísimos picos grandes con piezas de longitud total pequeña y se limita el resto por $1/(N+1)$. Esto da superiores arbitrariamente pequeñas, prueba Darboux y fija integral cero.

## §25.5 — Un criterio exacto por niveles

### Microcontrol 033

[]{#MA-MIC-ANM-01-025-033}

[]{#MA-MSOL-ANM-01-025-033}

[]{#MA-SEC-ANM-01-025-005}

**Pregunta.** ¿Qué significa contenido finito nulo?

**Solución.** Un conjunto $E$ tiene contenido finito nulo si para cada $\sigma>0$ hay una familia finita de intervalos abiertos reales que lo cubre y cuya suma de longitudes es menor que $\sigma$. La familia y su tamaño pueden depender de la tolerancia. El vacío usa la familia vacía.

### Microcontrol 034

[]{#MA-MIC-ANM-01-025-034}

[]{#MA-MSOL-ANM-01-025-034}

**Pregunta.** ¿Se ha definido una medida?

**Solución.** Se ha definido una propiedad de coberturas finitas que permite comparar sumas de anchuras. No se ha construido una función de medida ni probado reglas para uniones numerables. Por eso los argumentos del capítulo mantienen coberturas finitas en cada tolerancia.

### Microcontrol 035

[]{#MA-MIC-ANM-01-025-035}

[]{#MA-MSOL-ANM-01-025-035}

**Pregunta.** ¿Qué caracteriza R5?

**Solución.** Para una función acotada en $[a,b]$, con $a<b$, R5 afirma que la integrabilidad equivale a que $D_\eta=\{x:\Omega_f(x)\ge\eta\}$ tenga contenido finito nulo para cada $\eta>0$. Cada nivel controla discontinuidades de amplitud al menos igual a esa cantidad.

### Microcontrol 036

[]{#MA-MIC-ANM-01-025-036}

[]{#MA-MSOL-ANM-01-025-036}

**Pregunta.** ¿Por qué cubrir también los nodos en la necesidad?

**Solución.** Si un punto del nivel queda en el interior de una pieza buena, una vecindad contenida allí contradice su oscilación puntual grande. En un nodo no hay necesariamente una vecindad que quepa en una sola pieza. Cubrir los finitísimos nodos por intervalos cortos completa la inclusión del nivel en la cobertura.

### Microcontrol 037

[]{#MA-MIC-ANM-01-025-037}

[]{#MA-MSOL-ANM-01-025-037}

**Pregunta.** ¿Qué da $G<\eta\sigma/4$?

**Solución.** La cota $\eta\lambda_P(\eta)\le G$ y $\eta>0$ dan $\lambda_P(\eta)\le G/\eta<\sigma/4$. Éste es el presupuesto de longitud de las piezas malas. Queda margen para abrir sus extremos y añadir pequeños intervalos alrededor de los nodos.

### Microcontrol 038

[]{#MA-MIC-ANM-01-025-038}

[]{#MA-MSOL-ANM-01-025-038}

**Pregunta.** ¿Qué se cubre en la suficiencia?

**Solución.** Se cubre el nivel $D_\eta$ por abiertos de longitud total menor que $\sigma$. Dentro de su unión hay vecindades contenidas en ella; fuera, $\Omega_f(x)<\eta$ proporciona vecindades de oscilación pequeña. Compacidad convierte sus radios medios en una escala común que clasifica todas las piezas finas.

### Microcontrol 039

[]{#MA-MIC-ANM-01-025-039}

[]{#MA-MSOL-ANM-01-025-039}

**Pregunta.** ¿Se exige una cobertura pequeña de todas las discontinuidades juntas?

**Solución.** La cobertura pequeña se exige para cada nivel positivo por separado. En Thomae, cada nivel contiene sólo finitísimos denominadores reducidos, pero la unión de los niveles contiene todos los racionales del intervalo. Esa unión es densa y no tiene contenido finito nulo, aunque la tasa sea integrable.

### Microcontrol 040

[]{#MA-MIC-ANM-01-025-040}

[]{#MA-MSOL-ANM-01-025-040}

**Pregunta.** ¿Qué falla en Dirichlet según R5?

**Solución.** Como $\Omega_d(x)=1$, para $0<\eta\le1$ el nivel es $D_\eta=[a,b]$. Toda cobertura finita por intervalos de ese segmento tiene suma de longitudes al menos $b-a>0$. Por tanto ese nivel no admite coberturas arbitrariamente cortas y falla R5.

## §25.6 — Un soporte infinito de longitud evanescente

### Microcontrol 041

[]{#MA-MIC-ANM-01-025-041}

[]{#MA-MSOL-ANM-01-025-041}

[]{#MA-SEC-ANM-01-025-006}

**Pregunta.** ¿Qué hipótesis usa el lema de soporte?

**Solución.** Se supone un conjunto compacto $E$ de contenido finito nulo y una función $0\le f\le B$ que vale cero fuera de $E$. La compacidad permite controlar a la vez todas las piezas que toquen $E$, y la cobertura corta limita su contribución superior. La conclusión es integrabilidad con valor cero.

### Microcontrol 042

[]{#MA-MIC-ANM-01-025-042}

[]{#MA-MSOL-ANM-01-025-042}

**Pregunta.** ¿Qué controla la malla en ese lema?

**Solución.** Una cobertura abierta pequeña de $E$ admite un subcubrimiento finito de vecindades de radio medio. Si la malla es menor que el mínimo de esos radios, toda pieza que toca $E$ cabe en una vecindad grande dentro de la cobertura. Se incluyen las piezas que sólo tocan el soporte por un extremo.

### Microcontrol 043

[]{#MA-MIC-ANM-01-025-043}

[]{#MA-MSOL-ANM-01-025-043}

**Pregunta.** ¿Cuántas componentes tiene $C_n$?

**Solución.** En $C_0$ hay una componente. Cada paso reemplaza cada segmento por sus dos tercios extremos, separados por un hueco abierto. Así el número se duplica y la etapa $n\ge0$ tiene exactamente $2^n$ componentes cerradas.

### Microcontrol 044

[]{#MA-MIC-ANM-01-025-044}

[]{#MA-MSOL-ANM-01-025-044}

**Pregunta.** ¿Cuál es la anchura de cada componente?

**Solución.** La longitud inicial es uno y cada nueva componente mide un tercio de su padre. Tras $n$ pasos la longitud de cada segmento es $3^{-n}$. Los huecos separan las componentes, por lo que ninguna suma de etapas vuelve a unirlas.

### Microcontrol 045

[]{#MA-MIC-ANM-01-025-045}

[]{#MA-MSOL-ANM-01-025-045}

**Pregunta.** ¿Cuál es la longitud total de una etapa?

**Solución.** La etapa $C_n$ tiene $2^n$ componentes de longitud $3^{-n}$. Sumar sus anchuras da $2^n3^{-n}=(2/3)^n$, que tiende a cero. Es una suma finita de longitudes de la etapa, utilizada para construir coberturas del conjunto final.

### Microcontrol 046

[]{#MA-MIC-ANM-01-025-046}

[]{#MA-MSOL-ANM-01-025-046}

**Pregunta.** ¿Por qué el conjunto final es compacto?

**Solución.** Cada etapa es una unión finita de cerrados y por tanto cerrada. La intersección $C=\bigcap_{n\ge0}C_n$ también es cerrada y está contenida en el compacto $[0,1]$. La herencia de C16 la hace compacta. Los extremos cero y uno sobreviven en todas las etapas, así la intersección es no vacía.

### Microcontrol 047

[]{#MA-MIC-ANM-01-025-047}

[]{#MA-MSOL-ANM-01-025-047}

**Pregunta.** ¿Dónde es discontinua $\mathbf1_C$?

**Solución.** Fuera de $C$, su complemento abierto da una vecindad donde la indicadora vale cero. En $C$, el centro tiene valor uno y toda vecindad contiene alguna entrada del complemento, porque $C$ no contiene intervalos de longitud positiva. El error uno refuta continuidad allí, incluidos los bordes con vecindades relativas.

### Microcontrol 048

[]{#MA-MIC-ANM-01-025-048}

[]{#MA-MSOL-ANM-01-025-048}

**Pregunta.** ¿Qué integral tiene esa indicadora?

**Solución.** El conjunto $C$ es compacto y admite coberturas abiertas finitas de longitud arbitrariamente pequeña. Su indicadora está entre cero y uno y vale cero fuera de $C$. El lema de soporte da sumas superiores arbitrariamente pequeñas y prueba integral cero.

## §25.7 — Cambiar muchos valores y aproximar

### Microcontrol 049

[]{#MA-MIC-ANM-01-025-049}

[]{#MA-MSOL-ANM-01-025-049}

[]{#MA-SEC-ANM-01-025-007}

**Pregunta.** ¿Qué cota global compara oscilaciones de $f$ y $g$?

**Solución.** Si $|f-g|\le\delta$, para dos entradas $s,t$ de $I$ se tiene $f(s)-f(t)\le g(s)-g(t)+2\delta\le\omega(g,I)+2\delta$. Tomar supremo en $s$ e ínfimo en $t$ da $\omega(f,I)\le\omega(g,I)+2\delta$. Los extremos no necesitan alcanzarse.

### Microcontrol 050

[]{#MA-MIC-ANM-01-025-050}

[]{#MA-MSOL-ANM-01-025-050}

**Pregunta.** ¿Qué cota compara sus brechas?

**Solución.** Multiplicamos la comparación local por cada anchura positiva y sumamos: $G(f,P)\le G(g,P)+2\delta\sum_i\Delta_i=G(g,P)+2\delta(b-a)$. La misma cota de error debe valer en todas las entradas del intervalo para justificar cada término.

### Microcontrol 051

[]{#MA-MIC-ANM-01-025-051}

[]{#MA-MSOL-ANM-01-025-051}

**Pregunta.** ¿Cuándo se puede comparar los valores de sus integrales?

**Solución.** Primero se demuestra integrabilidad de $f$ mediante brechas pequeñas de sus aproximantes y la cota de oscilación. Con ambas integrales existentes, linealidad y orden dan $|\int f-\int g|\le\delta(b-a)$. Esa desigualdad compara valores ya definidos.

### Microcontrol 052

[]{#MA-MIC-ANM-01-025-052}

[]{#MA-MSOL-ANM-01-025-052}

**Pregunta.** ¿Qué soporte tiene $T_N$?

**Solución.** Definimos $T_N=T$ en $E_N$ y cero fuera. Como $T$ es positiva en cada racional de $E_N$, ése es exactamente su conjunto de entradas no nulas. Es finito, así $T_N$ es una modificación finita de la función cero y tiene integral cero por C23.

### Microcontrol 053

[]{#MA-MIC-ANM-01-025-053}

[]{#MA-MSOL-ANM-01-025-053}

**Pregunta.** ¿Qué error global aproxima Thomae?

**Solución.** En $E_N$, $T-T_N=0$. Fuera, $T_N=0$ y todas las alturas de $T$ están entre cero y $1/(N+1)$. Así $|T-T_N|\le1/(N+1)$ para todas las entradas. Un único $N$ suficientemente grande controla la familia completa para una tolerancia dada.

### Microcontrol 054

[]{#MA-MIC-ANM-01-025-054}

[]{#MA-MSOL-ANM-01-025-054}

**Pregunta.** ¿Qué límite entrada por entrada tienen $d_N=\mathbf1_{E_N}$?

**Solución.** En un racional reducido de denominador $q$, se tiene $d_N(x)=1$ desde que $N\ge q$. En un irracional, siempre vale cero. Así los valores en cada entrada se estabilizan en Dirichlet, aunque el índice a partir del que ocurre depende de la entrada.

### Microcontrol 055

[]{#MA-MIC-ANM-01-025-055}

[]{#MA-MSOL-ANM-01-025-055}

**Pregunta.** ¿Qué error global conservan esos indicadores?

**Solución.** Para cada $N\ge1$, la fracción reducida $1/(N+1)$ queda fuera de $E_N$. Allí Dirichlet vale uno y $d_N$ vale cero. Como ambas funciones sólo toman cero y uno, su error global máximo es exactamente uno para todo $N$. La estabilización de cada entrada no da control simultáneo.

### Microcontrol 056

[]{#MA-MIC-ANM-01-025-056}

[]{#MA-MSOL-ANM-01-025-056}

**Pregunta.** ¿Cambiar numerablemente muchos valores es la regla de cambios finitos?

**Solución.** Thomae y Dirichlet son dos modificaciones de la tasa cero en todos los racionales. La primera es integrable con valor cero; la segunda no es integrable. Por tanto el resultado de cambios finitos no se extiende automáticamente a un conjunto numerable de entradas modificadas.

## §25.8 — La frontera y el paso que todavía falta

### Microcontrol 057

[]{#MA-MIC-ANM-01-025-057}

[]{#MA-MSOL-ANM-01-025-057}

[]{#MA-SEC-ANM-01-025-008}

**Pregunta.** ¿Cuál es la primera exigencia para Riemann propia?

**Solución.** El contrato propio de Riemann sobre un cerrado no degenerado obliga a que la tasa esté acotada, como probó C23 variando una etiqueta. Sin esa cota no se obtiene un valor real común para todas las sumas suficientemente finas. El criterio de niveles se aplica bajo esta premisa.

### Microcontrol 058

[]{#MA-MIC-ANM-01-025-058}

[]{#MA-MSOL-ANM-01-025-058}

**Pregunta.** ¿El conjunto completo de discontinuidades debe ser de contenido finito nulo?

**Solución.** La integrabilidad sólo exige contenido finito nulo de cada $D_\eta$, para $\eta>0$. Thomae tiene niveles positivos finitos y discontinuidades en todos los racionales. Esa colección completa es densa y no tiene contenido finito nulo, mostrando que la exigencia sobre toda la unión sería más fuerte.

### Microcontrol 059

[]{#MA-MIC-ANM-01-025-059}

[]{#MA-MSOL-ANM-01-025-059}

**Pregunta.** ¿Los racionales de $[0,1]$ tienen contenido finito nulo?

**Solución.** Si una unión finita $O$ de intervalos abiertos cubre $\mathbb Q\cap[0,1]$, su clausura contiene todo el segmento por densidad. Como la unión es finita, su clausura es la unión de los intervalos cerrados correspondientes. Sus longitudes son las mismas y suman al menos uno por la comparación finita de longitudes. Así la cobertura original no puede ser arbitrariamente corta.

### Microcontrol 060

[]{#MA-MIC-ANM-01-025-060}

[]{#MA-MSOL-ANM-01-025-060}

**Pregunta.** ¿Basta continuidad salvo un punto sin acotación?

**Solución.** La función $h(0)=0$, $h(x)=1/x$ para $x>0$, es continua salvo en cero. Para cualquier $B>0$, la entrada $x=1/(B+1)$ tiene altura $B+1>B$. No existe cota global y el contrato propio de Riemann falla. El número de discontinuidades no sustituye la acotación.

### Microcontrol 061

[]{#MA-MIC-ANM-01-025-061}

[]{#MA-MSOL-ANM-01-025-061}

**Pregunta.** ¿Una etapa finita de Cantor es su intersección?

**Solución.** Cada $C_n$ contiene a $C$, pero conserva puntos que serán eliminados más adelante. Por ejemplo $1/(2\cdot3^n)$ está en la componente izquierda de $C_n$ y desaparece en el paso siguiente. La etapa ofrece una envolvente finita para cubrir la intersección.

### Microcontrol 062

[]{#MA-MIC-ANM-01-025-062}

[]{#MA-MSOL-ANM-01-025-062}

**Pregunta.** ¿Una tabla de alturas certifica todos los picos omitidos?

**Solución.** Una tabla sólo registra las alturas evaluadas. En Thomae, la reducción aritmética muestra que cualquier racional omitido de $E_N$ tiene denominador al menos $N+1$. De ahí la cota universal $T\le1/(N+1)$ fuera del conjunto, que protege todos los picos restantes sin muestrearlos.

### Microcontrol 063

[]{#MA-MIC-ANM-01-025-063}

[]{#MA-MSOL-ANM-01-025-063}

**Pregunta.** ¿Se asignó una integral de Lebesgue a Dirichlet?

**Solución.** Dirichlet queda descartada para la integral propia de Riemann por su brecha fija. El capítulo no construye una medida ni una integral de Lebesgue y no le asigna un valor mediante esa teoría. La comparación sólo motiva por qué una teoría más amplia requeriría herramientas nuevas.

### Microcontrol 064

[]{#MA-MIC-ANM-01-025-064}

[]{#MA-MSOL-ANM-01-025-064}

**Pregunta.** ¿Qué puerta sigue después del cierre?

**Solución.** El capítulo siguiente estudia sucesiones de funciones y convergencia punto por punto. El contraste entre truncaciones de Thomae e indicadores de $E_N$ muestra la dificultad que lo motiva: cada entrada puede estabilizarse sin que una sola escala controle simultáneamente todas las entradas.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 25](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html) · [Ejercicios](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann-microcontroles.html)
