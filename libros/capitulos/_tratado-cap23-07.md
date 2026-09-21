## 23.7. Convergencia absoluta y criterio $M$ de Weierstrass {#sec-ta-23-7}

El criterio de §23.6 controla directamente las sumas de bloques de funciones. Pero una cancelación puede hacer pequeño un bloque aunque sus términos, considerados por separado, tengan magnitudes considerables. La convergencia absoluta permite formular un control más fuerte: sumar primero los valores absolutos de los términos. La comparación con una única serie numérica convergente dará después un criterio que funciona simultáneamente para todos los puntos del dominio.

Como antes, $E\subseteq\mathbb R$ es un conjunto fijo, eventualmente vacío, y $\mathbf f=(f_n)_{n\in\mathbb N}:\mathbb N\to\mathbb R^E$ es una sucesión *dada*. Ninguna conclusión dependerá de que $E$ sea acotado o de que una función alcance un máximo.

### Definición 23.7.1 — Serie de magnitudes y convergencia absoluta puntual y uniforme
Para cada $n\in\mathbb N$ definimos la función de magnitudes $A_n:E\to\mathbb R$ por

$$
\boxed{A_n(x):=|f_n(x)|\qquad(x\in E).}
\tag{23.7.1}
$$

Cada grafo $\{\langle x,r\rangle\in E\times\mathbb R:r=|f_n(x)|\}$ existe por Separación y tiene un valor único en cada $x$. Como la propiedad «$H(x)=|f_n(x)|$ para todo $x\in E$» caracteriza una única función tipada $H\in\mathbb R^E$, Separación en $\mathbb N\times\mathbb R^E$ determina una única sucesión $\mathbf A=(A_n):\mathbb N\to\mathbb R^E$. La serie de magnitudes es la serie de funciones $\sum_{k=0}^{\infty}A_k$, también escrita $\sum_{k=0}^{\infty}|f_k|$ con esta interpretación punto a punto.

Diremos que $\sum f_k$ converge absolutamente en cada punto de $E$ si $\sum A_k$ converge puntualmente en $E$ en el sentido de Definición §23.6.2 — Convergencia puntual, convergencia uniforme y función suma de una serie. Diremos que $\sum f_k$ converge absolutamente de manera uniforme en $E$ si $\sum A_k$ converge uniformemente en $E$. Esta segunda propiedad no se reduce a que, en cada punto por separado, converja la serie numérica $\sum|f_k(x)|$: exige un umbral independiente del punto. Aún no se afirma que la serie original converja; ambas implicaciones se probarán más abajo.

Para $E=\varnothing$, la sucesión de magnitudes es la familia de funciones vacías y ambas nociones se satisfacen por vacuidad. No usamos el supremo de las magnitudes sobre un dominio arbitrario.

### Lema 23.7.2 — Comparación de bloques con magnitudes y mayorantes
Escribamos $\mathbf S=\operatorname{PS}_E(\mathbf f)$ y $\mathbf T=\operatorname{PS}_E(\mathbf A)$. Para todo $n<m$ y todo $x\in E$ se cumple

$$
\boxed{|S_m(x)-S_n(x)|\le T_m(x)-T_n(x)
=\sum_{k=n+1}^{m}|f_k(x)|.}
\tag{23.7.2}
$$

Además, supongamos dada una sucesión real $M:\mathbb N\to\mathbb R$ cuyos términos satisfacen $0\le |f_k(x)|\le M_k$ para todo $k\in\mathbb N$ y todo $x\in E$. Sean $U=\operatorname{PS}(M)$ sus sumas parciales numéricas. Entonces

$$
\boxed{0\le T_m(x)-T_n(x)\le U_m-U_n
=\sum_{k=n+1}^{m}M_k.}
\tag{23.7.3}
$$

**Demostración.**
Fijemos $n<m$ y $x\in E$. Las sucesiones numéricas $a_k=f_k(x)$ y $b_k=|a_k|$ están definidas por evaluación, y sus sumas parciales son respectivamente $S_k(x)$ y $T_k(x)$ por (23.6.3). La desigualdad de bloques numéricos Lema §14.8.2 — Desigualdad triangular para sumas finitas y bloques da $|S_m(x)-S_n(x)|\le T_m(x)-T_n(x)$ y, como cada $b_k\ge0$, el segundo miembro es una suma no negativa. La identidad con la suma finita sigue de Proposición §23.6.3 — Identidades de los bloques finitos de funciones.

