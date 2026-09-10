## Valor absoluto, distancia y desigualdades {#sec-t1-c02-03}

### Del orden a la distancia

En §2.2 aprendimos a comparar números: sabemos qué significa que uno esté a la izquierda de otro y qué operaciones preservan o invierten una desigualdad. Pero el cálculo necesitará algo más fino que decidir cuál de dos números es mayor.

Necesitaremos responder preguntas como estas:

- ¿qué tan lejos está $x$ de $0$?;
- ¿qué tan lejos está $x$ de un número fijo $a$?;
- ¿qué significa que $x$ esté «muy cerca» de $a$?;
- ¿cómo podemos convertir una afirmación geométrica de cercanía en desigualdades manipulables algebraicamente?

La herramienta elemental que responde todas estas preguntas es el **valor absoluto**.

::: {#def-t1-0014}
**Valor absoluto.** Para $x\in\mathbb R$, definimos

$$
|x|=
\begin{cases}
x, & x\ge0,\\
-x, & x<0.
\end{cases}
$$

El número $|x|$ representa la distancia de $x$ al origen sobre la recta real.
:::

La definición por casos puede parecer puramente algebraica, pero su significado es geométrico. Por ejemplo,

$$
|5|=5,
\qquad
|-5|=5,
$$

porque los puntos $5$ y $-5$ se encuentran a la misma distancia del origen.

Esta observación explica por qué el valor absoluto nunca es negativo: una distancia no puede serlo. Pero, como siempre, la intuición geométrica debe poder traducirse a las reglas del cuerpo ordenado.

### Propiedades básicas que no conviene memorizar aisladas

::: {#prp-t1-0008}
Para cualesquiera $x,y\in\mathbb R$ se cumplen las siguientes propiedades:

1. $|x|\ge0$, y $|x|=0$ si y solo si $x=0$;
2. $|-x|=|x|$;
3. $-|x|\le x\le|x|$;
4. $|xy|=|x|\,|y|$;
5. si $a\ge0$, entonces
   $$
   |x|\le a
   \iff
   -a\le x\le a;
   $$
6. si $a>0$, entonces
   $$
   |x|<a
   \iff
   -a<x<a.
   $$
:::

**Demostración.** Las tres primeras afirmaciones se leen directamente de la definición por casos.

Si $x\ge0$, entonces $|x|=x$; si $x<0$, entonces $|x|=-x>0$. Esto demuestra $|x|\ge0$, y la igualdad solo puede ocurrir cuando $x=0$. La igualdad $|-x|=|x|$ expresa algebraicamente que $x$ y $-x$ están a la misma distancia de $0$. Finalmente, tanto si $x\ge0$ como si $x<0$, se verifica

$$
-|x|\le x\le|x|.
$$

Para la propiedad del producto controlamos los signos. Si $x,y\ge0$, entonces

$$
|xy|=xy=|x|\,|y|.
$$

Si $x,y<0$, entonces $xy>0$ y

$$
|xy|=xy=(-x)(-y)=|x|\,|y|.
$$

Si uno es no negativo y el otro negativo, entonces $xy\le0$ y aparece exactamente una negación. Por ejemplo, si $x\ge0$ e $y<0$,

$$
|xy|=-xy=x(-y)=|x|\,|y|.
$$

El caso restante es simétrico. Por tanto, en todos los casos,

$$
|xy|=|x|\,|y|.
$$

Consideremos ahora $a\ge0$. Si $|x|\le a$, entonces, usando

$$
-|x|\le x\le|x|,
$$

obtenemos inmediatamente

$$
-a\le x\le a.
$$

Recíprocamente, supongamos

$$
-a\le x\le a.
$$

Si $x\ge0$, entonces $|x|=x\le a$. Si $x<0$, de $-a\le x$ se sigue, al multiplicar por $-1$, que $-x\le a$; por tanto $|x|=-x\le a$. Esto demuestra la equivalencia no estricta. El argumento para desigualdades estrictas es idéntico. $\blacksquare$

::: {.callout-note title="Lectura de la fórmula"}
La equivalencia

$$
|x|<a
\iff
-a<x<a
$$

no es un truco de resolución de inequaciones. Dice literalmente:

> estar a distancia menor que $a$ del origen equivale a encontrarse entre $-a$ y $a$.

La desigualdad algebraica y la descripción geométrica son dos lenguajes para la misma región de la recta.
:::

### Distancia entre dos puntos

Si $|x|$ mide la distancia de $x$ al origen, para medir la distancia entre dos puntos $x$ e $y$ basta trasladar uno de ellos al origen. La diferencia

$$
x-y
$$

indica cuánto debemos desplazarnos desde $y$ para llegar a $x$, y su valor absoluto elimina la orientación del desplazamiento.

Por eso definiremos, en la recta real,

$$
d(x,y)=|x-y|.
$$

No necesitamos todavía desarrollar la teoría general de espacios métricos. Nos basta observar las propiedades que esta distancia hereda del valor absoluto:

$$
d(x,y)\ge0,
$$

$$
d(x,y)=0\iff x=y,
$$

$$
d(x,y)=d(y,x).
$$

La última igualdad sigue de

$$
|x-y|=|-(y-x)|=|y-x|.
$$

Falta una propiedad más profunda. Si queremos viajar de $x$ a $z$, pasar primero por un punto intermedio $y$ no debería producir un trayecto más corto que ir directamente. Esa idea es la desigualdad triangular.

### La desigualdad triangular

::: {#thm-t1-0001}
**Desigualdad triangular.** Para cualesquiera $x,y\in\mathbb R$,

$$
|x+y|\le |x|+|y|.
$$
:::

::: {.callout-note title="Idea de la prueba"}
Ya sabemos que cada número queda atrapado entre el negativo y el positivo de su valor absoluto:

$$
-|x|\le x\le|x|,
\qquad
-|y|\le y\le|y|.
$$

Si sumamos ambas dobles desigualdades, obtendremos una cota inferior y otra superior para $x+y$. Después podremos volver a empaquetar esas dos cotas mediante la caracterización de $|\cdot|$ que acabamos de demostrar.
:::

**Demostración.** Sumando

$$
-|x|\le x\le|x|
$$

y

$$
-|y|\le y\le|y|,
$$

obtenemos

$$
-(|x|+|y|)\le x+y\le |x|+|y|.
$$

Como $|x|+|y|\ge0$, la Proposición `#prp-t1-0008` permite concluir

$$
|x+y|\le|x|+|y|.
$$

$\blacksquare$

::: {.callout-note title="Después de la prueba"}
La demostración tiene una arquitectura reutilizable:

1. convertir una expresión con valor absoluto en dos desigualdades ordinarias;
2. operar con ellas usando las leyes del orden;
3. reconstruir al final una desigualdad con valor absoluto.

Este movimiento entre **distancia** y **orden** reaparecerá constantemente en cálculo.
:::

Si sustituimos

$$
x=a-c,
\qquad
y=c-b,
$$

entonces $x+y=a-b$ y la desigualdad triangular adopta la forma

$$
\boxed{
|a-b|\le|a-c|+|c-b|.
}
$$

Ahora su nombre se vuelve completamente transparente: la distancia directa de $a$ a $b$ no supera la distancia obtenida pasando por $c$.

### La desigualdad triangular inversa

La desigualdad triangular también permite comparar las distancias de dos puntos al origen.

::: {#cor-t1-0001}
**Desigualdad triangular inversa.** Para cualesquiera $x,y\in\mathbb R$,

$$
\bigl||x|-|y|\bigr|\le|x-y|.
$$
:::

**Demostración.** Escribamos

$$
x=(x-y)+y.
$$

Por la desigualdad triangular,

$$
|x|
\le
|x-y|+|y|.
$$

Restando $|y|$ obtenemos

$$
|x|-|y|\le|x-y|.
$$

Si intercambiamos $x$ e $y$,

$$
|y|-|x|\le|y-x|=|x-y|.
$$

Las dos desigualdades juntas dicen

$$
-|x-y|
\le
|x|-|y|
\le
|x-y|.
$$

Por la caracterización del valor absoluto,

$$
\bigl||x|-|y|\bigr|\le|x-y|.
$$

$\blacksquare$

::: {.callout-note title="Por qué importa"}
La desigualdad triangular ordinaria controla la distancia de una **suma**. La inversa controla cuánto pueden diferir dos **magnitudes**:

$$
\bigl||x|-|y|\bigr|
\le
|x-y|.
$$

Dicho en lenguaje geométrico: la diferencia entre las distancias de $x$ e $y$ al origen nunca puede superar la distancia entre $x$ e $y$.
:::

### Una desigualdad centrada en un punto

En cálculo rara vez nos interesará solamente la distancia al origen. Mucho más frecuente será medir la distancia respecto de un número fijo $a$.

Si $r>0$, la condición

$$
|x-a|<r
$$

significa que la distancia de $x$ a $a$ es menor que $r$.

La Proposición `#prp-t1-0008` permite traducirla inmediatamente:

$$
\begin{aligned}
|x-a|<r
&\iff -r<x-a<r\\
&\iff a-r<x<a+r.
\end{aligned}
$$

Por tanto,

$$
\boxed{
|x-a|<r
\iff
x\in(a-r,a+r).
}
$$

La misma idea funciona con extremos incluidos.

::: {#prp-t1-0009}
Si $a\in\mathbb R$ y $r>0$, entonces

$$
|x-a|<r
\iff
a-r<x<a+r
\iff
x\in(a-r,a+r),
$$

mientras que

$$
|x-a|\le r
\iff
a-r\le x\le a+r
\iff
x\in[a-r,a+r].
$$

Además,

$$
|x-a|>r
\iff
x<a-r\ \text{o}\ x>a+r,
$$

y

$$
|x-a|\ge r
\iff
x\le a-r\ \text{o}\ x\ge a+r.
$$
:::

::: {.callout-warning title="Error frecuente: olvidar el centro"}
De

$$
|x-a|<r
$$

no se sigue $-r<x<r$ salvo que $a=0$.

El intervalo está centrado en $a$, no en el origen:

$$
(a-r,a+r).
$$
:::

### Dos maneras de leer una misma inequación

::: {#exm-t1-0013}
Resolvamos

$$
|2x-3|<5.
$$

Podemos hacerlo algebraicamente o geométricamente.
:::

**Lectura algebraica.** Por la equivalencia para el valor absoluto,

$$
-5<2x-3<5.
$$

Sumando $3$,

$$
-2<2x<8,
$$

y dividiendo por el número positivo $2$,

$$
-1<x<4.
$$

Por tanto,

$$
x\in(-1,4).
$$

**Lectura geométrica.** Factorizamos primero:

$$
|2x-3|
=
2\left|x-\frac32\right|.
$$

La inequación equivale a

$$
\left|x-\frac32\right|<\frac52.
$$

Así, $x$ debe encontrarse a distancia menor que $5/2$ del centro $3/2$. El intervalo correspondiente es

$$
\left(\frac32-\frac52,\frac32+\frac52\right)
=(-1,4).
$$

Las dos soluciones son la misma demostración expresada en dos lenguajes diferentes.

### Estimar no significa calcular exactamente

El valor absoluto será también nuestra herramienta básica para **estimar** cantidades.

Supongamos que conocemos una aproximación de $x$ a un punto $a$ en el sentido de que

$$
|x-a|<r.
$$

Quizá no sepamos el valor exacto de $x$, pero podemos controlar su tamaño. Como

$$
x=(x-a)+a,
$$

la desigualdad triangular da

$$
|x|
\le
|x-a|+|a|
<
r+|a|.
$$

Así obtenemos

$$
\boxed{
|x-a|<r
\quad\Longrightarrow\quad
|x|<|a|+r.
}
$$

Este pequeño patrón es una de las técnicas fundamentales del análisis:

$$
\boxed{
\text{cantidad desconocida}
=
\text{error respecto de una referencia}
+
\text{referencia conocida}.
}
$$

Después aplicamos la desigualdad triangular para transformar esa descomposición en una cota.

No estamos hablando todavía de límites. Pero cuando más adelante aparezcan expresiones como

$$
|x-a|<\delta
$$

o

$$
|u_n-L|<\varepsilon,
$$

su significado geométrico ya no deberá aprenderse de nuevo: serán afirmaciones acerca de **distancias**.

### Antes de seguir

::: {.callout-tip title="Antes de seguir"}
**1.** Describe mediante un intervalo el conjunto de todos los $x$ que satisfacen

$$
|x-4|<3.
$$

**Respuesta.** La distancia de $x$ a $4$ es menor que $3$, de modo que

$$
1<x<7.
$$

Por tanto,

$$
x\in(1,7).
$$
:::

::: {.callout-tip title="Antes de seguir"}
**2.** ¿Qué región describe

$$
|x+2|\ge5?
$$

**Respuesta.** Como $|x+2|=|x-(-2)|$, el centro es $-2$. Estar a distancia al menos $5$ significa encontrarse fuera del intervalo abierto $(-7,3)$, incluidos sus extremos:

$$
x\le-7
\quad\text{o}\quad
x\ge3.
$$
:::

::: {.callout-tip title="Antes de seguir"}
**3.** Si $|x-10|<\tfrac12$, da una cota sencilla para $|x|$.

**Respuesta.** Por la desigualdad triangular,

$$
|x|
\le
|x-10|+10
<
\frac12+10
=
\frac{21}{2}.
$$
:::

### Qué hemos ganado

El valor absoluto comenzó como una definición por casos y terminó organizando tres lenguajes que utilizaremos constantemente:

$$
\boxed{
\text{orden}
\longleftrightarrow
\text{valor absoluto}
\longleftrightarrow
\text{distancia}.
}
$$

Ahora podemos traducir

$$
|x-a|<r
$$

en cualquiera de estas formas:

- una desigualdad de valor absoluto;
- una afirmación de distancia;
- una doble desigualdad;
- pertenencia a un intervalo abierto.

También disponemos de las dos estimaciones fundamentales

$$
|x+y|\le|x|+|y|
$$

y

$$
\bigl||x|-|y|\bigr|\le|x-y|.
$$

Estas herramientas permiten hablar con precisión de tamaño y cercanía. Pero todavía no permiten hablar de «puntos frontera» de conjuntos que quizá no contengan sus extremos.

Ese será el problema de §2.4. Allí distinguiremos por primera vez entre **máximo** y **supremo**, y podremos comenzar a formular rigurosamente la clase de borde que faltaba en el sistema racional de §2.1.
