## 18.7. Conexidad de los subconjuntos de la recta {#sec-ta-18-7}

La compacidad controla cubiertas y produce consecuencias cuantitativas; la conexidad responde a una pregunta de otra índole. Un subconjunto $E$ de la recta es conexo cuando no puede repartirse en dos partes no vacías que sean **abiertas dentro del propio $E$**. La precisión «dentro de» es indispensable: por ejemplo, un intervalo cerrado no es abierto en la recta, pero puede contener subconjuntos relativamente abiertos. Primero fijaremos la separación relativa y su expresión mediante conjuntos simultáneamente abiertos y cerrados; después probaremos, sin utilizar el teorema del valor intermedio, que la conexidad equivale exactamente a no omitir ningún punto situado entre dos puntos del conjunto.

### Definición 18.7.1 — Separación relativa y conjunto conexo
Sea $E\subseteq\mathbb R$. Una **separación de $E$** es un par de subconjuntos $A,B\subseteq E$ tal que:

$$
\boxed{\begin{gathered}
A\ne\varnothing,\quad B\ne\varnothing,\quad
A\cap B=\varnothing,\quad E=A\cup B,\\
A\text{ y }B\text{ son abiertos relativos a }E.
\end{gathered}}
$$

Diremos que $E$ es **conexo** si no existe ninguna separación de $E$. Formalmente, negamos la existencia de dos miembros de $\mathcal P(E)$ que satisfagan simultáneamente las condiciones escritas. No se introduce una topología abstracta: «abierto relativo» conserva exactamente el significado de §17.3.1. En particular, las partes de una separación no tienen por qué ser abiertas en toda $\mathbb R$. El vacío se considera conexo, pues no admite dos partes no vacías; también lo será cualquier singleton, como se comprobará mediante el criterio siguiente.

### Proposición 18.7.2 — Criterio mediante subconjuntos abiertos y cerrados relativos
Para $E\subseteq\mathbb R$ son equivalentes:

1. $E$ es conexo.
2. Si $A\subseteq E$ es a la vez abierto y cerrado relativo a $E$, entonces $A=\varnothing$ o $A=E$.

**Demostración.**
Supongamos que $E$ es conexo y que $A\subseteq E$ es abierto y cerrado relativo a $E$. Pongamos $B:=E\setminus A$, conjunto existente por Separación. Como $A$ es cerrado relativo, $B$ es abierto relativo por definición; además $A\cup B=E$ y $A\cap B=\varnothing$. Si $A$ fuese distinto tanto de $\varnothing$ como de $E$, ambos $A$ y $B$ serían no vacíos, y formarían una separación, contradicción. Por tanto, $A=\varnothing$ o $A=E$.

Recíprocamente, supongamos que los únicos subconjuntos simultáneamente abiertos y cerrados relativos a $E$ son $\varnothing$ y $E$. Si existiese una separación $E=A\cup B$, su disjunción y su cobertura darían $B=E\setminus A$. La apertura relativa de $A$ y de $B$ implicaría, por la definición de cerrado relativo, que $A$ es también cerrado relativo. Pero la separación exige $A\ne\varnothing$ y $B\ne\varnothing$, de donde $A\ne E$: contradicción. Así, $E$ es conexo. $\square$

**Casos límite.** Si $E=\varnothing$, su único subconjunto es el vacío. Si $E=\{a\}$, sus únicos subconjuntos son $\varnothing$ y $E$. El criterio demuestra la conexidad de ambos sin declarar que un singleton sea abierto en la recta.

### Definición 18.7.3 — Intervalo como subconjunto convexo para el orden
Un conjunto $E\subseteq\mathbb R$ se denomina **intervalo** cuando, dados dos puntos cualesquiera $a,b\in E$ con $a\le b$, contiene todo el segmento comprendido entre ellos:

$$
\boxed{E\text{ es intervalo}\iff
\forall a,b\in E\;(a\le b\Longrightarrow[a,b]\subseteq E).}
$$

La notación $[a,b]$ conserva la definición de §4.3.1. Equivalentemente, para cualesquiera $a,b\in E$ con $a<b$ y cualquier $t\in\mathbb R$ tal que $a<t<b$, debe cumplirse $t\in E$: los extremos ya pertenecen a $E$ por hipótesis. No se impone que un intervalo sea abierto, cerrado, acotado o no vacío. El vacío y los singletons satisfacen esta definición; también $\mathbb R$, los intervalos acotados con cualquier modalidad de extremos y las semirrectas determinadas por desigualdades. Aquí «intervalo» es un **predicado sobre conjuntos**, no una nueva codificación conjuntista ni un símbolo para el infinito.

### Teorema 18.7.4 — Todo intervalo de la recta es conexo
Si $E\subseteq\mathbb R$ es un intervalo, entonces $E$ es conexo. Se incluyen $E=\varnothing$, los singletons, los intervalos no acotados y todos los casos de extremos abiertos, cerrados o semiabiertos.

**Demostración.**
**1. Supongamos que existe una separación.** Razonemos por contradicción. Sean $A,B$ subconjuntos no vacíos, disjuntos, abiertos relativos a $E$, con $E=A\cup B$. Fijemos un punto de $A$ y uno de $B$. Son distintos; por totalidad del orden, intercambiando **los nombres de las dos partes** si es necesario, podemos fijar

$$
a\in A,\qquad b\in B,\qquad a<b.
$$

Ésta es una decisión sobre dos testigos concretos, no una función de elección. Como $E$ es intervalo, $[a,b]\subseteq E$.

**2. La frontera dada por un supremo.** Formemos, por Separación dentro del segmento existente,

$$
S:=A\cap[a,b].
$$

Tenemos $a\in S$, luego $S\ne\varnothing$; asimismo $b$ es cota superior de $S$. La propiedad del supremo de $\mathbb R$ suministra un real único

$$
c:=\sup S,\qquad a\le c\le b.
$$

Así $c\in[a,b]\subseteq E$, de modo que exactamente una de las posibilidades $c\in A$ y $c\in B$ es verdadera.

**3. Si $c\in A$, se puede avanzar más allá del supremo.** Como $b\in B$ y las partes son disjuntas, $c\ne b$, luego $c<b$. La apertura relativa de $A$ y el criterio por bolas de §17.3.2 proporcionan un único radio testigo $r>0$ tal que

$$
E\cap B_r(c)\subseteq A.
$$

Definamos, comparando solamente dos números,

$$
d:=\min\{b,c+r/2\}.
$$

De $c<b$ y $r>0$ resulta $c<d\le b$, mientras que $d-c\le r/2<r$. Por ello $d\in[a,b]\subseteq E$ y $d\in B_r(c)$; la apertura relativa da $d\in A$. Se deduce $d\in S$ y $d>c$, contradiciendo que $c$ sea cota superior de $S$.

**4. Si $c\in B$, encontramos un punto de $A$ demasiado próximo.** La apertura relativa de $B$ proporciona, para este punto concreto $c$, un radio $s>0$ tal que

$$
E\cap B_s(c)\subseteq B.
$$

El número $c-s/2<c$ no puede ser cota superior de $S$, pues $c$ es la menor de ellas. En consecuencia existe **un** $t\in S$ con

$$
c-s/2<t\le c.
$$

Como $t\in S\subseteq A$ y $c\in B$, tenemos $t\ne c$; entonces $|t-c|=c-t<s/2<s$. Así $t\in E\cap B_s(c)\subseteq B$, incompatible con $t\in A$.

Los dos casos posibles para $c\in E=A\cup B$ conducen a contradicción. No existe separación y $E$ es conexo. Si $E$ es vacío o singleton, ni siquiera puede iniciarse el paso 1, pues no existen las dos partes no vacías y disjuntas requeridas. $\square$

**Lectura conceptual.** El supremo localiza la presunta frontera entre las dos partes. Si pertenece a la parte de la izquierda, la apertura permite avanzar; si pertenece a la otra, la propiedad aproximante del supremo fuerza un punto de la izquierda a entrar en su vecindad. La demostración no utiliza el teorema del valor intermedio ni construye sucesiones seleccionando puntos cercanos a la frontera.

### Teorema 18.7.5 — Todo conexo de la recta es un intervalo
Si $E\subseteq\mathbb R$ es conexo, entonces para cualesquiera $a,b\in E$ con $a<b$ se cumple $[a,b]\subseteq E$. Por tanto, $E$ es un intervalo.

**Demostración.**
Demostremos la contraposición. Si $E$ no es intervalo, la negación de Definición §18.7.3 — Intervalo como subconjunto convexo para el orden proporciona $a,b\in E$ con $a\le b$ y un $c\in[a,b]$ que no pertenece a $E$. Como $a,b\in E$, necesariamente

$$
a<c<b,\qquad c\notin E.
$$

Fijado ese único punto omitido, consideremos los conjuntos existentes por Separación

