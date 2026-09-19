## 15.8. Descripciones secuenciales y el alcance de la elección {#sec-ta-15-8}

Las sucesiones reales se construyeron en el Capítulo 13, antes de definir la topología de la recta. Podemos conectar ahora ambos lenguajes: si todos los términos de una sucesión pertenecen a un conjunto, ¿dónde puede situarse su límite? La dirección desde una **sucesión ya dada** hasta una propiedad topológica es inmediata. La dirección contraria exige mayor cuidado: de la afirmación «cada bola contiene algún punto de $A$» no se obtiene automáticamente, en ZF, una función que elija un punto de $A$ para cada uno de infinitos radios.

Desarrollaremos primero las caracterizaciones que sólo utilizan cuantificadores sobre puntos individuales. Después introduciremos los límites efectivamente representados por sucesiones y demostraremos cuándo una enumeración previa permite construir una sucesión de aproximantes. Los teoremas generales habituales se presentarán, al final, **sólo bajo una hipótesis de elección numerable expresamente declarada**. Esa hipótesis no forma parte del fundamento de este tratado.

### Lema 15.8.1 — Una escala numerable cofinal de radios positivos

Para cada $n\in\mathbb N$, definamos, como abreviatura local,

$$
\eta_n:=\bigl(\nu_{\mathbb R}(S(n))\bigr)^{-1}.
$$

Entonces $\eta_n>0$ para todo $n$ y

$$
\boxed{\forall r\in\mathbb R\;(r>0\ \Longrightarrow\
\exists N\in\mathbb N\ \forall n\ge N\ (0<\eta_n<r)).}
$$

**Demostración.**

El sucesor $S(n)$ es un natural positivo. La aplicación de numerales $\nu_{\mathbb R}$ preserva el orden, de modo que su imagen es un real positivo y su inverso existe y es positivo. El lema Lema 13.10.2 — Los recíprocos de los numerales positivos tienden a cero, especializado al cuerpo real estructural, prueba precisamente que la sucesión de estos recíprocos converge a cero. Dado $r>0$, su definición de convergencia proporciona $N\in\mathbb N$ tal que $n\ge N$ implica $|\eta_n-0|<r$. Como $\eta_n>0$, esto equivale a $0<\eta_n<r$. ∎

La sucesión $\eta$ está determinada término a término por una fórmula. No hemos elegido un radio de cada una de una familia de conjuntos: hemos definido **una única escala numérica**, disponible para todas las pruebas de esta sección.

### Teorema 15.8.2 — Pruebas de proximidad con radios numerables

Sea $A\subseteq\mathbb R$ y $x\in\mathbb R$. Con la escala $\eta_n$ del lema anterior se verifican las cinco equivalencias siguientes:

$$
\boxed{x\in\overline A\iff\
\forall n\in\mathbb N\ \exists a\in A\ (|a-x|<\eta_n);}
$$

$$
\boxed{x\in\operatorname{Acc}(A)\iff\
\forall n\in\mathbb N\ \exists a\in A\ (a\ne x\ \land\ |a-x|<\eta_n);}
$$

$$
\boxed{x\in\partial A\iff
\begin{cases}
\forall n\in\mathbb N\ \exists a\in A\ (|a-x|<\eta_n),\\
\forall n\in\mathbb N\ \exists b\in\mathbb R\setminus A\ (|b-x|<\eta_n);
\end{cases}}
$$

$$
\boxed{x\in A^\circ\iff\exists n\in\mathbb N\ (B_{\eta_n}(x)\subseteq A),}
$$

$$
\boxed{x\in\operatorname{Ext}(A)\iff\exists n\in\mathbb N\
(B_{\eta_n}(x)\cap A=\varnothing).}
$$

**Demostración.**

**Adherencia.** Si $x\in\overline A$, toda bola positiva centrada en $x$ corta a $A$; en particular lo hace $B_{\eta_n}(x)$, pues $\eta_n>0$. Para cada $n$ fijo, la pertenencia a esa intersección proporciona *un* $a\in A$ con $|a-x|<\eta_n$. Recíprocamente, supongamos la condición cuantificada sobre $n$ y fijemos un radio arbitrario $r>0$. El lema anterior proporciona un índice $n$ con $\eta_n<r$. Por hipótesis, existe un punto $a\in A$ a distancia menor que $\eta_n$; ese mismo punto pertenece a $B_r(x)$. Como $r$ era arbitrario, $x$ es adherente.