Para (23.7.3), consideremos los bloques numéricos $\sum_{k=n+1}^{m}b_k$ y $\sum_{k=n+1}^{m}M_k$. Si $m=n+1$, la desigualdad es $b_{n+1}\le M_{n+1}$. Si vale para un extremo $m>n$, la recursión de bloques Proposición §14.2.2 — Identidades de los bloques de sumación y la hipótesis $b_{m+1}\le M_{m+1}$ permiten añadir los términos respectivos y obtenerla para $m+1$. Por inducción alcanza todos los $m>n$, sin definir sumas vacías. De la no negatividad de los $M_k$ y $b_k$ se obtienen las cotas inferiores. Como $x,n,m$ eran arbitrarios, ambas estimaciones valen simultáneamente en sus dominios de cuantificación; no se han elegido puntos extremos ni familias de testigos. $\square$

### Teorema 23.7.3 — La convergencia absoluta produce convergencia ordinaria
Para una serie de funciones sobre $E$ se verifican las dos implicaciones siguientes:

1. Si converge absolutamente en cada punto de $E$, entonces converge puntualmente en $E$.
2. Si converge absolutamente de manera uniforme en $E$, entonces converge uniformemente en $E$.

En ambos casos, la función suma original sólo se utiliza una vez probada su existencia; no tiene por qué coincidir con la función suma de las magnitudes.

**Demostración.**
Para la primera afirmación, fijemos $x\in E$. La serie numérica de términos $a_k=f_k(x)$ tiene serie de magnitudes $\sum|a_k|=\sum A_k(x)$, convergente por hipótesis. El resultado numérico Teorema §14.8.3 — La convergencia absoluta implica convergencia ordinaria demuestra que $\sum a_k$ converge. Esto vale para cada $x$ y Definición §23.6.2 — Convergencia puntual, convergencia uniforme y función suma de una serie construye la función suma mediante el grafo de límites únicos; no seleccionamos simultáneamente números límite.

Para la segunda, fijemos $\varepsilon>0$. Aplicamos el criterio uniforme de Cauchy Teorema §23.6.4 — Criterio uniforme de Cauchy para series de funciones a la serie de magnitudes, que converge uniformemente: existe $N$ tal que para $N\le n<m$ y todo $x\in E$,

$$
|T_m(x)-T_n(x)|<\varepsilon.
$$

Los términos de magnitudes son no negativos y, por (23.7.2), $0\le|S_m(x)-S_n(x)|\le T_m(x)-T_n(x)<\varepsilon$. El mismo $N$ verifica el criterio Teorema §23.6.4 — Criterio uniforme de Cauchy para series de funciones para la serie original; ésta converge uniformemente. El caso vacío satisface ambas conclusiones por las definiciones de §23.6. $\square$

**Advertencia.** Ni el teorema ni la definición identifican «absoluta en cada punto» con «absoluta uniforme». La primera afirmación aplica un resultado numérico para cada $x$; la segunda necesita además un único umbral para todos los puntos.

### Teorema 23.7.4 — Criterio $M$ de Weierstrass y estimación del resto
Sea $M=(M_n):\mathbb N\to\mathbb R$ una sucesión real dada, con $M_n\ge0$ para todo $n$, y supongamos que la serie numérica $\sum_{n=0}^{\infty}M_n$ converge. Si

$$
\boxed{|f_n(x)|\le M_n\qquad(n\in\mathbb N,\ x\in E),}
\tag{23.7.4}
$$

entonces la serie $\sum_{n=0}^{\infty}f_n$ converge absolutamente de manera uniforme y, por tanto, converge uniformemente a una única función $F:E\to\mathbb R$.

Más precisamente, si $U_n=\sum_{k=0}^{n}M_k$ y $B:=\sum_{k=0}^{\infty}M_k\in\mathbb R$, se tiene para cada $n\in\mathbb N$ y cada $x\in E$ la cota del resto

$$
\boxed{\left|F(x)-S_n(x)\right|\le B-U_n.}
\tag{23.7.5}
$$

El número del lado derecho es no negativo y tiende a cero. No se exige que $E$ sea compacto, no se toma un máximo de $|f_n|$ ni se postula la existencia de $\sup_{x\in E}|f_n(x)|$.

**Demostración.**
Sean $\mathbf A$ la sucesión de magnitudes y $\mathbf T=\operatorname{PS}_E(\mathbf A)$. Puesto que la serie numérica $\sum M_n$ converge, Teorema §14.2.3 — Criterio de Cauchy para una serie numérica proporciona, para cualquier $\varepsilon>0$, un índice $N$ tal que

$$
N\le n<m\quad\Longrightarrow\quad |U_m-U_n|<\varepsilon.
\tag{23.7.6}
$$

Los $M_n$ son no negativos, por lo que $U_m-U_n\ge0$ cuando $n<m$. Aplicando (23.7.3), para todo $x\in E$ y los mismos $N\le n<m$, obtenemos

