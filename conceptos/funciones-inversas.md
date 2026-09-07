---
title: "Funciones inversas"
description: "Cuándo una función puede invertirse, por qué la biyectividad es la condición exacta y cómo construir, verificar e interpretar su inversa."
content-id: MA-CON-0010
content-type: concept
status: published
date-created: 2026-09-07
date-modified: 2026-09-07
areas:
  - fundamentos
  - algebra
  - calculo
level: fundamental
topics:
  - funciones
  - funcion-inversa
  - biyectividad
  - composicion-de-funciones
  - funcion-identidad
  - fibras
  - preimagen
  - restriccion-de-dominio
prerequisites:
  - MA-CON-0007
  - MA-CON-0008
  - MA-CON-0009
related:
  - MA-CON-0006
provenance:
  type: classical
  sources: []
license: GFDL-1.3-or-later
---

Una función puede transformar un elemento del dominio en un elemento del codominio. La pregunta natural es si ese proceso puede **deshacerse de manera funcional**.

Si

$$
f:A\to B,
$$

queremos saber cuándo existe otra función

$$
g:B\to A
$$

que recupere exactamente el punto de partida.

La respuesta está determinada por la biyectividad.

::: {.ma-block .ma-intuicion}
**Intuición**

Para invertir una función necesitamos poder regresar desde cada salida hasta **un único** punto del dominio.

- si una salida tiene dos antecedentes, no sabemos cuál elegir;
- si un elemento del codominio no tiene antecedente, no tenemos desde dónde regresar;
- si cada elemento del codominio tiene exactamente un antecedente, la inversión queda bien definida.

En lenguaje de fibras: una función es invertible precisamente cuando cada fibra contiene exactamente un elemento.
:::

## Definición de función inversa

Sea

$$
f:A\to B.
$$

Una función

$$
g:B\to A
$$

se llama **inversa de $f$** si satisface simultáneamente

$$
g\circ f=\operatorname{id}_A
$$

y

$$
f\circ g=\operatorname{id}_B.
$$

Cuando existe, se denota

$$
g=f^{-1}.
$$

Por tanto,

$$
\boxed{
f^{-1}\circ f=\operatorname{id}_A
\qquad\text{y}\qquad
f\circ f^{-1}=\operatorname{id}_B
}
$$

::: {.ma-block .ma-definicion}
**Definición**

La inversa de una función $f:A\to B$ es una función $f^{-1}:B\to A$ que deshace a $f$ en ambos sentidos mediante composición.
:::

La dirección de la flecha se invierte:

$$
f:A\to B
\qquad\Longrightarrow\qquad
f^{-1}:B\to A.
$$

Así, el dominio de $f^{-1}$ es el codominio de $f$, y el codominio de $f^{-1}$ es el dominio de $f$.

## La condición exacta: biyectividad

El resultado central es el siguiente.

::: {.ma-block .ma-definicion}
**Teorema**

Una función

$$
f:A\to B
$$

tiene función inversa si y sólo si es biyectiva.

En símbolos,

$$
\boxed{
f\text{ es invertible}
\iff
f\text{ es biyectiva}
}
$$
:::

### Si existe inversa, entonces $f$ es inyectiva

Supongamos que existe

$$
f^{-1}:B\to A.
$$

Sean $x_1,x_2\in A$ tales que

$$
f(x_1)=f(x_2).
$$

Aplicamos $f^{-1}$ a ambos lados:

$$
f^{-1}(f(x_1))=f^{-1}(f(x_2)).
$$

Como

$$
f^{-1}\circ f=\operatorname{id}_A,
$$

obtenemos

$$
x_1=x_2.
$$

Por tanto, $f$ es inyectiva.

### Si existe inversa, entonces $f$ es sobreyectiva

Sea $y\in B$ arbitrario. Como $f^{-1}$ está definida en todo $B$, podemos tomar

$$
x=f^{-1}(y)\in A.
$$

Entonces

$$
f(x)
=f(f^{-1}(y))
=y.
$$

Así, todo $y\in B$ tiene antecedente y $f$ es sobreyectiva.

Por tanto, la existencia de inversa implica que $f$ es biyectiva.

### Si $f$ es biyectiva, entonces existe inversa

Supongamos ahora que $f:A\to B$ es biyectiva.

Para cada $y\in B$:

- la sobreyectividad garantiza que existe al menos un $x\in A$ con $f(x)=y$;
- la inyectividad garantiza que ese $x$ es único.

Podemos entonces definir

$$
f^{-1}(y)=x
$$

como **el único** elemento $x\in A$ tal que

$$
f(x)=y.
$$

Esta asignación está definida para todo $y\in B$ y produce un único elemento de $A$, de modo que realmente define una función

