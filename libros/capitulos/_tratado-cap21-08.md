## 21.8. Integrabilidad de las funciones monótonas {#sec-ta-21-8}

La continuidad uniforme permite hacer pequeñas todas las oscilaciones locales. La monotonía ofrece un mecanismo diferente: la oscilación sobre cada subintervalo es exactamente la diferencia entre los valores en sus extremos, y la suma de esas diferencias se telescopa. Las oscilaciones individuales no necesitan ser pequeñas; basta multiplicar su suma total por anchuras suficientemente reducidas. Reutilizaremos la definición de monotonía de §20.5 (Definición §20.5.1 — Monotonía estricta y no estricta sobre un dominio ordenado), sin presuponer una derivada ni continuidad.

Fijemos primero $a<b$, $I=[a,b]$, una función tipada $f:I\to\mathbb R$ y una partición $P=\langle n,p\rangle$, con nodos $a=x_0<\cdots<x_n=b$. Todas las diferencias y anchuras siguientes son reales; los índices siguen siendo naturales.

### Lema 21.8.1 — Cotas y extremos locales de una función monótona
Si $f$ es no decreciente, entonces

$$
 f(a)\le f(t)\le f(b)\quad(t\in I),\qquad
 m_k(P)=f(x_k),\quad M_k(P)=f(x_{S(k)}).
 \tag{21.8.1}
$$

Si $f$ es no creciente, entonces

$$
 f(b)\le f(t)\le f(a)\quad(t\in I),\qquad
 m_k(P)=f(x_{S(k)}),\quad M_k(P)=f(x_k).
 \tag{21.8.2}
$$

En ambos casos $f$ está acotada y, para cada $k<n$,

$$
 \boxed{\omega_k(P)=|f(x_{S(k)})-f(x_k)|.}
 \tag{21.8.3}
$$

**Demostración.**
Para $a\le t\le b$, la definición de función no decreciente, aplicada a los pares $a<t$ y $t<b$ cuando sean estrictos, da $f(a)\le f(t)\le f(b)$; en caso de igualdad de argumentos, la correspondiente desigualdad es reflexiva. Así, $A=f(a)$ y $B=f(b)$ son dos cotas globales concretas. Sobre $I_k(P)=[x_k,x_{S(k)}]$ vale $f(x_k)\le f(t)\le f(x_{S(k)})$ para cada $t$. Como ambos extremos del subintervalo pertenecen a él, las dos cotas de valores se alcanzan y son respectivamente el ínfimo y el supremo; la existencia y unicidad de estos números están garantizadas por Lema §21.2.2 — Existencia de las cotas extremas locales y comparación por inclusión. Esto demuestra (21.8.1).

Para $f$ no creciente, las desigualdades se invierten, sus cotas globales pasan a ser $A=f(b)$ y $B=f(a)$, y los extremos locales intercambian papeles. La resta $M_k(P)-m_k(P)$ es en cada caso la diferencia positiva correspondiente, equivalente al valor absoluto de la diferencia de los valores extremos por Definición §4.2.1 — Valor absoluto. No se requiere continuidad en ningún nodo. $\square$

### Proposición 21.8.2 — Identidad telescópica y estimación de la brecha
Si $f$ es monótona en $I$, entonces, para toda partición $P$,

$$
 \boxed{\sum_{k=0}^{n-1}\omega_k(P)=|f(b)-f(a)|.}
 \tag{21.8.4}
$$

En consecuencia, para cada real $\delta>0$ tal que $\Delta_k(P)<\delta$ para todos los $k<n$,

$$
 \boxed{0\le G(f,P)=U(f,P)-L(f,P)
 \le\delta\,|f(b)-f(a)|.}
 \tag{21.8.5}
$$

Para la partición equidistante de (21.7.2), de anchura común $h=(b-a)/\nu_{\mathbb R}(n)$, se tiene incluso la identidad $G(f,P)=h\,|f(b)-f(a)|$.

**Demostración.**
Si $f$ es no decreciente, Lema §21.8.1 — Cotas y extremos locales de una función monótona da $\omega_k(P)=f(x_{S(k)})-f(x_k)\ge0$. La identidad de suma finita por bloques Proposición §14.2.2 — Identidades de los bloques de sumación, o equivalentemente una inducción en $n$ como la de §21.1, cancela cada valor interior una vez con cada signo:

$$
 \sum_{k<n}\omega_k(P)
 =\sum_{k<n}\bigl(f(x_{S(k)})-f(x_k)\bigr)
 =f(x_n)-f(x_0)=f(b)-f(a).
$$

Ésta es (21.8.4), pues la última diferencia es no negativa. Para $f$ no creciente, cada oscilación es $f(x_k)-f(x_{S(k)})$ y la misma cancelación da $f(a)-f(b)=|f(b)-f(a)|$. La función constante satisface ambas demostraciones y produce suma cero.

La identidad de Darboux Proposición §21.2.5 — Encierro global e identidad de la brecha y la no negatividad de cada oscilación permiten multiplicar $\Delta_k(P)<\delta$ por $\omega_k(P)\ge0$ y sumar:

$$
 0\le G(f,P)=\sum_{k<n}\omega_k(P)\Delta_k(P)
 \le\sum_{k<n}\omega_k(P)\delta
 =\delta\sum_{k<n}\omega_k(P)
 =\delta|f(b)-f(a)|.
$$

La comparación de sumas finitas es Proposición §14.5.1 — Comparación de sumas finitas y de bloques. Si todas las anchuras son la misma cantidad $h$, se obtiene igualdad en la extracción del factor. En esta prueba no se afirma que exista una anchura máxima seleccionada ni se introduce notación de malla. $\square$

**Lectura de la estimación.** No es necesario que $\omega_k(P)$ tienda a cero en la celda que contiene un salto. Lo que permanece acotado es la suma no ponderada de las oscilaciones: es exactamente la variación neta entre los dos extremos, por monotonía.

### Teorema 21.8.3 — Toda función monótona sobre un intervalo cerrado es integrable
Sean $a,b\in\mathbb R$ con $a\le b$ y $f:[a,b]\to\mathbb R$ monótona en el sentido de Definición §20.5.1 — Monotonía estricta y no estricta sobre un dominio ordenado. Entonces $f$ es integrable en $[a,b]$, aunque no sea continua. Cuando $a<b$, para cada $\varepsilon>0$ existe un $\delta>0$ tal que toda partición con $\Delta_k(P)<\delta$ verifica $G(f,P)<\varepsilon$.

**Demostración.**
Si $a=b$, el dominio es el singleton $[a,a]$ y la integrabilidad, con integral cero, está definida en Definición §21.6.5 — Integración en un intervalo degenerado; no se invoca una partición estricta. Supongamos $a<b$. El lema Lema §21.8.1 — Cotas y extremos locales de una función monótona demuestra primero que $f$ está acotada, por lo que las sumas de Darboux y su brecha están definidas. Fijemos $\varepsilon>0$ y escribamos el real no negativo $D:=|f(b)-f(a)|$. Elijamos para esta tolerancia

$$
 \delta:=\frac{\varepsilon}{D+1_{\mathbb R}}>0.
 \tag{21.8.6}
$$

El denominador es positivo y $D<D+1_{\mathbb R}$, luego $\delta D<\varepsilon$; esto sigue siendo cierto cuando $D=0$. Si $P$ tiene todas sus anchuras menores que $\delta$, (21.8.5) da

$$
 0\le G(f,P)\le\delta D<\varepsilon.
 \tag{21.8.7}
$$

El lema Lema §21.7.1 — Particiones equidistantes de anchura arbitrariamente pequeña construye una partición estricta con esas anchuras: para el $\delta$ ya fijado proporciona un único testigo finito requerido, sin elegir una sucesión de particiones. La brecha correspondiente satisface el criterio de Darboux Teorema §21.4.2 — Criterio de Darboux y estabilidad por refinamiento, que concluye la integrabilidad. No se utilizó el corolario sobre funciones continuas, ninguna derivada ni el teorema fundamental del cálculo. $\square$

### Proposición 21.8.4 — Ejemplo explícito: una función monótona integrable con un salto
Sean $a<c<b$. Definamos la función de dominio exactamente $I=[a,b]$ y codominio $\mathbb R$ por

$$
 s_c(t):=\begin{cases}
 0_{\mathbb R},&a\le t<c,\\
 1_{\mathbb R},&c\le t\le b.
 \end{cases}
 \tag{21.8.8}
$$