**Acumulación.** Repetimos exactamente el argumento, sustituyendo $A$ por $A\setminus\{x\}$ en las intersecciones de bolas. La desigualdad $a\ne x$ permanece explícita: no basta con permitir que el centro actúe como testigo.

**Frontera.** Su definición exige que cada bola corte tanto a $A$ como a $\mathbb R\setminus A$. Aplicamos por separado el razonamiento de adherencia a los dos conjuntos. No exigimos que ambos testigos sean el mismo punto; de hecho, pertenecen a conjuntos disjuntos.

**Interior.** Si $x\in A^\circ$, existe $r>0$ con $B_r(x)\subseteq A$. Tomamos $n$ tal que $\eta_n<r$ y usamos la inclusión de bolas concéntricas para obtener $B_{\eta_n}(x)\subseteq A$. La implicación inversa usa directamente el radio positivo $\eta_n$ como testigo de interioridad.

**Exterior.** Un punto es exterior si alguna bola positiva centrada en él es disjunta de $A$. Una bola de radio $\eta_n$ suficientemente pequeño está contenida en ella; recíprocamente, una bola de radio $\eta_n$ disjunta ya proporciona un radio legítimo. ∎

> **Distinción lógica.** Las primeras condiciones tienen la forma $\forall n\,\exists a\,P(n,a)$. No dicen $\exists(a_n)\,\forall n\,P(n,a_n)$. La segunda fórmula afirma la existencia de una **función** sobre $\mathbb N$ y es más fuerte en ZF. Ninguna de las cinco equivalencias anteriores necesita convertir la primera fórmula en la segunda.

### Definición 15.8.3 — Clausura secuencial de un conjunto

Para $A\subseteq\mathbb R$, definimos su **clausura secuencial** como

$$
\boxed{\operatorname{SCl}(A):=
\{x\in\mathbb R:\exists s\in\mathbb R^{\mathbb N}\ 
[\,\forall n\in\mathbb N\ (s_n\in A)\ \land\ s_n\to x\,]\}.}
$$

La expresión $s_n\to x$ conserva el significado y el tipo fijados en §13.3. La separación se efectúa sobre el conjunto ya existente $\mathbb R$; el cuantificador sobre sucesiones está restringido al conjunto $\mathbb R^{\mathbb N}$, construido en el Capítulo 13. Como la condición determina un subconjunto único para cada $A$, el grafo

$$
\{\langle A,C\rangle\in\mathcal P(\mathbb R)\times\mathcal P(\mathbb R):C=\operatorname{SCl}(A)\}
$$

existe por Separación y define una función $\mathcal P(\mathbb R)\to\mathcal P(\mathbb R)$. Su definición cuantifica sobre sucesiones que **ya existen**; no fabrica una a partir de testigos separados ni utiliza elección.

La notación $\operatorname{SCl}(A)$ distingue esta operación de $\overline A$, cuya definición sigue siendo la de adherencia mediante todas las bolas.

### Proposición 15.8.4 — Propiedades elementales de la clausura secuencial

Para $A,B\subseteq\mathbb R$ se cumplen

$$
\boxed{A\subseteq\operatorname{SCl}(A)\subseteq\overline A,}
$$

$$
\boxed{A\subseteq B\Longrightarrow
\operatorname{SCl}(A)\subseteq\operatorname{SCl}(B),}
$$

$$
\boxed{\operatorname{SCl}(\varnothing)=\varnothing,
\quad\operatorname{SCl}(\mathbb R)=\mathbb R,}
$$

$$
\boxed{\operatorname{SCl}(A\cup B)=
\operatorname{SCl}(A)\cup\operatorname{SCl}(B).}
$$

No afirmamos aquí que $\operatorname{SCl}(A)=\overline A$ ni que la clausura secuencial sea idempotente.

**Demostración.**

**Inclusiones.** Si $x\in A$, la sucesión constante $s_n=x$ tiene todos sus términos en $A$ y converge a $x$ por Proposición 13.3.4 — Las sucesiones constantes convergen a su valor; luego $x\in\operatorname{SCl}(A)$. Si $x\in\operatorname{SCl}(A)$, existe una sucesión $s_n\in A$ convergente a $x$. Para un radio arbitrario $r>0$, la convergencia suministra algún $N$ con $|s_N-x|<r$; por consiguiente $B_r(x)\cap A\ne\varnothing$ y $x\in\overline A$. La monotonía se deduce conservando una sucesión testigo al pasar de $A$ a un conjunto mayor. Ninguna sucesión puede tener todos sus términos en $\varnothing$ porque $0\in\mathbb N$; para $A=\mathbb R$ basta la inclusión ya probada y el hecho de que el codominio de la operación es $\mathcal P(\mathbb R)$.

