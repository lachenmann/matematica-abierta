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
\text{Queda demostrado [el teorema «Existencia de formas normales proposicionales»](#apm-i-t0001).}
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

### Reconocer formas normales {#apm-i-e0124}
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

### Construir desde las filas verdaderas {#apm-i-e0125}
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

### La conjunción y la cláusula de una fila {#apm-i-e0126}
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

### Explorar la no unicidad {#apm-i-e0127}
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

### Casos extremos {#apm-i-e0128}
#### a)

Da una FND y una FNC para una tautología.

#### b)

Da una FND y una FNC para una contradicción.

#### c)

Explica por qué estas fórmulas resuelven los casos extremos de [el teorema «Existencia de formas normales proposicionales»](#apm-i-t0001).

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

### Síntesis: tabla, FND, FNC y simplificación {#apm-i-e0129}
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

Por [la proposición «Equivalencias fundamentales del bicondicional»](#apm-i-p0006):

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

> [el teorema «Existencia de formas normales proposicionales»](#apm-i-t0001) — toda fórmula proposicional del lenguaje considerado admite una FND y una FNC lógicamente equivalentes.

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
