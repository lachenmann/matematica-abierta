## 10.3. Construcción diagonal {#sec-ta-10-3}

La política de selección de §10.2 elimina el problema fundacional de escoger representantes. Falta ahora controlar la precisión con la que aproximaremos el término exterior $x_n$.

No basta elegir una tolerancia positiva fija. Para que una sucesión racional reconstruya el comportamiento asintótico de una sucesión de Cauchy en $\mathbb R_C$, el error permitido debe tender a cero. Fijaremos por ello una escala racional canónica, independiente de la sucesión que queramos aproximar.

### Definición 10.3.1 — Escala racional canónica

Para $n\in\mathbb N$ definimos

$$
\boxed{
\lambda_n
:=
\bigl(\nu_{\mathbb N}^{\mathbb Q}(n)+1_{\mathbb Q}\bigr)^{-1}.
}
$$

Esta fórmula determina una función

$$
\lambda:\mathbb N\longrightarrow\mathbb Q.
$$

La definición está bien tipada. En efecto, $0\le n$ en $\mathbb N$; como $\nu_{\mathbb N}^{\mathbb Q}$ preserva el orden,

$$
0_{\mathbb Q}
\le
\nu_{\mathbb N}^{\mathbb Q}(n).
$$

Además $0_{\mathbb Q}<1_{\mathbb Q}$, de modo que

$$
0_{\mathbb Q}
<
\nu_{\mathbb N}^{\mathbb Q}(n)+1_{\mathbb Q}.
$$

El denominador es, por tanto, no nulo y su recíproco racional está definido.

La elección de esta escala tiene una ventaja técnica importante: no requiere introducir potencias naturales. Es simplemente la sucesión racional correspondiente a

$$
1,\ \frac12,\ \frac13,\ \ldots
$$

expresada mediante la copia canónica de $\mathbb N$ en $\mathbb Q$.

### Proposición 10.3.2 — Positividad y nulidad de la escala canónica

Para todo $n\in\mathbb N$,

$$
\boxed{0<\lambda_n,}
$$

y además

$$
\boxed{
\lambda_n\to_{\mathbb Q}0_{\mathbb Q}.
}
$$

**Demostración.**

La positividad ya está contenida en la verificación tipológica de la definición: el racional

$$
\nu_{\mathbb N}^{\mathbb Q}(n)+1_{\mathbb Q}
$$

es positivo, y el recíproco de un elemento positivo de un cuerpo ordenado es positivo.

Probemos la convergencia a cero. Sea $\varepsilon\in\mathbb Q$ con

$$
0<\varepsilon.
$$

Entonces $\varepsilon^{-1}>0$. Como $\mathbb Q$ es arquimediano (Teorema 3.8.5 — $\mathbb Q$ es arquimediano), existe $N\in\mathbb N$ tal que

$$
\varepsilon^{-1}
<
\nu_{\mathbb N}^{\mathbb Q}(N).
$$

Sea ahora $n\ge N$. La preservación del orden por $\nu_{\mathbb N}^{\mathbb Q}$ da

$$
\nu_{\mathbb N}^{\mathbb Q}(N)
\le
\nu_{\mathbb N}^{\mathbb Q}(n).
$$

Como $0<1_{\mathbb Q}$,

$$
\nu_{\mathbb N}^{\mathbb Q}(n)
<
\nu_{\mathbb N}^{\mathbb Q}(n)+1_{\mathbb Q}.
$$

Por transitividad,

$$
0
<
\varepsilon^{-1}
<
\nu_{\mathbb N}^{\mathbb Q}(n)+1_{\mathbb Q}.
$$

La inversión revierte el orden entre positivos. Por tanto,

$$
0
<
\bigl(\nu_{\mathbb N}^{\mathbb Q}(n)+1_{\mathbb Q}\bigr)^{-1}
<
(\varepsilon^{-1})^{-1}.
$$

Las leyes del inverso en el cuerpo racional dan

$$
(\varepsilon^{-1})^{-1}=\varepsilon.
$$

Así, para todo $n\ge N$,

$$
0<\lambda_n<\varepsilon.
$$

Como $\lambda_n>0$,

$$
|\lambda_n-0_{\mathbb Q}|=\lambda_n,
$$

y la caracterización de la convergencia racional de Proposición 8.3.3 — Formulaciones equivalentes de la convergencia racional concluye

$$
\lambda_n\to_{\mathbb Q}0_{\mathbb Q}.
$$

∎

### Lema 10.3.3 — La incrustación racional preserva el valor absoluto

Para todo $r\in\mathbb Q$,

$$
\boxed{
\left|\iota_C(r)\right|
=
\iota_C(|r|).
}
$$

**Demostración.**

Distinguimos los dos casos de la definición de valor absoluto.

Si $0\le r$, la preservación del orden por $\iota_C$ y la identidad $\iota_C(0_{\mathbb Q})=0_C$ dan

$$
0_C\le_C\iota_C(r).
$$

Por tanto,

$$
|\iota_C(r)|
=
\iota_C(r)
=
\iota_C(|r|).
$$

Si $r<0$, la preservación del orden estricto da

$$
\iota_C(r)<_C0_C.
$$

Entonces

$$
|\iota_C(r)|
=
-\iota_C(r).
$$

Como $\iota_C$ preserva opuestos,

$$
-\iota_C(r)
=
\iota_C(-r).
$$

Y, puesto que $|r|=-r$ en este caso,

$$
|\iota_C(r)|
=
\iota_C(|r|).
$$

∎

### Definición 10.3.4 — Operador diagonal de aproximación

Sea

$$
x=(x_n)_{n\in\mathbb N}
\in
\mathbb R_C^{\mathbb N}.
$$

Definimos su diagonal racional canónica por

$$
\boxed{
\bigl(\operatorname{diag}_C(x)\bigr)_n
:=
A_C(x_n,\lambda_n).
}
$$

Como $A_C$ y $\lambda$ son funciones ya construidas, esta fórmula determina término a término un único elemento de $\mathbb Q$. Por separación en el producto correspondiente se obtiene una función

$$
\operatorname{diag}_C(x):
\mathbb N\longrightarrow\mathbb Q.
$$

De este modo queda definida una aplicación

$$
\boxed{
\operatorname{diag}_C:
\mathbb R_C^{\mathbb N}
\longrightarrow
\mathbb Q^{\mathbb N}.
}
$$

La definición existe para toda sucesión en $\mathbb R_C$; sólo cuando la sucesión exterior sea de Cauchy demostraremos que su diagonal pertenece a $\mathcal C_{\mathbb Q}$.

> **Nota fundacional.** «Diagonal canónica» significa aquí canónica en sentido extensional: cada término queda determinado por funciones ya construidas. No significa que, dada una sucesión arbitraria de clases, exista un algoritmo que calcule la diagonal:
> $$
> \boxed{
> \text{diagonal canónica extensional}
> \neq
> \text{algoritmo general}.
> }
> $$
> Bajo nombres uniformemente computables y un procedimiento efectivo de aproximación racional, puede construirse una diagonal efectiva sin exigir el mínimo clásico usado por $A_C$.

### Teorema 10.3.5 — La diagonal de una sucesión de Cauchy es racionalmente de Cauchy

Sea

$$
x=(x_n)_{n\in\mathbb N}
\in
\mathbb R_C^{\mathbb N}
$$

una sucesión de Cauchy en $\mathbb R_C$, y escribamos

$$
q:=\operatorname{diag}_C(x).
$$

Entonces

$$
\boxed{
q\in\mathcal C_{\mathbb Q}.
}
$$

Además, para todo $n\in\mathbb N$,

$$
\boxed{
|x_n-\iota_C(q_n)|
<_C
\iota_C(\lambda_n).
}
$$

**Demostración.**

Por Proposición 10.3.2 — Positividad y nulidad de la escala canónica, $\lambda_n>0$ para todo $n$. La definición de $q$ y Proposición 10.2.9 — Corrección y selección simultánea sin Choice dan inmediatamente

$$
|x_n-\iota_C(q_n)|
<_C
\iota_C(\lambda_n)
\qquad(n\in\mathbb N).
$$

Resta demostrar que $q$ es de Cauchy en $\mathbb Q$.

Sea $\varepsilon\in\mathbb Q$ con $0<\varepsilon$. Pongamos

$$
s
:=
(1_{\mathbb Q}+1_{\mathbb Q})+1_{\mathbb Q}
$$

y

$$
\theta
:=
\frac{\varepsilon}{s}.
$$

Como $0<1_{\mathbb Q}$, dos aplicaciones de la invariancia estricta por traslación muestran que $0<s$. Por positividad de inversos y productos,

$$
0<\theta.
$$

Además, por distributividad y la ley del inverso,

$$
\boxed{
\theta+\theta+\theta=\varepsilon.
}
$$

Como $\lambda_n\to_{\mathbb Q}0_{\mathbb Q}$, existe $N_0\in\mathbb N$ tal que

$$
n\ge N_0
\Longrightarrow
\lambda_n<\theta.
$$

Por otro lado, como $x$ es de Cauchy en $\mathbb R_C$, el criterio racional Proposición 10.1.3 — Criterio racional para las sucesiones de Cauchy en $\mathbb R_C$, aplicado a $\theta>0$, proporciona $N_1\in\mathbb N$ tal que

$$
m,n\ge N_1
\Longrightarrow
|x_m-x_n|
<_C
\iota_C(\theta).
$$

Por totalidad del orden natural, uno de $N_0,N_1$ es mayor o igual que el otro. Tomamos como $N$ ese mayor. Ésta es una comparación finita entre dos índices, no una elección de una familia.

Sean $m,n\ge N$. Entonces $m,n\ge N_0$ y $m,n\ge N_1$. De la estimación diagonal y de la preservación del orden por $\iota_C$ obtenemos

$$
|x_m-\iota_C(q_m)|
<_C
\iota_C(\lambda_m)
<_C
\iota_C(\theta),
$$

y análogamente

$$
|x_n-\iota_C(q_n)|
<_C
\iota_C(\theta).
$$

En el cuerpo ordenado $\mathbb R_C$, la desigualdad triangular aplicada dos veces da

$$
\begin{aligned}
|\iota_C(q_m)-\iota_C(q_n)|
&=
|\,(\iota_C(q_m)-x_m)+(x_m-x_n)+(x_n-\iota_C(q_n))\,|\\
&\le_C
|\iota_C(q_m)-x_m|
+
|x_m-x_n|
+
|x_n-\iota_C(q_n)|.
\end{aligned}
$$

Por $|-y|=|y|$,

$$
|\iota_C(q_m)-x_m|
=
|x_m-\iota_C(q_m)|.
$$

Cada uno de los tres sumandos anteriores es estrictamente menor que $\iota_C(\theta)$. La compatibilidad estricta del orden con la suma produce entonces

$$
|\iota_C(q_m)-\iota_C(q_n)|
<_C
\iota_C(\theta)
+
\iota_C(\theta)
+
\iota_C(\theta).
$$

Como $\iota_C$ preserva la suma y $\theta+\theta+\theta=\varepsilon$,

$$
|\iota_C(q_m)-\iota_C(q_n)|
<_C
\iota_C(\varepsilon).
$$

Ahora, Proposición 9.9.3 — Preservación de la aritmética racional y Lema 10.3.3 — La incrustación racional preserva el valor absoluto dan

$$
\begin{aligned}
|\iota_C(q_m)-\iota_C(q_n)|
&=
|\iota_C(q_m-q_n)|\\
&=
\iota_C(|q_m-q_n|).
\end{aligned}
$$

La reflexión del orden estricto por $\iota_C$ implica

$$
|q_m-q_n|<\varepsilon.
$$

Por la definición de $d_{\mathbb Q}$,

$$
d_{\mathbb Q}(q_m,q_n)<\varepsilon.
$$

Como $\varepsilon>0$ era arbitraria, $q$ satisface Definición 8.4.1 — Sucesión racional de Cauchy; por Definición 8.4.2 — Conjunto de las sucesiones racionales de Cauchy,

$$
q\in\mathcal C_{\mathbb Q}.
$$

∎

El teorema produce ya un elemento legítimo de $\mathbb R_C$:

$$
\boxed{
[\operatorname{diag}_C(x)]_C
\in
\mathbb R_C.
}
$$

Éste será el candidato a límite de la sucesión exterior $x$.
