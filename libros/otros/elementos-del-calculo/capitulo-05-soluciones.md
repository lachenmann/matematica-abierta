---
title: Capítulo 5 — Soluciones desarrolladas
status: published
draft: false
book-id: MA-BOK-0015
editorial-project: EDC
date-modified: '2026-10-13'
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
source-id: EDC-C05-SOLUCIONES
source-sha256: 9e62ea655db771b3b36b586d56b9b2a4979132a6ebe130f07b79df570a8858ef
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-05.html) · [Ejercicios](capitulo-05-ejercicios.html) · [Soluciones](capitulo-05-soluciones.html)

Las soluciones distinguen los problemas de existencia de los de evaluación; todas utilizan únicamente C00–C05. Cada demostración se ofrece en el dominio indicado y no usa el Teorema Fundamental del Cálculo. Las identidades de valores de integrales de potencias se apoyan en el agotamiento numérico de C04, no en una primitiva general.

## A. Definiciones, supremos y lenguaje

### Solución 5.1 (`EDC-C05-SOL-001`)

La construcción utiliza dos niveles de cotas. En una partición $P=\{a=x_0<\cdots<x_n=b\}$ tomamos $m_i=\inf_{[x_{i-1},x_i]}f$ y $M_i=\sup_{[x_{i-1},x_i]}f$. Al ponderarlas por las anchuras obtenemos $L(f,P)=\sum_im_i\Delta_i$ y $U(f,P)=\sum_iM_i\Delta_i$. Después reunimos todas las particiones mediante $\underline{\mathcal I}(f)=\sup_P L(f,P)$ y $\overline{\mathcal I}(f)=\inf_P U(f,P)$.

La acotación garantiza cotas reales finitas en cada tramo. Si $|f|\le B$, cada suma tiene módulo a lo sumo $B(b-a)$, por lo que también los conjuntos de sumas están acotados y la completitud permite tomar sus extremos globales. No exigimos que cada cota sea alcanzada. El conjunto $(0,1)$, por ejemplo, tiene supremo $1$ e ínfimo $0$, pero carece de máximo y mínimo. Máximo y mínimo son valores que pertenecen al conjunto; supremo e ínfimo sólo han de ser sus mejores cotas.

La integral existe cuando las dos cotas globales coinciden. Que cada una exista por separado es parte de la construcción para cualquier función acotada, y deja abierta la posibilidad de que haya una distancia positiva entre ellas.

### Solución 5.2 (`EDC-C05-SOL-002`)

Los valores positivos $f(x)=x$ con $0<x\le1$ se aproximan a $0$ sin alcanzarlo. Además $f(0)=2$. Por tanto,

$$
\inf_{[0,1]} f=0\quad\text{(no alcanzado)},\qquad
\sup_{[0,1]} f=2=f(0)\quad\text{(alcanzado)}.
$$

Este ejemplo obliga a usar ínfimo y supremo en la definición general. No sería correcto sustituirlos siempre por mínimo y máximo antes de demostrar continuidad.

### Solución 5.3 (`EDC-C05-SOL-003`)

En $[0,1/2]$ la función $x^2$ tiene ínfimo $0$ y supremo $1/4$; en $[1/2,1]$, ínfimo $1/4$ y supremo $1$. Ambas anchuras son $1/2$, luego

$$
L(f,P)=0\cdot\frac12+\frac14\cdot\frac12=\frac18,
\qquad
U(f,P)=\frac14\cdot\frac12+1\cdot\frac12=\frac58.
$$

La diferencia es $1/2$. Las etiquetas sólo cambian $S(f;P,\xi)$, que siempre queda entre esas cotas; las sumas superior e inferior dependen de $f$ y de la partición, no de las etiquetas.

### Solución 5.4 (`EDC-C05-SOL-004`)

Como cada intervalo tiene longitud $1/3$,

$$
S(f;P,\xi)=\frac13\left(0+\frac12+1\right)=\frac12.
$$

La función es creciente, de modo que sus valores extremos son los de los extremos de cada intervalo:

$$
L(f,P)=\frac13\left(0+\frac13+\frac23\right)=\frac13,
\quad
U(f,P)=\frac13\left(\frac13+\frac23+1\right)=\frac23.
$$

Queda verificado el encaje $1/3\le1/2\le2/3$. Elegir otras etiquetas no altera las cotas Darboux.

## B. Refinamientos y compatibilidad

### Solución 5.5 (`EDC-C05-SOL-005`)

En la partición inicial $P=\{0,1\}$, $L(f,P)=0$ y $U(f,P)=1$. En la partición refinada $R=\{0,1/2,1\}$, la solución 5.3 dio $L(f,R)=1/8$ y $U(f,R)=5/8$. Así,

$$
0=L(f,P)\le\frac18=L(f,R)
\le\frac58=U(f,R)\le1=U(f,P).
$$

El incremento de la suma inferior y la disminución de la superior son consecuencia de restringir los conjuntos en los que se calculan ínfimos y supremos; no de la especial forma cuadrática de $f$.

### Solución 5.6 (`EDC-C05-SOL-006`)

Reunimos y ordenamos los puntos de las dos particiones; el refinamiento común es

$$
R=P\cup Q=\left\{0,\frac13,\frac12,\frac23,1\right\}.
$$

Las piezas originales no tienen por qué corresponderse, por lo que comparamos a través de $R$. Al refinar $P$, la suma inferior sólo puede aumentar: $L(f,P)\le L(f,R)$. Al refinar $Q$, la superior sólo puede disminuir: $U(f,R)\le U(f,Q)$. En la partición común, cada ínfimo no supera a su supremo y las anchuras son positivas, luego $L(f,R)\le U(f,R)$. Encadenar las tres comparaciones da $L(f,P)\le U(f,Q)$.

El argumento utiliza acotación para que las cotas existan, y restricciones de conjuntos para compararlas. No necesita monotonía, positividad ni continuidad de la función.

### Solución 5.7 (`EDC-C05-SOL-007`)

Por densidad de racionales e irracionales, toda pieza no degenerada de cualquier partición contiene puntos donde $d$ vale $0$ y otros donde vale $1$. Así sus ínfimos son $0$ y sus supremos $1$, de donde

$$
L(d,P)=\sum_i0\Delta_i=0,
\qquad U(d,P)=\sum_i1\Delta_i=1.
$$

Por tanto $\underline{\mathcal I}(d)=0$, $\overline{\mathcal I}(d)=1$. Como no coinciden, la función no es integrable. No se corrige la diferencia refinando: el salto de oscilación ocurre en **todas** las escalas.

### Solución 5.8 (`EDC-C05-SOL-008`)

El único valor no nulo está en $1/2$, así que el Lema 5.3 da integrabilidad e integral cero. Para reconstruir la cota, cada subintervalo cerrado de anchura positiva contiene puntos distintos de $1/2$, donde la función vale cero. Como es no negativa, su ínfimo es siempre cero.

El supremo sólo puede ser $5$ en un subintervalo que contenga $1/2$. Si el punto cae en el interior de una pieza, sólo esa pieza contribuye; si es un corte de la partición, puede pertenecer a las dos piezas adyacentes. Su longitud total es a lo sumo $2\|P\|$, y obtenemos

$$
0\le U(h,P)-L(h,P)=U(h,P)\le10\|P\|.
$$

La cota funciona sin adaptar los cortes al punto excepcional. Al hacer pequeña la finura, su altura fija queda multiplicada por una longitud total que tiende a cero.

## C. Criterios de existencia y ejemplos

### Solución 5.9 (`EDC-C05-SOL-009`)

La función $s$ es no decreciente y acotada, luego integrable por el Teorema 5.5. Para calcular el valor tomemos $0<\eta<1/3$ y una partición que incluya $1/3-\eta$, $1/3$ y los extremos $0,1$. En el intervalo que termina en $1/3$, el mínimo es $0$ y el máximo $1$; a la derecha, todas las alturas valen $1$. Resulta

$$
L(s,P)=\frac23,\qquad U(s,P)=\frac23+\eta.
$$

Como el valor integral queda entre ambos y $\eta$ puede ser arbitrariamente pequeño, $\int_0^1s=2/3$. El valor aislado $s(1/3)=1$ no añade ninguna anchura positiva.

### Solución 5.10 (`EDC-C05-SOL-010`)

Para $f(x)=-x$ los valores mayores están en el extremo izquierdo de cada pieza. Entonces

$$
U(f,P)-L(f,P)
=\sum_i\bigl[-x_{i-1}-(-x_i)\bigr]\Delta_i
=\sum_i\Delta_i^2
\le\|P\|\sum_i\Delta_i=\|P\|.
$$