**Unión, primera inclusión.** Por monotonía, $\operatorname{SCl}(A)$ y $\operatorname{SCl}(B)$ están contenidos en $\operatorname{SCl}(A\cup B)$; también lo está su unión.

**Unión, inclusión inversa.** Sea $x\in\operatorname{SCl}(A\cup B)$ y fijemos una sucesión $s\in\mathbb R^{\mathbb N}$ tal que $s_n\in A\cup B$ para cada $n$ y $s_n\to x$. El conjunto definido por Separación

$$
I:=\{n\in\mathbb N:s_n\in A\}
$$

satisface una de dos alternativas clásicas. Si tiene índices arbitrariamente grandes, el buen orden y la recursión ordinaria sobre los naturales permiten definir $\phi(0):=\min I$ y $\phi(k+1):=\min\{n\in I:n>\phi(k)\}$. El segundo mínimo existe porque $I$ tiene índices arbitrariamente grandes; la función recursiva es estrictamente creciente y satisface $\phi(k)\in I$ para todo $k$. Este es el procedimiento de extracción por mínimos empleado en Proposición 13.10.3 — Criterio de visitas arbitrariamente tardías. La subsucesión $s\circ\phi$ pertenece término a término a $A$ y converge a $x$ por Teorema 13.9.5 — Toda subsucesión de una sucesión convergente converge al mismo límite. Así, $x\in\operatorname{SCl}(A)$.

Si $I$ no tiene índices arbitrariamente grandes, existe $N$ tal que $n\ge N$ implica $s_n\notin A$. Dado que $s_n\in A\cup B$, todos esos términos pertenecen a $B$. La sucesión $t_k:=s_{N+k}$ es una función real sobre $\mathbb N$, pertenece enteramente a $B$ y converge a $x$: para una tolerancia $r>0$ tomamos un índice de convergencia $M$ de $s$, y entonces $k\ge M$ implica $N+k\ge M$. De ello se sigue $x\in\operatorname{SCl}(B)$. Los dos casos agotan las posibilidades y prueban la igualdad. ∎

La extracción anterior **no** elige puntos de conjuntos reales arbitrarios: parte de una sucesión existente y escoge los menores índices de un subconjunto de $\mathbb N$. Es una utilización legítima del buen orden de los naturales.

### Proposición 15.8.5 — Qué prueban las sucesiones convergentes sobre acumulación y frontera

Sean $A\subseteq\mathbb R$ y $x\in\mathbb R$.

1. Si existe una sucesión $s\in\mathbb R^{\mathbb N}$ con $s_n\in A\setminus\{x\}$ para todo $n$ y $s_n\to x$, entonces $x\in\operatorname{Acc}(A)$.
2. Si existen sucesiones $s,t\in\mathbb R^{\mathbb N}$ con $s_n\in A$ y $t_n\in\mathbb R\setminus A$ para todo $n$, ambas convergentes a $x$, entonces $x\in\partial A$.

**Demostración.**

Para (1), fijemos $r>0$. Por convergencia existe $N\in\mathbb N$ con $|s_N-x|<r$. Dado que $s_N\in A\setminus\{x\}$, este término pertenece a la intersección perforada $B_r(x)\cap(A\setminus\{x\})$, que es, por tanto, no vacía. Esto vale para cada $r>0$: $x$ es punto de acumulación.

Para (2), dado $r>0$, la convergencia de $s$ proporciona un índice $N$ con $s_N\in B_r(x)\cap A$; independientemente, la convergencia de $t$ da un índice $M$ con $t_M\in B_r(x)\cap(\mathbb R\setminus A)$. Ambas intersecciones son no vacías, luego $x\in\partial A$. Los índices se obtienen para el único radio fijado y no se construye ninguna sucesión adicional. ∎

Estas implicaciones no tienen una recíproca general demostrable con los axiomas actualmente admitidos. La siguiente proposición muestra cómo recuperarla cuando disponemos de una enumeración efectiva **como función matemática**, aunque no presupongamos que sea computable.

