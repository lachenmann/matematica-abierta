---
title: "Funciones reales: estructura, composición, inversas y gráficas"
description: "Tercer capítulo de Cálculo para matemáticos: funciones como objetos completos, imágenes y preimágenes, inyectividad, sobreyectividad, composición, inversas, gráficas y monotonía."
content-id: MA-BCH-0004
content-type: book-chapter
collection: PM-CAL
book-id: MA-BOK-0001
status: published
date-created: 2026-09-09
date-modified: 2026-09-09
areas:
  - fundamentos
  - calculo
  - analisis
level: fundamental
topics:
  - funciones
  - dominio
  - codominio
  - imagen
  - preimagen
  - inyectividad
  - sobreyectividad
  - biyectividad
  - composicion
  - identidad
  - funcion-inversa
  - graficas
  - funciones-por-tramos
  - transformaciones-de-graficas
  - monotonia
prerequisites:
  - MA-BCH-0001
  - MA-BCH-0003
related:
  - MA-CON-0006
  - MA-CON-0007
  - MA-CON-0008
  - MA-CON-0009
  - MA-CON-0010
  - MA-BOK-0001
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Funciones reales

En la matemática escolar una función suele aparecer junto a una fórmula:

$$
f(x)=x^2,
\qquad
f(x)=\frac1x,
\qquad
f(x)=\sqrt{x}.
$$

Para calcular valores, esa asociación puede resultar suficiente. Para hacer análisis, no lo es. Una función no queda determinada por una expresión aislada: necesitamos saber **qué entradas admite**, **en qué conjunto declaramos sus salidas** y **qué regla asigna una única salida a cada entrada**.

La pregunta rectora de este capítulo será

$$
\boxed{\text{¿qué información necesitamos para saber realmente qué función tenemos delante?}}
$$

El recorrido irá desde la definición completa de función hasta imágenes, preimágenes, composición, inversas, gráficas y monotonía. El objetivo no es acumular vocabulario, sino aprender a reconocer la estructura funcional que más adelante sostendrá sucesiones, límites, continuidad y derivación.

::: {.ma-block .ma-intuicion}
**Idea rectora**

Antes de manipular una fórmula, conviene separar cuatro preguntas:

1. ¿cuál es el dominio de la función?;
2. ¿cuál es su codominio?;
3. ¿qué valores alcanza realmente?;
4. ¿qué propiedades dependen de esos datos y no solamente de la fórmula?

La misma expresión algebraica puede definir funciones matemáticamente distintas.
:::

## 1. Una fórmula no es todavía una función {#ma-bch-0004-funcion-completa}

Consideremos la regla $x\mapsto x^2$ en cuatro declaraciones:

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2,
$$

$$
g\colon[0,\infty)\to[0,\infty),
\qquad
g(x)=x^2,
$$

$$
h\colon\mathbb R\to[0,\infty),
\qquad
h(x)=x^2,
$$

y

$$
k\colon[0,\infty)\to\mathbb R,
\qquad
k(x)=x^2.
$$

La fórmula es la misma, pero dominio y codominio cambian. Por ejemplo, $f(-2)$ está definido, mientras que $g(-2)$ y $k(-2)$ no lo están. Del mismo modo, $f$ declara como posibles salidas todos los reales, aunque ningún número negativo sea un cuadrado.

