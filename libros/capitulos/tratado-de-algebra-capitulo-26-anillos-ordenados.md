---
title: 'Tratado moderno de Álgebra — Capítulo 26: Anillos ordenados'
description: Capítulo del Tratado moderno de Álgebra dedicado a anillos ordenados, publicado desde la fuente canónica cerrada del tratado.
author: Gustav A. Tachek
content-id: MA-BCH-0062
content-type: book-chapter
book-id: MA-BOK-0007
status: published
date-created: '2026-09-19'
date-modified: '2026-09-26'
areas:
- algebra
- fundamentos
level: avanzado
topics:
- algebra
- estructuras-algebraicas
prerequisites:
- MA-BCH-0050
related:
- MA-BOK-0007
- MA-BCH-0050
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 26 — Anillos ordenados

## 26.0. El problema: hacer compatible el orden con dos operaciones

Un grupo ordenado combina una operación con una relación de orden. Un anillo introduce una dificultad nueva: sobre el mismo conjunto conviven **suma** y **multiplicación**, y el orden no interactúa con ambas de la misma manera.

Para la suma, la compatibilidad natural es global. Si

$$
a\le b,
$$

entonces añadir el mismo elemento a ambos miembros debe conservar la comparación:

$$
a+c\le b+c.
$$

Eso ya está contenido en la teoría de grupos ordenados del capítulo anterior.

La multiplicación exige más cuidado. No sería correcto postular que multiplicar una desigualdad por un elemento arbitrario conserva siempre el sentido del orden. La experiencia elemental con los números muestra precisamente el obstáculo: el signo del factor importa. Por ello la compatibilidad multiplicativa se formulará en torno a la región no negativa.

La pregunta estructural es entonces:

> **¿qué condición mínima debe relacionar multiplicación y orden para que la noción de “producto de elementos no negativos” tenga el comportamiento esperado?**

La respuesta será exigir que la no negatividad sea estable bajo multiplicación.

> **Profundidad pedagógica — P3.** El punto cognitivo central de este capítulo es distinguir tres capas: la estructura aditiva ordenada, la estructura multiplicativa del anillo y la ley que las conecta. No se debe trasladar mecánicamente a la multiplicación la regla de monotonía de la suma. La dirección correcta será primero fijar la estabilidad de los no negativos y, después, deducir de ella reglas de monotonía multiplicativa bajo hipótesis de signo.

La Parte V continúa siendo estrictamente algebraico-ordenada. En particular, en este capítulo no se introducen completitud, supremos, convergencia ni propiedades arquimedianas.

---

## 26.1. De grupo aditivo ordenado a anillo ordenado

El capítulo 14 fijó que un anillo

$$
\mathcal R=\langle R,+,\cdot\rangle
$$

tiene como estructura aditiva un grupo abeliano. El capítulo 25 fijó qué significa dotar a un grupo de un orden parcial compatible con sus traslaciones.

Por tanto, la primera parte de la definición siguiente no crea una nueva noción de compatibilidad aditiva: reutiliza exactamente la Definición 25.2.1 sobre el grupo

$$
\langle R,+\rangle.
$$

La segunda parte es genuinamente nueva y conecta el orden con la multiplicación.

### Definición 26.1.1 — Anillo ordenado {#talg-def-00059}

Sea

$$
\mathcal R=\langle R,+,\cdot\rangle
$$

un anillo y sea $\le$ un orden parcial sobre $R$. Diremos que la estructura

$$
\langle R,+,\cdot,\le\rangle
$$

es un **anillo ordenado** si se cumplen las dos condiciones siguientes:

1. el grupo aditivo

   $$
   \langle R,+\rangle
   $$

   junto con $\le$ es un grupo ordenado;

2. para todos $a,b\in R$,

   $$
   \boxed{
   0\le a\ \land\ 0\le b
   \Longrightarrow
   0\le a\cdot b.
   }
   $$

La expresión $\langle R,+,\cdot,\le\rangle$ es una abreviatura tipográfica de una codificación conjuntista mediante pares anidados; no introduce una cuádrupla primitiva.

La segunda condición puede leerse así:

$$
\boxed{
\text{no negativo}\times\text{no negativo}
\Longrightarrow
\text{no negativo}.
}
$$

Es la compatibilidad multiplicativa básica del anillo ordenado.

---

## 26.2. Qué exige —y qué no exige— la definición

La definición tiene una arquitectura deliberadamente austera.

### 26.2.1. La suma ya aporta la invariancia por traslación

Como $\langle R,+\rangle$ es abeliano, la compatibilidad bilateral de la Definición 25.2.1 se reduce, por el Corolario 25.3.2, a la regla familiar

$$
a\le b
\Longrightarrow
 a+c\le b+c.
$$

No es necesario añadir esta condición de nuevo como un axioma independiente del anillo ordenado.

### 26.2.2. La multiplicación no se declara monótona para factores arbitrarios

No se postula

$$
a\le b
\Longrightarrow
ac\le bc
$$

para todo $c\in R$.

Una regla de ese tipo sólo será válida bajo hipótesis apropiadas sobre el signo de $c$. Precisamente por eso la definición parte de la estabilidad multiplicativa de los no negativos. Las reglas de monotonía se demostrarán después; no se incorporan clandestinamente a la definición.

### 26.2.3. El orden no tiene por qué ser total

Un anillo ordenado, en el sentido fijado aquí, puede poseer elementos incomparables. No se exige

$$
a\le b\ \lor\ b\le a.
$$

La totalidad será una condición adicional cuando resulte necesaria.

### 26.2.4. La multiplicación no tiene por qué ser conmutativa

La palabra *anillo* conserva la convención establecida en la Definición 14.1.1: la multiplicación es asociativa y unital, pero no necesariamente conmutativa.

Por ello la definición de anillo ordenado tampoco añade conmutatividad. En desarrollos posteriores será importante distinguir, cuando corresponda, multiplicación por la izquierda y por la derecha.

### 26.2.5. No se postula todavía positividad estricta

La condición

$$
0\le a,
\qquad
0\le b
$$

implica solamente

$$
0\le ab.
$$

No se reemplaza por una afirmación estricta del tipo

$$
0<a,
\qquad
0<b
\Longrightarrow
0<ab.
$$

Tal fortalecimiento interactúa con divisores de cero, no trivialidad y totalidad, y debe analizarse por separado.

### 26.2.6. No se impone $0<1$

La definición general tampoco incorpora

$$
0<1.
$$

El tratado ya distingue la estructura de anillo de su no trivialidad, y aquí mantendremos esa separación. Cuando se introduzcan estructuras ordenadas más fuertes, las condiciones necesarias sobre $0$ y $1$ se deducirán o se añadirán explícitamente, según corresponda.

### 26.2.7. Totalidad no significa decidibilidad

Incluso si más adelante el orden se supone total, la afirmación

$$
a\le b\ \lor\ b\le a
$$

no se identificará con la existencia de un algoritmo que decida cuál de las dos relaciones se cumple. Del mismo modo, esta definición no establece decidibilidad de la igualdad, de la no negatividad ni de la comparación.

---

## 26.3. Cambio de representación: del orden al sector no negativo

La definición anterior puede leerse desde el cono no negativo del grupo aditivo. Si

$$
P_{\mathcal R}
=
\{a\in R:0\le a\},
$$

entonces la condición multiplicativa nueva dice precisamente que

$$
a,b\in P_{\mathcal R}
\Longrightarrow
ab\in P_{\mathcal R}.
$$

Es decir, al pasar de grupos ordenados a anillos ordenados, el cono no negativo no sólo debe codificar el orden aditivo: debe ser además **cerrado bajo la multiplicación del anillo**.

Este cambio de representación será útil porque concentra la interacción entre las dos operaciones en un solo subconjunto estructuralmente distinguido.

> **Autoexplicación.** En un grupo ordenado, el cono responde a la pregunta «¿qué elementos están por encima del origen?». En un anillo ordenado aparece una pregunta adicional: «¿qué hace la multiplicación con esa región?». La nueva exigencia responde: la mantiene cerrada.

---

## 26.4. Prueba de estrés de la definición

Antes de usar la nueva noción conviene separar afirmaciones que la definición **sí** proporciona de otras que todavía requieren demostración.

| Afirmación | Estado tras la Definición 26.1.1 |
|---|---|
| $a\le b\Rightarrow a+c\le b+c$ | disponible por la estructura aditiva ordenada |
| $0\le a$ y $0\le b\Rightarrow0\le ab$ | axioma multiplicativo de la definición |
| $a\le b$ y $0\le c\Rightarrow ac\le bc$ | demostrado en la Proposición 26.6.1 |
| $a\le b$ y $0\le c\Rightarrow ca\le cb$ | demostrado en la Proposición 26.6.1 |
| $a\le b$ y $c\le0\Rightarrow bc\le ac$ | demostrado en la Proposición 26.8.1 |
| $a\le b$ y $c\le0\Rightarrow cb\le ca$ | demostrado en la Proposición 26.8.1 |
| $a\le0$ y $b\le0\Rightarrow0\le ab$ | demostrado en el Corolario 26.10.1 |
| $0<a$ y $0<b\Rightarrow0<ab$ | no establecido |
| $a\le b\lor b\le a$ | no establecido |
| $ab=ba$ | no establecido |
| $0<1$ | no establecido |
| comparabilidad decidible | no establecido |

La distinción evita un error frecuente: leer como parte de la definición propiedades que en realidad dependen de distributividad, reglas de signos, hipótesis de no negatividad o condiciones estructurales posteriores.

---

## 26.6. Monotonía multiplicativa bajo una hipótesis de signo

La Definición 26.1.1 no declara que la multiplicación preserve el orden. Lo que declara es algo más elemental: el producto de dos elementos no negativos vuelve a ser no negativo. Ahora podemos convertir esa estabilidad en una regla de comparación.

La idea de la demostración tiene tres movimientos:

```text
a ≤ b
↓ trasladar por -a
0 ≤ b + (-a)
↓ multiplicar por un elemento no negativo
0 ≤ diferencia de los productos
↓ trasladar de nuevo
comparación entre los productos
```

El paso central es exactamente el lugar donde se necesita la hipótesis de signo sobre el factor.

### Proposición 26.6.1 — Monotonía multiplicativa por factores no negativos {#talg-pro-00068}

Sea

$$
\langle R,+,\cdot,\le\rangle
$$

un anillo ordenado. Para cualesquiera $a,b,c\in R$, si

$$
a\le b
\qquad\text{y}\qquad
0\le c,
$$

entonces

$$
a\cdot c\le b\cdot c.
$$

y

$$
c\cdot a\le c\cdot b.
$$

