## 16.3. Álgebra y orden de límites finitos {#sec-ta-16-3}

Hasta ahora hemos caracterizado el límite de una función mediante la proximidad de sus valores y hemos precisado el alcance del criterio secuencial. Queremos saber qué ocurre si combinamos dos funciones que tienen límite en el mismo punto. La respuesta se basará directamente en la definición $\varepsilon$–$\delta$: no necesitamos deducir límites funcionales de condiciones secuenciales y, por tanto, no necesitamos ningún principio de elección.

En esta sección fijaremos $D\subseteq\mathbb R$, un punto $a\in\operatorname{Acc}(D)$ y funciones $f,g:D\to\mathbb R$ con límites finitos respectivos $L,M\in\mathbb R$ en $a$, salvo que un enunciado especifique otras hipótesis. Todos los límites son **relativos a su dominio declarado**. El punto $a$ puede no pertenecer a $D$.

### Lema 16.3.1 — Acotación local perforada de una función con límite
Si $\lim_{\substack{x\to a\\x\in D}}f(x)=L$, existen $r>0$ y $K>0$ tales que

$$
\forall x\in D:\quad 0<|x-a|<r\ \Longrightarrow\ |f(x)|<K.
$$

**Demostración.**
Apliquemos la definición con la tolerancia real $1>0$. Obtenemos $r>0$ tal que $0<|x-a|<r$, $x\in D$, implica $|f(x)-L|<1$. Por la desigualdad triangular,

$$
|f(x)|\le |f(x)-L|+|L|<1+|L|.
$$

El número $K:=1+|L|$ es positivo. Estos $r,K$ satisfacen la conclusión. No se afirma que $f$ esté acotada en todo $D$, ni se toma su valor en $a$. ∎

La acotación local será necesaria para el producto: dos errores pequeños se multiplican por valores de funciones que deben permanecer controlados.


### Proposición 16.3.2 — Existencia y tipado de las operaciones puntuales
Para $f,g:D\to\mathbb R$ y $c\in\mathbb R$ están determinadas unívocamente las funciones

$$
\begin{aligned}
f+g &:D\to\mathbb R, &(f+g)(x)&=f(x)+g(x),\\
f-g &:D\to\mathbb R, &(f-g)(x)&=f(x)-g(x),\\
cf &:D\to\mathbb R, &(cf)(x)&=c\,f(x),\\
fg &:D\to\mathbb R, &(fg)(x)&=f(x)g(x),\\
|f| &:D\to\mathbb R, &|f|(x)&=|f(x)|.
\end{aligned}
$$

Sea $D_g:=\{x\in D:g(x)\ne0\}$. También están determinadas las funciones

$$
\frac1g:D_g\to\mathbb R,\qquad
\frac fg:D_g\to\mathbb R,
$$

por los valores $g(x)^{-1}$ y $f(x)g(x)^{-1}$, respectivamente. El cociente **no** se declara función sobre todo $D$ cuando $g$ puede anularse.

**Demostración.**
Para cualquiera de las primeras cinco expresiones, definamos su grafo por Separación dentro de $D\times\mathbb R$: un par $\langle x,y\rangle$ pertenece al grafo precisamente si $y$ es la correspondiente expresión algebraica en $f(x)$ y $g(x)$, o en $f(x)$ únicamente. Como las operaciones y el valor absoluto están definidos en el cuerpo real y dan un único real para cada $x\in D$, el grafo es funcional y total en $D$. Declarar dominio $D$ y codominio $\mathbb R$ completa cada función en el sentido de Definición §0.6.1 — Función como dominio, codominio y grafo.

El conjunto $D_g$ existe por Separación sobre $D$. Si $x\in D_g$, la estructura de cuerpo garantiza que $g(x)^{-1}$ existe y es único. La misma construcción por grafo, ahora dentro de $D_g\times\mathbb R$, da $1/g$ y $f/g$ con los codominios y dominios anunciados. Si $D_g=\varnothing$, los grafos vacíos siguen definiendo funciones, pero aún no se les puede atribuir límite en $a$. Ninguna construcción escoge representantes o valores arbitrarios. ∎


### Teorema 16.3.3 — Suma, resta y multiplicación por escalares
Si $f\to L$ y $g\to M$ cuando $x\to a$ a través de $D$, entonces, para todo $c\in\mathbb R$,

$$
\boxed{\lim_{x\to a}(f+g)(x)=L+M,\qquad
\lim_{x\to a}(f-g)(x)=L-M,\qquad
\lim_{x\to a}(cf)(x)=cL.}
$$

Estas tres relaciones usan el mismo dominio $D$.

**Demostración.**
**Suma.** Dado $\varepsilon>0$, apliquemos el límite de $f$ con $\varepsilon/2$ y el de $g$ con la misma tolerancia. Obtenemos radios positivos $\delta_f,\delta_g$. Para $\delta:=\min\{\delta_f,\delta_g\}>0$, todo $x\in D$ que cumpla $0<|x-a|<\delta$ satisface

$$
\begin{aligned}
|(f+g)(x)-(L+M)|
&=|(f(x)-L)+(g(x)-M)|\\
&\le |f(x)-L|+|g(x)-M|\\
&<\varepsilon/2+\varepsilon/2=\varepsilon.
\end{aligned}
$$

**Multiplicación escalar.** Si $c=0$, la función $cf$ es idénticamente cero y la desigualdad requerida es $0<\varepsilon$, para cualquier radio positivo. Si $c\ne0$, utilicemos para $f$ la tolerancia $\varepsilon/|c|>0$. El radio obtenido satisface

$$
|cf(x)-cL|=|c|\,|f(x)-L|<\varepsilon.
$$

**Resta.** La regla escalar con $c=-1$ demuestra que $-g$ tiene límite $-M$. La regla de la suma aplicada a $f$ y $-g$ concluye que $f-g$ tiene límite $L-M$. Todos los radios combinados son finitos en número: ninguna selección numerable interviene. ∎


### Teorema 16.3.4 — Producto y valor absoluto
Bajo las hipótesis iniciales,

$$
\boxed{\lim_{x\to a}(fg)(x)=LM,
\qquad \lim_{x\to a}|f|(x)=|L|.}
$$

**Demostración.**
**Producto.** Por Lema §16.3.1 — Acotación local perforada de una función con límite, existen $r>0$ y $K>0$ tales que $|g(x)|<K$ para $x\in D$ con $0<|x-a|<r$; podemos, concretamente, tomar $K=|M|+1$. Fijemos $\varepsilon>0$. El límite de $f$ proporciona $\delta_f>0$ para la tolerancia $\varepsilon/(2K)>0$, y el de $g$ proporciona $\delta_g>0$ para $\varepsilon/(2(|L|+1))>0$. Con

$$
\delta:=\min\{r,\delta_f,\delta_g\}>0
$$

obtenemos, para cada $x\in D$ que cumpla $0<|x-a|<\delta$,

$$
\begin{aligned}
|f(x)g(x)-LM|
&=|(f(x)-L)g(x)+L(g(x)-M)|\\
&\le |f(x)-L|\,|g(x)|+|L|\,|g(x)-M|\\
&<\frac{\varepsilon}{2K}K+
\frac{\varepsilon}{2(|L|+1)}|L|
\le\varepsilon.
\end{aligned}
$$

La primera desigualdad es estricta por las estimaciones de ambos límites; en consecuencia, el resultado final es $|f(x)g(x)-LM|<\varepsilon$, como exige la definición.

**Valor absoluto.** La desigualdad triangular inversa, ya demostrada en Corolario §4.2.4 — Desigualdad triangular inversa, da

$$
\bigl||f(x)|-|L|\bigr|\le |f(x)-L|.
$$

El radio del límite de $f$ correspondiente a $\varepsilon$ sirve sin modificación. No se ha presupuesto ningún teorema de continuidad para el valor absoluto. ∎

> **Por qué no basta invocar el álgebra secuencial.** El resultado Teorema §13.5.3 — Límite de un producto del Capítulo 13 establece el producto de sucesiones convergentes. Convertirlo en límite de funciones usando la recíproca del criterio secuencial exigiría hipótesis adicionales sobre el dominio; la demostración anterior evita enteramente ese desvío.