$$
L_c:=\{x\in\mathbb R:x<c\},\qquad
R_c:=\{x\in\mathbb R:c<x\},
$$

abiertos en $\mathbb R$ por Proposición §15.3.8 — Las dos semirrectas estrictas son abiertas. Definamos

$$
A:=E\cap L_c,\qquad B:=E\cap R_c.
$$

Son abiertos **relativos a $E$** por Definición §17.3.1 — Abiertos y cerrados relativos a un subconjunto de la recta; ambos son no vacíos, pues $a\in A$ y $b\in B$. Son disjuntos por incompatibilidad de $x<c$ y $c<x$. Finalmente, para cualquier $x\in E$ se tiene $x\ne c$, porque $c\notin E$, y la tricotomía del orden asegura $x<c$ o $c<x$. Por consiguiente, $E=A\cup B$. Hemos construido explícitamente una separación de $E$, que no es conexo. Por contraposición, todo conexo es intervalo. No se han escogido abiertos o testigos para una familia de cortes: una sola omisión de un punto intermedio determina las dos partes por fórmulas únicas. $\square$

### Corolario 18.7.6 — Caracterización exacta de los conexos reales
Para todo $E\subseteq\mathbb R$,

$$
\boxed{E\text{ es conexo}\quad\Longleftrightarrow\quad
E\text{ es intervalo}\quad\Longleftrightarrow\quad
\forall a,b\in E\;(a\le b\Rightarrow[a,b]\subseteq E).}
$$

**Demostración.**
La primera implicación es el Teorema 18.7.5; la recíproca es el Teorema 18.7.4. La segunda equivalencia es exactamente la definición de intervalo, incluidos los casos vacíos. $\square$

**Ejemplos y no-ejemplos.** Son conexos $\varnothing$, los singletons, $\mathbb R$ y cada intervalo abierto, cerrado, semiabierto o no acotado, porque contienen todos los puntos situados entre dos de sus elementos. El conjunto $\{a,b\}$ con $a<b$ no es conexo: su punto medio $(a+b)/2$ está estrictamente entre ambos y no pertenece al conjunto. Tampoco es conexo $\mathbb R\setminus\{c\}$: contiene $c-1$ y $c+1$ pero omite el punto intermedio $c$. Estos ejemplos no requieren invocar continuidad.

### Proposición 18.7.7 — Unión de dos conexos con intersección no vacía
Sean $E,F\subseteq\mathbb R$ conexos y supongamos $E\cap F\ne\varnothing$. Entonces $E\cup F$ es conexo. En particular, la unión de dos intervalos reales que tengan un punto común es también un intervalo.

**Demostración.**
Pongamos $H:=E\cup F$ y fijemos un único $p\in E\cap F$. Si $H$ no fuera conexo, existiría una separación $H=A\cup B$ con $A,B\ne\varnothing$, abiertos relativos a $H$ y disjuntos. Las intersecciones $E\cap A$ y $E\cap B$ son abiertas relativas a $E$: en efecto, si $A=H\cap U$ con $U$ abierto en la recta, entonces $E\cap A=E\cap U$ porque $E\subseteq H$, y análogamente para $B$. Son disjuntas y su unión es $E$. Dado que $E$ es conexo, no pueden ser ambas no vacías. Lo mismo se verifica con $F\cap A$ y $F\cap B$.

Como $p\in H=A\cup B$ y $A\cap B=\varnothing$, exactamente una de las dos partes contiene $p$. Supongamos $p\in A$; el caso $p\in B$ es simétrico. Entonces $E\cap A$ y $F\cap A$ son no vacíos. Por la conexidad de $E$ y de $F$, necesariamente $E\cap B=F\cap B=\varnothing$. Se sigue

$$
B=H\cap B=(E\cap B)\cup(F\cap B)=\varnothing,
$$

contra la definición de separación. Por tanto $H$ es conexo. Si $E$ y $F$ eran intervalos, son conexos por el Teorema 18.7.4; su unión es conexa y, por el Teorema 18.7.5, vuelve a ser intervalo. Ningún paso exige elección para una familia de componentes. $\square$

**Transición.** Ya sabemos que la imposibilidad de separar un conjunto real es equivalente a que no tenga huecos entre sus puntos. En §18.8 estudiaremos cómo transporta esta propiedad una función continua. Sólo **después**, en §18.9, deduciremos el teorema del valor intermedio como consecuencia, no como premisa de las pruebas actuales.
