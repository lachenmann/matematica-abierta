---
title: "Continuidad uniforme y teorema de Heine–Cantor"
description: "Cómo reforzar la continuidad puntual a un control global independiente del punto, y por qué toda función continua sobre un compacto es uniformemente continua."
content-id: MA-CON-0019
content-type: concept
status: published
date-created: 2026-09-07
date-modified: 2026-09-07
areas:
  - analisis
  - calculo
  - topologia
level: introductorio
topics:
  - continuidad
  - continuidad-uniforme
  - epsilon-delta
  - cuantificadores
  - compacidad
  - conjuntos-compactos
  - teorema-de-heine-cantor
  - control-global
  - funciones-lipschitz
  - composicion-de-funciones
  - intervalos-cerrados
prerequisites:
  - MA-CON-0008
  - MA-CON-0014
  - MA-CON-0018
related:
  - MA-CON-0016
  - MA-CON-0017
provenance:
  type: classical
  sources: []
license: GFDL-1.3-or-later
---

En `MA-CON-0014` definimos la continuidad punto por punto. Para cada $a$ del dominio y cada tolerancia $\varepsilon>0$, buscamos un $\delta>0$ que controle la función cerca de ese punto.

Pero hay una pregunta más fuerte:

> ¿puede elegirse **un mismo $\delta$** que funcione simultáneamente en todo el dominio?

La respuesta conduce a la **continuidad uniforme**.

En `MA-CON-0018` demostramos que la compacidad permite reducir controles locales infinitos a una familia finita. Esa propiedad será exactamente la herramienta que transforme continuidad puntual en continuidad uniforme.

::: {.ma-block .ma-intuicion}
**Intuición**

Continuidad ordinaria:

> en cada punto puedo encontrar una escala adecuada de control.

Continuidad uniforme:

> para una tolerancia de salida dada, existe una **escala única de entrada** que funciona en todos los puntos del dominio a la vez.

La diferencia parece pequeña, pero cambia el orden de los cuantificadores y convierte un control local en uno global.
:::

## Recordatorio: continuidad en un punto

Sea

$$
f:D\to\mathbb R.
$$

La función es continua en un punto $a\in D$ si

$$
\forall\varepsilon>0\;\exists\delta>0\;\forall x\in D:
|x-a|<\delta
\Longrightarrow
|f(x)-f(a)|<\varepsilon.
$$

Si afirmamos que $f$ es continua **en todo $D$**, el esquema completo es

$$
\boxed{
\forall a\in D\;\forall\varepsilon>0\;\exists\delta>0\;\forall x\in D:
|x-a|<\delta
\Longrightarrow
|f(x)-f(a)|<\varepsilon.
}
$$

Aquí el número $\delta$ puede depender de dos cosas:

- de $\varepsilon$;
- del punto $a$.

Podríamos escribir simbólicamente

$$
\delta=\delta(a,\varepsilon).
$$

Éste es el aspecto que cambia en la continuidad uniforme.

# Continuidad uniforme

::: {.ma-block .ma-definicion}
**Continuidad uniforme**

Sea

$$
f:D\to\mathbb R.
$$

Decimos que $f$ es **uniformemente continua** en $D$ si para todo $\varepsilon>0$ existe un $\delta>0$ tal que, para todos $x,y\in D$,

$$
|x-y|<\delta
\quad\Longrightarrow\quad
|f(x)-f(y)|<\varepsilon.
$$
:::

En símbolos,

$$
\boxed{
\forall\varepsilon>0\;\exists\delta>0\;\forall x,y\in D:
|x-y|<\delta
\Longrightarrow
|f(x)-f(y)|<\varepsilon.
}
$$

La diferencia esencial es que $\delta$ se elige **antes** de elegir $x$ e $y$.

Por tanto, debe funcionar para todo par de puntos del dominio.

## Comparación de cuantificadores

Continuidad en todo $D$:

$$
\forall a\in D\;\forall\varepsilon>0\;\exists\delta>0\;\forall x\in D.
$$

Continuidad uniforme:

$$
\forall\varepsilon>0\;\exists\delta>0\;\forall x,y\in D.
$$

La continuidad ordinaria permite escoger

$$
\delta=\delta(a,\varepsilon).
$$

La continuidad uniforme exige poder escoger

$$
\delta=\delta(\varepsilon)
$$

sin dependencia del punto.

::: {.ma-block .ma-error}
**No es una diferencia de notación**

Cambiar el orden

$$
\forall a\;\exists\delta
$$

por

$$
\exists\delta\;\forall a
$$

fortalece la afirmación.

En el primer caso puede existir un $\delta$ distinto para cada punto.

En el segundo debe existir un único $\delta$ que sirva para todos.
:::

## Lectura geométrica

Fijemos una tolerancia vertical $\varepsilon>0$.

Si $f$ es uniformemente continua, existe una separación horizontal $\delta>0$ con la propiedad siguiente:

> cualquier par $x,y\in D$ cuya distancia horizontal sea menor que $\delta$ produce valores $f(x)$ y $f(y)$ cuya distancia vertical es menor que $\varepsilon$.

La ubicación de $x$ e $y$ dentro del dominio no importa.

::: {.ma-block .ma-intuicion}
**Una misma resolución en todo el dominio**

La continuidad uniforme afirma que, una vez fijada la precisión deseada en la salida, podemos escoger una resolución de entrada válida globalmente.

No necesitamos aumentar indefinidamente la precisión al desplazarnos por el dominio.
:::

# Toda función uniformemente continua es continua

::: {.ma-block .ma-definicion}
**Proposición**

Si

$$
f:D\to\mathbb R
$$

es uniformemente continua en $D$, entonces es continua en cada punto de $D$.
:::

## Demostración

Sea $a\in D$ y sea $\varepsilon>0$.

Por continuidad uniforme, existe $\delta>0$ tal que para todos $x,y\in D$,

$$
|x-y|<\delta
\Longrightarrow
|f(x)-f(y)|<\varepsilon.
$$

Tomemos ahora

$$
y=a.
$$

Entonces, para todo $x\in D$,

$$
|x-a|<\delta
\Longrightarrow
|f(x)-f(a)|<\varepsilon.
$$

Ésta es exactamente la continuidad de $f$ en $a$.

Como $a$ era arbitrario,

$$
\boxed{f\text{ es continua en }D.}
$$

La recíproca, sin hipótesis adicionales, es falsa.

# Continuidad no implica continuidad uniforme

Consideremos

$$
f(x)=\frac1x
$$

en

$$
D=(0,1].
$$

La función es continua en cada punto de su dominio.

Demostraremos que no es uniformemente continua.

## Una elección de puntos cada vez más cercanos

Para $n\in\mathbb N$, tomemos

$$
x_n=\frac1n,
\qquad
y_n=\frac1{n+1}.
$$

La distancia entre las entradas es

$$
|x_n-y_n|
=
\frac1n-\frac1{n+1}
=
\frac1{n(n+1)}.
$$

Esta cantidad puede hacerse tan pequeña como queramos.

Sin embargo,

$$
f(x_n)=n
$$

y

$$
f(y_n)=n+1.
$$

Por tanto,

$$
|f(x_n)-f(y_n)|=1.
$$

Fijemos

$$
\varepsilon=\frac12.
$$

Si $f$ fuera uniformemente continua, existiría $\delta>0$ tal que

$$
|x-y|<\delta
\Longrightarrow
|f(x)-f(y)|<\frac12
$$

para todos $x,y\in(0,1]$.

Pero, por la propiedad arquimediana de `MA-CON-0016`, podemos escoger $n$ suficientemente grande para que

$$
\frac1{n(n+1)}<\delta.
$$

Entonces

$$
|x_n-y_n|<\delta,
$$

mientras que

$$
|f(x_n)-f(y_n)|=1>\frac12.
$$

Contradicción.

Así,

$$
\boxed{
f(x)=\frac1x
\text{ no es uniformemente continua en }(0,1].
}
$$

::: {.ma-block .ma-intuicion}
**Qué falla cerca de $0$**

A medida que nos acercamos a $0$, para mantener una variación fija en la salida necesitamos escoger intervalos horizontales cada vez más pequeños.

No existe una escala horizontal única que funcione simultáneamente en todo $(0,1]$.
:::

# Un segundo ejemplo: $x^2$ en toda la recta

La función

$$
f(x)=x^2
$$

es continua en $\mathbb R$.

Sin embargo, no es uniformemente continua en todo $\mathbb R$.

## Demostración

Fijemos

$$
\varepsilon=1.
$$

Supongamos que existiera un $\delta>0$ válido para toda la recta.

Tomemos un número $x$ tan grande que

$$
x>\frac1\delta
$$

y definamos

$$
y=x+\frac\delta2.
$$

Entonces

$$
|x-y|=\frac\delta2<\delta.
$$

Pero

$$
|f(y)-f(x)|
=
\left(x+\frac\delta2\right)^2-x^2
$$

$$
=x\delta+\frac{\delta^2}{4}.
$$

Como

$$
x>\frac1\delta,
$$

tenemos

$$
x\delta>1.
$$

Así,

$$
|f(y)-f(x)|>1=\varepsilon.
$$

Por tanto no existe un $\delta$ global y

$$
\boxed{x^2\text{ no es uniformemente continua en }\mathbb R.}
$$

## El dominio importa

La misma función sí es uniformemente continua en cualquier intervalo acotado

$$
[-M,M].
$$

En efecto, si $x,y\in[-M,M]$,

$$
|x^2-y^2|
=|x-y|\,|x+y|.
$$

Como

$$
|x+y|\le|x|+|y|\le2M,
$$

obtenemos

$$
|x^2-y^2|\le2M|x-y|.
$$

Dado $\varepsilon>0$, si $M>0$ basta escoger

$$
\delta=\frac{\varepsilon}{2M}.
$$

Entonces

$$
|x-y|<\delta
$$

implica

$$
|x^2-y^2|<\varepsilon.
$$

La misma fórmula que fracasa globalmente en $\mathbb R$ funciona perfectamente cuando el dominio impone un control uniforme sobre $|x+y|$.

# Una condición suficiente: funciones Lipschitz

El argumento anterior exhibe una estructura especialmente útil.

::: {.ma-block .ma-definicion}
**Condición de Lipschitz**

Una función

$$
f:D\to\mathbb R
$$

es **Lipschitz** en $D$ si existe una constante $L\ge0$ tal que

$$
|f(x)-f(y)|\le L|x-y|
$$

para todos $x,y\in D$.
:::

La constante $L$ controla globalmente cuánto puede amplificar la función las distancias.

## Toda función Lipschitz es uniformemente continua

Supongamos $L>0$.

Dado $\varepsilon>0$, tomemos

$$
\delta=\frac{\varepsilon}{L}.
$$

Si

$$
|x-y|<\delta,
$$

entonces

$$
|f(x)-f(y)|
\le L|x-y|
<L\delta
=\varepsilon.
$$

Por tanto,

$$
\boxed{
\text{Lipschitz}\Longrightarrow\text{uniformemente continua}.
}
$$

Si $L=0$, la función es constante y la conclusión es inmediata.

::: {.ma-block .ma-metodo}
**Estrategia directa**

Para demostrar continuidad uniforme sin usar compacidad, busca una estimación del tipo

$$
|f(x)-f(y)|\le\Phi(|x-y|),
$$

donde

$$
\Phi(t)\to0
$$

cuando $t\to0^+$.

Una estimación Lipschitz

$$
\Phi(t)=Lt
$$

es el caso más simple.
:::

# La compacidad fuerza uniformidad

Los ejemplos anteriores muestran que una función continua puede requerir escalas $\delta$ cada vez más pequeñas al desplazarnos por el dominio.

La compacidad impide que ese deterioro local escape sin control.

Éste es el contenido del teorema de Heine–Cantor.

# Teorema de Heine–Cantor

::: {.ma-block .ma-definicion}
**Teorema de Heine–Cantor**

Sea $K\subseteq\mathbb R$ compacto y sea

$$
f:K\to\mathbb R
$$

continua.

Entonces

$$
\boxed{f\text{ es uniformemente continua en }K.}
$$
:::

La hipótesis de compacidad es exactamente la estructura desarrollada en `MA-CON-0018`.

No tomaremos el resultado como una caja negra.

# Demostración mediante un subrecubrimiento finito

Sea

$$
\varepsilon>0.
$$

Queremos encontrar un único $\delta>0$ que funcione para **todos** los pares $x,y\in K$.

## Paso 1: usar continuidad en cada punto

Fijemos un punto

$$
a\in K.
$$

Como $f$ es continua en $a$, existe un número

$$
r_a>0
$$

tal que, para todo $t\in K$,

$$
|t-a|<r_a
\quad\Longrightarrow\quad
|f(t)-f(a)|<\frac\varepsilon2.
$$

Cada punto $a$ puede producir un radio diferente $r_a$.

Hasta aquí sólo tenemos continuidad puntual.

## Paso 2: construir un recubrimiento abierto

Consideremos, para cada $a\in K$, el intervalo abierto

$$
U_a=\left(a-\frac{r_a}{2},a+\frac{r_a}{2}\right).
$$

Como

$$
a\in U_a,
$$

la familia

$$
\{U_a:a\in K\}
$$

es un recubrimiento abierto de $K$.

## Paso 3: aplicar compacidad

Como $K$ es compacto, existe un subrecubrimiento finito

$$
U_{a_1},\dots,U_{a_N}
$$

tal que

$$
K\subseteq U_{a_1}\cup\cdots\cup U_{a_N}.
$$

Ahora sólo quedan finitos radios:

$$
r_{a_1},\dots,r_{a_N}.
$$

Por tanto podemos tomar un mínimo positivo.

Definamos

$$
\delta=rac12\min\{r_{a_1},\dots,r_{a_N}\}.
$$

Como se trata del mínimo de finitísimos números positivos,

$$
\delta>0.
$$

Éste será nuestro candidato global.

## Paso 4: comprobar que el mismo $\delta$ funciona en todo $K$

Sean

$$
x,y\in K
$$

tales que

$$
|x-y|<\delta.
$$

Como los $U_{a_j}$ cubren $K$, existe algún índice $j$ con

$$
x\in U_{a_j}.
$$

Por definición de $U_{a_j}$,

$$
|x-a_j|<\frac{r_{a_j}}2.
$$

Además,

$$
|x-y|<\delta\le\frac{r_{a_j}}2.
$$

Por la desigualdad triangular,

$$
|y-a_j|
\le|y-x|+|x-a_j|
<\frac{r_{a_j}}2+\frac{r_{a_j}}2
=r_{a_j}.
$$

Así, tanto $x$ como $y$ están suficientemente cerca de $a_j$ para aplicar el control de continuidad construido en el paso 1.

Tenemos

$$
|f(x)-f(a_j)|<\frac\varepsilon2
$$

y

$$
|f(y)-f(a_j)|<\frac\varepsilon2.
$$

Usando nuevamente la desigualdad triangular,

$$
|f(x)-f(y)|
\le
|f(x)-f(a_j)|+|f(a_j)-f(y)|
$$

$$
<\frac\varepsilon2+\frac\varepsilon2
=\varepsilon.
$$

Por tanto,

$$
|x-y|<\delta
\Longrightarrow
|f(x)-f(y)|<\varepsilon
$$

para **todos** $x,y\in K$.

Hemos demostrado

$$
\boxed{f\text{ es uniformemente continua en }K.}
$$

::: {.ma-block .ma-intuicion}
**Dónde intervino realmente la compacidad**

La continuidad produjo una colección potencialmente infinita de radios

$$
r_a.
$$

No tendría sentido tomar directamente

$$
\min_{a\in K}r_a,
$$

porque ese mínimo podría no existir o podría ser $0$.

La compacidad permitió conservar sólo finitos radios. Entonces sí existe un mínimo positivo y podemos fabricar un único $\delta$ global.
:::

## Versión para intervalos cerrados

Por Heine–Borel, todo intervalo cerrado y acotado

$$
[a,b]
$$

es compacto.

Por tanto obtenemos inmediatamente:

::: {.ma-block .ma-definicion}
**Corolario**

Si

$$
f:[a,b]\to\mathbb R
$$

es continua, entonces $f$ es uniformemente continua en $[a,b]$.
:::

Así, en un intervalo cerrado y acotado, la continuidad ordinaria automáticamente adquiere un control global.

# Compacidad: suficiente, pero no necesaria

Heine–Cantor afirma

$$
\text{continuidad}+\text{dominio compacto}
\Longrightarrow
\text{continuidad uniforme}.
$$

Pero no afirma la recíproca.

Una función puede ser uniformemente continua sobre un dominio no compacto.

## Ejemplo: la identidad en $\mathbb R$

Sea

$$
f(x)=x.
$$

Entonces

$$
|f(x)-f(y)|=|x-y|.
$$

Dado $\varepsilon>0$, basta escoger

$$
\delta=\varepsilon.
$$

Por tanto, la identidad es uniformemente continua en todo $\mathbb R$, aunque $\mathbb R$ no sea compacto.

::: {.ma-block .ma-observacion}
**Lectura lógica correcta**

La compacidad garantiza continuidad uniforme para toda función continua definida sobre ella.

No es una condición necesaria para que una función concreta sea uniformemente continua.
:::

# Uniformemente continua sin ser Lipschitz

La condición de Lipschitz también es suficiente, pero no necesaria.

Consideremos

$$
f(x)=\sqrt{x}
$$

en

$$
[0,\infty).
$$

Para $x,y\ge0$ se cumple

$$
|\sqrt{x}-\sqrt{y}|
\le\sqrt{|x-y|}.
$$

Veamos por qué.

Supongamos, sin pérdida de generalidad, que $x\ge y$. Entonces

$$
(\sqrt{x}-\sqrt{y})^2
=x+y-2\sqrt{xy}.
$$

Como

$$
\sqrt{xy}\ge y,
$$

obtenemos

$$
(\sqrt{x}-\sqrt{y})^2
\le x-y.
$$

Por tanto,

$$
|\sqrt{x}-\sqrt{y}|
\le\sqrt{x-y}
=
\sqrt{|x-y|}.
$$

Dado $\varepsilon>0$, basta tomar

$$
\delta=\varepsilon^2.
$$

Entonces

$$
|x-y|<\delta
$$

implica

$$
|\sqrt{x}-\sqrt{y}|
\le\sqrt{|x-y|}
<\sqrt\delta
=\varepsilon.
$$

Así,

$$
\boxed{\sqrt{x}\text{ es uniformemente continua en }[0,\infty).}
$$

El dominio no es compacto y no hemos usado una cota Lipschitz global.

# Composición de funciones uniformemente continuas

La continuidad uniforme se comporta bien bajo composición.

::: {.ma-block .ma-definicion}
**Proposición — composición**

Sean

$$
f:D\to E
$$

y

$$
g:E\to\mathbb R,
$$

donde $D,E\subseteq\mathbb R$.

Si $f$ es uniformemente continua en $D$ y $g$ es uniformemente continua en $E$, entonces

$$
\boxed{g\circ f\text{ es uniformemente continua en }D.}
$$
:::

## Demostración

Sea $\varepsilon>0$.

Como $g$ es uniformemente continua, existe $\eta>0$ tal que

$$
|u-v|<\eta
\Longrightarrow
|g(u)-g(v)|<\varepsilon
$$

para todos $u,v\in E$.

Como $f$ es uniformemente continua, para esa tolerancia $\eta$ existe $\delta>0$ tal que

$$
|x-y|<\delta
\Longrightarrow
|f(x)-f(y)|<\eta
$$

para todos $x,y\in D$.

Por tanto,

$$
|x-y|<\delta
$$

implica

$$
|g(f(x))-g(f(y))|<\varepsilon.
$$

Así,

$$
\boxed{g\circ f\text{ es uniformemente continua}.}
$$

La prueba es la misma arquitectura de tolerancias que ya apareció en la composición de funciones continuas, pero ahora ninguna escala depende de puntos particulares.

# Un criterio práctico para detectar fallo de uniformidad

Para demostrar que una función **no** es uniformemente continua, conviene negar correctamente la definición.

La definición es

$$
\forall\varepsilon>0\;\exists\delta>0\;\forall x,y\in D:
|x-y|<\delta
\Longrightarrow
|f(x)-f(y)|<\varepsilon.
$$

Su negación es

$$
\boxed{
\exists\varepsilon_0>0\;\forall\delta>0\;\exists x,y\in D:
|x-y|<\delta
\text{ y }
|f(x)-f(y)|\ge\varepsilon_0.
}
$$

Éste es exactamente el patrón que usamos para $1/x$ y $x^2$.

::: {.ma-block .ma-metodo}
**Método de refutación**

Para probar que $f$ no es uniformemente continua:

1. fija una tolerancia de salida $\varepsilon_0>0$;
2. toma un $\delta>0$ arbitrario;
3. construye puntos $x,y$ con
   $$
   |x-y|<\delta;
   $$
4. fuerza simultáneamente
   $$
   |f(x)-f(y)|\ge\varepsilon_0.
   $$

Si esto puede hacerse para todo $\delta>0$, no existe una escala global de control.
:::

# Por qué Heine–Cantor es más fuerte que la continuidad puntual

Para una función continua sobre un compacto $K$, cada punto $a$ produce inicialmente su propio radio

$$
\delta_a(\varepsilon).
$$

Heine–Cantor concluye que existe un único número

$$
\delta(\varepsilon)>0
$$

válido simultáneamente para todos los puntos del dominio.

Es decir, la compacidad permite pasar de

$$
\forall a\in K\;\exists\delta_a
$$

a

$$
\exists\delta\;\forall a\in K.
$$

No intercambiamos cuantificadores gratuitamente: la compacidad proporciona la razón matemática que lo hace posible.

# Relación con Weierstrass

`MA-CON-0018` produjo dos consecuencias de la compacidad para funciones continuas:

1. la imagen de un compacto es compacta;
2. una función continua sobre un compacto no vacío alcanza máximo y mínimo.

Heine–Cantor añade una tercera consecuencia:

3. la continuidad se vuelve uniforme.

Podemos resumir la situación así:

$$
\boxed{
\begin{array}{c}
K\text{ compacto},\\
f:K\to\mathbb R\text{ continua}
\end{array}
\Longrightarrow
\begin{cases}
f(K)\text{ es compacto},\\
f\text{ alcanza máximo y mínimo},\\
f\text{ es uniformemente continua}.
\end{cases}
}
$$

Estas tres propiedades son formas diferentes de control global.

# Relación con el teorema del valor intermedio

`MA-CON-0017` mostró que la continuidad sobre un intervalo impide huecos entre valores alcanzados.

`MA-CON-0018` mostró que, sobre un intervalo cerrado y acotado, los extremos de la imagen son alcanzados.

`MA-CON-0019` muestra ahora que, sobre ese mismo dominio, el control local puede hacerse uniforme.

Por tanto, para

$$
f:[a,b]\to\mathbb R
$$

continua tenemos simultáneamente:

$$
\boxed{
\begin{array}{ll}
\text{valor intermedio:} & \text{la imagen no tiene huecos},\\[1mm]
\text{Weierstrass:} & \text{la imagen tiene extremos alcanzados},\\[1mm]
\text{Heine--Cantor:} & \text{la variación local admite una escala global}.
\end{array}
}
$$

# Una consecuencia operativa: controlar toda la función con una misma escala

Sea

$$
f:[a,b]\to\mathbb R
$$

continua y fijemos $\varepsilon>0$.

Por Heine–Cantor existe $\delta>0$ tal que

$$
|x-y|<\delta
\Longrightarrow
|f(x)-f(y)|<\varepsilon
$$

para todos $x,y\in[a,b].

Esto significa que cualquier partición del intervalo cuyos subintervalos tengan longitud menor que $\delta$ produce un control uniforme de la oscilación de $f$ dentro de cada subintervalo.

