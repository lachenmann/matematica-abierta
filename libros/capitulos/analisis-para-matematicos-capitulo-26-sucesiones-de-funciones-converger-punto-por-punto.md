---
content-id: MA-BCH-0306
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-026
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
title: 'Capítulo 26 — Sucesiones de funciones: converger punto por punto'
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C26.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-26)

Una etapa entrega ahora una función entera. Miraremos sus columnas con las herramientas numéricas de C06 y preguntaremos qué cambia cuando también cambia la entrada. C12–C14 aportan tipos, límites y continuidad. C03 y las interfaces de C18/C23/C24/C25 se declaran al usarlas en pruebas y ejemplos; no se importan resultados de C27 o C28.

## 26.1. Dos índices, dos maneras de mirar

[]{#MA-SEC-ANM-01-026-001}

Una sucesión numérica entrega un número para cada índice. Ahora cada índice entrega una función completa. El dominio permanece fijo: sea $X\subseteq\mathbb R$, y para cada $n\in\mathbb N=\{0,1,2,\ldots\}$ sea $f_n:X\to\mathbb R$. El número $f_n(x)$ tiene dos argumentos de naturaleza distinta: $n$ ordena las etapas; $x$ señala una entrada del dominio. Cambiar el dominio entre etapas impide comparar columnas sin declarar antes una restricción común.

### Construir el objeto sin confundir sus representaciones

Por la teoría elemental de conjuntos y funciones declarada en C12, la colección $\mathcal F(X,\mathbb R)$ existe: sus elementos son los subconjuntos de $X\times\mathbb R$ que satisfacen existencia y unicidad de salida. Una sucesión de funciones es una aplicación $\mathbb N\to\mathcal F(X,\mathbb R)$. Equivalentemente, podemos dar una sola función
$$
F:\mathbb N\times X\to\mathbb R,\qquad F(n,x)=f_n(x).
$$
En la ida, la evaluación produce una salida única; en la vuelta, la sección $x\mapsto F(n,x)$ produce cada función. No se elige una salida entre varias. El grafo reúne pares con salidas ya únicas.

Fijar $n$ deja la fila $f_n$; fijar $x$ deja la sucesión numérica $n\mapsto f_n(x)$. La gráfica de una fila vive en $X\times\mathbb R$. Una columna se dibuja con índice horizontal y valor vertical. Usar un mismo dibujo sin distinguir esos ejes puede hacer parecer que la convergencia cambia el dominio.

Por ejemplo,
$$
f_n(x)=\frac{x}{n+1},\qquad X=\mathbb R.
$$
El denominador es positivo para todo índice, por lo que cada fila es una función real bien definida. En $x=2$ vemos $2,1,2/3,\ldots$; en $x=-1$ vemos $-1,-1/2,-1/3,\ldots$. Para una entrada fija $x$, el error respecto de cero es $|x|/(n+1)$. El destino es el mismo, pero los umbrales que lo certifican pueden depender de la columna.

### El conjunto donde las columnas convergen

No toda familia converge en todo su dominio. Definimos
$$
C=\{x\in X:\text{existe }y\in\mathbb R\text{ con }f_n(x)\to y\}.
$$
Para cada $x\in C$, la unicidad de C06 identifica un único $y$. El subconjunto
$$
G=\{(x,y)\in C\times\mathbb R:f_n(x)\to y\}
$$
es, por tanto, el grafo de una función $f:C\to\mathbb R$. No se invoca una selección numerable de límites: existencia y unicidad en cada fibra son precisamente la condición de función.

Para $f_n(x)=(-1)^n x$ en $\mathbb R$, la columna de cero es constante y converge. Si $x\ne0$, las subsecuencias pares e impares son constantes de valores $x$ y $-x$. Un supuesto límite tendría que coincidir con ambos por la transferencia a subsecuencias de C06; son distintos. Así $C=\{0\}$. Dar la fórmula de cada fila no garantiza la existencia de una función límite en todo $X$.

Si $X$ es vacío, existe una única función $X\to\mathbb R$ y toda afirmación para sus entradas es vacua. Los ejemplos y las refutaciones siguientes tendrán dominios no vacíos. Una figura con unas pocas columnas permite leer el tipo del objeto; no certifica las columnas que no muestra.

![Familia x/(n+1): las filas son gráficas respecto de x; las columnas fijan entradas y dibujan valores respecto del índice. Sólo se muestran tres entradas y tres etapas: la prueba para toda entrada está en R1–R2.](../../assets/books/anm/C26/C26-F01.svg){#fig-anm-c26-f01 fig-alt="Familia x/(n+1): las filas son gráficas respecto de x; las columnas fijan entradas y dibujan valores respecto del índice. Sólo se muestran tres entradas y tres etapas: la prueba para toda entrada está en R1–R2."}

### Microcontroles

#### Microcontrol 1

[]{#MA-MIC-ANM-01-026-001}

¿Qué queda fijo al mirar una columna?

[]{#MA-MSOL-ANM-01-026-001}

<details class="anm-solution">
<summary>Ver solución del microcontrol 1</summary>

La entrada $x\in X$; sólo varía el índice $n$, y los valores forman una sucesión real.

</details>

#### Microcontrol 2

[]{#MA-MIC-ANM-01-026-002}

¿Qué objeto es una fila?

[]{#MA-MSOL-ANM-01-026-002}

<details class="anm-solution">
<summary>Ver solución del microcontrol 2</summary>

Una función $f_n:X\to\mathbb R$, obtenida al fijar el índice y dejar variar la entrada.

</details>

#### Microcontrol 3

[]{#MA-MIC-ANM-01-026-003}

¿Por qué se declara un dominio común?

[]{#MA-MSOL-ANM-01-026-003}

<details class="anm-solution">
<summary>Ver solución del microcontrol 3</summary>

Para que toda columna esté definida en cada etapa y las comparaciones entre filas tengan el mismo tipo.

</details>

#### Microcontrol 4

[]{#MA-MIC-ANM-01-026-004}

¿En qué producto vive el grafo de una fila?

[]{#MA-MSOL-ANM-01-026-004}

<details class="anm-solution">
<summary>Ver solución del microcontrol 4</summary>

En $X\times\mathbb R$. El índice ordena las filas, pero no es la variable horizontal de esa gráfica.

</details>

#### Microcontrol 5

[]{#MA-MIC-ANM-01-026-005}

¿Qué garantiza salida única en el grafo del límite?

[]{#MA-MSOL-ANM-01-026-005}

<details class="anm-solution">
<summary>Ver solución del microcontrol 5</summary>

La unicidad del límite numérico de C06 para cada entrada donde converge la columna.

</details>

#### Microcontrol 6

[]{#MA-MIC-ANM-01-026-006}

¿Debe converger toda columna de una familia dada?

[]{#MA-MSOL-ANM-01-026-006}

<details class="anm-solution">
<summary>Ver solución del microcontrol 6</summary>

No. En $(-1)^n x$, sólo la entrada0 tiene columna convergente.

</details>

#### Microcontrol 7

[]{#MA-MIC-ANM-01-026-007}

¿Qué sucede si el dominio es vacío?

[]{#MA-MSOL-ANM-01-026-007}

<details class="anm-solution">
<summary>Ver solución del microcontrol 7</summary>

Existe una única función vacía y el contrato para todas las entradas es vacuo.

</details>

#### Microcontrol 8

[]{#MA-MIC-ANM-01-026-008}

¿Bastan tres columnas dibujadas para probar convergencia en un intervalo?

[]{#MA-MSOL-ANM-01-026-008}

<details class="anm-solution">
<summary>Ver solución del microcontrol 8</summary>

No; hay que responder al contrato para una entrada arbitraria del intervalo.

</details>

### Ejercicios de la sección 26.1

[]{#ejercicios-26}

#### Ejercicio 1. Fila y columna

[]{#MA-EX-ANM-01-026-001}

Para $F(n,x)=(n+1)x$ en $\mathbb N\times\mathbb R$, identifica filas, columnas y las entradas donde hay límite real.

[]{#MA-SOL-ANM-01-026-001}

<details class="anm-solution">
<summary>Ver solución del ejercicio 1</summary>

La fila de índice $n$ es la aplicación $x\mapsto(n+1)x$; la columna de entrada $x$ es $n\mapsto(n+1)x$. En cero la columna es constante0. Para $x>0$, dado $M>0$ basta $n+1>M/x$ para superar $M$; para $x<0$ los valores son menores que $-M$ cuando $n+1>M/|x|$. Una sucesión convergente sería acotada por C06, de modo que sólo converge la columna de cero. El conjunto de convergencia es $\{0\}$ y su función límite vale0.

**Retorno visual.** Véase [C26-F01](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html#fig-anm-c26-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 2. El dominio que se conserva

[]{#MA-EX-ANM-01-026-002}

Las fórmulas $f_n(x)=1/(x-n)$ tienen dominio $\mathbb R\setminus\{n\}$. Encuentra un dominio común y el límite allí.

[]{#MA-SOL-ANM-01-026-002}

<details class="anm-solution">
<summary>Ver solución del ejercicio 2</summary>

La intersección de los dominios es $X=\mathbb R\setminus\mathbb N$. Restringidas a $X$, todas las filas están definidas. Fijado $x\in X$, elegimos $N>|x|+1/\varepsilon$. Si $n\ge N$, $|x-n|\ge n-|x|>1/\varepsilon$, luego $|1/(x-n)|<\varepsilon$. Así convergen puntualmente a cero en $X$. Los ceros de denominador excluidos no pueden recuperarse sólo porque el error sea pequeño para índices posteriores.

</details>

#### Ejercicio 3. Alternancia dependiente de la entrada

[]{#MA-EX-ANM-01-026-003}

Calcula el conjunto de convergencia de $f_n(x)=(-1)^n(x-2)$ en $\mathbb R$.

[]{#MA-SOL-ANM-01-026-003}

<details class="anm-solution">
<summary>Ver solución del ejercicio 3</summary>

En $x=2$ todos los valores son0. Para otra entrada, las subsecuencias pares e impares tienen valores constantes $x-2$ y $2-x$, distintos. Si existiese límite de la columna, C06 lo transferiría a ambas y la unicidad lo identificaría con dos números distintos. Por tanto el conjunto de convergencia es $\{2\}$ y la función límite allí vale0. No se afirma convergencia en todo $\mathbb R$.

</details>

#### Ejercicio 4. Grafo del límite

[]{#MA-EX-ANM-01-026-004}

Explica por qué la existencia de límite real en cada columna de $X$ define una función sin escoger un límite arbitrario por entrada.

[]{#MA-SOL-ANM-01-026-004}

<details class="anm-solution">
<summary>Ver solución del ejercicio 4</summary>

Formamos el subconjunto $G=\{(x,y)\in X\times\mathbb R:f_n(x)\to y\}$. La hipótesis da al menos una salida en cada fibra y C06 da a lo sumo una. Por la definición de función de C12, $G$ es el grafo de una función $X\to\mathbb R$. Es una regla de salida única, no una aplicación del principio de selección entre varias salidas. Para $X$ vacío se obtiene el grafo vacío.

</details>

#### Ejercicio 5. Toda entrada salvo una

[]{#MA-EX-ANM-01-026-005}

Define $f_n(x)=1$ si $x=n$ y $0$ en otro caso, en $\mathbb R$. Determina su límite y explica por qué las gráficas no bastan.

[]{#MA-SOL-ANM-01-026-005}

<details class="anm-solution">
<summary>Ver solución del ejercicio 5</summary>

Para $x\notin\mathbb N$ la columna es siempre0. Si $x=m\in\mathbb N$, sólo el índice $m$ vale1; desde $N=m+1$ todos los términos son0. Por tanto el límite puntual es cero en toda la recta. Cada fila tiene un punto de altura1, pero una entrada fija encuentra como máximo uno. Una cantidad finita de gráficas no acredita las colas de todas las entradas; la clasificación anterior sí.

</details>
## 26.2. Una cola para cada entrada

[]{#MA-SEC-ANM-01-026-002}

Decimos que $f_n$ converge **puntualmente** a $f:X\to\mathbb R$ si
$$
\forall x\in X\ \forall\varepsilon>0\ \exists N\in\mathbb N\
\forall n\ge N:\quad |f_n(x)-f(x)|<\varepsilon.
$$
Es exactamente la convergencia numérica de C06 aplicada a cada entrada fija. Recibimos $x$ y $\varepsilon$ antes de construir $N$; después controlamos toda la cola en esa entrada. Escribimos $f_n\to f$ puntualmente en $X$ y dejamos explícito el dominio.

### Responder al desafío completo

Para $f_n(x)=x/(n+1)$ y $x=0$, sirve $N=0$. Si $x\ne0$, por la arquimedianidad de C03 elegimos un natural $N>|x|/\varepsilon$. Para $n\ge N$,
$$
|f_n(x)|=\frac{|x|}{n+1}
\le\frac{|x|}{N+1}<\varepsilon.
$$
La elección sirve también para $x=0$, pero separar la columna constante muestra que no necesitamos dividir por cero. La prueba responde a todo $x$ real y a toda tolerancia; comprobar dos entradas de una tabla no lo haría.

La dependencia permitida no es una dependencia obligatoria. Una familia puede tener un corte que funcione simultáneamente en muchas entradas. La definición puntual no exige ese privilegio. Si lo hay para un conjunto finito $A=\{x_1,\ldots,x_m\}$, lo podemos obtener: para una tolerancia fija, tomamos los $m$ cortes y su máximo. Toda cola posterior satisface las $m$ obligaciones. Si $A$ es vacío, sirve cualquier corte. No se toma el máximo de una colección infinita de umbrales.

### Unicidad y negación

Si $f_n\to f$ y $f_n\to g$ puntualmente, fijemos $x$. Si $d=|f(x)-g(x)|>0$, los dos cortes para $d/3$ tienen un máximo $N$. Entonces
$$
d\le |f(x)-f_N(x)|+|f_N(x)-g(x)|<2d/3,
$$
contradicción. Por tanto $f(x)=g(x)$ para toda entrada y C12 da igualdad de funciones.

La negación, para una candidata $f$ fija, es
$$
\exists x\in X\ \exists\varepsilon_0>0\ \forall N\in\mathbb N\
\exists n\ge N:\quad |f_n(x)-f(x)|\ge\varepsilon_0.
$$
El punto infractor debe permanecer fijo cuando $N$ varía. Si ante cada corte fabricamos una entrada distinta, habremos refutado una obligación simultánea más fuerte, no necesariamente la convergencia puntual.

Para $(-1)^n x$ y candidata cero, $x=1$ y $\varepsilon_0=1/2$ dan error1 en todo índice. Esto sí es una refutación puntual. Para $x/(n+1)$, escoger $x_n=n+1$ da error1 en cada etapa, pero la entrada cambia; la prueba anterior sigue mostrando convergencia puntual en $\mathbb R$.

### Umbrales mínimos sin elegir infinitamente

Para cada par $(x,\varepsilon)$, el conjunto
$$
H(x,\varepsilon)=\{N\in\mathbb N:\forall n\ge N,\
|f_n(x)-f(x)|<\varepsilon\}
$$
es no vacío cuando hay convergencia puntual. El buen orden de los naturales da su mínimo $\tau(x,\varepsilon)$. Esta regla es única y define una función sobre los pares autorizados. Si $\varepsilon$ disminuye, las obligaciones se vuelven más fuertes y el umbral mínimo no puede disminuir. Una fórmula suficiente de corte puede ser mayor que $\tau$; minimalidad y validez son preguntas distintas.

![Para x/(n+1) y tolerancia1/4, el umbral mínimo en las entradas no negativas mostradas es piso(4x). En cambio, la entrada móvil x_n=n+1 produce error1 en toda etapa. Esa ruta no refuta la convergencia puntual.](../../assets/books/anm/C26/C26-F02.svg){#fig-anm-c26-f02 fig-alt="Para x/(n+1) y tolerancia1/4, el umbral mínimo en las entradas no negativas mostradas es piso(4x). En cambio, la entrada móvil x_n=n+1 produce error1 en toda etapa. Esa ruta no refuta la convergencia puntual."}

### Microcontroles

#### Microcontrol 9

[]{#MA-MIC-ANM-01-026-009}

¿De qué datos puede depender el corte puntual?

[]{#MA-MSOL-ANM-01-026-009}

<details class="anm-solution">
<summary>Ver solución del microcontrol 9</summary>

De la entrada fija $x$ y la tolerancia positiva $\varepsilon$, recibidas antes de construirlo.

</details>

#### Microcontrol 10

[]{#MA-MIC-ANM-01-026-010}

¿Qué cuantificador sigue a la elección del corte?

[]{#MA-MSOL-ANM-01-026-010}

<details class="anm-solution">
<summary>Ver solución del microcontrol 10</summary>

El de todos los índices $n\ge N$; el error debe ser menor que la tolerancia en toda esa cola.

</details>

#### Microcontrol 11

[]{#MA-MIC-ANM-01-026-011}

¿Qué debe permanecer fijo al refutar convergencia hacia una candidata?

[]{#MA-MSOL-ANM-01-026-011}

<details class="anm-solution">
<summary>Ver solución del microcontrol 11</summary>

Una entrada y una tolerancia; para cada corte se produce un índice tardío infractor.

</details>

#### Microcontrol 12

[]{#MA-MIC-ANM-01-026-012}

¿Qué demuestra una entrada infractora que cambia con el corte?

[]{#MA-MSOL-ANM-01-026-012}

<details class="anm-solution">
<summary>Ver solución del microcontrol 12</summary>

Puede refutar un corte simultáneo para todas las entradas; por sí sola no refuta convergencia puntual.

</details>

#### Microcontrol 13

[]{#MA-MIC-ANM-01-026-013}

¿Por qué dos funciones límite puntuales coinciden?

[]{#MA-MSOL-ANM-01-026-013}

<details class="anm-solution">
<summary>Ver solución del microcontrol 13</summary>

En cada entrada, dos cortes para un tercio de la distancia entre supuestos destinos contradicen la desigualdad triangular.

</details>

#### Microcontrol 14

[]{#MA-MIC-ANM-01-026-014}

¿Cómo se reúnen los cortes de un conjunto finito de entradas?

[]{#MA-MSOL-ANM-01-026-014}

<details class="anm-solution">
<summary>Ver solución del microcontrol 14</summary>

Tomando su máximo finito, que domina todas las obligaciones de cola para la tolerancia fijada.

</details>

#### Microcontrol 15

[]{#MA-MIC-ANM-01-026-015}

¿Cómo se define el umbral mínimo $\tau(x,\varepsilon)$?

[]{#MA-MSOL-ANM-01-026-015}

<details class="anm-solution">
<summary>Ver solución del microcontrol 15</summary>

Como el mínimo natural del conjunto no vacío de cortes que controlan toda la cola en esa entrada y tolerancia.

</details>

#### Microcontrol 16

[]{#MA-MIC-ANM-01-026-016}

¿Qué ocurre con $\tau$ al disminuir la tolerancia?

[]{#MA-MSOL-ANM-01-026-016}

<details class="anm-solution">
<summary>Ver solución del microcontrol 16</summary>

No puede disminuir: cada corte válido para el desafío más exigente es válido para el menos exigente.

</details>

### Ejercicios de la sección 26.2

#### Ejercicio 6. Certificado explícito

[]{#MA-EX-ANM-01-026-006}

Da un corte para $f_n(x)=(x^2+1)/(n+1)\to0$ en $\mathbb R$ con error estricto menor que $\varepsilon$.

[]{#MA-SOL-ANM-01-026-006}

<details class="anm-solution">
<summary>Ver solución del ejercicio 6</summary>

Fijamos $x$ y $\varepsilon>0$ y elegimos un natural $N>(x^2+1)/\varepsilon$, por arquimedianidad. Para cualquier $n\ge N$, $(x^2+1)/(n+1)\le(x^2+1)/(N+1)<\varepsilon$. El numerador es positivo y el denominador también. El corte depende legítimamente de ambos desafíos y controla toda la cola.

</details>

#### Ejercicio 7. Negar en el orden correcto

[]{#MA-EX-ANM-01-026-007}

Escribe la negación de convergencia puntual hacia una candidata $f$ y úsala para refutar $f_n(x)=(-1)^n$ hacia cero en un dominio no vacío.

[]{#MA-SOL-ANM-01-026-007}

<details class="anm-solution">
<summary>Ver solución del ejercicio 7</summary>

La negación es $\exists x\in X\,\exists\varepsilon_0>0\,\forall N\,\exists n\ge N:\ |f_n(x)-f(x)|\ge\varepsilon_0$. Tomamos cualquier entrada del dominio no vacío y $\varepsilon_0=1/2$. Para cada $N$ sirve $n=N$, pues el error es1. Esa entrada no cambia con el corte. Además no hay otro límite real: las subsecuencias constantes1 y−1 lo refutarían por unicidad.

</details>

#### Ejercicio 8. Un infractor móvil

[]{#MA-EX-ANM-01-026-008}

Para $f_n(x)=x/(n+1)$ en $\mathbb R$, elige ante cada corte una entrada con error1. ¿Qué queda refutado?

[]{#MA-SOL-ANM-01-026-008}

<details class="anm-solution">
<summary>Ver solución del ejercicio 8</summary>

Dado $N$, usamos el índice $n=N$ y la entrada $x=N+1$. Entonces $f_N(x)=1$ y el error respecto del límite cero es1. Con tolerancia1/2 se refuta que exista un corte que controle simultáneamente todas las entradas. La entrada depende del corte, por lo que no se refuta la convergencia puntual, ya demostrada mediante $N(x,\varepsilon)>|x|/\varepsilon$.

**Retorno visual.** Véase [C26-F02](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html#fig-anm-c26-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 9. Reunión finita de obligaciones

[]{#MA-EX-ANM-01-026-009}

Para $f_n(x)=x/(n+1)$ y $A=\{-3,0,5\}$, produce un corte simultáneo y justifica la generalización a un conjunto finito.

[]{#MA-SOL-ANM-01-026-009}

<details class="anm-solution">
<summary>Ver solución del ejercicio 9</summary>

Un natural $N>5/\varepsilon$ funciona porque $|x|\le5$ en $A$ y $|f_n(x)|\le5/(N+1)<\varepsilon$. Para una familia puntual arbitraria en un conjunto finito, se toman los cortes de cada una de sus entradas para la misma tolerancia y su máximo finito. Ese máximo domina todas las obligaciones de cola. En el vacío sirve0. No se generaliza tomando un máximo infinito sin demostrar que existe.

</details>

#### Ejercicio 10. Umbral mínimo

[]{#MA-EX-ANM-01-026-010}

Para $f_n(x)=x/(n+1)$ calcula $\tau(x,\varepsilon)$ y comprueba la frontera estricta.

[]{#MA-SOL-ANM-01-026-010}

<details class="anm-solution">
<summary>Ver solución del ejercicio 10</summary>

Pongamos $r=|x|/\varepsilon\ge0$. Como los errores decrecen, un índice $N$ es válido exactamente cuando $N+1>r$. Si $r=0$, el mínimo es0. Para $r>0$, el piso de C06 satisface $\lfloor r\rfloor\le r<\lfloor r\rfloor+1$, y $N=\lfloor r\rfloor$ es válido. Un natural menor tiene $N+1\le\lfloor r\rfloor\le r$ y falla. Así $\tau=\lfloor r\rfloor$ también para $r=0$ con piso0. Cuando $r$ es entero positivo, bajar un índice deja error exactamente $\varepsilon$, que no basta.

</details>
## 26.3. Lo que se transporta columna por columna

[]{#MA-SEC-ANM-01-026-003}

Las operaciones puntuales se definen fila por fila y entrada por entrada. Para probar su convergencia fijamos primero $x$. Reutilizar resultados numéricos es legítimo porque entonces todos los términos que intervienen son reales de sucesiones ya dadas. Es útil reconstruir las estimaciones para ver dónde quedan las dependencias.

### Sumas, productos y cocientes

Si $f_n\to f$ y $g_n\to g$ puntualmente en $X$, entonces $\alpha f_n+\beta g_n\to\alpha f+\beta g$ para constantes reales. Repartimos una tolerancia entre los errores: bastan errores menores que $\varepsilon/[2(|\alpha|+1)]$ y $\varepsilon/[2(|\beta|+1)]$. El máximo de los dos cortes da error total menor que $\varepsilon$.

Para el producto, la convergencia de $f_n(x)$ da una cola con $|f_n(x)|\le |f(x)|+1=:B_x$. Allí
$$
|f_n(x)g_n(x)-f(x)g(x)|
\le B_x|g_n(x)-g(x)|+|g(x)|\,|f_n(x)-f(x)|.
$$
Elegimos los dos errores con los denominadores positivos $2(B_x+1)$ y $2(|g(x)|+1)$ y reunimos los tres cortes. No hemos obtenido una cota de $f_n$ que valga en todo $X$; sólo la cota necesaria en la entrada fijada.

Si $g(x)\ne0$, una cola con error menor que $|g(x)|/2$ satisface $|g_n(x)|>|g(x)|/2$. En esa cola el recíproco está definido y
$$
\left|\frac1{g_n(x)}-\frac1{g(x)}\right|
\le\frac{2|g_n(x)-g(x)|}{|g(x)|^2}\longrightarrow0.
$$
Esto prueba el cociente por el producto. Para hablar de una sucesión de funciones $f_n/g_n$ sobre un dominio fijo $Y$, se debe asegurar $g_n(x)\ne0$ para **todo** $n$ y $x\in Y$, o declarar valores de reparación para los ceros de cada fila. Que cada columna deje de tener ceros eventualmente no produce automáticamente un único comienzo válido para todas.

### Orden, encierro y composición

Si para la entrada fija $x$ se tiene $f_n(x)\le g_n(x)$ eventualmente, entonces $f(x)\le g(x)$. De fallar, con distancia $d=f(x)-g(x)>0$, dos errores menores que $d/3$ harían $f_n(x)>g_n(x)$ en una cola, contradicción. El comienzo de la desigualdad puede depender de $x$.

Si $a_n(x)\le f_n(x)\le b_n(x)$ eventualmente y ambos extremos convergen al mismo $h(x)$, entonces para errores extremos menores que $\varepsilon$ también $|f_n(x)-h(x)|<\varepsilon$. Para una función $\phi:D\to\mathbb R$ continua en $f(x)\in D$, y todas las entradas $f_n(x)\in D$, el radio de continuidad seguido del corte puntual prueba $\phi(f_n(x))\to\phi(f(x))$. La pertenencia al dominio va antes de componer. No se necesita continuidad de cada $f_n$ para estas reglas.

### Tres alcances de acotación

La convergencia puntual implica que para cada $x$ hay $B_x$ con $|f_n(x)|\le B_x$ para todos los índices: una cola acotada y el máximo de los términos iniciales finitos dan esa barrera por C06. No implica una constante común para todas las entradas e índices. Tampoco la acotación de cada fila implica una cota común entre filas.

En $[0,\infty)$, $u_n(x)=\min(n,x)$ converge a $u(x)=x$: para $n\ge x$ ya coincide. Cada fila está acotada por $n$, pero el límite no está acotado. En cambio, si $|f_n(x)|\le B$ para todos $n,x$, la preservación del orden da $|f(x)|\le B$ para todo $x$. La posición de la constante dentro o fuera de los cuantificadores determina qué puede heredarse.

![Filas u_n(x)=min(n,x), aquí restringidas a la ventana0≤x≤6 para dibujar. Cada fila tiene barrera n; cada columna tiene barrera x. El límite en todo\[0,∞) es x, no acotado. La ventana finita no demuestra la falta de cota global.](../../assets/books/anm/C26/C26-F03.svg){#fig-anm-c26-f03 fig-alt="Filas u_n(x)=min(n,x), aquí restringidas a la ventana0≤x≤6 para dibujar. Cada fila tiene barrera n; cada columna tiene barrera x. El límite en todo\[0,∞) es x, no acotado. La ventana finita no demuestra la falta de cota global."}

### Microcontroles

#### Microcontrol 17

[]{#MA-MIC-ANM-01-026-017}

¿Qué cota usa la prueba del producto?

[]{#MA-MSOL-ANM-01-026-017}

<details class="anm-solution">
<summary>Ver solución del microcontrol 17</summary>

Una cota eventual $|f_n(x)|\le|f(x)|+1$ en la entrada fijada; puede depender de ella.

</details>

#### Microcontrol 18

[]{#MA-MIC-ANM-01-026-018}

¿Qué barrera necesita el recíproco?

[]{#MA-MSOL-ANM-01-026-018}

<details class="anm-solution">
<summary>Ver solución del microcontrol 18</summary>

$|g_n(x)|>|g(x)|/2$ en una cola, después de declarar $g(x)\ne0$.

</details>

#### Microcontrol 19

[]{#MA-MIC-ANM-01-026-019}

¿Garantiza un denominador límite no nulo que todas las filas del cociente estén definidas?

[]{#MA-MSOL-ANM-01-026-019}

<details class="anm-solution">
<summary>Ver solución del microcontrol 19</summary>

No. Pueden tener ceros en índices iniciales distintos según la entrada; hace falta dominio común o reparación declarada.

</details>

#### Microcontrol 20

[]{#MA-MIC-ANM-01-026-020}

¿Se hereda una desigualdad estricta eventual?

[]{#MA-MSOL-ANM-01-026-020}

<details class="anm-solution">
<summary>Ver solución del microcontrol 20</summary>

No necesariamente: números positivos pueden tender a cero. El orden débil sí pasa al límite.

</details>

#### Microcontrol 21

[]{#MA-MIC-ANM-01-026-021}

¿Qué exige componer con una función exterior continua?

[]{#MA-MSOL-ANM-01-026-021}

<details class="anm-solution">
<summary>Ver solución del microcontrol 21</summary>

Que los valores de cada fila y el límite pertenezcan a su dominio, y continuidad en cada valor límite utilizado.

</details>

#### Microcontrol 22

[]{#MA-MIC-ANM-01-026-022}

¿Qué acotación produce una columna convergente?

[]{#MA-MSOL-ANM-01-026-022}

<details class="anm-solution">
<summary>Ver solución del microcontrol 22</summary>

Una barrera para todos sus términos, formada por una cola acotada y el máximo de su prefijo finito.

</details>

#### Microcontrol 23

[]{#MA-MIC-ANM-01-026-023}

¿Puede un límite puntual de filas acotadas ser no acotado?

[]{#MA-MSOL-ANM-01-026-023}

<details class="anm-solution">
<summary>Ver solución del microcontrol 23</summary>

Sí: $\min(n,x)$ en $[0,\infty)$ converge a $x$, sin cota global.

</details>

#### Microcontrol 24

[]{#MA-MIC-ANM-01-026-024}

¿Qué sucede si todas las filas tienen una misma barrera de magnitud?

[]{#MA-MSOL-ANM-01-026-024}

<details class="anm-solution">
<summary>Ver solución del microcontrol 24</summary>

El límite la hereda entrada por entrada mediante preservación del orden.

</details>

### Ejercicios de la sección 26.3

#### Ejercicio 11. Dos errores y una cota

[]{#MA-EX-ANM-01-026-011}

Prueba directamente que el producto de dos familias puntualmente convergentes converge al producto de sus límites.

[]{#MA-SOL-ANM-01-026-011}

<details class="anm-solution">
<summary>Ver solución del ejercicio 11</summary>

Fijamos $x$. La convergencia de $f_n(x)$ entrega una cola con $|f_n(x)|\le B=|f(x)|+1$. En ella el error del producto es como máximo $B|g_n(x)-g(x)|+|g(x)||f_n(x)-f(x)|$. Pedimos errores menores que $\varepsilon/[2(B+1)]$ y $\varepsilon/[2(|g(x)|+1)]$ y tomamos el máximo de esos dos cortes y el corte de acotación. La suma resultante es menor que $\varepsilon$. Cada constante fue fijada después de recibir $x$.

</details>

#### Ejercicio 12. Ceros por filas

[]{#MA-EX-ANM-01-026-012}

En $X=(0,1]$ sea $g_n(x)=x-1/(n+1)$. Prueba convergencia puntual y explica por qué $1/g_n$ no define una familia en todo $X$.

[]{#MA-SOL-ANM-01-026-012}

<details class="anm-solution">
<summary>Ver solución del ejercicio 12</summary>

El error respecto de $g(x)=x$ es $1/(n+1)$, que tiende a cero por C06. Cada columna tiene límite positivo y, desde algún corte dependiente de $x$, denominador positivo. Sin embargo, la fila $n$ se anula en $x=1/(n+1)\in X$. Por ello $1/g_n$ no es una función real sobre todo $X$. En $Y=X\setminus\{1/(n+1):n\in\mathbb N\}$ sí están definidas todas las filas y el recíproco converge a $1/x$ por la barrera $|g_n(x)|>x/2$ eventual.

</details>

#### Ejercicio 13. Orden eventual

[]{#MA-EX-ANM-01-026-013}

Si $f_n\to f$, $g_n\to g$ puntualmente y para cada $x$ hay un corte con $f_n(x)\le g_n(x)$ después de él, demuestra $f\le g$.

[]{#MA-SOL-ANM-01-026-013}

<details class="anm-solution">
<summary>Ver solución del ejercicio 13</summary>

Fijamos $x$. Si $d=f(x)-g(x)>0$, elegimos cortes para ambos errores menores que $d/3$ y los reunimos con el corte de orden. En una etapa posterior, $f_n(x)>f(x)-d/3$ y $g_n(x)<g(x)+d/3$, luego $f_n(x)-g_n(x)>d/3>0$, contradicción. Por tanto $f(x)\le g(x)$; la arbitrariedad de $x$ da el orden de funciones. La desigualdad estricta no se hereda necesariamente: $1/(n+1)>0$ converge a0.

</details>

#### Ejercicio 14. Filas acotadas, límite sin cota

[]{#MA-EX-ANM-01-026-014}

Analiza $u_n(x)=\min(n,x)$ en $[0,\infty)$ respecto de acotación de filas, columnas, límite y familia completa.

[]{#MA-SOL-ANM-01-026-014}

<details class="anm-solution">
<summary>Ver solución del ejercicio 14</summary>

Cada fila cumple $0\le u_n(x)\le n$. Para $x$ fijo, $0\le u_n(x)\le x$ y coincide con $x$ desde cualquier natural mayor que $x$. Así el límite es $u(x)=x$, sin cota superior en el dominio. No hay una barrera común para toda la familia: dado $B$, elegimos un natural $n>B$ y la entrada $x=n$, que da $u_n(n)=n>B$. Acotación fila por fila y columna por columna no producen una constante común.

**Retorno visual.** Véase [C26-F03](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html#fig-anm-c26-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 15. Componer dentro del tipo

[]{#MA-EX-ANM-01-026-015}

Si $f_n\to f$ puntualmente y todos sus valores y los de $f$ son no negativos, demuestra $\sqrt{f_n}\to\sqrt f$ sin suponer continuidad de las filas.

[]{#MA-SOL-ANM-01-026-015}

<details class="anm-solution">
<summary>Ver solución del ejercicio 15</summary>

Fijamos $x$. La raíz está definida para $f_n(x)$ y $f(x)$ por no negatividad; C14 demuestra continuidad relativa de la raíz en $[0,\infty)$, incluido0. Para una tolerancia recibimos su radio en el valor $f(x)$; la convergencia puntual da un corte que coloca todos los valores posteriores dentro de ese radio. La continuidad entrega error menor que la tolerancia. Sólo se usó continuidad de la operación exterior, no la de cada fila.

</details>
## 26.4. Potencias y una discontinuidad nueva

[]{#MA-SEC-ANM-01-026-004}

En $X=[0,1]$ definimos $p_0(x)=1$ y $p_{n+1}(x)=x\,p_n(x)$. Así $p_n(x)=x^n$ para $n\ge1$, sin dejar ambiguo el valor inicial en cero. Las filas son polinomios continuos por C14. El dominio compacto no evita por sí solo que el límite cambie la continuidad.

### Demostrar la convergencia, incluidos los extremos

En cero, $p_n(0)=0$ desde $n=1$; en uno, $p_n(1)=1$ siempre. Para $0<x<1$ ponemos $t=1/x-1>0$. Por inducción,
$$
(1+t)^n\ge1+nt\quad(n\in\mathbb N).
$$
El paso multiplica por $1+t>0$ y conserva el término adicional $nt^2\ge0$. Por ello
$$
0\le x^n\le\frac1{1+nt}.
$$
Para $\varepsilon>0$ elegimos $N>1/(\varepsilon t)$. Si $n\ge N$, la última cota es menor que $\varepsilon$. El límite puntual es
$$
p(x)=
\begin{cases}
0,&0\le x<1,\\
1,&x=1.
\end{cases}
$$
La prueba identifica primero los valores y después reúne las columnas; ningún argumento visual reemplaza la estimación.

La función $p$ es continua relativamente a $[0,1]$ en cada $x<1$: basta un radio menor que $1-x$ para quedar donde es constante. En uno falla. Para cualquier $\delta>0$, tomando $d=\min(\delta/2,1/2)>0$ y $y=1-d$ obtenemos $0<|y-1|<\delta$ y $|p(y)-p(1)|=1$. Con tolerancia $1/2$ ningún radio sirve. Así funciones continuas pueden tener un límite puntual discontinuo incluso en un segmento compacto.

### La entrada cercana al extremo responde tarde

Para cualquier índice $n\ge1$, el punto
$$
x_n=1-\frac1{2(n+1)}
$$
es menor que uno, por lo que $p(x_n)=0$. La desigualdad de Bernoulli en su versión $(1-s)^n\ge1-ns$, $0\le s\le1$, se obtiene por inducción: al multiplicar, el término extra $ns^2$ es no negativo. De aquí
$$
p_n(x_n)\ge1-\frac{n}{2(n+1)}>1/2.
$$
Cada etapa tiene una entrada con error grande aunque toda entrada fija menor que uno termina con error pequeño. Ante un supuesto corte común, tomar $n\ge\max(N,1)$ y ese $x_n$ lo refuta. No es una refutación de la convergencia puntual, pues la entrada varía.

Restringir a $[0,c]$ con $0<c<1$ permite usar el mismo $t_c=1/c-1$ para todas las entradas: $x^n\le c^n\le1/(1+nt_c)$. Si $c=0$, desde $n=1$ el error es cero. En $[0,1)$ el límite es continuo, pero los $x_n$ siguen perteneciendo al dominio y el error simultáneo persiste. Continuidad del límite y control simultáneo son obligaciones diferentes.

![Potencias en\[0,1\], con p0=1. El límite vale0 antes de1, punto abierto allí, y1 en1, punto cerrado. La ruta x_n=1−1/\[2(n+1)\] mantiene error mayor que1/2 mediante Bernoulli, aunque toda columna interior converge a cero.](../../assets/books/anm/C26/C26-F04.svg){#fig-anm-c26-f04 fig-alt="Potencias en\[0,1\], con p0=1. El límite vale0 antes de1, punto abierto allí, y1 en1, punto cerrado. La ruta x_n=1−1/\[2(n+1)\] mantiene error mayor que1/2 mediante Bernoulli, aunque toda columna interior converge a cero."}

### Microcontroles

#### Microcontrol 25

[]{#MA-MIC-ANM-01-026-025}

¿Cómo se define la etapa inicial de las potencias en cero?

[]{#MA-MSOL-ANM-01-026-025}

<details class="anm-solution">
<summary>Ver solución del microcontrol 25</summary>

Se declara $p_0=1$ en todo el dominio y se usa la recurrencia $p_{n+1}(x)=xp_n(x)$; no queda un símbolo ambiguo.

</details>

#### Microcontrol 26

[]{#MA-MIC-ANM-01-026-026}

¿Cuál es el límite de las potencias en una entrada $0<x<1$?

[]{#MA-MSOL-ANM-01-026-026}

<details class="anm-solution">
<summary>Ver solución del microcontrol 26</summary>

Cero, pues con $t=1/x-1>0$ se tiene $x^n\le1/(1+nt)$.

</details>

#### Microcontrol 27

[]{#MA-MIC-ANM-01-026-027}

¿Qué ocurre exactamente en uno?

[]{#MA-MSOL-ANM-01-026-027}

<details class="anm-solution">
<summary>Ver solución del microcontrol 27</summary>

Toda etapa vale1, por lo que el límite allí es1.

</details>

#### Microcontrol 28

[]{#MA-MIC-ANM-01-026-028}

¿Dónde falla continuidad del límite en $[0,1]$?

[]{#MA-MSOL-ANM-01-026-028}

<details class="anm-solution">
<summary>Ver solución del microcontrol 28</summary>

En1: cualquier ventana relativa contiene entradas menores que1 con valor límite0, frente al valor central1.

</details>

#### Microcontrol 29

[]{#MA-MIC-ANM-01-026-029}

¿Qué prueba Bernoulli para $x_n=1-1/[2(n+1)]$?

[]{#MA-MSOL-ANM-01-026-029}

<details class="anm-solution">
<summary>Ver solución del microcontrol 29</summary>

Que $x_n^n\ge1-n/[2(n+1)]>1/2$, con error grande respecto del límite en esa entrada.

</details>

#### Microcontrol 30

[]{#MA-MIC-ANM-01-026-030}

¿Por qué esa ruta no refuta convergencia puntual?

[]{#MA-MSOL-ANM-01-026-030}

<details class="anm-solution">
<summary>Ver solución del microcontrol 30</summary>

Porque la entrada cambia con el índice; cada entrada fija menor que1 sí tiene error tendente a cero.

</details>

#### Microcontrol 31

[]{#MA-MIC-ANM-01-026-031}

¿Qué facilita restringir a $[0,c]$ con $c<1$?

[]{#MA-MSOL-ANM-01-026-031}

<details class="anm-solution">
<summary>Ver solución del microcontrol 31</summary>

Una barrera $x^n\le c^n$ que entrega un corte para todas las entradas mediante el mismo $t_c>0$.

</details>

#### Microcontrol 32

[]{#MA-MIC-ANM-01-026-032}

¿Qué nueva columna debe examinarse en $[-1,1]$?

[]{#MA-MSOL-ANM-01-026-032}

<details class="anm-solution">
<summary>Ver solución del microcontrol 32</summary>

La de−1: alterna1 y−1, así no tiene límite real.

</details>

### Ejercicios de la sección 26.4

#### Ejercicio 16. Potencias y extremos

[]{#MA-EX-ANM-01-026-016}

Demuestra el límite puntual de $p_0=1$, $p_n(x)=x^n$ para $n\ge1$, en $[0,1]$, sin logaritmos.

[]{#MA-SOL-ANM-01-026-016}

<details class="anm-solution">
<summary>Ver solución del ejercicio 16</summary>

En cero todos los términos posteriores al inicial son0; en uno todos son1. Si $0<x<1$, ponemos $t=1/x-1>0$ y la inducción de Bernoulli da $(1+t)^n\ge1+nt$. Por reciprocidad positiva, $x^n\le1/(1+nt)$. Un natural $N>1/(\varepsilon t)$ hace esa cota menor que $\varepsilon$ para todo $n\ge N$. El límite vale0 en $[0,1)$ y1 en el extremo1.

</details>

#### Ejercicio 17. Discontinuidad relativa

[]{#MA-EX-ANM-01-026-017}

Refuta continuidad del límite de las potencias en1 con un testigo para cada radio.

[]{#MA-SOL-ANM-01-026-017}

<details class="anm-solution">
<summary>Ver solución del ejercicio 17</summary>

Fijamos tolerancia1/2. Dado $\delta>0$, definimos $d=\min(\delta/2,1/2)>0$ y $y=1-d$. Entonces $y\in[0,1)$, $0<|y-1|=d<\delta$, pero el límite toma valores0 en $y$ y1 en1. El error1 contradice cualquier radio de continuidad relativa. En cualquier centro menor que1, un radio menor que su distancia a1 deja el límite constante0, así que allí sí es continuo.

</details>

#### Ejercicio 18. Una infracción en cada etapa

[]{#MA-EX-ANM-01-026-018}

Con $x_n=1-1/[2(n+1)]$, prueba $p_n(x_n)>1/2$ y determina el alcance de la conclusión.

[]{#MA-SOL-ANM-01-026-018}

<details class="anm-solution">
<summary>Ver solución del ejercicio 18</summary>

Para $s=1/[2(n+1)]\in(0,1)$, la versión de Bernoulli $(1-s)^n\ge1-ns$ da $p_n(x_n)\ge1-n/[2(n+1)]>1/2$. En cada $x_n<1$ el límite vale0, luego hay error mayor que1/2 en todas las etapas, incluso en $n=0$ por $p_0=1$. Ante cualquier corte común, una de esas etapas lo viola. Las entradas varían con $n$; no se viola el contrato puntual.

**Retorno visual.** Véase [C26-F04](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html#fig-anm-c26-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 19. Cambiar el dominio

[]{#MA-EX-ANM-01-026-019}

Compara las potencias en $[0,c]$, $0<c<1$, y en $[0,1)$.

[]{#MA-SOL-ANM-01-026-019}

<details class="anm-solution">
<summary>Ver solución del ejercicio 19</summary>

En el primer dominio el límite es cero y $x^n\le c^n\le1/[1+n(1/c-1)]$. Un natural $N>1/[\varepsilon(1/c-1)]$ controla todas las entradas. En $[0,1)$ el límite también es cero y continuo, pero la ruta $x_n=1-1/[2(n+1)]$ permanece dentro del dominio y mantiene error mayor que1/2. Así no hay un corte simultáneo para esa tolerancia. El límite continuo no decide el control sobre todo un dominio infinito.

</details>

#### Ejercicio 20. Dominio ampliado

[]{#MA-EX-ANM-01-026-020}

Calcula el conjunto de convergencia real de la misma familia de potencias en $[-1,1]$.

[]{#MA-SOL-ANM-01-026-020}

<details class="anm-solution">
<summary>Ver solución del ejercicio 20</summary>

Para $|x|<1$, la prueba de Bernoulli aplicada a $|x|$ muestra $|x^n|\to0$, incluido el prefijo $p_0=1$. En1 el valor es siempre1. En−1 los valores alternan1 y−1, con subsecuencias constantes distintas; por unicidad no hay límite real. El conjunto de convergencia es $(-1,1]$, con límite0 en $(-1,1)$ y1 en1. Es indispensable revisar el nuevo extremo en lugar de reutilizar sin cambios la conclusión de $[0,1]$.

</details>
## 26.5. Cambiar la entrada mientras cambia el índice

[]{#MA-SEC-ANM-01-026-005}

La convergencia puntual mantiene fija la entrada durante toda la prueba. Una **diagonal** dada $x_n\in X$ cambia a la vez fila y columna; el dato $f_n(x_n)$ no está cubierto automáticamente por el contrato.

### Una capa de transición con fórmula racional

En $[0,1]$, sea
$$
a_n(x)=\frac{(n+1)x}{1+(n+1)x}.
$$
El denominador es al menos1; cada fila es continua. En cero vale0. Para $x>0$,
$$
|a_n(x)-1|=\frac1{1+(n+1)x}\le\frac1{(n+1)x}\longrightarrow0.
$$
Un corte natural mayor que $1/(\varepsilon x)$ controla la cola. El límite $a$ vale0 en cero y1 para $x>0$; es discontinuo en el origen, por el mismo argumento de ventana relativa usado en §26.4.

Tomemos ahora entradas explícitas:
$$
u_n=\frac1{n+1},\qquad v_n=\frac1{(n+1)^2}.
$$
Ambas convergen a cero y pertenecen al dominio, pero
$$
a_n(u_n)=1/2,\qquad
a_n(v_n)=\frac1{n+2}\longrightarrow0.
$$
Una tercera ruta, $w_n=1/\sqrt{n+1}$, da $a_n(w_n)=\sqrt{n+1}/(1+\sqrt{n+1})\to1$. La raíz positiva existe por C03; para justificar que el denominador crece, dado $M>0$ basta $n+1>M^2$. La diferencia respecto de1 es su recíproco. Las tres rutas llegan a la misma entrada y sus salidas tienen tres destinos.

Más generalmente, para $c>0$ y $u_n=c/(n+1)$, la ruta pertenece a $[0,1]$ desde un índice mayor que $c$ y allí $a_n(u_n)=c/(1+c)$. Podemos reparar el prefijo finito para obtener una ruta definida desde cero sin alterar ese límite. No basta poner una fórmula que abandona el dominio en las primeras etapas.

### Dos límites iterados efectivamente calculados

Para cada $n$ fijo, la continuidad y $a_n(0)=0$ dan
$$
\lim_{x\to0^+}a_n(x)=0,\qquad
\lim_{n\to\infty}\left(\lim_{x\to0^+}a_n(x)\right)=0.
$$
Por otra parte, para todo $x>0$ el límite en $n$ es1, de modo que
$$
\lim_{x\to0^+}\left(\lim_{n\to\infty}a_n(x)\right)=1.
$$
Se han comprobado ambas existencias antes de comparar. Que ambas operaciones de límite estén definidas no autoriza a permutarlas. Una figura de la transición muestra dónde se comprime el cambio, pero las dos evaluaciones son la prueba.

La diagonal tampoco queda resuelta sólo por la continuidad del límite. En la sección siguiente tendremos límite cero continuo y una ruta que sigue un pico de altura1. Para explicar qué dato adicional puede controlar diagonales, construiremos en §26.8 una estimación común de proximidad, sin usar aún los teoremas de C27 o C28.

![Capa a_n(x)=(n+1)x/\[1+(n+1)x\]. Las rutas1/(n+1),1/(n+1)^2 y1/√(n+1) llegan a0 pero sus salidas tienden a1/2,0 y1. Los límites iterados en entrada e índice dan0 y1; las curvas son representaciones de fórmulas probadas.](../../assets/books/anm/C26/C26-F05.svg){#fig-anm-c26-f05 fig-alt="Capa a_n(x)=(n+1)x/\[1+(n+1)x\]. Las rutas1/(n+1),1/(n+1)^2 y1/√(n+1) llegan a0 pero sus salidas tienden a1/2,0 y1. Los límites iterados en entrada e índice dan0 y1; las curvas son representaciones de fórmulas probadas."}

### Microcontroles

#### Microcontrol 33

[]{#MA-MIC-ANM-01-026-033}

¿Por qué cada fila de la capa racional está definida?

[]{#MA-MSOL-ANM-01-026-033}

<details class="anm-solution">
<summary>Ver solución del microcontrol 33</summary>

En $[0,1]$, su denominador $1+(n+1)x$ es al menos1.

</details>

#### Microcontrol 34

[]{#MA-MIC-ANM-01-026-034}

¿Qué error prueba el destino1 en entradas positivas?

[]{#MA-MSOL-ANM-01-026-034}

<details class="anm-solution">
<summary>Ver solución del microcontrol 34</summary>

$1/[1+(n+1)x]$, que es como máximo $1/[(n+1)x]$ y tiende a cero para $x$ fijo.

</details>

#### Microcontrol 35

[]{#MA-MIC-ANM-01-026-035}

¿Cuál es la salida en la ruta $1/(n+1)$?

[]{#MA-MSOL-ANM-01-026-035}

<details class="anm-solution">
<summary>Ver solución del microcontrol 35</summary>

Exactamente1/2 en toda etapa, porque el producto $(n+1)x$ vale1.

</details>

#### Microcontrol 36

[]{#MA-MIC-ANM-01-026-036}

¿Cuál es la salida en la ruta $1/(n+1)^2$?

[]{#MA-MSOL-ANM-01-026-036}

<details class="anm-solution">
<summary>Ver solución del microcontrol 36</summary>

$1/(n+2)$, que converge a cero.

</details>

#### Microcontrol 37

[]{#MA-MIC-ANM-01-026-037}

¿A qué destino llevan las entradas $1/\sqrt{n+1}$?

[]{#MA-MSOL-ANM-01-026-037}

<details class="anm-solution">
<summary>Ver solución del microcontrol 37</summary>

A1, pues la salida es $\sqrt{n+1}/(1+\sqrt{n+1})$.

</details>

#### Microcontrol 38

[]{#MA-MIC-ANM-01-026-038}

¿Qué precaución exige la ruta $c/(n+1)$ con $c>1$?

[]{#MA-MSOL-ANM-01-026-038}

<details class="anm-solution">
<summary>Ver solución del microcontrol 38</summary>

Reparar su prefijo para permanecer en $[0,1]$, por ejemplo tomando el mínimo con1.

</details>

#### Microcontrol 39

[]{#MA-MIC-ANM-01-026-039}

¿Qué valor da tomar primero el límite de entrada hacia cero?

[]{#MA-MSOL-ANM-01-026-039}

<details class="anm-solution">
<summary>Ver solución del microcontrol 39</summary>

Cero en cada fila y después cero al llevar el índice a infinito.

</details>

#### Microcontrol 40

[]{#MA-MIC-ANM-01-026-040}

¿Qué valor da tomar primero el límite del índice en entradas positivas?

[]{#MA-MSOL-ANM-01-026-040}

<details class="anm-solution">
<summary>Ver solución del microcontrol 40</summary>

Uno en cada entrada positiva y después uno al acercarla al origen.

</details>

### Ejercicios de la sección 26.5

#### Ejercicio 21. Capa racional

[]{#MA-EX-ANM-01-026-021}

Para $a_n(x)=(n+1)x/[1+(n+1)x]$ en $[0,1]$, prueba el límite y su fallo de continuidad en0.

[]{#MA-SOL-ANM-01-026-021}

<details class="anm-solution">
<summary>Ver solución del ejercicio 21</summary>

En0 los valores son0. Para $x>0$, el error respecto de1 es $1/[1+(n+1)x]\le1/[(n+1)x]$. Un corte mayor que $1/(\varepsilon x)$ lo controla. El límite es1 para toda entrada positiva y0 en0. Dado cualquier radio $\delta>0$, $y=\min(\delta/2,1/2)>0$ queda a distancia menor que $\delta$ de0 y tiene error1 respecto del valor central. Tolerancia1/2 refuta continuidad.

</details>

#### Ejercicio 22. Dos rutas, dos destinos

[]{#MA-EX-ANM-01-026-022}

Calcula $a_n(1/(n+1))$ y $a_n(1/(n+1)^2)$ y explica por qué no contradicen el límite puntual.

[]{#MA-SOL-ANM-01-026-022}

<details class="anm-solution">
<summary>Ver solución del ejercicio 22</summary>

La primera ruta hace $(n+1)x=1$ y la salida es1/2. La segunda hace $(n+1)x=1/(n+1)$ y la salida es1/(n+2), que tiende a0. Ambas entradas tienden a0 y pertenecen a $[0,1]$. No son una columna fija: el contrato puntual sólo controla $a_n(x)$ cuando $x$ permanece fijo al variar $n$. Por ello sus destinos diferentes son compatibles con el límite puntual obtenido.

**Retorno visual.** Véase [C26-F05](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html#fig-anm-c26-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 23. Una escala intermedia

[]{#MA-EX-ANM-01-026-023}

Para $w_n=1/\sqrt{n+1}$ calcula el destino de $a_n(w_n)$ y justifica las raíces y la convergencia.

[]{#MA-SOL-ANM-01-026-023}

<details class="anm-solution">
<summary>Ver solución del ejercicio 23</summary>

La raíz positiva de $n+1$ existe y es al menos1, así $w_n\in[0,1]$. Para cualquier $M>0$, elegir $n+1>M^2$ da $\sqrt{n+1}>M$; por ello $w_n\to0$. La salida es $\sqrt{n+1}/[1+\sqrt{n+1}]$, cuyo error respecto de1 es $1/[1+\sqrt{n+1}]$. Esta diferencia tiende a0 por la misma comparación. El destino es1, distinto de los de las dos rutas del ejercicio anterior.

</details>

#### Ejercicio 24. Límites iterados

[]{#MA-EX-ANM-01-026-024}

Calcula las dos operaciones iteradas en $n\to\infty$ y $x\to0^+$ para $a_n$.

[]{#MA-SOL-ANM-01-026-024}

<details class="anm-solution">
<summary>Ver solución del ejercicio 24</summary>

Para una fila fija, continuidad en0 y valor0 dan $\lim_{x\to0^+}a_n(x)=0$; el límite en $n$ de esos números es0. Para una entrada positiva fija, el límite en $n$ es1; el límite por $x\to0^+$ de la función constante1 es1. Ambas operaciones iteradas existen y dan valores diferentes. La comparación es legítima porque antes se calculó la existencia de cada límite interior y exterior.

</details>

#### Ejercicio 25. Reparar un prefijo fuera del dominio

[]{#MA-EX-ANM-01-026-025}

Para $c>0$ construye una ruta en $[0,1]$ que coincida eventualmente con $c/(n+1)$ y calcula las salidas de $a_n$.

[]{#MA-SOL-ANM-01-026-025}

<details class="anm-solution">
<summary>Ver solución del ejercicio 25</summary>

Definimos $x_n=\min(1,c/(n+1))$. Está en $[0,1]$ para todo índice y, desde un natural mayor que $c$, coincide con $c/(n+1)$. La ruta converge a0 por coincidencia eventual con esa sucesión numérica. En la cola, $(n+1)x_n=c$ y $a_n(x_n)=c/(1+c)$. Por transferencia de prefijos finitos, toda la sucesión de salidas converge a ese número. Si se usara la fórmula sin reparación y $c>1$, las primeras entradas podrían estar fuera del dominio.

</details>
## 26.6. Picos que ninguna entrada fija retiene

[]{#MA-SEC-ANM-01-026-006}

Una anomalía puede moverse de manera que ninguna entrada fija la retenga. Para $k=n+3$, definimos en $[0,1]$
$$
t_n(x)=\max\{0,1-|kx-2|\}.
$$
El máximo se expresa por $(u+v+|u-v|)/2$, de modo que C14 prueba continuidad de cada fila. La región positiva es $(1/k,3/k)$, el centro $2/k$ tiene altura1 y los extremos del soporte tienen valor0. Como $k\ge3$, todo el soporte está dentro del segmento, también en la primera etapa.

### Captura fija y seguimiento del pico

En cero, $t_n(0)=0$. Para un $x>0$ fijo, elegimos $N$ natural con $N+3>3/x$. Si $n\ge N$, entonces $kx>3$ y $t_n(x)=0$. La columna queda exactamente en cero desde ese corte, no sólo aproximadamente. Así $t_n\to0$ puntualmente.

La ruta $z_n=2/(n+3)$ converge a cero y satisface $t_n(z_n)=1$ en todo índice. El límite cero es continuo; la diagonal vale1. De nuevo se ve el gasto de mantener fija la entrada. Hay, además, una cota común $0\le t_n\le1$: ni esa cota ni la continuidad fila por fila solucionan el cambio de entrada.

### El área y la altura son gastos distintos

Las dos ramas no nulas son
$$
t_n(x)=kx-1\ \text{en }[1/k,2/k],\qquad
t_n(x)=3-kx\ \text{en }[2/k,3/k].
$$
C23 da integrabilidad por continuidad, restricción y aditividad. Para verificar el valor sin inferirlo de una figura, una función afín en un intervalo de anchura $d$, con valores extremos $A,B$, tiene integral $d(A+B)/2$: una primitiva cuadrática de C18 y C24 lo demuestra. Cada rama tiene anchura $1/k$ y extremos0,1 o1,0. Por tanto
$$
\int_0^1t_n(x)\,dx=\frac1k\longrightarrow0.
$$
El límite puntual también tiene integral0.

Ahora normalizamos la altura:
$$
b_n(x)=k\,t_n(x).
$$
Para cada entrada positiva, desde el mismo corte el valor es exactamente cero; en cero también. Por ello $b_n\to0$ puntualmente. Cada fila sigue siendo continua e integrable. Sin embargo,
$$
b_n(z_n)=k,\qquad \int_0^1b_n(x)\,dx=1.
$$
El límite de las integrales vale1 y la integral del límite vale0. Los dos valores existen y difieren. La amplitud compensa exactamente la anchura del soporte. Este ejemplo muestra un intercambio fallido, no un teorema general sobre cuándo intercambiar.

En $t_n$ había altura común y áreas decrecientes; en $b_n$ cada columna sigue acotada por su prefijo finito y cola cero, pero las alturas de las filas crecen. Ninguna de esas observaciones permite concluir a partir de un número finito de muestreos: los puntos que siguen el pico están dados por fórmula y prueban la obstrucción para todo índice.

![Tiendas con k=n+3, soporte\[1/k,3/k\] dentro\[0,1\]. Altura1 y área1/k a la izquierda; altura k y área1 a la derecha. Ambas familias convergen puntualmente a cero; seguir2/k mantiene el pico. No se infiere el área desde el dibujo: se calculó por ramas.](../../assets/books/anm/C26/C26-F06.svg){#fig-anm-c26-f06 fig-alt="Tiendas con k=n+3, soporte\[1/k,3/k\] dentro\[0,1\]. Altura1 y área1/k a la izquierda; altura k y área1 a la derecha. Ambas familias convergen puntualmente a cero; seguir2/k mantiene el pico. No se infiere el área desde el dibujo: se calculó por ramas."}

### Microcontroles

#### Microcontrol 41

[]{#MA-MIC-ANM-01-026-041}

¿Qué región tiene valores positivos en $t_n$?

[]{#MA-MSOL-ANM-01-026-041}

<details class="anm-solution">
<summary>Ver solución del microcontrol 41</summary>

$(1/k,3/k)$ con $k=n+3$; en los extremos vale0 y en el centro $2/k$ vale1.

</details>

#### Microcontrol 42

[]{#MA-MIC-ANM-01-026-042}

¿Por qué se eligió $k=n+3$?

[]{#MA-MSOL-ANM-01-026-042}

<details class="anm-solution">
<summary>Ver solución del microcontrol 42</summary>

Para que el soporte $[1/k,3/k]$ permanezca en $[0,1]$ desde la etapa inicial.

</details>

#### Microcontrol 43

[]{#MA-MIC-ANM-01-026-043}

¿Qué pasa en una entrada positiva fija?

[]{#MA-MSOL-ANM-01-026-043}

<details class="anm-solution">
<summary>Ver solución del microcontrol 43</summary>

Desde un corte con $n+3>3/x$, queda a la derecha del soporte y todos sus valores posteriores son0.

</details>

#### Microcontrol 44

[]{#MA-MIC-ANM-01-026-044}

¿Qué ruta sigue siempre el pico?

[]{#MA-MSOL-ANM-01-026-044}

<details class="anm-solution">
<summary>Ver solución del microcontrol 44</summary>

$z_n=2/(n+3)$, que converge al origen y produce salidas1.

</details>

#### Microcontrol 45

[]{#MA-MIC-ANM-01-026-045}

¿Qué integral tiene la tienda de altura1?

[]{#MA-MSOL-ANM-01-026-045}

<details class="anm-solution">
<summary>Ver solución del microcontrol 45</summary>

$1/k$: dos ramas afines de anchura1/k tienen integral1/(2k) cada una.

</details>

#### Microcontrol 46

[]{#MA-MIC-ANM-01-026-046}

¿Qué cambia al multiplicar la altura por $k$?

[]{#MA-MSOL-ANM-01-026-046}

<details class="anm-solution">
<summary>Ver solución del microcontrol 46</summary>

La integral pasa a1, mientras cada columna sigue quedando eventualmente en cero.

</details>

#### Microcontrol 47

[]{#MA-MIC-ANM-01-026-047}

¿Tiene $b_n$ una barrera de valores común entre etapas?

[]{#MA-MSOL-ANM-01-026-047}

<details class="anm-solution">
<summary>Ver solución del microcontrol 47</summary>

No: su valor en el centro es $k=n+3$, arbitrariamente grande.

</details>

#### Microcontrol 48

[]{#MA-MIC-ANM-01-026-048}

¿Por qué no hay una constante Lipschitz común para $t_n$?

[]{#MA-MSOL-ANM-01-026-048}

<details class="anm-solution">
<summary>Ver solución del microcontrol 48</summary>

Entre $1/k$ y $2/k$ la salida cambia1 en distancia1/k; toda constante válida debe ser al menos $k$.

</details>

### Ejercicios de la sección 26.6

#### Ejercicio 26. Tiendas continuas

[]{#MA-EX-ANM-01-026-026}

Para $k=n+3$ demuestra continuidad, soporte y convergencia puntual a cero de $t_n(x)=\max(0,1-|kx-2|)$ en $[0,1]$.

[]{#MA-SOL-ANM-01-026-026}

<details class="anm-solution">
<summary>Ver solución del ejercicio 26</summary>

La función afín, el valor absoluto y el máximo mediante $(u+v+|u-v|)/2$ son continuos por C14. La condición positiva equivale a $1<kx<3$, por lo que su región positiva es $(1/k,3/k)$ y en los extremos vale0. En0 es siempre0. Para $x>0$, un corte $N+3>3/x$ hace $kx>3$ en toda la cola y todos sus valores son0. Así el límite puntual es la función cero; el soporte cerrado es $[1/k,3/k]$.

</details>

#### Ejercicio 27. Seguir el centro

[]{#MA-EX-ANM-01-026-027}

Encuentra una ruta convergente al origen que produzca salidas constantes1 en las tiendas. ¿Bastan límite continuo y cota común para evitarlo?

[]{#MA-SOL-ANM-01-026-027}

<details class="anm-solution">
<summary>Ver solución del ejercicio 27</summary>

La ruta $z_n=2/(n+3)$ está en $[0,1]$ y tiende a0. En ella $kz_n=2$, por lo que $t_n(z_n)=1$. Sin embargo el límite puntual es cero, continuo, y toda fila satisface $0\le t_n\le1$. Las dos condiciones mencionadas no bastan, ni siquiera junto con continuidad de todas las filas y compactitud del dominio. El testigo es explícito para todos los índices.

</details>

#### Ejercicio 28. Certificar el área

[]{#MA-EX-ANM-01-026-028}

Calcula $\int_0^1t_n$ por ramas, acreditando existencia antes del valor.

[]{#MA-SOL-ANM-01-026-028}

<details class="anm-solution">
<summary>Ver solución del ejercicio 28</summary>

La continuidad da integrabilidad por C23. El valor fuera de $[1/k,3/k]$ es0. En la primera rama la función es $kx-1$ y en la segunda $3-kx$; ambas tienen anchura $1/k$ y valores extremos0,1 o1,0. Una primitiva cuadrática, o la fórmula afín probada desde C24, da área $1/(2k)$ a cada rama. Restricción y aditividad producen integral $1/k$. Con $k=n+3$, los valores tienden a0, igual a la integral del límite.

</details>

#### Ejercicio 29. Altura que compensa anchura

[]{#MA-EX-ANM-01-026-029}

Para $b_n=(n+3)t_n$ demuestra convergencia puntual y compara límite de integrales e integral del límite.

[]{#MA-SOL-ANM-01-026-029}

<details class="anm-solution">
<summary>Ver solución del ejercicio 29</summary>

Cada columna positiva queda exactamente en cero desde el mismo corte de $t_n$ y la columna de0 siempre vale0. Multiplicar por $n+3$ no cambia esa coincidencia eventual, así $b_n\to0$ puntualmente. Cada fila es continua e integrable. Por linealidad de C23 y el área anterior, $\int_0^1b_n=(n+3)/(n+3)=1$. El límite de esas integrales es1, mientras el límite puntual cero tiene integral0. Ambas integrales comparadas existen y difieren.

**Retorno visual.** Véase [C26-F06](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html#fig-anm-c26-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 30. Pendientes sin constante común

[]{#MA-EX-ANM-01-026-030}

Demuestra que las tiendas $t_n$ no satisfacen una cota Lipschitz con la misma constante para todas las filas.

[]{#MA-SOL-ANM-01-026-030}

<details class="anm-solution">
<summary>Ver solución del ejercicio 30</summary>

En los puntos $u_n=1/k$ y $v_n=2/k$ tenemos salidas0 y1, mientras la distancia de entrada es1/k. Una cota común $|t_n(u)-t_n(v)|\le L|u-v|$ obligaría a $1\le L/k$, esto es $k\le L$, para todos $k=n+3$. La arquimedianidad permite elegir uno mayor que $L$, contradicción. Cada fila sí tiene constante $k$, pero esa dependencia del índice es exactamente la obstrucción.

</details>
## 26.7. Tres intercambios que pueden fallar

[]{#MA-SEC-ANM-01-026-007}

Antes de intercambiar operaciones, hay que comprobar que los objetos que se comparan existen. C25 ya produjo una familia en la que esta precaución decide la cuestión.

### La integrabilidad puede desaparecer

Sea $E_m\subseteq[0,1]$ el conjunto de racionales irreducibles con denominador como máximo $m$, y $d_n=\mathbf1_{E_{n+1}}$. C25 demostró finitud de $E_m$ e integral0 de su indicadora. Si $x$ es irracional, $d_n(x)=0$ siempre. Si $x=p/q$ irreducible, $d_n(x)=1$ desde $n+1\ge q$. Por ello $d_n$ converge puntualmente a la indicadora de los racionales, la función de Dirichlet.

Todas las filas son integrables, con integral0, y la familia está acotada entre0 y1. El límite no es integrable por C25. Por tanto no se puede escribir su integral de Riemann como uno de los miembros de una igualdad. El ejemplo de $b_n$ era más fuerte respecto de otra pregunta: allí existían ambas integrales comparadas y tenían valores distintos. Cada contraejemplo tiene un alcance que conviene conservar.

### Las derivadas pueden tener otro límite

Para $k=n+1$, sea en $\mathbb R$
$$
h_n(x)=\frac{x}{1+kx^2}.
$$
El denominador es positivo; las reglas de C18 dan
$$
h_n'(x)=\frac{1-kx^2}{(1+kx^2)^2}.
$$
En cero, $h_n(0)=0$. Para $x\ne0$,
$$
|h_n(x)|\le\frac1{k|x|}\longrightarrow0.
$$
Así el límite $h$ es la función cero, derivable con $h'=0$.

Pero $h_n'(0)=1$ para todo índice. Si $x\ne0$, ponemos $s=kx^2>0$ y obtenemos
$$
|h_n'(x)|\le\frac{1+s}{(1+s)^2}
=\frac1{1+s}\longrightarrow0.
$$
Las derivadas convergen puntualmente a $g=\mathbf1_{\{0\}}$, que difiere de $h'$ en cero. En este ejemplo existen tanto la derivada del límite como el límite puntual de las derivadas; no son iguales. No se está afirmando que $g$ sea una derivada. La discontinuidad de $g$ no es, por sí sola, una prueba de que ninguna función pueda tenerla como derivada; ese sería otro problema.

Incluso el error de $h_n$ admite una cota para todas las entradas:
$$
1+kx^2\ge2\sqrt{k}|x|
\quad\Longrightarrow\quad
|h_n(x)|\le\frac1{2\sqrt{k}}.
$$
La primera desigualdad procede del cuadrado $(\sqrt{k}|x|-1)^2\ge0$; en cero la segunda se verifica directamente. En $x=1/\sqrt{k}$ se alcanza la cota. Así una estimación global de los valores tampoco basta por sí sola para intercambiar derivadas. No formulamos aquí la teoría que sí permite hacerlo; C28 la desarrollará con sus hipótesis propias.

### Continuidad: dónde se rompe la prueba tentadora

Para tratar de probar continuidad de $f$, la desigualdad natural es
$$
|f(y)-f(x)|
\le |f(y)-f_n(y)|+|f_n(y)-f_n(x)|+|f_n(x)-f(x)|.
$$
El control puntual en $x$ elige un $n$ grande para el último término; la continuidad de esa fila controla el término central cerca de $x$. El primer término requiere ahora controlar entradas $y$ variables con esa misma fila. La convergencia puntual no proporciona ese control en toda la ventana. Ese es el paso inválido, no la desigualdad triangular. Los ejemplos de potencias y capa racional lo hacen visible.

![h_n=x/(1+kx²) y h_n′=(1−kx²)/(1+kx²)², k=n+1. Los valores tienden a cero con máximo1/(2√k); las derivadas tienden a0 fuera de0 pero conservan1 en0. El punto excepcional del límite de derivadas está marcado; la derivada del límite vale0.](../../assets/books/anm/C26/C26-F07.svg){#fig-anm-c26-f07 fig-alt="h_n=x/(1+kx²) y h_n′=(1−kx²)/(1+kx²)², k=n+1. Los valores tienden a cero con máximo1/(2√k); las derivadas tienden a0 fuera de0 pero conservan1 en0. El punto excepcional del límite de derivadas está marcado; la derivada del límite vale0."}

### Microcontroles

#### Microcontrol 49

[]{#MA-MIC-ANM-01-026-049}

¿Cuál es el límite puntual de $\mathbf1_{E_{n+1}}$?

[]{#MA-MSOL-ANM-01-026-049}

<details class="anm-solution">
<summary>Ver solución del microcontrol 49</summary>

Dirichlet: cada racional de denominadorq aparece desde $n+1\ge q$, mientras los irracionales nunca aparecen.

</details>

#### Microcontrol 50

[]{#MA-MIC-ANM-01-026-050}

¿Existe su integral de Riemann?

[]{#MA-MSOL-ANM-01-026-050}

<details class="anm-solution">
<summary>Ver solución del microcontrol 50</summary>

No; C25 demostró la obstrucción de oscilación persistente en todo intervalo.

</details>

#### Microcontrol 51

[]{#MA-MIC-ANM-01-026-051}

¿Qué integral tiene cada indicadora finita?

[]{#MA-MSOL-ANM-01-026-051}

<details class="anm-solution">
<summary>Ver solución del microcontrol 51</summary>

Cero, por los resultados de C25 para modificaciones y soportes finitos.

</details>

#### Microcontrol 52

[]{#MA-MIC-ANM-01-026-052}

¿Qué valor tienen las derivadas $h_n^{\prime}(0)$?

[]{#MA-MSOL-ANM-01-026-052}

<details class="anm-solution">
<summary>Ver solución del microcontrol 52</summary>

Uno para toda etapa; el límite de los valores $h_n$ es cero y su derivada en0 vale0.

</details>

#### Microcontrol 53

[]{#MA-MIC-ANM-01-026-053}

¿Qué ocurre con $h_n^{\prime}(x)$ si $x\ne0$?

[]{#MA-MSOL-ANM-01-026-053}

<details class="anm-solution">
<summary>Ver solución del microcontrol 53</summary>

Su magnitud es como máximo $1/[1+(n+1)x^2]$, que tiende a cero.

</details>

#### Microcontrol 54

[]{#MA-MIC-ANM-01-026-054}

¿Dónde se alcanza el máximo de $|h_n|$?

[]{#MA-MSOL-ANM-01-026-054}

<details class="anm-solution">
<summary>Ver solución del microcontrol 54</summary>

En $x=\pm1/\sqrt{n+1}$; el valor máximo es $1/[2\sqrt{n+1}]$.

</details>

#### Microcontrol 55

[]{#MA-MIC-ANM-01-026-055}

¿Qué término queda sin control en la prueba triangular de continuidad?

[]{#MA-MSOL-ANM-01-026-055}

<details class="anm-solution">
<summary>Ver solución del microcontrol 55</summary>

$|f(y)-f_n(y)|$ para entradas variables $y$ de una ventana con una sola fila ya escogida.

</details>

#### Microcontrol 56

[]{#MA-MIC-ANM-01-026-056}

¿Qué debe comprobarse antes de comparar dos operaciones de límite?

[]{#MA-MSOL-ANM-01-026-056}

<details class="anm-solution">
<summary>Ver solución del microcontrol 56</summary>

La existencia y el dominio de cada operación interior y exterior, o de cada integral y derivada utilizadas.

</details>

### Ejercicios de la sección 26.7

#### Ejercicio 31. Límite sin integral propia

[]{#MA-EX-ANM-01-026-031}

Con $d_n=\mathbf1_{E_{n+1}}$ de C25, prueba límite puntual y explica qué comparación integral está mal tipada.

[]{#MA-SOL-ANM-01-026-031}

<details class="anm-solution">
<summary>Ver solución del ejercicio 31</summary>

Cada $E_{n+1}$ es finito; su indicadora es integrable con integral0. En un irracional, toda la columna vale0. En un racional irreducible $p/q$, vale1 desde $n+1\ge q$. El límite es Dirichlet, no integrable por C25. Por tanto el límite de las integrales sí existe y vale0, pero no se puede igualar con una integral de Riemann del límite: esa integral no existe. La acotación común0≤d_n≤1 no repara la falta de existencia.

</details>

#### Ejercicio 32. Calcular las derivadas

[]{#MA-EX-ANM-01-026-032}

Para $h_n(x)=x/[1+(n+1)x^2]$ en $\mathbb R$, calcula derivadas y demuestra convergencia puntual de valores y derivadas.

[]{#MA-SOL-ANM-01-026-032}

<details class="anm-solution">
<summary>Ver solución del ejercicio 32</summary>

Pongamos $k=n+1>0$. Cociente y potencia de C18 dan $h_n^{\prime}=(1-kx^2)/(1+kx^2)^2$. En0 los valores son0 y las derivadas1. Para $x\ne0$, $|h_n(x)|\le1/(k|x|)\to0$ y $|h_n^{\prime}(x)|\le1/(1+kx^2)\to0$. Los cortes arquimedianos para esos denominadores controlan cada cola. Así $h_n\to0$ y $h_n^{\prime}\to\mathbf1_{\{0\}}$ puntualmente. La derivada del límite cero es0 y difiere del límite de derivadas en0.

</details>

#### Ejercicio 33. Un máximo exacto de error

[]{#MA-EX-ANM-01-026-033}

Prueba la cota global $|h_n(x)|\le1/[2\sqrt{n+1}]$ y que se alcanza.

[]{#MA-SOL-ANM-01-026-033}

<details class="anm-solution">
<summary>Ver solución del ejercicio 33</summary>

Con $k=n+1$, el cuadrado $(\sqrt{k}|x|-1)^2\ge0$ equivale a $1+kx^2\ge2\sqrt{k}|x|$. Si $x\ne0$, dividir por los factores positivos da la cota; en0 se verifica directamente. Para $x=1/\sqrt{k}$, el denominador es2 y el valor absoluto es1/(2√k), por lo que es el máximo. La cota tiende a0, pero las derivadas en0 siguen valiendo1. El control global de valores por sí solo no autoriza el intercambio de derivadas.

**Retorno visual.** Véase [C26-F07](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html#fig-anm-c26-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 34. Auditar la prueba triangular

[]{#MA-EX-ANM-01-026-034}

En el intento de deducir continuidad del límite puntual de funciones continuas, identifica el paso no autorizado.

[]{#MA-SOL-ANM-01-026-034}

<details class="anm-solution">
<summary>Ver solución del ejercicio 34</summary>

La desigualdad $|f(y)-f(x)|\le|f(y)-f_n(y)|+|f_n(y)-f_n(x)|+|f_n(x)-f(x)|$ es válida. El corte puntual en $x$ controla el último término y continuidad de la fila escogida controla el central en una ventana. Falta controlar el primero para todos los $y$ de esa ventana usando la misma fila: el corte puntual en $y$ puede depender de $y$ y ser mayor que el ya escogido. Las potencias demuestran que esa omisión puede llevar a una conclusión falsa.

</details>

#### Ejercicio 35. Clasificar tres fracasos

[]{#MA-EX-ANM-01-026-035}

Compara potencias, tiendas normalizadas y $d_n$ según qué propiedad falla y qué objetos existen.

[]{#MA-SOL-ANM-01-026-035}

<details class="anm-solution">
<summary>Ver solución del ejercicio 35</summary>

Las potencias tienen filas continuas y límite puntual existente pero discontinuo. Las tiendas normalizadas tienen filas continuas integrables y límite cero integrable; el límite de integrales1 difiere de la integral del límite0. En $d_n$, las filas son integrables con integral0, pero el límite Dirichlet no tiene integral propia; no hay dos valores integrales que comparar. El ejemplo $h_n$ aporta además derivadas puntualmente convergentes que no coinciden con la derivada del límite. Cada afirmación conserva sus hipótesis y su alcance.

</details>
## 26.8. Certificados que recuperan control

[]{#MA-SEC-ANM-01-026-008}

El capítulo ha dado reglas válidas columna por columna y contraejemplos que impiden convertirlas sin más en reglas para toda la función. Podemos recuperar algunos controles mediante hipótesis concretas, sin adelantar los teoremas generales del capítulo siguiente.

### Una estimación común de proximidad pasa al límite

Supongamos que $f_n\to f$ puntualmente en $X$ y que existe $L\ge0$ con
$$
|f_n(x)-f_n(y)|\le L|x-y|
\quad\text{para todo }n\text{ y todo }x,y\in X.
$$
Fijados dos puntos, la regla de diferencias y la continuidad del valor absoluto permiten pasar al límite en el miembro izquierdo. La preservación del orden de §26.3 da
$$
|f(x)-f(y)|\le L|x-y|.
$$
La constante es la misma para todas las filas y pares antes de tomar límites. Esta desigualdad prueba continuidad de $f$: un radio $\delta=\varepsilon/(L+1)$ hace el error menor que $\varepsilon$. Si $L=0$, la estimación dice que todas las filas y el límite son constantes en cualquier dominio no vacío; no se divide por $L$.

Además, para cualquier ruta dada $x_n\in X$ con $x_n\to x\in X$,
$$
|f_n(x_n)-f(x)|
\le L|x_n-x|+|f_n(x)-f(x)|\longrightarrow0.
$$
Para una tolerancia, basta reunir el corte de la ruta para $\varepsilon/[2(L+1)]$ y el corte puntual en $x$ para $\varepsilon/2$. Aquí una hipótesis común ha cerrado el hueco de la diagonal. Las pendientes de las tiendas $t_n$ crecen como $n+3$, por lo que ese ejemplo no tiene una constante $L$ válida para todas sus filas.

### Monotonía por columnas y barreras dependientes de la entrada

Si para cada $x$ la columna $f_n(x)$ es creciente y tiene una cota superior real $M_x$, definimos
$$
f(x)=\sup\{f_n(x):n\in\mathbb N\}.
$$
La imagen es no vacía y acotada antes de aplicar completitud de C03. Para $\varepsilon>0$, existe $j$ con $f_j(x)>f(x)-\varepsilon$: de no existir, $f(x)-\varepsilon$ sería una cota superior menor que el supremo. Para $n\ge j$, la monotonía da
$$
f(x)-\varepsilon<f_j(x)\le f_n(x)\le f(x).
$$
Esto prueba convergencia puntual. Cada fibra tiene un único supremo, por lo que el grafo define $f$ sin seleccionar arbitrariamente cotas $M_x$. No se requiere una misma cota para todas las entradas. La versión decreciente usa el ínfimo y la desigualdad $f_{n+1}(x)\le f_n(x)$.

Para $u_n(x)=\min(n,x)$ en $[0,\infty)$, las columnas son crecientes y acotadas por $x$; el límite es $x$, no acotado en todo el dominio. Si, además, todas las filas tienen una barrera común, el límite la hereda. Que una sucesión sea monótona por columnas no significa que cada fila sea monótona respecto de su variable; son órdenes sobre argumentos distintos.

### Qué debe entregar una prueba

Un certificado puntual identifica dominio común, candidata, entrada fija, tolerancia, corte y control de toda la cola. Una refutación puntual conserva una entrada y una tolerancia mientras produce infracciones tardías. Una refutación de un corte simultáneo puede mover la entrada; una diagonal dada puede demostrar esa obstrucción sin elección numerable. Un intercambio fallido requiere declarar qué operaciones existen, como hicimos con las áreas y derivadas; si la integral del límite no existe, se informa precisamente eso.

En un conjunto finito, el máximo de umbrales resuelve todas las entradas para una tolerancia. En un conjunto infinito, ese máximo puede no existir. Compactitud del dominio, continuidad de las filas, continuidad del límite y una cota común de valores, considerados por separado, no borran las dependencias que los ejemplos han exhibido.

La siguiente pregunta queda bien formulada: ¿qué significa exigir una sola cola para todas las entradas y cómo se mide ese control? C27 dará el contrato y la distancia apropiados. Aquí ya sabemos por qué el cambio de cuantificadores es sustantivo; no usaremos sus resultados para certificar retroactivamente estas pruebas.

![Familia f_n(x)=x+1/(n+1), con constante Lipschitz común L=1 y límite x. En la ruta x_n=1/(n+1), el error hacia f(0) es2/(n+1), suma de distancia de entrada y error puntual. La estimación común, no una muestra finita, justifica el control para cualquier ruta convergente dada.](../../assets/books/anm/C26/C26-F08.svg){#fig-anm-c26-f08 fig-alt="Familia f_n(x)=x+1/(n+1), con constante Lipschitz común L=1 y límite x. En la ruta x_n=1/(n+1), el error hacia f(0) es2/(n+1), suma de distancia de entrada y error puntual. La estimación común, no una muestra finita, justifica el control para cualquier ruta convergente dada."}

### Microcontroles

#### Microcontrol 57

[]{#MA-MIC-ANM-01-026-057}

¿Qué cota común de proximidad pasa al límite puntual?

[]{#MA-MSOL-ANM-01-026-057}

<details class="anm-solution">
<summary>Ver solución del microcontrol 57</summary>

$|f_n(x)-f_n(y)|\le L|x-y|$ con el mismo $L\ge0$ para todas las filas y pares.

</details>

#### Microcontrol 58

[]{#MA-MIC-ANM-01-026-058}

¿Qué radio prueba continuidad del límite bajo esa cota?

[]{#MA-MSOL-ANM-01-026-058}

<details class="anm-solution">
<summary>Ver solución del microcontrol 58</summary>

$\delta=\varepsilon/(L+1)>0$, que incluye el caso $L=0$.

</details>

#### Microcontrol 59

[]{#MA-MIC-ANM-01-026-059}

¿Qué dos errores controlan una diagonal bajo la misma hipótesis?

[]{#MA-MSOL-ANM-01-026-059}

<details class="anm-solution">
<summary>Ver solución del microcontrol 59</summary>

$L|x_n-x|$ y el error puntual $|f_n(x)-f(x)|$ en la entrada fija de destino.

</details>

#### Microcontrol 60

[]{#MA-MIC-ANM-01-026-060}

¿Qué condición de monotonía se refiere al índice?

[]{#MA-MSOL-ANM-01-026-060}

<details class="anm-solution">
<summary>Ver solución del microcontrol 60</summary>

$f_n(x)\le f_{n+1}(x)$ para cada entrada fija; no describe el orden de una fila respecto de $x$.

</details>

#### Microcontrol 61

[]{#MA-MIC-ANM-01-026-061}

¿Qué objeto produce el límite de una columna creciente acotada?

[]{#MA-MSOL-ANM-01-026-061}

<details class="anm-solution">
<summary>Ver solución del microcontrol 61</summary>

El supremo de su imagen no vacía acotada, existente por completitud de C03.

</details>

#### Microcontrol 62

[]{#MA-MIC-ANM-01-026-062}

¿Por qué hay un término mayor que el supremo menos $\varepsilon$?

[]{#MA-MSOL-ANM-01-026-062}

<details class="anm-solution">
<summary>Ver solución del microcontrol 62</summary>

Si no lo hubiera, ese número menor sería una cota superior, contradiciendo la minimalidad del supremo.

</details>

#### Microcontrol 63

[]{#MA-MIC-ANM-01-026-063}

¿Cómo se corrige la desigualdad para columnas decrecientes?

[]{#MA-MSOL-ANM-01-026-063}

<details class="anm-solution">
<summary>Ver solución del microcontrol 63</summary>

Debe ser $f_{n+1}(x)\le f_n(x)$; invertirla describiría columnas crecientes.

</details>

#### Microcontrol 64

[]{#MA-MIC-ANM-01-026-064}

¿Qué pregunta entrega este capítulo a C27?

[]{#MA-MSOL-ANM-01-026-064}

<details class="anm-solution">
<summary>Ver solución del microcontrol 64</summary>

Cómo formular y medir una sola cola que controle todas las entradas, y qué consecuencias permite ese contrato.

</details>

### Ejercicios de la sección 26.8

#### Ejercicio 36. Transportar una cota común de proximidad

[]{#MA-EX-ANM-01-026-036}

Si $f_n\to f$ puntualmente y todas las filas son Lipschitz con la misma constante $L\ge0$, prueba que $f$ lo es y es continua.

[]{#MA-SOL-ANM-01-026-036}

<details class="anm-solution">
<summary>Ver solución del ejercicio 36</summary>

Fijamos $x,y$. Las diferencias numéricas convergen a $f(x)-f(y)$ y sus magnitudes convergen por continuidad del absoluto. El orden eventual aplicado a $|f_n(x)-f_n(y)|\le L|x-y|$ da la misma desigualdad para $f$. Para una tolerancia, $\delta=\varepsilon/(L+1)>0$ hace $L|x-y|<\varepsilon$ si $|x-y|<\delta$. En $L=0$ el error es0 para todos los pares; no se divide por $L$.

</details>

#### Ejercicio 37. Diagonal con presupuesto común

[]{#MA-EX-ANM-01-026-037}

Bajo la hipótesis del ejercicio anterior, si una ruta dada $x_n\to x\in X$ permanece en $X$, prueba $f_n(x_n)\to f(x)$.

[]{#MA-SOL-ANM-01-026-037}

<details class="anm-solution">
<summary>Ver solución del ejercicio 37</summary>

La desigualdad triangular y la cota común dan $|f_n(x_n)-f(x)|\le L|x_n-x|+|f_n(x)-f(x)|$. Para $\varepsilon>0$ reunimos el corte de la ruta con error menor que $\varepsilon/[2(L+1)]$ y el corte puntual en $x$ con error menor que $\varepsilon/2$. Todo índice posterior da error menor que $\varepsilon$. La constante fue común antes de recibir los índices; la ruta está dada y no requiere selección.

</details>

#### Ejercicio 38. Monotonía sin barrera universal

[]{#MA-EX-ANM-01-026-038}

Prueba existencia de límite puntual para columnas crecientes acotadas por una barrera que puede depender de la entrada.

[]{#MA-SOL-ANM-01-026-038}

<details class="anm-solution">
<summary>Ver solución del ejercicio 38</summary>

Para cada $x$, la imagen $\{f_n(x):n\in\mathbb N\}$ es no vacía y tiene cota superior real por hipótesis. C03 da su supremo $s_x$, único. Dada $\varepsilon>0$, algún $j$ cumple $f_j(x)>s_x-\varepsilon$, pues de otro modo ese número sería cota superior. Para $n\ge j$, monotonía da $s_x-\varepsilon<f_n(x)\le s_x$. Esto prueba convergencia. El grafo de los supremos únicos define la función sin elegir arbitrariamente una cota para cada entrada. No se obtiene acotación global del límite.

</details>

#### Ejercicio 39. Monotonía del índice y de la variable

[]{#MA-EX-ANM-01-026-039}

Construye una familia creciente por columnas cuyas filas no sean crecientes ni decrecientes en su variable.

[]{#MA-SOL-ANM-01-026-039}

<details class="anm-solution">
<summary>Ver solución del ejercicio 39</summary>

En $X=[-1,1]$ usamos $f_n(x)=x^2-1/(n+1)$. Para toda entrada fija, el término sustraído disminuye al aumentar el índice, luego la columna aumenta y converge a $x^2$. Cada fila toma el mismo valor en−1 y1 y un valor estrictamente menor en0; por ello no es creciente ni decreciente respecto de $x$ en todo el dominio. La cota superior por columna es $x^2$ y existe además una barrera común de magnitud1. Los dos argumentos ordenados no se pueden intercambiar.

</details>

#### Ejercicio 40. Un certificado y su límite de alcance

[]{#MA-EX-ANM-01-026-040}

Para $f_n(x)=x+1/(n+1)$ en $\mathbb R$, verifica límite puntual, cota Lipschitz común y toda diagonal $x_n\to x$. Compáralo con $t_n$.

[]{#MA-SOL-ANM-01-026-040}

<details class="anm-solution">
<summary>Ver solución del ejercicio 40</summary>

El error respecto de $f(x)=x$ es $1/(n+1)$; el corte de C06 sirve para cualquier entrada. Para todo par, $|f_n(u)-f_n(v)|=|u-v|$, así $L=1$ común. Una ruta dada $x_n\to x$ cumple $|f_n(x_n)-x|\le|x_n-x|+1/(n+1)\to0$. Las tiendas también tienen límite continuo y filas continuas, pero sus pendientes exigen constantes $n+3$ sin barrera común; su ruta central mantiene salida1. La prueba positiva identifica una hipótesis concreta que el contraejemplo no satisface.

**Retorno visual.** Véase [C26-F08](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html#fig-anm-c26-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-26)

[← Capítulo 25](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html) · [Capítulo 27 →](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez.html)
