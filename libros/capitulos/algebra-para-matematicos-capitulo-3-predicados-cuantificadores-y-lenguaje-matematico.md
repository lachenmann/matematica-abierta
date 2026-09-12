---
title: "Predicados, cuantificadores y lenguaje matemático"
description: "Tercer capítulo de Álgebra para matemáticos: fórmulas abiertas, predicados, cuantificadores, alcance, variables libres y ligadas, orden de cuantificadores, parámetros y existencia única."
content-id: MA-BCH-0011
source-id: APM-T1-C03
content-type: book-chapter
collection: PM-ALG
book-id: MA-BOK-0004
status: published
date-created: 2026-09-10
date-modified: 2026-09-10
areas:
  - fundamentos
  - algebra
  - logica
level: fundamental
topics:
  - predicados
  - cuantificadores
  - dominio-de-discurso
  - variables-libres-y-ligadas
  - alcance
  - orden-de-cuantificadores
  - parametros
  - existencia-y-unicidad
prerequisites:
  - MA-BCH-0008
related:
  - MA-BOK-0004
  - MA-BCH-0007
  - MA-BCH-0008
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Predicados, cuantificadores y lenguaje matemático

## §1. Una afirmación que espera un valor

En el capítulo anterior trabajamos con proposiciones: afirmaciones a las que, en un contexto dado, podemos asignar uno de los dos valores:

$$
\mathrm V,
\qquad
\mathrm F.
$$

Por ejemplo:

> «Tres más dos es igual a cinco».

expresa la proposición:

$$
3+2=5,
$$

que es verdadera. Y:

> «Tres más dos es igual a seis».

expresa $3+2=6$, que es falsa. En ambos casos sabemos exactamente de qué objetos estamos hablando.

Pero consideremos ahora:

$$
x+2=5.
$$

¿Es verdadera?

¿Es falsa?

La pregunta todavía no tiene una respuesta única. Si reemplazamos $x$ por $3$, obtenemos $3+2=5$, que es verdadera.

Si reemplazamos $x$ por $4$, obtenemos $4+2=5$, que es falsa.

La escritura $x+2=5$ no es todavía una proposición: el contexto aún no ha fijado el valor que ocupa el lugar de $x$.

Este será el punto de partida del capítulo.

$$
\boxed{
\text{una fórmula puede esperar todavía que fijemos el valor de una variable}.
}
$$

---

### 1.1 Una expresión con un lugar todavía abierto

Comparemos $7-2=5$ con $x-2=5$. En la primera expresión todos los valores están determinados.

Podemos decidir inmediatamente que:

$$
7-2=5
$$

es verdadera. En la segunda, una parte de la expresión permanece abierta.

La letra $x$ ocupa un lugar cuyo valor todavía puede cambiar.

Si sustituimos:

$$
x=7,
$$

obtenemos una proposición verdadera. Si sustituimos:

$$
x=6,
$$

obtenemos $6-2=5$, que es falsa. Por tanto, mientras no hayamos fijado $x$, la escritura $x-2=5$ no posee todavía un único valor de verdad.

::: {.ma-block .ma-definicion #apm-t1-c03-d0025}
**Definición — Fórmula abierta**

En esta primera etapa, llamaremos **fórmula abierta** a una fórmula que contiene una o más variables cuyos valores no han sido fijados y que, por ello, todavía no determina por sí sola una proposición.

Esta caracterización es provisional. En §6 la precisaremos mediante la noción de **aparición libre**.
:::

En esta sección trabajaremos únicamente con fórmulas abiertas muy sencillas.

Más adelante precisaremos esta noción cuando podamos distinguir formalmente entre apariciones libres y ligadas.

---

### 1.2 Sustituir un valor

Cuando una fórmula contiene una variable, podemos reemplazar esa variable por un valor concreto permitido.

Por ejemplo, partimos de:

$$
x^2=9.
$$

Si sustituimos:

$$
x=3,
$$

obtenemos $3^2=9$, que es verdadera. Si sustituimos:

$$
x=2,
$$

obtenemos $2^2=9$, que es falsa. La sustitución ha transformado la fórmula abierta en una afirmación concreta cuyo valor de verdad podemos decidir.

Así aparece una primera trayectoria:

$$
\boxed{
\text{fórmula abierta}
\longrightarrow
\text{sustitución concreta}
\longrightarrow
\text{proposición}.
}
$$

La variable no significa «un número desconocido» en un único sentido fijo.

En este contexto significa, más precisamente, un lugar cuyo valor puede variar dentro de lo que hayamos permitido.

Y eso conduce a una segunda pregunta:

> ¿qué valores están permitidos?

---

### 1.3 El dominio importa

Supongamos que escribimos:

$$
2x=1.
$$

Si estamos trabajando con los enteros, valores como:

$$
0,\quad 1,\quad -2,\quad 7
$$

son valores permitidos para $x$.

Pero:

$$
\frac12
$$

no es un entero. Si el contexto declara que $x$ debe tomar valores enteros, no podemos usar:

$$
x=\frac12
$$

como sustitución permitida.

En cambio, si estamos trabajando con los números racionales o con los números reales, entonces $x=\frac12$ sí es una sustitución admisible, y produce:

$$
2\cdot\frac12=1,
$$

que es verdadera. La escritura $2x=1$ es la misma.

Lo que cambia es la colección de objetos entre los que permitimos variar a $x$.

::: {.ma-block .ma-definicion #apm-t1-c03-d0026}
**Definición — Dominio de discurso**

El **dominio de discurso** es la colección de objetos admitidos como posibles valores de una variable durante una discusión.
:::

La palabra «colección» se usa aquí de manera informal.

Todavía no estamos desarrollando teoría de conjuntos. Lo único que necesitamos por ahora es declarar con claridad **qué clase de valores puede ocupar la variable**.

Por ejemplo:

> En esta discusión, $x$ puede tomar valores enteros.

o:

> En esta discusión, $x$ puede tomar valores reales.

En ambos casos el dominio queda determinado.

---

### 1.4 Una misma fórmula, distintas preguntas

Consideremos $x^2=4$. Si declaramos que $x$ toma valores enteros, podemos probar sustituciones como:

$$
x=2,
\qquad
x=-2,
\qquad
x=3.
$$

Obtenemos:

$$
2^2=4,
$$

$$
(-2)^2=4,
$$

$$
3^2=4.
$$

Las dos primeras proposiciones son verdaderas y la tercera es falsa.

Si ahora declaramos que $x$ toma valores reales, siguen siendo posibles esas mismas sustituciones, pero aparecen además muchas otras, por ejemplo:

$$
x=\frac12.
$$

Entonces $\left(\frac12\right)^2=4$ es falsa. La fórmula escrita sigue siendo:

$$
x^2=4.
$$

Pero el dominio determina qué valores tiene sentido considerar como sustituciones permitidas.

Esto es importante incluso cuando las sustituciones que hacen verdadera la fórmula coinciden en dos dominios diferentes.

El dominio forma parte del significado de la discusión.

---

### 1.5 Tres preguntas distintas

Ante una expresión como:

$$
x^2=4,
$$

conviene separar tres preguntas.

#### Pregunta 1 — ¿Cuál es la fórmula?

La fórmula es:

$$
x^2=4.
$$

#### Pregunta 2 — ¿Qué valores puede tomar la variable?

Eso lo determina el dominio. Por ejemplo:

> $x$ puede tomar valores enteros.

#### Pregunta 3 — ¿Qué ocurre después de una sustitución concreta?

Si elegimos:

$$
x=-2,
$$

obtenemos $(-2)^2=4$, que es verdadera. Si elegimos:

$$
x=0,
$$

obtenemos $0^2=4$, que es falsa. Mantener separadas estas tres preguntas evita una confusión frecuente:

> la fórmula abierta no tiene por sí sola «el» valor de verdad que tendrán todas sus sustituciones.

Distintas sustituciones pueden producir proposiciones con valores diferentes.

---

### 1.6 Fórmula abierta no significa fórmula falsa

Consideremos $x+1=10$. Sería incorrecto decir:

> «La fórmula es falsa porque no sabemos cuánto vale $x$».

No conocer todavía un valor de $x$ no convierte la fórmula en falsa.

Tampoco la convierte en verdadera. Mientras no hayamos fijado el valor de la variable, la fórmula sigue abierta.

Por ejemplo, $x=9$ produce:

$$
9+1=10,
$$

que es verdadera. Mientras que:

$$
x=8
$$

produce $8+1=10$, que es falsa. Por tanto:

$$
\boxed{
\text{«abierta» no significa «falsa»;}
\quad
\text{significa «con variables todavía no fijadas en esta etapa».}
}
$$

---

### 1.7 El dominio también puede cambiar el comportamiento

Volvamos a $2x=1$. En el dominio de los enteros, ninguna de las sustituciones permitidas convierte la fórmula en:

$$
\mathrm V.
$$

En el dominio de los racionales, en cambio:

$$
x=\frac12
$$

sí produce una proposición verdadera. Por tanto, el dominio no solo determina qué sustituciones podemos hacer.

También puede cambiar qué comportamientos encontramos al recorrer esas sustituciones.

Esto anticipa una idea fundamental:

$$

\text{el significado lógico de una fórmula con variables depende también de su dominio}.

$$

---

### 1.8 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-t1-c03-x0021}
**Ejemplo — La misma escritura y dos dominios**
:::

Consideremos:

$$
x^2=4.
$$

#### Primer contexto — valores enteros

Declaramos:

> $x$ puede tomar valores enteros.

Probemos tres sustituciones.

##### Sustitución 1

$$
x=2.
$$

Entonces $2^2=4$, que es verdadera.

##### Sustitución 2

$$
x=-2.
$$

Entonces $(-2)^2=4$, que también es verdadera.

##### Sustitución 3

$$
x=1.
$$

Entonces $1^2=4$, que es falsa. La fórmula abierta:

$$
x^2=4
$$

puede producir proposiciones verdaderas o falsas según la sustitución.

#### Segundo contexto — valores reales

Ahora declaramos:

> $x$ puede tomar valores reales.

Las sustituciones anteriores siguen teniendo sentido.

Pero podemos considerar también valores como:

$$
x=\frac12.
$$

Obtenemos $\left(\frac12\right)^2=4$, que es falsa. La fórmula escrita no cambió.

Cambió el dominio de valores permitidos.

#### Qué debemos aprender del ejemplo

Hay que distinguir:

1. la fórmula:
   $$
   x^2=4;
   $$
2. la variable:
   $$
   x;
   $$
3. el dominio declarado;
4. la sustitución concreta;
5. la proposición resultante;
6. su valor de verdad.

La fórmula abierta es el patrón. La sustitución concreta produce una proposición.

El dominio determina qué sustituciones están disponibles.

---
## Ejercicios

### Proposición o fórmula abierta {#apm-t1-c03-e0135}
Clasifica cada expresión como **proposición** o **fórmula abierta**.

#### a)

$$
5+3=8
$$

#### b)

$$
x+3=8
$$

#### c)

$$
(-2)^2=4
$$

#### d)

$$
y^2=16
$$

#### Solución


#### a)

$$
5+3=8
$$

es una proposición.

Todos los valores están determinados y la afirmación es verdadera.

#### b)

$$
x+3=8
$$

es una fórmula abierta.

Su valor depende todavía del valor asignado a $x$.

#### c)

$$
(-2)^2=4
$$

es una proposición.

Todos los valores están fijados y la proposición es verdadera.

#### d)

$$
y^2=16
$$

es una fórmula abierta.

Su valor de verdad depende del valor que ocupe el lugar de $y$.

---

### No hay todavía un único valor de verdad {#apm-t1-c03-e0136}
Explica por qué:

$$
x+1=4
$$

no tiene todavía un único valor de verdad mientras no hayamos fijado $x$.

#### Solución


Podemos hacer sustituciones diferentes.

Si:

$$
x=3,
$$

obtenemos:

$$
3+1=4,
$$

que es verdadera.

Si:

$$
x=2,
$$

obtenemos:

$$
2+1=4,
$$

que es falsa.

Por tanto, la escritura:

$$
x+1=4
$$

puede producir proposiciones con valores de verdad distintos.

Mientras no hayamos fijado $x$, la fórmula sigue abierta y no posee un único valor de verdad determinado.

---

### ¿Qué valores están permitidos? {#apm-t1-c03-e0137}
Compara los siguientes dos contextos para la fórmula:

$$
2x=3.
$$

#### Contexto A

$x$ puede tomar valores enteros.

#### Contexto B

$x$ puede tomar valores racionales.

Responde:

#### a)

¿Es $x=1$ una sustitución permitida en ambos contextos?

#### b)

¿Es $x=\frac32$ una sustitución permitida en ambos contextos?

#### c)

¿Qué muestra la comparación acerca del dominio?

#### Solución


#### a)

Sí.

El número:

$$
1
$$

es un valor permitido tanto cuando trabajamos con enteros como cuando trabajamos con racionales.

#### b)

No.

El valor:

$$
\frac32
$$

no es entero, pero sí es racional.

Por tanto, es admisible en el contexto B, pero no en el contexto A.

#### c)

El dominio determina qué valores pueden sustituir legítimamente a la variable.

La fórmula escrita:

$$
2x=3
$$

es la misma en ambos contextos, pero el repertorio de sustituciones permitidas cambia con el dominio.

---

### Por qué debemos declarar el dominio {#apm-t1-c03-e0138}
Considera:

$$
x^2=2.
$$

Explica por qué una discusión rigurosa debe indicar qué tipo de valores puede tomar $x$.

#### Solución


Sin un dominio declarado no sabemos qué sustituciones están permitidas.

Por ejemplo, si trabajamos con enteros, valores como:

$$
1,\quad -1,\quad 2
$$

son admisibles, pero otros valores no enteros no lo son.

Si trabajamos con números reales, el repertorio de sustituciones permitidas es más amplio.

Por tanto, declarar el dominio elimina una ambigüedad esencial: determina qué objetos pueden ocupar el lugar de $x$.

La fórmula:

$$
x^2=2
$$

no cambia gráficamente, pero la discusión matemática sí cambia según el dominio fijado.

---

### El dominio puede cambiar lo que encontramos {#apm-t1-c03-e0139}
Estudia:

$$
2x=1
$$

en los dos contextos siguientes.

#### Contexto A

$x$ puede tomar valores enteros.

#### Contexto B

$x$ puede tomar valores racionales.

#### a)

¿Encuentras en el contexto A una sustitución que produzca una proposición verdadera?

#### b)

¿Encuentras en el contexto B una sustitución que produzca una proposición verdadera?

#### c)

¿Qué enseña el ejemplo?

#### Solución


#### a)

No.

Si $x$ debe ser entero, no hay una sustitución entera que haga verdadera:

$$
2x=1.
$$

#### b)

Sí.

En el dominio de los racionales podemos tomar:

$$
x=\frac12.
$$

Entonces:

$$
2\cdot\frac12=1,
$$

que es verdadera.

#### c)

El ejemplo muestra que el dominio puede cambiar el comportamiento que observamos al considerar las sustituciones permitidas.

La fórmula escrita es la misma, pero los valores disponibles para la variable no son los mismos.

---

### Análisis completo de una fórmula abierta {#apm-t1-c03-e0140}
Considera:

$$
x^2-1=0
$$

y declara que $x$ puede tomar valores enteros.

#### a)

¿Cuál es la variable?

#### b)

¿Cuál es el dominio declarado?

#### c)

Sustituye $x=1$ y determina el valor de verdad de la proposición obtenida.

#### d)

Sustituye $x=0$ y determina el valor de verdad.

#### e)

Sustituye $x=-1$ y determina el valor de verdad.

#### f)

Explica por qué la expresión inicial sigue siendo una fórmula abierta antes de realizar una sustitución concreta.

#### Solución


#### a)

La variable es:

$$
x.
$$

#### b)

El dominio declarado es el de los números enteros.

#### c)

Si:

$$
x=1,
$$

obtenemos:

$$
1^2-1=0.
$$

Como:

$$
1-1=0,
$$

la proposición es verdadera.

#### d)

Si:

$$
x=0,
$$

obtenemos:

$$
0^2-1=0,
$$

es decir:

$$
-1=0,
$$

que es falsa.

#### e)

Si:

$$
x=-1,
$$

obtenemos:

$$
(-1)^2-1=0.
$$

Como:

$$
1-1=0,
$$

la proposición es verdadera.

#### f)

Antes de realizar una sustitución, el valor de verdad depende todavía del valor que ocupe el lugar de $x$.

Distintas sustituciones producen proposiciones verdaderas o falsas.

Por tanto:

$$
x^2-1=0
$$

es una fórmula abierta en el contexto considerado.

---

## Hacia la sección siguiente

En lugar de repetir continuamente:

> «la fórmula $x+2=5$»

queremos poder darle un nombre y hacer visible de qué variables depende.

La siguiente sección introducirá escrituras como: $P(x)$ y $R(x,y)$, y estudiará con precisión qué ocurre cuando sustituimos una, varias o todas sus variables.

## §2. Predicados y sustitución

En la sección anterior vimos expresiones como: $x+2=5$ y $x^2=4$.

Las llamamos **fórmulas abiertas** porque todavía contienen una o más variables no fijadas por el contexto ni reemplazadas mediante una sustitución.

Ahora queremos poder hablar de esas fórmulas de manera más cómoda.

En lugar de repetir continuamente:

> «la fórmula $x+2=5$»,

podemos darle un nombre. Por ejemplo, escribimos:

$$
P(x):\quad x+2=5.
$$

La letra $P$ nombra el patrón lógico que estamos estudiando, y la escritura:

$$
P(x)
$$

nos recuerda que ese patrón depende del valor de:

$$
x.
$$

Si reemplazamos $x$ por un valor concreto, obtenemos una afirmación concreta.

Por ejemplo, $P(3):\quad 3+2=5$, que es verdadera.

En cambio, $P(4):\quad 4+2=5$, es falsa. La notación nos permite separar con claridad:

$$
\boxed{
\text{el patrón}
\qquad\text{de}\qquad
\text{cada sustitución concreta}.
}
$$

---

### 2.1 Dar nombre a una condición

Consideremos $x^2=9$. Podemos escribir $P(x):\quad x^2=9$. Leeremos:

> «$P(x)$ es la condición $x^2=9$».

o, de manera equivalente:

> «$P(x)$ expresa que $x^2=9$».

No estamos agregando contenido nuevo. La fórmula sigue siendo:

$$
x^2=9.
$$

La notación:

$$
P(x)
$$

solo nos permite referirnos a ella de manera breve y hacer visible que depende de $x$.

::: {.ma-block .ma-definicion #apm-t1-c03-d0027}
**Definición — Predicado**

Un **predicado** es una fórmula abierta considerada como una condición acerca de una o más variables.

Escribiremos, por ejemplo:

$$
P(x),
\qquad
R(x,y),
$$

para indicar de qué variables depende la fórmula.
:::

En este capítulo la escritura $P(x)$ expresa **dependencia lógica**.

Todavía no estamos definiendo formalmente $P$ como una función.

---

### 2.2 Predicado y fórmula abierta

Los términos **fórmula abierta** y **predicado** están muy próximos, pero destacan aspectos distintos.

Cuando decimos:

> «$x^2=9$ es una fórmula abierta»,

subrayamos que todavía contiene una variable no fijada y que, en esta etapa, no constituye por sí sola una proposición.

Cuando escribimos:

$$
P(x):\quad x^2=9,
$$

y hablamos del predicado $P(x)$, destacamos la condición que esa fórmula expresa acerca de $x$.

Así:

$$
\boxed{
\text{«fórmula abierta» describe su estado lógico;}
\quad
\text{«predicado» destaca la condición expresada.}
}
$$

No necesitamos convertir esta diferencia en dos objetos matemáticos distintos.

Se trata de dos maneras de mirar la misma clase de expresiones.

---

### 2.3 Sustituir en un predicado de una variable

Sea, en el dominio de los enteros:

$$
P(x):\quad x-3=4.
$$

Si sustituimos:

$$
x=7,
$$

obtenemos $P(7):\quad 7-3=4$. Esta es una proposición verdadera. Si sustituimos:

$$
x=6,
$$

obtenemos $P(6):\quad 6-3=4$, que es falsa. Podemos registrar:

$$
P(7)=\mathrm V,
$$

$$
P(6)=\mathrm F,
$$

entendiendo con esta escritura que las proposiciones obtenidas mediante esas sustituciones son, respectivamente, verdadera y falsa.

Lo importante es distinguir:

$$
P(x)
$$

de:

$$
P(7).
$$

La primera escritura conserva una variable cuyo valor puede cambiar.

La segunda ya contiene un valor concreto en su lugar.

---

### 2.4 Predicados con más de una variable

No todas las fórmulas abiertas dependen de una sola variable.

Consideremos $x<y$. Podemos escribir $R(x,y):\quad x<y$. Ahora la fórmula depende de dos valores variables. Si sustituimos:

$$
x=2,
\qquad
y=5,
$$

obtenemos $R(2,5):\quad 2<5$, que es verdadera. Si sustituimos:

$$
x=7,
\qquad
y=3,
$$

obtenemos $R(7,3):\quad 7<3$, que es falsa. La posición importa. En:

$$
R(2,5)
$$

el primer valor ocupa el lugar de $x$ y el segundo ocupa el lugar de $y$.

Por eso: $R(2,5)$ y $R(5,2)$ no tienen por qué expresar la misma proposición.

En nuestro ejemplo:

$$
R(2,5)=\mathrm V,
$$

mientras que:

$$
R(5,2)=\mathrm F.
$$

---

### 2.5 Sustitución parcial

Supongamos nuevamente:

$$
R(x,y):\quad x<y.
$$

¿Qué ocurre si sustituimos solo una de las dos variables?

Por ejemplo, reemplazamos:

$$
x=2.
$$

Obtenemos $R(2,y):\quad 2<y$. Esta expresión **sigue siendo una fórmula abierta**, porque el valor de $y$ todavía puede cambiar.

Si después sustituimos:

$$
y=5,
$$

obtenemos $R(2,5):\quad 2<5$, que ya es una proposición verdadera. Podemos distinguir, por tanto:

#### Sustitución parcial

Se reemplaza alguna variable, pero queda al menos otra todavía variable.

Ejemplo:

$$
R(x,y)
\longrightarrow
R(2,y).
$$

#### Sustitución completa

Se reemplazan todas las variables de las que depende la fórmula.

Ejemplo:

$$
R(x,y)
\longrightarrow
R(2,5).
$$

En este último caso obtenemos una proposición. Así:

$$

\text{sustituir algunas variables puede dejar la fórmula abierta;}
\quad
\text{sustituirlas todas produce una proposición}.

$$

---

### 2.6 No confundir el nombre con el contenido

Supongamos $P(x):\quad x+1=6$. La letra $P$ no es la variable que estamos sustituyendo.

La variable es $x$ Y la fórmula que hemos nombrado mediante $P(x)$ es:

$$
x+1=6.
$$

Por tanto, hay que distinguir tres niveles:

1. el nombre del predicado:
   $$
   P;
   $$
2. la escritura que muestra su dependencia:
   $$
   P(x);
   $$
3. la condición concreta:
   $$
   x+1=6.
   $$

Después de sustituir:

$$
x=5,
$$

obtenemos $P(5):\quad 5+1=6$ No hemos «reemplazado $P$ por $5$». Hemos reemplazado la variable $x$ por $5$ dentro de la condición nombrada por $P$.

---

### 2.7 El dominio sigue siendo parte del contexto

Dar un nombre a un predicado no elimina la necesidad de declarar el dominio.

Consideremos $P(x):\quad 2x=1$. Si el dominio es el de los enteros, entonces $P\left(\frac12\right)$ no corresponde a una sustitución permitida en esa discusión.

Si el dominio es el de los racionales, en cambio, esa sustitución sí está permitida, y produce $2\cdot\frac12=1$, que es verdadera.

La notación:

$$
P(x)
$$

no contiene por sí sola toda la información semántica.

Debemos conservar el dominio fijado por el contexto.

---

### 2.8 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-t1-c03-x0022}
**Ejemplo — Predicados de una y dos variables**
:::

Trabajaremos con valores enteros. Definimos: $P(x):\quad x+2=5$, y $R(x,y):\quad x<y$.

#### Parte A — El predicado $P(x)$

Si sustituimos:

$$
x=3,
$$

obtenemos $P(3):\quad 3+2=5$, que es verdadera. Si sustituimos:

$$
x=1,
$$

obtenemos $P(1):\quad 1+2=5$, que es falsa. Así:

$$
P(3)=\mathrm V,
\qquad
P(1)=\mathrm F.
$$

#### Parte B — El predicado $R(x,y)$

Consideremos $R(x,y):\quad x<y$. Si sustituimos ambos valores:

$$
x=2,
\qquad
y=7,
$$

obtenemos $R(2,7):\quad 2<7$, que es verdadera.

Pero si invertimos las sustituciones $R(7,2):\quad 7<2$, obtenemos una proposición falsa.

#### Parte C — Una sustitución parcial

Sustituyamos únicamente:

$$
x=2.
$$

Obtenemos $R(2,y):\quad 2<y$. Todavía no podemos asignar a esta fórmula un único valor de verdad, porque $y$ sigue variando.

Por ejemplo, $R(2,5):\quad 2<5$ es verdadera, mientras que:

$$
R(2,1):\quad 2<1
$$

es falsa.

#### Conclusión

El ejemplo muestra tres situaciones distintas:

$$
P(x)
$$

depende de una variable;

$$
R(x,y)
$$

depende de dos; y:

$$
R(2,y)
$$

ha recibido una sustitución parcial, pero todavía permanece abierta.

---
## Ejercicios

### Nombrar una fórmula abierta {#apm-t1-c03-e0141}
En el dominio de los enteros, considera:

$$
x^2=16.
$$

#### a)

Escribe esta fórmula usando un nombre de predicado $P(x)$.

#### b)

Escribe $P(4)$ y determina su valor de verdad.

#### c)

Escribe $P(3)$ y determina su valor de verdad.

#### Solución


#### a)

Podemos definir:

$$
P(x):\quad x^2=16.
$$

#### b)

Sustituyendo:

$$
x=4,
$$

obtenemos:

$$
P(4):\quad 4^2=16.
$$

Como:

$$
16=16,
$$

la proposición es verdadera.

#### c)

Sustituyendo:

$$
x=3,
$$

obtenemos:

$$
P(3):\quad 3^2=16.
$$

Como:

$$
9\ne16,
$$

la proposición es falsa.

---

### Sustituir en uno y dos lugares {#apm-t1-c03-e0142}
Trabajamos con valores enteros.

Sea:

$$
P(x):\quad x-1=2,
$$

y:

$$
R(x,y):\quad x+y=10.
$$

Determina el valor de verdad de:

#### a)

$$
P(3)
$$

#### b)

$$
P(5)
$$

#### c)

$$
R(4,6)
$$

#### d)

$$
R(7,1)
$$

#### Solución


#### a)

$$
P(3):\quad 3-1=2.
$$

Es verdadera.

#### b)

$$
P(5):\quad 5-1=2.
$$

Como:

$$
4\ne2,
$$

es falsa.

#### c)

$$
R(4,6):\quad 4+6=10.
$$

Es verdadera.

#### d)

$$
R(7,1):\quad 7+1=10.
$$

Como:

$$
8\ne10,
$$

es falsa.

---

### Predicado, variable y sustitución {#apm-t1-c03-e0143}
Considera:

$$
Q(x):\quad 3x=12.
$$

Explica qué papel cumple cada una de las siguientes expresiones:

#### a)

$$
Q
$$

#### b)

$$
x
$$

#### c)

$$
Q(x)
$$

#### d)

$$
Q(4)
$$

#### Solución


#### a)

$Q$ es el nombre que hemos dado al predicado.

#### b)

$x$ es la variable de la que depende la fórmula.

#### c)

$Q(x)$ muestra que el predicado depende de $x$ y representa aquí la condición:

$$
3x=12.
$$

#### d)

$Q(4)$ es la proposición obtenida después de sustituir:

$$
x=4.
$$

En efecto:

$$
Q(4):\quad 3\cdot4=12,
$$

que es verdadera.

---

### Por qué no llamamos función a $P$ {#apm-t1-c03-e0144}
En este capítulo escribimos:

$$
P(x):\quad x^2=4.
$$

Explica por qué, en esta etapa del tratado, no necesitamos definir formalmente $P$ como una función.

#### Solución


La notación:

$$
P(x)
$$

se está utilizando para indicar que la condición:

$$
x^2=4
$$

depende del valor de $x$.

Para los objetivos actuales basta saber:

- cuál es la variable;
- cuál es el dominio;
- qué condición expresa la fórmula;
- qué ocurre al realizar sustituciones.

La teoría formal de funciones todavía no ha sido desarrollada en el tratado.

Por tanto, interpretar $P(x)$ como notación de **dependencia lógica** es suficiente y evita utilizar prematuramente un concepto que aún no hemos construido.

---

### Una sustitución parcial {#apm-t1-c03-e0145}
Trabajamos con valores enteros.

Sea:

$$
R(x,y):\quad x-y=2.
$$

#### a)

Sustituye $x=5$ y escribe la fórmula resultante.

#### b)

Explica por qué la fórmula obtenida sigue abierta.

#### c)

Sustituye después $y=3$ y determina el valor de verdad.

#### d)

Sustituye, en cambio, $y=1$ y determina el valor de verdad.

#### Solución


#### a)

Al sustituir:

$$
x=5,
$$

obtenemos:

$$
R(5,y):\quad 5-y=2.
$$

#### b)

La expresión sigue abierta porque $y$ todavía puede tomar distintos valores.

#### c)

Si:

$$
y=3,
$$

obtenemos:

$$
R(5,3):\quad 5-3=2,
$$

que es verdadera.

#### d)

Si:

$$
y=1,
$$

obtenemos:

$$
R(5,1):\quad 5-1=2.
$$

Como:

$$
4\ne2,
$$

la proposición es falsa.

---

### Construir y analizar un predicado de dos variables {#apm-t1-c03-e0146}
Trabajamos con valores enteros.

Construye un predicado:

$$
S(x,y)
$$

que exprese:

> «La suma de $x$ e $y$ es igual a $6$».

Después:

#### a)

escribe la fórmula correspondiente;

#### b)

evalúa $S(1,5)$;

#### c)

evalúa $S(4,1)$;

#### d)

escribe la expresión obtenida al sustituir solo $x=2$;

#### e)

explica si la expresión del apartado d) es una proposición o una fórmula abierta.

#### Solución


#### a)

Podemos definir:

$$
S(x,y):\quad x+y=6.
$$

#### b)

$$
S(1,5):\quad 1+5=6.
$$

Es verdadera.

#### c)

$$
S(4,1):\quad 4+1=6.
$$

Como:

$$
5\ne6,
$$

es falsa.

#### d)

Al sustituir solo:

$$
x=2,
$$

obtenemos:

$$
S(2,y):\quad 2+y=6.
$$

#### e)

Sigue siendo una fórmula abierta porque $y$ todavía puede tomar valores diferentes.

Por ejemplo:

$$
S(2,4)
$$

es verdadera, mientras que:

$$
S(2,3)
$$

es falsa.

---

## Síntesis

Una fórmula abierta puede recibir un nombre:

$$
P(x),
\qquad
R(x,y),
$$

que hace visible de qué variables depende. Llamamos **predicado** a esa fórmula abierta considerada como una condición acerca de sus variables.

La notación no convierte todavía al predicado en una función formal.

Además distinguimos:

$$

\text{sustitución parcial}
\neq
\text{sustitución completa}.

$$

En:

$$
R(x,y)
\longrightarrow
R(2,y),
$$

la fórmula sigue abierta. En:

$$
R(x,y)
\longrightarrow
R(2,5),
$$

todas las variables han sido reemplazadas y obtenemos una proposición.

La trayectoria general es:

$$

\text{predicado}
\longrightarrow
\text{sustitución}
\longrightarrow
\text{fórmula todavía abierta o proposición}.

$$

Pero sustituir valores uno por uno no es la única manera de obtener una proposición a partir de una fórmula abierta.

Existe otra operación lógica mucho más poderosa: afirmar que la condición se cumple **sin excepciones** dentro del dominio.

## Hacia la sección siguiente

Hasta ahora hemos preguntado:

> «¿Qué ocurre si sustituimos $x$ por este valor concreto?»

La pregunta siguiente será diferente:

> «¿Qué ocurre si queremos afirmar que la condición se cumple para cada valor permitido de $x$?»

Para expresarlo introduciremos nuestro primer cuantificador:

## §3. El cuantificador universal

Hasta ahora hemos convertido una fórmula abierta en una proposición mediante **sustitución**.

Si:

$$
P(x):\quad x+0=x,
$$

podemos sustituir un valor concreto:

$$
P(7):\quad 7+0=7.
$$

Pero muchas afirmaciones matemáticas no hablan de un valor particular.

Dicen algo más fuerte. Por ejemplo:

> «Todo número entero permanece igual al sumarle cero».

Aquí no estamos eligiendo primero:

$$
x=7,
$$

ni:

$$
x=-3,
$$

ni ningún otro valor particular. Queremos afirmar que la condición $x+0=x$ se cumple **para cada valor permitido de $x$**.

Para expresar esa idea necesitamos una nueva operación lógica.

---

### 3.1 De un caso particular a todos los casos

Declaramos que el dominio es el de los números enteros y consideramos:

$$
P(x):\quad x+0=x.
$$

Cada sustitución concreta produce una proposición:

$$
P(5):\quad 5+0=5,
$$

$$
P(-2):\quad -2+0=-2,
$$

$$
P(0):\quad 0+0=0.
$$

Pero la afirmación que queremos escribir no es ninguna de esas por separado.

Queremos abarcar **todos los valores del dominio de una sola vez**.

Escribimos $\forall x\,P(x)$. El símbolo $\forall$ se lee:

> «para todo»

o:

> «para cada».

Así, $\forall x\,P(x)$ se lee:

> «Para todo $x$, se cumple $P(x)$».

En nuestro ejemplo:

$$
\forall x\,(x+0=x)
$$

se lee:

> «Para todo valor entero de $x$, $x+0=x$».

---

### 3.2 El cuantificador universal

::: {.ma-block .ma-definicion #apm-t1-c03-d0028}
**Definición — Cuantificador universal**

El **cuantificador universal** es el símbolo:

$$
\forall.
$$

Si $P(x)$ es un predicado y el dominio de $x$ está fijado, la fórmula:

$$
\forall x\,P(x)
$$

afirma que $P(x)$ es verdadera para **cada valor permitido de $x$**.
:::

En este capítulo el dominio debe estar declarado explícitamente o fijado de manera inequívoca por el contexto.

Por ejemplo:

> En el dominio de los enteros,

podemos escribir $\forall x\,(x+0=x)$. El cuantificador $\forall x$ nos dice cómo debe interpretarse la variable $x$ en la fórmula que sigue:

> no elegimos un caso particular; exigimos que la condición se cumpla en todos los casos permitidos.

---

### 3.3 Una afirmación universal es una proposición

Recordemos:

$$
P(x):\quad x+0=x.
$$

Mientras escribimos solamente:

$$
P(x),
$$

la fórmula permanece abierta respecto de $x$.

En cambio, $\forall x\,P(x)$ ya no espera que elijamos un valor concreto de $x$.

La propia fórmula afirma qué debe ocurrir cuando $x$ recorre todo el dominio.

Así obtenemos una nueva trayectoria:

$$
\boxed{
\text{fórmula abierta}
\longrightarrow
\text{cuantificación universal}
\longrightarrow
\text{proposición}.
}
$$

Esto es conceptualmente distinto de la sustitución:

$$
P(x)
\longrightarrow
P(7).
$$

En una sustitución fijamos **un valor particular**. Con el cuantificador universal afirmamos algo acerca de **cada valor permitido**.

---

### 3.4 Qué exige realmente «para todo»

Consideremos ahora, en el dominio de los enteros:

$$
Q(x):\quad x^2=x.
$$

La afirmación universal sería:

$$
\forall x\,Q(x),
$$

es decir:

$$
\forall x\,(x^2=x).
$$

Probemos algunos valores. Para:

$$
x=0,
$$

obtenemos $0^2=0$, que es verdadera. Para:

$$
x=1,
$$

obtenemos $1^2=1$, que también es verdadera.

Pero para:

$$
x=2,
$$

obtenemos $2^2=2$, es decir:

$$
4=2,
$$

que es falsa. Por tanto:

$$
\forall x\,(x^2=x)
$$

es falsa en el dominio de los enteros. La razón es fundamental:

$$
\boxed{
\text{una afirmación universal no admite excepciones}.
}
$$

Para que:

$$
\forall x\,P(x)
$$

sea verdadera, cada valor permitido debe hacer verdadera la condición.

Un solo valor permitido que produzca una proposición falsa basta para que la afirmación universal sea falsa.

---

### 3.5 Contraejemplo

Supongamos que alguien afirma, en el dominio de los enteros:

$$
\forall x\,(x^2=x).
$$

El valor $x=2$ produce:

$$
2^2=2,
$$

que es falso. Ese valor concreto refuta la afirmación universal.

En este contexto llamaremos **contraejemplo** a un valor permitido del dominio para el cual la condición universal falla.

Así, $x=2$ es un contraejemplo a:

$$
\forall x\,(x^2=x).
$$

La idea es sencilla:

$$

\text{para refutar «todos», basta encontrar uno que falle}.

$$

Por ahora utilizaremos el contraejemplo únicamente con este sentido semántico.

Más adelante estudiaremos de manera sistemática cómo se organizan las demostraciones matemáticas.

---

### 3.6 Ver algunos casos no basta para afirmar «todos»

Hay una asimetría importante. Para refutar:

$$
\forall x\,P(x),
$$

un solo contraejemplo basta.

Pero verificar varios casos favorables no establece por sí solo una afirmación universal.

Supongamos, por ejemplo, que el dominio es el de los números enteros y examinamos una condición $P(x)$.

Podemos comprobar:

$$
P(0),
\qquad
P(1),
\qquad
P(2),
\qquad
P(3),
$$

y descubrir que todas son verdaderas. Eso solo nos informa acerca de esos cuatro valores.

Si el dominio contiene otros valores, todavía no hemos determinado qué ocurre con ellos.

Por tanto:

$$
\boxed{
\text{muchos ejemplos favorables no equivalen a «para todo».}
}
$$

Esta observación será esencial en toda la matemática posterior.

---

### 3.7 El dominio forma parte de la afirmación

Consideremos la misma condición:

$$
P(x):\quad x^2=x.
$$

#### Primer dominio

Supongamos que el dominio contiene únicamente los valores:

$$
0
\qquad\text{y}\qquad
1.
$$

Entonces, $0^2=0$ y $1^2=1$ Como esos son todos los valores permitidos, la afirmación:

$$
\forall x\,P(x)
$$

es verdadera en ese dominio.

#### Segundo dominio

Ahora supongamos que el dominio es el de los enteros.

El valor $x=2$ está permitido y produce:

$$
2^2=2,
$$

que es falsa. Por tanto, la misma escritura:

$$
\forall x\,P(x)
$$

es falsa en este segundo dominio. Así vemos nuevamente:

$$
\boxed{
\text{el dominio es parte esencial del significado de una fórmula cuantificada}.
}
$$

---

### 3.8 Leer antes de calcular

Ante una fórmula como:

$$
\forall x\,(x^2+1>0),
$$

no conviene comenzar sustituyendo valores al azar. Primero debemos leer su estructura.

Si el dominio ha sido fijado como el de los números reales, la fórmula dice:

> «Para todo número real $x$, $x^2+1$ es mayor que cero».

La palabra decisiva es:

> **todo**.

Eso nos indica que la afirmación no pregunta por un valor particular.

Describe una condición que debe cumplirse sin excepciones en el dominio.

Este hábito de lectura será cada vez más importante cuando las fórmulas contengan varios conectivos y, más adelante, varios cuantificadores.

---

### 3.9 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-t1-c03-x0023}
**Ejemplo — Una afirmación universal y una excepción**
:::

Trabajaremos con valores enteros. Definimos:

$$
P(x):\quad x+0=x.
$$

La fórmula $\forall x\,P(x)$ afirma:

> «Para todo valor entero de $x$, $x+0=x$».

La identidad al sumar cero se cumple para cada entero, de modo que la proposición universal es verdadera.

Ahora consideremos $Q(x):\quad x^2=x$. La fórmula $\forall x\,Q(x)$ afirma:

> «Para todo valor entero de $x$, $x^2=x$».

Los valores: $x=0$ y $x=1$ satisfacen la condición.

Pero:

$$
x=2
$$

produce $2^2=2$, es decir:

$$
4=2.
$$

La proposición obtenida es falsa. Por tanto:

$$
\forall x\,Q(x)
$$

es falsa. El valor $x=2$ es un contraejemplo.

#### Comparación

Tenemos así dos afirmaciones universales $\forall x\,(x+0=x)$, verdadera en el dominio de los enteros, y:

$$
\forall x\,(x^2=x),
$$

falsa en ese mismo dominio. La diferencia no está en el símbolo $\forall$ Está en si la condición que sigue al cuantificador se cumple efectivamente para **cada** valor del dominio.

---
## Ejercicios

### Escribir «para todo» {#apm-t1-c03-e0147}
En el dominio de los enteros, sea:

$$
P(x):\quad x+0=x.
$$

Escribe simbólicamente:

> «Para todo valor de $x$, se cumple $P(x)$».

Después escribe la fórmula sin utilizar el nombre $P$.

#### Solución


Con el nombre del predicado escribimos:

$$
\boxed{
\forall x\,P(x).
}
$$

Como:

$$
P(x):\quad x+0=x,
$$

podemos escribir directamente:

$$
\boxed{
\forall x\,(x+0=x).
}
$$

Ambas escrituras expresan la misma afirmación universal en el dominio declarado.

---

### Qué exige un universal {#apm-t1-c03-e0148}
Explica con tus propias palabras qué significa:

$$
\forall x\,P(x)
$$

cuando el dominio de $x$ ya ha sido declarado.

#### Solución


La fórmula afirma que:

$$
P(x)
$$

es verdadera para cada valor permitido de $x$.

No basta con que la condición sea verdadera para algunos valores, para muchos valores o para los primeros valores que probemos.

Debe cumplirse sin excepciones dentro del dominio.

---

### Verificar varios casos no basta {#apm-t1-c03-e0149}
El dominio es el de los enteros.

Supón que hemos comprobado que:

$$
P(0),\quad
P(1),\quad
P(2),\quad
P(3)
$$

son verdaderas.

¿Podemos concluir únicamente a partir de esas cuatro comprobaciones que:

$$
\forall x\,P(x)
$$

es verdadera?

Justifica.

#### Solución


No.

Las cuatro comprobaciones solo determinan qué ocurre para:

$$
0,\quad1,\quad2,\quad3.
$$

El dominio de los enteros contiene también otros valores.

Mientras no tengamos una razón que abarque todos los valores permitidos, sigue abierta la posibilidad de que alguno de los valores no examinados haga falsa la condición.

Por tanto, verificar algunos casos favorables no basta para concluir:

$$
\forall x\,P(x).
$$

---

### Refutar mediante un contraejemplo {#apm-t1-c03-e0150}
En el dominio de los enteros, considera:

$$
\forall x\,(x^2=x).
$$

Refuta la afirmación mediante un contraejemplo.

#### Solución


Tomemos:

$$
x=2.
$$

Entonces:

$$
x^2=x
$$

se convierte en:

$$
2^2=2,
$$

es decir:

$$
4=2,
$$

que es falsa.

Por tanto:

$$
x=2
$$

es un contraejemplo y la afirmación:

$$
\boxed{
\forall x\,(x^2=x)
}
$$

es falsa en el dominio de los enteros.

---

### La misma fórmula en dos dominios {#apm-t1-c03-e0151}
Considera:

$$
P(x):\quad x^2=x.
$$

#### Contexto A

El dominio contiene únicamente:

$$
0
\qquad\text{y}\qquad
1.
$$

#### Contexto B

El dominio es el de los enteros.

Determina el valor de verdad de:

$$
\forall x\,P(x)
$$

en cada contexto.

#### Solución


#### Contexto A

Los únicos valores permitidos son:

$$
0
\qquad\text{y}\qquad
1.
$$

Para:

$$
x=0,
$$

tenemos:

$$
0^2=0.
$$

Para:

$$
x=1,
$$

tenemos:

$$
1^2=1.
$$

La condición se cumple para cada valor permitido.

Por tanto:

$$
\boxed{
\forall x\,P(x)
}
$$

es verdadera en el contexto A.

#### Contexto B

Ahora el dominio es el de los enteros.

El valor:

$$
x=2
$$

está permitido, pero:

$$
2^2=2
$$

es falsa.

Por tanto:

$$
\boxed{
\forall x\,P(x)
}
$$

es falsa en el contexto B.

La comparación muestra que el dominio forma parte del significado de la afirmación cuantificada.

---

### Formular, leer y decidir {#apm-t1-c03-e0152}
Trabajamos con valores enteros y definimos:

$$
R(x):\quad x^2+1>0.
$$

#### a)

Escribe simbólicamente la afirmación:

> «Para todo valor entero de $x$, $x^2+1>0$».

#### b)

Lee en prosa la fórmula obtenida.

#### c)

Decide si la afirmación es verdadera o falsa y justifica tu respuesta.

#### Solución


#### a)

Escribimos:

$$
\boxed{
\forall x\,(x^2+1>0).
}
$$

#### b)

Se lee:

> «Para todo valor entero de $x$, $x^2+1$ es mayor que cero».

#### c)

Para cualquier entero $x$, su cuadrado satisface:

$$
x^2\ge0.
$$

Por tanto:

$$
x^2+1\ge1,
$$

y, en particular:

$$
x^2+1>0.
$$

La condición se cumple para cada valor entero permitido.

Así:

$$
\boxed{
\forall x\,(x^2+1>0)
}
$$

es verdadera.

---

## Síntesis

Hasta ahora disponíamos de:

$$
P(x)
\longrightarrow
P(a),
$$

es decir, una fórmula abierta que se convierte en proposición al sustituir un valor concreto.

Ahora añadimos una segunda posibilidad:

$$
P(x)
\longrightarrow
\forall x\,P(x).
$$

La diferencia es esencial. En:

$$
P(a),
$$

hablamos de un valor particular. En:

$$
\forall x\,P(x),
$$

afirmamos que la condición se cumple para cada valor permitido del dominio.

Por eso:

$$

\forall
\quad\text{significa una exigencia sin excepciones}.

$$

También aprendimos que:

- el dominio debe estar fijado;
- algunos casos favorables no bastan para establecer una afirmación universal;
- un solo contraejemplo basta para refutarla.

Pero «para todo» no es la única manera de convertir una fórmula abierta en una proposición.

A veces queremos afirmar algo mucho menos exigente:

> que la condición se cumpla para **al menos un valor**.

## Hacia la sección siguiente

La próxima sección introducirá el segundo cuantificador fundamental. En lugar de exigir que una condición se cumpla para cada valor del dominio, podremos afirmar que hay algún valor permitido que la satisface.

## §4. El cuantificador existencial

En la sección anterior introdujimos una manera de cerrar una fórmula abierta:

$$
P(x)
\longrightarrow
\forall x\,P(x).
$$

La afirmación universal exige que la condición se cumpla para **cada** valor permitido del dominio.

Pero muchas afirmaciones matemáticas tienen una exigencia diferente. Consideremos, en el dominio de los enteros:

$$
P(x):\quad x^2=9.
$$

No es cierto que:

$$
\forall x\,P(x),
$$

porque, por ejemplo:

$$
P(0):\quad 0^2=9
$$

es falsa.

Sin embargo, sí hay valores enteros que hacen verdadera la condición: $P(3):\quad 3^2=9$, y $P(-3):\quad (-3)^2=9$.

Por tanto, aunque la condición no se cumple para todos los enteros, podemos afirmar algo importante:

> hay al menos un valor permitido de $x$ que la satisface.

Para expresar esta idea utilizaremos nuestro segundo cuantificador fundamental.

---

### 4.1 «Existe» significa «hay al menos uno»

Escribimos $\exists x\,P(x)$. El símbolo $\exists$ se lee:

> «existe»

o:

> «hay al menos un».

Así, $\exists x\,P(x)$ se lee:

> «Existe un valor de $x$ para el cual se cumple $P(x)$».

En nuestro ejemplo:

$$
\exists x\,(x^2=9)
$$

se lee:

> «Existe un entero $x$ cuyo cuadrado es igual a $9$».

La afirmación es verdadera porque podemos encontrar valores permitidos que hacen verdadera la condición.

Por ejemplo:

$$
x=3.
$$

---

### 4.2 El cuantificador existencial

::: {.ma-block .ma-definicion #apm-t1-c03-d0029}
**Definición — Cuantificador existencial**

El **cuantificador existencial** es el símbolo:

$$
\exists.
$$

Si $P(x)$ es un predicado y el dominio de $x$ está fijado, la fórmula:

$$
\exists x\,P(x)
$$

afirma que $P(x)$ es verdadera para **al menos un valor permitido de $x$**.
:::

El dominio sigue siendo indispensable. La expresión $\exists x\,P(x)$ no nos dice por sí sola qué objetos pueden ocupar el lugar de $x$.

Esa información debe estar declarada por el contexto.

---

### 4.3 Una tercera manera de pasar de fórmula abierta a proposición

Ya conocemos tres situaciones.

#### Sustitución concreta

$$
P(x)
\longrightarrow
P(3).
$$

Hablamos de un valor particular.

#### Cuantificación universal

$$
P(x)
\longrightarrow
\forall x\,P(x).
$$

Afirmamos que la condición se cumple para cada valor permitido.

#### Cuantificación existencial

$$
P(x)
\longrightarrow
\exists x\,P(x).
$$

Afirmamos que la condición se cumple para al menos un valor permitido.

Podemos resumir:

$$
\boxed{
\begin{array}{ccl}
P(3) &:& \text{este valor concreto funciona},\\[4pt]
\forall x\,P(x) &:& \text{todos los valores funcionan},\\[4pt]
\exists x\,P(x) &:& \text{al menos un valor funciona}.
\end{array}
}
$$

Las tres afirmaciones tienen exigencias lógicas distintas.

---

### 4.4 Testigos de una afirmación existencial

Consideremos $\exists x\,(x^2=9)$ en el dominio de los enteros. El valor $x=3$ hace verdadera la condición:

$$
3^2=9.
$$

Por tanto, $3$ confirma concretamente que la afirmación existencial es verdadera.

Llamaremos **testigo** a un valor permitido que hace verdadera la condición de una afirmación existencial.

Así, $3$ es un testigo de:

$$
\exists x\,(x^2=9).
$$

También:

$$
-3
$$

es otro testigo, porque:

$$
(-3)^2=9.
$$

Esto muestra algo importante:

$$

\text{un testigo basta para confirmar una afirmación existencial concreta}.

$$

No necesitamos encontrar todos los valores que funcionan. Basta uno.

---

### 4.5 Existencia no significa unicidad

La afirmación:

$$
\exists x\,P(x)
$$

significa:

> «hay al menos un valor de $x$ que satisface $P(x)$».

No significa:

> «hay exactamente un valor».

Volvamos a $P(x):\quad x^2=9$ en los enteros. Tenemos dos testigos: $x=3$ y $x=-3$.

Por tanto:

$$
\exists x\,P(x)
$$

es verdadera.

Pero la condición no tiene un único valor que la satisfaga.

Esta distinción debe quedar fijada desde ahora:

$$

\text{«existe»}
\neq
\text{«existe exactamente uno».}

$$

Más adelante estudiaremos cómo expresar simbólicamente la existencia única.

---

### 4.6 Una afirmación existencial también puede ser falsa

El cuantificador existencial no convierte automáticamente una condición en una afirmación verdadera.

Consideremos, en el dominio de los enteros:

$$
Q(x):\quad 2x=1.
$$

La fórmula $\exists x\,Q(x)$ afirma:

> «Existe un entero $x$ tal que $2x=1$».

Pero ningún entero satisface esa ecuación. Por tanto:

$$
\exists x\,(2x=1)
$$

es falsa en el dominio de los enteros. La exigencia existencial es menos fuerte que la universal, pero sigue siendo una exigencia:

$$
\boxed{
\text{debe haber al menos un valor permitido que funcione}.
}
$$

---

### 4.7 El dominio puede cambiar una afirmación existencial

Consideremos nuevamente:

$$
Q(x):\quad 2x=1.
$$

#### Dominio de los enteros

No hay un entero que satisfaga:

$$
2x=1.
$$

Por tanto:

$$
\exists x\,(2x=1)
$$

es falsa.

#### Dominio de los racionales

Ahora el valor $x=\frac12$ está permitido. Y:

$$
2\cdot\frac12=1.
$$

Por tanto:

$$
\exists x\,(2x=1)
$$

es verdadera en este segundo dominio. La fórmula escrita es la misma.

El dominio cambia qué valores pueden servir como testigos.

Así:

$$
\boxed{
\text{el valor de verdad de una afirmación existencial puede depender del dominio}.
}
$$

---

### 4.8 Universal y existencial no dicen lo mismo

Consideremos, en el dominio de los enteros:

$$
P(x):\quad x^2=9.
$$

La afirmación:

$$
\forall x\,P(x)
$$

es falsa, porque no todos los enteros tienen cuadrado igual a $9$.

En cambio, $\exists x\,P(x)$ es verdadera, porque:

$$
x=3
$$

es un testigo. Por tanto: $\forall x\,P(x)$ y $\exists x\,P(x)$ no son dos maneras de escribir la misma idea.

El universal exige:

> todos.

El existencial exige:

> al menos uno.

Podemos visualizar la diferencia:

$$
\boxed{
\forall:\ \text{ninguna excepción}
\qquad
\exists:\ \text{al menos un caso favorable}.
}
$$

---

### 4.9 Encontrar muchos casos tampoco cambia el significado de «existe»

Si encontramos varios testigos, una afirmación existencial sigue diciendo solamente:

> «hay al menos uno».

Por ejemplo, en los enteros:

$$
\exists x\,(x^2=9)
$$

tiene al menos los testigos:

$$
3,\qquad -3.
$$

El hecho de que encontremos dos testigos no cambia el significado del cuantificador.

La afirmación existencial no lleva incorporado un conteo exacto de cuántos valores funcionan.

Por eso debemos resistir dos errores opuestos:

- creer que «existe» significa «existe exactamente uno»;
- creer que para justificar una existencia concreta debemos encontrar todos los valores que funcionan.

Ninguno de los dos es correcto.

---

### 4.10 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-t1-c03-x0024}
**Ejemplo — Existencia, testigos y ausencia de unicidad**
:::

Trabajaremos con valores enteros y definimos:

$$
P(x):\quad x^2=9.
$$

Consideremos $\exists x\,P(x)$. La fórmula afirma:

> «Existe al menos un entero $x$ cuyo cuadrado es igual a $9$».

Tomemos $x=3$. Entonces $P(3):\quad 3^2=9$, que es verdadera. Por tanto:

$$
x=3
$$

es un testigo y la afirmación existencial es verdadera.

Pero también podemos tomar:

$$
x=-3.
$$

Entonces $P(-3):\quad (-3)^2=9$, que también es verdadera. Así, tenemos al menos dos testigos:

$$
3
\qquad\text{y}\qquad
-3.
$$

#### Qué demuestra esto

Primero:

$$
\exists x\,(x^2=9)
$$

es verdadera en los enteros. Segundo, la afirmación existencial no dice que haya un único valor que funcione.

Por tanto:

$$
\boxed{
\text{existencia}
\quad\text{y}\quad
\text{unicidad}
}
$$

son cuestiones distintas.

---
## Ejercicios

### Escribir «existe» {#apm-t1-c03-e0153}
En el dominio de los enteros, sea:

$$
P(x):\quad x+2=7.
$$

Escribe simbólicamente:

> «Existe un valor de $x$ para el cual se cumple $P(x)$».

Después escribe la fórmula sin utilizar el nombre $P$.

#### Solución


Con el nombre del predicado:

$$
\boxed{
\exists x\,P(x).
}
$$

Como:

$$
P(x):\quad x+2=7,
$$

podemos escribir:

$$
\boxed{
\exists x\,(x+2=7).
}
$$

La afirmación es verdadera, pues:

$$
x=5
$$

es un testigo.

---

### «Existe» significa «al menos uno» {#apm-t1-c03-e0154}
Explica por qué:

$$
\exists x\,P(x)
$$

no afirma que exista exactamente un valor que satisfaga $P(x)$.

#### Solución


El cuantificador existencial exige solamente que haya **al menos un** valor permitido para el cual:

$$
P(x)
$$

sea verdadera.

Puede haber un solo valor, dos, diez o muchos más.

Por ejemplo, en los enteros:

$$
\exists x\,(x^2=9)
$$

es verdadera y tiene al menos dos testigos:

$$
3
\qquad\text{y}\qquad
-3.
$$

Por tanto, existencia y unicidad son afirmaciones diferentes.

---

### Por qué basta un testigo {#apm-t1-c03-e0155}
Trabajamos con valores enteros.

Considera:

$$
\exists x\,(x^2=16).
$$

Explica por qué exhibir:

$$
x=4
$$

es suficiente para determinar que la afirmación existencial es verdadera.

#### Solución


La afirmación:

$$
\exists x\,(x^2=16)
$$

exige que haya al menos un entero cuyo cuadrado sea $16$.

Tomamos:

$$
x=4.
$$

Entonces:

$$
4^2=16.
$$

Hemos encontrado un valor permitido que hace verdadera la condición.

Por tanto, la exigencia existencial ya está satisfecha.

No necesitamos encontrar todos los valores que funcionen para concluir que la afirmación es verdadera.

---

### Más de un testigo {#apm-t1-c03-e0156}
Trabajamos con valores enteros.

Considera:

$$
P(x):\quad x^2=25.
$$

#### a)

Encuentra un testigo de:

$$
\exists x\,P(x).
$$

#### b)

Encuentra un segundo testigo distinto.

#### c)

¿Qué muestra esto acerca de la relación entre existencia y unicidad?

#### Solución


#### a)

Podemos tomar:

$$
x=5.
$$

Entonces:

$$
5^2=25.
$$

Por tanto, $5$ es un testigo.

#### b)

También:

$$
x=-5
$$

satisface:

$$
(-5)^2=25.
$$

Así, $-5$ es un segundo testigo.

#### c)

La afirmación existencial es verdadera, pero hay más de un valor que satisface la condición.

Por tanto:

$$
\boxed{
\text{existencia no implica unicidad}.
}
$$

---

### Formular una afirmación existencial {#apm-t1-c03-e0157}
Trabajamos con valores enteros.

Escribe simbólicamente:

> «Existe un entero cuyo triple es igual a $12$».

Después encuentra un testigo y determina el valor de verdad de la afirmación.

#### Solución


Podemos escribir:

$$
\boxed{
\exists x\,(3x=12).
}
$$

Tomamos:

$$
x=4.
$$

Entonces:

$$
3\cdot4=12.
$$

Por tanto, $4$ es un testigo y la afirmación existencial es verdadera.

---

### La misma existencia en dos dominios {#apm-t1-c03-e0158}
Considera:

$$
P(x):\quad 2x=3.
$$

#### Contexto A

El dominio es el de los enteros.

#### Contexto B

El dominio es el de los racionales.

#### a)

Determina el valor de verdad de:

$$
\exists x\,P(x)
$$

en el contexto A.

#### b)

Determina el valor de verdad de la misma fórmula en el contexto B.

#### c)

Explica qué papel desempeña el dominio.

#### Solución


#### a)

En los enteros, la ecuación:

$$
2x=3
$$

no tiene una solución entera.

Por tanto:

$$
\boxed{
\exists x\,(2x=3)
}
$$

es falsa en el contexto A.

#### b)

En los racionales podemos tomar:

$$
x=\frac32.
$$

Entonces:

$$
2\cdot\frac32=3.
$$

Por tanto:

$$
\boxed{
\exists x\,(2x=3)
}
$$

es verdadera en el contexto B.

#### c)

El dominio determina qué valores pueden actuar como testigos.

La fórmula es la misma, pero un valor permitido en un dominio puede no estar permitido en otro.

Por eso el dominio forma parte del significado de la afirmación existencial.

---

## Síntesis

Ahora disponemos de los dos cuantificadores fundamentales del capítulo.

El universal:

$$
\forall x\,P(x)
$$

afirma:

> «$P(x)$ se cumple para cada valor permitido».

El existencial:

$$
\exists x\,P(x)
$$

afirma:

> «$P(x)$ se cumple para al menos un valor permitido».

La diferencia puede condensarse así:

$$

\forall:\ \text{todos}
\qquad
\exists:\ \text{al menos uno}.

$$

También introdujimos la idea de **testigo**:

$$

\text{un testigo es un valor permitido que hace verdadera la condición existencial}.

$$

Y fijamos una distinción que será esencial:

$$

\text{existencia}
\neq
\text{unicidad}.

$$

Ya podemos leer afirmaciones con:

$$
\forall
\qquad\text{y}\qquad
\exists.
$$

El siguiente problema será aprender a **negarlas correctamente**.

## Hacia la sección siguiente

¿Qué significa decir que no es verdad que todos los valores satisfacen una condición?

¿Y qué significa decir que no existe ningún valor que la satisfaga?

La negación hará que los dos cuantificadores se relacionen entre sí.

## §5. Negar cuantificadores

Ya sabemos leer:

$$
\forall x\,P(x)
$$

como:

> «$P(x)$ se cumple para cada valor permitido de $x$»,

y:

$$
\exists x\,P(x)
$$

como:

> «$P(x)$ se cumple para al menos un valor permitido de $x$».

Ahora queremos responder una pregunta decisiva:

> ¿qué significa negar correctamente una afirmación cuantificada?

Consideremos primero:

$$
\forall x\,P(x).
$$

Negarla significa afirmar:

> «No es verdad que $P(x)$ se cumpla para todos los valores».

Pero eso no significa que $P(x)$ falle para todos.

Basta que falle para **al menos uno**. Por tanto:

$$
\neg\forall x\,P(x)
$$

expresa la misma condición lógica que:

$$
\exists x\,\neg P(x).
$$

El universal se convierte en existencial y la negación alcanza finalmente a la condición.

Algo dual ocurre con:

$$
\exists x\,P(x).
$$

Negar que exista al menos un valor que haga verdadera $P(x)$ significa que **cada** valor permitido hace falsa $P(x)$.

Así, $\neg\exists x\,P(x)$ expresa lo mismo que:

$$
\forall x\,\neg P(x).
$$

Estas dos equivalencias serán las primeras leyes formales de lógica cuantificacional del capítulo.

---

### 5.1 Negar «todos»

Trabajemos con valores enteros y consideremos:

$$
P(x):\quad x>0.
$$

La afirmación:

$$
\forall x\,P(x)
$$

dice:

> «Todo entero es positivo».

Su negación es:

> «No todo entero es positivo».

¿Qué tendría que ocurrir para que esa negación fuera verdadera?

Basta que exista un entero que **no** sea positivo.

Por ejemplo, $x=0$ hace falsa la condición:

$$
x>0.
$$

Por tanto, decir:

$$
\neg\forall x\,P(x)
$$

equivale a decir:

$$
\exists x\,\neg P(x).
$$

En prosa:

> «No todos cumplen $P$»

equivale a:

> «Hay al menos uno que no cumple $P$».

La estructura es:

$$
\boxed{
\neg\forall
\quad\longrightarrow\quad
\exists\neg.
}
$$

---

### 5.2 «No todos» no significa «ninguno»

Esta distinción merece atención especial. Consideremos un dominio formado por los valores:

$$
1
\qquad\text{y}\qquad
2,
$$

y definamos:

$$
P(x):\quad x\text{ es par}.
$$

La afirmación:

> «No todos los valores del dominio son pares»

es verdadera, porque:

$$
1
$$

no es par. En símbolos:

$$
\neg\forall x\,P(x).
$$

Pero la afirmación:

> «Todos los valores del dominio no son pares»

es falsa, porque:

$$
2
$$

sí es par. En símbolos:

$$
\forall x\,\neg P(x).
$$

Por tanto:

$$
\boxed{
\neg\forall x\,P(x)
\not\equiv
\forall x\,\neg P(x).
}
$$

La negación de «todos» no produce «ninguno». Produce:

> «al menos uno no».

---

### 5.3 Negar «existe»

Consideremos ahora, en el dominio de los enteros:

$$
Q(x):\quad x^2=-1.
$$

La afirmación:

$$
\exists x\,Q(x)
$$

dice:

> «Existe un entero cuyo cuadrado es $-1$».

Negarla significa:

> «No existe ningún entero cuyo cuadrado sea $-1$».

¿Qué expresa esto acerca de cada entero?

Expresa que, cualquiera sea el valor permitido de $x$:

$$
x^2\ne-1.
$$

Por tanto:

$$
\neg\exists x\,Q(x)
$$

equivale a:

$$
\forall x\,\neg Q(x).
$$

En prosa:

> «No existe ninguno que cumpla $Q$»

equivale a:

> «Todos incumplen $Q$».

La estructura es:

$$
\boxed{
\neg\exists
\quad\longrightarrow\quad
\forall\neg.
}
$$

---

### 5.4 Las dos leyes

Ya podemos formular el resultado general.

::: {.ma-block .ma-enunciado #apm-t1-c03-p0007}
**Proposición — Leyes de negación de cuantificadores**

Sea $P(x)$ un predicado sobre un dominio no vacío previamente fijado. Entonces:

$$
\boxed{
\neg\forall x\,P(x)
\equiv
\exists x\,\neg P(x)
}
$$

y:

$$
\boxed{
\neg\exists x\,P(x)
\equiv
\forall x\,\neg P(x).
}
$$
:::

#### Demostración de la primera equivalencia

Consideremos $\neg\forall x\,P(x)$. Esta fórmula afirma que no es verdad que:

$$
P(x)
$$

se cumpla para cada valor permitido. Que una afirmación universal falle significa precisamente que hay al menos un valor permitido para el cual la condición falla.

Existe un valor de $x$ para el cual:

$$
\neg P(x)
$$

es verdadera. Eso es exactamente lo que afirma:

$$
\exists x\,\neg P(x).
$$

Así:

$$
\boxed{
\neg\forall x\,P(x)
\equiv
\exists x\,\neg P(x).
}
$$

#### Demostración de la segunda equivalencia

Consideremos $\neg\exists x\,P(x)$. Esta fórmula afirma que no es verdad que haya al menos un valor permitido para el cual:

$$
P(x)
$$

sea verdadera. Por tanto, ningún valor permitido hace verdadera $P(x)$.

Dicho de otro modo, para cada valor permitido de $x$:

$$
P(x)
$$

es falsa, es decir:

$$
\neg P(x)
$$

es verdadera. Eso es exactamente lo que afirma:

$$
\forall x\,\neg P(x).
$$

Por tanto:

$$
\boxed{
\neg\exists x\,P(x)
\equiv
\forall x\,\neg P(x).
}
$$

Quedan demostradas las dos leyes.

---

### 5.5 Una manera de recordarlas

No conviene aprender las leyes como un simple intercambio de símbolos.

Conviene reconstruir su significado.

#### Si negamos un universal

$$
\neg\forall x\,P(x),
$$

preguntamos:

> «¿Qué hace que falle la afirmación de que todos cumplen $P$?»

Respuesta:

> «Que haya al menos uno que no cumpla $P$».

Por eso:

$$
\neg\forall x\,P(x)
\equiv
\exists x\,\neg P(x).
$$

#### Si negamos un existencial

$$
\neg\exists x\,P(x),
$$

preguntamos:

> «¿Qué significa que no haya ni un solo valor que cumpla $P$?»

Respuesta:

> «Que todos los valores incumplan $P$».

Por eso:

$$
\neg\exists x\,P(x)
\equiv
\forall x\,\neg P(x).
$$

Podemos condensarlo así:

$$

\text{al negar un cuantificador, cambia su tipo y la negación continúa hacia la condición}.

$$

---

### 5.6 La negación debe llegar hasta la condición

Consideremos $\neg\forall x\,(x^2=x)$ No debemos detenernos en:

> «No todos los enteros satisfacen $x^2=x$».

Esa frase es correcta, pero podemos expresar la negación en una forma equivalente más informativa.

Por [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007):

$$
\neg\forall x\,(x^2=x)
\equiv
\exists x\,\neg(x^2=x).
$$

Negar la igualdad $x^2=x$ produce:

$$
x^2\ne x.
$$

Por tanto:

$$
\boxed{
\neg\forall x\,(x^2=x)
\equiv
\exists x\,(x^2\ne x).
}
$$

En prosa:

> «No todos los enteros satisfacen $x^2=x$»

equivale a:

> «Existe al menos un entero cuyo cuadrado no es igual a él mismo».

Por ejemplo, $x=2$ confirma la segunda afirmación.

---

### 5.7 Negar una existencia concreta

Consideremos, en el dominio de los enteros:

$$
\neg\exists x\,(2x=1).
$$

Por [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007):

$$
\neg\exists x\,(2x=1)
\equiv
\forall x\,\neg(2x=1).
$$

Negando la igualdad $\neg(2x=1)$ obtenemos:

$$
2x\ne1.
$$

Así:

$$
\boxed{
\neg\exists x\,(2x=1)
\equiv
\forall x\,(2x\ne1).
}
$$

Las dos fórmulas expresan la misma idea:

> «No existe un entero que satisfaga $2x=1$»

y:

> «Todo entero incumple $2x=1$».

---

### 5.8 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-t1-c03-x0025}
**Ejemplo — De «no todos» a «existe una excepción»**
:::

Trabajaremos con valores enteros y consideramos:

$$
P(x):\quad x^2=x.
$$

La afirmación universal:

$$
\forall x\,P(x)
$$

dice:

> «Todo entero satisface $x^2=x$».

Queremos negarla.

#### Paso 1 — Negar la afirmación completa

Escribimos $\neg\forall x\,P(x)$. En prosa:

> «No todos los enteros satisfacen $P$».

#### Paso 2 — Aplicar [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007)

Tenemos:

$$
\neg\forall x\,P(x)
\equiv
\exists x\,\neg P(x).
$$

#### Paso 3 — Recuperar la condición concreta

Como:

$$
P(x):\quad x^2=x,
$$

obtenemos $\exists x\,\neg(x^2=x)$. Por tanto:

$$

\exists x\,(x^2\ne x).

$$

#### Paso 4 — Volver a la prosa

La negación correcta es:

> «Existe al menos un entero cuyo cuadrado no es igual a él mismo».

#### Paso 5 — Comprobar el significado

Tomemos $x=2$. Entonces $2^2\ne2$. Por tanto, $2$ es un valor que hace verdadera la negación de la afirmación universal.

El ejemplo muestra que:

$$

\text{negar «todos»}
\quad\text{no produce}\quad
\text{«ninguno»,}

$$

sino:

$$

\text{«existe al menos una excepción».}

$$

---
## Ejercicios

### Negar un universal {#apm-t1-c03-e0159}
Trabajamos con valores enteros.

Niega correctamente:

$$
\forall x\,(x+0=x).
$$

Expresa el resultado en símbolos y en prosa.

#### Solución


Aplicamos [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007):

$$
\neg\forall x\,(x+0=x)
\equiv
\exists x\,\neg(x+0=x).
$$

Negando la igualdad:

$$
\neg(x+0=x)
$$

obtenemos:

$$
x+0\ne x.
$$

Por tanto, la negación es:

$$
\boxed{
\exists x\,(x+0\ne x).
}
$$

En prosa:

> «Existe al menos un entero para el cual $x+0\ne x$».

Esta negación es falsa, porque sumar cero no cambia ningún entero.

Eso es coherente con que la afirmación universal original sea verdadera.

---

### Negar un existencial {#apm-t1-c03-e0160}
Trabajamos con valores enteros.

Niega correctamente:

$$
\exists x\,(2x=1).
$$

Expresa el resultado en símbolos y en prosa.

#### Solución


Aplicamos [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007):

$$
\neg\exists x\,(2x=1)
\equiv
\forall x\,\neg(2x=1).
$$

Negando la igualdad:

$$
\neg(2x=1)
$$

obtenemos:

$$
2x\ne1.
$$

Por tanto:

$$
\boxed{
\forall x\,(2x\ne1).
}
$$

En prosa:

> «Para todo entero $x$, $2x$ es distinto de $1$».

Equivalentemente:

> «Ningún entero satisface $2x=1$».

---

### «No todos» frente a «todos no» {#apm-t1-c03-e0161}
El dominio contiene únicamente los valores:

$$
1
\qquad\text{y}\qquad
2.
$$

Sea:

$$
P(x):\quad x\text{ es par}.
$$

Compara:

$$
\neg\forall x\,P(x)
$$

con:

$$
\forall x\,\neg P(x).
$$

Determina el valor de verdad de cada fórmula y explica por qué no son equivalentes.

#### Solución


Primero:

$$
\neg\forall x\,P(x)
$$

significa:

> «No todos los valores del dominio son pares».

Esto es verdadero, porque:

$$
1
$$

no es par.

Ahora:

$$
\forall x\,\neg P(x)
$$

significa:

> «Todos los valores del dominio no son pares».

Esto es falso, porque:

$$
2
$$

sí es par.

Por tanto:

$$
\neg\forall x\,P(x)
$$

es verdadera, mientras que:

$$
\forall x\,\neg P(x)
$$

es falsa.

Así:

$$
\boxed{
\neg\forall x\,P(x)
\not\equiv
\forall x\,\neg P(x).
}
$$

---

### Justificar la primera ley {#apm-t1-c03-e0162}
Explica, sin limitarte a repetir la fórmula, por qué:

$$
\neg\forall x\,P(x)
\equiv
\exists x\,\neg P(x).
$$

#### Solución


La afirmación:

$$
\forall x\,P(x)
$$

exige que $P(x)$ sea verdadera para cada valor permitido.

Negarla significa que esa exigencia universal falla.

Para que falle, debe haber al menos un valor permitido para el cual:

$$
P(x)
$$

sea falsa.

Decir que hay al menos un valor para el cual $P(x)$ es falsa equivale a decir que hay al menos un valor para el cual:

$$
\neg P(x)
$$

es verdadera.

Eso es exactamente:

$$
\exists x\,\neg P(x).
$$

Por tanto:

$$
\boxed{
\neg\forall x\,P(x)
\equiv
\exists x\,\neg P(x).
}
$$

---

### Justificar la segunda ley {#apm-t1-c03-e0163}
Explica por qué:

$$
\neg\exists x\,P(x)
\equiv
\forall x\,\neg P(x).
$$

#### Solución


La afirmación:

$$
\exists x\,P(x)
$$

dice que hay al menos un valor permitido que hace verdadera $P(x)$.

Negarla significa que no hay ningún valor permitido con esa propiedad.

Por tanto, cada valor permitido hace falsa $P(x)$.

Decir que $P(x)$ es falsa para cada valor equivale a decir que:

$$
\neg P(x)
$$

es verdadera para cada valor.

Eso es:

$$
\forall x\,\neg P(x).
$$

Por tanto:

$$
\boxed{
\neg\exists x\,P(x)
\equiv
\forall x\,\neg P(x).
}
$$

---

### De la prosa a la negación y de vuelta {#apm-t1-c03-e0164}
Trabajamos con valores enteros.

Considera la afirmación:

> «Todo entero satisface $x^2=x$».

#### a)

Escríbela simbólicamente.

#### b)

Escribe su negación.

#### c)

Transforma la negación mediante [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007).

#### d)

Vuelve a expresar el resultado en prosa.

#### e)

Exhibe un valor que confirme que la negación es verdadera.

#### Solución


#### a)

La afirmación universal es:

$$
\forall x\,(x^2=x).
$$

#### b)

Su negación es:

$$
\neg\forall x\,(x^2=x).
$$

#### c)

Por [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007):

$$
\neg\forall x\,(x^2=x)
\equiv
\exists x\,\neg(x^2=x).
$$

Negando la igualdad:

$$
\boxed{
\exists x\,(x^2\ne x).
}
$$

#### d)

En prosa:

> «Existe al menos un entero cuyo cuadrado no es igual a él mismo».

#### e)

Podemos tomar:

$$
x=2.
$$

Entonces:

$$
2^2\ne2.
$$

Por tanto, la negación es verdadera.

---

## Síntesis

Los cuantificadores universal y existencial están conectados por la negación.

Las dos leyes fundamentales son:

$$

\neg\forall x\,P(x)
\equiv
\exists x\,\neg P(x)

$$

y:

$$

\neg\exists x\,P(x)
\equiv
\forall x\,\neg P(x).

$$

La lectura semántica es:

$$

\text{«no todos»}
\longleftrightarrow
\text{«al menos uno no»}

$$

y:

$$

\text{«no existe ninguno que cumpla»}
\longleftrightarrow
\text{«todos incumplen».}

$$

La regla práctica puede reconstruirse así:

$$

\text{negar cuantificador}
=
\text{cambiar }\forall\leftrightarrow\exists
+
\text{continuar la negación hacia la condición}.

$$

Pero las fórmulas cuantificadas pueden ser más complejas que: $\forall x\,P(x)$ o $\exists x\,P(x)$ Para leer correctamente expresiones mayores necesitaremos saber con precisión **qué parte de una fórmula controla cada cuantificador** y qué apariciones de las variables dependen de él.

## Hacia la sección siguiente

Consideremos:

$$
\forall x\,(P(x)\Rightarrow Q(x,y)).
$$

El símbolo $\forall x$ actúa sobre una parte determinada de la fórmula.

Además, las apariciones de $x$ y $y$ no tienen el mismo comportamiento lógico.

La próxima sección introducirá las herramientas necesarias para describir esa diferencia.

## §6. Alcance, variables ligadas y variables libres

Hasta ahora hemos escrito fórmulas como: $\forall x\,P(x)$ y $\exists x\,P(x)$.

En estos casos es fácil ver qué hace el cuantificador: actúa sobre la condición $P(x)$ y nos dice cómo debe interpretarse la variable $x$.

Pero consideremos una fórmula algo mayor:

$$
\forall x\,(P(x)\Rightarrow Q(x,y)).
$$

Aquí aparecen dos letras variables:

$$
x
\qquad\text{y}\qquad
y.
$$

El cuantificador $\forall x$ controla las apariciones de $x$ que están dentro de la fórmula que sigue.

Pero no controla la aparición de $y$. Por tanto, aunque $x$ haya quedado cuantificada, la expresión completa sigue dependiendo todavía de $y$.

Para describir esta diferencia necesitamos tres ideas nuevas:

- **alcance**;
- **aparición ligada**;
- **aparición libre**.

Y una cuarta idea nos permitirá reconocer cuándo una fórmula ya no depende de ningún valor variable que haya quedado sin controlar:

- **fórmula cerrada**.

---

### 6.1 El alcance de un cuantificador

Consideremos:

$$
\forall x\,(P(x)\Rightarrow Q(x,y)).
$$

La parte $P(x)\Rightarrow Q(x,y)$ es la fórmula sobre la que actúa:

$$
\forall x.
$$

Diremos que esa parte constituye el **alcance** del cuantificador.

::: {.ma-block .ma-definicion #apm-t1-c03-d0030}
**Definición — Alcance de un cuantificador**

El **alcance** de un cuantificador es la parte de la fórmula sobre la que ese cuantificador actúa.
:::

En APM escribiremos paréntesis explícitos siempre que ayuden a hacer visible ese alcance.

Así:

$$
\forall x\,(P(x)\Rightarrow Q(x,y))
$$

deja claro que el cuantificador universal actúa sobre toda la implicación:

$$
P(x)\Rightarrow Q(x,y).
$$

Los paréntesis no son decoración. Nos dicen qué parte de la fórmula debe leerse bajo el cuantificador.

---

### 6.2 Por qué el alcance importa

Comparemos $\forall x\,(P(x)\lor Q(x))$ con $(\forall x\,P(x))\lor Q(x)$. En la primera fórmula, el cuantificador $\forall x$ actúa sobre:

$$
P(x)\lor Q(x).
$$

Las dos apariciones de $x$ están dentro de su alcance.

En la segunda fórmula, el cuantificador actúa solamente sobre:

$$
P(x).
$$

La aparición de $x$ en:

$$
Q(x)
$$

queda fuera de su alcance. Las dos fórmulas no tienen la misma estructura lógica.

Esto muestra que no basta con ver el símbolo $\forall x$ También debemos preguntar:

> **¿hasta dónde llega?**

---

### 6.3 Apariciones ligadas

Volvamos a:

$$
\forall x\,(P(x)\Rightarrow Q(x,y)).
$$

Las dos apariciones de:

$$
x
$$

están dentro del alcance del cuantificador:

$$
\forall x.
$$

Diremos que esas apariciones están **ligadas** por el cuantificador.

::: {.ma-block .ma-definicion #apm-t1-c03-d0031}
**Definición — Aparición ligada**

Una aparición de una variable está **ligada** si se encuentra dentro del alcance de un cuantificador que cuantifica esa misma variable.
:::

Así, en:

$$
\forall x\,(P(x)\Rightarrow Q(x,y)),
$$

las apariciones de $x$ en: $P(x)$ y $Q(x,y)$ están ligadas por:

$$
\forall x.
$$

La palabra importante es **aparición**. No conviene decir simplemente:

> «$x$ es una variable ligada».

En fórmulas más grandes, una misma letra puede tener una aparición ligada en una parte y otra aparición libre en otra.

---

### 6.4 Apariciones libres

En la fórmula:

$$
\forall x\,(P(x)\Rightarrow Q(x,y)),
$$

la aparición de:

$$
y
$$

no está bajo ningún cuantificador que cuantifique $y$. Diremos que esa aparición es **libre**.

::: {.ma-block .ma-definicion #apm-t1-c03-d0032}
**Definición — Aparición libre**

Una aparición de una variable está **libre** si no se encuentra dentro del alcance de ningún cuantificador que cuantifique esa misma variable.
:::

Así:

$$
\forall x\,(P(x)\Rightarrow Q(x,y))
$$

contiene:

- apariciones ligadas de $x$;
- una aparición libre de $y$.

La fórmula ya no depende de una elección posterior de $x$.

Pero todavía depende del valor que ocupe el lugar de $y$.

---

### 6.5 Una misma letra puede aparecer libre y ligada

Consideremos $(\forall x\,P(x))\lor Q(x)$. La primera aparición de $x$, dentro de:

$$
P(x),
$$

está bajo el alcance de:

$$
\forall x.
$$

Por tanto, esa aparición está ligada.

Pero la aparición de $x$ en:

$$
Q(x)
$$

está fuera de ese alcance. Esa segunda aparición está libre.

En una sola fórmula encontramos entonces:

$$
\boxed{
\text{una aparición ligada de }x
\quad\text{y}\quad
\text{una aparición libre de }x.
}
$$

Esta es la razón por la que nuestra terminología habla de **apariciones** libres o ligadas.

El símbolo utilizado puede ser el mismo. Lo que cambia es su posición respecto del alcance de los cuantificadores.

---

### 6.6 Fórmulas que todavía permanecen abiertas

Consideremos $\forall x\,(x+y=0)$. El cuantificador $\forall x$ liga la aparición de $x$.

Pero la aparición de:

$$
y
$$

permanece libre. Por tanto, la fórmula completa continúa dependiendo de $y$.

Si fijamos:

$$
y=1,
$$

obtenemos $\forall x\,(x+1=0)$. Si fijamos:

$$
y=-1,
$$

obtenemos $\forall x\,(x-1=0)$. La fórmula original no expresaba todavía una proposición independiente de valores variables sin fijar, porque $y$ seguía libre.

La cuantificación de una variable no cierra necesariamente todas las demás.

---

### 6.7 Fórmulas cerradas

Ahora consideremos:

$$
\forall y\,\forall x\,(P(x)\Rightarrow Q(x,y)).
$$

Las apariciones de $x$ están ligadas por:

$$
\forall x,
$$

y las apariciones de $y$ están ligadas por:

$$
\forall y.
$$

No queda ninguna aparición libre.

::: {.ma-block .ma-definicion #apm-t1-c03-d0033}
**Definición — Fórmula cerrada**

Una **fórmula cerrada** es una fórmula que no contiene ninguna aparición libre de variables.
:::

Con esta terminología podemos precisar la caracterización provisional de §1:

$$
\boxed{
\text{una fórmula es abierta}
\iff
\text{contiene al menos una aparición libre de variable}.
}
$$

Esta es una condición **sintáctica**. No exige que el valor de verdad cambie efectivamente al cambiar una asignación. Por ejemplo, $x=x$ sigue siendo una fórmula abierta mientras la aparición de $x$ permanezca libre, aunque resulte verdadera para cualquier valor permitido de $x$.

Una fórmula cerrada ya no espera que fijemos desde fuera el valor de ninguna variable que permanezca libre.

En un dominio y una interpretación previamente fijados, puede evaluarse como una proposición.

Por ejemplo, $\forall x\,(x+0=x)$ es una fórmula cerrada.

En cambio, $\forall x\,(x+y=0)$ no lo es, porque $y$ aparece libre.

---

### 6.8 Cerrar una fórmula

Podemos partir de:

$$
R(x,y).
$$

Las apariciones de:

$$
x
\qquad\text{y}\qquad
y
$$

están libres. Si escribimos:

$$
\forall x\,R(x,y),
$$

las apariciones de $x$ quedan ligadas, pero las de $y$ permanecen libres.

Si después escribimos:

$$
\forall y\,\forall x\,R(x,y),
$$

también las apariciones de $y$ quedan ligadas. La fórmula resultante queda cerrada.

Esquemáticamente:

$$
\boxed{
R(x,y)
\longrightarrow
\forall x\,R(x,y)
\longrightarrow
\forall y\,\forall x\,R(x,y).
}
$$

En cada paso podemos preguntar:

> ¿queda alguna aparición libre?

Esa pregunta permite reconocer si la fórmula sigue abierta o ya está cerrada.

---

### 6.9 Los paréntesis controlan la lectura

Consideremos nuevamente:

$$
\forall x\,(P(x)\Rightarrow Q(x,y)).
$$

Los paréntesis indican explícitamente que el alcance de:

$$
\forall x
$$

es toda la implicación.

En cambio:

$$
(\forall x\,P(x))\Rightarrow Q(x,y)
$$

tiene otra estructura. Aquí el cuantificador actúa solamente sobre:

$$
P(x).
$$

La aparición de $x$ en:

$$
Q(x,y)
$$

queda fuera de su alcance y, por tanto, está libre.

En APM preferiremos la parentetización explícita precisamente para evitar que el lector deba adivinar hasta dónde llega un cuantificador.

---

### 6.10 No confundir «ligada» con «sustituida»

Una aparición ligada no ha sido sustituida por un valor concreto.

Comparemos $P(3)$ con $\forall x\,P(x)$. En:

$$
P(3),
$$

hemos reemplazado la variable por el valor:

$$
3.
$$

En:

$$
\forall x\,P(x),
$$

la variable sigue apareciendo como:

$$
x,
$$

pero sus apariciones están controladas por el cuantificador. Por tanto:

$$

\text{ligar una variable}
\neq
\text{sustituirla por un valor}.

$$

La sustitución elige un valor particular. La cuantificación determina cómo debe leerse la variable a lo largo de un alcance.

---

### 6.11 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-t1-c03-x0026}
**Ejemplo — Qué queda libre y qué queda ligado**
:::

Consideremos:

$$
\forall x\,(P(x)\Rightarrow Q(x,y)).
$$

#### Paso 1 — Identificar el cuantificador

Tenemos $\forall x$. Este cuantificador controla la variable:

$$
x.
$$

#### Paso 2 — Identificar su alcance

Por los paréntesis, su alcance es:

$$
P(x)\Rightarrow Q(x,y).
$$

#### Paso 3 — Examinar las apariciones de $x$

Hay una aparición de $x$ en:

$$
P(x)
$$

y otra en:

$$
Q(x,y).
$$

Ambas están dentro del alcance de:

$$
\forall x.
$$

Ambas están ligadas.

#### Paso 4 — Examinar la aparición de $y$

La aparición de:

$$
y
$$

en:

$$
Q(x,y)
$$

no está bajo ningún cuantificador que cuantifique $y$. Por tanto, está libre.

#### Paso 5 — Clasificar la fórmula

Como queda una aparición libre de $y$, la fórmula:

$$
\forall x\,(P(x)\Rightarrow Q(x,y))
$$

no está cerrada. Ahora añadamos:

$$
\forall y.
$$

Obtenemos:

$$
\forall y\,\forall x\,(P(x)\Rightarrow Q(x,y)).
$$

Las apariciones de $x$ quedan ligadas por:

$$
\forall x,
$$

y la aparición de $y$ queda ligada por:

$$
\forall y.
$$

No queda ninguna aparición libre. La nueva fórmula es cerrada.

---
## Ejercicios

### Identificar el alcance {#apm-t1-c03-e0165}
Considera:

$$
\forall x\,(P(x)\lor Q(x,y)).
$$

#### a)

¿Cuál es el cuantificador?

#### b)

¿Cuál es su alcance?

#### c)

¿Qué variable cuantifica?

#### Solución


#### a)

El cuantificador es:

$$
\forall x.
$$

#### b)

Su alcance es toda la fórmula situada dentro de los paréntesis:

$$
P(x)\lor Q(x,y).
$$

#### c)

El cuantificador cuantifica la variable:

$$
x.
$$

No cuantifica $y$.

---

### Marcar apariciones libres y ligadas {#apm-t1-c03-e0166}
Considera:

$$
\exists y\,(R(x,y)\land P(y)).
$$

Clasifica cada aparición de $x$ y de $y$ como libre o ligada.

#### Solución


El cuantificador es:

$$
\exists y,
$$

y su alcance es:

$$
R(x,y)\land P(y).
$$

Las dos apariciones de:

$$
y
$$

están dentro del alcance de un cuantificador que cuantifica $y$.

Por tanto, ambas están ligadas.

La aparición de:

$$
x
$$

no está bajo ningún cuantificador que cuantifique $x$.

Por tanto, está libre.

Así:

- $x$: una aparición libre;
- $y$: dos apariciones ligadas.

---

### La misma letra, dos situaciones {#apm-t1-c03-e0167}
Considera:

$$
(\forall x\,P(x))\land Q(x).
$$

#### a)

Clasifica la aparición de $x$ en $P(x)$.

#### b)

Clasifica la aparición de $x$ en $Q(x)$.

#### c)

Explica por qué sería impreciso decir simplemente: «$x$ es una variable ligada».

#### Solución


#### a)

La aparición de $x$ en:

$$
P(x)
$$

está dentro del alcance de:

$$
\forall x.
$$

Por tanto, está ligada.

#### b)

La aparición de $x$ en:

$$
Q(x)
$$

queda fuera del alcance de:

$$
\forall x.
$$

Por tanto, está libre.

#### c)

La misma letra:

$$
x
$$

tiene una aparición ligada y otra libre dentro de la misma fórmula.

Por eso la clasificación se aplica con precisión a **apariciones de variables**, no necesariamente a la letra considerada de manera global.

---

### ¿Abierta o cerrada? {#apm-t1-c03-e0168}
Clasifica cada fórmula como abierta o cerrada.

#### a)

$$
P(x)
$$

#### b)

$$
\forall x\,P(x)
$$

#### c)

$$
\forall x\,R(x,y)
$$

#### d)

$$
\exists y\,\forall x\,R(x,y)
$$

#### Solución


#### a)

$$
P(x)
$$

es abierta porque la aparición de $x$ está libre.

#### b)

$$
\forall x\,P(x)
$$

es cerrada porque la aparición de $x$ está ligada y no queda ninguna otra variable libre.

#### c)

$$
\forall x\,R(x,y)
$$

sigue abierta.

Las apariciones de $x$ están ligadas, pero $y$ aparece libre.

#### d)

$$
\exists y\,\forall x\,R(x,y)
$$

es cerrada.

Las apariciones de $x$ están ligadas por:

$$
\forall x,
$$

y las de $y$ por:

$$
\exists y.
$$

No queda ninguna aparición libre.

---

### Por qué los paréntesis importan {#apm-t1-c03-e0169}
Compara:

$$
\forall x\,(P(x)\Rightarrow Q(x))
$$

con:

$$
(\forall x\,P(x))\Rightarrow Q(x).
$$

Explica por qué los paréntesis cambian el estatus de la segunda aparición de $x$.

#### Solución


En:

$$
\forall x\,(P(x)\Rightarrow Q(x)),
$$

el alcance de:

$$
\forall x
$$

es toda la implicación:

$$
P(x)\Rightarrow Q(x).
$$

Por tanto, las dos apariciones de $x$ están ligadas.

En cambio, en:

$$
(\forall x\,P(x))\Rightarrow Q(x),
$$

el cuantificador:

$$
\forall x
$$

actúa únicamente sobre:

$$
P(x).
$$

La aparición de $x$ en:

$$
Q(x)
$$

queda fuera de su alcance y está libre.

Así, los paréntesis hacen visible hasta dónde actúa el cuantificador y cambian la estructura lógica de la fórmula.

---

### Análisis completo {#apm-t1-c03-e0170}
Considera:

$$
\forall x\,(P(x,y)\lor \exists z\,Q(x,z)).
$$

#### a)

¿Cuál es el alcance de $\forall x$?

#### b)

¿Cuál es el alcance de $\exists z$?

#### c)

Clasifica las apariciones de $x$, $y$ y $z$ como libres o ligadas.

#### d)

¿La fórmula es abierta o cerrada?

#### e)

Escribe una fórmula cerrada obtenida a partir de ella añadiendo un solo cuantificador.

#### Solución


#### a)

El alcance de:

$$
\forall x
$$

es:

$$
P(x,y)\lor \exists z\,Q(x,z).
$$

#### b)

El alcance de:

$$
\exists z
$$

es:

$$
Q(x,z).
$$

#### c)

Las apariciones de:

$$
x
$$

en:

$$
P(x,y)
$$

y:

$$
Q(x,z)
$$

están dentro del alcance de:

$$
\forall x.
$$

Por tanto, están ligadas.

La aparición de:

$$
z
$$

en:

$$
Q(x,z)
$$

está dentro del alcance de:

$$
\exists z.
$$

Por tanto, está ligada.

La aparición de:

$$
y
$$

en:

$$
P(x,y)
$$

no está bajo ningún cuantificador que cuantifique $y$.

Por tanto, está libre.

#### d)

La fórmula es abierta porque contiene una aparición libre de $y$.

#### e)

Podemos añadir:

$$
\forall y
$$

y obtener:

$$
\boxed{
\forall y\,\forall x\,(P(x,y)\lor \exists z\,Q(x,z)).
}
$$

Ahora las apariciones de $x$, $y$ y $z$ están ligadas.

La fórmula resultante es cerrada.

---

## Síntesis

Un cuantificador no actúa necesariamente sobre toda la expresión que vemos escrita a su derecha.

Actúa sobre un **alcance** determinado. Dentro de ese alcance podemos clasificar las apariciones de variables.

Una aparición está:

$$

\text{ligada}

$$

si queda bajo el alcance de un cuantificador que cuantifica esa misma variable.

Está:

$$

\text{libre}

$$

si no ocurre así. Por eso una misma letra puede tener apariciones con distinto estatus dentro de una misma fórmula.

Finalmente:

$$

\text{fórmula cerrada}
=
\text{fórmula sin apariciones libres de variables}.

$$

Estas nociones permiten leer con precisión fórmulas como:

$$
\forall x\,(P(x)\Rightarrow Q(x,y)),
$$

y reconocer inmediatamente que:

- las apariciones de $x$ están ligadas;
- $y$ aparece libre;
- la fórmula completa todavía está abierta.

El paso siguiente será estudiar fórmulas en las que aparecen **varios cuantificadores** y comprender por qué su orden puede cambiar radicalmente lo que afirmamos.

## Hacia la sección siguiente

Comparemos $\forall x\,\exists y\,R(x,y)$ con $\exists y\,\forall x\,R(x,y)$. Ambas fórmulas son cerradas. Ambas utilizan los mismos dos cuantificadores y el mismo predicado.

Sin embargo, no dicen lo mismo. La diferencia está en el **orden**.

## §7. Varios cuantificadores y orden

En la sección anterior aprendimos a leer fórmulas como:

$$
\forall x\,(P(x)\Rightarrow Q(x,y)).
$$

Sabemos reconocer qué apariciones de variables están ligadas, cuáles permanecen libres y cuándo una fórmula está cerrada.

Ahora aparece una dificultad nueva. Consideremos $\forall x\,\exists y\,R(x,y)$. Las dos variables están cuantificadas. La fórmula es cerrada.

Pero ¿qué afirma exactamente?

Y, sobre todo, ¿diría lo mismo si cambiáramos el orden?

$$
\exists y\,\forall x\,R(x,y).
$$

Las dos escrituras utilizan:

- el mismo predicado;
- las mismas variables;
- un cuantificador universal;
- un cuantificador existencial.

Sin embargo, en general **no expresan la misma afirmación**.

El orden de los cuantificadores puede determinar qué valores pueden ajustarse a otros y cuáles deben quedar fijados de una vez para todos los casos.

Este será el problema central de la sección.

---

### 7.1 Leer desde fuera hacia dentro

Consideremos $\forall x\,\exists y\,R(x,y)$. El cuantificador exterior es:

$$
\forall x.
$$

Por tanto, comenzamos leyendo:

> «Para todo valor permitido de $x$...»

Después aparece:

$$
\exists y.
$$

Continuamos:

> «...existe al menos un valor permitido de $y$...»

Finalmente leemos la condición:

$$
R(x,y).
$$

La lectura completa es:

> «Para todo valor permitido de $x$, existe al menos un valor permitido de $y$ para el cual se cumple $R(x,y)$».

La estructura importa. Primero se considera un valor de $x$.

Después debemos poder encontrar algún valor de $y$ que haga verdadera la condición correspondiente.

Ese valor de $y$ **puede ser distinto para distintos valores de $x$**.

---

### 7.2 Cuando la elección interior puede cambiar

Trabajemos con valores enteros y definamos:

$$
R(x,y):\quad y=x+1.
$$

Consideremos $\forall x\,\exists y\,R(x,y)$. La fórmula dice:

> «Para todo entero $x$, existe un entero $y$ tal que $y=x+1$».

Si:

$$
x=0,
$$

podemos tomar:

$$
y=1.
$$

Si:

$$
x=5,
$$

podemos tomar:

$$
y=6.
$$

Si:

$$
x=-3,
$$

podemos tomar:

$$
y=-2.
$$

El valor elegido para $y$ no tiene que ser siempre el mismo.

Puede ajustarse al valor de $x$ que estamos considerando.

Así:

$$
\boxed{
\forall x\,\exists y
\quad\text{permite que el valor elegido para }y\text{ cambie al cambiar }x.
}
$$

No estamos introduciendo todavía una estructura matemática adicional. Solo estamos describiendo el significado lógico del orden de los cuantificadores.

---

### 7.3 Invertir el orden cambia la exigencia

Consideremos ahora:

$$
\exists y\,\forall x\,R(x,y),
$$

con el mismo predicado:

$$
R(x,y):\quad y=x+1.
$$

La lectura es:

> «Existe un entero $y$ tal que, para todo entero $x$, se cumple $y=x+1$».

Ahora la situación es muy distinta. El cuantificador exterior es:

$$
\exists y.
$$

Primero debe existir **un solo valor de $y$**. Después ese mismo valor tiene que satisfacer la condición para cada valor de $x$.

No podemos cambiar $y$ cada vez que cambia $x$.

Pero ningún entero puede cumplir esa exigencia. En efecto, si proponemos un entero cualquiera $y$ y consideramos:

$$
x=y,
$$

la condición $y=x+1$ se convierte en:

$$
y=y+1,
$$

que es falsa. Por tanto:

$$
\exists y\,\forall x\,(y=x+1)
$$

es falsa sobre los enteros. Tenemos así:

$$

\forall x\,\exists y\,(y=x+1)

$$

verdadera, pero:

$$
\boxed{
\exists y\,\forall x\,(y=x+1)
}
$$

falsa. Por tanto:

$$
\boxed{
\forall x\,\exists y\,R(x,y)
\not\equiv
\exists y\,\forall x\,R(x,y)
}
$$

en general.

---

### 7.4 El orden codifica una dependencia

La diferencia anterior puede expresarse en lenguaje ordinario.

#### En:

$$
\forall x\,\exists y\,R(x,y),
$$

leemos:

> «Para cada $x$, podemos encontrar algún $y$ adecuado».

El valor de $y$ puede cambiar de un caso a otro.

#### En:

$$
\exists y\,\forall x\,R(x,y),
$$

leemos:

> «Hay un mismo $y$ que funciona para todos los valores de $x$».

La segunda afirmación exige mucho más. Podemos condensar:

$$
\boxed{
\forall x\,\exists y:
\quad
\text{un }y\text{ puede ajustarse a cada }x
}
$$

mientras que:

$$
\boxed{
\exists y\,\forall x:
\quad
\text{un solo }y\text{ debe servir para todos los }x.
}
$$

Esta diferencia aparecerá constantemente en matemáticas.

---

### 7.5 No todo cambio de orden altera el significado

El caso anterior podría sugerir que nunca podemos cambiar el orden de cuantificadores.

Eso también sería incorrecto. Consideremos $\forall x\,\forall y\,R(x,y)$. La fórmula afirma:

> «Para todo valor permitido de $x$ y para todo valor permitido de $y$, se cumple $R(x,y)$».

Si intercambiamos el orden:

$$
\forall y\,\forall x\,R(x,y),
$$

seguimos exigiendo que $R(x,y)$ sea verdadera para **cada valor de $x$ y cada valor de $y$**.

No importa cuál de los dos universales leamos primero.

Algo semejante ocurre con:

$$
\exists x\,\exists y\,R(x,y).
$$

La fórmula afirma que hay al menos un valor de $x$ y al menos un valor de $y$ que, juntos, hacen verdadera la condición.

Intercambiar:

$$
\exists x\,\exists y
$$

por:

$$
\exists y\,\exists x
$$

no cambia esa exigencia. El comportamiento es, por tanto, diferente cuando los cuantificadores consecutivos son del **mismo tipo**.

---

### 7.6 Conmutación de cuantificadores del mismo tipo

::: {.ma-block .ma-enunciado #apm-t1-c03-p0008}
**Proposición — Conmutación de cuantificadores consecutivos del mismo tipo**

Sean $x$ e $y$ variables con sus dominios no vacíos previamente fijados, y sea $R(x,y)$ un predicado. Entonces:

$$
\boxed{
\forall x\,\forall y\,R(x,y)
\equiv
\forall y\,\forall x\,R(x,y)
}
$$

y:

$$
\boxed{
\exists x\,\exists y\,R(x,y)
\equiv
\exists y\,\exists x\,R(x,y).
}
$$
:::

#### Demostración del caso universal

La fórmula $\forall x\,\forall y\,R(x,y)$ afirma que:

> para cada valor permitido de $x$, la condición $R(x,y)$ es verdadera para cada valor permitido de $y$.

Esto equivale a exigir que:

$$
R(x,y)
$$

sea verdadera para cada elección permitida de $x$ y para cada elección permitida de $y$.

Pero esa misma exigencia se expresa leyendo primero $y$ y después $x$:

$$
\forall y\,\forall x\,R(x,y).
$$

Por tanto:

$$
\boxed{
\forall x\,\forall y\,R(x,y)
\equiv
\forall y\,\forall x\,R(x,y).
}
$$

#### Demostración del caso existencial

La fórmula $\exists x\,\exists y\,R(x,y)$ afirma que:

> hay algún valor permitido de $x$ y algún valor permitido de $y$ para los cuales $R(x,y)$ es verdadera.

Que nombremos primero el valor de $x$ o primero el valor de $y$ no altera la existencia de esos dos valores.

Por tanto, la misma exigencia se expresa mediante:

$$
\exists y\,\exists x\,R(x,y).
$$

Así:

$$
\boxed{
\exists x\,\exists y\,R(x,y)
\equiv
\exists y\,\exists x\,R(x,y).
}
$$

Quedan demostradas ambas equivalencias.

---

### 7.7 Qué no dice [la proposición «Conmutación de cuantificadores consecutivos del mismo tipo»](#apm-t1-c03-p0008)

[la proposición «Conmutación de cuantificadores consecutivos del mismo tipo»](#apm-t1-c03-p0008) no autoriza a intercambiar arbitrariamente cuantificadores.

La proposición se refiere únicamente a cuantificadores consecutivos del mismo tipo: $\forall\forall$ o $\exists\exists$ No afirma:

$$
\forall x\,\exists y\,R(x,y)
\equiv
\exists y\,\forall x\,R(x,y).
$$

De hecho, ya hemos visto un contraejemplo concreto a esa equivalencia.

Por tanto:

$$

\text{mismo tipo: el orden puede conmutarse;}
\qquad
\text{tipo mixto: no, en general.}

$$

La expresión «en general» es importante. Para algún predicado particular, ambas fórmulas mixtas podrían tener el mismo valor de verdad.

Lo que no podemos hacer es suponer que son equivalentes para todo predicado y todo dominio.

---

### 7.8 Cuatro patrones diferentes

Para un predicado de dos variables podemos encontrar, entre otras, estas cuatro estructuras:

$$
\forall x\,\forall y\,R(x,y),
$$

$$
\forall x\,\exists y\,R(x,y),
$$

$$
\exists x\,\forall y\,R(x,y),
$$

$$
\exists x\,\exists y\,R(x,y).
$$

No deben confundirse. Podemos leerlas así.

#### Dos universales

$$
\forall x\,\forall y\,R(x,y)
$$

dice:

> «$R(x,y)$ se cumple para todos los valores de $x$ y todos los valores de $y$».

#### Universal y luego existencial

$$
\forall x\,\exists y\,R(x,y)
$$

dice:

> «Para cada $x$, hay al menos un $y$ que funciona».

#### Existencial y luego universal

$$
\exists x\,\forall y\,R(x,y)
$$

dice:

> «Hay al menos un $x$ que funciona para todos los valores de $y$».

#### Dos existenciales

$$
\exists x\,\exists y\,R(x,y)
$$

dice:

> «Hay al menos un $x$ y al menos un $y$ que funcionan juntos».

Cada patrón impone una exigencia diferente.

---

### 7.9 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-t1-c03-x0027}
**Ejemplo — El mismo predicado, dos órdenes**
:::

Trabajaremos con valores enteros y definiremos:

$$
R(x,y):\quad y=x+1.
$$

Comparemos $\forall x\,\exists y\,R(x,y)$ con $\exists y\,\forall x\,R(x,y)$.

#### Primera fórmula

$$
\forall x\,\exists y\,(y=x+1).
$$

La lectura es:

> «Para todo entero $x$, existe un entero $y$ tal que $y=x+1$».

Si fijamos cualquier entero $x$, el valor $y=x+1$ también es entero y satisface la condición.

Por tanto:

$$
\boxed{
\forall x\,\exists y\,(y=x+1)
}
$$

es verdadera. El valor de $y$ puede cambiar cuando cambia $x$.

#### Segunda fórmula

$$
\exists y\,\forall x\,(y=x+1).
$$

La lectura es:

> «Existe un entero $y$ que satisface $y=x+1$ para todo entero $x$».

Aquí necesitamos un solo entero $y$ que funcione para todos los valores de $x$.

Supongamos que se propone un valor cualquiera de $y$.

Como el dominio es el de los enteros, también podemos considerar:

$$
x=y.
$$

Entonces la condición exigiría:

$$
y=y+1,
$$

lo cual es falso. Ningún entero $y$ sirve para todos los enteros $x$.

Así:

$$
\boxed{
\exists y\,\forall x\,(y=x+1)
}
$$

es falsa.

#### Conclusión

Tenemos:

$$

\forall x\,\exists y\,R(x,y)=\mathrm V,

$$

pero:

$$

\exists y\,\forall x\,R(x,y)=\mathrm F.

$$

El orden de los cuantificadores mixtos ha cambiado el significado y el valor de verdad.

---
## Ejercicios

### Leer una cadena de cuantificadores {#apm-t1-c03-e0171}
Trabajamos con valores enteros.

Lee en prosa:

$$
\forall x\,\exists y\,R(x,y).
$$

Después explica cuál cuantificador se lee primero.

#### Solución


La fórmula se lee:

> «Para todo entero $x$, existe al menos un entero $y$ para el cual se cumple $R(x,y)$».

El cuantificador que se lee primero es el exterior:

$$
\forall x.
$$

Después, dentro de su alcance, aparece:

$$
\exists y.
$$

Por tanto, primero consideramos un valor de $x$ y después exigimos que haya algún valor de $y$ adecuado para ese caso.

---

### Qué puede cambiar {#apm-t1-c03-e0172}
Trabajamos con valores enteros y definimos:

$$
R(x,y):\quad x+y=0.
$$

Explica qué significa:

$$
\forall x\,\exists y\,R(x,y)
$$

y por qué el valor de $y$ puede cambiar cuando cambia $x$.

#### Solución


La fórmula afirma:

> «Para todo entero $x$, existe un entero $y$ tal que $x+y=0$».

Si:

$$
x=3,
$$

podemos tomar:

$$
y=-3.
$$

Si:

$$
x=-5,
$$

podemos tomar:

$$
y=5.
$$

El cuantificador existencial está dentro del alcance del cuantificador universal.

Por tanto, después de considerar cada valor de $x$, podemos encontrar un valor de $y$ adecuado para ese caso.

No se exige que el mismo $y$ funcione para todos los valores de $x$.

---

### Justificar una conmutación válida {#apm-t1-c03-e0173}
Explica por qué:

$$
\exists x\,\exists y\,R(x,y)
\equiv
\exists y\,\exists x\,R(x,y).
$$

No te limites a citar [la proposición «Conmutación de cuantificadores consecutivos del mismo tipo»](#apm-t1-c03-p0008): explica el significado de ambas fórmulas.

#### Solución


La primera fórmula:

$$
\exists x\,\exists y\,R(x,y)
$$

afirma que hay algún valor permitido de $x$ y algún valor permitido de $y$ para los cuales:

$$
R(x,y)
$$

es verdadera.

La segunda:

$$
\exists y\,\exists x\,R(x,y)
$$

afirma exactamente la misma existencia, pero nombra primero el valor de $y$ y después el de $x$.

Si existen valores adecuados de $x$ e $y$, existen independientemente del orden en que los mencionemos.

Por tanto:

$$
\boxed{
\exists x\,\exists y\,R(x,y)
\equiv
\exists y\,\exists x\,R(x,y).
}
$$

---

### Un intercambio inválido {#apm-t1-c03-e0174}
Trabajamos con valores enteros y definimos:

$$
R(x,y):\quad y=x+1.
$$

#### a)

Determina el valor de verdad de:

$$
\forall x\,\exists y\,R(x,y).
$$

#### b)

Determina el valor de verdad de:

$$
\exists y\,\forall x\,R(x,y).
$$

#### c)

Explica por qué este ejemplo refuta la equivalencia general entre ambas fórmulas.

#### Solución


#### a)

La fórmula:

$$
\forall x\,\exists y\,(y=x+1)
$$

es verdadera.

Para cualquier entero $x$, podemos tomar:

$$
y=x+1,
$$

que también es entero.

#### b)

La fórmula:

$$
\exists y\,\forall x\,(y=x+1)
$$

es falsa.

Un solo entero $y$ tendría que satisfacer la ecuación para todos los valores de $x$.

Para cualquier valor propuesto de $y$, podemos tomar:

$$
x=y.
$$

Entonces necesitaríamos:

$$
y=y+1,
$$

lo cual es falso.

#### c)

La primera fórmula es verdadera y la segunda es falsa bajo el mismo dominio y el mismo predicado.

Por tanto, no pueden ser lógicamente equivalentes en general.

---

### Construir un segundo contraejemplo {#apm-t1-c03-e0175}
Trabajamos con valores enteros y definimos:

$$
S(x,y):\quad x+y=0.
$$

Compara:

$$
\forall x\,\exists y\,S(x,y)
$$

con:

$$
\exists y\,\forall x\,S(x,y).
$$

Determina el valor de verdad de cada una y explica por qué este ejemplo vuelve a mostrar que los cuantificadores mixtos no pueden intercambiarse en general.

#### Solución


#### Primera fórmula

$$
\forall x\,\exists y\,(x+y=0).
$$

Para cada entero $x$, podemos tomar:

$$
y=-x.
$$

Entonces:

$$
x+(-x)=0.
$$

Por tanto, la fórmula es verdadera.

#### Segunda fórmula

$$
\exists y\,\forall x\,(x+y=0).
$$

Aquí tendría que existir un único entero $y$ que satisficiera:

$$
x+y=0
$$

para todos los enteros $x$.

Eso es imposible.

Por ejemplo, si la condición se cumpliera para:

$$
x=0,
$$

tendríamos:

$$
y=0.
$$

Pero entonces, para:

$$
x=1,
$$

obtendríamos:

$$
1+0=0,
$$

que es falso.

Por tanto, la segunda fórmula es falsa.

Una vez más:

$$
\forall x\,\exists y\,S(x,y)
$$

y:

$$
\exists y\,\forall x\,S(x,y)
$$

tienen valores de verdad distintos.

---

### Cuatro patrones cuantificados {#apm-t1-c03-e0176}
Trabajamos con valores enteros y definimos:

$$
R(x,y):\quad x<y.
$$

Determina el valor de verdad de cada fórmula y justifica.

#### a)

$$
\forall x\,\forall y\,R(x,y)
$$

#### b)

$$
\forall x\,\exists y\,R(x,y)
$$

#### c)

$$
\exists x\,\forall y\,R(x,y)
$$

#### d)

$$
\exists x\,\exists y\,R(x,y)
$$

#### Solución


#### a)

$$
\forall x\,\forall y\,(x<y)
$$

es falsa.

Por ejemplo, podemos tomar:

$$
x=0,
\qquad
y=0.
$$

Entonces:

$$
0<0
$$

es falsa.

#### b)

$$
\forall x\,\exists y\,(x<y)
$$

es verdadera.

Para cualquier entero $x$, podemos tomar:

$$
y=x+1.
$$

Entonces:

$$
x<x+1.
$$

#### c)

$$
\exists x\,\forall y\,(x<y)
$$

es falsa.

Para cualquier entero propuesto como $x$, podemos tomar:

$$
y=x.
$$

Entonces la condición exigiría:

$$
x<x,
$$

que es falsa.

Por tanto, ningún entero $x$ es menor que todos los enteros.

#### d)

$$
\exists x\,\exists y\,(x<y)
$$

es verdadera.

Por ejemplo:

$$
x=0,
\qquad
y=1
$$

satisfacen:

$$
0<1.
$$

#### Comparación

Obtenemos:

$$
\boxed{
\begin{array}{c|c}
\text{Fórmula} & \text{Valor}\\
\hline
\forall x\,\forall y\,R(x,y) & \mathrm F\\
\forall x\,\exists y\,R(x,y) & \mathrm V\\
\exists x\,\forall y\,R(x,y) & \mathrm F\\
\exists x\,\exists y\,R(x,y) & \mathrm V
\end{array}
}
$$

Los cuatro patrones imponen exigencias lógicas diferentes.

---

## Síntesis

Cuando una fórmula contiene varios cuantificadores debemos leerla desde fuera hacia dentro.

El orden puede codificar una diferencia esencial. En:

$$
\forall x\,\exists y\,R(x,y),
$$

el valor de $y$ puede ajustarse al valor de $x$ que estamos considerando.

En:

$$
\exists y\,\forall x\,R(x,y),
$$

un único valor de $y$ debe funcionar para todos los valores de $x$.

Por eso, en general:

$$

\forall x\,\exists y\,R(x,y)
\not\equiv
\exists y\,\forall x\,R(x,y).

$$

En cambio, los cuantificadores consecutivos del mismo tipo sí conmutan:

$$

\forall x\,\forall y\,R(x,y)
\equiv
\forall y\,\forall x\,R(x,y)

$$

y:

$$

\exists x\,\exists y\,R(x,y)
\equiv
\exists y\,\exists x\,R(x,y).

$$

La lección central es:

$$

\text{en una fórmula cuantificada, el orden también forma parte del significado}.

$$

Ahora ya sabemos leer las piezas fundamentales del lenguaje cuantificacional.

El paso siguiente será aprender a pasar sistemáticamente entre ese lenguaje simbólico y las frases matemáticas escritas en prosa.

## Hacia la sección siguiente

Una fórmula como:

$$
\forall x\,\exists y\,(P(x)\Rightarrow Q(x,y))
$$

debe poder leerse con precisión en castellano. Y una frase como:

> «Para cada valor de $x$, existe algún valor de $y$ que satisface cierta condición»

debe poder convertirse en una fórmula sin alterar el orden, el alcance ni los conectivos.

## §8. Traducir entre prosa y símbolos

Los símbolos lógicos no sustituyen al lenguaje matemático ordinario.

Lo hacen **más preciso**. Una fórmula como:

$$
\forall x\,(P(x)\Rightarrow Q(x))
$$

debe poder leerse en castellano sin perder nada de su estructura.

Y una frase como:

> «Todo objeto que cumple $P$ cumple también $Q$»

debe poder convertirse en una fórmula sin cambiar su significado.

Traducir bien exige conservar, al menos, cuatro elementos:

1. **el dominio**;
2. **los cuantificadores**;
3. **el orden y el alcance**;
4. **los conectivos que relacionan las condiciones**.

Una traducción que cambia alguno de estos elementos puede producir una afirmación matemática diferente.

Por tanto:

$$
\boxed{
\text{traducir}
\neq
\text{sustituir palabras por símbolos}.
}
$$

Traducir es reconstruir la **estructura lógica** de una afirmación.

---

### 8.1 Antes de traducir: fijar el dominio

Consideremos la frase:

> «Todo número tiene una propiedad $P$».

La palabra:

> «número»

es demasiado amplia si el contexto no ha dicho qué clase de números estamos considerando.

En una discusión podríamos estar trabajando con enteros. En otra, con racionales.

En otra, con reales. En este capítulo no escribiremos todavía cuantificadores restringidos mediante pertenencia.

Por eso declararemos primero el dominio. Por ejemplo:

> **Dominio:** números enteros.

Después escribiremos:

$$
\forall x\,P(x).
$$

El dominio no desaparece al pasar a símbolos. Permanece fijado por el contexto.

---

### 8.2 «Todo $P$ es $Q$»: aparece una implicación

Supongamos que el dominio ya está fijado y que:

$$
P(x)
$$

significa:

> «$x$ tiene la propiedad $P$»,

mientras:

$$
Q(x)
$$

significa:

> «$x$ tiene la propiedad $Q$».

Queremos traducir:

> «Todo objeto que cumple $P$ cumple $Q$».

La estructura no es:

$$
\forall x\,(P(x)\land Q(x)).
$$

Esa fórmula diría que **todos los objetos del dominio** cumplen simultáneamente $P$ y $Q$.

La frase original dice otra cosa:

> si un objeto cumple $P$, entonces cumple $Q$.

Por tanto:

$$

\forall x\,(P(x)\Rightarrow Q(x)).

$$

La implicación es esencial. El patrón es:

$$
\boxed{
\text{«todo }P\text{ es }Q\text{»}
\longrightarrow
\forall x\,(P(x)\Rightarrow Q(x)).
}
$$

---

### 8.3 «Algún $P$ es $Q$»: aparece una conjunción

Ahora traduzcamos:

> «Algún objeto cumple $P$ y cumple $Q$».

Necesitamos afirmar que existe al menos un valor para el cual las dos condiciones son verdaderas.

Por tanto:

$$

\exists x\,(P(x)\land Q(x)).

$$

Aquí la conjunción cumple un papel distinto del que tenía la implicación en el caso universal.

El patrón es:

$$
\boxed{
\text{«algún }P\text{ es }Q\text{»}
\longrightarrow
\exists x\,(P(x)\land Q(x)).
}
$$

Comparemos:

$$
\forall x\,(P(x)\Rightarrow Q(x))
$$

con:

$$
\exists x\,(P(x)\land Q(x)).
$$

La primera formula una condición universal. La segunda afirma la existencia de un caso donde ambas propiedades se cumplen.

---

### 8.4 Traducir «ningún»

La frase:

> «Ningún objeto que cumple $P$ cumple $Q$»

puede expresarse de más de una forma equivalente. Una opción es:

$$
\forall x\,(P(x)\Rightarrow\neg Q(x)).
$$

Se lee:

> «Para todo $x$, si $x$ cumple $P$, entonces no cumple $Q$».

Otra opción es decir que no existe ningún caso que cumpla simultáneamente ambas propiedades:

$$
\neg\exists x\,(P(x)\land Q(x)).
$$

Por las leyes ya demostradas en [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007), ambas formulaciones expresan la misma exclusión.

Así:

$$

\text{«ningún }P\text{ es }Q\text{»}

$$

puede representarse como:

$$

\forall x\,(P(x)\Rightarrow\neg Q(x))

$$

o, equivalentemente:

$$

\neg\exists x\,(P(x)\land Q(x)).

$$

La elección entre ambas formas puede depender de cuál sea más clara en el contexto.

---

### 8.5 Traducir «no todos»

Consideremos:

> «No todos los objetos cumplen $P$».

La traducción inmediata es:

$$
\neg\forall x\,P(x).
$$

Pero [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007) nos permite escribir una forma equivalente:

$$
\exists x\,\neg P(x).
$$

Por tanto:

$$

\text{«no todos cumplen }P\text{»}
\longleftrightarrow
\exists x\,\neg P(x).

$$

La frase **no** significa:

$$
\forall x\,\neg P(x).
$$

Eso diría:

> «Ninguno cumple $P$».

La diferencia lingüística corresponde exactamente a la diferencia lógica estudiada en §5.

---

### 8.6 Dos cuantificadores: preservar el orden

Supongamos ahora que:

$$
R(x,y)
$$

expresa una condición entre dos variables. La frase:

> «Para cada valor de $x$, existe algún valor de $y$ para el cual se cumple $R(x,y)$»

se traduce:

$$
\boxed{
\forall x\,\exists y\,R(x,y).
}
$$

En cambio:

> «Existe algún valor de $y$ tal que, para cada valor de $x$, se cumple $R(x,y)$»

se traduce:

$$
\boxed{
\exists y\,\forall x\,R(x,y).
}
$$

Ya sabemos que estas dos fórmulas no son equivalentes en general.

Por eso, al traducir una frase con varios cuantificadores:

$$
\boxed{
\text{el orden de la prosa debe conservarse en la fórmula}.
}
$$

No podemos decidir el orden por comodidad tipográfica.

---

### 8.7 El alcance también debe conservarse

Consideremos ahora una proposición $Q$ que no depende de $x$.

Comparemos las frases:

> «Si todos los valores de $x$ cumplen $P(x)$, entonces $Q$».

y:

> «Para todo valor de $x$, si $P(x)$ se cumple, entonces $Q$».

La primera tiene la estructura:

$$
(\forall x\,P(x))\Rightarrow Q.
$$

La segunda tiene la estructura:

$$
\forall x\,(P(x)\Rightarrow Q).
$$

Los mismos símbolos aparecen en ambas expresiones, pero el alcance del cuantificador es distinto.

En la primera, el universal forma parte del antecedente completo de la implicación:

$$
\forall x\,P(x).
$$

En la segunda, el universal gobierna toda la implicación $P(x)\Rightarrow Q$ No podemos mover los paréntesis sin analizar el significado.

Por ejemplo, si $Q$ es falsa y el dominio contiene dos valores, uno que satisface $P$ y otro que no la satisface, entonces $(\forall x\,P(x))\Rightarrow Q$ es verdadera, porque su antecedente es falso; en cambio:

$$
\forall x\,(P(x)\Rightarrow Q)
$$

es falsa, porque para el valor que satisface $P$ obtenemos una implicación con antecedente verdadero y consecuente falso.

Así:

$$
\boxed{
\text{preservar el alcance también es preservar el significado}.
}
$$

---

### 8.8 Símbolos hacia prosa: no leer mecánicamente

Consideremos:

$$
\forall x\,(P(x)\Rightarrow Q(x)).
$$

Una lectura demasiado mecánica sería:

> «Para todo $x$, $P(x)$ implica $Q(x)$».

No es incorrecta, pero puede ocultar el contenido. Una lectura matemática más natural es:

> «Todo objeto del dominio que cumple $P$ cumple también $Q$».

De manera semejante:

$$
\exists x\,(P(x)\land Q(x))
$$

puede leerse:

> «Existe al menos un objeto del dominio que cumple tanto $P$ como $Q$».

La traducción hacia prosa debe conservar la estructura lógica, pero puede utilizar una redacción natural.

---

### 8.9 Un procedimiento de traducción

Ante una frase matemática, conviene seguir este orden.

#### Paso 1 — Identificar el dominio

¿De qué objetos estamos hablando?

#### Paso 2 — Identificar las variables

¿Qué puede variar?

#### Paso 3 — Localizar las palabras cuantificacionales

Por ejemplo:

- todo;
- cada;
- algún;
- existe;
- ningún;
- no todos.

#### Paso 4 — Identificar los conectivos

Buscar estructuras como:

- «y»;
- «o»;
- «si..., entonces...»;
- «no».

#### Paso 5 — Determinar el alcance

¿Qué parte de la afirmación queda gobernada por cada cuantificador o conectivo?

#### Paso 6 — Preservar el orden

Especialmente cuando aparecen varios cuantificadores.

#### Paso 7 — Volver a leer la fórmula en prosa

La prueba final de una traducción es preguntar:

> «¿La fórmula que escribí vuelve a decir exactamente la frase original?»

Podemos resumir:

$$
\boxed{
\text{prosa}
\longrightarrow
\text{estructura}
\longrightarrow
\text{símbolos}
\longrightarrow
\text{prosa}.
}
$$

---

### 8.10 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-t1-c03-x0028}
**Ejemplo — Traducir en ambos sentidos**
:::

Trabajaremos sobre un dominio previamente fijado. Sean:

$$
P(x),
\qquad
Q(x),
\qquad
R(x,y)
$$

predicados.

#### A. «Todo objeto que cumple $P$ cumple $Q$»

La palabra:

> «todo»

indica cuantificación universal. La estructura:

> «que cumple $P$ ... cumple $Q$»

se expresa mediante una implicación. Por tanto:

$$
\boxed{
\forall x\,(P(x)\Rightarrow Q(x)).
}
$$

#### B. «Algún objeto cumple $P$ y $Q$»

La palabra:

> «algún»

indica cuantificación existencial. Debemos encontrar un mismo valor de $x$ para el cual se cumplan ambas condiciones.

Por tanto:

$$
\boxed{
\exists x\,(P(x)\land Q(x)).
}
$$

#### C. «Ningún objeto que cumple $P$ cumple $Q$»

Podemos escribir:

$$
\boxed{
\forall x\,(P(x)\Rightarrow\neg Q(x)).
}
$$

Equivalentemente:

$$
\boxed{
\neg\exists x\,(P(x)\land Q(x)).
}
$$

#### D. «No todos los objetos cumplen $P$»

Escribimos $\neg\forall x\,P(x)$. Por [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007):

$$
\boxed{
\exists x\,\neg P(x).
}
$$

#### E. «Para cada $x$, existe algún $y$ tal que $R(x,y)$»

El orden verbal es:

> «para cada $x$» → «existe algún $y$».

Por tanto:

$$
\boxed{
\forall x\,\exists y\,R(x,y).
}
$$

#### F. «Existe algún $y$ tal que, para cada $x$, se cumple $R(x,y)$»

Ahora el orden es el contrario:

> «existe algún $y$» → «para cada $x$».

Por tanto:

$$
\boxed{
\exists y\,\forall x\,R(x,y).
}
$$

Las fórmulas E y F utilizan los mismos símbolos, pero no dicen lo mismo en general.

#### G. Volver de símbolos a prosa

Consideremos:

$$
\forall x\,\exists y\,(P(x)\Rightarrow R(x,y)).
$$

Una lectura estructural es:

> «Para todo valor de $x$, existe al menos un valor de $y$ tal que, si $P(x)$ se cumple, entonces $R(x,y)$ se cumple».

La traducción preserva:

- el universal exterior;
- el existencial interior;
- el orden;
- la implicación;
- el alcance de los cuantificadores.

---
## Ejercicios

### De una frase universal a símbolos {#apm-t1-c03-e0177}
El dominio está previamente fijado.

Sean:

$$
P(x)
$$

y:

$$
Q(x)
$$

predicados.

Traduce:

> «Todo objeto que cumple $P$ cumple también $Q$».

#### Solución


La palabra:

> «todo»

indica que debemos cuantificar universalmente.

La frase no afirma que todos los objetos cumplan $P$ y $Q$.

Afirma que **si** un objeto cumple $P$, **entonces** cumple $Q$.

Por tanto:

$$
\boxed{
\forall x\,(P(x)\Rightarrow Q(x)).
}
$$

---

### Una existencia con dos condiciones {#apm-t1-c03-e0178}
El dominio está previamente fijado.

Traduce:

> «Existe al menos un objeto que cumple $P$ y no cumple $Q$».

#### Solución


La expresión:

> «existe al menos un»

indica:

$$
\exists x.
$$

Para ese mismo valor de $x$ deben cumplirse simultáneamente:

$$
P(x)
$$

y:

$$
\neg Q(x).
$$

Por tanto:

$$
\boxed{
\exists x\,(P(x)\land\neg Q(x)).
}
$$

---

### De símbolos a prosa {#apm-t1-c03-e0179}
Lee en prosa:

$$
\neg\exists x\,(P(x)\land Q(x)).
$$

Después da una segunda formulación equivalente utilizando [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007).

#### Solución


Una lectura natural es:

> «No existe ningún objeto del dominio que cumpla simultáneamente $P$ y $Q$».

Por [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007):

$$
\neg\exists x\,(P(x)\land Q(x))
\equiv
\forall x\,\neg(P(x)\land Q(x)).
$$

Por la ley de De Morgan de [el capítulo 2](algebra-para-matematicos-capitulo-2-logica-proposicional-y-algebra-de-proposiciones.md):

$$
\neg(P(x)\land Q(x))
\equiv
\neg P(x)\lor\neg Q(x).
$$

Por tanto, también podemos escribir:

$$
\boxed{
\forall x\,(\neg P(x)\lor\neg Q(x)).
}
$$

En prosa:

> «Para todo objeto del dominio, o bien no cumple $P$, o bien no cumple $Q$».

---

### Por qué no podemos invertir los cuantificadores {#apm-t1-c03-e0180}
Trabajamos con valores enteros y definimos:

$$
R(x,y):\quad y=x+1.
$$

Una persona traduce:

> «Para cada entero $x$, existe un entero $y$ tal que $y=x+1$»

como:

$$
\exists y\,\forall x\,R(x,y).
$$

Explica con precisión cuál es el error.

#### Solución


La frase comienza:

> «Para cada entero $x$...»

Por tanto, el cuantificador exterior debe ser:

$$
\forall x.
$$

Después dice:

> «...existe un entero $y$...»

Por tanto, dentro de ese universal debe aparecer:

$$
\exists y.
$$

La traducción correcta es:

$$
\boxed{
\forall x\,\exists y\,R(x,y).
}
$$

La fórmula propuesta:

$$
\exists y\,\forall x\,R(x,y)
$$

cambia el orden y, con él, el significado.

La fórmula correcta permite elegir un $y$ distinto para cada $x$.

La fórmula incorrecta exige un único $y$ que funcione para todos los enteros $x$.

En este ejemplo, la primera es verdadera y la segunda es falsa.

---

### Una implicación dentro del alcance {#apm-t1-c03-e0181}
El dominio está previamente fijado.

Sean:

$$
P(x)
$$

y:

$$
R(x,y)
$$

predicados.

Traduce:

> «Para todo valor de $x$, si $P(x)$ se cumple, entonces existe al menos un valor de $y$ para el cual se cumple $R(x,y)$».

Explica el alcance de cada cuantificador.

#### Solución


El primer fragmento:

> «Para todo valor de $x$»

produce:

$$
\forall x.
$$

Después aparece una implicación:

> «si $P(x)$ se cumple, entonces...»

La consecuencia afirma:

> «existe al menos un valor de $y$ para el cual se cumple $R(x,y)$».

Por tanto, la traducción es:

$$
\boxed{
\forall x\,(P(x)\Rightarrow\exists y\,R(x,y)).
}
$$

El alcance de:

$$
\forall x
$$

es toda la implicación:

$$
P(x)\Rightarrow\exists y\,R(x,y).
$$

El alcance de:

$$
\exists y
$$

es:

$$
R(x,y).
$$

---

### Traducción bidireccional con dos cuantificadores {#apm-t1-c03-e0182}
Trabajamos con valores enteros y definimos:

$$
R(x,y):\quad x+y=0.
$$

#### a)

Traduce a símbolos:

> «Para cada entero $x$, existe un entero $y$ cuya suma con $x$ es igual a cero».

#### b)

Decide si la afirmación es verdadera y explica su significado.

#### c)

Ahora lee en prosa:

$$
\exists y\,\forall x\,R(x,y).
$$

#### d)

Decide si esta segunda afirmación es verdadera.

#### e)

Explica qué información de la prosa debe conservarse necesariamente al traducir entre ambas direcciones.

#### Solución


#### a)

La frase comienza con:

> «Para cada entero $x$»

y después afirma:

> «existe un entero $y$».

Por tanto:

$$
\boxed{
\forall x\,\exists y\,(x+y=0).
}
$$

#### b)

La afirmación es verdadera.

Para cada entero $x$ podemos elegir:

$$
y=-x.
$$

Entonces:

$$
x+(-x)=0.
$$

La fórmula dice que cada entero admite algún entero que, sumado con él, produce cero.

#### c)

La fórmula:

$$
\exists y\,\forall x\,R(x,y)
$$

se lee:

> «Existe un entero $y$ tal que, para todo entero $x$, se cumple $x+y=0$».

#### d)

La segunda afirmación es falsa.

Si existiera un entero fijo $y$ que cumpliera:

$$
x+y=0
$$

para todo entero $x$, debería funcionar tanto para:

$$
x=0
$$

como para:

$$
x=1.
$$

Del primer caso obtendríamos:

$$
y=0.
$$

Pero entonces el segundo exigiría:

$$
1+0=0,
$$

lo cual es falso.

#### e)

Al traducir debemos conservar necesariamente:

- el dominio;
- qué variables aparecen;
- qué cuantificador corresponde a cada variable;
- el orden de los cuantificadores;
- el alcance;
- la condición expresada por el predicado.

Cambiar alguno de esos elementos puede producir una afirmación distinta.

---

## Síntesis

Traducir entre prosa y símbolos es una operación estructural.

No basta con reconocer palabras aisladas. Debemos identificar:

$$

\text{dominio}
+
\text{variables}
+
\text{cuantificadores}
+
\text{orden}
+
\text{alcance}
+
\text{conectivos}.

$$

Algunos patrones importantes son:

$$

\text{«todo }P\text{ es }Q\text{»}
\longrightarrow
\forall x\,(P(x)\Rightarrow Q(x))

$$

$$

\text{«algún }P\text{ es }Q\text{»}
\longrightarrow
\exists x\,(P(x)\land Q(x))

$$

$$

\text{«no todos cumplen }P\text{»}
\longrightarrow
\exists x\,\neg P(x)

$$

y:

$$

\text{«para cada }x\text{ existe un }y\text{»}
\longrightarrow
\forall x\,\exists y.

$$

La comprobación final consiste siempre en regresar a la prosa:

$$

\text{prosa}
\longrightarrow
\text{símbolos}
\longrightarrow
\text{prosa}.

$$

Si el significado cambia al volver, la traducción inicial no era correcta.

Hasta ahora todas las letras variables que hemos cuantificado podían variar dentro del dominio.

Pero en muchas discusiones matemáticas una letra queda **fijada** mientras otras continúan variando.

Para describir esa situación necesitamos distinguir una variable de un parámetro.

## Hacia la sección siguiente

Consideremos $P_a(x):\quad x+a=a$. Podemos estudiar esta condición manteniendo $a$ fijo mientras $x$ varía.

¿Qué significa exactamente que una letra permanezca fija dentro de una discusión?

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

::: {.ma-block .ma-definicion #apm-t1-c03-d0034}
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

::: {.ma-block .ma-observacion #apm-t1-c03-x0029}
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

### Parámetro y variable {#apm-t1-c03-e0183}
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

### ¿Qué significa «fijemos $a$»? {#apm-t1-c03-e0184}
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

### Dos contextos distintos {#apm-t1-c03-e0185}
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

### Por qué no puede cambiar de papel en silencio {#apm-t1-c03-e0186}
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

### Explorar varios valores de un parámetro {#apm-t1-c03-e0187}
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

### Parámetro y cuantificador {#apm-t1-c03-e0188}
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

## §10. Existencia y unicidad

En §4 aprendimos a leer:

$$
\exists x\,P(x)
$$

como:

> «Existe al menos un valor permitido de $x$ para el cual se cumple $P(x)$».

Desde entonces hemos insistido en una advertencia:

$$
\boxed{
\text{existencia}
\neq
\text{unicidad}.
}
$$

Encontrar un valor que satisface una condición demuestra que la exigencia existencial se cumple.

Pero no nos dice, por sí solo, si hay otros valores que también la satisfacen.

Consideremos, en el dominio de los enteros:

$$
P(x):\quad x^2=9.
$$

Tenemos, $P(3)$ y $P(-3)$. Por tanto:

$$
\exists x\,P(x)
$$

es verdadera.

Sin embargo, no hay un único valor que satisfaga la condición.

Ahora comparemos $Q(x):\quad 2x=6$. El valor $x=3$ satisface la condición.

Además, ningún otro entero la satisface. Aquí queremos expresar algo más fuerte que mera existencia:

> existe **exactamente un** valor.

---

### 10.1 Dos preguntas distintas

Ante una condición:

$$
P(x),
$$

podemos hacer dos preguntas.

#### Pregunta de existencia

> ¿Hay al menos un valor que satisface $P(x)$?

En símbolos:

$$
\exists x\,P(x).
$$

#### Pregunta de unicidad

> Si dos valores satisfacen $P(x)$, ¿tienen necesariamente que ser el mismo?

La existencia responde:

> «hay uno o más».

La unicidad responde:

> «no puede haber dos distintos».

Para afirmar **existencia única**, necesitamos ambas cosas. Así:

$$

\text{existencia única}
=
\text{existencia}
+
\text{unicidad}.

$$

---

### 10.2 La abreviatura \(\exists!\)

::: {.ma-block .ma-definicion #apm-t1-c03-d0035}
**Definición — Existencia única**

La escritura:

$$
\exists!x\,P(x)
$$

se lee:

> «Existe un único valor de $x$ para el cual se cumple $P(x)$».

Es una abreviatura de:

$$
\boxed{
\exists x\,\bigl(P(x)\land
\forall y\,(P(y)\Rightarrow y=x)\bigr).
}
$$
:::

El símbolo $\exists!$ no introduce un tercer tipo fundamental de cuantificador.

Es una abreviatura construida con:

$$
\exists,
\qquad
\forall,
\qquad
\land,
\qquad
\Rightarrow,
\qquad
=.
$$

Por eso conviene saber siempre expandirlo.

---

### 10.3 Leer la expansión

Examinemos:

$$
\exists x\,\bigl(P(x)\land
\forall y\,(P(y)\Rightarrow y=x)\bigr).
$$

La fórmula comienza con:

$$
\exists x.
$$

Por tanto, afirma que hay al menos un valor:

$$
x
$$

que cumple lo que sigue. Dentro encontramos una conjunción:

$$
P(x)
\land
\forall y\,(P(y)\Rightarrow y=x).
$$

La primera parte:

$$
P(x)
$$

dice:

> «$x$ satisface la condición».

La segunda:

$$
\forall y\,(P(y)\Rightarrow y=x)
$$

dice:

> «Cualquier otro valor $y$ que satisfaga la condición debe ser igual a $x$».

Así, el valor cuya existencia afirmamos no solo satisface $P$.

También absorbe todos los posibles casos: cualquiera que satisfaga $P$ tiene que coincidir con él.

---

### 10.4 La cláusula de existencia

Consideremos $\exists!x\,P(x)$. La expansión contiene:

$$
\exists x.
$$

Si no existe ningún valor que satisfaga:

$$
P(x),
$$

la afirmación de existencia única es falsa. Por ejemplo, en el dominio de los enteros:

$$
P(x):\quad 2x=1.
$$

No hay ningún entero que satisfaga la condición. Entonces $\exists!x\,(2x=1)$ es falsa.

No importa que podamos decir:

> «Si hubiera dos soluciones, serían iguales».

Sin existencia, no hay existencia única. Por eso la primera mitad del problema es siempre:

$$

\text{¿hay al menos un valor que funciona?}

$$

---

### 10.5 La cláusula de unicidad

Ahora consideremos, en los enteros:

$$
P(x):\quad x^2=9.
$$

Sí hay valores que satisfacen la condición. Por ejemplo: $x=3$.

Pero también:

$$
x=-3.
$$

Como:

$$
3\ne-3,
$$

hay al menos dos valores distintos que satisfacen $P$.

Por tanto:

$$
\exists!x\,(x^2=9)
$$

es falsa. La existencia se cumple. La unicidad falla. Así vemos que:

$$
\boxed{
\text{existencia sin unicidad}
\quad\text{no basta para}\quad
\exists!.
}
$$

---

### 10.6 Un ejemplo verdaderamente único

Trabajemos con enteros y consideremos:

$$
P(x):\quad 2x=6.
$$

Primero observamos que:

$$
x=3
$$

satisface:

$$
2x=6.
$$

Por tanto, existe al menos un valor. Ahora supongamos que un entero:

$$
y
$$

también satisface la condición. Entonces $2y=6$. Dividiendo ambos lados por $2$:

$$
y=3.
$$

Cualquier entero que satisfaga la condición debe ser igual a:

$$
3.
$$

Esto corresponde exactamente a:

$$
\forall y\,(2y=6\Rightarrow y=3).
$$

Así:

$$
\exists x\,\bigl(
2x=6
\land
\forall y\,(2y=6\Rightarrow y=x)
\bigr)
$$

es verdadera. En forma abreviada:

$$

\exists!x\,(2x=6).

$$

---

### 10.7 No confundir «el» con una prueba de unicidad

En la prosa matemática aparecen frases como:

> «el valor que satisface...»

o:

> «la solución...»

Ese artículo singular puede sugerir unicidad.

Pero el lenguaje no debe adelantarse a lo que hemos establecido.

Por ejemplo, para:

$$
x^2=9,
$$

sería engañoso hablar sin más de:

> «la solución entera»,

porque hay dos:

$$
3
\qquad\text{y}\qquad
-3.
$$

Antes de usar una descripción singular conviene saber si la condición realmente determina un único objeto.

La lógica nos ayuda a distinguir:

$$
\boxed{
\text{haber encontrado uno}
\neq
\text{haber demostrado que es el único}.
}
$$

---

### 10.8 Dos maneras equivalentes de expresar unicidad

La expansión canónica que adoptamos es:

$$
\exists x\,\bigl(
P(x)\land
\forall y\,(P(y)\Rightarrow y=x)
\bigr).
$$

Podemos leer la parte de unicidad como:

> «Todo valor que cumple $P$ coincide con el valor encontrado».

También podemos expresarla informalmente diciendo:

> «No existen dos valores distintos que cumplan $P$».

En este capítulo mantendremos como forma canónica la primera, porque hace visible la estructura:

1. encontrar un valor $x$;
2. exigir que cualquier $y$ que también cumpla $P$ satisfaga:
   $$
   y=x.
   $$

No necesitamos introducir otra abreviatura.

---

### 10.9 Existencia única y dominio

Como ocurre con toda afirmación cuantificada, el dominio sigue siendo esencial.

Consideremos $P(x):\quad x^2=4$. Si el dominio contiene únicamente valores no negativos, el único valor que satisface la condición es:

$$
2.
$$

En ese contexto:

$$
\exists!x\,P(x)
$$

es verdadera. Si el dominio es el de los enteros, en cambio, tanto:

$$
2
$$

como:

$$
-2
$$

satisfacen:

$$
x^2=4.
$$

Entonces la existencia se mantiene, pero la unicidad desaparece.

Así:

$$
\boxed{
\text{la unicidad también se afirma respecto de un dominio}.
}
$$

---

### 10.10 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-t1-c03-x0030}
**Ejemplo — Existencia y unicidad por separado**
:::

Trabajaremos con valores enteros y consideraremos:

$$
P(x):\quad 2x=6.
$$

Queremos analizar:

$$
\exists!x\,P(x).
$$

#### Paso 1 — Existencia

Tomemos $x=3$. Entonces $2\cdot3=6$. Por tanto:

$$
P(3)
$$

es verdadera. La existencia queda confirmada.

#### Paso 2 — Unicidad

Consideremos un entero cualquiera:

$$
y
$$

que también satisfaga:

$$
P(y).
$$

Entonces $2y=6$. Dividiendo por $2$:

$$
y=3.
$$

Por tanto, cualquier entero que satisfaga $P$ coincide con el valor:

$$
3.
$$

Esto se expresa mediante:

$$
\forall y\,(P(y)\Rightarrow y=3).
$$

#### Paso 3 — Reunir ambas partes

Tenemos:

$$
P(3)
$$

y:

$$
\forall y\,(P(y)\Rightarrow y=3).
$$

Por tanto:

$$
\exists x\,\bigl(
P(x)\land
\forall y\,(P(y)\Rightarrow y=x)
\bigr)
$$

es verdadera. En forma abreviada:

$$
\boxed{
\exists!x\,P(x).
}
$$

#### Comparación

Para:

$$
Q(x):\quad x^2=9,
$$

también hay existencia.

Pero: $Q(3)$ y $Q(-3)$ son verdaderas. Por tanto:

$$
\exists x\,Q(x)
$$

es verdadera, mientras:

$$
\exists!x\,Q(x)
$$

es falsa. La diferencia es exactamente la unicidad.

---
## Ejercicios

### Leer \(\exists!\) {#apm-t1-c03-e0189}
Trabajamos con valores enteros.

Lee en prosa:

$$
\exists!x\,(x+2=5).
$$

#### Solución


La fórmula se lee:

> «Existe un único entero $x$ tal que $x+2=5$».

La palabra:

> «único»

indica que la afirmación contiene dos exigencias:

- al menos un entero satisface la ecuación;
- ningún entero distinto puede satisfacerla también.

---

### Al menos uno y exactamente uno {#apm-t1-c03-e0190}
Compara:

$$
\exists x\,(x^2=9)
$$

con:

$$
\exists!x\,(x^2=9)
$$

en el dominio de los enteros.

Determina el valor de verdad de cada fórmula y explica la diferencia.

#### Solución


La primera fórmula:

$$
\exists x\,(x^2=9)
$$

es verdadera.

Por ejemplo:

$$
x=3
$$

satisface la condición.

Pero también:

$$
x=-3
$$

la satisface.

Por tanto, la segunda fórmula:

$$
\exists!x\,(x^2=9)
$$

es falsa.

La diferencia es:

- $\exists$ exige al menos un valor;
- $\exists!$ exige exactamente uno.

---

### Las dos cláusulas {#apm-t1-c03-e0191}
Explica qué función cumple cada parte de:

$$
\exists x\,\bigl(
P(x)\land
\forall y\,(P(y)\Rightarrow y=x)
\bigr).
$$

#### Solución


El cuantificador:

$$
\exists x
$$

afirma que hay algún valor:

$$
x
$$

para el cual se cumple la conjunción interna.

La primera parte:

$$
P(x)
$$

es la **cláusula de existencia**: el valor encontrado realmente satisface la condición.

La segunda:

$$
\forall y\,(P(y)\Rightarrow y=x)
$$

es la **cláusula de unicidad**: cualquier valor $y$ que también satisfaga $P$ debe coincidir con $x$.

Por tanto, la fórmula completa afirma que existe un valor y que ningún valor distinto puede satisfacer la misma condición.

---

### Existencia y unicidad en tres casos {#apm-t1-c03-e0192}
Trabajamos con valores enteros.

Clasifica cada condición según ocurra:

- ninguna solución;
- existencia sin unicidad;
- existencia única.

#### a)

$$
2x=1
$$

#### b)

$$
x^2=16
$$

#### c)

$$
3x=12
$$

#### Solución


#### a)

$$
2x=1
$$

no tiene solución entera.

Por tanto, no hay existencia.

#### b)

$$
x^2=16
$$

tiene al menos dos soluciones enteras:

$$
x=4
\qquad\text{y}\qquad
x=-4.
$$

Por tanto, hay existencia, pero no unicidad.

#### c)

$$
3x=12
$$

tiene la solución:

$$
x=4.
$$

Si un entero $y$ satisface:

$$
3y=12,
$$

entonces, dividiendo por $3$:

$$
y=4.
$$

Por tanto, hay existencia única.

---

### Expandir \(\exists!\) {#apm-t1-c03-e0193}
Expande completamente:

$$
\exists!x\,P(x)
$$

utilizando solo:

$$
\exists,
\qquad
\forall,
\qquad
\land,
\qquad
\Rightarrow,
\qquad
=.
$$

Después explica la expansión en prosa.

#### Solución


La expansión es:

$$
\boxed{
\exists x\,\bigl(
P(x)\land
\forall y\,(P(y)\Rightarrow y=x)
\bigr).
}
$$

En prosa:

> «Existe un valor $x$ que satisface $P$, y todo valor $y$ que también satisface $P$ debe ser igual a $x$».

La primera parte afirma existencia.

La segunda afirma unicidad.

---

### Formular una existencia única {#apm-t1-c03-e0194}
Trabajamos con valores enteros.

Escribe simbólicamente:

> «Existe un único entero cuyo doble es igual a $10$».

Después:

#### a)

escribe la forma abreviada;

#### b)

expándela sin utilizar $\exists!$;

#### c)

identifica el valor único.

#### Solución


#### a)

La forma abreviada es:

$$
\boxed{
\exists!x\,(2x=10).
}
$$

#### b)

La expansión es:

$$
\boxed{
\exists x\,\bigl(
2x=10
\land
\forall y\,(2y=10\Rightarrow y=x)
\bigr).
}
$$

#### c)

El valor:

$$
x=5
$$

satisface:

$$
2\cdot5=10.
$$

Si:

$$
2y=10,
$$

entonces, dividiendo por $2$:

$$
y=5.
$$

Por tanto, el único entero que satisface la condición es:

$$
\boxed{5}.
$$

---

## Síntesis

La afirmación:

$$
\exists x\,P(x)
$$

dice:

> «Hay al menos uno».

La afirmación:

$$
\exists!x\,P(x)
$$

dice:

> «Hay exactamente uno».

La segunda abrevia:

$$

\exists x\,\bigl(
P(x)\land
\forall y\,(P(y)\Rightarrow y=x)
\bigr).

$$

Su estructura contiene dos exigencias:

$$

\text{existencia}
+
\text{unicidad}.

$$

La existencia exige un valor que satisfaga la condición.

La unicidad exige que cualquier otro valor que también la satisfaga coincida con el primero.

Por tanto:

$$

\text{encontrar un ejemplo}
\neq
\text{establecer unicidad}.

$$

También vimos que la unicidad depende del dominio. Con esto ya disponemos de casi todo el vocabulario cuantificacional elemental del capítulo.

Las dos secciones finales se dedicarán a **integrarlo**.

## Hacia la sección siguiente

Una fórmula como:

$$
\neg\forall x\,\exists y\,R(x,y)
$$

combina:

- negación;
- dos cuantificadores;
- alcance;
- orden.

Ya sabemos qué significa cada pieza por separado. El siguiente paso será aprender a leer y transformar fórmulas de este tipo sin perder su estructura.

## §11. Leer y negar fórmulas cuantificadas largas

Hasta ahora hemos estudiado por separado:

- negación;
- cuantificadores;
- alcance;
- variables libres y ligadas;
- orden;
- conectivos proposicionales.

Ahora debemos hacerlos trabajar juntos. Consideremos:

$$
\neg\forall x\,\exists y\,R(x,y).
$$

Esta fórmula contiene tres capas lógicas:

1. una negación exterior;
2. un cuantificador universal;
3. un cuantificador existencial.

No conviene intentar transformarla «de un vistazo». La estrategia será leer y operar **desde fuera hacia dentro**, una capa a la vez.

Aplicando [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007) al cuantificador exterior:

$$
\neg\forall x\,\exists y\,R(x,y)
\equiv
\exists x\,\neg\exists y\,R(x,y).
$$

Aplicamos de nuevo [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007):

$$
\exists x\,\neg\exists y\,R(x,y)
\equiv
\exists x\,\forall y\,\neg R(x,y).
$$

Así obtenemos:

$$
\boxed{
\neg\forall x\,\exists y\,R(x,y)
\equiv
\exists x\,\forall y\,\neg R(x,y).
}
$$

La transformación no intercambia arbitrariamente cuantificadores. Cada cambio ocurre porque una negación atraviesa un cuantificador.

---

### 11.1 Leer la estructura antes de transformar

Ante una fórmula como:

$$
\neg\forall x\,\exists y\,R(x,y),
$$

conviene responder primero:

#### ¿Cuál es la operación exterior?

La negación:

$$
\neg.
$$

#### ¿Qué fórmula está siendo negada?

$$
\forall x\,\exists y\,R(x,y).
$$

#### ¿Cuál es el cuantificador exterior de esa fórmula?

$$
\forall x.
$$

#### ¿Qué queda dentro de su alcance?

$$
\exists y\,R(x,y).
$$

Solo después de identificar esta estructura comenzamos la transformación.

Podemos resumir:

$$

\text{leer primero}
\longrightarrow
\text{transformar después}.

$$

---

### 11.2 Una negación atraviesa los cuantificadores uno por uno

Recordemos [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007):

$$
\neg\forall x\,P(x)
\equiv
\exists x\,\neg P(x),
$$

$$
\neg\exists x\,P(x)
\equiv
\forall x\,\neg P(x).
$$

La negación cambia el tipo de cuantificador:

$$
\forall
\longleftrightarrow
\exists
$$

y continúa hacia el interior. Por tanto:

$$
\neg\forall x\,\exists y\,R(x,y)
$$

no se transforma directamente por una regla nueva. Usamos dos veces una regla ya conocida.

#### Primer paso

Tomamos como condición completa:

$$
P(x):\quad \exists y\,R(x,y).
$$

Entonces:

$$
\neg\forall x\,P(x)
\equiv
\exists x\,\neg P(x).
$$

Por tanto:

$$
\neg\forall x\,\exists y\,R(x,y)
\equiv
\exists x\,\neg\exists y\,R(x,y).
$$

#### Segundo paso

Ahora la negación exterior alcanza:

$$
\exists y\,R(x,y).
$$

Aplicamos nuevamente [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007):

$$
\neg\exists y\,R(x,y)
\equiv
\forall y\,\neg R(x,y).
$$

Así:

$$
\exists x\,\neg\exists y\,R(x,y)
\equiv
\exists x\,\forall y\,\neg R(x,y).
$$

---

### 11.3 El orden final no se elige libremente

Observemos qué ocurrió:

$$
\forall x\,\exists y
$$

se convirtió, bajo negación, en:

$$
\exists x\,\forall y.
$$

Pero no hemos intercambiado:

$$
x
\qquad\text{y}\qquad
y.
$$

El orden de las variables sigue siendo el mismo.

Lo que cambió fue el tipo de cada cuantificador al ser atravesado por la negación.

Por tanto:

$$

\neg\forall x\,\exists y
\quad\longrightarrow\quad
\exists x\,\forall y\,\neg

$$

y no:

$$
\forall y\,\exists x\,\neg
$$

ni ninguna otra permutación arbitraria. La regla práctica es:

$$

\text{conservar el orden de las variables}
\quad+\quad
\text{cambiar cada cuantificador atravesado por }\neg.

$$

---

### 11.4 Llegar hasta el predicado

Una negación puede quedar finalmente delante de una condición elemental:

$$
\neg R(x,y).
$$

En ese punto ya no hay cuantificadores que atravesar.

Por ejemplo, $\neg\exists x\,\forall y\,R(x,y)$ se transforma:

$$
\neg\exists x\,\forall y\,R(x,y)
\equiv
\forall x\,\neg\forall y\,R(x,y)
$$

y después:

$$
\forall x\,\neg\forall y\,R(x,y)
\equiv
\forall x\,\exists y\,\neg R(x,y).
$$

Por tanto:

$$
\boxed{
\neg\exists x\,\forall y\,R(x,y)
\equiv
\forall x\,\exists y\,\neg R(x,y).
}
$$

De nuevo, la negación ha llegado hasta el predicado.

---

### 11.5 Cuando dentro hay conectivos

Consideremos:

$$
\neg\forall x\,\bigl(P(x)\Rightarrow Q(x)\bigr).
$$

Primero atravesamos el cuantificador:

$$
\neg\forall x\,\bigl(P(x)\Rightarrow Q(x)\bigr)
\equiv
\exists x\,\neg\bigl(P(x)\Rightarrow Q(x)\bigr).
$$

En [el capítulo 2](algebra-para-matematicos-capitulo-2-logica-proposicional-y-algebra-de-proposiciones.md) demostramos:

$$
\neg(A\Rightarrow B)
\equiv
A\land\neg B.
$$

Aplicándola:

$$
\exists x\,\neg\bigl(P(x)\Rightarrow Q(x)\bigr)
\equiv
\exists x\,\bigl(P(x)\land\neg Q(x)\bigr).
$$

Así:

$$
\boxed{
\neg\forall x\,\bigl(P(x)\Rightarrow Q(x)\bigr)
\equiv
\exists x\,\bigl(P(x)\land\neg Q(x)\bigr).
}
$$

En prosa:

> «No todo objeto que cumple $P$ cumple $Q$»

equivale a:

> «Existe al menos un objeto que cumple $P$ y no cumple $Q$».

Aquí se combinan una ley cuantificacional y una ley proposicional.

---

### 11.6 De Morgan dentro de una fórmula cuantificada

Consideremos:

$$
\neg\exists x\,\bigl(P(x)\land Q(x)\bigr).
$$

Primero negamos el cuantificador:

$$
\neg\exists x\,\bigl(P(x)\land Q(x)\bigr)
\equiv
\forall x\,\neg\bigl(P(x)\land Q(x)\bigr).
$$

Después aplicamos De Morgan:

$$
\neg\bigl(P(x)\land Q(x)\bigr)
\equiv
\neg P(x)\lor\neg Q(x).
$$

Por tanto:

$$
\boxed{
\neg\exists x\,\bigl(P(x)\land Q(x)\bigr)
\equiv
\forall x\,\bigl(\neg P(x)\lor\neg Q(x)\bigr).
}
$$

La transformación ocurre por capas:

$$
\boxed{
\text{cuantificador}
\longrightarrow
\text{conectivo}
\longrightarrow
\text{condiciones elementales}.
}
$$

---

### 11.7 Un protocolo de lectura y transformación

Cuando una fórmula cuantificada es larga, seguiremos este orden.

#### Paso 1 — Identificar la operación exterior

Puede ser:

- una negación;
- un cuantificador;
- un conectivo proposicional.

#### Paso 2 — Marcar el alcance

Preguntar qué parte de la fórmula controla esa operación.

#### Paso 3 — Aplicar una sola equivalencia

No saltar varias capas a la vez.

#### Paso 4 — Repetir desde la nueva operación exterior relevante

Si queda: $\neg\forall$ o $\neg\exists$, volver a usar [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007).

#### Paso 5 — Cuando la negación llegue a conectivos, usar las leyes de [el capítulo 2](algebra-para-matematicos-capitulo-2-logica-proposicional-y-algebra-de-proposiciones.md)

Por ejemplo:

$$
\neg(A\land B)
\equiv
\neg A\lor\neg B,
$$

$$
\neg(A\lor B)
\equiv
\neg A\land\neg B,
$$

$$
\neg(A\Rightarrow B)
\equiv
A\land\neg B.
$$

#### Paso 6 — Leer el resultado en prosa

Esto sirve como control semántico. El procedimiento puede resumirse:

$$
\boxed{
\text{estructura}
\longrightarrow
\text{una equivalencia}
\longrightarrow
\text{nueva estructura}
\longrightarrow
\cdots
\longrightarrow
\text{lectura final}.
}
$$

---

### 11.8 No cambiar más de lo que autoriza cada ley

Supongamos que partimos de:

$$
\neg\forall x\,\exists y\,R(x,y).
$$

Sería incorrecto escribir directamente:

$$
\forall x\,\exists y\,\neg R(x,y).
$$

¿Por qué?

Porque al negar:

$$
\forall x
$$

debemos cambiarlo por:

$$
\exists x.
$$

Y al negar:

$$
\exists y
$$

debemos cambiarlo por:

$$
\forall y.
$$

La transformación correcta es:

$$
\exists x\,\forall y\,\neg R(x,y).
$$

Una buena práctica es exigir que **cada cambio de símbolo tenga una razón identificable**.

Si un cuantificador cambia, debemos poder señalar qué negación lo atravesó.

Si un conectivo cambia, debemos poder señalar qué ley proposicional estamos usando.

---

### 11.9 Comprobación semántica con un dominio pequeño

Las equivalencias se justifican por las leyes ya demostradas.

Pero un ejemplo concreto puede ayudarnos a detectar errores.

Tomemos un dominio formado únicamente por los valores:

$$
0
\qquad\text{y}\qquad
1,
$$

y definamos:

$$
R(x,y):\quad x<y.
$$

Consideremos $\forall x\,\exists y\,R(x,y)$ Para:

$$
x=1,
$$

no hay ningún valor permitido de $y$ tal que:

$$
1<y.
$$

Por tanto, la afirmación universal-existencial es falsa. Su negación:

$$
\neg\forall x\,\exists y\,R(x,y)
$$

es verdadera. Ahora examinemos la forma equivalente:

$$
\exists x\,\forall y\,\neg R(x,y).
$$

Tomemos $x=1$ Para: $y=0$ y $y=1$, se cumple:

$$
\neg(1<y).
$$

La fórmula es verdadera. Las dos formas tienen el mismo valor de verdad, como corresponde.

Este ejemplo no reemplaza la derivación. Funciona como **control semántico**.

---

### 11.10 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-t1-c03-x0031}
**Ejemplo — Negar dos cuantificadores sin perder el orden**
:::

Partimos de:

$$
\neg\forall x\,\exists y\,R(x,y).
$$

Queremos llevar la negación hasta el predicado.

#### Paso 1 — Identificar la primera capa

La fórmula negada comienza con:

$$
\forall x.
$$

Aplicamos [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007):

$$
\neg\forall x\,\exists y\,R(x,y)
\equiv
\exists x\,\neg\exists y\,R(x,y).
$$

#### Paso 2 — Identificar la segunda capa

Ahora tenemos $\neg\exists y\,R(x,y)$. Aplicamos de nuevo [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007):

$$
\neg\exists y\,R(x,y)
\equiv
\forall y\,\neg R(x,y).
$$

Sustituyendo:

$$
\exists x\,\neg\exists y\,R(x,y)
\equiv
\exists x\,\forall y\,\neg R(x,y).
$$

#### Resultado

$$
\boxed{
\neg\forall x\,\exists y\,R(x,y)
\equiv
\exists x\,\forall y\,\neg R(x,y).
}
$$

#### Lectura de la primera fórmula

> «No es verdad que para todo $x$ exista algún $y$ para el cual se cumple $R(x,y)$».

#### Lectura de la segunda

> «Existe algún $x$ tal que, para todo $y$, no se cumple $R(x,y)$».

Las dos frases expresan la misma situación:

> hay al menos un valor de $x$ para el cual ningún valor de $y$ consigue hacer verdadera $R(x,y)$.

#### Qué no hicimos

No intercambiamos:

$$
x
\qquad\text{y}\qquad
y.
$$

No inventamos una nueva regla. Aplicamos dos veces:

$$
\neg\forall
\equiv
\exists\neg
$$

o:

$$
\neg\exists
\equiv
\forall\neg,
$$

según correspondía.

---
## Ejercicios

### Negar dos cuantificadores {#apm-t1-c03-e0195}
Niega y transforma completamente:

$$
\forall x\,\exists y\,R(x,y).
$$

La respuesta final debe tener la negación aplicada directamente al predicado.

#### Solución


Comenzamos:

$$
\neg\forall x\,\exists y\,R(x,y).
$$

Por [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007):

$$
\neg\forall x\,\exists y\,R(x,y)
\equiv
\exists x\,\neg\exists y\,R(x,y).
$$

Aplicamos nuevamente [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007):

$$
\neg\exists y\,R(x,y)
\equiv
\forall y\,\neg R(x,y).
$$

Por tanto:

$$
\boxed{
\neg\forall x\,\exists y\,R(x,y)
\equiv
\exists x\,\forall y\,\neg R(x,y).
}
$$

---

### Negar un cuantificador y una conjunción {#apm-t1-c03-e0196}
Niega completamente:

$$
\exists x\,\bigl(P(x)\land Q(x)\bigr).
$$

#### Solución


Partimos de:

$$
\neg\exists x\,\bigl(P(x)\land Q(x)\bigr).
$$

Por [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007):

$$
\neg\exists x\,\bigl(P(x)\land Q(x)\bigr)
\equiv
\forall x\,\neg\bigl(P(x)\land Q(x)\bigr).
$$

Aplicamos De Morgan:

$$
\neg\bigl(P(x)\land Q(x)\bigr)
\equiv
\neg P(x)\lor\neg Q(x).
$$

Por tanto:

$$
\boxed{
\neg\exists x\,\bigl(P(x)\land Q(x)\bigr)
\equiv
\forall x\,\bigl(\neg P(x)\lor\neg Q(x)\bigr).
}
$$

---

### Justificar cada cambio {#apm-t1-c03-e0197}
Explica cada paso de:

$$
\neg\exists x\,\forall y\,P(x,y)
\equiv
\forall x\,\exists y\,\neg P(x,y).
$$

#### Solución


Comenzamos con:

$$
\neg\exists x\,\forall y\,P(x,y).
$$

La negación alcanza primero al cuantificador:

$$
\exists x.
$$

Por [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007):

$$
\neg\exists x\,\forall y\,P(x,y)
\equiv
\forall x\,\neg\forall y\,P(x,y).
$$

Ahora la negación alcanza al cuantificador:

$$
\forall y.
$$

Aplicamos nuevamente [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007):

$$
\neg\forall y\,P(x,y)
\equiv
\exists y\,\neg P(x,y).
$$

Así:

$$
\forall x\,\neg\forall y\,P(x,y)
\equiv
\forall x\,\exists y\,\neg P(x,y).
$$

Por tanto:

$$
\boxed{
\neg\exists x\,\forall y\,P(x,y)
\equiv
\forall x\,\exists y\,\neg P(x,y).
}
$$

Cada cuantificador cambió porque una negación lo atravesó.

El orden de las variables:

$$
x,\ y
$$

se conservó.

---

### Detectar una negación incorrecta {#apm-t1-c03-e0198}
Trabajamos con valores enteros y definimos:

$$
R(x,y):\quad y=x.
$$

Una persona afirma que:

$$
\neg\forall x\,\exists y\,R(x,y)
\equiv
\forall x\,\exists y\,\neg R(x,y).
$$

Demuestra mediante esta interpretación concreta que la equivalencia propuesta es falsa.

#### Solución


Primero analizamos:

$$
\forall x\,\exists y\,R(x,y).
$$

Como:

$$
R(x,y):\quad y=x,
$$

para cada entero $x$ podemos elegir:

$$
y=x.
$$

Por tanto:

$$
\forall x\,\exists y\,R(x,y)
$$

es verdadera.

Su negación:

$$
\neg\forall x\,\exists y\,R(x,y)
$$

es, entonces, falsa.

Ahora evaluemos la fórmula propuesta como equivalente:

$$
\forall x\,\exists y\,\neg R(x,y).
$$

Esto dice:

> «Para todo entero $x$, existe un entero $y$ distinto de $x$».

Es verdadera.

Para cada entero $x$ podemos tomar:

$$
y=x+1.
$$

Entonces:

$$
y\ne x.
$$

Hemos obtenido:

- lado izquierdo: falso;
- lado derecho: verdadero.

Por tanto:

$$
\boxed{
\neg\forall x\,\exists y\,R(x,y)
\not\equiv
\forall x\,\exists y\,\neg R(x,y).
}
$$

La transformación incorrecta no cambió los tipos de cuantificador como exige [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007).

---

### Transformar y volver a la prosa {#apm-t1-c03-e0199}
El dominio está previamente fijado.

Niega completamente:

$$
\exists x\,\forall y\,\bigl(P(x)\lor Q(y)\bigr).
$$

Después expresa la fórmula final en prosa.

#### Solución


Partimos de:

$$
\neg\exists x\,\forall y\,\bigl(P(x)\lor Q(y)\bigr).
$$

Primero:

$$
\neg\exists x\,\forall y\,\bigl(P(x)\lor Q(y)\bigr)
\equiv
\forall x\,\neg\forall y\,\bigl(P(x)\lor Q(y)\bigr).
$$

Después:

$$
\forall x\,\neg\forall y\,\bigl(P(x)\lor Q(y)\bigr)
\equiv
\forall x\,\exists y\,\neg\bigl(P(x)\lor Q(y)\bigr).
$$

Aplicamos De Morgan:

$$
\neg\bigl(P(x)\lor Q(y)\bigr)
\equiv
\neg P(x)\land\neg Q(y).
$$

Por tanto:

$$
\boxed{
\neg\exists x\,\forall y\,\bigl(P(x)\lor Q(y)\bigr)
\equiv
\forall x\,\exists y\,\bigl(\neg P(x)\land\neg Q(y)\bigr).
}
$$

Una lectura en prosa de la fórmula final es:

> «Para todo valor de $x$, existe al menos un valor de $y$ tal que $x$ no cumple $P$ y $y$ no cumple $Q$».

La lectura conserva el orden:

$$
\forall x\,\exists y.
$$

---

### Tres capas y conectivos {#apm-t1-c03-e0200}
Niega completamente:

$$
\forall x\,\exists y\,\forall z\,
\bigl(
P(x,z)\Rightarrow(Q(y)\lor R(x,y,z))
\bigr).
$$

Muestra todas las equivalencias hasta que la negación haya llegado a las condiciones elementales.

#### Solución


Partimos de:

$$
\neg\forall x\,\exists y\,\forall z\,
\bigl(
P(x,z)\Rightarrow(Q(y)\lor R(x,y,z))
\bigr).
$$

#### Primera capa

Por [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007):

$$
\equiv
\exists x\,\neg\exists y\,\forall z\,
\bigl(
P(x,z)\Rightarrow(Q(y)\lor R(x,y,z))
\bigr).
$$

#### Segunda capa

De nuevo por [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007):

$$
\equiv
\exists x\,\forall y\,\neg\forall z\,
\bigl(
P(x,z)\Rightarrow(Q(y)\lor R(x,y,z))
\bigr).
$$

#### Tercera capa

Otra vez:

$$
\equiv
\exists x\,\forall y\,\exists z\,
\neg\bigl(
P(x,z)\Rightarrow(Q(y)\lor R(x,y,z))
\bigr).
$$

#### Negar la implicación

En [el capítulo 2](algebra-para-matematicos-capitulo-2-logica-proposicional-y-algebra-de-proposiciones.md) demostramos:

$$
\neg(A\Rightarrow B)
\equiv
A\land\neg B.
$$

Por tanto:

$$
\equiv
\exists x\,\forall y\,\exists z\,
\Bigl(
P(x,z)\land
\neg(Q(y)\lor R(x,y,z))
\Bigr).
$$

#### Aplicar De Morgan

$$
\neg(Q(y)\lor R(x,y,z))
\equiv
\neg Q(y)\land\neg R(x,y,z).
$$

Así:

$$
\equiv
\exists x\,\forall y\,\exists z\,
\Bigl(
P(x,z)\land
(\neg Q(y)\land\neg R(x,y,z))
\Bigr).
$$

Por asociatividad de la conjunción podemos escribir:

$$
\boxed{
\exists x\,\forall y\,\exists z\,
\bigl(
P(x,z)\land
\neg Q(y)\land
\neg R(x,y,z)
\bigr).
}
$$

#### Control de la estructura

Los cuantificadores originales eran:

$$
\forall x\,\exists y\,\forall z.
$$

Al atravesarlos la negación se convirtieron, en el mismo orden, en:

$$
\exists x\,\forall y\,\exists z.
$$

Después la negación alcanzó la implicación y finalmente las condiciones elementales.

No se permutó ninguna variable.

---

## Síntesis

Una fórmula cuantificada larga debe transformarse por **capas**. El principio básico es:

$$

\text{leer desde fuera hacia dentro}

$$

y aplicar una sola equivalencia en cada paso. Cuando una negación atraviesa cuantificadores:

$$

\forall
\longleftrightarrow
\exists

$$

mientras el orden de las variables se conserva. Cuando la negación alcanza conectivos proposicionales, utilizamos las leyes ya demostradas en [el capítulo 2](algebra-para-matematicos-capitulo-2-logica-proposicional-y-algebra-de-proposiciones.md).

Así, $\neg\forall x\,\exists y\,R(x,y)$ se transforma en:

$$

\exists x\,\forall y\,\neg R(x,y).

$$

Y una fórmula más compleja puede exigir una cadena como:

$$

\text{cuantificadores}
\longrightarrow
\text{conectivos}
\longrightarrow
\text{condiciones elementales}.

$$

El criterio de seguridad es sencillo:

> **cada cambio de símbolo debe poder justificarse por una equivalencia ya demostrada.**

Nos queda una última tarea. Ya sabemos construir, leer, traducir y negar fórmulas cuantificadas.

Ahora debemos aprender a detectar rápidamente cuándo una fórmula o una traducción está mal formada conceptualmente.

## Hacia la sección siguiente

Los errores más frecuentes ya han aparecido a lo largo del capítulo:

- olvidar el dominio;
- confundir $\forall$ con $\exists$;
- intercambiar cuantificadores mixtos;
- dejar una variable libre sin advertirlo;
- interpretar «no todos» como «ninguno»;
- confundir existencia con unicidad.

La sección final reunirá estos errores y los convertirá en una herramienta de diagnóstico.

## §12. Diagnosticar errores y leer lenguaje matemático

A lo largo de este capítulo construimos un lenguaje para responder preguntas cada vez más precisas:

- ¿qué variable puede cambiar?;
- ¿sobre qué dominio cambia?;
- ¿qué afirma un cuantificador?;
- ¿hasta dónde llega?;
- ¿qué apariciones quedan libres?;
- ¿en qué orden se hacen las elecciones?;
- ¿qué significa negar la afirmación?;
- ¿hay al menos un valor o exactamente uno?;
- ¿qué símbolos permanecen fijos como parámetros?

La última tarea no consiste en añadir una nueva definición.

Consiste en aprender a **diagnosticar**. En matemáticas, muchas fórmulas incorrectas parecen plausibles porque contienen los símbolos adecuados, pero los organizan de manera equivocada.

Por ejemplo, una escritura puede contener:

$$
\forall,\qquad
\exists,\qquad
R(x,y),
$$

y aun así expresar algo distinto de la frase que pretendíamos traducir.

Por eso la lectura matemática debe incluir una pregunta crítica:

> **¿La fórmula dice realmente lo que creemos que dice?**

---

### 12.1 Ocho errores que debemos poder detectar

Al cerrar el capítulo, debemos reconocer al menos estos ocho problemas.

#### 1. Dominio omitido

La fórmula $\exists x\,(2x=1)$ no tiene un significado matemático suficientemente determinado si no sabemos qué valores están permitidos para $x$.

Sobre los enteros es falsa. Sobre los racionales es verdadera.

El dominio forma parte de la afirmación.

#### 2. Universal y existencial confundidos

No es lo mismo:

$$
\forall x\,P(x)
$$

que:

$$
\exists x\,P(x).
$$

La primera exige ausencia de excepciones. La segunda exige al menos un caso favorable.

#### 3. «No todos» confundido con «todos no»

No es lo mismo:

$$
\neg\forall x\,P(x)
$$

que:

$$
\forall x\,\neg P(x).
$$

La primera dice:

> «hay al menos una excepción».

La segunda dice:

> «todos incumplen la condición».

#### 4. Orden de cuantificadores alterado

En general:

$$
\forall x\,\exists y\,R(x,y)
\not\equiv
\exists y\,\forall x\,R(x,y).
$$

La primera permite que $y$ se ajuste a $x$.

La segunda exige un mismo $y$ para todos los valores de $x$.

#### 5. Aparición libre no advertida

En:

$$
\forall x\,R(x,y),
$$

$x$ está ligada, pero $y$ permanece libre. La fórmula no está cerrada.

#### 6. Alcance incorrecto

No es lo mismo:

$$
\forall x\,(P(x)\Rightarrow Q)
$$

que:

$$
(\forall x\,P(x))\Rightarrow Q.
$$

Los paréntesis determinan qué parte de la fórmula controla el cuantificador.

#### 7. Existencia confundida con unicidad

De:

$$
\exists x\,P(x)
$$

no podemos concluir:

$$
\exists!x\,P(x).
$$

Encontrar un testigo no demuestra que sea el único.

#### 8. Cuantificación universal implícita peligrosa

Una expresión como:

$$
x^2\ge0
$$

puede aparecer en prosa matemática con la intención informal de decir:

> «para todo valor permitido de $x$, $x^2\ge0$».

Pero en este capítulo no adoptamos esa cuantificación implícita como escritura canónica.

Si queremos afirmar universalidad, escribimos:

$$
\forall x\,(x^2\ge0)
$$

después de fijar el dominio. La escritura explícita evita que una aparición libre sea interpretada como cuantificada sin justificación.

---

### 12.2 Un diagnóstico debe identificar el tipo de error

Decir:

> «La fórmula está mal»

no basta. Debemos poder explicar **qué** está mal. Por ejemplo, si alguien traduce:

> «Para cada entero $x$, existe un entero $y$ tal que $y=x+1$»

como:

$$
\exists y\,\forall x\,(y=x+1),
$$

el problema no es simplemente que «los símbolos estén cambiados».

El diagnóstico preciso es:

> **el orden de los cuantificadores fue invertido.**

La reparación es:

$$
\boxed{
\forall x\,\exists y\,(y=x+1).
}
$$

La capacidad de nombrar el error ayuda a corregirlo sin modificar otras partes que sí estaban bien.

---

### 12.3 Diagnosticar por capas

Ante una fórmula dudosa podemos revisar, en este orden:

#### Capa 1 — Contexto

- ¿Está declarado el dominio?
- ¿Hay parámetros fijados?

#### Capa 2 — Variables

- ¿Qué letras pueden variar?
- ¿Qué apariciones están libres?
- ¿Qué apariciones están ligadas?

#### Capa 3 — Cuantificadores

- ¿Corresponde $\forall$ o $\exists$?
- ¿El orden coincide con la prosa?
- ¿Se está afirmando existencia o existencia única?

#### Capa 4 — Alcance

- ¿Los paréntesis reflejan correctamente qué controla cada cuantificador?
- ¿La negación alcanza la parte correcta?

#### Capa 5 — Conectivos

- ¿«todo $P$ es $Q$» fue traducido mediante implicación?
- ¿«algún $P$ es $Q$» fue traducido mediante conjunción?
- ¿La negación de los conectivos se hizo con las leyes correctas?

#### Capa 6 — Lectura inversa

Finalmente:

> «Si leo la fórmula resultante en prosa, ¿recupero la afirmación original?»

Podemos condensarlo así:

$$
\boxed{
\text{contexto}
\to
\text{variables}
\to
\text{cuantificadores}
\to
\text{alcance}
\to
\text{conectivos}
\to
\text{lectura inversa}.
}
$$

---

### 12.4 El dominio puede revelar un error invisible

Consideremos $\exists x\,(2x=3)$. Sin dominio, no podemos decidir qué afirma exactamente.

Si trabajamos con enteros, la afirmación es falsa. Si trabajamos con racionales, es verdadera, porque:

$$
x=\frac32
$$

es un valor permitido y satisface:

$$
2\cdot\frac32=3.
$$

El error no está dentro de los paréntesis. Tampoco está en el cuantificador.

Está en la información que falta **antes** de la fórmula.

Esto muestra que el diagnóstico lógico no se limita a inspeccionar símbolos.

También debemos revisar el contexto que les da significado.

---

### 12.5 Las variables libres son una señal de alarma

Supongamos que queremos expresar una proposición acerca de dos variables y escribimos:

$$
\forall x\,R(x,y).
$$

La aparición de $y$ permanece libre. Eso no significa automáticamente que la fórmula sea inútil.

Podría ocurrir que $y$ hubiese sido fijada como parámetro en el contexto.

Pero si no existe tal declaración, la fórmula todavía depende de un valor no fijado.

Por tanto, ante una variable libre debemos preguntar:

> **¿Debe ser cuantificada o fue fijada explícitamente por el contexto?**

No debemos corregirla de manera automática. Podrían ser apropiadas, según la intención, fórmulas tan distintas como:

$$
\forall y\,\forall x\,R(x,y),
$$

$$
\exists y\,\forall x\,R(x,y),
$$

o simplemente:

$$
\forall x\,R(x,y)
$$

si $y$ ha sido declarada como parámetro. El diagnóstico debe recuperar primero la intención.

---

### 12.6 Un contraejemplo puede detectar una traducción equivocada

Supongamos que alguien afirma:

$$
\forall x\,\exists y\,R(x,y)
\equiv
\exists y\,\forall x\,R(x,y).
$$

Para mostrar que la equivalencia general es falsa no necesitamos analizar todos los predicados posibles.

Basta una interpretación donde los dos lados tengan valores de verdad distintos.

Tomemos, sobre los enteros:

$$
R(x,y):\quad y=x+1.
$$

Entonces $\forall x\,\exists y\,(y=x+1)$ es verdadera.

Pero:

$$
\exists y\,\forall x\,(y=x+1)
$$

es falsa. Así detectamos que intercambiar cuantificadores mixtos no es una transformación válida en general.

El contraejemplo funciona aquí como control semántico de una traducción o equivalencia propuesta.

---

### 12.7 Existencia no autoriza el singular

Consideremos, sobre los enteros:

$$
x^2=4.
$$

Podemos encontrar:

$$
x=2.
$$

Eso confirma:

$$
\exists x\,(x^2=4).
$$

Pero también:

$$
x=-2
$$

satisface la condición. Sería incorrecto pasar de:

> «hemos encontrado una solución»

a:

> «hemos encontrado la única solución».

La fórmula $\exists!x\,(x^2=4)$ es falsa sobre los enteros. El diagnóstico es:

> **se confundió existencia con unicidad.**

---

### 12.8 No corregir una fórmula antes de reconstruir la intención

Una misma fórmula defectuosa puede admitir varias reparaciones. Consideremos $\forall x\,R(x,y)$, sin más contexto.

Podríamos sentir la tentación de añadir:

$$
\forall y.
$$

Pero quizá la intención era:

> «Existe un $y$ que funciona para todo $x$».

Entonces la reparación correcta sería:

$$
\exists y\,\forall x\,R(x,y).
$$

O quizá $y$ debía ser un parámetro fijado previamente.

En ese caso no habría que cuantificarla. Por tanto:

$$

\text{diagnosticar}
\neq
\text{añadir símbolos hasta cerrar la fórmula}.

$$

Primero reconstruimos el significado pretendido. Después reparamos la escritura.

---

### 12.9 La lectura en prosa es una prueba de control

Supongamos que hemos escrito:

$$
\exists y\,\forall x\,(x+y=0).
$$

Leamos:

> «Existe un entero $y$ tal que, para todo entero $x$, $x+y=0$».

Si nuestra intención era:

> «Para cada entero $x$ existe un entero $y$ tal que $x+y=0$»,

la lectura inversa revela inmediatamente que hemos escrito otra cosa.

La fórmula correcta era:

$$
\forall x\,\exists y\,(x+y=0).
$$

Por eso una buena práctica final es siempre:

$$
\boxed{
\text{prosa}
\longrightarrow
\text{fórmula}
\longrightarrow
\text{prosa}.
}
$$

Si la frase recuperada no coincide con la inicial, hay un error estructural.

---

### 12.10 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-t1-c03-x0032}
**Ejemplo — Expediente de tres errores**
:::

Queremos expresar la afirmación:

> «Para cada entero $x$, existe un entero $y$ tal que $x+y=0$».

La traducción correcta es:

$$

\forall x\,\exists y\,(x+y=0),

$$

con dominio de los enteros. Examinemos tres formulaciones defectuosas.

#### Formulación A

$$
\forall x\,\exists y\,(x+y=0)
$$

sin declarar ningún dominio.

##### Diagnóstico

Los cuantificadores y su orden coinciden con la frase, pero falta información esencial:

> ¿qué valores están permitidos para $x$ e $y$?

##### Reparación

Declaramos:

> «El dominio de $x$ y de $y$ es el de los enteros».

La fórmula queda entonces correctamente interpretada.

---

#### Formulación B

$$
\exists y\,\forall x\,(x+y=0).
$$

##### Diagnóstico

El dominio puede estar bien declarado y las dos variables están ligadas.

El error es otro:

> **se invirtió el orden de los cuantificadores.**

La fórmula afirma:

> «Hay un mismo entero $y$ que sumado con todo entero $x$ da cero».

Eso no es lo que decía la frase original.

##### Reparación

Restauramos el orden:

$$
\boxed{
\forall x\,\exists y\,(x+y=0).
}
$$

---

#### Formulación C

$$
\forall x\,(x+y=0).
$$

##### Diagnóstico

La aparición de:

$$
y
$$

queda libre. La frase original decía:

> «existe un entero $y$»

para cada $x$. Por tanto, falta el cuantificador existencial correspondiente.

##### Reparación

Escribimos:

$$
\boxed{
\forall x\,\exists y\,(x+y=0).
}
$$

---

#### Control semántico

La fórmula correcta es verdadera sobre los enteros. Para cada:

$$
x,
$$

podemos elegir:

$$
y=-x.
$$

Entonces:

$$
x+(-x)=0.
$$

#### Resultado del expediente

Los tres errores eran diferentes:

1. **A:** dominio omitido;
2. **B:** orden de cuantificadores alterado;
3. **C:** aparición libre no advertida.

La reparación correcta apareció solo después de identificar con precisión el problema de cada caso.

---

## Ejercicios

### El dominio que falta {#apm-t1-c03-e0201}
Considera:

$$
\exists x\,(2x=1).
$$

Una persona afirma:

> «La fórmula es verdadera».

Otra afirma:

> «La fórmula es falsa».

Explica por qué ninguna de las dos afirmaciones está suficientemente justificada mientras no se declare el dominio. Después compara los dominios de los enteros y de los racionales.

#### Solución


La fórmula:

$$
\exists x\,(2x=1)
$$

afirma que hay al menos un valor permitido de $x$ que satisface la ecuación.

Pero no sabemos todavía qué valores están permitidos.

#### Dominio de los enteros

No existe un entero:

$$
x
$$

tal que:

$$
2x=1.
$$

Por tanto, la fórmula es falsa.

#### Dominio de los racionales

Podemos tomar:

$$
x=\frac12.
$$

Entonces:

$$
2\cdot\frac12=1.
$$

Por tanto, la fórmula es verdadera.

Así, el diagnóstico correcto es:

$$
\boxed{
\text{falta declarar el dominio}.
}
$$

---

### «No todos» no es «todos no» {#apm-t1-c03-e0202}
El dominio contiene únicamente los valores:

$$
0
\qquad\text{y}\qquad
1.
$$

Definimos:

$$
P(x):\quad x=0.
$$

Compara:

$$
\neg\forall x\,P(x)
$$

con:

$$
\forall x\,\neg P(x).
$$

Determina el valor de verdad de cada una y explica el error de tratarlas como equivalentes.

#### Solución


Primero:

$$
\forall x\,P(x)
$$

afirma que tanto:

$$
0
$$

como:

$$
1
$$

son iguales a cero.

Eso es falso.

Por tanto:

$$
\neg\forall x\,P(x)
$$

es verdadera.

Ahora consideremos:

$$
\forall x\,\neg P(x).
$$

Esta fórmula afirma que ninguno de los dos valores es igual a cero.

Pero:

$$
0=0.
$$

Por tanto, la fórmula es falsa.

Así:

$$
\boxed{
\neg\forall x\,P(x)
\not\equiv
\forall x\,\neg P(x).
}
$$

«No todos» significa que hay al menos una excepción.

«Todos no» significa que todos incumplen la condición.

---

### La variable que quedó libre {#apm-t1-c03-e0203}
Considera:

$$
\forall x\,R(x,y).
$$

No se ha declarado ningún parámetro.

#### a)

Clasifica las apariciones de $x$ y $y$.

#### b)

Explica por qué la fórmula no está cerrada.

#### c)

¿Por qué no podemos decidir automáticamente si la reparación correcta es añadir $\forall y$ o $\exists y$?

#### Solución


#### a)

Las apariciones de:

$$
x
$$

están ligadas por:

$$
\forall x.
$$

La aparición de:

$$
y
$$

está libre porque no se encuentra bajo ningún cuantificador que cuantifique $y$.

#### b)

Una fórmula cerrada no contiene apariciones libres.

Como $y$ permanece libre:

$$
\forall x\,R(x,y)
$$

no está cerrada.

#### c)

No conocemos la afirmación que se pretendía expresar.

Podría querer decir:

> «Para todo $y$ y para todo $x$, se cumple $R(x,y)$»,

en cuyo caso escribiríamos:

$$
\forall y\,\forall x\,R(x,y).
$$

Pero también podría querer decir:

> «Existe un $y$ que funciona para todo $x$»,

en cuyo caso escribiríamos:

$$
\exists y\,\forall x\,R(x,y).
$$

Incluso podría ocurrir que $y$ debiera ser fijada como parámetro.

Por tanto, primero debemos reconstruir la intención y solo después reparar la fórmula.

---

### Refutar una inversión de cuantificadores {#apm-t1-c03-e0204}
Trabajamos con valores enteros y definimos:

$$
R(x,y):\quad y=x+1.
$$

Una persona afirma que:

$$
\forall x\,\exists y\,R(x,y)
$$

y:

$$
\exists y\,\forall x\,R(x,y)
$$

son equivalentes porque «usan los mismos símbolos».

Refuta la afirmación.

#### Solución


Consideremos primero:

$$
\forall x\,\exists y\,(y=x+1).
$$

Para cualquier entero $x$, podemos elegir:

$$
y=x+1.
$$

Por tanto, la fórmula es verdadera.

Ahora:

$$
\exists y\,\forall x\,(y=x+1)
$$

exigiría un único entero $y$ que funcionara para todos los enteros $x$.

Eso es imposible.

Para cualquier entero propuesto como $y$, tomemos:

$$
x=y.
$$

La condición exigiría:

$$
y=y+1,
$$

que es falsa.

Por tanto:

- la primera fórmula es verdadera;
- la segunda es falsa.

Así:

$$
\boxed{
\forall x\,\exists y\,R(x,y)
\not\equiv
\exists y\,\forall x\,R(x,y).
}
$$

El contraejemplo muestra que los cuantificadores mixtos no pueden intercambiarse en general.

---

### Existencia no implica unicidad {#apm-t1-c03-e0205}
Trabajamos con valores enteros.

Una persona observa que:

$$
2^2=4
$$

y concluye:

$$
\exists!x\,(x^2=4).
$$

Refuta la conclusión y explica exactamente qué parte del razonamiento sí es válida.

#### Solución


El cálculo:

$$
2^2=4
$$

muestra que:

$$
x=2
$$

es un testigo.

Por tanto, sí podemos concluir:

$$
\exists x\,(x^2=4).
$$

Pero también:

$$
(-2)^2=4.
$$

Tenemos dos valores distintos:

$$
2\ne-2
$$

que satisfacen la condición.

Por tanto:

$$
\exists!x\,(x^2=4)
$$

es falsa.

La parte válida del razonamiento establece **existencia**.

El error consiste en inferir **unicidad** a partir de un solo testigo.

---

### Diagnóstico integral {#apm-t1-c03-e0206}
Trabajamos con valores enteros.

Queremos expresar:

> «No es verdad que para cada entero $x$ exista un entero $y$ tal que $x+y=0$».

Una persona propone:

$$
\forall x\,\exists y\,(x+y\ne0).
$$

Otra propone:

$$
\exists y\,\forall x\,(x+y\ne0).
$$

#### a)

Escribe primero la traducción directa correcta de la frase, conservando la negación exterior.

#### b)

Transforma completamente esa negación mediante [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007).

#### c)

Diagnostica el error de la primera propuesta.

#### d)

Diagnostica el error de la segunda propuesta.

#### e)

Determina el valor de verdad de la afirmación original sobre los enteros.

#### f)

Explica qué información tuviste que controlar para resolver correctamente todo el problema.

#### Solución


#### a)

La frase interior es:

> «Para cada entero $x$, existe un entero $y$ tal que $x+y=0$».

Eso se escribe:

$$
\forall x\,\exists y\,(x+y=0).
$$

La frase completa niega esa afirmación.

Por tanto:

$$
\boxed{
\neg\forall x\,\exists y\,(x+y=0).
}
$$

#### b)

Aplicamos [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007) una capa a la vez:

$$
\neg\forall x\,\exists y\,(x+y=0)
\equiv
\exists x\,\neg\exists y\,(x+y=0).
$$

Después:

$$
\exists x\,\neg\exists y\,(x+y=0)
\equiv
\exists x\,\forall y\,\neg(x+y=0).
$$

Negando la igualdad:

$$
\boxed{
\exists x\,\forall y\,(x+y\ne0).
}
$$

#### c)

La primera propuesta era:

$$
\forall x\,\exists y\,(x+y\ne0).
$$

El error consiste en haber negado solamente la condición interna:

$$
x+y=0
$$

sin cambiar los cuantificadores atravesados por la negación.

La negación correcta de:

$$
\forall x\,\exists y
$$

produce:

$$
\exists x\,\forall y.
$$

#### d)

La segunda propuesta era:

$$
\exists y\,\forall x\,(x+y\ne0).
$$

Esta fórmula sí usa un existencial y un universal, pero **invierte el orden de las variables**.

La transformación correcta conserva:

$$
x
\quad\text{antes que}\quad
y.
$$

Por tanto, debe ser:

$$
\exists x\,\forall y\,(x+y\ne0).
$$

#### e)

La afirmación interior:

$$
\forall x\,\exists y\,(x+y=0)
$$

es verdadera sobre los enteros.

Para cada entero:

$$
x,
$$

podemos elegir:

$$
y=-x.
$$

Entonces:

$$
x+(-x)=0.
$$

Por tanto, su negación:

$$
\neg\forall x\,\exists y\,(x+y=0)
$$

es falsa.

La forma transformada:

$$
\exists x\,\forall y\,(x+y\ne0)
$$

también es falsa.

Para cualquier entero $x$, podemos elegir:

$$
y=-x,
$$

y entonces:

$$
x+y=0.
$$

#### f)

Para resolver el problema tuvimos que controlar:

- el dominio;
- las variables;
- el orden de los cuantificadores;
- el alcance de la negación;
- las leyes de negación de cuantificadores;
- la negación de la igualdad;
- la lectura en prosa;
- el valor de verdad final.

El diagnóstico integral puede resumirse:

$$
\boxed{
\text{contexto}
+
\text{estructura}
+
\text{equivalencias justificadas}
+
\text{control semántico}.
}
$$

---

## Síntesis del capítulo

Comenzamos con una escritura aparentemente sencilla:

$$
x+2=5.
$$

Descubrimos que no era todavía una proposición mientras el valor de $x$ permaneciera sin fijar.

Eso nos obligó a preguntar:

> ¿qué puede variar y sobre qué dominio?

A partir de ahí construimos el lenguaje de los predicados y de la cuantificación.

Aprendimos que:

$$
\forall x\,P(x)
$$

afirma que la condición se cumple para cada valor permitido, mientras:

$$
\exists x\,P(x)
$$

afirma que se cumple para al menos uno. La negación conectó ambos cuantificadores:

$$
\neg\forall x\,P(x)
\equiv
\exists x\,\neg P(x),
$$

$$
\neg\exists x\,P(x)
\equiv
\forall x\,\neg P(x).
$$

Después vimos que los cuantificadores tienen **alcance**, que las apariciones de variables pueden ser **libres** o **ligadas**, y que una fórmula es **cerrada** cuando no queda ninguna aparición libre.

El orden introdujo una nueva dimensión:

$$
\forall x\,\exists y\,R(x,y)
$$

no significa, en general, lo mismo que:

$$
\exists y\,\forall x\,R(x,y).
$$

En cambio:

$$
\forall x\,\forall y\,R(x,y)
\equiv
\forall y\,\forall x\,R(x,y),
$$

y:

$$
\exists x\,\exists y\,R(x,y)
\equiv
\exists y\,\exists x\,R(x,y).
$$

También aprendimos a traducir entre prosa y símbolos, a distinguir variables de parámetros fijados por contexto y a expresar existencia única mediante:

$$
\exists!x\,P(x).
$$

Finalmente integramos estas piezas para leer y negar fórmulas largas sin perder el orden ni el alcance.

El principio rector del capítulo puede escribirse ahora con mayor precisión:

$$

\text{variable}
+
\text{dominio}
+
\text{predicado}
+
\text{cuantificador}
=
\text{afirmación matemática precisa}.

$$

Pero esta fórmula todavía contiene una palabra que hemos tratado de manera deliberadamente preteórica:

> **dominio**.

Hasta ahora nos ha bastado decir:

> «el dominio es el de los enteros»

o:

> «el dominio contiene ciertos valores».

El siguiente capítulo dará el paso que falta. Construiremos el lenguaje de los **conjuntos** para poder hablar de colecciones matemáticas como objetos, expresar pertenencia y, después, estudiar de manera precisa las funciones.

## Hacia el capítulo siguiente

Pasaremos de preguntar:

> «¿sobre qué objetos puede variar $x$?»

a construir un lenguaje en el que podamos escribir y estudiar esos dominios como objetos matemáticos.

La transición será:

$$
\boxed{
\text{dominios y predicados}
\longrightarrow
\text{conjuntos}
\longrightarrow
\text{funciones}.
}
$$

**Capítulo 4. Conjuntos y funciones: lenguaje básico**
