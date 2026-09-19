## 13.11. Teorema de Bolzano--Weierstrass {#sec-ta-13-11}

En §13.10 aprendimos a reconocer un punto límite secuencial y comprobamos que los puntos límite de una sucesión acotada, si existen, respetan sus cotas. Todavía falta demostrar que **existe al menos uno**. El problema no se resuelve eligiendo un término de cada cola: tales términos podrían oscilar sin aproximarse a ningún número. Debemos seleccionar simultáneamente una región cada vez más estrecha y unos índices que continúen avanzando.

La estrategia consiste en partir de un intervalo cerrado que contenga toda la sucesión y bisecarlo sucesivamente. Conservar una mitad no exige que contenga *todos* los términos restantes: basta que siga recibiendo términos después de cualquier umbral. La regla «izquierda si sirve; derecha en caso contrario» fija la elección de la mitad. Una vez construidos los intervalos, el buen orden de $\mathbb N$ permitirá seleccionar el menor índice admisible en cada etapa. Esta separación entre **reducir el espacio de valores** y **hacer crecer los índices** es el mecanismo fundamental de la prueba.

### Definición 13.11.1 — Intervalo recurrente para una sucesión

Sea $a=(a_n)$ una sucesión real y sean $p,q\in\mathbb R$ con $p\le q$. Diremos que el intervalo cerrado $[p,q]$ es **recurrente para $a$** si

$$
\boxed{
\forall N\in\mathbb N\;\exists n\in\mathbb N,
\qquad N\le n\ \text{y}\ p\le a_n\le q.
}
$$

Equivalentemente, el conjunto de índices

$$
E_a[p,q]:=\{n\in\mathbb N:p\le a_n\le q\}
$$

corta todos los segmentos finales $\mathbb N_{\ge N}$. Existe por Separación dentro de $\mathbb N$. La expresión $E_a[p,q]$ es una abreviatura local para la demostración siguiente, no una nueva noción topológica.

> **Dos cuantificadores que no deben intercambiarse.** La recurrencia es $\forall N\,\exists n\ge N$; la pertenencia eventual al intervalo sería $\exists N\,\forall n\ge N$. Un intervalo puede ser recurrente sin contener toda la cola. Por ejemplo, la sucesión alternante de ceros y unos visita $[0,0]$ arbitrariamente tarde, pero no pertenece eventualmente a ese intervalo.

---

### Lema 13.11.2 — Una mitad de un intervalo recurrente sigue siendo recurrente

Sea $[p,q]$ recurrente para $a$. Definamos

$$
\boxed{h:=(1+1)^{-1},\qquad m:=(p+q)h.}
$$

Entonces $h>0$, $h+h=1$, $p\le m\le q$, y **al menos uno** de los intervalos

$$
[p,m],\qquad[m,q]
$$

es recurrente para $a$. En particular, la regla

$$
\boxed{
\begin{cases}
[p,m],&\text{si }[p,m]\text{ es recurrente},\\
[m,q],&\text{en caso contrario}
\end{cases}
}
$$

determina un único intervalo recurrente contenido en $[p,q]$, cuya anchura es la mitad de $q-p$.

**Demostración.**

Por Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado (3), $1>0$. Al sumar $1$ resulta $1<1+1$; por tanto $s:=1+1>0$ y su inverso $h=s^{-1}$ es positivo por Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado (6). Como $sh=1$ y la distributividad da $sh=h+h$, se tiene $h+h=1$. De $p\le q$, la compatibilidad multiplicativa por $h>0$ y la invariancia del orden bajo traslación implican

$$
0\le(q-p)h,
\qquad
p\le p+(q-p)h=(p+q)h=m.
$$

Análogamente $0\le(q-p)h=q-m$, luego $m\le q$. Las identidades anteriores muestran también

$$
\boxed{m-p=h(q-p)=q-m.}
$$

Las dos mitades cubren el intervalo original:

$$
\boxed{[p,q]=[p,m]\cup[m,q].}
$$

En efecto, cualquier $x\in[p,q]$ satisface $x\le m$ o $m\le x$ por totalidad del orden, y pertenece respectivamente a la primera o a la segunda mitad. La inclusión contraria es inmediata de $p\le m\le q$.

Si $[p,m]$ es recurrente, ya tenemos la mitad requerida. Supongamos, en cambio, que **no** es recurrente. Negando clásicamente los cuantificadores de Definición 13.11.1 — Intervalo recurrente para una sucesión, existe un umbral $N_0\in\mathbb N$ tal que

