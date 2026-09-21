## 24.5. Convergencia uniforme en los intervalos interiores y continuidad de la suma {#sec-ta-24-5}

La convergencia absoluta obtenida en §24.2 es una propiedad de cada evaluación por separado. Para pasar a convergencia uniforme fijaremos primero **un conjunto de puntos**, encontraremos una sola evaluación convergente a distancia mayor que todas las distancias de ese conjunto y construiremos una sucesión mayorante que no dependa del punto variable. Esta estrategia reutiliza el criterio $M$ del Capítulo 23: no se invoca una supuesta regla automática «convergencia puntual implica uniforme».

### Teorema 24.5.1 — Convergencia absoluta uniforme y cota geométrica del resto
Sean $a:\mathbb N\to\mathbb R$ y $c\in\mathbb R$, con radio $R:=R(a,c)$. Supongamos **una** de estas condiciones: (i) $R\in\mathbb R$ y $R>0$, con $0\le r<R$; o (ii) $R=+\infty$ (marca formal), con un real arbitrario $r\ge0$. Sea

$$
K_r:=[c-r,c+r]\subseteq\mathbb R.
\tag{24.5.1}
$$

La serie de restricciones $p_n^{a,c}\upharpoonright K_r:K_r\to\mathbb R$ converge **absoluta y uniformemente** sobre $K_r$ a la restricción $F_{a,c}\upharpoonright K_r$. Más precisamente, existen reales $M>0$ y $q$ con $0\le q<1$, independientes de $n$ y de $x\in K_r$, tales que

$$
\boxed{|a_n(x-c)^n|\le Mq^n
\qquad(n\in\mathbb N,\ x\in K_r).}
\tag{24.5.2}
$$

Para toda suma parcial de índice $N\in\mathbb N$, la función suma satisface la **cota uniforme de error**

$$
\boxed{\forall x\in K_r:\quad
|F_{a,c}(x)-S_N^{a,c}(x)|\le
\frac{Mq^{N+1}}{1-q}.}
\tag{24.5.3}
$$

La expresión $q^0$ conserva la convención $0^0=1$; en (24.5.3) el exponente $N+1\ge1$, por lo que, si $q=0$, el lado derecho es cero.

**Demostración.**
**1. Una distancia convergente mayor que $r$.** En el caso de radio finito positivo, $r<R=\sup D(a,c)$ no es cota superior de $D(a,c)$; existe por tanto $d\in D(a,c)$ con $d>r$. Si el radio es infinito, $D(a,c)$ no está acotado superiormente por definición y obtenemos igualmente $d\in D(a,c)$ con $d>r$. En cualquiera de los casos, la definición de $D(a,c)$ proporciona **un solo punto** $y\in C(a,c)$ con $|y-c|=d>r\ge0$. Por consiguiente $y\ne c$ y $d>0$. No hemos seleccionado testigos simultáneamente para todos los radios.

**2. Mayoración válida en todos los puntos.** Como la serie numérica $\sum a_n(y-c)^n$ converge, «Acotación de los términos al converger una serie numérica» proporciona un único $M>0$ tal que $|a_n(y-c)^n|\le M$ para todo $n$. Fijemos

$$
q:=\frac r d,\qquad 0\le q<1.
\tag{24.5.4}
$$

Si $x\in K_r$, entonces $|x-c|\le r$. La identidad de potencias (24.1.13), la multiplicatividad del valor absoluto y $d>0$ permiten escribir, para cada natural $n$,

$$
\begin{aligned}
|a_n(x-c)^n|
&=|a_n(y-c)^n|\left|\frac{x-c}{y-c}\right|^n\\
&\le M\left(\frac{|x-c|}{d}\right)^n
\le Mq^n.
\end{aligned}
\tag{24.5.5}
$$

La última desigualdad se obtiene por inducción en $n$ de la monotonía de las potencias de bases no negativas; también vale para $n=0$, cuando ambas potencias son $1$. Los dos parámetros $M$ y $q$ se fijaron **antes** de cuantificar sobre los puntos $x\in K_r$.

**3. Aplicación del criterio $M$ y reconocimiento del límite.** La sucesión de funciones restringidas está unívocamente determinada por sus grafos y tiene dominio común exacto $K_r$. Definimos la sucesión numérica mayorante $m_n:=Mq^n$; su grafo en $\mathbb N\times\mathbb R$ queda determinado por Separación, sin elecciones. La serie geométrica converge por «Convergencia y suma de la serie geométrica para $», y su producto por $M$ converge con suma $B=M/(1-q)$. La hipótesis del criterio $M$ «Criterio $M$ de Weierstrass y estimación del resto» es precisamente (24.5.2); por tanto la serie restringida converge absoluta y uniformemente hacia una única función $G:K_r\to\mathbb R$. Para cada $x\in K_r$ su serie numérica converge y tiene límite $G(x)$. La construcción previa de $F_{a,c}$ («Existencia y unicidad de la función suma sobre su dominio exacto») y la unicidad del límite real («Unicidad del límite real») implican $G(x)=F_{a,c}(x)$: $K_r\subseteq C(a,c)$ y las dos funciones coinciden en todos sus valores. Por igualdad de grafos tipados, $G=F_{a,c}\upharpoonright K_r$.

