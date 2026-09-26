## 24.7. Radio de la serie derivada y derivación término a término {#sec-ta-24-7}

En §24.6 construimos una primitiva mediante la integración de la serie original; ese hecho no autoriza a derivar una sucesión de sumas parciales e intercambiar derivada con límite. El Capítulo 23 exige controlar uniformemente las funciones derivadas y verificar un anclaje. En esta sección probaremos primero que la serie derivada posee el mismo radio que la serie inicial, después construiremos su límite uniforme en cerrados interiores y, sólo al final, aplicaremos el teorema de diferenciación bajo límite uniforme de derivadas. La marca formal $+\infty$ seguirá tratándose por casos, sin operaciones con infinitos.

### Definición 24.7.1 — Coeficientes de la serie derivada formal
Dados $a:\mathbb N\to\mathbb R$ y $c\in\mathbb R$, definimos una nueva sucesión real $b=\partial a:\mathbb N\to\mathbb R$ por

$$
\boxed{b_n:=(n+1)a_{n+1}\quad(n\in\mathbb N).}
\tag{24.7.1}
$$

Todos los numerales en productos con reales designan su imagen canónica en $\mathbb R$. El grafo $\{\langle n,t\rangle\in\mathbb N\times\mathbb R:t=(n+1)a_{n+1}\}$ existe por Separación y tiene un valor real único por índice; no se eligen coeficientes. La serie derivada formal, considerada inicialmente como otra serie de potencias según «Serie de potencias real centrada», es

$$
\boxed{\sum_{n=0}^{\infty}b_n(x-c)^n
=\sum_{n=1}^{\infty}n a_n(x-c)^{n-1}.}
\tag{24.7.2}
$$

La segunda expresión es una reindexación de sumas parciales: el índice $n=0$ de la primera corresponde al índice $1$ de la segunda. Todavía no se afirma ni convergencia ni igualdad con $F_{a,c}'$; el símbolo $\partial$ designa una transformación algebraica de coeficientes, no una derivada funcional ya legitimada.

### Lema 24.7.2 — Absorción del factor lineal por una razón geométrica mayor
Sean reales $0\le q<s<1$. Entonces existe una cota explícita $B>0$ tal que, para todo natural $n$,

$$
\boxed{(n+1)q^n\le B s^n,
\qquad B:=\frac{1}{1-q/s}.}
\tag{24.7.3}
$$

**Demostración.**
Como $s>0$, el cociente $t:=q/s$ está definido y satisface $0\le t<1$. Por la monotonía de las potencias de una base en $[0,1)$ respecto del exponente, para $0\le k\le n$ tenemos $t^n\le t^k$; la afirmación comprende $t=0$ y $n=0$ mediante $0^0=1$. Sumando $n+1$ desigualdades finitas se obtiene

$$
(n+1)t^n\le\sum_{k=0}^{n}t^k
=\frac{1-t^{n+1}}{1-t}\le\frac1{1-t}.
\tag{24.7.4}
$$

La fórmula finita es la identidad geométrica de «Convergencia y suma de la serie geométrica para $», y la última desigualdad utiliza $t^{n+1}\ge0$ y $1-t>0$. Al multiplicar por $s^n\ge0$ resulta $(n+1)q^n\le s^n/(1-q/s)$. El número $B$ propuesto es un real positivo independiente de $n$; no se ha derivado la serie geométrica para construirlo. $\square$

### Teorema 24.7.3 — Igualdad exacta de los radios de la serie y su derivada formal
Para toda sucesión real $a$ y todo centro $c$, si $b=\partial a$, los radios definidos mediante «Radio finito y radio infinito» satisfacen

$$
\boxed{R(b,c)=R(a,c).}
\tag{24.7.5}
$$

La igualdad incluye por separado los casos $R=0$, $0<R\in\mathbb R$ y $R=+\infty$; en este último caso significa igualdad de marcas formales, no una operación aritmética. No se afirma igualdad de los conjuntos completos de convergencia en los extremos.

**Demostración.**
1. De la convergencia original a la de la serie derivada, estrictamente hacia dentro. Sea $y\in C(a,c)$ con distancia $d:=|y-c|>0$. El lema «Acotación de los términos al converger una serie numérica» aplicado a la serie numérica convergente en $y$ proporciona un solo $M>0$ con $|a_k|d^k\le M$ para todo natural $k$. Fijemos $x$ con $h:=|x-c|<d$ y pongamos $q:=h/d\in[0,1)$. Para cada $n\ge0$, la identidad (24.7.1) y la cota en $k=n+1$ dan

$$
\begin{aligned}
|b_n(x-c)^n|
&=(n+1)|a_{n+1}|h^n\\
&\le\frac{M}{d}(n+1)q^n.
\end{aligned}
\tag{24.7.6}
$$

No se ha dividido por $h$, por lo que $x=c$ está incluido. Escojamos explícitamente $s:=(1+q)/2$, de modo que $0\le q<s<1$. Por «Absorción del factor lineal por una razón geométrica mayor» el lado derecho está dominado por $[M/(d(1-q/s))]s^n$. La serie de esta última expresión converge por la serie geométrica y la regla de multiplicación por un escalar. El criterio de comparación «Criterio de comparación directa» y la convergencia absoluta «La convergencia absoluta implica convergencia ordinaria» demuestran

$$
\boxed{y\in C(a,c),\ d>0,\ |x-c|<d
\ \Longrightarrow\ x\in C(b,c).}
\tag{24.7.7}
$$

2. De la serie derivada a la original, estrictamente hacia dentro. Recíprocamente, sea $y\in C(b,c)$ con $d:=|y-c|>0$. Ahora «Acotación de los términos al converger una serie numérica» da $M>0$ con

$$
|(n+1)a_{n+1}|d^n\le M\qquad(n\in\mathbb N).
\tag{24.7.8}
$$

Para un punto $x$ con $h:=|x-c|<d$, y $q=h/d\in[0,1)$, el término inicial $a_0$ es finito, mientras que para todo $n\ge0$,

$$
\begin{aligned}
|a_{n+1}(x-c)^{n+1}|
&=|(n+1)a_{n+1}(y-c)^n|\,
\frac{h}{n+1}q^n\\
&\le Mhq^n.
\end{aligned}
\tag{24.7.9}
$$

En la igualdad se usan únicamente denominadores $d^n$ y $n+1$, ambos no nulos en los lugares correspondientes; para $n=0$, $d^0=1$. Si $h=0$, el lado derecho es cero y todos los términos originales de índice positivo se anulan. Para $0<h<d$, la serie geométrica mayorante converge. Incorporar el único término inicial $a_0$ no altera la convergencia absoluta. En ambos casos

$$
\boxed{y\in C(b,c),\ d>0,\ |x-c|<d
\ \Longrightarrow\ x\in C(a,c).}
\tag{24.7.10}
$$

**3. Comparación de los radios, sin dividir por infinitos.** Escribamos $D_a:=D(a,c)$ y $D_b:=D(b,c)$. Las implicaciones (24.7.7) y (24.7.10) establecen: para cada $d>0$ de cualquiera de los dos conjuntos de distancias, toda distancia $0\le h<d$ pertenece al otro. En efecto, basta tomar el punto explícito $x=c+h$; la existencia del punto $y$ para el $d$ fijo está incluida en la definición de $D$. Ambos conjuntos contienen cero por «El centro siempre pertenece al conjunto de convergencia».

Si $D_a$ es no acotado superiormente, para un umbral real arbitrario $T$ existe $d\in D_a$ con $d>\max\{T,0\}+2$. El real explícito $h:=(d+\max\{T,0\})/2$ satisface $0<h<d$ y $h>T$; luego $h\in D_b$. Por tanto $D_b$ tampoco está acotado. La implicación contraria se demuestra intercambiando $a$ y $b$. Por definición, ambos radios son infinitos simultáneamente.

