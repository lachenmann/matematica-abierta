---
title: "Topos desde cero — 1.5 Bicondicionales y condiciones necesarias y suficientes"
description: "Unidad del capítulo 1 de Topos desde cero: bicondicional, si/solo si, condiciones necesarias y suficientes, y distinción entre ↔ y equivalencia lógica."
content-id: MA-LES-0002
content-type: lesson
status: published
date-created: 2026-09-08
date-modified: 2026-09-08
areas:
  - fundamentos
level: fundamental
topics:
  - logica-matematica
  - bicondicional
  - si-y-solo-si
  - condiciones-necesarias
  - condiciones-suficientes
  - equivalencia-logica
  - traduccion-logica
  - tautologias
prerequisites:
  - MA-LES-0001
related:
  - MA-BCH-0002
  - MA-BOK-0002
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# 1.5 Bicondicionales y condiciones necesarias y suficientes {#sec-1-5-bicondicionales}

::: {.callout-note title="Continuidad editorial"}
Esta unidad continúa el **Capítulo 1 — Proposiciones y razonamiento deductivo** de *Topos desde cero* (`MA-BCH-0002`). Presupone la sección 1.4, donde se introdujeron la implicación, la recíproca y la contrapositiva.
:::

::: {.callout-note title="Resultados de aprendizaje"}
Al terminar esta sección, el lector podrá:

- interpretar el bicondicional $P\leftrightarrow Q$ y construir su tabla de verdad;
- reconocer que $P\leftrightarrow Q$ equivale a $(P\to Q)\land(Q\to P)$;
- usar las formas equivalentes $(P\land Q)\lor(\neg P\land\neg Q)$ y $\neg(P\leftrightarrow Q)$;
- traducir correctamente «si», «solo si» y «si y solo si»;
- distinguir condiciones necesarias de condiciones suficientes;
- reconocer que «$P$ es condición necesaria y suficiente para $Q$» expresa un bicondicional;
- distinguir la conectiva $\leftrightarrow$ de la relación metalingüística $\equiv$;
- descomponer un bicondicional en las dos direcciones que más adelante habrá que demostrar.
:::

::: {.callout-warning title="Motivación"}
En matemáticas no siempre queremos afirmar una sola dirección. A menudo necesitamos decir que dos condiciones se determinan mutuamente: una implica la otra y la otra implica la primera. Esa situación aparece en caracterizaciones, definiciones equivalentes y teoremas del tipo «una propiedad ocurre exactamente cuando se cumple cierta condición».

El lenguaje cotidiano suele borrar la diferencia entre «si», «solo si» y «si y solo si». En matemáticas esa ambigüedad es peligrosa. Esta sección fija una traducción precisa para cada expresión.
:::

## 1.5.1 La conectiva bicondicional

::: {.callout-important title="Definición"}
Si $P$ y $Q$ son proposiciones, el **bicondicional**

$$
P\leftrightarrow Q
$$

se lee «$P$ si y solo si $Q$».

Por definición,

$$
\boxed{P\leftrightarrow Q\equiv(P\to Q)\land(Q\to P).}
$$

Es decir, el bicondicional reúne simultáneamente las dos implicaciones opuestas.

Su tabla de verdad es:

| $P$ | $Q$ | $P\leftrightarrow Q$ |
|---|---|---|
| V | V | V |
| V | F | F |
| F | V | F |
| F | F | V |
:::

Por tanto, $P\leftrightarrow Q$ es verdadero exactamente cuando $P$ y $Q$ tienen el mismo valor de verdad.

### Ejemplo resuelto 32

Calcula el valor de

$$
P\leftrightarrow Q
$$

si $P$ es verdadera y $Q$ es falsa.

**Solución.** Las proposiciones tienen valores distintos. Por la tabla del bicondicional,

$$
P\leftrightarrow Q=F.
$$

También puede verse desde la definición:

$$
P\to Q=F,\qquad Q\to P=V,
$$

y por tanto

$$
(P\to Q)\land(Q\to P)=F.
$$

### Ejemplo resuelto 33

Sean

$$
P:\quad 15\text{ es par},
$$

$$
Q:\quad 15\text{ es divisible por }4.
$$

Determina el valor de $P\leftrightarrow Q$.

**Solución.** Tanto $P$ como $Q$ son falsas. Como el bicondicional es verdadero cuando ambas proposiciones tienen el mismo valor de verdad,

$$
P\leftrightarrow Q=V.
$$

Este ejemplo recuerda algo importante: que un bicondicional concreto resulte verdadero no significa que hayamos descubierto una ley general entre las propiedades consideradas. Solo hemos evaluado dos proposiciones cerradas.

### Ejemplo resuelto 34

Verifica mediante una tabla que

$$
P\leftrightarrow Q\equiv(P\to Q)\land(Q\to P).
$$

**Solución.**

| $P$ | $Q$ | $P\to Q$ | $Q\to P$ | $(P\to Q)\land(Q\to P)$ |
|---|---|---|---|---|
| V | V | V | V | V |
| V | F | F | V | F |
| F | V | V | F | F |
| F | F | V | V | V |

La última columna tiene el patrón

$$
V,\ F,\ F,\ V,
$$

que es precisamente la tabla de $P\leftrightarrow Q$.

## 1.5.2 Dos formas equivalentes especialmente útiles

Como el bicondicional es verdadero cuando las dos proposiciones coinciden en valor, podemos describir sus dos casos favorables:

> $P$ y $Q$ verdaderas, o bien $P$ y $Q$ falsas.

Esto conduce a

$$
\boxed{P\leftrightarrow Q\equiv(P\land Q)\lor(\neg P\land\neg Q).}
$$

### Ejemplo resuelto 35

Deriva la equivalencia

$$
P\leftrightarrow Q\equiv(P\land Q)\lor(\neg P\land\neg Q)
$$

partiendo de la tabla del bicondicional.

**Solución.** La tabla de $P\leftrightarrow Q$ es verdadera exactamente en las filas

$$
(P,Q)=(V,V)
$$

y

$$
(P,Q)=(F,F).
$$

La primera fila favorable se describe mediante

$$
P\land Q,
$$

y la segunda mediante

$$
\neg P\land\neg Q.
$$

Como basta que ocurra uno de los dos casos, los unimos con $\lor$:

$$
(P\land Q)\lor(\neg P\land\neg Q).
$$

Negar un bicondicional significa exigir que las dos proposiciones tengan valores diferentes. Por eso

$$
\boxed{\neg(P\leftrightarrow Q)\equiv(P\land\neg Q)\lor(\neg P\land Q).}
$$

La expresión de la derecha es la disyunción exclusiva que encontramos anteriormente.

### Ejemplo resuelto 36

Simplifica

$$
\neg(P\leftrightarrow Q)
$$

sin usar el símbolo $\leftrightarrow$.

**Solución.** Un bicondicional es falso exactamente en dos casos:

$$
P=V,\ Q=F,
$$

o

$$
P=F,\ Q=V.
$$

Por tanto,

$$
\boxed{\neg(P\leftrightarrow Q)\equiv(P\land\neg Q)\lor(\neg P\land Q).}
$$

## 1.5.3 «Si», «solo si» y «si y solo si»

Las siguientes tres expresiones deben mantenerse estrictamente separadas:

$$
\text{«$P$ si $Q$»}\quad\Longleftrightarrow\quad Q\to P,
$$

$$
\text{«$P$ solo si $Q$»}\quad\Longleftrightarrow\quad P\to Q,
$$

$$
\text{«$P$ si y solo si $Q$»}\quad\Longleftrightarrow\quad P\leftrightarrow Q.
$$

La expresión «solo si» merece especial atención. Decir

> «$P$ solo si $Q$»

significa que $Q$ es indispensable para que ocurra $P$. Si $P$ ocurre, entonces $Q$ debe ocurrir:

$$
P\to Q.
$$

### Ejemplo resuelto 37

Traduce:

> «La solicitud se aprueba solo si está completa».

Sea

$$
A:\quad\text{«La solicitud se aprueba»},\qquad
C:\quad\text{«La solicitud está completa»}.
$$

**Solución.** «$A$ solo si $C$» significa

$$
A\to C.
$$

La frase no afirma todavía que toda solicitud completa sea aprobada. Esa sería la dirección recíproca $C\to A$.

### Ejemplo resuelto 38

Traduce:

> «La solicitud se aprueba si está completa».

con las mismas letras del ejemplo anterior.

**Solución.** Ahora la condición «estar completa» aparece después de «si» y funciona como antecedente:

$$
C\to A.
$$

Obsérvese que hemos invertido la dirección respecto del ejemplo 37.

### Ejemplo resuelto 39

Traduce:

> «La solicitud se aprueba si y solo si está completa».

**Solución.** La frase exige simultáneamente

$$
C\to A
$$

y

$$
A\to C.
$$

Por tanto,

$$
A\leftrightarrow C.
$$

::: {.callout-warning title="Atención"}
En el lenguaje ordinario, una persona puede decir «si» queriendo sugerir «si y solo si». En matemáticas no debemos añadir silenciosamente la dirección recíproca. Un enunciado $P\to Q$ afirma exactamente una dirección; si se necesitan ambas, debe escribirse o decirse explícitamente.
:::

## 1.5.4 Condiciones suficientes y condiciones necesarias

La terminología de condiciones expresa la misma estructura de la implicación desde otro punto de vista.

::: {.callout-important title="Definición"}
Para la implicación

$$
P\to Q,
$$

decimos que:

- $P$ es una **condición suficiente** para $Q$;
- $Q$ es una **condición necesaria** para $P$.
:::

La palabra **suficiente** apunta hacia adelante: que $P$ sea verdadera basta para garantizar $Q$.

La palabra **necesaria** apunta hacia atrás: si queremos que $P$ sea verdadera, no podemos prescindir de $Q$.

### Ejemplo resuelto 40

Sea

$$
E:\quad\text{«El documento está firmado electrónicamente»},
$$

$$
V:\quad\text{«El documento supera la verificación de firma»}.
$$

Supongamos que el enunciado considerado es

$$
E\to V.
$$

¿Cómo se expresa con el lenguaje de condiciones?

**Solución.** El antecedente es condición suficiente para el consecuente:

> «Estar firmado electrónicamente es una condición suficiente para superar la verificación de firma».

A la vez, el consecuente es condición necesaria para el antecedente:

> «Superar la verificación de firma es una condición necesaria para estar firmado electrónicamente».

Ambas frases representan la misma forma lógica $E\to V$.

### Ejemplo resuelto 41

Traduce:

> «Tener una contraseña válida es una condición necesaria para iniciar sesión».

Sea

$$
C:\quad\text{«La contraseña es válida»},\qquad
I:\quad\text{«Se inicia sesión»}.
$$

**Solución.** Si $C$ es necesaria para $I$, entonces no puede ocurrir $I$ sin $C$. La implicación es

$$
I\to C.
$$

No debemos invertirla: la frase no afirma que una contraseña válida sea por sí sola suficiente para iniciar sesión.

### Ejemplo resuelto 42

Traduce:

> «Estar inscrito es una condición suficiente para recibir el boletín».

Sea

$$
I:\quad\text{«La persona está inscrita»},\qquad
B:\quad\text{«La persona recibe el boletín»}.
$$

**Solución.** Una condición suficiente ocupa el antecedente:

$$
I\to B.
$$

Cuando una condición es a la vez necesaria y suficiente, obtenemos un bicondicional.

::: {.callout-important title="Definición"}
Decir que «$P$ es una condición necesaria y suficiente para $Q$» significa

$$
\boxed{P\leftrightarrow Q.}
$$

