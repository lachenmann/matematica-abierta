---
title: "Topos desde cero — 1.7 Repaso acumulativo del capítulo 1"
description: "Repaso acumulativo del capítulo 1 de Topos desde cero: sintaxis, semántica, equivalencias, traducción, implicaciones, bicondicionales y validez deductiva."
content-id: MA-LES-0004
content-type: lesson
status: published
date-created: 2026-09-09
date-modified: 2026-09-09
areas:
  - fundamentos
level: fundamental
topics:
  - logica-matematica
  - logica-proposicional
  - repaso-acumulativo
  - sintaxis-logica
  - semantica-logica
  - valuaciones
  - tablas-de-verdad
  - equivalencia-logica
  - implicacion
  - bicondicional
  - validez
  - reglas-de-inferencia
prerequisites: []
related:
  - MA-BCH-0002
  - MA-BOK-0002
  - MA-LES-0001
  - MA-LES-0002
  - MA-LES-0003
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# 1.7 Repaso acumulativo del capítulo 1 {#sec-1-7-repaso}

::: {.callout-note title="Continuidad editorial"}
Esta unidad cierra el **Capítulo 1 — Proposiciones y razonamiento deductivo** de *Topos desde cero* (`MA-BCH-0002`). No introduce nociones nuevas: recupera e intercala los contenidos de §§1.1–1.6 para comprobar que pueden utilizarse sin que el enunciado anuncie de antemano qué técnica corresponde.
:::

::: {.callout-note title="Resultados de aprendizaje"}
Al terminar este repaso, el lector podrá:

- recuperar sin apoyo inmediato las nociones centrales del lenguaje proposicional;
- elegir una estrategia adecuada sin que el enunciado anuncie de antemano qué técnica utilizar;
- combinar análisis sintáctico, valuaciones, equivalencias y reglas de inferencia;
- traducir con precisión entre lenguaje natural y fórmulas proposicionales;
- distinguir validez de verdad material de las premisas y de la conclusión;
- detectar errores típicos en implicaciones, bicondicionales y argumentos;
- justificar cada transformación o inferencia mediante una regla ya introducida.
:::

::: {.callout-warning title="Motivación"}
Las secciones anteriores aislaron las piezas del lenguaje proposicional. Pero una demostración real rara vez anuncia:

> «Ahora debes usar una tabla de verdad»,

ni:

> «Ahora debes aplicar *modus tollens*».

El objetivo de este repaso es retirar esas señales. Los problemas mezclan contenidos de §§1.1–1.6 y obligan a decidir qué información es relevante y qué herramienta conviene usar.
:::

## Cómo usar este repaso

Antes de leer una solución, intenta cada problema durante al menos **3–5 minutos**.

No es necesario resolverlos en orden. Si un problema se atasca, marca exactamente el punto donde aparece la dificultad:

- sintaxis;
- semántica;
- traducción;
- equivalencia;
- inferencia.

Las etiquetas **Recuperación**, **Consolidación**, **Diagnóstico** y **Síntesis** indican la función pedagógica del ejercicio, pero no revelan la técnica necesaria para resolverlo.

## 1.7.1 Problemas acumulativos

1. **[Recuperación]** Clasifica cada expresión como proposición, pregunta, instrucción o expresión abierta. Cuando sea una proposición, indica su valor de verdad si puede decidirse inmediatamente.

   a. $14=2\cdot 7$;

   b. «¿Es 19 primo?»;

   c. «Escribe un número impar»;

   d. $n+5=12$;

   e. «21 es divisible por 3».

2. **[Recuperación]** Para la fórmula

   $$
   \varphi=\neg\bigl(P\lor(Q\land\neg R)\bigr),
   $$

   determina:

   a. la conectiva principal;

   b. el alcance de cada negación;

   c. todas sus subfórmulas;

   d. si está bien formada, justificándolo mediante las reglas de formación.

3. **[Consolidación]** Sea la valuación

   $$
   \nu:\qquad P=V,\qquad Q=F,\qquad R=V.
   $$

   Evalúa de adentro hacia afuera

   $$
   \neg\bigl((P\land Q)\lor(\neg Q\land R)\bigr).
   $$

   Indica qué parte de tu trabajo es sintáctica y cuál es semántica.

4. **[Consolidación]** Construye la tabla de verdad de

   $$
   (P\lor Q)\land\neg(P\land Q).
   $$

   Clasifica la fórmula como tautología, contradicción o contingencia y describe verbalmente qué situación expresa.

