## Cotas, máximos, mínimos, supremos e ínfimos {#sec-t1-c02-04}

### De estar cerca a tener una frontera

En §2.3 aprendimos a medir cercanía. Podemos decir que un punto $x$ está a distancia menor que $r$ de $a$ escribiendo

$$
|x-a|<r.
$$

Pero el problema que quedó abierto desde §2.1 es diferente. Allí aparecieron conjuntos de racionales cuyos elementos se acercaban cada vez más a un borde sin alcanzarlo. Para describir esa situación necesitamos distinguir preguntas que en el lenguaje informal suelen mezclarse:

- ¿hay algún número que quede por encima de todos los elementos del conjunto?;
- ¿hay un elemento del propio conjunto que sea el mayor de todos?;
- si existen números que quedan por encima, ¿cuál es el menor de ellos?

Las tres preguntas son distintas.

La diferencia entre ellas será una de las ideas estructurales más importantes del capítulo.

### Cotas: barreras que no tienen por qué pertenecer al conjunto

::: {#def-t1-0015}
**Cotas y acotación.** Sea $A\subseteq\mathbb R$.

Un número $M\in\mathbb R$ es una **cota superior** de $A$ si

$$
\forall a\in A,\qquad a\le M.
$$

Un número $m\in\mathbb R$ es una **cota inferior** de $A$ si

$$
\forall a\in A,\qquad m\le a.
$$

Decimos que $A$ está **acotado superiormente** si posee al menos una cota superior, y **acotado inferiormente** si posee al menos una cota inferior. Decimos que $A$ está **acotado** si está acotado en ambos sentidos.
:::

La palabra decisiva es **barrera**. Una cota superior $M$ debe encontrarse a la derecha de todo el conjunto, pero no tiene por qué tocarlo ni pertenecer a él.

Por ejemplo, para

$$
A=(0,1),
$$

los números

$$
1,\ 2,\ 10,\ 10^6
$$

son todos cotas superiores. También lo es cualquier real $M\ge1$.

En cambio, $0.9$ no es una cota superior, porque existen elementos de $(0,1)$ mayores que $0.9$.

Del mismo modo, cualquier real $m\le0$ es una cota inferior de $(0,1)$.

::: {.callout-warning title="Error frecuente"}
Una cota superior **no tiene que pertenecer al conjunto**.

En

$$
A=(0,1),
$$

el número $1$ es una cota superior aunque

$$
1\notin A.
$$

Confundir «ser una cota» con «ser un elemento» hará imposible comprender correctamente el supremo.
:::

### Máximo y mínimo: extremos que sí pertenecen al conjunto

La noción cambia cuando exigimos que la barrera sea además un elemento del propio conjunto.

::: {#def-t1-0016}
**Máximo y mínimo.** Sea $A\subseteq\mathbb R$.

Un elemento $M\in A$ es el **máximo** de $A$ si

$$
\forall a\in A,\qquad a\le M.
$$

Un elemento $m\in A$ es el **mínimo** de $A$ si

$$
\forall a\in A,\qquad m\le a.
$$

Cuando existen, escribimos

$$
M=\max A,
\qquad
m=\min A.
$$
:::

Así, un máximo cumple simultáneamente dos condiciones:

$$
\boxed{
M\in A
\qquad\text{y}\qquad
M\text{ es una cota superior de }A.
}
$$

La primera condición es precisamente la que una cota superior arbitraria no necesita satisfacer.

::: {#exm-t1-0014}
**Una cota superior que no es máximo.** Consideremos

$$
A=(0,1).
$$

El número $1$ es una cota superior de $A$, pero $A$ no tiene máximo.
:::

**¿Por qué no hay máximo?** Tomemos un elemento cualquiera $a\in(0,1)$. Como $a<1$, el punto medio entre $a$ y $1$,

$$
b=\frac{a+1}{2},
$$

satisface

$$
a<b<1.
$$

Por tanto, $b\in A$ y $b>a$. Ningún elemento de $A$ puede ser el mayor, porque desde cualquiera de ellos podemos construir otro elemento del conjunto situado más a la derecha.

Observa la diferencia:

$$
\boxed{
1\text{ está por encima de todo }A,
\quad
pero\quad
1\notin A.
}
$$

Por eso $1$ puede ser una cota superior sin ser máximo.

El razonamiento recuerda inmediatamente a §2.1: allí Rudin construía, desde cualquier racional con cuadrado menor que $2$, otro racional mayor que seguía teniendo cuadrado menor que $2$. Esa construcción demostraba que el conjunto correspondiente no tenía mayor elemento. Ahora poseemos el lenguaje exacto para decirlo.

### Una cota superior especial: la menor de todas

En $(0,1)$ existen infinitas cotas superiores. Sin embargo, una de ellas ocupa una posición privilegiada: $1$.

No porque pertenezca al conjunto —no pertenece—, sino porque no existe una cota superior más pequeña.

Esta es la idea de **supremo**.

::: {#def-t1-0017}
**Supremo e ínfimo.** Sea $A\subseteq\mathbb R$.

Un número $s\in\mathbb R$ es el **supremo** de $A$ si:

1. $s$ es una cota superior de $A$;
2. si $u$ es cualquier cota superior de $A$, entonces
   $$
   s\le u.
   $$

Es decir, $s$ es la **menor cota superior** de $A$. Cuando existe, escribimos

$$
s=\sup A.
$$

De manera dual, un número $i\in\mathbb R$ es el **ínfimo** de $A$ si:

1. $i$ es una cota inferior de $A$;
2. si $\ell$ es cualquier cota inferior de $A$, entonces
   $$
   \ell\le i.
   $$

Es decir, $i$ es la **mayor cota inferior** de $A$. Cuando existe, escribimos

$$
i=\inf A.
$$
:::

Conviene leer lentamente estas definiciones.

El supremo no es «el número más grande del conjunto». Esa frase describe, cuando existe, al **máximo**.

El supremo es

$$
\boxed{\text{la más pequeña entre todas las barreras superiores}.}
$$

El ínfimo es

$$
\boxed{\text{la más grande entre todas las barreras inferiores}.}
$$

Esta diferencia de una palabra —«elemento» frente a «cota»— cambia toda la teoría.

### Máximo frente a supremo

Volvamos a dos intervalos muy parecidos:

$$
A=(0,1),
\qquad
B=(0,1].
$$

En ambos casos,

$$
\sup A=1,
\qquad
\sup B=1.
$$

Pero

$$
\max A\text{ no existe},
\qquad
\max B=1.
$$

¿Qué cambió? Solo la pertenencia del punto frontera:

$$
1\notin A,
\qquad
1\in B.
$$

De aquí obtenemos una regla muy útil:

> Si $\sup A$ existe, entonces $A$ tiene máximo exactamente cuando $\sup A\in A$; en ese caso,
> $$
> \max A=\sup A.
> $$

La afirmación dual vale para mínimo e ínfimo.

::: {.callout-note title="Lectura de la definición"}
Para probar que $s=\sup A$ hay **dos trabajos**:

1. demostrar que $s$ está por encima de todos los elementos de $A$;
2. demostrar que ninguna cota superior puede quedar por debajo de $s$.

Probar solamente el primer punto demuestra que $s$ es **una** cota superior, no que sea el supremo.
:::

### Por qué $1$ es realmente el supremo de $(0,1)$

Ya sabemos que $1$ es una cota superior. Falta demostrar que es la menor.

Sea $u$ una cota superior cualquiera de $(0,1)$. Como $1/2\in(0,1)$, necesariamente

$$
u\ge\frac12.
$$

Supongamos que $u<1$. Entonces

$$
b=\frac{u+1}{2}
$$

satisface

$$
u<b<1.
$$

Además, como $u\ge1/2$, tenemos $b>0$, de modo que $b\in(0,1)$. Pero $b>u$, lo que contradice que $u$ fuese una cota superior.

Por tanto, toda cota superior $u$ cumple

$$
1\le u.
$$

Como $1$ es una cota superior y es menor o igual que cualquier otra,

$$
\boxed{\sup(0,1)=1.}
$$

La misma idea da

$$
\inf(0,1)=0,
$$

aunque ni $0$ ni $1$ pertenezcan al intervalo.

### El supremo es único

¿Podría un conjunto tener dos supremos diferentes?

No.

Si $s$ y $t$ fueran ambos supremos de $A$, entonces $t$ sería una cota superior y, como $s$ es la menor cota superior,

$$
s\le t.
$$

Intercambiando los papeles,

$$
t\le s.
$$

Por antisimetría del orden,

$$
s=t.
$$

La misma demostración muestra que el ínfimo, cuando existe, también es único.

Por eso las expresiones

$$
\sup A,
\qquad
\inf A
$$

tienen sentido como números determinados, siempre que su existencia haya sido establecida.

### Una caracterización operativa: acercarse tanto como queramos

La definición de supremo compara $s$ con **todas las cotas superiores**. Esa formulación es conceptualmente exacta, pero en las demostraciones necesitaremos una versión más operativa.

Si $s$ es el supremo, podemos acercarnos a $s$ desde abajo mediante elementos de $A$ tanto como queramos.

La palabra «acercarnos» puede expresarse sin límites, usando solo desigualdades y cuantificadores.

::: {#prp-t1-0010}
**Caracterización aproximativa del supremo y del ínfimo.** Sea $A\subseteq\mathbb R$ no vacío.

Un número $s\in\mathbb R$ satisface

$$
s=\sup A
$$

si y solo si se cumplen las dos condiciones siguientes:

1. $s$ es una cota superior de $A$;
2. para todo $\varepsilon>0$ existe $a\in A$ tal que
   $$
   s-\varepsilon<a\le s.
   $$

De manera dual,

$$
i=\inf A
$$

si y solo si:

1. $i$ es una cota inferior de $A$;
2. para todo $\varepsilon>0$ existe $a\in A$ tal que
   $$
   i\le a<i+\varepsilon.
   $$
:::

::: {.callout-note title="Idea de la prueba"}
Si $s$ fuera el supremo pero existiera una franja $(s-\varepsilon,s]$ sin elementos de $A$, entonces $s-\varepsilon$ seguiría estando por encima de todo el conjunto. Habríamos encontrado una cota superior menor que $s$, contradiciendo que $s$ es la menor.

En la dirección inversa, si podemos encontrar elementos de $A$ arbitrariamente cerca de $s$ por debajo, ninguna cota superior puede situarse estrictamente por debajo de $s$: algún elemento del conjunto la sobrepasaría.
:::

**Demostración para el supremo.** Supongamos primero que

$$
s=\sup A.
$$

Por definición, $s$ es una cota superior. Sea ahora $\varepsilon>0$.

Si no existiera ningún $a\in A$ con

$$
s-\varepsilon<a,
$$

entonces todos los elementos de $A$ satisfarían

$$
a\le s-\varepsilon.
$$

Por tanto, $s-\varepsilon$ sería una cota superior de $A$. Pero

$$
s-\varepsilon<s,
$$

lo que contradice que $s$ sea la menor cota superior. Luego existe $a\in A$ tal que

$$
s-\varepsilon<a.
$$

Como $s$ es cota superior, además $a\le s$. Así,

$$
s-\varepsilon<a\le s.
$$

Recíprocamente, supongamos que $s$ es una cota superior y que, para todo $\varepsilon>0$, existe $a\in A$ con

$$
s-\varepsilon<a\le s.
$$

Queremos probar que $s$ es la **menor** cota superior. Sea $u$ cualquier cota superior de $A$.

Supongamos, para obtener una contradicción, que

$$
u<s.
$$

Tomemos

$$
\varepsilon=s-u>0.
$$

Por la propiedad aproximativa existe $a\in A$ tal que

$$
s-\varepsilon<a.
$$

Pero

$$
s-\varepsilon
=
s-(s-u)
=
u,
$$

por lo que

$$
u<a.
$$

Esto contradice que $u$ sea una cota superior de $A$. Por tanto, toda cota superior $u$ satisface

$$
s\le u.
$$

Así, $s$ es la menor cota superior y

$$
s=\sup A.
$$

La demostración para el ínfimo es exactamente dual: se invierten las desigualdades y se aproxima el borde desde arriba. $\blacksquare$

::: {.callout-note title="Después de la prueba"}
Aquí aparece por primera vez una forma cuantificada que será central en análisis:

$$
\forall\varepsilon>0\;\exists a\in A
\quad
s-\varepsilon<a\le s.
$$

Todavía no hay límites. La expresión dice algo puramente ordenado: **ninguna franja positiva inmediatamente debajo de $s$ puede quedar vacía de elementos de $A$**.

El orden de cuantificadores importa. El elemento $a$ puede depender de $\varepsilon$.
:::

### Ejemplos de lectura completa

::: {#exm-t1-0015}
**Máximo, mínimo, supremo e ínfimo en un conjunto elemental.** Sea

$$
C=(-2,1]\cup\{4\}.
$$

Entonces

$$
\sup C=4,
\qquad
\max C=4,
$$

mientras que

$$
\inf C=-2
$$

y $C$ no tiene mínimo.
:::

La parte superior es inmediata porque $4\in C$ y todo elemento de $C$ es menor o igual que $4$. Por tanto, $4$ es máximo y, en consecuencia, también supremo.

En el extremo inferior, $-2$ es una cota inferior, pero

$$
-2\notin C.
$$

No hay mínimo: si $x\in(-2,1]$, entonces el punto medio

$$
\frac{x-2}{2}
$$

satisface

$$
-2<\frac{x-2}{2}<x,
$$

por lo que siempre podemos encontrar otro elemento de $C$ menor que $x$. El punto $4$ evidentemente tampoco puede ser mínimo.

Para comprobar que $-2$ es el ínfimo, podemos usar la caracterización aproximativa. Dado $\varepsilon>0$, necesitamos un elemento de $C$ situado en

$$
[-2,-2+\varepsilon).
$$

Si $0<\varepsilon\le2$, podemos tomar

$$
a=-2+\frac{\varepsilon}{2},
$$

que pertenece a $(-2,1]\subset C$ y satisface

$$
-2<a<-2+\varepsilon.
$$

Si $\varepsilon>2$, basta tomar, por ejemplo, $a=-1\in C$, pues

$$
-2<-1<-2+\varepsilon.
$$

Así, ningún número mayor que $-2$ puede seguir siendo una cota inferior, y

$$
\inf C=-2.
$$

### No todo conjunto tiene máximo, ni todo conjunto tiene una cota

Conviene separar varios fenómenos.

El conjunto

$$
(0,1)
$$

está acotado, pero no tiene máximo ni mínimo.

El conjunto

$$
[0,1]
$$

está acotado y sí tiene ambos:

$$
\min[0,1]=0,
\qquad
\max[0,1]=1.
$$

En cambio,

$$
(0,\infty)
$$

no está acotado superiormente. Para cualquier candidato $M\in\mathbb R$, existe un elemento del conjunto mayor que él; por ejemplo, si $M>0$, podemos tomar $M+1$, y si $M\le0$, basta tomar $1$.

Por tanto, hablar de «la menor cota superior» carece de sentido si primero no hay ninguna cota superior.

Esta observación anticipa dos hipótesis que aparecerán en el axioma de completitud:

$$
\boxed{
\text{conjunto no vacío}
\quad+\quad
\text{acotado superiormente}.
}
$$

Todavía no afirmaremos que esas dos condiciones basten para garantizar la existencia de un supremo. Esa será precisamente la nueva propiedad de $\mathbb R$ que introduciremos en §2.5.

### Antes de seguir

::: {.callout-tip title="Antes de seguir"}
**1.** Sea

$$
A=[-3,2).
$$

Determina si existen $\max A$, $\min A$, $\sup A$ e $\inf A$.

**Respuesta.** Como $-3\in A$ y todo elemento de $A$ es mayor o igual que $-3$,

$$
\min A=-3,
\qquad
\inf A=-3.
$$

En el extremo superior, $2$ es la menor cota superior, pero $2\notin A$. Por tanto,

$$
\sup A=2,
$$

y $A$ no tiene máximo.
:::

::: {.callout-tip title="Antes de seguir"}
**2.** Si $s=\sup A$ y $\varepsilon=10^{-3}$, ¿qué garantiza la caracterización aproximativa?

**Respuesta.** Garantiza que existe algún $a\in A$ tal que

$$
s-10^{-3}<a\le s.
$$

No afirma que haya un único elemento ni que podamos escoger el mismo $a$ para todos los valores de $\varepsilon$.
:::

::: {.callout-tip title="Antes de seguir"}
**3.** ¿Puede un número ser simultáneamente supremo y máximo de un conjunto?

**Respuesta.** Sí. Ocurre exactamente cuando el supremo pertenece al conjunto. Por ejemplo,

$$
\sup[0,1]=\max[0,1]=1.
$$
:::

::: {.callout-tip title="Antes de seguir"}
**4.** ¿Por qué demostrar que $5$ es una cota superior de $A$ no basta para concluir que $\sup A=5$?

**Respuesta.** Porque quizá exista otra cota superior menor que $5$. Para probar que $5$ es el supremo debemos demostrar además que **ninguna** cota superior está por debajo de $5$.
:::

### El punto al que hemos llegado

Desde §2.1 venimos hablando informalmente de una frontera entre dos regiones racionales. Ahora podemos decir exactamente qué tipo de objeto buscamos.

Un supremo no tiene que ser un elemento del conjunto. Su función es registrar la frontera superior mediante dos propiedades simultáneas:

$$
\boxed{
\text{está por encima de todo el conjunto}
\quad+\quad
\text{no puede bajarse ni una cantidad positiva sin dejar de estarlo}.
}
$$

La segunda propiedad se expresa de manera operativa como

$$
\forall\varepsilon>0\;\exists a\in A
\qquad
s-\varepsilon<a\le s.
$$

Pero hemos definido el supremo **condicionalmente**: hemos dicho qué debe cumplir si existe.

Nos falta la pregunta decisiva:

> si un subconjunto no vacío de $\mathbb R$ está acotado superiormente, ¿tenemos siempre derecho a afirmar que existe una menor cota superior real?

La respuesta será sí, pero no se deduce de los axiomas de cuerpo y orden estudiados hasta ahora. De hecho, §2.1 ya nos mostró un sistema —$\mathbb Q$— donde esa garantía falla.

En §2.5 formularemos por fin la propiedad adicional que distingue a la recta real:

$$
\boxed{\text{la completitud}.}
$$
