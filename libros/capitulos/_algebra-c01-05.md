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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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
