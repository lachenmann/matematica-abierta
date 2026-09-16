---
title: 'Tratado moderno de Álgebra — Capítulo 25: Grupos ordenados'
description: Capítulo del Tratado moderno de Álgebra dedicado a grupos ordenados, publicado desde la fuente canónica cerrada del tratado.
author: Gustav A. Tachek
content-id: MA-BCH-0050
content-type: book-chapter
book-id: MA-BOK-0007
status: published
date-created: '2026-09-16'
date-modified: '2026-09-16'
areas:
- algebra
- fundamentos
level: avanzado
topics:
- algebra
- estructuras-algebraicas
prerequisites:
- MA-BCH-0049
related:
- MA-BOK-0007
- MA-BCH-0049
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 25 — Grupos ordenados

## 25.0. El problema: hacer compatible comparar con operar

Hasta ahora una estructura algebraica decía **qué operaciones pueden realizarse** y qué leyes satisfacen. Un orden añade otra clase de información: permite comparar elementos. El punto delicado no consiste en poner ambas estructuras una junto a otra, sino en exigir que sean compatibles.

Si $a\le b$, una operación de grupo no debería destruir arbitrariamente esa comparación. En un grupo general hay dos maneras de trasladar la desigualdad:

$$
a\le b
\quad\rightsquigarrow\quad
x\star a\le x\star b,
$$

y

$$
a\le b
\quad\rightsquigarrow\quad
a\star x\le b\star x.
$$

En un grupo no conmutativo estas dos exigencias no son formalmente la misma. Por eso comenzaremos con compatibilidad **bilateral**. Cuando el grupo sea abeliano veremos que una sola condición de traslación basta.

> **Profundidad pedagógica — P3.** Este capítulo inaugura la interacción entre dos estructuras distintas —grupo y orden—. La tarea cognitiva principal es distinguir: propiedades internas del orden, propiedades internas del grupo y axiomas de compatibilidad. Después reconstruiremos el orden completo a partir de una sola región del grupo: su cono no negativo.

La Parte V permanecerá estrictamente algebraico-ordenada. No introduciremos aquí completitud, convergencia ni argumentos topológicos.

---

## 25.1. Interfaz fundacional de órdenes

### Interfaz 25.1.1 — Órdenes parciales, totales y orden estricto asociado {#talg-imp-00004}

Reutilizamos de `TA-0003` únicamente la infraestructura cerrada siguiente:

1. `TA-DEF-00025`: una relación $\le$ sobre un conjunto $A$ es un **orden parcial** si es reflexiva, antisimétrica y transitiva; es **total** si además
   $$
   \forall a,b\in A,\qquad a\le b\ \lor\ b\le a;
   $$
2. `TA-DEF-00026`: dado un orden parcial,
   $$
   a<b
   \quad\Longleftrightarrow\quad
   a\le b\ \land\ a\ne b.
   $$

No importamos cotas, supremos, ínfimos, completitud ni la proposición general de tricotomía. La interfaz es deliberadamente mínima y no crea ciclo: `TA-0003` es fundacional, está cerrado y no utiliza resultados `TALG-*`.

> **Lectura fundacional.** Que un orden sea total es una propiedad matemática expresada mediante una disyunción. No se interpretará automáticamente como disponibilidad de un algoritmo para decidir comparaciones.

---

## 25.2. Compatibilidad bilateral

### Definición 25.2.1 — Grupo ordenado {#talg-def-00056}

Sea

$$
\mathcal G=\langle G,\star\rangle
$$

un grupo y sea $\le$ un orden parcial sobre $G$. Diremos que

$$
\langle G,\langle\star,\le\rangle\rangle
$$

es un **grupo ordenado** si, para todos $a,b,x\in G$,

$$
\boxed{
a\le b\Longrightarrow x\star a\le x\star b
}
$$

y

$$
\boxed{
a\le b\Longrightarrow a\star x\le b\star x.
}
$$

Es decir: las traslaciones por la izquierda y por la derecha preservan el orden.

La definición **no** exige que $\le$ sea total. Tampoco presupone decidibilidad de $a\le b$ ni de $a=b$.

