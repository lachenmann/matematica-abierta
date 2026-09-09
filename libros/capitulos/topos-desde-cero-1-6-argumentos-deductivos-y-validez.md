---
title: "Topos desde cero — 1.6 Argumentos deductivos y validez"
description: "Unidad del capítulo 1 de Topos desde cero: premisas, conclusión, validez, tablas de verdad, asignaciones refutadoras y reglas elementales de inferencia."
content-id: MA-LES-0003
content-type: lesson
status: published
date-created: 2026-09-09
date-modified: 2026-09-09
areas:
  - fundamentos
level: fundamental
topics:
  - logica-matematica
  - argumentos-deductivos
  - premisas
  - conclusion
  - validez
  - asignaciones-refutadoras
  - tablas-de-verdad
  - reglas-de-inferencia
  - modus-ponens
  - modus-tollens
  - silogismo-disyuntivo
  - silogismo-hipotetico
  - falacias
prerequisites: []
related:
  - MA-BCH-0002
  - MA-BOK-0002
  - MA-LES-0001
  - MA-LES-0002
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# 1.6 Argumentos deductivos y validez {#sec-1-6-argumentos-validez}

::: {.callout-note title="Continuidad editorial"}
Esta unidad continúa el **Capítulo 1 — Proposiciones y razonamiento deductivo** de *Topos desde cero* (`MA-BCH-0002`). Las secciones 1.4 y 1.5 se publican también como unidades modulares inmediatamente anteriores.
:::

::: {.callout-note title="Resultados de aprendizaje"}
Al terminar esta sección, el lector podrá:

- distinguir las premisas de la conclusión de un argumento;
- separar el contenido de un argumento de su forma lógica;
- definir con precisión qué significa que un argumento sea válido;
- comprobar la validez mediante tablas de verdad;
- refutar la validez encontrando una asignación en la que todas las premisas sean verdaderas y la conclusión falsa;
- relacionar la validez de un argumento con una tautología condicional;
- reconocer y aplicar *modus ponens* y *modus tollens*;
- reconocer otros esquemas elementales de inferencia válidos;
- detectar las falacias de afirmar el consecuente y negar el antecedente;
- encadenar varias inferencias válidas en un argumento más largo.
:::

::: {.callout-warning title="Motivación"}
Ya conocemos las cinco conectivas proposicionales básicas y sabemos analizar fórmulas mediante tablas de verdad. Falta convertir estas herramientas en lo que realmente necesitamos para hacer matemáticas: razonar desde ciertas afirmaciones hasta otra afirmación.

Un argumento deductivo no promete que sus premisas sean verdaderas. Lo que pretende es algo diferente: que, **si las premisas fueran todas verdaderas, la conclusión no podría resultar falsa**.

Esta distinción es fundamental. Una conclusión verdadera puede haberse obtenido mediante un razonamiento defectuoso; una forma de razonamiento puede ser perfectamente válida aunque se aplique a premisas falsas. La validez pertenece a la conexión lógica entre premisas y conclusión.
:::

## 1.6.1 Premisas, conclusión y forma lógica

::: {.callout-important title="Definición"}
Un **argumento deductivo** consta de una o más proposiciones llamadas **premisas** y de una proposición llamada **conclusión**.

Escribiremos, por ejemplo,

$$
P\to Q,\qquad P,\qquad \therefore Q,
$$

donde el símbolo $\therefore$ se lee «por tanto» o «por consiguiente».
:::

Consideremos:

> Si hoy es lunes, entonces hay clase.  
> Hoy es lunes.  
> Por tanto, hay clase.

Si

$$
L:\quad \text{«hoy es lunes»}
$$

y

$$
C:\quad \text{«hay clase»},
$$

la forma del argumento es

$$
L\to C,\qquad L,\qquad \therefore C.
$$

El contenido concreto ha desaparecido. Lo que queda es el patrón lógico

