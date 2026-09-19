## 10.1. Sucesiones de Cauchy en $\mathbb R_C$ {#sec-ta-10-1}

Como $\mathbb R_C$ es un conjunto, el conjunto de funciones

$$
\mathbb R_C^{\mathbb N}
$$

existe por la construcción general de conjuntos de funciones. Sus elementos serán las sucesiones de reales de Cauchy. Además, Teorema 9.10.3 — $\mathbb R_C$ es un cuerpo ordenado permite aplicar a $\mathbb R_C$ la definición general de valor absoluto de un cuerpo ordenado (Definición 4.2.1 — Valor absoluto).

### Definición 10.1.1 — Sucesión de Cauchy en $\mathbb R_C$

Sea

$$
x=(x_n)_{n\in\mathbb N}\in\mathbb R_C^{\mathbb N}.
$$

Diremos que $x$ es una **sucesión de Cauchy en $\mathbb R_C$** si

$$
\boxed{
\forall\varepsilon\in\mathbb R_C\;
\Bigl(
0_C<_C\varepsilon
\Longrightarrow
\exists N\in\mathbb N\;
\forall m,n\in\mathbb N\;
\bigl(
N\le m\land N\le n
\Longrightarrow
|x_m-x_n|<_C\varepsilon
\bigr)
\Bigr).
}
$$

La definición es enteramente interna al cuerpo ordenado $\mathbb R_C$. En particular, no se ha escogido ninguna sucesión racional representante de ninguno de los términos $x_n$.

Conviene observar también que la tolerancia $\varepsilon$ pertenece aquí a $\mathbb R_C$. Todavía no hemos demostrado completitud ni densidad de la copia racional; por tanto, no sustituiremos esa cuantificación por una cuantificación racional sin una prueba previa.

---

### Lema 10.1.2 — Escalas racionales positivas dentro de toda escala positiva de $\mathbb R_C$

Para todo $\varepsilon\in\mathbb R_C$ con

$$
0_C<_C\varepsilon,
$$

existe $q\in\mathbb Q$ tal que

$$
\boxed{
0<q
\qquad\text{y}\qquad
0_C<_C\iota_C(q)<_C\varepsilon.
}
$$

**Demostración.**

Fijemos $\varepsilon\in\mathbb R_C$ con $0_C<_C\varepsilon$. Por Proposición 9.4.4 — Representantes y criterio de igualdad de clases de Cauchy, existe un representante

$$
a\in\mathcal C_{\mathbb Q}
$$

tal que

$$
\varepsilon=[a]_C.
$$

Esta elección es local: corresponde a un único elemento $\varepsilon$ ya fijado.

Por Definición 9.6.1 — Cero y unidad de Cauchy,

$$
0_C=[\underline{0_{\mathbb Q}}]_C.
$$

Aplicamos Proposición 9.8.6 — Criterio de separación eventual para el orden estricto a

$$
[\underline{0_{\mathbb Q}}]_C
<_C
[a]_C.
$$

Existen entonces $\delta\in\mathbb Q$ y $N\in\mathbb N$ tales que

$$
0<\delta
$$

y, para todo $n\ge N$,

$$
0_{\mathbb Q}+\delta<a_n.
$$

Por la ley del cero,

$$
\delta<a_n
\qquad(n\ge N).
$$

Pongamos

$$
s:=1_{\mathbb Q}+1_{\mathbb Q}
$$

y definamos

$$
q:=\frac{\delta}{s}.
$$

Como $0<1_{\mathbb Q}$, se tiene $0<s$. La positividad del inverso y del producto en el cuerpo ordenado racional implica

$$
0<q.
$$

Además, por las leyes del cuerpo racional y la ley del inverso,

$$
q+q=\delta.
$$

La sucesión constante $\underline q$ pertenece a $\mathcal C_{\mathbb Q}$ por Proposición 8.4.4 — Las sucesiones constantes son de Cauchy. Para todo $n\ge N$ tenemos

$$
\underline q_n+q
=q+q
=\delta
<a_n.
$$

Como $q>0$, otra aplicación de Proposición 9.8.6 — Criterio de separación eventual para el orden estricto produce

$$
[\underline q]_C<_C[a]_C.
$$

Por la definición de $\iota_C$,

$$
[\underline q]_C=\iota_C(q),
$$

y por tanto

$$
\iota_C(q)<_C\varepsilon.
$$

Finalmente, Proposición 9.9.5 — Preservación y reflexión del orden racional preserva el orden estricto racional. Como

$$
0_{\mathbb Q}<q,
$$

se obtiene

$$
\iota_C(0_{\mathbb Q})<_C\iota_C(q).
$$

Por Proposición 9.9.3 — Preservación de la aritmética racional,

$$
\iota_C(0_{\mathbb Q})=0_C.
$$

Luego

$$
0_C<_C\iota_C(q)<_C\varepsilon.
$$

∎

> **Auditoría de elección.** Sólo se toma un representante de un elemento fijo $\varepsilon$ y los testigos $\delta,N$ suministrados por una única instancia de Proposición 9.8.6 — Criterio de separación eventual para el orden estricto. No se selecciona una familia de representantes ni una familia de racionales para todos los $\varepsilon$ simultáneamente.

El lema no afirma todavía que $\iota_C[\mathbb Q]$ sea denso en todo $\mathbb R_C$. Afirma exactamente lo que necesitamos en este punto: los racionales positivos incrustados forman una familia de escalas suficientemente pequeñas alrededor de cero.

---

### Proposición 10.1.3 — Criterio racional para las sucesiones de Cauchy en $\mathbb R_C$

Sea

$$
x=(x_n)_{n\in\mathbb N}\in\mathbb R_C^{\mathbb N}.
$$

Son equivalentes:

1. $x$ es una sucesión de Cauchy en $\mathbb R_C$;
2. para todo $q\in\mathbb Q$ con $0<q$, existe $N\in\mathbb N$ tal que, para todos $m,n\in\mathbb N$,

$$
N\le m\land N\le n
\Longrightarrow
|x_m-x_n|<_C\iota_C(q).
$$

En forma compacta,

$$
\boxed{
x\text{ es de Cauchy en }\mathbb R_C
\iff
\forall q\in\mathbb Q\;
\Bigl(
0<q
\Longrightarrow
\exists N\in\mathbb N\;
\forall m,n\ge N,
\ |x_m-x_n|<_C\iota_C(q)
\Bigr).
}
$$

**Demostración.**

Supongamos primero que $x$ es de Cauchy en $\mathbb R_C$. Sea $q\in\mathbb Q$ con $0<q$. Por Proposición 9.9.5 — Preservación y reflexión del orden racional y Proposición 9.9.3 — Preservación de la aritmética racional,

$$
0_C<_C\iota_C(q).
$$

Aplicando Definición 10.1.1 — Sucesión de Cauchy en $\mathbb R_C$ a la tolerancia

$$
\varepsilon:=\iota_C(q),
$$

obtenemos $N\in\mathbb N$ tal que

$$
N\le m\land N\le n
\Longrightarrow
|x_m-x_n|<_C\iota_C(q).
$$

Esto prueba $2$.

Recíprocamente, supongamos $2$. Sea $\varepsilon\in\mathbb R_C$ con

$$
0_C<_C\varepsilon.
$$

Por Lema 10.1.2 — Escalas racionales positivas dentro de toda escala positiva de $\mathbb R_C$, existe $q\in\mathbb Q$ con

$$
0<q
$$

y

$$
0_C<_C\iota_C(q)<_C\varepsilon.
$$

Aplicando $2$ a este $q$, existe $N\in\mathbb N$ tal que, para $m,n\ge N$,

$$
|x_m-x_n|<_C\iota_C(q).
$$

Por transitividad del orden estricto,

$$
|x_m-x_n|<_C\varepsilon.
$$

Como $\varepsilon>_C0_C$ era arbitraria, Definición 10.1.1 — Sucesión de Cauchy en $\mathbb R_C$ muestra que $x$ es de Cauchy en $\mathbb R_C$.

∎

> **Auditoría de elección.** En la implicación recíproca, para una tolerancia $\varepsilon$ fija se usa un único racional $q$ cuya existencia garantiza Lema 10.1.2 — Escalas racionales positivas dentro de toda escala positiva de $\mathbb R_C$. No se define todavía una función $\varepsilon\mapsto q$ ni se necesita elegir simultáneamente racionales para todas las tolerancias.

La proposición permite trabajar desde ahora con tolerancias racionales positivas sin modificar la noción intrínseca de Cauchy en $\mathbb R_C$. Éste es el puente exacto que necesitaremos para la construcción de aproximantes racionales.

---
