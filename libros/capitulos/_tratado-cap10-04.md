## 10.4. Convergencia y completitud secuencial {#sec-ta-10-4}

La construcción diagonal de §10.3 ha producido, para cada sucesión de Cauchy

$$
x=(x_n)_{n\in\mathbb N}
$$

en $\mathbb R_C$, una sucesión racional de Cauchy

$$
q=\operatorname{diag}_C(x)
$$

y, por tanto, una clase legítima

$$
[q]_C\in\mathbb R_C.
$$

Falta demostrar que esa clase realiza efectivamente la aproximación que motivó su construcción. Antes de hacerlo debemos formular la convergencia en $\mathbb R_C$ sin apelar a ningún modelo externo de los reales.

---

### Definición 10.4.1 — Convergencia en $\mathbb R_C$

Sean

$$
x=(x_n)_{n\in\mathbb N}\in\mathbb R_C^{\mathbb N}
$$

y $L\in\mathbb R_C$. Diremos que $x$ **converge a $L$ en $\mathbb R_C$** si

$$
\boxed{
\forall\varepsilon\in\mathbb R_C\;
\Bigl(
0_C<_C\varepsilon
\Longrightarrow
\exists N\in\mathbb N\;
\forall n\in\mathbb N\;
\bigl(
N\le n
\Longrightarrow
|x_n-L|<_C\varepsilon
\bigr)
\Bigr).
}
$$

La definición utiliza únicamente la estructura de cuerpo ordenado ya construida en $\mathbb R_C$. No presupone completitud y no menciona $\mathbb R_D$.

---

### Notación 10.4.2 — Convergencia en el modelo de Cauchy

Cuando se cumpla Definición 10.4.1 — Convergencia en $\mathbb R_C$ escribiremos

$$
\boxed{
x_n\to_C L.
}
$$

El subíndice $C$ recuerda que la convergencia se está formulando dentro del cuerpo $\mathbb R_C$. No introducimos todavía la notación $\lim$, que permanece reservada para una etapa posterior.

---

### Proposición 10.4.3 — Criterio racional para la convergencia en $\mathbb R_C$

Sean $x=(x_n)\in\mathbb R_C^{\mathbb N}$ y $L\in\mathbb R_C$. Son equivalentes:

1. $x_n\to_C L$;
2. para todo $r\in\mathbb Q$ con $0<r$, existe $N\in\mathbb N$ tal que

$$
n\ge N
\Longrightarrow
|x_n-L|<_C\iota_C(r).
$$

En forma compacta,

$$
\boxed{
x_n\to_C L
\iff
\forall r\in\mathbb Q\;
\Bigl(
0<r
\Longrightarrow
\exists N\in\mathbb N\;
\forall n\ge N,
\ |x_n-L|<_C\iota_C(r)
\Bigr).
}
$$

**Demostración.**

Supongamos primero $x_n\to_C L$. Sea $r\in\mathbb Q$ con $0<r$. Como $\iota_C$ preserva el orden y el cero,

$$
0_C<_C\iota_C(r).
$$

Aplicando Definición 10.4.1 — Convergencia en $\mathbb R_C$ a la tolerancia $\iota_C(r)$ obtenemos $N\in\mathbb N$ tal que

$$
n\ge N
\Longrightarrow
|x_n-L|<_C\iota_C(r).
$$

Recíprocamente, supongamos la condición racional y sea $\varepsilon\in\mathbb R_C$ con

$$
0_C<_C\varepsilon.
$$

Por Lema 10.1.2 — Escalas racionales positivas dentro de toda escala positiva de $\mathbb R_C$ existe $r\in\mathbb Q$ tal que

$$
0<r
\qquad\text{y}\qquad
0_C<_C\iota_C(r)<_C\varepsilon.
$$

La hipótesis proporciona $N\in\mathbb N$ con

$$
n\ge N
\Longrightarrow
|x_n-L|<_C\iota_C(r).
$$

Por transitividad del orden estricto,

$$
|x_n-L|<_C\varepsilon
\qquad(n\ge N).
$$

Así $x_n\to_C L$. ∎

