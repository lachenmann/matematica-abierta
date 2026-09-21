## 18.6. Heine–Cantor: la compacidad uniformiza la continuidad {#sec-ta-18-6}

En §17.6 distinguimos dos órdenes de cuantificadores: la continuidad puntual permite un radio diferente en cada centro, mientras que la continuidad uniforme exige un único radio para todos los pares de puntos del dominio. La compacidad permite pasar de la primera condición a la segunda. La dificultad fundacional consiste en que **no podemos escoger sin más un radio para cada punto de un conjunto arbitrario**. En lugar de postular una función de radios, reuniremos todos los pares centro-radio que satisfacen la condición local; esa familia existe mediante Separación y será una cubierta abierta indexada. La compacidad reducirá la familia a una cantidad finita de pares, cuyos radios sí tienen un mínimo positivo.

### Teorema 18.6.1 — Heine–Cantor en la recta
Sean $D\subseteq\mathbb R$, $f:D\to\mathbb R$ y $K\subseteq D$ un conjunto compacto. Si $f$ es continua en cada punto de $K$ **relativamente al dominio $D$**, entonces la restricción tipada $h:=f\upharpoonright K:K\to\mathbb R$ es uniformemente continua en $K$. En particular, si $f:K\to\mathbb R$ es continua en todo $K$ compacto, entonces es uniformemente continua:

$$
\boxed{\forall\varepsilon>0\ \exists\delta>0\ \forall x,y\in K:\quad
|x-y|<\delta\Longrightarrow |f(x)-f(y)|<\varepsilon.}
$$

No se exige que $D$ sea compacto ni que $K$ sea un intervalo. La afirmación incluye el compacto vacío.

**Demostración.**
**1. Reducción al dominio compacto y caso vacío.** La restricción $h=f\upharpoonright K$ existe como función $K\to\mathbb R$ por Definición §1.3.1 — Restricción de una función. La continuidad de $f$ en cada punto de $K$, con argumentos permitidos en $D$, implica la de $h$ en cada punto de $K$ porque todo $z\in K$ pertenece a $D$ y $h(z)=f(z)$. Fijemos $\varepsilon>0$. Si $K=\varnothing$, el número $\delta=1$ verifica la definición Definición §17.6.1 — Continuidad uniforme relativa a un dominio por vacuidad; no hacen falta cubiertas ni mínimos. En adelante supongamos $K\ne\varnothing$.

**2. La familia canónica de todos los radios admisibles.** Sea $\mathbb R_{>0}:=\{r\in\mathbb R:r>0\}$, subconjunto existente por Separación. Construyamos el siguiente conjunto de índices **sin escoger una aplicación $a\mapsto r_a$**:

$$
\begin{aligned}
I_{\varepsilon}:=\bigl\{\langle a,r\rangle\in K\times\mathbb R_{>0}:\quad
&\forall z\in K,\\[-2pt]
& |z-a|<2r\Longrightarrow |h(z)-h(a)|<\varepsilon/2\bigr\}.
\end{aligned}
$$

El producto $K\times\mathbb R_{>0}$ es un conjunto; su subconjunto $I_\varepsilon$ existe por Separación, pues la condición escrita es una fórmula cuyos cuantificadores sobre puntos están acotados por $K$. Para cada índice $i=\langle a,r\rangle\in I_\varepsilon$, definamos el abierto ambiente

$$
U_i:=B_r(a)=\{z\in\mathbb R:|z-a|<r\}.
$$

La unicidad de las componentes del par ordenado hace que la regla $i\mapsto U_i$ sea funcional. Su grafo se obtiene por Separación en $I_\varepsilon\times\mathcal P(\mathbb R)$: queda construida una función tipada $U:I_\varepsilon\to\mathcal P(\mathbb R)$. Cada miembro es abierto por la definición de bola y de abierto, ya cerradas en el capítulo 15.

**3. Verificación de la cobertura, punto por punto pero sin elección simultánea.** Sea $a\in K$ arbitrario. Por la continuidad de $h$ en $a$ aplicada a la tolerancia positiva $\varepsilon/2$, **existe** $\eta>0$ tal que

$$
\forall z\in K:\quad |z-a|<\eta\Longrightarrow |h(z)-h(a)|<\varepsilon/2.
$$

Para este punto fijo, el radio $r:=\eta/2>0$ satisface $2r=\eta$, de modo que $\langle a,r\rangle\in I_\varepsilon$ y $a\in U_{\langle a,r\rangle}$. Como $a$ era arbitrario, hemos probado la cobertura

$$
K\subseteq\bigcup_{i\in I_\varepsilon}U_i.
$$

Se ha demostrado $\forall a\in K\ \exists r>0$ en una relación ya definida; **no** se ha convertido esta afirmación en una función global que seleccione radios. Además, como $K\ne\varnothing$, toda subcubierta de $K$ debe tener algún índice.

**4. Finitud y mínimo positivo.** Por compacidad (Definición §18.1.4 — Compacidad por cubiertas abiertas), existe un **solo** subconjunto finito $J\subseteq I_\varepsilon$ tal que

$$
K\subseteq\bigcup_{i\in J}U_i.
$$

Como $K\ne\varnothing$, $J\ne\varnothing$. Para $i=\langle a,r\rangle\in J$ definamos $\rho(i):=r$. La regla de segunda proyección, restringida a $J$, constituye una función tipada $\rho:J\to\mathbb R_{>0}$ mediante su grafo; sus valores son estrictamente positivos. El lema finito Lema §18.3.1 — Mínimo positivo de una familia finita no vacía proporciona un **mínimo alcanzado** de estos radios:

$$
\delta:=\min\{\rho(i):i\in J\}>0,
\qquad\delta\le\rho(i)\quad(i\in J).
$$

Se toma el mínimo de la *familia finita concreta* entregada por una sola aplicación de compacidad; no se infiere que el ínfimo de una familia infinita de radios positivos sea positivo.

**5. Un mismo radio para todos los pares.** Sean $x,y\in K$ tales que $|x-y|<\delta$. La cobertura finita proporciona, para este $x$, **un** índice $i=\langle a,r\rangle\in J$ con $x\in U_i$, es decir, $|x-a|<r$. Puesto que $r=\rho(i)\ge\delta$, la desigualdad triangular da

$$
|y-a|\le |y-x|+|x-a|<\delta+r\le 2r.
$$

La propiedad que define $i\in I_\varepsilon$ puede aplicarse tanto a $x$ (porque $|x-a|<r<2r$) como a $y$ (porque $|y-a|<2r$). Por consiguiente,

$$
|h(x)-h(a)|<\varepsilon/2,
\qquad |h(y)-h(a)|<\varepsilon/2.
$$

Una segunda aplicación de la desigualdad triangular concluye

$$
|h(x)-h(y)|\le|h(x)-h(a)|+|h(a)-h(y)|
<\varepsilon/2+\varepsilon/2=\varepsilon.
$$

El número $\delta$ se fijó **antes** de considerar los puntos $x,y$ y sólo depende de $\varepsilon$, la función y el compacto fijados. Es exactamente el orden de cuantificadores de Definición §17.6.1 — Continuidad uniforme relativa a un dominio. El argumento no utiliza compacidad secuencial ni `\mathrm{CC}(\mathbb R)` y no supone ningún principio de elección. $\square$

**Lectura de la demostración.** La cubierta está formada por bolas pequeñas $B_r(a)$, pero cada índice conserva información adicional: la estimación de continuidad vale en la bola **dos veces mayor** $B_{2r}(a)\cap K$. El mínimo de los radios de una subcubierta finita asegura que dos puntos suficientemente próximos, aunque su centro varíe, se comparan con un mismo $a$. Indexar por **todos** los pares admisibles, y no por una elección de un radio por punto, es lo que mantiene válida la prueba en ZF.

### Corolario 18.6.2 — Funciones continuas sobre cerrados acotados e intervalos cerrados
Si $K\subseteq\mathbb R$ es cerrado y acotado, toda función continua $f:K\to\mathbb R$ es uniformemente continua. En particular, si $a\le b$, toda función continua $f:[a,b]\to\mathbb R$ es uniformemente continua en $[a,b]$. Lo mismo vale para la restricción a $K$ de una función continua en un dominio $D$ que contiene a $K$.

**Demostración.**
Heine–Borel Teorema §18.3.4 — Heine–Borel en la recta real convierte la cerradura y acotación de $K$ en compacidad. Apliquemos Teorema §18.6.1 — Heine–Cantor en la recta a $f$ (o a su restricción tipada, si $f$ está definida sobre un dominio mayor). Si $a\le b$, el teorema Teorema §18.2.1 — Todo intervalo cerrado y acotado es compacto aporta directamente la compacidad de $[a,b]$ y de nuevo se aplica Heine–Cantor. El conjunto vacío no requiere excepción: la continuidad uniforme es vacía en ese caso. $\square$

**La acotación sola no basta.** El recíproco $x\mapsto1/x$ es continuo pero no uniformemente continuo en $(0,1]$, según Proposición §17.6.7 — Dos funciones continuas que no son uniformemente continuas: este dominio está acotado pero no es cerrado. **La cerradura sola tampoco basta:** $x\mapsto x^2$ es continuo pero no uniformemente continuo en $\mathbb R$, también por Proposición §17.6.7 — Dos funciones continuas que no son uniformemente continuas. El teorema garantiza un radio uniforme mediante ambas condiciones, sin afirmar que sean necesarias para *cada función*; por ejemplo, la identidad es uniformemente continua en toda la recta.

### Corolario 18.6.3 — Uniformidad de los cocientes sin ceros en un compacto
Sean $D\subseteq\mathbb R$, $f,g:D\to\mathbb R$ continuas y $K\subseteq D$ compacto **no vacío**. Supongamos que $g(x)\ne0$ para todo $x\in K$. Entonces existe $m>0$ tal que $|g(x)|\ge m$ en $K$ y las funciones tipadas

$$
\left(\frac1g\right)\!\upharpoonright K:K\to\mathbb R,
\qquad
\left(\frac fg\right)\!\upharpoonright K:K\to\mathbb R
$$

son uniformemente continuas. Las restricciones aquí se toman de las funciones recíproca y cociente cuyos dominios efectivos en $D$ son los puntos donde $g\ne0$; ambas restricciones tienen exactamente el dominio $K$.

**Demostración.**
Las restricciones $f_K:=f\upharpoonright K$ y $g_K:=g\upharpoonright K$, ambas funciones $K\to\mathbb R$, son continuas por herencia de continuidad. El corolario Corolario §18.5.5 — Separación uniforme respecto del cero, aplicado con denominador $g_K$ y numerador $f_K$, proporciona $m>0$ con $|g_K(x)|\ge m$ para todo $x\in K$. Heine–Cantor Teorema §18.6.1 — Heine–Cantor en la recta muestra que $f_K$ y $g_K$ son uniformemente continuas. Asimismo, Corolario §18.5.2 — La imagen continua es cerrada y acotada asegura que $f_K$ está acotada en $K$. Se cumplen, por tanto, las hipótesis exactas del apartado de cocientes de Teorema §17.6.4 — Operaciones algebraicas uniformes: hipótesis globales exactas: sobre el conjunto efectivo $\{x\in K:g_K(x)\ne0\}=K$, tanto $1/g_K$ como $f_K/g_K$ son uniformemente continuas. Sus valores, dominios y codominios coinciden con los de las restricciones enunciadas, de modo que coinciden como **funciones tipadas**, no sólo punto a punto. $\square$

**Transición.** La compacidad ya proporciona tres resultados globales distintos: imágenes compactas, extremos alcanzados y continuidad uniforme. Ninguno afirma todavía que el conjunto de partida sea indivisible. Para llegar al teorema del valor intermedio habrá que introducir la conexidad de un subconjunto de la recta y demostrar que sus conjuntos conexos son precisamente los intervalos.
