## 13.10. Puntos límite secuenciales {#sec-ta-13-10}

La convergencia ordinaria exige que **todos** los términos suficientemente tardíos queden cerca de un mismo real. Una subsucesión permite una exigencia diferente: quizá la sucesión completa no converja, pero podamos conservar una cadena indefinidamente creciente de índices cuyos valores sí converjan. Los límites así obtenidos se estudiarán sin introducir todavía vecindades topológicas ni puntos de acumulación de conjuntos.

Debemos distinguir dos afirmaciones:

$$
\underbrace{a_n\to x}_{\text{converge la sucesión entera}}
\qquad\text{y}\qquad
\underbrace{a_{\phi(k)}\to x}_{\text{converge una extracción}}.
$$

La primera implica la segunda para cualquier selector, por Teorema 13.9.5 — Toda subsucesión de una sucesión convergente converge al mismo límite; la recíproca no está autorizada. Precisaremos ahora qué reales pueden alcanzarse por una extracción y cómo reconocerlos sin adivinar previamente el selector.

### Definición 13.10.1 — Punto límite secuencial

Sea $a=(a_n)_{n\in\mathbb N}$ una sucesión real. Un real $x$ es un **punto límite secuencial** de $a$ si existe un selector estrictamente creciente $\phi:\mathbb N\to\mathbb N$ tal que

$$
\boxed{a_{\phi(k)}\longrightarrow x.}
$$

Equivalentemente, $x$ es el límite de alguna subsucesión de $a$. El cuantificador existencial se refiere a un selector que testimonia una extracción concreta; no presupone una elección simultánea de selectores para distintos reales.

> **Lectura de la definición.** El real $x$ no necesita aparecer como término de $a$: puede ser sólo el destino de valores extraídos. Recíprocamente, que $x=a_j$ para algún índice aislado no lo convierte en punto límite; la extracción debe contener términos con índices estrictamente crecientes y, por tanto, arbitrariamente tardíos.

Para caracterizar la definición necesitamos una escala positiva que tienda a cero. No identificaremos el natural $n$ con su numeral real: utilizaremos la aplicación $\nu_{\mathbb R}:\mathbb N\to\mathbb R$ de Definición 4.1.5 — Aplicación de numerales naturales en un cuerpo ordenado.

### Lema 13.10.2 — Los recíprocos de los numerales positivos tienden a cero

Para cada $k\in\mathbb N$, sea

$$
\boxed{r_k:=\nu_{\mathbb R}(S(k))^{-1}.}
$$

Entonces $r=(r_k)$ es una sucesión real, $r_k>0$ para todo $k$, y

$$
\boxed{r_k\longrightarrow0.}
$$

**Demostración.**

Como $0<S(k)$ en el orden natural, Proposición 4.1.6 — Aritmética y orden de los numerales naturales implica

$$
0=\nu_{\mathbb R}(0)<\nu_{\mathbb R}(S(k)).
$$

Cada numeral posee, pues, recíproco positivo por Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado (6). Los valores están determinados unívocamente por operaciones de $\mathbb R$; su grafo se obtiene por Separación dentro de $\mathbb N\times\mathbb R$. Esto define la sucesión $r$ sin elección.

Sea $\varepsilon>0$. Como $\mathbb R$ es completo, Teorema 4.6.3 — Todo cuerpo ordenado completo es arquimediano garantiza que es arquimediano. La caracterización Proposición 4.4.2 — Caracterización por recíprocos pequeños proporciona un natural $N\ne0$ tal que

$$
0<\nu_{\mathbb R}(N)^{-1}<\varepsilon.
$$

Si $k\ge N$, entonces $N\le k<S(k)$; por Proposición 4.1.6 — Aritmética y orden de los numerales naturales,

$$
0<\nu_{\mathbb R}(N)<\nu_{\mathbb R}(S(k)).
$$

Al invertir el orden entre positivos mediante Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado (7),

$$
0<r_k
=\nu_{\mathbb R}(S(k))^{-1}
<\nu_{\mathbb R}(N)^{-1}
<\varepsilon.
$$

Por la definición de convergencia, $r_k\to0$. ∎

> **Control fundacional.** La escala se define mediante numerales reales, no por una identificación conjuntista $\mathbb N\subseteq\mathbb R$. La prueba no usa Choice; sí hereda la lógica clásica con la que Teorema 4.6.3 — Todo cuerpo ordenado completo es arquimediano dedujo la arquimedianidad de la completitud. No se afirma que los umbrales obtenidos sean calculables para una presentación arbitraria de los reales.

### Proposición 13.10.3 — Criterio de visitas arbitrariamente tardías

Sea $a=(a_n)$ una sucesión real y sea $x\in\mathbb R$. Son equivalentes:

1. $x$ es un punto límite secuencial de $a$.
2. Para todo $\varepsilon>0$ y todo $N\in\mathbb N$ existe $n\in\mathbb N$ tal que
   $$
   \boxed{N\le n\quad\text{y}\quad |a_n-x|<\varepsilon.}
   $$

La segunda condición significa que **cada intervalo de precisión alrededor de $x$ recibe términos de la sucesión después de cualquier umbral natural**.

**Demostración.**

**$1\Rightarrow2$.** Sea $\phi$ un selector tal que $a_{\phi(k)}\to x$. Fijemos $\varepsilon>0$ y $N\in\mathbb N$. Por convergencia existe $K$ tal que

$$
k\ge K\Longrightarrow |a_{\phi(k)}-x|<\varepsilon.
$$

Por totalidad del orden natural, uno de $K,N$ es mayor o igual que el otro. Tomemos $k$ igual al mayor; así $k\ge K,N$. Según Proposición 13.9.2 — Crecimiento, inyectividad y cofinalidad de los selectores de índices,

$$
\phi(k)\ge k\ge N.
$$

El índice $n:=\phi(k)$ satisface las dos condiciones requeridas.

**$2\Rightarrow1$.** Aquí no basta repetir el cuantificador existencial para cada precisión: necesitamos construir **una sola función** de índices estrictamente creciente.

Utilicemos la sucesión $r_k>0$ del lema anterior. Fijados $k,t\in\mathbb N$, consideremos el conjunto

$$
A_{k,t}:=
\{n\in\mathbb N:S(t)\le n\ \text{y}\ |a_n-x|<r_{S(k)}\}.
$$

Existe por Separación dentro de $\mathbb N$. Aplicando la hipótesis $2$ a la precisión positiva $r_{S(k)}$ y al umbral $S(t)$, obtenemos un elemento de $A_{k,t}$: el conjunto es no vacío. Por el buen orden Teorema 1.6.13 — Principio de buen orden posee un **único** elemento mínimo, que denotamos $H(k,t)$. La regla $H:\mathbb N\times\mathbb N\to\mathbb N$ determina una función genuina: su grafo se obtiene por Separación dentro de $(\mathbb N\times\mathbb N)\times\mathbb N$, exigiendo pertenencia a $A_{k,t}$ y minimalidad. No elegimos mínimos arbitrariamente; están unívocamente determinados.

De manera semejante, el conjunto

$$
A_0:=\{n\in\mathbb N:|a_n-x|<r_0\}
$$

es no vacío al aplicar $2$ con umbral $0$, y posee un mínimo único $p_0$.

Aplicaremos el teorema de recursión Teorema 1.3.7 — Teorema de recursión sobre $\mathbb N$ al conjunto $X=\mathbb N\times\mathbb N$, con estado inicial y transición

$$
s_0:=\langle0,p_0\rangle,
\qquad
G(\langle k,t\rangle):=\langle S(k),H(k,t)\rangle.
$$

La función $G:X\to X$ está bien definida por la funcionalidad de $H$. La recursión produce una única sucesión de estados $s:\mathbb N\to X$ con $s(0)=s_0$ y $s(S(k))=G(s(k))$. Por inducción, cada estado tiene la forma

$$
s(k)=\langle k,\phi(k)\rangle
$$

para una función $\phi:\mathbb N\to\mathbb N$ determinada por la segunda coordenada; su grafo también se obtiene por Separación. Las ecuaciones recursivas son

$$
\phi(0)=p_0,
\qquad
\phi(S(k))=H(k,\phi(k)).
$$

Por definición de $H$,

$$
S(\phi(k))\le\phi(S(k)),
$$

por lo que $\phi(k)<\phi(S(k))$. Por inducción en $n$ verificamos ahora que todo $m<n$ satisface $\phi(m)<\phi(n)$: en el paso sucesor, $m<S(n)$ implica $m<n$ o $m=n$; en el primer caso aplicamos la hipótesis inductiva seguida de $\phi(n)<\phi(S(n))$, y en el segundo usamos directamente esta última desigualdad. Por tanto $\phi$ es un selector.

Además, el caso inicial y las condiciones que definen los conjuntos $A_{k,t}$ dan, por inducción,

$$
\boxed{|a_{\phi(k)}-x|<r_k\quad(k\in\mathbb N).}
$$

En efecto, vale para $k=0$ por $p_0\in A_0$; si pasamos al sucesor, $H(k,\phi(k))\in A_{k,\phi(k)}$ impone la cota $r_{S(k)}$ para el nuevo índice.

Finalmente, dado $\varepsilon>0$, Lema 13.10.2 — Los recíprocos de los numerales positivos tienden a cero proporciona $K$ tal que $k\ge K$ implica $0<r_k<\varepsilon$. Por la estimación anterior,

$$
k\ge K
\Longrightarrow
|a_{\phi(k)}-x|<r_k<\varepsilon.
$$

Así $a_{\phi(k)}\to x$, y $x$ es un punto límite secuencial. ∎

> **Arquitectura de la extracción.** Visitas tardías para cada par $(\varepsilon,N)$ $\to$ conjuntos no vacíos de índices admisibles $\to$ mínimo único de cada conjunto $\to$ recursión de un selector estrictamente creciente $\to$ convergencia por $r_k\to0$.
>

### Definición 13.10.4 — Conjunto de puntos límite secuenciales

Para toda sucesión real $a$, definimos

$$
\boxed{
\operatorname{LimSub}(a)
:=\{x\in\mathbb R:x\text{ es punto límite secuencial de }a\}.
}
$$

El conjunto existe por Separación dentro de $\mathbb R$: la propiedad cuantifica sobre funciones y límites previamente definidos. No presupone que exista algún punto límite, por lo que $\operatorname{LimSub}(a)$ puede ser vacío. Esta notación designa un **conjunto de reales**, no una sucesión y tampoco el límite de $a$.

La condición equivalente de Proposición 13.10.3 — Criterio de visitas arbitrariamente tardías permite leer

$$
x\in\operatorname{LimSub}(a)
\iff
\forall\varepsilon>0\;\forall N\in\mathbb N\;
\exists n\ge N:\ |a_n-x|<\varepsilon.
$$

> **Distinción editorial.** $\operatorname{LimSub}(a)$ no redefine las envolventes $L_N(a),U_N(a)$ de §13.8 ni introduce todavía $\liminf$ o $\limsup$, que serán números determinados por otras definiciones cuando corresponda.

### Proposición 13.10.5 — Puntos límite de una sucesión convergente

Si $a_n\to\ell$, entonces

$$
\boxed{\operatorname{LimSub}(a)=\{\ell\}.}
$$

**Demostración.**

La sucesión $a$ es subsucesión de sí misma, como se probó en Corolario 13.9.7 — Caracterización de la convergencia mediante subsucesiones mediante el selector identidad. Su convergencia a $\ell$ muestra que $\ell\in\operatorname{LimSub}(a)$.

Recíprocamente, sea $x\in\operatorname{LimSub}(a)$. Existe una subsucesión $b$ con $b_k\to x$. Por Teorema 13.9.5 — Toda subsucesión de una sucesión convergente converge al mismo límite, la convergencia original también implica $b_k\to\ell$. La unicidad Teorema 13.3.5 — Unicidad del límite real da $x=\ell$. Ambas inclusiones y el criterio extensional Teorema 0.2.4 — Criterio extensional por doble inclusión prueban la igualdad. ∎

El resultado es unidireccional. La afirmación de que **tener un solo punto límite basta para converger** no se ha demostrado y no se utilizará como recíproca.

### Proposición 13.10.6 — Invariancia frente a cambios iniciales finitos

Si las sucesiones reales $a$ y $b$ coinciden eventualmente, entonces

$$
\boxed{\operatorname{LimSub}(a)=\operatorname{LimSub}(b).}
$$

**Demostración.**

Existe $T\in\mathbb N$ tal que $a_n=b_n$ para $n\ge T$. Sea $x\in\operatorname{LimSub}(a)$, y fijemos $\varepsilon>0$, $N\in\mathbb N$. Por la tricotomía natural, tomemos como umbral $M$ el mayor de $N$ y $T$. El criterio Proposición 13.10.3 — Criterio de visitas arbitrariamente tardías proporciona $n\ge M$ con

