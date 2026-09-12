---
title: "Lógica proposicional y álgebra de proposiciones"
description: "Segundo capítulo de Álgebra para matemáticos: proposiciones, conectivos, implicación y bicondicional, tablas de verdad, tautologías, equivalencia lógica, cálculo proposicional y formas normales."
content-id: MA-BCH-0008
source-id: APM-T1-C02
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
  - logica-proposicional
  - conectivos
  - tablas-de-verdad
  - tautologias
  - equivalencia-logica
  - algebra-proposicional
  - formas-normales
prerequisites:
  - MA-BCH-0007
related:
  - MA-BOK-0004
  - MA-BCH-0007
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Lógica proposicional y álgebra de proposiciones

## §1. Afirmaciones que pueden ser verdaderas o falsas

En el capítulo anterior trabajamos sobre todo con **expresiones**.

Por ejemplo:

$$
2+3,
$$

$$
4(x+1),
$$

o:

$$
\frac{a+b}{c}.
$$

Aprendimos a leer su estructura, sustituir valores y transformarlas sin cambiar el valor que representan.

Ahora comparemos:

$$
2+3
$$

con:

$$
2+3=5.
$$

La primera escritura representa una cantidad.

La segunda hace algo diferente: **afirma que dos cantidades son iguales**.

Y, además, podemos preguntarnos:

> ¿esa afirmación es verdadera o falsa?

En este caso es verdadera.

Comparemos ahora:

$$
2+3=6.
$$

La afirmación es falsa.

Pero sigue siendo una afirmación perfectamente comprensible.

Esta diferencia —entre una expresión que representa algo y una afirmación que puede ser verdadera o falsa— abre el nuevo capítulo.

Nuestro objeto de estudio ya no será solamente:

$$
\boxed{\text{qué representan los símbolos}},
$$

sino también:

$$
\boxed{\text{qué afirman y bajo qué condiciones esas afirmaciones son verdaderas o falsas}.}
$$

### 1.1 Expresar una cantidad no es afirmar algo

Consideremos:

$$
7+4.
$$

Esta escritura representa un número.

Podemos evaluarla:

$$
7+4=11.
$$

Pero la expresión:

$$
7+4
$$

por sí sola no afirma que algo sea verdadero o falso.

Ahora consideremos:

$$
7+4=11.
$$

Aquí sí encontramos una afirmación.

Podemos asignarle:

$$
\mathrm V
$$

porque es verdadera.

En cambio:

$$
7+4=12
$$

recibe:

$$
\mathrm F.
$$

La diferencia es estructural:

$$
\boxed{
\text{expresión}
\neq
\text{afirmación}.
}
$$

Una expresión puede formar parte de una afirmación, pero no toda expresión es una afirmación.

### 1.2 Proposiciones

Necesitamos un nombre para las afirmaciones a las que podemos atribuir verdad o falsedad.

::: {.ma-block .ma-definicion #apm-t1-c02-d0008}
**Definición — Proposición**

En este capítulo, una **proposición** es una afirmación cuyo valor de verdad está determinado en el contexto considerado: es verdadera o es falsa, y no ambas.
:::

Ejemplos:

$$
4+5=9
$$

es una proposición verdadera.

$$
4+5=10
$$

es una proposición falsa.

Lo importante no es que una proposición resulte verdadera.

Lo importante es que **afirme algo susceptible de ser verdadero o falso**.

::: {.ma-block .ma-intuicion}
**Idea clave**

Una proposición falsa sigue siendo una proposición.
:::

La lógica no estudia solamente afirmaciones verdaderas. También necesita representar afirmaciones falsas y analizar cómo se comportan al combinarlas.

### 1.3 Valores de verdad

En la lógica proposicional clásica que estudiaremos en este capítulo trabajaremos con dos valores de verdad.

::: {.ma-block .ma-definicion #apm-t1-c02-d0009}
**Definición — Valor de verdad**

El **valor de verdad** de una proposición indica si la proposición es verdadera o falsa. Usaremos:

$$
\mathrm V
$$

para «verdadera», y:

$$
\mathrm F
$$

para «falsa».
:::

Así:

$$
4+5=9
$$

tiene valor de verdad:

$$
\mathrm V,
$$

mientras que:

$$
4+5=10
$$

tiene valor de verdad:

$$
\mathrm F.
$$

| Proposición | Valor de verdad |
|---|---|
| $3+2=5$ | $\mathrm V$ |
| $3+2=6$ | $\mathrm F$ |
| $10-4=6$ | $\mathrm V$ |
| $10-4=5$ | $\mathrm F$ |

En este capítulo cada proposición tendrá exactamente uno de estos dos valores.

No estudiaremos todavía otros sistemas lógicos posibles. Nuestro marco de trabajo será la lógica proposicional clásica bivalente.

### 1.4 Ser falsa no significa carecer de sentido

Consideremos:

$$
8+1=12.
$$

La igualdad es falsa.

Pero entendemos perfectamente qué afirma.

Podemos calcular:

$$
8+1=9,
$$

y concluir que la proposición es falsa.

Comparemos esto con:

$$
8+1.
$$

Aquí no hay una afirmación falsa.

Hay simplemente una expresión.

No tiene sentido asignarle:

$$
\mathrm V
$$

o:

$$
\mathrm F.
$$

Su valor es numérico:

$$
9.
$$

Esta distinción será una de las más importantes del capítulo:

$$
\boxed{
\text{una expresión tiene un valor matemático;}
\qquad
\text{una proposición tiene un valor de verdad}.
}
$$

### 1.5 Preguntas y órdenes no son proposiciones

No toda oración es una proposición.

Consideremos:

> «¿Cuánto es $7+4$?»

Es una pregunta.

No afirma que algo sea verdadero ni falso.

Ahora consideremos:

> «Calcula $7+4$».

Es una orden o instrucción.

Tampoco afirma algo susceptible de ser verdadero o falso.

| Escritura | Tipo |
|---|---|
| $7+4$ | expresión |
| $7+4=11$ | proposición |
| $7+4=12$ | proposición |
| «¿Cuánto es $7+4$?» | pregunta |
| «Calcula $7+4$» | instrucción |

La clasificación depende de **qué función cumple la escritura**, no solamente de los símbolos que aparecen.

### 1.6 Una letra puede impedir que el valor de verdad esté fijado

Consideremos:

$$
x+2=5.
$$

¿Es verdadera o falsa?

Todavía no podemos responder.

Si:

$$
x=3,
$$

obtenemos:

$$
3+2=5,
$$

que es verdadera.

Pero si:

$$
x=1,
$$

obtenemos:

$$
1+2=5,
$$

que es falsa.

Por tanto, mientras el valor o el contexto de $x$ no esté fijado, la escritura:

$$
x+2=5
$$

no determina todavía una proposición con un único valor de verdad dentro del marco de esta sección.

Más adelante estudiaremos de manera sistemática las afirmaciones que dependen de variables.

Por ahora no necesitamos un nombre técnico para ellas.

### 1.7 No saber la respuesta no elimina el valor de verdad

Hay una diferencia importante entre:

1. que la información necesaria no esté fijada;
2. que la afirmación esté fijada, pero todavía no hayamos calculado o comprobado su verdad.

Consideremos:

$$
37\cdot41=1517.
$$

Antes de hacer la multiplicación quizá no sepamos si la igualdad es correcta.

Pero la proposición ya está completamente determinada.

Podemos comprobar:

$$
37\cdot41
=
37(40+1)
=
1480+37
=
1517.
$$

Así descubrimos que su valor de verdad es:

$$
\mathrm V.
$$

::: {.ma-block .ma-intuicion}
**Idea clave**

«No sé todavía si es verdadera» y «todavía no se ha determinado una afirmación completa» son situaciones diferentes.
:::

### 1.8 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-t1-c02-x0009}
**Ejemplo — Expresión, pregunta, instrucción o proposición**

:::

Clasifiquemos las siguientes escrituras.

#### 1.

$$
3+4
$$

Es una **expresión**.

Representa el número $7$, pero no afirma nada que deba ser clasificado como verdadero o falso.

#### 2.

$$
3+4=7
$$

Es una **proposición** verdadera:

$$
\mathrm V.
$$

#### 3.

$$
3+4=8
$$

También es una **proposición**, pero falsa:

$$
\mathrm F.
$$

#### 4.

> «¿Es $3+4$ igual a $7$?»

Es una **pregunta**.

#### 5.

> «Calcula $3+4$».

Es una **instrucción**.

#### 6.

$$
x+4=7
$$

si no se ha especificado nada sobre $x$.

En el marco actual, esta escritura **no determina todavía una proposición con valor de verdad fijado**.

La idea central es:

$$
\boxed{
\text{antes de preguntar si algo es verdadero o falso, comprueba que realmente se está haciendo una afirmación}.
}
$$

## Ejercicios

### Clasificar y evaluar {#apm-t1-c02-e0057}

Clasifica cada escritura como expresión, proposición, pregunta o instrucción. Cuando sea proposición, indica su valor de verdad.

#### a)

$$
6+2
$$

#### b)

$$
6+2=8
$$

#### c)

$$
6+2=9
$$

#### d)

> «¿Cuánto es $6+2$?»

#### e)

> «Calcula $6+2$».

#### Solución

a) Expresión. Su valor numérico es $8$, pero no tiene valor de verdad.

b) Proposición verdadera:

$$
\mathrm V.
$$

c) Proposición falsa:

$$
\mathrm F.
$$

d) Pregunta; no tiene valor de verdad.

e) Instrucción; no tiene valor de verdad.

### Una proposición falsa sigue siendo proposición {#apm-t1-c02-e0058}

Un estudiante afirma:

> «$5+5=11$ no es una proposición porque es falsa».

Explica el error.

#### Solución

Una proposición no se define como una afirmación verdadera, sino como una afirmación cuyo valor de verdad está determinado.

Como:

$$
5+5=10,
$$

la escritura:

$$
5+5=11
$$

es una proposición falsa:

$$
\boxed{\mathrm F}.
$$

### El papel del contexto {#apm-t1-c02-e0059}

Considera:

$$
x+1=4.
$$

#### a)

Explica por qué, sin información adicional sobre $x$, no podemos asignarle todavía un único valor de verdad en el marco de esta sección.

#### b)

¿Qué ocurre si $x=3$?

#### c)

¿Qué ocurre si $x=5$?

#### Solución

a) La verdad de la escritura depende del valor de $x$. Sin fijarlo, no obtenemos todavía una proposición con un único valor de verdad.

b) Si $x=3$:

$$
3+1=4,
$$

por lo que:

$$
\mathrm V.
$$

c) Si $x=5$:

$$
5+1=4,
$$

por lo que:

$$
\mathrm F.
$$

### No saber todavía {#apm-t1-c02-e0060}

Considera:

$$
23\cdot17=391.
$$

#### a)

¿Deja de ser proposición si todavía no has realizado la multiplicación?

#### b)

Determina su valor de verdad.

#### Solución

a) No. La afirmación está completamente determinada aunque todavía no conozcamos el resultado.

b)

$$
23\cdot17
=
23(10+7)
=
230+161
=
391.
$$

Por tanto:

$$
\boxed{\mathrm V}.
$$

### Síntesis {#apm-t1-c02-e0061}

Considera:

1. $2(4+1)$;
2. $2(4+1)=10$;
3. «¿Es $2(4+1)=10$?»;
4. «Simplifica $2(4+1)$»;
5. $y+2=7$, sin información sobre $y$;
6. $y+2=7$, sabiendo que $y=5$.

Para cada una, indica qué tipo de escritura es y si corresponde asignar $\mathrm V$ o $\mathrm F$.

#### Solución

1. Es una expresión. Representa $10$, pero no tiene valor de verdad.

2. Es una proposición verdadera:

$$
\mathrm V.
$$

3. Es una pregunta. No tiene valor de verdad.

4. Es una instrucción. No tiene valor de verdad.

5. Sin información sobre $y$, no determina todavía una proposición con un único valor de verdad en el marco actual.

6. Con $y=5$:

$$
5+2=7,
$$

por lo que es una proposición verdadera:

$$
\mathrm V.
$$

## Síntesis

Una expresión como:

$$
3+4
$$

representa una cantidad.

Una proposición como:

$$
3+4=7
$$

afirma algo que puede ser verdadero o falso.

La distinción central es:

$$
\boxed{
\text{expresión}\longrightarrow\text{valor matemático}
}
$$

frente a:

$$
\boxed{
\text{proposición}\longrightarrow\text{valor de verdad}.
}
$$

En la lógica proposicional clásica trabajaremos con:

$$
\boxed{
\mathrm V,\qquad \mathrm F.
}
$$

Además:

- una proposición falsa sigue siendo una proposición;
- una pregunta no es una proposición;
- una instrucción no es una proposición;
- ignorar todavía la verdad de una proposición no elimina su valor de verdad;
- una escritura que depende de una letra no especificada puede requerir más contexto.

## Hacia la sección siguiente

Para estudiar afirmaciones sin repetir frases largas, comenzaremos a representarlas mediante símbolos:

$$
p,\qquad q.
$$

Y construiremos nuevas afirmaciones como:

> «no $p$»,

> «$p$ y $q$»,

> «$p$ o $q$».

La siguiente sección estudiará precisamente cómo se forman estas expresiones lógicas:

## §2. Variables proposicionales y fórmulas

En la sección anterior trabajamos con proposiciones completas, por ejemplo:

> «Ocho es par».

> «Nueve es menor que cinco».

La primera es verdadera y la segunda es falsa.

Pero, si queremos estudiar cómo se combinan las proposiciones, repetir frases completas cada vez resultaría incómodo.

Podemos abreviar:

$$
p=\text{«Ocho es par»}
$$

y:

$$
q=\text{«Nueve es menor que cinco»}.
$$

Entonces, en lugar de repetir las oraciones, trabajaremos con:

$$
p,
\qquad
q.
$$

Esta sustitución no cambia el tipo de objeto que estamos estudiando.

La letra:

$$
p
$$

no representa ahora un número.

Representa una proposición.

Este es el primer cambio importante de lenguaje del capítulo:

$$
\boxed{
\text{las letras pueden representar proposiciones completas}.
}
$$

---

### 2.1 Variables proposicionales

::: {.ma-block .ma-definicion #apm-t1-c02-d0010}
**Definición — Variable proposicional**

Una **variable proposicional** es un símbolo, como $p$, $q$ o $r$, que puede representar una proposición y, por tanto, recibir un valor de verdad.
:::

Por ejemplo, si:

$$
p=\text{«Ocho es par»},
$$

entonces:

$$
p
$$

recibe el valor:

$$
\mathrm V.
$$

Si:

$$
q=\text{«Nueve es menor que cinco»},
$$

entonces:

$$
q
$$

recibe:

$$
\mathrm F.
$$

Conviene comparar esta situación con el álgebra.

En:

$$
x+2,
$$

la letra $x$ puede representar un número.

En:

$$
p\land q,
$$

las letras $p$ y $q$ representarán proposiciones.

Por eso:

::: {.ma-block .ma-intuicion}
**Idea clave**

Una variable proposicional no es una variable numérica. Su valor no es un número, sino un valor de verdad.
:::

En este capítulo utilizaremos preferentemente:

$$
p,q,r,s,\ldots
$$

para variables proposicionales atómicas.

---

### 2.2 De proposiciones simples a fórmulas

Supongamos:

$$
p=\text{«Llueve»},
$$

$$
q=\text{«Hace frío»}.
$$

A partir de estas proposiciones podemos construir otras:

> «No llueve».

> «Llueve y hace frío».

> «Llueve o hace frío».

En símbolos escribiremos:

$$
\neg p,
$$

$$
p\land q,
$$

$$
p\lor q.
$$

Estas escrituras ya no son variables proposicionales aisladas. Son expresiones lógicas construidas a partir de ellas.

::: {.ma-block .ma-definicion #apm-t1-c02-d0011}
**Definición — Fórmula proposicional**

Una **fórmula proposicional** es una expresión lógica construida a partir de variables proposicionales mediante los conectivos permitidos.

Por ahora:

- cada variable proposicional, como $p$, es una fórmula;
- si $P$ es una fórmula, entonces $\neg P$ es una fórmula;
- si $P$ y $Q$ son fórmulas, entonces $P\land Q$ y $P\lor Q$ son fórmulas.
:::

Más adelante ampliaremos el repertorio de conectivos.

Una variable proposicional aislada, como:

$$
p,
$$

se denomina también **fórmula atómica**.

Una fórmula construida con uno o más conectivos, como:

$$
\neg p
$$

o:

$$
p\lor q,
$$

es una **fórmula compuesta**.

---

### 2.3 Negación

La primera operación lógica que estudiaremos cambia el valor de verdad de una fórmula.

::: {.ma-block .ma-definicion #apm-t1-c02-d0012}
**Definición — Negación**

La **negación** de una fórmula $P$ es la fórmula:

$$
\neg P,
$$

que es verdadera cuando $P$ es falsa y falsa cuando $P$ es verdadera.
:::

Si:

$$
p=\text{«Ocho es par»},
$$

entonces:

$$
\neg p
$$

significa:

> «Ocho no es par».

Como $p$ es verdadera, $\neg p$ es falsa.

La tabla elemental de la negación es:

| $P$ | $\neg P$ |
|---|---|
| $\mathrm V$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ |

La negación actúa sobre **una sola fórmula**.

Por eso debemos prestar atención a su alcance.

Comparemos:

$$
\neg p\lor q
$$

con:

$$
\neg(p\lor q).
$$

En la primera escritura, la negación afecta únicamente a:

$$
p.
$$

En la segunda, afecta a toda la fórmula:

$$
p\lor q.
$$

Todavía no necesitamos decidir si ambas fórmulas pueden coincidir en algún caso. Lo importante aquí es reconocer que **su estructura es diferente**.

---

### 2.4 Conjunción

::: {.ma-block .ma-definicion #apm-t1-c02-d0013}
**Definición — Conjunción**

La **conjunción** de dos fórmulas $P$ y $Q$ es:

$$
P\land Q.
$$

Es verdadera exactamente cuando $P$ y $Q$ son ambas verdaderas.
:::

El símbolo:

$$
\land
$$

se lee normalmente:

> «y».

Por ejemplo, si:

$$
p=\text{«Doce es par»}
$$

y:

$$
q=\text{«Doce es mayor que diez»},
$$

entonces:

$$
p\land q
$$

significa:

> «Doce es par y doce es mayor que diez».

Las dos proposiciones son verdaderas, así que la conjunción es verdadera.

Su tabla elemental es:

| $P$ | $Q$ | $P\land Q$ |
|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |

Basta con que una de las dos fórmulas sea falsa para que la conjunción completa sea falsa.

---

### 2.5 Disyunción inclusiva

::: {.ma-block .ma-definicion #apm-t1-c02-d0014}
**Definición — Disyunción**

La **disyunción** de dos fórmulas $P$ y $Q$ es:

$$
P\lor Q.
$$

Es verdadera cuando al menos una de las dos fórmulas es verdadera, y es falsa solamente cuando ambas son falsas.
:::

El símbolo:

$$
\lor
$$

se lee:

> «o».

En lógica proposicional clásica, esta «o» es **inclusiva**.

Eso significa que:

$$
P\lor Q
$$

también es verdadera cuando:

$$
P
$$

y:

$$
Q
$$

son ambas verdaderas.

La tabla es:

| $P$ | $Q$ | $P\lor Q$ |
|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |

Por ejemplo, las proposiciones:

> «Doce es par»

y:

> «Doce es mayor que diez»

son ambas verdaderas.

Por tanto, su disyunción:

> «Doce es par o doce es mayor que diez»

es verdadera en el sentido lógico inclusivo.

::: {.ma-block .ma-observacion}
En el lenguaje cotidiano, «o» puede usarse a veces con sentido exclusivo: una cosa o la otra, pero no ambas. En este capítulo, salvo indicación expresa, $\lor$ será siempre inclusiva.
:::

---

### 2.6 El conectivo principal

Consideremos:

$$
\neg p\land q.
$$

La fórmula contiene dos conectivos:

$$
\neg
$$

y:

$$
\land.
$$

Pero no cumplen el mismo papel estructural.

Por nuestra convención de precedencia:

$$
\neg p\land q
$$

se lee como:

$$
(\neg p)\land q.
$$

La fórmula completa es una conjunción.

El conectivo que organiza la fórmula completa es:

$$
\land.
$$

Lo llamaremos **conectivo principal**.

En cambio, en:

$$
\neg(p\land q),
$$

el conectivo principal es:

$$
\neg,
$$

porque la negación actúa sobre toda la conjunción.

Así:

$$
\boxed{
\text{el conectivo principal es el que actúa desde el nivel más exterior de la fórmula}.
}
$$

Esta idea prolonga exactamente el hábito de T1-C01:

$$
\boxed{
\text{leer de fuera hacia dentro}.
}
$$

---

### 2.7 Subfórmulas

Consideremos:

$$
\neg(p\lor q).
$$

La expresión:

$$
p\lor q
$$

forma parte de una fórmula mayor.

Diremos que es una **subfórmula**.

También:

$$
p
$$

y:

$$
q
$$

son subfórmulas.

Podemos representar la estructura así:

```text
negación
└── disyunción
    ├── p
    └── q
```

Ahora consideremos:

$$
\neg(p\lor q)\land r.
$$

Su estructura es:

```text
conjunción
├── negación
│   └── disyunción
│       ├── p
│       └── q
└── r
```

La estructura no depende de la longitud de la fórmula, sino de cómo están agrupados sus componentes.

---

### 2.8 Paréntesis y precedencia

El checkpoint de notación del proyecto fija, para los conectivos que ya conocemos:

$$
\neg>\land>\lor.
$$

Esto significa que:

$$
\neg p\land q
$$

se interpreta como:

$$
(\neg p)\land q,
$$

y que:

$$
p\lor q\land r
$$

se interpreta como:

$$
p\lor(q\land r).
$$

Sin embargo, nuestra política editorial será más conservadora:

::: {.ma-block .ma-intuicion}
**Idea clave**

Cuando una fórmula tenga varios niveles, preferiremos paréntesis explícitos antes que obligar al lector a reconstruir mentalmente toda la precedencia.
:::

Por eso, aun siendo correcta la escritura:

$$
p\lor q\land r,
$$

normalmente preferiremos:

$$
p\lor(q\land r).
$$

La notación debe mostrar la estructura, no esconderla.

---

### 2.9 Evaluar una fórmula sin construir todavía una tabla completa

Supongamos que:

$$
p=\mathrm F,
\qquad
q=\mathrm V.
$$

¿Cuál es el valor de:

$$
\neg p\land q?
$$

Primero:

$$
p=\mathrm F.
$$

Por tanto:

$$
\neg p=\mathrm V.
$$

Después:

$$
(\neg p)\land q
=
\mathrm V\land\mathrm V.
$$

Así:

$$
\neg p\land q=\mathrm V.
$$

Hemos evaluado la fórmula **desde las subfórmulas hacia la fórmula completa**.

::: {.ma-block .ma-observacion}
En cálculos semánticos escribiremos a veces, por brevedad, expresiones como:

$$
\mathrm V\land\mathrm F=\mathrm F.
$$

Esto abrevia la frase: «una conjunción cuyos componentes reciben los valores $\mathrm V$ y $\mathrm F$ recibe el valor $\mathrm F$». Los símbolos $\mathrm V$ y $\mathrm F$ son valores de verdad, no variables proposicionales.
:::

Este procedimiento será la base de las tablas de verdad que sistematizaremos más adelante.

---

### 2.10 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-t1-c02-x0010}
**Ejemplo — Leer una fórmula desde fuera hacia dentro**

:::

Consideremos:

$$
\neg(p\lor q)\land r.
$$

Queremos hacer dos cosas:

1. reconocer su estructura;
2. evaluarla para una asignación concreta.

Supongamos:

$$
p=\mathrm F,
\qquad
q=\mathrm F,
\qquad
r=\mathrm V.
$$

#### Paso 1 — Conectivo principal

La fórmula completa es:

$$
[\neg(p\lor q)]\land r.
$$

El conectivo principal es:

$$
\land.
$$

Por tanto, las dos partes principales son:

$$
\neg(p\lor q)
$$

y:

$$
r.
$$

#### Paso 2 — Subfórmula interna

Dentro de:

$$
\neg(p\lor q)
$$

encontramos primero:

$$
p\lor q.
$$

Como:

$$
p=\mathrm F,
\qquad
q=\mathrm F,
$$

tenemos:

$$
p\lor q=\mathrm F.
$$

#### Paso 3 — Negación

Entonces:

$$
\neg(p\lor q)=\mathrm V.
$$

#### Paso 4 — Conjunción exterior

Finalmente:

$$
\neg(p\lor q)\land r
=
\mathrm V\land\mathrm V
=
\mathrm V.
$$

La evaluación completa puede escribirse como:

$$
\boxed{
\neg(p\lor q)\land r=\mathrm V
}
$$

para esta asignación.

La estrategia general es:

$$
\boxed{
\text{leer desde fuera para reconocer la estructura}
\quad+\quad
\text{evaluar desde dentro para obtener el valor}.
}
$$

---

## Ejercicios

### Traducir y evaluar {#apm-t1-c02-e0062}

Sea:

$$
p=\text{«Diez es par»}
$$

y:

$$
q=\text{«Diez es menor que siete»}.
$$

Escribe en símbolos y determina el valor de verdad de:

#### a)

> «Diez no es par».

#### b)

> «Diez es par y diez es menor que siete».

#### c)

> «Diez es par o diez es menor que siete».

#### Solución

Tenemos:

$$
p=\mathrm V,
\qquad
q=\mathrm F.
$$

#### a)

La fórmula es:

$$
\neg p.
$$

Como $p=\mathrm V$:

$$
\neg p=\mathrm F.
$$

#### b)

La fórmula es:

$$
p\land q.
$$

Entonces:

$$
\mathrm V\land\mathrm F=\mathrm F.
$$

#### c)

La fórmula es:

$$
p\lor q.
$$

Entonces:

$$
\mathrm V\lor\mathrm F=\mathrm V.
$$

---

### Conectivo principal {#apm-t1-c02-e0063}

Identifica el conectivo principal de cada fórmula.

#### a)

$$
\neg p\lor q
$$

#### b)

$$
\neg(p\lor q)
$$

#### c)

$$
(p\land q)\lor r
$$

#### d)

$$
\neg(p\land q)\lor r
$$

#### Solución

#### a)

Por precedencia:

$$
\neg p\lor q
=
(\neg p)\lor q.
$$

El conectivo principal es:

$$
\lor.
$$

#### b)

El conectivo principal es:

$$
\neg.
$$

#### c)

El conectivo principal es:

$$
\lor.
$$

#### d)

La fórmula completa es:

$$
[\neg(p\land q)]\lor r.
$$

El conectivo principal es:

$$
\lor.
$$

---

### Evaluar desde dentro {#apm-t1-c02-e0064}

Supón:

$$
p=\mathrm V,
\qquad
q=\mathrm F,
\qquad
r=\mathrm V.
$$

Determina el valor de verdad de:

#### a)

$$
\neg q
$$

#### b)

$$
p\land q
$$

#### c)

$$
q\lor r
$$

#### d)

$$
\neg(p\land q)\lor r
$$

#### Solución

#### a)

Como $q=\mathrm F$:

$$
\neg q=\mathrm V.
$$

#### b)

$$
p\land q
=
\mathrm V\land\mathrm F
=
\mathrm F.
$$

#### c)

$$
q\lor r
=
\mathrm F\lor\mathrm V
=
\mathrm V.
$$

#### d)

Primero:

$$
p\land q
=
\mathrm V\land\mathrm F
=
\mathrm F.
$$

Luego:

$$
\neg(p\land q)=\mathrm V.
$$

Finalmente:

$$
\neg(p\land q)\lor r
=
\mathrm V\lor\mathrm V
=
\mathrm V.
$$

---

### La «o» inclusiva {#apm-t1-c02-e0065}

Sean $p$ y $q$ dos proposiciones verdaderas.

#### a)

¿Cuál es el valor de:

$$
p\lor q?
$$

#### b)

Explica por qué este resultado puede diferir de algunos usos cotidianos de la palabra «o».

#### Solución

#### a)

Como ambas proposiciones son verdaderas:

$$
p\lor q
=
\mathrm V\lor\mathrm V
=
\mathrm V.
$$

#### b)

En lógica proposicional clásica, $\lor$ es inclusiva: basta con que una de las dos fórmulas sea verdadera, y también es verdadera cuando ambas lo son.

En el lenguaje cotidiano, algunas expresiones con «o» sugieren una elección exclusiva. Ese no será el significado de $\lor$ en este capítulo.

---

### El alcance de la negación {#apm-t1-c02-e0066}

Compara:

$$
\neg p\land q
$$

con:

$$
\neg(p\land q).
$$

Supón:

$$
p=\mathrm F,
\qquad
q=\mathrm F.
$$

#### a)

Evalúa la primera fórmula.

#### b)

Evalúa la segunda.

#### c)

Explica qué diferencia estructural produce los resultados.

#### Solución

#### a)

Por precedencia:

$$
\neg p\land q
=
(\neg p)\land q.
$$

Como:

$$
p=\mathrm F,
$$

tenemos:

$$
\neg p=\mathrm V.
$$

Entonces:

$$
(\neg p)\land q
=
\mathrm V\land\mathrm F
=
\mathrm F.
$$

#### b)

Primero:

$$
p\land q
=
\mathrm F\land\mathrm F
=
\mathrm F.
$$

Luego:

$$
\neg(p\land q)
=
\mathrm V.
$$

#### c)

En la primera fórmula, $\neg$ actúa solo sobre $p$.

En la segunda, $\neg$ actúa sobre toda la conjunción:

$$
p\land q.
$$

El cambio de alcance cambia la estructura y puede cambiar el valor de verdad.

---

### Los paréntesis importan {#apm-t1-c02-e0067}

Considera:

$$
p\lor(q\land r)
$$

y:

$$
(p\lor q)\land r.
$$

Encuentra una asignación de valores de verdad para $p,q,r$ en la que las dos fórmulas tengan valores diferentes.

#### Solución

Tomemos:

$$
p=\mathrm V,
\qquad
q=\mathrm F,
\qquad
r=\mathrm F.
$$

Para la primera:

$$
q\land r
=
\mathrm F\land\mathrm F
=
\mathrm F.
$$

Entonces:

$$
p\lor(q\land r)
=
\mathrm V\lor\mathrm F
=
\mathrm V.
$$

Para la segunda:

$$
p\lor q
=
\mathrm V\lor\mathrm F
=
\mathrm V.
$$

Luego:

$$
(p\lor q)\land r
=
\mathrm V\land\mathrm F
=
\mathrm F.
$$

Por tanto, con esta asignación:

$$
p\lor(q\land r)=\mathrm V
$$

y:

$$
(p\lor q)\land r=\mathrm F.
$$

La agrupación modifica la estructura.

---

### Síntesis: construir, leer y evaluar {#apm-t1-c02-e0068}

Sea:

$$
p=\text{«Quince es impar»},
$$

$$
q=\text{«Quince es mayor que veinte»},
$$

$$
r=\text{«Quince es múltiplo de cinco»}.
$$

Considera la afirmación:

> «Quince no es mayor que veinte y, además, quince es impar o múltiplo de cinco».

La agrupación pretendida es:

> «Quince no es mayor que veinte» **y** «quince es impar o múltiplo de cinco».

#### a)

Escribe la fórmula correspondiente.

#### b)

Identifica su conectivo principal.

#### c)

Determina los valores de $p,q,r$.

#### d)

Evalúa la fórmula paso a paso.

#### Solución

#### a)

La fórmula es:

$$
(\neg q)\land(p\lor r).
$$

#### b)

El conectivo principal es:

$$
\land.
$$

Las dos subfórmulas principales son:

$$
\neg q
$$

y:

$$
p\lor r.
$$

#### c)

Tenemos:

$$
p=\mathrm V,
$$

porque quince es impar;

$$
q=\mathrm F,
$$

porque quince no es mayor que veinte;

y:

$$
r=\mathrm V,
$$

porque quince es múltiplo de cinco.

#### d)

Primero:

$$
\neg q=\mathrm V.
$$

También:

$$
p\lor r
=
\mathrm V\lor\mathrm V
=
\mathrm V.
$$

Finalmente:

$$
(\neg q)\land(p\lor r)
=
\mathrm V\land\mathrm V
=
\mathrm V.
$$

---

## Síntesis

Las variables proposicionales:

$$
p,q,r,\ldots
$$

nos permiten representar proposiciones completas.

A partir de ellas construimos fórmulas mediante conectivos.

En esta sección hemos introducido:

$$
\neg,
\qquad
\land,
\qquad
\lor.
$$

Sus significados semánticos quedan determinados por sus tablas elementales.

La distinción central es:

$$
\boxed{
\text{variable proposicional}
\neq
\text{variable numérica}.
}
$$

Y el hábito estructural que heredamos de T1-C01 se fortalece:

$$
\boxed{
\text{leer desde fuera para reconocer la estructura;}
\qquad
\text{evaluar desde dentro para calcular el valor de verdad}.
}
$$

Los paréntesis y el alcance importan:

$$
\neg p\land q
$$

no tiene la misma estructura que:

$$
\neg(p\land q).
$$

Y, aunque existe una precedencia convencional:

$$
\neg>\land>\lor,
$$

preferiremos paréntesis explícitos cuando ayuden a que la estructura se vea sin esfuerzo.

---

## Hacia la sección siguiente

Ya podemos construir fórmulas que expresan:

> «no»,

> «y»,

> «o».

Pero las matemáticas utilizan constantemente una forma aún más importante:

> «Si ocurre esto, entonces ocurre aquello».

Por ejemplo:

> «Si un número es múltiplo de cuatro, entonces es par».

¿Cómo debemos interpretar esta construcción?

¿En qué caso es falsa?

¿Y qué significa exactamente decir que una condición es suficiente o necesaria?

La siguiente sección estará dedicada a:

## §3. Implicación: «si..., entonces...»

Ya sabemos representar proposiciones mediante letras y combinarlas con:

$$
\neg,\qquad
\land,\qquad
\lor.
$$

Pero gran parte del razonamiento matemático utiliza una construcción distinta:

> «Si ocurre esto, entonces ocurre aquello».

Consideremos dos proposiciones:

$$
p=\text{«18 es múltiplo de 6»}
$$

y:

$$
q=\text{«18 es par»}.
$$

Podemos formar la afirmación:

> «Si 18 es múltiplo de 6, entonces 18 es par».

En símbolos escribiremos:

$$
p\Rightarrow q.
$$

La dificultad no está en leer la frase.

La dificultad está en precisar **cuándo debe considerarse falsa**.

La idea fundamental será:

$$
\boxed{
p\Rightarrow q
\text{ falla únicamente cuando }
p=\mathrm V
\text{ y }
q=\mathrm F.
}
$$

Todo lo demás en esta sección se organizará alrededor de este hecho.

---

### 3.1 La implicación

::: {.ma-block .ma-definicion #apm-t1-c02-d0015}
**Definición — Implicación**

La **implicación** de dos fórmulas $P$ y $Q$ es la fórmula:

$$
P\Rightarrow Q.
$$

Se lee «si $P$, entonces $Q$». Es falsa exactamente cuando $P$ es verdadera y $Q$ es falsa; en los demás casos es verdadera.
:::

En:

$$
P\Rightarrow Q,
$$

llamamos:

- **antecedente** a $P$;
- **consecuente** a $Q$.

Así, en:

$$
p\Rightarrow q,
$$

$p$ es el antecedente y $q$ es el consecuente.

La tabla completa es:

::: {.ma-block .ma-observacion}
En evaluaciones concretas escribiremos, por brevedad, expresiones como $\mathrm V\Rightarrow\mathrm F=\mathrm F$. Esto significa que una implicación cuyo antecedente recibe $\mathrm V$ y cuyo consecuente recibe $\mathrm F$ recibe a su vez $\mathrm F$; $\mathrm V$ y $\mathrm F$ son valores de verdad.
:::

| $P$ | $Q$ | $P\Rightarrow Q$ |
|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ |

La tabla puede parecer menos inmediata que las de conjunción o disyunción.

Por eso debemos entender qué afirma realmente una implicación.

---

### 3.2 La implicación descarta un caso

La fórmula:

$$
P\Rightarrow Q
$$

establece una condición:

> no debe ocurrir que $P$ sea verdadera y $Q$ sea falsa.

Podemos condensarlo así:

$$
\boxed{
P\Rightarrow Q
\text{ excluye el caso }
(\mathrm V,\mathrm F).
}
$$

Esta perspectiva explica toda la tabla.

#### Caso 1

$$
P=\mathrm V,
\qquad
Q=\mathrm V.
$$

El antecedente ocurre y el consecuente también.

La condición no ha fallado:

$$
P\Rightarrow Q=\mathrm V.
$$

#### Caso 2

$$
P=\mathrm V,
\qquad
Q=\mathrm F.
$$

El antecedente ocurre, pero el consecuente no.

Este es exactamente el caso prohibido:

$$
P\Rightarrow Q=\mathrm F.
$$

#### Caso 3

$$
P=\mathrm F,
\qquad
Q=\mathrm V.
$$

El antecedente no ocurre.

Por tanto, no estamos ante el caso «antecedente verdadero y consecuente falso».

La implicación recibe:

$$
\mathrm V.
$$

#### Caso 4

$$
P=\mathrm F,
\qquad
Q=\mathrm F.
$$

De nuevo, el antecedente es falso.

Tampoco aparece el único caso que haría falsa la implicación.

Por tanto:

$$
P\Rightarrow Q=\mathrm V.
$$

::: {.ma-block .ma-intuicion}
**Idea clave**

Una implicación no afirma que su antecedente sea verdadero. Afirma qué debe ocurrir con el consecuente **si** el antecedente es verdadero.
:::

---

### 3.3 ¿Por qué una implicación con antecedente falso es verdadera?

Este suele ser el punto más extraño al principio.

Consideremos:

$$
p=\text{«10 es impar»},
$$

$$
q=\text{«10 es mayor que 3»}.
$$

Tenemos:

$$
p=\mathrm F,
\qquad
q=\mathrm V.
$$

Entonces:

$$
p\Rightarrow q=\mathrm V.
$$

La fórmula no dice que 10 sea impar.

Tampoco afirma que ser impar sea la causa de ser mayor que 3.

Solo establece una relación lógica entre los valores de las dos proposiciones.

Como el antecedente:

$$
p
$$

es falso, no se produce la única situación que refutaría la implicación:

$$
p=\mathrm V,
\qquad
q=\mathrm F.
$$

Podemos pensar la implicación como una regla que solo puede violarse cuando el antecedente se cumple y el consecuente falla.

Esta interpretación será especialmente útil cuando construyamos tablas más complejas.

---

### 3.4 Implicación no significa causalidad

Consideremos:

$$
p=\text{«2+2=4»},
$$

$$
q=\text{«7 es primo»}.
$$

Ambas proposiciones son verdaderas.

Por tanto:

$$
p\Rightarrow q
$$

es verdadera.

Pero sería absurdo afirmar que:

> «$2+2=4$ causa que 7 sea primo».

La lógica proposicional no está describiendo aquí una relación causal.

Está evaluando la fórmula únicamente a partir de los valores de verdad de sus componentes.

No afirmamos que todos los usos cotidianos de «si..., entonces...» queden agotados por esta tabla. En este capítulo estamos definiendo y estudiando un conectivo matemático preciso: la implicación de la lógica proposicional clásica.

::: {.ma-block .ma-intuicion}
**Idea clave**

El símbolo $\Rightarrow$ expresa la implicación de la lógica proposicional clásica; por sí solo no significa «causa», «produce» ni «ocurre antes que».
:::

En argumentos matemáticos, las proposiciones implicadas suelen tener además una relación conceptual importante. Pero esa relación no forma parte de la tabla de verdad del conectivo.

---

### 3.5 Varias maneras de decir la misma implicación

La fórmula:

$$
P\Rightarrow Q
$$

puede expresarse en español de varias maneras.

#### Forma directa

> «Si $P$, entonces $Q$».

#### Con «cuando»

> «Cuando $P$, se cumple $Q$».

Esta formulación debe usarse con cuidado en contextos temporales, pero en matemáticas suele expresar la misma dirección condicional.

#### Con «solo si»

> «$P$ solo si $Q$».

Esto también corresponde a:

$$
P\Rightarrow Q.
$$

La expresión «solo si» merece especial atención.

Por ejemplo:

> «Doce es múltiplo de cuatro solo si doce es par».

La parte que aparece después de «solo si» expresa una condición que debe cumplirse cuando se cumple la primera.

Por eso:

$$
\boxed{
\text{«$P$ solo si $Q$»}
\quad\longrightarrow\quad
P\Rightarrow Q.
}
$$

---

### 3.6 Condición suficiente

Si:

$$
P\Rightarrow Q,
$$

diremos que:

> **$P$ es una condición suficiente para $Q$.**

¿Por qué «suficiente»?

Porque, dentro de la implicación, la verdad de $P$ basta para exigir la verdad de $Q$.

En símbolos:

$$
P=\mathrm V
$$

obliga, si la implicación ha de ser verdadera, a:

$$
Q=\mathrm V.
$$

Así:

$$
\boxed{
P\Rightarrow Q
\quad\text{se lee también como}\quad
\text{«$P$ es suficiente para $Q$».}
}
$$

La palabra «suficiente» señala el antecedente.

---

### 3.7 Condición necesaria

La misma implicación:

$$
P\Rightarrow Q
$$

puede leerse desde el otro extremo:

> **$Q$ es una condición necesaria para $P$.**

¿Por qué «necesaria»?

Porque si $P$ es verdadera, $Q$ no puede ser falsa sin hacer falsa la implicación.

Es decir, para que pueda ocurrir $P$ respetando la implicación, necesitamos que ocurra $Q$.

Por tanto:

$$
\boxed{
P\Rightarrow Q
}
$$

expresa simultáneamente:

- $P$ es suficiente para $Q$;
- $Q$ es necesaria para $P$.

Esta pareja de formulaciones debe aprenderse como una sola estructura.

---

### 3.8 «Si» y «solo si» apuntan en direcciones distintas

Comparemos:

> «$P$ si $Q$»

con:

> «$P$ solo si $Q$».

La primera significa:

> «Si $Q$, entonces $P$»,

por tanto:

$$
Q\Rightarrow P.
$$

La segunda significa:

> «Si $P$, entonces $Q$»,

por tanto:

$$
P\Rightarrow Q.
$$

Así:

$$
\boxed{
\text{«$P$ si $Q$»}
\quad\longrightarrow\quad
Q\Rightarrow P
}
$$

mientras que:

$$
\boxed{
\text{«$P$ solo si $Q$»}
\quad\longrightarrow\quad
P\Rightarrow Q.
}
$$

Esta inversión es una fuente frecuente de errores de lectura.

No conviene memorizarla sin sentido: basta preguntar **qué condición obliga a cuál**.

---

### 3.9 La conversa

A partir de:

$$
P\Rightarrow Q,
$$

podemos intercambiar antecedente y consecuente.

Obtenemos:

$$
Q\Rightarrow P.
$$

Esta fórmula se denomina la **conversa** de la implicación original.

Así:

| Fórmula | Forma |
|---|---|
| implicación original | $P\Rightarrow Q$ |
| conversa | $Q\Rightarrow P$ |

No debemos suponer que, porque una implicación sea verdadera, su conversa también lo sea.

Consideremos:

$$
p=\text{«12 es múltiplo de 4»},
$$

$$
q=\text{«12 es par»}.
$$

En este caso tanto:

$$
p\Rightarrow q
$$

como:

$$
q\Rightarrow p
$$

resultan verdaderas, porque $p$ y $q$ son verdaderas.

Pero este ejemplo concreto no demuestra una regla general sobre implicaciones y conversas.

Más adelante tendremos herramientas para comparar sistemáticamente fórmulas.

---

### 3.10 La contraposición asociada

A partir de:

$$
P\Rightarrow Q,
$$

podemos formar:

$$
\neg Q\Rightarrow\neg P.
$$

Llamaremos a esta fórmula la **contraposición asociada** a:

$$
P\Rightarrow Q.
$$

El esquema es:

| Fórmula | Forma |
|---|---|
| implicación original | $P\Rightarrow Q$ |
| conversa | $Q\Rightarrow P$ |
| contraposición asociada | $\neg Q\Rightarrow\neg P$ |

Por ahora solo estamos aprendiendo a **construir y reconocer** estas fórmulas.

Más adelante demostraremos qué relación lógica existe entre una implicación y su contraposición.

Y, todavía después, estudiaremos cómo puede aprovecharse esa relación en una demostración matemática.

::: {.ma-block .ma-intuicion}
**Idea clave**

En esta sección la contraposición es una fórmula asociada. No la usamos todavía como método general de demostración.
:::

---

### 3.11 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-t1-c02-x0011}
**Ejemplo — Una implicación y sus cuatro asignaciones**

:::

Consideremos simplemente:

$$
p\Rightarrow q.
$$

Queremos entender qué sucede en las cuatro posibles asignaciones de valores de verdad.

#### Fila 1

$$
p=\mathrm V,
\qquad
q=\mathrm V.
$$

El antecedente es verdadero y el consecuente también.

No se viola la condición:

$$
p\Rightarrow q=\mathrm V.
$$

#### Fila 2

$$
p=\mathrm V,
\qquad
q=\mathrm F.
$$

El antecedente es verdadero, pero el consecuente falla.

Esta es la única fila que refuta la implicación:

$$
p\Rightarrow q=\mathrm F.
$$

#### Fila 3

$$
p=\mathrm F,
\qquad
q=\mathrm V.
$$

El antecedente es falso.

La combinación no es el caso prohibido:

$$
p\Rightarrow q=\mathrm V.
$$

#### Fila 4

$$
p=\mathrm F,
\qquad
q=\mathrm F.
$$

De nuevo, el antecedente es falso.

Por tanto:

$$
p\Rightarrow q=\mathrm V.
$$

Reunimos los resultados:

| $p$ | $q$ | $p\Rightarrow q$ |
|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ |

La manera más compacta de recordar la tabla no es memorizar cuatro filas independientes, sino recordar:

$$
\boxed{
\text{una implicación es falsa únicamente en el caso }
\mathrm V\Rightarrow\mathrm F.
}
$$

---

## Ejercicios

### Evaluar implicaciones {#apm-t1-c02-e0069}

Determina el valor de verdad.

#### a)

$$
\mathrm V\Rightarrow\mathrm V
$$

#### b)

$$
\mathrm V\Rightarrow\mathrm F
$$

#### c)

$$
\mathrm F\Rightarrow\mathrm V
$$

#### d)

$$
\mathrm F\Rightarrow\mathrm F
$$

#### Solución

Por la tabla de la implicación:

#### a)

$$
\mathrm V\Rightarrow\mathrm V=\mathrm V.
$$

#### b)

$$
\mathrm V\Rightarrow\mathrm F=\mathrm F.
$$

#### c)

$$
\mathrm F\Rightarrow\mathrm V=\mathrm V.
$$

#### d)

$$
\mathrm F\Rightarrow\mathrm F=\mathrm V.
$$

El único caso falso es:

$$
\boxed{
\mathrm V\Rightarrow\mathrm F.
}
$$

---

### Evaluar desde proposiciones concretas {#apm-t1-c02-e0070}

Sea:

$$
p=\text{«14 es par»},
$$

$$
q=\text{«14 es mayor que 20»}.
$$

Determina el valor de verdad de:

#### a)

$$
p\Rightarrow q
$$

#### b)

$$
q\Rightarrow p
$$

#### c)

$$
\neg q\Rightarrow p
$$

#### Solución

Tenemos:

$$
p=\mathrm V,
\qquad
q=\mathrm F.
$$

#### a)

$$
p\Rightarrow q
=
\mathrm V\Rightarrow\mathrm F
=
\mathrm F.
$$

#### b)

$$
q\Rightarrow p
=
\mathrm F\Rightarrow\mathrm V
=
\mathrm V.
$$

#### c)

Como:

$$
q=\mathrm F,
$$

tenemos:

$$
\neg q=\mathrm V.
$$

Entonces:

$$
\neg q\Rightarrow p
=
\mathrm V\Rightarrow\mathrm V
=
\mathrm V.
$$

---

### Suficiente y necesaria {#apm-t1-c02-e0071}

Supón que:

$$
P\Rightarrow Q.
$$

Completa correctamente.

#### a)

$P$ es una condición ________ para $Q$.

#### b)

$Q$ es una condición ________ para $P$.

#### c)

«$P$ solo si $Q$» se representa como ________.

#### Solución

#### a)

$P$ es una condición **suficiente** para $Q$.

#### b)

$Q$ es una condición **necesaria** para $P$.

#### c)

$$
P\Rightarrow Q.
$$

Por tanto:

$$
\boxed{
P\Rightarrow Q
}
$$

puede leerse simultáneamente desde sus dos extremos: suficiente desde el antecedente y necesaria desde el consecuente.

---

### «Si» frente a «solo si» {#apm-t1-c02-e0072}

Traduce a símbolos.

#### a)

> «$P$ si $Q$».

#### b)

> «$P$ solo si $Q$».

#### c)

Explica por qué las direcciones son diferentes.

#### Solución

#### a)

«$P$ si $Q$» significa:

> «Si $Q$, entonces $P$».

Por tanto:

$$
Q\Rightarrow P.
$$

#### b)

«$P$ solo si $Q$» significa:

$$
P\Rightarrow Q.
$$

#### c)

En el primer caso, $Q$ funciona como condición suficiente para $P$.

En el segundo, $Q$ funciona como condición necesaria para $P$.

Las frases contienen las mismas letras, pero organizan la dependencia lógica en direcciones contrarias.

---

### ¿Causalidad o implicación? {#apm-t1-c02-e0073}

Sean:

$$
p=\text{«5+5=10»},
$$

$$
q=\text{«11 es primo»}.
$$

#### a)

Determina el valor de:

$$
p\Rightarrow q.
$$

#### b)

¿La verdad de esta implicación significa que $5+5=10$ causa que 11 sea primo?

#### Solución

#### a)

Ambas proposiciones son verdaderas:

$$
p=\mathrm V,
\qquad
q=\mathrm V.
$$

Por tanto:

$$
p\Rightarrow q=\mathrm V.
$$

#### b)

No.

La tabla de verdad de la implicación depende únicamente de los valores de verdad de $p$ y $q$.

El conectivo:

$$
\Rightarrow
$$

no expresa por sí mismo una relación causal.

---

### Explorar el antecedente falso {#apm-t1-c02-e0074}

Supón que:

$$
P=\mathrm F.
$$

#### a)

¿Cuál es el valor de:

$$
P\Rightarrow Q
$$

si $Q=\mathrm V$?

#### b)

¿Y si $Q=\mathrm F$?

#### c)

Formula con tus palabras una regla que describa lo observado.

#### Solución

#### a)

$$
\mathrm F\Rightarrow\mathrm V=\mathrm V.
$$

#### b)

$$
\mathrm F\Rightarrow\mathrm F=\mathrm V.
$$

#### c)

Cuando el antecedente de una implicación es falso, la implicación es verdadera independientemente del valor de verdad del consecuente.

Esto ocurre porque no aparece el único caso que hace falsa una implicación:

$$
\mathrm V\Rightarrow\mathrm F.
$$

---

### Una contraasignación para la conversa {#apm-t1-c02-e0075}

Considera las dos fórmulas:

$$
P\Rightarrow Q
$$

y:

$$
Q\Rightarrow P.
$$

Encuentra valores para $P$ y $Q$ tales que la primera sea verdadera y la segunda sea falsa.

#### Solución

Necesitamos que:

$$
Q\Rightarrow P
$$

sea falsa.

La única posibilidad es:

$$
Q=\mathrm V,
\qquad
P=\mathrm F.
$$

Con esos valores:

$$
P\Rightarrow Q
=
\mathrm F\Rightarrow\mathrm V
=
\mathrm V,
$$

mientras que:

$$
Q\Rightarrow P
=
\mathrm V\Rightarrow\mathrm F
=
\mathrm F.
$$

Por tanto, la asignación:

$$
\boxed{
P=\mathrm F,
\qquad
Q=\mathrm V
}
$$

muestra que una implicación y su conversa no tienen necesariamente el mismo valor de verdad.

---

### Síntesis: leer una condición {#apm-t1-c02-e0076}

Sea:

$$
p=\text{«24 es múltiplo de 6»},
$$

$$
q=\text{«24 es par»}.
$$

#### a)

Determina los valores de verdad de $p$ y $q$.

#### b)

Escribe:

> «Si $p$, entonces $q$».

#### c)

Expresa la misma dirección usando las palabras «suficiente» y «necesaria».

#### d)

Escribe la conversa.

#### e)

Escribe la contraposición asociada.

#### f)

Evalúa la implicación original, su conversa y su contraposición asociada para estos valores concretos.

#### Solución

#### a)

Veinticuatro es múltiplo de seis y es par. Por tanto:

$$
p=\mathrm V,
\qquad
q=\mathrm V.
$$

#### b)

La fórmula es:

$$
p\Rightarrow q.
$$

#### c)

Podemos decir:

> «$p$ es suficiente para $q$».

y:

> «$q$ es necesaria para $p$».

Ambas frases corresponden a la dirección:

$$
p\Rightarrow q.
$$

#### d)

La conversa es:

$$
q\Rightarrow p.
$$

#### e)

La contraposición asociada es:

$$
\neg q\Rightarrow\neg p.
$$

#### f)

Como:

$$
p=\mathrm V,
\qquad
q=\mathrm V,
$$

tenemos:

$$
p\Rightarrow q
=
\mathrm V\Rightarrow\mathrm V
=
\mathrm V.
$$

También:

$$
q\Rightarrow p
=
\mathrm V\Rightarrow\mathrm V
=
\mathrm V.
$$

Además:

$$
\neg q=\mathrm F,
\qquad
\neg p=\mathrm F,
$$

por lo que:

$$
\neg q\Rightarrow\neg p
=
\mathrm F\Rightarrow\mathrm F
=
\mathrm V.
$$

Este ejemplo concreto muestra que las tres fórmulas resultan verdaderas con esta asignación. No demuestra, por sí solo, una relación general entre ellas.

---

## Síntesis

La implicación:

$$
P\Rightarrow Q
$$

se lee:

> «Si $P$, entonces $Q$».

Su tabla es:

| $P$ | $Q$ | $P\Rightarrow Q$ |
|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ |

El principio central es:

$$
\boxed{
P\Rightarrow Q
\text{ es falsa únicamente cuando }
P=\mathrm V
\text{ y }
Q=\mathrm F.
}
$$

También hemos aprendido que:

$$
P\Rightarrow Q
$$

puede leerse como:

- $P$ es suficiente para $Q$;
- $Q$ es necesaria para $P$;
- $P$ solo si $Q$.

Y debemos distinguir:

$$
P\Rightarrow Q
$$

de su conversa:

$$
Q\Rightarrow P,
$$

y de su contraposición asociada:

$$
\neg Q\Rightarrow\neg P.
$$

Por ahora no afirmamos que estas fórmulas se comporten de la misma manera. Esa comparación necesitará herramientas que todavía estamos construyendo.

---

## Hacia la sección siguiente

Una implicación expresa una sola dirección:

$$
P\Rightarrow Q.
$$

Pero a veces queremos afirmar simultáneamente que:

- $P$ conduce a $Q$;
- $Q$ conduce a $P$.

En el lenguaje matemático aparece entonces la expresión:

> «$P$ si y solo si $Q$».

La siguiente sección introducirá el conectivo que representa esa relación de dos direcciones:

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

## §5. Tablas de verdad como instrumento semántico

Hasta ahora hemos evaluado fórmulas para asignaciones concretas.

Por ejemplo, si:

$$
p=\mathrm V,
\qquad
q=\mathrm F,
$$

podemos calcular:

$$
p\Rightarrow q=\mathrm F.
$$

Pero una fórmula como:

$$
\neg(p\land q)\lor r
$$

contiene tres variables proposicionales.

Cada una puede recibir:

$$
\mathrm V
$$

o:

$$
\mathrm F.
$$

Si queremos comprender **todo el comportamiento semántico** de la fórmula, no basta con elegir una o dos asignaciones convenientes.

Necesitamos considerar **todas** las posibilidades.

Ese es el propósito de una tabla de verdad.

La idea no es:

$$
\boxed{\text{probar algunos casos}}
$$

sino:

$$
\boxed{\text{enumerar exhaustivamente todas las asignaciones posibles}.}
$$

---

### 5.1 Asignaciones de valores de verdad

::: {.ma-block .ma-definicion #apm-t1-c02-d0017}
**Definición — Asignación de valores de verdad**

Una **asignación de valores de verdad** para unas variables proposicionales consiste en elegir para cada una de ellas uno de los dos valores:

$$
\mathrm V
\qquad\text{o}\qquad
\mathrm F.
$$
:::

Por ejemplo, para:

$$
p,
\qquad
q,
$$

una asignación posible es:

$$
p=\mathrm V,
\qquad
q=\mathrm F.
$$

Otra es:

$$
p=\mathrm F,
\qquad
q=\mathrm F.
$$

La tabla de verdad de una fórmula debe contener todas las asignaciones posibles de las variables que intervienen en ella.

---

### 5.2 ¿Cuántas filas necesitamos?

Comencemos con una sola variable:

$$
p.
$$

Tiene dos posibilidades:

| $p$ |
|---|
| $\mathrm V$ |
| $\mathrm F$ |

Por tanto, necesitamos:

$$
2
$$

filas.

Ahora consideremos dos variables:

$$
p,
\qquad
q.
$$

Por cada valor posible de $p$, la variable $q$ puede ser verdadera o falsa.

Obtenemos:

| $p$ | $q$ |
|---|---|
| $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ |

Hay:

$$
4=2^2
$$

filas.

Con tres variables:

$$
p,
\qquad
q,
\qquad
r,
$$

cada una tiene dos elecciones posibles.

El número total de asignaciones es:

$$
2\cdot2\cdot2=2^3=8.
$$

En general, si una fórmula contiene:

$$
n
$$

variables proposicionales distintas, hay:

$$
\boxed{2^n}
$$

asignaciones posibles.

La razón es sencilla: cada nueva variable duplica el número de filas.

---

### 5.3 Cómo generar las filas sin olvidar ninguna

Para tres variables utilizaremos normalmente este orden:

| $p$ | $q$ | $r$ |
|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm V$ | $\mathrm F$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |

Observemos el patrón:

- $p$ cambia cada cuatro filas;
- $q$ cambia cada dos filas;
- $r$ cambia en cada fila.

Esto garantiza que aparecen exactamente una vez las ocho combinaciones posibles.

::: {.ma-block .ma-intuicion}
**Idea clave**

El orden concreto de las filas no cambia la semántica de la fórmula. Lo esencial es que todas las asignaciones aparezcan exactamente una vez.
:::

Usaremos este orden estándar porque facilita revisar tablas y compararlas.

---

### 5.4 Una tabla se construye por subfórmulas

Consideremos:

$$
\neg(p\land q)\lor r.
$$

No conviene intentar evaluar toda la fórmula de un solo salto.

Primero identificamos su estructura.

El conectivo principal es:

$$
\lor.
$$

Las dos partes principales son:

$$
\neg(p\land q)
$$

y:

$$
r.
$$

Dentro de la primera aparece:

$$
p\land q.
$$

Por tanto, un orden natural de columnas es:

1. $p$;
2. $q$;
3. $r$;
4. $p\land q$;
5. $\neg(p\land q)$;
6. $\neg(p\land q)\lor r$.

Así trasladamos a una tabla el mismo principio que venimos usando:

$$
\boxed{
\text{estructura}
\longrightarrow
\text{subfórmulas}
\longrightarrow
\text{evaluación}.
}
$$

---

### 5.5 Columnas auxiliares

Llamaremos **columnas auxiliares** a las columnas que calculamos para subfórmulas antes de llegar a la fórmula completa.

Por ejemplo:

| $p$ | $q$ | $p\land q$ | $\neg(p\land q)$ |
|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ |

La columna:

$$
p\land q
$$

es necesaria para obtener:

$$
\neg(p\land q).
$$

Las columnas auxiliares cumplen dos funciones:

1. hacen visible la estructura de la fórmula;
2. permiten revisar cada paso si aparece un error.

Una tabla con menos columnas puede ser correcta, pero no siempre será pedagógicamente mejor.

En este libro preferiremos mostrar las subfórmulas relevantes mientras estamos aprendiendo el procedimiento.

---

### 5.6 Algoritmo de construcción

Para construir una tabla de verdad completa seguiremos este procedimiento.

#### Paso 1 — Identificar las variables proposicionales distintas

Por ejemplo, en:

$$
\neg(p\land q)\lor r
$$

aparecen:

$$
p,
\qquad
q,
\qquad
r.
$$

Por tanto:

$$
n=3.
$$

#### Paso 2 — Determinar el número de filas

Necesitamos:

$$
2^3=8
$$

filas.

#### Paso 3 — Escribir todas las asignaciones

Sin repeticiones y sin omisiones.

#### Paso 4 — Identificar las subfórmulas relevantes

Aquí:

$$
p\land q,
$$

$$
\neg(p\land q),
$$

y finalmente:

$$
\neg(p\land q)\lor r.
$$

#### Paso 5 — Completar las columnas desde dentro hacia fuera

Primero las subfórmulas interiores.

Al final, el conectivo principal.

#### Paso 6 — Revisar la tabla

Comprobar:

- que hay exactamente $2^n$ filas;
- que ninguna asignación falta;
- que ninguna aparece dos veces;
- que cada columna se calculó a partir de columnas ya conocidas;
- que la última columna corresponde a la fórmula completa.

Podemos condensarlo:

$$
\boxed{
\text{variables}
\to
\text{filas}
\to
\text{subfórmulas}
\to
\text{columnas auxiliares}
\to
\text{columna final}.
}
$$

---

### 5.7 Una tabla no es una muestra

Supongamos que queremos estudiar una fórmula con tres variables.

Si calculamos únicamente:

$$
p=\mathrm V,
\qquad
q=\mathrm V,
\qquad
r=\mathrm V,
$$

hemos estudiado una sola de:

$$
8
$$

asignaciones.

Aunque la fórmula resulte verdadera en esa fila, no sabemos todavía qué sucede en las otras siete.

Lo mismo ocurre si comprobamos tres, cuatro o incluso siete filas.

Una tabla de verdad completa tiene fuerza semántica porque **no deja ninguna asignación fuera**.

Por eso existe una diferencia esencial entre:

$$
\boxed{\text{ejemplos}}
$$

y:

$$
\boxed{\text{enumeración exhaustiva}.}
$$

Esta distinción será decisiva en la sección siguiente.

---

### 5.8 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-t1-c02-x0013}
**Ejemplo — Tabla completa de una fórmula de tres variables**

:::

Construyamos la tabla de:

$$
\neg(p\land q)\lor r.
$$

#### Paso 1 — Variables

Aparecen tres:

$$
p,
\qquad
q,
\qquad
r.
$$

Por tanto:

$$
2^3=8
$$

filas.

#### Paso 2 — Estructura

Calcularemos:

$$
p\land q,
$$

después:

$$
\neg(p\land q),
$$

y finalmente:

$$
\neg(p\land q)\lor r.
$$

#### Paso 3 — Tabla

| $p$ | $q$ | $r$ | $p\land q$ | $\neg(p\land q)$ | $\neg(p\land q)\lor r$ |
|---|---|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |

#### Paso 4 — Leer la columna final

La fórmula es falsa únicamente en la asignación:

$$
p=\mathrm V,
\qquad
q=\mathrm V,
\qquad
r=\mathrm F.
$$

En las otras siete asignaciones es verdadera.

Todavía no necesitamos poner un nombre especial a este comportamiento.

Por ahora basta con haber determinado exhaustivamente qué ocurre.

---

## Ejercicios

### Generar todas las asignaciones {#apm-t1-c02-e0083}

#### a)

Escribe todas las asignaciones posibles para:

$$
p,
\qquad
q.
$$

#### b)

¿Cuántas son?

#### c)

Escribe todas las asignaciones posibles para:

$$
p,
\qquad
q,
\qquad
r.
$$

#### d)

¿Cuántas son?

#### Solución

#### a)

| $p$ | $q$ |
|---|---|
| $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ |

#### b)

Hay:

$$
2^2=4
$$

asignaciones.

#### c)

| $p$ | $q$ | $r$ |
|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm V$ | $\mathrm F$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |

#### d)

Hay:

$$
2^3=8
$$

asignaciones.

---

### Tabla de dos variables {#apm-t1-c02-e0084}

Construye la tabla completa de:

$$
\neg p\lor q.
$$

#### Solución

Usamos las columnas:

$$
p,
\qquad
q,
\qquad
\neg p,
\qquad
\neg p\lor q.
$$

| $p$ | $q$ | $\neg p$ | $\neg p\lor q$ |
|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |

---

### Tres variables y dos niveles {#apm-t1-c02-e0085}

Construye la tabla de:

$$
(p\lor q)\land\neg r.
$$

#### Solución

Necesitamos ocho filas.

Las columnas auxiliares serán:

$$
p\lor q
$$

y:

$$
\neg r.
$$

| $p$ | $q$ | $r$ | $p\lor q$ | $\neg r$ | $(p\lor q)\land\neg r$ |
|---|---|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ |

---

### Una tabla con implicación {#apm-t1-c02-e0086}

Construye la tabla de:

$$
(p\land q)\Rightarrow p.
$$

#### Solución

Primero calculamos:

$$
p\land q.
$$

| $p$ | $q$ | $p\land q$ | $(p\land q)\Rightarrow p$ |
|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ |

La columna final contiene:

$$
\mathrm V
$$

en las cuatro filas.

Guardaremos esta observación para la sección siguiente.

---

### ¿Por qué aparecen $2^n$ filas? {#apm-t1-c02-e0087}

Explica por qué una fórmula que contiene cuatro variables proposicionales distintas requiere:

$$
2^4=16
$$

filas en una tabla de verdad completa.

No basta con escribir el resultado: explica la razón.

#### Solución

Cada variable proposicional tiene dos valores posibles:

$$
\mathrm V
\qquad\text{o}\qquad
\mathrm F.
$$

Con una variable tenemos dos posibilidades.

Al añadir una segunda variable, cada posibilidad anterior se divide en dos, por lo que obtenemos:

$$
2\cdot2.
$$

Al añadir una tercera:

$$
2\cdot2\cdot2.
$$

Y con cuatro:

$$
2\cdot2\cdot2\cdot2
=
2^4
=
16.
$$

Cada nueva variable duplica el número de asignaciones.

---

### Diagnosticar una tabla incompleta {#apm-t1-c02-e0088}

Un estudiante quiere construir una tabla para una fórmula con tres variables y escribe únicamente estas filas:

| $p$ | $q$ | $r$ |
|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |

Afirma:

> «Hay valores verdaderos y falsos para cada variable, así que ya consideré todos los casos».

Explica el error.

#### Solución

Tener alguna aparición de:

$$
\mathrm V
$$

y:

$$
\mathrm F
$$

en cada columna no basta.

Con tres variables existen:

$$
2^3=8
$$

asignaciones diferentes.

El estudiante solo escribió cuatro.

Faltan, por ejemplo:

$$
(\mathrm V,\mathrm V,\mathrm F),
$$

$$
(\mathrm V,\mathrm F,\mathrm F),
$$

$$
(\mathrm F,\mathrm V,\mathrm V),
$$

y:

$$
(\mathrm F,\mathrm F,\mathrm V).
$$

Una tabla completa debe enumerar **cada combinación posible**, no solo utilizar ambos valores en cada variable.

---

### Síntesis: implicación y contraposición asociada {#apm-t1-c02-e0089}

Construye una tabla completa para:

$$
(p\Rightarrow q)
\leftrightarrow
(\neg q\Rightarrow\neg p).
$$

Usa columnas auxiliares suficientes para que cada paso pueda revisarse.

Después describe qué observas en la columna final, sin utilizar todavía ningún término técnico nuevo.

#### Solución

Necesitamos las columnas:

$$
\neg q,
$$

$$
\neg p,
$$

$$
p\Rightarrow q,
$$

$$
\neg q\Rightarrow\neg p,
$$

y finalmente el bicondicional.

| $p$ | $q$ | $\neg p$ | $\neg q$ | $p\Rightarrow q$ | $\neg q\Rightarrow\neg p$ | $(p\Rightarrow q)\leftrightarrow(\neg q\Rightarrow\neg p)$ |
|---|---|---|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |

La columna final recibe:

$$
\mathrm V
$$

en las cuatro asignaciones.

Además, las columnas:

$$
p\Rightarrow q
$$

y:

$$
\neg q\Rightarrow\neg p
$$

coinciden fila por fila.

Todavía no necesitamos poner un nombre técnico a estos dos hechos.

En las secciones siguientes estudiaremos precisamente qué significa que una fórmula sea verdadera en todas las asignaciones y qué significa que dos fórmulas tengan columnas idénticas.

---

## Síntesis

Una tabla de verdad enumera exhaustivamente las asignaciones de valores de verdad de las variables proposicionales de una fórmula.

Si aparecen:

$$
n
$$

variables distintas, necesitamos:

$$
\boxed{2^n}
$$

filas.

La construcción sigue un orden estructural:

$$
\boxed{
\text{variables}
\to
\text{todas las asignaciones}
\to
\text{subfórmulas}
\to
\text{columnas auxiliares}
\to
\text{fórmula completa}.
}
$$

El hábito que debemos evitar es:

> «He probado varias filas; probablemente las demás se comportan igual».

Una tabla de verdad completa no se apoya en una muestra.

Su fuerza está en que:

$$
\boxed{\text{no deja ninguna asignación fuera}.}
$$

---

## Hacia la sección siguiente

En [el ejercicio «Una tabla con implicación»](#apm-t1-c02-e0086) apareció una fórmula cuya columna final contiene:

$$
\mathrm V
$$

en todas las filas.

En [el ejercicio «Síntesis: implicación y contraposición asociada»](#apm-t1-c02-e0089) ocurrió lo mismo con una fórmula más compleja.

También podríamos encontrar fórmulas que sean falsas en todas las filas, o fórmulas que cambien de valor según la asignación.

Estas tres posibilidades reciben nombres específicos.

La siguiente sección estudiará:

## §6. Tautologías, contradicciones y contingencias

En la sección anterior construimos tablas de verdad completas.

Vimos, por ejemplo, que:

$$
(p\land q)\Rightarrow p
$$

recibe:

$$
\mathrm V
$$

en las cuatro asignaciones posibles de $p$ y $q$.

También vimos que una fórmula como:

$$
\neg(p\land q)\lor r
$$

puede ser verdadera en algunas asignaciones y falsa en otras.

Estas diferencias permiten clasificar las fórmulas según el comportamiento de **toda su columna final**.

La pregunta ya no será únicamente:

> «¿Qué valor recibe esta fórmula en esta fila?»

Ahora preguntaremos:

> «¿Qué valores recibe la fórmula cuando recorremos todas las asignaciones posibles?»

Aparecen tres comportamientos básicos:

$$
\boxed{
\text{siempre verdadera},
\qquad
\text{siempre falsa},
\qquad
\text{a veces verdadera y a veces falsa}.
}
$$

### 6.1 Tautologías

Consideremos:

$$
p\lor\neg p.
$$

| $p$ | $\neg p$ | $p\lor\neg p$ |
|---|---|---|
| $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |

La columna final contiene $\mathrm V$ en todas las filas.

::: {.ma-block .ma-definicion #apm-t1-c02-d0018}
**Definición — Tautología**

Una **tautología** es una fórmula proposicional que recibe el valor $\mathrm V$ en todas las asignaciones posibles de sus variables proposicionales.
:::

Por tanto:

$$
p\lor\neg p
$$

es una tautología.

El punto decisivo no es que hayamos encontrado una fila donde la fórmula sea verdadera, sino que **no existe ninguna fila de su tabla completa donde sea falsa**.

$$
\boxed{
\text{columna final toda }\mathrm V
\quad\longrightarrow\quad
\text{tautología}.
}
$$

### 6.2 Verdadera en una fila no significa tautológica

Consideremos:

$$
p\Rightarrow q.
$$

Si:

$$
p=\mathrm V,
\qquad
q=\mathrm V,
$$

entonces:

$$
p\Rightarrow q=\mathrm V.
$$

Pero eso no basta para afirmar que $p\Rightarrow q$ sea una tautología.

| $p$ | $q$ | $p\Rightarrow q$ |
|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ |

Aparece una fila falsa.

::: {.ma-block .ma-intuicion}
**Idea clave**

«La fórmula es verdadera para esta asignación» y «la fórmula es una tautología» son afirmaciones diferentes.
:::

La primera habla de **una fila**. La segunda habla de **toda la tabla**.

### 6.3 Contraasignaciones

Supongamos que alguien afirma:

> «$P$ es una tautología».

Para refutar esa afirmación basta encontrar una asignación en la que:

$$
P=\mathrm F.
$$

Llamaremos a esa asignación una **contraasignación** para la pretendida tautología.

Por ejemplo, para:

$$
p\Rightarrow q,
$$

tomamos:

$$
p=\mathrm V,
\qquad
q=\mathrm F.
$$

Entonces:

$$
p\Rightarrow q=\mathrm F.
$$

Esta única fila basta para concluir que $p\Rightarrow q$ no es una tautología.

La lógica es la misma que ya conocimos con contraejemplos algebraicos:

$$
\boxed{
\text{una sola excepción basta para refutar una afirmación sobre todos los casos}.
}
$$

Aquí no necesitamos todavía cuantificadores formales: la tabla contiene la lista finita de asignaciones que estamos examinando.

### 6.4 Contradicciones

Consideremos:

$$
p\land\neg p.
$$

| $p$ | $\neg p$ | $p\land\neg p$ |
|---|---|---|
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ |

La columna final contiene $\mathrm F$ en todas las filas.

::: {.ma-block .ma-definicion #apm-t1-c02-d0019}
**Definición — Contradicción**

Una **contradicción** es una fórmula proposicional que recibe el valor $\mathrm F$ en todas las asignaciones posibles de sus variables proposicionales.
:::

Por tanto:

$$
p\land\neg p
$$

es una contradicción.

$$
\boxed{
\text{columna final toda }\mathrm F
\quad\longrightarrow\quad
\text{contradicción}.
}
$$

Una fórmula no se convierte en contradicción por ser falsa en una sola fila. Debe ser falsa en **todas**.

### 6.5 Cómo refutar una pretendida contradicción

La situación es dual.

Si alguien afirma:

> «$P$ es una contradicción»,

basta encontrar una asignación en la que:

$$
P=\mathrm V
$$

para refutarlo.

Por ejemplo, $p\land q$ es falsa en varias asignaciones. Pero si:

$$
p=\mathrm V,
\qquad
q=\mathrm V,
$$

entonces:

$$
p\land q=\mathrm V.
$$

Por tanto, $p\land q$ no es una contradicción.

### 6.6 Contingencias

Nos queda el tercer comportamiento.

Consideremos nuevamente:

$$
p\Rightarrow q.
$$

Su columna final contiene ambos valores.

::: {.ma-block .ma-definicion #apm-t1-c02-d0020}
**Definición — Contingencia**

Una **contingencia** es una fórmula proposicional que recibe el valor $\mathrm V$ en al menos una asignación y el valor $\mathrm F$ en al menos otra.
:::

Por tanto:

$$
p\Rightarrow q
$$

es una contingencia.

$$
\boxed{
\text{la columna final contiene }\mathrm V\text{ y }\mathrm F
\quad\longrightarrow\quad
\text{contingencia}.
}
$$

Una contingencia depende realmente de la asignación: no es siempre verdadera ni siempre falsa.

### 6.7 Los tres comportamientos son excluyentes

Una fórmula no puede pertenecer simultáneamente a dos de estas tres clases.

| Columna final | Clasificación |
|---|---|
| solo $\mathrm V$ | tautología |
| solo $\mathrm F$ | contradicción |
| aparecen $\mathrm V$ y $\mathrm F$ | contingencia |

Para una fórmula con tabla completa, exactamente una de estas tres posibilidades ocurre.

### 6.8 Clasificar sin hacer trabajo innecesario

No siempre necesitamos construir una tabla completa para **descartar** una clasificación.

#### Para refutar «tautología»

Basta una fila falsa.

#### Para refutar «contradicción»

Basta una fila verdadera.

#### Para demostrar «contingencia»

Basta encontrar:

- una asignación verdadera;
- una asignación falsa.

Por ejemplo, consideremos:

$$
p\land q.
$$

Con:

$$
p=\mathrm V,
\qquad
q=\mathrm V,
$$

obtenemos:

$$
p\land q=\mathrm V.
$$

Con:

$$
p=\mathrm V,
\qquad
q=\mathrm F,
$$

obtenemos:

$$
p\land q=\mathrm F.
$$

Ya podemos concluir que $p\land q$ es una contingencia.

::: {.ma-block .ma-observacion}
La tabla completa sigue siendo el procedimiento general de referencia. Pero, cuando buscamos refutar «siempre verdadera», refutar «siempre falsa» o demostrar que aparecen ambos valores, unas pocas asignaciones estratégicas pueden bastar.
:::

### 6.9 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-t1-c02-x0014}
**Ejemplo — Tres comportamientos semánticos**

:::

Clasifiquemos:

$$
P_1=p\lor\neg p,
$$

$$
P_2=p\land\neg p,
$$

$$
P_3=p\Rightarrow q.
$$

#### Primera fórmula

| $p$ | $\neg p$ | $p\lor\neg p$ |
|---|---|---|
| $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |

La columna final contiene solo $\mathrm V$. Por tanto, $P_1$ es una **tautología**.

#### Segunda fórmula

| $p$ | $\neg p$ | $p\land\neg p$ |
|---|---|---|
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ |

La columna final contiene solo $\mathrm F$. Por tanto, $P_2$ es una **contradicción**.

#### Tercera fórmula

| $p$ | $q$ | $p\Rightarrow q$ |
|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ |

La columna final contiene ambos valores. Por tanto, $P_3$ es una **contingencia**.

$$
\boxed{
\begin{array}{c}
p\lor\neg p:\ \text{tautología},\\
p\land\neg p:\ \text{contradicción},\\
p\Rightarrow q:\ \text{contingencia}.
\end{array}
}
$$

## Ejercicios

### Clasificar por tabla {#apm-t1-c02-e0090}

Clasifica cada fórmula como tautología, contradicción o contingencia.

#### a)

$$
p\lor\neg p
$$

#### b)

$$
p\land\neg p
$$

#### c)

$$
p\land q
$$

#### Solución

#### a)

La columna final de $p\lor\neg p$ es toda $\mathrm V$. Por tanto:

$$
\boxed{\text{tautología}}.
$$

#### b)

La columna final de $p\land\neg p$ es toda $\mathrm F$. Por tanto:

$$
\boxed{\text{contradicción}}.
$$

#### c)

| $p$ | $q$ | $p\land q$ |
|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |

Aparecen $\mathrm V$ y $\mathrm F$. Por tanto:

$$
\boxed{\text{contingencia}}.
$$

### Verdadera no significa tautológica {#apm-t1-c02-e0091}

Un estudiante observa que $p\Rightarrow q$ es verdadera cuando:

$$
p=\mathrm F,
\qquad
q=\mathrm F.
$$

Concluye:

> «Entonces $p\Rightarrow q$ es una tautología».

Explica el error y clasifica correctamente la fórmula.

#### Solución

Una tautología debe ser verdadera en todas las asignaciones. La asignación dada solo comprueba una fila.

Tomemos:

$$
p=\mathrm V,
\qquad
q=\mathrm F.
$$

Entonces:

$$
p\Rightarrow q=\mathrm F.
$$

Esta contraasignación demuestra que la fórmula no es una tautología.

Como existen filas verdaderas y una fila falsa:

$$
\boxed{p\Rightarrow q\text{ es una contingencia}.}
$$

### Explorar una fórmula {#apm-t1-c02-e0092}

Considera:

$$
(p\land q)\Rightarrow q.
$$

#### a)

Antes de construir la tabla completa, intenta encontrar una asignación que haga falsa la fórmula.

#### b)

Construye después la tabla completa.

#### c)

Clasifica la fórmula.

#### Solución

#### a)

Para que una implicación sea falsa necesitamos antecedente verdadero y consecuente falso.

Si $p\land q$ fuera verdadero, entonces $q$ tendría que ser verdadero. Pero para hacer falsa la implicación necesitaríamos $q=\mathrm F$. Las dos exigencias son incompatibles.

#### b)

| $p$ | $q$ | $p\land q$ | $(p\land q)\Rightarrow q$ |
|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ |

#### c)

La columna final es toda $\mathrm V$. Por tanto:

$$
\boxed{(p\land q)\Rightarrow q\text{ es una tautología}.}
$$

### Contraasignación {#apm-t1-c02-e0093}

Alguien afirma que:

$$
(p\lor q)\Rightarrow p
$$

es una tautología.

Encuentra una contraasignación y explica por qué basta para refutar la afirmación.

#### Solución

Tomemos:

$$
p=\mathrm F,
\qquad
q=\mathrm V.
$$

Entonces:

$$
p\lor q=\mathrm V,
$$

y:

$$
(p\lor q)\Rightarrow p
=
\mathrm V\Rightarrow\mathrm F
=
\mathrm F.
$$

Una tautología tendría que ser verdadera en todas las asignaciones. Una sola fila falsa basta para refutar la afirmación.

### Refutar una pretendida contradicción {#apm-t1-c02-e0094}

Un estudiante afirma que:

$$
p\land q
$$

es una contradicción porque suele ser falsa.

Encuentra una asignación que refute esa afirmación.

#### Solución

Tomemos:

$$
p=\mathrm V,
\qquad
q=\mathrm V.
$$

Entonces:

$$
p\land q
=
\mathrm V\land\mathrm V
=
\mathrm V.
$$

Una contradicción debe ser falsa en todas las asignaciones. Esta única fila verdadera basta para refutar la afirmación.

De hecho, como la fórmula también es falsa en otras asignaciones, es una contingencia.

### Síntesis: clasificar con estrategia {#apm-t1-c02-e0095}

Clasifica:

$$
(p\Rightarrow q)\land(q\Rightarrow p).
$$

Puedes construir una tabla completa o reducir el trabajo mediante asignaciones estratégicas, pero debes justificar la clasificación.

#### Solución

Busquemos primero una asignación verdadera.

Si:

$$
p=\mathrm V,
\qquad
q=\mathrm V,
$$

entonces ambas implicaciones son verdaderas, y por tanto:

$$
(p\Rightarrow q)\land(q\Rightarrow p)=\mathrm V.
$$

Ahora busquemos una asignación falsa.

Tomemos:

$$
p=\mathrm V,
\qquad
q=\mathrm F.
$$

Entonces:

$$
p\Rightarrow q=\mathrm F,
$$

mientras que:

$$
q\Rightarrow p=\mathrm V.
$$

Por tanto:

$$
(p\Rightarrow q)\land(q\Rightarrow p)
=
\mathrm F\land\mathrm V
=
\mathrm F.
$$

Hemos encontrado una asignación verdadera y otra falsa. Por definición:

$$
\boxed{
(p\Rightarrow q)\land(q\Rightarrow p)
\text{ es una contingencia}.
}
$$

## Síntesis

La columna final de una tabla completa permite clasificar una fórmula.

Si contiene únicamente $\mathrm V$, tenemos una **tautología**.

Si contiene únicamente $\mathrm F$, tenemos una **contradicción**.

Si contiene ambos valores, tenemos una **contingencia**.

También hemos aprendido una herramienta de refutación muy eficiente:

$$
\boxed{
\text{una sola fila falsa refuta una pretendida tautología}.
}
$$

Y, de manera dual:

$$
\boxed{
\text{una sola fila verdadera refuta una pretendida contradicción}.
}
$$

Para demostrar que una fórmula es contingente basta exhibir dos asignaciones adecuadas: una que produzca $\mathrm V$ y otra que produzca $\mathrm F$.

## Hacia la sección siguiente

Hasta ahora hemos clasificado **una fórmula** observando su columna final.

Pero en [el ejercicio «Síntesis: implicación y contraposición asociada»](#apm-t1-c02-e0089) vimos algo diferente: dos fórmulas distintas,

$$
p\Rightarrow q
$$

y:

$$
\neg q\Rightarrow\neg p,
$$

produjeron exactamente la misma columna en todas las asignaciones.

Esto sugiere una nueva pregunta:

> ¿Cuándo podemos considerar que dos fórmulas distintas tienen exactamente el mismo comportamiento lógico?

La siguiente sección introducirá el concepto que permitirá responderla:

## §7. Equivalencia lógica

En [el ejercicio «Síntesis: implicación y contraposición asociada»](#apm-t1-c02-e0089) construimos una tabla para: $p\Rightarrow q$ y $\neg q\Rightarrow\neg p$.

Obtuvimos:

| $p$ | $q$ | $p\Rightarrow q$ | $\neg q\Rightarrow\neg p$ |
|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |

Las dos fórmulas tienen formas distintas.

Sin embargo, sus columnas coinciden fila por fila. Eso sugiere una idea nueva.

Hasta ahora preguntábamos:

> «¿Qué valor de verdad recibe una fórmula?»

Ahora preguntaremos:

> «¿Pueden dos fórmulas distintas tener exactamente el mismo comportamiento bajo todas las asignaciones?»

La respuesta es sí. Y esta será la noción que convertirá poco a poco la lógica proposicional en un **álgebra de fórmulas**.

---

### 7.1 Misma columna, mismo comportamiento lógico

Consideremos dos fórmulas: $P$ y $Q$ Para compararlas debemos construir una tabla conjunta que incluya todas las variables proposicionales que aparezcan en cualquiera de las dos.

Supongamos que, fila por fila, ocurre siempre:

- cuando $P$ recibe $\mathrm V$, también $Q$ recibe $\mathrm V$;
- cuando $P$ recibe $\mathrm F$, también $Q$ recibe $\mathrm F$.

Entonces las columnas de: $P$ y $Q$ son idénticas.

No significa necesariamente que las fórmulas tengan la misma escritura.

Significa que **ninguna asignación de valores de verdad permite distinguirlas semánticamente**.

---

### 7.2 Equivalencia lógica

::: {.ma-block .ma-definicion #apm-t1-c02-d0021}
**Definición — Equivalencia lógica**

Dos fórmulas proposicionales $P$ y $Q$ son **lógicamente equivalentes** cuando reciben el mismo valor de verdad en cada asignación de valores de verdad de todas las variables que aparecen en $P$ o en $Q$.

Escribiremos:

$$
P\equiv Q.
$$
:::

Por tanto:

$$
\boxed{
P\equiv Q
\quad\text{significa que las columnas de }P\text{ y }Q
\text{ coinciden fila por fila}.
}
$$

Esta definición contiene una exigencia fuerte. No basta con encontrar:

- una fila donde coincidan;
- varias filas donde coincidan;
- casi todas las filas donde coincidan.

Para afirmar:

$$
P\equiv Q,
$$

las columnas deben coincidir en **toda** la tabla conjunta.

---

### 7.3 Cómo refutar una pretendida equivalencia

Supongamos que alguien afirma $P\equiv Q$ Para refutarlo basta encontrar una asignación donde: $P$ y $Q$ reciban valores distintos.

Por ejemplo, comparemos: $p\lor q$ y $p\land q$. Tomemos:

$$
p=\mathrm V,
\qquad
q=\mathrm F.
$$

Entonces $p\lor q=\mathrm V$, mientras que:

$$
p\land q=\mathrm F.
$$

Por tanto: $p\lor q$ y $p\land q$ no son lógicamente equivalentes.

No necesitamos completar las otras tres filas para refutar la equivalencia.

La asignación:

$$
p=\mathrm V,
\qquad
q=\mathrm F
$$

funciona como **contraasignación**. Así:

$$

\text{una sola fila distinta refuta una pretendida equivalencia}.

$$

---

### 7.4 Bicondicional y equivalencia lógica no son lo mismo

Esta es una distinción central del capítulo. La escritura $P\leftrightarrow Q$ es una **fórmula proposicional**.

En cada asignación recibe: $\mathrm V$ o $\mathrm F$.

En cambio, $P\equiv Q$ expresa que las fórmulas $P$ y $Q$ tienen la misma columna completa.

En este capítulo, $\equiv$ pertenece al lenguaje con el que **hablamos acerca de las fórmulas**: no añadimos una columna «$P\equiv Q$» a la tabla como si fuera un nuevo conectivo. Para verificarlo, comparamos las columnas de $P$ y $Q$.

Podemos resumir:

| Escritura | Función |
|---|---|
| $P\leftrightarrow Q$ | fórmula proposicional |
| $P\equiv Q$ | afirmación de equivalencia lógica entre fórmulas |

Por ejemplo, en una asignación concreta puede ocurrir:

$$
P\leftrightarrow Q=\mathrm V.
$$

Eso solo nos dice que $P$ y $Q$ tienen el mismo valor **en esa fila**.

Todavía no permite concluir:

$$
P\equiv Q.
$$

Para esta última afirmación debemos comparar todas las filas.

::: {.ma-block .ma-intuicion}
**Idea clave**

El bicondicional compara los valores de $P$ y $Q$ **dentro de una asignación**.

La equivalencia lógica exige que esa coincidencia se mantenga **a través de todas las asignaciones**.
:::

---

### 7.5 El criterio mediante el bicondicional

La relación entre ambas ideas es, sin embargo, muy estrecha.

Si:

$$
P\equiv Q,
$$

entonces en cada fila $P$ y $Q$ tienen el mismo valor.

Pero el bicondicional:

$$
P\leftrightarrow Q
$$

es verdadero precisamente cuando sus dos componentes tienen el mismo valor.

Por tanto, si $P$ y $Q$ son equivalentes, el bicondicional debe ser verdadero en todas las filas.

Eso significa que:

$$
P\leftrightarrow Q
$$

es una tautología. Y el razonamiento también funciona en la dirección inversa.

Podemos formularlo como nuestro primer resultado formal del capítulo.

::: {.ma-block .ma-enunciado #apm-t1-c02-p0001}
**Proposición — Criterio bicondicional para la equivalencia lógica**

Sean $P$ y $Q$ fórmulas proposicionales. Entonces $P$ y $Q$ son lógicamente equivalentes si y solo si:

$$
P\leftrightarrow Q
$$

es una tautología.
:::

#### Lectura del resultado

La proposición conecta dos niveles:

1. comparar directamente las columnas de $P$ y $Q$;
2. construir una nueva fórmula $P\leftrightarrow Q$ y observar su columna.

Afirma que ambos procedimientos contienen exactamente la misma información.

#### Demostración

Construimos una tabla conjunta con todas las variables que aparecen en $P$ o en $Q$.

##### Primera dirección

Supongamos que:

$$
P\equiv Q.
$$

Por definición, en cada fila de la tabla conjunta, $P$ y $Q$ reciben el mismo valor de verdad.

Pero:

$$
P\leftrightarrow Q
$$

recibe $\mathrm V$ exactamente cuando $P$ y $Q$ tienen el mismo valor.

En cada fila:

$$
P\leftrightarrow Q=\mathrm V.
$$

Así, la columna completa del bicondicional contiene únicamente:

$$
\mathrm V.
$$

Luego:

$$
P\leftrightarrow Q
$$

es una tautología.

##### Segunda dirección

Supongamos ahora que:

$$
P\leftrightarrow Q
$$

es una tautología. Entonces su columna recibe $\mathrm V$ en cada fila de la tabla conjunta.

Por la definición del bicondicional, eso significa que en cada fila: $P$ y $Q$ reciben el mismo valor de verdad.

Por tanto, sus columnas coinciden fila por fila. Luego:

$$
P\equiv Q.
$$

Quedan demostradas las dos direcciones.

$$
\boxed{
P\equiv Q
\quad\text{exactamente cuando}\quad
P\leftrightarrow Q
\text{ es una tautología}.
}
$$

---

### 7.6 Dos procedimientos para demostrar una equivalencia

A partir de ahora tenemos dos procedimientos semánticos muy próximos.

#### Procedimiento A — Comparar columnas

Construimos la tabla de: $P$ y $Q$. Si las columnas coinciden completamente:

$$
P\equiv Q.
$$

#### Procedimiento B — Usar el criterio bicondicional

Construimos:

$$
P\leftrightarrow Q.
$$

Si su columna es toda:

$$
\mathrm V,
$$

entonces, por [la proposición «Criterio bicondicional para la equivalencia lógica»](#apm-t1-c02-p0001):

$$
P\equiv Q.
$$

En esta etapa ambos métodos siguen dependiendo de tablas.

Más adelante aprenderemos a demostrar equivalencias mediante **leyes ya establecidas**, sin reconstruir una tabla completa cada vez.

---

### 7.7 Una equivalencia puede cambiar mucho la forma

Consideremos $\neg(p\land q)$ y $\neg p\lor\neg q$. Las fórmulas no se parecen superficialmente.

La primera tiene como conectivo principal:

$$
\neg.
$$

La segunda tiene como conectivo principal:

$$
\lor.
$$

Construyamos una tabla:

| $p$ | $q$ | $p\land q$ | $\neg(p\land q)$ | $\neg p$ | $\neg q$ | $\neg p\lor\neg q$ |
|---|---|---|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |

Las dos columnas destacadas conceptualmente son: $\neg(p\land q)$ y $\neg p\lor\neg q$.

Coinciden fila por fila. Por tanto:

$$
\boxed{
\neg(p\land q)
\equiv
\neg p\lor\neg q.
}
$$

Más adelante este hecho formará parte de una familia de leyes con nombre propio.

Por ahora lo importante es cómo lo hemos establecido: **directamente desde la semántica**.

---

### 7.8 Igualdad y equivalencia tampoco son lo mismo

En álgebra escribimos, por ejemplo:

$$
2(x+1)=2x+2.
$$

Allí:

$$
=
$$

expresa igualdad entre valores matemáticos. En lógica proposicional escribiremos:

$$
\neg(p\land q)
\equiv
\neg p\lor\neg q.
$$

Aquí:

$$
\equiv
$$

expresa equivalencia lógica entre fórmulas. No intercambiaremos ambos símbolos.

La disciplina de notación queda:

$$

=
\neq
\equiv
\neq
\leftrightarrow.

$$

Cada símbolo expresa una relación diferente.

---

### 7.9 Cadenas de equivalencias

Supongamos que ya hemos justificado: $P\equiv Q$ y $Q\equiv R$. En cada fila:

- $P$ y $Q$ tienen el mismo valor;
- $Q$ y $R$ tienen el mismo valor.

En esa misma fila:

- $P$ y $R$ tienen el mismo valor.

Como esto ocurre en toda la tabla conjunta:

$$
P\equiv R.
$$

Esto nos permitirá escribir cadenas como:

$$
P
\equiv
Q
\equiv
R.
$$

Pero aparece una nueva exigencia de rigor:

::: {.ma-block .ma-intuicion}
**Idea clave**

Cada paso de una cadena de equivalencias debe estar justificado.
:::

Todavía conocemos pocas equivalencias reutilizables. Las secciones siguientes construirán precisamente ese repertorio.

---

### 7.10 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-t1-c02-x0015}
**Ejemplo — Demostrar una equivalencia por tabla**
:::

Demostremos:

$$
\neg(p\land q)
\equiv
\neg p\lor\neg q.
$$

#### Paso 1 — Variables

Ambas fórmulas dependen de:

$$
p,
\qquad
q.
$$

Necesitamos:

$$
2^2=4
$$

filas.

#### Paso 2 — Subfórmulas

Para la primera fórmula necesitamos:

$$
p\land q
$$

y después:

$$
\neg(p\land q).
$$

Para la segunda necesitamos:

$$
\neg p,
\qquad
\neg q,
$$

y finalmente:

$$
\neg p\lor\neg q.
$$

#### Paso 3 — Tabla conjunta

| $p$ | $q$ | $p\land q$ | $\neg(p\land q)$ | $\neg p$ | $\neg q$ | $\neg p\lor\neg q$ |
|---|---|---|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |

Las columnas de: $\neg(p\land q)$ y $\neg p\lor\neg q$ son idénticas.

#### Conclusión

Por definición de equivalencia lógica:

$$
\boxed{
\neg(p\land q)
\equiv
\neg p\lor\neg q.
}
$$

Además, por [la proposición «Criterio bicondicional para la equivalencia lógica»](#apm-t1-c02-p0001), podemos concluir que:

$$
\neg(p\land q)
\leftrightarrow
(\neg p\lor\neg q)
$$

es una tautología.

---
## Ejercicios

### Doble negación por tabla {#apm-t1-c02-e0096}
Construye una tabla para comparar:

$$
\neg\neg p
$$

y:

$$
p.
$$

Decide si son lógicamente equivalentes.

#### Solución


| $p$ | $\neg p$ | $\neg\neg p$ |
|---|---|---|
| $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ |

La columna de:

$$
\neg\neg p
$$

coincide con la de:

$$
p.
$$

Por tanto:

$$
\boxed{
\neg\neg p\equiv p.
}
$$

---

### Una fila no basta {#apm-t1-c02-e0097}
Un estudiante sabe que, para:

$$
p=\mathrm V,
\qquad
q=\mathrm V,
$$

el bicondicional:

$$
p\leftrightarrow q
$$

es verdadero.

Concluye:

$$
p\equiv q.
$$

Explica el error.

#### Solución


La verdad de:

$$
p\leftrightarrow q
$$

en una sola asignación solo muestra que $p$ y $q$ tienen el mismo valor **en esa fila**.

Para afirmar:

$$
p\equiv q,
$$

sus columnas deben coincidir en todas las asignaciones.

Tomemos:

$$
p=\mathrm V,
\qquad
q=\mathrm F.
$$

Entonces $p$ y $q$ reciben valores distintos.

Por tanto:

$$
p
$$

y:

$$
q
$$

no son lógicamente equivalentes.

---

### Idempotencia descubierta semánticamente {#apm-t1-c02-e0098}
Demuestra mediante una tabla que:

$$
p\lor p
\equiv
p.
$$

#### Solución


| $p$ | $p\lor p$ |
|---|---|
| $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ |

Las columnas coinciden en ambas asignaciones.

Por tanto:

$$
\boxed{
p\lor p\equiv p.
}
$$

Más adelante incorporaremos esta equivalencia a un conjunto sistemático de leyes.

---

### Simetría de la equivalencia {#apm-t1-c02-e0099}
Supón que ya se ha establecido:

$$
P\equiv Q.
$$

Justifica, usando únicamente la definición, por qué también podemos afirmar:

$$
Q\equiv P.
$$

#### Solución


Si:

$$
P\equiv Q,
$$

entonces las columnas de $P$ y $Q$ coinciden fila por fila.

Pero decir que el valor de $P$ coincide con el de $Q$ en cada fila es exactamente lo mismo que decir que el valor de $Q$ coincide con el de $P$ en cada fila.

Por tanto:

$$
\boxed{
Q\equiv P.
}
$$

No hemos utilizado ninguna ley adicional; solo la definición de equivalencia lógica.

---

### Refutar una equivalencia {#apm-t1-c02-e0100}
Alguien propone:

$$
p\lor q
\equiv
p\land q.
$$

Refuta la afirmación con una sola contraasignación.

#### Solución


Tomemos:

$$
p=\mathrm V,
\qquad
q=\mathrm F.
$$

Entonces:

$$
p\lor q=\mathrm V,
$$

mientras que:

$$
p\land q=\mathrm F.
$$

Las fórmulas reciben valores distintos en esta asignación.

Por tanto:

$$
\boxed{
p\lor q
\text{ y }
p\land q
\text{ no son lógicamente equivalentes}.
}
$$

Una sola fila distinta basta para refutar la equivalencia.

---

### Síntesis: una fórmula más simple con la misma columna {#apm-t1-c02-e0101}
Decide si:

$$
(p\land q)\lor(p\land\neg q)
$$

es lógicamente equivalente a:

$$
p.
$$

Construye una tabla conjunta y justifica tu conclusión.

#### Solución


Necesitamos calcular:

$$
p\land q,
$$

$$
\neg q,
$$

$$
p\land\neg q,
$$

y finalmente:

$$
(p\land q)\lor(p\land\neg q).
$$

| $p$ | $q$ | $p\land q$ | $\neg q$ | $p\land\neg q$ | $(p\land q)\lor(p\land\neg q)$ | $p$ |
|---|---|---|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |

Las dos últimas columnas coinciden fila por fila.

Por tanto:

$$
\boxed{
(p\land q)\lor(p\land\neg q)
\equiv
p.
}
$$

Por [la proposición «Criterio bicondicional para la equivalencia lógica»](#apm-t1-c02-p0001), también sabemos que:

$$
\bigl((p\land q)\lor(p\land\neg q)\bigr)
\leftrightarrow
p
$$

es una tautología.

Esta fórmula muestra por primera vez con claridad la utilidad futura del álgebra proposicional: una fórmula relativamente larga puede tener exactamente el mismo comportamiento lógico que otra mucho más simple.

---

## Síntesis

Dos fórmulas: $P$ y $Q$ son lógicamente equivalentes cuando sus columnas coinciden en toda la tabla conjunta.

Escribimos:

$$

P\equiv Q.

$$

Para demostrar una equivalencia mediante tablas debemos considerar todas las asignaciones.

Para refutarla basta una sola contraasignación donde los valores difieran.

La distinción notacional fundamental es:

$$

P\leftrightarrow Q
\neq
P\equiv Q.

$$

El primero es un bicondicional, es decir, una fórmula.

El segundo expresa equivalencia lógica entre fórmulas. La conexión entre ambos quedó establecida por:

> [la proposición «Criterio bicondicional para la equivalencia lógica»](#apm-t1-c02-p0001) — $P$ y $Q$ son lógicamente equivalentes si y solo si $P\leftrightarrow Q$ es una tautología.

Con esta proposición cerramos el bloque puramente semántico del capítulo.

---

## Hacia la sección siguiente

Hasta ahora, para establecer equivalencias hemos utilizado tablas.

Pero ya hemos descubierto ejemplos como: $\neg\neg p\equiv p$ y $p\lor p\equiv p$.

Si acumulamos equivalencias de este tipo, podremos empezar a **transformar fórmulas** sin reconstruir una tabla completa cada vez.

El siguiente paso será reunir las primeras leyes sistemáticas de ese cálculo:

## §8. Primeras leyes del álgebra proposicional

Hasta ahora, para demostrar una equivalencia lógica hemos regresado a la semántica: construimos una tabla, comparamos columnas y concluimos que dos fórmulas son equivalentes.

Ese procedimiento es seguro, pero empieza a resultar costoso.

En [el ejercicio «Doble negación por tabla»](#apm-t1-c02-e0096) vimos:

$$
\neg\neg P\equiv P.
$$

En [el ejercicio «Idempotencia descubierta semánticamente»](#apm-t1-c02-e0098) apareció:

$$
P\lor P\equiv P.
$$

Y en [el ejemplo «Demostrar una equivalencia por tabla»](#apm-t1-c02-x0015) establecimos:

$$
\neg(P\land Q)\equiv\neg P\lor\neg Q.
$$

Estas equivalencias sugieren un cambio de perspectiva. En álgebra elemental no demostramos desde cero cada vez que:

$$
a+b=b+a.
$$

Una vez establecida la conmutatividad, la utilizamos como una ley. Queremos hacer lo mismo con las fórmulas proposicionales.

La trayectoria será:

$$
\boxed{
\text{semántica}
\longrightarrow
\text{equivalencia demostrada}
\longrightarrow
\text{ley reutilizable}
\longrightarrow
\text{cálculo}.
}
$$

Pero el orden importa: **una equivalencia solo podrá usarse como ley después de haber sido justificada**.

---

### 8.1 Dos fórmulas especiales: una siempre verdadera y otra siempre falsa

Necesitaremos abreviar dos tipos de fórmulas que ya conocemos.

Sea $T$ una fórmula tautológica cualquiera, y sea:

$$
C
$$

una fórmula contradictoria cualquiera. Por tanto, bajo toda asignación relevante: $T=\mathrm V$ y $C=\mathrm F$.

Por ejemplo, podemos tomar: $T=P\lor\neg P$ y $C=P\land\neg P$.

::: {.ma-block .ma-observacion}
**Observación**

Las letras $T$ y $C$ no son nuevos valores de verdad. Son abreviaturas para **fórmulas**: $T$ representa una tautología y $C$ una contradicción.

Los valores de verdad del capítulo siguen siendo:

$$
\mathrm V,\qquad\mathrm F.
$$
:::

Esta distinción evita mezclar el nivel de las fórmulas con el nivel de sus valores.

---

### 8.2 Identidad y dominación

Comencemos con una fórmula arbitraria:

$$
P.
$$

Si la conjuntamos con una tautología:

$$
P\land T,
$$

la segunda parte siempre vale $\mathrm V$. El valor de la conjunción queda determinado exactamente por el valor de $P$.

| $P$ | $T$ | $P\land T$ |
|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ |

Así, $P\land T\equiv P$. De manera dual, como una contradicción siempre recibe $\mathrm F$:

$$
P\lor C\equiv P.
$$

Estas son **leyes de identidad**. Ahora observemos $P\lor T$ Como $T$ siempre es verdadera, toda la disyunción es verdadera:

$$
P\lor T\equiv T.
$$

Y, como $C$ siempre es falsa:

$$
P\land C\equiv C.
$$

Estas son **leyes de dominación**. Podemos reunir:

$$
\boxed{
\begin{aligned}
P\land T&\equiv P,\\
P\lor C&\equiv P,\\
P\lor T&\equiv T,\\
P\land C&\equiv C.
\end{aligned}
}
$$

---

### 8.3 Idempotencia

¿Qué ocurre si una fórmula se combina consigo misma?

Para la conjunción:

| $P$ | $P\land P$ |
|---|---|
| $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ |

Por tanto:

$$
P\land P\equiv P.
$$

Para la disyunción:

| $P$ | $P\lor P$ |
|---|---|
| $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ |

Así, $P\lor P\equiv P$. Estas son las **leyes de idempotencia**:

$$
\boxed{
P\land P\equiv P,
\qquad
P\lor P\equiv P.
}
$$

---

### 8.4 Complemento

Sabemos que $P$ y $\neg P$ tienen siempre valores opuestos. Por tanto:

$$
P\lor\neg P
$$

es siempre verdadera, mientras que:

$$
P\land\neg P
$$

es siempre falsa. En nuestra notación:

$$
\boxed{
P\lor\neg P\equiv T,
\qquad
P\land\neg P\equiv C.
}
$$

Estas son las **leyes de complemento**. Obsérvese nuevamente que $T$ y $C$ representan fórmulas tautológicas y contradictorias, no los valores $\mathrm V$ y $\mathrm F$.

---

### 8.5 Doble negación

La negación invierte el valor de una fórmula. Una segunda negación vuelve a invertirlo.

| $P$ | $\neg P$ | $\neg\neg P$ |
|---|---|---|
| $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ |

Por tanto:

$$

\neg\neg P\equiv P.

$$

Esta será nuestra **ley de doble negación**.

---

### 8.6 Conmutatividad

Comparemos $P\land Q$ y $Q\land P$.

| $P$ | $Q$ | $P\land Q$ | $Q\land P$ |
|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |

Las columnas coinciden. Así:

$$
P\land Q\equiv Q\land P.
$$

Lo mismo ocurre con la disyunción:

$$
P\lor Q\equiv Q\lor P.
$$

Tenemos las **leyes conmutativas**:

$$
\boxed{
P\land Q\equiv Q\land P,
\qquad
P\lor Q\equiv Q\lor P.
}
$$

El orden de los dos componentes no cambia el comportamiento lógico de una conjunción ni de una disyunción.

---

### 8.7 Asociatividad

Consideremos tres fórmulas:

$$
P,\qquad Q,\qquad R.
$$

Para la conjunción podemos agrupar: $(P\land Q)\land R$ o $P\land(Q\land R)$. La tabla conjunta es:

| $P$ | $Q$ | $R$ | $(P\land Q)\land R$ | $P\land(Q\land R)$ |
|---|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |

Por tanto:

$$
(P\land Q)\land R
\equiv
P\land(Q\land R).
$$

Para la disyunción obtenemos:

| $P$ | $Q$ | $R$ | $(P\lor Q)\lor R$ | $P\lor(Q\lor R)$ |
|---|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |

Así:

$$
(P\lor Q)\lor R
\equiv
P\lor(Q\lor R).
$$

Estas son las **leyes asociativas**.

---

### 8.8 Primer paquete de leyes

Podemos reunir lo anterior en un solo resultado.

::: {.ma-block .ma-enunciado #apm-t1-c02-p0002}
**Proposición — Primeras leyes del álgebra proposicional**

Para fórmulas proposicionales arbitrarias $P,Q,R$, una tautología $T$ y una contradicción $C$, se cumplen las siguientes equivalencias.

**Identidad**

$$
P\land T\equiv P,
\qquad
P\lor C\equiv P.
$$

**Dominación**

$$
P\lor T\equiv T,
\qquad
P\land C\equiv C.
$$

**Idempotencia**

$$
P\land P\equiv P,
\qquad
P\lor P\equiv P.
$$

**Complemento**

$$
P\lor\neg P\equiv T,
\qquad
P\land\neg P\equiv C.
$$

**Doble negación**

$$
\neg\neg P\equiv P.
$$

**Conmutatividad**

$$
P\land Q\equiv Q\land P,
\qquad
P\lor Q\equiv Q\lor P.
$$

**Asociatividad**

$$
(P\land Q)\land R\equiv P\land(Q\land R),
$$

$$
(P\lor Q)\lor R\equiv P\lor(Q\lor R).
$$
:::

#### Demostración

Las tablas y argumentos semánticos de §§8.2–8.7 muestran, para cada familia, que las fórmulas situadas a ambos lados de $\equiv$ reciben el mismo valor en todas las asignaciones.

Por [la definición «Equivalencia lógica»](#apm-t1-c02-d0021), eso es exactamente afirmar que son lógicamente equivalentes.

Por tanto, todas las equivalencias enunciadas quedan demostradas.

---

### 8.9 Por qué podemos reemplazar una subfórmula por otra equivalente

Para calcular algebraicamente necesitamos hacer explícita una operación que hasta ahora hemos usado solo de manera intuitiva.

Supongamos $A\equiv B$. Entonces, en cada asignación, $A$ y $B$ reciben el mismo valor.

Por tanto:

- $\neg A$ y $\neg B$ también reciben el mismo valor;
- $A\land R$ y $B\land R$ reciben el mismo valor;
- $A\lor R$ y $B\lor R$ reciben el mismo valor.

Lo mismo vale si $A$ y $B$ aparecen a la derecha:

$$
R\land A\equiv R\land B,
$$

$$
R\lor A\equiv R\lor B.
$$

La razón es puramente semántica: si sustituimos una entrada por otra que tiene exactamente el mismo valor en cada fila, la operación exterior recibe las mismas entradas y produce el mismo resultado.

Así podremos utilizar una ley **dentro de una fórmula mayor**.

::: {.ma-block .ma-intuicion}
**Idea clave**

Reemplazar una subfórmula por otra equivalente está permitido porque la equivalencia garantiza igualdad de valores de verdad fila por fila.
:::

No necesitamos todavía una teoría general de sustitución para fórmulas arbitrarias. Estas observaciones locales bastan para las reescrituras con $\neg,\land,\lor$ que realizaremos ahora.

---

### 8.10 De tabla a cálculo

Una vez que una ley está demostrada, ya no necesitamos reconstruir su tabla cada vez.

Por ejemplo, $P\lor P\equiv P$ puede utilizarse directamente como idempotencia. Y:

$$
\neg\neg P\equiv P
$$

puede utilizarse directamente como doble negación. Esto cambia el modo de trabajo.

Antes:

$$
\text{fórmula}
\longrightarrow
\text{tabla completa}
\longrightarrow
\text{equivalencia}.
$$

Ahora empezamos a disponer de:

$$
\text{fórmula}
\longrightarrow
\text{cadena de leyes}
\longrightarrow
\text{forma equivalente}.
$$

Pero cada paso debe citar una ley válida.

---

### 8.11 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-t1-c02-x0016}
**Ejemplo — Simplificar sin reconstruir una tabla completa**
:::

Simplifiquemos:

$$
(P\land P)\lor(Q\land\neg Q).
$$

Comenzamos por la idempotencia:

$$
(P\land P)\lor(Q\land\neg Q)
\equiv
P\lor(Q\land\neg Q).
$$

Por complemento:

$$
Q\land\neg Q\equiv C.
$$

Podemos sustituir esa subfórmula:

$$
P\lor(Q\land\neg Q)
\equiv
P\lor C.
$$

Finalmente, por identidad:

$$
P\lor C
\equiv
P.
$$

Por tanto:

$$

(P\land P)\lor(Q\land\neg Q)
\equiv
P.

$$

La cadena completa puede presentarse de manera compacta:

$$
\begin{aligned}
(P\land P)\lor(Q\land\neg Q)
&\equiv P\lor(Q\land\neg Q)
&&\text{(idempotencia)}\\
&\equiv P\lor C
&&\text{(complemento)}\\
&\equiv P
&&\text{(identidad).}
\end{aligned}
$$

Este es el nuevo tipo de cálculo que iremos desarrollando.

---
## Ejercicios

### Simplificaciones elementales {#apm-t1-c02-e0102}
Simplifica mediante [la proposición «Primeras leyes del álgebra proposicional»](#apm-t1-c02-p0002) y justifica cada paso.

#### a)

$$
\neg\neg(P\lor P)
$$

#### b)

$$
(P\land\neg P)\lor Q
$$

#### Solución


#### a)

Por idempotencia:

$$
P\lor P\equiv P.
$$

Sustituyendo dentro de la doble negación:

$$
\neg\neg(P\lor P)
\equiv
\neg\neg P.
$$

Por doble negación:

$$
\neg\neg P\equiv P.
$$

Por tanto:

$$
\boxed{
\neg\neg(P\lor P)\equiv P.
}
$$

#### b)

Por complemento:

$$
P\land\neg P\equiv C.
$$

Entonces:

$$
(P\land\neg P)\lor Q
\equiv
C\lor Q.
$$

Por conmutatividad:

$$
C\lor Q
\equiv
Q\lor C.
$$

Por identidad:

$$
Q\lor C\equiv Q.
$$

Así:

$$
\boxed{
(P\land\neg P)\lor Q\equiv Q.
}
$$

---

### Reordenar y eliminar repeticiones {#apm-t1-c02-e0103}
Simplifica:

$$
(P\land Q)\land P.
$$

Utiliza únicamente asociatividad, conmutatividad e idempotencia.

#### Solución


Por asociatividad:

$$
(P\land Q)\land P
\equiv
P\land(Q\land P).
$$

Por conmutatividad dentro del paréntesis:

$$
P\land(Q\land P)
\equiv
P\land(P\land Q).
$$

Por asociatividad en sentido inverso:

$$
P\land(P\land Q)
\equiv
(P\land P)\land Q.
$$

Por idempotencia:

$$
(P\land P)\land Q
\equiv
P\land Q.
$$

Por tanto:

$$
\boxed{
(P\land Q)\land P
\equiv
P\land Q.
}
$$

---

### Justificar la conmutatividad {#apm-t1-c02-e0104}
Demuestra mediante una tabla que:

$$
P\lor Q
\equiv
Q\lor P.
$$

Explica después por qué esa tabla autoriza a utilizar la conmutatividad de $\lor$ como ley de reescritura.

#### Solución


| $P$ | $Q$ | $P\lor Q$ | $Q\lor P$ |
|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |

Las dos columnas coinciden en toda la tabla.

Por definición:

$$
P\lor Q\equiv Q\lor P.
$$

Como la equivalencia ya ha sido demostrada para fórmulas arbitrarias $P,Q$, puede reutilizarse como ley sin reconstruir esta tabla en cada aplicación.

---

### Justificar una equivalencia derivada {#apm-t1-c02-e0105}
Demuestra mediante una cadena de leyes que:

$$
\neg\neg(P\land P)
\equiv
P.
$$

Indica la ley usada en cada paso.

#### Solución


Por doble negación:

$$
\neg\neg(P\land P)
\equiv
P\land P.
$$

Por idempotencia:

$$
P\land P
\equiv
P.
$$

Por tanto:

$$
\boxed{
\neg\neg(P\land P)
\equiv
P.
}
$$

Cada paso utiliza una ley ya demostrada en [la proposición «Primeras leyes del álgebra proposicional»](#apm-t1-c02-p0002).

---

### ¿Por qué la identidad vale para cualquier tautología? {#apm-t1-c02-e0106}
Sea $T$ una tautología cualquiera.

Justifica directamente desde las definiciones, sin elegir una fórmula tautológica particular, que:

$$
P\land T\equiv P.
$$

#### Solución


Como $T$ es una tautología, en toda asignación:

$$
T=\mathrm V.
$$

Consideremos cualquier fila.

Si:

$$
P=\mathrm V,
$$

entonces:

$$
P\land T
=
\mathrm V\land\mathrm V
=
\mathrm V,
$$

que coincide con el valor de $P$.

Si:

$$
P=\mathrm F,
$$

entonces:

$$
P\land T
=
\mathrm F\land\mathrm V
=
\mathrm F,
$$

que nuevamente coincide con el valor de $P$.

Por tanto, en cada asignación:

$$
P\land T
$$

y:

$$
P
$$

tienen el mismo valor.

Luego:

$$
\boxed{
P\land T\equiv P.
}
$$

La demostración no depende de qué tautología concreta representa $T$.

---

### Explorar la dualidad de las primeras leyes {#apm-t1-c02-e0107}
Observa las parejas:

$$
P\land T\equiv P,
\qquad
P\lor C\equiv P,
$$

y:

$$
P\lor T\equiv T,
\qquad
P\land C\equiv C.
$$

#### a)

¿Qué ocurre al intercambiar simultáneamente $\land$ con $\lor$ y los papeles de $T$ y $C$?

#### b)

Busca el mismo patrón en las leyes de complemento.

#### c)

Formula con tus palabras la regularidad observada, sin convertirla todavía en una nueva ley formal.

#### Solución


#### a)

La primera ley de identidad:

$$
P\land T\equiv P
$$

se transforma en:

$$
P\lor C\equiv P,
$$

que es la segunda ley de identidad.

Del mismo modo:

$$
P\lor T\equiv T
$$

se transforma en:

$$
P\land C\equiv C.
$$

#### b)

Las leyes:

$$
P\lor\neg P\equiv T
$$

y:

$$
P\land\neg P\equiv C
$$

también se intercambian al permutar $\lor$ con $\land$ y $T$ con $C$.

#### c)

Las primeras leyes aparecen organizadas en parejas: al intercambiar conjunción y disyunción, y simultáneamente tautología y contradicción, varias leyes se transforman unas en otras.

Esta regularidad sugiere una simetría interna del álgebra proposicional. Por ahora la registramos como observación estructural.

---

### Síntesis: una cadena larga {#apm-t1-c02-e0108}
Simplifica:

$$
\neg\neg\Bigl(((P\land Q)\land P)\lor(R\land\neg R)\Bigr)
\land
(S\lor\neg S).
$$

Utiliza únicamente las leyes de [la proposición «Primeras leyes del álgebra proposicional»](#apm-t1-c02-p0002). Justifica cada paso importante.

#### Solución


Comenzamos por la doble negación:

$$
\begin{aligned}
&\neg\neg\Bigl(((P\land Q)\land P)\lor(R\land\neg R)\Bigr)
\land
(S\lor\neg S)
\\
&\equiv
\Bigl(((P\land Q)\land P)\lor(R\land\neg R)\Bigr)
\land
(S\lor\neg S).
\end{aligned}
$$

En [el ejercicio «Reordenar y eliminar repeticiones»](#apm-t1-c02-e0103) vimos, usando asociatividad, conmutatividad e idempotencia, que:

$$
(P\land Q)\land P
\equiv
P\land Q.
$$

Sustituimos:

$$
\equiv
\Bigl((P\land Q)\lor(R\land\neg R)\Bigr)
\land
(S\lor\neg S).
$$

Por complemento:

$$
R\land\neg R\equiv C,
$$

de modo que:

$$
\equiv
\bigl((P\land Q)\lor C\bigr)
\land
(S\lor\neg S).
$$

Por identidad:

$$
(P\land Q)\lor C
\equiv
P\land Q.
$$

Entonces:

$$
\equiv
(P\land Q)\land(S\lor\neg S).
$$

Por complemento:

$$
S\lor\neg S\equiv T.
$$

Así:

$$
\equiv
(P\land Q)\land T.
$$

Finalmente, por identidad:

$$
(P\land Q)\land T
\equiv
P\land Q.
$$

Por tanto:

$$
\boxed{
\neg\neg\Bigl(((P\land Q)\land P)\lor(R\land\neg R)\Bigr)
\land
(S\lor\neg S)
\equiv
P\land Q.
}
$$

---

## Síntesis

En esta sección hemos dado el paso decisivo desde la semántica hacia el cálculo.

Primero establecimos por tablas o argumentos semánticos las leyes de:

- identidad;
- dominación;
- idempotencia;
- complemento;
- doble negación;
- conmutatividad;
- asociatividad.

Todas quedaron reunidas en:

$$
\texttt{[la proposición «Primeras leyes del álgebra proposicional»](#apm-t1-c02-p0002)}.
$$

Después justificamos por qué una subfórmula puede reemplazarse localmente por otra equivalente dentro de:

$$
\neg,\qquad\land,\qquad\lor.
$$

Con ello aparecen verdaderas cadenas de cálculo:

$$
F_0
\equiv
F_1
\equiv
\cdots
\equiv
F_n,
$$

donde cada paso debe indicar la ley que lo autoriza.

La diferencia con una manipulación meramente simbólica es esencial:

$$

\text{no movemos símbolos porque «parece funcionar»;}
\quad
\text{reescribimos mediante equivalencias ya demostradas}.

$$

---

## Hacia la sección siguiente

Nuestro primer paquete de leyes todavía está incompleto. En álgebra elemental, una operación puede distribuirse sobre otra.

En lógica proposicional ocurre algo particularmente interesante: la conjunción y la disyunción presentan una simetría mucho más fuerte de la que encontramos en la aritmética.

Además aparecerán dos herramientas decisivas:

- absorción;
- leyes de De Morgan.

La siguiente sección desarrollará:

## §9. Distributividad, absorción y leyes de De Morgan

En la sección anterior empezamos a calcular con fórmulas.

Ya disponemos de leyes como:

$$
P\land P\equiv P,
$$

$$
P\lor\neg P\equiv T,
$$

$$
\neg\neg P\equiv P,
$$

y podemos reordenar o reagrupar conjunciones y disyunciones.

Pero todavía falta una parte importante del paralelismo con el álgebra.

En aritmética conocemos:

$$
a(b+c)=ab+ac.
$$

La multiplicación se distribuye sobre la suma. En lógica proposicional aparecerá algo parecido, pero con una diferencia estructural notable:

> **la conjunción se distribuye sobre la disyunción y la disyunción se distribuye sobre la conjunción.**

Además, encontraremos dos nuevas familias de leyes:

- **absorción**, que elimina ciertas repeticiones estructurales;
- **De Morgan**, que describe cómo atraviesa una negación a una conjunción o a una disyunción.

Con estas herramientas el álgebra proposicional empieza a adquirir una fisonomía propia.

---

### 9.1 La conjunción distribuye sobre la disyunción

Consideremos $P\land(Q\lor R)$. La fórmula afirma que $P$ es verdadera y que, además, al menos una de $Q,R$ es verdadera.

Comparemos con:

$$
(P\land Q)\lor(P\land R).
$$

Esta segunda fórmula afirma que se cumple al menos una de las dos posibilidades:

- $P$ y $Q$ son verdaderas;
- $P$ y $R$ son verdaderas.

Ambas descripciones tienen el mismo comportamiento lógico. Podemos verlo sin una tabla de ocho filas completa.

#### Si $P=\mathrm F$

Entonces $P\land(Q\lor R)=\mathrm F$ También:

$$
P\land Q=\mathrm F,
\qquad
P\land R=\mathrm F,
$$

y por tanto:

$$
(P\land Q)\lor(P\land R)=\mathrm F.
$$

#### Si $P=\mathrm V$

Entonces $P\land(Q\lor R)$ recibe exactamente el valor de:

$$
Q\lor R.
$$

Por otra parte:

$$
P\land Q
$$

recibe el valor de $Q$, y:

$$
P\land R
$$

recibe el valor de $R$. Así, $(P\land Q)\lor(P\land R)$ también recibe exactamente el valor de:

$$
Q\lor R.
$$

En todos los casos:

$$
\boxed{
P\land(Q\lor R)
\equiv
(P\land Q)\lor(P\land R).
}
$$

---

### 9.2 La disyunción también distribuye sobre la conjunción

Ahora comparemos $P\lor(Q\land R)$ con $(P\lor Q)\land(P\lor R)$.

#### Si $P=\mathrm V$

La primera fórmula es verdadera porque contiene una disyunción con $P=\mathrm V$.

En la segunda: $P\lor Q=\mathrm V$ y $P\lor R=\mathrm V$. Por tanto, su conjunción también es verdadera.

#### Si $P=\mathrm F$

La primera fórmula recibe exactamente el valor de:

$$
Q\land R.
$$

En la segunda:

$$
P\lor Q
$$

recibe el valor de $Q$, mientras que:

$$
P\lor R
$$

recibe el valor de $R$. Por tanto:

$$
(P\lor Q)\land(P\lor R)
$$

recibe también el valor de:

$$
Q\land R.
$$

Así:

$$
\boxed{
P\lor(Q\land R)
\equiv
(P\lor Q)\land(P\lor R).
}
$$

::: {.ma-block .ma-intuicion}
**Idea clave**

En el álgebra proposicional las dos operaciones principales presentan una distributividad mutua:

$$
\land\text{ distribuye sobre }\lor,
$$

y:

$$
\lor\text{ distribuye sobre }\land.
$$
:::

Esta simetría será muy útil para transformar fórmulas.

---

### 9.3 Absorción

Consideremos $P\lor(P\land Q)$ Puede parecer que la segunda parte aporta información adicional.

Pero si $P$ es verdadera, toda la disyunción ya es verdadera.

Y si $P$ es falsa, entonces $P\land Q$ también es falsa.

La fórmula completa tiene siempre el mismo valor que $P$:

$$
P\lor(P\land Q)\equiv P.
$$

De manera dual:

$$
P\land(P\lor Q)\equiv P.
$$

Estas son las **leyes de absorción**. La palabra es apropiada: una aparición de $P$ absorbe una expresión mayor que ya contiene a $P$ de la forma adecuada.

---

### 9.4 Distributividad y absorción

Reunimos estas leyes.

::: {.ma-block .ma-enunciado #apm-t1-c02-p0003}
**Proposición — Distributividad y absorción**

Para fórmulas proposicionales arbitrarias $P,Q,R$:

**Distributividad**

$$
P\land(Q\lor R)
\equiv
(P\land Q)\lor(P\land R),
$$

$$
P\lor(Q\land R)
\equiv
(P\lor Q)\land(P\lor R).
$$

**Absorción**

$$
P\lor(P\land Q)\equiv P,
$$

$$
P\land(P\lor Q)\equiv P.
$$
:::

#### Demostración

Las dos leyes distributivas quedaron justificadas semánticamente en §§9.1–9.2 considerando los dos valores posibles de $P$.

Para la primera ley de absorción, fijemos una asignación.

- Si $P=\mathrm V$, entonces:
  $$
  P\lor(P\land Q)=\mathrm V,
  $$
  que coincide con $P$.
- Si $P=\mathrm F$, entonces:
  $$
  P\land Q=\mathrm F,
  $$
  y por tanto:
  $$
  P\lor(P\land Q)=\mathrm F,
  $$
  que nuevamente coincide con $P$.

Así, $P\lor(P\land Q)\equiv P$. La segunda absorción se verifica de manera dual:

- si $P=\mathrm F$, toda la conjunción es falsa;
- si $P=\mathrm V$, entonces $P\lor Q$ es verdadera y toda la conjunción es verdadera.

Por tanto:

$$
P\land(P\lor Q)\equiv P.
$$

Quedan demostradas las cuatro equivalencias.

---

### 9.5 Negar una conjunción

Consideremos $\neg(P\land Q)$. La fórmula es verdadera cuando:

$$
P\land Q
$$

es falsa.

Pero una conjunción es falsa precisamente cuando al menos uno de sus componentes es falso.

Eso sugiere:

$$
\neg P\lor\neg Q.
$$

Construimos la tabla:

| $P$ | $Q$ | $P\land Q$ | $\neg(P\land Q)$ | $\neg P$ | $\neg Q$ | $\neg P\lor\neg Q$ |
|---|---|---|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |

Las columnas coinciden:

$$
\boxed{
\neg(P\land Q)
\equiv
\neg P\lor\neg Q.
}
$$

Esta equivalencia ya había aparecido semánticamente en §7. Ahora queda incorporada formalmente al repertorio de leyes de cálculo.

---

### 9.6 Negar una disyunción

Ahora consideremos $\neg(P\lor Q)$ Para que una disyunción sea falsa, ambos componentes deben ser falsos.

Por tanto, su negación será verdadera exactamente cuando: $\neg P$ y $\neg Q$ sean ambas verdaderas.

La tabla lo confirma:

| $P$ | $Q$ | $P\lor Q$ | $\neg(P\lor Q)$ | $\neg P$ | $\neg Q$ | $\neg P\land\neg Q$ |
|---|---|---|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |

Así:

$$
\boxed{
\neg(P\lor Q)
\equiv
\neg P\land\neg Q.
}
$$

---

### 9.7 Las leyes de De Morgan

::: {.ma-block .ma-enunciado #apm-t1-c02-p0004}
**Proposición — Leyes de De Morgan**

Para fórmulas proposicionales arbitrarias $P,Q$:

$$
\neg(P\land Q)
\equiv
\neg P\lor\neg Q,
$$

y:

$$
\neg(P\lor Q)
\equiv
\neg P\land\neg Q.
$$
:::

#### Demostración

Las tablas de §§9.5–9.6 muestran que, en cada caso, las columnas situadas a ambos lados de $\equiv$ coinciden fila por fila.

Por la definición de equivalencia lógica, ambas equivalencias quedan demostradas.

---

### 9.8 Qué hace De Morgan

Las leyes de De Morgan no dicen simplemente que «la negación entra al paréntesis».

Al atravesar el conectivo, la negación **intercambia**: $\land$ con $\lor$.

Así, $\neg(P\land Q)$ no se transforma en:

$$
\neg P\land\neg Q,
$$

sino en: $\neg P\lor\neg Q$ Y $\neg(P\lor Q)$ no se transforma en:

$$
\neg P\lor\neg Q,
$$

sino en:

$$
\neg P\land\neg Q.
$$

La regla estructural es:

$$

\text{negar cada componente}
\quad+\quad
\text{intercambiar }\land\text{ y }\lor.

$$

Esta formulación será útil, pero nunca sustituye la justificación matemática: la regla es válida porque [la proposición «Leyes de De Morgan»](#apm-t1-c02-p0004) ya está demostrado.

---

### 9.9 Una simetría que empieza a hacerse visible

Comparemos algunas parejas:

$$
P\land T\equiv P,
\qquad
P\lor C\equiv P,
$$

$$
P\land(P\lor Q)\equiv P,
\qquad
P\lor(P\land Q)\equiv P,
$$

y:

$$
\neg(P\land Q)\equiv\neg P\lor\neg Q,
$$

$$
\neg(P\lor Q)\equiv\neg P\land\neg Q.
$$

El intercambio:

$$
\land
\longleftrightarrow
\lor
$$

aparece repetidamente acompañado por el intercambio entre comportamiento tautológico y contradictorio.

No convertiremos todavía esta observación en un principio abstracto.

Por ahora basta registrar que el álgebra proposicional tiene una **dualidad visible** entre conjunción y disyunción.

---

### 9.10 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-t1-c02-x0017}
**Ejemplo — De Morgan y absorción en una misma cadena**
:::

Simplifiquemos:

$$
\neg\bigl(P\land(P\lor Q)\bigr).
$$

Podríamos usar absorción inmediatamente dentro de la negación:

$$
P\land(P\lor Q)\equiv P.
$$

Pero queremos mostrar cómo interactúan las leyes nuevas. Primero aplicamos De Morgan:

$$
\neg\bigl(P\land(P\lor Q)\bigr)
\equiv
\neg P\lor\neg(P\lor Q).
$$

Aplicamos nuevamente De Morgan a la segunda negación:

$$
\neg(P\lor Q)
\equiv
\neg P\land\neg Q.
$$

Sustituyendo:

$$
\neg P\lor\neg(P\lor Q)
\equiv
\neg P\lor(\neg P\land\neg Q).
$$

Ahora aparece exactamente la forma de absorción:

$$
A\lor(A\land B)\equiv A,
$$

con:

$$
A=\neg P,
\qquad
B=\neg Q.
$$

Por tanto:

$$
\neg P\lor(\neg P\land\neg Q)
\equiv
\neg P.
$$

La cadena completa es:

$$
\begin{aligned}
\neg\bigl(P\land(P\lor Q)\bigr)
&\equiv
\neg P\lor\neg(P\lor Q)
&&\text{(De Morgan)}\\
&\equiv
\neg P\lor(\neg P\land\neg Q)
&&\text{(De Morgan)}\\
&\equiv
\neg P
&&\text{(absorción).}
\end{aligned}
$$

Así:

$$

\neg\bigl(P\land(P\lor Q)\bigr)
\equiv
\neg P.

$$

Este ejemplo muestra algo importante: una transformación puede ser correcta por rutas diferentes. Lo decisivo es que cada paso esté autorizado por una equivalencia previamente demostrada.

---
## Ejercicios

### Distribuir y simplificar {#apm-t1-c02-e0109}
Simplifica:

$$
P\land(Q\lor P).
$$

Utiliza distributividad y las leyes de [la proposición «Primeras leyes del álgebra proposicional»](#apm-t1-c02-p0002).

#### Solución


Por distributividad:

$$
P\land(Q\lor P)
\equiv
(P\land Q)\lor(P\land P).
$$

Por idempotencia:

$$
P\land P\equiv P.
$$

Entonces:

$$
(P\land Q)\lor(P\land P)
\equiv
(P\land Q)\lor P.
$$

Por conmutatividad:

$$
(P\land Q)\lor P
\equiv
P\lor(P\land Q).
$$

Por absorción:

$$
P\lor(P\land Q)\equiv P.
$$

Por tanto:

$$
\boxed{
P\land(Q\lor P)
\equiv
P.
}
$$

La simplificación coincide, naturalmente, con la ley de absorción en su forma conmutada.

---

### Justificar la segunda distributividad {#apm-t1-c02-e0110}
Demuestra mediante una tabla de verdad que:

$$
P\lor(Q\land R)
\equiv
(P\lor Q)\land(P\lor R).
$$

#### Solución


| $P$ | $Q$ | $R$ | $Q\land R$ | $P\lor(Q\land R)$ | $P\lor Q$ | $P\lor R$ | $(P\lor Q)\land(P\lor R)$ |
|---|---|---|---|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |

Las dos columnas finales que estamos comparando coinciden en las ocho filas.

Por tanto:

$$
\boxed{
P\lor(Q\land R)
\equiv
(P\lor Q)\land(P\lor R).
}
$$

---

### Justificar absorción {#apm-t1-c02-e0111}
Demuestra directamente desde los valores de verdad, sin usar la ley de absorción como premisa, que:

$$
P\land(P\lor Q)\equiv P.
$$

#### Solución


Consideremos los dos valores posibles de $P$.

#### Si $P=\mathrm F$

Entonces:

$$
P\land(P\lor Q)=\mathrm F,
$$

independientemente del valor de $Q$.

Ese valor coincide con $P$.

#### Si $P=\mathrm V$

Entonces:

$$
P\lor Q=\mathrm V.
$$

Por tanto:

$$
P\land(P\lor Q)
=
\mathrm V\land\mathrm V
=
\mathrm V,
$$

que nuevamente coincide con $P$.

Así, en toda asignación:

$$
P\land(P\lor Q)
$$

y:

$$
P
$$

reciben el mismo valor.

Por definición:

$$
\boxed{
P\land(P\lor Q)\equiv P.
}
$$

---

### Demostrar la segunda ley de De Morgan {#apm-t1-c02-e0112}
Construye una tabla para demostrar:

$$
\neg(P\lor Q)
\equiv
\neg P\land\neg Q.
$$

#### Solución


| $P$ | $Q$ | $P\lor Q$ | $\neg(P\lor Q)$ | $\neg P$ | $\neg Q$ | $\neg P\land\neg Q$ |
|---|---|---|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |

Las columnas:

$$
\neg(P\lor Q)
$$

y:

$$
\neg P\land\neg Q
$$

coinciden fila por fila.

Luego:

$$
\boxed{
\neg(P\lor Q)
\equiv
\neg P\land\neg Q.
}
$$

---

### Explorar la dualidad {#apm-t1-c02-e0113}
Considera las cuatro leyes:

$$
P\land(Q\lor R)
\equiv
(P\land Q)\lor(P\land R),
$$

$$
P\lor(Q\land R)
\equiv
(P\lor Q)\land(P\lor R),
$$

$$
\neg(P\land Q)
\equiv
\neg P\lor\neg Q,
$$

$$
\neg(P\lor Q)
\equiv
\neg P\land\neg Q.
$$

#### a)

Empareja cada ley con la que se obtiene al intercambiar:

$$
\land
$$

y:

$$
\lor.
$$

#### b)

¿Qué regularidad observas?

#### c)

¿Por qué esta observación no basta, por sí sola, para afirmar que cualquier fórmula obtenida intercambiando $\land$ y $\lor$ será equivalente a la original?

#### Solución


#### a)

Las dos leyes distributivas forman una pareja.

Las dos leyes de De Morgan forman otra.

#### b)

Las leyes aparecen en versiones duales: al intercambiar conjunción y disyunción obtenemos otra ley válida del mismo repertorio.

#### c)

La dualidad observada es una regularidad entre **leyes específicas ya demostradas**.

No hemos establecido un teorema general que permita intercambiar $\land$ y $\lor$ arbitrariamente dentro de cualquier fórmula conservando su valor.

De hecho, por ejemplo:

$$
P\land Q
$$

y:

$$
P\lor Q
$$

no son lógicamente equivalentes en general.

La observación estructural no autoriza reescrituras que no estén respaldadas por una ley demostrada.

---

### Una falsa ley de De Morgan {#apm-t1-c02-e0114}
Alguien propone:

$$
\neg(P\land Q)
\equiv
\neg P\land\neg Q.
$$

Refuta la pretendida equivalencia con una sola contraasignación.

#### Solución


Tomemos:

$$
P=\mathrm V,
\qquad
Q=\mathrm F.
$$

Entonces:

$$
P\land Q
=
\mathrm V\land\mathrm F
=
\mathrm F.
$$

Por tanto:

$$
\neg(P\land Q)=\mathrm V.
$$

En cambio:

$$
\neg P=\mathrm F,
\qquad
\neg Q=\mathrm V,
$$

de modo que:

$$
\neg P\land\neg Q
=
\mathrm F\land\mathrm V
=
\mathrm F.
$$

Las dos fórmulas reciben valores distintos.

Por tanto, no son lógicamente equivalentes.

La contraasignación muestra exactamente qué error contiene la falsa regla: al atravesar una conjunción, la negación debe cambiar $\land$ por $\lor$.

---

### Síntesis: dos caminos hacia la misma simplificación {#apm-t1-c02-e0115}
Simplifica:

$$
\neg\bigl((P\lor Q)\land(P\lor\neg Q)\bigr)
$$

hasta una fórmula que dependa solo de $P$.

Realiza **dos derivaciones**:

1. una que simplifique primero el interior mediante distributividad;
2. otra que comience aplicando De Morgan a la negación exterior.

#### Solución


### Primer camino — Distributividad en el interior

Usamos la distributividad de $\lor$ sobre $\land$ en sentido inverso:

$$
(P\lor Q)\land(P\lor\neg Q)
\equiv
P\lor(Q\land\neg Q).
$$

Por complemento:

$$
Q\land\neg Q\equiv C.
$$

Entonces:

$$
P\lor(Q\land\neg Q)
\equiv
P\lor C.
$$

Por identidad:

$$
P\lor C\equiv P.
$$

Sustituyendo dentro de la negación:

$$
\neg\bigl((P\lor Q)\land(P\lor\neg Q)\bigr)
\equiv
\neg P.
$$

Por tanto:

$$
\boxed{
\neg\bigl((P\lor Q)\land(P\lor\neg Q)\bigr)
\equiv
\neg P.
}
$$

### Segundo camino — De Morgan primero

Aplicamos De Morgan a la negación exterior:

$$
\begin{aligned}
&\neg\bigl((P\lor Q)\land(P\lor\neg Q)\bigr)\\
&\equiv
\neg(P\lor Q)\lor\neg(P\lor\neg Q).
\end{aligned}
$$

Aplicamos De Morgan a cada término:

$$
\equiv
(\neg P\land\neg Q)
\lor
(\neg P\land\neg\neg Q).
$$

Por doble negación:

$$
\equiv
(\neg P\land\neg Q)
\lor
(\neg P\land Q).
$$

Aplicamos distributividad en sentido inverso:

$$
\equiv
\neg P\land(\neg Q\lor Q).
$$

Por complemento:

$$
\neg Q\lor Q\equiv T.
$$

Entonces:

$$
\equiv
\neg P\land T.
$$

Por identidad:

$$
\equiv
\neg P.
$$

Llegamos nuevamente a:

$$
\boxed{
\neg\bigl((P\lor Q)\land(P\lor\neg Q)\bigr)
\equiv
\neg P.
}
$$

Las dos rutas son válidas porque cada paso está justificado por una equivalencia ya demostrada.

---

## Síntesis

El repertorio de cálculo proposicional se amplía ahora con:

> [la proposición «Distributividad y absorción»](#apm-t1-c02-p0003) — distributividad y absorción;

y:

> [la proposición «Leyes de De Morgan»](#apm-t1-c02-p0004) — leyes de De Morgan.

Las distributividades son:

$$
P\land(Q\lor R)
\equiv
(P\land Q)\lor(P\land R),
$$

$$
P\lor(Q\land R)
\equiv
(P\lor Q)\land(P\lor R).
$$

Las absorciones son:

$$
P\lor(P\land Q)\equiv P,
$$

$$
P\land(P\lor Q)\equiv P.
$$

Y De Morgan establece:

$$
\neg(P\land Q)
\equiv
\neg P\lor\neg Q,
$$

$$
\neg(P\lor Q)
\equiv
\neg P\land\neg Q.
$$

El principio operativo es:

$$

\text{cada reescritura debe corresponder a una equivalencia ya establecida}.

$$

Con [la proposición «Primeras leyes del álgebra proposicional»](#apm-t1-c02-p0002), [la proposición «Distributividad y absorción»](#apm-t1-c02-p0003) y [la proposición «Leyes de De Morgan»](#apm-t1-c02-p0004) disponemos ya de un verdadero núcleo de álgebra proposicional.

---

## Hacia la sección siguiente

Todavía quedan dos conectivos que no hemos incorporado plenamente al cálculo: $\Rightarrow$ y $\leftrightarrow$.

Hasta ahora sabemos evaluarlos mediante sus tablas, pero nuestras leyes de transformación trabajan sobre todo con:

$$
\neg,\qquad
\land,\qquad
\lor.
$$

La siguiente sección mostrará cómo eliminar implicaciones y bicondicionales y cómo transformar fórmulas largas de manera sistemática:

## §10. Eliminar implicaciones y transformar fórmulas largas

Hasta ahora nuestro cálculo algebraico trabaja principalmente con:

$$
\neg,\qquad \land,\qquad \lor.
$$

Ya disponemos de leyes para doble negación, identidad, dominación, idempotencia, complemento, conmutatividad, asociatividad, distributividad, absorción y De Morgan. Pero todavía hay dos conectivos que evaluamos semánticamente y que aún no hemos incorporado plenamente al cálculo:

$$
\Rightarrow
\qquad\text{y}\qquad
\leftrightarrow.
$$

El objetivo de esta sección es mostrar que podemos **eliminarlos mediante equivalencias lógicas**.

La idea general será:

$$
\boxed{
\text{eliminar }\Rightarrow,\leftrightarrow
\longrightarrow
\text{trabajar con }\neg,\land,\lor
\longrightarrow
\text{aplicar las leyes ya demostradas}.
}
$$

Esto nos permitirá transformar fórmulas largas mediante cadenas justificadas, en lugar de construir una tabla completa cada vez.

### 10.1 La implicación como disyunción

Recordemos la tabla de:

$$
P\Rightarrow Q.
$$

| $P$ | $Q$ | $P\Rightarrow Q$ |
|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ |

Ahora comparemos con:

$$
\neg P\lor Q.
$$

| $P$ | $Q$ | $\neg P$ | $\neg P\lor Q$ |
|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |

Las columnas coinciden. Por tanto:

$$
P\Rightarrow Q\equiv\neg P\lor Q.
$$

Esta equivalencia traduce la idea ya conocida: una implicación falla únicamente cuando el antecedente es verdadero y el consecuente es falso.

### 10.2 Contraposición

Consideremos $\neg Q\Rightarrow\neg P$. Aplicando la equivalencia recién demostrada:

$$
\neg Q\Rightarrow\neg P
\equiv
\neg\neg Q\lor\neg P.
$$

Por doble negación:

$$
\equiv Q\lor\neg P.
$$

Por conmutatividad:

$$
\equiv\neg P\lor Q.
$$

Pero:

$$
\neg P\lor Q\equiv P\Rightarrow Q.
$$

Por tanto:

$$
\boxed{P\Rightarrow Q\equiv\neg Q\Rightarrow\neg P.}
$$

La implicación y su contraposición asociada son lógicamente equivalentes. No estamos usando todavía la contraposición como método general de demostración: estamos estableciendo una equivalencia entre fórmulas.

### 10.3 Negar una implicación

Consideremos $\neg(P\Rightarrow Q)$. Eliminamos la implicación:

$$
\neg(P\Rightarrow Q)
\equiv
\neg(\neg P\lor Q).
$$

Por De Morgan:

$$
\equiv
\neg\neg P\land\neg Q.
$$

Por doble negación:

$$
\boxed{\neg(P\Rightarrow Q)\equiv P\land\neg Q.}
$$

La fórmula resultante expresa exactamente el único caso que hace falsa una implicación.

### 10.4 Equivalencias fundamentales de la implicación

::: {.ma-block .ma-enunciado #apm-t1-c02-p0005}
**Proposición — Equivalencias fundamentales de la implicación**

Para fórmulas proposicionales arbitrarias $P,Q$:

$$
P\Rightarrow Q\equiv\neg P\lor Q,
$$

$$
P\Rightarrow Q\equiv\neg Q\Rightarrow\neg P,
$$

y:

$$
\neg(P\Rightarrow Q)\equiv P\land\neg Q.
$$
:::

#### Demostración

La primera equivalencia se estableció por tabla en §10.1. La segunda se derivó en §10.2 a partir de eliminación de implicación, doble negación y conmutatividad. La tercera se derivó en §10.3 mediante eliminación de implicación, De Morgan y doble negación. Quedan demostradas las tres equivalencias.

### 10.5 El bicondicional como dos implicaciones

Desde §4 sabemos que «$P$ si y solo si $Q$» exige dos direcciones: $P\Rightarrow Q$ y $Q\Rightarrow P$.

Ahora podemos demostrar formalmente:

$$
P\leftrightarrow Q
\equiv
(P\Rightarrow Q)\land(Q\Rightarrow P).
$$

| $P$ | $Q$ | $P\leftrightarrow Q$ | $P\Rightarrow Q$ | $Q\Rightarrow P$ | $(P\Rightarrow Q)\land(Q\Rightarrow P)$ |
|---|---|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |

Las columnas coinciden. Así:

$$
\boxed{P\leftrightarrow Q\equiv(P\Rightarrow Q)\land(Q\Rightarrow P).}
$$

### 10.6 El bicondicional sin implicaciones

Podemos continuar eliminando las dos implicaciones:

$$
(P\Rightarrow Q)\land(Q\Rightarrow P)
\equiv
(\neg P\lor Q)\land(\neg Q\lor P).
$$

Esta forma ya utiliza únicamente:

$$
\neg,\qquad\land,\qquad\lor.
$$

Existe además una forma particularmente clara. El bicondicional es verdadero cuando $P$ y $Q$ son ambas verdaderas o ambas falsas. Esto sugiere:

$$
(P\land Q)\lor(\neg P\land\neg Q).
$$

La tabla conjunta confirma:

| $P$ | $Q$ | $P\leftrightarrow Q$ | $P\land Q$ | $\neg P\land\neg Q$ | $(P\land Q)\lor(\neg P\land\neg Q)$ |
|---|---|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |

Por tanto:

$$
\boxed{P\leftrightarrow Q\equiv(P\land Q)\lor(\neg P\land\neg Q).}
$$

### 10.7 Negar un bicondicional

Si el bicondicional afirma que $P$ y $Q$ tienen el mismo valor, su negación expresa que tienen valores distintos. Los dos casos posibles son: $P\land\neg Q$ y $\neg P\land Q$.

La tabla verifica:

| $P$ | $Q$ | $P\leftrightarrow Q$ | $\neg(P\leftrightarrow Q)$ | $P\land\neg Q$ | $\neg P\land Q$ | $(P\land\neg Q)\lor(\neg P\land Q)$ |
|---|---|---|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |

Así:

$$
\boxed{\neg(P\leftrightarrow Q)\equiv(P\land\neg Q)\lor(\neg P\land Q).}
$$

### 10.8 Equivalencias fundamentales del bicondicional

::: {.ma-block .ma-enunciado #apm-t1-c02-p0006}
**Proposición — Equivalencias fundamentales del bicondicional**

Para fórmulas proposicionales arbitrarias $P,Q$:

$$
P\leftrightarrow Q\equiv(P\Rightarrow Q)\land(Q\Rightarrow P),
$$

$$
P\leftrightarrow Q\equiv(P\land Q)\lor(\neg P\land\neg Q),
$$

y:

$$
\neg(P\leftrightarrow Q)\equiv(P\land\neg Q)\lor(\neg P\land Q).
$$
:::

#### Demostración

Las tres equivalencias fueron verificadas semánticamente en §§10.5–10.7 mediante tablas completas. Por la definición de equivalencia lógica, quedan demostradas.

### 10.9 Un protocolo para fórmulas largas

Ante una fórmula que contiene varios conectivos, seguiremos como guía:

1. **Identificar la estructura:** conectivo principal y subfórmulas.
2. **Eliminar bicondicionales:** usar una forma de [la proposición «Equivalencias fundamentales del bicondicional»](#apm-t1-c02-p0006) adecuada al objetivo.
3. **Eliminar implicaciones:** usar $P\Rightarrow Q\equiv\neg P\lor Q$.
4. **Empujar negaciones hacia dentro:** De Morgan, doble negación o las negaciones ya demostradas.
5. **Simplificar:** usar [la proposición «Primeras leyes del álgebra proposicional»](#apm-t1-c02-p0002)–P0004.
6. **Revisar cada paso:** toda transición de una cadena debe estar autorizada.

::: {.ma-block .ma-intuicion}
**Idea clave**

No existe obligación de seguir siempre el mismo camino. Distintas rutas pueden conducir a fórmulas equivalentes. La elección debe favorecer claridad, economía y control de errores.
:::

### 10.10 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-t1-c02-x0018}
**Ejemplo — Una transformación larga con justificación línea por línea**
:::

Demostremos:

$$
\neg[(p\Rightarrow q)\land(r\lor\neg q)]
\equiv
(p\land\neg q)\lor(\neg r\land q).
$$

Partimos de:

$$
\neg[(p\Rightarrow q)\land(r\lor\neg q)].
$$

Aplicamos De Morgan a la conjunción exterior:

$$
\equiv
\neg(p\Rightarrow q)\lor\neg(r\lor\neg q).
$$

Por [la proposición «Equivalencias fundamentales de la implicación»](#apm-t1-c02-p0005):

$$
\neg(p\Rightarrow q)\equiv p\land\neg q.
$$

Y, por De Morgan:

$$
\neg(r\lor\neg q)
\equiv
\neg r\land\neg\neg q.
$$

Sustituyendo:

$$
\equiv
(p\land\neg q)\lor(\neg r\land\neg\neg q).
$$

Por doble negación:

$$
\equiv
(p\land\neg q)\lor(\neg r\land q).
$$

Por tanto:

$$

\neg[(p\Rightarrow q)\land(r\lor\neg q)]
\equiv
(p\land\neg q)\lor(\neg r\land q).

$$

En forma compacta:

$$
\begin{aligned}
\neg[(p\Rightarrow q)\land(r\lor\neg q)]
&\equiv \neg(p\Rightarrow q)\lor\neg(r\lor\neg q)
&&\text{(De Morgan)}\\
&\equiv (p\land\neg q)\lor(\neg r\land\neg\neg q)
&&\text{(P0005 y De Morgan)}\\
&\equiv (p\land\neg q)\lor(\neg r\land q)
&&\text{(doble negación).}
\end{aligned}
$$

La fórmula final ya no contiene implicaciones.
## Ejercicios

### Eliminar implicaciones {#apm-t1-c02-e0116}
Reescribe utilizando únicamente $\neg,\land,\lor$ y simplifica cuando sea posible.

#### a)

$$
P\Rightarrow Q
$$

#### b)

$$
\neg(P\Rightarrow Q)
$$

#### c)

$$
P\Rightarrow\neg Q
$$

#### Solución


#### a)

Por [la proposición «Equivalencias fundamentales de la implicación»](#apm-t1-c02-p0005):

$$
\boxed{P\Rightarrow Q\equiv\neg P\lor Q.}
$$

#### b)

$$
\boxed{\neg(P\Rightarrow Q)\equiv P\land\neg Q.}
$$

#### c)

$$
P\Rightarrow\neg Q
\equiv
\neg P\lor\neg Q.
$$

Por De Morgan en sentido inverso:

$$
\neg P\lor\neg Q\equiv\neg(P\land Q).
$$

Por tanto:

$$
\boxed{P\Rightarrow\neg Q\equiv\neg P\lor\neg Q\equiv\neg(P\land Q).}
$$

### Contraposición algebraica {#apm-t1-c02-e0117}
Demuestra mediante una cadena de equivalencias, sin construir una tabla nueva, que:

$$
P\Rightarrow Q\equiv\neg Q\Rightarrow\neg P.
$$

#### Solución


Partimos de la contraposición asociada:

$$
\neg Q\Rightarrow\neg P
\equiv
\neg\neg Q\lor\neg P
\equiv
Q\lor\neg P
\equiv
\neg P\lor Q
\equiv
P\Rightarrow Q.
$$

Los pasos usan, respectivamente, eliminación de implicación, doble negación, conmutatividad y `P0005` en sentido inverso.

### Eliminar un bicondicional {#apm-t1-c02-e0118}
Transforma:

$$
P\leftrightarrow Q
$$

en una fórmula que use únicamente $\neg,\land,\lor$, partiendo de las dos implicaciones.

#### Solución


Por [la proposición «Equivalencias fundamentales del bicondicional»](#apm-t1-c02-p0006):

$$
P\leftrightarrow Q
\equiv
(P\Rightarrow Q)\land(Q\Rightarrow P).
$$

Eliminamos ambas implicaciones:

$$
\equiv
(\neg P\lor Q)\land(\neg Q\lor P).
$$

Por tanto:

$$
\boxed{P\leftrightarrow Q\equiv(\neg P\lor Q)\land(\neg Q\lor P).}
$$

### Justificar la negación del bicondicional {#apm-t1-c02-e0119}
Demuestra mediante una tabla completa:

$$
\neg(P\leftrightarrow Q)
\equiv
(P\land\neg Q)\lor(\neg P\land Q).
$$

#### Solución


| $P$ | $Q$ | $P\leftrightarrow Q$ | $\neg(P\leftrightarrow Q)$ | $P\land\neg Q$ | $\neg P\land Q$ | $(P\land\neg Q)\lor(\neg P\land Q)$ |
|---|---|---|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |

Las columnas comparadas coinciden fila por fila. Luego:

$$
\boxed{\neg(P\leftrightarrow Q)\equiv(P\land\neg Q)\lor(\neg P\land Q).}
$$

### Una equivalencia de implicaciones anidadas {#apm-t1-c02-e0120}
Demuestra que:

$$
p\Rightarrow(q\Rightarrow r)
$$

y:

$$
(p\land q)\Rightarrow r
$$

son lógicamente equivalentes. Concluye después que:

$$
(p\Rightarrow(q\Rightarrow r))
\leftrightarrow
((p\land q)\Rightarrow r)
$$

es una tautología.

#### Solución


Comenzamos por:

$$
p\Rightarrow(q\Rightarrow r).
$$

Eliminamos la implicación exterior:

$$
\equiv
\neg p\lor(q\Rightarrow r).
$$

Eliminamos la interior:

$$
\equiv
\neg p\lor(\neg q\lor r).
$$

Por asociatividad:

$$
\equiv
(\neg p\lor\neg q)\lor r.
$$

Por De Morgan en sentido inverso:

$$
\neg p\lor\neg q\equiv\neg(p\land q).
$$

Entonces:

$$
\equiv
\neg(p\land q)\lor r.
$$

Por `P0005` en sentido inverso:

$$
\equiv
(p\land q)\Rightarrow r.
$$

Así:

$$
\boxed{p\Rightarrow(q\Rightarrow r)\equiv(p\land q)\Rightarrow r.}
$$

Por [la proposición «Criterio bicondicional para la equivalencia lógica»](#apm-t1-c02-p0001), el bicondicional entre dos fórmulas equivalentes es una tautología. Luego:

$$
\boxed{(p\Rightarrow(q\Rightarrow r))\leftrightarrow((p\land q)\Rightarrow r)}
$$

es una tautología.

### Refutar una transformación incorrecta {#apm-t1-c02-e0121}
Alguien propone:

$$
P\Rightarrow Q\equiv P\lor Q.
$$

Refuta la equivalencia con una sola contraasignación y explica cuál es la forma correcta.

#### Solución


Tomemos:

$$
P=\mathrm V,
\qquad
Q=\mathrm F.
$$

Entonces:

$$
P\Rightarrow Q=\mathrm F,
$$

mientras que:

$$
P\lor Q=\mathrm V.
$$

Por tanto, las fórmulas no son equivalentes. La forma correcta es:

$$
\boxed{P\Rightarrow Q\equiv\neg P\lor Q.}
$$

### Síntesis con bicondicional y negación {#apm-t1-c02-e0122}
Simplifica:

$$
\neg(P\leftrightarrow Q)\lor(P\land Q)
$$

hasta una fórmula equivalente construida como disyunción de conjunciones de literales.

#### Solución


Por [la proposición «Equivalencias fundamentales del bicondicional»](#apm-t1-c02-p0006):

$$
\neg(P\leftrightarrow Q)
\equiv
(P\land\neg Q)\lor(\neg P\land Q).
$$

Sustituimos:

$$
\neg(P\leftrightarrow Q)\lor(P\land Q)
$$

$$
\equiv
(P\land\neg Q)\lor(\neg P\land Q)\lor(P\land Q).
$$

Por tanto:

$$
\boxed{(P\land\neg Q)\lor(\neg P\land Q)\lor(P\land Q).}
$$

La fórmula final no contiene $\Rightarrow$ ni $\leftrightarrow$. La clasificación sistemática de esta forma pertenece a la sección siguiente.

### Síntesis larga: elegir una ruta eficiente {#apm-t1-c02-e0123}
Transforma y simplifica:

$$
\neg\bigl[(P\leftrightarrow Q)\land(P\Rightarrow Q)\bigr].
$$

El resultado final no debe contener $\Rightarrow$ ni $\leftrightarrow$.

#### Solución


Aplicamos De Morgan:

$$
\neg\bigl[(P\leftrightarrow Q)\land(P\Rightarrow Q)\bigr]
\equiv
\neg(P\leftrightarrow Q)\lor\neg(P\Rightarrow Q).
$$

Por [la proposición «Equivalencias fundamentales del bicondicional»](#apm-t1-c02-p0006):

$$
\neg(P\leftrightarrow Q)
\equiv
(P\land\neg Q)\lor(\neg P\land Q).
$$

Por [la proposición «Equivalencias fundamentales de la implicación»](#apm-t1-c02-p0005):

$$
\neg(P\Rightarrow Q)
\equiv
P\land\neg Q.
$$

Sustituyendo:

$$
\equiv
\bigl[(P\land\neg Q)\lor(\neg P\land Q)\bigr]
\lor(P\land\neg Q).
$$

Por asociatividad, conmutatividad e idempotencia:

$$
\equiv
(P\land\neg Q)\lor(\neg P\land Q).
$$

Por tanto:

$$
\boxed{
\neg\bigl[(P\leftrightarrow Q)\land(P\Rightarrow Q)\bigr]
\equiv
(P\land\neg Q)\lor(\neg P\land Q).
}
$$

## Síntesis

La implicación queda incorporada al cálculo mediante [la proposición «Equivalencias fundamentales de la implicación»](#apm-t1-c02-p0005):

$$
P\Rightarrow Q\equiv\neg P\lor Q,
$$

$$
P\Rightarrow Q\equiv\neg Q\Rightarrow\neg P,
$$

$$
\neg(P\Rightarrow Q)\equiv P\land\neg Q.
$$

El bicondicional queda incorporado mediante [la proposición «Equivalencias fundamentales del bicondicional»](#apm-t1-c02-p0006):

$$
P\leftrightarrow Q\equiv(P\Rightarrow Q)\land(Q\Rightarrow P),
$$

$$
P\leftrightarrow Q\equiv(P\land Q)\lor(\neg P\land\neg Q),
$$

$$
\neg(P\leftrightarrow Q)\equiv(P\land\neg Q)\lor(\neg P\land Q).
$$

Con ello podemos transformar una fórmula hasta eliminar $\Rightarrow$ y $\leftrightarrow$ y trabajar únicamente con $\neg,\land,\lor$.

El protocolo general queda:

$$

\text{eliminar bicondicionales}
\to
\text{eliminar implicaciones}
\to
\text{empujar negaciones}
\to
\text{simplificar}.

$$

No es una receta rígida: una equivalencia más directa puede ahorrar pasos. Pero toda transformación debe permanecer justificada.

## Hacia la sección siguiente

En varios ejercicios hemos terminado con fórmulas formadas por proposiciones o negaciones de proposiciones, conjunciones y disyunciones. Por ejemplo:

$$
(P\land\neg Q)\lor(\neg P\land Q).
$$

¿Podemos organizar **cualquier fórmula proposicional** en formas sistemáticas de este tipo?

La respuesta será afirmativa. La siguiente sección introducirá:

## §11. Formas normales disyuntiva y conjuntiva

En la sección anterior aprendimos a eliminar:

$$
\Rightarrow
\qquad\text{y}\qquad
\leftrightarrow
$$

y a transformar fórmulas hasta trabajar únicamente con:

$$
\neg,\qquad
\land,\qquad
\lor.
$$

Pero todavía podemos pedir algo más. Consideremos:

$$
(P\land\neg Q)\lor(\neg P\land Q).
$$

Su estructura es especialmente regular:

- primero aparecen proposiciones o negaciones de proposiciones;
- después se forman conjunciones;
- finalmente esas conjunciones se unen mediante disyunciones.

Ahora comparemos:

$$
(\neg P\lor Q)\land(P\lor\neg Q).
$$

Aquí ocurre lo dual:

- aparecen proposiciones o negaciones de proposiciones;
- se forman disyunciones;
- finalmente esas disyunciones se unen mediante conjunciones.

Estas dos arquitecturas reciben nombres específicos. Y, más importante aún, demostraremos que **toda fórmula proposicional del lenguaje que hemos construido puede llevarse a una forma de cada tipo**.

La tabla de verdad dejará así de ser solamente un instrumento de evaluación.

También se convertirá en un procedimiento de **síntesis de fórmulas**.

---

### 11.1 Literales

Las piezas más pequeñas de las formas normales serán muy sencillas.

::: {.ma-block .ma-definicion #apm-t1-c02-d0022}
**Definición — Literal**

Un **literal** es una variable proposicional o la negación de una variable proposicional.
:::

Por ejemplo:

$$
p,
\qquad
\neg p,
\qquad
q,
\qquad
\neg r
$$

son literales.

En cambio:

$$
p\land q,
$$

$$
\neg(p\lor q)
$$

y:

$$
p\Rightarrow q
$$

no son literales. La negación de un literal, en el sentido que necesitaremos, debe estar aplicada directamente a una variable proposicional.

---

### 11.2 Forma normal disyuntiva

Consideremos:

$$
(p\land\neg q)
\lor
(\neg p\land r)
\lor
q.
$$

Cada bloque separado por:

$$
\lor
$$

es una conjunción de uno o más literales. El último bloque:

$$
q
$$

puede considerarse una conjunción de un solo literal.

::: {.ma-block .ma-definicion #apm-t1-c02-d0023}
**Definición — Forma normal disyuntiva**

Una fórmula está en **forma normal disyuntiva**, abreviada **FND**, cuando es una disyunción de una o más conjunciones de uno o más literales.
:::

Por ejemplo, $(p\land q)\lor(\neg p\land r)$ está en FND. También:

$$
p\lor\neg q
$$

está en FND, pues cada término puede consistir en un solo literal.

Y:

$$
p\land q
$$

también puede verse como una FND con un único término conjuntivo.

No exigiremos por ahora que una FND sea mínima, irredundante ni única.

---

### 11.3 Forma normal conjuntiva

Consideremos ahora:

$$
(p\lor\neg q)
\land
(\neg p\lor r)
\land
q.
$$

Cada bloque separado por:

$$
\land
$$

es una disyunción de uno o más literales.

::: {.ma-block .ma-definicion #apm-t1-c02-d0024}
**Definición — Forma normal conjuntiva**

Una fórmula está en **forma normal conjuntiva**, abreviada **FNC**, cuando es una conjunción de una o más disyunciones de uno o más literales.
:::

Así, $(p\lor q)\land(\neg p\lor r)$ está en FNC. También:

$$
p\land\neg q
$$

está en FNC, pues cada cláusula puede consistir en un solo literal.

Y una sola disyunción $p\lor q$ puede considerarse una FNC con una única cláusula.

De nuevo, no exigiremos minimalidad ni unicidad.

---

### 11.4 Una fila verdadera produce una conjunción

Supongamos que una tabla utiliza tres variables:

$$
p,\qquad q,\qquad r.
$$

Consideremos la fila:

$$
p=\mathrm V,
\qquad
q=\mathrm F,
\qquad
r=\mathrm V.
$$

Queremos construir una fórmula que sea verdadera **exactamente en esa fila**.

Elegimos:

- $p$, porque allí $p=\mathrm V$;
- $\neg q$, porque allí $q=\mathrm F$;
- $r$, porque allí $r=\mathrm V$.

Y los conjuntamos:

$$
p\land\neg q\land r.
$$

En la fila elegida:

$$
p=\mathrm V,
\qquad
\neg q=\mathrm V,
\qquad
r=\mathrm V,
$$

de modo que toda la conjunción es verdadera. Ahora cambiemos cualquier valor de la fila.

Si cambia $p$, el literal $p$ se vuelve falso.

Si cambia $q$, el literal $\neg q$ se vuelve falso.

Si cambia $r$, el literal $r$ se vuelve falso.

Por tanto:

$$
\boxed{
p\land\neg q\land r
}
$$

es verdadera exactamente en:

$$
(\mathrm V,\mathrm F,\mathrm V).
$$

Esta es la pieza fundamental de la construcción de una FND desde una tabla.

---

### 11.5 Construir la FND desde las filas verdaderas

Supongamos que una fórmula $F$ de dos variables tiene la tabla:

| $p$ | $q$ | $F$ |
|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm F$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |

Hay dos filas verdaderas.

#### Primera fila verdadera

$$
p=\mathrm V,
\qquad
q=\mathrm F.
$$

Construimos:

$$
p\land\neg q.
$$

#### Segunda fila verdadera

$$
p=\mathrm F,
\qquad
q=\mathrm V.
$$

Construimos:

$$
\neg p\land q.
$$

Ahora unimos ambas conjunciones mediante:

$$
\lor.
$$

Obtenemos:

$$
(p\land\neg q)\lor(\neg p\land q).
$$

Esta fórmula es verdadera exactamente en las mismas filas que $F$.

Por tanto:

$$
\boxed{
F
\equiv
(p\land\neg q)\lor(\neg p\land q).
}
$$

La tabla ha producido directamente una FND.

---

### 11.6 Una fila falsa produce una disyunción

Ahora queremos la construcción dual. Consideremos nuevamente la fila:

$$
p=\mathrm V,
\qquad
q=\mathrm F,
\qquad
r=\mathrm V.
$$

Queremos una fórmula que sea falsa **exactamente en esa fila**.

Para conseguirlo, elegimos literales que sean falsos allí:

- $\neg p$, porque $p=\mathrm V$;
- $q$, porque $q=\mathrm F$;
- $\neg r$, porque $r=\mathrm V$.

Los unimos mediante disyunción:

$$
\neg p\lor q\lor\neg r.
$$

En la fila elegida, los tres literales son falsos.

Por tanto, toda la disyunción es falsa. Si cambia cualquiera de los tres valores, al menos el literal correspondiente se vuelve verdadero.

Así:

$$

\neg p\lor q\lor\neg r

$$

es falsa exactamente en:

$$
(\mathrm V,\mathrm F,\mathrm V).
$$

Esta es la pieza fundamental de la construcción de una FNC.

---

### 11.7 Construir la FNC desde las filas falsas

Volvamos a la tabla:

| $p$ | $q$ | $F$ |
|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm F$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |

Hay dos filas falsas.

#### Primera fila falsa

$$
p=\mathrm V,
\qquad
q=\mathrm V.
$$

Queremos una disyunción falsa exactamente allí. Tomamos:

$$
\neg p\lor\neg q.
$$

#### Segunda fila falsa

$$
p=\mathrm F,
\qquad
q=\mathrm F.
$$

Tomamos:

$$
p\lor q.
$$

Ahora conjuntamos las dos cláusulas:

$$
(\neg p\lor\neg q)\land(p\lor q).
$$

Esta fórmula es falsa exactamente en las dos filas donde $F$ es falsa.

Por tanto:

$$
\boxed{
F
\equiv
(\neg p\lor\neg q)\land(p\lor q).
}
$$

La misma tabla nos ha producido ahora una FNC.

---

### 11.8 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-t1-c02-x0019}
**Ejemplo — De una tabla a FND y FNC**
:::

Construyamos una FND y una FNC para:

$$
p\leftrightarrow q.
$$

Su tabla es:

| $p$ | $q$ | $p\leftrightarrow q$ |
|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ |

#### FND desde las filas verdaderas

La primera fila verdadera es:

$$
(\mathrm V,\mathrm V).
$$

Produce:

$$
p\land q.
$$

La segunda fila verdadera es:

$$
(\mathrm F,\mathrm F).
$$

Produce:

$$
\neg p\land\neg q.
$$

Disyuntamos:

$$

(p\land q)\lor(\neg p\land\neg q).

$$

Así:

$$
p\leftrightarrow q
\equiv
(p\land q)\lor(\neg p\land\neg q).
$$

Esta es precisamente una equivalencia que ya habíamos demostrado en [la proposición «Equivalencias fundamentales del bicondicional»](#apm-t1-c02-p0006).

#### FNC desde las filas falsas

La primera fila falsa es:

$$
(\mathrm V,\mathrm F).
$$

Produce una cláusula falsa exactamente allí:

$$
\neg p\lor q.
$$

La segunda fila falsa es:

$$
(\mathrm F,\mathrm V).
$$

Produce:

$$
p\lor\neg q.
$$

Conjuntamos:

$$
\boxed{
(\neg p\lor q)\land(p\lor\neg q).
}
$$

Por tanto:

$$
p\leftrightarrow q
\equiv
(\neg p\lor q)\land(p\lor\neg q).
$$

La tabla de verdad ha producido dos fórmulas con estructuras diferentes, pero ambas equivalentes al bicondicional.

---

### 11.9 El teorema de existencia

Ya tenemos el mecanismo necesario para demostrar el resultado general.

::: {.ma-block .ma-enunciado #apm-t1-c02-t0001}
**Teorema — Existencia de formas normales proposicionales**

Sea $F$ una fórmula proposicional cuyas variables proposicionales distintas sean:

$$
p_1,\ldots,p_n,
$$

con:

$$
n\ge1.
$$

Entonces existe una fórmula en FND lógicamente equivalente a $F$, y existe una fórmula en FNC lógicamente equivalente a $F$.
:::

#### Lectura

El teorema no afirma que exista una única FND o una única FNC.

Afirma algo más básico y más importante:

> cualquier comportamiento semántico descrito por una tabla finita puede representarse mediante una fórmula organizada en cualquiera de estas dos arquitecturas.

#### Estrategia

Usaremos la tabla completa de $F$. Para la FND:

1. observaremos las filas donde $F=\mathrm V$;
2. construiremos una conjunción que reconozca exactamente cada una de esas filas;
3. disyuntaremos todas esas conjunciones.

Para la FNC:

1. observaremos las filas donde $F=\mathrm F$;
2. construiremos una disyunción que falle exactamente en cada una de esas filas;
3. conjuntaremos todas esas disyunciones.

#### Demostración — construcción de la FND

La tabla de $F$ tiene:

$$
2^n
$$

filas. Consideremos una fila donde:

$$
F=\mathrm V.
$$

Para esa fila formamos una conjunción con exactamente un literal por variable.

Para cada:

$$
p_i,
$$

elegimos:

$$
p_i
$$

si en la fila:

$$
p_i=\mathrm V,
$$

y elegimos:

$$
\neg p_i
$$

si en la fila:

$$
p_i=\mathrm F.
$$

La conjunción obtenida es verdadera exactamente en esa fila.

En efecto, para que toda la conjunción sea verdadera, cada variable debe recibir precisamente el valor que la fila especifica.

Repetimos esta construcción para cada fila donde $F$ sea verdadera.

Si hay al menos una fila verdadera, disyuntamos todas las conjunciones obtenidas.

Llamemos:

$$
D
$$

a esa disyunción. En una fila donde $F=\mathrm V$, aparece en $D$ la conjunción construida específicamente para esa fila; por tanto:

$$
D=\mathrm V.
$$

En una fila donde $F=\mathrm F$, ninguna de las conjunciones correspondientes a filas verdaderas puede ser verdadera, porque cada una exige una asignación distinta.

Por tanto:

$$
D=\mathrm F.
$$

Así, $D$ y $F$ tienen la misma columna. Luego:

$$
F\equiv D.
$$

Y $D$ está en FND.

#### Caso extremo: contradicción

Si $F$ no tiene ninguna fila verdadera, entonces $F$ es una contradicción.

Como:

$$
n\ge1,
$$

podemos usar, por ejemplo:

$$
p_1\land\neg p_1.
$$

Esta fórmula está en FND y es una contradicción.

Es lógicamente equivalente a $F$. Así queda probada la existencia de una FND en todos los casos.

#### Demostración — construcción de la FNC

Ahora consideremos una fila donde:

$$
F=\mathrm F.
$$

Para esa fila formamos una disyunción con exactamente un literal por variable.

Para cada:

$$
p_i,
$$

elegimos:

$$
\neg p_i
$$

si en la fila:

$$
p_i=\mathrm V,
$$

y elegimos:

$$
p_i
$$

si en la fila:

$$
p_i=\mathrm F.
$$

La disyunción obtenida es falsa exactamente en esa fila.

En efecto, allí todos sus literales son falsos. Si cambia cualquiera de los valores de la fila, el literal correspondiente se vuelve verdadero y, por tanto, toda la disyunción se vuelve verdadera.

Repetimos esta construcción para cada fila donde $F$ sea falsa.

Si hay al menos una fila falsa, conjuntamos todas las disyunciones obtenidas.

Llamemos:

$$
N
$$

a esa conjunción. En una fila donde $F=\mathrm F$, la cláusula construida específicamente para esa fila es falsa; por tanto:

$$
N=\mathrm F.
$$

En una fila donde $F=\mathrm V$, ninguna de las cláusulas correspondientes a filas falsas puede ser falsa, porque cada una falla únicamente en su propia fila.

Por tanto:

$$
N=\mathrm V.
$$

Así, $N$ y $F$ tienen la misma columna. Luego:

$$
F\equiv N.
$$

Y $N$ está en FNC.

#### Caso extremo: tautología

Si $F$ no tiene ninguna fila falsa, entonces $F$ es una tautología.

Podemos usar:

$$
p_1\lor\neg p_1.
$$

Esta fórmula está en FNC y es una tautología.

Por tanto, es lógicamente equivalente a $F$. Con ello queda probada también la existencia de una FNC.

Toda fórmula proposicional del lenguaje considerado admite una FND y una FNC lógicamente equivalentes.

$$
\text{Queda demostrado [el teorema «Existencia de formas normales proposicionales»](#apm-t1-c02-t0001).}
$$

---

### 11.10 Qué demuestra realmente el teorema

El resultado tiene una interpretación importante. Una fórmula puede haber sido construida con:

$$
\neg,\qquad
\land,\qquad
\lor,\qquad
\Rightarrow,\qquad
\leftrightarrow,
$$

y puede tener una estructura sintáctica muy compleja.

Sin embargo, su comportamiento semántico completo queda registrado en una tabla finita.

Y esa tabla permite reconstruir una fórmula equivalente usando únicamente:

$$
\neg,\qquad
\land,\qquad
\lor,
$$

con una organización especialmente regular. Así:

$$
\boxed{
\text{tabla de verdad}
\longrightarrow
\text{FND}
}
$$

y:

$$
\boxed{
\text{tabla de verdad}
\longrightarrow
\text{FNC}.
}
$$

La tabla no solo analiza una fórmula. También puede **fabricar otra fórmula con exactamente el mismo comportamiento lógico**.

---

### 11.11 Las formas normales no son únicas

El teorema afirma existencia, no unicidad. Consideremos $p$. Esta fórmula ya está en FND.

Pero también:

$$
(p\land q)\lor(p\land\neg q)
$$

está en FND. Por distributividad:

$$
(p\land q)\lor(p\land\neg q)
\equiv
p\land(q\lor\neg q).
$$

Por complemento:

$$
q\lor\neg q\equiv T.
$$

Por identidad:

$$
p\land T\equiv p.
$$

Por tanto:

$$
(p\land q)\lor(p\land\neg q)
\equiv
p.
$$

Análogamente:

$$
(p\lor q)\land(p\lor\neg q)
\equiv
p
$$

es una FNC equivalente a $p$. Así, una misma fórmula puede admitir muchas FND y muchas FNC.

La construcción por filas del teorema proporciona una forma **sistemática**, no necesariamente la más corta.

---
## Ejercicios

### Reconocer formas normales {#apm-t1-c02-e0124}
Decide si cada fórmula está en FND, en FNC, en ambas o en ninguna.

#### a)

$$
(p\land\neg q)\lor r
$$

#### b)

$$
(p\lor q)\land(\neg p\lor r)
$$

#### c)

$$
p\land q
$$

#### d)

$$
\neg(p\lor q)
$$

#### Solución


#### a)

Es una disyunción de:

$$
p\land\neg q
$$

y:

$$
r.
$$

Ambos son conjunciones de uno o más literales.

Por tanto, está en FND.

No está escrita como conjunción de disyunciones, así que no la clasificamos como FNC en su forma actual.

#### b)

Es una conjunción de dos disyunciones de literales.

Por tanto, está en FNC.

#### c)

$$
p\land q
$$

puede verse como una FND con un único término conjuntivo.

También puede verse como una FNC formada por dos cláusulas de un solo literal:

$$
p
\qquad\text{y}\qquad
q.
$$

Por tanto, está en ambas.

#### d)

La negación está aplicada a una fórmula compuesta:

$$
p\lor q.
$$

Por tanto, en su forma escrita no está ni en FND ni en FNC.

Por De Morgan:

$$
\neg(p\lor q)
\equiv
\neg p\land\neg q,
$$

y esta última sí está en ambas formas según nuestras convenciones.

---

### Construir desde las filas verdaderas {#apm-t1-c02-e0125}
Una fórmula $F$ tiene la tabla:

| $p$ | $q$ | $F$ |
|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm F$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |

Construye una FND equivalente a $F$ directamente desde las filas verdaderas.

#### Solución


Las filas verdaderas son:

$$
(\mathrm V,\mathrm F)
$$

y:

$$
(\mathrm F,\mathrm V).
$$

La primera produce:

$$
p\land\neg q.
$$

La segunda produce:

$$
\neg p\land q.
$$

Disyuntamos:

$$
\boxed{
F
\equiv
(p\land\neg q)\lor(\neg p\land q).
}
$$

Esta FND es verdadera exactamente en las dos filas verdaderas de $F$.

---

### La conjunción y la cláusula de una fila {#apm-t1-c02-e0126}
Considera la asignación:

$$
p=\mathrm V,
\qquad
q=\mathrm F,
\qquad
r=\mathrm V.
$$

#### a)

Construye una conjunción de literales verdadera exactamente en esa fila.

#### b)

Construye una disyunción de literales falsa exactamente en esa fila.

#### c)

Explica por qué las construcciones tienen esas propiedades.

#### Solución


#### a)

Tomamos el literal que recibe $\mathrm V$ para cada variable:

$$
p,\qquad
\neg q,\qquad
r.
$$

La conjunción es:

$$
\boxed{
p\land\neg q\land r.
}
$$

#### b)

Ahora tomamos un literal falso en la fila para cada variable:

$$
\neg p,\qquad
q,\qquad
\neg r.
$$

La disyunción es:

$$
\boxed{
\neg p\lor q\lor\neg r.
}
$$

#### c)

La conjunción exige simultáneamente los tres valores de la fila. Si cualquiera cambia, uno de sus literales se vuelve falso.

La disyunción es falsa solo cuando sus tres literales son falsos simultáneamente, lo que ocurre exactamente en la asignación dada.

---

### Explorar la no unicidad {#apm-t1-c02-e0127}
Demuestra mediante las leyes ya establecidas que:

$$
(p\land q)\lor(p\land\neg q)
\equiv
p
$$

y:

$$
(p\lor q)\land(p\lor\neg q)
\equiv
p.
$$

Explica qué muestran estas dos equivalencias sobre las formas normales.

#### Solución


Para la primera:

$$
(p\land q)\lor(p\land\neg q)
$$

$$
\equiv
p\land(q\lor\neg q)
\qquad\text{(distributividad inversa)}.
$$

Por complemento:

$$
q\lor\neg q\equiv T.
$$

Entonces:

$$
\equiv
p\land T.
$$

Por identidad:

$$
\equiv
p.
$$

Para la segunda:

$$
(p\lor q)\land(p\lor\neg q)
$$

$$
\equiv
p\lor(q\land\neg q)
\qquad\text{(distributividad inversa)}.
$$

Por complemento:

$$
q\land\neg q\equiv C.
$$

Entonces:

$$
\equiv
p\lor C.
$$

Por identidad:

$$
\equiv
p.
$$

Así, $p$ posee formas normales más largas equivalentes.

Esto demuestra que la FND y la FNC de una fórmula no son únicas.

---

### Casos extremos {#apm-t1-c02-e0128}
#### a)

Da una FND y una FNC para una tautología.

#### b)

Da una FND y una FNC para una contradicción.

#### c)

Explica por qué estas fórmulas resuelven los casos extremos de [el teorema «Existencia de formas normales proposicionales»](#apm-t1-c02-t0001).

#### Solución


Podemos usar una variable $p$.

#### a) Tautología

Una FND es:

$$
p\lor\neg p.
$$

Es una disyunción de dos términos de un solo literal.

La misma fórmula también es una FNC con una única cláusula:

$$
\boxed{
p\lor\neg p.
}
$$

#### b) Contradicción

Una FND con un único término es:

$$
p\land\neg p.
$$

La misma fórmula puede verse como FNC con dos cláusulas de un literal:

$$
p
$$

y:

$$
\neg p.
$$

Por tanto:

$$
\boxed{
p\land\neg p
}
$$

sirve en ambas formas.

#### c)

Si una fórmula es contradicción, no existen filas verdaderas a partir de las cuales construir términos de FND. La fórmula:

$$
p\land\neg p
$$

proporciona entonces una FND contradictoria equivalente.

Si una fórmula es tautología, no existen filas falsas a partir de las cuales construir cláusulas de FNC. La fórmula:

$$
p\lor\neg p
$$

proporciona una FNC tautológica equivalente.

---

### Síntesis: tabla, FND, FNC y simplificación {#apm-t1-c02-e0129}
Considera:

$$
F=\neg(p\leftrightarrow q)\lor p.
$$

#### a)

Construye la tabla completa de $F$.

#### b)

A partir de las filas verdaderas, construye una FND.

#### c)

A partir de las filas falsas, construye una FNC.

#### d)

Simplifica algebraicamente $F$ y compara el resultado con la FNC obtenida.

#### Solución


#### a) Tabla

| $p$ | $q$ | $p\leftrightarrow q$ | $\neg(p\leftrightarrow q)$ | $F$ |
|---|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |

#### b) FND

Las filas verdaderas son:

$$
(\mathrm V,\mathrm V),
\qquad
(\mathrm V,\mathrm F),
\qquad
(\mathrm F,\mathrm V).
$$

Producen:

$$
p\land q,
$$

$$
p\land\neg q,
$$

$$
\neg p\land q.
$$

Por tanto:

$$
\boxed{
F
\equiv
(p\land q)
\lor
(p\land\neg q)
\lor
(\neg p\land q).
}
$$

#### c) FNC

La única fila falsa es:

$$
(\mathrm F,\mathrm F).
$$

La cláusula falsa exactamente allí es:

$$
p\lor q.
$$

Por tanto:

$$
\boxed{
F\equiv p\lor q.
}
$$

Esta es una FNC de una sola cláusula.

#### d) Simplificación algebraica

Por [la proposición «Equivalencias fundamentales del bicondicional»](#apm-t1-c02-p0006):

$$
\neg(p\leftrightarrow q)
\equiv
(p\land\neg q)\lor(\neg p\land q).
$$

Entonces:

$$
F
\equiv
(p\land\neg q)\lor(\neg p\land q)\lor p.
$$

Por absorción:

$$
p\lor(p\land\neg q)
\equiv
p.
$$

Así:

$$
F
\equiv
p\lor(\neg p\land q).
$$

Por distributividad:

$$
p\lor(\neg p\land q)
\equiv
(p\lor\neg p)\land(p\lor q).
$$

Por complemento:

$$
p\lor\neg p\equiv T.
$$

Por identidad:

$$
F\equiv p\lor q.
$$

Obtenemos exactamente la FNC producida por la única fila falsa:

$$
\boxed{
F\equiv p\lor q.
}
$$

El ejercicio muestra dos rutas distintas hacia la misma forma: una semántica, desde la tabla, y otra algebraica, mediante equivalencias.

---

## Síntesis

Un **literal** es una variable proposicional o su negación.

Una **FND** es una disyunción de conjunciones de literales.

Una **FNC** es una conjunción de disyunciones de literales.

La tabla de verdad proporciona dos construcciones sistemáticas:

$$

\text{filas }\mathrm V
\longrightarrow
\text{conjunciones que reconocen cada fila}
\longrightarrow
\text{FND}

$$

y:

$$

\text{filas }\mathrm F
\longrightarrow
\text{disyunciones que fallan en cada fila}
\longrightarrow
\text{FNC}.

$$

Con ello demostramos:

> [el teorema «Existencia de formas normales proposicionales»](#apm-t1-c02-t0001) — toda fórmula proposicional del lenguaje considerado admite una FND y una FNC lógicamente equivalentes.

El resultado no garantiza unicidad ni minimalidad. Garantiza **existencia mediante un procedimiento explícito**.

---

## Hacia la sección siguiente

Ya tenemos dos grandes maneras de estudiar una fórmula:

1. construir su tabla de verdad;
2. transformarla mediante leyes de equivalencia.

Además, ahora sabemos fabricar formas normales directamente desde la tabla.

La última pregunta del capítulo será estratégica:

> ante una fórmula concreta, ¿qué método conviene elegir?

La sección final comparará estas herramientas y cerrará el tránsito desde semántica a cálculo:

## §12. Demostrar una tautología y elegir método

A lo largo del capítulo hemos construido varias herramientas para estudiar fórmulas proposicionales.

Podemos:

1. **evaluarlas** mediante una tabla de verdad;
2. **clasificarlas** como tautologías, contradicciones o contingencias;
3. **compararlas** mediante equivalencia lógica;
4. **transformarlas** mediante leyes ya demostradas;
5. **refutar** una afirmación mediante una contraasignación;
6. **reconstruirlas** desde su tabla mediante FND o FNC.

Estas herramientas no compiten entre sí. Responden a preguntas distintas.

El problema final del capítulo será aprender a elegir:

$$
\boxed{
\text{qué queremos demostrar}
\quad\longrightarrow\quad
\text{qué método conviene utilizar}.
}
$$

Una buena solución no es solamente correcta. También debe ser **proporcionada al problema**.

Construir una tabla de ocho filas para una equivalencia que se reduce en tres pasos puede ser correcto, pero innecesariamente costoso.

Intentar simplificar algebraicamente una fórmula cuando basta una sola contraasignación también puede ser correcto, pero poco eficiente.

La madurez lógica comienza cuando podemos reconocer esa diferencia.

---

### 12.1 Método 1 — Tabla de verdad

La tabla de verdad es el procedimiento semántico más directo.

Resulta especialmente útil cuando queremos:

- conocer el comportamiento completo de una fórmula;
- decidir si es tautología, contradicción o contingencia;
- comparar dos fórmulas con pocas variables;
- obtener una FND o una FNC desde las filas de la tabla.

Su principal ventaja es:

$$
\text{exhaustividad}.
$$

Si una fórmula contiene:

$$
n
$$

variables proposicionales distintas, la tabla contiene:

$$
2^n
$$

filas. Eso mismo muestra su principal costo. Con dos variables necesitamos:

$$
4
$$

filas. Con tres:

$$
8.
$$

Con cuatro:

$$
16.
$$

Con cinco:

$$
32.
$$

Por tanto, una tabla completa es conceptualmente sencilla, pero puede crecer rápidamente.

---

### 12.2 Método 2 — Cadena de equivalencias

Si reconocemos en una fórmula estructuras ya cubiertas por nuestras leyes, podemos transformarla mediante:

$$
F_0
\equiv
F_1
\equiv
\cdots
\equiv
F_n.
$$

Este método es especialmente útil cuando queremos:

- simplificar una fórmula;
- eliminar implicaciones o bicondicionales;
- demostrar que dos fórmulas son equivalentes;
- demostrar una tautología reduciéndola a una fórmula tautológica conocida.

Por ejemplo, $P\Rightarrow P$ se transforma en:

$$
\neg P\lor P.
$$

Por complemento:

$$
\neg P\lor P\equiv T.
$$

Luego:

$$
P\Rightarrow P
$$

es una tautología. No hemos necesitado construir su tabla.

La ventaja es:

$$
\text{economía cuando la estructura es reconocible}.
$$

La exigencia es igualmente clara:

> cada paso debe estar autorizado por una equivalencia previamente demostrada.

---

### 12.3 Método 3 — Contraasignación

Supongamos que alguien afirma:

> «$F$ es una tautología».

Para refutarlo no necesitamos saber qué ocurre en todas las filas.

Basta encontrar una donde:

$$
F=\mathrm F.
$$

Análogamente, para refutar:

$$
P\equiv Q,
$$

basta una asignación donde $P$ y $Q$ reciban valores distintos.

La contraasignación es, por tanto, el método natural cuando la tarea consiste en **refutar una afirmación universal sobre todas las asignaciones**.

Su ventaja es:

$$
\text{una sola fila puede bastar}.
$$

Por ejemplo, la fórmula $(P\lor Q)\Rightarrow P$ no es una tautología, porque para:

$$
P=\mathrm F,
\qquad
Q=\mathrm V
$$

obtenemos:

$$
(P\lor Q)\Rightarrow P
=
\mathrm V\Rightarrow\mathrm F
=
\mathrm F.
$$

No hace falta calcular las otras tres filas.

---

### 12.4 Método 4 — Formas normales

Las formas normales son especialmente útiles cuando queremos reconstruir una fórmula desde su comportamiento semántico.

Desde una tabla:

$$
\text{filas }\mathrm V
\longrightarrow
\text{FND},
$$

$$
\text{filas }\mathrm F
\longrightarrow
\text{FNC}.
$$

También pueden ser útiles cuando queremos una forma regular que utilice solamente:

$$
\neg,\qquad
\land,\qquad
\lor.
$$

Pero una forma normal obtenida directamente de una tabla no tiene por qué ser la forma más corta.

Así, las formas normales son especialmente valiosas para:

$$
\boxed{\text{existencia, reconstrucción y organización}},
$$

más que para garantizar simplificación mínima.

---

### 12.5 Una guía de elección

Podemos resumir provisionalmente:

| Pregunta | Método que conviene probar primero |
|---|---|
| ¿Qué ocurre en todas las asignaciones? | tabla de verdad |
| ¿Es tautología con pocas variables? | tabla o equivalencias |
| ¿Puedo reducirla rápidamente a leyes conocidas? | equivalencias |
| ¿Quiero refutar que sea tautología? | contraasignación |
| ¿Quiero refutar una equivalencia? | contraasignación |
| ¿Quiero construir una fórmula desde una tabla? | FND/FNC |
| ¿Quiero una forma regular con $\neg,\land,\lor$? | transformación o formas normales |

Esta tabla no es un algoritmo obligatorio. Una misma tarea puede admitir varios métodos correctos.

La elección depende de la estructura concreta de la fórmula.

---

### 12.6 Demostrar una tautología mediante equivalencias

Consideremos $(P\land Q)\Rightarrow P$. Podemos construir una tabla.

Pero la transformación algebraica es muy corta. Eliminamos la implicación:

$$
(P\land Q)\Rightarrow P
\equiv
\neg(P\land Q)\lor P.
$$

Por De Morgan:

$$
\equiv
(\neg P\lor\neg Q)\lor P.
$$

Por asociatividad y conmutatividad:

$$
\equiv
(\neg P\lor P)\lor\neg Q.
$$

Por complemento:

$$
\equiv
T\lor\neg Q.
$$

Por dominación:

$$
\equiv
T.
$$

Por tanto:

$$
\boxed{
(P\land Q)\Rightarrow P
\text{ es una tautología}.
}
$$

Aquí la cadena de equivalencias revela además **por qué** la fórmula es siempre verdadera.

---

### 12.7 Demostrar una tautología mediante una tabla

Ahora tomemos una fórmula más compleja:

$$
(p\Rightarrow(q\Rightarrow r))
\leftrightarrow
((p\land q)\Rightarrow r).
$$

En [el ejercicio «Una equivalencia de implicaciones anidadas»](#apm-t1-c02-e0120) ya demostramos algebraicamente que las dos partes del bicondicional son lógicamente equivalentes.

Ahora construiremos la tabla completa para comprobarlo semánticamente. Necesitamos ocho filas.

| $p$ | $q$ | $r$ | $q\Rightarrow r$ | $p\Rightarrow(q\Rightarrow r)$ | $p\land q$ | $(p\land q)\Rightarrow r$ | Fórmula completa |
|---|---|---|---|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |

La columna final contiene únicamente:

$$
\mathrm V.
$$

Por definición:

$$
\boxed{
(p\Rightarrow(q\Rightarrow r))
\leftrightarrow
((p\land q)\Rightarrow r)
}
$$

es una tautología.

---

### 12.8 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-t1-c02-x0020}
**Ejemplo — Una tautología por dos métodos**
:::

Demostremos nuevamente que:

$$
(p\Rightarrow(q\Rightarrow r))
\leftrightarrow
((p\land q)\Rightarrow r)
$$

es una tautología, pero ahora comparemos deliberadamente dos métodos.

#### Método A — Tabla

La tabla de §12.7 muestra que la columna final contiene:

$$
\mathrm V
$$

en las ocho asignaciones. La fórmula es una tautología.

#### Método B — Transformación algebraica

Estudiemos primero el lado izquierdo del bicondicional:

$$
p\Rightarrow(q\Rightarrow r).
$$

Eliminamos la implicación exterior:

$$
\equiv
\neg p\lor(q\Rightarrow r).
$$

Eliminamos la implicación interior:

$$
\equiv
\neg p\lor(\neg q\lor r).
$$

Por asociatividad:

$$
\equiv
(\neg p\lor\neg q)\lor r.
$$

Por De Morgan en sentido inverso:

$$
\equiv
\neg(p\land q)\lor r.
$$

Por [la proposición «Equivalencias fundamentales de la implicación»](#apm-t1-c02-p0005) en sentido inverso:

$$
\equiv
(p\land q)\Rightarrow r.
$$

Por tanto:

$$
\boxed{
p\Rightarrow(q\Rightarrow r)
\equiv
(p\land q)\Rightarrow r.
}
$$

Por [la proposición «Criterio bicondicional para la equivalencia lógica»](#apm-t1-c02-p0001), el bicondicional entre dos fórmulas lógicamente equivalentes es una tautología.

Luego:

$$
\boxed{
(p\Rightarrow(q\Rightarrow r))
\leftrightarrow
((p\land q)\Rightarrow r)
}
$$

es una tautología.

#### Comparación

La tabla tiene una ventaja:

> hace visible el comportamiento completo de las ocho asignaciones.

La transformación tiene otra:

> muestra que las dos partes son en realidad dos escrituras equivalentes de la misma condición lógica.

Ambos métodos son rigurosos.

Pero responden a intuiciones diferentes.

---

### 12.9 Elegir un método no significa adivinar

La elección estratégica puede apoyarse en preguntas concretas.

#### ¿Hay pocas variables?

Una tabla puede ser razonable.

#### ¿Reconozco una ley inmediata?

Conviene intentar equivalencias.

#### ¿La afirmación que quiero demostrar parece falsa?

Antes de construir una tabla completa, conviene buscar una contraasignación.

#### ¿Tengo una tabla y quiero reconstruir la fórmula?

Las formas normales son naturales.

#### ¿Una primera ruta se vuelve larga?

Puede ser señal de que otra herramienta es mejor.

No hay contradicción en cambiar de método durante una solución.

La lógica matemática no exige fidelidad a una técnica.

Exige que cada conclusión esté justificada.

---

### 12.10 Verificar y demostrar

Una tabla completa puede demostrar una afirmación semántica porque enumera todas las asignaciones posibles.

Una cadena de equivalencias puede demostrarla porque cada paso conserva el comportamiento lógico.

Una contraasignación puede refutarla porque una sola excepción basta.

Una forma normal puede reconstruirla porque está diseñada para reproducir exactamente las filas verdaderas o falsas.

Los cuatro procedimientos son diferentes manifestaciones de una misma disciplina:

$$
\boxed{
\text{no basta obtener el resultado;}
\quad
\text{hay que controlar por qué el procedimiento lo garantiza}.
}
$$

---
## Ejercicios

### Elegir el método {#apm-t1-c02-e0130}
Para cada tarea, indica qué método intentarías primero entre:

- tabla de verdad;
- cadena de equivalencias;
- contraasignación;
- formas normales.

Justifica brevemente.

#### a)

Decidir si:

$$
(P\lor Q)\Rightarrow P
$$

es una tautología.

#### b)

Simplificar:

$$
\neg\neg(P\lor(P\land Q)).
$$

#### c)

Construir una fórmula a partir de una tabla que especifica exactamente tres filas verdaderas.

#### d)

Comparar semánticamente dos fórmulas de dos variables cuando no reconoces todavía una transformación útil.

#### Solución


#### a)

Intentaría primero una **contraasignación**.

La fórmula parece susceptible de fallar cuando:

$$
P=\mathrm F,
\qquad
Q=\mathrm V.
$$

En efecto:

$$
P\lor Q=\mathrm V,
$$

y:

$$
(P\lor Q)\Rightarrow P
=
\mathrm V\Rightarrow\mathrm F
=
\mathrm F.
$$

Una sola fila resuelve la pregunta.

#### b)

Intentaría primero una **cadena de equivalencias**.

Por doble negación:

$$
\neg\neg(P\lor(P\land Q))
\equiv
P\lor(P\land Q).
$$

Por absorción:

$$
\equiv
P.
$$

#### c)

Utilizaría **formas normales**, concretamente la FND construida a partir de las tres filas verdaderas.

#### d)

Con solo dos variables, una **tabla de verdad conjunta** requiere cuatro filas y permite comparar exhaustivamente ambas fórmulas.

---

### Una tautología por cálculo {#apm-t1-c02-e0131}
Demuestra mediante equivalencias que:

$$
(P\land Q)\Rightarrow(Q\lor R)
$$

es una tautología.

#### Solución


Eliminamos la implicación:

$$
(P\land Q)\Rightarrow(Q\lor R)
$$

$$
\equiv
\neg(P\land Q)\lor(Q\lor R).
$$

Por De Morgan:

$$
\equiv
(\neg P\lor\neg Q)\lor(Q\lor R).
$$

Por asociatividad y conmutatividad:

$$
\equiv
\neg P\lor(\neg Q\lor Q)\lor R.
$$

Por complemento:

$$
\neg Q\lor Q\equiv T.
$$

Entonces:

$$
\equiv
\neg P\lor T\lor R.
$$

Por dominación:

$$
\equiv
T.
$$

Por tanto:

$$
\boxed{
(P\land Q)\Rightarrow(Q\lor R)
\text{ es una tautología}.
}
$$

---

### Refutar sin tabla completa {#apm-t1-c02-e0132}
Decide si:

$$
(P\Rightarrow Q)\Rightarrow(Q\Rightarrow P)
$$

es una tautología.

Si no lo es, refútalo mediante una sola contraasignación.

#### Solución


Para hacer falsa la implicación exterior necesitamos:

- antecedente verdadero;
- consecuente falso.

Tomemos:

$$
P=\mathrm F,
\qquad
Q=\mathrm V.
$$

Entonces:

$$
P\Rightarrow Q
=
\mathrm F\Rightarrow\mathrm V
=
\mathrm V.
$$

Pero:

$$
Q\Rightarrow P
=
\mathrm V\Rightarrow\mathrm F
=
\mathrm F.
$$

Por tanto:

$$
(P\Rightarrow Q)\Rightarrow(Q\Rightarrow P)
=
\mathrm V\Rightarrow\mathrm F
=
\mathrm F.
$$

Así:

$$
\boxed{
(P\Rightarrow Q)\Rightarrow(Q\Rightarrow P)
\text{ no es una tautología}.
}
$$

Una sola contraasignación basta.

---

### Dos fórmulas, una misma condición {#apm-t1-c02-e0133}
Demuestra:

$$
(P\lor Q)\Rightarrow R
\equiv
(P\Rightarrow R)\land(Q\Rightarrow R).
$$

Después explica qué método resultó especialmente natural.

#### Solución


Transformemos el lado izquierdo:

$$
(P\lor Q)\Rightarrow R.
$$

Eliminamos la implicación:

$$
\equiv
\neg(P\lor Q)\lor R.
$$

Por De Morgan:

$$
\equiv
(\neg P\land\neg Q)\lor R.
$$

Por conmutatividad:

$$
\equiv
R\lor(\neg P\land\neg Q).
$$

Por distributividad:

$$
\equiv
(R\lor\neg P)\land(R\lor\neg Q).
$$

Por conmutatividad en cada cláusula:

$$
\equiv
(\neg P\lor R)\land(\neg Q\lor R).
$$

Reconocemos las implicaciones:

$$
\equiv
(P\Rightarrow R)\land(Q\Rightarrow R).
$$

Por tanto:

$$
\boxed{
(P\lor Q)\Rightarrow R
\equiv
(P\Rightarrow R)\land(Q\Rightarrow R).
}
$$

La cadena de equivalencias es especialmente natural porque las leyes de eliminación de implicación, De Morgan y distributividad encajan directamente con la estructura de la fórmula.

Una tabla de ocho filas también funcionaría, pero sería más larga.

---

### Síntesis final {#apm-t1-c02-e0134}
Determina, con un método adecuado y una justificación completa, si:

$$
[(P\Rightarrow Q)\land(Q\Rightarrow R)]
\Rightarrow
(P\Rightarrow R)
$$

es una tautología.

#### Solución


Una cadena de equivalencias permite aprovechar directamente las leyes ya construidas.

Partimos de:

$$
[(P\Rightarrow Q)\land(Q\Rightarrow R)]
\Rightarrow
(P\Rightarrow R).
$$

Eliminamos la implicación exterior:

$$
\equiv
\neg[(P\Rightarrow Q)\land(Q\Rightarrow R)]
\lor
(P\Rightarrow R).
$$

Por De Morgan:

$$
\equiv
\neg(P\Rightarrow Q)
\lor
\neg(Q\Rightarrow R)
\lor
(P\Rightarrow R).
$$

Usamos [la proposición «Equivalencias fundamentales de la implicación»](#apm-t1-c02-p0005):

$$
\neg(P\Rightarrow Q)
\equiv
P\land\neg Q,
$$

$$
\neg(Q\Rightarrow R)
\equiv
Q\land\neg R,
$$

y:

$$
P\Rightarrow R
\equiv
\neg P\lor R.
$$

Entonces:

$$
\equiv
(P\land\neg Q)
\lor
(Q\land\neg R)
\lor
\neg P
\lor
R.
$$

Reordenamos:

$$
\equiv
\bigl[\neg P\lor(P\land\neg Q)\bigr]
\lor
(Q\land\neg R)
\lor
R.
$$

Por distributividad:

$$
\neg P\lor(P\land\neg Q)
$$

$$
\equiv
(\neg P\lor P)\land(\neg P\lor\neg Q).
$$

Por complemento e identidad:

$$
\equiv
\neg P\lor\neg Q.
$$

Sustituyendo:

$$
\equiv
(\neg P\lor\neg Q)
\lor
(Q\land\neg R)
\lor
R.
$$

Reordenamos para reunir:

$$
\neg Q
$$

con:

$$
Q\land\neg R.
$$

Entonces:

$$
\neg Q\lor(Q\land\neg R)
$$

$$
\equiv
(\neg Q\lor Q)\land(\neg Q\lor\neg R)
$$

$$
\equiv
\neg Q\lor\neg R.
$$

Por tanto, la fórmula completa es equivalente a:

$$
\neg P\lor\neg Q\lor\neg R\lor R.
$$

Reagrupamos:

$$
\equiv
\neg P\lor\neg Q\lor(\neg R\lor R).
$$

Por complemento:

$$
\neg R\lor R\equiv T.
$$

Por dominación:

$$
\equiv
T.
$$

Por tanto:

$$
\boxed{
[(P\Rightarrow Q)\land(Q\Rightarrow R)]
\Rightarrow
(P\Rightarrow R)
}
$$

es una tautología.

La fórmula expresa, dentro de la lógica proposicional, la transitividad esperada de una cadena de implicaciones.

---

## Síntesis del capítulo

Comenzamos distinguiendo:

$$
\text{expresión}
$$

de:

$$
\text{proposición}.
$$

Después representamos proposiciones mediante variables y aprendimos a construir fórmulas con:

$$
\neg,\qquad
\land,\qquad
\lor,\qquad
\Rightarrow,\qquad
\leftrightarrow.
$$

La tabla de verdad nos permitió pasar de una fórmula aislada a su comportamiento completo bajo todas las asignaciones.

A partir de allí distinguimos:

- tautologías;
- contradicciones;
- contingencias.

Después definimos:

$$
P\equiv Q
$$

y convertimos equivalencias demostradas en leyes de cálculo. Construimos progresivamente:

- identidad y dominación;
- idempotencia y complemento;
- doble negación;
- conmutatividad y asociatividad;
- distributividad y absorción;
- leyes de De Morgan;
- equivalencias de implicación;
- equivalencias del bicondicional.

Finalmente demostramos que toda fórmula del lenguaje considerado admite formas normales disyuntiva y conjuntiva equivalentes.

El recorrido completo puede condensarse así:

$$

\text{proposiciones}
\to
\text{fórmulas}
\to
\text{semántica}
\to
\text{equivalencia}
\to
\text{leyes}
\to
\text{cálculo lógico}.

$$

Volvemos así a una idea estructural que acompañará todo este tratado:

$$

\text{una estructura}
=
\text{objetos}
+
\text{operaciones}
+
\text{leyes}.

$$

En este capítulo:

- los **objetos** son fórmulas proposicionales;
- las **operaciones** son los conectivos;
- la **semántica** asigna valores de verdad;
- las **leyes** son equivalencias lógicas que permiten transformar fórmulas sin alterar su comportamiento.

---

## Hacia el capítulo siguiente

La lógica proposicional trata una proposición como una unidad.

Por ejemplo:

> «Siete es primo».

Puede representarse mediante una sola letra:

$$
p.
$$

Pero muchas afirmaciones matemáticas poseen una estructura interna que ahora queremos estudiar.

Comparemos:

> «Siete es primo».

con:

> «$x$ es primo».

La segunda escritura depende de qué objeto represente $x$.

Y aparecen además expresiones como:

> «Todo número de cierto tipo cumple una propiedad».

> «Existe algún número con determinada propiedad».

Para representar rigurosamente estas afirmaciones necesitaremos abrir la proposición y estudiar:

- variables;
- predicados;
- dominio;
- expresiones como «todo» y «existe».

Ese será el objeto del próximo capítulo:

[**Capítulo 3. Predicados, cuantificadores y lenguaje matemático**](algebra-para-matematicos-capitulo-3-predicados-cuantificadores-y-lenguaje-matematico.md)
