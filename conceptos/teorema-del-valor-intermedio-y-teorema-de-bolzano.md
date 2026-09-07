---
title: "Teorema del valor intermedio y teorema de Bolzano"
description: "Cómo la continuidad y la completitud de los números reales garantizan valores intermedios y raíces, mediante una demostración rigurosa basada en el supremo."
content-id: MA-CON-0017
content-type: concept
status: published
date-created: 2026-09-07
date-modified: 2026-09-07
areas:
  - analisis
  - calculo
level: introductorio
topics:
  - continuidad
  - teorema-del-valor-intermedio
  - teorema-de-bolzano
  - existencia-de-raices
  - teoremas-de-existencia
  - completitud
  - supremo
  - propiedad-del-supremo
  - numeros-reales
prerequisites:
  - MA-CON-0005
  - MA-CON-0014
  - MA-CON-0016
related:
  - MA-CON-0015
provenance:
  type: classical
  sources: []
license: GFDL-1.3-or-later
---

En `MA-CON-0014` definimos la continuidad como una propiedad **local**: cerca de un punto $c$, los valores $f(x)$ permanecen cerca de $f(c)$. En `MA-CON-0016` introdujimos una propiedad estructural de los números reales: todo conjunto no vacío y acotado superiormente posee un supremo.

Ahora ambas ideas se combinan para obtener un resultado **global**.

Si una función continua parte de un valor situado por debajo de cierto nivel $y$ y termina por encima de ese nivel, entonces no puede evitarlo durante el recorrido.

::: {.ma-block .ma-intuicion}
**Intuición**

Una función continua definida en todo el intervalo $[a,b]$ no puede pasar de

$$
f(a)<y
$$

a

$$
f(b)>y
$$

sin tomar en algún punto el valor exacto $y$.

La continuidad impide un salto local. La completitud de $\mathbb R$ permite construir rigurosamente el punto donde se produce el cruce.
:::

## El teorema de Bolzano: un cambio de signo obliga a una raíz

La versión más conocida del principio se refiere al nivel $y=0$.

::: {.ma-block .ma-definicion}
**Teorema de Bolzano**

Sea

$$
f:[a,b]\to\mathbb R
$$

continua en $[a,b]$, con $a<b$.

Si

$$
f(a)f(b)<0,
$$

entonces existe al menos un

$$
c\in(a,b)
$$

tal que

$$
\boxed{f(c)=0.}
$$
:::

La hipótesis

$$
f(a)f(b)<0
$$

significa que $f(a)$ y $f(b)$ tienen signos opuestos. Por tanto, el número $0$ está estrictamente entre ambos valores.

Bolzano será una consecuencia inmediata de un resultado más general.

## El teorema del valor intermedio

::: {.ma-block .ma-definicion}
**Teorema del valor intermedio**

Sea

$$
f:[a,b]\to\mathbb R
$$

continua en $[a,b]$, con $a<b$.

Si un número $y\in\mathbb R$ está entre $f(a)$ y $f(b)$, es decir,

$$
\min\{f(a),f(b)\}\le y\le\max\{f(a),f(b)\},
$$

entonces existe

$$
c\in[a,b]
$$

tal que

$$
\boxed{f(c)=y.}
$$
:::

El teorema afirma que la función **alcanza todos los niveles intermedios** entre los valores de sus extremos.

Si, por ejemplo,

$$
f(a)=2,
\qquad
f(b)=7,
$$

entonces una función continua en $[a,b]$ debe tomar los valores

$$
3,\quad 4.5,\quad 6,
$$

y cualquier otro real comprendido entre $2$ y $7$.

::: {.ma-block .ma-observacion}
**“Entre” no supone que la función sea creciente**

El teorema no exige monotonía. La función puede subir, bajar y oscilar muchas veces.

Sólo afirma que si sus valores en los extremos dejan un nivel $y$ entre ambos, la continuidad obliga a que ese nivel sea alcanzado al menos una vez.
:::

## Bolzano es un caso particular

Supongamos

$$
f(a)f(b)<0.
$$

Entonces uno de los valores $f(a)$ y $f(b)$ es negativo y el otro positivo. Por tanto,

$$
0
$$

está estrictamente entre ellos.

Aplicando el teorema del valor intermedio con

$$
y=0,
$$

obtenemos un punto $c\in[a,b]$ tal que

$$
f(c)=0.
$$

Como el producto $f(a)f(b)$ es estrictamente negativo, ninguno de los extremos es una raíz. En consecuencia,

$$
\boxed{c\in(a,b).}
$$

Así, el teorema de Bolzano es exactamente el caso $y=0$ del teorema del valor intermedio cuando los valores extremos tienen signos opuestos.

# Demostración rigurosa del teorema del valor intermedio

La demostración mostrará de manera explícita dónde entra la completitud de $\mathbb R$.

Primero resolvemos el caso

$$
f(a)<y<f(b).
$$

Después trataremos el orden invertido.

## Paso 0. Los casos en que $y$ coincide con un extremo

Si

$$
y=f(a),
$$

podemos tomar simplemente

$$
c=a.
$$

Si

$$
y=f(b),
$$

podemos tomar

$$
c=b.
$$

Por tanto, la parte realmente interesante de la prueba ocurre cuando $y$ está **estrictamente** entre los dos valores extremos.

## Paso 1. Suponemos $f(a)<y<f(b)$

Fijemos entonces

$$
\boxed{f(a)<y<f(b).}
$$

Queremos encontrar un punto donde la función alcance exactamente el nivel $y$.

En vez de intentar adivinar ese punto, construiremos un conjunto de puntos donde la función todavía está por debajo —o exactamente sobre— ese nivel.

Definimos

$$
\boxed{
A=\{x\in[a,b]:f(x)\le y\}.
}
$$

::: {.ma-block .ma-intuicion}
**Qué representa $A$**

El conjunto $A$ reúne todos los puntos del intervalo en los que la gráfica se encuentra a altura menor o igual que $y$.

Buscaremos la frontera derecha de ese conjunto.

Esa frontera será

$$
c=\sup A.
$$
:::

## Paso 2. $A$ no es vacío y está acotado superiormente

Como

$$
f(a)<y,
$$

tenemos en particular

$$
f(a)\le y.
$$

Por tanto,

$$
a\in A,
$$

y así

$$
A\ne\varnothing.
$$

Además,

$$
A\subseteq[a,b].
$$

Luego todo $x\in A$ satisface

$$
x\le b,
$$

de modo que $b$ es una cota superior de $A$.

Tenemos exactamente las dos hipótesis necesarias para aplicar la propiedad del supremo de `MA-CON-0016`:

$$
A\ne\varnothing
$$

y

$$
A\text{ está acotado superiormente}.
$$

Por completitud de $\mathbb R$, existe entonces

$$
\boxed{c=\sup A.}
$$

Este es el punto decisivo en que la estructura de los números reales entra en la demostración.

## Paso 3. El punto $c$ está dentro del intervalo

Sabemos inicialmente que

$$
a\le c\le b.
$$

Pero en el caso estricto que estamos estudiando podemos demostrar algo mejor:

$$
\boxed{a<c<b.}
$$

### Por qué $c>a$

Como

$$
f(a)<y,
$$

definimos

$$
\varepsilon_a=\frac{y-f(a)}2>0.
$$

La continuidad de $f$ en $a$ proporciona un $\delta_a>0$ tal que, para $x\in[a,b]$,

$$
|x-a|<\delta_a
\quad\Longrightarrow\quad
|f(x)-f(a)|<\varepsilon_a.
$$

Tomemos

$$
\eta_a=
\min\left\{\frac{\delta_a}{2},\frac{b-a}{2}\right\}>0
$$

y definamos

$$
x_a=a+\eta_a.
$$

Entonces

$$
a<x_a<b
$$

y

$$
|x_a-a|<\delta_a.
$$

Por continuidad,

$$
f(x_a)<f(a)+\varepsilon_a
=\frac{f(a)+y}{2}
<y.
$$

Por tanto,

$$
x_a\in A.
$$

Como $c$ es una cota superior de $A$,

$$
c\ge x_a>a.
$$

Luego

$$
\boxed{c>a.}
$$

### Por qué $c<b$

Como

$$
f(b)>y,
$$

definimos

$$
\varepsilon_b=\frac{f(b)-y}{2}>0.
$$

Por continuidad en $b$, existe $\delta_b>0$ tal que, para $x\in[a,b]$,

$$
|x-b|<\delta_b
\quad\Longrightarrow\quad
|f(x)-f(b)|<\varepsilon_b.
$$

Tomemos

$$
\eta_b=
\min\left\{\frac{\delta_b}{2},\frac{b-a}{2}\right\}>0
$$

y definamos

$$
u=b-\eta_b.
$$

Si

$$
x\in[u,b],
$$

entonces

$$
|x-b|\le\eta_b<\delta_b,
$$

y por tanto

$$
f(x)>f(b)-\varepsilon_b
=\frac{f(b)+y}{2}
>y.
$$

Ningún punto de $[u,b]$ pertenece entonces a $A$. En consecuencia, todo punto de $A$ satisface

$$
x<u,
$$

de modo que $u$ es una cota superior de $A$.

Como $c$ es la menor cota superior,

$$
c\le u<b.
$$

Luego

$$
\boxed{c<b.}
$$

Hemos probado que

$$
\boxed{a<c<b.}
$$

Esto nos permitirá movernos ligeramente a izquierda y derecha de $c$ sin abandonar $[a,b]$.

## Paso 4. No puede ocurrir que $f(c)<y$

Supongamos, buscando una contradicción, que

$$
f(c)<y.
$$

Definimos

$$
\varepsilon=\frac{y-f(c)}2>0.
$$

Como $f$ es continua en $c$, existe $\delta>0$ tal que

$$
|x-c|<\delta
\quad\Longrightarrow\quad
|f(x)-f(c)|<\varepsilon
$$

para $x\in[a,b]$.

Como $c<b$, podemos elegir

$$
\eta=
\min\left\{\frac\delta2,\frac{b-c}{2}\right\}>0
$$

y tomar

$$
x=c+\eta.
$$

Entonces

$$
x>c,
\qquad
x\in[a,b],
\qquad
|x-c|<\delta.
$$

Por continuidad,

$$
f(x)<f(c)+\varepsilon
=\frac{f(c)+y}{2}
<y.
$$

Por tanto,

$$
x\in A.
$$

Pero esto es imposible: $c$ es una cota superior de $A$, y acabamos de encontrar

$$
x\in A
\quad\text{con}\quad
x>c.
$$

La contradicción demuestra que

$$
\boxed{f(c)\ge y.}
$$

## Paso 5. No puede ocurrir que $f(c)>y$

Supongamos ahora

$$
f(c)>y.
$$

Definimos

$$
\varepsilon=\frac{f(c)-y}{2}>0.
$$

Por continuidad en $c$, existe $\delta>0$ tal que

$$
|x-c|<\delta
\quad\Longrightarrow\quad
|f(x)-f(c)|<\varepsilon.
$$

Como $c>a$, fijemos

$$
\eta=
\min\left\{\frac\delta2,\frac{c-a}{2}\right\}>0.
$$

Ahora utilizamos la caracterización épsilon del supremo demostrada en `MA-CON-0016`.

Como

$$
c=\sup A,
$$

existe un punto $x\in A$ tal que

$$
c-\eta<x\le c.
$$

En particular,

$$
|x-c|<\eta<\delta.
$$

La continuidad implica entonces

$$
f(x)>f(c)-\varepsilon
=\frac{f(c)+y}{2}
>y.
$$

Pero $x\in A$, y por definición de $A$ eso exige

$$
f(x)\le y.
$$

Obtenemos una contradicción.

Por tanto,

$$
\boxed{f(c)\le y.}
$$

## Paso 6. Conclusión del primer caso

Hemos demostrado simultáneamente

$$
f(c)\ge y
$$

y

$$
f(c)\le y.
$$

Por antisimetría del orden en $\mathbb R$,

$$
\boxed{f(c)=y.}
$$

Éste es precisamente el punto cuya existencia queríamos demostrar.

::: {.ma-block .ma-comprobacion}
**Dónde se usó cada ingrediente**

- El **orden** permitió definir el conjunto $A$ mediante la condición $f(x)\le y$ y comparar cotas.
- La **completitud** aseguró que $c=\sup A$ existe en $\mathbb R$.
- La **caracterización épsilon del supremo** produjo puntos de $A$ arbitrariamente cercanos a $c$ desde la izquierda.
- La **continuidad** trasladó la cercanía en la variable a cercanía entre valores de la función.
- La condición de que el dominio sea todo el intervalo $[a,b]$ permitió movernos entre los extremos sin encontrar huecos en la variable.
:::

## Paso 7. El caso invertido $f(b)<y<f(a)$

Queda tratar el segundo orden posible:

$$
f(b)<y<f(a).
$$

Podríamos repetir toda la demostración utilizando el conjunto

$$
\{x\in[a,b]:f(x)\ge y\}.
$$

Pero hay una reducción más limpia.

Definamos

$$
g(x)=-f(x).
$$

Como $f$ es continua, $g$ también es continua. Además,

$$
f(b)<y<f(a)
$$

