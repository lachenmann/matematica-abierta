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

Ese será el paso de §4.2: transformar la intuición

$$
\text{«$a_n$ se acerca a $L$»}
$$

en una afirmación cuantificada que pueda demostrarse línea por línea.

