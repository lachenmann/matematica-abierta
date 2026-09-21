## 23.5. Convergencia uniforme de derivadas y condición de anclaje {#sec-ta-23-5}

Una convergencia uniforme de funciones controla sus valores, pero no necesariamente las pendientes de sus gráficas. Tampoco basta conocer los límites de las derivadas para recuperar los valores: una derivada es incapaz de distinguir dos funciones que difieren en una constante. Para obtener un teorema correcto añadiremos un **punto de anclaje**, en el que converjan los valores de las funciones, y utilizaremos el teorema del valor medio para propagar ese control a todo el intervalo.

Fijaremos siempre $a<b$ e $I:=[a,b]$. Cada $f_n:I\to\mathbb R$ será continua en $I$ relativamente a su dominio y derivable en cada punto del **interior** $J:=(a,b)$, también relativamente a $I$. La sucesión de derivadas estará definida exclusivamente en $J$; no atribuiremos derivadas bilaterales a $a$ ni a $b$. En esta sección no supondremos que las derivadas sean continuas, acotadas por separado o integrables: bastarán las hipótesis formuladas a continuación y el teorema del valor medio ya demostrado.

### Definición 23.5.1 — Sucesión de derivadas interiores de una sucesión dada
Dadas las hipótesis anteriores, la **sucesión de derivadas interiores** de $(f_n)$ es la función $\mathbf d:\mathbb N\to\mathbb R^J$ cuyos términos son las funciones tipadas

$$
d_n:J\longrightarrow\mathbb R,\qquad d_n(t)=f_n'(t)\quad(t\in J).
\tag{23.5.1}
$$

Esta definición requiere justificar su existencia. Para un $n$ fijo, cada $t\in J$ es punto de acumulación de $I$, $f_n$ es derivable allí y Proposición §19.1.4 — Unicidad y criterio cuantificado de la derivada garantiza un **único** valor $f_n'(t)$. El conjunto

$$
G_n=\{\langle t,r\rangle\in J\times\mathbb R:\ r\text{ es la derivada de }f_n\text{ en }t\text{ relativa a }I\}
$$

existe por Separación y es el grafo de una función $d_n:J\to\mathbb R$. El predicado que determina $d_n$ tiene un único valor para cada $n$; por Separación en $\mathbb N\times\mathbb R^J$ obtenemos el grafo de $\mathbf d$. Por tanto, (23.5.1) no consiste en elegir libremente una función derivada para cada índice. Si $d_n$ converge uniformemente a una función $g:J\to\mathbb R$, esta última será un límite **en el interior**, sin extensión automática a los extremos.

### Lema 23.5.2 — Control de incrementos mediante diferencias de derivadas
Sean $n,m\in\mathbb N$ y $\eta\ge0$. Si

$$
|d_n(t)-d_m(t)|\le\eta\qquad(t\in J),
\tag{23.5.2}
$$

entonces, para cualesquiera $x,y\in I$,

$$
\boxed{|(f_n(x)-f_m(x))-(f_n(y)-f_m(y))|\le\eta|x-y|.}
\tag{23.5.3}
$$

**Demostración.**
Construyamos la diferencia puntual tipada $h:=f_n-f_m:I\to\mathbb R$ mediante Proposición §16.3.2 — Existencia y tipado de las operaciones puntuales. Por la estabilidad algebraica de la continuidad (Teorema §17.4.3 — Estabilidad de la continuidad bajo operaciones algebraicas y valor absoluto), $h$ es continua sobre $I$. La regla de la diferencia Corolario §19.4.2 — Multiplicación por escalares, opuestos y diferencias demuestra que es derivable en cada $t\in J$ y $h'(t)=d_n(t)-d_m(t)$.

Si $x=y$, ambos miembros de (23.5.3) son cero. Si $x<y$, aplicamos Corolario §20.3.3 — Valor medio en un subintervalo del dominio original a la función $h$ y al subintervalo $[x,y]\subseteq I$: existe $\xi\in(x,y)\subseteq J$ para el cual

$$
h(y)-h(x)=h'(\xi)(y-x).
$$

Por (23.5.2), $|h(y)-h(x)|\le\eta(y-x)=\eta|y-x|$, que es (23.5.3) tras sustituir $h=f_n-f_m$ y usar la simetría del valor absoluto. Para $y<x$ se intercambian los argumentos. El punto $\xi$ es un testigo local de una única aplicación del teorema del valor medio; no se construye una función que seleccione puntos intermedios para todos los pares. $\square$