Equivalentemente, $P$ es suficiente para $Q$ y también necesaria para $Q$.
:::

### Ejemplo resuelto 43

Traduce:

> «Que ambas luces estén encendidas es una condición necesaria y suficiente para que aparezca la señal verde».

Sea

$$
L:\quad\text{«Ambas luces están encendidas»},\qquad
S:\quad\text{«Aparece la señal verde»}.
$$

**Solución.** La condición es necesaria y suficiente, por tanto exige las dos direcciones:

$$
L\to S
$$

y

$$
S\to L.
$$

En forma compacta,

$$
L\leftrightarrow S.
$$

## 1.5.5 Bicondicional y equivalencia lógica

En la sección 1.3 usamos

$$
A\equiv B
$$

para decir, desde fuera de las fórmulas, que $A$ y $B$ tienen el mismo valor de verdad en todas las asignaciones posibles. Ahora disponemos de una fórmula que compara sus valores:

$$
A\leftrightarrow B.
$$

Las dos ideas están relacionadas, pero no son el mismo símbolo ni cumplen exactamente la misma función.

::: {.callout-important title="Definición"}
- $A\leftrightarrow B$ es una **fórmula proposicional**. Para cada asignación concreta, puede resultar verdadera o falsa.
- $A\equiv B$ afirma **metalingüísticamente** que $A$ y $B$ coinciden en todas las asignaciones.

De las definiciones se sigue:

$$
\boxed{A\equiv B\quad\Longleftrightarrow\quad A\leftrightarrow B\text{ es una tautología}.}
$$
:::

### Ejemplo resuelto 44

Usa el resultado anterior para justificar de otra manera que

$$
P\to Q\equiv\neg P\lor Q.
$$

**Solución.** La equivalencia lógica significa que la fórmula

$$
(P\to Q)\leftrightarrow(\neg P\lor Q)
$$

debe ser verdadera para todas las asignaciones. Como en la sección anterior ya verificamos que $P\to Q$ y $\neg P\lor Q$ tienen columnas idénticas, el bicondicional entre ellas tendrá valor verdadero en cada fila. Por tanto es una tautología y, en consecuencia,

$$
P\to Q\equiv\neg P\lor Q.
$$

## 1.5.6 Dos direcciones que más adelante habrá que demostrar

La identidad

$$
P\leftrightarrow Q\equiv(P\to Q)\land(Q\to P)
$$

no es solo una regla para tablas de verdad. Determina la arquitectura de futuras demostraciones.

Cuando más adelante queramos demostrar un enunciado de la forma

$$
P\leftrightarrow Q,
$$

normalmente tendremos dos tareas:

$$
P\to Q
$$

y

$$
Q\to P.
$$

A veces se las denomina las direcciones **ida** y **vuelta** del bicondicional.

::: {.callout-tip title="Mirada hacia adelante"}
En el capítulo dedicado a estrategias de demostración convertiremos esta descomposición lógica en una técnica formal: para probar un bicondicional, se prueban por separado sus dos implicaciones. Por ahora solo necesitamos reconocer correctamente cuáles son esas dos direcciones.
:::

## 1.5.7 Problemas de práctica resueltos

### Problema de práctica 14

Sea

$$
P:\quad\text{«La alarma está activada»},\qquad
Q:\quad\text{«La luz roja está encendida»}.
$$

Traduce por separado:

1. «La alarma está activada si la luz roja está encendida».
2. «La alarma está activada solo si la luz roja está encendida».
3. «La alarma está activada si y solo si la luz roja está encendida».

### Problema de práctica 15

Expresa $P\leftrightarrow Q$ usando solo $\land$, $\lor$ y $\neg$, y explica por qué la fórmula obtenida tiene el patrón de verdad correcto.

### Problema de práctica 16

Traduce:

> «Tener la credencial vigente es una condición necesaria para entrar».

Usa $C$ para «la credencial está vigente» y $E$ para «se entra».

### Problema de práctica 17

Decide si

