## 3.10. Qué hemos construido {#sec-ta-3-10}

Partimos del conjunto de representantes

$$
D_{\mathbb Q}
=
\mathbb Z\times\mathbb Z_{\neq0}
$$

y de la equivalencia

$$
(a,b)\sim_{\mathbb Q}(c,d)
\iff
ad=bc.
$$

El cociente

$$
\boxed{
\mathbb Q
=
D_{\mathbb Q}/{\sim_{\mathbb Q}}
}
$$

admite la notación legítima

$$
\frac ab=[(a,b)]_{\mathbb Q}.
$$

Las operaciones son

$$
\frac ab+\frac cd
=
\frac{ad+bc}{bd},
$$

$$
-\frac ab
=
\frac{-a}{b},
$$

$$
\frac ab\frac cd
=
\frac{ac}{bd},
$$

y, para $a\neq0$,

$$
\left(\frac ab\right)^{-1}
=
\frac ba.
$$

Se ha demostrado que $\mathbb Q$ es un cuerpo. La incrustación

$$
\jmath_{\mathbb Z}^{\mathbb Q}(a)=\frac a1
$$

es inyectiva y preserva $0$, $1$, suma, producto, opuesto y orden. La composición

$$
\nu_{\mathbb N}^{\mathbb Q}
=
\jmath_{\mathbb Z}^{\mathbb Q}
\circ
\iota_{\mathbb N}^{\mathbb Z}
$$

incorpora de manera canónica la aritmética natural.

El orden racional se reconoce, para denominadores positivos, mediante

$$
\frac ab\leq_{\mathbb Q}\frac cd
\iff
ad\leq_{\mathbb Z}bc.
$$

Es un orden total compatible con las operaciones. Además:

$$
x<y
\Longrightarrow
\exists z\in\mathbb Q\;(x<z<y),
$$

y para todo $q\in\mathbb Q$ existe $n\in\mathbb N$ con

$$
q<\nu(n).
$$

Sin embargo, el conjunto

$$
S_2
=
\{q\in\mathbb Q:0\leq q,\ q^2<2\}
$$

es no vacío y acotado superiormente, pero no posee supremo en $\mathbb Q$.

Ésta es la primera aparición formal del problema de la **completitud**.

---
