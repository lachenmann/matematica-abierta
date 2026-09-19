## 15.9. Densidad e intervalos {#sec-ta-15-9}

La palabra *denso* apareció anteriormente al demostrar que entre dos números reales distintos hay una imagen racional (Corolario 12.3.2 — Densidad racional en todo cuerpo ordenado completo). Ahora le daremos un significado topológico aplicable a **cualquier** subconjunto de la recta. El resultado central identificará la densidad con el encuentro de todos los intervalos abiertos no degenerados. Después distinguiremos densidad e interioridad, mostraremos que los abiertos se reconstruyen con intervalos de extremos racionales y completaremos la descripción de los intervalos semiabiertos.

En toda la sección, $\mathbb R$ es el cuerpo ordenado completo estructural de §12.9. Escribiremos $j:=\jmath_{\mathbb Q}^{\mathbb R}:\mathbb Q\to\mathbb R$ para su incrustación racional canónica (Definición 12.2.3 — Copia canónica de los racionales en un cuerpo ordenado, Teorema 12.2.5 — La copia racional es una incrustación de cuerpos ordenados). La abreviatura local $D_{\mathbb Q}:=j[\mathbb Q]$ designa un subconjunto genuino de $\mathbb R$; **no** supone la igualdad conjuntista $\mathbb Q\subseteq\mathbb R$.

### Definición 15.9.1 — Subconjunto denso de la recta

Un conjunto $D\subseteq\mathbb R$ se llama **denso en la recta real** si su clausura coincide con toda la recta:

$$
\boxed{D\text{ es denso en }\mathbb R\iff\overline D=\mathbb R.}
$$

Equivalentemente, *cada punto de la recta* es adherente a $D$. La definición no dice que $D=\mathbb R$, que tenga puntos interiores ni que haya una sucesión de elementos de $D$ convergente a cada real. Esta última formulación no se importará indebidamente de la sección anterior.

---

### Teorema 15.9.2 — Tres caracterizaciones de la densidad

Sea $D\subseteq\mathbb R$. Son equivalentes las siguientes afirmaciones:

1. $D$ es denso en $\mathbb R$.
2. Todo abierto $U\subseteq\mathbb R$ no vacío satisface $U\cap D\ne\varnothing$.
3. Para cualesquiera $a,b\in\mathbb R$ con $a<b$, se cumple $(a,b)\cap D\ne\varnothing$.

**Demostración.**

**(1) implica (2).** Sea $U$ abierto y no vacío. Fijemos *un* $x\in U$. Por apertura existe $r>0$ tal que $B_r(x)\subseteq U$. Como $\overline D=\mathbb R$, el punto $x$ es adherente a $D$; en consecuencia $B_r(x)\cap D\ne\varnothing$. La inclusión de la bola en $U$ proporciona $U\cap D\ne\varnothing$.

**(2) implica (3).** Para $a<b$, el intervalo $(a,b)$ es abierto por Proposición 15.2.9 — Ejemplos: intervalos abiertos y singletons y no vacío por densidad del orden real Teorema 4.1.11 — Todo cuerpo ordenado es densamente ordenado (por ejemplo, contiene el punto medio). Aplicamos (2) a ese abierto.

**(3) implica (1).** Fijemos $x\in\mathbb R$ y $r>0$. La igualdad Proposición 15.1.2 — Las bolas son intervalos abiertos centrados da $B_r(x)=(x-r,x+r)$; sus extremos están estrictamente ordenados porque $r>0$. Por (3), esta bola corta a $D$. Como $r$ era arbitrario, $x\in\overline D$. Hemos probado $\mathbb R\subseteq\overline D$; la inclusión inversa forma parte del tipo de la clausura. Concluimos $\overline D=\mathbb R$ por extensionalidad. ∎

> **Lectura de cuantificadores.** El criterio de intervalos afirma $\forall a\,\forall b\,(a<b\Rightarrow\exists d\in D\ (a<d<b))$. No proporciona una única función que escoja simultáneamente un punto para cada intervalo; tampoco es necesaria para demostrar densidad.

---

### Proposición 15.9.3 — Densidad de la copia racional canónica

Sea $D_{\mathbb Q}=j[\mathbb Q]$. Entonces

$$
\boxed{\overline{D_{\mathbb Q}}=\mathbb R.}
$$

En particular, todo abierto no vacío de la recta contiene la imagen de algún número racional.

**Demostración.**

El corolario Corolario 12.3.2 — Densidad racional en todo cuerpo ordenado completo, ya cerrado en §12.3, establece que para cada par $a<b$ de reales existe $q\in\mathbb Q$ con $a<j(q)<b$. Por tanto, todo intervalo abierto no degenerado corta a $D_{\mathbb Q}$, que satisface la condición (3) de Teorema 15.9.2 — Tres caracterizaciones de la densidad. El mismo teorema concluye que $D_{\mathbb Q}$ es denso y que corta todos los abiertos no vacíos. No estamos volviendo a probar la densidad *de orden* del Capítulo 12: la utilizamos para obtener su caracterización topológica. ∎

---

### Proposición 15.9.4 — Densidad, interior del complemento y frontera

Para todo $A\subseteq\mathbb R$ se tiene

$$
\boxed{A\text{ es denso}\iff(\mathbb R\setminus A)^\circ=\varnothing.}
$$

Además, si $A$ es denso, su frontera se caracteriza por

$$
\boxed{\partial A=\mathbb R\setminus A^\circ.}
$$

En particular, si tanto $A$ como su complemento son densos, ambos tienen interior vacío y $\partial A=\mathbb R$.

**Demostración.**

La dualidad de §15.4, obtenida a partir de Proposición 15.3.3 — El exterior es el interior del complemento y Proposición 15.4.3 — La adherencia es la negación de la exterioridad, dice que

$$
\overline A=\mathbb R\setminus(\mathbb R\setminus A)^\circ.
$$

Por doble complementación relativa a $\mathbb R$, esta clausura es toda la recta si y sólo si el interior del complemento es vacío. Aplicamos Definición 15.9.1 — Subconjunto denso de la recta para obtener la primera equivalencia. Si $A$ es denso, sustituimos $\overline A=\mathbb R$ en $\partial A=\overline A\setminus A^\circ$, identidad de Teorema 15.6.4 — Descomposición de la recta en interior, frontera y exterior; se obtiene la segunda fórmula. Finalmente, aplicando la primera equivalencia sucesivamente a $A$ y a su complemento, la densidad de ambos da $(\mathbb R\setminus A)^\circ=A^\circ=\varnothing$; la segunda identidad concluye $\partial A=\mathbb R$. ∎

**Advertencia.** Un conjunto denso puede tener interior no vacío: $A=\mathbb R$ es un ejemplo inmediato. La densidad de $A$ sólo fuerza el **vacío del interior de su complemento**. Las dos propiedades no deben confundirse.

---

### Proposición 15.9.5 — Intersección de un denso con un abierto

Si $D\subseteq\mathbb R$ es denso y $U\subseteq\mathbb R$ es abierto, entonces

$$
\boxed{\overline{U\cap D}=\overline U.}
$$

Si además $U\ne\varnothing$, necesariamente $U\cap D\ne\varnothing$.

**Demostración.**

Por inclusión $U\cap D\subseteq U$ y monotonía de la clausura (Proposición 15.4.4 — Extensividad y monotonía de la clausura),

$$
\overline{U\cap D}\subseteq\overline U.
$$

Para obtener la otra inclusión, fijemos $x\in U$ y un radio cualquiera $s>0$. Como $U$ es abierto, existe $r>0$ tal que $B_r(x)\subseteq U$. El número $t=\min\{r,s\}$ es positivo y $B_t(x)\subseteq B_s(x)\cap U$. Por densidad, $B_t(x)\cap D\ne\varnothing$, así que $B_s(x)\cap(U\cap D)\ne\varnothing$. Al variar $s$, esto demuestra $x\in\overline{U\cap D}$ y, por tanto,

$$
U\subseteq\overline{U\cap D}.
$$

Tomamos clausuras a ambos lados: la monotonía y la idempotencia (Proposición 15.4.8 — Idempotencia de la clausura) proporcionan $\overline U\subseteq\overline{U\cap D}$. Ambas inclusiones prueban la igualdad. Si $U$ es no vacío, su intersección con $D$ es no vacía por Teorema 15.9.2 — Tres caracterizaciones de la densidad. El argumento cubre también $U=\varnothing$: ambas clausuras son vacías. ∎

La igualdad expresa con precisión que, **dentro de cualquier región abierta**, los puntos de un conjunto denso se aproximan a todos los puntos de esa región y, por clausura, a sus puntos adherentes.

---

### Definición 15.9.6 — Familia de intervalos con extremos racionales

Denotemos por $\mathcal B_{\mathbb Q}$ la siguiente **familia de subconjuntos de la recta**:

$$
\boxed{\mathcal B_{\mathbb Q}:=
\{V\in\mathcal P(\mathbb R):\exists p,q\in\mathbb Q\,
[p<q\ \land\ V=(j(p),j(q))]\}.}
$$

