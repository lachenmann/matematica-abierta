## 5.5. La copia racional en el modelo de Dedekind {#sec-ta-5-5}

Ya sabemos que cada racional $q\in\mathbb Q$ determina una cortadura $\delta_q$, y que $\mathbb R_D$ posee un orden total por inclusión. Ha llegado el momento de unir ambas construcciones.

La idea es sencilla:

$$
q\longmapsto\delta_q.
$$

Pero no basta con una flecha informal. Debemos construir una función con dominio, codominio y grafo determinados, y después demostrar qué estructura conserva.

### Definición 5.5.1 — Aplicación canónica de $\mathbb Q$ en $\mathbb R_D$

Consideremos el subconjunto

$$
G_D\subseteq\mathbb Q\times\mathbb R_D
$$

definido por

$$
\boxed{
G_D
:=
\{\langle q,\alpha\rangle\in\mathbb Q\times\mathbb R_D:\alpha=\delta_q\}.
}
$$

Este conjunto existe por Separación, una vez construido el producto cartesiano $\mathbb Q\times\mathbb R_D$.

Para cada $q\in\mathbb Q$, Proposición 5.2.2 — Toda sección racional es una cortadura garantiza que $\delta_q\in\mathbb R_D$, de modo que existe al menos un $\alpha\in\mathbb R_D$ con

$$
\langle q,\alpha\rangle\in G_D.
$$

Ese valor es único: si

$$
\langle q,\alpha\rangle\in G_D
\qquad\text{y}\qquad
\langle q,\beta\rangle\in G_D,
$$

entonces

$$
\alpha=\delta_q=\beta.
$$

Por tanto $G_D$ es el grafo de una función con dominio $\mathbb Q$ y codominio $\mathbb R_D$.

Definimos la **aplicación canónica de Dedekind**

$$
\boxed{
\iota_D:\mathbb Q\longrightarrow\mathbb R_D
}
$$

mediante

$$
\boxed{
\iota_D(q):=\delta_q.
}
$$

No hemos utilizado el axioma de elección: para cada $q$, el valor $\delta_q$ está determinado de manera única por una fórmula.

Tampoco estamos identificando $q$ con $\delta_q$. Tenemos

$$
q\in\mathbb Q,
$$

mientras que

$$
\iota_D(q)=\delta_q\in\mathbb R_D.
$$

La relación entre ambos sistemas está mediada por $\iota_D$.

### Proposición 5.5.2 — Caracterización del orden mediante la aplicación canónica

Para cualesquiera $p,q\in\mathbb Q$,

$$
\boxed{
p\leq_{\mathbb Q}q
\quad\Longleftrightarrow\quad
\iota_D(p)\leq_D\iota_D(q).
}
$$

Equivalentemente,

$$
\boxed{
p\leq_{\mathbb Q}q
\quad\Longleftrightarrow\quad
\delta_p\subseteq\delta_q.
}
$$

**Demostración.**

Supongamos $p\leq q$. Si $r\in\delta_p$, entonces $r<p\leq q$ y, por transitividad entre $<$ y $\leq$,

$$
r<q.
$$

Así $r\in\delta_q$, luego $\delta_p\subseteq\delta_q$.

Recíprocamente, supongamos $\delta_p\subseteq\delta_q$. La comparación racional decidible Proposición 3.7.6 — Tricotomía decidible de los racionales da $q<p$ o $p\leq q$. Si ocurriera $q<p$, entonces

$$
q\in\delta_p
\qquad\text{pero}\qquad
q\notin\delta_q,
$$

contradiciendo la inclusión. Por tanto $p\leq q$.

Así,

$$
\boxed{
p\leq_{\mathbb Q}q
\iff
\iota_D(p)\leq_D\iota_D(q).
}
$$

∎

La recíproca utiliza únicamente la comparación **decidible de los racionales**, no la totalidad clásica de las cortaduras.

### Corolario 5.5.3 — $\iota_D$ es inyectiva y preserva y refleja el orden estricto

La función

$$
\iota_D:\mathbb Q\to\mathbb R_D
$$

es inyectiva. Además, para cualesquiera $p,q\in\mathbb Q$,

$$
\boxed{
p<_{\mathbb Q}q
\quad\Longleftrightarrow\quad
\iota_D(p)<_D\iota_D(q).
}
$$

**Demostración.**

Supongamos primero

$$
\iota_D(p)=\iota_D(q).
$$

Entonces

$$
\iota_D(p)\leq_D\iota_D(q)
\qquad\text{y}\qquad
\iota_D(q)\leq_D\iota_D(p).
$$

Por Proposición 5.5.2 — Caracterización del orden mediante la aplicación canónica,

$$
p\leq q
\qquad\text{y}\qquad
q\leq p.
$$

La antisimetría del orden racional da $p=q$. Luego $\iota_D$ es inyectiva.

Ahora, si $p<q$, entonces $p\leq q$ y $p\neq q$. Por Proposición 5.5.2 — Caracterización del orden mediante la aplicación canónica,

$$
\iota_D(p)\leq_D\iota_D(q),
$$

y por inyectividad

$$
\iota_D(p)\neq\iota_D(q).
$$

Por tanto

$$
\iota_D(p)<_D\iota_D(q).
$$

Recíprocamente, si

$$
\iota_D(p)<_D\iota_D(q),
$$

entonces $\iota_D(p)\leq_D\iota_D(q)$ y $\iota_D(p)\neq\iota_D(q)$. La primera condición da $p\leq q$ por Proposición 5.5.2 — Caracterización del orden mediante la aplicación canónica; la segunda implica $p\neq q$. Por definición del orden estricto asociado,

$$
p<q.
$$

∎

Sólo ahora podemos llamar rigurosamente a $\iota_D$ una **incrustación de órdenes**. No es todavía una incrustación de cuerpos ordenados, porque aún no hemos construido suma ni producto sobre $\mathbb R_D$.

### Corolario 5.5.4 — La copia racional no agota $\mathbb R_D$

La aplicación

$$
\iota_D:\mathbb Q\to\mathbb R_D
$$

no es sobreyectiva. En particular,

$$
\boxed{
\iota_D[\mathbb Q]\subsetneq\mathbb R_D.
}
$$

**Demostración.**

Por Proposición 5.3.2 — $\alpha_2$ es una cortadura de Dedekind,

$$
\alpha_2\in\mathbb R_D.
$$

Si $\iota_D$ fuera sobreyectiva, existiría $q\in\mathbb Q$ tal que

$$
\iota_D(q)=\alpha_2.
$$

Pero $\iota_D(q)=\delta_q$, de modo que

$$
\alpha_2=\delta_q,
$$

contradiciendo Proposición 5.3.3 — $\alpha_2$ no es una cortadura racional.

Luego $\iota_D$ no es sobreyectiva. Como $\iota_D[\mathbb Q]\subseteq\mathbb R_D$ y $\alpha_2$ pertenece al segundo conjunto pero no al primero,

$$
\boxed{
\iota_D[\mathbb Q]\subsetneq\mathbb R_D.
}
$$

∎

Ésta es la forma rigurosa en que la construcción de Dedekind amplía el sistema racional. La afirmación correcta no es una identidad conjuntista $\mathbb Q\subsetneq\mathbb R_D$, sino la existencia de una incrustación ordenada cuya imagen es un subconjunto propio de $\mathbb R_D$.
