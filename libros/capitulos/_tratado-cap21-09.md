## 21.9. Sumas etiquetadas y equivalencia de las definiciones de Riemann y Darboux {#sec-ta-21-9}

Las sumas de Darboux permiten encerrar un valor mediante ínfimos y supremos locales. Hay otra manera de aproximarlo: escoger un punto del subintervalo y usar el valor efectivo de la función en ese punto. Para relacionar ambas construcciones no basta demostrar que una suma escogida pertenece al intervalo de Darboux. Debemos probar que todas las sumas etiquetadas, con independencia de sus etiquetas, se aproximan simultáneamente al mismo número cuando la partición tiene malla suficientemente pequeña.

Durante toda la sección fijamos $a<b$, $I=[a,b]$ y una función acotada $f:I\to\mathbb R$. Para el intervalo degenerado continúa vigente únicamente la convención separada de §21.6; no extenderemos a él las particiones estrictas.

### Definición 21.9.1 — Etiquetas admisibles y suma etiquetada
Sea $P=\langle n,p\rangle\in\operatorname{Part}[a,b]$ y sea $K_n:=\{k\in\mathbb N:k<n\}$. Una familia de etiquetas admisibles para $P$ es una función tipada $\tau:K_n\to I$ que cumple

$$
 \tau(k)\in I_k(P)=[x_k,x_{S(k)}]\qquad(k<n).
 \tag{21.9.1}
$$

Por Separación dentro del conjunto de funciones $I^{K_n}$ definimos el conjunto

$$
 \operatorname{Tag}(P):=\{\tau\in I^{K_n}:(\forall k<n)\ \tau(k)\in I_k(P)\}.
 \tag{21.9.2}
$$

Una partición etiquetada es el par $\langle P,\tau\rangle$, con $\tau\in\operatorname{Tag}(P)$. La identidad de $P$ y la función $\tau$ se conservan: no identificamos una partición etiquetada con una lista informal de puntos. La suma etiquetada de $f$ es el real

$$
 \boxed{S(f;P,\tau):=\sum_{k=0}^{n-1}f(\tau(k))\Delta_k(P).}
 \tag{21.9.3}
$$

La suma tiene exactamente $n\ge1$ términos y todos sus argumentos pertenecen al dominio de $f$. La definición no presupone integrabilidad; tampoco prescribe escoger una familia de etiquetas para todas las particiones.

### Proposición 21.9.2 — Existencia de etiquetas y encierro de cada suma
Para toda partición $P$, el conjunto $\operatorname{Tag}(P)$ es no vacío. Cualesquiera que sean sus etiquetas $\tau$,

$$
 \boxed{L(f,P)\le S(f;P,\tau)\le U(f,P).}
 \tag{21.9.4}
$$

**Demostración.**
La función $\tau_0:K_n\to I$ definida por el grafo explícito $\tau_0(k)=x_k$ existe por Separación en $K_n\times I$. Como $x_k\in I_k(P)$, pertenece a $\operatorname{Tag}(P)$; no hemos elegido ningún punto arbitrario. Para una función admisible cualquiera, la definición de extremos locales da

$$
 m_k(P)\le f(\tau(k))\le M_k(P).
$$

Multiplicamos por $\Delta_k(P)>0$ y sumamos las $n$ desigualdades, usando la comparación de sumas finitas Proposición §14.5.1 — Comparación de sumas finitas y de bloques. Las sumas de los extremos son exactamente $L(f,P)$ y $U(f,P)$, lo que demuestra (21.9.4). $\square$

### Lema 21.9.3 — Aproximación finita de ambos extremos por etiquetas
Fijada una partición $P$, para cada $\varepsilon>0$ existen $\tau_-,\tau_+\in\operatorname{Tag}(P)$ tales que

$$
 \boxed{L(f,P)\le S(f;P,\tau_-)<L(f,P)+\varepsilon,}
 \tag{21.9.5}
$$

