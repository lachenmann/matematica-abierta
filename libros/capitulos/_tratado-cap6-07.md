## 6.7. Inversos multiplicativos {#sec-ta-6-7}

Sea $\alpha>_D0_D$. Los racionales positivos exteriores $s\notin\alpha$ están por encima de la frontera; sus recíprocos sugieren cotas superiores para la frontera recíproca. Esto conduce a la siguiente construcción interna.

### Definición 6.7.1 — Candidato a recíproco de una cortadura positiva

Para $\alpha\in\mathbb R_D^{>0}$ definimos

$$
\boxed{
I_D^+(\alpha)
:=
\{q\in\mathbb Q:
q\le0
\ \text{o}\\
\exists s\in\mathbb Q\;(0<s\land s\notin\alpha\land q<s^{-1})
\}.
}
$$

### Proposición 6.7.2 — El candidato a recíproco es una cortadura positiva

Para toda $\alpha\in\mathbb R_D^{>0}$,

$$
\boxed{I_D^+(\alpha)\in\mathbb R_D^{>0}.}
$$

**Demostración.**

$0\in I_D^+(\alpha)$, luego el conjunto es no vacío. Como $\alpha$ es positiva, existe $a\in\alpha$ con $a>0$. Afirmamos que $a^{-1}\notin I_D^+(\alpha)$. Si perteneciera mediante la segunda cláusula, existiría $s>0$, $s\notin\alpha$, con $a^{-1}<s^{-1}$. La inversión del orden para positivos daría $s<a$, y la clausura inferior implicaría $s\in\alpha$, contradicción. Así el conjunto es propio.

La clausura inferior es inmediata en cada cláusula de la definición. Para la ausencia de máximo: si $q<0$, entonces $q<0\in I_D^+(\alpha)$; si $q=0$, elegimos $s\notin\alpha$, que necesariamente es positivo porque $0\in\alpha$, y luego por densidad $0<r<s^{-1}$; si $q>0$ y $q<s^{-1}$ para un testigo exterior positivo $s$, elegimos por densidad $q<r<s^{-1}$. En todos los casos aparece un elemento mayor del mismo conjunto.

Finalmente $0\in I_D^+(\alpha)$, de modo que Lema 6.4.2 — Caracterizaciones de la positividad lo hace estrictamente positivo. ∎

### Definición 6.7.3 — Recíproco positivo de Dedekind

Definimos

$$
\boxed{
\operatorname{inv}_D^+:\mathbb R_D^{>0}\longrightarrow\mathbb R_D^{>0},
\qquad
\operatorname{inv}_D^+(\alpha):=I_D^+(\alpha).
}
$$

### Teorema 6.7.4 — Ley del inverso para cortaduras positivas

Para toda $\alpha>_D0_D$,

$$
\boxed{
\alpha\cdot_D^+\operatorname{inv}_D^+(\alpha)
=1_D
=\operatorname{inv}_D^+(\alpha)\cdot_D^+\alpha.
}
$$

**Demostración.**

Probemos primero la igualdad de la izquierda. Si

$$
x\in\alpha\cdot_D^+\operatorname{inv}_D^+(\alpha),
$$

existen $a\in\alpha$, $a>0$, y $b>0$ en el recíproco con $x<ab$. La positividad de $b$ obliga a la segunda cláusula de la definición: existe $s>0$, $s\notin\alpha$, con $b<s^{-1}$. Por Lema 6.1.1 — Todo punto exterior domina una cortadura, $a<s$. Así

$$
x<ab<a/s<1,
$$

de modo que $x\in1_D$.

Recíprocamente, sea $x<1$. Si $x\le0$, elegimos elementos positivos $a\in\alpha$ y $b\in\operatorname{inv}_D^+(\alpha)$; entonces $x<ab$.

Supongamos $0<x<1$. Elijamos $c\in\alpha$ con $c>0$. Como $(1-x)c>0$, por densidad escogemos

$$
0<h<(1-x)c.
$$

Lema 6.3.1 — Aproximación racional de la frontera proporciona $a\in\alpha$ tal que $s:=a+h\notin\alpha$. Puesto que $c\in\alpha$ y $s\notin\alpha$, Lema 6.1.1 — Todo punto exterior domina una cortadura da $c<s=a+h$, por lo que $a>c-h>0$ y también $s>0$.

Además,

$$
(1-x)(c-h)-xh=(1-x)c-h>0.
$$

Como $a>c-h$ y $1-x>0$,

$$
(1-x)a>xh,
$$

o equivalentemente

$$
a>x(a+h)=xs.
$$

Así

$$
\frac{x}{a}<\frac1s.
$$

Por densidad elegimos $b$ con

$$
\frac{x}{a}<b<\frac1s.
$$

Entonces $b>0$, $b\in\operatorname{inv}_D^+(\alpha)$ y $x<ab$. Por tanto $1_D\subseteq\alpha\cdot_D^+\operatorname{inv}_D^+(\alpha)$.

La igualdad con los factores invertidos se prueba sin usar conmutatividad posterior: en la primera inclusión los mismos testigos dan $x<ba<1$; en la segunda, los $a,b$ recién construidos satisfacen también $x<ba$ por conmutatividad de la multiplicación racional. ∎

### Proposición 6.7.5 — Compatibilidad con los recíprocos racionales positivos

Si $p>0$ es racional, entonces

$$
\boxed{\operatorname{inv}_D^+(\iota_D(p))=\iota_D(p^{-1}).}
$$

**Demostración.**

Sea $q\in\operatorname{inv}_D^+(\delta_p)$. Si $q\le0$, entonces $q<p^{-1}$. Si $q>0$, existe $s>0$, $s\notin\delta_p$, con $q<s^{-1}$. De $s\notin\delta_p$ se sigue $p\le s$, y por inversión del orden $s^{-1}\le p^{-1}$; luego $q<p^{-1}$. Así el recíproco está contenido en $\delta_{p^{-1}}$.

Recíprocamente, si $q<p^{-1}$ y $q\le0$, pertenece por la primera cláusula. Si $q>0$, tomamos $s=p$: $p\notin\delta_p$ y $q<p^{-1}=s^{-1}$. Por tanto $q$ pertenece al recíproco. ∎

### Definición 6.7.6 — Cortaduras no nulas

Definimos

$$
\boxed{\mathbb R_D^\times:=\{\alpha\in\mathbb R_D:\alpha\neq0_D\}.}
$$

> **Nota fundacional.** La condición $\alpha\neq0_D$ es negativa. Para una cortadura arbitraria no proporciona constructivamente el signo de $\alpha$ ni una separación positiva respecto de $0_D$. La definición clásica del inverso general utilizará la tricotomía heredada de Proposición 6.5.2 — Tricotomía respecto del cero; una futura capa efectiva empleará datos positivos de apartness.

### Definición 6.7.7 — Candidato a inverso general

Para $\alpha\in\mathbb R_D^\times$ definimos

$$
\boxed{
J_D(\alpha)
:=
\begin{cases}
\operatorname{inv}_D^+(\alpha),&\alpha>_D0_D,\\[1ex]
-_D\operatorname{inv}_D^+(-_D\alpha),&\alpha<_D0_D.
\end{cases}
}
$$

### Proposición 6.7.8 — El candidato general es no nulo

Para todo $\alpha\in\mathbb R_D^\times$,

$$
\boxed{J_D(\alpha)\in\mathbb R_D^\times.}
$$

Además conserva el signo de $\alpha$.

**Demostración.**

Si $\alpha>0_D$, Proposición 6.7.2 — El candidato a recíproco es una cortadura positiva hace $J_D(\alpha)$ positivo. Si $\alpha<0_D$, entonces $-_D\alpha>0_D$; su recíproco positivo es positivo y su opuesto es negativo por Lema 6.5.3 — El opuesto intercambia los signos. En ambos casos el resultado es no nulo. ∎

### Definición 6.7.9 — Inverso multiplicativo de Dedekind

La asignación anterior determina

$$
\boxed{
\operatorname{inv}_D:\mathbb R_D^\times\longrightarrow\mathbb R_D^\times,
\qquad
\alpha^{-1_D}:=\operatorname{inv}_D(\alpha).
}
$$

### Teorema 6.7.10 — Ley del inverso multiplicativo

Para toda $\alpha\in\mathbb R_D^\times$,

$$
\boxed{\alpha\cdot_D\alpha^{-1_D}=1_D=\alpha^{-1_D}\cdot_D\alpha.}
$$

**Demostración.**

Si $\alpha>0_D$, es Teorema 6.7.4 — Ley del inverso para cortaduras positivas, pues el producto general coincide con el positivo.

Si $\alpha<0_D$, pongamos $\beta:=-_D\alpha>0_D$. Entonces

$$
\alpha^{-1_D}=-_D\operatorname{inv}_D^+(\beta).
$$

Ambos factores son negativos, de modo que

$$
\alpha\cdot_D\alpha^{-1_D}
=(-_D\alpha)\cdot_D^+(-_D\alpha^{-1_D})
=\beta\cdot_D^+\operatorname{inv}_D^+(\beta)
=1_D,
$$

usando la involutividad del opuesto. El producto en el orden inverso se trata del mismo modo. ∎

### Definición 6.7.11 — División de Dedekind (operación derivada)

Sean $\alpha\in\mathbb R_D$ y $\beta\in\mathbb R_D^\times$, es decir, $\beta\neq0_D$. Definimos la división de Dedekind por

$$
\boxed{
\alpha\div_D\beta
:=\alpha\cdot_D\beta^{-1_D}.
}
$$

Esta definición determina una operación con dominio y codominio explícitos:

$$
\boxed{
\div_D:\mathbb R_D\times\mathbb R_D^\times\longrightarrow\mathbb R_D.
}
$$

La operación está bien definida: Definición 6.7.9 — Inverso multiplicativo de Dedekind asigna a cada $\beta\neq0_D$ un inverso multiplicativo único $\beta^{-1_D}\in\mathbb R_D$, y Definición 6.5.6 — Multiplicación de Dedekind proporciona el producto único $\alpha\cdot_D\beta^{-1_D}\in\mathbb R_D$; su clausura procede de Proposición 6.5.5 — Clausura y regla de signos del producto candidato. No se define $\alpha\div_D0_D$. En un contexto donde los operandos estén tipados como cortaduras, también escribiremos $\alpha/\beta$.

La división no es una nueva operación primitiva ni requiere axiomas adicionales: se obtiene de la multiplicación y la función inversa ya construidas. Su definición es extensional dentro de la base clásica del tratado y no afirma un algoritmo efectivo para cortaduras arbitrarias.
