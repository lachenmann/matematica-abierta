## 19.6. La regla de la cadena: composición y anulación de incrementos interiores {#sec-ta-19-6}

Las reglas precedentes operan con funciones que comparten argumento. En una composición, la variación pasa por un valor intermedio: primero cambia $g(x)$ y después cambia $f(g(x))$. La expresión habitual

$$
\frac{f(g(x))-f(g(a))}{x-a}
=\frac{f(g(x))-f(g(a))}{g(x)-g(a)}
 \frac{g(x)-g(a)}{x-a}
$$

**no es una identidad universal**: el primer factor no está definido si $g(x)=g(a)$, aunque $x\ne a$. El problema puede aparecer en puntos arbitrariamente próximos a $a$, incluso cuando ambas funciones son derivables. Construiremos un factor exterior con valor definido en el centro para demostrar una identidad legítima en todo el dominio perforado.

La composición conserva además un **dominio efectivo**, ya construido en Proposición §16.4.1 — Dominio efectivo y tipado de la composición y reutilizado en Teorema §17.4.5 — Composición en el dominio efectivo. Para $g:D\to\mathbb R$ y $f:E\to\mathbb R$, con $D,E\subseteq\mathbb R$, dicho dominio es

$$
T:=g^{-1}[E]=\{x\in D:g(x)\in E\}.
$$

El cambio explícito de codominio de $g\upharpoonright T$ a $E$ produce $g_T:T\to E$; la composición tipada es $h:=f\circ g_T:T\to\mathbb R$. En general, $a\in\operatorname{Acc}(D)$ y $g(a)\in\operatorname{Acc}(E)$ **no implican** $a\in\operatorname{Acc}(T)$, de modo que esta última condición deberá constar en el teorema.

### Lema 19.6.1 — Extensión continua del cociente incremental exterior
Sean $E\subseteq\mathbb R$, $f:E\to\mathbb R$ y $b\in E\cap\operatorname{Acc}(E)$. Si $f$ es derivable en $b$, existe una función $A_{f,b}:E\to\mathbb R$, determinada de manera única por

$$
\boxed{A_{f,b}(y):=
\begin{cases}
\dfrac{f(y)-f(b)}{y-b},&y\ne b,\\[5pt]
f'(b),&y=b,
\end{cases}}
$$

que es continua en $b$ relativamente a $E$ y satisface, **para todo** $y\in E$,

$$
\boxed{f(y)-f(b)=A_{f,b}(y)(y-b),\qquad A_{f,b}(b)=f'(b).}
$$

**Demostración.**
Fijemos $L:=f'(b)$. El grafo de $A_{f,b}$ se obtiene por Separación en $E\times\mathbb R$: un par $\langle y,z\rangle$ pertenece a él cuando $(y\ne b\land (y-b)z=f(y)-f(b))$ o $(y=b\land z=L)$. Para $y\ne b$ existe exactamente un $z$, porque $y-b$ es invertible; para $y=b$ existe exactamente $z=L$. Las alternativas son disjuntas y cubren $E$, luego el grafo determina una función con los tipos indicados. No se selecciona ningún representante ni se asigna un cociente a una división por cero.

Para $y\ne b$, la identidad del recuadro sigue multiplicando la definición por $y-b$. En $y=b$, ambos lados son cero; por tanto, la identidad vale también allí sin realizar esa división.

Resta comprobar continuidad. Fijemos $\varepsilon>0$. Por la definición de $f'(b)$ existe $\eta>0$ tal que, para todo $y\in E$ con $0<|y-b|<\eta$,

$$
\left|\frac{f(y)-f(b)}{y-b}-L\right|<\varepsilon.
$$

Si $y\in E$ y $|y-b|<\eta$, cuando $y\ne b$ esta desigualdad es precisamente $|A_{f,b}(y)-A_{f,b}(b)|<\varepsilon$; cuando $y=b$, la diferencia vale cero y también es menor que $\varepsilon$. El mismo radio sirve en ambos casos, de modo que $A_{f,b}$ es continua en $b$ relativamente a $E$. Sólo se ha usado una instancia de la condición de derivabilidad para cada tolerancia, sin ningún axioma de elección. $\square$

**Lectura de la construcción.** $A_{f,b}$ no es una nueva derivada ni convierte automáticamente al cociente incremental original en una función definida en $b$. Es **otra función**, cuyo valor central se ha establecido mediante la derivada ya existente. La igualdad de incrementos es válida aun cuando el incremento $y-b$ sea nulo.

### Teorema 19.6.2 — Regla de la cadena en el dominio efectivo
Sean $D,E\subseteq\mathbb R$, $g:D\to\mathbb R$ y $f:E\to\mathbb R$. Fijemos

$$
T:=\{x\in D:g(x)\in E\},\qquad g_T:T\to E,\qquad h:=f\circ g_T:T\to\mathbb R,
$$

con el cambio de codominio y la composición exactamente como en Proposición §16.4.1 — Dominio efectivo y tipado de la composición. Supongamos que

1. $a\in T\cap\operatorname{Acc}(T)$ y $g$ es derivable en $a$ relativamente a $D$;
2. $b:=g(a)\in E\cap\operatorname{Acc}(E)$ y $f$ es derivable en $b$ relativamente a $E$.

Entonces $h$ es derivable en $a$ **relativamente a $T$** y

$$
\boxed{h'(a)=f'(g(a))\,g'(a).}
$$

No se supone que $g(x)\ne g(a)$ para $x\ne a$, que $g'(a)$ sea distinto de cero, que $T$ sea abierto, ni que $g[T]$ contenga una vecindad de $b$.

**Demostración.**
**1. Existencia y dominios.** Por Proposición §16.4.1 — Dominio efectivo y tipado de la composición, $T$ es un conjunto, $g_T:T\to E$ es una función y $h=f\circ g_T:T\to\mathbb R$ está bien definida, con $h(x)=f(g(x))$ para todo $x\in T$. La hipótesis $a\in T\cap\operatorname{Acc}(T)$ garantiza que existe el dominio perforado necesario para el límite de $h$; como $T\subseteq D$, también $a\in\operatorname{Acc}(D)$. La proposición Proposición §19.5.2 — Restricción de una función derivable conserva, al restringir $g$ a $T$ con codominio $\mathbb R$, la derivada $g'(a)$. El mero cambio posterior del codominio a $E$ no altera ninguno de sus valores.

**2. Identidad que no divide por el incremento interior.** Sean $L:=f'(b)$ y $M:=g'(a)$. El lema anterior proporciona $A:=A_{f,b}:E\to\mathbb R$, continua en $b$, tal que $f(y)-f(b)=A(y)(y-b)$ para todo $y\in E$. Por consiguiente, para cada $x\in T\setminus\{a\}$,

$$
\begin{aligned}
q_{h,a}(x)
&=\frac{f(g(x))-f(b)}{x-a}\\
&=A(g(x))\frac{g(x)-g(a)}{x-a}\\
&=A(g(x))q_{g,a}(x).
\end{aligned}
$$

Sólo se divide por $x-a\ne0$. **Si $g(x)=g(a)=b$,** el incremento de $h$ es cero, $A(g(x))=L$ y $q_{g,a}(x)=0$; la identidad sigue siendo verdadera. En ningún momento se introduce el cociente $[f(g(x))-f(b)]/[g(x)-b]$ en tales puntos.

**3. Paso al límite con radios explícitos.** La derivabilidad de $g$ implica su continuidad en $a$ (Teorema §19.2.1 — Toda función derivable en un punto es continua en él). Fijemos $\varepsilon>0$ y pongamos $C:=|M|+1>0$. Como $A$ es continua en $b$, existe $\eta>0$ tal que

$$
\forall y\in E:\quad |y-b|<\eta\Longrightarrow
|A(y)-L|<\frac{\varepsilon}{2C}.
$$

Por continuidad de $g$ en $a$, existe $\delta_g>0$ tal que $x\in D$ y $|x-a|<\delta_g$ implican $|g(x)-b|<\eta$. Por derivabilidad de $g$, apliquemos la condición del cociente incremental a la tolerancia positiva

$$
\theta:=\min\left\{1,\frac{\varepsilon}{2(|L|+1)}\right\}>0.
$$

Obtenemos $\delta_q>0$ tal que $x\in D$ y $0<|x-a|<\delta_q$ implican $|q_{g,a}(x)-M|<\theta$. El número $\delta:=\min\{\delta_g,\delta_q\}$ es positivo y requiere únicamente un mínimo finito.

Para todo $x\in T$ con $0<|x-a|<\delta$ tenemos $g(x)\in E$, $|g(x)-b|<\eta$, $|q_{g,a}(x)-M|<1$ y, por desigualdad triangular, $|q_{g,a}(x)|<C$. Utilizando la identidad del paso 2,

$$
\begin{aligned}
|q_{h,a}(x)-LM|
&=|[A(g(x))-L]q_{g,a}(x)+L[q_{g,a}(x)-M]|\\
&\le |A(g(x))-L|\,|q_{g,a}(x)|
       +|L|\,|q_{g,a}(x)-M|\\
&<\frac{\varepsilon}{2C}C
  +\frac{|L|\varepsilon}{2(|L|+1)}
<\varepsilon.
\end{aligned}
$$

La última desigualdad incluye $L=0$. Hemos demostrado que $q_{h,a}$ tiende a $LM$ sobre $T\setminus\{a\}$; la hipótesis de acumulación hace que este límite no sea vacuo, y Proposición §19.1.4 — Unicidad y criterio cuantificado de la derivada identifica su único valor con $h'(a)$. Los radios $\eta,\delta_g,\delta_q$ se obtienen mediante una **cadena finita de instancias existenciales**, no mediante una función de elección. No se usan límites secuenciales ni teoremas del valor medio. $\square$

**Alcance exacto.** El resultado no pretende que la función $g_T:T\to E$ sea literalmente la misma función que $g:D\to\mathbb R$: sus dominios o codominios pueden diferir. La derivada de $g$ aparece legítimamente porque restringimos sus valores a un dominio donde la acumulación está garantizada y empleamos esos mismos valores en la identidad anterior.

### Corolario 19.6.3 — Composición con imagen interior contenida en el dominio exterior
Sean $g:D\to\mathbb R$ y $f:E\to\mathbb R$, con $g[D]\subseteq E$. Si $a\in D\cap\operatorname{Acc}(D)$, $g$ es derivable en $a$ y $f$ es derivable en $b=g(a)$ relativamente a $E$, entonces la composición tipada $h:D\to\mathbb R$, obtenida cambiando el codominio de $g$ a $E$ antes de componer, es derivable en $a$ y

$$
\boxed{(f\circ g_E)'(a)=f'(g(a))g'(a),\qquad g_E:D\to E.}
$$

**Demostración.**
Por $g[D]\subseteq E$, todo $x\in D$ pertenece al conjunto efectivo $T=\{x\in D:g(x)\in E\}$ y la inclusión opuesta es inmediata: $T=D$. En particular, $a\in T\cap\operatorname{Acc}(T)$. La función $g_T$ de Proposición §16.4.1 — Dominio efectivo y tipado de la composición tiene ahora dominio $D$, codominio $E$ y los valores de $g$; llamémosla $g_E$. Las demás hipótesis son exactamente las del teorema anterior, cuya aplicación da la afirmación. No se ha identificado $g_E$ con $g$ como objetos tipados. $\square$

### Proposición 19.6.4 — La acumulación del dominio efectivo no se hereda automáticamente
Es posible que $g:D\to\mathbb R$ sea derivable en $a$, que $f:E\to\mathbb R$ sea derivable en $g(a)$ y que ambos centros sean puntos de acumulación de sus dominios, pero que la composición efectiva tenga **un punto aislado** en $a$ y, por definición, no sea derivable allí.

**Demostración.**
Tomemos $D=\mathbb R$, $E=\{y\in\mathbb R:y\le0\}$, $a=0$, y las funciones $g:D\to\mathbb R$, $g(x)=x^2$, y $f:E\to\mathbb R$, $f(y)=y$. El punto $0$ acumula $D$, pues $r/2\in D\setminus\{0\}$ pertenece a toda bola de radio $r>0$ suficientemente indicada por esa fórmula. También acumula $E$: el punto $-r/2\in E\setminus\{0\}$ cumple $|-r/2|<r$. Por Proposición §19.1.6 — Primeros cálculos: funciones afines y función cuadrática, $g$ es derivable en $0$, con $g'(0)=0$. La identidad $\mathbb R\to\mathbb R$ es derivable en $0$ con derivada $1$ y, por Proposición §19.5.2 — Restricción de una función derivable, también lo es su restricción $f:E\to\mathbb R$, con $f'(0)=1$.

Sin embargo, $g(x)=x^2\ge0$ para todo real $x$, y $x^2=0$ equivale a $x=0$ por las propiedades del cuerpo ordenado. En consecuencia,

$$
T=\{x\in\mathbb R:g(x)\in E\}
 =\{x\in\mathbb R:x^2\le0\}=\{0\}.
$$

La composición $h:T\to\mathbb R$ existe y satisface $h(0)=0$, pero $0\notin\operatorname{Acc}(T)$: ninguna bola perforada contiene puntos del singleton. Por Definición §19.1.3 — Derivabilidad en un punto, $h'(0)$ **no está definida**, aunque las dos derivadas de entrada existan. La condición de acumulación efectiva del teorema no puede suprimirse sin modificar nuestra definición de derivada. $\square$

### Corolario 19.6.5 — Derivada de una composición racional cuadrática
La función $h:\mathbb R\to\mathbb R$ definida por

$$
\boxed{h(x)=\frac{1}{x^2+1}}
$$

está bien definida y es derivable en todo $a\in\mathbb R$, con

$$
\boxed{h'(a)=-\frac{2a}{(a^2+1)^2}.}
$$

**Demostración.**
La función interior $g:\mathbb R\to\mathbb R$, $g(x)=x^2+1$, se obtiene sumando las funciones cuadrática y constante sobre $\mathbb R$; por Proposición §19.1.6 — Primeros cálculos: funciones afines y función cuadrática y Teorema §19.4.1 — Regla de derivación de la suma es derivable en cada $a$, con $g'(a)=2a+0=2a$. Como $x^2\ge0$ en un cuerpo ordenado, $g(x)\ge1>0$ para todo $x$, y por tanto $g[\mathbb R]\subseteq E:=\mathbb R\setminus\{0\}$.

Tomemos la función exterior $f:E\to\mathbb R$, $f(y)=1/y$. Su derivabilidad en cada $y\in E$ y la fórmula $f'(y)=-1/y^2$ se demostraron en Corolario §19.5.5 — Funciones fraccionarias afines y ceros excluidos. Además, cada $b\in E$ es de acumulación de $E$: tomando $r>0$, sirve $b+\min\{r/2,|b|/2\}$ si $b>0$, y $b-\min\{r/2,|b|/2\}$ si $b<0$; ambos son distintos de $b$, están en $E$ y distan de $b$ menos que $r$. Por la inclusión de imágenes, el dominio efectivo de la composición es toda $\mathbb R$; aplicamos Corolario §19.6.3 — Composición con imagen interior contenida en el dominio exterior y obtenemos

$$
h'(a)=f'(g(a))g'(a)
=-\frac{1}{(a^2+1)^2}\,(2a)
=-\frac{2a}{(a^2+1)^2}.
$$

No se ha usado una regla genérica de potencias negativas ni una extensión de $1/y$ al cero; la prueba combina dos derivadas ya justificadas con una composición tipada. $\square$

**Transición.** La regla de la cadena permite relacionar una derivada con la de otra función mediante una composición. En §19.7 estudiaremos el problema inverso: si una función posee una inversa local bien definida, ¿cuándo puede derivarse ésta? Antes de dividir por $f'(a)$ comprobaremos su no nulidad y la acumulación del dominio de la inversa; no invocaremos Rolle ni el teorema del valor medio.
