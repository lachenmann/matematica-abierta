## 15.1. Bolas abiertas y vecindades {#sec-ta-15-1}

### Definición 15.1.1 — Bola abierta en la recta

Fijados un **centro** $a\in\mathbb R$ y un **radio** $r\in\mathbb R$ estrictamente positivo, definimos la *bola abierta de centro $a$ y radio $r$* como el subconjunto de la recta

$$
\boxed{B_r(a):=\{x\in\mathbb R:|x-a|<r\}.}
$$

La existencia de este conjunto se obtiene por Separación sobre $\mathbb R$: el valor absoluto y la relación de orden ya están definidos. La condición $r>0$ es parte de la definición y no se omitirá. En particular, $B_0(a)$ **no** queda definido por esta notación; si alguna vez necesitamos un radio nulo, habrá que extenderla explícitamente.

La palabra «abierta» es aquí el nombre tradicional de la bola. **Todavía no se ha definido qué significa que un subconjunto arbitrario de $\mathbb R$ sea abierto**; más adelante demostraremos que las bolas satisfacen esa definición. Tampoco confundimos $B_r(a)$, que es un conjunto, con el número real $|x-a|$, que determina la pertenencia de cada punto.

> **Pregunta de lectura.** ¿Pertenecen a $B_r(a)$ los dos puntos cuya distancia al centro es exactamente $r$? No: la desigualdad definitoria es estricta. El siguiente resultado convierte esta observación en una identidad de conjuntos.

### Proposición 15.1.2 — Las bolas son intervalos abiertos centrados

Para todo $a\in\mathbb R$ y todo $r>0$ se cumplen las siguientes afirmaciones:

$$
\boxed{B_r(a)=(a-r,a+r),}
$$

$$
\boxed{a\in B_r(a),}
$$

y, si $0<s\le r$,

$$
\boxed{B_s(a)\subseteq B_r(a).}
$$

**Demostración.**

Sea $x\in\mathbb R$ y escribamos $u=x-a$. Por la definición del valor absoluto Definición 4.2.1 — Valor absoluto, $|u|=\max\{u,-u\}$. En un orden total, el máximo de dos números es menor que $r$ si y sólo si ambos lo son. Así,

$$
\begin{aligned}
|x-a|<r
&\iff x-a<r\ \text{y}\ -(x-a)<r\\
&\iff -r<x-a<r\\
&\iff a-r<x<a+r\\
&\iff x\in(a-r,a+r).
\end{aligned}
$$

La última equivalencia usa exactamente la definición previa de intervalo abierto Definición 4.3.1 — Intervalos acotados. Como los dos conjuntos tienen los mismos elementos, el criterio extensional Teorema 0.2.4 — Criterio extensional por doble inclusión —o la extensionalidad de los conjuntos fijada en el fundamento— da $B_r(a)=(a-r,a+r)$. El resultado Proposición 4.3.3 — Intervalos centrados y valor absoluto ya estableció la versión con extremos **incluidos** y desigualdad no estricta; aquí no intercambiamos ambas versiones.

Además, $|a-a|=0<r$, de modo que $a\in B_r(a)$. Finalmente, si $0<s\le r$ y $x\in B_s(a)$, entonces $|x-a|<s\le r$, lo que prueba $x\in B_r(a)$. Concluyen las tres afirmaciones. ∎

> **Interpretación.** Una bola de la recta no es un objeto distinto de los intervalos que ya construimos: es un intervalo expresado mediante centro y radio. La ventaja de la descripción métrica es que se transportará con facilidad a argumentos de proximidad y, posteriormente, a otros espacios.

### Proposición 15.1.3 — Una bola contiene una bola alrededor de cada uno de sus puntos

Sean $a\in\mathbb R$, $r>0$ y $y\in B_r(a)$. Entonces el número

$$
\rho:=r-|y-a|
$$

es estrictamente positivo y satisface

$$
\boxed{B_\rho(y)\subseteq B_r(a).}
$$

**Demostración.**

La pertenencia $y\in B_r(a)$ significa $|y-a|<r$. Por compatibilidad del orden con la suma y la resta, $\rho=r-|y-a|>0$; por tanto, $B_\rho(y)$ está definida legítimamente.

Tomemos un punto arbitrario $z\in B_\rho(y)$. La desigualdad triangular Teorema 4.2.3 — Desigualdad triangular, aplicada a $(z-y)+(y-a)=z-a$, da

$$
\begin{aligned}
|z-a|
&\le |z-y|+|y-a|\\
&<\rho+|y-a|\\
&=r.
\end{aligned}
$$

Luego $z\in B_r(a)$. Como $z$ era arbitrario, se obtiene la inclusión. ∎

La elección del radio no ha sido arbitraria ni simultánea para una familia de puntos: para cada $y$ se dispone de la fórmula explícita $r-|y-a|$. Este hecho elemental será la herramienta principal para verificar que las bolas son conjuntos abiertos cuando esa noción se introduzca.

### Definición 15.1.4 — Vecindad de un punto

Sea $a\in\mathbb R$. Un conjunto $V\subseteq\mathbb R$ se denomina **vecindad de $a$** si contiene alguna bola abierta centrada en $a$; es decir,

$$
\boxed{V\text{ es vecindad de }a
\iff\exists r\in\mathbb R\;(r>0\ \text{y}\ B_r(a)\subseteq V).}
$$

No exigimos que $V$ sea una bola ni, por ahora, que sea un conjunto abierto: sólo debe contener un margen positivo alrededor de $a$. En particular, la pertenencia aislada $a\in V$ no basta para que $V$ sea vecindad de $a$. Esta distinción será indispensable al definir puntos interiores.

La noción está tipada sobre subconjuntos de la recta; si se necesita el conjunto de todas las vecindades de un punto fijo, puede obtenerse por Separación dentro de $\mathcal P(\mathbb R)$. No introducimos todavía un símbolo nuevo para tal familia.

### Proposición 15.1.5 — Propiedades elementales de las vecindades

Sea $a\in\mathbb R$. Se cumplen las siguientes propiedades:

1. Toda bola $B_r(a)$, con $r>0$, es una vecindad de $a$.
2. Toda vecindad de $a$ contiene a $a$.
3. Si $V$ es vecindad de $a$ y $V\subseteq W\subseteq\mathbb R$, entonces $W$ también es vecindad de $a$.
4. Si $V$ y $W$ son vecindades de $a$, también lo es $V\cap W$.

**Demostración.**

Para (1), la propia bola $B_r(a)$ proporciona el testigo de radio $r$: por reflexividad de la inclusión, $B_r(a)\subseteq B_r(a)$. Para (2), la definición de vecindad proporciona algún $r>0$ con $B_r(a)\subseteq V$. Por Proposición 15.1.2 — Las bolas son intervalos abiertos centrados, $a\in B_r(a)$; así, $a\in V$.

En (3) conservamos el mismo testigo $r$ de la vecindad $V$. La transitividad de la inclusión produce $B_r(a)\subseteq V\subseteq W$ y, por definición, $W$ es vecindad.

Para (4), de que $V$ y $W$ son vecindades obtenemos **dos** testigos $r,s>0$, tales que $B_r(a)\subseteq V$ y $B_s(a)\subseteq W$. Definamos $t:=\min\{r,s\}$, cuyo significado y unicidad provienen del orden total y de la teoría de mínimos ya establecida. Como $r>0$ y $s>0$, también $t>0$; además, $t\le r$ y $t\le s$. La inclusión entre bolas concéntricas de Proposición 15.1.2 — Las bolas son intervalos abiertos centrados da

$$
B_t(a)\subseteq B_r(a)\cap B_s(a)\subseteq V\cap W.
$$

Por tanto $V\cap W$ contiene una bola de radio positivo centrada en $a$ y es una vecindad de $a$. La prueba elimina únicamente dos cuantificadores existenciales finitos y no introduce ningún axioma de elección. ∎

> **No-ejemplo.** El conjunto $\{a\}$ contiene su único punto, pero no es vecindad de $a$: para cualquier $r>0$, el punto $a+r/(1+1)$ es distinto de $a$ y pertenece a $B_r(a)$, por lo que ninguna bola centrada en $a$ está contenida en el singleton. Aquí $1+1$ y su inverso son operaciones del cuerpo real; no se identifica ningún natural con un real por inclusión literal.

Las vecindades formalizan así una exigencia más fuerte que la mera pertenencia: deben proporcionar un margen completo de puntos alrededor del centro. La siguiente unidad utilizará esta distinción para definir **puntos interiores y conjuntos abiertos** sin circularidad.
