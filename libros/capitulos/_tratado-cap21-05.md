## 21.5. Propiedades algebraicas y de orden de la integral {#sec-ta-21-5}

Ya sabemos reconocer cuándo una función acotada es integrable y encerrar su integral entre dos sumas finitas. Ahora estudiaremos qué sucede al comparar dos funciones, sumarlas o multiplicarlas por un escalar. El orden deductivo importa: una fórmula como $\int_a^b(f+g)=\int_a^b f+\int_a^b g$ sólo tiene significado **después** de probar que $f+g$ es integrable. Las operaciones puntuales y su tipado están disponibles desde Proposición §16.3.2 — Existencia y tipado de las operaciones puntuales; las cotas extremas locales y las sumas de Darboux, desde §21.2.

En toda la sección fijamos $a,b\in\mathbb R$ con $a<b$, escribimos $I=[a,b]$, y entendemos que las funciones consideradas tienen dominio **exactamente** $I$ y codominio $\mathbb R$. El número de subintervalos de una partición es natural; los escalares, las anchuras y los valores integrales pertenecen a $\mathbb R$.

### Proposición 21.5.1 — Acotación de las operaciones y cálculo de las constantes
Si $f,g:I\to\mathbb R$ son acotadas y $\lambda,c\in\mathbb R$, entonces $f+g$, $\lambda f$ y la función constante $\mathbf c:I\to\mathbb R$, $\mathbf c(t)=c$, son funciones acotadas con el mismo dominio y codominio. Además, para **toda** partición $P$,

$$
\boxed{L(\mathbf c,P)=U(\mathbf c,P)=c(b-a).}
\tag{21.5.1}
$$

En consecuencia, $\mathbf c$ es integrable y

$$
\boxed{\int_a^b\mathbf c=c(b-a).}
\tag{21.5.2}
$$

**Demostración.**
Por acotación existen $A_f,B_f,A_g,B_g\in\mathbb R$ tales que $A_f\le f(t)\le B_f$ y $A_g\le g(t)\le B_g$ para cada $t\in I$. Fijamos esos **cuatro testigos**, sin elegir cotas para una familia de funciones: la suma puntual satisface

$$
A_f+A_g\le(f+g)(t)\le B_f+B_g.
$$

Si $\lambda>0$, las cotas de $\lambda f$ son $\lambda A_f$ y $\lambda B_f$; si $\lambda<0$, son $\lambda B_f$ y $\lambda A_f$; si $\lambda=0$, ambos valores son cero. Las operaciones puntuales dan funciones tipadas según Proposición §16.3.2 — Existencia y tipado de las operaciones puntuales; el grafo de $\mathbf c$ es el conjunto explícito $\{\langle t,c\rangle:t\in I\}\subseteq I\times\mathbb R$. Sus dos cotas pueden tomarse iguales a $c$.

Para cada subintervalo no vacío $I_k(P)$, la imagen de $\mathbf c$ es exactamente el singleton $\{c\}$; sus ínfimo y supremo son $c$. La definición de las sumas y la identidad finita de anchuras Proposición §21.1.2 — Existencia, anchuras positivas y suma de longitudes dan

$$
L(\mathbf c,P)=\sum_{k<n}c\Delta_k(P)
=c\sum_{k<n}\Delta_k(P)=c(b-a)=U(\mathbf c,P).
$$

La brecha es cero; el criterio de Darboux Teorema §21.4.2 — Criterio de Darboux y estabilidad por refinamiento establece integrabilidad. El encierro Proposición §21.4.4 — Encierro del valor integral y control por la brecha identifica su integral con el valor común de (21.5.1). No se ha inferido integrabilidad de ninguna función arbitraria a partir de su mera acotación. $\square$

### Proposición 21.5.2 — Orden puntual, sumas e integral
Sean $f,g:I\to\mathbb R$ acotadas y supongamos $f(t)\le g(t)$ para todo $t\in I$. Para cada conjunto **no vacío** $J\subseteq I$ y toda partición $P$,

$$
\boxed{m(f,J)\le m(g,J),\quad M(f,J)\le M(g,J),}
\tag{21.5.3}
$$

$$
\boxed{L(f,P)\le L(g,P),\qquad U(f,P)\le U(g,P).}
\tag{21.5.4}
$$

Si, además, ambas funciones son integrables, entonces

$$
\boxed{\int_a^b f\le\int_a^b g.}
\tag{21.5.5}
$$

**Demostración.**
Para todo $t\in J$, $m(f,J)\le f(t)\le g(t)$. Por ello $m(f,J)$ es una cota inferior de $g[J]$ y no excede su **mayor** cota inferior: $m(f,J)\le m(g,J)$. Asimismo, $f(t)\le g(t)\le M(g,J)$: el número $M(g,J)$ es cota superior de $f[J]$ y $M(f,J)\le M(g,J)$. Los extremos existen por Lema §21.2.2 — Existencia de las cotas extremas locales y comparación por inclusión, sin estar necesariamente alcanzados.

Aplicamos estas desigualdades a cada $J=I_k(P)$, multiplicamos por $\Delta_k(P)>0$ y sumamos: la comparación finita Proposición §14.5.1 — Comparación de sumas finitas y de bloques demuestra (21.5.4). Si $f$ y $g$ son integrables, para **toda** partición $P$ obtenemos

$$
L(f,P)\le L(g,P)\le\int_a^b g.
$$

Así $\int_a^b g$ es cota superior de $\mathcal L_f$. Su supremo es $\int_a^b f$ por §§21.3–21.4; se deduce (21.5.5). Obsérvese que la comparación de las **sumas** no exigió integrabilidad, mientras que la comparación de los **valores integrales** sí la exige en ambos miembros. $\square$

### Lema 21.5.3 — Estimaciones de Darboux para una suma puntual
Para funciones acotadas $f,g:I\to\mathbb R$, todo conjunto no vacío $J\subseteq I$ y toda partición $P$,

$$
\boxed{m(f,J)+m(g,J)\le m(f+g,J),}
\tag{21.5.6}
$$

$$
\boxed{M(f+g,J)\le M(f,J)+M(g,J),}
\tag{21.5.7}
$$

$$
\boxed{L(f,P)+L(g,P)\le L(f+g,P)\le U(f+g,P)
\le U(f,P)+U(g,P).}
\tag{21.5.8}
$$

Por tanto, la brecha de la suma está controlada por las de los sumandos:

$$
\boxed{0\le U(f+g,P)-L(f+g,P)
\le [U(f,P)-L(f,P)]+[U(g,P)-L(g,P)].}
\tag{21.5.9}
$$

No afirmamos que los ínfimos o supremos locales sean **aditivos**: las desigualdades (21.5.6)–(21.5.7) pueden ser estrictas.

**Demostración.**
Para cada $t\in J$ se cumple $m(f,J)+m(g,J)\le f(t)+g(t)$. El miembro izquierdo es, pues, cota inferior del conjunto no vacío $(f+g)[J]$; la propiedad del ínfimo establece (21.5.6). Igualmente, $f(t)+g(t)\le M(f,J)+M(g,J)$ para todo $t$, y la propiedad del supremo demuestra (21.5.7).

Apliquemos ambas a cada $I_k(P)$ y multipliquemos por las anchuras positivas. Al sumar, la distributividad y aditividad de sumas finitas dan

$$
\sum_{k<n}[m_k(f,P)+m_k(g,P)]\Delta_k(P)
=L(f,P)+L(g,P)\le L(f+g,P),
$$

$$
U(f+g,P)\le\sum_{k<n}[M_k(f,P)+M_k(g,P)]\Delta_k(P)
=U(f,P)+U(g,P).
$$

La desigualdad central $L(f+g,P)\le U(f+g,P)$ ya se demostró en Proposición §21.2.5 — Encierro global e identidad de la brecha. Restar la primera desigualdad extrema de la última produce (21.5.9); su no negatividad procede del mismo resultado. No hemos usado un punto que maximice $f$ o $g$: el razonamiento se hace enteramente con cotas extremales. $\square$

### Teorema 21.5.4 — La suma de funciones integrables es integrable y su integral es aditiva
Si $f,g:I\to\mathbb R$ son integrables, entonces $f+g$ es integrable y

$$
\boxed{\int_a^b(f+g)=\int_a^b f+\int_a^b g.}
\tag{21.5.10}
$$

**Demostración.**
La función $f+g$ está acotada por Proposición §21.5.1 — Acotación de las operaciones y cálculo de las constantes. Fijemos $\varepsilon>0$. El criterio Teorema §21.4.2 — Criterio de Darboux y estabilidad por refinamiento, aplicado **una vez** a cada sumando con tolerancia $\varepsilon/2$, entrega particiones $P_f,P_g$ tales que

$$
U(f,P_f)-L(f,P_f)<\varepsilon/2,\qquad
U(g,P_g)-L(g,P_g)<\varepsilon/2.
$$

El teorema del refinamiento común Teorema §21.1.5 — Existencia de un refinamiento común proporciona $R$ que refina ambas particiones. Sus brechas no crecen (Teorema §21.2.8 — Monotonía de las sumas bajo refinamiento), por lo que

$$
U(f,R)-L(f,R)<\varepsilon/2,\qquad
U(g,R)-L(g,R)<\varepsilon/2.
$$

Aplicamos (21.5.9) **a esta misma partición**:

$$
0\le U(f+g,R)-L(f+g,R)<\varepsilon.
$$

El criterio de Darboux concluye que $f+g$ es integrable. No se ha escogido una sucesión de particiones; para cada precisión se usan dos testigos y un refinamiento finito.

Identifiquemos ahora la integral. Escribamos $F:=\int_a^b f$, $G:=\int_a^b g$ y $H:=\int_a^b(f+g)$, valores bien definidos en este punto. Por el encierro Proposición §21.4.4 — Encierro del valor integral y control por la brecha,

$$
L(f,R)+L(g,R)\le F+G\le U(f,R)+U(g,R).
$$

La desigualdad (21.5.8), unida al encierro de $H$, proporciona **sobre la misma partición**

$$
L(f,R)+L(g,R)\le L(f+g,R)\le H
\le U(f+g,R)\le U(f,R)+U(g,R).
$$

Ambos reales $H$ y $F+G$ pertenecen, por tanto, al intervalo cuyos extremos son $L(f,R)+L(g,R)$ y $U(f,R)+U(g,R)$. Su distancia satisface

$$
|H-(F+G)|\le[U(f,R)-L(f,R)]+[U(g,R)-L(g,R)]<\varepsilon.
$$

Esto vale para cualquier $\varepsilon>0$. Si $H\ne F+G$, tomar $\varepsilon=|H-(F+G)|/2>0$ da una contradicción. Queda probada (21.5.10). La igualdad integral es una **conclusión**, no una hipótesis introducida al construir la suma. $\square$

### Lema 21.5.5 — Efecto exacto de un escalar sobre las cotas y las sumas
Sean $f:I\to\mathbb R$ acotada, $\lambda\in\mathbb R$, $J\subseteq I$ no vacío y $P$ una partición. Si $\lambda\ge0$, entonces

$$
\boxed{m(\lambda f,J)=\lambda m(f,J),\quad M(\lambda f,J)=\lambda M(f,J),}
\tag{21.5.11}
$$

$$
\boxed{L(\lambda f,P)=\lambda L(f,P),\quad U(\lambda f,P)=\lambda U(f,P).}
\tag{21.5.12}
$$

Si $\lambda<0$, se intercambian el mínimo y el máximo:

$$
\boxed{m(\lambda f,J)=\lambda M(f,J),\quad M(\lambda f,J)=\lambda m(f,J),}
\tag{21.5.13}
$$

$$
\boxed{L(\lambda f,P)=\lambda U(f,P),\quad U(\lambda f,P)=\lambda L(f,P).}
\tag{21.5.14}
$$

En **todos** los casos,

$$
\boxed{U(\lambda f,P)-L(\lambda f,P)
=|\lambda|\,[U(f,P)-L(f,P)].}
\tag{21.5.15}
$$

**Demostración.**
Si $\lambda=0$, $(\lambda f)[J]=\{0\}$ y las cuatro cotas de (21.5.11) son cero. Si $\lambda>0$, $\lambda m(f,J)$ es cota inferior de $(\lambda f)[J]$. Cualquier otra cota inferior $d$ satisface $d/\lambda\le f(t)$ para todo $t\in J$; por maximalidad del ínfimo, $d/\lambda\le m(f,J)$, es decir, $d\le\lambda m(f,J)$. Así se obtiene el primer caso del ínfimo. La prueba para el supremo es dual.

Si $\lambda<0$, multiplicar $f(t)\le M(f,J)$ invierte la desigualdad: $\lambda M(f,J)\le\lambda f(t)$. Si $d$ es cualquier cota inferior de $(\lambda f)[J]$, al dividir $d\le\lambda f(t)$ por $\lambda<0$ resulta $f(t)\le d/\lambda$; como $M(f,J)$ es la menor cota superior, $M(f,J)\le d/\lambda$, y multiplicar por $\lambda$ muestra $d\le\lambda M(f,J)$. Ésta es la primera identidad de (21.5.13); la segunda se obtiene intercambiando cotas inferiores y superiores. La división sólo se efectuó en las ramas $\lambda\ne0$.

Sustituimos estas identidades locales en las definiciones de las sumas. Las propiedades de las sumas finitas permiten sacar el escalar **real fijo** fuera de la suma; si es negativo, además se invierten los papeles de las sumas extrema inferior y superior. Se obtienen (21.5.12) y (21.5.14). Restarlas en los dos casos, y recordar que $|\lambda|=\lambda$ para $\lambda\ge0$ y $|\lambda|=-\lambda$ para $\lambda<0$, produce (21.5.15). $\square$

### Teorema 21.5.6 — Homogeneidad y conservación de la integrabilidad
Si $f:I\to\mathbb R$ es integrable y $\lambda\in\mathbb R$, entonces $\lambda f$ es integrable y

$$
\boxed{\int_a^b(\lambda f)=\lambda\int_a^b f.}
\tag{21.5.16}
$$

**Demostración.**
La acotación de $\lambda f$ ya está demostrada. Si $\lambda=0$, la función es la constante nula y la proposición 21.5.1 determina tanto su integrabilidad como el valor cero de la integral. Supongamos $\lambda\ne0$ y fijemos $\varepsilon>0$. Como $|\lambda|>0$, podemos aplicar el criterio de Darboux a $f$ con la tolerancia positiva $\varepsilon/|\lambda|$. La partición testigo $P$ cumple

$$
U(\lambda f,P)-L(\lambda f,P)
=|\lambda|[U(f,P)-L(f,P)]<\varepsilon
$$

por (21.5.15). El criterio establece que $\lambda f$ es integrable.

Pongamos $F:=\int_a^b f$ y $H:=\int_a^b(\lambda f)$. Si $\lambda>0$, multiplicar $L(f,P)\le F\le U(f,P)$ por $\lambda$ y aplicar (21.5.12) sitúa $\lambda F$ entre $L(\lambda f,P)$ y $U(\lambda f,P)$. Si $\lambda<0$, el orden se invierte, y (21.5.14) da **el mismo encierro**. También $H$ pertenece a ese intervalo por Proposición §21.4.4 — Encierro del valor integral y control por la brecha. Para cada $\varepsilon>0$ disponemos, como acaba de demostrarse, de una partición cuya brecha para $\lambda f$ es menor que $\varepsilon$; luego

$$
|H-\lambda F|\le U(\lambda f,P)-L(\lambda f,P)<\varepsilon.
$$

La elección puntual $\varepsilon:=|H-\lambda F|/2$ contradice esta desigualdad si $H\ne\lambda F$. Así $H=\lambda F$ también para escalares negativos. $\square$

### Corolario 21.5.7 — Linealidad para combinaciones finitas de dos funciones
Si $f,g:I\to\mathbb R$ son integrables y $\alpha,\beta\in\mathbb R$, entonces la combinación puntual $\alpha f+\beta g$ es integrable y

$$
\boxed{\int_a^b(\alpha f+\beta g)
=\alpha\int_a^b f+\beta\int_a^b g.}
\tag{21.5.17}
$$

**Demostración.**
Por Teorema §21.5.6 — Homogeneidad y conservación de la integrabilidad, las funciones $\alpha f$ y $\beta g$ son integrables y sus integrales valen $\alpha\int_a^b f$ y $\beta\int_a^b g$. Aplicamos Teorema §21.5.4 — La suma de funciones integrables es integrable y su integral es aditiva a su suma. El tipado de la combinación puntual procede de Proposición §16.3.2 — Existencia y tipado de las operaciones puntuales; no hay una suma formal de funciones con dominios diferentes. La sustitución de las dos identidades demuestra (21.5.17). $\square$

### Corolario 21.5.8 — Positividad y estimaciones por cotas constantes
Si $f:I\to\mathbb R$ es integrable y $A,B\in\mathbb R$ satisfacen $A\le f(t)\le B$ para todo $t\in I$, entonces

$$
\boxed{A(b-a)\le\int_a^b f\le B(b-a).}
\tag{21.5.18}
$$

En particular, $f(t)\ge0$ para todo $t$ implica $\int_a^b f\ge0$; y si $f(t)=g(t)$ para todo $t\in I$ y ambas son integrables, sus integrales coinciden.

**Demostración.**
Las funciones constantes $\mathbf A$ y $\mathbf B$ son integrables y sus integrales son $A(b-a)$ y $B(b-a)$ por Proposición §21.5.1 — Acotación de las operaciones y cálculo de las constantes. Aplicar la comparación integral Proposición §21.5.2 — Orden puntual, sumas e integral a $\mathbf A\le f\le\mathbf B$ da (21.5.18). La positividad es el caso $A=0$; la igualdad puntual implica ambas comparaciones $f\le g$ y $g\le f$, y la antisimetría del orden real identifica los valores integrales. $\square$

**Lectura estructural.** Las funciones integrables sobre $I$ están cerradas bajo suma y multiplicación por escalares y, con las operaciones puntuales ya construidas, forman un espacio vectorial real. La integral es un funcional lineal que preserva el orden. Esta conclusión resume los teoremas anteriores; no introduce un nuevo objeto ni importa resultados de teoría funcional. La igualdad de los extremos de Darboux se conserva porque las brechas se controlan cuantitativamente sobre **un refinamiento común**, no porque los extremos locales sean aditivos.

**Transición.** Las propiedades establecidas se refieren a un mismo intervalo fijo $[a,b]$ con $a<b$. La siguiente unidad, §21.6, deberá demostrar la aditividad respecto de la subdivisión del intervalo, cuidando que la restricción de una función integrable a cada subintervalo sea integrable, y fijar separadamente la convención del caso degenerado. No hemos utilizado primitiva, derivada ni el teorema fundamental del cálculo.
