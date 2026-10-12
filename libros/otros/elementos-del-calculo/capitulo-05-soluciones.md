---
title: Capítulo 5 — Soluciones desarrolladas
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
source-id: EDC-C05-SOLUCIONES
source-sha256: 52ab27aa9ff5f048e72af38a50de7b337a7f5f078f96be33542909a1b98ea7eb
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-05.html) · [Ejercicios](capitulo-05-ejercicios.html) · [Soluciones](capitulo-05-soluciones.html) · [Notas históricas](capitulo-05-notas.html)

Las soluciones distinguen los problemas de existencia de los de evaluación; todas utilizan únicamente C00–C05. Cada demostración se ofrece en el dominio indicado y no usa el Teorema Fundamental del Cálculo. Las identidades de valores de integrales de potencias se apoyan en el agotamiento numérico de C04, no en una primitiva general.

## A. Definiciones, supremos y lenguaje

### Solución 5.1 (`EDC-C05-SOL-001`)

Para una partición $P=\{a=x_0<\cdots<x_n=b\}$, ponemos $m_i=\inf_{[x_{i-1},x_i]}f$ y $M_i=\sup_{[x_{i-1},x_i]}f$. Entonces $L(f,P)=\sum_im_i\Delta_i$, $U(f,P)=\sum_iM_i\Delta_i$; sus extremos globales son $\underline{\mathcal I}(f)=\sup_P L(f,P)$ y $\overline{\mathcal I}(f)=\inf_P U(f,P)$. La acotación de $f$ garantiza que los $m_i,M_i$ sean números reales finitos y que los conjuntos de sumas estén acotados. El supremo no necesita pertenecer al conjunto; por ejemplo, el conjunto $(0,1)$ tiene supremo $1$ pero no máximo. Si ambos valores globales coinciden, la función es integrable; la mera existencia por separado de las integrales superior e inferior no basta.

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

El refinamiento común es

$$
R=P\cup Q=\left\{0,\frac13,\frac12,\frac23,1\right\}.
$$

Como $R$ contiene todos los puntos de ambas particiones, el Lema 5.1 implica $L(f,P)\le L(f,R)$ y $U(f,R)\le U(f,Q)$. Como $L(f,R)\le U(f,R)$ para cualquier función acotada, se sigue $L(f,P)\le U(f,Q)$. La prueba no exige que $f$ sea monótona, positiva o continua.

### Solución 5.7 (`EDC-C05-SOL-007`)

Por densidad de racionales e irracionales, toda pieza no degenerada de cualquier partición contiene puntos donde $d$ vale $0$ y otros donde vale $1$. Así sus ínfimos son $0$ y sus supremos $1$, de donde

$$
L(d,P)=\sum_i0\Delta_i=0,
\qquad U(d,P)=\sum_i1\Delta_i=1.
$$

Por tanto $\underline{\mathcal I}(d)=0$, $\overline{\mathcal I}(d)=1$. Como no coinciden, la función no es integrable. No se corrige la diferencia refinando: el salto de oscilación ocurre en **todas** las escalas.

### Solución 5.8 (`EDC-C05-SOL-008`)

La función es no negativa y sólo difiere de cero en un punto. Por el Lema 5.3 es integrable y su integral es $0$. Para obtener una cota concreta, una partición $P$ puede tener como máximo dos subintervalos cerrados que contienen $1/2$. Sólo en esos intervalos el supremo puede ser $5$; el ínfimo es $0$ en todos. La longitud total de esos subintervalos no supera $2\|P\|$, así que

$$
0\le U(h,P)-L(h,P)=U(h,P)\le10\|P\|.
$$

La cota no requiere que el punto $1/2$ sea un vértice de $P$: funciona también cuando cae en el interior de un solo subintervalo.

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

El teorema del valor medio de C03 da, para $x,y\in[0,2]$,

$$
|f(x)-f(y)|\le3|x-y|.
$$

Por tanto la oscilación en cada $[x_{i-1},x_i]$ está acotada por $3\Delta_i$, y

$$
U(f,P)-L(f,P)\le3\sum_i\Delta_i^2
\le3\|P\|\sum_i\Delta_i=6\|P\|.
$$

Para asegurar una diferencia estrictamente menor que $10^{-3}$ basta exigir $\|P\|<1/6000$. Hemos usado $|f'|\le3$ y el valor medio, no una regla de integración.

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

Si los valores globales coinciden en $I$, entonces por la propiedad de ínfimo existe $P_1$ con $U(f,P_1)<I+\varepsilon/2$. Por la propiedad de supremo existe $P_2$ con $L(f,P_2)>I-\varepsilon/2$. Esas particiones pueden ser incompatibles. Al tomar $R=P_1\cup P_2$, el lema de refinamiento asegura

$$
U(f,R)-L(f,R)
\le U(f,P_1)-L(f,P_2)<\varepsilon.
$$

La prueba usa la completitud real para garantizar el valor global y la compatibilidad entre particiones para poner juntas las dos estimaciones; ninguna de esas partes puede reemplazarse por la afirmación no demostrada de que «se afina la malla».

### Solución 5.16 (`EDC-C05-SOL-016`)

Fuera de los intervalos que contienen el punto de salto $c$, la función es constante, así que cada contribución es exactamente la constante correspondiente multiplicada por la anchura del subintervalo. Si $c$ cae en el interior de un intervalo de la partición, ese intervalo tiene longitud a lo sumo $\delta$ y sólo allí difieren la suma etiquetada y la longitud $b-c$, en valor absoluto a lo sumo $\delta$. Si $c$ es un vértice, puede aparecer un efecto de la etiqueta del intervalo a la izquierda, porque éste incluye el extremo $c$ donde $s_c(c)=1$, de nuevo con error a lo sumo $\delta$. Por tanto vale la cota pedida $|S(s_c;P,\xi)-(b-c)|\le2\delta$ en ambos casos (de hecho puede mejorarse a $\delta$). La estimación cubre **cualquier** etiqueta, no sólo las muestras de extremos convenientes.

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

La función $|2x-1|$ es continua en $[0,1]$ y por tanto integrable. Su gráfica consta de dos segmentos lineales que forman triángulos de base $1/2$ y altura $1$, uno a cada lado de $x=1/2$. Cada triángulo tiene área $(1/2)\cdot1/2=1/4$. Como las áreas de estas funciones afines se justifican por sumas de trapecios exactas —y el Teorema 5.8 permite dividir en $1/2$—,

$$
\int_0^1|2x-1|\,dx=\frac14+\frac14=\frac12.
$$

No se ha derivado ninguna primitiva; el cálculo usa la integral ya definida y sumas de funciones afines.

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

Para $a<u<v<b$, aplicamos primero el Teorema 5.8 en $u$ al intervalo $[a,b]$, obteniendo integrabilidad en $[u,b]$, y luego lo aplicamos a este último intervalo cortando en $v$: se obtiene integrabilidad en $[u,v]$. Si $u=a$, omitimos el primer corte; si $v=b$, omitimos el segundo. También puede demostrarse refinando directamente cualquier partición suficientemente buena de $[a,b]$ por los puntos $u,v$, porque la diferencia global se descompone en diferencias no negativas de cada pieza. Los intervalos degenerados $u=v$ tienen integral cero por definición.

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

Para $|f|\le A$, $|g|\le B$ y $x,y$ en el mismo intervalo cerrado $I$,

$$
|f(x)g(x)-f(y)g(y)|
\le|f(x)|\,|g(x)-g(y)|+|g(y)|\,|f(x)-f(y)|.
$$

Los supremos sobre pares dan $\operatorname{osc}_I(fg)\le A\operatorname{osc}_I(g)+B\operatorname{osc}_I(f)$. Multiplicamos por la longitud de cada subintervalo y sumamos. Como la integrabilidad de $f$ y de $g$ podría proporcionar **particiones distintas**, su refinamiento común permite hacer simultáneamente pequeñas ambas oscilaciones ponderadas; el refinamiento nunca aumenta $U-L$. Así el producto satisface el criterio de Darboux. La cota $A,B$ es uniforme porque $f,g$ son acotadas en todo $[a,b]$.

### Solución 5.29 (`EDC-C05-SOL-029`)

La función constante $-2$ tiene todas sus sumas etiquetadas iguales a $-2(3-0)=-6$, así que su integral es $-6$. El área geométrica de un rectángulo de base $3$ y altura positiva $2$ es $6$. La integral no es la magnitud absoluta de esa superficie cuando la función es negativa: es la acumulación **orientada**, o área algebraica. Si la constante expresa una velocidad $-2\,\mathrm{m/s}$ durante $3\,\mathrm{s}$, la integral representa desplazamiento de $-6\,\mathrm{m}$, no distancia recorrida negativa.

## G. Síntesis rigurosa

### Solución 5.30 (`EDC-C05-SOL-030`)

La función $x^2$ es continua y, por tanto, integrable. La función $s(x)=\mathbf1_{[1/2,1]}(x)$ es monótona, y la solución de la función escalón demuestra $\int_0^1s=1/2$. Por linealidad, para todo $\lambda\ge0$,

$$
\boxed{\int_0^1f_\lambda(x)\,dx=\frac13+\frac\lambda2.}
$$

Para cualquier partición $P$ con etiquetas $\xi$, el control de C04 para $x^2$ encierra tanto $S(x^2;P,\xi)$ como $1/3$ entre las sumas extremas, cuya diferencia no supera $\|P\|$. Así,

$$
\left|S(x^2;P,\xi)-\frac13\right|\le\|P\|.
$$

La solución 5.16, aplicada a $s$ con $c=1/2$, da $|S(s;P,\xi)-1/2|\le2\|P\|$. Usando la linealidad **finita** de las sumas y la desigualdad triangular concluimos

$$
\begin{aligned}
\left|S(f_\lambda;P,\xi)-\left(\frac13+\frac\lambda2\right)\right|
&\le\left|S(x^2;P,\xi)-\frac13\right|
+\lambda\left|S(s;P,\xi)-\frac12\right|\\
&\le(1+2\lambda)\|P\|.
\end{aligned}
$$

La cota depende de $\lambda$ y de la finura, **no** del número de subintervalos ni de la elección de etiquetas. Esto muestra concretamente el sentido cuantificado de la equivalencia Riemann–Darboux. No se ha empleado el Teorema Fundamental.

---

**Auditoría de cobertura:** exactamente un desarrollo `EDC-C05-SOL-001--030` por cada `EDC-C05-EXR-001--030`; todas las partes numéricas, conceptuales y demostrativas están respondidas.
