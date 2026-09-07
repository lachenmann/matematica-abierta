---
title: "Axiomas de cuerpo y consecuencias algebraicas básicas"
description: "Qué propiedades algebraicas se adoptan como axiomas en un cuerpo y cómo de ellas se deducen unicidad de neutros e inversos, cancelación, producto nulo y resolución de ecuaciones lineales."
content-id: MA-CON-0020
content-type: concept
status: published
date-created: 2026-09-07
date-modified: 2026-09-07
areas:
  - fundamentos
  - algebra
level: fundamental
topics:
  - axiomas
  - axiomas-de-cuerpo
  - cuerpos
  - estructura-algebraica
  - operaciones
  - elemento-neutro
  - inversos
  - distributividad
  - cancelacion
  - producto-nulo
  - division
  - ecuaciones-lineales
  - numeros-reales
prerequisites:
  - MA-BCH-0001
related:
  - MA-CON-0005
  - MA-CON-0016
  - MA-PRB-0005
  - MA-PRB-0006
provenance:
  type: classical
  sources: []
license: GFDL-1.3-or-later
---

# Axiomas de cuerpo y consecuencias algebraicas básicas

En el álgebra escolar usamos continuamente reglas como

$$
a+0=a,
\qquad
a(-1)=-a,
\qquad
ab=0\Longrightarrow a=0\text{ o }b=0,
$$

o cancelamos una misma cantidad en ambos miembros de una ecuación. Es fácil acostumbrarse a tratarlas como si todas tuviesen el mismo estatuto.

No lo tienen.

Algunas propiedades se adoptan como **puntos de partida**. Otras se deducen de esos puntos de partida. Aprender a distinguir ambas capas es parte esencial de la lectura matemática.

::: {.ma-block .ma-intuicion}
**Intuición**

Un sistema axiomático no intenta demostrarlo todo desde la nada. Primero declara una estructura mínima y después pregunta:

> **¿qué consecuencias quedan forzadas por esa estructura?**

En esta página la estructura será la de **cuerpo**. Nuestro objetivo no será memorizar una lista de axiomas, sino ver cómo de una lista relativamente corta emergen muchas de las reglas algebraicas que usamos habitualmente.
:::

La idea central puede resumirse así:

$$
\boxed{
\text{axiomas de cuerpo}
\longrightarrow
\text{identidades derivadas}
\longrightarrow
\text{cancelación y división}
\longrightarrow
\text{ecuaciones lineales}
}
$$

Todavía **no** introduciremos orden, positividad, desigualdades ni completitud. Esas estructuras requieren axiomas adicionales.

## 1. Qué estructura queremos aislar {#ma-con-0020-estructura}

Pensemos en un conjunto $F$ provisto de dos operaciones:

$$
+:F\times F\to F
$$

y

$$
\cdot:F\times F\to F.
$$

La primera la llamamos **suma** y la segunda **producto**.

Que sean operaciones sobre $F$ significa, en particular, que si $a,b\in F$, entonces

$$
a+b\in F
\qquad\text{y}\qquad
ab\in F.
$$

No estamos diciendo todavía que $F=\mathbb R$. La misma estructura aparece, por ejemplo, en $\mathbb Q$, $\mathbb R$ y $\mathbb C$.

::: {.ma-block .ma-observacion}
**Observación**

La palabra *cuerpo* describe una **estructura algebraica**. No describe por sí sola una geometría, un orden ni una noción de límite.

Por eso conviene separar desde el comienzo:

$$
\text{estructura de cuerpo}
\neq
\text{estructura de cuerpo ordenado}
\neq
\text{estructura de cuerpo ordenado completo}.
$$
:::

## 2. Los axiomas de cuerpo {#ma-con-0020-axiomas}

::: {.ma-block .ma-definicion}
**Definición — cuerpo**

Un **cuerpo** es un conjunto $F$ con dos operaciones, suma y producto, que satisfacen las siguientes propiedades para todos $a,b,c\in F$.

### Suma

**Asociatividad**

$$
(a+b)+c=a+(b+c).
$$

**Conmutatividad**

$$
a+b=b+a.
$$

**Elemento neutro aditivo**

Existe un elemento $0\in F$ tal que

$$
a+0=a.
$$

**Inverso aditivo**

Para cada $a\in F$ existe algún $b\in F$ tal que

$$
a+b=0.
$$

Más adelante demostraremos que ese $b$ es único; solo entonces quedará justificada sin ambigüedad la notación $-a$.

### Producto

