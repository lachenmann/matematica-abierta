---
title: "Límites laterales y criterio para el límite bilateral"
description: "Cómo separar la aproximación por la izquierda y por la derecha, formalizar límites laterales y decidir cuándo existe el límite bilateral."
content-id: MA-CON-0012
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
  - limites-laterales
  - limite-lateral-derecho
  - limite-lateral-izquierdo
  - limite-bilateral
  - punto-de-acumulacion-lateral
  - epsilon-delta
  - extremos-del-dominio
prerequisites:
  - MA-CON-0011
related:
  - MA-CON-0004
  - MA-CON-0005
  - MA-CON-0007
provenance:
  type: classical
  sources: []
license: GFDL-1.3-or-later
---

El límite

$$
\lim_{x\to a}f(x)
$$

estudia el comportamiento de una función en los puntos de su dominio que están cerca de $a$. Pero muchas veces conviene separar esos puntos según estén **a la izquierda** o **a la derecha** de $a$.

Esta separación conduce a los **límites laterales**.

::: {.ma-block .ma-intuicion}
**Intuición**

Acercarse a $a$ por la izquierda significa usar valores

$$
x<a,
$$

mientras que acercarse por la derecha significa usar valores

$$
x>a.
$$

Los dos procesos pueden producir el mismo comportamiento o comportamientos distintos. El límite bilateral sólo puede reunir ambos lados cuando éstos son compatibles.
:::

## Puntos de acumulación laterales

Antes de definir límites laterales debemos comprobar que realmente haya puntos del dominio acercándose desde el lado correspondiente.

Sea

$$
D\subseteq\mathbb R.
$$

::: {.ma-block .ma-definicion}
**Punto de acumulación por la derecha**

Decimos que $a\in\mathbb R$ es un **punto de acumulación de $D$ por la derecha** si para todo $\delta>0$ existe algún $x\in D$ tal que

$$
0<x-a<\delta.
$$

Equivalentemente, cada intervalo

$$
(a,a+\delta)
$$

contiene algún punto de $D$.
:::

::: {.ma-block .ma-definicion}
**Punto de acumulación por la izquierda**

Decimos que $a\in\mathbb R$ es un **punto de acumulación de $D$ por la izquierda** si para todo $\delta>0$ existe algún $x\in D$ tal que

$$
0<a-x<\delta.
$$

Equivalentemente, cada intervalo

$$
(a-\delta,a)
$$

contiene algún punto de $D$.
:::

No es necesario que $a\in D$.

Cuando $a$ es punto de acumulación de $D$ por ambos lados, diremos que hay **acumulación bilateral** en $a$.

::: {.ma-block .ma-observacion}
**Acumulación ordinaria y acumulación lateral**

Ser punto de acumulación de $D$ en el sentido de `MA-CON-0011` exige que haya puntos de $D$ distintos de $a$ arbitrariamente cerca de $a$, pero esos puntos podrían aparecer sólo por un lado.

Por ejemplo, si

$$
D=[0,\infty),
$$

entonces $0$ es punto de acumulación de $D$ y también punto de acumulación por la derecha, pero **no** por la izquierda.
:::

## Límite por la derecha

Supongamos que $a$ es punto de acumulación de $D$ por la derecha.

::: {.ma-block .ma-definicion}
**Límite lateral derecho**

Sea

$$
f:D\to\mathbb R.
$$

Decimos que

$$
\boxed{
\lim_{x\to a^+}f(x)=L
}
$$

si para todo $\varepsilon>0$ existe un $\delta>0$ tal que, para todo $x\in D$,

$$
0<x-a<\delta
\quad\Longrightarrow\quad
|f(x)-L|<\varepsilon.
$$
:::

El símbolo

$$
x\to a^+
$$

significa que $x$ se aproxima a $a$ utilizando valores **mayores que $a$**.

En términos de intervalos,

$$
0<x-a<\delta
$$

equivale a

$$
a<x<a+\delta.
$$

## Límite por la izquierda

Supongamos ahora que $a$ es punto de acumulación de $D$ por la izquierda.

::: {.ma-block .ma-definicion}
**Límite lateral izquierdo**

Decimos que

$$
\boxed{
\lim_{x\to a^-}f(x)=L
}
$$

si para todo $\varepsilon>0$ existe un $\delta>0$ tal que, para todo $x\in D$,

$$
0<a-x<\delta
\quad\Longrightarrow\quad
|f(x)-L|<\varepsilon.
$$
:::

El símbolo

$$
x\to a^-
$$

significa que $x$ se aproxima a $a$ utilizando valores **menores que $a$**.

En términos de intervalos,

$$
0<a-x<\delta
$$

equivale a

$$
a-\delta<x<a.
$$

::: {.ma-block .ma-error}
**No confundir los signos $+$ y $-$**

En

$$
x\to a^+
\qquad\text{y}\qquad
x\to a^-,
$$

los signos no describen el signo de $a$ ni el signo de $f(x)$.

Indican únicamente **desde qué lado de $a$ se aproxima la variable**.
:::

## Los límites laterales también son únicos

Siempre que el punto correspondiente sea de acumulación lateral, un límite lateral no puede tomar dos valores distintos.

La demostración es la misma que para la unicidad del límite ordinario, pero restringiendo los puntos del dominio al lado correspondiente.

Así, si existen,

$$
\lim_{x\to a^-}f(x)
$$

y

$$
\lim_{x\to a^+}f(x),
$$

cada uno determina un único número real.

## El criterio fundamental para el límite bilateral

Llegamos al resultado central.

::: {.ma-block .ma-definicion}
**Teorema — criterio mediante límites laterales**

Sea

$$
f:D\to\mathbb R,
$$

y supongamos que $a$ es punto de acumulación de $D$ **tanto por la izquierda como por la derecha**.

Entonces

$$
\boxed{
\lim_{x\to a}f(x)=L
}
$$

si y sólo si

$$
\boxed{
\lim_{x\to a^-}f(x)=L
\qquad\text{y}\qquad
\lim_{x\to a^+}f(x)=L.
}
$$
:::

En palabras: cuando ambos lados están disponibles, el límite bilateral existe exactamente cuando los dos límites laterales existen y son iguales.

### Demostración: del límite bilateral a los laterales

Supongamos que

$$
\lim_{x\to a}f(x)=L.
$$

Dado $\varepsilon>0$, existe $\delta>0$ tal que

$$
0<|x-a|<\delta
\quad\Longrightarrow\quad
|f(x)-L|<\varepsilon.
$$

Si además $x>a$, entonces

$$
0<x-a<\delta,
$$

de modo que la misma elección de $\delta$ demuestra

$$
\lim_{x\to a^+}f(x)=L.
$$

Análogamente, si $x<a$, entonces

$$
0<a-x<\delta,
$$

y obtenemos

$$
\lim_{x\to a^-}f(x)=L.
$$

Por tanto, el límite bilateral fuerza a ambos límites laterales a coincidir con $L$.

### Demostración: de los laterales al bilateral

Supongamos ahora que

$$
\lim_{x\to a^-}f(x)=L
$$

y

$$
\lim_{x\to a^+}f(x)=L.
$$

Sea $\varepsilon>0$.

Por el límite izquierdo existe $\delta_->0$ tal que

$$
0<a-x<\delta_-
\quad\Longrightarrow\quad
|f(x)-L|<\varepsilon.
$$

Por el límite derecho existe $\delta_+>0$ tal que

$$
0<x-a<\delta_+
\quad\Longrightarrow\quad
|f(x)-L|<\varepsilon.
$$

Elegimos

$$
\boxed{
\delta=\min\{\delta_-,\delta_+\}.
}
$$

Sea ahora $x\in D$ tal que

$$
0<|x-a|<\delta.
$$

Como $x\ne a$, necesariamente ocurre una de dos cosas:

$$
x<a
$$

o

$$
x>a.
$$

Si $x<a$, entonces

$$
0<a-x<\delta\le\delta_-,
$$

y por tanto

$$
|f(x)-L|<\varepsilon.
$$

Si $x>a$, entonces

$$
0<x-a<\delta\le\delta_+,
$$

y nuevamente

$$
|f(x)-L|<\varepsilon.
$$

En ambos casos se cumple la condición épsilon-delta del límite bilateral. Luego

$$
\lim_{x\to a}f(x)=L.
$$

## Consecuencia inmediata: límites laterales distintos

Del teorema obtenemos un criterio muy útil de inexistencia.

::: {.ma-block .ma-comprobacion}
**Criterio de no existencia**

Si $a$ es punto de acumulación por ambos lados y existen los límites laterales, pero

$$
\lim_{x\to a^-}f(x)
\ne
\lim_{x\to a^+}f(x),
$$

entonces

$$
\boxed{
\lim_{x\to a}f(x)
\text{ no existe}.
}
$$
:::

No hace falta buscar otro candidato: la incompatibilidad entre ambos lados impide cualquier límite bilateral.

## Ejemplo: los dos lados coinciden aunque el valor en el punto sea distinto

Definamos

$$
f:\mathbb R\to\mathbb R
$$

por

$$
f(x)=
\begin{cases}
x+2, & x<1,\\
100, & x=1,\\
4-x, & x>1.
\end{cases}
$$

Por la izquierda,

$$
\lim_{x\to1^-}f(x)
=
\lim_{x\to1^-}(x+2)
=3.
$$

De hecho,

$$
|f(x)-3|
=|x+2-3|
=|x-1|,
$$

por lo que basta elegir

$$
\delta=\varepsilon.
$$

Por la derecha,

$$
\lim_{x\to1^+}f(x)
=
\lim_{x\to1^+}(4-x)
=3,
$$

y nuevamente

$$
|f(x)-3|
=|4-x-3|
=|1-x|
=|x-1|.
$$

Por el criterio bilateral,

$$
\boxed{
\lim_{x\to1}f(x)=3.
}
$$

Sin embargo,

$$
f(1)=100.
$$

El ejemplo refuerza una idea ya establecida en `MA-CON-0011`: el límite depende del comportamiento **cerca del punto**, no del valor asignado exactamente en él.

