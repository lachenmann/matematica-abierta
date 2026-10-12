---
title: Capítulo 0. Del límite a la pregunta por el cálculo
status: published
draft: false
book-id: MA-BOK-0015
editorial-project: EDC
date-modified: '2026-10-12'
license: GFDL-1.3-or-later
areas:
- calculo
- analisis
- fundamentos
level: intermedio
topics:
- calculo-de-una-variable
- historia-de-las-matematicas
number-sections: false
provenance:
  type: original
  sources:
  - role: idea
    note: 'Inspiración metodológica: Gabor Toth, Elements of Mathematics (2021); obra
      independiente.'
source-id: EDC-C00
source-sha256: 3a7cdad92b8003d3236c478eee1a3d93a32dcd92270a8fc3352b37dfb43a2ac7
content-id: MA-BCH-0331
content-type: book-chapter
related:
- MA-BOK-0015
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-00.html) · [Ejercicios](capitulo-00-ejercicios.html) · [Soluciones](capitulo-00-soluciones.html) · [Notas históricas](capitulo-00-notas.html)

[Capítulo 1 →](capitulo-01.html)

> **Pregunta generadora.** ¿Qué permiten comprender ya los números reales, los límites y la continuidad, y qué debemos construir todavía para responder a los problemas de las tangentes, la velocidad y el área?

El cálculo no comenzó como un catálogo de reglas para derivar e integrar. Antes de que esas operaciones adquirieran sus formas modernas existían problemas geométricos, mecánicos y numéricos que reclamaban algo más que el álgebra ordinaria. ¿Cómo hablar de la inclinación de una curva en un punto? ¿Cómo asignar un área exacta a una región de borde curvo? ¿Cómo reconocer una magnitud que cambia a cada instante sin reducir el movimiento a una sucesión de posiciones inmóviles?

En este capítulo estableceremos el lenguaje matemático con el cual pueden formularse esas preguntas. No construiremos aquí la derivada ni la integral: serán las protagonistas de los capítulos siguientes. Nuestra tarea es otra y es imprescindible. Tenemos que distinguir con cuidado un cálculo finito, un proceso de aproximación y la existencia de un límite. También necesitamos saber qué aportan la completitud de los números reales y la continuidad de las funciones, porque de ellas dependerán resultados fundamentales sobre extremos, acumulaciones y variación.

Al terminar, el lector podrá justificar el paso de ciertas sucesiones y cocientes a sus límites, demostrar los principales teoremas de las funciones continuas sobre intervalos, y reconocer por qué una sucesión de aproximaciones numéricas no constituye, por sí sola, una definición general de área o de velocidad instantánea.

## 0.1. Dos preguntas ante una misma curva

Consideremos la parábola $y=x^2$. Es una función familiar; podemos evaluar $f(x)=x^2$ sin recurrir al cálculo. Sin embargo, aparecen enseguida dos problemas de naturaleza diferente.

**Primer problema: la inclinación.** Entre los puntos $(a,a^2)$ y $(a+h,(a+h)^2)$, con $h\neq0$, la recta secante tiene pendiente

$$
\frac{(a+h)^2-a^2}{h}=2a+h.
$$

Podemos hacer $h$ tan pequeño como queramos, manteniendo $h\neq0$. La expresión se aproxima a $2a$. Es importante advertir lo que **no** hemos hecho: no hemos sustituido $h=0$ en una fracción que dejaría de estar definida. Hemos simplificado algebraicamente un cociente válido sólo para $h\neq0$ y reconocido un valor al que se acerca. El capítulo 1 explicará en qué sentido esa operación permite definir una tangente.

**Segundo problema: la acumulación.** En el intervalo $[0,1]$ queremos medir la región comprendida entre el eje horizontal y la gráfica $y=x^2$. Si dividimos el intervalo en $n$ partes iguales, cada una de anchura $1/n$, podemos sumar áreas de rectángulos elegidos sobre los extremos derechos:

$$
R_n=\frac1n\sum_{k=1}^n\left(\frac{k}{n}\right)^2
=\frac1{n^3}\sum_{k=1}^n k^2.
$$

La identidad finita

$$
\sum_{k=1}^n k^2=\frac{n(n+1)(2n+1)}6
$$

se comprueba por inducción: al sumar $(n+1)^2$ al término $n(n+1)(2n+1)/6$ se obtiene $(n+1)(n+2)(2n+3)/6$, que es la misma fórmula con $n+1$; el caso $n=1$ es inmediato. Por consiguiente,

$$
R_n=\frac{(n+1)(2n+1)}{6n^2}
=\frac13+\frac1{2n}+\frac1{6n^2}.
$$

Por tanto, $R_n$ se acerca a $1/3$ cuando $n$ aumenta indefinidamente. Las sumas con extremos izquierdos también se acercan a $1/3$; lo comprobaremos en §0.7. La coincidencia es prometedora, pero aún no demuestra una teoría general de áreas curvilíneas. ¿Qué ocurrirá con otras funciones, subdivisiones desiguales y elecciones diferentes de alturas? Esa pregunta nos conducirá de las cuadraturas al concepto de integral.