**Asociatividad**

$$
(ab)c=a(bc).
$$

**Conmutatividad**

$$
ab=ba.
$$

**Elemento neutro multiplicativo**

Existe un elemento $1\in F$, distinto de $0$, tal que

$$
a\cdot1=a.
$$

**Inverso multiplicativo**

Para cada $a\in F$ con $a\neq0$ existe algún $b\in F$ tal que

$$
ab=1.
$$

También aquí la unicidad será una consecuencia; después podremos escribir ese inverso como $a^{-1}$.

### Compatibilidad entre suma y producto

**Distributividad**

$$
a(b+c)=ab+ac.
$$
:::

La condición

$$
0\neq1
$$

es indispensable. Sin ella, la estructura colapsaría en el sistema de un único elemento y perderíamos la aritmética que queremos modelar.

::: {.ma-block .ma-error}
**Error frecuente**

No todos los enunciados familiares acerca de números aparecen en la lista de axiomas.

Por ejemplo,

$$
0a=0,
\qquad
(-a)b=-(ab),
\qquad
ab=0\Longrightarrow a=0\text{ o }b=0
$$

**no se han supuesto**.

Tenemos que demostrarlos.
:::

## 3. Axioma no significa «regla arbitraria»

Un axioma es un punto de partida declarado dentro de una teoría. La pregunta matemática importante es qué puede deducirse de él junto con los demás axiomas.

Por ejemplo, el axioma del neutro aditivo afirma que **existe** un elemento $0$ que deja invariantes las sumas:

$$
a+0=a.
$$

Pero el axioma no dice explícitamente que solo pueda existir uno. La unicidad será una consecuencia.

Esta diferencia entre existencia y unicidad enlaza directamente con el método desarrollado en [*Leer y escribir matemáticas*](../libros/capitulos/leer-y-escribir-matematicas-proposiciones-cuantificadores-y-demostraciones.md) (`MA-BCH-0001`):

$$
\text{«existe»}
\quad\text{y}\quad
\text{«existe uno solo»}
$$

son afirmaciones distintas.

## 4. Unicidad de los elementos neutros {#res-ma-con-0020-unicidad}

### 4.1. El cero es único

Supongamos que $0$ y $0'$ satisfacen ambos la propiedad de ser neutros aditivos.

Como $0'$ es neutro,

$$
0+0'=0.
$$

Como $0$ también es neutro,

$$
0+0'=0'.
$$

Por tanto,

$$
\boxed{0=0'}.
$$

Hemos demostrado que el neutro aditivo es único.

::: {.ma-block .ma-comprobacion}
**Lectura de la prueba**

La demostración no utilizó números concretos. Solo utilizó la propiedad que define a un neutro aditivo.

La estrategia fue típica de una prueba de unicidad:

1. suponer dos candidatos;
2. explotar la propiedad que ambos satisfacen;
3. demostrar que necesariamente coinciden.
:::

### 4.2. El uno es único

El argumento es análogo.

Supongamos que $1$ y $1'$ son neutros multiplicativos. Entonces

$$
1\cdot1'=1
$$

porque $1'$ es neutro, y también

$$
1\cdot1'=1'
$$

porque $1$ es neutro.

Por tanto,

$$
\boxed{1=1'}.
$$

Así, el neutro multiplicativo también es único.

## 5. Unicidad de los inversos

### 5.1. El inverso aditivo de cada elemento es único

Sea $a\in F$. Supongamos que $b$ y $c$ son ambos inversos aditivos de $a$:

$$
a+b=0
\qquad\text{y}\qquad
a+c=0.
$$

Entonces

$$
\begin{aligned}
b
&=b+0\\
&=b+(a+c)\\
&=(b+a)+c\\
&=0+c\\
&=c.
\end{aligned}
$$

Por tanto,

$$
\boxed{b=c}.
$$

Esto justifica que podamos escribir **el** inverso aditivo de $a$ y denotarlo sin ambigüedad por

$$
-a.
$$

### 5.2. El inverso multiplicativo de un elemento no nulo es único

Sea $a\neq0$. Supongamos que $b$ y $c$ satisfacen

$$
ab=1
\qquad\text{y}\qquad
ac=1.
$$

Entonces

$$
\begin{aligned}
b
&=b\cdot1\\
&=b(ac)\\
&=(ba)c\\
&=1\cdot c\\
&=c.
\end{aligned}
$$

Por tanto, el inverso multiplicativo de $a$ es único:

$$
\boxed{b=c}.
$$

Podemos escribirlo sin ambigüedad como

$$
a^{-1}.
$$

A partir de ahora definimos además la **resta** por

$$
a-b:=a+(-b).
$$

Por tanto, restar $b$ significa sumar su inverso aditivo.

::: {.ma-block .ma-observacion}
**Una consecuencia de lenguaje**

Las notaciones

$$
-a
\qquad\text{y}\qquad
a^{-1}
$$

no son simples convenciones gráficas.

Su uso presupone que los objetos designados existen bajo las hipótesis adecuadas y que son únicos.
:::

## 6. El cero absorbe el producto {#res-ma-con-0020-cero}

Ahora demostraremos una regla elemental que no figuraba entre los axiomas:

$$
\boxed{0a=0}.
$$

Sea $a\in F$. Por distributividad,

$$
(0+0)a=0a+0a.
$$

Pero, como $0+0=0$,

$$
0a=0a+0a.
$$

Sumemos el inverso aditivo de $0a$ a ambos miembros:

$$
0a+(-(0a))
=
(0a+0a)+(-(0a)).
$$

El miembro izquierdo es $0$. En el derecho, usando asociatividad,

$$
(0a+0a)+(-(0a))
=
0a+\bigl(0a+(-(0a))\bigr)
=
0a+0
=
0a.
$$

Por tanto,

$$
\boxed{0=0a}.
$$

Como el producto es conmutativo,

$$
\boxed{a0=0}.
$$

::: {.ma-block .ma-comprobacion}
**Qué se usó**

La identidad $0a=0$ se dedujo de:

- el neutro aditivo;
- la existencia de inversos aditivos;
- la asociatividad;
- la distributividad.

No necesitamos ninguna propiedad de orden.
:::

## 7. El cero no puede tener inverso multiplicativo

Supongamos, para obtener una contradicción, que existiera $c\in F$ tal que

$$
0c=1.
$$

Pero acabamos de demostrar que

$$
0c=0.
$$

Luego tendríamos

$$
0=1,
$$

contradiciendo el axioma

$$
0\neq1.
$$

Por tanto,

$$
\boxed{\text{$0$ no tiene inverso multiplicativo}.}
$$

Ésta es la razón estructural por la que no existe división por cero en un cuerpo.

## 8. Reglas de signos como consecuencias

### 8.1. Multiplicar por $-1$

Queremos demostrar

$$
(-1)a=-a.
$$

Observemos:

$$
a+(-1)a
=
1a+(-1)a
=
(1+(-1))a
=
0a
=
0.
$$

Por tanto, $(-1)a$ es un inverso aditivo de $a$. Como ese inverso es único,

$$
\boxed{(-1)a=-a}.
$$

### 8.2. Mover un signo menos de un factor

Queremos demostrar

$$
(-a)b=-(ab).
$$

Tenemos

$$
ab+(-a)b
=
(a+(-a))b
=
0b
=
0.
$$

Así, $(-a)b$ es el inverso aditivo de $ab$. Por unicidad,

$$
\boxed{(-a)b=-(ab)}.
$$

Análogamente,

$$
\boxed{a(-b)=-(ab)}.
$$

### 8.3. Producto de dos negativos

Aplicando dos veces la regla anterior,

$$
(-a)(-b)
=
-\bigl(a(-b)\bigr)
=
-(-(ab)).
$$

Como el inverso aditivo del inverso aditivo de $ab$ es $ab$,

$$
\boxed{(-a)(-b)=ab}.
$$

::: {.ma-block .ma-intuicion}
**Qué significa realmente «menos por menos es más»**

La regla

$$
(-a)(-b)=ab
$$

no necesita memorizarse como una excepción misteriosa.

Es una consecuencia forzada por la distributividad y por la estructura de inversos aditivos.
:::

### 8.4. Doble negación

Como

$$
a+(-a)=0,
$$

el elemento $a$ es un inverso aditivo de $-a$. Por unicidad,

$$
\boxed{-(-a)=a}.
$$

En particular,

$$
\boxed{-0=0}.
$$

## 9. Cancelación aditiva {#res-ma-con-0020-cancelacion}

Supongamos que

$$
a+c=b+c.
$$

Sumando $-c$ a ambos miembros,

$$
(a+c)+(-c)=(b+c)+(-c).
$$

Por asociatividad,

$$
a+(c+(-c))=b+(c+(-c)).
$$

Así,

$$
a+0=b+0,
$$

y por tanto

$$
\boxed{a=b}.
$$

Hemos demostrado la **ley de cancelación aditiva**:

$$
\boxed{
a+c=b+c
\Longrightarrow
a=b.
}
$$

La implicación recíproca también es inmediata: si $a=b$, entonces $a+c=b+c$. Por tanto,

$$
\boxed{
a+c=b+c
\Longleftrightarrow
a=b.
}
$$

::: {.ma-block .ma-metodo}
**Método — cancelar no es borrar símbolos**

Cuando «cancelamos» una misma suma en ambos miembros, la justificación real es:

1. sumar el inverso aditivo;
2. reagrupar mediante asociatividad;
3. usar el neutro.

La notación abreviada es legítima porque existe esta demostración estructural detrás.
:::

## 10. Cancelación multiplicativa

Supongamos

$$
ac=bc
$$

y, además,

$$
c\neq0.
$$

Como $c\neq0$, existe $c^{-1}$. Multiplicamos ambos miembros por $c^{-1}$:

$$
(ac)c^{-1}=(bc)c^{-1}.
$$

Por asociatividad,

$$
a(cc^{-1})=b(cc^{-1}).
$$

Así,

$$
a\cdot1=b\cdot1,
$$

y concluimos

$$
\boxed{a=b}.
$$

Por tanto,

$$
\boxed{
ac=bc,\ c\neq0
\Longrightarrow
a=b.
}
$$

::: {.ma-block .ma-error}
**Error frecuente — cancelar cero**

La hipótesis $c\neq0$ es esencial.

Si $c=0$, entonces

$$
ac=0=bc
$$

para **cualesquiera** $a,b\in F$.

Por ejemplo,

$$
0\cdot0=1\cdot0,
$$

pero

$$
0\neq1.
$$

No podemos cancelar un factor cuyo inverso multiplicativo no existe.
:::

## 11. La propiedad del producto nulo {#res-ma-con-0020-producto-nulo}

Una de las reglas más importantes del álgebra elemental afirma:

$$
ab=0
\Longrightarrow
a=0\text{ o }b=0.
$$

En un cuerpo, esta propiedad es una consecuencia de la existencia de inversos multiplicativos.

Supongamos

$$
ab=0.
$$

Si $a=0$, ya tenemos una de las alternativas.

Supongamos entonces

$$
a\neq0.
$$

Existe $a^{-1}$. Multiplicamos la igualdad por $a^{-1}$:

$$
a^{-1}(ab)=a^{-1}0.
$$

Por asociatividad y por la propiedad $a^{-1}0=0$,

$$
(a^{-1}a)b=0.
$$

Por tanto,

$$
1b=0,
$$

y concluimos

$$
b=0.
$$

Así,

$$
\boxed{
ab=0
\Longrightarrow
a=0\text{ o }b=0.
}
$$

La recíproca es inmediata porque $0$ absorbe el producto. Por tanto,

$$
\boxed{
ab=0
\Longleftrightarrow
a=0\text{ o }b=0.
}
$$

::: {.ma-block .ma-observacion}
**Por qué importa**

La factorización de ecuaciones funciona porque podemos combinar

$$
uv=0
$$

con la propiedad de producto nulo y transformar una ecuación multiplicativa en dos alternativas:

$$
u=0
\qquad\text{o}\qquad
v=0.
$$

Ésta es la estructura que sostiene buena parte del álgebra de polinomios.
:::

## 12. Qué significa dividir {#met-ma-con-0020-division}

En un cuerpo, la división por un elemento no nulo no necesita introducirse como una tercera operación independiente.

Si

$$
b\neq0,
$$

definimos

$$
\boxed{
\frac{a}{b}=ab^{-1}.
}
$$

Así, dividir por $b$ significa multiplicar por su inverso.

La condición

$$
b\neq0
$$

no es un detalle técnico. Es exactamente la condición que garantiza la existencia de $b^{-1}$.

::: {.ma-block .ma-dominio}
**Dominio de la división**

La expresión

$$
\frac ab
$$

está definida en un cuerpo únicamente cuando

$$
b\neq0.
$$

Antes de cancelar denominadores o multiplicar por sus inversos, hay que controlar esta hipótesis.
:::

### Una equivalencia útil

Si $b\neq0$, entonces

$$
x=\frac ab
$$

equivale a

$$
bx=a.
$$

En efecto,

$$
x=ab^{-1}
$$

implica

$$
bx=b(ab^{-1})=a(bb^{-1})=a.
$$

Y si $bx=a$, multiplicar por $b^{-1}$ da

$$
x=b^{-1}a=ab^{-1}=\frac ab.
$$

## 13. Resolver una ecuación lineal usando la estructura de cuerpo

Consideremos

$$
ax=b,
$$

con

$$
a,b\in F.
$$

La respuesta depende de si $a$ es nulo.

### Caso 1: $a\neq0$

Como $a^{-1}$ existe,

$$
ax=b
$$

implica

$$
a^{-1}(ax)=a^{-1}b.
$$

Por asociatividad,

$$
(a^{-1}a)x=a^{-1}b,
$$

de modo que

$$
x=a^{-1}b.
$$

Por tanto,

$$
\boxed{
x=\frac ba.
}
$$

### Existencia

Definamos

$$
x=a^{-1}b.
$$

Entonces

$$
ax=a(a^{-1}b)=(aa^{-1})b=b.
$$

Así, existe una solución.

### Unicidad

Supongamos que $u$ y $v$ satisfacen

$$
au=b
\qquad\text{y}\qquad
av=b.
$$

Entonces

$$
au=av.
$$

Como $a\neq0$, la cancelación multiplicativa da

$$
u=v.
$$

Por tanto:

$$
\boxed{
a\neq0
\Longrightarrow
\text{$ax=b$ tiene una única solución, }x=\frac ba.
}
$$

Este resultado proporciona la justificación estructural de la técnica escolar de «dividir ambos miembros por $a$».

### Caso 2: $a=0$ y $b=0$

La ecuación queda

$$
0x=0,
$$

que es verdadera para todo $x\in F$.

Por tanto, hay tantas soluciones como elementos tenga $F$.

### Caso 3: $a=0$ y $b\neq0$

La ecuación queda

$$
0x=b.
$$

Pero $0x=0$. Así tendríamos que exigir

$$
0=b,
$$

lo que contradice $b\neq0$.

No hay solución.

::: {.ma-block .ma-metodo}
**Método — ecuaciones lineales con parámetro**

Para analizar

$$
ax=b,
$$

no dividas inmediatamente por $a$.

Primero separa:

1. $a\neq0$: existe $a^{-1}$ y hay una solución única;
2. $a=0$, $b=0$: todo elemento es solución;
3. $a=0$, $b\neq0$: no hay solución.

La clasificación depende de la disponibilidad del inverso.
:::

Esta estructura refuerza la lectura del problema [Existencia y unicidad en una ecuación lineal con parámetros](../problemas/existencia-y-unicidad-ecuacion-lineal-parametros.md) (`MA-PRB-0005`).

## 14. Ejemplos y no ejemplos de cuerpos

### 14.1. Ejemplos

Con sus operaciones usuales,

$$
\mathbb Q,\qquad \mathbb R,\qquad \mathbb C
$$

son cuerpos.

Por ahora podemos tratarlos como ejemplos conocidos. Una construcción rigurosa de $\mathbb Q$ y una caracterización estructural más completa de $\mathbb R$ pertenecen a etapas posteriores del recorrido.

### 14.2. Los enteros no forman un cuerpo

El conjunto

$$
\mathbb Z
$$

tiene suma y producto con muchas de las propiedades anteriores, pero falla el axioma de inversos multiplicativos.

Por ejemplo, $2\neq0$, pero no existe un entero $m$ tal que

$$
2m=1.
$$

Por tanto,

$$
\boxed{\mathbb Z\text{ no es un cuerpo}.}
$$

::: {.ma-block .ma-observacion}
**No basta con poder sumar y multiplicar**

Una estructura puede satisfacer asociatividad, conmutatividad, neutros, inversos aditivos y distributividad, y aun así no ser un cuerpo si los elementos no nulos no poseen inversos multiplicativos dentro del mismo conjunto.
:::

## 15. Qué NO se deduce todavía

Los axiomas de cuerpo organizan la aritmética de suma, producto e inversos. Pero no permiten, por sí solos, hablar de:

- qué elemento es mayor que otro;
- qué significa $a>0$;
- intervalos;
- desigualdades;
- cotas superiores;
- supremos;
- continuidad o límites;
- completitud.

Para obtener reglas de orden necesitamos añadir una relación de orden compatible con las operaciones.

Por eso, aunque en [Propiedades del orden en $\mathbb R$ y manipulación de desigualdades](propiedades-del-orden-en-r-y-manipulacion-de-desigualdades.md) (`MA-CON-0005`) ya usamos operacionalmente esas propiedades, la arquitectura fundacional completa debe distinguir dos capas:

$$
\boxed{
\text{cuerpo}
\longrightarrow
\text{cuerpo ordenado}.
}
$$

Y, en el caso de los reales, todavía falta una tercera capa:

$$
\boxed{
\text{cuerpo ordenado}
\longrightarrow
\text{cuerpo ordenado completo}.
}
$$

La completitud ya está desarrollada en [Supremo, ínfimo y completitud de $\mathbb R$](supremo-infimo-y-completitud-de-r.md) (`MA-CON-0016`).

## 16. Un mapa de dependencias algebraicas

La lógica interna de esta página puede visualizarse así:

$$
\begin{array}{c}
\text{axiomas de suma y producto}\\
\downarrow\\
\text{unicidad de }0,1,-a,a^{-1}\\
\downarrow\\
0a=0,\quad (-a)b=-(ab),\quad (-a)(-b)=ab\\
\downarrow\\
\text{cancelación}\\
\downarrow\\
\text{producto nulo y división}\\
\downarrow\\
\text{ecuaciones lineales}
\end{array}
$$

La dirección importa: cuando una consecuencia aparece abajo, no debe utilizarse circularmente para demostrar los hechos de los que depende.

::: {.ma-block .ma-comprobacion}
**Auditoría de dependencias**

En particular:

- para demostrar $0a=0$ no usamos producto nulo;
- para demostrar producto nulo usamos inversos y $0a=0$;
- para justificar división usamos la existencia y unicidad de inversos;
- para resolver $ax=b$ con $a\neq0$ usamos precisamente esa noción de división o, equivalentemente, multiplicamos por $a^{-1}$.
:::

## 17. Conexiones con el corpus

Esta página llena una pieza que hasta ahora estaba implícita.

- [`MA-BCH-0001`](../libros/capitulos/leer-y-escribir-matematicas-proposiciones-cuantificadores-y-demostraciones.md) proporciona el lenguaje de axiomas, demostraciones, existencia y unicidad.
- [`MA-CON-0005`](propiedades-del-orden-en-r-y-manipulacion-de-desigualdades.md) utiliza la capa adicional de orden sobre $\mathbb R$.
- [`MA-CON-0016`](supremo-infimo-y-completitud-de-r.md) introduce la propiedad de completitud que distingue a $\mathbb R$ dentro del recorrido analítico.
- [`MA-PRB-0005`](../problemas/existencia-y-unicidad-ecuacion-lineal-parametros.md) aplica la estructura de existencia y unicidad a una ecuación lineal.
- [`MA-PRB-0006`](../problemas/producto-nulo-y-cancelacion-en-un-cuerpo.md) ejercita directamente producto nulo, cancelación e hipótesis de no nulidad.

La secuencia fundacional queda ahora:

$$
\boxed{
\text{lenguaje de demostración}
\longrightarrow
\text{axiomas de cuerpo}
\longrightarrow
\text{orden}
\longrightarrow
\text{completitud}.
}
$$

## 18. Resumen operativo

En cualquier cuerpo $F$:

$$
\boxed{
\begin{aligned}
0a&=0,\\
(-1)a&=-a,\\
(-a)b&=-(ab),\\
(-a)(-b)&=ab,\\
a+c=b+c&\Longrightarrow a=b,\\
ac=bc,\ c\neq0&\Longrightarrow a=b,\\
ab=0&\Longleftrightarrow a=0\text{ o }b=0,\\
\frac ab&=ab^{-1}\qquad(b\neq0).
\end{aligned}
}
$$

Y para

$$
ax=b,
$$

tenemos:

$$
\boxed{
\begin{array}{c|c}
\text{condición} & \text{soluciones}\\
\hline
a\neq0 & x=a^{-1}b=b/a\text{, única}\\
a=0,\ b=0 & \text{todo }x\in F\\
a=0,\ b\neq0 & \text{ninguna}
\end{array}
}
$$

::: {.ma-block .ma-intuicion}
**Idea final**

Las reglas algebraicas escolares dejan de verse como una colección de permisos aislados cuando identificamos la estructura que las sostiene.

El siguiente paso fundacional será añadir una relación de orden compatible con suma y producto y estudiar qué nuevas consecuencias aparecen entonces.
:::

## Relaciones

- **Prerrequisitos:** `MA-BCH-0001`.
- **Contenidos relacionados:** `MA-CON-0005`, `MA-CON-0016`.
- **Problemas que usan este concepto:** `MA-PRB-0006`.
