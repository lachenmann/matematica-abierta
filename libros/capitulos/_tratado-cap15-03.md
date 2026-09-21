## 15.3. Puntos exteriores y conjuntos cerrados {#sec-ta-15-3}

En §15.2 describimos el interior de un conjunto: un punto es interior cuando podemos movernos ligeramente a su alrededor sin salir del conjunto. Ahora examinaremos la condición simétrica, pero debemos formularla con cuidado: estar **fuera** de $A$ no equivale necesariamente a poder permanecer fuera al efectuar cualquier desplazamiento suficientemente pequeño. La distinción conducirá a los puntos exteriores y, mediante el complemento, a los conjuntos cerrados.

### Definición 15.3.1 — Punto exterior de un conjunto
Sean $A\subseteq\mathbb R$ y $a\in\mathbb R$. Diremos que **$a$ es exterior a $A$** si existe un radio real estrictamente positivo tal que la bola centrada en $a$ no contiene ningún punto de $A$:

$$
\boxed{a\text{ es exterior a }A\iff
\exists r\in\mathbb R\ \bigl(r>0\ \text{y}\ B_r(a)\cap A=\varnothing\bigr).}
$$

Como $a\in B_r(a)$ para cada $r>0$ (Proposición §15.1.2 — Las bolas son intervalos abiertos centrados), la condición implica $a\notin A$. No vale la implicación inversa en general: de $a\notin A$ sólo conocemos la posición del centro, no la de los restantes puntos de una bola. Tampoco se define aquí un punto «de frontera» por exclusión: esa noción necesitará primero el estudio de los puntos adherentes.


### Definición 15.3.2 — Exterior de un conjunto
Definimos el **exterior** de $A\subseteq\mathbb R$ como el conjunto de sus puntos exteriores:

$$
\boxed{\operatorname{Ext}(A):=
\bigl\{x\in\mathbb R\setminus A:
\exists r\in\mathbb R\ (r>0\ \text{y}\ B_r(x)\cap A=\varnothing)\bigr\}.}
$$

La existencia se obtiene por Separación sobre $\mathbb R\setminus A$, que existe por Definición §0.2.11 — Diferencia conjuntista. Restringir la comprensión al complemento hace visible la condición de tipo $\operatorname{Ext}(A)\subseteq\mathbb R\setminus A$, aunque la definición anterior ya implica que todo punto exterior está fuera de $A$. Para cada $A$ este conjunto es único por extensionalidad; por Separación dentro de $\mathcal P(\mathbb R)\times\mathcal P(\mathbb R)$, la asignación $A\mapsto\operatorname{Ext}(A)$ determina asimismo una función total de $\mathcal P(\mathbb R)$ en sí mismo. No escogemos radios para construir dicha función.


### Proposición 15.3.3 — El exterior es el interior del complemento
Para todo $A\subseteq\mathbb R$ se cumple

$$
\boxed{\operatorname{Ext}(A)=(\mathbb R\setminus A)^\circ.}
$$

En particular, $\operatorname{Ext}(A)$ es abierto.

**Demostración.**
Fijemos $x\in\mathbb R$. Si $x\in\operatorname{Ext}(A)$, existe $r>0$ con $B_r(x)\cap A=\varnothing$. Para cada $y\in B_r(x)$, la pertenencia $y\in A$ contradiría esa intersección vacía; por tanto $y\in\mathbb R\setminus A$. Así $B_r(x)\subseteq\mathbb R\setminus A$ y, puesto que $x$ pertenece a su propia bola, $x\in(\mathbb R\setminus A)^\circ$.

Recíprocamente, si $x\in(\mathbb R\setminus A)^\circ$, algún $r>0$ satisface $B_r(x)\subseteq\mathbb R\setminus A$. Ningún elemento de la bola pertenece a $A$, de modo que $B_r(x)\cap A=\varnothing$; en particular $x$ es exterior a $A$ y pertenece a $\operatorname{Ext}(A)$. Las dos inclusiones prueban la igualdad. Finalmente, Teorema §15.2.8 — El interior es el mayor abierto contenido en el conjunto garantiza que el interior de cualquier subconjunto de $\mathbb R$ es abierto. Aplicándolo al complemento, obtenemos que $\operatorname{Ext}(A)$ es abierto. ∎

> **Interpretación.** El exterior no necesita una teoría distinta del interior: es el interior obtenido después de tomar el complemento. Este hecho no autoriza a identificarlo con todo el complemento; los puntos que estén fuera pero no posean una bola enteramente exterior quedarán fuera de $\operatorname{Ext}(A)$.


### Proposición 15.3.4 — Separación y antitonicidad del exterior
Para $A,C\subseteq\mathbb R$ se cumplen:

1. $\operatorname{Ext}(A)\cap A=\varnothing$ y, en consecuencia, $\operatorname{Ext}(A)\cap A^\circ=\varnothing$.
2. Si $A\subseteq C$, entonces $\operatorname{Ext}(C)\subseteq\operatorname{Ext}(A)$.

**Demostración.**
Por definición, $\operatorname{Ext}(A)\subseteq\mathbb R\setminus A$: ningún elemento suyo pertenece a $A$, de donde la primera intersección es vacía. Puesto que $A^\circ\subseteq A$ por Proposición §15.2.3 — Interior y vecindades, también es vacía la intersección con el interior.

Supongamos $A\subseteq C$ y fijemos $x\in\operatorname{Ext}(C)$. Existe $r>0$ tal que $B_r(x)\cap C=\varnothing$. Si algún $y$ perteneciera a $B_r(x)\cap A$, de $A\subseteq C$ deduciríamos $y\in B_r(x)\cap C$, contradicción. Luego $B_r(x)\cap A=\varnothing$ y $x\in\operatorname{Ext}(A)$. Esto demuestra la segunda inclusión. ∎

La inclusión se invierte: **a mayor conjunto, menor exterior**. No se afirma que cada punto de la recta sea necesariamente interior o exterior; una tercera posibilidad será estudiada después.


### Definición 15.3.5 — Conjunto cerrado de la recta
Un conjunto $F\subseteq\mathbb R$ se denomina **cerrado (en $\mathbb R$)** cuando su complemento en la recta es abierto:

$$
\boxed{F\text{ es cerrado}\iff\mathbb R\setminus F\text{ es abierto}.}
$$

La palabra «cerrado» no significa «no abierto». La definición afirma una propiedad positiva del **complemento**: cada punto exterior a $F$ en el sentido conjuntista deberá disponer de un margen completo fuera de $F$. El ambiente es siempre $\mathbb R$ y no se presupone ninguna noción de cerrado relativo a un subespacio.


### Proposición 15.3.6 — Criterio de cerradura mediante puntos exteriores
Para cualquier $F\subseteq\mathbb R$ son equivalentes las afirmaciones siguientes:

1. $F$ es cerrado.
2. $\operatorname{Ext}(F)=\mathbb R\setminus F$.
3. Para cada $x\in\mathbb R\setminus F$ existe $r>0$ tal que $B_r(x)\cap F=\varnothing$.

**Demostración.**
Por Proposición §15.3.3 — El exterior es el interior del complemento, $\operatorname{Ext}(F)=(\mathbb R\setminus F)^\circ$. El criterio de abiertos Proposición §15.2.6 — Caracterización de los abiertos mediante el interior, aplicado al conjunto $\mathbb R\setminus F$, afirma que este complemento es abierto si y sólo si coincide con su interior. Por la definición de cerrado, esto demuestra la equivalencia entre (1) y (2).

Si vale (2) y $x\in\mathbb R\setminus F$, entonces $x\in\operatorname{Ext}(F)$; la definición de punto exterior proporciona el radio requerido en (3). Si vale (3), cada punto del complemento pertenece al exterior. Por ello $\mathbb R\setminus F\subseteq\operatorname{Ext}(F)$; la inclusión inversa forma parte de Definición §15.3.2 — Exterior de un conjunto. La doble inclusión da (2). ∎

> **Lectura de cuantificadores.** Para que un conjunto sea cerrado se exige un radio para *cada punto de su complemento*. El radio puede variar con el punto; no afirmamos la existencia de un radio uniforme ni de una función que seleccione simultáneamente todos esos radios.


### Teorema 15.3.7 — Leyes fundamentales de los conjuntos cerrados
Se cumplen las siguientes propiedades:

1. $\varnothing$ y $\mathbb R$ son cerrados.
2. Si $I$ es un conjunto cualquiera y $(F_i)_{i\in I}$ es una familia de cerrados de la recta, su intersección $\bigcap_{i\in I}F_i$ es cerrada, incluido el caso $I=\varnothing$, cuya intersección relativa a $\mathbb R$ es $\mathbb R$.
3. Si $F,G\subseteq\mathbb R$ son cerrados, $F\cup G$ es cerrado. En consecuencia, toda unión **finita** de cerrados es cerrada, incluida la unión vacía.

**Demostración.**
**(1)** Por Teorema §15.2.7 — Leyes fundamentales de los conjuntos abiertos, tanto $\mathbb R$ como $\varnothing$ son abiertos. Sus complementos en $\mathbb R$ son, respectivamente, $\varnothing$ y $\mathbb R$; por la definición de cerrado, ambos son cerrados.

**(2)** La intersección indexada existe con ambiente $\mathbb R$ por Definición §0.6.16 — Familia indexada. Denotémosla localmente por $F$. Si $I=\varnothing$, entonces $F=\mathbb R$ y se aplica (1). Supongamos $I\ne\varnothing$ y tomemos $x\in\mathbb R\setminus F$. La pertenencia a $F$ significa $\forall i\in I,\ x\in F_i$; su negación, por la lógica clásica del contrato fundacional, da un índice $i\in I$ con $x\notin F_i$. Como $F_i$ es cerrado, Proposición §15.3.6 — Criterio de cerradura mediante puntos exteriores proporciona $r>0$ con $B_r(x)\cap F_i=\varnothing$. Dado que $F\subseteq F_i$, también $B_r(x)\cap F=\varnothing$. Cada punto del complemento posee tal radio; el mismo criterio prueba que $F$ es cerrado. El índice y el radio se obtienen **para el punto fijado**, sin construir una función de elección sobre $I$.

**(3)** Sea $x\in\mathbb R\setminus(F\cup G)$. Entonces $x\notin F$ y $x\notin G$. Como ambos son cerrados, encontramos radios $r,s>0$ con $B_r(x)\cap F=\varnothing$ y $B_s(x)\cap G=\varnothing$. Tomemos $t=\min\{r,s\}>0$. Por la inclusión entre bolas concéntricas de Proposición §15.1.2 — Las bolas son intervalos abiertos centrados,

$$
B_t(x)\subseteq B_r(x)\cap B_s(x).
$$

Así $B_t(x)$ no contiene puntos de $F$ ni de $G$, por lo que $B_t(x)\cap(F\cup G)=\varnothing$. El criterio de Proposición §15.3.6 — Criterio de cerradura mediante puntos exteriores prueba que $F\cup G$ es cerrado. La unión de cero cerrados es $\varnothing$, cerrada por (1); por inducción sobre el número natural de miembros, el caso binario extiende el resultado a toda unión finita. ∎

Las reglas son duales a las de los abiertos, pero no idénticas: los cerrados admiten **intersecciones arbitrarias y uniones finitas**. El calificativo «finita» no puede eliminarse de la segunda operación en general; demostraremos un contraejemplo explícito antes de terminar la sección.


### Proposición 15.3.8 — Las dos semirrectas estrictas son abiertas
Para cada $c\in\mathbb R$, los conjuntos

$$
L_c:=\{x\in\mathbb R:x<c\},\qquad
R_c:=\{x\in\mathbb R:c<x\}
$$

son abiertos en $\mathbb R$. Las letras $L_c,R_c$ son abreviaturas **locales** para conjuntos existentes por Separación; no incorporamos símbolos de infinito ni suponemos una definición previa de intervalos no acotados.

**Demostración.**
Sea $x\in L_c$, de manera que $x<c$. Definamos $r=c-x>0$. Para cualquier $y\in B_r(x)$, la identidad bola–intervalo de Proposición §15.1.2 — Las bolas son intervalos abiertos centrados da $y<x+r=c$; por tanto $y\in L_c$ y $B_r(x)\subseteq L_c$. Como $x$ es arbitrario, $L_c$ es abierto.

Análogamente, si $x\in R_c$, el radio $s=x-c>0$ cumple que todo $y\in B_s(x)$ satisface $y>x-s=c$. Luego $B_s(x)\subseteq R_c$, y $R_c$ también es abierto. ∎


### Corolario 15.3.9 — Los intervalos cerrados y los singletons son cerrados
Si $a,b\in\mathbb R$ y $a\le b$, el intervalo $[a,b]$ es cerrado. Para cualquier $a\in\mathbb R$, el singleton $\{a\}$ es cerrado, aunque no es abierto. Los conjuntos $\varnothing$ y $\mathbb R$ son simultáneamente abiertos y cerrados.

**Demostración.**
Con la notación local de Proposición §15.3.8 — Las dos semirrectas estrictas son abiertas tenemos, por orden total y por la definición de intervalo acotado,

$$
\mathbb R\setminus[a,b]=L_a\cup R_b.
$$

En efecto, un real está fuera de $[a,b]$ precisamente cuando es menor que $a$ o mayor que $b$. Ambos conjuntos de la derecha son abiertos; su unión es abierta por Teorema §15.2.7 — Leyes fundamentales de los conjuntos abiertos. El complemento de $[a,b]$ es, pues, abierto, y $[a,b]$ es cerrado.

De modo idéntico, $\mathbb R\setminus\{a\}=L_a\cup R_a$, abierto, luego $\{a\}$ es cerrado. Su falta de apertura ya fue demostrada en Proposición §15.2.9 — Ejemplos: intervalos abiertos y singletons. Por último, $\varnothing$ y $\mathbb R$ son abiertos por Teorema §15.2.7 — Leyes fundamentales de los conjuntos abiertos y cerrados por Teorema §15.3.7 — Leyes fundamentales de los conjuntos cerrados. ∎

> **Advertencia terminológica.** No hay contradicción en que un conjunto sea abierto y cerrado a la vez. Tampoco hay contradicción en que no sea ninguno de los dos: las definiciones se aplican independientemente al conjunto y a su complemento.


### Proposición 15.3.10 — Un conjunto que no es ni abierto ni cerrado
Sean $a,b\in\mathbb R$ con $a<b$, y definamos por Separación el conjunto

$$
H:=\{x\in\mathbb R:a\le x<b\}.
$$

Entonces $H$ no es abierto **ni** cerrado en $\mathbb R$.

**Demostración.**
Como $a<b$, tenemos $a\in H$. Sea $r>0$ arbitrario. El punto $y=a-r/(1+1)$ satisface $y<a$ y $|y-a|=r/(1+1)<r$: pertenece a $B_r(a)$ pero no a $H$. Ninguna bola de radio positivo centrada en $a$ queda contenida en $H$; por la definición de abierto, $H$ no es abierto.

Para negar la cerradura observemos que $b\notin H$. Fijemos cualquier $r>0$ y pongamos

$$
t:=\min\left\{\frac{r}{1+1},\frac{b-a}{1+1}\right\}>0,
\qquad z:=b-t.
$$

Como $0<t\le(b-a)/(1+1)<b-a$, resulta $a<z<b$, y por tanto $z\in H$. Además, $t\le r/(1+1)<r$ y $|z-b|=t$, de modo que $z\in B_r(b)$. Así, **toda** bola centrada en $b$ intersecta $H$, aunque $b\notin H$. Por Proposición §15.3.6 — Criterio de cerradura mediante puntos exteriores, $H$ no es cerrado. ∎

No hemos recurrido a la noción aún no definida de «punto adherente»: basta negar directamente la condición cuantificada de punto exterior. El ejemplo distingue rigurosamente «no abierto» de «cerrado».


### Proposición 15.3.11 — Las restricciones de finitud son necesarias
Existen una familia de abiertos cuya intersección no es abierta y una familia de cerrados cuya unión no es cerrada. En ambos casos las familias están **explícitamente determinadas**, sin ninguna selección de representantes o radios.

**Demostración.**
Fijemos $a\in\mathbb R$ y consideremos el conjunto de radios positivos

$$
I:=\{r\in\mathbb R:r>0\}.
$$

Existe por Separación y es no vacío, pues $1\in I$. La asignación $r\mapsto B_r(a)$ determina una función $I\to\mathcal P(\mathbb R)$: su grafo se obtiene por Separación dentro de $I\times\mathcal P(\mathbb R)$, y para cada $r\in I$ la bola ya existe y es única. Todos sus valores son abiertos por Teorema §15.2.5 — Toda bola abierta es un conjunto abierto.

Afirmamos que

$$
\boxed{\bigcap_{r\in I}B_r(a)=\{a\}.}
$$

En efecto, $a\in B_r(a)$ para cada $r>0$, luego pertenece a la intersección. Si $x\ne a$, entonces $r:=|x-a|>0$ por las propiedades del valor absoluto. Este $r$ pertenece a $I$, pero $x\notin B_r(a)$: la desigualdad definitoria $|x-a|<r=|x-a|$ es falsa. Por ello ningún $x\ne a$ está en la intersección. La igualdad sigue por extensionalidad. Como $\{a\}$ no es abierto (Proposición §15.2.9 — Ejemplos: intervalos abiertos y singletons), acabamos de exhibir una intersección arbitraria de abiertos que no es abierta.

Definamos ahora, para cada $r\in I$, $F_r:=\mathbb R\setminus B_r(a)$. Son cerrados por definición y, de nuevo, la familia está determinada por un grafo único obtenido por Separación, sin Choice. Para $x\in\mathbb R$, las leyes de pertenencia y la equivalencia elemental de De Morgan dan

$$
\begin{aligned}
x\in\bigcup_{r\in I}F_r
&\iff \exists r\in I\ \bigl(x\notin B_r(a)\bigr)\\
&\iff x\notin\bigcap_{r\in I}B_r(a)\\
&\iff x\in\mathbb R\setminus\{a\}.
\end{aligned}
$$

Así $\bigcup_{r\in I}F_r=\mathbb R\setminus\{a\}$. Esta unión **no es cerrada**: si lo fuese, su complemento $\{a\}$ sería abierto por Definición §15.3.5 — Conjunto cerrado de la recta, contra Proposición §15.2.9 — Ejemplos: intervalos abiertos y singletons. Quedan probados ambos contraejemplos. ∎

> **Balance conceptual.** La dualidad entre abiertos y cerrados fija exactamente la forma de sus leyes: uniones arbitrarias e intersecciones finitas para abiertos; intersecciones arbitrarias y uniones finitas para cerrados. Ni la palabra «abierto» ni la palabra «cerrado» se deducen de incluir o excluir individualmente un punto.

El siguiente paso consistirá en estudiar los puntos cuya **toda** vecindad encuentra al conjunto. Esa condición —distinta de ser interior o exterior— permitirá introducir la adherencia y construir la clausura sin circularidad en §15.4.