Estas dos experiencias anuncian la estructura del libro: **cambio local** y **acumulación**. Para pasar de las expresiones finitas a resultados demostrables debemos precisar el significado de «acercarse».

## 0.2. Por qué trabajamos con los números reales

### 0.2.1. Orden y completitud

Nuestro conjunto de números es $\mathbb R$. Adoptamos su estructura usual de **cuerpo ordenado**: son válidas las operaciones de suma, resta, producto y división por un número no nulo; el orden es compatible con suma y multiplicación por cantidades positivas. Tomaremos $\mathbb N=\{1,2,3,\ldots\}$; así, $0\notin\mathbb N$. Estas propiedades algebraicas son nuestro punto de partida, no un resultado secreto que se atribuya al cálculo.

Hay una propiedad adicional que distingue decisivamente a $\mathbb R$ de $\mathbb Q$.

**Definición 0.1 (cota superior y supremo; `EDC-C00-DEF-001`).** Sea $A\subseteq\mathbb R$ no vacío. Un número $M\in\mathbb R$ es **cota superior** de $A$ si $x\le M$ para todo $x\in A$. Decimos que $s$ es el **supremo** de $A$, escrito $s=\sup A$, si es cota superior y si ninguna cantidad menor que $s$ lo es. Equivalentemente,

$$
\bigl(\forall x\in A\;x\le s\bigr)
\quad\text{y}\quad
\bigl(\forall\varepsilon>0\;\exists x\in A:\ s-\varepsilon<x\bigr).
$$

La segunda parte explica cómo se aproxima un conjunto a su menor cota superior, aun si el supremo no pertenece al conjunto.

**Axioma de completitud de $\mathbb R$ (`EDC-C00-AX-001`).** Todo subconjunto no vacío de $\mathbb R$ que esté acotado superiormente posee supremo en $\mathbb R$.

No estamos haciendo aquí una construcción de los reales a partir de los racionales; eso pertenece a otro tipo de libro. Sí explicaremos las consecuencias del axioma que utilizaremos en el cálculo. Cada vez que aparezca un supremo habrá que comprobar antes que el conjunto no es vacío y está acotado.

### 0.2.2. La propiedad arquimediana

**Teorema 0.1 (`EDC-C00-THM-001`).** Para todo $x\in\mathbb R$ existe $n\in\mathbb N$ tal que $n>x$. En consecuencia, para todo $\varepsilon>0$ existe $n\in\mathbb N$ con $0<1/n<\varepsilon$.

**Demostración.** Si $\mathbb N$ estuviera acotado superiormente, por completitud existiría $s=\sup\mathbb N$. La caracterización aproximativa del supremo, aplicada a $\varepsilon=1$, daría $n\in\mathbb N$ con $s-1<n\le s$. Pero $n+1\in\mathbb N$ y $n+1>s$, contradicción. Por tanto, $\mathbb N$ no está acotado superiormente. Dado $\varepsilon>0$, elegimos $n>1/\varepsilon$ y obtenemos $1/n<\varepsilon$. $\square$

Este resultado descarta que exista en la recta real una magnitud positiva menor que todos los números $1/n$. El hecho de que $1/n$ pueda hacerse arbitrariamente pequeño no significa que alguno de sus valores sea cero.

### 0.2.3. Un hueco entre los racionales

En $\mathbb Q$, la ecuación $x^2=2$ no tiene solución. En efecto, si $p/q$ fuera una fracción irreducible con $(p/q)^2=2$, tendríamos $p^2=2q^2$. Así, $p$ sería par, digamos $p=2r$; entonces $q^2=2r^2$ y también $q$ sería par, contradiciendo la irreducibilidad.

La completitud permite, en cambio, demostrar la existencia de una solución real positiva.

**Proposición 0.1 (`EDC-C00-PRP-001`).** Existe un único $r>0$ con $r^2=2$.

**Demostración.** Consideremos $A=\{x\in[0,2]:x^2<2\}$. El conjunto es no vacío (contiene $1$) y está acotado por $2$. Sea $r=\sup A$. Como $1\in A$, se tiene $r\ge1$. Si $r^2<2$, elegimos $0<d<\min\{1,(2-r^2)/(2r+1)\}$. Entonces

$$
(r+d)^2=r^2+d(2r+d)<2,
$$

por lo que $r+d\in A$; esto contradice que $r$ sea cota superior. Si $r^2>2$, elegimos $0<d<\min\{r,(r^2-2)/(2r)\}$. De aquí

$$
(r-d)^2=r^2-2rd+d^2>2.
$$

