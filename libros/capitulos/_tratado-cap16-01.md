## 16.1. Dominio, definición del límite y unicidad {#sec-ta-16-1}

La noción de acumulación proporciona exactamente la disponibilidad de puntos que necesitaremos. Conviene expresarla primero sin conjuntos perforados, mediante una desigualdad.

### Lema 16.1.1 — Acumulación y aproximación perforada
Sean $D\subseteq\mathbb R$ y $a\in\mathbb R$. Entonces

$$
\boxed{a\in\operatorname{Acc}(D)
\iff
\forall r\in\mathbb R\,(r>0\Rightarrow
\exists x\in D:\ 0<|x-a|<r).}
$$

**Demostración.**
Por Definición §15.5.1 — Punto de acumulación y Definición §15.5.2 — Conjunto derivado o conjunto de puntos de acumulación, $a\in\operatorname{Acc}(D)$ significa que para cada $r>0$ existe un elemento de $(B_r(a)\setminus\{a\})\cap D$. Por la definición de bola (Definición §15.1.1 — Bola abierta en la recta), pertenecer a $B_r(a)$ equivale a $|x-a|<r$. Por la caracterización del valor absoluto (Proposición §4.2.2 — Propiedades elementales del valor absoluto), $x\ne a$ equivale a $|x-a|>0$. Por tanto, dicho elemento satisface simultáneamente $x\in D$ y $0<|x-a|<r$. A la inversa, un punto que cumple estas dos condiciones pertenece a la intersección perforada correspondiente. Ambas implicaciones valen para cada $r>0$, lo que prueba la equivalencia. ∎

> **Lectura de cuantificadores.** El lema afirma $\forall r>0\,\exists x\in D$; no construye ni necesita una sucesión $x_0,x_1,\ldots$ elegida simultáneamente. Para cada radio de una prueba concreta basta obtener un punto.


### Definición 16.1.2 — Límite real finito de una función
Sean $D\subseteq\mathbb R$, una función $f:D\to\mathbb R$, un punto $a\in\operatorname{Acc}(D)$ y un número $L\in\mathbb R$. Diremos que $f$ tiene límite finito $L$ cuando $x$ tiende a $a$ a través del dominio $D$ si

$$
\boxed{
\forall\varepsilon\in\mathbb R\ \bigl(\varepsilon>0\Rightarrow
\exists\delta\in\mathbb R\,[\delta>0\ \land
\forall x\in D\,(0<|x-a|<\delta
\Rightarrow |f(x)-L|<\varepsilon)]\bigr).
}
$$

Cuando esta relación se cumple escribiremos

$$
\boxed{\lim_{\substack{x\to a\\x\in D}} f(x)=L.}
$$

Si el dominio de la función ya es inequívoco, podremos abreviar la expresión como $\lim_{x\to a}f(x)=L$. El límite es aquí una relación entre datos tipados y un candidato $L$; la unicidad necesaria para hablar sin ambigüedad de *el* límite se demostrará en el Teorema 16.1.4. La notación sólo se utilizará cuando $a\in\operatorname{Acc}(D)$; si no lo está, no asignaremos un límite por la veracidad vacía de las implicaciones.

La primera desigualdad, $0<|x-a|$, elimina precisamente $x=a$. No exigimos $a\in D$ y, cuando sí pertenezca, no utilizamos $f(a)$ en la condición. Además, $\delta$ puede depender de $\varepsilon$, de la función y de los puntos y valores fijados, pero no puede depender del $x$ que aparece bajo el cuantificador universal.

> **Traducción lógica.** Para cualquier tolerancia positiva propuesta para la salida, debe existir un margen positivo de entrada tal que *todos* los argumentos del dominio situados dentro de ese margen, excepto el centro, produzcan imágenes dentro de la tolerancia. No basta encontrar un argumento favorable ni se exige un único $\delta$ que sirva para todas las tolerancias.


### Proposición 16.1.3 — Criterio mediante imágenes de bolas perforadas
Sean $f:D\to\mathbb R$ y $a\in\operatorname{Acc}(D)$, con $L\in\mathbb R$. La relación $\lim_{\substack{x\to a\\x\in D}} f(x)=L$ equivale a

$$
\boxed{\forall\varepsilon>0\ \exists\delta>0:\quad
f\!\left[D\cap\bigl(B_\delta(a)\setminus\{a\}\bigr)\right]
\subseteq B_\varepsilon(L).}
$$

**Demostración.**
Supongamos la condición $\varepsilon$–$\delta$ y fijemos $\varepsilon>0$. Existe $\delta>0$ con la implicación definitoria para todo $x\in D$. Si $y$ pertenece a la imagen indicada, por la definición de imagen directa Definición §0.6.9 — Imagen y preimagen existe $x\in D\cap(B_\delta(a)\setminus\{a\})$ con $y=f(x)$. La pertenencia al conjunto perforado da $0<|x-a|<\delta$, y la condición del límite da $|y-L|<\varepsilon$, esto es, $y\in B_\varepsilon(L)$. Se obtiene la inclusión.

Recíprocamente, supongamos las inclusiones de imágenes. Dado $\varepsilon>0$, tomemos el $\delta>0$ suministrado por la hipótesis. Si $x\in D$ y $0<|x-a|<\delta$, entonces $x\in D\cap(B_\delta(a)\setminus\{a\})$ y su imagen pertenece a $B_\varepsilon(L)$. Esto significa $|f(x)-L|<\varepsilon$, exactamente la condición de la definición. ∎

