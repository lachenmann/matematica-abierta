## 18.3. Teorema de Heine–Borel: equivalencia entre compacidad, cerradura y acotación {#sec-ta-18-3}

Hemos demostrado la compacidad de $[a,b]$ a partir del supremo (§18.2.1) y su transmisión a los cerrados relativos (§18.2.2). La recíproca exige trabajo: que un conjunto resista todas las cubiertas abiertas debe obligarlo, simultáneamente, a no escapar hacia infinito y a contener todos sus puntos de adherencia. Probaremos ambas necesidades sin recurrir a sucesiones ni a las equivalencias que todavía están pendientes. Aquí, «acotado» significa que el conjunto posee una cota inferior y una cota superior reales, conforme a la terminología de Definición §0.7.4 — Cotas superiores e inferiores.

### Lema 18.3.1 — Mínimo positivo de una familia finita no vacía
Sean $J$ un conjunto finito no vacío y $r:J\to\mathbb R$ una función dada tal que $r(j)>0$ para todo $j\in J$. Entonces existe $j_*\in J$ tal que

$$
\boxed{0<r(j_*)\le r(j)\quad\text{para todo }j\in J.}
$$

En particular, el real $\delta:=r(j_*)$ es positivo y sirve simultáneamente como cota inferior de los valores de la familia.

**Demostración.**
Por finitud, fijemos una biyección $e:n\to J$ para algún $n\in\mathbb N$. La no vaciedad de $J$ impide $n=0$; el teorema del predecesor permite escribir $n=k+1$. El elemento $j_0:=e(0)$ pertenece a $J$ y $r(j_0)>0$.

Recorramos, mediante inducción finita, los prefijos no vacíos $e[\{0,\ldots,h\}]$ de la enumeración, para $0\le h<n$. La propiedad inductiva afirma que existe un elemento $j_h$ de ese prefijo cuyo valor es menor o igual que el de todos sus miembros. El caso $h=0$ queda acreditado por $e(0)$. Si existe tal $j_h$ y $h+1<n$, comparamos los dos reales $r(j_h)$ y $r(e(h+1))$. Cuando el segundo es menor, el mínimo del prefijo ampliado lo alcanza $e(h+1)$; en caso contrario lo sigue alcanzando $j_h$. Se obtiene así el paso inductivo, sin escoger elementos de ninguna familia de conjuntos: sólo se compara un par de valores de una función ya dada. En el último prefijo, que es todo $J$, existe un minimizador $j_*$. Como $j_*\in J$, la hipótesis da $r(j_*)>0$. Las desigualdades restantes se obtienen de su minimalidad. $\square$

**Observación.** La finitud es esencial. Una familia infinita de reales positivos puede tener ínfimo cero y no proporcionar un radio común positivo. El lema únicamente afirma la existencia de un mínimo para una familia finita dada; no construye una selección simultánea de mínimos para una colección arbitraria de familias.

### Proposición 18.3.2 — Todo compacto de la recta es acotado
Si $K\subseteq\mathbb R$ es compacto, entonces existen $a,b\in\mathbb R$ tales que

$$
\boxed{K\subseteq[a,b].}
$$

En particular, $K$ está acotado inferior y superiormente.

**Demostración.**
Si $K=\varnothing$, bastan $a=b=0_{\mathbb R}$: el vacío está contenido en cualquier intervalo. Supongamos $K\ne\varnothing$.

Reutilicemos la familia explícita de §18.1.8,

$$
U_n=\bigl(-\nu_{\mathbb R}(n+1),\nu_{\mathbb R}(n+1)\bigr),
\qquad n\in\mathbb N.
$$

Proposición §18.1.8 — La recta real no es compacta ya establece que todos sus miembros son abiertos y que su unión es $\mathbb R$. Por tanto, esta misma familia es una cubierta abierta de $K$. Su compacidad proporciona un subconjunto finito $J\subseteq\mathbb N$ tal que

$$
K\subseteq\bigcup_{j\in J}U_j.
$$

El conjunto $J$ no puede ser vacío, ya que su unión sería vacía y $K$ no lo es. El argumento de máximo de índices finitos desarrollado en la prueba de Proposición §18.1.8 — La recta real no es compacta proporciona $m=\max J$. Para cada $j\in J$, el orden de los numerales implica $U_j\subseteq U_m$; así,

$$
K\subseteq U_m\subseteq
\left[-\nu_{\mathbb R}(m+1),\nu_{\mathbb R}(m+1)\right].
$$

Los dos extremos son reales y constituyen las cotas requeridas. La elección de $J$ es precisamente el testigo existencial de la compacidad para una sola cubierta fijada; ni se escoge un miembro para cada punto de $K$ ni se emplea elección numerable. $\square$

### Proposición 18.3.3 — Todo compacto de la recta es cerrado
Si $K\subseteq\mathbb R$ es compacto, entonces $K$ es cerrado en la recta; equivalentemente, $\mathbb R\setminus K$ es abierto.

**Demostración.**
Si $K=\varnothing$, su complemento es toda $\mathbb R$, abierto porque para cada $x\in\mathbb R$ la bola $B_1(x)$ está contenida en él. En adelante supongamos $K\ne\varnothing$ y fijemos un punto arbitrario $x\in\mathbb R\setminus K$. Demostraremos que existe $\delta>0$ con $B_\delta(x)\cap K=\varnothing$; ése es el criterio de cerrado de Proposición §15.3.6 — Criterio de cerradura mediante puntos exteriores.

**1. Cubierta canónica de $K$.** Para cada $y\in K$ se tiene $y\ne x$, luego $|x-y|>0$. Definamos de manera unívoca

$$
r_y:=\frac{|x-y|}{3}>0,
\qquad U_y:=B_{r_y}(y).
$$

El número $3$ designa aquí el numeral real positivo $\nu_{\mathbb R}(3)$. Las fórmulas determinan, por Separación en $K\times\mathbb R$ y $K\times\mathcal P(\mathbb R)$, funciones tipadas $r:K\to\mathbb R$ y $U:K\to\mathcal P(\mathbb R)$. No hemos elegido un radio para cada $y$: cada radio es una expresión funcional de $x$ e $y$.

Todas las bolas $U_y$ son abiertas por Teorema §15.2.5 — Toda bola abierta es un conjunto abierto; además $y\in U_y$, por lo que

$$
K\subseteq\bigcup_{y\in K}U_y.
$$

La compacidad de $K$ da un conjunto finito $J\subseteq K$ con $K\subseteq\bigcup_{y\in J}U_y$. Como $K$ es no vacío, necesariamente $J$ también lo es.

**2. Un radio común obtenido por finitud.** Apliquemos Lema §18.3.1 — Mínimo positivo de una familia finita no vacía a la restricción $r\upharpoonright J:J\to\mathbb R$. Existe $y_*\in J$ tal que, con

$$
\delta:=r_{y_*}>0,
\qquad \delta\le r_y\quad(y\in J),
$$

la bola $B_\delta(x)$ resulta disjunta de todos los miembros $U_y$ que forman la subcubierta finita. En efecto, si existieran $z\in B_\delta(x)\cap U_y$ para algún $y\in J$, la desigualdad triangular daría

$$
|x-y|\le|x-z|+|z-y|
<\delta+r_y\le2r_y<3r_y=|x-y|,
$$

una contradicción. Como $K\subseteq\bigcup_{y\in J}U_y$, obtenemos

$$
\boxed{B_\delta(x)\cap K=\varnothing.}
$$

El punto $x$ era arbitrario en el complemento; éste es abierto y $K$ es cerrado. Se ha utilizado una única subcubierta finita para cada $x$ fijado, dentro de una demostración existencial; no se ha formado una función que elija subcubiertas o radios para todos los puntos exteriores. $\square$

**Sentido geométrico.** Fuera de un compacto, cada punto está separado de él por una bola entera. La distancia al conjunto no se ha definido ni se ha supuesto que alcance un mínimo; el margen positivo resulta sólo de una cubierta canónica y de la finitud de una subcubierta.

### Teorema 18.3.4 — Heine–Borel en la recta real
Para todo subconjunto $K\subseteq\mathbb R$ son equivalentes:

1. $K$ es compacto según la definición por cubiertas abiertas Definición §18.1.4 — Compacidad por cubiertas abiertas.
2. $K$ es cerrado en $\mathbb R$ y acotado inferior y superiormente.

En símbolos,

$$
\boxed{K\text{ compacto}\iff
\bigl(K\text{ cerrado en }\mathbb R\bigr)
\land\bigl(K\text{ acotado}\bigr).}
$$

**Demostración.**
**Compacidad $\Rightarrow$ cerradura y acotación.** Si $K$ es compacto, Proposición §18.3.2 — Todo compacto de la recta es acotado proporciona cotas reales inferior y superior, y Proposición §18.3.3 — Todo compacto de la recta es cerrado demuestra que $K$ es cerrado en $\mathbb R$. Ambas propiedades quedan acreditadas sin ninguna equivalencia secuencial.

**Cerradura y acotación $\Rightarrow$ compacidad.** Supongamos que $K$ es cerrado y acotado. Si $K=\varnothing$, es compacto por Proposición §18.1.5 — El vacío y los singletons son compactos. Si $K\ne\varnothing$, la acotación proporciona reales $a,b$ tales que $a\le x\le b$ para todo $x\in K$. Fijando un único $x_0\in K$, se sigue $a\le x_0\le b$ y, por tanto, $a\le b$. De aquí,

$$
K\subseteq[a,b],\qquad K=[a,b]\cap K.
$$

Por Teorema §18.2.1 — Todo intervalo cerrado y acotado es compacto, el intervalo $[a,b]$ es compacto. Como $K$ es cerrado en $\mathbb R$, la igualdad anterior lo presenta como un cerrado relativo de $[a,b]$ conforme a Definición §17.3.1 — Abiertos y cerrados relativos a un subconjunto de la recta y Proposición §17.3.2 — Criterio por bolas y representación de los cerrados relativos. Aplicando Proposición §18.2.2 — Un cerrado relativo de un compacto es compacto, concluimos que $K$ es compacto.

Se han demostrado ambas direcciones y los casos vacíos. El nombre *Heine–Borel* designa aquí esta caracterización obtenida como teorema, no una nueva definición de compacidad. $\square$

**Consecuencias para la lectura.** El intervalo abierto $(0,1)$ es acotado pero no cerrado y, por este teorema, no es compacto; $\mathbb R$ es cerrado pero no acotado y tampoco es compacto. Un conjunto cerrado y acotado de la recta puede estar formado por varias piezas y no necesita ser un intervalo: la compacidad no implica conexidad. Estos contrastes no introducen ningún resultado de conexidad antes de su definición.

**Transición.** Heine–Borel proporciona una caracterización mediante el orden y la topología. La próxima unidad examinará otra perspectiva: qué puede afirmarse de las sucesiones contenidas en un compacto y cómo se relaciona esa propiedad con Bolzano–Weierstrass, sin convertir un criterio secuencial condicional bajo elección numerable en un resultado incondicional.