$$
0\le T_m(x)-T_n(x)\le U_m-U_n<\varepsilon.
\tag{23.7.7}
$$

El criterio Teorema §23.6.4 — Criterio uniforme de Cauchy para series de funciones aplicado a la serie de magnitudes demuestra su convergencia uniforme. Por Teorema §23.7.3 — La convergencia absoluta produce convergencia ordinaria, la serie original también converge uniformemente y tiene una función suma única $F:E\to\mathbb R$.

Para la estimación cuantitativa, fijemos ahora $n$ y $x$. La combinación de (23.7.2) y (23.7.3) proporciona, para todo $m>n$,

$$
|S_m(x)-S_n(x)|\le U_m-U_n.
\tag{23.7.8}
$$

Como $S_m(x)\to F(x)$ y $U_m\to B$, la continuidad del valor absoluto Proposición §13.5.5 — El valor absoluto preserva límites y la preservación de desigualdades al pasar al límite Teorema §13.6.2 — Preservación del orden en el paso al límite dan $|F(x)-S_n(x)|\le B-U_n$. De $U_m\ge U_n$ para todo $m>n$ y la misma preservación del orden resulta $B-U_n\ge0$. La convergencia numérica $U_n\to B$ implica $B-U_n\to0$. Así (23.7.5) es una estimación uniforme en $x$ mediante una sucesión de errores puramente numérica. Si $E$ es vacío, la desigualdad es vacua y la prueba de convergencia permanece válida. $\square$

**Cómo se utiliza.** No necesitamos conocer $F$ para demostrar que existe. Basta construir una serie numérica mayorante convergente y verificar (23.7.4); el resto se controla después por la cola de esa serie mayorante, nunca por una supuesta suma infinita no definida.

### Corolario 23.7.5 — Continuidad de una serie dominada
Supongamos las hipótesis del criterio $M$. Si cada $f_n:E\to\mathbb R$ es continua relativamente a $E$, entonces su función suma $F:E\to\mathbb R$ es continua en todo $E$.

**Demostración.**
La suma parcial $S_0=f_0$ es continua. Si $S_n$ lo es, la ecuación $S_{n+1}=S_n+f_{n+1}$ y la estabilidad algebraica de la continuidad Teorema §17.4.3 — Estabilidad de la continuidad bajo operaciones algebraicas y valor absoluto establecen que $S_{n+1}$ también es continua. Por inducción, todas las $S_n$ son continuas sobre el mismo dominio. El teorema Teorema §23.7.4 — Criterio $M$ de Weierstrass y estimación del resto garantiza $S_n\to F$ uniformemente; Corolario §23.3.2 — Continuidad del límite uniforme en todo el dominio entrega la continuidad de $F$ en cada punto del dominio. Si $E=\varnothing$, ambas nociones son vacuas y la misma conclusión rige. $\square$

### Corolario 23.7.6 — Integración término a término de una serie dominada
Sean $a,b\in\mathbb R$, $a\le b$, y sea $E=[a,b]$. Supongamos que cada $f_n:E\to\mathbb R$ es integrable en el sentido del Capítulo 21 y que se cumplen las hipótesis del criterio $M$. Entonces la función suma $F$ es integrable, la serie numérica de las integrales de los términos converge y

$$
\boxed{\int_a^b F=\sum_{n=0}^{\infty}\left(\int_a^b f_n\right).}
\tag{23.7.9}
$$

El símbolo del lado derecho denota una suma real sólo después de haber establecido su convergencia.

**Demostración.**
Por inducción, $S_0=f_0$ es integrable; si $S_n$ lo es, también $S_{n+1}=S_n+f_{n+1}$ por la linealidad finita Corolario §21.5.7 — Linealidad para combinaciones finitas de dos funciones. Así todas las sumas parciales son integrables. El criterio $M$ demuestra que $S_n\to F$ uniformemente. El teorema Teorema §23.4.2 — El límite uniforme de funciones integrables es integrable implica que $F$ es integrable, antes de escribir su integral.

Cada integral $\int_a^b f_n$ existe y es única, utilizando la definición ordinaria si $a<b$ (Definición §21.4.3 — Integral de Riemann–Darboux para funciones integrables) o la convención para $a=b$ (Definición §21.6.5 — Integración en un intervalo degenerado). Separación en $\mathbb N\times\mathbb R$ construye la sucesión real $c_n:=\int_a^b f_n$. Por inducción, la linealidad finita y la recursión (23.6.1) prueban

$$
\boxed{\int_a^b S_n=\sum_{k=0}^{n}c_k
\qquad(n\in\mathbb N).}
\tag{23.7.10}
$$

No se ha usado linealidad de ninguna suma infinita. El intercambio de límite e integral ya demostrado (Teorema §23.4.3 — Intercambio del límite y la integral), aplicado a la sucesión integrable $(S_n)$, da $\lim_n\int_a^bS_n=\int_a^bF$. Por (23.7.10), las sumas parciales numéricas de $(c_n)$ tienen ese límite: de ahí la convergencia de la serie numérica y la identidad (23.7.9). Cuando $a=b$, todas las integrales son cero y la convención del singleton verifica igualmente el argumento. $\square$

### Proposición 23.7.7 — El criterio $M$ es suficiente, pero no necesario
Existe una serie que converge absolutamente de manera uniforme sobre un dominio real $E$, pero para la cual no existe ninguna sucesión $M_n\ge0$ con $|f_n(x)|\le M_n$ para todo $n,x$ y con $\sum M_n$ convergente.

**Demostración.**
Sea $\nu_{\mathbb R}:\mathbb N\to\mathbb R$ la aplicación de numerales reales, inyectiva por Proposición §4.1.6 — Aritmética y orden de los numerales naturales, y definamos mediante Separación

$$
E:=\{x\in\mathbb R:\exists j\in\mathbb N,\ x=\nu_{\mathbb R}(j)\}.
$$

Para cada $k\in\mathbb N$ establezcamos la función $f_k:E\to\mathbb R$ por

$$
f_k(x):=\begin{cases}
\bigl(\nu_{\mathbb R}(k+1)\bigr)^{-1},&x=\nu_{\mathbb R}(k),\\
0,&x\ne\nu_{\mathbb R}(k).
\end{cases}
\tag{23.7.11}
$$

Los denominadores son estrictamente positivos. Esta fórmula define un único valor para cada $k,x$ y los grafos de $f_k$ y de $k\mapsto f_k$ existen por Separación en $E\times\mathbb R$ y $\mathbb N\times\mathbb R^E$. Cada $f_k$ es no negativa, por lo que su serie de magnitudes coincide con ella. La inyectividad de $\nu_{\mathbb R}$ asegura que, para cualquier $x\in E$, a lo sumo uno de los términos $f_k(x)$ es distinto de cero.

Fijemos $n<m$. El bloque de magnitudes $T_m(x)-T_n(x)$ es, por tanto, cero o igual a $1/\nu_{\mathbb R}(k+1)$ para un único $k$ con $n+1\le k\le m$. Por monotonía de los numerales y del recíproco positivo,

$$
0\le T_m(x)-T_n(x)
\le\frac{1}{\nu_{\mathbb R}(n+2)}
\qquad(x\in E).
\tag{23.7.12}
$$

La sucesión de recíprocos tiende a cero por Lema §13.10.2 — Los recíprocos de los numerales positivos tienden a cero. Dado $\varepsilon>0$, obtenemos un $N$ para el que $1/\nu_{\mathbb R}(n+2)<\varepsilon$ para todo $n\ge N$. La cota (23.7.12) verifica el criterio uniforme Teorema §23.6.4 — Criterio uniforme de Cauchy para series de funciones para la serie de magnitudes: converge absolutamente de manera uniforme.

Ahora supongamos que una sucesión mayorante $M$ como la del criterio $M$ existiese. Al evaluar en el punto explícito $x=\nu_{\mathbb R}(k)$ tendríamos

$$
M_k\ge |f_k(\nu_{\mathbb R}(k))|
=\frac1{\nu_{\mathbb R}(k+1)}.
$$

El criterio de comparación directa Teorema §14.5.2 — Criterio de comparación directa implicaría que la convergencia de $\sum M_k$ fuerza la convergencia de la serie armónica $\sum1/\nu_{\mathbb R}(k+1)$; esto contradice Proposición §14.2.7 — La condición $a_n\to0$ no es suficiente: la serie armónica. Por lo tanto, el criterio $M$ no es una caracterización de la convergencia absoluta uniforme, aunque siempre la garantiza cuando sus hipótesis se cumplen. $\square$

**Transición.** La teoría precedente parte de una sucesión arbitraria de funciones y separa rigurosamente la convergencia de sus sumas parciales de la convergencia de los términos. El Capítulo 24 estudiará la familia especial de las series de potencias: habrá que determinar dónde convergen, introducir y justificar su radio de convergencia y demostrar, con las hipótesis apropiadas, las operaciones de continuidad, derivación e integración de sus funciones suma. El criterio $M$ y la diferenciación bajo convergencia uniforme de derivadas estarán disponibles como herramientas, pero no convertirán esas conclusiones en axiomas ni autorizarán operaciones fuera de los conjuntos de convergencia probados.
