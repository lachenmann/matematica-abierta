## 13.7. Sucesiones monótonas y convergencia monótona {#sec-ta-13-7}

Hasta ahora la convergencia ha aparecido siempre como una hipótesis: suponíamos que una sucesión tenía límite y estudiábamos qué consecuencias se seguían de ello. La completitud de $\mathbb R$ permite invertir por primera vez esa dirección. Bajo condiciones adecuadas de orden y acotación, podremos **producir** la existencia del límite.

La idea central será sencilla pero profunda. Si una sucesión avanza siempre en una misma dirección y no puede escapar más allá de una cota, el extremo de su recorrido —su supremo o su ínfimo— será el único candidato posible a límite. La completitud garantiza que ese extremo existe; la monotonía obliga después a toda la cola a acercarse a él.

### Definición 13.7.1 — Sucesiones monótonas

Sea $a=(a_n)$ una sucesión real.

Diremos que $a$ es **creciente** si

$$
\boxed{
\forall n,m\in\mathbb N,
\qquad
n\le m\Longrightarrow a_n\le a_m.
}
$$

Diremos que $a$ es **decreciente** si

$$
\boxed{
\forall n,m\in\mathbb N,
\qquad
n\le m\Longrightarrow a_m\le a_n.
}
$$

Diremos que $a$ es **monótona** si es creciente o decreciente.

> **Convención terminológica.** En este tratado, «creciente» y «decreciente» significan monotonía **no estricta**. Si más adelante necesitamos las nociones estrictas, escribiremos explícitamente «estrictamente creciente» o «estrictamente decreciente».

Una sucesión constante es simultáneamente creciente y decreciente. La definición, por tanto, describe una dirección de orden, no un cambio obligatorio de valor entre términos consecutivos.

> **Lectura conceptual.** La monotonía es una condición global sobre pares de índices. No afirma todavía que exista límite. Lo que impide a una sucesión creciente escapar hacia arriba no es la monotonía, sino la presencia adicional de una cota superior; dualmente, una sucesión decreciente necesitará una cota inferior.

---

### Proposición 13.7.2 — La acotación pertinente de una sucesión monótona es unilateral

Sea $a=(a_n)$ una sucesión real.

1. Si $a$ es creciente, entonces
   $$
   \boxed{
   a\text{ es acotada}
   \iff
   a\text{ es acotada superiormente}.
   }
   $$

2. Si $a$ es decreciente, entonces
   $$
   \boxed{
   a\text{ es acotada}
   \iff
   a\text{ es acotada inferiormente}.
   }
   $$

**Demostración.**

La implicación desde la acotación global hacia cualquiera de las dos cotas unilaterales es inmediata por Definición 13.4.1 — Sucesiones acotadas superiormente, inferiormente y acotadas.

Supongamos ahora que $a$ es creciente y está acotada superiormente. Para cada $n\in\mathbb N$ se cumple

$$
0\le n.
$$

En efecto, por Definición 1.6.1 — Orden aritmético basta exhibir $k\in\mathbb N$ tal que $n=0+k$; tomamos $k=n$ y usamos Proposición 1.4.2 — Cero neutro por la izquierda.

La monotonía da entonces

$$
a_0\le a_n
$$

para todo $n$. Así, $a_0$ es una cota inferior del recorrido $a[\mathbb N]$. Junto con la cota superior supuesta, Definición 13.4.1 — Sucesiones acotadas superiormente, inferiormente y acotadas muestra que $a$ es acotada.

El caso decreciente es dual. De $0\le n$ y la monotonía se obtiene

$$
a_n\le a_0
$$

para todo $n$; por tanto $a_0$ es una cota superior. Si además existe una cota inferior, la sucesión es acotada. ∎

> **Consecuencia estructural.** En presencia de monotonía, una de las dos cotas viene gratis del primer término. El problema auténtico de existencia del límite queda reducido a impedir el escape en la dirección en que la sucesión se mueve.

