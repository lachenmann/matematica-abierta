## §9. Parámetros: qué está fijo y qué puede variar

Hasta ahora hemos utilizado letras para representar valores que pueden cambiar.

Por ejemplo, en:

$$
P(x):\quad x^2=4,
$$

la letra $x$ ocupa un lugar variable. Podemos sustituirla, cuantificarla o estudiar qué ocurre cuando recorre un dominio.

Pero en matemáticas también es frecuente encontrar letras cuyo papel es distinto.

Consideremos la frase:

> «Fijemos un entero $a$ y estudiemos los enteros $x$ que satisfacen $x+a=a$».

Aquí aparecen dos letras:

$$
a
\qquad\text{y}\qquad
x.
$$

Sin embargo, no cumplen la misma función. Durante esta discusión:

- $a$ se mantiene fijo;
- $x$ puede variar.

La letra $a$ recibe entonces el papel de **parámetro**.

Esta distinción será fundamental en álgebra.

---

### 9.1 Fijar no significa elegir para siempre

Supongamos que decimos:

> «Fijemos un entero $a$».

Podríamos estar considerando:

$$
a=5.
$$

Durante esa discusión, cuando estudiamos:

$$
x+a=a,
$$

la expresión concreta es:

$$
x+5=5.
$$

La letra $x$ puede tomar distintos valores.

Pero:

$$
a
$$

no cambia dentro de esa misma discusión.

Ahora bien, en otra discusión podríamos fijar:

$$
a=-2
$$

y estudiar:

$$
x-2=-2.
$$

Por tanto, «fijar $a$» no significa asignarle un valor que deba conservar para siempre.

Significa:

$$
\boxed{
\text{mantener su valor constante dentro del contexto actual}.
}
$$

El valor del parámetro puede cambiar cuando cambiamos de contexto.

---

### 9.2 Parámetro

::: {.ma-block .ma-definicion #apm-i-d0034}
**Definición — Parámetro**

Un **parámetro** es un símbolo cuyo valor se mantiene fijo dentro de una discusión, mientras otras variables pueden seguir variando o siendo cuantificadas.

El valor fijado para el parámetro puede ser distinto en otra discusión.
:::

Esta definición refina el uso operativo de **constante** introducido en [el capítulo 1](algebra-para-matematicos-capitulo-1-del-calculo-aritmetico-al-lenguaje-algebraico.md). En el sentido de aquel capítulo, un parámetro actúa como una constante dentro de la discusión: su valor permanece fijo. La palabra **parámetro** destaca ahora un papel más específico: ese valor fijo determina uno de varios casos posibles mientras otras variables continúan variando o siendo cuantificadas. Al cambiar de caso, el parámetro puede recibir otro valor.

Por tanto, en este nivel del tratado, «constante» y «parámetro» no son categorías incompatibles: todo parámetro actúa localmente como constante, pero hablamos de parámetro cuando queremos destacar su papel dentro de una familia de casos.

Así, si declaramos:

> «Fijemos un entero $a$»,

y escribimos:

$$
P_a(x):\quad x+a=a,
$$

la notación:

$$
P_a(x)
$$

hace visibles dos papeles:

- $a$ es un parámetro fijado por el contexto;
- $x$ es la variable de la condición.

No estamos definiendo todavía una función:

$$
a\longmapsto P_a.
$$

El subíndice solo nos recuerda que la condición que estudiamos depende del valor que haya sido fijado para $a$.

---

### 9.3 Variable y parámetro no son tipos de letras

Las letras:

$$
a,b,c
$$

no son parámetros por naturaleza. Del mismo modo, las letras:

$$
x,y,z
$$

no son variables por naturaleza. El papel depende del contexto.

Por ejemplo, podemos escribir:

> «Fijemos $a$ y dejemos variar $x$».

Aquí:

$$
a
$$

es parámetro y:

$$
x
$$

es variable.

Pero también podríamos iniciar otra discusión diciendo:

> «Fijemos $x$ y dejemos variar $a$».

Entonces sus papeles se invierten. Por tanto:

$$

\text{el papel de un símbolo se determina por la discusión, no por su forma gráfica}.

$$

Las convenciones de letras ayudan a leer, pero no sustituyen una declaración explícita.

---

### 9.4 Parámetro y variable cuantificada

Consideremos, en el dominio de los enteros:

> «Fijemos un entero $a$».

Ahora escribimos $\exists x\,(x+a=a)$. El cuantificador $\exists x$ actúa sobre:

$$
x.
$$

La letra $a$ no está siendo cuantificada. Permanece fija durante la discusión.

Para cualquier valor entero que hayamos fijado como parámetro, podemos tomar:

$$
x=0.
$$

Entonces $0+a=a$. Así, la fórmula cuantificada expresa una afirmación acerca de la variable $x$ **bajo un valor previamente fijado del parámetro $a$**.

La diferencia de papeles es:

$$

a:\ \text{fijo en el contexto}
\qquad
x:\ \text{ligado por el cuantificador}.

$$

---

### 9.5 Un parámetro puede aparecer muchas veces

Supongamos que hemos fijado un entero:

$$
a.
$$

Consideremos $R_a(x,y):\quad x+a=y+a$. El parámetro:

$$
a
$$

aparece dos veces. Las variables:

$$
x
\qquad\text{y}
$$

pueden variar. Si escribimos:

$$
\forall x\,\forall y\,R_a(x,y),
$$

los cuantificadores ligan las apariciones de $x$ y de $y$.

El parámetro $a$ permanece fijo. El hecho de que una letra aparezca muchas veces no determina si es parámetro o variable.

Lo determina el papel que le hemos asignado en el contexto.

---

### 9.6 Cambiar un parámetro entre contextos

Consideremos:

$$
P_a(x):\quad x+a=6.
$$

#### Primer contexto

Fijemos:

$$
a=1.
$$

Entonces $P_1(x):\quad x+1=6$. El valor $x=5$ satisface la condición.

#### Segundo contexto

Ahora comenzamos otra discusión y fijamos:

$$
a=4.
$$

Entonces $P_4(x):\quad x+4=6$. El valor $x=2$ satisface la condición. No hay contradicción. Hemos cambiado de contexto.

La condición depende del parámetro fijado y puede, por tanto, cambiar cuando elegimos otro valor para ese parámetro.

Podemos pensar informalmente en las expresiones:

$$
P_1(x),\quad P_2(x),\quad P_3(x),\ldots
$$

como distintas condiciones obtenidas al fijar distintos valores de $a$.

No necesitamos formalizar todavía esa colección como una función.

---

### 9.7 Lo que no debemos hacer: cambiar de papel en silencio

Supongamos que una argumentación comienza:

> «Fijemos un entero $a$».

A partir de ese momento, dentro de esa discusión, $a$ debe conservar ese papel mientras no anunciemos explícitamente un cambio de contexto.

Sería incorrecto razonar así:

> «Fijemos $a=3$. Como $a$ puede variar, tomemos ahora $a=7$».

La primera frase ha declarado que $a$ permanece fijo durante la discusión.

Cambiar su valor sin avisar destruye el contexto lógico en el que se estaban interpretando las fórmulas.

Si queremos considerar otro valor, debemos decirlo explícitamente:

> «Ahora iniciemos un segundo caso y fijemos $a=7$».

Así:

$$
\boxed{
\text{un parámetro puede cambiar entre contextos, no silenciosamente dentro de uno}.
}
$$

---

### 9.8 Parámetro no significa valor desconocido

En lenguaje elemental se dice a veces que una letra representa «un número desconocido».

Esa descripción es demasiado pobre para lo que necesitamos.

Un parámetro puede tener un valor perfectamente fijado en el contexto.

Por ejemplo:

> «Fijemos $a=5$».

No hay nada desconocido en:

$$
a.
$$

Lo importante es su **papel**:

$$
a
$$

permanece fijo mientras:

$$
x
$$

puede variar. Por tanto:

$$
\boxed{
\text{parámetro}
\neq
\text{«número que no conocemos».}
}
$$

La distinción pertinente es:

> **qué permanece fijo y qué puede variar**.

---

### 9.9 Una fórmula puede depender de un parámetro sin cuantificarlo

Fijemos un entero:

$$
a.
$$

Consideremos $\forall x\,(x+a=a+x)$. La variable:

$$
x
$$

está cuantificada. El parámetro:

$$
a
$$

permanece fijo. La fórmula dice:

> «Para todo entero $x$, $x+a=a+x$»,

bajo el valor de $a$ que haya sido fijado previamente.

Podemos repetir la discusión para distintos valores del parámetro.

Pero en cada discusión concreta, $a$ mantiene un único valor.

Esta forma de pensar será muy frecuente más adelante: estudiamos una afirmación **para una variable que recorre un dominio**, mientras uno o varios parámetros se mantienen fijos.

---

### 9.10 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-i-x0029}
**Ejemplo — Un parámetro fijo y una variable que cambia**
:::

Trabajaremos con valores enteros. Fijemos un entero:

$$
a.
$$

Consideremos:

$$
P_a(x):\quad x+a=a.
$$

#### Paso 1 — Identificar los papeles

La letra $a$ es un parámetro. Su valor permanece fijo durante la discusión.

La letra $x$ es la variable de la condición.

#### Paso 2 — Primer contexto

Fijemos:

$$
a=5.
$$

Entonces $P_5(x):\quad x+5=5$. Probamos:

$$
x=0.
$$

Obtenemos $0+5=5$, que es verdadera. Si probamos:

$$
x=2,
$$

obtenemos $2+5=5$, que es falsa. Durante este contexto:

$$
a=5
$$

no cambia.

#### Paso 3 — Segundo contexto

Iniciemos ahora otra discusión y fijemos:

$$
a=-2.
$$

Entonces $P_{-2}(x):\quad x-2=-2$. De nuevo:

$$
x=0
$$

hace verdadera la condición:

$$
0-2=-2.
$$

#### Paso 4 — Añadir un cuantificador

Bajo un valor fijo cualquiera de $a$, podemos escribir:

$$
\exists x\,P_a(x).
$$

La afirmación es verdadera porque:

$$
x=0
$$

es un testigo:

$$
0+a=a.
$$

Aquí:

- $a$ permanece fijo como parámetro;
- $x$ está ligado por el cuantificador existencial.

#### Conclusión

La misma escritura puede contener símbolos con papeles diferentes.

El contexto debe decirnos con claridad:

$$
\boxed{
\text{qué está fijo}
\qquad\text{y}\qquad
\text{qué puede variar}.
}
$$

---
## Ejercicios

### Parámetro y variable {#apm-i-e0183}
Trabajamos con enteros.

Se declara:

> «Fijemos un entero $a$ y consideremos $P_a(x): x+a=10$».

#### a)

¿Cuál es el parámetro?

#### b)

¿Cuál es la variable?

#### c)

Si fijamos $a=3$, ¿qué fórmula obtenemos?

#### Solución


#### a)

El parámetro es:

$$
a.
$$

Su valor se mantiene fijo durante la discusión.

#### b)

La variable es:

$$
x.
$$

Es el valor que puede cambiar al estudiar la condición.

#### c)

Si:

$$
a=3,
$$

obtenemos:

$$
P_3(x):\quad x+3=10.
$$

Dentro de ese contexto, $3$ permanece fijo mientras $x$ puede variar.

---

### ¿Qué significa «fijemos $a$»? {#apm-i-e0184}
Explica con tus propias palabras qué significa la instrucción:

> «Fijemos un entero $a$».

Aclara también qué **no** significa.

#### Solución


La instrucción significa que elegimos un valor entero para:

$$
a
$$

y mantenemos ese valor sin cambios durante la discusión que sigue.

No significa que:

- $a$ tenga que conservar ese mismo valor en todas las discusiones futuras;
- el valor de $a$ sea necesariamente desconocido;
- $a$ pueda cambiar silenciosamente mientras seguimos dentro del mismo contexto.

En otra discusión podemos fijar otro valor de $a$, pero debemos indicar explícitamente que hemos cambiado de contexto.

---

### Dos contextos distintos {#apm-i-e0185}
Considera:

$$
P_a(x):\quad x+a=8.
$$

#### Contexto A

Fijamos:

$$
a=2.
$$

#### Contexto B

Fijamos:

$$
a=5.
$$

#### a)

Escribe la condición correspondiente en cada contexto.

#### b)

Encuentra un valor de $x$ que la haga verdadera en cada caso.

#### c)

Explica por qué cambiar de $a=2$ a $a=5$ no contradice la idea de parámetro.

#### Solución


#### a)

En el contexto A:

$$
P_2(x):\quad x+2=8.
$$

En el contexto B:

$$
P_5(x):\quad x+5=8.
$$

#### b)

En el contexto A:

$$
x=6
$$

hace verdadera:

$$
6+2=8.
$$

En el contexto B:

$$
x=3
$$

hace verdadera:

$$
3+5=8.
$$

#### c)

No hemos cambiado el valor del parámetro dentro de una misma discusión.

Hemos considerado dos contextos diferentes.

En cada uno, $a$ permanece fijo.

La idea de parámetro permite precisamente repetir un mismo tipo de análisis bajo distintos valores fijados.

---

### Por qué no puede cambiar de papel en silencio {#apm-i-e0186}
Una argumentación comienza:

> «Fijemos $a=4$».

Después afirma:

> «Como $a$ puede variar, tomemos ahora $a=9$».

Explica cuál es el problema lógico y cómo podría corregirse la redacción.

#### Solución


La primera frase asignó a:

$$
a
$$

el papel de parámetro y fijó su valor en:

$$
4.
$$

Mientras permanezcamos en esa discusión, $a$ debe conservar ese valor.

La segunda frase cambia:

$$
a=4
$$

por:

$$
a=9
$$

sin anunciar un cambio de contexto.

Eso hace ambiguo qué fórmulas pertenecen a cada situación.

La redacción puede corregirse diciendo, por ejemplo:

> «En el primer contexto fijemos $a=4$. Ahora iniciemos un segundo contexto y fijemos $a=9$».

Así el papel de $a$ permanece coherente dentro de cada discusión.

---

### Explorar varios valores de un parámetro {#apm-i-e0187}
Trabajamos con enteros y consideramos:

$$
P_a(x):\quad x+a=5.
$$

Estudia los casos:

$$
a=0,\qquad a=2,\qquad a=5,\qquad a=-1.
$$

#### a)

Escribe las cuatro condiciones obtenidas.

#### b)

Encuentra en cada caso un valor de $x$ que haga verdadera la condición.

#### c)

¿Qué patrón observas entre el valor fijado de $a$ y el valor de $x$ que funciona?

#### Solución


#### a)

Si:

$$
a=0,
$$

tenemos:

$$
P_0(x):\quad x=5.
$$

Si:

$$
a=2,
$$

tenemos:

$$
P_2(x):\quad x+2=5.
$$

Si:

$$
a=5,
$$

tenemos:

$$
P_5(x):\quad x+5=5.
$$

Si:

$$
a=-1,
$$

tenemos:

$$
P_{-1}(x):\quad x-1=5.
$$

#### b)

Los valores correspondientes son:

$$
a=0 \quad\Rightarrow\quad x=5,
$$

$$
a=2 \quad\Rightarrow\quad x=3,
$$

$$
a=5 \quad\Rightarrow\quad x=0,
$$

$$
a=-1 \quad\Rightarrow\quad x=6.
$$

#### c)

En todos los casos se cumple:

$$
x=5-a.
$$

Al cambiar el valor fijado del parámetro cambia la condición concreta y, con ella, el valor de $x$ que la satisface.

---

### Parámetro y cuantificador {#apm-i-e0188}
Trabajamos con enteros.

Se declara:

> «Fijemos un entero $a$».

Considera:

$$
\forall x\,(x+a=a+x).
$$

#### a)

¿Qué símbolo funciona como parámetro?

#### b)

¿Qué símbolo está cuantificado?

#### c)

¿Qué permanece fijo y qué puede variar?

#### d)

Explica por qué cambiar el valor de $a$ exige iniciar otro contexto, mientras $x$ puede recorrer el dominio dentro de la misma afirmación.

#### e)

Escribe la fórmula concreta que obtenemos si fijamos $a=7$.

#### Solución


#### a)

El parámetro es:

$$
a.
$$

#### b)

La variable cuantificada es:

$$
x.
$$

#### c)

El valor de:

$$
a
$$

permanece fijo durante la discusión.

La variable:

$$
x
$$

recorre el dominio según lo indica:

$$
\forall x.
$$

#### d)

La declaración inicial asignó a $a$ un valor fijo dentro del contexto.

Cambiar ese valor sin avisar rompería esa declaración.

En cambio, la fórmula misma ordena considerar todos los valores permitidos de $x$, de modo que la variación de $x$ forma parte de la afirmación.

#### e)

Si fijamos:

$$
a=7,
$$

obtenemos:

$$
\boxed{
\forall x\,(x+7=7+x).
}
$$

El número $7$ ocupa ahora el lugar del parámetro fijado, mientras $x$ continúa cuantificada.

---

## Síntesis

La distinción central de esta sección es:

$$

\text{parámetro}
=
\text{símbolo fijado por el contexto}

$$

frente a:

$$

\text{variable}
=
\text{símbolo cuyo valor puede seguir variando o siendo cuantificado}.

$$

Pero esta diferencia no pertenece a las letras mismas.

Depende del papel que les asignamos. Así, en:

$$
P_a(x),
$$

podemos decidir que:

- $a$ permanece fijo;
- $x$ puede variar.

Y en:

$$
\exists x\,P_a(x),
$$

$x$ queda ligada por el cuantificador mientras $a$ continúa fijo por el contexto.

También debemos distinguir dos operaciones:

$$

\text{cambiar una variable dentro del mismo contexto}

$$

y:

$$

\text{cambiar el valor de un parámetro al iniciar otro contexto}.

$$

Un parámetro no puede cambiar silenciosamente de valor ni de papel dentro de una discusión.

Nos queda ahora una distinción lógica que ya anticipamos en §4.

Decir:

> «existe al menos uno»

no es lo mismo que decir:

> «existe exactamente uno».

## Hacia la sección siguiente

Hasta ahora escribimos:

$$
\exists x\,P(x)
$$

para afirmar existencia.

Pero ¿cómo expresamos que hay **un único** valor que satisface la condición?

La próxima sección introducirá la abreviatura:

$$
\exists!
$$

y separará rigurosamente las dos partes de una afirmación de existencia única:

- existencia;
- unicidad.
