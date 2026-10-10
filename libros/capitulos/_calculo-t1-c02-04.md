## Cotas, máximos, mínimos, supremos e ínfimos {#sec-t1-c02-04}

### De estar cerca a tener una frontera

En §1.2 aprendimos a medir cercanía. Podemos decir que un punto $x$ está a distancia menor que $r$ de $a$ escribiendo

$$
|x-a|<r.
$$

El cambio de pregunta es también un cambio de escala. La condición anterior compara un punto con otro; hablar de una frontera para un conjunto exigirá comparar un mismo candidato con **todos** los elementos del conjunto a la vez.

Pero la pregunta planteada en la introducción es diferente: ¿qué significaría que el conjunto de números cuyo cuadrado es menor que $2$ tuviera una frontera? Antes de examinar ese conjunto necesitamos distinguir preguntas que en el lenguaje informal suelen mezclarse:

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

El orden de los cuantificadores importa: primero se fija el candidato $M$ y después debe verificarse la desigualdad $a\le M$ para **todo** $a\in A$. Por negación,

$$
M\text{ no es cota superior de }A
\iff
\exists a\in A\text{ tal que }a>M.
$$

De manera dual,

$$
m\text{ no es cota inferior de }A
\iff
\exists a\in A\text{ tal que }a<m.
$$

Por ejemplo, para

$$
A=(0,1),
$$

los números

$$
1,\ 2,\ 10,\ 10^6
$$

son todos cotas superiores. También lo es cualquier real $M\ge1$.

En cambio, $0.9$ no es una cota superior. Basta exhibir un elemento de $(0,1)$ que la supere; por ejemplo,

$$
\frac{19}{20}\in(0,1)
\qquad\text{y}\qquad
\frac{19}{20}>\frac9{10}=0.9.
$$

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

Máximo y mínimo, cuando existen, son únicos. En efecto, si $M$ y $N$ fueran dos máximos de $A$, entonces $M,N\in A$; como $M$ es máximo, $N\le M$, y como $N$ es máximo, $M\le N$. Por antisimetría,

$$
M=N.
$$

El argumento para el mínimo es dual. Por eso las notaciones $\max A$ y $\min A$ designan, cuando existen, números determinados.

::: {#exm-t1-0014}
**Una cota superior que no es máximo.** Consideremos

$$
A=(0,1).
$$

El número $1$ es una cota superior de $A$, pero $A$ no tiene máximo.
:::

**¿Por qué no hay máximo?** Tomemos un elemento cualquiera $a\in(0,1)$. Como $a<1$, al sumar $a$ y después $1$ obtenemos

$$
2a<a+1<2.
$$

Dividiendo por $2>0$,

$$
a<\frac{a+1}{2}<1.
$$

Definamos

$$
b=\frac{a+1}{2}.
$$

Entonces $b\in A$ y $b>a$.

Como el punto $a\in A$ fue arbitrario, hemos probado

$$
\forall a\in A\;\exists b\in A
\qquad
a<b.
$$

Por tanto, ningún elemento de $A$ puede ser máximo: desde cualquiera de ellos podemos construir otro elemento permitido situado más a la derecha.

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

El argumento muestra una técnica general: para negar que un conjunto tenga máximo, tomamos un elemento arbitrario y construimos otro elemento permitido que lo supera. En §1.4 aplicaremos una técnica semejante, menos inmediata, al conjunto de racionales positivos cuyo cuadrado es menor que $2$.

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

Conviene leer lentamente estas definiciones. En la definición de supremo intervienen dos comparaciones universales distintas. La primera dice

$$
\forall a\in A,\qquad a\le s,
$$

y compara el candidato $s$ con los **elementos del conjunto**. La segunda puede escribirse

$$
\forall u\in\mathbb R,
\qquad
\left[
\bigl(\forall a\in A,\ a\le u\bigr)
\Longrightarrow
s\le u
\right],
$$

y compara $s$ con **todas las cotas superiores** posibles.

Por tanto, demostrar que $s=\sup A$ exige dos trabajos diferentes:

$$
\boxed{
\text{$s$ domina a todos los elementos de $A$}
\quad+\quad
\text{toda cota superior domina a $s$}.
}
$$

La lectura del ínfimo es exactamente dual:

$$
\forall a\in A,\qquad i\le a,
$$

y, para toda cota inferior $\ell$,

$$
\ell\le i.
$$

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

Ya demostramos que $A$ no tiene máximo. En cambio,

$$
\max B=1,
$$

porque $1\in B$ y todo $b\in B$ satisface $b\le1$.

La relación entre máximo y supremo puede formularse ahora sin ambigüedad.

Si $A$ tiene máximo $M$, entonces $M$ es una cota superior de $A$. Además, si $u$ es cualquier otra cota superior, como $M\in A$ debe cumplirse

$$
M\le u.
$$

Por tanto, $M$ es la menor cota superior y

$$
\boxed{\sup A=\max A=M.}
$$

Recíprocamente, supongamos que $s=\sup A$ existe y que además

$$
s\in A.
$$

Como $s$ es una cota superior,

$$
\forall a\in A,\qquad a\le s.
$$

La pertenencia $s\in A$ y esta desigualdad universal son precisamente las dos condiciones que definen al máximo. Luego

$$
\boxed{\max A=s=\sup A.}
$$

En consecuencia, siempre que $\sup A$ exista,

$$
\boxed{
A\text{ tiene máximo}
\iff
\sup A\in A,
}
$$

y, en ese caso,

$$
\max A=\sup A.
$$

La afirmación dual es igualmente válida: si $\inf A$ existe, entonces

$$
A\text{ tiene mínimo}
\iff
\inf A\in A,
$$

y, cuando esto ocurre,

$$
\min A=\inf A.
$$

Aplicado a $B=(0,1]$, el máximo ya identificado nos permite concluir inmediatamente

$$
\sup B=\max B=1.
$$

Para $A=(0,1)$ sabemos, en cambio, que no hay máximo. Todavía falta justificar que $1$ es efectivamente su supremo: esa demostración será el objeto del microtramo siguiente.

### Por qué $1$ es realmente el supremo de $(0,1)$

Probemos ahora las dos cláusulas de la definición de supremo.

**1. El número $1$ es una cota superior.** Sea $x\in(0,1)$. Por definición del intervalo,

$$
0<x<1.
$$

En particular,

$$
x\le1.
$$

Como $x$ fue arbitrario,

$$
\forall x\in(0,1),\qquad x\le1.
$$

Por tanto, $1$ es una cota superior de $(0,1)$.

**2. Toda cota superior está por encima de $1$.** Sea $u$ una cota superior cualquiera de $(0,1)$. Como

$$
\frac12\in(0,1),
$$

la definición de cota superior obliga a que

$$
\frac12\le u.
$$

Supongamos, para obtener una contradicción, que

$$
u<1.
$$

Definamos

$$
b=\frac{u+1}{2}.
$$

De $u<1$, sumando primero $u$ y después $1$, obtenemos

$$
2u<u+1<2.
$$

Como $2>0$, al dividir por $2$ resulta

$$
u<b<1.
$$

Además, $u\ge1/2>0$, de modo que $b>u>0$. Por tanto,

$$
b\in(0,1).
$$

Pero $b>u$, lo que contradice que $u$ sea una cota superior de $(0,1)$.

La suposición $u<1$ es imposible. Por tricotomía,

$$
1\le u.
$$

Como $u$ era una cota superior arbitraria, toda cota superior de $(0,1)$ domina a $1$. Junto con la primera parte, esto demuestra

$$
\boxed{\sup(0,1)=1.}
$$

El argumento inferior es dual, pero podemos dejarlo también explícito. El número $0$ es una cota inferior porque

$$
0<x
$$

para todo $x\in(0,1)$. Sea ahora $\ell$ cualquier cota inferior. Como $1/2\in(0,1)$,

$$
\ell\le\frac12.
$$

Si supusiéramos $\ell>0$, el número

$$
c=\frac{\ell}{2}
$$

satisfaría

$$
0<c<\ell
$$

y, como $\ell\le1/2<1$,

$$
c<1.
$$

Así $c\in(0,1)$, pero $c<\ell$, contradiciendo que $\ell$ fuera una cota inferior. Por tanto, toda cota inferior satisface

$$
\ell\le0.
$$

Concluimos

$$
\boxed{\inf(0,1)=0.}
$$

En particular, este intervalo tiene supremo e ínfimo aunque ninguno de los dos pertenezca al conjunto.

### El supremo es único

La definición de supremo contiene ya su unicidad.

Supongamos que $s$ y $t$ son ambos supremos de un mismo conjunto $A$. Como $t$ es un supremo, en particular es una cota superior de $A$. Pero $s$ es la menor cota superior, así que

$$
s\le t.
$$

Ahora intercambiamos los papeles. Como $s$ es una cota superior de $A$ y $t$ es la menor cota superior,

$$
t\le s.
$$

Tenemos, por tanto,

$$
s\le t
\qquad\text{y}\qquad
t\le s.
$$

Por antisimetría del orden,

$$
\boxed{s=t}.
$$

Así, un conjunto no puede tener dos supremos distintos: **si el supremo existe, es único**.

La demostración para el ínfimo es dual. Si $i$ y $j$ fueran ambos ínfimos de $A$, entonces $j$ sería una cota inferior y la maximalidad de $i$ daría $j\le i$; intercambiando los papeles obtendríamos $i\le j$. Por antisimetría,

$$
\boxed{i=j}.
$$

En consecuencia,

$$
\boxed{
\text{si }\sup A\text{ existe, es único;}
\qquad
\text{si }\inf A\text{ existe, es único.}
}
$$

Conviene separar esta afirmación de una cuestión distinta: aquí hemos demostrado **unicidad**, no **existencia**. El argumento dice que puede haber a lo sumo un número con la propiedad de ser supremo o ínfimo; todavía no hemos probado que todo conjunto apropiado posea uno.

Por eso las expresiones

$$
\sup A,
\qquad
\inf A
$$

tienen sentido como números determinados una vez que su existencia ha sido establecida.

### Una caracterización operativa: acercarse tanto como queramos

La definición de supremo compara $s$ con **todas las cotas superiores**. Esa formulación es conceptualmente exacta, pero en las demostraciones necesitaremos una versión más operativa.

Si $s$ es el supremo, ningún intervalo inmediatamente situado por debajo de $s$ puede quedar completamente vacío de elementos de $A$. La expresión «acercarnos tanto como queramos» puede formularse sin límites, usando solo desigualdades y cuantificadores.

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

En la segunda condición para el supremo, la desigualdad $a\le s$ ya viene garantizada por la primera condición; la conservamos escrita porque muestra geométricamente que $a$ pertenece a la franja

$$
(s-\varepsilon,s].
$$

Del mismo modo, en la caracterización del ínfimo la condición $i\le a$ procede de que $i$ es una cota inferior y permite visualizar la franja

$$
[i,i+\varepsilon).
$$

::: {.callout-note title="Idea de la prueba"}
Si $s$ fuera el supremo pero existiera una franja $(s-\varepsilon,s]$ sin elementos de $A$, entonces $s-\varepsilon$ seguiría estando por encima de todo el conjunto. Habríamos encontrado una cota superior menor que $s$, contradiciendo que $s$ es la menor.

En la dirección inversa, si podemos encontrar elementos de $A$ arbitrariamente cerca de $s$ por debajo, ninguna cota superior puede situarse estrictamente por debajo de $s$: algún elemento del conjunto la sobrepasaría.

Para el ínfimo ocurre exactamente la imagen reflejada: una franja $[i,i+\varepsilon)$ no puede quedar vacía, y ninguna cota inferior puede situarse estrictamente por encima de $i$.
:::

**Demostración para el supremo.** Supongamos primero que

$$
s=\sup A.
$$

Por definición, $s$ es una cota superior. Sea ahora $\varepsilon>0$.

Supongamos que no existe ningún $a\in A$ tal que

$$
s-\varepsilon<a.
$$

Negar la existencia significa que, para todo $a\in A$,

$$
\neg(s-\varepsilon<a).
$$

Como el orden es total, esta negación equivale a

$$
a\le s-\varepsilon.
$$

Por tanto,

$$
\forall a\in A,\qquad a\le s-\varepsilon,
$$

de modo que $s-\varepsilon$ sería una cota superior de $A$. Pero, como $\varepsilon>0$,

$$
s-\varepsilon<s,
$$

lo que contradice que $s$ sea la menor cota superior.

Luego existe $a\in A$ tal que

$$
s-\varepsilon<a.
$$

Como $s$ es cota superior, además $a\le s$. Así,

$$
s-\varepsilon<a\le s.
$$

Esto prueba la propiedad aproximativa.

Recíprocamente, supongamos que $s$ es una cota superior y que

$$
\forall\varepsilon>0\;\exists a\in A
\qquad
s-\varepsilon<a\le s.
$$

Queremos demostrar que $s$ es la **menor** cota superior. Sea $u$ una cota superior cualquiera de $A$.

Supongamos, para obtener una contradicción, que

$$
u<s.
$$

Entonces

$$
\varepsilon=s-u>0.
$$

Por la propiedad aproximativa existe $a\in A$ tal que

$$
s-\varepsilon<a\le s.
$$

Pero

$$
s-\varepsilon
=
s-(s-u)
=
u,
$$

así que

$$
u<a.
$$

Esto contradice que $u$ sea una cota superior, pues toda cota superior debe satisfacer $a\le u$ para cada $a\in A$.

Por tanto, $u<s$ es imposible. Como $u$ era una cota superior arbitraria,

$$
s\le u
$$

para toda cota superior $u$ de $A$. Así, $s$ es la menor cota superior y

$$
s=\sup A.
$$

**Demostración para el ínfimo.** Supongamos ahora que

$$
i=\inf A.
$$

Entonces $i$ es una cota inferior. Sea $\varepsilon>0$.

Si no existiera ningún $a\in A$ con

$$
a<i+\varepsilon,
$$

entonces, para todo $a\in A$,

$$
a\ge i+\varepsilon.
$$

Por tanto, $i+\varepsilon$ sería una cota inferior de $A$. Pero

$$
i<i+\varepsilon,
$$

lo que contradice que $i$ sea la **mayor** cota inferior.

Luego existe $a\in A$ tal que

$$
a<i+\varepsilon.
$$

Como $i$ es cota inferior, además $i\le a$. Por tanto,

$$
i\le a<i+\varepsilon.
$$

Recíprocamente, supongamos que $i$ es una cota inferior y que

$$
\forall\varepsilon>0\;\exists a\in A
\qquad
i\le a<i+\varepsilon.
$$

Sea $\ell$ una cota inferior cualquiera de $A$. Queremos demostrar

$$
\ell\le i.
$$

Supongamos, por contradicción, que

$$
i<\ell.
$$

Tomemos

$$
\varepsilon=\ell-i>0.
$$

Por la propiedad aproximativa existe $a\in A$ tal que

$$
a<i+\varepsilon=\ell.
$$

Pero esto contradice que $\ell$ sea una cota inferior, pues debería cumplirse

$$
\ell\le a.
$$

Por tanto, ninguna cota inferior puede ser mayor que $i$. Así,

$$
i=\inf A.
$$

$\blacksquare$

::: {.callout-note title="El orden de los cuantificadores no se puede intercambiar"}
La propiedad del supremo dice

$$
\forall\varepsilon>0\;\exists a_\varepsilon\in A
\qquad
s-\varepsilon<a_\varepsilon\le s.
$$

El elemento $a_\varepsilon$ **puede depender de** $\varepsilon$. No estamos afirmando

$$
\exists a\in A\;\forall\varepsilon>0
\qquad
s-\varepsilon<a\le s.
$$

Esta segunda afirmación sería mucho más fuerte. En efecto, si un mismo $a\in A$ funcionara para todo $\varepsilon>0$ y tuviéramos $a<s$, podríamos elegir

$$
\varepsilon=\frac{s-a}{2}>0.
$$

Entonces

$$
s-\varepsilon
=
\frac{s+a}{2}
>
a,
$$

contradiciendo $s-\varepsilon<a$. Por tanto tendría que cumplirse $a=s$, y en consecuencia $s\in A$: el supremo sería además un máximo.

Así, el patrón

$$
\forall\varepsilon>0\;\exists a_\varepsilon
$$

expresa aproximación a una frontera sin exigir que la frontera pertenezca al conjunto.
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

Estudiemos ahora el extremo inferior. Si $x\in C$, entonces o bien $x\in(-2,1]$ o bien $x=4$; en ambos casos

$$
-2<x.
$$

Por tanto, $-2$ es una cota inferior de $C$. Sin embargo,

$$
-2\notin C,
$$

de modo que $-2$ no puede ser mínimo.

Esto todavía no basta para concluir que $C$ carece de mínimo: podría existir otro elemento del conjunto que fuese el menor. Debemos descartarlo.

Sea $x\in C$ arbitrario. Si $x=4$, podemos tomar

$$
y=1\in C,
$$

y entonces $y<x$.

Si, en cambio, $x\in(-2,1]$, definimos

$$
y=\frac{x-2}{2}.
$$

Como $x>-2$,

$$
y+2
=
\frac{x+2}{2}
>0,
$$

y por tanto $y>-2$. Además,

$$
x-y
=
\frac{x+2}{2}
>0,
$$

de modo que $y<x$. Puesto que $y<x\le1$, concluimos

$$
y\in(-2,1]\subset C.
$$

Así, en todos los casos,

$$
\forall x\in C\;\exists y\in C
\qquad
y<x.
$$

Ningún elemento de $C$ puede ser, por tanto, su mínimo.

Falta comprobar que $-2$ no es solamente una cota inferior, sino la **mayor** cota inferior. Utilicemos la caracterización aproximativa del ínfimo. Sea $\varepsilon>0$. Necesitamos encontrar $a\in C$ tal que

$$
-2\le a<-2+\varepsilon.
$$

Si $0<\varepsilon\le2$, tomamos

$$
a=-2+\frac{\varepsilon}{2}.
$$

Entonces

$$
-2<a<-2+\varepsilon,
$$

y además

$$
-2<a\le-1<1,
$$

de modo que $a\in(-2,1]\subset C$.

Si $\varepsilon>2$, basta tomar

$$
a=-1\in C,
$$

pues

$$
-2<-1<-2+\varepsilon.
$$

Hemos mostrado que para todo $\varepsilon>0$ existe $a\in C$ con

$$
-2\le a<-2+\varepsilon.
$$

Como $-2$ es una cota inferior, @prp-t1-0010 permite concluir

$$
\boxed{\inf C=-2}.
$$

Así, este único ejemplo reúne las cuatro nociones:

$$
\boxed{
\max C=\sup C=4,
\qquad
\inf C=-2,
\qquad
C\text{ no tiene mínimo}.
}
$$

### No todo conjunto tiene máximo, ni todo conjunto tiene una cota

Conviene separar tres fenómenos: estar acotado, alcanzar una frontera y poseer siquiera una barrera en una dirección.

El conjunto

$$
(0,1)
$$

está acotado superior e inferiormente, pero no tiene máximo ni mínimo. En cambio,

$$
[0,1]
$$

también está acotado y sí alcanza ambas fronteras:

$$
\min[0,1]=0,
\qquad
\max[0,1]=1.
$$

Por tanto, estar acotado no obliga a que exista un elemento extremo. En particular,

$$
\boxed{
A\text{ tiene máximo}
\Longrightarrow
A\text{ está acotado superiormente},
}
$$

pero la implicación recíproca es falsa, como muestra $(0,1)$.

Consideremos ahora

$$
(0,\infty).
$$

Este conjunto está acotado inferiormente —por ejemplo, por $0$—, pero no está acotado superiormente. Negar la existencia de una cota superior significa precisamente afirmar

$$
\forall M\in\mathbb R\;\exists x\in(0,\infty)
\qquad
x>M.
$$

Fijemos, pues, un candidato arbitrario $M\in\mathbb R$. Si $M>0$, tomamos

$$
x=M+1;
$$

si $M\le0$, tomamos

$$
x=1.
$$

En ambos casos $x\in(0,\infty)$ y $x>M$. Como esto funciona para todo $M$, ninguna cota superior existe.

En consecuencia, $(0,\infty)$ no puede tener máximo: un máximo sería, por definición, una cota superior que además pertenece al conjunto. Tampoco puede tener supremo, porque un supremo debe ser ante todo una cota superior.

Hay todavía otra razón para exigir cuidado con las hipótesis. El conjunto vacío

$$
\varnothing
$$

está acotado superiormente en el sentido de la definición: dado cualquier $M\in\mathbb R$, no existe ningún elemento de $\varnothing$ que pueda violar la condición $a\le M$. Por tanto, **todo** real es una cota superior de $\varnothing$.

Sin embargo, $\varnothing$ no tiene supremo real. En efecto, si $s$ fuera la menor cota superior, entonces $s-1$ también sería una cota superior y

$$
s-1<s,
$$

contradiciendo la minimalidad de $s$.

Así aparecen de manera natural las dos hipótesis que más adelante acompañarán a la propiedad de existencia del supremo:

$$
\boxed{
A\ne\varnothing
\qquad+\qquad
A\text{ acotado superiormente}.
}
$$

Hasta aquí solo hemos comprobado que ambas condiciones son relevantes. **Todavía no hemos demostrado que basten** para garantizar la existencia de un supremo. Afirmar esa suficiencia será precisamente la nueva propiedad de $\mathbb R$ que introduciremos en §1.5.

### Antes de seguir

::: {.callout-tip title="Antes de seguir"}
**1.** Sea

$$
A=[-2,0)\cup(1,3).
$$

Determina $\sup A$, $\inf A$ y decide si existen máximo y mínimo.

**Respuesta.** Todo elemento de $A$ es menor o igual que $3$, de modo que $3$ es una cota superior.

Para demostrar que es la menor, sea $\varepsilon>0$ y definamos

$$
\delta=\min\left\{\frac{\varepsilon}{2},\frac12\right\}>0,
\qquad
a=3-\delta.
$$

Como $\delta\le1/2$,

$$
\frac52\le a<3,
$$

así que $a\in(1,3)\subset A$. Además, $\delta<\varepsilon$, y por tanto

$$
3-\varepsilon<a\le3.
$$

La caracterización aproximativa @prp-t1-0010 da entonces

$$
\boxed{\sup A=3}.
$$

Como $3\notin A$, el resultado «máximo $\Leftrightarrow$ supremo perteneciente al conjunto» muestra que $A$ no tiene máximo.

En el extremo inferior, todo elemento de $A$ satisface

$$
-2\le a,
$$

y además $-2\in A$. Por tanto,

$$
\boxed{\min A=-2}.
$$

Todo mínimo es también el ínfimo, luego

$$
\boxed{\inf A=\min A=-2}.
$$
:::

::: {.callout-tip title="Antes de seguir"}
**2.** Sea $A\ne\varnothing$ y $s=\sup A$. Demuestra que, para todo $t<s$, existe $a\in A$ tal que

$$
t<a\le s.
$$

**Respuesta.** Sea $t<s$ arbitrario. Entonces

$$
\varepsilon=s-t>0.
$$

La caracterización aproximativa del supremo produce un elemento $a\in A$ tal que

$$
s-\varepsilon<a\le s.
$$

Como

$$
s-\varepsilon
=
s-(s-t)
=
t,
$$

obtenemos

$$
t<a\le s.
$$

Como $t<s$ fue arbitrario, esto vale para todo real situado estrictamente por debajo de $s$.
:::

### El punto al que hemos llegado

La pregunta introductoria acerca de $x^2=2$ nos llevó a pensar en una frontera. Ahora disponemos del lenguaje necesario para distinguir tres situaciones que al comienzo podían confundirse.

Una **cota superior** $M$ satisface

$$
\forall a\in A,\qquad a\le M,
$$

pero no necesita pertenecer a $A$.

Un **máximo** $M$ satisface simultáneamente

$$
M\in A
\qquad\text{y}\qquad
\forall a\in A,\ a\le M.
$$

Un **supremo** $s$ es una cota superior con una exigencia adicional: ninguna otra cota superior puede quedar estrictamente por debajo de él. Cuando existe,

$$
\boxed{
s=\sup A
\iff
\begin{cases}
a\le s & \text{para todo }a\in A,\\
s\le u & \text{para toda cota superior }u\text{ de }A.
\end{cases}
}
$$

También hemos demostrado que, cuando existe, el supremo es único. Y si además

$$
\sup A\in A,
$$

entonces esa frontera es alcanzada y coincide con el máximo.

La caracterización aproximativa ofrece otra lectura de la misma frontera. Para un conjunto no vacío, una vez que $s$ es cota superior,

$$
s=\sup A
$$

equivale a exigir

$$
\boxed{
\forall\varepsilon>0\;\exists a_\varepsilon\in A
\qquad
s-\varepsilon<a_\varepsilon\le s.
}
$$

Así, el supremo puede no pertenecer al conjunto, pero ningún descenso positivo desde $s$ sigue quedando por encima de todos sus elementos.

Hay, sin embargo, una cuestión que §1.3 **no** ha resuelto. Todas estas afirmaciones nos permiten reconocer, comparar y caracterizar un supremo **si existe**; no garantizan todavía su existencia.

La pregunta decisiva queda entonces formulada con precisión:

> si $A\subseteq\mathbb R$ es no vacío y está acotado superiormente, ¿existe necesariamente una menor cota superior real?

Los axiomas de cuerpo y orden no bastan para responder afirmativamente. En §1.4 veremos de manera concreta qué puede fallar dentro de $\mathbb Q$ mediante la ecuación

$$
x^2=2,
$$

y en §1.5 incorporaremos la propiedad adicional de $\mathbb R$ que garantiza la existencia de esas fronteras bajo las hipótesis apropiadas:

$$
\boxed{\text{la completitud}.}
$$

