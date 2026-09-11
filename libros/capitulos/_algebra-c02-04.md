## §4. Bicondicional: «si y solo si»

La implicación expresa una dirección:

$$
P\Rightarrow Q.
$$

Podemos leerla como:

> «Si $P$, entonces $Q$».

Pero muchas afirmaciones matemáticas exigen dos direcciones simultáneas.

Queremos decir:

> «Si $P$, entonces $Q$»,

y también:

> «Si $Q$, entonces $P$».

Para expresar esa relación utilizaremos un nuevo conectivo:

$$
P\leftrightarrow Q.
$$

Se lee:

> «$P$ si y solo si $Q$».

La expresión «si y solo si» concentra dos exigencias: ninguna de las dos proposiciones puede ser verdadera mientras la otra sea falsa.

Por eso, la idea semántica fundamental será:

$$
\boxed{
P\leftrightarrow Q
\text{ es verdadera exactamente cuando }
P
\text{ y }
Q
\text{ tienen el mismo valor de verdad}.
}
$$

---

### 4.1 El bicondicional

::: {.ma-block .ma-definicion #apm-t1-c02-d0016}
**Definición — Bicondicional**

El **bicondicional** de dos fórmulas $P$ y $Q$ es la fórmula:

$$
P\leftrightarrow Q.
$$

Se lee «$P$ si y solo si $Q$». Es verdadera cuando $P$ y $Q$ tienen el mismo valor de verdad, y falsa cuando tienen valores de verdad diferentes.
:::

Su tabla es:

| $P$ | $Q$ | $P\leftrightarrow Q$ |
|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ |

La tabla tiene una simetría sencilla:

$$
\boxed{
\text{mismos valores}
\longrightarrow
\mathrm V;
\qquad
\text{valores distintos}
\longrightarrow
\mathrm F.
}
$$

::: {.ma-block .ma-observacion}
En evaluaciones concretas escribiremos, por brevedad, expresiones como:

$$
\mathrm F\leftrightarrow\mathrm F=\mathrm V.
$$

Esto significa que un bicondicional cuyas dos partes reciben $\mathrm F$ recibe el valor $\mathrm V$.
:::

---

### 4.2 Un bicondicional no exige que ambas partes sean verdaderas

Consideremos:

$$
p=\text{«9 es par»},
$$

$$
q=\text{«9 es múltiplo de 4»}.
$$

Ambas proposiciones son falsas:

$$
p=\mathrm F,
\qquad
q=\mathrm F.
$$

Sin embargo:

$$
p\leftrightarrow q
=
\mathrm F\leftrightarrow\mathrm F
=
\mathrm V.
$$

¿Por qué?

Porque el bicondicional compara los valores de verdad de sus dos componentes.

Aquí coinciden.

Por tanto, no debemos memorizar:

> «el bicondicional es verdadero cuando las dos proposiciones son verdaderas».

La regla correcta es:

::: {.ma-block .ma-intuicion}
**Idea clave**

El bicondicional es verdadero cuando sus dos componentes tienen **el mismo** valor de verdad.
:::

Esto incluye:

$$
(\mathrm V,\mathrm V)
$$

y:

$$
(\mathrm F,\mathrm F).
$$

---

### 4.3 Dos direcciones

La expresión:

> «$P$ si y solo si $Q$»

afirma dos direcciones:

1. si $P$, entonces $Q$;
2. si $Q$, entonces $P$.

Es decir, exige simultáneamente que sean aceptables:

$$
P\Rightarrow Q
$$

y:

$$
Q\Rightarrow P.
$$

Todavía no convertiremos esta observación en una ley simbólica de transformación. Más adelante, cuando hayamos definido formalmente la equivalencia lógica, podremos demostrar una fórmula precisa que relaciona el bicondicional con esas dos implicaciones.

Por ahora nos interesa la lectura:

$$
\boxed{
\text{«si y solo si»}
=
\text{dos direcciones exigidas simultáneamente}.
}
$$

---

### 4.4 Necesaria y suficiente

En la sección anterior aprendimos:

$$
P\Rightarrow Q
$$

significa que:

- $P$ es suficiente para $Q$;
- $Q$ es necesaria para $P$.

Ahora, si afirmamos:

$$
P\leftrightarrow Q,
$$

estamos exigiendo las dos direcciones.

Por tanto, podemos decir:

> **$P$ es una condición necesaria y suficiente para $Q$.**

También podemos invertir los nombres:

> **$Q$ es una condición necesaria y suficiente para $P$.**

La expresión «necesaria y suficiente» indica que ninguna de las dos condiciones es meramente unilateral.

Por ejemplo, si afirmamos:

> «Una figura concreta es un cuadrado si y solo si cumple cierta condición $Q$»,

estamos afirmando que:

- ser cuadrado basta para garantizar $Q$;
- cumplir $Q$ basta para garantizar que es cuadrado.

En este capítulo nos concentraremos en la estructura lógica de esta expresión, no en caracterizaciones geométricas particulares.

---

### 4.5 «Si y solo si» frente a «solo si»

Comparemos:

> «$P$ solo si $Q$»

con:

> «$P$ si y solo si $Q$».

La primera expresión corresponde a una sola dirección:

$$
P\Rightarrow Q.
$$

La segunda corresponde al bicondicional:

$$
P\leftrightarrow Q.
$$

Por tanto:

$$
\boxed{
\text{«solo si»}
\neq
\text{«si y solo si»}.
}
$$

El término adicional «si» cambia la estructura: ahora se exige también la dirección inversa.

---

### 4.6 El bicondicional es una fórmula

Este punto será esencial más adelante.

La escritura:

$$
P\leftrightarrow Q
$$

es una **fórmula proposicional**.

Por tanto, para una asignación concreta, recibe:

$$
\mathrm V
$$

o:

$$
\mathrm F.
$$

Por ejemplo, si:

$$
P=\mathrm V,
\qquad
Q=\mathrm F,
$$

entonces:

$$
P\leftrightarrow Q=\mathrm F.
$$

En una sección posterior introduciremos otro concepto: diremos que dos fórmulas son **lógicamente equivalentes** cuando coinciden en valor de verdad bajo todas las asignaciones relevantes.

No confundiremos ambas ideas:

- el bicondicional es una fórmula que se evalúa;
- la equivalencia lógica será una relación entre fórmulas considerada a través de todas las asignaciones.

Todavía no necesitamos la notación de esa relación.

---

### 4.7 Bicondicional y conectivo principal

Consideremos:

$$
(p\land q)\leftrightarrow r.
$$

El conectivo principal es:

$$
\leftrightarrow.
$$

Las dos subfórmulas principales son:

$$
p\land q
$$

y:

$$
r.
$$

En cambio, en:

$$
p\land(q\leftrightarrow r),
$$

el conectivo principal es:

$$
\land.
$$

Nuestra convención general de precedencia coloca al bicondicional por debajo de los conectivos ya estudiados:

$$
\neg>\land>\lor>\Rightarrow>\leftrightarrow.
$$

Sin embargo, seguiremos prefiriendo paréntesis explícitos en fórmulas complejas.

Así, en vez de confiar en la precedencia para leer:

$$
p\land q\leftrightarrow r,
$$

preferiremos escribir:

$$
(p\land q)\leftrightarrow r
$$

o:

$$
p\land(q\leftrightarrow r),
$$

según la estructura que realmente queramos expresar.

---

### 4.8 Evaluar un bicondicional compuesto

Supongamos:

$$
p=\mathrm V,
\qquad
q=\mathrm F,
\qquad
r=\mathrm F.
$$

Evaluemos:

$$
(p\land q)\leftrightarrow r.
$$

Primero:

$$
p\land q
=
\mathrm V\land\mathrm F
=
\mathrm F.
$$

Entonces:

$$
(p\land q)\leftrightarrow r
=
\mathrm F\leftrightarrow\mathrm F
=
\mathrm V.
$$

La estructura de evaluación sigue siendo la misma:

1. identificar el conectivo principal;
2. evaluar las subfórmulas;
3. aplicar la tabla del conectivo exterior.

---

### 4.9 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-t1-c02-x0012}
**Ejemplo — Dos direcciones de un «si y solo si»**

:::

Consideremos:

$$
p=\text{«10 es par»},
$$

$$
q=\text{«10 es divisible por 2»}.
$$

Tenemos:

$$
p=\mathrm V,
\qquad
q=\mathrm V.
$$

El bicondicional:

$$
p\leftrightarrow q
$$

recibe:

$$
\mathrm V.
$$

Pero queremos leer además su estructura verbal.

#### Primera dirección

> «Si 10 es par, entonces 10 es divisible por 2».

En símbolos:

$$
p\Rightarrow q.
$$

Con los valores concretos:

$$
\mathrm V\Rightarrow\mathrm V=\mathrm V.
$$

#### Segunda dirección

> «Si 10 es divisible por 2, entonces 10 es par».

En símbolos:

$$
q\Rightarrow p.
$$

También:

$$
\mathrm V\Rightarrow\mathrm V=\mathrm V.
$$

#### Lectura conjunta

El bicondicional:

$$
p\leftrightarrow q
$$

expresa que queremos sostener ambas direcciones.

En este ejemplo concreto, las dos direcciones y el bicondicional resultan verdaderos.

Esto no constituye todavía una demostración de una ley general entre esas fórmulas. Para establecer una relación general tendremos que considerar todas las asignaciones posibles.

---

## Ejercicios

### Evaluar el bicondicional {#apm-t1-c02-e0077}

Determina el valor de verdad.

#### a)

$$
\mathrm V\leftrightarrow\mathrm V
$$

#### b)

$$
\mathrm V\leftrightarrow\mathrm F
$$

#### c)

$$
\mathrm F\leftrightarrow\mathrm V
$$

#### d)

$$
\mathrm F\leftrightarrow\mathrm F
$$

#### Solución

Por la tabla del bicondicional:

#### a)

$$
\mathrm V\leftrightarrow\mathrm V=\mathrm V.
$$

#### b)

$$
\mathrm V\leftrightarrow\mathrm F=\mathrm F.
$$

#### c)

$$
\mathrm F\leftrightarrow\mathrm V=\mathrm F.
$$

#### d)

$$
\mathrm F\leftrightarrow\mathrm F=\mathrm V.
$$

La regla compacta es:

$$
\boxed{
\begin{array}{c}
\text{mismo valor}: \mathrm V,\\
\text{valores distintos}: \mathrm F.
\end{array}
}
$$

---

### ¿Basta con que ambas sean verdaderas? {#apm-t1-c02-e0078}

Un estudiante afirma:

> «$P\leftrightarrow Q$ solo puede ser verdadero cuando $P$ y $Q$ son ambas verdaderas».

Explica el error y da una asignación que lo refute.

#### Solución

La afirmación es incorrecta.

El bicondicional es verdadero cuando $P$ y $Q$ tienen el mismo valor de verdad.

Además de:

$$
P=\mathrm V,
\qquad
Q=\mathrm V,
$$

también tenemos el caso:

$$
P=\mathrm F,
\qquad
Q=\mathrm F.
$$

Entonces:

$$
P\leftrightarrow Q
=
\mathrm F\leftrightarrow\mathrm F
=
\mathrm V.
$$

---

### Necesaria y suficiente {#apm-t1-c02-e0079}

Supón que se afirma:

$$
P\leftrightarrow Q.
$$

Completa correctamente.

#### a)

$P$ es una condición ________ y ________ para $Q$.

#### b)

$Q$ es una condición ________ y ________ para $P$.

#### c)

¿Qué dos direcciones se están exigiendo?

#### Solución

#### a)

$P$ es una condición **necesaria** y **suficiente** para $Q$.

#### b)

$Q$ es una condición **necesaria** y **suficiente** para $P$.

#### c)

Se exigen:

$$
P\Rightarrow Q
$$

y:

$$
Q\Rightarrow P.
$$

---

### Justificar una fila {#apm-t1-c02-e0080}

Explica, sin limitarte a copiar la tabla, por qué:

$$
\mathrm F\leftrightarrow\mathrm F=\mathrm V.
$$

#### Solución

El bicondicional compara los valores de verdad de sus dos componentes.

Cuando ambos reciben:

$$
\mathrm F,
$$

sus valores coinciden.

Por definición, el bicondicional es verdadero cuando ambos componentes tienen el mismo valor de verdad.

Por eso:

$$
\mathrm F\leftrightarrow\mathrm F=\mathrm V.
$$

Otra manera de leerlo es observar que ninguna de las dos proposiciones es verdadera mientras la otra es falsa.

---

### Leer una fórmula compuesta {#apm-t1-c02-e0081}

Supón:

$$
p=\mathrm V,
\qquad
q=\mathrm F,
\qquad
r=\mathrm F.
$$

Considera:

$$
(p\lor q)\leftrightarrow\neg r.
$$

#### a)

Identifica el conectivo principal.

#### b)

Evalúa:

$$
p\lor q.
$$

#### c)

Evalúa:

$$
\neg r.
$$

#### d)

Determina el valor de la fórmula completa.

#### Solución

#### a)

El conectivo principal es:

$$
\leftrightarrow.
$$

#### b)

$$
p\lor q
=
\mathrm V\lor\mathrm F
=
\mathrm V.
$$

#### c)

Como:

$$
r=\mathrm F,
$$

tenemos:

$$
\neg r=\mathrm V.
$$

#### d)

Entonces:

$$
(p\lor q)\leftrightarrow\neg r
=
\mathrm V\leftrightarrow\mathrm V
=
\mathrm V.
$$

---

### Síntesis: una caracterización concreta {#apm-t1-c02-e0082}

Sea:

$$
p=\text{«18 es par»},
$$

$$
q=\text{«18 es divisible por 2»}.
$$

#### a)

Determina los valores de $p$ y $q$.

#### b)

Escribe en símbolos:

> «18 es par si y solo si 18 es divisible por 2».

#### c)

Escribe las dos implicaciones asociadas a esa lectura de dos direcciones.

#### d)

Expresa en palabras la relación usando «necesaria y suficiente».

#### e)

Evalúa el bicondicional.

#### f)

Explica por qué verificar este único ejemplo no demuestra una afirmación general sobre todos los números.

#### Solución

#### a)

Tenemos:

$$
p=\mathrm V,
\qquad
q=\mathrm V.
$$

#### b)

La fórmula es:

$$
p\leftrightarrow q.
$$

#### c)

Las dos direcciones son:

$$
p\Rightarrow q
$$

y:

$$
q\Rightarrow p.
$$

#### d)

Podemos decir:

> «Que 18 sea par es una condición necesaria y suficiente para que 18 sea divisible por 2».

También podemos invertir los papeles.

#### e)

Como ambos valores son verdaderos:

$$
p\leftrightarrow q
=
\mathrm V\leftrightarrow\mathrm V
=
\mathrm V.
$$

#### f)

Solo hemos evaluado proposiciones referentes al número concreto 18.

Un ejemplo particular no establece por sí mismo una afirmación acerca de todos los números.

La formulación general requeriría herramientas que todavía no hemos introducido en este capítulo.

---

## Síntesis

El bicondicional:

$$
P\leftrightarrow Q
$$

se lee:

> «$P$ si y solo si $Q$».

Su tabla es:

| $P$ | $Q$ | $P\leftrightarrow Q$ |
|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ |

La regla esencial es:

$$
\boxed{
P\leftrightarrow Q
\text{ es verdadera exactamente cuando }
P
\text{ y }
Q
\text{ tienen el mismo valor de verdad}.
}
$$

Además, «$P$ si y solo si $Q$» exige dos direcciones:

$$
P\Rightarrow Q
$$

y:

$$
Q\Rightarrow P.
$$

Por eso podemos decir que:

- $P$ es necesaria y suficiente para $Q$;
- $Q$ es necesaria y suficiente para $P$.

Finalmente, debemos conservar una distinción que pronto será decisiva:

> el bicondicional es una **fórmula** y recibe un valor de verdad en cada asignación;

mientras que, más adelante, la equivalencia lógica comparará dos fórmulas a través de **todas** las asignaciones.

---

## Hacia la sección siguiente

Ya conocemos los cinco conectivos básicos que utilizaremos:

$$
\neg,
\qquad
\land,
\qquad
\lor,
\qquad
\Rightarrow,
\qquad
\leftrightarrow.
$$

Hasta ahora hemos evaluado fórmulas caso por caso.

Pero, cuando una fórmula contiene varias variables, necesitamos un procedimiento sistemático que garantice que no olvidamos ninguna combinación posible.

Por ejemplo:

$$
\neg(p\land q)\lor r.
$$

La siguiente sección desarrollará ese instrumento:
