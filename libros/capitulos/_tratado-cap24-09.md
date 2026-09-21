## 24.9. Series de Taylor, resto y analiticidad real {#sec-ta-24-9}

El resultado de §24.8 tiene una dirección precisa: si una función está representada por una serie de potencias en un entorno de su centro, entonces sus coeficientes se recuperan mediante las derivadas en ese centro. La implicación inversa necesita una hipótesis más fuerte que la existencia de todas las derivadas. La investigaremos mediante las sumas finitas de Taylor y su resto; después construiremos dentro del tratado una función suave cuyo desarrollo de Taylor no la representa.

### Definición 24.9.1 — Serie y restos de Taylor de una función infinitamente derivable
Sea $J\subseteq\mathbb R$ un intervalo abierto no vacío, $f:J\to\mathbb R$ una función y $c\in J$. Diremos aquí que $f$ es infinitamente derivable en $J$, o $C^\infty$ en $J$, si existe la sucesión de funciones $f^{(k)}:J\to\mathbb R$ determinada por $f^{(0)}=f$ y por la condición $f^{(k+1)}=(f^{(k)})'$ en todos los puntos de $J$, para cada $k\in\mathbb N$. La notación designa derivadas sobre el dominio abierto $J$, no extensiones a sus puntos frontera. La existencia de cada derivada asegura su unicidad; el grafo de la familia completa se obtiene por Separación sobre $\mathbb N\times\mathbb R^J$ y no por una elección de funciones.

Cuando $f$ satisface esa condición, definimos su sucesión de coeficientes de Taylor en $c$, $t^{f,c}:\mathbb N\to\mathbb R$, por

$$
\boxed{t^{f,c}_k:=\frac{f^{(k)}(c)}{\eta_k},\qquad
\eta_k:=\nu_{\mathbb R}(k!)>0.}
\tag{24.9.1}
$$

La positividad del factorial real está probada en «Positividad y recurrencia de los factoriales»; jamás se divide por un factorial natural como si fuera literalmente un real. Formamos el polinomio tipado $T_N[f,c]:\mathbb R\to\mathbb R$ y la función resto $E_N[f,c]:J\to\mathbb R$ mediante

$$
\boxed{T_N[f,c](x):=\sum_{k=0}^{N}t^{f,c}_k(x-c)^k,
\qquad E_N[f,c](x):=f(x)-T_N[f,c](x)\quad(x\in J).}
\tag{24.9.2}
$$

La serie de Taylor es, por ahora formalmente, la serie de potencias $\sum_{k=0}^{\infty}t^{f,c}_k(x-c)^k$ de «Serie de potencias real centrada». Sus sumas parciales son $T_N[f,c]$ y su suma $F_{t^{f,c},c}$ sólo está definida sobre $C(t^{f,c},c)$; no se le atribuyen valores fuera de ese conjunto. Para todo $N$, $T_N[f,c](c)=f(c)$ y $E_N[f,c](c)=0$, pues $\eta_0=1$ y todas las potencias de exponente positivo se anulan en el centro.

**Precisión de alcance.** La fórmula (24.9.2) coincide con el polinomio finito de «Polinomio de Taylor finito en un centro» al restringir una cadena diferencial de longitud $N$ a un cerrado no degenerado alrededor de $c$ contenido en $J$. La existencia de la familia completa de derivadas no presupone que su serie infinita converja, ni mucho menos que su suma sea $f$.

### Proposición 24.9.2 — Criterio puntual y uniforme mediante el resto
Con las hipótesis y notación anteriores, para cualquier $x\in J$ son equivalentes las tres afirmaciones siguientes:

$$
\boxed{E_N[f,c](x)\longrightarrow0
\quad\Longleftrightarrow\quad
T_N[f,c](x)\longrightarrow f(x)
\quad\Longleftrightarrow\quad
\bigl[x\in C(t^{f,c},c)\ \text{y}\ F_{t^{f,c},c}(x)=f(x)\bigr].}
\tag{24.9.3}
$$

Además, para cualquier conjunto dado $A\subseteq J$, los restos $E_N[f,c]\upharpoonright A$ convergen uniformemente a cero si y sólo si los polinomios $T_N[f,c]\upharpoonright A$ convergen uniformemente a $f\upharpoonright A$. Esta equivalencia no exige que $A$ sea compacto; para $A=\varnothing$ ambos predicados uniformes son vacuos.