equivale a

$$
-f(a)<-y<-f(b),
$$

es decir,

$$
g(a)<-y<g(b).
$$

El primer caso, ya demostrado, aplicado a $g$ garantiza un $c\in[a,b]$ tal que

$$
g(c)=-y.
$$

Como $g(c)=-f(c)$,

$$
-f(c)=-y,
$$

y por tanto

$$
\boxed{f(c)=y.}
$$

Con esto quedan cubiertos ambos órdenes posibles y los casos de igualdad en los extremos. El teorema del valor intermedio está demostrado.

## El patrón de demostración detrás del teorema

La prueba anterior es importante no sólo por el resultado. Introduce un método reutilizable del análisis real.

::: {.ma-block .ma-metodo}
**Construcción mediante un supremo**

Cuando queremos demostrar la existencia de un punto crítico $c$:

1. definimos un conjunto $A$ formado por puntos que satisfacen una propiedad parcial;
2. demostramos que $A$ es no vacío;
3. demostramos que $A$ está acotado;
4. usamos completitud para definir

   $$
   c=\sup A;
   $$

5. aproximamos $c$ mediante elementos de $A$;
6. usamos continuidad, orden u otra propiedad local para demostrar que la frontera $c$ satisface exactamente la condición buscada.

En el teorema del valor intermedio, la propiedad parcial fue

$$
f(x)\le y.
$$
:::

Este patrón convierte una pregunta de existencia en una construcción rigurosa: el punto no se adivina ni se obtiene mediante una fórmula, sino como frontera de un conjunto.

## Ejemplo: existencia de una raíz sin resolver la ecuación

Consideremos

$$
f(x)=x^5+x-1.
$$

Al ser un polinomio, $f$ es continua en $\mathbb R$. En los extremos del intervalo $[0,1]$,

$$
f(0)=-1<0
$$

y

$$
f(1)=1>0.
$$

Por el teorema de Bolzano existe al menos un

$$
c\in(0,1)
$$

tal que

$$
\boxed{c^5+c-1=0.}
$$

No hemos necesitado despejar $c$.

Podemos incluso localizar mejor una raíz evaluando en dos puntos:

$$
f\left(\frac34\right)
=
\frac{243}{1024}+\frac34-1
=
-\frac{13}{1024}<0,
$$

mientras que

$$
f\left(\frac45\right)
=
\frac{1024}{3125}+\frac45-1
=
\frac{399}{3125}>0.
$$

Aplicando Bolzano otra vez,

$$
\boxed{
\exists c\in\left(\frac34,\frac45\right)
\text{ tal que }
c^5+c-1=0.
}
$$

::: {.ma-block .ma-intuicion}
**Existencia antes que cálculo exacto**

El teorema responde a la pregunta

> ¿hay una solución?

sin exigir primero una fórmula que produzca esa solución.

Esta separación entre **existencia** y **cálculo explícito** es una idea central del análisis.
:::

## El teorema no dice dónde está exactamente $c$

La conclusión

$$
\exists c\in[a,b]:f(c)=y
$$

no proporciona por sí sola una expresión cerrada para $c$.

El punto puede localizarse posteriormente mediante argumentos adicionales o procedimientos numéricos, pero eso pertenece a otra pregunta.

## El teorema tampoco garantiza unicidad

El teorema del valor intermedio y Bolzano son teoremas de **existencia**, no de unicidad.

Por ejemplo,

$$
p(x)=x^3-x
$$

es continua en $[-2,2]$ y satisface

$$
p(-2)=-6<0,
\qquad
p(2)=6>0.
$$

Bolzano garantiza al menos una raíz en $(-2,2)$.

De hecho,

$$
p(x)=x(x-1)(x+1),
$$

de modo que existen tres:

$$
-1,\quad0,\quad1.
$$

::: {.ma-block .ma-error}
**Error frecuente**

De

$$
f(a)f(b)<0
$$

no se concluye que exista **una única** raíz.

La conclusión correcta es:

$$
\boxed{\text{existe al menos una raíz en }(a,b).}
$$
:::

## Sin continuidad el resultado puede fallar

Consideremos la función

$$
f(x)=
\begin{cases}
-1,&x<0,\\
1,&x\ge0,
\end{cases}
$$

definida en $[-1,1]$.

Tenemos

$$
f(-1)=-1,
\qquad
f(1)=1.
$$

El valor

$$
y=0
$$

está entre los valores de los extremos.

Sin embargo,

$$
f(x)\ne0
$$

