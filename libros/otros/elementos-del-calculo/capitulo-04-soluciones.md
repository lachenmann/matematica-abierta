---
title: Capítulo 4 — Soluciones desarrolladas
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
source-id: EDC-C04-SOLUCIONES
source-sha256: 4942b0726b59436bf980389ab624142a721355a507ef1b0f6045359b64dd9cbb
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-04.html) · [Ejercicios](capitulo-04-ejercicios.html) · [Soluciones](capitulo-04-soluciones.html)

Las soluciones son demostraciones y cálculos propios correspondientes a los treinta ejercicios del capítulo. Se usan únicamente resultados de C00–C04 y geometría elemental de polígonos. La noción general de integral todavía no interviene.

## A. Lectura geométrica y precisión conceptual

### Solución 4.1 (`EDC-C04-SOL-001`)

La inclusión de $P_n$ en la región y de ésta en $Q_n$ exige que cualquier área compatible, si existe, pertenezca a $[A(P_n),A(Q_n)]$. Una aproximación interior no puede superar ese valor, y una cubierta exterior no puede quedar por debajo de él.

Si las anchuras tienden a cero, la Proposición 4.1 demuestra que dos números presentes en todos esos intervalos deben coincidir: su distancia fija no podría ser menor que anchuras arbitrariamente pequeñas. Eso asegura unicidad, pero todavía no proporciona un número común. Para ver la diferencia, tomemos $L_n=n$ y $U_n=n+1/n$. Aunque $L_n\le U_n$ y $U_n-L_n\to0$, cualquier número real fijado queda por debajo de $L_n$ para $n$ suficientemente grande. No pertenece a todos los intervalos.

En el problema geométrico debemos comprobar además que las cotas retienen algún candidato, o demostrar la existencia mediante otra propiedad de la construcción. En el segmento parabólico se hace lo primero: el número $4T/3$ se compara expresamente con los dos extremos de cada encaje.

### Solución 4.2 (`EDC-C04-SOL-002`)

La anchura horizontal es $\ell=b-a$. Al completar el cuadrado,

$$
k(x-a)(b-x)=k\left[\frac{\ell^2}{4}-\left(x-\frac{a+b}2\right)^2\right],
$$

por lo que la altura máxima es $H=k\ell^2/4$ y el área triangular $T=\ell H/2=k\ell^3/8$. Si $x$ e $y$ tienen dimensión de longitud, $(x-a)(b-x)$ tiene dimensión $L^2$ y, por tanto, $k$ debe tener dimensión $L^{-1}$. Entonces $k\ell^3$ tiene dimensión $L^2$, como corresponde al área.

### Solución 4.3 (`EDC-C04-SOL-003`)

Por monotonía de área, un polígono interior sólo ofrece una **cota inferior** $P$. Puede quedar una región considerable fuera de él; por ejemplo, bajo una parábola el triángulo inicial tiene área $T$, mientras la cuadratura da $4T/3$, de modo que faltaría $T/3$. Para ganar precisión se necesita además una cota exterior $U$ y una construcción de aproximaciones $L_n\le A\le U_n$ con $U_n-L_n$ arbitrariamente pequeño. El Lema 4.3 controla precisamente el resto de la construcción parabólica.

### Solución 4.4 (`EDC-C04-SOL-004`)

Agotar significa que, para cada tolerancia positiva fijada, podemos elegir un número finito de etapas cuyo error sea menor. Las etapas necesarias pueden crecer al pedir más precisión; la afirmación no exige que una única etapa deje resto cero.

Si $R_n\le R_0(1/2)^n$, el Lema 4.1 compara las potencias con una cota que tiende a cero por el principio arquimediano de C00. Para una tolerancia $\varepsilon>0$ podemos elegir un entero que haga la cota menor que $\varepsilon$, y así controlar todas las etapas posteriores. La prueba se refiere a errores de construcciones finitas.

La expresión «agregar todas las piezas» de una descomposición infinita deja sin precisar cómo se realiza esa suma y qué garantiza su existencia. Para utilizarla como una operación matemática necesitaríamos definirla y justificarla; el agotamiento obtiene la precisión solicitada mediante una etapa y una cota concretas.

## B. Triángulos parabólicos y agotamiento

### Solución 4.5 (`EDC-C04-SOL-005`)

Aquí $k=2$, $a=0$, $b=3$ y $\ell=3$. La altura máxima es $H=2\cdot9/4=9/2$, alcanzada en $x=3/2$. El triángulo principal tiene área

$$
T=\frac{3(9/2)}2=\frac{27}{4}.
$$

La cuadratura determina $4T/3=9$. La respuesta tiene unidades cuadradas si ambas coordenadas se miden en longitudes compatibles.

### Solución 4.6 (`EDC-C04-SOL-006`)

La anchura es $\ell=2$, la altura máxima $H=3(2^2)/4=3$, y el triángulo tiene área $T=2\cdot3/2=3$. El área parabólica determinada por el agotamiento es $4T/3=4$.

### Solución 4.7 (`EDC-C04-SOL-007`)

Se han incluido dos generaciones, las de índices $0$ y $1$, así que en las fórmulas del capítulo corresponde usar $n=2$. La primera aporta $T$ y la segunda $T/4$:

$$
P_2=T+\frac T4=\frac{5T}{4},
\qquad B_2=\frac{2T}{4^2}=\frac T8.
$$

El extremo inferior es el área ya cubierta, $P_2$. Para obtener una cota superior añadimos la cobertura de todo el resto, $B_2$, y queda

$$
\left[\frac{5T}{4},\frac{11T}{8}\right].
$$

El candidato $4T/3$ está dentro: supera al extremo inferior en $T/12$ y queda por debajo del superior en $T/24$. Esas dos distancias suman $T/8$, la anchura del intervalo. Por tanto, la cota $B_2$ controla el resto completo sin ser igual al error exacto del polígono interior, que aquí es $T/12$.

### Solución 4.8 (`EDC-C04-SOL-008`)

Con $T=3/2$, el error del polígono interior frente al valor final se reduce a

$$
\frac{4T}{3\cdot4^n}=\frac2{4^n}.
$$

Queremos que sea estrictamente menor que $1/1000$. Como $4^n>0$, podemos multiplicar sin cambiar el sentido: la condición equivale a $4^n>2000$. Las potencias crecen estrictamente y $4^5=1024<2000<4096=4^6$, así que el menor entero admisible es $n=6$. No necesitamos dibujar ni sumar individualmente los triángulos; la fórmula de la recurrencia ya reúne sus áreas y permite escoger la etapa por su error.

### Solución 4.9 (`EDC-C04-SOL-009`)

La fórmula del Lema 4.2 es válida también para cuerdas oblicuas: con anchura horizontal $d$ y coeficiente cuadrático $-k$, el área triangular es $kd^3/8$. Cada intervalo hijo tiene anchura $d/2$, y el coeficiente $k$ permanece igual al restar su nueva cuerda. Por eso su triángulo tiene área $k(d/2)^3/8=(kd^3/8)/8$.

Al partir la anchura por dos, la separación vertical máxima se divide por cuatro; los dos cambios juntos dividen el área por ocho. Hay dos triángulos nuevos, con interiores en mitades horizontales distintas, y sus áreas se suman: la pareja aporta $2(1/8)=1/4$ del área del padre. Toda la comparación utiliza tres triángulos y la aditividad finita.

### Solución 4.10 (`EDC-C04-SOL-010`)

En la generación $n$ hay $2^n$ triángulos. Cada uno tiene área $1/8^n$, porque cada generación multiplica el área individual por $1/8$. El total es

$$
\frac{2^n}{8^n}=\frac1{4^n}.
$$

Para $n=0$ la fórmula da un solo triángulo de área $1$, como exige la convención inicial.

## C. Rectángulos, particiones y potencias

### Solución 4.11 (`EDC-C04-SOL-011`)

Con $n=4$, usando las fórmulas de §4.6,

$$
L_4=\frac{(4-1)(2\cdot4-1)}{6\cdot4^2}
=\frac{21}{96}=\frac7{32},
$$

$$
R_4=\frac{(4+1)(2\cdot4+1)}{6\cdot4^2}
=\frac{45}{96}=\frac{15}{32}.
$$

La diferencia vale $8/32=1/4$ y $7/32<1/3<15/32$.

### Solución 4.12 (`EDC-C04-SOL-012`)

Los subintervalos tienen anchuras $1/4,1/2,1/4$. Para muestras izquierdas,

$$
L(P)=0\cdot\frac14+\frac1{16}\cdot\frac12+\frac9{16}\cdot\frac14
=\frac1{32}+\frac9{64}=\frac{11}{64}.
$$

Para muestras derechas,

$$
U(P)=\frac1{16}\cdot\frac14+\frac9{16}\cdot\frac12+1\cdot\frac14
=\frac1{64}+\frac{18}{64}+\frac{16}{64}=\frac{35}{64}.
$$

Así $U-L=24/64=3/8$. La finura es $\|P\|=1/2$, y se verifica $3/8\le1/2$.

### Solución 4.13 (`EDC-C04-SOL-013`)

Con $n=2$, los puntos medios son $1/4$ y $3/4$:

$$
M_2=\frac12\left[\left(\frac14\right)^2+\left(\frac34\right)^2\right]
=\frac5{16}.
$$

El trapecio compuesto da el promedio de las sumas izquierdas $1/8$ y derechas $5/8$, por lo que $T_2=3/8$. Sus errores respecto del candidato $1/3$ son

$$
\frac13-M_2=\frac1{48},\qquad T_2-\frac13=\frac1{24}.
$$

Ambos cálculos son exactos y, en este ejemplo, el punto medio tiene menor error absoluto.

### Solución 4.14 (`EDC-C04-SOL-014`)

Sobre $[x_{i-1},x_i]$ la figura bajo $y=x$ es un trapecio de área $\tfrac12(x_i+x_{i-1})\Delta_i$, que coincide con $\tfrac12(x_i^2-x_{i-1}^2)$. Al sumar, la expresión telescopa:

$$
T(P)=\frac12\sum_i(x_i^2-x_{i-1}^2)=\frac12.
$$

Para las sumas extremas,

$$
U(P)-L(P)=\sum_i(x_i-x_{i-1})\Delta_i=\sum_i\Delta_i^2.
$$

Es cero sólo en el caso degenerado sin anchuras positivas; para una partición finita estricta, la diferencia es positiva aunque pueda hacerse arbitrariamente pequeña.

### Solución 4.15 (`EDC-C04-SOL-015`)

Para $n=2$ y $f(x)=x^3$,

$$
L_{2,3}=\frac12\left(0^3+\frac18\right)=\frac1{16},
\qquad U_{2,3}=\frac12\left(\frac18+1\right)=\frac9{16}.
$$

Se cumple $1/16<1/4<9/16$. La diferencia es $1/2$, de acuerdo con el Teorema 4.3.

### Solución 4.16 (`EDC-C04-SOL-016`)

Para $k=2$ y longitud horizontal $\ell=2$, la altura máxima es $H=2(4)/4=2$ y el triángulo principal tiene $T=2\cdot2/2=2$. Por agotamiento,

$$
A=\frac43T=\frac83.
$$

No empleamos la evaluación de una integral de polinomios.

## D. Diagnóstico de razonamientos inválidos

### Solución 4.17 (`EDC-C04-SOL-017`)

Tomemos $d(x)=1$ para $x$ racional y $d(x)=0$ para $x$ irracional. Es acotada entre cero y uno. La densidad de racionales e irracionales (`EDC-C00-LEM-003`) asegura que en todo subintervalo de anchura positiva podemos seleccionar muestras racionales y obtener suma $1$, o muestras irracionales y obtener suma $0$. La elección no se estabiliza al disminuir la finura; por tanto no existe un valor independiente de muestras para esas sumas. La acotación sola es insuficiente.

### Solución 4.18 (`EDC-C04-SOL-018`)

La aditividad geométrica conocida se aplica a una **unión finita** de polígonos con interiores disjuntos. No afirma que el área de una unión infinita sea la suma de las áreas de sus partes, y menos aún que tal suma tenga el significado intuitivo supuesto. Las líneas pueden ser objetos de espesor nulo, pero inferir el área de una superficie a partir de «sumar ceros» exige definir rigurosamente una operación de composición infinita y el concepto de área pertinente. En el método de Cavalieri la comparación mediante secciones es una técnica geométrica histórica, no una suma aritmética literal de infinitos ceros.

### Solución 4.19 (`EDC-C04-SOL-019`)

La identidad $P_n\to4T/3$ controla las áreas de los polígonos interiores. Para relacionarlas con la región completa hay que estudiar lo que aún queda entre el polígono y el arco: el límite de lo cubierto no estima por sí solo ese resto.

El Lema 4.3 lo incluye en franjas poligonales cuya área total es $B_n=2T/4^n\to0$. Así cualquier valor compatible debe quedar entre $P_n$ y $P_n+B_n$ para cada $n$. El Teorema 4.2 comprueba que $4T/3$ pertenece efectivamente a cada intervalo, lo que establece existencia, y utiliza después la anchura tendiendo a cero para establecer unicidad. La cobertura exterior proporciona la comparación que faltaba en el argumento de la alumna.

### Solución 4.20 (`EDC-C04-SOL-020`)

Podemos aumentar el número de subintervalos sin tocar uno que siga siendo ancho. Conservemos $[0,1/2]$ como primer subintervalo en todas las particiones y dividamos sólo $[1/2,1]$ en $n$ partes iguales, cada una de longitud $1/(2n)$. El número total es $n+1\to\infty$, pero la anchura máxima sigue siendo $1/2$.

Los tramos del segundo bloque se hacen pequeños y el primero permanece igual. Una garantía que dependa de la finura no puede aplicarse sólo porque haya muchas piezas: hay que controlar también la más ancha.

### Solución 4.21 (`EDC-C04-SOL-021`)

La integral de Riemann–Darboux será definida en C05. Invocar ahora $\int_0^1x^2\,dx=1/3$ como premisa significaría usar una teoría aún no construida para fundamentar la necesidad de esa misma teoría. En cambio, la cuadratura parabólica ha sido demostrada mediante triángulos y cotas, y las sumas de cuadrados mediante identidades finitas y límites de sucesiones de C00. Que tales resultados coincidan con futuras integrales será una conclusión posterior, no una hipótesis oculta.

## E. Demostraciones y control de hipótesis

### Solución 4.22 (`EDC-C04-SOL-022`)

Sea $S_n=1+q+\cdots+q^{n-1}$. Entonces $qS_n=q+\cdots+q^n$, por lo que

$$
(1-q)S_n=S_n-qS_n=1-q^n.
$$

Como $q\ne1$, $S_n=(1-q^n)/(1-q)$. La diferencia respecto del candidato $1/(1-q)$ es

$$
\frac1{1-q}-S_n=\frac{q^n}{1-q},
$$

que tiende a cero para $0<q<1$ por el Lema 4.1. No ha sido necesario definir el producto de una serie infinita arbitraria.

### Solución 4.23 (`EDC-C04-SOL-023`)

La monotonía asegura que $f(x_i)-f(x_{i-1})\ge0$. El término correspondiente de la diferencia de sumas es esa variación multiplicada por $\Delta_i$; podemos reemplazar la anchura por $\|P\|$ para obtener una cota superior, porque el otro factor es no negativo. Resulta

$$
U(P)-L(P)=\sum_i[f(x_i)-f(x_{i-1})]\Delta_i
\le\|P\|\sum_i[f(x_i)-f(x_{i-1})].
$$

En la suma derecha, el valor en cada punto interior aparece una vez sumado y una vez restado. Sólo quedan $f(b)-f(a)\ge0$, que da la cota pedida. Cada sumando de la diferencia original es no negativo, por lo que también se cumple la cota inferior cero. La continuidad no interviene: la monotonía y la cancelación finita bastan.

### Solución 4.24 (`EDC-C04-SOL-024`)

Usamos dos consecuencias diferentes de la continuidad en un intervalo cerrado. El teorema de valores extremos garantiza que en cada $[x_{i-1},x_i]$ hay puntos donde se alcanzan el mínimo $m_i$ y el máximo $M_i$. La continuidad uniforme permite comparar esos dos valores con una misma tolerancia cualquiera que sea el lugar del subintervalo.

Para escoger esa tolerancia, observamos que la diferencia total es la suma de $(M_i-m_i)\Delta_i$. Si cada oscilación es menor que $\eta$, el total será menor que $\eta(b-a)$, pues las anchuras suman $b-a$. Elegimos $\eta=\varepsilon/[2(b-a)]$ y obtenemos por continuidad uniforme un $\delta>0$ tal que $|f(x)-f(y)|<\eta$ cuando $|x-y|<\delta$.

Con $\|P\|<\delta$, los puntos de mínimo y máximo de cada subintervalo distan menos que $\delta$, luego $M_i-m_i<\eta$. Al multiplicar por las anchuras y sumar,

$$
0\le A_+(P)-A_-(P)
<\eta\sum_i\Delta_i
=\varepsilon/2<\varepsilon.
$$

El mismo $\delta$ sirve para todas las particiones suficientemente finas. Una elección que dependiera sin control de cada punto no daría por sí sola esa garantía común.

### Solución 4.25 (`EDC-C04-SOL-025`)

Por inducción $R_n\le R_0(2/3)^n$; el caso $n=0$ es inmediato y el paso sigue multiplicando por $2/3$. Como $3/2>1$, la desigualdad binomial da $(3/2)^n\ge1+n/2$. En consecuencia,

$$
R_n\le\frac{R_0}{(3/2)^n}\le\frac{R_0}{1+n/2}\to0.
$$

Dado $\varepsilon>0$, basta escoger $n>2(R_0/\varepsilon-1)$, o cualquier entero mayor suficientemente grande si el lado derecho fuese negativo. Sólo se han usado estimaciones finitas y el principio arquimediano.

### Solución 4.26 (`EDC-C04-SOL-026`)

Queremos encontrar un número encerrado entre las sumas por extremos de cualquier partición. Elegimos $F(x)=x^{p+1}/(p+1)$ porque $F'(x)=x^p$, y sus incrementos consecutivos se cancelarán al sumarlos. El polinomio es continuo en cada $[x_{i-1},x_i]$ y derivable en su interior; el valor medio proporciona un $\xi_i$ interior con

$$
F(x_i)-F(x_{i-1})=\xi_i^p\Delta_i.
$$

La potencia $x^p$ es creciente sobre $[0,1]$, así que el valor intermedio queda entre las potencias de los dos extremos. Multiplicando por $\Delta_i>0$ obtenemos

$$
x_{i-1}^p\Delta_i\le F(x_i)-F(x_{i-1})\le x_i^p\Delta_i.
$$

Al sumar, los incrementos de $F$ dan $F(1)-F(0)=1/(p+1)$. La suma inferior es $L(P)$ y la superior $U(P)$; por tanto $L(P)\le1/(p+1)\le U(P)$. Para conocer la precisión, aplicamos la cota de finura a las variaciones no negativas de la potencia:

$$
U(P)-L(P)=\sum_i(x_i^p-x_{i-1}^p)\Delta_i
\le\|P\|\sum_i(x_i^p-x_{i-1}^p)=\|P\|.
$$

La última suma vale uno por cancelación de sus términos interiores. Así el candidato queda encerrado con una anchura a lo sumo $\|P\|$, aunque las anchuras individuales no sean iguales. Cualquier suma con muestras en esos subintervalos pertenece también al encaje, por la monotonía de la potencia.

## F. Descubrimiento y síntesis

### Solución 4.27 (`EDC-C04-SOL-027`)

Una partición uniforme de $n$ intervalos tiene finura $1/n$, y para $x^2$ la diferencia extrema es exactamente $1/n$. Si escogemos $n=2^{10}=1024$, entonces

$$
U(P)-L(P)=\frac1{1024}<\frac1{1000}.
$$

Nueve duplicaciones no bastan, pues $1/512>1/1000$. La elección depende de la precisión solicitada y no de un cálculo previo de áreas curvilíneas.

### Solución 4.28 (`EDC-C04-SOL-028`)

Para calcular el área entre la parábola y su cuerda, necesitamos la separación entre ambas, que puede ser positiva incluso si alguna ordenada de la parábola es negativa. Sea $f(x)=-2x^2+5x+1$ y $\ell(x)$ la recta que interpola sus valores en $1$ y $3$. Restarla conserva el coeficiente cuadrático $-2$ y crea ceros en los dos extremos, por lo que

$$
f(x)-\ell(x)=-2(x-1)(x-3)=2(x-1)(3-x).
$$

Esta diferencia tiene la forma del segmento estudiado, con $k=2$ y anchura horizontal $2$. El triángulo principal tiene área

$$
T=\frac{2\cdot2^3}{8}=2.
$$

La cuadratura por agotamiento da $4T/3=8/3$. La cuerda oblicua se trata con el Lema 4.2: el área depende de la anchura horizontal y de la separación vertical, sin exigir que la base esté sobre el eje horizontal.

### Solución 4.29 (`EDC-C04-SOL-029`)

Con $T=1$ y tres generaciones (índices $0,1,2$),

$$
P_3=1+\frac14+\frac1{16}=\frac{21}{16},
\qquad B_3=\frac2{4^3}=\frac1{32}.
$$

La cota exterior es $P_3+B_3=42/32+1/32=43/32$. El candidato $4/3$ satisface

$$
\frac{21}{16}<\frac43<\frac{43}{32}.
$$

Las diferencias son $4/3-21/16=1/48$ y $43/32-4/3=1/96$; suman $1/32$, exactamente la anchura del encaje.

## G. Desafío de conjunto

### Solución 4.30 (`EDC-C04-SOL-030`)

Para controlar todas las muestras aprovechamos primero dos funciones cuyos encajes ya conocemos, $x^2$ y $x$. La expresión dada se escribe $f_\lambda(x)=(1-\lambda)x^2+\lambda x$. En cualquier partición con muestras $\xi_i$, la distributividad y la linealidad de una suma finita dan

$$
S(P,\xi;f_\lambda)
=(1-\lambda)S(P,\xi;x^2)+\lambda S(P,\xi;x).
$$

El Ejercicio 4.26, con $p=2$, sitúa cualquier suma etiquetada de $x^2$ entre sus sumas extremas. El número $1/3$ pertenece al mismo intervalo, cuya anchura no supera $\|P\|$; la distancia entre dos números de ese intervalo tampoco puede superarla. Por tanto,

$$
\left|S(P,\xi;x^2)-\frac13\right|\le\|P\|.
$$

Para $p=1$ obtenemos de la misma manera

$$
\left|S(P,\xi;x)-\frac12\right|\le\|P\|.
$$

El coeficiente $1-\lambda$ puede ser negativo cuando $\lambda>1$, así que no multiplicamos los encajes manteniendo siempre su sentido. Restamos en cambio la combinación de los dos candidatos y usamos la desigualdad triangular con el valor absoluto de ese coeficiente. Como $\lambda\ge0$,

$$
\begin{aligned}
\left|S(P,\xi;f_\lambda)-\left(\frac{1-\lambda}{3}+\frac\lambda2\right)\right|
&\le|1-\lambda|\left|S(P,\xi;x^2)-\frac13\right|
+\lambda\left|S(P,\xi;x)-\frac12\right|\\
&\le(|1-\lambda|+\lambda)\|P\|.
\end{aligned}
$$

El candidato es $1/3+\lambda/6$. Para cada $\lambda$ fijo, la constante $|1-\lambda|+\lambda$ es finita y la cota tiende a cero cuando la finura tiende a cero. No depende del número de subintervalos ni de las muestras, por lo que todas las elecciones convergen al mismo candidato. La afirmación es para cada parámetro fijo; no exige una cota común a todos los valores ilimitados de $\lambda$.
