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

::: {.ma-block .ma-definicion #apm-i-d0018}
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

::: {.ma-block .ma-definicion #apm-i-d0019}
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

::: {.ma-block .ma-definicion #apm-i-d0020}
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

::: {.ma-block .ma-observacion #apm-i-x0014}
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

### Clasificar por tabla {#apm-i-e0090}

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

### Verdadera no significa tautológica {#apm-i-e0091}

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

### Explorar una fórmula {#apm-i-e0092}

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

### Contraasignación {#apm-i-e0093}

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

### Refutar una pretendida contradicción {#apm-i-e0094}

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

### Síntesis: clasificar con estrategia {#apm-i-e0095}

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

Pero en [el ejercicio «Síntesis: implicación y contraposición asociada»](#apm-i-e0089) vimos algo diferente: dos fórmulas distintas,

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
