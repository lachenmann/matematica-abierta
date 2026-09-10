## Laboratorio de completitud {#sec-t1-c02-10}

Hasta aquí hemos estudiado las herramientas del capítulo una por una. Sabemos trabajar con valor absoluto, cotas, supremos e ínfimos; conocemos el axioma de completitud y varias de sus consecuencias; podemos producir escalas pequeñas mediante la propiedad arquimediana, insertar racionales e irracionales por densidad y justificar la existencia de puntos comunes mediante intervalos encajados.

Ahora cambia la tarea.

En los problemas que siguen **no se anunciará de antemano qué herramienta debe utilizarse**. La primera parte de cada solución será, precisamente, diagnosticar la estructura del problema.

Conviene adoptar este protocolo:

$$
\boxed{
\text{leer el objetivo}
\to
\text{identificar la forma de existencia o estimación}
\to
\text{localizar la herramienta}
\to
\text{probar}
\to
\text{auditar dónde entró la completitud}
}
$$

La última pregunta es importante. No todo lo que hacemos en este capítulo utiliza directamente el axioma del supremo. Algunas herramientas dependen de él de manera indirecta y otras, como las propiedades elementales del valor absoluto, proceden solamente de la estructura de cuerpo ordenado.

### Laboratorio 1 — Una frontera que existe pero no se alcanza

Consideremos

$$
A=\{x\in\mathbb R:x\ge0,\ x^2<5\}.
$$

**Problema.** Determinar $\sup A$ y decidir si $A$ tiene máximo.

#### Diagnóstico

El enunciado contiene dos preguntas diferentes.

1. **Frontera:** necesitamos identificar la menor cota superior.
2. **Extremo alcanzado:** debemos decidir si esa frontera pertenece a $A$.

El teorema de raíces de §2.6 nos proporciona ya el número real $\sqrt5$. La pregunta es si ese número desempeña exactamente el papel de supremo.

#### Solución

Primero probemos que $\sqrt5$ es cota superior de $A$.

Si $x\in A$, entonces

$$
0\le x
$$

y

$$
x^2<5=(\sqrt5)^2.
$$

Como el cuadrado es creciente sobre los reales no negativos,

$$
x<\sqrt5.
$$

Por tanto, $\sqrt5$ es cota superior.

Falta demostrar que es la **menor**. Utilicemos la caracterización aproximativa del supremo. Sea $\varepsilon>0$ y definamos

$$
\delta=
\min\left\{\frac{\varepsilon}{2},\frac{\sqrt5}{2}\right\}>0,
\qquad
u=\sqrt5-\delta.
$$

Como $\delta\le\sqrt5/2$, tenemos $u>0$. Además,

$$
u<\sqrt5,
$$

por lo que

$$
u^2<5.
$$

Así, $u\in A$. Y como $\delta\le\varepsilon/2<\varepsilon$,

$$
\sqrt5-\varepsilon<u<\sqrt5.
$$

Hemos encontrado un elemento de $A$ dentro de toda franja positiva situada inmediatamente debajo de $\sqrt5$. En consecuencia,

$$
\boxed{\sup A=\sqrt5.}
$$

¿Hay máximo? No. En efecto, si $x\in A$, entonces $x<\sqrt5$. El punto medio

$$
y=\frac{x+\sqrt5}{2}
$$

satisface

$$
x<y<\sqrt5.
$$

Como $y\ge0$, se sigue que $y^2<5$, de modo que $y\in A$ y $y>x$.

Por tanto, ningún elemento de $A$ puede ser el mayor:

$$
\boxed{A\text{ no tiene máximo}.}
$$

#### Lectura de la solución

El problema obliga a separar nuevamente

$$
\boxed{\text{supremo}\neq\text{máximo}.}
$$

La frontera existe y está perfectamente determinada, pero queda fuera del conjunto porque la condición que define $A$ es estricta: $x^2<5$.

La completitud no aparece escrita en la última línea de la prueba. Está **aguas arriba**: fue la propiedad que permitió demostrar en §2.6 la existencia de $\sqrt5$.

### Laboratorio 2 — Una sola elección para dos exigencias

Sean $M>0$ y $\varepsilon>0$.

**Problema.** Demostrar que existe $n\in\mathbb N_{>0}$ tal que simultáneamente

$$
n>M
$$

y

$$
\frac1n<\varepsilon.
$$

#### Diagnóstico

Tenemos dos condiciones sobre el mismo natural $n$. No conviene elegir un natural para cada una y esperar que coincidan. Debemos convertir ambas exigencias en una única condición suficiente.

La segunda desigualdad queda garantizada si

$$
n>\frac1\varepsilon.
$$

Así que basta fabricar un natural mayor que **dos números reales a la vez**.

#### Solución

Sea

$$
R=\max\left\{M,\frac1\varepsilon\right\}.
$$

Por la propiedad arquimediana existe $n\in\mathbb N$ con

$$
n>R.
$$

Entonces, en particular,

$$
n>M
$$

y

$$
n>\frac1\varepsilon.
$$

Como $n>0$ y $\varepsilon>0$, la segunda desigualdad implica

$$
\frac1n<\varepsilon.
$$

Por tanto,

$$
\boxed{
\exists n\in\mathbb N_{>0}
\quad
n>M
\quad\text{y}\quad
\frac1n<\varepsilon.
}
$$

#### Por qué importa

Este pequeño argumento contiene un patrón que aparecerá constantemente en análisis:

$$
\boxed{
\text{varias restricciones}
\to
\text{una cota común mediante }\max
\to
\text{una sola elección que satisface todas}
}
$$

La propiedad arquimediana, a su vez, fue deducida de completitud en §2.7.

### Laboratorio 3 — Aproximar desde lados distintos y con naturalezas distintas

Sea $x\in\mathbb R$ y sea $\varepsilon>0$.

**Problema.** Encontrar un racional $q$ y un irracional $\xi$ tales que

$$
x-\varepsilon<q<x<\xi<x+\varepsilon.
$$

#### Diagnóstico

La desigualdad separa el problema en dos intervalos abiertos no vacíos:

$$
(x-\varepsilon,x)
\qquad\text{y}\qquad
(x,x+\varepsilon).
$$

La palabra clave es **insertar**. Eso apunta directamente a densidad.

#### Solución

Por la densidad de $\mathbb Q$ existe

$$
q\in\mathbb Q
$$

tal que

$$
x-\varepsilon<q<x.
$$

Por la densidad de los irracionales existe

$$
\xi\in\mathbb R\setminus\mathbb Q
$$

tal que

$$
x<\xi<x+\varepsilon.
$$

Por tanto,

$$
\boxed{x-\varepsilon<q<x<\xi<x+\varepsilon.}
$$

En lenguaje de distancia,

$$
0<|q-x|<\varepsilon,
\qquad
0<|\xi-x|<\varepsilon.
$$

El mismo punto $x$, por tanto, puede aproximarse arbitrariamente por números de **dos naturalezas aritméticas distintas** y además podemos prescribir de qué lado deben encontrarse.

### Laboratorio 4 — Perturbar un punto sin abandonar un intervalo

Supongamos

$$
|x-a|<r,
\qquad r>0,
$$

y sea $\eta>0$.

**Problema.** Demostrar que existen un racional $q$ y un irracional $\xi$ distintos de $x$ tales que

$$
|q-x|<\eta,
\qquad
|\xi-x|<\eta,
$$

y, al mismo tiempo,

$$
|q-a|<r,
\qquad
|\xi-a|<r.
$$

#### Diagnóstico

Sabemos que $x$ está dentro del intervalo centrado en $a$ y radio $r$. Antes de usar densidad debemos averiguar **cuánto margen queda hasta la frontera**.

Ese margen es

$$
r-|x-a|>0.
$$

Queremos movernos menos que ese margen y menos que la tolerancia $\eta$.

#### Solución

Definamos

$$
\delta=
\frac12
\min\{\eta,\ r-|x-a|\}>0.
$$

Por densidad racional podemos elegir

$$
q\in\mathbb Q\cap(x,x+\delta).
$$

Así, $q\ne x$ y

$$
|q-x|<\delta<\eta.
$$

Además, por desigualdad triangular,

$$
|q-a|
\le
|q-x|+|x-a|
<
\delta+|x-a|.
$$

Como

$$
\delta<r-|x-a|,
$$

obtenemos

$$
|q-a|<r.
$$

De manera análoga, por densidad de los irracionales podemos elegir

$$
\xi\in(\mathbb R\setminus\mathbb Q)\cap(x-\delta,x).
$$

Entonces $\xi\ne x$,

$$
|\xi-x|<\eta
$$

y

$$
|\xi-a|<r.
$$

Por tanto, podemos perturbarnos alrededor de $x$ por cantidades arbitrariamente pequeñas, usando racionales o irracionales, **sin salir del intervalo inicial**.

#### Qué técnicas se combinaron

Aquí no bastaba con decir «los racionales son densos». La estructura completa fue

$$
\boxed{
\text{valor absoluto}
\to
\text{margen hasta la frontera}
\to
\text{densidad}
\to
\text{desigualdad triangular}
}
$$

Este tipo de control local será esencial cuando estudiemos límites y continuidad.

### Laboratorio 5 — Bisección con certificado exacto de error

Sabemos por §2.6 que $\sqrt5$ existe y que

$$
2<\sqrt5<3.
$$

**Problema.** Aplicar cuatro pasos de bisección a $[2,3]$ para producir un intervalo racional de longitud $1/16$ que contenga a $\sqrt5$.

#### Diagnóstico

No necesitamos aproximaciones decimales. En cada punto medio basta comparar su cuadrado con $5$.

#### Solución

Partimos de

$$
I_0=[2,3].
$$

El primer punto medio es

$$
\frac52,
$$

y

$$
\left(\frac52\right)^2=\frac{25}{4}>5.
$$

Por tanto,

$$
I_1=\left[2,\frac52\right].
$$

El segundo punto medio es

$$
\frac94,
$$

y

$$
\left(\frac94\right)^2=\frac{81}{16}>5,
$$

de modo que

$$
I_2=\left[2,\frac94\right].
$$

El tercer punto medio es

$$
\frac{17}{8},
$$

y

$$
\left(\frac{17}{8}\right)^2=
\frac{289}{64}<5.
$$

Así,

$$
I_3=\left[\frac{17}{8},\frac94\right].
$$

El cuarto punto medio es

$$
\frac{35}{16},
$$

y

$$
\left(\frac{35}{16}\right)^2
=
\frac{1225}{256}<5.
$$

En consecuencia,

$$
I_4=\left[\frac{35}{16},\frac94\right].
$$

Su longitud es exactamente

$$
\frac94-\frac{35}{16}
=
\frac{36-35}{16}
=
\frac1{16}.
$$

Hemos obtenido el certificado

$$
\boxed{
\frac{35}{16}<\sqrt5<\frac94
}
$$

con un intervalo de incertidumbre de longitud $1/16$.

Si continuáramos el procedimiento indefinidamente, §2.9 garantiza que la cadena de intervalos cerrados tendría un único punto común, precisamente $\sqrt5$.

No hemos necesitado todavía hablar de una sucesión que converge.

### Laboratorio 6 — Auditoría de hipótesis

Decidamos cuáles de las siguientes afirmaciones son verdaderas y, sobre todo, **qué resultado del capítulo las justifica o qué contraejemplo las destruye**.

#### Afirmación A

> Todo subconjunto no vacío de $\mathbb R$ acotado superiormente tiene supremo real.

**Verdadera.** Es exactamente el axioma de completitud adoptado en §2.5.

#### Afirmación B

> Todo subconjunto no vacío de $\mathbb Q$ acotado superiormente tiene supremo racional.

**Falsa.** El conjunto

$$
S_{\mathbb Q}
=
\{q\in\mathbb Q:q\ge0,\ q^2<2\}
$$

es no vacío y está acotado superiormente en $\mathbb Q$, pero §2.5 demostró que no posee supremo racional.

#### Afirmación C

> Toda familia encajada de intervalos abiertos y acotados tiene intersección no vacía.

**Falsa.** Ya conocemos

$$
\left(0,\frac1{n+1}\right),
$$

cuya intersección es vacía.

#### Afirmación D

> Toda familia encajada de intervalos cerrados y acotados de $\mathbb R$ tiene intersección no vacía.

**Verdadera.** Es el principio de intervalos encajados de §2.9.

#### Afirmación E

> Si $|x-a|<r$ y
> $$
> |y-x|<r-|x-a|,
> $$
> entonces $|y-a|<r$.

**Verdadera.** Por desigualdad triangular,

$$
|y-a|
\le
|y-x|+|x-a|
<r.
$$

Aquí no necesitamos invocar completitud: basta la estructura de valor absoluto obtenida del cuerpo ordenado.

#### Afirmación F

> Todo intervalo abierto no vacío de $\mathbb R$ contiene un racional y un irracional.

**Verdadera.** Es precisamente la densidad demostrada en §2.8.

### Dónde está realmente la completitud

El laboratorio permite ahora ordenar las dependencias sin mezclar niveles.

No todo parte directamente del axioma del supremo. La arquitectura es más precisa:

$$
\boxed{
\text{cuerpo + orden}
\Longrightarrow
\text{intervalos, valor absoluto y desigualdades}
}
$$

mientras que

$$
\boxed{
\text{completitud}
\Longrightarrow
\text{supremos generales, raíces, arquimedianidad e intervalos encajados}
}
$$

y después

$$
\boxed{
\text{arquimedianidad}
\Longrightarrow
\text{densidad racional}
\Longrightarrow
\text{densidad irracional}
}
$$

usando en el último paso la existencia de un irracional fijo, como $\sqrt2$.

Esta distinción es importante. Una demostración rigurosa no solo debe saber **qué teorema** utiliza; debe saber también **de qué hipótesis estructurales depende ese teorema**.

### Un mapa de decisiones antes del banco final

Cuando aparezca un problema de este capítulo, estas preguntas ayudan a elegir estrategia.

- ¿Se pide una frontera de un conjunto? Busquemos cotas y pensemos en $\sup$ o $\inf$.
- ¿Hay que garantizar que esa frontera existe? Revisemos las hipótesis de completitud.
- ¿Aparece una tolerancia positiva y necesitamos algo muy grande o muy pequeño? Pensemos en la propiedad arquimediana.
- ¿Hay que insertar un número en un intervalo? Pensemos en densidad.
- ¿Tenemos una familia de aproximaciones por intervalos cerrados cada vez más estrechos? Pensemos en intervalos encajados y bisección.
- ¿Aparece $|x-a|$? Traduzcamos entre distancia, intervalo y desigualdad antes de manipular símbolos.
- ¿Se elimina una hipótesis de un teorema? Antes de intentar demostrar la nueva afirmación, busquemos un contraejemplo.

No se trata de convertir estas preguntas en una tabla mecánica. Su función es ayudar a reconocer la **forma matemática** de un problema.

### Antes de seguir

::: {.callout-tip title="Antes de seguir"}
**1.** En el Laboratorio 1, ¿dónde interviene la completitud si la prueba final solo menciona $\sqrt5$?

**Respuesta.** Interviene en la dependencia del objeto: la existencia de $\sqrt5$ fue demostrada en §2.6 mediante completitud. Una prueba puede depender de un axioma aunque no lo invoque nuevamente de forma explícita.
:::

::: {.callout-tip title="Antes de seguir"}
**2.** En el Laboratorio 4, ¿por qué no basta escoger $\delta=\eta$?

**Respuesta.** Porque $\eta$ controla cercanía a $x$, pero no garantiza que la perturbación permanezca dentro de $|y-a|<r$. También debemos respetar el margen $r-|x-a|$ hasta la frontera.
:::

::: {.callout-tip title="Antes de seguir"}
**3.** En la bisección, ¿qué produce existencia y qué produce unicidad?

**Respuesta.** La existencia del punto común proviene del principio de intervalos encajados, y por tanto de completitud. La unicidad aparece cuando las longitudes pueden hacerse menores que cualquier distancia positiva entre dos supuestos puntos distintos.
:::

::: {.callout-tip title="Antes de seguir"}
**4.** ¿La densidad de $\mathbb Q$ es equivalente a la completitud de $\mathbb R$?

**Respuesta.** No. La densidad es una consecuencia mucho más débil. De hecho, $\mathbb Q$ es denso y, sin embargo, no es completo.
:::

### Lo que queda antes de cerrar el capítulo

Ya no falta teoría conceptual nueva en `T1-C02`. La última sección será el banco completo de ejercicios y soluciones.

Allí tendremos que utilizar de manera autónoma todo el repertorio:

$$
\boxed{
\text{axiomas de cuerpo y álgebra derivada}
+
\text{orden}
+
|\cdot|
+
\sup/\inf
+
\text{completitud}
+
\text{arquimedianidad}
+
\text{densidad}
+
\text{bisección}
}
$$

Además, el banco contendrá las inecuaciones racionales con valor absoluto de alta complejidad ya comprometidas, con control explícito de dominio, puntos críticos, signos, extremos y recomposición final de soluciones.

En §2.11 desaparecerá buena parte del andamiaje guiado: el lector deberá decidir por sí mismo qué herramientas utilizar y justificar cada paso.
