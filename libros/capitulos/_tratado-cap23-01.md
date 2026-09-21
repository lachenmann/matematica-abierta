## 23.1. Dos órdenes de cuantificadores {#sec-ta-23-1}

### Definición 23.1.1 — Sucesión de funciones reales sobre un dominio común
Fijemos un conjunto $E\subseteq\mathbb R$, posiblemente vacío. Por Definición §0.6.11 — Conjunto de funciones y Proposición §0.6.12 — Existencia de $B^A$, existe el conjunto $\mathbb R^E$ de todas las funciones de dominio **exacto** $E$ y codominio $\mathbb R$. Una **sucesión de funciones reales sobre $E$** es una función

$$
\mathbf f:\mathbb N\longrightarrow\mathbb R^E,
\qquad n\longmapsto f_n:=\mathbf f(n).
\tag{23.1.1}
$$

Por consiguiente, para todo $n\in\mathbb N$ está determinada una función $f_n:E\to\mathbb R$. La familia $\mathbf f$ pertenece a $(\mathbb R^E)^{\mathbb N}$; no es su conjunto de valores, y dos términos iguales en diferentes índices siguen teniendo lugares distintos en la sucesión. Se trata de una única función ya dada, no de la instrucción de escoger arbitrariamente una función para cada natural. En este capítulo, la expresión $(f_n)_{n\in\mathbb N}$ es una escritura de $\mathbf f$, no una nueva estructura.

Cuando comparemos $\mathbf f$ con una función límite $f$, exigiremos siempre $f:E\to\mathbb R$ con **el mismo dominio y codominio**. No se entenderá que los dominios de los $f_n$ puedan variar sin una construcción adicional.

### Proposición 23.1.2 — Evaluación en un punto y sucesión real inducida
Sea $\mathbf f:\mathbb N\to\mathbb R^E$ una sucesión de funciones y sea $x\in E$ un punto fijo. Entonces existe una única sucesión real $a^{(x)}:\mathbb N\to\mathbb R$ que satisface

$$
\boxed{a^{(x)}_n=f_n(x)\qquad(n\in\mathbb N).}
\tag{23.1.2}
$$

**Demostración.**
Por (23.1.1), cada $f_n$ es función con dominio $E$; de $x\in E$ se sigue que existe un único $r\in\mathbb R$ igual a $f_n(x)$. El producto $\mathbb N\times\mathbb R$ existe (Proposición §0.3.7 — Existencia del producto cartesiano), por lo que Separación determina el conjunto

$$
G_x:=\{\langle n,r\rangle\in\mathbb N\times\mathbb R:r=f_n(x)\}.
$$

La existencia y unicidad para cada $n$ hacen de $G_x$ el grafo de una función de dominio exacto $\mathbb N$ y codominio $\mathbb R$. Es una sucesión real en el sentido de Definición §13.1.1 — Sucesión real, y la igualdad de grafos, dominios y codominios (Proposición §0.6.3 — Criterio de igualdad de funciones) demuestra su unicidad. No se escogió ningún valor: todos proceden de evaluaciones únicas de funciones dadas. $\square$

**Lectura.** Fijar $x$ transforma una sucesión de funciones en una sucesión de números; todavía no relaciona entre sí las etapas necesarias para puntos distintos.

### Definición 23.1.3 — Convergencia puntual
Sean $\mathbf f=(f_n)_{n\in\mathbb N}$ una sucesión de funciones sobre $E$ y $f:E\to\mathbb R$. Diremos que $f_n$ **converge puntualmente a $f$ en $E$** si, para todo $x\in E$, la sucesión real (23.1.2) converge a $f(x)$ en el sentido de Definición §13.3.1 — Convergencia de una sucesión real. En cuantificadores explícitos:

$$
\boxed{\forall x\in E\;\forall\varepsilon>0\;
\exists N\in\mathbb N\;\forall n\in\mathbb N\;
\bigl(n\ge N\Rightarrow |f_n(x)-f(x)|<\varepsilon\bigr).}
\tag{23.1.3}
$$

En estas fórmulas, $\varepsilon>0$ significa que $\varepsilon$ recorre los reales positivos. También escribiremos en el alcance de esta definición $f_n(x)\to f(x)$ para cada $x\in E$. Una escritura abreviada $f_n\to f$ **sin calificativo** queda descartada para evitar confusión con el modo uniforme.

En (23.1.3), el testigo $N$ puede depender tanto de $x$ como de $\varepsilon$. Esta definición **no produce** automáticamente una función que elija un índice $N(x,\varepsilon)$ para todos los pares: no necesitamos esa selección y no la postulamos.

