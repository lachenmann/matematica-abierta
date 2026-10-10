## 20.8. Fórmula de Taylor de orden finito y restos {#sec-ta-20-8}

La aproximación lineal del Capítulo 19 describe el primer incremento de una función. Si disponemos de información diferencial de orden superior, podemos buscar un polinomio que reproduzca sucesivamente esos datos en un centro dado. No basta escribir una suma formal: tendremos que construir sus coeficientes, demostrar las reglas que permiten derivarla y justificar qué queda fuera del polinomio.

El desarrollo será deliberadamente finito. Los índices pertenecen a $\mathbb N$; la suma de un número finito de términos ya existe por §14.1 y las potencias naturales reales por §14.3. Lo nuevo será el factorial, junto con una familia *dada* de derivadas sucesivas sobre un intervalo cerrado. No aparecerá una suma infinita, una integral ni un axioma de elección.

### Definición 20.8.1 — Factorial natural
El teorema de recursión sobre $\mathbb N$ (Teorema §1.3.7 — Teorema de recursión sobre $\mathbb N$) determina una única función $\operatorname{fac}:\mathbb N\to\mathbb N$ mediante

$$
\operatorname{fac}(0_{\mathbb N})=1_{\mathbb N},\qquad
\operatorname{fac}(S(k))=S(k)\cdot\operatorname{fac}(k).
\tag{20.8.1}
$$

El producto de la segunda igualdad es el producto natural, y el factor $S(k)$ está bien definido para cada índice. La existencia procede de recursión, no de una selección de productos para cada $k$.

### Notación 20.8.2 — Factorial y su copia real
Para $k\in\mathbb N$ escribiremos $k!:=\operatorname{fac}(k)\in\mathbb N$. Cuando el factorial figure como factor o denominador en una expresión real, escribiremos explícitamente

$$
\eta_k:=\nu_{\mathbb R}(k!)\in\mathbb R.
\tag{20.8.2}
$$

La letra $\eta_k$ es una abreviatura local de esta sección; en particular, $k!$ y $\eta_k$ no son literalmente el mismo objeto. En adelante todos los cocientes de coeficientes se formarán con $\eta_k$, no con un natural usado como denominador real por coerción silenciosa.

### Proposición 20.8.3 — Positividad y recurrencia de los factoriales
Para todo $k\in\mathbb N$ se tiene $k!>0_{\mathbb N}$ y, en consecuencia, $\eta_k>0$; además,

$$
\eta_0=1,\qquad \eta_{S(k)}=\nu_{\mathbb R}(S(k))\,\eta_k.
\tag{20.8.3}
$$

En particular, todos los denominadores $\eta_k$ que utilizaremos son no nulos, incluido $\eta_0=1$.

**Demostración.**
Procedemos por inducción. En $k=0$, la definición da $0!=1_{\mathbb N}>0_{\mathbb N}$. Si $k!>0_{\mathbb N}$, el sucesor $S(k)$ es un natural positivo y el producto de dos naturales positivos es positivo por las reglas aritméticas y de orden cerradas. Así, $(S(k))!=S(k)\,k!>0_{\mathbb N}$. La inducción Teorema §1.1.10 — Principio de inducción concluye la primera afirmación para todos los índices. Por Proposición §4.1.6 — Aritmética y orden de los numerales naturales, la incrustación de numerales reales preserva el orden positivo, la unidad y la multiplicación; aplicar $\nu_{\mathbb R}$ a (20.8.1) obtiene precisamente (20.8.3). No identificamos $\mathbb N$ y $\mathbb R$. $\square$

### Definición 20.8.4 — Cadena diferencial finita sobre un intervalo cerrado
Fijemos $A<B$, $I:=[A,B]$ y $n\in\mathbb N$. Una cadena diferencial finita de orden $n$ sobre $I$ es una familia *dada* $\mathbf f:J_n\to\mathbb R^I$, donde $J_n:=\{k\in\mathbb N:k\le n\}$, cuyas funciones $f_k:=\mathbf f(k):I\to\mathbb R$ cumplen:

1. Cada $f_k$ es continua en todo $I$, para $0\le k\le n$.
2. Para $0\le k<n$ y cada $t\in(A,B)$, $f_k$ es derivable en $t$, relativamente a $I$, y $f_k'(t)=f_{k+1}(t)$.

La función que se quiere aproximar será $f:=f_0$. La familia es un dato de las hipótesis y no se obtiene eligiendo derivadas: en el interior cada valor $f_{k+1}(t)$ coincide con la única derivada indicada. En los extremos, $f_k(A)$ y $f_k(B)$ son valores de las extensiones continuas *suministradas*, sin pretender que exista de antemano un operador de derivación sobre todos los extremos. Para $n=0$ sólo se exige continuidad de $f_0$.

### Definición 20.8.5 — Polinomio de Taylor finito en un centro
Para una cadena de orden $n$ y un centro $a\in I$, fijemos la sucesión real de coeficientes determinada por

$$
c_k:=\begin{cases}f_k(a)/\eta_k,&k\le n,\\0,&k>n.\end{cases}
$$

Cada cociente existe por la proposición anterior. La secuencia $k\mapsto c_k$ es una función total $\mathbb N\to\mathbb R$ por Separación, con una fórmula unívoca. El polinomio de Taylor de orden $n$, centrado en $a$, es la función $P_{n,a}:\mathbb R\to\mathbb R$ definida por la suma finita

$$
\boxed{P_{n,a}(t):=\sum_{k=0}^{n}\frac{f_k(a)}{\eta_k}(t-a)^k.}
\tag{20.8.4}
$$

La función existe por la construcción de polinomios Definición §17.5.1 — Función polinomial real determinada por una lista finita de coeficientes, aplicada a los coeficientes finitos y a la traslación $t\mapsto t-a$. La escritura $\sum_{k=0}^n$ conserva exactamente la suma inicial no vacía de Notación §14.1.2 — Suma finita de términos consecutivos. En $t=a$ se utiliza $0^0=1$ de Definición §14.3.1 — Potencias naturales de un número real, de modo que $P_{n,a}(a)=f_0(a)$. «Orden $n$» no significa que el coeficiente de grado $n$ sea necesariamente distinto de cero.

### Lema 20.8.6 — Derivación de las piezas polinómicas finitas
Fijados $n$, una cadena $f_0,\ldots,f_n$ y $a\in I$, para cada $k\le n$ sea $m\in\mathbb N$ el único natural con $n=k+m$, y definamos la función polinómica

$$
Q_k(t):=\sum_{r=0}^{m}\frac{f_{k+r}(a)}{\eta_r}(t-a)^r,
\qquad t\in\mathbb R.
\tag{20.8.5}
$$

Asimismo, para $k\le n+1$ y el único $p\in\mathbb N$ con $n+1=k+p$, pongamos

$$
B_k(t):=\frac{\eta_{n+1}}{\eta_p}(t-a)^p.
\tag{20.8.6}
$$

Estas funciones satisfacen

$$
\begin{gathered}
Q_0=P_{n,a},\quad Q_k(a)=f_k(a)\ (k\le n),\quad
Q_k'=Q_{k+1}\ (k<n),\\
B_k(a)=0\ (k\le n),\quad B_k'=B_{k+1}\ (k\le n),\quad
B_{n+1}(t)=\eta_{n+1}.
\end{gathered}
\tag{20.8.7}
$$

Las igualdades de derivadas se entienden primero para las funciones polinómicas sobre $\mathbb R$ y, por restricción, para cualquier punto interior de $I$. Los polinomios $Q_k,B_k$ son continuos en la recta.

**Demostración.**
Primero, para cada exponente natural positivo $j=S(r)$, la potencia $(t-a)^j$ es derivable y

$$
\frac{d}{dt}(t-a)^j=\nu_{\mathbb R}(j)(t-a)^r.
\tag{20.8.8}
$$

Para $j=1$, esto es la derivada $1$ de la función afín $t-a$ (Proposición §19.1.6 — Primeros cálculos: funciones afines y función cuadrática). Si vale para $j$, la identidad $(t-a)^{j+1}=(t-a)^j(t-a)$ y la regla del producto Teorema §19.4.3 — Regla de derivación del producto dan
$\nu_{\mathbb R}(j)(t-a)^j+(t-a)^j=\nu_{\mathbb R}(j+1)(t-a)^j$, por la aritmética de los numerales. Inducción ordinaria prueba (20.8.8). La potencia de exponente $0$ es la función constante $1$ y su derivada es cero.

Para obtener $Q_k'$, derivamos la suma finita (20.8.5) por inducción sobre el número de sumandos, mediante Corolario §19.4.2 — Multiplicación por escalares, opuestos y diferencias. Si $k<n$, entonces $m\ge1$ y el término $r=0$ tiene derivada nula; para $r=S(s)$, (20.8.8) y la recurrencia factorial dan

$$
\frac{f_{k+S(s)}(a)}{\eta_{S(s)}}
\nu_{\mathbb R}(S(s))(t-a)^s
=\frac{f_{k+1+s}(a)}{\eta_s}(t-a)^s.
$$

Reindexar el bloque finito de índices positivos mediante $r=S(s)$ produce $Q_{k+1}(t)$ exactamente, sin sumar un conjunto vacío. El mismo cálculo aplicado a $B_k$, cuyo exponente $p$ es positivo cuando $k\le n$, usa $\eta_p=\nu_{\mathbb R}(p)\eta_{p-1}$ y da $B_k'=B_{k+1}$. Cuando $k=n+1$, $p=0$ y $B_{n+1}=\eta_{n+1}/\eta_0=\eta_{n+1}$. Finalmente, en $t=a$ sólo sobrevive el término $r=0$ de $Q_k$, pues $\eta_0=1$; en $B_k(a)$ la potencia tiene exponente positivo para $k\le n$, así que vale cero. Para $k=0$, (20.8.5) es (20.8.4). La continuidad de todas estas expresiones se sigue de Teorema §17.5.3 — Todo polinomio real es continuo en la recta y de la composición con la traslación afín. La restricción conserva derivadas interiores por Proposición §19.5.2 — Restricción de una función derivable. $\square$

### Teorema 20.8.7 — Taylor finito con resto de Lagrange
Sean $A<B$, $I=[A,B]$, $n\in\mathbb N$ y $\mathbf f=(f_0,\ldots,f_n)$ una cadena diferencial de orden $n$ sobre $I$. Supongamos adicionalmente que $f_n$ es derivable en todos los puntos de $(A,B)$. Fijemos $a\in I$ y un $x\in I$ distinto de $a$. Entonces existe un punto $c$ estrictamente comprendido entre $a$ y $x$ tal que

$$
\boxed{f(x)=P_{n,a}(x)
+\frac{f_n'(c)}{\eta_{n+1}}(x-a)^{n+1}.}
\tag{20.8.9}
$$

La derivada $f_n'(c)$ se toma relativamente al dominio $I$. No se exige continuidad de esta derivada ni que exista en $A$ o $B$. Si $x=a$, se cumple trivialmente $f(a)=P_{n,a}(a)$, pero no se afirma la existencia de un punto entre dos extremos idénticos. Para $n=0$ el teorema es exactamente Lagrange.

**Demostración.**
**1. Preparación sin dividir por cero.** Sea $\eta:=\eta_{n+1}>0$ y pongamos

$$
K:=\frac{f(x)-P_{n,a}(x)}{(x-a)^{n+1}}.
\tag{20.8.10}
$$

El cociente existe porque $x\ne a$, el exponente es positivo y el cuerpo real no tiene divisores de cero. Para $0\le k\le n$ formemos las funciones bien tipadas $H_k:I\to\mathbb R$,

$$
H_k(t):=f_k(t)-Q_k(t)-K B_k(t),\qquad t\in I,
\tag{20.8.11}
$$

entendiendo $Q_k$ y $B_k$ restringidas explícitamente a $I$. Sólo se construyen las $n+1$ funciones de esta familia finita, cuyos valores determinan un grafo por Separación. Por continuidad de $f_k$ en todo $I$, de los polinomios y de las operaciones algebraicas de funciones continuas, cada $H_k$ es continua también en los extremos. El lema anterior da

$$
H_k(a)=0\quad(0\le k\le n),\qquad
H_0(x)=f(x)-P_{n,a}(x)-K(x-a)^{n+1}=0.
\tag{20.8.12}
$$

**2. Cadena exacta de derivadas.** Para $0\le k<n$ y $t\in(A,B)$, las hipótesis de la cadena, las reglas del Capítulo 19 y (20.8.7) proporcionan

$$
H_k'(t)=f_{k+1}(t)-Q_{k+1}(t)-KB_{k+1}(t)=H_{k+1}(t).
\tag{20.8.13}
$$

Para el último miembro, cuya derivada existe por la hipótesis adicional, el mismo cálculo produce

$$
H_n'(t)=f_n'(t)-K\eta.
\tag{20.8.14}
$$

**3. Rolle repetido un número finito de veces.** Sean $u:=\min\{a,x\}$ y $v:=\max\{a,x\}$, de modo que $u<v$ y $[u,v]\subseteq I$. Empezamos con $z_0:=x$. La igualdad $H_0(a)=H_0(z_0)=0$, la continuidad de $H_0$ en el segmento y su derivabilidad interior permiten aplicar Rolle a la restricción $H_0\upharpoonright[u,v]$. Su derivada interior coincide con la de $H_0$ respecto de $I$ por Proposición §19.5.2 — Restricción de una función derivable. Existe, por tanto, $z_1$ estrictamente entre $a$ y $z_0$ con $H_0'(z_1)=0$.

Si $n=0$, la igualdad (20.8.14) ya convierte esto en $f_0'(z_1)=K\eta_1$. Para $n\ge1$, (20.8.13) da $H_1(z_1)=0$. Como $H_1(a)=0$, repetimos Rolle sobre el segmento de extremos $a,z_1$, contenido en $I$: obtenemos $z_2$ estrictamente entre ambos con $H_1'(z_2)=0$ y, si $1<n$, $H_2(z_2)=0$. Formalmente, una inducción finita sobre $k\le n$ mantiene $H_k(a)=H_k(z_k)=0$ y produce $z_{k+1}$ estrictamente entre $a,z_k$ con $H_k'(z_{k+1})=0$; cuando $k<n$ se usa (20.8.13) para continuar. En el último paso $k=n$, (20.8.14) da un punto $c:=z_{n+1}$ estrictamente entre $a$ y $x$ para el que

$$
0=H_n'(c)=f_n'(c)-K\eta_{n+1}.
$$

Cada segmento intermedio tiene extremos distintos y su interior está incluido en $(A,B)$, por lo que Rolle se aplica legítimamente. La inducción produce sólo una cadena de longitud finita fijada por $n$. No se infiere de $\forall k\,\exists z_k$ una función de elección infinita ni se utiliza `CC(R)`.

**4. Recuperación de la igualdad.** La positividad de $\eta_{n+1}$ permite despejar $K=f_n'(c)/\eta_{n+1}$. Sustituirlo en (20.8.10) y multiplicar por $(x-a)^{n+1}$ demuestra (20.8.9). No se invocaron integrales, infinitas derivadas ni una serie de Taylor. $\square$

**Lectura deductiva.** El polinomio no aproxima porque sus coeficientes «parezcan adecuados». La identidad $Q_k'=Q_{k+1}$ hace que los $n$ primeros errores derivados se anulen en el centro. El coeficiente $K$ fuerza otra anulación en el extremo $x$. Rolle, aplicado sólo $n+1$ veces, transforma esos ceros en la igualdad para el resto.

### Corolario 20.8.8 — Cota uniforme para el resto
Bajo las hipótesis de Taylor, supongamos que existe un número real $M\ge0$ con $|f_n'(t)|\le M$ para todo $t\in(A,B)$. Entonces, para todos $a,x\in I$,

$$
\boxed{|f(x)-P_{n,a}(x)|
\le\frac{M}{\eta_{n+1}}|x-a|^{n+1}.}
\tag{20.8.15}
$$

La estimación incluye el caso $M=0$ y los extremos del intervalo; no supone existencia de un máximo de $|f_n'|$ ni deriva la cota de continuidad de $f_n'$.

**Demostración.**
Para $x=a$, ambos lados valen cero, pues $n+1>0$. Para $x\ne a$, fijemos *un* punto $c$ suministrado por (20.8.9). Tomamos valores absolutos y utilizamos $|f_n'(c)|\le M$, $\eta_{n+1}>0$ y $|(x-a)^{n+1}|=|x-a|^{n+1}$ (Lema §14.3.3 — El valor absoluto conmuta con las potencias naturales). Esto da exactamente (20.8.15). No se necesita seleccionar un punto $c$ para todos los pares $a,x$ simultáneamente. Si $M=0$, la desigualdad prueba $f(x)=P_{n,a}(x)$ en todos los puntos. $\square$

### Corolario 20.8.9 — Resto de Peano sin derivada de orden $n+1$
Sea ahora $n\ge1$ y demos únicamente una cadena diferencial de orden $n$ sobre $I=[A,B]$, con sus $f_0,\ldots,f_n$ continuas en todo $I$ y $f_k'=f_{k+1}$ en el interior para $k<n$. No se supone que $f_n'$ exista. Para cada centro $a\in I$,

$$
\boxed{f(x)-P_{n,a}(x)=o\bigl(|x-a|^n\bigr)
\quad\text{cuando }x\to a\text{ dentro de }I.}
\tag{20.8.16}
$$

El símbolo $o$ es una abreviatura local de la proposición cuantificada siguiente, no un objeto nuevo cuya definición se presuponga: para todo $\varepsilon>0$ existe $\delta>0$ tal que, para cada $x\in I$,

$$
0<|x-a|<\delta\quad\Longrightarrow\quad
|f(x)-P_{n,a}(x)|<\varepsilon|x-a|^n.
\tag{20.8.17}
$$

La aproximación vale desde los lados del intervalo que efectivamente acumulan en $a$; si $a=A$ o $a=B$, no se exige un entorno bilateral fuera del dominio.

**Demostración.**
Como $n\ge1$, hay un único $m\in\mathbb N$ con $n=S(m)$; por tanto $m=n-1$ en la abreviatura aritmética usual. La familia truncada $f_0,\ldots,f_m$ cumple las hipótesis de Teorema §20.8.7 — Taylor finito con resto de Lagrange a orden $m$: su último miembro $f_m$ es derivable en $(A,B)$ y su derivada allí es $f_n$. Para $x\ne a$, Taylor de orden $m$ proporciona $c$ estrictamente entre $a$ y $x$ tal que

$$
f(x)=P_{m,a}(x)+\frac{f_n(c)}{\eta_n}(x-a)^n.
\tag{20.8.18}
$$

Por definición, $P_{n,a}(x)=P_{m,a}(x)+[f_n(a)/\eta_n](x-a)^n$, identidad de dos sumas finitas con un término adicional. Restarlas da la igualdad exacta

$$
f(x)-P_{n,a}(x)
=\frac{f_n(c)-f_n(a)}{\eta_n}(x-a)^n.
\tag{20.8.19}
$$

Fijemos $\varepsilon>0$. La continuidad relativa de $f_n$ en $a$ proporciona $\delta>0$ tal que $t\in I$ y $|t-a|<\delta$ implican $|f_n(t)-f_n(a)|<\varepsilon\eta_n$, porque $\eta_n>0$. Si $x\in I$ cumple $0<|x-a|<\delta$, el punto intermedio $c$ de (20.8.18) pertenece a $I$ y satisface $|c-a|<|x-a|<\delta$. Así, (20.8.19) da

$$
|f(x)-P_{n,a}(x)|
<\varepsilon|x-a|^n.
$$

Se trata exactamente de (20.8.17). El argumento es puntual en un par $a,x$ arbitrario: sólo utiliza el testigo existencial de Taylor de orden anterior, no una función que elija todos los $c$. $\square$

**Alcance y frontera.** La fórmula de Lagrange requiere una derivada adicional interior, aunque no su continuidad; el resto de Peano exige en cambio continuidad de la última función de la cadena, pero ninguna derivada de orden $n+1$. Los dos enunciados son finitos y no afirman que una serie infinita converja ni que su valor sea $f(x)$. El ejemplo $f(t)=(t-a)^{n+1}$, con sus derivadas polinómicas dadas por el lema, tiene $P_{n,a}=0$ y resto exactamente $(t-a)^{n+1}$: no cabe borrar el término residual en general.

**Transición al cálculo integral.** Hemos pasado de una condición local sobre cocientes incrementales a resultados globales sobre extremos, incrementos, signos y aproximaciones finitas. El valor medio compara dos valores de una función; Taylor cuantifica el error de reemplazarla por un polinomio. Ninguna de estas afirmaciones requiere identificar una función con su serie infinita.

El siguiente capítulo abordará otro problema: asignar rigurosamente un número a la acumulación de valores de una función sobre un intervalo. Comenzaremos con particiones y refinamientos; después construiremos las sumas inferiores y superiores y definiremos la integral de Darboux–Riemann mediante supremos e ínfimos ya legítimos. Sólo más tarde caracterizaremos esa integral mediante sumas etiquetadas. La definición no presupone el teorema fundamental del cálculo, reservado para el Capítulo 22.
