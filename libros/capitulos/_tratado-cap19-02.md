## 19.2. La derivabilidad implica continuidad {#sec-ta-19-2}

La derivada mide un cociente de incrementos. La continuidad sólo exige que el incremento de la función se haga pequeño. El puente entre ambas propiedades será la identidad

$$
f(x)-f(a)=q_{f,a}(x)(x-a),\qquad x\in D_a.
$$

La igualdad no se utilizará en $x=a$, donde el cociente no está definido. En el centro, la continuidad se comprobará separadamente mediante $f(a)-f(a)=0$. Además de demostrar la implicación, identificaremos una estimación cuantitativa y mostraremos que su recíproca es falsa.

### Teorema 19.2.1 — Toda función derivable en un punto es continua en él
Sean $D\subseteq\mathbb R$, $f:D\to\mathbb R$ y $a\in D\cap\operatorname{Acc}(D)$. Si $f$ es derivable en $a$ relativamente a $D$, entonces es continua en $a$ relativamente al mismo dominio:

$$
\boxed{f\text{ derivable en }a\quad\Longrightarrow\quad f\text{ continua en }a.}
$$

**Demostración.**
Sea $L:=f'(a)$. Por la definición de derivada, $q_{f,a}:D_a\to\mathbb R$ converge a $L$ cuando $x\to a$ por $D_a$. Apliquemos la definición del límite a la única tolerancia $1>0$. Existe $r>0$ tal que, para todo $x\in D$,

$$
0<|x-a|<r\quad\Longrightarrow\quad |q_{f,a}(x)-L|<1.
$$

Por la desigualdad triangular, en esos mismos argumentos

$$
|q_{f,a}(x)|\le |q_{f,a}(x)-L|+|L|<|L|+1.
$$

Pongamos $C:=|L|+1>0$. Para todo $x\in D$ con $0<|x-a|<r$, la identidad del cociente incremental, válida porque $x-a\ne0$, da

$$
\begin{aligned}
|f(x)-f(a)|
&=|q_{f,a}(x)(x-a)|\\
&=|q_{f,a}(x)|\,|x-a|\\
&<C|x-a|.
\end{aligned}
$$

Fijemos ahora una tolerancia arbitraria $\varepsilon>0$. Los números $r$ y $\varepsilon/C$ son positivos, por lo que podemos definir $\delta:=\min\{r,\varepsilon/C\}>0$ (mínimo de dos números determinados). Sea $x\in D$ tal que $|x-a|<\delta$. Si $x\ne a$, entonces $0<|x-a|<r$ y

$$
|f(x)-f(a)|<C|x-a|<C\delta\le\varepsilon.
$$

Si $x=a$, se tiene directamente $|f(a)-f(a)|=0<\varepsilon$. Por tanto, el mismo $\delta$ sirve para todos los puntos de $D$ comprendidos en la bola de radio $\delta$. Ésta es exactamente la continuidad relativa de Definición §17.1.1 — Continuidad relativa al dominio en un punto. La prueba no escoge puntos del dominio, no invoca teoremas globales y no altera el codominio de $f$. $\square$

**Lectura de la prueba.** La existencia de un límite finito para las pendientes obliga a que éstas estén acotadas cerca del punto. Multiplicar esa cota por el incremento $|x-a|$, que puede hacerse arbitrariamente pequeño, controla el cambio de los valores de $f$. El carácter perforado del cociente y el carácter no perforado de la continuidad quedan conciliados al verificar aparte $x=a$.

### Corolario 19.2.2 — Control lineal local respecto del centro
Bajo las hipótesis del teorema, existen números $r>0$ y $C>0$ tales que

$$
\boxed{\forall x\in D:\quad |x-a|<r\ \Longrightarrow\
|f(x)-f(a)|\le C|x-a|.}
$$

En particular, puede tomarse $C=|f'(a)|+1$. Esta desigualdad controla la variación respecto del punto fijo $a$; no afirma todavía que $|f(x)-f(y)|\le C|x-y|$ para cualesquiera dos puntos próximos $x,y$.

**Demostración.**
Tomemos $L=f'(a)$ y apliquemos la condición de derivabilidad con tolerancia $1$. Existe $r>0$ tal que $0<|x-a|<r$ implica $|q_{f,a}(x)-L|<1$. La desigualdad triangular proporciona $|q_{f,a}(x)|<|L|+1=C$, de modo que $|f(x)-f(a)|<C|x-a|$ cuando $x\ne a$. Para $x=a$, ambos miembros de la desigualdad no estricta son cero. Así, un mismo $r$ y un mismo $C$ funcionan para todos los puntos indicados, sin seleccionar radios para una familia de centros. $\square$

### Proposición 19.2.3 — La continuidad no implica derivabilidad
La función $g:\mathbb R\to\mathbb R$ definida por $g(x)=|x|$ es continua en todo punto de $\mathbb R$, pero no es derivable en $0$.

**Demostración.**
El valor absoluto determina una función tipada $g:\mathbb R\to\mathbb R$ por Separación en $\mathbb R\times\mathbb R$. Para cualesquiera $x,y\in\mathbb R$, la desigualdad triangular inversa Corolario §4.2.4 — Desigualdad triangular inversa da

$$
\bigl||x|-|y|\bigr|\le |x-y|.
$$

Dado $a\in\mathbb R$ y $\varepsilon>0$, el radio $\delta=\varepsilon$ prueba que $|x-a|<\delta$ implica $|g(x)-g(a)|\le|x-a|<\varepsilon$. Luego $g$ es continua en todos los puntos, en particular en $0$.

Además, $0\in\operatorname{Acc}(\mathbb R)$: para cada $r>0$, $r/2\in\mathbb R$ cumple $0<|r/2|<r$. Supongamos, para obtener una contradicción, que $g$ fuera derivable en $0$, con derivada $L\in\mathbb R$. Al aplicar Definición §19.1.3 — Derivabilidad en un punto con $\varepsilon=1/2$, habría un $\delta>0$ tal que

$$
0<|x|<\delta\quad\Longrightarrow\quad
\left|\frac{|x|-|0|}{x}-L\right|<\frac12.
$$

Tomemos los dos puntos explícitos $x_+:=\delta/2>0$ y $x_-:=-\delta/2<0$. Ambos pertenecen al dominio perforado y satisfacen $0<|x_\pm|<\delta$; sus pendientes secantes valen, respectivamente,

$$
q_{g,0}(x_+)=1,\qquad q_{g,0}(x_-)=-1.
$$

Por tanto $|1-L|<1/2$ y $|-1-L|<1/2$. La desigualdad triangular produciría

$$
2=|1-(-1)|\le|1-L|+|L-(-1)|<1,
$$

contradicción. Así, $g'(0)$ no está definido. Se han construido dos testigos a partir de un solo radio; no se han escogido sucesiones de aproximantes ni se han presupuestado derivadas laterales todavía no definidas. $\square$

**Interpretación.** La continuidad permite cambios que se anulan al acercarnos al punto, pero no impone una única pendiente límite. En $g(x)=|x|$, las pendientes secantes calculadas desde argumentos positivos y negativos son incompatibles. La implicación demostrada en el teorema es estricta.

**Transición.** La estimación del error de §19.1.4 permite ahora una descripción más precisa: una derivada existente es el coeficiente de una aproximación afín cuyo error es pequeño en comparación con $|x-a|$. Éste será el contenido de §19.3, antes de formular las reglas de derivación.
