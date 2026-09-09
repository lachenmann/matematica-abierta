---
title: "Topos desde cero — 1.4 Implicación, contrapositiva y recíproca"
description: "Unidad del capítulo 1 de Topos desde cero: implicación, negación del condicional, recíproca, contrapositiva, inversa y errores de inferencia asociados."
content-id: MA-LES-0001
content-type: lesson
status: published
date-created: 2026-09-08
date-modified: 2026-09-08
areas:
  - fundamentos
level: fundamental
topics:
  - logica-matematica
  - implicacion
  - condicional
  - antecedente
  - consecuente
  - contrapositiva
  - reciproca
  - inversa
  - negacion-de-implicaciones
  - equivalencia-logica
  - inferencias-invalidas
prerequisites: []
related:
  - MA-BCH-0002
  - MA-BOK-0002
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# 1.4 Implicación, contrapositiva y recíproca {#sec-1-4-implicacion}

::: {.callout-note title="Continuidad editorial"}
Esta unidad continúa el **Capítulo 1 — Proposiciones y razonamiento deductivo** de *Topos desde cero* (`MA-BCH-0002`). Las secciones 1.1–1.3 permanecen reunidas en la página del capítulo; desde esta sección la publicación web adopta unidades modulares para mantener cada archivo editorial manejable y reutilizable.
:::

::: {.callout-note title="Resultados de aprendizaje"}
Al terminar esta sección, el lector podrá:

- interpretar la implicación $P\to Q$ e identificar su antecedente y su consecuente;
- construir y explicar la tabla de verdad de una implicación;
- reconocer que $P\to Q$ solo es falsa cuando $P$ es verdadera y $Q$ es falsa;
- usar las equivalencias $P\to Q\equiv\neg P\lor Q$ y $P\to Q\equiv\neg(P\land\neg Q)$;
- negar correctamente una implicación;
- distinguir una implicación de su recíproca, su contrapositiva y su inversa;
- justificar que una implicación es equivalente a su contrapositiva, pero no en general a su recíproca;
- detectar los errores de afirmar el consecuente y negar el antecedente.
:::

::: {.callout-warning title="Motivación"}
Una enorme proporción de las afirmaciones matemáticas tiene la forma «si ocurre esto, entonces ocurre aquello». Más adelante, las definiciones, los teoremas y las demostraciones estarán llenos de esta estructura. Por eso necesitamos fijar con precisión qué significa una implicación y, sobre todo, qué no significa.

El punto más delicado es este: una implicación lógica **no expresa necesariamente causalidad**. Su función es descartar una sola situación, aquella en la que el antecedente se cumple pero el consecuente falla.
:::

## 1.4.1 La conectiva condicional

::: {.callout-important title="Definición"}
Si $P$ y $Q$ son proposiciones, la **implicación** o **condicional**

$$
P\to Q
$$

se lee «si $P$, entonces $Q$». La proposición $P$ se llama **antecedente** y $Q$ se llama **consecuente**.

La tabla de verdad de la implicación es:

| $P$ | $Q$ | $P\to Q$ |
|---|---|---|
| V | V | V |
| V | F | F |
| F | V | V |
| F | F | V |
:::

La fila decisiva es la segunda. Si afirmamos «si $P$, entonces $Q$» y $P$ ocurre mientras $Q$ no ocurre, la afirmación ha fallado. En las otras tres filas no aparece ese fracaso.

### Ejemplo resuelto 19

Sean

$$
P:\quad 18\text{ es divisible por }3,
$$

$$
Q:\quad 18\text{ es par}.
$$

Ambas proposiciones son verdaderas. Por tanto,

$$
P\to Q
$$

es verdadera.

### Ejemplo resuelto 20

Sean

$$
P:\quad 15\text{ es divisible por }3,
$$

$$
Q:\quad 15\text{ es par}.
$$

Aquí $P$ es verdadera y $Q$ es falsa. Esta es precisamente la única combinación que hace falsa una implicación. Luego

$$
P\to Q
$$

es falsa.

### Ejemplo resuelto 21

Traduce la afirmación:

> «Si Ana estudia y no está cansada, entonces termina el capítulo».

Sea

$$
E:\quad\text{«Ana estudia»},\qquad
C:\quad\text{«Ana está cansada»},\qquad
T:\quad\text{«Ana termina el capítulo»}.
$$

El antecedente completo es $E\land\neg C$, y el consecuente es $T$. Por tanto,

$$
(E\land\neg C)\to T.
$$

Los paréntesis son esenciales: la implicación tiene como antecedente la conjunción completa.

## 1.4.2 Qué ocurre cuando el antecedente es falso

Las dos últimas filas de la tabla suelen sorprender al principio. Si $P$ es falsa, la implicación $P\to Q$ se considera verdadera, tanto si $Q$ es verdadera como si es falsa.

La razón se vuelve más transparente mediante una equivalencia fundamental:

$$
\boxed{P\to Q\equiv\neg P\lor Q.}
$$

Si $P$ es falsa, entonces $\neg P$ es verdadera, y por ello la disyunción $\neg P\lor Q$ es verdadera cualquiera que sea el valor de $Q$.

### Ejemplo resuelto 22

Verifica mediante una tabla que

$$
P\to Q\equiv\neg P\lor Q.
$$

**Solución.**

| $P$ | $Q$ | $\neg P$ | $P\to Q$ | $\neg P\lor Q$ |
|---|---|---|---|---|
| V | V | F | V | V |
| V | F | F | F | F |
| F | V | V | V | V |
| F | F | V | V | V |

Las dos columnas finales coinciden en todas las filas. Por tanto,

$$
\boxed{P\to Q\equiv\neg P\lor Q.}
$$

Existe una segunda formulación aún más útil:

$$
\boxed{P\to Q\equiv\neg(P\land\neg Q).}
$$

Una implicación afirma, por tanto, que no ocurre el caso prohibido

$$
P\land\neg Q.
$$

Dicho de otro modo: **no puede darse el antecedente sin el consecuente**.

### Ejemplo resuelto 23

Deriva

$$
P\to Q\equiv\neg(P\land\neg Q)
$$

a partir de $P\to Q\equiv\neg P\lor Q$.

**Solución.** Partimos de

$$
P\to Q\equiv\neg P\lor Q.
$$

Por doble negación,

$$
\neg P\lor Q\equiv\neg P\lor\neg\neg Q.
$$

Aplicando De Morgan en sentido inverso,

$$
\neg P\lor\neg\neg Q\equiv\neg(P\land\neg Q).
$$

Por transitividad de la equivalencia lógica,

$$
\boxed{P\to Q\equiv\neg(P\land\neg Q).}
$$

::: {.callout-warning title="Atención"}
No debemos leer $P\to Q$ como «$P$ causa $Q$». La conectiva solo codifica una condición de verdad. Por eso puede ser verdadera una implicación cuyos componentes no tengan ninguna relación causal entre sí. Lo único que la hace falsa es encontrar $P$ verdadera y $Q$ falsa.
:::

## 1.4.3 Negar una implicación

La equivalencia anterior permite obtener inmediatamente la negación correcta de una implicación:

$$
\neg(P\to Q)
\equiv
\neg\neg(P\land\neg Q)
\equiv
P\land\neg Q.
$$

Por tanto,

$$
\boxed{\neg(P\to Q)\equiv P\land\neg Q.}
$$

Esto expresa una idea decisiva para toda la matemática posterior: para refutar una afirmación de la forma «si $P$, entonces $Q$» necesitamos un caso en el que $P$ se cumpla y $Q$ falle.

### Ejemplo resuelto 24

Niega correctamente:

> «Si el número es múltiplo de 6, entonces es par».

**Solución.** Si llamamos $P$ a «el número es múltiplo de 6» y $Q$ a «el número es par», la afirmación tiene forma $P\to Q$. Su negación es

$$
P\land\neg Q.
$$

En palabras:

> «El número es múltiplo de 6 y no es par».

No basta decir «si el número es múltiplo de 6, entonces no es par», porque eso sería otra implicación distinta.

### Ejemplo resuelto 25

Simplifica

$$
\neg\bigl((P\land R)\to Q\bigr).
$$

**Solución.** Aplicamos la ley de negación del condicional tomando como antecedente $P\land R$:

$$
\neg\bigl((P\land R)\to Q\bigr)
\equiv
(P\land R)\land\neg Q.
$$

Por asociatividad,

$$
\boxed{P\land R\land\neg Q.}
$$

## 1.4.4 Recíproca, contrapositiva e inversa

A partir de una implicación

