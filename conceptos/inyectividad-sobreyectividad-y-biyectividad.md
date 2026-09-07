---
title: "Inyectividad, sobreyectividad y biyectividad"
description: "Cómo distinguir funciones inyectivas, sobreyectivas y biyectivas mediante imágenes, preimágenes, ecuaciones y composición."
content-id: MA-CON-0009
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
  - inyectividad
  - sobreyectividad
  - biyectividad
  - imagen
  - preimagen
  - codominio
  - composicion-de-funciones
prerequisites:
  - MA-CON-0007
  - MA-CON-0008
related:
  - MA-CON-0006
provenance:
  type: classical
  sources: []
license: GFDL-1.3-or-later
---

Una función

$$
f:A\to B
$$

puede relacionar su dominio y su codominio de maneras muy diferentes. Algunas funciones identifican entradas distintas en una misma salida; otras dejan elementos del codominio sin alcanzar; otras, en cambio, establecen una correspondencia exacta entre ambos conjuntos.

Las nociones de **inyectividad**, **sobreyectividad** y **biyectividad** permiten distinguir rigurosamente estas situaciones.

::: {.ma-block .ma-intuicion}
**Intuición**

Las tres preguntas fundamentales son:

1. **Inyectividad:** ¿pueden dos entradas distintas producir la misma salida?
2. **Sobreyectividad:** ¿todo elemento del codominio es alcanzado por alguna entrada?
3. **Biyectividad:** ¿cada elemento del codominio es alcanzado por exactamente una entrada?
:::

## Inyectividad

Una función

$$
f:A\to B
$$

es **inyectiva** si entradas diferentes siempre producen salidas diferentes.

Formalmente,

$$
f(x_1)=f(x_2)
\quad\Longrightarrow\quad
x_1=x_2
$$

para todos $x_1,x_2\in A$.

Equivalentemente,

$$
x_1\ne x_2
\quad\Longrightarrow\quad
f(x_1)\ne f(x_2).
$$

::: {.ma-block .ma-definicion}
**Definición**

Una función es inyectiva cuando cada valor que aparece como salida tiene **a lo sumo un antecedente** en el dominio.
:::

### Ejemplo: una función lineal

Consideremos

$$
f:\mathbb R\to\mathbb R,
\qquad
f(x)=2x-3.
$$

Para probar que es inyectiva, supongamos

$$
f(x_1)=f(x_2).
$$

Entonces

$$
2x_1-3=2x_2-3.
$$

Sumando $3$ en ambos lados,

$$
2x_1=2x_2,
$$

y dividiendo por $2$,

$$
x_1=x_2.
$$

Por tanto, $f$ es inyectiva.

### Contraejemplo: la función cuadrado

Sea

$$
q:\mathbb R\to\mathbb R,
\qquad
q(x)=x^2.
$$

Tenemos

$$
q(1)=1
$$

y también

$$
q(-1)=1.
$$

Como

$$
1\ne -1
$$

pero

$$
q(1)=q(-1),
$$

la función no es inyectiva.

::: {.ma-block .ma-metodo}
**Método para probar inyectividad**

Un procedimiento muy frecuente es:

1. tomar $x_1,x_2$ en el dominio;
2. suponer que $f(x_1)=f(x_2)$;
3. usar esa igualdad para demostrar que necesariamente $x_1=x_2$.

Para demostrar que una función **no** es inyectiva basta encontrar dos entradas distintas con la misma imagen.
:::

## Sobreyectividad

Una función

$$
f:A\to B
$$

es **sobreyectiva** si todo elemento del codominio $B$ es imagen de al menos un elemento del dominio.

Formalmente,

$$
\forall y\in B,
\quad
\exists x\in A
\text{ tal que }
f(x)=y.
$$

Esto equivale a afirmar que

$$
f(A)=B.
$$

Es decir, la imagen de la función coincide con su codominio.

::: {.ma-block .ma-definicion}
**Definición**

Una función es sobreyectiva cuando cada elemento del codominio tiene **al menos un antecedente** en el dominio.
:::

### Ejemplo: la misma función lineal

Volvamos a

$$
f:\mathbb R\to\mathbb R,
\qquad
f(x)=2x-3.
$$

Sea $y\in\mathbb R$ arbitrario. Queremos saber si existe $x\in\mathbb R$ tal que

$$
2x-3=y.
$$

Resolviendo para $x$,

$$
2x=y+3,
$$

$$
x=\frac{y+3}{2}.
$$

Como este número es real para todo $y\in\mathbb R$, cada elemento del codominio tiene un antecedente.

Por tanto, $f$ es sobreyectiva.

### La importancia del codominio

Consideremos otra vez la fórmula

$$
q(x)=x^2.
$$

Si declaramos

$$
q:\mathbb R\to\mathbb R,
$$

la función no es sobreyectiva, porque ningún número negativo es imagen de un número real:

$$
x^2\ge0
$$

