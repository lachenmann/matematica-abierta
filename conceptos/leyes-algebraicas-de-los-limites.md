---
title: "Leyes algebraicas de los límites"
description: "Cómo combinar límites mediante suma, resta, producto, cociente, potencias y operaciones algebraicas, con demostraciones épsilon-delta y aplicaciones a polinomios y funciones racionales."
content-id: MA-CON-0013
content-type: concept
status: published
date-created: 2026-09-07
date-modified: 2026-09-07
areas:
  - calculo
  - analisis
level: introductorio
topics:
  - funciones
  - limites
  - leyes-de-limites
  - suma-de-limites
  - producto-de-limites
  - cociente-de-limites
  - acotacion-local
  - polinomios
  - funciones-racionales
  - epsilon-delta
prerequisites:
  - MA-CON-0011
related:
  - MA-CON-0005
  - MA-CON-0012
provenance:
  type: classical
  sources: []
license: GFDL-1.3-or-later
---

Una vez definida rigurosamente la noción de límite, el siguiente paso es entender cómo se comporta frente a las operaciones algebraicas habituales.

Si sabemos que

$$
\lim_{x\to a}f(x)=L
\qquad\text{y}\qquad
\lim_{x\to a}g(x)=M,
$$

queremos justificar afirmaciones como

$$
\lim_{x\to a}(f(x)+g(x))=L+M
$$

o

$$
\lim_{x\to a}(f(x)g(x))=LM.
$$

Estas fórmulas son familiares, pero en análisis no se aceptan como simples reglas de manipulación simbólica: se deducen de la definición épsilon-delta.

::: {.ma-block .ma-intuicion}
**Intuición**

Si $f(x)$ está cerca de $L$ y $g(x)$ está cerca de $M$, entonces:

- $f(x)+g(x)$ debe estar cerca de $L+M$;
- $f(x)g(x)$ debe estar cerca de $LM$;
- si $M\ne0$, entonces $g(x)$ permanece lejos de $0$ cuando $x$ está suficientemente cerca de $a$, y por ello $f(x)/g(x)$ debe estar cerca de $L/M$.

La dificultad matemática consiste en convertir estas intuiciones en controles cuantitativos precisos.
:::

## Marco común

En esta página trabajaremos principalmente con dos funciones

$$
f,g:D\to\mathbb R,
$$

definidas sobre un mismo conjunto

$$
D\subseteq\mathbb R,
$$

y con $a$ punto de acumulación de $D$.

Supondremos que

$$
\lim_{x\to a}f(x)=L,
\qquad
\lim_{x\to a}g(x)=M.
$$

Trabajar sobre un dominio común evita una dificultad secundaria: si dos funciones están definidas sobre dominios distintos, la suma, el producto o el cociente sólo están definidos donde ambos dominios se intersectan.

Las leyes que probaremos se aplican igualmente a límites laterales, siempre que el punto sea de acumulación por el lado correspondiente.

## Primeras leyes: constantes e identidad

Antes de combinar funciones conviene fijar dos límites básicos.

::: {.ma-block .ma-definicion}
**Límite de una función constante**

Para cualquier $c\in\mathbb R$,

$$
\boxed{
\lim_{x\to a}c=c.
}
$$
:::

La demostración es inmediata. Para todo $x$,

$$
|c-c|=0.
$$

Por tanto, dado cualquier $\varepsilon>0$, cualquier elección de $\delta>0$ satisface

$$
0<|x-a|<\delta
\quad\Longrightarrow\quad
|c-c|<\varepsilon.
$$

::: {.ma-block .ma-definicion}
**Límite de la función identidad**

Si $a$ es punto de acumulación de $D$, entonces

$$
\boxed{
\lim_{x\to a}x=a.
}
$$
:::

En efecto,

$$
|x-a|<\delta.
$$

Dado $\varepsilon>0$, basta elegir

$$
\delta=\varepsilon.
$$

## Multiplicación por una constante

Sea $c\in\mathbb R$.

Entonces

$$
\boxed{
\lim_{x\to a}cf(x)=cL.
}
$$

Si $c=0$, la afirmación es inmediata.

Si $c\ne0$, dado $\varepsilon>0$, como

$$
\lim_{x\to a}f(x)=L,
$$

podemos exigir

$$
|f(x)-L|<\frac{\varepsilon}{|c|}.
$$

Entonces

$$
|cf(x)-cL|
=|c|\,|f(x)-L|
<\varepsilon.
$$

## Ley de la suma

::: {.ma-block .ma-definicion}
**Teorema — suma de límites**

Si

$$
\lim_{x\to a}f(x)=L
$$

y

$$
\lim_{x\to a}g(x)=M,
$$

entonces

$$
\boxed{
\lim_{x\to a}(f(x)+g(x))=L+M.
}
$$
:::

### Demostración

Sea $\varepsilon>0$.

Como

$$
\lim_{x\to a}f(x)=L,
$$

existe $\delta_f>0$ tal que

$$
0<|x-a|<\delta_f
\quad\Longrightarrow\quad
|f(x)-L|<\frac{\varepsilon}{2}.
$$

Del mismo modo, existe $\delta_g>0$ tal que

$$
0<|x-a|<\delta_g
\quad\Longrightarrow\quad
|g(x)-M|<\frac{\varepsilon}{2}.
$$

Elegimos

$$
\delta=\min\{\delta_f,\delta_g\}.
$$

Si

$$
0<|x-a|<\delta,
$$

entonces ambas estimaciones son válidas y, por la desigualdad triangular,

$$
\begin{aligned}
|(f(x)+g(x))-(L+M)|
&=|(f(x)-L)+(g(x)-M)|\\
&\le |f(x)-L|+|g(x)-M|\\
&<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}\\
&=\varepsilon.
\end{aligned}
$$

Por tanto,

$$
\lim_{x\to a}(f(x)+g(x))=L+M.
$$

::: {.ma-block .ma-metodo}
**Una técnica que aparecerá repetidamente**

Cuando necesitamos satisfacer simultáneamente varias condiciones locales, obtenemos varios radios

$$
\delta_1,\delta_2,\ldots
$$

y tomamos

$$
\boxed{
\delta=\min\{\delta_1,\delta_2,\ldots\}.
}
$$

Así garantizamos que todas las condiciones sean válidas al mismo tiempo.
:::

## Ley de la resta

Como

$$
f(x)-g(x)=f(x)+(-1)g(x),
$$

las leyes anteriores implican inmediatamente

$$
\boxed{
\lim_{x\to a}(f(x)-g(x))=L-M.
}
$$

## Un lema fundamental: una función con límite finito está localmente acotada

La suma se controla directamente mediante la desigualdad triangular. El producto requiere una idea adicional.

::: {.ma-block .ma-definicion}
**Lema — acotación local**

Si

$$
\lim_{x\to a}f(x)=L,
$$

entonces existe un $r>0$ y un número $K>0$ tales que

$$
0<|x-a|<r
\quad\Longrightarrow\quad
|f(x)|\le K.
$$
:::

### Demostración

Tomemos, por ejemplo,

$$
\varepsilon=1.
$$

Por la definición de límite existe $r>0$ tal que

$$
0<|x-a|<r
\quad\Longrightarrow\quad
|f(x)-L|<1.
$$

Entonces

$$
|f(x)|
\le |f(x)-L|+|L|
<1+|L|.
$$

Podemos tomar

$$
K=|L|+1.
$$

::: {.ma-block .ma-observacion}
**Qué significa el lema**

La existencia de un límite real impide que la función se vuelva arbitrariamente grande en un entorno perforado suficientemente pequeño del punto.

No estamos afirmando que $f$ sea globalmente acotada, sino sólo que lo es **localmente cerca de $a$**.
:::

## Ley del producto

::: {.ma-block .ma-definicion}
**Teorema — producto de límites**

Si

$$
\lim_{x\to a}f(x)=L
$$

y

$$
\lim_{x\to a}g(x)=M,
$$

entonces

$$
\boxed{
\lim_{x\to a}f(x)g(x)=LM.
}
$$
:::

### Demostración

Queremos controlar

$$
|f(x)g(x)-LM|.
$$

Añadimos y restamos $f(x)M$:

$$
\begin{aligned}
f(x)g(x)-LM
&=f(x)g(x)-f(x)M+f(x)M-LM\\
&=f(x)(g(x)-M)+M(f(x)-L).
\end{aligned}
$$

Por tanto,

$$
|f(x)g(x)-LM|
\le
|f(x)|\,|g(x)-M|
+|M|\,|f(x)-L|.
$$

Por el lema de acotación local, existe $r>0$ tal que

$$
0<|x-a|<r
\quad\Longrightarrow\quad
|f(x)|\le |L|+1.
$$

Definamos

$$
A=|L|+1.
$$

Dado $\varepsilon>0$, podemos elegir $\delta_1>0$ de modo que

$$
0<|x-a|<\delta_1
\quad\Longrightarrow\quad
|g(x)-M|<\frac{\varepsilon}{2A}.
$$

También elegimos $\delta_2>0$ tal que

$$
0<|x-a|<\delta_2
\quad\Longrightarrow\quad
|f(x)-L|<\frac{\varepsilon}{2(|M|+1)}.
$$

Finalmente tomamos

$$
\delta=\min\{r,\delta_1,\delta_2\}.
$$

Entonces

$$
\begin{aligned}
|f(x)g(x)-LM|
&\le |f(x)|\,|g(x)-M|+|M|\,|f(x)-L|\\
&< A\frac{\varepsilon}{2A}
+|M|\frac{\varepsilon}{2(|M|+1)}\\
&<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}\\
&=\varepsilon.
\end{aligned}
$$

Así queda demostrada la ley del producto.

## Potencias naturales

Aplicando repetidamente la ley del producto obtenemos, para todo entero $n\ge1$,

$$
\boxed{
\lim_{x\to a}(f(x))^n=L^n.
}
$$

Por ejemplo,

$$
\lim_{x\to a}(f(x))^3
=
\left(\lim_{x\to a}f(x)\right)^3.
$$

Para $n=0$, cuando la expresión considerada es la función constante $1$, el resultado se reduce a

$$
\lim_{x\to a}1=1.
$$

## Separación local de cero

Antes de tratar cocientes necesitamos demostrar que una función cuyo límite es distinto de cero no puede anularse arbitrariamente cerca del punto.

::: {.ma-block .ma-definicion}
**Lema — separación de cero**

Si

$$
\lim_{x\to a}g(x)=M
$$

y

$$
M\ne0,
$$

entonces existe $r>0$ tal que

$$
0<|x-a|<r
\quad\Longrightarrow\quad
|g(x)|>\frac{|M|}{2}>0.
$$
:::

### Demostración

Tomamos

$$
\varepsilon=\frac{|M|}{2}.
$$

Existe $r>0$ tal que

$$
0<|x-a|<r
\quad\Longrightarrow\quad
|g(x)-M|<\frac{|M|}{2}.
$$

Por la desigualdad triangular inversa,

$$
|g(x)|
\ge |M|-|g(x)-M|
>
|M|-\frac{|M|}{2}
=
\frac{|M|}{2}.
$$

En particular,

$$
g(x)\ne0
$$

para todo $x$ suficientemente cercano a $a$, salvo eventualmente el propio punto $a$.

::: {.ma-block .ma-observacion}
**Consecuencia conceptual**

La condición $M\ne0$ en la ley del cociente no es un detalle formal. Es lo que garantiza que el denominador deja de acercarse peligrosamente a cero en un entorno perforado suficientemente pequeño.
:::

## Límite del recíproco

Si

$$
\lim_{x\to a}g(x)=M
\qquad\text{con}\qquad
M\ne0,
$$

entonces

$$
\boxed{
\lim_{x\to a}\frac{1}{g(x)}=\frac{1}{M}.
}
$$

### Demostración

Por el lema anterior, para $x$ suficientemente cercano a $a$,

$$
|g(x)|>\frac{|M|}{2}.
$$

Entonces

$$
\begin{aligned}
\left|
\frac1{g(x)}-\frac1M
\right|
&=
\frac{|M-g(x)|}{|g(x)|\,|M|}\\
&<
\frac{2}{|M|^2}|g(x)-M|.
\end{aligned}
$$

Dado $\varepsilon>0$, basta exigir simultáneamente

$$
|g(x)-M|<\frac{|M|}{2}
$$

y

$$
|g(x)-M|<\frac{\varepsilon |M|^2}{2}.
$$

La definición de límite permite obtener un $\delta>0$ que satisfaga ambas condiciones tomando el mínimo de los radios correspondientes.

Entonces

