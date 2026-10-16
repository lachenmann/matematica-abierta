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
date-modified: '2026-10-16'
provenance:
  type: original
  sources:
  - ANM-C26.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-26)

La familia $f_n(x)=x/(n+1)$ tiende a cero en cada entrada real fija, aunque en toda etapa podamos encontrar una entrada donde su valor sea uno. Para entender esa diferencia, consideraremos cada columna como una sucesión numérica de C06 y mantendremos visible qué puede depender de la entrada. C12–C14 aportan funciones, límites y continuidad; la arquimedianidad de C03 y las herramientas de C18 y C23–C25 se utilizarán con sus hipótesis en los ejemplos.

## 26.1. Dos índices, dos maneras de mirar

[]{#MA-SEC-ANM-01-026-001}

Una sucesión numérica entrega un número para cada índice. Ahora cada índice entrega una función completa. El dominio permanece fijo: sea $X\subseteq\mathbb R$, y para cada $n\in\mathbb N=\{0,1,2,\ldots\}$ sea $f_n:X\to\mathbb R$. El número $f_n(x)$ tiene dos argumentos de naturaleza distinta: $n$ ordena las etapas; $x$ señala una entrada del dominio. Cambiar el dominio entre etapas impide comparar columnas sin declarar antes una restricción común.

### Construir el objeto sin confundir sus representaciones

Por la teoría elemental de conjuntos y funciones declarada en C12, la colección $\mathcal F(X,\mathbb R)$ existe: sus elementos son los subconjuntos de $X\times\mathbb R$ que satisfacen existencia y unicidad de salida. Una sucesión de funciones es una aplicación $\mathbb N\to\mathcal F(X,\mathbb R)$. Equivalentemente, podemos dar una sola función
$$
F:\mathbb N\times X\to\mathbb R,\qquad F(n,x)=f_n(x).
$$
En la ida, la evaluación produce una salida única; en la vuelta, la sección $x\mapsto F(n,x)$ produce cada función. No se elige una salida entre varias. El grafo reúne pares con salidas ya únicas.

Hay dos maneras de recorrer el mismo objeto. Al fijar $n$ obtenemos la fila $f_n$, cuya gráfica tiene entrada $x$ y salida real. Al fijar $x$ obtenemos una columna, la sucesión numérica $n\mapsto f_n(x)$, donde el eje horizontal representa ahora índices. Distinguir estos ejes evita atribuir a la función completa lo que sólo hemos comprobado para una entrada.

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

### Ejercicios de la sección 26.1

[]{#ejercicios-26}

#### Ejercicio 1. Fila y columna

[]{#MA-EX-ANM-01-026-001}

Para $F(n,x)=(n+1)x$ en $\mathbb N\times\mathbb R$, identifica filas, columnas y las entradas donde hay límite real.

[]{#MA-SOL-ANM-01-026-001}

<details class="anm-solution">
<summary>Ver solución del ejercicio 1</summary>

La fila $n$ es $f_n:x\mapsto(n+1)x$ sobre $\mathbb R$; la columna $x$ es la sucesión $((n+1)x)_{n\ge0}$. En $x=0$ todos los valores son cero. Si $x\ne0$, sus magnitudes $(n+1)|x|$ exceden cualquier $M>0$ desde un índice con $n+1>M/|x|$. La columna es entonces no acotada y no puede converger a un real, pues C06 hace acotada toda sucesión convergente. Para $x>0$ crece sin cota superior y para $x<0$ decrece sin cota inferior. El conjunto de convergencia real es exactamente $\{0\}$ y la función límite sobre él vale cero.

**Retorno visual.** Véase [C26-F01](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html#fig-anm-c26-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 2. El dominio que se conserva

[]{#MA-EX-ANM-01-026-002}

Las fórmulas $f_n(x)=1/(x-n)$ tienen dominio $\mathbb R\setminus\{n\}$. Encuentra un dominio común y el límite allí.

[]{#MA-SOL-ANM-01-026-002}

<details class="anm-solution">
<summary>Ver solución del ejercicio 2</summary>

Como los índices son $\mathbb N=\{0,1,2,\ldots\}$, la intersección de los dominios es $X=\mathbb R\setminus\mathbb N$. En ese conjunto cada denominador $x-n$ es no nulo para todo índice. Fijados $x\in X$ y $\varepsilon>0$, elegimos un natural $N>|x|+1/\varepsilon$. Para $n\ge N$, la triangular inversa da $|x-n|\ge n-|x|>1/\varepsilon$, así $|1/(x-n)|<\varepsilon$. Las restricciones convergen puntualmente a cero en $X$. Éste es el mayor dominio común de las fórmulas dadas; podrían elegirse subconjuntos suyos, pero incluir un natural exigiría declarar cómo se repara su fila singular.

</details>

#### Ejercicio 3. Alternancia dependiente de la entrada

[]{#MA-EX-ANM-01-026-003}

Calcula el conjunto de convergencia de $f_n(x)=(-1)^n(x-2)$ en $\mathbb R$.

[]{#MA-SOL-ANM-01-026-003}

<details class="anm-solution">
<summary>Ver solución del ejercicio 3</summary>

En $x=2$ todos los valores de la columna son cero. Para $x\ne2$, los índices pares tienen altura $x-2$ y los impares altura $2-x$. Si hubiera un límite real, ambas subsucesiones deberían converger a él por C06. Son constantes y sus valores son distintos, de modo que la unicidad lo hace imposible. El conjunto de convergencia es $\{2\}$ y la función límite allí vale cero. La alternancia no depende de una etapa inicial excepcional: sigue produciendo ambos valores en índices arbitrariamente tardíos.

</details>

#### Ejercicio 4. Grafo del límite

[]{#MA-EX-ANM-01-026-004}

Explica por qué la existencia de límite real en cada columna de $X$ define una función sin escoger un límite arbitrario por entrada.

[]{#MA-SOL-ANM-01-026-004}

<details class="anm-solution">
<summary>Ver solución del ejercicio 4</summary>

Definimos $G=\{(x,y)\in X\times\mathbb R:f_n(x)\to y\}$. La hipótesis de convergencia de cada columna proporciona al menos un $y$ para cada entrada. La unicidad del límite numérico proporciona a lo sumo uno. Por tanto $G$ es total y univaluada sobre $X$, y define una función $f:X\to\mathbb R$. La salida está determinada por una propiedad que tiene un único valor, sin elegir entre alternativas por entrada. Si $X$ es vacío, el mismo procedimiento produce el único grafo vacío.

</details>

#### Ejercicio 5. Toda entrada salvo una

[]{#MA-EX-ANM-01-026-005}

Define $f_n(x)=1$ si $x=n$ y $0$ en otro caso, en $\mathbb R$. Determina su límite y explica por qué las gráficas no bastan.

[]{#MA-SOL-ANM-01-026-005}

<details class="anm-solution">
<summary>Ver solución del ejercicio 5</summary>

Si $x\notin\mathbb N$, ninguna fila tiene su pico en esa entrada y la columna es cero desde el inicio. Si $x=m\in\mathbb N$, el único término de altura uno es el de índice $m$; desde $N=m+1$ toda la cola es cero. Así $f_n(x)\to0$ para cada $x\in\mathbb R$. Cada fila contiene un pico de altura uno, pero éste aparece en una entrada diferente al aumentar el índice. El argumento clasifica una entrada arbitraria y controla su cola completa; unas pocas gráficas no certificarían esa afirmación universal.

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

Aunque la definición permite que el corte dependa de la entrada, no obliga a que sea diferente en cada una. Para una tolerancia y un conjunto finito $A=\{x_1,\ldots,x_m\}$, podemos reunir los cortes puntuales y tomar su máximo. Toda cola posterior satisface las $m$ obligaciones a la vez. Si $A$ es vacío, cualquier corte sirve. La finitud es lo que permite esta operación; una familia infinita de umbrales puede no tener un máximo natural.

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

Para la familia $(-1)^n x$ y la candidata cero, la entrada fija $x=1$ conserva error uno en todo índice. Con $\varepsilon_0=1/2$ refutamos la convergencia puntual. En cambio, para $x/(n+1)$ podemos lograr el mismo error tomando $x_n=n+1$, pero ya hemos cambiado la entrada con la etapa. Esa ruta no contradice la prueba para cada columna fija; muestra que sus cortes no controlan simultáneamente toda la recta.

### Umbrales mínimos sin elegir infinitamente

Para cada par $(x,\varepsilon)$, el conjunto
$$
H(x,\varepsilon)=\{N\in\mathbb N:\forall n\ge N,\
|f_n(x)-f(x)|<\varepsilon\}
$$
es no vacío cuando hay convergencia puntual. El buen orden de los naturales da su mínimo $\tau(x,\varepsilon)$. Esta regla es única y define una función sobre los pares autorizados. Si $\varepsilon$ disminuye, las obligaciones se vuelven más fuertes y el umbral mínimo no puede disminuir. Una fórmula suficiente de corte puede ser mayor que $\tau$; minimalidad y validez son preguntas distintas.

![Para x/(n+1) y tolerancia1/4, el umbral mínimo en las entradas no negativas mostradas es piso(4x). En cambio, la entrada móvil x_n=n+1 produce error1 en toda etapa. Esa ruta no refuta la convergencia puntual.](../../assets/books/anm/C26/C26-F02.svg){#fig-anm-c26-f02 fig-alt="Para x/(n+1) y tolerancia1/4, el umbral mínimo en las entradas no negativas mostradas es piso(4x). En cambio, la entrada móvil x_n=n+1 produce error1 en toda etapa. Esa ruta no refuta la convergencia puntual."}

### Ejercicios de la sección 26.2

#### Ejercicio 6. Certificado explícito

[]{#MA-EX-ANM-01-026-006}

Da un corte para $f_n(x)=(x^2+1)/(n+1)\to0$ en $\mathbb R$ con error estricto menor que $\varepsilon$.

[]{#MA-SOL-ANM-01-026-006}

<details class="anm-solution">
<summary>Ver solución del ejercicio 6</summary>

Fijamos $x\in\mathbb R$ y $\varepsilon>0$. El numerador $x^2+1$ es positivo. Por arquimedianidad elegimos un natural $N>(x^2+1)/\varepsilon$. Para cualquier $n\ge N$, se tiene $0<(x^2+1)/(n+1)\le(x^2+1)/(N+1)<\varepsilon$. El corte sirve para toda la cola y depende sólo de los desafíos recibidos, la entrada y la tolerancia. Se obtiene convergencia puntual a cero en toda la recta.

</details>

#### Ejercicio 7. Negar en el orden correcto

[]{#MA-EX-ANM-01-026-007}

Escribe la negación de convergencia puntual hacia una candidata $f$ y úsala para refutar $f_n(x)=(-1)^n$ hacia cero en un dominio no vacío.

[]{#MA-SOL-ANM-01-026-007}

<details class="anm-solution">
<summary>Ver solución del ejercicio 7</summary>

La negación hacia una candidata fija $f$ es $\exists x\in X\ \exists\varepsilon_0>0\ \forall N\in\mathbb N\ \exists n\ge N:\ |f_n(x)-f(x)|\ge\varepsilon_0$. Para la candidata cero y $f_n(x)=(-1)^n$, fijamos cualquier entrada del dominio no vacío y $\varepsilon_0=1/2$. Ante cada corte $N$, el índice $n=N$ tiene error uno, así infringe la obligación. La entrada permanece fija y la refutación sí es puntual. La familia tampoco converge a otra candidata real en esa entrada, porque las subsucesiones constantes uno y menos uno no podrían compartir un límite.

</details>

#### Ejercicio 8. Un infractor móvil

[]{#MA-EX-ANM-01-026-008}

Para $f_n(x)=x/(n+1)$ en $\mathbb R$, elige ante cada corte una entrada con error1. ¿Qué queda refutado?

[]{#MA-SOL-ANM-01-026-008}

<details class="anm-solution">
<summary>Ver solución del ejercicio 8</summary>

El límite puntual es cero: para cada entrada fija, un corte $N>|x|/\varepsilon$ controla $|x|/(n+1)$ en toda la cola. Para refutar un corte simultáneo, fijamos tolerancia $1/2$. Ante cualquier $N$, tomamos $n=N$ y $x=N+1$, obteniendo $|f_N(x)|=1$. Se demuestra $\forall N\ \exists x\ \exists n\ge N$ con error grande. La entrada se elige después del corte, de modo que esa afirmación no es la negación del contrato puntual, cuyo infractor tendría que ser una misma entrada para todos los cortes.

**Retorno visual.** Véase [C26-F02](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html#fig-anm-c26-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 9. Reunión finita de obligaciones

[]{#MA-EX-ANM-01-026-009}

Para $f_n(x)=x/(n+1)$ y $A=\{-3,0,5\}$, produce un corte simultáneo y justifica la generalización a un conjunto finito.

[]{#MA-SOL-ANM-01-026-009}

<details class="anm-solution">
<summary>Ver solución del ejercicio 9</summary>

En $A=\{-3,0,5\}$, todas las magnitudes de entrada están acotadas por cinco. Un natural $N>5/\varepsilon$ da, para todo $n\ge N$ y todo $x\in A$, $|f_n(x)|\le5/(N+1)<\varepsilon$. Para una familia puntualmente convergente cualquiera sobre un conjunto finito, la tolerancia fija proporciona un corte por cada entrada. Se construye esa lista finita de cortes y se toma su máximo; cualquier índice posterior cumple todas las obligaciones. En el vacío sirve cero. La extensión a infinitas entradas necesitaría demostrar que sus umbrales tienen una barrera natural común.

</details>

#### Ejercicio 10. Umbral mínimo

[]{#MA-EX-ANM-01-026-010}

Para $f_n(x)=x/(n+1)$ calcula $\tau(x,\varepsilon)$ y comprueba la frontera estricta.

[]{#MA-SOL-ANM-01-026-010}

<details class="anm-solution">
<summary>Ver solución del ejercicio 10</summary>

Sea $r=|x|/\varepsilon\ge0$. Como el error $|x|/(n+1)$ no aumenta con $n$, un corte $N$ es válido exactamente cuando $N+1>r$. Ponemos $m=\lfloor r\rfloor$, caracterizado por $m\le r<m+1$. El corte $N=m$ cumple la desigualdad estricta. Si un natural $N<m$, entonces $N+1\le m\le r$, de modo que ya el error en ese índice es al menos $\varepsilon$ y falla. Por tanto $\tau(x,\varepsilon)=\lfloor|x|/\varepsilon\rfloor$, incluido $x=0$, donde el mínimo es cero. Cuando $r$ es un entero positivo, el índice anterior da error exactamente igual a $\varepsilon$, que no satisface el contrato estricto.

</details>

## 26.3. Lo que se transporta columna por columna

[]{#MA-SEC-ANM-01-026-003}

Para estudiar las operaciones fijamos primero una entrada $x$. Cada familia se convierte entonces en una sucesión de números reales y podemos aplicar las reglas de C06. Reconstruiremos las estimaciones para distinguir las constantes y cortes que dependen de esa entrada de los que, bajo otra hipótesis, podrían valer en todo el dominio.

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

La convergencia numérica en una columna proporciona una cota para todos sus términos: acotamos una cola y tomamos después el máximo con los finitísimos términos iniciales. Así, para cada $x$ existe $B_x$ con $|f_n(x)|\le B_x$ para todo $n$. Esa barrera puede crecer al cambiar $x$. También puede ocurrir que cada fila esté acotada y que sus cotas crezcan con $n$. Ninguna de esas afirmaciones produce por sí sola una constante para todas las filas y entradas.

En $[0,\infty)$, $u_n(x)=\min(n,x)$ converge a $u(x)=x$: para $n\ge x$ ya coincide. Cada fila está acotada por $n$, pero el límite no está acotado. En cambio, si $|f_n(x)|\le B$ para todos $n,x$, la preservación del orden da $|f(x)|\le B$ para todo $x$. La posición de la constante dentro o fuera de los cuantificadores determina qué puede heredarse.

![Filas u_n(x)=min(n,x), aquí restringidas a la ventana0≤x≤6 para dibujar. Cada fila tiene barrera n; cada columna tiene barrera x. El límite en todo\[0,∞) es x, no acotado. La ventana finita no demuestra la falta de cota global.](../../assets/books/anm/C26/C26-F03.svg){#fig-anm-c26-f03 fig-alt="Filas u_n(x)=min(n,x), aquí restringidas a la ventana0≤x≤6 para dibujar. Cada fila tiene barrera n; cada columna tiene barrera x. El límite en todo[0,∞) es x, no acotado. La ventana finita no demuestra la falta de cota global."}

### Ejercicios de la sección 26.3

#### Ejercicio 11. Dos errores y una cota

[]{#MA-EX-ANM-01-026-011}

Prueba directamente que el producto de dos familias puntualmente convergentes converge al producto de sus límites.

[]{#MA-SOL-ANM-01-026-011}

<details class="anm-solution">
<summary>Ver solución del ejercicio 11</summary>

Fijamos una entrada $x$ y abreviamos $f(x)=a$, $g(x)=b$. La convergencia de la primera columna da un corte de acotación con $|f_n(x)|\le B=|a|+1$. Usamos la identidad $f_ng_n-ab=f_n(g_n-b)+b(f_n-a)$. Su magnitud no supera $B|g_n-b|+|b||f_n-a|$. Pedimos a la segunda columna error menor que $\varepsilon/[2(B+1)]$ y a la primera menor que $\varepsilon/[2(|b|+1)]$. El máximo de esos dos cortes y el de acotación garantiza que la suma anterior es menor que $\varepsilon$, pues cada coeficiente sobre su denominador más uno es menor que uno. La entrada era arbitraria, así el producto converge puntualmente a $fg$. No se necesitó una cota global de las familias.

</details>

#### Ejercicio 12. Ceros por filas

[]{#MA-EX-ANM-01-026-012}

En $X=(0,1]$ sea $g_n(x)=x-1/(n+1)$. Prueba convergencia puntual y explica por qué $1/g_n$ no define una familia en todo $X$.

[]{#MA-SOL-ANM-01-026-012}

<details class="anm-solution">
<summary>Ver solución del ejercicio 12</summary>

Para $x\in(0,1]$, $|g_n(x)-x|=1/(n+1)\to0$, así el límite puntual es $g(x)=x>0$. Sin embargo, cada fila se anula en $x_n=1/(n+1)$, que pertenece al dominio. Por eso $1/g_n$ no define una función real en todo $X$ en ninguna etapa. Un dominio común posible para los recíprocos es $Y=X\setminus\{1/(n+1):n\in\mathbb N\}$. En una entrada fija de $Y$, desde un corte con $1/(n+1)<x/2$ tenemos $g_n(x)>x/2$. Entonces $|1/g_n(x)-1/x|=|x-g_n(x)|/(x|g_n(x)|)\le2/[x^2(n+1)]\to0$. La barrera eventual justifica el límite, mientras la restricción común justifica la existencia de todas las filas.

</details>

#### Ejercicio 13. Orden eventual

[]{#MA-EX-ANM-01-026-013}

Si $f_n\to f$, $g_n\to g$ puntualmente y para cada $x$ hay un corte con $f_n(x)\le g_n(x)$ después de él, demuestra $f\le g$.

[]{#MA-SOL-ANM-01-026-013}

<details class="anm-solution">
<summary>Ver solución del ejercicio 13</summary>

Fijemos $x$ y supongamos por contradicción que $d=f(x)-g(x)>0$. Reunimos los cortes para errores menores que $d/3$ de ambas columnas y el corte a partir del que se cumple su orden. En cualquier índice posterior, $f_n(x)>f(x)-d/3$ y $g_n(x)<g(x)+d/3$, así $f_n(x)-g_n(x)>d-2d/3=d/3>0$. Esto contradice $f_n(x)\le g_n(x)$. Por tanto $f(x)\le g(x)$ para toda entrada. La estrictitud no pasa automáticamente: las columnas $1/(n+1)>0$ y cero tienen el mismo límite cero.

</details>

#### Ejercicio 14. Filas acotadas, límite sin cota

[]{#MA-EX-ANM-01-026-014}

Analiza $u_n(x)=\min(n,x)$ en $[0,\infty)$ respecto de acotación de filas, columnas, límite y familia completa.

[]{#MA-SOL-ANM-01-026-014}

<details class="anm-solution">
<summary>Ver solución del ejercicio 14</summary>

Para cada $n$, la fila $u_n$ satisface $0\le u_n(x)\le n$ en todo $[0,\infty)$, así está acotada. Para cada entrada fija $x$, su columna satisface $0\le u_n(x)\le x$ y desde cualquier natural $N>x$ coincide con $x$. Por tanto su límite es $u(x)=x$. Esta función no tiene cota superior en todo el dominio. Tampoco hay una barrera común para toda la familia: dado $B\ge0$, elegimos un natural $n>B$ y tomamos $x=n$, obteniendo $u_n(n)=n>B$. Las cotas por filas y por columnas son válidas, pero dependen de argumentos diferentes y ninguna proporciona esa barrera global.

**Retorno visual.** Véase [C26-F03](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html#fig-anm-c26-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 15. Componer dentro del tipo

[]{#MA-EX-ANM-01-026-015}

Si $f_n\to f$ puntualmente y todos sus valores y los de $f$ son no negativos, demuestra $\sqrt{f_n}\to\sqrt f$ sin suponer continuidad de las filas.

[]{#MA-SOL-ANM-01-026-015}

<details class="anm-solution">
<summary>Ver solución del ejercicio 15</summary>

Para una entrada fija, escribimos $u_n=f_n(x)\ge0$ y $u=f(x)\ge0$. Sus raíces reales están definidas. Si $u_n\ge u$, la diferencia de raíces es no negativa y $u_n-u=(\sqrt{u_n}-\sqrt u)(\sqrt{u_n}+\sqrt u)\ge(\sqrt{u_n}-\sqrt u)^2$. Intercambiar los dos valores cubre el orden inverso, así $|\sqrt{u_n}-\sqrt u|^2\le|u_n-u|$. Para $\varepsilon>0$, la convergencia de la columna da una cola con $|u_n-u|<\varepsilon^2$, luego el error de raíces es menor que $\varepsilon$. Esto también cubre $u=0$. Sólo se usa el control de la columna y la operación raíz, sin continuidad de las filas.

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

Para $x<1$, un radio menor que $1-x$ mantiene las entradas en la región donde $p$ es constante, por lo que el límite es continuo allí. En uno ocurre lo contrario: dado cualquier $\delta>0$, tomamos $d=\min(\delta/2,1/2)>0$ e $y=1-d$. Se cumple $0<|y-1|<\delta$ y la diferencia de salidas es uno. Ningún radio sirve para la tolerancia $1/2$. Las filas continuas tienen, por tanto, un límite puntual discontinuo, incluso sobre este dominio compacto.

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

![Potencias en\[0,1\], con p0=1. El límite vale0 antes de1, punto abierto allí, y1 en1, punto cerrado. La ruta x_n=1−1/\[2(n+1)\] mantiene error mayor que1/2 mediante Bernoulli, aunque toda columna interior converge a cero.](../../assets/books/anm/C26/C26-F04.svg){#fig-anm-c26-f04 fig-alt="Potencias en[0,1], con p0=1. El límite vale0 antes de1, punto abierto allí, y1 en1, punto cerrado. La ruta x_n=1−1/[2(n+1)] mantiene error mayor que1/2 mediante Bernoulli, aunque toda columna interior converge a cero."}

### Ejercicios de la sección 26.4

#### Ejercicio 16. Potencias y extremos

[]{#MA-EX-ANM-01-026-016}

Demuestra el límite puntual de $p_0=1$, $p_n(x)=x^n$ para $n\ge1$, en $[0,1]$, sin logaritmos.

[]{#MA-SOL-ANM-01-026-016}

<details class="anm-solution">
<summary>Ver solución del ejercicio 16</summary>

La recurrencia declara $p_0=1$. En cero, $p_n(0)=0$ para $n\ge1$, así el límite es cero; en uno, todos los términos son uno. Si $0<x<1$, ponemos $t=1/x-1>0$. Bernoulli, probado por inducción, da $(1+t)^n\ge1+nt$, luego $0<p_n(x)=x^n\le1/(1+nt)$. Para $\varepsilon>0$, un natural $N>1/(\varepsilon t)$ hace esta cota menor que $\varepsilon$ para todos los índices posteriores. Por tanto el límite puntual vale cero en $[0,1)$ y uno en el extremo uno. La prueba mantiene la entrada fija y no usa logaritmos.

</details>

#### Ejercicio 17. Discontinuidad relativa

[]{#MA-EX-ANM-01-026-017}

Refuta continuidad del límite de las potencias en1 con un testigo para cada radio.

[]{#MA-SOL-ANM-01-026-017}

<details class="anm-solution">
<summary>Ver solución del ejercicio 17</summary>

Sea $p$ el límite, con $p(1)=1$ y $p(y)=0$ para $y<1$. Fijamos tolerancia $1/2$. Para cualquier $\delta>0$, tomamos $d=\min(\delta/2,1/2)>0$ y $y=1-d$. Entonces $y\in[0,1)$ y $0<|y-1|=d<\delta$, pero $|p(y)-p(1)|=1$. Ningún radio cumple continuidad relativa en uno. En un centro $x<1$, en cambio, un radio menor que $1-x$ evita el punto excepcional y deja la función constante cero. La discontinuidad nueva está exactamente en el extremo uno.

</details>

#### Ejercicio 18. Una infracción en cada etapa

[]{#MA-EX-ANM-01-026-018}

Con $x_n=1-1/[2(n+1)]$, prueba $p_n(x_n)>1/2$ y determina el alcance de la conclusión.

[]{#MA-SOL-ANM-01-026-018}

<details class="anm-solution">
<summary>Ver solución del ejercicio 18</summary>

Para cada $n\ge0$, la entrada $x_n=1-1/[2(n+1)]$ está entre cero y uno. La versión de Bernoulli $(1-s)^n\ge1-ns$ para $0\le s\le1$ da $p_n(x_n)\ge1-n/[2(n+1)]=(n+2)/[2(n+1)]>1/2$; para $n=0$ la fila inicial vale uno. Como el límite en $x_n<1$ es cero, el error supera $1/2$ en cada etapa. Ante cualquier corte común sirve la infracción de esa misma etapa. Sin embargo, las entradas varían con el índice y se aproximan a uno. El resultado refuta control simultáneo en todo el dominio, conservando la convergencia de cada columna fija.

**Retorno visual.** Véase [C26-F04](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html#fig-anm-c26-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 19. Cambiar el dominio

[]{#MA-EX-ANM-01-026-019}

Compara las potencias en $[0,c]$, $0<c<1$, y en $[0,1)$.

[]{#MA-SOL-ANM-01-026-019}

<details class="anm-solution">
<summary>Ver solución del ejercicio 19</summary>

En $[0,c]$, con $0<c<1$, el límite puntual es cero. Para $n\ge1$ y todas las entradas de ese segmento, $p_n(x)\le c^n\le1/[1+n(1/c-1)]$. Un natural $N>1/[\varepsilon(1/c-1)]$, también positivo, controla toda la cola y todas las entradas a la vez. En $[0,1)$, el límite sigue siendo cero, pero las entradas $x_n=1-1/[2(n+1)]$ pertenecen al dominio y tienen error mayor que $1/2$ en cada etapa. Allí no existe un corte simultáneo para esa tolerancia. La candidata es continua en ambos dominios; la pérdida de separación respecto del borde uno cambia el control global.

</details>

#### Ejercicio 20. Dominio ampliado

[]{#MA-EX-ANM-01-026-020}

Calcula el conjunto de convergencia real de la misma familia de potencias en $[-1,1]$.

[]{#MA-SOL-ANM-01-026-020}

<details class="anm-solution">
<summary>Ver solución del ejercicio 20</summary>

Si $|x|<1$, para $n\ge1$ tenemos $|p_n(x)|=|x|^n$. La prueba geométrica anterior aplicada a $|x|$ da límite cero, con el caso $x=0$ tratado por la recurrencia. En $x=1$, todos los valores son uno. En $x=-1$, las subsucesiones pares e impares son constantes uno y menos uno, así la columna no tiene límite real. Por tanto el conjunto de convergencia en $[-1,1]$ es $(-1,1]$. La función límite sobre él vale cero en $(-1,1)$ y uno en el extremo uno. La familia no converge puntualmente en todo el dominio ampliado porque falla la nueva columna de menos uno.

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

En la capa racional, el límite ya pierde continuidad en el origen. El ejemplo siguiente separará esa pérdida del problema de las diagonales: tendrá límite cero continuo, pero una ruta de entradas podrá seguir un pico de altura uno. Más adelante comprobaremos cómo una misma estimación Lipschitz para todas las filas sí permite controlar una ruta convergente.

![Capa a_n(x)=(n+1)x/\[1+(n+1)x\]. Las rutas1/(n+1),1/(n+1)^2 y1/√(n+1) llegan a0 pero sus salidas tienden a1/2,0 y1. Los límites iterados en entrada e índice dan0 y1; las curvas son representaciones de fórmulas probadas.](../../assets/books/anm/C26/C26-F05.svg){#fig-anm-c26-f05 fig-alt="Capa a_n(x)=(n+1)x/[1+(n+1)x]. Las rutas1/(n+1),1/(n+1)^2 y1/√(n+1) llegan a0 pero sus salidas tienden a1/2,0 y1. Los límites iterados en entrada e índice dan0 y1; las curvas son representaciones de fórmulas probadas."}

### Ejercicios de la sección 26.5

#### Ejercicio 21. Capa racional

[]{#MA-EX-ANM-01-026-021}

Para $a_n(x)=(n+1)x/[1+(n+1)x]$ en $[0,1]$, prueba el límite y su fallo de continuidad en0.

[]{#MA-SOL-ANM-01-026-021}

<details class="anm-solution">
<summary>Ver solución del ejercicio 21</summary>

Los denominadores son al menos uno en $[0,1]$, así cada fila está definida y es continua. En cero, $a_n(0)=0$ para todo $n$. Para una entrada fija $x>0$, $|a_n(x)-1|=1/[1+(n+1)x]\le1/[(n+1)x]$. Un natural $N>1/(\varepsilon x)$ controla este error en toda la cola. El límite $a$ vale cero en cero y uno en las entradas positivas. Con tolerancia $1/2$, ante cualquier $\delta>0$ tomamos $y=\min(\delta/2,1/2)>0$; pertenece al dominio, queda a distancia menor que $\delta$ del origen y tiene $|a(y)-a(0)|=1$. Así el límite no es continuo relativamente en cero.

</details>

#### Ejercicio 22. Dos rutas, dos destinos

[]{#MA-EX-ANM-01-026-022}

Calcula $a_n(1/(n+1))$ y $a_n(1/(n+1)^2)$ y explica por qué no contradicen el límite puntual.

[]{#MA-SOL-ANM-01-026-022}

<details class="anm-solution">
<summary>Ver solución del ejercicio 22</summary>

Ambas rutas permanecen en $[0,1]$ y tienden a cero. En la primera, $(n+1)/(n+1)=1$, así $a_n(1/(n+1))=1/2$ para todo índice. En la segunda, el producto de escala es $1/(n+1)$ y $a_n(1/(n+1)^2)=[1/(n+1)]/[1+1/(n+1)]=1/(n+2)\to0$. Sus destinos de salida son, por tanto, distintos. El límite puntual fija $x$ antes de variar $n$; ninguna de estas rutas es una columna fija. Sus resultados muestran cómo la elección simultánea de entrada e índice puede retener comportamientos que el contrato puntual no controla.

**Retorno visual.** Véase [C26-F05](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html#fig-anm-c26-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 23. Una escala intermedia

[]{#MA-EX-ANM-01-026-023}

Para $w_n=1/\sqrt{n+1}$ calcula el destino de $a_n(w_n)$ y justifica las raíces y la convergencia.

[]{#MA-SOL-ANM-01-026-023}

<details class="anm-solution">
<summary>Ver solución del ejercicio 23</summary>

Como $n+1\ge1$, existe su raíz positiva y satisface $\sqrt{n+1}\ge1$, así $w_n=1/\sqrt{n+1}\in(0,1]$. Para cualquier $\varepsilon>0$, desde $n+1>1/\varepsilon^2$ se tiene $w_n<\varepsilon$, por lo que la ruta tiende a cero. Usando $n+1=(\sqrt{n+1})^2$, el producto $(n+1)w_n$ es $\sqrt{n+1}$. Entonces $a_n(w_n)=\sqrt{n+1}/(1+\sqrt{n+1})$ y su error respecto de uno es $1/(1+\sqrt{n+1})\le w_n\to0$. El destino de esta escala intermedia es uno.

</details>

#### Ejercicio 24. Límites iterados

[]{#MA-EX-ANM-01-026-024}

Calcula las dos operaciones iteradas en $n\to\infty$ y $x\to0^+$ para $a_n$.

[]{#MA-SOL-ANM-01-026-024}

<details class="anm-solution">
<summary>Ver solución del ejercicio 24</summary>

Fijado $n$, la fila es continua en cero y su valor allí es cero. Por tanto $\lim_{x\to0^+}a_n(x)=0$, y el límite en $n$ de esa sucesión constante es cero. En el orden contrario, para cada entrada positiva fija ya se probó $\lim_{n\to\infty}a_n(x)=1$. La función resultante sobre $(0,1]$ es constante uno, así su límite por $x\to0^+$ es uno. Las dos operaciones iteradas existen y dan $\lim_n\lim_{x\to0^+}a_n(x)=0$ y $\lim_{x\to0^+}\lim_n a_n(x)=1$. Su diferencia muestra que el orden de operaciones no puede intercambiarse con la sola convergencia puntual.

</details>

#### Ejercicio 25. Reparar un prefijo fuera del dominio

[]{#MA-EX-ANM-01-026-025}

Para $c>0$ construye una ruta en $[0,1]$ que coincida eventualmente con $c/(n+1)$ y calcula las salidas de $a_n$.

[]{#MA-SOL-ANM-01-026-025}

<details class="anm-solution">
<summary>Ver solución del ejercicio 25</summary>

Para $c>0$, definimos $x_n=\min(1,c/(n+1))$. Cada entrada pertenece a $(0,1]$. Elegimos un natural $N>c$; para $n\ge N$, se tiene $c/(n+1)<1$ y la ruta coincide con la fórmula requerida. Esa cola tiende a cero, así toda la ruta también. En ella $(n+1)x_n=c$ y $a_n(x_n)=c/(1+c)$ exactamente. Las salidas iniciales pueden ser distintas, pero su prefijo finito no cambia el límite $c/(1+c)$. La reparación permite evaluar todas las etapas aunque $c>1$.

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

La altura común de $t_n$ deja que sus integrales disminuyan con la anchura; al multiplicar por $k$, la familia $b_n$ compensa exactamente esa disminución. En ambas, cada columna termina en cero y queda acotada por su prefijo finito, pero las cotas de las filas de $b_n$ crecen. La ruta explícita $z_n=2/(n+3)$ sigue las alturas máximas en todo índice y distingue esos controles que una tabla finita podría confundir.

![Tiendas con k=n+3, soporte\[1/k,3/k\] dentro\[0,1\]. Altura1 y área1/k a la izquierda; altura k y área1 a la derecha. Ambas familias convergen puntualmente a cero; seguir2/k mantiene el pico. No se infiere el área desde el dibujo: se calculó por ramas.](../../assets/books/anm/C26/C26-F06.svg){#fig-anm-c26-f06 fig-alt="Tiendas con k=n+3, soporte[1/k,3/k] dentro[0,1]. Altura1 y área1/k a la izquierda; altura k y área1 a la derecha. Ambas familias convergen puntualmente a cero; seguir2/k mantiene el pico. No se infiere el área desde el dibujo: se calculó por ramas."}

### Ejercicios de la sección 26.6

#### Ejercicio 26. Tiendas continuas

[]{#MA-EX-ANM-01-026-026}

Para $k=n+3$ demuestra continuidad, soporte y convergencia puntual a cero de $t_n(x)=\max(0,1-|kx-2|)$ en $[0,1]$.

[]{#MA-SOL-ANM-01-026-026}

<details class="anm-solution">
<summary>Ver solución del ejercicio 26</summary>

Con $k=n+3\ge3$, la composición afín $kx-2$, su valor absoluto y el máximo con cero son continuos, por las reglas de C14. Por tanto $t_n$ es continua en $[0,1]$. Su altura es positiva si y sólo si $|kx-2|<1$, equivalente a $1/k<x<3/k$; en los dos extremos vale cero y fuera también. El soporte cerrado es $[1/k,3/k]\subseteq[0,1]$. En cero toda columna vale cero. Para $x>0$ fijo, elegimos $N$ con $N+3>3/x$; desde ese corte $(n+3)x>3$ y todos los términos son cero. Así $t_n\to0$ puntualmente, por coincidencia eventual exacta en cada entrada.

</details>

#### Ejercicio 27. Seguir el centro

[]{#MA-EX-ANM-01-026-027}

Encuentra una ruta convergente al origen que produzca salidas constantes1 en las tiendas. ¿Bastan límite continuo y cota común para evitarlo?

[]{#MA-SOL-ANM-01-026-027}

<details class="anm-solution">
<summary>Ver solución del ejercicio 27</summary>

Tomamos $z_n=2/(n+3)$, que pertenece a $[0,1]$ y tiende al origen. En esa entrada, $(n+3)z_n=2$, así $t_n(z_n)=\max(0,1-0)=1$ para toda etapa. El límite puntual es la función cero y es continuo; todas las filas son continuas y comparten la cota $0\le t_n\le1$ en el dominio compacto. Aun así, la ruta central mantiene salidas uno, distintas de la salida cero del límite en su destino de entrada. Las condiciones mencionadas no aportan un control común de cómo varían las filas con la entrada.

</details>

#### Ejercicio 28. Certificar el área

[]{#MA-EX-ANM-01-026-028}

Calcula $\int_0^1t_n$ por ramas, acreditando existencia antes del valor.

[]{#MA-SOL-ANM-01-026-028}

<details class="anm-solution">
<summary>Ver solución del ejercicio 28</summary>

La continuidad de $t_n$ en el cerrado prueba primero su integrabilidad por C23. Fuera del soporte su integral es cero. En $[1/k,2/k]$ vale $kx-1$, y en $[2/k,3/k]$ vale $3-kx$. Ambas ramas tienen anchura $1/k$ y alturas extremas cero y uno en orden inverso. La fórmula afín por sumas de C22 da integral $1/(2k)$ en cada rama. Restricción y aditividad producen $\int_0^1t_n=1/k=1/(n+3)$. Estos valores tienden a cero, coincidiendo en este ejemplo con la integral del límite puntual nulo. La igualdad se ha calculado para la familia dada, sin asumir un teorema general de intercambio.

</details>

#### Ejercicio 29. Altura que compensa anchura

[]{#MA-EX-ANM-01-026-029}

Para $b_n=(n+3)t_n$ demuestra convergencia puntual y compara límite de integrales e integral del límite.

[]{#MA-SOL-ANM-01-026-029}

<details class="anm-solution">
<summary>Ver solución del ejercicio 29</summary>

Definimos $b_n=(n+3)t_n=kt_n$. Cada columna de $t_n$ es exactamente cero en una cola; multiplicar su altura por $k$ conserva ese hecho, así $b_n\to0$ puntualmente. Cada fila es continua e integrable. Por linealidad y la cuenta anterior, $\int_0^1b_n=k\int_0^1t_n=k/k=1$. La sucesión de integrales tiene límite uno, mientras la función límite cero es integrable con valor cero. Existen las dos operaciones comparadas y dan valores distintos. Aquí el aumento de altura compensa la contracción del soporte.

**Retorno visual.** Véase [C26-F06](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html#fig-anm-c26-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 30. Pendientes sin constante común

[]{#MA-EX-ANM-01-026-030}

Demuestra que las tiendas $t_n$ no satisfacen una cota Lipschitz con la misma constante para todas las filas.

[]{#MA-SOL-ANM-01-026-030}

<details class="anm-solution">
<summary>Ver solución del ejercicio 30</summary>

Para cualquier índice, ponemos $u_n=1/k$ y $v_n=2/k$, con $k=n+3$. Ambas entradas pertenecen al dominio y sus alturas son $t_n(u_n)=0$ y $t_n(v_n)=1$. Si existiera una constante Lipschitz común $L\ge0$, tendría que cumplirse $1=|t_n(v_n)-t_n(u_n)|\le L|v_n-u_n|=L/k$, luego $k\le L$ para todo índice. Arquimedianidad proporciona $n$ con $n+3>L$, contradicción. Cada fila sí tiene constante $k$, pues el absoluto y el máximo con cero no aumentan diferencias y la función afín tiene pendiente $k$. Lo que falta es una barrera independiente de la etapa.

</details>

## 26.7. Tres intercambios que pueden fallar

[]{#MA-SEC-ANM-01-026-007}

Los ejemplos siguientes separan dos fallos posibles: que una operación deje de existir en el límite o que siga existiendo y produzca un valor distinto del límite de los resultados. El caso de Dirichlet de C25 ofrece el primero; las tiendas de altura creciente ya ofrecieron el segundo para las integrales.

### La integrabilidad puede desaparecer

Sea $E_m\subseteq[0,1]$ el conjunto de racionales irreducibles con denominador como máximo $m$, y $d_n=\mathbf1_{E_{n+1}}$. C25 demostró finitud de $E_m$ e integral0 de su indicadora. Si $x$ es irracional, $d_n(x)=0$ siempre. Si $x=p/q$ irreducible, $d_n(x)=1$ desde $n+1\ge q$. Por ello $d_n$ converge puntualmente a la indicadora de los racionales, la función de Dirichlet.

Cada fila es integrable de valor cero y toda la familia queda entre cero y uno. Sin embargo, C25 demuestra que el límite de Dirichlet no tiene integral de Riemann. Aquí no hay dos valores integrales que comparar. En la familia $b_n$ sí existían tanto la integral del límite como el límite de las integrales y diferían. Mantener esta distinción permite formular exactamente qué refuta cada ejemplo.

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

### Ejercicios de la sección 26.7

#### Ejercicio 31. Límite sin integral propia

[]{#MA-EX-ANM-01-026-031}

Con $d_n=\mathbf1_{E_{n+1}}$ de C25, prueba límite puntual y explica qué comparación integral está mal tipada.

[]{#MA-SOL-ANM-01-026-031}

<details class="anm-solution">
<summary>Ver solución del ejercicio 31</summary>

El conjunto $E_{n+1}$ es finito y su indicadora es una modificación finita de la tasa cero. Por tanto cada $d_n$ es integrable con valor cero. En los irracionales todas sus columnas son cero; en un racional reducido de denominador $q$ la columna vale uno desde $n+1\ge q$. El límite puntual es Dirichlet, que C25 probó no integrable. Así $\lim_n\int_0^1d_n=0$ existe, pero $\int_0^1\lim_n d_n$ no es un valor real definido como integral propia de Riemann. No hay dos valores integrales que comparar en ese caso. La cota común entre cero y uno no asegura la integrabilidad del límite.

</details>

#### Ejercicio 32. Calcular las derivadas

[]{#MA-EX-ANM-01-026-032}

Para $h_n(x)=x/[1+(n+1)x^2]$ en $\mathbb R$, calcula derivadas y demuestra convergencia puntual de valores y derivadas.

[]{#MA-SOL-ANM-01-026-032}

<details class="anm-solution">
<summary>Ver solución del ejercicio 32</summary>

Escribimos $k=n+1>0$. El denominador $1+kx^2$ es positivo en toda la recta, y la regla del cociente da $h_n'(x)=[(1+kx^2)-x(2kx)]/(1+kx^2)^2=(1-kx^2)/(1+kx^2)^2$. En cero, $h_n(0)=0$ y $h_n'(0)=1$. Si $x\ne0$, $|h_n(x)|\le1/(k|x|)\to0$. Además $|1-kx^2|\le1+kx^2$, así $|h_n'(x)|\le1/(1+kx^2)\to0$. Cada cota ofrece un corte arquimediano para la entrada fija. Por tanto $h_n\to h=0$ y $h_n'\to g=\mathbf1_{\{0\}}$ puntualmente. La derivada de $h$ es cero y difiere de $g$ en el origen, donde ambas operaciones existen.

</details>

#### Ejercicio 33. Un máximo exacto de error

[]{#MA-EX-ANM-01-026-033}

Prueba la cota global $|h_n(x)|\le1/[2\sqrt{n+1}]$ y que se alcanza.

[]{#MA-SOL-ANM-01-026-033}

<details class="anm-solution">
<summary>Ver solución del ejercicio 33</summary>

Sea $k=n+1$ y $r=\sqrt{k}>0$. El cuadrado $(r|x|-1)^2\ge0$ equivale a $1+kx^2\ge2r|x|$. Para $x\ne0$, dividir por los denominadores positivos da $|h_n(x)|=|x|/(1+kx^2)\le1/(2r)$. En cero el valor es cero y cumple la misma cota. En $x=\pm1/r$, el denominador es dos y la magnitud $1/(2r)$, así la cota se alcanza y es el máximo exacto. Tiende a cero al aumentar el índice y controla todos los valores simultáneamente. Sin embargo $h_n'(0)=1$ para toda etapa, por lo que esa cota global de valores no basta para intercambiar derivadas.

**Retorno visual.** Véase [C26-F07](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html#fig-anm-c26-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 34. Auditar la prueba triangular

[]{#MA-EX-ANM-01-026-034}

En el intento de deducir continuidad del límite puntual de funciones continuas, identifica el paso no autorizado.

[]{#MA-SOL-ANM-01-026-034}

<details class="anm-solution">
<summary>Ver solución del ejercicio 34</summary>

La triangular $|f(y)-f(x)|\le|f(y)-f_n(y)|+|f_n(y)-f_n(x)|+|f_n(x)-f(x)|$ es válida. El error puntual en $x$ permite escoger un índice para el último término. La continuidad de esa fila permite elegir un radio que controle el término central para entradas cercanas. El primer término requiere ahora controlar $|f(y)-f_n(y)|$ para todas esas entradas con el mismo índice ya escogido. La convergencia puntual sólo da cortes que pueden depender de $y$ y no proporciona ese control de ventana. Las potencias en $[0,1]$, con filas continuas y límite discontinuo en uno, prueban que la conclusión pretendida puede ser falsa.

</details>

#### Ejercicio 35. Clasificar tres fracasos

[]{#MA-EX-ANM-01-026-035}

Compara potencias, tiendas normalizadas y $d_n$ según qué propiedad falla y qué objetos existen.

[]{#MA-SOL-ANM-01-026-035}

<details class="anm-solution">
<summary>Ver solución del ejercicio 35</summary>

En las potencias sobre $[0,1]$ todas las filas son continuas y el límite puntual existe, pero es discontinuo en uno. En las tiendas normalizadas $b_n$ existen las integrales de todas las filas y del límite nulo; el límite de las primeras es uno y la segunda vale cero. En $d_n=\mathbf1_{E_{n+1}}$, las filas tienen integral cero y límite puntual Dirichlet, pero éste carece de integral propia. Los dos ejemplos integrales fallan de formas distintas: uno da valores desiguales y el otro deja inexistente una operación. Cada afirmación debe conservar esa diferencia de alcance.

</details>

## 26.8. Certificados que recuperan control

[]{#MA-SEC-ANM-01-026-008}

La convergencia en cada entrada ha permitido operar con columnas, pero no ha dado control automático de entradas móviles. Buscaremos una hipótesis que relacione los valores de cada fila en dos entradas mediante una misma constante. Esa relación podrá pasar al límite y cerrar directamente el error de una diagonal.

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

En una prueba puntual, la entrada y la tolerancia se fijan antes de construir el corte, y la estimación debe valer en toda la cola. Para refutarla necesitamos mantener una entrada y una tolerancia con infracciones arbitrariamente tardías. Mover la entrada puede refutar un corte simultáneo, como hacen las rutas explícitas anteriores, pero no el contrato puntual. Antes de comparar límites con integrales o derivadas comprobamos además que existan las operaciones de ambos lados.

En un conjunto finito, el máximo de umbrales resuelve todas las entradas para una tolerancia. En un conjunto infinito, ese máximo puede no existir. Compactitud del dominio, continuidad de las filas, continuidad del límite y una cota común de valores, considerados por separado, no borran las dependencias que los ejemplos han exhibido.

El obstáculo en los ejemplos es la ausencia de un solo corte que sirva para todas las entradas. Exigir ese corte cambiará el contrato de convergencia y hará posible medir el error de la función completa. La prueba puntual, por sí sola, deja esa obligación abierta.

![Familia f_n(x)=x+1/(n+1), con constante Lipschitz común L=1 y límite x. En la ruta x_n=1/(n+1), el error hacia f(0) es2/(n+1), suma de distancia de entrada y error puntual. La estimación común, no una muestra finita, justifica el control para cualquier ruta convergente dada.](../../assets/books/anm/C26/C26-F08.svg){#fig-anm-c26-f08 fig-alt="Familia f_n(x)=x+1/(n+1), con constante Lipschitz común L=1 y límite x. En la ruta x_n=1/(n+1), el error hacia f(0) es2/(n+1), suma de distancia de entrada y error puntual. La estimación común, no una muestra finita, justifica el control para cualquier ruta convergente dada."}

### Ejercicios de la sección 26.8

#### Ejercicio 36. Transportar una cota común de proximidad

[]{#MA-EX-ANM-01-026-036}

Si $f_n\to f$ puntualmente y todas las filas son Lipschitz con la misma constante $L\ge0$, prueba que $f$ lo es y es continua.

[]{#MA-SOL-ANM-01-026-036}

<details class="anm-solution">
<summary>Ver solución del ejercicio 36</summary>

Fijamos $x,y\in X$. La convergencia de sus dos columnas y el álgebra numérica dan $f_n(x)-f_n(y)\to f(x)-f(y)$. La continuidad del absoluto da convergencia de sus magnitudes. Como todas están acotadas por el mismo $L|x-y|$, la preservación del orden produce $|f(x)-f(y)|\le L|x-y|$. Esto vale para todo par, así $f$ es Lipschitz con la misma constante. Para $\varepsilon>0$, tomamos $\delta=\varepsilon/(L+1)>0$. Si $L>0$ y la distancia es menor que $\delta$, el error es menor que $L\varepsilon/(L+1)<\varepsilon$; si $L=0$, es cero. Se obtiene continuidad relativa, incluso uniforme en el dominio.

</details>

#### Ejercicio 37. Diagonal con presupuesto común

[]{#MA-EX-ANM-01-026-037}

Bajo la hipótesis del ejercicio anterior, si una ruta dada $x_n\to x\in X$ permanece en $X$, prueba $f_n(x_n)\to f(x)$.

[]{#MA-SOL-ANM-01-026-037}

<details class="anm-solution">
<summary>Ver solución del ejercicio 37</summary>

La ruta está dada con $x_n\in X$ y $x_n\to x\in X$. La triangular y la cota común dan $|f_n(x_n)-f(x)|\le|f_n(x_n)-f_n(x)|+|f_n(x)-f(x)|\le L|x_n-x|+|f_n(x)-f(x)|$. Dada $\varepsilon>0$, tomamos el corte de la ruta para error menor que $\varepsilon/[2(L+1)]$ y el corte puntual en $x$ para error menor que $\varepsilon/2$. Su máximo garantiza que la expresión anterior es menor que $\varepsilon$. Para $L=0$ el primer término es cero y el mismo argumento sirve. La constante común controla el cambio de entrada que la convergencia puntual sola dejaba sin resolver.

</details>

#### Ejercicio 38. Monotonía sin barrera universal

[]{#MA-EX-ANM-01-026-038}

Prueba existencia de límite puntual para columnas crecientes acotadas por una barrera que puede depender de la entrada.

[]{#MA-SOL-ANM-01-026-038}

<details class="anm-solution">
<summary>Ver solución del ejercicio 38</summary>

Para cada entrada fija $x$, la imagen de su columna es no vacía y tiene una cota superior real por hipótesis. Completitud proporciona el supremo único $s_x$. Para $\varepsilon>0$, algún índice $j$ satisface $f_j(x)>s_x-\varepsilon$; de otro modo ese número menor sería cota superior. La monotonía por índice mantiene, para $n\ge j$, $s_x-\varepsilon<f_j(x)\le f_n(x)\le s_x$. Por tanto $|f_n(x)-s_x|<\varepsilon$ en toda la cola. Los supremos únicos forman el grafo de la función límite sin seleccionar una cota arbitraria por entrada. No se requiere una barrera común sobre todo $X$, ni se concluye que el límite esté globalmente acotado.

</details>

#### Ejercicio 39. Monotonía del índice y de la variable

[]{#MA-EX-ANM-01-026-039}

Construye una familia creciente por columnas cuyas filas no sean crecientes ni decrecientes en su variable.

[]{#MA-SOL-ANM-01-026-039}

<details class="anm-solution">
<summary>Ver solución del ejercicio 39</summary>

En $X=[-1,1]$, definimos $f_n(x)=x^2-1/(n+1)$. Para cada entrada, $f_{n+1}(x)-f_n(x)=1/[(n+1)(n+2)]>0$, así las columnas son estrictamente crecientes y convergen a $x^2$. Sin embargo, en una fila fija se tiene $f_n(-1)=f_n(1)=1-1/(n+1)$ y $f_n(0)=-1/(n+1)$, estrictamente menor. El orden $-1<0$ refuta que esa fila sea no decreciente, y $0<1$ refuta que sea no creciente. La monotonía por columnas compara etapas distintas; la monotonía respecto de la variable compara entradas distintas de una misma etapa.

</details>

#### Ejercicio 40. Un certificado y su límite de alcance

[]{#MA-EX-ANM-01-026-040}

Para $f_n(x)=x+1/(n+1)$ en $\mathbb R$, verifica límite puntual, cota Lipschitz común y toda diagonal $x_n\to x$. Compáralo con $t_n$.

[]{#MA-SOL-ANM-01-026-040}

<details class="anm-solution">
<summary>Ver solución del ejercicio 40</summary>

Para cualquier entrada $x$, $|f_n(x)-x|=1/(n+1)\to0$, así el límite puntual es la identidad. Para todo par $u,v$, $|f_n(u)-f_n(v)|=|u-v|$, dando constante Lipschitz común uno. Si $x_n\to x$ es una ruta dada, la triangular ofrece $|f_n(x_n)-x|\le|x_n-x|+1/(n+1)\to0$, reuniendo sus dos cortes. En las tiendas, las filas y el límite también son continuos, pero sus constantes Lipschitz crecen como $n+3$. La ruta central mantiene salida uno, así esas condiciones de continuidad no reemplazan la cota común que hace funcionar la prueba positiva.

**Retorno visual.** Véase [C26-F08](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html#fig-anm-c26-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-26)

[← Capítulo 25](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html) · [Capítulo 27 →](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez.html)
