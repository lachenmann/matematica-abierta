## 17.6. Continuidad uniforme: un radio común para todo el dominio {#sec-ta-17-6}

La continuidad puntual de §17.1 comienza fijando un centro $a$; sólo después se obtiene un radio, que puede cambiar si se cambia el centro. Para controlar una función sobre todo su dominio necesitaremos invertir ese orden: dada una tolerancia de salida, buscaremos un único radio que sirva para **cualquier par** de argumentos. No supondremos que el dominio es un intervalo, cerrado, acotado ni siquiera no vacío. El resultado que permite extraer uniformidad de continuidad sobre un compacto —Heine–Cantor— pertenece al Capítulo 18, donde se construirá la compacidad.

### Definición 17.6.1 — Continuidad uniforme relativa a un dominio
Sean $D\subseteq\mathbb R$ y $f:D\to\mathbb R$. Diremos que **$f$ es uniformemente continua en $D$** si

$$
\boxed{\forall\varepsilon>0\ \exists\delta>0\ \forall x,y\in D:\quad
|x-y|<\delta\Longrightarrow |f(x)-f(y)|<\varepsilon.}
$$

El orden es esencial: $\delta$ depende de $\varepsilon$, pero **no** de $x$ ni de $y$. Se permite $x=y$ y también $D=\varnothing$. En este último caso, para cada $\varepsilon>0$ el radio $\delta=1$ verifica la implicación universal vacía; no se asignan valores a la función fuera de su dominio.

> **Dos órdenes de cuantificadores.** Continuidad en todos los puntos: $\forall a\in D\ \forall\varepsilon>0\ \exists\delta>0\ \forall x\in D\,\cdots$. Continuidad uniforme: $\forall\varepsilon>0\ \exists\delta>0\ \forall x,y\in D\,\cdots$. La primera formulación no autoriza trasladar el cuantificador $\exists\delta$ por delante de $\forall a$.


### Proposición 17.6.2 — La uniformidad implica continuidad puntual y pasa a las restricciones
Si $f:D\to\mathbb R$ es uniformemente continua, entonces es continua en cada $a\in D$. Además, para todo $A\subseteq D$, la restricción $f\upharpoonright A:A\to\mathbb R$ es uniformemente continua en $A$.

**Demostración.**
Fijemos $a\in D$ y $\varepsilon>0$. Sea $\delta>0$ el radio uniforme. Si $x\in D$ y $|x-a|<\delta$, aplicamos la implicación a la pareja $(x,a)$ y obtenemos $|f(x)-f(a)|<\varepsilon$. Esto es exactamente continuidad en $a$. Si $A\subseteq D$, las parejas de $A\times A$ están también en $D\times D$, de modo que **el mismo** radio uniforme acredita la condición para la restricción, cuyo grafo y codominio se conservan conforme a §0.6 y §17.4. Cuando $D$ o $A$ es vacío no hay centros ni parejas que verificar. ∎

La recíproca no es válida en dominios arbitrarios, como se demostrará explícitamente en §17.6.7. Tampoco se ha invocado aquí el criterio secuencial condicional de §17.2.


### Proposición 17.6.3 — Una cota de tipo Lipschitz proporciona un radio uniforme
Supongamos que existe una constante real $L\ge0$ tal que

$$
\forall x,y\in D:\qquad |f(x)-f(y)|\le L|x-y|.
$$

Entonces $f:D\to\mathbb R$ es uniformemente continua. En particular, toda función constante y la inclusión $j_D:D\to\mathbb R$, $j_D(x)=x$, son uniformemente continuas sobre cualquier $D\subseteq\mathbb R$.

**Demostración.**
Fijemos $\varepsilon>0$ y elijamos $\delta:=\varepsilon/(L+1)>0$. Para $x,y\in D$ con $|x-y|<\delta$ obtenemos

$$
|f(x)-f(y)|\le L|x-y|\le (L+1)|x-y|<\varepsilon.
$$

La fórmula funciona también cuando $L=0$, sin división por cero. Las constantes satisfacen la cota con $L=0$; la inclusión la satisface con $L=1$. Ambas son funciones tipadas construidas en Proposición §17.4.1 — Funciones constantes e inclusión continua, y no identificamos $j_D:D\to\mathbb R$ con $\operatorname{id}_D:D\to D$ cuando los codominios difieren. ∎

El término «cota de tipo Lipschitz» nombra aquí la desigualdad formulada; no constituye un nuevo operador global ni se consume un ID de notación.


### Teorema 17.6.4 — Operaciones algebraicas uniformes: hipótesis globales exactas
Sean $f,g:D\to\mathbb R$ uniformemente continuas y $c\in\mathbb R$.

1. $f+g$, $f-g$, $cf$ y $|f|$, todas con dominio $D$, son uniformemente continuas.
2. Si existen $A,B\ge0$ con $|f(x)|\le A$ y $|g(x)|\le B$ para **todo** $x\in D$, entonces $fg:D\to\mathbb R$ es uniformemente continua.
3. Sea $D_g:=\{x\in D:g(x)\ne0\}$. Si existe $m>0$ tal que $|g(x)|\ge m$ para todo $x\in D_g$, entonces $1/g:D_g\to\mathbb R$ es uniformemente continua. Si, además, $f$ está acotada en $D$, el cociente $f/g:D_g\to\mathbb R$ es uniformemente continuo.

La mera condición puntual $g(x)\ne0$ no sustituye la separación **uniforme** $|g(x)|\ge m$; la continuidad uniforme de los factores, sin acotación, tampoco garantiza la del producto.

**Demostración.**
Para el primer punto fijemos $\varepsilon>0$. La continuidad uniforme de $f$ y $g$ para $\varepsilon/2$ proporciona radios $r_f,r_g>0$. El mínimo $\delta=\min\{r_f,r_g\}>0$ funciona simultáneamente y la desigualdad triangular da

$$
|(f+g)(x)-(f+g)(y)|
\le |f(x)-f(y)|+|g(x)-g(y)|<\varepsilon.
$$

Para el escalar $c$, tomamos el radio uniforme de $f$ correspondiente a $\varepsilon/(|c|+1)$; así,

$$
|(cf)(x)-(cf)(y)|=|c|\,|f(x)-f(y)|<\varepsilon.
$$

Esto incluye $c=0$. La resta resulta de la suma y el caso $c=-1$. La desigualdad triangular inversa da $\bigl||f(x)|-|f(y)|\bigr|\le|f(x)-f(y)|$, por lo que sirve el radio uniforme de $f$ para $\varepsilon$.

Para el producto, supongamos las dos cotas globales. Obtengamos $r_f$ para la tolerancia $\varepsilon/[2(B+1)]$ y $r_g$ para $\varepsilon/[2(A+1)]$. Si $x,y\in D$ y $|x-y|<\delta:=\min\{r_f,r_g\}$, entonces

$$
\begin{aligned}
|f(x)g(x)-f(y)g(y)|
&\le |f(x)-f(y)|\,|g(x)|+|f(y)|\,|g(x)-g(y)|\\
&\le (B+1)|f(x)-f(y)|+(A+1)|g(x)-g(y)|\\
&<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon.
\end{aligned}
$$

Las constantes $A+1$ y $B+1$ son estrictamente positivas; por ello el paso estricto es válido incluso si alguna de las cotas $A,B$ es cero. Hemos utilizado únicamente dos radios y su mínimo, no una familia de elecciones.

Para el recíproco, $D_g$ existe por Separación y el radio uniforme de $g$ sobre $D$ sigue siendo válido sobre $D_g$. Para cualesquiera $x,y\in D_g$,

$$
\left|\frac1{g(x)}-\frac1{g(y)}\right|
=\frac{|g(x)-g(y)|}{|g(x)|\,|g(y)|}
\le\frac{|g(x)-g(y)|}{m^2}.
$$

Dada $\varepsilon>0$, tomemos para $g$ un radio uniforme con tolerancia $\varepsilon m^2>0$; la última desigualdad demuestra continuidad uniforme de $1/g$. Además, $|1/g(x)|\le1/m$ en $D_g$. Si $|f(x)|\le A$ para todo $x\in D$, su restricción a $D_g$ es uniformemente continua y está acotada por $A$. El producto de esta restricción por $1/g$ es uniformemente continuo por el segundo punto y coincide, **como función tipada**, con $f/g$ en $D_g$. Cuando $D_g=\varnothing$ las dos conclusiones se verifican por la definición vacía, sin formar cocientes en ningún punto. ∎

**Advertencia.** Se puede multiplicar $x\mapsto x$ por sí misma sobre $\mathbb R$ para obtener una función continua en cada punto, pero no se ha probado uniformidad para ese producto: la hipótesis de acotación global falla. Asimismo, $x\mapsto1/x$ es continua en $\mathbb R\setminus\{0\}$ por §17.4, pero eso no le da automáticamente un radio uniforme.


### Teorema 17.6.5 — Composición uniformemente continua en el dominio efectivo
Sean $D,E\subseteq\mathbb R$, $f:D\to\mathbb R$ uniformemente continua en $D$ y $g:E\to\mathbb R$ uniformemente continua en $E$. Definamos

$$
T:=\{x\in D:f(x)\in E\},\qquad f_T:T\to E,
\qquad h:=g\circ f_T:T\to\mathbb R.
$$

Entonces $h$ es uniformemente continua en $T$. Si $f[D]\subseteq E$, esta conclusión vale con $T=D$.

**Demostración.**
La construcción tipada del dominio y del grafo de $h$ es la de Teorema §17.4.5 — Composición en el dominio efectivo: $T$ existe por Separación y $f_T$ conserva el grafo restringido de $f$, pero declara codominio $E$. Fijemos $\varepsilon>0$. La uniformidad de $g$ proporciona $\eta>0$ tal que, para todos $u,v\in E$, $|u-v|<\eta$ implica $|g(u)-g(v)|<\varepsilon$. La uniformidad de $f$ para esa **única tolerancia $\eta$** proporciona $\delta>0$ con

$$
\forall x,y\in D:\quad |x-y|<\delta\Longrightarrow|f(x)-f(y)|<\eta.
$$

Si $x,y\in T$ y $|x-y|<\delta$, las dos imágenes $f(x),f(y)$ pertenecen a $E$; por ello

$$
|h(x)-h(y)|=|g(f(x))-g(f(y))|<\varepsilon.
$$

El radio $\delta$ no depende de ninguno de los dos argumentos. El razonamiento sigue siendo válido si $T$ es vacío y no requiere que $E$ ni $T$ sean abiertos. Se han escogido dos testigos finitos, uno después del otro, sin ninguna versión de Choice. ∎


### Proposición 17.6.6 — Las raíces no negativas son uniformemente continuas
Para cada $n\in\mathbb N_{\ge1}$, la función $r_n:\mathbb R_{\ge0}\to\mathbb R$, $r_n(x)=\sqrt[n]{x}$, es uniformemente continua en **todo** $\mathbb R_{\ge0}$.

**Demostración.**
Fijemos $n\ge1$ y $\varepsilon>0$ y pongamos $\delta:=\varepsilon^n>0$. Para **cualquier** $x,y\ge0$, las raíces $u:=\sqrt[n]{x}$ y $v:=\sqrt[n]{y}$ están bien definidas y son no negativas, con $u^n=x$ y $v^n=y$. El Lema Lema §17.5.5 — Separación de potencias de argumentos no negativos entrega

$$
|u-v|^n\le |u^n-v^n|=|x-y|.
$$

Cuando $|x-y|<\delta=\varepsilon^n$, la monotonía de la potencia positiva sobre no negativos implica $|u-v|<\varepsilon$. Ningún paso ha fijado un centro: **el mismo radio sirve a todos los pares** y también a los que incluyen $0$. La prueba depende de la unicidad de la raíz ya construida, no de elecciones de soluciones. ∎


### Proposición 17.6.7 — Dos funciones continuas que no son uniformemente continuas
Se cumplen las siguientes afirmaciones:

1. $p:\mathbb R\to\mathbb R$, $p(x)=x^2$, es continua en cada punto, pero **no** es uniformemente continua en $\mathbb R$. Su restricción a todo subconjunto acotado de la recta **sí** es uniformemente continua.
2. $q:(0,1]\to\mathbb R$, $q(x)=1/x$, es continua en cada punto de su dominio, pero **no** es uniformemente continua en $(0,1]$.

**Demostración.**
La continuidad puntual de $p$ se deduce de Teorema §17.5.3 — Todo polinomio real es continuo en la recta. Para refutar su uniformidad fijemos $\varepsilon_0:=1$. Dado cualquier $\delta>0$, definamos de modo explícito $h:=\delta/2>0$, $x:=1/h$ y $y:=x+h$. Entonces $x,y\in\mathbb R$ y

$$
|x-y|=h<\delta,
\qquad |p(y)-p(x)|=(x+h)^2-x^2=2xh+h^2=2+h^2>1.
$$

Por tanto ningún radio sirve para la tolerancia $1$ en toda la recta. Si $A\subseteq\mathbb R$ es acotado, existe $M\ge0$ con $|x|\le M$ para todo $x\in A$. Para cualesquiera $x,y\in A$,

$$
|x^2-y^2|=|x-y|\,|x+y|\le2M|x-y|.
$$

La Proposición Proposición §17.6.3 — Una cota de tipo Lipschitz proporciona un radio uniforme se aplica a $p\upharpoonright A:A\to\mathbb R$ con constante $L=2M$, incluso si $A$ es vacío o $M=0$.

La continuidad puntual de $q$ resulta de Corolario §17.5.4 — Continuidad de las funciones racionales en su dominio natural (o del recíproco de §17.4), por restricción al intervalo $(0,1]$. Para refutar uniformidad volvemos a fijar $\varepsilon_0:=1$. Dado $\delta>0$, pongamos $h:=\min\{\delta/2,1/2\}>0$, $x:=h/2$ y $y:=h$. Ambos pertenecen a $(0,1]$ y

$$
|x-y|=h/2<\delta,
\qquad |q(x)-q(y)|=\frac2h-\frac1h=\frac1h\ge2>1.
$$

Así ninguna $\delta$ funciona para todas las parejas del dominio. En ambos contraejemplos, cada pareja infractora se da mediante una fórmula a partir de **un único radio arbitrario**: no se selecciona una sucesión de infractores. ∎

> **Diagnóstico.** La función cuadrática falla al alejarse indefinidamente hacia valores grandes de $|x|$; el recíproco falla cerca de una frontera excluida de su dominio. «Ser continuo en todos los puntos» no contiene un control global uniforme.


### Corolario 17.6.8 — Polinomios y racionales sobre conjuntos acotados, con separación del denominador
Sea $D\subseteq\mathbb R$ **acotado**. Todo polinomio real $P:\mathbb R\to\mathbb R$ definido en §17.5 es uniformemente continuo al restringirse a $D$ y está acotado sobre $D$. Sean ahora $P,Q:\mathbb R\to\mathbb R$ polinomios y

$$
T:=\{x\in D:Q(x)\ne0\}.
$$

Si se dispone adicionalmente de una constante $m>0$ que satisface $|Q(x)|\ge m$ para todo $x\in T$, la función racional $P/Q:T\to\mathbb R$ es uniformemente continua en $T$.

**Demostración.**
Por acotación existe $M\ge0$ tal que $|x|\le M$ para todo $x\in D$. La inclusión $j_D:D\to\mathbb R$ es uniformemente continua por Proposición §17.6.3 — Una cota de tipo Lipschitz proporciona un radio uniforme y está acotada por $M$. Las funciones potencia $p_k:D\to\mathbb R$, $p_k(x)=x^k$, se obtienen por recursión finita: $p_0$ es la constante $1$, y $p_{k+1}=p_kj_D$. Por inducción, $p_k$ es uniformemente continua, y está acotada por $(M+1)^k$: el caso $k=0$ es inmediato; para el paso se aplica el producto de Teorema §17.6.4 — Operaciones algebraicas uniformes: hipótesis globales exactas, puesto que ambos factores son uniformemente continuos y tienen cotas globales, y se usa $|x|^{k+1}\le(M+1)^{k+1}$. Todas las funciones tienen dominio $D$.

Si $c:I_d\to\mathbb R$ es la lista finita de coeficientes de $P$, cada $x\mapsto c(k)x^k$ es uniformemente continua y está acotada por $|c(k)|(M+1)^k$. La recursión de sumas parciales de Definición §14.1.1 — Sucesión de sumas parciales y serie numérica, junto con el primer punto de Teorema §17.6.4 — Operaciones algebraicas uniformes: hipótesis globales exactas, prueba por inducción que los prefijos polinomiales son uniformemente continuos. La desigualdad triangular, aplicada en la misma inducción, proporciona la cota global

$$
|P(x)|\le\sum_{k=0}^{d}|c(k)|(M+1)^k
\qquad(x\in D).
$$

Esta suma es **finita** y está definida en §14.1. Se concluye que $P\upharpoonright D$ y, por el mismo argumento, $Q\upharpoonright D$ son uniformemente continuas y acotadas en $D$. El conjunto $T$ existe por Separación; sobre él se aplica el punto 3 de Teorema §17.6.4 — Operaciones algebraicas uniformes: hipótesis globales exactas a las restricciones de $P,Q$, utilizando la constante $m$ expresamente supuesta. Se obtiene uniformidad de $P/Q:T\to\mathbb R$. Si $T=\varnothing$, la conclusión sólo cuantifica sobre parejas inexistentes y no evalúa el cociente. ∎

La condición $|Q|\ge m>0$ **no se deduce** de que $Q(x)\ne0$ para cada $x\in T$; el recíproco del ejemplo anterior muestra por qué hay que distinguir ambos enunciados. Tampoco hemos inferido tal cota mediante existencia de mínimos en compactos, que pertenece al capítulo siguiente.

**Síntesis y frontera.** La uniformidad exige un radio compartido por todos los puntos: la conservan restricciones, combinaciones aditivas y composiciones, y los productos y cocientes bajo las cotas globales indicadas. Las raíces no negativas admiten un radio explícito $\delta=\varepsilon^n$. El cuadrado en toda la recta y el recíproco sobre $(0,1]$ prueban que continuidad puntual y uniforme son propiedades distintas. La pregunta pendiente es: ¿qué condiciones geométricas sobre el dominio permiten deducir uniformidad de la mera continuidad? El Capítulo 18 responderá mediante la compacidad y Heine–Cantor; no hemos anticipado esos resultados.
