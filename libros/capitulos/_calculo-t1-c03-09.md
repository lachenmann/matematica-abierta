## Monotonía e inversas sobre intervalos {#sec-t1-c03-09}

Hasta ahora hemos estudiado funciones atendiendo a cómo asignan valores, cómo se componen, cuándo son inyectivas o sobreyectivas, cómo pueden invertirse y cómo se representan mediante gráficas. Falta incorporar una estructura que todavía no hemos utilizado de manera sistemática: **el orden de las entradas y de las salidas**.

Si el dominio es un subconjunto ordenado de $\mathbb R$, podemos comparar dos entradas $x_1<x_2$ y preguntar qué relación existe entre $f(x_1)$ y $f(x_2)$. Una función puede conservar el orden, invertirlo, conservarlo solo débilmente o no obedecer ningún patrón global de este tipo.

Esta pregunta conduce a la noción de **monotonía**.

### Comparar entradas para comparar salidas

Consideremos primero dos ejemplos sencillos.

Para

$$
f(x)=2x+1,
$$

si $x_1<x_2$, entonces

$$
2x_1+1<2x_2+1,
$$

de modo que el orden de las entradas se conserva estrictamente.

En cambio, para

$$
g(x)=-3x+4,
$$

si $x_1<x_2$, al multiplicar por $-3$ se invierte la desigualdad:

$$
-3x_1>-3x_2,
$$

y por tanto

$$
g(x_1)>g(x_2).
$$

Aquí el orden se invierte estrictamente.

Hay también situaciones en las que el orden solo se conserva de manera débil. Una función puede tener dos entradas distintas con la misma salida y, aun así, no disminuir nunca.

Por eso necesitamos distinguir cuidadosamente las versiones débiles de las estrictas.