### Teorema 23.5.3 — El anclaje y las derivadas uniformemente convergentes producen un límite uniforme
Bajo las hipótesis de la Definición 23.5.1, supongamos que existe $g:J\to\mathbb R$ tal que $d_n$ converge uniformemente a $g$ en $J$. Supongamos, además, que para **algún punto fijo** $c\in I$ la sucesión real $(f_n(c))_{n\in\mathbb N}$ converge a un número $\lambda\in\mathbb R$. Entonces existe una única función $f:I\to\mathbb R$ tal que $f_n$ converge uniformemente a $f$ en $I$, y satisface $f(c)=\lambda$.

**Demostración.**
Escribamos $\ell:=b-a>0$. Fijemos $\varepsilon>0$. Como $d_n$ converge uniformemente a $g$, Proposición §23.2.2 — Toda sucesión uniformemente convergente es uniformemente de Cauchy afirma que $(d_n)$ es uniformemente de Cauchy sobre $J$. Con tolerancia $\eta:=\varepsilon/(4\ell)>0$, existe un índice $N_1$ tal que

$$
|d_n(t)-d_m(t)|<\eta
\qquad(n,m\ge N_1,\ t\in J).
\tag{23.5.4}
$$

Por otra parte, la convergencia numérica de $f_n(c)$ a $\lambda$ implica su condición de Cauchy (Teorema §13.8.2 — Toda sucesión real convergente es de Cauchy): existe $N_0$ tal que

$$
|f_n(c)-f_m(c)|<\frac\varepsilon2
\qquad(n,m\ge N_0).
\tag{23.5.5}
$$

Pongamos $N:=\max\{N_0,N_1\}$. Fijados $n,m\ge N$ y $x\in I$, el lema anterior aplicado a (23.5.4), con los puntos $x,c$, produce

$$
\begin{aligned}
|f_n(x)-f_m(x)|
&\le |f_n(c)-f_m(c)|\\
&\quad+|(f_n(x)-f_m(x))-(f_n(c)-f_m(c))|\\
&<\frac\varepsilon2+\eta|x-c|\\
&\le\frac\varepsilon2+\eta\ell
=\frac{3\varepsilon}{4}<\varepsilon.
\end{aligned}
\tag{23.5.6}
$$

Aquí $|x-c|\le b-a=\ell$ porque ambos puntos pertenecen a $[a,b]$. El índice $N$ no depende de $x$ ni de los dos índices de la cola: (23.5.6) es la condición **uniforme** de Cauchy. El criterio Teorema §23.2.4 — Criterio uniforme de Cauchy construye mediante su grafo una única función $f:I\to\mathbb R$ que es límite uniforme de $f_n$.

Finalmente, la convergencia uniforme implica convergencia puntual en $c$ por Proposición §23.1.6 — La convergencia uniforme implica la puntual, mientras que la hipótesis dice que $f_n(c)\to\lambda$. La unicidad del límite numérico Teorema §13.3.5 — Unicidad del límite real da $f(c)=\lambda$. Se han reunido sólo los dos testigos $N_0,N_1$, sin seleccionar puntos, derivadas o límites simultáneamente. $\square$

**Lectura.** El teorema del valor medio transporta desde $c$ a cualquier $x$ el control de las derivadas. El factor $b-a$ permite usar un **mismo índice** para todo el intervalo. La convergencia de un único valor fija la constante que la derivada no distingue.

### Teorema 23.5.4 — Diferenciación bajo límite uniforme de derivadas
Sean $f_n$, $d_n$, $g$, $c$ y $\lambda$ como en el teorema anterior, y sea $f:I\to\mathbb R$ el límite uniforme allí construido. Entonces $f$ es continua sobre $I$, derivable en todos los puntos de $J=(a,b)$ relativamente a $I$, y

$$
\boxed{f'(x)=g(x)=\lim_{n\to\infty}f_n'(x)
\qquad(x\in(a,b)).}
\tag{23.5.7}
$$

La última expresión indica convergencia **puntual** de la sucesión numérica de derivadas en cada $x$; la convergencia de las funciones derivadas hacia $g$ es, por hipótesis, uniforme en $J$. No se afirma aquí que $f$ posea derivadas en $a$ o $b$.