### Teorema 15.8.6 — Caracterizaciones completas para conjuntos enumerados

Sea $A\subseteq\mathbb R$ y supongamos **dada** una sobreyección $e:\mathbb N\to A$. Entonces, para cada $x\in\mathbb R$,

$$
\boxed{x\in\overline A\iff
\exists s\in\mathbb R^{\mathbb N}\ 
[\,\forall n\ (s_n\in A)\ \land\ s_n\to x\,],}
$$

$$
\boxed{x\in\operatorname{Acc}(A)\iff
\exists s\in\mathbb R^{\mathbb N}\ 
[\,\forall n\ (s_n\in A\setminus\{x\})\ \land\ s_n\to x\,].}
$$

La sobreyectividad de $e$ implica $A\ne\varnothing$. La hipótesis no se extiende a una enumeración simultánea de **todo el complemento**: ello conduciría a enumerar la recta, como se probará en Lema 15.8.10 — La recta real no admite una enumeración. La caracterización no vacua de la frontera con dos subconjuntos densos provistos de enumeraciones se establece en Teorema 15.8.11 — Caracterización fronteriza mediante dos lados densamente enumerados.

**Demostración.**

Las implicaciones de derecha a izquierda resultan de Proposición 15.8.4 — Propiedades elementales de la clausura secuencial y Proposición 15.8.5 — Qué prueban las sucesiones convergentes sobre acumulación y frontera. Para las recíprocas describimos una construcción que depende sólo de las sobreyecciones **ya dadas**.

Supongamos $x\in\overline A$. Para cada $n\in\mathbb N$ consideremos el subconjunto de los naturales

$$
I_n:=\{k\in\mathbb N:|e(k)-x|<\eta_n\}.
$$

Por el criterio de Teorema 15.8.2 — Pruebas de proximidad con radios numerables, la bola $B_{\eta_n}(x)$ contiene algún $a\in A$. La sobreyectividad de $e$ da un índice $k$ con $e(k)=a$, así que $I_n$ es no vacío. El principio de buen orden de $\mathbb N$ (Teorema 1.6.13 — Principio de buen orden) le asigna un mínimo único $k_n:=\min I_n$. La fórmula que expresa esta unicidad define, por Separación sobre $\mathbb N\times\mathbb N$, el grafo de una función $n\mapsto k_n$. Componiéndola con $e$ obtenemos la sucesión $s_n=e(k_n)\in A$, con

$$
|s_n-x|<\eta_n\qquad(n\in\mathbb N).
$$

Dado $r>0$, tomamos $N$ de Lema 15.8.1 — Una escala numerable cofinal de radios positivos; para $n\ge N$ tenemos $|s_n-x|<\eta_n<r$. Por definición, $s_n\to x$.

Si $x\in\operatorname{Acc}(A)$, repetimos el mismo procedimiento con el conjunto no vacío

$$
J_n:=\{k\in\mathbb N:e(k)\ne x\ \land\ |e(k)-x|<\eta_n\}.
$$

Sus mínimos determinan una sucesión cuyos términos pertenecen a $A\setminus\{x\}$ y convergen a $x$. La no vaciedad de $J_n$ proviene específicamente de la condición perforada; sería incorrecto sustituirla por la sola adherencia.

La construcción de las dos clases de aproximantes se realiza únicamente dentro del conjunto ya enumerado $A$. Estas son exactamente las dos equivalencias del enunciado, y no necesitan enumerar su complemento. ∎

> **Importancia de la hipótesis.** La enumeración no surge de la frase «$A$ es un subconjunto de la recta». Se entrega como dato estructural. El buen orden selecciona **índices naturales** dentro de una función disponible, no puntos arbitrarios de una familia de subconjuntos de $\mathbb R$.

### Proposición 15.8.7 — Un abierto proporciona aproximantes racionales canónicos

Si $U\subseteq\mathbb R$ es abierto, entonces

$$
\boxed{\operatorname{SCl}(U)=\overline U.}
$$

Más precisamente, para cada $x\in\overline U$ existe una sucesión $s_n\to x$ cuyos términos pertenecen a

$$
U\cap\jmath_{\mathbb Q}^{\mathbb R}[\mathbb Q].
$$

**Demostración.**

La inclusión $\operatorname{SCl}(U)\subseteq\overline U$ ya está probada. Fijemos $x\in\overline U$. Para cada $n$, la bola $B_{\eta_n}(x)$ corta a $U$. Probaremos que contiene también un punto de la copia racional situado en $U$. Sea $y$ un punto de esa intersección, **fijado únicamente para esta demostración local**. La apertura de $U$ proporciona $r>0$ con $B_r(y)\subseteq U$, y Proposición 15.1.3 — Una bola contiene una bola alrededor de cada uno de sus puntos proporciona $d=\eta_n-|y-x|>0$ con $B_d(y)\subseteq B_{\eta_n}(x)$. Tomando $h:=\min\{r,d\}>0$, tenemos

$$
B_h(y)\subseteq U\cap B_{\eta_n}(x).
$$

Por densidad de la copia racional (Corolario 12.3.2 — Densidad racional en todo cuerpo ordenado completo), existe $q\in\mathbb Q$ tal que $\jmath_{\mathbb Q}^{\mathbb R}(q)\in B_h(y)$. Concluye la existencia de un racional situado simultáneamente en $U$ y en la bola original. **No hemos elegido los puntos $y$ ni los radios $r$ para todos los índices**: sólo hemos establecido, para un $n$ arbitrario, que el conjunto siguiente es no vacío:

$$
K_n:=\{k\in\mathbb N:
\jmath_{\mathbb Q}^{\mathbb R}(e_{\mathbb Q}(k))\in
U\cap B_{\eta_n}(x)\}.
$$

La sobreyectividad de la enumeración racional canónica $e_{\mathbb Q}$ (Proposición 10.2.6 — La enumeración racional es sobreyectiva) garantiza su no vaciedad. Definimos ahora $k_n=\min K_n$, de forma única por buen orden, y

$$
s_n:=\jmath_{\mathbb Q}^{\mathbb R}(e_{\mathbb Q}(k_n)).
$$

La definición funcional sobre $\mathbb N$ se obtiene por Separación y composición. Para todos los $n$, $s_n\in U$ y $|s_n-x|<\eta_n$. El lema de la escala prueba $s_n\to x$. Por tanto, $x\in\operatorname{SCl}(U)$, que establece la igualdad. ∎

Este argumento ofrece aproximantes concretamente definidos a partir de una enumeración **canónica preexistente de los racionales**. No implica que un conjunto arbitrario $A$ contenga racionales ni permite aplicar el mismo procedimiento a un conjunto sin apertura.

### Teorema 15.8.8 — Criterios secuenciales de cerradura y apertura: alcance exacto

Sea $A\subseteq\mathbb R$. Sin hipótesis adicional de elección se tienen las implicaciones:

1. Si $A$ es cerrado, toda sucesión $s\in\mathbb R^{\mathbb N}$ con $s_n\in A$ para todo $n$ y $s_n\to x$ satisface $x\in A$.
2. Si $A$ es abierto y $s_n\to x\in A$, entonces existe $N\in\mathbb N$ tal que $s_n\in A$ para todo $n\ge N$.

Además, la primera implicación es una equivalencia **si se dispone de una sobreyección** $e:\mathbb N\to A$; la segunda lo es **si se dispone de una sobreyección** $f:\mathbb N\to\mathbb R\setminus A$. Los casos $A=\varnothing$ en (1) y $A=\mathbb R$ en (2) se verifican directamente, sin enumeración.

**Demostración.**

**Cerradura, dirección general.** Una sucesión con todos sus términos en $A$ y límite $x$ demuestra $x\in\operatorname{SCl}(A)\subseteq\overline A$ por Proposición 15.8.4 — Propiedades elementales de la clausura secuencial. Si $A$ es cerrado, Corolario 15.4.7 — Un conjunto es cerrado si y sólo si coincide con su clausura proporciona $\overline A=A$, luego $x\in A$.

**Apertura, dirección general.** Si $x\in A$ y $A$ es abierto, existe $r>0$ tal que $B_r(x)\subseteq A$. Por $s_n\to x$, existe $N$ tal que $n\ge N$ implica $|s_n-x|<r$. Cada término de esa cola está, pues, en $A$.

