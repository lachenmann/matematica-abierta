---
content-id: MA-BCH-0326
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-031
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
title: Capítulo 31 — Completitud, compacidad y conexidad en espacios métricos
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C31.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-31)

C15 y C16 estudiaron conexidad y compacidad en la recta; C30 reconstruyó las herramientas de distancia. Ahora distinguiremos destinos de Cauchy, redes finitas, coberturas y separaciones. Las pruebas indicarán cuándo trabajan sobre una ruta dada y cuándo seleccionan puntos nuevos. Los resultados de dimensión finita se acreditan con las métricas declaradas; no se trasladan por semejanza visual a cualquier espacio.

## 31.1. Dar destino a todas las sucesiones de Cauchy

[]{#MA-SEC-ANM-01-031-001}

Un recorrido puede estabilizarse sin encontrar un punto donde terminar. En C30, $x_n=1/(n+2)$ era Cauchy en $(0,1)$, pero su único posible límite real era $0$, que no pertenecía al espacio. La cuestión global ya no es cuánto se acercan los términos, sino si el espacio contiene todos los destinos exigidos por esas colas.

Un espacio métrico $(X,d)$ es **completo** si toda sucesión de Cauchy $x:\mathbb N\to X$ converge a un punto de $X$. No se exige que toda sucesión converja; en $\mathbb R$, la sucesión $n$ no es Cauchy. El espacio vacío es completo de modo vacuo. Un espacio discreto también es completo: la condición de Cauchy para $\varepsilon=1/2$ obliga a una cola constante, cuyo valor es el destino. Esto no implica que el espacio sea finito.

La recta usual es completa por C10. Para $\mathbb R^m$, con $m\ge1$ finito y $d_\infty(x,y)=\max_i|x_i-y_i|$, una sucesión de Cauchy hace Cauchy cada coordenada. C10 produce sus $m$ límites $a_i$. Para una tolerancia dada tomamos el máximo de los $m$ cortes, y entonces $d_\infty(x_n,a)<\varepsilon$. Sólo se combinan finitamente muchos destinos y cortes. Las constantes $d_\infty\le d_1\le m d_\infty$ dan el mismo resultado para $d_1$ por C30.

**Dónde puede cerrarse un subespacio.** Si $Y\subset X$ es cerrado y $X$ completo, una sucesión Cauchy de $Y$ lo es en $X$, tiene límite $a\in X$ y, por el criterio directo de cerrado de C30, $a\in Y$. Por tanto $Y$ es completo. Para el converso no necesitamos que $X$ sea completo, pero sí producir testigos: si $Y$ es completo y $a\in\operatorname{cl}_X Y$, elegimos $y_n\in Y\cap B(a,1/(n+1))$. Esta elección usa elección numerable para subconjuntos de $Y$, o una familia ya suministrada. La sucesión converge a $a$ en $X$, es Cauchy y tiene límite $b\in Y$; la unicidad en $X$ fuerza $a=b$. Así $Y$ es cerrado bajo esa hipótesis de selección.

**Convención fundacional de este capítulo.** Las pruebas con una sucesión ya dada, las iteraciones de una función dada y las pruebas directas por coberturas no incorporan elección infinita implícita. Para las equivalencias generales que construyen sucesiones o eligen redes a todas las escalas, trabajamos explícitamente en el marco clásico con elección: fijamos selectores para las familias no vacías que aparecen. Esto incluye elección dependiente cuando la siguiente selección depende de las anteriores. No se deduce esta convención de la completitud de $\mathbb R$. Señalaremos cada uso; se pueden leer los resultados correspondientes como condicionales a los selectores descritos. C8 ya declaraba esta base para conjuntos reales; aquí se amplía expresamente a los espacios generales empleados.

**Un espacio de funciones completo.** Sea $T\ne\varnothing$ y $\mathcal B(T)$ el conjunto de funciones reales acotadas con $D_\infty(f,g)=\sup_{t\in T}|f(t)-g(t)|$, métrica construida en C30. Si $(f_n)$ es Cauchy en esta métrica, cada columna $(f_n(t))$ es Cauchy real y tiene un único límite $f(t)$. La unicidad define la función $f$ sin escoger entre varios destinos. Dado $\varepsilon>0$, fijamos $N$ de Cauchy para $\varepsilon/2$. Para $n,k\ge N$, $|f_n(t)-f_k(t)|<\varepsilon/2$ para todo $t$. Al pasar $k$ al límite queda $|f_n(t)-f(t)|\le\varepsilon/2$, y entonces $D_\infty(f_n,f)\le\varepsilon/2<\varepsilon$.

Antes de usar esa métrica debemos acreditar $f\in\mathcal B(T)$. Para $\varepsilon=1$, el argumento anterior da un índice $N$ con $|f(t)-f_N(t)|\le1/2$ para todo $t$. Si $|f_N(t)|\le M$, resulta $|f(t)|\le M+1/2$. La función límite es acotada y la convergencia en supremo está justificada. Sobre un espacio métrico $T$, las funciones acotadas continuas forman un subespacio completo: el límite uniforme es continuo por la prueba de tres errores de C28, que se reconstruye con bolas en el dominio y valor absoluto en el codominio. Concretamente, elegimos una función a distancia menor que $\varepsilon/3$ del límite y usamos su continuidad para el error central. No se exige compacidad de $T$.

![La misma cola recíproca tiene destino cero en [0,1] y carece de destino interno en (0,1). El recinto se declara antes de identificar su límite. Los primeros ocho términos son una muestra; la cota de Cauchy y la unicidad prueban el resultado para toda la cola.](../../assets/books/anm/C31/C31-F01.svg){#fig-anm-c31-f01 fig-alt="La misma cola recíproca tiene destino cero en [0,1] y carece de destino interno en (0,1). El recinto se declara antes de identificar su límite. Los primeros ocho términos son una muestra; la cota de Cauchy y la unicidad prueban el resultado para toda la cola."}

### Microcontroles

#### Microcontrol 1

[]{#MA-MIC-ANM-01-031-001}

¿Qué añade completitud a la condición de Cauchy?

[]{#MA-MSOL-ANM-01-031-001}

<details class="anm-solution">
<summary>Ver solución del microcontrol 1</summary>

**Pregunta.** ¿Qué añade completitud a la condición de Cauchy?

**Respuesta.** Un destino dentro del espacio para toda sucesión que ya cumple Cauchy.

</details>

#### Microcontrol 2

[]{#MA-MIC-ANM-01-031-002}

¿Completitud obliga a converger a toda sucesión?

[]{#MA-MSOL-ANM-01-031-002}

<details class="anm-solution">
<summary>Ver solución del microcontrol 2</summary>

**Pregunta.** ¿Completitud obliga a converger a toda sucesión?

**Respuesta.** No; en $\mathbb R$, $n$ no es Cauchy y no converge.

</details>

#### Microcontrol 3

[]{#MA-MIC-ANM-01-031-003}

¿Por qué la discreta es completa?

[]{#MA-MSOL-ANM-01-031-003}

<details class="anm-solution">
<summary>Ver solución del microcontrol 3</summary>

**Pregunta.** ¿Por qué la discreta es completa?

**Respuesta.** Una cola Cauchy para $1/2$ es constante y tiene destino interno.

</details>

#### Microcontrol 4

[]{#MA-MIC-ANM-01-031-004}

¿Qué ocurre en el espacio vacío?

[]{#MA-MSOL-ANM-01-031-004}

<details class="anm-solution">
<summary>Ver solución del microcontrol 4</summary>

**Pregunta.** ¿Qué ocurre en el espacio vacío?

**Respuesta.** No hay sucesiones hacia él; la condición universal de completitud es vacua.

</details>

#### Microcontrol 5

[]{#MA-MIC-ANM-01-031-005}

¿Qué prueba completitud de un cerrado en un completo?

[]{#MA-MSOL-ANM-01-031-005}

<details class="anm-solution">
<summary>Ver solución del microcontrol 5</summary>

**Pregunta.** ¿Qué prueba completitud de un cerrado en un completo?

**Respuesta.** El destino ambiental de la Cauchy queda en el cerrado por el criterio directo de C30.

</details>

#### Microcontrol 6

[]{#MA-MIC-ANM-01-031-006}

¿Qué selección exige el converso de cerrado?

[]{#MA-MSOL-ANM-01-031-006}

<details class="anm-solution">
<summary>Ver solución del microcontrol 6</summary>

**Pregunta.** ¿Qué selección exige el converso de cerrado?

**Respuesta.** Testigos de $Y\cap B(a,1/(n+1))$; elección numerable o testigos dados.

</details>

#### Microcontrol 7

[]{#MA-MIC-ANM-01-031-007}

¿Por qué el límite de columnas define una función sin elegir destinos?

[]{#MA-MSOL-ANM-01-031-007}

<details class="anm-solution">
<summary>Ver solución del microcontrol 7</summary>

**Pregunta.** ¿Por qué el límite de columnas define una función sin elegir destinos?

**Respuesta.** Cada columna real Cauchy tiene un límite único; la unicidad determina el valor.

</details>

#### Microcontrol 8

[]{#MA-MIC-ANM-01-031-008}

¿Cómo se acredita acotación de la función límite?

[]{#MA-MSOL-ANM-01-031-008}

<details class="anm-solution">
<summary>Ver solución del microcontrol 8</summary>

**Pregunta.** ¿Cómo se acredita acotación de la función límite?

**Respuesta.** Una función $f_N$ acotada y una cota uniforme $|f-f_N|\le1/2$ dan acotación.

</details>

### Ejercicios de la sección 31.1

[]{#ejercicios-31}

#### Ejercicio 1

[]{#MA-EX-ANM-01-031-001}

Prueba que un espacio métrico finito es completo, sin suponer que su métrica sea discreta.

[]{#MA-SOL-ANM-01-031-001}

<details class="anm-solution">
<summary>Ver solución del ejercicio 1</summary>

Si tiene cero o un punto, la afirmación es vacua o inmediata. Si tiene al menos dos, el conjunto finito de distancias positivas entre puntos distintos tiene mínimo $\eta>0$. Para una sucesión de Cauchy tomamos el corte de $\eta/2$. Dos términos de esa cola no pueden ser distintos, pues su distancia sería al menos $\eta$. La cola es constante y converge a su valor interno.

**Volver a la figura.** [C31-F01](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html#fig-anm-c31-f01): confronta el mecanismo de esta solución con las hipótesis y fronteras indicadas en su pie.

</details>

#### Ejercicio 2

[]{#MA-EX-ANM-01-031-002}

Decide si $(0,1]$ con distancia usual es completo, y acredita todos los pasos del contraejemplo.

[]{#MA-SOL-ANM-01-031-002}

<details class="anm-solution">
<summary>Ver solución del ejercicio 2</summary>

$x_n=1/(n+1)$ pertenece al dominio. Para $p,q\ge N$, $|x_p-x_q|\le1/(N+1)$, por lo que es Cauchy. En la recta converge a $0$. Si tuviera límite $a\in(0,1]$, también convergería a $a$ en la recta; unicidad daría $a=0$, contradicción. No es completo.

</details>

#### Ejercicio 3

[]{#MA-EX-ANM-01-031-003}

Sea $X$ completo y $a\in X$. Prueba que la bola cerrada $C(a,r)$, $r\ge0$, es completa.

[]{#MA-SOL-ANM-01-031-003}

<details class="anm-solution">
<summary>Ver solución del ejercicio 3</summary>

La triangular inversa implica que $x\mapsto d(x,a)$ es continua. Más directamente, si $d(x,a)>r$, una bola de radio $(d(x,a)-r)/2$ alrededor de $x$ queda fuera de $C(a,r)$. La bola cerrada es un subespacio cerrado de $X$ y §31.1 lo hace completo. Para $r=0$ es el singleton del centro.

</details>

#### Ejercicio 4

[]{#MA-EX-ANM-01-031-004}

Sea $T\ne\varnothing$ y $(f_n)$ Cauchy en $\mathcal B(T)$. Explica por qué no es legítimo escribir primero $D_\infty(f_n,f)$ sin acreditar que $f$ es acotada, y completa la prueba.

[]{#MA-SOL-ANM-01-031-004}

<details class="anm-solution">
<summary>Ver solución del ejercicio 4</summary>

Los límites reales únicos de cada columna definen $f$. Un corte Cauchy para $1/2$ da $|f(t)-f_N(t)|\le1/2$ al pasar al límite, uniformemente en $t$. Como $|f_N|\le M$, $|f|\le M+1/2$. Ahora $f\in\mathcal B(T)$ y la métrica está tipada. Un corte para $\varepsilon/2$ da $D_\infty(f_n,f)\le\varepsilon/2<\varepsilon$.

</details>

#### Ejercicio 5

[]{#MA-EX-ANM-01-031-005}

Sea $Y$ un subespacio completo de $X$. Demuestra que es cerrado declarando exactamente la selección requerida.

[]{#MA-SOL-ANM-01-031-005}

<details class="anm-solution">
<summary>Ver solución del ejercicio 5</summary>

Para $a\in\operatorname{cl}_XY$, los conjuntos $Y\cap B(a,1/(n+1))$ son no vacíos. Bajo elección numerable para ellos, o con testigos dados, fijamos $y_n$ en cada uno. Entonces $y_n\to a$ en $X$, es Cauchy y converge por completitud a $b\in Y$. Unicidad ambiental da $a=b\in Y$. Así contiene su clausura y es cerrado. La construcción de la ruta no se atribuye a la completitud.

</details>
## 31.2. Encerrar un destino y construirlo por iteración

[]{#MA-SEC-ANM-01-031-002}

La completitud puede reconocerse mirando recintos que se estrechan. Sea $(X,d)$ completo y sea $F_0\supset F_1\supset\cdots$ una familia de conjuntos cerrados no vacíos, de diámetro finito, con $\operatorname{diam}F_n\to0$. El diámetro es $\sup\{d(x,y):x,y\in F_n\}$. Para construir una sucesión fijamos testigos $x_n\in F_n$; éste es un uso de elección numerable, salvo que los testigos formen parte de los datos.

Si $p,q\ge N$, ambos testigos están en $F_N$ y $d(x_p,x_q)\le\operatorname{diam}F_N$. La sucesión es Cauchy, tiene límite $a$, y para cada $N$ su cola vive en el cerrado $F_N$, luego $a\in F_N$. Si $a,b$ pertenecen a todos los recintos, $d(a,b)\le\operatorname{diam}F_N$ para todo $N$, de donde $a=b$. Hay un único punto común. Sin encogimiento la unicidad falla: $F_n=[0,1]$. Sin completitud, $F_n=(0,1/(n+1)]$ son cerrados relativos en $(0,1)$, no vacíos, anidados y de diámetro $1/(n+1)$, pero su intersección es vacía.

**Una función puede suministrar sus propios testigos.** Sea $X\ne\varnothing$ completo y $T:X\to X$ una **contracción**: existe $q\in[0,1)$ con $d(Tx,Ty)\le qd(x,y)$ para todos los pares. Partimos de un $x_0$ dado y definimos $x_{n+1}=Tx_n$. Esta recursión es determinada; no se elige de nuevo en cada paso. Escribamos $C=d(x_1,x_0)$. Por inducción $d(x_{n+1},x_n)\le Cq^n$. Para $p>n$, sumar el bloque finito da
$$d(x_p,x_n)\le C\sum_{j=n}^{p-1}q^j\le\frac{Cq^n}{1-q}.$$
Con la convención $q^0=1$, esto incluye $q=0$: desde $x_1$ la sucesión es constante. Para $0<q<1$, las potencias tienden a cero y la cola es Cauchy. En ambos casos la completitud da un destino $a\in X$.

La desigualdad de contracción implica continuidad: para $q>0$ sirve $\delta=\varepsilon/q$, y para $q=0$ las imágenes tienen distancia cero. Por tanto $Tx_n\to Ta$. Pero $Tx_n=x_{n+1}\to a$, luego $Ta=a$. Si $Tb=b$, entonces $d(a,b)\le qd(a,b)$, y $(1-q)d(a,b)\le0$ obliga a $a=b$. Hemos probado existencia y unicidad de un punto fijo. Al pasar $p$ al límite en el bloque anterior obtenemos el certificado
$$d(x_n,a)\le\frac{Cq^n}{1-q}.$$
También $d(x_n,a)\le d(x_n,x_{n+1})+qd(x_n,a)$, por lo que el error es a lo sumo $d(x_n,x_{n+1})/(1-q)$: se certifica con el salto observado.

En $X=[0,1]$, $T(x)=(x+1)/2$ es una contracción de razón $1/2$. Desde $x_0=0$, $x_n=1-2^{-n}$ y el destino es $1$. La cota anterior es exactamente $2^{-n}$. Para error estrictamente menor que $1/16$ necesitamos $n\ge5$; $n=4$ cae en la frontera. En $(0,1)$ la misma función sigue llevando el espacio a sí mismo y sigue contrayendo, pero su punto fijo $1$ está fuera. La hipótesis de completitud no es un adorno. Tampoco basta $d(Tx,Ty)<d(x,y)$ para cada par distinto: en $[1,\infty)$, $T(x)=x+1/x$ cumple
$$|T(y)-T(x)|=(y-x)\left(1-\frac1{xy}\right)<y-x\quad(1\le x<y),$$
pero no tiene punto fijo. Los cocientes se acercan a $1$ y no hay una razón común menor que $1$.

![La iteración x(n+1)=(x(n)+1)/2 desde cero produce x(n)=1−2^(−n). El destino 1 pertenece al segmento y queda fuera del intervalo abierto. El error exacto coincide con la cota geométrica; para error estrictamente menor que 1/16 el primer corte es 5, no 4.](../../assets/books/anm/C31/C31-F02.svg){#fig-anm-c31-f02 fig-alt="La iteración x(n+1)=(x(n)+1)/2 desde cero produce x(n)=1−2^(−n). El destino 1 pertenece al segmento y queda fuera del intervalo abierto. El error exacto coincide con la cota geométrica; para error estrictamente menor que 1/16 el primer corte es 5, no 4."}

### Microcontroles

#### Microcontrol 9

[]{#MA-MIC-ANM-01-031-009}

¿Qué hipótesis encierra un único punto común?

[]{#MA-MSOL-ANM-01-031-009}

<details class="anm-solution">
<summary>Ver solución del microcontrol 9</summary>

**Pregunta.** ¿Qué hipótesis encierra un único punto común?

**Respuesta.** Recintos cerrados no vacíos anidados, diámetro que tiende a cero y espacio completo, con testigos seleccionados o dados.

</details>

#### Microcontrol 10

[]{#MA-MIC-ANM-01-031-010}

¿Dónde se usa elección en esos recintos?

[]{#MA-MSOL-ANM-01-031-010}

<details class="anm-solution">
<summary>Ver solución del microcontrol 10</summary>

**Pregunta.** ¿Dónde se usa elección en esos recintos?

**Respuesta.** Al fijar un punto en cada recinto de una familia numerable.

</details>

#### Microcontrol 11

[]{#MA-MIC-ANM-01-031-011}

¿Qué define una contracción?

[]{#MA-MSOL-ANM-01-031-011}

<details class="anm-solution">
<summary>Ver solución del microcontrol 11</summary>

**Pregunta.** ¿Qué define una contracción?

**Respuesta.** Una razón común $q<1$, $q\ge0$, que acota la distancia de todas las imágenes.

</details>

#### Microcontrol 12

[]{#MA-MIC-ANM-01-031-012}

¿La iteración de una función dada necesita elección en cada paso?

[]{#MA-MSOL-ANM-01-031-012}

<details class="anm-solution">
<summary>Ver solución del microcontrol 12</summary>

**Pregunta.** ¿La iteración de una función dada necesita elección en cada paso?

**Respuesta.** No; $x_{n+1}=Tx_n$ determina unívocamente cada término desde $x_0$.

</details>

#### Microcontrol 13

[]{#MA-MIC-ANM-01-031-013}

¿Qué controla el bloque desde n hasta p?

[]{#MA-MSOL-ANM-01-031-013}

<details class="anm-solution">
<summary>Ver solución del microcontrol 13</summary>

**Pregunta.** ¿Qué controla el bloque desde n hasta p?

**Respuesta.** La triangular y la suma geométrica: $d(x_p,x_n)\le Cq^n/(1-q)$.

</details>

#### Microcontrol 14

[]{#MA-MIC-ANM-01-031-014}

¿Qué ocurre si q=0?

[]{#MA-MSOL-ANM-01-031-014}

<details class="anm-solution">
<summary>Ver solución del microcontrol 14</summary>

**Pregunta.** ¿Qué ocurre si q=0?

**Respuesta.** Todas las imágenes coinciden; la iteración es constante desde $x_1$, con $q^0=1$.

</details>

#### Microcontrol 15

[]{#MA-MIC-ANM-01-031-015}

¿Qué corte da error menor que 1/16 en la iteración modelo?

[]{#MA-MSOL-ANM-01-031-015}

<details class="anm-solution">
<summary>Ver solución del microcontrol 15</summary>

**Pregunta.** ¿Qué corte da error menor que 1/16 en la iteración modelo?

**Respuesta.** $n\ge5$; en $4$ el error es igual a $1/16$.

</details>

#### Microcontrol 16

[]{#MA-MIC-ANM-01-031-016}

¿Disminuir estrictamente cada distancia da una contracción?

[]{#MA-MSOL-ANM-01-031-016}

<details class="anm-solution">
<summary>Ver solución del microcontrol 16</summary>

**Pregunta.** ¿Disminuir estrictamente cada distancia da una contracción?

**Respuesta.** No; los cocientes pueden acercarse a $1$ sin una razón uniforme menor que $1$.

</details>

### Ejercicios de la sección 31.2

#### Ejercicio 6

[]{#MA-EX-ANM-01-031-006}

En $\mathbb R$ considera $F_n=[1-2^{-n},1+2^{-n}]$, $n\ge0$. Encuentra la intersección y acredita el teorema de recintos.

[]{#MA-SOL-ANM-01-031-006}

<details class="anm-solution">
<summary>Ver solución del ejercicio 6</summary>

Son cerrados, no vacíos, anidados y de diámetro $2^{1-n}\to0$. El punto $1$ pertenece a todos. Si $a$ pertenece a la intersección, $|a-1|\le2^{-n}$ para todo $n$, luego $a=1$. La recta es completa y aquí los testigos pueden darse explícitamente como $x_n=1$.

**Volver a la figura.** [C31-F02](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html#fig-anm-c31-f02): confronta el mecanismo de esta solución con las hipótesis y fronteras indicadas en su pie.

</details>

#### Ejercicio 7

[]{#MA-EX-ANM-01-031-007}

Con $T(x)=(x+1)/2$ en $[0,1]$ y $x_0=0$, calcula la iteración y el primer corte para error estrictamente menor que $1/16$.

[]{#MA-SOL-ANM-01-031-007}

<details class="anm-solution">
<summary>Ver solución del ejercicio 7</summary>

Inducción da $x_n=1-2^{-n}$: vale para $0$ y sustituir en $T$ da el siguiente exponente. El punto fijo es $1$, el error exacto $2^{-n}$. En $n=4$ el error es $1/16$, no menor. Desde $n=5$ es a lo sumo $1/32<1/16$. El primer corte es $5$.

</details>

#### Ejercicio 8

[]{#MA-EX-ANM-01-031-008}

Para una contracción de razón $q\in[0,1)$, prueba la cota a posteriori $d(x_n,a)\le d(x_n,x_{n+1})/(1-q)$.

[]{#MA-SOL-ANM-01-031-008}

<details class="anm-solution">
<summary>Ver solución del ejercicio 8</summary>

Como $Ta=a$, la triangular da $d(x_n,a)\le d(x_n,Tx_n)+d(Tx_n,Ta)\le d(x_n,x_{n+1})+qd(x_n,a)$. Restamos la cantidad real $qd(x_n,a)$ y dividimos por $1-q>0$. Esto requiere un punto fijo ya acreditado, cuya existencia viene de completitud e iteración.

</details>

#### Ejercicio 9

[]{#MA-EX-ANM-01-031-009}

Muestra que la misma contracción $T(x)=(x+1)/2$ en $(0,1)$ no tiene punto fijo, aunque lleve el espacio a sí mismo.

[]{#MA-SOL-ANM-01-031-009}

<details class="anm-solution">
<summary>Ver solución del ejercicio 9</summary>

Para $0<x<1$, $1/2<Tx<1$, de modo que es una autoaplicación; $|Tx-Ty|=|x-y|/2$. La ecuación $x=(x+1)/2$ fuerza $x=1$, exterior. El dominio no es completo, como muestra la sucesión que converge a un extremo omitido. Se pierde exactamente la hipótesis que garantizaba un destino interno.

</details>

#### Ejercicio 10

[]{#MA-EX-ANM-01-031-010}

Verifica que $T(x)=x+1/x$ en $[1,\infty)$ reduce estrictamente las distancias de pares distintos y carece de punto fijo.

[]{#MA-SOL-ANM-01-031-010}

<details class="anm-solution">
<summary>Ver solución del ejercicio 10</summary>

Si $1\le x<y$, $T(y)-T(x)=(y-x)(1-1/(xy))$ es positivo y menor que $y-x$. La ecuación de punto fijo exigiría $1/x=0$, imposible. El dominio es cerrado real y completo. Para $x=n,y=n+1$ los cocientes $1-1/(n(n+1))$ tienden a $1$, así que no existe una razón uniforme $q<1$. La disminución estricta por pares no reemplaza esa razón.

</details>
## 31.3. Cubrir con pocas bolas a cada escala

[]{#MA-SEC-ANM-01-031-003}

Un conjunto puede estar contenido en una sola bola grande y, sin embargo, necesitar infinitas bolas pequeñas para ser cubierto. En un espacio discreto infinito todas las distancias son a lo sumo $1$, pero cada bola de radio $1/2$ es un singleton. La acotación no controla cuántas posiciones diferentes sobreviven a una escala pequeña.

Un espacio $X$ es **totalmente acotado** si para cada $\varepsilon>0$ existen finitos centros $a_1,\ldots,a_r\in X$ tales que $X=\bigcup_{i=1}^rB(a_i,\varepsilon)$. Llamamos a esos centros una red finita de radio $\varepsilon$. Para $X=\varnothing$ se admite $r=0$. La definición exige todas las escalas; una cobertura para un único radio sólo acredita una información parcial.

Si $X\ne\varnothing$ es totalmente acotado, una red de radio $1$ y un centro fijo $a$ dan $d(x,a)<1+\max_i d(a_i,a)$ para cualquier $x$: primero elegimos una bola que contenga ese punto. Esa selección individual es finita y no construye una familia infinita. Así la acotación total implica acotación. La discreta infinita prueba que el converso falla.

**Los subespacios heredan redes, con ajuste del radio.** Si $A\subset X$ y $X$ es totalmente acotado, tomamos una red de radio $\varepsilon/2$ en $X$. Para cada bola que corte $A$ elegimos un punto $b_i$ de esa intersección; son sólo finitas elecciones. Si $x\in A$ está en esa bola, $d(x,b_i)<\varepsilon$. Los $b_i$ son centros de una red de $A$. No podemos dejar centros exteriores al subespacio sin explicar esta conversión. La clausura también es totalmente acotada: una red de $A$ de radio $\varepsilon/2$, junto con un punto de $A$ a distancia menor que $\varepsilon/2$ del punto de clausura considerado, da una cobertura de $\operatorname{cl}A$ de radio $\varepsilon$. El caso $A=\varnothing$ es separado.

**Las coordenadas finitas admiten mallas.** Todo subconjunto acotado de $(\mathbb R^m,d_\infty)$ es totalmente acotado. Encerramos el conjunto en $[-M,M]^m$, elegimos un paso $h<\varepsilon$ y dividimos cada intervalo en finitos tramos de longitud a lo sumo $h$. Hay finitas celdas. De cada celda que corte el conjunto tomamos un representante; dos puntos de esa celda tienen distancia máximo a lo sumo $h<\varepsilon$. Los representantes forman una red. Se usa finitud, no una extracción simultánea de infinitos centros. Por comparación de métricas sirve para $d_1$, ajustando el paso a $h<\varepsilon/m$.

Un subconjunto finito es totalmente acotado a cualquier radio: sus propios puntos son centros. $(0,1)$ también lo es como subconjunto acotado de la recta, pero no es completo. La discreta infinita es completa y acotada, pero no totalmente acotada. Ya aparecen dos obstáculos independientes: faltar destinos y tener demasiados lugares separados a pequeña escala.

**La obstrucción separada.** Si existe $\eta>0$ y una sucesión con $d(x_n,x_k)\ge\eta$ para índices distintos, ninguna bola de radio $\eta/2$ puede contener dos términos. La triangular daría una distancia estrictamente menor que $\eta$. Una red finita es imposible. El argumento vale también para cualquier conjunto infinito de puntos separados, sin enumerarlo previamente: cada bola contiene a lo sumo un punto y una unión finita sólo contiene finitos puntos del conjunto.

![Cinco centros 0,1/4,1/2,3/4,1 cubren [0,1] con bolas relativas de radio 3/20: el peor error es 1/8, menor que el radio. En la discreta infinita cada bola de radio 1/2 sólo contiene un punto. Los seis puntos dibujados representan el patrón, no un espacio finito completo.](../../assets/books/anm/C31/C31-F03.svg){#fig-anm-c31-f03 fig-alt="Cinco centros 0,1/4,1/2,3/4,1 cubren [0,1] con bolas relativas de radio 3/20: el peor error es 1/8, menor que el radio. En la discreta infinita cada bola de radio 1/2 sólo contiene un punto. Los seis puntos dibujados representan el patrón, no un espacio finito completo."}

### Microcontroles

#### Microcontrol 17

[]{#MA-MIC-ANM-01-031-017}

¿Qué exige acotación total?

[]{#MA-MSOL-ANM-01-031-017}

<details class="anm-solution">
<summary>Ver solución del microcontrol 17</summary>

**Pregunta.** ¿Qué exige acotación total?

**Respuesta.** Una red finita con centros internos para cada radio positivo.

</details>

#### Microcontrol 18

[]{#MA-MIC-ANM-01-031-018}

¿Una sola escala basta?

[]{#MA-MSOL-ANM-01-031-018}

<details class="anm-solution">
<summary>Ver solución del microcontrol 18</summary>

**Pregunta.** ¿Una sola escala basta?

**Respuesta.** No; la cuantificación abarca todos los radios positivos.

</details>

#### Microcontrol 19

[]{#MA-MIC-ANM-01-031-019}

¿Acotación total implica acotación?

[]{#MA-MSOL-ANM-01-031-019}

<details class="anm-solution">
<summary>Ver solución del microcontrol 19</summary>

**Pregunta.** ¿Acotación total implica acotación?

**Respuesta.** Sí, una red de radio $1$ y un máximo finito de distancias de centros dan una cota global.

</details>

#### Microcontrol 20

[]{#MA-MIC-ANM-01-031-020}

¿Qué refuta el converso?

[]{#MA-MSOL-ANM-01-031-020}

<details class="anm-solution">
<summary>Ver solución del microcontrol 20</summary>

**Pregunta.** ¿Qué refuta el converso?

**Respuesta.** Un espacio discreto infinito: acotado, pero bolas pequeñas singleton.

</details>

#### Microcontrol 21

[]{#MA-MIC-ANM-01-031-021}

¿Cómo se trasladan centros a un subespacio?

[]{#MA-MSOL-ANM-01-031-021}

<details class="anm-solution">
<summary>Ver solución del microcontrol 21</summary>

**Pregunta.** ¿Cómo se trasladan centros a un subespacio?

**Respuesta.** Con una red ambiental de radio mitad y representantes de las finitas bolas que lo cortan.

</details>

#### Microcontrol 22

[]{#MA-MIC-ANM-01-031-022}

¿Qué estructura hace funcionar las mallas reales?

[]{#MA-MSOL-ANM-01-031-022}

<details class="anm-solution">
<summary>Ver solución del microcontrol 22</summary>

**Pregunta.** ¿Qué estructura hace funcionar las mallas reales?

**Respuesta.** Finitas coordenadas, intervalos de longitud controlada y finitas celdas.

</details>

#### Microcontrol 23

[]{#MA-MIC-ANM-01-031-023}

¿Cuántos puntos separados por eta caben en una bola de radio eta/2?

[]{#MA-MSOL-ANM-01-031-023}

<details class="anm-solution">
<summary>Ver solución del microcontrol 23</summary>

**Pregunta.** ¿Cuántos puntos separados por eta caben en una bola de radio eta/2?

**Respuesta.** A lo sumo uno, por la triangular y la desigualdad estricta de la bola.

</details>

#### Microcontrol 24

[]{#MA-MIC-ANM-01-031-024}

¿Totalmente acotado significa completo?

[]{#MA-MSOL-ANM-01-031-024}

<details class="anm-solution">
<summary>Ver solución del microcontrol 24</summary>

**Pregunta.** ¿Totalmente acotado significa completo?

**Respuesta.** No; $(0,1)$ tiene redes finitas y pierde destinos en sus extremos.

</details>

### Ejercicios de la sección 31.3

#### Ejercicio 11

[]{#MA-EX-ANM-01-031-011}

Construye para $(0,1)$ una red de radio $\varepsilon>0$ con centros interiores.

[]{#MA-SOL-ANM-01-031-011}

<details class="anm-solution">
<summary>Ver solución del ejercicio 11</summary>

Elegimos natural $m$ con $1/(2m)<\varepsilon$. Los centros $a_j=(j+1/2)/m$, $j=0,\ldots,m-1$, son interiores. Cada punto pertenece a una celda de longitud $1/m$ y queda a distancia a lo sumo $1/(2m)<\varepsilon$ de su centro. Son finitos y cubren con bolas abiertas.

**Volver a la figura.** [C31-F03](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html#fig-anm-c31-f03): confronta el mecanismo de esta solución con las hipótesis y fronteras indicadas en su pie.

</details>

#### Ejercicio 12

[]{#MA-EX-ANM-01-031-012}

Prueba que en un espacio discreto la acotación total equivale a finitud.

[]{#MA-SOL-ANM-01-031-012}

<details class="anm-solution">
<summary>Ver solución del ejercicio 12</summary>

Si es finito, sus puntos son centros de una red para cualquier radio. Si es totalmente acotado, una red para $\varepsilon=1/2$ lo cubre por finitos singletons, por lo que es finito. El vacío se incluye con red sin centros.

</details>

#### Ejercicio 13

[]{#MA-EX-ANM-01-031-013}

Sea $A\subset X$ y $X$ totalmente acotado. Justifica una red para $A$ con centros en $A$.

[]{#MA-SOL-ANM-01-031-013}

<details class="anm-solution">
<summary>Ver solución del ejercicio 13</summary>

Tomamos una red ambiental de radio $\varepsilon/2$. Descartamos bolas que no corten $A$ y elegimos un representante $b_i\in A$ en cada una de las restantes; la familia es finita. Para $x\in A$ cubierto por esa bola, $d(x,b_i)<\varepsilon$ por triangular. Los representantes son la red requerida. Si $A$ es vacío basta red vacía.

</details>

#### Ejercicio 14

[]{#MA-EX-ANM-01-031-014}

En $[-1,1]^2$ con $d_\infty$, construye una red de radio $1/3$ usando una malla explícita.

[]{#MA-SOL-ANM-01-031-014}

<details class="anm-solution">
<summary>Ver solución del ejercicio 14</summary>

Dividimos cada coordenada en cuatro intervalos de longitud $1/2$ y usamos sus puntos medios $-3/4,-1/4,1/4,3/4$. Los $16$ pares de puntos medios son centros del cuadrado. Cada punto queda a distancia máximo a lo sumo $1/4<1/3$ de uno. La inclusión de fronteras de las celdas no cambia esa cota.

</details>

#### Ejercicio 15

[]{#MA-EX-ANM-01-031-015}

Prueba que una sucesión con $d(x_n,x_m)\ge\eta>0$ para índices distintos impide acotación total.

[]{#MA-SOL-ANM-01-031-015}

<details class="anm-solution">
<summary>Ver solución del ejercicio 15</summary>

Una bola de radio $\eta/2$ no contiene dos términos, pues la triangular daría distancia menor que $\eta$. Si hubiese una red con $r$ centros, cubriría a lo sumo $r$ términos. Los primeros $r+1$ términos distintos producen contradicción. No basta usar radio $\eta$, porque allí dos puntos podrían compartir una bola.

</details>
## 31.4. Compacidad: reducir cualquier cobertura

[]{#MA-SEC-ANM-01-031-004}

En C16, la compacidad de la recta se formuló mediante coberturas. La definición se transporta sin coordenadas: $K\subset X$ es **compacto** si de toda familia de abiertos de $X$ que cubra $K$ se puede extraer una subfamilia finita que aún lo cubra. Equivalentemente usamos abiertos relativos de $K$, porque cada uno es intersección con un abierto de $X$ y toda cobertura ambiental induce una relativa. La propiedad pertenece al subespacio; no exige que el ambiente entero sea compacto. El vacío y los conjuntos finitos son compactos: basta cero abiertos, o un abierto por cada punto de una lista finita.

**El primer efecto cuantitativo.** Las bolas $B(k,\varepsilon)$, con $k\in K$, cubren $K$ para cada $\varepsilon>0$. La compacidad deja finitos centros de esa misma familia. Por tanto todo compacto métrico es totalmente acotado y, si no vacío, acotado. No se ha escogido una red para todos los radios a la vez; para cada radio se aplica la propiedad.

**Un compacto métrico es cerrado.** Para $a\notin K$ y cada $k\in K$, consideramos $U_k=B(k,d(a,k)/3)$. Una subcobertura finita tiene centros $k_1,\ldots,k_r$. Si $K\ne\varnothing$, $\delta=\min_i d(a,k_i)/3>0$. Ningún $z\in B(a,\delta)$ puede estar en un $U_{k_i}$: eso daría
$$d(a,k_i)\le d(a,z)+d(z,k_i)<\delta+d(a,k_i)/3\le2d(a,k_i)/3.$$
Así $B(a,\delta)$ evita $K$. Si $K$ es vacío, el complemento ya es todo el ambiente. El complemento es abierto y $K$ es cerrado. La separación métrica aporta la positividad que esta prueba necesita.

**La forma dual: intersecciones finitas.** En un compacto $K$, una familia de cerrados relativos con la **propiedad de intersección finita** —cada subfamilia finita tiene intersección no vacía— tiene intersección total no vacía. Si la intersección total fuese vacía, los complementos serían una cobertura abierta; una subcobertura finita contradiría aquella propiedad. El converso se obtiene tomando complementos de una cobertura sin subcobertura finita. Para $K=\varnothing$ no puede existir una familia con esa propiedad si se incluye la subfamilia vacía, cuya intersección es $K$; esta convención elimina una excepción artificial.

**Compacidad da completitud sin construir testigos nuevos.** Sea $(x_n)$ Cauchy en $K$ compacto. Los cerrados relativos $F_N=\operatorname{cl}_K\{x_n:n\ge N\}$ son no vacíos y anidados, por lo que tienen punto común $a$. Para $\varepsilon>0$ fijamos $N$ tal que $d(x_n,x_m)<\varepsilon/2$ para $n,m\ge N$. Para cada $n\ge N$, todos los términos de la cola $N$ están en la bola cerrada $C(x_n,\varepsilon/2)$. Esa bola es cerrada por C30; contiene $F_N$ y por tanto $a$. Luego $d(x_n,a)\le\varepsilon/2<\varepsilon$. La sucesión converge dentro de $K$. Se usó una sucesión ya dada y la propiedad de coberturas, sin seleccionar una sucesión adicional.

Un cerrado relativo de un compacto es compacto: una cobertura de $F$ se completa con $K\setminus F$, y una subcobertura finita de $K$ deja finitos abiertos para $F$. Una unión finita de compactos también es compacta, al unir sus subcoberturas finitas. Una unión infinita puede fallar: los singletons $\{n\}$ son compactos, pero $\mathbb N$ en la recta es no acotado y no compacto. En la discreta infinita, la cobertura por singletons no admite reducción finita, aunque el espacio sea completo y acotado.

![Las coberturas se reducen reteniendo miembros originales. Las dos ventanas (−1,3/4) y (1/4,2) cubren [0,1]. Para los recintos de colas de 1/(n+1), la clausura dentro de [0,1] contiene cero y tiene diámetro 1/(N+1); la anidación y la compacidad suministran el destino interno.](../../assets/books/anm/C31/C31-F04.svg){#fig-anm-c31-f04 fig-alt="Las coberturas se reducen reteniendo miembros originales. Las dos ventanas (−1,3/4) y (1/4,2) cubren [0,1]. Para los recintos de colas de 1/(n+1), la clausura dentro de [0,1] contiene cero y tiene diámetro 1/(N+1); la anidación y la compacidad suministran el destino interno."}

### Microcontroles

#### Microcontrol 25

[]{#MA-MIC-ANM-01-031-025}

¿Qué familia cuantifica la definición de compacto?

[]{#MA-MSOL-ANM-01-031-025}

<details class="anm-solution">
<summary>Ver solución del microcontrol 25</summary>

**Pregunta.** ¿Qué familia cuantifica la definición de compacto?

**Respuesta.** Toda cobertura abierta, de la que se exige una subcobertura finita.

</details>

#### Microcontrol 26

[]{#MA-MIC-ANM-01-031-026}

¿Por qué compacto implica totalmente acotado?

[]{#MA-MSOL-ANM-01-031-026}

<details class="anm-solution">
<summary>Ver solución del microcontrol 26</summary>

**Pregunta.** ¿Por qué compacto implica totalmente acotado?

**Respuesta.** La cobertura por todas las bolas de un radio dado admite finitos centros.

</details>

#### Microcontrol 27

[]{#MA-MIC-ANM-01-031-027}

¿Qué prueba que un compacto métrico es cerrado?

[]{#MA-MSOL-ANM-01-031-027}

<details class="anm-solution">
<summary>Ver solución del microcontrol 27</summary>

**Pregunta.** ¿Qué prueba que un compacto métrico es cerrado?

**Respuesta.** Para un punto exterior, una subcobertura finita de bolas con radios ligados a sus distancias produce una ventana disjunta.

</details>

#### Microcontrol 28

[]{#MA-MIC-ANM-01-031-028}

¿Qué es propiedad de intersección finita?

[]{#MA-MSOL-ANM-01-031-028}

<details class="anm-solution">
<summary>Ver solución del microcontrol 28</summary>

**Pregunta.** ¿Qué es propiedad de intersección finita?

**Respuesta.** Cada subfamilia finita de cerrados tiene intersección no vacía, incluida la subfamilia vacía.

</details>

#### Microcontrol 29

[]{#MA-MIC-ANM-01-031-029}

¿Cómo se pasa de coberturas a intersecciones?

[]{#MA-MSOL-ANM-01-031-029}

<details class="anm-solution">
<summary>Ver solución del microcontrol 29</summary>

**Pregunta.** ¿Cómo se pasa de coberturas a intersecciones?

**Respuesta.** Tomando complementos relativos y usando las leyes de De Morgan.

</details>

#### Microcontrol 30

[]{#MA-MIC-ANM-01-031-030}

¿Por qué las clausuras de colas son no vacías?

[]{#MA-MSOL-ANM-01-031-030}

<details class="anm-solution">
<summary>Ver solución del microcontrol 30</summary>

**Pregunta.** ¿Por qué las clausuras de colas son no vacías?

**Respuesta.** Cada cola contiene términos de la sucesión ya dada.

</details>

#### Microcontrol 31

[]{#MA-MIC-ANM-01-031-031}

¿La prueba directa de compacto implica completo fabrica una nueva ruta?

[]{#MA-MSOL-ANM-01-031-031}

<details class="anm-solution">
<summary>Ver solución del microcontrol 31</summary>

**Pregunta.** ¿La prueba directa de compacto implica completo fabrica una nueva ruta?

**Respuesta.** No; usa cerrados de colas y la propiedad de intersección finita.

</details>

#### Microcontrol 32

[]{#MA-MIC-ANM-01-031-032}

¿Una unión infinita de compactos debe ser compacta?

[]{#MA-MSOL-ANM-01-031-032}

<details class="anm-solution">
<summary>Ver solución del microcontrol 32</summary>

**Pregunta.** ¿Una unión infinita de compactos debe ser compacta?

**Respuesta.** No; la unión de singletons de naturales es no acotada en la recta.

</details>

### Ejercicios de la sección 31.4

#### Ejercicio 16

[]{#MA-EX-ANM-01-031-016}

Prueba que una unión finita de compactos en un espacio métrico es compacta.

[]{#MA-SOL-ANM-01-031-016}

<details class="anm-solution">
<summary>Ver solución del ejercicio 16</summary>

Una cobertura abierta de la unión cubre cada pieza. Para cada una de las finitas piezas tomamos una subcobertura finita. La unión de esas listas es finita y cubre la unión. La familia de elecciones es finita. El caso de cero piezas da el vacío compacto.

**Volver a la figura.** [C31-F04](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html#fig-anm-c31-f04): confronta el mecanismo de esta solución con las hipótesis y fronteras indicadas en su pie.

</details>

#### Ejercicio 17

[]{#MA-EX-ANM-01-031-017}

En la discreta sobre $\mathbb N$, exhibe una cobertura abierta que refute compacidad.

[]{#MA-SOL-ANM-01-031-017}

<details class="anm-solution">
<summary>Ver solución del ejercicio 17</summary>

Los singletons $\{n\}=B(n,1/2)$ son abiertos y cubren $\mathbb N$. Una subfamilia finita cubre sólo finitos naturales, y un natural mayor que todos sus índices queda fuera. La subfamilia vacía tampoco cubre. Es una cobertura concreta sin ninguna reducción finita.

</details>

#### Ejercicio 18

[]{#MA-EX-ANM-01-031-018}

Deduce la propiedad de intersección finita de la compacidad usando complementos.

[]{#MA-SOL-ANM-01-031-018}

<details class="anm-solution">
<summary>Ver solución del ejercicio 18</summary>

Si una familia de cerrados relativos tiene intersección total vacía, sus complementos abiertos cubren el compacto. Una subcobertura finita significa que los cerrados correspondientes tienen intersección vacía, contradiciendo la propiedad. Se incluye como subfamilia finita la vacía, cuya intersección es el espacio; por eso la premisa no se cumple en el espacio vacío.

</details>

#### Ejercicio 19

[]{#MA-EX-ANM-01-031-019}

Prueba directamente que un compacto métrico es completo usando clausuras de colas.

[]{#MA-SOL-ANM-01-031-019}

<details class="anm-solution">
<summary>Ver solución del ejercicio 19</summary>

Para una Cauchy dada, $F_N=\operatorname{cl}\{x_n:n\ge N\}$ son cerrados relativos no vacíos y anidados. Compacidad da $a$ en todos. Un corte Cauchy para $\varepsilon/2$ hace que la cola $N$ esté en cada bola cerrada $C(x_n,\varepsilon/2)$, $n\ge N$. Esa bola contiene $F_N$ por cerradura, luego $d(x_n,a)\le\varepsilon/2<\varepsilon$. Se obtuvo límite interno sin fabricar otra sucesión.

</details>

#### Ejercicio 20

[]{#MA-EX-ANM-01-031-020}

Sea $K\ne\varnothing$ compacto y $a\notin K$. Prueba que $\inf_{k\in K}d(a,k)>0$ sin suponer un mínimo alcanzado.

[]{#MA-SOL-ANM-01-031-020}

<details class="anm-solution">
<summary>Ver solución del ejercicio 20</summary>

La prueba de cerrado en §31.4 produce $\delta>0$ con $B(a,\delta)\cap K=\varnothing$. Por tanto $d(a,k)\ge\delta$ para todos los puntos de $K$. El ínfimo existe por no vacuidad y cota inferior cero, y es al menos $\delta>0$. No se necesita afirmar que algún punto alcance el ínfimo para esta conclusión.

</details>
## 31.5. La equivalencia métrica y sus elecciones

[]{#MA-SEC-ANM-01-031-005}

Tenemos ya una dirección sin selección infinita: compacto implica completo y totalmente acotado. Para volver necesitamos producir recorridos o escoger redes a diferentes escalas. En esta sección rige la convención clásica de selección declarada en §31.1; no escondemos ese paso detrás de una frase como «tomemos puntos».

Un espacio es **secuencialmente compacto** si toda sucesión en él tiene una subsucesión convergente con límite interno. El vacío satisface esta condición de modo vacuo. En un espacio totalmente acotado, fijamos una red finita para cada radio $2^{-j}$, $j=1,2,\ldots$; elegir la lista de redes usa elección numerable de tales listas. Sea $(x_n)$ una sucesión. Entre las bolas de la primera red, alguna captura infinitos índices. Escogemos la primera de una enumeración finita con esa propiedad, y conservamos sus índices. A cada nivel hacemos lo mismo dentro del conjunto infinito anterior, obteniendo conjuntos de índices $I_1\supset I_2\supset\cdots$, cada uno contenido en una bola de radio $2^{-j}$. El desempate finito se hace por menor posición de la lista, no por escoger un punto del espacio.

Elegimos $n_1=\min I_1$ y $n_{j+1}=\min\{n\in I_{j+1}:n>n_j\}$. Existen porque un conjunto infinito de naturales no está acotado. Si $p,q\ge j$, los puntos $x_{n_p},x_{n_q}$ están en la misma bola del nivel $j$, y su distancia es menor que $2^{1-j}$. La subsucesión es Cauchy. Si además el espacio es completo, converge a un punto interno. Hemos probado completo más totalmente acotado implica secuencialmente compacto, haciendo visibles los dos usos distintos: las redes requieren selección; los índices posteriores usan mínimos naturales.

**La secuencia impide una escala rebelde.** Si un espacio secuencialmente compacto no fuese totalmente acotado, existiría $\varepsilon>0$ para el que ninguna colección finita de bolas cubriera. Elegimos $x_0\in X$ y, recursivamente,
$$x_{n+1}\notin\bigcup_{i=0}^nB(x_i,\varepsilon).$$
El complemento es no vacío. Un selector fijo de subconjuntos no vacíos de $X$ determina esta recursión; es elección dependiente explícita. Los puntos quedan a distancia al menos $\varepsilon$ entre sí. Ninguna subsucesión es Cauchy, contradiciendo la convergencia de una subsucesión. Así el espacio es totalmente acotado. También es completo: una sucesión de Cauchy posee una subsucesión convergente y C30 transporta ese destino a toda la sucesión.

**De una cobertura a un radio común.** Sea $X$ secuencialmente compacto y $\mathcal U$ una cobertura abierta. Existe $\lambda>0$ tal que para todo $x\in X$ alguna $U\in\mathcal U$ contiene $B(x,\lambda)$. Si no, para cada $n$ elegimos $x_n$ cuya bola de radio $1/(n+1)$ no esté contenida en ningún miembro. Aquí se usa elección numerable para los puntos infractores. Una subsucesión converge a $a$. Elegimos un $U$ de la cobertura que contenga $a$ y un $r>0$ con $B(a,r)\subset U$. Para un índice de la subsucesión suficientemente grande, tanto $d(x_{n_j},a)<r/2$ como $1/(n_j+1)<r/2$. La triangular implica $B(x_{n_j},1/(n_j+1))\subset B(a,r)\subset U$, contradicción. Esta propiedad es una forma de **lema del número de Lebesgue**.

Como el espacio es totalmente acotado, una red finita de radio $\lambda/2$ cubre $X$. Para cada uno de sus finitos centros $a_i$, escogemos $U_i$ que contenga $B(a_i,\lambda)$; son elecciones finitas. Los $U_i$ cubren $X$. Por tanto secuencialmente compacto implica compacto. Juntando las pruebas, bajo la convención de selección indicada,
$$X\text{ compacto}\quad\Longleftrightarrow\quad X\text{ completo y totalmente acotado}\quad\Longleftrightarrow\quad X\text{ secuencialmente compacto}.$$
La diferencia con la recta queda localizada: allí acotación y acotación total coinciden por las mallas finitas. En un espacio métrico general no coinciden. Reemplazar «totalmente acotado» por «acotado» haría falsa la equivalencia. La extracción tampoco convierte cualquier sucesión original en convergente: en $[0,1]$, una sucesión alternante entre $0$ y $1$ tiene selecciones convergentes y carece de límite global.

![El mapa de prueba señala las direcciones entre compacto, completo más totalmente acotado y secuencialmente compacto. La dirección de coberturas a completitud y redes es directa. Las otras construcciones indican redes elegidas por niveles, selección dependiente o puntos infractores. Todas las equivalencias se leen bajo la convención de selección explícita del capítulo.](../../assets/books/anm/C31/C31-F05.svg){#fig-anm-c31-f05 fig-alt="El mapa de prueba señala las direcciones entre compacto, completo más totalmente acotado y secuencialmente compacto. La dirección de coberturas a completitud y redes es directa. Las otras construcciones indican redes elegidas por niveles, selección dependiente o puntos infractores. Todas las equivalencias se leen bajo la convención de selección explícita del capítulo."}

### Microcontroles

#### Microcontrol 33

[]{#MA-MIC-ANM-01-031-033}

¿Qué añade completitud a una extracción Cauchy?

[]{#MA-MSOL-ANM-01-031-033}

<details class="anm-solution">
<summary>Ver solución del microcontrol 33</summary>

**Pregunta.** ¿Qué añade completitud a una extracción Cauchy?

**Respuesta.** Un destino interno para esa subsucesión.

</details>

#### Microcontrol 34

[]{#MA-MIC-ANM-01-031-034}

¿Qué selección fija redes a todas las escalas?

[]{#MA-MSOL-ANM-01-031-034}

<details class="anm-solution">
<summary>Ver solución del microcontrol 34</summary>

**Pregunta.** ¿Qué selección fija redes a todas las escalas?

**Respuesta.** Elección numerable de listas finitas de centros, declarada en el marco del capítulo.

</details>

#### Microcontrol 35

[]{#MA-MIC-ANM-01-031-035}

¿Qué determina los índices crecientes de extracción?

[]{#MA-MSOL-ANM-01-031-035}

<details class="anm-solution">
<summary>Ver solución del microcontrol 35</summary>

**Pregunta.** ¿Qué determina los índices crecientes de extracción?

**Respuesta.** Mínimos de conjuntos infinitos de naturales después del índice anterior.

</details>

#### Microcontrol 36

[]{#MA-MIC-ANM-01-031-036}

¿Qué distancia máxima da una bola de radio 2 elevado a menos j?

[]{#MA-MSOL-ANM-01-031-036}

<details class="anm-solution">
<summary>Ver solución del microcontrol 36</summary>

**Pregunta.** ¿Qué distancia máxima da una bola de radio 2 elevado a menos j?

**Respuesta.** Dos puntos de ella están a distancia menor que $2^{1-j}$.

</details>

#### Microcontrol 37

[]{#MA-MIC-ANM-01-031-037}

¿Qué gasto tiene fabricar una ruta separada?

[]{#MA-MSOL-ANM-01-031-037}

<details class="anm-solution">
<summary>Ver solución del microcontrol 37</summary>

**Pregunta.** ¿Qué gasto tiene fabricar una ruta separada?

**Respuesta.** Elección dependiente de puntos exteriores a las bolas elegidas previamente, o un selector dado.

</details>

#### Microcontrol 38

[]{#MA-MIC-ANM-01-031-038}

¿Qué certifica el número de Lebesgue usado aquí?

[]{#MA-MSOL-ANM-01-031-038}

<details class="anm-solution">
<summary>Ver solución del microcontrol 38</summary>

**Pregunta.** ¿Qué certifica el número de Lebesgue usado aquí?

**Respuesta.** Cada bola de un radio común queda en algún miembro de la cobertura.

</details>

#### Microcontrol 39

[]{#MA-MIC-ANM-01-031-039}

¿Por qué no falla ese radio en un secuencialmente compacto?

[]{#MA-MSOL-ANM-01-031-039}

<details class="anm-solution">
<summary>Ver solución del microcontrol 39</summary>

**Pregunta.** ¿Por qué no falla ese radio en un secuencialmente compacto?

**Respuesta.** Puntos infractores seleccionados tendrían una subsucesión convergente que acabaría dentro de una ventana de la cobertura.

</details>

#### Microcontrol 40

[]{#MA-MIC-ANM-01-031-040}

¿Cuál es la equivalencia métrica bajo la selección declarada?

[]{#MA-MSOL-ANM-01-031-040}

<details class="anm-solution">
<summary>Ver solución del microcontrol 40</summary>

**Pregunta.** ¿Cuál es la equivalencia métrica bajo la selección declarada?

**Respuesta.** Compacto, completo y totalmente acotado, y secuencialmente compacto son equivalentes.

</details>

### Ejercicios de la sección 31.5

#### Ejercicio 21

[]{#MA-EX-ANM-01-031-021}

Explica por qué una extracción en redes de radios $2^{-j}$ produce una subsucesión de Cauchy y qué selecciones emplea.

[]{#MA-SOL-ANM-01-031-021}

<details class="anm-solution">
<summary>Ver solución del ejercicio 21</summary>

Se fijan redes finitas para todos los niveles; eso usa elección numerable de listas de centros. En cada lista enumerada se toma la primera bola que contiene infinitos índices de la etapa anterior. Los índices crecientes se toman por mínimos naturales. Para $p,q\ge j$, ambos términos elegidos están en la misma bola de radio $2^{-j}$ y su distancia es menor que $2^{1-j}\to0$. La completitud, si se tiene, da el destino.

**Volver a la figura.** [C31-F05](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html#fig-anm-c31-f05): confronta el mecanismo de esta solución con las hipótesis y fronteras indicadas en su pie.

</details>

#### Ejercicio 22

[]{#MA-EX-ANM-01-031-022}

Supón que ninguna red finita de radio $\varepsilon$ cubre $X$. Construye una sucesión separada, declarando la regla de selección.

[]{#MA-SOL-ANM-01-031-022}

<details class="anm-solution">
<summary>Ver solución del ejercicio 22</summary>

Fijamos un selector de subconjuntos no vacíos de $X$. Elegimos $x_0$ y aplicamos el selector al complemento de las bolas centradas en $x_0,\ldots,x_n$ para obtener $x_{n+1}$. Cada complemento es no vacío por la hipótesis. Por construcción $d(x_n,x_m)\ge\varepsilon$ si $n\ne m$. Éste es un uso explícito de elección dependiente, no una consecuencia de completitud.

</details>

#### Ejercicio 23

[]{#MA-EX-ANM-01-031-023}

Prueba que un espacio secuencialmente compacto es completo sin fabricar otra sucesión.

[]{#MA-SOL-ANM-01-031-023}

<details class="anm-solution">
<summary>Ver solución del ejercicio 23</summary>

Una sucesión Cauchy ya dada tiene una subsucesión que converge internamente por compacidad secuencial. Para $\varepsilon>0$ tomamos un corte Cauchy de $\varepsilon/2$ y un término de esa subsucesión posterior al corte y a distancia menor que $\varepsilon/2$ del destino. La triangular muestra que toda la cola original está a distancia menor que $\varepsilon$. C30 ya acreditó este mecanismo.

</details>

#### Ejercicio 24

[]{#MA-EX-ANM-01-031-024}

Para la cobertura de $[0,1]$ por $U=(-1,3/4)$ y $V=(1/4,2)$, verifica un número de Lebesgue en forma de bolas relativas.

[]{#MA-SOL-ANM-01-031-024}

<details class="anm-solution">
<summary>Ver solución del ejercicio 24</summary>

Sirve $\lambda=1/4$. Si $x\le1/2$, la bola relativa $B(x,1/4)\cap[0,1]$ tiene todos sus puntos menores que $3/4$ y queda en $U$. Si $x>1/2$, todos sus puntos son mayores que $1/4$ y queda en $V$. Las desigualdades estrictas de la bola resuelven el centro $1/2$. No se afirma que sea el mayor radio posible.

</details>

#### Ejercicio 25

[]{#MA-EX-ANM-01-031-025}

En un compacto, ¿toda sucesión converge? Da una refutación y dos subsucesiones.

[]{#MA-SOL-ANM-01-031-025}

<details class="anm-solution">
<summary>Ver solución del ejercicio 25</summary>

En $[0,1]$, $x_n=0$ para $n$ par y $1$ para $n$ impar. La selección par converge a $0$ y la impar a $1$. Si la sucesión completa convergiera, ambas compartirían su límite, contradiciendo unicidad. Compacidad secuencial garantiza alguna extracción convergente, no un destino para toda la sucesión.

</details>
## 31.6. Transportar compacidad por continuidad

[]{#MA-SEC-ANM-01-031-006}

La compacidad permite transformar ventanas locales en un control de todo el dominio. Primero probemos que una función continua $f:K\to Y$ lleva un compacto a un compacto. Si abiertos de $Y$ cubren $f(K)$, sus preimágenes son abiertos relativos de $K$ por C30 y cubren $K$. Una subcobertura finita de preimágenes da una subcobertura finita de la imagen. No se requieren inyectividad, sobreyectividad sobre $Y$ ni elección de puntos de fibras.

Para $f:K\to\mathbb R$ continua y $K\ne\varnothing$ compacto, $f(K)$ es no vacío, compacto, cerrado y acotado. Su supremo $s$ existe por C3. Toda bola real de radio $\varepsilon>0$ alrededor de $s$ corta $f(K)$, porque $s-\varepsilon$ no es cota superior. Así $s\in\operatorname{cl}f(K)=f(K)$. Hay un $a\in K$ con $f(a)=s$. El ínfimo se trata del mismo modo. La selección de un punto que alcanza cada extremo es una existencia aislada, no una familia infinita. Se recupera el teorema de extremos de C16 para una función real sobre cualquier compacto métrico. Para codominio métrico arbitrario podemos concluir imagen compacta y acotada, pero «máximo» requiere orden adicional.

**Continuidad uniforme desde coberturas.** Sea $f:K\to Y$ continua y $\varepsilon>0$. Para cada $a\in K$ existe un radio $r>0$ tal que $d(x,a)<r$ implica $\rho(f(x),f(a))<\varepsilon/2$. Para evitar elegir un radio simultáneamente para cada punto, consideramos la familia de **todos** los pares admisibles $(a,r)$. Las bolas $B(a,r/2)$ de esa familia cubren $K$. La compacidad deja finitos pares $(a_i,r_i)$, y $\delta=\min_i r_i/2>0$ si $K$ no es vacío. Si $x,y\in K$ y $d(x,y)<\delta$, una de las bolas reducidas contiene $x$. Entonces
$$d(y,a_i)\le d(y,x)+d(x,a_i)<\delta+r_i/2\le r_i.$$
Ambas imágenes están a distancia menor que $\varepsilon/2$ de $f(a_i)$, luego $\rho(f(x),f(y))<\varepsilon$. La prueba es directa y no usa elección infinita. En el dominio vacío la afirmación es vacua. Así toda función continua desde un compacto métrico es uniformemente continua.

Si $f$ es una biyección continua de un compacto $K$ a un espacio métrico $Y$, su inversa es continua. Para un cerrado $F\subset K$, $F$ es compacto, $f(F)$ es compacto y por tanto cerrado en $Y$. Es precisamente la preimagen de $F$ por $f^{-1}$; el criterio por cerrados de C30 prueba la continuidad. La compacidad corrige el fallo de la biyección continua de la discreta a la recta usual estudiado en C30.

**Heine–Borel en dimensión finita, con la métrica declarada.** Un subconjunto $K\subset(\mathbb R^m,d_\infty)$ es compacto si y sólo si es cerrado y acotado. El sentido directo ya está demostrado. En el otro, la recta completa por coordenadas hace completo $\mathbb R^m$; cerrado hace completo el subespacio; acotado produce mallas finitas de §31.3; §31.5 da compacidad, bajo su convención de selección. Para $d_1$ las constantes de comparación conservan todas estas propiedades. No se importa una norma euclídea sin definirla.

No basta que un espacio completo y acotado sea el dominio de una función continua para obtener uniformidad. Sobre $\mathbb N$ con $d(n,m)=|1/(n+1)-1/(m+1)|$ podemos tener pérdidas de destino, así que no usamos ese ejemplo para el requisito de completo. Un contraejemplo que sí lo satisface será construido en §31.8 mediante una métrica truncada sobre $\mathbb R$: la función $x\mapsto x^2$ es continua y no uniformemente continua. La compacidad es una hipótesis global precisa, no un sinónimo de «no irse demasiado lejos».

![Para f(t)=t² en [0,1], la imagen es [0,1] y contiene ambos extremos. Las bolas relativas de centros 0,1/4,1/2,3/4,1 y radio reducido 3/20 cubren el dominio. Los radios completos 3/10 controlan error de imagen menor que 3/5; con tolerancia 6/5, el mínimo de radios reducidos ofrece un control global de entrada.](../../assets/books/anm/C31/C31-F06.svg){#fig-anm-c31-f06 fig-alt="Para f(t)=t² en [0,1], la imagen es [0,1] y contiene ambos extremos. Las bolas relativas de centros 0,1/4,1/2,3/4,1 y radio reducido 3/20 cubren el dominio. Los radios completos 3/10 controlan error de imagen menor que 3/5; con tolerancia 6/5, el mínimo de radios reducidos ofrece un control global de entrada."}

### Microcontroles

#### Microcontrol 41

[]{#MA-MIC-ANM-01-031-041}

¿Cómo se transporta una cobertura de la imagen?

[]{#MA-MSOL-ANM-01-031-041}

<details class="anm-solution">
<summary>Ver solución del microcontrol 41</summary>

**Pregunta.** ¿Cómo se transporta una cobertura de la imagen?

**Respuesta.** Por preimágenes abiertas del dominio.

</details>

#### Microcontrol 42

[]{#MA-MIC-ANM-01-031-042}

¿La imagen compacta requiere inyectividad?

[]{#MA-MSOL-ANM-01-031-042}

<details class="anm-solution">
<summary>Ver solución del microcontrol 42</summary>

**Pregunta.** ¿La imagen compacta requiere inyectividad?

**Respuesta.** No; continuidad es suficiente.

</details>

#### Microcontrol 43

[]{#MA-MIC-ANM-01-031-043}

¿Por qué el supremo de la imagen real se alcanza?

[]{#MA-MSOL-ANM-01-031-043}

<details class="anm-solution">
<summary>Ver solución del microcontrol 43</summary>

**Pregunta.** ¿Por qué el supremo de la imagen real se alcanza?

**Respuesta.** Es adherente y la imagen compacta es cerrada.

</details>

#### Microcontrol 44

[]{#MA-MIC-ANM-01-031-044}

¿Qué sucede si el compacto es vacío en el teorema de extremos?

[]{#MA-MSOL-ANM-01-031-044}

<details class="anm-solution">
<summary>Ver solución del microcontrol 44</summary>

**Pregunta.** ¿Qué sucede si el compacto es vacío en el teorema de extremos?

**Respuesta.** No hay valores ni extremos; se requiere dominio no vacío.

</details>

#### Microcontrol 45

[]{#MA-MIC-ANM-01-031-045}

¿Qué familia evita elegir infinitos radios de continuidad?

[]{#MA-MSOL-ANM-01-031-045}

<details class="anm-solution">
<summary>Ver solución del microcontrol 45</summary>

**Pregunta.** ¿Qué familia evita elegir infinitos radios de continuidad?

**Respuesta.** Todas las parejas admisibles de centro y radio; compacidad retiene finitas.

</details>

#### Microcontrol 46

[]{#MA-MIC-ANM-01-031-046}

¿Qué hace continuo al inverso de una biyección desde un compacto?

[]{#MA-MSOL-ANM-01-031-046}

<details class="anm-solution">
<summary>Ver solución del microcontrol 46</summary>

**Pregunta.** ¿Qué hace continuo al inverso de una biyección desde un compacto?

**Respuesta.** La imagen de cada cerrado es compacta y cerrada en el codominio métrico.

</details>

#### Microcontrol 47

[]{#MA-MIC-ANM-01-031-047}

¿En qué ámbito cerrado y acotado implica compacto aquí?

[]{#MA-MSOL-ANM-01-031-047}

<details class="anm-solution">
<summary>Ver solución del microcontrol 47</summary>

**Pregunta.** ¿En qué ámbito cerrado y acotado implica compacto aquí?

**Respuesta.** En $\mathbb R^m$ con las métricas finitas declaradas; no en cualquier espacio métrico.

</details>

#### Microcontrol 48

[]{#MA-MIC-ANM-01-031-048}

¿Completitud y acotación bastan para continuidad uniforme?

[]{#MA-MSOL-ANM-01-031-048}

<details class="anm-solution">
<summary>Ver solución del microcontrol 48</summary>

**Pregunta.** ¿Completitud y acotación bastan para continuidad uniforme?

**Respuesta.** No; la recta con métrica truncada y $x^2$ da un contraejemplo.

</details>

### Ejercicios de la sección 31.6

#### Ejercicio 26

[]{#MA-EX-ANM-01-031-026}

Sea $f:K\to Y$ continua y $K$ compacto. Prueba compacidad de $f(K)$ conservando los índices de una cobertura.

[]{#MA-SOL-ANM-01-031-026}

<details class="anm-solution">
<summary>Ver solución del ejercicio 26</summary>

Dada una cobertura $(U_i)_{i\in I}$ de $f(K)$, las preimágenes $f^{-1}(U_i)$ son abiertos relativos y cubren $K$. Compacidad entrega un conjunto finito $J\subset I$. Para $y\in f(K)$ existe $x\in K$ con $f(x)=y$, y algún $j\in J$ contiene ese $x$ en la preimagen. Así $y\in U_j$. Los mismos índices finitos cubren la imagen; no se eligió una función inversa de fibras.

**Volver a la figura.** [C31-F06](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html#fig-anm-c31-f06): confronta el mecanismo de esta solución con las hipótesis y fronteras indicadas en su pie.

</details>

#### Ejercicio 27

[]{#MA-EX-ANM-01-031-027}

Una función continua $f:K\to\mathbb R$ sobre un compacto no vacío alcanza supremo. Prueba el paso de supremo a valor alcanzado.

[]{#MA-SOL-ANM-01-031-027}

<details class="anm-solution">
<summary>Ver solución del ejercicio 27</summary>

La imagen es compacta, luego cerrada y acotada. Su supremo $s$ existe. Para cada $\varepsilon>0$ hay un valor mayor que $s-\varepsilon$, pues ese número no es cota superior, y dicho valor es a lo sumo $s$. Cada bola alrededor de $s$ corta la imagen, de modo que $s$ es adherente. Cerradura lo pone en la imagen y proporciona una preimagen donde se alcanza. No se construye una sucesión de casi máximos.

</details>

#### Ejercicio 28

[]{#MA-EX-ANM-01-031-028}

Reconstruye la continuidad uniforme de una continua sobre un compacto sin elegir una función de radios sobre todos los puntos.

[]{#MA-SOL-ANM-01-031-028}

<details class="anm-solution">
<summary>Ver solución del ejercicio 28</summary>

Para una tolerancia $\varepsilon$ tomamos todas las parejas $(a,r)$ que controlan a menos de $\varepsilon/2$ el error desde $a$ en su bola. Las bolas de radio $r/2$ cubren. Una subcobertura finita da $\delta=\min r_i/2>0$. Si $x$ está en la bola reducida y $d(x,y)<\delta$, ambos están en la bola completa. La triangular en las imágenes da error menor que $\varepsilon$. Sólo se retienen finitos radios; el dominio vacío es vacuo.

</details>

#### Ejercicio 29

[]{#MA-EX-ANM-01-031-029}

Sea $f:K\to Y$ una biyección continua, $K$ compacto y $Y$ métrico. Prueba continuidad de su inversa.

[]{#MA-SOL-ANM-01-031-029}

<details class="anm-solution">
<summary>Ver solución del ejercicio 29</summary>

Si $F$ es cerrado en $K$, es compacto. Su imagen $f(F)$ es compacta y por tanto cerrada en $Y$. Esa imagen es $(f^{-1})^{-1}(F)$. El criterio de continuidad por preimágenes de cerrados prueba la continuidad de la inversa. La biyección acredita que la inversa es una función con esos tipos.

</details>

#### Ejercicio 30

[]{#MA-EX-ANM-01-031-030}

Clasifica $K=\{(x,y):\max(|x|,|y|)\le1\}$ en $\mathbb R^2$ con $d_\infty$: completitud, compacidad y conexidad por caminos.

[]{#MA-SOL-ANM-01-031-030}

<details class="anm-solution">
<summary>Ver solución del ejercicio 30</summary>

Es la bola cerrada de radio $1$ en un espacio completo por coordenadas, luego completa. Es acotada y tiene redes finitas por mallas, así que es compacta bajo §31.5. Para dos puntos del cuadrado, el segmento coordenado permanece en él por la desigualdad $|(1-t)x_i+ty_i|\le(1-t)|x_i|+t|y_i|\le1$. El camino es Lipschitz con constante $d_\infty(a,b)$, luego continuo. Es conexa por caminos y conexa.

</details>
## 31.7. Conexidad: impedir una separación

[]{#MA-SEC-ANM-01-031-007}

Completitud se ocupa de colas; compacidad, de coberturas. La tercera pregunta es si el espacio puede dividirse en dos regiones abiertas que no se toquen. Una **separación** de $X$ es una pareja de abiertos relativos no vacíos $U,V$ con $X=U\cup V$ y $U\cap V=\varnothing$. El espacio es **conexo** si no admite una separación. El vacío y los singletons son conexos. Un espacio discreto con al menos dos puntos no lo es: un singleton y su complemento dan una separación.

La definición equivale a no tener subconjuntos abiertos y cerrados a la vez salvo $\varnothing$ y $X$. En una separación cada abierto es complemento del otro y por tanto cerrado. Recíprocamente, un conjunto abierto y cerrado propio y no vacío forma una separación con su complemento. Hay una segunda lectura útil: $X$ es conexo si y sólo si toda función continua a $\{0,1\}$ con métrica discreta es constante. Una función no constante produce por preimagen la separación de los dos singletons. Una separación produce la función que vale $0$ en una parte y $1$ en la otra; las cuatro posibles preimágenes de abiertos del codominio son abiertas. Es un certificado binario de desconexión.

**Una imagen continua conserva conexidad.** Si $f(X)$ tuviera una separación relativa, sus preimágenes serían abiertos disjuntos que cubren $X$ y son no vacíos porque cada parte contiene una imagen. Contradice la conexidad. La continuidad no obliga a la imagen a ser abierta, pero sí transporta la imposibilidad de separar. Ninguna sucesión ni selector infinito interviene en esta prueba.

**En la recta usual, conexo significa intervalo.** Si $A$ es conexo y contiene $a<b$, pero no contiene algún $c\in(a,b)$, entonces $A\cap(-\infty,c)$ y $A\cap(c,\infty)$ son una separación. Por tanto contiene todos los puntos intermedios. Para probar el converso, sea $I$ un intervalo y supongamos una separación $U,V$. Tomamos $u\in U$, $v\in V$; intercambiando nombres si hace falta, $u<v$. El segmento $[u,v]$ pertenece a $I$. El conjunto $S=U\cap[u,v]$ es no vacío y acotado, de modo que tiene supremo $s\in[u,v]$.

Como $V$ es abierto relativo y contiene $v$, una ventana a la izquierda de $v$ evita $U$, así que $s<v$. Si $s\in U$, una ventana relativa en $s$ permite un punto de $U\cap[u,v]$ estrictamente mayor que $s$, contradiciendo que es cota. Si $s\in V$, entonces $s\ne u$ y una ventana a la izquierda de $s$ en $I$ evita $U$. Pero por el supremo hay puntos de $S$ mayores que $s-\eta$ para todo $\eta>0$; eligiendo $\eta$ menor que aquella ventana y que $s-u$ obtenemos contradicción. Como $s\in I=U\cup V$, no queda alternativa. El intervalo es conexo. El orden y el supremo se usan aquí sobre la recta; no se declaran disponibles en cualquier espacio.

La clausura de un conexo $A$ es conexa. Si su clausura se separara en $U,V$, la restricción a $A$ obliga a que $A$ esté íntegramente en una parte, digamos $U$. Un punto de la otra parte $V$, abierta relativa y no vacía, tiene una bola ambiental cuya intersección con la clausura está en $V$; por adherencia esa bola corta $A$, contradicción. Si $A$ es vacío, su clausura también lo es. Asimismo una unión de conjuntos conexos que comparten un punto es conexa: en una supuesta separación, cada conjunto debe estar en una sola parte, y el punto común obliga a que todos estén en la misma.

Un **camino** de $a$ a $b$ es una función continua $\gamma:[0,1]\to X$ con extremos $a,b$. Un espacio es conexo por caminos si cada par puede unirse así; en el vacío la condición es vacua. Todo espacio conexo por caminos es conexo: una separación y un punto en cada parte producirían por el camino una separación del intervalo mediante preimágenes. El converso no se afirma sin prueba. En $\mathbb R^m$ las operaciones coordenadas permiten caminos lineales $\gamma(t)=(1-t)a+tb$ dentro de cualquier conjunto convexo; la estimación $d_\infty(\gamma(t),\gamma(s))=|t-s|d_\infty(a,b)$ acredita continuidad. Una imagen real continua de un conexo toma todos los valores intermedios entre dos de sus valores, pues su imagen es un intervalo. Ésta es la forma métrica del mecanismo de C15.

![Dos segmentos separados admiten una función continua binaria que vale cero a la izquierda y uno a la derecha. Sobre el intervalo completo, el mismo salto no es continuo: una ventana alrededor de cero ve ambos valores. Conexidad se diagnostica con abiertos relativos o preimágenes, sin confundirla con compacidad de los dos segmentos.](../../assets/books/anm/C31/C31-F07.svg){#fig-anm-c31-f07 fig-alt="Dos segmentos separados admiten una función continua binaria que vale cero a la izquierda y uno a la derecha. Sobre el intervalo completo, el mismo salto no es continuo: una ventana alrededor de cero ve ambos valores. Conexidad se diagnostica con abiertos relativos o preimágenes, sin confundirla con compacidad de los dos segmentos."}

### Microcontroles

#### Microcontrol 49

[]{#MA-MIC-ANM-01-031-049}

¿Qué exige una separación?

[]{#MA-MSOL-ANM-01-031-049}

<details class="anm-solution">
<summary>Ver solución del microcontrol 49</summary>

**Pregunta.** ¿Qué exige una separación?

**Respuesta.** Dos abiertos relativos no vacíos, disjuntos, cuya unión sea el espacio.

</details>

#### Microcontrol 50

[]{#MA-MIC-ANM-01-031-050}

¿Qué subconjunto refuta conexidad por ser abierto y cerrado?

[]{#MA-MSOL-ANM-01-031-050}

<details class="anm-solution">
<summary>Ver solución del microcontrol 50</summary>

**Pregunta.** ¿Qué subconjunto refuta conexidad por ser abierto y cerrado?

**Respuesta.** Uno propio y no vacío.

</details>

#### Microcontrol 51

[]{#MA-MIC-ANM-01-031-051}

¿Vacío y singleton son conexos?

[]{#MA-MSOL-ANM-01-031-051}

<details class="anm-solution">
<summary>Ver solución del microcontrol 51</summary>

**Pregunta.** ¿Vacío y singleton son conexos?

**Respuesta.** Sí; no admiten dos partes no vacías en separación.

</details>

#### Microcontrol 52

[]{#MA-MIC-ANM-01-031-052}

¿Qué informa una continua no constante hacia dos puntos discretos?

[]{#MA-MSOL-ANM-01-031-052}

<details class="anm-solution">
<summary>Ver solución del microcontrol 52</summary>

**Pregunta.** ¿Qué informa una continua no constante hacia dos puntos discretos?

**Respuesta.** Sus preimágenes dan una separación del dominio.

</details>

#### Microcontrol 53

[]{#MA-MIC-ANM-01-031-053}

¿Qué conserva una imagen continua de un conexo?

[]{#MA-MSOL-ANM-01-031-053}

<details class="anm-solution">
<summary>Ver solución del microcontrol 53</summary>

**Pregunta.** ¿Qué conserva una imagen continua de un conexo?

**Respuesta.** Conexidad de la imagen, mediante preimágenes de una separación hipotética.

</details>

#### Microcontrol 54

[]{#MA-MIC-ANM-01-031-054}

¿Qué son los conexos reales usuales?

[]{#MA-MSOL-ANM-01-031-054}

<details class="anm-solution">
<summary>Ver solución del microcontrol 54</summary>

**Pregunta.** ¿Qué son los conexos reales usuales?

**Respuesta.** Los intervalos, incluyendo vacío y singleton.

</details>

#### Microcontrol 55

[]{#MA-MIC-ANM-01-031-055}

¿Conexo por caminos implica conexo?

[]{#MA-MSOL-ANM-01-031-055}

<details class="anm-solution">
<summary>Ver solución del microcontrol 55</summary>

**Pregunta.** ¿Conexo por caminos implica conexo?

**Respuesta.** Sí; un camino entre las dos partes de una separación separaría $[0,1]$ por preimágenes.

</details>

#### Microcontrol 56

[]{#MA-MIC-ANM-01-031-056}

¿Se ha afirmado el converso de conexo por caminos?

[]{#MA-MSOL-ANM-01-031-056}

<details class="anm-solution">
<summary>Ver solución del microcontrol 56</summary>

**Pregunta.** ¿Se ha afirmado el converso de conexo por caminos?

**Respuesta.** No; la conexidad sola no se identifica con esa propiedad sin una prueba adicional.

</details>

### Ejercicios de la sección 31.7

#### Ejercicio 31

[]{#MA-EX-ANM-01-031-031}

Prueba que conexidad equivale a que los únicos subconjuntos abiertos y cerrados sean el vacío y el espacio.

[]{#MA-SOL-ANM-01-031-031}

<details class="anm-solution">
<summary>Ver solución del ejercicio 31</summary>

Una separación $U,V$ hace a $U$ no vacío, propio, abierto y cerrado por ser complemento de $V$. Recíprocamente, si $A$ es propio, no vacío, abierto y cerrado, $A$ y su complemento son abiertos no vacíos disjuntos que cubren el espacio. Ambas implicaciones incluyen el vacío y el singleton, donde no existen tales subconjuntos propios.

**Volver a la figura.** [C31-F07](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html#fig-anm-c31-f07): confronta el mecanismo de esta solución con las hipótesis y fronteras indicadas en su pie.

</details>

#### Ejercicio 32

[]{#MA-EX-ANM-01-031-032}

En $A=[-2,-1]\cup[1,2]$ usual, acredita compacidad y una separación relativa.

[]{#MA-SOL-ANM-01-031-032}

<details class="anm-solution">
<summary>Ver solución del ejercicio 32</summary>

Es unión de dos segmentos compactos, luego compacto. Las intersecciones con $(-\infty,0)$ y $(0,\infty)$ son abiertos relativos no vacíos, disjuntos y cubren $A$. Por tanto no es conexo. Esta separación no contradice la compacidad, pues las propiedades tienen definiciones distintas.

</details>

#### Ejercicio 33

[]{#MA-EX-ANM-01-031-033}

Sea $X$ conexo y $f:X\to\{0,1\}$ continua con codominio discreto. Prueba que $f$ es constante.

[]{#MA-SOL-ANM-01-031-033}

<details class="anm-solution">
<summary>Ver solución del ejercicio 33</summary>

Si tomara ambos valores, sus preimágenes serían abiertas, no vacías, disjuntas y cubrirían $X$, una separación. Por tanto toma a lo sumo un valor. En dominio vacío la función es constante en sentido vacuo, es decir, no toma dos valores diferentes.

</details>

#### Ejercicio 34

[]{#MA-EX-ANM-01-031-034}

Prueba que la imagen real de una función continua sobre un conexo contiene todos los valores entre dos de sus valores.

[]{#MA-SOL-ANM-01-031-034}

<details class="anm-solution">
<summary>Ver solución del ejercicio 34</summary>

La imagen es conexa por la prueba de preimágenes. Si tomara $u<v$ y faltara $c\in(u,v)$, las intersecciones de la imagen con $(-\infty,c)$ y $(c,\infty)$ serían una separación. Por tanto $c$ pertenece a la imagen y existe un punto del dominio con valor $c$. No se requiere que el dominio sea un intervalo ni que la función tenga orden monótono.

</details>

#### Ejercicio 35

[]{#MA-EX-ANM-01-031-035}

Prueba que una unión de conjuntos conexos con un punto común es conexa.

[]{#MA-SOL-ANM-01-031-035}

<details class="anm-solution">
<summary>Ver solución del ejercicio 35</summary>

Si la unión tuviera separación $U,V$, cada conjunto, por conexidad, estaría enteramente en una de las partes: las intersecciones darían de otro modo separación relativa. El punto común pertenece a una parte, digamos $U$, y obliga a todos los conjuntos a estar en $U$. Entonces $V$ sería vacía, contradicción. Si la familia es vacía su unión es vacía y conexa, tratada aparte.

</details>
## 31.8. Comparar lo que sobrevive y cerrar la ruta

[]{#MA-SEC-ANM-01-031-008}

Llegamos a tres propiedades globales que responden preguntas diferentes. Un destino para cada Cauchy no impide una separación; una cobertura finita no exige un camino; la ausencia de separación no garantiza destinos. La comparación debe usar ejemplos con su ambiente y su métrica, porque cambiar esa información puede cambiar la respuesta.

| Espacio con métrica indicada | Completo | Totalmente acotado | Compacto | Conexo |
|---|---|---|---|---|
| $[0,1]$, usual | Sí | Sí | Sí | Sí |
| $(0,1)$, usual | No | Sí | No | Sí |
| $\mathbb R$, usual | Sí | No | No | Sí |
| $\{0,1\}$, usual | Sí | Sí | Sí | No |
| $\mathbb N$, discreta | Sí | No | No | No |

Cada fila tiene un certificado. El segmento es cerrado y acotado en la recta e intervalo. El abierto pierde el destino de los recíprocos, aunque tiene redes finitas y es intervalo. La recta contiene la sucesión de enteros separados y es completa e intervalo. Dos puntos son un compacto finito y se separan. La discreta infinita tiene todas las Cauchy eventualmente constantes y necesita un singleton por bola pequeña. «Acotado» no aparece como sustituto de acotación total: la última fila es acotada y sigue fallando compacidad.

**Acotar la regla de medir no acota la complejidad.** En $\mathbb R$ pongamos $d'(x,y)=\min\{|x-y|,1\}$. C30 probó que es una métrica con los mismos abiertos, convergencias y sucesiones de Cauchy que la usual. Por tanto es completa y conexa. Todo el espacio está acotado, pues $d'\le1$. Sin embargo los enteros distintos tienen distancia $1$, no hay red finita de radio $1/2$ y el espacio no es compacto. La función $f(x)=x^2$ es continua porque la topología del dominio es la usual, pero no uniformemente continua: para $x_n=n$, $y_n=n+1/n$, $n\ge1$, $d'(x_n,y_n)=1/n\to0$ mientras
$$|f(y_n)-f(x_n)|=2+1/n^2\ge2.$$
Una tolerancia de salida $1$ refuta cualquier radio de entrada global. Se acredita así el contraejemplo anunciado en §31.6, con dominio realmente completo y acotado.

**La topología no recuerda todas las Cauchy.** C30 construyó $e(x,y)=|\phi(x)-\phi(y)|$ en $\mathbb R$, donde $\phi(x)=x/(1+|x|)$ es una biyección continua con inversa continua hacia $(-1,1)$. Este espacio tiene los mismos abiertos que la recta usual, por lo que es conexo y no compacto: ambas propiedades se expresan con abiertos. Es totalmente acotado porque es isométrico a un intervalo acotado. Para construir una red, tomamos una red de $(-1,1)$ y transportamos sus finitos centros mediante la inversa. Pero no es completo: $\phi(n)=n/(n+1)$ es Cauchy real con destino $1$ exterior a $(-1,1)$. Si $n$ convergiera en $e$ a $a\in\mathbb R$, sus imágenes convergerían a $\phi(a)<1$, contradiciendo la unicidad real.

Las comparaciones por constantes positivas de C30 conservan abiertos, Cauchy, acotación total y completitud. Para una comparación $c d\le e\le C d$, una red $d$ de radio $\varepsilon/C$ es una red $e$ de radio $\varepsilon$, y se razona al revés con $c$. Un **homeomorfismo**, biyección continua con inversa continua, conserva compacidad y conexidad por las pruebas de imágenes, pero no tiene por qué conservar completitud o acotación total. Una biyección uniformemente continua con inversa uniformemente continua sí conserva esas dos: transporta Cauchy; si la imagen tiene un destino, la inversa lo devuelve; y para redes transforma una tolerancia de salida en un radio común de entrada. No basta continuidad punto a punto para esta última conversión.

Sobre un compacto, todo homeomorfismo entre espacios métricos es uniforme en ambos sentidos por §31.6; allí las distinciones se reconcilian. Fuera de la compacidad vuelven a separarse. El libro comenzó construyendo una recta sin huecos, aprendió a controlar ventanas y colas, y termina identificando cuáles de esos mecanismos pertenecían a la distancia y cuáles al orden o a la geometría finita. Las coordenadas múltiples reutilizarán mallas y cortes comunes; los espacios de funciones reutilizarán supremos y completitud; el análisis complejo reutilizará continuidad y regiones conexas; medida e integración posteriores deberán sustituir o ampliar los controles de longitud que aquí se construyeron. Ninguna de esas rutas se da por demostrada en esta síntesis.

![La métrica truncada en la recta conserva Cauchy y completitud, pero hace acotado un espacio todavía no compacto. Los pares n y n+1/n tienen entrada 1/n que tiende a cero y salida cuadrática 2+1/n² al menos 2. La tabla compara cuatro modelos y mantiene separadas completitud, redes finitas, compacidad y conexidad.](../../assets/books/anm/C31/C31-F08.svg){#fig-anm-c31-f08 fig-alt="La métrica truncada en la recta conserva Cauchy y completitud, pero hace acotado un espacio todavía no compacto. Los pares n y n+1/n tienen entrada 1/n que tiende a cero y salida cuadrática 2+1/n² al menos 2. La tabla compara cuatro modelos y mantiene separadas completitud, redes finitas, compacidad y conexidad."}

### Microcontroles

#### Microcontrol 57

[]{#MA-MIC-ANM-01-031-057}

¿Qué falta en (0,1) para ser compacto?

[]{#MA-MSOL-ANM-01-031-057}

<details class="anm-solution">
<summary>Ver solución del microcontrol 57</summary>

**Pregunta.** ¿Qué falta en (0,1) para ser compacto?

**Respuesta.** Completitud: una Cauchy puede tener destino sólo en un extremo exterior.

</details>

#### Microcontrol 58

[]{#MA-MIC-ANM-01-031-058}

¿Qué falta en la discreta infinita para ser compacta?

[]{#MA-MSOL-ANM-01-031-058}

<details class="anm-solution">
<summary>Ver solución del microcontrol 58</summary>

**Pregunta.** ¿Qué falta en la discreta infinita para ser compacta?

**Respuesta.** Acotación total, aunque sí es completa y acotada.

</details>

#### Microcontrol 59

[]{#MA-MIC-ANM-01-031-059}

¿Truncar la distancia usual hace compacta la recta?

[]{#MA-MSOL-ANM-01-031-059}

<details class="anm-solution">
<summary>Ver solución del microcontrol 59</summary>

**Pregunta.** ¿Truncar la distancia usual hace compacta la recta?

**Respuesta.** No; los enteros siguen separados a pequeña escala.

</details>

#### Microcontrol 60

[]{#MA-MIC-ANM-01-031-060}

¿Qué propiedades de la recta conserva la métrica truncada?

[]{#MA-MSOL-ANM-01-031-060}

<details class="anm-solution">
<summary>Ver solución del microcontrol 60</summary>

**Pregunta.** ¿Qué propiedades de la recta conserva la métrica truncada?

**Respuesta.** Topología, convergencia, Cauchy, completitud y conexidad; cambia acotación.

</details>

#### Microcontrol 61

[]{#MA-MIC-ANM-01-031-061}

¿La métrica transportada por phi es completa?

[]{#MA-MSOL-ANM-01-031-061}

<details class="anm-solution">
<summary>Ver solución del microcontrol 61</summary>

**Pregunta.** ¿La métrica transportada por phi es completa?

**Respuesta.** No; las imágenes de $n$ se acercan al punto $1$ fuera del recorrido.

</details>

#### Microcontrol 62

[]{#MA-MIC-ANM-01-031-062}

¿Qué conserva un homeomorfismo necesariamente?

[]{#MA-MSOL-ANM-01-031-062}

<details class="anm-solution">
<summary>Ver solución del microcontrol 62</summary>

**Pregunta.** ¿Qué conserva un homeomorfismo necesariamente?

**Respuesta.** Compacidad y conexidad, por continuidad en ambos sentidos.

</details>

#### Microcontrol 63

[]{#MA-MIC-ANM-01-031-063}

¿Qué añade un inverso uniformemente continuo?

[]{#MA-MSOL-ANM-01-031-063}

<details class="anm-solution">
<summary>Ver solución del microcontrol 63</summary>

**Pregunta.** ¿Qué añade un inverso uniformemente continuo?

**Respuesta.** Transporta Cauchy y redes con tolerancias comunes, permitiendo preservar completitud y acotación total.

</details>

#### Microcontrol 64

[]{#MA-MIC-ANM-01-031-064}

¿Qué propiedad depende especialmente de las mallas finitas de la recta?

[]{#MA-MSOL-ANM-01-031-064}

<details class="anm-solution">
<summary>Ver solución del microcontrol 64</summary>

**Pregunta.** ¿Qué propiedad depende especialmente de las mallas finitas de la recta?

**Respuesta.** Que acotación implique acotación total, base geométrica de Heine–Borel finito-dimensional.

</details>

### Ejercicios de la sección 31.8

#### Ejercicio 36

[]{#MA-EX-ANM-01-031-036}

Clasifica $(\mathbb R,d_*)$, $d_*(x,y)=\min(|x-y|,1)$: acotación, completitud, compacidad y conexidad.

[]{#MA-SOL-ANM-01-031-036}

<details class="anm-solution">
<summary>Ver solución del ejercicio 36</summary>

Está acotado porque $d_*\le1$. Las Cauchy y convergencias coinciden con las usuales al usar tolerancias menores que $1$, por lo que es completo. Sus enteros están separados por distancia $1$, así que no es totalmente acotado ni compacto. Tiene la misma topología usual, luego es conexo porque la recta es un intervalo. Es un completo acotado no compacto.

**Volver a la figura.** [C31-F08](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html#fig-anm-c31-f08): confronta el mecanismo de esta solución con las hipótesis y fronteras indicadas en su pie.

</details>

#### Ejercicio 37

[]{#MA-EX-ANM-01-031-037}

Con esa métrica truncada en el dominio, refuta continuidad uniforme de $f(x)=x^2$ hacia la recta usual.

[]{#MA-SOL-ANM-01-031-037}

<details class="anm-solution">
<summary>Ver solución del ejercicio 37</summary>

Para $n\ge1$ tomamos $x_n=n$, $y_n=n+1/n$. La distancia de entrada es $1/n\to0$, pero $|f(y_n)-f(x_n)|=2+1/n^2\ge2$. Para cualquier $\delta>0$ existe $n$ con $1/n<\delta$; esos dos puntos violan la tolerancia de salida $1$. La función sí es continua porque las bolas pequeñas del dominio son las usuales.

</details>

#### Ejercicio 38

[]{#MA-EX-ANM-01-031-038}

Clasifica la métrica $e(x,y)=|\phi(x)-\phi(y)|$ en $\mathbb R$, $\phi(x)=x/(1+|x|)$, sin confundir topología y completitud.

[]{#MA-SOL-ANM-01-031-038}

<details class="anm-solution">
<summary>Ver solución del ejercicio 38</summary>

$\phi$ es una isometría hacia $(-1,1)$ con distancia usual, con inversa $t/(1-|t|)$. El intervalo es totalmente acotado, y transportar sus centros da redes finitas. La sucesión $n$ tiene imágenes $n/(n+1)\to1$, es Cauchy sin destino interno, luego el espacio no es completo ni compacto. Su topología es la usual, por lo que es conexo. La isometría no lo hace completo si el espacio de llegada no lo es.

</details>

#### Ejercicio 39

[]{#MA-EX-ANM-01-031-039}

Supón $c d\le e\le C d$ con $c,C>0$. Prueba preservación de acotación total y completitud.

[]{#MA-SOL-ANM-01-031-039}

<details class="anm-solution">
<summary>Ver solución del ejercicio 39</summary>

Una red $d$ de radio $\varepsilon/C$ es una red $e$ de radio $\varepsilon$. Una red $e$ de radio $c\varepsilon$ es una red $d$ de radio $\varepsilon$. Para completitud, una Cauchy $e$ es Cauchy $d$ por la cota inferior; si $d$ es completa tiene destino, y la cota superior transporta la convergencia a $e$. Invertir los papeles usando $e/C\le d\le e/c$ prueba el otro sentido.

</details>

#### Ejercicio 40

[]{#MA-EX-ANM-01-031-040}

¿Qué propiedades conserva necesariamente un homeomorfismo entre espacios métricos? Justifica compacidad y conexidad y refuta completitud.

[]{#MA-SOL-ANM-01-031-040}

<details class="anm-solution">
<summary>Ver solución del ejercicio 40</summary>

Compacidad y conexidad se conservan porque la función y su inversa son continuas y ambas propiedades se conservan por imágenes continuas. La biyección $\phi$ de la recta usual a $(-1,1)$ es un homeomorfismo. La recta es completa y el intervalo no, pues recíprocos cercanos al extremo tienen destino exterior. Por tanto completitud no es un invariante puramente topológico. Uniformidad de ambas direcciones sería una hipótesis suficiente adicional.

</details>

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-31)

[← Capítulo 30](analisis-para-matematicos-capitulo-30-espacios-metricos.html) · [Epílogo →](analisis-para-matematicos-epilogo.html)