**Demostración.**
La continuidad de $f$ en todo $I$ se sigue de Corolario §23.3.2 — Continuidad del límite uniforme en todo el dominio, pues cada $f_n$ es continua y la convergencia de las funciones es uniforme. Fijemos ahora $x\in J$ y $\varepsilon>0$. Por la convergencia uniforme de $d_n$ a $g$, con tolerancia $\varepsilon/4$, elegimos $N$ tal que

$$
|d_k(t)-g(t)|<\frac\varepsilon4
\qquad(k\ge N,\ t\in J).
\tag{23.5.8}
$$

Para cualquier $m\ge N$ y cualquier $t\in J$, la desigualdad triangular da

$$
|d_m(t)-d_N(t)|
\le|d_m(t)-g(t)|+|g(t)-d_N(t)|
<\frac\varepsilon2.
$$

Apliquemos Lema §23.5.2 — Control de incrementos mediante diferencias de derivadas a $f_m$ y $f_N$, con $\eta=\varepsilon/2$. Para todo $y\in I$ distinto de $x$ obtenemos, tras dividir por $|y-x|>0$,

$$
\left|\frac{f_m(y)-f_m(x)}{y-x}
-\frac{f_N(y)-f_N(x)}{y-x}\right|
\le\frac\varepsilon2.
\tag{23.5.9}
$$

Mantengamos fijos **este** $x$ y **este** $y\ne x$ y hagamos $m\to\infty$. La convergencia uniforme de $f_m$ a $f$ implica convergencia de ambos valores $f_m(y)$ y $f_m(x)$, por lo que sus cocientes, con denominador fijo no nulo, convergen al cociente de $f$. Como todos los términos de (23.5.9) están en el intervalo cerrado de radio $\varepsilon/2$ alrededor del cociente de $f_N$, su límite pertenece al mismo intervalo (por la preservación del orden al pasar al límite Teorema §13.6.2 — Preservación del orden en el paso al límite). Así,

$$
\left|\frac{f(y)-f(x)}{y-x}
-\frac{f_N(y)-f_N(x)}{y-x}\right|
\le\frac\varepsilon2
\quad(y\in I,\ y\ne x).
\tag{23.5.10}
$$

**El índice $N$ de esta desigualdad no depende de $y$.** Puesto que $f_N$ es derivable en $x$ relativamente a $I$, la definición Definición §19.1.3 — Derivabilidad en un punto aplicada con tolerancia $\varepsilon/4$ proporciona un radio $\delta>0$ tal que, si $y\in I$ y $0<|y-x|<\delta$,

$$
\left|\frac{f_N(y)-f_N(x)}{y-x}-d_N(x)\right|<\frac\varepsilon4.
\tag{23.5.11}
$$

Combinando (23.5.10), (23.5.11) y (23.5.8) para $t=x$, hallamos

$$
\begin{aligned}
\left|\frac{f(y)-f(x)}{y-x}-g(x)\right|
&\le\left|\frac{f(y)-f(x)}{y-x}
-\frac{f_N(y)-f_N(x)}{y-x}\right|\\
&\quad+\left|\frac{f_N(y)-f_N(x)}{y-x}-d_N(x)\right|
+|d_N(x)-g(x)|\\
&<\frac\varepsilon2+\frac\varepsilon4+\frac\varepsilon4
=\varepsilon.
\end{aligned}
\tag{23.5.12}
$$

El punto $x$ es interior y, por ello, pertenece a $\operatorname{Acc}(I)$; (23.5.12) prueba que el cociente incremental de $f$ tiende a $g(x)$. La definición de derivabilidad y la unicidad de la derivada (Proposición §19.1.4 — Unicidad y criterio cuantificado de la derivada) concluyen $f'(x)=g(x)$. La arbitrariedad de $x$ establece (23.5.7) sobre todo $J$. Ninguna etapa ha presupuesto la integrabilidad o la continuidad de $g$ o de las derivadas. $\square$

**Alcance.** El argumento no intercambia formalmente dos límites sin justificación: primero obtiene una estimación uniforme de *cocientes de incrementos* con el teorema del valor medio y sólo entonces toma el límite en el índice. El radio local se elige después, para una función $f_N$ ya determinada.

### Proposición 23.5.5 — Las derivadas no controlan las constantes: necesidad del anclaje
Existe una sucesión de funciones continuas en $[0,1]$ y derivables en $(0,1)$ cuyas derivadas convergen uniformemente a cero, aunque las funciones **no convergen puntualmente en ningún punto**.

**Demostración.**
Para $n\in\mathbb N$ sea $f_n:[0,1]\to\mathbb R$ la función constante $f_n(x)=\nu_{\mathbb R}(n)$, donde $\nu_{\mathbb R}:\mathbb N\to\mathbb R$ es la incrustación de numerales reales de Definición §4.1.5 — Aplicación de numerales naturales en un cuerpo ordenado. Sus grafos y la función $n\mapsto f_n$ se construyen por Separación, con valores únicos. Cada $f_n$ es continua y derivable en el interior; por el cálculo de la derivada de una función constante (Proposición §19.1.6 — Primeros cálculos: funciones afines y función cuadrática), $d_n(t)=0$ en $(0,1)$ para todo $n$. Por tanto, las derivadas convergen uniformemente a la función nula: todos los errores son exactamente cero.

Sin embargo, fijado cualquier $c\in[0,1]$, la sucesión $f_n(c)=\nu_{\mathbb R}(n)$ no es de Cauchy: para cualquier $N$, los índices explícitos $n=N$ y $m=N+1$ verifican $|f_m(c)-f_n(c)|=1$, contra la tolerancia $1/2$ de Definición §13.8.1 — Sucesión real de Cauchy. Toda sucesión real convergente es de Cauchy (Teorema §13.8.2 — Toda sucesión real convergente es de Cauchy), así que no existe límite en $c$. La falta de anclaje no puede suprimirse del teorema general. $\square$

### Proposición 23.5.6 — La convergencia uniforme de funciones no garantiza la de sus derivadas
Existe una sucesión $f_n:[-1,1]\to\mathbb R$ de funciones continuas en todo el intervalo y derivables en su interior que converge uniformemente a la función nula $f$, pero **sus derivadas no convergen uniformemente a $f'$**; de hecho, ni siquiera convergen a $f'(0)$ en el punto interior $0$.

**Demostración.**
Pongamos $m_n:=\nu_{\mathbb R}(n+1)\ge1$ y definamos

$$
f_n(x):=\frac{x}{1+m_n^2x^2},\qquad x\in[-1,1].
\tag{23.5.13}
$$

El denominador es mayor o igual que $1$, así que nunca se anula. Separación construye los grafos tipados y la sucesión como en los ejemplos anteriores. Los polinomios son continuos y derivables; la continuidad de los cocientes y su regla de derivación (Corolario §17.5.4 — Continuidad de las funciones racionales en su dominio natural, Teorema §19.5.4 — Regla de derivación del cociente) muestran que cada $f_n$ es continua en el intervalo y derivable en todo su interior.

Para $t:=m_n|x|\ge0$ tenemos $(t-1)^2\ge0$, de donde $2t\le1+t^2$. Como $m_n>0$,

$$
|f_n(x)|=\frac{|x|}{1+m_n^2x^2}
\le\frac{1}{2m_n}\qquad(x\in[-1,1]).
\tag{23.5.14}
$$

La propiedad arquimediana implica $1/m_n\to0$. Para cada $\varepsilon>0$ existe un índice $N$ tal que $1/(2m_n)<\varepsilon$ para todo $n\ge N$. La cota (23.5.14), válida para **todo** $x$, demuestra $f_n\to f=0$ uniformemente.

Pero $f_n(0)=0$ y, si $h\ne0$ pertenece al intervalo,

$$
\frac{f_n(h)-f_n(0)}{h}=
\frac1{1+m_n^2h^2}\longrightarrow1\quad(h\to0),
$$

pues $m_n$ es una constante fija al derivar cada término. Por definición, $f_n'(0)=1$ para todo $n$, mientras que $f'(0)=0$ porque $f$ es constante. La sucesión numérica de derivadas en $0$ es constantemente igual a $1$ y no converge a $0$. En particular, no existe convergencia uniforme de $d_n$ a $f'\upharpoonright(-1,1)$. Este contraejemplo no contradice el teorema anterior: precisamente falta la hipótesis de convergencia uniforme de las derivadas hacia una función. $\square$

**Transición.** Ya conocemos una condición suficiente para diferenciar el límite y dos hipótesis que no pueden confundirse: el anclaje controla las constantes, mientras que la uniformidad de las derivadas controla la variación local. En §23.6 pasaremos de sucesiones a **series de funciones** mediante sus sucesiones de sumas parciales. Sólo después tendrá sentido formular el criterio $M$ de Weierstrass, sin introducir prematuramente la teoría de series de potencias del capítulo siguiente.
