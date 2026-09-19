## 6.4. Producto de cortaduras positivas {#sec-ta-6-4}

El conjunto $\{ab:a\in\alpha,b\in\beta\}$ no puede utilizarse para cortaduras arbitrarias: toda cortadura contiene racionales negativos arbitrariamente pequeños y los productos de dos de ellos pueden ser positivos arbitrariamente grandes. Comenzaremos en el cono estrictamente positivo y multiplicaremos únicamente racionales positivos situados bajo las fronteras.

### Definición 6.4.1 — Cortaduras estrictamente positivas

Definimos

$$
\boxed{\mathbb R_D^{>0}:=\{\alpha\in\mathbb R_D:0_D<_D\alpha\}.}
$$

### Lema 6.4.2 — Caracterizaciones de la positividad

Para $\alpha\in\mathbb R_D$ son equivalentes:

1. $0_D<_D\alpha$;
2. $0_{\mathbb Q}\in\alpha$;
3. existe $a\in\alpha$ con $0<a$.

**Demostración.**

Si $0_D<_D\alpha$, entonces $0_D\subsetneq\alpha$. Existe $x\in\alpha\setminus0_D$, de modo que $0\le x$. Si $x=0$, ya tenemos $0\in\alpha$; si $x>0$, la clausura inferior da también $0\in\alpha$.

Si $0\in\alpha$, la ausencia de máximo proporciona $a\in\alpha$ con $0<a$.

Finalmente, si $a\in\alpha$ y $a>0$, todo $q\in0_D$ satisface $q<0<a$, por lo que $q\in\alpha$. Así $0_D\subseteq\alpha$, y la inclusión es propia porque $a\in\alpha\setminus0_D$. Luego $0_D<_D\alpha$. ∎

### Definición 6.4.3 — Parte positiva de una cortadura

Para $\alpha\in\mathbb R_D$ definimos

$$
\boxed{\alpha_{>0}:=\{a\in\alpha:0<a\}.}
$$

Si $\alpha\in\mathbb R_D^{>0}$, Lema 6.4.2 — Caracterizaciones de la positividad garantiza $\alpha_{>0}\neq\varnothing$.

### Definición 6.4.4 — Candidato a producto positivo

Para $\alpha,\beta\in\mathbb R_D^{>0}$ definimos

$$
\boxed{
\Pi_D^+(\alpha,\beta)
:=
\{q\in\mathbb Q:\exists a\in\alpha_{>0}\;\exists b\in\beta_{>0}\;(q<ab)\}.
}
$$

La desigualdad estricta hace que el conjunto sea desde el inicio el lado inferior generado por los productos positivos.

### Proposición 6.4.5 — El producto positivo es una cortadura positiva

Si $\alpha,\beta\in\mathbb R_D^{>0}$, entonces

$$
\boxed{\Pi_D^+(\alpha,\beta)\in\mathbb R_D^{>0}.}
$$

**Demostración.**

Por positividad existen $a\in\alpha$ y $b\in\beta$ con $a,b>0$. Entonces $0<ab$, de modo que $0\in\Pi_D^+(\alpha,\beta)$; el conjunto es no vacío y, una vez probada su condición de cortadura, será positivo.

Para demostrar que es propio, elegimos $u\notin\alpha$ y $v\notin\beta$. Como $\alpha$ y $\beta$ contienen elementos positivos, Lema 6.1.1 — Todo punto exterior domina una cortadura muestra que $u,v>0$. Para cualesquiera $a\in\alpha_{>0}$ y $b\in\beta_{>0}$,

$$
a<u,
\qquad
b<v,
$$

y por compatibilidad del orden con el producto positivo,

$$
ab<ub<uv.
$$

Así $uv\notin\Pi_D^+(\alpha,\beta)$.

La clausura inferior es inmediata: si $r<x<ab$, entonces $r<ab$ con los mismos testigos. Para la ausencia de máximo, dado $x<ab$, la densidad racional proporciona $y$ con $x<y<ab$, y el mismo par $(a,b)$ muestra $y\in\Pi_D^+(\alpha,\beta)$.

Se trata, por tanto, de una cortadura. Como contiene $0$, Lema 6.4.2 — Caracterizaciones de la positividad da

$$
0_D<_D\Pi_D^+(\alpha,\beta).
$$

∎

### Definición 6.4.6 — Multiplicación positiva de Dedekind

La construcción anterior determina

$$
\boxed{
\cdot_D^+:\mathbb R_D^{>0}\times\mathbb R_D^{>0}\longrightarrow\mathbb R_D^{>0},
\qquad
\alpha\cdot_D^+\beta:=\Pi_D^+(\alpha,\beta).
}
$$

Reservaremos $\cdot_D$ para la multiplicación definida sobre todos los signos.

### Proposición 6.4.7 — Las imágenes de racionales positivos son positivas

Si $p\in\mathbb Q$ y $0<p$, entonces

$$
\boxed{\iota_D(p)\in\mathbb R_D^{>0}.}
$$

**Demostración.**

$\iota_D(p)=\delta_p$, y $0<p$ implica $0\in\delta_p$. Lema 6.4.2 — Caracterizaciones de la positividad proporciona la conclusión. ∎

### Proposición 6.4.8 — El producto positivo prolonga el producto racional positivo

Si $p,q\in\mathbb Q$ son positivos, entonces

$$
\boxed{\iota_D(pq)=\iota_D(p)\cdot_D^+\iota_D(q).}
$$

**Demostración.**

Si $x\in\delta_p\cdot_D^+\delta_q$, existen $0<a<p$ y $0<b<q$ con $x<ab$. Entonces $ab<pb<pq$, luego $x<pq$ y $x\in\delta_{pq}$.

Recíprocamente, sea $x<pq$. Si $x\le0$, la densidad proporciona $0<a<p$ y $0<b<q$, de modo que $x\le0<ab$ y $x$ pertenece al producto positivo.

Supongamos $0<x<pq$. Como $q>0$,

$$
\frac{x}{q}<p.
$$

Por densidad escogemos $a$ con

$$
\frac{x}{q}<a<p.
$$

Entonces $a>0$ y $x<aq$, por lo que $x/a<q$. Otra aplicación de la densidad proporciona $b$ con

$$
\frac{x}{a}<b<q.
$$

Así $a\in\delta_p$, $b\in\delta_q$, ambos son positivos y $x<ab$. Por doble inclusión,

$$
\delta_{pq}=\delta_p\cdot_D^+\delta_q.
$$

∎
