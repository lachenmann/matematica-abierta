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