$$
P\to Q
$$

podemos formar otras tres expresiones relacionadas.

::: {.callout-important title="Definición"}
Dada $P\to Q$:

- su **recíproca** es $Q\to P$;
- su **contrapositiva** es $\neg Q\to\neg P$;
- su **inversa** es $\neg P\to\neg Q$.
:::

La recíproca intercambia antecedente y consecuente. La contrapositiva, en cambio, los intercambia y además los niega.

### Ejemplo resuelto 26

Considera la implicación:

> «Si hoy es martes, entonces mañana es miércoles».

Sean

$$
P:\quad\text{«Hoy es martes»},\qquad
Q:\quad\text{«Mañana es miércoles»}.
$$

Entonces:

- original: $P\to Q$;
- recíproca: $Q\to P$, «Si mañana es miércoles, entonces hoy es martes»;
- contrapositiva: $\neg Q\to\neg P$, «Si mañana no es miércoles, entonces hoy no es martes»;
- inversa: $\neg P\to\neg Q$, «Si hoy no es martes, entonces mañana no es miércoles».

### Ejemplo resuelto 27

Compara mediante una tabla la implicación, su recíproca, su contrapositiva y su inversa.

**Solución.**

| $P$ | $Q$ | $P\to Q$ | $Q\to P$ | $\neg Q\to\neg P$ | $\neg P\to\neg Q$ |
|---|---|---|---|---|---|
| V | V | V | V | V | V |
| V | F | F | V | F | V |
| F | V | V | F | V | F |
| F | F | V | V | V | V |

Observamos dos pares de columnas idénticas:

$$
\boxed{P\to Q\equiv\neg Q\to\neg P,}
$$

$$
\boxed{Q\to P\equiv\neg P\to\neg Q.}
$$

La original no coincide, en general, con su recíproca.

### Ejemplo resuelto 28

Demuestra algebraicamente la ley de la contrapositiva:

$$
P\to Q\equiv\neg Q\to\neg P.
$$

**Solución.** Usamos la equivalencia condicional:

$$
\neg Q\to\neg P
\equiv
\neg\neg Q\lor\neg P.
$$

Por doble negación,

$$
\neg\neg Q\lor\neg P
\equiv
Q\lor\neg P.
$$

Por conmutatividad de $\lor$,

$$
Q\lor\neg P
\equiv
\neg P\lor Q.
$$

Y

$$
\neg P\lor Q\equiv P\to Q.
$$

Así,

$$
\boxed{P\to Q\equiv\neg Q\to\neg P.}
$$

::: {.callout-warning title="Atención"}
Una implicación y su recíproca no son equivalentes en general. Confundirlas es uno de los errores lógicos más frecuentes. Para demostrar que no son equivalentes basta encontrar una asignación en la que sus valores difieran; por ejemplo, $P=V$ y $Q=F$.
:::

## 1.4.5 La contrapositiva como estrategia futura

Como una implicación y su contrapositiva son lógicamente equivalentes, cualquier método que establezca

$$
\neg Q\to\neg P
$$

establece también

$$
P\to Q.
$$

Más adelante convertiremos esta equivalencia en una técnica sistemática de demostración. Por ahora solo necesitamos registrar la identidad lógica que la justifica.

### Ejemplo resuelto 29

Supón que queremos establecer una afirmación de forma

$$
P\to Q.
$$

¿Cuál de las siguientes metas sería lógicamente equivalente?

1. $Q\to P$;
2. $\neg P\to\neg Q$;
3. $\neg Q\to\neg P$.

**Solución.** La contrapositiva de $P\to Q$ se obtiene negando ambos componentes e invirtiendo su orden:

$$
\neg Q\to\neg P.
$$

Por tanto, la opción correcta es **3**. Las opciones 1 y 2 son recíproca e inversa, respectivamente; estas dos sí son equivalentes entre sí, pero no tienen por qué ser equivalentes a la original.

## 1.4.6 Dos inferencias engañosas

La distinción entre implicación, recíproca e inversa permite detectar dos razonamientos que parecen plausibles, pero no están justificados por una implicación sola.

### Afirmar el consecuente

De

$$
P\to Q
$$

y

$$
Q
$$

no podemos concluir $P$ en general. Hacerlo equivaldría a sustituir la implicación por su recíproca.

### Negar el antecedente

De

$$
P\to Q
$$

y

$$
\neg P
$$

no podemos concluir $\neg Q$ en general. Hacerlo equivaldría a sustituir la implicación por su inversa.

### Ejemplo resuelto 30

Encuentra una asignación que muestre que el esquema

$$
P\to Q,\qquad Q,\qquad \therefore P
$$

puede fallar.

**Solución.** Tomemos

$$
P=F,\qquad Q=V.
$$

Entonces $P\to Q=V$ porque el antecedente es falso, y $Q$ también es verdadera. Sin embargo, $P$ es falsa. Por tanto, las dos premisas pueden ser verdaderas mientras la conclusión es falsa.

### Ejemplo resuelto 31

Encuentra una asignación que muestre que el esquema

$$
P\to Q,\qquad\neg P,\qquad\therefore\neg Q
$$

puede fallar.

**Solución.** De nuevo tomamos

$$
P=F,\qquad Q=V.
$$

Entonces $P\to Q$ es verdadera y $\neg P$ es verdadera, pero $\neg Q$ es falsa. Por consiguiente, negar el antecedente no permite negar el consecuente.

::: {.callout-tip title="Mirada hacia adelante"}
En la sección 1.6 definiremos formalmente qué significa que un argumento sea válido y analizaremos con tablas esquemas como el *modus ponens* y el *modus tollens*. Aquí solo hemos preparado el terreno distinguiendo correctamente las cuatro formas asociadas a una implicación.
:::

## 1.4.7 Problemas de práctica resueltos

### Problema de práctica 9

Calcula el valor de verdad de las siguientes implicaciones:

1. Si 8 es par, entonces 10 es par.
2. Si 8 es par, entonces 9 es par.
3. Si 9 es par, entonces 10 es par.
4. Si 9 es par, entonces 11 es par.

### Problema de práctica 10

Simplifica

$$
(P\land Q)\to R
$$

usando solo $\neg$, $\lor$ y las equivalencias ya estudiadas.

### Problema de práctica 11

Escribe la recíproca, la contrapositiva y la inversa de

$$
P\to(Q\land R).
$$

### Problema de práctica 12

Niega y simplifica

$$
P\to(Q\lor R).
$$

### Problema de práctica 13

Decide si

$$
(P\to Q)\land(P\to R)
$$

es equivalente a

$$
P\to(Q\land R).
$$

Justifica la respuesta mediante equivalencias, no mediante una tabla completa.

## Soluciones de los problemas de práctica

### Problema de práctica 9

1. Antecedente verdadero y consecuente verdadero: la implicación es verdadera.
2. Antecedente verdadero y consecuente falso: la implicación es falsa.
3. Antecedente falso y consecuente verdadero: la implicación es verdadera.
4. Antecedente falso y consecuente falso: la implicación es verdadera.

Las cuatro respuestas reproducen las cuatro filas de la tabla del condicional.

### Problema de práctica 10

$$
(P\land Q)\to R
\equiv
\neg(P\land Q)\lor R.
$$

Por De Morgan,

$$
\neg(P\land Q)\lor R
\equiv
(\neg P\lor\neg Q)\lor R.
$$

Por asociatividad,

$$
\boxed{\neg P\lor\neg Q\lor R.}
$$

### Problema de práctica 11

Para

$$
P\to(Q\land R),
$$

tenemos:

- recíproca: $(Q\land R)\to P$;
- contrapositiva: $\neg(Q\land R)\to\neg P$;
- inversa: $\neg P\to\neg(Q\land R)$.

Si se desea, las negaciones compuestas pueden transformarse después mediante De Morgan.

### Problema de práctica 12

$$
\neg\bigl(P\to(Q\lor R)\bigr)
\equiv
P\land\neg(Q\lor R).
$$

Por De Morgan,

$$
P\land\neg(Q\lor R)
\equiv
P\land\neg Q\land\neg R.
$$

Por tanto,

$$
\boxed{\neg\bigl(P\to(Q\lor R)\bigr)\equiv P\land\neg Q\land\neg R.}
$$

### Problema de práctica 13

Transformamos el lado izquierdo:

$$
(P\to Q)\land(P\to R)
\equiv
(\neg P\lor Q)\land(\neg P\lor R).
$$

Por distributividad,

$$
(\neg P\lor Q)\land(\neg P\lor R)
\equiv
\neg P\lor(Q\land R).
$$

