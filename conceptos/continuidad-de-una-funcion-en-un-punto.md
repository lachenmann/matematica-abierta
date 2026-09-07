---
title: "Continuidad de una función en un punto"
description: "Cómo formalizar la continuidad en un punto, relacionarla con el límite, tratar puntos aislados y extremos del dominio, y demostrar su estabilidad bajo operaciones algebraicas y composición."
content-id: MA-CON-0014
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
  - continuidad
  - continuidad-en-un-punto
  - epsilon-delta
  - limite-en-un-punto
  - puntos-aislados
  - extremos-del-dominio
  - discontinuidad-removible
  - extension-continua
  - composicion-de-funciones
  - operaciones-con-funciones-continuas
  - polinomios
  - funciones-racionales
prerequisites:
  - MA-CON-0008
  - MA-CON-0011
  - MA-CON-0013
related:
  - MA-CON-0007
  - MA-CON-0012
provenance:
  type: classical
  sources: []
license: GFDL-1.3-or-later
---

La noción de límite estudia qué ocurre con $f(x)$ cuando $x$ se aproxima a un punto. La **continuidad** añade una condición decisiva: el comportamiento cercano debe concordar con el valor que la función toma exactamente en ese punto.

::: {.ma-block .ma-intuicion}
**Intuición**

Una función es continua en $a$ cuando pequeños cambios de la entrada alrededor de $a$ producen pequeños cambios de la salida alrededor de $f(a)$.

La referencia ya no es un número $L$ desconocido, sino el propio valor

$$
f(a).
$$

Por eso la continuidad combina dos informaciones que en el estudio de límites estaban separadas:

- qué ocurre **cerca** de $a$;
- qué ocurre **en** $a$.
:::

## La continuidad sólo se pregunta en puntos del dominio

Sea

$$
f:D\to\mathbb R.
$$

Para preguntar si $f$ es continua en $a$ necesitamos primero que

$$
a\in D,
$$

porque la expresión $f(a)$ debe estar definida.

Esta diferencia con los límites es fundamental: en `MA-CON-0011` el punto $a$ podía quedar fuera del dominio, siempre que hubiera puntos del dominio arbitrariamente cerca de él.

::: {.ma-block .ma-error}
**Primer control**

Si $a\notin D$, no decimos que $f$ sea continua o discontinua **en $a$ como punto de su dominio**: simplemente $f(a)$ no existe.

Sí puede tener sentido estudiar

$$
\lim_{x\to a}f(x),
$$

y ese límite puede permitir construir después una extensión continua.
:::

## Definición épsilon-delta

::: {.ma-block .ma-definicion}
**Continuidad en un punto**

Sea

$$
f:D\to\mathbb R
$$

y sea $a\in D$.

Decimos que $f$ es **continua en $a$** si para todo $\varepsilon>0$ existe un $\delta>0$ tal que, para todo $x\in D$,

$$
|x-a|<\delta
\quad\Longrightarrow\quad
|f(x)-f(a)|<\varepsilon.
$$
:::

En símbolos,

$$
\boxed{
\forall\varepsilon>0\;\exists\delta>0\;\forall x\in D:
|x-a|<\delta
\Longrightarrow
|f(x)-f(a)|<\varepsilon.
}
$$

La definición debe leerse en el orden de sus cuantificadores:

1. se fija una tolerancia $\varepsilon>0$ en la salida;
2. debemos encontrar una tolerancia $\delta>0$ en la entrada;
3. esa misma $\delta$ debe funcionar para **todo** punto $x$ del dominio suficientemente cercano a $a$.

## Por qué aquí no aparece $0<|x-a|$

En la definición de límite escribíamos

$$
0<|x-a|<\delta
$$

porque el valor de la función en $a$ no debía influir en el límite.

En continuidad escribimos simplemente

$$
|x-a|<\delta.
$$

Esto incluye el caso $x=a$, pero allí la desigualdad de salida es automática:

$$
|f(a)-f(a)|=0<\varepsilon.
$$

Por tanto, también podríamos escribir la condición sólo para $x\ne a$ y obtener una formulación equivalente cuando $a$ es punto de acumulación del dominio. La forma anterior es más natural porque expresa directamente el control de $f(x)$ alrededor de $f(a)$.

## Interpretación mediante intervalos

La condición

$$
|x-a|<\delta
$$

equivale a

$$
a-\delta<x<a+\delta.
$$

Y

$$
|f(x)-f(a)|<\varepsilon
$$

equivale a

$$
f(a)-\varepsilon<f(x)<f(a)+\varepsilon.
$$

Así, la continuidad afirma que para cada intervalo vertical

$$
(f(a)-\varepsilon,f(a)+\varepsilon)
$$

podemos encontrar un intervalo horizontal alrededor de $a$ cuya parte perteneciente al dominio sea enviada completamente dentro de ese intervalo vertical.

::: {.ma-block .ma-intuicion}
**Lectura geométrica**

No se exige que toda la recta alrededor de $a$ pertenezca al dominio.

Sólo controlamos los puntos

$$
x\in D.
$$

Por eso la continuidad es siempre relativa al dominio real de la función.
:::

## Relación fundamental entre continuidad y límite

Cuando $a$ es punto de acumulación de $D$, podemos comparar directamente la definición de continuidad con la definición de límite.

::: {.ma-block .ma-definicion}
**Teorema — criterio mediante el límite**

Sea

$$
f:D\to\mathbb R,
$$

sea $a\in D$ y supongamos que $a$ es punto de acumulación de $D$.

Entonces $f$ es continua en $a$ si y sólo si

$$
\boxed{
\lim_{x\to a}f(x)=f(a).
}
$$
:::

### Demostración: continuidad implica límite

Supongamos que $f$ es continua en $a$.

Dado $\varepsilon>0$, existe $\delta>0$ tal que para todo $x\in D$,

$$
|x-a|<\delta
\quad\Longrightarrow\quad
|f(x)-f(a)|<\varepsilon.
$$

En particular, la misma implicación vale para los puntos que satisfacen además

$$
0<|x-a|<\delta.
$$

Ésta es exactamente la definición de

$$
\lim_{x\to a}f(x)=f(a).
$$

### Demostración: límite igual al valor implica continuidad

Supongamos ahora que

$$
\lim_{x\to a}f(x)=f(a).
$$

Dado $\varepsilon>0$, existe $\delta>0$ tal que

$$
0<|x-a|<\delta
\quad\Longrightarrow\quad
|f(x)-f(a)|<\varepsilon.
$$

Si $x\in D$ satisface $|x-a|<\delta$, hay dos casos.

Si $x\ne a$, aplicamos la condición del límite. Si $x=a$, entonces

$$
|f(x)-f(a)|=0<\varepsilon.
$$

Por tanto,

$$
|x-a|<\delta
\quad\Longrightarrow\quad
|f(x)-f(a)|<\varepsilon,
$$

y $f$ es continua en $a$.

## Las tres condiciones prácticas

Cuando $a$ es punto de acumulación del dominio, el criterio anterior puede descomponerse en tres preguntas:

1. ¿Está definido $f(a)$?
2. ¿Existe
   $$
   \lim_{x\to a}f(x)?
   $$
3. ¿Coinciden ambos valores?

Es decir,

$$
\boxed{
\text{continuidad en }a
\iff
\begin{cases}
f(a)\text{ existe},\\
\lim_{x\to a}f(x)\text{ existe},\\
\lim_{x\to a}f(x)=f(a).
\end{cases}
}
$$

::: {.ma-block .ma-error}
**Este criterio tiene una hipótesis**

La equivalencia anterior usa que $a$ es punto de acumulación del dominio.

Si $a$ es un punto aislado de $D$, la continuidad sigue teniendo sentido, pero el límite ordinario de `MA-CON-0011` no se define allí porque no hay puntos del dominio distintos de $a$ arbitrariamente cerca.
:::

## Puntos aislados: continuidad automática

Sea $a\in D$ un punto **aislado** del dominio. Esto significa que existe algún $r>0$ tal que

$$
D\cap(a-r,a+r)=\{a\}.
$$

::: {.ma-block .ma-definicion}
**Proposición — todo punto aislado es punto de continuidad**

Toda función

$$
f:D\to\mathbb R
$$

es continua en cada punto aislado $a\in D$.
:::

### Demostración

Sea $\varepsilon>0$.

Como $a$ es aislado, existe $r>0$ tal que el único punto de $D$ con

$$
|x-a|<r
$$

es $x=a$.

Elegimos

$$
\delta=r.
$$

Entonces, para todo $x\in D$ con $|x-a|<\delta$, necesariamente $x=a$, y por tanto

$$
|f(x)-f(a)|=0<\varepsilon.
$$

Así $f$ es continua en $a$.

::: {.ma-block .ma-observacion}
**Una consecuencia importante**

La continuidad no significa siempre que haya una curva que podamos seguir a ambos lados del punto.

Es una propiedad formulada **respecto del dominio**. En un punto aislado no existen otros puntos cercanos que puedan violar la condición, y por eso la continuidad es automática.
:::

## Ejemplo épsilon-delta: una función lineal

Consideremos

$$
f:\mathbb R\to\mathbb R,
\qquad
f(x)=3x-2.
$$

Demostremos que $f$ es continua en un punto arbitrario $a\in\mathbb R$.

Tenemos

$$
f(a)=3a-2.
$$

Queremos conseguir

$$
|f(x)-f(a)|<\varepsilon.
$$

Pero

$$
|f(x)-f(a)|
=|3x-2-(3a-2)|
=3|x-a|.
$$

Por tanto basta imponer

$$
3|x-a|<\varepsilon,
$$

o sea

$$
|x-a|<\frac{\varepsilon}{3}.
$$

Elegimos

$$
\boxed{
\delta=\frac{\varepsilon}{3}.
}
$$

Si $|x-a|<\delta$, entonces

$$
|f(x)-f(a)|
=3|x-a|
<3\delta
=\varepsilon.
$$

Así $f$ es continua en todo $a\in\mathbb R$.

## Continuidad en extremos del dominio

Consideremos

$$
r:[0,\infty)\to\mathbb R,
\qquad
r(x)=\sqrt{x}.
$$

Queremos estudiar la continuidad en $0$.

No hay puntos del dominio a la izquierda de $0$. Eso no impide la continuidad, porque la definición sólo cuantifica sobre

$$
x\in[0,\infty).
$$

Tenemos

$$
r(0)=0.
$$

Sea $\varepsilon>0$ y elijamos

$$
\delta=\varepsilon^2.
$$

Si $x\in[0,\infty)$ y

$$
|x|<\delta,
$$

entonces

$$
0\le x<\varepsilon^2,
$$

y por tanto

$$
|r(x)-r(0)|
=\sqrt{x}
<\varepsilon.
$$

Luego

$$
\boxed{
\sqrt{x}\text{ es continua en }0
\text{ como función definida en }[0,\infty).
}
$$

Esto concuerda con `MA-CON-0012`: en un extremo derecho del dominio, cuando cerca del punto sólo existen puntos del dominio por la derecha, la condición de continuidad se controla precisamente mediante ese lado.

## Qué puede fallar

En un punto de acumulación del dominio, la continuidad puede fallar de maneras distintas.

### El límite existe pero no coincide con el valor

Definamos

$$
f:\mathbb R\to\mathbb R
$$

por

$$
f(x)=
\begin{cases}
\dfrac{x^2-1}{x-1}, & x\ne1,\\
5, & x=1.
\end{cases}
$$

Para $x\ne1$,

$$
\frac{x^2-1}{x-1}=x+1.
$$

Por tanto,