**4. Error explícito.** Sean $U_N:=\sum_{n=0}^{N}m_n$. La estimación del resto incluida en «Criterio $M$ de Weierstrass y estimación del resto» proporciona, para todos los $x\in K_r$,

$$
|F_{a,c}(x)-S_N^{a,c}(x)|\le B-U_N.
$$

La identidad finita geométrica, válida también para $q=0$, da $U_N=M(1-q^{N+1})/(1-q)$. Restando esta expresión de $B=M/(1-q)$ resulta exactamente (24.5.3). Como $q^{N+1}\to0$ por «Convergencia y suma de la serie geométrica para $» y la condición necesaria «Condición necesaria de convergencia: el término general tiende a cero» y $M/(1-q)$ es un real fijo, el error mayorante tiende a cero independientemente de $x$. $\square$

**Caso degenerado separado.** Si $R(a,c)=0$, sólo converge la serie en $\{c\}$ («Clasificación por el radio y convergencia interior»). En ese singleton las sumas parciales son idénticamente $a_0$ por «El centro siempre pertenece al conjunto de convergencia»; por eso hay convergencia uniforme trivial en $\{c\}$. No se le atribuye un intervalo interior de longitud positiva ni se inventa un número $r$ con $0<r<R$.

### Corolario 24.5.2 — Uniformidad en conjuntos de distancia uniformemente interior
Bajo las hipótesis sobre el radio del teorema precedente, sea $E\subseteq\mathbb R$ cualquier conjunto tal que **exista un solo real admisible** $r\ge0$ con

$$
\forall x\in E:\quad |x-c|\le r,
\qquad r<R\ \text{si }R\in\mathbb R.
\tag{24.5.6}
$$

La serie de potencias restringida a $E$ converge absoluta y uniformemente a $F_{a,c}\upharpoonright E$. Para ese mismo $r$ se conserva la estimación (24.5.3), con $x\in E$.

**Demostración.**
La condición equivale a la inclusión $E\subseteq K_r=[c-r,c+r]$. Fijamos el testigo $r$ **una vez**. Restringir a $E$ las funciones del teorema y la función límite conserva (24.5.2) y (24.5.3) con los mismos $M,q$, porque toda afirmación para cada $x\in K_r$ vale para cada $x\in E$. El criterio $M$ o directamente la definición de convergencia uniforme suministra el mismo índice para todos los puntos de $E$. Las restricciones poseen grafos únicos; no hay una selección de funciones ni de radios. Si $E=\varnothing$, las desigualdades y la uniformidad se cumplen vacuamente, como permiten las definiciones del Capítulo 23. $\square$

**Precisión sobre los compactos.** La forma de (24.5.6) es la hipótesis empleada en la demostración y no presupone que $E$ sea compacto. Todo compacto no vacío contenido en el intervalo abierto interior satisface esa condición por el teorema del valor extremo «Teorema del valor extremo: Weierstrass» aplicado a $x\mapsto|x-c|$; en el caso de radio infinito basta que el compacto sea acotado. Esta observación no sustituye la prueba de la uniformidad por la mera palabra «compacto».

### Teorema 24.5.3 — Continuidad de la función suma en el interior
Definamos el **dominio interior** $I$ de la serie por casos: si $R:=R(a,c)$ es real positivo, $I:=(c-R,c+R)$; si $R=+\infty$ como marca formal, $I:=\mathbb R$. Entonces $I\subseteq C(a,c)$ y la función

$$
\boxed{F_{a,c}\upharpoonright I:I\longrightarrow\mathbb R}
\tag{24.5.7}
$$

es continua en todos los puntos de $I$ (en el sentido usual, puesto que $I$ es abierto). En el caso de radio cero el conjunto de convergencia es $\{c\}$, pero no se afirma que éste sea un dominio abierto ni una continuidad de función definida en un entorno real.

**Demostración.**
El teorema de clasificación por el radio «Clasificación por el radio y convergencia interior» garantiza $I\subseteq C(a,c)$. La función restringida de (24.5.7) existe por el grafo de $F_{a,c}$ y la restricción de dominio, sin definir valores en puntos divergentes. Fijemos ahora $x_0\in I$. Pondremos $d_0:=|x_0-c|$. Si $R$ es finito y positivo, tomemos explícitamente $r:=(d_0+R)/2$, de modo que $d_0<r<R$. Si $R=+\infty$, tomemos $r:=d_0+1$, de modo que $0\le d_0<r<\infty$; la última desigualdad significa simplemente que $r$ es un real, no una comparación en un cuerpo de reales extendidos.

