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