**Recíproca de cerradura con enumeración.** Supongamos que $e:\mathbb N\to A$ es sobreyectiva y que todo límite de una sucesión contenida en $A$ pertenece a $A$. Si $x\in\overline A$, el teorema Teorema 15.8.6 — Caracterizaciones completas para conjuntos enumerados construye una sucesión en $A$ que converge a $x$. Por hipótesis $x\in A$. Así $\overline A\subseteq A$; la inclusión inversa siempre vale, de modo que $\overline A=A$ y el conjunto es cerrado.

**Recíproca de apertura con complemento enumerado.** Supongamos que está dada $f:\mathbb N\to C$, donde $C=\mathbb R\setminus A$, y que toda sucesión real convergente a un punto $x\in A$ está eventualmente en $A$. Si $A$ no fuese abierto, existiría $x\in A$ que no es interior. La dualidad de clausura e interior ya establecida implica entonces $x\in\overline C$. Por Teorema 15.8.6 — Caracterizaciones completas para conjuntos enumerados, aplicado a $C$ y a su enumeración $f$, existe una sucesión $t_n\in C$ convergente a $x$. La propiedad eventual exigiría que una cola de esa sucesión perteneciera a $A$, contradiciendo $A\cap C=\varnothing$. Por tanto $A$ es abierto. Las afirmaciones para el vacío y la recta siguen de sus definiciones de abierto y cerrado y de la inexistencia de sucesiones con términos en $\varnothing$. ∎

> **Precisión.** El criterio «todos los límites de sucesiones de $A$ siguen en $A$» define la *cerradura secuencial* de un conjunto en sentido de propiedad. Sin elección numerable no debe identificarse silenciosamente esa propiedad con ser cerrado en la topología construida mediante bolas.

### Teorema 15.8.9 — Formulaciones habituales bajo una hipótesis de elección explícita

Consideremos **exclusivamente como hipótesis de este teorema** el siguiente principio, denotado aquí por $\mathrm{CC}(\mathbb R)$:

> Para toda función $E:\mathbb N\to\mathcal P(\mathbb R)$ cuyos valores son no vacíos, existe una función $c:\mathbb N\to\mathbb R$ tal que $c(n)\in E(n)$ para todo $n$.

**Si se supone $\mathrm{CC}(\mathbb R)$**, entonces, para todo $A\subseteq\mathbb R$ y todo $x\in\mathbb R$, se obtienen las equivalencias generales

$$
\boxed{x\in\overline A\iff
\exists s\in\mathbb R^{\mathbb N}\
[\,\forall n\ (s_n\in A)\land s_n\to x\,],}
$$

$$
\boxed{x\in\operatorname{Acc}(A)\iff
\exists s\in\mathbb R^{\mathbb N}\
[\,\forall n\ (s_n\in A\setminus\{x\})\land s_n\to x\,],}
$$

$$
\boxed{x\in\partial A\iff
\exists s,t\in\mathbb R^{\mathbb N}\ [\,
\forall n\ (s_n\in A\land t_n\notin A),\ s_n\to x,\ t_n\to x\,].}
$$

También se obtiene $\operatorname{SCl}(A)=\overline A$; un conjunto es cerrado si y sólo si contiene los límites de todas sus sucesiones convergentes, y es abierto si y sólo si toda sucesión convergente a uno de sus puntos permanece eventualmente en él.

**Demostración condicional.**

Fijemos $A$ y $x\in\overline A$. Para cada $n$, el conjunto

$$
E_n:=A\cap B_{\eta_n}(x)
$$

existe por intersección de conjuntos y es no vacío por Teorema 15.8.2 — Pruebas de proximidad con radios numerables. Los valores determinan una función $E:\mathbb N\to\mathcal P(\mathbb R)$ mediante su fórmula y Separación. **Aquí, y sólo aquí, invocamos la hipótesis $\mathrm{CC}(\mathbb R)$**: obtenemos una función $s$ con $s_n\in E_n$ para todo $n$. Puesto que $|s_n-x|<\eta_n$ y $\eta_n\to0$, se tiene $s_n\to x$. La recíproca de adherencia ya es un teorema sin elección (Proposición 15.8.4 — Propiedades elementales de la clausura secuencial).

