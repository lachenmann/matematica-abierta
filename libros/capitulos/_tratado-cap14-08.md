## 14.8. Convergencia absoluta y condicional {#sec-ta-14-8}

Hasta ahora, la comparación y la condensación han trabajado fundamentalmente con términos no negativos. Una serie con signos variables plantea un problema adicional: la cancelación puede hacer pequeñas las sumas de bloques aun cuando las sumas de las magnitudes de esos mismos términos sean grandes. Debemos distinguir, por consiguiente, entre controlar la **suma con sus signos** y controlar la **suma de los valores absolutos**. La desigualdad triangular conecta ambos controles, pero sólo en una dirección.

### Definición 14.8.1 — Serie de valores absolutos; convergencia absoluta y condicional

Para una sucesión real $a=(a_n)_{n\in\mathbb N}$, definimos su **sucesión de magnitudes** por

$$
\boxed{\operatorname{Abs}(a)_n:=|a_n|\qquad(n\in\mathbb N).}
$$

Es una sucesión real total: su grafo se obtiene por Separación dentro de $\mathbb N\times\mathbb R$ imponiendo el valor único $|a_n|$ en cada índice. Así queda determinada también una función $\operatorname{Abs}:\mathbb R^{\mathbb N}\to\mathbb R^{\mathbb N}$; no hay elección de valores. Todos sus términos son no negativos. La **serie de valores absolutos** de $a$ es la serie cuyos términos son $\operatorname{Abs}(a)$:

$$
\sum_{n=0}^{\infty}|a_n|.
$$

Decimos que la serie de $a$ **converge absolutamente** si converge esta serie de magnitudes. Decimos que **converge condicionalmente** si converge la serie original y diverge la serie de magnitudes. En términos de conjuntos de sucesiones de términos, establecemos

$$
\boxed{
\begin{aligned}
\mathcal A_{\mathrm{ser}}
  &:=\{a\in\mathbb R^{\mathbb N}:\operatorname{Abs}(a)\in\mathcal C_{\mathrm{ser}}\},\\
\mathcal K_{\mathrm{ser}}
  &:=\{a\in\mathcal C_{\mathrm{ser}}:\operatorname{Abs}(a)\notin\mathcal C_{\mathrm{ser}}\}.
\end{aligned}}
$$

Ambos conjuntos existen por Separación en los conjuntos indicados. Por definición, $\mathcal K_{\mathrm{ser}}$ está contenido en $\mathcal C_{\mathrm{ser}}$; que también $\mathcal A_{\mathrm{ser}}$ esté contenido en $\mathcal C_{\mathrm{ser}}$ será un **teorema**, no una parte de la definición. La expresión «converge condicionalmente» no se aplica a una serie divergente, y no designa un valor numérico distinto de su suma ordinaria.

> **Tres preguntas distintas.** ¿Converge $\sum a_n$? ¿Converge $\sum|a_n|$? Si convergen ambas, ¿se relacionan sus sumas mediante una desigualdad? La primera y la segunda se deciden aplicando a dos sucesiones diferentes la definición de §14.1; la tercera requiere un argumento adicional.

### Lema 14.8.2 — Desigualdad triangular para sumas finitas y bloques

Sea $a$ una sucesión real, y pongamos $s=\operatorname{PS}(a)$ y $u=\operatorname{PS}(\operatorname{Abs}(a))$. Entonces se cumplen las desigualdades siguientes:

$$
\boxed{|s_n|\le u_n\qquad(n\in\mathbb N),}
$$

$$
\boxed{|s_m-s_n|\le u_m-u_n
\qquad(n,m\in\mathbb N,\ n<m).}
$$

El segundo miembro de la desigualdad de bloques es no negativo, pues los términos de $\operatorname{Abs}(a)$ son no negativos y $u$ es creciente.

**Demostración.**

La primera estimación se prueba por inducción. Para $n=0$,

$$
|s_0|=|a_0|=u_0.
$$

Si $|s_n|\le u_n$, la recursión de las sumas parciales y la desigualdad triangular Teorema 4.2.3 — Desigualdad triangular dan

$$
\begin{aligned}
|s_{n+1}|&=|s_n+a_{n+1}|\\
&\le|s_n|+|a_{n+1}|\\
&\le u_n+|a_{n+1}|=u_{n+1}.
\end{aligned}
$$

La inducción proporciona la estimación para todo $n$.

Para los bloques, fijemos $n$ y procedamos por inducción sobre su longitud positiva. El caso de un término, $m=n+1$, se sigue de Proposición 14.2.2 — Identidades de los bloques de sumación:

$$
|s_{n+1}-s_n|=|a_{n+1}|=u_{n+1}-u_n.
$$

Supongamos ahora que, para cierto $m>n$, vale $|s_m-s_n|\le u_m-u_n$. La recursión y la desigualdad triangular producen

$$
\begin{aligned}
|s_{m+1}-s_n|
&=|(s_m-s_n)+a_{m+1}|\\
&\le|s_m-s_n|+|a_{m+1}|\\
&\le(u_m-u_n)+|a_{m+1}|\\
&=u_{m+1}-u_n.
\end{aligned}
$$

La inducción cubre todos los extremos $m=n+d$ con $d\ge1$, pues todo natural no nulo es un sucesor y el orden natural proporciona esa representación. Finalmente, $u$ es creciente por Proposición 14.4.1 — Monotonía de las sumas parciales de una serie no negativa, lo que justifica $u_m-u_n\ge0$. ∎

> **Lectura de la desigualdad.** En un bloque, las cancelaciones pueden disminuir $|s_m-s_n|$; nunca pueden hacerla mayor que la suma de los valores absolutos de sus términos. No hemos supuesto que ninguna de las dos series converja: las desigualdades son finitas.

### Teorema 14.8.3 — La convergencia absoluta implica convergencia ordinaria

Si la serie de valores absolutos de $a$ converge, entonces la serie de $a$ converge. Más precisamente, si ambas tienen sumas reales $A$ y $S$, respectivamente, se verifica

$$
\boxed{
\sum_{n=0}^{\infty}|a_n|\text{ converge}
\quad\Longrightarrow\quad
\sum_{n=0}^{\infty}a_n\text{ converge},
\qquad |S|\le A.
}
$$

En consecuencia, $\mathcal A_{\mathrm{ser}}\subseteq\mathcal C_{\mathrm{ser}}$.

**Demostración.**

Denotemos por $u$ las sumas parciales de $\operatorname{Abs}(a)$ y por $s$ las de $a$. Por hipótesis, $u$ converge. Dado $\varepsilon>0$, el criterio de Cauchy para series Teorema 14.2.3 — Criterio de Cauchy para una serie numérica, aplicado a $\operatorname{Abs}(a)$, proporciona un natural $N$ tal que

$$
N\le n<m\quad\Longrightarrow\quad|u_m-u_n|<\varepsilon.
$$

La sucesión $u$ es creciente porque sus incrementos son $|a_{n+1}|\ge0$. En consecuencia, $u_m-u_n=|u_m-u_n|$ cuando $n<m$. Por el lema precedente,

$$
\boxed{
|s_m-s_n|\le u_m-u_n<\varepsilon
\qquad(N\le n<m).
}
$$

Ésta es exactamente la condición del criterio Teorema 14.2.3 — Criterio de Cauchy para una serie numérica para la serie original. Por tanto $s$ converge a algún $S\in\mathbb R$. La hipótesis proporciona también $u_n\to A\in\mathbb R$.

Para obtener la desigualdad entre las sumas, el primer apartado del lema establece $|s_n|\le u_n$ para **cada** $n$. La continuidad secuencial del valor absoluto Proposición 13.5.5 — El valor absoluto preserva límites da $|s_n|\to|S|$, y la preservación del orden al pasar al límite Teorema 13.6.2 — Preservación del orden en el paso al límite permite concluir $|S|\le A$. Las notaciones de suma infinita se han usado como valores numéricos sólo después de haber demostrado ambas convergencias. Por la definición de $\mathcal A_{\mathrm{ser}}$ y $\mathcal C_{\mathrm{ser}}$, también resulta la inclusión anunciada. ∎

