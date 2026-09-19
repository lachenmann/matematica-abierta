## 6.6. La unidad multiplicativa {#sec-ta-6-6}

### Definición 6.6.1 — Unidad de Dedekind

Definimos

$$
\boxed{1_D:=\iota_D(1_{\mathbb Q})=\delta_{1_{\mathbb Q}}.}
$$

### Proposición 6.6.2 — La unidad de Dedekind es estrictamente positiva

Se tiene

$$
\boxed{0_D<_D1_D.}
$$

En particular, $0_D\neq1_D$ y $1_D\in\mathbb R_D^{>0}$.

**Demostración.**

En $\mathbb Q$, $0<1$. Corolario 5.5.3 — $\iota_D$ es inyectiva y preserva y refleja el orden estricto muestra que $\iota_D$ preserva el orden estricto, luego $0_D<_D1_D$. ∎

### Lema 6.6.3 — Involutividad del opuesto

Para toda $\alpha\in\mathbb R_D$,

$$
\boxed{-_D(-_D\alpha)=\alpha.}
$$

**Demostración.**

Tanto $\alpha$ como $-_D(-_D\alpha)$ son inversos aditivos de $-_D\alpha$. Por unicidad del inverso, obtenida de la cancelación aditiva, son iguales. ∎

### Proposición 6.6.4 — La unidad actúa como neutro sobre cortaduras positivas

Si $\alpha>_D0_D$, entonces

$$
\boxed{\alpha\cdot_D^+1_D=\alpha=1_D\cdot_D^+\alpha.}
$$

**Demostración.**

Sea $x\in\alpha\cdot_D^+1_D$. Existen $a\in\alpha$, $0<a$, y $b$ con $0<b<1$ tales que $x<ab$. Como $ab<a$, la clausura inferior da $x\in\alpha$. Así $\alpha\cdot_D^+1_D\subseteq\alpha$.

Para la inclusión inversa, sea $x\in\alpha$. Si $x\le0$, elegimos cualquier $a\in\alpha$ positivo y, por densidad, $0<b<1$; entonces $x<ab$. Si $x>0$, la ausencia de máximo da $a\in\alpha$ con $x<a$. Así $0<x/a<1$, y por densidad existe $b$ con

$$
\frac{x}{a}<b<1.
$$

Entonces $b\in1_D$ y $x<ab$, por lo que $x\in\alpha\cdot_D^+1_D$.

La identidad $1_D\cdot_D^+\alpha=\alpha$ se demuestra del mismo modo con el orden de los dos testigos intercambiado: si $x<ba$ con $0<b<1$ y $a\in\alpha_{>0}$, entonces $x<a$; en la inclusión inversa se utilizan exactamente los mismos $a$ y $b$. ∎

### Teorema 6.6.5 — Leyes de la unidad multiplicativa

Para toda $\alpha\in\mathbb R_D$,

$$
\boxed{\alpha\cdot_D1_D=\alpha=1_D\cdot_D\alpha.}
$$

**Demostración.**

Si $\alpha=0_D$, es inmediato. Si $\alpha>_D0_D$, la multiplicación general coincide con $\cdot_D^+$ y la afirmación es Proposición 6.6.4 — La unidad actúa como neutro sobre cortaduras positivas.

Supongamos $\alpha<_D0_D$. Entonces $-_D\alpha>_D0_D$. Por definición signada,

$$
\alpha\cdot_D1_D
=-_D\bigl((-_D\alpha)\cdot_D^+1_D\bigr)
=-_D(-_D\alpha)
=\alpha.
$$

La identidad por la izquierda es igual. ∎
