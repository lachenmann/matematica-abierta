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

::: {.ma-block .ma-definicion #apm-i-d0025}
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

::: {.ma-block .ma-definicion #apm-i-d0026}
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

::: {.ma-block .ma-observacion #apm-i-x0021}
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

### Proposición o fórmula abierta {#apm-i-e0135}
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

### No hay todavía un único valor de verdad {#apm-i-e0136}
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

### ¿Qué valores están permitidos? {#apm-i-e0137}
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

### Por qué debemos declarar el dominio {#apm-i-e0138}
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

### El dominio puede cambiar lo que encontramos {#apm-i-e0139}
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

### Análisis completo de una fórmula abierta {#apm-i-e0140}
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
