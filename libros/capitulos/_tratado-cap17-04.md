## 17.4. Álgebra y composición de funciones continuas {#sec-ta-17-4}

La continuidad de una función expresa que un cambio suficientemente pequeño del argumento, dentro de su dominio, produce un cambio pequeño de su valor. Ya construimos las operaciones puntuales en §16.3.2, con sus dominios efectivos; ahora demostraremos que conservan la continuidad. Es importante no derivar estos resultados de una recíproca secuencial que, para dominios arbitrarios, sólo está disponible bajo una hipótesis adicional: todas las pruebas siguientes son directamente $\varepsilon$–$\delta$ y no utilizan elección.

### Proposición 17.4.1 — Funciones constantes e inclusión continua
Sea $D\subseteq\mathbb R$ arbitrario. Para cada $c\in\mathbb R$, la función constante $k_c:D\to\mathbb R$, $k_c(x)=c$, y la función inclusión $j_D:D\to\mathbb R$, $j_D(x)=x$, existen, son únicas con esos datos y son continuas en todos los puntos de $D$.

**Demostración.**
Los grafos $\{\langle x,c\rangle:x\in D\}$ y $\{\langle x,x\rangle:x\in D\}$ se obtienen por Separación dentro de $D\times\mathbb R$. Sus valores son únicos, y declarar exactamente el dominio $D$ y el codominio $\mathbb R$ determina las dos funciones. Si $D=\varnothing$, no hay puntos en los que comprobar continuidad.

Fijemos $a\in D$ y $\varepsilon>0$. Para $k_c$, tomemos $\delta=1$: en cualquier $x\in D$ se tiene $|k_c(x)-k_c(a)|=0<\varepsilon$. Para $j_D$, tomemos $\delta=\varepsilon$: de $|x-a|<\delta$ resulta $|j_D(x)-j_D(a)|=|x-a|<\varepsilon$. Ambos argumentos incluyen puntos aislados y no requieren acumulación. Obsérvese que $j_D:D\to\mathbb R$ no es, como función tipada, la identidad $\operatorname{id}_D:D\to D$ cuando sus codominios difieren. ∎


### Lema 17.4.2 — Acotación local y separación de un valor no nulo
Sea $g:D\to\mathbb R$ continua en $a\in D$ y escribamos $M=g(a)$. Existe $r>0$ tal que

$$
\forall x\in D:\quad |x-a|<r\Longrightarrow |g(x)|<|M|+1.
$$

Si, además, $M\ne0$, existe $r_0>0$ tal que

$$
\forall x\in D:\quad |x-a|<r_0\Longrightarrow
|g(x)|>\frac{|M|}{2}>0.
$$

En particular, $D_g:=\{x\in D:g(x)\ne0\}$ contiene $D\cap B_{r_0}(a)$, incluido $a$, y por tanto $a\in D_g$.

**Demostración.**
Apliquemos continuidad con tolerancia $1>0$ y obtengamos $r>0$ para el cual $|g(x)-M|<1$ siempre que $x\in D$ y $|x-a|<r$. La desigualdad triangular implica

$$
|g(x)|\le |g(x)-M|+|M|<|M|+1.
$$

Si $M\ne0$, entonces $|M|/2>0$. Apliquemos continuidad ahora con esa tolerancia y obtengamos $r_0>0$ tal que $|g(x)-M|<|M|/2$ en $D\cap B_{r_0}(a)$. La desigualdad triangular inversa da

$$
|g(x)|\ge |M|-|g(x)-M|>\frac{|M|}{2}>0.
$$

Por Separación existe $D_g$ y todos los puntos de la bola relativa indicada pertenecen a él. No hemos perforado la bola ni inferido acumulación del dominio. ∎


### Teorema 17.4.3 — Estabilidad de la continuidad bajo operaciones algebraicas y valor absoluto
Sean $f,g:D\to\mathbb R$ continuas en el mismo punto $a\in D$, y sea $c\in\mathbb R$. Entonces son continuas en $a$ las funciones $f+g$, $f-g$, $cf$, $fg$ y $|f|$, todas con dominio $D$ y codominio $\mathbb R$ conforme a §16.3.2.

**Demostración.**
Escribamos $L=f(a)$ y $M=g(a)$. Fijemos $\varepsilon>0$.

**Suma.** La continuidad de $f$ y $g$ con tolerancias $\varepsilon/2$ proporciona radios $\delta_f,\delta_g>0$. Si $x\in D$ y $|x-a|<\min\{\delta_f,\delta_g\}$, la desigualdad triangular da

$$
|(f+g)(x)-(f+g)(a)|
\le |f(x)-L|+|g(x)-M|<\varepsilon.
$$

