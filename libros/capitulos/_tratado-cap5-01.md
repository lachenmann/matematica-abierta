## 5.1. Definición y existencia de las cortaduras {#sec-ta-5-1}

### Definición 5.1.1 — Cortadura de Dedekind

Una **cortadura de Dedekind** es un subconjunto $\alpha\subseteq\mathbb Q$ que satisface las cuatro condiciones siguientes:

1. **no vaciedad:**
   $$
   \alpha\neq\varnothing;
   $$
2. **propiedad:**
   $$
   \alpha\neq\mathbb Q;
   $$
3. **clausura inferior:** si $r\in\alpha$ y $s<r$, entonces $s\in\alpha$;
4. **ausencia de máximo:** para todo $r\in\alpha$ existe $s\in\alpha$ tal que
   $$
   r<s.
   $$

La primera condición es necesaria porque el conjunto vacío satisfaría vacuamente la clausura inferior y la ausencia de máximo. La segunda excluye a $\mathbb Q$ mismo, que también es cerrado hacia abajo y, por densidad, carece de máximo.

La tercera condición expresa que una cortadura contiene con cada racional todos los racionales situados por debajo de él. La cuarta garantiza que el lado inferior no posee un último racional.

Conviene distinguir esta última propiedad de la ausencia de cota superior. Una cortadura puede estar acotada superiormente en $\mathbb Q$ y, sin embargo, no poseer máximo. Lo que excluimos es un **último elemento del propio lado inferior**.

Finalmente, la condición

$$
\forall r\in\alpha\;\exists s\in\alpha\;(r<s)
$$

no exige escoger simultáneamente un $s$ para cada $r$. Es una afirmación puramente existencial y no utiliza el axioma de elección.

> **Nota fundacional.** La definición anterior es la definición **clásica** que utilizaremos en el tratado. Sus dos primeras condiciones están formuladas negativamente:
> $$
> \alpha\neq\varnothing,
> \qquad
> \alpha\neq\mathbb Q.
> $$
> En lógica clásica permiten obtener, cuando una demostración lo necesita, un testigo interior $a\in\alpha$ y un testigo exterior $u\in\mathbb Q\setminus\alpha$. Constructivamente deben distinguirse:
> $$
> \boxed{
> \alpha\neq\varnothing\;\not\equiv\;\exists a\in\alpha,
> \qquad
> \alpha\neq\mathbb Q\;\not\equiv\;\exists u\notin\alpha.
> }
> $$
> No modificaremos aquí la noción clásica de cortadura. Más adelante, en la capa constructiva/efectiva, se aislarán datos positivos como habitabilidad interior/exterior y **localización** (*locatedness*).

### Proposición 5.1.2 — Existencia del conjunto de todas las cortaduras

Existe un conjunto cuyos elementos son exactamente las cortaduras de Dedekind de $\mathbb Q$.

**Demostración.**

Como $\mathbb Q$ es un conjunto, el axioma del conjunto potencia proporciona $\mathcal P(\mathbb Q)$.

Para $\alpha\in\mathcal P(\mathbb Q)$, sea $\Phi(\alpha)$ la fórmula

$$
\begin{aligned}
\Phi(\alpha)\iff{}&
\alpha\neq\varnothing
\ \land\\
\alpha\neq\mathbb Q\\
&\land\\
\forall r\in\alpha\;\forall s\in\mathbb Q\,(s<r\Rightarrow s\in\alpha)\\
&\land\\
\forall r\in\alpha\;\exists s\in\alpha\,(r<s).
\end{aligned}
$$

Por Separación existe entonces

$$
\mathcal D
:=
\{\alpha\in\mathcal P(\mathbb Q):\Phi(\alpha)\}.
$$

Por construcción, los elementos de $\mathcal D$ son exactamente las cortaduras de Dedekind.

Es importante que la definición se realice dentro del conjunto ambiente $\mathcal P(\mathbb Q)$. No hemos apelado a una colección irrestricta de todos los objetos que satisfacen cierta propiedad. ∎

> **Nota fundacional.** La construcción de $\mathbb R_D$ es extensional y perfectamente determinada en ZF:
> $$
> \mathbb R_D=\{\alpha\in\mathcal P(\mathbb Q):\Phi(\alpha)\}.
> $$
> Pero conjunto potencia + Separación producen la **totalidad clásica** de todas las cortaduras; no proporcionan una codificación finita, una enumeración efectiva ni un procedimiento uniforme para decidir, dada una cortadura arbitraria $\alpha$ y un racional $q$, si $q\in\alpha$.

### Definición 5.1.3 — Conjunto subyacente del modelo de Dedekind

Definimos

$$
\boxed{
\mathbb R_D:=\mathcal D.
}
$$

Equivalentemente,

$$
\mathbb R_D
=
\{\alpha\subseteq\mathbb Q:\alpha\text{ es una cortadura de Dedekind}\}.
$$

Un elemento de $\mathbb R_D$ será llamado **real de Dedekind** o, cuando queramos recordar su representación concreta, simplemente **cortadura**.

Esta terminología no anticipa todavía estructura algebraica ni completitud. En esta etapa sólo hemos construido el conjunto subyacente del modelo.