Pero

$$
\neg P\lor(Q\land R)
\equiv
P\to(Q\land R).
$$

Por tanto,

$$
\boxed{(P\to Q)\land(P\to R)\equiv P\to(Q\land R).}
$$

# Ejercicios de la sección 1.4

1. Construye la tabla de verdad de $P\to Q$ a partir de la fórmula equivalente $\neg P\lor Q$.
2. Determina el valor de verdad de cada afirmación:
   a. Si 12 es par, entonces 3 es primo.
   b. Si 12 es par, entonces 9 es primo.
   c. Si 15 es par, entonces 3 es primo.
   d. Si 15 es par, entonces 9 es primo.
3. Sean $A$: «abre la biblioteca», $L$: «Leo estudia» y $M$: «Marta llama». Traduce:
   a. Si abre la biblioteca, entonces Leo estudia.
   b. Si Leo estudia y Marta no llama, entonces abre la biblioteca.
   c. Si no abre la biblioteca, entonces Marta llama o Leo estudia.
4. Verifica mediante una tabla que $P\to Q\equiv\neg P\lor Q$.
5. Demuestra mediante equivalencias que $P\to Q\equiv\neg(P\land\neg Q)$.
6. Niega correctamente, primero simbólicamente y luego en palabras: «Si el examen es mañana, entonces hoy estudio».
7. Para la afirmación «Si la puerta está abierta, entonces entra luz», escribe su recíproca, su contrapositiva y su inversa.
8. Verifica mediante una tabla que una implicación y su contrapositiva son equivalentes.
9. Encuentra una asignación que muestre que $P\to Q$ y $Q\to P$ no son equivalentes.
10. Clasifica como tautología, contradicción o contingencia: $P\to P$.
11. Simplifica $P\to\neg P$. Clasifica después la fórmula resultante.
12. Simplifica usando solo $\neg$, $\lor$ y $\land$: $(P\land Q)\to R$.
13. Simplifica $P\to(Q\lor R)$.
14. Decide si son equivalentes $P\to(Q\to R)$ y $(P\land Q)\to R$.
15. Reescribe $P\to Q$ usando únicamente $\neg$ y $\lor$.
16. **Encontrar el error.** Un estudiante afirma: «Si $P$ es falsa, entonces $P\to Q$ no tiene valor de verdad porque no sabemos qué habría pasado si $P$ hubiera sido verdadera». Explica el error desde la definición veritativo-funcional adoptada.
17. **Encontrar el error.** Otro estudiante afirma: «$P\to Q$ y $Q\to P$ son equivalentes porque ambas fórmulas contienen las mismas letras». Da una refutación mínima.
18. **Desafío.** Demuestra que la recíproca $Q\to P$ es equivalente a la inversa $\neg P\to\neg Q$ sin construir una tabla completa.

# Soluciones completas de los ejercicios de la sección 1.4

## 1

Partimos de $\neg P\lor Q$:

| $P$ | $Q$ | $\neg P$ | $\neg P\lor Q$ |
|---|---|---|---|
| V | V | F | V |
| V | F | F | F |
| F | V | V | V |
| F | F | V | V |

Como $P\to Q\equiv\neg P\lor Q$, la última columna es precisamente la tabla del condicional.

## 2

1. 12 es par y 3 es primo: $V\to V=V$.
2. 12 es par y 9 no es primo: $V\to F=F$.
3. 15 no es par y 3 es primo: $F\to V=V$.
4. 15 no es par y 9 no es primo: $F\to F=V$.

## 3

1. $A\to L$.
2. $(L\land\neg M)\to A$.
3. $\neg A\to(M\lor L)$.

## 4

| $P$ | $Q$ | $P\to Q$ | $\neg P\lor Q$ |
|---|---|---|---|
| V | V | V | V |
| V | F | F | F |
| F | V | V | V |
| F | F | V | V |

Las columnas finales son idénticas.

## 5

$$
P\to Q
\equiv
\neg P\lor Q
\equiv
\neg P\lor\neg\neg Q
\equiv
\neg(P\land\neg Q).
$$

La última equivalencia es De Morgan leída de derecha a izquierda.

## 6

Sea $P$: «el examen es mañana» y $Q$: «hoy estudio». La frase es $P\to Q$. Su negación es