## Ejemplo: los dos lados son incompatibles

Consideremos

$$
s:\mathbb R\setminus\{0\}\to\mathbb R,
\qquad
s(x)=\frac{|x|}{x}.
$$

Si $x<0$, entonces

$$
|x|=-x,
$$

y por tanto

$$
s(x)=-1.
$$

Así,

$$
\lim_{x\to0^-}\frac{|x|}{x}=-1.
$$

Si $x>0$, entonces

$$
|x|=x,
$$

y por tanto

$$
s(x)=1.
$$

Así,

$$
\lim_{x\to0^+}\frac{|x|}{x}=1.
$$

Como

$$
-1\ne1,
$$

concluimos inmediatamente que

$$
\boxed{
\lim_{x\to0}\frac{|x|}{x}
\text{ no existe}.
}
$$

## Qué ocurre en un extremo del dominio

Los extremos de un dominio muestran por qué conviene distinguir cuidadosamente entre límite ordinario y límites laterales.

Consideremos

$$
r:[0,\infty)\to\mathbb R,
\qquad
r(x)=\sqrt{x}.
$$

El punto $0$ es de acumulación por la derecha, pero no por la izquierda.

Podemos demostrar que

$$
\boxed{
\lim_{x\to0^+}\sqrt{x}=0.
}
$$

Sea $\varepsilon>0$ y elijamos

$$
\delta=\varepsilon^2.
$$

Si

$$
0<x<\delta,
$$

entonces

$$
0<\sqrt{x}<\sqrt{\delta}=\varepsilon.
$$

Por tanto,

$$
|\sqrt{x}-0|<\varepsilon.
$$

No definimos aquí un límite lateral izquierdo en $0$, porque $0$ no es punto de acumulación del dominio por la izquierda.

::: {.ma-block .ma-observacion}
**Límite relativo al dominio**

Con la definición de `MA-CON-0011`, el límite

$$
\lim_{x\to0}\sqrt{x}=0
$$

también es correcto para la función cuyo dominio es $[0,\infty)$: todos los puntos del dominio suficientemente próximos a $0$ están necesariamente a la derecha.

Por eso, el teorema que identifica un límite bilateral con dos límites laterales iguales exige explícitamente que haya acumulación **por ambos lados**. En un extremo del dominio, ese supuesto no se cumple y el teorema simplemente no se aplica.
:::

## Una distinción importante

Hay dos situaciones diferentes que no conviene mezclar:

1. **un lado no está disponible en el dominio**;
2. **ambos lados están disponibles, pero producen límites diferentes**.

En el primer caso, como ocurre con $\sqrt{x}$ en $0$, el dominio sólo permite aproximación por un lado.

En el segundo, como ocurre con $|x|/x$ en $0$, ambos lados existen geométricamente pero son incompatibles, y eso destruye el límite bilateral.

## Procedimiento práctico

::: {.ma-block .ma-metodo}
**Cómo analizar un límite mediante sus lados**

1. Identifica el dominio de la función cerca de $a$.
2. Comprueba si $a$ es punto de acumulación por la izquierda, por la derecha o por ambos lados.
3. Si corresponde, estudia
   $$
   \lim_{x\to a^-}f(x)
   \qquad\text{y}\qquad
   \lim_{x\to a^+}f(x).
   $$
4. Si ambos lados están disponibles y dan el mismo valor $L$, concluye
   $$
   \lim_{x\to a}f(x)=L.
   $$
5. Si ambos límites laterales existen pero son distintos, el límite bilateral no existe.
6. En extremos del dominio, utiliza el límite lateral correspondiente y controla explícitamente qué noción de límite estás usando.
:::

## Comprobación conceptual

Antes de usar el criterio bilateral, conviene verificar siempre sus hipótesis:

$$
\boxed{
\text{acumulación por la izquierda}
+
\text{acumulación por la derecha}
}
$$

Sólo entonces tiene sentido exigir simultáneamente

$$
\lim_{x\to a^-}f(x)=L
$$

y

$$
\lim_{x\to a^+}f(x)=L
$$

como condición equivalente al límite bilateral.

La estructura conceptual queda así:

$$
\boxed{
\text{aproximación izquierda}
+
\text{aproximación derecha}
\longrightarrow
\text{compatibilidad lateral}
\longrightarrow
\text{límite bilateral}
}
$$

## Relaciones

- **Prerrequisito:** [Límite de una función en un punto](limite-de-una-funcion-en-un-punto.md) (`MA-CON-0011`).
- **Contenidos relacionados:** [Intervalos e intersección de conjuntos reales](intervalos-e-interseccion-de-conjuntos-reales.md) (`MA-CON-0004`); [Propiedades del orden en ℝ y manipulación de desigualdades](propiedades-del-orden-en-r-y-manipulacion-de-desigualdades.md) (`MA-CON-0005`); [Funciones reales: dominio, codominio, imagen y preimagen](funciones-reales-dominio-codominio-imagen-y-preimagen.md) (`MA-CON-0007`).
- **Siguiente paso natural:** leyes algebraicas de los límites y técnicas para calcular límites a partir de límites conocidos.