para todo $x\in\mathbb R$.

Por ejemplo, no existe $x\in\mathbb R$ tal que

$$
x^2=-1.
$$

En cambio, si definimos

$$
q:\mathbb R\to[0,\infty),
\qquad
q(x)=x^2,
$$

entonces sí es sobreyectiva: para cada $y\ge0$ podemos tomar, por ejemplo,

$$
x=\sqrt y,
$$

y obtenemos

$$
q(x)=y.
$$

::: {.ma-block .ma-observacion}
**Observación**

La sobreyectividad depende esencialmente del **codominio declarado**.

La misma fórmula y el mismo dominio pueden definir una función sobreyectiva o no sobreyectiva según cuál sea el codominio.
:::

::: {.ma-block .ma-metodo}
**Método para probar sobreyectividad**

Para probar que $f:A\to B$ es sobreyectiva:

1. toma un $y\in B$ arbitrario;
2. intenta resolver la ecuación
   $$
   f(x)=y;
   $$
3. verifica que la solución obtenida pertenece al dominio $A$.

Para demostrar que una función **no** es sobreyectiva basta encontrar un elemento del codominio que no tenga antecedente.
:::

## Biyectividad

Una función es **biyectiva** si es simultáneamente inyectiva y sobreyectiva.

Por tanto,

$$
\boxed{
\text{biyectiva}
\iff
\text{inyectiva y sobreyectiva}
}
$$

Esto significa que cada elemento del codominio tiene **exactamente un antecedente**.

La función

$$
f:\mathbb R\to\mathbb R,
\qquad
f(x)=2x-3
$$

es biyectiva, porque ya demostramos que es inyectiva y sobreyectiva.

::: {.ma-block .ma-intuicion}
**Intuición**

Una biyección empareja los elementos del dominio y del codominio sin repeticiones ni omisiones:

- ninguna salida recibe dos entradas distintas;
- ninguna salida del codominio queda sin recibir una entrada.
:::

## Una misma fórmula puede cambiar de clasificación

La función cuadrado proporciona un ejemplo especialmente instructivo.

### Caso 1

$$
q:\mathbb R\to\mathbb R,
\qquad
q(x)=x^2.
$$

No es inyectiva porque

$$
q(1)=q(-1),
$$

y no es sobreyectiva porque no alcanza números negativos.

Por tanto, no es biyectiva.

### Caso 2

$$
q:\mathbb R\to[0,\infty),
\qquad
q(x)=x^2.
$$

Ahora es sobreyectiva, pero continúa sin ser inyectiva.

### Caso 3

Restringimos también el dominio:

$$
r:[0,\infty)\to[0,\infty),
\qquad
r(x)=x^2.
$$

Esta función es sobreyectiva, porque para cada $y\ge0$ existe

$$
x=\sqrt y\ge0
$$

tal que $r(x)=y$.

También es inyectiva. Si $x_1,x_2\ge0$ y

$$
x_1^2=x_2^2,
$$

entonces

$$
(x_1-x_2)(x_1+x_2)=0.
$$

Como $x_1+x_2\ge0$, y el único caso en que puede ser $0$ es $x_1=x_2=0$, en todos los casos obtenemos

$$
x_1=x_2.
$$

Por tanto,

$$
r:[0,\infty)\to[0,\infty)
$$

es biyectiva.

::: {.ma-block .ma-observacion}
**Restricción de dominio y codominio**

Modificar el dominio o el codominio puede cambiar propiedades estructurales de una función.

En particular, una función no inyectiva puede convertirse en inyectiva al restringir adecuadamente su dominio, y una función no sobreyectiva puede convertirse en sobreyectiva al elegir como codominio su imagen.
:::

## Preimágenes y fibras

La definición de preimagen permite expresar las tres nociones de manera muy compacta.

Para $y\in B$, consideremos

$$
f^{-1}(\{y\})
=
\{x\in A:f(x)=y\}.
$$

Este conjunto reúne todos los antecedentes de $y$.

Entonces:

- $f$ es **inyectiva** si cada conjunto $f^{-1}(\{y\})$ tiene a lo sumo un elemento;
- $f$ es **sobreyectiva** si cada $f^{-1}(\{y\})$, con $y\in B$, tiene al menos un elemento;
- $f$ es **biyectiva** si cada $f^{-1}(\{y\})$, con $y\in B$, tiene exactamente un elemento.

Podemos resumirlo así:

$$
\begin{array}{c|c}
\text{propiedad} & \text{número de antecedentes de cada }y\in B\\
\hline
\text{inyectiva} & \le 1\\
\text{sobreyectiva} & \ge 1\\
\text{biyectiva} & =1
\end{array}
$$

::: {.ma-block .ma-error}
**No confundir preimagen con función inversa**

La notación

$$
f^{-1}(\{y\})
$$

tiene sentido para cualquier función: representa la preimagen de un conjunto.

