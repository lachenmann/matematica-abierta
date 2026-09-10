## Entre dos reales siempre hay más números {#sec-t1-c02-08}

### Qué significa que un conjunto sea denso

En §2.7 obtuvimos las herramientas necesarias para fabricar números entre dos reales cualesquiera. Antes de utilizarlas conviene precisar qué propiedad queremos demostrar.

::: {#def-t1-0018}
**Densidad en la recta real.** Sea $D\subseteq\mathbb R$. Diremos que $D$ es **denso en $\mathbb R$** si, para cualesquiera $a,b\in\mathbb R$ con $a<b$, existe $d\in D$ tal que

$$
a<d<b.
$$

Equivalentemente: todo intervalo abierto no vacío $(a,b)$ contiene al menos un elemento de $D$.
:::

La palabra *denso* puede inducir una imagen equivocada si se interpreta como «ocupa casi todos los puntos». No significa eso.

Un conjunto puede ser denso y, sin embargo, dejar fuera muchísimos números. Lo que la definición prohíbe es que exista un **intervalo abierto completo** que no contenga ningún elemento del conjunto.

La primera sorpresa será que los racionales son densos:

$$
\mathbb Q\text{ aparece dentro de todo intervalo abierto no vacío.}
$$

La segunda será que los irracionales también lo son.

Por tanto, ningún intervalo real, por pequeño que sea, puede estar reservado exclusivamente a una de las dos clases.

### Densidad de los racionales

::: {#thm-t1-0004}
**Densidad de $\mathbb Q$ en $\mathbb R$.** Si $a,b\in\mathbb R$ y $a<b$, entonces existe $r\in\mathbb Q$ tal que

$$
a<r<b.
$$
:::

::: {.callout-note title="Idea de la prueba"}
Un racional tiene la forma $m/n$. Así que el objetivo

$$
a<\frac mn<b
$$

se vuelve, después de multiplicar por un entero positivo $n$,

$$
na<m<nb.
$$

La pregunta es entonces: ¿podemos hacer que el intervalo $(na,nb)$ sea lo bastante ancho como para contener un entero?

La propiedad arquimediana permite escoger $n$ con

$$
\frac1n<b-a,
$$

es decir,

$$
nb-na>1.
$$

Una vez que el intervalo escalado tiene longitud mayor que $1$, el lema de encajonamiento entero de §2.7 nos proporciona el entero que necesitamos.
:::

**Demostración.** Sean $a,b\in\mathbb R$ con

$$
a<b.
$$

Entonces

$$
b-a>0.
$$

Por el corolario arquimediano existe $n\in\mathbb N_{>0}$ tal que

$$
\frac1n<b-a.
$$

Multiplicando por $n>0$ obtenemos

$$
1<n(b-a),
$$

y por tanto

$$
na+1<nb.
$$

Apliquemos ahora el lema de encajonamiento entero al número real $na$. Existe $k\in\mathbb Z$ tal que

$$
k\le na<k+1.
$$

Definamos

$$
m=k+1.
$$

Entonces $m\in\mathbb Z$ y, como $na<k+1$, tenemos

$$
na<m.
$$

Además, de $k\le na$ se sigue

$$
m=k+1\le na+1<nb.
$$

Por consiguiente,

$$
na<m<nb.
$$

Como $n>0$, podemos dividir toda la desigualdad por $n$ sin cambiar su sentido:

$$
a<\frac mn<b.
$$

Finalmente, $m\in\mathbb Z$ y $n\in\mathbb N_{>0}$, de modo que

$$
\frac mn\in\mathbb Q.
$$

Hemos construido un racional estrictamente entre $a$ y $b$. $\blacksquare$

::: {.callout-note title="Después de la prueba"}
La prueba tiene cuatro engranajes, y conviene poder reconstruirlos sin memorizar las líneas:

1. **medir el hueco:** $b-a>0$;
2. **elegir una escala fina:** $1/n<b-a$;
3. **escalar el intervalo:** $nb-na>1$;
4. **insertar un entero y desescalar:** $na<m<nb\Rightarrow a<m/n<b$.

En nuestra cadena de dependencias, la completitud entra **indirectamente**: §2.7 la utilizó para demostrar la propiedad arquimediana, y esta es la herramienta inmediata que se usa aquí.
:::

### Un ejemplo construido, no adivinado

::: {#exm-t1-0017}
**Un racional entre $\sqrt2$ y $3/2$.** Construyamos un número racional $r$ que satisfaga

$$
\sqrt2<r<\frac32.
$$
:::

Primero necesitamos una escala $1/n$ menor que el hueco

$$
\frac32-\sqrt2.
$$

La elección $n=12$ funciona porque

$$
\frac1{12}<\frac32-\sqrt2
$$

es equivalente a

$$
\sqrt2<\frac{17}{12},
$$

y esta última desigualdad puede verificarse elevando al cuadrado números positivos:

$$
2<\frac{289}{144}
$$

porque

$$
288<289.
$$

Ahora escalamos el extremo izquierdo:

$$
12\sqrt2.
$$

Sabemos que

$$
16<12\sqrt2<17,
$$

pues

$$
16^2=256<288=(12\sqrt2)^2<289=17^2.
$$

Así, el entero inmediatamente superior a $12\sqrt2$ es $17$, y al dividir por $12$ obtenemos

$$
\boxed{
\sqrt2<\frac{17}{12}<\frac32.
}
$$

El racional no apareció por ensayo decimal: fue producido por la arquitectura de la demostración.

### Densidad de los irracionales

Ahora queremos demostrar algo aparentemente más difícil:

> entre dos reales cualesquiera existe un irracional.

Podríamos intentar construirlo directamente dentro del intervalo. Hay una ruta más limpia: ya conocemos un irracional concreto, $\sqrt2$, y acabamos de demostrar que podemos insertar racionales en cualquier intervalo.

La idea será **trasladar** el intervalo.

::: {#thm-t1-0005}
**Densidad de los irracionales en $\mathbb R$.** Si $a,b\in\mathbb R$ y $a<b$, entonces existe

$$
\xi\in\mathbb R\setminus\mathbb Q
$$

tal que

$$
a<\xi<b.
$$
:::

::: {.callout-note title="Idea de la prueba"}
Restemos $\sqrt2$ a ambos extremos. Como

$$
a-\sqrt2<b-\sqrt2,
$$

la densidad racional permite escoger

$$
r\in\mathbb Q
$$

con

$$
a-\sqrt2<r<b-\sqrt2.
$$

Al volver a sumar $\sqrt2$, el número

$$
\xi=r+\sqrt2
$$

queda dentro de $(a,b)$. Y debe ser irracional: si fuese racional, al restarle el racional $r$ concluiríamos que $\sqrt2$ es racional.
:::

**Demostración.** Sean $a,b\in\mathbb R$ con $a<b$.

Restando $\sqrt2$ a ambos lados,

$$
a-\sqrt2<b-\sqrt2.
$$

Por la densidad de $\mathbb Q$ en $\mathbb R$, existe $r\in\mathbb Q$ tal que

$$
a-\sqrt2<r<b-\sqrt2.
$$

Sumando $\sqrt2$ obtenemos

$$
a<r+\sqrt2<b.
$$

Definamos

$$
\xi=r+\sqrt2.
$$

Solo falta verificar que $\xi$ es irracional. Supongamos, para obtener una contradicción, que $\xi\in\mathbb Q$. Como $r\in\mathbb Q$ y los racionales son cerrados bajo la resta, tendríamos

$$
\sqrt2=\xi-r\in\mathbb Q,
$$

contradiciendo el resultado de §2.1.

Por tanto,

$$
\xi\in\mathbb R\setminus\mathbb Q,
$$

y además $a<\xi<b$. $\blacksquare$

::: {.callout-note title="Lectura de la demostración"}
La densidad irracional no necesitó una nueva aplicación de completitud ni otra versión de la propiedad arquimediana. Una vez obtenida la densidad racional y conocido un irracional, bastó combinar:

$$
\boxed{
\text{traslación del intervalo}
+\text{densidad racional}
+\text{racional}+\text{irracional}=\text{irracional}.
}
$$

La última afirmación también ha sido demostrada dentro del argumento: si la suma fuera racional, restar el sumando racional volvería racional al irracional original.
:::

### Racionales e irracionales dentro del mismo intervalo

Volvamos al intervalo

$$
\left(\sqrt2,\frac32\right).
$$

Ya hemos construido el racional

$$
\frac{17}{12}.
$$

También podemos construir inmediatamente un irracional dentro del mismo intervalo. Como ya verificamos que

$$
\frac1{12}<\frac32-\sqrt2,
$$

tenemos

$$
\sqrt2<\sqrt2+\frac1{12}<\frac32.
$$

Y

$$
\sqrt2+\frac1{12}
$$

es irracional, porque la suma de $\sqrt2$ con un racional no puede ser racional.

Por tanto, dentro del mismo intervalo encontramos simultáneamente números de ambos tipos. Pero pertenecer al mismo intervalo no determina el orden relativo entre los puntos construidos; debemos compararlos.

En efecto,

$$
\frac{17}{12}-\left(\sqrt2+\frac1{12}\right)
=
\frac43-\sqrt2<0,
$$

porque

$$
\left(\frac43\right)^2=\frac{16}{9}<2.
$$

Así obtenemos la cadena correcta

$$
\boxed{
\sqrt2
<
\frac{17}{12}
<
\sqrt2+\frac1{12}
<
\frac32.
}
$$

::: {.callout-warning title="Error frecuente"}
Una construcción demuestra pertenencia a un intervalo, pero no autoriza a ordenar entre sí los objetos construidos sin una comparación adicional.

Este tipo de auditoría será especialmente importante cuando trabajemos con varias aproximaciones simultáneas.
:::

### Arbitrariamente cerca, sin hablar todavía de límites

La densidad puede reescribirse en un lenguaje que conecta directamente con §2.3.

Sea $x\in\mathbb R$ y sea $\varepsilon>0$. El intervalo

$$
(x-\varepsilon,x+\varepsilon)
$$

es abierto y no vacío. Por densidad contiene un racional $q$ y un irracional $\xi$. Así,

$$
|q-x|<\varepsilon,
\qquad
|\xi-x|<\varepsilon.
$$

Si queremos además que los puntos sean distintos de $x$, podemos aplicar los teoremas al intervalo $(x,x+\varepsilon)$ y obtener

$$
0<q-x<\varepsilon,
\qquad
0<\xi-x<\varepsilon.
$$

Por tanto:

$$
\boxed{
\forall x\in\mathbb R\;\forall\varepsilon>0,
\quad
\begin{array}{l}
\exists q\in\mathbb Q:\ 0<|q-x|<\varepsilon,\\[3pt]
\exists \xi\in\mathbb R\setminus\mathbb Q:\ 0<|\xi-x|<\varepsilon.
\end{array}
}
$$

Esto justifica rigurosamente la expresión «hay racionales e irracionales arbitrariamente cerca de todo real».

No estamos afirmando todavía que exista una **sucesión** de racionales o irracionales que converja a $x$. Esa reformulación pertenece al capítulo de sucesiones. Aquí solo utilizamos cuantificadores, intervalos y distancia.

### Todo intervalo abierto contiene infinitos de ambos tipos

Los teoremas de densidad garantizan al menos un punto de cada tipo. En realidad garantizan mucho más.

Tomemos un intervalo abierto no vacío $(a,b)$. Por densidad racional existe

$$
r_1\in\mathbb Q\cap(a,b).
$$

Aplicando otra vez densidad al intervalo $(a,r_1)$ obtenemos un racional distinto $r_2$. Repitiendo el argumento tantas veces como queramos, para cada $N\in\mathbb N_{>0}$ podemos producir $N$ racionales distintos dentro de $(a,b)$.

Por tanto, el intervalo contiene infinitos racionales.

El mismo argumento, usando densidad de los irracionales en cada subintervalo, muestra que contiene infinitos irracionales.

Así:

$$
\boxed{
\text{todo intervalo abierto no vacío contiene infinitos racionales e infinitos irracionales}.}
$$

Conviene notar lo que **no** hemos usado para llegar aquí: ni cardinalidades, ni teoría de conjuntos infinitos más avanzada, ni convergencia. Para descartar que haya solo una cantidad finita, basta poder producir tantos puntos distintos como cualquier número natural prefijado.

### Antes de seguir

::: {.callout-tip title="Antes de seguir"}
**1.** ¿Por qué elegimos $n$ de manera que $1/n<b-a$ en la prueba de densidad racional?

**Respuesta.** Porque eso garantiza que el intervalo escalado $(na,nb)$ tenga longitud mayor que $1$. Así, al encajonar $na$ entre enteros consecutivos, el entero siguiente todavía queda estrictamente antes de $nb$.
:::

::: {.callout-tip title="Antes de seguir"}
**2.** ¿Dónde entra la completitud en la demostración de densidad racional?

**Respuesta.** No se invoca directamente en §2.8. En nuestra arquitectura entra a través de §2.7: completitud implicó la propiedad arquimediana, que permite escoger la escala $1/n$.
:::

::: {.callout-tip title="Antes de seguir"}
**3.** ¿Por qué $r+\sqrt2$ es irracional cuando $r\in\mathbb Q$?

**Respuesta.** Si $r+\sqrt2$ fuera racional, al restarle el racional $r$ obtendríamos que $\sqrt2$ es racional, contradicción.
:::

::: {.callout-tip title="Antes de seguir"}
**4.** ¿Que $\mathbb Q$ sea denso significa que todo real es racional?

**Respuesta.** No. Significa que todo intervalo abierto no vacío contiene racionales. El propio $\sqrt2$ es irracional y, sin embargo, hay racionales arbitrariamente cerca de él.
:::

### Lo que exporta esta sección

Ahora conocemos dos hechos simultáneos:

$$
\boxed{
\mathbb Q\text{ es denso en }\mathbb R,
\qquad
\mathbb R\setminus\mathbb Q\text{ es denso en }\mathbb R.
}
$$

Por tanto, la recta no se divide en regiones racionales e irracionales. Ambas clases están entrelazadas a toda escala de intervalo.

La cadena estructural construida en las últimas secciones es ya considerable:

$$
\boxed{
\text{completitud}
\to
\text{propiedad arquimediana}
\to
\text{mallas }1/n
\to
\text{densidad racional}
\to
\text{densidad irracional}.}
$$

En §2.9 volveremos a la completitud desde otra dirección. En lugar de insertar puntos dentro de un intervalo, estudiaremos una familia de intervalos cerrados que se van encajando unos dentro de otros y preguntaremos:

> si continuamos estrechando indefinidamente, ¿queda necesariamente algún punto común?

La respuesta será el **principio de intervalos encajados**, y su prueba volverá a utilizar el supremo.
