## 19.3. La derivada como coeficiente de la aproximación lineal local {#sec-ta-19-3}

El control lineal de §19.2 garantiza que una función derivable cambia, cerca de un punto fijo, a lo sumo proporcionalmente a la distancia al centro. La derivada proporciona una afirmación más precisa: **después de sustraer el incremento lineal adecuado, el error puede hacerse menor que cualquier múltiplo positivo de esa distancia**. Éste es el significado de primer orden de la derivación; no se trata de minimizar una distancia global entre funciones ni de seleccionar una recta entre infinitas candidatas.

### Definición 19.3.1 — Aproximación afín local y error de primer orden
Sean $D\subseteq\mathbb R$, $f:D\to\mathbb R$, $a\in D$ y $L\in\mathbb R$. La **aproximación afín de coeficiente $L$ centrada en $a$** y su **error** son las funciones, ambas con dominio $D$ y codominio $\mathbb R$,

$$
\ell_{f,a,L}(x):=f(a)+L(x-a),\qquad
 e_{f,a,L}(x):=f(x)-\ell_{f,a,L}(x)\quad(x\in D).
$$

Sus grafos existen por Separación en $D\times\mathbb R$: para cada $x\in D$, las operaciones del cuerpo determinan un único valor en cada caso. En particular, $\ell_{f,a,L}(a)=f(a)$ y $e_{f,a,L}(a)=0$, independientemente de $L$.

Si además $a\in\operatorname{Acc}(D)$, diremos que **el error es despreciable respecto de la distancia al centro** cuando

$$
\boxed{\forall\varepsilon>0\ \exists\delta>0\ \forall x\in D:\quad
0<|x-a|<\delta\ \Longrightarrow\ |e_{f,a,L}(x)|<\varepsilon|x-a|.}
$$

La definición es enteramente cuantificada: no presupone ni define un símbolo $o(\cdot)$, ni requiere que $D$ contenga un intervalo. En el centro, el error es exactamente cero, pero el factor $|x-a|$ impide dividir allí; la condición compara sólo los demás puntos del dominio.

### Proposición 19.3.2 — Unicidad del coeficiente de primer orden
Sean $a\in D\cap\operatorname{Acc}(D)$ y $f:D\to\mathbb R$. Existe **a lo sumo un** coeficiente $L\in\mathbb R$ para el cual el error de $\ell_{f,a,L}$ es despreciable respecto de $|x-a|$.

**Demostración.**
Supongamos que dos coeficientes $L,M\in\mathbb R$ cumplen la condición. Si $L\ne M$, pongamos $d:=|L-M|>0$ y fijemos la tolerancia concreta $\varepsilon:=d/3>0$. Para $L$ existe un radio $\delta_L>0$ con $|e_{f,a,L}(x)|<\varepsilon|x-a|$ siempre que $x\in D$ y $0<|x-a|<\delta_L$; análogamente obtenemos $\delta_M>0$. El mínimo $\delta:=\min\{\delta_L,\delta_M\}>0$ está determinado por **dos** números, sin elección para una familia infinita.

Como $a\in\operatorname{Acc}(D)$, por el criterio de bolas perforadas Lema §16.1.1 — Acumulación y aproximación perforada existe un punto $x\in D$ tal que $0<|x-a|<\delta$. Las definiciones proporcionan la identidad algebraica

$$
e_{f,a,M}(x)-e_{f,a,L}(x)=(L-M)(x-a).
$$

En consecuencia, por la desigualdad triangular,

$$
\begin{aligned}
d|x-a|&=|e_{f,a,M}(x)-e_{f,a,L}(x)|\\
&\le |e_{f,a,M}(x)|+|e_{f,a,L}(x)|\\
&<2\varepsilon|x-a|.
\end{aligned}
$$

Dividimos por $|x-a|>0$ y obtenemos $d<2d/3<d$, contradicción. Por tanto $L=M$. La acumulación resulta indispensable: sin otros puntos arbitrariamente próximos, la condición sobre el error podría ser vacua para cualquier coeficiente. $\square$

### Teorema 19.3.3 — Caracterización de la derivabilidad por aproximación lineal
Sean $D\subseteq\mathbb R$, $f:D\to\mathbb R$ y $a\in D\cap\operatorname{Acc}(D)$. Son equivalentes:

1. $f$ es derivable en $a$, relativamente a $D$.
2. Existe $L\in\mathbb R$ tal que $f(x)=f(a)+L(x-a)+e_{f,a,L}(x)$ para todo $x\in D$, y su error es despreciable respecto de $|x-a|$ en el sentido de la definición anterior.

Cuando estas condiciones se cumplen, el coeficiente es único y coincide con la derivada:

$$
\boxed{L=f'(a),\qquad
f(x)=f(a)+f'(a)(x-a)+e_{f,a,f'(a)}(x),\qquad
\frac{|e_{f,a,f'(a)}(x)|}{|x-a|}\xrightarrow[\substack{x\to a\\x\in D_a}]{}0.}
$$

La última expresión sólo se evalúa para $x\ne a$; es una abreviatura del criterio cuantificado precedente, no una definición adicional del cociente en $a$.

**Demostración.**
La igualdad de (2) es la identidad algebraica que define $e_{f,a,L}$; la condición sustantiva es el control del error. Para $x\in D_a$, la definición del cociente incremental y el hecho de que $x-a\ne0$ dan

$$
\frac{f(x)-f(a)}{x-a}-L
=\frac{f(x)-f(a)-L(x-a)}{x-a}
=\frac{e_{f,a,L}(x)}{x-a}.
$$

Por las propiedades del valor absoluto, para cada $\varepsilon>0$ y cada $x\in D_a$,

$$
\left|q_{f,a}(x)-L\right|<\varepsilon
\quad\Longleftrightarrow\quad
|e_{f,a,L}(x)|<\varepsilon|x-a|.
$$

Esta equivalencia conserva el **mismo radio $\delta$ y los mismos cuantificadores**. Por el lema Lema §19.1.2 — Perforar el dominio preserva la acumulación en el centro, $a$ es punto de acumulación de $D_a$. Por ello, la condición de error equivale exactamente a que $q_{f,a}$ tenga límite $L$ cuando $x\to a$ a través de $D_a$, esto es, a la derivabilidad conforme a Definición §19.1.3 — Derivabilidad en un punto. Si $f$ es derivable, Proposición §19.1.4 — Unicidad y criterio cuantificado de la derivada identifica ese límite con $f'(a)$; alternativamente, la proposición anterior establece directamente la unicidad de cualquier coeficiente admisible.

Dividiendo la desigualdad del error por $|x-a|>0$ se obtiene la relación de límite indicada en el recuadro. No se ha supuesto continuidad como hipótesis independiente, ni se ha definido una función derivada global, ni se han utilizado resultados del capítulo 20. $\square$

**Lectura conceptual.** La recta $y=f(a)+L(x-a)$ pasa por $(a,f(a))$ para cualquier $L$. Sólo una pendiente, cuando existe, produce un error cuyo cociente con la distancia al centro tiende a cero. En este sentido preciso se habla de la *aproximación lineal de primer orden*: la unicidad procede de la condición asintótica, no de una minimización de distancias.

### Proposición 19.3.4 — Exactitud afín y error cuadrático
Sean $m,b,a\in\mathbb R$. Para la función afín $f:\mathbb R\to\mathbb R$, $f(x)=mx+b$, la aproximación en $a$ de coeficiente $m$ es exacta: $e_{f,a,m}(x)=0$ para todo $x$. Para $g:\mathbb R\to\mathbb R$, $g(x)=x^2$, la aproximación de coeficiente $2a$ satisface la identidad exacta

$$
\boxed{g(x)=a^2+2a(x-a)+(x-a)^2,\qquad e_{g,a,2a}(x)=(x-a)^2.}
$$

**Demostración.**
En el caso afín, la distributividad da $f(x)-f(a)=m(x-a)$ y el error es nulo en todo el dominio. En el caso cuadrático, expandir el miembro derecho del recuadro mediante las leyes del cuerpo conduce a $x^2$. Para $x\ne a$,

$$
\frac{|e_{g,a,2a}(x)|}{|x-a|}
=\frac{|x-a|^2}{|x-a|}=|x-a|.
$$

Dada una tolerancia $\varepsilon>0$, el radio $\delta=\varepsilon$ hace que este cociente sea menor que $\varepsilon$ para todo $0<|x-a|<\delta$; en $x=a$ el error es cero. Así, la caracterización anterior vuelve a dar $g'(a)=2a$, en concordancia con el cálculo directo de Proposición §19.1.6 — Primeros cálculos: funciones afines y función cuadrática. El término $(x-a)^2$ es un error **exactamente identificado**: no se infiere de aquí ninguna fórmula general de Taylor. $\square$

**Transición.** Hemos definido la derivada mediante un límite, comprobado que garantiza continuidad y demostrado que equivale a una aproximación afín única de primer orden. Podemos ahora deducir las reglas de derivación para suma, múltiplos escalares y producto mediante operaciones locales sobre cocientes y errores, sin recurrir al teorema del valor medio.