Para acumulación repetimos el argumento con $E_n=(A\setminus\{x\})\cap B_{\eta_n}(x)$; para frontera, lo aplicamos por separado a $A$ y a $\mathbb R\setminus A$, formando después un par finito de sucesiones. Los sentidos inversos están demostrados en Proposición 15.8.5 — Qué prueban las sucesiones convergentes sobre acumulación y frontera. La igualdad $\operatorname{SCl}(A)=\overline A$ sigue del primer criterio y de su definición. Para cerradura empleamos $A=\overline A$; para apertura, aplicamos el primer criterio al complemento de $A$ y la caracterización $A^\circ=\mathbb R\setminus\overline{\mathbb R\setminus A}$, reproduciendo el argumento eventual de Teorema 15.8.8 — Criterios secuenciales de cerradura y apertura: alcance exacto. ∎

**Estado fundacional.** Este teorema tiene la forma demostrada en ZF «$\mathrm{CC}(\mathbb R)\Rightarrow$ caracterizaciones secuenciales», y **no introduce $\mathrm{CC}(\mathbb R)$ como axioma**. Herrlich y Strecker demostraron incluso que la caracterización universal de adherencia mediante sucesiones es equivalente a dicho principio sobre conjuntos de reales. Por ello, promover sin hipótesis esa caracterización a teorema de nuestro sistema alteraría indebidamente el contrato fundacional. La referencia se registra como *countercheck* metamatemático, no como demostración importada en los resultados internos.

### Lema 15.8.10 — La recta real no admite una enumeración

No existe ninguna sobreyección $h:\mathbb N\to\mathbb R$. En particular, **no pueden existir simultáneamente**, para un mismo $A\subseteq\mathbb R$, sobreyecciones $e:\mathbb N\to A$ y $f:\mathbb N\to\mathbb R\setminus A$.

**Demostración.**

Supongamos dada una función $h:\mathbb N\to\mathbb R$. Construiremos, **sin escoger intervalos arbitrariamente**, una sucesión de intervalos cerrados no degenerados $J_n=[a_n,b_n]$ tal que

$$
J_0=[0,1],\qquad J_{n+1}\subseteq J_n,\qquad h(n)\notin J_{n+1}.
$$

Si ya está determinado $J_n=[a_n,b_n]$ con $a_n<b_n$, escribamos $d_n:=(b_n-a_n)/(1+1+1)>0$ y consideremos los intervalos cerrados

$$
L_n=[a_n,a_n+d_n],\qquad R_n=[b_n-d_n,b_n].
$$

Ambos son no vacíos, están contenidos en $J_n$ y son disjuntos: $a_n+d_n<b_n-d_n$, pues $b_n-a_n=(1+1+1)d_n$. Definimos mediante una regla unívoca

$$
J_{n+1}:=
\begin{cases}
R_n,&h(n)\in L_n,\\
L_n,&h(n)\notin L_n.
\end{cases}
$$

En el primer caso el nuevo intervalo evita $h(n)$ por disjunción; en el segundo lo evita por definición. Su longitud positiva es $d_n$. El teorema de recursión Teorema 1.3.7 — Teorema de recursión sobre $\mathbb N$, seguido de inducción, determina toda la sucesión con las propiedades indicadas. La distinción de pertenencia es clásica, pero la regla define **un único intervalo** en cada etapa; no utiliza elección.

El conjunto $S:=\{a_n:n\in\mathbb N\}$ existe como imagen de la sucesión de extremos izquierdos, es no vacío y está acotado superiormente por $b_0$. La propiedad del supremo proporciona $x:=\sup S\in\mathbb R$. Fijado $n$, tenemos $a_n\le x$. Además, cada $a_m\le b_n$: si $m\ge n$, por $J_m\subseteq J_n$; si $m<n$, por $a_m\le a_n\le b_n$. Así, $b_n$ es cota superior de $S$ y $x\le b_n$. Concluimos $x\in J_n$ para todo $n$.

Como $x\in J_{n+1}$ mientras que $h(n)\notin J_{n+1}$, se obtiene $x\ne h(n)$ para todo $n\in\mathbb N$. La función $h$ no es sobreyectiva. Puesto que era arbitraria, no existe una sobreyección de $\mathbb N$ sobre $\mathbb R$.

Finalmente, si se dispusiera de ambas sobreyecciones $e$ y $f$ del enunciado, la función dada por $g(2n)=e(n)$ y $g(2n+1)=f(n)$ estaría bien definida: los índices pares e impares son disjuntos y cubren $\mathbb N$, por la dicotomía de paridad Lema 3.9.3 — Dicotomía de paridad, y cada número par o impar posee su índice $n$ único por compatibilidad del orden con la multiplicación por dos. Así, la regla determina una función total con dominio $\mathbb N$. Cada real pertenece a $A$ o a su complemento y sería imagen de $g$, contradiciendo lo demostrado. ∎

> **Alcance del resultado.** No podemos caracterizar la frontera pidiendo enumeraciones completas y simultáneas de un conjunto y de su complemento: esa condición no tiene instancias en la recta. Para obtener un criterio aplicable bastará enumerar subconjuntos que sean densos dentro de cada uno de los dos lados.

### Teorema 15.8.11 — Caracterización fronteriza mediante dos lados densamente enumerados

Sea $A\subseteq\mathbb R$ y escribamos $C:=\mathbb R\setminus A$. Supongamos que están **dados** subconjuntos $D\subseteq A$ y $E\subseteq C$, junto con sobreyecciones $e:\mathbb N\to D$ y $f:\mathbb N\to E$, tales que

$$
A\subseteq\overline D,\qquad C\subseteq\overline E.
$$

Entonces, para cada $x\in\mathbb R$,

$$
\boxed{x\in\partial A\iff
\begin{gathered}
\exists s,t\in\mathbb R^{\mathbb N}\ \text{tales que}\\
\forall n\in\mathbb N\ (s_n\in A\land t_n\in C),\\
s_n\to x\quad\text{y}\quad t_n\to x.
\end{gathered}}
$$

**Demostración.**

Por $D\subseteq A$, la monotonía de clausura proporciona $\overline D\subseteq\overline A$. La inclusión contraria resulta de $A\subseteq\overline D$, la monotonía y la idempotencia: $\overline A\subseteq\overline{\overline D}=\overline D$. Por tanto $\overline A=\overline D$. El mismo argumento demuestra $\overline C=\overline E$.

Si $x\in\partial A$, la caracterización Teorema 15.6.3 — Caracterización de la frontera por dos clausuras proporciona $x\in\overline A\cap\overline C=\overline D\cap\overline E$. Aplicamos por separado Teorema 15.8.6 — Caracterizaciones completas para conjuntos enumerados al conjunto $D$ y a la sobreyección $e$, y luego al conjunto $E$ y a la sobreyección $f$. Obtenemos sucesiones $s_n\in D\subseteq A$ y $t_n\in E\subseteq C$ que convergen a $x$. Son dos aplicaciones ya determinadas por mínimos de índices naturales; no se escoge una familia adicional de aproximantes. La implicación inversa es exactamente Proposición 15.8.5 — Qué prueban las sucesiones convergentes sobre acumulación y frontera: las dos sucesiones ya existentes hacen que toda bola centrada en $x$ encuentre ambos lados. ∎

Las hipótesis **sí son realizables**. Por ejemplo, tomemos $A=\{0\}$ y $D=A$, enumerado por la sucesión constante. Para $C=\mathbb R\setminus\{0\}$, abreviemos localmente $j:=\jmath_{\mathbb Q}^{\mathbb R}$ y consideremos $E=j[\mathbb Q\setminus\{0_{\mathbb Q}\}]$. La enumeración racional canónica $e_{\mathbb Q}$ permite enumerar $E$ reemplazando por $1_{\mathbb Q}$ cada aparición de $0_{\mathbb Q}$ y aplicando después $j$. Todo intervalo abierto no vacío contiene una imagen racional distinta de cero: basta tomar dentro de él un subintervalo abierto no vacío que no contenga cero y aplicar Corolario 12.3.2 — Densidad racional en todo cuerpo ordenado completo. Así $\overline E=\mathbb R$ por la definición de adherencia, y las hipótesis se verifican. A diferencia de la doble enumeración de $A$ y **todo** su complemento, este caso no implica que la recta sea numerable.

La sección deja así una frontera deductiva precisa. Para un subconjunto arbitrario de $\mathbb R$, las definiciones con bolas y los criterios de radios numerables son **incondicionales en ZF**; los límites de sucesiones que ya existen aportan información topológica; los conjuntos enumerados y los abiertos poseen procedimientos canónicos adicionales; el criterio fronterizo tiene hipótesis realizables de densidad de ambos lados; las equivalencias para **todos** los subconjuntos requieren una hipótesis de elección que no hemos adoptado. Pasaremos a la densidad utilizando las definiciones originales de adherencia y las incrustaciones racionales ya construidas, sin apoyarnos en la recíproca secuencial condicional.
