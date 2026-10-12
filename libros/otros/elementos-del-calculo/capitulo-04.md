---
title: Capítulo 4. Cuadraturas y el desafío del área
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
      note: 'Inspiración metodológica: Gabor Toth, Elements of Mathematics (2021); obra independiente.'
source-id: EDC-C04
source-sha256: 6565070ce85499b4e733be09e165f378c81caf1540b6286b79c06bff6cb4f832
content-id: MA-BCH-0335
content-type: book-chapter
related:
  - MA-BOK-0015
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-04.html) · [Ejercicios](capitulo-04-ejercicios.html) · [Soluciones](capitulo-04-soluciones.html) · [Notas históricas](capitulo-04-notas.html)

[← Capítulo 3](capitulo-03.html) · [Capítulo 5 →](capitulo-05.html)

> **Pregunta generadora.** Sabemos calcular exactamente el área de un triángulo y de un rectángulo. ¿Cómo asignar un valor justificado a una región de contorno curvo, de tal manera que distintas aproximaciones geométricas no produzcan respuestas incompatibles?

El capítulo anterior examinó cómo un cálculo local de pendientes adquiere fuerza global mediante el teorema del valor medio. Ahora seguimos otro camino. Antes de poder relacionar áreas y derivadas hay que plantear el problema del área en sus propios términos. Un polígono se descompone en triángulos; una región limitada por una parábola no queda, en general, dividida exactamente por una cantidad finita de figuras rectilíneas. El trabajo decisivo consistirá en **construir cotas que se acerquen tanto como queramos** y explicar qué propiedad de los números reales vuelve inteligible esa aproximación.

El ejemplo central será la cuadratura de un segmento parabólico: una reconstrucción algebraico-geométrica moderna de un resultado documentado en *La cuadratura de la parábola* de Arquímedes. No fingiremos que Arquímedes escribía nuestras ecuaciones ni que nuestro argumento es una transcripción de su demostración. Después compararemos polígonos, rectángulos y sumas finitas, hasta llegar al problema que resolverá el capítulo 5: cómo definir **la integral de una función general** y comprobar que las distintas elecciones de aproximaciones determinan un mismo valor.

## 4.1. Cuadrar una región: qué se busca exactamente

**Definición 4.1 (`EDC-C04-DEF-001`; cuadratura en sentido geométrico).** Dada una región plana a la que se haya asignado un área, su *cuadratura* consiste en determinar un cuadrado —o una figura rectilínea de área conocida— con la misma área. La palabra no significa necesariamente obtener una primitiva, escribir una integral o construir un cuadrado con regla y compás bajo restricciones que habría que especificar aparte.

Tomamos como propiedades geométricas previas la fórmula del área de un rectángulo de lados positivos, $A=bh$; la del triángulo, $A=bh/2$; la aditividad para uniones finitas de polígonos de interiores disjuntos; y la monotonía: si un polígono está contenido en otro, el área del primero no supera la del segundo. Los argumentos de este capítulo se basan en estas reglas finitas y en los límites y desigualdades establecidos en C00. Todavía **no** adoptamos una función general de área para toda región curva.

La exigencia de monotonía implica una estrategia: si $P$ es una figura poligonal interior y $Q$ una figura poligonal exterior a una región $\mathcal R$, cualquier área $A(\mathcal R)$ compatible con las reglas geométricas debe cumplir

$$
A(P)\le A(\mathcal R)\le A(Q).
$$

Esta desigualdad es una condición sobre un eventual valor de área, no una prueba de que dicho valor exista. Confundir ambas afirmaciones supondría introducir silenciosamente lo que todavía queremos construir. De hecho, para una función arbitraria, diferentes familias de rectángulos pueden resistirse a determinar un valor común.

**Observación de unidades.** Una longitud tiene unidades de $L$; una superficie, de $L^2$. Si multiplicamos ambas coordenadas por un factor $c>0$, el área de un polígono se multiplica por $c^2$. En cambio, una transformación que sólo estire la coordenada horizontal por $c$ multiplica áreas por $c$. La dimensionalidad será una comprobación rápida de nuestras fórmulas.

## 4.2. El agotamiento: una dificultad siempre menor que otra

En lugar de esperar que una descomposición termine después de un número fijo de pasos, podemos pedir que **el resto sea menor que cualquier tolerancia positiva**. El principio es aritmético antes que geométrico.

**Lema 4.1 (`EDC-C04-LEM-001`; agotamiento geométrico).** Sean $R_0>0$ y $0<q<1$. Si una sucesión de restos no negativos satisface $R_n\le R_0q^n$ para todo $n\ge0$, entonces, para cada $\varepsilon>0$, existe $N$ tal que $R_n<\varepsilon$ para $n\ge N$.

**Demostración.** Pongamos $t=q^{-1}>1$. Por la desigualdad binomial, $t^n=(1+(t-1))^n\ge1+n(t-1)$ para $n\ge1$. Así,

$$
0\le R_n\le\frac{R_0}{1+n(t-1)}\longrightarrow0
$$

por el principio arquimediano (`EDC-C00-THM-001`). La definición de límite proporciona $N$. $\square$

En geometría antigua, una reducción reiterada del resto a una parte suficientemente pequeña permitió fundamentar comparaciones de magnitudes sin recurrir a una suma infinita como operación previamente definida. **No afirmamos** que el lema anterior sea la escritura literal de Euclides o Arquímedes: expresa en lenguaje de sucesiones una lógica afín a la del agotamiento. La Proposición X.1 de los *Elementos* de Euclides formula una disminución repetida de una magnitud hasta que el residuo resulta menor que otra magnitud dada; véanse las [notas históricas H1](capitulo-04-notas.html).

**Proposición 4.1 (`EDC-C04-PRP-001`; unicidad por encaje).** Sean $L_n\le U_n$ números reales para cada $n\ge1$, y supongamos que $U_n-L_n\to0$. Si dos números $A,B$ satisfacen $L_n\le A,B\le U_n$ para todo $n$, entonces $A=B$.

**Demostración.** Para cada $n$, $|A-B|\le U_n-L_n$. Si $|A-B|>0$, el límite nulo de la derecha contradice la desigualdad para $n$ suficientemente grande. $\square$

El enunciado sólo demuestra **unicidad condicional**. Una sucesión de intervalos de extremos cualesquiera y anchura decreciente podría desplazarse sin contener un punto fijo. Para probar existencia de un candidato se necesita información adicional (por ejemplo, intervalos encajados, como en C00, o compatibilidad de refinamientos, que examinaremos en C05).

## 4.3. El segmento parabólico y el triángulo fundamental

Consideremos $a<b$ y $k>0$. Entre la cuerda horizontal $y=0$ y el arco de la parábola

$$
f(x)=k(x-a)(b-x),\qquad a\le x\le b,
$$

queda una región convexa hacia arriba respecto de la cuerda (la gráfica, por ser cóncava, está encima de ella). Escribir $\ell=b-a$ permite reconocer

$$
f(x)=k\left[\frac{\ell^2}{4}-\left(x-\frac{a+b}{2}\right)^2\right].
$$

La altura máxima es $H=k\ell^2/4$, alcanzada en el punto medio $m=(a+b)/2$. Construimos el triángulo con vértices $(a,0)$, $(m,H)$ y $(b,0)$. Su área, calculable sin conocer aún el área de la región curva, es

$$
T=\frac{\ell H}{2}=\frac{k\ell^3}{8}.
$$

Esta figura no agota el segmento: a la izquierda y a la derecha del vértice quedan dos regiones curvilíneas menores. Cada una vuelve a ser un segmento parabólico, esta vez situado **entre su arco y la cuerda oblicua** que une dos vértices consecutivos del primer triángulo.

**Lema 4.2 (`EDC-C04-LEM-002`; diferencia con la cuerda).** Sea $f(x)=Ax^2+Bx+C$ con $A<0$, y sea $\ell_{u,v}(x)$ la recta secante que interpola $f$ en $u<v$. Entonces

$$
f(x)-\ell_{u,v}(x)=(-A)(x-u)(v-x),\qquad u\le x\le v.
$$

El triángulo con base sobre la cuerda $[(u,f(u)),(v,f(v))]$ y vértice en la gráfica sobre el punto medio tiene área $(-A)(v-u)^3/8$, calculada como base horizontal por altura vertical dividida por dos.

