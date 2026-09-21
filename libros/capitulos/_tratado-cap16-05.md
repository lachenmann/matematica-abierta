## 16.5. Límites laterales y reconstrucción del límite bilateral {#sec-ta-16-5}

La proximidad expresada por $|x-a|<\delta$ no distingue de qué lado llega el argumento. Sin embargo, el orden real permite separar sin ambigüedad los puntos menores y mayores que $a$. Un límite lateral no será una fórmula vacía aplicada a cualquier dominio: primero verificaremos que hay puntos del lado elegido arbitrariamente próximos a $a$. Tampoco añadiremos $-\infty$ o $+\infty$ al cuerpo real; los lados se definirán por desigualdades entre números reales ordinarios.

### Definición 16.5.1 — Dominios laterales de aproximación
Para $D\subseteq\mathbb R$ y $a\in\mathbb R$, definimos los dominios laterales

$$
\boxed{D_a^-:=\{x\in D:x<a\},\qquad
D_a^+:=\{x\in D:a<x\}.}
$$

Ambos existen por Separación sobre $D$ y satisfacen $D_a^-\subseteq D$, $D_a^+\subseteq D$ y $a\notin D_a^-\cup D_a^+$. Para $f:D\to\mathbb R$, las restricciones $f\upharpoonright D_a^-$ y $f\upharpoonright D_a^+$ existen como funciones de sus respectivos dominios a $\mathbb R$ (Definición §1.3.1 — Restricción de una función). Estos superíndices designan lados del dominio, no un opuesto, un inverso funcional ni un número infinito.

El orden total da la descomposición puntual

$$
\boxed{D\setminus\{a\}=D_a^-\cup D_a^+,\qquad
D_a^-\cap D_a^+=\varnothing.}
$$

En efecto, un $x\in D$ distinto de $a$ cumple exactamente una de $x<a$ o $a<x$, y cada una implica $x\ne a$. Las igualdades son identidades de conjuntos obtenidas por doble inclusión; no suponen que $a\in D$.


### Lema 16.5.2 — La acumulación procede de al menos un lado
Para todo $D\subseteq\mathbb R$ y todo $a\in\mathbb R$,

$$
\boxed{a\in\operatorname{Acc}(D)
\iff a\in\operatorname{Acc}(D_a^-)
\ \lor\ a\in\operatorname{Acc}(D_a^+).}
$$

**Demostración.**
Si $a$ es punto de acumulación de uno de los dos dominios laterales, cada radio $r>0$ contiene un punto de ese dominio distinto de $a$ por Lema §16.1.1 — Acumulación y aproximación perforada. Puesto que ambos están contenidos en $D$, el mismo punto acredita $a\in\operatorname{Acc}(D)$.

Para la implicación restante, supongamos $a\in\operatorname{Acc}(D)$ y, por contradicción, que $a$ no es punto de acumulación de ninguno de los dos dominios. La negación clásica del criterio Lema §16.1.1 — Acumulación y aproximación perforada proporciona radios $r_->0$ y $r_+>0$ tales que

$$
\begin{aligned}
&\nexists x\in D_a^-:\ 0<|x-a|<r_-,\\
&\nexists x\in D_a^+:\ 0<|x-a|<r_+.
\end{aligned}
$$

Sea $r:=\min\{r_-,r_+\}>0$. La acumulación de $D$ entrega un $x\in D$ con $0<|x-a|<r$. Como $x\ne a$, la descomposición de la definición anterior obliga a $x\in D_a^-$ o $x\in D_a^+$. Cualquiera de los dos casos contradice la exclusión que corresponde a su lado. Por tanto, al menos un dominio lateral acumula en $a$. Sólo hemos combinado dos radios: no se ha escogido una sucesión de puntos. ∎

**Importante.** El lema no afirma que haya acumulación por ambos lados. Un dominio como $D=\{x\in\mathbb R:x\ge a\}$ tiene acumulación en $a$ únicamente por la derecha: para cualquier $r>0$, $a+r/2$ es un testigo derecho, mientras que $D_a^-=\varnothing$.


