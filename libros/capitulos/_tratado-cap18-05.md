## 18.5. Imágenes continuas de compactos y valores extremos {#sec-ta-18-5}

Una función continua transforma información local sobre abiertos del codominio en información local sobre su dominio. La compacidad convierte esa correspondencia en un principio global: si una cubierta cubre los valores de la función, sus preimágenes cubren los argumentos, y bastan finalmente **los mismos índices finitos** para cubrir unos y otros. Debemos respetar que las preimágenes son abiertas *relativas* al dominio, mientras que nuestra definición de compacidad utiliza abiertos de toda la recta.

### Teorema 18.5.1 — La imagen continua de un compacto es compacta
Sea $f:D\to\mathbb R$ una función continua en todos los puntos de $D\subseteq\mathbb R$. Si $K\subseteq D$ es compacto, su imagen $f[K]\subseteq\mathbb R$ es compacta. La afirmación comprende $K=\varnothing$ y no exige que $D$ sea abierto, cerrado o compacto.

**Demostración.**
**1. Una cubierta de la imagen.** Fijemos una cubierta abierta *arbitraria* $U:I\to\mathcal P(\mathbb R)$ de $f[K]$. Así, todos los $U_i$ son abiertos en $\mathbb R$ y

$$
f[K]\subseteq\bigcup_{i\in I}U_i.
$$

La imagen existe por Definición §0.6.9 — Imagen y preimagen: concretamente, $f[K]=\{y\in\mathbb R:\exists x\in K,\ f(x)=y\}$. No hemos sustituido el codominio de $f$ por su imagen: $f$ sigue siendo la función tipada $D\to\mathbb R$.

**2. Preimágenes relativas y levantamiento canónico.** Sea $h:=f\upharpoonright K:K\to\mathbb R$, la restricción en el sentido de Definición §1.3.1 — Restricción de una función. Es continua por Corolario §17.4.6 — Clausura global, restricciones y cocientes. Para cada $i\in I$ definamos

$$
A_i:=h^{-1}[U_i]=\{x\in K:f(x)\in U_i\}.
$$

Por Teorema §17.3.4 — Caracterización global por preimágenes de abiertos, $A_i$ es abierto **relativo a $K$**. La compacidad de $K$ implica que $K$ es cerrado en $\mathbb R$ (Proposición §18.3.3 — Todo compacto de la recta es cerrado). En consecuencia, el conjunto determinado sin ninguna selección

$$
\boxed{W_i:=(\mathbb R\setminus K)\cup A_i}
$$

es abierto en $\mathbb R$. En efecto, un punto de $\mathbb R\setminus K$ dispone de una bola contenida en ese complemento. Si $x\in A_i$, la apertura relativa proporciona, para este índice fijo, un abierto ambiente $O$ con $A_i=K\cap O$; por tanto, $x\in O$ y $O\subseteq(\mathbb R\setminus K)\cup A_i=W_i$. De esta manera cada punto de $W_i$ tiene un entorno abierto contenido en $W_i$, sin haber seleccionado simultáneamente un abierto $O_i$ para todos los índices. Además,

$$
K\cap W_i=A_i.
$$

Los $A_i$ y $W_i$ son subconjuntos únicos de $\mathbb R$ dados por fórmulas con parámetros $h,U,i,K$. Por Separación en $I\times\mathcal P(\mathbb R)$ sus pares de valores constituyen **funciones tipadas** $A,W:I\to\mathcal P(\mathbb R)$. No se aplica un principio de elección para construir estas familias.

**3. Aplicación de la compacidad y devolución de los índices.** Sea $x\in K$. Como $f(x)\in f[K]$, la cubierta inicial suministra un índice $i\in I$ con $f(x)\in U_i$; luego $x\in A_i\subseteq W_i$. Por ello

$$
K\subseteq\bigcup_{i\in I}W_i.
$$

La compacidad de $K$ entrega **un único conjunto finito** $J\subseteq I$ tal que $K\subseteq\bigcup_{j\in J}W_j$. Tomemos ahora un $y\in f[K]$ arbitrario. Por definición de imagen existe $x\in K$ con $y=f(x)$; la cobertura finita de $K$ proporciona algún $j\in J$ con $x\in W_j$. Como $x\in K$, la identidad $K\cap W_j=A_j$ implica $x\in A_j$, es decir, $y=f(x)\in U_j$. Hemos demostrado

$$
\boxed{f[K]\subseteq\bigcup_{j\in J}U_j,\qquad J\subseteq I\text{ finito}.}
$$

La familia restringida $U\upharpoonright J$ es por tanto una subcubierta finita de la cubierta inicial. Como ésta era arbitraria, $f[K]$ es compacto. Si $K=\varnothing$, también $f[K]=\varnothing$ y sirve $J=\varnothing$; el argumento general sigue siendo válido, incluso cuando $I=\varnothing$. La prueba no usa la compacidad secuencial ni ninguna forma de elección. $\square$

**Lectura de la prueba.** No basta declarar que las preimágenes de los abiertos son abiertas: sólo sabemos que son abiertas respecto de $K$. El complemento abierto del compacto permite convertirlas mediante una fórmula en abiertos ambientales, **sin cambiar el conjunto de índices**. La subcubierta finita de los argumentos se convierte así en una subcubierta finita de los valores.

### Corolario 18.5.2 — La imagen continua es cerrada y acotada
Bajo las hipótesis del teorema anterior, $f[K]$ es cerrado en $\mathbb R$ y acotado inferior y superiormente. En particular, si $K\ne\varnothing$, existen $L,H\in\mathbb R$ tales que

$$
\forall x\in K:\quad L\le f(x)\le H.
$$

**Demostración.**
Por Teorema §18.5.1 — La imagen continua de un compacto es compacta, $f[K]$ es compacto. Sus propiedades de cerradura y acotación son, respectivamente, Proposición §18.3.3 — Todo compacto de la recta es cerrado y Proposición §18.3.2 — Todo compacto de la recta es acotado, o conjuntamente la dirección pertinente de Heine–Borel Teorema §18.3.4 — Heine–Borel en la recta real. Las cotas obtenidas se aplican a $f(x)$ porque $f(x)\in f[K]$ para cada $x\in K$. La imagen vacía también es cerrada y acotada, pero no se le atribuye punto de máximo o mínimo. $\square$

### Lema 18.5.3 — Los extremos de un compacto no vacío le pertenecen
Si $S\subseteq\mathbb R$ es compacto y no vacío, existen $m,M\in S$ tales que

$$
\boxed{m=\inf S=\min S,\qquad M=\sup S=\max S.}
$$

**Demostración.**
Por Proposición §18.3.2 — Todo compacto de la recta es acotado, $S$ tiene cotas inferior y superior. Como es no vacío y $\mathbb R$ es un cuerpo ordenado completo (Teorema §12.8.1 — Existencia y caracterización única de la completación ordenada de $\mathbb Q$), la propiedad del supremo (Definición §4.6.1 — Propiedad del supremo y cuerpo ordenado completo) proporciona $M=\sup S$, y la propiedad del ínfimo (Proposición §4.6.2 — La propiedad del supremo implica la propiedad del ínfimo) proporciona $m=\inf S$. Se cumplen $m\le y\le M$ para todo $y\in S$. Falta probar que ambos extremos **pertenecen** al conjunto.

Supongamos $M\notin S$. El conjunto $S$ es cerrado por Proposición §18.3.3 — Todo compacto de la recta es cerrado; el criterio exterior Proposición §15.3.6 — Criterio de cerradura mediante puntos exteriores proporciona $r>0$ tal que

$$
B_r(M)\cap S=\varnothing.
$$

Como $M-r/2<M$, ese número no puede ser cota superior de $S$: si lo fuese, contradiría la minimalidad de $M$. Por tanto existe $y\in S$ con $y>M-r/2$. A la vez $y\le M$, de donde

$$
|y-M|=M-y<r/2<r.
$$

Esto coloca $y$ en $B_r(M)\cap S$, contradicción. Luego $M\in S$ y, siendo cota superior, $M=\max S$.

Si $m\notin S$, existe de modo análogo un radio $s>0$ con $B_s(m)\cap S=\varnothing$. La desigualdad $m+s/2>m$ impide que $m+s/2$ sea cota inferior, pues $m$ es la mayor de ellas. Existe entonces $z\in S$ con $z<m+s/2$; como $m\le z$, tenemos $|z-m|=z-m<s/2<s$, contradicción. En consecuencia $m\in S$ y $m=\min S$. Sólo se han usado dos argumentos existenciales independientes y ningún selector para una colección de conjuntos. $\square$

### Teorema 18.5.4 — Teorema del valor extremo: Weierstrass
Sea $f:D\to\mathbb R$ continua en $D$ y sea $K\subseteq D$ **compacto y no vacío**. Entonces existen $x_-,x_+\in K$ tales que

$$
\boxed{\forall x\in K:\quad f(x_-)\le f(x)\le f(x_+).}
$$

Equivalentemente, la restricción $f\upharpoonright K:K\to\mathbb R$ **alcanza** sus valores mínimo y máximo sobre $K$. No se afirma que los puntos $x_-$ y $x_+$ sean únicos ni que sean distintos.

**Demostración.**
Al ser $K\ne\varnothing$, fijar un punto $a\in K$ muestra que $f(a)\in f[K]$, de modo que la imagen tampoco es vacía. Es compacta por Teorema §18.5.1 — La imagen continua de un compacto es compacta. El lema anterior proporciona valores $m,M\in f[K]$ con

$$
m\le y\le M\qquad(y\in f[K]).
$$

Por la **definición de imagen**, $m\in f[K]$ significa que existe un punto $x_-\in K$ tal que $f(x_-)=m$; análogamente, $M\in f[K]$ proporciona $x_+\in K$ con $f(x_+)=M$. Para todo $x\in K$, el valor $f(x)$ pertenece a $f[K]$, luego

$$
f(x_-)=m\le f(x)\le M=f(x_+).
$$

La prueba extrae dos testigos de dos afirmaciones existenciales concretas; no selecciona una preimagen para **cada** valor de $f[K]$. Si $K$ fuese vacío no existirían $x_-,x_+$: por eso la no vaciedad es una hipótesis esencial, no una convención. $\square$

**Caso fundamental.** Cuando $a\le b$, el intervalo $[a,b]$ es compacto por Teorema §18.2.1 — Todo intervalo cerrado y acotado es compacto. Si además $a\le b$ garantiza que contiene al menos $a$, toda función continua $f:[a,b]\to\mathbb R$ alcanza máximo y mínimo. No se exige continuidad fuera del intervalo ni se atribuyen necesariamente esos extremos a los puntos $a,b$.

### Corolario 18.5.5 — Separación uniforme respecto del cero
Sea $K\subseteq\mathbb R$ compacto **no vacío**, y sean $f,g:K\to\mathbb R$ continuas. Si $f(x)\ne0$ para todo $x\in K$, existe un real $m>0$ tal que

$$
\boxed{\forall x\in K:\quad |f(x)|\ge m>0.}
$$

En consecuencia, $1/f:K\to\mathbb R$ es una función bien definida y acotada por $|(1/f)(x)|\le1/m$. Además, $g/f:K\to\mathbb R$ es continua y acotada. Cuando $f(x)>0$ en todo $K$, la primera desigualdad puede escribirse $f(x)\ge m$.

**Demostración.**
La operación puntual de valor absoluto, existente en Proposición §16.3.2 — Existencia y tipado de las operaciones puntuales, da $|f|:K\to\mathbb R$, continua por Teorema §17.4.3 — Estabilidad de la continuidad bajo operaciones algebraicas y valor absoluto. Apliquemos el teorema del valor extremo a esta función: existe $x_0\in K$ tal que

$$
m:=|f(x_0)|=\min\{|f(x)|:x\in K\}.
$$

La hipótesis $f(x_0)\ne0$ implica $m>0$. Por minimalidad, $|f(x)|\ge m$ para todo $x\in K$. Como no hay ceros en $K$, el dominio efectivo de $1/f$ y de $g/f$ definido en §16.3.2 es exactamente $K$, no un subconjunto propio que deba ser identificado con él. La continuidad de ambos cocientes resulta de Teorema §17.4.4 — Continuidad del recíproco y del cociente en sus dominios efectivos. Por las reglas de valor absoluto y el orden de inversos positivos,

$$
\left|\frac1{f(x)}\right|=\frac1{|f(x)|}\le\frac1m.
$$

Finalmente, Corolario §18.5.2 — La imagen continua es cerrada y acotada aplicado a $g$ proporciona una cota $H>0$ con $|g(x)|\le H$ para todo $x\in K$ (si las dos cotas de la imagen son $L_0,H_0$, basta tomar $H=|L_0|+|H_0|+1$). Entonces $|g(x)/f(x)|\le H/m$ para todo $x\in K$, y el cociente es acotado. Si $f>0$, su valor absoluto coincide con $f$, lo que da la formulación final. $\square$

**Transición.** La imagen continua de un compacto es compacta; por ello hay cotas y, si no está vacía, **valores extremos alcanzados**. El siguiente resultado global relacionará otra vez continuidad y compacidad, pero ya no buscará un valor extremo: demostrará que, sobre un compacto, los radios de continuidad puntual se pueden reemplazar por un radio que funciona simultáneamente para todos sus puntos (teorema de Heine–Cantor).
