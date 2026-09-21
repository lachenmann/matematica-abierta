## 15.2. Puntos interiores y conjuntos abiertos {#sec-ta-15-2}

La propiedad de ser vecindad pertenece, en principio, a un conjunto *respecto de un punto*. La convertiremos ahora en dos nociones distintas. Primero preguntaremos si un punto dispone de espacio suficiente **dentro de un conjunto dado**. Después exigiremos que esa condición se cumpla para todos los puntos del conjunto. No intercambiaremos ambos niveles de cuantificación.

### Definición 15.2.1 — Punto interior de un conjunto
Sean $A\subseteq\mathbb R$ y $a\in\mathbb R$. Diremos que $a$ es un **punto interior de $A$** cuando existe un número real $r>0$ tal que la bola centrada en $a$ está contenida en $A$:

$$
\boxed{a\text{ es interior a }A\iff\exists r\in\mathbb R\ (r>0\ \text{y}\ B_r(a)\subseteq A).}
$$

Por Proposición §15.1.2 — Las bolas son intervalos abiertos centrados, el centro pertenece a cualquier bola de radio positivo. En consecuencia, la condición implica $a\in A$: no es necesario imponer esa pertenencia como una hipótesis adicional. El radio puede depender del punto $a$ y del conjunto $A$; no postulamos un radio común para todos los puntos.

> **Lectura de cuantificadores.** «$a$ es interior a $A$» significa que **existe** un margen positivo para **ese punto** y que **todos** los puntos suficientemente próximos permanecen en $A$. No significa que baste con encontrar un punto próximo que pertenezca a $A$.


### Definición 15.2.2 — Interior de un conjunto
Para $A\subseteq\mathbb R$, llamaremos **interior de $A$** al conjunto de sus puntos interiores y escribiremos

$$
\boxed{A^\circ:=\{a\in A:\exists r\in\mathbb R\ (r>0\ \text{y}\ B_r(a)\subseteq A)\}.}
$$

Este conjunto existe por Separación sobre $A$: en su fórmula sólo figuran el orden, el valor absoluto, las bolas y la inclusión, todos previamente definidos. El símbolo $A^\circ$ denota un **conjunto**, no un punto ni un radio. Además, la asignación $A\mapsto A^\circ$ determina una función $\mathcal P(\mathbb R)\to\mathcal P(\mathbb R)$: su grafo se obtiene por Separación dentro del producto de esos dos conjuntos, y para cada $A$ el conjunto definido es único por extensionalidad. No hay elección de radios para definirla.


### Proposición 15.2.3 — Interior y vecindades
Si $A\subseteq\mathbb R$ y $a\in\mathbb R$, entonces

$$
\boxed{a\in A^\circ\iff A\text{ es una vecindad de }a.}
$$

En particular, $A^\circ\subseteq A$.

**Demostración.**
Si $a\in A^\circ$, la definición del interior proporciona $r>0$ con $B_r(a)\subseteq A$; exactamente esto afirma que $A$ es vecindad de $a$. Recíprocamente, si $A$ es vecindad de $a$, existe $r>0$ con $B_r(a)\subseteq A$. Como $a\in B_r(a)$ por Proposición §15.1.2 — Las bolas son intervalos abiertos centrados, también $a\in A$; satisface por tanto la condición que define $A^\circ$. Finalmente, cada elemento de $A^\circ$ pertenece a $A$ por la propia Separación que lo define. ∎

La equivalencia explica por qué se introdujo primero la noción de vecindad: un punto es interior a $A$ precisamente cuando $A$ ofrece una vecindad de ese punto.


### Definición 15.2.4 — Conjunto abierto de la recta
Un subconjunto $U\subseteq\mathbb R$ se llama **abierto (en $\mathbb R$)** si cada uno de sus puntos es interior a él:

$$
\boxed{U\text{ es abierto}\iff
\forall x\in U\ \exists r\in\mathbb R\ (r>0\ \text{y}\ B_r(x)\subseteq U).}
$$

El alcance de «abierto» es el ambiente $\mathbb R$: no se ha definido aún ninguna topología de subespacio. La condición es universal sobre $x\in U$; cuando $U$ es vacío no existe ningún punto para el cual verificarla, y esta observación tendrá una consecuencia precisa. La palabra «bola abierta», usada en §15.1 como nombre del objeto, recibe ahora su justificación matemática.


### Teorema 15.2.5 — Toda bola abierta es un conjunto abierto
Para cualquier $a\in\mathbb R$ y cualquier $r>0$, el conjunto $B_r(a)$ es abierto en $\mathbb R$.

**Demostración.**
Fijemos $y\in B_r(a)$, sin presuponer una fórmula para todos los demás puntos. La proposición Proposición §15.1.3 — Una bola contiene una bola alrededor de cada uno de sus puntos demuestra que $\rho=r-|y-a|$ es estrictamente positivo y que

$$
B_\rho(y)\subseteq B_r(a).
$$

Hemos encontrado una bola centrada en el punto arbitrario $y$ y contenida en el conjunto considerado. Esto verifica exactamente la definición de abierto. ∎

La diferencia $r-|y-a|$ es el margen que queda hasta la frontera de la bola original. La prueba no usa completitud ni Choice: reutiliza la desigualdad triangular del Capítulo 4 y un radio explícito.


### Proposición 15.2.6 — Caracterización de los abiertos mediante el interior
Para todo $A\subseteq\mathbb R$,

$$
\boxed{A\text{ es abierto}\iff A^\circ=A.}
$$

**Demostración.**
Siempre tenemos $A^\circ\subseteq A$ por Proposición §15.2.3 — Interior y vecindades. Si $A$ es abierto, todo $x\in A$ dispone de un radio positivo con $B_r(x)\subseteq A$, por lo que $x\in A^\circ$ y $A\subseteq A^\circ$. La doble inclusión da $A=A^\circ$. Recíprocamente, si $A=A^\circ$, cada $x\in A$ pertenece al interior; la definición de este último proporciona una bola $B_r(x)\subseteq A$. Por tanto, $A$ es abierto. ∎

El interior permite reconocer un abierto sin volver a repetir verbalmente todos los cuantificadores: un conjunto es abierto exactamente cuando **no le faltan puntos interiores entre sus propios puntos**.


### Teorema 15.2.7 — Leyes fundamentales de los conjuntos abiertos
Se cumplen las propiedades siguientes:

1. $\varnothing$ y $\mathbb R$ son abiertos.
2. Si $I$ es cualquier conjunto y $(U_i)_{i\in I}$ es una familia de subconjuntos abiertos de $\mathbb R$, entonces $\bigcup_{i\in I}U_i$ es abierto, también para $I=\varnothing$.
3. Si $U,V\subseteq\mathbb R$ son abiertos, entonces $U\cap V$ es abierto. En consecuencia, toda intersección **finita** de abiertos es abierta, entendiendo la intersección de una familia vacía respecto del ambiente $\mathbb R$ como $\mathbb R$.

**Demostración.**
**(1)** Para $\varnothing$, el enunciado «para todo $x\in\varnothing$» es verdadero porque no hay elementos en ese conjunto. Para $\mathbb R$, fijemos $x\in\mathbb R$: el radio real $1>0$ está disponible en el cuerpo fijado, y $B_1(x)\subseteq\mathbb R$ por definición. Ambos conjuntos son abiertos.

**(2)** La unión indexada existe como conjunto por Definición §0.6.16 — Familia indexada, y sus elementos pertenecen a $\mathbb R$. Sea $x\in\bigcup_{i\in I}U_i$. Por la definición de unión existe **un índice** $i\in I$ tal que $x\in U_i$. Como ese $U_i$ es abierto, existe $r>0$ con $B_r(x)\subseteq U_i$. Por pertenencia a la unión, $U_i\subseteq\bigcup_{j\in I}U_j$; luego

$$
B_r(x)\subseteq\bigcup_{j\in I}U_j.
$$

El punto $x$ era arbitrario. Si $I=\varnothing$, la unión es $\varnothing$ y ya está cubierta por (1). En esta prueba se eliminan dos existenciales para un punto **fijo**; no se elige simultáneamente un índice o un radio para todos los puntos.

**(3)** Fijemos $x\in U\cap V$. Hay radios $r,s>0$ con $B_r(x)\subseteq U$ y $B_s(x)\subseteq V$. Por Proposición §15.1.5 — Propiedades elementales de las vecindades, la intersección de estas dos vecindades es una vecindad de $x$, o, explícitamente, tomando $t=\min\{r,s\}>0$, obtenemos

$$
B_t(x)\subseteq B_r(x)\cap B_s(x)\subseteq U\cap V.
$$

Así $U\cap V$ es abierto. Para una familia de abiertos indexada por cualquier número natural $n$ de índices, induzcamos sobre $n$: con cero índices su intersección en $\mathbb R$ es $\mathbb R$, abierta por (1); al añadir un conjunto al paso sucesor, se intersecta el abierto ya obtenido con el nuevo abierto y se aplica el caso binario. Toda intersección finita queda cubierta, incluida la vacía. ∎

> **La asimetría esencial.** En el caso de las uniones basta hallar **un** abierto que contenga al punto. En una intersección, en cambio, necesitamos una bola contenida en **todos** los conjuntos involucrados; la operación de tomar el mínimo de dos radios funciona para un número finito de ellos, pero no demuestra por sí sola que una intersección infinita sea abierta. No anticiparemos tal afirmación.


### Teorema 15.2.8 — El interior es el mayor abierto contenido en el conjunto
Sea $A\subseteq\mathbb R$. Entonces $A^\circ$ es abierto, está contenido en $A$ y satisface

$$
\boxed{U\subseteq A\ \text{y}\ U\text{ abierto}\implies U\subseteq A^\circ.}
$$

Es decir: $A^\circ$ es el **mayor** —respecto de la inclusión— entre los conjuntos abiertos contenidos en $A$.

**Demostración.**
Ya sabemos por Proposición §15.2.3 — Interior y vecindades que $A^\circ\subseteq A$. Para probar que es abierto, sea $x\in A^\circ$. Existe $r>0$ tal que $B_r(x)\subseteq A$. Afirmamos que, más precisamente,

$$
B_r(x)\subseteq A^\circ.
$$

En efecto, dado cualquier $y\in B_r(x)$, Proposición §15.1.3 — Una bola contiene una bola alrededor de cada uno de sus puntos produce el radio positivo $\rho=r-|y-x|$ para el cual

$$
B_\rho(y)\subseteq B_r(x)\subseteq A.
$$

Esto hace a $y$ interior a $A$, es decir, $y\in A^\circ$. La inclusión afirmada muestra que $x$ dispone de una bola contenida en $A^\circ$; puesto que $x$ era arbitrario, el interior es abierto.

Sea ahora $U\subseteq A$ cualquier abierto y tomemos $x\in U$. Por apertura existe $s>0$ con $B_s(x)\subseteq U$. La transitividad de la inclusión da $B_s(x)\subseteq A$ y por tanto $x\in A^\circ$. Queda probado $U\subseteq A^\circ$. La existencia del mayor abierto no exige escoger uno entre todos los abiertos: el conjunto $A^\circ$ se construyó explícitamente por Separación en Definición §15.2.2 — Interior de un conjunto. ∎

La propiedad de maximalidad será la justificación estructural de las leyes del interior. Por ejemplo, como $A^\circ$ ya es abierto, la proposición Proposición §15.2.6 — Caracterización de los abiertos mediante el interior permite concluir $(A^\circ)^\circ=A^\circ$; esta igualdad es una consecuencia inmediata de resultados ya demostrados, no una nueva definición.


### Proposición 15.2.9 — Ejemplos: intervalos abiertos y singletons
Para cualesquiera $a,b\in\mathbb R$ con $a<b$, el intervalo $(a,b)$ es abierto. En cambio, para todo $a\in\mathbb R$, el conjunto $\{a\}$ **no** es abierto en $\mathbb R$.

**Demostración.**
Sea $x\in(a,b)$, de modo que $a<x<b$. Ambos números $x-a$ y $b-x$ son positivos. Definamos

$$
r:=\min\{x-a,b-x\}>0.
$$

Si $y\in B_r(x)$, la igualdad bola–intervalo de Proposición §15.1.2 — Las bolas son intervalos abiertos centrados da $x-r<y<x+r$. Como $r\le x-a$ y $r\le b-x$, se tiene $a\le x-r<y<x+r\le b$; luego $a<y<b$. Así $B_r(x)\subseteq(a,b)$ y, al ser $x$ arbitrario, $(a,b)$ es abierto.

Para el singleton, supongamos que $\{a\}$ fuese abierto. La definición produciría $r>0$ con $B_r(a)\subseteq\{a\}$. Puesto que $a<a+r$ y el cuerpo ordenado real es densamente ordenado por Teorema §4.1.11 — Todo cuerpo ordenado es densamente ordenado, existe $y$ tal que $a<y<a+r$. Como $a-r<a<y$, la igualdad $B_r(a)=(a-r,a+r)$ implica $y\in B_r(a)$, pero $y\ne a$; contradicción. Por consiguiente $\{a\}$ no es abierto. ∎

> **Contraste decisivo.** La expresión «intervalo abierto» coincide con la noción de conjunto abierto que acabamos de definir; en cambio, que un conjunto contenga un punto no garantiza que ese punto sea interior. En la siguiente sección estudiaremos qué sucede fuera de $A$ y cómo el complemento permite definir los conjuntos cerrados, sin confundir «no abierto» con «cerrado».