**Demostración.**
Para un punto fijo $x\in J$ y todo $N$, la definición proporciona la identidad exacta $E_N[f,c](x)=f(x)-T_N[f,c](x)$ y, por tanto,

$$
|E_N[f,c](x)|=|T_N[f,c](x)-f(x)|.
\tag{24.9.4}
$$

Dado $\varepsilon>0$, el mismo índice $N_0$ verifica la desigualdad $|E_N[f,c](x)|<\varepsilon$ para todos los $N\ge N_0$ si y sólo si verifica $|T_N[f,c](x)-f(x)|<\varepsilon$ para ellos. Ésta es la primera equivalencia. Las sumas parciales de la serie de Taylor son precisamente $T_N[f,c](x)$ por «Construcción tipada de los términos y las sumas parciales»; la definición de $C$ y la unicidad de la función suma «Existencia y unicidad de la función suma sobre su dominio exacto» identifican su convergencia hacia $f(x)$ con la tercera afirmación. Para el caso uniforme basta cuantificar (24.9.4) simultáneamente sobre todos los $x\in A$: los mismos $\varepsilon$ y $N_0$ funcionan en ambas direcciones. Las restricciones tienen dominio y codominio comunes y no se selecciona un índice diferente para cada punto. $\square$

**Consecuencia lógica.** Una serie de Taylor puede converger en un punto y hacerlo hacia un valor distinto de $f(x)$. Conocer sólo la convergencia de los coeficientes no permite suprimir el resto de (24.9.3).

### Definición 24.9.3 — Función real analítica en un centro
Sean $J\subseteq\mathbb R$ un intervalo abierto y $f:J\to\mathbb R$. Diremos que $f$ es real analítica en $c\in J$ si existen una sucesión real $a:\mathbb N\to\mathbb R$ y un $\delta>0$ tales que el radio $R(a,c)$ es positivo o la marca formal $+\infty$, y

$$
\boxed{U:=(c-\delta,c+\delta)\subseteq J\cap I_{a,c},
\qquad f(x)=F_{a,c}(x)\quad(x\in U),}
\tag{24.9.5}
$$

siendo $I_{a,c}$ el intervalo abierto interior al radio de la serie $a$, igual a $\mathbb R$ cuando el radio es infinito. La igualdad es entre restricciones con dominio $U$ y codominio $\mathbb R$. Se dice que $f$ es analítica en $J$ cuando lo es en cada punto de $J$; el cuantificador $\forall c\in J\,\exists(a,\delta)$ no se convierte en la elección de una familia $c\mapsto a^c$. Una representación local hace automáticamente derivable de todos los órdenes a $f$ en ese entorno, por «Derivadas de todo orden y conservación del radio», pero la definición no supone de antemano suavidad global en un dominio más amplio.

### Teorema 24.9.4 — Caracterización de la analiticidad por el resto de Taylor
Sea $J\subseteq\mathbb R$ un intervalo abierto no vacío, $f:J\to\mathbb R$ infinitamente derivable en $J$ y $c\in J$. Entonces son equivalentes:

1. $f$ es analítica en $c$ en el sentido de «Función real analítica en un centro».
2. Existe $\delta>0$ con $U=(c-\delta,c+\delta)\subseteq J$ tal que, para cada $x\in U$, $E_N[f,c](x)\to0$.

En ese caso los coeficientes de toda representación local centrada en $c$ son necesariamente $t_k^{f,c}=f^{(k)}(c)/\eta_k$, y el resto converge uniformemente a cero sobre cada cerrado $K_r=[c-r,c+r]$ contenido estrictamente en un entorno de representación e interior a su radio.

**Demostración.**
**De 1 a 2.** Tomemos una sucesión $a$ y $\delta>0$ que cumplan (24.9.5). Sobre el abierto $U$, las funciones $f$ y $F_{a,c}$ coinciden. Por «Derivadas de todo orden y conservación del radio» sus derivadas de todo orden coinciden en el centro: los cocientes incrementales de las restricciones son iguales cerca de $c$, y esto se repite inductivamente para cada derivada. El corolario «Recuperación de cada coeficiente mediante la derivada en el centro» da

$$
f^{(k)}(c)=\eta_k a_k,
\qquad t_k^{f,c}=a_k\quad(k\in\mathbb N).
\tag{24.9.6}
$$

La serie de Taylor tiene, pues, las mismas sumas parciales que la serie $a$. Como $U\subseteq I_{a,c}$, «Clasificación por el radio y convergencia interior» asegura su convergencia en todo $U$ y la identidad con $f$ está dada por hipótesis. «Criterio puntual y uniforme mediante el resto» prueba $E_N[f,c](x)\to0$ para cada $x\in U$. Si $r>0$ se fija con $K_r\subseteq U$ y $r<R(a,c)$ en el caso finito (sin comparar números reales con la marca infinita), «Convergencia absoluta uniforme y cota geométrica del resto» da convergencia uniforme de esas mismas sumas parciales hacia $f$ sobre $K_r$; el criterio uniforme de 24.9.2 proporciona uniformidad de los restos. No se ha seleccionado una sucesión de radios.

**De 2 a 1.** Sean $\delta>0$ y $U$ como en 2, y pongamos $t:=t^{f,c}$. Por el criterio puntual 24.9.2, para todo $x\in U$ la serie con coeficientes $t$ converge hacia $f(x)$. En particular, el punto explícito $y:=c+\delta/2$ pertenece a $U\subseteq C(t,c)$ y su distancia positiva al centro es $d:=\delta/2$. Así $d\in D(t,c)$ y el radio de la serie $t$ es al menos $d$ si es finito, o infinito. Definamos $\rho:=d/2=\delta/4>0$. Para $|x-c|<\rho$, tenemos $x\in U\subseteq J$ y $|x-c|<\rho<d\le R(t,c)$ en el caso finito; en el infinito el interior radial es toda $\mathbb R$. En ambos casos, $(c-\rho,c+\rho)\subseteq J\cap I_{t,c}$ y la suma de la serie allí coincide con $f$ por el criterio puntual. La propia sucesión $t$ y el radio explícito $\rho$ verifican «Función real analítica en un centro». Se ha usado un solo punto elegido por fórmula a partir de $\delta$, no Choice. $\square$

**Lectura del criterio.** El resto no es un adorno en una igualdad formal: su límite nulo es exactamente la hipótesis que convierte una aproximación polinómica de orden creciente en una representación efectiva por serie de potencias. La convergencia de la serie sin esa identificación no basta.

### Corolario 24.9.5 — Una condición suficiente sobre el crecimiento de las derivadas
Sea $f:J\to\mathbb R$ infinitamente derivable en un intervalo abierto $J$ y $c\in J$. Supongamos que existen $d,M,A\in\mathbb R$ estrictamente positivos, con $K_d=[c-d,c+d]\subseteq J$, tales que

$$
\boxed{|f^{(n)}(t)|\le M\eta_n A^n
\qquad(n\ge1,\ t\in K_d).}
\tag{24.9.7}
$$

Entonces $f$ es real analítica en $c$. Más precisamente, para

$$
\rho:=\min\{d/2,\,1/(2A)\}>0
\tag{24.9.8}
$$

los restos satisfacen, para todos los $x\in K_\rho$ y $N\in\mathbb N$,

$$
\boxed{|E_N[f,c](x)|\le M(A|x-c|)^{N+1}
\le M2^{-(N+1)}.}
\tag{24.9.9}
$$

**Demostración.**
Fijemos $N$. Las restricciones $f^{(0)}\upharpoonright K_d,\ldots,f^{(N)}\upharpoonright K_d$ son continuas en $K_d$, pues son derivables en el abierto $J$, y forman la cadena diferencial finita de «Cadena diferencial finita sobre un intervalo cerrado» en su interior. La función final tiene derivada interior $f^{(N+1)}$, cuya magnitud está acotada por $M\eta_{N+1}A^{N+1}$ para todos los puntos del interior por (24.9.7). El corolario cerrado de Taylor–Lagrange «Cota uniforme para el resto de Taylor», aplicado con origen $c$ y extremo $x\in K_d$, da

$$
|f(x)-T_N[f,c](x)|\le
\frac{M\eta_{N+1}A^{N+1}}{\eta_{N+1}}|x-c|^{N+1}
=M(A|x-c|)^{N+1}.
\tag{24.9.10}
$$

La cancelación es legítima porque $\eta_{N+1}>0$. Por (24.9.8), $0<\rho\le d/2<d$ y $A\rho\le1/2$; de ahí (24.9.9) simultáneamente para todo $x\in K_\rho$. La geométrica de razón $1/2$ converge («Convergencia y suma de la serie geométrica para $»), así que los restos tienden uniformemente a cero en $K_\rho$; en particular, puntualmente en el abierto $(c-\rho,c+\rho)$. El teorema anterior prueba la analiticidad en $c$. La cota factorial uniforme (24.9.7) es una condición suficiente adicional, no una propiedad atribuida a toda función suave. $\square$

### Lema 24.9.6 — Construcción interna de una serie auxiliar entera
Definamos explícitamente $e:\mathbb N\to\mathbb R$ por $e_n:=1/\eta_n$, y su serie centrada en cero. La función suma, que denotaremos únicamente como auxiliar local a este desarrollo, satisface

$$
\boxed{\mathcal E:\mathbb R\to\mathbb R,
\quad\mathcal E(t)=\sum_{n=0}^{\infty}\frac{t^n}{\eta_n},
\quad\mathcal E'(t)=\mathcal E(t)\quad(t\in\mathbb R).}
\tag{24.9.11}
$$

Su radio es la marca formal infinita. Para todo $t\ge0$ y todo $m\in\mathbb N$,

$$
\boxed{\mathcal E(t)\ge1,
\qquad \mathcal E(t)\ge\frac{t^m}{\eta_m}>0\ \text{si }t>0.}
\tag{24.9.12}
$$

Estas afirmaciones se demostrarán sin importar funciones exponenciales, identidades de adición ni soluciones previamente supuestas de ecuaciones diferenciales.

**Demostración.**
La recurrencia $\eta_{n+1}=(n+1)\eta_n$ y su positividad son «Positividad y recurrencia de los factoriales». Así cada $e_n$ es un real único; Separación en $\mathbb N\times\mathbb R$ define la sucesión completa. Fijemos un real $t$ y pongamos $T:=|t|$. Si $T=0$, la serie es la suma del término inicial $1$ y todos los posteriores son cero. Si $T>0$, definamos $u_n:=T^n/\eta_n>0$. Por la propiedad arquimediana «Todo cuerpo ordenado completo es arquimediano» existe un índice que fijamos para este argumento $N\in\mathbb N$ suficientemente grande para que $n+1\ge2T$ cuando $n\ge N$. Entonces

$$
\frac{u_{n+1}}{u_n}=\frac{T}{n+1}\le\frac12
\qquad(n\ge N).
\tag{24.9.13}
$$

La inducción sobre $j$ da $u_{N+j}\le u_N2^{-j}$ para todos los naturales $j$. La serie geométrica de razón $1/2$ converge y una comparación de las sumas de esta cola, junto con los $N$ términos anteriores, prueba $\sum_n u_n<\infty$. Por tanto la serie original converge absolutamente en el real arbitrario $t$ («Criterio de comparación directa», «La convergencia absoluta implica convergencia ordinaria»), de modo que $C(e,0)=\mathbb R$ y su radio es infinito por «Radio finito y radio infinito» o «Clasificación por el radio y convergencia interior». La función $\mathcal E:=F_{e,0}:\mathbb R\to\mathbb R$ existe por «Existencia y unicidad de la función suma sobre su dominio exacto».

El coeficiente de la derivada formal es $(n+1)e_{n+1}=(n+1)/\eta_{n+1}=1/\eta_n=e_n$. La derivación término a término «Derivación término a término en el interior del radio» aplica en todo $\mathbb R$ por radio infinito y da $\mathcal E'=\mathcal E$. Si $t\ge0$, los sumandos $t^n/\eta_n$ son no negativos. Cada suma parcial es al menos el primer término, igual a $1$; asimismo, para $N\ge m$, es al menos el término $t^m/\eta_m$. Pasando a sus límites reales, la preservación del orden prueba ambas cotas de (24.9.12). Para $t>0$ el segundo término es positivo. Todos los pasos proceden de aritmética, comparación y convergencia ya construidas, sin importar la función exponencial bajo otro nombre como hipótesis. $\square$

### Teorema 24.9.7 — Existencia de una función suave que no es analítica
Existe una función $\phi:\mathbb R\to\mathbb R$ infinitamente derivable en toda la recta para la cual

$$
\boxed{\phi^{(k)}(0)=0\quad(k\in\mathbb N),
\qquad\phi(x)>0\quad(x>0).}
\tag{24.9.14}
$$

Por consiguiente, su serie de Taylor en el centro cero tiene radio infinito y suma la función nula, pero no representa a $\phi$ en ningún entorno abierto del centro. En particular, una función $C^\infty$ no tiene por qué ser real analítica.

**Demostración.**
**1. Una función tipada y positiva a la derecha.** Utilicemos la función $\mathcal E$ que acaba de construirse, no una función trascendental importada. Por (24.9.12), $\mathcal E(x^{-2})\ge1$ para todo $x>0$, por lo que la división siguiente es legítima. La regla por casos determina un único grafo en $\mathbb R\times\mathbb R$ mediante Separación:

$$
\boxed{\phi(x):=\begin{cases}
0,&x\le0,\\
\bigl[\mathcal E(x^{-2})\bigr]^{-1},&x>0.
\end{cases}}
\tag{24.9.15}
$$

Tenemos $\phi(0)=0$ y $0<\phi(x)\le1$ para $x>0$. La función es idénticamente cero en el semieje negativo, pero estrictamente positiva en el positivo.

**2. Cota de desaparición más rápida que cualquier potencia.** Para un entero natural arbitrario $m$ y $x>0$, apliquemos la segunda cota de (24.9.12) al argumento positivo $x^{-2}$. Obtenemos

$$
\mathcal E(x^{-2})\ge\frac{x^{-2m}}{\eta_m}>0,
\qquad 0<\phi(x)\le\eta_m x^{2m}.
\tag{24.9.16}
$$

La segunda desigualdad resulta de invertir dos reales estrictamente positivos; no introduce el límite de ninguna función exponencial. Para cada $m$ se dispone de una cota explícita válida para todo $x>0$.

**3. Forma de las derivadas en el semieje positivo.** En $x>0$ escribamos $z:=x^{-1}$. Las reglas de derivación del recíproco y de la composición («Regla de derivación del recíproco» y «Regla de la cadena en el dominio efectivo»), la fórmula de la derivada de $z^2$ y $\mathcal E'=\mathcal E$ dan

$$
\phi'(x)=\frac{-\mathcal E'(x^{-2})(-2x^{-3})}{\mathcal E(x^{-2})^2}
=2x^{-3}\phi(x)=2z^3\phi(x).
\tag{24.9.17}
$$