> **Alcance exacto.** La desigualdad $|S|\le A$ no afirma que $S=A$, ni que los términos deban ser no negativos. La prueba controla **todos** los bloques tardíos con un solo umbral; no basta observar que $|a_n|\to0$. La recíproca de la implicación se pondrá a prueba al final de la sección.

### Corolario 14.8.4 — Dominación absoluta eventual

Sean $a,b$ sucesiones reales y supongamos que $b_n\ge0$ para todo $n$.

1. Si existe $N\in\mathbb N$ tal que $|a_n|\le b_n$ para todo $n\ge N$, y la serie $\sum b_n$ converge, entonces $\sum a_n$ **converge absolutamente** y, en particular, converge.
2. Si existe $N\in\mathbb N$ tal que $b_n\le |a_n|$ para todo $n\ge N$, y la serie $\sum b_n$ diverge, entonces $\sum a_n$ **no** converge absolutamente. Esta segunda afirmación no determina por sí sola si la serie original converge o diverge.

**Demostración.**

Para la primera afirmación, fijemos su umbral $N$. La sucesión $c=\operatorname{Abs}(a)$ cumple $0\le c_n=|a_n|$ para cada índice y $c_n\le b_n$ para $n\ge N$. La comparación eventual Corolario 14.5.3 — Comparación válida a partir de cierto índice, aplicada a las series no negativas de $c$ y $b$, demuestra que la convergencia de la segunda implica la de la primera. Por definición, esto es convergencia absoluta de $a$, y Teorema 14.8.3 — La convergencia absoluta implica convergencia ordinaria da la convergencia ordinaria.

Para la segunda afirmación, tomemos su umbral, posiblemente distinto del anterior, supongamos $b_n\le c_n$ para todos los índices desde él y que la serie de $b$ diverge. La contraposición divergente de la misma comparación eventual establece que la serie de $c$ diverge. Así $a\notin\mathcal A_{\mathrm{ser}}$. No se ha establecido nada más sobre la convergencia de la serie con signos $a$: ésta será una distinción efectiva, no meramente lógica, en el ejemplo de §14.8.6. ∎

### Proposición 14.8.5 — Estabilidad de la convergencia absoluta bajo suma y producto por escalares

Si las series de $a$ y $b$ convergen absolutamente y $c\in\mathbb R$, entonces las series con términos $a_n+b_n$ y $ca_n$ también convergen absolutamente.

**Demostración.**

Sean $x=\operatorname{Abs}(a)$ e $y=\operatorname{Abs}(b)$. Por hipótesis, las series de $x$ e $y$ convergen. Definamos la sucesión no negativa $q_n:=x_n+y_n$ mediante operaciones puntuales ya disponibles. Si $X=\operatorname{PS}(x)$, $Y=\operatorname{PS}(y)$ y $Q=\operatorname{PS}(q)$, las ecuaciones recursivas dan $Q_0=x_0+y_0=X_0+Y_0$ y, suponiendo $Q_n=X_n+Y_n$,

$$
\begin{aligned}
Q_{n+1}&=Q_n+(x_{n+1}+y_{n+1})\\
&=(X_n+x_{n+1})+(Y_n+y_{n+1})\\
&=X_{n+1}+Y_{n+1}.
\end{aligned}
$$

Por inducción, $Q_n=X_n+Y_n$ para todo $n$. La suma de dos sucesiones reales convergentes converge por Proposición 13.5.1 — Límite de una suma, de modo que $\sum q_n$ converge. Para cada $n$, la desigualdad triangular implica

$$
0\le|a_n+b_n|\le|a_n|+|b_n|=q_n.
$$

El criterio de comparación directa Teorema 14.5.2 — Criterio de comparación directa prueba la convergencia de $\sum |a_n+b_n|$. Esto es la primera afirmación.

Para el escalar $c$, la multiplicatividad del valor absoluto (Proposición 4.2.2 — Propiedades elementales del valor absoluto) da

$$
|ca_n|=|c|\,|a_n|.
$$

Si $c\ne0$, entonces $|c|>0$, y Proposición 14.6.1 — Multiplicación de una serie por un escalar no nulo preserva la convergencia de la serie de $x$ al multiplicarla por $|c|$. Si $c=0$, todos los términos $|ca_n|$ son cero y las sumas parciales correspondientes son constantemente cero, caso cubierto por Proposición 14.1.6 — Estabilización de sumas parciales cuando los términos tardíos son nulos. Concluimos en ambos casos que la serie de $ca$ converge absolutamente. ∎

> **Interpretación algebraica.** Las sucesiones cuyos términos generan series absolutamente convergentes son estables bajo suma y multiplicación por escalares reales. No afirmamos todavía que la convergencia *condicional* tenga una estabilidad análoga ni introducimos aquí reordenamientos de series.

### Teorema 14.8.6 — Existe una serie condicionalmente convergente

Existe una sucesión real $a$ cuya serie converge a cero, pero cuya serie de valores absolutos diverge. Por tanto,

$$
\boxed{\mathcal K_{\mathrm{ser}}\ne\varnothing
\quad\text{y}\quad
\mathcal A_{\mathrm{ser}}\subsetneq\mathcal C_{\mathrm{ser}}.}
$$

**Demostración.**

Recuperemos la sucesión armónica ya construida en §14.2:

$$
h_k:=\nu_{\mathbb R}(k+1)^{-1}\quad(k\in\mathbb N).
$$

Los resultados Lema 13.10.2 — Los recíprocos de los numerales positivos tienden a cero y Proposición 14.2.7 — La condición $a_n\to0$ no es suficiente: la serie armónica aseguran, respectivamente, que $h_k>0$ y $h_k\to0$, pero que su serie diverge. Construyamos la sucesión $a$ **por parejas de términos**:

$$
\boxed{a_{2k}:=h_k,\qquad a_{2k+1}:=-h_k
\qquad(k\in\mathbb N).}
\tag{14.8.1}
$$

Aquí $2k$ y $2k+1$ son índices **naturales**; el $2$ es el natural de Notación 3.9.1 — El número dos en los tres sistemas, y $h_k$ pertenece a $\mathbb R$. La dicotomía de paridad Lema 3.9.3 — Dicotomía de paridad asegura que todo índice natural es par o impar y que esos casos son disjuntos. En cada caso el índice $k$ es único: si $2k=2j$ o $2k+1=2j+1$, cancelamos la suma final cuando procede y utilizamos que la multiplicación por el natural positivo $2$ es estrictamente creciente (Proposición 1.6.8 — Compatibilidad con el producto); si $k\ne j$, la totalidad del orden natural produciría una desigualdad estricta entre $2k$ y $2j$, contradiciendo su igualdad. Por tanto (14.8.1) asigna exactamente un real a cada índice. Su grafo existe por Separación en $\mathbb N\times\mathbb R$; no se eligen representantes ni se invoca Choice.

**Primero: convergencia de la serie original.** Escribamos $s=\operatorname{PS}(a)$. Una inducción sobre $k$ muestra que

$$
\boxed{s_{2k}=h_k,\qquad s_{2k+1}=0
\qquad(k\in\mathbb N).}
\tag{14.8.2}
$$

En efecto, para $k=0$ las sumas parciales son $s_0=a_0=h_0$ y $s_1=a_0+a_1=h_0-h_0=0$. Si $s_{2k+1}=0$, la recursión y las igualdades naturales $2(k+1)=2k+2$ y $2(k+1)+1=2k+3$ dan

$$
\begin{aligned}
s_{2(k+1)}&=s_{2k+1}+a_{2k+2}=0+h_{k+1}=h_{k+1},\\
s_{2(k+1)+1}&=s_{2(k+1)}+a_{2k+3}=h_{k+1}-h_{k+1}=0.
\end{aligned}
$$

