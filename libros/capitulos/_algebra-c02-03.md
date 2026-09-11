## §3. Implicación: «si..., entonces...»

Ya sabemos representar proposiciones mediante letras y combinarlas con:

$$
\neg,\qquad
\land,\qquad
\lor.
$$

Pero gran parte del razonamiento matemático utiliza una construcción distinta:

> «Si ocurre esto, entonces ocurre aquello».

Consideremos dos proposiciones:

$$
p=\text{«18 es múltiplo de 6»}
$$

y:

$$
q=\text{«18 es par»}.
$$

Podemos formar la afirmación:

> «Si 18 es múltiplo de 6, entonces 18 es par».

En símbolos escribiremos:

$$
p\Rightarrow q.
$$

La dificultad no está en leer la frase.

La dificultad está en precisar **cuándo debe considerarse falsa**.

La idea fundamental será:

$$
\boxed{
p\Rightarrow q
\text{ falla únicamente cuando }
p=\mathrm V
\text{ y }
q=\mathrm F.
}
$$

Todo lo demás en esta sección se organizará alrededor de este hecho.

---

### 3.1 La implicación

::: {.ma-block .ma-definicion #apm-t1-c02-d0015}
**Definición — Implicación**

La **implicación** de dos fórmulas $P$ y $Q$ es la fórmula:

$$
P\Rightarrow Q.
$$

Se lee «si $P$, entonces $Q$». Es falsa exactamente cuando $P$ es verdadera y $Q$ es falsa; en los demás casos es verdadera.
:::

En:

$$
P\Rightarrow Q,
$$

llamamos:

- **antecedente** a $P$;
- **consecuente** a $Q$.

Así, en:

$$
p\Rightarrow q,
$$

$p$ es el antecedente y $q$ es el consecuente.

La tabla completa es:

::: {.ma-block .ma-observacion}
En evaluaciones concretas escribiremos, por brevedad, expresiones como $\mathrm V\Rightarrow\mathrm F=\mathrm F$. Esto significa que una implicación cuyo antecedente recibe $\mathrm V$ y cuyo consecuente recibe $\mathrm F$ recibe a su vez $\mathrm F$; $\mathrm V$ y $\mathrm F$ son valores de verdad.
:::

| $P$ | $Q$ | $P\Rightarrow Q$ |
|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ |

La tabla puede parecer menos inmediata que las de conjunción o disyunción.

Por eso debemos entender qué afirma realmente una implicación.

---

### 3.2 La implicación descarta un caso

La fórmula:

$$
P\Rightarrow Q
$$

establece una condición:

> no debe ocurrir que $P$ sea verdadera y $Q$ sea falsa.

Podemos condensarlo así:

$$
\boxed{
P\Rightarrow Q
\text{ excluye el caso }
(\mathrm V,\mathrm F).
}
$$

Esta perspectiva explica toda la tabla.

#### Caso 1

$$
P=\mathrm V,
\qquad
Q=\mathrm V.
$$

El antecedente ocurre y el consecuente también.

La condición no ha fallado:

$$
P\Rightarrow Q=\mathrm V.
$$

#### Caso 2

$$
P=\mathrm V,
\qquad
Q=\mathrm F.
$$

El antecedente ocurre, pero el consecuente no.

Este es exactamente el caso prohibido:

$$
P\Rightarrow Q=\mathrm F.
$$

#### Caso 3

$$
P=\mathrm F,
\qquad
Q=\mathrm V.
$$

El antecedente no ocurre.

Por tanto, no estamos ante el caso «antecedente verdadero y consecuente falso».

La implicación recibe:

$$
\mathrm V.
$$

#### Caso 4

$$
P=\mathrm F,
\qquad
Q=\mathrm F.
$$

De nuevo, el antecedente es falso.

Tampoco aparece el único caso que haría falsa la implicación.

Por tanto:

$$
P\Rightarrow Q=\mathrm V.
$$

::: {.ma-block .ma-intuicion}
**Idea clave**

Una implicación no afirma que su antecedente sea verdadero. Afirma qué debe ocurrir con el consecuente **si** el antecedente es verdadero.
:::

---

### 3.3 ¿Por qué una implicación con antecedente falso es verdadera?

Este suele ser el punto más extraño al principio.

Consideremos:

$$
p=\text{«10 es impar»},
$$

$$
q=\text{«10 es mayor que 3»}.
$$

Tenemos:

$$
p=\mathrm F,
\qquad
q=\mathrm V.
$$

Entonces:

$$
p\Rightarrow q=\mathrm V.
$$

La fórmula no dice que 10 sea impar.

Tampoco afirma que ser impar sea la causa de ser mayor que 3.

Solo establece una relación lógica entre los valores de las dos proposiciones.

Como el antecedente:

$$
p
$$

es falso, no se produce la única situación que refutaría la implicación:

$$
p=\mathrm V,
\qquad
q=\mathrm F.
$$

Podemos pensar la implicación como una regla que solo puede violarse cuando el antecedente se cumple y el consecuente falla.

Esta interpretación será especialmente útil cuando construyamos tablas más complejas.

---

### 3.4 Implicación no significa causalidad

Consideremos:

$$
p=\text{«2+2=4»},
$$

$$
q=\text{«7 es primo»}.
$$

Ambas proposiciones son verdaderas.

Por tanto:

$$
p\Rightarrow q
$$

es verdadera.

Pero sería absurdo afirmar que:

> «$2+2=4$ causa que 7 sea primo».

La lógica proposicional no está describiendo aquí una relación causal.

Está evaluando la fórmula únicamente a partir de los valores de verdad de sus componentes.

No afirmamos que todos los usos cotidianos de «si..., entonces...» queden agotados por esta tabla. En este capítulo estamos definiendo y estudiando un conectivo matemático preciso: la implicación de la lógica proposicional clásica.

::: {.ma-block .ma-intuicion}
**Idea clave**

El símbolo $\Rightarrow$ expresa la implicación de la lógica proposicional clásica; por sí solo no significa «causa», «produce» ni «ocurre antes que».
:::

En argumentos matemáticos, las proposiciones implicadas suelen tener además una relación conceptual importante. Pero esa relación no forma parte de la tabla de verdad del conectivo.

---

### 3.5 Varias maneras de decir la misma implicación

La fórmula:

$$
P\Rightarrow Q
$$

puede expresarse en español de varias maneras.

#### Forma directa

> «Si $P$, entonces $Q$».

#### Con «cuando»

> «Cuando $P$, se cumple $Q$».

Esta formulación debe usarse con cuidado en contextos temporales, pero en matemáticas suele expresar la misma dirección condicional.

#### Con «solo si»

> «$P$ solo si $Q$».

Esto también corresponde a:

$$
P\Rightarrow Q.
$$

La expresión «solo si» merece especial atención.

Por ejemplo:

> «Doce es múltiplo de cuatro solo si doce es par».

La parte que aparece después de «solo si» expresa una condición que debe cumplirse cuando se cumple la primera.

Por eso:

$$
\boxed{
\text{«$P$ solo si $Q$»}
\quad\longrightarrow\quad
P\Rightarrow Q.
}
$$

---

### 3.6 Condición suficiente

Si:

$$
P\Rightarrow Q,
$$

diremos que:

> **$P$ es una condición suficiente para $Q$.**

¿Por qué «suficiente»?

Porque, dentro de la implicación, la verdad de $P$ basta para exigir la verdad de $Q$.

En símbolos:

$$
P=\mathrm V
$$

obliga, si la implicación ha de ser verdadera, a:

$$
Q=\mathrm V.
$$

Así:

$$
\boxed{
P\Rightarrow Q
\quad\text{se lee también como}\quad
\text{«$P$ es suficiente para $Q$».}
}
$$

La palabra «suficiente» señala el antecedente.

---

### 3.7 Condición necesaria

La misma implicación:

$$
P\Rightarrow Q
$$

puede leerse desde el otro extremo:

> **$Q$ es una condición necesaria para $P$.**

¿Por qué «necesaria»?

Porque si $P$ es verdadera, $Q$ no puede ser falsa sin hacer falsa la implicación.

Es decir, para que pueda ocurrir $P$ respetando la implicación, necesitamos que ocurra $Q$.

Por tanto:

$$
\boxed{
P\Rightarrow Q
}
$$

expresa simultáneamente:

- $P$ es suficiente para $Q$;
- $Q$ es necesaria para $P$.

Esta pareja de formulaciones debe aprenderse como una sola estructura.

---

### 3.8 «Si» y «solo si» apuntan en direcciones distintas

Comparemos:

> «$P$ si $Q$»

con:

> «$P$ solo si $Q$».

La primera significa:

> «Si $Q$, entonces $P$»,

por tanto:

$$
Q\Rightarrow P.
$$

La segunda significa:

> «Si $P$, entonces $Q$»,

por tanto:

$$
P\Rightarrow Q.
$$

Así:

$$
\boxed{
\text{«$P$ si $Q$»}
\quad\longrightarrow\quad
Q\Rightarrow P
}
$$

mientras que:

$$
\boxed{
\text{«$P$ solo si $Q$»}
\quad\longrightarrow\quad
P\Rightarrow Q.
}
$$

Esta inversión es una fuente frecuente de errores de lectura.

No conviene memorizarla sin sentido: basta preguntar **qué condición obliga a cuál**.

---

### 3.9 La conversa

A partir de:

$$
P\Rightarrow Q,
$$

podemos intercambiar antecedente y consecuente.

Obtenemos:

$$
Q\Rightarrow P.
$$

Esta fórmula se denomina la **conversa** de la implicación original.

Así:

| Fórmula | Forma |
|---|---|
| implicación original | $P\Rightarrow Q$ |
| conversa | $Q\Rightarrow P$ |

No debemos suponer que, porque una implicación sea verdadera, su conversa también lo sea.

Consideremos:

$$
p=\text{«12 es múltiplo de 4»},
$$

$$
q=\text{«12 es par»}.
$$

En este caso tanto:

$$
p\Rightarrow q
$$

como:

$$
q\Rightarrow p
$$

resultan verdaderas, porque $p$ y $q$ son verdaderas.

Pero este ejemplo concreto no demuestra una regla general sobre implicaciones y conversas.

Más adelante tendremos herramientas para comparar sistemáticamente fórmulas.

---

### 3.10 La contraposición asociada

A partir de:

$$
P\Rightarrow Q,
$$

podemos formar:

$$
\neg Q\Rightarrow\neg P.
$$

Llamaremos a esta fórmula la **contraposición asociada** a:

$$
P\Rightarrow Q.
$$

El esquema es:

| Fórmula | Forma |
|---|---|
| implicación original | $P\Rightarrow Q$ |
| conversa | $Q\Rightarrow P$ |
| contraposición asociada | $\neg Q\Rightarrow\neg P$ |

Por ahora solo estamos aprendiendo a **construir y reconocer** estas fórmulas.

Más adelante demostraremos qué relación lógica existe entre una implicación y su contraposición.

Y, todavía después, estudiaremos cómo puede aprovecharse esa relación en una demostración matemática.

::: {.ma-block .ma-intuicion}
**Idea clave**

En esta sección la contraposición es una fórmula asociada. No la usamos todavía como método general de demostración.
:::

---

### 3.11 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-t1-c02-x0011}
**Ejemplo — Una implicación y sus cuatro asignaciones**

:::

Consideremos simplemente:

$$
p\Rightarrow q.
$$

Queremos entender qué sucede en las cuatro posibles asignaciones de valores de verdad.

#### Fila 1

$$
p=\mathrm V,
\qquad
q=\mathrm V.
$$

El antecedente es verdadero y el consecuente también.

No se viola la condición:

$$
p\Rightarrow q=\mathrm V.
$$

#### Fila 2

$$
p=\mathrm V,
\qquad
q=\mathrm F.
$$

El antecedente es verdadero, pero el consecuente falla.

Esta es la única fila que refuta la implicación:

$$
p\Rightarrow q=\mathrm F.
$$

#### Fila 3

$$
p=\mathrm F,
\qquad
q=\mathrm V.
$$

El antecedente es falso.

La combinación no es el caso prohibido:

$$
p\Rightarrow q=\mathrm V.
$$

#### Fila 4

$$
p=\mathrm F,
\qquad
q=\mathrm F.
$$

De nuevo, el antecedente es falso.

Por tanto:

$$
p\Rightarrow q=\mathrm V.
$$

Reunimos los resultados:

| $p$ | $q$ | $p\Rightarrow q$ |
|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ |

La manera más compacta de recordar la tabla no es memorizar cuatro filas independientes, sino recordar:

$$
\boxed{
\text{una implicación es falsa únicamente en el caso }
\mathrm V\Rightarrow\mathrm F.
}
$$

---

## Ejercicios

### Evaluar implicaciones {#apm-t1-c02-e0069}

Determina el valor de verdad.

#### a)

$$
\mathrm V\Rightarrow\mathrm V
$$

#### b)

$$
\mathrm V\Rightarrow\mathrm F
$$

#### c)

$$
\mathrm F\Rightarrow\mathrm V
$$

#### d)

$$
\mathrm F\Rightarrow\mathrm F
$$

#### Solución

Por la tabla de la implicación:

#### a)

$$
\mathrm V\Rightarrow\mathrm V=\mathrm V.
$$

#### b)

$$
\mathrm V\Rightarrow\mathrm F=\mathrm F.
$$

#### c)

$$
\mathrm F\Rightarrow\mathrm V=\mathrm V.
$$

#### d)

$$
\mathrm F\Rightarrow\mathrm F=\mathrm V.
$$

El único caso falso es:

$$
\boxed{
\mathrm V\Rightarrow\mathrm F.
}
$$

---

### Evaluar desde proposiciones concretas {#apm-t1-c02-e0070}

Sea:

$$
p=\text{«14 es par»},
$$

$$
q=\text{«14 es mayor que 20»}.
$$

Determina el valor de verdad de:

#### a)

$$
p\Rightarrow q
$$

#### b)

$$
q\Rightarrow p
$$

#### c)

$$
\neg q\Rightarrow p
$$

#### Solución

Tenemos:

$$
p=\mathrm V,
\qquad
q=\mathrm F.
$$

#### a)

$$
p\Rightarrow q
=
\mathrm V\Rightarrow\mathrm F
=
\mathrm F.
$$

#### b)

$$
q\Rightarrow p
=
\mathrm F\Rightarrow\mathrm V
=
\mathrm V.
$$

#### c)

Como:

$$
q=\mathrm F,
$$

tenemos:

$$
\neg q=\mathrm V.
$$

Entonces:

$$
\neg q\Rightarrow p
=
\mathrm V\Rightarrow\mathrm V
=
\mathrm V.
$$

---

### Suficiente y necesaria {#apm-t1-c02-e0071}

Supón que:

$$
P\Rightarrow Q.
$$

Completa correctamente.

#### a)

$P$ es una condición ________ para $Q$.

#### b)

$Q$ es una condición ________ para $P$.

#### c)

«$P$ solo si $Q$» se representa como ________.

#### Solución

#### a)

$P$ es una condición **suficiente** para $Q$.

#### b)

$Q$ es una condición **necesaria** para $P$.

#### c)

$$
P\Rightarrow Q.
$$

Por tanto:

$$
\boxed{
P\Rightarrow Q
}
$$

puede leerse simultáneamente desde sus dos extremos: suficiente desde el antecedente y necesaria desde el consecuente.

---

### «Si» frente a «solo si» {#apm-t1-c02-e0072}

Traduce a símbolos.

#### a)

> «$P$ si $Q$».

#### b)

> «$P$ solo si $Q$».

#### c)

Explica por qué las direcciones son diferentes.

#### Solución

#### a)

«$P$ si $Q$» significa:

> «Si $Q$, entonces $P$».

Por tanto:

$$
Q\Rightarrow P.
$$

#### b)

«$P$ solo si $Q$» significa:

$$
P\Rightarrow Q.
$$

#### c)

En el primer caso, $Q$ funciona como condición suficiente para $P$.

En el segundo, $Q$ funciona como condición necesaria para $P$.

Las frases contienen las mismas letras, pero organizan la dependencia lógica en direcciones contrarias.

---

### ¿Causalidad o implicación? {#apm-t1-c02-e0073}

Sean:

$$
p=\text{«5+5=10»},
$$

$$
q=\text{«11 es primo»}.
$$

#### a)

Determina el valor de:

$$
p\Rightarrow q.
$$

#### b)

¿La verdad de esta implicación significa que $5+5=10$ causa que 11 sea primo?

#### Solución

#### a)

Ambas proposiciones son verdaderas:

$$
p=\mathrm V,
\qquad
q=\mathrm V.
$$

Por tanto:

$$
p\Rightarrow q=\mathrm V.
$$

#### b)

No.

La tabla de verdad de la implicación depende únicamente de los valores de verdad de $p$ y $q$.

El conectivo:

$$
\Rightarrow
$$

no expresa por sí mismo una relación causal.

---

### Explorar el antecedente falso {#apm-t1-c02-e0074}

Supón que:

$$
P=\mathrm F.
$$

#### a)

¿Cuál es el valor de:

$$
P\Rightarrow Q
$$

si $Q=\mathrm V$?

#### b)

¿Y si $Q=\mathrm F$?

#### c)

Formula con tus palabras una regla que describa lo observado.

#### Solución

#### a)

$$
\mathrm F\Rightarrow\mathrm V=\mathrm V.
$$

#### b)

$$
\mathrm F\Rightarrow\mathrm F=\mathrm V.
$$

#### c)

Cuando el antecedente de una implicación es falso, la implicación es verdadera independientemente del valor de verdad del consecuente.

Esto ocurre porque no aparece el único caso que hace falsa una implicación:

$$
\mathrm V\Rightarrow\mathrm F.
$$

---

### Una contraasignación para la conversa {#apm-t1-c02-e0075}

Considera las dos fórmulas:

$$
P\Rightarrow Q
$$

y:

$$
Q\Rightarrow P.
$$

Encuentra valores para $P$ y $Q$ tales que la primera sea verdadera y la segunda sea falsa.

#### Solución

Necesitamos que:

$$
Q\Rightarrow P
$$

sea falsa.

La única posibilidad es:

$$
Q=\mathrm V,
\qquad
P=\mathrm F.
$$

Con esos valores:

$$
P\Rightarrow Q
=
\mathrm F\Rightarrow\mathrm V
=
\mathrm V,
$$

mientras que:

$$
Q\Rightarrow P
=
\mathrm V\Rightarrow\mathrm F
=
\mathrm F.
$$

Por tanto, la asignación:

$$
\boxed{
P=\mathrm F,
\qquad
Q=\mathrm V
}
$$

muestra que una implicación y su conversa no tienen necesariamente el mismo valor de verdad.

---

### Síntesis: leer una condición {#apm-t1-c02-e0076}

Sea:

$$
p=\text{«24 es múltiplo de 6»},
$$

$$
q=\text{«24 es par»}.
$$

#### a)

Determina los valores de verdad de $p$ y $q$.

#### b)

Escribe:

> «Si $p$, entonces $q$».

#### c)

Expresa la misma dirección usando las palabras «suficiente» y «necesaria».

#### d)

Escribe la conversa.

#### e)

Escribe la contraposición asociada.

#### f)

Evalúa la implicación original, su conversa y su contraposición asociada para estos valores concretos.

#### Solución

#### a)

Veinticuatro es múltiplo de seis y es par. Por tanto:

$$
p=\mathrm V,
\qquad
q=\mathrm V.
$$

#### b)

La fórmula es:

$$
p\Rightarrow q.
$$

#### c)

Podemos decir:

> «$p$ es suficiente para $q$».

y:

> «$q$ es necesaria para $p$».

Ambas frases corresponden a la dirección:

$$
p\Rightarrow q.
$$

#### d)

La conversa es:

$$
q\Rightarrow p.
$$

#### e)

La contraposición asociada es:

$$
\neg q\Rightarrow\neg p.
$$

#### f)

Como:

$$
p=\mathrm V,
\qquad
q=\mathrm V,
$$

tenemos:

$$
p\Rightarrow q
=
\mathrm V\Rightarrow\mathrm V
=
\mathrm V.
$$

También:

$$
q\Rightarrow p
=
\mathrm V\Rightarrow\mathrm V
=
\mathrm V.
$$

Además:

$$
\neg q=\mathrm F,
\qquad
\neg p=\mathrm F,
$$

por lo que:

$$
\neg q\Rightarrow\neg p
=
\mathrm F\Rightarrow\mathrm F
=
\mathrm V.
$$

Este ejemplo concreto muestra que las tres fórmulas resultan verdaderas con esta asignación. No demuestra, por sí solo, una relación general entre ellas.

---

## Síntesis

La implicación:

$$
P\Rightarrow Q
$$

se lee:

> «Si $P$, entonces $Q$».

Su tabla es:

| $P$ | $Q$ | $P\Rightarrow Q$ |
|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ |

El principio central es:

$$
\boxed{
P\Rightarrow Q
\text{ es falsa únicamente cuando }
P=\mathrm V
\text{ y }
Q=\mathrm F.
}
$$

También hemos aprendido que:

$$
P\Rightarrow Q
$$

puede leerse como:

- $P$ es suficiente para $Q$;
- $Q$ es necesaria para $P$;
- $P$ solo si $Q$.

Y debemos distinguir:

$$
P\Rightarrow Q
$$

de su conversa:

$$
Q\Rightarrow P,
$$

y de su contraposición asociada:

$$
\neg Q\Rightarrow\neg P.
$$

Por ahora no afirmamos que estas fórmulas se comporten de la misma manera. Esa comparación necesitará herramientas que todavía estamos construyendo.

---

## Hacia la sección siguiente

Una implicación expresa una sola dirección:

$$
P\Rightarrow Q.
$$

Pero a veces queremos afirmar simultáneamente que:

- $P$ conduce a $Q$;
- $Q$ conduce a $P$.

En el lenguaje matemático aparece entonces la expresión:

> «$P$ si y solo si $Q$».

La siguiente sección introducirá el conectivo que representa esa relación de dos direcciones:
