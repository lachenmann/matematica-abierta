## 21.1. Particiones y refinamientos {#sec-ta-21-1}

Fijemos $a,b\in\mathbb R$ con $a<b$ y escribamos $I:=[a,b]$. Los índices serán naturales; los extremos y las anchuras serán reales. La distinción impide tratar un número natural como si fuese literalmente un elemento de $\mathbb R$.

### Definición 21.1.1 — Partición estricta de un intervalo cerrado
Una partición de $I$ es el par ordenado $P:=\langle n,p\rangle$ formado por un natural $n\ge1_{\mathbb N}$ y una función dada

$$
J_n:=\{k\in\mathbb N:k\le n\},\qquad p:J_n\longrightarrow I,
$$

que satisface

$$
\boxed{p(0)=a,\quad p(n)=b,\quad
   (\forall k\in\mathbb N)(k<n\Longrightarrow p(k)<p(S(k))).}
\tag{21.1.1}
$$

Escribimos $x_k:=p(k)$ cuando $k\in J_n$; entonces $P$ se representa, sin cambiar su identidad como par, por

$$
a=x_0<x_1<\cdots<x_n=b.
$$

Llamaremos conjunto de nodos al subconjunto bien determinado de $I$

$$
V(P):=\{t\in I:(\exists k\in J_n)\ t=p(k)\}.
\tag{21.1.2}
$$

Para cada $k<n$ definimos el subintervalo $I_k(P):=[x_k,x_{S(k)}]$ y su anchura $\Delta_k(P):=x_{S(k)}-x_k$. Todos son objetos reales o conjuntos reales: el subíndice natural no se convierte en real. El par $P$ retiene el orden y el número de subintervalos; no se identifica por definición con $V(P)$. Reservamos $\operatorname{Part}[a,b]$ para la colección de estos pares y demostraremos ahora que es un conjunto no vacío.

### Proposición 21.1.2 — Existencia, anchuras positivas y suma de longitudes
La colección $\operatorname{Part}[a,b]$ es un conjunto no vacío. Para toda partición $P=\langle n,p\rangle$ se cumplen:

$$
\boxed{\Delta_k(P)>0\ (k<n),\qquad
 \sum_{k=0}^{n-1}\Delta_k(P)=b-a.}
\tag{21.1.3}
$$

Además, $I=\bigcup_{k<n}I_k(P)$; cada subintervalo es no degenerado y dos subintervalos no consecutivos carecen de puntos interiores comunes. La unión indicada es finita y se interpreta mediante la familia dada, no mediante una elección de intervalos.

**Demostración.**
**Existencia del conjunto.** Por Definición §0.6.1 — Función como dominio, codominio y grafo, una función $p:J_n\to I$ conserva los datos de dominio, codominio y grafo. Como $J_n\subseteq\mathbb N$ y $G_p\subseteq\mathbb N\times I$, sus tres componentes están en el conjunto ambiente

$$
U_I:=\mathcal P(\mathbb N)\times\{I\}\times\mathcal P(\mathbb N\times I),
$$

entendiendo la triple codificación según Convención §0.3.5 — Tuplas finitas. Este conjunto existe por producto cartesiano y conjunto potencia. Por consiguiente, todos los pares candidatos $\langle n,p\rangle$ pertenecen a $\mathbb N\times U_I$. Separar de este último exactamente los pares que satisfacen (21.1.1), con el codominio fijo $I$, produce $\operatorname{Part}[a,b]$ como conjunto. La fórmula no requiere decidir algorítmicamente las desigualdades reales.

Para probar habitabilidad, tomemos $n=1_{\mathbb N}$, $J_n=\{0,1_{\mathbb N}\}$ y la función tipada $p:J_n\to I$ dada por $p(0)=a$, $p(1_{\mathbb N})=b$. Su grafo consta de los dos pares indicados y existe por la teoría de funciones; como $a<b$, satisface todas las condiciones. Esta es la partición trivial $P_0=\langle1_{\mathbb N},p\rangle$.

**Anchuras y suma.** La condición de crecimiento estricto da $x_{S(k)}-x_k>0$ para cada $k<n$. Probamos por inducción en la longitud $r\ge1_{\mathbb N}$ la identidad para cualquier lista real estrictamente creciente $z_0<\cdots<z_r$. Para $r=1_{\mathbb N}$ hay un único término $z_1-z_0$. Suponiendo la identidad para una lista de $r+1$ nodos, al añadir cualquier último nodo $z_{S(r)}>z_r$ se obtiene

$$
\sum_{k=0}^{r}(z_{S(k)}-z_k)
=(z_r-z_0)+(z_{S(r)}-z_r)=z_{S(r)}-z_0.
$$

La inducción natural (Teorema §1.1.10 — Principio de inducción) establece así la identidad para toda lista finita estrictamente creciente de longitud positiva. Aplicarla a los nodos de $P$ da (21.1.3), con $z_0=a$ y $z_n=b$. Se usa la suma finita ya definida (Notación §14.1.2 — Suma finita de términos consecutivos), nunca una suma infinita.

**Cobertura.** Cada $I_k(P)\subseteq[a,b]$ porque los nodos están ordenados entre los extremos. Recíprocamente, dado $t\in[a,b]$, si $t=b$ pertenece a $I_{n-1}(P)$, cuyo índice predecesor existe porque $n\ge1$. Si $t<b$, el conjunto finito no vacío $\{j\in J_n:t<x_j\}$ contiene $n$ y no contiene $0$ salvo que $t<a$, caso excluido. Su mínimo $j$ existe por el buen orden de $\mathbb N$ (Teorema §1.6.13 — Principio de buen orden). Tenemos $j=S(k)$ para un único $k<n$. La minimalidad impide $t<x_k$ y la definición del conjunto da $t<x_j$, luego $x_k\le t<x_j$ y $t\in I_k(P)$. Por último, si $k+1<\ell$, entonces $x_{k+1}\le x_\ell$; los interiores de $[x_k,x_{k+1}]$ y $[x_\ell,x_{\ell+1}]$ son disjuntos. Incluso los consecutivos comparten sólo el nodo común, no un punto interior. $\square$

**Lectura.** La positividad de las anchuras no es una hipótesis adicional: resulta del crecimiento estricto. La suma de anchuras recupera $b-a$ porque los puntos intermedios aparecen una vez con signo positivo y otra con signo negativo. Todavía no hay función integranda ni sumas superiores o inferiores.

### Definición 21.1.3 — Refinamiento
Sean $P,Q\in\operatorname{Part}[a,b]$. Diremos que $Q$ refina a $P$ y escribiremos

$$
\boxed{P\preccurlyeq Q\quad\Longleftrightarrow\quad V(P)\subseteq V(Q).}
\tag{21.1.4}
$$

Se trata de conservar todos los puntos de corte de $P$, admitiendo otros nuevos. Esta orientación de $\preccurlyeq$ será fija: el miembro de la derecha es el más fino. Un refinamiento es propio si la inclusión de nodos es propia. Por definición, $P\preccurlyeq P$ y, si $P\preccurlyeq Q\preccurlyeq R$, entonces $P\preccurlyeq R$; estas dos afirmaciones son reflexividad y transitividad de la inclusión ya demostradas en §0.2. No se presupone una regla que produzca un refinamiento: la probaremos construyendo una inserción.

### Lema 21.1.4 — Inserción de un único punto interior
Sean $P=\langle n,p\rangle\in\operatorname{Part}[a,b]$ y $t\in(a,b)$ con $t\notin V(P)$. Existe una partición $Q$ tal que

$$
\boxed{V(Q)=V(P)\cup\{t\}.}
\tag{21.1.5}
$$

En particular, $P\preccurlyeq Q$ es propio y $Q$ tiene exactamente $n+1_{\mathbb N}$ subintervalos. El punto nuevo se introduce una sola vez, en su lugar de orden.

**Demostración.**
Como $t<b=x_n$, el conjunto de índices $E:=\{j\in J_n:t<x_j\}$ es no vacío. El buen orden natural (Teorema §1.6.13 — Principio de buen orden) le da un mínimo $j$. No puede ser $0$, pues $x_0=a<t$, y por ello existe un único $r\in\mathbb N$ con $j=S(r)$ (Teorema §1.2.7 — Predecesor de todo natural no nulo). Por minimalidad, $t\not<x_r$; como $t\ne x_r$ por hipótesis y el orden real es total, $x_r<t$. Tenemos así

$$
x_r<t<x_j,\qquad j=S(r),\quad 1\le j\le n.
\tag{21.1.6}
$$

Formemos $m:=S(n)$ y la función $q:J_m\to I$ por su grafo explícito:

$$
q(k):=\begin{cases}
 x_k,&k<j,\\
 t,&k=j,\\
 x_s,&j<k\le m\text{ y }k=S(s).
\end{cases}
\tag{21.1.7}
$$

En el último caso $k>j\ge1$, por lo que el predecesor $s$ existe y es único; además $s\le n$, de modo que $x_s$ está definido. Las tres ramas son disjuntas y cubren $J_m$. Cada valor pertenece a $I$, así que la función tipada existe mediante Separación en el producto finito apropiado, sin seleccionar representantes ni índices adicionales.

Las comparaciones consecutivas de $q$ coinciden con las de $p$ salvo en las dos nuevas junturas: $q(r)=x_r<t=q(j)$ y $q(j)=t<x_j=q(S(j))$, donde $S(j)\le S(n)=m$. Los extremos siguen siendo $q(0)=a$ y $q(m)=x_n=b$. En consecuencia $Q:=\langle m,q\rangle$ es una partición. La inspección de (21.1.7) muestra que sus nodos son exactamente los antiguos junto con $t$ y que este último no estaba antes. No hay elección: $j$ es el único mínimo de un subconjunto natural especificado. $\square$

**Interpretación.** Insertar un punto divide un subintervalo $[x_r,x_j]$ en dos, sin alterar ninguno de los demás. Sus anchuras satisfacen la identidad aritmética

$$
(t-x_r)+(x_j-t)=x_j-x_r,
$$

cuya legitimidad no depende de integrales ni de áreas geométricas.

### Teorema 21.1.5 — Existencia de un refinamiento común
Para cualesquiera $P,Q\in\operatorname{Part}[a,b]$ existe $R\in\operatorname{Part}[a,b]$ tal que

$$
\boxed{V(R)=V(P)\cup V(Q),\qquad P\preccurlyeq R,\quad Q\preccurlyeq R.}
\tag{21.1.8}
$$

Además, si $S$ es otra partición que refina a la vez a $P$ y a $Q$, entonces $R\preccurlyeq S$. Así, el refinamiento común es el mínimo respecto de la inclusión de nodos; no se ha afirmado que exista antes de construirlo.

**Demostración.**
Escribamos $Q=\langle m,q\rangle$ y $y_i:=q(i)$ para $i\in J_m$. Probaremos por inducción finita en $i\le m$ que existe una partición $R_i$ con

$$
V(R_i)=V(P)\cup\{y_j:j\le i\}.
\tag{21.1.9}
$$

Para $i=0$, $y_0=a\in V(P)$; basta tomar $R_0=P$. Supongamos obtenida una partición $R_i$ para un índice $i<m$. El siguiente nodo $y_{S(i)}$ está en $[a,b]$. Si ya pertenece a $V(R_i)$, conservamos $R_{S(i)}:=R_i$. Si no pertenece, no puede ser $a$ ni $b$, pues ambos son nodos de toda partición; por tanto está en $(a,b)$ y aplicamos Lema §21.1.4 — Inserción de un único punto interior una sola vez para insertarlo. En ambos casos existe una partición que satisface (21.1.9) para $S(i)$. La inducción Teorema §1.1.10 — Principio de inducción, restringida a los $m+1$ índices correspondientes, da una partición $R:=R_m$ con

$$
V(R)=V(P)\cup\{y_j:j\le m\}=V(P)\cup V(Q).
$$

El procedimiento no escoge simultáneamente una partición para cada miembro de una familia infinita: $Q$ es fija, $m$ es finito y cada nuevo conjunto de nodos queda determinado por la igualdad. Las dos relaciones de refinamiento se deducen de las inclusiones de conjuntos. Si $P\preccurlyeq S$ y $Q\preccurlyeq S$, entonces $V(P)\cup V(Q)\subseteq V(S)$ por las reglas de inclusión, y (21.1.4) implica $R\preccurlyeq S$. $\square$

**Cierre de la unidad.** Para comparar sumas construidas sobre particiones distintas ya existe un modo demostrado de llevarlas a una misma partición sin introducir ningún punto de corte ajeno a las dos listas. En §21.2 definiremos primero las cotas de una función acotada sobre cada subintervalo y, sólo después, las sumas inferiores y superiores. Todavía no declaramos que una función sea integrable ni identificamos una suma etiquetada con su integral.