5. **[Consolidación]** Decide si

   $$
   \neg(P\land Q)
   $$

   y

   $$
   \neg P\land\neg Q
   $$

   son lógicamente equivalentes. No respondas por memoria: justifica mediante una tabla de verdad o mediante leyes de equivalencia ya disponibles.

6. **[Recuperación]** Sea

   $$
   P:\quad\text{«el entero es divisible por 4»},
   $$

   $$
   Q:\quad\text{«el entero es par»}.
   $$

   Traduce simbólicamente:

   a. si el entero es divisible por 4, entonces es par;

   b. el entero es par solo si es divisible por 4;

   c. ser divisible por 4 es condición suficiente para ser par;

   d. ser par es condición necesaria para ser divisible por 4;

   e. el entero es divisible por 4 si y solo si es par.

   Compara cuidadosamente las fórmulas obtenidas.

7. **[Consolidación]** Para

   $$
   P\to Q,
   $$

   escribe:

   a. la recíproca;

   b. la inversa;

   c. la contrapositiva.

   Luego determina cuáles son lógicamente equivalentes al condicional original y cuáles son equivalentes entre sí.

8. **[Consolidación]** Simplifica

   $$
   \neg(P\to Q)
   $$

   hasta una fórmula que utilice únicamente $\neg$ y $\land$.

   Explica qué combinación de valores de $P$ y $Q$ hace falsa a la implicación original.

9. **[Diagnóstico]** Un estudiante razona:

   > Si estudio, apruebo.  
   > Aprobé.  
   > Por tanto, estudié.

   a. simboliza el argumento;

   b. identifica el error;

   c. produce una valuación que refute la forma argumental;

   d. explica por qué la posible verdad de las tres frases en una situación concreta no vuelve válida la forma.

10. **[Diagnóstico]** Analiza:

    > Si el servidor está apagado, la pantalla está negra.  
    > El servidor no está apagado.  
    > Por tanto, la pantalla no está negra.

    Determina si el argumento es válido. Si no lo es, exhibe una asignación refutadora.

11. **[Consolidación]** Considera las premisas

    $$
    P\to Q,\qquad Q\to R,\qquad \neg R.
    $$

    Determina qué puede concluirse acerca de $P$ y justifica cada paso.

12. **[Consolidación]** Considera

    $$
    P\lor Q,\qquad \neg P,\qquad Q\to R.
    $$

    Determina una conclusión no trivial y presenta una cadena completa de inferencias.

13. **[Diagnóstico]** Un estudiante afirma

    $$
    P\leftrightarrow Q\equiv P\to Q.
    $$

    Encuentra una valuación que muestre el error y explica conceptualmente qué información adicional contiene el bicondicional.

14. **[Consolidación]** Decide si el siguiente argumento es válido:

    $$
    P\to(Q\lor R),\qquad \neg Q,\qquad \neg R,\qquad \therefore\neg P.
    $$

    Puedes razonar mediante equivalencias, reglas de inferencia o una tabla de verdad, pero debes hacer explícita tu justificación.

15. **[Síntesis]** Sean

    $$
    P:\quad\text{«la figura es un cuadrado»},
    $$

    $$
    Q:\quad\text{«la figura es un rectángulo»},
    $$

    $$
    R:\quad\text{«la figura tiene cuatro lados»}.
    $$

    Se dan las premisas

    $$
    P\to Q,\qquad Q\to R,\qquad \neg R.
    $$

    a. traduce las premisas al lenguaje natural;

    b. determina qué conclusiones pueden obtenerse sobre $Q$ y $P$;

    c. identifica las reglas utilizadas;

    d. explica por qué no fue necesario conocer si existen realmente cuadrados o rectángulos.

16. **[Síntesis]** Estudia las fórmulas

    $$
    A=(P\to Q)\land(Q\to P),
    $$

    $$
    B=P\leftrightarrow Q.
    $$

    a. construye una tabla suficiente para comparar $A$ y $B$;

    b. decide si $A\equiv B$;

    c. explica en palabras por qué el resultado era razonable antes de hacer la tabla.

17. **[Síntesis]** Considera el argumento

    $$
    P\lor Q,\qquad P\to R,\qquad Q\to R,\qquad \therefore R.
    $$

    a. determina si es válido;

    b. si lo es, justifícalo sin construir la tabla completa;

    c. verifica después la validez mediante la imposibilidad de una asignación refutadora.

18. **[Síntesis]** Diseña tú mismo un argumento de tres premisas y una conclusión que cumpla simultáneamente:

    a. utiliza al menos una implicación y una disyunción;

    b. es válido;

    c. una de sus premisas puede ser falsa en alguna valuación;

    d. su validez puede justificarse mediante una cadena de reglas de inferencia.

    Después simbolízalo, demuestra su validez y explica por qué «válido» no significa «todas sus premisas son verdaderas».

# Soluciones completas

## 1

1. $14=2\cdot7$ es una proposición verdadera.
2. «¿Es 19 primo?» es una pregunta, no una proposición.
3. «Escribe un número impar» es una instrucción.
4. $n+5=12$ es una expresión abierta mientras $n$ no esté fijado.
5. «21 es divisible por 3» es una proposición verdadera.

La clasificación lógica debe realizarse antes de preguntar por verdad o falsedad.

## 2

Tenemos

$$
\varphi=\neg\bigl(P\lor(Q\land\neg R)\bigr).
$$

La última operación aplicada es la negación exterior. Por tanto,

$$
\boxed{\text{conectiva principal de }\varphi=\neg.}
$$

La negación interior

$$
\neg R
$$

tiene alcance $R$.

La negación exterior tiene alcance

$$
P\lor(Q\land\neg R).
$$

Las subfórmulas son

$$
P,\qquad Q,\qquad R,
$$

$$
\neg R,
$$

$$
Q\land\neg R,
$$

$$
P\lor(Q\land\neg R),
$$

y

$$
\neg\bigl(P\lor(Q\land\neg R)\bigr).
$$

La fórmula está bien formada porque

$$
R\Longrightarrow\neg R,
$$

$$
Q,\neg R\Longrightarrow Q\land\neg R,
$$

$$
P,Q\land\neg R\Longrightarrow P\lor(Q\land\neg R),
$$

y finalmente

$$
P\lor(Q\land\neg R)\Longrightarrow\neg\bigl(P\lor(Q\land\neg R)\bigr).
$$

## 3

Bajo

$$
P=V,\qquad Q=F,\qquad R=V,
$$

calculamos primero

$$
P\land Q=V\land F=F.
$$

Después,

$$
\neg Q=V,
$$

y

$$
\neg Q\land R=V\land V=V.
$$

Así,

$$
(P\land Q)\lor(\neg Q\land R)=F\lor V=V.
$$

Finalmente,

$$
\neg\bigl((P\land Q)\lor(\neg Q\land R)\bigr)=F.
$$

Identificar las subfórmulas y el orden de evaluación es trabajo sintáctico. Sustituir valores y aplicar las tablas de las conectivas es trabajo semántico.

## 4

Construimos:

| $P$ | $Q$ | $P\lor Q$ | $P\land Q$ | $(P\lor Q)\land\neg(P\land Q)$ |
|---|---|---|---|---|
| V | V | V | V | F |
| V | F | V | F | V |
| F | V | V | F | V |
| F | F | F | F | F |

La fórmula es verdadera en algunas valuaciones y falsa en otras. Por tanto, **es contingente**.

Verbalmente expresa que exactamente una de las dos proposiciones es verdadera: al menos una es verdadera, pero no ambas simultáneamente.

## 5

Por De Morgan,

$$
\neg(P\land Q)\equiv\neg P\lor\neg Q.
$$

La fórmula propuesta

$$
\neg P\land\neg Q
$$

es más fuerte. Basta tomar

$$
P=V,\qquad Q=F.
$$

Entonces

$$
P\land Q=F
$$

y

$$
\neg(P\land Q)=V.
$$

Pero

$$
\neg P\land\neg Q=F\land V=F.
$$

Por tanto,

$$
\boxed{\neg(P\land Q)\not\equiv\neg P\land\neg Q.}
$$

## 6

Con

$$
P:\quad\text{divisible por 4},\qquad Q:\quad\text{par},
$$

tenemos:

1. «Si es divisible por 4, entonces es par»:

   $$
   P\to Q.
   $$

2. «Es par solo si es divisible por 4»:

   $$
   Q\to P.
   $$

3. «Ser divisible por 4 es condición suficiente para ser par»:

   $$
   P\to Q.
   $$

4. «Ser par es condición necesaria para ser divisible por 4»:

   $$
   P\to Q.
   $$

5. «Es divisible por 4 si y solo si es par»:

   $$
   P\leftrightarrow Q.
   $$

Los incisos 1, 3 y 4 expresan el mismo condicional. El inciso 2 expresa su recíproca. El inciso 5 exige ambas direcciones.

## 7

Para

$$
P\to Q,
$$

tenemos:

- recíproca: $Q\to P$;
- inversa: $\neg P\to\neg Q$;
- contrapositiva: $\neg Q\to\neg P$.

La equivalencia fundamental es

$$
P\to Q\equiv\neg Q\to\neg P.
$$

Además,

$$
Q\to P\equiv\neg P\to\neg Q.
$$

Por tanto, el condicional original es equivalente a su contrapositiva; la recíproca es equivalente a la inversa.

## 8

Sabemos

$$
P\to Q\equiv\neg P\lor Q.
$$

Negando,

$$
\neg(P\to Q)\equiv\neg(\neg P\lor Q).
$$

Por De Morgan,

$$
\neg(\neg P\lor Q)\equiv\neg\neg P\land\neg Q.
$$

Por doble negación,

$$
\boxed{\neg(P\to Q)\equiv P\land\neg Q.}
$$

Así, la implicación $P\to Q$ es falsa exactamente cuando

$$
P=V,\qquad Q=F.
$$

## 9

Sea

$$
P:\quad\text{«estudio»},\qquad Q:\quad\text{«apruebo»}.
$$

La forma es

$$
P\to Q,\qquad Q,\qquad \therefore P.
$$

Esta es la falacia de **afirmar el consecuente**.

Una asignación refutadora es

$$
P=F,\qquad Q=V.
$$

Entonces

$$
P\to Q=V,\qquad Q=V,
$$

pero

$$
P=F.
$$

Así las premisas pueden ser verdaderas y la conclusión falsa.

Incluso si, en una situación concreta, alguien estudió y aprobó, eso solo haría verdaderas las oraciones particulares. La validez exige que ninguna valuación haga verdaderas todas las premisas y falsa la conclusión.

## 10

Sea

$$
P:\quad\text{«el servidor está apagado»},\qquad Q:\quad\text{«la pantalla está negra»}.
$$

La forma es

$$
P\to Q,\qquad \neg P,\qquad \therefore\neg Q.
$$

Es la falacia de **negar el antecedente**.

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

Por tanto, **el argumento es inválido**.

## 11

Tenemos

$$
P\to Q,\qquad Q\to R,\qquad \neg R.
$$

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

Después, de

$$
P\to Q
$$

y

$$
\neg Q
$$

obtenemos nuevamente por *modus tollens*

$$
\boxed{\neg P.}
$$

También podríamos encadenar primero

$$
P\to Q,\qquad Q\to R
$$

para obtener

$$
P\to R,
$$

y usar después $\neg R$.

## 12

De

$$
P\lor Q
$$

y

$$
\neg P
$$

obtenemos por silogismo disyuntivo

$$
Q.
$$

De

$$
Q
$$

y

$$
Q\to R
$$

obtenemos por *modus ponens*

$$
R.
$$

La cadena completa es

$$
P\lor Q,\ \neg P\Longrightarrow Q\Longrightarrow R.
$$

## 13

El bicondicional

$$
P\leftrightarrow Q
$$

exige que $P$ y $Q$ tengan el mismo valor de verdad.

Tomemos

$$
P=F,\qquad Q=V.
$$

Entonces

$$
P\to Q=V,
$$

porque el antecedente es falso. Pero

$$
P\leftrightarrow Q=F,
$$

porque los valores son distintos.

Por tanto,

$$
\boxed{P\leftrightarrow Q\not\equiv P\to Q.}
$$

Conceptualmente, $P\leftrightarrow Q$ contiene las dos direcciones

$$
P\to Q
$$

y

$$
Q\to P.
$$

## 14

Las premisas son

$$
P\to(Q\lor R),\qquad \neg Q,\qquad \neg R.
$$

Por De Morgan,

$$
\neg Q\land\neg R\equiv\neg(Q\lor R).
$$

Así, de las dos últimas premisas obtenemos

$$
\neg(Q\lor R).
$$

Ahora aplicamos *modus tollens* a

$$
P\to(Q\lor R)
$$

y

$$
\neg(Q\lor R).
$$

Concluimos

$$
\boxed{\neg P.}
$$

Por tanto, **el argumento es válido**.

## 15

Las premisas significan:

- $P\to Q$: si la figura es un cuadrado, entonces es un rectángulo;
- $Q\to R$: si la figura es un rectángulo, entonces tiene cuatro lados;
- $\neg R$: la figura no tiene cuatro lados.

De

$$
Q\to R
$$

y

$$
\neg R
$$

obtenemos

$$
\neg Q
$$

por *modus tollens*.

Después, de

$$
P\to Q
$$

y

$$
\neg Q
$$

obtenemos

$$
\neg P.
$$

Así,

$$
\boxed{\neg Q\qquad\text{y}\qquad\neg P.}
$$

No necesitamos saber si existen realmente cuadrados o rectángulos porque la validez depende de la forma lógica del argumento, no de la materia de las proposiciones.

## 16

Construimos:

| $P$ | $Q$ | $P\to Q$ | $Q\to P$ | $A=(P\to Q)\land(Q\to P)$ |
|---|---|---|---|---|
| V | V | V | V | V |
| V | F | F | V | F |
| F | V | V | F | F |
| F | F | V | V | V |

El bicondicional

$$
B=P\leftrightarrow Q
$$

también es verdadero exactamente cuando $P$ y $Q$ tienen el mismo valor:

| $P$ | $Q$ | $B$ |
|---|---|---|
| V | V | V |
| V | F | F |
| F | V | F |
| F | F | V |

Por tanto,

$$
\boxed{(P\to Q)\land(Q\to P)\equiv P\leftrightarrow Q.}
$$

Era razonable esperar el resultado porque «$P$ si y solo si $Q$» afirma precisamente las dos direcciones condicionales.

## 17

Tenemos

$$
P\lor Q,\qquad P\to R,\qquad Q\to R.
$$

La disyunción nos dice que ocurre al menos uno de los dos casos.

Si ocurre $P$, entonces $R$ por $P\to R$.

Si ocurre $Q$, entonces $R$ por $Q\to R$.

En cualquiera de los casos,

$$
\boxed{R.}
$$

Para verificar que no existe una asignación refutadora, supongamos que las tres premisas son verdaderas y

$$
R=F.
$$

De

$$
P\to R=V
$$

y $R=F$ se sigue

$$
P=F.
$$

De

$$
Q\to R=V
$$

y $R=F$ se sigue

$$
Q=F.
$$

Pero entonces

$$
P\lor Q=F,
$$

contradiciendo la primera premisa.

Por tanto no existe asignación refutadora y el argumento es válido.

## 18

Hay muchas respuestas posibles. Una primera propuesta podría ser

$$
P\lor Q,
$$

$$
P\to R,
$$

$$
\neg P,
$$

$$
\therefore R.
$$

De

$$
P\lor Q
$$

y

$$
\neg P
$$

obtenemos $Q$. Sin embargo, todavía no tenemos una premisa que permita llegar a $R$. Así que esta primera propuesta no satisface lo pedido. **El diagnóstico forma parte del ejercicio.**

Podemos corregirla usando

$$
P\lor Q,
$$

$$
\neg P,
$$

$$
Q\to R,
$$

$$
\therefore R.
$$

Ahora

$$
P\lor Q,\ \neg P\Longrightarrow Q
$$

por silogismo disyuntivo, y

$$
Q,\ Q\to R\Longrightarrow R
$$

por *modus ponens*.

Así, **el argumento es válido**.

Una premisa puede ser falsa bajo alguna valuación; por ejemplo, $\neg P$ es falsa cuando $P=V$. Esto no afecta la validez.

«Válido» significa únicamente:

> no existe una valuación en la que todas las premisas sean verdaderas y la conclusión sea falsa.

::: {.callout-tip title="Mapa de recuperación del capítulo 1"}
Después de resolver el repaso, conviene poder reconstruir sin mirar el texto la cadena

$$
\boxed{
\text{proposición}
\longrightarrow
\text{fórmula bien formada}
\longrightarrow
\text{valuación}
\longrightarrow
\text{tabla de verdad}
\longrightarrow
\text{equivalencia}
\longrightarrow
\text{implicación}
\longrightarrow
\text{bicondicional}
\longrightarrow
\text{validez}
}
$$

Y conviene mantener separadas tres preguntas:

1. **¿Está bien formada?** — sintaxis.
2. **¿Qué valor recibe?** — semántica.
3. **¿La conclusión se sigue de las premisas?** — validez.
:::

::: {.callout-note title="Registro de dependencias"}
Esta sección no introduce ninguna noción nueva. Su función es recuperar e intercalar contenidos de §§1.1–1.6:

- proposiciones y expresiones abiertas;
- fórmulas bien formadas, subfórmulas, alcance y conectiva principal;
- valuaciones y tablas de verdad;
- equivalencia lógica;
- negación, conjunción, disyunción, implicación y bicondicional;
- recíproca, inversa y contrapositiva;
- condiciones necesarias y suficientes;
- premisas, conclusión, validez y asignaciones refutadoras;
- *modus ponens*, *modus tollens*, silogismo disyuntivo y silogismo hipotético;
- falacias de afirmar el consecuente y negar el antecedente.

No se han introducido cuantificadores ni teoría formal de predicados. El capítulo 2 puede comenzar ahora con una recuperación acumulativa reciente del lenguaje proposicional completo.
:::

---

**Siguiente capítulo:** Capítulo 2 — Cuantificadores y estructura lógica.