**Demostración.** La diferencia $f-\ell_{u,v}$ es un polinomio de grado dos con coeficiente principal $A$ y ceros $u,v$. Luego vale $A(x-u)(x-v)=(-A)(x-u)(v-x)$. La separación vertical máxima respecto de la cuerda se encuentra en el punto medio y vale $(-A)(v-u)^2/4$. La fórmula del triángulo sigue porque el determinante que calcula su área es anchura horizontal por separación vertical, incluso si la cuerda es oblicua. $\square$

**Teorema 4.1 (`EDC-C04-THM-001`; disminución de triángulos parabólicos).** Cuando una cuerda de longitud horizontal $d$ se divide en sus dos mitades y en cada subsegmento se inscribe el triángulo correspondiente, el área de **cada** nuevo triángulo es $1/8$ del área del triángulo construido sobre la cuerda original; el área total añadida por la pareja es $1/4$ de la anterior.

**Demostración.** Por el Lema 4.2, el área del triángulo sobre una subcuerda de anchura horizontal $d/2$ es $k(d/2)^3/8=(1/8)(kd^3/8)$, donde $k=-A>0$. Hay dos subcuerdas y sus interiores no se solapan, de modo que el total es dos veces esa área. $\square$

La recurrencia explica por qué **aparece la razón $1/4$**; no es un número adivinado por la suma de una serie. A cada generación se agregan $2^n$ triángulos, cada uno de área $T/8^n$, por lo que el área total de la generación $n$ es $T/4^n$.

<figure id="fig-edc-c04-01" class="quarto-float-fig">
<img src="/assets/books/elementos-del-calculo/EDC-C04-F01_AGOTAMIENTO_PARABOLA.svg" alt="Parábola cóncava y=4x(1−x) entre cero y uno, triángulo inscrito inicial T y dos triángulos añadidos de área T/8 cada uno.">
<figcaption>Figura 4.1. Dos nuevas piezas suman T/4. El agotamiento se completa con una cota poligonal del resto, no solamente mediante el dibujo.</figcaption>
</figure>



## 4.4. Una suma finita y un resto geométrico explícito

Tras construir las generaciones $0,1,\ldots,n-1$ (con $n\ge1$), obtenemos un polígono inscrito de área

$$
P_n=T\sum_{j=0}^{n-1}4^{-j}
=\frac{4T}{3}\bigl(1-4^{-n}\bigr).
$$

La última identidad es **finita** y se verifica multiplicando por $1-1/4$: la mayoría de los términos se cancelan. Por tanto,

$$
\frac{4T}{3}-P_n=\frac{4T}{3\cdot4^n}>0.
$$

Este cálculo todavía no identifica el área curvilínea. Para ello debemos demostrar que lo que permanece fuera del polígono se puede **dominar por figuras de área explícita**.

**Lema 4.3 (`EDC-C04-LEM-003`; cobertura del resto).** En la configuración del §4.3, después de $n$ generaciones el conjunto que queda entre el arco parabólico y el polígono inscrito puede cubrirse con un número finito de franjas de lados verticales, cada una situada entre una cuerda y una paralela superior, cuya suma de áreas es

$$
B_n=\frac{k\ell^3}{4^{n+1}}=\frac{2T}{4^n}.
$$

**Demostración.** Las cuerdas no cubiertas corresponden a los $2^n$ subintervalos horizontales de igual longitud $d=\ell/2^n$. En cada uno, el Lema 4.2 limita la separación vertical entre curva y cuerda por $kd^2/4$. La franja correspondiente es un paralelogramo de base horizontal $d$ y altura vertical $kd^2/4$; tiene área $kd^3/4$. Sus proyecciones horizontales son disjuntas salvo extremos, por lo que la suma de sus áreas es

$$
2^n\frac{k(\ell/2^n)^3}{4}
=\frac{k\ell^3}{4\cdot4^n}=\frac{2T}{4^n}.
$$

Los restos curvos están contenidos en estas franjas; no hemos necesitado asignarles un área previa. $\square$