No desarrollaremos todavía teoría de integración, pero esta observación será fundamental más adelante: permite convertir una función continua en un objeto que puede aproximarse globalmente mediante una malla suficientemente fina.

::: {.ma-block .ma-intuicion}
**Puente hacia el cálculo posterior**

La continuidad uniforme permite elegir una única resolución horizontal para todo el intervalo.

Ésta es precisamente la clase de control necesaria cuando se subdivide un intervalo entero en muchas piezas y se quiere que todas obedezcan simultáneamente la misma tolerancia.
:::

# Errores frecuentes

## Error 1: creer que continua significa uniformemente continua

Falso en dominios generales.

$$
\frac1x\text{ en }(0,1]
$$

y

$$
x^2\text{ en }\mathbb R
$$

son continuas pero no uniformemente continuas.

## Error 2: permitir que $\delta$ dependa del punto

Si para cada $a$ escribimos

$$
\delta=\delta(a,\varepsilon),
$$

sólo estamos demostrando continuidad ordinaria.

Para continuidad uniforme necesitamos

$$
\delta=\delta(\varepsilon).
$$

## Error 3: pensar que compactitud es necesaria

No.

La identidad en $\mathbb R$ es uniformemente continua y $\mathbb R$ no es compacto.

Heine–Cantor afirma que la compacidad es una hipótesis **suficiente para todas las funciones continuas** sobre ese dominio.

## Error 4: confundir uniformidad con una pendiente constante

Una función uniformemente continua no tiene por qué ser lineal ni Lipschitz.

El ejemplo

$$
\sqrt{x}
$$

en $[0,\infty)$ muestra que pueden existir controles globales de forma no lineal.

# Qué conviene recordar

::: {.ma-block .ma-comprobacion}
**Continuidad vs. continuidad uniforme**

Continuidad en $D$:

$$
\forall a\in D\;\forall\varepsilon>0\;\exists\delta>0\;\forall x\in D.
$$

Continuidad uniforme en $D$:

$$
\forall\varepsilon>0\;\exists\delta>0\;\forall x,y\in D.
$$

Siempre:

$$
\boxed{
\text{uniformemente continua}
\Longrightarrow
\text{continua}.
}
$$

Si $K$ es compacto:

$$
\boxed{
f:K\to\mathbb R\text{ continua}
\Longrightarrow
f\text{ uniformemente continua}.
}
$$

Si además existe $L\ge0$ con

$$
|f(x)-f(y)|\le L|x-y|,
$$

entonces $f$ es uniformemente continua, aunque el dominio no sea compacto.
:::

# Cierre del bloque Funciones → Análisis

Con esta página queda completada una primera arquitectura rigurosa de funciones y análisis real elemental.

La ruta construida es:

$$
\text{funciones}
\longrightarrow
\text{límites}
\longrightarrow
\text{continuidad}
\longrightarrow
\text{completitud}
\longrightarrow
\text{valor intermedio}
\longrightarrow
\text{compacidad}
\longrightarrow
\text{Weierstrass}
\longrightarrow
\text{Heine--Cantor}.
$$

Ya disponemos de:

- lenguaje estructural de funciones;
- límites y continuidad épsilon-delta;
- orden, supremo e ínfimo;
- completitud de $\mathbb R$;
- teoremas globales de existencia;
- compacidad en la recta real;
- control uniforme de funciones continuas sobre compactos.

Esta base permite abrir la siguiente etapa natural del cálculo: **derivación**, comenzando por la definición de derivada como límite de cocientes incrementales.

## Conexiones

Esta página depende directamente de:

- `MA-CON-0008` para composición de funciones;
- `MA-CON-0014` para continuidad épsilon-delta;
- `MA-CON-0018` para compacidad y recubrimientos abiertos.

También reutiliza:

- `MA-CON-0016` para la propiedad arquimediana;
- `MA-CON-0017` para situar Heine–Cantor junto a los demás resultados globales de continuidad.

La idea central puede resumirse en una sola frase:

$$
\boxed{
\text{la compacidad convierte continuidad local en control uniforme global}.}
$$