La caracterización no introduce una topología de subespacios: la intersección con $D$ aparece dentro de cada fórmula y las dos bolas son las ya definidas en la recta real.


### Teorema 16.1.4 — Unicidad del límite finito
Sean $f:D\to\mathbb R$ y $a\in\operatorname{Acc}(D)$. Si $L,M\in\mathbb R$ satisfacen

$$
\lim_{\substack{x\to a\\x\in D}}f(x)=L
\qquad\text{y}\qquad
\lim_{\substack{x\to a\\x\in D}}f(x)=M,
$$

entonces $L=M$. Así, un límite real finito, cuando existe, está determinado de manera única.

**Demostración.**
Supongamos que $L\ne M$. La propiedad del valor absoluto Proposición §4.2.2 — Propiedades elementales del valor absoluto implica que $d:=|L-M|>0$. Definamos $\varepsilon:=d/(1+1+1)>0$, donde los unos y las operaciones corresponden al cuerpo real, sin identificar conjuntos numéricos por inclusión literal.

La hipótesis de límite $L$ proporciona $\delta_L>0$ tal que

$$
 x\in D,\quad 0<|x-a|<\delta_L
 \quad\Longrightarrow\quad |f(x)-L|<\varepsilon.
$$

Análogamente, el límite $M$ proporciona $\delta_M>0$ con la desigualdad correspondiente para $M$. Tomemos $r:=\min\{\delta_L,\delta_M\}>0$. Como $a$ es punto de acumulación de $D$, el Lema 16.1.1 proporciona un punto $x\in D$ tal que $0<|x-a|<r$. Ambas estimaciones se aplican a ese mismo punto. Por la desigualdad triangular Teorema §4.2.3 — Desigualdad triangular,

$$
\begin{aligned}
 d=|L-M|
 &\le |L-f(x)|+|f(x)-M|\\
 &<2\varepsilon=\frac{2}{3}d<d,
\end{aligned}
$$

una contradicción. Por tanto $L=M$. Los dos radios y el único punto utilizado se obtienen mediante eliminación de existenciales finitos; no se ha construido una sucesión de elecciones. ∎

> **Por qué importa la acumulación.** Si $D=\{a\}$, la implicación de la definición, sin la hipótesis de acumulación, sería verdadera para todo $L$: ningún $x\in D$ cumple $0<|x-a|$. En tal caso la demostración anterior fallaría precisamente donde necesita obtener un $x$ cercano y distinto de $a$. La hipótesis no es ornamental: evita una definición vacía y hace posible la unicidad.


### Proposición 16.1.5 — Carácter local y libertad del valor puntual
Sean $f,g:D\to\mathbb R$ dos funciones con el mismo dominio y sea $a\in\operatorname{Acc}(D)$. Supongamos que existe $r>0$ tal que

$$
\forall x\in D:\quad 0<|x-a|<r\ \Longrightarrow\ f(x)=g(x).
$$

Entonces, para cada $L\in\mathbb R$,

$$
\boxed{\lim_{\substack{x\to a\\x\in D}}f(x)=L
\iff
\lim_{\substack{x\to a\\x\in D}}g(x)=L.}
$$

En particular, si $a\in D$, modificar exclusivamente el valor asignado en $a$ no modifica ningún límite finito de la función en dicho punto.

**Demostración.**
Supongamos que el límite de $f$ es $L$ y fijemos $\varepsilon>0$. Existe $\delta_f>0$ tal que $x\in D$ y $0<|x-a|<\delta_f$ implican $|f(x)-L|<\varepsilon$. Definamos $\delta:=\min\{\delta_f,r\}>0$. Para $x\in D$ con $0<|x-a|<\delta$ se cumplen simultáneamente $|x-a|<\delta_f$ y $|x-a|<r$. Por la hipótesis, $g(x)=f(x)$, de donde

$$
|g(x)-L|=|f(x)-L|<\varepsilon.
$$

Esto demuestra que $g$ tiene límite $L$. La implicación inversa se obtiene con idéntico argumento intercambiando $f$ y $g$, ya que la igualdad puntual es simétrica. Si ambas funciones difieren a lo sumo en $a$, coinciden automáticamente para todo $x\in D$ con $x\ne a$ y, en particular, cumplen la hipótesis con cualquier $r>0$. ∎

**Ejemplo de lectura.** Sea $D=\mathbb R$ y definamos $g:D\to\mathbb R$ por $g(0)=1$ y $g(x)=0$ para $x\ne0$. La función está bien definida por una regla funcional por casos, y $0\in\operatorname{Acc}(\mathbb R)$: dado $r>0$, el punto $r/(1+1)$ es real, distinto de cero y de valor absoluto menor que $r$. Para cualquier $\varepsilon>0$, podemos tomar $\delta=1$, pues $0<|x|<\delta$ implica $|g(x)-0|=0<\varepsilon$. Por consiguiente,

$$
\boxed{\lim_{x\to0}g(x)=0\quad\text{mientras que}\quad g(0)=1.}
$$

La misma comprobación vale para la función constante cero: los valores cercanos, y no el valor en el centro, deciden el límite.


Hemos construido el límite como una relación local no vacía, probado una caracterización con bolas y demostrado su unicidad. En la siguiente sección investigaremos qué pueden detectar las sucesiones del dominio. La implicación «límite funcional $\Rightarrow$ mismo límite a lo largo de cualquier sucesión del dominio que tienda a $a$ sin alcanzarlo» utiliza únicamente la definición; una recíproca universal para dominios arbitrarios requiere una revisión separada de los posibles selectores de puntos. No adoptaremos tácitamente `CC(\mathbb R)`.