### Definición 16.5.3 — Límites finitos por la izquierda y por la derecha
Sea $f:D\to\mathbb R$ y $a,L\in\mathbb R$. Cuando $a\in\operatorname{Acc}(D_a^-)$, diremos que $f$ tiene límite por la izquierda igual a $L$ si

$$
\boxed{\lim_{\substack{x\to a^-\\x\in D}}f(x)=L
\quad:\Longleftrightarrow\quad
\lim_{\substack{x\to a\\x\in D_a^-}}
(f\upharpoonright D_a^-)(x)=L.}
$$

Cuando $a\in\operatorname{Acc}(D_a^+)$, definimos análogamente

$$
\boxed{\lim_{\substack{x\to a^+\\x\in D}}f(x)=L
\quad:\Longleftrightarrow\quad
\lim_{\substack{x\to a\\x\in D_a^+}}
(f\upharpoonright D_a^+)(x)=L.}
$$

La definición reutiliza el límite finito Definición §16.1.2 — Límite real finito de una función relativo a su dominio; no redefine la noción mediante el valor $f(a)$ ni autoriza escribir un límite lateral cuando el lado elegido carece de puntos de acumulación. La unicidad para cada lado se hereda de Teorema §16.1.4 — Unicidad del límite finito. El superíndice $-$ o $+$ unido a $a$ designa la dirección de aproximación, no una operación aritmética sobre $a$.


### Proposición 16.5.4 — Caracterizaciones unilaterales $\varepsilon$–$\delta$
Supongamos $a\in\operatorname{Acc}(D_a^-)$ y $L\in\mathbb R$. Entonces

$$
\boxed{\lim_{\substack{x\to a^-\\x\in D}}f(x)=L
\iff\forall\varepsilon>0\ \exists\delta>0\ \forall x\in D:\
\bigl(0<a-x<\delta\Rightarrow |f(x)-L|<\varepsilon\bigr).}
$$

Si $a\in\operatorname{Acc}(D_a^+)$, la caracterización derecha es

$$
\boxed{\lim_{\substack{x\to a^+\\x\in D}}f(x)=L
\iff\forall\varepsilon>0\ \exists\delta>0\ \forall x\in D:\
\bigl(0<x-a<\delta\Rightarrow |f(x)-L|<\varepsilon\bigr).}
$$

En cada caso, cuando existe, el límite lateral es único.

**Demostración.**
Para $x\in D$, la desigualdad $0<a-x<\delta$ equivale a $x<a$ y $0<|x-a|<\delta$: si $x<a$, entonces $|x-a|=a-x$. Así, cuantificar sobre $x\in D$ bajo $0<a-x<\delta$ equivale exactamente a cuantificar sobre $x\in D_a^-$ bajo la condición perforada de Definición §16.1.2 — Límite real finito de una función relativo a su dominio. En $D_a^-$ la restricción coincide punto por punto con $f$, y la hipótesis de acumulación garantiza que la notación del límite no es vacua. Esto prueba la equivalencia izquierda. Para la derecha usamos $|x-a|=x-a$ cuando $x>a$ y repetimos las dos implicaciones. La unicidad se deduce aplicando Teorema §16.1.4 — Unicidad del límite finito a cada función restringida sobre su dominio lateral, cuya acumulación se exigió expresamente. ∎

La escritura $x\to a^-$ no indica una sucesión particular. El criterio contiene un cuantificador universal sobre todos los argumentos admisibles del lado respectivo y no invoca la recíproca secuencial condicional de §16.2.


### Teorema 16.5.5 — Reconstrucción bilateral cuando ambos lados acumulan
Sean $f:D\to\mathbb R$, $a,L\in\mathbb R$ y supongamos

$$
a\in\operatorname{Acc}(D_a^-)
\quad\text{y}\quad
a\in\operatorname{Acc}(D_a^+).
$$

Entonces las condiciones siguientes son equivalentes:

$$
\boxed{\lim_{\substack{x\to a\\x\in D}}f(x)=L}
$$

y

$$
\boxed{\lim_{\substack{x\to a^-\\x\in D}}f(x)=L
\quad\text{y}\quad
\lim_{\substack{x\to a^+\\x\in D}}f(x)=L.}
$$

**Demostración.**
La acumulación bilateral requerida para hablar del límite ordinario se sigue de cualquiera de las dos hipótesis por Lema §16.5.2 — La acumulación procede de al menos un lado.

**Bilateral $\Rightarrow$ laterales.** Supongamos que el límite bilateral es $L$ y fijemos $\varepsilon>0$. Sea $\delta>0$ un radio que controla todos los $x\in D$ con $0<|x-a|<\delta$. Toda entrada que cumpla $0<a-x<\delta$ es uno de esos puntos; por tanto satisface $|f(x)-L|<\varepsilon$. El mismo argumento se aplica a $0<x-a<\delta$. Por las caracterizaciones de Proposición §16.5.4 — Caracterizaciones unilaterales $\varepsilon$–$\delta$, ambos límites laterales valen $L$.

**Laterales $\Rightarrow$ bilateral.** Supongamos ambos límites laterales iguales a $L$ y fijemos $\varepsilon>0$. Obtenemos radios $\delta_->0$ y $\delta_+>0$ correspondientes a las dos caracterizaciones. Tomemos $\delta:=\min\{\delta_-,\delta_+\}>0$. Si $x\in D$ y $0<|x-a|<\delta$, entonces $x\ne a$ y se cumple exactamente una alternativa. Si $x<a$, tenemos $0<a-x<\delta_-$ y la estimación izquierda da $|f(x)-L|<\varepsilon$. Si $x>a$, se aplica la derecha. Como el punto $x$ fue arbitrario, la misma $\delta$ verifica la definición bilateral. ∎

> **Consecuencia inmediata.** Si existen ambos límites laterales pero sus valores son distintos, el límite bilateral no existe: de existir, el teorema lo identificaría con cada uno y la unicidad lateral obligaría a que coincidieran.


### Teorema 16.5.6 — Criterio completo para dominios de uno o dos lados
Sean $f:D\to\mathbb R$, $a\in\operatorname{Acc}(D)$ y $L\in\mathbb R$. El límite bilateral de $f$ en $a$ vale $L$ si y sólo si cada lado que efectivamente acumula en $a$ tiene límite lateral $L$. De manera exhaustiva, distinguimos tres casos; cada expresión de límite lateral se escribe únicamente bajo la hipótesis de acumulación del lado correspondiente:

$$
\begin{aligned}
&\text{Si ambos lados acumulan:} &&
\lim_{\substack{x\to a\\x\in D}}f(x)=L
\iff
\left(\lim_{\substack{x\to a^-\\x\in D}}f(x)=L
\;\land\;
\lim_{\substack{x\to a^+\\x\in D}}f(x)=L\right);\\[4pt]
&\text{Si sólo acumula el izquierdo:} &&
\lim_{\substack{x\to a\\x\in D}}f(x)=L
\iff \lim_{\substack{x\to a^-\\x\in D}}f(x)=L;\\[4pt]
&\text{Si sólo acumula el derecho:} &&
\lim_{\substack{x\to a\\x\in D}}f(x)=L
\iff \lim_{\substack{x\to a^+\\x\in D}}f(x)=L.
\end{aligned}
$$

No hay un cuarto caso: Lema §16.5.2 — La acumulación procede de al menos un lado asegura que al menos uno de los lados acumula. Esta presentación por casos evita incluir en una fórmula una expresión de límite lateral cuyo dominio no acumula y para la cual la notación aún no está definida.

**Demostración.**
Si el límite bilateral vale $L$, el argumento de restricción empleado en Teorema §16.5.5 — Reconstrucción bilateral cuando ambos lados acumulan da el límite $L$ en cualquier lado que acumule; no se intenta definir límite en los otros lados.

