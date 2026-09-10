## Completitud en acción: existencia de raíces {#sec-t1-c02-06}

### La frontera ya existe; ahora debemos identificarla

Al final de §2.5 llegamos a un punto que habría sido imposible justificar al comienzo del capítulo. Para el conjunto

$$
S_{\mathbb R}=\{x\in\mathbb R:x\ge0,\ x^2<2\}
$$

la completitud garantiza la existencia de un número real

$$
\alpha=\sup S_{\mathbb R}.
$$

Por primera vez sabemos rigurosamente que la región situada «por debajo de $2$» posee una frontera real. Pero todavía falta demostrar que esa frontera es exactamente el número que buscábamos desde §2.1.

La pregunta es:

$$
\boxed{\text{¿por qué debe cumplirse }\alpha^2=2?}
$$

No utilizaremos continuidad de la función $x\mapsto x^2$, porque la continuidad todavía no ha sido definida. Tampoco utilizaremos límites ni sucesiones convergentes. Toda la prueba deberá salir de tres recursos que ya poseemos:

- las propiedades del orden;
- la definición de supremo;
- la completitud, utilizada para garantizar que el supremo existe.

La idea que resolverá el problema es muy general. Si una frontera propuesta no tiene exactamente la propiedad que esperamos, intentaremos **perturbarla ligeramente** y demostrar que deja de poder ser un supremo.

### Qué significaría que el supremo estuviese en el lugar equivocado

Sustituyamos temporalmente el número $2$ por un real positivo arbitrario $a$. Consideremos

$$
S_a=\{x\in\mathbb R:x\ge0,\ x^2<a\}.
$$

Si la completitud nos proporciona

$$
\alpha=\sup S_a,
$$

hay solamente tres posibilidades:

$$
\alpha^2<a,
\qquad
\alpha^2=a,
\qquad
\alpha^2>a.
$$

La igualdad es precisamente lo que deseamos. Así que debemos comprender por qué las otras dos posibilidades son incompatibles con la condición de supremo.

Si

$$
\alpha^2<a,
$$

entonces queda un margen positivo

$$
a-\alpha^2>0.
$$

Debería ser posible movernos un poco hacia la derecha, hasta $\alpha+h$, sin hacer que el cuadrado alcance todavía a $a$. Pero entonces $\alpha+h$ pertenecería a $S_a$ y sería mayor que $\alpha$, contradiciendo que $\alpha$ sea una cota superior.

En cambio, si

$$
\alpha^2>a,
$$

hay un exceso positivo

$$
\alpha^2-a>0.
$$

Debería ser posible movernos un poco hacia la izquierda y encontrar $c<\alpha$ cuyo cuadrado siga siendo mayor que $a$. Si $c^2>a$, entonces todo $x\in S_a$ debe satisfacer $x<c$; por tanto, $c$ sería una cota superior de $S_a$ menor que $\alpha$. Eso contradice que $\alpha$ sea la **menor** cota superior.

Tenemos, pues, dos tipos de contradicción:

$$
\boxed{
\begin{array}{ccl}
\alpha^2<a&\Longrightarrow&\text{elemento de }S_a\text{ mayor que }\alpha,\\[4pt]
\alpha^2>a&\Longrightarrow&\text{cota superior menor que }\alpha.
\end{array}
}
$$

El problema técnico consiste únicamente en diseñar las perturbaciones con suficiente control algebraico.

### Cómo se diseña una perturbación controlada

El primer caso nos pide controlar

$$
(\alpha+h)^2
=
\alpha^2+h(2\alpha+h).
$$

Si sabemos que $\alpha^2<a$, llamemos

$$
\delta=a-\alpha^2>0.
$$

Queremos que

$$
h(2\alpha+h)<\delta.
$$

Una manera sencilla de garantizarlo consiste en imponer primero $h<\alpha$. Entonces

$$
2\alpha+h<3\alpha,
$$

y basta exigir además

$$
3\alpha h<\delta.
$$

Así aparece una elección de $h$ que no es adivinatoria: surge de las desigualdades que necesitamos satisfacer.

El segundo caso admite una elección todavía más reveladora. Si

$$
\alpha^2>a,
$$

queremos disminuir $\alpha$ sin atravesar el nivel $a$. Sea

$$
E=\alpha^2-a>0.
$$

Probemos a restar

$$
\frac{E}{2\alpha}.
$$

Definimos

$$
c
=
\alpha-\frac{\alpha^2-a}{2\alpha}
=
\frac12\left(\alpha+\frac{a}{\alpha}\right).
$$

Entonces $c<\alpha$, pero el nuevo defecto puede calcularse exactamente:

$$
\begin{aligned}
c^2-a
&=
\left(\alpha-\frac{\alpha^2-a}{2\alpha}\right)^2-a\\
&=
\frac{(\alpha^2-a)^2}{4\alpha^2}\\
&>0.
\end{aligned}
$$

Por tanto,

$$
c^2>a.
$$

La corrección ha reducido el error sin cambiar su signo. Esta es la misma filosofía que ya vimos al descomprimir el ejemplo de Rudin:

$$
\boxed{
\text{medir el defecto}
\to
\text{elegir una corrección}
\to
\text{controlar algebraicamente el nuevo defecto}.
}
$$

Ahora podemos ejecutar la prueba completa.

::: {#thm-t1-0002}
**Existencia y unicidad de la raíz cuadrada no negativa.** Para todo número real $a\ge0$ existe un único número real $\alpha\ge0$ tal que

$$
\alpha^2=a.
$$

Cuando $a>0$, este número es positivo.
:::

::: {.callout-note title="Idea de la prueba"}
Para $a>0$ construiremos el candidato como

$$
\alpha=\sup\{x\ge0:x^2<a\}.
$$

La completitud garantiza que este $\alpha$ existe. Luego descartaremos las posibilidades $\alpha^2<a$ y $\alpha^2>a$ mediante las dos perturbaciones preparadas arriba. La unicidad será un argumento separado: dos raíces no negativas del mismo número deben coincidir.
:::

**Demostración.** Si $a=0$, el número $0$ satisface $0^2=0$. Además, si $x\ge0$ y $x^2=0$, entonces $x$ no puede ser positivo, porque $x>0$ implicaría $x^2>0$. Por tanto, necesariamente $x=0$, y el resultado es inmediato en este caso.

Supongamos ahora que $a>0$ y definamos

$$
S_a=\{x\in\mathbb R:x\ge0,\ x^2<a\}.
$$

Antes de utilizar completitud debemos verificar sus hipótesis.

**1. $S_a$ es no vacío.** De hecho, el número

$$
r=\frac{a}{1+a}
$$

es positivo y pertenece a $S_a$. En efecto,

$$
r^2=\frac{a^2}{(1+a)^2}<a,
$$

porque

$$
a<(1+a)^2
$$

para todo $a>0$.

**2. $S_a$ está acotado superiormente.** El número $a+1$ es una cota superior. Si existiera $x\in S_a$ con $x\ge a+1$, como ambos números son no negativos tendríamos

$$
x^2\ge(a+1)^2>a,
$$

lo que contradice $x^2<a$.

Podemos aplicar entonces el axioma de completitud. Existe

$$
\alpha=\sup S_a.
$$

Además, como $r\in S_a$ y $r>0$,

$$
\alpha\ge r>0.
$$

Tenemos tres casos posibles.

**Caso 1: supongamos que $\alpha^2<a$.** Definamos

$$
\delta=a-\alpha^2>0
$$

y elijamos

$$
h=\frac12\min\left\{\alpha,\frac{\delta}{3\alpha}\right\}.
$$

Entonces $h>0$, $h<\alpha$ y

$$
h<\frac{\delta}{3\alpha}.
$$

Como $h<\alpha$,

$$
2\alpha+h<3\alpha.
$$

Por tanto,

$$
\begin{aligned}
(\alpha+h)^2
&=\alpha^2+h(2\alpha+h)\\
&<\alpha^2+3\alpha h\\
&<\alpha^2+\delta\\
&=a.
\end{aligned}
$$

Así,

$$
\alpha+h\in S_a.
$$

Pero $h>0$, de modo que

$$
\alpha+h>\alpha,
$$

lo cual contradice que $\alpha$ sea una cota superior de $S_a$.

Por consiguiente,

$$
\alpha^2<a
$$

es imposible.

**Caso 2: supongamos que $\alpha^2>a$.** Definamos

$$
c
=
\alpha-\frac{\alpha^2-a}{2\alpha}.
$$

Como $a>0$ y $\alpha>0$, también podemos escribir

$$
c=\frac{\alpha^2+a}{2\alpha}>0.
$$

Además, $\alpha^2-a>0$, por lo que

$$
c<\alpha.
$$

Por el cálculo preparado antes,

$$
c^2-a
=
\frac{(\alpha^2-a)^2}{4\alpha^2}>0,
$$

así que

$$
c^2>a.
$$

Veamos ahora que $c$ es una cota superior de $S_a$. Si $x\in S_a$, entonces

$$
0\le x,
\qquad
x^2<a<c^2,
\qquad
c>0.
$$

Si fuese $x\ge c$, la monotonía del cuadrado para números no negativos daría

$$
x^2\ge c^2>a,
$$

contradiciendo $x^2<a$. Por tanto,

$$
x<c.
$$

Por tanto, todo elemento de $S_a$ es menor que $c$, de modo que $c$ es una cota superior de $S_a$.

Pero acabamos de demostrar también que

$$
c<\alpha.
$$

Esto contradice que $\alpha$ sea la **menor** cota superior de $S_a$.

Por consiguiente,

$$
\alpha^2>a
$$

es imposible.

Como las dos desigualdades estrictas son imposibles, la tricotomía obliga a que

$$
\boxed{\alpha^2=a.}
$$

Esto demuestra la existencia.

Falta la unicidad. Supongamos que $u,v\ge0$ satisfacen

$$
u^2=a,
\qquad
v^2=a.
$$

Entonces

$$
u^2-v^2=0,
$$

y por factorización,

$$
(u-v)(u+v)=0.
$$

Si $a>0$, tanto $u$ como $v$ son positivos, de modo que $u+v>0$. Por tanto,

$$
u-v=0,
$$

es decir,

$$
u=v.
$$

El caso $a=0$ ya fue resuelto al comienzo. Por consiguiente, para todo $a\ge0$ existe exactamente una raíz cuadrada no negativa. $\blacksquare$

### Dónde entró realmente la completitud

La demostración es larga, pero la nueva propiedad de $\mathbb R$ se utilizó en un lugar muy preciso:

$$
S_a\ne\varnothing,
\quad
S_a\text{ acotado superiormente}
\quad\Longrightarrow\quad
\boxed{\alpha=\sup S_a\text{ existe}}.
$$

Todo lo que vino después fue álgebra y orden.

Esto permite distinguir dos tareas:

1. **la completitud fabrica el candidato** al garantizar la existencia de la frontera;
2. **las perturbaciones identifican el candidato** al demostrar que su cuadrado no puede quedar ni por debajo ni por encima de $a$.

La estructura completa es, por tanto,

$$
\boxed{
\text{conjunto adecuado}
\to
\text{supremo}
\to
\text{perturbaciones}
\to
\text{ecuación exacta}
\to
\text{unicidad}.
}
$$

Este patrón reaparecerá muchas veces en análisis: primero se construye un objeto mediante una propiedad de existencia; después se demuestra que posee exactamente la característica buscada.

### Ahora sí podemos definir $\sqrt a$

Hasta este punto habíamos evitado cuidadosamente utilizar la notación de raíz cuadrada como si su existencia fuese automática.

El teorema anterior nos autoriza finalmente a hacer la siguiente convención.

Para cada $a\ge0$, escribiremos

$$
\boxed{\sqrt a}
$$

para designar **el único número real no negativo** cuyo cuadrado es $a$.

Así,

$$
(\sqrt a)^2=a,
\qquad
\sqrt a\ge0.
$$

Si $a<0$, no existe ningún número real cuyo cuadrado sea $a$, porque todo cuadrado real es no negativo. Por tanto, dentro de $\mathbb R$ la notación $\sqrt a$ se reserva aquí para $a\ge0$.

Es importante leer correctamente la definición. Si $a>0$, la ecuación

$$
x^2=a
$$

no tiene una única solución real. Tiene exactamente dos:

$$
\boxed{x=\sqrt a\quad\text{o}\quad x=-\sqrt a.}
$$

La unicidad demostrada en el teorema es la unicidad de la **raíz no negativa**.

### La raíz que faltaba desde §2.1

Podemos regresar finalmente a la ecuación

$$
x^2=2.
$$

Como $2>0$, el teorema garantiza que existe un único número real positivo

$$
\sqrt2
$$

tal que

$$
(\sqrt2)^2=2.
$$

Además,

$$
1^2<2<2^2,
$$

y la monotonía del cuadrado en los no negativos nos da

$$
1<\sqrt2<2.
$$

En §2.1 demostramos que ningún racional tiene cuadrado igual a $2$. Por tanto,

$$
\boxed{\sqrt2\in\mathbb R\setminus\mathbb Q.}
$$

Ahora sí hemos probado las dos afirmaciones que al comienzo debían mantenerse separadas:

$$
\boxed{
\begin{array}{c}
\text{existe un número real positivo cuyo cuadrado es }2,\\[3pt]
\text{y ese número no es racional.}
\end{array}
}
$$

El «hueco» de los racionales ha sido ocupado dentro de $\mathbb R$, no mediante una aproximación decimal ni mediante una suposición geométrica, sino como consecuencia de la completitud.

### Una prueba sin continuidad

Conviene notar algo que adquirirá importancia cuando estudiemos funciones.

Más adelante podremos demostrar la existencia de raíces usando resultados de continuidad, por ejemplo mediante un teorema de valor intermedio. Pero ese camino no está disponible aquí y, sobre todo, **no debe utilizarse para fundamentar las herramientas que luego ayudarán a demostrar esos mismos teoremas de continuidad**.

Nuestra cadena lógica ha sido deliberadamente la contraria:

$$
\boxed{
\text{completitud}
\to
\text{existencia de raíces}
\to
\text{herramientas para el análisis posterior}.
}
$$

No hemos utilizado:

- límites;
- convergencia de sucesiones;
- continuidad;
- teorema del valor intermedio;
- Bolzano–Weierstrass.

La prueba es enteramente una prueba de orden y completitud.

### Antes de seguir

::: {.callout-tip title="Antes de seguir"}
**1.** ¿Por qué no bastaba con definir

$$
\alpha=\sup S_a
$$

y afirmar inmediatamente que $\alpha^2=a$?

**Respuesta.** Porque la definición de supremo solo caracteriza a $\alpha$ como una frontera de $S_a$. La igualdad $\alpha^2=a$ es una propiedad adicional que debe demostrarse. Precisamente para eso se descartan los casos $\alpha^2<a$ y $\alpha^2>a$.
:::

::: {.callout-tip title="Antes de seguir"}
**2.** En el caso $\alpha^2<a$, ¿qué parte de la definición de supremo se contradice?

**Respuesta.** Que $\alpha$ sea una **cota superior**. Construimos $\alpha+h\in S_a$ con $\alpha+h>\alpha$.
:::

::: {.callout-tip title="Antes de seguir"}
**3.** En el caso $\alpha^2>a$, ¿qué parte se contradice?

**Respuesta.** Que $\alpha$ sea la **menor** cota superior. Construimos una cota superior $c$ que satisface $c<\alpha$.
:::

::: {.callout-tip title="Antes de seguir"}
**4.** ¿Por qué el teorema no dice que $x^2=a$ tiene una única solución cuando $a>0$?

**Respuesta.** Porque entonces hay dos soluciones reales, $\sqrt a$ y $-\sqrt a$. Lo que es único es el número **no negativo** cuyo cuadrado es $a$.
:::

### Del primer hueco a una herramienta permanente

La ecuación $x^2=2$ fue elegida al comienzo del capítulo porque exhibía una insuficiencia concreta de $\mathbb Q$. Pero el resultado obtenido es mucho más general:

$$
\boxed{
\forall a\ge0\quad\exists!\,\alpha\ge0\quad \alpha^2=a.
}
$$

La completitud no se limitó a añadir un número especial llamado $\sqrt2$. Garantizó de una sola vez la existencia de una familia completa de objetos que el álgebra elemental utiliza constantemente.

En §2.7 extraeremos una consecuencia de naturaleza distinta. Ya no preguntaremos por una ecuación, sino por el tamaño de los números naturales dentro de la recta real. Demostraremos que

$$
\mathbb N
$$

no puede quedar atrapado bajo ninguna cota real. Esa es la **propiedad arquimediana**, y también resultará ser una consecuencia de la completitud.
