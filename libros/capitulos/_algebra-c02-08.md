## §8. Primeras leyes del álgebra proposicional

Hasta ahora, para demostrar una equivalencia lógica hemos regresado a la semántica: construimos una tabla, comparamos columnas y concluimos que dos fórmulas son equivalentes.

Ese procedimiento es seguro, pero empieza a resultar costoso.

En [el ejercicio «Doble negación por tabla»](#apm-i-e0096) vimos:

$$
\neg\neg P\equiv P.
$$

En [el ejercicio «Idempotencia descubierta semánticamente»](#apm-i-e0098) apareció:

$$
P\lor P\equiv P.
$$

Y en [el ejemplo «Demostrar una equivalencia por tabla»](#apm-i-x0015) establecimos:

$$
\neg(P\land Q)\equiv\neg P\lor\neg Q.
$$

Estas equivalencias sugieren un cambio de perspectiva. En álgebra elemental no demostramos desde cero cada vez que:

$$
a+b=b+a.
$$

Una vez establecida la conmutatividad, la utilizamos como una ley. Queremos hacer lo mismo con las fórmulas proposicionales.

La trayectoria será:

$$
\boxed{
\text{semántica}
\longrightarrow
\text{equivalencia demostrada}
\longrightarrow
\text{ley reutilizable}
\longrightarrow
\text{cálculo}.
}
$$

Pero el orden importa: **una equivalencia solo podrá usarse como ley después de haber sido justificada**.

---

### 8.1 Dos fórmulas especiales: una siempre verdadera y otra siempre falsa

Necesitaremos abreviar dos tipos de fórmulas que ya conocemos.

Sea $T$ una fórmula tautológica cualquiera, y sea:

$$
C
$$

una fórmula contradictoria cualquiera. Por tanto, bajo toda asignación relevante: $T=\mathrm V$ y $C=\mathrm F$.

Por ejemplo, podemos tomar: $T=P\lor\neg P$ y $C=P\land\neg P$.

::: {.ma-block .ma-observacion}
**Observación**

Las letras $T$ y $C$ no son nuevos valores de verdad. Son abreviaturas para **fórmulas**: $T$ representa una tautología y $C$ una contradicción.

Los valores de verdad del capítulo siguen siendo:

$$
\mathrm V,\qquad\mathrm F.
$$
:::

Esta distinción evita mezclar el nivel de las fórmulas con el nivel de sus valores.

---

### 8.2 Identidad y dominación

Comencemos con una fórmula arbitraria:

$$
P.
$$

Si la conjuntamos con una tautología:

$$
P\land T,
$$

la segunda parte siempre vale $\mathrm V$. El valor de la conjunción queda determinado exactamente por el valor de $P$.

| $P$ | $T$ | $P\land T$ |
|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ |

Así, $P\land T\equiv P$. De manera dual, como una contradicción siempre recibe $\mathrm F$:

$$
P\lor C\equiv P.
$$

Estas son **leyes de identidad**. Ahora observemos $P\lor T$ Como $T$ siempre es verdadera, toda la disyunción es verdadera:

$$
P\lor T\equiv T.
$$

Y, como $C$ siempre es falsa:

$$
P\land C\equiv C.
$$

Estas son **leyes de dominación**. Podemos reunir:

$$
\boxed{
\begin{aligned}
P\land T&\equiv P,\\
P\lor C&\equiv P,\\
P\lor T&\equiv T,\\
P\land C&\equiv C.
\end{aligned}
}
$$

---

### 8.3 Idempotencia

¿Qué ocurre si una fórmula se combina consigo misma?

Para la conjunción:

| $P$ | $P\land P$ |
|---|---|
| $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ |

Por tanto:

$$
P\land P\equiv P.
$$

Para la disyunción:

| $P$ | $P\lor P$ |
|---|---|
| $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ |

Así, $P\lor P\equiv P$. Estas son las **leyes de idempotencia**:

$$
\boxed{
P\land P\equiv P,
\qquad
P\lor P\equiv P.
}
$$

---

### 8.4 Complemento

Sabemos que $P$ y $\neg P$ tienen siempre valores opuestos. Por tanto:

$$
P\lor\neg P
$$

es siempre verdadera, mientras que:

$$
P\land\neg P
$$

es siempre falsa. En nuestra notación:

$$
\boxed{
P\lor\neg P\equiv T,
\qquad
P\land\neg P\equiv C.
}
$$

Estas son las **leyes de complemento**. Obsérvese nuevamente que $T$ y $C$ representan fórmulas tautológicas y contradictorias, no los valores $\mathrm V$ y $\mathrm F$.

---

### 8.5 Doble negación

La negación invierte el valor de una fórmula. Una segunda negación vuelve a invertirlo.

| $P$ | $\neg P$ | $\neg\neg P$ |
|---|---|---|
| $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ |

Por tanto:

$$

\neg\neg P\equiv P.

$$

Esta será nuestra **ley de doble negación**.

---

### 8.6 Conmutatividad

Comparemos $P\land Q$ y $Q\land P$.

| $P$ | $Q$ | $P\land Q$ | $Q\land P$ |
|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |

Las columnas coinciden. Así:

$$
P\land Q\equiv Q\land P.
$$

Lo mismo ocurre con la disyunción:

$$
P\lor Q\equiv Q\lor P.
$$

Tenemos las **leyes conmutativas**:

$$
\boxed{
P\land Q\equiv Q\land P,
\qquad
P\lor Q\equiv Q\lor P.
}
$$

El orden de los dos componentes no cambia el comportamiento lógico de una conjunción ni de una disyunción.

---

### 8.7 Asociatividad

Consideremos tres fórmulas:

$$
P,\qquad Q,\qquad R.
$$

Para la conjunción podemos agrupar: $(P\land Q)\land R$ o $P\land(Q\land R)$. La tabla conjunta es:

| $P$ | $Q$ | $R$ | $(P\land Q)\land R$ | $P\land(Q\land R)$ |
|---|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |

Por tanto:

$$
(P\land Q)\land R
\equiv
P\land(Q\land R).
$$

Para la disyunción obtenemos:

| $P$ | $Q$ | $R$ | $(P\lor Q)\lor R$ | $P\lor(Q\lor R)$ |
|---|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |

Así:

$$
(P\lor Q)\lor R
\equiv
P\lor(Q\lor R).
$$

Estas son las **leyes asociativas**.

---

### 8.8 Primer paquete de leyes

Podemos reunir lo anterior en un solo resultado.

::: {.ma-block .ma-enunciado #apm-i-p0002}
**Proposición — Primeras leyes del álgebra proposicional**

Para fórmulas proposicionales arbitrarias $P,Q,R$, una tautología $T$ y una contradicción $C$, se cumplen las siguientes equivalencias.

**Identidad**

$$
P\land T\equiv P,
\qquad
P\lor C\equiv P.
$$

**Dominación**

$$
P\lor T\equiv T,
\qquad
P\land C\equiv C.
$$

**Idempotencia**

$$
P\land P\equiv P,
\qquad
P\lor P\equiv P.
$$

**Complemento**

$$
P\lor\neg P\equiv T,
\qquad
P\land\neg P\equiv C.
$$

**Doble negación**

$$
\neg\neg P\equiv P.
$$

**Conmutatividad**

$$
P\land Q\equiv Q\land P,
\qquad
P\lor Q\equiv Q\lor P.
$$

**Asociatividad**

$$
(P\land Q)\land R\equiv P\land(Q\land R),
$$

$$
(P\lor Q)\lor R\equiv P\lor(Q\lor R).
$$
:::

#### Demostración

Las tablas y argumentos semánticos de §§8.2–8.7 muestran, para cada familia, que las fórmulas situadas a ambos lados de $\equiv$ reciben el mismo valor en todas las asignaciones.

Por [la definición «Equivalencia lógica»](#apm-i-d0021), eso es exactamente afirmar que son lógicamente equivalentes.

Por tanto, todas las equivalencias enunciadas quedan demostradas.

---

### 8.9 Por qué podemos reemplazar una subfórmula por otra equivalente

Para calcular algebraicamente necesitamos hacer explícita una operación que hasta ahora hemos usado solo de manera intuitiva.

Supongamos $A\equiv B$. Entonces, en cada asignación, $A$ y $B$ reciben el mismo valor.

Por tanto:

- $\neg A$ y $\neg B$ también reciben el mismo valor;
- $A\land R$ y $B\land R$ reciben el mismo valor;
- $A\lor R$ y $B\lor R$ reciben el mismo valor.

Lo mismo vale si $A$ y $B$ aparecen a la derecha:

$$
R\land A\equiv R\land B,
$$

$$
R\lor A\equiv R\lor B.
$$

La razón es puramente semántica: si sustituimos una entrada por otra que tiene exactamente el mismo valor en cada fila, la operación exterior recibe las mismas entradas y produce el mismo resultado.

Así podremos utilizar una ley **dentro de una fórmula mayor**.

::: {.ma-block .ma-intuicion}
**Idea clave**

Reemplazar una subfórmula por otra equivalente está permitido porque la equivalencia garantiza igualdad de valores de verdad fila por fila.
:::

No necesitamos todavía una teoría general de sustitución para fórmulas arbitrarias. Estas observaciones locales bastan para las reescrituras con $\neg,\land,\lor$ que realizaremos ahora.

---

### 8.10 De tabla a cálculo

Una vez que una ley está demostrada, ya no necesitamos reconstruir su tabla cada vez.

Por ejemplo, $P\lor P\equiv P$ puede utilizarse directamente como idempotencia. Y:

$$
\neg\neg P\equiv P
$$

puede utilizarse directamente como doble negación. Esto cambia el modo de trabajo.

Antes:

$$
\text{fórmula}
\longrightarrow
\text{tabla completa}
\longrightarrow
\text{equivalencia}.
$$

Ahora empezamos a disponer de:

$$
\text{fórmula}
\longrightarrow
\text{cadena de leyes}
\longrightarrow
\text{forma equivalente}.
$$

Pero cada paso debe citar una ley válida.

---

### 8.11 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-i-x0016}
**Ejemplo — Simplificar sin reconstruir una tabla completa**
:::

Simplifiquemos:

$$
(P\land P)\lor(Q\land\neg Q).
$$

Comenzamos por la idempotencia:

$$
(P\land P)\lor(Q\land\neg Q)
\equiv
P\lor(Q\land\neg Q).
$$

Por complemento:

$$
Q\land\neg Q\equiv C.
$$

Podemos sustituir esa subfórmula:

$$
P\lor(Q\land\neg Q)
\equiv
P\lor C.
$$

Finalmente, por identidad:

$$
P\lor C
\equiv
P.
$$

Por tanto:

$$

(P\land P)\lor(Q\land\neg Q)
\equiv
P.

$$

La cadena completa puede presentarse de manera compacta:

$$
\begin{aligned}
(P\land P)\lor(Q\land\neg Q)
&\equiv P\lor(Q\land\neg Q)
&&\text{(idempotencia)}\\
&\equiv P\lor C
&&\text{(complemento)}\\
&\equiv P
&&\text{(identidad).}
\end{aligned}
$$

Este es el nuevo tipo de cálculo que iremos desarrollando.

---
## Ejercicios

### Simplificaciones elementales {#apm-i-e0102}
Simplifica mediante [la proposición «Primeras leyes del álgebra proposicional»](#apm-i-p0002) y justifica cada paso.

#### a)

$$
\neg\neg(P\lor P)
$$

#### b)

$$
(P\land\neg P)\lor Q
$$

#### Solución


#### a)

Por idempotencia:

$$
P\lor P\equiv P.
$$

Sustituyendo dentro de la doble negación:

$$
\neg\neg(P\lor P)
\equiv
\neg\neg P.
$$

Por doble negación:

$$
\neg\neg P\equiv P.
$$

Por tanto:

$$
\boxed{
\neg\neg(P\lor P)\equiv P.
}
$$

#### b)

Por complemento:

$$
P\land\neg P\equiv C.
$$

Entonces:

$$
(P\land\neg P)\lor Q
\equiv
C\lor Q.
$$

Por conmutatividad:

$$
C\lor Q
\equiv
Q\lor C.
$$

Por identidad:

$$
Q\lor C\equiv Q.
$$

Así:

$$
\boxed{
(P\land\neg P)\lor Q\equiv Q.
}
$$

---

### Reordenar y eliminar repeticiones {#apm-i-e0103}
Simplifica:

$$
(P\land Q)\land P.
$$

Utiliza únicamente asociatividad, conmutatividad e idempotencia.

#### Solución


Por asociatividad:

$$
(P\land Q)\land P
\equiv
P\land(Q\land P).
$$

Por conmutatividad dentro del paréntesis:

$$
P\land(Q\land P)
\equiv
P\land(P\land Q).
$$

Por asociatividad en sentido inverso:

$$
P\land(P\land Q)
\equiv
(P\land P)\land Q.
$$

Por idempotencia:

$$
(P\land P)\land Q
\equiv
P\land Q.
$$

Por tanto:

$$
\boxed{
(P\land Q)\land P
\equiv
P\land Q.
}
$$

---

### Justificar la conmutatividad {#apm-i-e0104}
Demuestra mediante una tabla que:

$$
P\lor Q
\equiv
Q\lor P.
$$

Explica después por qué esa tabla autoriza a utilizar la conmutatividad de $\lor$ como ley de reescritura.

#### Solución


| $P$ | $Q$ | $P\lor Q$ | $Q\lor P$ |
|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ |

Las dos columnas coinciden en toda la tabla.

Por definición:

$$
P\lor Q\equiv Q\lor P.
$$

Como la equivalencia ya ha sido demostrada para fórmulas arbitrarias $P,Q$, puede reutilizarse como ley sin reconstruir esta tabla en cada aplicación.

---

### Justificar una equivalencia derivada {#apm-i-e0105}
Demuestra mediante una cadena de leyes que:

$$
\neg\neg(P\land P)
\equiv
P.
$$

Indica la ley usada en cada paso.

#### Solución


Por doble negación:

$$
\neg\neg(P\land P)
\equiv
P\land P.
$$

Por idempotencia:

$$
P\land P
\equiv
P.
$$

Por tanto:

$$
\boxed{
\neg\neg(P\land P)
\equiv
P.
}
$$

Cada paso utiliza una ley ya demostrada en [la proposición «Primeras leyes del álgebra proposicional»](#apm-i-p0002).

---

### ¿Por qué la identidad vale para cualquier tautología? {#apm-i-e0106}
Sea $T$ una tautología cualquiera.

Justifica directamente desde las definiciones, sin elegir una fórmula tautológica particular, que:

$$
P\land T\equiv P.
$$

#### Solución


Como $T$ es una tautología, en toda asignación:

$$
T=\mathrm V.
$$

Consideremos cualquier fila.

Si:

$$
P=\mathrm V,
$$

entonces:

$$
P\land T
=
\mathrm V\land\mathrm V
=
\mathrm V,
$$

que coincide con el valor de $P$.

Si:

$$
P=\mathrm F,
$$

entonces:

$$
P\land T
=
\mathrm F\land\mathrm V
=
\mathrm F,
$$

que nuevamente coincide con el valor de $P$.

Por tanto, en cada asignación:

$$
P\land T
$$

y:

$$
P
$$

tienen el mismo valor.

Luego:

$$
\boxed{
P\land T\equiv P.
}
$$

La demostración no depende de qué tautología concreta representa $T$.

---

### Explorar la dualidad de las primeras leyes {#apm-i-e0107}
Observa las parejas:

$$
P\land T\equiv P,
\qquad
P\lor C\equiv P,
$$

y:

$$
P\lor T\equiv T,
\qquad
P\land C\equiv C.
$$

#### a)

¿Qué ocurre al intercambiar simultáneamente $\land$ con $\lor$ y los papeles de $T$ y $C$?

#### b)

Busca el mismo patrón en las leyes de complemento.

#### c)

Formula con tus palabras la regularidad observada, sin convertirla todavía en una nueva ley formal.

#### Solución


#### a)

La primera ley de identidad:

$$
P\land T\equiv P
$$

se transforma en:

$$
P\lor C\equiv P,
$$

que es la segunda ley de identidad.

Del mismo modo:

$$
P\lor T\equiv T
$$

se transforma en:

$$
P\land C\equiv C.
$$

#### b)

Las leyes:

$$
P\lor\neg P\equiv T
$$

y:

$$
P\land\neg P\equiv C
$$

también se intercambian al permutar $\lor$ con $\land$ y $T$ con $C$.

#### c)

Las primeras leyes aparecen organizadas en parejas: al intercambiar conjunción y disyunción, y simultáneamente tautología y contradicción, varias leyes se transforman unas en otras.

Esta regularidad sugiere una simetría interna del álgebra proposicional. Por ahora la registramos como observación estructural.

---

### Síntesis: una cadena larga {#apm-i-e0108}
Simplifica:

$$
\neg\neg\Bigl(((P\land Q)\land P)\lor(R\land\neg R)\Bigr)
\land
(S\lor\neg S).
$$

Utiliza únicamente las leyes de [la proposición «Primeras leyes del álgebra proposicional»](#apm-i-p0002). Justifica cada paso importante.

#### Solución


Comenzamos por la doble negación:

$$
\begin{aligned}
&\neg\neg\Bigl(((P\land Q)\land P)\lor(R\land\neg R)\Bigr)
\land
(S\lor\neg S)
\\
&\equiv
\Bigl(((P\land Q)\land P)\lor(R\land\neg R)\Bigr)
\land
(S\lor\neg S).
\end{aligned}
$$

En [el ejercicio «Reordenar y eliminar repeticiones»](#apm-i-e0103) vimos, usando asociatividad, conmutatividad e idempotencia, que:

$$
(P\land Q)\land P
\equiv
P\land Q.
$$

Sustituimos:

$$
\equiv
\Bigl((P\land Q)\lor(R\land\neg R)\Bigr)
\land
(S\lor\neg S).
$$

Por complemento:

$$
R\land\neg R\equiv C,
$$

de modo que:

$$
\equiv
\bigl((P\land Q)\lor C\bigr)
\land
(S\lor\neg S).
$$

Por identidad:

$$
(P\land Q)\lor C
\equiv
P\land Q.
$$

Entonces:

$$
\equiv
(P\land Q)\land(S\lor\neg S).
$$

Por complemento:

$$
S\lor\neg S\equiv T.
$$

Así:

$$
\equiv
(P\land Q)\land T.
$$

Finalmente, por identidad:

$$
(P\land Q)\land T
\equiv
P\land Q.
$$

Por tanto:

$$
\boxed{
\neg\neg\Bigl(((P\land Q)\land P)\lor(R\land\neg R)\Bigr)
\land
(S\lor\neg S)
\equiv
P\land Q.
}
$$

---

## Síntesis

En esta sección hemos dado el paso decisivo desde la semántica hacia el cálculo.

Primero establecimos por tablas o argumentos semánticos las leyes de:

- identidad;
- dominación;
- idempotencia;
- complemento;
- doble negación;
- conmutatividad;
- asociatividad.

Todas quedaron reunidas en:

$$
\texttt{[la proposición «Primeras leyes del álgebra proposicional»](#apm-i-p0002)}.
$$

Después justificamos por qué una subfórmula puede reemplazarse localmente por otra equivalente dentro de:

$$
\neg,\qquad\land,\qquad\lor.
$$

Con ello aparecen verdaderas cadenas de cálculo:

$$
F_0
\equiv
F_1
\equiv
\cdots
\equiv
F_n,
$$

donde cada paso debe indicar la ley que lo autoriza.

La diferencia con una manipulación meramente simbólica es esencial:

$$

\text{no movemos símbolos porque «parece funcionar»;}
\quad
\text{reescribimos mediante equivalencias ya demostradas}.

$$

---

## Hacia la sección siguiente

Nuestro primer paquete de leyes todavía está incompleto. En álgebra elemental, una operación puede distribuirse sobre otra.

En lógica proposicional ocurre algo particularmente interesante: la conjunción y la disyunción presentan una simetría mucho más fuerte de la que encontramos en la aritmética.

Además aparecerán dos herramientas decisivas:

- absorción;
- leyes de De Morgan.

La siguiente sección desarrollará:
