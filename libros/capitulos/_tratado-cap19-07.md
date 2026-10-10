## 19.7. La derivada de la función inversa {#sec-ta-19-7}

La regla de la cadena relaciona la derivada de una composición con las de sus factores. Si una función inyectiva admite inversa, cabría esperar que la derivada de esta última fuera el recíproco de la derivada original. Pero la identidad formal $f(g(y))=y$ no autoriza, por sí sola, a derivar $g$: primero debemos justificar que la inversa existe con tipos precisos, que su dominio acumula en el punto de interés y que es continua allí. Una derivada no nula controla las pendientes *cerca de su propio centro*; en dominios arbitrarios no impide que puntos muy alejados tengan imágenes próximas al valor central.

Presentaremos primero el teorema local con la continuidad de la inversa como hipótesis explícita. Después demostraremos que dicha hipótesis se obtiene automáticamente para una función continua e inyectiva definida en un compacto, y delimitaremos con contraejemplos las condiciones empleadas. Todo el razonamiento es anterior a Rolle y al teorema del valor medio.

### Proposición 19.7.1 — Construcción tipada de la inversa y acumulación de la imagen
Sean $D\subseteq\mathbb R$ y $f:D\to\mathbb R$ inyectiva. Su imagen $E:=f[D]$ es un subconjunto de $\mathbb R$. Existe una única función $g:E\to\mathbb R$ con $g[E]\subseteq D$ y

$$
\boxed{g(f(x))=x\quad(x\in D),\qquad f(g(y))=y\quad(y\in E).}
$$

Si, además, $a\in D\cap\operatorname{Acc}(D)$ y $f$ es continua en $a$ relativamente a $D$, entonces

$$
\boxed{b:=f(a)\in E\cap\operatorname{Acc}(E).}
$$

**Demostración.**
El conjunto $E=f[D]$ existe mediante la operación de imagen ya construida. El mismo grafo de $f$, considerado con codominio $E$, determina una función $f_E:D\to E$: todo valor de $f$ pertenece a $E$ y cada $y\in E$ es imagen de algún $x\in D$. Por inyectividad, este último $x$ es único. Así, $f_E$ es biyectiva y Teorema §0.6.7 — Caracterización de las funciones invertibles proporciona una función inversa tipada $j:E\to D$.

Puesto que $D\subseteq\mathbb R$, el grafo de $j$ es también un subconjunto de $E\times\mathbb R$. Con él construimos $g:E\to\mathbb R$, que satisface $g(y)=j(y)\in D$. Por las identidades de inversa de $f_E$ obtenemos las dos igualdades del recuadro. Si $\widetilde g:E\to\mathbb R$ también toma valores en $D$ y satisface $f(\widetilde g(y))=y$, entonces, para cada $y\in E$, la inyectividad de $f$ obliga a $\widetilde g(y)=g(y)$; la igualdad de dominio, codominio y valores da $\widetilde g=g$. Es importante que $j:E\to D$ y $g:E\to\mathbb R$ no son literalmente la misma función tipada cuando $D\ne\mathbb R$, aunque sus grafos y valores coincidan.

Para la acumulación fijemos $\rho>0$. Por continuidad de $f$ en $a$ existe $\delta>0$ tal que, si $x\in D$ y $|x-a|<\delta$, entonces $|f(x)-b|<\rho$. Como $a\in\operatorname{Acc}(D)$, el criterio Lema §16.1.1 — Acumulación y aproximación perforada proporciona un $x\in D$ con $0<|x-a|<\delta$. Su imagen $y=f(x)$ pertenece a $E$, satisface $|y-b|<\rho$ y es distinta de $b=f(a)$ por inyectividad. Así $0<|y-b|<\rho$. Dado que $\rho$ era arbitrario, $b\in\operatorname{Acc}(E)$. No se ha seleccionado simultáneamente un testigo para todos los radios. $\square$

**Precisión de tipos.** En el resto de la sección, «la inversa real» designa $g:E\to\mathbb R$, mientras que $f_E^{-1}:E\to D$ es la inversa propiamente dicha de la biyección $f_E:D\to E$. Sólo la primera tiene automáticamente el codominio exigido por nuestra definición de derivada real.

### Teorema 19.7.2 — Derivación de la inversa bajo continuidad y derivada no nula
Sea $f:D\to\mathbb R$ inyectiva, con $D\subseteq\mathbb R$, y fijemos $a\in D\cap\operatorname{Acc}(D)$. Supongamos que $f$ es derivable en $a$ y que $L:=f'(a)\ne0$. Pongamos $E:=f[D]$, $b:=f(a)$ y sea $g:E\to\mathbb R$ la inversa real de la proposición anterior. Si $g$ es continua en $b$ relativamente a $E$, entonces $g$ es derivable en $b$ respecto de $E$ y

$$
\boxed{g'(b)=\frac{1}{f'(a)}.}
$$

La continuidad de $g$ es una hipótesis auténtica; no queda incorporada implícitamente en la palabra «inversa».

**Demostración.**
**1. Acumulación y valores.** Por Teorema §19.2.1 — Toda función derivable en un punto es continua en él, la derivabilidad de $f$ implica continuidad en $a$. La proposición anterior garantiza $b\in E\cap\operatorname{Acc}(E)$ y construye $g$ con $g(b)=a$ y $f(g(y))=y$ para todo $y\in E$. Por tanto el cociente incremental de $g$ está legítimamente definido en $E\setminus\{b\}$ y la derivabilidad en $b$ no será vacua.

**2. Denominador separado de cero.** Como $L\ne0$, la derivabilidad de $f$ aplicada a la tolerancia $|L|/2>0$ da $r>0$ tal que

$$
 x\in D,\quad 0<|x-a|<r
 \quad\Longrightarrow\quad |q_{f,a}(x)-L|<|L|/2.
$$

La desigualdad triangular inversa implica, en esta vecindad perforada,

$$
|q_{f,a}(x)|\ge |L|-|q_{f,a}(x)-L|>|L|/2>0.
$$

**3. Aproximación de la pendiente inversa.** Fijemos $\varepsilon>0$. Apliquemos nuevamente la derivabilidad de $f$, ahora a la tolerancia positiva $\varepsilon |L|^2/2$, y obtengamos $s>0$ tal que

$$
 x\in D,\quad 0<|x-a|<s
 \quad\Longrightarrow\quad |q_{f,a}(x)-L|<\varepsilon|L|^2/2.
$$

Definamos $t:=\min\{r,s\}>0$. La continuidad supuesta de $g$ en $b$ permite hallar $\eta>0$ tal que

$$
 y\in E,\quad |y-b|<\eta\quad\Longrightarrow\quad |g(y)-a|<t.
$$

Sea $y\in E$ con $0<|y-b|<\eta$, y pongamos $x:=g(y)$. Por construcción $x\in D$ y $f(x)=y$. Además, $x\ne a$: de lo contrario $y=f(x)=f(a)=b$. Luego $0<|x-a|<t$, de modo que las dos estimaciones anteriores se aplican a $q_{f,a}(x)$.

La identidad de las pendientes, válida porque ambos incrementos son ahora distintos de cero, es

$$
 q_{g,b}(y)=\frac{g(y)-g(b)}{y-b}
 =\frac{x-a}{f(x)-f(a)}
 =\frac1{q_{f,a}(x)}.
$$

Por consiguiente,

$$
\begin{aligned}
\left|q_{g,b}(y)-\frac1L\right|
&=\frac{|q_{f,a}(x)-L|}{|L|\,|q_{f,a}(x)|}\\
&<\frac{2}{|L|^2}\,\frac{\varepsilon|L|^2}{2}
=\varepsilon.
\end{aligned}
$$

Hemos encontrado un único $\eta>0$ para todos los $y\in E$ con $0<|y-b|<\eta$; así $q_{g,b}$ tiene límite $1/L$ y la definición Definición §19.1.3 — Derivabilidad en un punto, junto con la unicidad, concluye $g'(b)=1/L$. La prueba emplea dos radios de derivabilidad y uno de continuidad para una tolerancia fijada; no requiere elección ni teoremas globales del capítulo 20. $\square$

**Interpretación.** La pendiente de una secante inversa es el recíproco de la pendiente original sólo cuando ambos incrementos son no nulos. La inyectividad asegura esta condición para argumentos distintos del centro; la continuidad de la inversa aproxima el argumento recuperado $g(y)$ al punto $a$, y $f'(a)\ne0$ permite mantener las pendientes originales alejadas de cero.

### Proposición 19.7.3 — Una biyección continua desde un compacto tiene inversa continua
Sea $K\subseteq\mathbb R$ compacto y $f:K\to\mathbb R$ continua en todos los puntos de $K$ e inyectiva. Con $E:=f[K]$, la inversa real $g:E\to\mathbb R$ construida en §19.7.1 es continua en todos los puntos de $E$, con independencia de que $K$ sea o no un intervalo.

**Demostración.**
Si $K=\varnothing$, entonces $E=\varnothing$ y la afirmación universal sobre sus puntos es vacua. Consideremos $b\in E$. Por §19.7.1 existe un único $a:=g(b)\in K$ con $f(a)=b$. Fijemos $\varepsilon>0$ y formemos, por Separación, el conjunto

$$
F:=\{x\in K:|x-a|\ge\varepsilon\}
  =K\setminus B_{\varepsilon}(a).
$$

Es cerrado relativo en $K$ porque $B_{\varepsilon}(a)\cap K$ es abierto relativo. Como $K$ es compacto, Proposición §18.2.2 — Un cerrado relativo de un compacto es compacto prueba que $F$ es compacto. La restricción de $f$ a $F$ es continua; Teorema §18.5.1 — La imagen continua de un compacto es compacta demuestra que $f[F]$ es compacto en $\mathbb R$, y Proposición §18.3.3 — Todo compacto de la recta es cerrado, que es cerrado. La inyectividad de $f$ y $a\notin F$ implican $b=f(a)\notin f[F]$, aun cuando $F$ sea vacío.

Por tanto, el complemento abierto $\mathbb R\setminus f[F]$ contiene $b$. Existe $\eta>0$ tal que

$$
 B_{\eta}(b)\cap f[F]=\varnothing.
$$

Si $y\in E$ satisface $|y-b|<\eta$, entonces $x:=g(y)\in K$ y $f(x)=y$. No puede ocurrir $x\in F$, pues ello implicaría $y\in f[F]\cap B_{\eta}(b)$. En consecuencia $|g(y)-g(b)|=|x-a|<\varepsilon$, que es la continuidad de $g$ en $b$ relativamente a $E$. Se utiliza un solo conjunto $F$ asociado a la tolerancia y no se eligen preimágenes: la inyectividad ya determina cada una de ellas de forma única. $\square$

### Corolario 19.7.4 — Derivada de la inversa sobre un compacto
Sea $K\subseteq\mathbb R$ compacto y $f:K\to\mathbb R$ continua e inyectiva. Si $a\in K\cap\operatorname{Acc}(K)$, $f$ es derivable en $a$ relativamente a $K$ y $f'(a)\ne0$, entonces la inversa real $g:f[K]\to\mathbb R$ es derivable en $b=f(a)$ y

$$
\boxed{g'(f(a))=\frac1{f'(a)}.}
$$

**Demostración.**
La proposición §19.7.1 construye $g$ y demuestra que $b$ acumula $f[K]$, utilizando la continuidad de $f$, su inyectividad y la acumulación de $K$ en $a$. La proposición anterior asegura que $g$ es continua en $b$. Todas las hipótesis de Teorema §19.7.2 — Derivación de la inversa bajo continuidad y derivada no nula están satisfechas, incluida $f'(a)\ne0$; aplicar ese teorema produce la fórmula. No se supone que $K$ sea un intervalo ni que el teorema del valor medio esté disponible. $\square$

### Proposición 19.7.5 — Necesidad de las hipótesis: dos contraejemplos
Las siguientes afirmaciones son falsas si se omiten sus respectivas hipótesis: (i) una función inyectiva y derivable con derivada no nula tiene necesariamente inversa continua en el valor correspondiente, cuando su dominio es arbitrario; (ii) la inversa continua de una función derivable sobre un compacto es necesariamente derivable si se permite $f'(a)=0$.

**Demostración.**
**(i) Derivada no nula sin continuidad de la inversa.** Para $n\in\mathbb N$ escribamos $m_n:=\nu_{\mathbb R}(n+2_{\mathbb N})\ge2$; el símbolo $\nu_{\mathbb R}$ es la aplicación canónica de numerales, no una identificación conjuntista de naturales y reales. Formemos los conjuntos

$$
A:=\{x\in\mathbb R:\exists n\in\mathbb N,\ x=m_n^{-1}\},\qquad
B:=\{x\in\mathbb R:\exists n\in\mathbb N,\ x=m_n\},\qquad
D:=\{0\}\cup A\cup B.
$$

Se tiene $A\subset(0,1)$ y $B\subset[2,\infty)$, de modo que estas partes y $\{0\}$ son disjuntas. Construyamos por Separación la función $f:D\to\mathbb R$ con valores

$$
f(0)=0,\qquad f(x)=x\ (x\in A),\qquad
f(x)=-x^{-1}\ (x\in B).
$$

Las aplicaciones $n\mapsto m_n$ y $n\mapsto m_n^{-1}$ son inyectivas por la inyectividad de los numerales y del recíproco en números no nulos. Los valores de las tres ramas son respectivamente cero, positivos y negativos; por tanto $f$ es inyectiva. La propiedad arquimediana Teorema §4.6.3 — Todo cuerpo ordenado completo es arquimediano asegura que los recíprocos $m_n^{-1}$ pueden hacerse menores que cualquier radio positivo: para cada $r>0$ existe $n$ con $0<m_n^{-1}<r$. Así $0\in\operatorname{Acc}(D)$.

Cuando $x\in D$ y $0<|x|<1$, necesariamente $x\in A$ y $f(x)=x$; en consecuencia $q_{f,0}(x)=1$ para esos argumentos. El radio $\delta=1$ sirve para toda tolerancia, luego $f'(0)=1\ne0$. Sin embargo, $E=f[D]$ contiene $-m_n^{-1}$ para todos los $n$, y su inversa real satisface

$$
 g(-m_n^{-1})=m_n\ge2,
 \qquad g(0)=0.
$$

Para cualquier $\eta>0$ existe $n$ con $|-m_n^{-1}|<\eta$, mientras $|g(-m_n^{-1})-g(0)|\ge2>1$. La condición de continuidad de $g$ en $0$ falla ya para $\varepsilon=1$. En particular, $g$ tampoco es derivable allí por Teorema §19.2.1 — Toda función derivable en un punto es continua en él. La continuidad de la inversa no puede deducirse de la derivabilidad local de $f$ en un dominio no compacto y desconectado.

**(ii) Inversa continua con derivada original nula.** Tomemos $K=[0,1]$ y $f:K\to\mathbb R$, $f(x)=x^2$. El intervalo es compacto por Teorema §18.2.1 — Todo intervalo cerrado y acotado es compacto, y $f$ es continua por Teorema §17.5.3 — Todo polinomio real es continuo en la recta. Si $0\le x<z\le1$, entonces $z^2-x^2=(z-x)(z+x)>0$, por lo que $f$ es inyectiva. Además $0\in\operatorname{Acc}(K)$; por Proposición §19.1.6 — Primeros cálculos: funciones afines y función cuadrática y restricción Proposición §19.5.2 — Restricción de una función derivable, $f'(0)=0$. La inversa real $g:E=f[K]\to\mathbb R$ es continua por §19.7.3 y satisface $g(0)=0$, $g(t^2)=t$ para todo $0\le t\le1$.

Si $g'(0)=M$ existiera, su definición con $\varepsilon=1$ proporcionaría $\delta>0$ tal que

$$
 y\in E,\quad 0<y<\delta
 \quad\Longrightarrow\quad |q_{g,0}(y)-M|<1.
$$

Escojamos explícitamente un real $t$ con

$$
 0<t<\min\{1/2,\delta/2,1/(|M|+2)\}.
$$

Por ejemplo, sirve la mitad de ese mínimo positivo. Entonces $0<t<1$, $y:=t^2\in E$ satisface $0<y<t<\delta$ y

$$
 q_{g,0}(t^2)=\frac{g(t^2)-g(0)}{t^2}
 =\frac t{t^2}=\frac1t>|M|+2.
$$

De aquí $|q_{g,0}(t^2)-M|\ge1/t-|M|>2$, contradicción. Luego $g$ es continua pero no derivable en $0$. La no nulidad de $f'(a)$ no es sólo una precaución para escribir el recíproco: constituye una condición sustantiva del teorema. $\square$

**Transición.** Hemos probado la fórmula de la derivada inversa y aislado dos obstáculos independientes: la continuidad de la inversa y la anulación de la derivada original. La siguiente unidad, §19.8, distinguirá derivadas laterales de derivadas relativas a un dominio y cerrará las herramientas locales antes de los teoremas globales del capítulo 20.
