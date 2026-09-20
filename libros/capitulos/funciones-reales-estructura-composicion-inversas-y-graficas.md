---
title: "Funciones reales: estructura, composición, inversas y gráficas"
description: "Capítulo 2 de Cálculo para matemáticos. Edición canónica v11."
content-id: MA-BCH-0004
content-type: book-chapter
collection: PM-CAL
book-id: MA-BOK-0001
status: published
date-created: 2026-09-09
date-modified: 2026-09-19
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
number-sections: true
number-depth: 2
number-offset: [1]
---

# Funciones reales: estructura, composición, inversas y gráficas {#sec-t1-c03}

Durante buena parte de la matemática escolar una función aparece casi siempre acompañada por una fórmula:

$$
f(x)=x^2,
\qquad
f(x)=\frac{1}{x},
\qquad
f(x)=\sin x.
$$

Es natural que acabemos asociando las dos ideas: **función** y **fórmula**. Para calcular valores concretos, esa identificación suele resultar inofensiva. Para hacer análisis, deja de serlo.

Una función no es solamente una expresión en la que sustituimos una variable. Necesitamos saber **qué objetos podemos introducir**, **qué objetos admitimos como salidas** y **qué regla asigna una salida a cada entrada**. Cambiar cualquiera de esos datos puede cambiar la función y, sobre todo, puede cambiar sus propiedades matemáticas aun cuando la fórmula escrita permanezca intacta.

Este capítulo está dedicado a aprender a pensar funcionalmente antes de estudiar límites. Su pregunta central será

$$
\boxed{\text{¿qué información necesitamos para saber realmente qué función tenemos delante?}}
$$

El recorrido irá desde la definición completa de función hasta imágenes, preimágenes, composición, inversas, gráficas y monotonía. La idea será siempre la misma: no manipular una fórmula antes de haber identificado el objeto matemático al que esa fórmula pertenece.

## Convenciones conjuntistas indispensables {.unnumbered}

En lo que sigue trabajaremos con conjuntos entendidos en su sentido matemático habitual, sin detenernos en su construcción fundacional. La notación $x\in A$ significa que $x$ pertenece a $A$; $A\subseteq B$ significa que todo elemento de $A$ pertenece también a $B$. Dos conjuntos son iguales si tienen exactamente los mismos elementos. El conjunto vacío se denota por $\varnothing$.

Para conjuntos $E,F$ usamos $E\cup F=\{x:x\in E\text{ o }x\in F\}$ (unión), $E\cap F=\{x:x\in E\text{ y }x\in F\}$ (intersección) y $E\setminus F=\{x:x\in E\text{ y }x\notin F\}$ (diferencia). Estas igualdades funcionan también como instrucciones de prueba: demostrar una pertenencia equivale a verificar la condición situada a la derecha. Si $E\subseteq U$, su **complemento relativo a $U$** es $U\setminus E$: sin especificar el conjunto ambiente, la palabra «complemento» resulta ambigua.

Un **par ordenado** $(x,y)$ registra dos coordenadas en posiciones diferentes; $(x,y)=(u,v)$ equivale a $x=u$ e $y=v$. El **producto cartesiano** de $A$ y $B$ es $A\times B:=\{(x,y):x\in A,\ y\in B\}$. Esta convención permitirá definir una gráfica como conjunto de pares, sin exigir al lector un capítulo previo de teoría de conjuntos.

Por último, $\forall x\in A$ se lee «para todo $x$ de $A$»; $\exists x\in A$, «existe al menos un $x$ de $A$»; y $\exists!x\in A$, «existe exactamente uno». Estas expresiones se interpretarán y utilizarán siempre dentro de las definiciones y pruebas concretas del cálculo.

## Una fórmula no es todavía una función {#sec-t1-c03-01}

### Cuatro veces la misma fórmula

Comencemos con una expresión que no presenta ninguna dificultad algebraica:

$$
x^2.
$$

Consideremos ahora las cuatro asignaciones

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

A primera vista parece que hemos escrito cuatro nombres para «la misma función». Después de todo, cada vez que introducimos un número permitido, la operación que realizamos es exactamente la misma: elevarlo al cuadrado.

Pero comparemos con más cuidado.

En $f$ podemos introducir números negativos y positivos, mientras que en $g$ y $k$ solo podemos introducir números no negativos. Por tanto, $f(-2)$ tiene sentido, pero $g(-2)$ y $k(-2)$ no están definidos.

También cambia el conjunto en el que declaramos que viven las salidas. En $f$ y $k$ el conjunto de llegada es todo $\mathbb R$. Sin embargo, ningún cuadrado real es negativo. En $g$ y $h$, en cambio, el conjunto de llegada se ha ajustado precisamente a los números no negativos.

Esta diferencia afectará pronto a preguntas como las siguientes:

- ¿pueden dos entradas distintas producir la misma salida?;
- ¿se obtiene realmente cada elemento del conjunto de llegada?;
- ¿podemos recuperar una entrada a partir de una salida?

Por ejemplo, $f(2)=f(-2)=4$, mientras que en $g$ no tenemos la pareja de entradas $2$ y $-2$, porque $-2$ ni siquiera pertenece a su dominio. Y todo número no negativo aparece como cuadrado de algún número no negativo, gracias al teorema de existencia de raíces demostrado en `T1-C02`; por tanto, $g$ alcanza todo su conjunto de llegada.

Con la terminología que formalizaremos en §2.3, el contraste completo será este:

- $f$ no es inyectiva ni sobreyectiva: $2$ y $-2$ producen la misma salida, y ningún real negativo es alcanzado;
- $g$ es biyectiva: entre los números no negativos no aparecen dos entradas distintas con el mismo cuadrado, y todo número no negativo es el cuadrado de su raíz no negativa;
- $h$ es sobreyectiva pero no inyectiva: alcanza todo su codominio $[0,\infty)$, pero, por ejemplo, $h(2)=h(-2)$;
- $k$ es inyectiva pero no sobreyectiva: al restringir las entradas a $[0,\infty)$ desaparece la duplicación producida por $x$ y $-x$, pero siguen sin alcanzarse los números negativos de su codominio $\mathbb R$.

No necesitamos todavía memorizar esas palabras ni sus definiciones. El cuadro sirve para revelar el problema que las hará necesarias: **la fórmula no basta para decidir las propiedades de una función; dominio y codominio importan**.

Todavía no daremos definiciones formales de estas propiedades. Lo haremos en §2.3. Lo importante por ahora es advertir el fenómeno:

$$
\boxed{\text{la misma fórmula puede determinar funciones estructuralmente distintas}.}
$$

::: {#exm-t1-0020}
**Una misma regla, cuatro funciones distintas.** Las funciones $f,g,h,k$ anteriores utilizan la regla $x\mapsto x^2$, pero difieren en dominio o codominio. En particular:

- $f$ admite entradas negativas y declara como codominio todo $\mathbb R$;
- $g$ solo admite entradas no negativas y declara como codominio $[0,\infty)$;
- $h$ admite todas las entradas reales, pero su codominio es $[0,\infty)$;
- $k$ solo admite entradas no negativas, aunque su codominio declarado sea todo $\mathbb R$.

La fórmula aislada $x^2$ no contiene por sí sola toda esta información.
:::

::: {.callout-note title="Antes de seguir"}
Si alguien escribe únicamente

$$
p(x)=\frac1x,
$$

¿conoces ya el dominio de $p$?

No necesariamente. La expresión exige al menos que $x\ne0$, pero podría estar describiendo, por ejemplo,

$$
p\colon\mathbb R\setminus\{0\}\to\mathbb R,
$$

o una restricción como

$$
p\colon(0,\infty)\to(0,\infty).
$$

La fórmula ayuda a determinar qué entradas **son posibles**, pero el dominio matemático de una función es un dato que debe quedar fijado.
:::

### Qué significa realmente $f\colon A\to B$

Las convenciones conjuntistas recién introducidas y los cuantificadores permiten ahora formalizar la idea.

::: {#def-t1-0019}
**Función, dominio, codominio e imagen.** Sean $A$ y $B$ conjuntos. Una **función**

$$
f\colon A\to B
$$

es una regla de asignación que a **cada** elemento $x\in A$ hace corresponder **exactamente un** elemento $y\in B$. Ese elemento se denota por $f(x)$.

El conjunto $A$ se llama **dominio** de $f$ y $B$ se llama **codominio**.

El conjunto de valores que la función efectivamente toma,

$$
\operatorname{Im}(f)
=
\{f(x):x\in A\},
$$

se llama **imagen** o **recorrido** de $f$. Siempre se cumple

$$
\operatorname{Im}(f)\subseteq B.
$$
:::

Hay dos palabras pequeñas en esta definición que contienen casi todo el concepto:

> **cada** entrada tiene **exactamente una** salida.

La palabra **cada** expresa existencia. Para todo $x\in A$ debe existir una salida permitida $f(x)\in B$.

La expresión **exactamente una** añade unicidad. Una misma entrada no puede recibir dos salidas diferentes.

Expresada mediante cuantificadores, la condición puede leerse esquemáticamente como

$$
\forall x\in A\;\exists!y\in B
\quad
\text{tal que $y$ es la salida asignada a $x$}.
$$

La notación $f(x)$ presupone que esa existencia y esa unicidad ya están garantizadas por la regla que define $f$.

Esta reformulación permite diagnosticar dos maneras distintas en que una supuesta definición puede fracasar.

### Primer fallo posible: alguna entrada no tiene salida

Supongamos que declaramos

$$
r\colon\mathbb R\to\mathbb R,
\qquad
r(x)=\frac1x.
$$

La fórmula funciona para todo real distinto de cero, pero en $x=0$ exige dividir por cero. No existe ningún número real que pueda ser $r(0)$ de acuerdo con esa regla.

Por tanto, la declaración anterior **no define una función sobre todo $\mathbb R$**.

Podemos repararla cambiando el dominio:

$$
r\colon\mathbb R\setminus\{0\}\to\mathbb R,
\qquad
r(x)=\frac1x.
$$

Ahora sí existe una salida real para cada entrada permitida.

Este ejemplo enseña una regla de lectura que será permanente:

$$
\boxed{\text{antes de calcular con una fórmula, audita dónde está definida}.}
$$

### Segundo fallo posible: una entrada tiene más de una salida

Consideremos ahora la instrucción

> a cada $x\ge0$, asígnele un número real $y$ que satisfaga $y^2=x$.

Para $x=4$, tanto $y=2$ como $y=-2$ satisfacen la condición. La existencia está garantizada, pero la unicidad falla.

Así formulada, la instrucción **no define una función** de $[0,\infty)$ en $\mathbb R$.

En `T1-C02` demostramos, sin embargo, que para cada $x\ge0$ existe un único número **no negativo** cuyo cuadrado es $x$. Al añadir esa condición obtenemos una función perfectamente definida:

$$
s\colon[0,\infty)\to[0,\infty),
\qquad
s(x)=\sqrt{x}.
$$

La diferencia entre ambas instrucciones es exactamente la diferencia entre

$$
\exists y
$$

y

$$
\exists!y.
$$

No estamos aprendiendo una noción lógica nueva: estamos viendo por qué la lógica de existencia y unicidad era necesaria para definir uno de los objetos centrales del cálculo.

### Lo que **no** exige la definición

Existe un error casi simétrico al anterior. Un principiante puede pensar que, para ser función, entradas diferentes deben producir salidas diferentes.

Eso es falso.

La regla

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2,
$$

es una función aunque

$$
f(2)=f(-2)=4.
$$

La definición exige **una sola salida para cada entrada**, no **una sola entrada para cada salida**.

La segunda condición es más fuerte y recibirá el nombre de **inyectividad** en §2.3. Conviene mantener separados ambos niveles desde ahora:

$$
\boxed{
\begin{array}{c}
\text{ser función: una entrada no tiene dos salidas;}\\[4pt]
\text{ser inyectiva: dos entradas no comparten una salida.}
\end{array}}
$$

### Dominio, codominio e imagen no son la misma cosa

Volvamos a

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2.
$$

Su dominio es

$$
\mathbb R.
$$

Su codominio declarado también es

$$
\mathbb R.
$$

Pero su imagen es

$$
[0,\infty),
$$

porque todo cuadrado es no negativo y, recíprocamente, todo real no negativo posee una raíz cuadrada real.

Así,

$$
\operatorname{Im}(f)=[0,\infty)\subsetneq\mathbb R.
$$

Esta diferencia es decisiva. El **codominio** pertenece a la declaración de la función. La **imagen** se determina preguntando qué valores del codominio se alcanzan realmente.

En cambio, para

$$
h\colon\mathbb R\to[0,\infty),
\qquad
h(x)=x^2,
$$

tenemos

$$
\operatorname{Im}(h)=[0,\infty),
$$

de modo que imagen y codominio coinciden.

Por eso no podemos tratar el codominio como una ornamentación tipográfica. Cambiarlo puede cambiar afirmaciones matemáticas acerca de la función aunque la regla punto a punto permanezca intacta.

::: {.callout-warning title="Error frecuente"}
No leas automáticamente

$$
f\colon A\to B
$$

como si significara que $f$ toma **todos** los valores de $B$.

La flecha solo declara que las salidas de $f$ pertenecen a $B$. La afirmación adicional

$$
\operatorname{Im}(f)=B
$$

tendrá un nombre propio —sobreyectividad— y deberá demostrarse cuando sea necesaria.
:::

### Una convención sobre la identidad de las funciones

En distintos textos pueden encontrarse convenciones ligeramente diferentes acerca de qué datos se consideran parte de una función. En este libro adoptaremos una convención especialmente útil para el cálculo y para controlar composiciones e inversas:

> en una declaración $f\colon A\to B$, **dominio, codominio y regla de asignación forman parte de los datos de la función**.

Por ello, dos funciones serán iguales cuando coincidan esos datos.

::: {#def-t1-0020}
**Igualdad, restricción y extensión.** Sean

$$
f\colon A\to B,
\qquad
g\colon C\to D.
$$

Diremos que $f=g$ si

$$
A=C,
\qquad
B=D,
$$

y

$$
f(x)=g(x)
\qquad
\text{para todo }x\in A.
$$

Si $E\subseteq A$, la **restricción** de $f$ a $E$ es la función

$$
f|_E\colon E\to B
$$

definida por

$$
f|_E(x)=f(x)
\qquad(x\in E).
$$

Si $A\subseteq C$ y $g\colon C\to B$ satisface

$$
g|_A=f,
$$

diremos que $g$ es una **extensión** de $f$.
:::

La igualdad de funciones es, por tanto, más exigente que la igualdad de dos fórmulas escritas sobre una hoja.

Consideremos

$$
f\colon\mathbb R\to\mathbb R,
\qquad f(x)=x^2,
$$

y

$$
g\colon[0,\infty)\to\mathbb R,
\qquad g(x)=x^2.
$$

En el dominio de $g$ se cumple

$$
f(x)=g(x).
$$

Pero $f\ne g$, porque sus dominios son diferentes. En realidad,

$$
g=f|_{[0,\infty)}.
$$

Así, **restricción** es el nombre preciso para lo que hemos hecho: conservar la regla y permitir menos entradas.

### Restricción: perder entradas puede ganar estructura

Restringir una función no es simplemente «recortar un dibujo». Puede cambiar profundamente sus propiedades.

La función

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2,
$$

produce el mismo valor en $x$ y $-x$. Pero su restricción

$$
f|_{[0,\infty)}\colon[0,\infty)\to\mathbb R
$$

ya no contiene simultáneamente esas dos entradas salvo en $0$.

Más adelante veremos que esta restricción es precisamente lo que permite invertir la operación de elevar al cuadrado sobre los números no negativos.

Este ejemplo anticipa un principio general:

$$
\boxed{\text{cambiar el dominio puede cambiar las propiedades de una función}.}
$$

No cambia los valores que ya estaban definidos en los puntos conservados. Cambia el **objeto funcional** sobre el que formulamos preguntas.

### Extensión: conservar lo conocido y definir más

La operación inversa a restringir es extender.

Por ejemplo, consideremos

$$
u\colon[0,\infty)\to\mathbb R,
\qquad
u(x)=x.
$$

La función identidad sobre $\mathbb R$,

$$
U\colon\mathbb R\to\mathbb R,
\qquad
U(x)=x,
$$

es una extensión de $u$ porque coincide con ella en cada $x\ge0$.

Pero una extensión no tiene por qué ser única. También podemos definir

$$
V(x)=
\begin{cases}
x,&x\ge0,\\
0,&x<0,
\end{cases}
$$

como función $V\colon\mathbb R\to\mathbb R$. Entonces $V$ también extiende a $u$.

Por tanto,

$$
\boxed{\text{conocer una función en un subconjunto no determina, en general, una extensión única}.}
$$

Esta observación será importante mucho más adelante, pero aquí solo necesitamos aprender a distinguir los objetos.

### Una función no necesita una fórmula cerrada

Hasta ahora casi todos nuestros ejemplos han utilizado expresiones algebraicas. Eso puede reforzar accidentalmente la asociación que intentábamos romper.

Una función es una regla de asignación con existencia y unicidad. **La manera de comunicar esa regla puede variar.**

Podemos describir una función mediante una tabla. Por ejemplo, si

$$
A=\{a,b,c,d\},
$$

la tabla

$$
\begin{array}{c|cccc}
x&a&b&c&d\\
\hline
T(x)&2&-1&2&5
\end{array}
$$

define una función

$$
T\colon A\to\mathbb R.
$$

Obsérvese nuevamente que $T(a)=T(c)=2$ no causa ningún problema: cada entrada sigue teniendo una única salida.

También podemos usar una descripción verbal. Por ejemplo,

$$
\ell\colon\{\text{palabras finitas del alfabeto latino}\}\to\mathbb N
$$

puede asignar a cada palabra su número de letras.

O podemos usar un algoritmo.

::: {#exm-t1-0021}
**Una función descrita por un procedimiento.** Para cada $n\in\mathbb N_{>0}$, sea

$$
d(n)=\text{número de divisores positivos de }n.
$$

Esto define una función

$$
d\colon\mathbb N_{>0}\to\mathbb N_{>0}.
$$

Por ejemplo,

$$
d(1)=1,
\qquad
d(6)=4,
\qquad
d(12)=6,
$$

porque

$$
\{m\in\mathbb N_{>0}:m\mid12\}
=
\{1,2,3,4,6,12\}.
$$

Para calcular $d(n)$ podemos emplear un procedimiento: examinar los enteros positivos hasta $n$ y contar cuáles dividen exactamente a $n$. Esa descripción puede ser menos eficiente que una fórmula especializada, pero determina una salida única para cada entrada. Por tanto, determina una función.
:::

La existencia de una función no depende de que poseamos una expresión algebraica breve para ella.

### Fórmula, función y gráfica: tres niveles distintos

Podemos resumir ya la primera distinción del capítulo.

Una **fórmula** es una manera posible de especificar una regla.

Una **función** es el objeto que incluye entradas admitidas, salidas admitidas y una asignación única para cada entrada.

Una **gráfica**, que estudiaremos formalmente en §2.7, será un conjunto de pares

$$
(x,f(x))
$$

que representa geométricamente esa asignación.

Los tres niveles se relacionan, pero no deben confundirse:

$$
\boxed{
\text{fórmula o regla}
\longrightarrow
\text{función completa}
\longrightarrow
\text{representaciones de la función}.
}
$$

Una misma función puede describirse por fórmulas distintas en regiones diferentes. Una misma fórmula puede utilizarse para funciones con dominios distintos. Y una gráfica puede ayudarnos a comprender una función sin sustituir la información precisa de dominio y codominio.

### Cómo leer desde ahora una declaración funcional

Ante una escritura como

$$
f\colon A\to B,
$$

conviene hacer cuatro preguntas antes de manipularla:

1. ¿Cuál es el dominio $A$? Es decir, ¿qué entradas están permitidas?
2. ¿Cuál es el codominio $B$? Es decir, ¿dónde deben vivir las salidas?
3. ¿Cuál es la regla que determina $f(x)$ para cada $x\in A$?
4. ¿Qué conjunto constituye realmente la imagen $\operatorname{Im}(f)$?

La cuarta pregunta puede requerir una demostración. Las tres primeras forman parte de la especificación de la función.

::: {.callout-note title="Antes de seguir"}
Considera

$$
p\colon[-2,2]\to\mathbb R,
\qquad
p(x)=x^2.
$$

- El dominio es $[-2,2]$.
- El codominio es $\mathbb R$.
- La imagen es $[0,4]$.

¿Por qué la imagen no es simplemente $\mathbb R$? Porque el codominio declara **salidas permitidas**, mientras que la imagen registra **salidas realmente alcanzadas**. En este caso $p(x)$ nunca es negativo ni puede superar $4$ cuando $|x|\le2$.
:::

### Qué nos falta todavía

Ya sabemos qué datos constituyen una función y podemos distinguir dominio, codominio e imagen. Pero todavía no disponemos del lenguaje adecuado para responder de manera sistemática preguntas como estas:

- ¿qué conjunto de salidas produce un subconjunto dado del dominio?;
- ¿qué entradas terminan dentro de un subconjunto dado del codominio?;
- ¿cómo se comportan estas operaciones respecto de uniones e intersecciones?

Estas preguntas exigen pasar de la imagen de **un punto** a la imagen y la preimagen de **conjuntos completos**.

Ese será el objeto de §2.2.

## Imágenes y preimágenes {#sec-t1-c03-02}

En la sección anterior distinguimos tres conjuntos asociados a una función

$$
f\colon A\to B:
$$

el dominio $A$, el codominio $B$ y la imagen total $\operatorname{Im}(f)$. Ahora vamos a refinar esa mirada.

Una función no solo envía **puntos** del dominio a puntos del codominio. También nos permite seguir lo que ocurre con **subconjuntos completos**.

Si elegimos una región $E\subseteq A$, podemos preguntar:

> ¿qué valores produce la función cuando solo dejamos entrar elementos de $E$?

Y si elegimos una región $F\subseteq B$, podemos plantear la pregunta inversa:

> ¿qué entradas del dominio terminan dentro de $F$?

Estas dos preguntas conducen a dos operaciones fundamentales: **imagen** y **preimagen**.

La diferencia de dirección conviene verla desde el principio:

$$
\boxed{
\begin{array}{ccc}
E\subseteq A & \xrightarrow{\quad f\quad} & f(E)\subseteq B,\\[6pt]
f^{-1}(F)\subseteq A & \xleftarrow{\quad f\quad} & F\subseteq B.
\end{array}}
$$

La imagen avanza en el sentido de la función. La preimagen retrocede desde un conjunto de posibles salidas hacia las entradas que llegan a él.

### De la imagen de un punto a la imagen de un conjunto

Cuando $x\in A$, ya sabemos qué significa

$$
f(x).
$$

Es un **elemento** de $B$: la salida asignada a la entrada $x$.

Ahora sea $E\subseteq A$. En lugar de introducir una sola entrada, dejamos que $x$ recorra todo $E$. Reunimos entonces todas las salidas obtenidas.

::: {#def-t1-0021}
**Imagen y preimagen de subconjuntos.** Sea

$$
f\colon A\to B
$$

una función.

Si $E\subseteq A$, la **imagen de $E$ bajo $f$** es el subconjunto de $B$

$$
f(E)
=
\{f(x):x\in E\}.
$$

Equivalentemente,

$$
y\in f(E)
\iff
\exists x\in E\text{ tal que }f(x)=y.
$$

Si $F\subseteq B$, la **preimagen** o **imagen inversa de $F$ bajo $f$** es el subconjunto de $A$

$$
f^{-1}(F)
=
\{x\in A:f(x)\in F\}.
$$

Equivalentemente,

$$
x\in f^{-1}(F)
\iff
f(x)\in F.
$$
:::

La definición contiene una asimetría lógica importante.

Para demostrar que un elemento $y$ pertenece a $f(E)$ debemos encontrar **alguna entrada** $x\in E$ que produzca $y$. La pertenencia a una imagen contiene, por tanto, una afirmación existencial:

$$
y\in f(E)
\iff
\exists x\,(x\in E\land f(x)=y).
$$

En cambio, para decidir si $x$ pertenece a $f^{-1}(F)$ no tenemos que buscar ningún testigo adicional. Basta comprobar dónde cae su imagen:

$$
x\in f^{-1}(F)
\iff
f(x)\in F.
$$

Las convenciones conjuntistas anteriores se vuelven operativas: abrir una definición transforma una afirmación sobre conjuntos en una condición sobre elementos y cuantificadores.

### Un punto no es un conjunto

La notación puede parecer casi idéntica, pero debemos distinguir

$$
f(x)
$$

de

$$
f(E).
$$

Si $x\in A$, entonces $f(x)$ es un elemento de $B$.

Si $E\subseteq A$, entonces $f(E)$ es un subconjunto de $B$.

Por ejemplo, si

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2,
$$

entonces

$$
f(2)=4,
$$

mientras que

$$
f(\{2\})=\{4\}.
$$

La primera salida es un número. La segunda es un conjunto que contiene ese número.

En general,

$$
f(\{x\})=\{f(x)\}.
$$

Esta diferencia tipológica parece pequeña, pero evitará muchos errores cuando empecemos a combinar funciones y operaciones con conjuntos.

### El recorrido es una imagen particular

En §2.1 definimos

$$
\operatorname{Im}(f)
=
\{f(x):x\in A\}.
$$

Con la notación recién introducida podemos escribir simplemente

$$
\boxed{\operatorname{Im}(f)=f(A).}
$$

El recorrido de una función es, por tanto, la imagen de **todo su dominio**.

Esto permite separar dos afirmaciones que se confunden con frecuencia:

$$
f(A)\subseteq B
$$

siempre, porque todas las salidas deben pertenecer al codominio, mientras que

$$
f(A)=B
$$

es una afirmación adicional: dice que no queda ningún elemento del codominio sin alcanzar. En §2.3 daremos nombre y estructura lógica a esa propiedad.

### Seguir un conjunto hacia delante

Volvamos a la función

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2.
$$

Tomemos

$$
E=[-1,2].
$$

Queremos calcular $f(E)$.

No basta con sustituir los extremos y escribir apresuradamente

$$
[f(-1),f(2)]=[1,4].
$$

Eso sería incorrecto, porque $0\in E$ y

$$
f(0)=0.
$$

El conjunto imagen contiene, por tanto, valores menores que $1$.

Para calcularlo correctamente necesitamos resolver dos tareas:

1. demostrar que toda salida producida desde $E$ pertenece a cierto conjunto candidato;
2. demostrar que todo elemento de ese conjunto candidato es realmente producido por alguna entrada de $E$.

Es el mismo patrón de doble inclusión que aprendimos para demostrar igualdad de conjuntos.

Primero, si $x\in[-1,2]$, entonces $|x|\le2$, de modo que

$$
0\le x^2\le4.
$$

Por tanto,

$$
f([-1,2])\subseteq[0,4].
$$

Ahora tomemos un $y\in[0,4]$. Por la existencia de raíces establecida en `T1-C02`, existe $\sqrt y\in[0,2]$. En particular,

$$
\sqrt y\in[-1,2],
$$

y

$$
f(\sqrt y)=(\sqrt y)^2=y.
$$

Así, cada $y\in[0,4]$ pertenece a $f([-1,2])$. Luego

$$
[0,4]\subseteq f([-1,2]).
$$

Concluimos que

$$
\boxed{f([-1,2])=[0,4].}
$$

Este cálculo revela una diferencia importante entre **evaluar una función en puntos** y **determinar la imagen de un conjunto**. La segunda tarea suele ser un problema de conjuntos: debemos caracterizar todas las salidas posibles, no solamente calcular algunos valores.

::: {.callout-warning title="Error frecuente"}
Para una función cualquiera no existe una regla general que permita obtener la imagen de un intervalo evaluando solamente sus extremos.

En este capítulo aprenderemos más adelante qué información adicional —por ejemplo, ciertas propiedades de orden— permite controlar mejor las imágenes de intervalos. Aquí no debemos suponerla de antemano.
:::

### Retroceder desde las salidas: la preimagen

Consideremos de nuevo

$$
f(x)=x^2,
\qquad
f\colon\mathbb R\to\mathbb R,
$$

pero ahora partamos del conjunto de salidas

$$
F=[1,4].
$$

La pregunta ya no es «¿qué valores produce cierto conjunto de entradas?», sino

> ¿qué números reales tienen su cuadrado entre $1$ y $4$?

Por definición,

$$
f^{-1}([1,4])
=
\{x\in\mathbb R:1\le x^2\le4\}.
$$

La condición

$$
1\le x^2\le4
$$

es equivalente a

$$
1\le|x|\le2.
$$

Por tanto,

$$
\boxed{
f^{-1}([1,4])
=
[-2,-1]\cup[1,2].
}
$$

Observa la geometría algebraica del resultado: un solo intervalo situado en el lado no negativo del codominio tiene dos ramas de antecedentes, porque $x$ y $-x$ poseen el mismo cuadrado.

No hemos definido todavía la inyectividad formalmente, pero ya estamos viendo qué aspecto tiene su fracaso: una misma salida puede provenir de más de una entrada.

### Una misma función, imágenes y preimágenes

::: {#exm-t1-0022}
**Imágenes y preimágenes bajo $x\mapsto x^2$.** Sea

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2.
$$

Entonces:

$$
f([-1,2])=[0,4],
$$

$$
f(\{-2,0,3\})=\{0,4,9\},
$$

$$
f^{-1}([1,4])=[-2,-1]\cup[1,2],
$$

$$
f^{-1}(\{4\})=\{-2,2\},
$$

$$
f^{-1}(\{0\})=\{0\},
$$

y

$$
f^{-1}(\{-1\})=\varnothing.
$$

La última igualdad no significa que la preimagen «no exista». La preimagen existe y es un conjunto perfectamente definido; ocurre simplemente que ningún número real tiene cuadrado $-1$.
:::

Este ejemplo reúne tres posibilidades que conviene distinguir:

- una salida puede tener varios antecedentes;
- una salida puede tener exactamente un antecedente;
- una salida puede no tener antecedentes.

En todos los casos, la **preimagen del conjunto** está bien definida.

### Resolver una ecuación como calcular una preimagen

La notación de preimagen permite reinterpretar una tarea algebraica familiar.

Resolver

$$
f(x)=y
$$

para una salida fija $y\in B$ equivale a calcular

$$
f^{-1}(\{y\}).
$$

En efecto,

$$
x\in f^{-1}(\{y\})
\iff
f(x)\in\{y\}
\iff
f(x)=y.
$$

Por ejemplo, para $f(x)=x^2$,

$$
f^{-1}(\{4\})
=
\{x\in\mathbb R:x^2=4\}
=
\{-2,2\}.
$$

Así, la solución de la ecuación $x^2=4$ puede verse como la preimagen del conjunto unitario $\{4\}$.

Pero una preimagen general es más amplia que resolver una sola ecuación. Calcular

$$
f^{-1}([1,4])
$$

significa resolver una **condición de pertenencia**:

$$
f(x)\in[1,4],
$$

es decir,

$$
1\le f(x)\le4.
$$

Para $f(x)=x^2$, eso conduce a una inecuación, no a una ecuación puntual.

Podemos resumir:

$$
\boxed{
\begin{aligned}
f^{-1}(\{y\})&=\text{conjunto de soluciones de }f(x)=y,\\
f^{-1}(F)&=\text{conjunto de soluciones de }f(x)\in F.
\end{aligned}}
$$

### Un ejemplo lineal: la dirección importa

Sea

$$
g\colon\mathbb R\to\mathbb R,
\qquad
g(x)=2x-3.
$$

Calculemos primero la imagen de

$$
E=[0,2].
$$

Si $x\in[0,2]$, entonces

$$
0\le x\le2.
$$

Multiplicando por $2$ y restando $3$ obtenemos

$$
-3\le2x-3\le1.
$$

Por tanto,

$$
g([0,2])\subseteq[-3,1].
$$

Recíprocamente, si $y\in[-3,1]$, definimos

$$
x=\frac{y+3}{2}.
$$

De $-3\le y\le1$ se sigue que $0\le x\le2$, y además

$$
g(x)
=2\left(\frac{y+3}{2}\right)-3
=y.
$$

Luego

$$
\boxed{g([0,2])=[-3,1].}
$$

Ahora calculemos la preimagen de

$$
F=[-1,5].
$$

Por definición,

$$
g^{-1}([-1,5])
=
\{x\in\mathbb R:-1\le2x-3\le5\}.
$$

Sumando $3$ y dividiendo por $2$ obtenemos

$$
1\le x\le4.
$$

Así,

$$
\boxed{g^{-1}([-1,5])=[1,4].}
$$

Los dos cálculos pueden parecer similares porque la función es algebraicamente sencilla, pero responden a preguntas opuestas:

- para hallar $g(E)$, partimos de las **entradas** y caracterizamos sus salidas;
- para hallar $g^{-1}(F)$, partimos de las **salidas permitidas** y caracterizamos las entradas que llegan a ellas.

### La preimagen no exige una función inversa

Aquí aparece una de las advertencias notacionales más importantes del capítulo.

Para

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2,
$$

acabamos de escribir

$$
f^{-1}([1,4]).
$$

Sin embargo, ya vimos en §2.1 que esta función toma el mismo valor en $2$ y $-2$, y tampoco alcanza los reales negativos. Más adelante demostraremos que una función con estas características no posee una función inversa

$$
f^{-1}\colon\mathbb R\to\mathbb R.
$$

No hay contradicción.

La expresión

$$
f^{-1}(F)
$$

que hemos definido en esta sección significa **preimagen del conjunto $F$ bajo $f$**. Está definida para cualquier función $f\colon A\to B$ y cualquier subconjunto $F\subseteq B$.

La expresión

$$
f^{-1}(y)
$$

cuando $f^{-1}$ es una **función inversa** pertenece a otra construcción, que estudiaremos en §2.5 y que solo existe bajo hipótesis adicionales.

::: {.callout-warning title="La notación $f^{-1}$ tiene dos usos"}
No concluyas que existe una función inversa solo porque aparece una expresión como

$$
f^{-1}(F).
$$

La preimagen de conjuntos existe para toda función.

Cuando una verdadera función inversa exista, el contexto indicará qué significado tiene $f^{-1}$. Más adelante veremos además que ambos usos son compatibles en el caso biyectivo.
:::

### Tampoco significa tomar el recíproco

Existe una segunda confusión frecuente. Si $f$ es una función real, la expresión

$$
\frac1f
$$

puede utilizarse, donde tenga sentido, para la función definida por

$$
\left(\frac1f\right)(x)=\frac1{f(x)}.
$$

Esto no tiene relación con la preimagen y tampoco es, en general, una función inversa.

Por ejemplo, si

$$
f(x)=x^2,
$$

entonces

$$
\frac1{f(x)}=\frac1{x^2}
$$

para $x\ne0$.

En cambio,

$$
f^{-1}([1,4])=[-2,-1]\cup[1,2]
$$

es un **conjunto de entradas**.

Son objetos de tipos completamente diferentes.

### Comprobación de tipos

Una manera eficaz de evitar errores es preguntar siempre qué clase de objeto espera cada notación.

Si

$$
f\colon A\to B,
$$

entonces:

- para formar $f(x)$ necesitamos $x\in A$;
- para formar $f(E)$ necesitamos $E\subseteq A$;
- para formar $f^{-1}(F)$ como preimagen necesitamos $F\subseteq B$.

Y los resultados son:

$$
f(x)\in B,
$$

$$
f(E)\subseteq B,
$$

$$
f^{-1}(F)\subseteq A.
$$

Podemos organizarlo así:

$$
\boxed{
\begin{array}{c|c|c}
\text{entrada de la notación}&\text{operación}&\text{resultado}\\
\hline
x\in A&f(x)&\text{elemento de }B\\
E\subseteq A&f(E)&\text{subconjunto de }B\\
F\subseteq B&f^{-1}(F)&\text{subconjunto de }A
\end{array}}
$$

Esta «comprobación de tipos» es especialmente útil cuando dominio y codominio son conjuntos de naturaleza distinta.

### Cuatro pruebas de consistencia

Antes de pasar a ejemplos más elaborados, las definiciones nos proporcionan cuatro controles inmediatos.

Primero,

$$
f(\varnothing)=\varnothing.
$$

No hay entradas en el conjunto vacío, por lo que no puede producirse ninguna salida desde él.

Segundo,

$$
f^{-1}(\varnothing)=\varnothing.
$$

Ninguna entrada puede tener su imagen dentro de un conjunto que no contiene elementos.

Tercero,

$$
f(A)=\operatorname{Im}(f),
$$

como ya observamos.

Cuarto,

$$
\boxed{f^{-1}(B)=A.}
$$

Esta última igualdad merece atención. Toda entrada $x\in A$ satisface

$$
f(x)\in B
$$

por la propia definición de función $f\colon A\to B$. Por tanto, todas las entradas pertenecen a la preimagen del codominio.

No necesitamos que $f$ alcance todos los elementos de $B$. Así, puede ocurrir simultáneamente que

$$
f(A)\ne B
$$

pero

$$
f^{-1}(B)=A.
$$

La primera igualdad fallida habla de qué **salidas se alcanzan**. La segunda, siempre verdadera, habla de dónde están autorizadas a caer las salidas.

### Preimagen de un valor que no se alcanza

Sea otra vez

$$
f(x)=x^2,
\qquad
f\colon\mathbb R\to\mathbb R.
$$

Como $-1$ pertenece al codominio, tiene sentido preguntar por

$$
f^{-1}(\{-1\}).
$$

Pero ningún $x\in\mathbb R$ satisface $x^2=-1$. Por tanto,

$$
f^{-1}(\{-1\})=\varnothing.
$$

Esto muestra por qué debemos distinguir «pertenecer al codominio» de «ser alcanzado por la función».

El codominio determina qué preguntas de preimagen están tipadas correctamente. La imagen total determina cuáles de esas preguntas tienen antecedentes efectivos.

### Un método práctico para calcular imágenes

Cuando una función está dada por una fórmula y queremos calcular $f(E)$, conviene seguir este esquema:

1. **Propón un conjunto candidato** para las salidas posibles.
2. **Primera inclusión:** toma $x\in E$ y demuestra que $f(x)$ pertenece al candidato.
3. **Segunda inclusión:** toma una salida candidata $y$ y construye, si es posible, un $x\in E$ tal que $f(x)=y$.
4. Concluye la igualdad por doble inclusión.

El paso 3 suele ser el más informativo. No basta saber que ningún valor se sale del conjunto candidato; debemos saber también que no hemos incluido valores que la función nunca alcanza desde $E$.

Este método reaparecerá en §2.3 al estudiar sobreyectividad: allí la construcción de un antecedente será precisamente el núcleo de la demostración.

### Un método práctico para calcular preimágenes

Para calcular $f^{-1}(F)$ el procedimiento suele ser más directo:

1. escribe la definición
   $$
   f^{-1}(F)=\{x\in A:f(x)\in F\};
   $$
2. traduce la pertenencia $f(x)\in F$ a ecuaciones, inecuaciones o condiciones conocidas;
3. resuelve esas condiciones dentro del dominio $A$;
4. expresa el conjunto resultante de forma conveniente.

Por ejemplo, si

$$
f(x)=x^2
$$

y

$$
F=(1,4],
$$

entonces

$$
x\in f^{-1}((1,4])
\iff
1<x^2\le4
\iff
1<|x|\le2.
$$

Luego

$$
\boxed{
f^{-1}((1,4])
=[-2,-1)\cup(1,2].
}
$$

Nótese que no hemos «invertido la fórmula $x^2$». Hemos traducido una condición de pertenencia y la hemos resuelto.

### Mirar hacia §2.3 sin adelantarla

La imagen y la preimagen ya nos permiten formular con precisión las dos preguntas que motivaron la apertura del capítulo.

Para

$$
f\colon A\to B,
$$

podemos preguntar:

1. ¿cada $y\in B$ pertenece a $f(A)$?
2. para cada $y\in B$, ¿el conjunto $f^{-1}(\{y\})$ contiene como máximo un elemento?

La primera pregunta trata de si se alcanza todo el codominio. La segunda trata de si una salida puede provenir de dos entradas distintas.

En §2.3 convertiremos esas preguntas en las definiciones formales de **sobreyectividad** e **inyectividad**.

Por ahora basta conservar el mapa conceptual:

$$
\boxed{
\begin{array}{c}
\text{imagen: qué salidas produce un conjunto de entradas;}\\[4pt]
\text{preimagen: qué entradas terminan en un conjunto de salidas.}
\end{array}}
$$

Y queda pendiente una cuestión más sutil. Si combinamos subconjuntos mediante uniones, intersecciones o complementos, ¿cómo se comportan sus imágenes y preimágenes? Algunas igualdades funcionan siempre; otras requieren hipótesis adicionales.

No responderemos todavía esa pregunta. La reservamos para §2.6, donde servirá como laboratorio de demostración, contraejemplo y diagnóstico de hipótesis.

## Inyectividad, sobreyectividad y biyectividad {#sec-t1-c03-03}

La sección anterior terminó con dos preguntas sobre una función

$$
f\colon A\to B.
$$

La primera miraba hacia el codominio:

> ¿todo $y\in B$ es realmente alcanzado por alguna entrada?

La segunda miraba hacia las fibras de un valor:

> si dos entradas producen la misma salida, ¿tienen necesariamente que ser la misma entrada?

Estas preguntas describen dos propiedades diferentes. Una controla **cuántas salidas del codominio se alcanzan**; la otra controla **cuántas entradas pueden compartir una salida**. Conviene aprenderlas por separado antes de combinarlas.

### Tres propiedades y tres preguntas distintas

::: {#def-t1-0022}
**Inyectividad, sobreyectividad y biyectividad.** Sea

$$
f\colon A\to B.
$$

Diremos que $f$ es **inyectiva** si, para cualesquiera $x_1,x_2\in A$,

$$
f(x_1)=f(x_2)
\quad\Longrightarrow\quad
x_1=x_2.
$$

Diremos que $f$ es **sobreyectiva** si cada elemento del codominio es imagen de alguna entrada; es decir, si

$$
\forall y\in B\;\exists x\in A
\quad
f(x)=y.
$$

Equivalentemente,

$$
f(A)=B.
$$

Diremos que $f$ es **biyectiva** si es simultáneamente inyectiva y sobreyectiva.
:::

Las tres palabras responden, por tanto, a preguntas muy concretas:

- **inyectiva:** ¿pueden dos entradas distintas compartir una salida?;
- **sobreyectiva:** ¿queda algún elemento del codominio sin ser alcanzado?;
- **biyectiva:** ¿cada salida del codominio corresponde a una entrada y solo a una?

La última frase debe leerse con precisión. Una función biyectiva establece una correspondencia uno a uno entre el dominio y el codominio. La existencia de una función inversa formalizará esta idea en §2.5; no necesitamos todavía ese resultado para trabajar con la definición.

### Inyectividad: empezar suponiendo igualdad de imágenes

La forma lógica de la inyectividad ya nos indica cómo suele comenzar una demostración.

Queremos probar

$$
\forall x_1,x_2\in A,
\qquad
f(x_1)=f(x_2)\Longrightarrow x_1=x_2.
$$

Por tanto, el esqueleto estándar es:

1. toma $x_1,x_2\in A$ arbitrarios;
2. supone que $f(x_1)=f(x_2)$;
3. usa la regla de la función y las propiedades del dominio para deducir $x_1=x_2$.

Consideremos, por ejemplo,

$$
p\colon\mathbb R\to\mathbb R,
\qquad
p(x)=3x-7.
$$

Para probar que $p$ es inyectiva, sean $x_1,x_2\in\mathbb R$ y supongamos

$$
p(x_1)=p(x_2).
$$

Entonces

$$
3x_1-7=3x_2-7.
$$

Sumando $7$ y dividiendo por $3$ obtenemos

$$
x_1=x_2.
$$

Luego $p$ es inyectiva.

Obsérvese que no hemos comenzado escogiendo una salida arbitraria. Para la inyectividad, la información inicial útil es la **igualdad de dos imágenes**.

::: {.callout-warning title="Error frecuente"}
Demostrar que para cada $x\in A$ existe un único valor $f(x)$ **no demuestra inyectividad**.

Eso demuestra que la regla está bien definida como función: una entrada no recibe dos salidas.

La inyectividad exige una afirmación diferente:

$$
f(x_1)=f(x_2)\Longrightarrow x_1=x_2.
$$

Es decir, dos entradas no pueden compartir una misma salida salvo que en realidad sean la misma entrada.
:::

### Cómo demostrar que una función no es inyectiva

Negar la definición produce un criterio muy útil. Una función $f\colon A\to B$ **no** es inyectiva si existen $x_1,x_2\in A$ tales que

$$
x_1\ne x_2
$$

pero

$$
f(x_1)=f(x_2).
$$

Por tanto, para refutar la inyectividad basta un solo par de entradas distintas con la misma imagen.

Para

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2,
$$

tenemos

$$
2\ne-2
$$

pero

$$
f(2)=4=f(-2).
$$

Ese par constituye un contraejemplo completo a la inyectividad.

En el lenguaje de §2.2, la misma observación puede expresarse diciendo que

$$
f^{-1}(\{4\})=\{-2,2\}
$$

contiene más de un elemento.

### Sobreyectividad: comenzar con una salida arbitraria

La forma lógica de la sobreyectividad es diferente:

$$
\forall y\in B\;\exists x\in A
\quad
f(x)=y.
$$

Ahora el procedimiento natural es:

1. toma un $y\in B$ arbitrario;
2. busca o construye una entrada $x\in A$ que pueda producirlo;
3. verifica que esa entrada pertenece realmente al dominio;
4. comprueba que $f(x)=y$.

Volvamos a

$$
p\colon\mathbb R\to\mathbb R,
\qquad
p(x)=3x-7.
$$

Sea $y\in\mathbb R$ arbitrario. Queremos resolver

$$
3x-7=y
$$

para $x$. La ecuación sugiere

$$
x=\frac{y+7}{3}.
$$

Como $y\in\mathbb R$, también

$$
\frac{y+7}{3}\in\mathbb R,
$$

de modo que la entrada propuesta pertenece al dominio. Finalmente,

$$
p\left(\frac{y+7}{3}\right)
=
3\left(\frac{y+7}{3}\right)-7
=
y.
$$

Como el argumento funciona para todo $y\in\mathbb R$, la función $p$ es sobreyectiva.

Este ejemplo ilustra un principio general: una prueba de sobreyectividad es, con frecuencia, una **prueba de existencia parametrizada por una salida arbitraria**.

### Cómo demostrar que una función no es sobreyectiva

Para refutar la sobreyectividad debemos exhibir al menos un elemento del codominio que no sea alcanzado.

La negación de

$$
\forall y\in B\;\exists x\in A,
\qquad f(x)=y
$$

es

$$
\exists y\in B\;\forall x\in A,
\qquad f(x)\ne y.
$$

Así, basta encontrar un $y\in B$ tal que

$$
f^{-1}(\{y\})=\varnothing.
$$

Por ejemplo, para

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2,
$$

el número $-1$ pertenece al codominio, pero

$$
f^{-1}(\{-1\})=\varnothing.
$$

Luego $f$ no es sobreyectiva.

La misma conclusión se obtiene a partir del recorrido:

$$
f(\mathbb R)=[0,\infty)\ne\mathbb R.
$$

### Una misma fórmula, las cuatro posibilidades

Ahora podemos volver con plena precisión al contraste que abrió el capítulo.

::: {#exm-t1-0023}
**Cuatro clasificaciones con la regla $x\mapsto x^2$.** Consideremos

$$
f\colon\mathbb R\to\mathbb R,
\qquad f(x)=x^2,
$$

$$
g\colon[0,\infty)\to[0,\infty),
\qquad g(x)=x^2,
$$

$$
h\colon\mathbb R\to[0,\infty),
\qquad h(x)=x^2,
$$

y

$$
k\colon[0,\infty)\to\mathbb R,
\qquad k(x)=x^2.
$$

Entonces:

1. $f$ no es inyectiva ni sobreyectiva;
2. $g$ es biyectiva;
3. $h$ es sobreyectiva pero no inyectiva;
4. $k$ es inyectiva pero no sobreyectiva.
:::

Demostremos cada afirmación, porque las razones son más importantes que la tabla final.

**1. La función $f$ no es inyectiva.** Ya vimos que

$$
f(2)=f(-2)=4
$$

con $2\ne-2$.

**2. La función $f$ no es sobreyectiva.** Ningún real negativo pertenece a su imagen; por ejemplo,

$$
f^{-1}(\{-1\})=\varnothing.
$$

**3. La función $g$ es inyectiva.** Sean $x_1,x_2\in[0,\infty)$ y supongamos

$$
x_1^2=x_2^2.
$$

Entonces

$$
(x_1-x_2)(x_1+x_2)=0.
$$

Si $x_1-x_2=0$, ya tenemos $x_1=x_2$. Si $x_1+x_2=0$, como ambos números son no negativos, necesariamente

$$
x_1=x_2=0.
$$

En ambos casos $x_1=x_2$. Por tanto, $g$ es inyectiva.

**4. La función $g$ es sobreyectiva.** Sea $y\in[0,\infty)$. Por el resultado de existencia de raíces de `T1-C02`, existe $\sqrt y\in[0,\infty)$ y

$$
g(\sqrt y)=(\sqrt y)^2=y.
$$

Así, cada elemento del codominio tiene un antecedente. Luego $g$ es sobreyectiva y, por tanto, biyectiva.

**5. La función $h$ es sobreyectiva.** El mismo argumento con $\sqrt y$ funciona para todo $y\in[0,\infty)$.

**6. La función $h$ no es inyectiva.** De nuevo,

$$
h(2)=h(-2).
$$

**7. La función $k$ es inyectiva.** Su dominio coincide con el de $g$, y el argumento anterior para entradas no negativas demuestra la inyectividad.

**8. La función $k$ no es sobreyectiva.** Su codominio es $\mathbb R$, pero ningún número negativo es un cuadrado real.

La tabla completa es entonces

$$
\boxed{
\begin{array}{c|c|c}
\text{función} & \text{inyectiva} & \text{sobreyectiva}\\
\hline
f\colon\mathbb R\to\mathbb R & \text{no} & \text{no}\\
g\colon[0,\infty)\to[0,\infty) & \text{sí} & \text{sí}\\
h\colon\mathbb R\to[0,\infty) & \text{no} & \text{sí}\\
k\colon[0,\infty)\to\mathbb R & \text{sí} & \text{no}
\end{array}}
$$

Una sola expresión algebraica ha producido las cuatro combinaciones posibles.

### El dominio controla colisiones

Comparemos

$$
f\colon\mathbb R\to\mathbb R,
\qquad f(x)=x^2,
$$

con su restricción

$$
k=f|_{[0,\infty)}.
$$

La primera no es inyectiva y la segunda sí.

¿Qué cambió? No la fórmula. Cambió el conjunto de entradas permitidas. Al eliminar los números negativos, dejamos de tener simultáneamente los pares $x$ y $-x$ que producían la misma salida.

Esto sugiere una operación frecuente:

> cuando una función falla en ser inyectiva porque distintas regiones del dominio repiten valores, puede ser útil restringir el dominio a una región donde esas colisiones desaparezcan.

Pero la palabra «puede» importa. Restringir el dominio no garantiza automáticamente la inyectividad. Si restringimos $x^2$ al dominio

$$
[-2,-1]\cup[1,2],
$$

siguen apareciendo pares $x$ y $-x$ con la misma imagen.

Por tanto, una restricción debe elegirse por una razón matemática concreta.

### El codominio controla la sobreyectividad

Comparemos ahora

$$
f\colon\mathbb R\to\mathbb R,
\qquad f(x)=x^2,
$$

con

$$
h\colon\mathbb R\to[0,\infty),
\qquad h(x)=x^2.
$$

Dominio y regla son iguales. Sin embargo, $f$ no es sobreyectiva y $h$ sí.

La diferencia está únicamente en el codominio.

Para cualquier función

$$
u\colon A\to B,
$$

si sabemos que su imagen es

$$
u(A)=C\subseteq B,
$$

podemos considerar la misma asignación con codominio ajustado a su imagen:

$$
\widetilde u\colon A\to C,
\qquad
\widetilde u(x)=u(x).
$$

Por construcción,

$$
\widetilde u(A)=C,
$$

así que $\widetilde u$ es sobreyectiva.

No hemos demostrado una propiedad nueva de la antigua función $u$. Hemos definido una función distinta porque, según la convención de §2.1, el codominio forma parte de los datos de una función.

Esta observación evita una frase imprecisa que aparece a veces en cálculos informales: «toda función es sobreyectiva sobre su imagen». La idea es correcta si se entiende que estamos **cambiando el codominio y, por tanto, formando una nueva función**.

### Qué cambia y qué no al modificar dominio o codominio

Conviene reunir las observaciones anteriores.

- **Restringir el dominio** puede eliminar colisiones y convertir una función no inyectiva en inyectiva.
- Restringir el dominio también puede hacer que se pierdan valores antes alcanzados y, por tanto, puede destruir sobreyectividad.
- **Cambiar el codominio**, manteniendo la misma regla y el mismo dominio, no altera si dos entradas producen o no la misma salida; por tanto, no altera la cuestión de la inyectividad mientras el nuevo codominio siga conteniendo todas las imágenes.
- En cambio, el codominio es parte esencial de la sobreyectividad: una misma asignación puntual puede ser sobreyectiva hacia un codominio y no serlo hacia otro mayor.

Esta sensibilidad explica por qué una declaración funcional completa

$$
f\colon A\to B
$$

no puede sustituirse impunemente por una fórmula aislada.

### Dos pruebas, dos arquitecturas lógicas

Supongamos que queremos demostrar que

$$
p\colon\mathbb R\to\mathbb R,
\qquad
p(x)=5x+1
$$

es biyectiva.

No conviene escribir una sola cadena de cálculos sin indicar qué propiedad estamos probando. Una prueba rigurosa tiene dos partes conceptualmente distintas.

**Inyectividad.** Sean $x_1,x_2\in\mathbb R$ y supongamos

$$
p(x_1)=p(x_2).
$$

Entonces

$$
5x_1+1=5x_2+1,
$$

de donde

$$
x_1=x_2.
$$

**Sobreyectividad.** Sea $y\in\mathbb R$ arbitrario. Tomemos

$$
x=\frac{y-1}{5}.
$$

Este $x$ pertenece al dominio y satisface

$$
p(x)
=
5\left(\frac{y-1}{5}\right)+1
=y.
$$

Por tanto, $p$ es inyectiva y sobreyectiva; luego es biyectiva.

La diferencia entre las dos mitades se ve incluso antes de calcular:

$$
\boxed{
\begin{array}{c|c}
\text{inyectividad} & \forall x_1\,\forall x_2\\
\text{sobreyectividad} & \forall y\,\exists x
\end{array}}
$$

En una, comparamos dos entradas arbitrarias. En la otra, debemos construir una entrada que puede depender de una salida arbitraria.

### Negaciones útiles para buscar contraejemplos

Las negaciones también tienen formas diferentes.

Para refutar la inyectividad buscamos

$$
\boxed{
\exists x_1,x_2\in A:
\quad
x_1\ne x_2
\quad\text{y}\quad
f(x_1)=f(x_2).
}
$$

Para refutar la sobreyectividad buscamos

$$
\boxed{
\exists y\in B:
\quad
\forall x\in A,
\quad
f(x)\ne y.
}
$$

En lenguaje de preimágenes:

- no inyectiva: alguna preimagen puntual contiene al menos dos elementos;
- no sobreyectiva: alguna preimagen puntual es vacía.

Esto hace visible una conexión muy útil entre §§2.2 y 2.3. Para cada $y\in B$, observemos el conjunto

$$
f^{-1}(\{y\}).
$$

Entonces:

- la sobreyectividad exige que **ninguno** de esos conjuntos sea vacío;
- la inyectividad exige que **ninguno** tenga más de un elemento;
- la biyectividad exige que cada uno contenga **exactamente un** elemento.

Podemos condensarlo así:

$$
\boxed{
\begin{array}{c|c}
\text{propiedad} & \text{tamaño de }f^{-1}(\{y\})\\
\hline
\text{inyectiva} & \le 1\text{ para todo }y\in B\\
\text{sobreyectiva} & \ge 1\text{ para todo }y\in B\\
\text{biyectiva} & =1\text{ para todo }y\in B
\end{array}}
$$

No estamos usando cardinalidad infinita ni una teoría nueva de tamaños de conjuntos. Solo distinguimos aquí entre vacío, unitario y «más de un elemento».

### Antes de seguir

Cuando leas una afirmación de la forma

> «$f$ es biyectiva»,

no intentes demostrarla de una sola vez. Pregunta primero:

1. ¿cómo probaré la inyectividad?
2. ¿cómo probaré la sobreyectividad?

Y cuando leas

> «$f$ no es biyectiva»,

recuerda que basta con que falle **una** de las dos propiedades. No necesitas demostrar que fallan ambas.

Esta separación será fundamental en §2.4. Allí estudiaremos qué sucede con estas propiedades cuando dos funciones se encadenan mediante composición. Por ahora, el mapa conceptual del capítulo ha avanzado un paso:

$$
\boxed{
\text{función completa}
\to
\text{imagen/preimagen}
\to
\text{inyectividad/sobreyectividad/biyectividad}.
}
$$

## Composición e identidad {#sec-t1-c03-04}

Hasta ahora hemos estudiado una función mirando lo que hace por sí sola. Pero gran parte del cálculo se construye encadenando operaciones: primero transformamos una entrada de una manera y luego aplicamos otra transformación al resultado.

Por ejemplo, para calcular

$$
(3x-1)^2
$$

podemos pensar en dos etapas:

$$
x\longmapsto 3x-1
\longmapsto
(3x-1)^2.
$$

La primera etapa produce un valor intermedio; la segunda toma precisamente ese valor como nueva entrada. La **composición de funciones** formaliza esta idea de encadenamiento.

Pero hay una cuestión que debemos resolver antes de escribir fórmulas: **¿puede la segunda función aceptar todas las salidas que realmente produce la primera?**

### Antes de componer, audita los tipos

Sean

$$
f\colon A\to B
$$

y

$$
g\colon D\to C.
$$

Queremos aplicar primero $f$ y después $g$. Si partimos de $x\in A$, la primera etapa produce

$$
f(x)\in B.
$$

Para que tenga sentido escribir $g(f(x))$, necesitamos además que ese valor $f(x)$ pertenezca al dominio $D$ de $g$.

Por tanto, la condición exacta es

$$
\boxed{f(A)\subseteq D.}
$$

Cuando se cumple, cada salida efectiva de $f$ es una entrada permitida para $g$.

El caso más frecuente se presenta como una cadena tipada

$$
A\xrightarrow{\ f\ }B\xrightarrow{\ g\ }C,
$$

es decir,

$$
f\colon A\to B,
\qquad
g\colon B\to C.
$$

Aquí la compatibilidad es automática, porque $f(A)\subseteq B$ y $B$ es precisamente el dominio de $g$.

La condición general $f(A)\subseteq D$ es un poco más flexible: el codominio declarado de $f$ no tiene por qué coincidir literalmente con el dominio de $g$ si sabemos que **las salidas que $f$ toma de hecho** sí pertenecen a ese dominio.

::: {.callout-warning title="Error frecuente"}
No basta con que las fórmulas puedan escribirse una junto a la otra de manera informal.

Considera

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2,
$$

y

$$
g\colon(0,\infty)\to\mathbb R,
\qquad
 g(y)=\frac1y.
$$

Para $x\ne0$, la expresión $g(f(x))=1/x^2$ tiene sentido. Pero $f(0)=0$ y $0\notin(0,\infty)$, de modo que $g\circ f$ **no está definida como función sobre todo $\mathbb R$**.

La fórmula $1/x^2$ no corrige silenciosamente el problema de dominio. Habría que restringir la primera etapa a $\mathbb R\setminus\{0\}$ o modificar legítimamente los datos de las funciones.
:::

::: {#def-t1-0023}
**Composición e identidad.** Sean

$$
f\colon A\to B,
\qquad
g\colon D\to C,
$$

funciones tales que

$$
f(A)\subseteq D.
$$

La **composición de $g$ con $f$** es la función

$$
g\circ f\colon A\to C
$$

definida por

$$
(g\circ f)(x)=g(f(x))
\qquad(x\in A).
$$

Para cualquier conjunto $A$, la **función identidad sobre $A$** es

$$
\operatorname{id}_A\colon A\to A
$$

dada por

$$
\operatorname{id}_A(x)=x
\qquad(x\in A).
$$
:::

La notación

$$
g\circ f
$$

debe leerse de derecha a izquierda en el orden de aplicación:

$$
\boxed{
(g\circ f)(x)
=
g(f(x))
=
\text{primero $f$, después $g$}.
}
$$

El símbolo $\circ$ no significa multiplicación. Tampoco autoriza a intercambiar el orden de las funciones.

### Componer es construir una función nueva

Tomemos

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=3x-1,
$$

y

$$
g\colon\mathbb R\to[0,\infty),
\qquad
 g(y)=y^2.
$$

Entonces

$$
g\circ f\colon\mathbb R\to[0,\infty)
$$

y

$$
(g\circ f)(x)
=g(f(x))
=g(3x-1)
=(3x-1)^2.
$$

La expresión compuesta puede parecer una sola fórmula, pero estructuralmente conserva las dos etapas:

$$
\mathbb R
\xrightarrow{\ x\mapsto 3x-1\ }
\mathbb R
\xrightarrow{\ y\mapsto y^2\ }
[0,\infty).
$$

Esta perspectiva será importante muchas veces: una función complicada puede entenderse descomponiéndola en funciones más simples, y una función nueva puede construirse encadenando transformaciones conocidas.

### El orden importa: la composición no es conmutativa

El hecho de que $g\circ f$ exista no implica que $f\circ g$ exista. Para la segunda composición hay que realizar **otra** auditoría de dominios.

Y aun cuando ambas existan, no tienen por qué ser iguales.

::: {#exm-t1-0024}
**Dos composiciones existentes y distintas.** Sean

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x+1,
$$

y

$$
g\colon\mathbb R\to\mathbb R,
\qquad
 g(x)=x^2.
$$

Ambas composiciones están definidas sobre todo $\mathbb R$. Sin embargo,

$$
(g\circ f)(x)
=g(x+1)
=(x+1)^2,
$$

mientras que

$$
(f\circ g)(x)
=f(x^2)
=x^2+1.
$$

Por ejemplo, en $x=1$,

$$
(g\circ f)(1)=4,
\qquad
(f\circ g)(1)=2.
$$

Por tanto,

$$
\boxed{g\circ f\ne f\circ g.}
$$
:::

Este contraejemplo basta para descartar una supuesta ley de conmutatividad universal. La composición tiene otra propiedad, en cambio, que sí es universal cuando las funciones están tipadas de manera compatible: **la asociatividad**.

### Asociatividad: tres etapas, una sola cadena

Supongamos

$$
f\colon A\to B,
\qquad
g\colon B\to C,
\qquad
h\colon C\to D.
$$

Podemos componer primero $f$ con $g$ y después aplicar $h$:

$$
h\circ(g\circ f).
$$

O podemos componer primero $g$ con $h$ y después anteponer $f$:

$$
(h\circ g)\circ f.
$$

La intuición sugiere que ambas rutas ejecutan las mismas tres etapas

$$
x\longmapsto f(x)\longmapsto g(f(x))\longmapsto h(g(f(x))).
$$

Pero, según nuestra convención de igualdad de funciones, para demostrar que las dos composiciones son iguales no basta con observar que la fórmula final «parece la misma». Debemos comprobar primero que poseen el mismo dominio y codominio, y después que coinciden en cada punto.

::: {#prp-t1-0013}
**Asociatividad de la composición.** Sean

$$
f\colon A\to B,
\qquad
g\colon B\to C,
\qquad
h\colon C\to D.
$$

Entonces

$$
\boxed{
h\circ(g\circ f)
=
(h\circ g)\circ f.
}
$$
:::

**Idea de la prueba.** Las dos funciones empiezan en $A$ y terminan en $D$. Por tanto, una vez auditados los tipos, basta comprobar que asignan la misma salida a cada $x\in A$.

**Demostración.** Como

$$
g\circ f\colon A\to C,
$$

la composición

$$
h\circ(g\circ f)\colon A\to D
$$

está bien definida. Del mismo modo,

$$
h\circ g\colon B\to D,
$$

por lo que

$$
(h\circ g)\circ f\colon A\to D
$$

también está bien definida.

Así, ambas funciones tienen dominio $A$ y codominio $D$.

Sea ahora $x\in A$. Entonces

$$
\begin{aligned}
\bigl(h\circ(g\circ f)\bigr)(x)
&=h\bigl((g\circ f)(x)\bigr)\\
&=h(g(f(x)))\\
&=(h\circ g)(f(x))\\
&=\bigl((h\circ g)\circ f\bigr)(x).
\end{aligned}
$$

Como las dos funciones tienen el mismo dominio, el mismo codominio y coinciden en cada $x\in A$, son iguales. $\square$

::: {.callout-note title="Después de la prueba"}
La asociatividad permite escribir sin ambigüedad

$$
h\circ g\circ f
$$

cuando los tipos son compatibles. Los paréntesis pueden omitirse porque cualquier agrupación admisible produce la misma función.

Pero **no** podemos alterar el orden:

$$
h\circ g\circ f
$$

significa aplicar primero $f$, después $g$ y finalmente $h$.
:::

### La identidad no transforma nada

La función identidad

$$
\operatorname{id}_A\colon A\to A,
\qquad
\operatorname{id}_A(x)=x,
$$

parece demasiado simple para merecer un nombre. Su función estructural, sin embargo, es importante: actúa como una operación neutra para la composición.

Si

$$
f\colon A\to B,
$$

entonces podemos componer $f$ por la derecha con $\operatorname{id}_A$ y por la izquierda con $\operatorname{id}_B$.

::: {#prp-t1-0014}
**Leyes de identidad.** Para toda función

$$
f\colon A\to B,
$$

se cumple

$$
\boxed{
\operatorname{id}_B\circ f=f
\qquad\text{y}\qquad
f\circ\operatorname{id}_A=f.
}
$$
:::

**Demostración.** Las composiciones están bien definidas porque $f(A)\subseteq B$ y $\operatorname{id}_A(A)=A$.

Además,

$$
\operatorname{id}_B\circ f\colon A\to B,
$$

igual que $f$. Para cada $x\in A$,

$$
(\operatorname{id}_B\circ f)(x)
=
\operatorname{id}_B(f(x))
=
f(x).
$$

Por la convención de igualdad de funciones,

$$
\operatorname{id}_B\circ f=f.
$$

Análogamente,

$$
f\circ\operatorname{id}_A\colon A\to B,
$$

y para cada $x\in A$,

$$
(f\circ\operatorname{id}_A)(x)
=f(\operatorname{id}_A(x))
=f(x).
$$

Por tanto,

$$
f\circ\operatorname{id}_A=f.
$$

$\square$

La posición de la identidad importa para que los tipos coincidan. A la izquierda de $f$ aparece la identidad del **codominio** $B$; a la derecha aparece la identidad del **dominio** $A$.

### Qué sucede con inyectividad y sobreyectividad al componer

La sección anterior separó dos arquitecturas de prueba:

- para inyectividad, partimos de una igualdad de salidas;
- para sobreyectividad, partimos de una salida arbitraria y construimos un antecedente.

La composición permite ver ambas arquitecturas en cadena.

::: {#prp-t1-0015}
**Preservación por composición.** Sean

$$
f\colon A\to B,
\qquad
g\colon B\to C.
$$

Entonces:

1. si $f$ y $g$ son inyectivas, $g\circ f$ es inyectiva;
2. si $f$ y $g$ son sobreyectivas, $g\circ f$ es sobreyectiva;
3. si $f$ y $g$ son biyectivas, $g\circ f$ es biyectiva.
:::

**Idea de la prueba.** Para la inyectividad, una igualdad al final de la cadena debe retroceder primero a través de $g$ y después a través de $f$. Para la sobreyectividad, comenzamos en el codominio final y construimos antecedentes en sentido contrario al orden de aplicación: primero uno bajo $g$ y luego uno bajo $f$.

**Demostración.**

**1. Inyectividad.** Supongamos que $f$ y $g$ son inyectivas. Sean $x_1,x_2\in A$ y supongamos

$$
(g\circ f)(x_1)=(g\circ f)(x_2).
$$

Por definición de composición,

$$
g(f(x_1))=g(f(x_2)).
$$

Como $g$ es inyectiva,

$$
f(x_1)=f(x_2).
$$

Y como $f$ es inyectiva,

$$
x_1=x_2.
$$

Por tanto, $g\circ f$ es inyectiva.

**2. Sobreyectividad.** Supongamos que $f$ y $g$ son sobreyectivas. Sea $z\in C$ arbitrario.

Como $g$ es sobreyectiva, existe $y\in B$ tal que

$$
g(y)=z.
$$

Como $f$ es sobreyectiva, existe $x\in A$ tal que

$$
f(x)=y.
$$

Entonces

$$
(g\circ f)(x)
=g(f(x))
=g(y)
=z.
$$

Hemos encontrado, para un $z\in C$ arbitrario, un $x\in A$ cuya imagen por $g\circ f$ es $z$. Por tanto, $g\circ f$ es sobreyectiva.

**3. Biyectividad.** Si $f$ y $g$ son biyectivas, ambas son inyectivas y sobreyectivas. Por las partes 1 y 2, $g\circ f$ es inyectiva y sobreyectiva; por tanto, es biyectiva. $\square$

### Leer la composición como una cadena de dependencias

Hay una diferencia instructiva entre calcular y demostrar.

Para **evaluar**

$$
(g\circ f)(x),
$$

avanzamos en el orden natural de la cadena:

$$
x
\xrightarrow{f}
f(x)
\xrightarrow{g}
g(f(x)).
$$

Para demostrar **sobreyectividad**, en cambio, la construcción de testigos recorre la cadena hacia atrás:

$$
z\in C
\xleftarrow{g}
y\in B
\xleftarrow{f}
x\in A.
$$

Y para demostrar **inyectividad**, una igualdad de salidas también retrocede:

$$
g(f(x_1))=g(f(x_2))
\Longrightarrow
f(x_1)=f(x_2)
\Longrightarrow
x_1=x_2.
$$

Esta doble lectura —hacia delante para evaluar, hacia atrás para recuperar información— prepara una pregunta inevitable. Si una función es biyectiva, cada salida corresponde a exactamente una entrada. ¿Podemos convertir sistemáticamente esa correspondencia en una nueva función que deshaga la original?

Esa será la cuestión de §2.5. Por ahora, el mapa conceptual queda ampliado a

$$
\boxed{
\text{función completa}
\to
\text{imagen/preimagen}
\to
\text{clasificación}
\to
\text{composición e identidad}.
}
$$

## Funciones inversas: cuándo se puede deshacer una función {#sec-t1-c03-05}

La sección anterior terminó con una pregunta natural. Si una función

$$
f\colon A\to B
$$

es biyectiva, cada elemento de $B$ procede de **exactamente un** elemento de $A$. ¿Podemos utilizar esa correspondencia para construir una nueva función que recorra el proceso en sentido contrario?

La idea de «deshacer» una función es familiar en ejemplos elementales. Si una regla suma $5$, esperamos deshacerla restando $5$; si multiplica por $3$, esperamos deshacerla dividiendo por $3$. Pero una función general no tiene por qué admitir una operación inversa. Antes de buscar fórmulas necesitamos identificar la condición estructural que hace posible la recuperación de la entrada.

Supongamos, por ejemplo,

$$
f\colon\mathbb R\to[0,\infty),
\qquad
f(x)=x^2.
$$

La función es sobreyectiva, pero no inyectiva. Si la salida es $4$, hay dos entradas posibles:

$$
f(2)=4,
\qquad
f(-2)=4.
$$

Por tanto, intentar «deshacer» $f$ enviando $4$ a su antecedente no produce una salida única.

En cambio, para

$$
k\colon[0,\infty)\to\mathbb R,
\qquad
k(x)=x^2,
$$

la función es inyectiva, pero no sobreyectiva. Cada valor alcanzado tiene un único antecedente, pero un número como $-1$ no tiene antecedente alguno. Una supuesta inversa definida sobre todo el codominio $\mathbb R$ fallaría ahora por existencia.

Los dos obstáculos son exactamente los que distinguimos al definir una función:

$$
\boxed{
\text{sobreyectividad}
\Rightarrow
\text{existencia del antecedente},
\qquad
\text{inyectividad}
\Rightarrow
\text{unicidad del antecedente}.
}
$$

La biyectividad reúne ambas condiciones.

### Qué significa realmente deshacer una función

La composición y la identidad nos permiten formular la idea sin depender de una fórmula algebraica.

::: {#def-t1-0024}
**Función inversa.** Sea

$$
f\colon A\to B.
$$

Una función

$$
g\colon B\to A
$$

se llama **inversa** de $f$ si satisface simultáneamente

$$
g\circ f=\operatorname{id}_A
$$

y

$$
f\circ g=\operatorname{id}_B.
$$

El teorema siguiente demostrará que, cuando tal función existe, es única. En ese caso se denota por

$$
f^{-1}\colon B\to A.
$$
:::

Las dos identidades expresan dos maneras de recuperar el punto de partida.

Si comenzamos con $x\in A$, aplicamos primero $f$ y después la inversa, debemos volver a $x$:

$$
f^{-1}(f(x))=x.
$$

Si comenzamos con $y\in B$, aplicamos primero la inversa y después $f$, debemos volver a $y$:

$$
f(f^{-1}(y))=y.
$$

Así, una inversa no es simplemente una fórmula que «parece deshacer» otra. Es una función tipada en la dirección contraria y debe deshacer a $f$ **en ambos sentidos**.

::: {.callout-warning title="No confundir tres notaciones"}
Las expresiones siguientes son conceptualmente distintas:

1. **Función inversa:** si $f\colon A\to B$ es biyectiva,
   $$
   f^{-1}\colon B\to A.
   $$
2. **Preimagen de un conjunto:** para cualquier función $f\colon A\to B$ y cualquier $E\subseteq B$,
   $$
   f^{-1}(E)=\{x\in A:f(x)\in E\}.
   $$
3. **Recíproco de una función real:** cuando $f(x)\ne0$,
   $$
   \frac1f(x)=\frac{1}{f(x)}.
   $$

La preimagen existe como operación sobre subconjuntos aunque $f$ no sea biyectiva. La función inversa, en cambio, solo existirá bajo una condición que demostraremos enseguida.
:::

### La condición exacta: biyectividad

Ahora podemos demostrar el resultado central. No se trata de una regla mnemotécnica: la prueba muestra por qué las dos mitades de la biyectividad son precisamente las dos mitades de existencia y unicidad.

::: {#thm-t1-0007}
**Existencia de la función inversa.** Sea

$$
f\colon A\to B.
$$

Entonces $f$ admite una función inversa

$$
f^{-1}\colon B\to A
$$

si y solo si $f$ es biyectiva.

Cuando existe, la inversa es única.
:::

**Idea de la prueba.** En un sentido, si una función $g$ deshace a $f$, las identidades de composición obligan a que $f$ no identifique dos entradas distintas y a que todo elemento del codominio tenga antecedente. En el otro sentido, si $f$ es biyectiva, para cada $y\in B$ existe exactamente un $x\in A$ con $f(x)=y$; definimos la inversa asignando a $y$ ese único antecedente.

**Demostración.** Probaremos las dos implicaciones por separado.

**$(\Rightarrow)$ Supongamos que $f$ admite inversa.** Sea

$$
g\colon B\to A
$$

una inversa de $f$. Entonces

$$
g\circ f=\operatorname{id}_A,
\qquad
f\circ g=\operatorname{id}_B.
$$

Primero demostraremos que $f$ es inyectiva. Sean $x_1,x_2\in A$ y supongamos

$$
f(x_1)=f(x_2).
$$

Aplicamos $g$ a ambos miembros:

$$
g(f(x_1))=g(f(x_2)).
$$

Como $g\circ f=\operatorname{id}_A$,

$$
x_1=x_2.
$$

Por tanto, $f$ es inyectiva.

Ahora demostraremos que $f$ es sobreyectiva. Sea $y\in B$ arbitrario. Como $g(y)\in A$, podemos elegir

$$
x=g(y).
$$

Entonces

$$
f(x)
=f(g(y))
=(f\circ g)(y)
=\operatorname{id}_B(y)
=y.
$$

Así, todo $y\in B$ posee un antecedente bajo $f$. Por tanto, $f$ es sobreyectiva.

Concluimos que $f$ es biyectiva.

**$(\Leftarrow)$ Supongamos ahora que $f$ es biyectiva.** Queremos construir una función de $B$ en $A$ que recupere antecedentes.

Sea $y\in B$. Como $f$ es sobreyectiva, existe al menos un $x\in A$ tal que

$$
f(x)=y.
$$

Como $f$ es inyectiva, ese $x$ es único: si $x_1,x_2\in A$ satisfacen

$$
f(x_1)=y=f(x_2),
$$

entonces

$$
f(x_1)=f(x_2),
$$

y la inyectividad implica

$$
x_1=x_2.
$$

Por tanto, para cada $y\in B$ existe un único $x\in A$ con $f(x)=y$. Podemos definir

$$
g\colon B\to A
$$

por la regla

$$
g(y)=\text{el único }x\in A\text{ tal que }f(x)=y.
$$

Verifiquemos ahora que $g$ deshace a $f$ en ambos sentidos.

Sea $x\in A$. El elemento $x$ es un antecedente de $f(x)$. Como $g(f(x))$ está definido precisamente como el único antecedente de $f(x)$,

$$
g(f(x))=x.
$$

Por tanto,

$$
g\circ f=\operatorname{id}_A.
$$

Sea ahora $y\in B$. Por definición de $g(y)$,

$$
f(g(y))=y.
$$

Luego

$$
f\circ g=\operatorname{id}_B.
$$

Así, $g$ es una inversa de $f$.

Nos falta justificar la unicidad. Supongamos que

$$
g,h\colon B\to A
$$

son ambas inversas de $f$. Entonces

$$
g\circ f=\operatorname{id}_A,
\qquad
f\circ h=\operatorname{id}_B.
$$

Usando las leyes de identidad y la asociatividad demostradas en §2.4,

$$
\begin{aligned}
g
&=g\circ\operatorname{id}_B\\
&=g\circ(f\circ h)\\
&=(g\circ f)\circ h\\
&=\operatorname{id}_A\circ h\\
&=h.
\end{aligned}
$$

Por tanto, la inversa es única. Podemos denotarla sin ambigüedad por $f^{-1}$. $\square$

::: {.callout-note title="Después de la prueba"}
La equivalencia anterior puede recordarse por su estructura lógica, no por una frase aislada:

$$
\boxed{
\begin{array}{ccl}
\text{sobreyectiva} &\Longleftrightarrow& \text{cada salida tiene al menos un antecedente},\\[4pt]
\text{inyectiva} &\Longleftrightarrow& \text{cada salida tiene a lo sumo un antecedente},\\[4pt]
\text{biyectiva} &\Longleftrightarrow& \text{cada salida tiene exactamente un antecedente}.
\end{array}
}
$$

La última línea es precisamente lo que permite convertir «buscar antecedentes» en una función $B\to A$.
:::

### Las identidades de inversión

Una vez que $f$ es biyectiva, el teorema nos permite escribir

$$
f^{-1}\colon B\to A
$$

y las dos identidades fundamentales quedan

$$
\boxed{
 f^{-1}\circ f=\operatorname{id}_A,
 \qquad
 f\circ f^{-1}=\operatorname{id}_B.
}
$$

Punto a punto,

$$
\boxed{
 f^{-1}(f(x))=x\quad(x\in A),
 \qquad
 f(f^{-1}(y))=y\quad(y\in B).
}
$$

Además, $f^{-1}$ también es biyectiva. En efecto, acabamos de ver que $f$ es una inversa de $f^{-1}$, porque las mismas dos identidades se leen ahora en el sentido contrario. Por tanto,

$$
\boxed{(f^{-1})^{-1}=f.}
$$

### La inversa de una composición invierte el orden

La composición de biyecciones vuelve a ser biyectiva por §2.4. Así que, si

$$
f\colon A\to B,
\qquad
g\colon B\to C
$$

son biyectivas, la función

$$
g\circ f\colon A\to C
$$

admite inversa.

Para deshacer dos etapas, la intuición correcta es recorrerlas en orden contrario. Si primero aplicamos $f$ y después $g$, debemos deshacer primero $g$ y después $f$.

::: {#cor-t1-0005}
**Inversa de una composición.** Si

$$
f\colon A\to B,
\qquad
g\colon B\to C
$$

son biyectivas, entonces

$$
\boxed{
(g\circ f)^{-1}=f^{-1}\circ g^{-1}.
}
$$
:::

**Idea de la prueba.** Como la inversa de una función es única, basta demostrar que $f^{-1}\circ g^{-1}$ deshace a $g\circ f$ por ambos lados.

**Demostración.** Por el teorema anterior existen

$$
f^{-1}\colon B\to A,
\qquad
g^{-1}\colon C\to B.
$$

Por tanto,

$$
f^{-1}\circ g^{-1}\colon C\to A
$$

está bien definida.

Usando asociatividad e identidades,

$$
\begin{aligned}
(f^{-1}\circ g^{-1})\circ(g\circ f)
&=f^{-1}\circ(g^{-1}\circ g)\circ f\\
&=f^{-1}\circ\operatorname{id}_B\circ f\\
&=f^{-1}\circ f\\
&=\operatorname{id}_A.
\end{aligned}
$$

De manera análoga,

$$
\begin{aligned}
(g\circ f)\circ(f^{-1}\circ g^{-1})
&=g\circ(f\circ f^{-1})\circ g^{-1}\\
&=g\circ\operatorname{id}_B\circ g^{-1}\\
&=g\circ g^{-1}\\
&=\operatorname{id}_C.
\end{aligned}
$$

Así, $f^{-1}\circ g^{-1}$ es una inversa de $g\circ f$. Por unicidad,

$$
(g\circ f)^{-1}=f^{-1}\circ g^{-1}.
$$

$\square$

El orden invertido no es una convención arbitraria. Si una cadena hace

$$
A\xrightarrow{f}B\xrightarrow{g}C,
$$

la cadena inversa debe regresar como

$$
C\xrightarrow{g^{-1}}B\xrightarrow{f^{-1}}A.
$$

### La raíz cuadrada aparece como una inversa

Volvamos a la familia de funciones con la que comenzó el capítulo.

::: {#exm-t1-0025}
**El cuadrado restringido y la raíz cuadrada.** Consideremos

$$
q\colon[0,\infty)\to[0,\infty),
\qquad
q(x)=x^2.
$$

En §2.3 demostramos que $q$ es biyectiva: es inyectiva porque en el dominio no negativo el cuadrado conserva el orden estricto, y es sobreyectiva porque cada $y\ge0$ posee una raíz cuadrada no negativa.

Por el Teorema @thm-t1-0007, $q$ admite inversa. Para $y\ge0$, el único $x\ge0$ que satisface

$$
x^2=y
$$

es

$$
x=\sqrt y.
$$

Por tanto,

$$
q^{-1}\colon[0,\infty)\to[0,\infty),
\qquad
q^{-1}(y)=\sqrt y.
$$

Las identidades de inversión dicen

$$
\sqrt{x^2}=x
\qquad(x\ge0)
$$

y

$$
(\sqrt y)^2=y
\qquad(y\ge0).
$$

La restricción $x\ge0$ en la primera identidad es esencial. Sobre todo $\mathbb R$,

$$
\sqrt{x^2}=|x|,
$$

no $x$ en general. Precisamente por eso la función $x\mapsto x^2$ sobre $\mathbb R$ no puede tener como inversa a la raíz cuadrada: antes hay que eliminar la duplicación $x$ y $-x$ restringiendo legítimamente el dominio.
:::

Este ejemplo muestra una idea que reaparecerá muchas veces: una función que no es invertible globalmente puede volverse invertible después de restringir su dominio de modo que sea inyectiva y tomando como codominio exactamente la imagen pertinente.

### Inversa no significa recíproco

Consideremos la función biyectiva

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=2x+1.
$$

Para encontrar su inversa resolvemos

$$
y=2x+1
$$

para $x$:

$$
x=\frac{y-1}{2}.
$$

Por tanto,

$$
f^{-1}(y)=\frac{y-1}{2}.
$$

En cambio, el recíproco de los valores de $f$ es

$$
\frac1{f(x)}=\frac1{2x+1},
$$

que ni siquiera está definido en $x=-\tfrac12$.

Así,

$$
\boxed{
 f^{-1}\ne\frac1f
}
$$

en general. El exponente $-1$ en $f^{-1}$ indica **inversión respecto de la composición**, no inversión multiplicativa de valores.

### Función inversa y preimagen: misma notación, objetos distintos

Terminemos resolviendo la ambigüedad que apareció por primera vez en §2.2.

Si

$$
f\colon A\to B
$$

es una función cualquiera y $E\subseteq B$, la escritura

$$
f^{-1}(E)
$$

designa la **preimagen del conjunto** $E$:

$$
f^{-1}(E)=\{x\in A:f(x)\in E\}.
$$

Esto tiene sentido aunque $f$ no sea biyectiva.

Si $f$ es biyectiva, en cambio, también existe la función inversa

$$
f^{-1}\colon B\to A.
$$

Entonces, para un punto $y\in B$,

$$
f^{-1}(y)
$$

es un elemento de $A$: el único antecedente de $y$.

El tipo de argumento permite distinguir ambos usos:

$$
\boxed{
\begin{array}{ccl}
y\in B &\Longrightarrow& f^{-1}(y)\in A\quad\text{si existe la función inversa},\\[4pt]
E\subseteq B &\Longrightarrow& f^{-1}(E)\subseteq A\quad\text{para cualquier función}.
\end{array}
}
$$

Cuando $f$ es biyectiva, ambos significados son compatibles: la preimagen de un conjunto $E$ está formada exactamente por las imágenes de sus elementos bajo la función inversa. Pero no debemos usar esa compatibilidad para olvidar que la operación de preimagen existe en un contexto mucho más general.

La idea central de la sección puede resumirse así:

$$
\boxed{
\text{cada salida tiene exactamente un antecedente}
\iff
\text{la función es biyectiva}
\iff
\text{existe una función inversa}.
}
$$

En §2.6 volveremos a imágenes y preimágenes, ahora con una pregunta distinta: cómo interactúan con uniones, intersecciones, diferencias y complementos, y en qué punto la inyectividad se vuelve necesaria para transformar una inclusión en igualdad.

## El álgebra de imágenes y preimágenes {#sec-t1-c03-06}

En §2.2 aprendimos a calcular imágenes y preimágenes de conjuntos concretos. Ahora cambia la pregunta. Ya no queremos saber solamente **qué conjunto resulta**, sino **cómo interactúan estas operaciones con las operaciones de conjuntos** fijadas en nuestras convenciones iniciales.

Sea

$$
f\colon A\to B.
$$

Si $E,F\subseteq A$ y $S,T\subseteq B$, podemos preguntar, por ejemplo, si es legítimo escribir

$$
f(E\cup F)=f(E)\cup f(F),
$$

$$
f(E\cap F)=f(E)\cap f(F),
$$

o

$$
f^{-1}(S\cap T)=f^{-1}(S)\cap f^{-1}(T).
$$

Las tres fórmulas parecen naturales. Dos de ellas son siempre correctas. La restante puede fallar.

Lo importante de esta sección no será memorizar una tabla de identidades. Queremos aprender algo más útil: **cómo auditar una igualdad de conjuntos hasta descubrir exactamente qué hipótesis le falta**.

### Una primera ley: la inclusión se conserva hacia delante y hacia atrás

Empecemos por una propiedad que no presenta ninguna sorpresa.

Si

$$
E\subseteq F\subseteq A,
$$

entonces todo elemento de $E$ pertenece también a $F$. Por tanto, cualquier valor obtenido usando una entrada de $E$ también se obtiene usando una entrada de $F$:

$$
\boxed{E\subseteq F\Longrightarrow f(E)\subseteq f(F).}
$$

Del mismo modo, si

$$
S\subseteq T\subseteq B,
$$

y $x\in f^{-1}(S)$, entonces $f(x)\in S\subseteq T$, de modo que $x\in f^{-1}(T)$. Por tanto,

$$
\boxed{S\subseteq T\Longrightarrow f^{-1}(S)\subseteq f^{-1}(T).}
$$

Tanto la imagen como la preimagen son, pues, **monótonas respecto de la inclusión de conjuntos**. Aquí la palabra «monótona» se refiere solamente al orden dado por $\subseteq$ entre subconjuntos; no estamos introduciendo todavía la monotonía de funciones reales que estudiaremos en §2.9.

### Una igualdad muy plausible

Probemos ahora algo menos automático. Supongamos que $E,F\subseteq A$. Es tentador afirmar

$$
\boxed{f(E\cap F)=f(E)\cap f(F).}
$$

La igualdad parece razonable: si una entrada pertenece a ambos conjuntos, su imagen pertenece a ambas imágenes. Pero una igualdad de conjuntos exige **dos inclusiones**. Auditémoslas por separado.

#### Primera inclusión

Queremos demostrar

$$
f(E\cap F)\subseteq f(E)\cap f(F).
$$

Sea

$$
y\in f(E\cap F).
$$

Por definición de imagen, existe $x\in E\cap F$ tal que

$$
f(x)=y.
$$

Como $x\in E\cap F$, tenemos simultáneamente

$$
x\in E
\qquad\text{y}\qquad
x\in F.
$$

Por tanto,

$$
y=f(x)\in f(E)
$$

y también

$$
y=f(x)\in f(F).
$$

Así,

$$
y\in f(E)\cap f(F).
$$

Hemos demostrado, sin ninguna hipótesis adicional sobre $f$, que

$$
\boxed{f(E\cap F)\subseteq f(E)\cap f(F).}
$$

Hasta aquí la conjetura sigue viva.

#### Intentemos ahora la inclusión inversa

Queremos probar

$$
f(E)\cap f(F)\subseteq f(E\cap F).
$$

Sea

$$
y\in f(E)\cap f(F).
$$

Entonces

$$
y\in f(E)
\qquad\text{y}\qquad
y\in f(F).
$$

La primera pertenencia nos da **algún** $u\in E$ tal que

$$
f(u)=y.
$$

La segunda nos da **algún** $v\in F$ tal que

$$
f(v)=y.
$$

Por tanto,

$$
f(u)=f(v).
$$

Y aquí la demostración se atasca.

Para concluir que $y\in f(E\cap F)$ necesitaríamos encontrar **una sola entrada** que perteneciera simultáneamente a $E$ y a $F$. Pero lo único que hemos obtenido son dos posibles testigos:

$$
u\in E,
\qquad
v\in F,
\qquad
f(u)=f(v).
$$

Nada de lo demostrado hasta ahora permite afirmar que

$$
u=v.
$$

::: {.callout-note title="La prueba fallida ha descubierto una hipótesis"}
El punto donde la demostración se detiene no es ruido algebraico. Es información matemática precisa.

Necesitamos convertir

$$
f(u)=f(v)
$$

en

$$
u=v.
$$

Pero esa es exactamente la definición de **inyectividad**.

La prueba fallida nos ha dicho qué hipótesis faltaba.
:::

Si $f$ es inyectiva, entonces de $f(u)=f(v)$ obtenemos $u=v$. Llamemos $x$ a ese elemento común. Como

$$
x=u\in E
$$

y

$$
x=v\in F,
$$

tenemos

$$
x\in E\cap F.
$$

Además,

$$
f(x)=y.
$$

Por tanto,

$$
y\in f(E\cap F).
$$

Así, bajo inyectividad, la inclusión inversa sí queda demostrada.

Antes de formular el resultado correcto, debemos comprobar que la hipótesis añadida es realmente necesaria y no solo un artefacto de nuestra estrategia de prueba.

::: {#exm-t1-0026}
**La imagen no conserva siempre las intersecciones.** Sea

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2,
$$

y consideremos

$$
E=\{-1\},
\qquad
F=\{1\}.
$$

Como

$$
E\cap F=\varnothing,
$$

tenemos

$$
f(E\cap F)=f(\varnothing)=\varnothing.
$$

Sin embargo,

$$
f(E)=\{1\}
$$

y

$$
f(F)=\{1\}.
$$

Por tanto,

$$
f(E)\cap f(F)=\{1\}.
$$

En consecuencia,

$$
\boxed{
f(E\cap F)
=\varnothing
\subsetneq
\{1\}
=f(E)\cap f(F).
}
$$

El mecanismo del fallo es exactamente el diagnosticado en la prueba: los dos testigos son distintos,

$$
-1\ne1,
$$

pero tienen la misma imagen,

$$
f(-1)=f(1)=1.
$$
:::

Ya podemos registrar la versión correcta de las leyes básicas de imagen.

::: {#prp-t1-0017}
**Leyes básicas de la imagen.** Sea $f\colon A\to B$ y sean $E,F\subseteq A$.

1. Si $E\subseteq F$, entonces
   $$
   f(E)\subseteq f(F).
   $$
2. La imagen conserva uniones:
   $$
   f(E\cup F)=f(E)\cup f(F).
   $$
3. Para intersecciones siempre se tiene
   $$
   f(E\cap F)\subseteq f(E)\cap f(F).
   $$
4. Si además $f$ es inyectiva, entonces
   $$
   f(E\cap F)=f(E)\cap f(F).
   $$
:::

Ya hemos demostrado los apartados 1, 3 y 4. Probemos el apartado 2 para completar la proposición.

**Idea de la prueba de la unión.** Pertenecer a $E\cup F$ significa pertenecer a $E$ **o** a $F$. Esa disyunción pasa sin pérdida a las imágenes porque un mismo testigo $x$ basta para justificar una de las dos alternativas.

**Demostración.** Sea $y\in f(E\cup F)$. Entonces existe $x\in E\cup F$ tal que $f(x)=y$. Como $x\in E$ o $x\in F$, tenemos $y\in f(E)$ o $y\in f(F)$. Por tanto,

$$
y\in f(E)\cup f(F).
$$

Esto demuestra

$$
f(E\cup F)\subseteq f(E)\cup f(F).
$$

Para la inclusión inversa, sea $y\in f(E)\cup f(F)$. Entonces $y\in f(E)$ o $y\in f(F)$. En el primer caso existe $x\in E$ con $f(x)=y$; como $E\subseteq E\cup F$, ese mismo $x$ pertenece a $E\cup F$, y por tanto $y\in f(E\cup F)$. El segundo caso es análogo.

Luego

$$
f(E)\cup f(F)\subseteq f(E\cup F).
$$

y, por doble inclusión,

$$
\boxed{f(E\cup F)=f(E)\cup f(F).}
$$

$\square$

### Qué cambió lógicamente entre unión e intersección

Vale la pena detenerse aquí porque la diferencia es más profunda que una colección de símbolos.

Para la unión,

$$
y\in f(E\cup F)
$$

significa que existe un $x$ tal que

$$
x\in E\cup F
\qquad\text{y}\qquad
f(x)=y.
$$

La condición $x\in E\cup F$ se descompone como

$$
x\in E\quad\text{o}\quad x\in F.
$$

No aparecen dos testigos diferentes.

En cambio,

$$
y\in f(E)\cap f(F)
$$

significa simultáneamente

$$
\exists u\in E\quad f(u)=y
$$

y

$$
\exists v\in F\quad f(v)=y.
$$

Los cuantificadores existenciales pueden producir testigos distintos. Para fusionarlos necesitamos saber que una misma salida no puede proceder de dos entradas diferentes. Esa es exactamente la función estructural de la inyectividad.

Podemos condensarlo así:

$$
\boxed{
\begin{array}{c}
\text{la unión no obliga a identificar testigos;}\\[4pt]
\text{la intersección de imágenes puede exigir identificar dos testigos.}
\end{array}
}
$$

### Las preimágenes se comportan mejor

Pasemos ahora al sentido contrario. Sea $S\subseteq B$. Recordemos la equivalencia elemental

$$
x\in f^{-1}(S)
\iff
f(x)\in S.
$$

Aquí no necesitamos buscar un antecedente: **el punto $x$ ya está fijado**. Solo comprobamos si su imagen satisface una condición de pertenencia.

Esta diferencia hace que las operaciones de conjuntos se transporten con mucha más fidelidad mediante preimágenes.

::: {#prp-t1-0016}
**Leyes de preimagen.** Sea $f\colon A\to B$ y sean $S,T\subseteq B$.

1. Si $S\subseteq T$, entonces
   $$
   f^{-1}(S)\subseteq f^{-1}(T).
   $$
2. La preimagen conserva uniones:
   $$
   f^{-1}(S\cup T)
   =
   f^{-1}(S)\cup f^{-1}(T).
   $$
3. La preimagen conserva intersecciones:
   $$
   f^{-1}(S\cap T)
   =
   f^{-1}(S)\cap f^{-1}(T).
   $$
4. La preimagen conserva diferencias:
   $$
   f^{-1}(S\setminus T)
   =
   f^{-1}(S)\setminus f^{-1}(T).
   $$
5. En particular, para el complemento relativo al codominio,
   $$
   f^{-1}(B\setminus S)
   =
   A\setminus f^{-1}(S).
   $$
6. Si $g\colon B\to C$ y $R\subseteq C$, entonces
   $$
   (g\circ f)^{-1}(R)
   =
   f^{-1}\bigl(g^{-1}(R)\bigr).
   $$
:::

El apartado 1 ya fue demostrado al comienzo de la sección. Los demás pueden probarse de manera muy uniforme siguiendo la pertenencia de un punto arbitrario.

**Demostración de la unión.** Sea $x\in A$. Entonces

$$
\begin{aligned}
x\in f^{-1}(S\cup T)
&\iff f(x)\in S\cup T\\
&\iff \bigl(f(x)\in S\text{ o }f(x)\in T\bigr)\\
&\iff \bigl(x\in f^{-1}(S)\text{ o }x\in f^{-1}(T)\bigr)\\
&\iff x\in f^{-1}(S)\cup f^{-1}(T).
\end{aligned}
$$

Como la equivalencia vale para todo $x\in A$,

$$
f^{-1}(S\cup T)
=
f^{-1}(S)\cup f^{-1}(T).
$$

**Demostración de la intersección.** Del mismo modo,

$$
\begin{aligned}
x\in f^{-1}(S\cap T)
&\iff f(x)\in S\cap T\\
&\iff \bigl(f(x)\in S\text{ y }f(x)\in T\bigr)\\
&\iff \bigl(x\in f^{-1}(S)\text{ y }x\in f^{-1}(T)\bigr)\\
&\iff x\in f^{-1}(S)\cap f^{-1}(T).
\end{aligned}
$$

Por tanto,

$$
f^{-1}(S\cap T)
=
f^{-1}(S)\cap f^{-1}(T).
$$

Observa la diferencia con las imágenes: aquí el mismo $x$ aparece durante toda la cadena. No surge ningún problema de «dos antecedentes posiblemente distintos».

**Demostración de la diferencia.** Para $x\in A$,

$$
\begin{aligned}
x\in f^{-1}(S\setminus T)
&\iff f(x)\in S\setminus T\\
&\iff \bigl(f(x)\in S\text{ y }f(x)\notin T\bigr)\\
&\iff \bigl(x\in f^{-1}(S)\text{ y }x\notin f^{-1}(T)\bigr)\\
&\iff x\in f^{-1}(S)\setminus f^{-1}(T).
\end{aligned}
$$

Luego

$$
f^{-1}(S\setminus T)
=
f^{-1}(S)\setminus f^{-1}(T).
$$

Tomando $S=B$ y recordando que $f^{-1}(B)=A$, obtenemos inmediatamente

$$
\boxed{
f^{-1}(B\setminus T)
=
A\setminus f^{-1}(T).
}
$$

**Demostración de la composición de preimágenes.** Sean

$$
f\colon A\to B,
\qquad
g\colon B\to C,
$$

y sea $R\subseteq C$. Para $x\in A$,

$$
\begin{aligned}
x\in(g\circ f)^{-1}(R)
&\iff (g\circ f)(x)\in R\\
&\iff g(f(x))\in R\\
&\iff f(x)\in g^{-1}(R)\\
&\iff x\in f^{-1}\bigl(g^{-1}(R)\bigr).
\end{aligned}
$$

Por tanto,

$$
\boxed{
(g\circ f)^{-1}(R)
=
f^{-1}\bigl(g^{-1}(R)\bigr).
}
$$

$\square$

::: {.callout-note title="Lectura estructural"}
La fórmula anterior tiene el mismo orden inverso que apareció en §2.5:

$$
A\xrightarrow{f}B\xrightarrow{g}C.
$$

Para decidir qué puntos de $A$ terminan dentro de $R\subseteq C$, primero preguntamos qué puntos de $B$ caen en $R$ bajo $g$ y luego qué puntos de $A$ caen en ese conjunto bajo $f$:

$$
R
\xmapsto{\,g^{-1}\,}
g^{-1}(R)
\xmapsto{\,f^{-1}\,}
f^{-1}(g^{-1}(R)).
$$

Aquí los símbolos $g^{-1}$ y $f^{-1}$ designan **preimágenes de conjuntos**; no se supone que $f$ ni $g$ sean biyectivas.
:::

### Por qué la preimagen conserva mejor el álgebra de conjuntos

Podemos explicar todas estas identidades sin volver a demostrarlas una por una.

La afirmación

$$
x\in f^{-1}(S)
$$

es simplemente otra manera de escribir

$$
f(x)\in S.
$$

Por eso, cuando combinamos conjuntos mediante unión, intersección o complemento, las operaciones lógicas correspondientes pasan directamente a través de la preimagen:

$$
\begin{array}{ccl}
\cup &\longleftrightarrow& \text{«o»},\\[4pt]
\cap &\longleftrightarrow& \text{«y»},\\[4pt]
\text{complemento} &\longleftrightarrow& \text{«no»}.
\end{array}
$$

La preimagen no tiene que elegir ni comparar antecedentes. Evalúa siempre el mismo punto $x$ y pregunta dónde cae $f(x)$.

La imagen directa tiene una estructura lógica distinta. Para afirmar

$$
y\in f(E),
$$

necesitamos un testigo:

$$
\exists x\in E\quad f(x)=y.
$$

En una intersección de imágenes pueden aparecer dos testigos distintos para una misma salida. Precisamente ahí puede perderse la igualdad.

La diferencia conceptual puede resumirse así:

$$
\boxed{
\begin{array}{c}
\text{preimagen: sustituir }f(x)\text{ en una condición de pertenencia;}\\[4pt]
\text{imagen: afirmar la existencia de algún antecedente que produzca la salida.}
\end{array}
}
$$

### Un mapa de las leyes obtenidas

Para $f\colon A\to B$, $E,F\subseteq A$ y $S,T\subseteq B$:

$$
\boxed{
\begin{array}{rcl}
f(E\cup F) &=& f(E)\cup f(F),\\[4pt]
f(E\cap F) &\subseteq& f(E)\cap f(F),\\[4pt]
f(E\cap F) &=& f(E)\cap f(F)\quad\text{si $f$ es inyectiva},\\[8pt]
f^{-1}(S\cup T) &=& f^{-1}(S)\cup f^{-1}(T),\\[4pt]
f^{-1}(S\cap T) &=& f^{-1}(S)\cap f^{-1}(T),\\[4pt]
f^{-1}(S\setminus T) &=& f^{-1}(S)\setminus f^{-1}(T),\\[4pt]
f^{-1}(B\setminus S) &=& A\setminus f^{-1}(S).
\end{array}
}
$$

No hay que memorizar este cuadro como una colección arbitraria. La asimetría procede de los cuantificadores: **la imagen introduce existencia de antecedentes; la preimagen no**.

Y, sobre todo, la sección nos deja una técnica reutilizable de investigación matemática:

$$
\boxed{
\text{conjetura}
\to
\text{doble inclusión}
\to
\text{prueba que se atasca}
\to
\text{diagnóstico del paso faltante}
\to
\text{hipótesis correcta}
\to
\text{contraejemplo sin ella}.
}
$$

En §2.7 cambiaremos de representación: estudiaremos la **gráfica** de una función como subconjunto del producto cartesiano. Allí veremos qué información estructural puede leerse de un dibujo y, con igual importancia, qué información no está contenida en la curva por sí sola.

## Gráficas: una representación, no la definición completa {#sec-t1-c03-07}

Hasta ahora hemos hablado de funciones sin necesitar dibujarlas. Esa elección fue deliberada. Antes de usar una gráfica como herramienta, conviene saber **qué representa exactamente** y qué información puede —o no puede— contener.

Cuando una función real se dibuja en el plano, cada punto de la curva registra una entrada y su salida correspondiente. Si

$$
f\colon A\to B,
$$

entonces al valor $x\in A$ le corresponde el par ordenado

$$
(x,f(x)).
$$

La primera coordenada conserva la entrada; la segunda conserva la salida. Reunir todos esos pares produce la gráfica.

::: {#def-t1-0025}
**Gráfica de una función.** Sea

$$
f\colon A\to B.
$$

La **gráfica** de $f$ es el conjunto

$$
\Gamma_f
=
\{(x,f(x)):x\in A\}
\subseteq A\times B.
$$

Equivalentemente,

$$
(x,y)\in\Gamma_f
\iff
x\in A\text{ y }y=f(x).
$$
:::

Esta definición contiene una idea importante: una gráfica no es, en primer lugar, un dibujo. Es un **conjunto de pares ordenados**.

Si $A,B\subseteq\mathbb R$, podemos representar esos pares como puntos del plano cartesiano. Entonces el conjunto $\Gamma_f$ adquiere una apariencia geométrica: puede ser una curva, varios arcos separados, un conjunto discreto de puntos o una figura mucho menos regular. Pero el objeto matemático sigue siendo el conjunto de pares.

Por ejemplo, para

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2,
$$

la gráfica es

$$
\Gamma_f
=
\{(x,x^2):x\in\mathbb R\}.
$$

El punto $(2,4)$ pertenece a la gráfica porque $f(2)=4$; el punto $(2,5)$ no pertenece porque $f(2)\ne5$.

### Qué codifica cada coordenada

La gráfica permite recuperar inmediatamente dos conjuntos que ya conocemos.

Los valores que aparecen como **primeras coordenadas** son exactamente los elementos del dominio:

$$
A
=
\{x:\exists y\ ((x,y)\in\Gamma_f)\}.
$$

Los valores que aparecen como **segundas coordenadas** son exactamente los valores efectivamente alcanzados por la función, es decir, su imagen:

$$
f(A)
=
\{y:\exists x\ ((x,y)\in\Gamma_f)\}.
$$

Así, al mirar una gráfica exacta, podemos leer horizontalmente qué entradas aparecen y verticalmente qué salidas se alcanzan.

Sin embargo, hay que advertir desde ahora una asimetría:

$$
\boxed{\text{la gráfica determina la imagen, pero no determina por sí sola un codominio mayor que la imagen}.}
$$

Volveremos sobre este punto con un ejemplo explícito. Es la misma distinción que ya encontramos entre imagen y codominio en §2.1.

### Cuándo un conjunto de puntos puede ser la gráfica de una función

Supongamos ahora que todavía no sabemos si cierto conjunto

$$
R\subseteq A\times B
$$

es la gráfica de alguna función $A\to B$.

¿Qué tendría que ocurrir?

La definición de función exige dos cosas para **cada** $x\in A$:

1. debe existir una salida $y\in B$ asociada con $x$;
2. esa salida debe ser única.

Traducido al conjunto de pares, esto significa que para cada primera coordenada permitida $x$ debe haber exactamente un par de la forma $(x,y)$ dentro de $R$.

::: {#prp-t1-0018}
**Caracterización de las gráficas funcionales.** Sean $A$ y $B$ conjuntos y sea

$$
R\subseteq A\times B.
$$

Entonces $R$ es la gráfica de una única función

$$
f\colon A\to B
$$

si y solo si para cada $x\in A$ existe un único $y\in B$ tal que

$$
(x,y)\in R.
$$
:::

**Idea de la prueba.** No necesitamos descubrir una técnica nueva. La afirmación es exactamente la definición de función escrita en el lenguaje de pares ordenados.

Si $R$ ya es la gráfica de una función, cada entrada $x$ debe aparecer emparejada con $f(x)$ y con ninguna otra salida. En la dirección inversa, si cada $x$ aparece emparejado con un único $y$, podemos definir $f(x)$ como ese único valor.

**Demostración.** Supongamos primero que

$$
R=\Gamma_f
$$

para alguna función $f\colon A\to B$. Sea $x\in A$. Como $f$ es una función, existe el valor $f(x)\in B$, y por definición de gráfica

$$
(x,f(x))\in R.
$$

Esto demuestra existencia.

Para la unicidad, supongamos que $y_1,y_2\in B$ satisfacen

$$
(x,y_1)\in R
\qquad\text{y}\qquad
(x,y_2)\in R.
$$

Como $R=\Gamma_f$, ambos pares deben tener como segunda coordenada el valor de $f$ en $x$. Por tanto,

$$
y_1=f(x)=y_2,
$$

y así $y_1=y_2$.

Recíprocamente, supongamos que para cada $x\in A$ existe un único $y\in B$ tal que $(x,y)\in R$. Definimos

$$
f\colon A\to B
$$

asignando a cada $x$ ese único $y$.

La hipótesis de existencia garantiza que la asignación está definida para todo $x\in A$, y la hipótesis de unicidad garantiza que ninguna entrada recibe dos valores incompatibles. Por tanto, $f$ es una función.

Además, por construcción,

$$
(x,y)\in R
\iff
y=f(x),
$$

de modo que

$$
R=\Gamma_f.
$$

Finalmente, la propia construcción muestra que no puede existir otra función $g\colon A\to B$ con la misma gráfica: para cada $x\in A$, tanto $f(x)$ como $g(x)$ tendrían que ser el único $y$ asociado con $x$ en $R$. Luego $f(x)=g(x)$ para todo $x\in A$. $\square$

::: {.callout-note title="Después de la prueba"}
La proposición no añade una condición externa a la definición de función. La descompone geométricamente:

$$
\boxed{
\begin{array}{c}
\text{existencia: cada entrada aparece en algún par;}\\[4pt]
\text{unicidad: cada entrada aparece con una sola segunda coordenada.}
\end{array}}
$$

El llamado «criterio de la recta vertical» será simplemente esta misma afirmación cuando $A$ y $B$ sean subconjuntos de $\mathbb R$ y dibujemos $R$ en el plano.
:::

### De existencia y unicidad al criterio de la recta vertical

Supongamos que $A,B\subseteq\mathbb R$ y que un conjunto de puntos $R\subseteq A\times B$ está dibujado en el plano.

Fijar una entrada $x=a$ significa mirar la recta vertical

$$
x=a.
$$

Los puntos donde esa vertical corta a $R$ son precisamente los pares

$$
(a,y)\in R.
$$

Por tanto:

- si la vertical no corta a $R$, la entrada $a$ no tiene salida;
- si la vertical corta a $R$ en dos o más puntos, la entrada $a$ tendría dos o más salidas;
- si la vertical corta a $R$ exactamente una vez, existe una única salida asociada con $a$.

Así obtenemos el criterio geométrico:

$$
\boxed{
R\text{ es la gráfica de una función }A\to B
\iff
\text{cada vertical }x=a\text{ con }a\in A\text{ corta a }R\text{ exactamente una vez}.}
$$

La precisión «con $a\in A$» importa. Una función cuyo dominio sea, por ejemplo, $[0,1]$ no tiene obligación de producir puntos sobre las verticales $x=2$ o $x=-5$.

::: {.callout-warning title="Error frecuente"}
La «prueba de la recta vertical» no es una regla geométrica independiente que mágicamente decida qué es una función.

Es la traducción al plano de

$$
\forall x\in A\;\exists!y\in B
\quad\text{tal que}\quad
(x,y)\in\Gamma_f.
$$

Si olvidamos el dominio, o si olvidamos que se requieren **existencia y unicidad**, el criterio pierde su significado matemático.
:::

### Una curva que no es la gráfica de una función de $x$

Consideremos el círculo unitario

$$
R
=
\{(x,y)\in\mathbb R^2:x^2+y^2=1\}.
$$

¿Puede ser la gráfica de una función

$$
f\colon[-1,1]\to\mathbb R?
$$

Tomemos $x=0$. La ecuación del círculo se convierte en

$$
y^2=1,
$$

por lo que aparecen dos valores:

$$
y=1
\qquad\text{y}\qquad
y=-1.
$$

La vertical $x=0$ corta el círculo en los puntos

$$
(0,1)
\qquad\text{y}\qquad
(0,-1).
$$

Por tanto, el círculo completo no es la gráfica de una función de $x$ en $[-1,1]$.

El problema no es que la figura sea «demasiado complicada». El problema es exactamente la falta de unicidad de la segunda coordenada.

En cambio, si conservamos solo la semicircunferencia superior, obtenemos

$$
y=\sqrt{1-x^2},
\qquad -1\le x\le1,
$$

y cada vertical correspondiente a un $x\in[-1,1]$ encuentra un único punto. La semicircunferencia inferior representa análogamente

$$
y=-\sqrt{1-x^2}.
$$

Una misma relación geométrica puede, por tanto, necesitar ser separada en partes para que cada parte represente una función de la coordenada $x$.

### Leer dominio e imagen desde la gráfica

Consideremos ahora

$$
f\colon[-2,2]\to\mathbb R,
\qquad
f(x)=x^2.
$$

Su gráfica es

$$
\Gamma_f
=
\{(x,x^2):-2\le x\le2\}.
$$

Las primeras coordenadas recorren exactamente

$$
[-2,2],
$$

que es el dominio.

Las segundas coordenadas recorren exactamente

$$
[0,4],
$$

que es la imagen.

Geométricamente podemos expresar ambas lecturas como proyecciones:

$$
\boxed{
\begin{aligned}
\operatorname{Dom}(f)
&=\{x:\exists y\ ((x,y)\in\Gamma_f)\},\\[4pt]
f(A)
&=\{y:\exists x\ ((x,y)\in\Gamma_f)\}.
\end{aligned}}
$$

En un dibujo ordinario solemos describir esto diciendo que el dominio es la «sombra» de la gráfica sobre el eje horizontal y la imagen su «sombra» sobre el eje vertical.

La metáfora es útil siempre que recordemos que detrás de ella hay cuantificadores de existencia.

### Las horizontales preguntan por antecedentes

Las verticales fijaban una **entrada** y preguntaban cuántas salidas tenía. Las rectas horizontales hacen la pregunta inversa: fijan una posible **salida** $y=b$ y preguntan cuántas entradas producen ese valor.

Los puntos donde la horizontal

$$
y=b
$$

corta a la gráfica son exactamente los pares

$$
(x,b)\in\Gamma_f,
$$

es decir, las soluciones de

$$
f(x)=b.
$$

Esta observación conecta inmediatamente la geometría con §2.3.

#### Inyectividad

La función $f$ es inyectiva si una misma salida no puede provenir de dos entradas distintas. Por tanto,

$$
\boxed{
f\text{ es inyectiva}
\iff
\text{cada recta horizontal corta }\Gamma_f\text{ en a lo sumo un punto}.}
$$

«A lo sumo uno» permite cero intersecciones: un valor $b$ que no pertenece a la imagen simplemente no es producido por ninguna entrada.

Para

$$
f(x)=x^2
\qquad(x\in[-2,2]),
$$

la horizontal $y=1$ corta la gráfica en

$$
(-1,1)
\qquad\text{y}\qquad
(1,1).
$$

Eso permite leer inmediatamente la no inyectividad:

$$
f(-1)=f(1)=1,
\qquad -1\ne1.
$$

#### Sobreyectividad

La sobreyectividad hace una pregunta diferente. Dado el codominio declarado $B$, exige que **cada** $b\in B$ sea alcanzado.

Geométricamente,

$$
\boxed{
f\colon A\to B\text{ es sobreyectiva}
\iff
\text{cada horizontal }y=b\text{ con }b\in B\text{ corta }\Gamma_f\text{ al menos una vez}.}
$$

Aquí no basta mirar la curva. Necesitamos saber cuál es el conjunto $B$ respecto del cual estamos formulando la pregunta.

Finalmente, una función es biyectiva exactamente cuando, para cada $b\in B$, la horizontal $y=b$ corta la gráfica **exactamente una vez**.

Podemos reunir las cuatro lecturas:

$$
\boxed{
\begin{array}{rcl}
\text{ser función sobre }A
&\longleftrightarrow&
\text{una intersección vertical por cada }x\in A,\\[4pt]
\text{inyectiva}
&\longleftrightarrow&
\text{a lo sumo una intersección horizontal},\\[4pt]
\text{sobreyectiva sobre }B
&\longleftrightarrow&
\text{al menos una intersección horizontal por cada }y\in B,\\[4pt]
\text{biyectiva}
&\longleftrightarrow&
\text{exactamente una intersección horizontal por cada }y\in B.
\end{array}}
$$

Las palabras «por cada $x\in A$» y «por cada $y\in B$» son parte esencial del enunciado, no anotaciones secundarias.

### La misma curva puede corresponder a funciones con distinta sobreyectividad

Llegamos ahora a una limitación fundamental de la gráfica considerada solo como conjunto de puntos del plano.

::: {#exm-t1-0027}
**Misma gráfica, distinto codominio.** Consideremos

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2,
$$

y

$$
h\colon\mathbb R\to[0,\infty),
\qquad
h(x)=x^2.
$$

Como ambas funciones tienen el mismo dominio y asignan a cada $x$ el mismo valor, sus conjuntos de pares ordenados son idénticos:

$$
\Gamma_f
=
\{(x,x^2):x\in\mathbb R\}
=
\Gamma_h.
$$

Como subconjunto del plano, vemos exactamente la misma parábola.

Sin embargo, las funciones no son iguales bajo la convención adoptada en este libro, porque sus codominios son distintos.

Además,

$$
f\text{ no es sobreyectiva sobre }\mathbb R,
$$

pues ningún número negativo aparece como segunda coordenada, mientras que

$$
h\text{ sí es sobreyectiva sobre }[0,\infty),
$$

porque todo $y\ge0$ posee una raíz cuadrada real y, por tanto, aparece en la gráfica.

La curva dibujada no cambió. Cambió la pregunta matemática porque cambió el codominio.
:::

Este ejemplo muestra por qué no debemos identificar sin matices una función con «su curva».

El conjunto de puntos permite recuperar la regla punto a punto y el dominio mediante las primeras coordenadas. También permite recuperar la imagen mediante las segundas coordenadas. Pero si el codominio contiene elementos que la función no alcanza, esos elementos **no aparecen como puntos adicionales en la gráfica**.

Por eso, a partir de la parábola sola no podemos decidir si estamos mirando

$$
\mathbb R\to\mathbb R
$$

o

$$
\mathbb R\to[0,\infty).
$$

Y precisamente por eso la sobreyectividad nunca debe diagnosticarse solo por la forma de la curva sin conocer el codominio declarado.

::: {.callout-warning title="Una precisión sobre el ambiente"}
Si escribimos explícitamente

$$
\Gamma_f\subseteq A\times B,
$$

y declaramos $A$ y $B$, entonces el **ambiente** aporta información adicional. Pero el mero conjunto de puntos

$$
\{(x,f(x)):x\in A\}
$$

no registra qué elementos extra hemos decidido incluir en un codominio mayor que la imagen.

La distinción es entre **la gráfica como conjunto de pares** y **la gráfica junto con todos los datos de la función que la acompañan**.
:::

### Gráfica, fórmula, tabla y algoritmo

Ya vimos en §2.1 que una función no necesita venir dada por una fórmula cerrada. La gráfica es otra forma de representar la misma clase de objetos, no una nueva definición limitada a curvas suaves o expresiones familiares.

Una función puede presentarse mediante:

- una fórmula;
- una tabla de valores;
- una descripción verbal;
- un algoritmo;
- una gráfica;
- o una combinación de esas representaciones.

Cada representación hace visibles unas propiedades y oculta otras.

Una fórmula puede facilitar cálculos exactos, pero puede ocultar el comportamiento global. Una tabla muestra valores concretos, pero normalmente solo una parte del dominio. Un algoritmo puede definir perfectamente una función aunque no produzca una expresión cerrada sencilla. Una gráfica vuelve visibles relaciones entre entradas y salidas, pero un dibujo aproximado no sustituye una demostración y, como acabamos de ver, tampoco revela por sí solo el codominio completo.

Por eso conviene adoptar la siguiente regla de lectura:

$$
\boxed{
\text{representación}
\neq
\text{objeto representado}.}
$$

La función es el objeto matemático completo; fórmula, tabla, algoritmo y gráfica son maneras de acceder a él.

### Qué podemos y qué no podemos concluir de una gráfica

Si la gráfica es exacta y conocemos el dominio y el codominio declarados, podemos usarla para formular y, en muchos ejemplos, decidir preguntas estructurales:

- qué entradas pertenecen al dominio;
- qué valores pertenecen a la imagen;
- si alguna entrada tendría más de una salida;
- si dos entradas comparten una salida;
- si cada elemento del codominio es alcanzado.

Pero debemos evitar varios saltos ilegítimos.

Un dibujo de resolución finita no demuestra por sí solo que dos puntos coincidan exactamente, que no exista una intersección demasiado pequeña para verse o que una propiedad se mantenga en todos los puntos. Cuando la afirmación exige exactitud, la gráfica orienta la conjetura y la estructura de la prueba; no reemplaza el argumento.

Tampoco debemos atribuir al dibujo información que pertenece a la declaración de la función. En particular,

$$
\boxed{\text{la sobreyectividad depende de la gráfica y del codominio}.}
$$

Con esto se completa la distinción que abrió el capítulo:

$$
\boxed{
\text{fórmula}
\neq
\text{función completa}
\neq
\text{gráfica como representación}.}
$$

En §2.8 utilizaremos ya esta lectura estructural para trabajar con **funciones definidas por tramos** y con transformaciones elementales de gráficas. La regla seguirá siendo la misma: primero entender qué operación se ha realizado sobre la función; después interpretar geométricamente qué le ocurre a su representación.

## Funciones por tramos y transformaciones de gráficas {#sec-t1-c03-08}

En §2.7 aprendimos a leer una gráfica como un conjunto de pares ordenados. Esa perspectiva permite ahora hacer algo más activo: **construir funciones a partir de varias reglas** y **predecir cómo cambia su gráfica cuando modificamos algebraicamente la función**.

En ambos casos mantendremos la misma disciplina que ha guiado todo el capítulo:

$$
\boxed{\text{primero identificamos la función; después interpretamos su gráfica}.}
$$

No comenzaremos memorizando frases como «sumar afuera desplaza hacia arriba» o «restar adentro desplaza hacia la derecha». Esas reglas son correctas cuando se formulan con sus hipótesis, pero resultan mucho más seguras si podemos reconstruirlas a partir de la igualdad que define cada punto de la gráfica.

### Una función puede usar reglas diferentes en partes diferentes del dominio

No existe ninguna exigencia matemática de que una función deba estar descrita por una única fórmula en todo su dominio.

Supongamos que queremos definir una función

$$
f\colon A\to\mathbb R
$$

mediante subconjuntos $A_1,\dots,A_n\subseteq A$ y reglas $r_1,\dots,r_n$. Esquemáticamente escribiríamos

$$
f(x)=
\begin{cases}
r_1(x),&x\in A_1,\\
r_2(x),&x\in A_2,\\
\vdots&\vdots\\
r_n(x),&x\in A_n.
\end{cases}
$$

Para que esta escritura determine realmente una función sobre **todo** $A$, debemos volver a las dos exigencias de §2.1: existencia y unicidad.

#### Existencia: ningún punto del dominio puede quedar sin regla

Necesitamos

$$
A=A_1\cup\cdots\cup A_n.
$$

Si algún $x\in A$ no pertenece a ninguno de los conjuntos $A_i$, la receta no dice qué valor debe tener $f(x)$. En ese punto fallaría la existencia de una salida.

#### Unicidad: un punto cubierto por varias reglas no puede recibir valores incompatibles

No es necesario que los conjuntos $A_i$ sean disjuntos. Pueden solaparse, pero entonces las reglas deben ser compatibles en cada solapamiento.

Si

$$
x\in A_i\cap A_j,
$$

debemos tener

$$
r_i(x)=r_j(x).
$$

De lo contrario, la misma entrada recibiría dos valores distintos y la receta no definiría una función.

Así, la definición por tramos no introduce una noción nueva de función. Solo reutiliza la definición ya conocida:

$$
\boxed{
\begin{array}{c}
\text{los tramos deben cubrir el dominio}\\[2pt]
\text{y deben concordar allí donde se superponen.}
\end{array}}
$$

### El valor absoluto como primer modelo

La función valor absoluto puede escribirse como

$$
|x|=
\begin{cases}
-x,&x<0,\\
x,&x\ge0.
\end{cases}
$$

Los dos tramos cubren todo $\mathbb R$ y no se superponen, de modo que no existe ambigüedad.

También podríamos escribir

$$
|x|=
\begin{cases}
-x,&x\le0,\\
x,&x\ge0.
\end{cases}
$$

Ahora los tramos se superponen en $x=0$, pero las dos fórmulas producen allí el mismo valor:

$$
-0=0.
$$

Por tanto, la segunda receta también define exactamente la misma función.

En cambio,

$$
h(x)=
\begin{cases}
-x+1,&x\le0,\\
x,&x\ge0
\end{cases}
$$

**no** define una función sobre $\mathbb R$, porque en el punto de solapamiento obtenemos dos instrucciones incompatibles:

$$
-0+1=1,
\qquad
0=0.
$$

La entrada $0$ tendría dos salidas.

::: {.callout-note title="Lectura estructural"}
Cuando veas una definición por tramos, no empieces dibujando. Comprueba primero:

1. cuál es el dominio declarado;
2. si los tramos lo cubren por completo;
3. si hay puntos que pertenecen a más de un tramo;
4. si las fórmulas coinciden en esos puntos.

Solo después la receta está auditada como función.
:::

### Fórmulas familiares y dominios naturales

Las funciones por tramos amplían el repertorio, pero también conviene ordenar las familias de expresiones que ya conocemos.

Una función **polinómica**, por ejemplo

$$
p(x)=x^3-2x+1,
$$

puede evaluarse para todo $x\in\mathbb R$. Si no se declara otra cosa, su dominio natural es $\mathbb R$.

Una expresión **racional**

$$
r(x)=\frac{p(x)}{q(x)}
$$

solo puede evaluarse donde

$$
q(x)\ne0.
$$

Por ejemplo,

$$
r(x)=\frac{1}{x^2-1}
$$

tiene como dominio natural

$$
\mathbb R\setminus\{-1,1\}.
$$

Una expresión **algebraica** que contiene una raíz cuadrada real exige que el radicando sea no negativo. Por ejemplo,

$$
s(x)=\sqrt{4-x^2}
$$

requiere

$$
4-x^2\ge0,
$$

es decir,

$$
-2\le x\le2.
$$

Por tanto, su dominio natural es

$$
[-2,2].
$$

Entre las funciones trigonométricas conocidas, $\sin x$ y $\cos x$ están definidas para todo real, mientras que una expresión como

$$
\tan x=\frac{\sin x}{\cos x}
$$

solo está definida donde $\cos x\ne0$.

Estas observaciones conducen a una convención útil, pero debemos formularla con cuidado:

> cuando se proporciona **solo una expresión** y se pide su dominio natural, buscamos el mayor subconjunto de $\mathbb R$ en el que todas las operaciones indicadas están definidas.

Esto no reemplaza el dominio como parte de los datos de una función. Podemos restringir deliberadamente una expresión a un dominio menor. Por ejemplo,

$$
p\colon[0,1]\to\mathbb R,
\qquad
p(x)=x^3-2x+1,
$$

es una función perfectamente legítima aunque la fórmula polinómica tenga sentido fuera de $[0,1]$.

La distinción permanece:

$$
\boxed{
\text{dominio natural de una expresión}
\neq
\text{dominio declarado de toda función que use esa expresión}.}
$$

### Transformar una gráfica significa transformar sus puntos

Fijemos ahora una función real

$$
f\colon D\to\mathbb R
$$

y un punto cualquiera de su gráfica:

$$
(u,f(u))\in\Gamma_f.
$$

Para entender una transformación, seguiremos ese punto. Preguntaremos qué punto de la nueva gráfica contiene **el mismo valor**, una versión modificada de ese valor o una entrada modificada.

Este método evita casi todas las reglas mnemotécnicas problemáticas.

### Desplazamiento vertical: $f(x)+c$

Definamos

$$
g(x)=f(x)+c.
$$

El dominio de $g$ es el mismo $D$, porque no hemos cambiado la entrada que introducimos en $f$.

Si

$$
y=f(u),
$$

entonces

$$
g(u)=f(u)+c=y+c.
$$

Por tanto, el punto

$$
(u,y)
$$

de la gráfica original se convierte en

$$
(u,y+c).
$$

La primera coordenada permanece fija y la segunda aumenta en $c$. Si $c>0$, todos los puntos se desplazan $c$ unidades hacia arriba; si $c<0$, se desplazan $|c|$ unidades hacia abajo.

En símbolos,

$$
\boxed{(u,y)\longmapsto(u,y+c).}
$$

### Desplazamiento horizontal: $f(x-c)$

Definamos ahora

$$
h(x)=f(x-c).
$$

Aquí sí hemos cambiado la entrada de $f$. Antes de hablar de la gráfica debemos auditar el dominio:

$$
x\in\operatorname{Dom}(h)
\iff
x-c\in D.
$$

Tomemos nuevamente un punto original

$$
(u,f(u)).
$$

¿En qué entrada de $h$ reaparece el valor $f(u)$? Debemos resolver

$$
x-c=u.
$$

Por tanto,

$$
x=u+c.
$$

y

$$
h(u+c)=f((u+c)-c)=f(u).
$$

Así,

$$
\boxed{(u,y)\longmapsto(u+c,y).}
$$

Si $c>0$, la gráfica se desplaza $c$ unidades **hacia la derecha**.

El signo puede parecer contrario a la intuición superficial porque dentro de la fórmula aparece $x-c$. Pero el desplazamiento no se adivina mirando el signo: se obtiene resolviendo

$$
x-c=u.
$$

::: {.callout-warning title="Error frecuente: el signo del desplazamiento horizontal"}
No confundas

$$
f(x)+c
$$

con

$$
f(x-c).
$$

La primera operación modifica la **salida**:

$$
(u,y)\mapsto(u,y+c).
$$

La segunda modifica la **entrada necesaria para obtener el mismo valor**:

$$
(u,y)\mapsto(u+c,y).
$$

En particular, para $c>0$,

$$
f(x-c)
$$

se desplaza hacia la **derecha**, no hacia la izquierda.

Si dudas, no memorices: fija un punto $u$ de la función original y resuelve $x-c=u$.
:::

Un ejemplo especialmente transparente es

$$
f(x)=\sqrt{x},
\qquad x\ge0.
$$

Entonces

$$
h(x)=\sqrt{x-3}
$$

solo está definida cuando

$$
x-3\ge0,
$$

es decir, cuando $x\ge3$. El dominio $[0,\infty)$ se ha desplazado a $[3,\infty)$, exactamente como predice la transformación horizontal.

### Reflexión respecto del eje horizontal: $-f(x)$

Sea

$$
g(x)=-f(x).
$$

Para cada $u\in D$,

$$
g(u)=-f(u).
$$

Por tanto,

$$
\boxed{(u,y)\longmapsto(u,-y).}
$$

La primera coordenada permanece fija y cambia el signo de la segunda. Geométricamente, la gráfica se refleja respecto del eje horizontal.

### Reflexión respecto del eje vertical: $f(-x)$

Sea ahora

$$
h(x)=f(-x).
$$

Su dominio es

$$
\{x\in\mathbb R:-x\in D\}.
$$

Si $u\in D$, buscamos la entrada $x$ que satisface

$$
-x=u.
$$

Entonces

$$
x=-u
$$

y

$$
h(-u)=f(u).
$$

Así,

$$
\boxed{(u,y)\longmapsto(-u,y).}
$$

Cambia el signo de la primera coordenada y se conserva la segunda: obtenemos una reflexión respecto del eje vertical.

Las dos reflexiones muestran otra vez la diferencia entre modificar una salida y modificar una entrada:

$$
\boxed{
\begin{array}{rcl}
-f(x)&:&(u,y)\mapsto(u,-y),\\[4pt]
f(-x)&:&(u,y)\mapsto(-u,y).
\end{array}}
$$

### Escalas verticales y horizontales: $a f(bx)$

Consideremos

$$
g(x)=a f(bx).
$$

Supongamos primero que

$$
a\ne0,
\qquad
b\ne0.
$$

Si $(u,y)$ pertenece a la gráfica de $f$, entonces queremos elegir $x$ de manera que

$$
bx=u.
$$

Por tanto,

$$
x=\frac{u}{b}.
$$

En esa entrada,

$$
g\!\left(\frac{u}{b}\right)
=
a f(u)
=
ay.
$$

Así, la transformación completa de los puntos es

$$
\boxed{
(u,y)
\longmapsto
\left(\frac{u}{b},ay\right).}
$$

El factor $a$ actúa directamente sobre las alturas:

- si $|a|>1$, las distancias verticales al eje horizontal se multiplican por $|a|$;
- si $0<|a|<1$, se reducen por ese factor;
- si $a<0$, además aparece la reflexión respecto del eje horizontal.

El factor $b$ actúa de modo recíproco sobre las coordenadas horizontales:

- si $|b|>1$, las coordenadas horizontales se dividen por un número mayor que $1$ y la gráfica se comprime horizontalmente;
- si $0<|b|<1$, se dilata horizontalmente;
- si $b<0$, además aparece la reflexión respecto del eje vertical.

La reciprocidad $u\mapsto u/b$ no es una convención gráfica: procede directamente de resolver $bx=u$.

También el dominio debe transformarse. Si $D$ es el dominio de $f$, entonces

$$
\operatorname{Dom}(g)
=
\{x\in\mathbb R:bx\in D\}.
$$

Los casos $a=0$ o $b=0$ son degenerados y deben analizarse por la definición, no por prolongación automática de la regla geométrica. Si $a=0$, todos los valores de una función ya definida se convierten en $0$. Si $b=0$, la expresión exige evaluar $f(0)$; solo tiene sentido si $0\in D$, y entonces la dependencia respecto de $x$ desaparece en la parte interior.

### La composición unifica las transformaciones

La notación de composición de §2.4 permite ver que no estamos acumulando cinco trucos aislados.

Definamos, para $c,a\in\mathbb R$,

$$
\tau_c(x)=x+c,
\qquad
\sigma_a(x)=ax.
$$

Siempre que los dominios permitan las composiciones correspondientes, tenemos

$$
f(x)+c
=
(\tau_c\circ f)(x),
$$

$$
f(x-c)
=
(f\circ\tau_{-c})(x),
$$

$$
-f(x)
=
(\sigma_{-1}\circ f)(x),
$$

$$
f(-x)
=
(f\circ\sigma_{-1})(x),
$$

y

$$
a f(bx)
=
(\sigma_a\circ f\circ\sigma_b)(x).
$$

Esto explica la diferencia fundamental entre transformaciones «de afuera» y «de adentro»:

- componer **después** de $f$ modifica las salidas;
- componer **antes** de $f$ modifica las entradas que llegan a $f$.

La geometría refleja ese orden algebraico.

### Un ejemplo completo: construir por tramos y transformar

::: {#exm-t1-0028}
**Una función por tramos bajo varias transformaciones.** Definamos

$$
p\colon[-1,2]\to\mathbb R
$$

mediante

$$
p(x)=
\begin{cases}
x+1,&-1\le x\le0,\\[2pt]
1-\dfrac{x}{2},&0\le x\le2.
\end{cases}
$$

Los dos tramos cubren $[-1,2]$. Se superponen únicamente en $x=0$, y allí coinciden:

$$
0+1
=
1
=
1-\frac02.
$$

Por tanto, la receta define una función.

La primera rama recorre valores desde $0$ hasta $1$, y la segunda vuelve desde $1$ hasta $0$. Así,

$$
p([-1,2])=[0,1].
$$

Ahora sigamos varias transformaciones.

**1. Desplazamiento vertical.** Sea

$$
q(x)=p(x)+2.
$$

El dominio permanece $[-1,2]$ y

$$
q(x)=
\begin{cases}
x+3,&-1\le x\le0,\\[2pt]
3-\dfrac{x}{2},&0\le x\le2.
\end{cases}
$$

Cada punto $(u,y)$ pasa a $(u,y+2)$, y la imagen pasa de $[0,1]$ a

$$
[2,3].
$$

**2. Desplazamiento horizontal.** Sea

$$
r(x)=p(x-3).
$$

La condición $x-3\in[-1,2]$ equivale a

$$
2\le x\le5.
$$

Por tanto, el dominio nuevo es $[2,5]$. Sustituyendo cuidadosamente en cada tramo,

$$
r(x)=
\begin{cases}
x-2,&2\le x\le3,\\[2pt]
\dfrac{5-x}{2},&3\le x\le5.
\end{cases}
$$

La gráfica completa se ha desplazado tres unidades hacia la derecha:

$$
(u,y)\longmapsto(u+3,y).
$$

**3. Dos reflexiones.** Sea

$$
s(x)=-p(-x).
$$

La sustitución interior $-x$ refleja primero las entradas; el signo exterior refleja después las salidas. El dominio es $[-2,1]$ y, desarrollando los tramos,

$$
s(x)=
\begin{cases}
-1-\dfrac{x}{2},&-2\le x\le0,\\[4pt]
x-1,&0\le x\le1.
\end{cases}
$$

Cada punto de la gráfica original se transforma según

$$
(u,y)\longmapsto(-u,-y).
$$

**4. Cambio simultáneo de escalas.** Finalmente, sea

$$
t(x)=2p(2x).
$$

Como $2x\in[-1,2]$, el dominio es

$$
\left[-\frac12,1\right].
$$

Además,

$$
t(x)=
\begin{cases}
4x+2,&-\dfrac12\le x\le0,\\[4pt]
2-2x,&0\le x\le1.
\end{cases}
$$

Los puntos obedecen a

$$
(u,y)\longmapsto\left(\frac{u}{2},2y\right).
$$

La gráfica se comprime horizontalmente por un factor $2$ y las alturas se duplican. La imagen es ahora

$$
[0,2].
$$

En los cuatro casos no hemos necesitado adivinar la nueva gráfica: cada cambio se dedujo de la nueva regla y de su dominio.
:::

### Un protocolo seguro para transformar funciones

Cuando aparezca una expresión construida a partir de una función conocida, conviene seguir siempre este orden:

1. **Escribe la nueva función.** No trabajes todavía con el dibujo.
2. **Audita su dominio.** Las modificaciones interiores pueden cambiarlo.
3. **Fija un punto original $(u,f(u))$.**
4. **Resuelve qué nueva entrada produce el valor relacionado con $f(u)$.**
5. **Calcula la nueva salida.**
6. **Obtén la transformación de coordenadas.**
7. **Solo entonces interpreta desplazamiento, reflexión o cambio de escala.**

Este procedimiento es algo más lento que memorizar una tabla la primera vez, pero es mucho más robusto. Además, funciona también cuando varias transformaciones aparecen combinadas.

Podemos resumir las transformaciones básicas, para los casos en que las expresiones estén definidas, del siguiente modo:

$$
\boxed{
\begin{array}{rcl}
f(x)+c
&:&(u,y)\mapsto(u,y+c),\\[4pt]
f(x-c)
&:&(u,y)\mapsto(u+c,y),\\[4pt]
-f(x)
&:&(u,y)\mapsto(u,-y),\\[4pt]
f(-x)
&:&(u,y)\mapsto(-u,y),\\[4pt]
a f(bx)
&:&(u,y)\mapsto\left(\dfrac{u}{b},ay\right),\quad ab\ne0.
\end{array}}
$$

La tabla es ahora una **consecuencia** de los cálculos anteriores, no un sustituto de ellos.

En §2.9 añadiremos una propiedad cualitativa nueva que depende del orden del dominio: estudiaremos cómo comparar las salidas correspondientes a entradas ordenadas y por qué ciertas funciones pueden invertirse después de restringir adecuadamente su dominio. Hasta entonces, todo lo que hemos hecho en esta sección depende solo de la definición de función, de su dominio, de la composición y de la representación mediante pares ordenados.

## Monotonía e inversas sobre intervalos {#sec-t1-c03-09}

Hasta ahora hemos estudiado funciones atendiendo a cómo asignan valores, cómo se componen, cuándo son inyectivas o sobreyectivas, cómo pueden invertirse y cómo se representan mediante gráficas. Falta incorporar una estructura que todavía no hemos utilizado de manera sistemática: **el orden de las entradas y de las salidas**.

Si el dominio es un subconjunto ordenado de $\mathbb R$, podemos comparar dos entradas $x_1<x_2$ y preguntar qué relación existe entre $f(x_1)$ y $f(x_2)$. Una función puede conservar el orden, invertirlo, conservarlo solo débilmente o no obedecer ningún patrón global de este tipo.

Esta pregunta conduce a la noción de **monotonía**.

### Comparar entradas para comparar salidas

Consideremos primero dos ejemplos sencillos.

Para

$$
f(x)=2x+1,
$$

si $x_1<x_2$, entonces

$$
2x_1+1<2x_2+1,
$$

de modo que el orden de las entradas se conserva estrictamente.

En cambio, para

$$
g(x)=-3x+4,
$$

si $x_1<x_2$, al multiplicar por $-3$ se invierte la desigualdad:

$$
-3x_1>-3x_2,
$$

y por tanto

$$
g(x_1)>g(x_2).
$$

Aquí el orden se invierte estrictamente.

Hay también situaciones en las que el orden solo se conserva de manera débil. Una función puede tener dos entradas distintas con la misma salida y, aun así, no disminuir nunca.

Por eso necesitamos distinguir cuidadosamente las versiones débiles de las estrictas.

::: {#def-t1-0026}
**Monotonía.** Sea $D\subseteq\mathbb R$ y sea

$$
f\colon D\to\mathbb R.
$$

Diremos que $f$ es:

1. **no decreciente** en $D$ si, para cualesquiera $x_1,x_2\in D$,
   $$
   x_1<x_2
   \Longrightarrow
   f(x_1)\le f(x_2);
   $$

2. **estrictamente creciente** en $D$ si
   $$
   x_1<x_2
   \Longrightarrow
   f(x_1)<f(x_2);
   $$

3. **no creciente** en $D$ si
   $$
   x_1<x_2
   \Longrightarrow
   f(x_1)\ge f(x_2);
   $$

4. **estrictamente decreciente** en $D$ si
   $$
   x_1<x_2
   \Longrightarrow
   f(x_1)>f(x_2).
   $$

Una función se llama **monótona** cuando es no decreciente o no creciente, y **estrictamente monótona** cuando es estrictamente creciente o estrictamente decreciente.
:::

La terminología varía ligeramente entre libros: algunos autores usan «creciente» para la versión débil y otros para la estricta. Para evitar ambigüedades, en este libro escribiremos siempre **no decreciente**, **no creciente**, **estrictamente creciente** o **estrictamente decreciente** cuando la distinción sea relevante.

### El dominio debe estar ordenado

La definición anterior no depende de que $D$ sea un intervalo. Solo necesita que tenga sentido comparar dos elementos mediante $<$.

Por ejemplo, podríamos estudiar monotonía en

$$
D=\{-3,-1,2,7\}.
$$

Sin embargo, en análisis trabajaremos con especial frecuencia sobre **intervalos**, porque allí no hemos eliminado artificialmente puntos intermedios del dominio. Por esa razón el título de esta sección habla de monotonía sobre intervalos.

Conviene separar desde ahora dos afirmaciones:

$$
\boxed{
\begin{array}{c}
\text{la definición de monotonía necesita orden;}\\[4pt]
\text{muchos teoremas posteriores necesitarán además que el dominio sea un intervalo.}
\end{array}}
$$

El primer teorema de esta sección pertenece al primer grupo: ni siquiera necesita que el dominio sea un intervalo.

### Por qué la monotonía estricta impide repeticiones

En §2.3 definimos la inyectividad mediante

$$
f(x_1)=f(x_2)
\Longrightarrow
x_1=x_2.
$$

Ahora disponemos de una condición diferente, expresada mediante desigualdades. La pregunta natural es:

> si la función separa estrictamente las salidas cada vez que ordenamos dos entradas distintas, ¿pueden dos entradas distintas producir la misma salida?

La respuesta es negativa.

::: {#thm-t1-0008}
**Toda función estrictamente monótona es inyectiva.** Sea $D\subseteq\mathbb R$ y sea

$$
f\colon D\to\mathbb R.
$$

Si $f$ es estrictamente creciente o estrictamente decreciente en $D$, entonces $f$ es inyectiva.
:::

**Idea de la prueba.** Queremos demostrar que entradas distintas no pueden compartir una salida. Como $\mathbb R$ está ordenado, si $x_1\ne x_2$, entonces necesariamente ocurre una de las dos posibilidades

$$
x_1<x_2
\qquad\text{o}\qquad
x_2<x_1.
$$

La monotonía estricta convierte cualquiera de esas desigualdades entre entradas en una desigualdad estricta entre salidas. Por tanto, las salidas no pueden ser iguales.

**Demostración.** Supongamos primero que $f$ es estrictamente creciente. Sean $x_1,x_2\in D$ con

$$
x_1\ne x_2.
$$

Por el orden total de $\mathbb R$, o bien $x_1<x_2$ o bien $x_2<x_1$.

Si $x_1<x_2$, la monotonía estricta da

$$
f(x_1)<f(x_2),
$$

y por tanto

$$
f(x_1)\ne f(x_2).
$$

Si $x_2<x_1$, obtenemos análogamente

$$
f(x_2)<f(x_1),
$$

de nuevo con

$$
f(x_1)\ne f(x_2).
$$

Así, entradas distintas producen salidas distintas y $f$ es inyectiva.

Si $f$ es estrictamente decreciente, el argumento es idéntico salvo por el sentido de las desigualdades: de $x_1<x_2$ se sigue

$$
f(x_1)>f(x_2),
$$

y de $x_2<x_1$ se sigue

$$
f(x_2)>f(x_1).
$$

En ambos casos las salidas son diferentes. Por tanto, $f$ también es inyectiva. $\square$

::: {.callout-note title="Después de la prueba"}
La demostración no utilizó completitud, intervalos, continuidad, límites ni derivadas. Solo necesitó:

- que el dominio esté contenido en un conjunto totalmente ordenado;
- la definición de monotonía estricta.

La razón estructural es muy simple:

$$
\boxed{
\text{entradas distintas}
\Longrightarrow
\text{entradas comparables}
\Longrightarrow
\text{salidas estrictamente distintas}.}
$$
:::

### Por qué «estrictamente» no puede borrarse

Una función no decreciente puede conservar el orden débilmente y, sin embargo, repetir valores.

El ejemplo más simple es la función constante

$$
c\colon\mathbb R\to\mathbb R,
\qquad
c(x)=5.
$$

Si $x_1<x_2$, entonces

$$
c(x_1)=5\le5=c(x_2),
$$

de modo que $c$ es no decreciente. También es no creciente. Pero no es inyectiva, porque

$$
c(0)=c(1)=5.
$$

Por tanto,

$$
\boxed{
\text{no decreciente}
\centernot\Longrightarrow
\text{inyectiva}.}
$$

Lo mismo ocurre con «no creciente». La desigualdad estricta del teorema no es una comodidad estilística: es la condición que impide los tramos horizontales y, algebraicamente, impide que dos entradas ordenadas tengan la misma salida.

### Una vía natural hacia la inversa

Supongamos ahora que $I\subseteq\mathbb R$ es un intervalo y

$$
f\colon I\to\mathbb R
$$

es estrictamente monótona.

El teorema anterior nos da inmediatamente inyectividad. Pero para aplicar el criterio de §2.5 necesitamos también sobreyectividad.

Aquí aparece una maniobra que ya usamos con $x^2$: en lugar de mantener un codominio posiblemente demasiado grande, consideramos la misma regla con codominio igual a su imagen:

$$
f\colon I\to f(I).
$$

Esta función es sobreyectiva **por definición de $f(I)$**. Y es inyectiva por el teorema de monotonía estricta. Por tanto, es biyectiva y posee función inversa.

La monotonía nos permite decir todavía más: la inversa conserva el mismo tipo de orden.

::: {#cor-t1-0006}
**Inversa sobre la imagen y monotonía de la inversa.** Sea $I\subseteq\mathbb R$ un intervalo y sea

$$
f\colon I\to\mathbb R
$$

estrictamente monótona. Entonces la función

$$
f\colon I\to f(I)
$$

es biyectiva y, por tanto, admite una única inversa

$$
f^{-1}\colon f(I)\to I.
$$

Además:

1. si $f$ es estrictamente creciente, entonces $f^{-1}$ es estrictamente creciente;
2. si $f$ es estrictamente decreciente, entonces $f^{-1}$ es estrictamente decreciente.
:::

**Por qué existe la inversa.** La sobreyectividad de

$$
f\colon I\to f(I)
$$

es automática, porque cada elemento de $f(I)$ es, precisamente, un valor $f(x)$ con $x\in I$. La inyectividad proviene de @thm-t1-0008. Por @thm-t1-0007, la función es biyectiva y admite una única inversa.

Queda demostrar el comportamiento del orden.

**Caso 1: $f$ estrictamente creciente.** Sean

$$
y_1,y_2\in f(I)
\qquad\text{con}\qquad
y_1<y_2.
$$

Definamos

$$
x_1=f^{-1}(y_1),
\qquad
x_2=f^{-1}(y_2).
$$

Entonces

$$
f(x_1)=y_1,
\qquad
f(x_2)=y_2.
$$

Queremos demostrar

$$
x_1<x_2.
$$

Como $y_1<y_2$, tenemos $y_1\ne y_2$ y por tanto $x_1\ne x_2$. Si ocurriera $x_2<x_1$, la monotonía estrictamente creciente de $f$ produciría

$$
f(x_2)<f(x_1),
$$

es decir,

$$
y_2<y_1,
$$

contradicción.

La única posibilidad restante es

$$
x_1<x_2.
$$

Así,

$$
y_1<y_2
\Longrightarrow
f^{-1}(y_1)<f^{-1}(y_2),
$$

y $f^{-1}$ es estrictamente creciente.

**Caso 2: $f$ estrictamente decreciente.** Tomemos de nuevo $y_1<y_2$ y pongamos

$$
x_1=f^{-1}(y_1),
\qquad
x_2=f^{-1}(y_2).
$$

Si ocurriera $x_1<x_2$, como $f$ es estrictamente decreciente tendríamos

$$
f(x_1)>f(x_2),
$$

es decir,

$$
y_1>y_2,
$$

contradicción.

Como $x_1\ne x_2$, necesariamente

$$
x_1>x_2.
$$

Por tanto,

$$
y_1<y_2
\Longrightarrow
f^{-1}(y_1)>f^{-1}(y_2),
$$

y la inversa es estrictamente decreciente. $\square$

::: {.callout-note title="Dos inversiones distintas"}
En el caso decreciente aparecen dos ideas de «inversión» que no deben confundirse.

- $f$ **invierte el orden**:
  $$
  x_1<x_2\Longrightarrow f(x_1)>f(x_2).
  $$
- $f^{-1}$ **invierte la asignación** de entradas y salidas.

La inversa funcional de una función estrictamente decreciente sigue siendo estrictamente decreciente: al recorrer la relación en sentido contrario, el orden vuelve a invertirse.
:::

### Lo que todavía no podemos concluir sobre $f(I)$

El dominio $I$ es un intervalo, pero de lo demostrado hasta aquí **no se sigue** que la imagen $f(I)$ sea también un intervalo.

Consideremos

$$
f\colon\mathbb R\to\mathbb R,
$$

$$
f(x)=
\begin{cases}
x,&x<0,\\
x+1,&x\ge0.
\end{cases}
$$

Esta función es estrictamente creciente. En efecto:

- si $x_1<x_2<0$, entonces $f(x_1)=x_1<x_2=f(x_2)$;
- si $0\le x_1<x_2$, entonces $f(x_1)=x_1+1<x_2+1=f(x_2)$;
- si $x_1<0\le x_2$, entonces
  $$
  f(x_1)=x_1<0<1\le x_2+1=f(x_2).
  $$

Sin embargo,

$$
f(\mathbb R)=(-\infty,0)\cup[1,\infty),
$$

que no es un intervalo.

Esto marca con precisión la frontera actual del capítulo. La monotonía estricta basta para obtener **inyectividad** y, al ajustar el codominio a la imagen, una **inversa**. Para garantizar que ciertos valores intermedios no se omitan necesitaremos una propiedad adicional que todavía no hemos introducido.

### El modelo fundamental: cuadrado y raíz

Volvamos ahora a una función que nos acompaña desde el comienzo del capítulo.

::: {#exm-t1-0029}
**El cuadrado sobre $[0,\infty)$ y su inversa.** Consideremos

$$
q\colon[0,\infty)\to[0,\infty),
\qquad
q(x)=x^2.
$$

En §2.3 demostramos que $q$ es biyectiva y en §2.5 identificamos su inversa como

$$
q^{-1}(y)=\sqrt y.
$$

Ahora podemos comprender esa invertibilidad desde el orden.

Sean

$$
0\le x_1<x_2.
$$

Entonces

$$
x_2^2-x_1^2
=(x_2-x_1)(x_2+x_1).
$$

El primer factor es positivo:

$$
x_2-x_1>0.
$$

Además, como $x_2>x_1\ge0$, tenemos $x_2>0$, y por tanto

$$
x_2+x_1>0.
$$

Así,

$$
x_2^2-x_1^2>0,
$$

de donde

$$
x_1^2<x_2^2.
$$

Por consiguiente, $q$ es estrictamente creciente en $[0,\infty)$.

El corolario anterior implica entonces que su inversa

$$
\sqrt{\phantom{x}}\colon[0,\infty)\to[0,\infty)
$$

es también estrictamente creciente. En particular,

$$
0\le y_1<y_2
\Longrightarrow
\sqrt{y_1}<\sqrt{y_2}.
$$

Esta propiedad no necesita una nueva demostración mediante cuadrados: es una consecuencia estructural de que $x^2$ es estrictamente creciente en el dominio donde lo hemos hecho invertible.
:::

El ejemplo muestra por qué la restricción del dominio a $[0,\infty)$ era tan natural. En todo $\mathbb R$, la función $x\mapsto x^2$ no es estrictamente monótona: por ejemplo,

$$
-2<-1,
$$

pero

$$
(-2)^2=4>1=(-1)^2,
$$

mientras que

$$
0<1
\Longrightarrow
0^2<1^2.
$$

El comportamiento cambia al atravesar $0$. Al restringirnos a $[0,\infty)$ obtenemos una región del dominio en la que el orden se conserva estrictamente y, con ello, la inyectividad necesaria para invertir la función.

### La gráfica de la inversa y la diagonal $y=x$

En §2.7 definimos

$$
\Gamma_f
=
\{(x,f(x)):x\in I\}.
$$

Si $f\colon I\to f(I)$ es biyectiva, entonces

$$
y=f(x)
\Longleftrightarrow
x=f^{-1}(y).
$$

Por tanto,

$$
(x,y)\in\Gamma_f
\Longleftrightarrow
(y,x)\in\Gamma_{f^{-1}}.
$$

La gráfica de la inversa se obtiene, pues, **intercambiando las dos coordenadas** de cada punto:

$$
\boxed{(x,y)\longmapsto(y,x).}
$$

Geométricamente, ese intercambio es la reflexión respecto de la diagonal

$$
y=x.
$$

No necesitamos apelar al dibujo para justificarlo. La simetría gráfica es la traducción geométrica de las equivalencias

$$
y=f(x)
\Longleftrightarrow
x=f^{-1}(y).
$$

En el ejemplo anterior, los puntos

$$
(4,16),
\qquad
(9,81)
$$

de la gráfica de $q(x)=x^2$ sobre $[0,\infty)$ corresponden a los puntos

$$
(16,4),
\qquad
(81,9)
$$

de la gráfica de $q^{-1}(x)=\sqrt x$.

### Qué aporta realmente la monotonía

Podemos reunir la cadena lógica construida en esta sección:

$$
\boxed{
\text{monotonía estricta}
\Longrightarrow
\text{inyectividad}
\Longrightarrow
\text{biyección sobre la imagen}
\Longrightarrow
\text{existencia de inversa}.}
$$

Y además,

$$
\boxed{
\begin{array}{c}
\text{estrictamente creciente}
\Longrightarrow
\text{inversa estrictamente creciente},\\[4pt]
\text{estrictamente decreciente}
\Longrightarrow
\text{inversa estrictamente decreciente}.
\end{array}}
$$

La importancia de esta cadena es metodológica. Para construir una inversa no siempre conviene comenzar intentando despejar una fórmula. A menudo es más útil preguntar primero:

1. ¿en qué dominio la función tiene un comportamiento ordenado simple?;
2. ¿es estrictamente monótona allí?;
3. ¿qué imagen produce ese dominio?;
4. ¿podemos tomar esa imagen como codominio?

Si las respuestas encajan, la existencia de la inversa queda resuelta antes de calcular su fórmula.

En §2.10 reuniremos todas las estructuras del capítulo en un laboratorio integrado: dominio y codominio, imágenes y preimágenes, composición, inyectividad, inversas, gráficas y monotonía deberán aparecer ya no como temas aislados, sino como herramientas entre las que habrá que elegir según el problema.

## Laboratorio de estructura funcional {#sec-t1-c03-10}

Hasta aquí hemos construido las piezas del lenguaje funcional una por una. Sabemos distinguir una fórmula de una función completamente especificada; calcular imágenes y preimágenes; decidir inyectividad y sobreyectividad; componer funciones con control de tipos; construir inversas; leer gráficas; trabajar con definiciones por tramos y reconocer la fuerza de la monotonía estricta.

Ahora cambia la tarea.

En los problemas que siguen **no se anunciará de antemano qué herramienta debe utilizarse**. La primera parte de cada solución será diagnosticar qué información importa y qué estructura del capítulo permite avanzar.

Conviene adoptar este protocolo general:

$$
\boxed{
\text{identificar la función}
\to
\text{auditar tipos y conjuntos}
\to
\text{elegir la estructura pertinente}
\to
\text{resolver}
\to
\text{revisar qué hipótesis fueron esenciales}
}
$$

El objetivo no es repetir mecánicamente definiciones. Es empezar a ver dominio, codominio, imagen, composición, inyectividad, inversa, gráfica y monotonía como partes de un mismo sistema.

### Laboratorio 1 — Qué sabemos y qué todavía falta

Alguien escribe solamente

$$
p(x)=\sqrt{4-x^2}.
$$

**Problema.** Determinar qué información puede inferirse de esa expresión y qué información falta todavía para tener una función completamente especificada. Después, construir dos funciones distintas que utilicen exactamente la misma fórmula.

#### Diagnóstico

La expresión contiene información algebraica. Como estamos trabajando con valores reales, la raíz cuadrada exige

$$
4-x^2\ge0.
$$

Pero una **restricción impuesta por la fórmula** no es todavía lo mismo que un dominio declarado. Tampoco aparece un codominio.

Debemos separar, por tanto, tres preguntas:

1. ¿para qué reales puede evaluarse la expresión?;
2. ¿qué conjunto elegimos efectivamente como dominio?;
3. ¿en qué conjunto declaramos que viven las salidas?

#### Solución

La condición

$$
4-x^2\ge0
$$

equivale a

$$
x^2\le4,
$$

y por tanto a

$$
-2\le x\le2.
$$

Así, el **dominio real máximo de la expresión** es

$$
[-2,2].
$$

Además, para todo $x\in[-2,2]$,

$$
0\le\sqrt{4-x^2}\le2.
$$

Eso permite definir, por ejemplo,

$$
f\colon[-2,2]\to[0,2],
\qquad
f(x)=\sqrt{4-x^2},
$$

y también

$$
g\colon[0,2]\to\mathbb R,
\qquad
g(x)=\sqrt{4-x^2}.
$$

Ambas funciones utilizan la misma fórmula, pero son funciones distintas porque sus dominios y codominios no coinciden.

Todavía podríamos construir muchas otras. Si $D\subseteq[-2,2]$, la misma expresión define una función sobre $D$; y cualquier codominio que contenga las salidas efectivas puede formar parte de una declaración válida.

Lo que **no** podemos hacer a partir de la fórmula aislada es decidir, por ejemplo, si «$p$ es sobreyectiva». La sobreyectividad depende del codominio declarado. Tampoco podemos preguntar sin más si «$p$ tiene inversa», porque antes debemos conocer la función completa y su inyectividad/sobreyectividad.

#### Lectura de la solución

Este primer laboratorio recupera la pregunta central del capítulo:

$$
\boxed{\text{una expresión restringe posibilidades, pero no especifica por sí sola toda la función}.}
$$

El dominio natural de una expresión es una información que podemos **deducir**. El dominio y el codominio de una función son datos que debemos **declarar**.

### Laboratorio 2 — Una fórmula, cuatro clasificaciones

Consideremos ahora la regla

$$
x\longmapsto x^2-1.
$$

Definamos

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2-1,
$$

$$
g\colon[0,\infty)\to[-1,\infty),
\qquad
g(x)=x^2-1,
$$

$$
h\colon\mathbb R\to[-1,\infty),
\qquad
h(x)=x^2-1,
$$

y

$$
k\colon[0,\infty)\to\mathbb R,
\qquad
k(x)=x^2-1.
$$

**Problema.** Determinar la imagen y clasificar cada función como inyectiva, sobreyectiva, biyectiva o ninguna de ellas.

#### Diagnóstico

La fórmula es idéntica en las cuatro declaraciones. Por tanto, el cálculo de valores no distingue las funciones. Las diferencias deben provenir de dos lugares:

- qué entradas están permitidas;
- qué conjunto se ha declarado como codominio.

El cuadrado sobre todo $\mathbb R$ identifica $x$ y $-x$, mientras que sobre $[0,\infty)$ preserva estrictamente el orden. Además,

$$
x^2-1\ge-1.
$$

Estas dos observaciones controlan casi toda la clasificación.

#### Solución

Para $f$ y $h$, el dominio es todo $\mathbb R$. Como

$$
f(1)=f(-1)=0
$$

y

$$
h(1)=h(-1)=0,
$$

ninguna de las dos funciones es inyectiva.

La imagen de la regla sobre $\mathbb R$ es

$$
[-1,\infty).
$$

En efecto, $x^2-1\ge-1$ para todo real $x$. Recíprocamente, si $y\ge-1$, entonces $y+1\ge0$ y podemos tomar

$$
x=\sqrt{y+1},
$$

para obtener

$$
x^2-1=y.
$$

Por tanto,

$$
\operatorname{Im}(f)=\operatorname{Im}(h)=[-1,\infty).
$$

Como el codominio de $f$ es $\mathbb R$, los valores menores que $-1$ no son alcanzados. Así,

$$
\boxed{f\text{ no es inyectiva ni sobreyectiva}.}
$$

En cambio, el codominio de $h$ es exactamente $[-1,\infty)$, de modo que

$$
\boxed{h\text{ es sobreyectiva pero no inyectiva}.}
$$

Consideremos ahora $g$ y $k$. Si

$$
0\le x_1<x_2,
$$

entonces, como vimos en §2.9,

$$
x_1^2<x_2^2,
$$

y al restar $1$ obtenemos

$$
x_1^2-1<x_2^2-1.
$$

La regla es, por tanto, estrictamente creciente sobre $[0,\infty)$ y las dos funciones son inyectivas.

Su imagen sigue siendo

$$
[-1,\infty),
$$

porque para cada $y\ge-1$ el número

$$
\sqrt{y+1}\in[0,\infty)
$$

satisface

$$
(\sqrt{y+1})^2-1=y.
$$

Así,

$$
\boxed{g\text{ es biyectiva},}
$$

mientras que

$$
\boxed{k\text{ es inyectiva pero no sobreyectiva}.}
$$

Podemos resumir:

| Función | Imagen | Inyectiva | Sobreyectiva | Biyectiva |
|---|---|---:|---:|---:|
| $f\colon\mathbb R\to\mathbb R$ | $[-1,\infty)$ | no | no | no |
| $g\colon[0,\infty)\to[-1,\infty)$ | $[-1,\infty)$ | sí | sí | sí |
| $h\colon\mathbb R\to[-1,\infty)$ | $[-1,\infty)$ | no | sí | no |
| $k\colon[0,\infty)\to\mathbb R$ | $[-1,\infty)$ | sí | no | no |

#### Lectura de la solución

La tabla muestra dos sensibilidades diferentes:

$$
\boxed{\text{la inyectividad responde al dominio}}
$$

y

$$
\boxed{\text{la sobreyectividad responde al codominio y a la imagen}.}
$$

Cambiar el dominio puede eliminar entradas que producían la misma salida. Cambiar el codominio puede convertir una función en sobreyectiva sin alterar ninguno de sus valores punto a punto.

### Laboratorio 3 — Componer empieza por verificar que se puede

Sean

$$
f\colon\mathbb R\to[0,\infty),
\qquad
f(x)=x^2,
$$

$$
g\colon[0,\infty)\to\mathbb R,
\qquad
g(u)=u+1,
$$

y

$$
h\colon(0,\infty)\to\mathbb R,
\qquad
h(u)=\frac1u.
$$

**Problema.** Decidir cuáles de las composiciones

$$
g\circ f,
\qquad
f\circ g,
\qquad
h\circ f,
\qquad
f\circ h,
\qquad
h\circ g
$$

están definidas con las funciones tal como han sido declaradas. Calcular las que existan y explicar por qué el orden de composición importa.

#### Diagnóstico

Antes de sustituir fórmulas debemos auditar tipos. Para que $v\circ u$ esté definida sobre todo el dominio de $u$ necesitamos

$$
\operatorname{Im}(u)\subseteq\operatorname{Dom}(v).
$$

Esta condición es anterior a cualquier simplificación algebraica.

#### Solución

Como

$$
\operatorname{Im}(f)=[0,\infty)
$$

y ese conjunto es exactamente el dominio de $g$, existe

$$
g\circ f\colon\mathbb R\to\mathbb R,
$$

con

$$
(g\circ f)(x)=g(x^2)=x^2+1.
$$

También existe $f\circ g$. En efecto,

$$
\operatorname{Im}(g)=[1,\infty)\subseteq\mathbb R=\operatorname{Dom}(f).
$$

Por tanto,

$$
f\circ g\colon[0,\infty)\to[0,\infty)
$$

y

$$
(f\circ g)(u)=f(u+1)=(u+1)^2.
$$

Estas dos composiciones ya muestran que el orden importa. Bajo nuestra convención ni siquiera son la misma función, porque tienen dominios y codominios distintos. Incluso si comparamos un valor perteneciente a ambos dominios, por ejemplo $2$, obtenemos

$$
(g\circ f)(2)=5
$$

mientras que

$$
(f\circ g)(2)=9.
$$

Examinemos ahora $h\circ f$. Para que existiera sobre todo $\mathbb R$ necesitaríamos

$$
f(\mathbb R)\subseteq(0,\infty).
$$

Pero

$$
f(0)=0\notin(0,\infty).
$$

Así,

$$
\boxed{h\circ f\text{ no está definida como composición sobre todo }\mathbb R.}
$$

Es cierto que la expresión formal

$$
\frac1{x^2}
$$

puede evaluarse cuando $x\ne0$. Pero eso produciría una función sobre $\mathbb R\setminus\{0\}$, no la composición $h\circ f$ con el dominio original de $f$.

En cambio, $f\circ h$ sí existe porque

$$
\operatorname{Im}(h)=(0,\infty)\subseteq\mathbb R=\operatorname{Dom}(f).
$$

Entonces

$$
(f\circ h)(u)
=
\left(\frac1u\right)^2
=
\frac1{u^2},
\qquad u>0.
$$

Finalmente,

$$
\operatorname{Im}(g)=[1,\infty)\subseteq(0,\infty)=\operatorname{Dom}(h),
$$

por lo que también existe $h\circ g$ y

$$
(h\circ g)(u)=\frac1{u+1},
\qquad u\ge0.
$$

#### Lectura de la solución

El error que debemos evitar es

$$
\boxed{\text{ver dos fórmulas y componerlas antes de mirar sus tipos}.}
$$

Una expresión algebraica simplificada puede tener sentido en ciertos puntos aun cuando la composición de las funciones originalmente declaradas no exista sobre todo el dominio requerido.

### Laboratorio 4 — Cuando una prueba fallida descubre el teorema correcto

Sea

$$
f\colon A\to B
$$

y sean $E,F\subseteq A$.

Una igualdad tentadora es

$$
\boxed{f(E\setminus F)=f(E)\setminus f(F).}
$$

**Problema.** Investigar si la igualdad es siempre verdadera. No debemos comenzar buscando un contraejemplo al azar: intentemos primero demostrarla por doble inclusión y observemos dónde se detiene la prueba.

#### Diagnóstico

En §2.6 aprendimos que las imágenes directas pueden mezclar testigos distintos. Aquí aparece una dificultad parecida: que un punto $x$ no pertenezca a $F$ no impide, en principio, que otro punto $z\in F$ tenga la misma imagen.

La prueba debe revelar exactamente dónde importa esa posibilidad.

#### Primera inclusión

Tomemos

$$
y\in f(E)\setminus f(F).
$$

Como $y\in f(E)$, existe $x\in E$ tal que

$$
f(x)=y.
$$

Además,

$$
y\notin f(F).
$$

Si $x$ perteneciera a $F$, entonces $f(x)=y$ pertenecería a $f(F)$, contradicción. Por tanto,

$$
x\notin F.
$$

Así,

$$
x\in E\setminus F,
$$

y por ello

$$
y=f(x)\in f(E\setminus F).
$$

Hemos probado siempre que

$$
\boxed{f(E)\setminus f(F)\subseteq f(E\setminus F).}
$$

#### Intento de la inclusión inversa

Tomemos ahora

$$
y\in f(E\setminus F).
$$

Existe entonces $x\in E\setminus F$ tal que

$$
f(x)=y.
$$

Sabemos que $x\in E$, así que

$$
y\in f(E).
$$

Para concluir que

$$
y\in f(E)\setminus f(F)
$$

necesitamos demostrar

$$
y\notin f(F).
$$

Aquí se atasca la prueba. Del hecho

$$
x\notin F
$$

**no** podemos deducir automáticamente

$$
f(x)\notin f(F).
$$

Podría existir otro punto $z\in F$ con

$$
f(z)=f(x).
$$

Ese es el paso ilegítimo que habría que introducir para completar la demostración sin hipótesis adicionales.

#### La hipótesis que repara la prueba

Supongamos ahora que $f$ es inyectiva. Si $y=f(x)$ perteneciera también a $f(F)$, existiría $z\in F$ con

$$
f(z)=y=f(x).
$$

Por inyectividad,

$$
z=x.
$$

Pero $z\in F$ y $x\notin F$, contradicción. Por tanto,

$$
y\notin f(F),
$$

y obtenemos la inclusión inversa.

Así, bajo inyectividad,

$$
\boxed{f(E\setminus F)=f(E)\setminus f(F).}
$$

#### Contraejemplo sin inyectividad

Tomemos

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2,
$$

$$
E=\{-1\},
\qquad
F=\{1\}.
$$

Como $E\cap F=\varnothing$,

$$
E\setminus F=\{-1\},
$$

y por tanto

$$
f(E\setminus F)=\{1\}.
$$

Pero

$$
f(E)=\{1\}=f(F),
$$

de modo que

$$
f(E)\setminus f(F)=\varnothing.
$$

Así,

$$
\boxed{
\varnothing
=
f(E)\setminus f(F)
\subsetneq
f(E\setminus F)
=
\{1\}.
}
$$

#### Lectura de la solución

El laboratorio reproduce un patrón de investigación matemática muy útil:

$$
\boxed{
\text{conjetura}
\to
\text{intento de prueba}
\to
\text{punto de atasco}
\to
\text{hipótesis necesaria}
\to
\text{enunciado corregido}
\to
\text{contraejemplo sin la hipótesis}
}
$$

Una prueba que se atasca no es necesariamente tiempo perdido. Si sabemos leer el atasco, puede revelar la estructura exacta del resultado verdadero.

### Laboratorio 5 — Fabricar una inversa eligiendo la rama adecuada

Consideremos

$$
q\colon\mathbb R\to\mathbb R,
\qquad
q(x)=(x-2)^2+1.
$$

**Problema.** La función $q$ no es biyectiva. Construir dos restricciones naturales que sí sean biyectivas sobre su imagen y determinar sus inversas.

#### Diagnóstico

Hay dos fallos en la declaración original.

Primero,

$$
q(1)=2=q(3),
$$

así que $q$ no es inyectiva.

Segundo,

$$
q(x)=(x-2)^2+1\ge1,
$$

por lo que ningún real menor que $1$ pertenece a la imagen. Así, $q$ tampoco es sobreyectiva sobre $\mathbb R$.

La gráfica algebraica tiene un punto central en $x=2$. A la derecha de ese punto la regla es estrictamente creciente; a la izquierda es estrictamente decreciente. Eso sugiere dos restricciones posibles.

#### Primera rama: $x\ge2$

Definamos

$$
q_+\colon[2,\infty)\to[1,\infty),
\qquad
q_+(x)=(x-2)^2+1.
$$

Si

$$
2\le x_1<x_2,
$$

entonces

$$
q_+(x_2)-q_+(x_1)
=
(x_2-x_1)(x_1+x_2-4).
$$

El primer factor es positivo. Además, $x_2>2$ y $x_1\ge2$, así que

$$
x_1+x_2-4>0.
$$

Por tanto,

$$
q_+(x_1)<q_+(x_2).
$$

La función es estrictamente creciente y, en consecuencia, inyectiva.

Para demostrar sobreyectividad sobre $[1,\infty)$, sea $y\ge1$. Entonces

$$
y-1\ge0
$$

y podemos tomar

$$
x=2+\sqrt{y-1}\ge2.
$$

Se cumple

$$
q_+(x)
=
(\sqrt{y-1})^2+1
=
y.
$$

Así, $q_+$ es biyectiva. Resolviendo

$$
y=(x-2)^2+1
$$

con la condición $x\ge2$, obtenemos

$$
x-2=\sqrt{y-1},
$$

y por tanto

$$
\boxed{q_+^{-1}(y)=2+\sqrt{y-1},\qquad y\ge1.}
$$

#### Segunda rama: $x\le2$

Definamos ahora

$$
q_-\colon(-\infty,2]\to[1,\infty),
\qquad
q_-(x)=(x-2)^2+1.
$$

Si

$$
x_1<x_2\le2,
$$

entonces

$$
q_-(x_2)-q_-(x_1)
=
(x_2-x_1)(x_1+x_2-4).
$$

El primer factor es positivo, pero ahora

$$
x_1+x_2-4<0,
$$

porque $x_1<2$ y $x_2\le2$. Por tanto,

$$
q_-(x_2)<q_-(x_1),
$$

de modo que $q_-$ es estrictamente decreciente y, por ello, inyectiva.

Dado $y\ge1$, el número

$$
x=2-\sqrt{y-1}\le2
$$

satisface $q_-(x)=y$. Así, $q_-$ también es sobreyectiva sobre $[1,\infty)$ y por tanto biyectiva.

Esta vez la condición $x\le2$ selecciona el signo negativo:

$$
\boxed{q_-^{-1}(y)=2-\sqrt{y-1},\qquad y\ge1.}
$$

#### Lectura de la solución

No existe contradicción entre las dos fórmulas de inversa. No estamos afirmando que una misma función tenga dos inversas. Hemos construido **dos funciones distintas** mediante restricciones distintas del dominio:

$$
q_+
e q_-.
$$

Cada una posee su propia inversa única.

El patrón general es importante:

$$
\boxed{
\text{función no invertible}
\to
\text{localizar una región inyectiva}
\to
\text{restringir dominio}
\to
\text{ajustar codominio a la imagen}
\to
\text{invertir}
}
$$

### Laboratorio 6 — Una sucesión antes de hablar de límites

Definamos

$$
a\colon\mathbb N\to\mathbb R,
\qquad
 a(n)=\frac{n}{n+1},
$$

donde

$$
\mathbb N=\{0,1,2,\dots\}.
$$

**Problema.** Analizar esta regla utilizando únicamente el lenguaje funcional del capítulo: dominio, codominio, imagen, preimágenes puntuales, monotonía, inyectividad, sobreyectividad y gráfica. No debemos hablar todavía de convergencia.

#### Diagnóstico

La notación $a(n)$ puede hacer que el objeto parezca nuevo, pero estructuralmente no lo es. Tenemos simplemente una función cuyo dominio es $\mathbb N$.

La primera pregunta, por tanto, no es «¿a qué se acerca?», sino

$$
\boxed{\text{¿qué función es y qué propiedades funcionales tiene?}}
$$

#### Solución

El dominio es

$$
\mathbb N,
$$

y el codominio declarado es

$$
\mathbb R.
$$

Como $n\ge0$, el denominador $n+1$ es siempre positivo, de modo que la regla está definida para cada natural.

Podemos reescribir

$$
a(n)
=
1-\frac1{n+1}.
$$

En particular,

$$
0\le a(n)<1
$$

para todo $n\in\mathbb N$. Sin embargo, la imagen no es todo el intervalo $[0,1)$. Es el conjunto discreto

$$
\boxed{
\operatorname{Im}(a)
=
\left\{\frac{n}{n+1}:n\in\mathbb N\right\}
=
\left\{0,\frac12,\frac23,\frac34,\dots\right\}.
}
$$

Por ejemplo,

$$
a^{-1}\left(\left\{\frac12\right\}\right)=\{1\},
$$

$$
a^{-1}\left(\left\{\frac23\right\}\right)=\{2\},
$$

y

$$
a^{-1}(\{1\})=\varnothing.
$$

Estudiemos ahora la monotonía. Para $n\in\mathbb N$,

$$
a(n+1)-a(n)
=
\frac{n+1}{n+2}-\frac{n}{n+1}.
$$

Llevando a común denominador,

$$
a(n+1)-a(n)
=
\frac{(n+1)^2-n(n+2)}{(n+1)(n+2)}
=
\frac1{(n+1)(n+2)}.
$$

Como el denominador es positivo,

$$
a(n+1)>a(n).
$$

Más generalmente, si $m<n$, entonces

$$
\frac{m}{m+1}<\frac{n}{n+1},
$$

pues, al multiplicar por los denominadores positivos,

$$
m(n+1)<n(m+1)
$$

equivale a

$$
m<n.
$$

Así, $a$ es estrictamente creciente sobre $\mathbb N$. Por el teorema de §2.9,

$$
\boxed{a\text{ es inyectiva}.}
$$

No es sobreyectiva como función $\mathbb N\to\mathbb R$, porque, por ejemplo,

$$
2\notin\operatorname{Im}(a).
$$

Si en cambio consideramos

$$
a\colon\mathbb N\to\operatorname{Im}(a),
$$

la función es biyectiva. Para $y\in\operatorname{Im}(a)$, de

$$
y=\frac{n}{n+1}
$$

obtenemos

$$
y(n+1)=n,
$$

$$
y=n(1-y),
$$

y por tanto

$$
\boxed{n=\frac{y}{1-y}.}
$$

Así, sobre la imagen,

$$
a^{-1}(y)=\frac{y}{1-y}.
$$

No hay conflicto con el hecho de que la expresión de la derecha parezca real: si $y$ pertenece realmente a $\operatorname{Im}(a)$, ese cociente es precisamente el natural que produjo $y$.

La gráfica es

$$
\Gamma_a
=
\left\{
\left(n,\frac{n}{n+1}\right):n\in\mathbb N
\right\}.
$$

A diferencia de muchas gráficas anteriores, no forma una curva completa sobre un intervalo: solo contiene los puntos cuyas primeras coordenadas son naturales.

#### Lectura de la solución

Este objeto es lo que en el capítulo siguiente llamaremos una **sucesión real**. Pero todo lo que acabamos de hacer pertenece ya a la teoría de funciones:

$$
\boxed{
\text{sucesión}
=
\text{función con dominio }\mathbb N.
}
$$

Todavía no hemos preguntado si los valores «se acercan» a algún número ni hemos definido qué significaría rigurosamente esa frase. Esa será precisamente la nueva cuestión de `T1-C04`.

### Qué estructuras se combinaron

Las seis estaciones permiten revisar el capítulo como una red y no como una lista lineal.

- El Laboratorio 1 separó **restricciones de una expresión** de **datos de una función**.
- El Laboratorio 2 mostró simultáneamente la sensibilidad de inyectividad al dominio y de sobreyectividad al codominio.
- El Laboratorio 3 obligó a verificar **tipos** antes de componer y distinguió composición funcional de mera sustitución algebraica.
- El Laboratorio 4 utilizó una **prueba fallida** como instrumento para descubrir la hipótesis correcta.
- El Laboratorio 5 combinó restricción, monotonía, imagen, biyectividad e inversión.
- El Laboratorio 6 mostró que el siguiente objeto del curso, una sucesión, entra naturalmente en el lenguaje funcional ya construido.

La arquitectura general puede verse así:

$$
\boxed{
\begin{array}{c}
\text{función completa}
\to
\text{imagen/preimagen}
\to
\text{inyectividad/sobreyectividad}
\to
\text{composición}
\to
\text{inversa},\\[6pt]
\text{función}+\text{producto cartesiano}
\to
\text{gráfica},\\[6pt]
\text{función}+\text{orden}
\to
\text{monotonía}
\to
\text{inyectividad}.
\end{array}}
$$

### Un mapa de decisión antes del banco final

Cuando aparezca un problema funcional, conviene formular preguntas en un orden parecido al siguiente:

$$
\boxed{
\begin{array}{c}
\text{¿qué función es?}
\to
\text{dominio/codominio}
\to
\text{imagen/preimagen}\\
\to
\text{inyectiva/sobreyectiva?}
\to
\text{¿se compone?}
\to
\text{¿se puede invertir?}
\end{array}}
$$

El diagrama no es un algoritmo rígido. Algunas preguntas pueden no ser relevantes en un problema concreto. Su función es impedir que empecemos manipulando una fórmula antes de haber identificado la estructura matemática.

A ese eje principal podemos añadir dos preguntas transversales:

- **¿la gráfica aporta información útil?** Entonces conviene traducir entre puntos $(x,f(x))$ y propiedades funcionales, sin confundir imagen con codominio;
- **¿el dominio está ordenado?** Entonces puede ser útil estudiar monotonía, especialmente si buscamos inyectividad o una restricción invertible.

### Antes de seguir

::: {.callout-tip title="Antes de seguir"}
**1.** En el Laboratorio 1, ¿por qué $[-2,2]$ no debe llamarse automáticamente «el dominio de $p$»?

**Respuesta.** Porque $[-2,2]$ es el dominio real máximo permitido por la expresión $\sqrt{4-x^2}$. Una función puede declararse sobre cualquier subconjunto adecuado de ese conjunto. El dominio forma parte de los datos de la función, no es siempre sinónimo de «todos los puntos donde la fórmula puede evaluarse».
:::

::: {.callout-tip title="Antes de seguir"}
**2.** En el Laboratorio 4, ¿qué inclusión sobre diferencias de imágenes es válida sin suponer inyectividad?

**Respuesta.** Siempre se cumple

$$
f(E)\setminus f(F)\subseteq f(E\setminus F).
$$

La inclusión inversa puede fallar porque un punto de $E\setminus F$ y otro punto de $F$ pueden compartir la misma imagen. La inyectividad elimina exactamente esa posibilidad.
:::

::: {.callout-tip title="Antes de seguir"}
**3.** ¿Por qué las dos ramas del Laboratorio 5 no contradicen la unicidad de la función inversa?

**Respuesta.** Porque $q_+$ y $q_-$ son funciones distintas: tienen dominios distintos. Cada una posee una única inversa, y esas inversas son diferentes porque revierten asignaciones diferentes.
:::

::: {.callout-tip title="Antes de seguir"}
**4.** En el Laboratorio 6, ¿por qué no podemos escribir

$$
\operatorname{Im}(a)=[0,1)?
$$

**Respuesta.** Porque $a$ solo toma valores correspondientes a entradas naturales. Aunque todos sus valores pertenecen a $[0,1)$, la mayoría de los números de ese intervalo no son alcanzados. Por ejemplo, no existe $n\in\mathbb N$ con $n/(n+1)=1/3$.
:::

### Lo que queda antes de cerrar el capítulo

La arquitectura conceptual de `T1-C03` está ya completa. La última sección será el banco final de ejercicios y soluciones.

Allí desaparecerá gran parte del andamiaje del laboratorio. El lector deberá decidir de manera autónoma qué herramientas utilizar entre

$$
\boxed{
\text{dominio/codominio}
+
\text{imagen/preimagen}
+
\text{clasificación}
+
\text{composición}
+
\text{inversa}
+
\text{gráfica}
+
\text{monotonía}.
}
$$

Además, algunas consignas exigirán construir contraejemplos, reparar afirmaciones falsas o diseñar restricciones que hagan posible una inversa. La cuestión central seguirá siendo la misma con la que comenzó el capítulo: antes de calcular, debemos saber **qué función tenemos delante**.

## Ejercicios y soluciones {#sec-t1-c03-11}

Llegamos al banco final de `T1-C03`. En las secciones anteriores las herramientas funcionales fueron apareciendo de manera progresiva y, en §2.10, se combinaron todavía con una guía explícita de estrategia. Aquí la ayuda disminuye deliberadamente: antes de calcular, habrá que decidir qué estructura es relevante y qué datos de la función deben controlarse.

El banco contiene exactamente cuarenta ejercicios, distribuidos en siete niveles:

$$
7A+7B+7C+6D+5E+5F+3G=40.
$$

Los niveles no miden solamente dificultad algebraica. Un ejercicio puede resultar corto y, sin embargo, exigir una distinción conceptual importante. En particular, se evaluará de manera recurrente la capacidad de separar:

- fórmula, función completa y gráfica;
- dominio, codominio e imagen;
- preimagen de un conjunto y función inversa;
- existencia de una inversa y cálculo de una fórmula candidata;
- propiedades de una función y propiedades de una composición.

Todos los problemas pueden resolverse con el capítulo precedente sobre los reales y con el presente capítulo. No se necesitan límites, continuidad ni derivadas.

### Nivel A — Reconocimiento y comprensión

::: {#exr-t1-0076}
<!-- CPM-T1-EXR-0076 | A | CONCEPTUAL | COMPUTATION | ORIGINAL -->
**Ejercicio A1. Dominio, codominio e imagen.** Sea

$$
f\colon[-2,3]\to\mathbb R,
\qquad
f(x)=x^2.
$$

Identifica el dominio, el codominio y la imagen de $f$. Decide si imagen y codominio coinciden.
:::

::: {#exr-t1-0077}
<!-- CPM-T1-EXR-0077 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A2. ¿Es realmente una función?** Considera la relación

$$
R=\{(0,1),(1,2),(2,2),(2,3)\}
$$

desde $A=\{0,1,2\}$ hacia $B=\{1,2,3\}$.

1. ¿Define $R$ una función $A\to B$?
2. Identifica exactamente qué parte de la condición «a cada entrada corresponde exactamente una salida» falla.
3. Elimina el menor número posible de pares para obtener una función $A\to B$.
:::

::: {#exr-t1-0078}
<!-- CPM-T1-EXR-0078 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A3. Misma fórmula, ¿misma función?** Sean

$$
f\colon\mathbb R\to\mathbb R,
\qquad f(x)=x^2,
$$

y

$$
g\colon\mathbb R\to[0,\infty),
\qquad g(x)=x^2.
$$

Según la convención adoptada en este libro, decide si $f=g$ y justifica tu respuesta. Después compara sus imágenes.
:::

::: {#exr-t1-0079}
<!-- CPM-T1-EXR-0079 | A | COMPUTATION | CONCEPTUAL | ORIGINAL -->
**Ejercicio A4. Imagen y preimagen.** Sea

$$
q\colon\mathbb R\to[0,\infty),
\qquad q(x)=x^2.
$$

Calcula

$$
q([-2,1])
$$

y

$$
q^{-1}([1,4)).
$$

Recuerda que en la segunda expresión $q^{-1}$ designa una **preimagen de conjunto**.
:::

::: {#exr-t1-0080}
<!-- CPM-T1-EXR-0080 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A5. Leer una función desde una tabla.** Sea

$$
p\colon\{-2,-1,0,1\}\to\{1,2,3,4\}
$$

la función dada por

| $x$ | $-2$ | $-1$ | $0$ | $1$ |
|---:|---:|---:|---:|---:|
| $p(x)$ | $3$ | $1$ | $1$ | $4$ |

Determina:

1. $\operatorname{Im}(p)$;
2. si $p$ es inyectiva;
3. si $p$ es sobreyectiva.
:::

::: {#exr-t1-0081}
<!-- CPM-T1-EXR-0081 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A6. Una restricción cambia la función.** Sea

$$
f\colon\mathbb R\to\mathbb R,
\qquad f(x)=x^2,
$$

y considera la restricción

$$
f|_{[0,\infty)}\colon[0,\infty)\to\mathbb R.
$$

1. ¿Cuál es su imagen?
2. ¿Es inyectiva?
3. ¿Es sobreyectiva?
4. ¿Qué cambio adicional permitiría convertir esta restricción en una biyección?
:::

::: {#exr-t1-0082}
<!-- CPM-T1-EXR-0082 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A7. Leer la notación como una afirmación lógica.** Sea

$$
a\colon\{0,1,2,3\}\to\mathbb R,
\qquad
a(n)=\frac{n}{n+1}.
$$

1. Traduce la declaración $a\colon\{0,1,2,3\}\to\mathbb R$ a una frase que haga explícitas existencia y unicidad de la salida.
2. Calcula $\operatorname{Im}(a)$.
3. Explica por qué el hecho de que la imagen no sea todo $\mathbb R$ no impide que $a$ sea una función.
:::

### Nivel B — Aplicación directa

::: {#exr-t1-0083}
<!-- CPM-T1-EXR-0083 | B | COMPUTATION | ORIGINAL -->
**Ejercicio B1. Dos órdenes de composición.** Sean

$$
f\colon\mathbb R\to\mathbb R,
\qquad f(x)=2x-1,
$$

y

$$
g\colon\mathbb R\to\mathbb R,
\qquad g(x)=x^2.
$$

Calcula $g\circ f$ y $f\circ g$. Decide si son la misma función.
:::

::: {#exr-t1-0084}
<!-- CPM-T1-EXR-0084 | B | COMPUTATION | CONCEPTUAL | ORIGINAL -->
**Ejercicio B2. Antes de componer, controla los tipos.** Sean

$$
u\colon[-1,\infty)\to[0,\infty),
\qquad u(x)=\sqrt{x+1},
$$

y

$$
v\colon[0,\infty)\setminus\{2\}\to\mathbb R,
\qquad v(t)=\frac1{t-2}.
$$

1. Explica por qué $v\circ u$ no está definida como composición sobre todo $[-1,\infty)$ con las funciones tal como fueron declaradas.
2. Encuentra el mayor subconjunto $E\subseteq[-1,\infty)$ tal que
   $$
   v\circ(u|_E)
   $$
   esté bien definida.
3. Escribe su fórmula.
:::

::: {#exr-t1-0085}
<!-- CPM-T1-EXR-0085 | B | COMPUTATION | ORIGINAL -->
**Ejercicio B3. Intervalos bajo una función afín.** Sea

$$
f\colon\mathbb R\to\mathbb R,
\qquad f(x)=3x-2.
$$

Calcula

$$
f([1,4))
$$

y

$$
f^{-1}((-5,4]).
$$
:::

::: {#exr-t1-0086}
<!-- CPM-T1-EXR-0086 | B | COMPUTATION | ORIGINAL -->
**Ejercicio B4. La preimagen puede tener dos ramas.** Sea

$$
q\colon\mathbb R\to[0,\infty),
\qquad q(x)=x^2.
$$

Calcula

$$
q^{-1}((4,9])
$$

y explica por qué el resultado no es un solo intervalo.
:::

::: {#exr-t1-0087}
<!-- CPM-T1-EXR-0087 | B | CONCEPTUAL | ORIGINAL -->
**Ejercicio B5. Clasificar y reparar.** Considera

$$
r\colon[0,\infty)\to\mathbb R,
\qquad r(x)=x^2.
$$

1. Clasifica $r$ respecto de inyectividad y sobreyectividad.
2. Modifica solamente el codominio para obtener una biyección.
3. Escribe la inversa de la función resultante.
:::

::: {#exr-t1-0088}
<!-- CPM-T1-EXR-0088 | B | COMPUTATION | CONCEPTUAL | ORIGINAL -->
**Ejercicio B6. Función por tramos.** Sea

$$
p\colon\mathbb R\to\mathbb R,
\qquad
p(x)=
\begin{cases}
x+1, & x<0,\\
x^2, & x\ge0.
\end{cases}
$$

1. Calcula $p(-2)$, $p(0)$ y $p(2)$.
2. Determina $\operatorname{Im}(p)$.
3. Decide si $p$ es inyectiva y si es sobreyectiva.
:::

::: {#exr-t1-0089}
<!-- CPM-T1-EXR-0089 | B | GEOMETRY | CONCEPTUAL | ORIGINAL -->
**Ejercicio B7. Transformar una gráfica sin memorizar recetas.** Sea $f\colon\mathbb R\to\mathbb R$ una función y define

$$
h(x)=2f(x-3)-1.
$$

Supón que $(a,b)$ pertenece a la gráfica de $f$.

1. Determina qué punto de la gráfica de $h$ corresponde a $(a,b)$.
2. Describe, en orden, las transformaciones geométricas que llevan la gráfica de $f$ a la de $h$.
:::

### Nivel C — Combinación estructural

::: {#exr-t1-0090}
<!-- CPM-T1-EXR-0090 | C | PROOF | ORIGINAL -->
**Ejercicio C1. Inyectividad de una función afín.** Sea

$$
f\colon\mathbb R\to\mathbb R,
\qquad f(x)=ax+b,
$$

donde $a\ne0$. Demuestra que $f$ es inyectiva.
:::

::: {#exr-t1-0091}
<!-- CPM-T1-EXR-0091 | C | PROOF | ORIGINAL -->
**Ejercicio C2. Biyectividad del recíproco.** Sea

$$
r\colon(0,\infty)\to(0,\infty),
\qquad r(x)=\frac1x.
$$

Demuestra que $r$ es biyectiva y determina $r^{-1}$.
:::

::: {#exr-t1-0092}
<!-- CPM-T1-EXR-0092 | C | PROOF | COMPUTATION | ORIGINAL -->
**Ejercicio C3. Probar primero, invertir después.** Sea

$$
f\colon[0,\infty)\to[1,\infty),
\qquad f(x)=x^2+1.
$$

1. Demuestra que $f$ es inyectiva.
2. Demuestra que $f$ es sobreyectiva construyendo un antecedente de un $y\in[1,\infty)$ arbitrario.
3. Solo después de lo anterior, determina $f^{-1}$.
:::

::: {#exr-t1-0093}
<!-- CPM-T1-EXR-0093 | C | PROOF | SYNTHESIS | ORIGINAL -->
**Ejercicio C4. La composición conserva la inyectividad.** Sean

$$
f\colon A\to B,
\qquad g\colon B\to C
$$

funciones inyectivas. Demuestra directamente, a partir de la definición, que $g\circ f$ es inyectiva.
:::

::: {#exr-t1-0094}
<!-- CPM-T1-EXR-0094 | C | PROOF | SYNTHESIS | ORIGINAL -->
**Ejercicio C5. Álgebra de preimágenes.** Sea $f\colon A\to B$ y sean $U,V\subseteq B$. Demuestra:

$$
f^{-1}(U\cap V)=f^{-1}(U)\cap f^{-1}(V)
$$

y

$$
f^{-1}(B\setminus U)=A\setminus f^{-1}(U).
$$

Haz la demostración mediante pertenencia de un elemento arbitrario.
:::

::: {#exr-t1-0095}
<!-- CPM-T1-EXR-0095 | C | PROOF | CONCEPTUAL | ORIGINAL -->
**Ejercicio C6. El cuadrado cambia de monotonía.** Demuestra que

$$
q(x)=x^2
$$

es estrictamente creciente en $[0,\infty)$ y estrictamente decreciente en $(-\infty,0]$. Deduce que su restricción a cualquiera de esos intervalos es inyectiva.
:::

::: {#exr-t1-0096}
<!-- CPM-T1-EXR-0096 | C | GEOMETRY | PROOF | ORIGINAL -->
**Ejercicio C7. Gráfica de una función y de su inversa.** Sea

$$
f\colon\mathbb R\to\mathbb R,
\qquad f(x)=2x-3.
$$

1. Demuestra que $f$ es biyectiva y calcula $f^{-1}$.
2. Prueba que
   $$
   (x,y)\in\Gamma_f
   \quad\Longleftrightarrow\quad
   (y,x)\in\Gamma_{f^{-1}}.
   $$
3. Interpreta geométricamente la equivalencia anterior.
:::

### Nivel D — Inversión y diagnóstico

::: {#exr-t1-0097}
<!-- CPM-T1-EXR-0097 | D | PROOF | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio D1. ¿Qué hereda una composición inyectiva?** Sean

$$
f\colon A\to B,
\qquad g\colon B\to C.
$$

Supón que $g\circ f$ es inyectiva.

1. Demuestra que $f$ debe ser inyectiva.
2. Decide si $g$ debe ser inyectiva. Si la respuesta es negativa, construye un contraejemplo explícito.
:::

::: {#exr-t1-0098}
<!-- CPM-T1-EXR-0098 | D | PROOF | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio D2. ¿Qué hereda una composición sobreyectiva?** Sean

$$
f\colon A\to B,
\qquad g\colon B\to C.
$$

Supón que $g\circ f$ es sobreyectiva.

1. Demuestra que $g$ debe ser sobreyectiva.
2. Decide si $f$ debe ser sobreyectiva. Si la respuesta es negativa, construye un contraejemplo explícito.
:::

::: {#exr-t1-0099}
<!-- CPM-T1-EXR-0099 | D | CONCEPTUAL | SYNTHESIS | ORIGINAL -->
**Ejercicio D3. Auditoría de dominio y codominio.** Considera las cuatro funciones

$$
p\colon\mathbb R\to\mathbb R,
\qquad p(x)=x^2,
$$

$$
q\colon\mathbb R\to[0,\infty),
\qquad q(x)=x^2,
$$

$$
r\colon[0,\infty)\to\mathbb R,
\qquad r(x)=x^2,
$$

y

$$
s\colon[0,\infty)\to[0,\infty),
\qquad s(x)=x^2.
$$

1. Decide qué pares, si alguno, son funciones iguales según la convención del libro.
2. Clasifica cada función como inyectiva, sobreyectiva, biyectiva o ninguna de las anteriores.
3. Explica qué propiedad se modifica al cambiar solo el dominio y qué propiedad puede modificarse al cambiar solo el codominio.
:::

::: {#exr-t1-0100}
<!-- CPM-T1-EXR-0100 | D | CONCEPTUAL | SYNTHESIS | ORIGINAL -->
**Ejercicio D4. Una «inversa» demasiado rápida.** Un estudiante escribe:

> Si $f(x)=x^2$, entonces $y=x^2$, de donde $x=\sqrt y$. Por tanto, $f^{-1}(y)=\sqrt y$.

Analiza el argumento para la función

$$
f\colon\mathbb R\to[0,\infty),
\qquad f(x)=x^2.
$$

1. Localiza el error conceptual.
2. Explica por qué resolver una ecuación no basta para demostrar que existe una función inversa.
3. Repara la situación modificando el dominio de $f$ de dos maneras distintas y escribe las inversas correspondientes.
:::

::: {#exr-t1-0101}
<!-- CPM-T1-EXR-0101 | D | PROOF | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio D5. Una igualdad plausible que puede fallar.** Sea $f\colon A\to B$ y $E,F\subseteq A$.

1. Demuestra que siempre se cumple
   $$
   f(E\cap F)\subseteq f(E)\cap f(F).
   $$
2. Explica dónde se atascaría un intento de demostrar la inclusión inversa sin hipótesis adicionales.
3. Indica una hipótesis suficiente sobre $f$ que convierta la inclusión en igualdad.
:::

::: {#exr-t1-0102}
<!-- CPM-T1-EXR-0102 | D | CONCEPTUAL | SYNTHESIS | ORIGINAL -->
**Ejercicio D6. Reparar una función por tramos mal definida.** Se pretende definir

$$
h\colon\mathbb R\to\mathbb R,
\qquad
h(x)=
\begin{cases}
x+1, & x\ge0,\\
-x, & x\le0.
\end{cases}
$$

1. Explica por qué esta regla no define una función.
2. Propón dos reparaciones distintas que cambien únicamente las condiciones de los tramos, no las fórmulas $x+1$ y $-x$.
3. ¿Las dos reparaciones obtenidas definen necesariamente la misma función? Justifica.
:::

### Nivel E — Contraejemplos

::: {#exr-t1-0103}
<!-- CPM-T1-EXR-0103 | E | COUNTEREXAMPLE | CONCEPTUAL | ORIGINAL -->
**Ejercicio E1. Misma fórmula, funciones distintas.** Construye dos funciones distintas que utilicen la misma fórmula $1/x$. Deben diferir por su dominio, por su codominio o por ambos. Justifica formalmente que no son iguales.
:::

::: {#exr-t1-0104}
<!-- CPM-T1-EXR-0104 | E | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio E2. Separar inyectividad y sobreyectividad.** Construye:

1. una función inyectiva que no sea sobreyectiva;
2. una función sobreyectiva que no sea inyectiva.

Puedes usar conjuntos finitos o subconjuntos de $\mathbb R$, pero debes declarar dominio, codominio y regla.
:::

::: {#exr-t1-0105}
<!-- CPM-T1-EXR-0105 | E | COUNTEREXAMPLE | COMPUTATION | ORIGINAL -->
**Ejercicio E3. La composición no es conmutativa.** Construye funciones $f,g\colon\mathbb R\to\mathbb R$ tales que

$$
g\circ f\ne f\circ g.
$$

Calcula ambas composiciones y exhibe al menos un valor de $x$ en el que difieran.
:::

::: {#exr-t1-0106}
<!-- CPM-T1-EXR-0106 | E | COUNTEREXAMPLE | SYNTHESIS | ORIGINAL -->
**Ejercicio E4. Intersecciones e imágenes.** Construye una función $f\colon A\to B$ y subconjuntos $E,F\subseteq A$ tales que

$$
f(E\cap F)\subsetneq f(E)\cap f(F).
$$

Explica qué rasgo de $f$ hace posible la inclusión estricta.
:::

::: {#exr-t1-0107}
<!-- CPM-T1-EXR-0107 | E | COUNTEREXAMPLE | CONCEPTUAL | ORIGINAL -->
**Ejercicio E5. No decreciente no significa inyectiva.** Construye una función $m\colon\mathbb R\to\mathbb R$ que sea no decreciente pero no inyectiva. Verifica ambas afirmaciones.
:::

### Nivel F — Descubrimiento guiado

::: {#exr-t1-0108}
<!-- CPM-T1-EXR-0108 | F | DISCOVERY | CONCEPTUAL | ORIGINAL -->
**Ejercicio F1. Reconstruir una función desde su gráfica como conjunto.** Se sabe que $f\colon A\to B$ tiene

$$
B=\{1,2,4\}
$$

y que su gráfica es exactamente

$$
\Gamma_f=\{(-2,1),(0,1),(3,4)\}.
$$

1. Reconstruye $A$.
2. Escribe todos los valores de $f$.
3. Determina $\operatorname{Im}(f)$.
4. Decide si $f$ es inyectiva y si es sobreyectiva.
5. Explica por qué conocer solo la gráfica como conjunto de pares no habría bastado, bajo la convención de este libro, para reconstruir el codominio si $B$ no hubiese sido declarado.
:::

::: {#exr-t1-0109}
<!-- CPM-T1-EXR-0109 | F | DISCOVERY | PROOF | ORIGINAL -->
**Ejercicio F2. Descubrir las leyes de preimagen.** Sea $f\colon A\to B$ y sean $U,V\subseteq B$.

Completa una cadena de equivalencias empezando por un elemento arbitrario $x\in A$ para demostrar:

$$
f^{-1}(U\cup V)=f^{-1}(U)\cup f^{-1}(V),
$$

$$
f^{-1}(U\cap V)=f^{-1}(U)\cap f^{-1}(V),
$$

y

$$
f^{-1}(B\setminus U)=A\setminus f^{-1}(U).
$$

Después explica por qué ninguna de estas identidades requiere inyectividad ni sobreyectividad.
:::

::: {#exr-t1-0110}
<!-- CPM-T1-EXR-0110 | F | DISCOVERY | SYNTHESIS | ORIGINAL -->
**Ejercicio F3. Fabricar dos biyectividades a partir del cuadrado.** Parte de la regla

$$
x\mapsto x^2.
$$

1. Encuentra una restricción del dominio y un codominio que produzcan una biyección cuya inversa sea $y\mapsto\sqrt y$.
2. Encuentra otra restricción, distinta de la anterior, que produzca una biyección cuya inversa sea $y\mapsto-\sqrt y$.
3. Demuestra en ambos casos inyectividad y sobreyectividad.
:::

::: {#exr-t1-0111}
<!-- CPM-T1-EXR-0111 | F | DISCOVERY | PROOF | ORIGINAL -->
**Ejercicio F4. Descubrir el criterio exacto de existencia de una inversa.** Sea $f\colon A\to B$. Para cada $y\in B$, considera la ecuación

$$
f(x)=y.
$$

1. Explica qué propiedad de $f$ garantiza que para cada $y$ exista **al menos una** solución $x\in A$.
2. Explica qué propiedad garantiza que exista **a lo sumo una** solución.
3. Deduce que existe una función inversa $f^{-1}\colon B\to A$ si y solo si $f$ es biyectiva.
4. Indica cómo se define $f^{-1}(y)$ a partir de la solución única.
:::

::: {#exr-t1-0112}
<!-- CPM-T1-EXR-0112 | F | DISCOVERY | GEOMETRY | ORIGINAL -->
**Ejercicio F5. Reconstruir una transformación como composición.** Define

$$
s(x)=x^2,
\qquad
q(x)=-2(x-3)^2+1.
$$

Para $a,c\in\mathbb R$, escribe

$$
T_a(x)=x+a,
\qquad
M_c(x)=cx.
$$

1. Expresa $q$ como una composición de $s$, traslaciones $T_a$ y una dilatación/reflexión $M_c$.
2. Usa la composición obtenida para describir, en orden, cómo se transforma la gráfica de $s$ en la de $q$.
3. Determina el punto al que se transforma el vértice $(0,0)$.
:::

### Nivel G — Desafíos

::: {#exr-t1-0113}
<!-- CPM-T1-EXR-0113 | G | PROOF | SYNTHESIS | ORIGINAL -->
**Ejercicio G1. Caracterización de la inyectividad mediante intersecciones.** Sea $f\colon A\to B$. Demuestra que las siguientes afirmaciones son equivalentes:

1. $f$ es inyectiva;
2. para todos $E,F\subseteq A$,
   $$
   f(E\cap F)=f(E)\cap f(F).
   $$

En la dirección menos inmediata, elige subconjuntos apropiados para recuperar la inyectividad a partir de la igualdad de imágenes.
:::

::: {#exr-t1-0114}
<!-- CPM-T1-EXR-0114 | G | PROOF | COUNTEREXAMPLE | SYNTHESIS | ORIGINAL -->
**Ejercicio G2. Inversas laterales y cancelación.** Sean

$$
f\colon A\to B,
\qquad g\colon B\to A.
$$

1. Demuestra que
   $$
   g\circ f=\operatorname{id}_A
   $$
   implica que $f$ es inyectiva y $g$ es sobreyectiva.
2. Demuestra que
   $$
   f\circ g=\operatorname{id}_B
   $$
   implica que $f$ es sobreyectiva y $g$ es inyectiva.
3. Construye contraejemplos que muestren que, en general, las conclusiones de 1 o de 2 no bastan por sí solas para recuperar la identidad de composición correspondiente.
:::

::: {#exr-t1-0115}
<!-- CPM-T1-EXR-0115 | G | PROOF | COUNTEREXAMPLE | SYNTHESIS | ORIGINAL -->
**Ejercicio G3. Composición biyectiva: qué puede concluirse.** Sean

$$
f\colon A\to B,
\qquad g\colon B\to C,
$$

y supón que $g\circ f$ es biyectiva.

1. Demuestra que $f$ es inyectiva.
2. Demuestra que $g$ es sobreyectiva.
3. Decide, mediante prueba o contraejemplo, si $f$ y $g$ deben ser biyectivas.
4. Encuentra una hipótesis adicional sobre $f$ que sea suficiente para forzar que **ambas** funciones sean biyectivas.
5. Encuentra una hipótesis adicional sobre $g$ que también sea suficiente para forzar que **ambas** sean biyectivas.
:::

### Soluciones

Las soluciones siguen exactamente el orden de los ejercicios. En los niveles iniciales se privilegia la lectura precisa de definiciones; en los niveles D–G se explicitan los puntos donde una implicación puede fallar y se construyen contraejemplos cuando son necesarios.

#### Soluciones del nivel A

::: {#sol-t1-0076}
<!-- CPM-T1-SOL-0076 -->
**Solución A1.**

El dominio es el conjunto declarado a la izquierda de la flecha:

$$
\operatorname{Dom}(f)=[-2,3].
$$

El codominio es

$$
\mathbb R.
$$

Para hallar la imagen observamos que $x^2\ge0$ y que, dentro de $[-2,3]$, el valor mínimo $0$ se alcanza en $x=0$, mientras que el mayor cuadrado es

$$
3^2=9.
$$

Todo valor entre $0$ y $9$ aparece: si $0\le y\le9$, entonces $\sqrt y\in[0,3]\subseteq[-2,3]$ y

$$
f(\sqrt y)=y.
$$

Por tanto,

$$
\operatorname{Im}(f)=[0,9].
$$

Imagen y codominio no coinciden, pues

$$
[0,9]\subsetneq\mathbb R.
$$
:::

::: {#sol-t1-0077}
<!-- CPM-T1-SOL-0077 -->
**Solución A2.**

La relación no define una función $A\to B$. Las entradas $0$ y $1$ tienen una salida única, pero la entrada $2$ aparece en dos pares:

$$
(2,2),\qquad(2,3).
$$

Así, para $x=2$ falla la **unicidad** de la salida. No falla la existencia: cada elemento de $A$ aparece al menos una vez como primera coordenada.

Para reparar la relación basta eliminar uno de los dos pares que parten de $2$. Por ejemplo,

$$
\{(0,1),(1,2),(2,2)\}
$$

define una función $A\to B$. También habría servido conservar $(2,3)$ y eliminar $(2,2)$.
:::

::: {#sol-t1-0078}
<!-- CPM-T1-SOL-0078 -->
**Solución A3.**

No se cumple $f=g$ según la convención del libro. Aunque tienen el mismo dominio y satisfacen

$$
f(x)=g(x)=x^2
$$

para todo $x\in\mathbb R$, sus codominios son distintos:

$$
\operatorname{Cod}(f)=\mathbb R,
\qquad
\operatorname{Cod}(g)=[0,\infty).
$$

El codominio forma parte de los datos de la función.

Sin embargo, sus imágenes sí coinciden:

$$
\operatorname{Im}(f)=\operatorname{Im}(g)=[0,\infty).
$$

Esto muestra nuevamente que imagen y codominio son conceptos diferentes.
:::

::: {#sol-t1-0079}
<!-- CPM-T1-SOL-0079 -->
**Solución A4.**

Para la imagen de $[-2,1]$, los cuadrados van desde $0$ hasta $4$. El valor $4$ se alcanza en $x=-2$, y $0$ se alcanza en $x=0$. Por tanto,

$$
q([-2,1])=[0,4].
$$

Ahora buscamos los $x$ tales que

$$
1\le x^2<4.
$$

La primera desigualdad equivale a $|x|\ge1$ y la segunda a $|x|<2$. Combinándolas,

$$
1\le|x|<2.
$$

Por consiguiente,

$$
q^{-1}([1,4))=(-2,-1]\cup[1,2).
$$

No hemos utilizado una función inversa: hemos calculado el conjunto de entradas cuya imagen pertenece a $[1,4)$.
:::

::: {#sol-t1-0080}
<!-- CPM-T1-SOL-0080 -->
**Solución A5.**

Los valores que aparecen en la segunda fila son $3,1,1,4$, así que

$$
\operatorname{Im}(p)=\{1,3,4\}.
$$

La función no es inyectiva, porque

$$
p(-1)=p(0)=1
$$

con $-1\ne0$.

Tampoco es sobreyectiva sobre el codominio $\{1,2,3,4\}$, porque el valor $2$ no es alcanzado. En símbolos,

$$
2\notin\operatorname{Im}(p).
$$
:::

::: {#sol-t1-0081}
<!-- CPM-T1-SOL-0081 -->
**Solución A6.**

La restricción conserva la misma regla, pero solo admite entradas no negativas:

$$
f|_{[0,\infty)}(x)=x^2.
$$

Su imagen es

$$
[0,\infty).
$$

Es inyectiva. En efecto, si $x,y\ge0$ y $x^2=y^2$, entonces

$$
(x-y)(x+y)=0.
$$

Como $x+y\ge0$, la única posibilidad compatible con $x,y\ge0$ y cuadrados iguales es $x=y$; equivalentemente, el cuadrado es estrictamente creciente en $[0,\infty)$.

No es sobreyectiva como función hacia $\mathbb R$, porque ningún número negativo es alcanzado.

Si cambiamos el codominio a $[0,\infty)$, obtenemos

$$
[0,\infty)\to[0,\infty),
\qquad x\mapsto x^2,
$$

que es biyectiva.
:::

::: {#sol-t1-0082}
<!-- CPM-T1-SOL-0082 -->
**Solución A7.**

La declaración significa: para cada

$$
n\in\{0,1,2,3\}
$$

existe exactamente un número real $y$ tal que

$$
y=\frac{n}{n+1},
$$

y ese número se denota por $a(n)$.

Los cuatro valores son

$$
a(0)=0,
\qquad
a(1)=\frac12,
\qquad
a(2)=\frac23,
\qquad
a(3)=\frac34.
$$

Así,

$$
\operatorname{Im}(a)
=
\left\{0,\frac12,\frac23,\frac34\right\}.
$$

No es necesario que una función alcance todo su codominio. Eso sería la condición adicional de sobreyectividad. Para ser función basta que cada entrada del dominio tenga exactamente una salida perteneciente al codominio.
:::

#### Soluciones del nivel B

::: {#sol-t1-0083}
<!-- CPM-T1-SOL-0083 -->
**Solución B1.**

Por definición,

$$
(g\circ f)(x)=g(f(x))=(2x-1)^2.
$$

Por otro lado,

$$
(f\circ g)(x)=f(g(x))=2x^2-1.
$$

No son la misma función. Por ejemplo, en $x=1$,

$$
(g\circ f)(1)=1,
\qquad
(f\circ g)(1)=1,
$$

pero este valor no basta para distinguirlas. En $x=0$,

$$
(g\circ f)(0)=1,
\qquad
(f\circ g)(0)=-1.
$$

Luego

$$
g\circ f\ne f\circ g.
$$
:::

::: {#sol-t1-0084}
<!-- CPM-T1-SOL-0084 -->
**Solución B2.**

La función $u$ tiene imagen $[0,\infty)$, pero $v$ no admite la entrada $2$. Como

$$
u(3)=\sqrt4=2,
$$

no se cumple

$$
u([-1,\infty))\subseteq\operatorname{Dom}(v).
$$

Por tanto, con las funciones tal como fueron declaradas, la composición no está definida sobre todo el dominio de $u$.

Debemos excluir exactamente las entradas que $u$ envía a $2$. Resolver

$$
\sqrt{x+1}=2
$$

da

$$
x=3.
$$

Así, el mayor conjunto posible es

$$
E=[-1,\infty)\setminus\{3\}.
$$

En ese dominio,

$$
(v\circ(u|_E))(x)
=
\frac1{\sqrt{x+1}-2}.
$$

La exclusión de $x=3$ no es un detalle algebraico posterior: es la condición que hace posible la composición como función.
:::

::: {#sol-t1-0085}
<!-- CPM-T1-SOL-0085 -->
**Solución B3.**

Como $f(x)=3x-2$ es estrictamente creciente,

$$
f([1,4))=[f(1),f(4))=[1,10).
$$

Para la preimagen resolvemos

$$
-5<3x-2\le4.
$$

Sumando $2$,

$$
-3<3x\le6,
$$

y dividiendo por $3>0$,

$$
-1<x\le2.
$$

Por tanto,

$$
f^{-1}((-5,4])=(-1,2].
$$
:::

::: {#sol-t1-0086}
<!-- CPM-T1-SOL-0086 -->
**Solución B4.**

Buscamos

$$
4<x^2\le9.
$$

Esto equivale a

$$
2<|x|\le3.
$$

Por tanto,

$$
q^{-1}((4,9])=[-3,-2)\cup(2,3].
$$

Aparecen dos intervalos porque la función cuadrado toma el mismo valor positivo en dos puntos simétricos $x$ y $-x$. La preimagen registra ambas ramas.
:::

::: {#sol-t1-0087}
<!-- CPM-T1-SOL-0087 -->
**Solución B5.**

En $[0,\infty)$ la función $x\mapsto x^2$ es inyectiva. Sin embargo, como el codominio es todo $\mathbb R$, no es sobreyectiva: ningún número negativo pertenece a su imagen.

Si reemplazamos el codominio por $[0,\infty)$, obtenemos

$$
\widetilde r\colon[0,\infty)\to[0,\infty),
\qquad
\widetilde r(x)=x^2.
$$

Esta función es biyectiva. Su inversa asigna a cada $y\ge0$ la única raíz cuadrada no negativa:

$$
\widetilde r^{-1}(y)=\sqrt y.
$$
:::

::: {#sol-t1-0088}
<!-- CPM-T1-SOL-0088 -->
**Solución B6.**

Los valores pedidos son

$$
p(-2)=-1,
\qquad
p(0)=0,
\qquad
p(2)=4.
$$

Para $x<0$, la expresión $x+1$ toma todos los valores de $(-\infty,1)$. Para $x\ge0$, la expresión $x^2$ toma todos los valores de $[0,\infty)$. Por tanto,

$$
\operatorname{Im}(p)
=
(-\infty,1)\cup[0,\infty)
=
\mathbb R.
$$

Así, $p$ es sobreyectiva.

No es inyectiva. Por ejemplo,

$$
p(-1)=0=p(0),
$$

aunque $-1\ne0$.
:::

::: {#sol-t1-0089}
<!-- CPM-T1-SOL-0089 -->
**Solución B7.**

Si $(a,b)\in\Gamma_f$, entonces

$$
b=f(a).
$$

Para obtener un punto de la gráfica de $h$, necesitamos elegir $x$ de modo que

$$
x-3=a,
$$

es decir,

$$
x=a+3.
$$

Entonces

$$
h(a+3)=2f(a)-1=2b-1.
$$

Por tanto,

$$
(a,b)
\longmapsto
(a+3,2b-1).
$$

Geométricamente:

1. $x\mapsto x-3$ desplaza la gráfica $3$ unidades hacia la derecha;
2. multiplicar la salida por $2$ duplica las alturas;
3. restar $1$ desplaza el resultado una unidad hacia abajo.

La transformación se ha deducido de la fórmula, no de una regla memorizada.
:::

#### Soluciones del nivel C

::: {#sol-t1-0090}
<!-- CPM-T1-SOL-0090 -->
**Solución C1.**

Sean $x_1,x_2\in\mathbb R$ y supongamos

$$
f(x_1)=f(x_2).
$$

Entonces

$$
ax_1+b=ax_2+b.
$$

Restando $b$,

$$
ax_1=ax_2.
$$

Como $a\ne0$, podemos dividir por $a$ y obtener

$$
x_1=x_2.
$$

Por definición, $f$ es inyectiva. La hipótesis $a\ne0$ es esencial: si $a=0$, la función sería constante.
:::

::: {#sol-t1-0091}
<!-- CPM-T1-SOL-0091 -->
**Solución C2.**

Para la inyectividad, supongamos

$$
r(x_1)=r(x_2).
$$

Entonces

$$
\frac1{x_1}=\frac1{x_2}.
$$

Como $x_1,x_2>0$, ambos son no nulos y podemos multiplicar por $x_1x_2$, obteniendo

$$
x_2=x_1.
$$

Luego $r$ es inyectiva.

Para la sobreyectividad, tomemos un $y\in(0,\infty)$ arbitrario. Elegimos

$$
x=\frac1y.
$$

Como $y>0$, también $x>0$, y

$$
r(x)=\frac1{1/y}=y.
$$

Así, todo elemento del codominio tiene antecedente. Por tanto, $r$ es biyectiva.

Además, la misma fórmula deshace la asignación:

$$
r^{-1}(y)=\frac1y.
$$

En particular,

$$
r^{-1}=r.
$$
:::

::: {#sol-t1-0092}
<!-- CPM-T1-SOL-0092 -->
**Solución C3.**

Sean $x_1,x_2\ge0$ y supongamos

$$
x_1^2+1=x_2^2+1.
$$

Entonces

$$
x_1^2=x_2^2.
$$

Como ambos números son no negativos, se sigue $x_1=x_2$. Por tanto, $f$ es inyectiva.

Para la sobreyectividad, sea $y\in[1,\infty)$. Entonces

$$
y-1\ge0,
$$

y podemos definir

$$
x=\sqrt{y-1}.
$$

Este $x$ pertenece a $[0,\infty)$ y

$$
f(x)
=
(\sqrt{y-1})^2+1
=
y.
$$

Por tanto, $f$ es sobreyectiva y, en consecuencia, biyectiva.

Ahora sí podemos definir la inversa:

$$
f^{-1}(y)=\sqrt{y-1},
\qquad y\ge1.
$$
:::

::: {#sol-t1-0093}
<!-- CPM-T1-SOL-0093 -->
**Solución C4.**

Tomemos $x_1,x_2\in A$ y supongamos

$$
(g\circ f)(x_1)=(g\circ f)(x_2).
$$

Por definición de composición,

$$
g(f(x_1))=g(f(x_2)).
$$

Como $g$ es inyectiva,

$$
f(x_1)=f(x_2).
$$

Y como $f$ es inyectiva,

$$
x_1=x_2.
$$

Por tanto, $g\circ f$ es inyectiva.

El argumento usa las dos hipótesis en un orden determinado: primero cancelamos $g$ y después cancelamos $f$.
:::

::: {#sol-t1-0094}
<!-- CPM-T1-SOL-0094 -->
**Solución C5.**

Sea $x\in A$. Entonces

$$
\begin{aligned}
x\in f^{-1}(U\cap V)
&\Longleftrightarrow f(x)\in U\cap V\\
&\Longleftrightarrow f(x)\in U\text{ y }f(x)\in V\\
&\Longleftrightarrow x\in f^{-1}(U)\text{ y }x\in f^{-1}(V)\\
&\Longleftrightarrow x\in f^{-1}(U)\cap f^{-1}(V).
\end{aligned}
$$

Como la equivalencia vale para todo $x\in A$,

$$
f^{-1}(U\cap V)=f^{-1}(U)\cap f^{-1}(V).
$$

Para el complemento relativo a $B$,

$$
\begin{aligned}
x\in f^{-1}(B\setminus U)
&\Longleftrightarrow f(x)\in B\setminus U\\
&\Longleftrightarrow f(x)\notin U\\
&\Longleftrightarrow x\notin f^{-1}(U)\\
&\Longleftrightarrow x\in A\setminus f^{-1}(U).
\end{aligned}
$$

Por tanto,

$$
f^{-1}(B\setminus U)=A\setminus f^{-1}(U).
$$

No fue necesario suponer inyectividad ni sobreyectividad.
:::

::: {#sol-t1-0095}
<!-- CPM-T1-SOL-0095 -->
**Solución C6.**

Sean $0\le x<y$. Entonces

$$
y^2-x^2=(y-x)(y+x).
$$

Aquí $y-x>0$ y $y+x>0$, por lo que

$$
y^2-x^2>0.
$$

Así,

$$
x^2<y^2,
$$

y $q$ es estrictamente creciente en $[0,\infty)$.

Ahora sean $x<y\le0$. De nuevo,

$$
y^2-x^2=(y-x)(y+x).
$$

Tenemos $y-x>0$, pero $y+x<0$ porque $x<y\le0$ implica $x<0$ y, por tanto, $x+y<0$. Luego

$$
y^2-x^2<0,
$$

de modo que

$$
y^2<x^2.
$$

Por tanto, $q$ es estrictamente decreciente en $(-\infty,0]$.

Toda función estrictamente monótona es inyectiva. Así, las dos restricciones son inyectivas.
:::

::: {#sol-t1-0096}
<!-- CPM-T1-SOL-0096 -->
**Solución C7.**

La función afín tiene pendiente $2\ne0$, así que es inyectiva. Para cualquier $y\in\mathbb R$, la ecuación

$$
y=2x-3
$$

tiene la solución

$$
x=\frac{y+3}{2},
$$

que es real. Por tanto, $f$ es sobreyectiva y, en consecuencia, biyectiva. Su inversa es

$$
f^{-1}(y)=\frac{y+3}{2}.
$$

Ahora,

$$
(x,y)\in\Gamma_f
$$

significa exactamente

$$
y=f(x).
$$

Como $f$ es biyectiva, esta igualdad equivale a

$$
x=f^{-1}(y),
$$

que a su vez significa

$$
(y,x)\in\Gamma_{f^{-1}}.
$$

Por tanto,

$$
(x,y)\in\Gamma_f
\Longleftrightarrow
(y,x)\in\Gamma_{f^{-1}}.
$$

Intercambiar las coordenadas $(x,y)$ por $(y,x)$ corresponde geométricamente a reflejar respecto de la recta $y=x$. Por eso las gráficas de una función biyectiva y de su inversa son simétricas respecto de esa recta.
:::

#### Soluciones del nivel D

::: {#sol-t1-0097}
<!-- CPM-T1-SOL-0097 -->
**Solución D1.**

Supongamos que $g\circ f$ es inyectiva. Si

$$
f(x_1)=f(x_2),
$$

entonces, aplicando $g$ a ambos lados,

$$
g(f(x_1))=g(f(x_2)),
$$

es decir,

$$
(g\circ f)(x_1)=(g\circ f)(x_2).
$$

Como la composición es inyectiva,

$$
x_1=x_2.
$$

Por tanto, $f$ es inyectiva.

En cambio, $g$ no tiene por qué ser inyectiva fuera de la imagen de $f$. Consideremos

$$
A=\{0,1\},
\quad
B=\{0,1,2\},
\quad
C=\{0,1\},
$$

con

$$
f(0)=0,
\qquad f(1)=1,
$$

y

$$
g(0)=0,
\qquad g(1)=1,
\qquad g(2)=1.
$$

Entonces

$$
(g\circ f)(0)=0,
\qquad
(g\circ f)(1)=1,
$$

así que $g\circ f$ es inyectiva. Sin embargo,

$$
g(1)=g(2)=1
$$

con $1\ne2$, de modo que $g$ no es inyectiva.
:::

::: {#sol-t1-0098}
<!-- CPM-T1-SOL-0098 -->
**Solución D2.**

Sea $c\in C$. Como $g\circ f$ es sobreyectiva, existe $a\in A$ tal que

$$
g(f(a))=c.
$$

Si llamamos

$$
b=f(a)\in B,
$$

entonces $g(b)=c$. Así, todo $c\in C$ tiene antecedente bajo $g$, por lo que $g$ es sobreyectiva.

Pero $f$ no tiene por qué ser sobreyectiva sobre todo $B$. Tomemos

$$
A=\{0,1\},
\quad
B=\{0,1,2\},
\quad
C=\{0,1\},
$$

con

$$
f(0)=0,
\qquad f(1)=1,
$$

y

$$
g(0)=0,
\qquad g(1)=1,
\qquad g(2)=0.
$$

La composición satisface

$$
(g\circ f)(0)=0,
\qquad
(g\circ f)(1)=1,
$$

así que es sobreyectiva sobre $C$. Sin embargo, $2\in B$ no pertenece a la imagen de $f$, de modo que $f$ no es sobreyectiva.
:::

::: {#sol-t1-0099}
<!-- CPM-T1-SOL-0099 -->
**Solución D3.**

Ninguna de las cuatro funciones es igual a otra según la convención del libro. Aunque todas usan la regla $x\mapsto x^2$, al menos el dominio o el codominio difiere en cada par.

La clasificación es:

- $p\colon\mathbb R\to\mathbb R$: no es inyectiva y no es sobreyectiva;
- $q\colon\mathbb R\to[0,\infty)$: es sobreyectiva, pero no inyectiva;
- $r\colon[0,\infty)\to\mathbb R$: es inyectiva, pero no sobreyectiva;
- $s\colon[0,\infty)\to[0,\infty)$: es biyectiva.

Cambiar el **dominio** puede eliminar pares de entradas distintas que producían la misma salida; por eso puede modificar la inyectividad. Cambiar el **codominio** puede hacer que la imagen coincida o deje de coincidir con el conjunto de llegada; por eso puede modificar la sobreyectividad.

La regla puntual puede permanecer idéntica mientras cambian propiedades estructurales de la función.
:::

::: {#sol-t1-0100}
<!-- CPM-T1-SOL-0100 -->
**Solución D4.**

Para

$$
f\colon\mathbb R\to[0,\infty),
\qquad f(x)=x^2,
$$

la función no es inyectiva, pues

$$
f(1)=f(-1)=1.
$$

Por tanto, no puede poseer una función inversa definida sobre todo $[0,\infty)$.

El paso

$$
y=x^2
\quad\Longrightarrow\quad
x=\sqrt y
$$

ha descartado silenciosamente la otra solución

$$
x=-\sqrt y
$$

cuando $y>0$. Resolver la ecuación produce posibles antecedentes; para construir una función inversa necesitamos **exactamente uno** para cada $y$ del codominio.

Podemos reparar la situación restringiendo el dominio a $[0,\infty)$:

$$
f_+\colon[0,\infty)\to[0,\infty),
\qquad f_+(x)=x^2,
$$

con

$$
f_+^{-1}(y)=\sqrt y.
$$

O podemos restringirlo a $(-\infty,0]$:

$$
f_-\colon(-\infty,0]\to[0,\infty),
\qquad f_-(x)=x^2,
$$

con

$$
f_-^{-1}(y)=-\sqrt y.
$$

No hay contradicción entre las dos inversas: $f_+$ y $f_-$ son funciones distintas.
:::

::: {#sol-t1-0101}
<!-- CPM-T1-SOL-0101 -->
**Solución D5.**

Sea $y\in f(E\cap F)$. Entonces existe $x\in E\cap F$ tal que

$$
y=f(x).
$$

Como $x\in E$ y $x\in F$, tenemos

$$
y\in f(E)
\qquad\text{y}\qquad
y\in f(F).
$$

Por tanto,

$$
y\in f(E)\cap f(F),
$$

y queda demostrada la inclusión

$$
f(E\cap F)\subseteq f(E)\cap f(F).
$$

Para la inclusión inversa, si

$$
y\in f(E)\cap f(F),
$$

sabemos que existen $e\in E$ y $r\in F$ tales que

$$
f(e)=y=f(r).
$$

El problema es que no sabemos todavía que $e=r$. Sin esa igualdad no podemos concluir que exista un mismo punto perteneciente a $E\cap F$ que produzca $y$.

La hipótesis suficiente es que $f$ sea inyectiva. Entonces

$$
f(e)=f(r)
\Longrightarrow e=r,
$$

y ese punto común pertenece a $E\cap F$. En consecuencia, bajo inyectividad,

$$
f(E\cap F)=f(E)\cap f(F).
$$
:::

::: {#sol-t1-0102}
<!-- CPM-T1-SOL-0102 -->
**Solución D6.**

En $x=0$ se activan las dos condiciones. La primera rama asigna

$$
0+1=1,
$$

mientras que la segunda asigna

$$
-0=0.
$$

Por tanto, una misma entrada recibe dos salidas diferentes. Falla la unicidad y la regla no define una función.

Una reparación es

$$
h_1(x)=
\begin{cases}
x+1, & x\ge0,\\
-x, & x<0.
\end{cases}
$$

Otra es

$$
h_2(x)=
\begin{cases}
x+1, & x>0,\\
-x, & x\le0.
\end{cases}
$$

Ambas definen funciones porque los tramos cubren $\mathbb R$ sin superponerse.

No son la misma función: en $x=0$,

$$
h_1(0)=1,
\qquad
h_2(0)=0.
$$

Así, reparar una ambigüedad exige tomar una decisión matemática; no hay una única reparación automática.
:::

#### Soluciones del nivel E

::: {#sol-t1-0103}
<!-- CPM-T1-SOL-0103 -->
**Solución E1.**

Un ejemplo es

$$
f\colon\mathbb R\setminus\{0\}\to\mathbb R,
\qquad f(x)=\frac1x,
$$

y

$$
g\colon(0,\infty)\to(0,\infty),
\qquad g(x)=\frac1x.
$$

Utilizan la misma fórmula, pero sus dominios y codominios son distintos. En particular,

$$
-1\in\operatorname{Dom}(f)
$$

mientras que

$$
-1\notin\operatorname{Dom}(g).
$$

Por tanto, $f\ne g$.
:::

::: {#sol-t1-0104}
<!-- CPM-T1-SOL-0104 -->
**Solución E2.**

Para una función inyectiva no sobreyectiva podemos tomar

$$
f\colon\mathbb N\to\mathbb N,
\qquad f(n)=n+1.
$$

Es inyectiva porque

$$
n_1+1=n_2+1
\Longrightarrow n_1=n_2.
$$

No es sobreyectiva porque $0\in\mathbb N$ no pertenece a su imagen.

Para una función sobreyectiva no inyectiva podemos tomar

$$
g\colon\mathbb R\to[0,\infty),
\qquad g(x)=x^2.
$$

Es sobreyectiva porque cada $y\ge0$ es el cuadrado de $\sqrt y$, pero no es inyectiva porque

$$
g(1)=g(-1)=1.
$$
:::

::: {#sol-t1-0105}
<!-- CPM-T1-SOL-0105 -->
**Solución E3.**

Tomemos

$$
f(x)=x+1,
\qquad
g(x)=x^2,
$$

ambas como funciones $\mathbb R\to\mathbb R$.

Entonces

$$
(g\circ f)(x)=(x+1)^2,
$$

mientras que

$$
(f\circ g)(x)=x^2+1.
$$

En $x=1$,

$$
(g\circ f)(1)=4,
\qquad
(f\circ g)(1)=2.
$$

Por tanto,

$$
g\circ f\ne f\circ g.
$$
:::

::: {#sol-t1-0106}
<!-- CPM-T1-SOL-0106 -->
**Solución E4.**

Tomemos

$$
f\colon\mathbb R\to[0,\infty),
\qquad f(x)=x^2,
$$

y

$$
E=\{-1\},
\qquad
F=\{1\}.
$$

Como $E\cap F=\varnothing$,

$$
f(E\cap F)=\varnothing.
$$

Pero

$$
f(E)=\{1\}=f(F),
$$

de modo que

$$
f(E)\cap f(F)=\{1\}.
$$

Por tanto,

$$
f(E\cap F)=\varnothing
\subsetneq
\{1\}=f(E)\cap f(F).
$$

La inclusión puede ser estricta porque $f$ no es inyectiva: los puntos distintos $-1$ y $1$ comparten la misma imagen.
:::

::: {#sol-t1-0107}
<!-- CPM-T1-SOL-0107 -->
**Solución E5.**

Definamos

$$
m(x)=
\begin{cases}
0, & x\le0,\\
x, & x>0.
\end{cases}
$$

La función es no decreciente. En efecto, si $x\le y$:

- si $y\le0$, entonces $m(x)=m(y)=0$;
- si $x\le0<y$, entonces $m(x)=0<y=m(y)$;
- si $0<x\le y$, entonces $m(x)=x\le y=m(y)$.

Sin embargo, no es inyectiva. Por ejemplo,

$$
m(-2)=m(-1)=0
$$

con $-2\ne-1$.

La monotonía **estricta** implica inyectividad; la monotonía no estricta no.
:::

#### Soluciones del nivel F

::: {#sol-t1-0108}
<!-- CPM-T1-SOL-0108 -->
**Solución F1.**

La gráfica de una función contiene exactamente los pares

$$
(x,f(x))
$$

con $x$ en el dominio. Por tanto, las primeras coordenadas de los pares de $\Gamma_f$ reconstruyen

$$
A=\{-2,0,3\}.
$$

Los valores son

$$
f(-2)=1,
\qquad
f(0)=1,
\qquad
f(3)=4.
$$

Así,

$$
\operatorname{Im}(f)=\{1,4\}.
$$

La función no es inyectiva porque

$$
f(-2)=f(0)=1.
$$

Tampoco es sobreyectiva sobre

$$
B=\{1,2,4\},
$$

porque $2$ no es alcanzado.

Si solo conociéramos $\Gamma_f$, podríamos reconstruir dominio y valores, pero no el codominio declarado de manera única. Por ejemplo, la misma gráfica sería compatible con codominio $\{1,4\}$, con $\{1,2,4\}$ o con un conjunto mayor que contuviera la imagen. Bajo la convención del libro, esas declaraciones corresponden a funciones distintas.
:::

::: {#sol-t1-0109}
<!-- CPM-T1-SOL-0109 -->
**Solución F2.**

Sea $x\in A$.

Para la unión,

$$
\begin{aligned}
x\in f^{-1}(U\cup V)
&\Longleftrightarrow f(x)\in U\cup V\\
&\Longleftrightarrow f(x)\in U\text{ o }f(x)\in V\\
&\Longleftrightarrow x\in f^{-1}(U)\text{ o }x\in f^{-1}(V)\\
&\Longleftrightarrow x\in f^{-1}(U)\cup f^{-1}(V).
\end{aligned}
$$

Por tanto,

$$
f^{-1}(U\cup V)=f^{-1}(U)\cup f^{-1}(V).
$$

Para la intersección,

$$
\begin{aligned}
x\in f^{-1}(U\cap V)
&\Longleftrightarrow f(x)\in U\cap V\\
&\Longleftrightarrow f(x)\in U\text{ y }f(x)\in V\\
&\Longleftrightarrow x\in f^{-1}(U)\text{ y }x\in f^{-1}(V)\\
&\Longleftrightarrow x\in f^{-1}(U)\cap f^{-1}(V).
\end{aligned}
$$

Así,

$$
f^{-1}(U\cap V)=f^{-1}(U)\cap f^{-1}(V).
$$

Para el complemento,

$$
\begin{aligned}
x\in f^{-1}(B\setminus U)
&\Longleftrightarrow f(x)\notin U\\
&\Longleftrightarrow x\notin f^{-1}(U)\\
&\Longleftrightarrow x\in A\setminus f^{-1}(U).
\end{aligned}
$$

Por tanto,

$$
f^{-1}(B\setminus U)=A\setminus f^{-1}(U).
$$

Todas las equivalencias dependen solamente de la definición de preimagen y de las operaciones de conjuntos. No fue necesario comparar entradas distintas ni exigir que todos los puntos del codominio se alcancen. Por eso no se requiere inyectividad ni sobreyectividad.
:::

::: {#sol-t1-0110}
<!-- CPM-T1-SOL-0110 -->
**Solución F3.**

La primera elección es

$$
q_+\colon[0,\infty)\to[0,\infty),
\qquad q_+(x)=x^2.
$$

Es inyectiva porque el cuadrado es estrictamente creciente en $[0,\infty)$. Es sobreyectiva porque, dado $y\ge0$, existe la raíz no negativa $\sqrt y$ y

$$
q_+(\sqrt y)=y.
$$

Por tanto, es biyectiva y

$$
q_+^{-1}(y)=\sqrt y.
$$

La segunda elección es

$$
q_-\colon(-\infty,0]\to[0,\infty),
\qquad q_-(x)=x^2.
$$

Es inyectiva porque el cuadrado es estrictamente decreciente en $(-\infty,0]$. Para todo $y\ge0$, el número

$$
-\sqrt y\le0
$$

satisface

$$
q_-(-\sqrt y)=y,
$$

así que $q_-$ es sobreyectiva. Por tanto, es biyectiva y

$$
q_-^{-1}(y)=-\sqrt y.
$$

La misma regla de asignación produce dos biyectividades distintas al cambiar el dominio.
:::

::: {#sol-t1-0111}
<!-- CPM-T1-SOL-0111 -->
**Solución F4.**

Fijemos $y\in B$ y estudiemos

$$
f(x)=y.
$$

La afirmación «para cada $y\in B$ existe al menos un $x\in A$ con $f(x)=y$» es exactamente la definición de **sobreyectividad**.

La afirmación «para cada $y\in B$ existe a lo sumo un $x\in A$ con $f(x)=y$» equivale a **inyectividad**. En efecto, decir que una salida no puede tener dos antecedentes distintos es otra forma de decir

$$
f(x_1)=f(x_2)
\Longrightarrow
x_1=x_2.
$$

Por tanto, para cada $y\in B$ existe **exactamente un** antecedente si y solo si $f$ es simultáneamente sobreyectiva e inyectiva, es decir, biyectiva.

Cuando esto ocurre, definimos

$$
f^{-1}(y)=x,
$$

donde $x$ es el único elemento de $A$ que satisface

$$
f(x)=y.
$$

La sobreyectividad garantiza la existencia de $f^{-1}(y)$; la inyectividad garantiza su unicidad.
:::

::: {#sol-t1-0112}
<!-- CPM-T1-SOL-0112 -->
**Solución F5.**

Tenemos

$$
q(x)=-2(x-3)^2+1.
$$

Con las funciones dadas,

$$
T_{-3}(x)=x-3,
$$

$$
s(T_{-3}(x))=(x-3)^2,
$$

$$
M_{-2}(s(T_{-3}(x)))=-2(x-3)^2,
$$

y finalmente

$$
T_1(M_{-2}(s(T_{-3}(x))))=-2(x-3)^2+1.
$$

Por tanto,

$$
q=T_1\circ M_{-2}\circ s\circ T_{-3}.
$$

Leída desde la entrada hacia la salida, la composición indica:

1. trasladar la gráfica de $s$ tres unidades hacia la derecha;
2. multiplicar las alturas por $-2$, lo que combina reflexión respecto del eje horizontal y dilatación vertical por factor $2$;
3. trasladar una unidad hacia arriba.

El vértice $(0,0)$ de $s$ pasa primero a $(3,0)$ y después a

$$
(3,1).
$$

Ese es el vértice de la parábola descrita por $q$.
:::

#### Soluciones del nivel G

::: {#sol-t1-0113}
<!-- CPM-T1-SOL-0113 -->
**Solución G1.**

Supongamos primero que $f$ es inyectiva. En §2.6 ya sabemos que para cualesquiera $E,F\subseteq A$ siempre se cumple

$$
f(E\cap F)\subseteq f(E)\cap f(F).
$$

Para la inclusión inversa, sea

$$
y\in f(E)\cap f(F).
$$

Entonces existen $e\in E$ y $r\in F$ tales que

$$
f(e)=y=f(r).
$$

Como $f$ es inyectiva,

$$
e=r.
$$

Por tanto, ese mismo punto pertenece a $E\cap F$, y

$$
y\in f(E\cap F).
$$

Así,

$$
f(E\cap F)=f(E)\cap f(F).
$$

Recíprocamente, supongamos que para todos $E,F\subseteq A$ se cumple la igualdad anterior. Queremos recuperar la inyectividad.

Sean $x_1,x_2\in A$ y supongamos

$$
f(x_1)=f(x_2).
$$

Tomemos

$$
E=\{x_1\},
\qquad
F=\{x_2\}.
$$

Si $x_1\ne x_2$, entonces

$$
E\cap F=\varnothing,
$$

de modo que

$$
f(E\cap F)=\varnothing.
$$

Pero, como $f(x_1)=f(x_2)$,

$$
f(E)\cap f(F)
=
\{f(x_1)\}
\ne\varnothing.
$$

Esto contradice la igualdad supuesta para todos $E,F$. Por tanto, necesariamente

$$
x_1=x_2.
$$

Luego $f$ es inyectiva.

Hemos demostrado la equivalencia.
:::

::: {#sol-t1-0114}
<!-- CPM-T1-SOL-0114 -->
**Solución G2.**

Supongamos primero

$$
g\circ f=\operatorname{id}_A.
$$

Para demostrar que $f$ es inyectiva, sean $x_1,x_2\in A$ y supongamos

$$
f(x_1)=f(x_2).
$$

Aplicando $g$,

$$
g(f(x_1))=g(f(x_2)).
$$

Como $g\circ f=\operatorname{id}_A$,

$$
x_1=x_2.
$$

Así, $f$ es inyectiva.

Para demostrar que $g$ es sobreyectiva sobre $A$, tomemos cualquier $a\in A$. El elemento

$$
f(a)\in B
$$

satisface

$$
g(f(a))=a.
$$

Por tanto, cada $a$ tiene antecedente bajo $g$, y $g$ es sobreyectiva.

Ahora supongamos

$$
f\circ g=\operatorname{id}_B.
$$

Para cada $b\in B$, el elemento $g(b)\in A$ satisface

$$
f(g(b))=b,
$$

de modo que $f$ es sobreyectiva.

Para la inyectividad de $g$, si

$$
g(b_1)=g(b_2),
$$

aplicamos $f$ y obtenemos

$$
f(g(b_1))=f(g(b_2)),
$$

de donde

$$
b_1=b_2.
$$

Así, $g$ es inyectiva.

Las conversas generales fallan. Consideremos

$$
A=\{0,1\},
\qquad
B=\{0,1,2\}.
$$

Definamos

$$
f(0)=0,
\qquad f(1)=1,
$$

y

$$
g(0)=0,
\qquad g(1)=0,
\qquad g(2)=1.
$$

Aquí $f$ es inyectiva y $g$ es sobreyectiva sobre $A$, pero

$$
(g\circ f)(1)=g(1)=0\ne1,
$$

por lo que

$$
g\circ f\ne\operatorname{id}_A.
$$

De manera análoga, tomemos

$$
A=\{0,1,2\},
\qquad
B=\{0,1\},
$$

y definamos

$$
f(0)=0,
\qquad f(1)=0,
\qquad f(2)=1,
$$

$$
g(0)=0,
\qquad g(1)=1.
$$

Entonces $f$ es sobreyectiva y $g$ es inyectiva, pero

$$
(f\circ g)(1)=f(1)=0\ne1,
$$

de modo que

$$
f\circ g\ne\operatorname{id}_B.
$$

La existencia de una inversa lateral es, por tanto, una condición más fuerte que la mera combinación de inyectividad y sobreyectividad de funciones distintas.
:::

::: {#sol-t1-0115}
<!-- CPM-T1-SOL-0115 -->
**Solución G3.**

Supongamos que

$$
g\circ f\colon A\to C
$$

es biyectiva.

Como toda función biyectiva es inyectiva, $g\circ f$ es inyectiva. Por el argumento del Ejercicio D1, esto obliga a que $f$ sea inyectiva.

Como toda función biyectiva es sobreyectiva, $g\circ f$ es sobreyectiva. Por el argumento del Ejercicio D2, esto obliga a que $g$ sea sobreyectiva.

Sin embargo, no se sigue en general que $f$ sea sobreyectiva ni que $g$ sea inyectiva. Un solo ejemplo muestra simultáneamente ambas fallas. Tomemos

$$
A=C=\{0\},
\qquad
B=\{0,1\},
$$

con

$$
f(0)=0,
$$

y

$$
g(0)=0,
\qquad g(1)=0.
$$

La composición

$$
g\circ f\colon\{0\}\to\{0\}
$$

es biyectiva. Pero $f$ no es sobreyectiva sobre $B$, porque $1$ no es alcanzado, y $g$ no es inyectiva, porque $g(0)=g(1)$.

Ahora añadamos la hipótesis de que $f$ es sobreyectiva. Ya sabemos que $f$ es inyectiva, así que $f$ es biyectiva. También sabemos que $g$ es sobreyectiva. Falta probar que $g$ es inyectiva.

Sean $b_1,b_2\in B$ y supongamos

$$
g(b_1)=g(b_2).
$$

Como $f$ es sobreyectiva, existen $a_1,a_2\in A$ tales que

$$
f(a_1)=b_1,
\qquad
f(a_2)=b_2.
$$

Entonces

$$
(g\circ f)(a_1)=g(b_1)=g(b_2)=(g\circ f)(a_2).
$$

La composición es inyectiva, de modo que

$$
a_1=a_2,
$$

y por tanto

$$
b_1=f(a_1)=f(a_2)=b_2.
$$

Así, $g$ es inyectiva y, como ya era sobreyectiva, es biyectiva.

Por consiguiente, una hipótesis adicional suficiente es:

$$
\boxed{f\text{ sobreyectiva}.}
$$

Existe una condición dual igualmente suficiente. Supongamos ahora que $g$ es inyectiva. Ya sabemos que $g$ es sobreyectiva, así que $g$ es biyectiva. Falta probar que $f$ es sobreyectiva.

Sea $b\in B$. Entonces $g(b)\in C$. Como $g\circ f$ es sobreyectiva, existe $a\in A$ tal que

$$
g(f(a))=g(b).
$$

Por la inyectividad de $g$,

$$
f(a)=b.
$$

Así, todo $b\in B$ tiene antecedente bajo $f$, por lo que $f$ es sobreyectiva. Como ya sabíamos que $f$ es inyectiva, también $f$ es biyectiva.

Por tanto, otra hipótesis adicional suficiente es:

$$
\boxed{g\text{ inyectiva}.}
$$

El resultado completo puede resumirse así:

$$
\boxed{
\begin{array}{c}
g\circ f\text{ biyectiva}
\Longrightarrow
f\text{ inyectiva y }g\text{ sobreyectiva},\\[4pt]
\text{pero no necesariamente }f,g\text{ biyectivas};\\[4pt]
f\text{ sobreyectiva}\ \text{o}\ g\text{ inyectiva}
\Longrightarrow
f\text{ y }g\text{ biyectivas}.
\end{array}}
$$
:::

### Cierre del capítulo

El recorrido de `T1-C03` comenzó con una advertencia sencilla:

$$
\boxed{\text{una fórmula no es todavía una función}.}
$$

El banco final muestra hasta dónde llega esa advertencia. Para decidir si una función puede invertirse, si una composición tiene sentido, si una igualdad entre imágenes es correcta o si una gráfica representa realmente una función, la manipulación algebraica por sí sola no basta. Hay que controlar dominio, codominio, asignación y las propiedades estructurales que se han demostrado.

Con este lenguaje ya podemos dar el siguiente paso. Una sucesión será, antes que nada, una función cuyo dominio es $\mathbb N$. Esa perspectiva permitirá que las herramientas de este capítulo entren directamente en `T1-C04`, sin introducir todavía ninguna teoría nueva en estas páginas.
