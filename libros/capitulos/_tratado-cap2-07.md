## 2.7. Incrustación canónica de $\mathbb N$ {#sec-ta-2-7}

Hasta ahora $\mathbb N$ y $\mathbb Z$ son conjuntos distintos. Para demostrar que los enteros extienden realmente a los naturales debemos construir una función que preserve su aritmética.

### Definición 2.7.1 — Incrustación natural en los enteros {#ta-incrustacion-naturales-enteros}

*Glosario: [incrustación canónica](../otros/tratado-de-analisis-glosario.md#gl-incrustacion-canonica)*

Definimos

$$
\iota_{\mathbb N}^{\mathbb Z}:\mathbb N\to\mathbb Z
$$

por

$$
\boxed{
\iota_{\mathbb N}^{\mathbb Z}(n):=[(n,0)].
}
$$

Abreviaremos $\iota_{\mathbb N}^{\mathbb Z}$ a $\iota$ cuando no haya ambigüedad.

### Proposición 2.7.2 — La incrustación es inyectiva y preserva la aritmética {#ta-incrustacion-preserva-aritmetica}

Para $m,n\in\mathbb N$:

1. $\iota$ es inyectiva;
2. $\iota(0)=0_{\mathbb Z}$;
3. $\iota(1)=1_{\mathbb Z}$;
4. $\iota(m+n)=\iota(m)+\iota(n)$;
5. $\iota(mn)=\iota(m)\iota(n)$.

**Demostración.**  
Si

$$
\iota(m)=\iota(n),
$$

entonces

$$
[(m,0)]=[(n,0)].
$$

Por el criterio de igualdad de clases enteras,

$$
m+0=0+n,
$$

y por las leyes de la suma natural,

$$
m=n.
$$

Así $\iota$ es inyectiva.

Además,

$$
\iota(0)=[(0,0)]=0_{\mathbb Z},
$$

$$
\iota(1)=[(1,0)]=1_{\mathbb Z}.
$$

Para la suma,

$$
\iota(m)+\iota(n)
=
[(m,0)]+[(n,0)]
=
[(m+n,0)]
=
\iota(m+n).
$$

Para el producto,

$$
\iota(m)\iota(n)
=
[(m,0)][(n,0)]
=
[(mn+0,\;0+0)]
=
[(mn,0)]
=
\iota(mn).
$$

∎

Hemos demostrado ahora, y no antes, que la aritmética natural se reproduce fielmente dentro de $\mathbb Z$. Todavía no escribiremos literalmente

$$
\mathbb N\subseteq\mathbb Z.
$$

La relación canónica entre ambos sistemas es la función inyectiva $\iota$.

---

::: {.callout-note title="Publicación progresiva"}
Con §2.7 queda construida la incrustación canónica $\iota_{\mathbb N}^{\mathbb Z}$ y demostrado que preserva $0$, $1$, suma y producto. La siguiente entrega será **§2.8 — Forma normal con signo y ausencia de divisores de cero**.
:::
