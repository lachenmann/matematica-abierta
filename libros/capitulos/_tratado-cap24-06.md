## 24.6. Integración término a término en el interior del radio {#sec-ta-24-6}

La uniformidad demostrada en §24.5 permite integrar una serie de potencias sobre intervalos cerrados estrictamente interiores. Debemos separar tres operaciones que no son intercambiables por definición: la integración de cada monomio, el paso al límite de las sumas parciales y la construcción de una primitiva de la función suma. En particular, el tratado sólo define hasta aquí la integral de Riemann con extremos ordenados. En toda esta sección $I$ denota el dominio abierto interior de «Continuidad de la función suma en el interior»: $(c-R,c+R)$ para $0<R\in\mathbb R$, y $\mathbb R$ para radio formal infinito. Si $R=0$, no se afirma un resultado de integración sobre un intervalo interior de longitud positiva.

### Lema 24.6.1 — Integral de cada monomio centrado sobre un intervalo ordenado
Fijemos $a:\mathbb N\to\mathbb R$, $c\in\mathbb R$, $n\in\mathbb N$ y reales $u\le v$. La restricción $p_n^{a,c}\upharpoonright[u,v]:[u,v]\to\mathbb R$ es integrable y

$$
\boxed{\int_u^v\bigl(p_n^{a,c}\upharpoonright[u,v]\bigr)
=\frac{a_n}{n+1}\bigl((v-c)^{n+1}-(u-c)^{n+1}\bigr).}
\tag{24.6.1}
$$

Cuando $n+1$ interviene en una operación real, designa su imagen canónica $\nu_{\mathbb R}(n+1)$, que es estrictamente positiva porque $n+1\ge1$; se invierte esa imagen real, sin identificar literalmente los dos conjuntos numéricos. Cuando $u=v$ se usa la integral del singleton, no un teorema formulado sólo para intervalos no degenerados.

**Demostración.**
Primero verificamos la identidad diferencial para potencias naturales, sin presuponer la regla general. Sea $z(x)=x-c$ en $\mathbb R$. La derivada de $z$ es $1$, pues es afín («Primeros cálculos: funciones afines y función cuadrática»). Por inducción, para cada $k\ge1$ la función $z^k$ es derivable y $(z^k)'=kz^{k-1}$: el caso $k=1$ es la derivada de $z$; si vale en $k$, la regla del producto «Regla de derivación del producto» aplicada a $z^{k+1}=z^kz$ entrega

$$
(z^{k+1})'=kz^{k-1}z+z^k\cdot1=(k+1)z^k.
\tag{24.6.2}
$$

La identidad $z^{k-1}z=z^k$ procede de la recursión de potencias. En particular, con $k=n+1$, la función explícita

$$
H_n:\mathbb R\to\mathbb R,\qquad
H_n(x):=\frac{a_n}{n+1}(x-c)^{n+1}
\tag{24.6.3}
$$

es derivable con $H_n'=a_n(x-c)^n=p_n^{a,c}$ por la regla de escalar «Multiplicación por escalares, opuestos y diferencias»; las dos funciones son continuas por «Todo polinomio real es continuo en la recta» y estabilidad algebraica. Si $u<v$, la restricción del monomio al cerrado es integrable por «Toda función continua en un intervalo cerrado es integrable», y la restricción de $H_n$ es continua en el cerrado y derivable en el abierto, con derivada igual al monomio restringido. Por tanto satisface la definición de primitiva «Primitiva sobre un intervalo cerrado», y Newton–Leibniz «Regla de Newton–Leibniz para integrandas integrables que admiten primitiva» da $H_n(v)-H_n(u)$, exactamente (24.6.1). Si $u=v$, «Integración en un intervalo degenerado» asigna cero a la integral del singleton, mientras que $H_n(v)-H_n(u)=0$. Las funciones se definieron mediante fórmulas únicas y sus restricciones mediante grafos, sin seleccionar primitivas para una familia de índices. $\square$

### Teorema 24.6.2 — Integración término a término y convergencia absoluta de las integrales
Supongamos que el radio $R(a,c)$ es finito positivo o infinito en el sentido de «Radio finito y radio infinito». Sean extremos ordenados $u,v\in I$ con $u\le v$. La restricción de la función suma $F_{a,c}\upharpoonright[u,v]$ es integrable, la serie real de las integrales de los términos converge absolutamente, y vale

$$
\boxed{
\int_u^v\bigl(F_{a,c}\upharpoonright[u,v]\bigr)
=\sum_{n=0}^{\infty}\frac{a_n}{n+1}
\bigl((v-c)^{n+1}-(u-c)^{n+1}\bigr).}
\tag{24.6.4}
$$

La suma de la derecha denota un número real sólo tras verificar su convergencia. Más precisamente, para $r:=\max\{|u-c|,|v-c|\}$, existen $M>0$ y $0\le q<1$ tales que, para cada $N\in\mathbb N$,

$$
\boxed{\left|\int_u^v(F_{a,c}\upharpoonright[u,v])
-\sum_{n=0}^{N}\frac{a_n}{n+1}
\bigl((v-c)^{n+1}-(u-c)^{n+1}\bigr)\right|
\le(v-u)\frac{Mq^{N+1}}{1-q}.}
\tag{24.6.5}
$$

**Demostración.**
**1. Dominio común.** El real $r\ge0$ está bien definido por un máximo finito. Si $R\in\mathbb R$ y $R>0$, las hipótesis $u,v\in(c-R,c+R)$ dan $r<R$; si $R=+\infty$, $r$ es un real no negativo admisible sin efectuar comparación aritmética con $+\infty$. Todo $x\in[u,v]$ satisface $|x-c|\le r$, por análisis de los casos $x\ge c$ y $x\le c$ o por convexidad elemental del intervalo; por tanto $[u,v]\subseteq K_r=[c-r,c+r]\subseteq I$. La pertenencia de $u,v$ a $I$ garantiza que sus restricciones de $F_{a,c}$ y de los términos tienen dominio exacto $[u,v]$.

**2. Hipótesis del intercambio.** «Convergencia absoluta uniforme y cota geométrica del resto», aplicado una sola vez a $K_r$, suministra números $M>0$, $0\le q<1$ tales que $|p_n^{a,c}(x)|\le Mq^n$ simultáneamente para todo $n$ y todo $x\in K_r$. La misma cota sirve para todos los puntos de $[u,v]$, y $\sum Mq^n$ converge por «Convergencia y suma de la serie geométrica para $». Cada monomio restringido es continuo e integrable por el lema 24.6.1; por ello se cumplen todas las hipótesis de «Integración término a término de una serie dominada», incluida la dominación de Weierstrass. Este corolario demuestra primero la integrabilidad de la suma restringida, luego la convergencia de la serie numérica de integrales y finalmente el intercambio

$$
\int_u^v(F_{a,c}\upharpoonright[u,v])
=\sum_{n=0}^{\infty}\int_u^v(p_n^{a,c}\upharpoonright[u,v]).
\tag{24.6.6}
$$

En el caso $u=v$ el corolario utiliza la convención integral del singleton, de modo que ambas partes son cero.

**3. Evaluación y convergencia absoluta.** El lema anterior proporciona la fórmula explícita (24.6.1) para cada sumando de (24.6.6), lo cual prueba (24.6.4). Como $-Mq^n\le p_n^{a,c}(x)\le Mq^n$ para cada $x\in[u,v]$, la estimación de integrales por cotas constantes «Positividad y estimaciones por cotas constantes» asegura

$$
\left|\int_u^v(p_n^{a,c}\upharpoonright[u,v])\right|
\le(v-u)Mq^n.
\tag{24.6.7}
$$

Si $u=v$, ambos lados valen cero por definición; si $u<v$, se usa el resultado de cotas ordinario. La serie geométrica multiplicada por el real no negativo $v-u$ converge, también cuando ese factor es cero. El criterio de comparación «Criterio de comparación directa» demuestra convergencia de la serie de magnitudes de las integrales y, por «Serie de valores absolutos; convergencia absoluta y condicional», convergencia absoluta.

**4. Control de error.** Por linealidad *finita* de la integral, ya incorporada en «Integración término a término de una serie dominada», la suma de las primeras $N+1$ integrales es $\int_u^v(S_N^{a,c}\upharpoonright[u,v])$. En el cerrado $K_r$ la cota (24.5.3) da $|F_{a,c}(x)-S_N^{a,c}(x)|\le Mq^{N+1}/(1-q)$ para todos los puntos del intervalo de integración. Ambas funciones son integrables; su diferencia lo es por linealidad, y «Positividad y estimaciones por cotas constantes» acota su integral por la longitud $v-u$ multiplicada por esa constante. Esto prueba (24.6.5); $1-q>0$ hace legítimo el denominador y el resto geométrico tiende a cero. No se ha usado linealidad infinita como premisa ni se han elegido integrales simultáneamente: cada valor tiene unicidad y la sucesión es su grafo funcional. $\square$

