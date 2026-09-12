---
title: "Del cálculo aritmético al lenguaje algebraico"
description: "Primer capítulo de Álgebra para matemáticos: estructura de expresiones, variables, sustitución, igualdad, identidades, ecuaciones y transformación simbólica rigurosa."
content-id: MA-BCH-0007
source-id: APM-T1-C01
content-type: book-chapter
collection: PM-ALG
book-id: MA-BOK-0004
status: published
date-created: 2026-09-09
date-modified: 2026-09-10
areas:
  - fundamentos
  - algebra
level: fundamental
topics:
  - lenguaje-algebraico
  - expresiones
  - variables
  - sustitucion
  - igualdad
  - identidades
  - ecuaciones
  - sintaxis-matematica
  - transformacion-algebraica
prerequisites: []
related:
  - MA-BOK-0004
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Del cálculo aritmético al lenguaje algebraico

## §1. De una cuenta a una expresión

Hasta ahora, probablemente has visto miles de cuentas como estas:

$$
3+4\cdot5
$$

y

$$
(3+4)\cdot5.
$$

Contienen los mismos tres números y las mismas dos operaciones: una suma y una multiplicación. Sin embargo, sus valores son distintos:

$$
3+4\cdot5=23,
$$

mientras que

$$
(3+4)\cdot5=35.
$$

Podríamos explicar la diferencia diciendo simplemente que «la multiplicación se hace antes que la suma» y que los paréntesis cambian el orden de las operaciones. Esa explicación es correcta, pero para nuestro propósito se queda corta.

Queremos aprender a mirar una escritura algebraica de otra manera.

La diferencia esencial entre las dos expresiones anteriores no está solamente en **qué operación hacemos primero**, sino en **cómo está organizada la expresión**.

En

$$
3+4\cdot5,
$$

la multiplicación $4\cdot5$ forma una unidad dentro de una suma mayor:

$$
3+(4\cdot5).
$$

En cambio, en

$$
(3+4)\cdot5,
$$

la suma $3+4$ forma una unidad dentro de una multiplicación mayor:

$$
(3+4)\cdot5.
$$

En el primer caso, la expresión completa tiene la forma

$$
\boxed{\text{número}+\text{producto}},
$$

mientras que, en el segundo, tiene la forma

$$
\boxed{\text{suma}\cdot\text{número}}.
$$

Este será nuestro primer cambio de perspectiva:

::: {.ma-block .ma-intuicion}
**Idea clave**

Antes de calcular una expresión, conviene aprender a **leer su estructura**.
:::

***

### 1.1 Una cuenta tiene arquitectura

Considera ahora:

$$
7-2\cdot3.
$$

Sabemos calcularla:

$$
7-2\cdot3
=
7-6
=
1.
$$

Pero no queremos comenzar calculando. Queremos preguntar primero:

> ¿Cómo está construida esta expresión?

La parte

$$
2\cdot3
$$

es una multiplicación. La expresión completa es

$$
7-(2\cdot3).
$$

Por tanto, la operación que organiza la expresión completa es la resta.

Diremos, de manera todavía informal, que la **operación principal** es la operación que une las partes más grandes de la expresión.

En

$$
7-2\cdot3,
$$

la operación principal es la resta.

En cambio, en

$$
(7-2)\cdot3,
$$

la operación principal es la multiplicación, porque las dos grandes partes son

$$
(7-2)
\qquad\text{y}\qquad
3.
$$

Esta distinción parece muy sencilla, pero será fundamental cuando las expresiones sean mucho más largas.

Por ejemplo:

$$
5\bigl(2+(3-1)\bigr).
$$

Podemos leerla desde fuera hacia dentro.

La operación principal es la multiplicación:

$$
5
\cdot
\bigl(2+(3-1)\bigr).
$$

Dentro del segundo factor aparece la suma

$$
2+(3-1),
$$

y dentro de esa suma aparece la resta

$$
3-1.
$$

La expresión posee, por tanto, varios niveles.

Una forma útil de representarlos es:

```text
multiplicación
├── 5
└── suma
    ├── 2
    └── resta
        ├── 3
        └── 1
```

No necesitamos convertir estos diagramas en una teoría formal. Por ahora basta aprender la idea:

$$
\boxed{
\text{una expresión puede contener otras expresiones dentro de ella}.
}
$$

A esas partes internas las llamaremos **subexpresiones**.

***

### 1.2 Expresión y valor

Hasta aquí hemos usado la palabra «expresión» varias veces. Conviene fijar qué entenderemos por ella.

::: {.ma-block .ma-definicion #apm-t1-c01-d0001}
**Definición — Expresión matemática**

Una **expresión matemática** es una combinación de símbolos construida de acuerdo con ciertas reglas de escritura y destinada a representar un objeto o un valor matemático.
:::

En este capítulo trabajaremos sobre todo con expresiones que representan números.

Por ejemplo,

$$
3+4\cdot5
$$

es una expresión.

Al calcularla obtenemos:

$$
23.
$$

Decimos entonces que el **valor** de la expresión es $23$.

Conviene distinguir cuidadosamente estos dos niveles:

- la **expresión** es la escritura que representa;
- el **valor** es el número representado por esa escritura.

Así,

$$
3+4\cdot5
$$

y

$$
20+3
$$

son expresiones distintas, pero ambas tienen el mismo valor:

$$
23.
$$

También la escritura

$$
23
$$

es, por sí misma, una expresión muy sencilla que representa ese mismo número.

Por eso, cuando digamos informalmente

$$
\boxed{\text{expresión}\neq\text{valor}},
$$

no queremos afirmar que un número como $23$ no pueda aparecer escrito como expresión. Queremos recordar una distinción conceptual: **una cosa es la representación simbólica y otra el objeto que esa representación denota**.

Esta distinción será cada vez más importante.

***

### 1.3 Leer de fuera hacia dentro

Una estrategia especialmente útil consiste en buscar primero la estructura exterior.

Consideremos:

$$
18\div(2+4).
$$

Antes de calcular, preguntamos:

1. ¿Cuál es la operación principal?
2. ¿Cuáles son sus dos partes?

La operación principal es la división:

$$
\frac{18}{2+4}.
$$

Sus dos partes son:

$$
18
\qquad\text{y}\qquad
2+4.
$$

Solo después analizamos la segunda parte, cuya operación principal es la suma.

Finalmente calculamos:

$$
\frac{18}{2+4}
=
\frac{18}{6}
=
3.
$$

El orden mental que estamos practicando es:

$$
\boxed{
\text{leer la estructura}
\longrightarrow
\text{identificar las partes}
\longrightarrow
\text{calcular}.
}
$$

No es una regla destinada a hacer más lenta una cuenta sencilla. Es un entrenamiento para cuando las expresiones dejen de ser sencillas.

***

### 1.4 Mini ejemplo: la importancia del signo exterior

Mira las dos expresiones:

$$
20-(6+3)
$$

y

$$
(20-6)+3.
$$

En la primera, la operación principal es la resta:

$$
20-\boxed{(6+3)}.
$$

Su valor es

$$
20-9=11.
$$

En la segunda, la suma es la operación principal:

$$
\boxed{(20-6)}+3.
$$

Su valor es

$$
14+3=17.
$$

Los mismos números y los mismos signos pueden describir estructuras diferentes.

***

### 1.5 Mini ejemplo: una potencia dentro de una suma

Considera:

$$
2+3^2.
$$

La potencia

$$
3^2
$$

es una subexpresión.

La expresión completa tiene la forma

$$
2+(3^2),
$$

de modo que su operación principal es la suma.

Después de leerla podemos calcular:

$$
2+3^2
=
2+9
=
11.
$$

En cambio,

$$
(2+3)^2
$$

tiene como operación exterior la potenciación:

$$
(2+3)^2=5^2=25.
$$

Una vez más, los paréntesis no son un adorno tipográfico. Revelan la estructura.

***

### 1.6 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-t1-c01-x0001}
**Ejemplo — Los mismos símbolos, dos estructuras**

:::

Comparemos:

$$
8-3\cdot2
$$

y

$$
(8-3)\cdot2.
$$

#### Primera expresión

Tenemos:

$$
8-3\cdot2.
$$

La multiplicación

$$
3\cdot2
$$

forma una subexpresión. La estructura exterior es:

$$
8-(3\cdot2).
$$

Por tanto, la operación principal es la resta.

Ahora calculamos:

$$
8-3\cdot2
=
8-6
=
2.
$$

#### Segunda expresión

Tenemos:

$$
(8-3)\cdot2.
$$

La resta

$$
8-3
$$

forma una subexpresión. La estructura exterior es:

$$
(8-3)\cdot2.
$$

Por tanto, la operación principal es la multiplicación.

Ahora calculamos:

$$
(8-3)\cdot2
=
5\cdot2
=
10.
$$

#### Comparación

Las expresiones contienen los mismos números:

$$
8,\quad3,\quad2,
$$

y los mismos signos de resta y multiplicación. Pero los paréntesis determinan estructuras distintas:

$$
8-(3\cdot2)
$$

frente a

$$
(8-3)\cdot2.
$$

Por eso sus valores son distintos:

$$
2\neq10.
$$

La lección no es solamente «respeta el orden de las operaciones». Es más profunda:

$$
\boxed{
\text{el significado de una expresión depende de su estructura}.
}
$$

***

## Ejercicios

### Operación principal {#apm-t1-c01-e0001}

En cada expresión, identifica la operación principal. No calcules todavía.

1. $6+2\cdot5$
2. $(6+2)\cdot5$
3. $18-(4+3)$
4. $\dfrac{24}{3+5}$
5. $2+(3+4)^2$

#### Solución

**1.**

$$
6+2\cdot5
=
6+(2\cdot5).
$$

La multiplicación $2\cdot5$ es una subexpresión. La operación exterior es la suma.

**Operación principal:** suma.

**2.**

$$
(6+2)\cdot5.
$$

Las dos partes mayores son $(6+2)$ y $5$, unidas por un producto.

**Operación principal:** multiplicación.

**3.**

$$
18-(4+3).
$$

La suma $4+3$ está dentro de los paréntesis. La expresión completa resta esa suma a $18$.

**Operación principal:** resta.

**4.**

$$
\frac{24}{3+5}.
$$

El numerador es $24$ y el denominador es $3+5$. La expresión completa es un cociente.

**Operación principal:** división.

**5.**

$$
2+(3+4)^2.
$$

La potencia $(3+4)^2$ es una de las dos partes de una suma exterior:

$$
2+\bigl((3+4)^2\bigr).
$$

**Operación principal:** suma.

***

### Los paréntesis cambian la estructura {#apm-t1-c01-e0002}

Usa los números $2$, $3$ y $4$, en ese orden, y los signos $+$ y $\cdot$.

1. Escribe una expresión cuyo valor sea $14$.
2. Escribe otra, con los mismos símbolos básicos, cuyo valor sea $20$.
3. Explica por qué los valores son distintos.

#### Solución

Para obtener $14$ podemos escribir:

$$
2+3\cdot4.
$$

La multiplicación se encuentra dentro de una suma:

$$
2+(3\cdot4),
$$

por lo que

$$
2+3\cdot4
=
2+12
=
14.
$$

Para obtener $20$ escribimos:

$$
(2+3)\cdot4.
$$

Ahora la suma está dentro de una multiplicación:

$$
(2+3)\cdot4
=
5\cdot4
=
20.
$$

Los valores son distintos porque las expresiones tienen estructuras distintas. En la primera, la operación principal es la suma; en la segunda, es la multiplicación.

***

### Expresión y valor {#apm-t1-c01-e0003}

Para cada expresión:

1. describe su estructura exterior;
2. identifica una subexpresión;
3. calcula su valor.

#### a)

$$
15-(2+5)
$$

#### b)

$$
3(4+2)
$$

#### c)

$$
5+2^3
$$

#### Solución

#### a)

La expresión es:

$$
15-(2+5).
$$

Su estructura exterior es una resta. Una subexpresión es:

$$
2+5.
$$

Calculamos:

$$
15-(2+5)
=
15-7
=
8.
$$

El valor de la expresión es $8$.

#### b)

La expresión es:

$$
3(4+2).
$$

Su estructura exterior es una multiplicación. Una subexpresión es:

$$
4+2.
$$

Calculamos:

$$
3(4+2)
=
3\cdot6
=
18.
$$

El valor es $18$.

#### c)

La expresión es:

$$
5+2^3.
$$

Su estructura exterior es una suma. Una subexpresión es:

$$
2^3.
$$

Calculamos:

$$
5+2^3
=
5+8
=
13.
$$

El valor es $13$.

***

### Una expresión en palabras {#apm-t1-c01-e0004}

Describe con palabras la estructura de:

$$
5\bigl(2+3^2\bigr).
$$

Después calcula su valor.

#### Solución

Primero leemos desde fuera.

La operación principal es una multiplicación. Sus dos factores son:

$$
5
$$

y

$$
2+3^2.
$$

Dentro del segundo factor, la operación principal es una suma. Sus dos partes son:

$$
2
$$

y

$$
3^2.
$$

Dentro de esa suma aparece la potencia $3^2$.

Podemos describir la expresión como:

> cinco multiplicado por la suma de dos y el cuadrado de tres.

Solo después calculamos:

$$
5\bigl(2+3^2\bigr)
=
5(2+9)
=
5\cdot11
=
55.
$$

***

### Construcción {#apm-t1-c01-e0005}

Construye dos expresiones diferentes que:

- usen exactamente una vez los números $2$, $5$ y $6$;
- usen una suma y una multiplicación;
- tengan operaciones principales distintas.

Calcula luego sus valores y explica la diferencia estructural.

#### Solución

Una posibilidad es:

$$
2+5\cdot6
$$

y

$$
(2+5)\cdot6.
$$

En la primera expresión, la operación principal es la suma:

$$
2+(5\cdot6).
$$

Su valor es:

$$
2+5\cdot6
=
2+30
=
32.
$$

En la segunda, la operación principal es la multiplicación:

$$
(2+5)\cdot6.
$$

Su valor es:

$$
(2+5)\cdot6
=
7\cdot6
=
42.
$$

La diferencia no proviene de los números ni de las operaciones utilizadas, que son los mismos. Proviene de la manera en que esas operaciones están organizadas.

***

## Resumen de la sección

En esta primera sección hemos introducido una idea sencilla pero decisiva: una cuenta no es solo una secuencia de símbolos que debemos procesar.

Una expresión posee estructura.

Hemos aprendido a:

- identificar la operación principal;
- reconocer subexpresiones;
- leer una expresión de fuera hacia dentro;
- entender el papel estructural de los paréntesis;
- distinguir entre una expresión y el valor que representa.

La definición fundamental de la sección es:

::: {.ma-block .ma-observacion}
**Síntesis**

Una **expresión matemática** es una combinación de símbolos construida de acuerdo con ciertas reglas de escritura y destinada a representar un objeto o un valor matemático.
:::

El hábito que queremos conservar es:

$$
\boxed{
\text{leer}
\longrightarrow
\text{comprender la estructura}
\longrightarrow
\text{calcular}.
}
$$

***

## Hacia la sección siguiente

Todas las expresiones que hemos usado hasta ahora contienen números concretos:

$$
3,\quad5,\quad18,\quad24,\ldots
$$

Pero el álgebra comienza a mostrar toda su potencia cuando podemos hablar de un número **sin tener que decidir todavía cuál es**.

En lugar de escribir un número concreto, podemos darle un nombre:

$$
x,\qquad a,\qquad n.
$$

¿Qué significa exactamente una letra dentro de una expresión?

¿Es siempre una cantidad desconocida?

¿Tiene que «cambiar»?

¿Puede representar un número fijo?

Estas serán las preguntas de la siguiente sección:

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

***

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

***

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

***

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

***

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

***

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

***

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

***

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

***

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

***

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

***

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

***

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

***

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

***

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

***

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

***

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

## §3. Términos, expresiones y fórmulas

En las dos secciones anteriores hemos dado dos pasos. Primero aprendimos que una expresión tiene estructura; después introdujimos letras y vimos que su papel depende del contexto. Ahora necesitamos un vocabulario mínimo para describir expresiones como

$$
x+3,
$$

$$
2x^2-5x+1,
$$

$$
\frac{a+b}{c},
$$

o

$$
3(a+b)^2.
$$

La palabra «mínimo» es importante. No queremos aprender una lista de nombres como si el álgebra fuera una clasificación gramatical. Queremos palabras que nos ayuden a **leer la estructura**.

::: {.ma-block .ma-intuicion}
**Idea clave**

El vocabulario algebraico sirve para indicar **cómo está construida una expresión**.
:::

***

### 3.1 Sumas y términos

Consideremos:

$$
x+3.
$$

La operación principal es una suma. Las dos partes que esa suma reúne son

$$
x
$$

y

$$
3.
$$

En este contexto podemos llamar a esas partes **términos** de la suma.

Así, en

$$
a+b+c,
$$

podemos reconocer tres términos:

$$
a,
\qquad
b,
\qquad
c.
$$

La idea importante es que «término» no designa simplemente cualquier fragmento que veamos escrito. Describe una parte de una expresión cuando estamos mirando una **estructura aditiva**.

Consideremos ahora:

$$
2x+5.
$$

La expresión completa es una suma. Sus dos términos son

$$
2x
$$

y

$$
5.
$$

El primer término, a su vez, tiene estructura multiplicativa. Por tanto, una misma parte de una expresión puede describirse de maneras diferentes según el nivel que estemos observando.

En

$$
2x+5,
$$

la subexpresión

$$
2x
$$

es un **término** respecto de la suma exterior y un **producto** cuando la examinamos internamente.

Esta manera de hablar evita una dificultad frecuente: creer que cada símbolo debe recibir una sola etiqueta absoluta.

***

### 3.2 Productos y factores

Consideremos ahora:

$$
3x.
$$

Como vimos en la sección anterior, esta escritura significa

$$
3\cdot x.
$$

Las partes multiplicadas son

$$
3
$$

y

$$
x.
$$

Las llamamos **factores** del producto.

Así, en

$$
2ab,
$$

podemos leer

$$
2\cdot a\cdot b.
$$

Los factores son

$$
2,
\qquad
a,
\qquad
b.
$$

Pero volvamos a

$$
2x+5.
$$

Aquí debemos distinguir dos niveles. La expresión completa es una suma:

$$
\boxed{2x}+5.
$$

Por ello, $2x$ es uno de sus términos. Dentro de ese término encontramos un producto:

$$
2\cdot x.
$$

Por ello, $2$ y $x$ son factores de ese producto.

Podemos resumir la lectura así:

```text
suma
├── término: 2x
│   └── producto
│       ├── factor: 2
│       └── factor: x
└── término: 5
```

No pretendemos que este diagrama sea una definición formal. Es una ayuda para aprender a leer por niveles.

***

### 3.3 Restas y signos

Consideremos:

$$
2x-5.
$$

A primera vista podemos decir que aparecen una multiplicación y una resta. Eso es correcto. Pero en el lenguaje algebraico es frecuente tratar expresiones como

$$
2x-5
$$

como sumas de términos con signo:

$$
2x+(-5).
$$

Así podemos hablar de dos términos:

$$
2x
\qquad\text{y}\qquad
-5.
$$

No desarrollaremos todavía una teoría completa de suma de términos ni de números con signo; por ahora basta observar que el signo menos puede formar parte del término que sigue cuando la expresión se interpreta aditivamente.

Por ejemplo, en

$$
2x^2-5x+1,
$$

podemos reconocer los términos

$$
2x^2,
\qquad
-5x,
\qquad
1.
$$

Esta lectura será especialmente útil más adelante, cuando estudiemos polinomios.

::: {.ma-block .ma-error}
**Atención**

No debemos confundir el signo menos que pertenece a un término con una instrucción informal de «cambiar el signo» o «mover algo al otro lado». Las transformaciones de ecuaciones se estudiarán más adelante con precisión.
:::

***

### 3.4 Potencias: base y exponente

Consideremos:

$$
x^2.
$$

Esta expresión representa una potencia. La **base** es

$$
x,
$$

y el **exponente** es

$$
2.
$$

En

$$
(a+b)^3,
$$

la base completa es

$$
a+b,
$$

y el exponente es

$$
3.
$$

La estructura es:

```text
potencia
├── base: a+b
└── exponente: 3
```

Los paréntesis indican que toda la suma

$$
a+b
$$

actúa como base.

Comparemos:

$$
a+b^2
$$

con

$$
(a+b)^2.
$$

En la primera, solo $b$ está elevado al cuadrado. En la segunda, toda la suma está elevada al cuadrado.

***

### 3.5 Cocientes: numerador y denominador

Consideremos:

$$
\frac{a+b}{c}.
$$

La expresión completa es un cociente. Su numerador es

$$
a+b,
$$

y su denominador es

$$
c.
$$

Dentro del numerador hay una suma.

Podemos leer entonces:

```text
cociente
├── numerador: a+b
│   └── suma
│       ├── a
│       └── b
└── denominador: c
```

Comparemos ahora

$$
\frac{a+b}{c}
$$

con

$$
a+\frac{b}{c}.
$$

En la primera expresión, la operación principal es la división. En la segunda, la operación principal es la suma.

La barra de fracción cumple un papel semejante al de unos paréntesis extensos: agrupa todo el numerador y todo el denominador.

***

### 3.6 Leer una expresión por capas

Consideremos ahora una expresión más larga:

$$
\frac{2x-(a+b)^2}{3c}.
$$

No intentemos hacer nada con ella. Solo queremos leerla.

#### Primera capa

La expresión completa es un cociente:

$$
\frac{\boxed{2x-(a+b)^2}}{\boxed{3c}}.
$$

#### Segunda capa: numerador

El numerador es

$$
2x-(a+b)^2.
$$

Podemos leerlo aditivamente como dos términos:

$$
2x
\qquad\text{y}\qquad
-(a+b)^2.
$$

#### Tercera capa: primer término

En

$$
2x,
$$

hay un producto con factores

$$
2
\qquad\text{y}\qquad
x.
$$

#### Tercera capa: segundo término

En

$$
(a+b)^2,
$$

hay una potencia. La base es

$$
a+b,
$$

y el exponente es

$$
2.
$$

Dentro de la base aparece una suma con términos

$$
a
\qquad\text{y}\qquad
b.
$$

#### Segunda capa: denominador

El denominador es

$$
3c,
$$

un producto con factores

$$
3
\qquad\text{y}\qquad
c.
$$

Una expresión que inicialmente parecía complicada se vuelve mucho más legible cuando la recorremos por niveles.

El método es el mismo que aprendimos en §1:

$$
\boxed{
\text{primero la estructura exterior; después las partes interiores}.
}
$$

***

### 3.7 Una expresión representa; una igualdad afirma

Ahora comparemos:

$$
x+3
$$

con

$$
x+3=7.
$$

La primera escritura es una expresión. Representa un valor que dependerá de cómo se interprete $x$. Pero no afirma, por sí sola, que ese valor sea uno u otro.

La segunda escritura contiene una igualdad:

$$
x+3=7.
$$

Aquí ya no estamos simplemente representando un valor. Estamos **afirmando** que dos expresiones representan lo mismo:

$$
x+3
$$

y

$$
7.
$$

Todavía no introduciremos el término formal «proposición». Tampoco estudiaremos cuándo una afirmación es verdadera o falsa en sentido lógico.

Por ahora basta distinguir:

$$
\boxed{
\text{expresión}
\quad\text{frente a}\quad
\text{escritura que afirma una igualdad}.
}
$$

Esta diferencia será decisiva en las secciones siguientes.

***

### 3.8 ¿Qué llamaremos fórmula?

La palabra **fórmula** se usa en matemáticas de varias maneras.

Por ejemplo, solemos hablar de

$$
A=\pi r^2
$$

como «la fórmula del área de un círculo».

También podemos hablar de una fórmula como

$$
a(b+c)=ab+ac
$$

para expresar una relación general.

No intentaremos convertir «fórmula» en una categoría formal rígida en este capítulo.

La usaremos como una palabra funcional para una escritura matemática que expresa de manera compacta una regla, relación o patrón.

::: {.ma-block .ma-observacion}
**Observación**

Más adelante, en lógica matemática, la palabra «fórmula» puede adquirir un significado técnico más preciso. Cuando lleguemos allí distinguiremos cuidadosamente ese uso formal del uso corriente que hacemos ahora.
:::

***

### 3.9 Ejemplo guiado: leer sin simplificar

Consideremos:

$$
4a^2+\frac{b+1}{3}.
$$

La operación principal es la suma. Sus dos términos son

$$
4a^2
$$

y

$$
\frac{b+1}{3}.
$$

En el primer término,

$$
4a^2,
$$

podemos reconocer un producto entre

$$
4
$$

y

$$
a^2.
$$

La subexpresión

$$
a^2
$$

es una potencia de base $a$ y exponente $2$.

En el segundo término,

$$
\frac{b+1}{3},
$$

tenemos un cociente. El numerador es

$$
b+1,
$$

una suma de dos términos, y el denominador es

$$
3.
$$

No hemos calculado ni simplificado nada. Y, sin embargo, ahora comprendemos mucho mejor la escritura.

::: {.ma-block .ma-intuicion}
**Idea clave**

Nombrar partes de una expresión es útil solo si nos permite ver su organización.
:::

***

## Ejercicios

### Términos y factores {#apm-t1-c01-e0011}

En cada expresión, identifica los términos de la suma exterior. Después, cuando corresponda, identifica los factores de cada término.

#### a)

$$
3x+5
$$

#### b)

$$
2ab+7
$$

#### c)

$$
4x^2-3x+1
$$

#### Solución

#### a)

La suma exterior tiene dos términos:

$$
3x
\qquad\text{y}\qquad
5.
$$

Dentro de $3x$ hay un producto con factores

$$
3
\qquad\text{y}\qquad
x.
$$

#### b)

La expresión tiene dos términos:

$$
2ab
\qquad\text{y}\qquad
7.
$$

El primero puede leerse como

$$
2\cdot a\cdot b,
$$

de modo que sus factores son

$$
2,
\qquad
a,
\qquad
b.
$$

#### c)

Leída aditivamente, la expresión tiene los términos

$$
4x^2,
\qquad
-3x,
\qquad
1.
$$

En el primer término reconocemos los factores

$$
4
\qquad\text{y}\qquad
x^2.
$$

En el segundo, los factores son

$$
-3
\qquad\text{y}\qquad
x.
$$

***

### Bases y exponentes {#apm-t1-c01-e0012}

Identifica la base y el exponente de cada potencia.

#### a)

$$
x^5
$$

#### b)

$$
(a+b)^3
$$

#### c)

$$
(2x+1)^4
$$

#### Solución

#### a)

En

$$
x^5,
$$

la base es $x$ y el exponente es $5$.

#### b)

En

$$
(a+b)^3,
$$

la base completa es

$$
a+b,
$$

y el exponente es $3$.

Los paréntesis muestran que toda la suma es la base.

#### c)

En

$$
(2x+1)^4,
$$

la base es

$$
2x+1,
$$

y el exponente es $4$.

***

### Numerador, denominador y estructura {#apm-t1-c01-e0013}

Considera:

$$
\frac{x+2}{3y}.
$$

1. ¿Cuál es la operación principal?
2. ¿Cuál es el numerador?
3. ¿Cuál es el denominador?
4. ¿Qué estructura tiene el numerador?
5. ¿Qué estructura tiene el denominador?

#### Solución

La expresión completa es un cociente. Por tanto, la operación principal es la división.

El numerador es

$$
x+2.
$$

Tiene estructura de suma, con términos

$$
x
\qquad\text{y}\qquad
2.
$$

El denominador es

$$
3y.
$$

Tiene estructura de producto, con factores

$$
3
\qquad\text{y}\qquad
y.
$$

***

### Expresión o afirmación {#apm-t1-c01-e0014}

Indica cuáles de las siguientes escrituras son solo expresiones y cuáles afirman una igualdad.

1. $x+4$
2. $x+4=9$
3. $3a^2$
4. $\dfrac{a+b}{2}$
5. $(a+b)^2=a^2+2ab+b^2$

No decidas todavía si las igualdades son válidas para todos los valores. Solo clasifica el tipo de escritura.

#### Solución

**1.**

$$
x+4
$$

es una expresión. Representa un valor, pero no contiene ninguna afirmación de igualdad.

**2.**

$$
x+4=9
$$

afirma una igualdad entre las expresiones $x+4$ y $9$.

**3.**

$$
3a^2
$$

es una expresión.

**4.**

$$
\frac{a+b}{2}
$$

es una expresión.

**5.**

$$
(a+b)^2=a^2+2ab+b^2
$$

afirma una igualdad entre dos expresiones.

Todavía no estamos estudiando formalmente qué significa que esta igualdad sea válida para distintos valores; eso vendrá más adelante.

***

### Lectura por capas {#apm-t1-c01-e0015}

Describe la estructura de

$$
\frac{3a+(b-1)^2}{2c}.
$$

Debes identificar:

1. la estructura exterior;
2. numerador y denominador;
3. los términos principales del numerador;
4. la base y el exponente de la potencia;
5. los factores del denominador.

#### Solución

La expresión completa es

$$
\frac{3a+(b-1)^2}{2c}.
$$

#### 1. Estructura exterior

La operación principal es la división.

#### 2. Numerador y denominador

El numerador es

$$
3a+(b-1)^2.
$$

El denominador es

$$
2c.
$$

#### 3. Términos del numerador

La operación principal del numerador es una suma. Sus términos son

$$
3a
$$

y

$$
(b-1)^2.
$$

#### 4. Potencia

En

$$
(b-1)^2,
$$

la base es

$$
b-1,
$$

y el exponente es $2$.

Dentro de la base aparece una resta.

#### 5. Denominador

El denominador

$$
2c
$$

es un producto con factores

$$
2
\qquad\text{y}\qquad
c.
$$

La expresión completa queda organizada en capas, desde el cociente exterior hasta las subexpresiones interiores.

***

## Resumen de la sección

El objetivo de esta sección no ha sido acumular nombres, sino aprender a describir con precisión la estructura de una expresión.

Hemos usado las palabras:

- **término**, para partes de una suma;
- **factor**, para partes de un producto;
- **base** y **exponente**, para una potencia;
- **numerador** y **denominador**, para un cociente.

También hemos visto que estas palabras dependen del nivel de lectura.

En

$$
2x+5,
$$

la subexpresión $2x$ es un término de la suma exterior y, al mismo tiempo, es internamente un producto cuyos factores son $2$ y $x$.

El hábito fundamental sigue siendo:

$$
\boxed{
\text{leer de fuera hacia dentro}.
}
$$

Además distinguimos dos tipos de escritura:

$$
x+3
$$

representa una expresión, mientras que

$$
x+3=7
$$

afirma una igualdad.

Todavía no hemos formalizado el concepto lógico de afirmación; simplemente hemos preparado el terreno.

Finalmente, usaremos la palabra **fórmula** de manera no técnica para una escritura que expresa compactamente una regla, una relación o un patrón.

***

## Hacia la sección siguiente

Hasta ahora hemos hablado de expresiones como

$$
x^2+2x+1
$$

sin asignar necesariamente un valor a $x$.

Pero, si sabemos que

$$
x=-3,
$$

¿cómo debemos reemplazar correctamente cada aparición de $x$?

¿Es lo mismo escribir

$$
-3^2
$$

que

$$
(-3)^2?
$$

¿Qué ocurre si, en lugar de sustituir una variable por un número, la sustituimos por toda una expresión como

$$
a+b?
$$

Estas preguntas nos llevarán a una operación algebraica básica que exige mucho más cuidado del que parece:

## §4. Sustitución y evaluación

En §2 introdujimos letras como símbolos que pueden representar números. En §3 aprendimos a leer expresiones formadas con esas letras.

Consideremos ahora:

$$
x^2+2x+1.
$$

Mientras no fijemos un valor para $x$, la expresión permanece escrita de forma general.

Pero supongamos que nos dicen:

$$
x=3.
$$

Entonces podemos reemplazar cada aparición de $x$ por $3$:

$$
3^2+2\cdot3+1.
$$

Y ahora sí podemos calcular:

$$
3^2+2\cdot3+1
=
9+6+1
=
16.
$$

Hemos realizado dos acciones distintas:

1. **sustituir** el símbolo $x$ por un valor;
2. **evaluar** la expresión obtenida.

Parecen operaciones elementales. Y lo son. Sin embargo, muchos errores algebraicos futuros nacen precisamente de sustituir sin respetar la estructura de la expresión.

La idea central de esta sección será:

::: {.ma-block .ma-intuicion}
**Idea clave**

Sustituir no significa «borrar una letra y poner otra cosa en su lugar» de cualquier manera.  
Sustituir significa **reemplazar el símbolo por una nueva expresión conservando intacta la estructura que lo rodea**.
:::

***

### 4.1 Sustituir es reemplazar todas las apariciones

Consideremos:

$$
2x+5.
$$

Si:

$$
x=4,
$$

debemos reemplazar la aparición de $x$ por $4$:

$$
2x+5
\quad\longrightarrow\quad
2\cdot4+5.
$$

Después calculamos:

$$
2\cdot4+5
=
8+5
=
13.
$$

Ahora considera:

$$
x^2+3x-1.
$$

Si:

$$
x=2,
$$

la letra aparece dos veces.

Debemos reemplazar **ambas** apariciones:

$$
x^2+3x-1
\quad\longrightarrow\quad
2^2+3\cdot2-1.
$$

Entonces:

$$
2^2+3\cdot2-1
=
4+6-1
=
9.
$$

Un error frecuente sería sustituir solo la primera aparición:

$$
2^2+3x-1.
$$

Eso no es la evaluación de la expresión en $x=2$, porque todavía queda una aparición de $x$ sin reemplazar.

Por tanto:

$$
\boxed{
\text{si un símbolo recibe un valor, debemos sustituir todas sus apariciones relevantes}.
}
$$

***

### 4.2 Los paréntesis protegen la estructura

El caso más importante aparece cuando sustituimos un número negativo.

Consideremos:

$$
x^2.
$$

Si:

$$
x=-3,
$$

no debemos escribir simplemente

$$
-3^2.
$$

¿Por qué?

Porque:

$$
-3^2
$$

significa, según las convenciones usuales,

$$
-(3^2),
$$

y por tanto:

$$
-3^2=-9.
$$

Pero nosotros queremos elevar al cuadrado **el valor completo de $x$**, que es $-3$.

Debemos escribir:

$$
(-3)^2.
$$

Entonces:

$$
(-3)^2=9.
$$

Así,

$$
x^2
\quad\text{con}\quad
x=-3
$$

se convierte en:

$$
(-3)^2,
$$

no en:

$$
-3^2.
$$

::: {.ma-block .ma-intuicion}
**Idea clave**

Cuando sustituimos una variable por un número negativo, los paréntesis conservan el número completo como una unidad.
:::

Este no es un truco tipográfico. Es una consecuencia de la estructura que aprendimos a leer en §1 y §3.

***

### 4.3 Ejemplo desarrollado: un número negativo

::: {.ma-block .ma-observacion #apm-t1-c01-x0002}
**Ejemplo — Sustituir sin perder el signo**

:::

Evaluemos:

$$
x^2+2x+1
$$

cuando:

$$
x=-3.
$$

#### Paso 1 — Identificar todas las apariciones de $x$

La expresión contiene dos apariciones:

$$
x^2
$$

y

$$
2x.
$$

#### Paso 2 — Sustituir el valor completo

Como:

$$
x=-3,
$$

escribimos:

$$
(-3)^2+2(-3)+1.
$$

Los paréntesis son esenciales.

#### Paso 3 — Evaluar cada parte

Tenemos:

$$
(-3)^2=9
$$

y

$$
2(-3)=-6.
$$

Por tanto:

$$
(-3)^2+2(-3)+1
=
9-6+1
=
4.
$$

#### Resultado

El valor de la expresión cuando $x=-3$ es:

$$
\boxed{4}.
$$

#### Qué habría ocurrido con una sustitución incorrecta

Si hubiéramos escrito:

$$
-3^2+2(-3)+1,
$$

obtendríamos:

$$
-9-6+1=-14.
$$

El error no estaría en la aritmética final. Estaría mucho antes: habríamos alterado la estructura al reemplazar $x$ por $-3$ sin agrupar el valor completo.

***

### 4.4 Evaluar una expresión

Ya podemos fijar el vocabulario central de la sección.

::: {.ma-block .ma-definicion #apm-t1-c01-d0004}
**Definición — Evaluación de una expresión**

**Evaluar una expresión** para valores dados de sus símbolos consiste en sustituir esos valores en todas las apariciones correspondientes y, cuando sea posible, realizar las operaciones resultantes.
:::

Por ejemplo, evaluemos:

$$
3a-2
$$

cuando:

$$
a=5.
$$

Sustituimos:

$$
3a-2
\quad\longrightarrow\quad
3\cdot5-2.
$$

Calculamos:

$$
3\cdot5-2
=
15-2
=
13.
$$

La evaluación tiene, por tanto, una secuencia conceptual clara:

$$
\boxed{
\text{expresión general}
\longrightarrow
\text{sustitución}
\longrightarrow
\text{expresión concreta}
\longrightarrow
\text{valor}.
}
$$

***

### 4.5 El cero también debe sustituirse

Consideremos:

$$
4x+7.
$$

Si:

$$
x=0,
$$

la sustitución correcta es:

$$
4\cdot0+7.
$$

Entonces:

$$
4\cdot0+7
=
0+7
=
7.
$$

Puede parecer innecesario escribir explícitamente el cero, pero hacerlo ayuda a conservar la estructura.

En expresiones más complejas, «omitir» una parte porque vale cero puede ocultar errores.

Por ejemplo, en:

$$
x^2+5x+4,
$$

si $x=0$:

$$
0^2+5\cdot0+4
=
4.
$$

El método no cambia porque el valor elegido sea cero.

***

### 4.6 Sustitución con varias letras

Consideremos:

$$
2a+3b.
$$

Supongamos que:

$$
a=4,
\qquad
b=-2.
$$

Debemos sustituir cada letra por su valor correspondiente:

$$
2a+3b
\quad\longrightarrow\quad
2\cdot4+3(-2).
$$

Después evaluamos:

$$
2\cdot4+3(-2)
=
8-6
=
2.
$$

La sustitución debe respetar dos cosas:

1. **qué símbolo recibe qué valor**;
2. **todas las apariciones del símbolo**.

Consideremos:

$$
a^2+ab+b^2.
$$

Si:

$$
a=2,
\qquad
b=-1,
$$

obtenemos:

$$
2^2+2(-1)+(-1)^2.
$$

Y entonces:

$$
4-2+1
=
3.
$$

De nuevo, los paréntesis protegen el valor negativo de $b$.

***

### 4.7 Sustituir una expresión completa

Hasta ahora hemos sustituido letras por números.

Pero podemos hacer algo más general.

Consideremos:

$$
x^2+1.
$$

Supongamos que queremos reemplazar $x$ por la expresión:

$$
a+b.
$$

No estamos diciendo que $x$ sea un número concreto. Estamos indicando que, en esta escritura, donde aparecía $x$ debe aparecer ahora **toda la expresión** $a+b$.

Entonces:

$$
x^2+1
\quad\longrightarrow\quad
(a+b)^2+1.
$$

Los paréntesis vuelven a ser esenciales.

Si escribiéramos:

$$
a+b^2+1,
$$

habríamos sustituido incorrectamente, porque solo $b$ quedaría elevado al cuadrado.

La estructura original era:

$$
\boxed{x}^2+1.
$$

La nueva estructura debe ser:

$$
\boxed{(a+b)}^2+1.
$$

La expresión $a+b$ ocupa exactamente el lugar estructural que antes ocupaba $x$.

***

### 4.8 Ejemplo desarrollado: una expresión por otra expresión

::: {.ma-block .ma-observacion #apm-t1-c01-x0003}
**Ejemplo — Sustituir una expresión completa**

:::

Consideremos:

$$
2x^2-3x+4
$$

y sustituimos:

$$
x=a+1.
$$

#### Paso 1 — Localizar todas las apariciones de $x$

Aparece en:

$$
x^2
$$

y en:

$$
-3x.
$$

#### Paso 2 — Reemplazar $x$ por la expresión completa

Escribimos:

$$
2(a+1)^2-3(a+1)+4.
$$

No escribimos:

$$
2a+1^2-3a+1+4,
$$

porque eso destruiría los agrupamientos de la expresión original.

#### Paso 3 — Decidir si necesitamos seguir

Si nuestro objetivo era únicamente realizar la sustitución, podemos detenernos aquí:

$$
\boxed{2(a+1)^2-3(a+1)+4}.
$$

No existe ninguna obligación de expandir.

Más adelante aprenderemos a transformar expresiones de forma sistemática. Por ahora es preferible separar claramente:

$$
\text{sustituir}
\qquad\text{de}\qquad
\text{simplificar o expandir}.
$$

Esta distinción evita hacer varias operaciones mentalmente al mismo tiempo.

***

### 4.9 Sustituir no es simplificar

Consideremos:

$$
3x+2
$$

y supongamos:

$$
x=a+b.
$$

La sustitución produce:

$$
3(a+b)+2.
$$

Podríamos, usando distributividad, transformar después esa expresión en:

$$
3a+3b+2.
$$

Pero son dos etapas diferentes:

#### Sustitución

$$
3x+2
\quad\longrightarrow\quad
3(a+b)+2.
$$

#### Transformación posterior

$$
3(a+b)+2
\quad\longrightarrow\quad
3a+3b+2.
$$

Mantener separadas estas acciones es un buen hábito.

::: {.ma-block .ma-intuicion}
**Idea clave**

Primero sustituimos correctamente.  
Solo después, si el problema lo requiere, simplificamos o transformamos.
:::

***

### 4.10 Un error típico: cambiar solo lo visible

Consideremos:

$$
(x+1)^2.
$$

Si:

$$
x=-2,
$$

la sustitución correcta es:

$$
((-2)+1)^2.
$$

Podemos escribirla de forma más limpia como:

$$
(-2+1)^2.
$$

Y luego:

$$
(-2+1)^2
=
(-1)^2
=
1.
$$

Un error posible sería escribir:

$$
-2+1^2.
$$

Aquí se ha perdido el hecho de que **toda** la subexpresión $x+1$ estaba elevada al cuadrado.

La sustitución no solo debe respetar el símbolo reemplazado. Debe respetar también todas las operaciones que actuaban sobre él y sobre las expresiones que lo contienen.

***

## Ejercicios

### Sustitución directa {#apm-t1-c01-e0016}

Evalúa cada expresión para el valor indicado.

#### a)

$$
3x+4,
\qquad x=2.
$$

#### b)

$$
5a-1,
\qquad a=0.
$$

#### c)

$$
2n+7,
\qquad n=-3.
$$

#### Solución

#### a)

Sustituimos:

$$
3x+4
=
3\cdot2+4.
$$

Entonces:

$$
3\cdot2+4
=
6+4
=
10.
$$

#### b)

Sustituimos:

$$
5a-1
=
5\cdot0-1.
$$

Por tanto:

$$
5\cdot0-1
=
-1.
$$

#### c)

Como $n=-3$, usamos paréntesis:

$$
2n+7
=
2(-3)+7.
$$

Entonces:

$$
2(-3)+7
=
-6+7
=
1.
$$

***

### Todas las apariciones {#apm-t1-c01-e0017}

Evalúa:

$$
x^2+4x+3
$$

cuando:

$$
x=2.
$$

Explica por qué hay que sustituir dos veces.

#### Solución

La letra $x$ aparece en:

$$
x^2
$$

y en:

$$
4x.
$$

Como:

$$
x=2,
$$

debemos reemplazar ambas apariciones:

$$
x^2+4x+3
\quad\longrightarrow\quad
2^2+4\cdot2+3.
$$

Evaluamos:

$$
2^2+4\cdot2+3
=
4+8+3
=
15.
$$

Hay que sustituir dos veces porque ambas apariciones del símbolo $x$ representan el mismo valor fijado para esta evaluación.

***

### El peligro del signo negativo {#apm-t1-c01-e0018}

Evalúa:

$$
x^2-2x
$$

cuando:

$$
x=-4.
$$

Después explica por qué sería incorrecto escribir:

$$
-4^2-2(-4).
$$

#### Solución

Sustituimos el valor completo $-4$ usando paréntesis:

$$
x^2-2x
\quad\longrightarrow\quad
(-4)^2-2(-4).
$$

Ahora calculamos:

$$
(-4)^2=16
$$

y:

$$
-2(-4)=8.
$$

Por tanto:

$$
(-4)^2-2(-4)
=
16+8
=
24.
$$

La escritura:

$$
-4^2
$$

no representa el cuadrado de $-4$.

Representa:

$$
-(4^2)=-16.
$$

Por eso eliminar los paréntesis cambiaría la estructura y produciría una evaluación incorrecta.

***

### Dos variables {#apm-t1-c01-e0019}

Evalúa:

$$
a^2+2ab+b^2
$$

cuando:

$$
a=3,
\qquad
b=-2.
$$

#### Solución

Sustituimos cada símbolo por su valor:

$$
a^2+2ab+b^2
\quad\longrightarrow\quad
3^2+2\cdot3(-2)+(-2)^2.
$$

Calculamos:

$$
3^2=9,
$$

$$
2\cdot3(-2)=-12,
$$

y:

$$
(-2)^2=4.
$$

Entonces:

$$
9-12+4
=
1.
$$

Por tanto, el valor es:

$$
\boxed{1}.
$$

***

### Sustituir una expresión {#apm-t1-c01-e0020}

En:

$$
x^2+3x
$$

sustituye:

$$
x=a-1.
$$

No expandas el resultado.

#### Solución

La letra $x$ aparece dos veces.

Reemplazamos cada aparición por la expresión completa $a-1$:

$$
x^2+3x
\quad\longrightarrow\quad
(a-1)^2+3(a-1).
$$

Como el ejercicio pide únicamente sustituir, nos detenemos:

$$
\boxed{(a-1)^2+3(a-1)}.
$$

No es necesario expandir.

***

### Detectar una sustitución incorrecta {#apm-t1-c01-e0021}

Un estudiante quiere sustituir:

$$
x=-2
$$

en:

$$
3x^2+1.
$$

Escribe:

$$
3(-2^2)+1.
$$

1. ¿Qué parte de la escritura es problemática?
2. Corrige la sustitución.
3. Evalúa correctamente.

#### Solución

#### 1. El problema

La potencia debe actuar sobre el valor completo de $x$.

El estudiante escribió:

$$
-2^2,
$$

que significa:

$$
-(2^2).
$$

#### 2. Sustitución correcta

Debemos escribir:

$$
3(-2)^2+1.
$$

#### 3. Evaluación

Tenemos:

$$
(-2)^2=4.
$$

Entonces:

$$
3(-2)^2+1
=
3\cdot4+1
=
13.
$$

La evaluación correcta es:

$$
\boxed{13}.
$$

***

### Sustitución o transformación {#apm-t1-c01-e0022}

Considera:

$$
4x-3
$$

y sustituye:

$$
x=a+b.
$$

Un estudiante escribe directamente:

$$
4a+4b-3.
$$

1. ¿Es correcta esa expresión final?
2. ¿Qué paso intermedio conviene escribir?
3. ¿Por qué es útil separar sustitución y transformación?

#### Solución

#### 1. La expresión final

Sí, la expresión:

$$
4a+4b-3
$$

puede obtenerse correctamente usando distributividad.

#### 2. Paso intermedio

Sin embargo, la sustitución propiamente dicha produce primero:

$$
4(a+b)-3.
$$

Después podemos transformar:

$$
4(a+b)-3
=
4a+4b-3.
$$

#### 3. Razón pedagógica

Separar las etapas permite comprobar dos cosas distintas:

- que hemos reemplazado correctamente $x$ por toda la expresión $a+b$;
- que la transformación posterior usa una ley válida.

Escribir todo de una vez puede ocultar dónde apareció un error.

***

## Resumen de la sección

En esta sección hemos introducido una operación básica del lenguaje algebraico: la sustitución.

La regla principal es:

$$
\boxed{
\text{sustituir}
=
\text{reemplazar un símbolo conservando la estructura}.
}
$$

Hemos aprendido que:

- hay que sustituir todas las apariciones relevantes del símbolo;
- los números negativos suelen requerir paréntesis;
- el cero se sustituye igual que cualquier otro valor;
- podemos sustituir varias letras a la vez;
- una variable puede sustituirse por una expresión completa;
- sustituir y simplificar son operaciones conceptualmente distintas.

La definición nueva es:

::: {.ma-block .ma-observacion}
**Síntesis**

**Evaluar una expresión** para valores dados consiste en sustituir esos valores en las apariciones correspondientes y, cuando sea posible, realizar las operaciones resultantes.
:::

El hábito que queremos conservar es:

$$
\boxed{
\text{primero sustituir correctamente}
\longrightarrow
\text{después calcular o transformar}.
}
$$

***

## Hacia la sección siguiente

Durante toda esta sección hemos escrito cadenas como:

$$
3\cdot2+4
=
6+4
=
10.
$$

También hemos escrito:

$$
(-3)^2+2(-3)+1
=
9-6+1
=
4.
$$

El signo

$$
=
$$

ha aparecido constantemente.

Pero todavía no nos hemos detenido a preguntar qué está afirmando.

¿Significa «ahora calculo»?

¿Significa «el resultado es»?

Si escribimos:

$$
3+4=7\cdot2=14,
$$

¿qué tiene de incorrecto, si tanto $3+4=7$ como $7\cdot2=14$ son cálculos correctos?

La próxima sección estará dedicada por completo a esa pregunta:

## §5. Igualdad: una afirmación, no una orden

En las secciones anteriores hemos usado el signo igual muchas veces:

$$
3+4\cdot5=23,
$$

$$
(-3)^2+2(-3)+1=4,
$$

$$
3\cdot2+4=10.
$$

Hasta ahora lo hemos utilizado de manera natural, sin detenernos demasiado en él.

Pero el signo

$$
=
$$

es uno de los símbolos más importantes de toda la matemática.

Y también uno de los que peor se aprende si se interpreta solamente como una señal que significa:

> «ahora viene el resultado».

Consideremos esta cadena:

$$
3+4=7\cdot2=14.
$$

A primera vista puede parecer razonable.

En efecto:

$$
3+4=7
$$

es correcto, y

$$
7\cdot2=14
$$

también es correcto.

Sin embargo, la cadena completa

$$
3+4=7\cdot2=14
$$

es falsa.

¿Por qué?

Porque el signo igual no significa:

> «hago esta operación y después hago otra».

Cada signo igual afirma que las expresiones que conecta representan el mismo valor.

La cadena anterior afirma, entre otras cosas, que:

$$
3+4=14,
$$

es decir,

$$
7=14,
$$

lo cual es falso.

La primera idea de esta sección será, por tanto:

::: {.ma-block .ma-intuicion}
**Idea clave**

El signo $=$ no es una orden de cálculo ni una flecha de proceso.  
Es una afirmación de igualdad.
:::

***

### 5.1 Qué significa escribir \(A=B\)

Consideremos:

$$
2+5=7.
$$

A la izquierda tenemos la expresión:

$$
2+5.
$$

A la derecha tenemos:

$$
7.
$$

Ambas expresiones representan el mismo número.

Eso es exactamente lo que afirma:

$$
2+5=7.
$$

Podemos hacer lo mismo con expresiones más complicadas:

$$
3(4+2)=18.
$$

La igualdad afirma que:

$$
3(4+2)
$$

y

$$
18
$$

representan el mismo valor.

::: {.ma-block .ma-definicion #apm-t1-c01-d0005}
**Definición — Igualdad**

Una **igualdad** es una afirmación de que dos expresiones representan el mismo objeto o el mismo valor en el contexto considerado.
:::

En este capítulo trabajaremos principalmente con igualdades entre expresiones numéricas o algebraicas.

Más adelante veremos que el concepto de igualdad puede aplicarse a muchas clases de objetos matemáticos.

Por ahora basta conservar la idea esencial:

$$
\boxed{
A=B
\quad\text{afirma que }A\text{ y }B\text{ representan lo mismo}.
}
$$

***

### 5.2 El signo igual no significa «da»

En el lenguaje cotidiano de una clase es frecuente escuchar:

> «tres más cuatro da siete».

Como frase verbal no hay ningún problema especial.

El problema aparece cuando empezamos a interpretar el símbolo $=$ como si significara literalmente «da».

Por ejemplo, alguien podría escribir:

$$
3+4=7\times2=14.
$$

Su razonamiento mental quizá sea:

1. $3+4$ da $7$;
2. después multiplico por $2$;
3. eso da $14$.

El cálculo que quería realizar podría escribirse, por ejemplo, como:

$$
(3+4)\cdot2.
$$

Entonces una cadena correcta sería:

$$
(3+4)\cdot2
=
7\cdot2
=
14.
$$

Ahora sí todos los miembros representan el mismo número:

$$
14.
$$

La diferencia es fundamental.

En la escritura incorrecta:

$$
3+4=7\cdot2=14,
$$

la expresión inicial vale $7$, mientras que las siguientes valen $14$.

En la escritura correcta:

$$
(3+4)\cdot2
=
7\cdot2
=
14,
$$

todos los miembros valen $14$.

Por tanto:

$$
\boxed{
\text{una cadena de igualdades debe conservar el mismo valor a lo largo de toda la cadena}.
}
$$

***

### 5.3 Leer una igualdad en ambas direcciones

Si:

$$
2+5=7,
$$

también podemos escribir:

$$
7=2+5.
$$

Ambas escrituras afirman exactamente la misma igualdad.

Esto refleja una propiedad fundamental llamada **simetría de la igualdad**.

De manera informal:

> si una expresión $A$ es igual a una expresión $B$, entonces $B$ es igual a $A$.

Podemos expresarlo sin introducir todavía notación lógica:

> si $A=B$, entonces $B=A$.

La idea que debemos conservar es sencilla:

$$
\boxed{
A=B
\quad\text{y}\quad
B=A
}
$$

expresan la misma relación de igualdad.

Esto nos ayuda a abandonar otra mala intuición: que el lado izquierdo de una igualdad es siempre «el problema» y el lado derecho siempre «la respuesta».

Por ejemplo,

$$
12=3\cdot4
$$

es tan legítimo como:

$$
3\cdot4=12.
$$

***

### 5.4 Cadenas de igualdades

Consideremos:

$$
18
=
3\cdot6
=
3(4+2)
=
3\cdot4+3\cdot2.
$$

Si cada miembro representa el mismo valor, la cadena es correcta.

Comprobemos:

$$
18=18,
$$

$$
3\cdot6=18,
$$

$$
3(4+2)=18,
$$

$$
3\cdot4+3\cdot2=12+6=18.
$$

Todos los miembros representan el número $18$.

Una cadena

$$
A=B=C
$$

debe leerse como una abreviatura compacta de afirmaciones compatibles:

$$
A=B
$$

y

$$
B=C.
$$

Y, como consecuencia, también:

$$
A=C.
$$

Esta propiedad se llama **transitividad de la igualdad**.

En lenguaje ordinario:

> si $A$ es igual a $B$ y $B$ es igual a $C$, entonces $A$ es igual a $C$.

En palabras:

> si $A=B$ y $B=C$, entonces $A=C$.

No necesitamos demostrar formalmente esta propiedad aquí. La utilizaremos como una característica básica de la igualdad.

***

### 5.5 Una cadena correcta cuenta una sola historia

Observa:

$$
\begin{aligned}
5(3+2)
&=5\cdot5\\
&=25.
\end{aligned}
$$

Esta escritura puede leerse así:

> la expresión $5(3+2)$ representa el mismo número que $5\cdot5$, y este representa el mismo número que $25$.

La cadena conserva un solo valor.

Ahora comparemos:

$$
5+3=8\cdot2=16.
$$

Aquí los valores son:

$$
5+3=8,
$$

pero:

$$
8\cdot2=16.
$$

La cadena cambia de $8$ a $16$.

El problema no es que «el segundo cálculo esté mal». El problema es que se usó el signo igual para unir etapas que **no son iguales entre sí**.

Cuando queremos describir un procedimiento donde el objeto cambia, podemos:

- escribir una nueva línea;
- usar palabras;
- definir una nueva expresión;
- emplear, cuando corresponda, otro símbolo adecuado.

Pero no debemos utilizar $=$ para significar simplemente «y después».

***

### 5.6 Ejemplo desarrollado: reparar una cadena

::: {.ma-block .ma-observacion #apm-t1-c01-x0004}
**Ejemplo — Una cadena de igualdades debe conservar el valor**

:::

Un estudiante quiere calcular:

$$
(6+2)\cdot3.
$$

Escribe:

$$
6+2=8\cdot3=24.
$$

Analicemos la escritura.

#### Paso 1 — Revisar el primer miembro

Tenemos:

$$
6+2=8.
$$

Hasta aquí:

$$
6+2=8
$$

es correcto.

#### Paso 2 — Revisar el segundo enlace

La cadena continúa:

$$
8=8\cdot3.
$$

Pero:

$$
8\cdot3=24.
$$

Así que la cadena estaría afirmando:

$$
8=24.
$$

Eso es falso.

#### Paso 3 — Identificar qué se quería calcular

La expresión original era:

$$
(6+2)\cdot3.
$$

El factor $3$ debe permanecer presente desde el comienzo de la cadena.

#### Paso 4 — Escribir una cadena correcta

Podemos escribir:

$$
\begin{aligned}
(6+2)\cdot3
&=8\cdot3\\
&=24.
\end{aligned}
$$

Ahora cada miembro tiene el mismo valor:

$$
24.
$$

#### Lección

El error no estaba en sumar $6+2$ ni en multiplicar $8\cdot3$.

Estaba en el significado atribuido al signo igual.

$$
\boxed{
\text{el signo }=\text{ no enlaza pasos; enlaza expresiones iguales}.
}
$$

***

### 5.7 Igualdades verdaderas e igualdades falsas

Una escritura con signo igual hace una afirmación.

Por eso puede ocurrir que esa afirmación sea correcta o incorrecta.

Por ejemplo:

$$
4+5=9
$$

es una igualdad correcta.

En cambio:

$$
4+5=10
$$

es una igualdad falsa.

Cuando aparecen letras, la situación puede depender del valor representado.

Por ejemplo:

$$
x+2=5.
$$

Si sustituimos:

$$
x=3,
$$

obtenemos:

$$
3+2=5,
$$

que es correcto.

Si sustituimos:

$$
x=4,
$$

obtenemos:

$$
4+2=5,
$$

que es falso.

No estudiaremos todavía sistemáticamente esta dependencia. En §6 distinguiremos dos tipos importantes de igualdades con letras: las **identidades** y las **ecuaciones**.

Por ahora queremos advertir solamente:

::: {.ma-block .ma-observacion}
**Observación**

Una escritura con $=$ no es automáticamente correcta por el mero hecho de estar escrita. Es una afirmación matemática que debe interpretarse y, cuando sea necesario, justificarse.
:::

***

### 5.8 El formato vertical ayuda a pensar

Las cadenas largas pueden escribirse en una sola línea:

$$
3(4+2)=3\cdot6=18.
$$

Pero cuando el cálculo crece, suele ser más claro escribir:

$$
\begin{aligned}
3(4+2)
&=3\cdot6\\
&=18.
\end{aligned}
$$

Este formato tiene varias ventajas:

1. mantiene visible la expresión que estamos transformando;
2. coloca los signos igual en una misma columna;
3. facilita comprobar que cada línea conserva el mismo valor;
4. deja espacio para justificar transformaciones más adelante.

Por ejemplo:

$$
\begin{aligned}
2(5+3)+1
&=2\cdot8+1\\
&=16+1\\
&=17.
\end{aligned}
$$

Cada línea representa el mismo número.

En §7 utilizaremos este formato para añadir, junto a cada paso, la ley algebraica que lo justifica.

***

### 5.9 Igualdad no significa aproximación

La igualdad es una afirmación exacta.

Por ejemplo:

$$
\frac13+\frac23=1.
$$

Pero una escritura decimal truncada como:

$$
\frac13=0.33
$$

no es exacta.

El número:

$$
\frac13
$$

tiene desarrollo decimal:

$$
0.3333\ldots
$$

Por tanto, si queremos indicar que $0.33$ es una aproximación, no debemos escribir una igualdad exacta.

Más adelante fijaremos con detalle la notación de aproximación. Por ahora basta saber que:

$$
\boxed{
=\text{ expresa igualdad, no mera cercanía numérica}.
}
$$

Esta precisión evita usar el mismo símbolo para relaciones matemáticas diferentes.

***

## Ejercicios

### ¿Es correcta la cadena? {#apm-t1-c01-e0023}

Decide si cada cadena de igualdades es correcta. Justifica tu respuesta.

#### a)

$$
4+5=9=3^2.
$$

#### b)

$$
4+5=9\cdot2=18.
$$

#### c)

$$
2(3+4)=2\cdot7=14.
$$

#### d)

$$
20-5=15+1=16.
$$

#### Solución

#### a)

Tenemos:

$$
4+5=9
$$

y:

$$
3^2=9.
$$

Todos los miembros representan $9$.

Por tanto:

$$
4+5=9=3^2
$$

es correcta.

#### b)

El primer miembro vale:

$$
4+5=9.
$$

Pero:

$$
9\cdot2=18.
$$

La cadena estaría afirmando:

$$
9=18.
$$

Por tanto, es incorrecta.

#### c)

Tenemos:

$$
2(3+4)
=
2\cdot7
=
14.
$$

Todos los miembros representan $14$.

La cadena es correcta.

#### d)

Tenemos:

$$
20-5=15,
$$

pero:

$$
15+1=16.
$$

La cadena afirma:

$$
15=16.
$$

Por tanto, es incorrecta.

***

### Reparar una escritura {#apm-t1-c01-e0024}

Un estudiante quiere calcular:

$$
(9-4)\cdot6
$$

y escribe:

$$
9-4=5\cdot6=30.
$$

1. Explica el error.
2. Escribe una cadena correcta.

#### Solución

La escritura comienza con:

$$
9-4=5,
$$

que es correcta.

Pero después une mediante $=$:

$$
5
$$

con:

$$
5\cdot6=30.
$$

Eso implicaría:

$$
5=30,
$$

lo cual es falso.

El factor $6$ pertenecía a la expresión original y debe permanecer presente durante la transformación.

La cadena correcta es:

$$
\begin{aligned}
(9-4)\cdot6
&=5\cdot6\\
&=30.
\end{aligned}
$$

***

### Leer la igualdad al revés {#apm-t1-c01-e0025}

Reescribe cada igualdad intercambiando sus dos miembros.

#### a)

$$
7+5=12.
$$

#### b)

$$
3(2+4)=18.
$$

#### c)

$$
x+2=5.
$$

¿Qué propiedad de la igualdad estamos utilizando?

#### Solución

#### a)

$$
12=7+5.
$$

#### b)

$$
18=3(2+4).
$$

#### c)

$$
5=x+2.
$$

Estamos utilizando la **simetría de la igualdad**: si $A=B$, entonces también $B=A$.

No hemos cambiado el contenido de la afirmación.

***

### Completar una cadena {#apm-t1-c01-e0026}

Completa los espacios para obtener una cadena correcta:

$$
4(3+2)
=
4\cdot\boxed{\phantom{5}}
=
\boxed{\phantom{20}}.
$$

Después explica por qué los tres miembros son iguales.

#### Solución

Primero:

$$
3+2=5.
$$

Por tanto:

$$
4(3+2)
=
4\cdot5.
$$

Después:

$$
4\cdot5=20.
$$

La cadena completa es:

$$
4(3+2)
=
4\cdot5
=
20.
$$

Los tres miembros representan el mismo número, $20$.

***

### Encontrar el primer error {#apm-t1-c01-e0027}

Un estudiante escribe:

$$
\begin{aligned}
2(6+1)+3
&=2\cdot7+3\\
&=14\\
&=17.
\end{aligned}
$$

1. ¿Cuál es la primera línea incorrecta?
2. ¿Qué se perdió?
3. Corrige el cálculo.

#### Solución

La primera línea es correcta:

$$
2(6+1)+3
=
2\cdot7+3.
$$

La siguiente línea afirma:

$$
2\cdot7+3=14.
$$

Pero:

$$
2\cdot7+3
=
14+3
=
17.
$$

Por tanto, el primer error aparece al pasar a:

$$
14.
$$

Se perdió el término $+3$.

Una cadena correcta es:

$$
\begin{aligned}
2(6+1)+3
&=2\cdot7+3\\
&=14+3\\
&=17.
\end{aligned}
$$

Todas las líneas representan $17$.

***

### Igualdad exacta o no {#apm-t1-c01-e0028}

Decide cuáles de estas escrituras expresan una igualdad exacta.

#### a)

$$
\frac12=0.5
$$

#### b)

$$
\frac13=0.33
$$

#### c)

$$
2^3=8
$$

#### d)

$$
10\div4=2.5
$$

#### Solución

#### a)

$$
\frac12=0.5
$$

es exacta.

#### b)

$$
\frac13=0.33
$$

no es exacta.

En efecto:

$$
\frac13=0.3333\ldots
$$

mientras que $0.33$ es una aproximación truncada.

#### c)

$$
2^3=8
$$

es exacta.

#### d)

$$
10\div4=2.5
$$

es exacta, porque:

$$
\frac{10}{4}
=
\frac52
=
2.5.
$$

***

## Resumen de la sección

El signo igual tiene un significado preciso:

::: {.ma-block .ma-observacion}
**Síntesis**

Una **igualdad** afirma que dos expresiones representan el mismo objeto o el mismo valor en el contexto considerado.
:::

Por tanto:

$$
A=B
$$

no significa:

> «a partir de $A$, ahora hago $B$».

Significa:

> «$A$ y $B$ representan lo mismo».

Hemos aprendido además que:

- la igualdad puede leerse en ambas direcciones;
- si $A=B$ y $B=C$, entonces $A=C$;
- una cadena de igualdades debe conservar el mismo valor;
- una igualdad puede ser correcta o falsa;
- el signo $=$ expresa igualdad exacta, no aproximación.

La regla de escritura fundamental es:

$$
\boxed{
A=B=C
\quad\text{solo si todos los miembros representan lo mismo}.
}
$$

Este principio será indispensable cuando comencemos a transformar expresiones algebraicas más complejas.

***

## Hacia la sección siguiente

Consideremos ahora dos escrituras:

$$
2(x+3)=2x+6
$$

y

$$
2x+3=11.
$$

Ambas contienen el signo igual.

Sin embargo, parecen afirmar cosas diferentes.

La primera expresa una relación que esperamos conservar al sustituir distintos valores de $x$.

La segunda parece imponer una condición particular sobre $x$.

¿Qué diferencia hay entre ellas?

¿En qué sentido una igualdad puede ser válida de manera general y otra depender de valores especiales?

Estas preguntas conducen a la siguiente distinción:

## §6. Identidad y ecuación: primera distinción

En la sección anterior aprendimos que una igualdad es una afirmación:

$$
A=B
$$

dice que las expresiones $A$ y $B$ representan lo mismo en el contexto considerado.

Ahora comparemos dos igualdades que contienen la misma letra:

$$
2(x+3)=2x+6
$$

y

$$
2x+3=11.
$$

Ambas tienen un signo igual. Ambas contienen $x$. Sin embargo, no cumplen la misma función.

Probemos algunos valores en la primera.

Si $x=0$:

$$
2(0+3)=2\cdot0+6,
$$

es decir,

$$
6=6.
$$

Si $x=2$:

$$
2(2+3)=2\cdot2+6,
$$

y obtenemos:

$$
10=10.
$$

Si $x=-5$:

$$
2(-5+3)=2(-5)+6,
$$

de modo que:

$$
-4=-4.
$$

La igualdad sigue funcionando.

Consideremos ahora:

$$
2x+3=11.
$$

Si $x=4$:

$$
2\cdot4+3=11,
$$

y obtenemos:

$$
11=11.
$$

Pero si $x=3$:

$$
2\cdot3+3=11,
$$

es decir,

$$
9=11,
$$

que es falso.

Parece haber, por tanto, dos situaciones distintas:

- una igualdad que expresa un patrón general;
- una igualdad que impone una condición sobre el valor de la letra.

Esta es la primera distinción que queremos aprender.

***

### 6.1 Una igualdad que expresa un patrón general

Volvamos a:

$$
2(x+3)=2x+6.
$$

La igualdad no está intentando descubrir un valor particular de $x$.

Expresa una relación que esperamos que sea válida cada vez que sustituimos un valor permitido para $x$.

Esto ocurre porque estamos reconociendo una estructura conocida:

$$
2(x+3)
$$

puede transformarse mediante la distributividad en:

$$
2x+2\cdot3,
$$

es decir,

$$
2x+6.
$$

La igualdad expresa, por tanto, un mismo patrón algebraico.

::: {.ma-block .ma-definicion #apm-t1-c01-d0006}
**Definición — Identidad**

En este primer sentido operativo, una **identidad** es una igualdad que es válida para todos los valores permitidos de las letras que aparecen en ella, dentro del contexto considerado.
:::

La expresión «dentro del contexto considerado» vuelve a ser importante.

Por ejemplo, una igualdad que contenga una división puede exigir que ciertos valores no se utilicen. Más adelante aprenderemos a formular con precisión esas restricciones.

Por ahora trabajaremos con ejemplos elementales donde los valores permitidos son claros.

Otros ejemplos familiares de identidades son:

$$
a+0=a
$$

o:

$$
3(a+b)=3a+3b.
$$

En estos casos las letras no representan valores especiales que debamos descubrir. Representan valores generales dentro del contexto.

***

### 6.2 Probar casos no basta para demostrar una identidad

Supongamos que queremos saber si:

$$
x^2+x=x(x+1)
$$

es una identidad.

Podemos probar:

$$
x=1,
$$

y obtenemos:

$$
1^2+1=1(1+1),
$$

es decir:

$$
2=2.
$$

También podemos probar:

$$
x=2:
$$

$$
2^2+2=2(2+1),
$$

de modo que:

$$
6=6.
$$

Y con $x=-3$:

$$
(-3)^2+(-3)=(-3)(-3+1),
$$

por lo que:

$$
6=6.
$$

Estos ejemplos son compatibles con la idea de que tenemos una identidad.

Pero todavía no constituyen una demostración.

¿Por qué?

Porque hemos examinado solamente algunos valores. Una afirmación que pretende valer de manera general no queda establecida por una lista finita de comprobaciones.

Para justificar la igualdad debemos entender su estructura:

$$
x(x+1)
$$

se transforma por distributividad en:

$$
x^2+x.
$$

Esa razón algebraica explica por qué la igualdad no depende de haber elegido $1$, $2$ o $-3$.

::: {.ma-block .ma-intuicion}
**Idea clave**

Probar ejemplos puede **comprobar casos** y detectar errores, pero no demuestra por sí solo que una igualdad sea una identidad.
:::

Esta diferencia entre evidencia y demostración se volverá central en el capítulo 5.

***

### 6.3 Una igualdad que impone una condición

Consideremos ahora:

$$
2x+3=11.
$$

Aquí no afirmamos que la igualdad sea correcta para cualquier valor que demos a $x$.

La igualdad impone una condición.

Algunos valores la hacen verdadera y otros no.

Ya vimos que:

$$
x=4
$$

produce:

$$
11=11,
$$

mientras que:

$$
x=3
$$

produce:

$$
9=11.
$$

En este tipo de problema, la letra representa un valor que debe cumplir la igualdad.

::: {.ma-block .ma-definicion #apm-t1-c01-d0007}
**Definición — Ecuación**

En este primer sentido operativo, una **ecuación** es una igualdad en la que una o más letras se tratan como valores por determinar y se pregunta qué valores permitidos hacen verdadera la igualdad.
:::

No estudiaremos todavía métodos sistemáticos para encontrar esos valores.

Ese será el objetivo principal del capítulo 11.

Por ahora solo queremos reconocer qué clase de pregunta plantea una ecuación.

***

### 6.4 Identidad y ecuación no se distinguen solo por su apariencia

Considera:

$$
x+x=2x.
$$

Si la presentamos como una regla general del cálculo algebraico, la estamos usando como identidad.

Pero imaginemos una pregunta distinta:

> ¿Para qué valores de $x$ es verdadera la igualdad $x+x=2x$?

La misma escritura puede aparecer dentro de una pregunta sobre valores que satisfacen una igualdad.

En este caso descubriríamos que todos los valores permitidos la satisfacen.

Esto muestra una sutileza importante:

::: {.ma-block .ma-intuicion}
**Idea clave**

«Identidad» y «ecuación» no son etiquetas que podamos decidir siempre observando únicamente la forma de los símbolos. También importa **qué se está afirmando o preguntando**.
:::

En este capítulo usaremos normalmente:

- **identidad** cuando la intención sea expresar una igualdad general;
- **ecuación** cuando la intención sea determinar qué valores hacen verdadera una igualdad.

Más adelante podremos formular esta distinción con herramientas lógicas más precisas.

***

### 6.5 Una ecuación puede ser verdadera para un valor y falsa para otro

Consideremos:

$$
x^2=9.
$$

Si $x=3$:

$$
3^2=9,
$$

que es verdadero.

Si $x=-3$:

$$
(-3)^2=9,
$$

que también es verdadero.

Si $x=2$:

$$
2^2=9,
$$

es decir:

$$
4=9,
$$

que es falso.

No necesitamos resolver sistemáticamente esta ecuación para comprender su carácter.

La igualdad no está afirmando que:

$$
x^2=9
$$

sea válida para cualquier valor de $x$.

Está imponiendo una condición.

Este tipo de lectura será esencial cuando lleguemos a estudiar ecuaciones con precisión.

***

### 6.6 Ejemplo desarrollado: dos igualdades, dos funciones

::: {.ma-block .ma-observacion #apm-t1-c01-x0005}
**Ejemplo — Identidad frente a ecuación**

:::

Comparemos:

$$
3(x+2)=3x+6
$$

y

$$
3x+2=14.
$$

#### Primera igualdad

Probemos primero algunos valores en:

$$
3(x+2)=3x+6.
$$

Para $x=0$:

$$
3(0+2)=3\cdot0+6,
$$

por tanto:

$$
6=6.
$$

Para $x=5$:

$$
3(5+2)=3\cdot5+6,
$$

de modo que:

$$
21=21.
$$

Estos casos son compatibles con una identidad.

Pero la razón decisiva es estructural:

$$
3(x+2)
=
3x+3\cdot2
=
3x+6.
$$

La distributividad justifica la igualdad de manera general.

Por tanto, en el contexto usual:

$$
\boxed{3(x+2)=3x+6}
$$

es una identidad.

#### Segunda igualdad

Consideremos:

$$
3x+2=14.
$$

Si $x=4$:

$$
3\cdot4+2=14,
$$

y obtenemos:

$$
14=14.
$$

Si $x=3$:

$$
3\cdot3+2=14,
$$

es decir:

$$
11=14.
$$

La igualdad no es válida para cualquier valor.

Está imponiendo una condición sobre $x$.

Por tanto, en este contexto:

$$
\boxed{3x+2=14}
$$

es una ecuación.

#### Comparación

En la identidad preguntamos esencialmente:

> ¿qué relación general expresan estas dos formas?

En la ecuación preguntamos:

> ¿qué valores hacen verdadera esta igualdad?

Esa es la distinción fundamental de la sección.

***

### 6.7 Un contraejemplo puede descartar una supuesta identidad

Supongamos que alguien afirma:

$$
(a+b)^2=a^2+b^2.
$$

y sostiene que se trata de una identidad.

No necesitamos comprobar todos los valores posibles para demostrar que la afirmación es falsa.

Basta encontrar un caso donde falle.

Tomemos:

$$
a=1,
\qquad
b=1.
$$

El lado izquierdo vale:

$$
(1+1)^2=4.
$$

El lado derecho vale:

$$
1^2+1^2=2.
$$

Por tanto:

$$
4\ne2.
$$

La igualdad no puede ser una identidad.

Este razonamiento introduce una idea que estudiaremos con más profundidad después:

$$
\boxed{
\text{un solo caso donde falle basta para refutar una afirmación que pretende valer siempre}.
}
$$

Todavía no desarrollaremos formalmente el método del contraejemplo. Lo utilizaremos aquí únicamente como herramienta de diagnóstico.

***

### 6.8 Tres preguntas distintas ante una igualdad con letras

Cuando encontremos una igualdad que contiene letras, conviene preguntar:

#### 1. ¿Qué papel tienen las letras?

¿Representan valores generales, valores fijados o valores por determinar?

#### 2. ¿Qué pretende la igualdad?

¿Expresa un patrón general o impone una condición?

#### 3. ¿Cómo se justifica?

Si pretendemos que sea una identidad, ¿existe una ley algebraica que explique la igualdad?

Si estamos ante una ecuación, ¿qué valores hacen verdadera la igualdad?

Estas tres preguntas evitan una lectura mecánica de los símbolos.

***

## Ejercicios

### Identidad o ecuación {#apm-t1-c01-e0029}

En cada caso, indica si la escritura se está usando como identidad o como ecuación. Explica tu decisión.

#### a)

> La distributividad permite escribir:

$$
5(a+b)=5a+5b.
$$

#### b)

> Determina qué valor de $x$ hace verdadera:

$$
5x+2=17.
$$

#### c)

> La suma con cero cumple:

$$
n+0=n.
$$

#### d)

> ¿Qué valores de $y$ hacen verdadera:

$$
y^2=16?
$$

#### Solución

#### a)

La igualdad expresa un patrón general basado en la distributividad.

Se está usando como **identidad**.

#### b)

La igualdad impone una condición y la pregunta pide determinar el valor de $x$ que la satisface.

Se está usando como **ecuación**.

#### c)

La igualdad expresa una regla general de la suma.

Se está usando como **identidad**.

#### d)

La pregunta pide determinar qué valores hacen verdadera la igualdad.

Se está usando como **ecuación**.

***

### Comprobar valores en una ecuación {#apm-t1-c01-e0030}

Considera:

$$
2x+5=13.
$$

Decide si cada valor hace verdadera la igualdad:

1. $x=2$;
2. $x=4$;
3. $x=-4$.

No desarrolles un método general para resolver la ecuación; basta sustituir y comprobar.

#### Solución

#### 1. \(x=2\)

Sustituimos:

$$
2\cdot2+5=13.
$$

El lado izquierdo vale:

$$
4+5=9.
$$

Obtenemos:

$$
9=13,
$$

que es falso.

Por tanto, $x=2$ no hace verdadera la ecuación.

#### 2. \(x=4\)

Sustituimos:

$$
2\cdot4+5=13.
$$

Entonces:

$$
8+5=13.
$$

Obtenemos:

$$
13=13,
$$

que es verdadero.

Por tanto, $x=4$ sí hace verdadera la ecuación.

#### 3. \(x=-4\)

Sustituimos:

$$
2(-4)+5=13.
$$

Entonces:

$$
-8+5=-3.
$$

Obtenemos:

$$
-3=13,
$$

que es falso.

Por tanto, $x=-4$ no hace verdadera la ecuación.

***

### ¿Bastan tres casos? {#apm-t1-c01-e0031}

Un estudiante quiere demostrar que:

$$
4(x+1)=4x+4
$$

es una identidad.

Comprueba la igualdad para:

$$
x=0,\qquad x=1,\qquad x=10
$$

y concluye:

> «Como funcionó tres veces, ya está demostrada».

1. Comprueba los tres casos.
2. Explica por qué la conclusión del estudiante no está justificada solo por esas comprobaciones.
3. Indica qué ley algebraica explica la igualdad general.

#### Solución

#### 1. Comprobaciones

Para $x=0$:

$$
4(0+1)=4\cdot0+4,
$$

por lo que:

$$
4=4.
$$

Para $x=1$:

$$
4(1+1)=4\cdot1+4,
$$

de modo que:

$$
8=8.
$$

Para $x=10$:

$$
4(10+1)=4\cdot10+4,
$$

y obtenemos:

$$
44=44.
$$

Los tres casos funcionan.

#### 2. Por qué no basta

La identidad pretende ser válida para todos los valores permitidos de $x$.

Comprobar tres valores verifica únicamente esos tres casos.

Podría existir otro valor donde una igualdad distinta fallara.

Por tanto, los ejemplos aportan evidencia, pero no constituyen por sí solos una demostración general.

#### 3. Ley que lo explica

La distributividad da:

$$
4(x+1)
=
4x+4\cdot1
=
4x+4.
$$

Esta es la razón estructural que justifica la identidad.

***

### Refutar una supuesta identidad {#apm-t1-c01-e0032}

Un estudiante afirma que:

$$
(a-b)^2=a^2-b^2
$$

es una identidad.

Encuentra valores sencillos de $a$ y $b$ que muestren que la afirmación es falsa.

#### Solución

Podemos elegir:

$$
a=2,
\qquad
b=1.
$$

El lado izquierdo es:

$$
(2-1)^2=1.
$$

El lado derecho es:

$$
2^2-1^2
=
4-1
=
3.
$$

Por tanto:

$$
1\ne3.
$$

Así, la igualdad no puede ser una identidad.

No necesitamos examinar todos los valores: un solo caso donde falle basta para descartar una afirmación que pretendía valer siempre.

***

### La misma escritura, distinta pregunta {#apm-t1-c01-e0033}

Considera:

$$
x+x=2x.
$$

#### a)

Interprétala como una identidad y explica qué afirma.

#### b)

Interprétala como una ecuación mediante la pregunta:

> «¿Qué valores de $x$ hacen verdadera esta igualdad?»

#### c)

Explica qué enseña este ejemplo sobre las palabras «identidad» y «ecuación».

#### Solución

#### a)

Como identidad, la igualdad expresa que sumar un número consigo mismo produce el doble de ese número:

$$
x+x=2x.
$$

La intención es formular un patrón general.

#### b)

Como ecuación, preguntamos qué valores de $x$ hacen verdadera la igualdad.

En este caso, la misma ley algebraica muestra que la igualdad se cumple para todos los valores permitidos en el contexto usual.

No necesitamos construir todavía un conjunto formal de soluciones.

#### c)

El ejemplo muestra que «identidad» y «ecuación» no se distinguen únicamente por la apariencia de la escritura.

También importa la función que cumple la igualdad:

- expresar una relación general;
- o plantear una pregunta sobre los valores que la hacen verdadera.

***

## Resumen de la sección

En esta sección hemos distinguido dos usos fundamentales de las igualdades con letras.

::: {.ma-block .ma-observacion}
**Síntesis**

Una **identidad** es, en nuestro sentido operativo inicial, una igualdad válida para todos los valores permitidos de las letras dentro del contexto.

Una **ecuación** es, en nuestro sentido operativo inicial, una igualdad en la que una o más letras se tratan como valores por determinar y se pregunta qué valores permitidos la hacen verdadera.
:::

El contraste básico es:

$$
\boxed{
\text{identidad}
\longleftrightarrow
\text{patrón general}
}
$$

frente a:

$$
\boxed{
\text{ecuación}
\longleftrightarrow
\text{condición sobre valores}.
}
$$

También hemos aprendido algo metodológicamente decisivo:

$$
\boxed{
\text{comprobar ejemplos}
\neq
\text{demostrar una afirmación general}.
}
$$

Los ejemplos pueden apoyar una conjetura o detectar un error. La justificación general exige una razón matemática.

Finalmente, hemos visto que un solo contraejemplo puede refutar una supuesta identidad.

***

## Hacia la sección siguiente

En esta sección hemos usado varias veces identidades como:

$$
3(x+2)=3x+6.
$$

Pero todavía no hemos estudiado de manera sistemática **qué significa transformar una expresión sin cambiar su valor**.

Consideremos:

$$
3(x+2)+2x.
$$

Podemos escribir:

$$
3x+6+2x
$$

y luego:

$$
5x+6.
$$

¿Por qué están permitidos esos pasos?

¿Qué ley justifica cada uno?

¿«Simplificar» significa simplemente mover símbolos hasta que la expresión se vea más corta?

La siguiente sección fijará una disciplina que usaremos durante todo el libro:

## §7. Transformar sin cambiar el valor

Hasta ahora hemos aprendido a leer expresiones, sustituir valores, interpretar el signo igual y distinguir identidades de ecuaciones.

Ahora llegamos a una actividad que suele asociarse inmediatamente con el álgebra:

> **transformar expresiones**.

Consideremos:

$$
3(x+2)+2x.
$$

Tal vez ya sepas convertirla en:

$$
5x+6.
$$

Pero la pregunta que nos interesa no es solo:

> ¿cómo se hace?

Queremos preguntar:

> **¿por qué cada paso está permitido?**

Podemos escribir:

$$
\begin{aligned}
3(x+2)+2x
&=3x+6+2x\\
&=3x+2x+6\\
&=(3+2)x+6\\
&=5x+6.
\end{aligned}
$$

Cada línea representa la misma cantidad que la anterior para los valores permitidos de $x$.

Eso no ocurre por magia ni porque ciertos símbolos «se muevan». Ocurre porque en cada paso aplicamos una ley algebraica.

La idea central de esta sección será:

::: {.ma-block .ma-intuicion}
**Idea clave**

Transformar una expresión consiste en reemplazarla por otra expresión que conserva el mismo valor, y cada reemplazo debe estar respaldado por una razón matemática.
:::

Por tanto, aprender álgebra no significa memorizar movimientos de símbolos. Significa aprender **qué transformaciones conservan el valor y por qué**.

***

### 7.1 Una transformación no es un desplazamiento de símbolos

Volvamos a:

$$
3(x+2)+2x.
$$

El primer paso fue:

$$
3(x+2)+2x
=
3x+6+2x.
$$

¿Qué ocurrió?

Aplicamos la distributividad:

$$
3(x+2)
=
3x+3\cdot2
=
3x+6.
$$

No «sacamos el paréntesis».

No «metimos el $3$».

No «repartimos porque sí».

Usamos una ley conocida:

$$
a(b+c)=ab+ac.
$$

Después escribimos:

$$
3x+6+2x
=
3x+2x+6.
$$

Aquí reordenamos y reagrupamos una suma. La justificación procede de las leyes conmutativa y asociativa de la suma.

Finalmente:

$$
3x+2x
=
(3+2)x
$$

es nuevamente una aplicación de la distributividad, ahora leída de derecha a izquierda:

$$
ax+bx=(a+b)x.
$$

Así obtenemos:

$$
(3+2)x+6
=
5x+6.
$$

La cadena completa puede escribirse haciendo visibles las razones:

$$
\begin{aligned}
3(x+2)+2x
&=3x+6+2x
&&\text{distributividad}\\
&=3x+2x+6
&&\text{conmutatividad y asociatividad}\\
&=(3+2)x+6
&&\text{distributividad}\\
&=5x+6
&&\text{aritmética}.
\end{aligned}
$$

Este formato será uno de nuestros hábitos fundamentales.

***

### 7.2 Tres leyes operativas

En este capítulo utilizaremos tres familias de leyes que el lector probablemente conoce por experiencia aritmética.

No las estamos presentando todavía como axiomas de una estructura abstracta. Eso ocurrirá mucho más adelante.

Por ahora las usamos como **leyes operativas** del sistema numérico en el que estamos trabajando.

#### Conmutatividad

En una suma:

$$
a+b=b+a.
$$

En un producto:

$$
ab=ba.
$$

La conmutatividad permite cambiar el orden de los términos de una suma o de los factores de un producto.

Por ejemplo:

$$
2x+7+3x
=
2x+3x+7.
$$

#### Asociatividad

En una suma:

$$
(a+b)+c=a+(b+c).
$$

En un producto:

$$
(ab)c=a(bc).
$$

La asociatividad permite cambiar la agrupación cuando repetimos la misma operación.

Por ejemplo:

$$
(2x+3x)+7
=
2x+(3x+7).
$$

No debe confundirse con cambiar arbitrariamente una operación por otra.

#### Distributividad

La multiplicación se distribuye sobre la suma:

$$
a(b+c)=ab+ac.
$$

También podemos leer la misma igualdad en la dirección contraria:

$$
ab+ac=a(b+c).
$$

En una dirección solemos hablar de **desarrollar** o **expandir**; en la otra, de **extraer un factor común** o **factorizar** en este sentido elemental.

Por ejemplo:

$$
4(x+3)=4x+12,
$$

y también:

$$
4x+12=4(x+3).
$$

Son expresiones distintas, pero representan el mismo valor para los valores permitidos en el contexto.

***

### 7.3 La dirección de una transformación depende del objetivo

Consideremos:

$$
5(x+2).
$$

Podemos transformarla en:

$$
5x+10.
$$

¿Es esta segunda expresión «mejor»?

No necesariamente.

Depende de qué queramos hacer.

Si deseamos ver una suma de términos, puede ser útil:

$$
5x+10.
$$

Si deseamos hacer visible el factor común $5$, puede ser más informativa:

$$
5(x+2).
$$

Ambas formas conservan el mismo valor:

$$
5(x+2)=5x+10.
$$

Por tanto:

::: {.ma-block .ma-intuicion}
**Idea clave**

Transformar una expresión no significa necesariamente hacerla más corta.  
Significa obtener una forma que conserve el valor y resulte útil para el propósito actual.
:::

Esto será cada vez más importante.

Una misma expresión puede tener varias formas correctas, y cada forma puede revelar una estructura distinta.

***

### 7.4 La distributividad funciona en ambas direcciones

Consideremos:

$$
6x+9x.
$$

Podemos ver dos términos:

$$
6x
\qquad\text{y}\qquad
9x.
$$

Ambos contienen el factor $x$.

Por distributividad:

$$
6x+9x
=
(6+9)x
=
15x.
$$

No estamos «sumando las letras».

Estamos usando:

$$
ax+bx=(a+b)x.
$$

El factor $x$ permanece común y sumamos los coeficientes.

Del mismo modo:

$$
4a+4b
=
4(a+b).
$$

Aquí no obtenemos:

$$
8ab
$$

ni ninguna combinación semejante. Lo que hacemos es reconocer un factor común.

La lectura estructural determina la transformación correcta.

***

### 7.5 Reordenar exige una razón

Consideremos:

$$
2x+5+3x.
$$

Queremos reunir los términos que contienen $x$.

Podemos escribir:

$$
2x+5+3x
=
2x+3x+5.
$$

A veces se dice informalmente:

> «muevo el $3x$ junto al $2x$».

Pero esa frase oculta la razón matemática.

Lo que realmente usamos es que podemos reordenar y reagrupar los sumandos mediante conmutatividad y asociatividad.

Después:

$$
2x+3x+5
=
(2+3)x+5
=
5x+5.
$$

El proceso completo puede escribirse:

$$
\begin{aligned}
2x+5+3x
&=2x+3x+5
&&\text{conmutatividad y asociatividad}\\
&=(2+3)x+5
&&\text{distributividad}\\
&=5x+5
&&\text{aritmética}.
\end{aligned}
$$

La expresión no cambia de valor en ningún paso.

***

### 7.6 Ejemplo desarrollado: justificar cada transformación

::: {.ma-block .ma-observacion #apm-t1-c01-x0006}
**Ejemplo — De \(3(x+2)+2x\) a \(5x+6\)**

:::

Queremos transformar:

$$
3(x+2)+2x.
$$

#### Paso 1 — Desarrollar el producto

Aplicamos distributividad:

$$
3(x+2)
=
3x+3\cdot2.
$$

Por tanto:

$$
3(x+2)+2x
=
3x+6+2x.
$$

#### Paso 2 — Reunir los términos con \(x\)

Reordenamos y reagrupamos la suma:

$$
3x+6+2x
=
3x+2x+6.
$$

La razón es la conmutatividad y la asociatividad de la suma.

#### Paso 3 — Extraer el factor común \(x\)

Aplicamos distributividad en sentido inverso:

$$
3x+2x
=
(3+2)x.
$$

Entonces:

$$
3x+2x+6
=
(3+2)x+6.
$$

#### Paso 4 — Realizar la aritmética

$$
(3+2)x+6
=
5x+6.
$$

#### Cadena completa

$$
\begin{aligned}
3(x+2)+2x
&=3x+6+2x
&&\text{distributividad}\\
&=3x+2x+6
&&\text{conmutatividad y asociatividad}\\
&=(3+2)x+6
&&\text{distributividad}\\
&=5x+6
&&\text{aritmética}.
\end{aligned}
$$

No hemos aplicado una receta de «quitar paréntesis y juntar letras».

Hemos construido una cadena de igualdades, y cada igualdad tiene una justificación.

***

### 7.7 Dos caminos correctos pueden llegar al mismo lugar

Consideremos:

$$
2(x+3)+4(x+3).
$$

#### Camino A — Desarrollar primero

Aplicamos distributividad a cada producto:

$$
2(x+3)+4(x+3)
=
2x+6+4x+12.
$$

Reordenamos:

$$
2x+6+4x+12
=
2x+4x+6+12.
$$

Reunimos términos:

$$
2x+4x+6+12
=
6x+18.
$$

#### Camino B — Reconocer primero el factor común

Ambos términos contienen el factor:

$$
x+3.
$$

Por distributividad en sentido inverso:

$$
2(x+3)+4(x+3)
=
(2+4)(x+3).
$$

Entonces:

$$
(2+4)(x+3)
=
6(x+3).
$$

Si deseamos desarrollar:

$$
6(x+3)
=
6x+18.
$$

Los dos caminos llegan a:

$$
6x+18.
$$

Ninguno es «el único método correcto».

Sin embargo, el segundo camino reconoce antes una estructura común y requiere menos pasos.

Esto introduce otro hábito importante:

$$
\boxed{
\text{una transformación puede ser correcta y, además, más o menos conveniente}.
}
$$

La corrección y la eficiencia son cuestiones distintas.

***

### 7.8 Cómo detectar un paso inválido

Consideremos la supuesta transformación:

$$
3(x+2)+2x
=
3x+2+2x.
$$

¿Qué ocurrió?

Parece que alguien escribió:

$$
3(x+2)=3x+2.
$$

Pero la distributividad exige multiplicar **cada término** de la suma por $3$:

$$
3(x+2)=3x+6.
$$

Podemos detectar el error también mediante una comprobación numérica.

Tomemos:

$$
x=0.
$$

La expresión original vale:

$$
3(0+2)+2\cdot0=6.
$$

La expresión supuestamente transformada vale:

$$
3\cdot0+2+2\cdot0=2.
$$

Como:

$$
6\ne2,
$$

las dos expresiones no conservan el mismo valor.

La comprobación numérica no sustituye la explicación estructural, pero puede ayudarnos a detectar que algo salió mal.

::: {.ma-block .ma-error}
**Atención**

Una transformación algebraica no es válida porque «parezca habitual». Debemos poder indicar la ley que la justifica.
:::

***

### 7.9 «Mover», «pasar» y «cancelar» pueden ocultar matemáticas

En muchos cursos se oyen expresiones como:

- «muevo este término»;
- «paso este número»;
- «cambia de signo al cruzar»;
- «cancelo estas letras».

A veces estas frases se utilizan como abreviaturas informales de razonamientos correctos.

El problema aparece cuando la abreviatura sustituye a la razón.

En una expresión como:

$$
2x+5+3x,
$$

decir «movemos $3x$» no explica por qué está permitido escribir:

$$
2x+3x+5.
$$

La razón es la conmutatividad y asociatividad de la suma.

Más adelante, cuando estudiemos ecuaciones, veremos que «pasar al otro lado» tampoco es una operación algebraica independiente. Habrá que justificar qué hacemos a ambos miembros de la igualdad.

Por ahora adoptaremos una regla editorial para todo el libro:

::: {.ma-block .ma-intuicion}
**Idea clave**

Podemos usar una abreviatura verbal solo después de que la operación matemática que resume haya quedado clara. Nunca reemplazaremos una justificación por la imagen de que los símbolos «se trasladan» solos.
:::

***

### 7.10 Transformar no es cambiar arbitrariamente

Una expresión puede adoptar muchas formas correctas, pero no cualquier forma.

Por ejemplo:

$$
2(x+5)
=
2x+10
$$

es correcto por distributividad.

Pero:

$$
2(x+5)
=
2x+5
$$

es falso.

Asimismo:

$$
3x+4x=7x
$$

es correcto porque:

$$
3x+4x=(3+4)x.
$$

En cambio:

$$
3x+4=7x
$$

no está justificado: los dos términos no comparten el factor $x$.

La pregunta decisiva ante cada paso es:

> **¿qué ley permite reemplazar la expresión anterior por la nueva?**

Si no podemos responder, debemos revisar el paso.

***

## Ejercicios

### Nombrar la ley {#apm-t1-c01-e0034}

Indica qué ley justifica cada igualdad.

#### a)

$$
a+b=b+a
$$

#### b)

$$
(a+b)+c=a+(b+c)
$$

#### c)

$$
3(x+4)=3x+12
$$

#### d)

$$
5x+2x=(5+2)x
$$

#### e)

$$
ab=ba
$$

#### Solución

#### a)

$$
a+b=b+a
$$

usa la **conmutatividad de la suma**.

#### b)

$$
(a+b)+c=a+(b+c)
$$

usa la **asociatividad de la suma**.

#### c)

$$
3(x+4)=3x+12
$$

usa la **distributividad**:

$$
3(x+4)=3x+3\cdot4=3x+12.
$$

#### d)

$$
5x+2x=(5+2)x
$$

usa la **distributividad en sentido inverso**.

#### e)

$$
ab=ba
$$

usa la **conmutatividad del producto**.

***

### Justificar cada paso {#apm-t1-c01-e0035}

Completa las razones de la transformación:

$$
\begin{aligned}
4(x+2)+3x
&=4x+8+3x\\
&=4x+3x+8\\
&=(4+3)x+8\\
&=7x+8.
\end{aligned}
$$

#### Solución

La primera igualdad:

$$
4(x+2)+3x
=
4x+8+3x
$$

usa distributividad.

La segunda:

$$
4x+8+3x
=
4x+3x+8
$$

usa conmutatividad y asociatividad de la suma para reordenar y reagrupar.

La tercera:

$$
4x+3x+8
=
(4+3)x+8
$$

usa distributividad en sentido inverso.

La cuarta:

$$
(4+3)x+8
=
7x+8
$$

usa aritmética.

***

### Transformar sin saltos {#apm-t1-c01-e0036}

Transforma:

$$
5(x+1)+2x
$$

hasta obtener una expresión de la forma:

$$
ax+b.
$$

Justifica cada paso.

#### Solución

Comenzamos con:

$$
5(x+1)+2x.
$$

Por distributividad:

$$
5(x+1)+2x
=
5x+5+2x.
$$

Reordenamos y reagrupamos:

$$
5x+5+2x
=
5x+2x+5.
$$

Por distributividad en sentido inverso:

$$
5x+2x+5
=
(5+2)x+5.
$$

Finalmente:

$$
(5+2)x+5
=
7x+5.
$$

La cadena completa es:

$$
\begin{aligned}
5(x+1)+2x
&=5x+5+2x
&&\text{distributividad}\\
&=5x+2x+5
&&\text{conmutatividad y asociatividad}\\
&=(5+2)x+5
&&\text{distributividad}\\
&=7x+5
&&\text{aritmética}.
\end{aligned}
$$

***

### Dos caminos {#apm-t1-c01-e0037}

Transforma:

$$
3(x+2)+5(x+2)
$$

de dos maneras:

1. desarrollando primero ambos productos;
2. reconociendo primero el factor común $x+2$.

Comprueba que ambos caminos conducen a la misma forma desarrollada.

#### Solución

#### Camino 1 — Desarrollar

$$
\begin{aligned}
3(x+2)+5(x+2)
&=3x+6+5x+10\\
&=3x+5x+6+10\\
&=8x+16.
\end{aligned}
$$

#### Camino 2 — Factor común

Por distributividad en sentido inverso:

$$
3(x+2)+5(x+2)
=
(3+5)(x+2).
$$

Entonces:

$$
(3+5)(x+2)
=
8(x+2).
$$

Desarrollamos:

$$
8(x+2)
=
8x+16.
$$

Ambos caminos llegan a:

$$
\boxed{8x+16}.
$$

El segundo camino reconoce antes la estructura común.

***

### Encontrar el primer paso inválido {#apm-t1-c01-e0038}

Un estudiante escribe:

$$
\begin{aligned}
2(x+4)+3x
&=2x+4+3x\\
&=5x+4.
\end{aligned}
$$

1. Identifica el primer paso incorrecto.
2. Explica qué ley se aplicó mal.
3. Corrige toda la transformación.

#### Solución

El primer paso incorrecto es:

$$
2(x+4)=2x+4.
$$

La distributividad se aplicó de manera incompleta.

Debe multiplicarse por $2$ cada término del paréntesis:

$$
2(x+4)
=
2x+8.
$$

Por tanto:

$$
\begin{aligned}
2(x+4)+3x
&=2x+8+3x\\
&=2x+3x+8\\
&=(2+3)x+8\\
&=5x+8.
\end{aligned}
$$

La forma correcta es:

$$
\boxed{5x+8}.
$$

***

### ¿Puede reunirse? {#apm-t1-c01-e0039}

Decide si la transformación propuesta está justificada. Explica por qué.

#### a)

$$
3x+4x=7x
$$

#### b)

$$
3x+4=7x
$$

#### c)

$$
2a+5a=(2+5)a
$$

#### d)

$$
2a+5b=7ab
$$

#### Solución

#### a)

Sí.

$$
3x+4x
=
(3+4)x
=
7x
$$

por distributividad.

#### b)

No.

En:

$$
3x+4,
$$

los términos $3x$ y $4$ no comparten el factor $x$.

No existe una aplicación de distributividad que permita escribir:

$$
3x+4=7x.
$$

#### c)

Sí.

$$
2a+5a
=
(2+5)a
=
7a.
$$

#### d)

No.

Los términos:

$$
2a
\qquad\text{y}\qquad
5b
$$

no tienen la estructura necesaria para obtener:

$$
7ab.
$$

La transformación propuesta no está justificada.

***

### Elegir una forma útil {#apm-t1-c01-e0040}

Considera:

$$
6x+18.
$$

#### a)

Escribe una forma factorizada usando distributividad en sentido inverso.

#### b)

¿Cuál de las dos formas hace más visible el factor común $6$?

#### c)

¿Cuál hace más visible que la expresión es una suma de dos términos?

#### Solución

#### a)

Extraemos el factor común $6$:

$$
6x+18
=
6x+6\cdot3
=
6(x+3).
$$

#### b)

La forma:

$$
6(x+3)
$$

hace visible el factor común $6$.

#### c)

La forma:

$$
6x+18
$$

hace visible inmediatamente que tenemos una suma de dos términos.

Ninguna forma es absolutamente «mejor». Cada una revela una estructura distinta.

***

## Resumen de la sección

Transformar una expresión no consiste en desplazar símbolos.

Consiste en construir una cadena de igualdades donde cada paso conserva el valor y está respaldado por una ley conocida.

Las tres leyes operativas principales de esta sección han sido:

$$
\boxed{
a+b=b+a
}
$$

y:

$$
\boxed{
ab=ba
}
$$

para la conmutatividad;

$$
\boxed{
(a+b)+c=a+(b+c)
}
$$

y:

$$
\boxed{
(ab)c=a(bc)
}
$$

para la asociatividad; y:

$$
\boxed{
a(b+c)=ab+ac
}
$$

para la distributividad.

Hemos aprendido además que:

- la distributividad puede leerse en ambas direcciones;
- reordenar términos exige conmutatividad y asociatividad;
- reunir términos semejantes es una aplicación de distributividad;
- distintas transformaciones correctas pueden conducir al mismo resultado;
- una forma no es siempre mejor por ser más corta;
- una comprobación numérica puede detectar un error, pero la justificación es la ley algebraica;
- expresiones como «mover», «pasar» o «cancelar» no deben sustituir a la razón matemática.

El principio que debe quedar instalado es:

$$
\boxed{
\text{cada paso algebraico debe poder responder a la pregunta: «¿por qué?»}
}
$$

***

## Hacia la sección siguiente

Las leyes algebraicas nos permiten transformar expresiones correctamente.

Pero incluso una transformación matemáticamente válida puede resultar difícil de leer si la notación es ambigua.

Consideremos:

$$
-x^2
$$

y:

$$
(-x)^2.
$$

¿Representan lo mismo?

O comparemos:

$$
\frac{a+b}{c}
$$

con:

$$
a+\frac{b}{c}.
$$

En ambos casos, pequeños cambios en la escritura alteran la estructura.

La próxima sección estudiará precisamente ese problema:

## §8. Sintaxis: escribir para que no haya dudas

En las secciones anteriores hemos insistido en una idea:

$$
\boxed{\text{una expresión tiene estructura}.}
$$

Esa estructura no existe solamente en nuestra mente. La notación debe permitirnos verla.

Comparemos:

$$
-x^2
$$

y

$$
(-x)^2.
$$

Las dos escrituras contienen los mismos símbolos básicos:

$$
-,\qquad x,\qquad 2.
$$

Sin embargo, no representan lo mismo.

En la primera, la potencia actúa sobre $x$:

$$
-x^2=-(x^2).
$$

En la segunda, la potencia actúa sobre toda la expresión $-x$:

$$
(-x)^2.
$$

Si, por ejemplo, $x=3$:

$$
-x^2=-9,
$$

mientras que:

$$
(-x)^2=9.
$$

La diferencia está en el **alcance** de las operaciones.

La pregunta central de esta sección será:

> ¿cómo debemos escribir una expresión para que el lector pueda reconocer sin dudas qué operación actúa sobre qué parte?

La respuesta combinará convenciones de precedencia, paréntesis, barras de fracción, exponentes y hábitos de escritura clara.

::: {.ma-block .ma-intuicion}
**Idea clave**

Una buena notación no obliga al lector a adivinar la estructura.
:::

***

### 8.1 La escritura también tiene jerarquía

Consideremos:

$$
2+3x^2.
$$

No la leemos como si todos los símbolos tuvieran la misma jerarquía.

Las convenciones usuales nos indican que primero reconocemos la potencia:

$$
x^2,
$$

después el producto:

$$
3x^2,
$$

y finalmente la suma:

$$
2+3x^2.
$$

Podemos hacer visible la estructura escribiendo:

$$
2+\bigl(3(x^2)\bigr).
$$

Normalmente no necesitamos tantos paréntesis, porque las convenciones de precedencia ya hacen inequívoca la lectura.

Pero conviene comprender qué están abreviando esas convenciones.

En términos muy generales, en las expresiones elementales de este capítulo:

1. los agrupamientos explícitos se respetan primero;
2. las potencias tienen un alcance más estrecho que los productos y cocientes;
3. los productos y cocientes se reconocen antes que las sumas y restas.

No queremos convertir esta lista en una mnemotecnia ciega.

El objetivo es entender que las convenciones tipográficas hacen visible una **estructura jerárquica**.

***

### 8.2 Los paréntesis cambian el alcance

Comparemos:

$$
2+3^2
$$

y

$$
(2+3)^2.
$$

En la primera:

$$
2+3^2
=
2+9
=
11.
$$

En la segunda:

$$
(2+3)^2
=
5^2
=
25.
$$

Los paréntesis indican que la potencia debe actuar sobre la suma completa.

Lo mismo ocurre con:

$$
-2^2
$$

y:

$$
(-2)^2.
$$

Tenemos:

$$
-2^2
=
-(2^2)
=
-4,
$$

mientras que:

$$
(-2)^2
=
4.
$$

Los paréntesis no son decoración. Determinan qué expresión queda agrupada y, por tanto, cuál es el alcance de una operación exterior.

***

### 8.3 El signo menos merece atención especial

La escritura:

$$
-x^2
$$

se interpreta como:

$$
-(x^2).
$$

El exponente $2$ afecta a $x$, no al signo menos exterior.

En cambio:

$$
(-x)^2
$$

eleva al cuadrado toda la expresión:

$$
-x.
$$

Esto explica por qué, al sustituir un número negativo, §4 insistió en escribir:

$$
(-3)^2
$$

y no:

$$
-3^2.
$$

El problema no era únicamente «poner paréntesis porque sí». Los paréntesis protegían el alcance correcto de la potencia.

Podemos resumir:

$$
\boxed{
-x^2=-(x^2),
\qquad
(-x)^2=(-x)(-x).
}
$$

Cuando $x\ne0$, estas expresiones tienen signos opuestos.

***

### 8.4 La barra de fracción agrupa

Consideremos:

$$
\frac{a+b}{c}.
$$

La barra de fracción no solo indica división. También agrupa.

Todo lo que aparece en el numerador:

$$
a+b
$$

forma una unidad.

Por tanto:

$$
\frac{a+b}{c}
$$

tiene una estructura distinta de:

$$
a+\frac bc.
$$

Probemos, por ejemplo:

$$
a=2,\qquad b=4,\qquad c=3.
$$

Entonces:

$$
\frac{a+b}{c}
=
\frac{2+4}{3}
=
2,
$$

mientras que:

$$
a+\frac bc
=
2+\frac43
=
\frac{10}{3}.
$$

Así:

$$
\frac{a+b}{c}
\ne
a+\frac bc
$$

para estos valores.

La fracción vertical hace visible la agrupación.

***

### 8.5 Cuando escribimos en una sola línea

En texto plano, una fracción vertical puede tener que escribirse mediante `/`.

Entonces debemos ser más cuidadosos.

La expresión:

$$
\frac{a+b}{c}
$$

debe escribirse linealmente como:

```text
(a+b)/c
```

y no como:

```text
a+b/c
```

porque esta segunda escritura corresponde a:

$$
a+\frac bc.
$$

De manera semejante:

$$
\frac{a}{b+c}
$$

debe escribirse:

```text
a/(b+c)
```

si queremos que todo $b+c$ esté en el denominador.

La regla práctica es sencilla:

::: {.ma-block .ma-intuicion}
**Idea clave**

Al pasar una expresión bidimensional a una línea de texto, añade los paréntesis necesarios para conservar exactamente la estructura original.
:::

***

### 8.6 Multiplicación implícita: brevedad sin confusión

En álgebra escribimos:

$$
3x
$$

en lugar de:

$$
3\cdot x.
$$

También escribimos:

$$
2(a+b)
$$

en lugar de:

$$
2\cdot(a+b).
$$

Esta multiplicación implícita suele ser clara.

Pero no toda abreviación es igualmente buena.

Por ejemplo, una escritura lineal como:

```text
1/2x
```

puede resultar poco clara para un lector: ¿se pretende escribir

$$
\frac{1}{2x}
$$

o:

$$
\frac12 x?
$$

Aunque un contexto o una convención local pudiera decidir la lectura, podemos evitar el problema.

Si queremos:

$$
\frac{1}{2x},
$$

escribimos:

```text
1/(2x)
```

Si queremos:

$$
\frac12 x,
$$

podemos escribir:

```text
(1/2)x
```

o, mejor aún cuando el formato lo permite:

$$
\frac12 x.
$$

::: {.ma-block .ma-observacion}
**Observación**

La notación matemática no debe convertirse en una prueba de adivinación. Cuando una escritura breve pueda generar una lectura razonablemente distinta, preferiremos la forma más explícita.
:::

***

### 8.7 Los exponentes también tienen alcance

Comparemos:

$$
a+b^2
$$

con:

$$
(a+b)^2.
$$

En la primera, el exponente afecta solo a $b$.

En la segunda, afecta a toda la suma.

También debemos distinguir:

$$
x^{2+1}
$$

de:

$$
x^2+1.
$$

La primera es una potencia cuyo exponente completo es:

$$
2+1.
$$

La segunda es una suma:

$$
x^2+1.
$$

Cuando el exponente contiene más de un símbolo, las llaves de LaTeX o la composición tipográfica indican qué parte pertenece al exponente:

```text
x^{2+1}
```

produce:

$$
x^{2+1}.
$$

La regla estructural sigue siendo la misma:

$$
\boxed{\text{debemos saber qué expresión está dentro del alcance del exponente}.}
$$

***

### 8.8 Paréntesis anidados

Consideremos:

$$
3\bigl(2+(x-1)^2\bigr).
$$

Podemos leerla desde fuera hacia dentro.

La operación exterior es un producto:

$$
3\cdot\bigl(2+(x-1)^2\bigr).
$$

Dentro del segundo factor aparece una suma:

$$
2+(x-1)^2.
$$

Dentro de esa suma aparece una potencia:

$$
(x-1)^2.
$$

Y su base es:

$$
x-1.
$$

La notación contiene varios niveles de agrupamiento.

Cuando la expresión se hace más compleja, es frecuente alternar visualmente paréntesis y otros delimitadores:

$$
3\left[2+(x-1)^2\right].
$$

Matemáticamente, los corchetes pueden cumplir aquí el mismo papel de agrupamiento que los paréntesis. Se utilizan para mejorar la lectura.

La claridad tipográfica debe acompañar a la estructura matemática.

***

### 8.9 No todos los paréntesis son obligatorios, pero algunos son útiles

La expresión:

$$
2+(3x)
$$

puede escribirse simplemente:

$$
2+3x,
$$

porque la precedencia usual ya indica que $3x$ forma un producto.

En cambio:

$$
(2+3)x
$$

no puede escribirse como:

$$
2+3x
$$

sin cambiar la estructura.

Existe, por tanto, una diferencia entre:

- paréntesis **necesarios** para determinar la estructura;
- paréntesis **opcionales** que pueden ayudar a hacerla más visible.

Por ejemplo:

$$
a+(b+c)
$$

y:

$$
a+b+c
$$

pueden representar el mismo valor en nuestro contexto por asociatividad de la suma.

Sin embargo, si estamos estudiando específicamente la subexpresión $b+c$, conservar los paréntesis puede ser pedagógicamente útil.

La buena escritura matemática no busca siempre el mínimo número posible de signos. Busca una relación equilibrada entre economía y claridad.

***

### 8.10 Ejemplo desarrollado: leer una expresión compleja

::: {.ma-block .ma-observacion #apm-t1-c01-x0008}
**Ejemplo — Alcance y estructura en una expresión anidada**

:::

Consideremos:

$$
-\frac{2x-(a+b)^2}{3c}.
$$

No queremos simplificarla. Queremos leerla con precisión.

#### Paso 1 — El signo exterior

Toda la fracción aparece precedida por un signo menos:

$$
-\left(\frac{2x-(a+b)^2}{3c}\right).
$$

Por tanto, el signo menos actúa sobre el cociente completo.

#### Paso 2 — La fracción

El numerador es:

$$
2x-(a+b)^2.
$$

El denominador es:

$$
3c.
$$

#### Paso 3 — El numerador

Dentro del numerador aparecen dos grandes partes:

$$
2x
$$

y:

$$
(a+b)^2.
$$

La segunda está restada.

#### Paso 4 — La potencia

En:

$$
(a+b)^2,
$$

la base completa es:

$$
a+b.
$$

El exponente es:

$$
2.
$$

#### Paso 5 — Los productos

En:

$$
2x,
$$

hay un producto entre $2$ y $x$.

En:

$$
3c,
$$

hay un producto entre $3$ y $c$.

#### Lectura completa

Podemos describir la expresión como:

> el opuesto del cociente cuyo numerador es la diferencia entre $2x$ y el cuadrado de $a+b$, y cuyo denominador es $3c$.

La estructura puede esquematizarse así:

```text
opuesto
└── cociente
    ├── numerador: 2x - (a+b)^2
    │   ├── producto: 2x
    │   └── potencia: (a+b)^2
    │       └── base: a+b
    └── denominador: 3c
        └── producto: 3·c
```

Este ejemplo resume el hábito que venimos construyendo desde §1:

$$
\boxed{
\text{leer de fuera hacia dentro}
\longrightarrow
\text{reconocer el alcance}
\longrightarrow
\text{interpretar sin adivinar}.
}
$$

***

### 8.11 Una regla editorial: escribir para otro lector

En un cuaderno personal podemos comprender una abreviatura porque recordamos qué queríamos decir.

En un libro, una demostración o una solución escrita para otra persona, esa memoria privada no existe.

La notación debe sostenerse por sí sola.

Por eso preferiremos:

```text
(a+b)/c
```

a una escritura lineal que pueda confundirse con:

```text
a+b/c
```

y preferiremos:

```text
1/(2x)
```

cuando queramos evitar que `1/2x` admita una segunda lectura razonable.

Esta regla no es solamente estética.

La claridad de la notación reduce errores matemáticos.

$$
\boxed{
\text{escribir con claridad forma parte de razonar con claridad}.
}
$$

***

## Ejercicios

### Mismo símbolo, distinto alcance {#apm-t1-c01-e0041}

Explica la diferencia estructural entre cada par. No te limites a calcular.

#### a)

$$
-3^2
\qquad\text{y}\qquad
(-3)^2
$$

#### b)

$$
2+x^2
\qquad\text{y}\qquad
(2+x)^2
$$

#### c)

$$
a+b^3
\qquad\text{y}\qquad
(a+b)^3
$$

#### Solución

#### a)

En:

$$
-3^2,
$$

la potencia actúa sobre $3$:

$$
-(3^2)=-9.
$$

En:

$$
(-3)^2,
$$

la base completa es $-3$:

$$
(-3)^2=9.
$$

#### b)

En:

$$
2+x^2,
$$

solo $x$ está elevado al cuadrado.

En:

$$
(2+x)^2,
$$

toda la suma $2+x$ constituye la base de la potencia.

#### c)

En:

$$
a+b^3,
$$

el exponente $3$ afecta solamente a $b$.

En:

$$
(a+b)^3,
$$

la base completa es $a+b$.

La diferencia en los tres pares es una diferencia de **alcance**.

***

### Barras de fracción {#apm-t1-c01-e0042}

Describe la estructura de:

$$
\frac{a+b}{c+d}.
$$

Después escribe la misma expresión en notación lineal usando `/`.

#### Solución

La expresión completa es un cociente.

El numerador es:

$$
a+b.
$$

El denominador es:

$$
c+d.
$$

Para conservar esa estructura en una sola línea debemos escribir:

```text
(a+b)/(c+d)
```

Los paréntesis son necesarios para indicar que las dos sumas completas son el numerador y el denominador.

***

### Dos escrituras lineales {#apm-t1-c01-e0043}

Interpreta las siguientes escrituras lineales y escríbelas con fracciones verticales.

#### a)

```text
(a+b)/c
```

#### b)

```text
a+b/c
```

#### c)

```text
a/(b+c)
```

Explica por qué las tres estructuras son diferentes.

#### Solución

#### a)

```text
(a+b)/c
```

corresponde a:

$$
\frac{a+b}{c}.
$$

La suma $a+b$ completa forma el numerador.

#### b)

```text
a+b/c
```

corresponde a:

$$
a+\frac bc.
$$

La operación exterior es una suma.

#### c)

```text
a/(b+c)
```

corresponde a:

$$
\frac{a}{b+c}.
$$

La suma $b+c$ completa forma el denominador.

Las tres estructuras difieren porque las operaciones no tienen el mismo alcance.

***

### Elige la escritura inequívoca {#apm-t1-c01-e0044}

Escribe en una sola línea, usando `/`, cada expresión.

#### a)

$$
\frac{1}{2x}
$$

#### b)

$$
\frac12 x
$$

#### c)

$$
\frac{x+1}{y-2}
$$

#### Solución

#### a)

Una escritura inequívoca es:

```text
1/(2x)
```

#### b)

Podemos escribir:

```text
(1/2)x
```

Así queda claro que primero tenemos el factor $1/2$ y luego multiplicamos por $x$.

#### c)

Debemos escribir:

```text
(x+1)/(y-2)
```

Los paréntesis conservan las dos agrupaciones de la fracción original.

***

### Lectura jerárquica {#apm-t1-c01-e0045}

Considera:

$$
-\frac{3x+(y-1)^2}{2z}.
$$

Describe la expresión de fuera hacia dentro e identifica:

1. el alcance del signo menos exterior;
2. numerador y denominador;
3. la potencia y su base;
4. los productos que aparecen.

#### Solución

#### 1. Signo menos

El signo menos exterior afecta a toda la fracción:

$$
-\left(\frac{3x+(y-1)^2}{2z}\right).
$$

#### 2. Fracción

El numerador es:

$$
3x+(y-1)^2.
$$

El denominador es:

$$
2z.
$$

#### 3. Potencia

La potencia es:

$$
(y-1)^2.
$$

Su base completa es:

$$
y-1,
$$

y su exponente es $2$.

#### 4. Productos

En el numerador aparece:

$$
3x,
$$

un producto entre $3$ y $x$.

En el denominador aparece:

$$
2z,
$$

un producto entre $2$ y $z$.

La lectura completa comienza por el signo exterior y avanza hacia las subexpresiones internas.

***

## Resumen de la sección

La sintaxis matemática organiza el alcance de las operaciones.

Hemos aprendido a distinguir expresiones como:

$$
-x^2
\qquad\text{y}\qquad
(-x)^2,
$$

así como:

$$
\frac{a+b}{c}
\qquad\text{y}\qquad
a+\frac bc.
$$

Los recursos principales para hacer visible la estructura son:

- convenciones de precedencia;
- paréntesis y otros delimitadores;
- barras de fracción;
- posición de los exponentes;
- multiplicación implícita usada con cuidado.

Al escribir en una sola línea debemos añadir los paréntesis necesarios para preservar la estructura:

$$
\frac{a+b}{c}
\quad\longleftrightarrow\quad
\texttt{(a+b)/c}.
$$

La regla editorial que conservaremos es:

$$
\boxed{
\text{si una escritura puede inducir una lectura razonablemente distinta, la hacemos más explícita}.
}
$$

Y el hábito matemático es:

$$
\boxed{
\text{reconocer el alcance antes de operar}.
}
$$

***

## Hacia la sección siguiente

Ya sabemos leer la estructura, sustituir valores, interpretar igualdades, distinguir identidades y ecuaciones, justificar transformaciones y escribir de forma inequívoca.

Eso nos permite abordar un nuevo tipo de problema.

Consideremos:

$$
(a+b)^2=a^2+b^2.
$$

O:

$$
\frac{a+b}{a}=b.
$$

O:

$$
2+3x=5x.
$$

Las tres escrituras pueden parecer plausibles si se aplican reglas de manera superficial.

Pero ¿qué estructura fue ignorada en cada caso?

¿Cómo podemos detectar rápidamente que una supuesta regla es falsa?

¿Podemos construir un valor concreto que la contradiga?

La siguiente sección estará dedicada a aprender a diagnosticar precisamente esos errores:

## §9. Errores que parecen álgebra

Aprender álgebra no consiste únicamente en conocer reglas correctas.

También debemos aprender a reconocer transformaciones que **parecen** razonables pero no conservan el valor.

Consideremos:

$$
(a+b)^2=a^2+b^2.
$$

La escritura resulta tentadora.

Alguien podría pensar:

> «el cuadrado afecta a todo lo que está dentro del paréntesis, así que elevo al cuadrado cada término».

Pero esa explicación confunde la estructura de una potencia con la estructura de una suma.

La expresión:

$$
(a+b)^2
$$

significa:

$$
(a+b)(a+b),
$$

no:

$$
a^2+b^2.
$$

Si tomamos:

$$
a=1,
\qquad
b=1,
$$

obtenemos:

$$
(a+b)^2=(1+1)^2=4,
$$

mientras que:

$$
a^2+b^2=1^2+1^2=2.
$$

Por tanto:

$$
4\ne2.
$$

La supuesta regla es falsa.

Este ejemplo muestra una estrategia que usaremos durante toda la sección:

1. identificar la regla aparente;
2. localizar la estructura que se ha ignorado;
3. buscar un caso numérico sencillo;
4. escribir la regla correcta, cuando exista.

::: {.ma-block .ma-intuicion}
**Idea clave**

Un paso algebraico no se vuelve correcto porque se parezca a una regla conocida. Debe respetar exactamente la estructura a la que esa regla se aplica.
:::

***

### 9.1 Primer error: distribuir una potencia sobre una suma

La falsa regla es:

$$
(a+b)^2=a^2+b^2.
$$

#### Qué parece haberse hecho

Se ha tratado la potencia como si pudiera distribuirse sobre la suma.

#### Qué estructura se ignoró

Un cuadrado significa multiplicar una expresión por sí misma:

$$
(a+b)^2=(a+b)(a+b).
$$

Ahora sí podemos usar distributividad:

$$
\begin{aligned}
(a+b)(a+b)
&=a(a+b)+b(a+b)\\
&=a^2+ab+ab+b^2\\
&=a^2+2ab+b^2.
\end{aligned}
$$

Por tanto:

$$
\boxed{
(a+b)^2=a^2+2ab+b^2.
}
$$

El término:

$$
2ab
$$

no aparece por un detalle accidental. Surge de los dos productos cruzados:

$$
ab
\qquad\text{y}\qquad
ba.
$$

#### Contraejemplo

Con:

$$
a=b=1,
$$

la regla falsa daría:

$$
4=2.
$$

Un solo caso donde falla basta para saber que no puede ser una identidad.

***

### 9.2 Segundo error: cancelar dentro de una suma

Consideremos:

$$
\frac{a+b}{a}=b.
$$

Podría imaginarse un razonamiento como:

> «hay una $a$ arriba y una $a$ abajo; las cancelo».

Pero en el numerador:

$$
a+b
$$

la letra $a$ no es un factor de toda la suma.

Es solamente uno de sus términos.

La fracción puede separarse, siempre que $a\ne0$:

$$
\frac{a+b}{a}
=
\frac aa+\frac ba
=
1+\frac ba.
$$

No obtenemos $b$.

#### Contraejemplo

Tomemos:

$$
a=2,
\qquad
b=4.
$$

Entonces:

$$
\frac{a+b}{a}
=
\frac{2+4}{2}
=
3,
$$

mientras que:

$$
b=4.
$$

Por tanto:

$$
3\ne4.
$$

La supuesta cancelación es falsa.

La lección estructural es:

$$
\boxed{
\text{se cancelan factores comunes, no términos aislados dentro de una suma}.
}
$$

***

### 9.3 Qué significa cancelar correctamente

Consideremos ahora:

$$
\frac{a(b+1)}{a}.
$$

Si:

$$
a\ne0,
$$

el numerador completo tiene al factor $a$:

$$
a(b+1).
$$

Podemos escribir:

$$
\frac{a(b+1)}{a}
=
\frac{a}{a}(b+1)
=
b+1.
$$

Aquí sí existe un factor común entre numerador y denominador.

Comparemos:

$$
\frac{a(b+1)}{a}
$$

con:

$$
\frac{a+b}{a}.
$$

En la primera, el numerador es un producto:

$$
a\cdot(b+1).
$$

En la segunda, el numerador es una suma:

$$
a+b.
$$

La diferencia no es visualmente enorme, pero estructuralmente es decisiva.

***

### 9.4 Tercer error: sumar términos que no tienen la misma estructura

Consideremos:

$$
2+3x=5x.
$$

Alguien podría haber sumado:

$$
2+3=5
$$

y conservado la letra $x$.

Pero el término:

$$
2
$$

no contiene el factor $x$.

En cambio:

$$
2x+3x
$$

sí puede transformarse:

$$
2x+3x
=
(2+3)x
=
5x.
$$

La distributividad explica por qué.

No existe una transformación análoga para:

$$
2+3x.
$$

#### Contraejemplo

Tomemos:

$$
x=0.
$$

El lado izquierdo vale:

$$
2+3\cdot0=2.
$$

El lado derecho vale:

$$
5\cdot0=0.
$$

Por tanto:

$$
2\ne0.
$$

La igualdad propuesta es falsa.

::: {.ma-block .ma-intuicion}
**Idea clave**

«Términos semejantes» no significa «términos que están uno al lado del otro». La posibilidad de reunirlos debe venir de una estructura común, como un factor compartido.
:::

***

### 9.5 Cuarto error: cancelar expresiones que aparecen sumando

Consideremos:

$$
\frac{x+3}{x+5}.
$$

Un estudiante podría intentar «cancelar las $x$» y escribir:

$$
\frac{x+3}{x+5}
=
\frac35.
$$

Pero las $x$ no son factores de numerador y denominador.

Son términos dentro de dos sumas distintas.

#### Contraejemplo

Tomemos:

$$
x=1.
$$

Entonces:

$$
\frac{x+3}{x+5}
=
\frac46
=
\frac23,
$$

mientras que:

$$
\frac35
$$

es otro número.

Por tanto:

$$
\frac23\ne\frac35.
$$

La cancelación es inválida.

***

### 9.6 Ejemplo desarrollado: qué puede cancelarse

::: {.ma-block .ma-observacion #apm-t1-c01-x0007}
**Ejemplo — Cancelar factores, no términos**

:::

Comparemos dos expresiones.

#### Caso A

$$
\frac{x(x+3)}{x}.
$$

Suponiendo:

$$
x\ne0,
$$

el numerador es un producto:

$$
x\cdot(x+3).
$$

Por tanto:

$$
\frac{x(x+3)}{x}
=
\frac{x}{x}(x+3)
=
x+3.
$$

La cancelación es válida porque $x$ es factor de todo el numerador y también del denominador.

#### Caso B

$$
\frac{x+3}{x}.
$$

Aquí el numerador no es:

$$
x\cdot3.
$$

Es una suma:

$$
x+3.
$$

Por tanto no podemos cancelar la $x$ como si fuera un factor común.

Si $x\ne0$, podemos escribir:

$$
\frac{x+3}{x}
=
\frac xx+\frac3x
=
1+\frac3x.
$$

#### Comparación

La diferencia estructural es:

$$
\boxed{x(x+3)}
$$

frente a:

$$
\boxed{x+3}.
$$

En el primer caso, $x$ es factor del numerador completo.

En el segundo, $x$ es solamente un término de la suma.

Por eso, la regla práctica es:

$$
\boxed{
\text{una cancelación legítima exige un factor común no nulo}
}
$$

en el numerador y el denominador.

***

### 9.7 Un contraejemplo no explica todo, pero decide mucho

Supongamos que alguien propone:

$$
(a-b)^2=a^2-b^2.
$$

Podemos elegir:

$$
a=2,
\qquad
b=1.
$$

Entonces:

$$
(a-b)^2=1,
$$

mientras que:

$$
a^2-b^2=3.
$$

Así:

$$
1\ne3.
$$

Ya sabemos que la supuesta identidad es falsa.

Pero el contraejemplo no nos dice por sí solo **por qué** alguien cometió el error.

Para comprenderlo debemos volver a la estructura:

$$
(a-b)^2
=
(a-b)(a-b),
$$

y distribuir:

$$
(a-b)^2
=
a^2-2ab+b^2.
$$

Por tanto, debemos distinguir dos funciones del contraejemplo:

- **refutar** una afirmación general falsa;
- **diagnosticar**, junto con el análisis estructural, el origen del error.

Esta sección usa ambas funciones de manera informal.

***

### 9.8 Una regla verdadera puede usarse en el lugar equivocado

Muchos errores no consisten en inventar una regla completamente nueva.

Consisten en tomar una regla verdadera y aplicarla donde no corresponde.

Por ejemplo, la distributividad dice:

$$
a(b+c)=ab+ac.
$$

Pero de ahí no se sigue:

$$
(a+b)^2=a^2+b^2.
$$

La cancelación de un factor común puede ser válida:

$$
\frac{ab}{a}=b
\qquad
(a\ne0),
$$

pero de ahí no se sigue:

$$
\frac{a+b}{a}=b.
$$

Y:

$$
2x+3x=5x
$$

es correcto, pero no autoriza:

$$
2+3x=5x.
$$

La forma superficial de dos expresiones puede parecer parecida.

La estructura es la que decide qué ley está disponible.

$$
\boxed{
\text{regla correcta}
+
\text{estructura incorrecta}
=
\text{aplicación incorrecta}.
}
$$

***

### 9.9 Un protocolo para revisar una transformación sospechosa

Cuando una transformación nos produzca dudas, podemos seguir este procedimiento.

#### Paso 1 — Leer la estructura

Preguntar:

- ¿hay una suma?
- ¿hay un producto?
- ¿qué es factor de qué?
- ¿qué operación tiene alcance sobre qué parte?

#### Paso 2 — Nombrar la ley

Preguntar:

> ¿qué propiedad concreta justifica el paso?

Si la respuesta es solamente:

> «porque se cancela»,

o:

> «porque se pasa»,

todavía falta una explicación.

#### Paso 3 — Probar un valor sencillo

Si la supuesta regla pretende valer en general, podemos probar números fáciles.

Un valor que produzca resultados diferentes demuestra que la regla es falsa.

#### Paso 4 — Reconstruir correctamente

Una vez detectado el error, no basta con tacharlo.

Conviene escribir la transformación correcta y explicar qué estructura la permite.

Este protocolo convierte el error en una oportunidad de lectura algebraica.

***

## Ejercicios

### Cuadrado de una suma {#apm-t1-c01-e0046}

Un estudiante escribe:

$$
(x+2)^2=x^2+4.
$$

1. Encuentra un valor de $x$ que muestre que la igualdad es falsa.
2. Expande correctamente $(x+2)^2$.

#### Solución

Podemos tomar:

$$
x=1.
$$

El lado izquierdo vale:

$$
(1+2)^2=9.
$$

El lado derecho de la regla falsa vale:

$$
1^2+4=5.
$$

Como:

$$
9\ne5,
$$

la igualdad no es una identidad.

Ahora:

$$
(x+2)^2=(x+2)(x+2).
$$

Por distributividad:

$$
\begin{aligned}
(x+2)(x+2)
&=x^2+2x+2x+4\\
&=x^2+4x+4.
\end{aligned}
$$

Por tanto:

$$
\boxed{(x+2)^2=x^2+4x+4}.
$$

***

### ¿Cancelación válida? {#apm-t1-c01-e0047}

Decide si cada paso es válido. Justifica.

#### a)

$$
\frac{3x}{3}=x
$$

#### b)

$$
\frac{x+3}{3}=x
$$

#### c)

$$
\frac{3(x+2)}{3}=x+2
$$

#### d)

$$
\frac{x+3}{x}=3
$$

#### Solución

#### a)

Sí.

El numerador es el producto:

$$
3\cdot x.
$$

El factor $3$ puede cancelarse con el denominador:

$$
\frac{3x}{3}=x.
$$

#### b)

No.

En:

$$
x+3,
$$

el $3$ es un término, no un factor de todo el numerador.

#### c)

Sí.

El numerador es:

$$
3(x+2),
$$

de modo que $3$ es factor de toda la expresión:

$$
\frac{3(x+2)}3=x+2.
$$

#### d)

No.

En:

$$
x+3,
$$

la letra $x$ es un término, no un factor del numerador completo.

Para $x\ne0$:

$$
\frac{x+3}{x}
=
1+\frac3x.
$$

***

### Mismo aspecto, distinta estructura {#apm-t1-c01-e0048}

Decide si cada transformación es correcta. En los casos correctos, identifica el factor común. En los incorrectos, explica qué parte de la estructura cambia.

#### a)

$$
3(x+1)+2(x+1)=5(x+1)
$$

#### b)

$$
3(x+1)+2x=5(x+1)
$$

#### c)

$$
4(a-b)-(a-b)=3(a-b)
$$

#### d)

$$
4(a-b)-(a+b)=3(a-b)
$$

#### Solución

#### a)

Es correcta.

Los dos términos comparten el factor:

$$
x+1.
$$

Por distributividad en sentido inverso:

$$
3(x+1)+2(x+1)
=
(3+2)(x+1)
=
5(x+1).
$$

#### b)

Es incorrecta.

El segundo término es:

$$
2x,
$$

no:

$$
2(x+1).
$$

Por tanto, los dos términos no comparten el factor completo $x+1$.

Por ejemplo, con $x=0$:

$$
3(0+1)+2\cdot0=3,
$$

mientras que:

$$
5(0+1)=5.
$$

Así:

$$
3\ne5.
$$

#### c)

Es correcta.

La expresión $a-b$ es factor común:

$$
4(a-b)-(a-b)
=
4(a-b)-1(a-b).
$$

Por distributividad en sentido inverso:

$$
4(a-b)-1(a-b)
=
(4-1)(a-b)
=
3(a-b).
$$

#### d)

Es incorrecta.

Las expresiones:

$$
a-b
$$

y:

$$
a+b
$$

no son el mismo factor.

Tomemos, por ejemplo:

$$
a=2,\qquad b=1.
$$

El lado izquierdo vale:

$$
4(2-1)-(2+1)
=
4-3
=
1.
$$

El lado derecho vale:

$$
3(2-1)=3.
$$

Por tanto:

$$
1\ne3.
$$


### Refutar con un contraejemplo {#apm-t1-c01-e0049}

Encuentra valores sencillos que refuten cada supuesta identidad.

#### a)

$$
(a+b)^3=a^3+b^3
$$

#### b)

$$
\frac{a+b}{a}=b
$$

#### c)

$$
2+5x=7x
$$

#### Solución

#### a)

Tomemos:

$$
a=b=1.
$$

Entonces:

$$
(a+b)^3=2^3=8,
$$

mientras que:

$$
a^3+b^3=1+1=2.
$$

Por tanto:

$$
8\ne2.
$$

#### b)

Tomemos:

$$
a=2,\qquad b=4.
$$

Entonces:

$$
\frac{a+b}{a}=3,
$$

pero:

$$
b=4.
$$

Por tanto:

$$
3\ne4.
$$

#### c)

Tomemos:

$$
x=0.
$$

Entonces:

$$
2+5x=2,
$$

mientras que:

$$
7x=0.
$$

Por tanto:

$$
2\ne0.
$$

***

### Detectar la regla mal aplicada {#apm-t1-c01-e0050}

En cada caso, explica qué regla verdadera parece haber sido utilizada fuera de su contexto.

#### a)

$$
(a+b)^2=a^2+b^2
$$

#### b)

$$
\frac{x+4}{x}=4
$$

#### c)

$$
3+2x=5x
$$

#### Solución

#### a)

Se ha tratado la potencia como si se distribuyera sobre una suma.

Pero:

$$
(a+b)^2
$$

significa:

$$
(a+b)(a+b),
$$

y debe desarrollarse mediante multiplicación y distributividad.

#### b)

Se ha intentado usar cancelación como si $x$ fuera factor de todo el numerador.

Pero el numerador:

$$
x+4
$$

es una suma.

#### c)

Se ha usado el patrón correcto:

$$
3x+2x=5x
$$

en una situación donde el primer término es $3$, no $3x$.

No existe un factor común $x$ en ambos términos.

***

### Diagnóstico completo {#apm-t1-c01-e0051}

Un estudiante escribe:

$$
\frac{x^2+2x}{x}
=
x+2x
=
3x.
$$

Supón $x\ne0$.

1. Identifica el primer paso incorrecto.
2. Explica la estructura correcta del numerador.
3. Simplifica correctamente la expresión.

#### Solución

El numerador es:

$$
x^2+2x.
$$

Ambos términos contienen el factor $x$:

$$
x^2+2x
=
x(x+2).
$$

Por tanto:

$$
\frac{x^2+2x}{x}
=
\frac{x(x+2)}{x}.
$$

Como $x\ne0$, podemos cancelar el factor común $x$:

$$
\frac{x(x+2)}{x}
=
x+2.
$$

La transformación correcta es:

$$
\boxed{
\frac{x^2+2x}{x}=x+2.
}
$$

El estudiante escribió:

$$
x+2x,
$$

como si dividir cada término por $x$ produjera $x$ y $2x$.

Pero:

$$
\frac{2x}{x}=2,
$$

no $2x$.

También podríamos separar correctamente la fracción:

$$
\frac{x^2}{x}+\frac{2x}{x}
=
x+2.
$$

***

## Resumen de la sección

Los errores algebraicos más persistentes suelen parecerse a reglas verdaderas.

Por eso no basta con memorizar una lista de prohibiciones.

Debemos leer la estructura.

Hemos analizado cuatro patrones fundamentales de error:

$$
(a+b)^2=a^2+b^2,
$$

$$
\frac{a+b}{a}=b,
$$

$$
2+3x=5x,
$$

y cancelaciones falsas en expresiones como:

$$
\frac{x+3}{x+5}.
$$

El principio central de cancelación es:

$$
\boxed{
\text{se cancelan factores comunes, no términos dentro de sumas}.
}
$$

Y el protocolo general de diagnóstico es:

$$
\boxed{
\text{estructura}
\longrightarrow
\text{ley}
\longrightarrow
\text{contraejemplo}
\longrightarrow
\text{corrección}.
}
$$

Un contraejemplo puede demostrar que una supuesta regla general es falsa.

Pero comprender el error exige además identificar qué estructura fue ignorada.

La pregunta que debemos acostumbrarnos a formular es:

> **¿qué ley justifica exactamente este paso?**

***

## Hacia la sección siguiente

El capítulo comenzó con una cuenta:

$$
3+4\cdot5.
$$

Desde entonces hemos aprendido a:

- leer estructuras;
- interpretar letras;
- distinguir términos y factores;
- sustituir y evaluar;
- comprender la igualdad;
- distinguir identidades y ecuaciones;
- justificar transformaciones;
- escribir de manera inequívoca;
- diagnosticar reglas falsas.

Solo falta reunir estas capacidades en problemas donde no se indique de antemano qué técnica utilizar.

La última sección del capítulo tendrá ese objetivo:

### §10. Leer antes de operar

Allí el lector deberá decidir por sí mismo qué está viendo antes de calcular, transformar o refutar.

## §10. Leer antes de operar

Este capítulo comenzó con una pregunta muy sencilla:

> ¿qué estamos mirando cuando vemos una expresión matemática?

Desde entonces hemos aprendido que una escritura algebraica no es una fila de símbolos sobre la que debamos actuar inmediatamente.

Antes de operar podemos tener que:

- reconocer la estructura;
- interpretar el papel de una letra;
- distinguir términos y factores;
- sustituir un valor;
- leer una igualdad;
- decidir si una igualdad expresa un patrón general o una condición;
- justificar una transformación;
- aclarar el alcance de una operación;
- detectar una regla falsa.

La idea que reúne todo el capítulo es:

$$
\boxed{
\text{leer}
\longrightarrow
\text{decidir}
\longrightarrow
\text{operar o justificar}.
}
$$

No siempre la primera acción correcta es calcular.

A veces debemos detenernos y preguntar:

> **¿qué clase de objeto matemático tengo delante y qué se me está pidiendo hacer con él?**

Esta última sección no introducirá nuevas reglas. Su función es reunir las anteriores en problemas donde la técnica apropiada no viene anunciada de antemano.

***

### 10.1 Una misma escritura puede invitar a preguntas distintas

Consideremos:

$$
2(x+3)+x.
$$

Podríamos preguntar:

> ¿cuál es su operación principal?

O:

> ¿cuánto vale cuando $x=-2$?

O:

> ¿puede transformarse en una forma más simple?

Cada pregunta exige una acción distinta.

#### Pregunta estructural

La expresión completa es una suma:

$$
2(x+3)+x.
$$

Sus dos términos exteriores son:

$$
2(x+3)
\qquad\text{y}\qquad
x.
$$

#### Pregunta de evaluación

Si:

$$
x=-2,
$$

sustituimos:

$$
2((-2)+3)+(-2)
=
2\cdot1-2
=
0.
$$

#### Pregunta de transformación

Podemos escribir:

$$
\begin{aligned}
2(x+3)+x
&=2x+6+x\\
&=3x+6.
\end{aligned}
$$

Las tres respuestas hablan de la misma expresión, pero responden a preguntas diferentes.

::: {.ma-block .ma-intuicion}
**Idea clave**

Una buena lectura comienza identificando **qué problema se está planteando**, no aplicando automáticamente la última técnica aprendida.
:::

***

### 10.2 Antes de transformar, comprueba qué estás transformando

Consideremos:

$$
3x+5.
$$

No tiene sentido preguntar simplemente:

> «¿cuánto da?»

si no conocemos el valor de $x$.

Tampoco tiene sentido «simplificar» por obligación:

$$
3x+5
$$

ya expresa con claridad una suma de dos términos.

En cambio, si encontramos:

$$
3x+5+2x,
$$

podemos reconocer una estructura que permite escribir:

$$
\begin{aligned}
3x+5+2x
&=3x+2x+5\\
&=5x+5.
\end{aligned}
$$

La diferencia no consiste en que una expresión sea «larga» y otra «corta».

Consiste en que una ley algebraica ofrece una transformación útil.

***

### 10.3 Antes de confiar en una igualdad, pregúntate qué afirma

Comparemos:

$$
3(x+2)=3x+6
$$

y:

$$
3x+2=11.
$$

En el primer caso, reconocemos una identidad basada en distributividad.

En el segundo, reconocemos una ecuación: la igualdad impone una condición sobre $x$.

Ahora comparemos:

$$
3(x+2)=3x+2.
$$

Aquí no basta con observar que «hay distributividad».

Precisamente la distributividad nos permite detectar que la transformación está mal:

$$
3(x+2)
=
3x+6,
$$

no:

$$
3x+2.
$$

Podemos confirmarlo con un valor sencillo, por ejemplo:

$$
x=0.
$$

La igualdad falsa produciría:

$$
6=2.
$$

Así, una misma lectura estructural nos permite:

- reconocer una identidad correcta;
- reconocer una ecuación;
- refutar una supuesta identidad.

***

### 10.4 Antes de cancelar, busca factores

Consideremos:

$$
\frac{x(x+4)}{x}
$$

y:

$$
\frac{x+4}{x}.
$$

En la primera expresión, cuando $x\ne0$, existe un factor común $x$:

$$
\frac{x(x+4)}{x}=x+4.
$$

En la segunda, $x$ es solo un término del numerador:

$$
\frac{x+4}{x}
=
1+\frac4x,
\qquad x\ne0.
$$

No se cancela.

La pregunta adecuada antes de tachar símbolos es:

> ¿lo que quiero cancelar es realmente un factor de toda la expresión correspondiente?

El hábito de **leer antes de operar** evita aquí un error que no podría corregirse únicamente con rapidez de cálculo.

***

### 10.5 Antes de aceptar una notación, reconstruye su alcance

Comparemos:

$$
-x^2
$$

con:

$$
(-x)^2.
$$

O:

$$
\frac{a+b}{c}
$$

con:

$$
a+\frac bc.
$$

En cada par, pequeños cambios de notación producen estructuras distintas.

Cuando recibimos una expresión compleja, conviene leerla desde fuera hacia dentro:

1. identificar la operación exterior;
2. reconocer sus partes principales;
3. continuar con las subexpresiones;
4. solo después operar.

Este procedimiento no añade una regla nueva al álgebra.

Añade disciplina a la lectura.

***

### 10.6 Un protocolo mínimo para afrontar una expresión

Podemos reunir el capítulo en una secuencia de preguntas.

#### 1. ¿Qué está escrito?

¿Es una expresión, una igualdad, una cadena de igualdades?

#### 2. ¿Cuál es su estructura?

¿Qué operación actúa desde fuera? ¿Cuáles son las subexpresiones?

#### 3. ¿Qué significan las letras?

¿Hay valores dados? ¿Son variables generales? ¿Hay alguna por determinar?

#### 4. ¿Qué se pide?

¿Evaluar, transformar, comparar, justificar, refutar?

#### 5. Si transformo, ¿qué ley uso?

¿Conmutatividad, asociatividad, distributividad u otra regla ya establecida?

#### 6. Si sospecho que algo es falso, ¿puedo probar un caso sencillo?

El valor concreto puede revelar rápidamente una inconsistencia.

#### 7. ¿La escritura final conserva lo que quería expresar?

¿Los paréntesis, exponentes y barras de fracción tienen el alcance correcto?

Este protocolo resume la transición que buscaba el capítulo:

$$
\boxed{
\text{hacer cuentas}
\longrightarrow
\text{leer estructuras}
\longrightarrow
\text{justificar transformaciones}.
}
$$

***

## Problemas de síntesis

### Una expresión, varias preguntas {#apm-t1-c01-e0052}

Considera:

$$
4(x-1)+2x.
$$

#### a)

Identifica la operación principal y los términos exteriores.

#### b)

Evalúa la expresión cuando:

$$
x=3.
$$

#### c)

Transfórmala a una expresión de la forma:

$$
ax+b
$$

y justifica cada paso.

#### Solución

#### a)

La operación principal es una suma.

Los términos exteriores son:

$$
4(x-1)
$$

y:

$$
2x.
$$

#### b)

Sustituimos:

$$
x=3.
$$

Entonces:

$$
4(3-1)+2\cdot3
=
4\cdot2+6
=
14.
$$

#### c)

Por distributividad:

$$
4(x-1)+2x
=
4x-4+2x.
$$

Reordenamos y agrupamos:

$$
4x-4+2x
=
4x+2x-4.
$$

Por distributividad en sentido inverso:

$$
4x+2x-4
=
(4+2)x-4.
$$

Por aritmética:

$$
(4+2)x-4
=
6x-4.
$$

Así:

$$
\boxed{4(x-1)+2x=6x-4}.
$$

***

### Una línea, dos estructuras {#apm-t1-c01-e0053}

Considera la escritura lineal:

```text
12/3+1
```

#### a)

Escríbela de manera inequívoca si se quiere representar:

$$
\frac{12}{3}+1.
$$

Calcula su valor e identifica la operación principal.

#### b)

Modifica los paréntesis para representar:

$$
\frac{12}{3+1}.
$$

Calcula su valor e identifica la operación principal.

#### c)

Explica por qué una escritura lineal clara debe conservar la estructura de la expresión original.

#### Solución

#### a)

Podemos escribir:

```text
(12/3)+1
```

o simplemente:

```text
12/3+1
```

si usamos la precedencia usual.

La expresión matemática es:

$$
\frac{12}{3}+1.
$$

Calculamos:

$$
\frac{12}{3}+1
=
4+1
=
5.
$$

La operación principal es la suma.

#### b)

Debemos escribir:

```text
12/(3+1)
```

porque todo $3+1$ forma el denominador.

Entonces:

$$
\frac{12}{3+1}
=
\frac{12}{4}
=
3.
$$

La operación principal es la división.

#### c)

Las dos expresiones contienen los mismos números y signos básicos, pero los paréntesis determinan agrupamientos diferentes.

Por tanto:

$$
\boxed{
\text{la escritura lineal debe conservar el alcance de las operaciones}.
}
$$


### Reparar una cadena {#apm-t1-c01-e0054}

Un estudiante quiere calcular:

$$
3(5+1)+2.
$$

Escribe:

$$
5+1=6\cdot3=18+2=20.
$$

#### a)

Explica por qué la cadena es incorrecta.

#### b)

Escribe una cadena correcta.

#### c)

Indica qué principio sobre el signo igual estás utilizando.

#### Solución

#### a)

La cadena usa $=$ como si significara «y después».

Por ejemplo, afirma:

$$
5+1=6\cdot3,
$$

es decir:

$$
6=18,
$$

lo cual es falso.

#### b)

Debemos conservar el valor de la expresión original:

$$
\begin{aligned}
3(5+1)+2
&=3\cdot6+2\\
&=18+2\\
&=20.
\end{aligned}
$$

#### c)

Cada signo igual afirma que las expresiones que conecta representan el mismo valor.

Por eso todos los miembros de una cadena correcta de igualdades deben representar lo mismo.

***

### Identidad, ecuación o falsa regla {#apm-t1-c01-e0055}

Clasifica cada escritura en el contexto indicado.

#### a)

> «La distributividad nos da»:

$$
7(x+2)=7x+14.
$$

#### b)

> «Determina qué valores de $x$ hacen verdadera»:

$$
7x+2=16.
$$

#### c)

> «Esta regla vale para cualquier $x$»:

$$
7(x+2)=7x+2.
$$

En el caso c), decide además si la afirmación es correcta.

#### Solución

#### a)

Se presenta como una **identidad**.

La distributividad justifica:

$$
7(x+2)
=
7x+14.
$$

#### b)

Se presenta como una **ecuación**.

La pregunta pide determinar qué valores de $x$ hacen verdadera la igualdad.

No necesitamos resolverla aquí para clasificarla.

#### c)

Se pretende presentar como una identidad, pero es falsa.

Tomemos:

$$
x=0.
$$

Entonces el lado izquierdo vale:

$$
7(0+2)=14,
$$

mientras que el derecho vale:

$$
7\cdot0+2=2.
$$

Como:

$$
14\ne2,
$$

la supuesta identidad queda refutada.

***

### Diagnóstico final {#apm-t1-c01-e0056}

Un estudiante escribe:

$$
\frac{2x+6}{2}=x+6.
$$

#### a)

Decide si la igualdad es correcta.

#### b)

Si es falsa, encuentra un contraejemplo numérico.

#### c)

Analiza la estructura del numerador.

#### d)

Corrige la transformación.

#### Solución

#### a)

La igualdad es falsa.

#### b)

Tomemos:

$$
x=0.
$$

Entonces:

$$
\frac{2\cdot0+6}{2}
=
\frac62
=
3,
$$

mientras que:

$$
0+6=6.
$$

Por tanto:

$$
3\ne6.
$$

#### c)

El numerador es:

$$
2x+6.
$$

Podemos extraer el factor común $2$:

$$
2x+6
=
2x+2\cdot3
=
2(x+3).
$$

#### d)

Así:

$$
\frac{2x+6}{2}
=
\frac{2(x+3)}{2}
=
x+3.
$$

La transformación correcta es:

$$
\boxed{
\frac{2x+6}{2}=x+3.
}
$$

El error consistió en dividir correctamente $2x$ por $2$, pero no dividir también $6$ por $2$.

***

## Cierre del capítulo

El objetivo de este capítulo no era enseñar una colección de trucos algebraicos.

Era cambiar la manera de mirar una escritura matemática.

Comenzamos distinguiendo una expresión de su valor.

Después vimos que las letras adquieren significado por el contexto, que una expresión tiene partes y niveles, y que sustituir exige conservar su estructura.

Aprendimos que:

$$
=
$$

no significa «ahora hago otra cosa», sino que afirma igualdad.

Distinguimos una identidad de una ecuación en un primer sentido operativo.

Vimos que transformar una expresión exige una ley, que la notación debe hacer visible el alcance de las operaciones y que muchas reglas falsas nacen de aplicar una regla correcta a la estructura equivocada.

Podemos condensar el capítulo en cinco hábitos.

::: {.ma-block .ma-observacion}
**Síntesis**

**1. Leer antes de calcular.**  
**2. Conservar la estructura al sustituir.**  
**3. Usar el signo igual con significado.**  
**4. Justificar cada transformación.**  
**5. Buscar la estructura antes de aplicar una regla.**
:::

El resultado no es todavía una teoría abstracta del álgebra.

Es algo previo y necesario: una disciplina del lenguaje simbólico.

***

## Hacia el capítulo siguiente

Consideremos ahora dos afirmaciones:

$$
x=2
$$

y:

$$
x^2=4.
$$

Podemos preguntar:

- si la primera es correcta, ¿qué podemos decir de la segunda?
- si la segunda es correcta, ¿podemos concluir la primera?
- ¿cómo expresamos «y», «o» y «no» dentro del razonamiento matemático?
- ¿cuándo dos afirmaciones dicen esencialmente lo mismo?
- ¿cómo podemos transformar una afirmación sin cambiar su contenido?

Hasta ahora hemos trabajado principalmente con **expresiones** e **igualdades**.

El paso siguiente será estudiar las afirmaciones mismas y las operaciones que podemos realizar con ellas.

Eso abre:

**Capítulo 2. Lógica proposicional y álgebra de proposiciones**

Allí encontraremos una nueva clase de objetos simbólicos y una nueva colección de operaciones y leyes.

La misma idea estructural reaparecerá:

$$
\boxed{
\text{objetos}
+
\text{operaciones}
+
\text{leyes}.
}
$$

Y descubriremos que el tipo de pensamiento que acabamos de practicar con expresiones algebraicas puede aplicarse también al razonamiento lógico.