---

### Teorema 13.7.3 — Teorema de convergencia monótona

Sea $a=(a_n)$ una sucesión real.

1. Si $a$ es creciente y está acotada superiormente, entonces
   $$
   \boxed{
   a_n\longrightarrow \sup a[\mathbb N].
   }
   $$

2. Si $a$ es decreciente y está acotada inferiormente, entonces
   $$
   \boxed{
   a_n\longrightarrow \inf a[\mathbb N].
   }
   $$

**Demostración.**

Comenzamos por el caso creciente. Sea

$$
A:=a[\mathbb N].
$$

El conjunto $A$ está habitado: como $0\in\mathbb N$,

$$
a_0\in A.
$$

Por hipótesis, $A$ está acotado superiormente. Como $\mathbb R$ es un cuerpo ordenado completo, Definición 4.6.1 — Propiedad del supremo y cuerpo ordenado completo garantiza la existencia de

$$
s:=\sup A.
$$

Mostraremos que $a_n\to s$.

Sea $\varepsilon>0$. Entonces

$$
s-\varepsilon<s.
$$

Por definición de supremo, $s-\varepsilon$ no puede ser una cota superior de $A$: si lo fuera, la minimalidad de $s$ entre las cotas superiores implicaría

$$
s\le s-\varepsilon,
$$

contradiciendo $s-\varepsilon<s$.

Que $s-\varepsilon$ no sea cota superior significa

$$
\neg\Bigl(
\forall x\in A,
\;x\le s-\varepsilon
\Bigr).
$$

Aquí aparece el paso clásico central de la demostración. Por negación clásica de cuantificadores existe $x\in A$ tal que

$$
\neg(x\le s-\varepsilon).
$$

La totalidad del orden real da entonces

$$
s-\varepsilon<x.
$$

Como $x\in A=a[\mathbb N]$, existe $N\in\mathbb N$ con

$$
x=a_N.
$$

Por tanto

$$
s-\varepsilon<a_N.
$$

Si $n\ge N$, la monotonía creciente produce

$$
a_N\le a_n.
$$

Además, $s$ es una cota superior de $A$, de modo que

$$
a_n\le s.
$$

En consecuencia, para todo $n\ge N$,

$$
s-\varepsilon
<a_N
\le a_n
\le s
<s+\varepsilon.
$$

Así,

$$
s-\varepsilon<a_n<s+\varepsilon
$$

para todo índice suficientemente grande. Por la formulación en ventanas de Proposición 13.3.3 — Formulaciones equivalentes de la convergencia,

$$
a_n\to s.
$$

Esto demuestra la primera afirmación.

Consideremos ahora el caso decreciente. Sea nuevamente

$$
A:=a[\mathbb N].
$$

El conjunto está habitado por $a_0$ y, por hipótesis, está acotado inferiormente. La propiedad del ínfimo disponible en Proposición 4.6.2 — La propiedad del supremo implica la propiedad del ínfimo garantiza la existencia de

$$
i:=\inf A.
$$

Sea $\varepsilon>0$. Entonces

$$
i<i+\varepsilon.
$$

El elemento $i+\varepsilon$ no puede ser una cota inferior de $A$: si lo fuera, la maximalidad de $i$ entre las cotas inferiores daría

$$
i+\varepsilon\le i,
$$

contradiciendo $i<i+\varepsilon$.

Por negación clásica de cuantificadores existe, pues, $x\in A$ tal que

$$
\neg(i+\varepsilon\le x).
$$

La totalidad del orden implica

$$
x<i+\varepsilon.
$$

Escribiendo $x=a_N$ para algún $N\in\mathbb N$, obtenemos

$$
a_N<i+\varepsilon.
$$

Si $n\ge N$, la monotonía decreciente da

$$
a_n\le a_N.
$$

Como $i$ es cota inferior de $A$,

$$
i\le a_n.
$$

Por tanto

