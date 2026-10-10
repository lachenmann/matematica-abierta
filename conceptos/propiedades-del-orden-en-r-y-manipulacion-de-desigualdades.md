---
title: "Propiedades del orden en ℝ y manipulación de desigualdades"
description: "Reglas fundamentales para transformar desigualdades reales con control explícito de signos y equivalencias."
content-id: MA-CON-0005
content-type: concept
status: published
date-created: 2026-09-06
date-modified: 2026-09-06
areas:
  - fundamentos
  - algebra
level: fundamental
topics:
  - numeros-reales
  - orden
  - desigualdades
  - signos
  - manipulacion-algebraica
  - equivalencias
prerequisites: []
related:
  - MA-CON-0001
  - MA-CON-0002
  - MA-CON-0003
  - MA-CON-0004
  - MA-PRB-0001
  - MA-PRB-0002
provenance:
  type: classical
  sources: []
license: GFDL-1.3-or-later
---

Las desigualdades no se manipulan mediante una colección de trucos aislados. Sus reglas provienen de la manera en que el **orden** de los números reales interactúa con las operaciones aritméticas.

El objetivo de esta página es establecer esas reglas con suficiente precisión para distinguir entre una transformación siempre válida y otra que exige información adicional sobre los signos.

::: {.ma-block .ma-intuicion}
**Intuición**

Una desigualdad expresa una posición relativa en la recta real. Algunas operaciones trasladan o escalan esa recta sin cambiar el orden; otras invierten su orientación.

La pregunta útil no es solamente «¿qué operación hago?», sino:

> **¿esta operación conserva el orden, lo invierte o necesita una hipótesis de signo?**
:::

## El orden de los números reales

Dados dos números reales $a$ y $b$, exactamente una de las siguientes posibilidades ocurre:

$$
a<b,\qquad a=b,\qquad a>b.
$$

Esta propiedad se conoce como **tricotomía**.

Además, el orden es transitivo:

$$
a<b\quad\text{y}\quad b<c
\quad\Longrightarrow\quad
a<c.
$$

Análogamente,

$$
a\le b\quad\text{y}\quad b\le c
\quad\Longrightarrow\quad
a\le c.
$$

Estas propiedades permiten escribir cadenas como

$$
a<b<c
$$

como abreviatura de las dos condiciones

$$
a<b
\qquad\text{y}\qquad
b<c.
$$

## Sumar o restar la misma cantidad

Si

$$
a<b,
$$

entonces, para cualquier $c\in\mathbb R$,

$$
a+c<b+c.
$$

Más aún, la implicación es reversible:

$$
\boxed{
a<b
\quad\Longleftrightarrow\quad
a+c<b+c
}.
$$

Lo mismo vale para $\le$, $>$ y $\ge$.

Por ejemplo,

$$
x-7\le 4
$$

es equivalente a

$$
x\le 11.
$$

::: {.ma-block .ma-metodo}
**Método**

Sumar o restar una misma cantidad en ambos miembros de una desigualdad **no cambia su sentido**.

No hace falta conocer el signo de la cantidad añadida.
:::

## Multiplicar por un número positivo

Si

$$
a<b
$$

y $c>0$, entonces

$$
ac<bc.
$$

Por tanto,

$$
\boxed{
a<b
\quad\Longleftrightarrow\quad
ac<bc
\qquad(c>0)
}.
$$

Dividir por un número positivo produce la misma conservación del orden.

Ejemplo:

$$
3x<12
\quad\Longleftrightarrow\quad
x<4.
$$

## Multiplicar por un número negativo

Si $c<0$, la orientación cambia:

$$
a<b
\quad\Longrightarrow\quad
ac>bc.
$$

Así,

$$
\boxed{
a<b
\quad\Longleftrightarrow\quad
ac>bc
\qquad(c<0)
}.
$$

Por ejemplo,

$$
-2x\le 6
$$

al dividir por $-2$ se convierte en

$$
x\ge -3.
$$

::: {.ma-block .ma-error}
**Error frecuente**

No se invierte una desigualdad simplemente «porque estamos dividiendo». Se invierte **porque se multiplica o divide por una cantidad negativa**.

El signo del factor es la información decisiva.
:::

### Por qué aparece la inversión

Si

$$
a<b,
$$

entonces, al sumar $-b$ a ambos lados,

$$
a-b<0.
$$

Multiplicar por $-1$ cambia el signo de un número negativo:

$$
-(a-b)>0.
$$

Como

$$
-(a-b)=b-a,
$$

tenemos

$$
b-a>0,
$$

es decir,

$$
-b<-a.
$$

Por eso

$$
\boxed{a<b\Longleftrightarrow -a>-b}.
$$

## El caso del factor cero

Multiplicar ambos miembros por cero destruye la información de orden:

$$
a<b
$$

se transforma en

$$
0=0.
$$

Por tanto, no existe una equivalencia del tipo

$$
a<b
\Longleftrightarrow
0a<0b.
$$

::: {.ma-block .ma-observacion}
**Observación**

Cuando dividimos una desigualdad por una expresión que contiene la variable, primero debemos saber si esa expresión es positiva, negativa o cero. Sin ese control, no sabemos si el sentido se conserva, se invierte o si la división está prohibida.
:::

## Sumar desigualdades

Si

$$
a\le b
$$

y

$$
c\le d,
$$

entonces

$$
\boxed{a+c\le b+d}.
$$

En efecto,

$$
a+c\le b+c\le b+d.
$$

La transitividad completa el argumento.

Para desigualdades estrictas, si

$$
a<b
\qquad\text{y}\qquad
c<d,
$$

entonces

$$
a+c<b+d.
$$

Sin embargo, no toda operación puede hacerse miembro a miembro con la misma libertad.

## Multiplicar desigualdades requiere control de signos

De

$$
a\le b
\qquad\text{y}\qquad
c\le d
$$

no se puede concluir en general que

$$
ac\le bd.
$$

Por ejemplo,

$$
-3<-2
\qquad\text{y}\qquad
-3<-2,
$$

pero

$$
9>4.
$$

Una condición suficiente frecuente es que todas las cantidades sean no negativas:

$$
0\le a\le b,
\qquad
0\le c\le d.
$$

Entonces sí:

$$
ac\le bc\le bd,
$$

y por tanto

$$
\boxed{ac\le bd}.
$$

::: {.ma-block .ma-dominio}
**Control de signos**

Antes de multiplicar desigualdades, dividir por expresiones variables, tomar recíprocos o elevar al cuadrado, determina qué signos son posibles.

Muchas manipulaciones incorrectas no fallan por álgebra, sino por haber omitido este paso lógico.
:::

## Tomar recíprocos

Supongamos que $a$ y $b$ son no nulos y tienen el mismo signo. Si

$$
a<b,
$$

entonces

$$
\boxed{
\frac1a>\frac1b
}.
$$

Una manera compacta de verlo es observar que $ab>0$. Dividir

$$
a<b
$$

por el número positivo $ab$ conserva el sentido:

$$
\frac{a}{ab}<\frac{b}{ab},
$$

o sea,

$$
\frac1b<\frac1a.
$$

Por ejemplo,

$$
2<5
\quad\Longrightarrow\quad
\frac12>\frac15.
$$

Y también

$$
-5<-2
\quad\Longrightarrow\quad
-\frac15>-\frac12.
$$

Si el intervalo considerado atraviesa el cero, esta regla no puede aplicarse sin separar casos, porque $1/x$ ni siquiera está definida en $x=0$.

## Elevar al cuadrado no siempre conserva el orden

De

$$
a<b
$$

no se deduce en general

$$
a^2<b^2.
$$

Por ejemplo,

$$
-4<-2,
$$

pero

$$
16>4.
$$

La función

$$
t\mapsto t^2
$$

es creciente sobre $[0,\infty)$, pero no sobre toda la recta real.

Por eso, si

$$
0\le a<b,
$$

entonces sí

$$
a^2<b^2.
$$

Y si

$$
a<b\le0,
$$

entonces ocurre lo contrario:

$$
a^2>b^2.
$$

Esta distinción es esencial al trabajar con radicales.

## Cuadrar una desigualdad con una raíz

Consideremos

$$
\sqrt{u}\le v.
$$

Para que la expresión tenga sentido necesitamos

$$
u\ge0.
$$

Además, como $\sqrt u\ge0$, la desigualdad sólo puede cumplirse si

$$
v\ge0.
$$

Bajo esas dos condiciones, ambos miembros son no negativos y podemos cuadrar preservando la equivalencia:

$$
\boxed{
\sqrt u\le v
\quad\Longleftrightarrow\quad
u\le v^2
}
$$

siempre que se mantengan explícitamente

$$
u\ge0,
\qquad
v\ge0.
$$

Esta es exactamente la precaución utilizada al determinar dominios con radicales anidados.

## Resolver una desigualdad lineal paso a paso

Consideremos

$$
5-3x<11.
$$

Restamos $5$ en ambos miembros:

$$
-3x<6.
$$

Ahora dividimos por $-3$. Como el divisor es negativo, invertimos el sentido:

$$
x>-2.
$$

Por tanto, el conjunto solución es

$$
\boxed{(-2,\infty)}.
$$

Cada paso es una equivalencia:

$$
5-3x<11
\Longleftrightarrow
-3x<6
\Longleftrightarrow
x>-2.
$$

## Una desigualdad con parámetro de signo desconocido

Supongamos que queremos resolver

$$
ax<b
$$

respecto de $x$.

No existe una única respuesta sin conocer $a$.

Si $a>0$,

$$
x<\frac ba.
$$

Si $a<0$,

$$
x>\frac ba.
$$

Si $a=0$, la desigualdad se convierte en

$$
0<b,
$$

que puede ser verdadera para todo $x$ o falsa para todo $x$, según el valor de $b$.

::: {.ma-block .ma-error}
**Error frecuente**

La expresión

$$
ax<b
\quad\Longrightarrow\quad
x<\frac ba
$$

no es válida sin la hipótesis $a>0$.

Dividir por una cantidad cuyo signo se desconoce exige separar casos.
:::

## Desigualdades dobles

Una cadena como

$$
-2<3x+1\le7
$$

representa simultáneamente

$$
-2<3x+1
$$

y

$$
3x+1\le7.
$$

Como las mismas operaciones son válidas en los tres miembros, podemos restar $1$:

$$
-3<3x\le6,
$$

y después dividir por $3>0$:

$$
-1<x\le2.
$$

En notación de intervalos,

$$
\boxed{x\in(-1,2]}.
$$

Aquí aparece directamente la conexión con [Intervalos e intersección de conjuntos reales](intervalos-e-interseccion-de-conjuntos-reales.md) (`MA-CON-0004`).

## Qué significa preservar equivalencia

Al resolver una desigualdad buscamos, idealmente, una cadena de expresiones con el **mismo conjunto solución**.

Por eso conviene distinguir

$$
P\Longrightarrow Q
$$

de

$$
P\Longleftrightarrow Q.
$$

Una transformación reversible bajo las hipótesis vigentes permite usar $\Longleftrightarrow$.

Una transformación que sólo garantiza una dirección puede introducir soluciones adicionales o perder información.

::: {.ma-block .ma-metodo}
**Método de control**

Antes de transformar una desigualdad, pregunta:

1. ¿la operación está definida?
2. ¿conozco el signo de las cantidades relevantes?
3. ¿el orden se conserva o se invierte?
4. ¿el paso es reversible?
5. ¿mantengo el mismo conjunto solución?
:::

## Conexiones con el corpus

Estas reglas sostienen directamente varios contenidos ya publicados:

- [Desigualdades cuadráticas por factorización](desigualdades-cuadraticas-por-factorizacion.md) (`MA-CON-0001`) usa el signo de factores y la inversión producida por factores negativos.
- [Valor absoluto y desigualdades básicas](valor-absoluto-y-desigualdades-basicas.md) (`MA-CON-0002`) traduce relaciones de orden en condiciones de distancia.
- [Dominio de funciones reales con radicales](dominio-de-funciones-reales-con-radicales.md) (`MA-CON-0003`) exige controlar signos antes de cuadrar.
- [Intervalos e intersección de conjuntos reales](intervalos-e-interseccion-de-conjuntos-reales.md) (`MA-CON-0004`) proporciona el lenguaje conjuntista para expresar los conjuntos solución.

Los problemas [Dominio de una función radical cuadrática](../problemas/dominio-funcion-radical-cuadratica.md) (`MA-PRB-0001`) y [Dominio de un radical anidado](../problemas/dominio-de-un-radical-anidado.md) (`MA-PRB-0002`) son aplicaciones concretas de estas reglas.

## Resumen operativo

Para $a,b,c\in\mathbb R$:

$$
\boxed{
a<b
\Longleftrightarrow
a+c<b+c
}
$$

para todo $c$;

$$
\boxed{
a<b
\Longleftrightarrow
ac<bc
}
$$

si $c>0$;

$$
\boxed{
a<b
\Longleftrightarrow
ac>bc
}
$$

si $c<0$.

Y, antes de aplicar transformaciones como

$$
\text{dividir},\qquad
\text{invertir},\qquad
\text{multiplicar desigualdades},\qquad
\text{elevar al cuadrado},
$$

la regla general es:

$$
\boxed{
\text{primero controlar signos; después transformar}
}.
$$