**Contrato de área por agotamiento (MAT-03).** Para **este segmento parabólico particular**, un *valor de área compatible* significa un número real $A$ que satisface $P_n\le A\le P_n+B_n$ **para cada entero $n\ge1$**, donde $P_n$ es el área del polígono interior de la generación correspondiente y $B_n$ la suma de áreas de las cubiertas exteriores del Lema 4.3. La comparación se funda en inclusiones de regiones y áreas poligonales finitas. No hemos definido todavía un funcional de área para **todas** las regiones curvas. El objetivo inmediato es demostrar que estos encerramientos concretos poseen **un único número compatible**; si una noción geométrica previa de área respeta la inclusión y coincide con las áreas poligonales, tendrá forzosamente ese valor para el segmento. La integral general será construida independientemente en C05 mediante todas las particiones y las sumas de Darboux.

**Teorema 4.2 (`EDC-C04-THM-002`; cuadratura del segmento parabólico).** Para un segmento parabólico de la forma descrita en §4.3, la construcción de polígonos interiores y exteriores determina un único valor compatible de área, **en el sentido definido arriba**, y éste es

$$
\boxed{A=\frac43T=\frac{k(b-a)^3}{6}.}
$$

**Demostración.** El polígono inscrito tiene área $P_n$ y el polígono obtenido añadiendo las franjas superiores tiene área a lo sumo $P_n+B_n$. Es decir, cualquier valor compatible debe quedar, para todo $n\ge1$, entre

$$
L_n=\frac{4T}{3}\bigl(1-4^{-n}\bigr)
\quad\text{y}\quad
U_n=L_n+\frac{2T}{4^n}.
$$

El número $A_0=4T/3$ pertenece realmente a cada intervalo: $A_0-L_n=4T/(3\cdot4^n)$ y $U_n-A_0=2T/(3\cdot4^n)$, ambos no negativos. Con ello queda demostrada **la existencia** de un valor compatible para los encerramientos explícitos. Además $U_n-L_n=2T/4^n\to0$ por el Lema 4.1. La Proposición 4.1 obliga a que **todo** valor compatible sea $A_0$, demostrando **la unicidad**. Estos dos pasos determinan el valor de cuadratura **de este segmento**; no pretenden construir todavía el área de todas las regiones curvas ni una integral general. $\square$

No hemos inferido el resultado por la sola igualdad de una serie infinita. Hemos identificado un candidato, construido una sucesión de polígonos y dado una cota explícita de la región no cubierta. En lenguaje actual esto es un **argumento de agotamiento con control del error**. Las bases oblicuas de las generaciones intermedias no alteran la demostración, porque el Lema 4.2 mide la separación vertical entre la parábola y cada cuerda y las áreas se calculan mediante determinantes de triángulos y paralelogramos.

La fórmula se extiende a todo arco de parábola que sea la gráfica de un polinomio cuadrático estrictamente cóncavo sobre $[a,b]$, tomando como base la cuerda que une sus extremos. La diferencia entre arco y cuerda es precisamente la función cuadrática positiva del Lema 4.2.

## 4.5. Arquímedes: descubrimiento, prueba y reconstrucción

La *Cuadratura de la parábola* reúne procedimientos mecánicos y geométricos y culmina, en su Proposición 24, con el resultado de los cuatro tercios del triángulo inscrito. La versión que acabamos de demostrar utiliza coordenadas cartesianas, polinomios, índices $n$ y límites; no es una reconstrucción literal de los argumentos del siglo III a. C. Su valor didáctico reside en hacer visibles la recurrencia de las áreas, la fórmula finita y el error que puede hacerse arbitrariamente pequeño.

La introducción de la obra, conservada en traducción inglesa reproducida por MacTutor, presenta a Arquímedes describiendo una búsqueda inicialmente motivada por medios mecánicos y posteriormente justificada geométricamente. El contexto está documentado en [H2](capitulo-04-notas.html), sin convertir esa traducción accesible en una colación del texto griego.

Es importante no confundir **justificación de una cuadratura particular** con una teoría de área aplicable a cualquier función. El éxito con la parábola no garantiza que las aproximaciones de todas las regiones curvilíneas sean convergentes o que el valor obtenido sea independiente del procedimiento de muestreo.

::: {.callout-note appearance="simple" icon="false" collapse="false" title="Historia — Arquímedes: el área que faltaba"}

