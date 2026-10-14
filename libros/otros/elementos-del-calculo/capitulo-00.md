---
title: Capítulo 0. Del límite a la pregunta por el cálculo
status: published
draft: false
book-id: MA-BOK-0015
editorial-project: EDC
date-modified: '2026-10-13'
license: GFDL-1.3-or-later
areas:
  - calculo
  - analisis
  - fundamentos
level: intermedio
topics:
  - calculo-de-una-variable
  - historia-de-las-matematicas
number-sections: false
provenance:
  type: original
  sources:
    - role: idea
      note: 'Inspiración metodológica: Gabor Toth, Elements of Mathematics (2021); obra independiente.'
source-id: EDC-C00
source-sha256: 3be078b456aa44a3b298219376e2e9cf10153a60d2093ca179cb74887113589b
content-id: MA-BCH-0331
content-type: book-chapter
related:
  - MA-BOK-0015
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-00.html) · [Ejercicios](capitulo-00-ejercicios.html) · [Soluciones](capitulo-00-soluciones.html)

[Capítulo 1 →](capitulo-01.html)

> **Pregunta generadora.** ¿Qué permiten comprender ya los números reales, los límites y la continuidad, y qué debemos construir todavía para responder a los problemas de las tangentes, la velocidad y el área?

La parábola permite calcular sin dificultad la altura de cada uno de sus puntos; basta elevar al cuadrado la coordenada horizontal. Pero conocer todos esos valores deja abiertas otras preguntas sobre la misma curva: qué inclinación tiene en un punto y cuánto mide la región que delimita junto al eje horizontal. El álgebra nos ofrece un comienzo para ambas investigaciones, pues podemos calcular pendientes entre dos puntos y sumar áreas de rectángulos, aunque en cada caso obtenemos cantidades que dependen de una elección: la separación entre los puntos o la anchura de los rectángulos.

Podemos reducir esas separaciones y observar cómo cambian los resultados. Para que esa observación llegue a justificar una inclinación o un área, necesitamos precisar qué significa que los números calculados se acerquen a un valor y qué garantiza que ese valor exista. Ése es el trabajo de los límites. Al hacerlo descubriremos también por qué importa que nuestras cantidades sean números reales y cómo la continuidad permite trasladar el comportamiento de unos puntos al de otros que se aproximan a ellos.

## 0.1. Dos preguntas ante una misma curva

Consideremos la parábola $y=x^2$, dada por la función $f(x)=x^2$. Podemos estudiar los dos problemas con esta misma fórmula y observar dónde exige cada uno pasar de un cálculo finito a un proceso de aproximación.

**Primer problema: la inclinación.** Entre los puntos $(a,a^2)$ y $(a+h,(a+h)^2)$, con $h\neq0$, la recta secante tiene pendiente

$$
\frac{(a+h)^2-a^2}{h}=2a+h.
$$

La pendiente depende de $h$, pero el resultado del cálculo permite ver qué sucede cuando acercamos el segundo punto al primero: el sumando $h$ se hace pequeño y queda un valor próximo a $2a$. Toda la simplificación se efectuó con $h\neq0$, condición que permite dividir; por eso podemos investigar la aproximación a $2a$ sin asignar ningún valor a la fracción original en $h=0$. Para reconocer en ese número la pendiente de una tangente todavía tendremos que precisar qué significa aproximar una curva por una recta cerca del punto.

**Segundo problema: la acumulación.** En el intervalo $[0,1]$ queremos medir la región comprendida entre el eje horizontal y la gráfica $y=x^2$. Si dividimos el intervalo en $n$ partes iguales, cada una de anchura $1/n$, podemos sumar áreas de rectángulos elegidos sobre los extremos derechos:

$$
R_n=\frac1n\sum_{k=1}^n\left(\frac{k}{n}\right)^2
=\frac1{n^3}\sum_{k=1}^n k^2.
$$

La identidad finita

$$
\sum_{k=1}^n k^2=\frac{n(n+1)(2n+1)}6
$$

se comprueba por inducción: al sumar $(n+1)^2$ al término $n(n+1)(2n+1)/6$ se obtiene $(n+1)(n+2)(2n+3)/6$, que es la misma fórmula con $n+1$; el caso $n=1$ es inmediato. Por consiguiente,

$$
R_n=\frac{(n+1)(2n+1)}{6n^2}
=\frac13+\frac1{2n}+\frac1{6n^2}.
$$

Los dos últimos sumandos se hacen pequeños al aumentar $n$, de modo que $R_n$ se acerca a $1/3$. Si elegimos las alturas en los extremos izquierdos, los rectángulos quedan por debajo de la curva y obtenemos otras sumas; en §0.7 comprobaremos que también se acercan a $1/3$. La coincidencia sugiere que el valor depende de la región y que las elecciones usadas para aproximarla dejan de importar cuando los rectángulos se estrechan. Habrá que poner a prueba esa sugerencia con otras funciones, subdivisiones desiguales y muestras distintas antes de confiar en ella como procedimiento general.

En la pendiente hemos comparado valores de la función mediante una división; en el área los hemos reunido mediante una suma. Ambos cálculos nos obligan a seguir un proceso de aproximación, y su justificación comienza por la palabra que todavía usamos de manera informal: «acercarse».

## 0.2. Por qué trabajamos con los números reales

### 0.2.1. Orden y completitud

Nuestro conjunto de números es $\mathbb R$. Adoptamos su estructura usual de **cuerpo ordenado**: son válidas las operaciones de suma, resta, producto y división por un número no nulo; el orden es compatible con suma y multiplicación por cantidades positivas. Tomaremos $\mathbb N=\{1,2,3,\ldots\}$; así, $0\notin\mathbb N$. Partimos de estas propiedades algebraicas para estudiar qué operaciones podemos justificar cuando intervienen límites.

También los racionales permiten esas operaciones y tienen un orden compatible con ellas. La diferencia aparecerá al buscar la frontera de un conjunto de números: puede haber racionales que se acerquen cuanto queramos a una posición de la recta sin que esa posición corresponda a un racional. Para expresar la propiedad de los reales que resuelve esa dificultad, necesitamos distinguir entre una cota cualquiera y la menor de todas las cotas superiores.

**Definición 0.1 (cota superior y supremo; `EDC-C00-DEF-001`).** Sea $A\subseteq\mathbb R$ no vacío. Un número $M\in\mathbb R$ es **cota superior** de $A$ si $x\le M$ para todo $x\in A$. Decimos que $s$ es el **supremo** de $A$, escrito $s=\sup A$, si es cota superior y si ninguna cantidad menor que $s$ lo es. Equivalentemente,

$$
\bigl(\forall x\in A\;x\le s\bigr)
\quad\text{y}\quad
\bigl(\forall\varepsilon>0\;\exists x\in A:\ s-\varepsilon<x\bigr).
$$

La segunda cláusula impide que quede espacio entre el conjunto y su menor cota superior: por pequeña que sea la tolerancia, algún elemento debe sobrepasar la cota disminuida en esa tolerancia. El supremo puede pertenecer al conjunto, en cuyo caso es su máximo, pero la definición permite igualmente que todos los elementos queden por debajo de él. Esa posibilidad será la que usemos para construir números y límites.

**Axioma de completitud de $\mathbb R$ (`EDC-C00-AX-001`).** Todo subconjunto no vacío de $\mathbb R$ que esté acotado superiormente posee supremo en $\mathbb R$.

Adoptamos este axioma junto con las propiedades de cuerpo ordenado, y a partir de ellos demostraremos los resultados que necesitamos. La existencia de un supremo exige las dos condiciones del axioma: que haya al menos un elemento y que exista una cota superior. Tendremos que comprobarlas cada vez que el argumento use la completitud, incluso cuando un dibujo sugiera sin dificultad dónde debería encontrarse la frontera.

### 0.2.2. La propiedad arquimediana

**Teorema 0.1 (`EDC-C00-THM-001`).** Para todo $x\in\mathbb R$ existe $n\in\mathbb N$ tal que $n>x$. En consecuencia, para todo $\varepsilon>0$ existe $n\in\mathbb N$ con $0<1/n<\varepsilon$.

**Demostración.** Supongamos que los naturales tienen una cota superior y llamemos $s=\sup\mathbb N$ a su supremo, cuya existencia garantiza la completitud. Si ningún natural sobrepasara $s-1$, ese número también sería cota superior, en contra de la elección de $s$ como la menor. La caracterización aproximativa del supremo, aplicada a $\varepsilon=1$, proporciona por tanto $n\in\mathbb N$ con $s-1<n\le s$. El natural siguiente, $n+1\in\mathbb N$, satisface $n+1>s$, y contradice que $s$ sea cota superior. Hemos probado que $\mathbb N$ no está acotado superiormente.

Dado $\varepsilon>0$, podemos entonces elegir $n>1/\varepsilon$. Como ambos números son positivos, al tomar sus recíprocos obtenemos $0<1/n$ y $1/n<\varepsilon$. $\square$

Cada número $1/n$ es positivo, y sin embargo podemos encontrar uno menor que cualquier tolerancia positiva que se nos proponga. El tamaño de esa tolerancia determina hasta qué natural tendremos que llegar. Ésta será una forma recurrente de controlar errores de aproximación: conservar cantidades positivas en cada cálculo finito y demostrar que ninguna distancia positiva puede impedirles acercarse a cero.

### 0.2.3. Un hueco entre los racionales

En $\mathbb Q$, la ecuación $x^2=2$ no tiene solución. En efecto, si $p/q$ fuera una fracción irreducible con $(p/q)^2=2$, tendríamos $p^2=2q^2$. Así, $p$ sería par, digamos $p=2r$; entonces $q^2=2r^2$ y también $q$ sería par, contradiciendo la irreducibilidad.

La completitud permite, en cambio, demostrar la existencia de una solución real positiva.

**Proposición 0.1 (`EDC-C00-PRP-001`).** Existe un único $r>0$ con $r^2=2$.

**Demostración.** Busquemos la raíz a través de los números no negativos cuyo cuadrado todavía queda por debajo de $2$. Consideremos $A=\{x\in[0,2]:x^2<2\}$. Se cumple $1\in A$ y el conjunto está acotado por $2$, de modo que existe $r=\sup A$; tenemos $r\ge1$ y también $r\le2$. La elección de $A$ sugiere que su frontera debería tener cuadrado $2$; para demostrarlo hay que excluir que su cuadrado quede a cualquiera de los dos lados.

Si $r^2<2$, todavía hay una diferencia positiva entre $r^2$ y $2$. Queremos aprovecharla para aumentar un poco $r$ conservando el cuadrado por debajo de $2$, lo que contradirá que $r$ sea cota superior. El aumento del cuadrado es $d(2r+d)$; al exigir $d<1$ podemos acotarlo por $d(2r+1)$ y escoger $d$ a partir de la diferencia disponible. Elegimos así $0<d<\min\{1,(2-r^2)/(2r+1)\}$. Entonces

$$
(r+d)^2=r^2+d(2r+d)<2,
$$

y como $r+d>0$ y su cuadrado es menor que $2$, también $r+d<2$. Por tanto, $r+d\in A$, aunque sobrepasa a su cota superior $r$.

Si $r^2>2$, buscamos en cambio un número positivo un poco menor que $r$ cuyo cuadrado siga siendo mayor que $2$. Elegimos $0<d<\min\{r,(r^2-2)/(2r)\}$: la primera restricción mantiene $r-d>0$ y la segunda garantiza

$$
(r-d)^2=r^2-2rd+d^2>2.
$$

La propiedad aproximativa del supremo proporciona $x\in A$ con $r-d<x\le r$. Puesto que $x\ge0$ y $r-d>0$, el orden de esos números se conserva al elevarlos al cuadrado, y obtenemos $x^2>(r-d)^2>2$, contrario a la pertenencia de $x$ a $A$. Quedan excluidas las dos desigualdades, luego $r^2=2$.

La unicidad usa sólo el orden: si $0<r<s$ y ambos tuvieran cuadrado $2$, tendríamos $r^2<s^2$, una contradicción. $\square$

La prueba de irracionalidad nos decía que la raíz no podía encontrarse entre las fracciones; la completitud ha permitido encontrarla entre los reales. Cuando estudiemos aproximaciones racionales a un número, tendremos que conservar esa distinción: los términos pueden ser racionales aunque el valor al que se aproximan sólo exista en el conjunto más amplio.

## 0.3. Sucesiones: lo que significa acercarse

Una sucesión permite registrar los resultados de un proceso en el orden en que los calculamos. La afirmación de que esos resultados se aproximan a un número exige más que encontrar algunos términos cercanos: una vez alcanzada la precisión que pedimos, todos los términos posteriores deben conservarla. Además, hemos de poder pedir cualquier precisión positiva, aunque ello nos obligue a avanzar más en la sucesión.

**Definición 0.2 (`EDC-C00-DEF-002`).** Una sucesión real es una función $n\mapsto x_n$ de $\mathbb N$ en $\mathbb R$. Decimos que $x_n$ **converge** a $\ell\in\mathbb R$ si

$$
\forall\varepsilon>0\;\exists N\in\mathbb N\;\forall n\ge N:
\quad |x_n-\ell|<\varepsilon.
$$

Escribimos $x_n\to\ell$ o $\lim_{n\to\infty}x_n=\ell$. La definición empieza por una tolerancia $\varepsilon$ y nos pide encontrar un índice $N$ a partir del cual todos los errores sean menores que ella; si la tolerancia cambia, podemos elegir otro índice. Lo que no podemos hacer es cambiar $N$ para cada $n$ después de haberlo elegido, pues perderíamos el control de toda la cola. El Teorema 0.1 muestra, por ejemplo, que $1/n\to0$: elegimos $N>1/\varepsilon$ y para todo $n\ge N$ se cumple $1/n\le1/N<\varepsilon$.

**Lema 0.1 (`EDC-C00-LEM-001`).** Toda sucesión convergente tiene límite único y está acotada. Si $u_n\to u$ y $v_n\to v$, entonces $u_n+v_n\to u+v$, $u_nv_n\to uv$ y, si $v\neq0$, $u_n/v_n\to u/v$ (el cociente está definido para $n$ suficientemente grande).

**Demostración.** Si $x_n\to a$ y $x_n\to b$, podemos pedir que los términos estén simultáneamente cerca de ambos candidatos. Para cualquier $\varepsilon>0$ escogemos un índice a partir del cual se cumplan las dos estimaciones, y la desigualdad triangular da

$$
|a-b|\le|a-x_n|+|x_n-b|<2\varepsilon.
$$

Una distancia positiva entre $a$ y $b$ sería incompatible con esa desigualdad para todas las tolerancias; por ejemplo, bastaría tomar $\varepsilon=|a-b|/3$. Luego $a=b$.

La acotación requiere separar la cola del comienzo de la sucesión. Al tomar $\varepsilon=1$, los términos desde cierto índice satisfacen $|x_n|\le|\ell|+1$; los anteriores son finitos en número, de modo que sus módulos también tienen una cota. Podemos elegir una cota que sirva para ambos grupos.

Para la suma, la desigualdad triangular acota el error por la suma de los dos errores conocidos, y basta hacer cada uno menor que la mitad de la tolerancia. En el producto hay además un factor variable: al sumar y restar $u_nv$ separamos el error en

$$
|u_nv_n-uv|\le |u_n|\,|v_n-v|+|v|\,|u_n-u|;
$$

la sucesión $u_n$ está acotada por lo que acabamos de probar. Si elegimos una cota positiva $B$ para sus módulos, podemos hacer el primer término menor que $\varepsilon/2$ exigiendo $|v_n-v|<\varepsilon/(2B)$; el segundo queda menor que $\varepsilon/2$ al exigir $|u_n-u|<\varepsilon/(2(|v|+1))$. Un índice común satisface las dos exigencias.

En el cociente debemos controlar primero el denominador. Como $v\neq0$, la convergencia permite asegurar $|v_n-v|<|v|/2$ para índices suficientemente grandes; entonces $|v_n|>|v|/2$, y las divisiones están definidas. Escribimos

$$
\left|\frac{u_n}{v_n}-\frac uv\right|
=\frac{|v(u_n-u)-u(v_n-v)|}{|v|\,|v_n|}
\longrightarrow0.
$$

El numerador tiende a cero por las estimaciones de suma y producto ya demostradas, mientras que el denominador queda por encima de la constante positiva $|v|^2/2$. Esa cota permite hacer la fracción menor que cualquier tolerancia mediante un índice suficientemente grande. $\square$

**Lema 0.2 (encajonamiento; `EDC-C00-LEM-002`).** Si $a_n\le b_n\le c_n$ desde cierto índice y $a_n\to L$, $c_n\to L$, entonces $b_n\to L$.

**Demostración.** Para $\varepsilon>0$, tanto $a_n$ como $c_n$ pertenecen al intervalo $(L-\varepsilon,L+\varepsilon)$ a partir de un índice común. La desigualdad obliga a que también $b_n$ pertenezca a él. $\square$

### 0.3.1. Sucesiones monótonas e intervalos encajados

**Teorema 0.2 (convergencia monótona; `EDC-C00-THM-002`).** Toda sucesión real no decreciente y acotada superiormente converge al supremo de sus términos. La afirmación dual vale para sucesiones no crecientes acotadas inferiormente.

**Demostración.** Sea $s=\sup\{x_n:n\in\mathbb N\}$, que existe porque el conjunto de términos es no vacío y está acotado superiormente. La propiedad de supremo asegura que, para una tolerancia $\varepsilon>0$, algún término satisface $x_N>s-\varepsilon$. Aquí interviene la monotonía: los términos posteriores no pueden retroceder por debajo de $x_N$, y tampoco pueden superar la cota $s$. Para $n\ge N$ tenemos por tanto $s-\varepsilon<x_N\le x_n\le s$, de donde $|x_n-s|<\varepsilon$. Si la sucesión es no creciente y está acotada inferiormente, la sucesión $-x_n$ es no decreciente y está acotada superiormente; aplicamos a ella la primera parte y cambiamos el signo del límite. $\square$

**Teorema 0.3 (intervalos encajados; `EDC-C00-THM-003`).** Sean $I_n=[a_n,b_n]$ intervalos cerrados no vacíos y acotados tales que $I_{n+1}\subseteq I_n$. Entonces $\bigcap_{n\ge1}I_n$ no es vacío. Si además $b_n-a_n\to0$, esa intersección consta de un solo número.

**Demostración.** El encajamiento obliga a que los extremos izquierdos formen una sucesión no decreciente y los derechos una no creciente. Para todos ellos se cumple $a_n\le b_1$, de modo que existe $c=\sup\{a_n:n\ge1\}$. Este número queda a la derecha de todos los extremos izquierdos; para que pertenezca a cada intervalo necesitamos comprobar también que ninguno de sus extremos derechos queda por debajo de él.

Fijemos $n$. Para cada índice $k$ se cumple $a_k\le b_n$: si $k\le n$, el encajamiento da $a_k\le a_n\le b_n$; si $k\ge n$, da $a_k\le b_k\le b_n$. Luego $b_n$ es cota superior de todos los $a_k$ y, por ser $c$ la menor de esas cotas, $c\le b_n$. Junto con $a_n\le c$, obtenemos $c\in I_n$ para todo $n$.

Si $d$ pertenece también a todos los intervalos, los dos números quedan dentro de cada uno y su distancia satisface $|c-d|\le b_n-a_n$ para todo $n$. Cuando esas longitudes tienden a cero, una distancia positiva resulta imposible, por lo que $c=d$. $\square$

### 0.3.2. La selección de una subsucesión convergente

**Teorema 0.4 (Bolzano–Weierstrass en la recta; `EDC-C00-THM-004`).** Toda sucesión real acotada posee una subsucesión convergente.

**Demostración.** Incluyamos todos los términos en $I_0=[a,b]$. Si $a=b$, la sucesión es constante y basta tomarla como subsucesión. Cuando $a<b$, el problema consiste en conservar infinitos términos mientras reducimos el intervalo que los contiene: disponer de un término en cada intervalo pequeño no bastaría, porque podría tratarse siempre de uno de los primeros.

Dividimos $I_0$ en dos mitades cerradas. Al menos una contiene términos correspondientes a infinitos índices, pues si ambas contuvieran sólo un número finito, la sucesión entera tendría sólo un número finito de índices. Elegimos una de esas mitades como $I_1$ y repetimos la operación dentro de ella. Obtenemos intervalos cerrados encajados $I_k$ de longitud $(b-a)/2^k$, cada uno de los cuales conserva infinitos términos contados por sus índices. Sus longitudes satisfacen $(b-a)/2^k\to0$: por inducción $2^k\ge k+1$, y el Teorema 0.1 permite concluir $2^{-k}\to0$. El Teorema 0.3 proporciona por tanto un único $c$ que pertenece a todos los intervalos.

Podemos escoger sucesivamente $n_1<n_2<\cdots$ con $x_{n_k}\in I_k$, ya que un conjunto infinito de índices naturales contiene índices mayores que cualquiera fijado de antemano. Esa elección convierte los términos retenidos en una subsucesión. Como $x_{n_k}$ y $c$ pertenecen a $I_k$,

$$
|x_{n_k}-c|\le\frac{b-a}{2^k}\longrightarrow0.
$$

Por tanto, $x_{n_k}\to c$. $\square$

## 0.4. Límites de funciones y continuidad

### 0.4.1. El valor al que se acerca una función

Un **punto de acumulación** de $D\subseteq\mathbb R$ es un número $a$ tal que todo intervalo $(a-\delta,a+\delta)$, $\delta>0$, contiene algún punto de $D$ diferente de $a$. Este requisito evita hablar de un límite determinado cuando no existen puntos del dominio que se acerquen al lugar considerado.

**Definición 0.3 (límite funcional; `EDC-C00-DEF-003`).** Sea $f:D\to\mathbb R$, $D\subseteq\mathbb R$, y sea $a$ un punto de acumulación de $D$. Afirmamos que

$$
\lim_{x\to a,\ x\in D} f(x)=L
$$

si, para todo $\varepsilon>0$, existe $\delta>0$ tal que

$$
x\in D,\quad 0<|x-a|<\delta
\quad\Longrightarrow\quad |f(x)-L|<\varepsilon.
$$

La distancia $\delta$ controla qué argumentos examinamos; la tolerancia $\varepsilon$ controla cuánto pueden separarse sus valores del candidato $L$. Para cada tolerancia debemos encontrar una distancia que sirva para todos los argumentos permitidos, y por eso una lista de valores próximos no basta para establecer el límite. La condición $0<|x-a|$ deja fuera el punto $a$, que **no tiene que pertenecer** a $D$; si pertenece, el valor $f(a)$ no interviene en esta definición. Cuando el dominio está claro omitiremos la indicación $x\in D$ debajo del límite.

Por ejemplo, con $D=\mathbb R\setminus\{a\}$, la función $f(x)=(x^2-a^2)/(x-a)$ coincide en su dominio con $x+a$. Por tanto, $\lim_{x\to a}f(x)=2a$, aunque $f(a)$ no esté definido.

**Teorema 0.5 (criterio secuencial del límite; `EDC-C00-THM-005`).** En las condiciones de la definición anterior,

$$
\lim_{x\to a,\ x\in D}f(x)=L
$$

si y sólo si para toda sucesión $(x_n)$ con $x_n\in D\setminus\{a\}$ y $x_n\to a$ se cumple $f(x_n)\to L$.

**Demostración.** Supongamos primero el límite funcional y tomemos una sucesión de las admitidas en el enunciado. Dado $\varepsilon>0$, la definición proporciona una distancia $\delta$ que sirve para todos los puntos del dominio en el entorno perforado. Como $x_n\to a$, desde cierto índice se cumple $|x_n-a|<\delta$, y como ningún término es $a$, podemos aplicar esa garantía y obtener $|f(x_n)-L|<\varepsilon$.

Para la recíproca resulta útil pensar cómo podría fallar la definición de límite. Tendría que haber una tolerancia $\varepsilon_0>0$ que ninguna distancia consiguiera asegurar: por pequeño que fuera el entorno perforado, dentro de él habría un punto cuyo valor se apartara de $L$ al menos esa tolerancia. Podemos convertir esos puntos en una sucesión escogiendo, para cada $n\in\mathbb N$, un $x_n\in D$ con

$$
0<|x_n-a|<\frac1n,
\qquad |f(x_n)-L|\ge\varepsilon_0.
$$

La primera desigualdad garantiza $x_n\to a$ y que los términos son distintos de $a$; la segunda impide $f(x_n)\to L$. Esa sucesión contradice la condición del enunciado. $\square$

**Corolario 0.1 (`EDC-C00-COR-001`).** Un límite funcional finito, en un punto de acumulación, es único. Son válidas las reglas de suma, producto y cociente de límites cuando el límite del denominador es distinto de cero.

**Demostración.** Por acumulación se puede elegir una sucesión de puntos distintos de $a$ que tienda a $a$ (tomando uno a distancia menor que $1/n$). Si existieran dos límites diferentes, esa sucesión de valores convergería a ambos, contra el Lema 0.1. Las reglas se siguen aplicando el Teorema 0.5 y las operaciones con sucesiones del mismo lema; la condición de denominador no nulo asegura que las divisiones están definidas suficientemente cerca del punto. $\square$

### 0.4.2. Continuidad: aproximarse también al valor

**Definición 0.4 (continuidad relativa al dominio; `EDC-C00-DEF-004`).** Sea $f:D\to\mathbb R$ y $a\in D$. La función es **continua en $a$** si para todo $\varepsilon>0$ existe $\delta>0$ tal que

$$
x\in D,\quad |x-a|<\delta
\quad\Longrightarrow\quad |f(x)-f(a)|<\varepsilon.
$$

Si $a$ es punto de acumulación, esta condición equivale a $\lim_{x\to a,\,x\in D}f(x)=f(a)$. Si $a$ es aislado en $D$, la continuidad relativa se cumple automáticamente; no se debe inventar un límite de valores que no pueden aproximarse desde otros puntos del dominio.

La continuidad sobre $[a,b]$ exige continuidad relativa en cada punto del intervalo; en los extremos equivale a continuidad desde el lado que pertenece al dominio. Una función puede ser continua a un lado y no al otro. Por ejemplo, para $f(x)=0$ cuando $x\le0$ y $f(x)=1$ cuando $x>0$, los límites laterales en $0$ difieren: no existe límite bilateral ni continuidad en ese punto.

**Proposición 0.2 (criterio secuencial de continuidad; `EDC-C00-PRP-002`).** Una función $f:D\to\mathbb R$ es continua en $a\in D$ si y sólo si para toda sucesión $x_n\in D$ con $x_n\to a$ se tiene $f(x_n)\to f(a)$.

**Demostración.** Si $f$ es continua en $a$, para cada tolerancia $\varepsilon>0$ existe una distancia $\delta>0$ que controla $|f(x)-f(a)|$ siempre que $x\in D$ y $|x-a|<\delta$. Toda sucesión $x_n\in D$ que converge a $a$ cumple esa condición desde algún índice, luego $f(x_n)\to f(a)$.

Si la continuidad fallara, existiría una tolerancia $\varepsilon_0>0$ para la cual podríamos elegir, en cada entorno de radio $1/n$, un punto $x_n\in D$ con $|x_n-a|<1/n$ y $|f(x_n)-f(a)|\ge\varepsilon_0$. Los argumentos convergerían a $a$, mientras que sus valores no convergerían a $f(a)$, en contra de la condición supuesta. La prueba permite que algunos términos sean $a$ y comprende también el caso aislado; en éste, una sucesión del dominio que converge a $a$ termina tomando siempre ese valor. $\square$

**Proposición 0.3 (operaciones y composición; `EDC-C00-PRP-003`).** Sean $f,g:D\to\mathbb R$ continuas en $a\in D$. Entonces $f+g$ y $fg$ son continuas allí; si $g(a)\ne0$, la función $g$ no se anula en algún entorno relativo de $a$ y el cociente $f/g$ es continuo **en $a$**. Si $g:D\to E$ es continua en $a$ y $f:E\to\mathbb R$ es continua en $g(a)$, entonces $f\circ g$ es continua en $a$.

**Demostración.** Tomemos una sucesión $x_n\to a$ con términos en $D$. El criterio secuencial de continuidad da $f(x_n)\to f(a)$ y $g(x_n)\to g(a)$, y el Lema 0.1 permite sumar y multiplicar esas sucesiones conservando sus límites. Al aplicar de nuevo el criterio secuencial obtenemos la continuidad de $f+g$ y $fg$.

Si $g(a)\ne0$, la continuidad de $g$ permite elegir un entorno relativo de $a$ en el que $|g(x)-g(a)|<|g(a)|/2$; dentro de él se tiene $|g(x)|>|g(a)|/2$, y por tanto $g(x)\ne0$. El cociente está definido en ese entorno y la regla de cocientes del Lema 0.1 se aplica a las sucesiones de sus valores, lo que demuestra su continuidad en $a$.

Para la composición, la primera función lleva $x_n$ a una sucesión $g(x_n)\to g(a)$ con términos en $E$. La continuidad de la segunda en $g(a)$ permite entonces concluir $f(g(x_n))\to f(g(a))$, incluso si algunos términos coinciden con $g(a)$. El criterio secuencial demuestra que $f\circ g$ es continua en $a$. $\square$

Estas reglas permiten demostrar sin cálculo diferencial que los polinomios son continuos en toda la recta y las funciones racionales son continuas en los puntos de su dominio.

**Repertorio que encontraremos después.** Las potencias $x^m$ con $m\in\mathbb N$ son polinomios y su continuidad ya está justificada aquí. En cambio, al escribir $\sqrt{x}$ hay que exigir $x\ge0$, al escribir $\ln x$ hay que exigir $x>0$, y al escribir $x^r$ para $r\in\mathbb R$ arbitrario la base positiva evita problemas de definición. Las funciones $\exp x$, $\sin x$ y $\cos x$ se consideran en la recta real, pero no se empleará en este capítulo su continuidad como premisa no demostrada. Sus construcciones y los límites específicos que justifican sus reglas de derivación se presentarán en C02 o se reconstruirán explícitamente cuando el argumento los necesite. El dominio determina qué argumentos podemos aproximar y desde qué lados; el valor indica qué sucede en el punto, y el límite describe lo que sucede en sus proximidades. Mantener separados esos datos permitirá decidir qué afirmaciones sobre cada función están justificadas.

::: {.callout-note appearance="simple" icon="false" collapse="false" title="Historia — Cauchy y el arte de acercarse"}
*Lectura opcional.*

En 1821, Cauchy puso por escrito su *Cours d’analyse* para los alumnos de la École polytechnique. En los preliminares explicó el límite mediante una cantidad cuyos valores sucesivos se aproximan a un valor fijo hasta diferir de él tan poco como se quiera; entre sus ejemplos figuran las fracciones que aproximan un número irracional y los polígonos inscritos que aproximan el área de un círculo.