Pero, por ser $r=\sup A$, existe $x\in A$ con $r-d<x\le r$; como $x\ge0$ y $r-d>0$, tenemos $x^2>(r-d)^2>2$, otra contradicción. Por tanto, $r^2=2$. Si $0<r<s$ y ambos tuvieran cuadrado $2$, la desigualdad $r^2<s^2$ sería imposible. $\square$

Este ejemplo ilustra un fenómeno esencial: una sucesión de aproximaciones racionales puede dirigirse hacia un número que no es racional. La noción rigurosa de límite requiere decidir primero en qué conjunto se pretende encontrar su valor.

## 0.3. Sucesiones: lo que significa acercarse

**Definición 0.2 (`EDC-C00-DEF-002`).** Una sucesión real es una función $n\mapsto x_n$ de $\mathbb N$ en $\mathbb R$. Decimos que $x_n$ **converge** a $\ell\in\mathbb R$ si

$$
\forall\varepsilon>0\;\exists N\in\mathbb N\;\forall n\ge N:
\quad |x_n-\ell|<\varepsilon.
$$

Escribimos $x_n\to\ell$ o $\lim_{n\to\infty}x_n=\ell$. El orden de los cuantificadores importa: $N$ puede depender de $\varepsilon$, pero no del índice $n$ que viene después. Por el Teorema 0.1, $1/n\to0$.

**Lema 0.1 (`EDC-C00-LEM-001`).** Toda sucesión convergente tiene límite único y está acotada. Si $u_n\to u$ y $v_n\to v$, entonces $u_n+v_n\to u+v$, $u_nv_n\to uv$ y, si $v\neq0$, $u_n/v_n\to u/v$ (el cociente está definido para $n$ suficientemente grande).

**Demostración.** Si $x_n\to a$ y $x_n\to b$, para cualquier $\varepsilon>0$ y $n$ suficientemente grande,

$$
|a-b|\le|a-x_n|+|x_n-b|<2\varepsilon.
$$

Como $\varepsilon$ es arbitrario, $a=b$. Para la acotación, tomamos $\varepsilon=1$: los términos desde cierto índice satisfacen $|x_n|\le|\ell|+1$ y los anteriores son finitos en número. La suma se controla mediante la desigualdad triangular. Para el producto usamos

$$
|u_nv_n-uv|\le |u_n|\,|v_n-v|+|v|\,|u_n-u|;
$$

el primer factor permanece acotado. Finalmente, si $v\neq0$, para índices grandes $|v_n|>|v|/2$, y

$$
\left|\frac{u_n}{v_n}-\frac uv\right|
=\frac{|v(u_n-u)-u(v_n-v)|}{|v|\,|v_n|}
\longrightarrow0.
$$

Cada estimación se hace menor que una tolerancia fijada escogiendo un índice común suficientemente grande. $\square$

**Lema 0.2 (encajonamiento; `EDC-C00-LEM-002`).** Si $a_n\le b_n\le c_n$ desde cierto índice y $a_n\to L$, $c_n\to L$, entonces $b_n\to L$.

**Demostración.** Para $\varepsilon>0$, tanto $a_n$ como $c_n$ pertenecen al intervalo $(L-\varepsilon,L+\varepsilon)$ a partir de un índice común. La desigualdad obliga a que también $b_n$ pertenezca a él. $\square$

### 0.3.1. Sucesiones monótonas e intervalos encajados

**Teorema 0.2 (convergencia monótona; `EDC-C00-THM-002`).** Toda sucesión real no decreciente y acotada superiormente converge al supremo de sus términos. La afirmación dual vale para sucesiones no crecientes acotadas inferiormente.

**Demostración.** Sea $s=\sup\{x_n:n\in\mathbb N\}$. Dado $\varepsilon>0$, hay un término $x_N>s-\varepsilon$. Para $n\ge N$, la monotonía y la propiedad de cota superior dan $s-\varepsilon<x_N\le x_n\le s$. Por consiguiente, $|x_n-s|<\varepsilon$. Para el caso no creciente aplicamos la primera parte a $-x_n$. $\square$

**Teorema 0.3 (intervalos encajados; `EDC-C00-THM-003`).** Sean $I_n=[a_n,b_n]$ intervalos cerrados no vacíos y acotados tales que $I_{n+1}\subseteq I_n$. Entonces $\bigcap_{n\ge1}I_n$ no es vacío. Si además $b_n-a_n\to0$, esa intersección consta de un solo número.

**Demostración.** Los extremos izquierdos forman una sucesión no decreciente y los derechos una no creciente. Sea $c=\sup\{a_n:n\ge1\}$. Este supremo existe, pues $a_n\le b_1$. Para cada $n$ y todo $k$, $a_k\le b_n$: si $k\le n$, por encajamiento $a_k\le a_n\le b_n$; si $k\ge n$, $a_k\le b_k\le b_n$. Así, $b_n$ es cota superior de todos los $a_k$, de modo que $c\le b_n$; y por definición $a_n\le c$. Luego $c\in I_n$ para todo $n$. Si $d$ también pertenece a todos ellos, $|c-d|\le b_n-a_n$ para todo $n$. Si estas longitudes tienden a cero, $c=d$. $\square$

