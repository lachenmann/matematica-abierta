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

::: {.ma-block .ma-definicion #apm-i-d0030}
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

::: {.ma-block .ma-definicion #apm-i-d0031}
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

::: {.ma-block .ma-definicion #apm-i-d0032}
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

::: {.ma-block .ma-definicion #apm-i-d0033}
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

::: {.ma-block .ma-observacion #apm-i-x0026}
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

### Identificar el alcance {#apm-i-e0165}
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

### Marcar apariciones libres y ligadas {#apm-i-e0166}
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

### La misma letra, dos situaciones {#apm-i-e0167}
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

### ¿Abierta o cerrada? {#apm-i-e0168}
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

### Por qué los paréntesis importan {#apm-i-e0169}
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

### Análisis completo {#apm-i-e0170}
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
