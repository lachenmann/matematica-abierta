## 19.5. Derivación del recíproco y del cociente {#sec-ta-19-5}

La división introduce una diferencia respecto de §19.4: aunque $f,g:D\to\mathbb R$ tengan el mismo dominio, la función $f/g$ sólo está definida en $D_g:=\{x\in D:g(x)\ne0\}$. Antes de escribir una derivada debemos comprobar tanto que $a\in D_g$ como que $a$ es punto de acumulación **de ese dominio**, no únicamente de $D$. La continuidad de $g$ y la condición $g(a)\ne0$ resolverán simultáneamente ambas cuestiones.

Partiremos de un principio sobre restricciones que también será útil para la regla de la cadena: una derivada relativa a un dominio mayor se conserva al restringirlo, siempre que el punto siga siendo de acumulación. Para el recíproco calcularemos directamente el cociente incremental; la regla del cociente se deducirá entonces de la del producto. Todos los límites y derivadas se entenderán relativamente a los dominios expresamente indicados.

### Lema 19.5.1 — La coincidencia local conserva la acumulación
Sean $E\subseteq D\subseteq\mathbb R$ y $a\in E\cap\operatorname{Acc}(D)$. Supongamos que existe $r>0$ tal que

$$
D\cap B_r(a)\subseteq E.
$$

Entonces $a\in\operatorname{Acc}(E)$; en particular, los dominios perforados de $E$ y $D$ coinciden dentro de esa bola:

$$
\boxed{E\cap(B_r(a)\setminus\{a\})=D\cap(B_r(a)\setminus\{a\}).}
$$

**Demostración.**
La inclusión $E\subseteq D$ y la hipótesis local prueban por doble inclusión la igualdad del recuadro. Para demostrar la acumulación, fijemos cualquier $\rho>0$. El número $\eta:=\min\{r,\rho\}>0$ está determinado por dos valores positivos. Como $a\in\operatorname{Acc}(D)$, el criterio de bolas perforadas Lema §16.1.1 — Acumulación y aproximación perforada proporciona **un** $x\in D$ con $0<|x-a|<\eta$. En particular, $x\in B_r(a)$, de donde $x\in E$, y $0<|x-a|<\rho$. Por el mismo criterio, $a\in\operatorname{Acc}(E)$. La prueba toma un testigo sólo después de fijar $\rho$; no construye ninguna elección simultánea. $\square$

### Proposición 19.5.2 — Restricción de una función derivable
Sean $f:D\to\mathbb R$ derivable en $a\in D\cap\operatorname{Acc}(D)$ y $E\subseteq D$ tal que $a\in E\cap\operatorname{Acc}(E)$. La restricción tipada $f\upharpoonright E:E\to\mathbb R$ es derivable en $a$ y

$$
\boxed{(f\upharpoonright E)'(a)=f'(a).}
$$

No se requiere que $E$ coincida localmente con $D$: basta que contenga $a$ y conserve la acumulación. Si $E$ sí coincide localmente con $D$, el lema anterior garantiza esta última hipótesis.

**Demostración.**
La restricción existe con dominio exactamente $E$ y codominio $\mathbb R$ por Definición §1.3.1 — Restricción de una función y Proposición §1.3.2 — Existencia y unicidad de la restricción; además, $(f\upharpoonright E)(a)=f(a)$. Fijemos $L:=f'(a)$ y $\varepsilon>0$. La derivabilidad de $f$ sobre $D$ proporciona $\delta>0$ tal que, para todo $x\in D$ con $0<|x-a|<\delta$,

$$
\left|\frac{f(x)-f(a)}{x-a}-L\right|<\varepsilon.
$$

La **misma** desigualdad y el **mismo** radio valen para cada $x\in E\setminus\{a\}$, porque $E\subseteq D$ y los valores de la restricción coinciden. Como $a\in\operatorname{Acc}(E)$, su dominio perforado acumula en $a$ por Lema §19.1.2 — Perforar el dominio preserva la acumulación en el centro; por la definición de derivada, $f\upharpoonright E$ es derivable allí. La unicidad Proposición §19.1.4 — Unicidad y criterio cuantificado de la derivada identifica su derivada con $L$. No se extiende una derivada definida solamente en un subconjunto a uno mayor: la afirmación tiene exclusivamente la dirección indicada. $\square$

### Teorema 19.5.3 — Regla de derivación del recíproco
Sea $g:D\to\mathbb R$ derivable en $a\in D\cap\operatorname{Acc}(D)$ y supongamos $g(a)\ne0$. Formemos, por Separación, el dominio efectivo