### Proposición 23.1.4 — Unicidad del límite puntual como función tipada
Si $f,g:E\to\mathbb R$ son dos límites puntuales de la misma sucesión $\mathbf f$, entonces $f=g$ como funciones.

**Demostración.**
Tomemos $x\in E$ arbitrario. La sucesión real única $a^{(x)}=(f_n(x))$ de Proposición §23.1.2 — Evaluación en un punto y sucesión real inducida converge a $f(x)$ y a $g(x)$ por hipótesis. La unicidad del límite real Teorema §13.3.5 — Unicidad del límite real implica $f(x)=g(x)$. Así, ambas funciones coinciden punto por punto; como también tienen el mismo dominio $E$ y codominio $\mathbb R$, el criterio Proposición §0.6.3 — Criterio de igualdad de funciones concluye $f=g$. Si $E=\varnothing$, la igualdad resulta igualmente del grafo vacío y los tipos comunes, sin evaluar un punto inexistente. $\square$

### Definición 23.1.5 — Convergencia uniforme
Con los mismos tipos, diremos que $f_n$ **converge uniformemente a $f$ en $E$** si

$$
\boxed{\forall\varepsilon>0\;
\exists N\in\mathbb N\;\forall n\in\mathbb N\;\forall x\in E\;
\bigl(n\ge N\Rightarrow |f_n(x)-f(x)|<\varepsilon\bigr).}
\tag{23.1.4}
$$

El índice $N$ depende de la tolerancia, **pero no del punto**. La definición es válida para un $E$ no acotado o vacío: no presupone la existencia de $\sup_{x\in E}|f_n(x)-f(x)|$, que podría no existir como real finito. En el caso $E=\varnothing$, (23.1.3) y (23.1.4) son vacuamente verdaderas para la única función de dominio vacío y codominio real.

Las expresiones «puntual» y «uniforme» nombran relaciones entre una sucesión de funciones, un candidato a límite y un **dominio especificado**. La convergencia uniforme en un subconjunto no implica, por pura definición, uniformidad sobre un conjunto mayor.

### Proposición 23.1.6 — La convergencia uniforme implica la puntual
Sean $\mathbf f$ y $f$ como antes. Si $f_n$ converge uniformemente a $f$ en $E$, entonces converge puntualmente a $f$ en $E$.

**Demostración.**
Sea $x\in E$ arbitrario y sea $\varepsilon>0$. La uniformidad (23.1.4) proporciona un natural $N$ tal que **para todos** $n\ge N$ y **todos** $y\in E$ se tiene $|f_n(y)-f(y)|<\varepsilon$. En particular, poniendo $y=x$, obtenemos la estimación requerida para la convergencia de la sucesión real $a^{(x)}$ hacia $f(x)$. Como $x$ y $\varepsilon$ eran arbitrarios, vale (23.1.3). Si $E=\varnothing$, la conclusión se satisface directamente por vacuidad. $\square$

La implicación inversa requeriría intercambiar $\forall x\in E$ con $\exists N$. No existe una regla lógica general que permita ese intercambio: el ejemplo siguiente muestra por qué no es un teorema de análisis.

### Proposición 23.1.7 — Contraejemplo: potencias puntualmente convergentes sin convergencia uniforme
En $E=[0,1]$ consideremos las funciones tipadas $f_n:E\to\mathbb R$ definidas, para cada $n\in\mathbb N$, por

$$
f_n(x):=x^n,
\qquad x\in[0,1],
\tag{23.1.5}
$$

donde la potencia natural está construida en Definición §14.3.1 — Potencias naturales de un número real y, por esa misma definición, $0^0=1$. La expresión determina una sucesión de funciones: el grafo de cada $f_n$ es el subconjunto definible de $E\times\mathbb R$ dado por $r=x^n$, y el grafo de $n\mapsto f_n$ se obtiene por Separación en el conjunto existente $\mathbb N\times\mathbb R^E$, utilizando la operación total de potencia. Su límite puntual es

$$
\boxed{f(x)=\begin{cases}0,&0\le x<1,\\1,&x=1.\end{cases}}
\tag{23.1.6}
$$

La sucesión **no** converge uniformemente a $f$ sobre $[0,1]$; además, cada $f_n$ es continua en el intervalo y $f$ no es continua en $1$.

**Demostración.**
**Convergencia puntual.** Si $x=1$, se cumple $f_n(1)=1$ para todo $n$, así que la sucesión numérica es constante y converge a $1$. Si $0\le x<1$, entonces $|x|<1$ y Teorema §14.3.4 — Las potencias de una base de módulo menor que uno tienden a cero demuestra que $x^n\to0$. Por Definición §23.1.3 — Convergencia puntual, estos dos casos prueban que el límite puntual es exactamente la función (23.1.6); su unicidad está cubierta por Proposición §23.1.4 — Unicidad del límite puntual como función tipada.

**Cota elemental.** Demostremos por inducción natural, para cada $u\in[0,1]$ fijo y $m\in\mathbb N$, la desigualdad de Bernoulli

$$
(1-u)^m\ge 1-\nu_{\mathbb R}(m)u.
\tag{23.1.7}
$$

En $m=0$, ambos lados valen $1$. Si vale para $m$, como $1-u\ge0$, al multiplicar y desarrollar obtenemos

$$
(1-u)^{m+1}\ge(1-\nu_{\mathbb R}(m)u)(1-u)
=1-\nu_{\mathbb R}(m+1)u+\nu_{\mathbb R}(m)u^2
\ge 1-\nu_{\mathbb R}(m+1)u.
$$

El último paso utiliza $\nu_{\mathbb R}(m)\ge0$ y $u^2\ge0$. Queda probado (23.1.7) para todos los naturales, sin elegir una familia de testigos.

**Falla de uniformidad.** Supongamos (23.1.4) y fijemos $\varepsilon=1/4$. Sea $N$ el índice que proporcionaría esa condición. Tomemos explícitamente $n:=N+1$ —entonces $n\ge N$ y $n\ge1$— y el punto

$$
x_n:=1-\frac{1}{2\nu_{\mathbb R}(n)}\in[1/2,1).
$$

La división es legítima, pues $\nu_{\mathbb R}(n)>0$. En particular, $f(x_n)=0$. La estimación (23.1.7), aplicada a $u=1/(2\nu_{\mathbb R}(n))$, proporciona

$$
|f_n(x_n)-f(x_n)|=x_n^n
\ge 1-\nu_{\mathbb R}(n)\frac{1}{2\nu_{\mathbb R}(n)}
=\frac12>\frac14.
\tag{23.1.8}
$$

Esto contradice la exigencia de que **todos** los puntos satisfagan un error estrictamente menor que $1/4$ a partir de $N$. No hay convergencia uniforme.

**Continuidad.** Para cada $n$ fijo, $x\mapsto x^n$ es una función polinómica, continua por Teorema §17.5.3 — Todo polinomio real es continuo en la recta (y por restricción al intervalo). La función $f$, en cambio, toma el valor $1$ en el extremo $1$ y el valor $0$ en todo punto de $[0,1)$. Para cualquier radio $\delta>0$, el punto explícito $x=1-\frac12\min\{\delta,1\}$ pertenece a $[0,1)$, satisface $|x-1|<\delta$, pero $|f(x)-f(1)|=1>1/2$. La definición relativa de continuidad Definición §17.1.1 — Continuidad relativa al dominio en un punto fracasa en $1$. $\square$

**Interpretación.** Fijado un punto $x<1$, las potencias acaban por hacerse pequeñas; sin embargo, a medida que crece el índice podemos desplazarnos hacia $1$ y encontrar puntos donde el error continúa siendo grande. En convergencia puntual no hay obligación de controlar esos puntos **móviles** con un mismo índice. La pérdida de continuidad demuestra que esa distinción tiene consecuencias matemáticas y prepara el problema de §23.3.

**Contraste con un caso uniforme.** Para $h_n:[0,1]\to\mathbb R$, $h_n(x)=x/\nu_{\mathbb R}(n+1)$, vale $|h_n(x)|\le1/\nu_{\mathbb R}(n+1)$ para todo $x$. Dada $\varepsilon>0$, la propiedad arquimediana de los reales (Teorema §4.6.3 — Todo cuerpo ordenado completo es arquimediano) suministra $N\in\mathbb N$ con $\nu_{\mathbb R}(N+1)>1/\varepsilon$; para $n\ge N$, la monotonía de los numerales implica $1/\nu_{\mathbb R}(n+1)<\varepsilon$. El mismo $N$ sirve para todos los puntos; así $h_n\to0$ uniformemente. En ninguno de los ejemplos se ha supuesto que los puntos de máxima desviación existan o que puedan elegirse globalmente.

**Transición.** Hasta aquí la sucesión posee un límite candidato y comparamos dos formas de aproximarlo. El próximo paso será formular un criterio de Cauchy directamente uniforme —sin conocer de antemano el límite— y demostrar su equivalencia con la convergencia uniforme usando la completitud de $\mathbb R$ sin elección numerable oculta.