$$
 \boxed{U(f,P)-\varepsilon<S(f;P,\tau_+)\le U(f,P).}
 \tag{21.9.6}
$$

En particular, el conjunto real $\mathcal S(f,P):=\{s\in\mathbb R:\exists\tau\in\operatorname{Tag}(P),\ s=S(f;P,\tau)\}$ existe y es no vacío, y sus extremos satisfacen

$$
 \boxed{\inf\mathcal S(f,P)=L(f,P),\qquad
 \sup\mathcal S(f,P)=U(f,P).}
 \tag{21.9.7}
$$

**Demostración.**
Tomemos $\eta:=\varepsilon/(b-a)>0$; la división es legítima porque $a<b$. Para cada índice fijo $k<n$, el número $m_k(P)$ es el ínfimo de la imagen no vacía $f[I_k(P)]$. Por la propiedad característica del ínfimo, existe $t_k^-\in I_k(P)$ con

$$
 m_k(P)\le f(t_k^-)<m_k(P)+\eta.
$$

De no existir, $m_k(P)+\eta$ sería una cota inferior de la imagen estrictamente mayor que su ínfimo. De forma dual, por la propiedad del supremo existe $t_k^+\in I_k(P)$ tal que

$$
 M_k(P)-\eta<f(t_k^+)\le M_k(P).
$$

**Justificación fundacional de las etiquetas simultáneas.** No pasamos de $\forall k\,\exists t_k$ a una familia infinita por decreto. Aplicamos inducción natural a los segmentos finitos de índices: el grafo vacío es una función parcial admisible; si ya se ha construido un grafo sobre los índices menores que $j<n$, instanciamos la existencia para ese único índice $j$ y añadimos el par $\langle j,t_j^-\rangle$. La unión finita es una función porque $j$ no figuraba en el dominio anterior. Tras $n$ pasos obtenemos una función $\tau_-:K_n\to I$ con todas las desigualdades, y repetimos esta misma inducción para $\tau_+$. Este argumento prueba por inducción la existencia de dos funciones finitas para el $P$ y el $\varepsilon$ dados, sin construir una función de elección sobre un conjunto infinito de particiones o tolerancias.

Multiplicando cada desigualdad por la anchura positiva y sumando, con $\sum_{k<n}\Delta_k(P)=b-a$, llegamos a

$$
 0\le S(f;P,\tau_-)-L(f,P)
 <\eta\sum_{k<n}\Delta_k(P)=\varepsilon,
$$

$$
 0\le U(f,P)-S(f;P,\tau_+)<\varepsilon.
$$

La estricta desigualdad se conserva porque la suma es finita y no vacía y cada diferencia ponderada es estrictamente menor que $\eta\Delta_k(P)$. El encierro (21.9.4) completa (21.9.5)–(21.9.6).

La fórmula definitoria de $\mathcal S(f,P)$ permite obtenerla por Separación en $\mathbb R$; es no vacía por la proposición precedente y está acotada por (21.9.4). Luego tiene supremo e ínfimo reales. Como $U(f,P)$ es cota superior y (21.9.6) proporciona valores mayores que $U(f,P)-\varepsilon$ para toda precisión positiva, ningún real menor que $U(f,P)$ puede ser una cota superior. Así $\sup\mathcal S(f,P)=U(f,P)$; la prueba dual da el ínfimo. $\square$

**Lectura.** Que $U(f,P)$ sea supremo de las sumas etiquetadas no implica que alguna etiqueta alcance todos los supremos locales. El lema sólo aproxima simultáneamente un número finito de extremos, y eso basta.

### Proposición 21.9.4 — Existencia del máximo de las anchuras y particiones finas
Para cada $P=\langle n,p\rangle\in\operatorname{Part}[a,b]$ existe un único máximo $d(P)$ del conjunto no vacío de anchuras

$$
 W(P):=\{d\in\mathbb R:(\exists k<n)\ d=\Delta_k(P)\}.
 \tag{21.9.8}
$$