Las particiones uniformes de $n$ subintervalos tienen finura $1/n\to0$, luego el criterio de Darboux prueba integrabilidad. El resultado vale sin necesitar un teorema de derivadas ni una primitiva.

### Solución 5.11 (`EDC-C05-SOL-011`)

La función seno es continua en toda la recta: en particular en el intervalo cerrado $[0,\pi]$, según las identidades geométricas y derivadas justificadas en C02. Por el Teorema 5.4, es integrable. La afirmación de existencia no requiere conocer el valor numérico de $\int_0^\pi\sin x\,dx$. Invocar una primitiva para asegurar integrabilidad invertiría el orden lógico de C05 y C06.

### Solución 5.12 (`EDC-C05-SOL-012`)

Para comparar dos valores, aplicamos el valor medio al segmento que los une dentro de $[0,2]$. La continuidad hasta los extremos garantiza sus hipótesis aunque alguno de los puntos sea $0$ o $2$; en el interior tenemos derivabilidad y la cota $|f'|\le3$. Si los puntos coinciden, la desigualdad es inmediata. En todos los casos,

$$
|f(x)-f(y)|\le3|x-y|.
$$

La función es continua y alcanza sus extremos en cada subintervalo. Los puntos de máximo y mínimo distan a lo sumo su anchura, por lo que $M_i-m_i\le3\Delta_i$. Multiplicamos por esa misma anchura y sumamos:

$$
U(f,P)-L(f,P)\le3\sum_i\Delta_i^2
\le3\|P\|\sum_i\Delta_i=6\|P\|.
$$

La segunda comparación usa $\Delta_i\le\|P\|$, y las anchuras suman la longitud total $2$. Basta exigir $\|P\|<1/6000$ para obtener una diferencia estrictamente menor que $10^{-3}$. La elección depende del control de variación y de la longitud del intervalo, sin calcular la integral.

### Solución 5.13 (`EDC-C05-SOL-013`)

Cada suma con muestras irracionales vale $0$ porque $d(\xi_i)=0$, incluso si se toman particiones uniformes cada vez más finas. Pero para esas **mismas** particiones podemos elegir muestras racionales en todos los subintervalos y obtener suma $1$. La integrabilidad exige uniformidad respecto de **todas** las elecciones de etiquetas; una familia prefijada sólo aporta una sucesión de números, no el cuantificador universal del Teorema 5.3.

### Solución 5.14 (`EDC-C05-SOL-014`)

Conservemos el intervalo $[0,1/2]$ sin subdividir. Dividamos $[1/2,1]$ en $n$ piezas iguales, de longitud $1/(2n)$. El número total de intervalos es $n+1\to\infty$, pero

$$
\|P_n\|=\max\left\{\frac12,\frac1{2n}\right\}=\frac12.
$$

No es una familia cuya finura tienda a cero. El Teorema 5.3 demanda un $\delta$ de forma que **toda partición** con finura menor que $\delta$ cumpla una estimación; la familia propuesta puede quedar siempre fuera de ese conjunto cuando $\delta<1/2$.

## D. Demostraciones y auditoría de hipótesis

### Solución 5.15 (`EDC-C05-SOL-015`)

La igualdad de las cotas globales proporciona dos aproximaciones al mismo número $I$, aunque cada una pueda requerir una partición distinta. Por la propiedad del ínfimo elegimos $P_1$ con $U(f,P_1)<I+\varepsilon/2$. Por la del supremo elegimos $P_2$ con $L(f,P_2)>I-\varepsilon/2$.

La tolerancia se reparte en dos mitades para que la distancia entre esas cotas sea menor que $\varepsilon$. Para convertirlas en las dos sumas de una misma partición tomamos $R=P_1\cup P_2$. El refinamiento disminuye la superior de $P_1$ y aumenta la inferior de $P_2$, por lo que

$$
U(f,R)-L(f,R)
\le U(f,P_1)-L(f,P_2)<\varepsilon.
$$

La completitud asegura los números globales; las propiedades de supremo e ínfimo permiten aproximarlos; el refinamiento reúne ambas elecciones sin perder precisión. Así se obtiene la única partición requerida por el criterio, sin suponer que las elecciones iniciales fueran iguales.

### Solución 5.16 (`EDC-C05-SOL-016`)

Fuera del salto, la función es constante en cada pieza situada completamente a un lado de $c$. Allí la suma etiquetada coincide exactamente con la constante por la anchura. Sólo debemos controlar la pieza que atraviesa el salto o el efecto del valor en $c$ cuando es un corte.

Si $c$ está en el interior de $[u,v]$, su contribución ideal al número $b-c$ es la longitud $v-c$. La etiqueta da altura cero o uno, y su contribución es entonces cero o $v-u$. Las diferencias posibles son $v-c$ y $c-u$, ambas no mayores que $v-u\le\delta$. Las demás piezas suman exactamente la longitud restante donde la función vale uno.

Si $c$ es un vértice de la partición, las piezas a su derecha tienen altura uno en todo punto y las de la izquierda tienen altura cero, salvo que la pieza que termina en $c$ elija justamente ese punto como etiqueta. Esa elección añade a lo sumo su anchura, también menor o igual que $\delta$.

En ambos casos el error está acotado por $\delta$ y, en particular, satisface la cota pedida $|S(s_c;P,\xi)-(b-c)|\le2\delta$. La estimación cubre cualquier etiqueta; no depende de que elijamos una muestra conveniente a cada lado del salto.

### Solución 5.17 (`EDC-C05-SOL-017`)

Sean $I_f=\int_a^bf$ e $I_g=\int_a^bg$. Dado $\varepsilon>0$, el Teorema 5.3 da $\delta_f>0$ tal que para toda partición de finura menor que $\delta_f$ y cualquier etiqueta, $|S(f)-I_f|<\varepsilon/2$. Análogamente, existe $\delta_g$ para $g$. Elegimos $\delta=\min\{\delta_f,\delta_g\}$, que es positivo. Si $\|P\|<\delta$,

$$
\begin{aligned}
|S(f+g;P,\xi)-(I_f+I_g)|
&=|[S(f;P,\xi)-I_f]+[S(g;P,\xi)-I_g]|\\
&\le|S(f)-I_f|+|S(g)-I_g|<\varepsilon.
\end{aligned}
$$

El teorema recíproco de sumas de Riemann implica integrabilidad de $f+g$ y que su integral vale $I_f+I_g$. Aquí $\delta$ depende de $\varepsilon$, pero nunca de las etiquetas posteriores.

### Solución 5.18 (`EDC-C05-SOL-018`)

Para $f(x)=g(x)=x$, la función producto es $x^2$. Los valores establecidos sin primitivas son $\int_0^1x=1/2$ y $\int_0^1x^2=1/3$. Así,

$$
\int_0^1fg=\frac13\ne\frac14
=\left(\int_0^1f\right)\left(\int_0^1g\right).
$$

Que el producto de dos funciones integrables sea integrable no significa que la operación integral preserve productos.

### Solución 5.19 (`EDC-C05-SOL-019`)

La función $|2x-1|$ es continua en $[0,1]$, así que su integral existe. Cortamos en $x=1/2$, donde cambia la expresión del módulo: a la izquierda vale $1-2x$ y a la derecha $2x-1$. En cada mitad la gráfica es un segmento recto y forma con el eje un triángulo de base $1/2$ y altura $1$.

Para una función afín no negativa, los trapecios de cualquier partición cubren exactamente esa región. Cada área trapezoidal es el promedio de los dos valores extremos por la anchura, por lo que queda entre las sumas inferior y superior. Esas cotas se aproximan a la integral al refinar, y su encaje identifica el área exacta con ella. Cada triángulo aporta por tanto $(1/2)\cdot1/2=1/4$.

El Teorema 5.8 permite reunir los dos intervalos y obtenemos

$$
\int_0^1|2x-1|\,dx=\frac14+\frac14=\frac12.
$$

El corte fue elegido para disponer de una expresión afín en cada lado. El cálculo combina áreas poligonales y la integral ya definida, sin recurrir a primitivas.

### Solución 5.20 (`EDC-C05-SOL-020`)

Por la Proposición 5.2 aplicada al intervalo de longitud $4$,

$$
\left|\int_0^4 f-\int_0^4 g\right|
\le4\sup_{x\in[0,4]}|f(x)-g(x)|\le4\cdot0.01=0.04.
$$

La cota puede alcanzarse con funciones constantes que difieren en exactamente $0.01$ en todo punto, así que no cabe mejorarla **sin información adicional** sobre $f-g$.

## E. Aditividad, orientación y cálculo

### Solución 5.21 (`EDC-C05-SOL-021`)

En $[0,1]$, la función vale $0$ salvo en el punto $1$, donde vale $3$. El Lema 5.3 prueba que su integral es $0$. En $[1,2]$, $s$ es la constante $3$, cuya integral es $3(2-1)=3$. La aditividad de intervalos da

$$
\int_0^2s=\int_0^1s+\int_1^2s=0+3=3.
$$

El punto de salto puede ser extremo de las dos restricciones sin duplicar una contribución de anchura positiva. Contar el valor de $s(1)$ como un rectángulo de anchura positiva sería un error de modelación.

### Solución 5.22 (`EDC-C05-SOL-022`)

Si $a<u<v<b$, el Teorema 5.8 aplicado con el corte $u$ asegura integrabilidad de la restricción a $[u,b]$. Lo aplicamos otra vez a ese intervalo, ahora con el corte $v$, y obtenemos integrabilidad en $[u,v]$. Cada restricción continúa siendo acotada porque la función original lo es.

Si $u=a$, no necesitamos el primer corte; si $v=b$, no necesitamos el segundo. Si ambos coinciden con los extremos originales, la hipótesis ya da el resultado. En el caso degenerado $u=v$, la integral se fija en cero por definición.

También podemos ver el mecanismo directamente: añadimos los puntos $u,v$ a una partición buena del intervalo completo. Su diferencia superior–inferior no aumenta y se descompone en diferencias no negativas de las piezas. La correspondiente a $[u,v]$ no puede superar el total, de modo que queda menor que la tolerancia elegida. Esto explica por qué la integrabilidad se conserva al restringir el intervalo.

### Solución 5.23 (`EDC-C05-SOL-023`)

En $[1,3]$, la función afín $f(x)=2x$ está representada por la recta que va de altura $2$ a altura $6$. La suma de trapecios sobre **cualquier** partición es exactamente el área algebraica del trapecio total,

$$
\frac{2+6}{2}(3-1)=8.
$$

Las sumas de trapecios aproximan la integral por encaje: en funciones afines la oscilación se acota por la finura, y tanto el valor de trapecio como la integral quedan entre sumas extremas cuya diferencia tiende a cero. Por tanto $\int_1^3 2x\,dx=8$. Al invertir los extremos se cambia el signo: $\int_3^1 2x\,dx=-8$.

### Solución 5.24 (`EDC-C05-SOL-024`)

Desarrollamos $(1-x)^2=1-2x+x^2$. La linealidad del Teorema 5.6 y las cuadraturas previamente justificadas dan

$$
\int_0^1(1-x)^2\,dx
=\int_0^1 1\,dx-2\int_0^1x\,dx+\int_0^1x^2\,dx
=1-2\cdot\frac12+\frac13=\frac13.
$$

La respuesta proviene de sumas finitas y no de evaluar una función primitiva.

## F. Valor medio, contraejemplos y estabilidad

### Solución 5.25 (`EDC-C05-SOL-025`)

Como la cuadratura de C04 y C05 demuestra $\int_0^1x^2\,dx=1/3$ y la longitud del intervalo es $1$, el teorema del valor medio integral pide $c^2=1/3$. El único punto de $[0,1]$ que cumple la igualdad es

$$
c=\frac1{\sqrt3}.
$$

La continuidad del cuadrado en $[0,1]$ asegura la existencia abstracta de un punto promedio; el cálculo algebraico identifica ese punto.

### Solución 5.26 (`EDC-C05-SOL-026`)

La función es no decreciente y acotada, de modo que es integrable por el Teorema 5.5. Su valor integral es la longitud del tramo donde vale $1$, a saber, $1/2$, como demuestra el método de particiones adaptadas al salto. El promedio es $\frac1{1-0}\int_0^1f=1/2$. Sin embargo, para todo punto del dominio se tiene $f(c)\in\{0,1\}$, nunca $1/2$. Por ello el teorema del valor medio integral requiere la hipótesis de **continuidad** para garantizar que el promedio esté en la imagen.

### Solución 5.27 (`EDC-C05-SOL-027`)

Sea $h$ la diferencia entre la función modificada y $x^2$. Se anula fuera del punto $c=1/2$ y toma allí el valor $100-1/4=399/4$. Por el Lema 5.3, $h$ es integrable y $\int_0^1h=0$. La linealidad permite escribir

$$
\int_0^1(x^2+h)=\int_0^1x^2+\int_0^1h=\frac13.
$$

