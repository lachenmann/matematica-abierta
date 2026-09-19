## 15.4. Puntos adherentes y clausura {#sec-ta-15-4}

En §15.3 vimos que un punto exterior a $A$ dispone de una bola completamente separada de $A$. Negar esta condición conduce a una relación de proximidad que no exige pertenecer al conjunto: **ninguna bola centrada en el punto puede evitar $A$**. Esta será la noción de adherencia. Primero construiremos el conjunto de todos esos puntos; sólo después probaremos su relación con los cerrados. La noción de punto de acumulación, que impone además una condición sobre puntos *distintos* del centro, queda reservada para la sección siguiente.

### Definición 15.4.1 — Punto adherente de un conjunto

Sean $A\subseteq\mathbb R$ y $x\in\mathbb R$. Diremos que **$x$ es adherente a $A$** cuando toda bola abierta de radio positivo centrada en $x$ contiene al menos un punto de $A$:

$$
\boxed{x\text{ es adherente a }A\iff
\forall r\in\mathbb R\;\bigl(r>0\implies B_r(x)\cap A\ne\varnothing\bigr).}
$$

La negación de «la intersección es vacía» equivale a que existe algún $y\in A$ con $|y-x|<r$. El testigo $y$ puede depender de $r$; **no se afirma que exista un punto de $A$ que sirva simultáneamente para todos los radios**. Tampoco exigimos $y\ne x$: cuando $x\in A$, el propio centro proporcionará un testigo para cada bola. La condición distinta $y\ne x$ se estudiará al definir la acumulación, no aquí.

> **Pregunta de lectura.** ¿Puede un punto adherente quedar fuera de $A$? Sí: el extremo $b$ del conjunto $H=\{x\in\mathbb R:a\le x<b\}$ de §15.3 no pertenece a $H$, pero la prueba de Proposición 15.3.10 — Un conjunto que no es ni abierto ni cerrado exhibe un elemento de $B_r(b)\cap H$ para cada $r>0$.

### Definición 15.4.2 — Clausura de un conjunto

Para $A\subseteq\mathbb R$, definimos su **clausura** como el conjunto de todos los puntos adherentes a $A$:

$$
\boxed{\overline A:=\{x\in\mathbb R:
\forall r\in\mathbb R\;(r>0\implies B_r(x)\cap A\ne\varnothing)\}.}
$$

El conjunto existe por Separación sobre $\mathbb R$: no estamos intentando reunir puntos sin un conjunto ambiente. La extensionalidad asegura su unicidad. En particular, la asignación $A\mapsto\overline A$ define una operación total $\mathcal P(\mathbb R)\to\mathcal P(\mathbb R)$: su grafo se obtiene por Separación dentro de $\mathcal P(\mathbb R)\times\mathcal P(\mathbb R)$, utilizando la fórmula anterior, y cada argumento tiene una única imagen. No se construye una función de elección de puntos de las intersecciones, porque la definición sólo cuantifica su existencia **por cada radio**.

La barra superior se aplica a **subconjuntos de $\mathbb R$**; no se confunde con la barra de una función inducida en un cociente ni se interpreta como límite de una sucesión. «Clausura» nombra inicialmente este conjunto definido por bolas: todavía falta demostrar que es cerrado.

### Proposición 15.4.3 — La adherencia es la negación de la exterioridad

Para todo $A\subseteq\mathbb R$ y todo $x\in\mathbb R$,

$$
\boxed{x\in\overline A\iff x\notin\operatorname{Ext}(A).}
$$

En consecuencia,

$$
\boxed{\overline A=\mathbb R\setminus\operatorname{Ext}(A),
\qquad\mathbb R\setminus\overline A=\operatorname{Ext}(A).}
$$

**Demostración.**

Por la definición de clausura, $x\in\overline A$ significa que, para **todo** $r>0$, la intersección $B_r(x)\cap A$ es no vacía. En cambio, ser exterior significa que **existe** $r>0$ para el cual esa intersección es vacía. Estas dos afirmaciones son negaciones lógicas una de otra: si todas las intersecciones son no vacías, no existe el radio exterior; y, recíprocamente, si no existe tal radio, la lógica clásica permite concluir que cada intersección es no vacía. La condición adicional $x\in\mathbb R\setminus A$ en la definición conjuntista de $\operatorname{Ext}(A)$ es redundante gracias a Definición 15.3.1 — Punto exterior de un conjunto y a que $x\in B_r(x)$ para $r>0$.