*Lectura opcional.*

Dibujar un triángulo dentro de una parábola es fácil. Lo fascinante comienza cuando nos preguntamos cuánto del área queda afuera y si podemos recuperar ese resto añadiendo nuevos triángulos.

Arquímedes encontró una respuesta extraordinaria: el segmento parabólico tiene un área igual a cuatro tercios de la del triángulo con la misma base y altura. En la carta a Dositeo que acompaña la Cuadratura de la parábola cuenta que llegó al resultado mediante consideraciones mecánicas y después lo demostró geométricamente. La imaginación y la prueba participaron en el descubrimiento.

La construcción de este capítulo permite sentir la fuerza de esa idea. Cada nueva generación de triángulos ocupa parte de lo que faltaba; el hueco disminuye siguiendo una pauta. Podemos acercarnos al área exacta y, además, saber cuánto queda por recuperar. Un problema antiguo se vuelve así una lección muy viva sobre aproximación.

**Para seguir leyendo:** [Arquímedes, carta a Dositeo, traducción reproducida en MacTutor](https://mathshistory.st-andrews.ac.uk/Extras/Archimedes_parabola/).

:::

## 4.6. De los triángulos a las sumas de rectángulos

Consideremos ahora una función no negativa $f:[a,b]\to\mathbb R$ y una subdivisión finita

$$
a=x_0<x_1<\cdots<x_n=b,
\qquad\Delta_i=x_i-x_{i-1}>0.
$$

**Definición 4.2 (`EDC-C04-DEF-002`; subdivisión y finura).** La lista ordenada anterior es una *partición finita* de $[a,b]$. Su **finura** es $\|P\|=\max_i\Delta_i$. Para muestras $\xi_i\in[x_{i-1},x_i]$, la expresión

$$
S(P,\xi;f)=\sum_{i=1}^{n}f(\xi_i)\Delta_i
$$

es una suma finita de áreas de rectángulos. Todavía no definimos su límite general ni llamamos integral a ese límite.

Cuando $f$ es creciente, la suma con muestras izquierdas es una aproximación inferior y la de muestras derechas una superior. Para $f(x)=x^2$ sobre $[0,1]$ con $x_i=i/n$ obtenemos los números ya encontrados en C00:

$$
L_n=\frac1n\sum_{k=0}^{n-1}\left(\frac{k}{n}\right)^2
=\frac13-\frac1{2n}+\frac1{6n^2},
$$

$$
R_n=\frac1n\sum_{k=1}^{n}\left(\frac{k}{n}\right)^2
=\frac13+\frac1{2n}+\frac1{6n^2}.
$$

Ambos se acercan a $1/3$, y $R_n-L_n=1/n$. Desde el punto de vista de la cuadratura, tenemos una **horquilla numérica** cuyas dos ramas se aproximan. Pero un razonamiento de este tipo, construido sólo con extremos de subintervalos, es específico de una función monótona.

**Proposición 4.2 (`EDC-C04-PRP-002`; control para $x^2$ sin partición uniforme).** Sea $P$ cualquier partición de $[0,1]$ con finura $\|P\|$. Las sumas rectangulares con extremos izquierdos y derechos, respectivamente $L(P)$ y $U(P)$, cumplen

$$
0\le U(P)-L(P)\le\|P\|.
$$

**Demostración.** Como $x^2$ es creciente en $[0,1]$,

$$
U(P)-L(P)
=\sum_{i=1}^n(x_i^2-x_{i-1}^2)\Delta_i
\le\|P\|\sum_{i=1}^n(x_i^2-x_{i-1}^2)
=\|P\|.
$$

No se ha utilizado una fórmula integral; el último paso es una suma telescópica finita. $\square$

La proposición elimina una dependencia artificial de particiones uniformes. Si la finura tiende a cero, la diferencia de las dos sumas tiende a cero, aunque haya muchas longitudes distintas. La existencia e independencia del valor límite para **todas** las selecciones de muestras se formalizará en C05.

## 4.7. Un laboratorio finito para las potencias

La relación entre cuadrados, cubos y sumas rectangulares permite un resultado sorprendente sin emplear integral. Está disponible el teorema del valor medio de C03; lo aplicaremos a una función algebraica sobre intervalos pequeños.

**Teorema 4.3 (`EDC-C04-THM-003`; cuadratura numérica de potencias enteras).** Para cada entero $p\ge1$, definamos las sumas uniformes

$$
L_{n,p}=\frac1n\sum_{k=0}^{n-1}\left(\frac kn\right)^p,
\qquad
U_{n,p}=\frac1n\sum_{k=1}^{n}\left(\frac kn\right)^p.
$$

Entonces

$$
L_{n,p}\le\frac1{p+1}\le U_{n,p},\qquad
U_{n,p}-L_{n,p}=\frac1n,
$$

así que ambas sucesiones convergen a $1/(p+1)$.

**Demostración.** Tomemos $F(x)=x^{p+1}/(p+1)$; por C02, $F'(x)=x^p$. En cada subintervalo $[(k-1)/n,k/n]$, el teorema del valor medio (`EDC-C03-THM-003`) proporciona $\xi_k$ interior con

$$
F(k/n)-F((k-1)/n)=\frac1n\xi_k^p.
$$

La función $x^p$ es creciente en $[0,1]$, de modo que el término de la derecha está entre $((k-1)/n)^p/n$ y $(k/n)^p/n$. Sumamos para $k=1,\ldots,n$: el lado izquierdo telescopa a $F(1)-F(0)=1/(p+1)$. Finalmente,

$$
U_{n,p}-L_{n,p}
=\frac1n\left[\sum_{k=1}^n(k/n)^p-\sum_{k=0}^{n-1}(k/n)^p\right]
=\frac1n.
$$

Por encajonamiento, ambas sucesiones convergen al valor anunciado. $\square$

Éste es un **resultado especial sobre sumas finitas**, obtenido del valor medio y de la fórmula de derivación de potencias ya demostradas. No es todavía el Teorema Fundamental del Cálculo: no se ha introducido la integral general, ni probado que toda derivada determine de este modo un área, ni decidido qué funciones admiten cuadratura por sumas.

La conexión entre potencias y cuadraturas reapareció históricamente en el siglo XVII mediante procedimientos diferentes, entre ellos los indivisibles de Cavalieri. No atribuyamos al matemático italiano la demostración moderna que acabamos de escribir.

## 4.8. Rectángulos, trapecios y precisión

La elección de muestras no es indiferente si una subdivisión tiene anchura positiva. En $[0,1]$ para $f(x)=x^2$, además de $L_n$ y $R_n$ podemos usar trapecios y puntos medios:

$$
T_n=\frac{L_n+R_n}{2}=\frac13+\frac1{6n^2},
$$

$$
M_n=\frac1n\sum_{k=1}^{n}
\left(\frac{k-1/2}{n}\right)^2
=\frac13-\frac1{12n^2}.
$$

Las identidades son sumas finitas: al expandir $(k-1/2)^2$ usamos las fórmulas de $\sum k$ y $\sum k^2$. Ambas aproximaciones comparten el valor $1/3$, pero sus errores frente a ese candidato son de orden $1/n^2$, más pequeños que los errores $1/n$ que se obtienen, como cotas generales, al comparar sumas por extremos.

**Proposición 4.3 (`EDC-C04-PRP-003`; trapecios y convexidad).** Si $f:[a,b]\to\mathbb R$ es convexa, entonces en cada subintervalo $[u,v]\subset[a,b]$ el segmento recto que une $(u,f(u))$ y $(v,f(v))$ queda por encima de la gráfica. Si $f$ es cóncava, ocurre la desigualdad inversa.

**Demostración.** Para $x=(1-t)u+tv$ con $0\le t\le1$, la definición de convexidad (`EDC-C03`) da

$$
f(x)\le(1-t)f(u)+tf(v),
$$

que es precisamente la ordenada de la cuerda en $x$. La concavidad invierte la desigualdad. $\square$

La comparación no autoriza a sustituir sin más una suma de trapecios por un área exacta para toda función convexa. Las cuerdas construyen una aproximación geométrica determinada y el control del error requiere todavía argumentar sobre su diferencia con la curva. El caso cuadrático, donde la diferencia con la cuerda se calcula exactamente, es un ejemplo especialmente transparente.

## 4.9. La continuidad y un error común a todas las subdivisiones

Si $f$ es continua sobre el intervalo cerrado $[a,b]$, el teorema de valores extremos (`EDC-C00-THM-007`) garantiza, en cada subintervalo $[x_{i-1},x_i]$, un mínimo $m_i$ y un máximo $M_i$. Construyamos dos figuras rectangulares con áreas finitas

$$
A_-(P)=\sum_{i=1}^n m_i\Delta_i,
\qquad
A_+(P)=\sum_{i=1}^n M_i\Delta_i.
$$

Si $f\ge0$, pueden leerse como rectángulos interiores y exteriores a la región bajo la gráfica. Para funciones con valores negativos, estas expresiones conservan sentido algebraico como sumas, pero la lectura como áreas ordinarias requiere separar las partes o trasladar verticalmente la gráfica.

**Teorema 4.4 (`EDC-C04-THM-004`; estimación preparatoria).** Sea $f:[a,b]\to\mathbb R$ continua, con $a<b$. Para todo $\varepsilon>0$ existe $\delta>0$ tal que cualquier partición finita $P$ de $[a,b]$ con $\|P\|<\delta$ satisface

$$
0\le A_+(P)-A_-(P)<\varepsilon.
$$

**Demostración.** Por continuidad uniforme de $f$ en $[a,b]$ (`EDC-C00-THM-008`), para la tolerancia $\eta=\varepsilon/[2(b-a)]$ existe $\delta>0$ tal que $|f(x)-f(y)|<\eta$ si $|x-y|<\delta$. Si $\|P\|<\delta$, los puntos donde se alcanzan $m_i$ y $M_i$ pertenecen a un mismo subintervalo de longitud menor que $\delta$. Por tanto $0\le M_i-m_i<\eta$ y

$$
0\le A_+(P)-A_-(P)
=\sum_{i=1}^n(M_i-m_i)\Delta_i
<\eta\sum_{i=1}^n\Delta_i
=\frac{\varepsilon}{2}<\varepsilon.
$$

$\square$

Hemos obtenido una cota que funciona **para todas las particiones suficientemente finas**, no sólo para subdivisiones uniformes. Sin embargo, todavía no hemos definido las integrales inferior y superior, ni demostrado la compatibilidad de sumas correspondientes a **dos particiones distintas**, ni formulado una teoría completa de integrabilidad. Hacer esos tres trabajos explícitos será la misión de C05. El teorema anterior constituye la preparación matemática central.

## 4.10. Cavalieri y el problema de los indivisibles

En el siglo XVII, los procedimientos de *indivisibles* permitieron comparar figuras por colecciones de secciones paralelas y formular cuadraturas que podían resultar difíciles de obtener por agotamiento geométrico. La obra *Geometria indivisibilibus continuorum nova quadam ratione promota* de Bonaventura Cavalieri apareció publicada en 1635. La historiografía registra tanto su fecundidad como objeciones acerca de qué significaba considerar una superficie en términos de «todas sus líneas».

Hay que distinguir tres afirmaciones:

1. Es correcto calcular el área de un rectángulo con base por altura.
2. Es tentador imaginar una superficie como una colección de líneas paralelas de espesor nulo.
3. **No se deduce** de lo anterior que cualquier colección arbitraria de líneas tenga, por simple suma informal, un área bien definida.

En la geometría elemental, los polígonos pueden seccionarse y sus áreas compararse por descomposiciones finitas. Para regiones curvas, la comparación entre secciones exige reglas adicionales y una teoría de aproximación. Cavalieri no puede reducirse a una simple aplicación del teorema de Fubini, que aún no existe dentro de nuestra obra. La relación histórica y los límites de nuestra reconstrucción se documentan en [H4](capitulo-04-notas.html).

::: {.callout-note appearance="simple" icon="false" collapse="false" title="Historia — Cavalieri: mirar un sólido rebanada por rebanada"}

*Lectura opcional.*

Imaginemos dos panes de formas distintas. Los cortamos a la misma altura y comparamos sus rebanadas. Si en cada nivel las secciones tienen la misma área, resulta tentador pensar que los panes contienen el mismo volumen.

Esta manera de mirar las figuras nos acerca a Cavalieri y a su Geometria indivisibilibus, publicada en 1635. En lugar de examinar sólo el contorno de una región o de un sólido, sus métodos dirigían la atención hacia las secciones que lo atraviesan.

La imagen es muy fecunda para aprender a integrar. Un corte nos informa sobre un nivel; reunir la información de muchos niveles permite estudiar el conjunto. Los rectángulos de nuestras sumas desempeñan un papel parecido: cada uno representa una pequeña contribución. Al comparar y reunir esas contribuciones, vamos pasando del perfil de una figura a la magnitud que encierra.

**Para seguir leyendo:** [Notas históricas del capítulo 4, apartado H4](capitulo-04-notas.html).

:::

## 4.11. El obstáculo: dos familias de rectángulos incompatibles

La función de Dirichlet, ya usada en C00, vale $1$ en los racionales y $0$ en los irracionales de $[0,1]$. Cada subintervalo no degenerado contiene tanto unos como otros. Por consiguiente, dada **cualquier** partición finita, podemos escoger las muestras de manera que la suma rectangular sea siempre $1$ o siempre $0$.

Que las particiones sean cada vez más finas no remedia la ambigüedad. Este ejemplo muestra que no basta escribir $S(P,\xi;f)$ y hacer tender $\|P\|$ a cero sin especificar qué significa convergencia **independiente de particiones y muestras**. El teorema preparatorio del §4.9 revela por qué las funciones continuas no presentan la misma dificultad; el contraejemplo explica por qué esa hipótesis no puede reemplazarse por «estar acotada» sin más.

## 4.12. Dos tradiciones y una pregunta que queda abierta

La cuadratura por triángulos y agotamiento, ejemplificada por Arquímedes, y los procedimientos de rectángulos y secciones, que pueden reconstruirse mediante sumas finitas, comparten una preocupación: calcular áreas curvilíneas controlando aproximaciones. Pero no son idénticos como prácticas históricas ni implican automáticamente una única definición moderna.

Hemos demostrado resultados particulares: el valor de cuatro tercios en un segmento parabólico, varias fórmulas de sumas rectangulares, una cota independiente de la subdivisión para $x^2$ y un control uniforme del error entre rectángulos extremos cuando $f$ es continua. Lo pendiente es elevar esas observaciones a un concepto general que tenga un dominio de aplicación, un criterio de existencia y propiedades demostradas.

En el capítulo 5 estableceremos el significado preciso de *integrabilidad de Riemann–Darboux*. Sólo después, en el capítulo 6, estudiaremos por qué el problema de la acumulación y el problema de la derivada se unen en el Teorema Fundamental del Cálculo. No hemos invocado ninguno de esos teoremas para resolver la cuadratura de hoy.

### Mapa de dependencias

- **De C00:** completitud y principio arquimediano; operaciones con límites; sucesiones geométricas y encajonamiento; valor extremo y continuidad uniforme en intervalos cerrados.
- **De C01–C03:** la derivada de polinomios y el teorema del valor medio se emplean sólo en el laboratorio especial de potencias (§4.7); la convexidad caracteriza la posición de una curva respecto de su cuerda (§4.8). Los argumentos de agotamiento parabólico no precisan cálculo diferencial.
- **Aportaciones de C04:** `EDC-C04-THM-001--004`, `EDC-C04-LEM-001--003` y `EDC-C04-PRP-001--003`, más las aproximaciones rectangulares y su interpretación geométrica.
- **Expresamente no utilizado:** definición general de integral de Riemann–Darboux, Teorema Fundamental, cálculo de primitivas como cuadratura general, series de funciones o teoría de medida.
- **Fuentes históricas:** [Notas del capítulo 4](capitulo-04-notas.html), distinguiendo testimonio antiguo traducido, historiografía leída y libros localizados sin lectura directa.

### Trabajo del lector

Los [ejercicios del capítulo](capitulo-04-ejercicios.html) buscan reconstruir polígonos, estimar errores, refutar argumentos inválidos y demostrar identidades finitas. Sus [soluciones desarrolladas](capitulo-04-soluciones.html) se entregan por separado para preservar el trabajo autónomo.