$$
f^{-1}:B\to A.
$$

Por construcción,

$$
f^{-1}(f(x))=x
$$

para todo $x\in A$, y

$$
f(f^{-1}(y))=y
$$

para todo $y\in B$.

Luego $f^{-1}$ es la inversa de $f$.

## La equivalencia fundamental

Si $f:A\to B$ es biyectiva, entonces para todo $x\in A$ y todo $y\in B$ se cumple

$$
\boxed{
f(x)=y
\iff
f^{-1}(y)=x
}
$$

En efecto, si $f(x)=y$, al aplicar $f^{-1}$ obtenemos

$$
f^{-1}(f(x))=f^{-1}(y),
$$

y por tanto

$$
x=f^{-1}(y).
$$

Recíprocamente, si

$$
f^{-1}(y)=x,
$$

al aplicar $f$ obtenemos

$$
f(f^{-1}(y))=f(x),
$$

y por tanto

$$
y=f(x).
$$

::: {.ma-block .ma-intuicion}
**Lectura operacional**

La igualdad

$$
f(x)=y
$$

puede leerse en sentido inverso como

$$
f^{-1}(y)=x.
$$

Es la misma correspondencia recorrida en direcciones opuestas:

$$
x\xrightarrow{f}y
\qquad\Longleftrightarrow\qquad
y\xrightarrow{f^{-1}}x.
$$
:::

## La interpretación mediante fibras

Para $y\in B$, la fibra de $f$ sobre $y$ es

$$
f^{-1}(\{y\})
=
\{x\in A:f(x)=y\}.
$$

La biyectividad dice exactamente que

$$
\boxed{
f^{-1}(\{y\})\text{ tiene un único elemento para cada }y\in B.
}
$$

Si escribimos

$$
f^{-1}(\{y\})=\{x\},
$$

entonces la función inversa simplemente asigna

$$
f^{-1}(y)=x.
$$

::: {.ma-block .ma-observacion}
**De la fibra a la inversa**

La fibra $f^{-1}(\{y\})$ es un **conjunto** de antecedentes y tiene sentido para cualquier función.

Cuando $f$ es biyectiva, cada una de esas fibras es un conjunto unitario. Entonces podemos extraer de cada fibra su único elemento y obtener la función inversa.
:::

## Dos usos distintos de la notación $f^{-1}$

La notación exige atención.

### Preimagen de un conjunto

Para cualquier función $f:A\to B$ y cualquier conjunto $C\subseteq B$,

$$
f^{-1}(C)
=
\{x\in A:f(x)\in C\}
$$

significa la **preimagen** de $C$.

Esto no requiere que $f$ sea biyectiva.

### Función inversa

Si $f$ es biyectiva, también existe la función

$$
f^{-1}:B\to A.
$$

En este segundo uso, $f^{-1}$ es una función.

Cuando $f$ es biyectiva y $C\subseteq B$, ambos lenguajes son compatibles:

$$
\boxed{
f^{-1}(C)
=
\{f^{-1}(y):y\in C\}.
}
$$

Aquí las dos apariciones de $f^{-1}$ tienen funciones notacionales distintas:

- en el lado izquierdo, $f^{-1}(C)$ es la **preimagen de $C$ por $f$**;
- en el lado derecho, $f^{-1}(y)$ es el **valor de la función inversa** en $y$.

::: {.ma-block .ma-error}
**No confundir**

La expresión

$$
f^{-1}(\{y\})
$$

puede denotar la preimagen del conjunto unitario $\{y\}$ incluso cuando $f$ no tiene inversa.

En cambio,

$$
f^{-1}(y)
$$

como valor de una **función inversa** sólo tiene sentido cuando la inversa existe.
:::

## La inversa no es el recíproco

Otra confusión frecuente consiste en identificar

$$
f^{-1}(x)
$$

con

$$
\frac{1}{f(x)}.
$$

Son objetos completamente diferentes.

Por ejemplo, si

$$
f(x)=2x-3,
$$

su función inversa será

$$
f^{-1}(x)=\frac{x+3}{2},
$$

mientras que el recíproco de sus valores es

$$
\frac{1}{f(x)}=\frac{1}{2x-3}.
$$

::: {.ma-block .ma-error}
**Error frecuente**

El exponente $-1$ en $f^{-1}$ no significa elevar los valores de $f$ a la potencia $-1$.

La notación indica **inversión respecto de la composición**, no inversión multiplicativa.
:::

## Ejemplo: una función lineal

Consideremos

$$
f:\mathbb R\to\mathbb R,
\qquad
f(x)=2x-3.
$$

Ya sabemos que esta función es biyectiva. Para hallar su inversa, partimos de

$$
y=2x-3
$$

y resolvemos para $x$:

$$
y+3=2x,
$$

$$
x=\frac{y+3}{2}.
$$

Intercambiando el nombre de la variable de entrada,

$$
\boxed{
f^{-1}(x)=\frac{x+3}{2}}
$$

con

$$
f^{-1}:\mathbb R\to\mathbb R.
$$

### Verificación por composición

Primero,

$$
(f^{-1}\circ f)(x)
=
f^{-1}(2x-3)
=
\frac{(2x-3)+3}{2}
=x.
$$

Por tanto,

$$
f^{-1}\circ f=\operatorname{id}_{\mathbb R}.
$$

En el otro sentido,

$$
(f\circ f^{-1})(x)
=
2\left(\frac{x+3}{2}\right)-3
=x.
$$

Así,

$$
f\circ f^{-1}=\operatorname{id}_{\mathbb R}.
$$

::: {.ma-block .ma-metodo}
**Método algebraico para hallar una inversa**

Cuando trabajamos con funciones reales dadas por fórmulas:

1. verifica primero que la función sea biyectiva en el dominio y codominio declarados;
2. escribe $y=f(x)$;
3. despeja $x$ en función de $y$;
4. intercambia los nombres de las variables si resulta conveniente;
5. declara explícitamente dominio y codominio de $f^{-1}$;
6. comprueba, cuando sea necesario,
   $$
   f^{-1}\circ f=\operatorname{id}
   \quad\text{y}\quad
   f\circ f^{-1}=\operatorname{id}.
   $$
:::

Despejar una ecuación puede sugerir una fórmula candidata, pero **no sustituye la verificación de biyectividad ni el control de dominio y codominio**.

## La función cuadrado: por qué el dominio importa

Consideremos

$$
q:\mathbb R\to\mathbb R,
\qquad
q(x)=x^2.
$$

Esta función no es inyectiva porque

$$
q(1)=q(-1)=1,
$$

y tampoco es sobreyectiva sobre $\mathbb R$ porque no alcanza valores negativos.

Por tanto, no tiene inversa

$$
q^{-1}:\mathbb R\to\mathbb R.
$$

Si intentamos despejar

$$
y=x^2,
$$

obtenemos

$$
x=\pm\sqrt y.
$$

El signo $\pm$ revela precisamente el problema: para $y>0$ existen dos antecedentes, de modo que no podemos asignar un único valor sin introducir una restricción adicional.

### Restricción que produce una biyección

Definamos

$$
r:[0,\infty)\to[0,\infty),
\qquad
r(x)=x^2.
$$

Esta función sí es biyectiva. Como $x\ge0$, al resolver

$$
y=x^2
$$

obtenemos unívocamente

$$
x=\sqrt y.
$$

Por tanto,

$$
\boxed{
r^{-1}(x)=\sqrt x}
$$

con

$$
r^{-1}:[0,\infty)\to[0,\infty).
$$

::: {.ma-block .ma-observacion}
**Restricción e inversión**

Una fórmula que no define una función invertible sobre cierto dominio puede volverse invertible al restringir el dominio de manera que desaparezcan las repeticiones de valores y al elegir un codominio adecuado.

La raíz cuadrada principal aparece precisamente como inversa de la función cuadrado restringida a $[0,\infty)$.
:::

## Interpretación gráfica

Si $f$ es una función real invertible, los puntos de su gráfica tienen la forma

$$
(x,f(x)).
$$

Como

$$
f^{-1}(f(x))=x,
$$

la gráfica de la inversa contiene el punto

$$
(f(x),x).
$$

Las coordenadas se intercambian. Geométricamente, esto corresponde a reflejar la gráfica respecto de la recta

$$
y=x.
$$

Por tanto, las gráficas de $f$ y $f^{-1}$ son simétricas respecto de esa recta.

::: {.ma-block .ma-intuicion}
**Lectura gráfica**

Invertir una función intercambia el papel de entrada y salida. En el plano cartesiano eso intercambia las coordenadas $(x,y)$ por $(y,x)$, que es exactamente la reflexión respecto de $y=x$.
:::

## La inversa de la identidad

Para cualquier conjunto $A$,

$$
\operatorname{id}_A:A\to A,
\qquad
\operatorname{id}_A(x)=x
$$

es biyectiva.

Además,

$$
\operatorname{id}_A\circ\operatorname{id}_A
=
\operatorname{id}_A.
$$

Por tanto,

$$
\boxed{
\operatorname{id}_A^{-1}=\operatorname{id}_A
}
$$

La identidad es su propia inversa.

## Inversa de una composición

Sean

$$
f:A\to B,
\qquad
g:B\to C
$$

