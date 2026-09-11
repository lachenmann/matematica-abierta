## §10. Eliminar implicaciones y transformar fórmulas largas

Hasta ahora nuestro cálculo algebraico trabaja principalmente con:

$$
\neg,\qquad \land,\qquad \lor.
$$

Ya disponemos de leyes para doble negación, identidad, dominación, idempotencia, complemento, conmutatividad, asociatividad, distributividad, absorción y De Morgan. Pero todavía hay dos conectivos que evaluamos semánticamente y que aún no hemos incorporado plenamente al cálculo:

$$
\Rightarrow
\qquad\text{y}\qquad
\leftrightarrow.
$$

El objetivo de esta sección es mostrar que podemos **eliminarlos mediante equivalencias lógicas**.

La idea general será:

$$
\boxed{
\text{eliminar }\Rightarrow,\leftrightarrow
\longrightarrow
\text{trabajar con }\neg,\land,\lor
\longrightarrow
\text{aplicar las leyes ya demostradas}.
}
$$

Esto nos permitirá transformar fórmulas largas mediante cadenas justificadas, en lugar de construir una tabla completa cada vez.

### 10.1 La implicación como disyunción

Recordemos la tabla de:

$$
P\Rightarrow Q.
$$

| $P$ | $Q$ | $P\Rightarrow Q$ |
|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ |

Ahora comparemos con:

$$
\neg P\lor Q.
$$

| $P$ | $Q$ | $\neg P$ | $\neg P\lor Q$ |
|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |

Las columnas coinciden. Por tanto:

$$
P\Rightarrow Q\equiv\neg P\lor Q.
$$

Esta equivalencia traduce la idea ya conocida: una implicación falla únicamente cuando el antecedente es verdadero y el consecuente es falso.

### 10.2 Contraposición

Consideremos $\neg Q\Rightarrow\neg P$. Aplicando la equivalencia recién demostrada:

$$
\neg Q\Rightarrow\neg P
\equiv
\neg\neg Q\lor\neg P.
$$

Por doble negación:

$$
\equiv Q\lor\neg P.
$$

Por conmutatividad:

$$
\equiv\neg P\lor Q.
$$

Pero:

$$
\neg P\lor Q\equiv P\Rightarrow Q.
$$

Por tanto:

$$
\boxed{P\Rightarrow Q\equiv\neg Q\Rightarrow\neg P.}
$$

La implicación y su contraposición asociada son lógicamente equivalentes. No estamos usando todavía la contraposición como método general de demostración: estamos estableciendo una equivalencia entre fórmulas.

### 10.3 Negar una implicación

Consideremos $\neg(P\Rightarrow Q)$. Eliminamos la implicación:

$$
\neg(P\Rightarrow Q)
\equiv
\neg(\neg P\lor Q).
$$

Por De Morgan:

$$
\equiv
\neg\neg P\land\neg Q.
$$

Por doble negación:

$$
\boxed{\neg(P\Rightarrow Q)\equiv P\land\neg Q.}
$$

La fórmula resultante expresa exactamente el único caso que hace falsa una implicación.

### 10.4 Equivalencias fundamentales de la implicación