$$
P\to Q,\qquad P,\qquad \therefore Q.
$$

Varios argumentos de asuntos completamente distintos pueden compartir esta misma forma.

### Ejemplo resuelto 45

Determina las premisas, la conclusión y la forma lógica del argumento:

> Si el número es divisible por 4, entonces es par.  
> El número es divisible por 4.  
> Por tanto, el número es par.

**Solución.** Definimos

$$
D:\quad \text{«el número es divisible por 4»},
$$

$$
E:\quad \text{«el número es par»}.
$$

Las premisas son

$$
D\to E
$$

y

$$
D,
$$

y la conclusión es

$$
E.
$$

La forma lógica es

$$
P\to Q,\qquad P,\qquad \therefore Q.
$$

### Ejemplo resuelto 46

Compara los argumentos:

> Si llueve, la calle se moja. Llueve. Por tanto, la calle se moja.

 y

> Si 12 es divisible por 4, entonces 12 es par. 12 es divisible por 4. Por tanto, 12 es par.

**Solución.** Los contenidos son distintos, pero ambos tienen la forma

$$
P\to Q,\qquad P,\qquad \therefore Q.
$$

Por ello, cualquier análisis de la validez de esa forma sirve simultáneamente para ambos argumentos. Esta es una de las razones por las que sustituimos proposiciones concretas por letras: nos permite estudiar la estructura del razonamiento independientemente del tema.

## 1.6.2 Qué significa que un argumento sea válido

::: {.callout-important title="Definición"}
Un argumento es **válido** si no existe ninguna asignación de valores de verdad en la que todas sus premisas sean verdaderas y su conclusión sea falsa.

Equivalentemente: siempre que todas las premisas sean verdaderas, la conclusión también debe ser verdadera.
:::

La definición no dice:

- que las premisas sean realmente verdaderas;
- que la conclusión sea realmente verdadera;
- que un argumento sea válido porque su conclusión resulte verdadera.

Solo exige preservar la verdad desde las premisas hasta la conclusión.

::: {.callout-warning title="Atención"}
Para demostrar que un argumento es inválido basta encontrar una sola asignación con este patrón:

$$
\boxed{\text{todas las premisas: V},\qquad \text{conclusión: F}.}
$$

Esa asignación funciona como contraejemplo a la validez.
:::

### Ejemplo resuelto 47

¿Puede un argumento tener una conclusión verdadera y ser inválido?

Consideremos

$$
P,\qquad Q,\qquad \therefore R.
$$

Tomemos el contenido concreto:

> 2 es par.  
> 4 es par.  
> Por tanto, 6 es par.

**Solución.** Las tres proposiciones concretas son verdaderas. Sin embargo, la forma

$$
P,\qquad Q,\qquad \therefore R
$$

es inválida: podemos asignar

$$
P=V,\qquad Q=V,\qquad R=F.
$$

Las premisas son verdaderas y la conclusión falsa.

Por consiguiente, que una conclusión sea verdadera no demuestra que haya sido deducida válidamente. En el ejemplo concreto, la verdad de «6 es par» no depende lógicamente de las dos premisas dadas.

### Ejemplo resuelto 48

¿Puede una forma de argumento ser válida aunque alguna de sus proposiciones concretas sea falsa?

Consideremos

$$
P\to Q,\qquad P,\qquad \therefore Q.
$$

Sustituyamos

$$
P:\quad 2=3,
$$

$$
Q:\quad 5=7.
$$

**Solución.** El argumento concreto contiene proposiciones falsas. Esto no afecta a la validez de la forma. Para que el esquema fuese inválido necesitaríamos una asignación en la que

$$
P\to Q=V,\qquad P=V,\qquad Q=F.
$$

Pero, cuando

$$
P=V,\qquad Q=F,
$$

la implicación $P\to Q$ es falsa. Por tanto, no existe una fila con todas las premisas verdaderas y la conclusión falsa.

