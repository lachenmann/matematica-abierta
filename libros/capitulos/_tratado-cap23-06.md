## 23.6. Series de funciones: sumas parciales y convergencia {#sec-ta-23-6}

Una serie numérica no es un número al que se haya concedido de antemano existencia: en el Capítulo 14 la definimos a partir de una sucesión de sumas parciales. Para una serie de funciones la misma distinción resulta imprescindible y aparece una dificultad adicional: la suma parcial debe ser una **función completa sobre el dominio común**, mientras que el límite de esas funciones puede ser puntual o uniforme. No bastará comprobar que cada suma finita está definida; tampoco bastará que los términos individuales tiendan a cero.

Fijemos un conjunto $E\subseteq\mathbb R$, que puede ser vacío, y una sucesión dada $\mathbf f=(f_n)_{n\in\mathbb N}:\mathbb N\to\mathbb R^E$. Todos los términos tienen dominio **exacto** $E$ y codominio $\mathbb R$. Conservaremos la convención del Capítulo 14: los índices comienzan en $0$, la suma parcial de índice $n$ contiene los términos $0,\ldots,n$ y un bloque posterior a $n$ comienza en $n+1$.

### Definición 23.6.1 — Sucesión de sumas parciales de funciones
La **sucesión de sumas parciales de funciones** de $\mathbf f$ es la única sucesión $\mathbf S=(S_n)_{n\in\mathbb N}:\mathbb N\to\mathbb R^E$ tal que

$$
\boxed{S_0=f_0,\qquad S_{n+1}=S_n+f_{n+1}\quad(n\in\mathbb N),}
\tag{23.6.1}
$$

donde las sumas del lado derecho son operaciones puntuales sobre funciones con el mismo dominio y codominio. Escribimos

$$
\operatorname{PS}_E(\mathbf f):=\mathbf S,
\qquad \sum_{k=0}^{n}f_k:=S_n.
\tag{23.6.2}
$$

**Existencia, tipado y unicidad.** Para cada $x\in E$, Proposición §23.1.2 — Evaluación en un punto y sucesión real inducida construye una única sucesión real $a^{(x)}$ con $a^{(x)}_n=f_n(x)$. La operación numérica Definición §14.1.1 — Sucesión de sumas parciales y serie numérica produce una única sucesión $\operatorname{PS}(a^{(x)})$. Para cada $n$ fijado, Separación en $E\times\mathbb R$ forma

$$
G_n:=\{\langle x,r\rangle\in E\times\mathbb R:
       r=\operatorname{PS}(a^{(x)})_n\}.
\tag{23.6.3}
$$

Cada $G_n$ es el grafo de una función $S_n:E\to\mathbb R$: para cada $x$ hay exactamente un valor $r$. La relación $\{\langle n,H\rangle\in\mathbb N\times\mathbb R^E:H=S_n\}$ existe igualmente por Separación, pues $S_n$ está caracterizada de manera única por (23.6.3), y determina la sucesión $\mathbf S$. Las ecuaciones numéricas de Definición §14.1.1 — Sucesión de sumas parciales y serie numérica dicen $S_0(x)=f_0(x)$ y $S_{n+1}(x)=S_n(x)+f_{n+1}(x)$ para todo $x$. La igualdad tipada de funciones Proposición §0.6.3 — Criterio de igualdad de funciones implica (23.6.1). Si otra sucesión satisficiera esas ecuaciones, para cada $x$ sus evaluaciones serían las mismas sumas parciales numéricas, luego todos sus términos serían las funciones $S_n$. Queda probada la unicidad. Para $E=\varnothing$, cada grafo es vacío y la misma construcción funciona sin fijar un punto inexistente.

De hecho, Separación en el conjunto existente $(\mathbb R^E)^{\mathbb N}\times(\mathbb R^E)^{\mathbb N}$ y la unicidad precedente legitiman $\operatorname{PS}_E$ como función **total** sobre el conjunto de sucesiones de funciones. Una serie de funciones es el proceso secuencial representado por $\operatorname{PS}_E(\mathbf f)$, tanto si converge como si no. La construcción no elige independientemente sumas para infinitos índices: utiliza las sucesiones numéricas recursivas ya definidas y grafos de valor único.

### Definición 23.6.2 — Convergencia puntual, convergencia uniforme y función suma de una serie
Sea $\mathbf S=\operatorname{PS}_E(\mathbf f)$. Diremos que la serie $\sum_{k=0}^{\infty}f_k$ **converge puntualmente en $E$** si existe $F:E\to\mathbb R$ a la cual $S_n$ converge puntualmente, es decir,

$$
\boxed{\forall x\in E\;\forall\varepsilon>0\;\exists N\in\mathbb N\;
\forall n\ge N:\quad |S_n(x)-F(x)|<\varepsilon.}
\tag{23.6.4}
$$

Diremos que **converge uniformemente en $E$** si existe $F:E\to\mathbb R$ tal que

$$
\boxed{\forall\varepsilon>0\;\exists N\in\mathbb N\;
\forall n\ge N\;\forall x\in E:\quad |S_n(x)-F(x)|<\varepsilon.}
\tag{23.6.5}
$$

La expresión $\sum_{k=0}^{\infty}f_k$ designa la serie, definida aun sin convergencia. **Sólo después de establecer convergencia puntual** puede denotar su *función suma* $F$ y escribirse una igualdad $\sum_{k=0}^{\infty}f_k=F$, entendida como igualdad de funciones de dominio $E$ y codominio $\mathbb R$. Si la convergencia es uniforme, lo indicaremos expresamente; no se sobreentiende por el signo de suma.

La función suma, cuando existe, es única por Proposición §23.1.4 — Unicidad del límite puntual como función tipada. Más aún, la convergencia de la serie numérica $\sum_{k=0}^{\infty}f_k(x)$ para cada $x\in E$ basta para **construir** la función suma: Definición §14.1.4 — Convergencia, divergencia y suma de una serie y la unicidad del límite real Teorema §13.3.5 — Unicidad del límite real aseguran que para cada $x$ existe exactamente un real $r$ que es límite de $\operatorname{PS}(a^{(x)})$. Separación en $E\times\mathbb R$ determina el grafo

$$
G_F:=\{\langle x,r\rangle\in E\times\mathbb R:
       \operatorname{PS}(a^{(x)})_n\longrightarrow r\}.
\tag{23.6.6}
$$

Su totalidad y valor único proporcionan $F:E\to\mathbb R$, y (23.6.3) identifica su límite en cada punto con el de $S_n(x)$. Por Proposición §23.1.6 — La convergencia uniforme implica la puntual, la convergencia uniforme de la serie implica la puntual. Si $E=\varnothing$, todos los términos y sus sumas parciales son la única función vacía tipada, ambas convergencias se cumplen por vacuidad y la función suma es esa misma función vacía. No se introduce una suma real sobre un dominio vacío ni se elige una familia de límites mediante Choice.

**Distinción de lectura.** La convergencia puntual permite que $N$ dependa de $x$; la uniforme exige fijarlo **antes** de recorrer el dominio. Una serie de funciones puede tener una función suma sin converger uniformemente a ella.

### Proposición 23.6.3 — Identidades de los bloques finitos de funciones
Sean $n,m\in\mathbb N$ con $n<m$. Definimos el **bloque posterior a $n$ y terminado en $m$** como la función tipada

$$
\boxed{\sum_{k=n+1}^{m}f_k:=S_m-S_n:E\longrightarrow\mathbb R.}
\tag{23.6.7}
$$

Para cada $x\in E$ valen las identidades

$$
\boxed{\left(\sum_{k=n+1}^{m}f_k\right)(x)
=\sum_{k=n+1}^{m}f_k(x)=S_m(x)-S_n(x),}
\tag{23.6.8}
$$

$$
\sum_{k=n+1}^{n+1}f_k=f_{n+1},\qquad
S_m=S_n+\sum_{k=n+1}^{m}f_k.
\tag{23.6.9}
$$

En particular, el bloque representa exactamente la suma **finita** de los términos consecutivos $f_{n+1},\ldots,f_m$, sin definir una suma vacía.

**Demostración.**
Las funciones $S_m$ y $S_n$ tienen el mismo dominio $E$ y codominio $\mathbb R$; su diferencia puntual existe como función tipada por Proposición §16.3.2 — Existencia y tipado de las operaciones puntuales. Fijemos $x\in E$. La construcción de (23.6.3) identifica $S_j(x)$ con la suma parcial numérica de $a^{(x)}$ para cada $j$. La notación y las identidades del bloque numérico Notación §14.2.1 — Suma de un bloque finito posterior y Proposición §14.2.2 — Identidades de los bloques de sumación dan precisamente (23.6.8), incluido el hecho de que el primer término del bloque es $f_{n+1}(x)$. La recursión (23.6.1) y las leyes aditivas reales proporcionan $S_{n+1}(x)-S_n(x)=f_{n+1}(x)$ y $S_n(x)+(S_m(x)-S_n(x))=S_m(x)$. La igualdad de las funciones en (23.6.9) resulta de la coincidencia en cada punto y de sus tipos comunes (Proposición §0.6.3 — Criterio de igualdad de funciones). Si $E$ es vacío, todas estas igualdades son igualdades de funciones con grafo vacío. $\square$

### Teorema 23.6.4 — Criterio uniforme de Cauchy para series de funciones
Para una sucesión dada $f_n:E\to\mathbb R$, son equivalentes:

1. La serie $\sum_{k=0}^{\infty}f_k$ converge uniformemente en $E$.
2. Para todo $\varepsilon>0$ existe $N\in\mathbb N$ tal que, para cualesquiera naturales $n,m$ y cualquier $x\in E$,

$$
\boxed{N\le n<m\quad\Longrightarrow\quad
\left|\left(\sum_{k=n+1}^{m}f_k\right)(x)\right|<\varepsilon.}
\tag{23.6.10}
$$

Cuando estas condiciones se cumplen, la función suma es única. El criterio vale para conjuntos $E$ arbitrarios, incluidos los vacíos o no acotados; no presupone la existencia de una norma supremo finita.

**Demostración.**
Sea $\mathbf S=\operatorname{PS}_E(\mathbf f)$. La primera condición significa, por definición, que la sucesión $\mathbf S$ converge uniformemente hacia alguna función $F:E\to\mathbb R$. El criterio uniforme de Cauchy Teorema §23.2.4 — Criterio uniforme de Cauchy afirma que esto equivale a

$$
\forall\varepsilon>0\;\exists N\in\mathbb N\;
\forall n,m\ge N\;\forall x\in E:
|S_m(x)-S_n(x)|<\varepsilon.
\tag{23.6.11}
$$

Si se satisface (23.6.11) y $N\le n<m$, (23.6.8) transforma inmediatamente el error en el módulo del bloque de (23.6.10). En sentido inverso, fijemos $\varepsilon>0$ y el $N$ de (23.6.10). Para $n,m\ge N$, la tricotomía natural Proposición §1.6.7 — Tricotomía decidible de los naturales distingue $n<m$, $m<n$ y $m=n$. En el primer caso aplicamos la hipótesis; en el segundo intercambiamos ambos índices y utilizamos $|S_m(x)-S_n(x)|=|S_n(x)-S_m(x)|$ (Proposición §4.2.2 — Propiedades elementales del valor absoluto); en el tercero la diferencia vale $0<\varepsilon$. Como el mismo $N$ sirve para todos los puntos, resulta (23.6.11). El teorema Teorema §23.2.4 — Criterio uniforme de Cauchy proporciona entonces la función límite uniforme única, que es la suma de la serie por Definición §23.6.2 — Convergencia puntual, convergencia uniforme y función suma de una serie.

Si $E=\varnothing$, tanto el control de bloques como la convergencia uniforme a la única función vacía son verdaderos por vacuidad. No se escogió un punto del dominio ni una función límite entre varios candidatos. $\square$

**Interpretación.** El criterio no solicita que un término aislado sea pequeño: exige que cualquier número finito de términos **consecutivos y suficientemente tardíos** tenga suma pequeña, de manera simultánea para todos los puntos. El orden $\exists N\,\forall n,m\,\forall x$ es esencial.

### Corolario 23.6.5 — La convergencia uniforme de una serie obliga a la anulación uniforme de sus términos
Si $\sum_{k=0}^{\infty}f_k$ converge uniformemente en $E$, entonces la sucesión de términos $f_n$ converge **uniformemente a la función nula** $0_E:E\to\mathbb R$, $0_E(x)=0$.

**Demostración.**
La función nula existe como grafo $\{\langle x,0\rangle:x\in E\}\subseteq E\times\mathbb R$, definido por Separación. Fijemos $\varepsilon>0$ y obtengamos del criterio (23.6.10) un índice $N$. Para cada $n\ge N$ y todo $x\in E$, el bloque con extremos $n<n+1$ tiene un solo término. Por (23.6.9),

$$
|f_{n+1}(x)-0_E(x)|
=\left|\left(\sum_{k=n+1}^{n+1}f_k\right)(x)\right|
<\varepsilon.
\tag{23.6.12}
$$

El umbral $N+1$ sirve entonces para todos los índices $k\ge N+1$: en los naturales, cada tal $k$ es $n+1$ con $n\ge N$. Es exactamente la convergencia uniforme $f_k\to0_E$. El caso de dominio vacío también se satisface por vacuidad. $\square$

Este resultado es una **condición necesaria**, no un criterio suficiente. La diferencia se aprecia ya en una serie de funciones constantes.

### Proposición 23.6.6 — Términos uniformemente nulos con serie divergente
Existe una sucesión de funciones continuas $f_n:[0,1]\to\mathbb R$ que converge uniformemente a cero, mientras que su serie $\sum_{k=0}^{\infty}f_k$ no converge **en ningún punto** de $[0,1]$.

**Demostración.**
Tomemos la sucesión armónica numérica del Capítulo 14:

$$
h_n:=\nu_{\mathbb R}(n+1)^{-1},\qquad
f_n(x):=h_n\quad(x\in[0,1]).
\tag{23.6.13}
$$

Cada numerador y denominador está tipado en $\mathbb R$; $\nu_{\mathbb R}(n+1)>0$, así que su inverso existe. Los grafos de las funciones constantes y el de la familia $n\mapsto f_n$ existen por Separación, pues la fórmula da un único valor para cada par $(n,x)$. Cada $f_n$ es continua. Lema §13.10.2 — Los recíprocos de los numerales positivos tienden a cero demuestra que $h_n\to0$; como $|f_n(x)|=|h_n|$ **independientemente de $x$**, un único índice numérico para cada tolerancia verifica la convergencia uniforme de $f_n$ hacia $0_{[0,1]}$.

Sin embargo, en cualquier $x\in[0,1]$, las sumas parciales $S_n(x)$ coinciden, por (23.6.3), con las sumas parciales numéricas de la serie armónica. Proposición §14.2.7 — La condición $a_n\to0$ no es suficiente: la serie armónica prueba que esa serie **diverge**. No existe, pues, un límite de $S_n(x)$ en ningún punto; en particular, no hay función suma ni convergencia uniforme. Se ha demostrado que la condición necesaria del corolario anterior no es suficiente. $\square$

### Proposición 23.6.7 — Una serie de funciones continuas puede converger puntualmente sin hacerlo uniformemente
Existe una serie de funciones continuas en $[0,1]$ que converge puntualmente a una función discontinua, pero no converge uniformemente.

**Demostración.**
Sean $g_n:[0,1]\to\mathbb R$, $g_n(x)=x^n$, las funciones tipadas de Proposición §23.1.7 — Contraejemplo: potencias puntualmente convergentes sin convergencia uniforme; recordemos que $x^0=1$, también para $x=0$. Definimos los términos de una nueva sucesión por

$$
f_0:=g_0,\qquad f_{n+1}:=g_{n+1}-g_n
\quad(n\in\mathbb N).
\tag{23.6.14}
$$

Las diferencias existen como funciones por Proposición §16.3.2 — Existencia y tipado de las operaciones puntuales; la fórmula da un único término en cada índice y, por Separación en $\mathbb N\times\mathbb R^{[0,1]}$, construye la sucesión $\mathbf f$. Cada función $f_n$ es continua porque las potencias lo son (Teorema §17.5.3 — Todo polinomio real es continuo en la recta) y la continuidad se conserva bajo restas (Teorema §17.4.3 — Estabilidad de la continuidad bajo operaciones algebraicas y valor absoluto). Escribamos $\mathbf S=\operatorname{PS}_{[0,1]}(\mathbf f)$. Demostraremos por inducción que

$$
\boxed{S_n=g_n\qquad(n\in\mathbb N).}
\tag{23.6.15}
$$

En $n=0$, $S_0=f_0=g_0$. Si $S_n=g_n$, la recursión y (23.6.14) dan, como igualdad de funciones tipadas sobre $[0,1]$,

$$
S_{n+1}=S_n+f_{n+1}
=g_n+(g_{n+1}-g_n)=g_{n+1}.
$$

Por inducción queda probada (23.6.15): se ha realizado una cancelación **finita**, no un reordenamiento de sumas infinitas. La proposición Proposición §23.1.7 — Contraejemplo: potencias puntualmente convergentes sin convergencia uniforme establece que $g_n=x^n$ converge puntualmente a

$$
F(x)=\begin{cases}0,&0\le x<1,\\1,&x=1,\end{cases}
$$

pero no converge uniformemente en $[0,1]$, y que $F$ no es continua en el extremo $1$. Por (23.6.15) y la Definición 23.6.2, la serie de términos $f_n$ tiene exactamente la misma función suma puntual $F$, sin convergencia uniforme. $\square$

**Transición.** Hemos legitimado las series como sucesiones de sumas parciales, caracterizado su convergencia uniforme por bloques y separado tres hechos diferentes: los términos tienden a cero, la serie converge puntualmente y la serie converge uniformemente. El próximo paso es estudiar la **convergencia absoluta** de una serie de funciones y demostrar el criterio $M$ de Weierstrass, comparando sus bloques con los de una serie numérica convergente. No utilizaremos una norma supremo sin demostrar previamente que sus valores son finitos, ni anticiparemos las series de potencias del Capítulo 24.