Queda el caso en que los dos conjuntos están acotados. Sean $A:=\sup D_a$ y $B:=\sup D_b$, reales no negativos, cuyas existencias ya están justificadas. Si $A<B$, el número $A$ no es cota superior de $D_b$, de modo que existe $d\in D_b$ con $d>A$. Entonces $h:=(A+d)/2$ satisface $A<h<d$ y, por (24.7.10), $h\in D_a$, en contradicción con que $A$ sea cota superior. Si $B<A$, se usa simétricamente (24.7.7) y se contradice la propiedad de cota superior de $B$. Por tricotomía $A=B$, incluso cuando ambos valen cero. Ésta es exactamente (24.7.5). Los argumentos sólo instancian existenciales para umbrales fijados; no introducen una sucesión de testigos ni Choice. $\square$

### Teorema 24.7.4 — Convergencia absoluta uniforme de la serie derivada en cada cerrado interior
Supongamos $R:=R(a,c)>0$ finito o $R(a,c)=+\infty$ como marca formal. Sea $I$ el dominio abierto interior definido en «Continuidad de la función suma en el interior» y sea $b=\partial a$. Entonces existe la función suma restringida de la serie derivada

$$
\boxed{G_{a,c}:=F_{b,c}\upharpoonright I:I\longrightarrow\mathbb R,
\qquad G_{a,c}(x)=\sum_{n=0}^{\infty}b_n(x-c)^n.}
\tag{24.7.11}
$$

Para cada $r\ge0$ con $r<R$ si $R$ es real positivo, o arbitrario si el radio es infinito, la serie derivada converge absoluta y uniformemente en $K_r=[c-r,c+r]$ a $G_{a,c}\upharpoonright K_r$. Más precisamente, existen reales $B>0$ y $0<s<1$, independientes de $x\in K_r$ y de $n$, con

$$
\boxed{|b_n(x-c)^n|\le Bs^n
\quad(n\in\mathbb N,\ x\in K_r),}
\tag{24.7.12}
$$

lo que proporciona, para cada $N$, una estimación uniforme del resto de la serie derivada:

$$
\boxed{\forall x\in K_r:\quad
\left|G_{a,c}(x)-\sum_{n=0}^{N}b_n(x-c)^n\right|
\le\frac{Bs^{N+1}}{1-s}.}
\tag{24.7.13}
$$

**Demostración.**
Por el teorema anterior, $R(b,c)=R(a,c)$ en los tres casos de radio. La clasificación «Clasificación por el radio y convergencia interior» garantiza, bajo las hipótesis actuales, $I\subseteq C(b,c)$; por «Existencia y unicidad de la función suma sobre su dominio exacto» está por tanto bien definida la restricción (24.7.11), con dominio y codominio exactos.

Fijemos una sola vez el real $r$ del enunciado. Como en el paso 1 de «Convergencia absoluta uniforme y cota geométrica del resto», hay una distancia $d\in D(a,c)$ con $d>r$: en el caso finito, $r<\sup D(a,c)$ y no puede ser cota superior; en el infinito, $D(a,c)$ es no acotado. La pertenencia de $d$ suministra un solo $y\in C(a,c)$ con $|y-c|=d>0$. El lema «Acotación de los términos al converger una serie numérica» da $M>0$ con $|a_k|d^k\le M$ para todo $k$. Definamos explícitamente

$$
q:=r/d,\qquad s:=(1+q)/2,
\qquad B:=\frac{M}{d(1-q/s)}.
\tag{24.7.14}
$$

Se tiene $0\le q<s<1$ y $B>0$. Para todos $n\in\mathbb N$ y $x\in K_r$ simultáneamente, $|x-c|\le r$ y, por el paso 1 de (24.7.6) y el lema 24.7.2,

$$
|b_n(x-c)^n|\le\frac{M}{d}(n+1)q^n
\le Bs^n.
\tag{24.7.15}
$$

Para $r=0$ la convención $0^0=1$ asegura también la desigualdad en $n=0$; los demás términos se anulan en el centro. La serie de números positivos $\sum Bs^n$ converge. El criterio $M$ «Criterio $M$ de Weierstrass y estimación del resto» prueba convergencia absoluta y uniforme de la serie restringida y da el resto (24.7.13), mediante la suma geométrica $Bs^{N+1}/(1-s)$. El límite único es la restricción de $F_{b,c}$, pues coincide con ella punto por punto por la definición de suma y la unicidad del límite real. Ninguna cota depende de $x$; ningún valor se definió fuera del dominio probado. $\square$

### Teorema 24.7.5 — Derivación término a término en el interior del radio
Si el radio $R(a,c)$ es finito positivo o infinito, la función $F_{a,c}\upharpoonright I:I\to\mathbb R$ es derivable en cada punto interior $x\in I$ y satisface

$$
\boxed{\left(F_{a,c}\upharpoonright I\right)'(x)
=\sum_{n=1}^{\infty}n a_n(x-c)^{n-1}
=G_{a,c}(x).}
\tag{24.7.16}
$$

La serie de derivadas converge absoluta y uniformemente en cada $K_r$ interior, como se probó antes; no se afirma derivabilidad en los extremos del radio finito, aunque alguno pertenezca al conjunto de convergencia. Si $R(a,c)=0$, $F_{a,c}$ tiene sólo el dominio $\{c\}$ y el enunciado no le atribuye una derivada bilateral.

**Demostración.**
Fijemos $x_0\in I$ y definamos $d_0:=|x_0-c|$. Si el radio es finito positivo, tomemos $r:=(d_0+R)/2$; si es infinito, $r:=d_0+1$. En ambos casos $r>d_0\ge0$, luego $r>0$, y $x_0,c\in(c-r,c+r)$; además $K_r=[c-r,c+r]\subseteq I$. El uso de un $r$ estrictamente positivo permite aplicar el teorema del Capítulo 23, que exige un intervalo cerrado no degenerado.

Consideremos, sobre el dominio fijo $K_r$, las funciones polinómicas

$$
f_N:=S_{N+1}^{a,c}\upharpoonright K_r,
\qquad N\in\mathbb N.
\tag{24.7.17}
$$

Las $f_N$ son continuas en todo $K_r$ («Todo polinomio real es continuo en la recta») y derivables en su interior. El lema «Integral de cada monomio centrado sobre un intervalo ordenado» ya demostró la fórmula de derivación de cada potencia centrada; por linealidad finita de la derivada («Multiplicación por escalares, opuestos y diferencias») y derivada nula de la constante, para todo $t\in(c-r,c+r)$,

$$
\begin{aligned}
f_N'(t)
&=\sum_{k=1}^{N+1}k a_k(t-c)^{k-1}\\
&=\sum_{n=0}^{N}(n+1)a_{n+1}(t-c)^n
=\sum_{n=0}^{N}b_n(t-c)^n.
\end{aligned}
\tag{24.7.18}
$$

El desplazamiento $N\mapsto N+1$ evita perder el primer término derivado: $f_N'$ coincide con la suma parcial de índice $N$ de la serie derivada. Sus grafos y el grafo de la sucesión de derivadas interiores provienen de fórmulas de valor único; cumplen el tipado de «Sucesión de derivadas interiores de una sucesión dada» sin selección.

Por «Convergencia absoluta uniforme de la serie derivada en cada cerrado interior», las derivadas $f_N'$ convergen uniformemente a $G_{a,c}\upharpoonright(c-r,c+r)$: la convergencia en todo $K_r$ implica la uniformidad en su subconjunto interior. Para el anclaje tomamos el mismo punto $c$ para todos los índices; la proposición «El centro siempre pertenece al conjunto de convergencia» da