> **Prueba de estrés de la definición.** Pedir solamente que $\le$ sea un orden parcial produciría dos estructuras coexistentes, pero no relacionadas. Pedir sólo compatibilidad izquierda sería suficiente para estudiar grupos *left-ordered*, pero no garantiza la simetría estructural que necesitaremos al pasar a conjugación, conos y estructuras de anillo. La bilateralidad es aquí una decisión deliberada.

---

### Notación 25.2.2 — Estructura de grupo ordenado {#talg-not-00018}

Cuando el contexto sea inequívoco escribiremos

$$
\mathcal G_{\le}
:=
\langle G,\langle\star,\le\rangle\rangle
$$

para una estructura de grupo ordenado. La escritura es una abreviatura mediante pares anidados; no introduce una terna primitiva.

---

## 25.3. Trasladar no sólo preserva: también refleja

### Proposición 25.3.1 — Invariancia bilateral exacta del orden {#talg-pro-00062}

Sea $\mathcal G_{\le}$ un grupo ordenado. Para todos $a,b,x\in G$,

$$
\boxed{
a\le b
\iff
x\star a\le x\star b
}
$$

y

$$
\boxed{
a\le b
\iff
a\star x\le b\star x.
}
$$

#### Demostración {#talg-prf-00101}

Las implicaciones hacia la derecha son exactamente los axiomas de compatibilidad de la [Definición 25.2.1](tratado-de-algebra-capitulo-25-grupos-ordenados.md#talg-def-00056).

Supongamos ahora

$$
x\star a\le x\star b.
$$

La compatibilidad izquierda permite trasladar por $x^{-1}$:

$$
x^{-1}\star(x\star a)
\le
x^{-1}\star(x\star b).
$$

Por asociatividad y las leyes de inverso y neutro,

$$
a\le b.
$$

El argumento derecho es análogo: de $a\star x\le b\star x$ trasladamos por $x^{-1}$ a la derecha y obtenemos $a\le b$. $\square$

> **Autoexplicación.** El axioma dice que trasladar **preserva** el orden. La existencia de traslaciones inversas —propia del grupo— mejora el resultado: trasladar también **refleja** el orden.

---

### Corolario 25.3.2 — En un grupo abeliano basta una compatibilidad lateral {#talg-cor-00016}

Sea $\mathcal G=\langle G,\star\rangle$ un grupo abeliano y $\le$ un orden parcial sobre $G$. Entonces son equivalentes:

1. $a\le b\Rightarrow x\star a\le x\star b$ para todos $a,b,x\in G$;
2. $a\le b\Rightarrow a\star x\le b\star x$ para todos $a,b,x\in G$;
3. $\langle G,\langle\star,\le\rangle\rangle$ es un grupo ordenado.

#### Demostración {#talg-prf-00102}

En un grupo abeliano,

$$
x\star a=a\star x,
\qquad
x\star b=b\star x.
$$

Por tanto la compatibilidad izquierda y la derecha son la misma afirmación escrita en distinto orden. Cualquiera de ellas implica ambas y, por la [Definición 25.2.1](tratado-de-algebra-capitulo-25-grupos-ordenados.md#talg-def-00056), la estructura es un grupo ordenado. La implicación de (3) hacia (1) y (2) es inmediata por definición. $\square$

Este corolario será la forma relevante para los grupos aditivos de anillos, que son abelianos.

---

## 25.4. Invertir revierte el orden

### Proposición 25.4.1 — La inversión es antítona {#talg-pro-00063}

Para todos $a,b\in G$,

$$
\boxed{
a\le b
\iff
b^{-1}\le a^{-1}.
}
$$

#### Demostración {#talg-prf-00103}

Supongamos $a\le b$. Por invariancia izquierda,

$$
b^{-1}\star a\le e.
$$

Trasladando esta desigualdad por $a^{-1}$ a la derecha,

$$
b^{-1}\le a^{-1}.
$$

Recíprocamente, si $b^{-1}\le a^{-1}$, aplicamos el mismo argumento a $b^{-1}$ y $a^{-1}$. Sus inversos son $b$ y $a$, respectivamente, y obtenemos $a\le b$. $\square$

En particular,

$$
e\le a\iff a^{-1}\le e,
$$

y

$$
a\le e\iff e\le a^{-1}.
$$

---

## 25.5. El orden estricto también es compatible

### Proposición 25.5.1 — Traslación e inversión del orden estricto {#talg-pro-00064}

Si $a<b$, entonces para todo $x\in G$,

$$
\boxed{x\star a<x\star b,}
$$

$$
\boxed{a\star x<b\star x,}
$$

y

$$
\boxed{b^{-1}<a^{-1}.}
$$

#### Demostración {#talg-prf-00104}

Por la definición importada de orden estricto,

$$
a<b
\Longrightarrow
a\le b\ \land\ a\ne b.
$$

La [Proposición 25.3.1](tratado-de-algebra-capitulo-25-grupos-ordenados.md#talg-pro-00062) preserva la parte no estricta. Además $x\star a=x\star b$ implicaría $a=b$ al trasladar por $x^{-1}$, contradicción. Por tanto $x\star a<x\star b$. El caso derecho es idéntico.

Por la [Proposición 25.4.1](tratado-de-algebra-capitulo-25-grupos-ordenados.md#talg-pro-00063), $a\le b$ implica $b^{-1}\le a^{-1}$. Si $b^{-1}=a^{-1}$, al invertir ambos elementos se obtiene $b=a$, contradicción. Luego $b^{-1}<a^{-1}$. $\square$

No se ha utilizado una tricotomía ni un procedimiento para decidir $a<b$.

---

## 25.6. Cuando todas las parejas son comparables

### Definición 25.6.1 — Grupo totalmente ordenado {#talg-def-00057}

Un **grupo totalmente ordenado** es un grupo ordenado $\mathcal G_{\le}$ cuya relación $\le$ es un orden total sobre $G$.

Así, para todos $a,b\in G$ se dispone matemáticamente de

$$
a\le b\ \lor\ b\le a.
$$

Esta totalidad no se reinterpretará como decidibilidad algorítmica del orden.

> **Separación conceptual.** “Grupo ordenado” significa en este tratado *parcialmente ordenado y bilateralmente compatible*. “Grupo totalmente ordenado” añade comparabilidad de todos los pares. Mantener ambas nociones evita introducir totalidad donde los argumentos sólo necesitan monotonía.

---

## 25.7. El cono no negativo

### Definición 25.7.1 — Cono no negativo de un grupo ordenado {#talg-def-00058}

Sea $\mathcal G_{\le}$ un grupo ordenado y sea $e$ su neutro. Definimos el **cono no negativo** por

$$
\boxed{
P_{\mathcal G}
:=
\{g\in G:e\le g\}.
}
$$

Su existencia como conjunto se obtiene por Separación dentro de $G$.

El término “cono” no introduce aquí estructura geométrica ni convexidad: designa la región del grupo situada por encima del neutro.

---

### Notación 25.7.2 — Cono no negativo {#talg-not-00019}

Usaremos $P_{\mathcal G}$ —o simplemente $P$ cuando no haya ambigüedad— para el cono no negativo de un grupo ordenado.

---

### Proposición 25.7.3 — Propiedades algebraicas del cono no negativo {#talg-pro-00065}

El cono $P=P_{\mathcal G}$ satisface:

1. $e\in P$;
2. si $a,b\in P$, entonces $a\star b\in P$;
3. si $a\in P$ y $x\in G$, entonces
   $$
   x\star a\star x^{-1}\in P;
   $$
4. si $a\in P$ y $a^{-1}\in P$, entonces $a=e$.

#### Demostración {#talg-prf-00105}

1. La reflexividad del orden da $e\le e$, luego $e\in P$.
2. Sean $e\le a$ y $e\le b$. Trasladando $e\le b$ por $a$ a la izquierda obtenemos
   $$
   a\le a\star b.
   $$
   Con $e\le a$ y transitividad,
   $$
   e\le a\star b.
   $$
3. De $e\le a$, trasladamos por $x$ a la izquierda y por $x^{-1}$ a la derecha:
   $$
   x\star e\star x^{-1}
   \le
   x\star a\star x^{-1}.
   $$
   El miembro izquierdo es $e$.
4. Si $e\le a$, la [Proposición 25.4.1](tratado-de-algebra-capitulo-25-grupos-ordenados.md#talg-pro-00063) da $a^{-1}\le e$. Como además $e\le a^{-1}$, la antisimetría produce $a^{-1}=e$, y por tanto $a=e$.

Así el cono está cerrado multiplicativamente, es estable por conjugación y es apuntado en el neutro. $\square$

> **Lectura estructural.** Las cuatro propiedades anteriores son la huella algebraica del orden. La siguiente proposición muestra que el orden entero puede leerse desde esa huella.

---

### Proposición 25.7.4 — El orden se recupera desde el cono {#talg-pro-00066}

Para todos $a,b\in G$,

$$
\boxed{
a\le b
\iff
a^{-1}\star b\in P_{\mathcal G}
}
$$

y también

$$
\boxed{
a\le b
\iff
b\star a^{-1}\in P_{\mathcal G}.
}
$$

#### Demostración {#talg-prf-00106}

Por la [Proposición 25.3.1](tratado-de-algebra-capitulo-25-grupos-ordenados.md#talg-pro-00062), trasladar por $a^{-1}$ a la izquierda preserva y refleja el orden:

$$
a\le b
\iff
e\le a^{-1}\star b.
$$

La última condición significa exactamente

$$
a^{-1}\star b\in P_{\mathcal G}.
$$

Trasladando por $a^{-1}$ a la derecha se obtiene análogamente

$$
a\le b
\iff
e\le b\star a^{-1}
\iff
b\star a^{-1}\in P_{\mathcal G}.
$$

$\square$

---

## 25.8. Reconstrucción del orden desde datos algebraicos

### Teorema 25.8.1 — Caracterización por cono no negativo {#talg-thm-00018}

Sea $\mathcal G=\langle G,\star\rangle$ un grupo y sea $P\subseteq G$ un subconjunto tal que:

1. $e\in P$;
2. $a,b\in P\Rightarrow a\star b\in P$;
3. $a\in P$ y $x\in G\Rightarrow x\star a\star x^{-1}\in P$;
4. $a\in P$ y $a^{-1}\in P\Rightarrow a=e$.

Definimos una relación $\preceq_P$ sobre $G$ por

$$
\boxed{
a\preceq_P b
\quad\Longleftrightarrow\quad
a^{-1}\star b\in P.
}
$$

Entonces $\preceq_P$ es un orden parcial bilateralmente compatible con la operación del grupo. Por tanto,

$$
\boxed{
\langle G,\langle\star,\preceq_P\rangle\rangle
}
$$

es un grupo ordenado. Además, su cono no negativo es exactamente $P$.

#### Demostración {#talg-prf-00107}

La relación existe por Separación como subconjunto de $G\times G$.

**Reflexividad.** Para $a\in G$,

$$
a^{-1}\star a=e\in P,
$$

luego $a\preceq_P a$.

**Antisimetría.** Supongamos $a\preceq_P b$ y $b\preceq_P a$. Entonces

$$
a^{-1}\star b\in P
$$

y

$$
b^{-1}\star a=(a^{-1}\star b)^{-1}\in P.
$$

Por (4), $a^{-1}\star b=e$, de donde $a=b$.

**Transitividad.** Si $a\preceq_P b$ y $b\preceq_P c$, entonces

$$
a^{-1}\star b\in P,
\qquad
b^{-1}\star c\in P.
$$

Por (2),

$$
(a^{-1}\star b)\star(b^{-1}\star c)
=
a^{-1}\star c
\in P.
$$

Luego $a\preceq_P c$.

**Compatibilidad izquierda.** Si $a\preceq_P b$, entonces para $x\in G$,

$$
(x\star a)^{-1}\star(x\star b)
=
a^{-1}\star b
\in P.
$$

Por tanto $x\star a\preceq_P x\star b$.

**Compatibilidad derecha.** Si $a\preceq_P b$, entonces

$$
(a\star x)^{-1}\star(b\star x)
=
x^{-1}\star(a^{-1}\star b)\star x.
$$

El miembro derecho pertenece a $P$ por (3). Por tanto

$$
a\star x\preceq_P b\star x.
$$

Así $\preceq_P$ satisface la [Definición 25.2.1](tratado-de-algebra-capitulo-25-grupos-ordenados.md#talg-def-00056).

Finalmente,

$$
e\preceq_P g
\iff
e^{-1}\star g=g\in P,
$$

de modo que el cono no negativo inducido es exactamente $P$. $\square$

> **Reconstrucción.** El orden no es información completamente independiente: una vez fijado el grupo, queda codificado por qué elementos se consideran no negativos, siempre que ese subconjunto satisfaga las cuatro condiciones anteriores.

---

### Proposición 25.8.2 — Totalidad en términos del cono {#talg-pro-00067}

Sea $\mathcal G_{\le}$ un grupo ordenado con cono $P=P_{\mathcal G}$. Entonces el orden es total si y sólo si

$$
\boxed{
\forall g\in G,
\qquad
g\in P\ \lor\ g^{-1}\in P.
}
$$

#### Demostración {#talg-prf-00108}

Supongamos primero que el orden es total. Para $g\in G$, la totalidad aplicada a $e$ y $g$ da

$$
e\le g
\quad\lor\quad
g\le e.
$$

La primera alternativa equivale a $g\in P$. En la segunda, la [Proposición 25.4.1](tratado-de-algebra-capitulo-25-grupos-ordenados.md#talg-pro-00063) da $e\le g^{-1}$, es decir, $g^{-1}\in P$.

Recíprocamente, supongamos que para todo $g$ vale $g\in P$ o $g^{-1}\in P$. Sean $a,b\in G$ y apliquemos la hipótesis a

$$
g=a^{-1}\star b.
$$

Si $g\in P$, la [Proposición 25.7.4](tratado-de-algebra-capitulo-25-grupos-ordenados.md#talg-pro-00066) da $a\le b$. Si $g^{-1}\in P$, entonces

$$
g^{-1}=b^{-1}\star a\in P,
$$

y la [Proposición 25.7.4](tratado-de-algebra-capitulo-25-grupos-ordenados.md#talg-pro-00066) da $b\le a$. Por tanto $\le$ es total. $\square$

Esta equivalencia expresa totalidad mediante una condición positiva sobre el cono; no afirma que la disyunción sea decidible algorítmicamente.

---

## 25.9. Cierre conceptual

La estructura desarrollada puede comprimirse en la cadena

$$
\boxed{
\text{grupo}
+
\text{orden parcial}
+
\text{traslaciones monótonas bilaterales}
\Longrightarrow
\text{grupo ordenado}.
}
$$

A partir de ella obtenemos:

$$
\text{traslaciones preservan y reflejan orden},
$$

$$
\text{inversión revierte orden},
$$

$$
\text{orden estricto compatible},
$$

$$
\text{orden}\longleftrightarrow\text{cono no negativo}.
$$

El último paso prepara directamente el capítulo siguiente. Para ordenar un anillo, la suma proporcionará el grupo abeliano ordenado y la multiplicación deberá respetar la región no negativa.

### Control fundacional de cierre

- Choice: `none`.
- Lógica clásica sustantiva nueva: `none`.
- Totalidad no se confunde con decidibilidad.
- El cono existe por Separación; no se eligen representantes ni testigos globales.
- No se introduce completitud ni ninguna noción analítica.
- Nueva interfaz intertratados: únicamente `TA-DEF-00025` y `TA-DEF-00026` desde el capítulo fundacional cerrado `TA-0003`.

---

[← **Capítulo 24 — Cuerpo de fracciones de un dominio íntegro**](tratado-de-algebra-capitulo-24-cuerpo-de-fracciones-de-un-dominio-integro.md) · [**Tratado moderno de Álgebra** →](../otros/tratado-de-algebra.md)