$$
(P\leftrightarrow Q)\leftrightarrow(Q\leftrightarrow P)
$$

es una tautología.

### Problema de práctica 18

Niega correctamente la afirmación

$$
P\leftrightarrow Q
$$

y expresa la negación sin usar $\leftrightarrow$.

## Soluciones de los problemas de práctica

### Problema de práctica 14

1. «$P$ si $Q$» significa

   $$
   Q\to P.
   $$

2. «$P$ solo si $Q$» significa

   $$
   P\to Q.
   $$

3. «$P$ si y solo si $Q$» significa

   $$
   P\leftrightarrow Q.
   $$

### Problema de práctica 15

El bicondicional es verdadero cuando $P,Q$ son ambas verdaderas o ambas falsas. Los dos casos son

$$
P\land Q
$$

y

$$
\neg P\land\neg Q.
$$

Por tanto,

$$
\boxed{P\leftrightarrow Q\equiv(P\land Q)\lor(\neg P\land\neg Q).}
$$

### Problema de práctica 16

Si $C$ es necesaria para $E$, entonces $E$ no puede ocurrir sin $C$:

$$
E\to C.
$$

### Problema de práctica 17

El bicondicional es simétrico: $P\leftrightarrow Q$ y $Q\leftrightarrow P$ tienen siempre el mismo valor de verdad. Por tanto, el bicondicional entre ambas fórmulas es siempre verdadero:

$$
(P\leftrightarrow Q)\leftrightarrow(Q\leftrightarrow P)
$$

es una tautología.

### Problema de práctica 18

Negar $P\leftrightarrow Q$ significa exigir valores distintos:

$$
\boxed{\neg(P\leftrightarrow Q)\equiv(P\land\neg Q)\lor(\neg P\land Q).}
$$

# Ejercicios de la sección 1.5

1. Construye la tabla de verdad de $P\leftrightarrow Q$ a partir de $(P\to Q)\land(Q\to P)$.
2. Decide el valor de verdad de los siguientes bicondicionales:
   a. «10 es par si y solo si $10>3$»;
   b. «9 es par si y solo si 9 es divisible por 2»;
   c. «$7<4$ si y solo si $12<5$».
3. Demuestra mediante una tabla que

   $$
   P\leftrightarrow Q\equiv(P\land Q)\lor(\neg P\land\neg Q).
   $$
4. Demuestra mediante una tabla que

   $$
   \neg(P\leftrightarrow Q)\equiv(P\land\neg Q)\lor(\neg P\land Q).
   $$
5. Traduce usando $P$ para «se publica el artículo» y $R$ para «el artículo supera la revisión»:
   a. «El artículo se publica si supera la revisión»;
   b. «El artículo se publica solo si supera la revisión»;
   c. «El artículo se publica si y solo si supera la revisión».
6. Sea $P\to Q$. Indica cuál de $P,Q$ es condición suficiente y cuál es condición necesaria.
7. Traduce «$P$ es condición suficiente para $Q$».
8. Traduce «$P$ es condición necesaria para $Q$».
9. Traduce «$P$ es condición necesaria y suficiente para $Q$».
10. Explica por qué «$P$ solo si $Q$» no significa $Q\to P$.
11. Decide si las fórmulas

    $$
    P\leftrightarrow Q
    $$

    y

    $$
    \neg P\leftrightarrow\neg Q
    $$

    son lógicamente equivalentes.
12. Simplifica

    $$
    (P\leftrightarrow Q)\land(P\leftrightarrow\neg Q).
    $$

    Clasifica el resultado como tautología, contradicción o contingencia.
13. Determina si

    $$
    (P\leftrightarrow Q)\lor(P\leftrightarrow\neg Q)
    $$

    es tautología, contradicción o contingencia.
