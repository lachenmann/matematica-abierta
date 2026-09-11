## §1. De una cuenta a una expresión

Hasta ahora, probablemente has visto miles de cuentas como estas:

$$
3+4\cdot5
$$

y

$$
(3+4)\cdot5.
$$

Contienen los mismos tres números y las mismas dos operaciones: una suma y una multiplicación. Sin embargo, sus valores son distintos:

$$
3+4\cdot5=23,
$$

mientras que

$$
(3+4)\cdot5=35.
$$

Podríamos explicar la diferencia diciendo simplemente que «la multiplicación se hace antes que la suma» y que los paréntesis cambian el orden de las operaciones. Esa explicación es correcta, pero para nuestro propósito se queda corta.

Queremos aprender a mirar una escritura algebraica de otra manera.

La diferencia esencial entre las dos expresiones anteriores no está solamente en **qué operación hacemos primero**, sino en **cómo está organizada la expresión**.

En

$$
3+4\cdot5,
$$

la multiplicación $4\cdot5$ forma una unidad dentro de una suma mayor:

$$
3+(4\cdot5).
$$

En cambio, en

$$
(3+4)\cdot5,
$$

la suma $3+4$ forma una unidad dentro de una multiplicación mayor:

$$
(3+4)\cdot5.
$$

En el primer caso, la expresión completa tiene la forma

$$
\boxed{\text{número}+\text{producto}},
$$

mientras que, en el segundo, tiene la forma

$$
\boxed{\text{suma}\cdot\text{número}}.
$$

Este será nuestro primer cambio de perspectiva:

::: {.ma-block .ma-intuicion}
**Idea clave**

Antes de calcular una expresión, conviene aprender a **leer su estructura**.
:::

---

### 1.1 Una cuenta tiene arquitectura

Considera ahora:

$$
7-2\cdot3.
$$

Sabemos calcularla:

$$
7-2\cdot3
=
7-6
=
1.
$$

Pero no queremos comenzar calculando. Queremos preguntar primero:

> ¿Cómo está construida esta expresión?

La parte

$$
2\cdot3
$$

es una multiplicación. La expresión completa es

$$
7-(2\cdot3).
$$

Por tanto, la operación que organiza la expresión completa es la resta.

Diremos, de manera todavía informal, que la **operación principal** es la operación que une las partes más grandes de la expresión.

En

$$
7-2\cdot3,
$$

la operación principal es la resta.

En cambio, en

$$
(7-2)\cdot3,
$$

la operación principal es la multiplicación, porque las dos grandes partes son

$$
(7-2)
\qquad\text{y}\qquad
3.
$$

Esta distinción parece muy sencilla, pero será fundamental cuando las expresiones sean mucho más largas.

Por ejemplo:

$$
5\bigl(2+(3-1)\bigr).
$$

Podemos leerla desde fuera hacia dentro.

La operación principal es la multiplicación:

$$
5
\cdot
\bigl(2+(3-1)\bigr).
$$

Dentro del segundo factor aparece la suma

$$
2+(3-1),
$$

y dentro de esa suma aparece la resta

$$
3-1.
$$

La expresión posee, por tanto, varios niveles.

Una forma útil de representarlos es:

```text
multiplicación
├── 5
└── suma
    ├── 2
    └── resta
        ├── 3
        └── 1
```

No necesitamos convertir estos diagramas en una teoría formal. Por ahora basta aprender la idea:

$$
\boxed{
\text{una expresión puede contener otras expresiones dentro de ella}.
}
$$

A esas partes internas las llamaremos **subexpresiones**.

---

### 1.2 Expresión y valor

Hasta aquí hemos usado la palabra «expresión» varias veces. Conviene fijar qué entenderemos por ella.