$$
n\ge N_0\Longrightarrow a_n\notin[p,m].
$$

Fijemos un umbral arbitrario $N$. Por totalidad del orden natural, el mayor de $N$ y $N_0$ es un natural $K$. Como $[p,q]$ es recurrente, existe $n\ge K$ con $a_n\in[p,q]$. En particular, $n\ge N_0$; por tanto $a_n\notin[p,m]$. La igualdad de unión recién demostrada obliga a que

$$
a_n\in[m,q].
$$

Además $n\ge N$. Como $N$ era arbitrario, $[m,q]$ es recurrente. La alternativa clásica «la mitad izquierda es recurrente o no lo es» fija cuál de las dos mitades se toma; no selecciona un elemento arbitrario de ninguna familia. La anchura de la mitad seleccionada es, en ambos casos, $h(q-p)$. ∎

> **Auditoría de decisión.** El predicado «este intervalo es recurrente» cuantifica sobre infinitos índices y comparaciones reales; no se ha demostrado decidible. La regla anterior es una *definición por casos en lógica clásica*, no un algoritmo de bisección certificado. Al ser única la salida de cada caso, la operación resultante puede construirse como función por Separación, sin Choice.

---

### Proposición 13.11.3 — Bisección recursiva canónica

Sea $a=(a_n)$ una sucesión real acotada. Fijemos $M\ge0$ tal que $|a_n|\le M$ para todo $n$, y conservemos $h=(1+1)^{-1}$. Existen sucesiones reales

$$
l=(l_k)_{k\in\mathbb N},
\qquad
u=(u_k)_{k\in\mathbb N}
$$

**unívocamente determinadas por la regla de bisección** del lema anterior, que cumplen:

1. $l_0=-M$ y $u_0=M$;
2. cada intervalo $I_k:=[l_k,u_k]$ es recurrente para $a$;
3. $I_{k+1}\subseteq I_k$ para todo $k$;
4. si $w_k:=u_k-l_k$ es su anchura, entonces
   $$
   \boxed{w_k\ge0,\qquad w_{k+1}=h\,w_k.}
   $$

**Demostración.**

La acotación y Proposición 13.4.2 — Caracterización de la acotación mediante el valor absoluto proporcionan el número $M$ del enunciado. Por Proposición 4.2.2 — Propiedades elementales del valor absoluto (6),

$$
-M\le a_n\le M
\qquad(n\in\mathbb N).
$$

Así $I_0=[-M,M]$ es recurrente: para cada umbral $N$, el índice determinado $n=N$ pertenece a él. El par $\langle-M,M\rangle$ pertenece al producto cartesiano $\mathbb R\times\mathbb R$.

Construyamos explícitamente el conjunto de estados permitidos:

$$
X:=\left\{
\langle p,q\rangle\in\mathbb R\times\mathbb R:
-M\le p\le q\le M
\text{ y }[p,q]\text{ es recurrente para }a
\right\}.
$$

Existe por Separación dentro de $\mathbb R\times\mathbb R$ y contiene $\langle-M,M\rangle$. Fijemos un estado $\langle p,q\rangle\in X$ y su punto medio $m=(p+q)h$. El lema Lema 13.11.2 — Una mitad de un intervalo recurrente sigue siendo recurrente garantiza que ambas mitades quedan dentro de $[-M,M]$ y que la regla «izquierda si recurrente; derecha si no» produce exactamente un par de $X$. Designémoslo por $F(\langle p,q\rangle)$.

El grafo de $F$ se obtiene por Separación dentro de $X\times X$, imponiendo la igualdad con $\langle p,m\rangle$ cuando la mitad izquierda es recurrente, y con $\langle m,q\rangle$ en caso contrario. La exclusión mutua de ambos casos y la unicidad del punto medio prueban que

$$
F:X\longrightarrow X
$$

es una función total, no una correspondencia multivaluada. El teorema de recursión Teorema 1.3.7 — Teorema de recursión sobre $\mathbb N$, con estado inicial $s(0)=\langle-M,M\rangle$, determina una única función $s:\mathbb N\to X$ tal que

$$
\boxed{s(S(k))=F(s(k)).}
$$

Por la definición de par ordenado, cada $s(k)$ tiene componentes únicas $l_k,u_k\in\mathbb R$. Los grafos de las dos proyecciones se obtienen por Separación dentro de $\mathbb N\times\mathbb R$, de modo que $l$ y $u$ son sucesiones reales definidas unívocamente como objetos conjuntistas, sin seleccionar pares de manera arbitraria.

La pertenencia $s(k)\in X$ asegura que $l_k\le u_k$ y que $I_k$ es recurrente. La propia regla de $F$ asegura $I_{S(k)}\subseteq I_k$ y, por la última identidad de Lema 13.11.2 — Una mitad de un intervalo recurrente sigue siendo recurrente,

$$
u_{S(k)}-l_{S(k)}=h(u_k-l_k).
$$

Esto es $w_{k+1}=hw_k$ si escribimos $k+1=S(k)$, y $w_k\ge0$ resulta de $l_k\le u_k$. Las condiciones iniciales proceden de $s(0)$; la función $s$ es única por recursión y determina también unívocamente ambas sucesiones de extremos. ∎

> **Estructura de la construcción.** La prueba no postula una sucesión de intervalos preexistente. Construye el conjunto de estados, demuestra que la transición es una función total y **sólo entonces** aplica recursión. En cada etapa se conserva el predicado de recurrencia, no se escoge «una mitad cualquiera».

---

### Lema 13.11.4 — Las anchuras de la bisección tienden a cero

Para las anchuras $w_k=u_k-l_k$ de Proposición 13.11.3 — Bisección recursiva canónica se cumple

$$
\boxed{w_k\longrightarrow0.}
$$

**Demostración.**

La diferencia puntual de las sucesiones $u$ y $l$ existe por Definición 13.1.3 — Operaciones puntuales sobre sucesiones reales, por lo que $w=(w_k)$ es una sucesión real. De Proposición 13.11.3 — Bisección recursiva canónica sabemos que

$$
0\le w_k,
\qquad
w_{S(k)}=hw_k.
$$

Como $0<1<1+1$, la regla de inversos de Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado (7) da

$$
\boxed{0<h<1.}
$$

Por tanto $0<1-h$. El producto de los números no negativos $1-h$ y $w_k$ es no negativo, de donde

$$
w_k-hw_k=(1-h)w_k\ge0.
$$

Así $w_{S(k)}=hw_k\le w_k$. Por transitividad e inducción, $w$ es decreciente en el sentido de Definición 13.7.1 — Sucesiones monótonas. Está acotada inferiormente por $0$, y el teorema de convergencia monótona Teorema 13.7.3 — Teorema de convergencia monótona proporciona un real $d$ con

$$
w_k\longrightarrow d.
$$

La cola reindexada $w^{\langle1\rangle}$ es una subsucesión de $w$ por Proposición 13.9.4 — Las colas son subsucesiones y las subsucesiones se componen; sus términos son $w_{1+k}=w_{S(k)}$. El teorema Teorema 13.9.5 — Toda subsucesión de una sucesión convergente converge al mismo límite implica entonces

$$
w_{S(k)}\longrightarrow d.
$$

Por la compatibilidad de los límites con un factor constante Corolario 13.5.4 — Compatibilidad con la multiplicación por una constante, también

$$
hw_k\longrightarrow hd.
$$

Como $w_{S(k)}=hw_k$ para todo $k$, la unicidad del límite Teorema 13.3.5 — Unicidad del límite real obliga a que $d=hd$. Restando $hd$ obtenemos

$$
(1-h)d=0.
$$

El factor $1-h$ es positivo y, en particular, no nulo. Multiplicando por su inverso, concluimos $d=0$. ∎

> **Por qué no utilizamos potencias prematuras.** La identidad $w_{k+1}=hw_k$ sugiere escribir $w_k=h^kw_0$, pero el tratado ha introducido hasta aquí el cuadrado, no las potencias naturales generales. No necesitamos anticiparlas: la convergencia monótona y la ecuación satisfecha por el límite prueban que las anchuras se anulan asintóticamente.

---

### Teorema 13.11.5 — Bolzano–Weierstrass para sucesiones reales

**Toda sucesión real acotada admite una subsucesión convergente.** Precisamente, si $a=(a_n)$ es acotada, existen un selector estrictamente creciente $\phi:\mathbb N\to\mathbb N$ y un real $x$ tales que

$$
\boxed{a_{\phi(k)}\longrightarrow x.}
$$

Si $|a_n|\le M$ para todo $n$, el límite puede obtenerse dentro de $[-M,M]$.

**Demostración.**

**Primera etapa: intervalos encajados.** Sea $M$ una cota absoluta dada por Proposición 13.4.2 — Caracterización de la acotación mediante el valor absoluto. La proposición Proposición 13.11.3 — Bisección recursiva canónica construye dos sucesiones de extremos $l_k,u_k$ cuyos intervalos

$$
I_k=[l_k,u_k]
$$

son recurrentes, satisfacen $I_0=[-M,M]$ y $I_{S(k)}\subseteq I_k$. Por inducción, si $i\le j$ entonces $I_j\subseteq I_i$.

Para aplicar el principio de intersección de intervalos de Definición 4.7.3 — Principio de intersección de intervalos cerrados, debemos verificar su hipótesis **cruzada**. Sean $i,j\in\mathbb N$. Por totalidad natural, $i\le j$ o $j\le i$. En el primer caso,

$$
l_i\le l_j\le u_j;
$$

en el segundo,

$$
l_i\le u_i\le u_j.
$$

Luego $l_i\le u_j$ para todos $i,j$. Como el conjunto de índices $\mathbb N$ está habitado por $0$ y $\mathbb R$ es completo, Teorema 4.7.4 — Equivalencia con el principio de intersección de intervalos proporciona un real $x$ tal que

$$
\boxed{l_k\le x\le u_k\qquad(k\in\mathbb N).}
$$

En particular $x\in I_0=[-M,M]$.

La intersección contiene, además, **un único** real. En efecto, si $x,y$ pertenecen a todos los $I_k$, entonces para cada $k$,

$$
-w_k\le x-y\le w_k,
\qquad
|x-y|\le w_k
$$

por Proposición 4.2.2 — Propiedades elementales del valor absoluto (6). Si $x\ne y$, la positividad de $|x-y|$ proporciona $\delta:=|x-y|>0$. Pero Lema 13.11.4 — Las anchuras de la bisección tienden a cero da algún $k$ con $0\le w_k<\delta$, contradiciendo $\delta\le w_k$. Así la intersección es exactamente $\{x\}$. La unicidad no afirma que podamos calcular $x$.

**Segunda etapa: una extracción genuina, sin Choice.** Que cada $I_k$ sea recurrente asegura que contiene términos arbitrariamente tardíos. Necesitamos convertir esa afirmación en **una sola función creciente** de índices, no en una colección sin relación de testigos existenciales.

Para $k,t\in\mathbb N$ definamos

$$
B_{k,t}:=
\{n\in\mathbb N:S(t)\le n\ \text{y}\ l_{S(k)}\le a_n\le u_{S(k)}\}.
$$

Existe por Separación. La recurrencia de $I_{S(k)}$ aplicada al umbral $S(t)$ muestra que $B_{k,t}$ está habitado. El principio de buen orden Teorema 1.6.13 — Principio de buen orden da su mínimo único $H(k,t)$. El grafo de la asignación $(k,t)\mapsto H(k,t)$ se obtiene por Separación dentro de $(\mathbb N\times\mathbb N)\times\mathbb N$, imponiendo pertenencia y minimalidad; por ello $H$ es una función, sin elecciones arbitrarias.

Aplicamos ahora Teorema 1.3.7 — Teorema de recursión sobre $\mathbb N$ al espacio de estados $\mathbb N\times\mathbb N$, con inicio $\langle0,0\rangle$ y transición

$$
G(\langle k,t\rangle):=\langle S(k),H(k,t)\rangle.
$$

La recursión determina unívocamente una función $\phi:\mathbb N\to\mathbb N$ mediante su segunda coordenada:

$$
\boxed{
\phi(0)=0,
\qquad
\phi(S(k))=H(k,\phi(k)).
}
$$

Los grafos de la sucesión de estados y de $\phi$ existen por la construcción recursiva y por Separación. La condición definitoria de $H$ implica

$$
S(\phi(k))\le\phi(S(k)),
$$

de modo que $\phi(k)<\phi(S(k))$. Una inducción, utilizando la transitividad del orden natural, extiende esta desigualdad adyacente a

$$
i<j\Longrightarrow\phi(i)<\phi(j).
$$

Por Definición 13.9.1 — Selector de índices de subsucesión, $\phi$ es un selector de subsucesión. Además,

$$
\boxed{a_{\phi(k)}\in I_k\qquad(k\in\mathbb N).}
$$

Para $k=0$ esto se sigue de $\phi(0)=0$ y de que $I_0$ contiene todos los términos de $a$; en el paso sucesor se sigue directamente de $\phi(S(k))\in B_{k,\phi(k)}$.

**Tercera etapa: convergencia.** Como tanto $x$ como $a_{\phi(k)}$ pertenecen al intervalo $[l_k,u_k]$,

$$
\boxed{|a_{\phi(k)}-x|\le u_k-l_k=w_k.}
$$

Sea $\varepsilon>0$. Por Lema 13.11.4 — Las anchuras de la bisección tienden a cero, existe $K$ tal que, para $k\ge K$,

$$
0\le w_k<\varepsilon.
$$

En consecuencia,

$$
k\ge K
\Longrightarrow
|a_{\phi(k)}-x|\le w_k<\varepsilon.
$$

Por Definición 13.3.1 — Convergencia de una sucesión real, $a_{\phi(k)}\to x$. La función $a\circ\phi$ es una subsucesión por Definición 13.9.3 — Subsucesión de una sucesión real y converge en $\mathbb R$, como se quería. ∎

> **Reconstrucción de la prueba.** Acotación $\Rightarrow$ intervalo inicial recurrente $\Rightarrow$ bisecciones recurrentes y encajadas $\Rightarrow$ anchuras que tienden a cero $\Rightarrow$ un único punto real en la intersección (completitud) $\Rightarrow$ índices mínimos estrictamente crecientes $\Rightarrow$ convergencia de la extracción. La recurrencia garantiza que nunca nos quedamos sin índices; la disminución de anchuras garantiza que los valores seleccionados se aproximan al mismo real.

> **Dónde se utiliza cada hipótesis.** La acotación proporciona $I_0$; sin ella no disponemos en general de un intervalo cerrado y acotado inicial que contenga todos los términos. La completitud se utiliza para asegurar la intersección no vacía y, mediante el teorema de convergencia monótona, para probar $w_k\to0$. El crecimiento de los índices procede del buen orden de $\mathbb N$ y de la restricción $n\ge S(t)$, no de la completitud.

> **Auditoría fundacional.** La bisección utiliza lógica clásica para decidir formalmente el predicado de recurrencia y el buen orden general en las minimizaciones. No se supone decidibilidad de la comparación de reales ni se obtiene un algoritmo efectivo. No interviene Choice: la mitad se fija por una regla de casos, cada índice es el **mínimo único** de un conjunto no vacío, ambas funciones se construyen por Separación y recursión, y el punto de intersección es único. La existencia formal de $x$ y de $\phi$ no equivale a poder computarlos a partir de una presentación extensional arbitraria de $a$.

---

### Corolario 13.11.6 — Existencia de puntos límite secuenciales para sucesiones acotadas

Si $a$ es una sucesión real acotada, entonces

$$
\boxed{\operatorname{LimSub}(a)\ne\varnothing.}
$$

**Demostración.**

Por Teorema 13.11.5 — Bolzano–Weierstrass para sucesiones reales existen un selector $\phi$ y un real $x$ con $a_{\phi(k)}\to x$. La definición Definición 13.10.1 — Punto límite secuencial dice exactamente que $x$ es un punto límite secuencial; por Definición 13.10.4 — Conjunto de puntos límite secuenciales, $x\in\operatorname{LimSub}(a)$. ∎

> **Prueba de estrés.** La conclusión no afirma que la sucesión completa converja: la sucesión alternante de §13.10 es acotada y tiene al menos dos puntos límite. Tampoco admite la conversa «tener un punto límite implica estar acotada»: si $c$ es la alternante de §13.10 y definimos $d_n:=\nu_{\mathbb R}(n)c_n$, entonces $d_{k+k}=0$ y $d_{S(k+k)}=\nu_{\mathbb R}(S(k+k))$. La primera extracción es constante nula, mientras que la segunda no está acotada por arquimedianidad. Así $d$ tiene un punto límite sin estar acotada. Bolzano--Weierstrass asegura **una extracción convergente a partir de acotación global**, nada más.

---

Hemos obtenido la afirmación que permanecía abierta desde §13.10:

$$
\boxed{
\text{acotación de }a
\Longrightarrow
\operatorname{LimSub}(a)\ne\varnothing.
}
$$

La infraestructura de §13.8 permite ahora afinar esta existencia: sus envolventes $L_N(a)$ y $U_N(a)$ convergen por monotonía y completitud. La sección siguiente estudiará los **límites inferior y superior**, establecerá su relación exacta con $\operatorname{LimSub}(a)$ y fijará la notación $\liminf$ y $\limsup$ sólo después de justificar la existencia de los números que denotan.

---