funciones biyectivas. Entonces

$$
g\circ f:A\to C
$$

es biyectiva y

$$
\boxed{
(g\circ f)^{-1}
=
f^{-1}\circ g^{-1}
}
$$

Observa que el **orden se invierte**.

### Demostración

Componemos:

$$
(f^{-1}\circ g^{-1})\circ(g\circ f).
$$

Por asociatividad,

$$
f^{-1}\circ(g^{-1}\circ g)\circ f.
$$

Como

$$
g^{-1}\circ g=\operatorname{id}_B,
$$

queda

$$
f^{-1}\circ\operatorname{id}_B\circ f
=
f^{-1}\circ f
=
\operatorname{id}_A.
$$

En el otro sentido,

$$
(g\circ f)\circ(f^{-1}\circ g^{-1})
$$

se reduce a

$$
g\circ(f\circ f^{-1})\circ g^{-1}
=
g\circ\operatorname{id}_B\circ g^{-1}
=
\operatorname{id}_C.
$$

Por tanto,

$$
(g\circ f)^{-1}=f^{-1}\circ g^{-1}.
$$

::: {.ma-block .ma-intuicion}
**Por qué se invierte el orden**

Si primero aplicamos $f$ y después $g$, para deshacer el proceso debemos comenzar deshaciendo $g$ y sólo entonces deshacer $f$:

$$
A\xrightarrow{f}B\xrightarrow{g}C
\qquad\leadsto\qquad
C\xrightarrow{g^{-1}}B\xrightarrow{f^{-1}}A.
$$
:::

## La inversa es única

Si una función $f:A\to B$ tiene inversa, esa inversa es única.

Supongamos que $g:B\to A$ y $h:B\to A$ son ambas inversas de $f$. Entonces

$$
g
=
g\circ\operatorname{id}_B
=
g\circ(f\circ h).
$$

Por asociatividad,

$$
g\circ(f\circ h)
=(g\circ f)\circ h.
$$

Como $g\circ f=\operatorname{id}_A$,

$$
(g\circ f)\circ h
=
\operatorname{id}_A\circ h
=h.
$$

Luego

$$
\boxed{g=h}.
$$

Así, cuando escribimos $f^{-1}$, no hay ambigüedad: una función invertible posee una única inversa.

## Invertir dos veces recupera la función

Si $f:A\to B$ es biyectiva, entonces su inversa

$$
f^{-1}:B\to A
$$

también es biyectiva. Además, las identidades

$$
f\circ f^{-1}=\operatorname{id}_B
$$

y

$$
f^{-1}\circ f=\operatorname{id}_A
$$

muestran que $f$ es precisamente la inversa de $f^{-1}$.

Por tanto,

$$
\boxed{
(f^{-1})^{-1}=f
}
$$

::: {.ma-block .ma-observacion}
**La inversión es reversible**

Pasar de $f$ a $f^{-1}$ no pierde información: invertir nuevamente devuelve la función original.
:::

## Comprobación conceptual

::: {.ma-block .ma-comprobacion}
**Antes de afirmar que una inversa existe**

Para una función $f:A\to B$, conviene comprobar:

1. **Inyectividad:** cada $y\in B$ tiene a lo sumo un antecedente.
2. **Sobreyectividad:** cada $y\in B$ tiene al menos un antecedente.
3. **Biyectividad:** por tanto, cada $y\in B$ tiene exactamente un antecedente.
4. Sólo entonces ese antecedente único puede definirse como $f^{-1}(y)$.

En términos de composición, la verificación final es

$$
f^{-1}\circ f=\operatorname{id}_A,
\qquad
f\circ f^{-1}=\operatorname{id}_B.
$$
:::

La idea central puede condensarse en una sola cadena:

$$
\boxed{
\text{fibras unitarias}
\iff
\text{biyectividad}
\iff
\text{existencia de función inversa}
}
$$

## Relaciones

- **Prerrequisitos:** [Funciones reales: dominio, codominio, imagen y preimagen](funciones-reales-dominio-codominio-imagen-y-preimagen.md) (`MA-CON-0007`); [Composición de funciones e identidad](composicion-de-funciones-e-identidad.md) (`MA-CON-0008`); [Inyectividad, sobreyectividad y biyectividad](inyectividad-sobreyectividad-y-biyectividad.md) (`MA-CON-0009`).
- **Contenidos relacionados:** [Operaciones con conjuntos reales: unión, intersección, complemento y diferencia](operaciones-con-conjuntos-reales.md) (`MA-CON-0006`).
- **Siguiente paso natural:** comportamiento de funciones inversas bajo continuidad y derivación, una vez introducidas esas nociones.