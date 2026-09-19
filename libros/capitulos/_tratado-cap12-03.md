## 12.3. Densidad de la copia racional canónica {#sec-ta-12-3}

La sección anterior identificó de manera exacta la relación entre el subcuerpo primo de un cuerpo ordenado y el sistema racional ya construido:

$$
\jmath_{\mathbb Q}^{F}[\mathbb Q]=P_F.
$$

Por otra parte, el Capítulo 4 ya demostró un hecho de orden independiente de toda construcción concreta de los reales: si $F$ es arquimediano, entonces $P_F$ es denso en $F$. No debemos repetir aquí aquella demostración. Lo que faltaba entonces era saber que los elementos de $P_F$ son precisamente las imágenes de racionales bajo una aplicación canónica y única.

La densidad racional puede ahora formularse en el lenguaje que necesitaremos para comparar completaciones.

### Teorema 12.3.1 — Densidad de la copia racional canónica en un cuerpo arquimediano

Sea $F$ un cuerpo ordenado arquimediano. Para cualesquiera $x,y\in F$ con

$$
x<y,
$$

existe $q\in\mathbb Q$ tal que

$$
\boxed{
x<\jmath_{\mathbb Q}^{F}(q)<y.
}
$$

Equivalente y más concisamente, la imagen

$$
\jmath_{\mathbb Q}^{F}[\mathbb Q]
$$

es densa en $F$.

**Demostración.**

Como $F$ es arquimediano, Teorema 4.5.1 — Densidad del subcuerpo primo en un cuerpo arquimediano proporciona un elemento

$$
r\in P_F
$$

tal que

$$
x<r<y.
$$

Pero Corolario 12.2.7 — La copia racional es exactamente el subcuerpo primo establece

$$
P_F=\jmath_{\mathbb Q}^{F}[\mathbb Q].
$$

Por tanto

$$
r\in\jmath_{\mathbb Q}^{F}[\mathbb Q].
$$

Por la definición de imagen directa, existe $q\in\mathbb Q$ tal que

$$
r=\jmath_{\mathbb Q}^{F}(q).
$$

Sustituyendo en la desigualdad anterior obtenemos

$$
x<\jmath_{\mathbb Q}^{F}(q)<y,
$$

como se quería. ∎

> **Auditoría de elección.** El argumento utiliza únicamente el testigo existencial $r$ suministrado por la densidad de $P_F$ y, para ese $r$ fijo, el testigo $q$ contenido en la afirmación $r\in\jmath_{\mathbb Q}^{F}[\mathbb Q]$. No se define una elección simultánea de racionales para todos los intervalos de $F$.

> **Nota fundacional.** La dependencia clásica está heredada de Teorema 4.5.1 — Densidad del subcuerpo primo en un cuerpo arquimediano, cuya prueba localiza un mínimo en un subconjunto arbitrario de $\mathbb N$. La extracción posterior de un racional para este intervalo fijo es local y no constituye Choice.

---

### Corolario 12.3.2 — Densidad racional en todo cuerpo ordenado completo

Sea $F$ un cuerpo ordenado completo. Entonces, para todos $x,y\in F$ con $x<y$, existe $q\in\mathbb Q$ tal que

$$
\boxed{
x<\jmath_{\mathbb Q}^{F}(q)<y.
}
$$

**Demostración.**

Por Teorema 4.6.3 — Todo cuerpo ordenado completo es arquimediano, todo cuerpo ordenado completo es arquimediano. Aplicamos entonces Teorema 12.3.1 — Densidad de la copia racional canónica en un cuerpo arquimediano. ∎

La conclusión contiene exactamente la densidad que utilizaremos a partir de ahora. Si $(E,\iota_E)$ es una completación ordenada de $\mathbb Q$, Corolario 12.2.9 — La copia racional de toda completación es la copia canónica ya demostró

$$
\iota_E=\jmath_{\mathbb Q}^{E}.
$$

Así, Corolario 12.3.2 — Densidad racional en todo cuerpo ordenado completo puede escribirse en la forma familiar

$$
x<y
\Longrightarrow
\exists q\in\mathbb Q\;
\bigl(x<\iota_E(q)<y\bigr),
$$

que coincide con la densidad de la imagen racional probada anteriormente en Proposición 4.8.3 — La imagen racional de una completación es densa, pero ahora sabemos además que la incrustación que aparece allí no es un dato arbitrario: es la única copia racional posible en $E$.

Este punto es decisivo para la siguiente construcción. Dado $x\in E$, podremos considerar el conjunto de todos los racionales cuya imagen canónica queda estrictamente por debajo de $x$. La densidad recién establecida garantizará que ese conjunto codifica con suficiente precisión la posición de $x$ dentro del orden. Ése será el punto de partida de §12.4.

---