Entonces $s_c$ es no decreciente, acotada e integrable en $[a,b]$, pero no es continua en $c$ con respecto al dominio $I$.

**Demostración.**
Las ramas $a\le t<c$ y $c\le t\le b$ son disjuntas y cubren $I$. Separar del producto $I\times\mathbb R$ los pares determinados por (21.8.8) construye el grafo de una función tipada; cada argumento recibe un solo real. Si $u<v$ están ambos a la izquierda de $c$ o ambos a su derecha, $s_c(u)=s_c(v)$. Si $u<c\le v$, entonces $s_c(u)=0_{\mathbb R}<1_{\mathbb R}=s_c(v)$. Se cumple por tanto la definición de no decreciente. Las cotas $0_{\mathbb R}\le s_c(t)\le1_{\mathbb R}$ son explícitas y la integrabilidad resulta de Teorema §21.8.3 — Toda función monótona sobre un intervalo cerrado es integrable.

Para comprobar que la continuidad falla en $c$, fijemos $\varepsilon_0:=1_{\mathbb R}/2_{\mathbb R}>0$. Dado cualquier $\delta>0$, definamos $r:=\min\{\delta,c-a\}>0$ por totalidad del orden real y $x:=c-r/2_{\mathbb R}$. Se verifica $a<x<c$, $0<|x-c|=r/2_{\mathbb R}<\delta$, pero

$$
 |s_c(x)-s_c(c)|=|0_{\mathbb R}-1_{\mathbb R}|
 =1_{\mathbb R}>\varepsilon_0.
$$

Por la negación de la definición de continuidad relativa de Definición §17.1.1 — Continuidad relativa al dominio en un punto, $s_c$ no es continua en $c$. El punto $x$ se obtiene por fórmula para cada $\delta$; no hay selección de una familia numerable. $\square$

### Proposición 21.8.5 — Cálculo directo de la integral de la función escalón
Para la función $s_c:[a,b]\to\mathbb R$ de (21.8.8),

$$
 \boxed{\int_a^b s_c=b-c.}
 \tag{21.8.9}
$$

**Demostración.**
La integral $J:=\int_a^b s_c$ existe por Proposición §21.8.4 — Ejemplo explícito: una función monótona integrable con un salto. Consideremos primero la partición con nodos $a<c<b$. En $[a,c]$ la función toma tanto $0$ como $1$, de modo que su ínfimo es $0$ y su supremo es $1$; en $[c,b]$ es constantemente $1$. Por definición de la suma inferior,

$$
 L(s_c,\{a,c,b\})=0\,(c-a)+1\,(b-c)=b-c.
 \tag{21.8.10}
$$

La escritura abreviada de la lista de nodos representa aquí la partición tipada única que dicha lista determina (Lema §21.2.7 — Una lista estricta queda determinada por sus nodos). Por el encierro Proposición §21.4.4 — Encierro del valor integral y control por la brecha, tenemos $b-c\le J$.

Ahora, para cualquier $h$ con $0<h<c-a$, formemos la partición de nodos $a<c-h<c<b$. Sus tres subintervalos son $[a,c-h]$, $[c-h,c]$ y $[c,b]$. Sobre el primero $s_c$ es nula, sobre el tercero es uno y sólo el segundo contiene los dos valores $0$ y $1$. Se obtiene exactamente

$$
 U(s_c,P_h)=0\,(c-h-a)+1\,h+1\,(b-c)=b-c+h.
 \tag{21.8.11}
$$

El encierro de la integral da $J\le b-c+h$. Si $J>b-c$, elijamos el único real explícito $h:=\frac12\min\{c-a,J-(b-c)\}>0$; entonces $h<c-a$ y $h<J-(b-c)$, de modo que $J\le b-c+h<J$, contradicción. Por totalidad del orden, $J\le b-c$. Combinando con la cota inferior concluimos (21.8.9), sin recurrir a primitivas, a sumas etiquetadas ni a un teorema de paso al límite. $\square$

**Cierre de la unidad.** Hemos construido una clase de funciones integrables que contiene funciones discontinuas y hemos calculado un ejemplo directamente desde las sumas de Darboux. Continuidad y monotonía son condiciones suficientes alternativas, no condiciones necesarias en la definición. La próxima sección desarrollará las sumas etiquetadas y su relación con la integral de Darboux; hasta entonces no se asumirá su equivalencia.