para todo $x\in[-1,1]$.

La función salta directamente de $-1$ a $1$ en $0$.

::: {.ma-block .ma-error}
**La continuidad no es decorativa**

El cambio de signo de los extremos, por sí solo, no garantiza una raíz.

Lo que impide saltar sobre el nivel intermedio es la continuidad.
:::

## Por qué importa que el dominio sea un intervalo completo

La continuidad siempre es relativa al dominio, como vimos en `MA-CON-0014`.

Si eliminamos puntos intermedios del dominio, una función puede ser continua en todos los puntos de su dominio y aun así no alcanzar valores intermedios entre dos extremos.

Por ejemplo, sea

$$
D=[-1,0)\cup(0,1]
$$

y definamos

$$
h(x)=
\begin{cases}
-1,&x<0,\\
1,&x>0.
\end{cases}
$$

La función es localmente constante —y por tanto continua— en cada punto de $D$. Además,

$$
h(-1)=-1,
\qquad
h(1)=1.
$$

Pero no existe $x\in D$ con

$$
h(x)=0.
$$

El problema es que el dominio no contiene todos los puntos entre $-1$ y $1$.

En el teorema del valor intermedio, la hipótesis

$$
f:[a,b]\to\mathbb R
$$

garantiza precisamente que no haya huecos de este tipo en la variable real.

## La completitud de $\mathbb R$ no es accidental

La demostración utilizó la existencia de

$$
c=\sup A.
$$

Esa existencia depende de la completitud de los reales.

La diferencia se ve con claridad si intentamos trabajar sólo con números racionales.

Consideremos

$$
D=\mathbb Q\cap[0,2]
$$

y la función

$$
f:D\to\mathbb Q,
\qquad
f(x)=x^2-2.
$$

Esta función es continua respecto de la métrica usual restringida a $\mathbb Q$. Además,

$$
f(0)=-2<0,
\qquad
f(2)=2>0.
$$

Pero no existe ningún número racional $c$ tal que

$$
c^2-2=0,
$$

porque

$$
\sqrt2\notin\mathbb Q.
$$

::: {.ma-block .ma-observacion}
**Qué revela el ejemplo racional**

Este ejemplo no contradice el teorema real: su dominio no es el intervalo real $[0,2]$, sino su parte racional.

Lo que muestra es que, al pasar de $\mathbb R$ a $\mathbb Q$, desaparece justamente el punto frontera que la completitud real garantiza.

La relación con `MA-CON-0016` es por tanto estructural, no meramente técnica.
:::

## Relación con el orden y la comparación

En `MA-CON-0005` aprendimos a manipular desigualdades preservando correctamente el orden. En `MA-CON-0015` usamos desigualdades para comparar funciones y forzar límites mediante el teorema del sándwich.

Aquí el orden cumple una función distinta: permite separar los puntos según

$$
f(x)\le y
$$

y

$$
f(x)>y,
$$

construir una frontera mediante el supremo y demostrar que la continuidad obliga a que esa frontera corresponda exactamente al nivel $y$.

Podemos resumir la arquitectura lógica así:

$$
\boxed{
\text{orden}
+\text{completitud de }\mathbb R
+\text{continuidad}
\Longrightarrow
\text{valor intermedio}.
}
$$

Y para $y=0$:

$$
\boxed{
\text{continuidad}
+\text{cambio de signo}
\Longrightarrow
\text{existencia de una raíz}.
}
$$

## Control de interpretación

Antes de aplicar el teorema del valor intermedio conviene verificar cuatro puntos:

1. la función está definida en **todo** el intervalo $[a,b]$;
2. la función es continua en $[a,b]$;
3. el nivel $y$ está realmente entre $f(a)$ y $f(b)$;
4. la conclusión buscada es de **existencia**, salvo que dispongamos de hipótesis adicionales que permitan demostrar unicidad.

Para Bolzano, el tercer control se sustituye por

$$
f(a)f(b)<0.
$$

::: {.ma-block .ma-comprobacion}
**Lectura final**

El teorema del valor intermedio no es una regla gráfica informal.

Su demostración se apoya en una cadena rigurosa:

$$
A=\{x:f(x)\le y\}
\longrightarrow
c=\sup A
\longrightarrow
\text{aproximación a }c
\longrightarrow
\text{continuidad}
\longrightarrow
f(c)=y.
$$

Así, la completitud de $\mathbb R$ se convierte en un teorema concreto sobre el comportamiento de las funciones continuas.
:::
