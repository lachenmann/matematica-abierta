## 17.5. Continuidad de las funciones elementales disponibles {#sec-ta-17-5}

No debemos llamar «elemental» a una fórmula cuya operación todavía no se haya construido. Disponemos de las potencias de exponente natural (§14.3), de sumas finitas (§14.1) y de raíces no negativas de índice natural positivo (§14.9). Las reglas de §17.4 permitirán obtener funciones polinomiales y racionales sin postular su continuidad. Las funciones exponencial, logarítmica y trigonométricas quedan fuera de esta sección: aquí no se les atribuye una definición ni una propiedad de continuidad no demostrada. Toda operación será interpretada en su dominio efectivo.

### Definición 17.5.1 — Función polinomial real determinada por una lista finita de coeficientes
Sea $m\in\mathbb N$, pongamos $I_m:=\{k\in\mathbb N:k\le m\}$ y fijemos una **función dada** de coeficientes $c:I_m\to\mathbb R$. Para cada $x\in\mathbb R$ definimos la sucesión real $a^x:\mathbb N\to\mathbb R$ por

$$
a^x_k:=\begin{cases}c(k)x^k,&k\le m,\\0,&k>m.\end{cases}
$$

La sucesión existe por Separación en $\mathbb N\times\mathbb R$; su definición no elige coeficientes, porque $c$ ya es un dato. La suma finita de §14.1 determina la función **polinomial asociada** $P_c:\mathbb R\to\mathbb R$ mediante

$$
\boxed{P_c(x):=\sum_{k=0}^{m}a^x_k
      =c(0)+c(1)x+\cdots+c(m)x^m.}
$$

La primera expresión —la suma inicial previamente definida— es la definición formal; los puntos suspensivos sólo son una presentación convencional. El grafo $\{\langle x,y\rangle\in\mathbb R\times\mathbb R:y=\sum_{k=0}^m a^x_k\}$ existe por Separación, y la unicidad de cada suma determina exactamente una función con dominio y codominio $\mathbb R$. Se admite $m=0$, que produce una constante; no exigimos que $c(m)\ne0$, por lo que $m$ es una cota de grado, no necesariamente el grado efectivo del polinomio. La letra $P_c$ es local a esta construcción y no consume un nuevo identificador de notación.


### Proposición 17.5.2 — Continuidad de toda potencia de exponente natural
Para cada $n\in\mathbb N$, la función $p_n:\mathbb R\to\mathbb R$, $p_n(x)=x^n$, es continua en todos los puntos de $\mathbb R$. La afirmación incluye $n=0$, con la convención ya fijada $0^0=1$.

**Demostración.**
Para cada $n$, $p_n$ existe como función tipada: la aplicación $x\mapsto x^n$ es la sección de la operación $\operatorname{pow}_{\mathbb R}:\mathbb R\times\mathbb N\to\mathbb R$ de Definición §14.3.1 — Potencias naturales de un número real, y su grafo se obtiene por Separación en $\mathbb R\times\mathbb R$. Procedemos por inducción sobre $n$. Para $n=0$, $p_0$ es la función constante de valor $1$, continua por Proposición §17.4.1 — Funciones constantes e inclusión continua. Si $p_n$ es continua en toda la recta, la identidad-inclusión $j_{\mathbb R}:\mathbb R\to\mathbb R$ también lo es. El producto puntual $p_nj_{\mathbb R}:\mathbb R\to\mathbb R$ es continuo por Teorema §17.4.3 — Estabilidad de la continuidad bajo operaciones algebraicas y valor absoluto y, por la recursión de potencias, coincide como función tipada con $p_{n+1}$. El principio de inducción concluye la afirmación para cada exponente natural, sin tomar una familia de radios simultáneamente para todos los exponentes. ∎


### Teorema 17.5.3 — Todo polinomio real es continuo en la recta
Para cualquier $m\in\mathbb N$ y cualquier función de coeficientes $c:I_m\to\mathbb R$, el polinomio $P_c:\mathbb R\to\mathbb R$ de la Definición 17.5.1 es continuo en todo $\mathbb R$.

**Demostración.**
Fijemos $m$ y $c$ y, para cada $j\in I_m$, definamos la función prefijo $P_j:\mathbb R\to\mathbb R$ tomando la suma inicial de la sucesión $a^x$ hasta $j$. Es una función tipada por el mismo argumento de Separación de la definición; las expresiones dependen de modo unívoco de $j,x,c$, sin seleccionar datos. La recursión de sumas parciales (Definición §14.1.1 — Sucesión de sumas parciales y serie numérica y Notación §14.1.2 — Suma finita de términos consecutivos) proporciona, para $j<m$,

$$
P_0(x)=c(0)x^0=c(0),\qquad
P_{j+1}(x)=P_j(x)+c(j+1)x^{j+1}.
$$

$P_0$ es constante, y por tanto continua. Supongamos continua $P_j$ para un $j<m$. Por la Proposición 17.5.2, $p_{j+1}$ es continua; por la regla escalar y la suma del Teorema 17.4.3, también lo es $P_j+c(j+1)p_{j+1}=P_{j+1}$. La inducción finita se efectúa exclusivamente sobre el segmento $I_m$: parte de $j=0$ y, para cada $j<m$, establece el paso de $P_j$ a $P_{j+1}$. Al llegar a $j=m$ concluye que $P_m=P_c$ es continua. No se enuncia ni se evalúa $P_j$ para $j\notin I_m$. Si $m=0$, ya se resolvió el caso en el paso inicial. ∎

**Ejemplo.** $P(x)=x^2-2$ es un polinomio real; su continuidad en todo $\mathbb R$ queda ahora justificada sin límites secuenciales ni derivadas. La constante $2$ se interpreta en el cuerpo real mediante el numeral correspondiente, no mediante una igualdad literal con el elemento racional $2_{\mathbb Q}$.


### Corolario 17.5.4 — Continuidad de las funciones racionales en su dominio natural
Sean $P,Q:\mathbb R\to\mathbb R$ dos funciones polinomiales de la Definición 17.5.1, dadas posiblemente por listas de coeficientes de longitudes diferentes. Pongamos

$$
D_Q:=\{x\in\mathbb R:Q(x)\ne0\}.
$$

Entonces la expresión $R(x)=P(x)/Q(x)$ determina una función $R:D_Q\to\mathbb R$, **continua en todos los puntos de $D_Q$**. El conjunto $D_Q$ puede ser vacío.

**Demostración.**
Por Teorema §17.5.3 — Todo polinomio real es continuo en la recta, $P$ y $Q$ son continuos sobre $\mathbb R$. El conjunto $D_Q$ existe por Separación; el cociente funcional sobre él existe conforme a Proposición §16.3.2 — Existencia y tipado de las operaciones puntuales. Fijemos $a\in D_Q$: entonces $Q(a)\ne0$, y Teorema §17.4.4 — Continuidad del recíproco y del cociente en sus dominios efectivos prueba la continuidad de $P/Q$ en $a$ relativamente a $D_Q$. La arbitrariedad de $a$ acredita la continuidad global. Si $D_Q=\varnothing$, la afirmación «continua en cada punto de su dominio» es universalmente verdadera, pero no se declara ningún límite en el vacío. La simplificación algebraica de una expresión no añade por sí sola puntos a este dominio. ∎

**Advertencia de dominio.** $R(x)=(x^2-1)/(x-1)$ tiene dominio $\mathbb R\setminus\{1\}$, aunque allí coincida en valores con $x+1$. Estas dos funciones no son idénticas como funciones tipadas: tienen dominios distintos. La continuidad de $x+1$ en $1$ no define el valor de $R$ en $1$.


### Lema 17.5.5 — Separación de potencias de argumentos no negativos
Para $n\in\mathbb N$ con $n\ge1$ y $u,v\in\mathbb R_{\ge0}$ se tiene

$$
\boxed{|u-v|^n\le |u^n-v^n|.}
\tag{17.5.1}
$$

**Demostración.**
Por la totalidad del orden, basta probar la desigualdad cuando $u\ge v\ge0$; el otro caso se obtiene permutando los argumentos. Fijemos $d:=u-v\ge0$, de modo que $u=v+d\ge d$. Probaremos por inducción sobre $k\in\mathbb N$ que

$$
u^{k+1}-v^{k+1}\ge d^{k+1}.
$$

El caso $k=0$ es la igualdad $u-v=d$. Supongamos válida la desigualdad para $k$. Por la recursión de la potencia,

$$
\begin{aligned}
u^{k+2}-v^{k+2}
&=(u^{k+1}-v^{k+1})u+v^{k+1}(u-v)\\
&\ge d^{k+1}u\\
&\ge d^{k+1}d=d^{k+2}.
\end{aligned}
$$

Las multiplicaciones preservan el orden porque todos los factores multiplicadores utilizados son no negativos; $v^{k+1}\ge0$. La inducción da $u^n-v^n\ge(u-v)^n$. En el caso $u\ge v$, ambos valores absolutos son las correspondientes diferencias no negativas por la monotonía de Lema §14.9.1 — Monotonía de las potencias positivas y cota de variación finita. Si $v\ge u$, aplicamos la misma prueba al par $(v,u)$. Así se obtiene (17.5.1) sin fórmula binomial ni raíces aún en uso dentro de la prueba. ∎


### Teorema 17.5.6 — Continuidad de todas las raíces reales no negativas disponibles
Para cada índice natural positivo $n\in\mathbb N_{\ge1}$, la asignación ya construida

$$
r_n:\mathbb R_{\ge0}\to\mathbb R,
\qquad r_n(x)=\sqrt[n]{x},
$$

es continua en **todos** los puntos de su dominio, incluido $0$. La función está provista explícitamente del codominio $\mathbb R$; su recorrido está contenido en $\mathbb R_{\ge0}$.

**Demostración.**
La existencia y unicidad para cada $x\ge0$ y $n\ge1$, y el grafo de la función de raíces, están certificados en Teorema §14.9.2 — Existencia y unicidad de la raíz no negativa de índice positivo y Notación §14.9.3 — Raíz enésima real no negativa. Fijemos $a\ge0$ y $\varepsilon>0$. La potencia $\varepsilon^n$ es estrictamente positiva; tomemos

$$
\boxed{\delta:=\varepsilon^n>0.}
$$

Si $x\ge0$ y $|x-a|<\delta$, escribamos $u:=\sqrt[n]{x}\ge0$ y $v:=\sqrt[n]{a}\ge0$. Sus ecuaciones definitorias dan $u^n=x$ y $v^n=a$. El lema anterior produce

$$
|u-v|^n\le |x-a|<\varepsilon^n.
$$

Por la estricta monotonía de la potencia de exponente positivo entre reales no negativos (Lema §14.9.1 — Monotonía de las potencias positivas y cota de variación finita), la desigualdad implica $|u-v|<\varepsilon$: de lo contrario, $|u-v|\ge\varepsilon$ implicaría $|u-v|^n\ge\varepsilon^n$. Es exactamente la continuidad en $a$ relativa a $\mathbb R_{\ge0}$. La prueba sirve sin cambio en $a=0$, donde no hay valores de raíz definidos para radicandos negativos. La raíz es la solución única de una ecuación ya demostrada, no una elección entre soluciones. ∎


### Corolario 17.5.7 — Continuidad de un radical compuesto en su dominio efectivo
Sean $D\subseteq\mathbb R$, $g:D\to\mathbb R$ continua en todos los puntos de $D$, y $n\in\mathbb N_{\ge1}$. Definamos

$$
T:=\{x\in D:g(x)\ge0\}.
$$

Entonces $h:T\to\mathbb R$, $h(x)=\sqrt[n]{g(x)}$, es una función bien definida y continua en **cada punto de $T$**. Si $T=D$, la continuidad vale sobre todo el dominio original; si $T=\varnothing$, no se evalúa el radical en ningún punto.

**Demostración.**
Por Separación existe $T$. La restricción de $g$ a $T$ toma valores en $E:=\mathbb R_{\ge0}$ y, tras declarar expresamente su codominio $E$, determina $g_T:T\to E$. Por Teorema §17.5.6 — Continuidad de todas las raíces reales no negativas disponibles la función exterior $r_n:E\to\mathbb R$ es continua en cada punto de $E$. Para cada $a\in T$, la continuidad de $g$ en $a$ relativamente a $D$ y de $r_n$ en $g(a)\in E$ permite aplicar Teorema §17.4.5 — Composición en el dominio efectivo y concluir que $r_n\circ g_T:T\to\mathbb R$ es continua en $a$. La composición coincide en dominio, codominio y valores con $h$. No se extiende el radical a los puntos con $g(x)<0$. ∎

**Ejemplos.** $x\mapsto\sqrt{x}$ es continua en $[0,\infty)$, incluida la frontera $0$. También $x\mapsto\sqrt{1-x^2}$ es continua en $[-1,1]$ por continuidad polinomial y composición efectiva; no se le atribuye un valor real fuera de ese intervalo.

**Transición.** Hemos establecido continuidad para las funciones algebraicas cuyas operaciones y raíces ya tenían una definición legítima. Estas pruebas son puntuales: el radio puede depender del punto considerado. La próxima sección introducirá una condición diferente, con un radio que pueda elegirse **independientemente del centro**: la continuidad uniforme. Su teorema global sobre compactos permanecerá reservado al Capítulo 18.
