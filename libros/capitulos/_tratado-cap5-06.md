## 5.6. Qué hemos construido {#sec-ta-5-6}

Podemos ahora precisar exactamente qué se ha obtenido y, con igual importancia, qué falta todavía por construir.

Partimos únicamente del cuerpo ordenado racional y consideramos ciertos subconjuntos de $\mathbb Q$: los lados inferiores no vacíos, propios, cerrados hacia abajo y sin elemento máximo.

El conjunto de todos ellos fue definido como

$$
\boxed{
\mathbb R_D
=
\{\alpha\subseteq\mathbb Q:\alpha\text{ es una cortadura de Dedekind}\}.
}
$$

Su existencia se obtuvo enteramente dentro de ZF mediante conjunto potencia y Separación. No fue necesario escoger representantes ni utilizar el axioma de elección.

Después vimos que cada racional $q$ determina una cortadura

$$
\delta_q=\{r\in\mathbb Q:r<q\}.
$$

Las cortaduras racionales no agotan el nuevo conjunto. A partir de $S_2$ construimos

$$
\alpha_2\in\mathbb R_D
$$

y demostramos

$$
\forall q\in\mathbb Q,
\qquad
\alpha_2\neq\delta_q.
$$

Ordenamos luego las cortaduras mediante inclusión:

$$
\boxed{
\alpha\leq_D\beta
\iff
\alpha\subseteq\beta.
}
$$

La clausura inferior y la totalidad del orden racional fuerzan que este orden sea total.

Finalmente construimos

$$
\iota_D:\mathbb Q\longrightarrow\mathbb R_D,
\qquad
\iota_D(q)=\delta_q,
$$

y demostramos que preserva y refleja el orden:

$$
\boxed{
p\leq_{\mathbb Q}q
\iff
\iota_D(p)\leq_D\iota_D(q).
}
$$

En particular, $\iota_D$ es inyectiva y

$$
p<_{\mathbb Q}q
\iff
\iota_D(p)<_D\iota_D(q).
$$

Además,

$$
\boxed{
\iota_D[\mathbb Q]\subsetneq\mathbb R_D.
}
$$

Hasta este punto hemos obtenido una extensión **ordenada** de $\mathbb Q$:

$$
\boxed{
(\mathbb Q,\leq_{\mathbb Q})
\hookrightarrow
(\mathbb R_D,\leq_D).
}
$$

Todavía no hemos construido sobre $\mathbb R_D$ el cero, el uno, la suma, los opuestos, el producto ni los inversos. Por ello no podemos afirmar que $\mathbb R_D$ sea un cuerpo ordenado.

Tampoco hemos demostrado todavía la propiedad del supremo. En consecuencia, no podemos afirmar aún que $\mathbb R_D$ sea completo.

La construcción del número real de Dedekind continúa.