$$
i-\varepsilon
<i
\le a_n
\le a_N
<i+\varepsilon.
$$

De nuevo Proposición 13.3.3 — Formulaciones equivalentes de la convergencia concluye

$$
a_n\to i.
$$

Quedan demostradas ambas afirmaciones. ∎

> **Arquitectura de la prueba.** El argumento combina exactamente tres piezas:
>
> $$
> \boxed{
> \text{cota unilateral}
> \;\xrightarrow{\text{completitud}}\;
> \text{supremo/ínfimo}
> \;\xrightarrow{\text{no extremalidad de }s\mp\varepsilon}\;
> \text{un término cercano}
> \;\xrightarrow{\text{monotonía}}\;
> \text{toda la cola cercana}.
> }
> $$
>
> La completitud crea el candidato al límite; la monotonía transforma un solo término suficientemente próximo en control de toda la cola.

> **Nota fundacional.** Éste es el primer resultado del Capítulo 13 que utiliza esencialmente la completitud de $\mathbb R$. No usa Choice: para cada $\varepsilon>0$ se demuestra la existencia de algún umbral $N$, pero no se selecciona simultáneamente una función global $\varepsilon\mapsto N$. Bajo la interfaz actual de supremo/ínfimo, el paso «no es cota $\Rightarrow$ existe un elemento que la viola» usa negación clásica de cuantificadores. Tampoco se afirma que $\sup A$, $\inf A$ o los umbrales obtenidos sean computables.

> **Prueba de estrés.** La acotación y la monotonía cumplen funciones distintas. La cota produce un extremo dentro de $\mathbb R$; la monotonía impide que, después de alcanzar una zona próxima a ese extremo, la sucesión vuelva a alejarse de ella. Quitar cualquiera de las dos hipótesis destruye el mecanismo de la prueba.

---

### Corolario 13.7.4 — Criterio de convergencia para sucesiones monótonas

Sea $a=(a_n)$ una sucesión real monótona. Entonces

$$
\boxed{
a\text{ converge}
\iff
a\text{ es acotada}.
}
$$

**Demostración.**

Si $a$ converge, entonces es acotada por Teorema 13.4.5 — Toda sucesión real convergente es acotada.

Recíprocamente, supongamos que $a$ es acotada. Como es monótona, por Definición 13.7.1 — Sucesiones monótonas es creciente o decreciente.

- Si es creciente, la acotación proporciona en particular una cota superior, y Teorema 13.7.3 — Teorema de convergencia monótona (1) garantiza su convergencia.
- Si es decreciente, la acotación proporciona una cota inferior, y Teorema 13.7.3 — Teorema de convergencia monótona (2) garantiza su convergencia.

Por tanto toda sucesión real monótona y acotada converge. ∎

Este corolario resume el papel exacto de la completitud en esta clase de sucesiones:

$$
\boxed{
\text{monotonía}
+
\text{acotación}
\Longleftrightarrow
\text{convergencia}
\qquad
\text{(para sucesiones monótonas reales).}
}
$$

La equivalencia no sería verdadera en $\mathbb Q$: allí pueden existir sucesiones racionales monótonas y acotadas cuyo extremo natural no pertenece al cuerpo. La diferencia no está en la definición de sucesión ni en la de monotonía, sino en la completitud del espacio numérico en el que viven sus términos.

---

La sección ha producido por primera vez un límite sin suponerlo de antemano. El esquema esencial queda fijado como

$$
\boxed{
\text{monotonía}
+
\text{cota adecuada}
+
\text{completitud de }\mathbb R
\Longrightarrow
\text{convergencia}.
}
$$

El siguiente paso será abandonar la monotonía y buscar una condición interna sobre la propia sucesión que detecte convergencia sin conocer previamente el límite. Esa condición será la **condición de Cauchy**. En §13.8 definiremos sucesiones de Cauchy en $\mathbb R$ y demostraremos el criterio de Cauchy usando la completitud ya disponible.
---