14. **Encontrar el error.** Un estudiante traduce «Aprobar es condición necesaria para recibir el certificado» como $A\to C$, donde $A$ significa «se aprueba» y $C$ significa «se recibe el certificado». Explica y corrige el error.
15. **Encontrar el error.** Otro estudiante afirma que, como $P\leftrightarrow Q$ y $P\equiv Q$ «significan lo mismo», los símbolos pueden intercambiarse en cualquier fórmula. Explica por qué debemos distinguirlos.
16. Demuestra que

    $$
    P\leftrightarrow Q\equiv(P\to Q)\land(\neg P\to\neg Q).
    $$
17. Encuentra una fórmula usando solo $\neg$ y $\to$ que sea lógicamente equivalente a $P\leftrightarrow Q$.
18. **Desafío.** Demuestra que

    $$
    (P\leftrightarrow Q)\land(Q\leftrightarrow R)\to(P\leftrightarrow R)
    $$

    es una tautología. Interpreta verbalmente qué expresa.

# Soluciones completas de los ejercicios de la sección 1.5

## 1

| $P$ | $Q$ | $P\to Q$ | $Q\to P$ | $(P\to Q)\land(Q\to P)$ |
|---|---|---|---|---|
| V | V | V | V | V |
| V | F | F | V | F |
| F | V | V | F | F |
| F | F | V | V | V |

Así obtenemos la tabla de $P\leftrightarrow Q$.

## 2

1. «10 es par» y «$10>3$» son ambas verdaderas; el bicondicional es verdadero.
2. «9 es par» y «9 es divisible por 2» son ambas falsas; el bicondicional es verdadero.
3. «$7<4$» y «$12<5$» son ambas falsas; el bicondicional es verdadero.

En todos los casos los dos componentes tienen el mismo valor de verdad.

## 3

| $P$ | $Q$ | $P\leftrightarrow Q$ | $(P\land Q)\lor(\neg P\land\neg Q)$ |
|---|---|---|---|
| V | V | V | V |
| V | F | F | F |
| F | V | F | F |
| F | F | V | V |

Las columnas coinciden, luego las fórmulas son equivalentes.

## 4

| $P$ | $Q$ | $\neg(P\leftrightarrow Q)$ | $(P\land\neg Q)\lor(\neg P\land Q)$ |
|---|---|---|---|
| V | V | F | F |
| V | F | V | V |
| F | V | V | V |
| F | F | F | F |

Las columnas coinciden.

## 5

1. «$P$ si $R$»:

   $$
   R\to P.
   $$

2. «$P$ solo si $R$»:

   $$
   P\to R.
   $$

3. «$P$ si y solo si $R$»:

   $$
   P\leftrightarrow R.
   $$

## 6

En $P\to Q$,

$$
P\text{ es suficiente para }Q
$$

y

$$
Q\text{ es necesaria para }P.
$$

## 7

«$P$ es condición suficiente para $Q$» significa que la verdad de $P$ garantiza la de $Q$:

$$
P\to Q.
$$

## 8

«$P$ es condición necesaria para $Q$» significa que $Q$ no puede ocurrir sin $P$:

$$
Q\to P.
$$

## 9

Si $P$ es a la vez necesaria y suficiente para $Q$, se requieren las dos direcciones:

$$
P\to Q
$$

y

$$
Q\to P.
$$

Por tanto,

$$
P\leftrightarrow Q.
$$

## 10

«$P$ solo si $Q$» afirma que $Q$ es necesaria para $P$. Si $P$ ocurre, $Q$ debe ocurrir:

$$
P\to Q.
$$

La fórmula $Q\to P$ expresa la recíproca y requeriría una afirmación adicional.

## 11

Negar simultáneamente ambos componentes no cambia si coinciden o difieren. La tabla es:

| $P$ | $Q$ | $P\leftrightarrow Q$ | $\neg P\leftrightarrow\neg Q$ |
|---|---|---|---|
| V | V | V | V |
| V | F | F | F |
| F | V | F | F |
| F | F | V | V |

Por tanto,

$$
\boxed{(P\leftrightarrow Q)\equiv(\neg P\leftrightarrow\neg Q).}
$$

## 12