Cada intervalo de esta familia es abierto y no vacío. El conjunto $\mathcal B_{\mathbb Q}$ existe por Separación **dentro de $\mathcal P(\mathbb R)$**; no es una colección irrestricta. Sus extremos son *imágenes de racionales* y por ello pertenecen a $\mathbb R$. No se ha añadido una nueva topología ni se identifica $\mathbb Q$ con su imagen.

---

### Teorema 15.9.7 — Todo abierto es unión de intervalos con extremos racionales

Para todo conjunto abierto $U\subseteq\mathbb R$,

$$
\boxed{U=\bigcup\{V\in\mathcal B_{\mathbb Q}:V\subseteq U\}.}
$$

La unión se toma sobre una familia que es un **conjunto**. Si $U=\varnothing$, la familia de intervalos contenidos en él es vacía y la unión es $\varnothing$.

**Demostración.**

Definamos $\mathcal F_U:=\{V\in\mathcal B_{\mathbb Q}:V\subseteq U\}$ mediante Separación sobre la familia existente $\mathcal B_{\mathbb Q}$. Su unión existe como conjunto y está contenida en $U$, ya que cada miembro de $\mathcal F_U$ lo está.

Para la inclusión inversa, tomemos $x\in U$. La apertura produce un radio $r>0$ con

$$
B_r(x)=(x-r,x+r)\subseteq U.
$$

Los dos intervalos $(x-r,x)$ y $(x,x+r)$ tienen extremos estrictamente ordenados. Por la densidad **de orden** Corolario 12.3.2 — Densidad racional en todo cuerpo ordenado completo, existen racionales $p,q\in\mathbb Q$ con

$$
x-r<j(p)<x<j(q)<x+r.
$$

Hemos utilizado dos instancias finitas de un teorema existencial para el único $x$ fijado; no se asignan pares de extremos a todos los puntos de $U$. Sea $V:=(j(p),j(q))$. Entonces $p<q$ porque $j$ refleja el orden (Teorema 12.2.5 — La copia racional es una incrustación de cuerpos ordenados), así que $V\in\mathcal B_{\mathbb Q}$. Además,

$$
x\in V\subseteq(x-r,x+r)\subseteq U.
$$

Luego $V\in\mathcal F_U$ y $x\in\bigcup\mathcal F_U$. Como $x$ era arbitrario, $U\subseteq\bigcup\mathcal F_U$ y concluimos por doble inclusión. ∎

> **Por qué no interviene Choice.** Sería incorrecto deducir sin más una función global $x\mapsto r_x$ a partir de que cada $x\in U$ posee *algún* radio. En lugar de escoger radios o intervalos, construimos el conjunto de **todos** los intervalos racionales que caben en $U$. Cada punto pertenece localmente a alguno y eso basta para la igualdad.

---

### Proposición 15.9.8 — Interior, clausura y frontera de los intervalos semiabiertos

Sean $a,b\in\mathbb R$ con $a<b$ y sea $H$ cualquiera de los dos intervalos $[a,b)$ o $(a,b]$. Entonces

$$
\boxed{H^\circ=(a,b),\qquad
\overline H=[a,b],\qquad
\partial H=\{a,b\}.}
$$

**Demostración.**

Para cualquiera de las dos formas, las definiciones de intervalos proporcionan

$$
(a,b)\subseteq H\subseteq[a,b].
$$

La monotonía del interior Proposición 15.7.1 — Monotonía y leyes del interior da $(a,b)^\circ\subseteq H^\circ\subseteq[a,b]^\circ$. Las demostraciones de Proposición 15.6.8 — Ejemplos: extremos, singletons y falta de monotonía ya establecieron $(a,b)^\circ=[a,b]^\circ=(a,b)$; luego $H^\circ=(a,b)$ por doble inclusión.

Análogamente, la monotonía de la clausura da

$$
\overline{(a,b)}\subseteq\overline H\subseteq\overline{[a,b]}.
$$

Por Proposición 15.6.8 — Ejemplos: extremos, singletons y falta de monotonía y los resultados de cierre reutilizados allí, las clausuras de ambos extremos de esta cadena son $[a,b]$. Por ello $\overline H=[a,b]$. La identidad ya cerrada Teorema 15.6.4 — Descomposición de la recta en interior, frontera y exterior concluye

$$
\partial H=\overline H\setminus H^\circ=[a,b]\setminus(a,b)=\{a,b\}.
$$

No hemos redefinido intervalos ni repetido las pruebas de los casos abierto y cerrado: las dos cadenas de inclusiones completan los casos semiabiertos. ∎

---

### Proposición 15.9.9 — Dos subconjuntos densos disjuntos

El conjunto $D_{\mathbb Q}=j[\mathbb Q]$ y su complemento

$$
I_{\mathbb R}:=\mathbb R\setminus D_{\mathbb Q}
$$

son **disjuntos y ambos densos** en $\mathbb R$. En consecuencia,

$$
\boxed{D_{\mathbb Q}^\circ=I_{\mathbb R}^\circ=\varnothing,
\qquad\partial D_{\mathbb Q}=\partial I_{\mathbb R}=\mathbb R.}
$$

**Demostración.**

**Existencia de un real fuera de la copia racional.** En el modelo de Dedekind, Proposición 5.3.3 — $\alpha_2$ no es una cortadura racional y Corolario 5.5.4 — La copia racional no agota $\mathbb R_D$ proporcionan una cortadura $\alpha_2\in\mathbb R_D$ que no pertenece a $\iota_D[\mathbb Q]$. La unicidad estructural de la completación (Teorema 12.7.2 — Unicidad del isomorfismo entre completaciones ordenadas–Teorema 12.8.1 — Existencia y caracterización única de la completación ordenada de $\mathbb Q$) proporciona un isomorfismo de cuerpos ordenados $\Phi:\mathbb R_D\to\mathbb R$ que conmuta con las incrustaciones racionales: $\Phi\circ\iota_D=j$. Fijemos $\xi:=\Phi(\alpha_2)$. Si $\xi=j(q)$ para algún $q\in\mathbb Q$, la inyectividad de $\Phi$ implicaría $\alpha_2=\iota_D(q)$, contradicción. Por tanto $\xi\notin D_{\mathbb Q}$; en particular, $\xi\ne0$.

**Un elemento del complemento en cada intervalo.** Sean $a<b$. También $a-\xi<b-\xi$; por la densidad racional de orden Corolario 12.3.2 — Densidad racional en todo cuerpo ordenado completo, existe $q\in\mathbb Q$ tal que

$$
a-\xi<j(q)<b-\xi.
$$

Sumando $\xi$ obtenemos $y:=j(q)+\xi\in(a,b)$. Este punto no pertenece a $D_{\mathbb Q}$: si $y=j(t)$ para algún $t\in\mathbb Q$, la incrustación de cuerpos ordenados Teorema 12.2.5 — La copia racional es una incrustación de cuerpos ordenados y el carácter de subcuerpo de su imagen (Lema 12.2.6 — La imagen de la copia racional es un subcuerpo) darían

$$
\xi=j(t)-j(q)=j(t-q)\in D_{\mathbb Q},
$$

contradicción. Por tanto, todo intervalo no degenerado corta a $I_{\mathbb R}$. La traslación por el irracional fijo $\xi$ ha bastado: no se necesita elegir una sucesión de aproximantes ni emplear arquimedianidad de nuevo.

El intervalo $(a,b)$ era arbitrario. Por Teorema 15.9.2 — Tres caracterizaciones de la densidad, $I_{\mathbb R}$ es denso. La densidad de $D_{\mathbb Q}$ ya quedó demostrada en Proposición 15.9.3 — Densidad de la copia racional canónica. Ambos conjuntos son disjuntos por la definición del complemento, y Proposición 15.9.4 — Densidad, interior del complemento y frontera aplicada en ambos sentidos muestra que sus interiores son vacíos. Como uno de ellos es denso y tiene interior vacío, su frontera es toda la recta; la simetría Proposición 15.6.5 — La frontera es cerrada y no cambia al tomar el complemento da lo mismo para el otro. ∎

> **Consecuencia conceptual.** Dos conjuntos disjuntos pueden ser densos simultáneamente. No debemos confundir «todo intervalo contiene elementos del conjunto» con «algún intervalo está contenido en el conjunto». La primera condición es densidad; la segunda, existencia de interior no vacío.

---

Las definiciones y leyes topológicas básicas de la recta quedan así conectadas con su orden y con la copia racional construida en la Parte I. La sección se apoya exclusivamente en las condiciones con bolas y en los teoremas racionales ya cerrados: no utiliza la caracterización secuencial condicional de §15.8, no introduce espacios topológicos abstractos y no exige una elección de puntos para una familia de intervalos.

El Capítulo 16 utilizará esta estructura local para estudiar los límites de funciones. Su punto de partida será un punto de acumulación del dominio: allí se examinará el comportamiento de los valores de una función cuando la variable se aproxima al punto **sin exigir que coincida con él**. La distinción entre adherencia y acumulación construida aquí evitará imponer un límite donde sólo existe una pertenencia aislada.
