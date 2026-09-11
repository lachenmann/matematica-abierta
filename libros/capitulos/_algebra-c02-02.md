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
