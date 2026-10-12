---
title: Capítulo 4 — Soluciones desarrolladas
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
source-id: EDC-C04-SOLUCIONES
source-sha256: 3df6d09658e21de7497d40cf502c1992b520d9685b28582ecf660383ed71ac15
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-04.html) · [Ejercicios](capitulo-04-ejercicios.html) · [Soluciones](capitulo-04-soluciones.html) · [Notas históricas](capitulo-04-notas.html)

Las soluciones son demostraciones y cálculos propios correspondientes a los treinta ejercicios del capítulo. Se usan únicamente resultados de C00–C04 y geometría elemental de polígonos. La noción general de integral todavía no interviene.

## A. Lectura geométrica y precisión conceptual

### Solución 4.1 (`EDC-C04-SOL-001`)

Si $P_n$ está contenido en la región y ésta en $Q_n$, un área compatible, **si existe**, debe pertenecer al intervalo $[A(P_n),A(Q_n)]$. La anchura de esos intervalos puede tender a cero; la Proposición 4.1 asegura entonces que no caben dos valores distintos presentes en **todos** los intervalos. Pero esta condición aislada no garantiza existencia. Por ejemplo, tomando $L_n=n$ y $U_n=n+1/n$, tenemos $L_n\le U_n$ y $U_n-L_n\to0$, pero ningún número real puede pertenecer a $[L_n,U_n]$ para todo $n$. En un problema geométrico es necesario construir un candidato y comprobar que las cotas interiores y exteriores lo encierran, o demostrar mediante una estructura adicional la existencia de un punto común.

### Solución 4.2 (`EDC-C04-SOL-002`)

La anchura horizontal es $\ell=b-a$. Al completar el cuadrado,

$$
k(x-a)(b-x)=k\left[\frac{\ell^2}{4}-\left(x-\frac{a+b}2\right)^2\right],
$$

por lo que la altura máxima es $H=k\ell^2/4$ y el área triangular $T=\ell H/2=k\ell^3/8$. Si $x$ e $y$ tienen dimensión de longitud, $(x-a)(b-x)$ tiene dimensión $L^2$ y, por tanto, $k$ debe tener dimensión $L^{-1}$. Entonces $k\ell^3$ tiene dimensión $L^2$, como corresponde al área.

### Solución 4.3 (`EDC-C04-SOL-003`)

Por monotonía de área, un polígono interior sólo ofrece una **cota inferior** $P$. Puede quedar una región considerable fuera de él; por ejemplo, bajo una parábola el triángulo inicial tiene área $T$, mientras la cuadratura da $4T/3$, de modo que faltaría $T/3$. Para ganar precisión se necesita además una cota exterior $U$ y una construcción de aproximaciones $L_n\le A\le U_n$ con $U_n-L_n$ arbitrariamente pequeño. El Lema 4.3 controla precisamente el resto de la construcción parabólica.

### Solución 4.4 (`EDC-C04-SOL-004`)

Agotar significa probar: *dada cualquier* tolerancia positiva, un número **finito** de operaciones deja un error inferior a ella. Por ejemplo, si después de $n$ pasos $R_n\le R_0(1/2)^n$, el principio arquimediano y el Lema 4.1 permiten escoger un $n$ adecuado. Decir que se han agregado «todas» las piezas de una partición infinita no especifica qué operación suma las áreas ni por qué el resultado existe. La diferencia es lógica: una es una afirmación cuantificada sobre pasos finitos y tolerancias, mientras la otra demanda una teoría adicional del infinito.

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

Después de las generaciones $0$ y $1$ contamos $n=2$, de modo que

$$
P_2=T+\frac T4=\frac{5T}{4},
\qquad B_2=\frac{2T}{4^2}=\frac T8.
$$

El intervalo de encaje es

$$
\left[\frac{5T}{4},\frac{11T}{8}\right].
$$

En efecto $5T/4=10T/8$, y el valor $4T/3$ queda entre sus extremos: $1.25T<1.333\ldots T<1.375T$. Su anchura es $T/8$, no el error exacto del polígono interior frente al valor final.

### Solución 4.8 (`EDC-C04-SOL-008`)

Con $T=3/2$, el error interior es

$$
\frac{4T}{3\cdot4^n}=\frac2{4^n}.
$$

Exigimos $2/4^n<1/1000$, esto es $4^n>2000$. Se cumple por primera vez para $n=6$, pues $4^5=1024<2000<4096=4^6$. No hay que calcular 4096 triángulos: basta aplicar la razón de áreas ya demostrada.

### Solución 4.9 (`EDC-C04-SOL-009`)

Si el intervalo horizontal original tiene anchura $d$, su triángulo tiene área $kd^3/8$. Cada intervalo hijo tiene anchura $d/2$ y el área del triángulo asociado es $k(d/2)^3/8=(kd^3/8)/8$, exactamente un octavo. Dos triángulos sin superposición interior agregan $2(1/8)=1/4$ del área del padre. Se trata de una razón de áreas **finitas** y no de una suma infinita.

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

La identidad $P_n\to4T/3$ establece el límite de las **áreas de polígonos interiores**, no de manera automática el área del segmento parabólico. Podría quedar una parte cuya área no estuviera controlada. El Lema 4.3 cubre esa parte mediante paralelogramos de área total $B_n=2T/4^n\to0$. Sólo entonces el Teorema 4.2 demuestra que cualquier valor geométricamente compatible queda obligado a ser $4T/3$.

### Solución 4.20 (`EDC-C04-SOL-020`)

Fijemos el primer subintervalo $[0,1/2]$ para todas las particiones. Para el restante $[1/2,1]$ hagamos $n$ subdivisiones iguales, de longitud $1/(2n)$. El número total de subintervalos es $n+1\to\infty$, pero la finura sigue siendo $1/2$. No podemos aplicar teoremas cuyo supuesto es $\|P\|\to0$; subsisten intervalos de anchura macroscópica.

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

Como $f$ es no decreciente, $f(x_i)-f(x_{i-1})\ge0$. Así,

$$
U(P)-L(P)=\sum_i[f(x_i)-f(x_{i-1})]\Delta_i
\le\|P\|\sum_i[f(x_i)-f(x_{i-1})].
$$

La suma derecha telescopa a $f(b)-f(a)\ge0$, y por tanto se obtiene la cota requerida. No se presupone continuidad; el argumento sólo usa monotonía y suma finita.

### Solución 4.24 (`EDC-C04-SOL-024`)

El teorema de valores extremos asegura que $m_i$ y $M_i$ existen **como números alcanzados** sobre cada intervalo cerrado $[x_{i-1},x_i]$. La continuidad uniforme proporciona, para $\eta=\varepsilon/[2(b-a)]$, un $\delta>0$ común a todas las posiciones, tal que $|f(x)-f(y)|<\eta$ si $|x-y|<\delta$. Con $\|P\|<\delta$, los puntos de mínimo y máximo de cada subintervalo distan menos que $\delta$, luego $M_i-m_i<\eta$. Sumando,

$$
0\le A_+(P)-A_-(P)
<\eta\sum_i\Delta_i
=\varepsilon/2<\varepsilon.
$$

No bastaría una continuidad expresada mediante un $\delta$ que variara sin control de un subintervalo a otro.

### Solución 4.25 (`EDC-C04-SOL-025`)

Por inducción $R_n\le R_0(2/3)^n$; el caso $n=0$ es inmediato y el paso sigue multiplicando por $2/3$. Como $3/2>1$, la desigualdad binomial da $(3/2)^n\ge1+n/2$. En consecuencia,

$$
R_n\le\frac{R_0}{(3/2)^n}\le\frac{R_0}{1+n/2}\to0.
$$

Dado $\varepsilon>0$, basta escoger $n>2(R_0/\varepsilon-1)$, o cualquier entero mayor suficientemente grande si el lado derecho fuese negativo. Sólo se han usado estimaciones finitas y el principio arquimediano.

### Solución 4.26 (`EDC-C04-SOL-026`)

