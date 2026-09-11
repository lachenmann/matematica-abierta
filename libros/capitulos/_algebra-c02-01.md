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