::: {.ma-block .ma-definicion #apm-t1-c01-d0001}
**Definición — Expresión matemática**

Una **expresión matemática** es una combinación de símbolos construida de acuerdo con ciertas reglas de escritura y destinada a representar un objeto o un valor matemático.
:::

En este capítulo trabajaremos sobre todo con expresiones que representan números.

Por ejemplo,

$$
3+4\cdot5
$$

es una expresión.

Al calcularla obtenemos:

$$
23.
$$

Decimos entonces que el **valor** de la expresión es $23$.

Conviene distinguir cuidadosamente estos dos niveles:

- la **expresión** es la escritura que representa;
- el **valor** es el número representado por esa escritura.

Así,

$$
3+4\cdot5
$$

y

$$
20+3
$$

son expresiones distintas, pero ambas tienen el mismo valor:

$$
23.
$$

También la escritura

$$
23
$$

es, por sí misma, una expresión muy sencilla que representa ese mismo número.

Por eso, cuando digamos informalmente

$$
\boxed{\text{expresión}\neq\text{valor}},
$$

no queremos afirmar que un número como $23$ no pueda aparecer escrito como expresión. Queremos recordar una distinción conceptual: **una cosa es la representación simbólica y otra el objeto que esa representación denota**.

Esta distinción será cada vez más importante.

---

### 1.3 Leer de fuera hacia dentro

Una estrategia especialmente útil consiste en buscar primero la estructura exterior.

Consideremos:

$$
18\div(2+4).
$$

Antes de calcular, preguntamos:

1. ¿Cuál es la operación principal?
2. ¿Cuáles son sus dos partes?

La operación principal es la división:

$$
\frac{18}{2+4}.
$$

Sus dos partes son:

$$
18
\qquad\text{y}\qquad
2+4.
$$

Solo después analizamos la segunda parte, cuya operación principal es la suma.

Finalmente calculamos:

$$
\frac{18}{2+4}
=
\frac{18}{6}
=
3.
$$

El orden mental que estamos practicando es:

$$
\boxed{
\text{leer la estructura}
\longrightarrow
\text{identificar las partes}
\longrightarrow
\text{calcular}.
}
$$

No es una regla destinada a hacer más lenta una cuenta sencilla. Es un entrenamiento para cuando las expresiones dejen de ser sencillas.

---

### 1.4 Mini ejemplo: la importancia del signo exterior

Mira las dos expresiones:

$$
20-(6+3)
$$

y

$$
(20-6)+3.
$$

En la primera, la operación principal es la resta:

$$
20-\boxed{(6+3)}.
$$

Su valor es

$$
20-9=11.
$$

En la segunda, la suma es la operación principal:

$$
\boxed{(20-6)}+3.
$$

Su valor es

$$
14+3=17.
$$

Los mismos números y los mismos signos pueden describir estructuras diferentes.

---

### 1.5 Mini ejemplo: una potencia dentro de una suma

Considera:

$$
2+3^2.
$$

La potencia

$$
3^2
$$

es una subexpresión.

La expresión completa tiene la forma

$$
2+(3^2),
$$

de modo que su operación principal es la suma.

Después de leerla podemos calcular:

$$
2+3^2
=
2+9
=
11.
$$

En cambio,

$$
(2+3)^2
$$

tiene como operación exterior la potenciación:

$$
(2+3)^2=5^2=25.
$$

Una vez más, los paréntesis no son un adorno tipográfico. Revelan la estructura.

---

### 1.6 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-t1-c01-x0001}
**Ejemplo — Los mismos símbolos, dos estructuras**

:::

Comparemos:

$$
8-3\cdot2
$$

y

$$
(8-3)\cdot2.
$$

#### Primera expresión

Tenemos:

$$
8-3\cdot2.
$$

La multiplicación

$$
3\cdot2
$$

forma una subexpresión. La estructura exterior es:

$$
8-(3\cdot2).
$$

Por tanto, la operación principal es la resta.

Ahora calculamos:

$$
8-3\cdot2
=
8-6
=
2.
$$

#### Segunda expresión

Tenemos:

$$
(8-3)\cdot2.
$$

La resta

$$
8-3
$$

forma una subexpresión. La estructura exterior es:

$$
(8-3)\cdot2.
$$

Por tanto, la operación principal es la multiplicación.

Ahora calculamos:

$$
(8-3)\cdot2
=
5\cdot2
=
10.
$$

#### Comparación

Las expresiones contienen los mismos números:

$$
8,\quad3,\quad2,
$$

y los mismos signos de resta y multiplicación. Pero los paréntesis determinan estructuras distintas:

$$
8-(3\cdot2)
$$

frente a

$$
(8-3)\cdot2.
$$

Por eso sus valores son distintos:

$$
2\neq10.
$$

La lección no es solamente «respeta el orden de las operaciones». Es más profunda:

$$
\boxed{
\text{el significado de una expresión depende de su estructura}.
}
$$

---

## Ejercicios

### Operación principal {#apm-t1-c01-e0001}

En cada expresión, identifica la operación principal. No calcules todavía.

1. $6+2\cdot5$
2. $(6+2)\cdot5$
3. $18-(4+3)$
4. $\dfrac{24}{3+5}$
5. $2+(3+4)^2$

#### Solución

**1.**

$$
6+2\cdot5
=
6+(2\cdot5).
$$

La multiplicación $2\cdot5$ es una subexpresión. La operación exterior es la suma.

**Operación principal:** suma.

**2.**

$$
(6+2)\cdot5.
$$

Las dos partes mayores son $(6+2)$ y $5$, unidas por un producto.

**Operación principal:** multiplicación.

**3.**

$$
18-(4+3).
$$

La suma $4+3$ está dentro de los paréntesis. La expresión completa resta esa suma a $18$.

**Operación principal:** resta.

**4.**

$$
\frac{24}{3+5}.
$$

El numerador es $24$ y el denominador es $3+5$. La expresión completa es un cociente.

**Operación principal:** división.

**5.**

$$
2+(3+4)^2.
$$

La potencia $(3+4)^2$ es una de las dos partes de una suma exterior:

$$
2+\bigl((3+4)^2\bigr).
$$

**Operación principal:** suma.

---

### Los paréntesis cambian la estructura {#apm-t1-c01-e0002}

Usa los números $2$, $3$ y $4$, en ese orden, y los signos $+$ y $\cdot$.

1. Escribe una expresión cuyo valor sea $14$.
2. Escribe otra, con los mismos símbolos básicos, cuyo valor sea $20$.
3. Explica por qué los valores son distintos.

#### Solución

Para obtener $14$ podemos escribir:

$$
2+3\cdot4.
$$

La multiplicación se encuentra dentro de una suma:

$$
2+(3\cdot4),
$$

por lo que

$$
2+3\cdot4
=
2+12
=
14.
$$

Para obtener $20$ escribimos:

$$
(2+3)\cdot4.
$$

Ahora la suma está dentro de una multiplicación:

$$
(2+3)\cdot4
=
5\cdot4
=
20.
$$

Los valores son distintos porque las expresiones tienen estructuras distintas. En la primera, la operación principal es la suma; en la segunda, es la multiplicación.

---

### Expresión y valor {#apm-t1-c01-e0003}

Para cada expresión:

1. describe su estructura exterior;
2. identifica una subexpresión;
3. calcula su valor.

#### a)

$$
15-(2+5)
$$

#### b)

$$
3(4+2)
$$

#### c)

$$
5+2^3
$$

#### Solución

#### a)

La expresión es:

$$
15-(2+5).
$$

Su estructura exterior es una resta. Una subexpresión es:

$$
2+5.
$$

Calculamos:

$$
15-(2+5)
=
15-7
=
8.
$$

El valor de la expresión es $8$.

#### b)

La expresión es:

$$
3(4+2).
$$

Su estructura exterior es una multiplicación. Una subexpresión es:

$$
4+2.
$$

Calculamos:

$$
3(4+2)
=
3\cdot6
=
18.
$$

El valor es $18$.

#### c)

La expresión es:

$$
5+2^3.
$$

Su estructura exterior es una suma. Una subexpresión es:

$$
2^3.
$$

Calculamos:

$$
5+2^3
=
5+8
=
13.
$$

El valor es $13$.

---

### Una expresión en palabras {#apm-t1-c01-e0004}

Describe con palabras la estructura de:

$$
5\bigl(2+3^2\bigr).
$$

Después calcula su valor.

#### Solución

Primero leemos desde fuera.

La operación principal es una multiplicación. Sus dos factores son:

$$
5
$$

y

$$
2+3^2.
$$

Dentro del segundo factor, la operación principal es una suma. Sus dos partes son:

$$
2
$$

y

$$
3^2.
$$

Dentro de esa suma aparece la potencia $3^2$.

Podemos describir la expresión como:

> cinco multiplicado por la suma de dos y el cuadrado de tres.

Solo después calculamos:

$$
5\bigl(2+3^2\bigr)
=
5(2+9)
=
5\cdot11
=
55.
$$

---

### Construcción {#apm-t1-c01-e0005}

Construye dos expresiones diferentes que:

- usen exactamente una vez los números $2$, $5$ y $6$;
- usen una suma y una multiplicación;
- tengan operaciones principales distintas.

Calcula luego sus valores y explica la diferencia estructural.

#### Solución

Una posibilidad es:

$$
2+5\cdot6
$$

y

$$
(2+5)\cdot6.
$$

En la primera expresión, la operación principal es la suma:

$$
2+(5\cdot6).
$$

Su valor es:

$$
2+5\cdot6
=
2+30
=
32.
$$

En la segunda, la operación principal es la multiplicación:

$$
(2+5)\cdot6.
$$

Su valor es:

$$
(2+5)\cdot6
=
7\cdot6
=
42.
$$

La diferencia no proviene de los números ni de las operaciones utilizadas, que son los mismos. Proviene de la manera en que esas operaciones están organizadas.

---

## Resumen de la sección

En esta primera sección hemos introducido una idea sencilla pero decisiva: una cuenta no es solo una secuencia de símbolos que debemos procesar.

Una expresión posee estructura.

Hemos aprendido a:

- identificar la operación principal;
- reconocer subexpresiones;
- leer una expresión de fuera hacia dentro;
- entender el papel estructural de los paréntesis;
- distinguir entre una expresión y el valor que representa.

La definición fundamental de la sección es:

::: {.ma-block .ma-observacion}
**Síntesis**

Una **expresión matemática** es una combinación de símbolos construida de acuerdo con ciertas reglas de escritura y destinada a representar un objeto o un valor matemático.
:::

El hábito que queremos conservar es:

$$
\boxed{
\text{leer}
\longrightarrow
\text{comprender la estructura}
\longrightarrow
\text{calcular}.
}
$$

---

## Hacia la sección siguiente

Todas las expresiones que hemos usado hasta ahora contienen números concretos:

$$
3,\quad5,\quad18,\quad24,\ldots
$$

Pero el álgebra comienza a mostrar toda su potencia cuando podemos hablar de un número **sin tener que decidir todavía cuál es**.

En lugar de escribir un número concreto, podemos darle un nombre:

$$
x,\qquad a,\qquad n.
$$

¿Qué significa exactamente una letra dentro de una expresión?

¿Es siempre una cantidad desconocida?

¿Tiene que «cambiar»?

¿Puede representar un número fijo?

Estas serán las preguntas de la siguiente sección:
