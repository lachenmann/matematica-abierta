## 2.10. Qué hemos construido {#sec-ta-2-10}

La construcción partió únicamente de $\mathbb N$, sus operaciones y la infraestructura conjuntista del Capítulo 0. El objeto obtenido es

$$
\boxed{
\mathbb Z=(\mathbb N\times\mathbb N)/{\sim_{\mathbb Z}},
}
$$

donde

$$
(a,b)\sim_{\mathbb Z}(c,d)
\iff
a+d=b+c.
$$

Sobre este cociente hemos definido

$$
[(a,b)]+[(c,d)]=[(a+c,b+d)],
$$

$$
-[(a,b)]=[(b,a)],
$$

$$
[(a,b)][(c,d)]
=
[(ac+bd,ad+bc)].
$$

La sustracción se define por

$$
x-y=x+(-y),
$$

y toda ecuación

$$
x+y=z
$$

posee una única solución.

La función canónica

$$
\iota_{\mathbb N}^{\mathbb Z}(n)=[(n,0)]
$$

es inyectiva y satisface

$$
\iota(0)=0_{\mathbb Z},
\qquad
\iota(1)=1_{\mathbb Z},
$$

$$
\iota(m+n)=\iota(m)+\iota(n),
$$

$$
\iota(mn)=\iota(m)\iota(n).
$$

El orden entero está definido por

$$
x\leq_{\mathbb Z}y
\iff
\exists n\in\mathbb N\;
\bigl(y=x+\iota(n)\bigr),
$$

y puede reconocerse sobre representantes mediante

$$
[(a,b)]\leq_{\mathbb Z}[(c,d)]
\iff
a+d\leq c+b.
$$

Además,

$$
m\leq n
\iff
\iota(m)\leq_{\mathbb Z}\iota(n).
$$

En consecuencia, $\mathbb Z$ es un dominio de integridad totalmente ordenado y la incrustación $\iota$ preserva la estructura aritmética construida en $\mathbb N$.

Conviene subrayar lo que **no** hemos hecho. No hemos declarado que

$$
\mathbb N\subseteq\mathbb Z.
$$

Los dos sistemas siguen siendo, conjuntísticamente, objetos diferentes. Lo que hemos construido es una incrustación canónica que justifica una futura convención de identificación con la imagen cuando esa convención resulte útil y sea declarada explícitamente.

---

::: {.callout-note title="Publicación progresiva"}
Con §2.10 queda reunida en una sola síntesis la construcción completa de $\mathbb Z$ alcanzada hasta aquí. La siguiente entrega será **§2.11 — Por qué la construcción funciona**, donde se explicará el patrón metodológico de representantes, equivalencia, cociente y buena definición que volverá a utilizarse en la construcción de $\mathbb Q$.
:::
