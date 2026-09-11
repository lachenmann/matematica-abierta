## §2. Nombres para números: constantes y variables

En la sección anterior aprendimos a mirar una expresión antes de calcularla. Distinguimos su estructura, identificamos subexpresiones y separamos la expresión escrita del valor que representa.

Hasta ahora, sin embargo, casi todos nuestros símbolos han sido números concretos:

$$
3,\qquad 7,\qquad 24,\qquad 5^2.
$$

El álgebra comienza a adquirir una potencia distinta cuando podemos hablar de números **sin decidir de antemano cuáles son**.

Considera primero la suma

$$
3+3+3+3.
$$

Podemos escribirla de forma más compacta como

$$
4\cdot3.
$$

Ahora imagina que queremos describir la misma situación, pero no sabemos todavía cuál es el número que se repite cuatro veces.

Podemos darle un nombre:

$$
x+x+x+x.
$$

Como es habitual en álgebra, escribiremos

$$
4x
$$

en lugar de

$$
4\cdot x.
$$

Así, la escritura $4x$ representa cuatro veces el número representado por $x$.

La letra $x$ nos permite conservar la estructura del cálculo sin fijar todavía un valor concreto.

Pero aquí aparece una pregunta decisiva:

::: {.ma-block .ma-metodo}
**Pregunta**

¿Qué significa exactamente la letra $x$?
:::

Una respuesta habitual sería:

> «$x$ es una incógnita».

Otra:

> «$x$ es una variable».

Y otra, todavía más frecuente:

> «una variable es una letra que cambia».

Las tres frases pueden resultar útiles en ciertos contextos, pero ninguna explica por sí sola qué está ocurriendo.

En matemáticas, **el significado de una letra depende del contexto en que se usa**.

Esa será la idea central de esta sección.

---

### 2.1 Una letra puede ser un nombre

Comencemos con una situación muy sencilla.

Supongamos que decimos:

> Sea $a$ el número $7$.

A partir de ese momento, dentro de esa discusión,

$$
a=7.
$$

Entonces podemos escribir:

$$
a+5
$$

en lugar de

$$
7+5.
$$

Y podemos calcular:

$$
a+5=12.
$$

Aquí la letra $a$ no está «cambiando». Tampoco representa un número misterioso. Simplemente estamos usando un símbolo como **nombre** de un número que hemos fijado.

Lo mismo ocurre cuando una fórmula científica usa letras para ciertas cantidades ya determinadas en un problema, o cuando una demostración da nombres a varios objetos para poder hablar de ellos con claridad.

La primera lección es, por tanto:

$$
\boxed{
\text{una letra en matemáticas no tiene un significado único por sí sola}.
}
$$

Necesitamos saber cómo ha sido introducida.

---

### 2.2 Una letra puede representar un número desconocido

Considera ahora:

> Pensamos en un número, pero todavía no sabemos cuál es. Lo llamaremos $x$.

Si sabemos además que al sumarle $5$ obtenemos $12$, podemos escribir:

$$
x+5=12.
$$

Aquí la situación es distinta.

La letra $x$ representa un número que suponemos determinado, pero cuyo valor todavía no conocemos.

En este contexto es natural llamarla **incógnita**.

Obsérvese la diferencia:

#### Primer contexto

> Sea $x=7$.

El valor está fijado y conocido.

#### Segundo contexto

> $x+5=12$.

El valor está fijado por la situación, pero todavía debemos determinarlo.

La misma letra $x$ puede aparecer en ambos casos. Por eso su significado no procede de la forma del símbolo, sino de su uso.

::: {.ma-block .ma-intuicion}
**Idea clave**

Una letra no «nace» siendo incógnita, variable o constante. Su papel matemático está determinado por el contexto.
:::

La teoría sistemática de ecuaciones y de sus soluciones vendrá mucho más adelante. Aquí solo queremos aprender a leer correctamente la situación.

---

### 2.3 Una letra puede representar un número arbitrario

Existe un tercer uso todavía más importante para las matemáticas puras.

Considera la afirmación informal:

> El doble de un número más el doble de otro número es igual al doble de su suma.

Podemos escribir:

$$
2a+2b=2(a+b).
$$

Aquí no estamos buscando valores especiales de $a$ y $b$.

Tampoco hemos decidido que:

$$
a=3,
\qquad
b=5.
$$

Queremos que las letras puedan representar números cualesquiera dentro del contexto en que estemos trabajando.

Si probamos, por ejemplo,

$$
a=3,\qquad b=5,
$$

obtenemos:

$$
2\cdot3+2\cdot5=2(3+5),
$$

es decir,

$$
6+10=16.
$$

Pero el ejemplo numérico no es lo que da significado a la escritura original. Las letras permiten expresar de una sola vez un patrón que no depende de haber elegido precisamente $3$ y $5$.

Este uso de letras será fundamental durante todo el libro.

Más adelante aprenderemos a expresar con precisión frases como:

> «para cualquier número $a$...»

o

> «existe un número $x$ tal que...».

Para hacerlo necesitaremos cuantificadores y lenguaje lógico. Todavía no los introduciremos.

---

### 2.4 ¿Qué es una constante?

En una discusión matemática solemos distinguir entre cantidades cuyo valor consideramos fijado y cantidades que pueden asumir distintos valores permitidos.

::: {.ma-block .ma-definicion #apm-t1-c01-d0002}
**Definición — Constante**

En un contexto dado, una **constante** es una cantidad o un símbolo cuyo valor se considera fijo durante la discusión.
:::

La expresión «en un contexto dado» es esencial.

Por ejemplo, supongamos que estudiamos:

$$
ax+3.
$$

Si el problema comienza diciendo:

> Sea $a=5$,

entonces $a$ se considera constante en esa discusión:

$$
ax+3=5x+3.
$$

También los números escritos directamente,

$$
3,\qquad -2,\qquad \frac12,
$$

actúan como valores constantes.

En matemáticas aparecen además constantes especiales a las que se asignan nombres convencionales, como:

$$
\pi
$$

o

$$
e,
$$

aunque su estudio pertenece a otros contextos.

Lo importante aquí es comprender que «constante» describe un **papel dentro de una discusión**, no necesariamente una forma tipográfica.

Una letra puede representar una constante.

---

### 2.5 ¿Qué es una variable?

Ahora podemos formular una primera definición operativa.

::: {.ma-block .ma-definicion #apm-t1-c01-d0003}
**Definición — Variable**

En un contexto dado, una **variable** es un símbolo cuyo valor no se fija de una vez para toda la discusión y que puede representar distintos valores permitidos por ese contexto.
:::

Esta definición todavía será refinada más adelante.

Por ahora nos permite evitar una frase demasiado pobre:

> «una variable es una letra que cambia».

¿Por qué es insuficiente?

Porque el símbolo no se mueve ni se transforma por sí mismo. Además, en muchos argumentos podemos elegir un valor para una variable y mantenerlo fijo durante varias líneas.

Por ejemplo, si consideramos la expresión:

$$
x+4
$$

y decidimos examinar qué ocurre cuando

$$
x=10,
$$

durante ese cálculo usamos un valor fijo:

$$
x+4=10+4=14.
$$

Eso no hace que $x$ deje de pertenecer al papel de variable en la expresión general $x+4$.

Lo importante es que la expresión admite distintos valores de $x$ en distintas evaluaciones:

$$
x=1,\qquad x=10,\qquad x=-3,\ldots
$$

La idea central es, por tanto:

$$
\boxed{
\text{variable}
\neq
\text{letra que físicamente «cambia»};
}
$$

una variable es un símbolo cuyo valor puede variar **dentro de las posibilidades que el contexto admite**.

---

### 2.6 El contexto decide el papel

Comparemos tres situaciones con la misma letra $x$.

#### Situación A — valor fijado

> Sea $x=4$.

Entonces:

$$
x+3
$$

representa, en esa discusión,

$$
4+3.
$$

Aquí $x$ tiene un valor fijado.

#### Situación B — valor desconocido

> Un número $x$ satisface

$$
x+3=7.
$$

Aquí $x$ representa un valor que la situación pretende determinar, pero que todavía no hemos identificado.

#### Situación C — valor variable

Consideramos la expresión:

$$
x+3
$$

para distintos valores permitidos de $x$.

Podemos examinar:

$$
1+3,\qquad 5+3,\qquad (-2)+3,\ldots
$$

Aquí $x$ funciona como variable.

Los tres contextos utilizan exactamente el mismo símbolo:

$$
x.
$$

Sin embargo, el papel que desempeña no es el mismo.

::: {.ma-block .ma-observacion}
**Ejemplo**

**Un mismo símbolo, tres papeles**

El símbolo $x$ no contiene internamente las instrucciones «soy una incógnita» o «soy una variable». Es la frase matemática que lo rodea la que determina cómo debemos interpretarlo.
:::

Esta observación será muy importante cuando nuestras fórmulas contengan muchas letras.

---

### 2.7 No todas las letras cumplen el mismo papel en una fórmula

Consideremos:

$$
ax+b.
$$

Sin contexto adicional no sabemos qué papel desempeña cada letra.

Podría ocurrir que:

- $a$ y $b$ estén fijados;
- $x$ pueda tomar distintos valores.

Por ejemplo, si:

$$
a=2,\qquad b=5,
$$

entonces estamos estudiando:

$$
2x+5.
$$

En ese contexto, $a$ y $b$ han quedado fijados, mientras que $x$ continúa siendo la cantidad cuyo valor podemos variar.

Pero otro problema podría fijar $x$ y permitir que cambie $a$.

Por eso no debemos intentar deducir el papel de una letra únicamente por su posición.

Más adelante introduciremos otros nombres para ciertos papeles especiales —por ejemplo, el de **parámetro**—, pero todavía no los necesitamos.

---

### 2.8 Las letras permiten expresar patrones

¿Por qué introducir letras en lugar de trabajar siempre con números?

Porque permiten separar una estructura general de un caso particular.

Considera:

$$
3(4+5)=3\cdot4+3\cdot5.
$$

Esta igualdad muestra un caso concreto.

Pero:

$$
a(b+c)=ab+ac
$$

muestra el patrón de una sola vez.

No necesitamos todavía formular rigurosamente para qué valores se afirma esa igualdad ni demostrarla desde axiomas. Lo importante es advertir lo que las letras hacen posible:

$$
\boxed{
\text{las letras permiten representar familias de casos mediante una sola escritura}.
}
$$

Esta capacidad de expresar patrones es una de las razones por las que el álgebra es mucho más que una técnica para «encontrar $x$».

---

## Ejercicios

### ¿Qué papel tiene la letra? {#apm-t1-c01-e0006}

En cada situación, explica el papel que desempeña la letra.

#### a)

> Sea $a=9$. Consideremos $a+4$.

#### b)

> Pensamos en un número $n$ que satisface $n+2=10$.

#### c)

> Consideremos $x+5$ para distintos valores de $x$.

#### Solución

#### a)

La letra $a$ tiene un valor fijado:

$$
a=9.
$$

Dentro de esta discusión actúa como nombre de una cantidad constante.

Por tanto,

$$
a+4
$$

representa:

$$
9+4.
$$

#### b)

La letra $n$ representa un número cuyo valor no se ha identificado todavía, aunque la condición

$$
n+2=10
$$

pretende determinarlo.

En este contexto es natural describir $n$ como una incógnita.

No necesitamos resolver la ecuación para reconocer ese papel.

#### c)

Aquí $x$ está destinado a representar distintos valores en distintas evaluaciones de la expresión:

$$
x+5.
$$

Por tanto, $x$ desempeña el papel de variable.

---

### La misma letra en contextos distintos {#apm-t1-c01-e0007}

Explica por qué no podemos afirmar, sin contexto, que la letra $x$ «es una incógnita».

Compara:

1. «Sea $x=12$».
2. «$x+4=12$».
3. «Estudiemos $x+4$ para distintos valores de $x$».

#### Solución

En la primera frase,

$$
x=12,
$$

el valor de $x$ está fijado y conocido.

En la segunda,

$$
x+4=12,
$$

$x$ representa un valor que todavía no conocemos y que la condición pretende determinar.

En la tercera, $x$ puede representar distintos valores permitidos.

Por tanto, el símbolo $x$ no posee un papel fijo por el simple hecho de ser una letra. El contexto determina su interpretación.

---

### Constantes y variable en una expresión {#apm-t1-c01-e0008}

Supongamos que:

$$
a=3,
\qquad
b=-1,
$$

y que en la expresión

$$
ax+b
$$

la letra $x$ puede tomar distintos valores.

1. ¿Qué letras tienen valores fijados?
2. ¿Qué letra funciona como variable?
3. Reescribe la expresión usando los valores fijados de $a$ y $b$.

#### Solución

Los valores de $a$ y $b$ están fijados:

$$
a=3,
\qquad
b=-1.
$$

Por tanto, dentro de este contexto actúan como constantes.

La letra $x$ puede tomar distintos valores, de modo que funciona como variable.

Sustituyendo únicamente los valores fijados obtenemos:

$$
ax+b
=
3x+(-1).
$$

Podemos escribir de manera más usual:

$$
3x-1.
$$

No hemos asignado ningún valor concreto a $x$.

---

### De un patrón verbal a una expresión {#apm-t1-c01-e0009}

Usa una letra para escribir cada descripción.

#### a)

El triple de un número.

#### b)

Un número aumentado en $7$.

#### c)

Cuatro veces un número, más $2$.

#### d)

La suma de dos números que no hemos fijado.

#### Solución

#### a)

Si llamamos $x$ al número:

$$
3x.
$$

#### b)

Si llamamos $x$ al número:

$$
x+7.
$$

#### c)

Si llamamos $x$ al número:

$$
4x+2.
$$

#### d)

Necesitamos dos símbolos, por ejemplo $a$ y $b$:

$$
a+b.
$$

No hay nada especial en las letras elegidas. Podríamos haber usado otros símbolos, siempre que dejáramos claro qué representan.

---

### ¿Qué información falta? {#apm-t1-c01-e0010}

Considera la expresión:

$$
a+2x.
$$

Un estudiante afirma:

> «$a$ es una constante y $x$ es una variable».

¿Podemos saberlo solo observando la expresión?

#### Solución

No.

La escritura

$$
a+2x
$$

nos muestra cómo se combinan los símbolos, pero no nos informa por sí sola de qué valores están fijados y cuáles pueden variar.

Por ejemplo, un contexto podría decir:

> Sea $a=5$ y permita que $x$ tome distintos valores.

Entonces $a$ actuaría como constante y $x$ como variable.

Pero otro contexto podría fijar $x$ y permitir distintos valores de $a$.

Por tanto, necesitamos información adicional.

La conclusión es:

$$
\boxed{
\text{el papel de una letra no puede determinarse siempre por su apariencia o posición}.
}
$$

---

## Resumen de la sección

Las letras son una herramienta para nombrar y representar números sin tener que escribir siempre un valor concreto.

Hemos visto que una misma letra puede desempeñar papeles diferentes.

Puede representar:

- un valor fijado y conocido;
- un valor fijado pero todavía desconocido;
- distintos valores permitidos dentro de una discusión.

Por eso evitaremos la definición escolar:

> «una variable es una letra que cambia».

Las dos definiciones fundamentales de esta sección son:

::: {.ma-block .ma-observacion}
**Síntesis**

**Constante:** en un contexto dado, una cantidad o símbolo cuyo valor se considera fijo durante la discusión.

**Variable:** en un contexto dado, un símbolo cuyo valor no se fija de una vez para toda la discusión y que puede representar distintos valores permitidos por ese contexto.
:::

La frase que debemos conservar es:

$$
\boxed{
\text{el contexto determina el papel del símbolo}.
}
$$

Y hemos descubierto además una de las grandes ventajas del lenguaje algebraico:

$$
\boxed{
\text{una sola expresión puede representar un patrón de muchos casos}.
}
$$

---

## Hacia la sección siguiente

Ya podemos leer expresiones que contienen números y letras:

$$
x+3,
$$

$$
2x+5,
$$

$$
a(b+c),
$$

$$
\frac{a+b}{3}.
$$

Pero ahora aparece una nueva dificultad.

¿Qué partes forman una expresión como

$$
2x^2-5x+1?
$$

¿Qué significa llamar «término» a una parte y «factor» a otra?

¿En qué se diferencia una expresión como

$$
x+3
$$

de una escritura como

$$
x+3=7?
$$

Para avanzar necesitamos una gramática algebraica mínima: no una lista de nombres para memorizar, sino herramientas para **leer correctamente la estructura simbólica**.

Ese será el objetivo de:
