## 17.3. Continuidad y preimágenes de conjuntos abiertos {#sec-ta-17-3}

La continuidad fue definida en §17.1 mediante una condición local, centrada en cada punto del dominio. El Capítulo 15, en cambio, llamó *abierto de la recta* a un conjunto que contiene una bola alrededor de cada uno de sus puntos. Para relacionar ambos lenguajes debemos recordar que una función puede estar definida sólo sobre $D\subseteq\mathbb R$. En tal caso, el entorno pertinente es la intersección de una bola con $D$; no exigiremos que el propio dominio sea abierto en la recta.

### Definición 17.3.1 — Abiertos y cerrados relativos a un subconjunto de la recta
Fijemos $D\subseteq\mathbb R$ y $A\subseteq D$. Diremos que **$A$ es abierto relativo a $D$** si existe un abierto $U\subseteq\mathbb R$ tal que

$$
\boxed{A=D\cap U.}
$$

Diremos que **$A$ es cerrado relativo a $D$** si $D\setminus A$ es abierto relativo a $D$. Ambas expresiones son predicados sobre subconjuntos $A\subseteq D$; el conjunto ambiente forma parte de su significado. En particular, que $A$ sea abierto relativo a $D$ no afirma que sea abierto en $\mathbb R$. Estas definiciones introducen únicamente la noción elemental de subespacio de la recta, sin presuponer la teoría general de espacios topológicos.

### Proposición 17.3.2 — Criterio por bolas y representación de los cerrados relativos
Para $A\subseteq D\subseteq\mathbb R$ se cumplen dos equivalencias:

$$
\boxed{\begin{aligned}
A\text{ es abierto relativo a }D
&\iff \forall a\in A\ \exists r>0:\ D\cap B_r(a)\subseteq A;\\
A\text{ es cerrado relativo a }D
&\iff \exists F\subseteq\mathbb R:\ F\text{ cerrado y }A=D\cap F.
\end{aligned}}
$$

**Demostración.**
Supongamos $A=D\cap U$ con $U$ abierto en $\mathbb R$. Para cada $a\in A$, también $a\in U$, de modo que la apertura de $U$ proporciona un radio $r>0$ con $B_r(a)\subseteq U$. Entonces $D\cap B_r(a)\subseteq D\cap U=A$.

Recíprocamente, supongamos el criterio de bolas y definamos el conjunto

$$
U:=\bigcup\{B_r(a):a\in A,\ r\in\mathbb R,\ r>0,\ D\cap B_r(a)\subseteq A\}.
$$

La familia indicada es un conjunto: el conjunto de pares admisibles se obtiene por Separación en $A\times\mathbb R$; el grafo de $(a,r)\mapsto B_r(a)$ se obtiene por Separación en $(A\times\mathbb R)\times\mathcal P(\mathbb R)$, y su recorrido es un conjunto. La unión existe por el axioma de Unión. No se requiere Reemplazo ni Elección. Cada bola es abierta por Teorema §15.2.5 — Toda bola abierta es un conjunto abierto; su unión es abierta por Teorema §15.2.7 — Leyes fundamentales de los conjuntos abiertos. Si $a\in A$, el criterio proporciona un radio que sitúa $a\in B_r(a)\subseteq U$, y por tanto $A\subseteq D\cap U$. Si $x\in D\cap U$, alguna bola de la familia contiene $x$; la condición que define esa familia implica $x\in A$. En consecuencia, $A=D\cap U$. No se escoge un radio *para cada punto*: se reúnen **todas** las bolas que cumplen la condición.

Para la segunda equivalencia, si $A$ es cerrado relativo, existe un abierto $U$ de $\mathbb R$ con $D\setminus A=D\cap U$. Poniendo $F=\mathbb R\setminus U$, el conjunto $F$ es cerrado y las identidades de complemento relativo dan

$$
A=D\setminus(D\cap U)=D\cap(\mathbb R\setminus U)=D\cap F.
$$

En sentido inverso, si $A=D\cap F$ con $F$ cerrado en la recta, entonces $D\setminus A=D\cap(\mathbb R\setminus F)$ es abierto relativo. Esto concluye ambas caracterizaciones. ∎

La definición y la proposición cubren también $D=\varnothing$: su único subconjunto es simultáneamente abierto y cerrado relativo. Cuando $D$ es cualquier conjunto, $D=D\cap\mathbb R$ es abierto relativo a sí mismo, aunque $D$ no sea abierto en la recta.


### Proposición 17.3.3 — Criterio local de continuidad mediante abiertos de llegada
Sean $f:D\to\mathbb R$ y $a\in D$. Las siguientes condiciones son equivalentes:

1. $f$ es continua en $a$.
2. Para todo abierto $V\subseteq\mathbb R$ tal que $f(a)\in V$, existe un abierto relativo $W\subseteq D$ con

   $$
   \boxed{a\in W\subseteq f^{-1}[V].}
   $$

La preimagen significa siempre $f^{-1}[V]=\{x\in D:f(x)\in V\}$; no presupone que $f$ sea invertible.

**Demostración.**
Supongamos continua $f$ en $a$ y fijemos un abierto $V$ que contenga $f(a)$. Por apertura existe $\varepsilon>0$ tal que $B_\varepsilon(f(a))\subseteq V$. La continuidad para ese $\varepsilon$ suministra $\delta>0$ con $f[D\cap B_\delta(a)]\subseteq B_\varepsilon(f(a))\subseteq V$. Tomemos $W=D\cap B_\delta(a)$, que es abierto relativo porque la bola es abierta en $\mathbb R$; como $a\in D$ y $\delta>0$, tenemos $a\in W$ y, por definición de preimagen, $W\subseteq f^{-1}[V]$.

Para la recíproca, sea $\varepsilon>0$ y pongamos $V=B_\varepsilon(f(a))$. Este conjunto es abierto y contiene $f(a)$. Por la segunda condición existe un abierto relativo $W$ con $a\in W\subseteq f^{-1}[V]$. El criterio por bolas de Proposición §17.3.2 — Criterio por bolas y representación de los cerrados relativos produce $\delta>0$ tal que $D\cap B_\delta(a)\subseteq W$. De ahí, para todo $x\in D$ con $|x-a|<\delta$, tenemos $f(x)\in V$, es decir, $|f(x)-f(a)|<\varepsilon$. Como $\varepsilon$ era arbitrario, $f$ es continua en $a$. Ninguna de las dos direcciones selecciona simultáneamente vecindades para distintos valores de $a$ o $V$. ∎


### Teorema 17.3.4 — Caracterización global por preimágenes de abiertos
Sea $f:D\to\mathbb R$, con $D\subseteq\mathbb R$ arbitrario. Son equivalentes:

$$
\boxed{\begin{gathered}
\forall a\in D,\quad f\text{ es continua en }a;\\
\text{para todo abierto }V\subseteq\mathbb R,\quad
f^{-1}[V]\text{ es abierto relativo a }D.
\end{gathered}}
$$

En la caja se enuncian dos propiedades equivalentes, no una conjunción que defina «continuidad» de nuevo. Para $D=\varnothing$ ambas propiedades se satisfacen, pues la primera es universal sobre el vacío y toda preimagen es $\varnothing$, abierto relativo a $D$.

**Demostración.**
Supongamos que $f$ es continua en cada $a\in D$. Sea $V$ un abierto de la recta y escribamos $A=f^{-1}[V]\subseteq D$. Para acreditar que $A$ es abierto relativo basta, por Proposición §17.3.2 — Criterio por bolas y representación de los cerrados relativos, comprobar el criterio de bolas para cada $a\in A$. Tomemos uno arbitrario. De $a\in f^{-1}[V]$ resulta $f(a)\in V$; la apertura de $V$ y la continuidad en $a$, o directamente Proposición §17.3.3 — Criterio local de continuidad mediante abiertos de llegada, proporcionan un abierto relativo $W_a$ con $a\in W_a\subseteq A$. Aplicando el criterio por bolas a **ese** $W_a$ obtenemos un radio $r>0$ tal que $D\cap B_r(a)\subseteq W_a\subseteq A$. Como $a$ era arbitrario, $A$ es abierto relativo. El argumento no construye una familia $a\mapsto W_a$: elimina los testigos sólo para un punto fijado.

Recíprocamente, supongamos que toda preimagen de un abierto es abierta relativa. Fijemos $a\in D$ y un abierto $V$ que contenga $f(a)$. Entonces $A=f^{-1}[V]$ es abierto relativo y $a\in A$. Tomando $W=A$ se verifica la segunda condición de Proposición §17.3.3 — Criterio local de continuidad mediante abiertos de llegada; por dicha proposición, $f$ es continua en $a$. La arbitrariedad de $a$ concluye la continuidad en todo $D$. No se ha utilizado Teorema §17.2.4 — Criterio secuencial universal bajo elección numerable explícita ni ninguna hipótesis de elección numerable. ∎

**Ejemplo que precisa el ambiente.** Sea $D=[0,1]\subseteq\mathbb R$ y $f:D\to\mathbb R$ la inclusión funcional $f(x)=x$, con su dominio y codominio tipados. Es continua por la definición $\varepsilon$–$\delta$: para cada $a\in D$ basta $\delta=\varepsilon$. Si $V=(-1,1/2)$, su preimagen es $[0,1/2)$, que no es abierto en la recta porque $0$ carece de una bola íntegramente incluida en él, pero sí es abierto relativo a $D$:

$$
f^{-1}[V]=D\cap(-1,1/2).
$$

La forma correcta del teorema no puede sustituir «abierto relativo a $D$» por «abierto en $\mathbb R$» sin añadir otras hipótesis, y ni siquiera se necesita que $D$ sea abierto para que $f$ sea continua.


### Corolario 17.3.5 — Caracterización equivalente por preimágenes de cerrados
Una función $f:D\to\mathbb R$ es continua en todo $D$ si y sólo si, para todo cerrado $F\subseteq\mathbb R$, la preimagen $f^{-1}[F]$ es **cerrada relativa a $D$**.

**Demostración.**
Para cualquier $F\subseteq\mathbb R$, la definición de preimagen y el hecho de que $f$ tenga dominio exactamente $D$ proporcionan la identidad

$$
\boxed{D\setminus f^{-1}[F]=f^{-1}[\mathbb R\setminus F].}
$$

En efecto, para $x\in D$, no pertenecer a $f^{-1}[F]$ equivale a que $f(x)\notin F$, es decir, a $f(x)\in\mathbb R\setminus F$. Esta comprobación puntual demuestra la igualdad de conjuntos por extensionalidad.

Si $f$ es continua y $F$ es cerrado, el complemento $V=\mathbb R\setminus F$ es abierto. El teorema anterior asegura que $f^{-1}[V]=D\setminus f^{-1}[F]$ es abierto relativo, de modo que $f^{-1}[F]$ es cerrado relativo. Inversamente, supongamos que todas las preimágenes de cerrados son cerradas relativas. Para cualquier abierto $V$, el conjunto $F=\mathbb R\setminus V$ es cerrado; su preimagen es cerrada relativa, por lo que $D\setminus f^{-1}[F]=f^{-1}[V]$ es abierta relativa. El Teorema 17.3.4 concluye que $f$ es continua en todo $D$. ∎

**Síntesis.** Las tres descripciones —control $\varepsilon$–$\delta$ en cada punto, transporte local de vecindades y preimágenes globales de abiertos o cerrados— son equivalentes en ZF para dominios arbitrarios. La continuidad es una condición sobre las preimágenes, no sobre la imagen directa de los abiertos: no hemos afirmado que $f[U]$ sea abierto cuando $U$ lo es. En §17.4 aprovecharemos el criterio para estudiar álgebra y composición de funciones continuas, conservando siempre sus dominios efectivos.