$$
\lim_{x\to1}f(x)=2,
$$

pero

$$
f(1)=5.
$$

Así

$$
\boxed{
f\text{ no es continua en }1.
}
$$

La discrepancia es exactamente

$$
\lim_{x\to1}f(x)\ne f(1).
$$

### El límite no existe

Consideremos

$$
g(x)=
\begin{cases}
-1, & x<0,\\
0, & x=0,\\
1, & x>0.
\end{cases}
$$

Tenemos

$$
\lim_{x\to0^-}g(x)=-1
$$

y

$$
\lim_{x\to0^+}g(x)=1.
$$

Por `MA-CON-0012`, el límite bilateral no existe. Por tanto $g$ no puede ser continua en $0$, independientemente del valor que asignemos a $g(0)$.

::: {.ma-block .ma-observacion}
**Cambiar sólo el valor en el punto no siempre repara una discontinuidad**

Si el límite bilateral no existe, ningún valor elegido para $f(a)$ puede hacer continua la función en $a$.

En cambio, si el límite existe y es finito, una elección adecuada del valor puede producir una extensión continua.
:::

## Discontinuidad removible y extensión continua

Supongamos que una función está definida cerca de $a$ excepto quizá en $a$, y que

$$
\lim_{x\to a}f(x)=L.
$$

Definimos una nueva función $F$ asignando

$$
F(a)=L
$$

y dejando los demás valores iguales a los de $f$.

Entonces

$$
\lim_{x\to a}F(x)=L=F(a),
$$

por lo que $F$ es continua en $a$.

::: {.ma-block .ma-definicion}
**Extensión continua en un punto**

Cuando un límite finito

$$
\lim_{x\to a}f(x)=L
$$

existe y el único obstáculo para la continuidad es que $f(a)$ no está definido o tiene un valor diferente, podemos definir

$$
F(a)=L
$$

para obtener continuidad en $a$.

A este tipo de defecto se lo denomina habitualmente **discontinuidad removible**.
:::

Para

$$
f(x)=\frac{x^2-1}{x-1},
\qquad x\ne1,
$$

como

$$
\lim_{x\to1}f(x)=2,
$$

la extensión

$$
F(x)=
\begin{cases}
\dfrac{x^2-1}{x-1}, & x\ne1,\\
2, & x=1
\end{cases}
$$

es continua en $1$.

## Continuidad y operaciones algebraicas

Las leyes de límites de `MA-CON-0013` se convierten inmediatamente en leyes de continuidad.

Supongamos que $f$ y $g$ son continuas en $a$. Entonces

$$
\lim_{x\to a}f(x)=f(a)
$$

y

$$
\lim_{x\to a}g(x)=g(a).
$$

Aplicando las leyes algebraicas obtenemos los siguientes resultados.

::: {.ma-block .ma-definicion}
**Teorema — estabilidad algebraica de la continuidad**

Si $f$ y $g$ son continuas en $a$, entonces también son continuas en $a$:

$$
f+g,
\qquad
f-g,
\qquad
cf
$$

para todo $c\in\mathbb R$,

$$
fg,
$$

y

$$
f^n
$$

para todo entero $n\ge1$.

Además, si

$$
g(a)\ne0,
$$

entonces

$$
\frac{f}{g}
$$

es continua en $a$.
:::

Por ejemplo,

$$
\lim_{x\to a}(f+g)(x)
=f(a)+g(a)
=(f+g)(a),
$$

que es exactamente la continuidad de $f+g$ en $a$.

En el cociente, la condición

$$
g(a)\ne0
$$

permite aplicar la ley del cociente porque, por continuidad,

$$
\lim_{x\to a}g(x)=g(a)\ne0.
$$

## Polinomios y funciones racionales

Como las funciones constantes y la identidad

$$
x\mapsto x
$$

son continuas, las operaciones anteriores permiten construir todos los polinomios.

::: {.ma-block .ma-comprobacion}
**Todo polinomio es continuo en $\mathbb R$**

Si

$$
p(x)=a_nx^n+\cdots+a_1x+a_0,
$$

entonces para todo $c\in\mathbb R$,

$$
\lim_{x\to c}p(x)=p(c).
$$

Por tanto $p$ es continuo en todo número real.
:::

Si

$$
r(x)=\frac{p(x)}{q(x)},
$$

con $p$ y $q$ polinomios, entonces $r$ es continua en cada punto de su dominio, es decir, en todo $a$ tal que

$$
q(a)\ne0.
$$

Así, para las funciones racionales, la sustitución directa en un punto del dominio no es una regla informal: es una consecuencia de la continuidad.

## Continuidad del valor absoluto

La desigualdad triangular inversa da

$$
\big||x|-|a|\big|
\le|x-a|.
$$

Por tanto, dada $\varepsilon>0$, basta elegir

$$
\delta=\varepsilon.
$$

Si

$$
|x-a|<\delta,
$$

entonces

$$
\big||x|-|a|\big|
\le|x-a|
<\varepsilon.
$$

Luego la función

$$
x\mapsto|x|
$$

es continua en todo $a\in\mathbb R$.

Este ejemplo muestra que la continuidad puede demostrarse directamente sin calcular primero un límite separado.

## Composición de funciones continuas

La composición introducida en `MA-CON-0008` preserva continuidad.

::: {.ma-block .ma-definicion}
**Teorema — continuidad de una composición**

Sean

$$
f:D\to E
$$

y

$$
g:E\to\mathbb R.
$$

Si $f$ es continua en $a\in D$ y $g$ es continua en $f(a)\in E$, entonces

$$
\boxed{
g\circ f\text{ es continua en }a.
}
$$
:::

### Demostración

Sea $\varepsilon>0$.

Como $g$ es continua en $f(a)$, existe $\eta>0$ tal que para todo $y\in E$,

$$
|y-f(a)|<\eta
\quad\Longrightarrow\quad
|g(y)-g(f(a))|<\varepsilon.
$$

Como $f$ es continua en $a$, para esa tolerancia $\eta$ existe $\delta>0$ tal que para todo $x\in D$,

$$
|x-a|<\delta
\quad\Longrightarrow\quad
|f(x)-f(a)|<\eta.
$$

Por tanto, si $x\in D$ y $|x-a|<\delta$, entonces

$$
|g(f(x))-g(f(a))|<\varepsilon.
$$

Pero

$$
(g\circ f)(x)=g(f(x))
$$

y

$$
(g\circ f)(a)=g(f(a)).
$$

Luego

$$
|(g\circ f)(x)-(g\circ f)(a)|<\varepsilon,
$$

y $g\circ f$ es continua en $a$.

::: {.ma-block .ma-metodo}
**Estructura del argumento**

La tolerancia viaja hacia atrás:

$$
\varepsilon
\xleftarrow{\;g\;}
\eta
\xleftarrow{\;f\;}
\delta.
$$

Primero preguntamos cuánto debe aproximarse la entrada de $g$ a $f(a)$; después usamos la continuidad de $f$ para garantizar esa aproximación.
:::

## Las funciones continuas pueden pasar a través del límite

El teorema anterior tiene una versión especialmente útil para calcular límites.

Supongamos que

$$
\lim_{x\to a}f(x)=L
$$

y que $g$ es continua en $L$.

Entonces, siempre que la composición esté definida en los puntos relevantes,

$$
\boxed{
\lim_{x\to a}g(f(x))=g(L).
}
$$

La demostración repite exactamente el mecanismo

$$
\varepsilon\to\eta\to\delta.
$$

Esta propiedad explica por qué, una vez conocida la continuidad de una función exterior, podemos evaluar muchos límites mediante sustitución en su argumento.

::: {.ma-block .ma-error}
**La sustitución directa no es la definición de límite**

Es una consecuencia de teoremas de continuidad.

Cuando una función no es continua en el valor relevante, o cuando la expresión sale de su dominio, sustituir formalmente puede ser inválido o no resolver el problema.
:::

## La continuidad preserva localmente una desigualdad estricta

Supongamos que $f$ es continua en $a$ y

$$
f(a)>0.
$$

Tomemos

$$
\varepsilon=\frac{f(a)}{2}>0.
$$

Por continuidad existe $\delta>0$ tal que

$$
|x-a|<\delta
\quad\Longrightarrow\quad
|f(x)-f(a)|<\frac{f(a)}{2}.
$$

Entonces

$$
f(x)>f(a)-\frac{f(a)}{2}
=\frac{f(a)}{2}>0.
$$

Por tanto,

$$
\boxed{
f(a)>0
\Longrightarrow
f(x)>0\text{ para }x\text{ suficientemente cercano a }a.
}
$$

Análogamente, si $f(a)<0$, entonces $f(x)<0$ cerca de $a$.

En particular, si

$$
f(a)\ne0,
$$

la función permanece distinta de cero en algún entorno relativo de $a$. Esto recupera, desde continuidad, la separación local de cero utilizada en `MA-CON-0013`.

## Continuidad en un conjunto

La noción puntual se extiende de manera directa.

::: {.ma-block .ma-definicion}
**Continuidad en un conjunto**

Sea

$$
f:D\to\mathbb R.
$$

Decimos que $f$ es **continua en $D$** si es continua en cada punto

$$
a\in D.
$$
:::

Esto incluye automáticamente cualquier extremo o punto aislado que pertenezca al dominio: siempre se utiliza la geometría real de $D$, no una prolongación imaginaria fuera de él.

## Errores frecuentes

::: {.ma-block .ma-error}
**1. Olvidar que $a$ debe pertenecer al dominio**

Para continuidad necesitamos $f(a)$.
:::

::: {.ma-block .ma-error}
**2. Pensar que continuidad significa solamente que el límite existe**

También necesitamos

$$
\lim_{x\to a}f(x)=f(a).
$$
:::

::: {.ma-block .ma-error}
**3. Exigir puntos del dominio a ambos lados**

La continuidad se define respecto del dominio. En un extremo puede bastar un solo lado, y en un punto aislado es automática.
:::

::: {.ma-block .ma-error}
**4. Usar el criterio del límite en un punto aislado**

La continuidad allí se verifica directamente; el límite de `MA-CON-0011` requiere un punto de acumulación.
:::

::: {.ma-block .ma-error}
**5. Aplicar la ley del cociente cuando el denominador vale cero en el punto**

Para concluir continuidad de $f/g$ en $a$ necesitamos

$$
g(a)\ne0.
$$
:::

## Resumen estructural

Para $a\in D$, la definición fundamental es

$$
\boxed{
\forall\varepsilon>0\;\exists\delta>0:
|x-a|<\delta
\Longrightarrow
|f(x)-f(a)|<\varepsilon
\quad(x\in D).
}
$$

Si $a$ es además punto de acumulación de $D$, entonces

$$
\boxed{
f\text{ continua en }a
\iff
\lim_{x\to a}f(x)=f(a).
}
$$

Las funciones continuas son estables bajo:

$$
+,
\quad
-,
\quad
\text{multiplicación},
\quad
\text{potencias},
\quad
\text{cocientes con denominador no nulo},
\quad
\text{composición}.
$$

Además:

- todo polinomio es continuo en $\mathbb R$;
- toda función racional es continua en su dominio;
- $|x|$ es continua en $\mathbb R$;
- un punto aislado del dominio es siempre punto de continuidad;
- en un extremo del dominio se consideran sólo los puntos del dominio disponibles;
- si un límite finito existe pero falta el valor adecuado en el punto, puede construirse una extensión continua asignando ese límite.

La continuidad convierte así el lenguaje de límites en una propiedad estructural de las funciones y prepara el estudio de resultados globales sobre intervalos, así como la derivación.