::: {.ma-block .ma-enunciado #apm-t1-c02-p0005}
**Proposición — Equivalencias fundamentales de la implicación**

Para fórmulas proposicionales arbitrarias $P,Q$:

$$
P\Rightarrow Q\equiv\neg P\lor Q,
$$

$$
P\Rightarrow Q\equiv\neg Q\Rightarrow\neg P,
$$

y:

$$
\neg(P\Rightarrow Q)\equiv P\land\neg Q.
$$
:::

#### Demostración

La primera equivalencia se estableció por tabla en §10.1. La segunda se derivó en §10.2 a partir de eliminación de implicación, doble negación y conmutatividad. La tercera se derivó en §10.3 mediante eliminación de implicación, De Morgan y doble negación. Quedan demostradas las tres equivalencias.

### 10.5 El bicondicional como dos implicaciones

Desde §4 sabemos que «$P$ si y solo si $Q$» exige dos direcciones: $P\Rightarrow Q$ y $Q\Rightarrow P$.

Ahora podemos demostrar formalmente:

$$
P\leftrightarrow Q
\equiv
(P\Rightarrow Q)\land(Q\Rightarrow P).
$$

| $P$ | $Q$ | $P\leftrightarrow Q$ | $P\Rightarrow Q$ | $Q\Rightarrow P$ | $(P\Rightarrow Q)\land(Q\Rightarrow P)$ |
|---|---|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |

Las columnas coinciden. Así:

$$
\boxed{P\leftrightarrow Q\equiv(P\Rightarrow Q)\land(Q\Rightarrow P).}
$$

### 10.6 El bicondicional sin implicaciones

Podemos continuar eliminando las dos implicaciones:

$$
(P\Rightarrow Q)\land(Q\Rightarrow P)
\equiv
(\neg P\lor Q)\land(\neg Q\lor P).
$$

Esta forma ya utiliza únicamente:

$$
\neg,\qquad\land,\qquad\lor.
$$

Existe además una forma particularmente clara. El bicondicional es verdadero cuando $P$ y $Q$ son ambas verdaderas o ambas falsas. Esto sugiere:

$$
(P\land Q)\lor(\neg P\land\neg Q).
$$

La tabla conjunta confirma:

| $P$ | $Q$ | $P\leftrightarrow Q$ | $P\land Q$ | $\neg P\land\neg Q$ | $(P\land Q)\lor(\neg P\land\neg Q)$ |
|---|---|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |

Por tanto:

$$
\boxed{P\leftrightarrow Q\equiv(P\land Q)\lor(\neg P\land\neg Q).}
$$

### 10.7 Negar un bicondicional

Si el bicondicional afirma que $P$ y $Q$ tienen el mismo valor, su negación expresa que tienen valores distintos. Los dos casos posibles son: $P\land\neg Q$ y $\neg P\land Q$.

La tabla verifica:

| $P$ | $Q$ | $P\leftrightarrow Q$ | $\neg(P\leftrightarrow Q)$ | $P\land\neg Q$ | $\neg P\land Q$ | $(P\land\neg Q)\lor(\neg P\land Q)$ |
|---|---|---|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |

Así:

$$
\boxed{\neg(P\leftrightarrow Q)\equiv(P\land\neg Q)\lor(\neg P\land Q).}
$$

### 10.8 Equivalencias fundamentales del bicondicional

::: {.ma-block .ma-enunciado #apm-t1-c02-p0006}
**Proposición — Equivalencias fundamentales del bicondicional**

Para fórmulas proposicionales arbitrarias $P,Q$:

$$
P\leftrightarrow Q\equiv(P\Rightarrow Q)\land(Q\Rightarrow P),
$$

$$
P\leftrightarrow Q\equiv(P\land Q)\lor(\neg P\land\neg Q),
$$

y:

$$
\neg(P\leftrightarrow Q)\equiv(P\land\neg Q)\lor(\neg P\land Q).
$$
:::

#### Demostración

Las tres equivalencias fueron verificadas semánticamente en §§10.5–10.7 mediante tablas completas. Por la definición de equivalencia lógica, quedan demostradas.

### 10.9 Un protocolo para fórmulas largas

Ante una fórmula que contiene varios conectivos, seguiremos como guía:

1. **Identificar la estructura:** conectivo principal y subfórmulas.
2. **Eliminar bicondicionales:** usar una forma de [la proposición «Equivalencias fundamentales del bicondicional»](#apm-t1-c02-p0006) adecuada al objetivo.
3. **Eliminar implicaciones:** usar $P\Rightarrow Q\equiv\neg P\lor Q$.
4. **Empujar negaciones hacia dentro:** De Morgan, doble negación o las negaciones ya demostradas.
5. **Simplificar:** usar [la proposición «Primeras leyes del álgebra proposicional»](#apm-t1-c02-p0002)–P0004.
6. **Revisar cada paso:** toda transición de una cadena debe estar autorizada.

::: {.ma-block .ma-intuicion}
**Idea clave**

No existe obligación de seguir siempre el mismo camino. Distintas rutas pueden conducir a fórmulas equivalentes. La elección debe favorecer claridad, economía y control de errores.
:::

### 10.10 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-t1-c02-x0018}
**Ejemplo — Una transformación larga con justificación línea por línea**
:::

Demostremos:

$$
\neg[(p\Rightarrow q)\land(r\lor\neg q)]
\equiv
(p\land\neg q)\lor(\neg r\land q).
$$

Partimos de:

$$
\neg[(p\Rightarrow q)\land(r\lor\neg q)].
$$

Aplicamos De Morgan a la conjunción exterior:

$$
\equiv
\neg(p\Rightarrow q)\lor\neg(r\lor\neg q).
$$

Por [la proposición «Equivalencias fundamentales de la implicación»](#apm-t1-c02-p0005):

$$
\neg(p\Rightarrow q)\equiv p\land\neg q.
$$

Y, por De Morgan:

$$
\neg(r\lor\neg q)
\equiv
\neg r\land\neg\neg q.
$$

Sustituyendo:

$$
\equiv
(p\land\neg q)\lor(\neg r\land\neg\neg q).
$$

Por doble negación:

$$
\equiv
(p\land\neg q)\lor(\neg r\land q).
$$

Por tanto:

$$

\neg[(p\Rightarrow q)\land(r\lor\neg q)]
\equiv
(p\land\neg q)\lor(\neg r\land q).

$$

En forma compacta:

$$
\begin{aligned}
\neg[(p\Rightarrow q)\land(r\lor\neg q)]
&\equiv \neg(p\Rightarrow q)\lor\neg(r\lor\neg q)
&&\text{(De Morgan)}\\
&\equiv (p\land\neg q)\lor(\neg r\land\neg\neg q)
&&\text{(P0005 y De Morgan)}\\
&\equiv (p\land\neg q)\lor(\neg r\land q)
&&\text{(doble negación).}
\end{aligned}
$$

La fórmula final ya no contiene implicaciones.
## Ejercicios

### Eliminar implicaciones {#apm-t1-c02-e0116}
Reescribe utilizando únicamente $\neg,\land,\lor$ y simplifica cuando sea posible.

#### a)

$$
P\Rightarrow Q
$$

#### b)

$$
\neg(P\Rightarrow Q)
$$

#### c)

$$
P\Rightarrow\neg Q
$$

#### Solución


#### a)

Por [la proposición «Equivalencias fundamentales de la implicación»](#apm-t1-c02-p0005):

$$
\boxed{P\Rightarrow Q\equiv\neg P\lor Q.}
$$

#### b)

$$
\boxed{\neg(P\Rightarrow Q)\equiv P\land\neg Q.}
$$

#### c)

$$
P\Rightarrow\neg Q
\equiv
\neg P\lor\neg Q.
$$

Por De Morgan en sentido inverso:

$$
\neg P\lor\neg Q\equiv\neg(P\land Q).
$$

Por tanto:

$$
\boxed{P\Rightarrow\neg Q\equiv\neg P\lor\neg Q\equiv\neg(P\land Q).}
$$

### Contraposición algebraica {#apm-t1-c02-e0117}
Demuestra mediante una cadena de equivalencias, sin construir una tabla nueva, que:

$$
P\Rightarrow Q\equiv\neg Q\Rightarrow\neg P.
$$

#### Solución


Partimos de la contraposición asociada:

$$
\neg Q\Rightarrow\neg P
\equiv
\neg\neg Q\lor\neg P
\equiv
Q\lor\neg P
\equiv
\neg P\lor Q
\equiv
P\Rightarrow Q.
$$

Los pasos usan, respectivamente, eliminación de implicación, doble negación, conmutatividad y `P0005` en sentido inverso.

### Eliminar un bicondicional {#apm-t1-c02-e0118}
Transforma:

$$
P\leftrightarrow Q
$$

en una fórmula que use únicamente $\neg,\land,\lor$, partiendo de las dos implicaciones.

#### Solución


Por [la proposición «Equivalencias fundamentales del bicondicional»](#apm-t1-c02-p0006):

$$
P\leftrightarrow Q
\equiv
(P\Rightarrow Q)\land(Q\Rightarrow P).
$$

Eliminamos ambas implicaciones:

$$
\equiv
(\neg P\lor Q)\land(\neg Q\lor P).
$$

Por tanto:

$$
\boxed{P\leftrightarrow Q\equiv(\neg P\lor Q)\land(\neg Q\lor P).}
$$

### Justificar la negación del bicondicional {#apm-t1-c02-e0119}
Demuestra mediante una tabla completa:

$$
\neg(P\leftrightarrow Q)
\equiv
(P\land\neg Q)\lor(\neg P\land Q).
$$

#### Solución


| $P$ | $Q$ | $P\leftrightarrow Q$ | $\neg(P\leftrightarrow Q)$ | $P\land\neg Q$ | $\neg P\land Q$ | $(P\land\neg Q)\lor(\neg P\land Q)$ |
|---|---|---|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |

Las columnas comparadas coinciden fila por fila. Luego:

$$
\boxed{\neg(P\leftrightarrow Q)\equiv(P\land\neg Q)\lor(\neg P\land Q).}
$$

### Una equivalencia de implicaciones anidadas {#apm-t1-c02-e0120}
Demuestra que:

$$
p\Rightarrow(q\Rightarrow r)
$$

y:

$$
(p\land q)\Rightarrow r
$$

son lógicamente equivalentes. Concluye después que:

$$
(p\Rightarrow(q\Rightarrow r))
\leftrightarrow
((p\land q)\Rightarrow r)
$$

es una tautología.

#### Solución


Comenzamos por:

$$
p\Rightarrow(q\Rightarrow r).
$$

Eliminamos la implicación exterior:

$$
\equiv
\neg p\lor(q\Rightarrow r).
$$

Eliminamos la interior:

$$
\equiv
\neg p\lor(\neg q\lor r).
$$

Por asociatividad:

$$
\equiv
(\neg p\lor\neg q)\lor r.
$$

Por De Morgan en sentido inverso:

$$
\neg p\lor\neg q\equiv\neg(p\land q).
$$

Entonces:

$$
\equiv
\neg(p\land q)\lor r.
$$

Por `P0005` en sentido inverso:

$$
\equiv
(p\land q)\Rightarrow r.
$$

Así:

$$
\boxed{p\Rightarrow(q\Rightarrow r)\equiv(p\land q)\Rightarrow r.}
$$

Por [la proposición «Criterio bicondicional para la equivalencia lógica»](#apm-t1-c02-p0001), el bicondicional entre dos fórmulas equivalentes es una tautología. Luego:

$$
\boxed{(p\Rightarrow(q\Rightarrow r))\leftrightarrow((p\land q)\Rightarrow r)}
$$

es una tautología.

### Refutar una transformación incorrecta {#apm-t1-c02-e0121}
Alguien propone:

$$
P\Rightarrow Q\equiv P\lor Q.
$$

Refuta la equivalencia con una sola contraasignación y explica cuál es la forma correcta.

#### Solución


Tomemos:

$$
P=\mathrm V,
\qquad
Q=\mathrm F.
$$

Entonces:

$$
P\Rightarrow Q=\mathrm F,
$$

mientras que:

$$
P\lor Q=\mathrm V.
$$

Por tanto, las fórmulas no son equivalentes. La forma correcta es:

$$
\boxed{P\Rightarrow Q\equiv\neg P\lor Q.}
$$

### Síntesis con bicondicional y negación {#apm-t1-c02-e0122}
Simplifica:

$$
\neg(P\leftrightarrow Q)\lor(P\land Q)
$$

hasta una fórmula equivalente construida como disyunción de conjunciones de literales.

#### Solución


Por [la proposición «Equivalencias fundamentales del bicondicional»](#apm-t1-c02-p0006):

$$
\neg(P\leftrightarrow Q)
\equiv
(P\land\neg Q)\lor(\neg P\land Q).
$$

Sustituimos:

$$
\neg(P\leftrightarrow Q)\lor(P\land Q)
$$

$$
\equiv
(P\land\neg Q)\lor(\neg P\land Q)\lor(P\land Q).
$$

Por tanto:

$$
\boxed{(P\land\neg Q)\lor(\neg P\land Q)\lor(P\land Q).}
$$

La fórmula final no contiene $\Rightarrow$ ni $\leftrightarrow$. La clasificación sistemática de esta forma pertenece a la sección siguiente.

### Síntesis larga: elegir una ruta eficiente {#apm-t1-c02-e0123}
Transforma y simplifica:

$$
\neg\bigl[(P\leftrightarrow Q)\land(P\Rightarrow Q)\bigr].
$$

El resultado final no debe contener $\Rightarrow$ ni $\leftrightarrow$.

#### Solución


Aplicamos De Morgan:

$$
\neg\bigl[(P\leftrightarrow Q)\land(P\Rightarrow Q)\bigr]
\equiv
\neg(P\leftrightarrow Q)\lor\neg(P\Rightarrow Q).
$$

Por [la proposición «Equivalencias fundamentales del bicondicional»](#apm-t1-c02-p0006):

$$
\neg(P\leftrightarrow Q)
\equiv
(P\land\neg Q)\lor(\neg P\land Q).
$$

Por [la proposición «Equivalencias fundamentales de la implicación»](#apm-t1-c02-p0005):

$$
\neg(P\Rightarrow Q)
\equiv
P\land\neg Q.
$$

Sustituyendo:

$$
\equiv
\bigl[(P\land\neg Q)\lor(\neg P\land Q)\bigr]
\lor(P\land\neg Q).
$$

Por asociatividad, conmutatividad e idempotencia:

$$
\equiv
(P\land\neg Q)\lor(\neg P\land Q).
$$

Por tanto:

$$
\boxed{
\neg\bigl[(P\leftrightarrow Q)\land(P\Rightarrow Q)\bigr]
\equiv
(P\land\neg Q)\lor(\neg P\land Q).
}
$$

## Síntesis

La implicación queda incorporada al cálculo mediante [la proposición «Equivalencias fundamentales de la implicación»](#apm-t1-c02-p0005):

$$
P\Rightarrow Q\equiv\neg P\lor Q,
$$

$$
P\Rightarrow Q\equiv\neg Q\Rightarrow\neg P,
$$

$$
\neg(P\Rightarrow Q)\equiv P\land\neg Q.
$$

El bicondicional queda incorporado mediante [la proposición «Equivalencias fundamentales del bicondicional»](#apm-t1-c02-p0006):

$$
P\leftrightarrow Q\equiv(P\Rightarrow Q)\land(Q\Rightarrow P),
$$

$$
P\leftrightarrow Q\equiv(P\land Q)\lor(\neg P\land\neg Q),
$$

$$
\neg(P\leftrightarrow Q)\equiv(P\land\neg Q)\lor(\neg P\land Q).
$$

Con ello podemos transformar una fórmula hasta eliminar $\Rightarrow$ y $\leftrightarrow$ y trabajar únicamente con $\neg,\land,\lor$.

El protocolo general queda:

$$

\text{eliminar bicondicionales}
\to
\text{eliminar implicaciones}
\to
\text{empujar negaciones}
\to
\text{simplificar}.

$$

No es una receta rígida: una equivalencia más directa puede ahorrar pasos. Pero toda transformación debe permanecer justificada.

## Hacia la sección siguiente

En varios ejercicios hemos terminado con fórmulas formadas por proposiciones o negaciones de proposiciones, conjunciones y disyunciones. Por ejemplo:

$$
(P\land\neg Q)\lor(\neg P\land Q).
$$

¿Podemos organizar **cualquier fórmula proposicional** en formas sistemáticas de este tipo?

La respuesta será afirmativa. La siguiente sección introducirá:
