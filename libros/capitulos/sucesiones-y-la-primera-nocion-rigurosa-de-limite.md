---
title: "Sucesiones y la primera noción rigurosa de límite"
description: "Capítulo 3 de Cálculo para matemáticos. Edición canónica v11."
content-id: MA-BCH-0010
content-type: book-chapter
collection: PM-CAL
book-id: MA-BOK-0001
status: published
date-created: 2026-09-10
date-modified: 2026-09-19
areas:
  - fundamentos
  - calculo
  - analisis
level: fundamental
topics:
  - sucesiones
  - colas
  - convergencia
  - limites-secuenciales
  - epsilon-N
  - algebra-de-limites
  - teorema-del-sandwich
  - monotonia
  - completitud
  - sucesiones-recursivas
  - limites-infinitos
prerequisites: 
  - MA-BCH-0003
  - MA-BCH-0004
related:
  - MA-CON-0016
  - MA-BOK-0001
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
number-sections: true
number-depth: 2
number-offset: [2]
---

# Sucesiones y la primera noción rigurosa de límite {#sec-t1-c04}

Los dos capítulos precedentes proporcionaron la estructura ordenada y completa de $\mathbb R$ y la definición precisa de función. En ambos aprendimos también a separar hipótesis, existencia y unicidad y a justificar los pasos de una demostración.

Ahora esos tres hilos empiezan a encontrarse.

La idea de **límite** intenta describir un tipo de comportamiento que no puede decidirse mirando únicamente una cantidad fija de datos. Cuando escribimos una sucesión

$$
a_0,a_1,a_2,a_3,\dots,
$$

la lista no termina. Podemos calcular cien términos, mil o un millón, pero siempre quedan términos posteriores. Por eso una teoría rigurosa del límite necesita responder una pregunta distinta de las que aparecen en un cálculo finito:

$$
\boxed{
\text{¿cómo expresamos matemáticamente lo que ocurre a partir de algún momento y para siempre después?}
}
$$

Las sucesiones serán nuestro primer laboratorio para esa pregunta. Son funciones, pero tienen un dominio especialmente simple: los números naturales. Esa discreción nos permitirá concentrarnos en la estructura lógica del límite antes de afrontar, en el capítulo siguiente, la dificultad adicional de acercar una variable real a un punto.

Este capítulo no comenzará definiendo el límite. Antes necesitamos aprender a mirar una sucesión de la manera adecuada. La noción decisiva será la de **cola**: para estudiar el comportamiento final, los primeros términos pueden dejar de importar.

## Una sucesión es una función, pero el límite vive en la cola {#sec-t1-c04-01}

### Dos sucesiones que parecen iguales durante muchísimo tiempo

Consideremos primero

$$
a_n=\frac{1}{n+1},
\qquad n\in\mathbb N.
$$

Como en este tratado usamos

$$
\mathbb N=\{0,1,2,\dots\},
$$

sus primeros términos son

$$
1,\frac12,\frac13,\frac14,\frac15,\dots
$$

A medida que el índice crece, los términos se hacen pequeños. No estamos formulando todavía qué significa rigurosamente «hacerse pequeños», pero la tendencia visual y aritmética resulta familiar.

Construyamos ahora otra sucesión:

$$
b_n=
\begin{cases}
\dfrac{1}{n+1}, & 0\le n\le 10^6,\\[4pt]
1, & n>10^6.
\end{cases}
$$

Durante todo el tramo

$$
n=0,1,2,\dots,10^6,
$$

las dos sucesiones son exactamente iguales:

$$
a_n=b_n.
$$

Esto significa que podemos inspeccionar más de un millón de términos sin detectar diferencia alguna. Sin embargo, después del índice $10^6$ sus comportamientos se separan por completo.

La primera sigue obedeciendo

$$
a_n=\frac{1}{n+1},
$$

y sus términos continúan disminuyendo en tamaño. La segunda, en cambio, queda fijada para siempre en

$$
b_n=1.
$$

Si nuestro criterio dependiera solo de una muestra finita de términos, por enorme que fuera, no podría distinguir estas dos sucesiones. Podemos hacer que el tramo común tenga diez términos, un millón, un billón o cualquier cantidad finita previamente elegida. Siempre es posible modificar lo que ocurre después.

Este ejemplo contiene la primera dificultad conceptual del capítulo:

$$
\boxed{
\text{ninguna inspección de una cantidad finita de términos determina por sí sola el comportamiento final de una sucesión.}
}
$$

Por eso, cuando más adelante hablemos de límite, la pregunta relevante no será

> ¿qué ocurre en los primeros términos?,

sino

> ¿qué ocurre con **todos los términos suficientemente tardíos**?

Antes de formalizar esa idea necesitamos precisar qué es exactamente una sucesión.

### La variable ya no recorre un intervalo real

En `T1-C03` escribíamos funciones como

$$
f\colon\mathbb R\to\mathbb R
$$

o

$$
g\colon[0,\infty)\to\mathbb R.
$$

Una sucesión real es también una función, pero ahora el dominio es discreto. En lugar de introducir cualquier número real permitido, introducimos índices naturales.

Por ejemplo,

$$
a\colon\mathbb N\to\mathbb R,
\qquad
a(n)=\frac{1}{n+1}.
$$

La notación tradicional para sucesiones reemplaza habitualmente $a(n)$ por

$$
a_n.
$$

Así,

$$
a_0=1,
\qquad
a_1=\frac12,
\qquad
a_2=\frac13,
\qquad\dots
$$

El subíndice no crea un nuevo tipo de objeto: simplemente indica que estamos evaluando una función en el índice $n$.

Esta observación conecta directamente este capítulo con el anterior:

$$
\boxed{a_n=a(n).}
$$

La escritura con subíndices es conveniente, pero la estructura subyacente sigue siendo funcional.

### Índice y término no son lo mismo

En

$$
a_n=\frac{1}{n+1},
$$

el número $n$ es el **índice** y $a_n$ es el **término correspondiente**.

Para $n=4$ tenemos

$$
a_4=\frac15.
$$

Aquí $4$ y $1/5$ desempeñan papeles completamente distintos. El primero pertenece al dominio de la función; el segundo pertenece a su codominio.

Conviene hacer esta separación desde el principio porque las afirmaciones sobre sucesiones mezclan con frecuencia ambas variables. Una frase como

> para índices suficientemente grandes, los términos son menores que $0.01$

habla simultáneamente de

- **índices** $n$ que deben ser suficientemente grandes;
- **términos** $a_n$ que deben satisfacer una cierta desigualdad.

Confundir esos dos niveles hace casi imposible leer correctamente las definiciones de límite.

### Las sucesiones pueden comenzar después de cero

No toda fórmula natural está definida en $n=0$. Por ejemplo,

$$
c_n=\frac1n
$$

no tiene sentido para $n=0$. No necesitamos alterar nuestra convención sobre $\mathbb N$. Simplemente podemos declarar

$$
c\colon\{n\in\mathbb N:n\ge1\}\to\mathbb R,
\qquad
c_n=\frac1n.
$$

En general, será conveniente permitir sucesiones que comiencen en un índice $n_0\in\mathbb N$.

El conjunto

$$
\{n\in\mathbb N:n\ge n_0\}
$$

es una cola de $\mathbb N$: contiene $n_0$ y todos los naturales posteriores.

Esto no es un detalle puramente tipográfico. Muchas veces la expresión que define una sucesión solo tiene sentido a partir de cierto índice. La teoría del comportamiento final debe poder trabajar naturalmente con ese tipo de dominio.

::: {#def-t1-0027}
**Sucesión real, término, cola y propiedad eventual.** Sea $n_0\in\mathbb N$.

Una **sucesión real a partir de $n_0$** es una función

$$
a\colon\{n\in\mathbb N:n\ge n_0\}\to\mathbb R.
$$

El valor

$$
a_n:=a(n)
$$

se llama **término de índice $n$**. La sucesión puede denotarse por

$$
(a_n)_{n\ge n_0}.
$$

Cuando $n_0=0$, escribiremos con frecuencia simplemente

$$
(a_n).
$$

Si $N\ge n_0$, la **cola de la sucesión a partir de $N$** es la restricción

$$
a|_{\{n\in\mathbb N:n\ge N\}},
$$

que escribiremos también como

$$
(a_n)_{n\ge N}.
$$

Diremos que una propiedad $P(n)$ de los términos de la sucesión se cumple **eventualmente** si existe un índice $N\ge n_0$ tal que

$$
P(n)
\qquad
\text{para todo }n\ge N.
$$

En símbolos,

$$
\exists N\ge n_0\;\forall n\ge N:\;P(n).
$$
:::

La palabra **eventualmente** condensa por tanto una estructura lógica muy concreta:

$$
\boxed{
\text{eventualmente}
\quad\Longleftrightarrow\quad
\exists N\;\forall n\ge N.
}
$$

No significa «muchas veces», «para índices grandes en general» ni «casi siempre» en un sentido informal. Significa que podemos encontrar un umbral después del cual **no aparece ninguna excepción**.

### Una sucesión no es solo el conjunto de sus valores

Consideremos

$$
u_n=(-1)^n.
$$

La sucesión es

$$
1,-1,1,-1,1,-1,\dots
$$

El conjunto de valores que toma es simplemente

$$
\{-1,1\}.
$$

Pero la sucesión contiene información que ese conjunto ha perdido: cuál valor aparece en cada índice y en qué orden aparecen los términos.

La función

$$
v_n=1
$$

cuando $n$ es par y

$$
v_n=-1
$$

cuando $n$ es impar describe la misma sucesión que $u_n=(-1)^n$. En cambio, una sucesión que vale $1$ durante los primeros cien índices y luego vale siempre $-1$ tiene también como conjunto de valores

$$
\{-1,1\},
$$

pero su comportamiento es completamente distinto.

Por eso no identificaremos

$$
(a_n)
$$

con

$$
\{a_n:n\ge n_0\}.
$$

La segunda expresión es un conjunto; la primera es una función indexada. En un conjunto desaparecen el orden y las repeticiones. En una sucesión, ambos forman parte de la información.

### Distintas maneras de especificar una sucesión

Como cualquier función, una sucesión puede quedar determinada de distintas maneras. Una fórmula explícita es solo una posibilidad.

::: {#exm-t1-0030}
**Cuatro maneras de especificar sucesiones.**

1. **Mediante una fórmula explícita.**

   $$
   a_n=\frac{(-1)^n}{n+1},
   \qquad n\ge0.
   $$

   Cada índice determina directamente su término.

2. **Mediante una regla por casos.**

   $$
   b_n=
   \begin{cases}
   0, & n\text{ par},\\
   1, & n\text{ impar}.
   \end{cases}
   $$

   Aquí la paridad del índice decide qué valor se asigna.

3. **Mediante una regla verbal inequívoca.**

   Sea $c_n=1$ si $n$ es un número primo y $c_n=0$ en caso contrario. La regla determina un único número real para cada $n\in\mathbb N$.

4. **Mediante una recurrencia y datos iniciales.**

   $$
   d_0=3,
   \qquad
   d_{n+1}=\frac{d_n+1}{2}.
   $$

   No disponemos aquí de una fórmula explícita para $d_n$ desde el comienzo, pero los datos determinan sucesivamente

   $$
   d_1=2,
   \qquad
   d_2=\frac32,
   \qquad
   d_3=\frac54,
   \qquad\dots
   $$

En los cuatro casos el objeto final es del mismo tipo: una función cuyo dominio es un conjunto de índices naturales.
:::

Este ejemplo permite corregir otra intuición engañosa: una sucesión no necesita venir acompañada por una fórmula cerrada del tipo

$$
a_n=F(n).
$$

Una recurrencia puede definirla perfectamente bien si los datos iniciales y la regla determinan de manera única cada término posterior.

También debemos tener cuidado con las tablas. Una tabla **infinita** de pares índice–valor podría especificar una sucesión completa, del mismo modo que podría especificar cualquier función. Pero una tabla impresa con, por ejemplo, los valores

$$
\begin{array}{c|ccccc}
n&0&1&2&3&4\\
\hline
a_n&1&2&4&8&16
\end{array}
$$

solo fija cinco términos. Por sí sola no determina qué ocurre en $n=5,6,7,\dots$.

Podemos conjeturar que la regla es $a_n=2^n$, pero también existen infinitas sucesiones diferentes que comienzan con

$$
1,2,4,8,16
$$

y después se comportan de otra manera. Una muestra finita puede sugerir una ley; no la sustituye.

### Qué significa mirar una cola

Sea

$$
a_n=\frac{(-1)^n}{n+1}.
$$

Sus primeros términos son

$$
1,-\frac12,\frac13,-\frac14,\frac15,\dots
$$

La cola a partir de $N=4$ es

$$
\left(\frac15,-\frac16,\frac17,-\frac18,\dots\right).
$$

La cola a partir de $N=100$ comienza en $a_{100}$ y descarta todos los términos anteriores.

En lenguaje de funciones, no hemos creado un objeto misterioso: simplemente hemos restringido el dominio de $a$ a

$$
\{n\in\mathbb N:n\ge N\}.
$$

La idea de cola sirve para separar dos tipos de información:

- lo que ocurre en una cantidad finita de índices iniciales;
- lo que persiste después de algún índice.

El segundo tipo será el relevante para los límites.

### Propiedades que llegan para quedarse

Consideremos la afirmación

$$
|a_n|<\frac1{100}
$$

para la sucesión

$$
a_n=\frac{(-1)^n}{n+1}.
$$

Como

$$
|a_n|=\frac1{n+1},
$$

si $n\ge100$, entonces

$$
n+1\ge101
$$

y por tanto

$$
|a_n|=\frac1{n+1}\le\frac1{101}<\frac1{100}.
$$

Así, la propiedad

$$
|a_n|<\frac1{100}
$$

se cumple eventualmente. Un índice que funciona como umbral es $N=100$.

No afirmamos que la desigualdad se cumpla para todos los índices. De hecho,

$$
|a_0|=1.
$$

Lo que importa es que, una vez superado cierto umbral, no vuelve a fallar.

Comparemos con otra propiedad:

$$
a_n>0.
$$

Esta no se cumple eventualmente, porque para todo $N$ existen índices impares $n\ge N$, y en ellos

$$
a_n<0.
$$

Tampoco se cumple eventualmente

$$
a_n<0,
$$

porque siempre reaparecen índices pares con $a_n>0$.

El contraste muestra que «eventualmente» no quiere decir que una afirmación sea frecuente. En esta sucesión hay infinitos términos positivos e infinitos términos negativos, pero ninguna de las dos propiedades de signo llega a mantenerse para siempre.

### El orden de los cuantificadores importa

La definición de eventualidad contiene

$$
\exists N\;\forall n\ge N.
$$

Primero debemos encontrar **un solo** umbral $N$. Después, ese mismo umbral debe controlar **todos** los índices posteriores.

No sería suficiente decir:

> para cada índice $n$ puedo encontrar algún $N\le n$ para el cual la propiedad se cumple en $n$.

Eso permitiría cambiar el umbral cada vez y no impondría ningún comportamiento persistente.

La estructura correcta tiene una dirección temporal lógica:

$$
\boxed{
\text{elegimos un umbral}
\longrightarrow
\text{controlamos toda la cola posterior}.
}
$$

Esta arquitectura aparecerá una y otra vez en análisis. En la sección siguiente añadiremos un cuantificador nuevo delante de ella: alguien fijará una tolerancia y nosotros tendremos que responder con un umbral que controle toda la cola.

### Un prefijo enorme sigue siendo un prefijo finito

Volvamos ahora a las sucesiones con las que abrimos la sección.

::: {#exm-t1-0031}
**Coincidir durante un millón de índices no determina el comportamiento final.** Sean

$$
a_n=\frac1{n+1}
$$

y

$$
b_n=
\begin{cases}
\dfrac1{n+1}, & 0\le n\le10^6,\\[4pt]
1, & n>10^6.
\end{cases}
$$

Para todo índice del intervalo

$$
0\le n\le10^6
$$

tenemos

$$
a_n=b_n.
$$

Sin embargo, consideremos la propiedad

$$
P(n):\quad a_n<\frac12.
$$

Para la sucesión $(a_n)$, esta propiedad se cumple eventualmente. Por ejemplo, si $n\ge2$, entonces

$$
a_n=\frac1{n+1}\le\frac13<\frac12.
$$

En cambio, para $(b_n)$ la propiedad

$$
b_n<\frac12
$$

no se cumple eventualmente. En efecto, para todo $n>10^6$ tenemos

$$
b_n=1.
$$

Las dos sucesiones comparten un prefijo extraordinariamente largo, pero sus colas satisfacen propiedades eventuales diferentes.
:::

Podríamos reemplazar $10^6$ por cualquier número natural $M$. La conclusión sería la misma. No existe una longitud finita privilegiada a partir de la cual una inspección por sí sola garantice el comportamiento futuro.

Esta es una razón profunda para que las definiciones de análisis utilicen cuantificadores en lugar de expresiones como

> «miramos muchos términos y parece que...».

La experimentación numérica puede sugerir una conjetura. La definición rigurosa debe controlar una cantidad infinita de índices mediante una afirmación finita.

### Cambiar una cantidad finita de términos no altera una propiedad eventual

La noción de cola produce inmediatamente un principio que utilizaremos de manera constante.

Supongamos que una propiedad $P(n)$ se cumple eventualmente para una sucesión $(a_n)$. Entonces existe algún $N$ tal que

$$
P(n)
\qquad
\text{para todo }n\ge N.
$$

Ahora modifiquemos los términos

$$
a_0,a_1,\dots,a_M
$$

para algún índice finito $M$, dejando intactos todos los términos posteriores.

Si $M<N$, la cola a partir de $N$ ni siquiera ha sido tocada.

Si $M\ge N$, basta comenzar a mirar después de ambas fronteras. Por ejemplo, podemos elegir

$$
K=M+1.
$$

Entonces, para todo $n\ge K$, los términos modificados y los originales coinciden. Como además $K>N$, la propiedad $P(n)$ sigue cumpliéndose en toda esa cola.

En forma esquemática,

$$
\boxed{
\text{una propiedad eventual depende de alguna cola, no de un prefijo finito.}
}
$$

No estamos diciendo que cambiar los primeros términos sea irrelevante para **todas** las preguntas sobre una sucesión. Puede cambiar, por ejemplo, su primer término, su valor máximo o una identidad que se exija para cada índice. La afirmación es más precisa: las propiedades formuladas como

$$
\exists N\;\forall n\ge N
$$

son insensibles a cualquier modificación que afecte solo a una cantidad finita de índices.

### «Para índices grandes» no significa que exista un índice mágico

El lenguaje informal «cuando $n$ es grande» puede inducir a pensar que existe un número universal a partir del cual todas las propiedades interesantes se vuelven verdaderas. No es así.

Para

$$
a_n=\frac1{n+1},
$$

la propiedad

$$
a_n<\frac1{10}
$$

se cumple, por ejemplo, desde $n=10$.

La propiedad más exigente

$$
a_n<\frac1{1000}
$$

requiere avanzar mucho más. Podemos usar $N=1000$.

Y si exigimos

$$
a_n<\frac1{10^9},
$$

el umbral deberá alejarse todavía más.

Por tanto, «eventualmente» siempre debe leerse en relación con **una propiedad concreta**. El umbral que sirve para una condición puede no servir para otra.

Esta dependencia será el centro lógico de la definición de límite: cuanto menor sea la tolerancia que exijamos, más lejos podría ser necesario avanzar en la sucesión.

Todavía no escribiremos esa definición. Antes conviene fijar una última distinción.

### Lo eventual no exige monotonía

La sucesión

$$
a_n=\frac{(-1)^n}{n+1}
$$

alterna de signo. Sus términos no avanzan todos en una misma dirección: uno es positivo, el siguiente negativo, y así sucesivamente.

Sin embargo, como vimos,

$$
|a_n|<\frac1{100}
$$

se cumple eventualmente.

Esto muestra que una propiedad de cola puede estabilizarse aunque los términos continúen oscilando en otros aspectos. Más adelante distinguiremos cuidadosamente entre

- acercarse a un valor;
- ser creciente o decreciente;
- estar acotada;
- oscilar.

Son propiedades diferentes y ninguna debe confundirse prematuramente con las demás.

### Qué hemos ganado antes de definir un límite

Ya podemos describir con precisión el tipo de pregunta que nos interesa.

Una sucesión es una función

$$
a\colon\{n\in\mathbb N:n\ge n_0\}\to\mathbb R.
$$

Sus términos están ordenados por índices. Una cola descarta una cantidad finita de términos iniciales y conserva todos los posteriores. Una propiedad es eventual cuando existe una cola completa en la que esa propiedad se cumple sin excepciones.

El esquema lógico es

$$
\boxed{
\exists N\;\forall n\ge N.
}
$$

Eso todavía no define que $(a_n)$ tenga límite $L$. Pero ya contiene la parte temporal de la definición: **a partir de algún índice, todos los términos posteriores deberán obedecer una condición**.

La pregunta siguiente será cuál debe ser esa condición.

Si queremos expresar que los términos se acercan a un número $L$, decir simplemente «$a_n$ está cerca de $L$» no basta. Necesitamos medir la cercanía y exigir que podamos hacerla tan estricta como queramos.

Ese será el paso de §3.2: transformar la intuición

$$
\text{«$a_n$ se acerca a $L$»}
$$

en una afirmación cuantificada que pueda demostrarse línea por línea.

## Tan cerca como queramos, desde algún momento: la definición $\varepsilon$–$N$ {#sec-t1-c04-02}

En §3.1 aprendimos a reconocer la parte temporal de una afirmación sobre el comportamiento final de una sucesión:

$$
\exists N\;\forall n\ge N.
$$

Quedó pendiente decidir qué propiedad deben satisfacer todos esos términos tardíos si queremos expresar que una sucesión «se acerca» a un número $L$.

La palabra **cerca** todavía es demasiado imprecisa. Dos números pueden parecernos cercanos en una escala y muy alejados en otra. Si estamos aproximando una longitud de varios kilómetros, un error de un metro puede ser pequeño; si estamos midiendo el grosor de una célula, el mismo error sería enorme. Una definición matemática no puede depender de esa apreciación contextual.

Necesitamos sustituir «cerca» por una condición numérica que podamos hacer tan exigente como queramos.

### De la cercanía a una tolerancia

Sean $a_n$ un término de la sucesión y $L\in\mathbb R$ un número que queremos considerar como posible límite. La distancia entre ambos es

$$
|a_n-L|.
$$

Si elegimos una tolerancia $\varepsilon>0$, la condición

$$
|a_n-L|<\varepsilon
$$

significa que $a_n$ está a distancia menor que $\varepsilon$ de $L$.

Por las equivalencias de valor absoluto estudiadas en `T1-C02`, esto es lo mismo que

$$
L-\varepsilon<a_n<L+\varepsilon.
$$

Así, exigir

$$
|a_n-L|<\varepsilon
$$

significa pedir que el término $a_n$ pertenezca al intervalo abierto

$$
(L-\varepsilon,L+\varepsilon).
$$

Si $\varepsilon=1$, permitimos una franja bastante amplia alrededor de $L$. Si $\varepsilon=10^{-3}$, exigimos mucha más precisión. Si $\varepsilon=10^{-20}$, la exigencia es todavía más estricta.

Pero ninguna tolerancia positiva particular puede definir por sí sola el límite. Una sucesión podría terminar entrando en el intervalo de radio $1$ alrededor de $L$ y, sin embargo, permanecer siempre a distancia mayor que $10^{-3}$ de $L$.

Por eso la idea de límite no es

> los términos terminan estando cerca de $L$ con alguna precisión fija,

sino

> **cualquiera que sea la precisión positiva que exijamos**, llega un momento a partir del cual todos los términos satisfacen esa precisión.

La expresión «tan cerca como queramos» se convierte así en

$$
\forall\varepsilon>0.
$$

Y la expresión «desde algún momento y para siempre después» ya fue preparada en §3.1:

$$
\exists N\;\forall n\ge N.
$$

Al unir ambas estructuras aparece la definición fundamental.

::: {#def-t1-0028}
**Convergencia, límite y divergencia.** Sea

$$
(a_n)_{n\ge n_0}
$$

una sucesión real y sea $L\in\mathbb R$.

Diremos que $(a_n)$ **converge a $L$** si para todo $\varepsilon>0$ existe un índice $N\ge n_0$ tal que

$$
|a_n-L|<\varepsilon
$$

para todo $n\ge N$.

En símbolos,

$$
\forall\varepsilon>0\;\exists N\ge n_0\;\forall n\ge N:
|a_n-L|<\varepsilon.
$$

En ese caso escribimos

$$
a_n\to L,
$$

$$
\lim_{n\to\infty}a_n=L,
$$

o, cuando no haya ambigüedad,

$$
(a_n)\to L.
$$

El número $L$ se llama **límite** de la sucesión.

Diremos que $(a_n)$ **diverge** si no existe ningún número real $L$ al cual converja.
:::

La notación

$$
n\to\infty
$$

no significa que $n$ llegue a tomar como valor un objeto llamado $\infty$. El símbolo expresa que estamos estudiando índices arbitrariamente grandes, es decir, colas cada vez más alejadas del comienzo de la sucesión.

### Leer la definición de izquierda a derecha

La definición contiene tres cuantificadores encadenados:

$$
\boxed{
\forall\varepsilon>0
\quad
\exists N\ge n_0
\quad
\forall n\ge N.
}
$$

Su orden es parte esencial del significado.

Podemos leerla como un juego de responsabilidades.

1. **La exigencia:** se nos entrega una tolerancia arbitraria $\varepsilon>0$.
2. **Nuestra respuesta:** debemos encontrar un umbral $N$ que funcione para esa tolerancia.
3. **La verificación:** una vez elegido $N$, cualquier índice $n\ge N$ debe satisfacer
   $$
   |a_n-L|<\varepsilon.
   $$

El primer cuantificador es universal. No podemos elegir una tolerancia cómoda y detenernos allí. La afirmación debe funcionar para

$$
\varepsilon=1,
\qquad
\varepsilon=10^{-2},
\qquad
\varepsilon=10^{-100},
$$

y para cualquier otro real positivo.

El segundo cuantificador es existencial. No necesitamos encontrar el menor $N$ posible. Basta producir **algún** umbral que funcione.

El tercer cuantificador vuelve a ser universal. Después de $N$ no basta con encontrar muchos términos buenos: deben ser buenos **todos** los términos de la cola.

Esta última condición es precisamente la noción de eventualidad de §3.1. Para cada tolerancia $\varepsilon>0$, la propiedad

$$
|a_n-L|<\varepsilon
$$

debe cumplirse eventualmente.

Por eso podemos resumir la definición diciendo:

$$
\boxed{
 a_n\to L
 \quad\Longleftrightarrow\quad
 \text{para toda tolerancia positiva, la sucesión está eventualmente dentro de esa tolerancia alrededor de $L$.}
}
$$

### El umbral puede depender de la tolerancia

Una de las primeras dificultades lógicas consiste en entender la dependencia entre $\varepsilon$ y $N$.

La definición permite que

$$
N=N(\varepsilon).
$$

Una tolerancia amplia puede admitir un umbral pequeño; una tolerancia más estricta puede obligarnos a avanzar mucho más.

Por ejemplo, para

$$
a_n=\frac1{n+1}
$$

y candidato $L=0$, la condición

$$
|a_n-0|<\frac1{10}
$$

se cumple desde $n=10$.

En cambio,

$$
|a_n-0|<\frac1{10^6}
$$

requiere un umbral mucho más lejano.

No hay ningún problema en que los dos valores de $N$ sean distintos. La definición no exige un único $N$ capaz de responder simultáneamente a todas las tolerancias.

De hecho, si exigiéramos

$$
\exists N\;\forall\varepsilon>0\;\forall n\ge N:
|a_n-L|<\varepsilon,
$$

estaríamos diciendo algo mucho más fuerte. Para un $n\ge N$ fijo, el número $|a_n-L|$ tendría que ser menor que **todo** real positivo. Eso solo es posible si

$$
|a_n-L|=0,
$$

es decir,

$$
a_n=L.
$$

Por tanto, ese orden incorrecto de cuantificadores describiría sucesiones que a partir de cierto índice son exactamente constantes iguales a $L$. La convergencia es mucho más flexible: permite que los términos nunca lleguen a ser exactamente $L$, siempre que podamos hacer su distancia a $L$ arbitrariamente pequeña en una cola adecuada.

### Cómo se construye una prueba $\varepsilon$–$N$

La primera vez que vemos una prueba de convergencia puede parecer que el valor de $N$ aparece por inspiración. En realidad, conviene separar dos momentos.

**Búsqueda.** Partimos de la desigualdad que queremos conseguir,

$$
|a_n-L|<\varepsilon,
$$

y la manipulamos para descubrir qué condición sobre $n$ bastaría para garantizarla.

**Demostración.** Después escribimos el argumento en el orden lógico de la definición:

1. sea $\varepsilon>0$ arbitrario;
2. elegimos un $N$ que satisfaga la condición descubierta;
3. tomamos cualquier $n\ge N$;
4. verificamos que $|a_n-L|<\varepsilon$.

El cálculo exploratorio puede ir «hacia atrás»; la prueba final debe ir «hacia adelante».

::: {#exm-t1-0032}
**Primera prueba completa: $1/(n+1)\to0$.** Consideremos

$$
a_n=\frac1{n+1},
\qquad n\ge0.
$$

Queremos demostrar directamente desde la definición que

$$
\lim_{n\to\infty}\frac1{n+1}=0.
$$

**Búsqueda del umbral.** Necesitamos lograr

$$
\left|\frac1{n+1}-0\right|<\varepsilon.
$$

Como $n+1>0$, esto equivale a pedir

$$
\frac1{n+1}<\varepsilon,
$$

y sería suficiente garantizar

$$
n+1>\frac1\varepsilon.
$$

La propiedad arquimediana demostrada en `T1-C02` asegura que existe un número natural $N$ tal que

$$
N>\frac1\varepsilon.
$$

Ese $N$ será una respuesta válida.

**Demostración.** Sea $\varepsilon>0$. Por la propiedad arquimediana, elegimos $N\in\mathbb N$ tal que

$$
N>\frac1\varepsilon.
$$

Si $n\ge N$, entonces

$$
n+1\ge N+1>N>\frac1\varepsilon.
$$

Como todas estas cantidades son positivas, al tomar recíprocos se invierte la desigualdad y obtenemos

$$
\frac1{n+1}<\varepsilon.
$$

Por tanto,

$$
\left|\frac1{n+1}-0\right|<\varepsilon
$$

para todo $n\ge N$. Como $\varepsilon>0$ era arbitrario, concluimos que

$$
\frac1{n+1}\to0.
$$
:::

Vale la pena leer la prueba señalando dónde aparece cada cuantificador:

- **para todo** $\varepsilon>0$: comenzamos con una tolerancia arbitraria;
- **existe** $N$: la propiedad arquimediana nos permite construir una respuesta;
- **para todo** $n\ge N$: la última cadena de desigualdades funciona para cualquier término de la cola.

El argumento no demuestra que algunos términos estén cerca de cero. Demuestra que, dada cualquier precisión positiva, existe una cola completa dentro de esa precisión.

### Un mismo umbral no tiene que ser óptimo

En el ejemplo anterior elegimos $N$ satisfaciendo

$$
N>\frac1\varepsilon.
$$

Esta elección es deliberadamente cómoda y puede estar lejos de ser mínima.

La definición de convergencia no pregunta

> ¿cuál es el primer índice exacto a partir del cual funciona la desigualdad?,

sino

> ¿existe algún índice a partir del cual funciona para todos los términos posteriores?

Esta diferencia libera muchas pruebas de cálculos innecesarios. Un $N$ más grande de lo imprescindible sigue siendo perfectamente válido.

### Estar cerca muchas veces no es converger

La sucesión

$$
a_n=(-1)^n
$$

toma los valores

$$
1,-1,1,-1,1,-1,\dots
$$

Si proponemos $L=1$, hay infinitos términos que están exactamente en $1$: todos los índices pares satisfacen

$$
a_n=1.
$$

Sin embargo, eso no implica convergencia a $1$. Después de cualquier índice vuelven a aparecer términos iguales a $-1$.

La definición no pide

> para toda tolerancia existen términos arbitrariamente tardíos que están cerca de $L$,

sino

> para toda tolerancia existe un momento después del cual **todos** los términos están cerca de $L$.

En símbolos, no debemos confundir

$$
\forall N\;\exists n\ge N
$$

con

$$
\exists N\;\forall n\ge N.
$$

La primera estructura expresa que algo vuelve a ocurrir por lejos que avancemos. La segunda expresa que, desde cierto punto, algo ocurre sin excepciones. Para la convergencia necesitamos la segunda.

### Negar correctamente que $a_n\to L$

La definición de convergencia a un candidato $L$ es

$$
\forall\varepsilon>0\;\exists N\ge n_0\;\forall n\ge N:
|a_n-L|<\varepsilon.
$$

Para negarla debemos invertir los cuantificadores y negar la desigualdad final. Obtenemos:

$$
\boxed{
 a_n\not\to L
 \quad\Longleftrightarrow\quad
 \exists\varepsilon_0>0\;\forall N\ge n_0\;\exists n\ge N:
 |a_n-L|\ge\varepsilon_0.
}
$$

Esta fórmula merece una lectura pausada.

Para demostrar que $L$ **no** es el límite, no tenemos que fracasar ante todas las tolerancias. Basta encontrar **una** tolerancia positiva $\varepsilon_0$ que la sucesión sea incapaz de satisfacer eventualmente.

Una vez fijada esa tolerancia, debemos demostrar que ningún umbral funciona: por lejos que alguien coloque $N$, todavía podemos encontrar algún término posterior que queda a distancia al menos $\varepsilon_0$ de $L$.

La negación tiene así la forma de un obstáculo persistente:

$$
\boxed{
\text{existe una precisión fija que la sucesión vuelve a violar arbitrariamente lejos.}
}
$$

### Refutar un candidato no basta para demostrar divergencia

Hay que distinguir dos afirmaciones:

$$
a_n\not\to L
$$

y

$$
(a_n)\text{ diverge}.
$$

La primera excluye **un** candidato concreto. La segunda afirma que **ningún** real sirve como límite.

Por ejemplo,

$$
\frac1{n+1}\not\to1,
$$

pero eso no vuelve divergente a la sucesión: acabamos de demostrar que converge a $0$.

Como divergencia significa ausencia de todo límite real, su forma lógica completa es

$$
\forall L\in\mathbb R\;\exists\varepsilon_0>0\;\forall N\ge n_0\;\exists n\ge N:
|a_n-L|\ge\varepsilon_0.
$$

En muchas situaciones posteriores dispondremos de criterios más económicos para demostrar divergencia. Por ahora podemos hacerlo directamente desde esta negación.

::: {#exm-t1-0033}
**Divergencia de $(-1)^n$ desde la definición.** Sea

$$
a_n=(-1)^n.
$$

Demostraremos que la sucesión no converge a ningún número real.

Sea $L\in\mathbb R$ un candidato arbitrario. Los dos posibles valores de la sucesión son $1$ y $-1$. Por la desigualdad triangular,

$$
2
=|1-(-1)|
\le |1-L|+|L-(-1)|
=|1-L|+|-1-L|.
$$

Por tanto, al menos uno de los dos números

$$
|1-L|,
\qquad
|-1-L|
$$

es mayor o igual que $1$.

Tomemos

$$
\varepsilon_0=1.
$$

Ahora sea $N\in\mathbb N$ cualquier umbral.

- Si $|1-L|\ge1$, elegimos un índice par $n\ge N$, por ejemplo $n=2N$. Entonces $a_n=1$ y
  $$
  |a_n-L|=|1-L|\ge1=\varepsilon_0.
  $$
- Si $|-1-L|\ge1$, elegimos un índice impar $n\ge N$, por ejemplo $n=2N+1$. Entonces $a_n=-1$ y
  $$
  |a_n-L|=|-1-L|\ge1=\varepsilon_0.
  $$

En cualquiera de los dos casos, para todo $N$ encontramos un $n\ge N$ tal que

$$
|a_n-L|\ge\varepsilon_0.
$$

Así, $a_n\not\to L$.

Como $L\in\mathbb R$ era arbitrario, ningún real puede ser límite de la sucesión. Por consiguiente,

$$
((-1)^n)\text{ diverge}.
$$
:::

Observe qué hizo posible la prueba: no necesitamos adivinar cuál sería el «verdadero» candidato. Elegimos un $L$ completamente arbitrario y demostramos que la oscilación entre $1$ y $-1$ impide que toda una cola quede dentro de una tolerancia suficientemente estrecha alrededor de ese $L$.

### Una definición que ya contiene un método de trabajo

La definición $\varepsilon$–$N$ no es solamente una frase que debamos memorizar. También prescribe la arquitectura de las primeras demostraciones.

Para **probar convergencia hacia un candidato $L$**:

$$
\boxed{
\varepsilon>0
\longrightarrow
\text{buscar una condición suficiente sobre }n
\longrightarrow
\text{elegir }N(\varepsilon)
\longrightarrow
\forall n\ge N:\ |a_n-L|<\varepsilon.
}
$$

Para **refutar que $L$ sea límite**:

$$
\boxed{
\text{elegir }\varepsilon_0>0
\longrightarrow
\forall N
\longrightarrow
\text{encontrar }n\ge N
\text{ con }
|a_n-L|\ge\varepsilon_0.
}
$$

Estas dos arquitecturas son lógicamente opuestas. Aprender a reconocerlas será tan importante como aprender a calcular límites.

En esta sección hemos definido qué significa converger, pero todavía no hemos estudiado qué consecuencias tiene hacerlo. Por ejemplo:

- ¿podría una misma sucesión converger a dos números distintos?;
- ¿puede una sucesión convergente escapar arbitrariamente lejos de todos los números?;
- ¿qué ocurre si modificamos una cantidad finita de términos de una sucesión convergente?

Las respuestas pertenecen a §3.3. Allí comenzaremos a demostrar los primeros teoremas generales que se desprenden únicamente de la definición que acabamos de construir.

## Qué fuerza tiene converger: unicidad, colas y acotación {#sec-t1-c04-03}

La definición $\varepsilon$–$N$ parece, a primera vista, exigir únicamente que una sucesión se acerque a cierto número. Sin embargo, esa exigencia tiene consecuencias mucho más fuertes de lo que sugiere la intuición inicial.

En esta sección responderemos tres preguntas.

1. Si una sucesión converge, ¿puede tener dos límites distintos?
2. Si alteramos solamente una cantidad finita de términos, ¿podemos cambiar su convergencia?
3. ¿Puede una sucesión convergente tener términos de tamaño arbitrariamente grande?

Las respuestas serán, respectivamente,

$$
\boxed{
\text{no},\qquad
\text{no},\qquad
\text{no}.
}
$$

Lo importante no será solo conocer estas conclusiones. Cada prueba revelará un patrón de razonamiento que reutilizaremos durante todo el cálculo.

### Una sucesión no puede acercarse indefinidamente a dos números distintos

Supongamos que una sucesión $(a_n)$ convergiera a dos números reales $L$ y $M$.

Si $L\ne M$, existe una distancia positiva entre ellos:

$$
|L-M|>0.
$$

La definición de convergencia permitiría entonces exigir simultáneamente que, a partir de cierto momento, los términos de la sucesión estén muy cerca de $L$ y muy cerca de $M$.

Pero dos entornos suficientemente pequeños alrededor de puntos distintos no pueden compartir un mismo punto.

Esta observación geométrica se convertirá en una contradicción mediante la desigualdad triangular.

::: {#thm-t1-0009}
**Unicidad del límite secuencial.** Sea $(a_n)_{n\ge n_0}$ una sucesión real. Si

$$
a_n\to L
$$

y también

$$
a_n\to M,
$$

entonces

$$
L=M.
$$

**Demostración.** Supongamos, buscando una contradicción, que

$$
L\ne M.
$$

Entonces

$$
d:=|L-M|>0.
$$

Elegimos la tolerancia

$$
\varepsilon=\frac d3.
$$

Como $a_n\to L$, existe un índice $N_L\ge n_0$ tal que, para todo $n\ge N_L$,

$$
|a_n-L|<\frac d3.
$$

Como también $a_n\to M$, existe un índice $N_M\ge n_0$ tal que, para todo $n\ge N_M$,

$$
|a_n-M|<\frac d3.
$$

Tomemos

$$
N=\max\{N_L,N_M\}.
$$

Entonces, para todo $n\ge N$, ambas desigualdades se cumplen simultáneamente. Fijemos uno de esos índices. Por la desigualdad triangular,

$$
|L-M|
\le |L-a_n|+|a_n-M|.
$$

Por las estimaciones anteriores,

$$
|L-M|
<\frac d3+\frac d3
=\frac{2d}{3}.
$$

Pero $|L-M|=d$, de modo que obtenemos

$$
d<\frac{2d}{3},
$$

lo cual es imposible porque $d>0$.

Por tanto, la suposición $L\ne M$ era falsa y necesariamente

$$
L=M.
$$
:::

La prueba merece ser leída por su arquitectura, no solo por su resultado.

**Objetivo.** Queríamos demostrar que dos supuestos límites debían coincidir.

**Estrategia.** Supusimos que eran distintos y convertimos su distancia positiva en una tolerancia.

**Paso decisivo.** La convergencia a $L$ y a $M$ produce dos umbrales distintos. El máximo

$$
N=\max\{N_L,N_M\}
$$

permite entrar simultáneamente en ambas colas.

**Contradicción.** Un mismo término $a_n$ no puede estar a menos de $d/3$ de ambos extremos de un segmento cuya longitud es $d$.

Podríamos haber usado, por ejemplo, $\varepsilon=d/4$. Lo esencial es elegir una tolerancia tal que dos errores sumados sigan siendo estrictamente menores que $d$.

La elección

$$
\varepsilon=\frac d2
$$

sería menos conveniente para esta prueba tal como está escrita: produciría solamente

$$
|L-M|<\frac d2+\frac d2=d,
$$

que sigue siendo una contradicción porque las desigualdades son estrictas, pero deja el argumento exactamente en la frontera. Elegir $d/3$ hace visible un margen positivo y prepara un hábito útil: cuando una desigualdad triangular divide un error entre varias partes, conviene reservar espacio suficiente para todas ellas.

A partir de ahora, gracias a la unicidad, tiene sentido escribir

$$
\lim_{n\to\infty}a_n=L
$$

sin ambigüedad: si el límite real existe, hay uno solo.

### La convergencia pertenece a la cola

En §3.1 vimos que una propiedad eventual no depende de un prefijo finito. La convergencia está formulada precisamente mediante propiedades eventuales:

$$
\forall\varepsilon>0\;\exists N\;\forall n\ge N:
|a_n-L|<\varepsilon.
$$

Por eso modificar algunos términos iniciales no puede destruir una convergencia ya existente ni fabricar un límite diferente.

Conviene formular esta estabilidad de manera algo más general.

::: {#prp-t1-0019}
**Coincidencia eventual y estabilidad de la convergencia.** Sean $(a_n)$ y $(b_n)$ dos sucesiones reales definidas, al menos, a partir de algún índice común $n_0$. Supongamos que coinciden eventualmente; es decir, existe $K\ge n_0$ tal que

$$
a_n=b_n
\qquad
\text{para todo }n\ge K.
$$

Entonces, para todo $L\in\mathbb R$,

$$
a_n\to L
\quad\Longleftrightarrow\quad
b_n\to L.
$$

En particular, cambiar una cantidad finita de términos de una sucesión no modifica su convergencia ni su límite.

**Demostración.** Supongamos primero que

$$
a_n\to L.
$$

Sea $\varepsilon>0$. Por convergencia existe $N_a\ge n_0$ tal que

$$
n\ge N_a
\quad\Longrightarrow\quad
|a_n-L|<\varepsilon.
$$

Definimos

$$
N=\max\{N_a,K\}.
$$

Si $n\ge N$, entonces simultáneamente

$$
n\ge N_a
$$

y

$$
n\ge K.
$$

La primera desigualdad da

$$
|a_n-L|<\varepsilon,
$$

y la segunda garantiza que

$$
b_n=a_n.
$$

Por tanto,

$$
|b_n-L|
=|a_n-L|
<\varepsilon.
$$

Hemos demostrado que $b_n\to L$.

El argumento inverso es idéntico, intercambiando los papeles de $(a_n)$ y $(b_n)$. Por consiguiente,

$$
a_n\to L
\quad\Longleftrightarrow\quad
b_n\to L.
$$
:::

El mecanismo de la prueba puede resumirse en una sola operación:

$$
\boxed{
\text{umbral de convergencia}
+
\text{umbral de coincidencia}
\longrightarrow
\max\{N_a,K\}.
}
$$

Este uso del máximo aparecerá constantemente. Siempre que varias propiedades sean verdaderas eventualmente, podemos hacerlas verdaderas **simultáneamente** avanzando hasta el mayor de sus umbrales.

#### Quitar o añadir una cantidad finita de términos

La proposición anterior tiene una consecuencia inmediata. Si

$$
a_n\to L,
$$

entonces cualquier cola

$$
(a_n)_{n\ge K}
$$

converge al mismo $L$.

Recíprocamente, si alguna cola de la sucesión converge a $L$, entonces la sucesión completa también converge a $L$: los términos anteriores a $K$ forman solo un prefijo finito y no intervienen en ninguna condición que deba cumplirse desde un umbral suficientemente tardío.

Así,

$$
\boxed{
(a_n)\text{ converge a }L
\quad\Longleftrightarrow\quad
\text{cualquier cola de }(a_n)\text{ converge a }L.
}
$$

Esta equivalencia expresa con precisión una frase que utilizaremos muchas veces:

> para estudiar un límite podemos descartar una cantidad finita de términos iniciales.

Descartar no significa borrar información del objeto original. Significa que esa información no afecta la pregunta específica de convergencia.

#### Desplazar los índices tampoco cambia el límite

Sea $r\in\mathbb N$ fijo y, para $n\ge n_0$, definamos

$$
b_n=a_{n+r}.
$$

La sucesión $(b_n)$ recorre los mismos términos que una cola de $(a_n)$, pero vuelve a numerarlos comenzando en un índice anterior.

Demostremos directamente que

$$
a_n\to L
\quad\Longleftrightarrow\quad
b_n\to L.
$$

Supongamos que $a_n\to L$ y sea $\varepsilon>0$. Existe $N$ tal que

$$
m\ge N
\quad\Longrightarrow\quad
|a_m-L|<\varepsilon.
$$

Si elegimos un índice $n$ suficientemente grande para que

$$
n+r\ge N,
$$

entonces

$$
|b_n-L|
=|a_{n+r}-L|
<\varepsilon.
$$

Por ejemplo, basta tomar

$$
N_b=\max\{n_0,N-r\}.
$$

En la dirección contraria, si $b_n\to L$, entonces existe un umbral $N_b$ después del cual

$$
|a_{n+r}-L|<\varepsilon.
$$

Para todo

$$
m\ge N_b+r,
$$

podemos escribir $m=n+r$ con $n=m-r\ge N_b$, y obtenemos

$$
|a_m-L|<\varepsilon.
$$

Por tanto, desplazar una cantidad fija de posiciones el índice tampoco altera el límite.

Este hecho será decisivo cuando estudiemos recurrencias: si

$$
a_n\to L,
$$

entonces también

$$
a_{n+1}\to L.
$$

No estamos usando continuidad ni álgebra de límites. Es una consecuencia directa de que quitar el primer término no cambia el comportamiento de la cola.

### Convergencia no significa que todos los términos estén cerca del límite

La estabilidad bajo modificaciones finitas corrige una intuición frecuente.

Una sucesión convergente puede comenzar con términos enormes o completamente irregulares. Por ejemplo, definamos

$$
a_0=10^{100},
\qquad
a_1=-10^{50},
\qquad
a_2=37,
$$

y, para $n\ge3$,

$$
a_n=\frac1{n+1}.
$$

Como la cola coincide con la sucesión ya estudiada $1/(n+1)$, tenemos

$$
a_n\to0.
$$

Los primeros términos pueden estar muy lejos de $0$ sin afectar el límite.

La convergencia no dice

$$
|a_n-L|<\varepsilon
\qquad
\text{para todo }n.
$$

Dice que, para cada tolerancia, esa desigualdad termina siendo verdadera **eventualmente**.

Esta distinción será importante en la siguiente prueba. La convergencia controlará automáticamente una cola, pero para obtener una afirmación sobre **todos** los términos deberemos tratar por separado el prefijo finito restante.

### Acotación: encerrar todos los términos en un intervalo fijo

Hasta ahora hemos utilizado cotas para conjuntos de números reales. Como una sucesión es una función, también podemos preguntar si su conjunto de valores permanece dentro de una región finita de la recta.

::: {#def-t1-0029}
**Sucesión acotada.** Sea $(a_n)_{n\ge n_0}$ una sucesión real. Diremos que $(a_n)$ es **acotada** si existe un número $M>0$ tal que

$$
|a_n|\le M
\qquad
\text{para todo }n\ge n_0.
$$

Equivalentemente, existe $M>0$ tal que todos los términos pertenecen al intervalo

$$
[-M,M].
$$
:::

La constante $M$ debe ser **una sola cota para toda la sucesión**. No sería suficiente permitir una cota distinta para cada término: para cualquier número real $a_n$ podríamos elegir trivialmente $M_n=|a_n|+1$, y esa condición no expresaría ningún control global.

En lenguaje de funciones, la definición equivale a afirmar que la imagen

$$
\{a_n:n\ge n_0\}
$$

es un subconjunto acotado de $\mathbb R$.

También podemos separar cotas superiores e inferiores. Una sucesión es acotada si existen números $m,M\in\mathbb R$ tales que

$$
m\le a_n\le M
\qquad
\text{para todo }n\ge n_0.
$$

La forma simétrica

$$
|a_n|\le C
$$

es especialmente cómoda porque reúne ambas desigualdades en una sola expresión.

### Toda sucesión convergente es acotada

La definición de convergencia ya contiene casi toda la prueba.

Si

$$
a_n\to L,
$$

podemos escoger una tolerancia concreta, por ejemplo

$$
\varepsilon=1.
$$

Entonces, desde algún índice $N$,

$$
|a_n-L|<1.
$$

La desigualdad triangular da

$$
|a_n|
\le |a_n-L|+|L|
<1+|L|.
$$

Así, toda la cola está acotada por $|L|+1$.

Pero la definición de sucesión acotada exige controlar **todos** los términos, incluidos los anteriores a $N$. Aquí aparece el segundo ingrediente: antes de $N$ solo hay una cantidad finita de términos, y una cantidad finita de números reales siempre admite un máximo de sus valores absolutos.

::: {#prp-t1-0020}
**Toda sucesión convergente es acotada.** Si

$$
a_n\to L,
$$

entonces la sucesión $(a_n)$ es acotada.

**Demostración.** Como $a_n\to L$, podemos aplicar la definición con la tolerancia

$$
\varepsilon=1.
$$

Existe entonces un índice $N_0\ge n_0$ tal que

$$
n\ge N_0
\quad\Longrightarrow\quad
|a_n-L|<1.
$$

Si fuera necesario, reemplazamos $N_0$ por

$$
N=\max\{N_0,n_0+1\}.
$$

La propiedad anterior sigue siendo válida para $n\ge N$, y ahora existe al menos un término en el prefijo que va desde $n_0$ hasta $N-1$.

Para todo $n\ge N$, por la desigualdad triangular,

$$
|a_n|
\le |a_n-L|+|L|
<1+|L|.
$$

Por otra parte, los términos

$$
a_{n_0},a_{n_0+1},\dots,a_{N-1}
$$

son finitos en número. Por tanto existe el máximo

$$
M_0
=
\max\{|a_{n_0}|,|a_{n_0+1}|,\dots,|a_{N-1}|\}.
$$

Definamos

$$
M=\max\{M_0,|L|+1\}.
$$

Entonces $M>0$ y controla ambas regiones:

- si $n_0\le n<N$, tenemos $|a_n|\le M_0\le M$;
- si $n\ge N$, tenemos $|a_n|<|L|+1\le M$.

En consecuencia,

$$
|a_n|\le M
\qquad
\text{para todo }n\ge n_0.
$$

Por definición, $(a_n)$ es acotada.
:::

Esta demostración contiene un patrón que conviene conservar:

$$
\boxed{
\text{controlar la cola}
+
\text{controlar el prefijo finito}
\longrightarrow
\text{control global}.
}
$$

La convergencia proporciona el primer control. La finitud del prefijo proporciona el segundo.

Observe también que no necesitábamos la definición completa para **todas** las tolerancias. Para demostrar acotación bastó utilizar una sola, $\varepsilon=1$. Una definición universal puede tener consecuencias que se obtienen seleccionando estratégicamente un caso particular.

### Qué hipótesis usamos realmente en la prueba de acotación

Es útil auditar el argumento.

1. **Convergencia.** Se usó para encontrar una cola dentro de distancia $1$ de $L$.
2. **Desigualdad triangular.** Transformó una cota sobre $|a_n-L|$ en una cota sobre $|a_n|$.
3. **Finitud del prefijo.** Permitió tomar el máximo de los términos no controlados por la cola.

No se utilizó completitud, monotonía, álgebra de límites ni ningún teorema posterior.

La prueba es, por tanto, una consecuencia muy temprana y directa de la definición $\varepsilon$–$N$.

### La recíproca es falsa

Acabamos de demostrar

$$
\boxed{
\text{convergente}\Longrightarrow\text{acotada}.
}
$$

No debemos invertir automáticamente la implicación.

La sucesión

$$
a_n=(-1)^n
$$

satisface

$$
|a_n|=1
$$

para todo $n$. Por tanto es acotada, con $M=1$.

Sin embargo, en §3.2 demostramos directamente que diverge.

Así,

$$
\boxed{
\text{acotada}\centernot\Longrightarrow\text{convergente}.
}
$$

Esta separación será fundamental más adelante. La acotación impide que los términos escapen indefinidamente en tamaño, pero no impide que sigan oscilando entre regiones distintas.

### Convergencia tampoco significa monotonía

Otra confusión frecuente consiste en imaginar una sucesión convergente como una lista de términos que se aproxima al límite siempre desde el mismo lado y en una sola dirección.

La definición no exige nada semejante.

::: {#exm-t1-0034}
**Dos separaciones esenciales: convergencia sin monotonía y acotación sin convergencia.**

Consideremos primero

$$
a_n=\frac{(-1)^n}{n+1}.
$$

Para todo $n$,

$$
|a_n-0|
=\frac1{n+1}.
$$

Dado $\varepsilon>0$, en §3.2 ya construimos un umbral $N$ tal que

$$
n\ge N
\quad\Longrightarrow\quad
\frac1{n+1}<\varepsilon.
$$

El mismo umbral produce

$$
|a_n|<\varepsilon.
$$

Por tanto,

$$
\frac{(-1)^n}{n+1}\to0.
$$

Pero la sucesión no es creciente ni decreciente. Sus tres primeros términos son

$$
1,-\frac12,\frac13,
$$

de modo que

$$
a_0>a_1
$$

y también

$$
a_1<a_2.
$$

Una sucesión creciente no podría presentar la primera desigualdad, y una decreciente no podría presentar la segunda. Así, $(a_n)$ converge pero no es monótona.

Consideremos ahora

$$
b_n=(-1)^n.
$$

Como

$$
|b_n|=1
$$

para todo $n$, la sucesión es acotada. Sin embargo, @exm-t1-0033 demostró que no converge a ningún número real.

Tenemos entonces dos contraejemplos complementarios:

$$
\boxed{
\text{convergente}\centernot\Longrightarrow\text{monótona},
}
$$

$$
\boxed{
\text{acotada}\centernot\Longrightarrow\text{convergente}.
}
$$
:::

Estos ejemplos muestran que conviene mantener separadas tres propiedades:

- **convergencia:** toda cola suficientemente tardía queda dentro de cualquier tolerancia alrededor de un único $L$;
- **acotación:** todos los términos permanecen dentro de algún intervalo fijo;
- **monotonía:** los términos respetan sistemáticamente un sentido de orden entre índices consecutivos o cualesquiera índices ordenados.

Ninguna de estas frases es sinónimo de las otras.

Más adelante aparecerá una interacción mucho más profunda: una sucesión **monótona y acotada** sí tendrá que converger. Esa afirmación requerirá la completitud de $\mathbb R$ y será uno de los resultados centrales del capítulo. Todavía no podemos usarla.

### Una primera red de implicaciones

Con los resultados disponibles hasta ahora podemos escribir:

$$
\boxed{
\begin{array}{c}
 a_n\to L\\[2pt]
 \Downarrow\\[2pt]
 \text{límite único}\quad+\quad\text{acotación}\quad+\quad\text{estabilidad de colas}
\end{array}
}
$$

Pero no podemos añadir las flechas recíprocas sin hipótesis adicionales.

En particular:

$$
\text{acotada}\centernot\Longrightarrow\text{convergente},
$$

$$
\text{convergente}\centernot\Longrightarrow\text{monótona}.
$$

Y la unicidad no afirma existencia: decir que **si** existe un límite entonces es único no demuestra que una sucesión dada converja.

Esta distinción entre existencia y unicidad es la misma que empleamos al demostrar la unicidad de inversos y la existencia de raíces en el capítulo inicial. El @thm-t1-0009 resuelve solamente la parte de «a lo sumo uno». Para establecer que una sucesión concreta tiene límite todavía necesitamos demostrar existencia mediante la definición o mediante resultados que construiremos después.

### Qué hemos ganado

La definición de §3.2 ya no es una pieza aislada. Ha producido tres herramientas generales:

1. **Unicidad:** si una sucesión converge, no hay ambigüedad acerca de su límite.
2. **Estabilidad de cola:** eliminar, añadir o modificar finitos términos no afecta el límite; desplazar el índice una cantidad fija tampoco.
3. **Acotación:** toda sucesión convergente permanece globalmente dentro de algún intervalo finito.

Estas propiedades permitirán que, a partir de la próxima sección, dejemos de volver a la definición $\varepsilon$–$N$ para cada cálculo elemental.

El siguiente problema será demostrar que las operaciones algebraicas respetan los límites. Si

$$
a_n\to A
$$

y

$$
b_n\to B,
$$

¿podemos concluir que

$$
a_n+b_n\to A+B,
$$

$$
a_nb_n\to AB,
$$

o que

$$
\frac{a_n}{b_n}\to\frac AB?
$$

La respuesta será afirmativa bajo las hipótesis adecuadas, pero la prueba del producto revelará por qué la acotación que acabamos de establecer no era un resultado accesorio: será exactamente la herramienta necesaria para controlar un factor variable.

## El álgebra de límites: cuándo podemos calcular sin volver a $\varepsilon$ {#sec-t1-c04-04}

Hasta ahora, cada vez que quisimos demostrar un límite tuvimos que regresar a la definición

$$
\forall\varepsilon>0\;\exists N\;\forall n\ge N:
|a_n-L|<\varepsilon.
$$

Ese trabajo era necesario. Antes de utilizar reglas de cálculo debíamos demostrar que esas reglas son compatibles con la noción rigurosa de convergencia que acabamos de construir.

La pregunta de esta sección es la siguiente:

$$
\boxed{
\text{si conocemos los límites de dos sucesiones, ¿qué ocurre al sumarlas, multiplicarlas o dividirlas?}
}
$$

Las respuestas serán las que sugiere el álgebra ordinaria, pero no las aceptaremos por analogía. Las deduciremos de la definición $\varepsilon$–$N$.

El premio por hacer ese trabajo una vez será considerable: después podremos calcular muchos límites sin reconstruir desde cero una prueba con tolerancias.

### Las reglas algebraicas son teoremas, no convenciones

Supongamos que

$$
a_n\to A
$$

y

$$
b_n\to B.
$$

Es natural esperar

$$
a_n+b_n\to A+B,
$$

$$
a_nb_n\to AB,
$$

y, cuando el denominador no plantee problemas,

$$
\frac{a_n}{b_n}\to\frac AB.
$$

Pero cada una de estas afirmaciones contiene una dificultad distinta.

Para la suma, la distancia al límite esperado se separa inmediatamente:

$$
\begin{aligned}
|(a_n+b_n)-(A+B)|
&=|(a_n-A)+(b_n-B)|\\
&\le |a_n-A|+|b_n-B|.
\end{aligned}
$$

Así, podemos repartir la tolerancia entre dos errores que ya sabemos controlar.

Para el producto aparece algo nuevo. La identidad útil es

$$
\begin{aligned}
a_nb_n-AB
&=a_nb_n-Ab_n+Ab_n-AB\\
&=b_n(a_n-A)+A(b_n-B).
\end{aligned}
$$

Por tanto,

$$
|a_nb_n-AB|
\le
|b_n|\,|a_n-A|+|A|\,|b_n-B|.
$$

El segundo término contiene una constante $|A|$, pero el primero contiene el factor variable $|b_n|$. Saber únicamente que $|a_n-A|$ puede hacerse pequeño no basta si no controlamos cuánto puede valer $|b_n|$.

Aquí reaparece exactamente el resultado de §3.3:

> toda sucesión convergente es acotada.

La acotación permitirá reemplazar el factor variable $|b_n|$ por una constante fija.

El cociente contiene una dificultad diferente: aunque $B\ne0$, necesitamos asegurar que los términos $b_n$ tampoco se acerquen peligrosamente a cero cuando $n$ sea grande.

Estas tres ideas —**repartir el error**, **acotar factores variables** y **separar denominadores de cero**— constituyen la ingeniería de las leyes algebraicas del límite.

::: {#prp-t1-0021}
**Álgebra de límites secuenciales.** Sean $(a_n)$ y $(b_n)$ sucesiones reales tales que

$$
a_n\to A
\qquad\text{y}\qquad
b_n\to B.
$$

Entonces:

1. para todo $c\in\mathbb R$,
   $$
   ca_n\to cA;
   $$
2. 
   $$
   a_n+b_n\to A+B;
   $$
3. 
   $$
   a_nb_n\to AB;
   $$
4. si $B\ne0$, entonces existe una cola en la que $b_n\ne0$ y, sobre esa cola,
   $$
   \frac{a_n}{b_n}\to\frac AB.
   $$

En particular, usando $c=-1$, también

$$
a_n-b_n\to A-B.
$$

**Demostración.** Demostraremos cada afirmación directamente desde la definición de convergencia.

**1. Multiplicación por una constante.** Si $c=0$, entonces $ca_n=0$ para todo $n$, y la sucesión constante nula converge a $0=cA$.

Supongamos ahora $c\ne0$. Sea $\varepsilon>0$. Como $a_n\to A$, existe $N$ tal que

$$
n\ge N
\quad\Longrightarrow\quad
|a_n-A|<\frac{\varepsilon}{|c|}.
$$

Entonces, para todo $n\ge N$,

$$
|ca_n-cA|
=|c|\,|a_n-A|
<|c|\frac{\varepsilon}{|c|}
=\varepsilon.
$$

Por tanto,

$$
ca_n\to cA.
$$

**2. Suma.** Sea $\varepsilon>0$. Como $a_n\to A$, existe $N_1$ tal que

$$
n\ge N_1
\quad\Longrightarrow\quad
|a_n-A|<\frac\varepsilon2.
$$

Como $b_n\to B$, existe $N_2$ tal que

$$
n\ge N_2
\quad\Longrightarrow\quad
|b_n-B|<\frac\varepsilon2.
$$

Tomemos

$$
N=\max\{N_1,N_2\}.
$$

Si $n\ge N$, ambas estimaciones son válidas simultáneamente y, por la desigualdad triangular,

$$
\begin{aligned}
|(a_n+b_n)-(A+B)|
&\le |a_n-A|+|b_n-B|\\
&<\frac\varepsilon2+\frac\varepsilon2\\
&=\varepsilon.
\end{aligned}
$$

Luego

$$
a_n+b_n\to A+B.
$$

**3. Producto.** Esta es la parte delicada. Por @prp-t1-0020, la sucesión convergente $(b_n)$ es acotada. Por tanto existe $M>0$ tal que

$$
|b_n|\le M
$$

para todo índice de la sucesión.

Sea $\varepsilon>0$. Como $a_n\to A$, existe $N_1$ tal que

$$
n\ge N_1
\quad\Longrightarrow\quad
|a_n-A|<\frac{\varepsilon}{2M}.
$$

Como $b_n\to B$, existe $N_2$ tal que

$$
n\ge N_2
\quad\Longrightarrow\quad
|b_n-B|<\frac{\varepsilon}{2(|A|+1)}.
$$

Elegimos

$$
N=\max\{N_1,N_2\}.
$$

Para todo $n\ge N$,

$$
\begin{aligned}
|a_nb_n-AB|
&=|b_n(a_n-A)+A(b_n-B)|\\
&\le |b_n|\,|a_n-A|+|A|\,|b_n-B|\\
&\le M|a_n-A|+|A|\,|b_n-B|\\
&<M\frac{\varepsilon}{2M}
+|A|\frac{\varepsilon}{2(|A|+1)}\\
&<\frac\varepsilon2+\frac\varepsilon2\\
&=\varepsilon.
\end{aligned}
$$

Por consiguiente,

$$
a_nb_n\to AB.
$$

**4. Cociente.** Supongamos $B\ne0$. Antes de estudiar $a_n/b_n$ debemos demostrar que el denominador no se anula en una cola.

Como $b_n\to B$, podemos aplicar la definición con la tolerancia

$$
\frac{|B|}{2}>0.
$$

Existe $N_0$ tal que

$$
n\ge N_0
\quad\Longrightarrow\quad
|b_n-B|<\frac{|B|}{2}.
$$

Por la desigualdad triangular inversa,

$$
\bigl||b_n|-|B|\bigr|
\le |b_n-B|.
$$

Así, para $n\ge N_0$,

$$
|b_n|
>|B|-\frac{|B|}{2}
=\frac{|B|}{2}>0.
$$

En particular,

$$
b_n\ne0
$$

para todo $n\ge N_0$. El cociente está, por tanto, bien definido en esa cola.

Demostremos primero que

$$
\frac1{b_n}\to\frac1B.
$$

Sea $\varepsilon>0$. Además del umbral $N_0$, como $b_n\to B$ existe $N_1$ tal que

$$
n\ge N_1
\quad\Longrightarrow\quad
|b_n-B|<\frac{\varepsilon |B|^2}{2}.
$$

Tomemos

$$
N=\max\{N_0,N_1\}.
$$

Entonces, si $n\ge N$,

$$
\begin{aligned}
\left|\frac1{b_n}-\frac1B\right|
&=\frac{|B-b_n|}{|B|\,|b_n|}\\
&\le
\frac{|B-b_n|}{|B|(|B|/2)}\\
&=\frac{2|b_n-B|}{|B|^2}\\
&<\varepsilon.
\end{aligned}
$$

Por tanto,

$$
\frac1{b_n}\to\frac1B.
$$

Finalmente,

$$
\frac{a_n}{b_n}
=a_n\frac1{b_n}
$$

para todo $n$ suficientemente grande. Aplicando la parte del producto,

$$
\frac{a_n}{b_n}\to A\frac1B=\frac AB.
$$

Esto completa la demostración.
:::

### Cómo leer la prueba del producto

La prueba anterior contiene una técnica que aparecerá muchas veces en análisis.

Nuestro objetivo era controlar

$$
|a_nb_n-AB|.
$$

La expresión no estaba inicialmente escrita en términos de los dos errores que la convergencia nos permite hacer pequeños:

$$
|a_n-A|
\qquad\text{y}\qquad
|b_n-B|.
$$

Para hacerlos aparecer introdujimos un término intermedio:

$$
a_nb_n
\longrightarrow
Ab_n
\longrightarrow
AB.
$$

Algebraicamente, esto equivale a sumar y restar $Ab_n$:

$$
a_nb_n-AB
=(a_nb_n-Ab_n)+(Ab_n-AB).
$$

Después la desigualdad triangular transformó el problema en

$$
|b_n|\,|a_n-A|+|A|\,|b_n-B|.
$$

Ahora sí aparecen los errores conocidos, pero uno viene multiplicado por $|b_n|$. La acotación de $(b_n)$ convierte ese factor variable en una constante manejable.

La cadena de ideas es, por tanto,

$$
\boxed{
\text{crear los errores conocidos}
\to
\text{usar desigualdad triangular}
\to
\text{acotar el factor variable}
\to
\text{repartir }\varepsilon.
}
$$

Esto explica por qué @prp-t1-0020 no era una propiedad decorativa. El teorema de acotación se convierte inmediatamente en una herramienta para demostrar otro teorema.

### Una observación sobre las cotas usadas en una prueba

En la demostración del producto usamos una cota global

$$
|b_n|\le M.
$$

En realidad habría bastado una **cota eventual**. Como $b_n\to B$, tomando, por ejemplo, $\varepsilon=1$ obtenemos

$$
|b_n-B|<1
$$

desde algún índice, y entonces

$$
|b_n|
\le |b_n-B|+|B|
<1+|B|.
$$

Esto controla exactamente la cola que interviene en la definición de límite.

La versión global obtenida en §3.3 es más fuerte y más cómoda, pero conviene reconocer qué parte de una hipótesis utiliza realmente una demostración.

### El denominador no nulo no puede tratarse como un detalle

La afirmación

$$
b_n\to B\ne0
$$

contiene más información que simplemente «el límite del denominador no es cero». Garantiza que los términos quedan finalmente dentro de una región que no contiene al cero.

En efecto, desde cierto índice tenemos

$$
|b_n-B|<\frac{|B|}{2},
$$

y por tanto

$$
|b_n|>\frac{|B|}{2}.
$$

Geométricamente, los términos terminan atrapados en un intervalo centrado en $B$ cuyo radio es menor que la distancia de $B$ al origen.

Este paso cumple dos funciones distintas:

1. garantiza que $1/b_n$ está definido en una cola;
2. proporciona la estimación
   $$
   \frac1{|b_n|}<\frac2{|B|},
   $$
   necesaria para controlar el error del recíproco.

No debemos escribir simplemente «como $B\ne0$, dividimos». El denominador de cada término es $b_n$, no $B$; la separación eventual de cero es el puente entre ambos hechos.

### Sucesiones constantes y diferencias

Las leyes anteriores producen inmediatamente varias herramientas básicas.

Para cualquier $c\in\mathbb R$, la sucesión constante

$$
a_n=c
$$

converge a $c$, porque

$$
|a_n-c|=0<\varepsilon
$$

para toda $\varepsilon>0$ y para todos los índices.

Además, si

$$
a_n\to A,
\qquad
b_n\to B,
$$

entonces, aplicando primero la multiplicación por $-1$ y después la suma,

$$
a_n-b_n
=a_n+(-1)b_n
\to
A-B.
$$

Estas consecuencias pequeñas permiten construir expresiones algebraicas cada vez más complejas sin regresar a la definición en cada paso.

### El valor absoluto también respeta el límite

El valor absoluto no es una operación algebraica binaria como suma o producto, pero la desigualdad triangular inversa permite controlarlo directamente.

::: {#cor-t1-0007}
**Límite del valor absoluto.** Si

$$
a_n\to A,
$$

entonces

$$
|a_n|\to|A|.
$$

**Demostración.** Para todo $n$, la desigualdad triangular inversa da

$$
\bigl||a_n|-|A|\bigr|
\le |a_n-A|.
$$

Sea $\varepsilon>0$. Como $a_n\to A$, existe $N$ tal que

$$
n\ge N
\quad\Longrightarrow\quad
|a_n-A|<\varepsilon.
$$

Para esos mismos índices,

$$
\bigl||a_n|-|A|\bigr|
\le |a_n-A|
<\varepsilon.
$$

Por definición,

$$
|a_n|\to|A|.
$$
:::

La demostración merece atención por su economía. No hemos utilizado ninguna afirmación sobre la continuidad de la función $x\mapsto|x|$. Esa teoría todavía no existe en nuestro desarrollo. Todo proviene de una desigualdad ya demostrada en `T1-C02`.

### De la prueba a la herramienta de cálculo

Una vez demostrado @prp-t1-0021, ya podemos utilizarlo como un resultado previo. Esto cambia el modo de resolver muchos problemas.

Si sabemos, por ejemplo, que

$$
a_n\to A
$$

y queremos estudiar una expresión como

$$
3a_n^2-5a_n+7,
$$

no necesitamos construir desde cero un $N(\varepsilon)$ para toda la expresión.

Podemos razonar en capas:

$$
a_n\to A,
$$

luego

$$
a_n^2=a_na_n\to A^2,
$$

entonces

$$
3a_n^2\to3A^2,
$$

$$
-5a_n\to-5A,
$$

y, sumando con la sucesión constante $7$,

$$
3a_n^2-5a_n+7
\to
3A^2-5A+7.
$$

La definición $\varepsilon$–$N$ no ha desaparecido. Está **encapsulada** dentro de los teoremas que acabamos de demostrar.

Esta es una característica fundamental del trabajo matemático: una vez justificada una herramienta, podemos reutilizarla sin repetir cada vez toda su construcción interna.

### Un cociente de polinomios en $n$

Veamos ahora cómo estas leyes convierten un límite aparentemente más complicado en una combinación de límites ya conocidos.

::: {#exm-t1-0035}
**Un límite racional calculado mediante el álgebra de límites.** Consideremos

$$
r_n=\frac{2n+1}{3n-4},
\qquad n\in\mathbb N.
$$

El denominador nunca se anula para un índice natural, porque la ecuación

$$
3n-4=0
$$

tendría la solución $n=4/3$, que no pertenece a $\mathbb N$.

Para $n\ge1$ podemos dividir numerador y denominador por $n$:

$$
r_n
=
\frac{2+1/n}{3-4/n}.
$$

Ya sabemos que

$$
\frac1n\to0
$$

para $n\ge1$. En efecto, dada $\varepsilon>0$, la propiedad arquimediana permite elegir $N$ con $N>1/\varepsilon$; entonces, si $n\ge N$,

$$
0<\frac1n\le\frac1N<\varepsilon.
$$

Es la misma estimación básica que utilizamos en §3.2, ahora escrita para una sucesión que comienza en $n=1$.

Por la multiplicación por constantes,

$$
\frac4n\to0.
$$

Como las sucesiones constantes $2$ y $3$ convergen respectivamente a $2$ y $3$, la ley de la suma da

$$
2+\frac1n\to2
$$

y

$$
3-\frac4n\to3.
$$

El límite del denominador es $3\ne0$. Por la ley del cociente,

$$
\frac{2+1/n}{3-4/n}
\to
\frac23.
$$

Por tanto,

$$
\boxed{
\frac{2n+1}{3n-4}\to\frac23.
}
$$
:::

Obsérvese qué cambió respecto de §3.2. Allí una afirmación como

$$
\frac1{n+1}\to0
$$

requirió abrir la definición, fijar $\varepsilon$ y fabricar un umbral mediante la propiedad arquimediana.

Aquí ya no necesitamos repetir ese mecanismo para toda la fracción. Hemos reducido el problema a piezas cuyos límites conocemos y hemos aplicado resultados generales previamente demostrados.

### Qué está permitido escribir desde ahora

Después de esta sección podremos abreviar razonamientos como

$$
a_n\to A,
\qquad
b_n\to B
$$

mediante expresiones del tipo

$$
\lim_{n\to\infty}(a_n+b_n)=A+B,
$$

$$
\lim_{n\to\infty}(a_nb_n)=AB,
$$

o, si $B\ne0$,

$$
\lim_{n\to\infty}\frac{a_n}{b_n}=\frac AB.
$$

Pero estas fórmulas deben leerse como aplicaciones de @prp-t1-0021, no como una licencia para sustituir símbolos mecánicamente.

Antes de usar una regla conviene comprobar:

- que los límites de las piezas realmente existen;
- que la expresión está definida en una cola suficiente;
- que, en un cociente, el límite del denominador es no nulo.

La última condición es esencial. Si

$$
b_n\to0,
$$

la ley del cociente no autoriza ninguna conclusión del tipo

$$
\frac{a_n}{b_n}\to\frac A0.
$$

La expresión $A/0$ ni siquiera es un número real. Los cocientes con denominadores que tienden a cero requerirán análisis adicional según el problema concreto; no existe aquí una regla algebraica automática.

### Qué hemos ganado

La teoría de límites dispone ahora de su primer cálculo interno.

A partir de

$$
a_n\to A,
\qquad
b_n\to B,
$$

sabemos transportar la convergencia a través de:

$$
\text{escalas},
\qquad
\text{sumas y diferencias},
\qquad
\text{productos},
\qquad
\text{cocientes con límite denominador no nulo},
$$

y también a través del valor absoluto.

La estructura de las pruebas revela tres principios reutilizables:

$$
\boxed{
\begin{array}{c}
\text{sincronizar varios controles mediante }\max,\\[3pt]
\text{convertir factores variables en cotas fijas},\\[3pt]
\text{separar de cero aquello que aparecerá en un denominador}.
\end{array}
}
$$

En la siguiente sección añadiremos una estructura distinta: el **orden**. Ya no preguntaremos qué ocurre al combinar sucesiones algebraicamente, sino qué información sobre desigualdades sobrevive al pasar al límite y cómo dos sucesiones pueden atrapar a una tercera.

## Orden y teorema del sándwich {#sec-t1-c04-05}

Las leyes algebraicas de §3.4 nos permiten transportar límites a través de sumas, productos y cocientes. Pero muchas sucesiones no se controlan mejor mediante una identidad algebraica, sino mediante una **desigualdad**.

A veces no sabemos calcular directamente una sucesión complicada, pero sí podemos compararla con otras más sencillas. En otras ocasiones sabemos que una sucesión queda siempre por debajo de otra y queremos averiguar si esa relación puede invertirse cuando pasamos al límite.

La pregunta de esta sección es, por tanto,

$$
\boxed{
\text{¿qué información de orden que vale en una cola sigue siendo visible en el límite?}
}
$$

La palabra **cola** vuelve a ser decisiva. Como el límite ignora cualquier prefijo finito, no necesitaremos exigir que una desigualdad sea verdadera desde el primer término. Bastará que lo sea eventualmente.

### Una desigualdad eventual no puede invertirse en el límite

Supongamos que

$$
a_n\le b_n
$$

para todos los índices suficientemente grandes y que

$$
a_n\to A,
\qquad
b_n\to B.
$$

¿Podría ocurrir que

$$
A>B?
$$

Si así fuera, existiría una distancia positiva entre ambos límites. La convergencia permitiría entonces obligar a $a_n$ a permanecer muy cerca de $A$ y a $b_n$ muy cerca de $B$. Para tolerancias suficientemente pequeñas, los términos de $a_n$ quedarían necesariamente **por encima** de los de $b_n$, contradiciendo la desigualdad eventual.

La intuición se convierte en la siguiente proposición.

::: {#prp-t1-0022}
**Preservación eventual del orden bajo límites.** Sean $(a_n)$ y $(b_n)$ sucesiones reales tales que

$$
a_n\to A
$$

y

$$
b_n\to B.
$$

Supongamos además que existe un índice $K$ tal que

$$
a_n\le b_n
\qquad
\text{para todo }n\ge K.
$$

Entonces

$$
A\le B.
$$

**Demostración.** Supongamos, buscando una contradicción, que

$$
A>B.
$$

Definamos

$$
d:=A-B>0.
$$

Elegimos la tolerancia

$$
\varepsilon=\frac d3.
$$

Como $a_n\to A$, existe $N_a$ tal que, si $n\ge N_a$, entonces

$$
|a_n-A|<\frac d3.
$$

En particular,

$$
a_n>A-\frac d3.
$$

Como $A=B+d$,

$$
A-\frac d3
=
B+\frac{2d}{3}.
$$

Por tanto, para $n\ge N_a$,

$$
a_n>B+\frac{2d}{3}.
$$

Por otra parte, como $b_n\to B$, existe $N_b$ tal que, si $n\ge N_b$, entonces

$$
|b_n-B|<\frac d3,
$$

y de aquí

$$
b_n<B+\frac d3.
$$

Tomemos ahora

$$
N=\max\{K,N_a,N_b\}.
$$

Para todo $n\ge N$ se cumplen simultáneamente las tres informaciones:

$$
a_n\le b_n,
$$

$$
a_n>B+\frac{2d}{3},
$$

y

$$
b_n<B+\frac d3.
$$

Las dos últimas implican

$$
a_n>b_n,
$$

porque

$$
B+\frac{2d}{3}>B+\frac d3.
$$

Esto contradice $a_n\le b_n$.

Por consiguiente, la suposición $A>B$ es imposible y debe cumplirse

$$
A\le B.
$$
:::

La prueba utiliza una arquitectura ya conocida:

$$
\boxed{
\text{hipótesis eventual}
+
\text{dos controles de convergencia}
\longrightarrow
\text{un único umbral mediante }\max.
}
$$

No importa que la desigualdad falle en los primeros cien, mil o un millón de términos. Si existe una cola en la que

$$
a_n\le b_n,
$$

esa cola basta para impedir que los límites aparezcan en el orden contrario.

### Consecuencias inmediatas

La proposición anterior contiene varias formas útiles como casos particulares.

Si

$$
a_n\ge0
$$

eventualmente y

$$
a_n\to A,
$$

podemos comparar $(a_n)$ con la sucesión constante $0$. Como

$$
0\to0,
$$

obtenemos

$$
A\ge0.
$$

Análogamente, si existe una constante $c\in\mathbb R$ tal que

$$
a_n\le c
$$

eventualmente y $a_n\to A$, entonces

$$
A\le c.
$$

Y si

$$
a_n\ge c
$$

eventualmente, entonces

$$
A\ge c.
$$

Estas versiones permiten transportar al límite cotas que solo empiezan a cumplirse después de cierto índice.

### El orden estricto puede desaparecer

Hay que leer @prp-t1-0022 con precisión. De

$$
a_n<b_n
$$

eventualmente no podemos concluir necesariamente

$$
A<B.
$$

La razón es que dos sucesiones pueden mantener una separación positiva en cada índice y, sin embargo, esa separación hacerse cada vez menor.

El ejemplo más sencillo ya está disponible:

$$
0<\frac1{n+1}
$$

para todo $n\in\mathbb N$.

Sin embargo,

$$
0\to0
$$

y, por §3.2,

$$
\frac1{n+1}\to0.
$$

Por tanto los límites satisfacen

$$
0=0,
$$

no una desigualdad estricta.

Así,

$$
\boxed{
a_n<b_n\text{ eventualmente}
\quad\centernot\Longrightarrow\quad
A<B.
}
$$

Lo que sí preserva el teorema es la versión débil:

$$
a_n<b_n
\quad\Longrightarrow\quad
a_n\le b_n
\quad\Longrightarrow\quad
A\le B.
$$

Para conservar una separación estricta en el límite necesitamos información cuantitativa adicional. Por ejemplo, si existe $\delta>0$ tal que eventualmente

$$
a_n+\delta\le b_n,
$$

entonces, usando §3.4,

$$
a_n+\delta\to A+\delta.
$$

La preservación del orden produce

$$
A+\delta\le B,
$$

y por tanto

$$
A<B.
$$

La diferencia es importante: no basta que cada desigualdad sea estricta; hace falta que exista una **separación positiva uniforme** que no se desvanezca al avanzar por la sucesión.

### Atrapar una sucesión entre dos aproximaciones

La preservación del orden resuelve una pregunta cuando ya sabemos que las dos sucesiones comparadas convergen. Pero a menudo queremos utilizar desigualdades para demostrar precisamente que una tercera sucesión **converge**.

Supongamos que podemos establecer, eventualmente,

$$
a_n\le b_n\le c_n,
$$

y que las sucesiones exteriores convergen al mismo número:

$$
a_n\to L,
\qquad
c_n\to L.
$$

Intuitivamente, si $a_n$ y $c_n$ terminan dentro de cualquier tolerancia alrededor de $L$, entonces $b_n$, atrapada entre ambas, no tiene ningún lugar fuera de ese mismo intervalo al cual escapar.

Esta es la idea del teorema del sándwich.

::: {#prp-t1-0023}
**Teorema del sándwich.** Sean $(a_n)$, $(b_n)$ y $(c_n)$ sucesiones reales. Supongamos que existe un índice $K$ tal que

$$
a_n\le b_n\le c_n
\qquad
\text{para todo }n\ge K.
$$

Si

$$
a_n\to L
$$

y

$$
c_n\to L,
$$

entonces

$$
b_n\to L.
$$

**Demostración.** Sea $\varepsilon>0$.

Como $a_n\to L$, existe $N_a$ tal que

$$
n\ge N_a
\quad\Longrightarrow\quad
|a_n-L|<\varepsilon.
$$

Esto implica

$$
L-\varepsilon<a_n<L+\varepsilon.
$$

Como $c_n\to L$, existe $N_c$ tal que

$$
n\ge N_c
\quad\Longrightarrow\quad
|c_n-L|<\varepsilon,
$$

y por tanto

$$
L-\varepsilon<c_n<L+\varepsilon.
$$

Tomemos

$$
N=\max\{K,N_a,N_c\}.
$$

Si $n\ge N$, entonces

$$
a_n\le b_n\le c_n,
$$

mientras que

$$
L-\varepsilon<a_n
$$

y

$$
c_n<L+\varepsilon.
$$

Encadenando las desigualdades,

$$
L-\varepsilon
<
a_n
\le
b_n
\le
c_n
<
L+\varepsilon.
$$

En particular,

$$
L-\varepsilon<b_n<L+\varepsilon.
$$

Por la caracterización de valor absoluto,

$$
|b_n-L|<\varepsilon.
$$

Como $\varepsilon>0$ era arbitrario, concluimos que

$$
b_n\to L.
$$
:::

Hay un detalle lógico importante en esta prueba. **No** podemos justificar el teorema diciendo simplemente:

> como $a_n\le b_n\le c_n$, pasamos al límite y obtenemos $L\le\lim b_n\le L$.

Esa escritura presupone que $\lim b_n$ ya existe, que es precisamente lo que estamos intentando demostrar.

El teorema del sándwich debe producir simultáneamente dos cosas:

1. la **existencia** del límite de $(b_n)$;
2. la **identificación** de ese límite como $L$.

La prueba $\varepsilon$–$N$ anterior hace ambas tareas sin circularidad.

### Los extremos deben converger al mismo número

La coincidencia de los límites exteriores es esencial.

Por ejemplo, consideremos

$$
a_n=0,
\qquad
c_n=1,
$$

y

$$
b_n=
\frac{1+(-1)^n}{2}.
$$

Para todo $n$,

$$
0\le b_n\le1.
$$

Las sucesiones exteriores convergen:

$$
a_n\to0,
\qquad
c_n\to1.
$$

Pero sus límites son distintos. La sucesión intermedia alterna entre $1$ y $0$, de modo que no converge.

Así, una mera cota

$$
a_n\le b_n\le c_n
$$

no basta. El sándwich funciona porque las dos paredes exteriores **se cierran sobre el mismo número**.

### La forma absoluta: una herramienta especialmente útil

En muchos problemas no resulta natural buscar dos sucesiones exteriores por separado. Es más eficiente controlar directamente la distancia del término al candidato.

Supongamos que

$$
|u_n|\le v_n
$$

eventualmente y que

$$
v_n\to0.
$$

De la desigualdad de valor absoluto obtenemos

$$
-v_n\le u_n\le v_n.
$$

Por el álgebra de límites,

$$
-v_n\to0,
$$

mientras que, por hipótesis,

$$
v_n\to0.
$$

El teorema del sándwich da entonces

$$
u_n\to0.
$$

Podemos registrar esta forma operativa como

$$
\boxed{
|u_n|\le v_n\text{ eventualmente},
\qquad
v_n\to0
\quad\Longrightarrow\quad
u_n\to0.
}
$$

Esta versión será una de las herramientas más reutilizadas del capítulo.

Su lógica es particularmente transparente: si el **tamaño** de $u_n$ está dominado por una cantidad que puede hacerse arbitrariamente pequeña, entonces $u_n$ debe acercarse a cero, aunque cambie de signo, oscile o carezca de monotonía.

### Una oscilación que desaparece por estar dominada

::: {#exm-t1-0036}
**Una sucesión oscilante controlada por sándwich.** Consideremos

$$
a_n=\frac{\sin n}{n+1},
\qquad
n\in\mathbb N.
$$

Los valores de $\sin n$ oscilan y no necesitamos describir su comportamiento con mayor precisión. Basta la desigualdad elemental

$$
|\sin n|\le1.
$$

Por tanto,

$$
\left|\frac{\sin n}{n+1}\right|
=
\frac{|\sin n|}{n+1}
\le
\frac1{n+1}.
$$

Ya sabemos que

$$
\frac1{n+1}\to0.
$$

Aplicando la forma absoluta del teorema del sándwich,

$$
\boxed{
\frac{\sin n}{n+1}\to0.
}
$$

Equivalentemente, podríamos escribir

$$
-\frac1{n+1}
\le
\frac{\sin n}{n+1}
\le
\frac1{n+1},
$$

y observar que las dos sucesiones exteriores convergen a $0$.
:::

Este ejemplo muestra por qué el sándwich es más que una regla para «calcular límites». Permite ignorar una parte complicada de una sucesión cuando esa parte está uniformemente controlada.

Aquí no necesitamos averiguar si

$$
\sin n
$$

se acerca a algún número. Ni siquiera necesitamos que converja. Lo único relevante es que su tamaño nunca excede $1$, mientras que el factor

$$
\frac1{n+1}
$$

se hace arbitrariamente pequeño.

El patrón general es

$$
\boxed{
\text{oscilación acotada}
\times
\text{factor que tiende a }0
\longrightarrow
\text{producto que tiende a }0,
}
$$

siempre que podamos justificar la estimación correspondiente.

### Cómo buscar un sándwich

En la práctica, rara vez nos entregan las tres sucesiones ya preparadas. La parte creativa consiste en **fabricar** buenas cotas.

Una estrategia especialmente eficaz para demostrar

$$
a_n\to L
$$

es comenzar por el error

$$
|a_n-L|.
$$

Si podemos encontrar una sucesión sencilla $(r_n)$ tal que

$$
|a_n-L|\le r_n
$$

eventualmente y

$$
r_n\to0,
$$

la forma absoluta del sándwich termina la prueba.

El trabajo se desplaza entonces desde

> calcular exactamente $a_n$

hacia

> encontrar una estimación suficientemente buena del error.

Este cambio de perspectiva es central en análisis. Una cota puede contener menos información que una fórmula exacta y, sin embargo, ser exactamente la información necesaria para demostrar convergencia.

### Tres errores que conviene evitar

**1. Una sola cota no determina un límite.**

De

$$
a_n\le b_n
$$

y

$$
a_n\to L
$$

no se sigue que $b_n\to L$.

Por ejemplo,

$$
0\le1
$$

para todos los índices, pero las sucesiones constantes $0$ y $1$ tienen límites distintos.

**2. Estar entre dos sucesiones convergentes no basta si sus límites son distintos.**

El ejemplo

$$
0\le\frac{1+(-1)^n}{2}\le1
$$

muestra que una sucesión intermedia puede divergir cuando las cotas exteriores convergen a números diferentes.

**3. La desigualdad estricta no tiene por qué permanecer estricta.**

Aunque

$$
0<\frac1{n+1}
$$

para todo $n$, ambos lados convergen a $0$.

Las tres advertencias comparten una misma lección: al trabajar con orden no basta mirar el símbolo de desigualdad; hay que auditar **qué límites poseen las sucesiones comparadas y qué separación cuantitativa conservan**.

### Qué hemos ganado

A la estructura algebraica de §3.4 añadimos ahora una estructura de orden.

Sabemos que:

$$
a_n\le b_n\text{ eventualmente},
\qquad
a_n\to A,
\qquad
b_n\to B
\quad\Longrightarrow\quad
A\le B;
$$

y que

$$
a_n\le b_n\le c_n\text{ eventualmente},
\qquad
a_n,c_n\to L
\quad\Longrightarrow\quad
b_n\to L.
$$

Además, disponemos de la forma especialmente útil

$$
|u_n|\le v_n\text{ eventualmente},
\qquad
v_n\to0
\quad\Longrightarrow\quad
u_n\to0.
$$

Con estas herramientas podemos pasar de la definición y las leyes generales a un pequeño repertorio de límites fundamentales. En §3.6 utilizaremos el sándwich junto con desigualdades elementales e inducción para demostrar, entre otros resultados, que las potencias recíprocas tienden a cero y que

$$
q^n\to0
$$

cuando

$$
|q|<1.
$$

## Un pequeño repertorio de límites fundamentales {#sec-t1-c04-06}

Las secciones anteriores construyeron herramientas generales. Ya sabemos trabajar directamente con la definición $\varepsilon$–$N$, combinar límites mediante operaciones algebraicas y utilizar desigualdades para atrapar una sucesión entre otras más sencillas.

Ahora conviene transformar esas herramientas en un pequeño repertorio de resultados que podamos reutilizar sin reconstruir cada prueba desde cero.

La palabra **repertorio** debe interpretarse con cuidado. No queremos una tabla de límites que se memoriza y se aplica mecánicamente. Queremos unas pocas piezas cuya demostración entendamos y que después puedan convertirse en componentes de argumentos más grandes.

El criterio será siempre el mismo:

$$
\boxed{
\text{un límite fundamental debe quedar apoyado en resultados anteriores y no en teoría todavía no construida.}
}
$$

Por eso en esta sección no utilizaremos continuidad de funciones, exponenciales reales, logaritmos, series ni regla de l'Hôpital. Todo saldrá de arquimedianidad, inducción, álgebra de límites y teorema del sándwich.

### Las potencias recíprocas también desaparecen

Ya demostramos que

$$
\frac1{n+1}\to0.
$$

¿Qué ocurre si aumentamos la potencia del denominador?

Sea $p\in\mathbb N_{>0}$. Para todo $n\in\mathbb N$ tenemos

$$
n+1\ge1.
$$

Como $p\ge1$,

$$
(n+1)^p\ge n+1,
$$

y, al tomar recíprocos positivos,

$$
0<\frac1{(n+1)^p}\le\frac1{n+1}.
$$

Los extremos satisfacen

$$
0\to0
$$

y

$$
\frac1{n+1}\to0.
$$

Por el teorema del sándwich,

$$
\boxed{
\frac1{(n+1)^p}\to0
\qquad
\text{para todo }p\in\mathbb N_{>0}.
}
$$

Este pequeño argumento ya muestra una ventaja importante de disponer de resultados generales. No necesitamos volver a fabricar un $N(\varepsilon)$ diferente para cada potencia. Una sola comparación con una sucesión cuyo límite conocemos resuelve toda la familia.

También podemos multiplicar por una constante. Si $c\in\mathbb R$, el álgebra de límites da

$$
\frac{c}{(n+1)^p}\to0.
$$

Así obtenemos un primer patrón reutilizable:

$$
\boxed{
\text{constante}
\times
\text{potencia recíproca positiva}
\longrightarrow 0.
}
$$

### Un problema diferente: ¿por qué una potencia geométrica tiende a cero?

Consideremos ahora una sucesión de la forma

$$
q^n.
$$

La intuición es familiar cuando

$$
|q|<1.
$$

Por ejemplo,

$$
\left(\frac12\right)^n,
\qquad
\left(\frac23\right)^n,
\qquad
\left(-\frac34\right)^n
$$

parecen hacerse cada vez menores en valor absoluto.

Pero aquí aparece una dificultad distinta de la que encontramos con $1/(n+1)$. La variable $n$ está en el **exponente**, de modo que una desigualdad como

$$
q^n<\varepsilon
$$

no se despeja mediante el álgebra elemental que hemos utilizado hasta ahora sin introducir logaritmos. Y los logaritmos todavía no forman parte de nuestra teoría.

Necesitamos, por tanto, otra estrategia.

Para $0<q<1$ podemos escribir

$$
q=\frac1{1+h}
$$

con algún $h>0$. Basta tomar

$$
h=\frac{1-q}{q}.
$$

Entonces

$$
q^n=\frac1{(1+h)^n}.
$$

Si conseguimos una **cota inferior sencilla** para $(1+h)^n$, obtendremos una cota superior para $q^n$.

La herramienta adecuada es una desigualdad elemental que puede demostrarse por inducción.

### La desigualdad de Bernoulli como puente entre crecimiento multiplicativo y crecimiento lineal

Sea $h>0$. Afirmamos que para todo $n\in\mathbb N$,

$$
\boxed{
(1+h)^n\ge1+nh.
}
$$

La demostración será inductiva: indicaremos explícitamente el caso base y el paso que transmite la desigualdad de $n$ a $n+1$.

**Caso base.** Para $n=0$,

$$
(1+h)^0=1=1+0h.
$$

**Paso inductivo.** Supongamos que

$$
(1+h)^n\ge1+nh.
$$

Como $1+h>0$, podemos multiplicar la desigualdad por ese número sin cambiar su sentido:

$$
(1+h)^{n+1}
\ge
(1+nh)(1+h).
$$

Desarrollando el lado derecho,

$$
(1+nh)(1+h)
=
1+(n+1)h+nh^2.
$$

Como

$$
nh^2\ge0,
$$

tenemos

$$
(1+h)^{n+1}
\ge
1+(n+1)h.
$$

La inducción queda cerrada.

La importancia de esta desigualdad en nuestro problema no consiste en que describa con gran precisión $(1+h)^n$. De hecho, la cota lineal

$$
1+nh
$$

es muy rudimentaria comparada con la potencia. Pero es suficiente para nuestro objetivo.

Al tomar recíprocos positivos obtenemos

$$
0<\frac1{(1+h)^n}\le\frac1{1+nh}.
$$

Hemos convertido una potencia en una expresión lineal en $n$ que sí podemos controlar directamente.

### Un caso completo antes del resultado general

::: {#exm-t1-0037}
**Construcción detallada del límite geométrico: $(2/3)^n\to0$.** Consideremos

$$
a_n=\left(\frac23\right)^n,
\qquad n\ge0.
$$

No utilizaremos logaritmos ni una función exponencial real.

Escribimos

$$
\frac23
=
\frac1{1+1/2}.
$$

Por la desigualdad de Bernoulli con $h=1/2$,

$$
\left(1+\frac12\right)^n
\ge
1+\frac n2.
$$

Tomando recíprocos,

$$
0<
\left(\frac23\right)^n
\le
\frac1{1+n/2}
=
\frac2{n+2}.
$$

Ahora debemos justificar que la sucesión de la derecha tiende a cero. Podemos hacerlo con el álgebra ya disponible:

$$
\frac2{n+2}
=
\frac{2/(n+1)}{(n+2)/(n+1)}
=
\frac{2/(n+1)}{1+1/(n+1)}.
$$

Como

$$
\frac1{n+1}\to0,
$$

tenemos

$$
\frac{2}{n+1}\to0
$$

y

$$
1+\frac1{n+1}\to1.
$$

Por la ley del cociente,

$$
\frac2{n+2}\to0.
$$

Por tanto,

$$
0
\le
\left(\frac23\right)^n
\le
\frac2{n+2},
$$

con ambos extremos convergiendo a $0$. El teorema del sándwich da

$$
\boxed{
\left(\frac23\right)^n\to0.
}
$$

**Lectura de la estrategia.** La potencia no se resolvió despejando $n$. La reemplazamos por una cota más sencilla:

$$
\left(\frac23\right)^n
=
\frac1{(1+1/2)^n}
\le
\frac1{1+n/2}.
$$

Bernoulli produjo la comparación y el sándwich convirtió esa comparación en convergencia.
:::

El ejemplo contiene ya toda la estructura necesaria para el caso general.

::: {#cor-t1-0008}
**Límite de una sucesión geométrica con razón de módulo menor que uno.** Sea $q\in\mathbb R$ con

$$
|q|<1.
$$

Entonces, considerando la sucesión $(q^n)_{n\ge1}$,

$$
\boxed{q^n\to0.}
$$

**Demostración.** Distinguimos casos.

Si $q=0$, entonces

$$
q^n=0
$$

para todo $n\ge1$, y la conclusión es inmediata.

Supongamos ahora

$$
0<|q|<1.
$$

Definimos

$$
r=|q|.
$$

Entonces $0<r<1$. Existe $h>0$ tal que

$$
r=\frac1{1+h};
$$

por ejemplo,

$$
h=\frac{1-r}{r}>0.
$$

Por Bernoulli,

$$
(1+h)^n\ge1+nh.
$$

Por tanto,

$$
0<r^n
=
\frac1{(1+h)^n}
\le
\frac1{1+nh}.
$$

Veamos directamente que

$$
\frac1{1+nh}\to0.
$$

Sea $\varepsilon>0$. Por la propiedad arquimediana podemos elegir $N\in\mathbb N$ con

$$
N>\frac1{h\varepsilon}.
$$

En particular $N>0$. Si $n\ge N$, entonces

$$
1+nh>nh\ge Nh>\frac1\varepsilon.
$$

Tomando recíprocos positivos,

$$
0<\frac1{1+nh}<\varepsilon.
$$

Así,

$$
\frac1{1+nh}\to0.
$$

El sándwich produce

$$
r^n\to0.
$$

Finalmente,

$$
|q^n|
=
|q|^n
=
r^n.
$$

Como $r^n\to0$, la forma absoluta del teorema del sándwich implica

$$
q^n\to0.
$$
:::

Esta prueba merece una segunda lectura porque combina casi todo lo construido hasta ahora:

1. **álgebra:** $|q|=1/(1+h)$;
2. **inducción:** Bernoulli;
3. **arquimedianidad:** producir un umbral para $1/(1+nh)$;
4. **orden:** convertir una desigualdad en una cota útil;
5. **sándwich:** transportar el límite de la cota a la potencia geométrica;
6. **valor absoluto:** reducir el caso negativo al positivo.

No hemos utilizado ninguna teoría de la función exponencial. El resultado pertenece enteramente a la teoría secuencial ya disponible.

### Por qué la hipótesis $|q|<1$ es esencial

Conviene auditar la frontera del corolario.

Si

$$
q=1,
$$

entonces

$$
q^n=1
$$

para todo $n$, de modo que el límite es $1$, no $0$.

Si

$$
q=-1,
$$

obtenemos

$$
(-1)^n,
$$

cuya divergencia ya demostramos en §3.2.

Por tanto, no podemos reemplazar la condición

$$
|q|<1
$$

por

$$
|q|\le1.
$$

Cuando $|q|>1$, los tamaños $|q|^n$ crecen en lugar de contraerse. Todavía no formalizaremos ese comportamiento mediante límites infinitos; esa será tarea de §3.9.

### Cocientes de polinomios: dividir por la potencia dominante

Los límites anteriores permiten sistematizar una familia importante de ejemplos.

Consideremos

$$
a_n=
\frac{3n^2-5n+7}{2n^2+n-4}.
$$

La dificultad aparente es que numerador y denominador aumentan de tamaño. Pero para un límite real no necesitamos estudiar ambos por separado. Dividimos toda la fracción por la mayor potencia presente, aquí $n^2$.

Para $n\ge1$,

$$
\frac{3n^2-5n+7}{2n^2+n-4}
=
\frac{3-5/n+7/n^2}{2+1/n-4/n^2}.
$$

Ya sabemos que

$$
\frac1n\to0
$$

y

$$
\frac1{n^2}\to0.
$$

Por el álgebra de límites,

$$
3-\frac5n+\frac7{n^2}\to3
$$

y

$$
2+\frac1n-\frac4{n^2}\to2.
$$

Como el límite del denominador es distinto de cero, la ley del cociente da

$$
\boxed{
\frac{3n^2-5n+7}{2n^2+n-4}
\to
\frac32.
}
$$

El procedimiento general ya es visible. Si numerador y denominador son polinomios del mismo grado, dividir por la potencia dominante hace desaparecer todos los términos de grado inferior mediante factores del tipo $1/n^p$. El límite queda determinado por el cociente de los coeficientes principales.

Si el grado del numerador es menor que el del denominador, la misma operación deja en el numerador únicamente términos que contienen potencias recíprocas. Por ejemplo,

$$
\frac{4n+1}{n^3+2}
=
\frac{4/n^2+1/n^3}{1+2/n^3}
\to0.
$$

Así obtenemos, para los casos de límite real que necesitamos ahora, la regla estructural:

$$
\boxed{
\begin{array}{ll}
\deg P<\deg Q
&\Longrightarrow\dfrac{P(n)}{Q(n)}\to0,\\[8pt]
\deg P=\deg Q
&\Longrightarrow\dfrac{P(n)}{Q(n)}\to
\dfrac{\text{coeficiente principal de }P}
{\text{coeficiente principal de }Q},
\end{array}
}
$$

siempre que el denominador esté definido en la cola correspondiente.

No hemos creado una nueva regla independiente. Todo proviene de

$$
\frac1{n^p}\to0
$$

y del álgebra de límites.

El caso

$$
\deg P>\deg Q
$$

suele producir crecimiento sin límite real finito. Lo estudiaremos cuando dispongamos de la definición rigurosa de $+\infty$ y $-\infty$ en §3.9.

### Oscilaciones amortiguadas: lo complicado puede quedar encerrado en una cota

El ejemplo de §3.5 con

$$
\frac{\sin n}{n+1}
$$

mostró un fenómeno general: una parte de la sucesión puede oscilar sin converger, mientras otro factor reduce su tamaño hasta volver irrelevante esa oscilación para el límite.

Consideremos, por ejemplo,

$$
a_n=
\frac{3(-1)^n-2\sin n}{(n+1)^2}.
$$

No necesitamos comprender la interacción exacta entre $(-1)^n$ y $\sin n$. Basta estimar:

$$
\begin{aligned}
|3(-1)^n-2\sin n|
&\le
3|(-1)^n|+2|\sin n|\\
&\le3+2\\
&=5.
\end{aligned}
$$

Por tanto,

$$
|a_n|
\le
\frac5{(n+1)^2}.
$$

Como

$$
\frac5{(n+1)^2}\to0,
$$

la forma absoluta del sándwich da

$$
\boxed{
\frac{3(-1)^n-2\sin n}{(n+1)^2}
\to0.
}
$$

Aquí aparece un principio que conviene conservar:

$$
\boxed{
\text{numerador uniformemente acotado}
\quad+
\text{denominador cuyo recíproco tiende a }0
\quad\Longrightarrow\quad
\text{cociente que tiende a }0,
}
$$

siempre que la estimación se formule rigurosamente.

Más generalmente, si $(u_n)$ es una sucesión acotada y

$$
v_n\to0,
$$

entonces

$$
u_nv_n\to0.
$$

Podemos justificarlo de dos maneras con herramientas ya conocidas.

Por un lado, como $(u_n)$ es acotada, existe $M>0$ tal que

$$
|u_n|\le M.
$$

Entonces

$$
|u_nv_n|
\le
M|v_n|.
$$

Como

$$
|v_n|\to0
$$

y por álgebra

$$
M|v_n|\to0,
$$

el sándwich da

$$
u_nv_n\to0.
$$

Por otro lado, si además supiéramos que $(u_n)$ converge, el resultado sería un caso particular de la ley del producto. La estimación anterior es más fuerte para este propósito: **no exige que $(u_n)$ converja**, solo que esté acotada.

Esto explica por qué podemos controlar factores como

$$
(-1)^n,
\qquad
\sin n,
\qquad
\cos n,
$$

cuando aparecen multiplicados por una sucesión que tiende a cero.

### Una red mínima de límites que ya podemos reutilizar

Podemos reunir lo construido hasta ahora sin convertirlo en una lista aislada de recetas.

Sabemos que

$$
\frac1{n+1}\to0,
$$

que para cada $p\in\mathbb N_{>0}$,

$$
\frac1{(n+1)^p}\to0,
$$

y que si $|q|<1$,

$$
q^n\to0.
$$

Además, mediante álgebra y sándwich podemos obtener inmediatamente límites de expresiones construidas con estas piezas.

Por ejemplo,

$$
\frac{7}{(n+1)^3}\to0,
$$

$$
\left(-\frac45\right)^n\to0,
$$

y

$$
\frac{2+\sin n}{n+1}\to0,
$$

porque

$$
|2+\sin n|\le3.
$$

La meta de esta sección no era acumular ejemplos, sino disponer de unas pocas **unidades de construcción** cuyo origen conocemos.

### Qué no hemos utilizado

Es importante hacer explícita la frontera lógica de los argumentos.

Para obtener los límites de esta sección usamos:

- la propiedad arquimediana;
- inducción matemática;
- desigualdades elementales;
- álgebra de límites;
- preservación del orden;
- teorema del sándwich;
- valor absoluto.

No utilizamos:

- límites de funciones;
- continuidad;
- función exponencial real;
- logaritmos;
- derivadas;
- regla de l'Hôpital;
- series;
- subsucesiones;
- Bolzano–Weierstrass;
- criterio de Cauchy.

Esta auditoría importa porque el siguiente gran paso del capítulo será cualitativamente distinto.

Hasta ahora, en todos los límites que hemos demostrado, **ya conocíamos o sospechábamos el candidato** y después verificábamos que los términos se acercaban a él.

En §3.7 preguntaremos algo más profundo:

> ¿puede la estructura de $\mathbb R$ garantizar que una sucesión converge aunque todavía no conozcamos de antemano su límite?

La respuesta será afirmativa para sucesiones monótonas y acotadas. Allí aparecerá por primera vez en este capítulo la completitud de $\mathbb R$ como mecanismo directo de existencia de límites.

## Monotonía + completitud = convergencia {#sec-t1-c04-07}

Hasta ahora, para demostrar que una sucesión converge, hemos seguido casi siempre este esquema:

1. proponemos o descubrimos un candidato $L$;
2. demostramos que $a_n\to L$ mediante la definición, el álgebra o el sándwich.

Ese procedimiento responde bien a preguntas del tipo

$$
\text{«¿cuál es el límite de esta sucesión?»}
$$

cuando ya disponemos de una expresión que permite adivinar el candidato.

Pero existe otra pregunta, más estructural:

$$
\boxed{
\text{¿podemos demostrar que un límite existe sin conocer primero su valor?}
}
$$

La respuesta será afirmativa cuando una sucesión combine dos tipos de control que hasta ahora hemos mantenido separados:

- **monotonía**, que impide retrocesos en una dirección de orden;
- **acotación**, que impide avanzar indefinidamente en esa misma dirección.

La afirmación decisiva no será una propiedad puramente algebraica. Para convertir esos dos controles en la existencia de un número real que actúe como límite necesitaremos la **completitud de $\mathbb R$**.

Esta es la cadena que debemos hacer visible:

$$
\boxed{
\text{monotonía}
+
\text{cota}
+
\text{completitud}
\longrightarrow
\sup/\inf
\longrightarrow
\text{límite}.
}
$$

### Monotonía para sucesiones

Como una sucesión es una función cuyo dominio está ordenado, podemos trasladar directamente el lenguaje de monotonía desarrollado en `T1-C03`. Conviene, sin embargo, fijar la notación específica que usaremos a partir de ahora.

::: {#def-t1-0030}
**Sucesiones crecientes, decrecientes y monótonas.** Sea $(a_n)_{n\ge n_0}$ una sucesión real.

Diremos que $(a_n)$ es **creciente** si

$$
n<m
\quad\Longrightarrow\quad
a_n\le a_m.
$$

Diremos que es **decreciente** si

$$
n<m
\quad\Longrightarrow\quad
a_n\ge a_m.
$$

La sucesión es **monótona** si es creciente o decreciente.

Diremos que es **estrictamente creciente** si

$$
n<m
\quad\Longrightarrow\quad
a_n<a_m,
$$

y **estrictamente decreciente** si

$$
n<m
\quad\Longrightarrow\quad
a_n>a_m.
$$
:::

En este tratado, por tanto, las palabras **creciente** y **decreciente** se usan en sentido débil: se permite la igualdad entre términos distintos. Cuando necesitemos excluirla diremos explícitamente **estrictamente** creciente o decreciente.

Por ejemplo, una sucesión constante es a la vez creciente y decreciente. Esta convención es importante porque el teorema que demostraremos no necesita monotonía estricta.

Para verificar monotonía suele bastar comparar términos consecutivos. Si

$$
a_n\le a_{n+1}
$$

para todo $n\ge n_0$, entonces, dados $n<m$, podemos encadenar

$$
a_n\le a_{n+1}\le\cdots\le a_m,
$$

y por tanto $a_n\le a_m$. El argumento para sucesiones decrecientes es análogo.

Así, en la práctica, muchas pruebas de monotonía comenzarán estudiando el signo de

$$
a_{n+1}-a_n
$$

o comparando directamente $a_{n+1}$ con $a_n$.

### Dos controles distintos: dirección y barrera

Una sucesión creciente satisface

$$
a_{n_0}\le a_{n_0+1}\le a_{n_0+2}\le\cdots.
$$

Esto controla la **dirección**, pero no impide que los términos crezcan sin límite real finito. La sucesión

$$
a_n=n
$$

es creciente y no está acotada superiormente.

Una cota superior, en cambio, proporciona una **barrera**. Si existe $M\in\mathbb R$ tal que

$$
a_n\le M
$$

para todo $n$, los términos no pueden atravesar $M$. Pero la acotación por sí sola no controla la dirección: $(-1)^n$ permanece entre $-1$ y $1$ y, sin embargo, oscila para siempre.

Por separado, entonces,

$$
\text{monotonía}
\qquad\text{y}\qquad
\text{acotación}
$$

no garantizan convergencia.

Lo notable es que, en $\mathbb R$, su combinación sí lo hace.

### ¿De dónde saldrá el candidato a límite?

Supongamos que $(a_n)$ es creciente y está acotada superiormente. Consideremos el conjunto de todos sus valores:

$$
S=\{a_n:n\ge n_0\}.
$$

El conjunto $S$ es no vacío y está acotado superiormente. Por la completitud de $\mathbb R$, existe

$$
L=\sup S.
$$

Aquí aparece el candidato que antes no teníamos que adivinar.

La elección no es arbitraria. Como $L$ es una cota superior,

$$
a_n\le L
$$

para todo $n$. Y como es la **menor** cota superior, cualquier número un poco menor que $L$ deja de ser cota superior.

En particular, para todo $\varepsilon>0$,

$$
L-\varepsilon
$$

no puede ser una cota superior de $S$. Por la caracterización aproximativa del supremo demostrada en `T1-C02`, existe entonces algún término $a_N$ tal que

$$
L-\varepsilon<a_N\le L.
$$

Hasta aquí hemos encontrado **un** término suficientemente próximo a $L$. Eso todavía no es convergencia: necesitamos controlar todos los términos posteriores.

Aquí entra exactamente la monotonía. Si $n\ge N$, entonces

$$
a_N\le a_n.
$$

Por tanto,

$$
L-\varepsilon<a_N\le a_n\le L<L+\varepsilon.
$$

Y ahora sí toda la cola queda atrapada en el intervalo

$$
(L-\varepsilon,L+\varepsilon).
$$

La prueba completa no necesita nada más.

::: {#thm-t1-0010}
**Teorema de convergencia monótona.** Sea $(a_n)_{n\ge n_0}$ una sucesión real.

1. Si $(a_n)$ es creciente y está acotada superiormente, entonces converge y
   $$
   \lim_{n\to\infty}a_n
   =
   \sup\{a_n:n\ge n_0\}.
   $$

2. Si $(a_n)$ es decreciente y está acotada inferiormente, entonces converge y
   $$
   \lim_{n\to\infty}a_n
   =
   \inf\{a_n:n\ge n_0\}.
   $$

En particular, toda sucesión monótona y acotada converge.

**Demostración.** Demostremos primero el caso creciente.

Sea

$$
S=\{a_n:n\ge n_0\}.
$$

Como la sucesión está acotada superiormente, $S$ es un conjunto no vacío y acotado superiormente. Por completitud de $\mathbb R$, existe

$$
L=\sup S.
$$

Queremos demostrar que $a_n\to L$.

Sea $\varepsilon>0$. Como $L$ es el supremo de $S$, el número

$$
L-\varepsilon
$$

no es una cota superior de $S$. Por tanto existe algún índice $N\ge n_0$ tal que

$$
L-\varepsilon<a_N.
$$

Como $L$ sí es una cota superior de $S$,

$$
a_n\le L
$$

para todo $n\ge n_0$.

Además, como la sucesión es creciente, para todo $n\ge N$ tenemos

$$
a_N\le a_n.
$$

Combinando las tres desigualdades,

$$
L-\varepsilon<a_N\le a_n\le L<L+\varepsilon.
$$

Así, para todo $n\ge N$,

$$
L-\varepsilon<a_n<L+\varepsilon,
$$

lo cual equivale a

$$
|a_n-L|<\varepsilon.
$$

Como $\varepsilon>0$ era arbitrario,

$$
a_n\to L.
$$

Por tanto,

$$
\lim_{n\to\infty}a_n
=
\sup\{a_n:n\ge n_0\}.
$$

Consideremos ahora el caso decreciente. Sea nuevamente

$$
S=\{a_n:n\ge n_0\}.
$$

Como la sucesión está acotada inferiormente, $S$ es no vacío y acotado inferiormente. La completitud de $\mathbb R$, mediante la existencia de ínfimos ya deducida en `T1-C02`, garantiza que existe

$$
L=\inf S.
$$

Sea $\varepsilon>0$. Como $L$ es el ínfimo de $S$, el número

$$
L+\varepsilon
$$

no es una cota inferior de $S$. Por tanto existe algún índice $N\ge n_0$ tal que

$$
a_N<L+\varepsilon.
$$

Como $L$ es una cota inferior,

$$
L\le a_n
$$

para todo $n\ge n_0$.

Y como la sucesión es decreciente, si $n\ge N$ entonces

$$
a_n\le a_N.
$$

En consecuencia,

$$
L-\varepsilon<L\le a_n\le a_N<L+\varepsilon.
$$

Por tanto,

$$
|a_n-L|<\varepsilon
$$

para todo $n\ge N$. Como $\varepsilon>0$ era arbitrario,

$$
a_n\to L.
$$

Así,

$$
\lim_{n\to\infty}a_n
=
\inf\{a_n:n\ge n_0\}.
$$

Quedan demostradas ambas afirmaciones.
:::

### Dónde se usa exactamente cada hipótesis

El teorema es suficientemente importante como para auditar su demostración línea por línea.

En el caso creciente:

1. **Acotación superior.** Garantiza que el conjunto
   $$
   S=\{a_n:n\ge n_0\}
   $$
   tiene cotas superiores.
2. **Completitud de $\mathbb R$.** Garantiza que entre esas cotas existe una menor:
   $$
   L=\sup S\in\mathbb R.
   $$
3. **Propiedad aproximativa del supremo.** Para cada $\varepsilon>0$ produce un índice $N$ con
   $$
   L-\varepsilon<a_N.
   $$
4. **Monotonía creciente.** Propaga esa aproximación puntual a toda la cola:
   $$
   n\ge N
   \quad\Longrightarrow\quad
   a_N\le a_n.
   $$
5. **Propiedad de cota superior del supremo.** Impide que los términos atraviesen $L$:
   $$
   a_n\le L.
   $$

La arquitectura es, por tanto,

$$
\boxed{
\begin{array}{c}
\text{acotación superior}\\
+\\
\text{completitud}
\end{array}
\Longrightarrow
L=\sup S
\Longrightarrow
\begin{array}{c}
\text{un término entra cerca de }L\\
+\\
\text{monotonía}
\end{array}
\Longrightarrow
\text{toda la cola entra cerca de }L.
}
$$

El caso decreciente reproduce el mismo mecanismo con ínfimos y orden invertido.

### La completitud no está escondida: es el motor de existencia

En las primeras pruebas $\varepsilon$–$N$ del capítulo, la propiedad arquimediana nos permitía fabricar umbrales. En el teorema anterior ocurre algo distinto: antes de buscar un umbral necesitamos **producir el propio candidato a límite**.

Ese candidato aparece como

$$
\sup S
$$

o

$$
\inf S.
$$

La afirmación de que esos números existen en $\mathbb R$ no procede de la monotonía. Procede de la completitud.

Esto permite localizar con precisión el punto donde fallaría la misma demostración si trabajáramos únicamente en $\mathbb Q$. Un conjunto no vacío y acotado de racionales puede carecer de supremo racional, como vimos en `T1-C02`. En ese caso, el paso

$$
S\text{ acotado superiormente}
\quad\Longrightarrow\quad
\sup S\text{ existe en el mismo sistema numérico}
$$

no estaría disponible.

Por eso el teorema de convergencia monótona no es simplemente una consecuencia del orden: es una manifestación secuencial de la completitud de los números reales.

Podemos condensar esta segunda gran aparición operativa de completitud en el tratado como

$$
\boxed{
\text{completitud}
\longrightarrow
\sup/\inf
\longrightarrow
\text{convergencia monótona}.
}
$$

### Qué falla si quitamos una hipótesis

El teorema necesita las dos piezas de control.

**Sin acotación suficiente.** La sucesión

$$
a_n=n
$$

es creciente, pero no está acotada superiormente. Tampoco puede converger a un número real: si convergiera, @prp-t1-0020 implicaría que sería acotada, contradiciendo la propiedad arquimediana.

Así,

$$
\boxed{
\text{creciente}
\centernot\Longrightarrow
\text{convergente}.
}
$$

La versión decreciente presenta el mismo problema si falta una cota inferior.

**Sin monotonía.** La sucesión

$$
b_n=(-1)^n
$$

es acotada, pero @exm-t1-0033 demostró que diverge.

Por tanto,

$$
\boxed{
\text{acotada}
\centernot\Longrightarrow
\text{convergente}.
}
$$

Lo que sí obtenemos al combinar ambas condiciones es

$$
\boxed{
\text{monótona}+\text{acotada}
\Longrightarrow
\text{convergente}.
}
$$

No estamos corrigiendo las implicaciones falsas anteriores; estamos añadiendo exactamente la hipótesis que faltaba para convertirlas en un teorema verdadero.

### Una cota en la dirección correcta es suficiente

La formulación «monótona y acotada» es cómoda, pero la demostración revela una versión más precisa.

Para una sucesión **creciente** solo necesitamos una cota **superior**. Ya existe automáticamente una cota inferior: el primer término satisface

$$
a_{n_0}\le a_n
$$

para todo $n\ge n_0$.

Del mismo modo, para una sucesión **decreciente** solo necesitamos una cota **inferior**, porque

$$
a_n\le a_{n_0}
$$

para todo $n\ge n_0$.

Así, las hipótesis realmente ajustadas son

$$
\boxed{
\begin{aligned}
\text{creciente}+\text{acotada superiormente}
&\Longrightarrow\text{convergente},\\
\text{decreciente}+\text{acotada inferiormente}
&\Longrightarrow\text{convergente}.
\end{aligned}
}
$$

Esta precisión será útil en sucesiones recursivas: no necesitaremos encerrar siempre todos los términos entre dos cotas nuevas; bastará demostrar monotonía y encontrar una barrera en la dirección hacia la que avanzan.

### El teorema demuestra existencia antes de identificar un número sencillo

Consideremos una sucesión creciente y acotada superiormente. El teorema garantiza que

$$
L=\sup\{a_n:n\ge n_0\}
$$

es su límite, incluso si todavía no disponemos de una fórmula elemental para $L$.

Este cambio de perspectiva es importante. Hasta ahora el candidato solía aparecer antes que la prueba de convergencia. A partir de ahora podremos invertir el orden lógico:

$$
\boxed{
\text{primero demostrar que el límite existe}
\quad\longrightarrow\quad
\text{después identificarlo}.
}
$$

En una sucesión recursiva, por ejemplo, la monotonía y una cota podrán darnos existencia mediante el teorema de convergencia monótona. Solo después tendrá sentido utilizar la recurrencia y el álgebra de límites para deducir una ecuación satisfecha por el límite.

Resolver primero esa ecuación y declarar que la sucesión converge sería invertir indebidamente la lógica.

### Monotonía eventual también basta

La convergencia depende de una cola. Por ello, si una sucesión no es monótona desde su primer término pero existe un índice $N_0$ tal que la cola

$$
(a_n)_{n\ge N_0}
$$

es creciente y está acotada superiormente, el teorema de convergencia monótona se aplica a esa cola. La cola converge y, por @prp-t1-0019, la sucesión completa converge al mismo límite.

Análogamente, una cola decreciente y acotada inferiormente basta.

Esta observación evita exigir regularidad innecesaria a una cantidad finita de términos iniciales.

### La herramienta que necesitábamos para las recurrencias

Con §3.7 disponemos por primera vez de un criterio de **existencia de límite** que no requiere conocer de antemano el valor del límite.

El protocolo que emerge es:

$$
\boxed{
\text{demostrar monotonía}
\quad+
\text{encontrar una cota en la dirección correcta}
\quad\Longrightarrow\quad
\text{obtener convergencia por completitud}.
}
$$

En §3.8 aplicaremos exactamente este mecanismo a una sucesión definida recursivamente. Allí habrá que separar cinco preguntas:

1. ¿la recurrencia está bien definida?;
2. ¿qué región permanece invariante?;
3. ¿la sucesión es monótona?;
4. ¿por qué existe un límite?;
5. una vez establecida la existencia, ¿cómo identificamos ese límite sin invocar continuidad?

El cuarto paso será una aplicación directa del @thm-t1-0010. El quinto utilizará el desplazamiento de índices y el álgebra de límites ya demostrados.

## Sucesiones recursivas: fabricar y controlar un límite {#sec-t1-c04-08}

Las sucesiones estudiadas hasta ahora estaban dadas, en su mayoría, por una fórmula que permitía calcular directamente el término de índice $n$. Por ejemplo,

$$
a_n=\frac{1}{n+1}
$$

nos entrega $a_n$ sin necesidad de conocer $a_{n-1}$.

Una **regla recursiva** funciona de otra manera. En lugar de decirnos directamente cuánto vale el término de índice $n$, nos indica cómo fabricar el término siguiente a partir de uno o varios términos anteriores.

Por ejemplo,

$$
a_0=1,
\qquad
a_{n+1}=\sqrt{2+a_n}
$$

produce sucesivamente

$$
a_1=\sqrt3,
$$

$$
a_2=\sqrt{2+\sqrt3},
$$

$$
a_3=\sqrt{2+\sqrt{2+\sqrt3}},
$$

y así indefinidamente, siempre que cada paso esté bien definido.

Esta diferencia cambia también la estrategia de estudio. Una fórmula explícita puede permitirnos comparar directamente $a_n$ con un candidato de límite. En una recurrencia, en cambio, la información principal suele estar escondida en la relación entre términos consecutivos.

La pregunta deja de ser solamente

> ¿qué expresión tiene $a_n$?,

y pasa a ser

> **¿qué propiedades conserva el procedimiento que transforma $a_n$ en $a_{n+1}$?**

Ese cambio de mirada será el centro de esta sección.

### Una regla recursiva no garantiza por sí sola una sucesión real infinita

Es fácil escribir una recurrencia sintácticamente correcta y olvidar que cada término posterior debe existir dentro del sistema numérico en el que estamos trabajando.

Por ejemplo, si intentáramos definir

$$
c_0=-3,
\qquad
c_{n+1}=\sqrt{2+c_n},
$$

el primer paso exigiría

$$
c_1=\sqrt{-1},
$$

que no es un número real.

Por tanto, la expresión

$$
c_{n+1}=\sqrt{2+c_n}
$$

no basta por sí sola para garantizar una sucesión real definida para todo $n\in\mathbb N$. Debemos verificar que, cada vez que aplicamos la regla, el nuevo término vuelve a quedar dentro del dominio donde el siguiente paso tiene sentido.

Esta observación es una versión dinámica de una pregunta ya conocida desde `T1-C03`:

$$
\boxed{
\text{antes de usar una regla, debemos comprobar que está bien definida sobre los objetos que realmente aparecen.}
}
$$

En una recurrencia esa comprobación suele hacerse encontrando una **región invariante**: un conjunto de valores del cual la regla no consigue sacar a la sucesión.

No introduciremos una teoría abstracta de sistemas dinámicos. Nos basta la idea operativa:

> si demostramos que $a_n$ pertenece a cierto intervalo y que esa pertenencia obliga a que $a_{n+1}$ permanezca en el mismo intervalo, la inducción controla todos los términos.

### Cinco preguntas para auditar una recurrencia

A partir de ahora organizaremos muchos problemas recursivos mediante cinco preguntas.

1. **¿Está bien definida?**  
   ¿Cada paso produce un número real permitido?

2. **¿Qué región permanece invariante?**  
   ¿Podemos encerrar todos los términos en un intervalo o encontrar una barrera útil?

3. **¿Es monótona?**  
   ¿Los términos avanzan sistemáticamente en una dirección?

4. **¿Por qué existe un límite?**  
   Si obtenemos monotonía y una cota en la dirección correcta, podemos invocar @thm-t1-0010.

5. **Una vez demostrada la existencia, ¿cómo identificamos el límite?**  
   Aquí utilizaremos desplazamiento de índices y el álgebra de límites de §3.4.

La separación entre las preguntas 4 y 5 es esencial:

$$
\boxed{
\text{demostrar existencia del límite}
\neq
\text{resolver una ecuación que un eventual límite tendría que satisfacer}.
}
$$

Una ecuación puede producir **candidatos**. No produce por sí sola convergencia.

### El ejemplo rector: un radical construido término a término

Analicemos completamente la sucesión

$$
a_0=1,
\qquad
a_{n+1}=\sqrt{2+a_n}.
$$

Los primeros términos son aproximadamente

$$
1,\quad
1.732,\quad
1.932,\quad
1.983,\quad\dots
$$

Esta inspección sugiere dos conjeturas:

- los términos parecen crecer;
- parecen acercarse a $2$ sin superarlo.

Pero una tabla finita no demuestra ninguna de las dos afirmaciones. Nuestro objetivo será convertir esas observaciones en una cadena deductiva completa.

::: {#exm-t1-0038}
**Una recurrencia controlada desde el principio hasta el límite.** Sea $(a_n)$ la sucesión definida por

$$
a_0=1,
\qquad
a_{n+1}=\sqrt{2+a_n}.
$$

Demostraremos, en este orden, que

1. la sucesión está bien definida para todo $n$;
2. 
   $$
   1\le a_n<2
   $$
   para todo $n$;
3. $(a_n)$ es estrictamente creciente;
4. $(a_n)$ converge por el teorema de convergencia monótona;
5. su límite es
   $$
   2.
   $$

**Paso 1 y paso 2: bien definida y región invariante.**

Demostraremos por inducción la afirmación

$$
P(n):\qquad 1\le a_n<2.
$$

**Caso base.** Como

$$
a_0=1,
$$

se cumple inmediatamente

$$
1\le a_0<2.
$$

**Paso inductivo.** Supongamos que para algún $n\in\mathbb N$ tenemos

$$
1\le a_n<2.
$$

Entonces

$$
3\le 2+a_n<4.
$$

En particular,

$$
2+a_n>0,
$$

de modo que la raíz cuadrada real

$$
a_{n+1}=\sqrt{2+a_n}
$$

está bien definida.

Además, como $a_{n+1}\ge0$ y

$$
a_{n+1}^2=2+a_n,
$$

las desigualdades

$$
1<3\le a_{n+1}^2<4=2^2
$$

implican

$$
1<a_{n+1}<2.
$$

Por tanto,

$$
1\le a_{n+1}<2.
$$

La inducción queda cerrada. Hemos demostrado simultáneamente que todos los pasos de la recurrencia tienen sentido en $\mathbb R$ y que

$$
\boxed{
1\le a_n<2
\qquad
\text{para todo }n\in\mathbb N.
}
$$

El intervalo $[1,2)$ es, en este sentido, una región invariante para la recurrencia.

En particular, $2$ es una cota superior de la sucesión.

**Paso 3: monotonía.**

Queremos demostrar que

$$
a_{n+1}>a_n
$$

para todo $n$.

Ya sabemos que ambos números son no negativos. Por tanto, podemos comparar sus cuadrados.

Usando la recurrencia,

$$
a_{n+1}^2-a_n^2
=
(2+a_n)-a_n^2.
$$

Factorizamos:

$$
\begin{aligned}
2+a_n-a_n^2
&=-(a_n^2-a_n-2)\\
&=-(a_n-2)(a_n+1)\\
&=(2-a_n)(a_n+1).
\end{aligned}
$$

Por el paso anterior,

$$
a_n<2
$$

y

$$
a_n\ge1,
$$

así que

$$
2-a_n>0
$$

y

$$
a_n+1>0.
$$

Por consiguiente,

$$
a_{n+1}^2-a_n^2
=
(2-a_n)(a_n+1)
>0.
$$

Luego

$$
a_{n+1}^2>a_n^2.
$$

Como $a_{n+1}\ge0$ y $a_n\ge0$, se sigue que

$$
a_{n+1}>a_n.
$$

Así, $(a_n)$ es estrictamente creciente.

**Paso 4: existencia del límite.**

Hemos demostrado dos propiedades:

$$
(a_n)\text{ es creciente}
$$

y

$$
a_n<2
\qquad
\text{para todo }n.
$$

Por tanto, la sucesión es creciente y está acotada superiormente.

Aplicando @thm-t1-0010, existe un número real $L$ tal que

$$
a_n\to L.
$$

Además, el teorema identifica abstractamente ese número como

$$
L=\sup\{a_n:n\in\mathbb N\}.
$$

Como cada término satisface

$$
1\le a_n<2,
$$

tenemos en particular

$$
1\le L\le2.
$$

Hasta aquí hemos demostrado **existencia**. Todavía no hemos demostrado que $L=2$.

**Paso 5: identificación del límite sin continuidad.**

Como

$$
a_n\to L,
$$

la invariancia por desplazamiento de índices establecida en §3.3 da

$$
a_{n+1}\to L.
$$

La recurrencia satisface, para todo $n$,

$$
a_{n+1}^2=2+a_n.
$$

Ahora utilizamos únicamente el álgebra de límites ya demostrada.

Como

$$
a_{n+1}\to L,
$$

la regla del producto implica

$$
a_{n+1}^2
=
a_{n+1}a_{n+1}
\to
L^2.
$$

Y como

$$
a_n\to L,
$$

las reglas para constantes y sumas dan

$$
2+a_n\to2+L.
$$

Pero las sucesiones

$$
(a_{n+1}^2)
$$

y

$$
(2+a_n)
$$

son idénticas término a término. Por unicidad del límite,

$$
L^2=2+L.
$$

Reordenando,

$$
L^2-L-2=0,
$$

y factorizando,

$$
(L-2)(L+1)=0.
$$

Los candidatos algebraicos son, por tanto,

$$
L=2
$$

o

$$
L=-1.
$$

Sin embargo, ya sabemos que

$$
1\le L\le2.
$$

La segunda posibilidad queda excluida. Luego

$$
\boxed{
\lim_{n\to\infty}a_n=2.
}
$$
:::

La demostración anterior es importante porque ninguna de sus piezas puede intercambiarse libremente de posición.

La ecuación

$$
L^2=L+2
$$

solo aparece **después** de saber que existe un límite $L$.

Antes de ese punto, la letra $L$ no designa todavía un objeto cuya existencia esté demostrada.

### Cómo se descubre la barrera $2$

En una demostración final conviene presentar las ideas en orden lógico. Durante la búsqueda, sin embargo, podemos trabajar hacia atrás.

Los primeros términos sugieren que $2$ podría desempeñar un papel especial. Para comprobar si es una barrera estable, preguntamos:

> si $a_n<2$, ¿la recurrencia obliga a que también $a_{n+1}<2$?

La condición buscada es

$$
\sqrt{2+a_n}<2.
$$

Como ambos lados son no negativos, podemos elevar al cuadrado y obtener la condición equivalente

$$
2+a_n<4,
$$

es decir,

$$
a_n<2.
$$

La desigualdad que queremos conservar reaparece exactamente en el lado derecho.

Este es un indicio muy fuerte de invariancia:

$$
a_n<2
\quad\Longrightarrow\quad
a_{n+1}<2.
$$

La cota no fue entonces una adivinanza gratuita. La propia recurrencia nos permite comprobar si una barrera propuesta se reproduce de un paso al siguiente.

La búsqueda de regiones invariantes suele funcionar así:

1. conjeturamos una región a partir de los primeros términos o de la forma algebraica de la regla;
2. suponemos que $a_n$ pertenece a esa región;
3. utilizamos la recurrencia para demostrar que $a_{n+1}$ vuelve a pertenecer;
4. cerramos el argumento por inducción.

### Cómo se descubre la monotonía

También podemos reconstruir la búsqueda de la desigualdad

$$
a_{n+1}>a_n.
$$

La recurrencia nos dice

$$
a_{n+1}=\sqrt{2+a_n}.
$$

Como ya sabemos que los términos son positivos, podemos comparar cuadrados:

$$
a_{n+1}>a_n
\quad\Longleftrightarrow\quad
a_{n+1}^2>a_n^2.
$$

Sustituyendo la recurrencia,

$$
2+a_n>a_n^2.
$$

Llevando todo a un lado,

$$
2+a_n-a_n^2>0.
$$

Y la factorización

$$
2+a_n-a_n^2=(2-a_n)(a_n+1)
$$

revela por qué la región invariante encontrada en el paso anterior era exactamente la información que necesitábamos.

Dentro de

$$
1\le a_n<2,
$$

ambos factores son positivos.

Así, la prueba de monotonía **reutiliza** la prueba de acotación. Las dos tareas no son independientes: encontrar una región adecuada puede proporcionar simultáneamente dominio, cotas y signo para la comparación entre términos consecutivos.

### La ecuación de punto fijo es una condición necesaria, no una prueba de convergencia

Existe un error particularmente tentador con las recurrencias.

Supongamos que escribimos

$$
x_{n+1}=F(x_n)
$$

y queremos estudiar su comportamiento. Es natural pensar:

> si $x_n\to L$, entonces también $x_{n+1}\to L$; por tanto, tal vez $L$ deba satisfacer $L=F(L)$.

La idea puede ser útil para **encontrar candidatos**, siempre que el paso algebraico utilizado para llegar a la ecuación esté justificado por resultados ya demostrados.

El error consiste en invertir la implicación:

$$
\boxed{
L=F(L)
\centernot\Longrightarrow
x_n\to L.
}
$$

Veamos un ejemplo elemental. Definamos

$$
y_0=1,
\qquad
y_{n+1}=3-y_n.
$$

Si alguien supone sin demostrar que $y_n$ tiene límite $L$, entonces el desplazamiento y el álgebra de límites obligarían a

$$
L=3-L,
$$

de donde

$$
L=\frac32.
$$

Pero calculemos los términos:

$$
y_0=1,
\qquad
y_1=2,
\qquad
y_2=1,
\qquad
y_3=2,
\qquad\dots
$$

La sucesión oscila para siempre.

Más aún, para todo $n$,

$$
\left|y_n-\frac32\right|
=
\frac12.
$$

Tomando, por ejemplo,

$$
\varepsilon=\frac14,
$$

ninguna cola satisface

$$
\left|y_n-\frac32\right|<\varepsilon.
$$

Por tanto,

$$
y_n\not\to\frac32.
$$

Y como cualquier eventual límite tendría que satisfacer necesariamente

$$
L=3-L,
$$

no existe ningún otro candidato posible. La sucesión diverge.

El número $3/2$ es un **punto fijo** de la regla

$$
F(x)=3-x,
$$

pero eso no obliga a que la órbita que comienza en $1$ se acerque a él.

La lección lógica es:

$$
\boxed{
\begin{array}{c}
\text{convergencia demostrada}\\
+\ \text{recurrencia}\\
+\ \text{leyes de límites}
\end{array}
\Longrightarrow
\text{ecuación necesaria para el límite},
}
$$

pero no al revés.

### En nuestro ejemplo no pasamos el límite «a través de la raíz»

Conviene aislar un detalle metodológico del @exm-t1-0038.

Podría resultar tentador escribir

$$
a_{n+1}=\sqrt{2+a_n}
$$

y, como $a_n\to L$, declarar inmediatamente

$$
L=\sqrt{2+L}.
$$

Ese paso sería precisamente utilizar, sin haberlo demostrado todavía, que la función

$$
x\mapsto\sqrt{x}
$$

preserva límites.

En este tratado esa propiedad pertenecerá a la teoría de continuidad posterior. No la necesitamos aquí.

En lugar de ello utilizamos la identidad algebraica

$$
a_{n+1}^2=2+a_n.
$$

Cada operación que aparece ahora —producto, suma y constante— ya tiene una ley de límites demostrada en §3.4.

Por eso la cadena legítima es

$$
\boxed{
a_n\to L
\Longrightarrow
a_{n+1}\to L
\Longrightarrow
a_{n+1}^2\to L^2
}
$$

y, simultáneamente,

$$
\boxed{
a_n\to L
\Longrightarrow
2+a_n\to2+L.
}
$$

La igualdad término a término entre ambos lados obliga entonces a

$$
L^2=2+L.
$$

No hemos apelado a continuidad de la raíz ni a un límite funcional.

### Existencia e identificación son dos problemas distintos

El ejemplo rector puede resumirse en dos bloques.

**Bloque A: demostrar existencia.**

$$
\boxed{
\begin{array}{c}
1\le a_n<2\\
a_{n+1}>a_n
\end{array}
\Longrightarrow
\text{creciente + cota superior}
\Longrightarrow
a_n\to L.
}
$$

Aquí entra la completitud a través de @thm-t1-0010.

**Bloque B: identificar el número.**

$$
\boxed{
a_n\to L
\Longrightarrow
a_{n+1}\to L
\Longrightarrow
L^2=L+2
\Longrightarrow
L\in\{-1,2\}
\Longrightarrow
L=2.
}
$$

Aquí entran la estabilidad bajo desplazamiento, el álgebra de límites y la información de orden obtenida antes.

Confundir ambos bloques produce uno de los errores más frecuentes en problemas de recurrencias.

### El protocolo reutilizable

Ante una sucesión definida por

$$
a_{n+1}=F(a_n),
$$

no buscaremos automáticamente una fórmula cerrada para $a_n$. Muchas recurrencias útiles pueden estudiarse sin ella.

El protocolo será:

$$
\boxed{
\begin{array}{c}
\text{1. bien definida}\\
\downarrow\\
\text{2. región invariante / cota}\\
\downarrow\\
\text{3. monotonía}\\
\downarrow\\
\text{4. existencia por convergencia monótona}\\
\downarrow\\
\text{5. identificación mediante desplazamiento + álgebra}
\end{array}
}
$$

No todos los problemas seguirán exactamente esta ruta. Algunas sucesiones no serán monótonas; otras necesitarán otra técnica. Pero cuando la recurrencia conserva una región y empuja los términos siempre en una misma dirección, este esquema debe ser una de las primeras estrategias que examinemos.

### Qué hemos ganado

La recurrencia

$$
a_{n+1}=\sqrt{2+a_n}
$$

nos permitió reunir por primera vez casi todas las herramientas del capítulo en una sola demostración:

- inducción para conservar una región;
- orden para construir cotas;
- comparación algebraica para demostrar monotonía;
- completitud, a través del teorema de convergencia monótona, para obtener existencia;
- estabilidad de colas y desplazamientos para pasar de $(a_n)$ a $(a_{n+1})$;
- álgebra de límites para identificar el valor final;
- control lógico para no confundir un punto fijo con una prueba de convergencia.

Esta arquitectura aparecerá muchas veces en análisis numérico, ecuaciones y procesos iterativos, aunque más adelante dispongamos de herramientas mucho más potentes.

Hasta ahora, sin embargo, todas las sucesiones convergentes del capítulo tenían un límite real finito.

La siguiente pregunta será qué lenguaje utilizar cuando los términos crecen más allá de toda cota real o disminuyen por debajo de toda cota real.

Ese será el objeto de §3.9: los **límites infinitos** y la diferencia entre escapar sistemáticamente hacia $+\infty$ o $-\infty$ y ser simplemente no acotada.

## Cuando no hay límite real: límites infinitos y divergencia {#sec-t1-c04-09}

Hasta ahora, cuando una sucesión convergía, buscábamos un número real $L$ alrededor del cual terminara concentrándose toda la cola. Pero hay sucesiones cuyo comportamiento final es ordenado y describible aunque no se acerquen a ningún número real.

El ejemplo más simple es

$$
a_n=n.
$$

Los términos

$$
0,1,2,3,\dots
$$

no se aproximan a un real fijo. Al contrario: sobrepasan cualquier barrera real que fijemos, siempre que avancemos lo suficiente.

La frase importante no es

> «los términos se hacen muy grandes»,

sino una afirmación cuantificada:

> **dada cualquier cota real que queramos superar, toda la cola termina quedando por encima de ella.**

Este patrón es análogo a la definición $\varepsilon$–$N$, pero cambia el tipo de desafío. Allí alguien fijaba una tolerancia alrededor de un candidato $L$; aquí alguien fija una barrera real $M$ que debemos superar de manera permanente.

### Superar cualquier barrera

::: {#def-t1-0031}
**Límites infinitos de una sucesión.** Sea $(a_n)_{n\ge n_0}$ una sucesión real.

Diremos que

$$
a_n\to+\infty
$$

si para todo número real $M$ existe un índice $N\ge n_0$ tal que

$$
a_n>M
$$

para todo $n\ge N$. En símbolos,

$$
\forall M\in\mathbb R\;\exists N\ge n_0\;\forall n\ge N:
\quad a_n>M.
$$

Diremos que

$$
a_n\to-\infty
$$

si para todo número real $M$ existe un índice $N\ge n_0$ tal que

$$
a_n<M
$$

para todo $n\ge N$. En símbolos,

$$
\forall M\in\mathbb R\;\exists N\ge n_0\;\forall n\ge N:
\quad a_n<M.
$$
:::

La estructura lógica debe leerse con el mismo cuidado que en la convergencia ordinaria:

$$
\boxed{
\text{barrera arbitraria}
\longrightarrow
\text{umbral adecuado}
\longrightarrow
\text{toda la cola al otro lado de la barrera}.
}
$$

Para $+\infty$, la barrera se supera por arriba. Para $-\infty$, se supera por abajo.

### El símbolo $\infty$ no nombra un número real

La notación

$$
\lim_{n\to\infty}a_n=+\infty
$$

es útil, pero debe interpretarse mediante @def-t1-0031. No significa que exista un número real llamado $+\infty$ al cual se acerquen los términos.

En particular,

$$
+\infty\notin\mathbb R,
\qquad
-\infty\notin\mathbb R.
$$

Por eso, si $a_n\to+\infty$ o $a_n\to-\infty$, la sucesión **no converge en el sentido real ordinario** de @def-t1-0028.

Hay también una razón estructural inmediata. Si $a_n\to+\infty$, entonces la sucesión no está acotada superiormente: dada cualquier supuesta cota $B$, la definición con $M=B$ produce términos tardíos mayores que $B$. Análogamente, si $a_n\to-\infty$, no está acotada inferiormente.

Pero @prp-t1-0020 demostró que toda sucesión convergente a un número real es acotada. Por tanto,

$$
\boxed{
 a_n\to\pm\infty
 \Longrightarrow
 (a_n)\text{ diverge como sucesión real.}
}
$$

La palabra **diverge**, sin embargo, es más amplia. Una sucesión puede divergir sin escapar ordenadamente hacia ninguno de los dos infinitos.

### El ejemplo básico: $n\to+\infty$

Probemos la afirmación directamente desde la propiedad arquimediana de $\mathbb R$.

Sea $M\in\mathbb R$ arbitrario. Por la propiedad arquimediana existe un número natural $N$ tal que

$$
N>M.
$$

Entonces, para todo $n\ge N$,

$$
n\ge N>M.
$$

Por consiguiente,

$$
\forall M\in\mathbb R\;\exists N\in\mathbb N\;\forall n\ge N:
\quad n>M,
$$

y por @def-t1-0031,

$$
\boxed{n\to+\infty.}
$$

El argumento muestra con precisión qué papel desempeña la arquimedianidad: garantiza que ninguna barrera real puede quedar por encima de todos los naturales.

De la misma manera,

$$
-n\to-\infty,
$$

porque dada una barrera real $M$, basta elegir $N>-M$; entonces, si $n\ge N$,

$$
-n\le -N<M.
$$

### No acotada no significa tender a infinito

Una sucesión que tiende a $+\infty$ es necesariamente no acotada superiormente. Pero la recíproca es falsa. Ser no acotada solo afirma que podemos encontrar términos arbitrariamente grandes; no dice que **todos los términos suficientemente tardíos** sean grandes.

La diferencia vuelve a estar en los cuantificadores.

No estar acotada superiormente significa

$$
\forall M\in\mathbb R\;\exists n\ge n_0:
\quad a_n>M.
$$

Tender a $+\infty$ exige mucho más:

$$
\forall M\in\mathbb R\;\exists N\ge n_0\;\forall n\ge N:
\quad a_n>M.
$$

En la primera afirmación encontramos **algún término** que supera la barrera. En la segunda encontramos **una cola completa** que queda por encima de ella.

::: {#exm-t1-0039}
**No acotación frente a límite infinito.** Consideremos

$$
a_n=(-1)^n n.
$$

La sucesión toma la forma

$$
0,-1,2,-3,4,-5,\dots
$$

Es no acotada superiormente y no acotada inferiormente. Sin embargo,

$$
a_n\not\to+\infty
$$

y

$$
a_n\not\to-\infty.
$$
:::

**No está acotada superiormente.** Sea $B\in\mathbb R$. Por arquimedianidad podemos elegir un número natural $m$ tan grande que

$$
2m>B.
$$

Para el índice par $n=2m$,

$$
a_{2m}=2m>B.
$$

Así, ninguna cota superior real puede controlar todos los términos.

**No está acotada inferiormente.** Dado $B\in\mathbb R$, elijamos $m$ con

$$
2m+1>-B.
$$

Entonces

$$
a_{2m+1}=-(2m+1)<B.
$$

Por tanto, tampoco existe una cota inferior real.

**No tiende a $+\infty$.** Fijemos la barrera

$$
M=0.
$$

Para que $a_n\to+\infty$, debería existir un índice $N$ después del cual todos los términos fueran positivos. Pero, dado cualquier $N$, podemos elegir un índice impar $n\ge N$. Para ese índice,

$$
a_n=-n<0.
$$

Así, ninguna cola queda enteramente por encima de $0$.

**No tiende a $-\infty$.** De nuevo usemos la barrera $M=0$. Dado cualquier $N$, podemos elegir un índice par $n\ge N$. Entonces

$$
a_n=n\ge0,
$$

de modo que ninguna cola queda enteramente por debajo de $0$.

La sucesión escapa a cotas arbitrariamente grandes en ambos sentidos, pero sigue cruzando una y otra vez de un lado al otro. No existe una dirección unilateral de escape.

El ejemplo separa tres ideas:

$$
\boxed{
\text{no acotada}
\not\Longrightarrow
+\infty,
\qquad
\text{no acotada}
\not\Longrightarrow
-\infty.
}
$$

### El recíproco convierte crecimiento infinito en pequeñez

Hay una conexión muy útil entre los límites infinitos y los límites reales ya estudiados. Para números positivos, afirmar que $a_n$ termina superando cualquier barrera equivale a afirmar que su recíproco termina siendo tan pequeño como queramos.

::: {#prp-t1-0024}
**Recíprocos y crecimiento hacia $+\infty$.** Sea $(a_n)_{n\ge n_0}$ una sucesión real que es eventualmente positiva. Entonces

$$
a_n\to+\infty
\quad\Longleftrightarrow\quad
\frac1{a_n}\to0.
$$
:::

**Demostración.** Supongamos primero que

$$
a_n\to+\infty.
$$

Sea $\varepsilon>0$. Como $1/\varepsilon$ es un número real, la definición de límite infinito proporciona un índice $N_1$ tal que

$$
a_n>\frac1\varepsilon
$$

para todo $n\ge N_1$.

Además, por positividad eventual existe $N_0$ tal que

$$
a_n>0
$$

para todo $n\ge N_0$.

Si

$$
N=\max\{N_0,N_1\},
$$

entonces, para $n\ge N$,

$$
0<\frac1{a_n}<\varepsilon.
$$

Por tanto,

$$
\left|\frac1{a_n}-0\right|<\varepsilon,
$$

y concluimos

$$
\frac1{a_n}\to0.
$$

Recíprocamente, supongamos que

$$
\frac1{a_n}\to0
$$

y que $a_n>0$ eventualmente. Queremos demostrar que toda barrera real termina siendo superada.

Sea $M\in\mathbb R$.

Si $M\le0$, la positividad eventual basta: existe $N_0$ tal que, para $n\ge N_0$,

$$
a_n>0\ge M.
$$

Si $M>0$, tomemos

$$
\varepsilon=\frac1M.
$$

Como $1/a_n\to0$, existe $N_1$ tal que, para todo $n\ge N_1$,

$$
\left|\frac1{a_n}\right|<\frac1M.
$$

Tomando además una cola donde $a_n>0$, obtenemos

$$
0<\frac1{a_n}<\frac1M.
$$

Como ambos lados son positivos, el orden de los recíprocos se invierte y resulta

$$
a_n>M.
$$

En ambos casos existe un umbral después del cual $a_n>M$. Como $M$ era arbitrario,

$$
a_n\to+\infty.
$$

$\blacksquare$

La hipótesis de positividad eventual no es decorativa. Sin ella, la condición

$$
\frac1{a_n}\to0
$$

solo informa que $|a_n|$ se hace grande en magnitud; no selecciona hacia qué lado de la recta escapan los términos. El ejemplo $a_n=(-1)^n n$ lo muestra de inmediato: su recíproco, a partir de $n=1$, satisface

$$
\frac1{a_n}=\frac{(-1)^n}{n}\to0,
$$

pero $(a_n)$ no tiende ni a $+\infty$ ni a $-\infty$.

Por simetría de signo, una versión análoga relaciona $a_n\to-\infty$ con $1/a_n\to0$ cuando la sucesión es eventualmente negativa. No necesitamos introducir un nuevo principio: basta aplicar el resultado anterior a $(-a_n)$.

### Divergir tiene varias formas

A esta altura conviene ordenar el vocabulario.

Una sucesión puede:

- converger a un número real $L$;
- tender a $+\infty$;
- tender a $-\infty$;
- divergir sin tener ninguno de esos comportamientos, como $(-1)^n$ o $(-1)^n n$.

Así, decir simplemente

> «la sucesión diverge»

no especifica **cómo** falla la convergencia real.

En particular,

$$
\boxed{
\text{divergente}
\not\Longrightarrow
\text{límite infinito}.
}
$$

Esta distinción será importante cuando más adelante clasifiquemos comportamientos de funciones y series.

### No haremos álgebra formal con el símbolo $\infty$

Las leyes de @prp-t1-0021 fueron demostradas para límites **reales**. No hemos demostrado todavía un cálculo general para expresiones que involucren $+\infty$ o $-\infty$.

Y no podemos obtenerlo tratando esos símbolos como números.

Por ejemplo, las tres parejas

$$
a_n=n,
\qquad
b_n=-n,
$$

$$
c_n=2n,
\qquad
b_n=-n,
$$

y

$$
a_n=n,
\qquad
d_n=-2n
$$

tienen siempre un término que tiende a $+\infty$ y otro que tiende a $-\infty$. Sin embargo,

$$
a_n+b_n=0,
$$

$$
c_n+b_n=n\to+\infty,
$$

y

$$
a_n+d_n=-n\to-\infty.
$$

Por tanto, la escritura informal

$$
+\infty+(-\infty)
$$

no determina por sí sola un resultado.

Más adelante aprenderemos a reconocer y resolver distintas **formas indeterminadas** bajo hipótesis adicionales. Por ahora basta fijar una disciplina:

$$
\boxed{
\text{los símbolos }\pm\infty\text{ se interpretan mediante definiciones cuantificadas, no mediante aritmética ficticia.}
}
$$

### Qué hemos ganado

Ya podemos distinguir cuatro niveles de comportamiento final:

$$
\boxed{
\begin{array}{c}
\text{convergencia a un real}\\[2pt]
\text{escape a }+\infty\text{ o }-\infty\\[2pt]
\text{no acotación sin dirección unilateral}\\[2pt]
\text{otras formas de divergencia}
\end{array}
}
$$

La herramienta común sigue siendo la misma: controlar **toda una cola** mediante cuantificadores.

Para un límite real, dada una tolerancia $\varepsilon>0$, toda la cola debe entrar en un intervalo alrededor de $L$.

Para $+\infty$, dada una barrera $M$, toda la cola debe quedar por encima de ella.

Para $-\infty$, dada una barrera $M$, toda la cola debe quedar por debajo.

Con esto hemos completado el repertorio conceptual principal del capítulo. En §3.10 dejaremos de introducir teoría nueva y recorreremos un laboratorio de diagnóstico: reconocer qué herramienta conviene usar, reconstruir pruebas y detectar errores lógicos antes de afrontar el banco final de ejercicios.

## Laboratorio de límites secuenciales {#sec-t1-c04-10}

Hasta aquí hemos construido las herramientas del capítulo una por una. Sabemos traducir «acercarse» a una afirmación $\varepsilon$–$N$; negar correctamente una convergencia; usar unicidad, acotación, álgebra y orden; reconocer cuándo conviene aplicar el teorema del sándwich; obtener convergencia a partir de monotonía y completitud; analizar recurrencias; y distinguir un límite real de un escape hacia $+\infty$ o $-\infty$.

Ahora cambia la tarea.

En las seis estaciones que siguen **no introduciremos teoría nueva**. El problema será decidir qué herramienta conviene usar, justificar por qué puede usarse y detectar los pasos que una solución demasiado rápida podría ocultar.

Conviene adoptar este protocolo general:

$$
\boxed{
\text{leer el objetivo}
\to
\text{identificar la estructura de la cola}
\to
\text{elegir la herramienta}
\to
\text{probar}
\to
\text{auditar hipótesis y dependencias}
}
$$

La pregunta ya no será solamente

> ¿puedo calcular este límite?,

sino también

> **¿qué teorema o definición convierte la información disponible en control de toda una cola?**

### Estación 1 — Convertir un candidato en una prueba $\varepsilon$–$N$

Consideremos

$$
a_n=\frac{4n-1}{2n+3},
\qquad n\ge0.
$$

Una manipulación informal de los términos dominantes sugiere

$$
\frac{4n-1}{2n+3}\approx\frac{4n}{2n}=2.
$$

**Problema.** Demostrar directamente desde la definición que

$$
a_n\to2,
$$

fabricando un umbral $N(\varepsilon)$ y señalando dónde aparece cada cuantificador.

#### Diagnóstico

El candidato está dado. Por tanto, la definición nos exige controlar

$$
|a_n-2|.
$$

Antes de escribir «sea $\varepsilon>0$», conviene hacer el cálculo de búsqueda: simplificar el error hasta descubrir qué condición sobre $n$ bastaría para hacerlo menor que $\varepsilon$.

#### Búsqueda del umbral

Tenemos

$$
\begin{aligned}
\left|\frac{4n-1}{2n+3}-2\right|
&=
\left|\frac{4n-1-2(2n+3)}{2n+3}\right|\\
&=
\left|\frac{-7}{2n+3}\right|\\
&=
\frac7{2n+3}.
\end{aligned}
$$

Queremos garantizar

$$
\frac7{2n+3}<\varepsilon.
$$

Sería suficiente imponer una condición un poco más fuerte y más cómoda:

$$
2n>\frac7\varepsilon,
$$

es decir,

$$
n>\frac7{2\varepsilon}.
$$

La propiedad arquimediana nos permite producir un natural que supere esa cantidad real.

#### Demostración

Sea $\varepsilon>0$ arbitrario. Por la propiedad arquimediana, elegimos $N\in\mathbb N$ tal que

$$
N>\frac7{2\varepsilon}.
$$

Sea ahora $n\ge N$. Entonces

$$
2n+3>2n\ge2N>\frac7\varepsilon.
$$

Como todas las cantidades son positivas,

$$
\frac7{2n+3}<\varepsilon.
$$

Por consiguiente,

$$
\left|\frac{4n-1}{2n+3}-2\right|<\varepsilon
$$

para todo $n\ge N$. Como $\varepsilon>0$ era arbitrario,

$$
\boxed{
\frac{4n-1}{2n+3}\to2.
}
$$

#### Lectura de la solución

La prueba contiene exactamente la arquitectura

$$
\forall\varepsilon>0
\;\exists N
\;\forall n\ge N.
$$

- El adversario lógico elige $\varepsilon$.
- Nosotros respondemos con un $N$ que puede depender de $\varepsilon$.
- Después ese mismo $N$ debe controlar **todos** los índices posteriores.

La desigualdad preliminar

$$
n>\frac7{2\varepsilon}
$$

no es todavía la demostración: es la **búsqueda** que nos permite diseñar el testigo existencial $N$.

Podríamos obtener el mismo límite más rápidamente mediante el álgebra de límites de @prp-t1-0021. Aquí hemos evitado deliberadamente ese atajo porque el objetivo de la estación era reconstruir la lógica elemental sobre la que descansa toda la teoría.

### Estación 2 — Negar una convergencia sin cambiar el orden de los cuantificadores

Sea

$$
b_n=(-1)^n+\frac1{n+1}.
$$

Algunos términos son positivos y otros negativos, y el término adicional $1/(n+1)$ se hace pequeño. Alguien podría mirar esa pequeñez y conjeturar erróneamente que

$$
b_n\to0.
$$

**Problema.** Refutar ese candidato directamente desde la negación de la definición de convergencia.

#### Diagnóstico

Para probar

$$
b_n\not\to0
$$

no debemos demostrar que «muchos términos» quedan lejos de cero. Necesitamos una tolerancia fija $\varepsilon_0>0$ que ninguna cola consiga satisfacer por completo:

$$
\exists\varepsilon_0>0
\;\forall N
\;\exists n\ge N:
|b_n|\ge\varepsilon_0.
$$

La alternancia sugiere elegir siempre un índice par suficientemente tardío.

#### Solución

Tomemos

$$
\varepsilon_0=\frac12.
$$

Sea $N\in\mathbb N$ arbitrario. Elegimos

$$
n=2N.
$$

Entonces $n$ es par y además $n\ge N$. Por tanto,

$$
(-1)^n=1,
$$

y

$$
b_n
=
1+\frac1{2N+1}
>1.
$$

En particular,

$$
|b_n|>1>\frac12=\varepsilon_0.
$$

Así, para todo umbral $N$ encontramos un índice $n\ge N$ que queda fuera del intervalo

$$
\left(-\frac12,\frac12\right).
$$

Por la negación de la definición,

$$
\boxed{b_n\not\to0.}
$$

#### Qué demuestra y qué no demuestra

La conclusión excluye **el candidato $0$**. Por sí sola no demuestra todavía que $(b_n)$ diverja, porque podría existir otro número real como límite.

Esta separación reproduce una distinción de §3.2:

$$
\boxed{
\text{refutar un candidato}
\neq
\text{refutar todos los candidatos}.
}
$$

La estación se concentra en una habilidad lógica más básica: leer correctamente

$$
\forall N\;\exists n\ge N
$$

como «por lejos que avancemos, todavía reaparece una violación», y no confundirla con

$$
\exists N\;\forall n\ge N,
$$

que expresa estabilidad de toda una cola.

### Estación 3 — Abrir una prueba algebraica y encontrar los controles ocultos

Supongamos que

$$
x_n\to2
\qquad\text{y}\qquad
y_n\to-1.
$$

El álgebra de límites permite concluir inmediatamente

$$
x_ny_n\to-2
$$

y

$$
\frac{x_n}{y_n}\to-2.
$$

Pero ahora queremos mirar **dentro** de esas dos conclusiones.

**Problema.** Reconstruir qué controles hacen posibles las pruebas del producto y del cociente. En particular:

1. explicar por qué la prueba del producto necesita una cota para uno de los factores;
2. explicar por qué la prueba del cociente necesita separar $y_n$ de cero.

#### Primera reparación: controlar el producto

La diferencia respecto del límite esperado puede escribirse como

$$
\begin{aligned}
x_ny_n-(-2)
&=x_ny_n+2\\
&=x_n(y_n+1)-(x_n-2).
\end{aligned}
$$

Por la desigualdad triangular,

$$
|x_ny_n+2|
\le
|x_n|\,|y_n+1|+|x_n-2|.
$$

Aquí aparece el punto delicado. Sabemos que

$$
|y_n+1|\to0,
$$

pero ese factor está multiplicado por $|x_n|$. Para convertir la pequeñez de $|y_n+1|$ en pequeñez del producto necesitamos impedir que $|x_n|$ crezca sin control.

Como $x_n\to2$, existe una cola en la que

$$
|x_n-2|<1.
$$

En esa cola,

$$
|x_n|
\le
|x_n-2|+2
<3.
$$

Ya tenemos la cota que faltaba.

Sea ahora $\varepsilon>0$. Elegimos índices suficientemente grandes para que simultáneamente

$$
|x_n|<3,
$$

$$
|y_n+1|<\frac\varepsilon6,
$$

y

$$
|x_n-2|<\frac\varepsilon2.
$$

Tomando el máximo de los tres umbrales correspondientes, todas las condiciones valen en una misma cola. Entonces

$$
\begin{aligned}
|x_ny_n+2|
&\le
|x_n|\,|y_n+1|+|x_n-2|\\
&<
3\frac\varepsilon6+\frac\varepsilon2\\
&=\varepsilon.
\end{aligned}
$$

Así reaparece, desde dentro de la prueba, la razón estructural por la que la convergencia implica acotación: **un factor que tiende a cero solo puede controlar un producto si el otro factor no se escapa**.

#### Segunda reparación: controlar el cociente

Ahora examinemos

$$
\frac{x_n}{y_n}.
$$

Antes de estimar el error debemos garantizar que el denominador no se acerque a cero. Como

$$
y_n\to-1,
$$

podemos exigir

$$
|y_n+1|<\frac12.
$$

Entonces

$$
-\frac32<y_n<-\frac12,
$$

y por tanto

$$
|y_n|>\frac12.
$$

En esa cola el cociente está bien definido y además

$$
\frac1{|y_n|}<2.
$$

Ahora calculamos

$$
\begin{aligned}
\left|\frac{x_n}{y_n}+2\right|
&=
\frac{|x_n+2y_n|}{|y_n|}\\
&=
\frac{|(x_n-2)+2(y_n+1)|}{|y_n|}\\
&\le
\frac{|x_n-2|+2|y_n+1|}{|y_n|}.
\end{aligned}
$$

Sea $\varepsilon>0$. En una cola común podemos exigir

$$
|y_n+1|<\frac12,
$$

$$
|x_n-2|<\frac\varepsilon4,
$$

y

$$
|y_n+1|<\frac\varepsilon8.
$$

Entonces

$$
\begin{aligned}
\left|\frac{x_n}{y_n}+2\right|
&<
2\left(\frac\varepsilon4+2\frac\varepsilon8\right)\\
&=\varepsilon.
\end{aligned}
$$

Por tanto,

$$
\frac{x_n}{y_n}\to-2.
$$

#### Lectura de la solución

Las dos pruebas tienen obstáculos diferentes:

$$
\boxed{
\begin{array}{c}
\text{producto: controlar un factor que multiplica el error;}\\[4pt]
\text{cociente: impedir que el denominador haga explotar el error.}
\end{array}
}
$$

El teorema algebraico de @prp-t1-0021 comprime estos razonamientos para reutilizarlos. Esta estación muestra qué información permanece escondida cuando escribimos simplemente «por el álgebra de límites».

### Estación 4 — Cuando la oscilación no necesita tener límite

Consideremos

$$
u_n=\frac{2\sin n-\cos n}{n+1}.
$$

**Problema.** Determinar el límite sin suponer que las sucesiones $(\sin n)$ o $(\cos n)$ tengan límite.

#### Diagnóstico

La expresión contiene dos factores oscilantes. Intentar aplicar el álgebra de límites término a término nos obligaría a conocer primero límites para $\sin n$ y $\cos n$.

Pero no necesitamos esa información.

Lo que sí sabemos es

$$
|\sin n|\le1,
\qquad
|\cos n|\le1.
$$

La pregunta correcta no es, por tanto,

> ¿a qué número se acercan el seno y el coseno?,

sino

> ¿podemos encerrar toda la expresión entre cantidades cuya magnitud tienda a cero?

Eso apunta al teorema del sándwich.

#### Solución

Por desigualdad triangular,

$$
|2\sin n-\cos n|
\le
2|\sin n|+|\cos n|
\le3.
$$

Por tanto,

$$
|u_n|
=
\frac{|2\sin n-\cos n|}{n+1}
\le
\frac3{n+1}.
$$

Ya sabemos que

$$
\frac1{n+1}\to0,
$$

así que, por multiplicación por el escalar $3$,

$$
\frac3{n+1}\to0.
$$

La forma absoluta del teorema del sándwich @prp-t1-0023 da entonces

$$
\boxed{
u_n\to0.}
$$

#### Lectura de la solución

La oscilación no fue eliminada: fue **dominada**.

$$
\boxed{
\text{factor oscilante acotado}
\times
\text{factor que tiende a }0
\longrightarrow
\text{producto que tiende a }0.
}
$$

Esta arquitectura es más importante que el ejemplo trigonométrico concreto. Cuando una parte de una expresión se resiste a tener un comportamiento simple, conviene preguntar si basta controlar su magnitud.

### Estación 5 — Detectar cuándo la completitud produce el límite

Definamos

$$
a_n=\sqrt{2-\frac1{n+1}},
\qquad n\ge0.
$$

**Problema.** Demostrar que $(a_n)$ converge y determinar su límite **sin utilizar continuidad de la raíz cuadrada**.

#### Diagnóstico

Es tentador escribir

$$
2-\frac1{n+1}\to2
$$

y después afirmar inmediatamente

$$
\sqrt{2-\frac1{n+1}}\to\sqrt2.
$$

Pero esa segunda inferencia sería precisamente una aplicación de continuidad de $x\mapsto\sqrt x$, noción que todavía no pertenece a este capítulo.

Debemos separar las dos preguntas:

1. ¿por qué existe un límite real para $(a_n)$?;
2. una vez asegurada su existencia, ¿cómo identificamos su valor usando únicamente el álgebra ya demostrada?

La forma de la sucesión sugiere que sus términos crecen y permanecen por debajo de $\sqrt2$.

#### Monotonía y cota

Para todo $n\ge0$,

$$
0<\frac1{n+1}\le1,
$$

de modo que

$$
1\le2-\frac1{n+1}<2.
$$

Por tanto,

$$
1\le a_n<\sqrt2.
$$

Así, $(a_n)$ está acotada superiormente por $\sqrt2$.

Además,

$$
\frac1{n+2}<\frac1{n+1},
$$

por lo que

$$
2-\frac1{n+2}
>
2-\frac1{n+1}.
$$

La raíz cuadrada es estrictamente creciente sobre $[0,\infty)$, de modo que

$$
a_{n+1}>a_n.
$$

La sucesión es, pues, creciente y acotada superiormente.

#### Existencia del límite

Por el teorema de convergencia monótona @thm-t1-0010, existe $L\in\mathbb R$ tal que

$$
a_n\to L.
$$

Aquí está el paso en el que actúa la completitud de $\mathbb R$: el teorema de convergencia monótona se demostró tomando el supremo de la imagen de la sucesión.

Además, como todos los términos satisfacen $a_n\ge1$, el límite producido por el teorema es no negativo; de hecho,

$$
1\le L\le\sqrt2.
$$

#### Identificación sin continuidad

La definición de $a_n$ nos da la identidad exacta

$$
a_n^2
=
2-\frac1{n+1}.
$$

Como $a_n\to L$, el álgebra de límites implica

$$
a_n^2\to L^2.
$$

Por otra parte,

$$
\frac1{n+1}\to0,
$$

y por tanto

$$
2-\frac1{n+1}\to2.
$$

Las dos sucesiones de ambos lados de la identidad son la misma término a término, así que sus límites deben coincidir. Por unicidad,

$$
L^2=2.
$$

Como $L\ge0$, la unicidad de la raíz no negativa demostrada en `T1-C02` obliga a

$$
L=\sqrt2.
$$

Concluimos

$$
\boxed{
\sqrt{2-\frac1{n+1}}
\to
\sqrt2.
}
$$

#### Dónde estaba la completitud

La prueba tiene dos capas claramente separadas:

$$
\boxed{
\text{monotonía + cota + completitud}
\to
\text{existencia de }L
\to
\text{álgebra}
\to
\text{identificación de }L.
}
$$

No hemos pasado una raíz cuadrada a través del símbolo de límite. Primero obtuvimos **existencia** mediante el orden completo de $\mathbb R$ y solo después utilizamos una identidad algebraica para averiguar quién era el límite.

### Estación 6 — Auditar una recurrencia antes de resolver su ecuación de punto fijo

Sea

$$
u_0=0,
\qquad
u_{n+1}=\frac{u_n+3}{2}.
$$

Una solución apresurada podría decir:

> «Si $u_n\to L$, entonces $L=(L+3)/2$, de donde $L=3$. Por tanto, $u_n\to3$.»

**Problema.** Localizar el fallo lógico y reparar completamente la demostración sin utilizar continuidad.

#### Diagnóstico del argumento defectuoso

La primera frase comienza con una hipótesis condicional:

$$
\text{si }u_n\to L.
$$

La ecuación

$$
L=\frac{L+3}{2}
$$

solo puede servir para **identificar un candidato después de saber que el límite existe**. Resolverla no demuestra que la sucesión converja.

La prueba correcta debe seguir el protocolo de §3.8:

$$
\boxed{
\text{bien definida}
\to
\text{región invariante}
\to
\text{monotonía}
\to
\text{existencia}
\to
\text{identificación}.
}
$$

#### Paso 1: la recurrencia está bien definida y preserva una región

Demostraremos por inducción que

$$
0\le u_n<3
$$

para todo $n\ge0$.

Para $n=0$,

$$
u_0=0,
$$

de modo que la afirmación es verdadera.

Supongamos ahora

$$
0\le u_n<3.
$$

Entonces

$$
3\le u_n+3<6,
$$

y al dividir por $2$,

$$
\frac32\le u_{n+1}<3.
$$

En particular,

$$
0\le u_{n+1}<3.
$$

Por inducción, la región $[0,3)$ es invariante bajo la recurrencia.

#### Paso 2: monotonía

Para todo $n$,

$$
\begin{aligned}
u_{n+1}-u_n
&=\frac{u_n+3}{2}-u_n\\
&=\frac{3-u_n}{2}.
\end{aligned}
$$

Como $u_n<3$,

$$
u_{n+1}-u_n>0.
$$

Así, $(u_n)$ es estrictamente creciente.

Además, la región invariante ya nos dio la cota superior

$$
u_n<3.
$$

#### Paso 3: existencia por completitud

La sucesión es creciente y acotada superiormente. Por @thm-t1-0010,

$$
u_n\to L
$$

para algún $L\in\mathbb R$.

Solo ahora tenemos derecho a buscar una ecuación para $L$.

#### Paso 4: identificación mediante desplazamiento y álgebra

Por la estabilidad bajo desplazamiento de índices @prp-t1-0019,

$$
u_{n+1}\to L.
$$

La recurrencia satisface

$$
2u_{n+1}=u_n+3.
$$

Aplicando únicamente el álgebra de límites,

$$
2L=L+3.
$$

Por tanto,

$$
L=3.
$$

Concluimos

$$
\boxed{u_n\to3.}
$$

#### Lectura de la solución

La ecuación de punto fijo era correcta; lo incorrecto era su **posición lógica** dentro del argumento.

$$
\boxed{
\text{ecuación del candidato}
\not\Longrightarrow
\text{existencia del límite}.
}
$$

El orden correcto es

$$
\boxed{
\text{probar que el límite existe}
\longrightarrow
\text{usar la recurrencia para identificarlo}.
}
$$

Esta distinción será especialmente importante más adelante, cuando las recurrencias sean suficientemente complejas como para poseer varios puntos fijos o para no converger a ninguno de ellos.

### Un mapa de decisiones para problemas de sucesiones

Las seis estaciones muestran que «calcular un límite» no designa una única técnica. Antes de hacer álgebra conviene diagnosticar qué tipo de información tenemos.

Un primer mapa puede organizarse así:

$$
\boxed{
\begin{array}{c}
\text{¿definición directa?}\\
\downarrow\\
\text{¿álgebra?}\quad\text{¿sándwich?}\quad\text{¿monotonía + cota?}\\
\downarrow\\
\text{¿recurrencia?}\quad\text{¿límite infinito?}
\end{array}
}
$$

Podemos convertirlo en preguntas operativas.

**Si nos dan un candidato real $L$**, preguntamos primero si podemos estimar directamente

$$
|a_n-L|.
$$

Cuando el error se reduce a una expresión elemental en $n$, una prueba $\varepsilon$–$N$ puede ser la ruta más transparente.

**Si la sucesión está construida a partir de otras cuyos límites ya conocemos**, el álgebra de @prp-t1-0021 puede comprimir el trabajo. Pero debemos auditar sus hipótesis: en productos aparece acotación y en cocientes el denominador debe quedar eventualmente separado de cero.

**Si aparece una oscilación acotada multiplicada por algo pequeño**, conviene buscar una desigualdad en valor absoluto y aplicar el sándwich en vez de intentar asignar un límite a cada factor.

**Si no conocemos el candidato pero la sucesión tiene una dirección de movimiento**, preguntamos si es monótona y está acotada en la dirección adecuada. Si ambas respuestas son afirmativas, la completitud puede producir el límite mediante @thm-t1-0010.

**Si la sucesión está dada por recurrencia**, no comenzamos resolviendo una ecuación de punto fijo. Primero debemos demostrar que la regla está bien definida, encontrar una región invariante o cotas, estudiar monotonía y obtener existencia. Solo después usamos desplazamiento de índices y álgebra para identificar el límite.

**Si los términos parecen crecer sin cota**, debemos distinguir no acotación de límite infinito. Para probar

$$
a_n\to+\infty
$$

o

$$
a_n\to-\infty,
$$

la definición exige superar o descender cualquier barrera con **toda una cola**, no solo con términos arbitrariamente grandes en magnitud.

**Si queremos refutar una convergencia**, buscamos una tolerancia fija que reaparezca violada arbitrariamente lejos. La estructura correcta es

$$
\exists\varepsilon_0>0
\;\forall N
\;\exists n\ge N.
$$

### Qué debe poder hacer ahora el lector

Al terminar este laboratorio, una solución completa ya no debería consistir únicamente en una cadena de manipulaciones simbólicas. Antes de calcular, debemos ser capaces de decir:

- qué afirmación cuantificada intentamos probar o negar;
- qué información pertenece solo a un prefijo y qué información controla una cola;
- si estamos usando una definición o un teorema ya demostrado;
- cuáles son las hipótesis delicadas de ese teorema;
- si la existencia del límite está demostrada o solo hemos encontrado un candidato;
- dónde entra la completitud, cuando entra;
- y qué herramientas posteriores estamos evitando para no razonar circularmente.

El capítulo comenzó preguntando cómo expresar rigurosamente lo que ocurre «a partir de algún momento y para siempre después». Después de estas seis estaciones, esa pregunta ya dispone de un repertorio de respuestas diferentes pero coordinadas:

$$
\boxed{
\begin{array}{c}
\varepsilon\text{–}N,\\
\text{álgebra y orden},\\
\text{sándwich},\\
\text{monotonía + completitud},\\
\text{recurrencias},\\
M\text{–}N\text{ para límites infinitos}.
\end{array}
}
$$

En §3.11 ese repertorio dejará de estar organizado por estaciones. El banco final mezclará reconocimiento, prueba directa, diagnóstico, contraejemplos, descubrimiento guiado y desafíos de síntesis. La tarea será elegir la herramienta adecuada sin que el enunciado anuncie de antemano cuál es.

## Ejercicios y soluciones {#sec-t1-c04-11}

Llegamos al banco final de `T1-C04`. Hasta aquí las técnicas aparecieron primero de manera aislada y después, en §3.10, como estaciones guiadas. En esta sección desaparece esa señalización: antes de comenzar una prueba habrá que decidir si el problema pide trabajar directamente con cuantificadores, usar álgebra de límites, estimar por sándwich, explotar monotonía y completitud, controlar una recurrencia o interpretar un límite infinito.

El banco contiene exactamente cuarenta ejercicios, distribuidos en siete niveles:

$$
7A+7B+7C+6D+5E+5F+3G=40.
$$

Los niveles no miden solo dificultad de cálculo. En particular, los niveles D y E obligan a distinguir afirmaciones verdaderas de recíprocas falsas, mientras que los niveles F y G exigen reconstruir por qué funcionan las herramientas del capítulo.

Todos los problemas pueden resolverse con los capítulos publicados desde los números reales hasta el presente. No se necesitan límites de funciones, continuidad, derivadas, subsucesiones, Bolzano–Weierstrass, criterio de Cauchy ni $\limsup/\liminf$.

### Nivel A — Reconocimiento y comprensión

::: {#exr-t1-0116}
<!-- CPM-T1-EXR-0116 | A | CONCEPTUAL | COMPUTATION | ORIGINAL -->
**Ejercicio A1. Índices y términos.** Sea

$$
a_n=\frac{2n+1}{n+1},
\qquad n\ge0.
$$

1. Escribe los cuatro primeros términos.
2. Identifica el término de índice $3$.
3. Explica la diferencia entre el índice $3$ y el término $a_3$.
:::

::: {#exr-t1-0117}
<!-- CPM-T1-EXR-0117 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A2. Cola y eventualidad.** Sea

$$
a_n=\frac{(-1)^n}{n+1}.
$$

Decide cuáles de las siguientes propiedades se cumplen eventualmente:

1. $|a_n|<1/10$;
2. $a_n>0$;
3. $-1/10<a_n<1/10$.

Cuando la respuesta sea afirmativa, proporciona un umbral $N$ que funcione.
:::

::: {#exr-t1-0118}
<!-- CPM-T1-EXR-0118 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A3. Tres comportamientos distintos.** Considera

$$
p_n=2-\frac1{n+1},
\qquad
q_n=(-1)^n,
\qquad
r_n=n.
$$

Para cada sucesión, indica si es acotada, si es monótona y cuál de las siguientes descripciones corresponde:

- converge a un número real;
- tiende a $+\infty$;
- diverge sin límite infinito unilateral.
:::

::: {#exr-t1-0119}
<!-- CPM-T1-EXR-0119 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A4. Leer $\varepsilon$–$N$.** Traduce a lenguaje ordinario la afirmación

$$
\forall\varepsilon>0\;\exists N\in\mathbb N\;\forall n\ge N:
|a_n-5|<\varepsilon.
$$

Después responde:

1. ¿puede $N$ depender de $\varepsilon$?;
2. ¿puede $N$ depender de un índice $n$ elegido después?;
3. ¿qué número afirma la fórmula que es el límite?
:::

::: {#exr-t1-0120}
<!-- CPM-T1-EXR-0120 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A5. Un cambio finito.** Sean

$$
a_n=\frac1{n+1}
$$

y

$$
b_n=
\begin{cases}
1000-n, & 0\le n\le50,\\[4pt]
\dfrac1{n+1}, & n>50.
\end{cases}
$$

Sin volver a demostrar el límite desde la definición, determina el límite de $(b_n)$ y explica qué resultado del capítulo estás usando.
:::

::: {#exr-t1-0121}
<!-- CPM-T1-EXR-0121 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A6. Real, infinito o ninguno.** Clasifica cada sucesión:

$$
a_n=\frac1{n+1},
\qquad
b_n=n,
\qquad
c_n=-n,
\qquad
d_n=(-1)^n.
$$

Para cada una indica si tiene límite real, límite $+\infty$, límite $-\infty$ o ninguna de esas tres posibilidades.
:::

::: {#exr-t1-0122}
<!-- CPM-T1-EXR-0122 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A7. Infinitas visitas no son una cola.** Define

$$
a_n=
\begin{cases}
0, & n\text{ par},\\
1, & n\text{ impar}.
\end{cases}
$$

1. Explica por qué hay términos arbitrariamente tardíos exactamente iguales a $0$.
2. Decide si $a_n\to0$.
3. Señala qué orden de cuantificadores distingue ambas afirmaciones.
:::

### Nivel B — Aplicación directa

::: {#exr-t1-0123}
<!-- CPM-T1-EXR-0123 | B | COMPUTATION | ORIGINAL -->
**Ejercicio B1. Álgebra de límites.** Supón que

$$
a_n\to2,
\qquad
b_n\to-1.
$$

Calcula

$$
\lim_{n\to\infty}
\frac{3a_n-2b_n}{a_n+b_n}.
$$

Justifica por qué el cociente puede tratarse con el álgebra de límites.
:::

::: {#exr-t1-0124}
<!-- CPM-T1-EXR-0124 | B | COMPUTATION | ORIGINAL -->
**Ejercicio B2. Cociente de polinomios.** Para $n\ge1$, calcula

$$
\lim_{n\to\infty}
\frac{5n^3-2n}{2n^3+n^2+1}.
$$
:::

::: {#exr-t1-0125}
<!-- CPM-T1-EXR-0125 | B | COMPUTATION | PROOF | ORIGINAL -->
**Ejercicio B3. Oscilación amortiguada.** Demuestra que

$$
\frac{2+\sin n}{n+1}\to0.
$$
:::

::: {#exr-t1-0126}
<!-- CPM-T1-EXR-0126 | B | COMPUTATION | ORIGINAL -->
**Ejercicio B4. Geométrica dentro de una expresión.** Calcula

$$
\lim_{n\to\infty}
\left(2+4\left(-\frac35\right)^n\right).
$$
:::

::: {#exr-t1-0127}
<!-- CPM-T1-EXR-0127 | B | CONCEPTUAL | PROOF | ORIGINAL -->
**Ejercicio B5. Qué preserva el orden.** Sean $(a_n)$ y $(b_n)$ sucesiones convergentes tales que

$$
a_n<b_n
$$

para todo $n$. Si

$$
a_n\to A,
\qquad
b_n\to B,
$$

¿qué relación entre $A$ y $B$ está garantizada? Da un ejemplo que muestre por qué no puede exigirse siempre una desigualdad estricta entre los límites.
:::

::: {#exr-t1-0128}
<!-- CPM-T1-EXR-0128 | B | COMPUTATION | ORIGINAL -->
**Ejercicio B6. Valor absoluto y cociente.** Supón que

$$
a_n\to-3,
\qquad
b_n\to2.
$$

Calcula

$$
\lim_{n\to\infty}\frac{|a_n|}{b_n+1}.
$$
:::

::: {#exr-t1-0129}
<!-- CPM-T1-EXR-0129 | B | PROOF | ORIGINAL -->
**Ejercicio B7. Una barrera cualquiera.** Demuestra desde la definición $M$–$N$ que

$$
2n-5\to+\infty.
$$
:::

### Nivel C — Combinación estructural

::: {#exr-t1-0130}
<!-- CPM-T1-EXR-0130 | C | PROOF | ORIGINAL -->
**Ejercicio C1. Una prueba $\varepsilon$–$N$ completa.** Demuestra directamente desde la definición que

$$
\frac{3n+1}{n+1}\to3.
$$

Tu prueba debe exhibir una elección explícita de $N(\varepsilon)$.
:::

::: {#exr-t1-0131}
<!-- CPM-T1-EXR-0131 | C | PROOF | ORIGINAL -->
**Ejercicio C2. Diseñar el umbral.** Demuestra directamente que

$$
\frac1{2n+3}\to0.
$$

Antes de escribir la prueba final, determina qué condición suficiente sobre $n$ garantiza

$$
\frac1{2n+3}<\varepsilon.
$$
:::

::: {#exr-t1-0132}
<!-- CPM-T1-EXR-0132 | C | PROOF | ORIGINAL -->
**Ejercicio C3. Convergencia y acotación visible.** Para

$$
a_n=\frac{(-1)^n}{n+1},
$$

demuestra que $a_n\to0$ mediante sándwich y encuentra además una cota global $M$ tal que

$$
|a_n|\le M
$$

para todo $n$.
:::

::: {#exr-t1-0133}
<!-- CPM-T1-EXR-0133 | C | PROOF | ORIGINAL -->
**Ejercicio C4. Sándwich racional.** Para $n\ge1$, demuestra que

$$
\frac{n}{n^2+1}\to0
$$

sin dividir numerador y denominador por $n^2$. Busca directamente una sucesión dominante sencilla.
:::

::: {#exr-t1-0134}
<!-- CPM-T1-EXR-0134 | C | PROOF | ORIGINAL -->
**Ejercicio C5. Separar un denominador de cero.** Supón que

$$
b_n\to4.
$$

1. Demuestra que existe $N$ tal que $b_n>2$ para todo $n\ge N$.
2. Deduce que $b_n\ne0$ eventualmente.
3. Concluye que
   $$
   \frac1{b_n}\to\frac14.
   $$
:::

::: {#exr-t1-0135}
<!-- CPM-T1-EXR-0135 | C | PROOF | DISCOVERY | ORIGINAL -->
**Ejercicio C6. Una geométrica desde Bernoulli.** Demuestra que

$$
\left(\frac34\right)^n\to0
$$

usando únicamente la desigualdad de Bernoulli y el teorema del sándwich.

Sugerencia: escribe

$$
\frac34=\frac1{1+h}
$$

con $h>0$.
:::

::: {#exr-t1-0136}
<!-- CPM-T1-EXR-0136 | C | PROOF | ORIGINAL -->
**Ejercicio C7. Un límite infinito desde la definición.** Demuestra que

$$
n^2\to+\infty
$$

usando directamente la definición $M$–$N$.
:::

### Nivel D — Inversión y diagnóstico

En cada ejercicio decide si la afirmación es verdadera. Si es falsa, construye un contraejemplo y verifica las propiedades relevantes.

::: {#exr-t1-0137}
<!-- CPM-T1-EXR-0137 | D | COUNTEREXAMPLE | CONCEPTUAL | ORIGINAL -->
**Ejercicio D1. «Acotada implica convergente».** Decide si toda sucesión real acotada converge.
:::

::: {#exr-t1-0138}
<!-- CPM-T1-EXR-0138 | D | COUNTEREXAMPLE | CONCEPTUAL | ORIGINAL -->
**Ejercicio D2. «Convergente implica monótona».** Decide si toda sucesión real convergente es monótona.
:::

::: {#exr-t1-0139}
<!-- CPM-T1-EXR-0139 | D | COUNTEREXAMPLE | CONCEPTUAL | ORIGINAL -->
**Ejercicio D3. «No acotada implica límite infinito».** Decide si toda sucesión no acotada satisface

$$
a_n\to+\infty
$$

o

$$
a_n\to-\infty.
$$
:::

::: {#exr-t1-0140}
<!-- CPM-T1-EXR-0140 | D | COUNTEREXAMPLE | CONCEPTUAL | ORIGINAL -->
**Ejercicio D4. Cuadrados convergentes.** Decide si

$$
a_n^2\text{ converge}
\quad\Longrightarrow\quad
a_n\text{ converge}.
$$
:::

::: {#exr-t1-0141}
<!-- CPM-T1-EXR-0141 | D | COUNTEREXAMPLE | PROOF | ORIGINAL -->
**Ejercicio D5. Diferencias sucesivas pequeñas.** Decide si

$$
a_{n+1}-a_n\to0
\quad\Longrightarrow\quad
a_n\text{ converge}.
$$
:::

::: {#exr-t1-0142}
<!-- CPM-T1-EXR-0142 | D | COUNTEREXAMPLE | CONCEPTUAL | ORIGINAL -->
**Ejercicio D6. El punto fijo no garantiza convergencia.** Una sucesión satisface

$$
y_0=0,
\qquad
y_{n+1}=3-y_n.
$$

La ecuación de punto fijo

$$
L=3-L
$$

tiene la solución $L=3/2$. Decide si $(y_n)$ converge y explica qué error lógico cometeríamos al concluir convergencia solo a partir de esa ecuación.
:::

### Nivel E — Contraejemplos construidos

::: {#exr-t1-0143}
<!-- CPM-T1-EXR-0143 | E | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio E1. Acotada y divergente.** Construye una sucesión que permanezca en el intervalo $[0,2]$ y no converja a ningún número real. Verifica ambas afirmaciones.
:::

::: {#exr-t1-0144}
<!-- CPM-T1-EXR-0144 | E | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio E2. Convergente pero no monótona.** Construye una sucesión que converja a $1$ y no sea monótona. Demuestra las dos propiedades.
:::

::: {#exr-t1-0145}
<!-- CPM-T1-EXR-0145 | E | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio E3. No acotada sin escape unilateral.** Construye una sucesión no acotada que no tienda ni a $+\infty$ ni a $-\infty$. Justifica las tres afirmaciones.
:::

::: {#exr-t1-0146}
<!-- CPM-T1-EXR-0146 | E | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio E4. Un prefijo arbitrariamente largo no decide el límite.** Sea $M\in\mathbb N$ arbitrario. Construye dos sucesiones $(a_n)$ y $(b_n)$ tales que

$$
a_n=b_n
\qquad
\text{para }0\le n\le M,
$$

pero cuyos límites reales sean distintos.
:::

::: {#exr-t1-0147}
<!-- CPM-T1-EXR-0147 | E | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio E5. Infinitamente cerca y, sin embargo, divergente.** Construye una sucesión que tenga términos arbitrariamente tardíos exactamente iguales a $0$, pero que no converja a $0$. Verifica la negación $\varepsilon$–$N$.
:::

### Nivel F — Descubrimiento guiado

::: {#exr-t1-0148}
<!-- CPM-T1-EXR-0148 | F | DISCOVERY | PROOF | ORIGINAL -->
**Ejercicio F1. Reconstruir $1/(n+1)\to0$.** Completa el siguiente programa.

1. Parte de
   $$
   \frac1{n+1}<\varepsilon.
   $$
   ¿Qué desigualdad suficiente sobre $n$ aparece al invertir?
2. Usa la propiedad arquimediana para producir un natural que satisfaga esa desigualdad.
3. Reescribe el argumento en el orden
   $$
   \varepsilon\to N\to n\ge N\to |a_n|<\varepsilon.
   $$
:::

::: {#exr-t1-0149}
<!-- CPM-T1-EXR-0149 | F | DISCOVERY | PROOF | ORIGINAL -->
**Ejercicio F2. Descubrir la estimación del producto.** Sean

$$
a_n\to A,
\qquad
b_n\to B.
$$

Reconstruye una prueba de

$$
a_nb_n\to AB
$$

siguiendo estas pistas:

1. suma y resta $a_nB$;
2. demuestra primero que $(a_n)$ está eventualmente acotada;
3. obtiene una estimación de
   $$
   |a_nb_n-AB|
   $$
   mediante dos errores;
4. elige tolerancias para que cada error contribuya menos que $\varepsilon/2$.
:::

::: {#exr-t1-0150}
<!-- CPM-T1-EXR-0150 | F | DISCOVERY | PROOF | ORIGINAL -->
**Ejercicio F3. Descubrir el límite geométrico.** Sea $q$ real con $0<q<1$.

1. Escribe
   $$
   q=\frac1{1+h}
   $$
   con $h>0$.
2. Usa Bernoulli para demostrar
   $$
   0<q^n\le\frac1{1+nh}.
   $$
3. Demuestra que el término de la derecha tiende a $0$.
4. Concluye $q^n\to0$ por sándwich.
5. Explica cómo se extiende el resultado a $-1<q<0$.
:::

::: {#exr-t1-0151}
<!-- CPM-T1-EXR-0151 | F | DISCOVERY | PROOF | ORIGINAL -->
**Ejercicio F4. Una recurrencia completa.** Define

$$
a_0=0,
\qquad
a_{n+1}=\frac{a_n+4}{2}.
$$

Demuestra, en este orden:

1. que $0\le a_n<4$ para todo $n$;
2. que $(a_n)$ es creciente;
3. que converge por el teorema de convergencia monótona;
4. que su límite es $4$, usando desplazamiento de índices y álgebra de límites.
:::

::: {#exr-t1-0152}
<!-- CPM-T1-EXR-0152 | F | DISCOVERY | PROOF | ORIGINAL -->
**Ejercicio F5. Reconstruir convergencia monótona.** Sea $(a_n)$ creciente y acotada superiormente, y define

$$
S=\{a_n:n\ge n_0\},
\qquad
L=\sup S.
$$

Usando únicamente la caracterización aproximativa del supremo y la monotonía, demuestra que $a_n\to L$. Señala exactamente dónde se utilizó la completitud de $\mathbb R$.
:::

### Nivel G — Desafíos de síntesis

::: {#exr-t1-0153}
<!-- CPM-T1-EXR-0153 | G | SYNTHESIS | PROOF | ORIGINAL -->
**Ejercicio G1. Intervalos encajados y sándwich secuencial.** Sea

$$
I_n=[a_n,b_n],
\qquad n\ge0,
$$

una sucesión de intervalos cerrados no vacíos tal que

$$
I_{n+1}\subseteq I_n
$$

para todo $n$ y

$$
b_n-a_n\to0.
$$

1. Demuestra que existe un único $L\in\mathbb R$ perteneciente a todos los intervalos.
2. Demuestra que
   $$
   a_n\to L,
   \qquad
   b_n\to L.
   $$
3. Si $(x_n)$ satisface $x_n\in[a_n,b_n]$ para todo $n$, demuestra que $x_n\to L$.
:::

::: {#exr-t1-0154}
<!-- CPM-T1-EXR-0154 | G | SYNTHESIS | PROOF | ORIGINAL -->
**Ejercicio G2. Método de Herón sin derivadas ni continuidad.** Sea $a>0$ y elige

$$
x_0>\sqrt a.
$$

Define

$$
x_{n+1}
=
\frac12\left(x_n+\frac{a}{x_n}\right).
$$

Demuestra que:

1. la sucesión está bien definida;
2. para todo $n$,
   $$
   \sqrt a\le x_{n+1}\le x_n;
   $$
3. $(x_n)$ converge;
4. su límite es $\sqrt a$.

La identificación final debe utilizar únicamente desplazamiento de índices y álgebra de límites.
:::

::: {#exr-t1-0155}
<!-- CPM-T1-EXR-0155 | G | SYNTHESIS | COUNTEREXAMPLE | PROOF | ORIGINAL -->
**Ejercicio G3. Diferencias pequeñas no bastan.** Define

$$
a_n=\sqrt{n+1}.
$$

1. Demuestra que
   $$
   a_n\to+\infty.
   $$
2. Demuestra que
   $$
   a_{n+1}-a_n
   =
   \frac1{\sqrt{n+2}+\sqrt{n+1}}
   \to0.
   $$
3. Explica con precisión qué afirmación falsa destruye este ejemplo.
:::

### Soluciones

Las soluciones siguen exactamente el orden de los ejercicios. En los niveles A–C se hace visible la herramienta utilizada; en D–G se insiste en la arquitectura lógica, la verificación de contraejemplos y la frontera de no circularidad del capítulo.

#### Soluciones del nivel A

::: {#sol-t1-0116}
<!-- CPM-T1-SOL-0116 -->
**Solución A1.**

Sustituyendo $n=0,1,2,3$ obtenemos

$$
a_0=1,
\qquad
a_1=\frac32,
\qquad
a_2=\frac53,
\qquad
a_3=\frac74.
$$

Por tanto, el término de índice $3$ es

$$
a_3=\frac74.
$$

El número $3$ es una **entrada** de la función que define la sucesión; pertenece al dominio de índices. El número $7/4$ es la **salida** asociada a esa entrada. En símbolos,

$$
a(3)=a_3=\frac74.
$$
:::

::: {#sol-t1-0117}
<!-- CPM-T1-SOL-0117 -->
**Solución A2.**

Como

$$
|a_n|=\frac1{n+1},
$$

si $n\ge10$, entonces

$$
|a_n|
=
\frac1{n+1}
\le
\frac1{11}
<
\frac1{10}.
$$

Así, la primera propiedad se cumple eventualmente; por ejemplo, $N=10$ funciona.

La segunda propiedad no se cumple eventualmente. Para cualquier $N$ existe un índice impar $n\ge N$, y entonces

$$
a_n<0.
$$

La tercera propiedad equivale a

$$
|a_n|<\frac1{10},
$$

de modo que también se cumple eventualmente con $N=10$.
:::

::: {#sol-t1-0118}
<!-- CPM-T1-SOL-0118 -->
**Solución A3.**

Para

$$
p_n=2-\frac1{n+1},
$$

el término $1/(n+1)$ disminuye hacia $0$, de modo que $(p_n)$ es creciente. Además,

$$
1\le p_n<2.
$$

Por tanto es acotada y, usando el álgebra de límites,

$$
p_n\to2.
$$

La sucesión

$$
q_n=(-1)^n
$$

está acotada por $|q_n|=1$, pero alterna entre $1$ y $-1$, así que no es monótona ni converge a un real. Tampoco tiende a $+\infty$ ni a $-\infty$, pues continúa tomando ambos valores.

Finalmente,

$$
r_n=n
$$

es creciente, no está acotada superiormente y satisface

$$
r_n\to+\infty.
$$

En resumen:

| Sucesión | Acotada | Monótona | Comportamiento |
|---|---:|---:|---|
| $(p_n)$ | sí | creciente | $p_n\to2$ |
| $(q_n)$ | sí | no | divergente, sin límite infinito |
| $(r_n)$ | no | creciente | $r_n\to+\infty$ |
:::

::: {#sol-t1-0119}
<!-- CPM-T1-SOL-0119 -->
**Solución A4.**

La fórmula dice:

> cualquiera que sea la tolerancia positiva $\varepsilon$, existe un índice $N$ tal que todos los términos con índice $n\ge N$ están a distancia menor que $\varepsilon$ de $5$.

Sí, $N$ puede depender de la tolerancia:

$$
N=N(\varepsilon).
$$

No puede depender de un índice $n$ elegido **después**, porque el orden de los cuantificadores es

$$
\forall\varepsilon\;\exists N\;\forall n\ge N.
$$

Primero se fija $\varepsilon$, después se elige un único $N$, y ese mismo $N$ debe controlar todos los índices posteriores.

La fórmula afirma exactamente que

$$
a_n\to5.
$$
:::

::: {#sol-t1-0120}
<!-- CPM-T1-SOL-0120 -->
**Solución A5.**

Para todo $n>50$,

$$
a_n=b_n.
$$

Las dos sucesiones coinciden eventualmente. Por @prp-t1-0019, la convergencia y el límite no cambian al modificar una cantidad finita de términos.

Como

$$
a_n=\frac1{n+1}\to0,
$$

se sigue inmediatamente que

$$
\boxed{b_n\to0.}
$$

Los valores iniciales de $(b_n)$ pueden ser grandes e irregulares; no intervienen en el comportamiento de su cola.
:::

::: {#sol-t1-0121}
<!-- CPM-T1-SOL-0121 -->
**Solución A6.**

Tenemos:

$$
\frac1{n+1}\to0,
$$

así que $(a_n)$ tiene límite real $0$.

Por la propiedad arquimediana,

$$
n\to+\infty,
$$

de modo que $(b_n)$ tiene límite infinito positivo.

Análogamente,

$$
-n\to-\infty,
$$

de modo que $(c_n)$ tiene límite infinito negativo.

Finalmente,

$$
d_n=(-1)^n
$$

alterna entre $1$ y $-1$. No converge a un real y tampoco puede superar eventualmente toda barrera ni quedar eventualmente por debajo de toda barrera. Por tanto no tiene límite real ni límite infinito unilateral.
:::

::: {#sol-t1-0122}
<!-- CPM-T1-SOL-0122 -->
**Solución A7.**

Para todo $N$ podemos encontrar un índice par $n\ge N$. En ese índice,

$$
a_n=0.
$$

Por tanto,

$$
\forall N\;\exists n\ge N:\ a_n=0.
$$

Sin embargo, $a_n\not\to0$. Tomemos, por ejemplo,

$$
\varepsilon_0=\frac12.
$$

Para todo $N$ existe un índice impar $n\ge N$, y entonces

$$
|a_n-0|=1\ge\frac12.
$$

Así,

$$
\exists\varepsilon_0>0\;
\forall N\;
\exists n\ge N:
|a_n|\ge\varepsilon_0,
$$

que es precisamente la negación de la convergencia a $0$.

La diferencia lógica es

$$
\forall N\;\exists n\ge N
$$

frente a

$$
\exists N\;\forall n\ge N.
$$

La primera expresa reaparición arbitrariamente tardía; la segunda, control de toda una cola.
:::

#### Soluciones del nivel B

::: {#sol-t1-0123}
<!-- CPM-T1-SOL-0123 -->
**Solución B1.**

Por el álgebra de límites,

$$
3a_n-2b_n
\to
3\cdot2-2(-1)
=
8,
$$

y

$$
a_n+b_n\to2+(-1)=1.
$$

Como el límite del denominador es distinto de cero, el denominador queda eventualmente separado de cero y podemos aplicar la ley del cociente. Por tanto,

$$
\boxed{
\frac{3a_n-2b_n}{a_n+b_n}\to8.
}
$$
:::

::: {#sol-t1-0124}
<!-- CPM-T1-SOL-0124 -->
**Solución B2.**

Dividimos numerador y denominador por $n^3$:

$$
\frac{5n^3-2n}{2n^3+n^2+1}
=
\frac{5-\dfrac2{n^2}}
{2+\dfrac1n+\dfrac1{n^3}}.
$$

Las potencias recíprocas satisfacen

$$
\frac1n\to0,
\qquad
\frac1{n^2}\to0,
\qquad
\frac1{n^3}\to0.
$$

Así, el numerador tiende a $5$ y el denominador a $2\ne0$. Por la ley del cociente,

$$
\boxed{
\frac{5n^3-2n}{2n^3+n^2+1}\to\frac52.
}
$$
:::

::: {#sol-t1-0125}
<!-- CPM-T1-SOL-0125 -->
**Solución B3.**

Como

$$
-1\le\sin n\le1,
$$

tenemos

$$
1\le2+\sin n\le3.
$$

Para todo $n\ge0$,

$$
0
\le
\frac{2+\sin n}{n+1}
\le
\frac3{n+1}.
$$

Y

$$
\frac3{n+1}\to0.
$$

Por el teorema del sándwich,

$$
\boxed{
\frac{2+\sin n}{n+1}\to0.
}
$$
:::

::: {#sol-t1-0126}
<!-- CPM-T1-SOL-0126 -->
**Solución B4.**

Como

$$
\left|-\frac35\right|<1,
$$

el resultado geométrico @cor-t1-0008 da

$$
\left(-\frac35\right)^n\to0.
$$

Por el álgebra de límites,

$$
2+4\left(-\frac35\right)^n
\to
2+4\cdot0
=
2.
$$

Por tanto,

$$
\boxed{
\lim_{n\to\infty}
\left(2+4\left(-\frac35\right)^n\right)=2.
}
$$
:::

::: {#sol-t1-0127}
<!-- CPM-T1-SOL-0127 -->
**Solución B5.**

De

$$
a_n<b_n
$$

para todo $n$ se sigue, en particular,

$$
a_n\le b_n
$$

eventualmente. Por @prp-t1-0022,

$$
\boxed{A\le B.}
$$

No podemos concluir necesariamente $A<B$. Por ejemplo, tomemos

$$
a_n=0,
\qquad
b_n=\frac1{n+1}.
$$

Entonces

$$
a_n<b_n
$$

para todo $n$, pero

$$
a_n\to0,
\qquad
b_n\to0.
$$

La desigualdad estricta de los términos puede colapsar a igualdad en el límite.
:::

::: {#sol-t1-0128}
<!-- CPM-T1-SOL-0128 -->
**Solución B6.**

Por @cor-t1-0007,

$$
|a_n|\to|-3|=3.
$$

Además,

$$
b_n+1\to2+1=3.
$$

Como $3\ne0$, podemos aplicar la ley del cociente:

$$
\boxed{
\frac{|a_n|}{b_n+1}\to\frac33=1.
}
$$
:::

::: {#sol-t1-0129}
<!-- CPM-T1-SOL-0129 -->
**Solución B7.**

Debemos demostrar que para todo $M\in\mathbb R$ existe $N$ tal que

$$
n\ge N
\quad\Longrightarrow\quad
2n-5>M.
$$

Sea $M\in\mathbb R$. Por la propiedad arquimediana podemos elegir $N\in\mathbb N$ tal que

$$
N>\frac{M+5}{2}.
$$

Si $n\ge N$, entonces

$$
2n-5
\ge
2N-5
>
M.
$$

Por tanto,

$$
\forall M\in\mathbb R\;
\exists N\;
\forall n\ge N:
2n-5>M,
$$

y concluimos

$$
\boxed{2n-5\to+\infty.}
$$
:::

#### Soluciones del nivel C

::: {#sol-t1-0130}
<!-- CPM-T1-SOL-0130 -->
**Solución C1.**

Queremos controlar

$$
\left|
\frac{3n+1}{n+1}-3
\right|.
$$

Simplificando,

$$
\left|
\frac{3n+1-3n-3}{n+1}
\right|
=
\frac2{n+1}.
$$

Sea $\varepsilon>0$. Por la propiedad arquimediana elegimos $N\in\mathbb N$ tal que

$$
N>\frac2\varepsilon.
$$

Si $n\ge N$, entonces

$$
n+1>N>\frac2\varepsilon,
$$

y por tanto

$$
\left|
\frac{3n+1}{n+1}-3
\right|
=
\frac2{n+1}
<
\varepsilon.
$$

Como $\varepsilon>0$ era arbitrario,

$$
\boxed{
\frac{3n+1}{n+1}\to3.
}
$$
:::

::: {#sol-t1-0131}
<!-- CPM-T1-SOL-0131 -->
**Solución C2.**

En la fase de búsqueda queremos

$$
\frac1{2n+3}<\varepsilon.
$$

Sería suficiente exigir

$$
2n>\frac1\varepsilon,
$$

es decir,

$$
n>\frac1{2\varepsilon}.
$$

Ahora escribimos la prueba en el orden lógico correcto.

Sea $\varepsilon>0$. Por la propiedad arquimediana elegimos $N\in\mathbb N$ tal que

$$
N>\frac1{2\varepsilon}.
$$

Si $n\ge N$, entonces

$$
2n+3
>
2N
>
\frac1\varepsilon.
$$

Todas las cantidades son positivas, de modo que al tomar recíprocos obtenemos

$$
\frac1{2n+3}<\varepsilon.
$$

Por consiguiente,

$$
\boxed{
\frac1{2n+3}\to0.
}
$$
:::

::: {#sol-t1-0132}
<!-- CPM-T1-SOL-0132 -->
**Solución C3.**

Para todo $n$,

$$
|a_n|
=
\frac1{n+1}.
$$

Así,

$$
-\frac1{n+1}
\le
a_n
\le
\frac1{n+1}.
$$

Como

$$
-\frac1{n+1}\to0
\qquad\text{y}\qquad
\frac1{n+1}\to0,
$$

el teorema del sándwich da

$$
\boxed{a_n\to0.}
$$

Además,

$$
|a_n|
=
\frac1{n+1}
\le1
$$

para todo $n\ge0$. Por tanto, una cota global válida es

$$
\boxed{M=1.}
$$

Este ejemplo hace visible que una sucesión puede oscilar y, sin embargo, converger.
:::

::: {#sol-t1-0133}
<!-- CPM-T1-SOL-0133 -->
**Solución C4.**

Para $n\ge1$ tenemos

$$
n^2+1\ge n^2>0.
$$

Por tanto,

$$
0
\le
\frac{n}{n^2+1}
\le
\frac{n}{n^2}
=
\frac1n.
$$

Y

$$
\frac1n\to0.
$$

Por el teorema del sándwich,

$$
\boxed{
\frac{n}{n^2+1}\to0.
}
$$

La ventaja de esta ruta es que no necesitamos reescribir el cociente completo: basta reconocer una cota dominante cuyo límite ya conocemos.
:::

::: {#sol-t1-0134}
<!-- CPM-T1-SOL-0134 -->
**Solución C5.**

Como

$$
b_n\to4,
$$

podemos utilizar en la definición la tolerancia

$$
\varepsilon=2.
$$

Existe entonces $N$ tal que, para todo $n\ge N$,

$$
|b_n-4|<2.
$$

Esto equivale a

$$
2<b_n<6.
$$

En particular,

$$
b_n>2
$$

para todo $n\ge N$. Por tanto, $b_n$ queda eventualmente separado de cero y, en particular,

$$
b_n\ne0
$$

eventualmente.

Ahora podemos aplicar la ley del cociente a la sucesión constante $1$ y a $(b_n)$:

$$
\frac1{b_n}
\to
\frac14.
$$

Así,

$$
\boxed{\frac1{b_n}\to\frac14.}
$$
:::

::: {#sol-t1-0135}
<!-- CPM-T1-SOL-0135 -->
**Solución C6.**

Escribimos

$$
\frac34
=
\frac1{1+\frac13}.
$$

Así, con

$$
h=\frac13>0,
$$

tenemos

$$
\left(\frac34\right)^n
=
\frac1{(1+h)^n}.
$$

Por la desigualdad de Bernoulli,

$$
(1+h)^n\ge1+nh.
$$

Por tanto,

$$
0
<
\left(\frac34\right)^n
\le
\frac1{1+n/3}
=
\frac3{n+3}.
$$

Ahora,

$$
0\le\frac3{n+3}\le\frac3{n+1},
$$

y

$$
\frac3{n+1}\to0.
$$

De nuevo por sándwich,

$$
\frac3{n+3}\to0.
$$

Aplicando una vez más el sándwich,

$$
\boxed{
\left(\frac34\right)^n\to0.
}
$$
:::

::: {#sol-t1-0136}
<!-- CPM-T1-SOL-0136 -->
**Solución C7.**

Sea $M\in\mathbb R$. Definimos

$$
R=\max\{1,M\}.
$$

Por la propiedad arquimediana elegimos $N\in\mathbb N$ tal que

$$
N>R.
$$

Si $n\ge N$, entonces $n\ge1$, de modo que

$$
n^2\ge n\ge N>R\ge M.
$$

Así,

$$
\forall M\in\mathbb R\;
\exists N\;
\forall n\ge N:
n^2>M.
$$

Por definición,

$$
\boxed{n^2\to+\infty.}
$$
:::

#### Soluciones del nivel D

::: {#sol-t1-0137}
<!-- CPM-T1-SOL-0137 -->
**Solución D1.**

La afirmación es falsa.

Tomemos

$$
a_n=(-1)^n.
$$

La sucesión está acotada porque

$$
|a_n|=1
$$

para todo $n$.

Sin embargo, no converge. Como se demostró en @exm-t1-0033, la alternancia entre $1$ y $-1$ impide que una cola completa quede dentro de una tolerancia suficientemente pequeña alrededor de cualquier real.

Por tanto,

$$
\boxed{
\text{acotada}\not\Longrightarrow\text{convergente}.
}
$$
:::

::: {#sol-t1-0138}
<!-- CPM-T1-SOL-0138 -->
**Solución D2.**

La afirmación es falsa.

Consideremos

$$
a_n=\frac{(-1)^n}{n+1}.
$$

Como

$$
|a_n|\le\frac1{n+1}
$$

y $1/(n+1)\to0$, el teorema del sándwich da

$$
a_n\to0.
$$

Pero la sucesión no es monótona. Por ejemplo,

$$
a_0=1,
\qquad
a_1=-\frac12,
\qquad
a_2=\frac13.
$$

Primero disminuye y luego aumenta. Por tanto no es creciente ni decreciente.

Así,

$$
\boxed{
\text{convergente}\not\Longrightarrow\text{monótona}.
}
$$
:::

::: {#sol-t1-0139}
<!-- CPM-T1-SOL-0139 -->
**Solución D3.**

La afirmación es falsa.

Sea

$$
a_n=(-1)^n n.
$$

La sucesión no está acotada: en los índices pares toma valores positivos arbitrariamente grandes y en los impares valores negativos de magnitud arbitrariamente grande.

No tiende a $+\infty$. Basta elegir la barrera $M=0$. Después de cualquier umbral $N$ existe un índice impar $n\ge N$, y entonces

$$
a_n=-n<0=M.
$$

Tampoco tiende a $-\infty$. Con la barrera $M=0$ en la definición correspondiente, después de cualquier $N$ existe un índice par $n\ge N$ con

$$
a_n=n>0.
$$

Por tanto,

$$
\boxed{
\text{no acotada}
\not\Longrightarrow
a_n\to+\infty\text{ o }a_n\to-\infty.
}
$$
:::

::: {#sol-t1-0140}
<!-- CPM-T1-SOL-0140 -->
**Solución D4.**

La afirmación es falsa.

Tomemos

$$
a_n=(-1)^n.
$$

Entonces

$$
a_n^2=1
$$

para todo $n$, de modo que

$$
a_n^2\to1.
$$

Sin embargo, $(a_n)$ diverge porque alterna entre $1$ y $-1$.

Así,

$$
\boxed{
a_n^2\text{ convergente}
\not\Longrightarrow
a_n\text{ convergente}.
}
$$

El cuadrado ha borrado la información de signo responsable de la oscilación.
:::

::: {#sol-t1-0141}
<!-- CPM-T1-SOL-0141 -->
**Solución D5.**

La afirmación es falsa.

Tomemos

$$
a_n=\sqrt{n+1}.
$$

Primero observemos que

$$
a_{n+1}-a_n
=
\sqrt{n+2}-\sqrt{n+1}.
$$

Racionalizando,

$$
a_{n+1}-a_n
=
\frac1{\sqrt{n+2}+\sqrt{n+1}}.
$$

Como el denominador es al menos $\sqrt{n+1}$,

$$
0
<
a_{n+1}-a_n
\le
\frac1{\sqrt{n+1}}.
$$

Además,

$$
\sqrt{n+1}\to+\infty,
$$

y por @prp-t1-0024,

$$
\frac1{\sqrt{n+1}}\to0.
$$

Por sándwich,

$$
a_{n+1}-a_n\to0.
$$

Pero la propia sucesión satisface

$$
a_n=\sqrt{n+1}\to+\infty,
$$

así que no converge a ningún real.

Por tanto,

$$
\boxed{
a_{n+1}-a_n\to0
\not\Longrightarrow
a_n\text{ convergente}.
}
$$
:::

::: {#sol-t1-0142}
<!-- CPM-T1-SOL-0142 -->
**Solución D6.**

Calculamos los primeros términos:

$$
y_0=0,
\qquad
y_1=3,
\qquad
y_2=0,
\qquad
y_3=3,
\qquad\dots
$$

Por inducción,

$$
y_{2k}=0,
\qquad
y_{2k+1}=3.
$$

La sucesión no converge: por ejemplo, respecto del candidato $3/2$, todos sus términos están a distancia

$$
\left|0-\frac32\right|
=
\left|3-\frac32\right|
=
\frac32.
$$

La ecuación

$$
L=3-L
$$

solo responde a la pregunta:

> si la sucesión convergiera y pudiéramos identificar el límite mediante la recurrencia, ¿qué valor tendría que satisfacer?

La respuesta es $L=3/2$. Pero la existencia del límite nunca fue demostrada.

Así,

$$
\boxed{
L=F(L)\text{ identifica candidatos; no demuestra convergencia}.
}
$$
:::

#### Soluciones del nivel E

::: {#sol-t1-0143}
<!-- CPM-T1-SOL-0143 -->
**Solución E1.**

Una construcción sencilla es

$$
a_n=
\begin{cases}
0, & n\text{ par},\\
2, & n\text{ impar}.
\end{cases}
$$

Claramente,

$$
0\le a_n\le2
$$

para todo $n$, así que la sucesión está acotada y permanece en $[0,2]$.

Demostremos que no converge. Supongamos que $a_n\to L$. Como hay términos pares e impares arbitrariamente tardíos, una cola tendría que contener valores $0$ y $2$ simultáneamente.

Más directamente, por la desigualdad triangular,

$$
2
=
|2-0|
\le
|2-L|+|L|.
$$

Por tanto, al menos una de las cantidades $|L|$ y $|2-L|$ es mayor o igual que $1$. Tomemos $\varepsilon_0=1$. Después de cualquier $N$ podemos elegir un índice de la paridad que produce ese valor y obtener

$$
|a_n-L|\ge1.
$$

Así no existe límite real.
:::

::: {#sol-t1-0144}
<!-- CPM-T1-SOL-0144 -->
**Solución E2.**

Podemos tomar

$$
a_n
=
1+\frac{(-1)^n}{n+1}.
$$

Como

$$
\frac{(-1)^n}{n+1}\to0,
$$

el álgebra de límites da

$$
\boxed{a_n\to1.}
$$

No es monótona. En efecto,

$$
a_0=2,
\qquad
a_1=\frac12,
\qquad
a_2=\frac43.
$$

De $a_0>a_1<a_2$ vemos que la dirección cambia ya en los primeros pasos. Por tanto, la sucesión converge a $1$ pero no es monótona.
:::

::: {#sol-t1-0145}
<!-- CPM-T1-SOL-0145 -->
**Solución E3.**

Definamos

$$
a_n=
\begin{cases}
n, & n\text{ par},\\
-n, & n\text{ impar}.
\end{cases}
$$

La sucesión no está acotada superiormente, porque para cualquier $M$ podemos elegir un índice par suficientemente grande con $n>M$. Tampoco está acotada inferiormente, porque los índices impares producen valores $-n$ arbitrariamente negativos.

No tiende a $+\infty$: con la barrera $M=0$, después de todo umbral reaparece un índice impar con $a_n<0$.

No tiende a $-\infty$: después de todo umbral reaparece un índice par con $a_n>0$.

Así, la sucesión es no acotada pero no posee límite infinito unilateral.
:::

::: {#sol-t1-0146}
<!-- CPM-T1-SOL-0146 -->
**Solución E4.**

Fijemos un $M\in\mathbb N$ arbitrario y definamos

$$
a_n=0
$$

para todo $n$, mientras que

$$
b_n=
\begin{cases}
0, & 0\le n\le M,\\
1, & n>M.
\end{cases}
$$

Entonces

$$
a_n=b_n
$$

para todos los índices del prefijo $0,\dots,M$.

Sin embargo,

$$
a_n\to0,
$$

porque es constante igual a $0$, mientras que

$$
b_n\to1,
$$

porque a partir de $M+1$ es constante igual a $1$.

Como $M$ era arbitrario, podemos hacer el prefijo común tan largo como queramos. Ninguna cantidad finita de términos iniciales determina por sí sola el límite.
:::

::: {#sol-t1-0147}
<!-- CPM-T1-SOL-0147 -->
**Solución E5.**

Tomemos

$$
a_n=
\begin{cases}
0, & n\text{ par},\\
1, & n\text{ impar}.
\end{cases}
$$

Para todo $N$ existe un índice par $n\ge N$, así que hay términos arbitrariamente tardíos exactamente iguales a $0$.

Pero $a_n\not\to0$. Fijemos

$$
\varepsilon_0=\frac12.
$$

Para todo $N$ existe un índice impar $n\ge N$, y entonces

$$
|a_n-0|
=
1
\ge
\frac12.
$$

Por tanto,

$$
\exists\varepsilon_0>0\;
\forall N\;
\exists n\ge N:
|a_n|\ge\varepsilon_0.
$$

Esta es la negación exacta de $a_n\to0$.
:::

#### Soluciones del nivel F

::: {#sol-t1-0148}
<!-- CPM-T1-SOL-0148 -->
**Solución F1.**

Queremos demostrar

$$
\frac1{n+1}\to0.
$$

La búsqueda comienza con

$$
\frac1{n+1}<\varepsilon.
$$

Como ambos lados son positivos, esto queda garantizado si

$$
n+1>\frac1\varepsilon.
$$

Es suficiente, por ejemplo, pedir

$$
n>\frac1\varepsilon.
$$

Sea ahora $\varepsilon>0$. Por la propiedad arquimediana elegimos $N\in\mathbb N$ tal que

$$
N>\frac1\varepsilon.
$$

Si $n\ge N$, entonces

$$
n+1
\ge
N+1
>
N
>
\frac1\varepsilon.
$$

Al tomar recíprocos,

$$
\frac1{n+1}<\varepsilon.
$$

Así,

$$
\forall\varepsilon>0\;
\exists N\;
\forall n\ge N:
\left|\frac1{n+1}-0\right|<\varepsilon,
$$

y por definición,

$$
\boxed{\frac1{n+1}\to0.}
$$

La fase de búsqueda fue hacia atrás; la prueba final respeta el orden de cuantificadores.
:::

::: {#sol-t1-0149}
<!-- CPM-T1-SOL-0149 -->
**Solución F2.**

Partimos de

$$
a_nb_n-AB.
$$

Sumamos y restamos $a_nB$:

$$
a_nb_n-AB
=
a_n(b_n-B)+B(a_n-A).
$$

Por la desigualdad triangular,

$$
|a_nb_n-AB|
\le
|a_n|\,|b_n-B|
+
|B|\,|a_n-A|.
$$

Necesitamos controlar $|a_n|$. Como $a_n\to A$, tomando $\varepsilon=1$ existe $N_0$ tal que, para $n\ge N_0$,

$$
|a_n-A|<1.
$$

Entonces

$$
|a_n|
\le
|a_n-A|+|A|
<
1+|A|.
$$

Definamos

$$
K=1+|A|>0.
$$

Dado $\varepsilon>0$, como $b_n\to B$, existe $N_1$ tal que

$$
|b_n-B|
<
\frac{\varepsilon}{2K}
$$

para $n\ge N_1$.

Para el segundo término distinguimos solo una pequeña comodidad técnica. Definimos

$$
C=|B|+1>0.
$$

Como $a_n\to A$, existe $N_2$ tal que

$$
|a_n-A|
<
\frac{\varepsilon}{2C}
$$

para $n\ge N_2$.

Si

$$
n\ge N=\max\{N_0,N_1,N_2\},
$$

entonces

$$
\begin{aligned}
|a_nb_n-AB|
&\le
|a_n|\,|b_n-B|
+
|B|\,|a_n-A|\\
&<
K\frac{\varepsilon}{2K}
+
|B|\frac{\varepsilon}{2C}\\
&\le
\frac\varepsilon2+\frac\varepsilon2
=
\varepsilon,
\end{aligned}
$$

porque $|B|/C\le1$.

Por tanto,

$$
\boxed{a_nb_n\to AB.}
$$

La cota eventual no es un adorno: es lo que impide que el factor $|a_n|$ destruya el control del error $|b_n-B|$.
:::

::: {#sol-t1-0150}
<!-- CPM-T1-SOL-0150 -->
**Solución F3.**

Sea $0<q<1$. Definimos

$$
h=\frac1q-1.
$$

Como $q<1$ y $q>0$,

$$
h>0,
$$

y

$$
q=\frac1{1+h}.
$$

Entonces

$$
q^n=\frac1{(1+h)^n}.
$$

Por Bernoulli,

$$
(1+h)^n\ge1+nh.
$$

Como todas las cantidades son positivas,

$$
0<q^n\le\frac1{1+nh}.
$$

Para ver que el término de la derecha tiende a $0$, observemos que para $n\ge1$,

$$
0<
\frac1{1+nh}
\le
\frac1{nh}
=
\frac1h\frac1n.
$$

Como $1/n\to0$, el sándwich da

$$
\frac1{1+nh}\to0.
$$

Aplicando sándwich una vez más,

$$
\boxed{q^n\to0.}
$$

Si ahora

$$
-1<q<0,
$$

entonces $|q|\in(0,1)$ y

$$
|q^n|=|q|^n\to0.
$$

La forma absoluta del sándwich implica

$$
q^n\to0.
$$

Así recuperamos el resultado completo para $|q|<1$.
:::

::: {#sol-t1-0151}
<!-- CPM-T1-SOL-0151 -->
**Solución F4.**

La recurrencia es

$$
a_0=0,
\qquad
a_{n+1}=\frac{a_n+4}{2}.
$$

**1. Región invariante.** Demostraremos por inducción que

$$
0\le a_n<4.
$$

Para $n=0$,

$$
a_0=0.
$$

Supongamos

$$
0\le a_n<4.
$$

Entonces

$$
4\le a_n+4<8,
$$

y al dividir por $2$,

$$
2\le a_{n+1}<4.
$$

En particular,

$$
0\le a_{n+1}<4.
$$

Por inducción, la afirmación vale para todo $n$.

**2. Monotonía.** Tenemos

$$
a_{n+1}-a_n
=
\frac{4-a_n}{2}.
$$

Como $a_n<4$,

$$
a_{n+1}-a_n>0.
$$

Por tanto, $(a_n)$ es estrictamente creciente.

**3. Existencia del límite.** La sucesión es creciente y está acotada superiormente por $4$. Por @thm-t1-0010 existe $L\in\mathbb R$ tal que

$$
a_n\to L.
$$

**4. Identificación.** Por @prp-t1-0019,

$$
a_{n+1}\to L.
$$

La recurrencia puede escribirse como

$$
2a_{n+1}=a_n+4.
$$

Usando solo el álgebra de límites,

$$
2L=L+4.
$$

Por tanto,

$$
\boxed{L=4.}
$$

En consecuencia,

$$
\boxed{a_n\to4.}
$$
:::

::: {#sol-t1-0152}
<!-- CPM-T1-SOL-0152 -->
**Solución F5.**

Sea

$$
S=\{a_n:n\ge n_0\}.
$$

Como la sucesión está acotada superiormente, $S$ es no vacío y acotado superiormente. La **completitud** de $\mathbb R$ garantiza la existencia de

$$
L=\sup S\in\mathbb R.
$$

Este es el punto exacto donde entra la completitud.

Sea ahora $\varepsilon>0$. Como $L$ es el supremo, el número

$$
L-\varepsilon
$$

no puede ser una cota superior de $S$. Por la caracterización aproximativa del supremo existe un índice $N$ tal que

$$
a_N>L-\varepsilon.
$$

Como la sucesión es creciente, para todo $n\ge N$,

$$
a_n\ge a_N.
$$

Y como $L$ es cota superior de $S$,

$$
a_n\le L.
$$

Por tanto, para todo $n\ge N$,

$$
L-\varepsilon
<
a_N
\le
a_n
\le
L
<
L+\varepsilon.
$$

Esto implica

$$
|a_n-L|<\varepsilon.
$$

Como $\varepsilon>0$ era arbitrario,

$$
\boxed{a_n\to L=\sup S.}
$$

La arquitectura de la prueba es

$$
\boxed{
\text{completitud}
\to
L=\sup S
\to
\text{un término cerca de }L
\to
\text{monotonía}
\to
\text{toda la cola cerca de }L.
}
$$
:::

#### Soluciones del nivel G

::: {#sol-t1-0153}
<!-- CPM-T1-SOL-0153 -->
**Solución G1.**

Como

$$
I_{n+1}\subseteq I_n,
$$

los intervalos están encajados. Además, cada $I_n$ es cerrado, no vacío y está contenido en $I_0$, que es acotado. Por el principio de intervalos cerrados encajados demostrado en `T1-C02`, existe al menos un punto

$$
L\in\bigcap_{n=0}^{\infty}I_n.
$$

Demostremos que es único. Si $L$ y $K$ pertenecieran a todos los intervalos, entonces para todo $n$,

$$
|L-K|\le b_n-a_n.
$$

Como

$$
b_n-a_n\to0,
$$

el sándwich implicaría que la sucesión constante $|L-K|$ tiene límite $0$. Por unicidad del límite,

$$
|L-K|=0,
$$

y por tanto

$$
L=K.
$$

Así, la intersección contiene exactamente un punto.

Ahora, como $L\in[a_n,b_n]$,

$$
0\le L-a_n\le b_n-a_n.
$$

El extremo derecho tiende a $0$, luego por sándwich

$$
L-a_n\to0.
$$

Por el álgebra de límites,

$$
\boxed{a_n\to L.}
$$

Análogamente,

$$
0\le b_n-L\le b_n-a_n,
$$

de modo que

$$
\boxed{b_n\to L.}
$$

Finalmente, si

$$
x_n\in[a_n,b_n],
$$

entonces tanto $x_n$ como $L$ pertenecen al mismo intervalo $[a_n,b_n]$. Por tanto,

$$
|x_n-L|
\le
b_n-a_n.
$$

Como el lado derecho tiende a $0$, la forma absoluta del teorema del sándwich da

$$
\boxed{x_n\to L.}
$$

El argumento integra dos manifestaciones de completitud: el principio de intervalos encajados produce el punto común y el lenguaje secuencial permite demostrar que toda elección dentro de los intervalos converge hacia él.
:::

::: {#sol-t1-0154}
<!-- CPM-T1-SOL-0154 -->
**Solución G2.**

Sea $a>0$ y

$$
x_0>\sqrt a>0.
$$

Demostraremos simultáneamente que todos los términos están bien definidos y permanecen por encima de $\sqrt a$.

Supongamos que

$$
x_n\ge\sqrt a>0.
$$

Entonces $x_n\ne0$, por lo que

$$
x_{n+1}
=
\frac12\left(x_n+\frac a{x_n}\right)
$$

está bien definido.

Además,

$$
\begin{aligned}
x_{n+1}-\sqrt a
&=
\frac12\left(x_n+\frac a{x_n}-2\sqrt a\right)\\
&=
\frac{x_n^2-2x_n\sqrt a+a}{2x_n}\\
&=
\frac{(x_n-\sqrt a)^2}{2x_n}
\ge0.
\end{aligned}
$$

Por tanto,

$$
x_{n+1}\ge\sqrt a.
$$

Como $x_0>\sqrt a$, la inducción muestra que todos los términos están definidos y satisfacen

$$
x_n\ge\sqrt a>0.
$$

Ahora comparemos términos consecutivos:

$$
\begin{aligned}
x_n-x_{n+1}
&=
x_n-\frac12\left(x_n+\frac a{x_n}\right)\\
&=
\frac{x_n^2-a}{2x_n}.
\end{aligned}
$$

Como $x_n\ge\sqrt a$,

$$
x_n^2\ge a,
$$

y por tanto

$$
x_n-x_{n+1}\ge0.
$$

Así,

$$
\boxed{\sqrt a\le x_{n+1}\le x_n}
$$

para todo $n$.

La sucesión es decreciente y está acotada inferiormente por $\sqrt a$. Por el teorema de convergencia monótona existe $L\in\mathbb R$ tal que

$$
x_n\to L.
$$

Además,

$$
L\ge\sqrt a>0.
$$

Para identificar $L$ no usamos continuidad. Multiplicamos la recurrencia por $2x_n$:

$$
2x_nx_{n+1}=x_n^2+a.
$$

Por estabilidad ante desplazamientos,

$$
x_{n+1}\to L.
$$

El álgebra de límites da entonces

$$
2L^2=L^2+a.
$$

Por tanto,

$$
L^2=a.
$$

Como $L\ge0$ y $\sqrt a$ es la raíz no negativa de $a$,

$$
\boxed{L=\sqrt a.}
$$

Así,

$$
\boxed{x_n\to\sqrt a.}
$$
:::

::: {#sol-t1-0155}
<!-- CPM-T1-SOL-0155 -->
**Solución G3.**

Sea

$$
a_n=\sqrt{n+1}.
$$

**1. Límite infinito.** Debemos probar que toda barrera real es superada por una cola.

Sea $M\in\mathbb R$. Definimos

$$
M_+=\max\{M,0\}.
$$

Por la propiedad arquimediana existe $N\in\mathbb N$ tal que

$$
N>M_+^2.
$$

Si $n\ge N$, entonces

$$
n+1>N>M_+^2.
$$

Como ambos lados son no negativos,

$$
\sqrt{n+1}>M_+\ge M.
$$

Por definición,

$$
\boxed{a_n\to+\infty.}
$$

**2. Diferencias sucesivas.** Racionalizando,

$$
\begin{aligned}
a_{n+1}-a_n
&=
\sqrt{n+2}-\sqrt{n+1}\\
&=
\frac{(n+2)-(n+1)}
{\sqrt{n+2}+\sqrt{n+1}}\\
&=
\frac1{\sqrt{n+2}+\sqrt{n+1}}.
\end{aligned}
$$

Como

$$
\sqrt{n+2}+\sqrt{n+1}
\ge
\sqrt{n+1},
$$

tenemos

$$
0
<
a_{n+1}-a_n
\le
\frac1{\sqrt{n+1}}.
$$

Ya demostramos que

$$
\sqrt{n+1}\to+\infty
$$

y la sucesión es positiva. Por @prp-t1-0024,

$$
\frac1{\sqrt{n+1}}\to0.
$$

El teorema del sándwich da

$$
\boxed{a_{n+1}-a_n\to0.}
$$

**3. Diagnóstico.** El ejemplo destruye la afirmación

$$
\boxed{
a_{n+1}-a_n\to0
\quad\Longrightarrow\quad
a_n\text{ converge}.
}
$$

Que los pasos consecutivos se hagan arbitrariamente pequeños solo controla la distancia **local** entre términos vecinos. No impide que la sucesión continúe avanzando indefinidamente en una misma dirección. Aquí los incrementos tienden a cero mientras la sucesión completa escapa hacia $+\infty$.
:::

### Auditoría del banco

El banco contiene exactamente cuarenta ejercicios y cuarenta soluciones:

$$
\boxed{
\text{EXR }0116\text{--}0155
\qquad\leftrightarrow\qquad
\text{SOL }0116\text{--}0155.
}
$$

La distribución por niveles es

$$
\boxed{
7A+7B+7C+6D+5E+5F+3G=40.
}
$$

Las seis afirmaciones de diagnóstico del nivel D quedan cubiertas explícitamente:

- acotada $\Rightarrow$ convergente;
- convergente $\Rightarrow$ monótona;
- no acotada $\Rightarrow$ límite infinito unilateral;
- $a_n^2$ convergente $\Rightarrow a_n$ convergente;
- $a_{n+1}-a_n\to0\Rightarrow a_n$ convergente;
- ecuación de punto fijo $\Rightarrow$ convergencia de la recurrencia.

Los niveles E–G añaden construcción de contraejemplos, reconstrucción de pruebas fundamentales y síntesis entre completitud, orden, sándwich, recurrencias y límites infinitos.

Ninguna solución utiliza límites funcionales, continuidad, IVT/EVT, derivadas, regla de l'Hôpital, subsucesiones, Bolzano–Weierstrass, criterio de Cauchy ni $\limsup/\liminf$.

Con este banco queda cerrado el primer capítulo del tratado dedicado a una noción rigurosa de límite. El paso siguiente ya no será una nueva técnica de sucesiones: en `T1-C05` la misma arquitectura de tolerancias y cuantificadores se trasladará al estudio del límite de una función real.