Demostremos la convergencia de **toda** $s$, y no sólo de la subsucesión de índices impares. Dado $\varepsilon>0$, de $h_k\to0$ obtenemos un $K\in\mathbb N$ tal que $k\ge K$ implica $0<h_k<\varepsilon$. Tomemos el único umbral natural $N:=2K+1$. Si $n\ge N$, la dicotomía de paridad escribe $n=2k$ o $n=2k+1$. En el primer caso, $2k\ge2K+1$ excluye $k\le K$ por el crecimiento del producto y, por tanto, $k\ge K$; entonces $|s_n|=h_k<\varepsilon$. En el segundo caso, $2k+1\ge2K+1$ implica $k\ge K$ por cancelación y crecimiento, y $|s_n|=0<\varepsilon$. En ambos casos, $|s_n-0|<\varepsilon$ para todo $n\ge N$; así $s_n\to0$ y

$$
\boxed{\sum_{n=0}^{\infty}a_n=0.}
$$

**Segundo: divergencia de la serie de magnitudes.** Como $h_k>0$ y $|-h_k|=h_k$, los términos de $\operatorname{Abs}(a)$ satisfacen

$$
|a_{2k}|=|a_{2k+1}|=h_k.
$$

Sea $u=\operatorname{PS}(\operatorname{Abs}(a))$ y sea $H=\operatorname{PS}(h)$ la sucesión armónica de sumas parciales. Por recursión, $u_1=h_0+h_0=(1+1)H_0$. Si $u_{2k+1}=(1+1)H_k$, la adición de los términos de la pareja siguiente entrega

$$
\begin{aligned}
u_{2(k+1)+1}
&=u_{2k+1}+|a_{2k+2}|+|a_{2k+3}|\\
&=(1+1)H_k+h_{k+1}+h_{k+1}\\
&=(1+1)H_{k+1}.
\end{aligned}
$$

Por inducción,

$$
\boxed{u_{2k+1}=(1+1)H_k\qquad(k\in\mathbb N).}
\tag{14.8.3}
$$

La serie armónica tiene términos no negativos y diverge (Proposición 14.2.7 — La condición $a_n\to0$ no es suficiente: la serie armónica). Su criterio de convergencia Teorema 14.4.2 — Criterio de convergencia para series de términos no negativos implica, por contraposición, que $H$ no está acotada superiormente. Si la serie de $|a_n|$ convergiera, su sucesión $u$ estaría acotada superiormente por el mismo criterio, digamos $u_n\le M$ para todos los índices. Pero (14.8.3) daría

$$
H_k\le (1+1)^{-1}M\qquad(k\in\mathbb N),
$$

contradicción: el factor $(1+1)^{-1}$ es positivo. Por tanto la serie de magnitudes diverge. Hemos construido una serie convergente que no converge absolutamente, es decir, $a\in\mathcal K_{\mathrm{ser}}$. Junto con Teorema 14.8.3 — La convergencia absoluta implica convergencia ordinaria, esto establece la inclusión propia anunciada. ∎

> **Por qué funciona el ejemplo.** Cada pareja suma exactamente cero, mientras que las magnitudes de sus dos términos suman $h_k+h_k$. Los valores absolutos destruyen la cancelación que estabiliza la suma original. El ejemplo se ha construido directamente con la armónica cerrada: no depende del criterio para series alternadas ni de un teorema de reordenamiento, ambos reservados para más adelante.

**Un contraste adicional.** La presencia de signos alternados tampoco basta para concluir que una serie es sólo condicionalmente convergente. Para $r=-(1+1)^{-1}$ tenemos $|r|=(1+1)^{-1}<1$. El teorema geométrico Teorema 14.3.5 — Convergencia y suma de la serie geométrica para $|r|<1$ prueba la convergencia de $\sum r^n$, mientras que Lema 14.3.3 — El valor absoluto conmuta con las potencias naturales da $|r^n|=|r|^n$ y el mismo teorema prueba que la serie de magnitudes converge. Por tanto esta serie con signos alternados converge **absolutamente**. No se utiliza ninguna regla nueva de intercambio de sumas infinitas.
