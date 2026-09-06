---
title: "Funciones reales: dominio, codominio, imagen y preimagen"
description: "Qué es una función real, cómo distinguir dominio, codominio e imagen, y cómo trabajar con imágenes y preimágenes de conjuntos."
content-id: MA-CON-0007
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
  - dominio-de-funciones
  - codominio
  - imagen
  - preimagen
  - conjuntos
  - grafica-de-funciones
prerequisites:
  - MA-CON-0004
  - MA-CON-0006
related:
  - MA-CON-0003
  - MA-PRB-0001
  - MA-PRB-0002
provenance:
  type: classical
  sources: []
license: GFDL-1.3-or-later
---

Una de las ideas centrales de toda la matemática moderna es la de **función**. En cálculo, álgebra, análisis, probabilidad y muchas otras áreas, una función permite describir cómo un dato de entrada determina un dato de salida.

Pero para trabajar con precisión necesitamos distinguir varias nociones que a menudo se confunden:

- la **regla de asignación**;
- el **dominio**;
- el **codominio**;
- la **imagen**;
- la **preimagen**.

::: {.ma-block .ma-intuicion}
**Intuición**

Una función no es solamente una fórmula. Es una asignación que parte de un conjunto determinado y llega a otro conjunto determinado.

La expresión

$$
x^2
$$

por sí sola no especifica todavía toda la información de una función.
:::

## Definición de función

Sean $A$ y $B$ conjuntos. Una **función**

$$
f:A\to B
$$

es una regla que asigna a **cada** elemento $x\in A$ un **único** elemento de $B$, que denotamos por

$$
f(x).
$$

El conjunto $A$ se llama **dominio** de $f$ y el conjunto $B$ se llama **codominio**.

La condición decisiva es la unicidad:

$$
\boxed{
\text{cada entrada del dominio tiene exactamente una salida}
}
$$

Puede ocurrir que dos entradas distintas tengan la misma salida. Lo que no puede ocurrir es que una misma entrada tenga dos salidas diferentes.

### Ejemplo

Consideremos

$$
f:\mathbb R\to\mathbb R,
\qquad
f(x)=x^2.
$$

Entonces

$$
f(2)=4,
\qquad
f(-2)=4.
$$

No hay ningún problema en que

$$
f(2)=f(-2).
$$

La definición de función no exige que entradas distintas produzcan salidas distintas.

## Dominio y codominio

En

$$
f:A\to B,
$$

el **dominio** es el conjunto de entradas permitidas:

$$
\operatorname{Dom}(f)=A.
$$

El **codominio** es el conjunto que se declara como espacio de llegada:

$$
B.
$$

Estos conjuntos forman parte de la definición de la función.

::: {.ma-block .ma-error}
**Error frecuente**

No debemos identificar automáticamente una función con la expresión que aparece a la derecha de $f(x)=$.

Por ejemplo,

$$
f:\mathbb R\to\mathbb R,
\qquad f(x)=x^2,
$$

y

$$
g:[0,\infty)\to[0,\infty),
\qquad g(x)=x^2,
$$

usan la misma fórmula, pero no tienen el mismo dominio ni el mismo codominio. Por tanto, son funciones diferentes.
:::

## Imagen de una función

La **imagen** de $f:A\to B$ es el conjunto de valores que la función alcanza realmente:

$$
f(A)
=
\{f(x):x\in A\}.
$$

También puede escribirse

$$
\operatorname{Im}(f)
=
\{y\in B:\text{existe }x\in A\text{ tal que }f(x)=y\}.
$$

Siempre se cumple

$$
\operatorname{Im}(f)\subseteq B.
$$

La inclusión puede ser estricta.

### Ejemplo: imagen distinta del codominio

Para

$$
f:\mathbb R\to\mathbb R,
\qquad
f(x)=x^2,
$$

ningún número negativo puede ser salida de la función. Por tanto,

$$
\operatorname{Im}(f)=[0,\infty).
$$

El codominio, sin embargo, sigue siendo

$$
\mathbb R.
$$

Así,

$$
[0,\infty)\subsetneq\mathbb R.
$$

::: {.ma-block .ma-definicion}
**Codominio e imagen no son sinónimos**

- **Codominio:** conjunto de llegada especificado al definir la función.
- **Imagen:** valores del codominio que la función alcanza efectivamente.
:::

## Imagen de un subconjunto

No sólo podemos considerar la imagen de todo el dominio. Si

$$
S\subseteq A,
$$

definimos la **imagen de $S$** mediante

$$
f(S)
=
\{f(x):x\in S\}.
$$

Por ejemplo, para

$$
f(x)=x^2
$$

y

$$
S=[-2,1],
$$

tenemos

$$
f(S)=[0,4].
$$

Obsérvese que no basta con elevar solamente los extremos al cuadrado y conservar su orden. Debemos pensar qué valores toma la función en **todo** el conjunto.

## Preimagen de un conjunto

Sea

$$
f:A\to B
$$

y sea

$$
C\subseteq B.
$$

La **preimagen** de $C$ es el conjunto de entradas cuya salida pertenece a $C$:

$$
f^{-1}(C)
=
\{x\in A:f(x)\in C\}.
$$

La preimagen es, por tanto, un subconjunto del dominio:

$$
f^{-1}(C)\subseteq A.
$$

::: {.ma-block .ma-intuicion}
**Intuición**

La imagen pregunta:

> ¿adónde llegan estos puntos?

La preimagen pregunta:

> ¿qué puntos del dominio llegan a este conjunto?
:::

### Ejemplo

Tomemos nuevamente

$$
f:\mathbb R\to\mathbb R,
\qquad
f(x)=x^2,
$$

y consideremos

$$
C=[1,4].
$$

Buscamos los números reales tales que

$$
1\le x^2\le4.
$$

Esto ocurre exactamente cuando

$$
1\le |x|\le2.
$$

Por tanto,

$$
\boxed{
f^{-1}([1,4])=[-2,-1]\cup[1,2]
}.
$$

Aquí aparecen naturalmente las operaciones con intervalos y conjuntos estudiadas anteriormente.

## La notación $f^{-1}$ no implica necesariamente función inversa

La expresión

$$
f^{-1}(C)
$$

para la preimagen de un conjunto está definida para **cualquier función** $f:A\to B$ y cualquier conjunto $C\subseteq B$.

Esto no significa que exista una función inversa

$$
f^{-1}:B\to A.
$$

Por ejemplo,

$$
f(x)=x^2
$$

sobre todo $\mathbb R$ no tiene una función inversa global $\mathbb R\to\mathbb R$, porque

$$
f(2)=f(-2).
$$

Sin embargo, la preimagen

$$
f^{-1}(C)
$$

de cualquier conjunto $C\subseteq\mathbb R$ sigue teniendo sentido.

::: {.ma-block .ma-error}
**Error frecuente**

No confundas

$$
f^{-1}(C)
$$

con

$$
\frac{1}{f(C)}.
$$

El símbolo $^{-1}$ en la notación de preimagen no significa «tomar el recíproco».
:::

## Preimagen de un punto

Si $y\in B$, podemos considerar el conjunto de todas las entradas que producen ese valor:

$$
f^{-1}(\{y\})
=
\{x\in A:f(x)=y\}.
$$

Para

$$
f(x)=x^2,
$$

tenemos

$$
f^{-1}(\{4\})=\{-2,2\},
$$

mientras que

$$
f^{-1}(\{-1\})=\varnothing.
$$

Esto muestra otra vez que una salida puede tener varias preimágenes o ninguna.

## Gráfica de una función

La **gráfica** de una función $f:A\to B$ es el conjunto de pares ordenados

$$
\operatorname{Gr}(f)
=
\{(x,f(x)):x\in A\}.
$$

Si $A$ y $B$ son subconjuntos de $\mathbb R$, podemos representar esos pares como puntos del plano cartesiano.

La condición de unicidad de una función significa que para cada $x\in A$ existe exactamente un punto de la gráfica cuya primera coordenada es $x$.

Geométricamente, esto está relacionado con el conocido **criterio de la recta vertical**: una recta vertical no puede cortar la gráfica de una función real en dos puntos diferentes.

## Una fórmula y su dominio natural

En muchos ejercicios se da solamente una expresión como

$$
f(x)=\frac{\sqrt{2-x}}{x-1}
$$

y se pregunta por su dominio real.

En este contexto se entiende normalmente que buscamos el **dominio real máximo** para el cual la expresión está definida.

Tenemos dos restricciones:

1. la raíz cuadrada exige

$$
2-x\ge0,
$$

es decir,

$$
x\le2;
$$

2. el denominador exige

$$
x-1\ne0,
$$

es decir,

$$
x\ne1.
$$

Por tanto,

$$
\operatorname{Dom}(f)
=
(-\infty,2]\setminus\{1\}
$$

y, equivalentemente,

$$
\boxed{
\operatorname{Dom}(f)=(-\infty,1)\cup(1,2]
}.
$$

::: {.ma-block .ma-dominio}
**Dominio**

Determinar el dominio de una expresión consiste en identificar todas las condiciones necesarias para que la salida tenga sentido y combinar después esas condiciones mediante operaciones de conjuntos.
:::

## La misma fórmula puede dar funciones distintas

Consideremos

$$
f:\mathbb R\to\mathbb R,
\qquad
f(x)=x^2,
$$

y

$$
g:\mathbb R\to[0,\infty),
\qquad
g(x)=x^2.
$$

Ambas tienen el mismo dominio y la misma regla, pero distinto codominio.

Además,

$$
\operatorname{Im}(f)=\operatorname{Im}(g)=[0,\infty).
$$

Para $g$, la imagen coincide con el codominio. Para $f$, no.

Esto muestra por qué el codominio no es información decorativa: forma parte de la estructura de la función.

## Cómo interactúan las funciones con unión e intersección

Sean $S,T\subseteq A$. Para las imágenes se cumple siempre

$$
f(S\cup T)=f(S)\cup f(T).
$$

Para la intersección sólo podemos garantizar

$$
f(S\cap T)\subseteq f(S)\cap f(T).
$$

La igualdad puede fallar porque dos entradas diferentes pueden producir la misma salida.

### Ejemplo de inclusión estricta

Sea

$$
f(x)=x^2,
$$

con

$$
S=\{-1\},
\qquad
T=\{1\}.
$$

Entonces

$$
S\cap T=\varnothing,
$$

de modo que

$$
f(S\cap T)=\varnothing.
$$

Pero

$$
f(S)=f(T)=\{1\},
$$

y por tanto

$$
f(S)\cap f(T)=\{1\}.
$$

Así,

$$
f(S\cap T)\subsetneq f(S)\cap f(T).
$$

## Las preimágenes preservan las operaciones de conjuntos

Las preimágenes tienen un comportamiento especialmente limpio. Si $C,D\subseteq B$, entonces

$$
f^{-1}(C\cup D)
=
f^{-1}(C)\cup f^{-1}(D),
$$

$$
f^{-1}(C\cap D)
=
f^{-1}(C)\cap f^{-1}(D).
$$

Además, tomando complementos respecto del codominio $B$ y del dominio $A$,

$$
f^{-1}(B\setminus C)
=
A\setminus f^{-1}(C).
$$

Estas identidades no son coincidencias: traducen directamente las palabras lógicas «o», «y» y «no».

Por ejemplo,

$$
x\in f^{-1}(C\cap D)
$$

significa

$$
f(x)\in C\cap D,
$$

es decir,

$$
f(x)\in C
\quad\text{y}\quad
f(x)\in D.
$$

Por tanto,

$$
x\in f^{-1}(C)
\quad\text{y}\quad
x\in f^{-1}(D),
$$

que equivale a

$$
x\in f^{-1}(C)\cap f^{-1}(D).
$$

## Resumen operativo

Para una función

$$
f:A\to B,
$$

conviene separar siempre cuatro preguntas:

1. **Dominio:** ¿qué entradas están permitidas?
2. **Codominio:** ¿qué conjunto se declara como espacio de llegada?
3. **Imagen:** ¿qué valores alcanza realmente la función?
4. **Preimagen:** ¿qué entradas llevan a un conjunto dado del codominio?

En símbolos:

$$
\operatorname{Dom}(f)=A,
$$

$$
\operatorname{Im}(f)=f(A)\subseteq B,
$$

$$
f^{-1}(C)=\{x\in A:f(x)\in C\}.
$$

::: {.ma-block .ma-comprobacion}
**Comprobación**

Cuando trabajes con una función, verifica siempre:

- que cada entrada del dominio tenga una única salida;
- que los valores obtenidos pertenezcan al codominio declarado;
- que no confundas codominio con imagen;
- que una preimagen es un conjunto de entradas;
- que las restricciones de una fórmula se traduzcan finalmente en un conjunto bien definido.
:::

## Conexiones

Este concepto utiliza directamente:

- [Intervalos e intersección de conjuntos reales](intervalos-e-interseccion-de-conjuntos-reales.md) (`MA-CON-0004`);
- [Operaciones con conjuntos reales](operaciones-con-conjuntos-reales.md) (`MA-CON-0006`).

Se conecta especialmente con:

- [Dominio de funciones reales con radicales](dominio-de-funciones-reales-con-radicales.md) (`MA-CON-0003`);
- [Dominio de una función radical cuadrática](../problemas/dominio-funcion-radical-cuadratica.md) (`MA-PRB-0001`);
- [Dominio de un radical anidado](../problemas/dominio-de-un-radical-anidado.md) (`MA-PRB-0002`).

La distinción entre dominio, imagen y preimagen será fundamental más adelante para estudiar composición, funciones inversas, límites, continuidad y derivadas.
