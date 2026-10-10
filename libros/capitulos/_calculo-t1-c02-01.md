## El hueco de los racionales {#sec-t1-c02-01}

### Una ecuación demasiado sencilla para causar problemas

Busquemos primero soluciones racionales de

$$
x^2=2.
$$

Antes de decidir si tal racional existe, podemos localizar dónde tendría que estar una eventual solución positiva.

Como

$$
1^2<2<2^2,
$$

si $x\ge0$ y $x^2=2$, no puede ocurrir $x\le1$: por la monotonía del cuadrado en los no negativos, demostrada en @prp-t1-0007, tendríamos $x^2\le1$. Tampoco puede ocurrir $x\ge2$, pues entonces $x^2\ge4$. Por tanto,

$$
1<x<2.
$$

Podemos estrechar la localización con racionales intermedios:

$$
\left(\frac43\right)^2=\frac{16}{9}<2,
\qquad
\left(\frac32\right)^2=\frac94>2.
$$

El mismo argumento de monotonía muestra que una solución positiva debería satisfacer

$$
\frac43<x<\frac32.
$$

Podríamos continuar insertando puntos medios racionales. En cada etapa ocurre una de tres cosas: el punto medio tiene cuadrado menor que $2$, mayor que $2$ o exactamente igual a $2$. En los dos primeros casos conservamos la mitad que todavía encierra una eventual solución; en el tercero habríamos encontrado una solución racional exacta.

Este procedimiento puede producir intervalos racionales cada vez más estrechos, pero por sí solo no responde la pregunta decisiva: **¿algún racional satisface exactamente $x^2=2$?**

La cuestión precisa es, por tanto:

> ¿podemos demostrar que existe un racional con cuadrado $2$, o podemos demostrar que ninguno existe?

La segunda alternativa es la correcta.

::: {#prp-t1-0006}
**Inexistencia de una solución racional de $x^2=2$.** No existe ningún número racional $q$ tal que

$$
q^2=2.
$$
:::

::: {.callout-note title="Idea de la prueba"}
Si un racional $q$ satisficiera $q^2=2$, podríamos elegir una representación reducida

$$
q=\frac mn
$$

con $m,n\in\mathbb Z$, $n\ne0$, y sin factor común entero mayor que $1$. La ecuación obligará primero a que $m$ sea par y después a que $n$ también sea par. Entonces ambos tendrán el factor común $2$, contradiciendo que la fracción fuese reducida.

El único hecho aritmético adicional que necesitaremos es este: si el cuadrado de un entero es par, entonces el entero es par. Lo justificamos localmente antes de usarlo.
:::

::: {.callout-note title="Lema de paridad (demostración local)"}
Supongamos que $m\in\mathbb Z$ y que $m^2$ es par. Si $m$ no fuera par, sería impar y podríamos escribir

$$
m=2k+1
$$

para algún $k\in\mathbb Z$. Entonces

$$
m^2=(2k+1)^2
=4k^2+4k+1
=2(2k^2+2k)+1,
$$

que es impar. Esto contradice que $m^2$ sea par. Por tanto,

$$
\boxed{m^2\text{ par}\Longrightarrow m\text{ par}.}
$$
:::

**Demostración.** Supongamos, para obtener una contradicción, que existe

$$
q\in\mathbb Q
$$

tal que

$$
q^2=2.
$$

Elegimos una representación reducida

$$
q=\frac mn,
$$

con $m,n\in\mathbb Z$, $n\ne0$, y sin factor común entero mayor que $1$.

Sustituyendo en la ecuación,

$$
\left(\frac mn\right)^2=2.
$$

Como $n\ne0$, podemos multiplicar por $n^2$ y obtener

$$
m^2=2n^2.
$$

El miembro derecho es divisible por $2$, así que $m^2$ es par. Por el lema de paridad, $m$ es par. Existe entonces $k\in\mathbb Z$ tal que

$$
m=2k.
$$

Sustituyendo esta expresión en $m^2=2n^2$,

$$
(2k)^2=2n^2,
$$

de modo que

$$
4k^2=2n^2.
$$

Dividiendo por $2$,

$$
n^2=2k^2.
$$

Por la misma razón, $n^2$ es par y el lema implica que $n$ es par. Existe, pues, $\ell\in\mathbb Z$ tal que

$$
n=2\ell.
$$

Hemos obtenido simultáneamente

$$
m=2k,
\qquad
n=2\ell.
$$

Por tanto, $m$ y $n$ tienen el factor común $2$, en contradicción con que $m/n$ hubiese sido elegida como una fracción reducida.

La suposición inicial es imposible. En consecuencia,

$$
\boxed{
\forall q\in\mathbb Q,\qquad q^2\ne2.
}
$$

$\blacksquare$

::: {.callout-note title="Después de la prueba"}
Conviene identificar la arquitectura del argumento.

1. **Objetivo:** demostrar una inexistencia dentro de $\mathbb Q$.
2. **Estrategia:** contradicción.
3. **Suposición temporal:** existe $q\in\mathbb Q$ con $q^2=2$.
4. **Representación útil:** $q=m/n$ en forma reducida.
5. **Mecanismo:** la ecuación fuerza primero $2\mid m$ y después $2\mid n$.
6. **Contradicción:** numerador y denominador tienen el factor común $2$.

La conclusión debe leerse con precisión. Hemos demostrado

$$
\boxed{
\text{no existe }q\in\mathbb Q\text{ tal que }q^2=2.
}
$$

No hemos demostrado todavía que exista algún número real cuyo cuadrado sea $2$. La inexistencia en un dominio y la existencia en otro son afirmaciones lógicamente distintas. Mantendremos esa separación hasta que la completitud nos autorice a construir la frontera real correspondiente.
:::

### Qué hemos demostrado y qué no

La proposición anterior establece exactamente

$$
\boxed{
\neg\exists q\in\mathbb Q
\qquad
q^2=2.
}
$$

Es decir: **dentro de $\mathbb Q$ no existe solución** de la ecuación $x^2=2$.

Es fácil deslizarse, sin advertirlo, desde esta afirmación hasta otra diferente:

$$
\exists x\in\mathbb R\setminus\mathbb Q
\qquad
x^2=2.
$$

Pero la segunda proposición contiene una afirmación nueva: **afirma que una solución existe**.

La diferencia lógica puede verse separando dos trabajos:

$$
\boxed{
\begin{array}{rcl}
\text{(I)}&\neg\exists q\in\mathbb Q& q^2=2,\\[3pt]
\text{(II)}&\exists x\in\mathbb R& x^2=2.
\end{array}
}
$$

La proposición anterior demuestra (I). Todavía no hemos demostrado (II).

Solo después de establecer (II) podremos combinar ambas afirmaciones: si existe $x\in\mathbb R$ con $x^2=2$ y ningún racional satisface esa ecuación, entonces ese $x$ necesariamente cumple

$$
x\notin\mathbb Q,
$$

y por tanto

$$
x\in\mathbb R\setminus\mathbb Q.
$$

Así, demostrar que **ningún racional** posee cierta propiedad no fabrica por sí solo un objeto no racional que la posea.

::: {.callout-warning title="Una negación de existencia no es una existencia"}
De

$$
\neg\exists q\in\mathbb Q\qquad q^2=2
$$

no podemos concluir, sin una premisa adicional,

$$
\exists x\in\mathbb R\setminus\mathbb Q\qquad x^2=2.
$$

Para esa conclusión necesitamos primero demostrar que alguna solución existe en $\mathbb R$.
:::

Esta distinción explica también una precaución de notación. Todavía no utilizaremos el símbolo

$$
\sqrt2
$$

como nombre de un número real cuya existencia ya hubiese sido establecida. Una notación puede describir qué objeto **queremos** identificar, pero no sustituye una demostración de que tal objeto existe.

La existencia real será obtenida más adelante mediante completitud: primero construiremos una frontera real como supremo y después demostraremos que esa frontera tiene cuadrado $2$. Solo entonces quedará legitimada, dentro de nuestra cadena lógica, la escritura $\sqrt2$.

### La diagonal de un cuadrado y el problema aritmético

La geometría hace que la situación sea todavía más provocadora. Consideremos un cuadrado de lado $1$. Si llamamos $d$ a la longitud de su diagonal, el teorema de Pitágoras impone la relación

$$
d^2=1^2+1^2=2.
$$

Aquí conviene distinguir dos lenguajes. La geometría nos presenta una **magnitud** —la diagonal— y una relación que esa magnitud debe satisfacer. La aritmética pregunta además:

> ¿puede esa magnitud representarse mediante un número del sistema numérico en el que estamos trabajando?

Si intentáramos representarla por un racional $q>0$, necesariamente tendría que cumplirse

$$
q^2=2.
$$

Pero acabamos de demostrar que ningún racional satisface esa ecuación. Por tanto,

$$
\boxed{
\text{la longitud de la diagonal de un cuadrado de lado }1
\text{ no puede representarse mediante un número racional}.
}
$$

Esta conclusión sigue sin ser una prueba de que, dentro de nuestro desarrollo axiomático, exista ya un número real particular que represente esa longitud. La imagen geométrica funciona aquí como **motivación del problema aritmético**: muestra qué clase de magnitud queremos poder incorporar, mientras que la existencia numérica deberá justificarse después mediante la completitud.

El obstáculo tampoco consiste en que los racionales estén «muy separados». Sean $r,s\in\mathbb Q$ con

$$
r<s.
$$

Su punto medio

$$
m=\frac{r+s}{2}
$$

sigue siendo racional. Además,

$$
m-r
=
\frac{s-r}{2}
>0
$$

y

$$
s-m
=
\frac{s-r}{2}
>0.
$$

Por tanto,

$$
\boxed{
r<\frac{r+s}{2}<s.
}
$$

Así, entre dos racionales distintos siempre existe otro racional. Podemos incluso repetir el procedimiento indefinidamente y seguir insertando racionales entre racionales.

Pero esta riqueza local del orden no responde una pregunta diferente: si ciertos racionales quedan sistemáticamente a un lado de una frontera y otros al lado opuesto, **¿debe existir un racional que ocupe esa frontera?**

La respuesta será negativa. La densidad entre puntos racionales no impide que falte un punto frontera racional.

Para hacer precisa esta diferencia entre «siempre hay puntos intermedios» y «toda frontera existe dentro del sistema», examinaremos ahora el ejemplo introductorio de Rudin.

### El ejemplo introductorio de Rudin, paso a paso

En el Ejemplo 1.1 de la tercera edición de *Principles of Mathematical Analysis*, Walter Rudin utiliza la ecuación $p^2=2$ para exhibir el hueco de los racionales. Después de demostrar que esa ecuación no tiene solución racional, considera los conjuntos

$$
A=\{p\in\mathbb Q:p>0,\ p^2<2\}
$$

y

$$
B=\{p\in\mathbb Q:p>0,\ p^2>2\}.
$$

Antes de estudiar la fórmula que aparecerá enseguida, conviene describir con precisión la estructura de estos dos conjuntos.

En primer lugar, ambos son no vacíos:

$$
1\in A,
\qquad
2\in B,
$$

porque

$$
1^2<2<2^2.
$$

En segundo lugar, todo racional positivo pertenece exactamente a uno de ellos. En efecto, si $p\in\mathbb Q$ y $p>0$, la tricotomía aplicada a $p^2$ y $2$ da exactamente una de las posibilidades

$$
p^2<2,
\qquad
p^2=2,
\qquad
p^2>2.
$$

La posibilidad intermedia ya fue excluida: ningún racional tiene cuadrado igual a $2$. Por tanto,

$$
p\in A
\qquad\text{o}\qquad
p\in B,
$$

y las dos alternativas son mutuamente excluyentes.

En tercer lugar, todo elemento de $A$ está estrictamente a la izquierda de todo elemento de $B$. Sean

$$
a\in A,
\qquad
b\in B.
$$

Supongamos, para obtener una contradicción, que $b\le a$. Como $a,b>0$, tenemos

$$
0<b\le a.
$$

La monotonía del cuadrado en los no negativos, @prp-t1-0007, da entonces

$$
b^2\le a^2.
$$

Pero $a\in A$ implica $a^2<2$, así que

$$
b^2\le a^2<2,
$$

en contradicción con $b\in B$, que exige $b^2>2$.

Por tanto,

$$
\boxed{
\forall a\in A\;\forall b\in B,
\qquad
a<b.
}
$$

Tenemos así dos regiones racionales no vacías, disjuntas y ordenadas:

$$
\boxed{
A\quad\text{queda por debajo del borde},
\qquad
B\quad\text{queda por encima del borde}.
}
$$

Pero todavía no hemos producido ningún punto que ocupe ese borde. El paso siguiente de Rudin es más fino: demostrar que tampoco hay un **último** racional por debajo ni un **primero** por encima.

En términos de cuantificadores, debemos probar

$$
\boxed{
\forall p\in A\;\exists q\in A
\qquad
p<q,
}
$$

y

$$
\boxed{
\forall p\in B\;\exists q\in B
\qquad
q<p.
}
$$

Estas dos afirmaciones implicarán, respectivamente, que $A$ no tiene máximo y que $B$ no tiene mínimo.

Para lograr ambas cosas con una sola construcción, Rudin introduce, para un racional positivo $p$,

$$
q
=
p-\frac{p^2-2}{p+2}
=
\frac{2p+2}{p+2}
=
\frac{2(p+1)}{p+2}.
$$

La fórmula funciona admirablemente, pero un lector novel puede preguntarse con toda razón:

> ¿de dónde salió $q$?

Conviene separar dos tareas. Primero verificaremos que la fórmula satisface exactamente las propiedades cuantificadas que necesitamos. Después reconstruiremos una ruta sistemática para diseñarla.

::: {#exm-t1-0012}
**El ejemplo de Rudin, sin pasos ocultos.** Para cada $p\in\mathbb Q$ con $p>0$, definamos

$$
q=p-\frac{p^2-2}{p+2}.
$$

Entonces:

- si $p^2<2$, se cumple
  $$
  p<q,
  \qquad
  q^2<2;
  $$
- si $p^2>2$, se cumple
  $$
  0<q<p,
  \qquad
  q^2>2.
  $$

En consecuencia,

$$
\forall p\in A\;\exists q\in A
\qquad
p<q,
$$

y

$$
\forall p\in B\;\exists q\in B
\qquad
q<p.
$$

Por tanto, $A$ no tiene máximo y $B$ no tiene mínimo.
:::

#### Primera pregunta: ¿q sigue siendo racional y positivo?

Sí, pero conviene separar tres comprobaciones.

**1. La expresión está bien definida.** Partimos de $p\in\mathbb Q$ con $p>0$. Entonces

$$
p+2>0,
$$

y, en particular,

$$
p+2\ne0.
$$

Por tanto, el cociente que aparece en

$$
q=\frac{2(p+1)}{p+2}
$$

está definido.

**2. El nuevo número sigue siendo racional.** Como $p\in\mathbb Q$ y $\mathbb Q$ es un cuerpo,

$$
p+1\in\mathbb Q,
\qquad
p+2\in\mathbb Q.
$$

Además, $2(p+1)\in\mathbb Q$ y, como $p+2\ne0$, también su cociente pertenece a $\mathbb Q$. Por tanto,

$$
\boxed{q\in\mathbb Q}.
$$

**3. El nuevo número sigue siendo positivo.** De $p>0$ obtenemos

$$
p+1>0,
\qquad
p+2>0.
$$

Como $2>0$,

$$
2(p+1)>0.
$$

El cociente de dos números positivos es positivo, luego

$$
\boxed{q>0}.
$$

Hemos probado así las dos condiciones de dominio que necesitaremos después:

$$
\boxed{
q\in\mathbb Q
\qquad\text{y}\qquad
q>0.
}
$$

Todavía no sabemos si $q$ pertenece a $A$ o a $B$. Para decidirlo faltan dos controles distintos: comparar primero $q$ con $p$ y después comparar $q^2$ con $2$.

#### Segunda pregunta: ¿q se mueve en la dirección correcta?

Comparemos ahora $q$ con el punto de partida $p$. Como

$$
q=\frac{2(p+1)}{p+2},
$$

podemos escribir

$$
\begin{aligned}
q-p
&=
\frac{2(p+1)}{p+2}-p\\
&=
\frac{2(p+1)-p(p+2)}{p+2}\\
&=
\frac{2+2p-p^2-2p}{p+2}\\
&=
\frac{2-p^2}{p+2}.
\end{aligned}
$$

La hipótesis $p>0$ ya nos dio

$$
p+2>0.
$$

Por tanto, dividir por $p+2$ **no cambia el signo**: el signo de $q-p$ es exactamente el signo de $2-p^2$.

Si $p\in A$, entonces

$$
p^2<2,
$$

de modo que

$$
2-p^2>0.
$$

Así,

$$
q-p>0,
$$

y por definición del orden

$$
\boxed{p<q}.
$$

Si, en cambio, $p\in B$, entonces

$$
p^2>2,
$$

por lo que

$$
2-p^2<0.
$$

En consecuencia,

$$
q-p<0,
$$

y por tanto

$$
\boxed{q<p}.
$$

Como ningún racional positivo satisface $p^2=2$, el numerador $2-p^2$ nunca es $0$ para los valores de $p$ que estamos considerando. Por ello el desplazamiento es siempre **estricto**.

Hemos demostrado hasta aquí exactamente

$$
\boxed{
\begin{aligned}
p\in A&\Longrightarrow p<q,\\
p\in B&\Longrightarrow q<p.
\end{aligned}
}
$$

La transformación se mueve, pues, en la dirección correcta: hacia la derecha desde $A$ y hacia la izquierda desde $B$.

Pero esta información todavía no basta para concluir

$$
q\in A
\qquad\text{o}\qquad
q\in B
$$

en el caso correspondiente. Moverse en la dirección adecuada no garantiza que no atravesemos la frontera.

Por ejemplo, si partiéramos de $p=1$ y utilizáramos la corrección ingenua

$$
p+(2-p^2),
$$

obtendríamos

$$
1+(2-1)=2,
$$

cuyo cuadrado es $4>2$. La dirección del movimiento era correcta, pero el paso fue demasiado grande y terminó al otro lado.

Por tanto, queda una tercera obligación: demostrar que la transformación de Rudin **conserva el lado** de la frontera en el que comenzó $p$.

#### Tercera pregunta: ¿q permanece en el mismo lado?

La comparación entre $q$ y $p$ controla la **dirección** del movimiento, pero todavía debemos verificar que la corrección no atraviese la frontera. Para ello necesitamos comparar $q^2$ con $2$.

Partimos de

$$
q=\frac{2(p+1)}{p+2}.
$$

Entonces

$$
\begin{aligned}
q^2-2
&=
\left(\frac{2(p+1)}{p+2}\right)^2-2\\
&=
\frac{4(p+1)^2}{(p+2)^2}
-
\frac{2(p+2)^2}{(p+2)^2}\\
&=
\frac{4(p+1)^2-2(p+2)^2}{(p+2)^2}.
\end{aligned}
$$

Abramos ahora el numerador:

$$
\begin{aligned}
4(p+1)^2-2(p+2)^2
&=
4(p^2+2p+1)-2(p^2+4p+4)\\
&=
4p^2+8p+4-2p^2-8p-8\\
&=
2p^2-4\\
&=
2(p^2-2).
\end{aligned}
$$

Por tanto,

$$
\boxed{
q^2-2
=
\frac{2(p^2-2)}{(p+2)^2}.
}
$$

De la primera comprobación sabemos que $p>0$, luego

$$
p+2>0
$$

y, en consecuencia,

$$
(p+2)^2>0.
$$

Además,

$$
2>0.
$$

Así, el factor

$$
\frac{2}{(p+2)^2}
$$

es estrictamente positivo. Multiplicar por él no cambia el signo. Por consiguiente,

$$
\boxed{
q^2-2\ \text{tiene exactamente el mismo signo que}\ p^2-2.
}
$$

Ahora podemos reunir las tres comprobaciones anteriores.

Si $p\in A$, entonces

$$
p\in\mathbb Q,
\qquad
p>0,
\qquad
p^2<2.
$$

La primera pregunta mostró que $q\in\mathbb Q$ y $q>0$; la segunda mostró que $p<q$; y la identidad recién obtenida da

$$
q^2-2<0,
$$

es decir,

$$
q^2<2.
$$

Por tanto,

$$
q\in A
$$

y, además,

$$
p<q.
$$

Como $p\in A$ fue arbitrario,

$$
\boxed{
\forall p\in A\;\exists q\in A
\qquad
p<q.
}
$$

En consecuencia, $A$ no tiene máximo.

Si $p\in B$, entonces

$$
p\in\mathbb Q,
\qquad
p>0,
\qquad
p^2>2.
$$

De nuevo, $q\in\mathbb Q$ y $q>0$; la segunda pregunta dio $q<p$; y ahora

$$
q^2-2>0,
$$

de modo que

$$
q^2>2.
$$

Así,

$$
q\in B
$$

y

$$
q<p.
$$

Como $p\in B$ fue arbitrario,

$$
\boxed{
\forall p\in B\;\exists q\in B
\qquad
q<p.
}
$$

Por tanto, $B$ no tiene mínimo.

La transformación ha cumplido simultáneamente las dos exigencias que fijamos al comienzo:

$$
\boxed{
\begin{array}{c}
p\in A\Longrightarrow p<q\in A,\\[4pt]
p\in B\Longrightarrow q\in B\text{ y }q<p.
\end{array}
}
$$

La demostración del ejemplo de Rudin queda así cerrada. La cuestión siguiente ya no será verificar que la fórmula funciona, sino comprender cómo puede diseñarse una transformación con estas propiedades.

### Cómo se fabrica una fórmula que parece caída del cielo

Rudin presenta $q$ directamente. Nosotros reconstruiremos una ruta posible para descubrirla. No pretendemos afirmar que este haya sido históricamente el proceso mental exacto mediante el cual se eligió la fórmula. Lo que sí podemos mostrar es que **una transformación con las propiedades necesarias puede diseñarse sistemáticamente**.

Partamos de un racional positivo $p$ y midamos su defecto respecto de la ecuación mediante

$$
E(p)=p^2-2.
$$

El signo de $E(p)$ indica de qué lado de la frontera se encuentra $p$:

$$
E(p)<0
\iff
p\in A,
$$

mientras que

$$
E(p)>0
\iff
p\in B.
$$

Por tanto, queremos que la corrección tenga signo opuesto al defecto:

- si $E(p)<0$, debemos aumentar $p$;
- si $E(p)>0$, debemos disminuirlo.

Una familia natural es

$$
q_c
=
p-\frac{p^2-2}{p+c},
$$

donde elegiremos

$$
c\in\mathbb Q,
\qquad
c>0.
$$

La positividad de $c$ cumple una primera función. Como $p>0$,

$$
p+c>0,
$$

de modo que el denominador no se anula. Además,

$$
q_c
=
\frac{cp+2}{p+c}.
$$

Como $c,p>0$, tanto $cp+2$ como $p+c$ son positivos. En consecuencia,

$$
\boxed{
q_c\in\mathbb Q
\qquad\text{y}\qquad
q_c>0.
}
$$

Ahora controlemos la **dirección** del movimiento. Restando $p$,

$$
\begin{aligned}
q_c-p
&=
-\frac{p^2-2}{p+c}\\
&=
\frac{2-p^2}{p+c}.
\end{aligned}
$$

Como $p+c>0$,

$$
\boxed{
\operatorname{sgn}(q_c-p)
=
\operatorname{sgn}(2-p^2).
}
$$

Así, para cualquier $c>0$, la transformación se mueve en la dirección deseada.

Pero eso no basta: también debemos impedir que atraviese la frontera. Calculemos el nuevo defecto:

$$
\begin{aligned}
q_c^2-2
&=
\frac{(cp+2)^2-2(p+c)^2}{(p+c)^2}\\
&=
\frac{c^2p^2+4cp+4-2p^2-4cp-2c^2}{(p+c)^2}\\
&=
\frac{(c^2-2)p^2-2(c^2-2)}{(p+c)^2}\\
&=
\boxed{
\frac{(c^2-2)(p^2-2)}{(p+c)^2}
}.
\end{aligned}
$$

Como

$$
(p+c)^2>0,
$$

el signo del nuevo defecto queda determinado por los dos factores

$$
c^2-2
\qquad\text{y}\qquad
p^2-2.
$$

Queremos que $q_c^2-2$ tenga el **mismo signo** que $p^2-2$. Para ello basta imponer

$$
\boxed{c^2-2>0}.
$$

La condición sobre el parámetro ya no es arbitraria. Si eligiéramos un racional positivo con

$$
c^2<2,
$$

el factor $c^2-2$ sería negativo y el signo del defecto se invertiría: la transformación cruzaría al lado opuesto. La posibilidad

$$
c^2=2
$$

no está disponible dentro de $\mathbb Q$, porque ya demostramos que ningún racional tiene cuadrado $2$.

Por tanto, entre los parámetros racionales positivos, la condición

$$
c^2>2
$$

es exactamente la que nos permite conservar el lado.

No necesitamos conocer todavía ningún número real con cuadrado $2$ para exhibir un parámetro racional adecuado. Basta escoger

$$
c=2,
$$

pues

$$
2^2-2=2>0.
$$

Sustituyendo $c=2$ obtenemos

$$
\boxed{
q
=
p-\frac{p^2-2}{p+2},
}
$$

que es precisamente la transformación utilizada en el ejemplo.

::: {.callout-important title="La técnica escondida"}
La fórmula puede reconstruirse mediante cuatro decisiones sucesivas:

1. **medir el defecto:** $E(p)=p^2-2$;
2. **elegir la dirección:** corregir $p$ con signo opuesto al defecto;
3. **introducir un parámetro racional positivo:** controlar el tamaño de la corrección sin perder racionalidad ni positividad;
4. **imponer un invariante de signo:** exigir que el nuevo defecto permanezca en el mismo lado.

En símbolos, el diseño busca simultáneamente

$$
\operatorname{sgn}(q_c-p)
=
-\operatorname{sgn}(E(p))
$$

y

$$
\operatorname{sgn}(E(q_c))
=
\operatorname{sgn}(E(p)).
$$

La primera condición mueve el punto **hacia** la frontera; la segunda evita que la atraviese.
:::

La fórmula de Rudin no es, por tanto, la única posible dentro de esta familia. Todo racional positivo $c$ con $c^2>2$ produce la misma arquitectura cualitativa. La elección $c=2$ es especialmente simple porque satisface inmediatamente la condición requerida y deja una expresión elemental.

### Ver la máquina funcionando

Las identidades anteriores ya demuestran el comportamiento de la transformación para todo racional positivo. Ahora podemos seguir algunas iteraciones concretas para ver el mecanismo con aritmética exacta.

Partamos por debajo del borde con

$$
p=1.
$$

Como

$$
T(p)=\frac{2(p+1)}{p+2},
$$

obtenemos sucesivamente

$$
1
\longmapsto
\frac43
\longmapsto
\frac75
\longmapsto
\frac{24}{17}.
$$

Verifiquemos que cada punto sigue del mismo lado:

$$
1^2=1<2,
$$

$$
\left(\frac43\right)^2
=
\frac{16}{9}
<2,
$$

$$
\left(\frac75\right)^2
=
\frac{49}{25}
<2,
$$

y

$$
\left(\frac{24}{17}\right)^2
=
\frac{576}{289}
<
\frac{578}{289}
=
2.
$$

Además,

$$
1<\frac43<\frac75<\frac{24}{17}.
$$

La cadena se mueve, por tanto, hacia la derecha sin abandonar $A$.

Si comenzamos por encima del borde con

$$
p=2,
$$

la misma transformación produce

$$
2
\longmapsto
\frac32
\longmapsto
\frac{10}{7}
\longmapsto
\frac{17}{12}.
$$

Ahora las comprobaciones son

$$
2^2=4>2,
$$

$$
\left(\frac32\right)^2
=
\frac94
>2,
$$

$$
\left(\frac{10}{7}\right)^2
=
\frac{100}{49}
>
\frac{98}{49}
=
2,
$$

y

$$
\left(\frac{17}{12}\right)^2
=
\frac{289}{144}
>
\frac{288}{144}
=
2.
$$

También

$$
2>\frac32>\frac{10}{7}>\frac{17}{12}.
$$

Esta cadena se mueve hacia la izquierda sin abandonar $B$.

Los cálculos ilustran el comportamiento, pero **una lista de ejemplos no demuestra la afirmación general**. La demostración sigue estando en las dos identidades válidas para todo racional positivo $p$:

$$
\boxed{
T(p)-p
=
\frac{2-p^2}{p+2},
}
$$

y

$$
\boxed{
T(p)^2-2
=
\frac{2(p^2-2)}{(p+2)^2}.
}
$$

La primera controla la dirección del movimiento; la segunda controla el lado de la frontera.

Tampoco diremos todavía que estas cadenas «convergen». No hemos definido convergencia de sucesiones ni demostrado ningún teorema que permita extraer de estas iteraciones la existencia de un límite. Por ahora solo estamos observando desigualdades exactas entre racionales.

::: {.callout-tip title="Antes de seguir"}
Sea

$$
T(p)=p-\frac{p^2-2}{p+2},
\qquad
p\ge1.
$$

Usando la identidad ya demostrada para $T(p)^2-2$, prueba que

$$
|T(p)^2-2|
\le
\frac29|p^2-2|.
$$

**Respuesta.** De

$$
T(p)^2-2
=
\frac{2(p^2-2)}{(p+2)^2}
$$

obtenemos, usando la multiplicatividad del valor absoluto,

$$
|T(p)^2-2|
=
\frac{2}{(p+2)^2}|p^2-2|,
$$

porque $(p+2)^2>0$.

Como $p\ge1$,

$$
p+2\ge3>0.
$$

La monotonía del cuadrado en los no negativos da

$$
(p+2)^2\ge9.
$$

Como ambas cantidades son positivas, al tomar recíprocos se invierte el orden:

$$
\frac{1}{(p+2)^2}
\le
\frac19.
$$

Multiplicando por $2>0$,

$$
0<
\frac{2}{(p+2)^2}
\le
\frac29.
$$

Finalmente,

$$
\boxed{
|T(p)^2-2|
\le
\frac29|p^2-2|.
}
$$

Así, para $p\ge1$, una aplicación de $T$ deja el nuevo defecto absoluto como máximo en $2/9$ del defecto anterior. Esta es una estimación cuantitativa exacta; todavía no la interpretamos como una afirmación de convergencia.
:::

### Entonces, ¿dónde está exactamente el hueco?

La palabra «hueco» puede inducir una imagen equivocada. No significa que exista alrededor de la frontera un intervalo sin números racionales. Eso sería falso: entre dos racionales distintos siempre podemos insertar otro racional.

El fenómeno es más sutil.

Recordemos

$$
A=\{p\in\mathbb Q:p>0,\ p^2<2\}
$$

y

$$
B=\{p\in\mathbb Q:p>0,\ p^2>2\}.
$$

Ya hemos demostrado cuatro hechos:

$$
A\ne\varnothing,
\qquad
B\ne\varnothing,
$$

$$
\forall a\in A\;\forall b\in B,
\qquad
a<b,
$$

$$
\forall a\in A\;\exists a'\in A,
\qquad
a<a',
$$

y

$$
\forall b\in B\;\exists b'\in B,
\qquad
b'<b.
$$

Por tanto, $A$ no tiene máximo y $B$ no tiene mínimo. Además, como todo elemento de $A$ está por debajo de todo elemento de $B$, cada $b\in B$ es una cota superior racional de $A$.

Aquí aparece una distinción importante. Que $A$ no tenga máximo **no basta**, por sí solo, para decir que carece de supremo. Por ejemplo,

$$
(0,1)\cap\mathbb Q
$$

no tiene máximo dentro de $\mathbb Q$, pero sí posee la menor cota superior racional $1$.

Así que el problema no consiste simplemente en que «falta el último elemento de $A$». La pregunta correcta es más fuerte:

> entre todas las cotas superiores racionales de la región inferior, ¿existe una que sea menor que todas las demás?

Para conectar esta pregunta con la formulación que utilizaremos en §1.5, introducimos

$$
S_{\mathbb Q}
=
\{q\in\mathbb Q:q\ge0,\ q^2<2\}.
$$

Este conjunto no es literalmente el mismo que $A$. Como $0^2<2$,

$$
\boxed{
S_{\mathbb Q}=A\cup\{0\}.
}
$$

Sin embargo, añadir $0$ no cambia las cotas superiores. En efecto, como

$$
1\in A,
$$

toda cota superior $u$ de $A$ satisface

$$
1\le u,
$$

y por tanto también

$$
0\le u.
$$

Así, toda cota superior de $A$ también domina al nuevo elemento $0$. Recíprocamente, toda cota superior de $S_{\mathbb Q}$ es automáticamente cota superior de $A\subseteq S_{\mathbb Q}$. Luego ambos conjuntos tienen exactamente las mismas cotas superiores racionales.

Podemos formular entonces con precisión la cuestión pendiente:

$$
\boxed{
\text{¿existe }s\in\mathbb Q
\text{ que sea la menor cota superior de }S_{\mathbb Q}\text{ dentro de }\mathbb Q?
}
$$

El trabajo realizado en esta sección ya ha dejado visibles todos los ingredientes que harán fracasar esa posibilidad: por debajo siempre podemos subir, por encima siempre podemos bajar y ningún racional satisface $q^2=2$.

Pero conviene mantener separadas **intuición estructural** y **demostración formal**. En §1.5 volveremos a $S_{\mathbb Q}$ y probaremos explícitamente, en el lenguaje de supremos, que

$$
S_{\mathbb Q}
$$

es no vacío y está acotado superiormente en $\mathbb Q$, pero no posee una menor cota superior racional.

Ese será el sentido preciso del hueco:

$$
\boxed{
\begin{array}{c}
\text{no falta un intervalo de racionales;}\\[3pt]
\text{falta en }\mathbb Q\text{ el punto frontera exigido por la propiedad del supremo.}
\end{array}
}
$$

El paso a $\mathbb R$ no consistirá, por tanto, en «rellenar espacios visibles» entre racionales, sino en imponer una propiedad estructural que garantice la existencia de fronteras bajo hipótesis precisas.

### Una segunda lectura del ejemplo de Rudin

El ejemplo clásico comprime mucho más que una manipulación ingeniosa. Conviene releerlo ahora como un pequeño mapa de habilidades matemáticas.

**1. Traducir una afirmación verbal a cuantificadores.** Decir que $A$ no tiene máximo no significa comprobar algunos elementos. Exige demostrar

$$
\forall p\in A\;\exists q\in A
\qquad
p<q.
$$

Del mismo modo, decir que $B$ no tiene mínimo exige

$$
\forall p\in B\;\exists q\in B
\qquad
q<p.
$$

El elemento nuevo puede depender del punto de partida, pero la construcción debe funcionar para **todo** punto admisible.

**2. Diseñar un objeto que satisfaga varias condiciones a la vez.** No basta producir un racional mayor que $p$ cuando $p\in A$, ni uno menor cuando $p\in B$. El nuevo número debe conservar simultáneamente:

$$
q\in\mathbb Q,
\qquad
q>0,
$$

y el lado de la desigualdad respecto de $2$:

$$
p^2<2
\Longrightarrow
q^2<2,
$$

$$
p^2>2
\Longrightarrow
q^2>2.
$$

Por eso el problema no era simplemente «mover $p$», sino moverlo **sin abandonar la región correcta**.

**3. Separar las funciones de cada cálculo.** Las dos identidades centrales responden a preguntas distintas:

$$
q-p=\frac{2-p^2}{p+2}
$$

controla la **dirección** del movimiento, mientras que

$$
q^2-2=\frac{2(p^2-2)}{(p+2)^2}
$$

controla el **invariante de signo** que impide cruzar de $A$ a $B$ o de $B$ a $A$.

Ninguna de las dos comprobaciones reemplaza a la otra.

**4. Interpretar la construcción en el nivel estructural correcto.** De las identidades anteriores obtenemos

$$
A\text{ no tiene máximo}
\qquad\text{y}\qquad
B\text{ no tiene mínimo}.
$$

Pero, como acabamos de advertir, de aquí todavía no se sigue que $A$ —o $S_{\mathbb Q}$— carezca de supremo racional. La ausencia de un elemento extremo y la ausencia de una menor cota superior son afirmaciones diferentes.

El paso conceptual decisivo consiste precisamente en cambiar de pregunta:

$$
\boxed{
\text{¿existe dentro de }\mathbb Q
\text{ una menor cota superior para }S_{\mathbb Q}\,?
}
$$

La transformación de Rudin ya contiene la maquinaria que necesitaremos para responder, pero la respuesta formal pertenece a §1.5.

::: {.callout-note title="Mapa de dependencias"}
El argumento puede leerse también como una cadena de dependencias:

$$
\boxed{
\begin{array}{c}
\text{cuerpo ordenado}
\\[3pt]
\downarrow
\\[3pt]
\text{signos, desigualdades y monotonía del cuadrado}
\\[3pt]
\downarrow
\\[3pt]
\text{transformación racional controlada}
\\[3pt]
\downarrow
\\[3pt]
A\text{ sin máximo y }B\text{ sin mínimo}
\\[3pt]
\downarrow
\\[3pt]
\text{pregunta por la existencia de una frontera como supremo}.
\end{array}
}
$$

La demostración de que ningún racional satisface $q^2=2$ elimina además la única posibilidad de que la frontera buscada estuviera representada por un racional con cuadrado exactamente igual a $2$.
:::

El verdadero tema que ha aparecido no es, por tanto, la raíz cuadrada de $2$ como objeto aislado. La pregunta general es:

> si un conjunto no vacío está acotado superiormente, ¿qué propiedad del sistema numérico garantiza que exista dentro de ese mismo sistema una menor cota superior?

Ya disponemos del vocabulario necesario para formular la respuesta. La propiedad adicional será la **completitud**.

### Qué nos llevamos a la sección siguiente

El estudio del hueco racional deja cuatro conclusiones que conviene mantener separadas.

**Primera.** Hemos demostrado una inexistencia precisa dentro de $\mathbb Q$:

$$
\boxed{
\forall q\in\mathbb Q,
\qquad
q^2\ne2.
}
$$

Esta afirmación no contiene todavía una prueba de que exista algún número real cuyo cuadrado sea $2$.

**Segunda.** La densidad elemental de los racionales no resuelve el problema de las fronteras. Saber que entre dos racionales distintos existe otro racional responde a una pregunta sobre **puntos intermedios**. Preguntar si un conjunto no vacío y acotado superiormente posee una **menor cota superior dentro del mismo sistema** es una pregunta distinta.

En particular, para

$$
S_{\mathbb Q}
=
\{q\in\mathbb Q:q\ge0,\ q^2<2\},
$$

la cuestión pendiente es

$$
\boxed{
\text{¿existe }\sup_{\mathbb Q}S_{\mathbb Q}\text{?}
}
$$

**Tercera.** El ejemplo de Rudin ha dejado una técnica de construcción reutilizable:

$$
\boxed{
\text{medir el defecto}
\to
\text{corregir en la dirección adecuada}
\to
\text{controlar dominio y signo}
\to
\text{producir un nuevo punto sin cruzar la frontera}.
}
$$

La fórmula concreta importa menos que esta arquitectura: una construcción útil debe satisfacer simultáneamente todas las condiciones exigidas por el problema.

**Cuarta.** La deuda de existencia permanece abierta. Hasta aquí la estructura de cuerpo ordenado nos ha permitido formular el problema y analizarlo, pero no nos ha proporcionado todavía el punto frontera buscado en $\mathbb R$.

La secuencia lógica de las dos secciones siguientes será deliberadamente separada. En §1.5 formularemos el **axioma de completitud** y volveremos a $S_{\mathbb Q}$ para demostrar formalmente que no posee supremo racional. Después consideraremos la región análoga dentro de $\mathbb R$ y la completitud garantizará la existencia de un supremo real.

Eso todavía no bastará para resolver la ecuación. En §1.6 deberemos identificar la frontera obtenida y demostrar, sin continuidad ni límites, que su cuadrado es exactamente $2$.

Podemos resumir el tránsito así:

$$
\boxed{
\text{pregunta por el fallo en }\mathbb Q
\to
\text{completitud de }\mathbb R
\to
\text{existencia de una frontera real}
\to
\text{identificación de esa frontera}.
}
$$

