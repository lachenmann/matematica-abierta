## §9. Distributividad, absorción y leyes de De Morgan

En la sección anterior empezamos a calcular con fórmulas.

Ya disponemos de leyes como:

$$
P\land P\equiv P,
$$

$$
P\lor\neg P\equiv T,
$$

$$
\neg\neg P\equiv P,
$$

y podemos reordenar o reagrupar conjunciones y disyunciones.

Pero todavía falta una parte importante del paralelismo con el álgebra.

En aritmética conocemos:

$$
a(b+c)=ab+ac.
$$

La multiplicación se distribuye sobre la suma. En lógica proposicional aparecerá algo parecido, pero con una diferencia estructural notable:

> **la conjunción se distribuye sobre la disyunción y la disyunción se distribuye sobre la conjunción.**

Además, encontraremos dos nuevas familias de leyes:

- **absorción**, que elimina ciertas repeticiones estructurales;
- **De Morgan**, que describe cómo atraviesa una negación a una conjunción o a una disyunción.

Con estas herramientas el álgebra proposicional empieza a adquirir una fisonomía propia.

---

### 9.1 La conjunción distribuye sobre la disyunción

Consideremos $P\land(Q\lor R)$. La fórmula afirma que $P$ es verdadera y que, además, al menos una de $Q,R$ es verdadera.

Comparemos con:

$$
(P\land Q)\lor(P\land R).
$$

Esta segunda fórmula afirma que se cumple al menos una de las dos posibilidades:

- $P$ y $Q$ son verdaderas;
- $P$ y $R$ son verdaderas.

Ambas descripciones tienen el mismo comportamiento lógico. Podemos verlo sin una tabla de ocho filas completa.

#### Si $P=\mathrm F$

Entonces $P\land(Q\lor R)=\mathrm F$ También:

$$
P\land Q=\mathrm F,
\qquad
P\land R=\mathrm F,
$$

y por tanto:

$$
(P\land Q)\lor(P\land R)=\mathrm F.
$$

#### Si $P=\mathrm V$

Entonces $P\land(Q\lor R)$ recibe exactamente el valor de:

$$
Q\lor R.
$$

Por otra parte:

$$
P\land Q
$$

recibe el valor de $Q$, y:

$$
P\land R
$$

recibe el valor de $R$. Así, $(P\land Q)\lor(P\land R)$ también recibe exactamente el valor de:

$$
Q\lor R.
$$

En todos los casos:

$$
\boxed{
P\land(Q\lor R)
\equiv
(P\land Q)\lor(P\land R).
}
$$

---

### 9.2 La disyunción también distribuye sobre la conjunción

Ahora comparemos $P\lor(Q\land R)$ con $(P\lor Q)\land(P\lor R)$.

#### Si $P=\mathrm V$

La primera fórmula es verdadera porque contiene una disyunción con $P=\mathrm V$.

En la segunda: $P\lor Q=\mathrm V$ y $P\lor R=\mathrm V$. Por tanto, su conjunción también es verdadera.

#### Si $P=\mathrm F$

La primera fórmula recibe exactamente el valor de:

$$
Q\land R.
$$

En la segunda:

$$
P\lor Q
$$

recibe el valor de $Q$, mientras que:

$$
P\lor R
$$

recibe el valor de $R$. Por tanto:

$$
(P\lor Q)\land(P\lor R)
$$

recibe también el valor de:

$$
Q\land R.
$$

Así:

$$
\boxed{
P\lor(Q\land R)
\equiv
(P\lor Q)\land(P\lor R).
}
$$

::: {.ma-block .ma-intuicion}
**Idea clave**

En el álgebra proposicional las dos operaciones principales presentan una distributividad mutua:

$$
\land\text{ distribuye sobre }\lor,
$$

y:

$$
\lor\text{ distribuye sobre }\land.
$$
:::

Esta simetría será muy útil para transformar fórmulas.

---

### 9.3 Absorción

Consideremos $P\lor(P\land Q)$ Puede parecer que la segunda parte aporta información adicional.

Pero si $P$ es verdadera, toda la disyunción ya es verdadera.

Y si $P$ es falsa, entonces $P\land Q$ también es falsa.

La fórmula completa tiene siempre el mismo valor que $P$:

$$
P\lor(P\land Q)\equiv P.
$$

De manera dual:

$$
P\land(P\lor Q)\equiv P.
$$

Estas son las **leyes de absorción**. La palabra es apropiada: una aparición de $P$ absorbe una expresión mayor que ya contiene a $P$ de la forma adecuada.

---

### 9.4 Distributividad y absorción

Reunimos estas leyes.

::: {.ma-block .ma-enunciado #apm-t1-c02-p0003}
**Proposición — Distributividad y absorción**

Para fórmulas proposicionales arbitrarias $P,Q,R$:

**Distributividad**

$$
P\land(Q\lor R)
\equiv
(P\land Q)\lor(P\land R),
$$

$$
P\lor(Q\land R)
\equiv
(P\lor Q)\land(P\lor R).
$$

**Absorción**

$$
P\lor(P\land Q)\equiv P,
$$

$$
P\land(P\lor Q)\equiv P.
$$
:::

#### Demostración

Las dos leyes distributivas quedaron justificadas semánticamente en §§9.1–9.2 considerando los dos valores posibles de $P$.

Para la primera ley de absorción, fijemos una asignación.

- Si $P=\mathrm V$, entonces:
  $$
  P\lor(P\land Q)=\mathrm V,
  $$
  que coincide con $P$.
- Si $P=\mathrm F$, entonces:
  $$
  P\land Q=\mathrm F,
  $$
  y por tanto:
  $$
  P\lor(P\land Q)=\mathrm F,
  $$
  que nuevamente coincide con $P$.

Así, $P\lor(P\land Q)\equiv P$. La segunda absorción se verifica de manera dual:

- si $P=\mathrm F$, toda la conjunción es falsa;
- si $P=\mathrm V$, entonces $P\lor Q$ es verdadera y toda la conjunción es verdadera.

Por tanto:

$$
P\land(P\lor Q)\equiv P.
$$

Quedan demostradas las cuatro equivalencias.

---

### 9.5 Negar una conjunción

Consideremos $\neg(P\land Q)$. La fórmula es verdadera cuando:

$$
P\land Q
$$

es falsa.

Pero una conjunción es falsa precisamente cuando al menos uno de sus componentes es falso.

Eso sugiere:

$$
\neg P\lor\neg Q.
$$

Construimos la tabla:

| $P$ | $Q$ | $P\land Q$ | $\neg(P\land Q)$ | $\neg P$ | $\neg Q$ | $\neg P\lor\neg Q$ |
|---|---|---|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |

Las columnas coinciden:

$$
\boxed{
\neg(P\land Q)
\equiv
\neg P\lor\neg Q.
}
$$

Esta equivalencia ya había aparecido semánticamente en §7. Ahora queda incorporada formalmente al repertorio de leyes de cálculo.

---

### 9.6 Negar una disyunción

Ahora consideremos $\neg(P\lor Q)$ Para que una disyunción sea falsa, ambos componentes deben ser falsos.

Por tanto, su negación será verdadera exactamente cuando: $\neg P$ y $\neg Q$ sean ambas verdaderas.

La tabla lo confirma:

| $P$ | $Q$ | $P\lor Q$ | $\neg(P\lor Q)$ | $\neg P$ | $\neg Q$ | $\neg P\land\neg Q$ |
|---|---|---|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |

Así:

$$
\boxed{
\neg(P\lor Q)
\equiv
\neg P\land\neg Q.
}
$$

---

### 9.7 Las leyes de De Morgan

::: {.ma-block .ma-enunciado #apm-t1-c02-p0004}
**Proposición — Leyes de De Morgan**

Para fórmulas proposicionales arbitrarias $P,Q$:

$$
\neg(P\land Q)
\equiv
\neg P\lor\neg Q,
$$

y:

$$
\neg(P\lor Q)
\equiv
\neg P\land\neg Q.
$$
:::

#### Demostración

Las tablas de §§9.5–9.6 muestran que, en cada caso, las columnas situadas a ambos lados de $\equiv$ coinciden fila por fila.

Por la definición de equivalencia lógica, ambas equivalencias quedan demostradas.

---

### 9.8 Qué hace De Morgan

Las leyes de De Morgan no dicen simplemente que «la negación entra al paréntesis».

Al atravesar el conectivo, la negación **intercambia**: $\land$ con $\lor$.

Así, $\neg(P\land Q)$ no se transforma en:

$$
\neg P\land\neg Q,
$$

sino en: $\neg P\lor\neg Q$ Y $\neg(P\lor Q)$ no se transforma en:

$$
\neg P\lor\neg Q,
$$

sino en:

$$
\neg P\land\neg Q.
$$

La regla estructural es:

$$

\text{negar cada componente}
\quad+\quad
\text{intercambiar }\land\text{ y }\lor.

$$

Esta formulación será útil, pero nunca sustituye la justificación matemática: la regla es válida porque [la proposición «Leyes de De Morgan»](#apm-t1-c02-p0004) ya está demostrado.

---

### 9.9 Una simetría que empieza a hacerse visible

Comparemos algunas parejas:

$$
P\land T\equiv P,
\qquad
P\lor C\equiv P,
$$

$$
P\land(P\lor Q)\equiv P,
\qquad
P\lor(P\land Q)\equiv P,
$$

y:

$$
\neg(P\land Q)\equiv\neg P\lor\neg Q,
$$

$$
\neg(P\lor Q)\equiv\neg P\land\neg Q.
$$

El intercambio:

$$
\land
\longleftrightarrow
\lor
$$

aparece repetidamente acompañado por el intercambio entre comportamiento tautológico y contradictorio.

No convertiremos todavía esta observación en un principio abstracto.

Por ahora basta registrar que el álgebra proposicional tiene una **dualidad visible** entre conjunción y disyunción.

---

### 9.10 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-t1-c02-x0017}
**Ejemplo — De Morgan y absorción en una misma cadena**
:::

Simplifiquemos:

$$
\neg\bigl(P\land(P\lor Q)\bigr).
$$

Podríamos usar absorción inmediatamente dentro de la negación:

$$
P\land(P\lor Q)\equiv P.
$$

Pero queremos mostrar cómo interactúan las leyes nuevas. Primero aplicamos De Morgan:

$$
\neg\bigl(P\land(P\lor Q)\bigr)
\equiv
\neg P\lor\neg(P\lor Q).
$$

Aplicamos nuevamente De Morgan a la segunda negación:

$$
\neg(P\lor Q)
\equiv
\neg P\land\neg Q.
$$

Sustituyendo:

$$
\neg P\lor\neg(P\lor Q)
\equiv
\neg P\lor(\neg P\land\neg Q).
$$

Ahora aparece exactamente la forma de absorción:

$$
A\lor(A\land B)\equiv A,
$$

con:

$$
A=\neg P,
\qquad
B=\neg Q.
$$

Por tanto:

$$
\neg P\lor(\neg P\land\neg Q)
\equiv
\neg P.
$$

La cadena completa es:

$$
\begin{aligned}
\neg\bigl(P\land(P\lor Q)\bigr)
&\equiv
\neg P\lor\neg(P\lor Q)
&&\text{(De Morgan)}\\
&\equiv
\neg P\lor(\neg P\land\neg Q)
&&\text{(De Morgan)}\\
&\equiv
\neg P
&&\text{(absorción).}
\end{aligned}
$$

Así:

$$

\neg\bigl(P\land(P\lor Q)\bigr)
\equiv
\neg P.

$$

Este ejemplo muestra algo importante: una transformación puede ser correcta por rutas diferentes. Lo decisivo es que cada paso esté autorizado por una equivalencia previamente demostrada.

---
## Ejercicios

### Distribuir y simplificar {#apm-t1-c02-e0109}
Simplifica:

$$
P\land(Q\lor P).
$$

Utiliza distributividad y las leyes de [la proposición «Primeras leyes del álgebra proposicional»](#apm-t1-c02-p0002).

#### Solución


Por distributividad:

$$
P\land(Q\lor P)
\equiv
(P\land Q)\lor(P\land P).
$$

Por idempotencia:

$$
P\land P\equiv P.
$$

Entonces:

$$
(P\land Q)\lor(P\land P)
\equiv
(P\land Q)\lor P.
$$

Por conmutatividad:

$$
(P\land Q)\lor P
\equiv
P\lor(P\land Q).
$$

Por absorción:

$$
P\lor(P\land Q)\equiv P.
$$

Por tanto:

$$
\boxed{
P\land(Q\lor P)
\equiv
P.
}
$$

La simplificación coincide, naturalmente, con la ley de absorción en su forma conmutada.

---

### Justificar la segunda distributividad {#apm-t1-c02-e0110}
Demuestra mediante una tabla de verdad que:

$$
P\lor(Q\land R)
\equiv
(P\lor Q)\land(P\lor R).
$$

#### Solución


| $P$ | $Q$ | $R$ | $Q\land R$ | $P\lor(Q\land R)$ | $P\lor Q$ | $P\lor R$ | $(P\lor Q)\land(P\lor R)$ |
|---|---|---|---|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |

Las dos columnas finales que estamos comparando coinciden en las ocho filas.

Por tanto:

$$
\boxed{
P\lor(Q\land R)
\equiv
(P\lor Q)\land(P\lor R).
}
$$

---

### Justificar absorción {#apm-t1-c02-e0111}
Demuestra directamente desde los valores de verdad, sin usar la ley de absorción como premisa, que:

$$
P\land(P\lor Q)\equiv P.
$$

#### Solución


Consideremos los dos valores posibles de $P$.

#### Si $P=\mathrm F$

Entonces:

$$
P\land(P\lor Q)=\mathrm F,
$$

independientemente del valor de $Q$.

Ese valor coincide con $P$.

#### Si $P=\mathrm V$

Entonces:

$$
P\lor Q=\mathrm V.
$$

Por tanto:

$$
P\land(P\lor Q)
=
\mathrm V\land\mathrm V
=
\mathrm V,
$$

que nuevamente coincide con $P$.

Así, en toda asignación:

$$
P\land(P\lor Q)
$$

y:

$$
P
$$

reciben el mismo valor.

Por definición:

$$
\boxed{
P\land(P\lor Q)\equiv P.
}
$$

---

### Demostrar la segunda ley de De Morgan {#apm-t1-c02-e0112}
Construye una tabla para demostrar:

$$
\neg(P\lor Q)
\equiv
\neg P\land\neg Q.
$$

#### Solución


| $P$ | $Q$ | $P\lor Q$ | $\neg(P\lor Q)$ | $\neg P$ | $\neg Q$ | $\neg P\land\neg Q$ |
|---|---|---|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |

Las columnas:

$$
\neg(P\lor Q)
$$

y:

$$
\neg P\land\neg Q
$$

coinciden fila por fila.

Luego:

$$
\boxed{
\neg(P\lor Q)
\equiv
\neg P\land\neg Q.
}
$$

---

### Explorar la dualidad {#apm-t1-c02-e0113}
Considera las cuatro leyes:

$$
P\land(Q\lor R)
\equiv
(P\land Q)\lor(P\land R),
$$

$$
P\lor(Q\land R)
\equiv
(P\lor Q)\land(P\lor R),
$$

$$
\neg(P\land Q)
\equiv
\neg P\lor\neg Q,
$$

$$
\neg(P\lor Q)
\equiv
\neg P\land\neg Q.
$$

#### a)

Empareja cada ley con la que se obtiene al intercambiar:

$$
\land
$$

y:

$$
\lor.
$$

#### b)

¿Qué regularidad observas?

#### c)

¿Por qué esta observación no basta, por sí sola, para afirmar que cualquier fórmula obtenida intercambiando $\land$ y $\lor$ será equivalente a la original?

#### Solución


#### a)

Las dos leyes distributivas forman una pareja.

Las dos leyes de De Morgan forman otra.

#### b)

Las leyes aparecen en versiones duales: al intercambiar conjunción y disyunción obtenemos otra ley válida del mismo repertorio.

#### c)

La dualidad observada es una regularidad entre **leyes específicas ya demostradas**.

No hemos establecido un teorema general que permita intercambiar $\land$ y $\lor$ arbitrariamente dentro de cualquier fórmula conservando su valor.

De hecho, por ejemplo:

$$
P\land Q
$$

y:

$$
P\lor Q
$$

no son lógicamente equivalentes en general.

La observación estructural no autoriza reescrituras que no estén respaldadas por una ley demostrada.

---

### Una falsa ley de De Morgan {#apm-t1-c02-e0114}
Alguien propone:

$$
\neg(P\land Q)
\equiv
\neg P\land\neg Q.
$$

Refuta la pretendida equivalencia con una sola contraasignación.

#### Solución


Tomemos:

$$
P=\mathrm V,
\qquad
Q=\mathrm F.
$$

Entonces:

$$
P\land Q
=
\mathrm V\land\mathrm F
=
\mathrm F.
$$

Por tanto:

$$
\neg(P\land Q)=\mathrm V.
$$

En cambio:

$$
\neg P=\mathrm F,
\qquad
\neg Q=\mathrm V,
$$

de modo que:

$$
\neg P\land\neg Q
=
\mathrm F\land\mathrm V
=
\mathrm F.
$$

Las dos fórmulas reciben valores distintos.

Por tanto, no son lógicamente equivalentes.

La contraasignación muestra exactamente qué error contiene la falsa regla: al atravesar una conjunción, la negación debe cambiar $\land$ por $\lor$.

---

### Síntesis: dos caminos hacia la misma simplificación {#apm-t1-c02-e0115}
Simplifica:

$$
\neg\bigl((P\lor Q)\land(P\lor\neg Q)\bigr)
$$

hasta una fórmula que dependa solo de $P$.

Realiza **dos derivaciones**:

1. una que simplifique primero el interior mediante distributividad;
2. otra que comience aplicando De Morgan a la negación exterior.

#### Solución


### Primer camino — Distributividad en el interior

Usamos la distributividad de $\lor$ sobre $\land$ en sentido inverso:

$$
(P\lor Q)\land(P\lor\neg Q)
\equiv
P\lor(Q\land\neg Q).
$$

Por complemento:

$$
Q\land\neg Q\equiv C.
$$

Entonces:

$$
P\lor(Q\land\neg Q)
\equiv
P\lor C.
$$

Por identidad:

$$
P\lor C\equiv P.
$$

Sustituyendo dentro de la negación:

$$
\neg\bigl((P\lor Q)\land(P\lor\neg Q)\bigr)
\equiv
\neg P.
$$

Por tanto:

$$
\boxed{
\neg\bigl((P\lor Q)\land(P\lor\neg Q)\bigr)
\equiv
\neg P.
}
$$

### Segundo camino — De Morgan primero

Aplicamos De Morgan a la negación exterior:

$$
\begin{aligned}
&\neg\bigl((P\lor Q)\land(P\lor\neg Q)\bigr)\\
&\equiv
\neg(P\lor Q)\lor\neg(P\lor\neg Q).
\end{aligned}
$$

Aplicamos De Morgan a cada término:

$$
\equiv
(\neg P\land\neg Q)
\lor
(\neg P\land\neg\neg Q).
$$

Por doble negación:

$$
\equiv
(\neg P\land\neg Q)
\lor
(\neg P\land Q).
$$

Aplicamos distributividad en sentido inverso:

$$
\equiv
\neg P\land(\neg Q\lor Q).
$$

Por complemento:

$$
\neg Q\lor Q\equiv T.
$$

Entonces:

$$
\equiv
\neg P\land T.
$$

Por identidad:

$$
\equiv
\neg P.
$$

Llegamos nuevamente a:

$$
\boxed{
\neg\bigl((P\lor Q)\land(P\lor\neg Q)\bigr)
\equiv
\neg P.
}
$$

Las dos rutas son válidas porque cada paso está justificado por una equivalencia ya demostrada.

---

## Síntesis

El repertorio de cálculo proposicional se amplía ahora con:

> [la proposición «Distributividad y absorción»](#apm-t1-c02-p0003) — distributividad y absorción;

y:

> [la proposición «Leyes de De Morgan»](#apm-t1-c02-p0004) — leyes de De Morgan.

Las distributividades son:

$$
P\land(Q\lor R)
\equiv
(P\land Q)\lor(P\land R),
$$

$$
P\lor(Q\land R)
\equiv
(P\lor Q)\land(P\lor R).
$$

Las absorciones son:

$$
P\lor(P\land Q)\equiv P,
$$

$$
P\land(P\lor Q)\equiv P.
$$

Y De Morgan establece:

$$
\neg(P\land Q)
\equiv
\neg P\lor\neg Q,
$$

$$
\neg(P\lor Q)
\equiv
\neg P\land\neg Q.
$$

El principio operativo es:

$$

\text{cada reescritura debe corresponder a una equivalencia ya establecida}.

$$

Con [la proposición «Primeras leyes del álgebra proposicional»](#apm-t1-c02-p0002), [la proposición «Distributividad y absorción»](#apm-t1-c02-p0003) y [la proposición «Leyes de De Morgan»](#apm-t1-c02-p0004) disponemos ya de un verdadero núcleo de álgebra proposicional.

---

## Hacia la sección siguiente

Todavía quedan dos conectivos que no hemos incorporado plenamente al cálculo: $\Rightarrow$ y $\leftrightarrow$.

Hasta ahora sabemos evaluarlos mediante sus tablas, pero nuestras leyes de transformación trabajan sobre todo con:

$$
\neg,\qquad
\land,\qquad
\lor.
$$

La siguiente sección mostrará cómo eliminar implicaciones y bicondicionales y cómo transformar fórmulas largas de manera sistemática:
