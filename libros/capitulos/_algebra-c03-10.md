## §10. Existencia y unicidad

En §4 aprendimos a leer:

$$
\exists x\,P(x)
$$

como:

> «Existe al menos un valor permitido de $x$ para el cual se cumple $P(x)$».

Desde entonces hemos insistido en una advertencia:

$$
\boxed{
\text{existencia}
\neq
\text{unicidad}.
}
$$

Encontrar un valor que satisface una condición demuestra que la exigencia existencial se cumple.

Pero no nos dice, por sí solo, si hay otros valores que también la satisfacen.

Consideremos, en el dominio de los enteros:

$$
P(x):\quad x^2=9.
$$

Tenemos, $P(3)$ y $P(-3)$. Por tanto:

$$
\exists x\,P(x)
$$

es verdadera.

Sin embargo, no hay un único valor que satisfaga la condición.

Ahora comparemos $Q(x):\quad 2x=6$. El valor $x=3$ satisface la condición.

Además, ningún otro entero la satisface. Aquí queremos expresar algo más fuerte que mera existencia:

> existe **exactamente un** valor.

---

### 10.1 Dos preguntas distintas

Ante una condición:

$$
P(x),
$$

podemos hacer dos preguntas.

#### Pregunta de existencia

> ¿Hay al menos un valor que satisface $P(x)$?

En símbolos:

$$
\exists x\,P(x).
$$

#### Pregunta de unicidad

> Si dos valores satisfacen $P(x)$, ¿tienen necesariamente que ser el mismo?

La existencia responde:

> «hay uno o más».

La unicidad responde:

> «no puede haber dos distintos».

Para afirmar **existencia única**, necesitamos ambas cosas. Así:

$$

\text{existencia única}
=
\text{existencia}
+
\text{unicidad}.

$$

---

### 10.2 La abreviatura \(\exists!\)

::: {.ma-block .ma-definicion #apm-t1-c03-d0035}
**Definición — Existencia única**

La escritura:

$$
\exists!x\,P(x)
$$

se lee:

> «Existe un único valor de $x$ para el cual se cumple $P(x)$».

Es una abreviatura de:

$$
\boxed{
\exists x\,\bigl(P(x)\land
\forall y\,(P(y)\Rightarrow y=x)\bigr).
}
$$
:::

El símbolo $\exists!$ no introduce un tercer tipo fundamental de cuantificador.

Es una abreviatura construida con:

$$
\exists,
\qquad
\forall,
\qquad
\land,
\qquad
\Rightarrow,
\qquad
=.
$$

Por eso conviene saber siempre expandirlo.

---

### 10.3 Leer la expansión

Examinemos:

$$
\exists x\,\bigl(P(x)\land
\forall y\,(P(y)\Rightarrow y=x)\bigr).
$$

La fórmula comienza con:

$$
\exists x.
$$

Por tanto, afirma que hay al menos un valor:

$$
x
$$

que cumple lo que sigue. Dentro encontramos una conjunción:

$$
P(x)
\land
\forall y\,(P(y)\Rightarrow y=x).
$$

La primera parte:

$$
P(x)
$$

dice:

> «$x$ satisface la condición».

La segunda:

$$
\forall y\,(P(y)\Rightarrow y=x)
$$

dice:

> «Cualquier otro valor $y$ que satisfaga la condición debe ser igual a $x$».

Así, el valor cuya existencia afirmamos no solo satisface $P$.

También absorbe todos los posibles casos: cualquiera que satisfaga $P$ tiene que coincidir con él.

---

### 10.4 La cláusula de existencia

Consideremos $\exists!x\,P(x)$. La expansión contiene:

$$
\exists x.
$$

Si no existe ningún valor que satisfaga:

$$
P(x),
$$

la afirmación de existencia única es falsa. Por ejemplo, en el dominio de los enteros:

$$
P(x):\quad 2x=1.
$$

No hay ningún entero que satisfaga la condición. Entonces $\exists!x\,(2x=1)$ es falsa.

No importa que podamos decir:

> «Si hubiera dos soluciones, serían iguales».

Sin existencia, no hay existencia única. Por eso la primera mitad del problema es siempre:

$$

\text{¿hay al menos un valor que funciona?}

$$

---

### 10.5 La cláusula de unicidad

Ahora consideremos, en los enteros:

$$
P(x):\quad x^2=9.
$$

Sí hay valores que satisfacen la condición. Por ejemplo: $x=3$.

Pero también:

$$
x=-3.
$$

Como:

$$
3\ne-3,
$$

hay al menos dos valores distintos que satisfacen $P$.

Por tanto:

$$
\exists!x\,(x^2=9)
$$

es falsa. La existencia se cumple. La unicidad falla. Así vemos que:

$$
\boxed{
\text{existencia sin unicidad}
\quad\text{no basta para}\quad
\exists!.
}
$$

---

### 10.6 Un ejemplo verdaderamente único

Trabajemos con enteros y consideremos:

$$
P(x):\quad 2x=6.
$$

Primero observamos que:

$$
x=3
$$

satisface:

$$
2x=6.
$$

Por tanto, existe al menos un valor. Ahora supongamos que un entero:

$$
y
$$

también satisface la condición. Entonces $2y=6$. Dividiendo ambos lados por $2$:

$$
y=3.
$$

Cualquier entero que satisfaga la condición debe ser igual a:

$$
3.
$$

Esto corresponde exactamente a:

$$
\forall y\,(2y=6\Rightarrow y=3).
$$

Así:

$$
\exists x\,\bigl(
2x=6
\land
\forall y\,(2y=6\Rightarrow y=x)
\bigr)
$$

es verdadera. En forma abreviada:

$$

\exists!x\,(2x=6).

$$

---

### 10.7 No confundir «el» con una prueba de unicidad

En la prosa matemática aparecen frases como:

> «el valor que satisface...»

o:

> «la solución...»

Ese artículo singular puede sugerir unicidad.

Pero el lenguaje no debe adelantarse a lo que hemos establecido.

Por ejemplo, para:

$$
x^2=9,
$$

sería engañoso hablar sin más de:

> «la solución entera»,

porque hay dos:

$$
3
\qquad\text{y}\qquad
-3.
$$

Antes de usar una descripción singular conviene saber si la condición realmente determina un único objeto.

La lógica nos ayuda a distinguir:

$$
\boxed{
\text{haber encontrado uno}
\neq
\text{haber demostrado que es el único}.
}
$$

---

### 10.8 Dos maneras equivalentes de expresar unicidad

La expansión canónica que adoptamos es:

$$
\exists x\,\bigl(
P(x)\land
\forall y\,(P(y)\Rightarrow y=x)
\bigr).
$$

Podemos leer la parte de unicidad como:

> «Todo valor que cumple $P$ coincide con el valor encontrado».

También podemos expresarla informalmente diciendo:

> «No existen dos valores distintos que cumplan $P$».

En este capítulo mantendremos como forma canónica la primera, porque hace visible la estructura:

1. encontrar un valor $x$;
2. exigir que cualquier $y$ que también cumpla $P$ satisfaga:
   $$
   y=x.
   $$

No necesitamos introducir otra abreviatura.

---

### 10.9 Existencia única y dominio

Como ocurre con toda afirmación cuantificada, el dominio sigue siendo esencial.

Consideremos $P(x):\quad x^2=4$. Si el dominio contiene únicamente valores no negativos, el único valor que satisface la condición es:

$$
2.
$$

En ese contexto:

$$
\exists!x\,P(x)
$$

es verdadera. Si el dominio es el de los enteros, en cambio, tanto:

$$
2
$$

como:

$$
-2
$$

satisfacen:

$$
x^2=4.
$$

Entonces la existencia se mantiene, pero la unicidad desaparece.

Así:

$$
\boxed{
\text{la unicidad también se afirma respecto de un dominio}.
}
$$

---

### 10.10 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-t1-c03-x0030}
**Ejemplo — Existencia y unicidad por separado**
:::

Trabajaremos con valores enteros y consideraremos:

$$
P(x):\quad 2x=6.
$$

Queremos analizar:

$$
\exists!x\,P(x).
$$

#### Paso 1 — Existencia

Tomemos $x=3$. Entonces $2\cdot3=6$. Por tanto:

$$
P(3)
$$

es verdadera. La existencia queda confirmada.

#### Paso 2 — Unicidad

Consideremos un entero cualquiera:

$$
y
$$

que también satisfaga:

$$
P(y).
$$

Entonces $2y=6$. Dividiendo por $2$:

$$
y=3.
$$

Por tanto, cualquier entero que satisfaga $P$ coincide con el valor:

$$
3.
$$

Esto se expresa mediante:

$$
\forall y\,(P(y)\Rightarrow y=3).
$$

#### Paso 3 — Reunir ambas partes

Tenemos:

$$
P(3)
$$

y:

$$
\forall y\,(P(y)\Rightarrow y=3).
$$

Por tanto:

$$
\exists x\,\bigl(
P(x)\land
\forall y\,(P(y)\Rightarrow y=x)
\bigr)
$$

es verdadera. En forma abreviada:

$$
\boxed{
\exists!x\,P(x).
}
$$

#### Comparación

Para:

$$
Q(x):\quad x^2=9,
$$

también hay existencia.

Pero: $Q(3)$ y $Q(-3)$ son verdaderas. Por tanto:

$$
\exists x\,Q(x)
$$

es verdadera, mientras:

$$
\exists!x\,Q(x)
$$

es falsa. La diferencia es exactamente la unicidad.

---
## Ejercicios

### Leer \(\exists!\) {#apm-t1-c03-e0189}
Trabajamos con valores enteros.

Lee en prosa:

$$
\exists!x\,(x+2=5).
$$

#### Solución


La fórmula se lee:

> «Existe un único entero $x$ tal que $x+2=5$».

La palabra:

> «único»

indica que la afirmación contiene dos exigencias:

- al menos un entero satisface la ecuación;
- ningún entero distinto puede satisfacerla también.

---

### Al menos uno y exactamente uno {#apm-t1-c03-e0190}
Compara:

$$
\exists x\,(x^2=9)
$$

con:

$$
\exists!x\,(x^2=9)
$$

en el dominio de los enteros.

Determina el valor de verdad de cada fórmula y explica la diferencia.

#### Solución


La primera fórmula:

$$
\exists x\,(x^2=9)
$$

es verdadera.

Por ejemplo:

$$
x=3
$$

satisface la condición.

Pero también:

$$
x=-3
$$

la satisface.

Por tanto, la segunda fórmula:

$$
\exists!x\,(x^2=9)
$$

es falsa.

La diferencia es:

- $\exists$ exige al menos un valor;
- $\exists!$ exige exactamente uno.

---

### Las dos cláusulas {#apm-t1-c03-e0191}
Explica qué función cumple cada parte de:

$$
\exists x\,\bigl(
P(x)\land
\forall y\,(P(y)\Rightarrow y=x)
\bigr).
$$

#### Solución


El cuantificador:

$$
\exists x
$$

afirma que hay algún valor:

$$
x
$$

para el cual se cumple la conjunción interna.

La primera parte:

$$
P(x)
$$

es la **cláusula de existencia**: el valor encontrado realmente satisface la condición.

La segunda:

$$
\forall y\,(P(y)\Rightarrow y=x)
$$

es la **cláusula de unicidad**: cualquier valor $y$ que también satisfaga $P$ debe coincidir con $x$.

Por tanto, la fórmula completa afirma que existe un valor y que ningún valor distinto puede satisfacer la misma condición.

---

### Existencia y unicidad en tres casos {#apm-t1-c03-e0192}
Trabajamos con valores enteros.

Clasifica cada condición según ocurra:

- ninguna solución;
- existencia sin unicidad;
- existencia única.

#### a)

$$
2x=1
$$

#### b)

$$
x^2=16
$$

#### c)

$$
3x=12
$$

#### Solución


#### a)

$$
2x=1
$$

no tiene solución entera.

Por tanto, no hay existencia.

#### b)

$$
x^2=16
$$

tiene al menos dos soluciones enteras:

$$
x=4
\qquad\text{y}\qquad
x=-4.
$$

Por tanto, hay existencia, pero no unicidad.

#### c)

$$
3x=12
$$

tiene la solución:

$$
x=4.
$$

Si un entero $y$ satisface:

$$
3y=12,
$$

entonces, dividiendo por $3$:

$$
y=4.
$$

Por tanto, hay existencia única.

---

### Expandir \(\exists!\) {#apm-t1-c03-e0193}
Expande completamente:

$$
\exists!x\,P(x)
$$

utilizando solo:

$$
\exists,
\qquad
\forall,
\qquad
\land,
\qquad
\Rightarrow,
\qquad
=.
$$

Después explica la expansión en prosa.

#### Solución


La expansión es:

$$
\boxed{
\exists x\,\bigl(
P(x)\land
\forall y\,(P(y)\Rightarrow y=x)
\bigr).
}
$$

En prosa:

> «Existe un valor $x$ que satisface $P$, y todo valor $y$ que también satisface $P$ debe ser igual a $x$».

La primera parte afirma existencia.

La segunda afirma unicidad.

---

### Formular una existencia única {#apm-t1-c03-e0194}
Trabajamos con valores enteros.

Escribe simbólicamente:

> «Existe un único entero cuyo doble es igual a $10$».

Después:

#### a)

escribe la forma abreviada;

#### b)

expándela sin utilizar $\exists!$;

#### c)

identifica el valor único.

#### Solución


#### a)

La forma abreviada es:

$$
\boxed{
\exists!x\,(2x=10).
}
$$

#### b)

La expansión es:

$$
\boxed{
\exists x\,\bigl(
2x=10
\land
\forall y\,(2y=10\Rightarrow y=x)
\bigr).
}
$$

#### c)

El valor:

$$
x=5
$$

satisface:

$$
2\cdot5=10.
$$

Si:

$$
2y=10,
$$

entonces, dividiendo por $2$:

$$
y=5.
$$

Por tanto, el único entero que satisface la condición es:

$$
\boxed{5}.
$$

---

## Síntesis

La afirmación:

$$
\exists x\,P(x)
$$

dice:

> «Hay al menos uno».

La afirmación:

$$
\exists!x\,P(x)
$$

dice:

> «Hay exactamente uno».

La segunda abrevia:

$$

\exists x\,\bigl(
P(x)\land
\forall y\,(P(y)\Rightarrow y=x)
\bigr).

$$

Su estructura contiene dos exigencias:

$$

\text{existencia}
+
\text{unicidad}.

$$

La existencia exige un valor que satisfaga la condición.

La unicidad exige que cualquier otro valor que también la satisfaga coincida con el primero.

Por tanto:

$$

\text{encontrar un ejemplo}
\neq
\text{establecer unicidad}.

$$

También vimos que la unicidad depende del dominio. Con esto ya disponemos de casi todo el vocabulario cuantificacional elemental del capítulo.

Las dos secciones finales se dedicarán a **integrarlo**.

## Hacia la sección siguiente

Una fórmula como:

$$
\neg\forall x\,\exists y\,R(x,y)
$$

combina:

- negación;
- dos cuantificadores;
- alcance;
- orden.

Ya sabemos qué significa cada pieza por separado. El siguiente paso será aprender a leer y transformar fórmulas de este tipo sin perder su estructura.