$$
D_g:=\{x\in D:g(x)\ne0\}
$$

y la función ya legitimada en Proposición §16.3.2 — Existencia y tipado de las operaciones puntuales, $u:=1/g:D_g\to\mathbb R$. Entonces $a\in D_g\cap\operatorname{Acc}(D_g)$, $u$ es derivable en $a$ relativamente a $D_g$ y

$$
\boxed{\left(\frac1g\right)'(a)=-\frac{g'(a)}{g(a)^2}.}
$$

**Demostración.**
Pongamos $M:=g(a)\ne0$ y $L:=g'(a)$. Por Teorema §19.2.1 — Toda función derivable en un punto es continua en él, $g$ es continua en $a$ relativamente a $D$. El lema de separación Lema §17.4.2 — Acotación local y separación de un valor no nulo proporciona $r>0$ tal que

$$
\forall x\in D:\quad |x-a|<r\Longrightarrow |g(x)|>\frac{|M|}{2}>0.
$$

Así, $D\cap B_r(a)\subseteq D_g$ y $a\in D_g$. El lema anterior Lema §19.5.1 — La coincidencia local conserva la acumulación, aplicado a $E=D_g$, asegura $a\in\operatorname{Acc}(D_g)$. Por ello el cociente incremental de $u:D_g\to\mathbb R$ tiene un dominio perforado que acumula en $a$; todas las derivadas que aparecerán están correctamente tipadas.

Para $x\in D_g\setminus\{a\}$, las operaciones del cuerpo, con $g(x)M(x-a)\ne0$, dan la identidad **exacta**

$$
\begin{aligned}
q_{u,a}(x)
&=\frac{g(x)^{-1}-M^{-1}}{x-a}
=\frac{M-g(x)}{M g(x)(x-a)}
=-\frac{q_{g,a}(x)}{M g(x)}.
\end{aligned}
$$

Restando el valor candidato $-L/M^2$, se obtiene, otra vez sólo para los puntos perforados del dominio efectivo,

$$
\left|q_{u,a}(x)+\frac{L}{M^2}\right|
=\frac{|L(g(x)-M)-M(q_{g,a}(x)-L)|}{|M|^2|g(x)|}
\le\frac{2|L|}{|M|^3}|g(x)-M|
+\frac{2}{|M|^2}|q_{g,a}(x)-L|,
$$

donde la última estimación utiliza $|g(x)|>|M|/2$ si $|x-a|<r$. Fijemos $\varepsilon>0$. Por continuidad de $g$ existe $\delta_g>0$ tal que $|g(x)-M|<\varepsilon |M|^3/[4(|L|+1)]$ en $D\cap B_{\delta_g}(a)$. Por derivabilidad, existe $\delta_q>0$ tal que $|q_{g,a}(x)-L|<\varepsilon|M|^2/4$ en el dominio perforado dentro de $B_{\delta_q}(a)$. Con el mínimo finito

$$
\delta:=\min\{r,\delta_g,\delta_q\}>0,
$$

para todo $x\in D_g$ con $0<|x-a|<\delta$ obtenemos

$$
\left|q_{u,a}(x)+\frac{L}{M^2}\right|
<\frac{\varepsilon |L|}{2(|L|+1)}+\frac\varepsilon2<\varepsilon.
$$

Si $L=0$, el primer sumando es nulo y la última desigualdad sigue siendo estricta gracias al segundo; si $L\ne0$, ambas cotas son estrictas. En todos los casos el argumento prueba el límite del cociente incremental, y su unicidad establece $u'(a)=-L/M^2$. Sólo se han elegido tres radios **para la tolerancia fijada**, sin selección de una familia infinita. $\square$

**Interpretación.** El signo negativo procede de intercambiar $g(x)-g(a)$ por $g(a)-g(x)$ en la diferencia de los recíprocos. La hipótesis $g(a)\ne0$ es indispensable: garantiza el valor central, la separación local y el denominador $g(a)^2$ de la fórmula. Ni la continuidad ni la derivabilidad autorizan evaluar un recíproco en un cero.

### Teorema 19.5.4 — Regla de derivación del cociente
Sean $f,g:D\to\mathbb R$ derivables en $a\in D\cap\operatorname{Acc}(D)$ y supongamos $g(a)\ne0$. Con $D_g:=\{x\in D:g(x)\ne0\}$, la función $h:=f/g:D_g\to\mathbb R$ es derivable en $a$ **relativamente a $D_g$** y

$$
\boxed{\left(\frac fg\right)'(a)
=\frac{f'(a)g(a)-f(a)g'(a)}{g(a)^2}.}
$$

**Demostración.**
La derivabilidad de $g$ implica su continuidad en $a$, y la condición $g(a)\ne0$ da $D\cap B_r(a)\subseteq D_g$ para algún $r>0$ por Lema §17.4.2 — Acotación local y separación de un valor no nulo. En consecuencia, el lema Lema §19.5.1 — La coincidencia local conserva la acumulación garantiza $a\in D_g\cap\operatorname{Acc}(D_g)$. La proposición Proposición §19.5.2 — Restricción de una función derivable permite restringir $f$ a este dominio y asegura

$$
F:=f\upharpoonright D_g:D_g\to\mathbb R,
\qquad F(a)=f(a),\quad F'(a)=f'(a).
$$

Por el teorema anterior, $u:=1/g:D_g\to\mathbb R$ es derivable en $a$, con $u(a)=1/g(a)$ y $u'(a)=-g'(a)/g(a)^2$. Como las dos funciones $F,u$ comparten exactamente el dominio $D_g$ y el codominio $\mathbb R$, la regla del producto Teorema §19.4.3 — Regla de derivación del producto es aplicable. Además, $h=Fu$ como **funciones tipadas**: tienen el mismo dominio, codominio y valores. Por ello

$$
\begin{aligned}
h'(a)&=F'(a)u(a)+F(a)u'(a)\\
&=\frac{f'(a)}{g(a)}-\frac{f(a)g'(a)}{g(a)^2}\\
&=\frac{f'(a)g(a)-f(a)g'(a)}{g(a)^2}.
\end{aligned}
$$

Cada división está legitimada por $g(a)\ne0$, que también implica $g(a)^2\ne0$. No se han identificado $f$ y $F$, cuyos dominios son distintos cuando $D_g\ne D$; se utilizan únicamente sus valores y derivadas coincidentes en $a$. No hemos empleado la regla de la cadena ni el teorema del valor medio. $\square$

### Corolario 19.5.5 — Funciones fraccionarias afines y ceros excluidos
Sean $m,b,c,d\in\mathbb R$ y definamos $f,g:\mathbb R\to\mathbb R$ por $f(x)=mx+b$ y $g(x)=cx+d$. En el dominio efectivo $D_g:=\{x\in\mathbb R:cx+d\ne0\}$, la función $h=f/g:D_g\to\mathbb R$ es derivable en **cada punto** $a\in D_g$ y

$$
\boxed{h'(a)=\frac{md-bc}{(ca+d)^2}.}
$$

En particular, $x\mapsto 1/x$ es una función $\mathbb R\setminus\{0\}\to\mathbb R$ derivable en cada $a\ne0$, con derivada $-1/a^2$. Una cancelación algebraica en una expresión, como $x/x=1$ para $x\ne0$, **no** añade automáticamente el punto $0$ al dominio de la función original ni le atribuye derivada allí.

**Demostración.**
Por Proposición §19.1.6 — Primeros cálculos: funciones afines y función cuadrática, las funciones afines $f$ y $g$ son derivables sobre $\mathbb R$ con $f'(a)=m$ y $g'(a)=c$. Fijemos $a\in D_g$; entonces $ca+d\ne0$ y $a\in\operatorname{Acc}(\mathbb R)$. La regla del cociente prueba la derivabilidad de $h$ en $a$ relativamente a $D_g$ y da

$$
h'(a)=\frac{m(ca+d)-(ma+b)c}{(ca+d)^2}
=\frac{md-bc}{(ca+d)^2}.
$$

La arbitrariedad de $a$ establece la afirmación en todo el dominio, incluido el caso $D_g=\varnothing$, para el cual no se asevera derivada en ningún punto. Tomar $m=0,b=1,c=1,d=0$ da la fórmula de $1/x$ sobre $\mathbb R\setminus\{0\}$; tomar $m=c=1,b=d=0$ muestra que $x/x$ coincide punto a punto con la función constante $1$ **restringida** al mismo dominio perforado, pero difiere de la constante $1:\mathbb R\to\mathbb R$ como función tipada. En particular, $0\notin D_g$ y $h'(0)$ carece de significado. $\square$

**Transición.** Las reglas anteriores combinan funciones reales con valores y derivadas calculados en un punto, siempre dentro de un dominio efectivo comprobado. En §19.6 estudiaremos la composición: su dominio será también un subconjunto explícito, y la regla de la cadena se demostrará sin suponer que las pendientes secantes puedan evaluarse en puntos donde el incremento interior se anula.