La forma es válida aunque esta sustitución concreta no nos proporcione premisas verdaderas.

## 1.6.3 Comprobar la validez con una tabla de verdad

El procedimiento es sistemático:

1. identificamos las letras proposicionales;
2. construimos todas las filas posibles;
3. calculamos una columna para cada premisa y otra para la conclusión;
4. buscamos únicamente las filas en las que todas las premisas son verdaderas;
5. comprobamos la conclusión en esas filas.

Si en todas ellas la conclusión es verdadera, el argumento es válido. Si aparece una sola fila con premisas verdaderas y conclusión falsa, el argumento es inválido.

### Ejemplo resuelto 49

Comprueba mediante una tabla la validez de

$$
P\to Q,\qquad P,\qquad \therefore Q.
$$

**Solución.**

| $P$ | $Q$ | $P\to Q$ | $P$ | $Q$ |
|---|---|---|---|---|
| V | V | V | V | V |
| V | F | F | V | F |
| F | V | V | F | V |
| F | F | V | F | F |

La única fila en la que las dos premisas son verdaderas es la primera, y allí la conclusión también es verdadera. Por tanto,

$$
P\to Q,\qquad P,\qquad \therefore Q
$$

es válido.

Esta regla recibe el nombre de **modus ponens**.

### Ejemplo resuelto 50

Comprueba mediante una tabla si

$$
P\to Q,\qquad Q,\qquad \therefore P
$$

es válido.

**Solución.**

| $P$ | $Q$ | $P\to Q$ | $Q$ | $P$ |
|---|---|---|---|---|
| V | V | V | V | V |
| V | F | F | F | V |
| F | V | V | V | F |
| F | F | V | F | F |

La tercera fila es decisiva:

$$
P=F,\qquad Q=V.
$$

En ella,

$$
P\to Q=V
$$

y

$$
Q=V,
$$

pero la conclusión $P$ es falsa. Por tanto,

$$
P\to Q,\qquad Q,\qquad \therefore P
$$

es inválido.

Es la falacia de **afirmar el consecuente**.

### Ejemplo resuelto 51

Determina si

$$
P\lor Q,\qquad \neg Q,\qquad \therefore P
$$

es válido.

**Solución.**

| $P$ | $Q$ | $P\lor Q$ | $\neg Q$ | $P$ |
|---|---|---|---|---|
| V | V | V | F | V |
| V | F | V | V | V |
| F | V | V | F | F |
| F | F | F | V | F |

Solo en la segunda fila ambas premisas son verdaderas, y allí $P$ es verdadera. Por tanto,

$$
P\lor Q,\qquad \neg Q,\qquad \therefore P
$$

es válido.

Esta forma se conoce como **silogismo disyuntivo**.

## 1.6.4 Validez y tautologías

Hay una segunda forma de estudiar un argumento. Supongamos que sus premisas son

$$
A_1,A_2,\ldots,A_n
$$

y que su conclusión es $C$. Formamos una sola proposición:

$$
(A_1\land A_2\land\cdots\land A_n)\to C.
$$

::: {.callout-important title="Definición y criterio"}
El argumento

$$
A_1,A_2,\ldots,A_n,\qquad \therefore C
$$

es válido exactamente cuando

$$
(A_1\land A_2\land\cdots\land A_n)\to C
$$

es una tautología.
:::

La razón procede directamente de las definiciones. La implicación anterior solo podría ser falsa en una fila donde su antecedente fuese verdadero y su consecuente falso. Pero el antecedente es verdadero exactamente cuando todas las premisas son verdaderas. Así, una fila que hace falsa la implicación es precisamente una fila que refuta la validez del argumento.

### Ejemplo resuelto 52

Usa el criterio de tautología para justificar el *modus ponens*.

**Solución.** El argumento

$$
P\to Q,\qquad P,\qquad \therefore Q
$$

corresponde a la fórmula

$$
\bigl((P\to Q)\land P\bigr)\to Q.
$$

Si el antecedente de esta fórmula es verdadero, entonces $P\to Q$ y $P$ son ambos verdaderos. Como ya sabemos por la tabla del condicional, esto obliga a que $Q$ sea verdadero. Por tanto, la implicación completa nunca puede ser falsa:

$$
\boxed{\bigl((P\to Q)\land P\bigr)\to Q}
$$

es una tautología. Luego el argumento es válido.

## 1.6.5 Reglas elementales de inferencia

Una forma de argumento que sabemos válida puede utilizarse como una **regla de inferencia**: cada vez que aparezcan premisas con esa forma, estamos autorizados a obtener la conclusión correspondiente.

### Modus ponens

$$
P\to Q,\qquad P,\qquad \therefore Q.
$$

### Modus tollens

$$
P\to Q,\qquad \neg Q,\qquad \therefore \neg P.
$$

### Silogismo disyuntivo

$$
P\lor Q,\qquad \neg Q,\qquad \therefore P.
$$

### Silogismo hipotético

$$
P\to Q,\qquad Q\to R,\qquad \therefore P\to R.
$$

Estas formas pueden verificarse mediante tablas de verdad. Más adelante, cuando escribamos demostraciones, las utilizaremos sin reconstruir la tabla cada vez, del mismo modo que usamos una identidad algebraica ya demostrada.

### Ejemplo resuelto 53

Verifica conceptualmente el *modus tollens*:

$$
P\to Q,\qquad \neg Q,\qquad \therefore \neg P.
$$

**Solución.** Supongamos que ambas premisas son verdaderas. La segunda dice que

$$
Q=F.
$$

Si además $P$ fuese verdadera, entonces $P\to Q$ tendría la combinación

$$
V\to F,
$$

que hace falsa la primera premisa. Esto contradice que ambas premisas sean verdaderas. Por tanto $P$ no puede ser verdadera:

$$
P=F,
$$

y así

$$
\neg P=V.
$$

Luego el argumento es válido.

### Ejemplo resuelto 54

Comprueba el silogismo hipotético:

$$
P\to Q,\qquad Q\to R,\qquad \therefore P\to R.
$$

**Solución.** Queremos saber si es posible que las dos premisas sean verdaderas y la conclusión falsa.

Para que

$$
P\to R
$$

sea falsa, debe ocurrir

$$
P=V,\qquad R=F.
$$

Como $P=V$ y la primera premisa $P\to Q$ es verdadera, necesariamente

$$
Q=V.
$$

Pero entonces, con

$$
Q=V,\qquad R=F,
$$

la segunda premisa $Q\to R$ sería falsa. Por tanto, no existe una asignación con ambas premisas verdaderas y conclusión falsa. El argumento es válido.

### Ejemplo resuelto 55

Analiza

$$
P\leftrightarrow Q,\qquad P,\qquad \therefore Q.
$$

**Solución.** Por definición,

$$
P\leftrightarrow Q\equiv(P\to Q)\land(Q\to P).
$$

Si la primera premisa es verdadera, entonces en particular $P\to Q$ es verdadera. La segunda premisa nos da $P$. Aplicando *modus ponens*, obtenemos

$$
Q.
$$

Luego el argumento es válido.

Obsérvese que no necesitamos una tabla nueva: hemos descompuesto el bicondicional en las dos implicaciones que ya conocemos.

## 1.6.6 Dos formas inválidas que deben evitarse

Las secciones anteriores ya anticiparon dos errores frecuentes.

### Afirmar el consecuente

$$
P\to Q,\qquad Q,\qquad \therefore P.
$$

### Negar el antecedente

$$
P\to Q,\qquad \neg P,\qquad \therefore \neg Q.
$$

Ambos confunden una implicación con otra dirección que no está garantizada.

### Ejemplo resuelto 56

Explica por qué es inválido:

> Si una figura es un cuadrado, entonces tiene cuatro lados.  
> La figura tiene cuatro lados.  
> Por tanto, la figura es un cuadrado.

**Solución.** Sea

$$
C:\quad \text{«la figura es un cuadrado»},
$$

$$
L:\quad \text{«la figura tiene cuatro lados»}.
$$

La forma es

$$
C\to L,\qquad L,\qquad \therefore C,
$$

que afirma el consecuente.

Un rectángulo que no sea cuadrado proporciona intuitivamente el contraejemplo:

$$
C=F,\qquad L=V.
$$

Entonces $C\to L$ es verdadera y $L$ es verdadera, pero $C$ es falsa. Por tanto, el argumento es inválido.

## 1.6.7 Encadenar inferencias

Los argumentos matemáticos reales rara vez constan de una sola aplicación de una regla. Normalmente obtenemos una conclusión intermedia y la utilizamos como nueva información.

### Ejemplo resuelto 57

Demuestra que el siguiente argumento es válido:

$$
P\to Q,\qquad Q\to R,\qquad P,\qquad \therefore R.
$$

**Solución.** De

$$
P\to Q
$$

y

$$
P
$$

obtenemos por *modus ponens*

$$
Q.
$$

Ahora disponemos de

$$
Q\to R
$$

y

$$
Q,
$$

por lo que una segunda aplicación de *modus ponens* da

$$
R.
$$

Así, la conclusión se obtiene mediante dos pasos válidos.

### Ejemplo resuelto 58

Analiza el argumento

$$
P\lor Q,\qquad P\to R,\qquad Q\to R,\qquad \therefore R.
$$

**Solución.** La primera premisa asegura que al menos una de $P,Q$ es verdadera.

Si $P$ es verdadera, entonces $P\to R$ y *modus ponens* obligan a $R$.

Si $Q$ es verdadera, entonces $Q\to R$ y *modus ponens* obligan igualmente a $R$.

En cualquiera de las posibilidades permitidas por $P\lor Q$, obtenemos $R$. Por tanto, el argumento es válido.

También puede verificarse con una tabla de verdad de ocho filas.

::: {.callout-tip title="Mirada hacia adelante"}
Hasta aquí hemos estudiado argumentos cuyas proposiciones están tratadas como unidades completas. En el capítulo siguiente abriremos esas unidades e introduciremos variables y cuantificadores. Entonces podremos analizar afirmaciones como «todo elemento con cierta propiedad cumple otra» y «existe un objeto con tal característica».

Las reglas de validez de este capítulo seguirán funcionando, pero aplicadas a una estructura lógica mucho más rica.
:::

## 1.6.8 Problemas de práctica resueltos

### Problema de práctica 19

Decide mediante una tabla si

$$
P\to Q,\qquad \neg Q,\qquad \therefore \neg P
$$

es válido.

### Problema de práctica 20

Encuentra una asignación que refute

$$
P\to Q,\qquad \neg P,\qquad \therefore \neg Q.
$$

### Problema de práctica 21

Determina si es válido:

$$
P\lor Q,\qquad \neg P,\qquad \therefore Q.
$$

### Problema de práctica 22

Justifica sin tabla completa:

$$
P\to Q,\qquad Q\to R,\qquad \neg R,\qquad \therefore \neg P.
$$

### Problema de práctica 23

Determina si es válido:

$$
P\leftrightarrow Q,\qquad \neg P,\qquad \therefore \neg Q.
$$

## Soluciones de los problemas de práctica

### Problema de práctica 19

| $P$ | $Q$ | $P\to Q$ | $\neg Q$ | $\neg P$ |
|---|---|---|---|---|
| V | V | V | F | F |
| V | F | F | V | F |
| F | V | V | F | V |
| F | F | V | V | V |

La única fila en la que ambas premisas son verdaderas es la cuarta, y allí la conclusión también lo es. Por tanto, el argumento es válido: es *modus tollens*.

### Problema de práctica 20

Tomemos

$$
P=F,\qquad Q=V.
$$

Entonces

$$
P\to Q=V,\qquad \neg P=V,
$$

pero

$$
\neg Q=F.
$$

Las premisas son verdaderas y la conclusión falsa. Por tanto, el argumento es inválido.

### Problema de práctica 21

Si las premisas

$$
P\lor Q
$$

y

$$
\neg P
$$

son verdaderas, entonces $P$ es falsa. Para que $P\lor Q$ siga siendo verdadera debe ser

$$
Q=V.
$$

Por tanto,

$$
P\lor Q,\qquad \neg P,\qquad \therefore Q
$$

es válido.

### Problema de práctica 22

De

$$
Q\to R
$$

y

$$
\neg R
$$

obtenemos por *modus tollens*

$$
\neg Q.
$$

Luego, de

$$
P\to Q
$$

y

$$
\neg Q
$$

obtenemos nuevamente por *modus tollens*

$$
\neg P.
$$

El argumento es válido.

### Problema de práctica 23

Si

$$
P\leftrightarrow Q
$$

es verdadero, entonces también es verdadera la dirección

$$
Q\to P.
$$

Junto con

$$
\neg P,
$$

el *modus tollens* aplicado a $Q\to P$ produce

$$
\neg Q.
$$

Por tanto, el argumento es válido.

# Ejercicios de la sección 1.6

1. Identifica premisas y conclusión:

   > Si el archivo compila, entonces no contiene ese error de sintaxis. El archivo compila. Por tanto, no contiene ese error de sintaxis.

2. Escribe la forma lógica del argumento anterior usando $C$ y $E$.
3. Construye una tabla para comprobar

   $$
   P\to Q,\qquad P,\qquad \therefore Q.
   $$

4. Construye una tabla para comprobar

   $$
   P\to Q,\qquad \neg Q,\qquad \therefore \neg P.
   $$

5. Encuentra una asignación que demuestre la invalidez de

   $$
   P\to Q,\qquad Q,\qquad \therefore P.
   $$

6. Encuentra una asignación que demuestre la invalidez de

   $$
   P\to Q,\qquad \neg P,\qquad \therefore \neg Q.
   $$

7. Decide si es válido:

   $$
   P\lor Q,\qquad \neg P,\qquad \therefore Q.
   $$

8. Decide si es válido:

   $$
   P\land Q,\qquad \therefore P.
   $$

9. Decide si es válido:

   $$
   P,\qquad \therefore P\lor Q.
   $$

10. Decide si es válido:

    $$
    P\to Q,\qquad Q\to R,\qquad \therefore P\to R.
    $$

11. Decide si es válido:

    $$
    P\to Q,\qquad R\to Q,\qquad Q,\qquad \therefore P\lor R.
    $$

12. Usa el criterio de tautología para expresar la validez de

    $$
    P\lor Q,\qquad \neg Q,\qquad \therefore P
    $$

    como una sola fórmula.

13. Demuestra que, si el argumento

    $$
    A,\qquad B,\qquad \therefore C
    $$

    es válido, entonces

    $$
    (A\land B)\to C
    $$

    es una tautología.

14. **Encontrar el error.** Un estudiante dice: «La conclusión es verdadera, así que el argumento es válido». Explica el error.
15. **Encontrar el error.** Otro estudiante dice: «Una premisa es falsa, así que el argumento es inválido». Explica el error.
16. Analiza:

    $$
    P\leftrightarrow Q,\qquad P,\qquad \therefore Q.
    $$

17. Analiza:

    $$
    P\leftrightarrow Q,\qquad \neg P,\qquad \therefore \neg Q.
    $$

18. Demuestra por una cadena de inferencias:

    $$
    P\to Q,\qquad Q\to R,\qquad R\to S,\qquad P,\qquad \therefore S.
    $$

19. Determina si es válido:

    $$
    P\lor Q,\qquad P\to R,\qquad Q\to R,\qquad \therefore R.
    $$

20. **Desafío integrador.** Determina si

    $$
    (P\to Q)\land(R\to S),\qquad P\lor R,\qquad \neg Q,\qquad \therefore S
    $$

    es válido. Justifica tu respuesta mediante inferencias o mediante una asignación refutadora.

# Soluciones completas de los ejercicios de la sección 1.6

## 1

Las premisas son:

> «Si el archivo compila, entonces no contiene ese error de sintaxis»

 y

> «El archivo compila».

La conclusión es:

> «El archivo no contiene ese error de sintaxis».

## 2

Sea

$$
C:\quad \text{«el archivo compila»},
$$

$$
E:\quad \text{«el archivo contiene ese error de sintaxis»}.
$$

La forma es

$$
C\to\neg E,\qquad C,\qquad \therefore\neg E.
$$

## 3

| $P$ | $Q$ | $P\to Q$ | $P$ | $Q$ |
|---|---|---|---|---|
| V | V | V | V | V |
| V | F | F | V | F |
| F | V | V | F | V |
| F | F | V | F | F |

La única fila con ambas premisas verdaderas es la primera, donde $Q$ es verdadera. El argumento es válido.

## 4

| $P$ | $Q$ | $P\to Q$ | $\neg Q$ | $\neg P$ |
|---|---|---|---|---|
| V | V | V | F | F |
| V | F | F | V | F |
| F | V | V | F | V |
| F | F | V | V | V |

Solo la última fila hace verdaderas ambas premisas, y allí $\neg P$ es verdadera. El argumento es válido.

## 5

Tomemos

$$
P=F,\qquad Q=V.
$$

Entonces $P\to Q$ y $Q$ son verdaderas, mientras que $P$ es falsa. El argumento es inválido.

## 6

Tomemos nuevamente

$$
P=F,\qquad Q=V.
$$

Entonces

$$
P\to Q=V,\qquad \neg P=V,\qquad \neg Q=F.
$$

Por tanto, el argumento es inválido.

## 7

Es válido. Si $\neg P$ es verdadera, entonces $P$ es falsa. Para que la otra premisa $P\lor Q$ sea verdadera debe ser $Q$ verdadera. Luego la conclusión está forzada.

## 8

Es válido. Si

$$
P\land Q
$$

es verdadera, entonces, por la definición de conjunción, $P$ es verdadera. No existe una fila en la que la premisa sea verdadera y la conclusión falsa.

## 9

Es válido. Si $P$ es verdadera, entonces

$$
P\lor Q
$$

es verdadera independientemente del valor de $Q$.

## 10

Es válido. Si $P$ es falsa, la conclusión $P\to R$ ya es verdadera. Si $P$ es verdadera, la primera premisa obliga a $Q$ y la segunda obliga a $R$; entonces $P\to R$ también es verdadera. Equivalentemente, es el silogismo hipotético.

## 11

Es inválido. Tomemos

$$
P=F,\qquad R=F,\qquad Q=V.
$$

Entonces

$$
P\to Q=V,\qquad R\to Q=V,\qquad Q=V,
$$

pero

$$
P\lor R=F.
$$

Tenemos todas las premisas verdaderas y la conclusión falsa.

## 12

La conjunción de las premisas es

$$
(P\lor Q)\land\neg Q.
$$

Por tanto, el argumento es válido exactamente cuando

$$
\boxed{\bigl((P\lor Q)\land\neg Q\bigr)\to P}
$$

es una tautología. Lo es, porque si el antecedente es verdadero, $Q$ es falsa y $P\lor Q$ verdadera, lo que obliga a $P$.

## 13

Si el argumento es válido, no existe una asignación en la que $A$ y $B$ sean verdaderas y $C$ falsa. Pero

$$
(A\land B)\to C
$$

solo podría ser falsa precisamente en una asignación con

$$
A=V,\qquad B=V,\qquad C=F.
$$

Como tal asignación no existe, la fórmula es verdadera en todas las filas; por tanto, es una tautología.

## 14

La validez no consiste en que la conclusión sea verdadera de hecho. Exige que no sea posible mantener verdaderas todas las premisas y hacer falsa la conclusión. Una conclusión puede ser verdadera por razones completamente ajenas a las premisas.

## 15

Una premisa falsa en la situación concreta no hace inválida la forma del argumento. La validez pregunta qué ocurriría en todas las asignaciones en las que las premisas fuesen verdaderas. Para refutar la validez debemos encontrar una asignación con todas las premisas verdaderas y conclusión falsa.

## 16

De

$$
P\leftrightarrow Q
$$

obtenemos

$$
P\to Q.
$$

Con la segunda premisa $P$, el *modus ponens* produce

$$
Q.
$$

El argumento es válido.

## 17

De

$$
P\leftrightarrow Q
$$

obtenemos la dirección

$$
Q\to P.
$$

Con $\neg P$, el *modus tollens* produce

$$
\neg Q.
$$

El argumento es válido.

## 18

Aplicamos *modus ponens* sucesivamente:

$$
P,\ P\to Q\quad\Longrightarrow\quad Q,
$$

$$
Q,\ Q\to R\quad\Longrightarrow\quad R,
$$

$$
R,\ R\to S\quad\Longrightarrow\quad S.
$$

Por tanto, la conclusión $S$ se obtiene mediante una cadena de inferencias válidas.

## 19

Es válido. Si $P\lor Q$ es verdadera, al menos una de las dos posibilidades ocurre. Si ocurre $P$, entonces $P\to R$ da $R$; si ocurre $Q$, entonces $Q\to R$ da igualmente $R$. En ambos casos la conclusión es verdadera.

## 20

De la primera premisa

$$
(P\to Q)\land(R\to S)
$$

obtenemos por separado

$$
P\to Q
$$

y

$$
R\to S.
$$

Con

$$
P\to Q
$$

y

$$
\neg Q,
$$

el *modus tollens* produce

$$
\neg P.
$$

La segunda premisa es

$$
P\lor R.
$$

Junto con $\neg P$, el silogismo disyuntivo produce

$$
R.
$$

Finalmente, de

$$
R
$$

y

$$
R\to S
$$

obtenemos por *modus ponens*

$$
S.
$$

Por tanto, el argumento es válido.

# Cierre del capítulo 1

El capítulo comenzó distinguiendo proposiciones de otras expresiones y terminó estudiando cadenas completas de inferencia. El recorrido lógico ha sido:

$$
\boxed{
\text{proposiciones}
\longrightarrow
\text{conectivas}
\longrightarrow
\text{tablas de verdad}
\longrightarrow
\text{equivalencia}
\longrightarrow
\text{implicación}
\longrightarrow
\text{bicondicional}
\longrightarrow
\text{validez deductiva}
}
$$

A partir de este punto podemos leer una proposición compuesta, reconstruir su forma lógica, calcular sus condiciones de verdad y determinar si una conclusión se sigue válidamente de ciertas premisas.

::: {.callout-note title="Registro de dependencias"}
Esta sección introduce:

- premisa;
- conclusión;
- argumento deductivo;
- validez;
- asignación refutadora;
- regla de inferencia.

Se verifican y utilizan *modus ponens*, *modus tollens*, el silogismo disyuntivo y el silogismo hipotético, y se formalizan las falacias de afirmar el consecuente y negar el antecedente.

Con esto queda cerrado el lenguaje proposicional básico del capítulo 1. El capítulo 2 podrá introducir variables, predicados y cuantificadores sin presuponer ninguna conectiva ni noción de validez que no haya sido desarrollada previamente.
:::

---

**Siguiente sección:** 1.7 — Repaso acumulativo del capítulo 1.
