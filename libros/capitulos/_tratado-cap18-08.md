## 18.8. Preservación de la conexidad por aplicaciones continuas {#sec-ta-18-8}

El criterio anterior identifica los conjuntos conexos de la recta por su ausencia de huecos. Ahora estableceremos una propiedad de transporte: una función continua no puede producir una separación de su imagen cuando el conjunto de partida carece de separaciones. La demostración debe distinguir cuidadosamente los abiertos relativos a la imagen de los abiertos relativos al dominio: la continuidad proporciona estos últimos mediante preimágenes, no mediante una identificación de los dos ambientes.

### Teorema 18.8.1 — La imagen continua de un conexo es conexa
Sean $D\subseteq\mathbb R$, $f:D\to\mathbb R$ una función continua en todos los puntos de $D$ y $E\subseteq D$ un conjunto conexo. Entonces su imagen directa

$$
\boxed{H:=f[E]=\{y\in\mathbb R:\exists x\in E,\ f(x)=y\}\quad\text{es conexa}.}
$$

El conjunto $E$ puede ser vacío y no se exige que sea compacto, cerrado ni acotado. La función $f$ conserva el codominio $\mathbb R$; $H$ es su imagen de $E$, no un cambio tácito de codominio.

**Demostración.**
**1. Restricción y supuesta separación de la imagen.** Por Definición §1.3.1 — Restricción de una función existe la restricción tipada $h:=f\upharpoonright E:E\to\mathbb R$. Es continua en todos los puntos de $E$ por Corolario §17.4.6 — Clausura global, restricciones y cocientes y satisface $h[E]=f[E]=H$. Si $E=\varnothing$, entonces $H=\varnothing$, conexo por Definición §18.7.1 — Separación relativa y conjunto conexo; en adelante también podemos proceder por contradicción sin excluir ese caso.

Supongamos que $H$ no es conexo. Por Definición §18.7.1 — Separación relativa y conjunto conexo, existen $A,B\subseteq H$ tales que

$$
A\ne\varnothing,\quad B\ne\varnothing,\quad A\cap B=\varnothing,
\quad H=A\cup B,
$$

siendo ambos abiertos relativos a $H$. La definición Definición §17.3.1 — Abiertos y cerrados relativos a un subconjunto de la recta suministra dos abiertos $V,W\subseteq\mathbb R$ con

$$
A=H\cap V,\qquad B=H\cap W.
$$

No se escogió un abierto para cada punto ni para una familia arbitraria: sólo se instanciaron dos existencias.

**2. Transportamos la separación por preimagen.** Definamos mediante Separación los subconjuntos determinados de $E$

$$
P:=\{x\in E:h(x)\in A\},\qquad
Q:=\{x\in E:h(x)\in B\}.
$$

Dado que $h(x)\in H$ para todo $x\in E$, las igualdades $A=H\cap V$ y $B=H\cap W$ implican exactamente

$$
P=h^{-1}[V],\qquad Q=h^{-1}[W].
$$

Aquí las preimágenes se calculan respecto de la función $h:E\to\mathbb R$. Por el criterio global de continuidad Teorema §17.3.4 — Caracterización global por preimágenes de abiertos, $P$ y $Q$ son abiertos relativos a $E$. No afirmamos que sean abiertos de toda la recta.

Son disjuntos: un $x$ común produciría $h(x)\in A\cap B=\varnothing$. Cubren $E$: para cualquier $x\in E$ tenemos $h(x)\in H=A\cup B$, luego $x\in P\cup Q$. Finalmente, ambos son no vacíos. En efecto, $A\ne\varnothing$ proporciona un único $y_A\in A\subseteq H$ y, por la definición de imagen, un $x_A\in E$ con $h(x_A)=y_A$, por lo que $x_A\in P$. Del mismo modo, $B\ne\varnothing$ proporciona un $x_B\in Q$. Sólo se necesitan dos testigos concretos de fibras, no una función $y\mapsto x_y$ definida sobre $H$.

Así $P,Q$ satisfacen todas las condiciones de una separación de $E$, contradiciendo su conexidad. La supuesta separación de $H$ es imposible; $f[E]$ es conexo. $\square$

**Lectura de la demostración.** Una separación de valores produciría una separación de argumentos. La continuidad garantiza que las dos partes inversas son relativamente abiertas; la sobreyectividad de $h$ sobre su imagen como relación de valores, que se usa sólo elemento a elemento, asegura que ambas partes tienen puntos. No es necesario construir una nueva función $E\to H$ ni seleccionar simultáneamente preimágenes de todos los valores.

### Corolario 18.8.2 — La imagen continua de un intervalo es un intervalo
Sea $f:D\to\mathbb R$ continua en $D$ y sea $I\subseteq D$ un intervalo, en el sentido de Definición §18.7.3 — Intervalo como subconjunto convexo para el orden. Entonces $f[I]$ es un intervalo de la recta, incluso si $I$ es vacío o consta de un único punto.

**Demostración.**
Por Corolario §18.7.6 — Caracterización exacta de los conexos reales, el intervalo $I$ es conexo. El Teorema 18.8.1, aplicado a $f$ e $I\subseteq D$, afirma que $f[I]$ es conexo. La otra dirección de Corolario §18.7.6 — Caracterización exacta de los conexos reales establece que $f[I]$ es intervalo. La imagen existe por Definición §0.6.9 — Imagen y preimagen y se entiende como subconjunto de $\mathbb R$; no se modifican los tipos de $f$. Si $I=\varnothing$, su imagen es vacía; si $I$ es singleton, su imagen es singleton, y ambos satisfacen la definición de intervalo. $\square$

**Precisión sobre la dirección de la implicación.** La preimagen de un conjunto conexo no tiene por qué ser conexa, aunque la función y su dominio lo sean. Por ejemplo, sea $p:[-2,2]\to\mathbb R$, $p(x)=x^2$, restricción de una función polinomial continua por §17.5. Entonces $\{1\}$ es conexo, mientras que

$$
p^{-1}[\{1\}]=\{-1,1\}
$$

no es intervalo y, por Corolario §18.7.6 — Caracterización exacta de los conexos reales, no es conexo. No invertiremos indebidamente el teorema de preservación.

**Transición.** El corolario prueba que la imagen de un intervalo no omite ningún valor comprendido entre dos de sus valores. En §18.9 formularemos esa consecuencia cuantificada como teorema del valor intermedio, distinguiendo el caso general de intervalos y la formulación habitual para $[a,b]$. El resultado de §18.8 será su premisa y no su conclusión anticipada.
