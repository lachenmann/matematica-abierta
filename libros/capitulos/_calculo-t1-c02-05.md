## Completitud: la propiedad que falta en $\mathbb Q$ {#sec-t1-c02-05}

### Una definición no garantiza una existencia

En §2.4 aprendimos a reconocer un supremo cuando tenemos un candidato. Para demostrar que $s=\sup A$ verificamos dos hechos: que $s$ es una cota superior y que ninguna cota superior puede ser menor que $s$.

Pero esa definición deja abierta una cuestión diferente:

> ¿qué ocurre si $A$ es no vacío y está acotado superiormente, pero no sabemos de antemano cuál debería ser su menor cota superior?

Nada de lo demostrado hasta ahora garantiza que esa menor cota exista dentro del sistema numérico en el que estamos trabajando.

Esta distinción es fundamental. Una definición responde a la pregunta

$$
\boxed{\text{¿qué propiedades tendría el objeto si existiera?}}
$$

mientras que un teorema o un axioma de existencia responde a otra:

$$
\boxed{\text{¿tenemos derecho a afirmar que tal objeto existe?}}
$$

En §2.1 ya vimos una advertencia de este tipo: conocer la ecuación $x^2=2$ no nos autorizaba todavía a suponer que existía una solución positiva en nuestro dominio. Ahora aparece el mismo problema en un nivel estructural.

### El axioma de completitud {#sec-t1-c02-completeness-axiom}

Adoptaremos como propiedad fundamental de $\mathbb R$ el siguiente enunciado.

::: {.callout-important title="Axioma de completitud"}
Todo subconjunto no vacío $A\subseteq\mathbb R$ que esté acotado superiormente posee un supremo en $\mathbb R$.

En símbolos, si

$$
A\ne\varnothing
$$

y existe $M\in\mathbb R$ tal que

$$
a\le M
\qquad\text{para todo }a\in A,
$$

entonces existe $s\in\mathbb R$ tal que

$$
s=\sup A.
$$
:::

La fuerza del axioma está en una sola palabra: **existe**.

Antes de §2.5 podíamos decir:

> si $A$ tiene supremo, entonces ese supremo es único y puede caracterizarse mediante cotas y aproximación desde abajo.

Ahora podemos añadir:

> si $A\subseteq\mathbb R$ es no vacío y está acotado superiormente, entonces ese supremo existe.

Por tanto,

$$
\boxed{
A\ne\varnothing
\quad+\quad
A\text{ acotado superiormente}
\quad\Longrightarrow\quad
\exists\sup A\in\mathbb R.
}
$$

### ¿Por qué lo llamamos axioma?

Dentro del desarrollo que hemos elegido, la completitud no se deduce de los axiomas de cuerpo y orden. La **adoptamos** como una propiedad adicional de los números reales.

Esto no significa que sea una afirmación inmotivada ni que en todos los tratamientos deba aparecer necesariamente como axioma. Si se construye $\mathbb R$ a partir de objetos más elementales —por ejemplo, mediante cortes de Dedekind o clases apropiadas de sucesiones racionales—, la propiedad correspondiente de completitud debe demostrarse como un teorema acerca de la construcción realizada.

Nuestro objetivo aquí es distinto. No estamos construyendo los reales desde cero; estamos identificando la estructura mínima que necesitaremos para hacer cálculo rigurosamente. En esta presentación,

$$
\boxed{
\text{estructura axiomática de }\mathbb R
=
\text{cuerpo ordenado}
+
\text{completitud}
}
$$

es una caracterización estructural, no una receta de construcción.

::: {.callout-note title="Terminología"}
En este capítulo, **completitud** significa específicamente la propiedad del supremo recién enunciada. Más adelante aparecerán formulaciones distintas pero relacionadas —por ejemplo, mediante sucesiones de Cauchy—. No las utilizaremos aquí para justificar este axioma, porque la teoría rigurosa de sucesiones todavía no ha sido desarrollada.
:::

### Qué autoriza el axioma y qué no

Para aplicar completitud debemos verificar **antes** sus dos hipótesis:

$$
A\ne\varnothing,
\qquad
A\text{ está acotado superiormente}.
$$

Si alguna falla, el axioma no dice nada.

Por ejemplo, para

$$
A=(0,\infty)
$$

no podemos invocar completitud para obtener un supremo real, porque $A$ no está acotado superiormente.

Tampoco el axioma afirma que $\sup A\in A$. El conjunto

$$
A=(0,1)
$$

es no vacío y acotado superiormente, y por tanto tiene supremo; ya sabemos que

$$
\sup A=1,
$$

aunque $1\notin A$.

Finalmente, el axioma garantiza **existencia**, pero no nos entrega automáticamente una fórmula para el supremo ni sus propiedades adicionales. Esas deberán obtenerse mediante argumentos posteriores.

Este punto será visible inmediatamente en el conjunto que preparará la existencia de la raíz de $2$.

### El ínfimo no necesita un segundo axioma

El axioma fue formulado únicamente para conjuntos acotados **superiormente**. Podríamos añadir una versión dual para conjuntos acotados inferiormente, pero sería redundante.

::: {#prp-t1-0011}
**Existencia de ínfimos a partir del axioma de completitud.** Todo subconjunto no vacío $A\subseteq\mathbb R$ que esté acotado inferiormente posee un ínfimo en $\mathbb R$.
:::

::: {.callout-note title="Idea de la prueba"}
En lugar de buscar directamente el mayor de los límites inferiores de $A$, reuniremos **todas las cotas inferiores** de $A$ en un nuevo conjunto. Ese conjunto estará acotado superiormente. La completitud producirá entonces su supremo, y ese supremo resultará ser precisamente $\inf A$.
:::

**Demostración.** Sea $A\subseteq\mathbb R$ no vacío y acotado inferiormente. Definamos

$$
L=\{\ell\in\mathbb R:\ell\le a\text{ para todo }a\in A\}.
$$

Así, $L$ es el conjunto de todas las cotas inferiores de $A$.

Como $A$ está acotado inferiormente, existe al menos una cota inferior. Por tanto,

$$
L\ne\varnothing.
$$

Como $A$ es no vacío, podemos escoger $a_0\in A$. Toda $\ell\in L$ satisface

$$
\ell\le a_0,
$$

porque $\ell$ es cota inferior de **todos** los elementos de $A$. Luego $a_0$ es una cota superior de $L$. Por tanto, $L$ está acotado superiormente.

El axioma de completitud puede aplicarse a $L$. Existe entonces

$$
s=\sup L.
$$

Mostremos que $s=\inf A$.

Sea $a\in A$ arbitrario. Por definición de $L$, toda $\ell\in L$ cumple

$$
\ell\le a.
$$

Así, $a$ es una cota superior de $L$. Como $s$ es la **menor** cota superior de $L$,

$$
s\le a.
$$

Esto vale para todo $a\in A$, de modo que $s$ es una cota inferior de $A$.

Ahora sea $\ell$ cualquier cota inferior de $A$. Entonces $\ell\in L$, y como $s=\sup L$,

$$
\ell\le s.
$$

Hemos demostrado que $s$ es una cota inferior de $A$ y que ninguna cota inferior puede ser mayor que $s$. Por definición,

$$
\boxed{s=\inf A.}
$$

$\blacksquare$

::: {.callout-note title="Después de la prueba"}
La completitud se utilizó una sola vez: para garantizar que $L$, por ser no vacío y estar acotado superiormente, tenía supremo.

Todo lo demás fue trabajo de definiciones y orden. Por eso no necesitamos postular por separado una «propiedad del ínfimo».
:::

### Ahora volvamos a $\mathbb Q$

La importancia del axioma sería difícil de apreciar si también fuera válido en $\mathbb Q$. Pero no lo es.

Consideremos nuevamente

$$
S_{\mathbb Q}
=
\{q\in\mathbb Q:q\ge0,\ q^2<2\}.
$$

Este conjunto es no vacío porque

$$
1\in S_{\mathbb Q}.
$$

También está acotado superiormente dentro de $\mathbb Q$. Por ejemplo, $2$ es una cota superior: si $q\ge2$, entonces, como $q\ge0$,

$$
q^2\ge4>2,
$$

de modo que tal $q$ no puede pertenecer a $S_{\mathbb Q}$.

Tenemos, pues,

$$
\boxed{
S_{\mathbb Q}\ne\varnothing
\qquad\text{y}\qquad
S_{\mathbb Q}\text{ está acotado superiormente en }\mathbb Q.
}
$$

Si $\mathbb Q$ tuviera la propiedad de completitud que acabamos de adoptar para $\mathbb R$, este conjunto debería poseer un supremo racional.

No lo posee.

::: {#prp-t1-0012}
**Fallo de la propiedad del supremo en $\mathbb Q$.** El conjunto

$$
S_{\mathbb Q}
=
\{q\in\mathbb Q:q\ge0,\ q^2<2\}
$$

es no vacío y está acotado superiormente en $\mathbb Q$, pero no tiene supremo en $\mathbb Q$.
:::

::: {.callout-note title="Idea de la prueba"}
Supongamos que existe un supremo racional $s$. Como $s\in\mathbb Q$, su cuadrado debe caer en exactamente uno de tres casos:

$$
s^2<2,
\qquad
s^2=2,
\qquad
s^2>2.
$$

La transformación de Rudin estudiada en §2.1 permitirá destruir los casos primero y tercero; el segundo ya fue excluido por la irracionalidad demostrada al comienzo del capítulo.
:::

**Demostración.** Supongamos, para obtener una contradicción, que existe

$$
s=\sup_{\mathbb Q}S_{\mathbb Q}
$$

con $s\in\mathbb Q$.

Como $1\in S_{\mathbb Q}$ y $s$ es una cota superior,

$$
s\ge1.
$$

En particular, $s+2>0$. Definamos, exactamente como en §2.1,

$$
T(s)
=
s-\frac{s^2-2}{s+2}
=
\frac{2(s+1)}{s+2}.
$$

Como $s\in\mathbb Q$, también $T(s)\in\mathbb Q$, y como $s\ge1$, tenemos $T(s)>0$.

Ya demostramos las dos identidades decisivas

$$
T(s)-s
=
\frac{2-s^2}{s+2},
$$

$$
T(s)^2-2
=
\frac{2(s^2-2)}{(s+2)^2}.
$$

Consideremos los tres casos posibles.

**Caso 1: $s^2<2$.** Entonces

$$
T(s)-s>0,
$$

de modo que $T(s)>s$. Además,

$$
T(s)^2-2<0.
$$

Por tanto,

$$
T(s)\in S_{\mathbb Q}
$$

y $T(s)>s$. Esto contradice que $s$ sea una cota superior de $S_{\mathbb Q}$.

**Caso 2: $s^2>2$.** Ahora

$$
T(s)<s
$$

y

$$
T(s)^2>2.
$$

Afirmamos que $T(s)$ sigue siendo una cota superior de $S_{\mathbb Q}$. En efecto, si existiera $q\in S_{\mathbb Q}$ con

$$
q\ge T(s),
$$

entonces, como $q\ge0$ y $T(s)>0$, la monotonía del cuadrado en $[0,\infty)$ daría

$$
q^2\ge T(s)^2>2,
$$

contradiciendo $q^2<2$.

Así, todo $q\in S_{\mathbb Q}$ satisface

$$
q<T(s).
$$

Por consiguiente, $T(s)$ es una cota superior racional de $S_{\mathbb Q}$ y

$$
T(s)<s.
$$

Esto contradice que $s$ sea la **menor** cota superior.

**Caso 3: $s^2=2$.** Este caso es imposible porque en §2.1 demostramos que ningún número racional tiene cuadrado igual a $2$.

Los tres casos conducen a contradicción. Por tanto, $S_{\mathbb Q}$ no posee supremo en $\mathbb Q$. $\blacksquare$

### Qué hizo realmente la transformación de Rudin

En §2.1 la fórmula

$$
T(p)=p-\frac{p^2-2}{p+2}
$$

podía parecer una técnica ingeniosa para acercarnos a un borde todavía informal.

Ahora su función estructural queda completamente visible.

Si un candidato racional $s$ queda **por debajo** del borde, la transformación produce otro racional permitido que está más arriba:

$$
s^2<2
\quad\Longrightarrow\quad
s<T(s),\qquad T(s)^2<2.
$$

Por tanto, $s$ no puede ser cota superior.

Si el candidato queda **por encima**, la transformación produce una cota superior racional más pequeña:

$$
s^2>2
\quad\Longrightarrow\quad
T(s)<s,\qquad T(s)^2>2.
$$

Por tanto, $s$ no puede ser la menor cota superior.

Y el único tercer lugar imaginable,

$$
s^2=2,
$$

no existe dentro de $\mathbb Q$.

Así, el «hueco» de §2.1 puede formularse ahora con total precisión:

$$
\boxed{
\mathbb Q\text{ contiene un conjunto no vacío y acotado superiormente que no tiene supremo en }\mathbb Q.
}
$$

Esto, y no simplemente la frase informal «faltan irracionales», es el fracaso de completitud que nos interesa.

### El mismo problema dentro de $\mathbb R$

Ahora cambiemos de sistema ambiente. Consideremos

$$
S_{\mathbb R}
=
\{x\in\mathbb R:x\ge0,\ x^2<2\}.
$$

::: {#exm-t1-0016}
**La completitud produce la frontera antes de que sepamos identificarla.** El conjunto $S_{\mathbb R}$ es no vacío y está acotado superiormente. Por tanto, el axioma de completitud garantiza que existe un número real

$$
\alpha=\sup S_{\mathbb R}.
$$

En este punto todavía no hemos demostrado que $\alpha^2=2$.
:::

En efecto,

$$
1\in S_{\mathbb R},
$$

así que el conjunto es no vacío. Y $2$ es una cota superior por el mismo argumento usado antes. Por completitud, existe

$$
\alpha=\sup S_{\mathbb R}\in\mathbb R.
$$

Observemos con cuidado lo que hemos ganado y lo que todavía falta.

La completitud nos entrega **un punto frontera real**. No nos dice todavía que ese punto satisfaga

$$
\alpha^2=2.
$$

Demostrar esa igualdad será el trabajo de §2.6. Solo después podremos identificar legítimamente a $\alpha$ con la raíz cuadrada positiva de $2$.

Esta separación es un ejemplo perfecto de la arquitectura

$$
\boxed{
\text{existencia estructural}
\quad\longrightarrow\quad
\text{identificación del objeto}.
}
$$

### El sistema ambiente importa

El conjunto $S_{\mathbb Q}$ puede verse como subconjunto de $\mathbb Q$ o como subconjunto de $\mathbb R$.

Cuando trabajamos **dentro de $\mathbb Q$**, preguntamos si existe una menor cota superior racional. Acabamos de demostrar que no.

Cuando lo consideramos como subconjunto de $\mathbb R$, la completitud de los reales garantiza que posee una menor cota superior real.

Por tanto, expresiones como

$$
\sup A
$$

no deben separarse del sistema ordenado en el que se está buscando esa frontera cuando existe alguna ambigüedad sobre el universo ambiente.

En nuestro desarrollo habitual, una vez fijado $A\subseteq\mathbb R$, la notación $\sup A$ significará siempre supremum en $\mathbb R$.

### Antes de seguir

::: {.callout-tip title="Antes de seguir"}
**1.** ¿Podemos aplicar el axioma de completitud al conjunto $A=(0,\infty)$?

**Respuesta.** No. Aunque $A$ es no vacío, no está acotado superiormente. El axioma exige ambas hipótesis.
:::

::: {.callout-tip title="Antes de seguir"}
**2.** Si la completitud garantiza que $s=\sup A$ existe, ¿garantiza también que $s\in A$?

**Respuesta.** No. Por ejemplo,

$$
\sup(0,1)=1
$$

pero $1\notin(0,1)$.
:::

::: {.callout-tip title="Antes de seguir"}
**3.** ¿Por qué la existencia de muchas cotas superiores racionales para $S_{\mathbb Q}$ no contradice nuestro resultado?

**Respuesta.** Porque el problema no es la falta de cotas superiores. El conjunto tiene, por ejemplo, las cotas racionales $2$, $3$ y muchas otras. Lo que no existe en $\mathbb Q$ es una **menor** cota superior.
:::

::: {.callout-tip title="Antes de seguir"}
**4.** ¿Por qué no podemos escribir todavía $\alpha=\sqrt2$ para $\alpha=\sup S_{\mathbb R}$?

**Respuesta.** Porque la completitud solo ha demostrado que $\alpha$ existe como supremo. Todavía debemos probar que

$$
\alpha^2=2.
$$

Esa identificación será precisamente la aplicación central de §2.6.
:::

### La diferencia decisiva

Podemos resumir el capítulo hasta aquí de la siguiente manera.

Los racionales y los reales comparten la estructura de cuerpo ordenado. En ambos podemos sumar, multiplicar, comparar, utilizar valor absoluto, hablar de distancia, definir cotas y formular qué significaría ser supremo.

La diferencia aparece cuando preguntamos si ciertas fronteras **deben existir**.

En $\mathbb Q$ encontramos el conjunto

$$
S_{\mathbb Q}=\{q\in\mathbb Q:q\ge0,\ q^2<2\},
$$

que es no vacío y acotado superiormente pero no posee supremo racional.

En $\mathbb R$, la completitud afirma que ese tipo de fracaso no puede ocurrir:

$$
\boxed{
A\subseteq\mathbb R,
\quad
A\ne\varnothing,
\quad
A\text{ acotado superiormente}
\quad\Longrightarrow\quad
\sup A\in\mathbb R.
}
$$

Esta es la primera respuesta rigurosa a la pregunta que abrió el capítulo:

$$
\boxed{
\text{lo que añadimos al pasar de un cuerpo ordenado a }\mathbb R
\text{ es una garantía de existencia de fronteras.}
}
$$

En §2.6 haremos trabajar esa garantía. Tomaremos

$$
\alpha=\sup\{x\in\mathbb R:x\ge0,\ x^2<2\}
$$

y demostraremos, sin utilizar continuidad ni límites, que necesariamente

$$
\alpha^2=2.
$$

Solo entonces la raíz que faltaba desde la primera página del capítulo habrá sido construida dentro de nuestro sistema axiomático.
