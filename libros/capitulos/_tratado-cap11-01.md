## 11.1. Del proceso racional a la cortadura {#sec-ta-11-1}

Sea

$$
a=(a_n)_{n\in\mathbb N}\in\mathcal C_{\mathbb Q}.
$$

Si $a$ tuviera un límite $L$, la cortadura correspondiente debería contener exactamente los racionales $q$ situados estrictamente por debajo de $L$. Como no podemos mencionar todavía tal $L$, sustituiremos la desigualdad $q<L$ por una condición que pueda leerse directamente sobre la sucesión: $q$ debe quedar, a partir de cierto índice, **separado por un margen racional positivo** de todos los términos de $a$.

Esta condición reproduce exactamente el criterio de orden estricto ya demostrado para las clases de Cauchy, pero se formula primero en el nivel de representantes.

### Definición 11.1.1 — Lado inferior asociado a una sucesión racional de Cauchy

Para $a\in\mathcal C_{\mathbb Q}$ definimos

$$
\boxed{
\mathcal L_C(a)
:=
\left\{
q\in\mathbb Q:
\begin{array}{l}
\exists\varepsilon\in\mathbb Q\;\exists N\in\mathbb N\;\bigl(
0<\varepsilon\\[1mm]
\qquad\land\ \forall n\in\mathbb N\,
(N\le n\Rightarrow q+\varepsilon<a_n)
\bigr)
\end{array}
\right\}.
}
$$

En forma abreviada,

$$
q\in\mathcal L_C(a)
\iff
\exists\varepsilon>0\;\exists N\in\mathbb N\;
\forall n\ge N,
\quad
q+\varepsilon<a_n.
$$

El conjunto $\mathcal L_C(a)$ existe por Separación sobre $\mathbb Q$. La fórmula sólo utiliza la aritmética y el orden racionales ya construidos, la sucesión $a$ y cuantificación sobre $\mathbb N$.

La presencia del margen $\varepsilon>0$ es esencial. Exigir simplemente que $q<a_n$ eventualmente no sería estable frente a perturbaciones nulas: una sucesión puede oscilar alrededor de una frontera sin mantenerse de un solo lado. El margen positivo expresa que $q$ se encuentra **estrictamente** por debajo de la posición asintótica representada por $a$.

---

### Proposición 11.1.2 — Caracterización mediante el orden de $\mathbb R_C$

Para todo $a\in\mathcal C_{\mathbb Q}$ y todo $q\in\mathbb Q$,

$$
\boxed{
q\in\mathcal L_C(a)
\iff
\iota_C(q)<_C[a]_C.
}
$$

**Demostración.**

Fijemos $a\in\mathcal C_{\mathbb Q}$ y $q\in\mathbb Q$. La sucesión constante $\underline q$ pertenece a $\mathcal C_{\mathbb Q}$ por Proposición 8.4.4 — Las sucesiones constantes son de Cauchy, y por definición de la incrustación de Cauchy,

$$
\iota_C(q)=[\underline q]_C.
$$

Por Proposición 9.8.6 — Criterio de separación eventual para el orden estricto,

$$
[\underline q]_C<_C[a]_C
$$

si y sólo si existen $\varepsilon\in\mathbb Q$ y $N\in\mathbb N$ tales que

$$
0<\varepsilon
$$

y, para todo $n\ge N$,

$$
\underline q_n+\varepsilon<a_n.
$$

Como $\underline q_n=q$ para todo $n$, esta última condición equivale a

$$
\exists\varepsilon>0\;\exists N\in\mathbb N\;
\forall n\ge N,
\quad
q+\varepsilon<a_n,
$$

que es exactamente, por Definición 11.1.1 — Lado inferior asociado a una sucesión racional de Cauchy, la afirmación

$$
q\in\mathcal L_C(a).
$$

Por tanto,

$$
q\in\mathcal L_C(a)
\iff
\iota_C(q)<_C[a]_C.
$$

∎

> **Nota conceptual.** La proposición no redefine $\mathcal L_C(a)$ mediante $\mathbb R_C$. La definición permanece enteramente racional; el resultado demuestra después que esa condición racional coincide con estar por debajo de la clase $[a]_C$ en el cuerpo de Cauchy.

---

### Proposición 11.1.3 — El lado inferior de Cauchy es una cortadura de Dedekind

Para toda sucesión

$$
a\in\mathcal C_{\mathbb Q},
$$

se tiene

$$
\boxed{
\mathcal L_C(a)\in\mathbb R_D.
}
$$

**Demostración.**

Fijemos $a\in\mathcal C_{\mathbb Q}$. Por Teorema 8.6.3 — Toda sucesión racional de Cauchy es acotada, existe $B\in\mathbb Q$ con

$$
0_{\mathbb Q}\le B
$$

y

$$
|a_n|\le B
\qquad(n\in\mathbb N).
$$

Por Proposición 4.2.2 — Propiedades elementales del valor absoluto, para todo $n$,

$$
-B\le a_n\le B.
$$

Verificaremos directamente las cuatro condiciones de Definición 5.1.1 — Cortadura de Dedekind para $\mathcal L_C(a)$.

**1. No vaciedad.** Definamos

$$
q_-:=-B-1_{\mathbb Q}.
$$

