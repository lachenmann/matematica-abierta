## 15.6. Frontera de un conjunto {#sec-ta-15-6}

El interior de $A$ reúne los puntos alrededor de los cuales cabe permanecer enteramente en $A$; su exterior reúne aquellos alrededor de los cuales cabe permanecer enteramente fuera de $A$. Pero estas dos posibilidades no agotan necesariamente la recta. Puede ocurrir que **cada** bola centrada en un punto encuentre simultáneamente puntos de $A$ y de su complemento. Ése será nuestro criterio para reconocer la frontera.

La definición no exige que el centro pertenezca a $A$ y tampoco debe confundirse con la acumulación: allí se excluye el centro al buscar *otro punto de $A$*; aquí se exige proximidad con **dos conjuntos diferentes**, sin perforar ninguna bola.

### Definición 15.6.1 — Punto de frontera
Sean $A\subseteq\mathbb R$ y $x\in\mathbb R$. Diremos que **$x$ es un punto de frontera de $A$** si, para cada $r\in\mathbb R$ con $r>0$, se cumplen simultáneamente

$$
\boxed{B_r(x)\cap A\ne\varnothing
\qquad\text{y}\qquad
B_r(x)\cap(\mathbb R\setminus A)\ne\varnothing.}
$$

Los dos cuantificadores existenciales implícitos en las intersecciones no vacías se refieren a un radio **fijado**. No se pide una función que asigne testigos a todos los radios. Tampoco se exige $x\in A$: el centro puede pertenecer al conjunto o a su complemento. En ambos casos debe haber puntos de los dos lados tan próximos como se quiera.


### Definición 15.6.2 — Frontera de un conjunto
Para $A\subseteq\mathbb R$, definimos su **frontera** como el conjunto de todos sus puntos de frontera:

$$
\boxed{\partial A:=\left\{x\in\mathbb R:
\forall r\in\mathbb R\,\bigl(r>0\Rightarrow
[B_r(x)\cap A\ne\varnothing\ \land\
B_r(x)\cap(\mathbb R\setminus A)\ne\varnothing]\bigr)\right\}.}
$$

El complemento $\mathbb R\setminus A$ ya existe; la fórmula está definida para cada $x\in\mathbb R$ y el conjunto $\partial A$ existe por **Separación sobre $\mathbb R$**. La extensionalidad garantiza su unicidad. Puesto que $\mathcal P(\mathbb R)$ es un conjunto y para cada $A\in\mathcal P(\mathbb R)$ se determina un único $\partial A\in\mathcal P(\mathbb R)$, el grafo

$$
\{\langle A,F\rangle\in\mathcal P(\mathbb R)\times\mathcal P(\mathbb R):F=\partial A\}
$$

existe por Separación dentro de ese producto y define una función total de $\mathcal P(\mathbb R)$ en sí mismo. La escritura $\partial A$ queda reservada a esta operación sobre subconjuntos de la recta; no designa la derivada de una función ni presupone una topología abstracta. Ninguna de las dos construcciones selecciona puntos de las intersecciones.


### Teorema 15.6.3 — Caracterización de la frontera por dos clausuras
Para cualquier $A\subseteq\mathbb R$,

$$
\boxed{\partial A=\overline A\cap\overline{\mathbb R\setminus A}.}
$$

**Demostración.**
Tomemos $x\in\partial A$. Para cada radio $r>0$, la definición proporciona una intersección no vacía $B_r(x)\cap A$; por la definición de adherencia de §15.4, $x\in\overline A$. Para esos mismos radios se tiene además $B_r(x)\cap(\mathbb R\setminus A)\ne\varnothing$, de donde $x\in\overline{\mathbb R\setminus A}$. Así,

$$
\partial A\subseteq\overline A\cap\overline{\mathbb R\setminus A}.
$$

Para la inclusión inversa, sea $x\in\overline A\cap\overline{\mathbb R\setminus A}$. Fijemos un radio arbitrario $r>0$. La primera pertenencia afirma que $B_r(x)\cap A\ne\varnothing$; la segunda afirma que $B_r(x)\cap(\mathbb R\setminus A)\ne\varnothing$. Ambas condiciones se cumplen para el **mismo** radio arbitrario, luego $x$ es fronterizo y pertenece a $\partial A$. La doble inclusión y la extensionalidad completan la prueba. ∎

> **Interpretación.** La frontera no es simplemente el conjunto de puntos que están fuera de $A$ ni su conjunto derivado. Es el lugar donde la adherencia a $A$ y la adherencia a su complemento coinciden.


### Teorema 15.6.4 — Descomposición de la recta en interior, frontera y exterior
Para todo $A\subseteq\mathbb R$ se tienen las identidades

$$
\boxed{\partial A=\overline A\setminus A^\circ,}
\qquad
\boxed{\overline A=A^\circ\cup\partial A,}
$$

así como la descomposición

$$
\boxed{\mathbb R=A^\circ\cup\partial A\cup\operatorname{Ext}(A).}
$$

Las tres partes de la última unión son **disjuntas dos a dos**.

**Demostración.**
Apliquemos Proposición §15.4.3 — La adherencia es la negación de la exterioridad al complemento $C:=\mathbb R\setminus A$. Allí se demostró que $\overline C=\mathbb R\setminus\operatorname{Ext}(C)$. A su vez, Proposición §15.3.3 — El exterior es el interior del complemento, junto con la doble complementación relativa a $\mathbb R$, da

$$
\operatorname{Ext}(C)
=(\mathbb R\setminus C)^\circ=A^\circ.
$$

En consecuencia,

$$
\overline{\mathbb R\setminus A}=\mathbb R\setminus A^\circ.
$$

Sustituyendo en Teorema §15.6.3 — Caracterización de la frontera por dos clausuras y aplicando la ley de intersección con un complemento, obtenemos por extensionalidad

$$
\partial A=\overline A\cap(\mathbb R\setminus A^\circ)
=\overline A\setminus A^\circ.
$$

Como $A^\circ\subseteq A\subseteq\overline A$ (Proposición §15.2.3 — Interior y vecindades y Proposición §15.4.4 — Extensividad y monotonía de la clausura), todo punto de $\overline A$ pertenece a $A^\circ$ o a $\overline A\setminus A^\circ$ por distinción clásica de casos. Recíprocamente, ambos conjuntos están contenidos en $\overline A$. Esto demuestra $\overline A=A^\circ\cup\partial A$ y prueba también $A^\circ\cap\partial A=\varnothing$.

Finalmente, Proposición §15.4.3 — La adherencia es la negación de la exterioridad proporciona $\mathbb R\setminus\overline A=\operatorname{Ext}(A)$. Todo punto real está en $\overline A$ o en su complemento; utilizando la identidad precedente obtenemos la unión anunciada. La parte exterior no intersecta $A^\circ$ ni $\partial A$, porque ambas están contenidas en $\overline A$. Así, las tres partes son disjuntas dos a dos y cubren exactamente $\mathbb R$. ∎

Esta descomposición no dice que $A$ coincida con su interior unido a la frontera: lo que coincide con esa unión es **la clausura de $A$**. Según cómo se hayan incluido sus puntos fronterizos, dos conjuntos distintos pueden tener la misma clausura y la misma frontera.


### Proposición 15.6.5 — La frontera es cerrada y no cambia al tomar el complemento
Para todo $A\subseteq\mathbb R$,

$$
\boxed{\partial A\text{ es cerrado},}
\qquad
\boxed{\partial(\mathbb R\setminus A)=\partial A.}
$$

**Demostración.**
Por Teorema §15.4.5 — La clausura es un conjunto cerrado, los conjuntos $\overline A$ y $\overline{\mathbb R\setminus A}$ son cerrados. Su intersección también lo es por la ley de intersecciones de cerrados Teorema §15.3.7 — Leyes fundamentales de los conjuntos cerrados; la identidad de Teorema §15.6.3 — Caracterización de la frontera por dos clausuras identifica esta intersección con $\partial A$, lo que demuestra la primera afirmación.

Para la segunda, apliquemos la misma identidad al complemento $C=\mathbb R\setminus A$:

$$
\partial C=\overline C\cap\overline{\mathbb R\setminus C}
=\overline{\mathbb R\setminus A}\cap\overline A
=\partial A.
$$

La doble complementación tiene lugar siempre **dentro de $\mathbb R$**. La conmutatividad de la intersección, demostrable por pertenencia a ambos factores, concluye la prueba. ∎

La simetría expresa que una frontera no privilegia ninguno de los dos lados: intercambiar $A$ con su complemento no modifica la región en la que ambos se aproximan.


### Teorema 15.6.6 — Criterios de apertura y cerradura mediante la frontera
Sea $A\subseteq\mathbb R$. Entonces

$$
\boxed{A\text{ es abierto}\iff A\cap\partial A=\varnothing,}
$$

$$
\boxed{A\text{ es cerrado}\iff\partial A\subseteq A.}
$$

**Demostración.**
**Apertura, implicación directa.** Si $A$ es abierto, Proposición §15.2.6 — Caracterización de los abiertos mediante el interior da $A=A^\circ$. Por la descomposición disjunta de Teorema §15.6.4 — Descomposición de la recta en interior, frontera y exterior, $A^\circ\cap\partial A=\varnothing$; luego $A\cap\partial A=\varnothing$.

**Apertura, implicación recíproca.** Supongamos $A\cap\partial A=\varnothing$ y tomemos $x\in A$. Por extensividad, $x\in\overline A$. La igualdad $\overline A=A^\circ\cup\partial A$ implica que $x\in A^\circ$ o $x\in\partial A$. La segunda posibilidad contradice $x\in A$ y la disjunción supuesta; por tanto $x\in A^\circ$. Hemos probado $A\subseteq A^\circ$, y la inclusión inversa figura en Proposición §15.2.3 — Interior y vecindades. Así $A=A^\circ$, de donde $A$ es abierto por Proposición §15.2.6 — Caracterización de los abiertos mediante el interior.

**Cerradura, implicación directa.** Si $A$ es cerrado, Corolario §15.4.7 — Un conjunto es cerrado si y sólo si coincide con su clausura asegura $\overline A=A$. La identidad $\partial A\subseteq\overline A$, inmediata de Teorema §15.6.4 — Descomposición de la recta en interior, frontera y exterior, da $\partial A\subseteq A$.

**Cerradura, implicación recíproca.** Supongamos $\partial A\subseteq A$. Dado $x\in\overline A$, la descomposición $\overline A=A^\circ\cup\partial A$ proporciona dos casos. En el primero, $x\in A^\circ\subseteq A$; en el segundo, $x\in\partial A\subseteq A$. Luego $\overline A\subseteq A$, mientras que $A\subseteq\overline A$ siempre. Por extensionalidad, $A=\overline A$ y el criterio Corolario §15.4.7 — Un conjunto es cerrado si y sólo si coincide con su clausura concluye que $A$ es cerrado. ∎

La apertura exige que **ningún punto del propio conjunto** sea fronterizo; la cerradura exige, por el contrario, que **todos los puntos fronterizos** estén incluidos en él. No se deduce de aquí que todo conjunto sea abierto o cerrado: puede no satisfacer ninguna de las dos exigencias.


### Corolario 15.6.7 — Frontera vacía y conjuntos abiertos y cerrados
Para $A\subseteq\mathbb R$,

$$
\boxed{\partial A=\varnothing\iff A\text{ es abierto y cerrado}.}
$$

**Demostración.**
Si $\partial A=\varnothing$, tanto $A\cap\partial A=\varnothing$ como $\partial A\subseteq A$ se cumplen; las dos equivalencias de Teorema §15.6.6 — Criterios de apertura y cerradura mediante la frontera hacen a $A$ abierto y cerrado. Recíprocamente, si $A$ es abierto y cerrado, esas equivalencias dan $A\cap\partial A=\varnothing$ y $\partial A\subseteq A$. Cualquier $x\in\partial A$ pertenecería entonces a $A\cap\partial A$, contradicción. Por tanto, $\partial A$ no tiene elementos y es vacío por extensionalidad. ∎

Todavía **no** afirmamos que los únicos subconjuntos simultáneamente abiertos y cerrados de $\mathbb R$ sean $\varnothing$ y $\mathbb R$: tal afirmación necesita su propia demostración y no se obtiene sólo de las definiciones anteriores.


### Proposición 15.6.8 — Ejemplos: extremos, singletons y falta de monotonía
Para $a,b\in\mathbb R$ con $a<b$ se tienen las identidades

$$
\boxed{\partial\varnothing=\partial\mathbb R=\varnothing,\qquad
\partial\{a\}=\{a\},}
$$

$$
\boxed{\partial(a,b)=\partial[a,b]=\{a,b\}.}
$$

La operación frontera **no es monótona** respecto de la inclusión: pueden existir $A\subseteq B$ con $\partial A\not\subseteq\partial B$.

**Demostración.**
**Vacío y recta.** Por Proposición §15.4.9 — Clausura del vacío, de la recta y de un singleton, $\overline\varnothing=\varnothing$ y $\overline{\mathbb R}=\mathbb R$. Aplicando la caracterización de Teorema §15.6.3 — Caracterización de la frontera por dos clausuras a $\varnothing$ y a $\mathbb R$, con sus complementos relativos intercambiados, ambas fronteras resultan ser $\varnothing\cap\mathbb R=\varnothing$.

**Singleton.** El conjunto $\{a\}$ es cerrado por Corolario §15.3.9 — Los intervalos cerrados y los singletons son cerrados y, por Corolario §15.4.7 — Un conjunto es cerrado si y sólo si coincide con su clausura, su clausura es $\{a\}$. Su interior es vacío: si $a$ fuera interior, habría un $r>0$ con $B_r(a)\subseteq\{a\}$; pero $a+r/(1+1)$ pertenece a esa bola y es distinto de $a$. Como $A^\circ\subseteq A$, ningún otro punto puede ser interior al singleton. Por consiguiente, la identidad $\partial A=\overline A\setminus A^\circ$ de Teorema §15.6.4 — Descomposición de la recta en interior, frontera y exterior da $\partial\{a\}=\{a\}$.

**Intervalo abierto.** Proposición §15.2.9 — Ejemplos: intervalos abiertos y singletons prueba que $(a,b)$ es abierto y, por Proposición §15.2.6 — Caracterización de los abiertos mediante el interior, su interior es $(a,b)$. La proposición Proposición §15.5.9 — Ejemplos y límite de la ley de unión establece $\operatorname{Acc}((a,b))=[a,b]$; combinada con $\overline A=A\cup\operatorname{Acc}(A)$ de Teorema §15.5.4 — Descomposición de la clausura y criterio de cerradura, implica $\overline{(a,b)}=[a,b]$. En consecuencia,

$$
\partial(a,b)=[a,b]\setminus(a,b)=\{a,b\},
$$

pues $a<b$ y el orden total determina exactamente qué extremos agrega el intervalo cerrado.

**Intervalo cerrado.** Corolario §15.3.9 — Los intervalos cerrados y los singletons son cerrados demuestra que $[a,b]$ es cerrado, y por ello $\overline{[a,b]}=[a,b]$. Probemos que su interior es precisamente $(a,b)$. Cada $x\in(a,b)$ es interior a $(a,b)$ por apertura; una bola contenida en $(a,b)$ también está contenida en $[a,b]$. De modo que $(a,b)\subseteq[a,b]^\circ$. A la inversa, cualquier punto interior a $[a,b]$ pertenece al propio intervalo. El extremo $a$ no puede ser interior: para todo $r>0$, el punto $a-r/(1+1)$ pertenece a $B_r(a)$ y queda fuera de $[a,b]$. Análogamente, $b+r/(1+1)$ demuestra que $b$ no es interior. Todo punto restante de $[a,b]$ está estrictamente entre $a$ y $b$, por totalidad del orden. Así, $[a,b]^\circ=(a,b)$ y

$$
\partial[a,b]=[a,b]\setminus(a,b)=\{a,b\}.
$$

**Ausencia de monotonía.** Tomemos $A=\{a\}$ y $B=\mathbb R$. Ciertamente $A\subseteq B$, pero acabamos de demostrar $\partial A=\{a\}$ y $\partial B=\varnothing$. La inclusión $\partial A\subseteq\partial B$ es falsa. ∎

Estos ejemplos muestran por qué «frontera» no significa «puntos exteriores» ni «puntos de acumulación»: la frontera de un singleton contiene a su centro, aunque Proposición §15.5.9 — Ejemplos y límite de la ley de unión prueba que dicho singleton no tiene puntos de acumulación. Asimismo, un intervalo abierto y su versión cerrada tienen idéntica frontera, aun cuando difieren en la pertenencia de los extremos. Más adelante estudiaremos las leyes de la frontera bajo operaciones de conjuntos y su relación con otras caracterizaciones de proximidad; ninguna de ellas ha sido supuesta en esta unidad.