**Escalares y resta.** Si $c=0$, $cf$ es constante y es continua por la Proposición 17.4.1. Si $c\ne0$, el radio correspondiente a $\varepsilon/|c|$ para $f$ verifica

$$
|(cf)(x)-(cf)(a)|=|c|\,|f(x)-L|<\varepsilon.
$$

La continuidad de $-g$ se deduce con $c=-1$ y la de $f-g=f+(-g)$, mediante la regla ya probada para la suma.

**Producto.** Por el Lema 17.4.2 existen $r>0$ y $K:=|M|+1>0$ tales que $|g(x)|<K$ para $x\in D$ con $|x-a|<r$. Tomemos un radio $\delta_f>0$ para la tolerancia $\varepsilon/(2K)$ de $f$ y otro $\delta_g>0$ para $\varepsilon/(2(|L|+1))$ de $g$. Con $\delta:=\min\{r,\delta_f,\delta_g\}>0$ obtenemos

$$
\begin{aligned}
|f(x)g(x)-LM|
&=|(f(x)-L)g(x)+L(g(x)-M)|\\
&\le |f(x)-L|\,|g(x)|+|L|\,|g(x)-M|\\
&<\frac{\varepsilon}{2K}K+
\frac{\varepsilon}{2(|L|+1)}|L|\\
&\le\varepsilon.
\end{aligned}
$$

La estimación estricta de la línea anterior implica $|f(x)g(x)-LM|<\varepsilon$; no se usa la desigualdad final no estricta como si fuera estricta.

**Valor absoluto.** La desigualdad triangular inversa ya probada proporciona

$$
\bigl||f(x)|-|f(a)|\bigr|\le |f(x)-f(a)|.
$$

El radio de continuidad de $f$ para $\varepsilon$ sirve también para $|f|$. En todos los casos se eligen solamente un número finito de radios, combinados mediante su mínimo. ∎


### Teorema 17.4.4 — Continuidad del recíproco y del cociente en sus dominios efectivos
Sean $f,g:D\to\mathbb R$ continuas en $a\in D$, y supongamos $g(a)\ne0$. Definamos

$$
D_g=\{x\in D:g(x)\ne0\}.
$$

Entonces $a\in D_g$ y las funciones ya construidas

$$
\frac1g:D_g\to\mathbb R,
\qquad \frac fg:D_g\to\mathbb R
$$

son continuas en $a$ relativamente a $D_g$. De hecho, $D_g$ coincide con $D$ en alguna bola centrada en $a$, intersectada con $D$.

**Demostración.**
Pongamos $M=g(a)\ne0$. El Lema 17.4.2 proporciona $r_0>0$ con $D\cap B_{r_0}(a)\subseteq D_g$; la inclusión contraria $D_g\subseteq D$ es definitoria. Por tanto $D_g\cap B_{r_0}(a)=D\cap B_{r_0}(a)$ y $a\in D_g$.

Fijemos $\varepsilon>0$. La continuidad de $g$ en $a$ suministra $\delta_g>0$ tal que

$$
|g(x)-M|<\frac{\varepsilon|M|^2}{2}
\quad\text{si }x\in D,\ |x-a|<\delta_g.
$$

Con $\delta=\min\{r_0,\delta_g\}$, para todo $x\in D_g$ con $|x-a|<\delta$ tenemos $|g(x)|>|M|/2$ y

$$
\left|\frac1{g(x)}-\frac1M\right|
=\frac{|g(x)-M|}{|g(x)|\,|M|}
<\frac{2|g(x)-M|}{|M|^2}<\varepsilon.
$$

Esto prueba la continuidad de $1/g$ en $a$ con el dominio exacto $D_g$. La restricción $f\upharpoonright D_g:D_g\to\mathbb R$ es continua en $a$: todo radio que funciona para $f$ sobre $D$ sigue funcionando para el subconjunto $D_g$ que contiene $a$. Sobre $D_g$, la función producto $(f\upharpoonright D_g)(1/g)$ coincide con $f/g$ en dominio, codominio y valores. Por el Teorema 17.4.3 dicho producto es continuo en $a$. No se define $1/g(a)$ si $g(a)=0$, ni se afirma que $f/g$ sea una función total sobre $D$ cuando $D_g\ne D$. ∎

**Ejemplo de la restricción necesaria.** Para $f(x)=1$ y $g(x)=x$ en $D=\mathbb R$, el cociente tiene dominio $D_g=\mathbb R\setminus\{0\}$ y es continuo en todos sus puntos, pero no se le atribuye continuidad en $0$, donde no tiene valor.


### Teorema 17.4.5 — Composición en el dominio efectivo
Sean $D,E\subseteq\mathbb R$, $f:D\to\mathbb R$ y $g:E\to\mathbb R$. Definamos el dominio efectivo de composición

$$
T:=\{x\in D:f(x)\in E\}.
$$

La restricción de $f$ a $T$, provista del codominio $E$, es una función $f_T:T\to E$; por consiguiente $h:=g\circ f_T:T\to\mathbb R$ está definida sin evaluar $g$ fuera de $E$. Si $a\in T$, $f$ es continua en $a$ relativamente a $D$ y $g$ es continua en $b:=f(a)$ relativamente a $E$, entonces $h$ es continua en $a$ relativamente a $T$.

**Demostración.**
El conjunto $T$ existe por Separación en $D$. Por definición, cada $f(x)$ para $x\in T$ pertenece a $E$; la restricción del grafo de $f$ a $T$, con dominio $T$ y codominio expresamente cambiado a $E$, es una función. La composición funcional de §0.6.4 produce $h:T\to\mathbb R$ con $h(x)=g(f(x))$. Como $a\in T$, también $b=f(a)\in E$ y $h(a)=g(b)$.

Fijemos $\varepsilon>0$. La continuidad de $g$ en $b$ proporciona $\eta>0$ tal que, para todo $y\in E$,

$$
|y-b|<\eta\Longrightarrow |g(y)-g(b)|<\varepsilon.
$$

La continuidad de $f$ en $a$ para la tolerancia $\eta$ proporciona $\delta>0$ tal que, para todo $x\in D$,

$$
|x-a|<\delta\Longrightarrow |f(x)-b|<\eta.
$$

Si $x\in T$ y $|x-a|<\delta$, entonces $x\in D$ y $f(x)\in E$. Podemos sustituir $y=f(x)$ en la primera implicación y obtener

$$
|h(x)-h(a)|=|g(f(x))-g(f(a))|<\varepsilon.
$$

Esto es continuidad relativa a $T$, incluidos sus puntos aislados. No se exige que $b$ sea punto de acumulación de $E$, que $f(x)\ne b$, ni que $f[T]$ sea abierto. La elección de $\eta$ y luego de $\delta$ es finita y dependiente, pero no es un axioma de elección. ∎

**Caso total.** Si $f[D]\subseteq E$, se tiene $T=D$ y la conclusión afirma continuidad de $g\circ f_D:D\to\mathbb R$ en $a$, donde $f_D:D\to E$ indica el re-tipado explícito de $f$. No identificamos dos funciones con distintos codominios.


### Corolario 17.4.6 — Clausura global, restricciones y cocientes
Si $f,g:D\to\mathbb R$ son continuas en todos los puntos de $D$, también lo son $f\pm g$, $cf$, $fg$ y $|f|$. La restricción de cualquier función continua $f$ a $A\subseteq D$ es continua en cada punto de $A$. Si $g$ es continua en todo $D$, entonces $1/g$ y $f/g$ son continuas en su dominio efectivo $D_g$, que puede ser vacío. Para funciones $f:D\to\mathbb R$, $g:E\to\mathbb R$ globalmente continuas en sus respectivos dominios, su composición tipada es continua en $T=\{x\in D:f(x)\in E\}$; en particular, si $f[D]\subseteq E$, es continua en $D$.

**Demostración.**
Fijado cualquier $a\in D$, el Teorema 17.4.3 demuestra la primera afirmación, y la arbitrariedad del punto la extiende a $D$. Si $a\in A$, entonces $a\in D$ y cualquier radio de continuidad de $f$ en $a$ controla también los argumentos de $A$; la restricción conserva el valor en $a$, por lo que es continua allí. Para cada $a\in D_g$, tenemos $g(a)\ne0$ y aplicamos el Teorema 17.4.4; si $D_g$ es vacío, la afirmación universal no exige testigos. Finalmente, fijemos $a\in T$: la continuidad de $f$ en $a$ y la de $g$ en $f(a)\in E$ permiten aplicar el Teorema 17.4.5. Otra vez, $T=\varnothing$ presenta una cuantificación universal vacía y no un límite vacuo. ∎

**Síntesis.** Las operaciones algebraicas conservan la continuidad donde sus expresiones están definidas; el cociente requiere la exclusión efectiva de los ceros de su denominador, y la composición requiere pertenencia al dominio exterior. Ninguna conclusión identifica dominios o codominios distintos ni necesita convertir un criterio secuencial condicional en un teorema incondicional. En §17.5 aplicaremos estas reglas a funciones elementales cuya definición y legitimidad ya estén establecidas.