Tomemos

$$
\varepsilon:=\frac{1_{\mathbb Q}}{2_{\mathbb Q}}>0.
$$

Como $-B\le a_n$ para todo $n$,

$$
q_-+\varepsilon
=
-B-\frac{1_{\mathbb Q}}{2_{\mathbb Q}}
<
-B
\le a_n
$$

para todo $n$. Por Definición 11.1.1 — Lado inferior asociado a una sucesión racional de Cauchy,

$$
q_-\in\mathcal L_C(a).
$$

Así $\mathcal L_C(a)$ está habitada y, en particular,

$$
\mathcal L_C(a)\neq\varnothing.
$$

**2. Propiedad.** Definamos

$$
q_+:=B+1_{\mathbb Q}.
$$

Afirmamos que

$$
q_+\notin\mathcal L_C(a).
$$

En efecto, si $q_+\in\mathcal L_C(a)$, existirían $\varepsilon>0$ y $N\in\mathbb N$ tales que

$$
q_++\varepsilon<a_n
$$

para todo $n\ge N$. Tomando $n=N$ y usando $a_N\le B$,

$$
B+1_{\mathbb Q}
<
q_++\varepsilon
<
a_N
\le B,
$$

contradicción. Luego

$$
q_+\in\mathbb Q\setminus\mathcal L_C(a),
$$

y por tanto

$$
\mathcal L_C(a)\neq\mathbb Q.
$$

**3. Clausura inferior.** Sean

$$
r\in\mathcal L_C(a),
\qquad
s<r.
$$

Por Definición 11.1.1 — Lado inferior asociado a una sucesión racional de Cauchy existen $\varepsilon>0$ y $N$ tales que

$$
r+\varepsilon<a_n
\qquad(n\ge N).
$$

Como $s<r$, la compatibilidad del orden racional con la suma da

$$
s+\varepsilon<r+\varepsilon<a_n
\qquad(n\ge N).
$$

Por tanto

$$
s\in\mathcal L_C(a).
$$

**4. Ausencia de máximo.** Sea

$$
r\in\mathcal L_C(a).
$$

Elijamos testigos locales $\varepsilon>0$ y $N$ con

$$
r+\varepsilon<a_n
\qquad(n\ge N).
$$

Definamos canónicamente

$$
s:=r+\frac{\varepsilon}{2_{\mathbb Q}}.
$$

Entonces

$$
r<s
$$

y

$$
s+\frac{\varepsilon}{2_{\mathbb Q}}
=
r+\varepsilon
<
a_n
\qquad(n\ge N).
$$

Por Definición 11.1.1 — Lado inferior asociado a una sucesión racional de Cauchy,

$$
s\in\mathcal L_C(a).
$$

Así ningún elemento de $\mathcal L_C(a)$ es máximo.

Se cumplen las cuatro condiciones de una cortadura de Dedekind. Por Definición 5.1.3 — Conjunto subyacente del modelo de Dedekind,

$$
\mathcal L_C(a)\in\mathbb R_D.
$$

∎

> **Nota fundacional.** La prueba ya no usa la densidad global de $\mathbb Q$ en $\mathbb R_C$. Todo se obtiene directamente de la acotación de la sucesión de Cauchy y de márgenes racionales explícitos. Los testigos utilizados son locales para la sucesión o el racional fijados; no interviene Choice.

### Definición 11.1.4 — Aplicación de representantes de Cauchy a cortaduras

Por Proposición 11.1.3 — El lado inferior de Cauchy es una cortadura de Dedekind, para cada $a\in\mathcal C_{\mathbb Q}$ el conjunto $\mathcal L_C(a)$ pertenece a $\mathbb R_D$. Definimos entonces

$$
\boxed{
\Lambda_C:
\mathcal C_{\mathbb Q}
\longrightarrow
\mathbb R_D,
\qquad
\Lambda_C(a):=\mathcal L_C(a).
}
$$

Conjuntistamente, su grafo es

$$
G_{\Lambda_C}
:=
\left\{
\langle a,\alpha\rangle
\in
\mathcal C_{\mathbb Q}\times\mathbb R_D:
\alpha=\mathcal L_C(a)
\right\}.
$$

El producto cartesiano existe, y el subconjunto indicado se obtiene por Separación. Para cada $a\in\mathcal C_{\mathbb Q}$ existe exactamente una $\alpha\in\mathbb R_D$ que satisface la condición, pues $\mathcal L_C(a)$ es un conjunto unívocamente determinado por Definición 11.1.1 — Lado inferior asociado a una sucesión racional de Cauchy y pertenece a $\mathbb R_D$ por Proposición 11.1.3 — El lado inferior de Cauchy es una cortadura de Dedekind. Por tanto $G_{\Lambda_C}$ es el grafo de una función.

Todavía **no** hemos construido una función

$$
\mathbb R_C\to\mathbb R_D.
$$

La función $\Lambda_C$ tiene como dominio las **sucesiones representantes**, no sus clases. Antes de descenderla al cociente debemos probar la afirmación decisiva:

$$
a\sim_C b
\Longrightarrow
\Lambda_C(a)=\Lambda_C(b).
$$

Éste es exactamente el problema de §11.2.

---
