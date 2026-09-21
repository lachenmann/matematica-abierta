## 21.2. Cotas locales, oscilación y sumas de Darboux {#sec-ta-21-2}

Una partición establece dónde dividimos el intervalo, pero no dice todavía qué altura asociar a cada parte. Para que las aproximaciones sean números reales finitos, comenzaremos con funciones **acotadas**. Sobre cada subintervalo habrá un ínfimo y un supremo de los valores efectivos de la función, aunque ésta no sea continua y ninguno de los dos extremos de valores tenga que alcanzarse. Las sumas inferiores y superiores utilizarán esas cotas, no puntos escogidos arbitrariamente.

### Definición 21.2.1 — Función acotada en el intervalo
Fijados $a<b$ e $I=[a,b]$, una función $f:I\to\mathbb R$ se llama **acotada** si existen números reales $A,B$ tales que

$$
\boxed{A\le f(t)\le B\qquad(t\in I).}
\tag{21.2.1}
$$

Las cotas pertenecen a $\mathbb R$ y pueden depender de $f$; no se les asigna una elección canónica. La condición equivale a que el conjunto no vacío $f[I]$ esté acotado por ambos lados. No exigimos continuidad ni que $f$ alcance $A$ o $B$.

### Lema 21.2.2 — Existencia de las cotas extremas locales y comparación por inclusión
Sea $f:I\to\mathbb R$ acotada y sean $J,K\subseteq I$ conjuntos no vacíos. Existen en $\mathbb R$ los números $\inf f[J],\sup f[J],\inf f[K]$ y $\sup f[K]$. Si $J\subseteq K$, entonces

$$
\boxed{A\le\inf f[K]\le\inf f[J]\le\sup f[J]\le\sup f[K]\le B,}
\tag{21.2.2}
$$

para **cualesquiera** cotas globales $A,B$ que satisfagan (21.2.1). En particular, para cada partición $P$ y cada $k<n$, el conjunto $f[I_k(P)]$ posee ínfimo y supremo reales.

**Demostración.**
Como $J\ne\varnothing$, hay un $t\in J$ y $f(t)\in f[J]$; la imagen existe por la definición de función e imagen. Por (21.2.1), $f[J]\subseteq[A,B]$, así que es no vacía y acotada superior e inferiormente. La propiedad del supremo de $\mathbb R$ (Teorema §12.8.1 — Existencia y caracterización única de la completación ordenada de $\mathbb Q$ y Definición §4.6.1 — Propiedad del supremo y cuerpo ordenado completo) da $\sup f[J]$; la propiedad del ínfimo ya deducida de ella (Proposición §4.6.2 — La propiedad del supremo implica la propiedad del ínfimo) da $\inf f[J]$. Lo mismo vale para $K$. Todo elemento de $f[J]$ queda entre su ínfimo y supremo, de donde $\inf f[J]\le\sup f[J]$ usando el testigo $f(t)$; las cotas globales implican $A\le\inf f[J]$ y $\sup f[J]\le B$, y análogamente para $K$.

Si $J\subseteq K$, entonces $f[J]\subseteq f[K]$. Toda cota inferior de $f[K]$ es también cota inferior de $f[J]$; por la propiedad de *mayor cota inferior*, $\inf f[K]\le\inf f[J]$. La inclusión de las cotas superiores da simétricamente $\sup f[J]\le\sup f[K]$. Combinamos estas desigualdades para obtener (21.2.2). Por §21.1, $I_k(P)$ contiene $x_k$ y está incluido en $I$, luego se aplica el caso $J=I_k(P)$. No se elige una cota o un extremo para cada subintervalo: cada ínfimo y supremo está determinado unívocamente por el conjunto de valores. $\square$

### Definición 21.2.3 — Ínfimo, supremo y oscilación de un conjunto de valores
Para una función acotada $f:I\to\mathbb R$ y un conjunto no vacío $J\subseteq I$, definimos

$$
 m(f,J):=\inf f[J],\qquad M(f,J):=\sup f[J],\qquad
 \omega(f,J):=M(f,J)-m(f,J).
 \tag{21.2.3}
$$

La **oscilación** $\omega(f,J)$ es un real no negativo. Para una partición $P=\langle n,p\rangle$ abreviamos, sólo si $k<n$,

$$
 m_k(P):=m(f,I_k(P)),\quad M_k(P):=M(f,I_k(P)),\quad
 \omega_k(P):=\omega(f,I_k(P)).
 \tag{21.2.4}
$$

Cuando $f$ está fija, también omitiremos $f$ de las abreviaturas. En general, $m(f,J)$ y $M(f,J)$ **no son** valores $f(t)$ para algún $t\in J$. Son extremos del conjunto de valores, cuya existencia está justificada por el lema anterior.

### Definición 21.2.4 — Sumas inferior y superior de Darboux
Sea $f:[a,b]\to\mathbb R$ acotada y $P=\langle n,p\rangle\in\operatorname{Part}[a,b]$. Definimos la **suma inferior** y la **suma superior** de $f$ respecto de $P$ por

$$
\boxed{L(f,P):=\sum_{k=0}^{n-1}m_k(P)\Delta_k(P),\qquad
U(f,P):=\sum_{k=0}^{n-1}M_k(P)\Delta_k(P).}
\tag{21.2.5}
$$

Estas son sumas de **exactamente $n$ términos reales**: $n\ge1$, los factores $m_k,M_k,\Delta_k$ existen para todo $k<n$ y la suma finita fue construida en el capítulo 14. El uso de $\inf$ y $\sup$ no es una prescripción algorítmica para calcularlos. Aún no se ha definido integral alguna.

### Proposición 21.2.5 — Encierro global e identidad de la brecha
Para toda $f:[a,b]\to\mathbb R$ acotada, toda partición $P$ y cualesquiera cotas $A,B$ de (21.2.1),

$$
\boxed{A(b-a)\le L(f,P)\le U(f,P)\le B(b-a).}
\tag{21.2.6}
$$

Además,

$$
\boxed{U(f,P)-L(f,P)=\sum_{k=0}^{n-1}\omega_k(P)\Delta_k(P)\ge0.}
\tag{21.2.7}
$$

La brecha es nula si y sólo si $\omega_k(P)=0$ para **todo** $k<n$.

**Demostración.**
Por (21.2.2), $A\le m_k(P)\le M_k(P)\le B$. Cada anchura $\Delta_k(P)>0$ por Proposición §21.1.2 — Existencia, anchuras positivas y suma de longitudes. La compatibilidad del orden real con la multiplicación por un número positivo proporciona

$$
 A\Delta_k(P)\le m_k(P)\Delta_k(P)\le M_k(P)\Delta_k(P)\le B\Delta_k(P).
$$

Sumar término a término preserva las desigualdades por la comparación de sumas finitas (Proposición §14.5.1 — Comparación de sumas finitas y de bloques); la distributividad finita y la identidad de longitudes Proposición §21.1.2 — Existencia, anchuras positivas y suma de longitudes dan, por ejemplo, $\sum_{k<n}A\Delta_k=A(b-a)$, y de igual manera para $B$. Esto demuestra (21.2.6). Restar las dos sumas mediante la aritmética finita y distribuir cada anchura produce

$$
 U(f,P)-L(f,P)
 =\sum_{k<n}(M_k(P)-m_k(P))\Delta_k(P)
 =\sum_{k<n}\omega_k(P)\Delta_k(P).
$$

Todos los sumandos son no negativos. Si cada oscilación es nula, la suma lo es. Recíprocamente, si la suma es cero, para un índice fijo $j<n$ tenemos $0\le\omega_j(P)\Delta_j(P)\le\sum_{k<n}\omega_k(P)\Delta_k(P)=0$, por comparación finita con los otros términos no negativos. Puesto que $\Delta_j(P)>0$, se concluye $\omega_j(P)=0$; $j$ era arbitrario. No se ha supuesto que $f$ sea continua ni se han escogido extremos de su imagen. $\square$

### Lema 21.2.6 — Una inserción mejora ambas sumas
Sea $f:[a,b]\to\mathbb R$ una función acotada, sea $P\in\operatorname{Part}[a,b]$ y sea $t\in(a,b)\setminus V(P)$. Sea $Q$ la partición obtenida insertando $t$ como en Lema §21.1.4 — Inserción de un único punto interior. Entonces

$$
\boxed{L(f,P)\le L(f,Q),\qquad U(f,Q)\le U(f,P).}
\tag{21.2.8}
$$

**Demostración.**
El lema de inserción sitúa $t$ en un único intervalo original $J=[x_r,x_{r+1}]$, con $x_r<t<x_{r+1}$. Sean $J_-=[x_r,t]$ y $J_+=[t,x_{r+1}]$, y escribamos $d_-=t-x_r>0$, $d_+=x_{r+1}-t>0$. Por inclusión $J_-,J_+\subseteq J$ y Lema §21.2.2 — Existencia de las cotas extremas locales y comparación por inclusión,

$$
 m(f,J)\le m(f,J_-),m(f,J_+),\qquad
 M(f,J_-),M(f,J_+)\le M(f,J).
$$

Multiplicando por las anchuras positivas y sumando obtenemos

$$
 m(f,J)(d_-+d_+)\le m(f,J_-)d_-+m(f,J_+)d_+,
$$
$$
 M(f,J_-)d_-+M(f,J_+)d_+\le M(f,J)(d_-+d_+).
$$

Como $d_-+d_+=x_{r+1}-x_r=\Delta_r(P)$, éstas comparan el sumando antiguo con los **dos** sumandos que lo sustituyen. Todos los demás subintervalos y sus cotas son idénticos, aunque sus índices posteriores se desplacen una posición. La identidad de sumas por bloques Proposición §14.2.2 — Identidades de los bloques de sumación agrupa el prefijo, el bloque sustituido y el sufijo; si el prefijo o el sufijo carece de términos, simplemente se omite ese bloque. Los términos restantes son idénticos y se cancelan exactamente. Quedan ambas desigualdades de (21.2.8). La inserción usa el único índice mínimo construido en §21.1, no una elección. $\square$

### Lema 21.2.7 — Una lista estricta queda determinada por sus nodos
Si $P,Q\in\operatorname{Part}[a,b]$ y $V(P)=V(Q)$, entonces $P=Q$ como pares de un natural y una función tipada. Por tanto, $P\preccurlyeq Q$ y $Q\preccurlyeq P$ implican $P=Q$.

**Demostración.**
Escribamos $P=(x_0<\cdots<x_n)$ y $Q=(y_0<\cdots<y_m)$, abreviando las funciones del par original. Sus primeros nodos son $a$, y ambos conjuntos de nodos coinciden. Supongamos que los primeros $j$ nodos coinciden, con $j<n$ y $j<m$. El nodo $x_{j+1}$ es el **menor elemento** de $V(P)\setminus\{x_0,\dots,x_j\}$: todos los nodos posteriores son estrictamente mayores y no hay nodos de $P$ entre dos consecutivos. Idénticamente, $y_{j+1}$ es el menor elemento del mismo conjunto, pues $V(Q)=V(P)$ y el prefijo es común. La unicidad del mínimo en un orden total da $x_{j+1}=y_{j+1}$. Por inducción, ambas enumeraciones coinciden hasta el menor de $n,m$. Si $n<m$, en ese índice $x_n=b$, mientras que la estricta lista $Q$ aún tiene $y_{n+1}>y_n=b$, contradicción con $y_{n+1}\in[a,b]$. El caso $m<n$ es simétrico. Luego $n=m$, todos los valores de los grafos son iguales y los dominios y codominios también; la igualdad de funciones Proposición §0.6.3 — Criterio de igualdad de funciones proporciona $P=Q$. La segunda afirmación es doble inclusión de los conjuntos de nodos seguida del resultado recién demostrado. $\square$

### Teorema 21.2.8 — Monotonía de las sumas bajo refinamiento
Para toda función acotada $f:[a,b]\to\mathbb R$ y todas las particiones $P,Q$, si $P\preccurlyeq Q$, entonces

$$
\boxed{L(f,P)\le L(f,Q)\le U(f,Q)\le U(f,P).}
\tag{21.2.9}
$$

**Demostración.**
Escribamos $Q=(y_0<\cdots<y_m)$. Partimos de $P$ e incorporamos sucesivamente $y_0,\ldots,y_m$: si el nodo ya está, conservamos la partición actual; si falta, insertamos ese **único** nodo mediante Lema §21.1.4 — Inserción de un único punto interior. Es la misma inducción finita empleada para construir el refinamiento común Teorema §21.1.5 — Existencia de un refinamiento común. Como $V(P)\subseteq V(Q)$, la partición final $R$ satisface $V(R)=V(P)\cup V(Q)=V(Q)$. Por Lema §21.2.7 — Una lista estricta queda determinada por sus nodos, $R=Q$.

En cada paso sin inserción las sumas permanecen idénticas. En cada paso con inserción, Lema §21.2.6 — Una inserción mejora ambas sumas muestra que la suma inferior no disminuye y la superior no aumenta. La transitividad de $\le$ aplicada al número finito de pasos da $L(f,P)\le L(f,R)$ y $U(f,R)\le U(f,P)$; sustituyendo $R=Q$ y usando $L(f,Q)\le U(f,Q)$ de Proposición §21.2.5 — Encierro global e identidad de la brecha, obtenemos (21.2.9). No se forma una sucesión infinita de particiones ni se aplica ningún principio de elección: los $m+1$ pasos están fijados por la lista ya dada. $\square$

### Corolario 21.2.9 — Toda suma inferior queda por debajo de toda suma superior
Para **cualesquiera** particiones $P,Q\in\operatorname{Part}[a,b]$ de una función acotada fija,

$$
\boxed{L(f,P)\le U(f,Q).}
\tag{21.2.10}
$$

**Demostración.**
El teorema Teorema §21.1.5 — Existencia de un refinamiento común proporciona **una** partición $R$ que refina simultáneamente a $P$ y a $Q$. Aplicando Teorema §21.2.8 — Monotonía de las sumas bajo refinamiento en cada una de las dos comparaciones,

$$
 L(f,P)\le L(f,R)\le U(f,R)\le U(f,Q).
$$

La transitividad del orden real da (21.2.10). El punto importante es que no comparamos directamente sumandos cuyos intervalos sean diferentes: primero pasamos a una partición común cuya existencia ya fue probada. $\square$

**Ejemplo de control.** Si $f(t)=c$ para todo $t\in[a,b]$, su imagen sobre cada subintervalo es el singleton $\{c\}$. En consecuencia, $m_k(P)=M_k(P)=c$ y ambas sumas valen $c\sum_{k<n}\Delta_k(P)=c(b-a)$. Para una función no constante, en cambio, la igualdad entre las dos sumas no se presume: su brecha está determinada por (21.2.7).

**Transición.** La comparación universal (21.2.10) es la pieza indispensable para el siguiente paso. En §21.3 consideraremos los conjuntos de **todas** las sumas inferiores y superiores; sólo tras probar que son no vacíos y acotados introduciremos su supremo e ínfimo como integral inferior e integral superior. La integrabilidad exigirá después demostrar la igualdad de esos dos reales; no se anticipa aquí.