$$
\left|
\frac1{g(x)}-\frac1M
\right|<\varepsilon.
$$

## Ley del cociente

::: {.ma-block .ma-definicion}
**Teorema — cociente de límites**

Si

$$
\lim_{x\to a}f(x)=L,
\qquad
\lim_{x\to a}g(x)=M,
$$

con

$$
M\ne0,
$$

entonces, donde el cociente está definido,

$$
\boxed{
\lim_{x\to a}\frac{f(x)}{g(x)}
=
\frac{L}{M}.
}
$$
:::

La demostración se obtiene escribiendo

$$
\frac{f(x)}{g(x)}
=
f(x)\frac1{g(x)}
$$

y aplicando la ley del producto junto con el límite del recíproco.

## Resumen de las leyes algebraicas

Si

$$
\lim_{x\to a}f(x)=L
\qquad\text{y}\qquad
\lim_{x\to a}g(x)=M,
$$

entonces:

$$
\boxed{
\lim_{x\to a}(f+g)=L+M
}
$$

$$
\boxed{
\lim_{x\to a}(f-g)=L-M
}
$$

$$
\boxed{
\lim_{x\to a}(cf)=cL
}
$$

$$
\boxed{
\lim_{x\to a}(fg)=LM
}
$$

$$
\boxed{
\lim_{x\to a}f^n=L^n,
\qquad n\in\mathbb N,\ n\ge1
}
$$

y, si $M\ne0$,

$$
\boxed{
\lim_{x\to a}\frac{f}{g}=\frac{L}{M}.
}
$$

::: {.ma-block .ma-error}
**Las leyes no son equivalencias en sentido inverso**

Que exista el límite de una suma o de un producto no implica que existan necesariamente los límites de cada término o factor.

Por ejemplo, para

$$
s(x)=\frac{|x|}{x},
\qquad x\ne0,
$$

el límite bilateral de $s(x)$ en $0$ no existe, pero

$$
s(x)^2=1
$$

para todo $x\ne0$, de modo que

$$
\lim_{x\to0}s(x)^2=1.
$$

La ley del producto dice qué ocurre **si ya conocemos** los límites de los factores; no proporciona el recíproco lógico.
:::

## Aplicación: límites de polinomios

Sea

$$
p(x)=a_0+a_1x+a_2x^2+\cdots+a_nx^n.
$$

Como

$$
\lim_{x\to a}x=a,
$$

las leyes de potencias, multiplicación por constantes y suma permiten concluir

$$
\boxed{
\lim_{x\to a}p(x)=p(a).
}
$$

### Ejemplo

Calculemos

$$
\lim_{x\to2}(2x^3-5x+4).
$$

Por las leyes algebraicas,

$$
\begin{aligned}
\lim_{x\to2}(2x^3-5x+4)
&=2\left(\lim_{x\to2}x\right)^3
-5\left(\lim_{x\to2}x\right)+4\\
&=2(2)^3-5(2)+4\\
&=16-10+4\\
&=10.
\end{aligned}
$$

Por tanto,

$$
\boxed{
\lim_{x\to2}(2x^3-5x+4)=10.
}
$$

## Aplicación: límites de funciones racionales

Sean $p$ y $q$ polinomios y consideremos

$$
r(x)=\frac{p(x)}{q(x)}.
$$

Si

$$
q(a)\ne0,
$$

entonces

$$
\boxed{
\lim_{x\to a}\frac{p(x)}{q(x)}
=
\frac{p(a)}{q(a)}.
}
$$

### Ejemplo

Consideremos

$$
\lim_{x\to1}
\frac{x^2+3x-1}{2x+5}.
$$

El denominador en $x=1$ vale

$$
2(1)+5=7\ne0.
$$

Por tanto,

$$
\begin{aligned}
\lim_{x\to1}
\frac{x^2+3x-1}{2x+5}
&=
\frac{1^2+3(1)-1}{2(1)+5}\\
&=\frac{3}{7}.
\end{aligned}
$$

Así,

$$
\boxed{
\lim_{x\to1}
\frac{x^2+3x-1}{2x+5}
=
\frac37.
}
$$

## Cuando el denominador tiende a cero

La condición

$$
M\ne0
$$

en la ley del cociente es indispensable para aplicar el teorema.

Pero su fracaso **no permite concluir automáticamente que el límite del cociente no exista**.

