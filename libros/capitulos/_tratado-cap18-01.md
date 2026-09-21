## 18.1. Cubiertas abiertas y subcubiertas finitas {#sec-ta-18-1}

El adjetivo «finita» afecta al **número de miembros que se conservan**, no al número de puntos cubiertos. Un conjunto infinito puede quedar cubierto por un solo abierto; por otra parte, una cubierta cuyos miembros son todos abiertos puede no admitir una reducción finita. Comenzaremos haciendo explícitos los objetos y sus tipos.

### Definición 18.1.1 — Conjunto finito
Diremos que un conjunto $F$ es **finito** si existen $n\in\mathbb N$ y una biyección tipada $e:n\to F$, donde $n$ es el ordinal natural de von Neumann ya construido. En símbolos,

$$
\boxed{F\text{ es finito}\iff\exists n\in\mathbb N\ \exists e:n\overset{\sim}{\longrightarrow}F.}
$$

Aquí la flecha adornada indica, **únicamente en esta fórmula**, que $e$ es biyectiva en el sentido de Definición §0.6.6 — Inyectividad, sobreyectividad y biyectividad; no se introduce una nueva operación. El ordinal $0=\varnothing$ se admite: la función vacía $0\to\varnothing$ es biyectiva y acredita que el vacío es finito. Esta formulación hace preciso el uso de «finito» empleado en los capítulos previos; no altera sus resultados. La biyección es un testigo de finitud, no una enumeración que debamos elegir simultáneamente para todos los conjuntos finitos.

### Lema 18.1.2 — Herencia, adjunción y unión de conjuntos finitos
Sean $F,G$ conjuntos finitos, $H\subseteq F$ y $z$ un conjunto cualquiera. Entonces $H$, $F\cup\{z\}$ y $F\cup G$ son finitos.

**Demostración.**
**Adjunción de un punto.** Sea $e:n\to F$ una biyección, cuya existencia constituye un único dato fijado. Si $z\in F$, entonces $F\cup\{z\}=F$. Si $z\notin F$, definimos $e':n+1\to F\cup\{z\}$ conservando $e'(k)=e(k)$ para $k\in n$ y poniendo $e'(n)=z$. El grafo se obtiene añadiendo a $G_e$ el par $\langle n,z\rangle$; es funcional, inyectivo y sobreyectivo porque $n\notin n$ y $z\notin F$. En ambos casos el conjunto resultante es finito.

**Herencia.** Probemos por inducción en $n$ que, para toda biyección $e:n\to F$ y todo $H\subseteq F$, el conjunto $H$ es finito. Si $n=0$, también $F=H=\varnothing$, y sirve la biyección vacía. Para el paso, dada $e:n+1\to F$, su restricción a $n$ es una biyección sobre $F':=e[n]$. Por la hipótesis inductiva, $H':=H\cap F'$ es finito. Si $e(n)\in H$, entonces $H=H'\cup\{e(n)\}$, finito por la adjunción ya probada; si $e(n)\notin H$, entonces $H=H'$. La inducción de Teorema §1.1.10 — Principio de inducción concluye el resultado para todo $n$ y, por tanto, para todo $F$ finito.

**Unión.** Fijemos una biyección $g:m\to G$ y, para cada $k\le m$, formemos $H_k:=F\cup g[k]$. Se trata de conjuntos existentes por imagen y unión, y $H_0=F$. Si $k<m$ y $H_k$ es finito, la igualdad $H_{k+1}=H_k\cup\{g(k)\}$ y la adjunción demuestran que $H_{k+1}$ es finito. Una inducción finita sobre los índices hasta $m$ prueba que $H_m=F\cup G$ es finito. Se utilizaron las dos biyecciones fijadas para un par dado de conjuntos; no se seleccionó una biyección para cada miembro de una familia arbitraria. ∎

### Definición 18.1.3 — Cubierta abierta y subcubierta finita
Sean $K\subseteq\mathbb R$, $I$ un conjunto y $U:I\to\mathcal P(\mathbb R)$ una **función dada**. Diremos que $U=(U_i)_{i\in I}$ es una **cubierta abierta de $K$** si se cumplen las dos condiciones

$$
\boxed{\left(\forall i\in I:\ U_i\text{ es abierto en }\mathbb R\right)
\quad\land\quad K\subseteq\bigcup_{i\in I}U_i.}
$$

Un subconjunto $J\subseteq I$ determina la familia restringida $U\upharpoonright J:J\to\mathcal P(\mathbb R)$. Lo llamaremos **subcubierta finita** si $J$ es finito y

$$
\boxed{K\subseteq\bigcup_{i\in J}U_i.}
$$

La condición de cobertura puede leerse sin abreviar:

$$
\forall x\in K\ \exists i\in I:\ x\in U_i.
$$

Esto no significa que ya se haya construido una función que elija un índice $i$ para **cada** $x\in K$. La familia $U$ está dada y su grafo tiene dominio y codominio explícitos. Se admiten índices repetidos en el sentido de que $U_i=U_j$ puede ocurrir con $i\ne j$; los índices no se identifican con los propios abiertos. Si $I=\varnothing$, la unión es vacía y la familia sólo cubre $K=\varnothing$. Si $J=\varnothing$, su unión es también vacía y sólo puede ser subcubierta de un conjunto vacío.

### Definición 18.1.4 — Compacidad por cubiertas abiertas
Un conjunto $K\subseteq\mathbb R$ se denomina **compacto** si **toda** cubierta abierta indexada de $K$ admite una subcubierta finita. La formulación completa es

$$
\boxed{\begin{gathered}
\forall I\ \forall U:I\to\mathcal P(\mathbb R),\\
\left[\bigl(\forall i\in I:\ U_i\text{ abierto}\bigr)
\land K\subseteq\bigcup_{i\in I}U_i\right]\\
\Longrightarrow\exists J\subseteq I:\left[J\text{ finito}\land
K\subseteq\bigcup_{i\in J}U_i\right].
\end{gathered}}
$$

Los cuantificadores sobre $I$ y $U$ expresan un esquema de propiedades de conjuntos y funciones dados, no una comprensión irrestricta que pretenda formar «el conjunto de todas las familias». El subconjunto $J$ puede depender de la cubierta completa, pero una vez fijado debe cubrir **todos** los puntos de $K$. Esta es la definición primaria; todavía no se han demostrado sus posibles caracterizaciones mediante sucesiones, cerradura y acotación. En particular, no llamaremos compacto a un conjunto *por definición* sólo porque sea cerrado y acotado.

### Proposición 18.1.5 — El vacío y los singletons son compactos
El conjunto vacío es compacto. Para todo $a\in\mathbb R$, el conjunto $\{a\}$ es compacto.

**Demostración.**
Fijemos una cubierta abierta $U:I\to\mathcal P(\mathbb R)$ de $\varnothing$. El subconjunto $J=\varnothing\subseteq I$ es finito por Definición §18.1.1 — Conjunto finito y cumple $\varnothing\subseteq\bigcup_{i\in J}U_i=\varnothing$. Así, $\varnothing$ es compacto, también cuando la cubierta tiene índice vacío.

Fijemos ahora $a\in\mathbb R$ y una cubierta abierta $U$ de $\{a\}$. La inclusión $a\in\bigcup_{i\in I}U_i$ suministra **un** índice $i_0\in I$ con $a\in U_{i_0}$. El conjunto $J=\{i_0\}$ es finito porque la función de dominio $1$ que envía $0$ a $i_0$ es biyectiva sobre él; además $\{a\}\subseteq U_{i_0}=\bigcup_{i\in J}U_i$. Como la cubierta inicial era arbitraria, el singleton es compacto. Se eligió un índice para una única cubierta de un único punto, no una familia simultánea de índices. ∎

### Proposición 18.1.6 — La unión de dos compactos es compacta
Si $K,L\subseteq\mathbb R$ son compactos, entonces $K\cup L$ es compacto.

**Demostración.**
Sea $U:I\to\mathcal P(\mathbb R)$ una cubierta abierta de $K\cup L$. Como $K\subseteq K\cup L$ y $L\subseteq K\cup L$, la **misma familia** cubre por separado a $K$ y a $L$. La compacidad proporciona un conjunto finito de índices $J_K\subseteq I$ que cubre $K$, y otro conjunto finito $J_L\subseteq I$ que cubre $L$. Pongamos $J:=J_K\cup J_L$. Es finito por Lema §18.1.2 — Herencia, adjunción y unión de conjuntos finitos y está contenido en $I$. Todo $x\in K\cup L$ pertenece a uno de los dos conjuntos y, en consecuencia, a algún $U_i$ con $i\in J_K$ o $i\in J_L$; por ello $K\cup L\subseteq\bigcup_{i\in J}U_i$. Esta es una subcubierta finita de la familia original. Sólo se combinaron dos testigos existenciales de una cubierta fijada: no se utilizó elección infinita. ∎

### Corolario 18.1.7 — Todo conjunto finito de reales es compacto
Todo subconjunto finito $F\subseteq\mathbb R$ es compacto. En particular, una unión finita de compactos es compacta.