En ambos casos $K_r=[c-r,c+r]\subseteq I$. El teorema «Convergencia absoluta uniforme y cota geométrica del resto» proporciona convergencia uniforme de $S_N^{a,c}\upharpoonright K_r$ a $F_{a,c}\upharpoonright K_r$. Elegimos el radio local explícito

$$
\delta:=\frac{r-d_0}{2}>0,
\qquad V:=I\cap(x_0-\delta,x_0+\delta).
\tag{24.5.8}
$$

Para $x\in V$, la desigualdad triangular da $|x-c|\le|x-x_0|+d_0<\delta+d_0<r$. Así $V\subseteq K_r$ y las mismas sumas parciales restringidas a $V$ convergen uniformemente a $F_{a,c}\upharpoonright V$.

Cada término $x\mapsto a_n(x-c)^n$ es continuo en toda la recta: la traslación $x\mapsto x-c$ es continua, las potencias naturales lo son por inducción mediante el producto y la constante $a_n$ preserva continuidad. Todas las sumas parciales $S_N^{a,c}$ son continuas por inducción y la estabilidad de las sumas y productos de funciones continuas («Estabilidad de la continuidad bajo operaciones algebraicas y valor absoluto», en consonancia con «Todo polinomio real es continuo en la recta» sobre polinomios). Sus restricciones a $I$ son continuas relativamente a $I$. Aplicamos entonces «Basta la convergencia uniforme cerca del punto» al dominio original $E=I$, al punto $x_0$ y al entorno $V$ de (24.5.8): la uniformidad local y la continuidad de las sumas parciales prueban la continuidad de $F_{a,c}\upharpoonright I$ en $x_0$ relativamente a $I$. Como $x_0$ era arbitrario e $I$ es abierto, la conclusión es la continuidad ordinaria en todo $I$. No se eligió una familia simultánea de radios ni se obtuvo continuidad en los extremos $|x-c|=R$. $\square$

### Proposición 24.5.4 — La uniformidad no se extiende necesariamente al intervalo abierto completo
Existe una serie de potencias con radio positivo finito que converge absolutamente en cada punto de su intervalo abierto interior y absoluta y uniformemente en todos sus subintervalos cerrados estrictamente interiores, **pero no converge uniformemente en el intervalo abierto completo**.

**Demostración.**
Tomemos la serie geométrica $\sum_{n=0}^{\infty}x^n$, esto es, $c=0$ y $a_n=1$ para todo $n$. «Realización de los tres tipos de radio» ya establece que su radio es $R=1$; «Clasificación completa de la convergencia de la serie geométrica» determina su conjunto de convergencia $C(a,0)=(-1,1)$. Por el teorema 24.5.1, la serie converge absoluta y uniformemente sobre $[-r,r]$ para cada $0\le r<1$.

Si la serie convergiera uniformemente en todo $E:=(-1,1)$, el resultado cerrado «La convergencia uniforme de una serie obliga a la anulación uniforme de sus términos» obligaría a que la sucesión de términos $p_n(x)=x^n$ tendiera a cero **uniformemente** en $E$. Pero para cualquier natural fijo $n\ge1$ existe el real único

$$
x_n:=\sqrt[n]{3/4},\qquad 0<x_n<1,
\qquad |p_n(x_n)|=x_n^n=3/4>1/2.
\tag{24.5.9}
$$

La existencia, unicidad y desigualdades del radicando positivo y su raíz positiva provienen de «Existencia y unicidad de la raíz no negativa de índice positivo» y la monotonía de las potencias; se trata de una fórmula explícita, no de escoger puntos arbitrarios. Dada la tolerancia $\varepsilon=1/2$, **ningún** umbral $N$ puede conseguir $|p_n(x)|<\varepsilon$ para todos $n\ge N$ y todos $x\in E$: basta fijar $n\ge\max\{N,1\}$ y evaluar en $x_n$. Esto contradice la anulación uniforme necesaria; por tanto no hay convergencia uniforme en $(-1,1)$. $\square$

**Conclusión y transición.** Los intervalos interiores poseen control geométrico uniforme con un radio y una cota fijados antes de variar el punto; de ahí se obtiene la continuidad de la suma en su dominio abierto interior. El ejemplo geométrico impide generalizar esa uniformidad al intervalo abierto completo sin hipótesis nuevas. Tampoco hemos probado continuidad hasta los extremos convergentes, ni intercambio de derivada e integral con la serie: deberán justificarse en unidades posteriores. La siguiente unidad estudiará la integración término a término sobre intervalos cerrados interiores a partir de «Integración término a término de una serie dominada» y la derivación tras establecer una cota uniforme para la serie derivada; ninguna de esas conclusiones se presupone aquí.
---
