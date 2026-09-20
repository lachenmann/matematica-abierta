---
title: "La derivada y la aproximación lineal local"
description: "Capítulo 6 de Cálculo para matemáticos. Edición canónica v11."
content-id: MA-BCH-0064
content-type: book-chapter
collection: PM-CAL
book-id: MA-BOK-0001
status: published
areas:
  - calculo
  - analisis
level: fundamental
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
date-created: 2026-09-19
date-modified: 2026-09-19
prerequisites: 
  - MA-BCH-0003
  - MA-BCH-0004
  - MA-BCH-0010
  - MA-BCH-0062
  - MA-BCH-0063
number-sections: true
number-depth: 2
number-offset: [5]
---

# La derivada y la aproximación lineal local {#sec-t1-c07}

En los capítulos anteriores hemos aprendido a describir cada vez con mayor precisión el comportamiento de una función cerca de un punto. Primero construimos el lenguaje del límite; después exigimos que ese comportamiento alrededor del punto fuese compatible con el valor tomado en el centro y obtuvimos la continuidad.

Si $a$ es un punto de acumulación del dominio y $f$ es continua en $a$, sabemos que

$$
f(a+h)\longrightarrow f(a)
\qquad\text{cuando}\qquad
h\longrightarrow0,
$$

con $h$ restringido a incrementos no nulos para los que $a+h$ pertenece al dominio.

Pero esta información deja abierta una pregunta más fina. Dos funciones pueden ser continuas en el mismo punto y, sin embargo, cambiar allí de maneras muy diferentes. Cerca de $0$, por ejemplo,

$$
x,
\qquad
x^2,
\qquad
|x|
$$

se aproximan todas a $0$ cuando $x\to0$, pero no lo hacen con la misma geometría ni con la misma escala de variación.

La continuidad responde a una pregunta del tipo

$$
\boxed{
\text{¿se hace pequeña la variación de la función cuando se hace pequeño el incremento?}
}
$$

El cálculo diferencial comienza cuando refinamos la pregunta:

$$
\boxed{
\text{¿cuál es la parte principal de esa variación cuando observamos la función a escala muy pequeña?}
}
$$

La respuesta conducirá a la derivada, pero conviene no apresurarse a introducir el símbolo $f'(a)$. Antes necesitamos descubrir qué cantidad debe aproximarse, por qué aparece un cociente y qué problema resuelve tomar un límite.

El recorrido de este capítulo será

$$
\boxed{
\text{secante}
\to
\text{cociente incremental}
\to
\text{límite}
\to
\text{derivada}
\to
\text{tangente}
\to
\text{aproximación afín local}
\to
\text{error pequeño frente al incremento}.
}
$$

La derivada aparecerá así con dos lecturas inseparables. Por un lado, medirá una **tasa instantánea de cambio**. Por otro, identificará la **parte lineal de primer orden** que modela localmente a una función. La primera lectura nos llevará desde velocidades medias y pendientes de secantes; la segunda será desarrollada más adelante en el capítulo.

Comenzaremos por la pregunta más elemental: ¿cómo puede una razón de cambio calculada entre **dos** puntos contener información acerca del comportamiento de una función en **un solo** punto?

## De la secante a la tasa instantánea {#sec-t1-c07-01}

### Medir un cambio exige comparar dos estados

Supongamos que una cantidad $y$ depende de una variable $x$ mediante

$$
y=f(x).
$$

Si queremos describir cuánto ha cambiado $y$, necesitamos comparar dos valores de la variable. Tomemos un punto de referencia $a$ y un incremento $h$ tal que $a+h$ también pertenezca al dominio. Así obtenemos otro punto cercano $a+h$.

El número

$$
h=(a+h)-a
$$

mide el **incremento de la variable de entrada**. El correspondiente cambio en la salida es

$$
f(a+h)-f(a).
$$

Conviene leer estas dos cantidades en paralelo:

$$
\begin{aligned}
\text{incremento de entrada} &:& h,\\
\text{variación de salida} &:& f(a+h)-f(a).
\end{aligned}
$$

Si $h>0$, el segundo punto está a la derecha de $a$; si $h<0$, está a la izquierda. En ambos casos, mientras $h\ne0$, tenemos dos entradas distintas y podemos comparar los cambios.

Una diferencia aislada como

$$
f(a+h)-f(a)
$$

no dice todavía cuán rápido está cambiando la función. Una variación de $10$ unidades puede ser enorme si ocurrió durante un incremento de entrada de $0.001$, pero muy pequeña si ocurrió durante un incremento de $10^6$.

Para medir una **razón de cambio** debemos comparar la variación de salida con el tamaño orientado del incremento de entrada. Esto conduce al cociente

$$
\frac{f(a+h)-f(a)}{h},
\qquad h\ne0.
$$

Este será el objeto central de la sección.

::: {.callout-note title="Lectura de la fórmula"}
En

$$
\frac{f(a+h)-f(a)}{h},
$$

el numerador mide cuánto cambió la salida y el denominador mide cuánto cambió la entrada. El cociente pregunta:

> ¿cuántas unidades de salida cambian, en promedio, por cada unidad de entrada durante este desplazamiento?

La palabra **promedio** es importante. Todavía estamos comparando dos puntos distintos.
:::

### La misma razón de cambio tiene una lectura geométrica

Consideremos la gráfica de $f$ y los puntos

$$
P=(a,f(a))
$$

y

$$
Q_h=(a+h,f(a+h)),
\qquad h\ne0.
$$

Como $P$ y $Q_h$ son distintos, determinan una única recta. Esa recta es una **secante** a la gráfica en los dos puntos considerados.

Su pendiente es

$$
\frac{f(a+h)-f(a)}{(a+h)-a}
=
\frac{f(a+h)-f(a)}{h}.
$$

Así, el cociente anterior no es una construcción arbitraria. Es exactamente la pendiente de la recta que une los dos puntos de la gráfica.

Si escribimos

$$
Q_a(h):=\frac{f(a+h)-f(a)}{h},
\qquad h\ne0,
$$

solo estamos dando un nombre temporal a esa pendiente secante. No estamos definiendo todavía la derivada.

La secante que pasa por $P$ y $Q_h$ puede escribirse como

$$
S_h(x)=f(a)+Q_a(h)(x-a).
$$

Todas estas rectas pasan por el mismo punto $P$. Lo único que cambia con $h$ es su pendiente.

Esto sugiere una estrategia geométrica. Si hacemos que $Q_h$ se acerque a $P$, es decir, si hacemos

$$
h\to0,
$$

podemos observar qué ocurre con las pendientes de las secantes.

No necesitamos hablar de un misterioso «límite de rectas». Ya sabemos estudiar límites de números. Basta preguntar si los números

$$
Q_a(h)
$$

se aproximan a algún valor cuando $h$ se aproxima a $0$.

::: {.callout-note title="Antes de seguir"}
Imagina que para incrementos cada vez menores las pendientes de las secantes son

$$
1.9,
\quad
1.99,
\quad
1.999,
\quad
2.001,
\quad
2.01.
$$

¿Qué número parece estar emergiendo? ¿Qué parte de nuestra teoría previa permite sustituir esta impresión visual por una afirmación matemática rigurosa?

La respuesta a la segunda pregunta es: **la teoría de límites**.
:::

### Un primer laboratorio: la parábola

Veamos el mecanismo en una función suficientemente sencilla para que toda la estructura quede visible.

::: {#exm-t1-0062}
**Secantes de $f(x)=x^2$ y estabilización de sus pendientes.** Fijemos un punto $a\in\mathbb R$ y consideremos

$$
f(x)=x^2.
$$

Para $h\ne0$, la pendiente de la secante que une

$$
(a,a^2)
$$

con

$$
(a+h,(a+h)^2)
$$

es

$$
\frac{(a+h)^2-a^2}{h}.
$$

Desarrollando el numerador,

$$
(a+h)^2-a^2
=
a^2+2ah+h^2-a^2
=
2ah+h^2.
$$

Como estamos trabajando con $h\ne0$, podemos factorizar y cancelar $h$:

$$
\frac{2ah+h^2}{h}
=
\frac{h(2a+h)}{h}
=
2a+h.
$$

Por tanto, cada incremento no nulo produce una pendiente secante

$$
Q_a(h)=2a+h.
$$

Ahora el comportamiento cuando $h$ se hace pequeño es transparente:

$$
2a+h\longrightarrow2a
\qquad(h\to0).
$$

Tomemos, por ejemplo, $a=1$. Entonces

$$
Q_1(h)=2+h.
$$

Algunos valores son:

| $h$ | $Q_1(h)$ |
|---:|---:|
| $1$ | $3$ |
| $0.1$ | $2.1$ |
| $0.01$ | $2.01$ |
| $0.001$ | $2.001$ |
| $-0.001$ | $1.999$ |
| $-0.01$ | $1.99$ |
| $-0.1$ | $1.9$ |

Las pendientes obtenidas desde la derecha y desde la izquierda se concentran alrededor de $2$.

La observación importante no es la tabla finita. La igualdad exacta

$$
Q_1(h)=2+h
$$

permite usar la teoría de límites y concluir rigurosamente que

$$
\lim_{h\to0}Q_1(h)=2.
$$

Más generalmente,

$$
\lim_{h\to0}Q_a(h)=2a.
$$

Todavía no hemos dado un nombre formal a este límite. Por ahora solo hemos descubierto que, en la parábola, las pendientes de las secantes poseen una pendiente límite bien determinada alrededor de cada punto.
:::

El ejemplo contiene varias ideas que conviene separar.

Primero, el cociente

$$
\frac{f(a+h)-f(a)}{h}
$$

solo está definido para $h\ne0$. La cancelación anterior fue legítima precisamente porque trabajábamos en un entorno **perforado** de $0$.

Segundo, después de cancelar obtenemos una expresión que sí tiene un comportamiento sencillo cuando $h\to0$. El límite no exige sustituir $h=0$ en la expresión original.

Tercero, no bastó observar que las secantes «parecen estabilizarse». La teoría de límites transformó esa intuición en una afirmación exacta.

::: {.callout-warning title="Error frecuente: poner $h=0$ demasiado pronto"}
El cociente incremental de la parábola en $a$ es inicialmente

$$
\frac{(a+h)^2-a^2}{h}.
$$

Si sustituimos $h=0$, obtenemos

$$
\frac00,
$$

que no es un número real.

Esto **no** significa que el proceso haya fracasado. Significa que estamos ante un problema de límite. Para $h\ne0$ simplificamos el cociente a $2a+h$ y después estudiamos qué ocurre cuando $h$ **se aproxima** a $0$.

El límite analiza valores arbitrariamente próximos al centro; no necesita evaluar la expresión en el centro.
:::

### Cambiar de escala sin perder la información principal

La variable $h$ cumple aquí un papel semejante al radio $\delta$ de nuestros capítulos de límites y continuidad: controla la escala con la que observamos la función alrededor de $a$.

Si $|h|$ es grande, el segundo punto puede estar lejos y la secante describe un comportamiento bastante global. Si reducimos $|h|$, los dos puntos están cada vez más próximos y la secante examina la gráfica a una escala cada vez más local.

Podemos visualizar el proceso como

$$
|h|
\text{ grande}
\quad\longrightarrow\quad
|h|
\text{ pequeño}
\quad\longrightarrow\quad
Q_h\text{ próximo a }P.
$$

Pero hay una sutileza fundamental. Al acercar $Q_h$ a $P$, la secante pierde en el límite sus **dos puntos distintos**: cuando $h=0$, ambos puntos coincidirían. Por eso no podemos definir la pendiente buscada usando directamente dos puntos coincidentes.

La información debe sobrevivir de otra manera.

Lo que podemos conservar es el comportamiento límite de las pendientes

$$
\frac{f(a+h)-f(a)}{h}.
$$

Así aparece una característica esencial del cálculo diferencial:

$$
\boxed{
\text{para obtener información en un punto, estudiamos primero información entre puntos cercanos y después tomamos un límite.}
}
$$

### La lectura cinemática: de velocidad media a velocidad instantánea

La misma estructura aparece si $f$ describe una posición que cambia con el tiempo.

Sea

$$
s(t)
$$

la posición de una partícula en el instante $t$. Durante el intervalo que va de $t$ a $t+h$, el desplazamiento es

$$
s(t+h)-s(t),
$$

y la duración orientada del intervalo es

$$
h.
$$

La **velocidad media** durante ese intervalo es entonces

$$
\frac{s(t+h)-s(t)}{h},
\qquad h\ne0.
$$

La fórmula es exactamente el mismo cociente que apareció en la pendiente de la secante.

Geométricamente:

$$
\frac{f(a+h)-f(a)}{h}
=
\text{pendiente secante}.
$$

Cinemáticamente:

$$
\frac{s(t+h)-s(t)}{h}
=
\text{velocidad media}.
$$

En ambos casos estamos midiendo una razón de cambio sobre un intervalo no degenerado.

Pero un velocímetro pretende responder otra pregunta: ¿cuál es la velocidad **en el instante** $t$?

No podemos resolverla tomando literalmente un intervalo de duración cero, porque

$$
\frac{s(t)-s(t)}{0}
$$

no está definido. La estrategia correcta vuelve a ser la misma: calcular velocidades medias en intervalos cada vez más pequeños y preguntar si esas velocidades se aproximan a un único número.

Por ejemplo, si

$$
s(t)=t^2,
$$

entonces, para $h\ne0$,

$$
\frac{s(t+h)-s(t)}{h}
=
\frac{(t+h)^2-t^2}{h}
=
2t+h.
$$

Al reducir $|h|$, la velocidad media se aproxima a

$$
2t.
$$

De nuevo, el valor asociado al instante no se obtiene evaluando el cociente en $h=0$, sino estudiando su límite cuando $h\to0$.

Esta coincidencia entre geometría y movimiento no es accidental. Ambas situaciones están expresando una misma estructura matemática: **la tasa de cambio local de una función**.

### Tasa media primero, tasa instantánea después

Para dos puntos distintos $x_1$ y $x_2$ del dominio de una función, la razón

$$
\frac{f(x_2)-f(x_1)}{x_2-x_1}
$$

mide la tasa media de cambio de $f$ entre ambos puntos.

Si fijamos

$$
x_1=a
$$

y escribimos

$$
x_2=a+h,
$$

obtenemos exactamente

$$
\frac{f(a+h)-f(a)}{h}.
$$

La palabra «media» no implica aquí que estemos calculando una media aritmética de muchos valores. Significa que estamos condensando todo el cambio ocurrido entre dos entradas en una única razón global para ese intervalo.

La tasa **instantánea**, en cambio, no puede calcularse directamente entre dos instantes distintos, porque pretende estar asociada a un solo punto. La idea del cálculo consiste en no abandonar las tasas medias, sino hacerlas cada vez más locales:

$$
\text{tasa media en un intervalo}
\quad\xrightarrow{\;h\to0\;}
\quad
\text{candidato a tasa instantánea en el punto}.
$$

La palabra **candidato** importa. No toda función producirá necesariamente un límite finito y único. Puede ocurrir que las pendientes provenientes de ambos lados se aproximen a números diferentes, que crezcan sin cota, que oscilen o que el punto ni siquiera admita aproximaciones no triviales dentro del dominio.

Todas esas posibilidades serán estudiadas antes de que podamos hablar con seguridad de derivabilidad.

### No estamos usando infinitesimales como números misteriosos

Es frecuente describir informalmente el cálculo diciendo que $h$ se vuelve «infinitamente pequeño». Esa frase puede servir como intuición inicial, pero no será nuestro fundamento lógico.

En la teoría que ya hemos construido, escribir

$$
h\to0
$$

no significa introducir un número real no nulo cuyo tamaño sea «menor que cualquier real positivo».

Significa estudiar el comportamiento de una expresión para valores reales $h\ne0$ que pueden elegirse tan próximos a $0$ como sea necesario.

La diferencia es importante. Durante todo el proceso

$$
h\ne0,
$$

de modo que el cociente incremental está definido. Lo que hacemos es preguntar si existe un número $L$ tal que los valores

$$
\frac{f(a+h)-f(a)}{h}
$$

puedan forzarse a quedar arbitrariamente próximos a $L$ haciendo $|h|$ suficientemente pequeño.

Ésta es exactamente la clase de pregunta que aprendimos a responder con la definición rigurosa de límite.

::: {.callout-important title="La transición conceptual"}
La derivada no aparecerá porque «dividimos por un infinitesimal».

Aparecerá porque construimos una función del incremento,

$$
h\longmapsto\frac{f(a+h)-f(a)}{h},
\qquad h\ne0,
$$

y estudiamos si esa función posee un límite finito cuando $h\to0$.
:::

### Una misma estructura, tres lenguajes

Hemos llegado al mismo objeto desde tres perspectivas.

En lenguaje algebraico, tenemos el cociente incremental

$$
\frac{f(a+h)-f(a)}{h}.
$$

En lenguaje geométrico, tenemos la pendiente de la secante que une

$$
(a,f(a))
\quad\text{y}\quad
(a+h,f(a+h)).
$$

En lenguaje de tasas de cambio, tenemos la razón media entre variación de salida e incremento de entrada.

Podemos resumirlo así:

$$
\boxed{
\begin{array}{c}
\text{cociente incremental}\\
\Updownarrow\\
\text{pendiente de una secante}\\
\Updownarrow\\
\text{tasa media de cambio}
\end{array}
}
$$

La siguiente operación también es común a las tres lecturas:

$$
h\to0.
$$

- geométricamente, el segundo punto de la secante se aproxima al primero;
- cinemáticamente, el intervalo de tiempo se hace cada vez más corto;
- analíticamente, estudiamos el límite del cociente incremental.

Si ese proceso produce un único número real, habremos encontrado una cantidad local asociada al punto $a$.

### Qué falta todavía

El ejemplo de $x^2$ mostró un caso favorable, pero una definición matemática no puede construirse a partir de un dibujo convincente ni de una función bien comportada.

Antes de dar el siguiente paso debemos responder con precisión varias preguntas.

1. ¿Qué hipótesis sobre el dominio permiten que $h$ se aproxime realmente a $0$?
2. ¿Qué significa exactamente que el cociente incremental tenga un límite?
3. ¿Por qué, si ese límite existe, hay un único valor posible?
4. ¿Es equivalente acercarse mediante $h\to0$ a escribir directamente $x\to a$?
5. ¿Qué ocurre en el extremo de un intervalo, donde quizá solo podemos acercarnos desde un lado?
6. ¿Debemos aceptar $+\infty$ o $-\infty$ como valores de la nueva cantidad?
7. ¿Cómo podemos demostrar rigurosamente que el límite no existe cuando las pendientes se comportan de manera incompatible?

Estas preguntas muestran que ya estamos preparados para la definición, pero también que la definición debe formularse con cuidado.

La idea obtenida en esta sección puede condensarse en una sola cadena:

$$
\boxed{
\text{comparar dos puntos}
\to
\text{formar una tasa media}
\to
\text{reducir la escala}
\to
\text{buscar un límite en un punto}.
}
$$

En la sección siguiente convertiremos esa cadena en una noción matemática exacta: la **derivada de una función en un punto**.


## Derivada en un punto: definición, unicidad y criterio secuencial {#sec-t1-c07-02}

La sección anterior terminó con una pregunta precisa. Fijados un punto $a$ y una función $f$, podemos formar para puntos cercanos el cociente incremental

$$
\frac{f(a+h)-f(a)}{h},
\qquad h\ne0,
$$

y preguntar si esos valores se aproximan a un único número cuando $h\to0$.

Ahora convertiremos esa idea en una definición. El paso parece breve, pero exige cuidar tres aspectos que serán importantes durante todo el cálculo diferencial:

1. **el dominio desde el que nos acercamos a $a$**;
2. **la existencia de un límite real finito**;
3. **la unicidad del número obtenido**.

La derivada no será, por tanto, un símbolo nuevo añadido a una fórmula. Será una propiedad local de una función en un punto, construida enteramente a partir de la teoría de límites del capítulo 4.

### Antes de definir: ¿desde dónde puede acercarse el segundo punto?

Sea

$$
f\colon A\to\mathbb R
$$

y sea $a\in A$.

Para comparar $f(a)$ con valores $f(x)$ próximos necesitamos puntos del dominio distintos de $a$ que puedan acercarse a $a$. Por eso la hipótesis natural no es simplemente $a\in A$, sino que $a$ sea un **punto de acumulación de $A$**.

Esta condición garantiza que existen puntos de $A\setminus\{a\}$ arbitrariamente próximos a $a$ y, por tanto, que el cociente

$$
\frac{f(x)-f(a)}{x-a}
$$

puede estudiarse mediante un límite relativo al dominio.

Si $a$ fuera un punto aislado de $A$, no habría información incremental arbitrariamente próxima al centro. En ese caso no asignaremos una derivada a $f$ en $a$.

::: {.callout-warning title="Por qué no definimos derivadas en puntos aislados"}
En un punto aislado no existen puntos del dominio, distintos de $a$, suficientemente próximos a $a$.

La teoría de límites del capítulo 4 fue construida precisamente para evitar conclusiones vacías en esta situación. La derivada pretende medir **cómo cambia** la función al desplazarnos desde $a$. Si el dominio no permite desplazamientos arbitrariamente pequeños, esa información no existe.
:::

Cuando $a$ es un punto interior de $A$, podemos acercarnos desde ambos lados. Si el dominio permite acercarse solo desde uno, el límite relativo conserva esa geometría del dominio. En §6.4 separaremos explícitamente las nociones de derivada derecha e izquierda; por ahora mantendremos la formulación general relativa al dominio.

### La definición

::: {#def-t1-0042}
**Diferenciabilidad y derivada en un punto.** Sea $f\colon A\to\mathbb R$ y sea $a\in A$ un punto de acumulación de $A$.

Decimos que $f$ es **diferenciable en $a$ respecto del dominio $A$** si existe un número real $L$ tal que

$$
\lim_{\substack{x\to a\\x\in A}}
\frac{f(x)-f(a)}{x-a}
=L.
$$

Ese número, necesariamente único, se llama **derivada de $f$ en $a$ respecto de $A$** y se escribe

$$
f'_A(a)=L.
$$

Cuando el dominio está claro por el contexto escribiremos simplemente

$$
f'(a).
$$

El conjunto de puntos del dominio en los que $f$ es diferenciable será

$$
\operatorname{Dom}(f')
=
\left\{
 a\in A:
 a\text{ es punto de acumulación de }A
 \text{ y }f'_A(a)\text{ existe como número real}
\right\}.
$$

Así, cuando este conjunto no es vacío, la **función derivada** es la aplicación

$$
f'\colon \operatorname{Dom}(f')\to\mathbb R,
\qquad
 a\longmapsto f'(a).
$$
:::

La definición contiene varias decisiones que conviene hacer visibles.

Primero, el cociente se evalúa para $x\ne a$. El punto central no pertenece al dominio del cociente incremental porque allí aparecería una división por cero.

Segundo, el límite es **relativo a $A$**. No pedimos información sobre puntos que no pertenecen al dominio de $f$.

Tercero, exigimos que el límite sea un número de $\mathbb R$. Si el cociente crece sin cota hacia $+\infty$ o $-\infty$, podemos obtener una geometría interesante, pero bajo esta definición $f$ no es diferenciable en $a$.

Cuarto, la diferenciabilidad es una propiedad **puntual**. Afirmar que $f$ es diferenciable en $a$ no afirma todavía nada sobre la existencia de derivadas en puntos vecinos.

::: {.callout-note title="Leer la definición como una cadena de condiciones"}
Para preguntar si $f'(a)$ existe, audita en este orden:

$$
\boxed{
 a\in A
 \longrightarrow
 a\text{ punto de acumulación de }A
 \longrightarrow
 \text{cociente incremental definido para }x\ne a
 \longrightarrow
 \text{límite real finito}.
}
$$

Si falla una de estas etapas, la derivada no queda definida por `#def-t1-0042`.
:::

### La forma con incrementos $h$

La definición anterior utiliza un punto variable $x$. En §6.1 trabajamos, en cambio, con un incremento $h$ y escribimos $x=a+h$. Ambas formas describen exactamente el mismo proceso, pero conviene demostrarlo en lugar de tratarlo como una sustitución simbólica automática.

Para un punto fijo $a\in A$, definamos el conjunto de incrementos admisibles

$$
H_a:=\{h\in\mathbb R:a+h\in A\}.
$$

Entonces $0\in H_a$ porque $a\in A$, y si $a$ es punto de acumulación de $A$, $0$ es punto de acumulación de $H_a$.

Además, la correspondencia

$$
x\longleftrightarrow h=x-a
$$

transforma los puntos $x\in A\setminus\{a\}$ próximos a $a$ en incrementos $h\in H_a\setminus\{0\}$ próximos a $0$.

Por eso el cociente puede escribirse como

$$
\frac{f(x)-f(a)}{x-a}
=
\frac{f(a+h)-f(a)}{h}.
$$

Esta identidad algebraica es sencilla. Lo importante es que también se conserva la forma de aproximación al punto.

::: {#prp-t1-0035}
**Equivalencia de las dos formas del cociente incremental y unicidad de la derivada.** Sea $f\colon A\to\mathbb R$ y sea $a\in A$ un punto de acumulación de $A$. Para $L\in\mathbb R$, son equivalentes:

$$
\lim_{\substack{x\to a\\x\in A}}
\frac{f(x)-f(a)}{x-a}
=L,
$$

y

$$
\lim_{\substack{h\to0\\h\in H_a}}
\frac{f(a+h)-f(a)}{h}
=L,
$$

donde $H_a=\{h\in\mathbb R:a+h\in A\}$ y en ambos cocientes se entiende que $x\ne a$ o, equivalentemente, $h\ne0$.

En particular, si la derivada existe, su valor es único.
:::

**Demostración.** Consideremos primero la transformación

$$
h=x-a.
$$

Cuando $x\in A$ y $x\ne a$, tenemos $h\in H_a$ y $h\ne0$. Además,

$$
x\to a
\quad\Longleftrightarrow\quad
x-a\to0
\quad\Longleftrightarrow\quad
h\to0.
$$

Y para esos puntos

$$
\frac{f(x)-f(a)}{x-a}
=
\frac{f(a+h)-f(a)}{h}.
$$

Por tanto, la primera función de aproximación no es más que la segunda escrita en la coordenada desplazada $h=x-a$. El límite relativo a $A$ en $a$ existe y vale $L$ exactamente cuando el límite relativo a $H_a$ en $0$ existe y vale $L$.

Para la unicidad, si dos números reales $L$ y $M$ fueran valores de la derivada en $a$, el mismo cociente incremental tendría límite $L$ y límite $M$ en el mismo punto. Por la unicidad del límite funcional demostrada en `T1-C05`, necesariamente

$$
L=M.
$$

Así, cuando la derivada existe, no hay elección posible para su valor. $\square$

La demostración separa dos cuestiones diferentes.

- La equivalencia de las formas $x\to a$ y $h\to0$ proviene de una **traslación de coordenadas**.
- La unicidad de $f'(a)$ no es una nueva propiedad misteriosa: hereda directamente la **unicidad del límite**.

### La definición en lenguaje $\varepsilon$–$\delta$

Como la derivada es un límite funcional, podemos abrir inmediatamente su contenido cuantificado. Decir

$$
f'_A(a)=L
$$

significa que para todo $\varepsilon>0$ existe $\delta>0$ tal que, para todo $x\in A$,

$$
0<|x-a|<\delta
$$

implica

$$
\left|
\frac{f(x)-f(a)}{x-a}-L
\right|<\varepsilon.
$$

En lenguaje de incrementos, equivale a afirmar que para todo $\varepsilon>0$ existe $\delta>0$ tal que, para todo incremento admisible $h$,

$$
0<|h|<\delta
$$

implica

$$
\left|
\frac{f(a+h)-f(a)}{h}-L
\right|<\varepsilon.
$$

La estructura lógica es la ya conocida:

$$
\forall\varepsilon>0
\;\exists\delta>0
\;\forall h\in H_a:
\quad
0<|h|<\delta
\Longrightarrow
\left|
\frac{f(a+h)-f(a)}{h}-L
\right|<\varepsilon.
$$

La novedad no está en los cuantificadores. Está en **qué función** sometemos al control $\varepsilon$–$\delta$: el cociente incremental.

::: {.callout-important title="Qué controla realmente la derivada"}
La condición anterior no exige que

$$
f(a+h)-f(a)
$$

sea simplemente pequeño. La continuidad ya controlaba eso.

La derivada exige algo más preciso: que la **razón**

$$
\frac{f(a+h)-f(a)}{h}
$$

sea arbitrariamente próxima a un número fijo $L$ cuando la escala $|h|$ se hace pequeña.
:::

### Primeros cálculos desde la definición

El objetivo de este capítulo no es construir todavía un catálogo de reglas. Antes de aprender a derivar mecánicamente sumas, productos o composiciones, necesitamos ver qué dice la definición en los casos más simples.

::: {#exm-t1-0063}
**Funciones constante y afín desde la definición.** Consideremos primero una función constante

$$
f(x)=c
$$

sobre un dominio $A\subseteq\mathbb R$, y sea $a\in A$ un punto de acumulación de $A$. Para todo incremento admisible $h\ne0$,

$$
\frac{f(a+h)-f(a)}{h}
=
\frac{c-c}{h}
=0.
$$

Por tanto,

$$
f'_A(a)=0.
$$

Ahora sea

$$
g(x)=mx+b.
$$

Entonces, para $h\ne0$,

$$
\begin{aligned}
\frac{g(a+h)-g(a)}{h}
&=
\frac{m(a+h)+b-(ma+b)}{h}\\
&=
\frac{mh}{h}\\
&=m.
\end{aligned}
$$

El cociente incremental es ya constante en todo entorno perforado admisible de $0$. En consecuencia,

$$
g'_A(a)=m.
$$

Así, la derivada recupera exactamente la pendiente de una función afín y da pendiente nula a una función constante.
:::

Este ejemplo merece una lectura conceptual. Para una función afín, todas las secantes tienen la misma pendiente. No hace falta que las pendientes **se estabilicen** al reducir la escala: ya están estabilizadas desde el comienzo.

En una función no afín, como $x^2$, la pendiente de la secante depende de $h$ y solo al tomar un límite aparece una pendiente local. Ésta es una primera diferencia entre una función exactamente afín y una función que, más adelante, será aproximadamente afín a pequeña escala.

### El criterio secuencial para diferenciabilidad

La definición $\varepsilon$–$\delta$ es la formulación básica, pero el capítulo 4 nos dio otro lenguaje completamente equivalente para los límites funcionales: las sucesiones.

Apliquémoslo ahora no a $f$ directamente, sino a la función cociente incremental

$$
q_a(x):=
\frac{f(x)-f(a)}{x-a},
\qquad
x\in A\setminus\{a\}.
$$

Preguntar si $f$ es diferenciable en $a$ es exactamente preguntar si $q_a(x)$ tiene un límite real cuando $x\to a$ dentro de $A$.

::: {#prp-t1-0036}
**Criterio secuencial para diferenciabilidad.** Sea $f\colon A\to\mathbb R$ y sea $a\in A$ un punto de acumulación de $A$. Sea $L\in\mathbb R$. Entonces son equivalentes:

1. $f$ es diferenciable en $a$ y $f'_A(a)=L$;
2. para toda sucesión $(x_n)$ de puntos de $A\setminus\{a\}$ tal que
   $$
   x_n\to a,
   $$
   se cumple
   $$
   \frac{f(x_n)-f(a)}{x_n-a}\longrightarrow L.
   $$

Equivalentemente, en lenguaje de incrementos: para toda sucesión de incrementos admisibles $h_n\in H_a\setminus\{0\}$ con $h_n\to0$,

$$
\frac{f(a+h_n)-f(a)}{h_n}\longrightarrow L.
$$
:::

**Demostración.** Consideremos de nuevo

$$
q_a(x)=\frac{f(x)-f(a)}{x-a}
$$

sobre $A\setminus\{a\}$.

Por definición,

$$
f'_A(a)=L
$$

si y solo si

$$
\lim_{\substack{x\to a\\x\in A}}q_a(x)=L.
$$

El criterio secuencial para límites funcionales de `T1-C05` afirma que este límite existe y vale $L$ si y solo si, para toda sucesión $(x_n)$ del dominio perforado que converja a $a$,

$$
q_a(x_n)\to L.
$$

Sustituyendo la definición de $q_a$ obtenemos exactamente

$$
\frac{f(x_n)-f(a)}{x_n-a}\to L.
$$

La versión con $h_n$ se obtiene mediante $h_n=x_n-a$ y la equivalencia de `#prp-t1-0035`. $\square$

Este criterio tiene dos usos distintos.

Para **demostrar** que una derivada existe, hay que controlar el cociente para toda sucesión admisible que se acerque al punto. En muchos ejemplos sencillos será más directo calcular el límite funcional.

Para **demostrar que una derivada no existe**, en cambio, basta encontrar dos sucesiones admisibles que se acerquen al mismo punto y produzcan comportamientos incompatibles del cociente incremental. Ese método será central en §6.3.

::: {.callout-note title="Cómo refutar una derivada con sucesiones"}
Si encontramos $x_n\to a$ y $y_n\to a$, con $x_n,y_n\in A\setminus\{a\}$, tales que

$$
\frac{f(x_n)-f(a)}{x_n-a}\to L_1
$$

y

$$
\frac{f(y_n)-f(a)}{y_n-a}\to L_2,
$$

con $L_1\ne L_2$, entonces $f'(a)$ no existe.

No estamos usando una regla especial de derivación: estamos negando la existencia de un límite mediante el criterio secuencial.
:::

### Tres pruebas de estrés para la definición

Una definición matemática se comprende mejor cuando intentamos hacerla fallar.

#### 1. El centro pertenece al dominio, pero se excluye del cociente

Para hablar de $f'(a)$ necesitamos conocer $f(a)$, pues aparece en el numerador. Sin embargo, el cociente

$$
\frac{f(x)-f(a)}{x-a}
$$

solo se evalúa cuando $x\ne a$.

No hay contradicción. La función original debe estar definida en el centro, mientras que la función auxiliar $q_a$ vive en un dominio perforado alrededor de ese centro.

#### 2. Un punto aislado no tiene derivada bajo nuestra definición

Supongamos, por ejemplo, que

$$
A=\{0\}\cup[1,\infty)
$$

y consideramos cualquier función $f\colon A\to\mathbb R$.

El punto $0$ pertenece al dominio, pero es aislado. No existen puntos de $A\setminus\{0\}$ arbitrariamente próximos a $0$.

Por tanto, `#def-t1-0042` no asigna $f'_A(0)$. La ausencia de puntos cercanos no constituye una prueba de regularidad; constituye ausencia de información diferencial.

#### 3. Una pendiente que escapa a infinito no es una derivada real

Nuestra definición exige

$$
f'_A(a)\in\mathbb R.
$$

Si el cociente incremental tiende a $+\infty$ o $-\infty$, el límite no existe **como número real finito**. Más adelante distinguiremos ese comportamiento de una esquina y de una oscilación, pero desde ahora debe quedar claro que escribir informalmente “$f'(a)=\infty$” no concuerda con la definición adoptada aquí.

### Derivada en un punto y función derivada no son lo mismo

La notación $f'(a)$ designa un número asociado a un punto concreto, siempre que el límite correspondiente exista.

La notación $f'$ designa, en cambio, una nueva función cuyo dominio es

$$
\operatorname{Dom}(f')
=
\{a\in A:f\text{ es diferenciable en }a\}.
$$

Estas dos afirmaciones tienen niveles lógicos diferentes:

$$
\boxed{
\text{$f$ es diferenciable en $a$}
}
$$

es una afirmación puntual, mientras que

$$
\boxed{
\text{$f$ es diferenciable en todos los puntos de un conjunto $E$}
}
$$

es una familia de afirmaciones puntuales, una por cada $a\in E$.

Todavía no estudiaremos propiedades globales de $f'$, ni preguntaremos si $f'$ es continua. Eso pertenece a etapas posteriores. Por ahora la prioridad es comprender con precisión qué significa que **un solo** número $f'(a)$ exista.

### Lo que la definición todavía no nos regala

Hemos formalizado la derivada, pero no hemos obtenido ninguna regla de cálculo.

De `#def-t1-0042` no se sigue automáticamente una tabla como

$$
(f+g)'=f'+g',
\qquad
(fg)'=f'g+fg',
\qquad
(g\circ f)'=(g'\circ f)f'.
$$

Esas afirmaciones requieren teoremas y pertenecen a `T1-C08`.

En este capítulo seguiremos trabajando primero **desde la definición**. Esta disciplina tiene una finalidad: aprender qué mecanismo debe verificarse antes de convertir la derivación en una técnica algebraica eficiente.

Por el momento, el núcleo conceptual es exactamente éste:

$$
\boxed{
 f'_A(a)=L
 \quad\Longleftrightarrow\quad
 \frac{f(a+h)-f(a)}{h}\longrightarrow L
 \text{ para incrementos admisibles }h\to0.
}
$$

Y, por el criterio secuencial,

$$
\boxed{
 f'_A(a)=L
 \quad\Longleftrightarrow\quad
 \frac{f(a+h_n)-f(a)}{h_n}\longrightarrow L
 \text{ para toda sucesión admisible }h_n\to0,
}
$$

con $h_n\ne0$.

La sección siguiente utilizará estas dos formulaciones como herramientas de trabajo. Calcularemos derivadas sencillas directamente desde la definición y, con la misma definición, aprenderemos a demostrar que una derivada **no** existe.


## Calcular desde la definición y aprender a fallar {#sec-t1-c07-03}

Ya tenemos una definición precisa de derivada y dos lenguajes equivalentes para usarla. Si $f$ está definida alrededor de un punto $a$, podemos estudiar directamente

$$
\frac{f(a+h)-f(a)}{h},
\qquad h\ne0,
$$

y preguntar si ese cociente tiene un límite real cuando $h\to0$.

Éste será todavía nuestro único mecanismo de cálculo. No usaremos reglas de suma, producto, cociente, potencias o composición. Esas reglas llegarán en `T1-C08` y deberán ser demostradas. Por ahora queremos adquirir una habilidad más básica: **mirar una función, construir su cociente incremental y decidir qué le ocurre cuando la escala se reduce**.

La misma definición servirá para dos tareas aparentemente opuestas:

$$
\boxed{
\begin{array}{c}
\text{hacer aparecer un límite}\\[2mm]
\text{y}\\[2mm]
\text{demostrar que ningún límite puede existir}.
\end{array}
}
$$

Esa simetría es importante. Saber derivar no consiste solo en obtener números; también consiste en reconocer cuándo la información local de la función es incompatible con una única pendiente.

### Un protocolo de cálculo desde la definición

Antes de trabajar ejemplos conviene separar las operaciones que realmente intervienen.

Fijado un punto $a$, seguiremos este esquema:

1. calcular exactamente $f(a+h)-f(a)$;
2. formar el cociente incremental para $h\ne0$;
3. simplificar **solo bajo la condición $h\ne0$**;
4. estudiar el límite de la expresión simplificada cuando $h\to0$;
5. si el límite existe como número real, identificarlo con $f'(a)$.

La parte algebraica ocurre en los pasos 1–3. La parte analítica ocurre en el paso 4. Confundirlas suele producir dos errores opuestos: intentar sustituir $h=0$ antes de simplificar o, al revés, creer que una simplificación algebraica por sí sola ya demuestra la existencia del límite.

::: {.callout-note title="La pregunta que debe guiar el cálculo"}
No preguntes primero «¿qué fórmula de derivación conozco?». Pregunta:

$$
\boxed{
\text{¿en qué se convierte exactamente el cociente incremental para }h\ne0?
}
$$

Una vez respondida esa pregunta, la teoría de límites hace el resto.
:::

### La parábola, ahora sí como cálculo de derivada

En §6.1 ya descubrimos que las pendientes secantes de $x^2$ se estabilizan. Ahora podemos reinterpretar ese mismo cálculo mediante la definición formal introducida en §6.2.

::: {#exm-t1-0064}
**Derivada de $f(x)=x^2$ en un punto arbitrario desde la definición.** Sea

$$
f(x)=x^2,
\qquad x\in\mathbb R,
$$

y fijemos $a\in\mathbb R$.

Para $h\ne0$,

$$
\begin{aligned}
\frac{f(a+h)-f(a)}{h}
&=
\frac{(a+h)^2-a^2}{h}\\
&=
\frac{2ah+h^2}{h}\\
&=
2a+h.
\end{aligned}
$$

La cancelación de $h$ es legítima porque estamos trabajando en el dominio perforado $h\ne0$. Ahora sí tomamos el límite:

$$
\lim_{h\to0}(2a+h)=2a.
$$

Por `#def-t1-0042`,

$$
\boxed{f'(a)=2a.}
$$

Como $a$ era arbitrario, la función es diferenciable en todo punto real y su función derivada queda dada, en este caso concreto, por

$$
f'(x)=2x.
$$

Este resultado ha sido obtenido **sin** utilizar una regla para derivar potencias.
:::

El cálculo anterior contiene un patrón que volverá a aparecer muchas veces: el numerador parece producir una indeterminación si uno intenta poner $h=0$, pero para $h\ne0$ contiene un factor $h$ que puede separarse. Después de cancelar ese factor queda una expresión cuyo límite es ordinario.

Podemos describir la arquitectura del cálculo así:

$$
\boxed{
\frac{(a+h)^2-a^2}{h}
\xrightarrow{\;h\ne0\;}
2a+h
\xrightarrow{\;h\to0\;}
2a.
}
$$

La primera flecha es álgebra. La segunda es análisis.

### Un grado más: $x^3$ sin regla de potencias

Repitamos deliberadamente el procedimiento con

$$
g(x)=x^3.
$$

Fijado $a\in\mathbb R$ y para $h\ne0$,

$$
\begin{aligned}
\frac{g(a+h)-g(a)}{h}
&=
\frac{(a+h)^3-a^3}{h}\\
&=
\frac{3a^2h+3ah^2+h^3}{h}\\
&=
3a^2+3ah+h^2.
\end{aligned}
$$

Por tanto,

$$
\lim_{h\to0}
\left(3a^2+3ah+h^2\right)
=3a^2,
$$

y así

$$
\boxed{g'(a)=3a^2.}
$$

De nuevo, no hemos usado una regla general. Hemos demostrado el resultado para esta función mediante una identidad algebraica exacta y las leyes de límites ya disponibles.

Conviene observar qué fue esencial y qué no. No era importante «recordar» la expansión del cubo como un truco de derivación. Lo importante era transformar

$$
(a+h)^3-a^3
$$

en una expresión donde el factor $h$ que necesariamente aparece al comparar dos valores pueda hacerse visible y cancelarse para $h\ne0$.

::: {.callout-important title="Factorizar no es tomar el límite"}
En los ejemplos de $x^2$ y $x^3$, la factorización elimina una obstrucción algebraica. Pero la derivada aparece **después**, al demostrar un límite.

No debemos confundir

$$
\text{simplificar el cociente}
$$

con

$$
\text{demostrar que el cociente tiene límite}.
$$
:::

### La definición también debe saber decir «no»

Hasta ahora todos los ejemplos han sido favorables. Podría parecer que, una vez construido el cociente incremental, siempre será posible simplificarlo y obtener algún número.

Eso es falso.

La diferenciabilidad exige que **todos** los modos admisibles de acercarse al punto produzcan el mismo comportamiento límite del cociente. Por eso el criterio secuencial de `#prp-t1-0036` es especialmente eficaz para refutar una derivada: basta encontrar dos sucesiones que se aproximen al mismo punto y produzcan límites incompatibles.

El valor absoluto proporciona el ejemplo elemental decisivo.

::: {#exm-t1-0065}
**$f(x)=|x|$ en $0$: continuidad sin derivabilidad.** Consideremos

$$
f(x)=|x|.
$$

Sabemos que $f$ es continua en $0$ y que $f(0)=0$. Para estudiar la derivabilidad debemos examinar otra cantidad:

$$
\frac{f(h)-f(0)}{h}
=
\frac{|h|}{h},
\qquad h\ne0.
$$

Si $h>0$, entonces $|h|=h$ y por tanto

$$
\frac{|h|}{h}=1.
$$

Si $h<0$, entonces $|h|=-h$ y

$$
\frac{|h|}{h}=-1.
$$

Ahora usemos dos sucesiones de incrementos admisibles:

$$
h_n=\frac1n,
\qquad
k_n=-\frac1n.
$$

Ambas satisfacen

$$
h_n\to0,
\qquad
k_n\to0,
$$

pero los correspondientes cocientes incrementales cumplen

$$
\frac{|h_n|}{h_n}=1
\longrightarrow1,
$$

mientras que

$$
\frac{|k_n|}{k_n}=-1
\longrightarrow-1.
$$

Si $f'(0)$ existiera, `#prp-t1-0036` obligaría a que **toda** sucesión admisible produjera el mismo límite. Como hemos obtenido dos valores distintos,

$$
1\ne-1,
$$

concluimos que

$$
\boxed{f'(0)\text{ no existe}.}
$$

Así, $|x|$ es continua en $0$ pero no diferenciable allí.
:::

Este argumento merece ser leído lógicamente. No hemos demostrado la inexistencia de la derivada examinando «muchos» valores de $h$. Hemos usado la negación exacta del criterio universal.

La diferenciabilidad exigiría:

$$
\text{para toda sucesión }h_n\to0,
\quad
\frac{f(h_n)-f(0)}{h_n}\to L
$$

para un mismo $L$. Para negar esa afirmación basta exhibir dos sucesiones que obliguen a valores incompatibles.

En otras palabras,

$$
\boxed{
\text{dos caminos incompatibles bastan para destruir un límite único}.
}
$$

No necesitamos todavía introducir el vocabulario formal de derivada derecha e izquierda. En §6.4 daremos nombre a esos comportamientos. Aquí basta observar que los incrementos positivos y negativos producen información incompatible.

### Continuidad y diferenciabilidad están mirando escalas distintas

El ejemplo de $|x|$ permite ver una diferencia conceptual importante.

Para continuidad en $0$ estudiamos

$$
|h|-|0|=|h|,
$$

y esta cantidad tiende a $0$.

Para diferenciabilidad estudiamos la variación **dividida por la escala del incremento**:

$$
\frac{|h|}{h}.
$$

La variación absoluta se hace pequeña, pero su razón con el incremento conserva una diferencia de signo que no desaparece al aumentar el zoom.

Podemos resumir el contraste así:

$$
\boxed{
\begin{array}{rcl}
|h| &\longrightarrow& 0,\\[1mm]
\dfrac{|h|}{h} &\not\longrightarrow& \text{un único número real}.
\end{array}
}
$$

Esto muestra concretamente por qué conocer la continuidad no basta para conocer la derivabilidad. La primera controla que el cambio sea pequeño; la segunda exige además que ese cambio tenga una **parte proporcional estable de primer orden**.

### Cambiar de fórmula no implica perder la derivabilidad

El fracaso de $|x|$ podría sugerir otra regla falsa: «si una función cambia de fórmula en un punto, entonces allí no puede ser diferenciable».

También es falso.

Lo decisivo no es cuántas fórmulas aparecen en la definición, sino qué ocurre con el cociente incremental.

::: {#exm-t1-0066}
**$f(x)=x|x|$ en $0$: cambio de fórmula sin pérdida de derivabilidad.** Consideremos

$$
f(x)=x|x|.
$$

Esta función puede escribirse por tramos como

$$
f(x)=
\begin{cases}
x^2, & x\ge0,\\
-x^2, & x<0.
\end{cases}
$$

En particular,

$$
f(0)=0.
$$

Para $h\ne0$,

$$
\frac{f(h)-f(0)}{h}
=
\frac{h|h|}{h}
=|h|.
$$

Ahora el comportamiento es completamente distinto del ejemplo anterior:

$$
|h|\longrightarrow0
\qquad(h\to0).
$$

Por tanto,

$$
\boxed{f'(0)=0.}
$$

También podemos verificarlo con el criterio secuencial. Si $(h_n)$ es **cualquier** sucesión no nula con $h_n\to0$, entonces

$$
\frac{f(h_n)-f(0)}{h_n}
=|h_n|\to0.
$$

La forma de la función cambia al atravesar $0$, pero toda sucesión admisible produce el mismo límite del cociente incremental.
:::

Comparemos los dos ejemplos centrales:

| función | cociente incremental en $0$ | comportamiento |
|---|---|---|
| $|x|$ | $\dfrac{|h|}{h}$ | produce $1$ para $h>0$ y $-1$ para $h<0$ |
| $x|x|$ | $|h|$ | tiende a $0$ desde cualquier sucesión admisible |

La diferencia entre ambas funciones es pequeña en apariencia, pero decisiva a escala diferencial. Multiplicar $|x|$ por $x$ añade precisamente un factor que hace desaparecer la incompatibilidad de primer orden.

No necesitamos todavía formular esta observación mediante órdenes asintóticos. Ese lenguaje llegará en §6.7. Por ahora basta leer directamente los cocientes.

### Dos funciones por tramos pueden comportarse de maneras opuestas

Los ejemplos anteriores permiten desmontar una intuición gráfica demasiado rápida.

Una función por tramos puede presentar un cambio visible de expresión algebraica y, sin embargo, ser diferenciable en la interfaz. Otra puede ser perfectamente continua y aun así no poseer una derivada allí.

Por tanto, ninguna de estas frases constituye un criterio válido:

- «la fórmula cambia, luego no hay derivada»;
- «la gráfica no tiene salto, luego hay derivada»;
- «la función se ve suave, luego el límite existe».

El criterio válido sigue siendo el mismo:

$$
\boxed{
\text{construir el cociente incremental y estudiar su límite}.
}
$$

### Cómo elegir una estrategia: cálculo o refutación

En los ejemplos de esta sección han aparecido dos arquitecturas distintas.

Cuando queremos **demostrar existencia**, buscamos una expresión exacta que permita controlar todos los incrementos admisibles:

$$
\frac{f(a+h)-f(a)}{h}
\longrightarrow L.
$$

Así procedimos para $x^2$, $x^3$ y $x|x|$.

Cuando queremos **demostrar inexistencia**, puede ser mucho más eficiente construir testigos incompatibles:

$$
h_n\to0,
\qquad
k_n\to0,
$$

pero

$$
\frac{f(a+h_n)-f(a)}{h_n}\to L_1,
\qquad
\frac{f(a+k_n)-f(a)}{k_n}\to L_2,
\qquad
L_1\ne L_2.
$$

Así procedimos para $|x|$.

Podemos convertirlo en un pequeño mapa de decisión:

$$
\boxed{
\begin{array}{c}
\text{formar el cociente incremental}\\[1mm]
\downarrow\\[1mm]
\text{¿puedo simplificarlo y controlar todos los }h?\\[1mm]
\swarrow\qquad\searrow\\[-1mm]
\text{sí}\qquad\qquad\text{no o sospecho incompatibilidad}\\[1mm]
\downarrow\qquad\qquad\downarrow\\[1mm]
\text{calcular el límite}\qquad
\text{buscar sucesiones testigo}.
\end{array}
}
$$

### Errores que estos ejemplos permiten diagnosticar

::: {.callout-warning title="Cuatro errores frecuentes"}
**1. Sustituir $h=0$ en el cociente original.**  
La derivada es un límite en un entorno perforado. El cociente no necesita estar definido en $h=0$.

**2. Comprobar solo incrementos positivos.**  
En un punto interior de un dominio como $\mathbb R$, la definición exige controlar todos los incrementos suficientemente pequeños, no solo los de un signo.

**3. Usar una regla de derivación que todavía no ha sido demostrada.**  
Saber por experiencia que $(x^3)'=3x^2$ no reemplaza la prueba desde la definición que estamos practicando aquí.

**4. Decidir por la apariencia de la gráfica.**  
Un dibujo puede sugerir qué investigar, pero la existencia o inexistencia de la derivada es una afirmación sobre un límite.
:::

Hay además una disciplina algebraica que conviene conservar. Factorizar, expandir o racionalizar no son rituales del cálculo. Son herramientas que se usan solo cuando ayudan a revelar el comportamiento del cociente para $h\ne0$. En $x^2$ y $x^3$ la factorización aparece naturalmente; en otros ejemplos puede ser necesaria otra transformación. La estrategia debe responder a la estructura del numerador, no a una receta memorizada.

### Tres niveles de lectura de un cálculo de derivada

Un cálculo completo puede leerse en tres niveles.

**Nivel algebraico.** ¿Qué identidad exacta convierte el cociente en una forma manejable?

**Nivel analítico.** ¿Qué teorema de límites justifica el paso $h\to0$?

**Nivel lógico.** ¿Estoy probando existencia para todos los acercamientos admisibles o refutándola mediante testigos incompatibles?

Por ejemplo, para $x^2$:

$$
\underbrace{\frac{(a+h)^2-a^2}{h}=2a+h}_{\text{álgebra para }h\ne0}
\quad\Longrightarrow\quad
\underbrace{2a+h\to2a}_{\text{límite}}
\quad\Longrightarrow\quad
\underbrace{f'(a)=2a}_{\text{definición}}.
$$

Para $|x|$:

$$
\underbrace{\frac{|h|}{h}}_{\text{cociente}}
\quad\xrightarrow{\ h_n=1/n\ }
1,
\qquad
\underbrace{\frac{|h|}{h}}_{\text{mismo cociente}}
\quad\xrightarrow{\ k_n=-1/n\ }
-1,
$$

y la incompatibilidad de esos límites refuta la existencia de una derivada única.

### Qué hemos aprendido antes de tener reglas

Sin disponer todavía de un álgebra de derivadas, ya podemos distinguir cuatro situaciones conceptuales:

1. una función afín, cuyo cociente incremental es constante;
2. una función como $x^2$ o $x^3$, cuyo cociente depende de $h$ pero converge tras simplificar;
3. una función como $|x|$, cuyo cociente conserva comportamientos incompatibles al acercarse al punto;
4. una función por tramos como $x|x|$, cuya expresión cambia pero cuyo cociente sí converge.

El punto común a las cuatro situaciones es que la derivabilidad no está codificada en la apariencia superficial de la fórmula. Está codificada en el **límite del cambio relativo a la escala**.

La sección puede resumirse mediante una sola oposición:

$$
\boxed{
\begin{array}{ccc}
\text{existencia de derivada}
&\Longleftrightarrow&
\text{un único comportamiento límite del cociente},\\[2mm]
\text{no derivabilidad}
&\Longleftarrow&
\text{dos comportamientos límite incompatibles}.
\end{array}
}
$$

En §6.4 daremos una organización más fina a las maneras en que este límite puede fallar. Introduciremos derivadas derecha e izquierda, distinguiremos una esquina de una pendiente que crece sin cota y separaremos ambos fenómenos de la oscilación persistente del cociente incremental.

## Derivadas laterales, extremos, esquinas y pendientes verticales {#sec-t1-c07-04}

En §6.3 vimos que la derivabilidad puede fallar porque distintos modos de acercarse al punto producen comportamientos incompatibles del cociente incremental. El ejemplo de $|x|$ ya contenía la idea esencial: los incrementos positivos y negativos aportaban información diferente.

Ahora daremos un nombre preciso a esas dos direcciones y separaremos tres fenómenos que un dibujo puede confundir fácilmente:

$$
\boxed{
\text{esquina}
\qquad\text{vs.}\qquad
\text{pendiente vertical}
\qquad\text{vs.}\qquad
\text{oscilación persistente}.
}
$$

Los tres impiden una derivada bilateral real finita, pero lo hacen por razones matemáticamente distintas.

### Acercarse al punto desde un solo lado

Sea

$$
f\colon A\to\mathbb R,
$$

y sea $a\in A$.

Para hablar de comportamiento diferencial desde la derecha necesitamos que existan puntos de $A$ mayores que $a$ arbitrariamente próximos a $a$. Es decir, $a$ debe ser punto de acumulación de

$$
A\cap(a,\infty).
$$

Análogamente, para hablar de comportamiento desde la izquierda necesitamos que $a$ sea punto de acumulación de

$$
A\cap(-\infty,a).
$$

La idea es exactamente la misma que para los límites laterales del capítulo 4, pero aplicada al cociente incremental.

::: {#def-t1-0043}
**Derivadas laterales.** Sea $f\colon A\to\mathbb R$ y sea $a\in A$.

Si $a$ es punto de acumulación de $A\cap(a,\infty)$, decimos que $f$ tiene **derivada derecha** en $a$ respecto de $A$ si existe como número real finito el límite

$$
f'_{A,+}(a)
:=
\lim_{\substack{x\to a\\x\in A,\ x>a}}
\frac{f(x)-f(a)}{x-a}.
$$

Equivalentemente, en lenguaje de incrementos,

$$
f'_{A,+}(a)
=
\lim_{\substack{h\to0^+\\a+h\in A}}
\frac{f(a+h)-f(a)}{h}.
$$

Si $a$ es punto de acumulación de $A\cap(-\infty,a)$, decimos que $f$ tiene **derivada izquierda** en $a$ respecto de $A$ si existe como número real finito el límite

$$
f'_{A,-}(a)
:=
\lim_{\substack{x\to a\\x\in A,\ x<a}}
\frac{f(x)-f(a)}{x-a},
$$

o, equivalentemente,

$$
f'_{A,-}(a)
=
\lim_{\substack{h\to0^-\\a+h\in A}}
\frac{f(a+h)-f(a)}{h}.
$$

Cuando el dominio sea claro escribiremos simplemente $f'_+(a)$ y $f'_-(a)$.
:::

Hay dos detalles de la definición que conviene destacar.

Primero, una derivada lateral sigue siendo una **derivada definida mediante un límite**. No consiste en sustituir un signo en una fórmula ni en mirar solo una parte del dibujo.

Segundo, bajo nuestra convención, una derivada lateral también debe ser un número real finito. Si el cociente incremental tiende a $+\infty$ o $-\infty$ por uno de los lados, describiremos ese comportamiento explícitamente, pero no escribiremos que la derivada lateral vale infinito.

### El criterio bilateral por derivadas laterales

En un punto interior de un intervalo —o, más generalmente, en un punto donde el dominio acumula por ambos lados— la derivada ordinaria debe reconciliar la información derecha e izquierda.

La razón es estructural. El cociente incremental

$$
q_a(x)=\frac{f(x)-f(a)}{x-a}
$$

posee un límite bilateral exactamente cuando sus dos límites laterales existen y coinciden.

::: {#prp-t1-0037}
**Criterio lateral para la derivada bilateral.** Sea $f\colon A\to\mathbb R$ y sea $a\in A$. Supongamos que $a$ es punto de acumulación de $A$ tanto por la izquierda como por la derecha.

Entonces $f$ es diferenciable en $a$ respecto de $A$ si y solo si existen las dos derivadas laterales como números reales y

$$
f'_{A,-}(a)=f'_{A,+}(a).
$$

En ese caso,

$$
f'_A(a)=f'_{A,-}(a)=f'_{A,+}(a).
$$
:::

**Demostración.** Definamos, para $x\in A\setminus\{a\}$,

$$
q_a(x):=\frac{f(x)-f(a)}{x-a}.
$$

Por `#def-t1-0042`, $f$ es diferenciable en $a$ exactamente cuando existe el límite bilateral

$$
\lim_{\substack{x\to a\\x\in A}}q_a(x)
$$

como número real finito.

Como $A$ acumula en $a$ por ambos lados, el criterio de límites laterales demostrado en `T1-C05` afirma que este límite bilateral existe y vale $L$ si y solo si existen los dos límites laterales de $q_a$ y ambos valen $L$.

Pero esos dos límites son precisamente

$$
f'_{A,-}(a)
\qquad\text{y}\qquad
f'_{A,+}(a).
$$

Por tanto, la derivada bilateral existe si y solo si ambas derivadas laterales existen como números reales y coinciden. En ese caso los tres valores son iguales. $\square$

La prueba es deliberadamente corta porque no necesita una teoría nueva: el resultado se hereda directamente del teorema bilateral ↔ laterales para límites funcionales.

::: {.callout-important title="La hipótesis de dos lados no es ornamental"}
El criterio anterior supone que el dominio acumula en $a$ **por ambos lados**.

Si $A=[0,\infty)$ y $a=0$, no existe aproximación dentro de $A$ desde la izquierda. En ese caso la derivada relativa al dominio de `#def-t1-0042` es naturalmente unilateral y coincide con la derivada derecha cuando ésta existe.

No debemos exigir un límite lateral desde puntos que no pertenecen al dominio.
:::

### Extremos de intervalos: la geometría del dominio importa

Consideremos la restricción

$$
f\colon[0,\infty)\to\mathbb R,
\qquad
f(x)=x^2.
$$

En $0$ solo existen incrementos admisibles $h\ge0$. Para $h>0$,

$$
\frac{f(h)-f(0)}{h}
=
\frac{h^2}{h}
=h,
$$

y por tanto

$$
\lim_{h\to0^+}h=0.
$$

Así,

$$
f'_{[0,\infty)}(0)=f'_+(0)=0.
$$

No hay ninguna derivada izquierda que verificar respecto de este dominio, porque $0$ no es punto de acumulación de $[0,\infty)$ por la izquierda.

Esto muestra por qué la frase «para que exista una derivada deben coincidir las derivadas izquierda y derecha» necesita una condición previa. Es correcta en un punto donde ambas aproximaciones existen dentro del dominio; no es un criterio universal para extremos.

### Una esquina: dos pendientes finitas, pero incompatibles

Regresemos a

$$
f(x)=|x|.
$$

En §6.3 calculamos

$$
\frac{f(h)-f(0)}{h}
=
\frac{|h|}{h}.
$$

Ahora podemos expresar el diagnóstico en el nuevo lenguaje:

$$
f'_-(0)=-1,
\qquad
f'_+(0)=1.
$$

Las dos derivadas laterales existen y son finitas, pero no coinciden. Por `#prp-t1-0037`, $f'(0)$ no existe.

A este patrón local lo llamaremos una **esquina**: las pendientes laterales se aproximan a dos números reales distintos.

El punto importante no es la palabra geométrica, sino la firma analítica:

$$
\boxed{
\text{esquina en }a
\quad\Longrightarrow\quad
f'_-(a),f'_+(a)\in\mathbb R
\text{ existen, pero }
f'_-(a)\ne f'_+(a).
}
$$

La implicación se usa aquí como descripción del patrón que estamos llamando esquina; no pretende clasificar toda posible geometría no suave a partir de una figura.

### Pendiente vertical: el cociente no se estabiliza en un número real

Una situación distinta ocurre cuando las pendientes secantes crecen sin cota al acercarnos al punto.

Consideremos la función de raíz cuadrada con signo

$$
g(x)=
\begin{cases}
\sqrt{x}, & x\ge0,\\
-\sqrt{-x}, & x<0.
\end{cases}
$$

La continuidad de $\sqrt{\phantom{x}}$ en $[0,\infty)$ ya está disponible desde `T1-C06`, de modo que $g(x)\to0=g(0)$ cuando $x\to0$. En $0$, para $h\ne0$,

$$
\frac{g(h)-g(0)}{h}
=
\frac{1}{\sqrt{|h|}}.
$$

Como $\sqrt{|h|}\to0^+$ cuando $h\to0$,

$$
\frac{1}{\sqrt{|h|}}\longrightarrow+\infty.
$$

Geométricamente, las pendientes de las secantes se hacen arbitrariamente grandes y la gráfica presenta una **tangente vertical** en el sentido geométrico usual, la recta $x=0$.

Pero bajo `#def-t1-0042` esto no significa

$$
g'(0)=+\infty.
$$

Tal igualdad no pertenece a nuestra definición: $+\infty$ no es un número real. La conclusión correcta es

$$
\boxed{g'(0)\text{ no existe como derivada real finita}.}
$$

El fenómeno es diferente de una esquina. En una esquina existen dos pendientes laterales reales incompatibles; aquí no aparece ninguna pendiente real finita porque el cociente escapa sin cota.

### Un mismo «no hay derivada» puede esconder mecanismos distintos

::: {#exm-t1-0067}
**Esquina, pendiente vertical y oscilación: tres fallos diferentes.** Comparemos tres funciones en $0$.

**1. Esquina:**

$$
f(x)=|x|.
$$

Tenemos

$$
f'_-(0)=-1,
\qquad
f'_+(0)=1.
$$

Los dos límites laterales del cociente existen como números reales, pero son distintos.

**2. Pendiente vertical:**

$$
g(x)=
\begin{cases}
\sqrt{x}, & x\ge0,\\
-\sqrt{-x}, & x<0.
\end{cases}
$$

Su cociente incremental es

$$
\frac{g(h)-g(0)}{h}
=
\frac{1}{\sqrt{|h|}}
\longrightarrow+\infty.
$$

No hay una derivada real finita, aunque geométricamente las secantes sugieren la recta vertical $x=0$.

**3. Oscilación persistente:** definamos

$$
p(x)=
\begin{cases}
 x\sin(1/x), & x\ne0,\\
 0, & x=0.
\end{cases}
$$

La función es continua en $0$ porque

$$
|x\sin(1/x)|\le |x|\longrightarrow0.
$$

Sin embargo, para $h\ne0$,

$$
\frac{p(h)-p(0)}{h}
=
\sin(1/h).
$$

Incluso restringiéndonos a $h>0$, tomemos

$$
h_n=\frac{1}{\frac{\pi}{2}+2\pi n},
\qquad
k_n=\frac{1}{\frac{3\pi}{2}+2\pi n}.
$$

Entonces

$$
h_n\to0^+,
\qquad
k_n\to0^+,
$$

pero

$$
\sin(1/h_n)=1,
\qquad
\sin(1/k_n)=-1.
$$

Por el criterio secuencial, ni siquiera existe la derivada derecha de $p$ en $0$.

Los tres casos concluyen «no existe una derivada bilateral real finita», pero por mecanismos distintos:

| fenómeno | comportamiento del cociente incremental |
|---|---|
| esquina | dos límites laterales finitos distintos |
| pendiente vertical | crecimiento sin cota |
| oscilación | no hay estabilización ni siquiera lateral |
:::

Este cuadro es más informativo que una única etiqueta «no diferenciable». El cálculo diferencial no solo pregunta si un límite existe: cuando falla, conviene identificar **cómo** falla.

### Cuidado con la palabra «cúspide»

En dibujos elementales se usa a veces la palabra **cúspide** para diversos perfiles puntiagudos con pendientes no acotadas. Esa terminología geométrica no será nuestra herramienta de clasificación principal.

Analíticamente distinguiremos siempre el comportamiento concreto del cociente incremental. Por ejemplo, puede ocurrir que

$$
\frac{f(a+h)-f(a)}{h}\to+\infty
$$

desde ambos lados, o que tienda a $-\infty$ desde un lado y a $+\infty$ desde el otro. Ninguno de estos casos produce una derivada real finita, aunque sus dibujos puedan recibir nombres geométricos diferentes.

La disciplina del capítulo será describir primero los límites que realmente ocurren y solo después añadir una interpretación gráfica.

### Las derivadas laterales no son dos números que siempre existan

Es tentador pensar que toda función posee automáticamente una «pendiente por la izquierda» y otra «por la derecha», y que el único problema consiste en compararlas.

Eso también es falso.

Para que $f'_+(a)$ exista necesitamos un límite real finito del cociente cuando $h\to0^+$. El ejemplo oscilatorio anterior muestra que este límite puede no existir. Lo mismo puede ocurrir por la izquierda.

Así, en un punto donde el dominio acumula por ambos lados, la auditoría correcta es:

$$
\boxed{
\begin{array}{c}
\text{¿existe }f'_-(a)\text{ como real finito?}\\[1mm]
\text{¿existe }f'_+(a)\text{ como real finito?}\\[1mm]
\text{si ambas existen, ¿son iguales?}
\end{array}
}
$$

Solo una respuesta afirmativa a las tres preguntas produce una derivada bilateral.

### Un mapa de diagnóstico local

Podemos organizar los comportamientos vistos hasta ahora como un árbol de decisión.

Partimos del cociente incremental

$$
Q_a(h)=\frac{f(a+h)-f(a)}{h}.
$$

Si el dominio admite incrementos de ambos signos, preguntamos primero por cada lado:

$$
\boxed{
\begin{array}{c}
Q_a(h)\text{ cuando }h\to0^-\qquad Q_a(h)\text{ cuando }h\to0^+\\[2mm]
\downarrow\hspace{43mm}\downarrow\\[-1mm]
\text{¿límite real finito?}\hspace{18mm}\text{¿límite real finito?}
\end{array}
}
$$

A partir de allí:

- si ambos límites finitos existen y son iguales, hay derivada bilateral;
- si ambos existen pero son distintos, aparece el patrón de esquina;
- si el cociente escapa a $\pm\infty$, hay pendiente no acotada, no una derivada real;
- si el cociente oscila sin límite, falla incluso la estabilización lateral correspondiente.

En un extremo del dominio, en cambio, solo se audita el lado que realmente pertenece al dominio.

### Qué no hemos usado

Toda la sección descansa únicamente en:

1. la definición de derivada de §6.2;
2. los límites laterales de `T1-C05`;
3. el criterio bilateral ↔ laterales para límites funcionales;
4. el criterio secuencial;
5. estimaciones y álgebra elementales.

No hemos usado reglas de suma, producto, cociente o cadena para derivadas. Tampoco hemos usado Rolle, el teorema del valor medio ni ninguna caracterización global de monotonía.

Eso preserva la dirección deductiva del capítulo.

### Hacia una relación estructural con la continuidad

Las secciones anteriores han mostrado que una función puede ser continua y, sin embargo, fallar en ser diferenciable: $|x|$ y la función oscilatoria $x\sin(1/x)$ en $0$ son ejemplos distintos de ese fenómeno.

La pregunta inversa es más profunda:

$$
\boxed{
\text{si una función es diferenciable en }a,\text{ ¿debe ser continua en }a?
}
$$

En §6.5 demostraremos que la respuesta es afirmativa. El resultado no necesitará ninguna regla de derivación: surgirá directamente de la definición y del álgebra de límites.

## Diferenciabilidad implica continuidad {#sec-t1-c07-05}

Las secciones anteriores han separado cuidadosamente dos preguntas locales.

La **continuidad** en $a$ pregunta si

$$
f(x)-f(a)\longrightarrow0
\qquad(x\to a),
$$

mientras que la **diferenciabilidad** pregunta si la variación, después de dividirla por la escala $x-a$, posee un límite real finito:

$$
\frac{f(x)-f(a)}{x-a}
\longrightarrow
f'(a).
$$

A primera vista son condiciones distintas. Sin embargo, la segunda contiene más información que la primera. Si conocemos cómo se comporta la variación **por unidad de incremento**, entonces podemos reconstruir la variación misma multiplicando de nuevo por el incremento.

La pregunta guía de esta sección es, por tanto,

$$
\boxed{
\text{¿por qué controlar la variación hasta primer orden obliga ya a controlar el valor de la función?}
}
$$

### Antes de demostrar: qué relación debemos esperar

Ya sabemos que la continuidad no garantiza diferenciabilidad. La función $|x|$ es continua en $0$, pero su cociente incremental tiene comportamientos laterales incompatibles.

Así que una equivalencia

$$
\text{continuidad}
\Longleftrightarrow
\text{diferenciabilidad}
$$

no puede ser verdadera.

Queda abierta la dirección contraria:

$$
\text{diferenciabilidad}
\Longrightarrow
\text{continuidad}.
$$

¿Por qué debería funcionar?

Si $f$ es diferenciable en $a$, entonces cerca de $a$ el cociente

$$
\frac{f(x)-f(a)}{x-a}
$$

se aproxima a un número real. En particular, no puede crecer sin control ni oscilar con amplitud ilimitada. Pero

$$
f(x)-f(a)
=
(x-a)
\frac{f(x)-f(a)}{x-a}
$$

para $x\ne a$.

El primer factor tiende a $0$; el segundo tiende a un número real finito. Esa identidad contiene ya toda la prueba.

::: {.callout-note title="Arquitectura antes de la demostración"}
La estrategia es

$$
\boxed{
\begin{array}{c}
\text{diferenciabilidad}\\[1mm]
\Downarrow\\[1mm]
\dfrac{f(x)-f(a)}{x-a}\to f'(a)\in\mathbb R\\[3mm]
\Downarrow\\[1mm]
(x-a)\dfrac{f(x)-f(a)}{x-a}\to0\cdot f'(a)=0\\[3mm]
\Downarrow\\[1mm]
f(x)-f(a)\to0\\[1mm]
\Downarrow\\[1mm]
\text{continuidad}.
\end{array}
}
$$

La prueba no necesita ninguna regla de derivación. Solo necesita la definición de derivada y el álgebra de límites ya construida.
:::

### El teorema fundamental de esta sección

::: {#thm-t1-0024}
**Diferenciabilidad implica continuidad.** Sea $f\colon A\to\mathbb R$ y sea $a\in A$ un punto de acumulación de $A$. Si $f$ es diferenciable en $a$ respecto del dominio $A$, entonces $f$ es continua en $a$ respecto de $A$.
:::

**Demostración.** Supongamos que $f$ es diferenciable en $a$. Entonces existe el número real

$$
L=f'_A(a)
$$

y, por definición,

$$
\lim_{\substack{x\to a\\x\in A}}
\frac{f(x)-f(a)}{x-a}
=L.
$$

Para todo $x\in A$ con $x\ne a$ tenemos la identidad exacta

$$
f(x)-f(a)
=
(x-a)
\frac{f(x)-f(a)}{x-a}.
$$

Cuando $x\to a$ dentro de $A$,

$$
x-a\longrightarrow0
$$

y

$$
\frac{f(x)-f(a)}{x-a}
\longrightarrow L.
$$

Por la regla del producto para límites funcionales,

$$
\lim_{\substack{x\to a\\x\in A}}
\bigl(f(x)-f(a)\bigr)
=
0\cdot L
=0.
$$

Por tanto,

$$
\lim_{\substack{x\to a\\x\in A}}f(x)
=f(a),
$$

que es precisamente la continuidad de $f$ en $a$ relativa a su dominio. $\square$

La demostración es corta, pero conviene no confundir brevedad con trivialidad. Su mecanismo depende de una decisión anterior muy importante: la derivada fue definida como un **límite real finito**. Si el cociente incremental escapara a infinito, no podríamos aplicar simplemente el producto de límites reales como acabamos de hacerlo.

### Leer la prueba sin memorizarla

La identidad central

$$
f(x)-f(a)
=
(x-a)
\frac{f(x)-f(a)}{x-a}
$$

puede reconstruirse preguntando qué queremos demostrar.

Para continuidad necesitamos controlar

$$
f(x)-f(a).
$$

Para diferenciabilidad ya controlamos

$$
\frac{f(x)-f(a)}{x-a}.
$$

La forma natural de conectar ambas expresiones es multiplicar el cociente por aquello que habíamos dividido:

$$
(x-a)
\frac{f(x)-f(a)}{x-a}.
$$

Así, la arquitectura de la prueba no surge de un truco aislado. Surge de alinear exactamente la **hipótesis disponible** con el **objetivo deseado**.

::: {.callout-important title="El factor que hace el trabajo"}
La diferenciabilidad controla el cociente incremental:

$$
\frac{f(x)-f(a)}{x-a}\to L.
$$

La continuidad aparece porque el incremento de entrada satisface

$$
x-a\to0.
$$

Por eso

$$
\underbrace{f(x)-f(a)}_{\text{variación de salida}}
=
\underbrace{x-a}_{\to0}
\underbrace{\frac{f(x)-f(a)}{x-a}}_{\to L}.
$$

La variación de salida queda forzada a tender a $0$.
:::

### La misma prueba descomprimida en lenguaje $\varepsilon$–$\delta$

El argumento con álgebra de límites es completo. Pero descomprimirlo permite ver cuantitativamente dónde aparece el control.

Sea

$$
L=f'_A(a).
$$

Como

$$
\frac{f(x)-f(a)}{x-a}\to L,
$$

podemos exigir, por ejemplo, que para $x$ suficientemente próximo a $a$ y $x\ne a$,

$$
\left|
\frac{f(x)-f(a)}{x-a}-L
\right|<1.
$$

Entonces, por desigualdad triangular,

$$
\left|
\frac{f(x)-f(a)}{x-a}
\right|
\le
|L|+1.
$$

Es decir: la existencia de una derivada finita fuerza al cociente incremental a quedar **localmente acotado**.

Ahora, para esos mismos puntos,

$$
|f(x)-f(a)|
=
|x-a|
\left|
\frac{f(x)-f(a)}{x-a}
\right|
\le
(|L|+1)|x-a|.
$$

Dado $\varepsilon>0$, basta exigir además

$$
|x-a|<\frac{\varepsilon}{|L|+1}.
$$

Combinando ambas restricciones sobre $|x-a|$, obtenemos

$$
|f(x)-f(a)|<\varepsilon.
$$

Y si $x=a$, la desigualdad es automática porque

$$
|f(a)-f(a)|=0.
$$

Así se recupera directamente la definición de continuidad.

Esta versión hace visible una idea útil:

$$
\boxed{
\text{derivabilidad}
\Longrightarrow
\text{cociente incremental localmente acotado}
\Longrightarrow
|f(x)-f(a)|\le C|x-a|
\text{ cerca de }a.
}
$$

No estamos introduciendo aquí una teoría nueva de regularidad. Solo estamos leyendo con mayor detalle la información que ya contiene la existencia de la derivada.

### Una consecuencia inmediata: la discontinuidad descarta la derivabilidad

El teorema anterior puede leerse por contraposición.

::: {#cor-t1-0013}
**Una discontinuidad excluye diferenciabilidad.** Sea $f\colon A\to\mathbb R$ y sea $a\in A$ un punto de acumulación de $A$. Si $f$ no es continua en $a$ respecto de $A$, entonces $f$ no es diferenciable en $a$ respecto de $A$.
:::

**Demostración.** Si $f$ fuera diferenciable en $a$, el teorema anterior obligaría a que fuera continua en $a$. Por contraposición, la discontinuidad impide la diferenciabilidad. $\square$

Este corolario es una herramienta de **descarte**, no un procedimiento para calcular derivadas. Si una función tiene un salto, una oscilación que destruye continuidad o un valor central incompatible con su límite, ya sabemos que no puede ser diferenciable allí. No hace falta estudiar después su cociente incremental.

Pero debe leerse con cuidado. El corolario afirma

$$
\text{discontinua en }a
\Longrightarrow
\text{no diferenciable en }a.
$$

No afirma la recíproca.

### La conversa es falsa

::: {#exm-t1-0068}
**Continuidad necesaria, pero no suficiente: $f(x)=|x|$ en $0$.** Consideremos

$$
f(x)=|x|.
$$

La función es continua en $0$ porque

$$
\lim_{x\to0}|x|=0=f(0).
$$

Sin embargo, en §6.3 calculamos el cociente incremental

$$
\frac{f(h)-f(0)}{h}
=
\frac{|h|}{h},
\qquad h\ne0,
$$

y en §6.4 identificamos sus derivadas laterales:

$$
f'_-(0)=-1,
\qquad
f'_+(0)=1.
$$

Como los dos límites laterales finitos son distintos, la derivada bilateral no existe.

Por tanto,

$$
\boxed{
\text{$|x|$ es continua en $0$, pero no diferenciable en $0$.}
}
$$

Este ejemplo refuta la conversa del teorema.
:::

La relación lógica correcta es entonces

$$
\boxed{
\text{diferenciabilidad en }a
\Longrightarrow
\text{continuidad en }a,
}
$$

pero

$$
\boxed{
\text{continuidad en }a
\not\Longrightarrow
\text{diferenciabilidad en }a.
}
$$

En otras palabras, la continuidad es una **condición necesaria** para la diferenciabilidad, pero no es suficiente.

### Qué ocurre en un extremo del dominio

Como todas nuestras definiciones son relativas al dominio, el teorema no exige que $a$ sea un punto interior de $A$.

Por ejemplo, si

$$
f\colon[0,\infty)\to\mathbb R
$$

es diferenciable en $0$ según la aproximación permitida por su dominio, el cociente incremental solo usa $h>0$ suficientemente pequeño. La misma identidad

$$
f(h)-f(0)
=
h\frac{f(h)-f(0)}{h}
$$

muestra que

$$
f(h)\to f(0)
\qquad(h\to0^+).
$$

Eso es exactamente continuidad relativa a $[0,\infty)$ en $0$.

No necesitamos inventar valores de la función a la izquierda del dominio para obtener la conclusión.

### Dos errores lógicos que conviene bloquear

::: {.callout-warning title="No invertir ni fortalecer el teorema"}
**Error 1.** «Si $f$ es continua en $a$, entonces $f$ es diferenciable en $a$.»  
Falso: $|x|$ en $0$ lo refuta.

**Error 2.** «Si $f$ es diferenciable en $a$, entonces $f$ es diferenciable cerca de $a$.»  
Tampoco se sigue. El teorema es puntual: de la derivabilidad en **ese punto** solo deducimos continuidad en **ese punto**.
:::

La segunda advertencia será especialmente importante más adelante. Una derivada en un punto no convierte automáticamente a la función en una función diferenciable sobre un intervalo, ni autoriza todavía conclusiones sobre monotonía, extremos o comportamiento global.

### Una lectura secuencial del mismo resultado

También podemos reconstruir el teorema usando sucesiones, sin introducir una prueba nueva esencial.

Supongamos que $f$ es diferenciable en $a$ y tomemos cualquier sucesión $(x_n)$ de puntos de $A$ tal que

$$
x_n\to a.
$$

Si algunos términos satisfacen $x_n=a$, entonces para esos índices

$$
f(x_n)-f(a)=0.
$$

Para los índices restantes,

$$
f(x_n)-f(a)
=
(x_n-a)
\frac{f(x_n)-f(a)}{x_n-a}.
$$

Sobre esa parte de la sucesión, el primer factor tiende a $0$ y, por el criterio secuencial de diferenciabilidad, el segundo tiende a $f'_A(a)$. Así, los términos no centrales de $f(x_n)-f(a)$ tienden a $0$, mientras que los términos centrales son exactamente $0$. En conjunto,

$$
f(x_n)-f(a)\to0,
$$

y así

$$
f(x_n)\to f(a).
$$

El criterio secuencial de continuidad recupera la misma conclusión.

Esta lectura confirma que la prueba no depende de una forma particular de aproximación: funciona para **todo** acercamiento permitido por el dominio.

### Qué hemos ganado

Antes de esta sección teníamos dos nociones locales estudiadas por separado. Ahora sabemos que están jerarquizadas:

$$
\boxed{
\text{diferenciabilidad}
\quad\text{es una condición local más fuerte que}\quad
\text{continuidad}.
}
$$

La razón estructural puede condensarse en una sola identidad:

$$
\boxed{
f(x)-f(a)
=
(x-a)
\frac{f(x)-f(a)}{x-a}.}
$$

La derivada controla el segundo factor; la proximidad $x\to a$ hace desaparecer el primero.

Todavía, sin embargo, seguimos leyendo $f'(a)$ principalmente como un número obtenido de pendientes secantes. En §6.6 convertiremos ese número en un objeto geométrico preciso: la **recta tangente**. La definición será local y no dependerá de cuántas veces una recta intersecte globalmente la gráfica.

## La recta tangente: una definición local, no una figura {#sec-t1-c07-06}

Hasta ahora la derivada ha aparecido como un número: el límite de las pendientes de secantes cuando el segundo punto de la gráfica se aproxima al primero. Esa construcción sugiere inmediatamente una recta, pero conviene separar con cuidado la intuición geométrica de la definición matemática.

La pregunta es ahora:

$$
\boxed{
\text{si }f'(a)\text{ existe, ¿qué recta representa exactamente esa pendiente local?}
}
$$

La respuesta será sencilla en su fórmula, pero importante en su interpretación. La recta tangente no se definirá por «tocar» la gráfica, por quedar de un solo lado de ella ni por tener una única intersección. Se definirá a partir de la información local contenida en la derivada.

### De una pendiente local a una recta

Supongamos que

$$
f\colon A\to\mathbb R
$$

es diferenciable en un punto $a\in A$ respecto del dominio $A$. Entonces ya conocemos dos datos:

$$
P=(a,f(a))
$$

y

$$
f'_A(a).
$$

El primero fija un punto del plano. El segundo fija una pendiente real finita.

Por la geometría elemental de la recta, existe una única recta que pasa por $P$ y tiene esa pendiente. Su ecuación, en forma punto-pendiente, es

$$
y-f(a)=f'_A(a)(x-a).
$$

Equivalentemente,

$$
y=f(a)+f'_A(a)(x-a).
$$

Esta observación conduce a la definición.

::: {#def-t1-0044}
**Recta tangente asociada a una derivada finita.** Sea $f\colon A\to\mathbb R$ y sea $a\in A$ un punto de acumulación de $A$. Supongamos que $f$ es diferenciable en $a$ respecto de $A$.

La **recta tangente a la gráfica de $f$ en $(a,f(a))$**, respecto de ese dominio, es la recta de ecuación

$$
\boxed{
T_a(x)=f(a)+f'_A(a)(x-a).
}
$$

Cuando el dominio está claro por el contexto escribiremos simplemente

$$
T_a(x)=f(a)+f'(a)(x-a).
$$
:::

La definición conserva exactamente la información que produjo la derivada:

$$
\begin{aligned}
\text{punto de paso} &:& (a,f(a)),\\
\text{pendiente} &:& f'_A(a).
\end{aligned}
$$

No añade ninguna condición global sobre la gráfica.

### Por qué esta recta está vinculada a las secantes

En §6.1 escribimos la secante determinada por los puntos

$$
(a,f(a))
\quad\text{y}\quad
(a+h,f(a+h))
$$

como

$$
S_h(x)
=
f(a)+Q_a(h)(x-a),
$$

con

$$
Q_a(h)=\frac{f(a+h)-f(a)}{h}.
$$

Si $f$ es diferenciable en $a$, entonces

$$
Q_a(h)\longrightarrow f'_A(a)
$$

para incrementos admisibles $h\to0$.

Por tanto, el coeficiente que cambia en la familia de secantes —su pendiente— converge precisamente a la pendiente de $T_a$.

Para cualquier $x$ fijo,

$$
S_h(x)-T_a(x)
=
\bigl(Q_a(h)-f'_A(a)\bigr)(x-a),
$$

y de aquí

$$
S_h(x)\longrightarrow T_a(x)
$$

cuando $h\to0$ dentro del dominio admisible.

Esta observación da sentido preciso, al nivel que necesitamos ahora, a la frase informal «la tangente es el límite de las secantes». No estamos construyendo todavía una teoría abstracta de límites de rectas: controlamos la pendiente y, con ello, el valor de cada secante en todo punto $x$ fijo.

::: {.callout-note title="Qué significa aquí «límite de secantes»"}
Todas las secantes $S_h$ pasan por el mismo punto $(a,f(a))$. Lo que varía es su pendiente.

La derivabilidad afirma exactamente que

$$
\text{pendiente de }S_h
\longrightarrow
f'_A(a).
$$

La tangente es la recta que pasa por el mismo punto y posee esa pendiente límite.
:::

### Una tangente puede cruzar la gráfica

Una imagen escolar frecuente sugiere que una recta tangente «toca» la curva pero no la atraviesa. Esa descripción puede funcionar en algunos dibujos, pero no puede servir como definición.

El ejemplo más simple ya está disponible con una función que calculamos desde la definición.

::: {#exm-t1-0069}
**La tangente a $f(x)=x^3$ en $0$ cruza la gráfica.** Consideremos

$$
f(x)=x^3.
$$

En §6.3 obtuvimos desde el cociente incremental que

$$
f'(a)=3a^2.
$$

En particular,

$$
f(0)=0,
\qquad
f'(0)=0.
$$

Por `#def-t1-0044`, la recta tangente en el origen es

$$
T_0(x)
=
f(0)+f'(0)(x-0)
=0.
$$

Es decir, la tangente es el eje horizontal

$$
y=0.
$$

Pero la función satisface

$$
x^3<0\quad\text{si }x<0,
$$

y

$$
x^3>0\quad\text{si }x>0.
$$

Por tanto, al atravesar $x=0$, la gráfica pasa de un lado de la recta $y=0$ al otro.

La recta tangente **cruza** la gráfica en el punto de tangencia.

Así queda refutada la regla informal

$$
\boxed{
\text{«una tangente no puede atravesar la curva».}
}
$$
:::

La derivada no contiene ninguna condición que obligue a la gráfica a permanecer de un solo lado de la tangente. Solo determina el comportamiento de primer orden de las pendientes secantes alrededor del punto.

### Una tangente puede volver a intersectar la gráfica lejos del punto

También es falsa otra descripción frecuente: «la tangente es una recta que tiene exactamente un punto en común con la gráfica».

Consideremos, sin introducir un nuevo objeto numerado,

$$
p(x)=x^2(x-10).
$$

En $a=0$ tenemos $p(0)=0$ y, para $h\ne0$,

$$
\frac{p(h)-p(0)}{h}
=
\frac{h^2(h-10)}{h}
=
h(h-10).
$$

Como

$$
h(h-10)\longrightarrow0,
$$

se sigue directamente de la definición que

$$
p'(0)=0.
$$

La tangente en el origen es entonces

$$
y=0.
$$

Sin embargo,

$$
p(10)=10^2(10-10)=0.
$$

La misma recta tangente vuelve a intersectar la gráfica en

$$
(10,0).
$$

Nada de esto modifica la tangencia en el origen. El punto $x=10$ está fuera de la información que interviene en el límite $h\to0$.

Este ejemplo deja una separación importante:

$$
\boxed{
\text{tangencia en }a
\quad\text{es una noción local, no un conteo global de intersecciones.}
}
$$

### Lo local y lo global no deben confundirse

Para determinar $T_a$ necesitamos solamente

$$
f(a)
$$

y

$$
f'_A(a).
$$

El segundo dato se obtiene observando el cociente incremental para puntos arbitrariamente próximos a $a$. Por eso cambiar la función lejos de $a$ puede alterar drásticamente la gráfica completa sin cambiar la pendiente tangente en $a$.

Podemos organizar la distinción así:

| información relevante para la tangente en $a$ | información que no forma parte de la definición |
|---|---|
| el valor $f(a)$ | cuántas intersecciones hay lejos de $a$ |
| el límite del cociente incremental en $a$ | si la gráfica queda globalmente arriba o abajo de la recta |
| la pendiente finita $f'_A(a)$ | la forma completa de la gráfica |
| el comportamiento arbitrariamente próximo a $a$ | lo que ocurre en regiones alejadas del punto |

Más adelante formalizaremos con precisión esta idea de **localidad** de la derivada. Por ahora basta observar que la definición de tangente hereda la naturaleza local del límite que define $f'(a)$.

### El caso de un extremo del dominio

La definición tampoco exige que $a$ sea interior del dominio.

Supongamos, por ejemplo, que

$$
f\colon[0,\infty)\to\mathbb R,
\qquad
f(x)=x^2.
$$

En $a=0$, los incrementos admisibles son $h>0$. Desde el dominio,

$$
\frac{f(h)-f(0)}{h}
=
h
\longrightarrow0
\qquad(h\to0^+).
$$

Así,

$$
f'_{[0,\infty)}(0)=0,
$$

y la recta tangente determinada por nuestra definición es

$$
T_0(x)=0.
$$

La evidencia diferencial proviene solo del lado disponible del dominio, pero la recta obtenida es una recta ordinaria del plano. No necesitamos extender artificialmente la función a $x<0$ para definirla.

### Pendiente vertical y nuestra definición de tangente

En §6.4 distinguimos un cociente incremental que tiende a infinito de una derivada real finita. Esa decisión tiene ahora una consecuencia geométrica explícita.

`#def-t1-0044` define una recta tangente mediante el número real

$$
f'_A(a).
$$

Si el cociente incremental crece sin cota, entonces $f'_A(a)$ no existe bajo nuestra definición y, por tanto, tampoco existe una recta tangente **en el sentido de `#def-t1-0044`**.

Geométricamente puede ser útil decir que la gráfica presenta una **tangente vertical** y señalar la recta

$$
x=a,
$$

pero esa es una extensión terminológica distinta. No debemos escribir

$$
f'(a)=\infty
$$

ni confundir una pendiente vertical con una derivada real.

::: {.callout-warning title="Tres definiciones falsas de tangente"}
No adoptaremos ninguna de estas reglas:

1. **«La tangente toca la gráfica pero no la cruza.»** Falso: $x^3$ en $0$.
2. **«La tangente tiene exactamente una intersección con la gráfica.»** Falso: $x^2(x-10)$ en $0$ tiene la tangente $y=0$, que vuelve a cortar la gráfica en $x=10$.
3. **«Cualquier recta que visualmente parezca ajustarse a la curva es tangente.»** Insuficiente: la pendiente debe ser exactamente la derivada definida mediante el límite del cociente incremental.
:::

### La ecuación de la tangente todavía no es toda la historia

Hemos convertido la derivada en una recta precisa:

$$
\boxed{
T_a(x)=f(a)+f'_A(a)(x-a).
}
$$

Sabemos además de dónde proviene su pendiente: es el límite de las pendientes secantes.

Pero todavía queda una pregunta más profunda.

¿Por qué esta recta no es solo una traducción geométrica del número $f'(a)$, sino un **modelo local de la función**?

Para responder necesitamos comparar directamente

$$
f(a+h)
$$

con

$$
T_a(a+h)=f(a)+f'_A(a)h
$$

y medir el error entre ambos a la escala del incremento $h$.

Ese será el objetivo de §6.7. Allí pasaremos de

$$
\text{pendiente tangente}
$$

a

$$
\text{aproximación lineal local de primer orden},
$$

sin usar Taylor ni ninguna regla de derivación posterior.

## Diferenciabilidad como aproximación lineal local {#sec-t1-c07-07}

La sección anterior definió la recta tangente a partir de la derivada y dejó abierta una pregunta más profunda. Si

$$
T_a(x)=f(a)+f'_A(a)(x-a),
$$

¿en qué sentido matemático esta recta **aproxima** realmente a la función cerca de $a$?

Decir solamente que ambas pasan por $(a,f(a))$ es demasiado débil: infinitas rectas pasan por ese punto. Decir que tienen la misma pendiente local ya es más informativo, pero todavía queremos convertir esa idea en una afirmación directa sobre los valores de $f$.

La pregunta guía será

$$
\boxed{
\text{¿qué información más profunda contiene el número }f'(a)\text{ además de una pendiente?}
}
$$

La respuesta será que la derivada determina la **parte lineal principal** del cambio de la función. Después de retirar esa parte lineal, queda un error que se vuelve despreciable frente a la propia escala del incremento.

### De la continuidad al primer orden

Supongamos que $f$ es continua en $a$. Entonces

$$
f(a+h)-f(a)\longrightarrow0
\qquad(h\to0),
$$

con $h$ restringido, como siempre, a incrementos admisibles por el dominio.

Esta afirmación dice que la variación total se hace pequeña. Pero no dice **a qué velocidad** se hace pequeña respecto de $h$.

Por ejemplo, las cantidades

$$
h,
\qquad
h^2,
\qquad
|h|^{1/2}
$$

tienden todas a $0$ cuando $h\to0$. Sin embargo, su tamaño relativo frente a $|h|$ es muy distinto:

$$
\frac{|h|}{|h|}=1,
\qquad
\frac{|h|^2}{|h|}=|h|\to0,
\qquad
\frac{|h|^{1/2}}{|h|}=\frac1{|h|^{1/2}}\to+\infty.
$$

Así, «el error tiende a $0$» no basta para identificar un comportamiento de primer orden.

La diferenciabilidad exige algo más fino. Si $L=f'_A(a)$, queremos separar

$$
f(a+h)-f(a)
$$

en una parte principal

$$
Lh
$$

y un residuo mucho menor que $h$.

### El residuo después de retirar la parte lineal

Fijemos $L\in\mathbb R$ y definamos, para todo incremento admisible $h$,

$$
r(h):=f(a+h)-f(a)-Lh.
$$

Entonces tenemos la identidad exacta

$$
f(a+h)=f(a)+Lh+r(h).
$$

No hemos aproximado nada todavía: simplemente hemos nombrado la diferencia entre el valor real de la función y el modelo afín

$$
f(a)+Lh.
$$

La cuestión decisiva es el tamaño de $r(h)$ cuando $h\to0$.

Si solo sabemos que

$$
r(h)\to0,
$$

el residuo puede seguir siendo del mismo orden que $h$. Por ejemplo, $r(h)=h$ tiende a $0$, pero

$$
\frac{r(h)}{h}=1.
$$

Para que $Lh$ sea realmente la parte principal de primer orden necesitamos una condición más fuerte:

$$
\frac{r(h)}{h}\longrightarrow0.
$$

Esto significa que, comparado con el incremento $h$, el residuo se vuelve proporcionalmente insignificante.

### La notación $o(h)$

::: {#def-t1-0045}
**Pequeño-o de primer orden.** Sea $H\subseteq\mathbb R$ un conjunto para el cual $0$ es punto de acumulación, y sea $r\colon H\to\mathbb R$ una función definida al menos en un entorno relativo de $0$.

Escribimos

$$
r(h)=o(h)
\qquad(h\to0,\ h\in H)
$$

si

$$
\lim_{\substack{h\to0\\h\in H}}
\frac{r(h)}{h}
=0.
$$

Equivalentemente, para todo $\varepsilon>0$ existe $\delta>0$ tal que, para todo $h\in H$,

$$
0<|h|<\delta
\quad\Longrightarrow\quad
|r(h)|<\varepsilon |h|.
$$

Cuando el conjunto de incrementos admisibles está claro por el contexto, abreviaremos simplemente

$$
r(h)=o(h).
$$
:::

La definición debe leerse como una comparación de escalas:

$$
\boxed{
r(h)=o(h)
\quad\Longleftrightarrow\quad
\text{el residuo es despreciable frente a }|h|\text{ cuando }h\to0.
}
$$

::: {.callout-warning title="Qué significa —y qué no significa— $o(h)$"}
La expresión $o(h)$ **no designa un número especial** ni una función universal llamada «$o$».

En una fórmula como

$$
f(a+h)=f(a)+Lh+o(h),
$$

la notación afirma que existe un término residual $r(h)$ que satisface

$$
r(h)=o(h).
$$

Tampoco basta con que $r(h)\to0$. La condición característica es la comparación

$$
\frac{r(h)}{h}\to0.
$$
:::

En este capítulo no desarrollaremos un cálculo asintótico general. Usaremos $o(h)$ únicamente para expresar con precisión la aproximación de primer orden asociada a la derivada.

### El teorema de linealización local

Ahora podemos reformular la diferenciabilidad sin hablar primero de cocientes incrementales.

::: {#thm-t1-0025}
**Caracterización de la diferenciabilidad por linealización local.** Sea $f\colon A\to\mathbb R$, sea $a\in A$ un punto de acumulación de $A$ y sea $L\in\mathbb R$. Denotemos por

$$
H_a=\{h\in\mathbb R:a+h\in A\}
$$

el conjunto de incrementos admisibles.

Son equivalentes:

1. $f$ es diferenciable en $a$ respecto de $A$ y
   $$
   f'_A(a)=L;
   $$
2. existe un residuo $r$ tal que, para $h\in H_a$ suficientemente próximo a $0$,
   $$
   f(a+h)=f(a)+Lh+r(h)
   $$
   y
   $$
   r(h)=o(h)
   \qquad(h\to0,\ h\in H_a).
   $$

Por tanto podemos escribir de forma abreviada

$$
\boxed{
f'_A(a)=L
\quad\Longleftrightarrow\quad
f(a+h)=f(a)+Lh+o(h)
}
$$

cuando $h\to0$ a través de los incrementos admisibles del dominio.
:::

**Demostración.** Supongamos primero que

$$
f'_A(a)=L.
$$

Por la forma incremental de la derivada,

$$
\frac{f(a+h)-f(a)}{h}
\longrightarrow L
\qquad(h\to0,\ h\in H_a).
$$

Definamos

$$
r(h)=f(a+h)-f(a)-Lh.
$$

Para $h\ne0$,

$$
\frac{r(h)}{h}
=
\frac{f(a+h)-f(a)}{h}-L.
$$

Al tomar el límite,

$$
\frac{r(h)}{h}\longrightarrow L-L=0.
$$

Luego

$$
r(h)=o(h),
$$

y la identidad

$$
f(a+h)=f(a)+Lh+r(h)
$$

da la linealización buscada.

Recíprocamente, supongamos que

$$
f(a+h)=f(a)+Lh+r(h)
$$

con

$$
r(h)=o(h).
$$

Para $h\ne0$ podemos dividir por $h$:

$$
\frac{f(a+h)-f(a)}{h}
=
L+\frac{r(h)}{h}.
$$

Como

$$
\frac{r(h)}{h}\longrightarrow0,
$$

obtenemos

$$
\frac{f(a+h)-f(a)}{h}
\longrightarrow L.
$$

Por la definición de derivada,

$$
f'_A(a)=L.
$$

Esto prueba ambas implicaciones. $\square$

### La misma afirmación escrita con cuantificadores

La notación $o(h)$ es compacta, pero no debe ocultar su contenido lógico. Aplicando directamente `#def-t1-0045`, el teorema anterior dice que

$$
f'_A(a)=L
$$

si y solo si

$$
\forall\varepsilon>0\;\exists\delta>0
$$

tal que, para todo $h\in H_a$,

$$
0<|h|<\delta
\quad\Longrightarrow\quad
|f(a+h)-f(a)-Lh|<\varepsilon |h|.
$$

Esta desigualdad merece una lectura pausada.

El término

$$
f(a+h)-f(a)-Lh
$$

es el error que queda después de retirar la variación lineal prevista por $Lh$.

La cota

$$
|f(a+h)-f(a)-Lh|<\varepsilon|h|
$$

dice que podemos hacer ese error menor que **cualquier fracción prescrita de la escala $|h|$**, siempre que observemos suficientemente cerca de $a$.

No estamos afirmando solamente

$$
|f(a+h)-f(a)-Lh|<\varepsilon.
$$

Eso sería un control absoluto. La diferenciabilidad proporciona un control más fuerte y escalado por el propio incremento.

::: {.callout-note title="Continuidad frente a diferenciabilidad"}
La continuidad proporciona

$$
f(a+h)-f(a)\longrightarrow0,
$$

mientras que la diferenciabilidad proporciona la afirmación más fuerte

$$
f(a+h)-f(a)-f'_A(a)h=o(h).
$$

La segunda afirmación contiene información de escala que la primera no posee.
:::

### La tangente aparece ahora como modelo, no solo como pendiente

Si $L=f'_A(a)$, la recta tangente satisface

$$
T_a(a+h)=f(a)+Lh.
$$

Por tanto el residuo es exactamente

$$
r(h)=f(a+h)-T_a(a+h).
$$

El teorema de linealización se convierte en

$$
\boxed{
f(a+h)-T_a(a+h)=o(h).
}
$$

Esta fórmula da un significado preciso a la frase «la tangente aproxima localmente a la gráfica».

No estamos midiendo aquí la distancia euclídea mínima desde un punto de la gráfica hasta la recta. Comparamos los valores de ambas expresiones en la **misma coordenada horizontal** $a+h$. La diferencia vertical, dividida por el tamaño de la escala horizontal, tiende a cero:

$$
\frac{|f(a+h)-T_a(a+h)|}{|h|}
\longrightarrow0.
$$

Así, al observar la función a escalas cada vez menores, la discrepancia entre la gráfica y su modelo tangente se vuelve insignificante frente al propio desplazamiento horizontal.

La misma identidad puede leerse desde las pendientes. Como

$$
f(a+h)-f(a)=Lh+r(h),
$$

para $h\ne0$ tenemos

$$
\frac{f(a+h)-f(a)}{h}
=
L+\frac{r(h)}{h}.
$$

Por tanto

$$
\frac{f(a+h)-f(a)}{h}-L
=
\frac{r(h)}{h}
\longrightarrow0.
$$

La interpretación mediante secantes y la interpretación mediante linealización son, pues, dos lecturas de la misma estructura.

### Un laboratorio exacto con $x^2$

::: {#exm-t1-0070}
**La parábola: el error exacto es $h^2$.** Consideremos

$$
f(x)=x^2
$$

y fijemos $a\in\mathbb R$.

Ya demostramos directamente desde la definición que

$$
f'(a)=2a.
$$

Evaluemos la función en $a+h$:

$$
f(a+h)
=(a+h)^2
=a^2+2ah+h^2.
$$

Como

$$
f(a)=a^2,
$$

obtenemos la descomposición exacta

$$
\boxed{
f(a+h)=f(a)+2ah+h^2.
}
$$

La parte lineal es

$$
2ah=f'(a)h,
$$

y el residuo es

$$
r(h)=h^2.
$$

Ahora

$$
\frac{r(h)}{h}
=
h
\longrightarrow0,
$$

así que

$$
h^2=o(h).
$$

Por tanto

$$
f(a+h)=f(a)+f'(a)h+o(h).
$$

La recta tangente en $a$ es

$$
T_a(x)=a^2+2a(x-a).
$$

Al evaluar en $x=a+h$,

$$
T_a(a+h)=a^2+2ah,
$$

de modo que el error vertical es exactamente

$$
f(a+h)-T_a(a+h)=h^2.
$$

Además,

$$
\frac{|f(a+h)-T_a(a+h)|}{|h|}
=
|h|
\longrightarrow0.
$$

La versión cuantificada también es transparente. Dado $\varepsilon>0$, basta elegir, por ejemplo,

$$
\delta=\varepsilon.
$$

Si $0<|h|<\delta$, entonces

$$
|h^2|
=|h|^2
<\varepsilon|h|.
$$

Así vemos simultáneamente la derivada, la tangente y el control de primer orden del error.
:::

El ejemplo contiene una advertencia importante. Para $x^2$ el residuo $h^2$ es no negativo, de modo que la gráfica queda por encima de su tangente. Esa propiedad particular **no forma parte de la definición de diferenciabilidad** y no debe generalizarse todavía. El estudio sistemático de la forma de las gráficas y de la convexidad pertenece a capítulos posteriores.

### Un test conceptual: ¿es pequeño o es de orden menor?

Consideremos tres posibles residuos:

$$
r_1(h)=h,
\qquad
r_2(h)=h^2,
\qquad
r_3(h)=h|h|.
$$

Los tres tienden a $0$. Pero

$$
\frac{r_1(h)}{h}=1,
$$

mientras que

$$
\frac{r_2(h)}{h}=h\to0
$$

y

$$
\frac{r_3(h)}{h}=|h|\to0.
$$

Por tanto

$$
r_1(h)\ne o(h),
\qquad
r_2(h)=o(h),
\qquad
r_3(h)=o(h).
$$

La pregunta correcta no es solamente

> ¿el residuo se hace pequeño?

sino

> ¿se hace pequeño **en comparación con el incremento**?

Esa segunda pregunta es la que detecta el primer orden.

### La formulación respeta el dominio

Todo el argumento anterior conserva la convención relativa al dominio introducida en §6.2. Si

$$
f\colon A\to\mathbb R,
$$

los incrementos se toman en

$$
H_a=\{h:a+h\in A\}.
$$

Si $a$ es un extremo de un intervalo, quizá solo existan incrementos positivos o solo negativos suficientemente pequeños. La condición

$$
r(h)=o(h)
$$

se interpreta entonces mediante ese acercamiento unilateral permitido por $H_a$.

No necesitamos extender artificialmente la función fuera de su dominio para hablar de linealización relativa.

### Qué hemos ganado al reformular la derivada

La definición original decía

$$
\frac{f(a+h)-f(a)}{h}
\longrightarrow f'_A(a).
$$

Ahora podemos decir exactamente lo mismo de otra manera:

$$
\boxed{
f(a+h)
=
f(a)
+
f'_A(a)h
+
o(h).
}
$$

Esta forma separa tres niveles de información:

$$
\begin{array}{ccl}
f(a) &:& \text{valor de referencia},\\
f'_A(a)h &:& \text{variación lineal de primer orden},\\
o(h) &:& \text{error despreciable frente a la escala }h.
\end{array}
$$

La derivada deja así de ser solamente la pendiente de una recta y aparece como el coeficiente que organiza el comportamiento local de la función hasta primer orden.

Todavía queda una pregunta lógica importante. Si una pendiente $L$ produce un residuo $o(h)$, ¿podría otra pendiente distinta $M$ producir también un residuo $o(h)$?

Responderemos esa pregunta en §6.8. Allí daremos un significado exacto a la afirmación de que la aproximación afín de primer orden es **única**, sin introducir Taylor, mínimos cuadrados ni ninguna teoría posterior.

## Por qué la aproximación de primer orden es única {#sec-t1-c07-08}

En §6.7 vimos que la diferenciabilidad en $a$ puede expresarse mediante una descomposición

$$
f(a+h)=f(a)+Lh+r(h),
\qquad
r(h)=o(h).
$$

La parte $Lh$ recoge la variación de primer orden y el residuo es despreciable frente a $h$. Pero esta formulación deja una pregunta decisiva:

> si una pendiente $L$ produce un error $o(h)$, ¿podría otra pendiente distinta $M$ producir también un error $o(h)$?

Si la respuesta fuese afirmativa, la idea de «aproximación lineal de primer orden» sería ambigua. Una misma función admitiría varias pendientes igualmente válidas a esa escala.

La respuesta es negativa. La pendiente de primer orden está forzada por la función.

### Dos modelos candidatos no pueden sobrevivir a la misma escala

Supongamos que, para los incrementos admisibles $h$ alrededor de $a$, tenemos simultáneamente

$$
f(a+h)=f(a)+Lh+r_L(h)
$$

y

$$
f(a+h)=f(a)+Mh+r_M(h),
$$

con

$$
r_L(h)=o(h)
\qquad\text{y}\qquad
r_M(h)=o(h).
$$

Las dos expresiones describen el mismo número $f(a+h)$. Por tanto podemos restarlas:

$$
Lh+r_L(h)=Mh+r_M(h),
$$

de donde

$$
(L-M)h=r_M(h)-r_L(h).
$$

Mientras $h\ne0$, dividimos por $h$:

$$
L-M
=
\frac{r_M(h)}{h}
-
\frac{r_L(h)}{h}.
$$

Ahora aparece el punto clave. Los dos cocientes de la derecha tienden a $0$. Por álgebra de límites,

$$
L-M=0.
$$

Así,

$$
L=M.
$$

No queda ninguna libertad en el coeficiente lineal.

::: {#thm-t1-0026}
**Unicidad del modelo afín de primer orden.** Sea $f\colon A\to\mathbb R$, sea $a\in A$ un punto de acumulación de $A$ y consideremos los incrementos admisibles

$$
H_a=\{h\in\mathbb R:a+h\in A\}.
$$

Supongamos que existen $L,M\in\mathbb R$ y residuos $r_L,r_M$ tales que, para $h\in H_a$ suficientemente próximo a $0$,

$$
f(a+h)=f(a)+Lh+r_L(h),
\qquad
r_L(h)=o(h),
$$

y

$$
f(a+h)=f(a)+Mh+r_M(h),
\qquad
r_M(h)=o(h).
$$

Entonces

$$
L=M.
$$

En particular, si $f$ es diferenciable en $a$, el único modelo afín de la forma

$$
x\longmapsto f(a)+m(x-a)
$$

cuyo error respecto de $f$ es $o(x-a)$ cuando $x\to a$ dentro de $A$ es

$$
T_a(x)=f(a)+f'_A(a)(x-a).
$$

**Demostración.** Restando las dos representaciones obtenemos

$$
(L-M)h=r_M(h)-r_L(h).
$$

Para todo incremento admisible no nulo suficientemente pequeño,

$$
L-M
=
\frac{r_M(h)}{h}
-
\frac{r_L(h)}{h}.
$$

Como

$$
\frac{r_L(h)}{h}\longrightarrow0
\qquad\text{y}\qquad
\frac{r_M(h)}{h}\longrightarrow0,
$$

el miembro derecho tiende a $0$. El miembro izquierdo es constante, así que necesariamente

$$
L-M=0.
$$

Por tanto $L=M$. $\square$
:::

La prueba contiene una idea que conviene retener: **si elegimos una pendiente incorrecta, el error conserva inevitablemente una parte de tamaño proporcional a $h$**. Esa parte no puede esconderse dentro de un término $o(h)$.

### Qué significa aquí «mejor aproximación»

Ya podemos precisar una expresión frecuente del cálculo: «la tangente es la mejor aproximación lineal de la función cerca del punto».

En este capítulo, la palabra **mejor** no significa que hayamos minimizado una distancia global ni una suma de cuadrados. Tampoco significa que la tangente sea la recta que visualmente parezca ajustarse mejor a una gráfica.

Significa algo exacto:

$$
\boxed{
\text{la tangente es la única recta por }(a,f(a))
\text{ cuyo error es }o(|x-a|).
}
$$

Equivalentemente, entre todas las rectas

$$
P_m(x)=f(a)+m(x-a),
$$

solo una puede satisfacer

$$
\frac{f(x)-P_m(x)}{x-a}\longrightarrow0
\qquad(x\to a,\ x\in A).
$$

Por `#thm-t1-0026`, su pendiente es necesariamente

$$
m=f'_A(a).
$$

::: {.callout-important title="El sentido preciso de mejor"}
No comparamos rectas en todo el dominio.

No medimos un error total sobre un intervalo.

No resolvemos un problema de optimización.

Comparamos el **orden local del error** cuando $x\to a$. La tangente es privilegiada porque elimina toda componente lineal restante del error.
:::

### Qué ocurre si forzamos una pendiente equivocada

Volvamos a la parábola

$$
f(x)=x^2
$$

alrededor de $a$. Sabemos exactamente que

$$
f(a+h)=a^2+2ah+h^2.
$$

La pendiente correcta es $2a$. Supongamos, en cambio, que intentamos usar

$$
m=2a+c,
$$

con $c\ne0$.

El modelo propuesto sería

$$
a^2+(2a+c)h.
$$

Su residuo exacto es

$$
\begin{aligned}
r_c(h)
&=f(a+h)-a^2-(2a+c)h\\
&=h^2-ch.
\end{aligned}
$$

Este error sí tiende a $0$ cuando $h\to0$. Pero eso no basta. Dividiendo por $h$,

$$
\frac{r_c(h)}{h}=h-c\longrightarrow-c\ne0.
$$

Por tanto

$$
r_c(h)\ne o(h).
$$

La pendiente equivocada deja una huella lineal $-ch$ que sobrevive exactamente a la escala de primer orden.

Este cálculo muestra por qué la condición $o(h)$ es mucho más discriminante que pedir simplemente que el error tienda a cero.

### Mismo primer orden, errores diferentes

La unicidad del coeficiente lineal no significa que dos funciones con el mismo primer orden deban ser iguales. Pueden diferir en términos que sean pequeños frente a $h$.

::: {#exm-t1-0071}
**Dos funciones indistinguibles a primer orden, con residuos distintos.** Consideremos

$$
f(x)=x+x^2
$$

y

$$
g(x)=x+x|x|.
$$

En $a=0$ ambas toman el mismo valor:

$$
f(0)=g(0)=0.
$$

Además, para un incremento $h$,

$$
f(h)=h+h^2
$$

y

$$
g(h)=h+h|h|.
$$

Ahora

$$
\frac{h^2}{h}=h\longrightarrow0
$$

y

$$
\frac{h|h|}{h}=|h|\longrightarrow0.
$$

Por tanto

$$
h^2=o(h)
\qquad\text{y}\qquad
h|h|=o(h).
$$

Las dos funciones admiten así la misma linealización de primer orden:

$$
f(h)=h+o(h),
$$

$$
g(h)=h+o(h).
$$

Por `#thm-t1-0025`, ambas son diferenciables en $0$ y

$$
f'(0)=g'(0)=1.
$$

Sin embargo, sus residuos no son iguales:

$$
h^2\ne h|h|
$$

para $h<0$.

La derivada detecta el comportamiento de primer orden, pero no registra toda la información de escalas menores.
:::

Este ejemplo permite formular una consecuencia general sin introducir nueva notación formal. Si $f,g:A\to\mathbb R$ son diferenciables en $a$ respecto de un mismo dominio $A$, con $a$ punto de acumulación de $A$, y

$$
f(a)=g(a),
\qquad
f'(a)=g'(a)=L,
$$

entonces podemos escribir

$$
f(a+h)=f(a)+Lh+r_f(h)
$$

y

$$
g(a+h)=g(a)+Lh+r_g(h),
$$

con

$$
\frac{r_f(h)}{h}\to0,
\qquad
\frac{r_g(h)}{h}\to0.
$$

Restando,

$$
f(a+h)-g(a+h)=r_f(h)-r_g(h).
$$

Y al dividir por $h$,

$$
\frac{f(a+h)-g(a+h)}{h}
=
\frac{r_f(h)}{h}
-
\frac{r_g(h)}{h}
\longrightarrow0.
$$

En este sentido preciso, dos funciones con el mismo valor y la misma derivada en un punto son **indistinguibles a primer orden** alrededor de ese punto.

Eso no significa que sean iguales cerca de $a$. Significa que su diferencia es demasiado pequeña, comparada con $|h|$, para ser detectada en la escala lineal.

### El residuo puede contener información que todavía no estamos clasificando

En `#exm-t1-0071` aparecieron dos residuos distintos:

$$
h^2
\qquad\text{y}\qquad
h|h|.
$$

Ambos son $o(h)$. Para la teoría de este capítulo eso es suficiente: los dos pertenecen a una escala menor que la lineal.

Podríamos intentar distinguir entre residuos cuadráticos, cúbicos o de otros órdenes. Esa pregunta es legítima, pero todavía no corresponde desarrollarla sistemáticamente. Las derivadas superiores y la fórmula de Taylor aparecerán más adelante.

Aquí la frontera conceptual es deliberada:

$$
\boxed{
\text{primer orden}
=
\text{parte lineal única}
+
\text{resto }o(h).
}
$$

No necesitamos clasificar más finamente el resto para comprender qué significa ser diferenciable.

### Una aproximación numérica que no usa Taylor

La linealización puede producir aproximaciones numéricas aun antes de disponer de una teoría general de Taylor. Pero debemos distinguir con cuidado entre una aproximación respaldada por una identidad exacta y una regla general de estimación del error.

Para

$$
f(x)=x^2
$$

alrededor de $a=3$, la identidad exacta es

$$
(3+h)^2=9+6h+h^2.
$$

La parte de primer orden es

$$
9+6h.
$$

Si queremos aproximar

$$
(3.01)^2,
$$

tomamos $h=0.01$ y obtenemos

$$
9+6(0.01)=9.06.
$$

La identidad exacta muestra que el error es

$$
h^2=0.0001,
$$

de modo que

$$
(3.01)^2=9.0601.
$$

Aquí no hemos usado Taylor ni el teorema del valor medio. Conocíamos de antemano el residuo exacto $h^2$.

En una función diferenciable arbitraria, la información

$$
f(a+h)=f(a)+f'(a)h+o(h)
$$

garantiza que el error es pequeño **relativamente a $|h|$**, pero por sí sola no proporciona una fórmula numérica universal para ese error. Obtener cotas más explícitas requerirá herramientas adicionales.

### Qué hemos demostrado realmente

La cadena lógica de §§6.7–6.8 puede resumirse así:

$$
\boxed{
\begin{array}{c}
f\text{ diferenciable en }a\\[2mm]
\Downarrow\\[2mm]
f(a+h)=f(a)+f'_A(a)h+o(h)\\[2mm]
\Downarrow\\[2mm]
\text{la parte lineal de primer orden es única.}
\end{array}
}
$$

Por eso la derivada no es solo **una** pendiente compatible con el comportamiento local. Es **la única pendiente** que deja un error despreciable frente al incremento.

La noción de tangente, la derivada y la linealización quedan ahora unificadas:

$$
\boxed{
\text{derivada}
\Longleftrightarrow
\text{pendiente tangente}
\Longleftrightarrow
\text{coeficiente lineal único de primer orden}.
}
$$

En §6.9 volveremos a mirar $f'$ ya no solo como un valor asociado a un punto, sino como una nueva función definida sobre el conjunto de puntos donde $f$ es diferenciable. Allí formalizaremos además una propiedad que hemos usado intuitivamente desde el comienzo: **la derivada es un concepto local**.


## La derivada como función y la localidad del concepto {#sec-t1-c07-09}

Hasta ahora hemos usado la notación $f'(a)$ para describir un número asociado a un punto concreto. Pero, si repetimos la misma pregunta en muchos puntos del dominio, obtenemos algo nuevo: una función cuyos valores son precisamente esas derivadas.

Esta transición parece pequeña,

$$
a
\longmapsto
f'(a),
$$

pero cambia la escala de nuestras preguntas. Ya no preguntamos solamente

> ¿cuál es la derivada de $f$ en este punto?

sino también

> ¿en qué puntos existe la derivada y cómo se comportan entre sí los valores obtenidos?

La primera pregunta sigue siendo puntual. La segunda empieza a mirar la derivada como un objeto funcional.

### Del valor $f'(a)$ a la función $f'$

En §6.2 definimos el conjunto

$$
\operatorname{Dom}(f')
=
\left\{
a\in A:
a\text{ es punto de acumulación de }A
\text{ y }f'_A(a)\text{ existe como número real}
\right\}.
$$

Cuando este conjunto no es vacío, podemos reunir todos los valores de la derivada en la aplicación

$$
f'\colon \operatorname{Dom}(f')\to\mathbb R,
\qquad
a\longmapsto f'_A(a).
$$

Conviene detenerse en el dominio. En general,

$$
\operatorname{Dom}(f')
\subseteq A,
$$

y la inclusión puede ser estricta.

Que $f$ esté definida en un punto no significa que sea diferenciable allí. El ejemplo de $|x|$ en $0$ ya mostró exactamente esa diferencia.

Por eso hay tres objetos que no debemos confundir:

$$
\boxed{
A,
\qquad
\operatorname{Dom}(f'),
\qquad
f'.
}
$$

El primero es el dominio de la función original. El segundo selecciona los puntos donde existe una derivada real finita según nuestra definición. El tercero asigna a cada uno de esos puntos el número correspondiente.

Cuando digamos que $f$ es **diferenciable en un conjunto** $E\subseteq A$, entenderemos simplemente que

$$
E\subseteq \operatorname{Dom}(f').
$$

Esta convención no añade una nueva teoría: abrevia una afirmación punto por punto.

### La derivada solo mira lo que ocurre cerca del punto

La definición de derivada está escrita mediante un límite. Y los límites poseen una propiedad fundamental que ya conocemos: cambiar una función lejos del punto de estudio no altera su límite en ese punto.

La misma idea debe heredarse por la derivada.

Supongamos que queremos decidir qué ocurre en $a$. El cociente incremental solo utiliza

$$
f(a)
$$

y valores

$$
f(x)
$$

para $x$ arbitrariamente próximo a $a$.

Por tanto, lo que haga la función lejos de $a$ no debería importar.

Esta intuición se formaliza en la siguiente proposición.

::: {#prp-t1-0038}
**Localidad de la derivada.** Sean

$$
f,g\colon A\to\mathbb R
$$

y sea $a\in A$ un punto de acumulación de $A$.

Supongamos que existe $\delta_0>0$ tal que

$$
x\in A,
\qquad
|x-a|<\delta_0
\Longrightarrow
f(x)=g(x).
$$

Entonces

$$
f\text{ es diferenciable en }a
\iff
g\text{ es diferenciable en }a.
$$

Cuando estas condiciones se cumplen,

$$
f'_A(a)=g'_A(a).
$$

**Demostración.** Como $a\in A$ y $|a-a|=0<\delta_0$, la hipótesis implica primero que

$$
f(a)=g(a).
$$

Además, si

$$
x\in A,
\qquad
0<|x-a|<\delta_0,
$$

entonces

$$
f(x)=g(x).
$$

Por tanto, en ese entorno perforado relativo al dominio,

$$
\frac{f(x)-f(a)}{x-a}
=
\frac{g(x)-g(a)}{x-a}.
$$

Los dos cocientes incrementales coinciden para todos los puntos de $A$ suficientemente próximos a $a$, salvo el propio centro.

Por la localidad del límite, uno de estos cocientes posee un límite real cuando $x\to a$ dentro de $A$ si y solo si el otro lo posee, y en tal caso ambos límites son iguales.

Así,

$$
f'_A(a)
=
\lim_{\substack{x\to a\\x\in A}}
\frac{f(x)-f(a)}{x-a}
=
\lim_{\substack{x\to a\\x\in A}}
\frac{g(x)-g(a)}{x-a}
=
g'_A(a).
$$

Esto prueba simultáneamente la equivalencia de la diferenciabilidad y la igualdad de las derivadas. $\square$
:::

La arquitectura de la prueba es corta porque toda la carga conceptual ya estaba contenida en la teoría de límites:

$$
\boxed{
\text{coincidencia local de }f\text{ y }g
\Longrightarrow
\text{coincidencia local de cocientes}
\Longrightarrow
\text{mismo límite}.
}
$$

La derivada es, por tanto, una propiedad genuinamente **local**.

### Local no significa «solo importa el entorno perforado»

Hay una sutileza importante en la proposición anterior. Pedimos que $f$ y $g$ coincidan en un entorno de $a$ **incluido el valor en el centro**.

No basta con que coincidan para $x\ne a$.

Consideremos

$$
f(x)=x
$$

para todo $x\in\mathbb R$ y definamos

$$
g(x)=
\begin{cases}
x, & x\ne0,\\
1, & x=0.
\end{cases}
$$

Las funciones coinciden en todo punto distinto de $0$. Sin embargo,

$$
f(0)=0
\qquad\text{y}\qquad
g(0)=1.
$$

Para $f$, el cociente incremental en $0$ es

$$
\frac{f(h)-f(0)}{h}
=
\frac{h}{h}
=
1,
\qquad h\ne0,
$$

de modo que

$$
f'(0)=1.
$$

Para $g$,

$$
\frac{g(h)-g(0)}{h}
=
\frac{h-1}{h}
=
1-\frac1h,
\qquad h\ne0,
$$

y esta expresión no posee límite real cuando $h\to0$.

Así, modificar solamente el valor central puede destruir la diferenciabilidad.

La palabra **local** significa que solo importa lo que ocurre en algún entorno suficientemente pequeño del punto; no significa que podamos olvidar el propio valor $f(a)$.

### Un uso inmediato: reconstruir la derivada de $|x|$ fuera de la esquina

La localidad permite obtener información sin desarrollar todavía reglas generales de derivación.

Consideremos

$$
f(x)=|x|.
$$

Ya sabemos que $f$ no es diferenciable en $0$.

Tomemos ahora un punto

$$
a>0.
$$

Podemos elegir, por ejemplo,

$$
\delta=\frac a2.
$$

Si $|x-a|<\delta$, entonces

$$
x>a-\frac a2=\frac a2>0.
$$

En ese entorno,

$$
|x|=x.
$$

Por localidad, $|x|$ tiene en $a$ la misma derivada que la función afín $x\mapsto x$. Como esta última tiene derivada $1$ desde la definición,

$$
f'(a)=1
\qquad(a>0).
$$

Análogamente, si

$$
a<0,
$$

podemos elegir un entorno suficientemente pequeño contenido en $(-\infty,0)$. Allí

$$
|x|=-x,
$$

y por localidad

$$
f'(a)=-1
\qquad(a<0).
$$

Junto con la no diferenciabilidad en $0$, obtenemos

$$
\operatorname{Dom}(f')
=
\mathbb R\setminus\{0\}
$$

y

$$
f'(x)
=
\begin{cases}
-1, & x<0,\\
1, & x>0.
\end{cases}
$$

No hemos usado una regla de derivación para el valor absoluto. Hemos usado únicamente:

1. derivadas de funciones afines ya calculadas desde la definición;
2. la igualdad local de las funciones;
3. `#prp-t1-0038`.

Este ejemplo muestra para qué sirve pensar en la derivada como función: podemos preguntar simultáneamente por su dominio y por sus valores.

### «$f$ es diferenciable» y «$f'$ es continua» son afirmaciones distintas

Una vez que aparece la función derivada, surge una tentación natural: mezclar la existencia de $f'$ con la continuidad de $f'$.

Son preguntas diferentes.

Afirmar que $f$ es diferenciable en un punto $a$ significa estudiar el límite

$$
\lim_{\substack{x\to a\\x\in A}}
\frac{f(x)-f(a)}{x-a}.
$$

En cambio, preguntar si **$f'$ es continua en $a$** significa aplicar la definición de continuidad relativa al dominio $\operatorname{Dom}(f')$. Cuando

$$
a\in\operatorname{Dom}(f')
$$

es además punto de acumulación de ese dominio, esto equivale a estudiar otro límite:

$$
\lim_{\substack{x\to a\\x\in\operatorname{Dom}(f')}}
f'(x)
$$

y compararlo con

$$
f'(a).
$$

Las dos preguntas operan en niveles distintos:

$$
\boxed{
\begin{array}{ccl}
f\text{ diferenciable en }a
&:&
\text{comportamiento de }f\text{ a primer orden en }a,\\[1mm]
f'\text{ continua en }a
&:&
\text{comportamiento de las derivadas en puntos próximos a }a.
\end{array}
}
$$

Que $f'(a)$ exista nos entrega **un valor** de la función derivada. No establece por sí solo cómo se relaciona ese valor con $f'(x)$ cuando $x$ varía.

En este capítulo no supondremos ni utilizaremos que la existencia de la derivada implique continuidad de la función derivada. Tampoco introduciremos todavía una clasificación sistemática de funciones según la regularidad de $f'$.

Eso pertenece a una capa posterior de la teoría.

::: {.callout-warning title="Dos errores de nivel"}
De

$$
f'(a)>0
$$

no podemos concluir que

$$
f'(x)>0
$$

para todos los $x$ cercanos a $a$.

La primera afirmación habla de **un solo valor** de la función derivada. Para transferir información de $f'(a)$ a valores vecinos de $f'$ necesitaríamos hipótesis adicionales.

Y aun una afirmación sobre el signo de $f'$ en muchos puntos no debe convertirse todavía, sin prueba, en un teorema global de monotonía. Esa conexión será establecida más adelante mediante los teoremas del valor medio.
:::

Esta distinción es importante porque evita convertir la notación $f'$ en una caja negra. Primero existe una derivada punto por punto; solo después podemos estudiar propiedades de la nueva función formada por esos valores.

### La localidad también fija una estrategia de cálculo

La proposición de localidad no es solamente un dato teórico. Sugiere una estrategia reutilizable.

Para calcular una derivada en $a$, podemos preguntar:

> ¿coincide la función, en algún entorno de $a$, con otra función cuyo comportamiento diferencial ya conocemos?

Si la respuesta es afirmativa, no necesitamos analizar la fórmula global.

Por ejemplo, una función por tramos puede tener una expresión complicada lejos de $a$ y, sin embargo, coincidir cerca de $a$ con una función afín. En tal caso, la derivada en $a$ queda determinada por ese tramo local.

Esto explica por qué una modificación remota de la gráfica no cambia la tangente ni la linealización en el punto.

Podemos resumir la idea como

$$
\boxed{
\text{la derivada en }a
\text{ depende del germen local de la función en }a,
\text{ no de su comportamiento global}.
}
$$

No necesitamos formalizar aquí la palabra *germen*. La frase expresa solamente la propiedad probada en `#prp-t1-0038`: dos funciones que coinciden en un entorno del punto son indistinguibles para la derivada en ese punto.

### Qué queda fuera de esta sección

La aparición de la función $f'$ abre varias preguntas que deliberadamente no resolveremos todavía.

En `T1-C08` desarrollaremos las reglas que permiten construir nuevas derivadas a partir de derivadas conocidas:

- suma y escalares;
- producto;
- cociente;
- regla de la cadena.

En `T1-C09` estudiaremos sistemáticamente derivadas de funciones elementales, inversas e implícitas.

En `T1-C10` aparecerán Rolle y los teoremas del valor medio, que conectarán información sobre la derivada con el comportamiento de la función a lo largo de un intervalo.

Y las derivadas superiores pertenecen a capítulos posteriores.

La frontera actual puede escribirse así:

$$
\boxed{
\begin{array}{c}
\text{C07: qué es }f'(a),\text{ qué información local contiene y cómo se organiza en }f'\\[1mm]
\Downarrow\\[1mm]
\text{C08--C10: cómo calcular }f'\text{ sistemáticamente y qué consecuencias globales produce.}
\end{array}
}
$$

### Cierre conceptual

Durante las primeras secciones del capítulo, la derivada apareció como un límite de pendientes secantes. Después se convirtió en pendiente tangente y, finalmente, en el coeficiente único de la aproximación de primer orden.

Ahora añadimos una última perspectiva:

$$
\boxed{
f'
\text{ es una nueva función, pero cada uno de sus valores se determina localmente.}
}
$$

La cadena conceptual queda ampliada:

$$
\boxed{
\text{cociente incremental}
\to
\text{derivada en un punto}
\to
\text{tangente}
\to
\text{linealización}
\to
\text{unicidad de primer orden}
\to
\text{función derivada y localidad}.
}
$$

Con esto la teoría básica de C07 está conceptualmente construida. Antes de pasar al banco de ejercicios, §6.10 funcionará como laboratorio de reconstrucción: no añadirá teoría nueva, sino que obligará a reconocer qué razonamientos producen realmente cada una de las ideas desarrolladas en el capítulo.


## Laboratorio: reconstruir el pensamiento diferencial {#sec-t1-c07-10}

La teoría básica de este capítulo ya está construida. Sabemos pasar de secantes a cocientes incrementales, definir la derivada como límite, diagnosticar fallos laterales, obtener la tangente, expresar la diferenciabilidad como aproximación de primer orden y reconocer que la derivada es local.

Pero conocer una lista de resultados no garantiza todavía que sepamos **reconstruir el pensamiento que los produce**.

Ése es el objetivo de este laboratorio.

No introduciremos teoría nueva. Tampoco añadiremos fórmulas para memorizar. Trabajaremos, en cambio, sobre ocho movimientos cognitivos que deberían poder recuperarse incluso si olvidáramos temporalmente los enunciados del capítulo.

La pregunta que gobernará toda la sección es:

$$
\boxed{
\text{si desaparecieran las fórmulas de nuestras notas, ¿podríamos volver a construir la idea de derivada?}
}
$$

Cada estación tendrá tres momentos:

1. **reconstrucción**: partir de una pregunta y producir el objeto matemático necesario;
2. **auditoría**: localizar el paso lógico delicado;
3. **autoexplicación**: formular con palabras propias qué se ha aprendido y qué no se ha demostrado.

La meta no es rapidez. La meta es que el mecanismo conceptual quede disponible para problemas nuevos.

### Estación 1 — Reconstruir la derivada desde una familia de secantes

Supongamos que olvidamos por un momento la definición formal de derivada. Conservemos únicamente una pregunta geométrica:

> ¿cómo describir la inclinación local de la gráfica de $f$ en el punto $(a,f(a))$?

Con un solo punto no podemos calcular una pendiente. Necesitamos un segundo punto de la gráfica. Tomemos

$$
(a+h,f(a+h)),
\qquad h\ne0.
$$

La pendiente de la secante que une ambos puntos es

$$
\frac{f(a+h)-f(a)}{h}.
$$

Hasta aquí no hay derivada. Hay una **familia de pendientes**, una para cada incremento admisible $h\ne0$.

El siguiente movimiento intelectual consiste en reducir la escala. Queremos que el segundo punto se acerque al primero, pero sin hacerlo coincidir con él mientras calculamos la pendiente. Por eso preguntamos por el comportamiento de

$$
\frac{f(a+h)-f(a)}{h}
$$

cuando

$$
h\to0.
$$

Si las pendientes secantes se estabilizan alrededor de un único número real $L$, ese número contiene precisamente la información local que buscábamos.

La reconstrucción completa es entonces

$$
\boxed{
\begin{array}{c}
\text{dos puntos de la gráfica}\\[1mm]
\Downarrow\\[1mm]
\text{pendiente secante}\\[1mm]
\Downarrow\\[1mm]
\text{segundo punto se aproxima al primero}\\[1mm]
\Downarrow\\[1mm]
\text{límite de pendientes}\\[1mm]
\Downarrow\\[1mm]
\text{derivada, si el límite real existe}.
\end{array}
}
$$

Obsérvese que la definición no aparece como una convención arbitraria. Es la respuesta rigurosa a un problema previo.

::: {.callout-note title="Autoexplicación"}
Sin mirar la definición de §6.2, intenta responder:

- ¿por qué aparecen **dos** valores de la función en el numerador?;
- ¿por qué dividimos por el incremento de entrada?;
- ¿por qué $h$ debe ser distinto de $0$ durante el cálculo?;
- ¿por qué finalmente hacemos $h\to0$?;
- ¿por qué exigimos un límite **real finito**?

Si puedes reconstruir esas cinco respuestas, la fórmula deja de ser una pieza aislada de memoria.
:::

La misma arquitectura puede leerse sin geometría. Si $f$ representa una magnitud que cambia con el tiempo, el mismo cociente mide una tasa media y el límite busca una tasa instantánea. El objeto matemático es el mismo; cambia únicamente la interpretación.

### Estación 2 — Separar continuidad, derivabilidad y derivadas laterales

Uno de los errores más frecuentes consiste en tratar continuidad, derivabilidad y existencia de derivadas laterales como si fueran tres nombres para una misma propiedad.

No lo son.

La continuidad en $a$ pregunta si

$$
f(x)\to f(a)
\qquad(x\to a).
$$

La derivabilidad pregunta si el cambio de la función, después de dividirse por la escala $x-a$, posee un límite real finito:

$$
\frac{f(x)-f(a)}{x-a}
\longrightarrow L.
$$

Las derivadas laterales, cuando el dominio acumula por ambos lados, separan ese segundo problema en dos procesos:

$$
x\to a^-
\qquad\text{y}\qquad
x\to a^+.
$$

La relación lógica correcta puede organizarse así:

$$
\boxed{
\text{derivabilidad}
\Longrightarrow
\text{continuidad},
}
$$

pero la conversa es falsa.

Además, en un punto interior con aproximación desde ambos lados,

$$
\boxed{
\text{derivabilidad bilateral}
\Longleftrightarrow
\text{derivadas laterales finitas existentes e iguales}.
}
$$

El valor absoluto en $0$ sigue siendo el laboratorio más económico. La función

$$
f(x)=|x|
$$

es continua en $0$, porque

$$
|x|\to0.
$$

Sin embargo, los cocientes laterales son

$$
\frac{|h|}{h}
=
\begin{cases}
-1,&h<0,\\
1,&h>0.
\end{cases}
$$

Cada lado tiene un límite real, pero los dos límites son distintos. Por tanto la continuidad no basta para fabricar una derivada.

Podemos comparar varios mecanismos ya vistos:

| Comportamiento en el punto | Continuidad | Laterales del cociente | Derivada real bilateral |
|---|---|---|---|
| $x^2$ en $0$ | sí | existen y coinciden | sí |
| $|x|$ en $0$ | sí | existen, pero difieren | no |
| $x\sin(1/x)$ en $0$, con valor $0$ | sí | el cociente oscila | no |
| pendiente que crece sin cota | puede haber continuidad | no hay límite lateral real finito | no |

La tabla no sustituye las definiciones. Su función es mostrar que distintos fallos deben diagnosticarse con distintas preguntas.

::: {.callout-important title="Orden de diagnóstico"}
Ante un punto problemático, no preguntes primero «¿es derivable?». Descompón el problema:

1. ¿el punto pertenece al dominio y es punto de acumulación?;
2. ¿la función es continua allí?;
3. ¿qué ocurre con el cociente por cada lado disponible?;
4. ¿los límites laterales son reales finitos?;
5. si existen ambos, ¿coinciden?

Este orden evita confundir discontinuidad, esquina, pendiente no acotada y oscilación.
:::

En un extremo del dominio, la auditoría cambia: solo exigimos la dirección desde la cual el dominio realmente se aproxima al punto. La geometría del dominio forma parte del problema.

### Estación 3 — Por qué no se evalúa el cociente incremental en $h=0$

Consideremos otra vez el cociente

$$
Q(h)=\frac{f(a+h)-f(a)}{h}.
$$

El impulso de «sustituir $h=0$» produce

$$
\frac{f(a)-f(a)}0,
$$

que no está definido.

El error no consiste solamente en haber obtenido una división por cero. Es más profundo: se está confundiendo **evaluación** con **límite**.

La derivada no pregunta por el valor de $Q$ en $0$. Pregunta por el comportamiento de $Q(h)$ para incrementos no nulos arbitrariamente pequeños.

La distinción es exactamente la misma que ya utilizamos en teoría de límites:

$$
\boxed{
\text{valor en el centro}
\neq
\text{comportamiento cuando nos aproximamos al centro}.
}
$$

Por eso una expresión puede no estar definida en $h=0$ y, sin embargo, poseer un límite perfectamente determinado cuando $h\to0$.

Para la parábola,

$$
Q(h)
=
\frac{(a+h)^2-a^2}{h},
\qquad h\ne0.
$$

No necesitamos asignar ningún valor al cociente original en $h=0$. Toda la información relevante vive en el entorno perforado.

::: {.callout-warning title="Diagnóstico del error"}
La frase

> «para hallar la derivada pongo $h=0$»

es incorrecta.

La frase correcta es

> «estudio valores con $h\ne0$ y determino si el cociente posee un límite cuando $h$ se aproxima a $0$».
:::

La diferencia entre ambas frases contiene buena parte de la lógica del cálculo.

### Estación 4 — Cancelar $h$: qué estamos haciendo realmente

En el ejemplo de $x^2$ aparece

$$
\frac{(a+h)^2-a^2}{h}
=
\frac{2ah+h^2}{h}.
$$

Factorizamos:

$$
\frac{h(2a+h)}{h}.
$$

Y cancelamos $h$ para obtener

$$
2a+h.
$$

¿Por qué es legítima la cancelación si después queremos hacer $h\to0$?

Porque durante la cancelación estamos trabajando bajo la hipótesis

$$
h\ne0.
$$

La igualdad exacta es

$$
\frac{(a+h)^2-a^2}{h}
=
2a+h
\qquad\text{para todo }h\ne0.
$$

No hemos demostrado que las dos expresiones sean la misma función en $h=0$. De hecho, la primera ni siquiera está definida allí.

Lo que hemos demostrado es algo suficiente para los límites: **coinciden en un entorno perforado de $0$**.

Como el límite solo inspecciona valores arbitrariamente próximos al centro y no exige usar el valor central, podemos reemplazar una expresión por la otra al calcular el límite.

La cadena correcta es

$$
\boxed{
\begin{array}{c}
h\ne0\text{ porque estamos en el dominio perforado}\\[1mm]
\Downarrow\\[1mm]
\text{cancelación algebraica legítima}\\[1mm]
\Downarrow\\[1mm]
Q(h)=2a+h\text{ para }h\ne0\text{ cercano a }0\\[1mm]
\Downarrow\\[1mm]
\lim_{h\to0}Q(h)=2a.
\end{array}
}
$$

El límite no vuelve retroactivamente ilegal la cancelación. Al contrario: la teoría de límites está diseñada precisamente para permitir que trabajemos en dominios perforados.

::: {.callout-note title="Pregunta de control"}
¿Qué afirmación es más precisa?

1. «Cancelamos $h$ y luego ponemos $h=0$.»
2. «Para $h\ne0$ simplificamos el cociente; después calculamos el límite de la expresión equivalente en el entorno perforado.»

La segunda. En ella no aparece ninguna división por cero ni ninguna sustitución ilegítima.
:::

### Estación 5 — La simetría no puede sustituir la derivada ordinaria

Alguien podría proponer un atajo. En vez de estudiar

$$
\frac{f(a+h)-f(a)}{h},
$$

podría comparar puntos simétricos alrededor de $a$ y formar

$$
\frac{f(a+h)-f(a-h)}{2h}.
$$

Esta expresión puede ser útil en otros contextos, pero **no puede reemplazar nuestra definición de derivada**.

El valor absoluto muestra por qué.

Tomemos

$$
f(x)=|x|
$$

en $a=0$. Para $h\ne0$,

$$
\frac{f(h)-f(-h)}{2h}
=
\frac{|h|-|-h|}{2h}
=
0.
$$

Así, el cociente simétrico tiene el límite

$$
0.
$$

Sin embargo, ya sabemos que la derivada ordinaria de $|x|$ en $0$ no existe, porque

$$
\lim_{h\to0^-}\frac{|h|}{h}=-1
\qquad\text{y}\qquad
\lim_{h\to0^+}\frac{|h|}{h}=1.
$$

¿Qué ocurrió?

El cociente simétrico combinó información de ambos lados de una manera que hizo desaparecer la incompatibilidad. Las dos pendientes laterales $-1$ y $1$ se compensaron en la comparación simétrica.

Pero la derivada ordinaria exige algo más fuerte: que **cada** cociente incremental, para todos los incrementos admisibles suficientemente pequeños, se aproxime al mismo número.

Por eso

$$
\boxed{
\text{estabilización de un promedio simétrico}
\not\Longrightarrow
\text{existencia de la derivada ordinaria}.
}
$$

::: {.callout-important title="Prueba de estrés de una definición"}
Cuando aparezca una propuesta alternativa para definir un concepto, no preguntes solo si funciona en funciones suaves. Pruébala contra un caso límite conocido.

Aquí $|x|$ cumple esa función: conserva suficiente simetría para engañar al cociente propuesto, pero mantiene una esquina que la derivada ordinaria debe detectar.
:::

Este ejercicio de diagnóstico es más general que el caso concreto: una definición adecuada debe distinguir los fenómenos que la teoría pretende distinguir.

### Estación 6 — ¿Qué dice exactamente $r(h)=o(h)$?

La notación

$$
r(h)=o(h)
\qquad(h\to0)
$$

puede parecer una etiqueta sofisticada si se memoriza sin abrirla. Su contenido es únicamente

$$
\frac{r(h)}{h}\to0.
$$

La idea no es simplemente que

$$
r(h)\to0.
$$

Eso sería demasiado débil. También

$$
r(h)=3h
$$

tiende a $0$, pero

$$
\frac{r(h)}h=3,
$$

por lo que $3h$ **no** es $o(h)$.

La condición $o(h)$ compara dos escalas. Dice que el error $r(h)$ se vuelve despreciable **respecto de la escala lineal $h$**.

Podemos auditar algunos casos:

$$
r(h)=h^2
\quad\Longrightarrow\quad
\frac{r(h)}h=h\to0,
$$

así que

$$
h^2=o(h).
$$

También

$$
r(h)=h|h|
\quad\Longrightarrow\quad
\frac{r(h)}h=|h|\to0,
$$

por lo que

$$
h|h|=o(h).
$$

En cambio,

$$
r(h)=|h|
$$

no satisface la condición bilateral, porque

$$
\frac{|h|}{h}
=
\begin{cases}
-1,&h<0,\\
1,&h>0.
\end{cases}
$$

La pregunta correcta ante cualquier candidato es, por tanto:

$$
\boxed{
\text{¿qué ocurre con }\frac{r(h)}h\text{ cuando }h\to0?
}
$$

Esta lectura permite recuperar la linealización sin memorizarla. Si $f$ es diferenciable en $a$ con derivada $L$, la afirmación

$$
f(a+h)=f(a)+Lh+o(h)
$$

dice que, después de restar el valor central y el término lineal principal, lo que queda es pequeño **en comparación con $h$**.

Equivalentemente, para tolerancias arbitrarias,

$$
|f(a+h)-f(a)-Lh|
<
\varepsilon|h|
$$

cuando $h$ es suficientemente pequeño y admisible.

::: {.callout-note title="Autoexplicación"}
Completa mentalmente la frase:

> «El error tiende a cero» no basta para ser de orden menor que $h$, porque...

La respuesta esencial es: **debemos comparar el error con $h$ dividiendo por $h$**. Solo si esa razón tiende a $0$ el error es despreciable a escala lineal.
:::

### Estación 7 — Reconstruir diferenciabilidad $\Rightarrow$ continuidad

Supongamos que hemos olvidado la demostración del teorema, pero recordamos las dos definiciones.

Queremos probar continuidad en $a$. Eso significa que debemos lograr

$$
f(x)-f(a)\to0.
$$

¿Qué información entrega la diferenciabilidad?

Nos dice que

$$
\frac{f(x)-f(a)}{x-a}
\to
f'(a),
$$

con un límite real finito.

Ahora hay que encontrar un puente entre ambas expresiones. Para $x\ne a$,

$$
f(x)-f(a)
=
(x-a)
\frac{f(x)-f(a)}{x-a}.
$$

La estructura de la prueba aparece por sí sola:

- el primer factor tiende a $0$;
- el segundo factor tiende al número real $f'(a)$;
- por el álgebra de límites, el producto tiende a $0$.

Por tanto,

$$
f(x)-f(a)\to0,
$$

y de ahí

$$
f(x)\to f(a).
$$

La continuidad ha sido reconstruida.

El punto delicado vuelve a ser el dominio perforado. La identidad de factorización se escribe para

$$
x\ne a,
$$

pero eso es exactamente lo que necesita un límite. No existe ninguna laguna al no usar el centro durante la factorización.

Podemos reconstruir el mismo razonamiento con la linealización. Si

$$
f(a+h)-f(a)=f'(a)h+r(h),
\qquad
r(h)=o(h),
$$

entonces

$$
f'(a)h\to0
$$

y, como $r(h)/h\to0$, también $r(h)=h\,(r(h)/h)\to0$. Así la variación total tiende a $0$.

Las dos pruebas son lecturas diferentes de una misma idea:

$$
\boxed{
\text{diferenciabilidad controla la variación a una escala más fina que la continuidad}.
}
$$

::: {.callout-important title="Reconstrucción, no recitación"}
Si olvidas la prueba, no intentes recordar una secuencia de líneas. Pregunta:

1. ¿cuál es el objetivo de continuidad?;
2. ¿qué expresión controla la diferenciabilidad?;
3. ¿cómo puedo transformar una en la otra?

La factorización surge entonces como una necesidad lógica, no como un truco que debamos memorizar.
:::

Y la conversa sigue siendo falsa: $|x|$ es continua en $0$ pero no diferenciable allí. La diferencia entre necesidad y suficiencia debe permanecer visible.

### Estación 8 — De $f'(a)>0$ a información puntual, no a monotonía

Supongamos ahora que

$$
f'(a)>0.
$$

¿Qué podemos concluir **solo** desde la definición?

Como

$$
\frac{f(a+h)-f(a)}h
\longrightarrow
f'(a),
$$

podemos elegir una tolerancia menor que el propio valor límite. Por ejemplo,

$$
\varepsilon=\frac{f'(a)}2.
$$

Para $h$ suficientemente pequeño, no nulo y admisible,

$$
\left|
\frac{f(a+h)-f(a)}h-f'(a)
\right|
<
\frac{f'(a)}2.
$$

De aquí se obtiene

$$
\frac{f(a+h)-f(a)}h
>
\frac{f'(a)}2
>
0.
$$

Ésta es una conclusión rigurosa.

Si $h>0$, entonces

$$
f(a+h)>f(a).
$$

Si $h<0$, al multiplicar por un número negativo cambia el sentido de la desigualdad y obtenemos

$$
f(a+h)<f(a).
$$

Así, respecto del **centro fijo $a$**, la función queda localmente por debajo a la izquierda y por encima a la derecha.

Pero esto no demuestra todavía que $f$ sea creciente en un entorno de $a$.

¿Por qué no?

Porque crecer en un intervalo exige comparar **dos puntos arbitrarios** $x<y$ del intervalo y demostrar

$$
f(x)\le f(y).
$$

La información obtenida desde $f'(a)>0$ compara, en cambio, cada punto cercano únicamente con el centro $a$:

$$
f(a+h)
\quad\text{frente a}\quad
f(a).
$$

No compara entre sí dos puntos situados ambos a la derecha de $a$, ni dos puntos situados ambos a la izquierda.

La diferencia lógica puede verse así:

$$
\boxed{
\begin{array}{c}
f'(a)>0\\[1mm]
\Downarrow\\[1mm]
\text{signo de cocientes con centro fijo }a
\end{array}
}
$$

no es todavía

$$
\boxed{
\forall x<y\text{ cercanos},
\qquad
f(x)\le f(y).
}
$$

Convertir información sobre derivadas en afirmaciones de monotonía sobre intervalos requerirá un mecanismo nuevo. Ese mecanismo aparecerá más adelante mediante los teoremas del valor medio.

::: {.callout-warning title="No adelantar un teorema futuro"}
Del signo de **una derivada puntual** no debemos fabricar una conclusión global o local entre pares arbitrarios.

La pregunta de auditoría es siempre:

> ¿qué puntos está comparando realmente la desigualdad que acabo de demostrar?

Si todos los cocientes tienen el mismo centro $a$, la conclusión sigue siendo puntual.
:::

### Síntesis — Ocho preguntas que deben sobrevivir al capítulo

Después de recorrer el laboratorio, la teoría diferencial básica puede reconstruirse mediante ocho preguntas.

1. **¿De dónde sale el cociente incremental?** De comparar la variación de salida con el incremento de entrada entre dos puntos.
2. **¿Qué distingue continuidad de derivabilidad?** La derivabilidad controla la variación después de dividir por la escala del incremento.
3. **¿Por qué no evaluamos en $h=0$?** Porque la derivada es un límite sobre un entorno perforado, no el valor del cociente en el centro.
4. **¿Por qué podemos cancelar $h$?** Porque la cancelación se realiza donde $h\ne0$, y la coincidencia en un entorno perforado basta para conservar el límite.
5. **¿Por qué un cociente simétrico no sustituye la derivada?** Porque puede ocultar discrepancias entre los dos lados.
6. **¿Qué significa $o(h)$?** Que el error dividido por $h$ tiende a $0$; el error es despreciable frente a la escala lineal.
7. **¿Por qué diferenciabilidad implica continuidad?** Porque la variación es el producto de un incremento que tiende a $0$ por un cociente que posee límite finito, o equivalentemente porque es término lineal más error de orden menor.
8. **¿Por qué $f'(a)>0$ no demuestra monotonía?** Porque la definición compara puntos cercanos con un centro fijo, no todos los pares de puntos de un intervalo.

Estas preguntas forman un mapa cognitivo del capítulo:

$$
\boxed{
\text{construir}
\to
\text{distinguir}
\to
\text{diagnosticar}
\to
\text{justificar}
\to
\text{poner a prueba}
\to
\text{interpretar}
\to
\text{reconstruir}
\to
\text{delimitar}.
}
$$

Ese mapa es más importante que memorizar una colección de frases aisladas. La autonomía matemática comienza cuando podemos recuperar un resultado desde sus definiciones, detectar qué hipótesis hacen el trabajo y reconocer con precisión qué **no** se sigue todavía.

Con esta reconstrucción termina la parte conceptual de `T1-C07`. La sección siguiente reunirá el banco completo de ejercicios y soluciones para poner a prueba, en niveles progresivos, todas las ideas desarrolladas en el capítulo.

## Ejercicios y soluciones {#sec-t1-c07-11}

Llegamos al banco final de `T1-C07`. El capítulo ha construido la derivada desde el cociente incremental y ha mostrado que una misma idea puede leerse como tasa instantánea, pendiente tangente y coeficiente de la aproximación afín local de primer orden.

En estos problemas no se utilizarán todavía reglas generales de derivación. Antes de comenzar cada ejercicio conviene auditar cuatro preguntas:

1. ¿el problema pide calcular un cociente incremental, estudiar su límite o reconstruir una linealización?;
2. ¿el punto es interior del dominio, extremo o punto donde el dominio cambia de forma?;
3. ¿la conclusión es puntual —centrada en un solo punto— o pretende comparar pares arbitrarios en un entorno?;
4. ¿la herramienta necesaria pertenece realmente a este capítulo, o estaríamos anticipando una regla de `T1-C08` o un teorema del valor medio de `T1-C10`?

El banco contiene exactamente cuarenta ejercicios:

$$
7A+7B+7C+6D+5E+5F+3G=40.
$$

Todos son originales y pueden resolverse usando los capítulos publicados desde los números reales hasta el presente. Las reglas sistemáticas de derivación, la regla de la cadena, la derivación de funciones elementales como repertorio, Rolle, los teoremas del valor medio, Taylor y Newton quedan fuera.

### Nivel A — Reconocimiento y comprensión

::: {#exr-t1-0236}
<!-- CPM-T1-EXR-0236 | A | CONCEPTUAL | GEOMETRY | ORIGINAL -->
**Ejercicio A1. Incrementos y pendiente secante.** Sea $f(x)=x^2$. Fija $a\in\mathbb R$ y un incremento $h\ne0$.

1. Identifica el incremento de entrada $\Delta x$ entre $a$ y $a+h$.
2. Identifica la variación de salida $\Delta y$.
3. Escribe la pendiente de la secante que une $(a,f(a))$ con $(a+h,f(a+h))$.
4. Simplifica esa pendiente sin tomar todavía ningún límite.
:::

::: {#exr-t1-0237}
<!-- CPM-T1-EXR-0237 | A | PROOF | ORIGINAL -->
**Ejercicio A2. La derivada de una constante desde la definición.** Sea $A\subseteq\mathbb R$, sea $a\in A$ un punto de acumulación de $A$ y sea

$$
f(x)=c
\qquad(x\in A),
$$

donde $c\in\mathbb R$ es fijo. Demuestra directamente desde la definición que $f$ es diferenciable en $a$ y que

$$
f'_A(a)=0.
$$
:::

::: {#exr-t1-0238}
<!-- CPM-T1-EXR-0238 | A | PROOF | ORIGINAL -->
**Ejercicio A3. La identidad desde la definición.** Para

$$
f(x)=x,
$$

demuestra directamente, sin usar ninguna regla de derivación, que

$$
f'(a)=1
$$

para todo $a\in\mathbb R$.
:::

::: {#exr-t1-0239}
<!-- CPM-T1-EXR-0239 | A | COMPUTATION | PROOF | ORIGINAL -->
**Ejercicio A4. El cuadrado desde la definición.** Sea $f(x)=x^2$. Calcula $f'(a)$ para un punto arbitrario $a\in\mathbb R$ partiendo únicamente de

$$
\frac{f(a+h)-f(a)}{h}.
$$

No cites una regla para derivar potencias.
:::

::: {#exr-t1-0240}
<!-- CPM-T1-EXR-0240 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A5. Tres objetos que no deben confundirse.** Sea $f$ diferenciable en $a$. Clasifica cada expresión como **pendiente de una secante**, **derivada en el punto**, **pendiente de la tangente**, **recta tangente** o **ninguna de las anteriores**:

1.
   $$
   \frac{f(a+h)-f(a)}{h},
   \qquad h\ne0;
   $$
2.
   $$
   \lim_{h\to0}\frac{f(a+h)-f(a)}{h};
   $$
3.
   $$
   f'(a);
   $$
4.
   $$
   T_a(x)=f(a)+f'(a)(x-a);
   $$
5. $f(a)$.

Explica por qué dos de las respuestas anteriores representan el mismo número, aunque procedan de descripciones conceptuales diferentes.
:::

::: {#exr-t1-0241}
<!-- CPM-T1-EXR-0241 | A | GEOMETRY | ORIGINAL -->
**Ejercicio A6. Tangente a la parábola.** Usando únicamente el cálculo directo de la derivada de $x^2$, escribe la recta tangente a

$$
f(x)=x^2
$$

en el punto de abscisa $a$. Simplifica su ecuación.
:::

::: {#exr-t1-0242}
<!-- CPM-T1-EXR-0242 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A7. Reconocer un error de orden menor.** Decide cuáles de las siguientes funciones de $h$ satisfacen

$$
r(h)=o(h)
\qquad(h\to0):
$$

$$
h^2,
\qquad
h|h|,
\qquad
|h|,
\qquad
h+h^2.
$$

Justifica cada respuesta dividiendo por $h$ para $h\ne0$.
:::

### Nivel B — Aplicación directa

::: {#exr-t1-0243}
<!-- CPM-T1-EXR-0243 | B | COMPUTATION | PROOF | ORIGINAL -->
**Ejercicio B1. El cubo desde la definición.** Para

$$
f(x)=x^3,
$$

calcula $f'(a)$ en un punto arbitrario $a$ usando solamente el cociente incremental y álgebra elemental.
:::

::: {#exr-t1-0244}
<!-- CPM-T1-EXR-0244 | B | COMPUTATION | PROOF | ORIGINAL -->
**Ejercicio B2. El recíproco desde la definición.** Sea

$$
f(x)=\frac1x
$$

y fija $a\ne0$. Calcula $f'(a)$ directamente desde la definición. Explica por qué, para $h$ suficientemente pequeño, el denominador $a+h$ permanece distinto de $0$.
:::

::: {#exr-t1-0245}
<!-- CPM-T1-EXR-0245 | B | PROOF | ORIGINAL -->
**Ejercicio B3. Cambiar de fórmula sin perder diferenciabilidad.** Define

$$
f(x)=x|x|.
$$

Demuestra desde la definición que $f$ es diferenciable en $0$ y calcula $f'(0)$.
:::

::: {#exr-t1-0246}
<!-- CPM-T1-EXR-0246 | B | COMPUTATION | CONCEPTUAL | ORIGINAL -->
**Ejercicio B4. Las dos pendientes de una esquina.** Para

$$
f(x)=|x|,
$$

calcula la derivada derecha y la derivada izquierda en $0$. Decide si existe la derivada bilateral.
:::

::: {#exr-t1-0247}
<!-- CPM-T1-EXR-0247 | B | COMPUTATION | CONCEPTUAL | ORIGINAL -->
**Ejercicio B5. Un extremo del dominio.** Considera

$$
f:[0,\infty)\to\mathbb R,
\qquad
f(x)=x^2.
$$

1. Calcula la derivada derecha de $f$ en $0$.
2. Considera la extensión $F:\mathbb R\to\mathbb R$, $F(x)=x^2$. Calcula su derivada bilateral en $0$ desde la definición.
3. Explica por qué los dos cálculos coinciden en este caso, aunque conceptualmente no sean la misma pregunta.
:::

::: {#exr-t1-0248}
<!-- CPM-T1-EXR-0248 | B | PROOF | SEQUENCES | ORIGINAL -->
**Ejercicio B6. Refutar un límite con dos sucesiones.** Usa las sucesiones

$$
h_n=\frac1n,
\qquad
k_n=-\frac1n
$$

para demostrar, mediante el criterio secuencial, que $|x|$ no es diferenciable en $0$.
:::

::: {#exr-t1-0249}
<!-- CPM-T1-EXR-0249 | B | PROOF | CONCEPTUAL | ORIGINAL -->
**Ejercicio B7. Un salto excluye diferenciabilidad.** Sea $f:A\to\mathbb R$ y sea $a\in A$ un punto de acumulación. Supón que $f$ es discontinua en $a$; por ejemplo, porque presenta un salto allí. Justifica que $f$ no puede ser diferenciable en $a$.

Indica con precisión qué resultado del capítulo estás usando y qué forma lógica tiene el argumento.
:::

### Nivel C — Combinación estructural

::: {#exr-t1-0250}
<!-- CPM-T1-EXR-0250 | C | SYNTHESIS | PROOF | ORIGINAL -->
**Ejercicio C1. Pegar dos fórmulas con diferenciabilidad.** Para parámetros $\alpha,\beta,\gamma,\delta\in\mathbb R$, define

$$
f(x)=
\begin{cases}
\alpha x+\beta,&x\le0,\\
x^2+\gamma x+\delta,&x>0.
\end{cases}
$$

Determina todas las relaciones entre los parámetros que hacen a $f$ diferenciable en $0$.

Organiza la solución en dos controles separados: continuidad y coincidencia de los cocientes laterales.
:::

::: {#exr-t1-0251}
<!-- CPM-T1-EXR-0251 | C | PROOF | ORIGINAL -->
**Ejercicio C2. Localidad de la derivada.** Sean $f,g:A\to\mathbb R$ y sea $a\in A$ un punto de acumulación. Supón que existe $\delta_0>0$ tal que

$$
x\in A,\quad |x-a|<\delta_0
\Longrightarrow
f(x)=g(x).
$$

Demuestra directamente que $f$ es diferenciable en $a$ si y solo si $g$ lo es y que, cuando existen,

$$
f'_A(a)=g'_A(a).
$$
:::

::: {#exr-t1-0252}
<!-- CPM-T1-EXR-0252 | C | PROOF | ORIGINAL -->
**Ejercicio C3. Linealización cuando el valor central es cero.** Supón que $f$ es diferenciable en $a$ y que

$$
f(a)=0.
$$

Demuestra que

$$
f(a+h)=f'(a)h+o(h)
\qquad(h\to0).
$$
:::

::: {#exr-t1-0253}
<!-- CPM-T1-EXR-0253 | C | PROOF | ORIGINAL -->
**Ejercicio C4. Derivada nula y error sublineal.** Sea $f$ diferenciable en $a$. Demuestra la equivalencia

$$
f'(a)=0
\iff
f(a+h)-f(a)=o(h)
\qquad(h\to0).
$$
:::

::: {#exr-t1-0254}
<!-- CPM-T1-EXR-0254 | C | CONCEPTUAL | PROOF | ORIGINAL -->
**Ejercicio C5. Mismo primer orden, distinto residuo.** Considera

$$
f(x)=x^2,
\qquad
g(x)=x^2+x^3.
$$

En $a=0$:

1. calcula directamente $f(0)$, $g(0)$, $f'(0)$ y $g'(0)$;
2. escribe la linealización de primer orden de ambas funciones;
3. calcula los residuos respecto de esa linealización;
4. explica en qué sentido las funciones tienen el mismo comportamiento de primer orden aunque no sean iguales cerca de $0$.
:::

::: {#exr-t1-0255}
<!-- CPM-T1-EXR-0255 | C | PROOF | ORIGINAL -->
**Ejercicio C6. Reconstruir diferenciabilidad implica continuidad.** Supón que

$$
f(a+h)=f(a)+Lh+o(h).
$$

Demuestra directamente, sin volver al cociente incremental, que $f$ es continua en $a$.
:::

::: {#exr-t1-0256}
<!-- CPM-T1-EXR-0256 | C | CONCEPTUAL | PROOF | ORIGINAL -->
**Ejercicio C7. La derivada depende del dominio.** Sea

$$
f(x)=|x|.
$$

1. Considera $f$ como función $\mathbb R\to\mathbb R$ y estudia su diferenciabilidad en $0$.
2. Restringe ahora la misma regla a
   $$
   g:[0,\infty)\to\mathbb R,
   \qquad
   g(x)=|x|.
   $$
   Calcula la derivada relativa de $g$ en $0$.
3. Explica por qué no hay contradicción entre ambas respuestas.
:::

### Nivel D — Inversión y diagnóstico

::: {#exr-t1-0257}
<!-- CPM-T1-EXR-0257 | D | DIAGNOSIS | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio D1. Reparar una implicación falsa.** Un estudiante escribe:

> «Si $f$ es continua en $a$, entonces $f(a+h)-f(a)\to0$. Como además $h\to0$, el cociente
> $$
> \frac{f(a+h)-f(a)}{h}
> $$
> también debe tener límite; por tanto, toda función continua es diferenciable».

Identifica exactamente el paso inválido y refuta la conclusión mediante una función concreta.
:::

::: {#exr-t1-0258}
<!-- CPM-T1-EXR-0258 | D | DIAGNOSIS | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio D2. El cociente simétrico no es la derivada.** Para una función $f$ definida cerca de $a$, considera el cociente simétrico

$$
\frac{f(a+h)-f(a-h)}{2h}.
$$

Demuestra que, para $f(x)=|x|$ y $a=0$, este cociente tiene límite cuando $h\to0$, pero la derivada ordinaria de $f$ en $0$ no existe.

Explica qué información pierde el promedio simétrico.
:::

::: {#exr-t1-0259}
<!-- CPM-T1-EXR-0259 | D | GEOMETRY | DIAGNOSIS | ORIGINAL -->
**Ejercicio D3. Una tangente no se reconoce por el dibujo global.** Considera primero

$$
f(x)=x^3.
$$

1. Calcula desde la definición $f'(0)$ y escribe la tangente en $0$.
2. Demuestra que la gráfica cruza esa tangente en el punto de tangencia.

Ahora considera

$$
g(x)=x^2(x-1).
$$

3. Calcula $g'(0)$ directamente desde el cociente incremental.
4. Comprueba que la tangente en $0$ vuelve a intersectar la gráfica en $x=1$.

Explica por qué estos dos ejemplos invalidan las caracterizaciones «una tangente no cruza la curva» y «una tangente solo puede encontrarse con la gráfica en el punto de tangencia».
:::

::: {#exr-t1-0260}
<!-- CPM-T1-EXR-0260 | D | CONCEPTUAL | ORIGINAL -->
**Ejercicio D4. Pendiente vertical no significa derivada finita.** Sea

$$
f(x)=\sqrt[3]{x}.
$$

1. Justifica que $f$ es continua en $0$.
2. Estudia el cociente incremental en $0$.
3. Decide si $f'(0)$ existe según la definición de este capítulo.
4. Interpreta geométricamente el comportamiento del cociente.
:::

::: {#exr-t1-0261}
<!-- CPM-T1-EXR-0261 | D | CONCEPTUAL | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio D5. Una derivada derecha no determina una extensión.** Sea

$$
f:[0,\infty)\to\mathbb R,
\qquad
f(x)=x.
$$

1. Calcula la derivada derecha de $f$ en $0$.
2. Construye dos extensiones $F_1,F_2:\mathbb R\to\mathbb R$ que coincidan con $f$ en $[0,\infty)$, pero tales que $F_1$ sea diferenciable en $0$ y $F_2$ no lo sea.
3. Explica por qué una derivada lateral en un extremo no autoriza a atribuir una derivada bilateral a una extensión arbitraria.
:::

::: {#exr-t1-0262}
<!-- CPM-T1-EXR-0262 | D | DIAGNOSIS | ORIGINAL -->
**Ejercicio D6. No sustituir $h=0$ en el cociente.** Un estudiante intenta hallar $f'(a)$ escribiendo

$$
f'(a)
=
\frac{f(a+0)-f(a)}{0}
=
\frac00
$$

y concluye que «la derivada nunca existe».

Repara el razonamiento. Explica:

1. dónde está definido el cociente incremental;
2. qué estudia realmente el límite $h\to0$;
3. por qué una simplificación algebraica válida para $h\ne0$ puede determinar el límite.
:::

### Nivel E — Contraejemplos

::: {#exr-t1-0263}
<!-- CPM-T1-EXR-0263 | E | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio E1. Continuidad sin diferenciabilidad.** Da una función continua en $0$ que no sea diferenciable en $0$ y verifica ambas afirmaciones desde las definiciones o criterios ya demostrados.
:::

::: {#exr-t1-0264}
<!-- CPM-T1-EXR-0264 | E | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio E2. Dos pendientes laterales finitas y distintas.** Construye una función continua por tramos en $0$ cuyas derivadas laterales en $0$ existan como números reales pero sean diferentes. Verifica continuidad y calcula ambos límites laterales.
:::

::: {#exr-t1-0265}
<!-- CPM-T1-EXR-0265 | E | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio E3. Cociente incremental no acotado.** Construye una función continua en $0$ cuyo cociente incremental en $0$ sea no acotado en todo entorno perforado de $0$. Verifica ambas propiedades.
:::

::: {#exr-t1-0266}
<!-- CPM-T1-EXR-0266 | E | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio E4. Derivada simétrica existente, derivada ordinaria inexistente.** Construye una función para la cual

$$
\lim_{h\to0}\frac{f(h)-f(-h)}{2h}
$$

exista, pero

$$
\lim_{h\to0}\frac{f(h)-f(0)}{h}
$$

no exista. Justifica los dos hechos.
:::

::: {#exr-t1-0267}
<!-- CPM-T1-EXR-0267 | E | COUNTEREXAMPLE | SEQUENCES | ORIGINAL -->
**Ejercicio E5. Racionales e irracionales producen pendientes distintas.** Define

$$
f(0)=0,
$$

y, para $x\ne0$,

$$
f(x)=
\begin{cases}
x,&x\in\mathbb Q,\\
2x,&x\notin\mathbb Q.
\end{cases}
$$

1. Demuestra que $f$ es continua en $0$.
2. Demuestra que $f$ no es diferenciable en $0$ usando sucesiones racionales e irracionales que converjan a $0$.
:::

### Nivel F — Descubrimiento guiado

::: {#exr-t1-0268}
<!-- CPM-T1-EXR-0268 | F | DISCOVERY | PROOF | ORIGINAL -->
**Ejercicio F1. Descubrir el residuo.** Supón que

$$
\lim_{h\to0}\frac{f(a+h)-f(a)}{h}=L.
$$

Sin citar directamente el teorema de linealización, realiza los siguientes pasos:

1. define
   $$
   r(h)=f(a+h)-f(a)-Lh;
   $$
2. calcula $r(h)/h$ para $h\ne0$;
3. demuestra que $r(h)=o(h)$;
4. reescribe $f(a+h)$ usando $Lh$ y $r(h)$.

¿Qué información estructural sobre la función has recuperado?
:::

::: {#exr-t1-0269}
<!-- CPM-T1-EXR-0269 | F | DISCOVERY | PROOF | ORIGINAL -->
**Ejercicio F2. Del control del error a la continuidad.** Supón que para cada $\varepsilon>0$ existe $\delta>0$ tal que

$$
0<|h|<\delta
\Longrightarrow
|f(a+h)-f(a)-Lh|<\varepsilon|h|.
$$

Demuestra directamente que $f$ es continua en $a$. No cites como caja negra «diferenciabilidad implica continuidad»: reconstruye la estimación que lo hace verdadero.
:::

::: {#exr-t1-0270}
<!-- CPM-T1-EXR-0270 | F | DISCOVERY | PROOF | ORIGINAL -->
**Ejercicio F3. Reconstruir el criterio bilateral.** Sea $a$ un punto interior del dominio de $f$. Supón que existen como números reales las derivadas laterales

$$
f'_-(a),
\qquad
f'_+(a).
$$

Demuestra que $f'(a)$ existe si y solo si

$$
f'_-(a)=f'_+(a),
$$

y que, en ese caso, los tres valores coinciden.
:::

::: {#exr-t1-0271}
<!-- CPM-T1-EXR-0271 | F | DISCOVERY | SYNTHESIS | ORIGINAL -->
**Ejercicio F4. La única recta que puede pegarse suavemente a la parábola.** Fija $a\in\mathbb R$ y una recta

$$
\ell(x)=mx+b.
$$

Define

$$
F(x)=
\begin{cases}
\ell(x),&x<a,\\
x^2,&x\ge a.
\end{cases}
$$

Determina los únicos valores de $m$ y $b$ para los cuales $F$ es diferenciable en $a$. Interpreta la recta obtenida.
:::

::: {#exr-t1-0272}
<!-- CPM-T1-EXR-0272 | F | DISCOVERY | CONCEPTUAL | ORIGINAL -->
**Ejercicio F5. Diferenciable con error mayor que cuadrático.** Sea

$$
f(x)=|x|^{3/2}.
$$

1. Demuestra que $f$ es diferenciable en $0$ y que $f'(0)=0$.
2. Su linealización en $0$ es la función nula. Demuestra que el residuo
   $$
   r(h)=|h|^{3/2}
   $$
   no satisface una cota cuadrática local: no existen $C>0$ y $\delta>0$ tales que
   $$
   |r(h)|\le C|h|^2
   \qquad(0<|h|<\delta).
   $$
3. Explica por qué la diferenciabilidad solo exige $r(h)=o(h)$ y no un error de orden cuadrático.
:::

### Nivel G — Desafío

::: {#exr-t1-0273}
<!-- CPM-T1-EXR-0273 | G | CHALLENGE | PROOF | ORIGINAL -->
**Ejercicio G1. Una derivada positiva da información con centro fijo.** Supón que $f$ es diferenciable en $a$ y

$$
f'(a)>0.
$$

1. Demuestra que existe $\delta>0$ tal que para todo $h$ admisible con
   $$
   0<|h|<\delta
   $$
   se cumple
   $$
   \frac{f(a+h)-f(a)}{h}>0.
   $$
2. Deduce que, para esos incrementos,
   $$
   h>0\Longrightarrow f(a+h)>f(a),
   $$
   y
   $$
   h<0\Longrightarrow f(a+h)<f(a).
   $$
3. Explica cuidadosamente por qué esto **no** demuestra que $f$ sea creciente en un entorno de $a$.
:::

::: {#exr-t1-0274}
<!-- CPM-T1-EXR-0274 | G | CHALLENGE | PROOF | ORIGINAL -->
**Ejercicio G2. Mismo valor y misma derivada como equivalencia de primer orden.** Sean $f,g:A\to\mathbb R$ diferenciables en un punto de acumulación $a\in A$, respecto del mismo dominio $A$. Todos los límites siguientes se entienden a través de incrementos admisibles de $A$. Demuestra que son equivalentes las siguientes afirmaciones:

1.
   $$
   f(a)=g(a)
   \qquad\text{y}\qquad
   f'(a)=g'(a);
   $$
2.
   $$
   f(a+h)-g(a+h)=o(h)
   \qquad(h\to0).
   $$

La dirección inversa requiere justificar primero la igualdad de los valores centrales y después la igualdad de las derivadas.
:::

::: {#exr-t1-0275}
<!-- CPM-T1-EXR-0275 | G | CHALLENGE | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio G3. Diferenciable en un punto, irregular en todos los demás.** Define $f:\mathbb R\to\mathbb R$ por

$$
f(0)=0,
$$

y, para $x\ne0$,

$$
f(x)=
\begin{cases}
x^2,&x\in\mathbb Q,\\
0,&x\notin\mathbb Q.
\end{cases}
$$

1. Demuestra que $f$ es continua en $0$.
2. Demuestra que $f$ es diferenciable en $0$ y calcula $f'(0)$.
3. Sea $c\ne0$. Usa la densidad de $\mathbb Q$ y de $\mathbb R\setminus\mathbb Q$ para construir dos sucesiones que converjan a $c$ y produzcan comportamientos incompatibles de $f$.
4. Concluye que $f$ es discontinua en todo $c\ne0$ y, por tanto, no es diferenciable en ninguno de esos puntos.
:::

### Soluciones

#### Soluciones del nivel A

::: {#sol-t1-0236}
<!-- CPM-T1-SOL-0236 -->
**Solución A1.**

Entre las entradas $a$ y $a+h$,

$$
\Delta x=(a+h)-a=h.
$$

Como $f(x)=x^2$,

$$
\Delta y=f(a+h)-f(a)
=(a+h)^2-a^2.
$$

La pendiente de la secante es

$$
\frac{\Delta y}{\Delta x}
=
\frac{(a+h)^2-a^2}{h},
\qquad h\ne0.
$$

Desarrollando y factorizando,

$$
(a+h)^2-a^2
=
2ah+h^2
=
h(2a+h).
$$

Por tanto,

$$
\boxed{
\frac{f(a+h)-f(a)}{h}=2a+h
}
\qquad(h\ne0).
$$

Todavía no hemos tomado un límite: $2a+h$ es la pendiente de una secante concreta determinada por el incremento $h$.
:::

::: {#sol-t1-0237}
<!-- CPM-T1-SOL-0237 -->
**Solución A2.**

Para todo $x\in A$ con $x\ne a$,

$$
\frac{f(x)-f(a)}{x-a}
=
\frac{c-c}{x-a}
=
0.
$$

El cociente incremental es, por tanto, idénticamente nulo en el dominio perforado relativo a $A$. Luego

$$
\lim_{\substack{x\to a\\x\in A}}
\frac{f(x)-f(a)}{x-a}
=
0.
$$

Por definición,

$$
\boxed{f'_A(a)=0}.
$$

La hipótesis de que $a$ sea punto de acumulación garantiza que el límite describe información incremental no vacía.
:::

::: {#sol-t1-0238}
<!-- CPM-T1-SOL-0238 -->
**Solución A3.**

Si $f(x)=x$, entonces para $h\ne0$,

$$
\frac{f(a+h)-f(a)}{h}
=
\frac{(a+h)-a}{h}
=
\frac hh
=
1.
$$

Así,

$$
\lim_{h\to0}
\frac{f(a+h)-f(a)}{h}
=
1,
$$

y por definición

$$
\boxed{f'(a)=1}.
$$

El cálculo no depende del valor de $a$.
:::

::: {#sol-t1-0239}
<!-- CPM-T1-SOL-0239 -->
**Solución A4.**

Para $h\ne0$,

$$
\frac{f(a+h)-f(a)}{h}
=
\frac{(a+h)^2-a^2}{h}.
$$

Factorizando,

$$
(a+h)^2-a^2
=
h(2a+h),
$$

de modo que

$$
\frac{(a+h)^2-a^2}{h}
=
2a+h.
$$

Ahora sí tomamos el límite:

$$
\lim_{h\to0}(2a+h)=2a.
$$

Por tanto,

$$
\boxed{f'(a)=2a}.
$$

La fórmula se ha obtenido desde la definición, no desde una regla general para potencias.
:::

::: {#sol-t1-0240}
<!-- CPM-T1-SOL-0240 -->
**Solución A5.**

1. 
   $$
   \frac{f(a+h)-f(a)}{h}
   $$
   con $h\ne0$ es la **pendiente de una secante**.
2.
   $$
   \lim_{h\to0}\frac{f(a+h)-f(a)}{h}
   $$
   es la **derivada en el punto**, siempre que el límite exista como número real.
3. $f'(a)$ es también la **derivada en el punto** y, por definición de tangente, es la **pendiente de la tangente**.
4.
   $$
   T_a(x)=f(a)+f'(a)(x-a)
   $$
   es la **recta tangente**.
5. $f(a)$ es el valor de la función en el centro; no es, por sí mismo, una pendiente ni una recta.

Los apartados 2 y 3 representan el mismo número porque $f'(a)$ es precisamente el nombre asignado al límite del cociente incremental. Ese mismo número adquiere una lectura geométrica adicional como pendiente de la tangente.
:::

::: {#sol-t1-0241}
<!-- CPM-T1-SOL-0241 -->
**Solución A6.**

Para $f(x)=x^2$ ya obtuvimos directamente

$$
f'(a)=2a.
$$

La recta tangente es

$$
T_a(x)
=
f(a)+f'(a)(x-a)
=
a^2+2a(x-a).
$$

Simplificando,

$$
T_a(x)
=
a^2+2ax-2a^2
=
2ax-a^2.
$$

Por tanto,

$$
\boxed{T_a(x)=2ax-a^2}.
$$
:::

::: {#sol-t1-0242}
<!-- CPM-T1-SOL-0242 -->
**Solución A7.**

Debemos estudiar $r(h)/h$ para $h\ne0$.

Para $r(h)=h^2$,

$$
\frac{h^2}{h}=h\to0,
$$

así que

$$
h^2=o(h).
$$

Para $r(h)=h|h|$,

$$
\frac{h|h|}{h}=|h|\to0,
$$

por lo que

$$
h|h|=o(h).
$$

Para $r(h)=|h|$,

$$
\frac{|h|}{h}
=
\begin{cases}
1,&h>0,\\
-1,&h<0,
\end{cases}
$$

y el límite bilateral no existe. Luego $|h|$ no es $o(h)$.

Finalmente,

$$
\frac{h+h^2}{h}=1+h\to1,
$$

no a $0$. Por tanto, $h+h^2$ tampoco es $o(h)$.

En resumen,

$$
\boxed{h^2,\;h|h|\text{ son }o(h);}
$$

$$
\boxed{|h|,\;h+h^2\text{ no lo son}.}
$$
:::

#### Soluciones del nivel B

::: {#sol-t1-0243}
<!-- CPM-T1-SOL-0243 -->
**Solución B1.**

Para $h\ne0$,

$$
\frac{(a+h)^3-a^3}{h}
=
\frac{a^3+3a^2h+3ah^2+h^3-a^3}{h}.
$$

Factorizando $h$,

$$
\frac{(a+h)^3-a^3}{h}
=
3a^2+3ah+h^2.
$$

Al hacer $h\to0$,

$$
3a^2+3ah+h^2\longrightarrow3a^2.
$$

Por tanto,

$$
\boxed{f'(a)=3a^2}.
$$
:::

::: {#sol-t1-0244}
<!-- CPM-T1-SOL-0244 -->
**Solución B2.**

Como $a\ne0$, podemos elegir por ejemplo

$$
|h|<\frac{|a|}{2}.
$$

Entonces

$$
|a+h|
\ge |a|-|h|
>
\frac{|a|}{2}>0,
$$

de modo que $a+h\ne0$.

Para esos $h\ne0$,

$$
\frac{\frac1{a+h}-\frac1a}{h}
=
\frac{a-(a+h)}{a(a+h)h}
=
\frac{-h}{a(a+h)h}
=
-\frac1{a(a+h)}.
$$

Como $a+h\to a$,

$$
-\frac1{a(a+h)}
\longrightarrow
-\frac1{a^2}.
$$

Así,

$$
\boxed{f'(a)=-\frac1{a^2}}.
$$
:::

::: {#sol-t1-0245}
<!-- CPM-T1-SOL-0245 -->
**Solución B3.**

Tenemos $f(0)=0$. Para $h\ne0$,

$$
\frac{f(h)-f(0)}{h}
=
\frac{h|h|}{h}
=
|h|.
$$

Como

$$
|h|\to0,
$$

se sigue que el cociente incremental posee límite real y

$$
\boxed{f'(0)=0}.
$$

El cambio de fórmula implícito en el valor absoluto no impide la diferenciabilidad porque, después de dividir por $h$, queda un término que tiende a $0$ desde ambos lados.
:::

::: {#sol-t1-0246}
<!-- CPM-T1-SOL-0246 -->
**Solución B4.**

Como $f(0)=0$, para $h\ne0$,

$$
\frac{f(h)-f(0)}{h}
=
\frac{|h|}{h}.
$$

Si $h>0$,

$$
\frac{|h|}{h}=1,
$$

por lo que

$$
f'_+(0)=1.
$$

Si $h<0$,

$$
\frac{|h|}{h}=-1,
$$

y entonces

$$
f'_-(0)=-1.
$$

Los dos límites laterales existen como números reales pero son distintos. Por el criterio lateral,

$$
\boxed{f'(0)\text{ no existe}.}
$$
:::

::: {#sol-t1-0247}
<!-- CPM-T1-SOL-0247 -->
**Solución B5.**

En el dominio $[0,\infty)$ solo son admisibles incrementos $h>0$ cerca de $0$. Por tanto,

$$
f'_+(0)
=
\lim_{h\to0^+}\frac{h^2-0}{h}
=
\lim_{h\to0^+}h
=
0.
$$

Para la extensión $F(x)=x^2$ sobre todo $\mathbb R$,

$$
F'(0)
=
\lim_{h\to0}\frac{h^2}{h}
=
\lim_{h\to0}h
=
0.
$$

Los valores coinciden:

$$
\boxed{f'_+(0)=F'(0)=0}.
$$

Pero las preguntas son distintas. La primera utiliza únicamente puntos del dominio a la derecha de $0$; la segunda exige compatibilidad de los cocientes desde ambos lados. La coincidencia ocurre porque la extensión concreta $x^2$ posee el mismo comportamiento desde la izquierda.
:::

::: {#sol-t1-0248}
<!-- CPM-T1-SOL-0248 -->
**Solución B6.**

El cociente incremental de $|x|$ en $0$ es

$$
Q(h)=\frac{|h|}{h}.
$$

Para

$$
h_n=\frac1n,
$$

tenemos $h_n\to0$ y

$$
Q(h_n)=1
$$

para todo $n$.

Para

$$
k_n=-\frac1n,
$$

tenemos $k_n\to0$ y

$$
Q(k_n)=-1.
$$

Si $Q(h)$ tuviera un límite real cuando $h\to0$, el criterio secuencial obligaría a que ambos valores sucesionales convergieran al mismo número. Pero

$$
1\ne-1.
$$

Por tanto,

$$
\boxed{|x|\text{ no es diferenciable en }0}.
$$
:::

::: {#sol-t1-0249}
<!-- CPM-T1-SOL-0249 -->
**Solución B7.**

El capítulo demostró

$$
f\text{ diferenciable en }a
\Longrightarrow
f\text{ continua en }a.
$$

Su contraposición es

$$
f\text{ discontinua en }a
\Longrightarrow
f\text{ no diferenciable en }a.
$$

Como la hipótesis afirma precisamente que $f$ es discontinua en $a$, podemos aplicar esa contraposición y concluir

$$
\boxed{f'(a)\text{ no existe como derivada real finita}.}
$$

El argumento es lógico, no un cálculo del cociente: usamos una condición necesaria para diferenciabilidad.
:::

#### Soluciones del nivel C

::: {#sol-t1-0250}
<!-- CPM-T1-SOL-0250 -->
**Solución C1.**

Para que $f$ sea diferenciable en $0$, primero debe ser continua allí.

Como

$$
f(0)=\beta,
$$

mientras que

$$
\lim_{x\to0^+}f(x)=\delta,
$$

la continuidad exige

$$
\boxed{\beta=\delta}.
$$

Bajo esta condición, calculamos los cocientes laterales.

Por la izquierda, para $h<0$,

$$
\frac{f(h)-f(0)}{h}
=
\frac{\alpha h+\beta-\beta}{h}
=
\alpha.
$$

Así,

$$
f'_-(0)=\alpha.
$$

Por la derecha, para $h>0$ y usando $\delta=\beta$,

$$
\frac{f(h)-f(0)}{h}
=
\frac{h^2+\gamma h+\delta-\beta}{h}
=
h+\gamma,
$$

de modo que

$$
f'_+(0)=\gamma.
$$

La derivada bilateral existe exactamente cuando ambos valores coinciden:

$$
\boxed{\alpha=\gamma}.
$$

Por tanto,

$$
\boxed{
f\text{ es diferenciable en }0
\iff
\beta=\delta
\text{ y }
\alpha=\gamma.
}
$$
:::

::: {#sol-t1-0251}
<!-- CPM-T1-SOL-0251 -->
**Solución C2.**

La hipótesis incluye el centro, así que

$$
f(a)=g(a).
$$

Además, cuando

$$
x\in A,
\qquad
0<|x-a|<\delta_0,
$$

tenemos $f(x)=g(x)$. Por tanto,

$$
\frac{f(x)-f(a)}{x-a}
=
\frac{g(x)-g(a)}{x-a}
$$

en un entorno perforado relativo al dominio.

Dos funciones que coinciden en algún entorno perforado de un punto tienen el mismo comportamiento límite allí. En consecuencia, uno de esos cocientes posee límite real si y solo si el otro lo posee y, en tal caso, los límites son iguales.

Así,

$$
\boxed{
f\text{ diferenciable en }a
\iff
g\text{ diferenciable en }a,
}
$$

y, cuando ocurre,

$$
\boxed{f'_A(a)=g'_A(a)}.
$$
:::

::: {#sol-t1-0252}
<!-- CPM-T1-SOL-0252 -->
**Solución C3.**

Por la caracterización de la diferenciabilidad mediante linealización,

$$
f(a+h)
=
f(a)+f'(a)h+o(h).
$$

Como $f(a)=0$,

$$
f(a+h)
=
f'(a)h+o(h).
$$

Por tanto,

$$
\boxed{
f(a+h)=f'(a)h+o(h).
}
$$

La hipótesis sobre el valor central elimina únicamente el término constante de la aproximación afín.
:::

::: {#sol-t1-0253}
<!-- CPM-T1-SOL-0253 -->
**Solución C4.**

Si $f'(a)=0$, la linealización da

$$
f(a+h)
=
f(a)+0\cdot h+o(h),
$$

por lo que

$$
f(a+h)-f(a)=o(h).
$$

Recíprocamente, supongamos

$$
f(a+h)-f(a)=o(h).
$$

Para $h\ne0$,

$$
\frac{f(a+h)-f(a)}{h}
=
\frac{o(h)}{h}.
$$

Por definición de $o(h)$, el lado derecho tiende a $0$. Entonces

$$
f'(a)=0.
$$

Así,

$$
\boxed{
f'(a)=0
\iff
f(a+h)-f(a)=o(h).
}
$$
:::

::: {#sol-t1-0254}
<!-- CPM-T1-SOL-0254 -->
**Solución C5.**

En $0$,

$$
f(0)=g(0)=0.
$$

Para $f$,

$$
\frac{f(h)-f(0)}{h}
=
h\to0.
$$

Para $g$,

$$
\frac{g(h)-g(0)}{h}
=
\frac{h^2+h^3}{h}
=
h+h^2
\to0.
$$

Por tanto,

$$
f'(0)=g'(0)=0.
$$

La linealización de primer orden de ambas funciones es

$$
T(h)=0.
$$

Los residuos son

$$
r_f(h)=h^2,
$$

y

$$
r_g(h)=h^2+h^3.
$$

Ambos satisfacen

$$
\frac{r_f(h)}h\to0,
\qquad
\frac{r_g(h)}h\to0,
$$

de modo que ambos son $o(h)$.

Las funciones no son iguales cerca de $0$ porque

$$
g(h)-f(h)=h^3,
$$

pero esa diferencia también es $o(h)$. Así, a escala de primer orden comparten el mismo valor central y el mismo coeficiente lineal, aunque sus términos de orden menor sean distintos.
:::

::: {#sol-t1-0255}
<!-- CPM-T1-SOL-0255 -->
**Solución C6.**

Escribamos

$$
f(a+h)-f(a)=Lh+r(h),
$$

donde

$$
r(h)=o(h).
$$

Como $r(h)/h\to0$, existe una función $\varepsilon(h)\to0$ tal que

$$
r(h)=h\varepsilon(h)
$$

para $h\ne0$ suficientemente pequeño. Entonces

$$
f(a+h)-f(a)
=
h\bigl(L+\varepsilon(h)\bigr).
$$

El factor $h$ tiende a $0$, mientras que

$$
L+\varepsilon(h)\to L
$$

es acotado cerca de $0$. Por álgebra de límites,

$$
f(a+h)-f(a)\to0.
$$

Por tanto,

$$
f(a+h)\to f(a),
$$

y $f$ es continua en $a$.
:::

::: {#sol-t1-0256}
<!-- CPM-T1-SOL-0256 -->
**Solución C7.**

Como función sobre $\mathbb R$,

$$
\frac{|h|-0}{h}
=
\frac{|h|}{h}.
$$

El límite por la derecha es $1$ y por la izquierda es $-1$. Por tanto, $|x|$ no es diferenciable en $0$ sobre $\mathbb R$.

En cambio, para

$$
g:[0,\infty)\to\mathbb R,
\qquad
g(x)=|x|=x,
$$

los incrementos admisibles cerca de $0$ satisfacen $h>0$. Así,

$$
g'_{[0,\infty)}(0)
=
\lim_{h\to0^+}\frac{h}{h}
=
1.
$$

No hay contradicción. La derivada relativa es un límite relativo al dominio. Sobre $\mathbb R$ debemos compatibilizar ambos lados; sobre $[0,\infty)$ solo existe aproximación desde la derecha.
:::

#### Soluciones del nivel D

::: {#sol-t1-0257}
<!-- CPM-T1-SOL-0257 -->
**Solución D1.**

La continuidad proporciona

$$
f(a+h)-f(a)\to0.
$$

Pero de

$$
u(h)\to0,
\qquad
v(h)\to0
$$

no se sigue que $u(h)/v(h)$ tenga límite. La regla del cociente para límites requiere que el límite del denominador sea distinto de $0$.

Aquí precisamente

$$
h\to0,
$$

de modo que la división no está protegida por esa regla.

Un contraejemplo es

$$
f(x)=|x|
$$

en $a=0$. La función es continua porque $|x|\to0$, pero

$$
\frac{|h|}{h}
=
\begin{cases}
1,&h>0,\\
-1,&h<0,
\end{cases}
$$

no posee límite bilateral.

Por tanto, continuidad no implica diferenciabilidad.
:::

::: {#sol-t1-0258}
<!-- CPM-T1-SOL-0258 -->
**Solución D2.**

Para $f(x)=|x|$ y $a=0$,

$$
\frac{f(h)-f(-h)}{2h}
=
\frac{|h|-|-h|}{2h}.
$$

Como

$$
|-h|=|h|,
$$

el numerador es $0$ y, para $h\ne0$,

$$
\frac{|h|-|-h|}{2h}=0.
$$

Por tanto, el cociente simétrico tiene límite $0$.

Sin embargo, el cociente incremental ordinario es

$$
\frac{|h|-0}{h}
=
\frac{|h|}{h},
$$

cuyos límites laterales son $1$ y $-1$. La derivada ordinaria no existe.

El cociente simétrico compara simultáneamente los valores a ambos lados y puede hacer que comportamientos opuestos se cancelen. Por eso no sustituye el control unilateral necesario para el límite ordinario.
:::

::: {#sol-t1-0259}
<!-- CPM-T1-SOL-0259 -->
**Solución D3.**

Para $f(x)=x^3$,

$$
\frac{f(h)-f(0)}{h}
=
h^2\to0.
$$

Así,

$$
f'(0)=0,
$$

y la tangente es

$$
y=0.
$$

Pero

$$
x^3<0\quad(x<0),
\qquad
x^3>0\quad(x>0).
$$

La gráfica pasa de un lado de la recta $y=0$ al otro: la tangente **cruza** la gráfica en el punto de tangencia.

Ahora,

$$
g(x)=x^2(x-1)=x^3-x^2,
$$

y $g(0)=0$. Para $h\ne0$,

$$
\frac{g(h)-g(0)}h
=
\frac{h^2(h-1)}h
=
h(h-1)\to0.
$$

Por tanto, la tangente en $0$ vuelve a ser

$$
y=0.
$$

Las intersecciones con la gráfica satisfacen

$$
x^2(x-1)=0,
$$

así que aparecen en

$$
x=0
\qquad\text{y}\qquad
x=1.
$$

Los dos ejemplos muestran que la tangencia es una noción local de primer orden. Ni «no cruzar» ni «intersectar una sola vez» pueden servir como definición.
:::

::: {#sol-t1-0260}
<!-- CPM-T1-SOL-0260 -->
**Solución D4.**

Primero comprobamos la continuidad en $0$. Dado $\varepsilon>0$, si

$$
|x|<\varepsilon^3,
$$

entonces

$$
|f(x)-f(0)|
=
|\sqrt[3]{x}|
=
|x|^{1/3}
<
\varepsilon.
$$

Por tanto,

$$
f(x)\to0=f(0)
\qquad(x\to0).
$$

Para $h\ne0$,

$$
\frac{f(h)-f(0)}h
=
\frac{\sqrt[3]{h}}h.
$$

Como

$$
h=(\sqrt[3]{h})^3,
$$

obtenemos

$$
\frac{\sqrt[3]{h}}h
=
\frac1{(\sqrt[3]{h})^2}
=
\frac1{|h|^{2/3}}.
$$

Cuando $h\to0$,

$$
\frac1{|h|^{2/3}}\to+\infty.
$$

El cociente incremental no converge a un número real finito. Por tanto, según la definición del capítulo,

$$
\boxed{f'(0)\text{ no existe}.}
$$

Geométricamente, el crecimiento sin cota de las pendientes secantes sugiere una tangente vertical. Pero una tangente vertical en ese sentido geométrico no convierte $+\infty$ en una derivada real.
:::

::: {#sol-t1-0261}
<!-- CPM-T1-SOL-0261 -->
**Solución D5.**

Para $h>0$,

$$
\frac{f(h)-f(0)}h
=
\frac hh
=
1.
$$

Así,

$$
f'_+(0)=1.
$$

Una primera extensión es

$$
F_1(x)=x
\qquad(x\in\mathbb R).
$$

Entonces

$$
F_1'(0)=1.
$$

Una segunda extensión es

$$
F_2(x)=|x|
=
\begin{cases}
-x,&x<0,\\
x,&x\ge0.
\end{cases}
$$

Esta coincide con $f$ para $x\ge0$, pero en $0$ sus derivadas laterales son

$$
F'_{2,-}(0)=-1,
\qquad
F'_{2,+}(0)=1.
$$

Por tanto, $F_2'(0)$ no existe.

La información del dominio $[0,\infty)$ no contiene ninguna condición sobre cómo debe comportarse una extensión a la izquierda de $0$. Una derivada derecha no determina ese dato ausente.
:::

::: {#sol-t1-0262}
<!-- CPM-T1-SOL-0262 -->
**Solución D6.**

El cociente incremental

$$
\frac{f(a+h)-f(a)}h
$$

solo se considera para

$$
h\ne0.
$$

En $h=0$ aparece una división por cero, así que no hay valor del cociente que debamos evaluar allí.

La derivada pregunta por el límite

$$
\lim_{h\to0}
\frac{f(a+h)-f(a)}h,
$$

es decir, por el comportamiento de la expresión en un entorno perforado de $0$.

Por ejemplo, para $f(x)=x^2$,

$$
\frac{(a+h)^2-a^2}{h}
=
2a+h
\qquad(h\ne0).
$$

La igualdad es válida exactamente donde se necesita para estudiar el límite. Aunque el cociente original no esté definido en $h=0$,

$$
2a+h\to2a.
$$

Por tanto, la derivada puede existir perfectamente. El límite no exige evaluar la expresión original en el punto excluido.
:::

#### Soluciones del nivel E

::: {#sol-t1-0263}
<!-- CPM-T1-SOL-0263 -->
**Solución E1.**

Tomemos

$$
f(x)=|x|.
$$

Como

$$
|f(x)-f(0)|
=
|x|,
$$

se tiene

$$
f(x)\to0=f(0)
\qquad(x\to0),
$$

así que $f$ es continua en $0$.

Pero para $h\ne0$,

$$
\frac{f(h)-f(0)}h
=
\frac{|h|}h,
$$

que vale $1$ si $h>0$ y $-1$ si $h<0$. Los límites laterales no coinciden.

Por tanto,

$$
\boxed{
|x|\text{ es continua pero no diferenciable en }0.
}
$$
:::

::: {#sol-t1-0264}
<!-- CPM-T1-SOL-0264 -->
**Solución E2.**

Un ejemplo es

$$
f(x)=
\begin{cases}
2x,&x<0,\\
x,&x\ge0.
\end{cases}
$$

En ambos lados,

$$
f(x)\to0=f(0)
\qquad(x\to0),
$$

por lo que $f$ es continua en $0$.

Para $h<0$,

$$
\frac{f(h)-f(0)}h
=
\frac{2h}h
=
2,
$$

así que

$$
f'_-(0)=2.
$$

Para $h>0$,

$$
\frac{f(h)-f(0)}h
=
\frac hh
=
1,
$$

por lo que

$$
f'_+(0)=1.
$$

Ambas derivadas laterales existen y son finitas, pero

$$
2\ne1.
$$

Así, la derivada bilateral no existe.
:::

::: {#sol-t1-0265}
<!-- CPM-T1-SOL-0265 -->
**Solución E3.**

Tomemos

$$
f(x)=\sqrt{|x|}.
$$

La función es continua en $0$ porque

$$
\sqrt{|x|}\to0=f(0).
$$

Para $h\ne0$,

$$
\frac{f(h)-f(0)}h
=
\frac{\sqrt{|h|}}h.
$$

Su valor absoluto es

$$
\left|
\frac{\sqrt{|h|}}h
\right|
=
\frac1{\sqrt{|h|}}.
$$

Cuando $h\to0$,

$$
\frac1{\sqrt{|h|}}\to+\infty.
$$

Por tanto, el cociente incremental es no acotado en todo entorno perforado de $0$ y no puede converger a una derivada real finita.
:::

::: {#sol-t1-0266}
<!-- CPM-T1-SOL-0266 -->
**Solución E4.**

De nuevo podemos tomar

$$
f(x)=|x|.
$$

Para $h\ne0$,

$$
\frac{f(h)-f(-h)}{2h}
=
\frac{|h|-|-h|}{2h}
=
0.
$$

Así, la derivada simétrica existe y vale $0$.

En cambio,

$$
\frac{f(h)-f(0)}h
=
\frac{|h|}h
$$

vale $1$ para $h>0$ y $-1$ para $h<0$. Por tanto, la derivada ordinaria no existe.

El ejemplo muestra que la existencia del promedio simétrico es estrictamente más débil que la existencia del límite ordinario del cociente incremental.
:::

::: {#sol-t1-0267}
<!-- CPM-T1-SOL-0267 -->
**Solución E5.**

Para todo $x$,

$$
|f(x)|
\le2|x|.
$$

Como $2|x|\to0$ cuando $x\to0$, el teorema del sándwich da

$$
f(x)\to0=f(0).
$$

Así, $f$ es continua en $0$.

Para $h\ne0$,

$$
\frac{f(h)-f(0)}h
=
\begin{cases}
1,&h\in\mathbb Q,\\
2,&h\notin\mathbb Q.
\end{cases}
$$

Por densidad existen sucesiones de racionales no nulos $q_n\to0$ y de irracionales $r_n\to0$. A lo largo de ellas,

$$
\frac{f(q_n)}{q_n}=1,
$$

mientras que

$$
\frac{f(r_n)}{r_n}=2.
$$

El criterio secuencial impide que el cociente tenga un único límite. Por tanto,

$$
\boxed{f'(0)\text{ no existe}.}
$$
:::

#### Soluciones del nivel F

::: {#sol-t1-0268}
<!-- CPM-T1-SOL-0268 -->
**Solución F1.**

Definimos

$$
r(h)=f(a+h)-f(a)-Lh.
$$

Para $h\ne0$,

$$
\frac{r(h)}h
=
\frac{f(a+h)-f(a)}h-L.
$$

Por hipótesis,

$$
\frac{f(a+h)-f(a)}h\to L,
$$

de modo que

$$
\frac{r(h)}h\to0.
$$

Esto significa exactamente

$$
r(h)=o(h).
$$

Reordenando la definición de $r$,

$$
\boxed{
f(a+h)=f(a)+Lh+o(h).
}
$$

Hemos recuperado la estructura de primer orden: la variación de $f$ se descompone en una parte lineal principal $Lh$ y un error despreciable frente a $h$.
:::

::: {#sol-t1-0269}
<!-- CPM-T1-SOL-0269 -->
**Solución F2.**

Queremos demostrar que

$$
f(a+h)-f(a)\to0.
$$

Tomemos primero $\varepsilon=1$ en la hipótesis. Existe $\delta_1>0$ tal que, si

$$
0<|h|<\delta_1,
$$

entonces

$$
|f(a+h)-f(a)-Lh|<|h|.
$$

Por desigualdad triangular,

$$
|f(a+h)-f(a)|
\le
|L||h|
+
|f(a+h)-f(a)-Lh|
<
(|L|+1)|h|.
$$

Dada una tolerancia $\eta>0$, elijamos

$$
\delta
=
\min\left\{
\delta_1,
\frac{\eta}{|L|+1}
\right\}.
$$

Entonces

$$
0<|h|<\delta
\Longrightarrow
|f(a+h)-f(a)|<\eta.
$$

Para $h=0$ la diferencia es exactamente $0$. Por tanto,

$$
f(a+h)\to f(a),
$$

y $f$ es continua en $a$.
:::

::: {#sol-t1-0270}
<!-- CPM-T1-SOL-0270 -->
**Solución F3.**

Consideremos el cociente incremental

$$
Q(x)=\frac{f(x)-f(a)}{x-a}
$$

sobre el dominio perforado.

La derivada izquierda es el límite de $Q(x)$ cuando $x\to a^-$ y la derecha es el límite cuando $x\to a^+$.

La teoría previa de límites laterales establece que un límite bilateral existe como número real si y solo si existen ambos límites laterales y son iguales.

Por tanto,

$$
f'(a)\text{ existe}
\iff
f'_-(a)\text{ y }f'_+(a)\text{ existen y son iguales}.
$$

Si

$$
f'_-(a)=f'_+(a)=L,
$$

entonces el límite bilateral del mismo cociente es $L$, y

$$
\boxed{
f'(a)=f'_-(a)=f'_+(a)=L.
}
$$
:::

::: {#sol-t1-0271}
<!-- CPM-T1-SOL-0271 -->
**Solución F4.**

Para que $F$ sea diferenciable en $a$, debe ser continua allí.

Como el valor del tramo derecho es

$$
F(a)=a^2,
$$

la continuidad desde la izquierda exige

$$
ma+b=a^2.
$$

La derivada izquierda de la recta es, desde el cociente incremental,

$$
m.
$$

La derivada derecha del tramo $x^2$ en $a$ es

$$
2a.
$$

La diferenciabilidad exige que ambas coincidan:

$$
m=2a.
$$

Sustituyendo en la condición de continuidad,

$$
2a^2+b=a^2,
$$

de donde

$$
b=-a^2.
$$

La única recta es

$$
\boxed{
\ell(x)=2ax-a^2.
}
$$

Pero ésta es exactamente

$$
a^2+2a(x-a),
$$

la recta tangente a $x^2$ en $x=a$.
:::

::: {#sol-t1-0272}
<!-- CPM-T1-SOL-0272 -->
**Solución F5.**

Como $f(0)=0$, para $h\ne0$,

$$
\frac{f(h)-f(0)}h
=
\frac{|h|^{3/2}}h.
$$

Escribiendo $h=\operatorname{sgn}(h)|h|$,

$$
\frac{|h|^{3/2}}h
=
\operatorname{sgn}(h)|h|^{1/2}.
$$

Su valor absoluto es $|h|^{1/2}\to0$. Por tanto,

$$
\boxed{f'(0)=0}.
$$

La linealización es la función nula y el residuo es

$$
r(h)=|h|^{3/2}.
$$

Supongamos que existieran $C>0$ y $\delta>0$ tales que

$$
|h|^{3/2}\le C|h|^2
$$

para todo $0<|h|<\delta$. Dividiendo por $|h|^{3/2}>0$,

$$
1\le C|h|^{1/2}.
$$

Pero el lado derecho puede hacerse menor que $1$ tomando $|h|$ suficientemente pequeño, contradicción.

Equivalentemente,

$$
\frac{|h|^{3/2}}{|h|^2}
=
\frac1{|h|^{1/2}}
\to+\infty.
$$

La diferenciabilidad solo exige

$$
\frac{r(h)}h\to0,
$$

es decir, $r(h)=o(h)$. No exige una cota cuadrática.
:::

#### Soluciones del nivel G

::: {#sol-t1-0273}
<!-- CPM-T1-SOL-0273 -->
**Solución G1.**

Sea

$$
L=f'(a)>0.
$$

Por definición,

$$
\frac{f(a+h)-f(a)}h\to L.
$$

Tomemos

$$
\varepsilon=\frac L2>0.
$$

Existe $\delta>0$ tal que, para todo incremento admisible con

$$
0<|h|<\delta,
$$

se cumple

$$
\left|
\frac{f(a+h)-f(a)}h-L
\right|
<
\frac L2.
$$

Entonces

$$
\frac{f(a+h)-f(a)}h
>
L-\frac L2
=
\frac L2
>0.
$$

Si $h>0$, multiplicar por $h$ conserva el signo:

$$
f(a+h)-f(a)>0,
$$

así que

$$
f(a+h)>f(a).
$$

Si $h<0$, multiplicar por $h$ invierte el signo:

$$
f(a+h)-f(a)<0,
$$

y por tanto

$$
f(a+h)<f(a).
$$

Sin embargo, todas estas comparaciones tienen el mismo centro $a$. No hemos demostrado que, para puntos arbitrarios $x<y$ cercanos a $a$,

$$
f(x)\le f(y).
$$

Esa afirmación exige comparar pares variables, no únicamente cada punto con $a$. Por eso el resultado es puntual y no constituye todavía un teorema de monotonía en un entorno.
:::

::: {#sol-t1-0274}
<!-- CPM-T1-SOL-0274 -->
**Solución G2.**

Supongamos primero

$$
f(a)=g(a)
$$

y

$$
f'(a)=g'(a)=L.
$$

Las linealizaciones son

$$
f(a+h)=f(a)+Lh+r_f(h),
$$

$$
g(a+h)=g(a)+Lh+r_g(h),
$$

con

$$
r_f(h)=o(h),
\qquad
r_g(h)=o(h).
$$

Restando,

$$
f(a+h)-g(a+h)
=
r_f(h)-r_g(h).
$$

Como

$$
\frac{r_f(h)-r_g(h)}h
=
\frac{r_f(h)}h-\frac{r_g(h)}h
\to0,
$$

obtenemos

$$
f(a+h)-g(a+h)=o(h).
$$

Recíprocamente, supongamos

$$
d(h):=f(a+h)-g(a+h)=o(h).
$$

Entonces

$$
\frac{d(h)}h\to0.
$$

En particular, $d(h)\to0$. Como $f$ y $g$ son diferenciables en $a$, ambas son continuas allí; por tanto,

$$
d(h)
=
f(a+h)-g(a+h)
\to
f(a)-g(a).
$$

La unicidad del límite da

$$
f(a)-g(a)=0,
$$

es decir,

$$
f(a)=g(a).
$$

Ahora, para $h\ne0$,

$$
\frac{d(h)}h
=
\frac{f(a+h)-f(a)}h
-
\frac{g(a+h)-g(a)}h,
$$

porque los valores centrales son iguales. Al tomar límites,

$$
0=f'(a)-g'(a).
$$

Así,

$$
f'(a)=g'(a).
$$

Concluimos la equivalencia completa.
:::

::: {#sol-t1-0275}
<!-- CPM-T1-SOL-0275 -->
**Solución G3.**

Para todo $x$,

$$
|f(x)|
\le x^2.
$$

Como $x^2\to0$ cuando $x\to0$, el sándwich da

$$
f(x)\to0=f(0).
$$

Por tanto, $f$ es continua en $0$.

Para $h\ne0$,

$$
\frac{f(h)-f(0)}h
=
\begin{cases}
h,&h\in\mathbb Q,\\
0,&h\notin\mathbb Q.
\end{cases}
$$

En ambos casos,

$$
\left|
\frac{f(h)-f(0)}h
\right|
\le |h|.
$$

Como $|h|\to0$,

$$
\boxed{f'(0)=0}.
$$

Ahora sea $c\ne0$. Por densidad existen sucesiones

$$
q_n\in\mathbb Q,
\qquad
q_n\to c,
$$

y

$$
r_n\notin\mathbb Q,
\qquad
r_n\to c.
$$

A lo largo de los racionales,

$$
f(q_n)=q_n^2\to c^2.
$$

A lo largo de los irracionales,

$$
f(r_n)=0\to0.
$$

Como $c\ne0$,

$$
c^2\ne0.
$$

Por el criterio secuencial, $f$ no puede ser continua en $c$. Así, $f$ es discontinua en todo punto no nulo.

Finalmente, diferenciabilidad implica continuidad. Por contraposición,

$$
\boxed{
f\text{ no es diferenciable en ningún }c\ne0.
}
$$

El ejemplo muestra que la diferenciabilidad en un solo punto no impone regularidad diferencial en un entorno completo.
:::

### Auditoría del banco

El banco materializado contiene exactamente

$$
40\text{ ejercicios}+40\text{ soluciones}
$$

con correspondencia ordinal

$$
\texttt{0236--0275}.
$$

La distribución es

$$
7A+7B+7C+6D+5E+5F+3G.
$$

Todos los ejercicios son `ORIGINAL`. La frontera demostrativa permanece dentro de los capítulos publicados desde los números reales hasta el presente: los cálculos de derivadas sencillas se hacen desde la definición; no se emplean reglas sistemáticas de suma, producto, cociente o cadena, derivación organizada de funciones elementales, Rolle, teoremas del valor medio, Taylor ni Newton.

Las pruebas de estrés del capítulo quedan cubiertas explícitamente: continuidad sin diferenciabilidad; tangentes que cruzan o vuelven a intersectar la gráfica; cociente simétrico insuficiente; pendiente no acotada sin derivada real finita; dependencia respecto del dominio; irregularidad racional/irracional; y distinción entre información puntual de $f'(a)>0$ y monotonía en un entorno.

Con este banco queda materialmente completa la redacción de §§6.1–6.11 en la numeración visible proyectada. La auditoría histórica del manuscrito original consta en `00 - Administración/T1_C07_FINAL_AUDIT_v01.md`: **PASS / COMPLETE**; la numeración de esta maqueta aún requiere validación editorial y de Quarto. Se precisó el dominio común en la comparación de primer orden y el desafío G2 (`0274`), sin alterar resultados, IDs ni secuencia de ejercicios.
