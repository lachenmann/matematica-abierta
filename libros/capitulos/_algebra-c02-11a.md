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

Pero todavía podemos pedir algo más.

Consideremos:

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

Estas dos arquitecturas reciben nombres específicos.

Y, más importante aún, demostraremos que **toda fórmula proposicional del lenguaje que hemos construido puede llevarse a una forma de cada tipo**.

La tabla de verdad dejará así de ser solamente un instrumento de evaluación.

También se convertirá en un procedimiento de **síntesis de fórmulas**.

---

### 11.1 Literales

Las piezas más pequeñas de las formas normales serán muy sencillas.

::: {.ma-block .ma-definicion #apm-i-d0022}
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

no son literales.

La negación de un literal, en el sentido que necesitaremos, debe estar aplicada directamente a una variable proposicional.

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

es una conjunción de uno o más literales.

El último bloque:

$$
q
$$

puede considerarse una conjunción de un solo literal.

::: {.ma-block .ma-definicion #apm-i-d0023}
**Definición — Forma normal disyuntiva**

Una fórmula está en **forma normal disyuntiva**, abreviada **FND**, cuando es una disyunción de una o más conjunciones de uno o más literales.
:::

Por ejemplo:

$$
(p\land q)\lor(\neg p\land r)
$$

está en FND.

También:

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

::: {.ma-block .ma-definicion #apm-i-d0024}
**Definición — Forma normal conjuntiva**

Una fórmula está en **forma normal conjuntiva**, abreviada **FNC**, cuando es una conjunción de una o más disyunciones de uno o más literales.
:::

Así:

$$
(p\lor q)\land(\neg p\lor r)
$$

está en FNC.

También:

$$
p\land\neg q
$$

está en FNC, pues cada cláusula puede consistir en un solo literal.

Y una sola disyunción:

$$
p\lor q
$$

puede considerarse una FNC con una única cláusula.

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

de modo que toda la conjunción es verdadera.

Ahora cambiemos cualquier valor de la fila.

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

Ahora queremos la construcción dual.

Consideremos nuevamente la fila:

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

Por tanto, toda la disyunción es falsa.

Si cambia cualquiera de los tres valores, al menos el literal correspondiente se vuelve verdadero.

Así:

$$
\boxed{
\neg p\lor q\lor\neg r
}
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

Queremos una disyunción falsa exactamente allí.

Tomamos:

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

::: {.ma-block .ma-observacion #apm-i-x0019}
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
\boxed{
(p\land q)\lor(\neg p\land\neg q).
}
$$

Así:

$$
p\leftrightarrow q
\equiv
(p\land q)\lor(\neg p\land\neg q).
$$

Esta es precisamente una equivalencia que ya habíamos demostrado en [la proposición «Equivalencias fundamentales del bicondicional»](#apm-i-p0006).

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

::: {.ma-block .ma-enunciado #apm-i-t0001}
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

Usaremos la tabla completa de $F$.

Para la FND:

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

filas.

Consideremos una fila donde:

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

a esa disyunción.

En una fila donde $F=\mathrm V$, aparece en $D$ la conjunción construida específicamente para esa fila; por tanto:

$$
D=\mathrm V.
$$

En una fila donde $F=\mathrm F$, ninguna de las conjunciones correspondientes a filas verdaderas puede ser verdadera, porque cada una exige una asignación distinta.

Por tanto:

$$
D=\mathrm F.
$$

Así, $D$ y $F$ tienen la misma columna.

Luego:

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

Por tanto, es lógicamente equivalente a $F$.

Así queda probada la existencia de una FND en todos los casos.

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

En efecto, allí todos sus literales son falsos.

Si cambia cualquiera de los valores de la fila, el literal correspondiente se vuelve verdadero y, por tanto, toda la disyunción se vuelve verdadera.

Repetimos esta construcción para cada fila donde $F$ sea falsa.

Si hay al menos una fila falsa, conjuntamos todas las disyunciones obtenidas.

Llamemos:

$$
N
$$

a esa conjunción.

En una fila donde $F=\mathrm F$, la cláusula construida específicamente para esa fila es falsa; por tanto:

$$
N=\mathrm F.
$$

En una fila donde $F=\mathrm V$, ninguna de las cláusulas correspondientes a filas falsas puede ser falsa, porque cada una falla únicamente en su propia fila.

Por tanto:

$$
N=\mathrm V.
$$

Así, $N$ y $F$ tienen la misma columna.

Luego:

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

Por tanto, es lógicamente equivalente a $F$.

Con ello queda probada también la existencia de una FNC.

Por tanto, toda fórmula proposicional del lenguaje considerado admite una FND y una FNC lógicamente equivalentes.

$$
\boxed{\text{Queda demostrado el teorema «Existencia de formas normales proposicionales».}}
$$

---