### 0.3.2. La selección de una subsucesión convergente

**Teorema 0.4 (Bolzano–Weierstrass en la recta; `EDC-C00-THM-004`).** Toda sucesión real acotada posee una subsucesión convergente.

**Demostración.** Incluyamos todos los términos en $I_0=[a,b]$; si $a=b$, la afirmación es inmediata. Dividimos $I_0$ en dos mitades cerradas: al menos una contiene infinitos términos de la sucesión (contados por sus índices). La escogemos como $I_1$ y repetimos el procedimiento dentro de ella. Así construimos intervalos cerrados encajados $I_k$ de longitud $(b-a)/2^k$, cada uno con infinitos términos. Por el Teorema 0.3 y porque $(b-a)/2^k\to0$, existe un único $c$ en todos los intervalos.

Escogemos sucesivamente $n_1<n_2<\cdots$ de manera que $x_{n_k}\in I_k$: es posible porque cada $I_k$ contiene términos con índices arbitrariamente grandes. Como $x_{n_k}$ y $c$ están en $I_k$,

$$
|x_{n_k}-c|\le\frac{b-a}{2^k}\longrightarrow0.
$$

Por tanto, $x_{n_k}\to c$. $\square$

Para justificar que $2^{-k}\to0$ basta observar $2^k\ge k+1$ por inducción y aplicar el Teorema 0.1. Los teoremas anteriores son consecuencias concretas de la completitud real; no hemos necesitado hablar de espacios métricos abstractos.

## 0.4. Límites de funciones y continuidad

### 0.4.1. El valor al que se acerca una función

Un **punto de acumulación** de $D\subseteq\mathbb R$ es un número $a$ tal que todo intervalo $(a-\delta,a+\delta)$, $\delta>0$, contiene algún punto de $D$ diferente de $a$. Este requisito evita hablar de un límite determinado cuando no existen puntos del dominio que se acerquen al lugar considerado.

**Definición 0.3 (límite funcional; `EDC-C00-DEF-003`).** Sea $f:D\to\mathbb R$, $D\subseteq\mathbb R$, y sea $a$ un punto de acumulación de $D$. Afirmamos que

$$
\lim_{x\to a,\ x\in D} f(x)=L
$$

si, para todo $\varepsilon>0$, existe $\delta>0$ tal que

$$
x\in D,\quad 0<|x-a|<\delta
\quad\Longrightarrow\quad |f(x)-L|<\varepsilon.
$$

El punto $a$ **no tiene que pertenecer** a $D$. Si pertenece, el valor $f(a)$ no interviene en esta definición: el entorno es perforado. Cuando el dominio está claro omitiremos la indicación $x\in D$ debajo del límite.

Por ejemplo, con $D=\mathbb R\setminus\{a\}$, la función $f(x)=(x^2-a^2)/(x-a)$ coincide en su dominio con $x+a$. Por tanto, $\lim_{x\to a}f(x)=2a$, aunque $f(a)$ no esté definido.

**Teorema 0.5 (criterio secuencial del límite; `EDC-C00-THM-005`).** En las condiciones de la definición anterior,

$$
\lim_{x\to a,\ x\in D}f(x)=L
$$

si y sólo si para toda sucesión $(x_n)$ con $x_n\in D\setminus\{a\}$ y $x_n\to a$ se cumple $f(x_n)\to L$.

**Demostración.** Supongamos el límite funcional. Dado $\varepsilon>0$, elegimos su $\delta$. Toda sucesión que converge a $a$ permanece a distancia menor que $\delta$ desde cierto índice, y por hipótesis nunca toma el valor $a$; luego $|f(x_n)-L|<\varepsilon$ finalmente.

Recíprocamente, si no hubiera límite $L$, existiría $\varepsilon_0>0$ tal que para cada $n\in\mathbb N$ podríamos elegir $x_n\in D$ con

$$
0<|x_n-a|<\frac1n,
\qquad |f(x_n)-L|\ge\varepsilon_0.
$$

Entonces $x_n\to a$ pero $f(x_n)$ no converge a $L$, contradicción. $\square$

**Corolario 0.1 (`EDC-C00-COR-001`).** Un límite funcional finito, en un punto de acumulación, es único. Son válidas las reglas de suma, producto y cociente de límites cuando el límite del denominador es distinto de cero.

**Demostración.** Por acumulación se puede elegir una sucesión de puntos distintos de $a$ que tienda a $a$ (tomando uno a distancia menor que $1/n$). Si existieran dos límites diferentes, esa sucesión de valores convergería a ambos, contra el Lema 0.1. Las reglas se siguen aplicando el Teorema 0.5 y las operaciones con sucesiones del mismo lema; la condición de denominador no nulo asegura que las divisiones están definidas suficientemente cerca del punto. $\square$

### 0.4.2. Continuidad: aproximarse también al valor

**Definición 0.4 (continuidad relativa al dominio; `EDC-C00-DEF-004`).** Sea $f:D\to\mathbb R$ y $a\in D$. La función es **continua en $a$** si para todo $\varepsilon>0$ existe $\delta>0$ tal que

$$
x\in D,\quad |x-a|<\delta
\quad\Longrightarrow\quad |f(x)-f(a)|<\varepsilon.
$$

Si $a$ es punto de acumulación, esta condición equivale a $\lim_{x\to a,\,x\in D}f(x)=f(a)$. Si $a$ es aislado en $D$, la continuidad relativa se cumple automáticamente; no se debe inventar un límite de valores que no pueden aproximarse desde otros puntos del dominio.

La continuidad sobre $[a,b]$ exige continuidad relativa en cada punto del intervalo; en los extremos equivale a continuidad desde el lado que pertenece al dominio. Una función puede ser continua a un lado y no al otro. Por ejemplo, para $f(x)=0$ cuando $x\le0$ y $f(x)=1$ cuando $x>0$, los límites laterales en $0$ difieren: no existe límite bilateral ni continuidad en ese punto.

**Proposición 0.2 (criterio secuencial de continuidad; `EDC-C00-PRP-002`).** Una función $f:D\to\mathbb R$ es continua en $a\in D$ si y sólo si para toda sucesión $x_n\in D$ con $x_n\to a$ se tiene $f(x_n)\to f(a)$.

**Demostración.** La dirección directa sigue aplicando la definición de continuidad a cada $x_n$ desde un índice suficientemente grande. Para la inversa, si la definición fallara, elegiríamos, para algún $\varepsilon_0>0$ y para cada $n$, un $x_n\in D$ con $|x_n-a|<1/n$ y $|f(x_n)-f(a)|\ge\varepsilon_0$, contradiciendo el supuesto. El argumento incluye puntos aislados. $\square$

**Proposición 0.3 (operaciones y composición; `EDC-C00-PRP-003`).** Sean $f,g:D\to\mathbb R$ continuas en $a\in D$. Entonces $f+g$ y $fg$ son continuas allí; si $g(a)\ne0$, la función $g$ no se anula en algún entorno relativo de $a$ y el cociente $f/g$ es continuo **en $a$**. Si $g:D\to E$ es continua en $a$ y $f:E\to\mathbb R$ es continua en $g(a)$, entonces $f\circ g$ es continua en $a$.

**Demostración.** Por el criterio secuencial, para cada $x_n\to a$ en $D$ se cumple $f(x_n)\to f(a)$ y $g(x_n)\to g(a)$. Aplicamos el Lema 0.1 a sumas, productos y cocientes. Si $g(a)\ne0$, la continuidad asegura $g(x)\ne0$ en un entorno relativo de $a$. Para la composición, $g(x_n)\to g(a)$ con términos en $E$, y la continuidad de $f$ da $f(g(x_n))\to f(g(a))$. Volvemos a aplicar el criterio secuencial. $\square$

Estas reglas permiten demostrar sin cálculo diferencial que los polinomios son continuos en toda la recta y las funciones racionales son continuas en los puntos de su dominio.

**Repertorio que encontraremos después.** Las potencias $x^m$ con $m\in\mathbb N$ son polinomios y su continuidad ya está justificada aquí. En cambio, al escribir $\sqrt{x}$ hay que exigir $x\ge0$, al escribir $\ln x$ hay que exigir $x>0$, y al escribir $x^r$ para $r\in\mathbb R$ arbitrario la base positiva evita problemas de definición. Las funciones $\exp x$, $\sin x$ y $\cos x$ se consideran en la recta real, pero no se empleará en este capítulo su continuidad como premisa no demostrada. Sus construcciones y los límites específicos que justifican sus reglas de derivación se presentarán en C02 o se reconstruirán explícitamente cuando el argumento los necesite. Distinguir **dominio**, **valor** y **comportamiento límite** es parte del método, no un detalle de notación.

## 0.5. Dos teoremas que hacen posible el cálculo

El nombre «continuidad» sugiere que la gráfica no rompe su recorrido. La primera consecuencia precisa esta imagen; la segunda garantiza que, bajo las hipótesis apropiadas, un máximo y un mínimo existen realmente. Ambas afirmaciones dependen de estar trabajando en intervalos reales y, de manera decisiva, de la completitud.

### 0.5.1. Valores intermedios

**Teorema 0.6 (valor intermedio; `EDC-C00-THM-006`).** Sean $a<b$ y $f:[a,b]\to\mathbb R$ continua. Si $y$ está estrictamente entre $f(a)$ y $f(b)$, existe $c\in(a,b)$ tal que $f(c)=y$.

**Demostración.** Podemos suponer $f(a)<y<f(b)$; el caso contrario se obtiene aplicando el argumento a $-f$. Consideremos

$$
A=\{x\in[a,b]:f(x)\le y\}.
$$

Contiene a $a$ y está acotado superiormente por $b$. Sea $c=\sup A$. Por la caracterización del supremo, para cada $n$ elegimos $x_n\in A$ con $c-1/n<x_n\le c$. Así, $x_n\to c$. Como $f$ es continua en $c$ y $f(x_n)\le y$, la preservación del orden al pasar al límite da $f(c)\le y$: si $f(c)>y$, la continuidad impondría $f(x_n)>y$ para $n$ suficientemente grande, contradiciendo $x_n\in A$.

Si $f(c)<y$, tenemos necesariamente $c<b$, pues $f(b)>y$. Por continuidad en $c$ podemos encontrar $\delta>0$ tal que $f(x)<y$ siempre que $x\in[a,b]$ y $|x-c|<\delta$. Elegimos $z$ con $c<z<\min\{b,c+\delta\}$. Entonces $z\in A$ y $z>c$, contradicción. Concluimos $f(c)=y$. Las desigualdades estrictas en los extremos obligan a $a<c<b$. $\square$

Hemos usado un hecho elemental sobre límites y orden: si $u_n\le y$ y $u_n\to u$, necesariamente $u\le y$; si no, la tolerancia $(u-y)/2$ produciría la contradicción. El valor intermedio no se extiende a una función meramente definida sobre racionales: la existencia de una frontera real puede ser exactamente lo que falta.

### 0.5.2. Valores extremos

**Teorema 0.7 (valores extremos; `EDC-C00-THM-007`).** Si $a<b$ y $f:[a,b]\to\mathbb R$ es continua, existen $u,v\in[a,b]$ tales que

$$
f(u)\le f(x)\le f(v)\qquad\text{para todo }x\in[a,b].
$$

En otras palabras, la función está acotada y alcanza su mínimo y su máximo.

**Demostración.** Primero demostraremos que $f$ es acotada. Si no lo fuera, podríamos elegir $x_n\in[a,b]$ con $|f(x_n)|>n$. Por Bolzano–Weierstrass, cierta subsucesión $x_{n_k}$ converge a $c\in[a,b]$ (el límite pertenece al intervalo cerrado). La continuidad de $f$ da $f(x_{n_k})\to f(c)$, sucesión necesariamente acotada. Pero $|f(x_{n_k})|>n_k\to\infty$, contradicción.

Sea ahora $M=\sup f([a,b])$, que existe porque la imagen es no vacía y acotada. Elegimos $x_n\in[a,b]$ con $M-1/n<f(x_n)\le M$. Una subsucesión $x_{n_k}$ converge a un punto $v\in[a,b]$; la continuidad implica $f(x_{n_k})\to f(v)$ y las desigualdades obligan a $f(v)=M$. Aplicando el mismo argumento a $-f$ obtenemos el mínimo. $\square$

**Contraejemplos que delimitan el teorema.** La función $x\mapsto1/x$ es continua en $(0,1]$, pero no está acotada: no podemos omitir el extremo $0$ y conservar la conclusión. Por otra parte, $f(0)=0$ y $f(x)=1/x$ para $x\in(0,1]$ define una función sobre $[0,1]$ que no está acotada ni es continua en $0$: tampoco podemos suprimir la continuidad. El teorema no afirma que todo extremo esté en el interior, ni que en un extremo deba existir una tangente horizontal.

### 0.5.3. Un control cuantitativo uniforme

La continuidad se define punto por punto: la distancia $\delta$ permitida puede depender de la posición $x$. En un intervalo cerrado y acotado sucede algo más fuerte, que será fundamental cuando las subdivisiones se hagan pequeñas.

**Teorema 0.8 (continuidad uniforme en $[a,b]$; `EDC-C00-THM-008`).** Si $f:[a,b]\to\mathbb R$ es continua y $a<b$, entonces

$$
\forall\varepsilon>0\;\exists\delta>0\;\forall x,y\in[a,b]:
\quad |x-y|<\delta\Longrightarrow |f(x)-f(y)|<\varepsilon.
$$

Aquí $\delta$ depende de $\varepsilon$ pero **no** del lugar $x$ ni del lugar $y$.

**Demostración.** Supongamos que no es uniformemente continua. Existiría $\varepsilon_0>0$ tal que, para cada $n$, podríamos elegir $x_n,y_n\in[a,b]$ con $|x_n-y_n|<1/n$ y $|f(x_n)-f(y_n)|\ge\varepsilon_0$. Por Bolzano–Weierstrass, alguna subsucesión $x_{n_k}$ converge a $c\in[a,b]$. La desigualdad triangular da

$$
|y_{n_k}-c|\le|y_{n_k}-x_{n_k}|+|x_{n_k}-c|\longrightarrow0.
$$

La continuidad en $c$ implica $f(x_{n_k})\to f(c)$ y $f(y_{n_k})\to f(c)$. Su diferencia debe tender a cero, en contradicción con la cota $\varepsilon_0$. $\square$

Ésta es la versión concreta, suficiente para nuestro propósito, de una propiedad que en un curso de análisis se estudiaría dentro de una teoría más amplia de la compacidad. No necesitaremos desarrollar esa teoría abstracta para justificar la integrabilidad de las funciones continuas en C05.

## 0.6. Las diferencias pequeñas no son diferencias nulas

Volvamos a la primera pregunta de §0.1. El cociente

$$
Q_h(a)=\frac{f(a+h)-f(a)}h,\qquad h\ne0,
$$

es una **tasa media de cambio** a lo largo de un incremento $h$. La tentación consiste en llamar instantánea a esa tasa «cuando $h=0$». Pero justamente allí la fórmula deja de tener sentido. La posibilidad correcta es investigar si $Q_h(a)$ tiene límite cuando $h\to0$, con $h\neq0$ y con los dos argumentos en el dominio de $f$.

En $f(x)=x^2$ obtuvimos $Q_h(a)=2a+h$. El límite existe. Para $f(x)=|x|$ en $a=0$, en cambio,

$$
Q_h(0)=\frac{|h|}{h}
=\begin{cases}1,&h>0,\\-1,&h<0.\end{cases}
$$

Las dos aproximaciones laterales son incompatibles. El dibujo de una punta no sustituye este cálculo: ahora tenemos una razón matemática por la cual no aparece una inclinación bilateral única.

Si pensamos en una posición $s(t)=t^2$ con $t\ge0$, la tasa media en un intervalo de duración $h>0$ es $2t+h$, y su límite por la derecha es $2t$. La unidad del cociente es «unidad de posición por unidad de tiempo»; las unidades de $s(t)$ y de $t$ no pueden confundirse. En $t=0$, además, el dominio físico impone una aproximación lateral, no una supuesta variación desde tiempos negativos.

El Capítulo 1 convertirá esta investigación en una definición y demostrará sus primeras consecuencias. Entonces podremos precisar con alcance general la palabra **derivada**.

## 0.7. Las sumas finitas no son todavía una integral

La otra pregunta de §0.1 se refiere a la acumulación. Para la parábola $f(x)=x^2$ en $[0,1]$, las sumas de rectángulos de extremos izquierdos son

$$
L_n=\frac1n\sum_{k=0}^{n-1}\left(\frac{k}{n}\right)^2
=\frac{(n-1)(2n-1)}{6n^2}.
$$

Puesto que $f$ es creciente en $[0,1]$, los rectángulos izquierdos quedan debajo de la curva y los derechos por encima. Las fórmulas dan

$$
R_n-L_n=\frac1n,
\qquad L_n\longrightarrow\frac13,\quad R_n\longrightarrow\frac13.
$$

Así, las dos aproximaciones geométricas encajan un mismo valor. Este argumento particular es mucho más instructivo que escribir prematuramente el símbolo de una integral: exhibe una cantidad de error concreta, $1/n$, y explica por qué se hace pequeña.

¿Bastaría repetir el procedimiento con cualquier función? No. Para verlo, primero precisamos un hecho aritmético.

**Lema 0.3 (densidad de racionales e irracionales; `EDC-C00-LEM-003`).** Todo intervalo abierto no vacío $(a,b)$ contiene un número racional y un número irracional.

**Demostración.** Por la propiedad arquimediana elegimos $n\in\mathbb N$ con $n(b-a)>1$. Existe un entero $m$ tal que $na<m\le na+1$ (el primer entero estrictamente mayor que $na$). Como $na+1<nb$, se obtiene $a<m/n<b$. La existencia del entero indicado se sigue de que los enteros no están acotados ni superior ni inferiormente, y de que en todo intervalo finito hay sólo un número finito de enteros; para elegir el menor de los que superan $na$ basta acotarlos primero entre dos enteros de gran valor absoluto. Hemos hallado un racional. Para el irracional aplicamos la primera parte al intervalo $(a-\sqrt2,b-\sqrt2)$, obteniendo un racional $q$; entonces $q+\sqrt2\in(a,b)$ y es irracional. $\square$

Definamos $d:[0,1]\to\mathbb R$ mediante

$$
d(x)=\begin{cases}1,&x\in\mathbb Q,\\0,&x\notin\mathbb Q.\end{cases}
$$

Dividamos $[0,1]$ en cualquier número finito de intervalos de anchura positiva. En cada uno podemos escoger como muestra un racional, y la suma de alturas por anchuras será exactamente $1$. Pero podemos escoger muestras irracionales en todos ellos, y la suma resultante será $0$. Las subdivisiones pueden hacerse arbitrariamente finas y la divergencia permanece. **No existe un valor común forzado por estas aproximaciones.**