::: {#def-t1-0026}
**Monotonía.** Sea $D\subseteq\mathbb R$ y sea

$$
f\colon D\to\mathbb R.
$$

Diremos que $f$ es:

1. **no decreciente** en $D$ si, para cualesquiera $x_1,x_2\in D$,
   $$
   x_1<x_2
   \Longrightarrow
   f(x_1)\le f(x_2);
   $$

2. **estrictamente creciente** en $D$ si
   $$
   x_1<x_2
   \Longrightarrow
   f(x_1)<f(x_2);
   $$

3. **no creciente** en $D$ si
   $$
   x_1<x_2
   \Longrightarrow
   f(x_1)\ge f(x_2);
   $$

4. **estrictamente decreciente** en $D$ si
   $$
   x_1<x_2
   \Longrightarrow
   f(x_1)>f(x_2).
   $$

Una función se llama **monótona** cuando es no decreciente o no creciente, y **estrictamente monótona** cuando es estrictamente creciente o estrictamente decreciente.
:::

La terminología varía ligeramente entre libros: algunos autores usan «creciente» para la versión débil y otros para la estricta. Para evitar ambigüedades, en este libro escribiremos siempre **no decreciente**, **no creciente**, **estrictamente creciente** o **estrictamente decreciente** cuando la distinción sea relevante.

### El dominio debe estar ordenado

La definición anterior no depende de que $D$ sea un intervalo. Solo necesita que tenga sentido comparar dos elementos mediante $<$.

Por ejemplo, podríamos estudiar monotonía en

$$
D=\{-3,-1,2,7\}.
$$

Sin embargo, en análisis trabajaremos con especial frecuencia sobre **intervalos**, porque allí no hemos eliminado artificialmente puntos intermedios del dominio. Por esa razón el título de esta sección habla de monotonía sobre intervalos.

Conviene separar desde ahora dos afirmaciones:

$$
\boxed{
\begin{array}{c}
\text{la definición de monotonía necesita orden;}\\[4pt]
\text{muchos teoremas posteriores necesitarán además que el dominio sea un intervalo.}
\end{array}}
$$

El primer teorema de esta sección pertenece al primer grupo: ni siquiera necesita que el dominio sea un intervalo.

### Por qué la monotonía estricta impide repeticiones

En §3.3 definimos la inyectividad mediante

$$
f(x_1)=f(x_2)
\Longrightarrow
x_1=x_2.
$$

Ahora disponemos de una condición diferente, expresada mediante desigualdades. La pregunta natural es:

> si la función separa estrictamente las salidas cada vez que ordenamos dos entradas distintas, ¿pueden dos entradas distintas producir la misma salida?

La respuesta es negativa.

::: {#thm-t1-0008}
**Toda función estrictamente monótona es inyectiva.** Sea $D\subseteq\mathbb R$ y sea

$$
f\colon D\to\mathbb R.
$$

Si $f$ es estrictamente creciente o estrictamente decreciente en $D$, entonces $f$ es inyectiva.
:::

**Idea de la prueba.** Queremos demostrar que entradas distintas no pueden compartir una salida. Como $\mathbb R$ está ordenado, si $x_1\ne x_2$, entonces necesariamente ocurre una de las dos posibilidades

$$
x_1<x_2
\qquad\text{o}\qquad
x_2<x_1.
$$

La monotonía estricta convierte cualquiera de esas desigualdades entre entradas en una desigualdad estricta entre salidas. Por tanto, las salidas no pueden ser iguales.

**Demostración.** Supongamos primero que $f$ es estrictamente creciente. Sean $x_1,x_2\in D$ con

$$
x_1\ne x_2.
$$

Por el orden total de $\mathbb R$, o bien $x_1<x_2$ o bien $x_2<x_1$.

Si $x_1<x_2$, la monotonía estricta da

$$
f(x_1)<f(x_2),
$$

y por tanto

$$
f(x_1)\ne f(x_2).
$$

Si $x_2<x_1$, obtenemos análogamente

$$
f(x_2)<f(x_1),
$$

de nuevo con

$$
f(x_1)\ne f(x_2).
$$

Así, entradas distintas producen salidas distintas y $f$ es inyectiva.

Si $f$ es estrictamente decreciente, el argumento es idéntico salvo por el sentido de las desigualdades: de $x_1<x_2$ se sigue

$$
f(x_1)>f(x_2),
$$

y de $x_2<x_1$ se sigue

$$
f(x_2)>f(x_1).
$$

En ambos casos las salidas son diferentes. Por tanto, $f$ también es inyectiva. $\square$

::: {.callout-note title="Después de la prueba"}
La demostración no utilizó completitud, intervalos, continuidad, límites ni derivadas. Solo necesitó:

- que el dominio esté contenido en un conjunto totalmente ordenado;
- la definición de monotonía estricta.

La razón estructural es muy simple:

$$
\boxed{
\text{entradas distintas}
\Longrightarrow
\text{entradas comparables}
\Longrightarrow
\text{salidas estrictamente distintas}.}
$$
:::

### Por qué «estrictamente» no puede borrarse

Una función no decreciente puede conservar el orden débilmente y, sin embargo, repetir valores.

El ejemplo más simple es la función constante

$$
c\colon\mathbb R\to\mathbb R,
\qquad
c(x)=5.
$$

Si $x_1<x_2$, entonces

$$
c(x_1)=5\le5=c(x_2),
$$

de modo que $c$ es no decreciente. También es no creciente. Pero no es inyectiva, porque

$$
c(0)=c(1)=5.
$$

Por tanto,

$$
\boxed{
\text{no decreciente}
\centernot\Longrightarrow
\text{inyectiva}.}
$$

Lo mismo ocurre con «no creciente». La desigualdad estricta del teorema no es una comodidad estilística: es la condición que impide los tramos horizontales y, algebraicamente, impide que dos entradas ordenadas tengan la misma salida.

### Una vía natural hacia la inversa

Supongamos ahora que $I\subseteq\mathbb R$ es un intervalo y

$$
f\colon I\to\mathbb R
$$

es estrictamente monótona.

El teorema anterior nos da inmediatamente inyectividad. Pero para aplicar el criterio de §3.5 necesitamos también sobreyectividad.

Aquí aparece una maniobra que ya usamos con $x^2$: en lugar de mantener un codominio posiblemente demasiado grande, consideramos la misma regla con codominio igual a su imagen:

$$
f\colon I\to f(I).
$$

Esta función es sobreyectiva **por definición de $f(I)$**. Y es inyectiva por el teorema de monotonía estricta. Por tanto, es biyectiva y posee función inversa.

La monotonía nos permite decir todavía más: la inversa conserva el mismo tipo de orden.

::: {#cor-t1-0006}
**Inversa sobre la imagen y monotonía de la inversa.** Sea $I\subseteq\mathbb R$ un intervalo y sea

$$
f\colon I\to\mathbb R
$$

estrictamente monótona. Entonces la función

$$
f\colon I\to f(I)
$$

es biyectiva y, por tanto, admite una única inversa

$$
f^{-1}\colon f(I)\to I.
$$

Además:

1. si $f$ es estrictamente creciente, entonces $f^{-1}$ es estrictamente creciente;
2. si $f$ es estrictamente decreciente, entonces $f^{-1}$ es estrictamente decreciente.
:::

**Por qué existe la inversa.** La sobreyectividad de

$$
f\colon I\to f(I)
$$

es automática, porque cada elemento de $f(I)$ es, precisamente, un valor $f(x)$ con $x\in I$. La inyectividad proviene de @thm-t1-0008. Por @thm-t1-0007, la función es biyectiva y admite una única inversa.

Queda demostrar el comportamiento del orden.

**Caso 1: $f$ estrictamente creciente.** Sean

$$
y_1,y_2\in f(I)
\qquad\text{con}\qquad
y_1<y_2.
$$

Definamos

$$
x_1=f^{-1}(y_1),
\qquad
x_2=f^{-1}(y_2).
$$

Entonces

$$
f(x_1)=y_1,
\qquad
f(x_2)=y_2.
$$

Queremos demostrar

$$
x_1<x_2.
$$

Como $y_1<y_2$, tenemos $y_1\ne y_2$ y por tanto $x_1\ne x_2$. Si ocurriera $x_2<x_1$, la monotonía estrictamente creciente de $f$ produciría

$$
f(x_2)<f(x_1),
$$

es decir,

$$
y_2<y_1,
$$

contradicción.

La única posibilidad restante es

$$
x_1<x_2.
$$

Así,

$$
y_1<y_2
\Longrightarrow
f^{-1}(y_1)<f^{-1}(y_2),
$$

y $f^{-1}$ es estrictamente creciente.

**Caso 2: $f$ estrictamente decreciente.** Tomemos de nuevo $y_1<y_2$ y pongamos

$$
x_1=f^{-1}(y_1),
\qquad
x_2=f^{-1}(y_2).
$$

Si ocurriera $x_1<x_2$, como $f$ es estrictamente decreciente tendríamos

$$
f(x_1)>f(x_2),
$$

es decir,

$$
y_1>y_2,
$$

contradicción.

Como $x_1\ne x_2$, necesariamente

$$
x_1>x_2.
$$

Por tanto,

$$
y_1<y_2
\Longrightarrow
f^{-1}(y_1)>f^{-1}(y_2),
$$

y la inversa es estrictamente decreciente. $\square$

::: {.callout-note title="Dos inversiones distintas"}
En el caso decreciente aparecen dos ideas de «inversión» que no deben confundirse.

- $f$ **invierte el orden**:
  $$
  x_1<x_2\Longrightarrow f(x_1)>f(x_2).
  $$
- $f^{-1}$ **invierte la asignación** de entradas y salidas.

La inversa funcional de una función estrictamente decreciente sigue siendo estrictamente decreciente: al recorrer la relación en sentido contrario, el orden vuelve a invertirse.
:::

### Lo que todavía no podemos concluir sobre $f(I)$

El dominio $I$ es un intervalo, pero de lo demostrado hasta aquí **no se sigue** que la imagen $f(I)$ sea también un intervalo.

Consideremos

$$
f\colon\mathbb R\to\mathbb R,
$$

$$
f(x)=
\begin{cases}
x,&x<0,\\
x+1,&x\ge0.
\end{cases}
$$

Esta función es estrictamente creciente. En efecto:

- si $x_1<x_2<0$, entonces $f(x_1)=x_1<x_2=f(x_2)$;
- si $0\le x_1<x_2$, entonces $f(x_1)=x_1+1<x_2+1=f(x_2)$;
- si $x_1<0\le x_2$, entonces
  $$
  f(x_1)=x_1<0<1\le x_2+1=f(x_2).
  $$

Sin embargo,

$$
f(\mathbb R)=(-\infty,0)\cup[1,\infty),
$$

que no es un intervalo.

Esto marca con precisión la frontera actual del capítulo. La monotonía estricta basta para obtener **inyectividad** y, al ajustar el codominio a la imagen, una **inversa**. Para garantizar que ciertos valores intermedios no se omitan necesitaremos una propiedad adicional que todavía no hemos introducido.

### El modelo fundamental: cuadrado y raíz

Volvamos ahora a una función que nos acompaña desde el comienzo del capítulo.

::: {#exm-t1-0029}
**El cuadrado sobre $[0,\infty)$ y su inversa.** Consideremos

$$
q\colon[0,\infty)\to[0,\infty),
\qquad
q(x)=x^2.
$$

En §3.3 demostramos que $q$ es biyectiva y en §3.5 identificamos su inversa como

$$
q^{-1}(y)=\sqrt y.
$$

Ahora podemos comprender esa invertibilidad desde el orden.

Sean

$$
0\le x_1<x_2.
$$

Entonces

$$
x_2^2-x_1^2
=(x_2-x_1)(x_2+x_1).
$$

El primer factor es positivo:

$$
x_2-x_1>0.
$$

Además, como $x_2>x_1\ge0$, tenemos $x_2>0$, y por tanto

$$
x_2+x_1>0.
$$

Así,

$$
x_2^2-x_1^2>0,
$$

de donde

$$
x_1^2<x_2^2.
$$

Por consiguiente, $q$ es estrictamente creciente en $[0,\infty)$.

El corolario anterior implica entonces que su inversa

$$
\sqrt{\phantom{x}}\colon[0,\infty)\to[0,\infty)
$$

es también estrictamente creciente. En particular,

$$
0\le y_1<y_2
\Longrightarrow
\sqrt{y_1}<\sqrt{y_2}.
$$

Esta propiedad no necesita una nueva demostración mediante cuadrados: es una consecuencia estructural de que $x^2$ es estrictamente creciente en el dominio donde lo hemos hecho invertible.
:::

El ejemplo muestra por qué la restricción del dominio a $[0,\infty)$ era tan natural. En todo $\mathbb R$, la función $x\mapsto x^2$ no es estrictamente monótona: por ejemplo,

$$
-2<-1,
$$

pero

$$
(-2)^2=4>1=(-1)^2,
$$

mientras que

$$
0<1
\Longrightarrow
0^2<1^2.
$$

El comportamiento cambia al atravesar $0$. Al restringirnos a $[0,\infty)$ obtenemos una región del dominio en la que el orden se conserva estrictamente y, con ello, la inyectividad necesaria para invertir la función.

### La gráfica de la inversa y la diagonal $y=x$

En §3.7 definimos

$$
\Gamma_f
=
\{(x,f(x)):x\in I\}.
$$

Si $f\colon I\to f(I)$ es biyectiva, entonces

$$
y=f(x)
\Longleftrightarrow
x=f^{-1}(y).
$$

Por tanto,

$$
(x,y)\in\Gamma_f
\Longleftrightarrow
(y,x)\in\Gamma_{f^{-1}}.
$$

La gráfica de la inversa se obtiene, pues, **intercambiando las dos coordenadas** de cada punto:

$$
\boxed{(x,y)\longmapsto(y,x).}
$$

Geométricamente, ese intercambio es la reflexión respecto de la diagonal

$$
y=x.
$$

No necesitamos apelar al dibujo para justificarlo. La simetría gráfica es la traducción geométrica de las equivalencias

$$
y=f(x)
\Longleftrightarrow
x=f^{-1}(y).
$$

En el ejemplo anterior, los puntos

$$
(4,16),
\qquad
(9,81)
$$

de la gráfica de $q(x)=x^2$ sobre $[0,\infty)$ corresponden a los puntos

$$
(16,4),
\qquad
(81,9)
$$

de la gráfica de $q^{-1}(x)=\sqrt x$.

### Qué aporta realmente la monotonía

Podemos reunir la cadena lógica construida en esta sección:

$$
\boxed{
\text{monotonía estricta}
\Longrightarrow
\text{inyectividad}
\Longrightarrow
\text{biyección sobre la imagen}
\Longrightarrow
\text{existencia de inversa}.}
$$

Y además,

$$
\boxed{
\begin{array}{c}
\text{estrictamente creciente}
\Longrightarrow
\text{inversa estrictamente creciente},\\[4pt]
\text{estrictamente decreciente}
\Longrightarrow
\text{inversa estrictamente decreciente}.
\end{array}}
$$

La importancia de esta cadena es metodológica. Para construir una inversa no siempre conviene comenzar intentando despejar una fórmula. A menudo es más útil preguntar primero:

1. ¿en qué dominio la función tiene un comportamiento ordenado simple?;
2. ¿es estrictamente monótona allí?;
3. ¿qué imagen produce ese dominio?;
4. ¿podemos tomar esa imagen como codominio?

Si las respuestas encajan, la existencia de la inversa queda resuelta antes de calcular su fórmula.

En §3.10 reuniremos todas las estructuras del capítulo en un laboratorio integrado: dominio y codominio, imágenes y preimágenes, composición, inyectividad, inversas, gráficas y monotonía deberán aparecer ya no como temas aislados, sino como herramientas entre las que habrá que elegir según el problema.