$$
f_N(c)=S_{N+1}^{a,c}(c)=a_0\qquad(N\in\mathbb N),
\tag{24.7.19}
$$

una sucesión constante convergente. Todas las hipótesis de «El anclaje y las derivadas uniformemente convergentes producen un límite uniforme» y «Diferenciación bajo límite uniforme de derivadas» quedan así verificadas en el intervalo cerrado no degenerado $K_r$, cuyo interior es $(c-r,c+r)$. Esos teoremas proporcionan una función límite uniforme $f:K_r\to\mathbb R$, derivable en el interior, con $f'=G_{a,c}$ allí.

Identifiquemos el límite sin presuponer la conclusión: por «Convergencia absoluta uniforme y cota geométrica del resto», las sumas parciales $S_N^{a,c}\upharpoonright K_r$ convergen uniformemente a $F_{a,c}\upharpoonright K_r$; su cola $S_{N+1}^{a,c}$ tiene el mismo límite. Por unicidad puntual y de funciones tipadas, el $f$ construido por el capítulo 23 coincide con $F_{a,c}\upharpoonright K_r$. En particular,

$$
\bigl(F_{a,c}\upharpoonright K_r\bigr)'(x_0)
=G_{a,c}(x_0).
\tag{24.7.20}
$$

Puesto que $x_0$ es interior de $K_r$ y éste está contenido en $I$, la restricción de $F_{a,c}$ a $K_r$ y su restricción a $I$ tienen idénticos cocientes incrementales para todo argumento suficientemente cercano a $x_0$; la igualdad (24.7.20) es por ello la derivada de $F_{a,c}\upharpoonright I$ en $x_0$. Como $x_0$ era arbitrario, obtenemos la primera igualdad de (24.7.16); la segunda es la definición de $G_{a,c}$ y la reindexación demostrada en (24.7.2). La única convergencia de derivadas utilizada es la que acabamos de establecer por mayoración geométrica; no se intercambiaron límites formalmente ni se usó Choice. $\square$

Ejemplo de frontera: los radios coinciden, pero los extremos convergentes pueden cambiar. Para $c=0$, tomemos la sucesión explícita $a_n=1/((n+1)(n+2))$. En §24.3 quedó probado que la serie $\sum a_nx^n$ tiene radio $1$ y converge absolutamente en los dos extremos. En el extremo derecho, sin embargo, los términos de su serie derivada son, para $n\ge1$,

$$
\frac{n}{(n+1)(n+2)}
=\frac1{n+1}\frac{n}{n+2}
\ge\frac1{3(n+1)}.
\tag{24.7.21}
$$

La serie armónica diverge («La condición $a_n\to0$ no es suficiente: la serie armónica»); si la serie no negativa de derivadas convergiera, la comparación forzaría la convergencia de un tercio de la armónica, contradicción. Por tanto la serie original converge en $x=1$ mientras que su serie derivada diverge allí, aunque ambos radios son iguales por el teorema 24.7.3. Este ejemplo no determina por sí solo si la función suma admite alguna derivada unilateral en $1$: los teoremas de esta sección sólo operan en el abierto interior.

**Balance y transición.** La serie derivada quedó construida con coeficientes y dominio explícitos, su radio coincide con el original y converge absoluta y uniformemente en cada cerrado interior. El anclaje $S_{N+1}^{a,c}(c)=a_0$ permite aplicar el teorema cerrado de §23.5 y obtener la derivación término a término, sin circularidad con la primitiva construida en §24.6. El siguiente paso será la unicidad de los coeficientes y las derivadas sucesivas, preparando la teoría de las series de Taylor y la distinción entre suavidad y analiticidad. No se abre un nuevo checkpoint Lean.

---
