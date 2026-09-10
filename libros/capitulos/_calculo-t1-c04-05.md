## Orden y teorema del sándwich {#sec-t1-c04-05}

Las leyes algebraicas de §4.4 nos permiten transportar límites a través de sumas, productos y cocientes. Pero muchas sucesiones no se controlan mejor mediante una identidad algebraica, sino mediante una **desigualdad**.

A veces no sabemos calcular directamente una sucesión complicada, pero sí podemos compararla con otras más sencillas. En otras ocasiones sabemos que una sucesión queda siempre por debajo de otra y queremos averiguar si esa relación puede invertirse cuando pasamos al límite.

La pregunta de esta sección es, por tanto,

$$
\boxed{
\text{¿qué información de orden que vale en una cola sigue siendo visible en el límite?}
}
$$

La palabra **cola** vuelve a ser decisiva. Como el límite ignora cualquier prefijo finito, no necesitaremos exigir que una desigualdad sea verdadera desde el primer término. Bastará que lo sea eventualmente.

### Una desigualdad eventual no puede invertirse en el límite

Supongamos que

$$
a_n\le b_n
$$

para todos los índices suficientemente grandes y que

$$
a_n\to A,
\qquad
b_n\to B.
$$

¿Podría ocurrir que

$$
A>B?
$$

Si así fuera, existiría una distancia positiva entre ambos límites. La convergencia permitiría entonces obligar a $a_n$ a permanecer muy cerca de $A$ y a $b_n$ muy cerca de $B$. Para tolerancias suficientemente pequeñas, los términos de $a_n$ quedarían necesariamente **por encima** de los de $b_n$, contradiciendo la desigualdad eventual.

La intuición se convierte en la siguiente proposición.

::: {#prp-t1-0022}
**Preservación eventual del orden bajo límites.** Sean $(a_n)$ y $(b_n)$ sucesiones reales tales que

$$
a_n\to A
$$

y

$$
b_n\to B.
$$

Supongamos además que existe un índice $K$ tal que

$$
a_n\le b_n
\qquad
\text{para todo }n\ge K.
$$

Entonces

$$
A\le B.
$$

**Demostración.** Supongamos, buscando una contradicción, que

$$
A>B.
$$

Definamos

$$
d:=A-B>0.
$$

Elegimos la tolerancia

$$
\varepsilon=\frac d3.
$$

Como $a_n\to A$, existe $N_a$ tal que, si $n\ge N_a$, entonces

$$
|a_n-A|<\frac d3.
$$

En particular,

$$
a_n>A-\frac d3.
$$

Como $A=B+d$,

$$
A-\frac d3
=
B+\frac{2d}{3}.
$$

Por tanto, para $n\ge N_a$,

$$
a_n>B+\frac{2d}{3}.
$$

Por otra parte, como $b_n\to B$, existe $N_b$ tal que, si $n\ge N_b$, entonces

$$
|b_n-B|<\frac d3,
$$

y de aquí

$$
b_n<B+\frac d3.
$$

Tomemos ahora

$$
N=\max\{K,N_a,N_b\}.
$$

Para todo $n\ge N$ se cumplen simultáneamente las tres informaciones:

$$
a_n\le b_n,
$$

$$
a_n>B+\frac{2d}{3},
$$

y

$$
b_n<B+\frac d3.
$$

Las dos últimas implican

$$
a_n>b_n,
$$

porque

$$
B+\frac{2d}{3}>B+\frac d3.
$$

Esto contradice $a_n\le b_n$.

Por consiguiente, la suposición $A>B$ es imposible y debe cumplirse

$$
A\le B.
$$
:::

La prueba utiliza una arquitectura ya conocida:

$$
\boxed{
\text{hipótesis eventual}
+
\text{dos controles de convergencia}
\longrightarrow
\text{un único umbral mediante }\max.
}
$$

No importa que la desigualdad falle en los primeros cien, mil o un millón de términos. Si existe una cola en la que

$$
a_n\le b_n,
$$

esa cola basta para impedir que los límites aparezcan en el orden contrario.

### Consecuencias inmediatas

La proposición anterior contiene varias formas útiles como casos particulares.

Si

$$
a_n\ge0
$$

eventualmente y

$$
a_n\to A,
$$

podemos comparar $(a_n)$ con la sucesión constante $0$. Como

$$
0\to0,
$$

obtenemos

$$
A\ge0.
$$

Análogamente, si existe una constante $c\in\mathbb R$ tal que

$$
a_n\le c
$$

eventualmente y $a_n\to A$, entonces

$$
A\le c.
$$

Y si

$$
a_n\ge c
$$

eventualmente, entonces

$$
A\ge c.
$$

Estas versiones permiten transportar al límite cotas que solo empiezan a cumplirse después de cierto índice.

### El orden estricto puede desaparecer

Hay que leer @prp-t1-0022 con precisión. De

$$
a_n<b_n
$$

eventualmente no podemos concluir necesariamente

$$
A<B.
$$

La razón es que dos sucesiones pueden mantener una separación positiva en cada índice y, sin embargo, esa separación hacerse cada vez menor.

El ejemplo más sencillo ya está disponible:

$$
0<\frac1{n+1}
$$

para todo $n\in\mathbb N$.

Sin embargo,

$$
0\to0
$$

y, por §4.2,

$$
\frac1{n+1}\to0.
$$

Por tanto los límites satisfacen

$$
0=0,
$$

no una desigualdad estricta.

Así,

$$
\boxed{
a_n<b_n\text{ eventualmente}
\quad\centernot\Longrightarrow\quad
A<B.
}
$$

Lo que sí preserva el teorema es la versión débil:

$$
a_n<b_n
\quad\Longrightarrow\quad
a_n\le b_n
\quad\Longrightarrow\quad
A\le B.
$$

Para conservar una separación estricta en el límite necesitamos información cuantitativa adicional. Por ejemplo, si existe $\delta>0$ tal que eventualmente

$$
a_n+\delta\le b_n,
$$

entonces, usando §4.4,

$$
a_n+\delta\to A+\delta.
$$

La preservación del orden produce

$$
A+\delta\le B,
$$

y por tanto

$$
A<B.
$$

La diferencia es importante: no basta que cada desigualdad sea estricta; hace falta que exista una **separación positiva uniforme** que no se desvanezca al avanzar por la sucesión.

### Atrapar una sucesión entre dos aproximaciones

La preservación del orden resuelve una pregunta cuando ya sabemos que las dos sucesiones comparadas convergen. Pero a menudo queremos utilizar desigualdades para demostrar precisamente que una tercera sucesión **converge**.

Supongamos que podemos establecer, eventualmente,

$$
a_n\le b_n\le c_n,
$$

y que las sucesiones exteriores convergen al mismo número:

$$
a_n\to L,
\qquad
c_n\to L.
$$

Intuitivamente, si $a_n$ y $c_n$ terminan dentro de cualquier tolerancia alrededor de $L$, entonces $b_n$, atrapada entre ambas, no tiene ningún lugar fuera de ese mismo intervalo al cual escapar.

Esta es la idea del teorema del sándwich.

::: {#prp-t1-0023}
**Teorema del sándwich.** Sean $(a_n)$, $(b_n)$ y $(c_n)$ sucesiones reales. Supongamos que existe un índice $K$ tal que

$$
a_n\le b_n\le c_n
\qquad
\text{para todo }n\ge K.
$$

Si

$$
a_n\to L
$$

y

$$
c_n\to L,
$$

entonces

$$
b_n\to L.
$$

**Demostración.** Sea $\varepsilon>0$.

Como $a_n\to L$, existe $N_a$ tal que

$$
n\ge N_a
\quad\Longrightarrow\quad
|a_n-L|<\varepsilon.
$$

Esto implica

$$
L-\varepsilon<a_n<L+\varepsilon.
$$

Como $c_n\to L$, existe $N_c$ tal que

$$
n\ge N_c
\quad\Longrightarrow\quad
|c_n-L|<\varepsilon,
$$

y por tanto

$$
L-\varepsilon<c_n<L+\varepsilon.
$$

Tomemos

$$
N=\max\{K,N_a,N_c\}.
$$

Si $n\ge N$, entonces

$$
a_n\le b_n\le c_n,
$$

mientras que

$$
L-\varepsilon<a_n
$$

y

$$
c_n<L+\varepsilon.
$$

Encadenando las desigualdades,

$$
L-\varepsilon
<
a_n
\le
b_n
\le
c_n
<
L+\varepsilon.
$$

En particular,

$$
L-\varepsilon<b_n<L+\varepsilon.
$$

Por la caracterización de valor absoluto,

$$
|b_n-L|<\varepsilon.
$$

Como $\varepsilon>0$ era arbitrario, concluimos que

$$
b_n\to L.
$$
:::

Hay un detalle lógico importante en esta prueba. **No** podemos justificar el teorema diciendo simplemente:

> como $a_n\le b_n\le c_n$, pasamos al límite y obtenemos $L\le\lim b_n\le L$.

Esa escritura presupone que $\lim b_n$ ya existe, que es precisamente lo que estamos intentando demostrar.

El teorema del sándwich debe producir simultáneamente dos cosas:

1. la **existencia** del límite de $(b_n)$;
2. la **identificación** de ese límite como $L$.

La prueba $\varepsilon$–$N$ anterior hace ambas tareas sin circularidad.

### Los extremos deben converger al mismo número

La coincidencia de los límites exteriores es esencial.

Por ejemplo, consideremos

$$
a_n=0,
\qquad
c_n=1,
$$

y

$$
b_n=
\frac{1+(-1)^n}{2}.
$$

Para todo $n$,

$$
0\le b_n\le1.
$$

Las sucesiones exteriores convergen:

$$
a_n\to0,
\qquad
c_n\to1.
$$

Pero sus límites son distintos. La sucesión intermedia alterna entre $1$ y $0$, de modo que no converge.

Así, una mera cota

$$
a_n\le b_n\le c_n
$$

no basta. El sándwich funciona porque las dos paredes exteriores **se cierran sobre el mismo número**.

### La forma absoluta: una herramienta especialmente útil

En muchos problemas no resulta natural buscar dos sucesiones exteriores por separado. Es más eficiente controlar directamente la distancia del término al candidato.

Supongamos que

$$
|u_n|\le v_n
$$

eventualmente y que

$$
v_n\to0.
$$

De la desigualdad de valor absoluto obtenemos

$$
-v_n\le u_n\le v_n.
$$

Por el álgebra de límites,

$$
-v_n\to0,
$$

mientras que, por hipótesis,

$$
v_n\to0.
$$

El teorema del sándwich da entonces

$$
u_n\to0.
$$

Podemos registrar esta forma operativa como

$$
\boxed{
|u_n|\le v_n\text{ eventualmente},
\qquad
v_n\to0
\quad\Longrightarrow\quad
u_n\to0.
}
$$

Esta versión será una de las herramientas más reutilizadas del capítulo.

Su lógica es particularmente transparente: si el **tamaño** de $u_n$ está dominado por una cantidad que puede hacerse arbitrariamente pequeña, entonces $u_n$ debe acercarse a cero, aunque cambie de signo, oscile o carezca de monotonía.

### Una oscilación que desaparece por estar dominada

::: {#exm-t1-0036}
**Una sucesión oscilante controlada por sándwich.** Consideremos

$$
a_n=\frac{\sin n}{n+1},
\qquad
n\in\mathbb N.
$$

Los valores de $\sin n$ oscilan y no necesitamos describir su comportamiento con mayor precisión. Basta la desigualdad elemental

$$
|\sin n|\le1.
$$

Por tanto,

$$
\left|\frac{\sin n}{n+1}\right|
=
\frac{|\sin n|}{n+1}
\le
\frac1{n+1}.
$$

Ya sabemos que

$$
\frac1{n+1}\to0.
$$

Aplicando la forma absoluta del teorema del sándwich,

$$
\boxed{
\frac{\sin n}{n+1}\to0.
}
$$

Equivalentemente, podríamos escribir

$$
-\frac1{n+1}
\le
\frac{\sin n}{n+1}
\le
\frac1{n+1},
$$

y observar que las dos sucesiones exteriores convergen a $0$.
:::

Este ejemplo muestra por qué el sándwich es más que una regla para «calcular límites». Permite ignorar una parte complicada de una sucesión cuando esa parte está uniformemente controlada.

Aquí no necesitamos averiguar si

$$
\sin n
$$

se acerca a algún número. Ni siquiera necesitamos que converja. Lo único relevante es que su tamaño nunca excede $1$, mientras que el factor

$$
\frac1{n+1}
$$

se hace arbitrariamente pequeño.

El patrón general es

$$
\boxed{
\text{oscilación acotada}
\times
\text{factor que tiende a }0
\longrightarrow
\text{producto que tiende a }0,
}
$$

siempre que podamos justificar la estimación correspondiente.

### Cómo buscar un sándwich

En la práctica, rara vez nos entregan las tres sucesiones ya preparadas. La parte creativa consiste en **fabricar** buenas cotas.

Una estrategia especialmente eficaz para demostrar

$$
a_n\to L
$$

es comenzar por el error

$$
|a_n-L|.
$$

Si podemos encontrar una sucesión sencilla $(r_n)$ tal que

$$
|a_n-L|\le r_n
$$

eventualmente y

$$
r_n\to0,
$$

la forma absoluta del sándwich termina la prueba.

El trabajo se desplaza entonces desde

> calcular exactamente $a_n$

hacia

> encontrar una estimación suficientemente buena del error.

Este cambio de perspectiva es central en análisis. Una cota puede contener menos información que una fórmula exacta y, sin embargo, ser exactamente la información necesaria para demostrar convergencia.

### Tres errores que conviene evitar

**1. Una sola cota no determina un límite.**

De

$$
a_n\le b_n
$$

y

$$
a_n\to L
$$

no se sigue que $b_n\to L$.

Por ejemplo,

$$
0\le1
$$

para todos los índices, pero las sucesiones constantes $0$ y $1$ tienen límites distintos.

**2. Estar entre dos sucesiones convergentes no basta si sus límites son distintos.**

El ejemplo

$$
0\le\frac{1+(-1)^n}{2}\le1
$$

muestra que una sucesión intermedia puede divergir cuando las cotas exteriores convergen a números diferentes.

**3. La desigualdad estricta no tiene por qué permanecer estricta.**

Aunque

$$
0<\frac1{n+1}
$$

para todo $n$, ambos lados convergen a $0$.

Las tres advertencias comparten una misma lección: al trabajar con orden no basta mirar el símbolo de desigualdad; hay que auditar **qué límites poseen las sucesiones comparadas y qué separación cuantitativa conservan**.

### Qué hemos ganado

A la estructura algebraica de §4.4 añadimos ahora una estructura de orden.

Sabemos que:

$$
a_n\le b_n\text{ eventualmente},
\qquad
a_n\to A,
\qquad
b_n\to B
\quad\Longrightarrow\quad
A\le B;
$$

y que

$$
a_n\le b_n\le c_n\text{ eventualmente},
\qquad
a_n,c_n\to L
\quad\Longrightarrow\quad
b_n\to L.
$$

Además, disponemos de la forma especialmente útil

$$
|u_n|\le v_n\text{ eventualmente},
\qquad
v_n\to0
\quad\Longrightarrow\quad
u_n\to0.
$$

Con estas herramientas podemos pasar de la definición y las leyes generales a un pequeño repertorio de límites fundamentales. En §4.6 utilizaremos el sándwich junto con desigualdades elementales e inducción para demostrar, entre otros resultados, que las potencias recíprocas tienden a cero y que

$$
q^n\to0
$$

cuando

$$
|q|<1.
$$