Tomemos $F(x)=x^{p+1}/(p+1)$. En cada intervalo $[x_{i-1},x_i]$ el valor medio proporciona $\xi_i$ con

$$
F(x_i)-F(x_{i-1})=\xi_i^p\Delta_i.
$$

Como $x^p$ es creciente sobre $[0,1]$,

$$
x_{i-1}^p\Delta_i\le F(x_i)-F(x_{i-1})\le x_i^p\Delta_i.
$$

Al sumar, la expresión central telescopa a $1/(p+1)$; por tanto $L(P)\le1/(p+1)\le U(P)$. Además,

$$
U(P)-L(P)=\sum_i(x_i^p-x_{i-1}^p)\Delta_i
\le\|P\|\sum_i(x_i^p-x_{i-1}^p)=\|P\|.
$$

Esto prueba la aproximación independiente del reparto particular de anchuras, sin definir una integral general.

## F. Descubrimiento y síntesis

### Solución 4.27 (`EDC-C04-SOL-027`)

Una partición uniforme de $n$ intervalos tiene finura $1/n$, y para $x^2$ la diferencia extrema es exactamente $1/n$. Si escogemos $n=2^{10}=1024$, entonces

$$
U(P)-L(P)=\frac1{1024}<\frac1{1000}.
$$

Nueve duplicaciones no bastan, pues $1/512>1/1000$. La elección depende de la precisión solicitada y no de un cálculo previo de áreas curvilíneas.

### Solución 4.28 (`EDC-C04-SOL-028`)

Sea $f(x)=-2x^2+5x+1$ y $\ell(x)$ la cuerda interpolante en $x=1$ y $x=3$. La diferencia $f-\ell$ es cuadrática, tiene ceros $1$ y $3$ y coeficiente principal $-2$. Luego

$$
f(x)-\ell(x)=-2(x-1)(x-3)=2(x-1)(3-x).
$$

La anchura horizontal es $2$, así que el triángulo principal entre arco y cuerda tiene

$$
T=\frac{2\cdot2^3}{8}=2.
$$

El área del segmento parabólico es $4T/3=8/3$. La cuerda puede ser oblicua y parte de la gráfica puede tener valores negativos sin afectar el área **entre** la parábola y su cuerda.

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

Para cualquier partición y muestras $\xi_i$, por linealidad **finita** de la suma,

$$
S(P,\xi;f_\lambda)
=(1-\lambda)S(P,\xi;x^2)+\lambda S(P,\xi;x).
$$

El Ejercicio 4.26 con $p=2$ muestra que cualquier suma etiquetada de $x^2$ queda entre sus sumas extremas, y que $1/3$ pertenece al mismo intervalo de anchura a lo sumo $\|P\|$. Por tanto,

$$
\left|S(P,\xi;x^2)-\frac13\right|\le\|P\|.
$$

Aplicando el mismo argumento a $p=1$, obtenemos

$$
\left|S(P,\xi;x)-\frac12\right|\le\|P\|.
$$

Así, para todo $\lambda\ge0$,

$$
\begin{aligned}
\left|S(P,\xi;f_\lambda)-\left(\frac{1-\lambda}{3}+\frac\lambda2\right)\right|
&\le|1-\lambda|\left|S(P,\xi;x^2)-\frac13\right|
+\lambda\left|S(P,\xi;x)-\frac12\right|\\
&\le(|1-\lambda|+\lambda)\|P\|.
\end{aligned}
$$

El candidato se simplifica a $1/3+\lambda/6$. La cota es independiente del número de subintervalos y de las muestras particulares; si la finura tiende a cero, el error también. Hemos probado este caso especial de cuadratura por combinaciones finitas de dos funciones controladas, sin recurrir al teorema de linealidad de una integral que todavía no se ha construido.

---

**Control de cobertura:** `EDC-C04-SOL-001--030` corresponde biunívocamente a `EDC-C04-EXR-001--030`. Las pruebas geométricas usan sólo propiedades de áreas poligonales; los resultados de derivadas y valor medio se emplean únicamente allí donde el enunciado lo indica expresamente. Ninguna respuesta se obtiene invocando C05 o C06.
