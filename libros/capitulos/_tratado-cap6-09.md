## 6.9. Qué hemos construido {#sec-ta-6-9}

En el Capítulo 5 obtuvimos únicamente una ampliación ordenada. En este capítulo construimos directamente sobre las cortaduras

$$
+_D,
\qquad
-_D,
\qquad
\cdot_D,
\qquad
(\cdot)^{-1_D},
\qquad
\div_D,
\qquad
0_D,
\qquad
1_D,
$$

y demostramos

$$
\boxed{(\mathbb R_D,+_D,\cdot_D,\le_D)\text{ es un cuerpo ordenado}.}
$$

La aplicación canónica es ahora, en sentido pleno,

$$
\boxed{\iota_D:\mathbb Q\hookrightarrow\mathbb R_D}
$$

como incrustación de cuerpos ordenados, y satisface

$$
\begin{aligned}
\iota_D(p+q)&=\iota_D(p)+_D\iota_D(q),\\
\iota_D(p-q)&=\iota_D(p)-_D\iota_D(q),\\
\iota_D(pq)&=\iota_D(p)\cdot_D\iota_D(q),\\
\iota_D(p^{-1})&=\iota_D(p)^{-1_D}\qquad(p\neq0),\\
\iota_D(p/q)&=\iota_D(p)\div_D\iota_D(q)\qquad(q\neq0),\\
\iota_D(0_{\mathbb Q})&=0_D,\\
\iota_D(1_{\mathbb Q})&=1_D.
\end{aligned}
$$

Hasta este punto no hemos utilizado completitud de $\mathbb R_D$; todavía no ha sido demostrada. La propiedad que motivó la construcción será el objeto del capítulo siguiente.

Si $\mathcal A\subseteq\mathbb R_D$ es no vacía y está acotada superiormente, el candidato natural a supremo es

$$
\boxed{\bigcup\mathcal A.}
$$

Habrá que demostrar que esta unión es una cortadura, que contiene a cada miembro de $\mathcal A$ y que está contenida en toda cota superior. Sólo entonces podremos concluir que $\mathbb R_D$ es un cuerpo ordenado completo.