> **Auditoría de elección.** Para cada tolerancia real positiva se usa un único racional testigo suministrado localmente por Lema 10.1.2 — Escalas racionales positivas dentro de toda escala positiva de $\mathbb R_C$. No se construye una función que escoja simultáneamente un racional para todas las tolerancias.

---

### Teorema 10.4.4 — Unicidad del límite en $\mathbb R_C$

Si una sucesión $x=(x_n)\in\mathbb R_C^{\mathbb N}$ satisface

$$
x_n\to_C L
\qquad\text{y}\qquad
x_n\to_C M,
$$

entonces

$$
\boxed{L=M.}
$$

**Demostración.**

Supongamos, para obtener una contradicción, que $L\neq M$. Entonces

$$
\delta:=|L-M|
$$

es no nulo por Proposición 4.2.2 — Propiedades elementales del valor absoluto (2) y no negativo por Proposición 4.2.2 — Propiedades elementales del valor absoluto (1). Por tanto

$$
0_C<_C\delta.
$$

Pongamos

$$
s:=1_C+1_C.
$$

Como $0_C<_C1_C$, la invariancia estricta por traslación da

$$
1_C<_Cs,
$$

y en particular $0_C<_Cs$. Por tanto $s^{-1}$ existe y es positivo. Definimos

$$
\eta:=\delta s^{-1}.
$$

Entonces $0_C<_C\eta$ y, por distributividad y la ley del inverso en el cuerpo $\mathbb R_C$,

$$
\boxed{\eta+\eta=\delta.}
$$

Aplicando la convergencia a $L$ con tolerancia $\eta$, existe $N_0\in\mathbb N$ tal que

$$
n\ge N_0
\Longrightarrow
|x_n-L|<_C\eta.
$$

De manera análoga, existe $N_1\in\mathbb N$ tal que

$$
n\ge N_1
\Longrightarrow
|x_n-M|<_C\eta.
$$

Por totalidad del orden natural, uno de $N_0,N_1$ domina al otro. Sea $N$ el mayor de ambos y tomemos $n=N$. Entonces

$$
|L-x_n|=|x_n-L|<_C\eta
$$

y

$$
|x_n-M|<_C\eta.
$$

La desigualdad triangular produce

$$
\begin{aligned}
\delta
&=|L-M|\\
&=|(L-x_n)+(x_n-M)|\\
&\le_C|L-x_n|+|x_n-M|\\
&<_C\eta+\eta\\
&=\delta,
\end{aligned}
$$

contradicción con la irreflexividad del orden estricto. Luego $L=M$. ∎

> **Auditoría de elección.** Sólo se combinan dos testigos locales $N_0,N_1$ mediante la totalidad del orden natural. No se realiza ninguna selección infinita.

> **Nota lógica.** La prueba parte de $L\neq M$ y, tras obtener contradicción, concluye $L=M$. Como la igualdad en $\mathbb R_C$ no es decidible en general, este cierre se clasifica como reductio/DNE clásico. No hay, sin embargo, ningún uso de Choice.

---

### Lema 10.4.5 — Un representante de Cauchy converge a su propia clase

Sea

$$
q=(q_n)_{n\in\mathbb N}\in\mathcal C_{\mathbb Q}
$$

y sea

$$
L:=[q]_C\in\mathbb R_C.
$$

Entonces la sucesión $\iota_C\circ q:\mathbb N\to\mathbb R_C$ satisface

$$
\boxed{
\iota_C(q_n)\to_C[q]_C.
}
$$

**Demostración.**

Aplicaremos el criterio racional Proposición 10.4.3 — Criterio racional para la convergencia en $\mathbb R_C$. Fijemos $\varepsilon\in\mathbb Q$ con $0<\varepsilon$. Pongamos

$$
s:=1_{\mathbb Q}+1_{\mathbb Q}
$$

y

$$
\theta:=\frac{\varepsilon}{s}.
$$

Como $0<s$, se tiene $0<\theta$ y

$$
\boxed{\theta+\theta=\varepsilon.}
$$

La condición de Cauchy de $q$ proporciona $N\in\mathbb N$ tal que, para cualesquiera $k,n\ge N$,

$$
d_{\mathbb Q}(q_k,q_n)<\theta.
$$

Por Proposición 8.2.3 — Caracterización $\varepsilon$-local de la distancia racional, esto equivale a

$$
-\theta<q_k-q_n<\theta.
$$

Fijemos ahora $n\ge N$. Como $q\in\mathcal C_{\mathbb Q}$ y las sucesiones constantes son de Cauchy, también

$$
q-\underline{q_n}\in\mathcal C_{\mathbb Q}.
$$

Además,

$$
L-\iota_C(q_n)
=
[q-\underline{q_n}]_C.
$$

Para todo $k\ge N$, de $q_k-q_n<\theta$ se sigue

$$
(q_k-q_n)+\theta
<
\theta+\theta
=
\varepsilon.
$$

El criterio de separación eventual Proposición 9.8.6 — Criterio de separación eventual para el orden estricto, aplicado a $q-\underline{q_n}$ y $\underline\varepsilon$ con margen $\theta>0$, da

$$
L-\iota_C(q_n)
<_C
\iota_C(\varepsilon).
$$

Por otra parte, de $-\theta<q_k-q_n$ y $\varepsilon=\theta+\theta$ obtenemos

$$
-\varepsilon+\theta
=
-\theta
<
q_k-q_n.
$$

Aplicando de nuevo Proposición 9.8.6 — Criterio de separación eventual para el orden estricto, ahora a $\underline{-\varepsilon}$ y $q-\underline{q_n}$, obtenemos

$$
-\iota_C(\varepsilon)
<_C
L-\iota_C(q_n).
$$

Hemos demostrado

$$
-\iota_C(\varepsilon)
<_C
L-\iota_C(q_n)
<_C
\iota_C(\varepsilon).
$$

Pongamos

$$
y:=L-\iota_C(q_n).
$$

Hemos probado

$$
-\iota_C(\varepsilon)<_Cy<_C\iota_C(\varepsilon).
$$

La desigualdad izquierda, al tomar opuestos, da

$$
-y<_C\iota_C(\varepsilon),
$$

mientras que la derecha da directamente $y<_C\iota_C(\varepsilon)$. Como, tras P0-C,

$$
|y|=\max\{y,-y\},
$$

la caracterización del máximo implica sin decidir el signo de $y$ que

$$
|L-\iota_C(q_n)|
=|y|
<_C
\iota_C(\varepsilon).
$$

Finalmente,

$$
|\iota_C(q_n)-L|
=
|-(L-\iota_C(q_n))|
=
|L-\iota_C(q_n)|,
$$

por lo que, para todo $n\ge N$,

$$
|\iota_C(q_n)-L|
<_C
\iota_C(\varepsilon).
$$

El criterio racional de convergencia concluye

$$
\iota_C(q_n)\to_C L.
$$

∎

> **Auditoría de elección.** El representante $q$ forma parte de la hipótesis del lema; no se escoge dentro de una familia de clases. Para cada $\varepsilon$ se usa un único índice $N$ suministrado por la condición de Cauchy de $q$.

---

### Teorema 10.4.6 — Convergencia al elemento diagonal canónico

Sea

$$
x=(x_n)_{n\in\mathbb N}\in\mathbb R_C^{\mathbb N}
$$

una sucesión de Cauchy y definamos

$$
q:=\operatorname{diag}_C(x),
\qquad
L:=[q]_C.
$$

Entonces

$$
\boxed{
x_n\to_C L.}
$$

Además, $L$ es el único elemento de $\mathbb R_C$ con esta propiedad.

**Demostración.**

Por Teorema 10.3.5 — La diagonal de una sucesión de Cauchy es racionalmente de Cauchy,

$$
q\in\mathcal C_{\mathbb Q}
$$

y, para todo $n$,

$$
|x_n-\iota_C(q_n)|
<_C
\iota_C(\lambda_n).
$$

El mismo teorema legitima por tanto la clase $L=[q]_C$. Por Lema 10.4.5 — Un representante de Cauchy converge a su propia clase,

$$
\iota_C(q_n)\to_C L.
$$

Demostraremos $x_n\to_C L$ mediante Proposición 10.4.3 — Criterio racional para la convergencia en $\mathbb R_C$. Sea $\varepsilon\in\mathbb Q$ con $0<\varepsilon$. Definamos

$$
s:=1_{\mathbb Q}+1_{\mathbb Q},
\qquad
\theta:=\frac{\varepsilon}{s}.
$$

Entonces $0<\theta$ y

$$
\theta+\theta=\varepsilon.
$$

Como $\lambda_n\to_{\mathbb Q}0_{\mathbb Q}$ y $\lambda_n>0$, existe $N_0\in\mathbb N$ tal que

$$
n\ge N_0
\Longrightarrow
\lambda_n<\theta.
$$

Por la convergencia $\iota_C(q_n)\to_C L$ y el criterio racional Proposición 10.4.3 — Criterio racional para la convergencia en $\mathbb R_C$, existe $N_1\in\mathbb N$ tal que

$$
n\ge N_1
\Longrightarrow
|\iota_C(q_n)-L|
<_C
\iota_C(\theta).
$$

Sea $N$ el mayor de $N_0$ y $N_1$, obtenido por una comparación en el orden total de $\mathbb N$. Para $n\ge N$, la preservación del orden por $\iota_C$ da

$$
|x_n-\iota_C(q_n)|
<_C
\iota_C(\lambda_n)
<_C
\iota_C(\theta).
$$

La desigualdad triangular en $\mathbb R_C$ produce

$$
\begin{aligned}
|x_n-L|
&\le_C
|x_n-\iota_C(q_n)|
+
|\iota_C(q_n)-L|\\
&<_C
\iota_C(\theta)+\iota_C(\theta)\\
&=
\iota_C(\varepsilon).
\end{aligned}
$$

Así, para toda tolerancia racional positiva $\varepsilon$, existe una cola en la que

$$
|x_n-L|<_C\iota_C(\varepsilon).
$$

Por Proposición 10.4.3 — Criterio racional para la convergencia en $\mathbb R_C$,

$$
x_n\to_C L.
$$

La unicidad se sigue de Teorema 10.4.4 — Unicidad del límite en $\mathbb R_C$. ∎

> **Auditoría de elección.** Tanto $q=\operatorname{diag}_C(x)$ como $L=[q]_C$ están determinados canónicamente. Los únicos índices utilizados en la prueba son testigos locales de dos propiedades de convergencia y se combinan mediante una comparación finita. No se escoge ningún representante de los $x_n$.

---

### Definición 10.4.7 — Completitud secuencial de $\mathbb R_C$

Diremos que $\mathbb R_C$ es **secuencialmente completo** si toda sucesión de Cauchy

$$
x=(x_n)_{n\in\mathbb N}\in\mathbb R_C^{\mathbb N}
$$

posee algún $L\in\mathbb R_C$ tal que

$$
x_n\to_C L.
$$

Esta definición es el análogo, dentro del modelo de Cauchy, de Definición 8.7.1 — Completitud secuencial de $\mathbb Q$ para $\mathbb Q$.

---

### Corolario 10.4.8 — $\mathbb R_C$ es secuencialmente completo

El cuerpo ordenado $\mathbb R_C$ es secuencialmente completo.

**Demostración.**

Sea $x$ una sucesión de Cauchy en $\mathbb R_C$. El teorema Teorema 10.4.6 — Convergencia al elemento diagonal canónico construye el elemento canónico

$$
L
=
[\operatorname{diag}_C(x)]_C
\in\mathbb R_C
$$

y demuestra

$$
x_n\to_C L.
$$

Esto verifica exactamente Definición 10.4.7 — Completitud secuencial de $\mathbb R_C$. ∎

> **Conclusión de la sección.** La insuficiencia secuencial detectada en $\mathbb Q$ ha desaparecido en $\mathbb R_C$: todo proceso de Cauchy de elementos del nuevo cuerpo posee un límite en el propio cuerpo. La demostración no eligió una familia de representantes; el límite se obtuvo mediante la diagonal canónica construida en §§10.2–10.3.

> **Nota fundacional.** Ésta es una **completitud secuencial clásica sin $AC_\omega$**. El límite queda canónicamente determinado por la diagonal, pero la diagonal usa el selector clásico Definición 10.2.8 — Selector canónico de aproximantes racionales; por ello la conclusión no debe leerse como un algoritmo general de límite. Bajo nombres uniformemente computables y un módulo computable de Cauchy exterior, la misma estrategia admite una versión efectiva paralela.

---
