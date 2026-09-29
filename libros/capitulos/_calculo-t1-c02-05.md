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

La importancia del axioma de completitud sería difícil de apreciar si la misma propiedad fuese válida también en $\mathbb Q$. Veamos que no lo es.

Consideremos nuevamente

$$
S_{\mathbb Q}
=
\{q\in\mathbb Q:q\ge0,\ q^2<2\}.
$$

Antes de preguntar por su supremo debemos auditar las dos hipótesis de existencia.

**1. $S_{\mathbb Q}$ es no vacío.** El número $1$ es racional y satisface

$$
1\ge0
\qquad\text{y}\qquad
1^2=1<2.
$$

Por tanto,

$$
1\in S_{\mathbb Q},
$$

y así

$$
S_{\mathbb Q}\ne\varnothing.
$$

**2. $S_{\mathbb Q}$ está acotado superiormente en $\mathbb Q$.** Mostremos que $2$ es una cota superior racional. Sea

$$
q\in S_{\mathbb Q}.
$$

Entonces

$$
q\ge0
\qquad\text{y}\qquad
q^2<2.
$$

Si ocurriera $q\ge2$, tendríamos

$$
0\le2\le q,
$$

y la monotonía del cuadrado en los no negativos, @prp-t1-0007, daría

$$
4=2^2\le q^2.
$$

Esto contradice $q^2<2$. Por tanto,

$$
q<2,
$$

y en particular

$$
q\le2.
$$

Como $q\in S_{\mathbb Q}$ fue arbitrario,

$$
\forall q\in S_{\mathbb Q},
\qquad
q\le2.
$$

Así, $2\in\mathbb Q$ es una cota superior de $S_{\mathbb Q}$ dentro del sistema racional.

Hemos verificado, pues,

$$
\boxed{
S_{\mathbb Q}\ne\varnothing
\qquad\text{y}\qquad
S_{\mathbb Q}\text{ está acotado superiormente en }\mathbb Q.
}
$$

Si $\mathbb Q$ satisficiera la propiedad del supremo que hemos adoptado para $\mathbb R$, estas dos condiciones obligarían a que existiera una menor cota superior **racional**.

Conviene fijar la notación. Escribiremos

$$
s=\sup_{\mathbb Q}S_{\mathbb Q}
$$

para decir que $s\in\mathbb Q$ satisface simultáneamente

$$
\forall q\in S_{\mathbb Q},
\qquad
q\le s,
$$

y

$$
\forall u\in\mathbb Q,
\qquad
\left[
\bigl(\forall q\in S_{\mathbb Q},\ q\le u\bigr)
\Longrightarrow
s\le u
\right].
$$

Es decir, $s$ tendría que ser una cota superior racional y, además, la menor entre **todas las cotas superiores racionales**.

La siguiente proposición demuestra que tal $s$ no existe.

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
Supongamos que existiera

$$
s=\sup_{\mathbb Q}S_{\mathbb Q}.
$$

Como $1\in S_{\mathbb Q}$ y $s$ sería una cota superior, tendríamos $s\ge1$. En particular, podremos aplicar a $s$ la transformación racional estudiada en §1.4.

La tricotomía deja exactamente tres posibilidades:

$$
s^2<2,
\qquad
s^2=2,
\qquad
s^2>2.
$$

Cada caso ataca una parte distinta de la definición de supremo.

- Si $s^2<2$, la transformación producirá un elemento de $S_{\mathbb Q}$ estrictamente mayor que $s$. Así, $s$ dejará de ser siquiera una **cota superior**.
- Si $s^2>2$, producirá una **cota superior racional** estrictamente menor que $s$. Así, $s$ dejará de ser la **menor** cota superior.
- Si $s^2=2$, contradiremos el resultado de §1.4: ningún racional tiene cuadrado $2$.

Los tres casos serán imposibles.
:::

**Demostración.** Supongamos, para obtener una contradicción, que existe un racional

$$
s=\sup_{\mathbb Q}S_{\mathbb Q}.
$$

Por la definición fijada arriba, $s$ es en particular una cota superior racional de $S_{\mathbb Q}$:

$$
\forall q\in S_{\mathbb Q},
\qquad
q\le s.
$$

Como

$$
1\in S_{\mathbb Q},
$$

obtenemos

$$
1\le s.
$$

En particular,

$$
s>0
\qquad\text{y}\qquad
s+2>0,
$$

de modo que

$$
s+2\ne0.
$$

Aplicaremos al candidato $s$ la misma transformación estudiada en §1.4:

$$
T(s)
=
s-\frac{s^2-2}{s+2}
=
\frac{2(s+1)}{s+2}.
$$

Como $s\in\mathbb Q$, también

$$
s+1\in\mathbb Q,
\qquad
s+2\in\mathbb Q.
$$

Además, $s+2\ne0$. Puesto que $\mathbb Q$ es un cuerpo, concluimos

$$
\boxed{T(s)\in\mathbb Q}.
$$

Por otra parte,

$$
s+1>0,
\qquad
s+2>0,
\qquad
2>0,
$$

así que

$$
\boxed{T(s)>0}.
$$

Ya demostramos en §1.4 las dos identidades decisivas:

$$
\boxed{
T(s)-s
=
\frac{2-s^2}{s+2}
}
$$

y

$$
\boxed{
T(s)^2-2
=
\frac{2(s^2-2)}{(s+2)^2}.
}
$$

La primera controla la **dirección** del desplazamiento; la segunda controla el **lado** respecto de $2$.

Consideremos los tres casos que proporciona la tricotomía para $s^2$ y $2$.

**Caso 1: $s^2<2$.** Entonces

$$
2-s^2>0.
$$

Como

$$
s+2>0,
$$

la primera identidad da

$$
T(s)-s>0.
$$

Por definición del orden,

$$
\boxed{T(s)>s}.
$$

Ahora debemos comprobar que este nuevo racional sigue perteneciendo al conjunto. De

$$
s^2<2
$$

obtenemos

$$
s^2-2<0.
$$

Además,

$$
\frac{2}{(s+2)^2}>0,
$$

pues $2>0$ y $(s+2)^2>0$. Multiplicar $s^2-2$ por este factor positivo conserva su signo. Por la segunda identidad,

$$
T(s)^2-2<0,
$$

y por tanto

$$
\boxed{T(s)^2<2}.
$$

Reunamos las condiciones de pertenencia:

$$
T(s)\in\mathbb Q,
\qquad
T(s)>0,
\qquad
T(s)^2<2.
$$

Luego

$$
\boxed{T(s)\in S_{\mathbb Q}}.
$$

Pero $s$ es una cota superior de $S_{\mathbb Q}$. Por consiguiente, todo elemento del conjunto debe satisfacer

$$
q\le s.
$$

Particularizando en el elemento $q=T(s)\in S_{\mathbb Q}$,

$$
T(s)\le s.
$$

Esto contradice

$$
T(s)>s.
$$

Por tanto,

$$
\boxed{s^2<2\text{ es imposible}.}
$$

**Caso 2: $s^2>2$.** Entonces

$$
2-s^2<0.
$$

Como ya sabemos que

$$
s+2>0,
$$

la identidad

$$
T(s)-s
=
\frac{2-s^2}{s+2}
$$

da

$$
T(s)-s<0.
$$

Por definición del orden,

$$
\boxed{T(s)<s}.
$$

La segunda identidad controla ahora el lado de la frontera. De

$$
s^2>2
$$

se sigue

$$
s^2-2>0.
$$

Además,

$$
\frac{2}{(s+2)^2}>0.
$$

Por tanto,

$$
T(s)^2-2
=
\frac{2(s^2-2)}{(s+2)^2}
>0,
$$

y así

$$
\boxed{T(s)^2>2}.
$$

Hasta aquí solo sabemos que $T(s)$ es un racional positivo situado por encima del nivel $2$ y que además

$$
T(s)<s.
$$

Para contradecir la **minimalidad** de $s$ todavía debemos demostrar que $T(s)$ es una cota superior de $S_{\mathbb Q}$.

Sea, pues,

$$
q\in S_{\mathbb Q}
$$

arbitrario. Entonces

$$
q\ge0
\qquad\text{y}\qquad
q^2<2.
$$

Supongamos, para obtener una contradicción, que

$$
q\ge T(s).
$$

Ya demostramos antes de separar los casos que

$$
T(s)>0.
$$

Por tanto,

$$
0<T(s)\le q.
$$

La monotonía del cuadrado en los no negativos, @prp-t1-0007, implica

$$
T(s)^2\le q^2.
$$

Pero acabamos de demostrar

$$
T(s)^2>2,
$$

mientras que la pertenencia $q\in S_{\mathbb Q}$ exige

$$
q^2<2.
$$

Obtendríamos entonces

$$
2<T(s)^2\le q^2<2,
$$

una contradicción.

Así, la suposición $q\ge T(s)$ es imposible y necesariamente

$$
q<T(s).
$$

Como $q\in S_{\mathbb Q}$ era arbitrario,

$$
\boxed{
\forall q\in S_{\mathbb Q},
\qquad
q<T(s).
}
$$

En particular,

$$
\forall q\in S_{\mathbb Q},
\qquad
q\le T(s).
$$

Por tanto, $T(s)$ es una cota superior de $S_{\mathbb Q}$. Y, como ya establecimos que

$$
T(s)\in\mathbb Q,
$$

se trata de una **cota superior racional**.

Ahora entra la segunda cláusula de

$$
s=\sup_{\mathbb Q}S_{\mathbb Q}.
$$

Como $T(s)\in\mathbb Q$ es una cota superior racional, la minimalidad de $s$ obliga a que

$$
s\le T(s).
$$

Pero antes habíamos obtenido

$$
T(s)<s.
$$

Las dos desigualdades son incompatibles. Por tanto,

$$
\boxed{s^2>2\text{ es imposible}.}
$$

**Caso 3: $s^2=2$.** Recordemos que, desde el comienzo de la contradicción, hemos supuesto

$$
s\in\mathbb Q.
$$

Pero en §1.4 demostramos

$$
\forall q\in\mathbb Q,
\qquad
q^2\ne2.
$$

Particularizando esa afirmación en el racional $s$, obtenemos

$$
s^2\ne2.
$$

Esto contradice directamente la hipótesis del caso. Por tanto,

$$
\boxed{s^2=2\text{ es imposible}.}
$$

La tricotomía aplicada a $s^2$ y $2$ afirma que ocurre exactamente una de las tres posibilidades

$$
s^2<2,
\qquad
s^2=2,
\qquad
s^2>2.
$$

Hemos demostrado que las tres son imposibles bajo la suposición

$$
s=\sup_{\mathbb Q}S_{\mathbb Q}.
$$

Por tanto, esa suposición inicial debe ser falsa:

$$
\boxed{
\neg\exists s\in\mathbb Q
\text{ tal que }
s=\sup_{\mathbb Q}S_{\mathbb Q}.
}
$$

Equivalentemente,

$$
\boxed{
S_{\mathbb Q}
\text{ no posee supremo en }\mathbb Q.
}
$$

Junto con la no vacuidad y la acotación superior ya demostradas, concluimos que $\mathbb Q$ falla la propiedad del supremo.

$\blacksquare$

### Qué hizo realmente la transformación de Rudin

En §1.4 introdujimos

$$
T(p)=p-\frac{p^2-2}{p+2}
$$

para demostrar que no existe un último racional positivo con cuadrado menor que $2$ ni un primero con cuadrado mayor que $2$.

En la prueba que acabamos de cerrar, las mismas identidades desempeñan una función lógica más precisa. La transformación no intenta **encontrar** un supremo racional. Hace exactamente lo contrario: permite **refutar cualquier candidato racional** según el lado del nivel $2$ en que se encuentre.

Supongamos que $s\in\mathbb Q$ pretende satisfacer las dos cláusulas de

$$
s=\sup_{\mathbb Q}S_{\mathbb Q}.
$$

Hay tres posibilidades.

**1. Si $s^2<2$, falla la condición de cota superior.** La transformación produce

$$
T(s)\in S_{\mathbb Q}
\qquad\text{y}\qquad
T(s)>s.
$$

Así existe un elemento permitido situado por encima de $s$. En símbolos,

$$
\boxed{
s^2<2
\quad\Longrightarrow\quad
\exists q\in S_{\mathbb Q}\text{ tal que }q>s.
}
$$

Por tanto, $s$ no puede dominar a todos los elementos de $S_{\mathbb Q}$.

**2. Si $s^2>2$, falla la minimalidad.** En este caso la transformación produce un racional $T(s)$ tal que

$$
T(s)<s
$$

y, además,

$$
\forall q\in S_{\mathbb Q},
\qquad
q\le T(s).
$$

Es decir, $T(s)$ es una cota superior racional estrictamente menor que $s$. Por tanto,

$$
\boxed{
s^2>2
\quad\Longrightarrow\quad
\exists u\in\mathbb Q
\text{ cota superior de }S_{\mathbb Q}
\text{ con }u<s.
}
$$

Así, aun cuando $s$ fuese una cota superior, no podría ser la menor.

**3. Si $s^2=2$, falla la racionalidad del candidato.** Este caso no lo descarta la transformación, sino @prp-t1-0006:

$$
\boxed{
\forall q\in\mathbb Q,
\qquad
q^2\ne2.
}
$$

Por eso los tres casos atacan exactamente las tres posibilidades abiertas por la tricotomía, pero no todos con la misma herramienta: $T$ elimina las dos desigualdades estrictas y la inexistencia racional de una raíz elimina la igualdad.

Podemos condensar la arquitectura así:

$$
\boxed{
\begin{array}{ccl}
s^2<2
&\Longrightarrow&
\text{$s$ no es cota superior},\\[4pt]
s^2>2
&\Longrightarrow&
\text{$s$ no es la menor cota superior},\\[4pt]
s^2=2
&\Longrightarrow&
\text{contradicción con }s\in\mathbb Q.
\end{array}
}
$$

En consecuencia, **todo candidato racional falla** antes de poder satisfacer simultáneamente las dos cláusulas de supremo.

Esta es la función estructural de la transformación de Rudin: no aproxima por sí sola un objeto cuya existencia ya conozcamos, ni produce una frontera racional. Es un **mecanismo de exclusión** que muestra cómo fracasa cada candidato posible dentro de $\mathbb Q$.

El resultado tiene además una consecuencia lógica que habíamos dejado pendiente. Ya sabemos que

$$
\mathbb Q
$$

es un cuerpo ordenado, pero acabamos de exhibir en él un conjunto no vacío y acotado superiormente que no posee supremo racional. Por tanto,

$$
\boxed{
\text{cuerpo}
+
\text{orden}
\not\Longrightarrow
\text{completitud}.
}
$$

Así, la completitud contiene información estructural genuinamente adicional. El «hueco» no consiste simplemente en que «faltan irracionales», sino en que $\mathbb Q$ no garantiza la existencia interna de ciertas fronteras que su propio orden permite describir.

### El mismo problema dentro de $\mathbb R$

Cambiemos ahora el sistema ambiente. Consideremos

$$
S_{\mathbb R}
=
\{x\in\mathbb R:x\ge0,\ x^2<2\}.
$$

La desigualdad que define el conjunto es la misma que antes, pero ahora los candidatos y las cotas pertenecen a $\mathbb R$. Por eso podemos intentar aplicar el axioma de completitud.

Antes debemos verificar sus dos hipótesis.

**1. $S_{\mathbb R}$ es no vacío.** El número $1$ es real y satisface

$$
1\ge0
\qquad\text{y}\qquad
1^2=1<2.
$$

Por tanto,

$$
\boxed{1\in S_{\mathbb R}},
$$

y así

$$
S_{\mathbb R}\ne\varnothing.
$$

**2. $S_{\mathbb R}$ está acotado superiormente.** Mostremos que $2$ es una cota superior. Sea

$$
x\in S_{\mathbb R}.
$$

Entonces

$$
x\ge0
\qquad\text{y}\qquad
x^2<2.
$$

Si ocurriera $x\ge2$, tendríamos

$$
0\le2\le x.
$$

La monotonía del cuadrado en los no negativos, @prp-t1-0007, daría

$$
4=2^2\le x^2,
$$

en contradicción con $x^2<2$. Por tanto,

$$
x<2,
$$

y en particular

$$
x\le2.
$$

Como $x\in S_{\mathbb R}$ fue arbitrario,

$$
\boxed{
\forall x\in S_{\mathbb R},
\qquad
x\le2.
}
$$

Así, $2$ es una cota superior real de $S_{\mathbb R}$.

Hemos verificado exactamente las hipótesis del axioma:

$$
S_{\mathbb R}\ne\varnothing
\qquad\text{y}\qquad
S_{\mathbb R}\text{ está acotado superiormente en }\mathbb R.
$$

Por completitud existe un número real

$$
\boxed{
\alpha=\sup S_{\mathbb R}.
}
$$

::: {#exm-t1-0016}
**La completitud produce la frontera antes de que sepamos identificarla.** La afirmación

$$
\alpha=\sup S_{\mathbb R}
$$

significa que $\alpha\in\mathbb R$ satisface simultáneamente

$$
\forall x\in S_{\mathbb R},
\qquad
x\le\alpha,
$$

y

$$
\forall u\in\mathbb R,
\qquad
\left[
\bigl(\forall x\in S_{\mathbb R},\ x\le u\bigr)
\Longrightarrow
\alpha\le u
\right].
$$

La completitud garantiza la **existencia** de ese número. La unicidad procede de la unicidad general del supremo demostrada en §1.3.
:::

Podemos extraer inmediatamente dos cotas para $\alpha$.

Como

$$
1\in S_{\mathbb R}
$$

y $\alpha$ es una cota superior,

$$
1\le\alpha.
$$

Por otra parte, $2$ es una cota superior de $S_{\mathbb R}$ y $\alpha$ es la menor de todas ellas. Por tanto,

$$
\alpha\le2.
$$

Así,

$$
\boxed{
1\le\alpha\le2.
}
$$

En este punto sabemos rigurosamente que existe una frontera real y sabemos dónde está localizada. Pero completitud no nos ha entregado todavía la propiedad que motivó toda la construcción.

No hemos demostrado aún

$$
\alpha^2=2.
$$

Tampoco tenemos derecho todavía a escribir

$$
\alpha=\sqrt2,
$$

porque la notación $\sqrt2$ como nombre de una raíz real positiva solo quedará legitimada después de probar esa existencia e identificación.

El trabajo se divide, por tanto, en dos etapas distintas:

$$
\boxed{
\begin{array}{c}
\text{completitud}\\
\downarrow\\
\text{existe }\alpha=\sup S_{\mathbb R}\\
\downarrow\\
\text{demostrar que }\alpha^2=2.
\end{array}
}
$$

La primera etapa acaba de cerrarse. La segunda será el objetivo de §1.6, y requerirá un argumento adicional de álgebra y orden: la completitud fabrica el candidato, pero no lo identifica automáticamente.

### El sistema ambiente importa

La notación de supremo depende no solo del conjunto cuyos elementos estudiamos, sino también del **sistema ordenado en el que permitimos buscar las cotas**.

Conviene separar dos operaciones distintas.

**1. Mantener fijo el conjunto y cambiar el sistema ambiente.** Consideremos exactamente el mismo conjunto

$$
S_{\mathbb Q}
=
\{q\in\mathbb Q:q\ge0,\ q^2<2\}.
$$

Podemos estudiar sus cotas superiores dentro de $\mathbb Q$ o dentro de $\mathbb R$.

Las cotas superiores racionales forman el conjunto

$$
U_{\mathbb Q}
=
\left\{
u\in\mathbb Q:
\forall q\in S_{\mathbb Q},\ q\le u
\right\},
$$

mientras que las cotas superiores reales forman

$$
U_{\mathbb R}
=
\left\{
u\in\mathbb R:
\forall q\in S_{\mathbb Q},\ q\le u
\right\}.
$$

Como $\mathbb Q\subseteq\mathbb R$,

$$
\boxed{
U_{\mathbb Q}=U_{\mathbb R}\cap\mathbb Q.
}
$$

En §1.5 demostramos que $U_{\mathbb Q}$ no posee elemento mínimo. Esta es exactamente la afirmación

$$
\boxed{
S_{\mathbb Q}
\text{ no tiene supremo dentro de }\mathbb Q.
}
$$

Pero el mismo conjunto $S_{\mathbb Q}$, considerado ahora como subconjunto de $\mathbb R$, sigue siendo no vacío y está acotado superiormente por $2$. Por completitud existe entonces

$$
\boxed{
\beta=\sup_{\mathbb R}S_{\mathbb Q}.
}
$$

Aquí $\beta$ es el mínimo de $U_{\mathbb R}$.

Podemos deducir inmediatamente algo más:

$$
\boxed{\beta\notin\mathbb Q.}
$$

En efecto, supongamos que $\beta\in\mathbb Q$. Como $\beta$ es una cota superior real de $S_{\mathbb Q}$, sería entonces también una cota superior racional:

$$
\beta\in U_{\mathbb Q}.
$$

Además, si $u\in U_{\mathbb Q}$, entonces $u\in U_{\mathbb R}$. Como $\beta$ es el mínimo de $U_{\mathbb R}$,

$$
\beta\le u.
$$

Por tanto, $\beta$ sería el mínimo de $U_{\mathbb Q}$, es decir,

$$
\beta=\sup_{\mathbb Q}S_{\mathbb Q},
$$

en contradicción con @prp-t1-0012.

Así, el cambio de sistema ambiente puede convertir

$$
\boxed{
\text{«no existe supremo en }\mathbb Q\text{»}
}
$$

en

$$
\boxed{
\text{«existe un supremo en }\mathbb R\text{, y no es racional».}
}
$$

**2. Cambiar además el conjunto.** En el microtramo anterior introdujimos

$$
S_{\mathbb R}
=
\{x\in\mathbb R:x\ge0,\ x^2<2\}.
$$

Esto ya no consiste únicamente en buscar las cotas de $S_{\mathbb Q}$ en un sistema mayor. También hemos ampliado el universo permitido para los **elementos del propio conjunto**.

La relación exacta entre ambos conjuntos es

$$
\boxed{
S_{\mathbb Q}=S_{\mathbb R}\cap\mathbb Q.
}
$$

Por tanto, debemos distinguir cuidadosamente

$$
\sup_{\mathbb R}S_{\mathbb Q}
$$

de

$$
\sup_{\mathbb R}S_{\mathbb R}.
$$

Sabemos que ambos existen por completitud, pero en este punto del desarrollo **no hemos demostrado que sean iguales**. Tampoco necesitamos esa igualdad para lo que sigue.

Lo importante es comprender qué está variando en cada pregunta:

$$
\boxed{
\begin{array}{c}
\text{conjunto fijo }S_{\mathbb Q}
+\text{ ambiente }\mathbb Q
\longrightarrow
\text{no hay supremo racional},
\\[5pt]
\text{conjunto fijo }S_{\mathbb Q}
+\text{ ambiente }\mathbb R
\longrightarrow
\text{existe }\sup_{\mathbb R}S_{\mathbb Q},
\\[5pt]
\text{conjunto }S_{\mathbb R}
+\text{ ambiente }\mathbb R
\longrightarrow
\text{existe }\alpha=\sup_{\mathbb R}S_{\mathbb R}.
\end{array}
}
$$

Esta distinción evita una ambigüedad frecuente: un supremo no es una propiedad aislada de una colección de símbolos; depende del **orden ambiente en el que se permiten las cotas**.

En nuestro desarrollo habitual, cuando $A\subseteq\mathbb R$ esté fijado y no exista ambigüedad, escribiremos simplemente

$$
\sup A
$$

para significar el supremo en $\mathbb R$. Cuando el sistema ambiente sea relevante —como en el contraste con $\mathbb Q$— utilizaremos explícitamente

$$
\sup_{\mathbb Q}A
\qquad\text{o}\qquad
\sup_{\mathbb R}A.
$$

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