Para que $P\leftrightarrow Q$ sea verdadero, $P$ y $Q$ deben tener el mismo valor. Para que $P\leftrightarrow\neg Q$ sea verdadero, $P$ y $Q$ deben tener valores distintos. Ambas condiciones no pueden cumplirse simultáneamente. Por tanto,

$$
(P\leftrightarrow Q)\land(P\leftrightarrow\neg Q)
$$

es una **contradicción**.

## 13

En toda asignación, $P$ y $Q$ o bien tienen el mismo valor, o bien tienen valores distintos. En el primer caso es verdadero $P\leftrightarrow Q$; en el segundo, $P\leftrightarrow\neg Q$. Por tanto,

$$
(P\leftrightarrow Q)\lor(P\leftrightarrow\neg Q)
$$

es una **tautología**.

## 14

Si «aprobar» es necesario para «recibir el certificado», entonces no se puede recibir el certificado sin aprobar. La dirección correcta es

$$
C\to A.
$$

La traducción $A\to C$ convertiría aprobar en condición suficiente, que es una afirmación diferente.

## 15

$P\leftrightarrow Q$ es una fórmula proposicional y, según los valores asignados a $P$ y $Q$, puede ser verdadera o falsa. En cambio,

$$
P\equiv Q
$$

no es una conectiva dentro de la fórmula: afirma que las dos fórmulas tienen la misma tabla de verdad.

La relación correcta es que

$$
P\equiv Q
$$

si y solo si $P\leftrightarrow Q$ es una tautología.

## 16

Partimos de

$$
P\leftrightarrow Q\equiv(P\to Q)\land(Q\to P).
$$

Por la ley de la contrapositiva aplicada a $Q\to P$,

$$
Q\to P\equiv\neg P\to\neg Q.
$$

Sustituyendo,

$$
\boxed{P\leftrightarrow Q\equiv(P\to Q)\land(\neg P\to\neg Q).}
$$

## 17

Usamos

$$
P\leftrightarrow Q\equiv(P\to Q)\land(Q\to P).
$$

Usamos ahora la ley condicional para obtener una forma de la conjunción con solo $\neg$ y $\to$:

$$
\neg(A\to\neg B)
\equiv
\neg(\neg A\lor\neg B)
\equiv
A\land B,
$$

donde el último paso usa De Morgan y doble negación.

Tomando

$$
A=(P\to Q),\qquad B=(Q\to P),
$$

obtenemos

$$
\boxed{\neg\bigl((P\to Q)\to\neg(Q\to P)\bigr).}
$$

Una tabla de verdad verifica que esta fórmula coincide con $P\leftrightarrow Q$.

## 18

Si

$$
P\leftrightarrow Q
$$

y

$$
Q\leftrightarrow R
$$

son verdaderos, entonces $P$ tiene el mismo valor de verdad que $Q$, y $Q$ el mismo que $R$. Por tanto $P$ y $R$ tienen el mismo valor, de modo que

$$
P\leftrightarrow R
$$

es verdadero.

Si el antecedente compuesto es falso, la implicación completa es verdadera por la tabla de $\to$. Así,

$$
\boxed{(P\leftrightarrow Q)\land(Q\leftrightarrow R)\to(P\leftrightarrow R)}
$$

es una tautología.

Verbalmente expresa que, si $P$ coincide en valor de verdad con $Q$ y $Q$ coincide con $R$, entonces $P$ coincide con $R$.

::: {.callout-note title="Registro de dependencias"}
Esta sección introduce y deja disponibles:

- el bicondicional $\leftrightarrow$;
- las expresiones «si», «solo si» y «si y solo si»;
- la terminología de condiciones necesarias y suficientes;
- la distinción entre $\leftrightarrow$ y la equivalencia lógica $\equiv$.

Con las cinco conectivas principales ya disponibles, la sección 1.6 podrá estudiar formalmente argumentos deductivos, premisas, conclusiones y validez.
:::

---

**Siguiente sección:** 1.6 — Argumentos deductivos y validez.