Esto **no** significa que exista una función inversa $f^{-1}$. La existencia de una función inversa requerirá una condición adicional que estudiaremos después.
:::

## Interpretación gráfica

Para una función real cuya gráfica se dibuja en el plano cartesiano, las rectas horizontales proporcionan una interpretación visual útil.

### Inyectividad

Una función es inyectiva si ninguna recta horizontal corta su gráfica en más de un punto.

Es el llamado **criterio de la recta horizontal**.

### Sobreyectividad

Si el codominio es $B\subseteq\mathbb R$, la función es sobreyectiva si, para cada $y\in B$, la recta horizontal de altura $y$ corta la gráfica al menos una vez.

### Biyectividad

Es biyectiva si cada altura correspondiente a un elemento del codominio corta la gráfica exactamente una vez.

::: {.ma-block .ma-error}
**Error frecuente**

El criterio gráfico de sobreyectividad siempre debe interpretarse respecto del **codominio**.

No basta mirar qué valores parece alcanzar una curva sin saber cuál es el conjunto de llegada declarado.
:::

## Composición e inyectividad

Sean

$$
f:A\to B,
\qquad
g:B\to C.
$$

Si $f$ y $g$ son inyectivas, entonces

$$
g\circ f:A\to C
$$

también es inyectiva.

### Demostración

Supongamos

$$
(g\circ f)(x_1)=(g\circ f)(x_2).
$$

Entonces

$$
g(f(x_1))=g(f(x_2)).
$$

Como $g$ es inyectiva,

$$
f(x_1)=f(x_2).
$$

Como $f$ también es inyectiva,

$$
x_1=x_2.
$$

Por tanto, $g\circ f$ es inyectiva.

Además, existe una implicación parcial importante:

$$
g\circ f\text{ inyectiva}
\quad\Longrightarrow\quad
f\text{ inyectiva}.
$$

En efecto, si $f(x_1)=f(x_2)$, entonces automáticamente

$$
g(f(x_1))=g(f(x_2)),
$$

y la inyectividad de $g\circ f$ obliga a que $x_1=x_2$.

## Composición y sobreyectividad

Si $f$ y $g$ son sobreyectivas, entonces $g\circ f$ también es sobreyectiva.

### Demostración

Sea $z\in C$. Como $g$ es sobreyectiva, existe $y\in B$ tal que

$$
g(y)=z.
$$

Como $f$ es sobreyectiva, existe $x\in A$ tal que

$$
f(x)=y.
$$

Por tanto,

$$
(g\circ f)(x)
=
g(f(x))
=
g(y)
=
z.
$$

Así, todo elemento de $C$ es alcanzado por $g\circ f$.

También tenemos la implicación parcial

$$
g\circ f\text{ sobreyectiva}
\quad\Longrightarrow\quad
g\text{ sobreyectiva}.
$$

## Composición y biyectividad

Si $f$ y $g$ son biyectivas, entonces ambas son inyectivas y sobreyectivas. Por los resultados anteriores,

$$
g\circ f
$$

es también inyectiva y sobreyectiva, y por tanto biyectiva.

En símbolos,

$$
\boxed{
f,g\text{ biyectivas}
\Longrightarrow
g\circ f\text{ biyectiva}}
$$

La función identidad proporciona el ejemplo más inmediato:

$$
\operatorname{id}_A:A\to A,
\qquad
\operatorname{id}_A(x)=x.
$$

Cada elemento se envía a sí mismo, de modo que la identidad es biyectiva.

## Hacia las funciones inversas

La biyectividad prepara una de las construcciones más importantes de la teoría de funciones.

Si cada $y\in B$ posee exactamente un antecedente $x\in A$, podemos intentar invertir la correspondencia:

$$
y\longmapsto x.
$$

La existencia y las propiedades de esa **función inversa** serán el siguiente paso natural.

::: {.ma-block .ma-comprobacion}
**Comprobación conceptual**

Para clasificar una función $f:A\to B$, conviene formular separadamente estas preguntas:

- ¿puedo encontrar $x_1\ne x_2$ con $f(x_1)=f(x_2)$? Si sí, no es inyectiva.
- ¿existe algún $y\in B$ que no pueda escribirse como $f(x)$? Si sí, no es sobreyectiva.
- si ninguna de estas dos obstrucciones aparece, la función es biyectiva.
:::

## Relaciones

- **Prerrequisitos:** [Funciones reales: dominio, codominio, imagen y preimagen](funciones-reales-dominio-codominio-imagen-y-preimagen.md) (`MA-CON-0007`); [Composición de funciones e identidad](composicion-de-funciones-e-identidad.md) (`MA-CON-0008`).
- **Contenidos relacionados:** [Operaciones con conjuntos reales: unión, intersección, complemento y diferencia](operaciones-con-conjuntos-reales.md) (`MA-CON-0006`).
- **Siguiente paso natural:** funciones inversas y caracterización de las biyecciones.
