## 24.0. De las series de funciones a las series de potencias {#sec-ta-24-0}

Una serie de funciones, tal como fue construida en el Capítulo 23, comienza con una sucesión de funciones reales sobre un dominio común. Sus sumas parciales constituyen otra sucesión de funciones; la convergencia puntual o uniforme no se deduce de que cada suma finita esté bien definida. En este capítulo examinaremos una familia especial, determinada por un centro real $c$ y por una sucesión real fija $(a_n)_{n\in\mathbb N}$:

$$
\sum_{n=0}^{\infty}a_n(x-c)^n.
\tag{24.0.1}
$$

La forma algebraica de sus términos impone relaciones entre las evaluaciones en puntos distintos. En efecto, si $y\ne c$, la expresión $x-c$ puede compararse con $y-c$ mediante el cociente $(x-c)/(y-c)$; elevarlo a una potencia natural producirá un factor geométrico. Esta relación no existe para una sucesión arbitraria de funciones y será el fundamento del comportamiento espacial de la convergencia.

El primer problema no consiste en sumar (24.0.1) para todo real ni en asignarle anticipadamente una función global. Consiste en determinar en qué puntos converge la sucesión numérica de sus sumas parciales. Sólo una vez construido ese conjunto podremos hablar de su función suma con dominio exacto y, después de demostrar propiedades adicionales, de un radio de convergencia y de operaciones término a término. Ni el criterio $M$ de Weierstrass ni los teoremas de intercambio del capítulo precedente autorizan esas operaciones sin verificar sus hipótesis.

Conservaremos los índices naturales desde $0$: la suma parcial de índice $N$ contiene exactamente los términos $0,\ldots,N$. Las potencias son las construidas por recursión en «Potencias naturales de un número real», incluida la convención $r^0=1$ para todo $r\in\mathbb R$ y, en particular, $0^0=1$. Todas las funciones introducidas a continuación se consideran con dominio y codominio expresos.

---
