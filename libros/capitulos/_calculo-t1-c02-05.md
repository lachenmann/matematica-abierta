## Completitud: la propiedad que falta en $\mathbb Q$ {#sec-t1-c02-05}

### Una definición no garantiza una existencia

En §1.3 fijamos qué significa afirmar que un número $s$ es el supremo de un conjunto $A$. Para un candidato dado $s\in\mathbb R$, esa afirmación reúne dos propiedades:

$$
\boxed{
\begin{aligned}
&\forall a\in A,\qquad a\le s,\\[3pt]
&\forall u\in\mathbb R,\qquad
\left[
\bigl(\forall a\in A,\ a\le u\bigr)
\Longrightarrow
s\le u
\right].
\end{aligned}
}
$$

La primera cláusula dice que $s$ es una cota superior; la segunda, que ninguna otra cota superior queda por debajo de $s$.

Para distinguir con claridad **caracterización** y **existencia**, llamemos provisionalmente $P_A(s)$ a la conjunción de esas dos condiciones. Entonces escribir

$$
s=\sup A
$$

significa precisamente que

$$
P_A(s)
$$

es verdadera.

En §1.3 demostramos además que, si dos números satisfacen esa propiedad, necesariamente coinciden:

$$
P_A(s)\ \text{y}\ P_A(t)
\Longrightarrow
s=t.
$$

Es decir, la definición y la unicidad nos permiten afirmar que puede haber **a lo sumo un** supremo.

Pero ninguna de esas afirmaciones produce por sí sola un número $s$ que satisfaga $P_A(s)$. La proposición

$$
\boxed{
\exists s\in\mathbb R
\qquad
P_A(s)
}
$$

es una afirmación adicional de existencia.

Esta diferencia es exactamente la misma que ya encontramos con la ecuación

$$
x^2=2.
$$

La ecuación especifica qué propiedad tendría una solución; no demuestra que exista una. Del mismo modo, la definición de supremo especifica qué debe cumplir una menor cota superior; no garantiza que todo conjunto posea una.

En §1.3 ya identificamos las hipótesis naturales bajo las cuales queremos plantear el problema:

$$
A\ne\varnothing
$$

y

$$
A\text{ está acotado superiormente}.
$$

La pregunta que queda abierta es, por tanto,

$$
\boxed{
A\ne\varnothing
\quad\text{y}\quad
A\text{ acotado superiormente}
\quad\stackrel{?}{\Longrightarrow}\quad
\exists s\in\mathbb R\;P_A(s).
}
$$

Nada de los axiomas de cuerpo y orden demostrados hasta ahora autoriza esa implicación. La sección anterior mostró precisamente por qué debemos esperar una propiedad adicional: dentro de $\mathbb Q$ puede aparecer una región acotada cuya frontera no está disponible como menor cota superior racional.

El paso siguiente consistirá en incorporar, para $\mathbb R$, la afirmación de existencia que falta.

### El axioma de completitud {#sec-t1-c02-completeness-axiom}

La pregunta abierta al final del microtramo anterior era:

$$
A\ne\varnothing,
\qquad
A\text{ acotado superiormente}
\quad\stackrel{?}{\Longrightarrow}\quad
\exists s\in\mathbb R\;P_A(s).
$$

La propiedad adicional que adoptaremos para $\mathbb R$ responde afirmativamente a esa pregunta.

::: {.callout-important title="Axioma de completitud"}
Todo subconjunto no vacío $A\subseteq\mathbb R$ que esté acotado superiormente posee un supremo en $\mathbb R$.

En símbolos,

$$
\boxed{
A\ne\varnothing
\quad\text{y}\quad
\exists M\in\mathbb R\;
\forall a\in A,\ a\le M
\quad\Longrightarrow\quad
\exists s\in\mathbb R\;P_A(s).
}
$$

Equivalentemente, existe $s\in\mathbb R$ tal que

$$
s=\sup A.
$$
:::

La fuerza nueva del axioma está en el cuantificador

$$
\boxed{\exists s\in\mathbb R.}
$$

La definición de supremo ya nos decía qué debía satisfacer un candidato; la completitud afirma que, bajo las hipótesis

$$
A\ne\varnothing
$$

y

$$
A\text{ acotado superiormente},
$$

ese candidato **existe dentro de $\mathbb R$**.

Además, en §1.3 ya demostramos que el supremo, si existe, es único. Por tanto, combinando aquella unicidad con el axioma de completitud obtenemos inmediatamente

$$
\boxed{
A\ne\varnothing,
\quad
A\subseteq\mathbb R,
\quad
A\text{ acotado superiormente}
\quad\Longrightarrow\quad
\exists!\,s\in\mathbb R
\text{ tal que }
s=\sup A.
}
$$

Así, la completitud no redefine la noción de supremo. Añade exactamente la garantía de existencia que faltaba:

$$
\boxed{
\text{definición}
+
\text{unicidad}
+
\text{completitud}
\quad\Longrightarrow\quad
\text{existencia y unicidad del supremo}.
}
$$

### ¿Por qué lo llamamos axioma?

La palabra **axioma** describe el papel que una afirmación desempeña dentro de un desarrollo determinado. No significa que la afirmación carezca de justificación en cualquier contexto ni que deba adoptarse siempre como punto de partida.

En este libro hemos elegido una vía axiomática. No construiremos $\mathbb R$ a partir de objetos más elementales; asumiremos que los números reales forman un cuerpo ordenado y añadiremos como propiedad fundamental la completitud recién enunciada.

Así, dentro de nuestra cadena lógica,

$$
\boxed{
\text{cuerpo}
+
\text{orden}
+
\text{completitud}
}
$$

son datos estructurales de partida para $\mathbb R$, y las consecuencias posteriores deberán deducirse de ellos.

Hay otra vía posible. Si se construye $\mathbb R$ —por ejemplo, mediante cortes de Dedekind o mediante una construcción apropiada a partir de sucesiones racionales—, entonces las propiedades de cuerpo, orden y completitud deben demostrarse para el objeto construido. En ese contexto, la propiedad del supremo aparece como **teorema de la construcción**, no como axioma inicial.

Por tanto, la diferencia no está en el contenido matemático de la propiedad, sino en su **posición dentro de la cadena de dependencias**:

$$
\boxed{
\begin{array}{c}
\text{presentación axiomática:}
\quad
\text{completitud}\longrightarrow\text{consecuencias},\\[5pt]
\text{presentación constructiva:}
\quad
\text{construcción de }\mathbb R
\longrightarrow
\text{demostración de completitud}.
\end{array}
}
$$

En nuestra presentación utilizaremos la primera ruta.

Conviene añadir una precisión lógica. En este punto acabamos de **adoptar** la completitud como hipótesis adicional; todavía no hemos demostrado formalmente dentro del capítulo que no pueda deducirse de los axiomas de cuerpo y orden.

Esa separación quedará certificada más adelante en esta misma sección. Demostraremos que $\mathbb Q$ es un cuerpo ordenado pero contiene un conjunto no vacío y acotado superiormente que no posee supremo racional. Entonces tendremos un ejemplo de estructura que satisface cuerpo y orden pero falla la propiedad del supremo. Por ello, la completitud contiene información que cuerpo y orden, por sí solos, no fuerzan.

::: {.callout-note title="Terminología"}
En este capítulo, **completitud** significará específicamente la **propiedad del supremo** que acabamos de adoptar.

Más adelante aparecerán otras nociones de completitud, por ejemplo formuladas mediante sucesiones de Cauchy. No las utilizaremos aquí para justificar este axioma: la teoría rigurosa de sucesiones todavía no ha sido desarrollada y las relaciones entre esas formulaciones deberán demostrarse en el lugar correspondiente.
:::

El objetivo de esta presentación no es, por tanto, construir los reales, sino fijar con precisión qué estructura de $\mathbb R$ utilizaremos para desarrollar el cálculo y qué resultados dependen de cada parte de esa estructura.

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
**1.** Sea $A\subseteq\mathbb R$ no vacío y acotado superiormente, y sea $c\in\mathbb R$. Define

$$
A+c=\{a+c:a\in A\}.
$$

¿Por qué el axioma de completitud puede aplicarse a $A+c$?

**Respuesta.** Si $M$ es una cota superior de $A$, entonces $M+c$ es una cota superior de $A+c$. Además, si $a_0\in A$, entonces $a_0+c\in A+c$. Por tanto, $A+c$ es no vacío y está acotado superiormente.
:::

::: {.callout-tip title="Antes de seguir"}
**2.** Sea $A\ne\varnothing$ y acotado inferiormente. Explica cómo la completitud aplicada a

$$
-A=\{-a:a\in A\}
$$

produce un candidato para $\inf A$.

**Respuesta.** Si $m$ es cota inferior de $A$, entonces $-m$ es cota superior de $-A$; así, $-A$ es no vacío y acotado superiormente. La completitud produce $s=\sup(-A)$, y el número $-s$ es el candidato natural a $\inf A$.
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