Se cumple $d(P)>0$. Para cada $\delta>0$ existe una partición $P$ con $d(P)<\delta$.

**Demostración.**
El conjunto $W(P)$ existe por Separación, ya que sus anchuras son reales definidos a partir de una función finita. Contiene $\Delta_0(P)$ porque $n\ge1$. El máximo de la primera anchura es ella misma. Si el máximo de las primeras $j\ge1$ anchuras es $d_j$, la totalidad del orden real permite definir de manera única el máximo de $d_j$ y $\Delta_j(P)$: es uno de esos dos valores, según su comparación. La inducción finita llega al máximo de las $n$ anchuras; pertenece a $W(P)$ y está por encima de todas ellas. Su unicidad resulta de la antisimetría. Como todas las anchuras son positivas, también lo es el máximo.

Dado $\delta>0$, Lema §21.7.1 — Particiones equidistantes de anchura arbitrariamente pequeña construye una partición equidistante para la cual todas las anchuras son menores que $\delta$; su máximo es una de ellas, luego también es menor que $\delta$. No hemos seleccionado una partición simultáneamente para cada radio. $\square$

### Definición 21.9.5 — Malla de una partición
Definimos la malla de $P$ como el máximo cuya existencia acabamos de demostrar:

$$
 \boxed{\operatorname{mesh}(P):=d(P)=\max_{k<n}\Delta_k(P)>0.}
 \tag{21.9.9}
$$

Así, $\operatorname{mesh}(P)<\delta$ equivale exactamente a que $\Delta_k(P)<\delta$ para todo $k<n$. Usaremos $\operatorname{mesh}(P)$ en lugar del símbolo alternativo $\lVert P\rVert$: la malla es una anchura real y no una norma definida sobre un espacio vectorial de particiones.

### Lema 21.9.6 — Una partición fina hereda una brecha pequeña de otra partición
Sean $A,B\in\mathbb R$ cotas globales $A\le f(t)\le B$ en $I$, y escribamos $C:=B-A\ge0$. Sea $Q=\langle m,q\rangle$ una partición fija. Para toda partición $P$ se cumple

$$
 \boxed{0\le G(f,P)\le G(f,Q)+C\,\nu_{\mathbb R}(m)\operatorname{mesh}(P),}
 \tag{21.9.10}
$$

con $G(f,T):=U(f,T)-L(f,T)$ y $\nu_{\mathbb R}(m)$ el numeral real del natural $m$. En particular, para cada $\varepsilon>0$ existe un $\delta>0$ tal que toda partición $P$ con $\operatorname{mesh}(P)<\delta$ satisface

$$
 G(f,P)<G(f,Q)+\varepsilon.
 \tag{21.9.11}
$$

**Demostración.**
Construyamos el refinamiento común $R$ de $P$ y $Q$ de Teorema §21.1.5 — Existencia de un refinamiento común, de modo que $V(R)=V(P)\cup V(Q)$ y $Q\preccurlyeq R$. Llamemos mala a una celda $I_k(P)$ cuyo interior contiene algún nodo de $Q$. Si no es mala, ningún nodo adicional del refinamiento cae en su interior y la misma celda figura sin modificación en $R$; su contribución a la brecha es exactamente la misma en ambas particiones.

Cada celda mala contiene al menos un nodo interior de $Q$, y los interiores de celdas distintas de $P$ son disjuntos. Para cada celda mala tomamos el primer índice en la lista dada de $Q$ cuyo nodo está en ese interior. El mínimo natural es único, así que la aplicación de celdas malas a esos índices es una inyección; ninguna selección arbitraria se requiere. Existen como máximo $m$ celdas malas, pues $Q$ tiene $m$ subintervalos y sólo los índices $1,\ldots,m-1$ pueden corresponder a nodos interiores de $I$.

La acotación global implica $0\le\omega_k(P)\le C$. En una celda mala su contribución original a $G(f,P)$ es a lo sumo $C\Delta_k(P)$. Todas las contribuciones de las subceldas de $R$ son no negativas, gracias a (21.2.7). Como las contribuciones de las celdas buenas coinciden, la descomposición finita de sumas por bloques da