Consideremos

$$
\frac{x^2-1}{x-1}.
$$

Cuando $x\to1$,

$$
x-1\to0,
$$

por lo que la ley del cociente no puede usarse directamente.

Sin embargo, para $x\ne1$,

$$
\frac{x^2-1}{x-1}
=x+1.
$$

Por el principio de localidad desarrollado en `MA-CON-0011`, ambas expresiones tienen el mismo comportamiento límite en $1$. Entonces

$$
\boxed{
\lim_{x\to1}\frac{x^2-1}{x-1}=2.
}
$$

::: {.ma-block .ma-error}
**No confundir “el teorema no se aplica” con “el límite no existe”**

Si el límite del denominador es $0$, la ley del cociente no proporciona una conclusión.

A partir de ahí puede ocurrir que:

- el límite exista después de una simplificación;
- el límite no exista;
- aparezca un comportamiento no acotado;
- sea necesario usar otra técnica.

La imposibilidad de aplicar una ley no es por sí sola un resultado sobre el límite.
:::

## Las mismas leyes para límites laterales

Supongamos que $a$ es punto de acumulación del dominio por la derecha y que

$$
\lim_{x\to a^+}f(x)=L,
\qquad
\lim_{x\to a^+}g(x)=M.
$$

Todas las demostraciones anteriores permanecen válidas reemplazando la condición

$$
0<|x-a|<\delta
$$

por

$$
0<x-a<\delta.
$$

Por tanto, por ejemplo,

$$
\lim_{x\to a^+}(f(x)+g(x))=L+M
$$

y, si $M\ne0$,

$$
\lim_{x\to a^+}\frac{f(x)}{g(x)}=\frac{L}{M}.
$$

Lo mismo ocurre para límites por la izquierda.

Esto permite combinar las leyes algebraicas con el criterio bilateral de `MA-CON-0012`.

## Qué hemos ganado

Hasta ahora, la definición épsilon-delta permitía estudiar cada límite desde cero.

Las leyes algebraicas cambian la escala del trabajo:

$$
\text{límites básicos}
\longrightarrow
\text{operaciones algebraicas}
\longrightarrow
\text{familias completas de funciones}.
$$

A partir de

$$
\lim_{x\to a}x=a
$$

y del límite de las constantes obtenemos inmediatamente todos los límites de polinomios y, cuando el denominador no se anula en el punto límite, todos los límites de funciones racionales.

::: {.ma-block .ma-comprobacion}
**Control conceptual**

Antes de aplicar una ley de límites conviene comprobar:

1. que existen los límites de las piezas que queremos combinar;
2. que las funciones están definidas en un dominio común suficientemente cerca del punto;
3. que, para un cociente, el límite del denominador es distinto de cero;
4. que no estamos usando la conclusión de una ley como si también fuera una condición necesaria.
:::

## Conexión con continuidad

Las identidades

$$
\lim_{x\to a}p(x)=p(a)
$$

para polinomios y

$$
\lim_{x\to a}\frac{p(x)}{q(x)}
=
\frac{p(a)}{q(a)}
$$

cuando $q(a)\ne0$ anticipan una noción fundamental.

Diremos más adelante que una función es **continua en $a$** cuando

$$
\lim_{x\to a}f(x)=f(a).
$$

Las leyes algebraicas mostrarán entonces que la continuidad también se conserva bajo suma, resta, producto y cociente con denominador no nulo.

## Síntesis

Las leyes algebraicas permiten pasar de límites conocidos a nuevos límites sin reconstruir cada demostración desde la definición.

El núcleo es:

$$
\boxed{
\begin{aligned}
\lim(f+g)&=L+M,\\
\lim(f-g)&=L-M,\\
\lim(cf)&=cL,\\
\lim(fg)&=LM,\\
\lim(f^n)&=L^n,\\
\lim\frac{f}{g}&=\frac{L}{M}\quad(M\ne0).
\end{aligned}
}
$$

Pero detrás de estas fórmulas hay tres ideas analíticas que conviene conservar:

- combinar varios controles tomando el mínimo de sus radios $\delta$;
- usar la existencia de un límite para obtener **acotación local**;
- usar un límite no nulo para obtener **separación local de cero**.

Esas ideas reaparecerán en demostraciones posteriores de continuidad y análisis real.
