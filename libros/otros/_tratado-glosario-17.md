## Incrustación canónica {#gl-incrustacion-canonica}

**Idea.** Una aplicación inyectiva que permite reconocer una estructura ya construida dentro de otra más amplia sin identificar inicialmente sus elementos como objetos literalmente iguales.

**En este tratado.** La incrustación canónica de los naturales en los enteros es

$$
\boxed{
\iota_{\mathbb N}^{\mathbb Z}:\mathbb N\to\mathbb Z,
\qquad
\iota_{\mathbb N}^{\mathbb Z}(n)=[(n,0)].
}
$$

La aplicación es inyectiva y preserva los elementos $0$ y $1$, además de la suma y el producto:

$$
\iota(0)=0_{\mathbb Z},
\qquad
\iota(1)=1_{\mathbb Z},
$$

$$
\iota(m+n)=\iota(m)+\iota(n),
\qquad
\iota(mn)=\iota(m)\iota(n).
$$

Una vez construido el orden entero, también preserva y refleja el orden:

$$
m\leq n
\iff
\iota(m)\leq_{\mathbb Z}\iota(n).
$$

Esto expresa que la aritmética natural se reproduce fielmente dentro de $\mathbb Z$. En este punto no se identifica literalmente $\mathbb N$ con un subconjunto de $\mathbb Z$; la relación entre ambos sistemas queda mediada por $\iota$.

**En el Tratado:** [Definición 2.7.1 — Incrustación natural en los enteros](../capitulos/tratado-de-analisis-capitulo-2-los-numeros-enteros.md#ta-incrustacion-naturales-enteros), [Proposición 2.7.2 — La incrustación es inyectiva y preserva la aritmética](../capitulos/tratado-de-analisis-capitulo-2-los-numeros-enteros.md#ta-incrustacion-preserva-aritmetica) y [Proposición 2.9.5 — La incrustación preserva y refleja el orden](../capitulos/tratado-de-analisis-capitulo-2-los-numeros-enteros.md#ta-incrustacion-preserva-orden).

**Véase también:** [Inyectividad](#gl-inyectividad), [Número entero](#gl-numero-entero), [Números naturales](#gl-numeros-naturales), [Orden entero](#gl-orden-entero).

---
