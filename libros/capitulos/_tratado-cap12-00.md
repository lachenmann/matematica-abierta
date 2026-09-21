## 12.0. De dos modelos concretos a la unicidad general {#sec-ta-12-0}

El capítulo anterior terminó con un isomorfismo explícito

$$
\Phi:\mathbb R_C\longrightarrow\mathbb R_D
$$

que preserva las operaciones y el orden y satisface

$$
\Phi\circ\iota_C=\iota_D.
$$

Ese resultado resuelve la comparación entre dos construcciones concretas. Queda, sin embargo, una cuestión más fuerte. Si

$$
(E,\iota_E)
\qquad\text{y}\qquad
(F,\iota_F)
$$

son dos completaciones ordenadas de $\mathbb Q$ en el sentido de Definición 4.8.2 — Completación ordenada de $\mathbb Q$, ¿existe necesariamente un isomorfismo de cuerpos ordenados

$$
T:E\longrightarrow F
$$

que haga conmutar las copias racionales,

$$
T\circ\iota_E=\iota_F,
$$

y, en caso afirmativo, está determinado de manera única?

La demostración no debe depender de que los elementos de $E$ sean cortaduras, clases de Cauchy o cualquier otra codificación. Debe utilizar únicamente la estructura abstracta ya aislada: cuerpo ordenado, completitud y copia racional.

La arquitectura del argumento será

$$
\text{subcuerpo primo}
\longrightarrow
\text{copia canónica de }\mathbb Q
\longrightarrow
\text{densidad racional}
\longrightarrow
\text{cortes racionales}
\longrightarrow
\text{isomorfismo}
\longrightarrow
\text{unicidad}.
$$

Hay una primera precaución. El subcuerpo primo no se redefinirá aquí. Ya fue construido en Definición 4.1.8 — Subcuerpo primo como

$$
P_F=\bigcap\{K\subseteq F:K\text{ es subcuerpo de }F\},
$$

Proposición 4.1.9 — Minimalidad del subcuerpo primo probó su minimalidad y Corolario 4.1.10 — Los numerales naturales pertenecen al subcuerpo primo demostró que contiene todos los numerales $\nu_F(n)$. La tarea de §12.1 es completar la parte que entonces no necesitábamos: identificar dentro de un cuerpo ordenado la copia canónica de los enteros generada por esos numerales. Sólo después podremos pasar, mediante inversos, a la copia canónica de $\mathbb Q$.
