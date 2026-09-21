## 16.4. Composición de funciones y el valor en el punto intermedio {#sec-ta-16-4}

La regla informal «el límite de una composición es la composición de los límites» necesita dos precauciones diferentes. Primero, la función exterior sólo puede evaluarse donde está definida. Segundo, la aproximación $f(x)\to b$ permite que $f(x)=b$ ocurra incluso para argumentos $x\ne a$; en cambio, la definición de $\lim_{y\to b}g(y)$ sólo examina $y\ne b$. Por ello construiremos primero el dominio efectivo y después separaremos los dos modos legítimos de controlar el punto intermedio.

### Proposición 16.4.1 — Dominio efectivo y tipado de la composición
Sean $D,E\subseteq\mathbb R$, $f:D\to\mathbb R$ y $g:E\to\mathbb R$. Existe el conjunto

$$
T:=\{x\in D:f(x)\in E\}=f^{-1}[E].
$$

Conservando el grafo de $f\upharpoonright T$ y declarando el **codominio $E$**, obtenemos una función $f_T:T\to E$. Está entonces bien definida, con dominio exacto $T$ y codominio $\mathbb R$, la composición

$$
h:=g\circ f_T:T\longrightarrow\mathbb R,
\qquad h(x)=g(f(x)).
$$

La condición $a\in\operatorname{Acc}(D)$, incluso junto con $\lim_{\substack{x\to a\\x\in D}}f(x)=b$ y $b\in\operatorname{Acc}(E)$, **no garantiza** $a\in\operatorname{Acc}(T)$. Esta última acumulación deberá verificarse o darse como hipótesis antes de atribuir un límite a $h$.

**Demostración.**
La preimagen $T$ existe por Definición §0.6.9 — Imagen y preimagen o, directamente, por Separación en $D$; por definición $T\subseteq D$ y $f[T]\subseteq E$. La restricción $f\upharpoonright T$ tiene dominio $T$ y codominio $\mathbb R$; al conservar su grafo y sustituir ese codominio por $E$, la totalidad y unicidad de los valores permanecen intactas. Por Definición §0.6.4 — Identidad y composición de funciones, $g\circ f_T$ es una función $T\to\mathbb R$ y satisface la ecuación indicada.

Para comprobar la advertencia, tomemos $D=\mathbb R$, $E=\mathbb R\setminus\{0\}$, $a=b=0$ y $f(x)=0$ para todo $x\in D$. El cero es de acumulación tanto de $D$ como de $E$: dado $r>0$, el real $r/2$ es un testigo perforado. Además, $f$ tiene límite $0$ en $0$ por la definición, pero $T=\varnothing$. No puede afirmarse $0\in\operatorname{Acc}(T)$, ni escribirse un límite de la composición en ese punto. ∎

En los resultados que siguen fijaremos precisamente $D,E,f,g,T,f_T,h$ como arriba y supondremos

$$
\boxed{\begin{gathered}
a\in\operatorname{Acc}(T),\qquad b\in\operatorname{Acc}(E),\\
\lim_{\substack{x\to a\\x\in T}}f_T(x)=b,\qquad
\lim_{\substack{y\to b\\y\in E}}g(y)=M.
\end{gathered}}
$$

Estas condiciones no exigen $a\in T$ ni $b\in E$. Cuando se da desde el principio $f:D\to E$, el dominio efectivo es $T=D$; entonces $f_T$ es la misma función tipada y basta asumir $a\in\operatorname{Acc}(D)$.


### Lema 16.4.2 — Control del límite exterior con o sin el centro
Bajo la hipótesis exterior $g:E\to\mathbb R$, $b\in\operatorname{Acc}(E)$ y $\lim_{\substack{y\to b\\y\in E}}g(y)=M$, son equivalentes:

**(i)** $b\notin E$, o bien $b\in E$ y $g(b)=M$.

**(ii)** Para todo $\varepsilon>0$ existe $\eta>0$ tal que

$$
\forall y\in E:\quad |y-b|<\eta
\Longrightarrow |g(y)-M|<\varepsilon.
$$

La diferencia con la definición de límite es que en **(ii)** se admite $y=b$ si éste pertenece a $E$.

**Demostración.**
**(i) $\Rightarrow$ (ii).** Fijemos $\varepsilon>0$ y tomemos el radio $\eta>0$ que entrega el límite exterior. Si $y\in E$ y $|y-b|<\eta$, hay dos casos. Si $y\ne b$, entonces $0<|y-b|<\eta$, por lo que $|g(y)-M|<\varepsilon$. Si $y=b$, necesariamente $b\in E$, y la primera condición impone $g(b)=M$; por ello $|g(y)-M|=0<\varepsilon$. El mismo radio sirve para todos los puntos, sin excluir el centro.

**(ii) $\Rightarrow$ (i).** Si $b\notin E$, se cumple la primera alternativa. Si $b\in E$, supongamos $g(b)\ne M$ y definamos $d:=|g(b)-M|>0$. Apliquemos (ii) con $\varepsilon=d/2$. Para el radio correspondiente, el elemento $y=b$ pertenece a $E$ y satisface $|b-b|=0<\eta$, de modo que $d=|g(b)-M|<d/2$, contradicción. Así $g(b)=M$. ∎

> No hemos definido aquí «continuidad». El lema es una afirmación sobre la desigualdad concreta requerida para componer límites; la teoría general de la continuidad pertenece al Capítulo 17.


### Teorema 16.4.3 — Composición cuando la función interior evita su límite
Supongamos las hipótesis comunes. Si existe $r>0$ tal que

$$
\forall x\in T:\quad 0<|x-a|<r\Longrightarrow f_T(x)\ne b,
$$

entonces

$$
\boxed{\lim_{\substack{x\to a\\x\in T}}(g\circ f_T)(x)=M.}
$$

**Demostración.**
Fijemos una tolerancia $\varepsilon>0$. El límite exterior proporciona $\eta>0$ tal que

$$
y\in E,\quad 0<|y-b|<\eta
\quad\Longrightarrow\quad |g(y)-M|<\varepsilon.
$$

Apliquemos el límite interior con tolerancia $\eta$: existe $\delta_f>0$ tal que, para $x\in T$ y $0<|x-a|<\delta_f$, se tiene $|f_T(x)-b|<\eta$. Tomemos $\delta:=\min\{r,\delta_f\}>0$. Si $x\in T$ y $0<|x-a|<\delta$, el tipado $f_T:T\to E$ da $f_T(x)\in E$ y la hipótesis adicional asegura $f_T(x)\ne b$. Por tanto

$$
0<|f_T(x)-b|<\eta,
\qquad |g(f_T(x))-M|<\varepsilon.
$$

Ésta es la condición $\varepsilon$–$\delta$ para $h:T\to\mathbb R$; la acumulación de $T$ ya figura en las hipótesis comunes. Sólo se eligen dos radios y se calcula su mínimo. ∎

En particular, si $b\notin E$, la exclusión es automática: ningún $f_T(x)\in E$ puede ser igual a $b$.


### Teorema 16.4.4 — Composición cuando el valor exterior coincide con su límite
Supongamos las hipótesis comunes y, además,

$$
b\in E,\qquad g(b)=M.
$$

Entonces, sin ninguna restricción sobre la frecuencia con que $f_T(x)=b$,

$$
\boxed{\lim_{\substack{x\to a\\x\in T}}(g\circ f_T)(x)=M.}
$$

**Demostración.**
Sea $\varepsilon>0$. El Lema 16.4.2, aplicado a las hipótesis exteriores y a $g(b)=M$, proporciona $\eta>0$ tal que **todo** $y\in E$ con $|y-b|<\eta$ verifica $|g(y)-M|<\varepsilon$, incluido el eventual valor $y=b$. Por el límite de $f_T$ existe $\delta>0$ tal que, para $x\in T$ con $0<|x-a|<\delta$, se cumple $|f_T(x)-b|<\eta$. Como $f_T(x)\in E$, podemos sustituir $y=f_T(x)$ en la estimación inclusiva: $|h(x)-M|<\varepsilon$. No se ha supuesto ni deducido que $f_T(x)\ne b$. ∎


### Teorema 16.4.5 — Necesidad de evitar el centro cuando el valor exterior difiere
Supongamos las hipótesis comunes y que $b\in E$ pero $g(b)\ne M$. Entonces las condiciones siguientes son equivalentes:

$$
\boxed{\lim_{\substack{x\to a\\x\in T}}h(x)=M}
$$

y

$$
\boxed{\exists r>0\ \forall x\in T:\quad
0<|x-a|<r\Longrightarrow f_T(x)\ne b.}
$$

**Demostración.**
La segunda condición implica la primera por el Teorema 16.4.3. Recíprocamente, supongamos $h\to M$. Como $g(b)\ne M$, el número $d:=|g(b)-M|$ es positivo. La definición del límite de $h$ aplicada a $\varepsilon:=d/2$ proporciona $r>0$ tal que

$$
x\in T,\quad0<|x-a|<r
\quad\Longrightarrow\quad|g(f_T(x))-M|<d/2.
$$

Ninguno de esos puntos puede satisfacer $f_T(x)=b$, pues entonces la última desigualdad sería $d=|g(b)-M|<d/2$, imposible. Así, el mismo radio $r$ asegura la segunda condición. La necesidad se prueba examinando un punto arbitrario de la vecindad, sin elegir una sucesión de puntos infractores. ∎

**Contraejemplo a la regla sin hipótesis.** Pongamos $D=E=\mathbb R$, $a=b=M=0$, $f(x)=0$ para todo $x$, y

$$
g(y)=\begin{cases}1,&y=0,\\0,&y\ne0.\end{cases}
$$

Ambos centros son puntos de acumulación. La función $f$ tiene límite $0$ en $0$, y también $g(y)\to0$ cuando $y\to0$: en la vecindad perforada $g$ es idénticamente cero, como comprobamos en §16.1.5. Sin embargo $g(f(x))=g(0)=1$ para **todo** $x$, por lo que la composición tiene límite $1$ y no $0$, según la unicidad Teorema §16.1.4 — Unicidad del límite finito. El defecto no es de tipado ni de acumulación: únicamente falta controlar $g(b)$ o evitar que la función interior tome el valor $b$.


### Corolario 16.4.6 — Criterio exacto de composición de límites finitos
Bajo las hipótesis comunes de esta sección, el límite de la composición es $M$ **si y sólo si** ocurre al menos una de estas dos circunstancias:

$$
\boxed{\begin{aligned}
&\exists r>0\ \forall x\in T:
\bigl(0<|x-a|<r\Longrightarrow f_T(x)\ne b\bigr);\\[2pt]
&\text{o bien }\ b\in E\ \text{y}\ g(b)=M.
\end{aligned}}
$$

En particular, para funciones dadas directamente como $f:D\to E$ y $g:E\to\mathbb R$, basta sustituir $T=D$ y exigir $a\in\operatorname{Acc}(D)$; el límite de $f$ se interpreta entonces a través de $D$.

**Demostración.**
Si se cumple la primera circunstancia, aplica Teorema §16.4.3 — Composición cuando la función interior evita su límite; si se cumple la segunda, aplica Teorema §16.4.4 — Composición cuando el valor exterior coincide con su límite. Para la necesidad supongamos $h\to M$. Si $b\notin E$, la primera circunstancia se cumple con cualquier $r>0$, porque el recorrido de $f_T$ está contenido en $E$. Si $b\in E$, separamos los casos $g(b)=M$ y $g(b)\ne M$. En el primero se cumple la segunda circunstancia; en el segundo, Teorema §16.4.5 — Necesidad de evitar el centro cuando el valor exterior difiere proporciona el radio de exclusión de la primera. Éstos agotan los casos en la lógica clásica del tratado. ∎

> **Lectura conceptual.** Una función exterior puede tener un límite perfectamente determinado y, aun así, asignar un valor diferente en el punto intermedio. La composición sólo falla por ese valor cuando la función interior lo alcanza arbitrariamente cerca del punto inicial. El criterio precedente identifica exactamente esa obstrucción, además de hacer explícito el dominio efectivo. No presupone continuidad ni usa la recíproca secuencial condicional.


El dominio y el punto intermedio están ya controlados para la composición. La siguiente unidad examinará **límites laterales**, para los que la procedencia izquierda o derecha de los argumentos debe incorporarse al dominio sin redefinir el orden real ni atribuir un límite a un conjunto sin puntos de acumulación en el lado elegido.