### Lema 16.3.5 — Separación local de un denominador con límite no nulo
Si $\lim_{\substack{x\to a\\x\in D}}g(x)=M$ y $M\ne0$, existe $r>0$ tal que

$$
\forall x\in D:\quad 0<|x-a|<r\Longrightarrow
|g(x)|>\frac{|M|}{2}>0.
$$

En particular, $g(x)\ne0$ en esa vecindad perforada, y el conjunto $D_g=\{x\in D:g(x)\ne0\}$ coincide allí con $D$.

**Demostración.**
Como $M\ne0$, $|M|/2>0$. Apliquemos el límite de $g$ con tolerancia $|M|/2$ y llamemos $r>0$ al radio obtenido. Para los puntos especificados se cumple $|g(x)-M|<|M|/2$. La desigualdad triangular inversa implica

$$
|g(x)|\ge |M|-|g(x)-M|>|M|/2>0.
$$

Por la caracterización del valor absoluto, $g(x)\ne0$. El conjunto $D_g$ existe por Separación y contiene todos los puntos perforados de $D$ dentro del radio $r$. La inclusión contraria $D_g\subseteq D$ es definitoria. ∎


### Teorema 16.3.6 — Recíproco y cociente: precisión del dominio
Supongamos $M\ne0$ y definamos $D_g=\{x\in D:g(x)\ne0\}$. Entonces:

1. $a\in\operatorname{Acc}(D_g)$;
2. las funciones $1/g$ y $f/g$ tienen dominio $D_g$ y límites finitos

$$
\boxed{
\lim_{\substack{x\to a\\x\in D_g}}\frac1{g(x)}=\frac1M,
\qquad
\lim_{\substack{x\to a\\x\in D_g}}\frac{f(x)}{g(x)}=\frac LM.}
$$

El límite de $f$ relativo a $D$ también es límite de su restricción a $D_g$, pues una implicación válida para todos los puntos próximos de $D$ sigue siendo válida en el subconjunto $D_g$.

**Demostración.**
El lema anterior proporciona $r>0$ con $D\cap(B_r(a)\setminus\{a\})\subseteq D_g$. Dado $\rho>0$, por $a\in\operatorname{Acc}(D)$ y Lema §16.1.1 — Acumulación y aproximación perforada existe **un solo** punto $x\in D$ tal que $0<|x-a|<\min\{r,\rho\}$. Este $x$ también pertenece a $D_g$; aplicar de nuevo el criterio de acumulación demuestra $a\in\operatorname{Acc}(D_g)$. No se ha seleccionado una familia de puntos.

Fijemos ahora $\varepsilon>0$. Por $g\to M$, existe $\delta_g>0$ que fuerza

$$
|g(x)-M|<\frac{\varepsilon|M|^2}{2}
$$

cuando $x\in D$ y $0<|x-a|<\delta_g$. Sea $\delta:=\min\{r,\delta_g\}>0$. Para $x\in D_g$ en esa vecindad perforada, el lema da $|g(x)|>|M|/2$ y, por tanto,

$$
\left|\frac1{g(x)}-\frac1M\right|
=\frac{|g(x)-M|}{|g(x)|\,|M|}
\le\frac{2|g(x)-M|}{|M|^2}
<\varepsilon.
$$

Hemos demostrado el límite del recíproco con su dominio exacto. La función restringida $f\upharpoonright D_g:D_g\to\mathbb R$ conserva el límite $L$ porque $D_g\subseteq D$ y acabamos de verificar la acumulación necesaria. En $D_g$ el producto de esa restricción por $1/g$ coincide, como función con dominio y codominio, con $f/g$. Aplicar Teorema §16.3.4 — Producto y valor absoluto **sobre $D_g$** produce el límite $L\,(1/M)=L/M$. ∎

> **No se divide por un límite cero.** Si $M=0$, ninguna estimación anterior proporciona una cota inferior positiva para $|g(x)|$; además, $1/M$ no está definido en el cuerpo real. La existencia del cociente como función sobre $D_g$ por sí sola no asegura la existencia de un límite finito.


### Teorema 16.3.7 — Orden y separación estricta
Sean $f,g:D\to\mathbb R$ con límites $L,M$ en $a$. Se cumplen las siguientes afirmaciones:

**(i)** Si existen $r>0$ y la desigualdad $f(x)\le g(x)$ para todo $x\in D$ con $0<|x-a|<r$, entonces $L\le M$.

**(ii)** Si $L<M$, existe $r>0$ tal que $f(x)<g(x)$ para todo $x\in D$ con $0<|x-a|<r$.

En general, de $f(x)<g(x)$ para todos los puntos suficientemente próximos **no se sigue** $L<M$.

**Demostración.**
**(i)** Supongamos por contradicción $L>M$. Sea $\varepsilon:=(L-M)/3>0$. Existen radios $\delta_f,\delta_g>0$ tales que, en sus respectivas vecindades perforadas,

$$
 f(x)>L-\varepsilon,
\qquad g(x)<M+\varepsilon.
$$

Tomemos $\rho=\min\{r,\delta_f,\delta_g\}>0$. Por acumulación, Lema §16.1.1 — Acumulación y aproximación perforada proporciona **un** $x\in D$ con $0<|x-a|<\rho$. Entonces

$$
f(x)>L-\varepsilon>M+\varepsilon>g(x),
$$

porque $L-M=3\varepsilon>2\varepsilon$. Esto contradice $f(x)\le g(x)$ y prueba $L\le M$.

**(ii)** Sea $\varepsilon:=(M-L)/3>0$. Tomemos los radios de los límites de $f$ y $g$ correspondientes a $\varepsilon$ y su mínimo $r>0$. En todo punto perforado de $D$ bajo ese radio,

$$
f(x)<L+\varepsilon<M-\varepsilon<g(x),
$$

lo que establece la separación estricta.

**Advertencia sobre el signo estricto.** En $D=\mathbb R$, $a=0$, $f(x)=0$ y $g(x)=|x|$, para todo $x\ne0$ se cumple $f(x)<g(x)$. Sin embargo, ambos límites son cero: para $f$ cualquier radio sirve y para $g$ basta $\delta=\varepsilon$, pues $||x|-0|=|x|<\varepsilon$. Se cumple $L=M=0$, no $L<M$. ∎


### Corolario 16.3.8 — Teorema del sándwich para límites de funciones
Sean $f,h,g:D\to\mathbb R$, $a\in\operatorname{Acc}(D)$, y supongamos que, para cierto $r>0$,

$$
\forall x\in D:\quad 0<|x-a|<r\Longrightarrow f(x)\le h(x)\le g(x).
$$

Si $f$ y $g$ tienen el **mismo** límite finito $L$ en $a$, entonces también

$$
\boxed{\lim_{\substack{x\to a\\x\in D}}h(x)=L.}
$$

**Demostración.**
Fijemos $\varepsilon>0$. Los límites de $f$ y $g$ suministran radios positivos $\delta_f$ y $\delta_g$ tales que $|f(x)-L|<\varepsilon$ y $|g(x)-L|<\varepsilon$ en sus respectivas vecindades perforadas. Sea $\delta:=\min\{r,\delta_f,\delta_g\}>0$. Para cualquier $x\in D$ con $0<|x-a|<\delta$ se obtiene

$$
L-\varepsilon<f(x)\le h(x)\le g(x)<L+\varepsilon.
$$

Esta doble desigualdad equivale a $|h(x)-L|<\varepsilon$, exactamente la definición de límite para $h$. No se ha empleado el criterio secuencial. ∎

> **Ejercicio de control de hipótesis.** En la regla del producto no se exige $L$ ni $M$ distinto de cero. En el cociente sí se exige $M\ne0$; el dominio efectivo de la función cociente se reduce a $D_g$. En la preservación del orden, una desigualdad estricta de valores puede producir igualdad de límites. En el sándwich, las funciones extremas deben tener el mismo límite.


Los límites finitos admiten las operaciones algebraicas y las comparaciones demostradas, siempre con los dominios y la acumulación adecuados. La siguiente sección estudiará la composición $g\circ f$: allí habrá que asegurar que las imágenes de los puntos cercanos pertenecen al dominio de la función exterior y atender especialmente al caso en que $f(x)$ alcanza exactamente su valor límite.