Es decir: multiplicar por un elemento no negativo preserva el orden tanto por la derecha como por la izquierda.

#### Demostración {#talg-prf-00109}

Supongamos

$$
a\le b
$$

y

$$
0\le c.
$$

Como el grupo aditivo de un anillo ordenado es un grupo ordenado, podemos trasladar la primera desigualdad por $-a$. Obtenemos

$$
(-a)+a
\le
(-a)+b.
$$

El miembro izquierdo es $0$ y, por conmutatividad de la suma,

$$
0\le b+(-a).
$$

Ahora tanto $b+(-a)$ como $c$ son no negativos. Por la condición multiplicativa de la Definición 26.1.1,

$$
0\le \bigl(b+(-a)\bigr)\cdot c.
$$

Usando distributividad por la derecha y la regla de signos de la Proposición 14.4.1,

$$
(b+(-a))\cdot c
= b\cdot c+(-a)\cdot c
= b\cdot c+(-(a\cdot c)).
$$

Por tanto,

$$
0\le b\cdot c+\bigl(-(a\cdot c)\bigr).
$$

Trasladando ahora por $a\cdot c$ en el grupo aditivo ordenado,

$$
a\cdot c
\le
a\cdot c+\bigl(b\cdot c+(-(a\cdot c))\bigr).
$$

Por asociatividad y conmutatividad de la suma, el miembro derecho se reduce a $b\cdot c$. Luego

$$
a\cdot c\le b\cdot c.
$$

Para la multiplicación por la izquierda partimos de la misma desigualdad

$$
0\le b+(-a).
$$

Como $0\le c$, la definición de anillo ordenado da

$$
0\le c\cdot\bigl(b+(-a)\bigr).
$$

Por distributividad por la izquierda y la regla de signos,

$$
c\cdot(b+(-a))
= c\cdot b+c\cdot(-a)
= c\cdot b+(-(c\cdot a)).
$$

Así,

$$
0\le c\cdot b+\bigl(-(c\cdot a)\bigr).
$$

Trasladando por $c\cdot a$,

$$
c\cdot a\le c\cdot b.
$$

Esto demuestra ambas afirmaciones. $\square$

> **Dónde trabaja la hipótesis $0\le c$.** No se utiliza para trasladar la desigualdad $a\le b$; esa tarea pertenece al grupo aditivo ordenado. Se utiliza exactamente cuando pasamos de $0\le b+(-a)$ a la no negatividad de su producto con $c$.

> **Error plausible.** De $a\le b$ no puede escribirse inmediatamente $ac\le bc$ sólo porque el anillo esté ordenado. Esa conclusión requiere controlar el signo de $c$. La definición no contiene una monotonía multiplicativa global.

> **Lateralidad.** Las dos conclusiones se demuestran por separado. En un anillo no conmutativo, $a\cdot c$ y $c\cdot a$ no son intercambiables y una de las dos desigualdades no debe obtenerse de la otra por una conmutatividad inexistente.

---

## 26.8. Multiplicar por un factor no positivo invierte el orden

La Proposición 26.6.1 resolvió el caso de un factor no negativo: la multiplicación preserva el orden. El caso no positivo no exige un axioma nuevo. La inversión del sentido de la desigualdad se obtiene convirtiendo primero el factor en uno no negativo mediante el opuesto aditivo.

El mecanismo puede leerse así:

```text
c ≤ 0
↓ tomar opuestos
0 ≤ -c
↓ aplicar monotonía multiplicativa
productos con -c conservan el orden
↓ reescribir signos y tomar opuestos
los productos con c invierten el orden
```

Este argumento contiene **dos inversiones de signo distintas**: una sobre el factor, que permite usar la Proposición 26.6.1, y otra sobre los productos, que revierte la comparación final.

### Proposición 26.8.1 — Antitonicidad multiplicativa por factores no positivos {#talg-pro-00069}

Sea

$$
\langle R,+,\cdot,\le\rangle
$$

un anillo ordenado. Para cualesquiera $a,b,c\in R$, si

$$
a\le b
\qquad\text{y}\qquad
c\le0,
$$

entonces

$$
b\cdot c\le a\cdot c
$$

y

$$
c\cdot b\le c\cdot a.
$$

Es decir: multiplicar por un elemento no positivo invierte el orden tanto por la derecha como por la izquierda.

#### Demostración {#talg-prf-00110}

Supongamos

$$
a\le b
$$

y

$$
c\le0.
$$

Como el grupo aditivo de un anillo ordenado es un grupo ordenado, trasladamos

$$
c\le0
$$

por $-c$. Obtenemos

$$
c+(-c)\le0+(-c),
$$

y por las leyes del grupo aditivo,

$$
0\le -c.
$$

Ya podemos aplicar la Proposición 26.6.1 al factor no negativo $-c$. Por multiplicación a la derecha,

$$
a\cdot(-c)\le b\cdot(-c).
$$

Por las reglas de signos de la Proposición 14.4.1,

$$
-(a\cdot c)\le -(b\cdot c).
$$

Aplicando nuevamente la Proposición 25.4.1, ahora a esta desigualdad del grupo aditivo, la inversión revierte el orden y obtenemos

$$
b\cdot c\le a\cdot c.
$$

Para la multiplicación por la izquierda, la misma Proposición 26.6.1 da

$$
(-c)\cdot a\le(-c)\cdot b.
$$

Las reglas de signos transforman esta desigualdad en

$$
-(c\cdot a)\le -(c\cdot b).
$$

Aplicando otra vez la antitonicidad del opuesto aditivo,

$$
c\cdot b\le c\cdot a.
$$

Quedan demostradas ambas lateralidades. $\square$

> **Caso frontera.** La hipótesis es $c\le0$, no $c<0$. Si $c=0$, ambas conclusiones se reducen a $0\le0$. Por eso el resultado es antitónico en sentido no estricto.

> **Error plausible.** No basta recordar la regla escolar «multiplicar por un negativo cambia el signo». Aquí hay que justificarla estructuralmente: primero se convierte $c\le0$ en $0\le-c$; después se usa la monotonía ya demostrada para factores no negativos; finalmente las reglas de signos y la antitonicidad del opuesto producen la inversión de la desigualdad.

> **Lateralidad.** Tampoco aquí se usa conmutatividad multiplicativa. Las desigualdades $bc\le ac$ y $cb\le ca$ proceden de las dos lateralidades distintas de la Proposición 26.6.1.

---

## 26.10. El producto de dos elementos no positivos

La Proposición 26.8.1 permite extraer una regla de signos ordenada sin convertirla en un axioma independiente. Si ambos factores están por debajo de $0$, uno de ellos puede usarse como factor no positivo aplicado a la comparación del otro con $0$.

El mecanismo es mínimo:

```text
a ≤ 0,  b ≤ 0
↓ usar b como factor no positivo sobre a ≤ 0
0·b ≤ a·b
↓ absorción del cero
0 ≤ a·b
```

### Corolario 26.10.1 — Producto de dos elementos no positivos es no negativo {#talg-cor-00017}

Sea

$$
\langle R,+,\cdot,\le\rangle
$$

un anillo ordenado. Si $a,b\in R$ satisfacen

$$
a\le0
\qquad\text{y}\qquad
b\le0,
$$

entonces

$$
0\le a\cdot b.
$$

#### Demostración {#talg-prf-00111}

Partimos de

$$
a\le0
$$

y usamos $b\le0$ como hipótesis de signo para multiplicar por la derecha. Por la Proposición 26.8.1,

$$
0\cdot b\le a\cdot b.
$$

La Proposición 14.3.1 da

$$
0\cdot b=0.
$$

Por tanto,

$$
0\le a\cdot b.
$$

$\square$

> **Lectura estructural.** La regla escolar «negativo por negativo da positivo» aparece aquí en una forma más precisa: *no positivo por no positivo es no negativo*. No se postula como una ley de signos adicional; se deduce de la antitonicidad multiplicativa y de la absorción del cero.

> **Sin conmutatividad.** La prueba no intercambia los factores. También podría usarse la lateralidad izquierda de la Proposición 26.8.1 sobre $b\le0$ con factor $a\le0$, pero no es necesario identificar $ab$ con $ba$.

> **Frontera lógica.** El corolario no afirma que $ab>0$ cuando $a<0$ y $b<0$. La positividad estricta requiere hipótesis adicionales y permanece fuera de este nodo.

---

## 26.12. Cuando todas las parejas son comparables

La noción general de anillo ordenado no exige que dos elementos cualesquiera puedan compararse. Para algunos resultados, sin embargo, la totalidad del orden permite convertir una propiedad local de signo en una dicotomía exhaustiva.

La nueva estructura no altera las leyes del anillo ni fortalece por sí misma la compatibilidad multiplicativa. Añade únicamente comparabilidad global:

$$
\text{anillo ordenado}
\quad+\quad
\text{orden total}
\quad\Longrightarrow\quad
\text{anillo totalmente ordenado}.
$$

### Definición 26.12.1 — Anillo totalmente ordenado {#talg-def-00060}

Un **anillo totalmente ordenado** es un anillo ordenado

$$
\langle R,+,\cdot,\le\rangle
$$

cuyo grupo aditivo ordenado es un grupo totalmente ordenado.

Equivalentemente, además de las condiciones de la Definición 26.1.1, la relación $\le$ es un orden total sobre $R$. Por tanto, para cualesquiera $a,b\in R$,

$$
a\le b\ \lor\ b\le a.
$$

Esta disyunción expresa **totalidad matemática**, no un procedimiento que decida cuál comparación vale para elementos dados.

> **Separación conceptual.** Un anillo ordenado puede tener elementos incomparables; un anillo totalmente ordenado no. La nueva palabra no añade conmutatividad multiplicativa, no exige $0<1$, no impone no trivialidad y no convierte automáticamente la comparación en una operación computable.

> **Por qué importa.** La totalidad permite ahora aplicar argumentos por casos de signo. En particular, para cualquier $a\in R$ podremos usar la comparación entre $a$ y $0$ para distinguir los casos $0\le a$ y $a\le0$. Esa dicotomía será el mecanismo del siguiente resultado sobre cuadrados.

---

## 26.14. Por qué la totalidad garantiza la no negatividad de los cuadrados

La condición multiplicativa de la Definición 26.1.1 sólo controla directamente productos cuyos dos factores son no negativos. El Corolario 26.10.1 aporta el segundo caso: también es no negativo el producto de dos factores no positivos. Para aplicar una de estas reglas a un elemento arbitrario necesitamos saber que se encuentra en al menos uno de los dos sectores.

La totalidad proporciona exactamente la disyunción que falta:

$$
0\le a\ \lor\ a\le0.
$$

Ambas alternativas pueden cumplirse simultáneamente cuando $a=0$. No necesitamos elegir una de manera exclusiva ni disponer de un algoritmo que decida el signo: basta con demostrar la misma conclusión bajo cada hipótesis.

Escribiremos $a^2$ como abreviatura local del producto $a\cdot a$; no se introduce en este punto una teoría general de potencias.

### Proposición 26.14.1 — Todo cuadrado es no negativo en un anillo totalmente ordenado {#talg-pro-00070}

Sea

$$
\langle R,+,\cdot,\le\rangle
$$

un anillo totalmente ordenado. Para todo $a\in R$,

$$
0\le a^2,
\qquad a^2:=a\cdot a.
$$

#### Demostración {#talg-prf-00112}

Fijemos $a\in R$. Como el orden es total por la Definición 26.12.1, aplicándolo a los elementos $0$ y $a$ obtenemos

$$
0\le a\ \lor\ a\le0.
$$

**Primer caso: $0\le a$.** Aplicamos la condición multiplicativa de la Definición 26.1.1 a los dos factores iguales $a$ y $a$. Resulta

$$
0\le a\cdot a.
$$

**Segundo caso: $a\le0$.** Aplicamos el Corolario 26.10.1 a los dos factores iguales $a$ y $a$. Obtenemos igualmente

$$
0\le a\cdot a.
$$

Puesto que ambas alternativas de la disyunción conducen a la misma desigualdad, concluimos por eliminación de la disyunción que

$$
0\le a^2.
$$

$\square$

> **Dónde trabaja la totalidad.** No se usa para multiplicar desigualdades: ambas reglas multiplicativas ya estaban demostradas para anillos parcialmente ordenados. Se usa exclusivamente para garantizar que un $a$ arbitrario satisface $0\le a$ o $a\le0$.

> **Dos casos no significa un test computable.** La demostración deduce una conclusión común a partir de una disyunción matemática. No construye una función que, dado $a$, devuelva su signo; tampoco demuestra la decidibilidad de $a\le0$ ni de $a=0$.

> **Prueba de estrés: sin totalidad, la afirmación puede fallar.** En un anillo unitario no trivial provisto del *orden de igualdad*, definido por $x\le y$ si y sólo si $x=y$, la estructura aditiva está ordenada y el único elemento no negativo es $0$, cuyo producto consigo mismo vuelve a ser $0$. Así se satisfacen los axiomas de anillo ordenado. Sin embargo, $1^2=1\ne0$ y, para este orden, $0\nleq1^2$. La totalidad es una hipótesis suficiente real, no una decoración del enunciado.

> **Frontera.** El resultado no asegura que $a^2>0$ para todo $a\ne0$; tampoco presupone ausencia de divisores de cero, conmutatividad multiplicativa ni $0<1$.

---

## 26.16. La posición de la unidad multiplicativa

Hasta aquí no hemos añadido $0<1$ como parte de la definición de anillo ordenado. Ahora podemos **deducir la comparación no estricta** en un anillo totalmente ordenado, en lugar de introducirla como un axioma independiente. Para pasar de ella a una comparación estricta necesitaremos, y declararemos separadamente, la no trivialidad.

La estrategia consiste en aprovechar un elemento cuya multiplicación consigo mismo ya conocemos algebraicamente:

$$
1^2=1\cdot1=1.
$$

### Proposición 26.16.1 — La unidad es no negativa y, bajo no trivialidad, positiva {#talg-pro-00071}

Sea $\langle R,+,\cdot,\le\rangle$ un anillo totalmente ordenado, con unidad multiplicativa $1$ y neutro aditivo $0$. Entonces

$$
0\le1.
$$

Si además el anillo es **no trivial**, es decir, $0\ne1$, entonces

$$
0<1.
$$

#### Demostración {#talg-prf-00113}

Por la Proposición 26.14.1, todo cuadrado es no negativo. Apliquémosla al elemento $1\in R$:

$$
0\le1^2.
$$

La ley de unidad multiplicativa, contenida en la definición de anillo (Definición 14.1.1), establece que

$$
1^2=1\cdot1=1.
$$

Sustituyendo, obtenemos $0\le1$, sin haber supuesto que el anillo sea no trivial.

Supongamos ahora adicionalmente $0\ne1$, que es exactamente la condición de no trivialidad de la Definición 16.1.1. Según la definición del orden estricto asociado, recogida en la Interfaz 25.1.1,

$$
0<1\quad\Longleftrightarrow\quad 0\le1\ \land\ 0\ne1.
$$

Acabamos de demostrar ambas condiciones del segundo miembro; por tanto, $0<1$. $\square$

> **Lectura de la prueba.** La primera conclusión procede de un cuadrado y de la ley multiplicativa $1\cdot1=1$. La segunda no exige multiplicar otra desigualdad: añade exactamente la información $0\ne1$ que faltaba para usar la definición de $<$.

> **Prueba de estrés: retirar la no trivialidad.** En el anillo cero, $0=1$ y el único orden es total. Sigue siendo verdadero $0\le1$, por reflexividad, pero es falso $0<1$. Por ello no debe incorporarse la positividad estricta a la definición general de anillo totalmente ordenado.

> **Prueba de estrés: retirar la totalidad.** En un anillo no trivial con el orden de igualdad, $1$ es incomparable con $0$. Como se señaló tras la Proposición 26.14.1, ese orden satisface la definición de anillo ordenado, pero no se deduce $0\le1$. La hipótesis de totalidad no puede omitirse de este enunciado sin reemplazarla por alguna condición adicional.

> **Frontera deductiva.** De $0<1$ no se infiere todavía $0<ab$ para todos $0<a$ y $0<b$. La definición sólo garantiza $0\le ab$; convertir esa relación en estricta requiere excluir $ab=0$, lo que remite a hipótesis sobre divisores de cero.

---

## 26.18. De la no negatividad a la positividad del producto

La definición de anillo ordenado garantiza que el producto de dos elementos no negativos es no negativo. Si los factores son estrictamente positivos, no basta repetir esa misma conclusión y sustituir $\le$ por $<$: debemos excluir que el producto sea cero.

El mecanismo tiene dos pasos independientes:

```text
0 < a, 0 < b
↓ cierre multiplicativo del cono no negativo
0 ≤ a·b
+ hipótesis independiente a·b ≠ 0
↓ definición del orden estricto
0 < a·b
```

En un anillo general no necesariamente conmutativo, la condición global apropiada se expresará **sin ambigüedad lateral**:

$$
\forall x,y\in R,\qquad
(x\ne0\ \land\ y\ne0)\Longrightarrow x\cdot y\ne0.
$$

Esta propiedad es la ausencia de productos nulos formados por dos factores no nulos; en un anillo no trivial excluye las dos nociones laterales de divisor de cero de la Definición 16.2.1. No se ha añadido como axioma a la definición de anillo ordenado.

### Proposición 26.18.1 — Positividad estricta del producto bajo ausencia de divisores de cero {#talg-pro-00072}

Sea $\langle R,+,\cdot,\le\rangle$ un anillo ordenado, sin suponer que el orden sea total ni que la multiplicación sea conmutativa. Si $a,b\in R$ cumplen

$$
0<a,\qquad 0<b,\qquad a\cdot b\ne0,
$$

entonces

$$
0<a\cdot b.
$$

**En particular**, si el anillo satisface la condición global

$$
\forall x,y\in R,\qquad
(x\ne0\ \land\ y\ne0)\Longrightarrow x\cdot y\ne0,
$$

se cumple, para todos $a,b\in R$,

$$
0<a\ \land\ 0<b\Longrightarrow0<a\cdot b.
$$

#### Demostración {#talg-prf-00114}

Supongamos $0<a$ y $0<b$. Por la definición de orden estricto asociado (Interfaz 25.1.1), obtenemos

$$
0\le a,\qquad 0\le b,\qquad a\ne0,\qquad b\ne0.
$$

La condición multiplicativa de la Definición 26.1.1, aplicada a $a$ y $b$, proporciona

$$
0\le a\cdot b.
$$

Si además $a\cdot b\ne0$, la definición del orden estricto asociado permite concluir de inmediato

$$
0<a\cdot b.
$$

Esto establece el primer enunciado. Para el segundo, fijemos dos factores estrictamente positivos $a,b$. Ya hemos obtenido $a\ne0$ y $b\ne0$; la condición global asumida implica, por instanciación con $x=a$ e $y=b$, que $a\cdot b\ne0$. Aplicamos entonces el primer enunciado y concluimos $0<a\cdot b$. $\square$

> **Dónde trabaja cada hipótesis.** El orden del anillo sólo proporciona $0\le ab$. La exclusión de productos nulos sólo proporciona $ab\ne0$ cuando los factores son no nulos. El orden estricto asociado combina exactamente ambas informaciones. Ninguna de estas operaciones requiere comparar todos los pares de elementos del anillo.

> **Precisión terminológica.** En un anillo no trivial, excluir productos nulos de dos factores no nulos equivale a la ausencia de divisores de cero por la izquierda y, asimismo, por la derecha en el sentido de la Definición 16.2.1. La formulación universal evita ocultar una convención lateral. No se está afirmando que el anillo sea conmutativo ni se invoca la definición especializada de divisor de cero para anillos conmutativos.

> **Prueba de estrés: la totalidad no sustituye la hipótesis multiplicativa.** Construimos el ejemplo directamente sobre $E=\mathbb Z\times\mathbb Z$, usando los enteros importados en la [Interfaz 24.0.1](tratado-de-algebra-capitulo-24-cuerpo-de-fracciones-de-un-dominio-integro.md#talg-imp-00005). Para $x=(m,n)$, $y=(p,q)$, definimos
>
> $$
> x+y=(m+p,n+q),\qquad xy=(mp,mq+np).
> $$
>
> La suma es un grupo abeliano por coordenadas, con cero $(0,0)$ y opuesto $(-m,-n)$. El producto es conmutativo y tiene unidad $(1,0)$. Para $z=(r,s)$, ambos productos $(xy)z$ y $x(yz)$ son
>
> $$
> (mpr,mps+mqr+npr).
> $$
>
> Además, al expandir $x(y+z)$ se obtiene $(mp+mr,mq+ms+np+nr)=xy+xz$; la conmutatividad da la otra distributividad. Por tanto las operaciones definen un anillo conmutativo con identidad.
>
> Definimos el orden lexicográfico por
>
> $$
> (m,n)\le_{\rm lex}(p,q)
> \quad\Longleftrightarrow\quad m<p\ \lor\ (m=p\ \land\ n\le q).
> $$
>
> La tricotomía entera da totalidad. La reflexividad proviene de la igualdad de primeras coordenadas y de $n\le n$; dos comparaciones opuestas fuerzan igualdad en ambas coordenadas, de donde la antisimetría. En una cadena de dos comparaciones, si alguna primera coordenada aumenta estrictamente, también lo hace entre los extremos; si ambas permanecen iguales, la transitividad se reduce a las segundas coordenadas. Así se obtiene transitividad. Sumar un mismo par preserva las comparaciones estrictas y las igualdades de primeras coordenadas, y preserva el orden de las segundas: el orden es compatible con la suma.
>
> Falta comprobar la condición multiplicativa. Si $x,y\ge_{\rm lex}0$, sus primeras coordenadas son no negativas. Si $m,p>0$, entonces $mp>0$, y por ello $xy>_{\rm lex}0$. Si $m=0$, tenemos $n\ge0$ y $xy=(0,np)\ge_{\rm lex}0$. El caso $p=0$ es simétrico, con $q\ge0$ y $xy=(0,mq)\ge_{\rm lex}0$. Se han cubierto todos los casos. Esto verifica la Definición 26.1.1 y la totalidad del orden.
>
> Llamamos a este anillo el de **números duales enteros** y escribimos $\varepsilon=(0,1)$. Entonces $\varepsilon>0$, pero $\varepsilon^2=(0,0)$. Por tanto un anillo totalmente ordenado puede tener un producto nulo de factores estrictamente positivos bajo nuestra definición. La construcción por pares basta para este contraejemplo; no presupone una teoría de polinomios. No se utiliza como premisa de la proposición anterior.

> **No se ha probado una regla más fuerte de monotonía estricta.** El paso de $a<b$ a $ac<bc$ exige analizar el producto $(b+(-a))c$ y sus hipótesis de no nulidad. Queda reservado para un resultado posterior.

---

## 26.20. Una desigualdad estricta y el producto de su diferencia

La Proposición 26.6.1 afirma que un factor no negativo preserva una desigualdad no estricta. Cambiar simplemente el símbolo $\le$ por $<$ sería ilegítimo: si la diferencia entre ambos miembros se anula al multiplicarla por el factor, los productos pueden coincidir.

La estrategia correcta consiste en convertir la comparación inicial en una desigualdad respecto de cero:

```text
a < b
↓ trasladar estrictamente por -a
0 < b + (-a)
↓ multiplicar por c > 0 y excluir el producto nulo
0 < (b + (-a))c      y      0 < c(b + (-a))
↓ distribuir, reescribir signos y trasladar
ac < bc              y      ca < cb
```

El diagrama reúne dos rutas que se **justifican por separado**: la multiplicación por la derecha no puede sustituirse por la izquierda en un anillo no conmutativo.

### Proposición 26.20.1 — Monotonía multiplicativa estricta por factores positivos sin productos nulos {#talg-pro-00073}

Sea $\langle R,+,\cdot,\le\rangle$ un anillo ordenado y sean $a,b,c\in R$ tales que

$$
a<b,\qquad 0<c.
$$

Escribamos $d:=b+(-a)$. Se cumplen las dos afirmaciones siguientes:

1. Si $d\cdot c\ne0$, entonces $a\cdot c<b\cdot c$.
2. Si $c\cdot d\ne0$, entonces $c\cdot a<c\cdot b$.

**En particular**, si el anillo satisface la condición global

$$
\forall x,y\in R,\qquad
(x\ne0\ \land\ y\ne0)\Longrightarrow x\cdot y\ne0,
$$

entonces ambas conclusiones valen simultáneamente para todos $a<b$ y $0<c$:

$$
a\cdot c<b\cdot c,
\qquad
c\cdot a<c\cdot b.
$$

#### Demostración {#talg-prf-00115}

Por hipótesis, $a<b$. La traslación estricta del grupo aditivo ordenado, establecida en la Proposición 25.5.1, permite sumar $-a$ a ambos miembros:

$$
a+(-a)<b+(-a).
$$

Como $a+(-a)=0$, resulta

$$
0<d,
\qquad d:=b+(-a).
$$

También suponemos $0<c$. Por tanto, $d$ y $c$ son estrictamente positivos.

**Primera afirmación: multiplicación por la derecha.** Si además $d\cdot c\ne0$, aplicamos la primera parte de la Proposición 26.18.1 a $d$ y $c$:

$$
0<d\cdot c.
$$

La distributividad por la derecha y las reglas de signos de la Proposición 14.4.1 dan

$$
d\cdot c
=(b+(-a))\cdot c
=b\cdot c+(-a)\cdot c
=b\cdot c+(-(a\cdot c)).
$$

Sustituimos en la desigualdad y trasladamos estrictamente por $a\cdot c$:

$$
a\cdot c
<a\cdot c+\bigl(b\cdot c+(-(a\cdot c))\bigr)
=b\cdot c.
$$

La última igualdad utiliza únicamente las leyes del grupo aditivo abeliano. Queda probado $a\cdot c<b\cdot c$.

**Segunda afirmación: multiplicación por la izquierda.** Si además $c\cdot d\ne0$, la misma Proposición 26.18.1, ahora aplicada a los factores $c$ y $d$ en ese orden, proporciona

$$
0<c\cdot d.
$$

Usando la distributividad por la izquierda y las reglas de signos,

$$
c\cdot d
=c\cdot(b+(-a))
=c\cdot b+c\cdot(-a)
=c\cdot b+(-(c\cdot a)).
$$

Trasladando estrictamente por $c\cdot a$ y simplificando en el grupo aditivo,

$$
c\cdot a<c\cdot b.
$$

Finalmente, supongamos la condición global del enunciado. De $0<d$ y $0<c$ se deduce $d\ne0$ y $c\ne0$ por definición del orden estricto. La condición global aplicada tanto a $(d,c)$ como a $(c,d)$ da

$$
d\cdot c\ne0,
\qquad
c\cdot d\ne0.
$$

Las dos afirmaciones anteriores producen simultáneamente las conclusiones deseadas. $\square$

> **Dónde trabaja cada condición.** La hipótesis $a<b$ proporciona una diferencia positiva; $0<c$ proporciona el segundo factor positivo. La no nulidad de $dc$ sirve sólo para la desigualdad derecha, mientras que la de $cd$ sirve sólo para la izquierda. La condición global las garantiza por separado, sin introducir $dc=cd$.

> **Prueba de estrés: un factor positivo no basta.** En el anillo totalmente ordenado de números duales enteros del contraste posterior a la Proposición 26.18.1, tomemos $a=0$, $b=\varepsilon$ y $c=\varepsilon$. Entonces $a<b$ y $0<c$, pero $ac=bc=0$ y $ca=cb=0$, pues $\varepsilon^2=0$. El orden total no rescata ninguna de las dos desigualdades estrictas. Se trata de un ejemplo ilustrativo, no de una premisa de la prueba.

> **Lo que no se ha demostrado.** La proposición no afirma monotonía estricta al multiplicar por un elemento arbitrario ni convierte la ausencia de divisores de cero en un axioma para todos los anillos ordenados. Tampoco requiere que el orden sea total o que pueda decidirse computacionalmente.

---

## 26.22. De la monotonía estricta a la inversión estricta

En la Proposición 26.20.1 comprobamos que un factor positivo preserva las comparaciones estrictas si el producto de ese factor por la diferencia no se anula. Para un factor **negativo** no es preciso introducir otra ley de compatibilidad: el opuesto del factor es positivo, y tomar opuestos invierte el orden.

La prueba se organiza en cuatro movimientos:

```text
a < b, c < 0
↓ inversión estricta del signo de c
0 < -c
↓ productos de la diferencia con -c no nulos
multiplicación estrictamente monótona por -c, en ambos lados
↓ reglas de signos e inversión estricta
bc < ac                  cb < ca
```

La no nulidad de cada producto de la diferencia sigue siendo una hipótesis **lateral**; no se deduce del mero hecho de que $c$ sea negativo.

### Proposición 26.22.1 — Antitonicidad multiplicativa estricta por factores negativos sin productos nulos {#talg-pro-00074}

Sea $\langle R,+,\cdot,\le\rangle$ un anillo ordenado y sean $a,b,c\in R$ con

$$
a<b,\qquad c<0.
$$

Escribamos $d:=b+(-a)$. Valen separadamente:

1. Si $d\cdot c\ne0$, entonces $b\cdot c<a\cdot c$.
2. Si $c\cdot d\ne0$, entonces $c\cdot b<c\cdot a$.

**En particular**, si el anillo cumple la condición global

$$
\forall x,y\in R,\qquad
(x\ne0\ \land\ y\ne0)\Longrightarrow x\cdot y\ne0,
$$

entonces para todos $a<b$ y $c<0$ se obtienen **ambas** desigualdades estrictas:

$$
b\cdot c<a\cdot c,\qquad c\cdot b<c\cdot a.
$$

#### Demostración {#talg-prf-00116}

La traslación estricta de la Proposición 25.5.1, aplicada a $a<b$, da

$$
0<b+(-a)=d.
$$

Como $c<0$, la inversión del orden estricto de la misma proposición implica

$$
0=-0<-c.
$$

Pongamos $h:=-c$. Tenemos $0<h$. Además, las reglas de signos de la Proposición 14.4.1 proporcionan

$$
dh=d(-c)=-(dc),\qquad hd=(-c)d=-(cd).
$$

En el grupo aditivo, tomar opuestos es involutivo y $-0=0$; por ello $dc\ne0$ implica $dh\ne0$, y $cd\ne0$ implica $hd\ne0$. En efecto, $dh=0$ implicaría $dc=-0=0$; el segundo caso es análogo.

**Primera afirmación: multiplicación por la derecha.** Supongamos $dc\ne0$. La consecuencia recién demostrada asegura $dh\ne0$. Aplicando la Proposición 26.20.1 a $a<b$ y al factor $h>0$, por su lateralidad derecha obtenemos

$$
a\cdot h<b\cdot h.
$$

Sustituimos $h=-c$ y usamos las reglas de signos:

$$
-(a\cdot c)<-(b\cdot c).
$$

La inversión estricta del orden (Proposición 25.5.1) transforma esta desigualdad en

$$
b\cdot c<a\cdot c.
$$

**Segunda afirmación: multiplicación por la izquierda.** Supongamos ahora $cd\ne0$. Entonces $hd\ne0$ y podemos aplicar la lateralidad izquierda de la Proposición 26.20.1:

$$
h\cdot a<h\cdot b.
$$

De nuevo, las reglas de signos dan

$$
-(c\cdot a)<-(c\cdot b).
$$

Invertimos estrictamente el orden y concluimos

$$
c\cdot b<c\cdot a.
$$

Por último, bajo la condición global, las desigualdades $0<d$ y $c<0$ implican $d\ne0$ y $c\ne0$. Aplicando la condición global a los pares ordenados $(d,c)$ y $(c,d)$ obtenemos respectivamente $dc\ne0$ y $cd\ne0$. Las dos partes anteriores demuestran las conclusiones simultáneas. $\square$

> **Lectura de las hipótesis.** La negatividad de $c$ convierte $-c$ en un factor positivo; la condición $dc\ne0$ permite preservar estrictamente el orden a la derecha antes de invertirlo, mientras que $cd\ne0$ hace lo mismo a la izquierda. En ningún punto se identifica $dc$ con $cd$.

> **Prueba de estrés: la negatividad sola es insuficiente.** En el anillo totalmente ordenado de números duales enteros descrito después de la Proposición 26.18.1, elijamos $a=0$, $b=\varepsilon$ y $c=-\varepsilon$. Se cumple $a<b$ y $c<0$, pero $bc=ac=cb=ca=0$, pues $\varepsilon^2=0$. La totalidad del orden no impide que la diferencia se anule al multiplicarla por un factor negativo. Este ejemplo ilustra la necesidad de la hipótesis; no interviene como premisa de la demostración.

> **Conexión con el siguiente paso.** La antitonicidad no estricta ya controla productos de factores de signos opuestos. La versión estricta recién demostrada permitirá distinguir con precisión *producto no positivo* de *producto estrictamente negativo*.

---

## 26.24. Signos opuestos: del orden no estricto al estricto

Las dos reglas de antitonicidad anteriores permiten sintetizar una ley de signos sin convertirla en un axioma: el producto de un factor no negativo por uno no positivo no puede ser positivo. Para afirmar que es *estrictamente negativo* hace falta excluir el caso en que el producto se anula. Como no hemos exigido conmutatividad, esa exclusión deberá comprobarse para cada orden de los factores.

El recorrido deductivo es el siguiente:

```text
0 ≤ a, b ≤ 0               0 < a, b < 0
      ↓ 26.8.1                  ↓ 26.22.1 + producto no nulo
ab ≤ 0, ba ≤ 0             ab < 0, ba < 0
```

### Corolario 26.24.1 — Producto de factores de signo opuesto: no positividad y negatividad estricta bajo no nulidad {#talg-cor-00018}

Sea $\langle R,+,\cdot,\le\rangle$ un anillo ordenado, no necesariamente conmutativo ni totalmente ordenado, y sean $a,b\in R$.

**I. Signos opuestos no estrictos.** Si

$$
0\le a,\qquad b\le0,
$$

entonces

$$
ab\le0\qquad\text{y}\qquad ba\le0.
$$

También se obtienen ambas conclusiones si $a\le0$ y $0\le b$.

**II. Signos opuestos estrictos.** Si

$$
0<a,\qquad b<0,
$$

se tienen dos implicaciones independientes:

$$
ab\ne0\Longrightarrow ab<0,
\qquad
ba\ne0\Longrightarrow ba<0.
$$

Las mismas implicaciones valen para $a<0$ y $0<b$, intercambiando los nombres de los factores. En particular, si se cumple la condición global

$$
\forall x,y\in R,\qquad
(x\ne0\land y\ne0)\Longrightarrow xy\ne0,
$$

cualquiera de los dos órdenes de multiplicación de factores de signos estrictamente opuestos produce un elemento estrictamente negativo.

#### Demostración {#talg-prf-00117}

**I. No positividad.** Supongamos $0\le a$ y $b\le0$. Aplicamos la antitonicidad no estricta de la Proposición 26.8.1 a la comparación $0\le a$, tomando $b$ como factor no positivo. La multiplicación por la derecha proporciona

$$
a\cdot b\le0\cdot b=0;
$$

y la multiplicación por la izquierda proporciona

$$
b\cdot a\le b\cdot0=0.
$$

Las igualdades finales son casos de la absorción bilateral del cero demostrada en la Proposición 14.3.1. Si $a\le0$ y $0\le b$, aplicamos lo ya probado al par $(b,a)$: así obtenemos $ba\le0$ y $ab\le0$, sin intercambiar ilícitamente los factores dentro de un producto.

**II. Negatividad estricta.** Supongamos $0<a$ y $b<0$. Aplicamos la antitonicidad estricta de la Proposición 26.22.1 a la comparación $0<a$ y al factor negativo $b$. La diferencia del término mayor con el menor es $a+(-0)=a$.

Si $ab\ne0$, se cumple la hipótesis local de la multiplicación por la derecha y obtenemos

$$
a\cdot b<0\cdot b=0.
$$

Si, independientemente, $ba\ne0$, la hipótesis local de la multiplicación por la izquierda produce

$$
b\cdot a<b\cdot0=0.
$$

En ambas cadenas usamos sólo la absorción del cero. Si $a<0$ y $0<b$, intercambiamos los nombres $a$ y $b$ al aplicar los dos resultados recién demostrados; se obtienen por separado los productos $ba$ y $ab$ estrictamente negativos bajo sus respectivas hipótesis de no nulidad.

Finalmente, bajo la condición global, los signos estrictos implican $a\ne0$ y $b\ne0$. La condición global aplicada a los pares ordenados $(a,b)$ y $(b,a)$ da respectivamente $ab\ne0$ y $ba\ne0$. Las dos implicaciones locales concluyen la demostración. $\square$

> **Lectura guiada.** La propiedad $ab\le0$ no implica por sí sola $ab<0$: el orden estricto asociado exige además $ab\ne0$. En un anillo sin conmutatividad no se deduce $ba\ne0$ únicamente de $ab\ne0$; la prueba registra ambas hipótesis y las utiliza por separado.

> **Casos frontera.** Si $a=0$ o $b=0$, los dos productos son cero, incluso en un anillo sin divisores de cero. Por eso la primera parte admite signos no estrictos, mientras que la segunda exige factores de signos estrictos.

> **Contraejemplo a la supresión de la no nulidad.** En el anillo de números duales enteros con orden lexicográfico descrito después de la Proposición 26.18.1, $a=\varepsilon>0$ y $b=-\varepsilon<0$ satisfacen $ab=ba=-\varepsilon^2=0$. Ni siquiera la totalidad del orden permite deducir la negatividad estricta sin la hipótesis multiplicativa correspondiente. Este ejemplo es ilustrativo, no una dependencia de la prueba.

> **Conexión.** Combinando la no negatividad de cuadrados ya demostrada para anillos totalmente ordenados con una condición de no nulidad de $a^2$ será posible obtener positividad estricta de cuadrados no nulos, sin añadir tal conclusión a la definición de anillo ordenado.

---

## 26.26. Cuándo un cuadrado es estrictamente positivo

La Proposición 26.14.1 garantiza que todo cuadrado de un anillo totalmente ordenado es **no negativo**. No garantiza que sea estrictamente positivo cuando el elemento original es distinto de cero: un factor no nulo puede tener cuadrado nulo. El fortalecimiento correcto consiste en añadir la no nulidad del **cuadrado**, no sólo la del factor.

La distinción puede representarse sin confundir los dos enunciados:

```text
anillo totalmente ordenado ── Proposición 26.14.1 ──→ 0 ≤ a²
                                                      │
                                  hipótesis a² ≠ 0 ────┤
                                                      ↓
                                                    0 < a²

hipótesis global: x ≠ 0, y ≠ 0 ⇒ xy ≠ 0
                     + a ≠ 0
                         ↓ aplicar a (a,a)
                       a² ≠ 0
```

La primera ruta exige una condición **local** sobre $a^2$; la segunda exhibe una condición **global suficiente** para obtenerla a partir de $a\ne0$.

### Proposición 26.26.1 — Positividad estricta de cuadrados no nulos en anillos totalmente ordenados {#talg-pro-00075}

Sea $\langle R,+,\cdot,\le\rangle$ un anillo totalmente ordenado. Para todo $a\in R$, escribamos $a^2:=a\cdot a$. Entonces:

1. **Criterio local exacto:**

   $$
   0<a^2\quad\Longleftrightarrow\quad a^2\ne0.
   $$

2. **Relación entre las dos no nulidades:** $a^2\ne0$ implica $a\ne0$. No se afirma aquí la recíproca.

3. **Condición global suficiente:** si el anillo satisface

   $$
   \forall x,y\in R,\qquad
   (x\ne0\ \land\ y\ne0)\Longrightarrow x\cdot y\ne0,
   $$

   entonces, para todo $a\in R$,

   $$
   a\ne0\Longrightarrow 0<a^2.
   $$

#### Demostración {#talg-prf-00118}

Fijemos $a\in R$. Puesto que el anillo es totalmente ordenado, la Proposición 26.14.1 proporciona

$$
0\le a^2.
$$

**1. Criterio local.** Supongamos primero $a^2\ne0$. La definición del orden estricto asociado, fijada en la Interfaz 25.1.1, es

$$
x<y\quad\Longleftrightarrow\quad x\le y\ \land\ x\ne y.
$$

Aplicada a $x=0$ e $y=a^2$, combina exactamente las dos condiciones disponibles y da $0<a^2$. A la inversa, si $0<a^2$, la misma definición contiene como una de sus cláusulas $0\ne a^2$, equivalente a $a^2\ne0$. Concluimos

$$
0<a^2\quad\Longleftrightarrow\quad a^2\ne0.
$$

**2. No nulidad del factor.** Supongamos $a^2\ne0$. Para demostrar $a\ne0$, supongamos provisionalmente $a=0$. La sustitución en $a^2=a\cdot a$ y la absorción del cero de la Proposición 14.3.1 darían

$$
a^2=0\cdot0=0,
$$

contradicción con la hipótesis. Así, $a\ne0$.

**3. Garantía global.** Supongamos ahora la condición global del enunciado y fijemos $a\in R$ tal que $a\ne0$. Podemos aplicarla al par concreto $(x,y)=(a,a)$: sus dos antecedentes son precisamente la misma hipótesis $a\ne0$. Obtenemos

$$
a\cdot a=a^2\ne0.
$$

La primera parte transforma inmediatamente esta no nulidad en $0<a^2$. Como $a$ era arbitrario, queda probada la última implicación. $\square$

> **Lectura de la prueba.** La totalidad interviene únicamente al disponer de la no negatividad de todos los cuadrados mediante la Proposición 26.14.1; no se utiliza para decidir algorítmicamente el signo de $a$. La no nulidad local convierte $0\le a^2$ en $0<a^2$. La hipótesis global interviene sólo para deducir $a^2\ne0$ a partir de $a\ne0$.

> **Contraejemplo a sustituir $a^2\ne0$ por $a\ne0$.** En el anillo totalmente ordenado de números duales enteros ya descrito después de la Proposición 26.18.1, $\varepsilon\ne0$ e incluso $0<\varepsilon$, pero $\varepsilon^2=0$. Por consiguiente, ni la totalidad ni el signo estricto del factor justifican $0<a^2$ para todo $a\ne0$ sin una condición adicional. El ejemplo no es una dependencia deductiva.

> **Alcance.** No se ha supuesto multiplicación conmutativa ni no trivialidad como axioma independiente. La condición global es suficiente, no parte de la definición de anillo totalmente ordenado. Tampoco se afirman decidibilidad, algoritmos de comparación o resultados analíticos.

---

## 26.28. De dos factores negativos a un producto estrictamente positivo

Ya sabemos, por el Corolario 26.10.1, que multiplicar dos elementos **no positivos** produce un elemento no negativo. La pregunta pendiente es cuándo podemos fortalecer esa conclusión. La respuesta exige distinguir el signo de los factores de la eventual anulación de su producto.

```text
a < 0, b < 0
       │
       ├── ambos factores son no positivos
       │                ↓ Corolario 26.10.1
       │          0 ≤ ab  y  0 ≤ ba
       │
       ├── añadir ab ≠ 0 ────────────────→ 0 < ab
       └── añadir ba ≠ 0 ────────────────→ 0 < ba
```

El diagrama mantiene separados $ab$ y $ba$: en un anillo no conmutativo, la no nulidad de uno de estos productos no se sustituye por la del otro. Tampoco hace falta que todos los elementos sean comparables; aquí las comparaciones con cero forman parte de las hipótesis.

### Corolario 26.28.1 — Positividad estricta de productos de factores negativos bajo no nulidad {#talg-cor-00019}

Sea $\langle R,+,\cdot,\le\rangle$ un anillo ordenado y sean $a,b\in R$ tales que $a<0$ y $b<0$. Entonces se verifican las afirmaciones siguientes:

1. **No negatividad bilateral:**

   $$
   0\le ab,\qquad 0\le ba.
   $$

2. **Criterios locales exactos, independientes entre sí:**

   $$
   0<ab\quad\Longleftrightarrow\quad ab\ne0,
   $$

   $$
   0<ba\quad\Longleftrightarrow\quad ba\ne0.
   $$

3. **Condición global suficiente:** si se verifica

   $$
   \forall x,y\in R,\qquad
   (x\ne0\ \land\ y\ne0)\Longrightarrow xy\ne0,
   $$

   entonces $0<ab$ y $0<ba$.

#### Demostración {#talg-prf-00119}

**1. De signos estrictamente negativos a productos no negativos.** Por la definición del orden estricto asociado, $a<0$ implica $a\le0$, y $b<0$ implica $b\le0$. El Corolario 26.10.1 aplicado a estos dos elementos proporciona

$$
0\le ab.
$$

El mismo corolario, ahora aplicado a los factores en el orden $(b,a)$, proporciona independientemente

$$
0\le ba.
$$

No se ha reemplazado un producto por el otro mediante conmutatividad.

**2. Conversión local al orden estricto.** La definición del orden estricto asociado, recordada en la Interfaz 25.1.1, establece para todo $z\in R$:

$$
0<z\quad\Longleftrightarrow\quad (0\le z\ \land\ z\ne0).
$$

Para $z=ab$ ya conocemos $0\le ab$. Por consiguiente, añadir $ab\ne0$ es suficiente para obtener $0<ab$; recíprocamente, $0<ab$ contiene necesariamente la condición $ab\ne0$. Se obtiene así la primera equivalencia.

Repetimos el argumento con $z=ba$ y con la no negatividad demostrada por separado. La hipótesis y conclusión correspondientes son $ba\ne0$ y $0<ba$. Queda establecida la segunda equivalencia, sin suponer que $ab=ba$ ni que la no nulidad de uno garantice la del otro.

**3. Exclusión global de productos nulos.** Si vale la condición global, las hipótesis $a<0$ y $b<0$ proporcionan también $a\ne0$ y $b\ne0$ por la definición de orden estricto. Aplicando la condición global al par ordenado $(a,b)$, deducimos $ab\ne0$. Aplicándola *otra vez* al par $(b,a)$, deducimos $ba\ne0$. Las dos equivalencias locales del paso anterior concluyen

$$
0<ab,\qquad 0<ba.
$$

Esto completa la demostración. $\square$

> **Lectura guiada.** «Negativo por negativo es positivo» se descompone en dos pasos matemáticos: primero se prueba que el producto es no negativo; después se excluye que sea cero. La no nulidad de los factores no reemplaza por sí sola la segunda comprobación en un anillo con divisores de cero.

> **Contraejemplo a eliminar la hipótesis local.** En el anillo totalmente ordenado de números duales enteros descrito después de la Proposición 26.18.1, tomemos $a=b=-\varepsilon$. Se cumple $a<0$ y $b<0$, pero $ab=ba=\varepsilon^2=0$. La totalidad no sustituye la no nulidad del producto. El ejemplo es un control pedagógico, no una premisa de la demostración.

> **Alcance estructural.** El enunciado vale para órdenes parciales y multiplicación posiblemente no conmutativa; no exige decidir la igualdad ni el signo, y no introduce elección ni nociones analíticas.

---

## 26.30. Preservar una comparación no equivale a reflejarla

La Proposición 26.20.1 proporciona una implicación directa: si $a<b$ y $c>0$, la desigualdad $ac<bc$ se obtiene **cuando el producto de la diferencia por $c$ no se anula**. La cuestión recíproca es diferente. Si ya sabemos que $ac<bc$, ¿podemos recuperar $a<b$? En un orden total, la respuesta es afirmativa, aun cuando el anillo tenga divisores de cero: la monotonía no estricta descarta la comparación opuesta.

```text
                 anillo totalmente ordenado, c > 0

  ac < bc ── totalidad + monotonía no estricta ──→ a < b
  ca < cb ── totalidad + monotonía no estricta ──→ a < b

  a < b ── (b-a)c ≠ 0 ──→ ac < bc
  a < b ── c(b-a) ≠ 0 ──→ ca < cb
```

El dibujo separa dos operaciones lógicas: *reflejar* una desigualdad ya observada y *preservar estrictamente* una desigualdad inicial. Las condiciones de no nulidad sólo aparecen en las flechas que van desde $a<b$ hacia los productos.

### Proposición 26.30.1 — Reflexión del orden estricto por factores positivos en anillos totalmente ordenados {#talg-pro-00076}

Sea $\langle R,+,\cdot,\le\rangle$ un **anillo totalmente ordenado** y sean $a,b,c\in R$ con $0<c$. Entonces:

1. **Reflexión estricta por la derecha:** $ac<bc\Longrightarrow a<b$.
2. **Reflexión estricta por la izquierda:** $ca<cb\Longrightarrow a<b$.
3. **Criterios locales exactos:** si además $a<b$ y $d:=b+(-a)$, entonces

   $$
   ac<bc\quad\Longleftrightarrow\quad dc\ne0,
   $$

   $$
   ca<cb\quad\Longleftrightarrow\quad cd\ne0.
   $$

4. **Equivalencias bajo una condición global suficiente:** si

   $$
   \forall x,y\in R,\qquad (x\ne0\ \land\ y\ne0)\Longrightarrow xy\ne0,
   $$

   entonces, para todo $a,b\in R$ y todo $c>0$,

   $$
   a<b\quad\Longleftrightarrow\quad ac<bc,
   $$

   $$
   a<b\quad\Longleftrightarrow\quad ca<cb.
   $$

En las dos primeras afirmaciones puede debilitarse $0<c$ a $0\le c$. Esta mejora no se extiende automáticamente a las implicaciones directas del cuarto apartado.

#### Demostración {#talg-prf-00120}

**1. Reflexión por la derecha.** Supongamos $ac<bc$. Como $0<c$, también $0\le c$. Por totalidad, aplicada a $a$ y $b$, disponemos de la disyunción

$$
a\le b\quad\lor\quad b\le a.
$$

En la segunda alternativa, la monotonía no estricta por la derecha de la Proposición 26.6.1 daría $bc\le ac$. Pero $ac<bc$ significa $ac\le bc$ y $ac\ne bc$. La antisimetría aplicada a $ac\le bc$ y $bc\le ac$ impondría $ac=bc$, contradicción. Por tanto, la segunda alternativa es imposible y subsiste $a\le b$.

Si $a=b$, la sustitución en el producto por la derecha produciría $ac=bc$, otra contradicción. Así, $a\ne b$. Por definición de orden estricto asociado,

$$
a\le b\ \land\ a\ne b\quad\Longrightarrow\quad a<b.
$$

La prueba no ha empleado una ley de cancelación multiplicativa ni ha supuesto que $c$ sea regular.

**2. Reflexión por la izquierda.** Ahora supongamos $ca<cb$. La misma totalidad ofrece $a\le b$ o $b\le a$. En la segunda alternativa, la lateralidad **izquierda** de la Proposición 26.6.1 da $cb\le ca$, que contradice $ca<cb$ por antisimetría. Luego $a\le b$. Si $a=b$, se seguiría $ca=cb$, incompatible con la desigualdad estricta inicial. Por consiguiente, $a<b$. No se ha intercambiado $ac$ con $ca$.

Ambos argumentos sólo emplearon $0\le c$. Si $c=0$, la absorción del cero de la Proposición 14.3.1 hace que los productos comparados sean iguales y, por tanto, el antecedente estricto simplemente no se cumple. Esto demuestra también la versión debilitada anunciada.

**3. Caracterización de la conservación estricta.** Supongamos ahora $a<b$ y definamos $d:=b+(-a)$. La traslación estricta de la Proposición 25.5.1 proporciona $0<d$, luego $d\ne0$. La distributividad y las reglas de signos de la Proposición 14.4.1 dan dos identidades, cada una en su lateralidad:

$$
dc=(b+(-a))c=bc+(-(ac)),
$$

$$
cd=c(b+(-a))=cb+(-(ca)).
$$

En un grupo aditivo, $bc+(-(ac))=0$ equivale a $bc=ac$. Por consiguiente,

$$
dc\ne0\quad\Longleftrightarrow\quad ac\ne bc.
$$

Análogamente, sin permutar factores,

$$
cd\ne0\quad\Longleftrightarrow\quad ca\ne cb.
$$

Por la Proposición 26.6.1, $a<b$ y $0<c$ proporcionan $ac\le bc$ y $ca\le cb$. Al añadir respectivamente las dos desigualdades entre productos, la definición de $<$ transforma estas comparaciones no estrictas en las equivalencias locales enunciadas. De modo equivalente, la suficiencia de cada no nulidad está demostrada ya en la Proposición 26.20.1.

**4. Condición global.** Si ningún producto de dos factores no nulos se anula, $0<d$ y $0<c$ aseguran $dc\ne0$ aplicando la condición al par $(d,c)$ y $cd\ne0$ aplicándola al par $(c,d)$. Las equivalencias locales del paso 3 dan las dos implicaciones directas. Las implicaciones inversas fueron demostradas en los pasos 1 y 2, sin necesidad de esa condición global. Obtenemos ambas equivalencias para todos $a,b$ y todo $c>0$. $\square$

> **Construcción del modelo por coordenadas.** Sobre $R=\mathbb Z\times\mathbb Z$ usamos ahora $(m,n)(p,q)=(mp,nq)$, con suma por coordenadas, cero $(0,0)$, unidad $(1,1)$ y opuesto $(-m,-n)$. Cada ley de anillo se verifica en cada coordenada mediante la correspondiente ley entera importada en la [Interfaz 24.0.1](tratado-de-algebra-capitulo-24-cuerpo-de-fracciones-de-un-dominio-integro.md#talg-imp-00005). Definimos $(m,n)\le(p,q)$ si $m\le p$ y $n\le q$. Reflexividad, antisimetría, transitividad y compatibilidad aditiva se verifican por coordenadas. El producto de dos pares no negativos tiene ambas coordenadas no negativas por la compatibilidad del orden entero con el producto. Se obtiene así un anillo ordenado, cuyo orden no es total: $(0,1)$ y $(1,0)$ son incomparables. Este producto y este orden son distintos de los usados en el modelo de números duales de §26.18.

> **Prueba de estrés de la totalidad.** En $R=\mathbb Z\times\mathbb Z$ con suma y producto por coordenadas y orden parcial por coordenadas, consideremos $a=(0,1)$, $b=(1,0)$ y $c=(1,0)>0$. Se tiene $ac=(0,0)<(1,0)=bc$; sin embargo, $a$ y $b$ son incomparables. El cono no negativo es cerrado bajo la multiplicación, de modo que este sí es un anillo ordenado. La totalidad no se puede suprimir sin reemplazarla por alguna propiedad específica de reflexión del factor. El ejemplo es ilustrativo y no interviene en la prueba.

> **Prueba de estrés de la no nulidad.** En el anillo totalmente ordenado de números duales enteros del §26.18, fijemos $a=0$, $b=\varepsilon$ y $c=\varepsilon>0$. Se cumple $a<b$, pero $ac=bc=ca=cb=0$, porque $\varepsilon^2=0$. La reflexión sigue siendo válida; lo que falla sin hipótesis locales es la conservación estricta.

> **Lectura guiada.** Si una comparación estricta *sobrevive* a la multiplicación por un factor positivo, la totalidad permite recuperar la comparación original. No significa que toda comparación estricta deba sobrevivir: esa afirmación exige excluir la anulación de un producto determinado. La diferencia entre ambas direcciones impide confundir monotonía estricta, cancelación e inmersión de orden.

---

## 26.32. Multiplicar por un negativo: recuperar y transmitir el orden

La Proposición 26.22.1 establece que, si $a<b$ y $c<0$, podemos concluir $bc<ac$ cuando se ha comprobado que $(b-a)c$ no es cero. La pregunta inversa parte de una información diferente: **si ya observamos $bc<ac$, ¿qué sabemos acerca de $a$ y $b$?** En un anillo totalmente ordenado recuperaremos $a<b$ sin recurrir a cancelación multiplicativa ni exigir ausencia de divisores de cero.

```text
                anillo totalmente ordenado; c < 0

    bc < ac ── totalidad + antitonicidad no estricta ──→ a < b
    cb < ca ── totalidad + antitonicidad no estricta ──→ a < b

    a < b ── (b-a)c ≠ 0 ──────────────────────────────→ bc < ac
    a < b ── c(b-a) ≠ 0 ──────────────────────────────→ cb < ca
```

**Problema de lectura.** La inversión del signo del orden aparece en ambos sentidos de la comparación, pero la exigencia de no nulidad aparece solamente cuando queremos *producir* una desigualdad estricta entre productos a partir de $a<b$. El producto puede anular la diferencia incluso si el multiplicador es estrictamente negativo.

### Proposición 26.32.1 — Reflexión de la antitonicidad estricta por factores negativos en anillos totalmente ordenados {#talg-pro-00077}

Sea $\langle R,+,\cdot,\le\rangle$ un **anillo totalmente ordenado** y sean $a,b,c\in R$, con $c<0$. Se cumplen las siguientes afirmaciones:

1. **Reflexión estricta por la derecha:** $bc<ac\Longrightarrow a<b$.
2. **Reflexión estricta por la izquierda:** $cb<ca\Longrightarrow a<b$.
3. **Criterios locales exactos:** si además $a<b$ y $d:=b+(-a)$, entonces

   $$
   bc<ac\quad\Longleftrightarrow\quad dc\ne0,
   $$

   $$
   cb<ca\quad\Longleftrightarrow\quad cd\ne0.
   $$

4. **Equivalencias bajo una condición global suficiente:** si

   $$
   \forall x,y\in R,\qquad(x\ne0\ \land\ y\ne0)\Longrightarrow xy\ne0,
   $$

   entonces, para cualesquiera $a,b\in R$ y todo $c<0$,

   $$
   a<b\quad\Longleftrightarrow\quad bc<ac,
   $$

   $$
   a<b\quad\Longleftrightarrow\quad cb<ca.
   $$

Las dos primeras implicaciones son válidas incluso bajo la hipótesis debilitada $c\le0$. Las equivalencias del cuarto apartado exigen $c<0$; el factor cero no conserva ninguna desigualdad estricta.

#### Demostración {#talg-prf-00121}

**1. Reflexión por la derecha.** Supongamos $bc<ac$. Como $c<0$, tenemos $c\le0$. La totalidad del orden, aplicada a $a,b$, proporciona

$$
a\le b\quad\lor\quad b\le a.
$$

Si $b\le a$, la antitonicidad no estricta **por la derecha** de la Proposición 26.8.1, aplicada a esta comparación y al factor $c\le0$, implica

$$
ac\le bc.
$$

Sin embargo, $bc<ac$ significa $bc\le ac$ y $bc\ne ac$. Por antisimetría, las desigualdades $bc\le ac$ y $ac\le bc$ obligarían a $bc=ac$, contradicción. En consecuencia, la segunda alternativa de la totalidad es imposible y queda $a\le b$. Además, $a=b$ produciría $bc=ac$ por sustitución, también imposible. Tenemos $a\le b$ y $a\ne b$, es decir, $a<b$ por definición del orden estricto asociado.

Esta reflexión no divide por $c$ y no aplica cancelación multiplicativa: sólo excluye una comparación incompatible con la desigualdad estricta observada.

**2. Reflexión por la izquierda.** Supongamos $cb<ca$. De nuevo, la totalidad da $a\le b$ o $b\le a$. Si $b\le a$, la parte **izquierda** de la Proposición 26.8.1 da $ca\le cb$. Junto con $cb<ca$, la antisimetría conduciría a $cb=ca$, una contradicción. Por tanto, $a\le b$. La igualdad $a=b$ también es imposible porque implicaría $cb=ca$. Concluimos $a<b$. Nunca se identificaron los productos $bc$ y $cb$.

En ambas reflexiones bastó $c\le0$. Para $c=0$, la absorción del cero de la Proposición 14.3.1 da $bc=ac=cb=ca=0$; ningún antecedente estricto puede cumplirse. La afirmación debilitada permanece válida, aunque vacuamente en ese caso.

**3. Criterios locales de conservación estricta.** Añadamos $a<b$ y definamos $d:=b+(-a)$. La compatibilidad del orden estricto con traslaciones, recogida en la Proposición 25.5.1, proporciona $0<d$ y, por tanto, $d\ne0$. Por distributividad y por las reglas de signos de la Proposición 14.4.1,

$$
dc=(b+(-a))c=bc+(-(ac)),
$$

$$
cd=c(b+(-a))=cb+(-(ca)).
$$

Las leyes del grupo aditivo establecen las equivalencias

$$
dc=0\quad\Longleftrightarrow\quad bc=ac,
$$

$$
cd=0\quad\Longleftrightarrow\quad cb=ca.
$$

Por la antitonicidad no estricta de la Proposición 26.8.1, de $a<b$ y $c<0$ se sigue $bc\le ac$ y $cb\le ca$. En cada caso, la desigualdad estricta equivale a que los dos productos comparados no sean iguales. Las identidades anteriores proporcionan exactamente

$$
bc<ac\quad\Longleftrightarrow\quad dc\ne0,
$$

$$
cb<ca\quad\Longleftrightarrow\quad cd\ne0.
$$

La suficiencia de ambas condiciones de no nulidad también está contenida en la Proposición 26.22.1. Aquí hemos establecido además su necesidad sin cancelar factores.

**4. Garantía global y equivalencias.** Supongamos que ningún producto de dos factores no nulos se anula. De $0<d$ y $c<0$ deducimos $d\ne0$ y $c\ne0$. Aplicamos la condición global al par ordenado $(d,c)$ para obtener $dc\ne0$, y de forma independiente al par $(c,d)$ para obtener $cd\ne0$. El apartado 3 demuestra que $a<b$ implica $bc<ac$ y $cb<ca$. Las dos implicaciones recíprocas se probaron en los apartados 1 y 2 sin la condición global. Quedan establecidas las equivalencias para todo $a,b$ y cada $c<0$. $\square$

> **Totalidad frente a orden parcial.** Consideremos $R=\mathbb Z\times\mathbb Z$, con operaciones y orden parcial por coordenadas, y $a=(0,1)$, $b=(1,0)$, $c=(-1,0)<0$. Se obtiene $bc=(-1,0)<(0,0)=ac$ y también $cb<ca$, pero $a$ y $b$ son incomparables. Es un anillo ordenado: el cono no negativo es cerrado bajo el producto coordenado. El ejemplo prueba que no puede suprimirse sin más la totalidad en las implicaciones de reflexión; no interviene en la demostración.

> **Signo negativo frente a productos nulos.** En el anillo totalmente ordenado de números duales enteros descrito en §26.18, tomemos $a=0$, $b=\varepsilon>0$ y $c=-\varepsilon<0$. Entonces $a<b$, pero $bc=ac=cb=ca=0$ porque $\varepsilon^2=0$. El signo negativo del factor no garantiza conservación estricta. El ejemplo es exclusivamente pedagógico.

> **Lectura guiada.** Una desigualdad estricta entre productos *ya observada* permite recuperar $a<b$ bajo totalidad. En cambio, para producir esa desigualdad a partir de $a<b$ necesitamos que no se anule el producto concreto de la diferencia por el factor. Las lateralidades y los sentidos de implicación son independientes.

---

## 26.34. Una desigualdad no estricta puede ocultar una igualdad de productos

Las Proposiciones 26.30.1 y 26.32.1 reflejan una comparación *estricta* observada después de multiplicar: la estrictitud impide que los productos sean iguales. Para una comparación no estricta, esa salida ya no está disponible. Aunque $c>0$, de $ac\le bc$ podrían resultar simplemente dos productos iguales, sin que esto determine la relación entre $a$ y $b$ si el factor anula diferencias no nulas.

La hipótesis global que excluye esos colapsos será

$$
\tag{NZ}
\forall x,y\in R,\qquad (x\ne0\ \land\ y\ne0)\Longrightarrow xy\ne0.
$$

La prueba conservará la multiplicación no conmutativa: necesitaremos dos argumentos de cancelación, uno para $(u-v)c$ y otro para $c(u-v)$.

```text
                      totalidad + (NZ); c ≠ 0

   c > 0     a ≤ b  ⇔  ac ≤ bc       a ≤ b  ⇔  ca ≤ cb
   c < 0     a ≤ b  ⇔  bc ≤ ac       a ≤ b  ⇔  cb ≤ ca

            conservación: ley de signo ya demostrada
            reflexión: totalidad + exclusión de colapsos
```

> **Pregunta de control.** ¿Por qué no bastaba repetir la reflexión estricta? Porque de $ac\le bc$ no obtenemos $ac<bc$ hasta descartar la posibilidad $ac=bc$. La condición (NZ) hace precisamente posible recuperar la igualdad original en ese caso.

### Proposición 26.34.1 — Reflexión del orden no estricto bajo ausencia de productos nulos en anillos totalmente ordenados {#talg-pro-00078}

Sea $\langle R,+,\cdot,\le\rangle$ un anillo totalmente ordenado que satisface (NZ), y sean $a,b,c\in R$.

1. Si $0<c$, se cumplen, **independientemente por cada lateralidad**,

   $$
   a\le b\quad\Longleftrightarrow\quad ac\le bc,
   $$

   $$
   a\le b\quad\Longleftrightarrow\quad ca\le cb.
   $$

2. Si $c<0$, se cumplen las equivalencias de **orden invertido**,

   $$
   a\le b\quad\Longleftrightarrow\quad bc\le ac,
   $$

   $$
   a\le b\quad\Longleftrightarrow\quad cb\le ca.
   $$

La condición global (NZ) puede sustituirse por la regularidad *lateral correspondiente* del factor $c$: $xc=0\Rightarrow x=0$ para las dos afirmaciones derechas, o $cx=0\Rightarrow x=0$ para las dos izquierdas, para todo $x\in R$. La regularidad se toma aquí como una hipótesis explícita y no como consecuencia del mero signo.

#### Demostración {#talg-prf-00122}

**1. Cancelación previa, separada por lateralidad.** Fijemos $c\ne0$. Primero, supongamos $uc=vc$. Por distributividad y las reglas de signos de la Proposición 14.4.1,

$$
(u+(-v))c=uc+(-(vc))=0.
$$

Si $u\ne v$, las leyes del grupo aditivo implican $u+(-v)\ne0$: de la igualdad $u+(-v)=0$ se recuperaría $u=v$ trasladando por $v$. Por (NZ), aplicado al par ordenado $(u+(-v),c)$, deberíamos tener $(u+(-v))c\ne0$, contradicción. Hemos demostrado $\neg(u\ne v)$, esto es, $\neg\neg(u=v)$. **En este único paso utilizamos la lógica clásica del fundamento ZF** para concluir $u=v$. Por tanto,

$$
uc=vc\quad\Longrightarrow\quad u=v.
$$

La cancelación izquierda se demuestra *de nuevo*, no permutando los factores. Si $cu=cv$, entonces

$$
c(u+(-v))=cu+(-(cv))=0.
$$

Si $u\ne v$, (NZ) aplicado a $(c,u+(-v))$ contradice esta igualdad. La misma eliminación clásica de doble negación da $u=v$, y queda

$$
cu=cv\quad\Longrightarrow\quad u=v.
$$

Alternativamente, si se adopta directamente la ley $xy=0\Rightarrow x=0\lor y=0$, o la regularidad lateral formulada en el enunciado, estos argumentos de cancelación no necesitan el paso de doble negación. Aquí hemos mantenido la hipótesis (NZ) ya fijada en el tratado y registrado fielmente la inferencia clásica.

**2. Factor positivo: conservación.** Supongamos $0<c$, de donde $0\le c$ y $c\ne0$. Si $a\le b$, la monotonía bilateral de la Proposición 26.6.1 produce, por separado, $ac\le bc$ y $ca\le cb$. No se necesita (NZ) para estas dos implicaciones.

**3. Factor positivo: reflexión por la derecha.** Supongamos $ac\le bc$. La totalidad suministra $a\le b$ o $b\le a$. En el primer caso ya tenemos lo buscado. En el segundo, la monotonía de la Proposición 26.6.1 da $bc\le ac$. Por antisimetría,

$$
ac=bc.
$$

Como $c\ne0$, la cancelación **derecha** demostrada en el paso 1 da $a=b$ y, por reflexividad, $a\le b$. Ambos casos de la disyunción concluyen lo mismo.

**4. Factor positivo: reflexión por la izquierda.** Si $ca\le cb$, la totalidad vuelve a dar $a\le b$ o $b\le a$. En la segunda rama la monotonía izquierda produce $cb\le ca$; por antisimetría $ca=cb$. La cancelación **izquierda** del paso 1 implica $a=b$, luego $a\le b$. Quedan probadas las dos equivalencias del apartado 1.

**5. Factor negativo: conservación.** Si $c<0$, tenemos $c\le0$ y $c\ne0$. Partiendo de $a\le b$, la Proposición 26.8.1, en sus dos lateralidades, da $bc\le ac$ y $cb\le ca$. Estas implicaciones tampoco precisan (NZ).

**6. Factor negativo: reflexión por la derecha.** Partamos de $bc\le ac$ y de la disyunción total $a\le b\lor b\le a$. La primera rama concluye. Si $b\le a$, la antitonicidad por la derecha da $ac\le bc$. La antisimetría impone $bc=ac$, y la cancelación derecha por $c\ne0$ impone $b=a$. Así $a\le b$ también en esta rama.

**7. Factor negativo: reflexión por la izquierda.** Partamos de $cb\le ca$. Si la totalidad da $a\le b$, ya está. En la otra rama, $b\le a$ implica $ca\le cb$ por antitonicidad izquierda; la antisimetría produce $cb=ca$. Cancelamos por la izquierda, obtenemos $b=a$ y concluimos $a\le b$.

Las cuatro equivalencias están demostradas sin conmutatividad de la multiplicación. La inspección de los pasos 3, 4, 6 y 7 muestra que sólo se emplea la cancelación lateral respectiva; por ello basta, en cada caso, la regularidad correspondiente de $c$ indicada en el enunciado. $\square$

> **Contraejemplo: el signo no garantiza reflexión no estricta.** En el anillo totalmente ordenado de números duales enteros del §26.18, $\varepsilon>0$, $\varepsilon^2=0$. Sean $a=\varepsilon$, $b=0$ y $c=\varepsilon>0$. Entonces $ac=bc=ca=cb=0$, de modo que las dos comparaciones de productos son verdaderas, aunque $a\le b$ es falsa. Si se toma $c=-\varepsilon<0$, ocurre la misma igualdad y fallan igualmente las reflexiones negativas. Esto demuestra la necesidad de controlar colapsos; no demuestra que la condición global (NZ) sea *necesaria* en todos los casos particulares.

> **Factor cero.** Cuando $c=0$, la Proposición 14.3.1 da $ac=bc=ca=cb=0$ para cualesquiera $a,b$. Por tanto, salvo circunstancias degeneradas, la comparación entre productos carece de información sobre $a$ y $b$. Las equivalencias del enunciado exigen signo *estricto* y nunca incluyen $c=0$.

> **Lectura inversa.** En las desigualdades estrictas, la información $ac<bc$ bastaba para reflejar el orden mediante totalidad. En las no estrictas hay que atender además a la rama de igualdad $ac=bc$: la exclusión de productos nulos garantiza cancelación, y sólo entonces permite volver a $a\le b$. El razonamiento es simétrico en su arquitectura, pero no identifica productos izquierdos y derechos.

---

## 26.36. Síntesis deductiva del capítulo

El problema planteado en §26.0 era hacer compatibles las dos operaciones de un anillo con una relación de orden, **sin atribuir a la multiplicación la invariancia que pertenece a las traslaciones aditivas**. La cadena de resultados cerrados permite ahora dar una respuesta sistemática:

```text
anillo + grupo aditivo ordenado + cierre multiplicativo de los no negativos
           │
           ├── anillo ordenado (§26.1)
           │   ├── factor c ≥ 0: conservación de ≤ (§26.6)
           │   ├── factor c ≤ 0: inversión de ≤ (§26.8)
           │   └── producto de dos no positivos ≥ 0 (§26.10)
           │
           └── orden total (§26.12)
               ├── cuadrados ≥ 0; unidad ≥ 0 (§§26.14–26.16)
               ├── producto no nulo: control de estrictitud (§§26.18–26.28)
               ├── reflexión estricta sin cancelar (§§26.30–26.32)
               └── reflexión no estricta: cancelación o regularidad (§26.34)
```

La **totalidad** aporta comparabilidad; no prohíbe que se anulen productos de factores no nulos. La **ausencia de productos nulos** es una condición distinta que permite controlar la igualdad de productos y garantizar algunas desigualdades estrictas. El **cuerpo** se introdujo previamente en el capítulo 22 como una estructura conmutativa, no trivial y con inversos para todos sus elementos no nulos. La siguiente unidad reunirá esa noción con el orden total aquí construido.

No se introdujeron completitud, topología, límites, supremos, axioma arquimediano ni algoritmos de comparación. Los contraejemplos con anillos coordenados y números duales delimitan las hipótesis; no sustituyen las pruebas.

---

[← **Capítulo 25 — Grupos ordenados**](tratado-de-algebra-capitulo-25-grupos-ordenados.md) · [**Tratado moderno de Álgebra**](../otros/tratado-de-algebra.md)
