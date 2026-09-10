## Qué fuerza tiene converger: unicidad, colas y acotación {#sec-t1-c04-03}

La definición $\varepsilon$–$N$ parece, a primera vista, exigir únicamente que una sucesión se acerque a cierto número. Sin embargo, esa exigencia tiene consecuencias mucho más fuertes de lo que sugiere la intuición inicial.

En esta sección responderemos tres preguntas.

1. Si una sucesión converge, ¿puede tener dos límites distintos?
2. Si alteramos solamente una cantidad finita de términos, ¿podemos cambiar su convergencia?
3. ¿Puede una sucesión convergente tener términos de tamaño arbitrariamente grande?

Las respuestas serán, respectivamente,

$$
\boxed{
\text{no},\qquad
\text{no},\qquad
\text{no}.
}
$$

Lo importante no será solo conocer estas conclusiones. Cada prueba revelará un patrón de razonamiento que reutilizaremos durante todo el cálculo.

### Una sucesión no puede acercarse indefinidamente a dos números distintos

Supongamos que una sucesión $(a_n)$ convergiera a dos números reales $L$ y $M$.

Si $L\ne M$, existe una distancia positiva entre ellos:

$$
|L-M|>0.
$$

La definición de convergencia permitiría entonces exigir simultáneamente que, a partir de cierto momento, los términos de la sucesión estén muy cerca de $L$ y muy cerca de $M$.

Pero dos entornos suficientemente pequeños alrededor de puntos distintos no pueden compartir un mismo punto.

Esta observación geométrica se convertirá en una contradicción mediante la desigualdad triangular.

::: {#thm-t1-0009}
**Unicidad del límite secuencial.** Sea $(a_n)_{n\ge n_0}$ una sucesión real. Si

$$
a_n\to L
$$

y también

$$
a_n\to M,
$$

entonces

$$
L=M.
$$

**Demostración.** Supongamos, buscando una contradicción, que

$$
L\ne M.
$$

Entonces

$$
d:=|L-M|>0.
$$

Elegimos la tolerancia

$$
\varepsilon=\frac d3.
$$

Como $a_n\to L$, existe un índice $N_L\ge n_0$ tal que, para todo $n\ge N_L$,

$$
|a_n-L|<\frac d3.
$$

Como también $a_n\to M$, existe un índice $N_M\ge n_0$ tal que, para todo $n\ge N_M$,

$$
|a_n-M|<\frac d3.
$$

Tomemos

$$
N=\max\{N_L,N_M\}.
$$

Entonces, para todo $n\ge N$, ambas desigualdades se cumplen simultáneamente. Fijemos uno de esos índices. Por la desigualdad triangular,

$$
|L-M|
\le |L-a_n|+|a_n-M|.
$$

Por las estimaciones anteriores,

$$
|L-M|
<\frac d3+\frac d3
=\frac{2d}{3}.
$$

Pero $|L-M|=d$, de modo que obtenemos

$$
d<\frac{2d}{3},
$$

lo cual es imposible porque $d>0$.

Por tanto, la suposición $L\ne M$ era falsa y necesariamente

$$
L=M.
$$
:::

La prueba merece ser leída por su arquitectura, no solo por su resultado.

**Objetivo.** Queríamos demostrar que dos supuestos límites debían coincidir.

**Estrategia.** Supusimos que eran distintos y convertimos su distancia positiva en una tolerancia.

**Paso decisivo.** La convergencia a $L$ y a $M$ produce dos umbrales distintos. El máximo

$$
N=\max\{N_L,N_M\}
$$

permite entrar simultáneamente en ambas colas.

**Contradicción.** Un mismo término $a_n$ no puede estar a menos de $d/3$ de ambos extremos de un segmento cuya longitud es $d$.

Podríamos haber usado, por ejemplo, $\varepsilon=d/4$. Lo esencial es elegir una tolerancia tal que dos errores sumados sigan siendo estrictamente menores que $d$.

La elección

$$
\varepsilon=\frac d2
$$

sería menos conveniente para esta prueba tal como está escrita: produciría solamente

$$
|L-M|<\frac d2+\frac d2=d,
$$

que sigue siendo una contradicción porque las desigualdades son estrictas, pero deja el argumento exactamente en la frontera. Elegir $d/3$ hace visible un margen positivo y prepara un hábito útil: cuando una desigualdad triangular divide un error entre varias partes, conviene reservar espacio suficiente para todas ellas.

A partir de ahora, gracias a la unicidad, tiene sentido escribir

$$
\lim_{n\to\infty}a_n=L
$$

sin ambigüedad: si el límite real existe, hay uno solo.

### La convergencia pertenece a la cola

En §4.1 vimos que una propiedad eventual no depende de un prefijo finito. La convergencia está formulada precisamente mediante propiedades eventuales:

$$
\forall\varepsilon>0\;\exists N\;\forall n\ge N:
|a_n-L|<\varepsilon.
$$

Por eso modificar algunos términos iniciales no puede destruir una convergencia ya existente ni fabricar un límite diferente.

Conviene formular esta estabilidad de manera algo más general.

::: {#prp-t1-0019}
**Coincidencia eventual y estabilidad de la convergencia.** Sean $(a_n)$ y $(b_n)$ dos sucesiones reales definidas, al menos, a partir de algún índice común $n_0$. Supongamos que coinciden eventualmente; es decir, existe $K\ge n_0$ tal que

$$
a_n=b_n
\qquad
\text{para todo }n\ge K.
$$

Entonces, para todo $L\in\mathbb R$,

$$
a_n\to L
\quad\Longleftrightarrow\quad
b_n\to L.
$$

En particular, cambiar una cantidad finita de términos de una sucesión no modifica su convergencia ni su límite.

**Demostración.** Supongamos primero que

$$
a_n\to L.
$$

Sea $\varepsilon>0$. Por convergencia existe $N_a\ge n_0$ tal que

$$
n\ge N_a
\quad\Longrightarrow\quad
|a_n-L|<\varepsilon.
$$

Definimos

$$
N=\max\{N_a,K\}.
$$

Si $n\ge N$, entonces simultáneamente

$$
n\ge N_a
$$

y

$$
n\ge K.
$$

La primera desigualdad da

$$
|a_n-L|<\varepsilon,
$$

y la segunda garantiza que

$$
b_n=a_n.
$$

Por tanto,

$$
|b_n-L|
=|a_n-L|
<\varepsilon.
$$

Hemos demostrado que $b_n\to L$.

El argumento inverso es idéntico, intercambiando los papeles de $(a_n)$ y $(b_n)$. Por consiguiente,

$$
a_n\to L
\quad\Longleftrightarrow\quad
b_n\to L.
$$
:::

El mecanismo de la prueba puede resumirse en una sola operación:

$$
\boxed{
\text{umbral de convergencia}
+
\text{umbral de coincidencia}
\longrightarrow
\max\{N_a,K\}.
}
$$

Este uso del máximo aparecerá constantemente. Siempre que varias propiedades sean verdaderas eventualmente, podemos hacerlas verdaderas **simultáneamente** avanzando hasta el mayor de sus umbrales.

#### Quitar o añadir una cantidad finita de términos

La proposición anterior tiene una consecuencia inmediata. Si

$$
a_n\to L,
$$

entonces cualquier cola

$$
(a_n)_{n\ge K}
$$

converge al mismo $L$.

Recíprocamente, si alguna cola de la sucesión converge a $L$, entonces la sucesión completa también converge a $L$: los términos anteriores a $K$ forman solo un prefijo finito y no intervienen en ninguna condición que deba cumplirse desde un umbral suficientemente tardío.

Así,

$$
\boxed{
(a_n)\text{ converge a }L
\quad\Longleftrightarrow\quad
\text{cualquier cola de }(a_n)\text{ converge a }L.
}
$$

Esta equivalencia expresa con precisión una frase que utilizaremos muchas veces:

> para estudiar un límite podemos descartar una cantidad finita de términos iniciales.

Descartar no significa borrar información del objeto original. Significa que esa información no afecta la pregunta específica de convergencia.

#### Desplazar los índices tampoco cambia el límite

Sea $r\in\mathbb N$ fijo y, para $n\ge n_0$, definamos

$$
b_n=a_{n+r}.
$$

La sucesión $(b_n)$ recorre los mismos términos que una cola de $(a_n)$, pero vuelve a numerarlos comenzando en un índice anterior.

Demostremos directamente que

$$
a_n\to L
\quad\Longleftrightarrow\quad
b_n\to L.
$$

Supongamos que $a_n\to L$ y sea $\varepsilon>0$. Existe $N$ tal que

$$
m\ge N
\quad\Longrightarrow\quad
|a_m-L|<\varepsilon.
$$

Si elegimos un índice $n$ suficientemente grande para que

$$
n+r\ge N,
$$

entonces

$$
|b_n-L|
=|a_{n+r}-L|
<\varepsilon.
$$

Por ejemplo, basta tomar

$$
N_b=\max\{n_0,N-r\}.
$$

En la dirección contraria, si $b_n\to L$, entonces existe un umbral $N_b$ después del cual

$$
|a_{n+r}-L|<\varepsilon.
$$

Para todo

$$
m\ge N_b+r,
$$

podemos escribir $m=n+r$ con $n=m-r\ge N_b$, y obtenemos

$$
|a_m-L|<\varepsilon.
$$

Por tanto, desplazar una cantidad fija de posiciones el índice tampoco altera el límite.

Este hecho será decisivo cuando estudiemos recurrencias: si

$$
a_n\to L,
$$

entonces también

$$
a_{n+1}\to L.
$$

No estamos usando continuidad ni álgebra de límites. Es una consecuencia directa de que quitar el primer término no cambia el comportamiento de la cola.

### Convergencia no significa que todos los términos estén cerca del límite

La estabilidad bajo modificaciones finitas corrige una intuición frecuente.

Una sucesión convergente puede comenzar con términos enormes o completamente irregulares. Por ejemplo, definamos

$$
a_0=10^{100},
\qquad
a_1=-10^{50},
\qquad
a_2=37,
$$

y, para $n\ge3$,

$$
a_n=\frac1{n+1}.
$$

Como la cola coincide con la sucesión ya estudiada $1/(n+1)$, tenemos

$$
a_n\to0.
$$

Los primeros términos pueden estar muy lejos de $0$ sin afectar el límite.

La convergencia no dice

$$
|a_n-L|<\varepsilon
\qquad
\text{para todo }n.
$$

Dice que, para cada tolerancia, esa desigualdad termina siendo verdadera **eventualmente**.

Esta distinción será importante en la siguiente prueba. La convergencia controlará automáticamente una cola, pero para obtener una afirmación sobre **todos** los términos deberemos tratar por separado el prefijo finito restante.

### Acotación: encerrar todos los términos en un intervalo fijo

Hasta ahora hemos utilizado cotas para conjuntos de números reales. Como una sucesión es una función, también podemos preguntar si su conjunto de valores permanece dentro de una región finita de la recta.

::: {#def-t1-0029}
**Sucesión acotada.** Sea $(a_n)_{n\ge n_0}$ una sucesión real. Diremos que $(a_n)$ es **acotada** si existe un número $M>0$ tal que

$$
|a_n|\le M
\qquad
\text{para todo }n\ge n_0.
$$

Equivalentemente, existe $M>0$ tal que todos los términos pertenecen al intervalo

$$
[-M,M].
$$
:::

La constante $M$ debe ser **una sola cota para toda la sucesión**. No sería suficiente permitir una cota distinta para cada término: para cualquier número real $a_n$ podríamos elegir trivialmente $M_n=|a_n|+1$, y esa condición no expresaría ningún control global.

En lenguaje de funciones, la definición equivale a afirmar que la imagen

$$
\{a_n:n\ge n_0\}
$$

es un subconjunto acotado de $\mathbb R$.

También podemos separar cotas superiores e inferiores. Una sucesión es acotada si existen números $m,M\in\mathbb R$ tales que

$$
m\le a_n\le M
\qquad
\text{para todo }n\ge n_0.
$$

La forma simétrica

$$
|a_n|\le C
$$

es especialmente cómoda porque reúne ambas desigualdades en una sola expresión.

### Toda sucesión convergente es acotada

La definición de convergencia ya contiene casi toda la prueba.

Si

$$
a_n\to L,
$$

podemos escoger una tolerancia concreta, por ejemplo

$$
\varepsilon=1.
$$

Entonces, desde algún índice $N$,

$$
|a_n-L|<1.
$$

La desigualdad triangular da

$$
|a_n|
\le |a_n-L|+|L|
<1+|L|.
$$

Así, toda la cola está acotada por $|L|+1$.

Pero la definición de sucesión acotada exige controlar **todos** los términos, incluidos los anteriores a $N$. Aquí aparece el segundo ingrediente: antes de $N$ solo hay una cantidad finita de términos, y una cantidad finita de números reales siempre admite un máximo de sus valores absolutos.

::: {#prp-t1-0020}
**Toda sucesión convergente es acotada.** Si

$$
a_n\to L,
$$

entonces la sucesión $(a_n)$ es acotada.

**Demostración.** Como $a_n\to L$, podemos aplicar la definición con la tolerancia

$$
\varepsilon=1.
$$

Existe entonces un índice $N_0\ge n_0$ tal que

$$
n\ge N_0
\quad\Longrightarrow\quad
|a_n-L|<1.
$$

Si fuera necesario, reemplazamos $N_0$ por

$$
N=\max\{N_0,n_0+1\}.
$$

La propiedad anterior sigue siendo válida para $n\ge N$, y ahora existe al menos un término en el prefijo que va desde $n_0$ hasta $N-1$.

Para todo $n\ge N$, por la desigualdad triangular,

$$
|a_n|
\le |a_n-L|+|L|
<1+|L|.
$$

Por otra parte, los términos

$$
a_{n_0},a_{n_0+1},\dots,a_{N-1}
$$

son finitos en número. Por tanto existe el máximo

$$
M_0
=
\max\{|a_{n_0}|,|a_{n_0+1}|,\dots,|a_{N-1}|\}.
$$

Definamos

$$
M=\max\{M_0,|L|+1\}.
$$

Entonces $M>0$ y controla ambas regiones:

- si $n_0\le n<N$, tenemos $|a_n|\le M_0\le M$;
- si $n\ge N$, tenemos $|a_n|<|L|+1\le M$.

En consecuencia,

$$
|a_n|\le M
\qquad
\text{para todo }n\ge n_0.
$$

Por definición, $(a_n)$ es acotada.
:::

Esta demostración contiene un patrón que conviene conservar:

$$
\boxed{
\text{controlar la cola}
+
\text{controlar el prefijo finito}
\longrightarrow
\text{control global}.
}
$$

La convergencia proporciona el primer control. La finitud del prefijo proporciona el segundo.

Observe también que no necesitábamos la definición completa para **todas** las tolerancias. Para demostrar acotación bastó utilizar una sola, $\varepsilon=1$. Una definición universal puede tener consecuencias que se obtienen seleccionando estratégicamente un caso particular.

### Qué hipótesis usamos realmente en la prueba de acotación

Es útil auditar el argumento.

1. **Convergencia.** Se usó para encontrar una cola dentro de distancia $1$ de $L$.
2. **Desigualdad triangular.** Transformó una cota sobre $|a_n-L|$ en una cota sobre $|a_n|$.
3. **Finitud del prefijo.** Permitió tomar el máximo de los términos no controlados por la cola.

No se utilizó completitud, monotonía, álgebra de límites ni ningún teorema posterior.

La prueba es, por tanto, una consecuencia muy temprana y directa de la definición $\varepsilon$–$N$.

### La recíproca es falsa

Acabamos de demostrar

$$
\boxed{
\text{convergente}\Longrightarrow\text{acotada}.
}
$$

No debemos invertir automáticamente la implicación.

La sucesión

$$
a_n=(-1)^n
$$

satisface

$$
|a_n|=1
$$

para todo $n$. Por tanto es acotada, con $M=1$.

Sin embargo, en §4.2 demostramos directamente que diverge.

Así,

$$
\boxed{
\text{acotada}\centernot\Longrightarrow\text{convergente}.
}
$$

Esta separación será fundamental más adelante. La acotación impide que los términos escapen indefinidamente en tamaño, pero no impide que sigan oscilando entre regiones distintas.

### Convergencia tampoco significa monotonía

Otra confusión frecuente consiste en imaginar una sucesión convergente como una lista de términos que se aproxima al límite siempre desde el mismo lado y en una sola dirección.

La definición no exige nada semejante.

::: {#exm-t1-0034}
**Dos separaciones esenciales: convergencia sin monotonía y acotación sin convergencia.**

Consideremos primero

$$
a_n=\frac{(-1)^n}{n+1}.
$$

Para todo $n$,

$$
|a_n-0|
=\frac1{n+1}.
$$

Dado $\varepsilon>0$, en §4.2 ya construimos un umbral $N$ tal que

$$
n\ge N
\quad\Longrightarrow\quad
\frac1{n+1}<\varepsilon.
$$

El mismo umbral produce

$$
|a_n|<\varepsilon.
$$

Por tanto,

$$
\frac{(-1)^n}{n+1}\to0.
$$

Pero la sucesión no es creciente ni decreciente. Sus tres primeros términos son

$$
1,-\frac12,\frac13,
$$

de modo que

$$
a_0>a_1
$$

y también

$$
a_1<a_2.
$$

Una sucesión creciente no podría presentar la primera desigualdad, y una decreciente no podría presentar la segunda. Así, $(a_n)$ converge pero no es monótona.

Consideremos ahora

$$
b_n=(-1)^n.
$$

Como

$$
|b_n|=1
$$

para todo $n$, la sucesión es acotada. Sin embargo, @exm-t1-0033 demostró que no converge a ningún número real.

Tenemos entonces dos contraejemplos complementarios:

$$
\boxed{
\text{convergente}\centernot\Longrightarrow\text{monótona},
}
$$

$$
\boxed{
\text{acotada}\centernot\Longrightarrow\text{convergente}.
}
$$
:::

Estos ejemplos muestran que conviene mantener separadas tres propiedades:

- **convergencia:** toda cola suficientemente tardía queda dentro de cualquier tolerancia alrededor de un único $L$;
- **acotación:** todos los términos permanecen dentro de algún intervalo fijo;
- **monotonía:** los términos respetan sistemáticamente un sentido de orden entre índices consecutivos o cualesquiera índices ordenados.

Ninguna de estas frases es sinónimo de las otras.

Más adelante aparecerá una interacción mucho más profunda: una sucesión **monótona y acotada** sí tendrá que converger. Esa afirmación requerirá la completitud de $\mathbb R$ y será uno de los resultados centrales del capítulo. Todavía no podemos usarla.

### Una primera red de implicaciones

Con los resultados disponibles hasta ahora podemos escribir:

$$
\boxed{
\begin{array}{c}
 a_n\to L\\[2pt]
 \Downarrow\\[2pt]
 \text{límite único}\quad+\quad\text{acotación}\quad+\quad\text{estabilidad de colas}
\end{array}
}
$$

Pero no podemos añadir las flechas recíprocas sin hipótesis adicionales.

En particular:

$$
\text{acotada}\centernot\Longrightarrow\text{convergente},
$$

$$
\text{convergente}\centernot\Longrightarrow\text{monótona}.
$$

Y la unicidad no afirma existencia: decir que **si** existe un límite entonces es único no demuestra que una sucesión dada converja.

Esta distinción entre existencia y unicidad retoma una estructura lógica que ya apareció en `T1-C01`. El @thm-t1-0009 resuelve solamente la parte de «a lo sumo uno». Para establecer que una sucesión concreta tiene límite todavía necesitamos demostrar existencia mediante la definición o mediante resultados que construiremos después.

### Qué hemos ganado

La definición de §4.2 ya no es una pieza aislada. Ha producido tres herramientas generales:

1. **Unicidad:** si una sucesión converge, no hay ambigüedad acerca de su límite.
2. **Estabilidad de cola:** eliminar, añadir o modificar finitos términos no afecta el límite; desplazar el índice una cantidad fija tampoco.
3. **Acotación:** toda sucesión convergente permanece globalmente dentro de algún intervalo finito.

Estas propiedades permitirán que, a partir de la próxima sección, dejemos de volver a la definición $\varepsilon$–$N$ para cada cálculo elemental.

El siguiente problema será demostrar que las operaciones algebraicas respetan los límites. Si

$$
a_n\to A
$$

y

$$
b_n\to B,
$$

¿podemos concluir que

$$
a_n+b_n\to A+B,
$$

$$
a_nb_n\to AB,
$$

o que

$$
\frac{a_n}{b_n}\to\frac AB?
$$

La respuesta será afirmativa bajo las hipótesis adecuadas, pero la prueba del producto revelará por qué la acotación que acabamos de establecer no era un resultado accesorio: será exactamente la herramienta necesaria para controlar un factor variable.

