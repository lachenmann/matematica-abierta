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

El axioma de completitud es una herramienta de **existencia** con hipótesis precisas. Antes de invocarlo conviene auditar tres datos.

**1. Sistema ambiente.** Debemos estar considerando

$$
A\subseteq\mathbb R.
$$

La acotación y el supremo se entienden entonces dentro de $\mathbb R$. Si un conjunto de racionales se considera como subconjunto de $\mathbb R$, la completitud puede producir un supremo real, pero no afirma que ese supremo pertenezca a $\mathbb Q$.

**2. No vacuidad.** Debemos verificar

$$
A\ne\varnothing.
$$

En una demostración suele bastar exhibir un testigo concreto

$$
a_0\in A.
$$

**3. Acotación superior en $\mathbb R$.** Debemos producir al menos un número $M\in\mathbb R$ tal que

$$
\forall a\in A,
\qquad
a\le M.
$$

Solo después de estas comprobaciones el axioma autoriza exactamente la afirmación

$$
\boxed{
\exists s\in\mathbb R
\qquad
s=\sup A.
}
$$

La palabra **exactamente** importa. La existencia procede del axioma de completitud; la unicidad no. La unicidad del supremo ya fue demostrada en §1.3 a partir de su definición y de la antisimetría del orden.

Por tanto, al combinar ambos resultados obtenemos

$$
\boxed{
\begin{array}{c}
A\subseteq\mathbb R,\\
A\ne\varnothing,\\
\exists M\in\mathbb R\;\forall a\in A,\ a\le M
\end{array}
\quad\Longrightarrow\quad
\exists!\,s\in\mathbb R
\text{ tal que }
s=\sup A.
}
$$

El cuantificador $\exists!$ es, pues, una **conclusión combinada**: completitud aporta existencia y el resultado previo de §1.3 aporta unicidad.

Conviene observar también qué **no** forma parte de las hipótesis. No necesitamos que $A$ esté acotado inferiormente. Por ejemplo,

$$
A=(-\infty,0]
$$

es no vacío y está acotado superiormente en $\mathbb R$ por $0$, aunque no está acotado inferiormente. La completitud se aplica igualmente.

Veamos ahora dos fallos de hipótesis.

Para

$$
A=\varnothing,
$$

la condición de no vacuidad falla. El conjunto vacío está acotado superiormente de manera vacua, pero eso no basta para aplicar el axioma.

Para

$$
A=(0,\infty),
$$

la no vacuidad sí se cumple, pero no existe ninguna cota superior real. Por tanto, tampoco podemos invocar completitud.

En ambos casos la conclusión del axioma queda fuera de alcance. Lógicamente,

$$
\boxed{
\text{no poder aplicar un teorema}
\not\Longrightarrow
\text{haber demostrado la negación de su conclusión}.
}
$$

Cualquier afirmación adicional deberá justificarse por otro argumento.

Hay otras tres cosas que el axioma tampoco afirma.

**Primero, no dice que el supremo pertenezca al conjunto.** Para

$$
A=(0,1),
$$

la completitud garantiza la existencia de un supremo real, y ya demostramos que

$$
\sup A=1,
$$

pero

$$
1\notin A.
$$

Por tanto,

$$
\boxed{
\text{completitud garantiza un supremo, no necesariamente un máximo}.
}
$$

**Segundo, el axioma no calcula el supremo.** Puede garantizar que existe un número

$$
s=\sup A
$$

sin proporcionar una fórmula explícita para $s$.

**Tercero, tampoco entrega automáticamente propiedades adicionales del objeto construido.** Si más adelante definimos un conjunto mediante una ecuación o una desigualdad y obtenemos su supremo por completitud, todavía tendremos que demostrar por separado que esa frontera posee la propiedad concreta que buscamos.

::: {.callout-important title="Protocolo de uso de completitud"}
Antes de escribir «por completitud», audite:

1. **ambiente:** ¿el conjunto está siendo considerado dentro de $\mathbb R$?;
2. **testigo:** ¿hemos exhibido al menos un elemento del conjunto?;
3. **cota:** ¿hemos exhibido una cota superior en $\mathbb R$?;
4. **conclusión exacta:** ¿estamos usando el axioma solamente para afirmar existencia?

Si después escribimos «existe un único supremo», la unicidad proviene del resultado ya demostrado en §1.3. Cualquier identificación o propiedad adicional del supremo requiere trabajo posterior.
:::

El axioma está formulado de manera unilateral, para cotas superiores. En el microtramo siguiente veremos que no hace falta postular por separado la existencia de ínfimos: la versión inferior puede deducirse de esta misma propiedad.

### El ínfimo no necesita un segundo axioma

El axioma de completitud fue formulado únicamente para conjuntos no vacíos y acotados **superiormente**. Podríamos postular una segunda propiedad, dual, para conjuntos acotados inferiormente. No hace falta: la existencia de ínfimos puede deducirse del mismo axioma.

::: {#prp-t1-0011}
**Existencia de ínfimos a partir del axioma de completitud.** Todo subconjunto no vacío $A\subseteq\mathbb R$ que esté acotado inferiormente posee un ínfimo en $\mathbb R$.
:::

::: {.callout-note title="Idea de la prueba"}
Reuniremos en un solo conjunto **todas las cotas inferiores de $A$**:

$$
L=\{\ell\in\mathbb R:\ell\le a\text{ para todo }a\in A\}.
$$

La hipótesis de acotación inferior hará que $L$ sea no vacío. La hipótesis $A\ne\varnothing$ nos permitirá escoger un elemento de $A$ que funcione como cota superior de $L$.

Entonces podremos aplicar completitud a $L$. Su supremo resultará ser exactamente la mayor de todas las cotas inferiores de $A$, es decir, $\inf A$.
:::

**Demostración.** Sea $A\subseteq\mathbb R$ no vacío y acotado inferiormente. Definamos

$$
L=\{\ell\in\mathbb R:\forall a\in A,\ \ell\le a\}.
$$

Por definición, $L$ es el conjunto de todas las cotas inferiores de $A$.

**1. $L$ es no vacío.** Como $A$ está acotado inferiormente, existe algún $\ell_0\in\mathbb R$ tal que

$$
\forall a\in A,
\qquad
\ell_0\le a.
$$

Por la definición de $L$,

$$
\ell_0\in L.
$$

Por tanto,

$$
L\ne\varnothing.
$$

**2. $L$ está acotado superiormente.** Como $A\ne\varnothing$, podemos escoger

$$
a_0\in A.
$$

Sea $\ell\in L$ arbitrario. Puesto que $\ell$ es una cota inferior de $A$, debe cumplirse en particular

$$
\ell\le a_0.
$$

Así,

$$
\forall\ell\in L,
\qquad
\ell\le a_0.
$$

Por tanto, $a_0$ es una cota superior de $L$.

Ya hemos verificado exactamente las dos hipótesis que necesita completitud:

$$
L\ne\varnothing
\qquad\text{y}\qquad
L\text{ está acotado superiormente}.
$$

Existe entonces un número real

$$
s=\sup L.
$$

Debemos demostrar que este mismo número es el ínfimo de $A$. Para ello verificaremos las dos cláusulas de la definición.

**3. $s$ es una cota inferior de $A$.** Sea $a\in A$ arbitrario. Para todo $\ell\in L$ tenemos

$$
\ell\le a,
$$

porque cada elemento de $L$ es una cota inferior de $A$. Esto significa que $a$ es una cota superior de $L$.

Como

$$
s=\sup L
$$

es la **menor** cota superior de $L$,

$$
s\le a.
$$

El elemento $a\in A$ era arbitrario. Por tanto,

$$
\forall a\in A,
\qquad
s\le a,
$$

y así $s$ es una cota inferior de $A$. Equivalentemente,

$$
s\in L.
$$

**4. Ninguna cota inferior de $A$ es mayor que $s$.** Sea $\ell$ una cota inferior cualquiera de $A$. Entonces, por definición,

$$
\ell\in L.
$$

Pero $s=\sup L$ es, en particular, una cota superior de $L$. Por tanto,

$$
\ell\le s.
$$

Hemos demostrado simultáneamente que

$$
s\le a
\qquad
\text{para todo }a\in A,
$$

y que

$$
\ell\le s
\qquad
\text{para toda cota inferior }\ell\text{ de }A.
$$

Estas son exactamente las dos cláusulas que caracterizan al ínfimo. En consecuencia,

$$
\boxed{s=\inf A.}
$$

$\blacksquare$

La demostración proporciona además una identidad conceptual útil. Si

$$
L=\{\ell\in\mathbb R:\ell\text{ es cota inferior de }A\},
$$

entonces

$$
\boxed{
\inf A=\sup L.
}
$$

Más aún, como acabamos de demostrar que $s=\sup L$ pertenece al propio $L$,

$$
\boxed{
\inf A=\sup L=\max L.
}
$$

Es decir: el ínfimo de $A$ es literalmente **la mayor de todas sus cotas inferiores**.

::: {.callout-note title="Dónde se usó cada hipótesis"}
Las dos hipótesis sobre $A$ desempeñan funciones distintas:

- $A$ **acotado inferiormente** $\Longrightarrow L\ne\varnothing$;
- $A\ne\varnothing$ $\Longrightarrow$ podemos escoger $a_0\in A$, que sirve como cota superior de $L$.

Solo después de esas dos verificaciones entra la completitud, una única vez:

$$
L\ne\varnothing
\quad+\quad
L\text{ acotado superiormente}
\quad\Longrightarrow\quad
\sup L\text{ existe}.
$$

El resto de la prueba utiliza únicamente las definiciones de cota, supremo e ínfimo y las propiedades del orden.
:::

Por tanto, no necesitamos añadir una segunda «propiedad de completitud para ínfimos». La versión inferior ya está contenida en la propiedad del supremo.

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