$$
|a_n-x|<\varepsilon.
$$

Como $n\ge T$, $a_n=b_n$; y como $n\ge N$, ese mismo índice muestra que $b$ satisface la condición de visitas tardías. Aplicando nuevamente el criterio, $x\in\operatorname{LimSub}(b)$. Intercambiando $a$ y $b$ obtenemos la inclusión opuesta. La extensionalidad concluye la igualdad. ∎

No se confunde aquí un término inicial excepcional con un comportamiento que puede seguir observándose arbitrariamente tarde.

> **Ejemplos para contrastar.** Si $a_0=100$ y $a_n=0$ para $n\ge1$, entonces $a$ coincide eventualmente con la sucesión constante nula; por la proposición y Proposición 13.10.5 — Puntos límite de una sucesión convergente, su único punto límite secuencial es $0$, no $100$. Por otra parte, definamos recursivamente $c_0=0$ y $c_{S(n)}=1-c_n$. Por inducción, $c_{k+k}=0$ y $c_{S(k+k)}=1$; los selectores $k\mapsto k+k$ y $k\mapsto S(k+k)$ dan subsucesiones constantes de límites distintos. La sucesión $c$ no converge, pues la unicidad del límite y Teorema 13.9.5 — Toda subsucesión de una sucesión convergente converge al mismo límite impedirían esos dos límites. Así, una sucesión puede admitir varios puntos límite aunque carezca de límite ordinario.

### Proposición 13.10.7 — Los puntos límite de una sucesión acotada están acotados

Si $a$ es una sucesión real acotada, existe $M\in\mathbb R$, $M\ge0$, tal que

$$
\boxed{\operatorname{LimSub}(a)\subseteq[-M,M].}
$$

**Demostración.**

Por Proposición 13.4.2 — Caracterización de la acotación mediante el valor absoluto, la acotación de $a$ proporciona $M\ge0$ con $|a_n|\le M$ para todo $n$. Sea $x\in\operatorname{LimSub}(a)$ y tomemos una subsucesión $b$ convergente a $x$. Por Proposición 13.9.6 — Acotación y condición de Cauchy pasan a las subsucesiones, y directamente por la fórmula $b_k=a_{\phi(k)}$,

$$
-M\le b_k\le M
\qquad(k\in\mathbb N).
$$

Las sucesiones constantes de valores $-M$ y $M$ convergen a esos valores por Proposición 13.3.4 — Las sucesiones constantes convergen a su valor. Aplicando dos veces el teorema de orden de los límites Teorema 13.6.2 — Preservación del orden en el paso al límite obtenemos

$$
-M\le x\le M.
$$

Por la definición de intervalo cerrado, $x\in[-M,M]$. Como $x$ era arbitrario, se sigue la inclusión. ∎

> **Precisión importante.** Hemos demostrado que, *si hay puntos límite*, no pueden escapar de las cotas de la sucesión. Todavía **no** hemos demostrado que una sucesión acotada posea alguno. La existencia es justamente el contenido del siguiente teorema.
>
> La posibilidad de vacío es real: para $a_n=\nu_{\mathbb R}(n)$, todo selector satisface $\phi(k)\ge k$. Por arquimedianidad, dado $x\in\mathbb R$ existe $K$ con $\nu_{\mathbb R}(K)>x+1$; para $k\ge K$, la preservación del orden de los numerales da $a_{\phi(k)}>x+1$. Ninguna subsucesión converge a $x$: la condición de convergencia falla para $\varepsilon=1$. Por tanto $\operatorname{LimSub}(a)=\varnothing$. La acotación en Bolzano--Weierstrass no es ornamental.

La lectura conjunta de esta sección identifica el problema que queda pendiente:

$$
\boxed{
\text{sucesión acotada}
\quad\overset{?}{\Longrightarrow}\quad
\operatorname{LimSub}(a)\ne\varnothing.
}
$$

La respuesta exigirá construir una extracción convergente usando la completitud de la recta; será el **teorema de Bolzano--Weierstrass** de §13.11. Hasta entonces no debemos invocarlo, ni utilizar formulaciones generales de compacidad o topología aún no desarrolladas.