**Alcance de los extremos.** En (24.6.4) no se integra hasta $c\pm R$ cuando $R$ es finito. Aunque la serie pueda converger en alguno de esos puntos, §24.5 no aseguró convergencia uniforme en un cerrado que toque la frontera. Tal ampliación requeriría hipótesis y una prueba adicionales.

### Corolario 24.6.3 — Serie de primitivas centrada y estimación uniforme
Bajo las hipótesis de radio del teorema anterior existe una única función $H_{a,c}:I\to\mathbb R$ determinada por

$$
\boxed{H_{a,c}(x):=\sum_{n=0}^{\infty}
\frac{a_n}{n+1}(x-c)^{n+1},\qquad x\in I.}
\tag{24.6.8}
$$

La serie converge absoluta y uniformemente sobre cada $K_r$ admisible de §24.5. Satisface $H_{a,c}(c)=0$ y, para cada $x\in I$, puede expresarse solamente por integrales con extremos ordenados:

$$
\boxed{H_{a,c}(x)=
\begin{cases}
\displaystyle\int_c^x(F_{a,c}\upharpoonright[c,x]),&x\ge c,\\[4pt]
\displaystyle-\int_x^c(F_{a,c}\upharpoonright[x,c]),&x<c.
\end{cases}}
\tag{24.6.9}
$$

Para los parámetros $M,q$ de «Convergencia absoluta uniforme y cota geométrica del resto» asociados a $K_r$ y para $x\in K_r$ se tiene

$$
\boxed{\left|H_{a,c}(x)-\sum_{n=0}^{N}\frac{a_n}{n+1}(x-c)^{n+1}\right|
\le r\frac{Mq^{N+1}}{1-q}.}
\tag{24.6.10}
$$

**Demostración.**
Sea $x\in I$. Existe un real $r\ge|x-c|$ que satisface las condiciones de §24.5: si el radio es finito positivo, tomamos $r:=(|x-c|+R)/2<R$; si es infinito, $r:=|x-c|+1$. Al aplicar «Convergencia absoluta uniforme y cota geométrica del resto» a $K_r$, obtenemos una sola pareja $M,q$ con $|a_n(t-c)^n|\le Mq^n$ para $t\in K_r$. Para todo $t\in K_r$ y $n\ge0$,

$$
\left|\frac{a_n}{n+1}(t-c)^{n+1}\right|
=\frac{|t-c|}{n+1}|a_n(t-c)^n|
\le rMq^n,
\tag{24.6.11}
$$

ya que $n+1\ge1$. La comparación geométrica y el criterio $M$ «Criterio $M$ de Weierstrass y estimación del resto» demuestran convergencia absoluta y uniforme de la serie de (24.6.8) en $K_r$; en particular, existe un límite real único para el $x$ fijado. Como $x$ es arbitrario y los límites son únicos, la Separación en $I\times\mathbb R$ construye el grafo de $H_{a,c}$ con dominio exacto $I$, sin una elección numerable de valores. Si $x=c$, cada sumando es cero porque su exponente es $n+1\ge1$, de donde $H_{a,c}(c)=0$.

Para $x\ge c$, el intervalo $[c,x]$ está contenido en $I$; «Integración término a término y convergencia absoluta de las integrales», con $u=c$ y $v=x$, prueba que su integral es la serie de (24.6.8), ya que $(c-c)^{n+1}=0$. Para $x<c$, se aplica ese mismo teorema a los extremos ordenados $x\le c$: la integral $\int_x^c$ vale $-\sum a_n(x-c)^{n+1}/(n+1)$, y su opuesto es $H_{a,c}(x)$. Finalmente, volvamos a la única cota común (24.6.11), obtenida antes de variar $x$: para todo $t\in K_r$ y todo $n$, el valor absoluto del término integrado es a lo sumo $rMq^n$. El criterio $M$ «Criterio $M$ de Weierstrass y estimación del resto», aplicado a esta misma sucesión mayorante, acota la cola tras el índice $N$ por $\sum_{n=N+1}^{\infty}rMq^n=rMq^{N+1}/(1-q)$, simultáneamente para todos los $t\in K_r$. Ésta es exactamente (24.6.10), con los mismos $M,q$ para todo el cerrado; no se transfieren indebidamente parámetros existenciales de las integrales de intervalos variables. La coincidencia entre las expresiones puntuales y la uniformidad en $K_r$ no exige uniformidad sobre todo $I$. $\square$

### Teorema 24.6.4 — La serie integrada es una primitiva normalizada de la función suma
Bajo las hipótesis de radio de esta sección, $H_{a,c}:I\to\mathbb R$ es derivable en todo punto de $I$ y

$$
\boxed{H_{a,c}'(x)=F_{a,c}(x)\quad(x\in I),\qquad H_{a,c}(c)=0.}
\tag{24.6.12}
$$

Por consiguiente es la única primitiva de $F_{a,c}\upharpoonright I$ que se anula en $c$, entre las funciones derivables sobre $I$. Esta afirmación no deriva término a término la serie de potencias inicial: deriva la función suma de la serie integrada mediante el teorema fundamental del cálculo.

**Demostración.**
Fijemos $x_0\in I$. Escojamos el radio real explícito $r:=(|x_0-c|+R)/2$ si $0<R\in\mathbb R$, o $r:=|x_0-c|+1$ si el radio es infinito. Entonces $|x_0-c|<r$, $c\in K_r$ y $x_0$ es interior de $K_r=[c-r,c+r]\subseteq I$. La función $f:=F_{a,c}\upharpoonright K_r$ es continua en todo $K_r$ por «Continuidad de la función suma en el interior», luego integrable por «Toda función continua en un intervalo cerrado es integrable». Su acumulada ordinaria, con origen $\alpha:=c-r$, es la función tipada $A:=F_{f,\alpha}:K_r\to\mathbb R$ de «Función integral acumulada». La primera parte del teorema fundamental («Integranda continua sobre todo el intervalo») da

$$
A'(x_0)=f(x_0)=F_{a,c}(x_0).
\tag{24.6.13}
$$

Para todo $x\in K_r$, «Valores extremos e identidad exacta de los incrementos» proporciona, cuando $x\ge c$, la identidad $A(x)-A(c)=\int_c^x(f\upharpoonright[c,x])$; cuando $x<c$ proporciona $A(c)-A(x)=\int_x^c(f\upharpoonright[x,c])$. Las restricciones de $f$ coinciden con las de $F_{a,c}$ por igualdad tipada. La fórmula ordenada (24.6.9) implica entonces, en ambos casos,

$$
H_{a,c}(x)=A(x)-A(c)\qquad(x\in K_r).
\tag{24.6.14}
$$

Restar una constante no altera la derivada («Multiplicación por escalares, opuestos y diferencias»); como $x_0$ es interior de $K_r$ y la función global $H_{a,c}$ coincide con $A-A(c)$ en un entorno de $x_0$, los cocientes incrementales coinciden allí, y (24.6.13) prueba $H_{a,c}'(x_0)=F_{a,c}(x_0)$. El punto era arbitrario, así que (24.6.12) vale en todo $I$; el valor en $c$ ya se estableció en el corolario anterior.

Para la unicidad, sea $G:I\to\mathbb R$ otra función derivable con $G'=F_{a,c}$ y $G(c)=0$. Fijemos $x\in I$ y un cerrado $K_r$ que contenga $c$ y $x$ estrictamente en su interior, como antes. La función $G-H_{a,c}$ es continua en $K_r$ y derivable en su interior, con derivada idénticamente cero; por el corolario de constancia del teorema del valor medio «Derivada idénticamente nula si y sólo si la función es constante», su restricción es constante. Al evaluar en $c$ su valor es $0$, por lo que $G(x)=H_{a,c}(x)$. Como $x$ era arbitrario, la igualdad de grafos tipados «Criterio de igualdad de funciones» da $G=H_{a,c}$. No se ha escogido una familia de primitivas: la función $H_{a,c}$ se construyó explícitamente a partir de una serie con límite único. $\square$

**Balance y transición.** La integración término a término está autorizada únicamente en cerrados interiores; la serie integrada proporciona una primitiva normalizada sobre $I$ y dispone de un resto uniforme calculable a partir de $M,q$. El paso inverso —derivar la serie original término a término— no se obtiene intercambiando informalmente derivada y límite: deberá demostrarse antes que la serie de funciones derivadas posee control uniforme en cada cerrado interior y que conserva el radio apropiado. Esa será la materia de §24.7. No se abre un checkpoint Lean adicional.

---