**Demostración.**
Fijemos una biyección $e:n\to F$. Para cada $k\le n$, definamos $F_k:=e[k]\subseteq\mathbb R$. Mostremos por inducción sobre $k$ hasta $n$ que $F_k$ es compacto. El caso inicial es $F_0=\varnothing$, compacto por Proposición §18.1.5 — El vacío y los singletons son compactos. Si $k<n$ y $F_k$ es compacto, entonces $F_{k+1}=F_k\cup\{e(k)\}$; el singleton es compacto por Proposición §18.1.5 — El vacío y los singletons son compactos y la unión por Proposición §18.1.6 — La unión de dos compactos es compacta. Al finalizar, $F_n=F$ es compacto.

Para la afirmación adicional, dada una familia $C:n\to\mathcal P(\mathbb R)$ de conjuntos compactos, el mismo argumento parte de la unión vacía y añade sucesivamente el conjunto $C(k)$; cada paso aplica Proposición §18.1.6 — La unión de dos compactos es compacta. El resultado es $\bigcup_{k\in n}C(k)$, incluso si $n=0$. Una familia finita dada con cualquier conjunto de índices finito se reindexa mediante una de sus biyecciones testigo. No se escogen cubiertas ni subcubiertas para infinitos índices. ∎

### Proposición 18.1.8 — La recta real no es compacta
La familia de intervalos abiertos

$$
U_n:=\bigl(-\nu_{\mathbb R}(n+1),\nu_{\mathbb R}(n+1)\bigr),
\qquad n\in\mathbb N,
$$

es una cubierta abierta de $\mathbb R$ que **no** admite subcubierta finita. En consecuencia, $\mathbb R$ no es compacto.

**Demostración.**
La aplicación $n\mapsto U_n$ determina una función $U:\mathbb N\to\mathcal P(\mathbb R)$: el intervalo de extremos determinados existe y su grafo se forma por Separación en $\mathbb N\times\mathcal P(\mathbb R)$. Cada $U_n$ es abierto por Proposición §15.2.9 — Ejemplos: intervalos abiertos y singletons. Dado $x\in\mathbb R$, la propiedad arquimediana (Teorema §4.6.3 — Todo cuerpo ordenado completo es arquimediano, aplicada a $\mathbb R$ por Teorema §12.8.1 — Existencia y caracterización única de la completación ordenada de $\mathbb Q$) proporciona un natural $n$ con $\nu_{\mathbb R}(n+1)>|x|$. Entonces $x\in U_n$. Por tanto, $\mathbb R=\bigcup_{n\in\mathbb N}U_n$.

Supongamos que un conjunto finito $J\subseteq\mathbb N$ diese una subcubierta. No puede ser vacío porque $0\in\mathbb R$ y la unión vacía no contiene puntos. Un subconjunto finito no vacío de $\mathbb N$ tiene un máximo $m\in J$: fijada una biyección $e:k\to J$, necesariamente $k\ne0$; al recorrer sus $k$ valores, la inducción finita conserva el mayor de los ya examinados tomando, en cada paso, el mayor de dos naturales según el orden total Teorema §1.6.5 — Orden total. Esto prueba la existencia del máximo sin escoger elementos de una familia arbitraria.

Para cada $j\in J$ tenemos $j\le m$, de donde $U_j\subseteq U_m$ por el orden de los numerales (Proposición §4.1.6 — Aritmética y orden de los numerales naturales). El punto real $x:=\nu_{\mathbb R}(m+2)$ pertenece a $\mathbb R$ pero no a $U_m$, pues es mayor que el extremo derecho $\nu_{\mathbb R}(m+1)$. En consecuencia, no pertenece a ninguno de los $U_j$ con $j\in J$, contradicción con que $J$ cubra la recta. Esta cubierta concreta demuestra la falta de compacidad de $\mathbb R$, sin recurrir a Heine–Borel ni al concepto todavía no definido de compacidad secuencial. ∎

**Lectura conceptual.** La apertura de los miembros sólo garantiza que cada punto posee un pequeño margen dentro de algún abierto. La compacidad exige algo global y mucho más fuerte: reducir **cualquier** cubierta a una subfamilia finita. Los conjuntos finitos poseen esa propiedad; la recta entera no la posee, aunque cada uno de sus puntos pertenezca a muchos intervalos abiertos. La sección §18.2 demostrará que los intervalos cerrados y acotados sí tienen la propiedad de reducción finita, utilizando la completitud del orden real y no una caracterización de compacidad aún no probada.
