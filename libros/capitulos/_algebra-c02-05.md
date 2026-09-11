## §5. Tablas de verdad como instrumento semántico

Hasta ahora hemos evaluado fórmulas para asignaciones concretas.

Por ejemplo, si:

$$
p=\mathrm V,
\qquad
q=\mathrm F,
$$

podemos calcular:

$$
p\Rightarrow q=\mathrm F.
$$

Pero una fórmula como:

$$
\neg(p\land q)\lor r
$$

contiene tres variables proposicionales.

Cada una puede recibir:

$$
\mathrm V
$$

o:

$$
\mathrm F.
$$

Si queremos comprender **todo el comportamiento semántico** de la fórmula, no basta con elegir una o dos asignaciones convenientes.

Necesitamos considerar **todas** las posibilidades.

Ese es el propósito de una tabla de verdad.

La idea no es:

$$
\boxed{\text{probar algunos casos}}
$$

sino:

$$
\boxed{\text{enumerar exhaustivamente todas las asignaciones posibles}.}
$$

---

### 5.1 Asignaciones de valores de verdad

::: {.ma-block .ma-definicion #apm-t1-c02-d0017}
**Definición — Asignación de valores de verdad**

Una **asignación de valores de verdad** para unas variables proposicionales consiste en elegir para cada una de ellas uno de los dos valores:

$$
\mathrm V
\qquad\text{o}\qquad
\mathrm F.
$$
:::

Por ejemplo, para:

$$
p,
\qquad
q,
$$

una asignación posible es:

$$
p=\mathrm V,
\qquad
q=\mathrm F.
$$

Otra es:

$$
p=\mathrm F,
\qquad
q=\mathrm F.
$$

La tabla de verdad de una fórmula debe contener todas las asignaciones posibles de las variables que intervienen en ella.

---

### 5.2 ¿Cuántas filas necesitamos?

Comencemos con una sola variable:

$$
p.
$$

Tiene dos posibilidades:

| $p$ |
|---|
| $\mathrm V$ |
| $\mathrm F$ |

Por tanto, necesitamos:

$$
2
$$

filas.

Ahora consideremos dos variables:

$$
p,
\qquad
q.
$$

Por cada valor posible de $p$, la variable $q$ puede ser verdadera o falsa.

Obtenemos:

| $p$ | $q$ |
|---|---|
| $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ |

Hay:

$$
4=2^2
$$

filas.

Con tres variables:

$$
p,
\qquad
q,
\qquad
r,
$$

cada una tiene dos elecciones posibles.

El número total de asignaciones es:

$$
2\cdot2\cdot2=2^3=8.
$$

En general, si una fórmula contiene:

$$
n
$$

variables proposicionales distintas, hay:

$$
\boxed{2^n}
$$

asignaciones posibles.

La razón es sencilla: cada nueva variable duplica el número de filas.

---

### 5.3 Cómo generar las filas sin olvidar ninguna

Para tres variables utilizaremos normalmente este orden:

| $p$ | $q$ | $r$ |
|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm V$ | $\mathrm F$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |

Observemos el patrón:

- $p$ cambia cada cuatro filas;
- $q$ cambia cada dos filas;
- $r$ cambia en cada fila.

Esto garantiza que aparecen exactamente una vez las ocho combinaciones posibles.

::: {.ma-block .ma-intuicion}
**Idea clave**

El orden concreto de las filas no cambia la semántica de la fórmula. Lo esencial es que todas las asignaciones aparezcan exactamente una vez.
:::

Usaremos este orden estándar porque facilita revisar tablas y compararlas.

---

### 5.4 Una tabla se construye por subfórmulas

Consideremos:

$$
\neg(p\land q)\lor r.
$$

No conviene intentar evaluar toda la fórmula de un solo salto.

Primero identificamos su estructura.

El conectivo principal es:

$$
\lor.
$$

Las dos partes principales son:

$$
\neg(p\land q)
$$

y:

$$
r.
$$

Dentro de la primera aparece:

$$
p\land q.
$$

Por tanto, un orden natural de columnas es:

1. $p$;
2. $q$;
3. $r$;
4. $p\land q$;
5. $\neg(p\land q)$;
6. $\neg(p\land q)\lor r$.

Así trasladamos a una tabla el mismo principio que venimos usando:

$$
\boxed{
\text{estructura}
\longrightarrow
\text{subfórmulas}
\longrightarrow
\text{evaluación}.
}
$$

---

### 5.5 Columnas auxiliares

Llamaremos **columnas auxiliares** a las columnas que calculamos para subfórmulas antes de llegar a la fórmula completa.

Por ejemplo:

| $p$ | $q$ | $p\land q$ | $\neg(p\land q)$ |
|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ |

La columna:

$$
p\land q
$$

es necesaria para obtener:

$$
\neg(p\land q).
$$

Las columnas auxiliares cumplen dos funciones:

1. hacen visible la estructura de la fórmula;
2. permiten revisar cada paso si aparece un error.

Una tabla con menos columnas puede ser correcta, pero no siempre será pedagógicamente mejor.

En este libro preferiremos mostrar las subfórmulas relevantes mientras estamos aprendiendo el procedimiento.

---

### 5.6 Algoritmo de construcción

Para construir una tabla de verdad completa seguiremos este procedimiento.

#### Paso 1 — Identificar las variables proposicionales distintas

Por ejemplo, en:

$$
\neg(p\land q)\lor r
$$

aparecen:

$$
p,
\qquad
q,
\qquad
r.
$$

Por tanto:

$$
n=3.
$$

#### Paso 2 — Determinar el número de filas

Necesitamos:

$$
2^3=8
$$

filas.

#### Paso 3 — Escribir todas las asignaciones

Sin repeticiones y sin omisiones.

#### Paso 4 — Identificar las subfórmulas relevantes

Aquí:

$$
p\land q,
$$

$$
\neg(p\land q),
$$

y finalmente:

$$
\neg(p\land q)\lor r.
$$

#### Paso 5 — Completar las columnas desde dentro hacia fuera

Primero las subfórmulas interiores.

Al final, el conectivo principal.

#### Paso 6 — Revisar la tabla

Comprobar:

- que hay exactamente $2^n$ filas;
- que ninguna asignación falta;
- que ninguna aparece dos veces;
- que cada columna se calculó a partir de columnas ya conocidas;
- que la última columna corresponde a la fórmula completa.

Podemos condensarlo:

$$
\boxed{
\text{variables}
\to
\text{filas}
\to
\text{subfórmulas}
\to
\text{columnas auxiliares}
\to
\text{columna final}.
}
$$

---

### 5.7 Una tabla no es una muestra

Supongamos que queremos estudiar una fórmula con tres variables.

Si calculamos únicamente:

$$
p=\mathrm V,
\qquad
q=\mathrm V,
\qquad
r=\mathrm V,
$$

hemos estudiado una sola de:

$$
8
$$

asignaciones.

Aunque la fórmula resulte verdadera en esa fila, no sabemos todavía qué sucede en las otras siete.

Lo mismo ocurre si comprobamos tres, cuatro o incluso siete filas.

Una tabla de verdad completa tiene fuerza semántica porque **no deja ninguna asignación fuera**.

Por eso existe una diferencia esencial entre:

$$
\boxed{\text{ejemplos}}
$$

y:

$$
\boxed{\text{enumeración exhaustiva}.}
$$

Esta distinción será decisiva en la sección siguiente.

---

### 5.8 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-t1-c02-x0013}
**Ejemplo — Tabla completa de una fórmula de tres variables**

:::

Construyamos la tabla de:

$$
\neg(p\land q)\lor r.
$$

#### Paso 1 — Variables

Aparecen tres:

$$
p,
\qquad
q,
\qquad
r.
$$

Por tanto:

$$
2^3=8
$$

filas.

#### Paso 2 — Estructura

Calcularemos:

$$
p\land q,
$$

después:

$$
\neg(p\land q),
$$

y finalmente:

$$
\neg(p\land q)\lor r.
$$

#### Paso 3 — Tabla

| $p$ | $q$ | $r$ | $p\land q$ | $\neg(p\land q)$ | $\neg(p\land q)\lor r$ |
|---|---|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |

#### Paso 4 — Leer la columna final

La fórmula es falsa únicamente en la asignación:

$$
p=\mathrm V,
\qquad
q=\mathrm V,
\qquad
r=\mathrm F.
$$

En las otras siete asignaciones es verdadera.

Todavía no necesitamos poner un nombre especial a este comportamiento.

Por ahora basta con haber determinado exhaustivamente qué ocurre.

---

## Ejercicios

### Generar todas las asignaciones {#apm-t1-c02-e0083}

#### a)

Escribe todas las asignaciones posibles para:

$$
p,
\qquad
q.
$$

#### b)

¿Cuántas son?

#### c)

Escribe todas las asignaciones posibles para:

$$
p,
\qquad
q,
\qquad
r.
$$

#### d)

¿Cuántas son?

#### Solución

#### a)

| $p$ | $q$ |
|---|---|
| $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ |

#### b)

Hay:

$$
2^2=4
$$

asignaciones.

#### c)

| $p$ | $q$ | $r$ |
|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm V$ | $\mathrm F$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |

#### d)

Hay:

$$
2^3=8
$$

asignaciones.

---

### Tabla de dos variables {#apm-t1-c02-e0084}

Construye la tabla completa de:

$$
\neg p\lor q.
$$

#### Solución

Usamos las columnas:

$$
p,
\qquad
q,
\qquad
\neg p,
\qquad
\neg p\lor q.
$$

| $p$ | $q$ | $\neg p$ | $\neg p\lor q$ |
|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |

---

### Tres variables y dos niveles {#apm-t1-c02-e0085}

Construye la tabla de:

$$
(p\lor q)\land\neg r.
$$

#### Solución

Necesitamos ocho filas.

Las columnas auxiliares serán:

$$
p\lor q
$$

y:

$$
\neg r.
$$

| $p$ | $q$ | $r$ | $p\lor q$ | $\neg r$ | $(p\lor q)\land\neg r$ |
|---|---|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ |

---

### Una tabla con implicación {#apm-t1-c02-e0086}

Construye la tabla de:

$$
(p\land q)\Rightarrow p.
$$

#### Solución

Primero calculamos:

$$
p\land q.
$$

| $p$ | $q$ | $p\land q$ | $(p\land q)\Rightarrow p$ |
|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ |

La columna final contiene:

$$
\mathrm V
$$

en las cuatro filas.

Guardaremos esta observación para la sección siguiente.

---

### ¿Por qué aparecen $2^n$ filas? {#apm-t1-c02-e0087}

Explica por qué una fórmula que contiene cuatro variables proposicionales distintas requiere:

$$
2^4=16
$$

filas en una tabla de verdad completa.

No basta con escribir el resultado: explica la razón.

#### Solución

Cada variable proposicional tiene dos valores posibles:

$$
\mathrm V
\qquad\text{o}\qquad
\mathrm F.
$$

Con una variable tenemos dos posibilidades.

Al añadir una segunda variable, cada posibilidad anterior se divide en dos, por lo que obtenemos:

$$
2\cdot2.
$$

Al añadir una tercera:

$$
2\cdot2\cdot2.
$$

Y con cuatro:

$$
2\cdot2\cdot2\cdot2
=
2^4
=
16.
$$

Cada nueva variable duplica el número de asignaciones.

---

### Diagnosticar una tabla incompleta {#apm-t1-c02-e0088}

Un estudiante quiere construir una tabla para una fórmula con tres variables y escribe únicamente estas filas:

| $p$ | $q$ | $r$ |
|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |

Afirma:

> «Hay valores verdaderos y falsos para cada variable, así que ya consideré todos los casos».

Explica el error.

#### Solución

Tener alguna aparición de:

$$
\mathrm V
$$

y:

$$
\mathrm F
$$

en cada columna no basta.

Con tres variables existen:

$$
2^3=8
$$

asignaciones diferentes.

El estudiante solo escribió cuatro.

Faltan, por ejemplo:

$$
(\mathrm V,\mathrm V,\mathrm F),
$$

$$
(\mathrm V,\mathrm F,\mathrm F),
$$

$$
(\mathrm F,\mathrm V,\mathrm V),
$$

y:

$$
(\mathrm F,\mathrm F,\mathrm V).
$$

Una tabla completa debe enumerar **cada combinación posible**, no solo utilizar ambos valores en cada variable.

---

### Síntesis: implicación y contraposición asociada {#apm-t1-c02-e0089}

Construye una tabla completa para:

$$
(p\Rightarrow q)
\leftrightarrow
(\neg q\Rightarrow\neg p).
$$

Usa columnas auxiliares suficientes para que cada paso pueda revisarse.

Después describe qué observas en la columna final, sin utilizar todavía ningún término técnico nuevo.

#### Solución

Necesitamos las columnas:

$$
\neg q,
$$

$$
\neg p,
$$

$$
p\Rightarrow q,
$$

$$
\neg q\Rightarrow\neg p,
$$

y finalmente el bicondicional.

| $p$ | $q$ | $\neg p$ | $\neg q$ | $p\Rightarrow q$ | $\neg q\Rightarrow\neg p$ | $(p\Rightarrow q)\leftrightarrow(\neg q\Rightarrow\neg p)$ |
|---|---|---|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |

La columna final recibe:

$$
\mathrm V
$$

en las cuatro asignaciones.

Además, las columnas:

$$
p\Rightarrow q
$$

y:

$$
\neg q\Rightarrow\neg p
$$

coinciden fila por fila.

Todavía no necesitamos poner un nombre técnico a estos dos hechos.

En las secciones siguientes estudiaremos precisamente qué significa que una fórmula sea verdadera en todas las asignaciones y qué significa que dos fórmulas tengan columnas idénticas.

---

## Síntesis

Una tabla de verdad enumera exhaustivamente las asignaciones de valores de verdad de las variables proposicionales de una fórmula.

Si aparecen:

$$
n
$$

variables distintas, necesitamos:

$$
\boxed{2^n}
$$

filas.

La construcción sigue un orden estructural:

$$
\boxed{
\text{variables}
\to
\text{todas las asignaciones}
\to
\text{subfórmulas}
\to
\text{columnas auxiliares}
\to
\text{fórmula completa}.
}
$$

El hábito que debemos evitar es:

> «He probado varias filas; probablemente las demás se comportan igual».

Una tabla de verdad completa no se apoya en una muestra.

Su fuerza está en que:

$$
\boxed{\text{no deja ninguna asignación fuera}.}
$$

---

## Hacia la sección siguiente

En [el ejercicio «Una tabla con implicación»](#apm-t1-c02-e0086) apareció una fórmula cuya columna final contiene:

$$
\mathrm V
$$

en todas las filas.

En [el ejercicio «Síntesis: implicación y contraposición asociada»](#apm-t1-c02-e0089) ocurrió lo mismo con una fórmula más compleja.

También podríamos encontrar fórmulas que sean falsas en todas las filas, o fórmulas que cambien de valor según la asignación.

Estas tres posibilidades reciben nombres específicos.

La siguiente sección estudiará:
