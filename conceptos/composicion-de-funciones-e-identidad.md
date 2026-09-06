---
title: "Composición de funciones e identidad"
description: "Cómo componer funciones, controlar el dominio de una composición y entender el papel de la función identidad y la asociatividad."
content-id: MA-CON-0008
content-type: concept
status: published
date-created: 2026-09-06
date-modified: 2026-09-06
areas:
  - fundamentos
  - algebra
  - calculo
level: fundamental
topics:
  - funciones
  - composicion-de-funciones
  - funcion-identidad
  - dominio-de-funciones
  - asociatividad
  - imagen
  - preimagen
prerequisites:
  - MA-CON-0007
related:
  - MA-CON-0003
  - MA-CON-0004
  - MA-CON-0006
provenance:
  type: classical
  sources: []
license: GFDL-1.3-or-later
---

Una función puede utilizar como entrada la salida producida por otra función. Esta operación se llama **composición** y es una de las estructuras fundamentales de la teoría de funciones.

Si una función transforma

$$
x\longmapsto f(x)
$$

y una segunda función transforma

$$
y\longmapsto g(y),
$$

podemos aplicar primero $f$ y después $g$:

$$
x
\longmapsto
f(x)
\longmapsto
g(f(x)).
$$

La función resultante se denota

$$
g\circ f.
$$

::: {.ma-block .ma-intuicion}
**Intuición**

En la composición $g\circ f$, la función que está más cerca de la variable actúa primero:

$$
(g\circ f)(x)=g(f(x)).
$$

Por eso $g\circ f$ se lee como «$g$ después de $f$».
:::

## Definición de composición

Sean

$$
f:A\to B
$$

y

$$
g:B\to C.
$$

La **composición de $g$ con $f$** es la función

$$
g\circ f:A\to C
$$

definida por

$$
\boxed{(g\circ f)(x)=g(f(x))}.
$$

La estructura de conjuntos es importante:

$$
A\xrightarrow{\ f\ }B\xrightarrow{\ g\ }C.
$$

La salida de $f$ pertenece a $B$, y $B$ es precisamente el conjunto desde el que $g$ acepta entradas.

::: {.ma-block .ma-definicion}
**Definición**

Si $f:A\to B$ y $g:B\to C$, entonces

$$
g\circ f:A\to C,
\qquad
(g\circ f)(x)=g(f(x)).
$$
:::

## Un primer ejemplo

Sean

$$
f(x)=x+1
$$

y

$$
g(x)=x^2.
$$

Entonces

$$
(g\circ f)(x)
=
g(f(x))
=
g(x+1)
=(x+1)^2.
$$

Por tanto,

$$
\boxed{(g\circ f)(x)=(x+1)^2}.
$$

La operación se realiza en dos pasos:

$$
x
\xrightarrow{\ f\ }
x+1
\xrightarrow{\ g\ }(x+1)^2.
$$

## El orden de composición importa

Con las mismas funciones,

$$
(f\circ g)(x)
=
f(g(x))
=
f(x^2)
=x^2+1.
$$

Así,

$$
(g\circ f)(x)=(x+1)^2
$$

pero

$$
(f\circ g)(x)=x^2+1.
$$

En general,

$$
\boxed{g\circ f\ne f\circ g}.
$$

::: {.ma-block .ma-error}
**Error frecuente**

La composición de funciones **no es conmutativa** en general.

No se puede intercambiar el orden de $f$ y $g$ sin comprobar qué ocurre con las funciones concretas.
:::

## La composición debe estar bien definida

La escritura

$$
g(f(x))
$$

sólo tiene sentido si $f(x)$ es una entrada permitida para $g$.

En la situación

$$
f:A\to B,
\qquad
g:B\to C,
$$

esto está garantizado porque

$$
f(x)\in B
$$

para todo $x\in A$.

Más generalmente, si

$$
f:A\to B
$$

y $g$ está definida sobre un conjunto $D_g$, basta que

$$
f(A)\subseteq D_g.
$$

Es decir: **toda salida de $f$ que vayamos a utilizar debe pertenecer al dominio de $g$**.

## Dominio de una composición dada por fórmulas

En cálculo es frecuente que las funciones aparezcan simplemente mediante fórmulas. En ese contexto hay que reconstruir cuidadosamente el dominio de la composición.

La regla general es

$$
\boxed{
D_{g\circ f}
=
\{x\in D_f:f(x)\in D_g\}
}.
$$

Esto impone dos condiciones simultáneas:

1. $x$ debe pertenecer al dominio de $f$;
2. la salida $f(x)$ debe pertenecer al dominio de $g$.

::: {.ma-block .ma-dominio}
**Dominio**

Para determinar el dominio de $g\circ f$, no basta con simplificar la fórmula final. Debemos conservar las restricciones que aparecen durante el proceso

$$
x\longmapsto f(x)\longmapsto g(f(x)).
$$
:::

## Ejemplo: una raíz en la función exterior

Sean

$$
f(x)=x-1
$$

y

$$
g(x)=\sqrt{x}.
$$

Tenemos

$$
(g\circ f)(x)
=
\sqrt{x-1}.
$$

Como $g$ sólo acepta entradas no negativas, necesitamos

$$
f(x)=x-1\ge0.
$$

Por tanto,

$$
x\ge1
$$

y

$$
\boxed{D_{g\circ f}=[1,\infty)}.
$$

En cambio,

$$
(f\circ g)(x)
=
\sqrt{x}-1,
$$

cuyo dominio es

$$
\boxed{D_{f\circ g}=[0,\infty)}.
$$

Esto muestra que cambiar el orden puede cambiar **tanto la fórmula como el dominio**.

## Ejemplo: una restricción que desaparece en la fórmula simplificada

Consideremos

$$
f(x)=\sqrt{x}
$$

y

$$
g(x)=x^2.
$$

Entonces

$$
(g\circ f)(x)
=
(\sqrt{x})^2
=
x.
$$

Sería incorrecto concluir que el dominio es todo $\mathbb R$ sólo porque la fórmula final es $x$.

La composición comienza aplicando $f(x)=\sqrt{x}$, de modo que necesariamente

$$
x\ge0.
$$

Por tanto,

$$
\boxed{D_{g\circ f}=[0,\infty)}.
$$

La función compuesta coincide con la fórmula $x$ **sólo sobre ese dominio**.

::: {.ma-block .ma-error}
**Error frecuente**

Simplificar una expresión puede ocultar restricciones de dominio.

La igualdad

$$
(\sqrt{x})^2=x
$$

es válida para los valores de $x$ para los que $\sqrt{x}$ está definida como número real, es decir, para $x\ge0$.
:::

## La función identidad

Para cualquier conjunto $A$, definimos la **función identidad sobre $A$** por

$$
\operatorname{id}_A:A\to A,
$$

$$
\operatorname{id}_A(x)=x.
$$

La identidad deja cada elemento exactamente donde estaba:

$$
x\xrightarrow{\operatorname{id}_A}x.
$$

Si

$$
f:A\to B,
$$

entonces podemos componer con las identidades correspondientes:

$$
\operatorname{id}_B\circ f:A\to B
$$

y

$$
f\circ\operatorname{id}_A:A\to B.
$$

Para cada $x\in A$,

$$
(\operatorname{id}_B\circ f)(x)
=
\operatorname{id}_B(f(x))
=
f(x),
$$

y también

$$
(f\circ\operatorname{id}_A)(x)
=
f(\operatorname{id}_A(x))
=
f(x).
$$

Por tanto,

$$
\boxed{
\operatorname{id}_B\circ f
=
f
=
f\circ\operatorname{id}_A
}.
$$

::: {.ma-block .ma-intuicion}
**Intuición**

La función identidad desempeña para la composición un papel análogo al del número $1$ en la multiplicación:

$$
1\cdot a=a=a\cdot1.
$$

No cambia el objeto sobre el que actúa.
:::

## Asociatividad de la composición

Sean

$$
f:A\to B,
\qquad
g:B\to C,
\qquad h:C\to D.
$$

Podemos formar

$$
h\circ(g\circ f)
$$

o bien

$$
(h\circ g)\circ f.
$$

Para cada $x\in A$,

$$
\bigl(h\circ(g\circ f)\bigr)(x)
=
h((g\circ f)(x))
=
h(g(f(x))),
$$

mientras que

$$
\bigl((h\circ g)\circ f\bigr)(x)
=
(h\circ g)(f(x))
=
h(g(f(x))).
$$

Por tanto,

$$
\boxed{
h\circ(g\circ f)
=
(h\circ g)\circ f
}.
$$

La composición de funciones es **asociativa**.

Gracias a esto podemos escribir sin ambigüedad

$$
h\circ g\circ f.
$$

::: {.ma-block .ma-observacion}
**Observación**

La composición es asociativa, pero no conmutativa:

$$
h\circ(g\circ f)=(h\circ g)\circ f,
$$

mientras que, en general,

$$
g\circ f\ne f\circ g.
$$

Son propiedades completamente distintas.
:::

## Composición e imágenes

Si

$$
f:A\to B
$$

y

$$
g:B\to C,
$$

entonces la imagen de un subconjunto $S\subseteq A$ bajo la composición puede obtenerse por etapas:

$$
(g\circ f)(S)=g(f(S)).
$$

Primero calculamos la imagen de $S$ mediante $f$ y después la imagen del resultado mediante $g$.

Esto refleja exactamente el proceso

$$
S
\xrightarrow{\ f\ }
f(S)
\xrightarrow{\ g\ }g(f(S)).
$$

## Composición y preimágenes

Sea $T\subseteq C$. Entonces

$$
(g\circ f)^{-1}(T)
=
f^{-1}(g^{-1}(T)).
$$

La lectura conceptual es inversa al recorrido de las imágenes:

1. buscamos primero qué elementos de $B$ llegan a $T$ mediante $g$;
2. luego buscamos qué elementos de $A$ llegan a ese conjunto mediante $f$.

Por eso aparece el orden

$$
T
\xrightarrow{\ g^{-1}\ }
g^{-1}(T)
\xrightarrow{\ f^{-1}\ }
f^{-1}(g^{-1}(T)).
$$

::: {.ma-block .ma-error}
**Notación importante**

En esta fórmula, $f^{-1}(S)$ y $g^{-1}(T)$ significan **preimagen de un conjunto**. No estamos suponiendo que $f$ o $g$ posean funciones inversas.
:::

## Una composición puede revelar estructura

Consideremos

$$
f(x)=2x+3
$$

y

$$
g(x)=\frac{x-3}{2}.
$$

Entonces

$$
(g\circ f)(x)
=
\frac{(2x+3)-3}{2}
=x,
$$

y

$$
(f\circ g)(x)
=
2\left(\frac{x-3}{2}\right)+3
=x.
$$

Así,

$$
g\circ f=\operatorname{id}_{\mathbb R}
$$

y

$$
f\circ g=\operatorname{id}_{\mathbb R}.
$$

Este fenómeno anticipa la noción de **función inversa**: dos funciones son inversas cuando sus composiciones, en los dominios y codominios adecuados, producen las funciones identidad correspondientes.

Todavía no necesitamos formalizar esa teoría; lo importante aquí es reconocer que la composición permite expresar con precisión la idea de «deshacer» una transformación.

## Procedimiento práctico

Para calcular una composición $g\circ f$:

1. identifica claramente $f$ y $g$;
2. escribe
   $$
   (g\circ f)(x)=g(f(x));
   $$
3. calcula primero $f(x)$;
4. sustituye esa salida como entrada de $g$;
5. simplifica la expresión cuando sea conveniente;
6. determina el dominio conservando todas las restricciones de $f$ y de $g$;
7. si comparas con $f\circ g$, repite el proceso desde cero: no supongas que las dos composiciones coinciden.

::: {.ma-block .ma-metodo}
**Método**

Cuando haya restricciones de dominio, piensa siempre en la cadena

$$
x
\xrightarrow{\ f\ }
f(x)
\xrightarrow{\ g\ }g(f(x)).
$$

Pregunta en cada etapa: **¿esta entrada está permitida?**
:::

## Resumen estructural

Si

$$
f:A\to B,
\qquad
g:B\to C,
$$

entonces

$$
g\circ f:A\to C,
\qquad
(g\circ f)(x)=g(f(x)).
$$

Las propiedades fundamentales son:

$$
\boxed{g\circ f\ne f\circ g\quad\text{en general}},
$$

$$
\boxed{h\circ(g\circ f)=(h\circ g)\circ f},
$$

$$
\boxed{\operatorname{id}_B\circ f=f=f\circ\operatorname{id}_A}.
$$

Para funciones dadas mediante fórmulas,

$$
\boxed{
D_{g\circ f}
=
\{x\in D_f:f(x)\in D_g\}
}.
$$

La composición convierte así a las funciones en objetos que pueden encadenarse de manera controlada, y prepara directamente el camino hacia inyectividad, sobreyectividad, biyectividad y funciones inversas.

## Relaciones

- **Prerrequisitos:** [Funciones reales: dominio, codominio, imagen y preimagen](funciones-reales-dominio-codominio-imagen-y-preimagen.md) (`MA-CON-0007`).
- **Contenidos relacionados:** [Dominio de funciones reales con radicales](dominio-de-funciones-reales-con-radicales.md) (`MA-CON-0003`), [Intervalos e intersección de conjuntos reales](intervalos-e-interseccion-de-conjuntos-reales.md) (`MA-CON-0004`) y [Operaciones con conjuntos reales](operaciones-con-conjuntos-reales.md) (`MA-CON-0006`).
- **Siguiente desarrollo natural:** inyectividad, sobreyectividad, biyectividad y funciones inversas.
