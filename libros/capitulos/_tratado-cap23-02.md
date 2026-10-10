## 23.2. Criterio uniforme de Cauchy {#sec-ta-23-2}

La definición de convergencia uniforme de §23.1 compara cada término con una función límite ya conocida. El criterio que sigue sólo compara entre sí términos suficientemente avanzados. Su fuerza reside en exigir un mismo índice para todos los argumentos; la existencia de la función límite será una conclusión, no una premisa encubierta.

### Definición 23.2.1 — Sucesión uniformemente de Cauchy
Sea $E\subseteq\mathbb R$, posiblemente vacío, y sea $\mathbf f=(f_n)_{n\in\mathbb N}:\mathbb N\to\mathbb R^E$ una sucesión de funciones. Diremos que $\mathbf f$ es uniformemente de Cauchy sobre $E$ si

$$
\boxed{\forall\varepsilon>0\;\exists N\in\mathbb N\;
\forall n,m\in\mathbb N\;\forall x\in E:\quad
(n\ge N\ \land\ m\ge N)\Longrightarrow
|f_n(x)-f_m(x)|<\varepsilon.}
\tag{23.2.1}
$$

Los índices $n,m$ varían independientemente; el mismo umbral $N$ sirve para todos los pares de términos de la cola y todos los puntos de $E$. No exigimos que $E$ sea compacto o acotado, ni definimos un supremo de errores que pudiera carecer de valor real finito. Para $E=\varnothing$, la condición es verdadera por vacuidad; trataremos también ese caso al construir el límite.

La condición de Cauchy numérica Definición §13.8.1 — Sucesión real de Cauchy se obtiene de (23.2.1) fijando un punto $x$, pero la recíproca de esa observación no queda autorizada: los índices numéricos podrían depender del punto.

### Proposición 23.2.2 — Toda sucesión uniformemente convergente es uniformemente de Cauchy
Si $f_n:E\to\mathbb R$ converge uniformemente a $f:E\to\mathbb R$, entonces $(f_n)$ es uniformemente de Cauchy en $E$.

**Demostración.**
Dado $\varepsilon>0$, la convergencia uniforme aplicada a $\varepsilon/2$ proporciona $N\in\mathbb N$ tal que

$$
|f_k(x)-f(x)|<\frac\varepsilon2
\quad\text{para todo }k\ge N\text{ y todo }x\in E.
$$

Tomemos ahora $n,m\ge N$ y $x\in E$ cualesquiera. Por la desigualdad triangular Teorema §4.2.3 — Desigualdad triangular y la simetría del valor absoluto,

$$
\begin{aligned}
|f_n(x)-f_m(x)|
&\le |f_n(x)-f(x)|+|f(x)-f_m(x)|\\
&<\frac\varepsilon2+\frac\varepsilon2=\varepsilon.
\end{aligned}
$$

El índice $N$ inicial no cambió con $n$, $m$ ni $x$; esto es exactamente (23.2.1). Si $E$ es vacío, la conclusión es inmediata por vacuidad. $\square$

### Lema 23.2.3 — Construcción de un único límite puntual desde la condición uniforme de Cauchy
Sea $\mathbf f:\mathbb N\to\mathbb R^E$ uniformemente de Cauchy. Existe una única función tipada $f:E\to\mathbb R$ tal que $f_n$ converge puntualmente a $f$ en $E$.

**Demostración.**
**Primero, un punto arbitrario.** Fijemos $x\in E$ y una tolerancia $\varepsilon>0$. El índice $N$ de (23.2.1) satisface

$$
|f_n(x)-f_m(x)|<\varepsilon\qquad(n,m\ge N).
$$

La sucesión real $a^{(x)}=(f_n(x))$, construida en Proposición §23.1.2 — Evaluación en un punto y sucesión real inducida, es pues de Cauchy en el sentido de Definición §13.8.1 — Sucesión real de Cauchy. El teorema de completitud secuencial Teorema §13.8.7 — Toda sucesión real de Cauchy converge asegura que existe $\ell\in\mathbb R$ con $f_n(x)\to\ell$. Su unicidad se sigue de Teorema §13.3.5 — Unicidad del límite real. Por tanto, para cada $x\in E$ existe exactamente un real $\ell$ que es límite de $(f_n(x))$; la afirmación es universal y no especifica ni solicita una elección de testigos para diferentes puntos.

**Segundo, una función y no sólo una correspondencia informal.** El producto $E\times\mathbb R$ existe porque ambos factores son conjuntos. Mediante Separación formamos

$$
G:=\bigl\{\langle x,r\rangle\in E\times\mathbb R:\
\forall\varepsilon>0\;\exists N\in\mathbb N\;\forall n\ge N,
\ |f_n(x)-r|<\varepsilon\bigr\}.
\tag{23.2.2}
$$

El predicado de la derecha es una fórmula conjuntista con la sucesión dada como parámetro. La existencia y unicidad del límite numérico para cada $x$ hacen que $G$ sea el grafo de una función $f$ con dominio exacto $E$ y codominio $\mathbb R$. Su definición establece (23.1.3), y por ello $f_n$ converge puntualmente a $f$. Cualquier otra función tipada con la misma propiedad coincide con $f$ por Proposición §23.1.4 — Unicidad del límite puntual como función tipada.

Si $E=\varnothing$, el producto y el grafo son vacíos: existe una única función de dominio vacío y codominio $\mathbb R$, y la convergencia puntual se cumple por vacuidad. Este caso no requiere tomar un $x\in E$ inexistente. $\square$

**Alcance lógico.** Del enunciado $\forall x\in E\;\exists!\ell\in\mathbb R$ obtenemos la función por un predicado de valor único, no por una selección arbitraria $x\mapsto\ell_x$. La completitud se aplica a cada sucesión numérica ya definida; no se introduce $CC(\mathbb R)$.

### Teorema 23.2.4 — Criterio uniforme de Cauchy
Para cualquier $E\subseteq\mathbb R$ y cualquier sucesión $\mathbf f:\mathbb N\to\mathbb R^E$, son equivalentes:

1. existe una función $f:E\to\mathbb R$ tal que $f_n\to f$ uniformemente en $E$;
2. la sucesión $(f_n)$ satisface la condición uniforme de Cauchy (23.2.1).

Cuando estas condiciones se cumplen, la función límite uniforme es única.

**Demostración.**
La implicación 1 $\Rightarrow$ 2 es Proposición §23.2.2 — Toda sucesión uniformemente convergente es uniformemente de Cauchy.

Para 2 $\Rightarrow$ 1, Lema §23.2.3 — Construcción de un único límite puntual desde la condición uniforme de Cauchy proporciona una función $f:E\to\mathbb R$ construida por su grafo y tal que, para cada $x\in E$, la sucesión $f_n(x)$ converge a $f(x)$. Resta demostrar la uniformidad: la convergencia puntual, por sí sola, no bastaría.

Fijemos $\varepsilon>0$. La condición (23.2.1), aplicada a $\varepsilon/2$, da un único umbral $N\in\mathbb N$ tal que

$$
|f_n(x)-f_m(x)|<\frac\varepsilon2
\qquad(n,m\ge N,\ x\in E).
\tag{23.2.3}
$$

Sean ahora $n\ge N$ y $x\in E$ arbitrarios. La convergencia numérica de $f_k(x)$ hacia $f(x)$, con la tolerancia $\varepsilon/2$, suministra un índice $M\in\mathbb N$ para este punto fijo. Definamos expresamente $m:=\max\{N,M\}$. Así $m\ge N$ y $m\ge M$, luego (23.2.3), la convergencia puntual y la desigualdad triangular dan

$$
\begin{aligned}
|f_n(x)-f(x)|
&\le |f_n(x)-f_m(x)|+|f_m(x)-f(x)|\\
&<\frac\varepsilon2+\frac\varepsilon2=\varepsilon.
\end{aligned}
\tag{23.2.4}
$$

Es importante el orden de la prueba: $M$ puede depender de $x$, pero sólo se utiliza para establecer la desigualdad correspondiente a ese punto. El umbral final es el mismo $N$, obtenido antes de fijar $n$ y $x$. Por universalización, (23.2.4) vale para todos $n\ge N$ y todos $x\in E$: ésta es la convergencia uniforme (23.1.4). En el caso vacío, el límite del lema anterior es la función vacía tipada y la condición uniforme es vacuamente verdadera.

Si $g:E\to\mathbb R$ fuese otro límite uniforme, Proposición §23.1.6 — La convergencia uniforme implica la puntual aplicado a ambas convergencias daría dos límites puntuales; Proposición §23.1.4 — Unicidad del límite puntual como función tipada implica $g=f$. $\square$

**Lectura de la estrategia.** Completitud proporciona los límites numéricos y unicidad permite ensamblarlos en una función. La condición uniforme de Cauchy hace lo que la mera convergencia puntual no puede hacer: conserva un único umbral al pasar desde las diferencias $f_n-f_m$ a las diferencias $f_n-f$.

**Aplicación al ejemplo anterior.** Las funciones $x\mapsto x^n$ de Proposición §23.1.7 — Contraejemplo: potencias puntualmente convergentes sin convergencia uniforme no son uniformemente de Cauchy sobre $[0,1]$. En efecto, si lo fueran, el teorema les daría un límite uniforme; la proposición Proposición §23.1.6 — La convergencia uniforme implica la puntual y la unicidad Proposición §23.1.4 — Unicidad del límite puntual como función tipada obligarían a que fuese la función discontinua (23.1.6), pero Proposición §23.1.7 — Contraejemplo: potencias puntualmente convergentes sin convergencia uniforme ya probó que no hay convergencia uniforme hacia ella. No hemos usado aquí el teorema todavía pendiente sobre continuidad de límites uniformes.

### Corolario 23.2.5 — Control por dos subconjuntos que cubren el dominio
Supongamos $E=A\cup B\subseteq\mathbb R$, con $A,B\subseteq E$ (se admiten conjuntos vacíos). Una sucesión $f_n:E\to\mathbb R$ es uniformemente de Cauchy en $E$ si y sólo si las sucesiones de restricciones $f_n\upharpoonright A:A\to\mathbb R$ y $f_n\upharpoonright B:B\to\mathbb R$ lo son en sus dominios respectivos. En consecuencia, $(f_n)$ converge uniformemente sobre $E$ si y sólo si ambas sucesiones de restricciones son uniformemente de Cauchy.

**Demostración.**
Por Definición §1.3.1 — Restricción de una función y Proposición §1.3.2 — Existencia y unicidad de la restricción, cada restricción está unívocamente determinada con el dominio indicado y codominio $\mathbb R$. Separación dentro de $\mathbb N\times\mathbb R^A$ y $\mathbb N\times\mathbb R^B$ define las respectivas sucesiones indexadas, sin escoger funciones.

Si $(f_n)$ es uniformemente de Cauchy en $E$, el mismo $N$ de (23.2.1) satisface la condición en $A$ y en $B$, pues ambos son subconjuntos de $E$.

Recíprocamente, fijemos $\varepsilon>0$. Las dos condiciones proporcionan dos índices $N_A,N_B\in\mathbb N$. Pongamos $N:=\max\{N_A,N_B\}$. Para $n,m\ge N$ y $x\in E=A\cup B$, se tiene $x\in A$ o $x\in B$; en el primer caso aplicamos el umbral $N_A$ y en el segundo $N_B$. En ambos casos $|f_n(x)-f_m(x)|<\varepsilon$, independientemente de $x$. Hemos demostrado la equivalencia de Cauchy. Aplicando Teorema §23.2.4 — Criterio uniforme de Cauchy a $E$, a $A$ y a $B$ se deduce la última afirmación. Sólo se combinaron dos testigos mediante un máximo finito, no una familia infinita de elecciones. $\square$

**Transición.** El criterio de Cauchy produce una función límite uniforme sin presuponerla. En §23.3 utilizaremos el umbral común para demostrar que, si los términos son continuos en un punto, también lo es su límite allí. La función discontinua de (23.1.6) quedará entonces excluida como límite uniforme de funciones continuas por una segunda vía, independiente del cálculo explícito del error.
