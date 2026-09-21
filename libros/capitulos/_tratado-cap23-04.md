## 23.4. Intercambio del límite y la integral de Riemann {#sec-ta-23-4}

Una función acotada no tiene por qué ser integrable, como mostró Proposición §21.4.6 — Una función acotada que no es integrable. Por eso, incluso si todos los términos de una sucesión son integrables, **no es lícito escribir la integral del límite antes de probar su existencia**. La demostración utilizará primero la estabilidad cuantitativa de las sumas de Darboux ante una perturbación uniformemente pequeña. Solamente después de establecer la integrabilidad de la función límite podremos comparar las integrales. En esta sección $a,b$ son reales con $a\le b$; cada integral sobre un intervalo no degenerado conserva la definición del Capítulo 21 y el caso $a=b$ se rige exclusivamente por Definición §21.6.5 — Integración en un intervalo degenerado.

### Lema 23.4.1 — Control de las sumas de Darboux bajo perturbación uniforme
Sean $a<b$, $g:[a,b]\to\mathbb R$ una función acotada y $h:[a,b]\to\mathbb R$ otra función. Si $\eta\ge0$ verifica

$$
|h(t)-g(t)|\le\eta\qquad(t\in[a,b]),
\tag{23.4.1}
$$

entonces $h$ es acotada y, para toda partición $P$ del intervalo, se cumplen

$$
\begin{aligned}
|L(h,P)-L(g,P)|&\le\eta(b-a),\\
|U(h,P)-U(g,P)|&\le\eta(b-a),
\end{aligned}
\tag{23.4.2}
$$

$$
\boxed{0\le U(h,P)-L(h,P)
\le U(g,P)-L(g,P)+2\eta(b-a).}
\tag{23.4.3}
$$

**Demostración.**
Elijamos una pareja de cotas globales $A\le g(t)\le B$, cuya existencia procede de la acotación de $g$. De (23.4.1) resulta

$$
A-\eta\le h(t)\le B+\eta\qquad(t\in[a,b]),
$$

así que $h$ también está acotada. Fijemos ahora una partición $P$ y una de sus celdas cerradas no vacías $I$. Por Lema §21.2.2 — Existencia de las cotas extremas locales y comparación por inclusión, están definidos los cuatro extremos finitos

$$
m_g(I)=\inf g[I],\quad M_g(I)=\sup g[I],\quad
m_h(I)=\inf h[I],\quad M_h(I)=\sup h[I].
$$

Las desigualdades $g-\eta\le h\le g+\eta$ implican, por las propiedades definitorias del ínfimo y del supremo,

$$
m_g(I)-\eta\le m_h(I)\le m_g(I)+\eta,
\qquad M_g(I)-\eta\le M_h(I)\le M_g(I)+\eta.
\tag{23.4.4}
$$

Para justificar también los extremos derechos sin suponer máximos o mínimos alcanzados, escribimos la comparación equivalente $h-\eta\le g\le h+\eta$ e intercambiamos los papeles de ambas funciones; ya sabemos que las dos están acotadas. Multiplicamos (23.4.4) por la anchura positiva de cada celda y sumamos sobre las celdas de $P$. La identidad finita de anchuras Proposición §21.1.2 — Existencia, anchuras positivas y suma de longitudes da $\sum_k\Delta_k(P)=b-a$. Así,

$$
L(g,P)-\eta(b-a)\le L(h,P)\le L(g,P)+\eta(b-a),
$$

con las dos desigualdades análogas para $U$. Se sigue (23.4.2). Restando la cota inferior de $L(h,P)$ de la cota superior de $U(h,P)$ obtenemos (23.4.3); su primer miembro es no negativo por Proposición §21.2.5 — Encierro global e identidad de la brecha. No se escoge un punto que realice ninguno de los extremos: sólo se utilizan sus propiedades de orden. $\square$

**Lectura.** Una perturbación de tamaño a lo sumo $\eta$ puede desplazar cada suma inferior y superior a lo sumo $\eta(b-a)$. El factor $2$ aparece al comparar simultáneamente ambos extremos; todavía **no** representa una cota para diferencias de integrales, porque $h$ podría no ser integrable.

### Teorema 23.4.2 — El límite uniforme de funciones integrables es integrable
Sea $a\le b$, y sea $(f_n)_{n\in\mathbb N}$ una sucesión de funciones tipadas $f_n:[a,b]\to\mathbb R$. Si **cada** $f_n$ es integrable y $f_n$ converge uniformemente a $f:[a,b]\to\mathbb R$, entonces $f$ es integrable en $[a,b]$.

**Demostración.**
Si $a=b$, toda función $[a,a]\to\mathbb R$ es integrable por Definición §21.6.5 — Integración en un intervalo degenerado; esto incluye a $f$ sin construir una partición imposible del singleton.

Supongamos $a<b$ y pongamos $\ell:=b-a>0$. Fijemos una tolerancia arbitraria $\varepsilon>0$ y definamos expresamente $\eta:=\varepsilon/(4\ell)>0$. La convergencia uniforme proporciona **un** $N\in\mathbb N$ tal que

$$
|f(t)-f_N(t)|<\eta\qquad(t\in[a,b]).
\tag{23.4.5}
$$

El término $f_N$ es integrable y, por tanto, acotado según Definición §21.4.1 — Integrabilidad de Darboux por igualdad de integrales extremas. El lema anterior, con $g=f_N$ y $h=f$, demuestra primero que $f$ está acotada; además, para cualquier partición $P$,

$$
U(f,P)-L(f,P)
\le U(f_N,P)-L(f_N,P)+2\eta\ell.
\tag{23.4.6}
$$

Apliquemos el criterio de Darboux Teorema §21.4.2 — Criterio de Darboux y estabilidad por refinamiento a **ese término fijo** $f_N$, con tolerancia $\varepsilon/2$. Existe una partición $P$ tal que

$$
U(f_N,P)-L(f_N,P)<\frac\varepsilon2.
$$

Como $2\eta\ell=\varepsilon/2$, (23.4.6) implica

$$
0\le U(f,P)-L(f,P)<\varepsilon.
$$

La función $f$ ya está demostrada acotada y posee, para cada $\varepsilon>0$, una partición con brecha inferior a $\varepsilon$. Por el criterio de Darboux es integrable. La prueba no forma una sucesión $P_N$ ni elige simultáneamente particiones para infinitos índices o tolerancias: fija una tolerancia, obtiene un término y encuentra una sola partición. $\square$

**Interpretación.** Este resultado es más fuerte que la continuidad del límite uniforme: los términos no han de ser continuos. Basta que sus integrales de Riemann existan, incluso cuando presenten discontinuidades.

### Teorema 23.4.3 — Intercambio del límite y la integral
Bajo las hipótesis del teorema anterior, existe la sucesión real de integrales

$$
I:\mathbb N\to\mathbb R,
\qquad I(n):=\int_a^b f_n,
$$

y satisface

$$
\boxed{\lim_{n\to\infty}\int_a^b f_n
=\int_a^b f.}
\tag{23.4.7}
$$

**Demostración.**
Teorema §23.4.2 — El límite uniforme de funciones integrables es integrable asegura que $f$ es integrable. Como cada $f_n$ también lo es, **sólo ahora** tienen sentido todas las integrales de (23.4.7). Cada integral es un real unívocamente determinado por Definición §21.4.3 — Integral de Riemann–Darboux para funciones integrables si $a<b$, o por Definición §21.6.5 — Integración en un intervalo degenerado si $a=b$. El grafo

$$
\bigl\{\langle n,r\rangle\in\mathbb N\times\mathbb R:
 r=\textstyle\int_a^b f_n\bigr\}
$$

existe por Separación y define la sucesión real $I$; no requiere elegir valores entre múltiples candidatos.

Si $a=b$, todas las integrales del enunciado son cero por definición, de modo que (23.4.7) es la convergencia de una sucesión constante. Supongamos $a<b$ y escribamos $\ell=b-a>0$. Fijemos $\varepsilon>0$ y usemos uniformidad con $\eta:=\varepsilon/(2\ell)$. Obtenemos $N$ tal que, para $n\ge N$ y $t\in[a,b]$,

$$
-\eta\le f_n(t)-f(t)\le\eta.
$$

Las funciones $f_n$ y $f$ son integrables, así que su diferencia puntual $d_n:=f_n-f$ también es integrable por la linealidad Corolario §21.5.7 — Linealidad para combinaciones finitas de dos funciones. La estimación por cotas constantes Corolario §21.5.8 — Positividad y estimaciones por cotas constantes, ahora aplicada a $d_n$, implica

$$
-\eta\ell\le\int_a^b d_n\le\eta\ell.
$$

Por la misma linealidad,

$$
\left|\int_a^b f_n-\int_a^b f\right|
=\left|\int_a^b d_n\right|
\le\eta\ell=\frac\varepsilon2<\varepsilon.
\tag{23.4.8}
$$

El umbral $N$ vale para **todos** los índices de la cola y demuestra precisamente la convergencia numérica de $I$ a $\int_a^b f$ (Definición §13.3.1 — Convergencia de una sucesión real). No hemos supuesto que una integral conmute con un límite: lo acabamos de deducir de una cota previamente legitimada. $\square$

### Corolario 23.4.4 — Convergencia uniforme de las integrales acumuladas
Sean $a<b$ y $(f_n)$ como en el teorema anterior. Para cada $n$, denotemos por $F_n:=F_{f_n,a}:[a,b]\to\mathbb R$ la acumulada de Definición §22.1.1 — Función integral acumulada, y por $F:=F_{f,a}$ la acumulada del límite. Entonces $(F_n)_{n\in\mathbb N}$ es una sucesión de funciones bien definida y converge **uniformemente** a $F$ sobre $[a,b]$.

**Demostración.**
Todas las integrandas $f_n$, así como $f$ por Teorema §23.4.2 — El límite uniforme de funciones integrables es integrable, son integrables. Definición §22.1.1 — Función integral acumulada produce para cada una su única acumulada, con **dominio exacto** $[a,b]$ y codominio $\mathbb R$. El predicado «$H=F_{f_n,a}$» tiene valor único en el conjunto existente $\mathbb R^{[a,b]}$; mediante Separación en $\mathbb N\times\mathbb R^{[a,b]}$ construimos el grafo de $n\mapsto F_n$, sin escoger funciones.

Fijemos $\varepsilon>0$ y pongamos $\ell=b-a>0$, $\eta=\varepsilon/(2\ell)$. La convergencia uniforme de $f_n$ a $f$ proporciona $N$ tal que $|f_n(t)-f(t)|<\eta$ para todos $n\ge N$ y $t\in[a,b]$. Sea $x\in[a,b]$ arbitrario. Si $x=a$, ambas acumuladas valen cero por la convención singleton. Si $a<x\le b$, Corolario §21.6.6 — Aditividad para todo punto del intervalo cerrado garantiza la integrabilidad de las restricciones de $f_n$ y $f$ a $[a,x]$; su diferencia también es integrable por Corolario §21.5.7 — Linealidad para combinaciones finitas de dos funciones. La linealidad y la estimación de Corolario §21.5.8 — Positividad y estimaciones por cotas constantes en este subintervalo dan

$$
\begin{aligned}
|F_n(x)-F(x)|
&=\left|\int_a^x\bigl((f_n-f)\upharpoonright[a,x]\bigr)\right|\\
&\le\eta(x-a)\le\eta(b-a)=\frac\varepsilon2<\varepsilon.
\end{aligned}
\tag{23.4.9}
$$

La restricción de la diferencia coincide punto a punto y por tipo con la diferencia de las restricciones. Puesto que el mismo $N$ precede a la elección de $x$, (23.4.9) demuestra la uniformidad de la convergencia sobre **todo** $[a,b]$. El corolario no pretende extender la definición de acumulada a un intervalo degenerado. $\square$

**Interpretación.** El teorema 23.4.3 compara dos números correspondientes a un extremo final fijo. El corolario controla simultáneamente **todos los extremos variables** y prepara el anclaje necesario para estudiar límites de derivadas en §23.5.

### Proposición 23.4.5 — La convergencia puntual no basta para intercambiar límite e integral
Existe una sucesión de funciones continuas $u_n:[0,1]\to\mathbb R$ que converge puntualmente a la función nula, mientras que **todas** sus integrales son iguales a $1$. Por tanto, aun cuando todos los términos y el límite sean integrables, la convergencia puntual no garantiza (23.4.7).

**Demostración.**
Sea $m_n:=\nu_{\mathbb R}(n+2)\ge2$ el numeral **real** correspondiente al natural $n+2$. Para $x\in[0,1]$ definimos

$$
u_n(x):=
\begin{cases}
m_n^2x,&0\le x\le 1/m_n,\\
2m_n-m_n^2x,&1/m_n<x\le 2/m_n,\\
0,&2/m_n<x\le1.
\end{cases}
\tag{23.4.10}
$$

Cada condición corresponde a uno de tres casos disjuntos y exhaustivos, con divisores no nulos. Por Separación en $[0,1]\times\mathbb R$ obtenemos el grafo de una función tipada $u_n$ y, mediante la fórmula conjunta en $\mathbb N\times\mathbb R^{[0,1]}$, el de la sucesión $(u_n)$. Los dos polinomios de la fórmula coinciden en $x=1/m_n$, donde valen $m_n$, y el segundo coincide con la función cero en $x=2/m_n$, donde vale $0$; si $m_n=2$, el último tramo es vacío. Cada rama es continua en su subintervalo por los resultados de continuidad de polinomios del Capítulo 17. En cada punto de unión, las continuidades relativas de las dos ramas proporcionan, para una tolerancia fija, dos radios que combinamos con un mínimo finito. Como sus valores en la unión coinciden, este radio prueba la continuidad de $u_n$ allí. Fuera de las uniones, la continuidad es la de una sola rama. Así $u_n$ es continua en $[0,1]$ y, por Corolario §21.7.4 — Toda función continua en un intervalo cerrado es integrable, integrable.

Para $x=0$ tenemos $u_n(0)=0$ para todo $n$. Si $x>0$ está fijo, la propiedad arquimediana Teorema §4.6.3 — Todo cuerpo ordenado completo es arquimediano permite tomar $N$ tal que $m_n>2/x$ para $n\ge N$; entonces $x>2/m_n$ y $u_n(x)=0$. En consecuencia,

$$
u_n(x)\longrightarrow0\qquad\text{para cada }x\in[0,1].
\tag{23.4.11}
$$

Calculemos ahora las integrales. Las primitivas polinómicas $p_n(t)=m_n^2t^2/2$ y $q_n(t)=2m_nt-m_n^2t^2/2$ tienen por derivadas, respectivamente, las dos primeras expresiones de (23.4.10). El teorema fundamental del cálculo, aplicado a esas funciones continuas **en sus intervalos tipados**, proporciona

$$
\int_0^{1/m_n}u_n
=\left[\frac{m_n^2t^2}{2}\right]_{0}^{1/m_n}
=\frac12,
\qquad
\int_{1/m_n}^{2/m_n}u_n
=\left[2m_nt-\frac{m_n^2t^2}{2}\right]_{1/m_n}^{2/m_n}
=\frac12.
\tag{23.4.12}
$$

En estas expresiones, las integrales sobre los subintervalos designan las de las correspondientes **restricciones tipadas**. El tramo $[2/m_n,1]$, si tiene longitud positiva, es idénticamente nulo y posee integral cero; si sus extremos coinciden, su integral también es cero por Definición §21.6.5 — Integración en un intervalo degenerado. La aditividad Corolario §21.6.6 — Aditividad para todo punto del intervalo cerrado, aplicada sucesivamente en $1/m_n$ y $2/m_n$, concluye

$$
\boxed{\int_0^1u_n=\frac12+\frac12+0=1\quad(n\in\mathbb N).}
\tag{23.4.13}
$$

La función límite $u(x)=0$ es integrable, pero $\int_0^1u=0$ por Proposición §21.5.1 — Acotación de las operaciones y cálculo de las constantes. Por ello, la sucesión de integrales constante igual a $1$ no converge a la integral del límite. Más aún, la convergencia no es uniforme: en el punto determinado $x_n:=1/m_n$ se tiene $|u_n(x_n)-u(x_n)|=m_n\ge2$, lo que contradice el requisito uniforme para $\varepsilon=1$. No se ha elegido ningún punto mediante un principio de elección: $x_n$ viene dado por una fórmula. $\square$

**Lectura del contraejemplo.** Los triángulos se estrechan hacia el origen, de manera que cada punto fijo termina fuera de sus soportes; al mismo tiempo, su altura crece y su área permanece igual a uno. La convergencia puntual sólo detecta lo primero. La estimación uniforme de (23.4.8) impide lo segundo cuando existe convergencia uniforme.

**Transición.** La integración se comporta de manera estable ante convergencia uniforme, y también lo hacen las acumuladas. Para la diferenciación, en cambio, la convergencia uniforme de las funciones por sí sola no será suficiente. En §23.5 estudiaremos la convergencia uniforme de las derivadas y una condición de anclaje que permita recuperar los valores de las funciones.
