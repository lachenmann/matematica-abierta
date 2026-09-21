## 21.4. Integrabilidad y criterio de Darboux {#sec-ta-21-4}

Las dos integrales extremas ya existen para cualquier función acotada, pero su desigualdad $\underline{\int_a^b}f\le\overline{\int_a^b}f$ puede ser estricta. La definición de integral propiamente dicha debe distinguir ambos casos. El criterio que demostraremos sustituye la igualdad entre dos extremos de conjuntos posiblemente infinitos por una condición sobre **una partición finita para cada precisión prescrita**. No afirma la existencia de una partición que alcance los extremos ni la posibilidad de escoger de una vez particiones para todas las precisiones.

### Definición 21.4.1 — Integrabilidad de Darboux
Sean $a,b\in\mathbb R$, $a<b$, y $f:[a,b]\to\mathbb R$ una función **acotada**. Diremos que $f$ es *integrable de Darboux* (o, en el presente capítulo, *integrable de Riemann*) en $[a,b]$ si

$$
\boxed{\underline{\int_a^b}f=\overline{\int_a^b}f.}
\tag{21.4.1}
$$

La condición está bien tipada porque ambos miembros son reales ya construidos en Definición §21.3.3 — Integrales inferior y superior de Darboux. Si

$$
D_f:=\overline{\int_a^b}f-\underline{\int_a^b}f,
$$

entonces $D_f\ge0$ por Proposición §21.3.4 — Orden y encierro de las integrales extremas y la integrabilidad equivale a $D_f=0$. Por ahora, la palabra «integrable» se refiere a funciones **acotadas en el intervalo no degenerado**; no se asigna una integral a una función no acotada ni se define el caso $a=b$.

### Teorema 21.4.2 — Criterio de Darboux y persistencia bajo refinamiento
Sea $f:[a,b]\to\mathbb R$ acotada, con $a<b$. Son equivalentes:

1. $f$ es integrable en $[a,b]$.
2. Para todo $\varepsilon>0$ existe una partición $P\in\operatorname{Part}[a,b]$ tal que
   $$
   \boxed{U(f,P)-L(f,P)<\varepsilon.}
   \tag{21.4.2}
   $$
3. Para todo $\varepsilon>0$ existe una partición $P\in\operatorname{Part}[a,b]$ tal que **toda** partición $Q$ con $P\preccurlyeq Q$ satisface
   $$
   U(f,Q)-L(f,Q)<\varepsilon.
   \tag{21.4.3}
   $$

**Demostración.**
**(1 $\Rightarrow$ 2).** Fijemos $\varepsilon>0$. Por integrabilidad, $D_f=0$. La aproximación simultánea Corolario §21.3.5 — Aproximación simultánea mediante una partición, en su fórmula (21.3.6), proporciona una partición $P$ tal que

$$
0=D_f\le U(f,P)-L(f,P)<D_f+\varepsilon=\varepsilon.
$$

La partición obtenida es un testigo para este $\varepsilon$ fijo; la demostración no construye una función que asigne testigos a todas las tolerancias.

**(2 $\Rightarrow$ 1).** Para toda partición $P$, las desigualdades de Proposición §21.3.4 — Orden y encierro de las integrales extremas implican

$$
0\le D_f
=\overline{\int_a^b}f-\underline{\int_a^b}f
\le U(f,P)-L(f,P).
\tag{21.4.4}
$$

Si $D_f>0$, podemos elegir **una tolerancia determinada** $\varepsilon:=D_f/2>0$. La condición (2) produce una partición $P$ con

$$
D_f\le U(f,P)-L(f,P)<D_f/2<D_f,
$$

contradicción. Como $D_f\ge0$ y el orden real es total, necesariamente $D_f=0$, que es precisamente (21.4.1). No hemos utilizado una sucesión de particiones, un límite de sumas ni el axioma de elección.

**(2 $\Rightarrow$ 3).** Dado $\varepsilon>0$, tomemos el testigo $P$ de (2). Si $P\preccurlyeq Q$, la monotonía bajo refinamiento (Teorema §21.2.8 — Monotonía de las sumas bajo refinamiento) proporciona

$$
0\le U(f,Q)-L(f,Q)\le U(f,P)-L(f,P)<\varepsilon.
$$

**(3 $\Rightarrow$ 2).** Basta tomar $Q=P$, pues la relación de refinamiento es reflexiva (Definición §21.1.3 — Refinamiento). Quedan demostradas las tres equivalencias. $\square$

**Lectura de los cuantificadores.** El criterio no dice que toda partición tenga brecha pequeña. Afirma que, para cada precisión, se puede encontrar **una partición suficientemente adecuada**; a partir de ella, ninguna inserción ulterior de nodos empeora la estimación. La condición de acotación de $f$ forma parte de la hipótesis de todo el teorema.

### Definición 21.4.3 — Valor de la integral de Riemann–Darboux
Si $f:[a,b]\to\mathbb R$ es acotada e integrable, sus integrales extremas son, por (21.4.1), **el mismo número real**. Definimos entonces

$$
\boxed{\int_a^b f
:=\underline{\int_a^b}f
=\overline{\int_a^b}f.}
\tag{21.4.5}
$$

La expresión $\int_a^b f$ se introduce aquí, y **únicamente aquí**, para funciones cuya integrabilidad esté establecida; es un número real unívocamente determinado por los dos extremos, que a su vez son únicos por completitud. Cuando la variable de evaluación de $f$ sea $t$, podremos escribir $\int_a^b f(t)\,dt$ como una abreviatura tipada de este mismo valor; el símbolo $dt$ no introduce todavía diferenciales ni una operación nueva. Una función no integrable conserva sus integrales inferior y superior, pero **no** recibe el valor (21.4.5).

### Proposición 21.4.4 — Encierro y error controlado por la brecha
Sea $f:[a,b]\to\mathbb R$ integrable y escribamos $I_f:=\int_a^b f$. Para cada partición $P$ se cumplen

$$
\boxed{L(f,P)\le I_f\le U(f,P),}
\tag{21.4.6}
$$

$$
\boxed{
0\le I_f-L(f,P)\le U(f,P)-L(f,P),\qquad
0\le U(f,P)-I_f\le U(f,P)-L(f,P).}
\tag{21.4.7}
$$

Si $P\preccurlyeq Q$, ambos errores extremos son no crecientes:

$$
0\le I_f-L(f,Q)\le I_f-L(f,P),\qquad
0\le U(f,Q)-I_f\le U(f,P)-I_f.
\tag{21.4.8}
$$

En particular, una partición con $U(f,P)-L(f,P)<\varepsilon$ determina un intervalo numérico $[L(f,P),U(f,P)]$ de anchura menor que $\varepsilon$ que contiene el valor integral; sus dos sumas lo aproximan con error estrictamente menor que $\varepsilon$.

**Demostración.**
Por Proposición §21.3.4 — Orden y encierro de las integrales extremas, para cada $P$,

$$
L(f,P)\le\underline{\int_a^b}f
=I_f
=\overline{\int_a^b}f\le U(f,P),
$$

donde las igualdades proceden de la integrabilidad y de la definición (21.4.5). Ésta es (21.4.6). Restando $L(f,P)$ o $I_f$ en las desigualdades correspondientes, y usando que $I_f$ permanece dentro del mismo intervalo, se obtienen las dos cotas de (21.4.7).

Si $P\preccurlyeq Q$, el teorema Teorema §21.2.8 — Monotonía de las sumas bajo refinamiento da

$$
L(f,P)\le L(f,Q)\le I_f\le U(f,Q)\le U(f,P).
$$

Restar las cantidades fijas pertinentes demuestra (21.4.8). La última afirmación se deduce directamente de (21.4.6)–(21.4.7) y de la definición de longitud del intervalo real. No se presupone que el valor $I_f$ sea una suma inferior o superior alcanzada. $\square$

### Corolario 21.4.5 — Aproximación bilateral y unicidad del número aproximado
Sea $f:[a,b]\to\mathbb R$ acotada, con $a<b$. Las siguientes afirmaciones son equivalentes:

1. $f$ es integrable en $[a,b]$.
2. Existe un número real $J$ tal que, para **todo** $\varepsilon>0$, existe una partición $P$ que satisface simultáneamente
   $$
   \boxed{J-\varepsilon<L(f,P)\le U(f,P)<J+\varepsilon.}
   \tag{21.4.9}
   $$

Si se cumple (2), ese $J$ es **único** y coincide con $\int_a^b f$. En consecuencia, el valor integral también puede caracterizarse como el único real que admite aproximación bilateral mediante las sumas de una misma partición, aunque su definición primaria continúa siendo (21.4.5).

**Demostración.**
**(1 $\Rightarrow$ 2).** Definamos $J:=\int_a^b f$. Por Corolario §21.3.5 — Aproximación simultánea mediante una partición, para un $\varepsilon>0$ fijado existe una partición $P$ para la cual

$$
J-\varepsilon<L(f,P)\le J\le U(f,P)<J+\varepsilon.
$$

En particular, cumple (21.4.9).

**(2 $\Rightarrow$ 1).** Supongamos que existe $J$ con (21.4.9). Dado $\delta>0$, apliquemos la propiedad a $\varepsilon:=\delta/2>0$. La partición obtenida satisface

$$
0\le U(f,P)-L(f,P)
<(J+\delta/2)-(J-\delta/2)=\delta.
$$

El criterio de Darboux Teorema §21.4.2 — Criterio de Darboux y estabilidad por refinamiento demuestra que $f$ es integrable.

**Identificación y unicidad de $J$.** Ya justificada la integrabilidad, pongamos $I_f:=\int_a^b f$. Para cualquier $\varepsilon>0$ tomemos el testigo de (21.4.9). Por (21.4.6),

$$
J-\varepsilon<L(f,P)\le I_f\le U(f,P)<J+\varepsilon,
$$

de modo que $|I_f-J|<\varepsilon$. Si $I_f\ne J$, la tolerancia positiva $\varepsilon:=|I_f-J|/2$ contradice esta última desigualdad. Luego $J=I_f$. Cualquier otro real con la misma propiedad coincide igualmente con $I_f$ y, por consiguiente, con $J$. No fue necesaria una selección simultánea de particiones para todos los valores de $\varepsilon$. $\square$

**Primer ejemplo, ahora legítimamente integral.** Para la función constante $f(t)=c$, §21.2 probó que toda partición verifica $L(f,P)=U(f,P)=c(b-a)$. Por el criterio de Darboux, $f$ es integrable y

$$
\int_a^b c\,dt=c(b-a).
\tag{21.4.10}
$$

Ésta es una consecuencia de las sumas de Darboux y la telescopía de las anchuras; **no** se ha utilizado una regla de primitivas ni el teorema fundamental del cálculo.

### Proposición 21.4.6 — Una función acotada que no es integrable
La acotación, por sí sola, no garantiza integrabilidad. Sea $j:\mathbb Q\to\mathbb R$ la incrustación canónica de Definición §12.2.3 — Copia canónica de los racionales en un cuerpo ordenado y sea $D:=j[\mathbb Q]\subseteq\mathbb R$. En $I=[a,b]$, con $a<b$, definamos una función de dominio exactamente $I$ y codominio $\mathbb R$ mediante

$$
\chi_D(t):=\begin{cases}
1_{\mathbb R},&t\in D,\\
0_{\mathbb R},&t\notin D.
\end{cases}
\tag{21.4.11}
$$

Entonces $\chi_D$ está acotada, pero sus integrales extremas son distintas:

$$
\boxed{\underline{\int_a^b}\chi_D=0_{\mathbb R},\qquad
\overline{\int_a^b}\chi_D=b-a>0_{\mathbb R}.}
\tag{21.4.12}
$$

Por tanto, $\chi_D$ **no es integrable** en $[a,b]$.

**Demostración.**
La pertenencia $t\in D$ o su negación produce dos ramas disjuntas y exhaustivas. Separar dentro de $I\times\mathbb R$ los pares determinados por (21.4.11) da el grafo de una función tipada. Se verifica $0_{\mathbb R}\le\chi_D(t)\le1_{\mathbb R}$ para todo $t\in I$, por lo que la función está acotada.

Fijemos **una partición arbitraria** $P=\langle n,p\rangle$. Cada celda $I_k(P)=[x_k,x_{S(k)}]$ tiene interior no vacío, pues $x_k<x_{S(k)}$. Proposición §15.9.9 — Dos subconjuntos densos disjuntos demuestra que tanto $D=j[\mathbb Q]$ como su complemento $\mathbb R\setminus D$ son densos; en particular, **cada intervalo abierto no vacío** $(x_k,x_{S(k)})$ contiene algún punto de cada conjunto. La imagen de $I_k(P)$ por $\chi_D$ es, por ello, exactamente $\{0_{\mathbb R},1_{\mathbb R}\}$, de donde

$$
m(\chi_D,I_k(P))=0_{\mathbb R},\qquad
M(\chi_D,I_k(P))=1_{\mathbb R}.
$$

No hemos seleccionado simultáneamente puntos testigo para las diferentes celdas: se utiliza directamente, para cada índice, la propiedad universal de densidad. Las definiciones de Darboux y la identidad de anchuras Proposición §21.1.2 — Existencia, anchuras positivas y suma de longitudes proporcionan, para **toda** partición $P$,

$$
L(\chi_D,P)=0_{\mathbb R},\qquad
U(\chi_D,P)=\sum_{k<n}\Delta_k(P)=b-a.
$$

Así, los conjuntos de sumas de Definición §21.3.1 — Conjuntos de sumas inferiores y superiores son los respectivos singletons $\{0_{\mathbb R}\}$ y $\{b-a\}$. Su supremo y su ínfimo, definidos antes de utilizarlos en Definición §21.3.3 — Integrales inferior y superior de Darboux, son los dos números de (21.4.12). Como $a<b$, son diferentes; falla la igualdad de Definición §21.4.1 — Integrabilidad de Darboux por igualdad de integrales extremas. $\square$

**Interpretación.** Los dos conjuntos densos obligan a que cada subintervalo de anchura positiva contenga las dos alturas. Ningún refinamiento reduce la brecha: $U(\chi_D,P)-L(\chi_D,P)=b-a$ para todas las particiones. El ejemplo muestra que la hipótesis «acotada» es necesaria para construir las sumas finitas, pero insuficiente para garantizar su convergencia al mismo valor.

**Transición.** Hemos definido el valor integral sin circularidad, demostrado su unicidad y establecido un criterio finito de integrabilidad y control de errores. §21.5 desarrollará las primeras propiedades algebraicas y de orden de la integral, distinguiendo siempre entre las desigualdades de las sumas y la preservación de la integrabilidad. Las secciones siguientes demostrarán la estructura algebraica de la integral, su aditividad por intervalos y la integrabilidad de funciones continuas y monótonas; finalmente, las sumas etiquetadas permitirán caracterizar el mismo valor.