El movimiento entre valores enlazaba problemas de aritmética y geometría. En el capítulo II, Cauchy describió la continuidad mediante el efecto de un incremento infinitamente pequeño del argumento sobre el incremento de la función. Podemos reconocer allí la preocupación que acabamos de expresar con tolerancias y distancias: controlar cuánto cambia un valor cuando el argumento cambia poco.

Su introducción explica el cuidado que guía esos cálculos: las fórmulas algebraicas tienen condiciones de validez que deben determinarse. Para quien estaba aprendiendo a manejar procesos infinitos, saber cuándo podía usar una fórmula formaba parte de comprenderla.

**Para seguir leyendo:** [Cauchy, *Cours d’analyse* (1821), introducción, preliminares y capítulo II, §II](https://fr.wikisource.org/wiki/Cours_d’analyse_de_l’école_royale_polytechnique/Texte_entier).
:::

## 0.5. Dos teoremas que hacen posible el cálculo

La continuidad permite controlar los valores cerca de cada punto, pero también tiene consecuencias sobre un intervalo entero. Si una función pasa de un valor a otro, esperamos que alcance los que están entre ambos; si buscamos su mayor valor en un intervalo cerrado y acotado, esperamos encontrar un punto donde se alcance. Son expectativas distintas, y necesitamos demostrar cada una: la primera se resolverá buscando una frontera mediante el supremo; la segunda, seleccionando una subsucesión convergente entre los puntos que se acercan al valor extremo.

### 0.5.1. Valores intermedios

**Teorema 0.6 (valor intermedio; `EDC-C00-THM-006`).** Sean $a<b$ y $f:[a,b]\to\mathbb R$ continua. Si $y$ está estrictamente entre $f(a)$ y $f(b)$, existe $c\in(a,b)$ tal que $f(c)=y$.

**Demostración.** Podemos suponer $f(a)<y<f(b)$, pues el caso contrario se reduce a éste aplicando el argumento a $-f$. Busquemos el punto hasta el que puede llegar el conjunto de argumentos cuyos valores no sobrepasan $y$:

$$
A=\{x\in[a,b]:f(x)\le y\}.
$$

El conjunto contiene a $a$ y está acotado superiormente por $b$, de modo que existe $c=\sup A$ y $c\in[a,b]$. Elegir esta frontera permite usar la continuidad desde dos perspectivas: los puntos de $A$ se acercan a ella, pero ningún punto situado a su derecha puede pertenecer a $A$.

Por la caracterización del supremo, para cada $n$ elegimos $x_n\in A$ con $c-1/n<x_n\le c$. Así, $x_n\to c$ y, por continuidad, $f(x_n)\to f(c)$. Como $f(x_n)\le y$ para todos los índices, también $f(c)\le y$. En efecto, si $f(c)>y$, una tolerancia menor que la distancia entre ambos forzaría $f(x_n)>y$ para índices grandes, contradiciendo la elección de $x_n$.

Queda por excluir $f(c)<y$. En ese caso $c<b$, ya que $f(b)>y$, y la continuidad en $c$ conservaría los valores por debajo de $y$ en un entorno relativo: existe $\delta>0$ tal que $f(x)<y$ para $x\in[a,b]$ con $|x-c|<\delta$. Podemos escoger $z$ con $c<z<\min\{b,c+\delta\}$, pues ambos extremos de ese intervalo están ordenados estrictamente. Entonces $z\in A$, aunque $z>c$, en contra de que $c$ sea cota superior.

Se sigue que $f(c)=y$, y las desigualdades estrictas $f(a)<y<f(b)$ obligan a que $a<c<b$. $\square$

Hemos usado un hecho elemental sobre límites y orden: si $u_n\le y$ y $u_n\to u$, necesariamente $u\le y$; si no, la tolerancia $(u-y)/2$ produciría la contradicción. El valor intermedio no se extiende a una función meramente definida sobre racionales: la existencia de una frontera real puede ser exactamente lo que falta.

### 0.5.2. Valores extremos

**Teorema 0.7 (valores extremos; `EDC-C00-THM-007`).** Si $a<b$ y $f:[a,b]\to\mathbb R$ es continua, existen $u,v\in[a,b]$ tales que

$$
f(u)\le f(x)\le f(v)\qquad\text{para todo }x\in[a,b].
$$

En otras palabras, la función está acotada y alcanza su mínimo y su máximo.

**Demostración.** Para buscar el máximo mediante un supremo tenemos que demostrar primero que la imagen está acotada. Supongamos que no lo está en valor absoluto; podríamos elegir $x_n\in[a,b]$ con $|f(x_n)|>n$. Los argumentos, en cambio, sí forman una sucesión acotada, y Bolzano–Weierstrass proporciona una subsucesión $x_{n_k}\to c$. Como cada término pertenece a $[a,b]$, las desigualdades se conservan al pasar al límite y $c\in[a,b]$. Podemos aplicar por tanto la continuidad en $c$ y concluir $f(x_{n_k})\to f(c)$. Esa sucesión de valores tendría que estar acotada por el Lema 0.1, pero satisface $|f(x_{n_k})|>n_k\to\infty$, una contradicción.

La imagen es no vacía y acotada, luego existe $M=\sup f([a,b])$. El supremo es por ahora un número que acota los valores; falta encontrar un argumento que lo produzca. La propiedad aproximativa permite elegir $x_n\in[a,b]$ con $M-1/n<f(x_n)\le M$, cuyos valores convergen a $M$. Volvemos a usar Bolzano–Weierstrass para obtener $x_{n_k}\to v$, con $v\in[a,b]$. Por continuidad, $f(x_{n_k})\to f(v)$, mientras que las desigualdades anteriores obligan a que esa misma subsucesión de valores converja a $M$. La unicidad del límite da $f(v)=M$: el supremo se alcanza. Al aplicar este argumento a $-f$, su máximo corresponde al mínimo de $f$. $\square$

**Contraejemplos que delimitan el teorema.** La función $x\mapsto1/x$ es continua en $(0,1]$, pero no está acotada: no podemos omitir el extremo $0$ y conservar la conclusión. Por otra parte, $f(0)=0$ y $f(x)=1/x$ para $x\in(0,1]$ define una función sobre $[0,1]$ que no está acotada ni es continua en $0$: tampoco podemos suprimir la continuidad. El teorema no afirma que todo extremo esté en el interior, ni que en un extremo deba existir una tangente horizontal.

### 0.5.3. Un control cuantitativo uniforme

Cuando usamos la continuidad en un punto, la distancia $\delta$ puede depender tanto de la tolerancia como de ese punto. Para controlar muchas subdivisiones a la vez sería útil elegir una distancia que sirviera en cualquier parte del intervalo: así bastaría hacer pequeños todos los subintervalos para asegurar que la función cambia poco dentro de cada uno. En un intervalo cerrado y acotado la continuidad proporciona ese control común.

**Teorema 0.8 (continuidad uniforme en $[a,b]$; `EDC-C00-THM-008`).** Si $f:[a,b]\to\mathbb R$ es continua y $a<b$, entonces

$$
\forall\varepsilon>0\;\exists\delta>0\;\forall x,y\in[a,b]:
\quad |x-y|<\delta\Longrightarrow |f(x)-f(y)|<\varepsilon.
$$

Aquí $\delta$ depende de $\varepsilon$ pero **no** del lugar $x$ ni del lugar $y$.

**Demostración.** Si ninguna distancia común sirviera para una tolerancia $\varepsilon_0>0$, podríamos encontrar pares de argumentos cada vez más cercanos cuyos valores siguieran separados al menos por esa tolerancia. Para cada $n$ elegimos así $x_n,y_n\in[a,b]$ con $|x_n-y_n|<1/n$ y $|f(x_n)-f(y_n)|\ge\varepsilon_0$.

Como $(x_n)$ está acotada, Bolzano–Weierstrass proporciona una subsucesión $x_{n_k}\to c\in[a,b]$. Los puntos $y_{n_k}$ de los mismos pares tienen que acercarse a $c$, porque la distancia entre cada par tiende a cero. La desigualdad triangular lo confirma:

$$
|y_{n_k}-c|\le|y_{n_k}-x_{n_k}|+|x_{n_k}-c|\longrightarrow0.
$$

La continuidad en ese único punto $c$ da $f(x_{n_k})\to f(c)$ y $f(y_{n_k})\to f(c)$. Su diferencia debe tender a cero por el álgebra de límites, lo que contradice la separación $\varepsilon_0$ que conservan todos los pares. $\square$

El control uniforme se ha obtenido combinando la continuidad en un punto con la posibilidad de seleccionar una subsucesión convergente en el intervalo. En C05 permitirá pasar del comportamiento local de la función al control simultáneo de todas las piezas de una partición.

## 0.6. Las diferencias pequeñas no son diferencias nulas

Volvamos a la primera pregunta de §0.1. El cociente

$$
Q_h(a)=\frac{f(a+h)-f(a)}h,\qquad h\ne0,
$$

es una **tasa media de cambio** a lo largo de un incremento $h$. Si queremos obtener información sobre un solo punto, la división impide hacer coincidir directamente los dos argumentos: con $h=0$ deja de estar definida. El límite ofrece una operación distinta y bien justificada: investigar si $Q_h(a)$ se aproxima a un número cuando $h\to0$, manteniendo $h\neq0$ y los dos argumentos en el dominio de $f$.

En $f(x)=x^2$ obtuvimos $Q_h(a)=2a+h$. El límite existe. Para $f(x)=|x|$ en $a=0$, en cambio,

$$
Q_h(0)=\frac{|h|}{h}
=\begin{cases}1,&h>0,\\-1,&h<0.\end{cases}
$$

Los incrementos positivos producen siempre el valor $1$ y los negativos siempre el valor $-1$. Cada lado conserva así una inclinación diferente por mucho que acortemos el incremento, de modo que ningún número puede ser límite de todos esos cocientes. La punta que vemos en la gráfica corresponde a esta incompatibilidad calculable entre los dos lados.

Si pensamos en una posición $s(t)=t^2$ con $t\ge0$, la tasa media en un intervalo de duración $h>0$ es $2t+h$, y su límite por la derecha es $2t$. La unidad del cociente es «unidad de posición por unidad de tiempo»; las unidades de $s(t)$ y de $t$ no pueden confundirse. En $t=0$, además, el dominio físico impone una aproximación lateral, no una supuesta variación desde tiempos negativos.

La existencia del límite del cociente será la condición que nos permita definir la **derivada** en el capítulo 1. El contraste entre la parábola y el valor absoluto muestra por qué esa existencia debe examinarse: disponer de una función continua y poder calcular sus tasas medias no asegura que todas ellas se aproximen a una misma tasa local.

## 0.7. Las sumas finitas no son todavía una integral

La otra pregunta de §0.1 se refiere a la acumulación. Para la parábola $f(x)=x^2$ en $[0,1]$, las sumas de rectángulos de extremos izquierdos son

$$
L_n=\frac1n\sum_{k=0}^{n-1}\left(\frac{k}{n}\right)^2
=\frac{(n-1)(2n-1)}{6n^2}.
$$

Puesto que $f$ es creciente en $[0,1]$, los rectángulos izquierdos quedan debajo de la curva y los derechos por encima. Las fórmulas dan

$$
R_n-L_n=\frac1n,
\qquad L_n\longrightarrow\frac13,\quad R_n\longrightarrow\frac13.
$$

La diferencia $1/n$ mide la separación entre las dos sumas y tiende a cero, mientras que ambas se aproximan a $1/3$. Para esta región, los rectángulos de abajo y los de arriba van estrechando un mismo valor. Sin embargo, el éxito depende del comportamiento de la función: podemos construir otra para la cual dos elecciones de alturas produzcan resultados separados incluso cuando los subintervalos sean muy pequeños. La construcción utiliza un hecho aritmético sobre los puntos que encontramos en cualquier intervalo.

**Lema 0.3 (densidad de racionales e irracionales; `EDC-C00-LEM-003`).** Todo intervalo abierto no vacío $(a,b)$ contiene un número racional y un número irracional.

**Demostración.** Para encontrar un racional de la forma $m/n$ entre $a$ y $b$, queremos que el intervalo multiplicado por $n$ tenga longitud mayor que uno: así podremos situar un entero entre sus extremos. Por la propiedad arquimediana elegimos $n\in\mathbb N$ con $n(b-a)>1$. Sea $m$ el primer entero estrictamente mayor que $na$; entonces $na<m\le na+1$, pues de otro modo $m-1$ también superaría a $na$. Como $na+1<nb$, obtenemos $a<m/n<b$.

Para justificar la existencia de ese primer entero, podemos escoger un natural de gran valor que deje a $na$ entre dos enteros opuestos. Los enteros de ese intervalo son finitos en número y alguno supera a $na$; el menor de los que lo superan es también el menor entre todos los enteros que lo hacen. Hemos encontrado un racional sin presuponer la densidad que queríamos demostrar.

Apliquemos el resultado al intervalo trasladado $(a-\sqrt2,b-\sqrt2)$. Contiene un racional $q$, y entonces $q+\sqrt2\in(a,b)$. Este último número es irracional, pues si fuera racional, al restarle $q$ obtendríamos un valor racional para $\sqrt2$, contra lo demostrado en §0.2.3. $\square$

Definamos $d:[0,1]\to\mathbb R$ mediante

$$
d(x)=\begin{cases}1,&x\in\mathbb Q,\\0,&x\notin\mathbb Q.\end{cases}
$$

Dividamos $[0,1]$ en cualquier número finito de intervalos de anchura positiva. En cada uno podemos escoger como muestra un racional, y la suma de alturas por anchuras será exactamente $1$. Pero podemos escoger muestras irracionales en todos ellos, y la suma resultante será $0$. Las subdivisiones pueden hacerse arbitrariamente finas y la divergencia permanece. **No existe un valor común forzado por estas aproximaciones.**

Una definición de integral tendrá que exigir que el resultado quede determinado pese a la libertad de escoger las muestras. Para la parábola, las aproximaciones inferiores y superiores nos han dado una forma de controlar esa libertad; para la función recién construida, la separación persiste en cualquier partición. En C04–C05 estudiaremos cómo convertir ese contraste en un criterio preciso de existencia.

Hay, además, una coincidencia sugerente para la parábola. Definamos la función polinómica $F(x)=x^3/3$. Para $h\neq0$,

$$
\frac{F(x+h)-F(x)}h=x^2+xh+\frac{h^2}3\longrightarrow x^2.
$$

El cociente incremental de $F$ reproduce, al pasar al límite, las alturas $x^2$ que utilizamos en las sumas rectangulares. Además, el cambio de $F$ entre los extremos $0$ y $1$ es $1/3$, el mismo valor al que convergen esas sumas. La coincidencia hace visible una posible relación entre acumular alturas y recuperar una tasa de cambio, pero nuestro cálculo sólo la ha comprobado para un polinomio. Para establecer el Teorema Fundamental del Cálculo en C06 habrá que definir la acumulación para una clase de funciones, demostrar su existencia y justificar qué condiciones permiten recuperar la función inicial mediante ese límite.

## 0.8. Un puente histórico y el camino que sigue

Los problemas de cuadratura y los de tangentes no son invenciones de un curso moderno de cálculo. La cuadratura de regiones curvilíneas cuenta con antecedentes antiguos, entre ellos el estudio de Arquímedes del segmento parabólico. En la matemática europea de los siglos XVI y XVII se desarrollaron asimismo procedimientos para tangentes, cuadraturas y magnitudes variables; Newton y Leibniz fueron decisivos para articular parte de esas investigaciones en métodos generales, aunque con conceptos y lenguajes distintos de los actuales. Los cálculos de este capítulo permiten comprender problemas que también interesaron a esos matemáticos, aunque para conocer sus respuestas tenemos que acudir a sus textos y examinar los recursos con los que trabajaban.

Nuestro orden de estudio responde a las dependencias de las demostraciones: comenzamos por el límite porque permite justificar los procedimientos que construiremos después. La historia recorrió otros caminos, y muchas cuadraturas, técnicas de tangentes y expansiones en serie precedieron a las definiciones con las que hoy las examinamos. Podemos aprender de esas investigaciones sin hacerlas hablar con nuestras palabras: el agotamiento geométrico, los indivisibles y las fluxiones merecen entenderse dentro de sus propios argumentos, mientras que las pruebas con $\varepsilon$ y $\delta$ que ofrecemos aquí pertenecen a la exposición moderna.

Las pruebas han mostrado dónde interviene la completitud: al obtener una frontera mediante el supremo y al retener puntos dentro de intervalos cada vez menores. La continuidad permite después llevar a los valores de la función lo que hemos demostrado sobre sus argumentos. Podemos reunir esas dependencias en la cadena

$$
\text{completitud de }\mathbb R
\Longrightarrow
\begin{cases}
\text{principio arquimediano y convergencia monótona},\\
\text{intervalos encajados y Bolzano--Weierstrass}
\end{cases}
\Longrightarrow
\begin{cases}
\text{valor intermedio},\\
\text{valores extremos},\\
\text{continuidad uniforme en }[a,b].
\end{cases}
$$

En los dos cálculos con la parábola ya podemos justificar qué significa el valor al que nos acercamos. También hemos encontrado funciones para las que las aproximaciones laterales son incompatibles o las muestras mantienen separadas las sumas. Al definir la derivada y la integral tendremos que recoger ambas experiencias: la posibilidad de obtener un valor determinado y las condiciones que hacen posible esa determinación.

### Mapa de dependencias y lecturas de trabajo

- **Fundamento adoptado:** axiomas de cuerpo ordenado y completitud de $\mathbb R$, aritmética de $\mathbb N$ e identidades algebraicas finitas. No se utiliza derivación, integración, Taylor, teorema de Rolle ni Teorema Fundamental.
- **Resultados derivados:** `EDC-C00-THM-001` → `EDC-C00-THM-002` y `EDC-C00-THM-003` → `EDC-C00-THM-004`; `EDC-C00-THM-005` y `EDC-C00-PRP-002` permiten transportar límites/continuidad; `EDC-C00-THM-006--008` requieren continuidad y completitud en intervalos cerrados de la recta.
- **Uso posterior:** C01 y C02 usarán límites y continuidad; C03, valores extremos; C04–C05, completitud, extremos y continuidad uniforme; C06, lo anterior junto con la teoría diferencial e integral ya construida.
- **Lecturas complementarias:** Gabor Toth, *Elements of Mathematics* (2021), lectura previa o paralela recomendada. Ninguna de estas lecturas es requisito para validar las demostraciones presentes.

**Trabajo del lector.** Los [ejercicios de este capítulo](capitulo-00-ejercicios.html) desarrollan la lectura precisa de cuantificadores, la búsqueda de contraejemplos, el uso de completitud y la interpretación de sumas y cocientes. Sus desarrollos completos están separados en [soluciones](capitulo-00-soluciones.html) para no interrumpir la exposición.