Recíprocamente, supongamos la condición derecha. Según Lema §16.5.2 — La acumulación procede de al menos un lado existe al menos un lado activo. Si ambos acumulan, Teorema §16.5.5 — Reconstrucción bilateral cuando ambos lados acumulan concluye inmediatamente. Supongamos entonces que el izquierdo acumula y el derecho no. Dado $\varepsilon>0$, el límite izquierdo suministra $\delta_->0$ tal que $0<a-x<\delta_-$, con $x\in D$, implica $|f(x)-L|<\varepsilon$. Como $a\notin\operatorname{Acc}(D_a^+)$, la negación clásica de Lema §16.1.1 — Acumulación y aproximación perforada da $r_+>0$ tal que no hay $x\in D_a^+$ con $0<|x-a|<r_+$. Definamos $\delta:=\min\{\delta_-,r_+\}>0$. Para cualquier $x\in D$ con $0<|x-a|<\delta$, la alternativa $x>a$ contradiría la exclusión de puntos derechos. Luego $x<a$ y se aplica la estimación izquierda. Esto demuestra el límite bilateral $L$. Si sólo acumula el lado derecho, intercambiamos $+$ y $-$ y repetimos el argumento con su radio de exclusión izquierdo. Ninguna demostración selecciona puntos de infinitas vecindades: sólo requiere elegir un número finito de radios y tomar su mínimo. ∎

**Advertencia sobre el lenguaje.** «Límite bilateral» aquí designa el límite definido en §16.1 sobre todo el dominio, incluso si el dominio sólo posee puntos próximos por un lado. No debe inferirse que el calificativo implique, como hipótesis adicional, presencia de puntos por ambos lados. El teorema muestra exactamente cuándo es legítimo hablar del límite de $f$ en el sentido ya definido.


### Corolario 16.5.7 — Funciones dadas por dos ramas y límites laterales incompatibles
Sea $f:D\to\mathbb R$ y sea $a$ un punto de acumulación de ambos dominios laterales. Supongamos que los límites de las dos restricciones existen, con valores $L_-$ y $L_+$, respectivamente. Entonces

$$
\boxed{\text{$f$ tiene límite finito en $a$}
\iff L_-=L_+.}
$$

Cuando coinciden, el límite común es el bilateral. Esta afirmación vale aunque $a\notin D$ y, cuando $a\in D$, independientemente de $f(a)$.

**Demostración.**
Si existe un límite bilateral $L$, Teorema §16.5.5 — Reconstrucción bilateral cuando ambos lados acumulan proporciona los dos límites laterales iguales a $L$. La unicidad lateral de Proposición §16.5.4 — Caracterizaciones unilaterales $\varepsilon$–$\delta$ implica $L_-=L=L_+$. Inversamente, si $L_-=L_+=L$, aplicamos la otra implicación de Teorema §16.5.5 — Reconstrucción bilateral cuando ambos lados acumulan y obtenemos el límite bilateral $L$. Todas las desigualdades definitorias son perforadas y, por Proposición §16.1.5 — Carácter local del límite y libertad en el valor puntual, un cambio exclusivamente en $f(a)$ no altera la conclusión. ∎

**Ejemplo: dos ramas incompatibles.** En $D=\mathbb R$, definamos

$$
f(x)=\begin{cases}
0,&x<0,\\
2,&x\ge0.
\end{cases}
$$

El punto $0$ es de acumulación de $D_0^-$ y $D_0^+$: dado $r>0$, los puntos $-r/2$ y $r/2$, considerados cada uno para ese radio concreto, son testigos. Para toda tolerancia $\varepsilon>0$, el lado izquierdo satisface $|f(x)-0|=0<\varepsilon$ y el derecho $|f(x)-2|=0<\varepsilon$; puede tomarse $\delta=1$ en cada caso. Así,

$$
\lim_{x\to0^-}f(x)=0,
\qquad \lim_{x\to0^+}f(x)=2.
$$

Como $0\ne2$, el límite bilateral no existe. Modificar $f(0)$ no puede resolverlo: el obstáculo está en las dos ramas perforadas y no en el valor central. No hemos definido todavía «continuidad» ni una clasificación general de sus discontinuidades; esas nociones quedan para el Capítulo 17.


Hemos distinguido formalmente las dos direcciones del orden, exigido acumulación antes de definir cada límite lateral y determinado cómo recomponer el límite sobre cualquier dominio. La siguiente sección, §16.6, tratará límites infinitos y límites cuando el argumento crece sin cota, mediante relaciones cuantificadas y conjuntos de aproximación explícitos, sin añadir $+\infty$ ni $-\infty$ como elementos ordinarios de $\mathbb R$ ni anticipar continuidad.