La modificación no es pequeña en altura, pero afecta sólo una posición: todas las sumas cambian a lo sumo una cantidad proporcional a la anchura de los pocos subintervalos que tocan ese punto.

### Solución 5.28 (`EDC-C05-SOL-028`)

Para controlar el producto necesitamos separar el cambio de cada factor. Añadimos y restamos $f(x)g(y)$ y aplicamos la desigualdad triangular; con $|f|\le A$, $|g|\le B$ obtenemos, para $x,y$ de un mismo intervalo cerrado $I$,

$$
|f(x)g(x)-f(y)g(y)|
\le|f(x)|\,|g(x)-g(y)|+|g(y)|\,|f(x)-f(y)|.
$$

Las cotas globales limitan los multiplicadores por $A$ y $B$. Al tomar supremos sobre parejas resulta $\operatorname{osc}_I(fg)\le A\operatorname{osc}_I(g)+B\operatorname{osc}_I(f)$. La identidad entre oscilación y supremo de separaciones no exige valores máximos o mínimos alcanzados: se pueden aproximar las cotas locales cuanto se quiera.

Multiplicamos por la longitud de cada pieza y sumamos. Para conseguir un error menor que $\varepsilon$, elegimos mediante Darboux una partición para $f$ y otra para $g$, cada una con diferencia menor que $\varepsilon/(1+A+B)$. Tomamos su refinamiento común, que conserva o mejora ambas diferencias. La cota del producto queda entonces menor que $\varepsilon$, y el criterio demuestra integrabilidad. El denominador elegido funciona también cuando alguna cota es cero; $A$ y $B$ no dependen de la pieza porque controlan todo $[a,b]$.

### Solución 5.29 (`EDC-C05-SOL-029`)

La función constante $-2$ tiene todas sus sumas etiquetadas iguales a $-2(3-0)=-6$, así que su integral es $-6$. El área geométrica de un rectángulo de base $3$ y altura positiva $2$ es $6$. La integral no es la magnitud absoluta de esa superficie cuando la función es negativa: es la acumulación **orientada**, o área algebraica. Si la constante expresa una velocidad $-2\,\mathrm{m/s}$ durante $3\,\mathrm{s}$, la integral representa desplazamiento de $-6\,\mathrm{m}$, no distancia recorrida negativa.

## G. Síntesis rigurosa

### Solución 5.30 (`EDC-C05-SOL-030`)

Separamos la función en una parte continua y una función escalón. La función $x^2$ es integrable por continuidad; $s(x)=\mathbf1_{[1/2,1]}(x)$ lo es por monotonía y tiene integral $1/2$, según el cálculo de particiones adaptadas al salto. Por linealidad, para cada $\lambda\ge0$,

$$
\boxed{\int_0^1f_\lambda(x)\,dx=\frac13+\frac\lambda2.}
$$

Para estimar una suma con muestras arbitrarias, el control de C04 sitúa tanto $S(x^2;P,\xi)$ como el candidato $1/3$ entre las sumas extremas. Su distancia no supera la anchura del encaje, y por tanto

$$
\left|S(x^2;P,\xi)-\frac13\right|\le\|P\|.
$$

Para el escalón usamos la solución 5.16, que controla el único tramo afectado por el salto y sirve también si éste es un vértice: $|S(s;P,\xi)-1/2|\le2\|P\|$. La linealidad de las sumas es una identidad finita para la misma partición y las mismas etiquetas. Al restar el valor integral y aplicar la desigualdad triangular, con $\lambda\ge0$, obtenemos

$$
\begin{aligned}
\left|S(f_\lambda;P,\xi)-\left(\frac13+\frac\lambda2\right)\right|
&\le\left|S(x^2;P,\xi)-\frac13\right|
+\lambda\left|S(s;P,\xi)-\frac12\right|\\
&\le(1+2\lambda)\|P\|.
\end{aligned}
$$

Para un parámetro fijo y una tolerancia $\varepsilon>0$, basta exigir $\|P\|<\varepsilon/(1+2\lambda)$. La elección se hace antes de escoger la partición y las etiquetas, y garantiza la precisión para todas ellas. La constante depende de $\lambda$; la afirmación no exige uniformidad para un parámetro que crezca sin límite. El Teorema Fundamental no interviene.

---

**Auditoría de cobertura:** exactamente un desarrollo `EDC-C05-SOL-001--030` por cada `EDC-C05-EXR-001--030`; todas las partes numéricas, conceptuales y demostrativas están respondidas.
