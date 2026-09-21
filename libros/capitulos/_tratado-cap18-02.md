## 18.2. Compacidad de los intervalos cerrados y acotados {#sec-ta-18-2}

La definición anterior exige una reducción finita de **cualquier** cubierta abierta. No basta exhibir una cubierta particularmente sencilla. Demostraremos la propiedad para $[a,b]$ sin emplear todavía Heine–Borel ni equivalencias secuenciales: el argumento sólo necesita la propiedad del supremo, la apertura de los miembros de una cubierta dada y las operaciones finitas ya legitimadas en §18.1.

### Teorema 18.2.1 — Todo intervalo cerrado y acotado es compacto
Para cualesquiera $a,b\in\mathbb R$ tales que $a\le b$, el intervalo $[a,b]$ es compacto: toda cubierta abierta indexada del intervalo posee una subcubierta finita.

**Demostración.**
**1. La cubierta y los segmentos ya cubiertos finitamente.** Fijemos un conjunto de índices $I$ y una familia dada $U:I\to\mathcal P(\mathbb R)$ de abiertos tal que

$$
[a,b]\subseteq\bigcup_{i\in I}U_i.
$$

Queremos encontrar un solo conjunto finito $J\subseteq I$ con $[a,b]\subseteq\bigcup_{i\in J}U_i$. Definamos por Separación dentro del conjunto $[a,b]$:

$$
S:=\left\{x\in[a,b]:\ \exists J\subseteq I\ \bigl(J\text{ finito}\ \land\ [a,x]\subseteq\bigcup_{i\in J}U_i\bigr)\right\}.
$$

La condición es una fórmula conjuntista: $J$ varía dentro de $\mathcal P(I)$, la finitud tiene la definición Definición §18.1.1 — Conjunto finito y las uniones están determinadas por la familia ya dada. No estamos formando una colección irrestricta ni escogiendo un $J_x$ para todos los $x\in S$.

El conjunto $S$ es no vacío. En efecto, $a\in[a,b]$, así que la cubierta proporciona **un** índice $i_a\in I$ con $a\in U_{i_a}$. Como $[a,a]=\{a\}$, el singleton de índices $\{i_a\}$ cubre $[a,a]$, y es finito. Por consiguiente $a\in S$. Además $S\subseteq[a,b]$, de modo que $b$ es una cota superior suya.

**2. Un supremo que no puede detener el avance.** La completitud de $\mathbb R$ garantiza

$$
c:=\sup S,\qquad a\le c\le b.
$$

Como $c\in[a,b]$, existe **un** índice $i_c\in I$ con $c\in U_{i_c}$. La apertura de $U_{i_c}$ proporciona $r>0$ tal que

$$
B_r(c)=(c-r,c+r)\subseteq U_{i_c}.
$$

Afirmamos que existe $t\in S$ con $c-r/2<t\le c$. Si no existiera, $c-r/2$ sería una cota superior de $S$, estrictamente menor que $c$, contradiciendo la definición de supremo. Fijemos **un** tal $t$. Por pertenecer a $S$, existe un conjunto finito de índices $J_t\subseteq I$ que cubre $[a,t]$. Sólo se han fijado dos testigos asociados a esta cubierta: el índice $i_c$ y una subcubierta para este $t$ particular.

Sea

$$
d:=\min\{b,c+r/2\},
$$

entendiendo el mínimo de estos **dos** reales por comparación en el orden total. Como $c\le b$ y $r>0$, tenemos $c\le d\le b$; si $c<b$, entonces $c<d$. Para todo $y\in[t,d]$ se verifica

$$
c-r<c-r/2<t\le y\le d\le c+r/2<c+r.
$$

Así, $[t,d]\subseteq B_r(c)\subseteq U_{i_c}$. Como $[a,d]=[a,t]\cup[t,d]$, la familia de índices

$$
J':=J_t\cup\{i_c\}
$$

cubre $[a,d]$. Es finita por Lema §18.1.2 — Herencia, adjunción y unión de conjuntos finitos y está contenida en $I$; por tanto, $d\in S$.

Al ser $c$ cota superior de $S$, obtenemos $d\le c$. Junto con $c\le d$, resulta $d=c$. Pero, si $c<b$, la construcción de $d$ daría $c<d$: contradicción. Necesariamente $c=b$. Y como $d=c=b\in S$, la propia definición de $S$ suministra una subcubierta finita de $[a,b]$, que era exactamente lo exigido.

**3. Control fundacional.** La cubierta $U$ se mantuvo arbitraria durante toda la demostración. El supremo existe por completitud; la obtención de un índice que cubre un punto y de una subcubierta para un único $t$ utiliza sólo instanciación existencial finita. En ningún momento se construye una función $x\mapsto i_x$ ni una elección simultánea de subcubiertas $x\mapsto J_x$. Tampoco se ha invocado un resultado posterior. $\square$

**Lectura de la prueba.** La completitud convierte una colección de segmentos que ya podemos cubrir finitamente en un punto extremo $c$. La apertura de un único miembro que contiene a $c$ impide que la cobertura finita se interrumpa allí. El argumento también comprende $a=b$: en ese caso el supremo es el único punto del intervalo y la construcción produce directamente su subcubierta finita.

### Proposición 18.2.2 — Un cerrado relativo de un compacto es compacto
Sea $K\subseteq\mathbb R$ compacto y sea $A\subseteq K$ cerrado **relativo a $K$**. Entonces $A$ es compacto. En particular, la intersección de un compacto de la recta con un cerrado de la recta es compacta.

**Demostración.**
Por la representación de cerrados relativos Proposición §17.3.2 — Criterio por bolas y representación de los cerrados relativos, existe un cerrado $F\subseteq\mathbb R$ con $A=K\cap F$. Fijemos una cubierta abierta arbitraria $U:I\to\mathcal P(\mathbb R)$ de $A$. Su cobertura no tiene por qué alcanzar a los puntos de $K\setminus A$; añadiremos **un único abierto**, el complemento $V:=\mathbb R\setminus F$, abierto por Definición §15.3.5 — Conjunto cerrado de la recta.

Para conservar el tipado incluso si algún miembro original coincide con $V$, definamos el conjunto de índices etiquetados

$$
I^*:=(I\times\{0\})\cup\{\langle\varnothing,1\rangle\}.
$$

Los números naturales $0$ y $1$ son distintos; por la propiedad característica de los pares ordenados, el índice excepcional $\langle\varnothing,1\rangle$ no coincide con ninguno de los $\langle i,0\rangle$. La fórmula

$$
W_{\langle i,0\rangle}:=U_i\quad(i\in I),
\qquad W_{\langle\varnothing,1\rangle}:=V
$$

construye, mediante Separación en $I^*\times\mathcal P(\mathbb R)$, una función tipada $W:I^*\to\mathcal P(\mathbb R)$. Todos sus valores son abiertos. Si $x\in K$, o bien $x\in F$, y entonces $x\in A$ está cubierto por algún $U_i$, o bien $x\in\mathbb R\setminus F=V$. Por tanto $W$ cubre $K$.

La compacidad de $K$ proporciona un conjunto finito $J^*\subseteq I^*$ tal que $K\subseteq\bigcup_{j\in J^*}W_j$. Retengamos sólo los índices originales que aparecen etiquetados:

$$
J:=\{i\in I:\ \langle i,0\rangle\in J^*\}.
$$

La intersección $H:=J^*\cap(I\times\{0\})$ es finita, al ser subconjunto de $J^*$ (Lema §18.1.2 — Herencia, adjunción y unión de conjuntos finitos). La proyección tipada $\langle i,0\rangle\mapsto i$ es una biyección $H\to J$, cuyo grafo es definible por Separación; una biyección testigo de la finitud de $H$ compuesta con esta proyección acredita que $J$ es finito. No se eligió un representante de cada abierto: el primer componente del índice etiquetado está unívocamente determinado.

Por último, sea $x\in A$. Algún $j\in J^*$ satisface $x\in W_j$; ese índice no puede ser el excepcional porque $x\in F$ y $W_{\langle\varnothing,1\rangle}=\mathbb R\setminus F$. Por tanto $j=\langle i,0\rangle$ para cierto $i\in J$ y $x\in U_i$. Así $A\subseteq\bigcup_{i\in J}U_i$. Como la cubierta inicial era arbitraria, $A$ es compacto.

Para la última afirmación, si $F$ es cerrado en $\mathbb R$, el conjunto $K\cap F$ es cerrado relativo a $K$ por Definición §17.3.1 — Abiertos y cerrados relativos a un subconjunto de la recta y Proposición §17.3.2 — Criterio por bolas y representación de los cerrados relativos; aplicamos lo demostrado. $\square$

### Corolario 18.2.3 — Casos degenerados y uniones finitas de intervalos
Para cualquier par $a,b\in\mathbb R$, el conjunto definido por la notación de intervalo cerrado $[a,b]$ es compacto, incluido el caso $a>b$, en el que es vacío. Toda unión finita de intervalos cerrados y acotados de la recta es compacta.

**Demostración.**
Si $a\le b$, aplicamos Teorema §18.2.1 — Todo intervalo cerrado y acotado es compacto. Si $a>b$, la definición de intervalo da $[a,b]=\varnothing$, compacto por Proposición §18.1.5 — El vacío y los singletons son compactos. No existe un tercer caso por el orden total real. Sea ahora una familia de intervalos cerrados y acotados $C:I\to\mathcal P(\mathbb R)$ cuyo conjunto de índices $I$ sea finito. Cada $C_i$ es compacto por la primera afirmación. La unión es compacta por la afirmación de unión finita de Corolario §18.1.7 — Todo conjunto finito de reales es compacto, reindexando si es necesario mediante una biyección testigo de la finitud de $I$. El caso $I=\varnothing$ vuelve a dar el conjunto vacío. $\square$

**Transición.** Hemos obtenido la dirección de suficiencia más importante para Heine–Borel: todos los intervalos $[a,b]$ son compactos, y todo cerrado que se encuentre dentro de uno de ellos hereda la compacidad. Aún no hemos demostrado que **todo** compacto real deba ser cerrado y acotado. Ése será el siguiente problema y permitirá reconocer la equivalencia exacta, sin convertirla retrospectivamente en una definición.
