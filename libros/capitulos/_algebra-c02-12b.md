## Ejercicios

### Elegir el método {#apm-i-e0130}

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

### Una tautología por cálculo {#apm-i-e0131}

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

### Refutar sin tabla completa {#apm-i-e0132}

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

### Dos fórmulas, una misma condición {#apm-i-e0133}

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

### Síntesis final {#apm-i-e0134}

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

Usamos [la proposición «Equivalencias fundamentales de la implicación»](#apm-i-p0005):

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

y convertimos equivalencias demostradas en leyes de cálculo.

Construimos progresivamente:

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
\boxed{
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
}
$$

Volvemos así a una idea estructural que acompañará todo este tratado:

$$
\boxed{
\text{una estructura}
=
\text{objetos}
+
\text{operaciones}
+
\text{leyes}.
}
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

## T1-C03 — Predicados, cuantificadores y lenguaje matemático