Construyamos ahora recursivamente los polinomios reales $P_k$ por $P_0(z)=1$ y

$$
\boxed{P_{k+1}(z):=-z^2P_k'(z)+2z^3P_k(z).}
\tag{24.9.18}
$$

Para precisar el conjunto de estados de la recursión, consideremos el subconjunto de $\mathbb R^{\mathbb N}$ de las sucesiones de coeficientes con soporte finito: consta de las $p$ para las que existe $d\in\mathbb N$ tal que $p_j=0$ para todo $j>d$, y existe por Separación en el conjunto de funciones ya construido. Cada sucesión de ese tipo determina un único polinomio real. La derivada de un polinomio es la suma finita de las derivadas de sus monomios, según «Derivación de las piezas polinómicas finitas» y las reglas de §19; multiplicarla por $-z^2$ o por $2z^3$, y sumar los resultados, vuelve a producir un polinomio de soporte finito. La fórmula (24.9.18) define así una operación total de valor único sobre ese conjunto de coeficientes. Con estado inicial $P_0=1$, la recursión natural de «Teorema de recursión sobre $\mathbb N$» construye la sucesión $k\mapsto P_k$, cuyos grafos polinómicos se obtienen por las fórmulas únicas, sin escoger polinomios. Por inducción, usando $z'=-z^2$, la regla de producto y (24.9.17), obtenemos

$$
\boxed{\phi^{(k)}(x)=\phi(x)P_k(x^{-1})
\qquad(x>0,\ k\in\mathbb N).}
\tag{24.9.19}
$$

En efecto, para $k=0$ esto es $P_0=1$; si vale a orden $k$, la derivada de su miembro derecho es $\phi(x)[2z^3P_k(z)-z^2P_k'(z)]$, exactamente la recurrencia propuesta.

**4. Derivabilidad de todos los órdenes en el centro.** Fijemos, *sin elección simultánea para distintos órdenes*, un $k\in\mathbb N$. Escribamos $P_k(z)=\sum_{j=0}^{d_k}p_{k,j}z^j$ con un grado finito $d_k\ge0$ que podemos tomar igual a cero para el polinomio nulo; pongamos $C_k:=1+\sum_{j=0}^{d_k}|p_{k,j}|>0$. Para $0<x\le1$, la desigualdad $x^{-j}\le x^{-d_k}$ si $j\le d_k$ proporciona

$$
|P_k(x^{-1})|\le C_kx^{-d_k}.
\tag{24.9.20}
$$

Combinemos (24.9.16) y (24.9.20) con el índice explícito $m:=d_k+2$. Resulta, para $0<x\le1$,

$$
\boxed{|\phi(x)P_k(x^{-1})|\le C_k\eta_m x^{2m-d_k},
\quad\left|\frac{\phi(x)P_k(x^{-1})}{x}\right|
\le C_k\eta_m x^{2m-d_k-1}.}
\tag{24.9.21}
$$

Los exponentes naturales $2m-d_k=d_k+4$ y $2m-d_k-1=d_k+3$ son estrictamente positivos; ambas cotas tienden a cero cuando $x\downarrow0$. En efecto, si $\varepsilon>0$, los exponentes son al menos uno y basta $0<x<\min\{1,\varepsilon/(C_k\eta_m)\}$ para que ambas magnitudes sean menores que $\varepsilon$. No se ha escogido $m$ a partir de infinitas desigualdades: su fórmula depende sólo del grado del polinomio ya determinado $P_k$.

Para cada $k$ definamos la función total $D_k:\mathbb R\to\mathbb R$ mediante $D_k(x)=0$ si $x\le0$ y $D_k(x)=\phi(x)P_k(x^{-1})$ si $x>0$. Se tiene $D_0=\phi$. En cada punto $x<0$, $D_k$ es localmente cero y su derivada vale cero. En $x>0$, el paso 3 y la recurrencia dan $D_k'(x)=D_{k+1}(x)$. En $x=0$, $D_k(0)=0$ y, para $h<0$, su cociente incremental es cero; para $0<h\le1$, el segundo límite en (24.9.21) da $D_k(h)/h\to0$. La derivada bilateral en cero existe, vale $0=D_{k+1}(0)$ y está justificada por la definición relativa en $\mathbb R$. Por tanto, para todo $k$,

$$
D_k'=D_{k+1}\text{ en }\mathbb R,
\qquad D_k(0)=0.
\tag{24.9.22}
$$

Por inducción, $D_k=\phi^{(k)}$ para todos los órdenes. Cada $D_k$ es continua: es derivable en toda la recta según acabamos de probar (también puede verificarse directamente con la primera cota). Así $\phi\in C^\infty(\mathbb R)$ y todas sus derivadas en cero se anulan.

**5. La serie converge, pero no representa la función.** De (24.9.14), la sucesión de Taylor de $\phi$ en cero es idénticamente nula: $t_k^{\phi,0}=0/\eta_k=0$ para todo $k$. Cada polinomio $T_N[\phi,0]$ es la función nula y su serie de potencias converge con radio infinito a cero sobre $\mathbb R$. Sin embargo, si $\delta>0$ es arbitrario, el punto explícito $x:=\delta/2$ satisface $0<x<\delta$ y $\phi(x)>0$. En ese punto,

$$
E_N[\phi,0](x)=\phi(x)>0\qquad\text{para todo }N,
\tag{24.9.23}
$$

por lo que el resto no tiende a cero. El criterio «Caracterización de la analiticidad por el resto de Taylor» descarta la analiticidad de $\phi$ en cero, a pesar de su suavidad y de la convergencia global de la serie de Taylor. La dificultad no es una serie divergente, sino la falta de igualdad con la función dada. $\square$

**Síntesis.** Una serie de potencias construye su función suma únicamente en el conjunto donde convergen sus sumas parciales. En el interior del radio, las mayoraciones geométricas justifican la continuidad y los intercambios con integración y derivación; las derivadas recuperan unívocamente los coeficientes. Para una función suave dada, en cambio, los coeficientes de Taylor no garantizan la igualdad con la función: ésta exige que el resto tienda a cero. La función $\phi$ muestra que incluso una serie de Taylor de radio infinito puede tener una suma diferente de la función que la originó. Así se cierra el puente entre convergencia funcional, cálculo diferencial e integral y analiticidad real, sin atribuir a las fronteras del radio propiedades que no han sido demostradas.