$$
P\land\neg Q.
$$

En palabras:

> «El examen es mañana y hoy no estudio».

## 7

Sea $P$: «la puerta está abierta» y $Q$: «entra luz».

- recíproca: $Q\to P$, «Si entra luz, entonces la puerta está abierta»;
- contrapositiva: $\neg Q\to\neg P$, «Si no entra luz, entonces la puerta no está abierta»;
- inversa: $\neg P\to\neg Q$, «Si la puerta no está abierta, entonces no entra luz».

## 8

| $P$ | $Q$ | $P\to Q$ | $\neg Q\to\neg P$ |
|---|---|---|---|
| V | V | V | V |
| V | F | F | F |
| F | V | V | V |
| F | F | V | V |

Luego

$$
\boxed{P\to Q\equiv\neg Q\to\neg P.}
$$

## 9

Tomemos $P=V$ y $Q=F$. Entonces

$$
P\to Q=F,
$$

mientras que

$$
Q\to P=V.
$$

Una sola asignación distinta basta para probar que no son equivalentes.

## 10

$$
P\to P\equiv\neg P\lor P.
$$

Esta es la ley del tercero excluido, verdadera en toda asignación clásica. Por tanto,

$$
\boxed{P\to P\text{ es una tautología}.}
$$

## 11

$$
P\to\neg P
\equiv
\neg P\lor\neg P
\equiv
\neg P.
$$

La fórmula es verdadera cuando $P$ es falsa y falsa cuando $P$ es verdadera. Por tanto es **contingente**.

## 12

$$
(P\land Q)\to R
\equiv
\neg(P\land Q)\lor R
\equiv
\neg P\lor\neg Q\lor R.
$$

## 13

$$
P\to(Q\lor R)
\equiv
\neg P\lor(Q\lor R)
\equiv
\neg P\lor Q\lor R.
$$

## 14

Por la ley condicional,

$$
P\to(Q\to R)
\equiv
\neg P\lor(\neg Q\lor R)
\equiv
\neg P\lor\neg Q\lor R.
$$

Por otra parte,

$$
(P\land Q)\to R
\equiv
\neg(P\land Q)\lor R
\equiv
\neg P\lor\neg Q\lor R.
$$

Ambas se reducen a la misma fórmula, de modo que

$$
\boxed{P\to(Q\to R)\equiv(P\land Q)\to R.}
$$

## 15

La equivalencia pedida es directamente

$$
\boxed{P\to Q\equiv\neg P\lor Q.}
$$

## 16

En la lógica proposicional clásica que estamos usando, cada conectiva se define por una tabla de verdad. La tabla de $\to$ asigna un valor también cuando el antecedente es falso. En esas dos filas, $P\to Q$ es verdadera. La pregunta contrafáctica «qué habría pasado» no forma parte de la definición de esta conectiva.

## 17

Basta tomar

$$
P=V,\qquad Q=F.
$$

Entonces $P\to Q$ es falsa y $Q\to P$ es verdadera. Tener las mismas letras no implica tener la misma forma lógica ni la misma tabla de verdad.

## 18

La inversa de $P\to Q$ es

$$
\neg P\to\neg Q.
$$

Aplicamos la ley de la contrapositiva a la recíproca $Q\to P$:

$$
Q\to P\equiv\neg P\to\neg Q.
$$

Por tanto,

$$
\boxed{Q\to P\equiv\neg P\to\neg Q.}
$$

::: {.callout-note title="Registro de dependencias"}
Esta sección introduce y deja disponibles:

- la implicación $\to$;
- antecedente y consecuente;
- las leyes condicionales $P\to Q\equiv\neg P\lor Q$ y $P\to Q\equiv\neg(P\land\neg Q)$;
- la negación de una implicación;
- recíproca, contrapositiva e inversa;
- la equivalencia entre una implicación y su contrapositiva;
- los esquemas no válidos de afirmar el consecuente y negar el antecedente.

El bicondicional y las expresiones «condición necesaria» y «condición suficiente» quedan reservados para la sección 1.5.
:::

---

**Secciones anteriores:** [Capítulo 1 — 1.1 a 1.3](topos-desde-cero-capitulo-1-proposiciones-y-razonamiento-deductivo.md).

**Siguiente sección:** 1.5 — Bicondicionales y condiciones necesarias y suficientes.
