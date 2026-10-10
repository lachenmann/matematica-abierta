## 21.7. Integrabilidad de las funciones continuas {#sec-ta-21-7}

La continuidad impide cambios bruscos en torno a cada punto, pero las sumas de Darboux exigen controlar todos los subintervalos con una única escala. En un intervalo cerrado, la compacidad permite pasar de continuidad puntual a continuidad uniforme (Corolario §18.6.2 — Funciones continuas sobre cerrados acotados e intervalos cerrados). El teorema del valor extremo (Teorema §18.5.4 — Teorema del valor extremo: Weierstrass) aporta, por separado, la acotación requerida para definir las sumas. Nuestro argumento se organizará en tres pasos: construir particiones de anchura prescrita, trasladar una estimación uniforme de diferencias a la oscilación local y aplicar el criterio de Darboux. Ninguno de estos pasos supone una integral ya existente.

En esta sección, si $a<b$, $I=[a,b]$ y $P=\langle n,p\rangle\in\operatorname{Part}[a,b]$, conservamos las abreviaturas $I_k(P)$, $\Delta_k(P)$ y $\omega_k(P)$ de §§21.1–21.2. Escribimos $G(f,P):=U(f,P)-L(f,P)$ para la brecha sólo cuando $f$ es acotada y $a<b$. Los numerales $\nu_{\mathbb R}(n)$ son las imágenes de naturales en el cuerpo real; no son identificaciones literales de $\mathbb N$ con un subconjunto de $\mathbb R$.

### Lema 21.7.1 — Particiones equidistantes de anchura arbitrariamente pequeña
Para $a<b$ y cada $\delta>0$ existe una partición $P=\langle n,p\rangle$ de $[a,b]$ cuyas anchuras satisfacen

$$
\boxed{0<\Delta_k(P)<\delta\qquad(k<n).}
\tag{21.7.1}
$$

Más precisamente, existe una partición equidistante con nodos

$$
x_k=a+\frac{\nu_{\mathbb R}(k)}{\nu_{\mathbb R}(n)}(b-a)
\quad(k\in J_n),\qquad
\Delta_k(P)=\frac{b-a}{\nu_{\mathbb R}(n)}.
\tag{21.7.2}
$$

**Demostración.**
El real $\delta/(b-a)$ es positivo. La arquimedianidad de $\mathbb R$, obtenida de su completitud en Teorema §4.6.3 — Todo cuerpo ordenado completo es arquimediano, y su caracterización por recíprocos pequeños (Proposición §4.4.2 — Caracterización por recíprocos pequeños) proporcionan un natural fijo $n\ge1_{\mathbb N}$ tal que

$$
0<\frac{1_{\mathbb R}}{\nu_{\mathbb R}(n)}
<\frac{\delta}{b-a}.
\tag{21.7.3}
$$

La imagen $\nu_{\mathbb R}(n)$ es estrictamente positiva por Proposición §4.1.6 — Aritmética y orden de los numerales naturales, así que las divisiones son legítimas. Para $k\in J_n$, la fórmula (21.7.2) determina un único real $x_k\in[a,b]$, pues $0\le\nu_{\mathbb R}(k)\le\nu_{\mathbb R}(n)$. El grafo $\{\langle k,x_k\rangle:k\in J_n\}$ se obtiene por Separación dentro de $J_n\times[a,b]$ y define una función tipada $p:J_n\to[a,b]$, sin escoger un punto en cada posición. La aritmética de los numerales da

$$
x_0=a,\qquad x_n=b,\qquad
x_{S(k)}-x_k=\frac{b-a}{\nu_{\mathbb R}(n)}>0
\quad(k<n).
$$

Por tanto, $P=\langle n,p\rangle$ es una partición estricta. Multiplicar (21.7.3) por $b-a>0$ demuestra que su anchura común es menor que $\delta$. $\square$

**Lectura.** El lema no afirma que una partición arbitraria se vuelva «fina» por aumentar simbólicamente un índice. Exhibe, para un $\delta$ fijo, una familia finita de nodos cuya anchura se calcula exactamente. La propiedad arquimediana es la infraestructura que asegura la existencia de $n$.

### Lema 21.7.2 — Control de la oscilación mediante diferencias de valores
Sea $f:I\to\mathbb R$ acotada, $J\subseteq I$ no vacío y $\eta>0$. Si

$$
(\forall x,y\in J)\quad |f(x)-f(y)|<\eta,
\tag{21.7.4}
$$

entonces

$$
\boxed{0\le\omega(f,J)\le\eta.}
\tag{21.7.5}
$$

En particular, si una misma estimación (21.7.4) vale sobre cada $I_k(P)$, entonces

$$
\boxed{0\le G(f,P)\le\eta(b-a).}
\tag{21.7.6}
$$

**Demostración.**
El conjunto $f[J]$ es no vacío y acotado, de modo que $m:=m(f,J)$ y $M:=M(f,J)$ existen por Lema §21.2.2 — Existencia de las cotas extremas locales y comparación por inclusión. Fijemos temporalmente un $y\in J$. Para todo $x\in J$, (21.7.4) implica $f(x)<f(y)+\eta$, por lo que $f(y)+\eta$ es una cota superior de $f[J]$ y $M\le f(y)+\eta$. Esta última desigualdad vale para cada $y\in J$. Por tanto, $M-\eta$ es una cota inferior de $f[J]$ y, por maximalidad del ínfimo, $M-\eta\le m$. Se sigue $M-m\le\eta$; la no negatividad es parte de Definición §21.2.3 — Ínfimo, supremo y oscilación de un conjunto de valores. No hemos supuesto que $m$ o $M$ se alcancen en $J$, ni hemos escogido un punto para cada subintervalo.

Aplicando (21.7.5) a cada $I_k(P)$, la identidad de la brecha Proposición §21.2.5 — Encierro global e identidad de la brecha, las anchuras positivas y la comparación de sumas finitas dan

$$
0\le G(f,P)=\sum_{k<n}\omega_k(P)\Delta_k(P)
\le\sum_{k<n}\eta\Delta_k(P)
=\eta(b-a),
$$

donde el último paso es Proposición §21.1.2 — Existencia, anchuras positivas y suma de longitudes. $\square$

**Precisión sobre el signo.** Aunque en (21.7.4) todas las diferencias son estrictamente menores que $\eta$, su supremo puede ser igual a $\eta$. Por eso (21.7.5) lleva $\le\eta$ y no $<\eta$; la estricta desigualdad que necesita Darboux se asegurará escogiendo una tolerancia menor que la final.

### Teorema 21.7.3 — Una función acotada uniformemente continua es integrable
Si $a<b$ y $f:[a,b]\to\mathbb R$ es acotada y uniformemente continua, entonces $f$ es integrable en $[a,b]$. De hecho, para cada $\varepsilon>0$ existe un $\delta>0$ tal que cualquier partición $P$ cuyas anchuras cumplen $\Delta_k(P)<\delta$ para todo $k<n$ verifica

$$
\boxed{0\le U(f,P)-L(f,P)<\varepsilon.}
\tag{21.7.7}
$$

**Demostración.**
Fijemos $\varepsilon>0$ y definamos el real positivo

$$
\eta:=\frac{\varepsilon}{2(b-a)}>0.
\tag{21.7.8}
$$

Por continuidad uniforme (Definición §17.6.1 — Continuidad uniforme relativa a un dominio), existe $\delta>0$ tal que, para todos $x,y\in I$,

$$
|x-y|<\delta\quad\Longrightarrow\quad |f(x)-f(y)|<\eta.
\tag{21.7.9}
$$

Sea ahora cualquier partición $P$ cuyas anchuras sean menores que $\delta$. Si $x,y\in I_k(P)=[x_k,x_{S(k)}]$, el orden del intervalo proporciona

$$
|x-y|\le x_{S(k)}-x_k=\Delta_k(P)<\delta.
$$

La estimación (21.7.9) vale por ello sobre cada subintervalo, con el mismo $\eta$. El lema Lema §21.7.2 — Control de la oscilación mediante diferencias de valores demuestra

$$
0\le G(f,P)\le\eta(b-a)
=\frac{\varepsilon}{2}<\varepsilon.
\tag{21.7.10}
$$

El lema Lema §21.7.1 — Particiones equidistantes de anchura arbitrariamente pequeña asegura la existencia de una partición equidistante $P_\varepsilon$ con todas sus anchuras menores que este $\delta$. Para esa partición (21.7.10) proporciona el testigo requerido por el criterio de Darboux (Teorema §21.4.2 — Criterio de Darboux y estabilidad por refinamiento); como $f$ ya es acotada, el criterio concluye que es integrable. La prueba establece incluso (21.7.7) para toda partición suficientemente fina, sin afirmar convergencia de sumas etiquetadas ni elegir una sucesión de particiones. $\square$

### Corolario 21.7.4 — Toda función continua en un intervalo cerrado es integrable
Sean $a,b\in\mathbb R$ con $a\le b$ y $f:[a,b]\to\mathbb R$ continua en todos los puntos de su dominio, incluidos los extremos con la continuidad relativa de §17. Entonces $f$ es integrable en $[a,b]$; para $a<b$ la palabra «integrable» tiene el significado de Darboux de Definición §21.4.1 — Integrabilidad de Darboux por igualdad de integrales extremas y, para $a=b$, el de la convención Definición §21.6.5 — Integración en un intervalo degenerado.

**Demostración.**
Si $a=b$, la función tiene por dominio el singleton $[a,a]$ y es integrable por definición (Definición §21.6.5 — Integración en un intervalo degenerado), con integral cero. No hay particiones estrictas que analizar.

Supongamos $a<b$. El intervalo $[a,b]$ es compacto y no vacío por Teorema §18.2.1 — Todo intervalo cerrado y acotado es compacto. El teorema del valor extremo Teorema §18.5.4 — Teorema del valor extremo: Weierstrass entrega dos puntos particulares $u,v\in[a,b]$ tales que

$$
f(u)\le f(t)\le f(v)\qquad(t\in[a,b]).
$$

Esto demuestra la acotación de $f$ requerida en §21.2; no basta afirmar que es continua y pasar por alto dicha hipótesis. A su vez, Heine–Cantor para intervalos cerrados (Corolario §18.6.2 — Funciones continuas sobre cerrados acotados e intervalos cerrados) demuestra que $f$ es uniformemente continua. Ambas premisas están, por tanto, verificadas, y Teorema §21.7.3 — Una función acotada uniformemente continua es integrable establece la integrabilidad de $f$. No se ha utilizado el teorema fundamental del cálculo, que aún no se ha formulado para la integral construida. $\square$

**Interpretación deductiva.** La compacidad desempeña aquí dos funciones lógicamente distintas: asegura cotas globales y convierte en uniforme la continuidad. Sólo después entran en escena la propiedad arquimediana (particiones suficientemente finas) y la completitud (ínfimos y supremos de Darboux). La continuidad es una condición suficiente, no una parte de la definición de integrabilidad.

### Corolario 21.7.5 — Primeras clases de ejemplos integrables
Para todo $a\le b$, las siguientes funciones son integrables en $[a,b]$:

1. La restricción $p\upharpoonright[a,b]:[a,b]\to\mathbb R$ de cualquier polinomio real tipado $p:\mathbb R\to\mathbb R$ construido en §17.5.
2. La restricción $r\upharpoonright[a,b]:[a,b]\to\mathbb R$ de cualquier función racional $r:D\to\mathbb R$ de §17.5, siempre que $[a,b]\subseteq D$, es decir, que su denominador no se anule en el intervalo y la función esté allí efectivamente definida.

**Demostración.**
El teorema Teorema §17.5.3 — Todo polinomio real es continuo en la recta demuestra la continuidad de $p$ sobre $\mathbb R$, y Corolario §17.5.4 — Continuidad de las funciones racionales en su dominio natural la de $r$ en su dominio efectivo $D$. La conservación de la continuidad por restricción (Corolario §17.4.6 — Clausura global, restricciones y cocientes) permite tratarlas como funciones con dominio exactamente $[a,b]$ y codominio $\mathbb R$, siempre que se cumpla la inclusión exigida para $r$. Aplicar Corolario §21.7.4 — Toda función continua en un intervalo cerrado es integrable a cada restricción demuestra ambas afirmaciones; si $a=b$, se utiliza igualmente su rama degenerada. No se ha evaluado ninguna integral ni se ha supuesto existencia de una primitiva. $\square$

**Transición.** La continuidad produce integrabilidad al controlar todas las oscilaciones locales mediante un mismo radio. §21.8 estudiará una condición suficiente independiente —la monotonía—, que admite discontinuidades; así distinguiremos con precisión «continua», «acotada» e «integrable». Las sumas etiquetadas y su equivalencia con el valor de Darboux quedan para una unidad posterior.