En C04 estudiaremos la lógica de las cuadraturas y en C05 definiremos las sumas superiores e inferiores de Darboux y estableceremos cuándo determinan una integral. No necesitamos adelantar aquí esa definición, pero ya conocemos el obstáculo al que tendrá que responder.

Hay, además, una coincidencia sugerente para la parábola. Definamos la función polinómica $F(x)=x^3/3$. Para $h\neq0$,

$$
\frac{F(x+h)-F(x)}h=x^2+xh+\frac{h^2}3\longrightarrow x^2.
$$

La función $F$ tiene, en este sentido todavía exploratorio, una tasa de cambio vinculada con las alturas $x^2$ cuyas sumas rectangulares estudiamos. Esta correspondencia particular invita a preguntar por una relación universal entre acumulación y variación. Pero **no hemos demostrado todavía** que toda función admita una acumulación bien definida ni que tal acumulación posea una tasa de cambio recuperable. El Teorema Fundamental del Cálculo de C06 dará la respuesta dentro de hipótesis explícitas.

## 0.8. Un puente histórico y el camino que sigue

Los problemas de cuadratura y los de tangentes no son invenciones de un curso moderno de cálculo. La cuadratura de regiones curvilíneas cuenta con antecedentes antiguos, entre ellos el estudio de Arquímedes del segmento parabólico. En la matemática europea de los siglos XVI y XVII se desarrollaron asimismo procedimientos para tangentes, cuadraturas y magnitudes variables; Newton y Leibniz fueron decisivos para articular parte de esas investigaciones en métodos generales, aunque con conceptos y lenguajes distintos de los actuales. Estas formulaciones son deliberadamente prudentes: los testimonios, las dataciones y las diferencias entre métodos se registran en las [notas históricas](capitulo-00-notas.html), no se deducen del álgebra moderna que acabamos de escribir.

La organización de este libro no pretende reconstruir una sucesión lineal de descubrimientos. Empezamos por el límite porque es una herramienta de **justificación** especialmente clara para el lector actual; históricamente muchas cuadraturas, procedimientos de tangentes y desarrollos en serie precedieron a las definiciones rigurosas que hoy usamos para evaluarlos. No debemos atribuir retrospectivamente una demostración con $\varepsilon$ y $\delta$ a quien operaba con agotamiento geométrico, indivisibles, fluxiones u otros recursos. La historia ilumina por qué fueron necesarias ciertas ideas, pero las demostraciones que siguen son nuestras y pertenecen a la matemática contemporánea.

El lector cuenta ahora con una cadena de resultados autónoma:

$$
\text{completitud de }\mathbb R
\Longrightarrow
\begin{cases}
\text{principio arquimediano y convergencia monótona},\\
\text{intervalos encajados y Bolzano--Weierstrass}
\end{cases}
\Longrightarrow
\begin{cases}
\text{valor intermedio},\\
\text{valores extremos},\\
\text{continuidad uniforme en }[a,b].
\end{cases}
$$

El capítulo siguiente vuelve al primer problema: del cociente incremental a la derivada. El segundo arco, que comienza en C04, partirá de sumas finitas para definir la integral. En C06 las dos trayectorias se reunirán. Sólo entonces podremos afirmar, con demostración y bajo condiciones establecidas, cómo el cambio local y la acumulación se relacionan.

### Mapa de dependencias y lecturas de trabajo

- **Fundamento adoptado:** axiomas de cuerpo ordenado y completitud de $\mathbb R$, aritmética de $\mathbb N$ e identidades algebraicas finitas. No se utiliza derivación, integración, Taylor, teorema de Rolle ni Teorema Fundamental.
- **Resultados derivados:** `EDC-C00-THM-001` → `EDC-C00-THM-002` y `EDC-C00-THM-003` → `EDC-C00-THM-004`; `EDC-C00-THM-005` y `EDC-C00-PRP-002` permiten transportar límites/continuidad; `EDC-C00-THM-006--008` requieren continuidad y completitud en intervalos cerrados de la recta.
- **Uso posterior:** C01 y C02 usarán límites y continuidad; C03, valores extremos; C04–C05, completitud, extremos y continuidad uniforme; C06, lo anterior junto con la teoría diferencial e integral ya construida.
- **Lecturas complementarias:** Gabor Toth, *Elements of Mathematics* (2021), lectura previa o paralela recomendada; otras fuentes históricas documentadas en [Notas históricas del capítulo 0](capitulo-00-notas.html). Ninguna de estas lecturas es requisito para validar las demostraciones presentes.

**Trabajo del lector.** Los [ejercicios de este capítulo](capitulo-00-ejercicios.html) desarrollan la lectura precisa de cuantificadores, la búsqueda de contraejemplos, el uso de completitud y la interpretación de sumas y cocientes. Sus desarrollos completos están separados en [soluciones](capitulo-00-soluciones.html) para no interrumpir la exposición.