$$
 \begin{aligned}
 G(f,P)&\le G(f,R)+C\sum_{k\text{ malo}}\Delta_k(P)\\
 &\le G(f,Q)+C\,\nu_{\mathbb R}(m)\operatorname{mesh}(P).
 \end{aligned}
 \tag{21.9.12}
$$

En la segunda línea utilizamos la monotonía de la brecha bajo refinamiento $Q\preccurlyeq R$, y el hecho de que a lo sumo $m$ sumandos no negativos están acotados por la malla; la multiplicidad natural se traduce a su numeral real antes de multiplicar. La primera desigualdad de (21.9.10) es la no negatividad de la brecha.

Para (21.9.11), dado $\varepsilon>0$, basta fijar

$$
 \delta:=\frac{\varepsilon}{(C+1_{\mathbb R})(\nu_{\mathbb R}(m)+1_{\mathbb R})}>0.
$$

Si $\operatorname{mesh}(P)<\delta$, entonces $C\nu_{\mathbb R}(m)\operatorname{mesh}(P)<\varepsilon$, incluso si $C=0$. No se eligió una familia de refinamientos: $R$ se construyó para el par de particiones dado. $\square$

**Por qué se necesitaba este lema.** El criterio de Darboux de §21.4 asegura una partición con brecha pequeña y todos sus refinamientos. Una partición con malla pequeña, sin embargo, no tiene por qué refinarla: puede omitir todos sus nodos interiores. La estimación (21.9.10) subsana precisamente esta diferencia; el posible error se concentra en las pocas celdas que atraviesan nodos de $Q$.

### Definición 21.9.7 — Criterio de integrabilidad por sumas etiquetadas
Para una función acotada $f:[a,b]\to\mathbb R$ diremos que satisface el criterio de Riemann por sumas etiquetadas si existe un real $J$ tal que

$$
 \boxed{(\forall\varepsilon>0)(\exists\delta>0)
 (\forall P\in\operatorname{Part}[a,b])
 (\operatorname{mesh}(P)<\delta\Longrightarrow
 (\forall\tau\in\operatorname{Tag}(P))\,
 |S(f;P,\tau)-J|<\varepsilon).}
 \tag{21.9.13}
$$

La posición de $\forall\tau$ después de $\forall P$ es esencial: las etiquetas son cualesquiera y la misma malla $\delta$ sirve para todas las particiones. La definición no presupone un límite previamente construido de una sucesión de sumas, ni exige elegir una partición por cada natural. El alcance sigue restringido a funciones acotadas y a $a<b$; al intervalo singleton le corresponde §21.6.

### Teorema 21.9.8 — Equivalencia exacta entre Darboux y las sumas etiquetadas
Para $a<b$ y una función acotada $f:[a,b]\to\mathbb R$, las siguientes condiciones son equivalentes:

1. $f$ es integrable de Darboux en el sentido de Definición §21.4.1 — Integrabilidad de Darboux por igualdad de integrales extremas.
2. $f$ satisface el criterio de sumas etiquetadas (21.9.13) para algún $J\in\mathbb R$.

Cuando se verifican, el número $J$ es único y necesariamente

$$
 \boxed{J=\int_a^b f.}
 \tag{21.9.14}
$$

**Demostración.**
**Darboux implica Riemann etiquetado.** Supongamos que $f$ es integrable y escribamos $I_f:=\int_a^b f$. Fijemos $\varepsilon>0$. El criterio Teorema §21.4.2 — Criterio de Darboux y estabilidad por refinamiento proporciona una partición fija $Q=\langle m,q\rangle$ con

$$
 G(f,Q)<\varepsilon/2.
$$

Tomemos cualesquiera cotas globales $A\le f\le B$ y $C=B-A\ge0$. Elijamos el real explícito

$$
 \delta:=\frac{\varepsilon}{2(C+1_{\mathbb R})(\nu_{\mathbb R}(m)+1_{\mathbb R})}>0.
$$

Para toda partición $P$ con $\operatorname{mesh}(P)<\delta$, el lema anterior da

$$
 0\le G(f,P)\le G(f,Q)+C\nu_{\mathbb R}(m)\operatorname{mesh}(P)<\varepsilon.
 \tag{21.9.15}
$$

La última desigualdad es estricta porque $G(f,Q)<\varepsilon/2$ y el segundo término es menor que $\varepsilon/2$. Por el encierro de las sumas etiquetadas (21.9.4) y el encierro de la integral Proposición §21.4.4 — Encierro del valor integral y control por la brecha, tanto $S(f;P,\tau)$ como $I_f$ pertenecen al mismo intervalo $[L(f,P),U(f,P)]$. Por ello, para toda etiqueta admisible,

$$
 |S(f;P,\tau)-I_f|\le G(f,P)<\varepsilon.
$$

Ésta es exactamente (21.9.13) con $J=I_f$. No hemos supuesto que $P$ refine a $Q$.

**Riemann etiquetado implica Darboux.** Supongamos que existe un $J$ con (21.9.13). Para una tolerancia arbitraria $\varepsilon>0$, apliquemos dicha condición con $\eta:=\varepsilon/3>0$ y obtengamos $\delta>0$. Por Proposición §21.9.4 — Existencia del máximo de las anchuras y particiones finas existe una partición $P$ con $\operatorname{mesh}(P)<\delta$. Así, todas sus sumas etiquetadas satisfacen

$$
 J-\eta<S(f;P,\tau)<J+\eta.
$$

El lema Lema §21.9.3 — Aproximación finita de ambos extremos por etiquetas demuestra que las sumas etiquetadas tienen por ínfimo $L(f,P)$ y por supremo $U(f,P)$. Por las propiedades extremales, las desigualdades válidas para todas las etiquetas implican las cotas no estrictas

$$
 J-\eta\le L(f,P)\le U(f,P)\le J+\eta.
 \tag{21.9.16}
$$

Por consiguiente,

$$
 0\le G(f,P)\le2\eta=2\varepsilon/3<\varepsilon.
$$

El criterio de Darboux Teorema §21.4.2 — Criterio de Darboux y estabilidad por refinamiento prueba la integrabilidad de $f$; ahora, y sólo ahora, la expresión $I_f:=\int_a^b f$ está definida. Su encierro Proposición §21.4.4 — Encierro del valor integral y control por la brecha y (21.9.16) dan

$$
 J-\eta\le I_f\le J+\eta.
 \tag{21.9.17}
$$

La deducción vale para cada $\varepsilon>0$, y por tanto para todo $\eta>0$. Si $I_f\ne J$, tomemos $\eta=|I_f-J|/2>0$; (21.9.17) implicaría $|I_f-J|\le\eta<|I_f-J|$, contradicción. Se sigue $I_f=J$, lo que prueba también la unicidad del número que satisface (21.9.13). $\square$

**Conclusión conceptual.** La integral se define mediante los supremos e ínfimos de Darboux, pero puede caracterizarse como el valor al que se aproximan uniformemente todas las sumas etiquetadas de malla suficientemente pequeña. Una sola selección favorable de etiquetas no reemplaza el cuantificador universal. Ni la existencia de extremos locales ni su aproximación finita requieren que $f$ sea continua; tampoco intervienen primitivas, medida de Lebesgue o el teorema fundamental del cálculo.

**Transición al teorema fundamental del cálculo.** La integral ha sido construida mediante supremos e ínfimos de sumas finitas y caracterizada, después, por sumas etiquetadas de malla pequeña. La cuestión siguiente será estudiar la función que asigna a cada extremo variable la integral acumulada y establecer, bajo hipótesis explícitas, su relación con la derivación. Nada de lo probado aquí presupone esa relación: será el objeto del Capítulo 22.
