## §7. Equivalencia lógica

En [el ejercicio «Síntesis: implicación y contraposición asociada»](#apm-i-e0089) construimos una tabla para: $p\Rightarrow q$ y $\neg q\Rightarrow\neg p$.

Obtuvimos:

| $p$ | $q$ | $p\Rightarrow q$ | $\neg q\Rightarrow\neg p$ |
|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |

Las dos fórmulas tienen formas distintas.

Sin embargo, sus columnas coinciden fila por fila. Eso sugiere una idea nueva.

Hasta ahora preguntábamos:

> «¿Qué valor de verdad recibe una fórmula?»

Ahora preguntaremos:

> «¿Pueden dos fórmulas distintas tener exactamente el mismo comportamiento bajo todas las asignaciones?»

La respuesta es sí. Y esta será la noción que convertirá poco a poco la lógica proposicional en un **álgebra de fórmulas**.

---

### 7.1 Misma columna, mismo comportamiento lógico

Consideremos dos fórmulas: $P$ y $Q$ Para compararlas debemos construir una tabla conjunta que incluya todas las variables proposicionales que aparezcan en cualquiera de las dos.

Supongamos que, fila por fila, ocurre siempre:

- cuando $P$ recibe $\mathrm V$, también $Q$ recibe $\mathrm V$;
- cuando $P$ recibe $\mathrm F$, también $Q$ recibe $\mathrm F$.

Entonces las columnas de: $P$ y $Q$ son idénticas.

No significa necesariamente que las fórmulas tengan la misma escritura.

Significa que **ninguna asignación de valores de verdad permite distinguirlas semánticamente**.

---

### 7.2 Equivalencia lógica

::: {.ma-block .ma-definicion #apm-i-d0021}
**Definición — Equivalencia lógica**

Dos fórmulas proposicionales $P$ y $Q$ son **lógicamente equivalentes** cuando reciben el mismo valor de verdad en cada asignación de valores de verdad de todas las variables que aparecen en $P$ o en $Q$.

Escribiremos:

$$
P\equiv Q.
$$
:::

Por tanto:

$$
\boxed{
P\equiv Q
\quad\text{significa que las columnas de }P\text{ y }Q
\text{ coinciden fila por fila}.
}
$$

Esta definición contiene una exigencia fuerte. No basta con encontrar:

- una fila donde coincidan;
- varias filas donde coincidan;
- casi todas las filas donde coincidan.

Para afirmar:

$$
P\equiv Q,
$$

las columnas deben coincidir en **toda** la tabla conjunta.

---

### 7.3 Cómo refutar una pretendida equivalencia

Supongamos que alguien afirma $P\equiv Q$ Para refutarlo basta encontrar una asignación donde: $P$ y $Q$ reciban valores distintos.

Por ejemplo, comparemos: $p\lor q$ y $p\land q$. Tomemos:

$$
p=\mathrm V,
\qquad
q=\mathrm F.
$$

Entonces $p\lor q=\mathrm V$, mientras que:

$$
p\land q=\mathrm F.
$$

Por tanto: $p\lor q$ y $p\land q$ no son lógicamente equivalentes.

No necesitamos completar las otras tres filas para refutar la equivalencia.

La asignación:

$$
p=\mathrm V,
\qquad
q=\mathrm F
$$

funciona como **contraasignación**. Así:

$$

\text{una sola fila distinta refuta una pretendida equivalencia}.

$$

---

### 7.4 Bicondicional y equivalencia lógica no son lo mismo

Esta es una distinción central del capítulo. La escritura $P\leftrightarrow Q$ es una **fórmula proposicional**.

En cada asignación recibe: $\mathrm V$ o $\mathrm F$.

En cambio, $P\equiv Q$ expresa que las fórmulas $P$ y $Q$ tienen la misma columna completa.

En este capítulo, $\equiv$ pertenece al lenguaje con el que **hablamos acerca de las fórmulas**: no añadimos una columna «$P\equiv Q$» a la tabla como si fuera un nuevo conectivo. Para verificarlo, comparamos las columnas de $P$ y $Q$.

Podemos resumir:

| Escritura | Función |
|---|---|
| $P\leftrightarrow Q$ | fórmula proposicional |
| $P\equiv Q$ | afirmación de equivalencia lógica entre fórmulas |

Por ejemplo, en una asignación concreta puede ocurrir:

$$
P\leftrightarrow Q=\mathrm V.
$$

Eso solo nos dice que $P$ y $Q$ tienen el mismo valor **en esa fila**.

Todavía no permite concluir:

$$
P\equiv Q.
$$

Para esta última afirmación debemos comparar todas las filas.

::: {.ma-block .ma-intuicion}
**Idea clave**

El bicondicional compara los valores de $P$ y $Q$ **dentro de una asignación**.

La equivalencia lógica exige que esa coincidencia se mantenga **a través de todas las asignaciones**.
:::

---

### 7.5 El criterio mediante el bicondicional

La relación entre ambas ideas es, sin embargo, muy estrecha.

Si:

$$
P\equiv Q,
$$

entonces en cada fila $P$ y $Q$ tienen el mismo valor.

Pero el bicondicional:

$$
P\leftrightarrow Q
$$

es verdadero precisamente cuando sus dos componentes tienen el mismo valor.

Por tanto, si $P$ y $Q$ son equivalentes, el bicondicional debe ser verdadero en todas las filas.

Eso significa que:

$$
P\leftrightarrow Q
$$

es una tautología. Y el razonamiento también funciona en la dirección inversa.

Podemos formularlo como nuestro primer resultado formal del capítulo.

::: {.ma-block .ma-enunciado #apm-i-p0001}
**Proposición — Criterio bicondicional para la equivalencia lógica**

Sean $P$ y $Q$ fórmulas proposicionales. Entonces $P$ y $Q$ son lógicamente equivalentes si y solo si:

$$
P\leftrightarrow Q
$$

es una tautología.
:::

#### Lectura del resultado

La proposición conecta dos niveles:

1. comparar directamente las columnas de $P$ y $Q$;
2. construir una nueva fórmula $P\leftrightarrow Q$ y observar su columna.

Afirma que ambos procedimientos contienen exactamente la misma información.

#### Demostración

Construimos una tabla conjunta con todas las variables que aparecen en $P$ o en $Q$.

##### Primera dirección

Supongamos que:

$$
P\equiv Q.
$$

Por definición, en cada fila de la tabla conjunta, $P$ y $Q$ reciben el mismo valor de verdad.

Pero:

$$
P\leftrightarrow Q
$$

recibe $\mathrm V$ exactamente cuando $P$ y $Q$ tienen el mismo valor.

En cada fila:

$$
P\leftrightarrow Q=\mathrm V.
$$

Así, la columna completa del bicondicional contiene únicamente:

$$
\mathrm V.
$$

Luego:

$$
P\leftrightarrow Q
$$

es una tautología.

##### Segunda dirección

Supongamos ahora que:

$$
P\leftrightarrow Q
$$

es una tautología. Entonces su columna recibe $\mathrm V$ en cada fila de la tabla conjunta.

Por la definición del bicondicional, eso significa que en cada fila: $P$ y $Q$ reciben el mismo valor de verdad.

Por tanto, sus columnas coinciden fila por fila. Luego:

$$
P\equiv Q.
$$

Quedan demostradas las dos direcciones.

$$
\boxed{
P\equiv Q
\quad\text{exactamente cuando}\quad
P\leftrightarrow Q
\text{ es una tautología}.
}
$$

---

### 7.6 Dos procedimientos para demostrar una equivalencia

A partir de ahora tenemos dos procedimientos semánticos muy próximos.

#### Procedimiento A — Comparar columnas

Construimos la tabla de: $P$ y $Q$. Si las columnas coinciden completamente:

$$
P\equiv Q.
$$

#### Procedimiento B — Usar el criterio bicondicional

Construimos:

$$
P\leftrightarrow Q.
$$

Si su columna es toda:

$$
\mathrm V,
$$

entonces, por [la proposición «Criterio bicondicional para la equivalencia lógica»](#apm-i-p0001):

$$
P\equiv Q.
$$

En esta etapa ambos métodos siguen dependiendo de tablas.

Más adelante aprenderemos a demostrar equivalencias mediante **leyes ya establecidas**, sin reconstruir una tabla completa cada vez.

---

### 7.7 Una equivalencia puede cambiar mucho la forma

Consideremos $\neg(p\land q)$ y $\neg p\lor\neg q$. Las fórmulas no se parecen superficialmente.

La primera tiene como conectivo principal:

$$
\neg.
$$

La segunda tiene como conectivo principal:

$$
\lor.
$$

Construyamos una tabla:

| $p$ | $q$ | $p\land q$ | $\neg(p\land q)$ | $\neg p$ | $\neg q$ | $\neg p\lor\neg q$ |
|---|---|---|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |

Las dos columnas destacadas conceptualmente son: $\neg(p\land q)$ y $\neg p\lor\neg q$.

Coinciden fila por fila. Por tanto:

$$
\boxed{
\neg(p\land q)
\equiv
\neg p\lor\neg q.
}
$$

Más adelante este hecho formará parte de una familia de leyes con nombre propio.

Por ahora lo importante es cómo lo hemos establecido: **directamente desde la semántica**.

---

### 7.8 Igualdad y equivalencia tampoco son lo mismo

En álgebra escribimos, por ejemplo:

$$
2(x+1)=2x+2.
$$

Allí:

$$
=
$$

expresa igualdad entre valores matemáticos. En lógica proposicional escribiremos:

$$
\neg(p\land q)
\equiv
\neg p\lor\neg q.
$$

Aquí:

$$
\equiv
$$

expresa equivalencia lógica entre fórmulas. No intercambiaremos ambos símbolos.

La disciplina de notación queda:

$$

=
\neq
\equiv
\neq
\leftrightarrow.

$$

Cada símbolo expresa una relación diferente.

---

### 7.9 Cadenas de equivalencias

Supongamos que ya hemos justificado: $P\equiv Q$ y $Q\equiv R$. En cada fila:

- $P$ y $Q$ tienen el mismo valor;
- $Q$ y $R$ tienen el mismo valor.

En esa misma fila:

- $P$ y $R$ tienen el mismo valor.

Como esto ocurre en toda la tabla conjunta:

$$
P\equiv R.
$$

Esto nos permitirá escribir cadenas como:

$$
P
\equiv
Q
\equiv
R.
$$

Pero aparece una nueva exigencia de rigor:

::: {.ma-block .ma-intuicion}
**Idea clave**

Cada paso de una cadena de equivalencias debe estar justificado.
:::

Todavía conocemos pocas equivalencias reutilizables. Las secciones siguientes construirán precisamente ese repertorio.

---

### 7.10 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-i-x0015}
**Ejemplo — Demostrar una equivalencia por tabla**
:::

Demostremos:

$$
\neg(p\land q)
\equiv
\neg p\lor\neg q.
$$

#### Paso 1 — Variables

Ambas fórmulas dependen de:

$$
p,
\qquad
q.
$$

Necesitamos:

$$
2^2=4
$$

filas.

#### Paso 2 — Subfórmulas

Para la primera fórmula necesitamos:

$$
p\land q
$$

y después:

$$
\neg(p\land q).
$$

Para la segunda necesitamos:

$$
\neg p,
\qquad
\neg q,
$$

y finalmente:

$$
\neg p\lor\neg q.
$$

#### Paso 3 — Tabla conjunta

| $p$ | $q$ | $p\land q$ | $\neg(p\land q)$ | $\neg p$ | $\neg q$ | $\neg p\lor\neg q$ |
|---|---|---|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |

Las columnas de: $\neg(p\land q)$ y $\neg p\lor\neg q$ son idénticas.

#### Conclusión

Por definición de equivalencia lógica:

$$
\boxed{
\neg(p\land q)
\equiv
\neg p\lor\neg q.
}
$$

Además, por [la proposición «Criterio bicondicional para la equivalencia lógica»](#apm-i-p0001), podemos concluir que:

$$
\neg(p\land q)
\leftrightarrow
(\neg p\lor\neg q)
$$

es una tautología.

---
## Ejercicios

### Doble negación por tabla {#apm-i-e0096}
Construye una tabla para comparar:

$$
\neg\neg p
$$

y:

$$
p.
$$

Decide si son lógicamente equivalentes.

#### Solución


| $p$ | $\neg p$ | $\neg\neg p$ |
|---|---|---|
| $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ |

La columna de:

$$
\neg\neg p
$$

coincide con la de:

$$
p.
$$

Por tanto:

$$
\boxed{
\neg\neg p\equiv p.
}
$$

---

### Una fila no basta {#apm-i-e0097}
Un estudiante sabe que, para:

$$
p=\mathrm V,
\qquad
q=\mathrm V,
$$

el bicondicional:

$$
p\leftrightarrow q
$$

es verdadero.

Concluye:

$$
p\equiv q.
$$

Explica el error.

#### Solución


La verdad de:

$$
p\leftrightarrow q
$$

en una sola asignación solo muestra que $p$ y $q$ tienen el mismo valor **en esa fila**.

Para afirmar:

$$
p\equiv q,
$$

sus columnas deben coincidir en todas las asignaciones.

Tomemos:

$$
p=\mathrm V,
\qquad
q=\mathrm F.
$$

Entonces $p$ y $q$ reciben valores distintos.

Por tanto:

$$
p
$$

y:

$$
q
$$

no son lógicamente equivalentes.

---

### Idempotencia descubierta semánticamente {#apm-i-e0098}
Demuestra mediante una tabla que:

$$
p\lor p
\equiv
p.
$$

#### Solución


| $p$ | $p\lor p$ |
|---|---|
| $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ |

Las columnas coinciden en ambas asignaciones.

Por tanto:

$$
\boxed{
p\lor p\equiv p.
}
$$

Más adelante incorporaremos esta equivalencia a un conjunto sistemático de leyes.

---

### Simetría de la equivalencia {#apm-i-e0099}
Supón que ya se ha establecido:

$$
P\equiv Q.
$$

Justifica, usando únicamente la definición, por qué también podemos afirmar:

$$
Q\equiv P.
$$

#### Solución


Si:

$$
P\equiv Q,
$$

entonces las columnas de $P$ y $Q$ coinciden fila por fila.

Pero decir que el valor de $P$ coincide con el de $Q$ en cada fila es exactamente lo mismo que decir que el valor de $Q$ coincide con el de $P$ en cada fila.

Por tanto:

$$
\boxed{
Q\equiv P.
}
$$

No hemos utilizado ninguna ley adicional; solo la definición de equivalencia lógica.

---

### Refutar una equivalencia {#apm-i-e0100}
Alguien propone:

$$
p\lor q
\equiv
p\land q.
$$

Refuta la afirmación con una sola contraasignación.

#### Solución


Tomemos:

$$
p=\mathrm V,
\qquad
q=\mathrm F.
$$

Entonces:

$$
p\lor q=\mathrm V,
$$

mientras que:

$$
p\land q=\mathrm F.
$$

Las fórmulas reciben valores distintos en esta asignación.

Por tanto:

$$
\boxed{
p\lor q
\text{ y }
p\land q
\text{ no son lógicamente equivalentes}.
}
$$

Una sola fila distinta basta para refutar la equivalencia.

---

### Síntesis: una fórmula más simple con la misma columna {#apm-i-e0101}
Decide si:

$$
(p\land q)\lor(p\land\neg q)
$$

es lógicamente equivalente a:

$$
p.
$$

Construye una tabla conjunta y justifica tu conclusión.

#### Solución


Necesitamos calcular:

$$
p\land q,
$$

$$
\neg q,
$$

$$
p\land\neg q,
$$

y finalmente:

$$
(p\land q)\lor(p\land\neg q).
$$

| $p$ | $q$ | $p\land q$ | $\neg q$ | $p\land\neg q$ | $(p\land q)\lor(p\land\neg q)$ | $p$ |
|---|---|---|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |

Las dos últimas columnas coinciden fila por fila.

Por tanto:

$$
\boxed{
(p\land q)\lor(p\land\neg q)
\equiv
p.
}
$$

Por [la proposición «Criterio bicondicional para la equivalencia lógica»](#apm-i-p0001), también sabemos que:

$$
\bigl((p\land q)\lor(p\land\neg q)\bigr)
\leftrightarrow
p
$$

es una tautología.

Esta fórmula muestra por primera vez con claridad la utilidad futura del álgebra proposicional: una fórmula relativamente larga puede tener exactamente el mismo comportamiento lógico que otra mucho más simple.

---

## Síntesis

Dos fórmulas: $P$ y $Q$ son lógicamente equivalentes cuando sus columnas coinciden en toda la tabla conjunta.

Escribimos:

$$

P\equiv Q.

$$

Para demostrar una equivalencia mediante tablas debemos considerar todas las asignaciones.

Para refutarla basta una sola contraasignación donde los valores difieran.

La distinción notacional fundamental es:

$$

P\leftrightarrow Q
\neq
P\equiv Q.

$$

El primero es un bicondicional, es decir, una fórmula.

El segundo expresa equivalencia lógica entre fórmulas. La conexión entre ambos quedó establecida por:

> [la proposición «Criterio bicondicional para la equivalencia lógica»](#apm-i-p0001) — $P$ y $Q$ son lógicamente equivalentes si y solo si $P\leftrightarrow Q$ es una tautología.

Con esta proposición cerramos el bloque puramente semántico del capítulo.

---

## Hacia la sección siguiente

Hasta ahora, para establecer equivalencias hemos utilizado tablas.

Pero ya hemos descubierto ejemplos como: $\neg\neg p\equiv p$ y $p\lor p\equiv p$.

Si acumulamos equivalencias de este tipo, podremos empezar a **transformar fórmulas** sin reconstruir una tabla completa cada vez.

El siguiente paso será reunir las primeras leyes sistemáticas de ese cálculo:
