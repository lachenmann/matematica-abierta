## 8.5. Toda sucesión convergente es de Cauchy {#sec-ta-8-5}

La convergencia racional y la condición de Cauchy expresan dos formas distintas de control asintótico. En la primera, los términos tardíos se comparan con un racional fijo $\ell$; en la segunda, se comparan entre sí.

La relación entre ambas nociones debe demostrarse. Si todos los términos suficientemente tardíos están muy próximos a un mismo racional, entonces dos cualesquiera de esos términos deberán estar próximos entre sí. La desigualdad triangular convierte esta intuición en una estimación precisa.

El único cuidado cuantitativo consiste en no gastar toda la tolerancia $\varepsilon$ en cada uno de los dos tramos

$$
q_m\longrightarrow \ell
\qquad\text{y}\qquad
\ell\longrightarrow q_n.
$$

Por ello aplicaremos la convergencia con la mitad racional de la precisión requerida.

### Teorema 8.5.1 — Toda sucesión racionalmente convergente es de Cauchy

Sea $q=(q_n)_{n\in\mathbb N}$ una sucesión racional y sea $\ell\in\mathbb Q$. Si

$$
q_n\to_{\mathbb Q}\ell,
$$

entonces $q$ es de Cauchy. Equivalentemente,

$$
\boxed{
q_n\to_{\mathbb Q}\ell
\Longrightarrow
q\in\mathcal C_{\mathbb Q}.
}
$$

**Demostración.**

Supongamos

$$
q_n\to_{\mathbb Q}\ell.
$$

Sea $\varepsilon\in\mathbb Q$ con

$$
0<\varepsilon.
$$

Debemos encontrar un índice $N\in\mathbb N$ a partir del cual cualesquiera dos términos de la sucesión estén a distancia menor que $\varepsilon$.

Trabajaremos enteramente dentro de $\mathbb Q$. Pongamos

$$
s:=1_{\mathbb Q}+1_{\mathbb Q}.
$$

Como $\mathbb Q$ es un cuerpo ordenado, Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado (3) da

$$
0<1_{\mathbb Q}.
$$

Sumando $1_{\mathbb Q}$ a la desigualdad anterior mediante Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado (8),

$$
1_{\mathbb Q}<s.
$$

Por transitividad,

$$
0<s.
$$

En particular $s\neq0$, de modo que está definida la división por $s$. Definamos

$$
\eta:=\frac{\varepsilon}{s}.
$$

La positividad del inverso y del producto en un cuerpo ordenado (Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado (5),(6)) implica

$$
0<\eta.
$$

Además, por la definición de división y la ley del inverso Proposición 3.6.5 — Ley del inverso multiplicativo,

$$
\begin{aligned}
\eta+\eta
&=\varepsilon s^{-1}+\varepsilon s^{-1}\\
&=\varepsilon(1_{\mathbb Q}+1_{\mathbb Q})s^{-1}\\
&=\varepsilon ss^{-1}\\
&=\varepsilon.
\end{aligned}
$$

Así, $\eta$ es precisamente la mitad racional de la tolerancia $\varepsilon$.

Aplicamos ahora la convergencia de $q$ a la precisión racional positiva $\eta$. Por Definición 8.3.1 — Convergencia racional, existe $N\in\mathbb N$ tal que, para todo $k\in\mathbb N$,

$$
N\leq k
\Longrightarrow
d_{\mathbb Q}(q_k,\ell)<\eta.
$$

Sean $m,n\in\mathbb N$ con

$$
N\leq m,
\qquad
N\leq n.
$$

Entonces

$$
d_{\mathbb Q}(q_m,\ell)<\eta
$$

y

$$
d_{\mathbb Q}(q_n,\ell)<\eta.
$$

Por simetría de la distancia racional,

$$
d_{\mathbb Q}(\ell,q_n)
=
d_{\mathbb Q}(q_n,\ell)
<
\eta.
$$

La desigualdad triangular de Proposición 8.2.2 — Propiedades fundamentales de la distancia racional da

$$
d_{\mathbb Q}(q_m,q_n)
\leq
d_{\mathbb Q}(q_m,\ell)
+
d_{\mathbb Q}(\ell,q_n).
$$

Como ambos sumandos del miembro derecho son estrictamente menores que $\eta$, la compatibilidad del orden con la suma produce

$$
d_{\mathbb Q}(q_m,\ell)
+
d_{\mathbb Q}(\ell,q_n)
<
\eta+\eta
=
\varepsilon.
$$

Por transitividad,

$$
d_{\mathbb Q}(q_m,q_n)<\varepsilon.
$$

Hemos probado que para la precisión racional positiva arbitraria $\varepsilon$ existe $N\in\mathbb N$ tal que todos los índices $m,n\geq N$ satisfacen la condición requerida. Por Definición 8.4.1 — Sucesión racional de Cauchy, $q$ es de Cauchy; por Definición 8.4.2 — Conjunto de las sucesiones racionales de Cauchy,

$$
q\in\mathcal C_{\mathbb Q}.
$$

Esto demuestra la afirmación. ∎

> **Contenido efectivo.** Si la convergencia viene acompañada de un módulo $\mu$, la prueba produce
> explícitamente un módulo de Cauchy:
> $$ \boxed{\mu_C(\varepsilon)=\mu(\varepsilon/2_{\mathbb Q}).} $$
> Por tanto un módulo computable de convergencia induce un módulo computable de Cauchy.
>
> **Auditoría de elección.** Para una precisión racional positiva arbitraria $\varepsilon$ construimos canónicamente $\eta=\varepsilon/s$ y extraemos de la hipótesis de convergencia un único testigo $N$ para esa precisión. No se selecciona simultáneamente una familia de índices y no interviene el axioma de elección.

---

### Lo que hemos ganado

La convergencia racional implica necesariamente estabilización interna:

$$
\boxed{
q_n\to_{\mathbb Q}\ell
\Longrightarrow
q\in\mathcal C_{\mathbb Q}.
}
$$

Por tanto, la condición de Cauchy es una **condición necesaria** para que una sucesión racional posea un límite racional.

La recíproca no ha sido demostrada y no debe suponerse. Precisamente porque la definición de Cauchy no menciona un límite, puede detectar procesos racionales coherentes cuya eventual “posición” todavía no sabemos representar dentro de $\mathbb Q$.

Antes de exhibir esa insuficiencia secuencial debemos establecer una propiedad estructural básica de estos procesos: **toda sucesión racional de Cauchy es acotada**. Ése será el contenido de §8.6.

---
