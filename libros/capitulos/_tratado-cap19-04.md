## 19.4. Reglas algebraicas de derivación {#sec-ta-19-4}

En §§19.1–19.3 hemos establecido qué significa derivar **en un punto**, sin exigir que la función esté definida en un intervalo abierto. Esta generalidad se conserva en las reglas algebraicas: todas las funciones consideradas tendrán el mismo dominio $D\subseteq\mathbb R$, y su derivabilidad se exigirá en un punto $a\in D\cap\operatorname{Acc}(D)$. Las operaciones puntuales $f+g$, $cf$, $f-g$ y $fg$ ya fueron construidas como funciones tipadas $D\to\mathbb R$ en Proposición §16.3.2 — Existencia y tipado de las operaciones puntuales. No confundiremos la derivada en $a$ con una función derivada definida automáticamente sobre todo $D$.

La estrategia es comparar los cocientes incrementales **en el dominio perforado $D_a$**. Para la suma y los escalares, su álgebra es inmediata. En el producto aparece un factor que depende del argumento; su límite existe gracias a la continuidad que ya hemos deducido de la derivabilidad. Así evitaremos utilizar el teorema del valor medio o las propiedades secuenciales cuya recíproca pueda requerir elección.

### Teorema 19.4.1 — Regla de derivación de la suma
Sean $f,g:D\to\mathbb R$ derivables en $a\in D\cap\operatorname{Acc}(D)$, con derivadas $L:=f'(a)$ y $M:=g'(a)$. Entonces la función puntual $f+g:D\to\mathbb R$ es derivable en $a$ y

$$
\boxed{(f+g)'(a)=f'(a)+g'(a).}
$$

**Demostración.**
La operación puntual existe y conserva dominio y codominio por Proposición §16.3.2 — Existencia y tipado de las operaciones puntuales. Como $a$ acumula $D$, el lema Lema §19.1.2 — Perforar el dominio preserva la acumulación en el centro asegura que acumula asimismo $D_a$. Para $x\in D_a$ tenemos $x-a\ne0$ y, por distributividad en el cuerpo real,

$$
\begin{aligned}
q_{f+g,a}(x)
&=\frac{[f(x)+g(x)]-[f(a)+g(a)]}{x-a}\\
&=\frac{f(x)-f(a)}{x-a}+\frac{g(x)-g(a)}{x-a}\\
&=q_{f,a}(x)+q_{g,a}(x).
\end{aligned}
$$

Por derivabilidad, las dos funciones $q_{f,a},q_{g,a}:D_a\to\mathbb R$ tienen límites respectivos $L$ y $M$ en $a$. El teorema de suma de límites Teorema §16.3.3 — Suma, resta y multiplicación por escalares, aplicado **a ese mismo dominio $D_a$**, da $\lim_{x\to a}q_{f+g,a}(x)=L+M$. La definición Definición §19.1.3 — Derivabilidad en un punto demuestra la derivabilidad de $f+g$ y la unicidad establecida en Proposición §19.1.4 — Unicidad y criterio cuantificado de la derivada identifica su derivada con $L+M$. La identidad nunca evalúa los cocientes en $a$. $\square$

### Corolario 19.4.2 — Multiplicación por escalares, opuestos y diferencias
Sean $f,g:D\to\mathbb R$ derivables en $a\in D\cap\operatorname{Acc}(D)$ y sea $c\in\mathbb R$ un escalar fijo. Entonces $cf$, $-f$ y $f-g$, consideradas como funciones $D\to\mathbb R$, son derivables en $a$, con

$$
\boxed{(cf)'(a)=cf'(a),\qquad (-f)'(a)=-f'(a),\qquad
(f-g)'(a)=f'(a)-g'(a).}
$$

**Demostración.**
Por el tipado de Proposición §16.3.2 — Existencia y tipado de las operaciones puntuales, $cf:D\to\mathbb R$ está definida para todo $c$, incluso $c=0$. Si $x\in D_a$, la aritmética del cuerpo da la identidad exacta

$$
q_{cf,a}(x)=\frac{cf(x)-cf(a)}{x-a}=c\,q_{f,a}(x).
$$

Como $q_{f,a}$ tiende a $f'(a)$ en el dominio $D_a$, la regla escalar de límites Teorema §16.3.3 — Suma, resta y multiplicación por escalares demuestra que $q_{cf,a}$ tiende a $cf'(a)$; este resultado incluye $c=0$, donde el cociente es constantemente cero. La definición de derivada y su unicidad prueban la primera fórmula.

Con $c=-1$ obtenemos $(-f)'(a)=-f'(a)$. Aplicamos este mismo caso a $g$, y después el teorema de la suma a las dos funciones derivables $f$ y $-g$. Puesto que $f-g=f+(-g)$ como funciones tipadas sobre $D$, resulta

$$
(f-g)'(a)=(f+(-g))'(a)=f'(a)+(-g)'(a)=f'(a)-g'(a).
$$

No se necesita ninguna decisión sobre el signo de $c$, ni se eligen testigos para una familia infinita de funciones. $\square$

### Teorema 19.4.3 — Regla de derivación del producto
Sean $f,g:D\to\mathbb R$ derivables en $a\in D\cap\operatorname{Acc}(D)$. Entonces el producto puntual $fg:D\to\mathbb R$ es derivable en $a$ y

$$
\boxed{(fg)'(a)=f'(a)g(a)+f(a)g'(a).}
$$

**Demostración.**
El producto $fg:D\to\mathbb R$ existe por Proposición §16.3.2 — Existencia y tipado de las operaciones puntuales. Para cada $x\in D_a$, sumemos y restemos el término $f(x)g(a)$ en el numerador; esta manipulación es válida independientemente de que $f(a)$ o $g(a)$ sean nulos:

$$
\begin{aligned}
q_{fg,a}(x)
&=\frac{f(x)g(x)-f(a)g(a)}{x-a}\\
&=\frac{f(x)[g(x)-g(a)]+g(a)[f(x)-f(a)]}{x-a}\\
&=f(x)q_{g,a}(x)+g(a)q_{f,a}(x).
\end{aligned}
$$

**Control del factor variable.** La derivabilidad de $f$ implica su continuidad en $a$ por Teorema §19.2.1 — Toda función derivable en un punto es continua en él. Es decir, dado $\varepsilon>0$, existe $r>0$ tal que $x\in D$ y $|x-a|<r$ implican $|f(x)-f(a)|<\varepsilon$. Esa misma desigualdad, aplicada sólo a $x\in D_a$, demuestra directamente por Definición §16.1.2 — Límite real finito de una función relativo a su dominio que la restricción de $f$ al dominio perforado tiene límite $f(a)$ en $a$; el punto $a$ acumula $D_a$ por Lema §19.1.2 — Perforar el dominio preserva la acumulación en el centro. No se utiliza un valor ficticio de $q_{f,a}(a)$.

Por definición de derivada, $q_{g,a}$ tiende a $g'(a)$ y $q_{f,a}$ tiende a $f'(a)$, ambos sobre $D_a$. En ese dominio común, el teorema del producto de límites Teorema §16.3.4 — Producto y valor absoluto da

$$
\lim_{\substack{x\to a\\x\in D_a}}f(x)q_{g,a}(x)=f(a)g'(a),
$$

y la regla escalar Teorema §16.3.3 — Suma, resta y multiplicación por escalares da el límite $g(a)f'(a)$ para el segundo término. La regla de suma de ese mismo teorema y la identidad exacta del cociente prueban

$$
\lim_{\substack{x\to a\\x\in D_a}}q_{fg,a}(x)
=f(a)g'(a)+g(a)f'(a).
$$

En consecuencia, $fg$ es derivable en $a$, y la unicidad de su derivada establece la fórmula anunciada. Los límites invocados son los **límites de funciones del capítulo 16**, no los de sucesiones ni ningún resultado global de diferenciación. $\square$

**Lectura de la regla.** No es correcto escribir $(fg)'(a)=f'(a)g'(a)$. El incremento de un producto distribuye la variación entre sus dos factores; uno de ellos se conserva con su **valor** en el centro mientras el otro aporta su derivada. La continuidad del factor variable es exactamente lo que permite reemplazar $f(x)$ por $f(a)$ en el límite.

### Corolario 19.4.4 — Derivada del cuadrado de una función
Si $f:D\to\mathbb R$ es derivable en $a\in D\cap\operatorname{Acc}(D)$, la función $h:D\to\mathbb R$ definida por $h(x)=f(x)^2$ es derivable en $a$ y

$$
\boxed{h'(a)=2f(a)f'(a),\qquad 2:=1+1\ \text{en }\mathbb R.}
$$

**Demostración.**
Por la notación de cuadrado Notación §3.1.7 — Cuadrado, $h=ff$ es el producto puntual ya construido de $f$ consigo misma. Aplicando Teorema §19.4.3 — Regla de derivación del producto con ambos factores iguales, obtenemos

$$
h'(a)=f'(a)f(a)+f(a)f'(a)=(1+1)f(a)f'(a)=2f(a)f'(a).
$$

La constante $2$ es aquí la suma de dos unidades **reales**. No hemos supuesto ni construido una regla para potencias arbitrarias a partir de este caso particular. $\square$

**Transición.** Las operaciones sin división conservan el dominio $D$ de los factores. Para un cociente, en cambio, habrá que restringirlo explícitamente al conjunto donde el denominador no se anula y comprobar que el punto sigue siendo de acumulación de ese dominio. En §19.5 desarrollaremos el recíproco y la regla del cociente con esa precaución, sin adelantar la regla de la cadena.