Hemos probado la equivalencia para un $x\in\mathbb R$ arbitrario. Por extensionalidad, los puntos de $\overline A$ son exactamente los del complemento de $\operatorname{Ext}(A)$ dentro de $\mathbb R$. Al tomar de nuevo complementos relativos a $\mathbb R$ obtenemos la segunda identidad. ∎

La equivalencia también muestra que interioridad, exterioridad y adherencia responden a preguntas diferentes. El punto $x$ es interior si **una** bola está contenida en $A$; es exterior si **una** bola evita $A$; es adherente si **ninguna** bola evita $A$.

### Proposición 15.4.4 — Extensividad y monotonía de la clausura

Para cualesquiera $A,B\subseteq\mathbb R$ se cumplen:

$$
\boxed{A\subseteq\overline A,}
$$

$$
\boxed{A\subseteq B\implies\overline A\subseteq\overline B.}
$$

**Demostración.**

Para la primera inclusión fijemos $x\in A$ y un radio arbitrario $r>0$. La proposición Proposición 15.1.2 — Las bolas son intervalos abiertos centrados afirma que $x\in B_r(x)$. Como también $x\in A$, tenemos $x\in B_r(x)\cap A$, de modo que esa intersección no es vacía. Esto vale para cada $r>0$, luego $x\in\overline A$. No fue necesario seleccionar testigos: **el mismo $x$ sirve para todos los radios**.

Para la monotonía, supongamos $A\subseteq B$ y fijemos $x\in\overline A$. Sea $r>0$ cualquiera. Por adherencia, existe un punto $y\in B_r(x)\cap A$. La inclusión $A\subseteq B$ implica $y\in B_r(x)\cap B$. Por tanto, toda bola centrada en $x$ intersecta $B$ y $x\in\overline B$. El punto y el radio eran arbitrarios, así que $\overline A\subseteq\overline B$. ∎

> **Interpretación.** La clausura no descarta puntos del conjunto inicial. Además, al añadir elementos a $A$ no se pierden puntos adherentes; la operación respeta la inclusión.

### Teorema 15.4.5 — La clausura es un conjunto cerrado

Para todo $A\subseteq\mathbb R$, el conjunto $\overline A$ es cerrado.

**Demostración.**

La proposición anterior Proposición 15.4.3 — La adherencia es la negación de la exterioridad estableció la identidad

$$
\mathbb R\setminus\overline A=\operatorname{Ext}(A).
$$

Por Proposición 15.3.3 — El exterior es el interior del complemento, el exterior de cualquier conjunto es abierto. En consecuencia, el complemento de $\overline A$ es abierto. La definición Definición 15.3.5 — Conjunto cerrado de la recta de conjunto cerrado, aplicada **después** de haber construido la clausura, demuestra que $\overline A$ es cerrado. ∎

No hemos definido la clausura como «el cerrado más pequeño»: esta propiedad aparecerá ahora como un teorema y no como una petición circular de existencia.

### Teorema 15.4.6 — La clausura es el menor cerrado que contiene al conjunto

Sea $A\subseteq\mathbb R$. La clausura $\overline A$ es cerrada, contiene a $A$ y, para todo $F\subseteq\mathbb R$ cerrado,

$$
\boxed{A\subseteq F\implies\overline A\subseteq F.}
$$

Equivalentemente, si definimos

$$
\mathcal F_A:=\{F\in\mathcal P(\mathbb R):A\subseteq F\ \text{y}\ F\text{ es cerrado}\},
$$

entonces esta familia es un conjunto no vacío y

$$
\boxed{\overline A=\bigcap_{F\in\mathcal F_A}F.}
$$

**Demostración.**

La inclusión $A\subseteq\overline A$ está demostrada en Proposición 15.4.4 — Extensividad y monotonía de la clausura, y Teorema 15.4.5 — La clausura es un conjunto cerrado asegura que $\overline A$ es cerrado. Falta verificar su minimalidad.

Sea $F$ cerrado con $A\subseteq F$ y fijemos $x\in\overline A$. Si $x\notin F$, el criterio Proposición 15.3.6 — Criterio de cerradura mediante puntos exteriores aplicado a ese punto del complemento de $F$ proporciona un radio $r>0$ tal que $B_r(x)\cap F=\varnothing$. Como $A\subseteq F$, también $B_r(x)\cap A=\varnothing$. Esto contradice que $x\in\overline A$, pues cada bola de radio positivo centrada en $x$ debe intersectar $A$. Por consiguiente, $x\in F$. La arbitrariedad de $x$ demuestra $\overline A\subseteq F$.

Para justificar la fórmula final sin hablar de una «intersección de todos los cerrados» como si fuese una clase irrestricta, definimos $\mathcal F_A$ **por Separación sobre $\mathcal P(\mathbb R)$**. Este conjunto no es vacío: $\mathbb R$ es cerrado por Teorema 15.3.7 — Leyes fundamentales de los conjuntos cerrados y contiene a $A$. La familia identidad $F\mapsto F$, con dominio $\mathcal F_A$ y codominio $\mathcal P(\mathbb R)$, está definida por restricción de la identidad ya disponible; su intersección existe con ambiente $\mathbb R$ conforme a Definición 0.6.16 — Familia indexada.

La minimalidad recién probada implica $\overline A\subseteq F$ para cada $F\in\mathcal F_A$, por lo que $\overline A\subseteq\bigcap_{F\in\mathcal F_A}F$. A la inversa, $\overline A\in\mathcal F_A$, al ser cerrado y contener a $A$; por definición de intersección, $\bigcap_{F\in\mathcal F_A}F\subseteq\overline A$. La doble inclusión prueba la igualdad. Ningún paso requiere elegir un cerrado de manera arbitraria para cada punto ni escoger radios simultáneamente. ∎

La caracterización por intersección concuerda con las leyes de cerrados de §15.3: una intersección de cerrados es cerrada. La demostración anterior es además una **prueba de existencia** del mínimo: no se ha supuesto que tal mínimo exista para después denominarlo clausura.

### Corolario 15.4.7 — Un conjunto es cerrado si y sólo si coincide con su clausura

Para todo $A\subseteq\mathbb R$,

$$
\boxed{A\text{ es cerrado}\iff\overline A=A.}
$$

**Demostración.**

Si $A$ es cerrado, se puede usar $F=A$ en la propiedad de minimalidad de Teorema 15.4.6 — La clausura es el menor cerrado que contiene al conjunto. La inclusión $A\subseteq F$ es reflexiva y se obtiene $\overline A\subseteq A$. La inclusión opuesta $A\subseteq\overline A$ es Proposición 15.4.4 — Extensividad y monotonía de la clausura; por extensionalidad, $\overline A=A$.

Recíprocamente, si $\overline A=A$, el teorema Teorema 15.4.5 — La clausura es un conjunto cerrado dice que $\overline A$ es cerrado; sustituyendo conjuntos iguales, $A$ también es cerrado. ∎

### Proposición 15.4.8 — Idempotencia de la clausura

Para cualquier $A\subseteq\mathbb R$,

$$
\boxed{\overline{\overline A}=\overline A.}
$$

**Demostración.**

La primera clausura $\overline A$ es cerrada por Teorema 15.4.5 — La clausura es un conjunto cerrado. Aplicamos el criterio Corolario 15.4.7 — Un conjunto es cerrado si y sólo si coincide con su clausura al conjunto **ya construido** $\overline A$, que es un subconjunto de $\mathbb R$. Todo cerrado coincide con su clausura, de donde $\overline{\overline A}=\overline A$. Alternativamente, la extensividad y la minimalidad proporcionan respectivamente las inclusiones opuestas. ∎

El operador no añade nuevos puntos al repetirse: el resultado de la primera aplicación ya es cerrado.

### Proposición 15.4.9 — Clausura del vacío, de la recta y de un singleton

Para todo $a\in\mathbb R$,

$$
\boxed{\overline{\varnothing}=\varnothing,\qquad
\overline{\mathbb R}=\mathbb R,\qquad
\overline{\{a\}}=\{a\}.}
$$

**Demostración.**

Por Teorema 15.3.7 — Leyes fundamentales de los conjuntos cerrados, $\varnothing$ y $\mathbb R$ son cerrados. Por Corolario 15.3.9 — Los intervalos cerrados y los singletons son cerrados, también lo es $\{a\}$. Apliquemos a cada uno, por separado, Corolario 15.4.7 — Un conjunto es cerrado si y sólo si coincide con su clausura: al ser cerrados coinciden con sus clausuras, lo que proporciona exactamente las tres identidades. En particular, el vacío no posee puntos adherentes; no se interpreta la clausura como una operación que necesariamente agregue nuevos elementos. ∎

### Teorema 15.4.10 — Clausura de uniones e intersecciones

Sean $A,B\subseteq\mathbb R$. Entonces

$$
\boxed{\overline{A\cup B}=\overline A\cup\overline B,}
$$

$$
\boxed{\overline{A\cap B}\subseteq\overline A\cap\overline B.}
$$

Más generalmente, para cualquier conjunto de índices $I$ y cualquier familia $(A_i)_{i\in I}$ de subconjuntos de $\mathbb R$,

$$
\boxed{\bigcup_{i\in I}\overline{A_i}\subseteq
\overline{\bigcup_{i\in I}A_i},\qquad
\overline{\bigcap_{i\in I}A_i}\subseteq
\bigcap_{i\in I}\overline{A_i}.}
$$

Se admiten $I=\varnothing$, usando la convención previa de que la unión vacía es $\varnothing$ y la intersección vacía **en el ambiente $\mathbb R$** es $\mathbb R$. Las dos inclusiones indexadas no se anuncian como igualdades generales.

**Demostración.**

**Unión binaria.** Por la inclusión $A\subseteq A\cup B$ y la monotonía Proposición 15.4.4 — Extensividad y monotonía de la clausura, $\overline A\subseteq\overline{A\cup B}$. Del mismo modo, $\overline B\subseteq\overline{A\cup B}$. Reuniendo ambas inclusiones obtenemos

$$
\overline A\cup\overline B\subseteq\overline{A\cup B}.
$$

Para la inclusión inversa, $\overline A$ y $\overline B$ son cerrados por Teorema 15.4.5 — La clausura es un conjunto cerrado. Su unión es cerrada por la ley binaria de Teorema 15.3.7 — Leyes fundamentales de los conjuntos cerrados y contiene a $A\cup B$, porque $A\subseteq\overline A$ y $B\subseteq\overline B$. La minimalidad de la clausura Teorema 15.4.6 — La clausura es el menor cerrado que contiene al conjunto implica entonces

$$
\overline{A\cup B}\subseteq\overline A\cup\overline B.
$$

Las dos inclusiones demuestran la igualdad.

**Intersección binaria.** Como $A\cap B\subseteq A$ y $A\cap B\subseteq B$, la monotonía produce $\overline{A\cap B}\subseteq\overline A$ y $\overline{A\cap B}\subseteq\overline B$. La conjunción de ambas afirmaciones equivale a $\overline{A\cap B}\subseteq\overline A\cap\overline B$.

**Familias arbitrarias.** Como la aplicación de clausura es una función total $\mathcal P(\mathbb R)\to\mathcal P(\mathbb R)$, su composición con la familia $i\mapsto A_i$ proporciona, sin selección, la familia bien definida $i\mapsto\overline{A_i}$. Ambas uniones e intersecciones existen por Definición 0.6.16 — Familia indexada. Escribamos $U:=\bigcup_{i\in I}A_i$. Para cada $i\in I$ tenemos $A_i\subseteq U$ y, por monotonía, $\overline{A_i}\subseteq\overline U$. Si un punto pertenece a $\bigcup_i\overline{A_i}$, pertenece a una de esas clausuras y, por tanto, a $\overline U$. Queda probada la primera inclusión.

Para la segunda, escribamos $V:=\bigcap_{i\in I}A_i$, con ambiente $\mathbb R$. Cada $i\in I$ satisface $V\subseteq A_i$; por monotonía, $\overline V\subseteq\overline{A_i}$. Así, todos los puntos de $\overline V$ pertenecen a todas las clausuras y, por definición de intersección, $\overline V\subseteq\bigcap_i\overline{A_i}$. Si $I=\varnothing$, la primera inclusión se reduce a $\varnothing\subseteq\overline\varnothing$ y la segunda a $\overline{\mathbb R}\subseteq\mathbb R$, válidas por Proposición 15.4.9 — Clausura del vacío, de la recta y de un singleton. Ninguna parte seleccionó simultáneamente un índice o un punto para todos los radios. ∎

> **Lectura conceptual.** La clausura **conserva exactamente las uniones finitas**; para intersecciones siempre se obtiene al menos una inclusión. En familias arbitrarias, las dos leyes anteriores sólo proporcionan inclusiones. La siguiente proposición muestra por qué ninguna de esas dos inclusiones puede convertirse automáticamente en igualdad.

### Proposición 15.4.11 — Dos inclusiones que pueden ser estrictas

Existen $A,B\subseteq\mathbb R$ para los que

$$
\overline{A\cap B}\subsetneq\overline A\cap\overline B,
$$

y existe una familia de conjuntos **cerrados** $(F_r)_{r\in I}$ tal que

$$
\bigcup_{r\in I}\overline{F_r}\subsetneq
\overline{\bigcup_{r\in I}F_r}.
$$

**Demostración.**

**Primera afirmación.** Fijemos $a\in\mathbb R$ y formemos por Separación las semirrectas estrictas

$$
A:=\{x\in\mathbb R:x<a\},\qquad
B:=\{x\in\mathbb R:a<x\},
$$

ya estudiadas en Proposición 15.3.8 — Las dos semirrectas estrictas son abiertas. Son disjuntas, así que $A\cap B=\varnothing$ y $\overline{A\cap B}=\varnothing$ por Proposición 15.4.9 — Clausura del vacío, de la recta y de un singleton. No obstante, para cada $r>0$ el punto $a-r/(1+1)$ pertenece a $A$ y a $B_r(a)$: su distancia a $a$ es $r/(1+1)<r$. De igual modo, $a+r/(1+1)\in B\cap B_r(a)$. Por la definición de adherencia, $a\in\overline A\cap\overline B$. Esta intersección no es vacía, mientras que $\overline{A\cap B}$ sí lo es. La inclusión de Teorema 15.4.10 — Clausura de uniones e intersecciones es estricta.

**Segunda afirmación.** Reutilicemos la familia **explícita** construida en Proposición 15.3.11 — Las restricciones de finitud son necesarias: $I:=\{r\in\mathbb R:r>0\}$ y $F_r:=\mathbb R\setminus B_r(a)$. Allí se probaron tanto la existencia de esta familia como la identidad

$$
\bigcup_{r\in I}F_r=\mathbb R\setminus\{a\}.
$$

Cada $F_r$ es cerrado, por lo que Corolario 15.4.7 — Un conjunto es cerrado si y sólo si coincide con su clausura da $\overline{F_r}=F_r$. En consecuencia,

$$
\bigcup_{r\in I}\overline{F_r}=\mathbb R\setminus\{a\}.
$$

Por extensividad, todos los puntos distintos de $a$ pertenecen a la clausura del conjunto $\mathbb R\setminus\{a\}$. También pertenece $a$: para cada radio $s>0$, el punto $a+s/(1+1)$ está en $B_s(a)$ y es distinto de $a$, de modo que

$$
B_s(a)\cap(\mathbb R\setminus\{a\})\ne\varnothing.
$$

Luego $a$ es adherente al complemento del singleton y su clausura es toda la recta. Hemos obtenido

$$
\bigcup_{r\in I}\overline{F_r}=\mathbb R\setminus\{a\}
\subsetneq\mathbb R
=\overline{\bigcup_{r\in I}F_r},
$$

como queríamos. Toda la familia está determinada por una fórmula, sin seleccionar radios ni usar un axioma de elección. ∎

La clausura puede entenderse, por tanto, tanto mediante bolas como mediante cerrados: es el conjunto de los puntos cuya proximidad con $A$ resulta inevitable y, simultáneamente, el menor cerrado que contiene a $A$. La siguiente unidad distinguirá ahora los **puntos de acumulación** de los meramente adherentes; en particular, deberá exigir que las bolas contengan puntos de $A$ *diferentes del propio centro*.