::: {#res-ma-bch-0004-def-funcion}
### Definición — función, dominio, codominio e imagen

Sean $A$ y $B$ conjuntos. Una **función**

$$
f\colon A\to B
$$

asigna a cada $x\in A$ exactamente un elemento $f(x)\in B$.

El conjunto $A$ es el **dominio** y $B$ el **codominio**. La **imagen** o **recorrido** de $f$ es

$$
\operatorname{Im}(f)
=
\{f(x):x\in A\}.
$$

Siempre se cumple

$$
\operatorname{Im}(f)\subseteq B.
$$
:::

Las palabras «cada» y «exactamente uno» expresan dos exigencias distintas:

$$
\forall x\in A\;\exists!y\in B
\quad\text{tal que}\quad y=f(x).
$$

Una regla puede fallar porque alguna entrada no tenga salida. Por ejemplo,

$$
r\colon\mathbb R\to\mathbb R,
\qquad
r(x)=\frac1x
$$

no define una función sobre todo $\mathbb R$, porque la expresión no tiene valor real en $x=0$.

También puede fallar la unicidad. La instrucción «a cada $x\ge0$ asígnele un real $y$ con $y^2=x$» no define una función hacia $\mathbb R$, pues para $x=4$ sirven $2$ y $-2$. En cambio, el teorema de existencia y unicidad de raíces positivas del capítulo anterior permite definir

$$
s\colon[0,\infty)\to[0,\infty),
\qquad
s(x)=\sqrt{x}.
$$

::: {.ma-block .ma-error}
**Error frecuente — Confundir unicidad de la salida con inyectividad**

Ser función significa que **una entrada no puede tener dos salidas**.

Ser inyectiva significará algo diferente: **dos entradas distintas no pueden compartir una salida**.
:::

### Dominio, codominio e imagen

Para

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2,
$$

tenemos

$$
\operatorname{Dom}(f)=\mathbb R,
\qquad
\operatorname{Cod}(f)=\mathbb R,
\qquad
\operatorname{Im}(f)=[0,\infty).
$$

El codominio forma parte de la declaración de la función; la imagen registra las salidas que se alcanzan efectivamente.

En esta obra adoptaremos la convención de que **dominio, codominio y regla de asignación forman parte de los datos de una función**. Por tanto, las cuatro funciones $f,g,h,k$ anteriores son objetos diferentes.

Si $E\subseteq A$, la **restricción** de $f\colon A\to B$ a $E$ es

$$
f|_E\colon E\to B,
\qquad
f|_E(x)=f(x).
$$

Restringir el dominio puede cambiar propiedades de la función aun cuando los valores conservados sigan siendo los mismos.

El desarrollo autónomo de estas distinciones está en [Funciones reales: dominio, codominio, imagen y preimagen](../../conceptos/funciones-reales-dominio-codominio-imagen-y-preimagen.md) (`MA-CON-0007`).

## 2. Imágenes y preimágenes de conjuntos {#ma-bch-0004-imagen-preimagen}

Una función actúa sobre puntos, pero también induce operaciones naturales entre subconjuntos.

Sea

$$
f\colon A\to B.
$$

Si $E\subseteq A$, su **imagen directa** es

$$
\boxed{f(E)=\{f(x):x\in E\}.}
$$

Si $F\subseteq B$, su **preimagen** es

$$
\boxed{f^{-1}(F)=\{x\in A:f(x)\in F\}.}
$$

La imagen avanza desde entradas hacia salidas; la preimagen parte de una condición sobre las salidas y recupera todas las entradas que la satisfacen.

Por ejemplo, para

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2,
$$

tenemos

$$
f([-2,1])=[0,4]
$$

y

$$
f^{-1}([1,4])=[-2,-1]\cup[1,2].
$$

En el segundo cálculo no hemos «invertido» la función $x^2$. Hemos resuelto la condición

$$
1\le x^2\le4.
$$

::: {.ma-block .ma-observacion}
**La preimagen no exige una función inversa**

La notación $f^{-1}(F)$ para un conjunto $F\subseteq B$ está definida para **toda** función $f\colon A\to B$.

Una verdadera función inversa $f^{-1}\colon B\to A$ solo existirá bajo hipótesis adicionales. El contexto distingue ambos usos de la notación.
:::

Dos identidades elementales ayudan a controlar los tipos:

$$
f(A)=\operatorname{Im}(f),
\qquad
f^{-1}(B)=A.
$$

Resolver una ecuación puede reinterpretarse como calcular una preimagen. Si $y\in B$, entonces

$$
f(x)=y
$$

equivale a preguntar por los elementos de

$$
f^{-1}(\{y\}).
$$

Esta perspectiva prepara directamente las nociones de inyectividad y sobreyectividad.

## 3. Inyectividad, sobreyectividad y biyectividad {#ma-bch-0004-biyectividad}

Sea $f\colon A\to B$.

::: {#res-ma-bch-0004-def-biyectividad}
### Definición — tres propiedades fundamentales

La función $f$ es **inyectiva** si

$$
f(x_1)=f(x_2)
\Longrightarrow
x_1=x_2
$$

para cualesquiera $x_1,x_2\in A$.

Es **sobreyectiva** si

$$
\forall y\in B\;\exists x\in A
\quad\text{tal que}\quad
f(x)=y.
$$

Equivalentemente,

$$
f(A)=B.
$$

Es **biyectiva** si es simultáneamente inyectiva y sobreyectiva.
:::

Las arquitecturas de prueba son distintas:

- para demostrar inyectividad, solemos comenzar suponiendo $f(x_1)=f(x_2)$ y tratamos de deducir $x_1=x_2$;
- para demostrar sobreyectividad, fijamos un $y\in B$ arbitrario y construimos un antecedente $x\in A$ con $f(x)=y$.

Para refutar inyectividad basta exhibir dos entradas distintas con la misma salida. Para refutar sobreyectividad basta exhibir un elemento del codominio que no se alcance.

### La misma fórmula y cuatro clasificaciones

Volvamos a $x^2$:

| Función | Inyectiva | Sobreyectiva | Biyectiva |
|---|:---:|:---:|:---:|
| $f\colon\mathbb R\to\mathbb R$ | no | no | no |
| $g\colon[0,\infty)\to[0,\infty)$ | sí | sí | sí |
| $h\colon\mathbb R\to[0,\infty)$ | no | sí | no |
| $k\colon[0,\infty)\to\mathbb R$ | sí | no | no |

La sobreyectividad de $g$ y $h$ usa una herramienta del capítulo anterior: para todo $y\ge0$ existe $\sqrt y\ge0$ con

$$
(\sqrt y)^2=y.
$$

La inyectividad de $g$ y $k$ se obtiene porque, para $x_1,x_2\ge0$,

$$
x_1^2=x_2^2
\Longrightarrow
(x_1-x_2)(x_1+x_2)=0.
$$

Como $x_1+x_2\ge0$, la única posibilidad compatible con dos números no negativos distintos de signo opuesto queda excluida; por tanto $x_1=x_2$.

::: {.ma-block .ma-intuicion}
**Dos sensibilidades diferentes**

La inyectividad detecta **colisiones entre entradas** y depende de manera decisiva del dominio.

La sobreyectividad pregunta si se alcanza **todo el codominio** y depende de manera decisiva de cuál sea ese codominio.
:::

Consulta también [Inyectividad, sobreyectividad y biyectividad](../../conceptos/inyectividad-sobreyectividad-y-biyectividad.md) (`MA-CON-0009`).

## 4. Composición e identidad {#ma-bch-0004-composicion}

Muchas operaciones del cálculo se realizan por etapas. Si

$$
f\colon A\to B,
\qquad
g\colon B\to C,
$$

podemos aplicar primero $f$ y después $g$.

::: {#res-ma-bch-0004-def-composicion}
### Definición — composición

La **composición** de $g$ con $f$ es la función

$$
g\circ f\colon A\to C
$$

dada por

$$
\boxed{(g\circ f)(x)=g(f(x)).}
$$
:::

El orden de lectura es de derecha a izquierda: primero actúa $f$, después $g$.

Cuando las funciones se presentan mediante fórmulas con dominios que no coinciden automáticamente, la auditoría de tipos es indispensable. El dominio máximo de la expresión compuesta es

$$
\{x\in\operatorname{Dom}(f):f(x)\in\operatorname{Dom}(g)\}.
$$

Por ejemplo, si

$$
f(x)=x^2-1,
\qquad
g(t)=\sqrt t,
$$

entonces

$$
(g\circ f)(x)=\sqrt{x^2-1}
$$

solo está definida para

$$
|x|\ge1.
$$

### La composición no es conmutativa

Aun cuando ambas composiciones existan, en general

$$
g\circ f\ne f\circ g.
$$

Por ejemplo, para

$$
f(x)=x+1,
\qquad
g(x)=x^2,
$$

tenemos

$$
(g\circ f)(x)=(x+1)^2,
$$

mientras que

$$
(f\circ g)(x)=x^2+1.
$$

### Asociatividad

Si

$$
f\colon A\to B,
\qquad
g\colon B\to C,
\qquad
h\colon C\to D,
$$

entonces

$$
\boxed{h\circ(g\circ f)=(h\circ g)\circ f.}
$$

En efecto, para todo $x\in A$,

$$
[h\circ(g\circ f)](x)
=h(g(f(x)))
=[(h\circ g)\circ f](x).
$$

Las dos funciones tienen el mismo dominio, el mismo codominio y los mismos valores; por tanto son iguales.

### Identidad

Para todo conjunto $A$, la función identidad es

$$
\operatorname{id}_A\colon A\to A,
\qquad
\operatorname{id}_A(x)=x.
$$

Si $f\colon A\to B$, entonces

$$
\boxed{
\operatorname{id}_B\circ f=f
=f\circ\operatorname{id}_A.
}
$$

La posición de cada identidad está determinada por los tipos.

::: {#res-ma-bch-0004-composicion-propiedades}
### Proposición — propiedades que se conservan al componer

Sean

$$
f\colon A\to B,
\qquad
g\colon B\to C.
$$

1. Si $f$ y $g$ son inyectivas, entonces $g\circ f$ es inyectiva.
2. Si $f$ y $g$ son sobreyectivas, entonces $g\circ f$ es sobreyectiva.
3. Si $f$ y $g$ son biyectivas, entonces $g\circ f$ es biyectiva.
:::

### Demostración

Para la primera afirmación, supongamos

$$
(g\circ f)(x_1)=(g\circ f)(x_2).
$$

Entonces

$$
g(f(x_1))=g(f(x_2)).
$$

La inyectividad de $g$ implica $f(x_1)=f(x_2)$ y la de $f$ implica $x_1=x_2$.

Para la segunda, sea $z\in C$. Como $g$ es sobreyectiva, existe $y\in B$ con $g(y)=z$. Como $f$ es sobreyectiva, existe $x\in A$ con $f(x)=y$. Entonces

$$
(g\circ f)(x)=g(f(x))=g(y)=z.
$$

La tercera afirmación combina las dos anteriores. $\square$

El tratamiento modular de esta operación está en [Composición de funciones e identidad](../../conceptos/composicion-de-funciones-e-identidad.md) (`MA-CON-0008`).

## 5. Funciones inversas {#ma-bch-0004-inversas}

Invertir una función significa poder deshacerla mediante composición.

::: {#res-ma-bch-0004-def-inversa}
### Definición — función inversa

Sea $f\colon A\to B$. Una función

$$
g\colon B\to A
$$

es una **inversa** de $f$ si

$$
g\circ f=\operatorname{id}_A
$$

y

$$
f\circ g=\operatorname{id}_B.
$$

Cuando existe, se denota por $f^{-1}$.
:::

La existencia de una inversa exige exactamente dos cosas: que cada salida de $B$ tenga antecedente y que ese antecedente sea único.

::: {#res-ma-bch-0004-inversa-biyectiva}
### Teorema — una función es invertible si y solo si es biyectiva

Sea $f\colon A\to B$. Existe una función inversa

$$
f^{-1}\colon B\to A
$$

si y solo si $f$ es biyectiva.
:::

### Demostración

Supongamos primero que existe $f^{-1}$. Si

$$
f(x_1)=f(x_2),
$$

aplicamos $f^{-1}$ a ambos lados:

$$
f^{-1}(f(x_1))=f^{-1}(f(x_2)),
$$

y obtenemos $x_1=x_2$. Luego $f$ es inyectiva.

Ahora sea $y\in B$. Tomemos

$$
x=f^{-1}(y).
$$

Entonces

$$
f(x)=f(f^{-1}(y))=y,
$$

por lo que $f$ es sobreyectiva. Así, $f$ es biyectiva.

Recíprocamente, supongamos que $f$ es biyectiva. Para cada $y\in B$, la sobreyectividad garantiza que existe al menos un $x\in A$ con $f(x)=y$, y la inyectividad garantiza que ese $x$ es único. Definimos

$$
f^{-1}(y)=x.
$$

Por construcción,

$$
f^{-1}(f(x))=x
$$

para todo $x\in A$, y

$$
f(f^{-1}(y))=y
$$

para todo $y\in B$. Por tanto, $f^{-1}$ es una inversa de $f$. $\square$

La prueba también muestra que la inversa es única.

### Inversa de una composición

Si

$$
f\colon A\to B,
\qquad
g\colon B\to C
$$

son biyectivas, entonces

$$
\boxed{(g\circ f)^{-1}=f^{-1}\circ g^{-1}.}
$$

El orden se invierte porque, para deshacer la cadena

$$
A\xrightarrow{f}B\xrightarrow{g}C,
$$

primero debemos deshacer $g$ y después $f$.

### Cuadrado y raíz cuadrada

La función

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2
$$

no tiene inversa: no es inyectiva ni sobreyectiva. Pero su restricción

$$
g\colon[0,\infty)\to[0,\infty),
\qquad
g(x)=x^2
$$

sí es biyectiva. Su inversa es

$$
g^{-1}(y)=\sqrt y.
$$

La identidad

$$
\sqrt{x^2}=|x|
$$

explica por qué la raíz cuadrada no puede deshacer globalmente a $x^2$ sobre todo $\mathbb R$.

Consulta también [Funciones inversas](../../conceptos/funciones-inversas.md) (`MA-CON-0010`).

## 6. Álgebra de imágenes y preimágenes {#ma-bch-0004-algebra-imagenes}

Las operaciones de conjuntos estudiadas en el primer capítulo interactúan de manera distinta con imágenes y preimágenes.

Sean $E,F\subseteq A$ y $S,T\subseteq B$.

Para las imágenes directas siempre tenemos

$$
\boxed{f(E\cup F)=f(E)\cup f(F)}
$$

y

$$
\boxed{f(E\cap F)\subseteq f(E)\cap f(F).}
$$

La segunda inclusión puede ser estricta. Para

$$
f(x)=x^2,
\qquad
E=\{-1\},
\qquad
F=\{1\},
$$

tenemos

$$
E\cap F=\varnothing,
$$

de modo que

$$
f(E\cap F)=\varnothing,
$$

pero

$$
f(E)\cap f(F)=\{1\}.
$$

La razón lógica es importante: un elemento de $f(E)\cap f(F)$ puede provenir de **dos antecedentes distintos**, uno en $E$ y otro en $F$.

Si $f$ es inyectiva, esos dos antecedentes deben coincidir y recuperamos la igualdad:

$$
\boxed{
f\text{ inyectiva}
\Longrightarrow
f(E\cap F)=f(E)\cap f(F).
}
$$

Las preimágenes se comportan de manera más exacta. Siempre se cumple

$$
\boxed{f^{-1}(S\cup T)=f^{-1}(S)\cup f^{-1}(T),}
$$

$$
\boxed{f^{-1}(S\cap T)=f^{-1}(S)\cap f^{-1}(T),}
$$

$$
\boxed{f^{-1}(B\setminus S)=A\setminus f^{-1}(S),}
$$

y, por tanto,

$$
\boxed{f^{-1}(S\setminus T)=f^{-1}(S)\setminus f^{-1}(T).}
$$

Por ejemplo, para la intersección,

$$
\begin{aligned}
x\in f^{-1}(S\cap T)
&\iff f(x)\in S\cap T\\
&\iff f(x)\in S\ \text{y}\ f(x)\in T\\
&\iff x\in f^{-1}(S)\ \text{y}\ x\in f^{-1}(T)\\
&\iff x\in f^{-1}(S)\cap f^{-1}(T).
\end{aligned}
$$

Aquí no aparecen dos testigos que deban identificarse: toda la argumentación sigue al mismo elemento $x$.

Estas leyes conectan naturalmente con [Operaciones con conjuntos reales: unión, intersección, complemento y diferencia](../../conceptos/operaciones-con-conjuntos-reales.md) (`MA-CON-0006`).

## 7. Gráficas: representación y estructura {#ma-bch-0004-graficas}

Si $A,B\subseteq\mathbb R$ y $f\colon A\to B$, la **gráfica** de $f$ es

$$
\Gamma_f
=
\{(x,f(x)):x\in A\}
\subseteq A\times B.
$$

La primera coordenada registra una entrada y la segunda su salida.

Un subconjunto

$$
R\subseteq A\times B
$$

es la gráfica de una función $A\to B$ exactamente cuando

$$
\forall x\in A\;\exists!y\in B
\quad\text{tal que}\quad
(x,y)\in R.
$$

Éste es el contenido preciso del llamado **criterio de la recta vertical**: cada vertical correspondiente a una entrada del dominio debe encontrar exactamente un punto de la gráfica.

### Qué puede leerse de la gráfica

Las primeras coordenadas de $\Gamma_f$ recuperan el dominio:

$$
A=\{x:\exists y\ ((x,y)\in\Gamma_f)\}.
$$

Las segundas coordenadas recuperan la imagen:

$$
\operatorname{Im}(f)
=\{y:\exists x\ ((x,y)\in\Gamma_f)\}.
$$

La gráfica, sin información adicional, no determina un codominio mayor que la imagen. Dos funciones con la misma regla, el mismo dominio y codominios distintos pueden tener exactamente el mismo conjunto de puntos como gráfica.

### Horizontales, inyectividad y sobreyectividad

Una horizontal $y=b$ pregunta por las soluciones de

$$
f(x)=b.
$$

Por tanto:

- $f$ es inyectiva si cada horizontal corta la gráfica **a lo sumo una vez**;
- $f$ es sobreyectiva sobre el codominio $B$ si, para cada $b\in B$, la horizontal $y=b$ corta la gráfica **al menos una vez**.

La segunda afirmación no puede decidirse sin conocer el codominio declarado.

### Gráfica de la inversa

Si $f\colon A\to B$ es biyectiva, entonces

$$
(x,y)\in\Gamma_f
\iff
y=f(x)
\iff
x=f^{-1}(y)
\iff
(y,x)\in\Gamma_{f^{-1}}.
$$

Así, intercambiar las coordenadas transforma la gráfica de $f$ en la de $f^{-1}$. Geométricamente, esto corresponde a reflejar respecto de la diagonal $y=x$.

::: {.ma-block .ma-observacion}
**La gráfica no sustituye la definición completa**

Fórmula, tabla, algoritmo y gráfica son representaciones de una función. Ninguna de ellas debe hacer olvidar los datos de dominio y codominio.
:::

## 8. Funciones por tramos y transformaciones de gráficas {#ma-bch-0004-tramos-transformaciones}

Una función puede utilizar reglas distintas en distintas partes de su dominio. Supongamos

$$
f(x)=
\begin{cases}
f_1(x),&x\in A_1,\\
\vdots&\\
f_n(x),&x\in A_n.
\end{cases}
$$

Para que esta receta defina una función sobre $A$, deben cumplirse dos condiciones:

1. **cobertura:**
   $$
   A=A_1\cup\cdots\cup A_n;
   $$
2. **compatibilidad:** si $x\in A_i\cap A_j$, entonces
   $$
   f_i(x)=f_j(x).
   $$

No es obligatorio que los tramos sean disjuntos; lo obligatorio es que ningún punto quede sin salida y que ningún punto reciba dos salidas incompatibles.

El valor absoluto es el ejemplo básico:

$$
|x|=
\begin{cases}
x,&x\ge0,\\
-x,&x<0.
\end{cases}
$$

### Transformar una gráfica siguiendo sus puntos

Sea $f\colon D\to\mathbb R$ y supongamos que $(u,y)$ pertenece a su gráfica, es decir, $y=f(u)$.

Las transformaciones elementales pueden deducirse sin memorizar reglas aisladas:

$$
\begin{array}{ccl}
f(x)+c&:&(u,y)\mapsto(u,y+c),\\[4pt]
f(x-c)&:&(u,y)\mapsto(u+c,y),\\[4pt]
-f(x)&:&(u,y)\mapsto(u,-y),\\[4pt]
f(-x)&:&(u,y)\mapsto(-u,y).
\end{array}
$$

Si $a,b\ne0$, para

$$
g(x)=a f(bx)
$$

un punto $(u,y)$ de la gráfica de $f$ produce el punto

$$
\boxed{\left(\frac{u}{b},ay\right)}
$$

de la gráfica de $g$.

Pero la geometría no debe ocultar el dominio. Para $g(x)=a f(bx)$,

$$
\operatorname{Dom}(g)
=
\{x\in\mathbb R:bx\in D\}.
$$

::: {.ma-block .ma-error}
**Error frecuente — Transformar el dibujo antes de auditar la función**

Las modificaciones «dentro» de la fórmula pueden cambiar el dominio. El orden seguro es:

1. escribir la nueva función;
2. determinar su dominio;
3. calcular cómo cambian los puntos;
4. interpretar la geometría.
:::

## 9. Monotonía e inversas {#ma-bch-0004-monotonia}

La estructura de orden de $\mathbb R$ permite comparar entradas y salidas.

Sea $D\subseteq\mathbb R$ y $f\colon D\to\mathbb R$.

Decimos que $f$ es:

- **no decreciente** si $x_1<x_2$ implica $f(x_1)\le f(x_2)$;
- **no creciente** si $x_1<x_2$ implica $f(x_1)\ge f(x_2)$;
- **estrictamente creciente** si $x_1<x_2$ implica $f(x_1)<f(x_2)$;
- **estrictamente decreciente** si $x_1<x_2$ implica $f(x_1)>f(x_2)$.

::: {#res-ma-bch-0004-monotona-inyectiva}
### Teorema — la monotonía estricta implica inyectividad

Toda función estrictamente creciente o estrictamente decreciente es inyectiva.
:::

### Demostración

Supongamos primero que $f$ es estrictamente creciente. Sean $x_1,x_2\in D$ y supongamos

$$
f(x_1)=f(x_2).
$$

Si $x_1<x_2$, la monotonía estricta daría

$$
f(x_1)<f(x_2),
$$

contradicción. Si $x_2<x_1$, obtendríamos análogamente

$$
f(x_2)<f(x_1),
$$

otra contradicción. Por tricotomía, sólo queda $x_1=x_2$.

El caso estrictamente decreciente es idéntico con las desigualdades invertidas. $\square$

La palabra «estrictamente» es esencial: una función constante es no decreciente y no creciente, pero no es inyectiva si su dominio contiene más de un punto.

### Invertir sobre la imagen

Si $f\colon D\to\mathbb R$ es estrictamente monótona, el teorema anterior muestra que es inyectiva. Definamos

$$
J=f(D)
$$

y consideremos la misma regla con codominio ajustado:

$$
\widetilde f\colon D\to J,
\qquad
\widetilde f(x)=f(x).
$$

Por definición de $J$, $\widetilde f$ es sobreyectiva; por monotonía estricta, es inyectiva. Por tanto es biyectiva y posee inversa

$$
\widetilde f^{-1}\colon J\to D.
$$

Además, el orden de la inversa queda controlado.

::: {#res-ma-bch-0004-monotonia-inversa}
### Proposición — monotonía de la inversa

Si $f\colon D\to J$ es biyectiva y estrictamente creciente, entonces $f^{-1}$ es estrictamente creciente.

Si $f$ es estrictamente decreciente, entonces $f^{-1}$ es estrictamente decreciente.
:::

### Demostración

Supongamos que $f$ es estrictamente creciente y tomemos $y_1<y_2$ en $J$. Escribamos

$$
x_1=f^{-1}(y_1),
\qquad
x_2=f^{-1}(y_2).
$$

Si fuera $x_2<x_1$, la monotonía de $f$ implicaría

$$
y_2=f(x_2)<f(x_1)=y_1,
$$

contradicción. Tampoco puede ocurrir $x_1=x_2$, pues entonces $y_1=y_2$. Luego

$$
x_1<x_2,
$$

y $f^{-1}$ es estrictamente creciente. El caso decreciente se demuestra del mismo modo. $\square$

### Una frontera importante: monotonía no es continuidad

No debemos adelantar resultados del capítulo de continuidad. Una función estrictamente creciente definida en un intervalo puede tener una imagen que **no sea un intervalo**.

Consideremos

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=
\begin{cases}
x,&x<0,\\
x+1,&x\ge0.
\end{cases}
$$

Esta función es estrictamente creciente. Si $x_1<x_2$ y ambos están a un mismo lado de $0$, la desigualdad se conserva inmediatamente; si $x_1<0\le x_2$, entonces

$$
f(x_1)=x_1<0<1\le x_2+1=f(x_2).
$$

Sin embargo,

$$
f(\mathbb R)=(-\infty,0)\cup[1,\infty),
$$

que no es un intervalo.

::: {.ma-block .ma-observacion}
**Qué hemos demostrado y qué todavía no**

La monotonía estricta basta para obtener inyectividad y, al ajustar el codominio a la imagen, una función inversa.

No basta para garantizar que la función tome todos los valores intermedios entre dos salidas. Esa propiedad requerirá herramientas posteriores.
:::

## 10. Mapa de dependencias del capítulo {#ma-bch-0004-dependencias}

Las ideas construidas aquí no aparecen aisladas. Dependen directamente de los dos capítulos anteriores.

Del lenguaje lógico y de conjuntos necesitamos:

- cuantificadores;
- existencia y unicidad;
- igualdad de conjuntos por doble inclusión;
- producto cartesiano;
- técnicas de prueba y contraejemplo.

De la estructura de $\mathbb R$ necesitamos:

- orden y tricotomía;
- manipulación rigurosa de desigualdades;
- intervalos;
- existencia y unicidad de raíces no negativas.

Con esas herramientas obtenemos la cadena

$$
\boxed{
\begin{array}{c}
\text{función completa}\\
\downarrow\\
\text{imagen y preimagen}\\
\downarrow\\
\text{inyectividad / sobreyectividad / biyectividad}\\
\downarrow\\
\text{composición e identidad}\\
\downarrow\\
\text{función inversa}\\
\downarrow\\
\text{gráfica y transformaciones}\\
\downarrow\\
\text{monotonía e invertibilidad sobre la imagen}.
\end{array}}
$$

Esta arquitectura será reutilizada inmediatamente. Una **sucesión** será, antes que nada, una función cuyo dominio es $\mathbb N$. El capítulo siguiente añadirá una pregunta nueva: qué significa que los valores de esa función se aproximen a un número cuando el índice crece.

## 11. Páginas reutilizables asociadas {#ma-bch-0004-paginas-asociadas}

Para consultar partes del capítulo de forma independiente:

- [Funciones reales: dominio, codominio, imagen y preimagen](../../conceptos/funciones-reales-dominio-codominio-imagen-y-preimagen.md) — `MA-CON-0007`.
- [Composición de funciones e identidad](../../conceptos/composicion-de-funciones-e-identidad.md) — `MA-CON-0008`.
- [Inyectividad, sobreyectividad y biyectividad](../../conceptos/inyectividad-sobreyectividad-y-biyectividad.md) — `MA-CON-0009`.
- [Funciones inversas](../../conceptos/funciones-inversas.md) — `MA-CON-0010`.
- [Operaciones con conjuntos reales: unión, intersección, complemento y diferencia](../../conceptos/operaciones-con-conjuntos-reales.md) — `MA-CON-0006`.

El recorrido completo pertenece a [Cálculo para matemáticos](../para-matematicos/calculo-para-matematicos.md) (`MA-BOK-0001`).

## Cierre

El paso esencial de este capítulo puede resumirse así:

$$
\boxed{
\text{una función no es una fórmula: es una estructura de asignación con dominio y codominio.}
}
$$

Una vez fijada esa estructura, imágenes, preimágenes, composición, inyectividad, inversas, gráficas y monotonía dejan de ser temas separados y se convierten en diferentes maneras de interrogar al mismo objeto matemático.

Con este lenguaje ya disponible, el siguiente paso del libro será estudiar **sucesiones** como funciones y construir sobre ellas la primera noción rigurosa de límite.
