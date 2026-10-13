---
title: Capítulo 11 — Soluciones desarrolladas
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
source-id: EDC-C11-SOLUCIONES
source-sha256: 9cbc478e8b01bd027b3b26a131b82a9c204bfca3b59aade6d1fc28476345e8ba
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-11.html) · [Ejercicios](capitulo-11-ejercicios.html) · [Soluciones](capitulo-11-soluciones.html) · [Notas históricas](capitulo-11-notas.html)

Cada solución responde exactamente a un problema de [C11](capitulo-11-ejercicios.html). No se añaden teoremas de análisis real o de EDO que el libro no haya demostrado. En las preguntas históricas se diferencia una conclusión documentada de la reconstrucción matemática moderna.

## A. Qué constituye una prueba en cálculo

### Solución 11.1 (`EDC-C11-SOL-001`)

Una expresión finita, como $\sum_{k=0}^n2^{-k}$ para un entero fijo $n$, es un número calculable mediante un número finito de operaciones. Una sucesión $A_n$ **converge** a $A$ si para cada $\varepsilon>0$ se pueden hacer suficientemente pequeñas todas las diferencias $|A_n-A|$. Una certificación añade una cota cuantitativa explícita $\varepsilon_n$ que tiende a cero. Para $A_n=2-2^{-n}$, se obtiene exactamente

$$
|A_n-2|=2^{-n}.
$$

La sucesión $\varepsilon_n=2^{-n}$ tiende a cero por la convergencia de potencias geométricas con razón $1/2$ (C00/C08). La Proposición 11.1 prueba $A_n\to2$. Para una tolerancia $\varepsilon>0$, podemos escoger $N$ con $2^{-N}<\varepsilon$; como las potencias decrecen, la misma desigualdad vale para todos los $n\ge N$. Ésta es la información que convierte los valores calculados en una aproximación certificada. Para cada $n$ finito queda todavía una diferencia positiva $2^{-n}$ respecto de dos.

### Solución 11.2 (`EDC-C11-SOL-002`)

(a) Falta controlar las **sumas de todas las colas**, no sólo el término general: $a_n=1/n\to0$, pero $\sum1/n$ diverge por agrupación diádica (C08). (b) Falta que, **para cada $x$ considerado**, los restos $R_n(x)$ tiendan a cero cuando $n\to\infty$: la función plana $g(x)=e^{-1/x^2}$ fuera de cero y $g(0)=0$ tiene derivadas de todo orden y Taylor nula, aunque $g(x)>0$ si $x\ne0$ (C09). (c) La cota local corresponde a un paso **que parte del dato exacto**; un segundo paso parte de un valor numérico ya perturbado. Falta estimar la transmisión del error mediante hipótesis sobre $F(t,u)-F(t,v)$, por ejemplo una cota Lipschitz, y resolver la recurrencia resultante. Hay dos cuestiones por resolver: cómo cambia la pendiente al perturbar el valor de partida y cómo se suman las perturbaciones a lo largo de los pasos. Una cota Lipschitz puede ayudar con la primera, pero todavía hay que desarrollar la recurrencia para la segunda. El símbolo $O(h^2)$ del resto local no contiene esas estimaciones globales.

### Solución 11.3 (`EDC-C11-SOL-003`)

La diferencia $h=f-g$ es continua en $[0,2]$, derivable en $(0,2)$ y satisface $h'=f'-g'=0$ en todo el interior. Dados $0\le u<v\le2$, el teorema del valor medio proporciona $\xi\in(u,v)$ con $h(v)-h(u)=h'(\xi)(v-u)=0$. Así $h$ es constante en el segmento. Su valor en cero es $f(0)-g(0)=3$, por lo que $f(x)=g(x)+3$ para todo $x\in[0,2]$. Es indispensable que la igualdad de derivadas se haya supuesto en **todo** el intervalo interior.

### Solución 11.4 (`EDC-C11-SOL-004`)

Las derivadas son $f'(x)=2x$ y $g'(x)=0$, de modo que ambas valen cero en $x=0$. Sin embargo $f(x)-g(x)=x^2$. En cualquier intervalo abierto que contenga cero hay $r\ne0$ y entonces $h(r)=r^2>0=h(0)$. Por consiguiente no es constante. El Teorema 11.1 exige $f'=g'$ en **todos los puntos interiores**, no en un punto aislado.

### Solución 11.5 (`EDC-C11-SOL-005`)

La función $f(x)=|x|$ es continua sobre $[-1,1]$ por la desigualdad $||x|-|y||\le|x-y|$. Para $h>0$, $[f(h)-f(0)]/h=1$; para $h<0$, vale $-1$. No existe derivada bilateral en cero. Aunque $f(-1)=f(1)=1$, Rolle exige derivabilidad en **todo** $(-1,1)$ y esta hipótesis falla en cero; no puede concluirse la existencia de una pendiente horizontal por dicho teorema. De hecho, donde existe, la derivada vale $-1$ a la izquierda y $+1$ a la derecha, nunca cero.

## B. Reconstruir mediante integral y cotas de error

### Solución 11.6 (`EDC-C11-SOL-006`)

Como $f\in C^1([0,1])$, la derivada $f'$ es continua en el segmento y, por C05, Riemann–Darboux integrable. La **segunda** parte del Teorema Fundamental C06 aplicada a la primitiva $f$ da

$$
\int_0^x f'(t)\,dt=f(x)-f(0)
\quad(0\le x\le1).
$$

Reorganizar prueba la identidad pedida. La **primera** parte reconstruye una primitiva a partir de un integrando continuo y ofrece la dirección recíproca, pero no es la que se acaba de aplicar para evaluar la integral de $f'$.

### Solución 11.7 (`EDC-C11-SOL-007`)

Por la reconstrucción de C06 y el Corolario 11.1,

$$
y(t)=4+\int_0^t3s^2ds=4+t^3.
$$

La derivada de $4+t^3$ es $3t^2$, y el valor en cero es cuatro. Si $z$ fuese otra función continua en $[0,2]$, derivable en $(0,2)$ con la misma derivada y el mismo dato en cero, el Teorema 11.1 fuerza $z-y$ a ser la constante cero. No se dividió por la incógnita.

### Solución 11.8 (`EDC-C11-SOL-008`)

Para cualquier $\varepsilon>0$, escogemos $\delta>0$ con $14\delta<\varepsilon$, $0<\delta<1/2$, e incluimos en la partición $0,1/2-\delta,1/2,1/2+\delta,1$. El punto $1/2$ pertenece a los dos subintervalos cerrados adyacentes. En cada uno hay valores cero y el valor excepcional siete, de modo que su ínfimo es cero y su supremo siete. Fuera de ellos la función es nula. La longitud afectada es $2\delta$, y por ello la diferencia entre las sumas sólo recibe esos dos aportes. Por tanto

$$
U(f,P)-L(f,P)\le14\delta<\varepsilon.
$$

El criterio de Darboux C05 demuestra integrabilidad. Como $f\ge0$, $L(f,P)=0$ para toda partición; la cota permite hacer $U(f,P)$ arbitrariamente pequeña y se concluye $\int_0^1f=0$. No se introdujo la noción de medida nula.

### Solución 11.9 (`EDC-C11-SOL-009`)

En cualquier subintervalo no degenerado de $[0,1]$ hay racionales e irracionales. Por ello el ínfimo de $d$ es cero y el supremo uno en **cada** subintervalo de cualquier partición $P$. Por definición,

$$
L(d,P)=\sum_i0\cdot\Delta x_i=0,
\qquad
U(d,P)=\sum_i1\cdot\Delta x_i=1.
$$

La integral inferior vale cero y la superior uno; nunca coinciden. La función está acotada pero no es Riemann–Darboux integrable (C05). Se ha mostrado una obstrucción mediante **todas** las particiones, no sólo algunas muestras escogidas.

### Solución 11.10 (`EDC-C11-SOL-010`)

Para $f(x)=x^2$ en $[0,1]$, $f'(x)=2x$ y $|f'(x)|\le2=M$. El Teorema 11.3 con $b-a=1$ y $n$ partes iguales da, sin importar las muestras,

$$
\left|\int_0^1x^2dx-\frac1n\sum_{i=1}^n\xi_i^2\right|
\le\frac{2}{2n}=\frac1n.
$$

Para que esta cota garantice un error **estrictamente** menor que $10^{-3}$, necesitamos $n>1000$; el menor entero que satisface la condición suficiente es $n=1001$. Para $n=1000$ sólo obtenemos la garantía $\text{error}\le10^{-3}$, que no es la desigualdad estricta pedida. Elegir $n=1001$ la asegura para todas las muestras, aunque una elección concreta podría alcanzar la tolerancia con menos rectángulos. El número calculado es el mínimo para esta condición suficiente, no una afirmación de que cualquier método necesite al menos tantos.

### Solución 11.11 (`EDC-C11-SOL-011`)

En la partición uniforme $x_i=i/n$ y con extremos derechos $\xi_i=i/n$, la suma es

$$
S_n=\sum_{i=1}^n\frac{2i}{n}\frac1n
=\frac{2}{n^2}\frac{n(n+1)}2=1+\frac1n.
$$

La integral exacta $\int_0^1 2x\,dx=1$ se obtiene mediante C06, así que $|S_n-1|=1/n$. En el Teorema 11.3 podemos tomar $M=2$ porque $f'=2$, y la cota da también $M/(2n)=1/n$: **hay igualdad** para las muestras de extremo derecho de esta función lineal. Podemos reconocer la igualdad en la prueba del teorema: la muestra está en un extremo, así que una de las longitudes $u,v$ es cero y $u^2+v^2=(u+v)^2$. Además, $2x$ es creciente y cada rectángulo derecho sobrestima su integral; al sumar, los errores tienen el mismo signo y la desigualdad triangular no pierde precisión. Por eso la cota se alcanza en este caso.

### Solución 11.12 (`EDC-C11-SOL-012`)

Para $0\le t\le h$, el valor medio C03 sobre $[0,t]$ implica $|f(t)-f(0)|\le4t$, puesto que $|f'|\le4$. Por linealidad y desigualdad de integrales propias,

$$
\left|\int_0^hf(t)dt-3h\right|
=\left|\int_0^h[f(t)-3]dt\right|
\le\int_0^h4t\,dt=2h^2.
$$

El valor medio permite pasar de una cota de la **derivada** a una cota de la variación **del integrando**; la integral acumula luego esa cota. Si $h=0$, ambos lados son cero.

## C. La frontera de las series y los desarrollos locales

### Solución 11.13 (`EDC-C11-SOL-013`)

En el bloque $2^k\le n<2^{k+1}$ hay $2^k$ términos y cada uno es al menos $1/2^{k+1}$. La suma del bloque vale al menos $1/2$. Tras sumar $m$ bloques completos, la suma parcial supera $m/2$ y, por lo tanto, no está acotada. Como los términos son positivos, la convergencia exigiría sumas parciales acotadas (C08). La serie diverge aunque $1/n\to0$. El término general pequeño es condición **necesaria**, nunca suficiente.

### Solución 11.14 (`EDC-C11-SOL-014`)

La identidad finita para $x\ne1$ es $\sum_{k=0}^N x^k=(1-x^{N+1})/(1-x)$. Si $|x|<1$, $x^{N+1}\to0$ y la suma vale $(1-x)^{-1}$. Si $x=1$, las sumas parciales valen $N+1$; si $x=-1$, alternan entre cero y uno. En ambos extremos divergen. El radio de convergencia es uno, con intervalo total $(-1,1)$. La expresión algebraica $(1-x)^{-1}$ está definida en $x=-1$, pero la serie no converge allí; la identidad con una **serie infinita** no hereda sin prueba todo el dominio de la función racional.

### Solución 11.15 (`EDC-C11-SOL-015`)

C08 probó que, en cualquier intervalo cerrado $[-r,r]$ con $r<1$, las sumas parciales y sus derivadas poseen cotas de colas que tienden a cero. El Teorema 8.9 legitima entonces derivar $F(x)=\sum_{n=0}^{\infty}x^n=(1-x)^{-1}$ término a término en $|x|<1$:

$$
\sum_{n=1}^{\infty}nx^{n-1}=F'(x)=\frac1{(1-x)^2}.
$$

En $x=-1$, el término general de la serie derivada es $n(-1)^{n-1}$, que no tiende a cero; por tanto la serie **diverge** allí. El miembro racional vale $1/4$ en $x=-1$, pero la serie derivada no posee suma allí. La diferenciación término a término se justificó en puntos interiores y no convierte una expresión racional definida en el borde en una suma convergente. El examen del término general basta para decidir este caso fronterizo.

### Solución 11.16 (`EDC-C11-SOL-016`)

Las tres primeras derivadas de $e^x$ (órdenes cero, uno y dos) valen $e^x$, así que $T_{2,0}e^x=1+x+x^2/2$. En el segmento $[0,x]$ para $0\le x\le1/2$, la derivada de orden tres es $e^t\le e^{1/2}$. Taylor–Lagrange C09 con orden dos garantiza

$$
|e^x-(1+x+x^2/2)|
\le\frac{e^{1/2}x^3}{3!}.
$$

En el centro $x=0$ el resto es cero. La cota es una **afirmación finita**, independiente de hacer tender a infinito el orden del polinomio.

### Solución 11.17 (`EDC-C11-SOL-017`)

Definimos $g(0)=0$ y $g(x)=e^{-1/x^2}$ para $x\ne0$. El Lema 9.1 probó que $|x|^{-m}e^{-1/x^2}\to0$ para todo entero $m\ge0$. Las derivadas fuera de cero tienen la forma $P_k(1/x)e^{-1/x^2}$, con $P_k$ polinómico. Para realizar la inducción, extendemos esa expresión por el valor cero en el centro. Su continuidad se obtiene término a término, pues cada monomio en $1/x$ queda dominado por una potencia que la exponencial vence según el Lema 9.1. Para demostrar la siguiente derivada en cero, dividimos $P_k(1/h)e^{-1/h^2}$ por $h$; aparece una potencia adicional de $1/h$, también cubierta por el mismo lema. El cociente incremental tiende a cero y la derivada siguiente se une continuamente. Así obtenemos $g\in C^\infty$ y $g^{(k)}(0)=0$ para todo $k$. Por ello la serie de Taylor en cero es $\sum_{k\ge0}0\cdot x^k=0$, convergente para **todos** los reales. Pero $g(x)>0$ si $x\ne0$: ninguna vecindad abierta de cero tiene igualdad entre la suma y $g$, por lo que $g$ no es analítica en cero.

### Solución 11.18 (`EDC-C11-SOL-018`)

La afirmación (i) exige: **para todo entero fijo $n$** y cada $\varepsilon>0$ existe $\delta=\delta(n,\varepsilon)>0$ tal que $0<|x-a|<\delta$ implica $|f(x)-T_{n,a}f(x)|/|x-a|^n<\varepsilon$. El límite se toma haciendo $x\to a$ **después de fijar $n$**. La afirmación (ii) exige: **para cada $x$ fijo del dominio** y cada $\varepsilon>0$ existe $N=N(x,\varepsilon)$ tal que todo $n\ge N$ cumple $|f(x)-T_{n,a}f(x)|<\varepsilon$. Ésta hace crecer $n$ con $x$ fijo. En la primera afirmación, el entorno permitido puede cambiar con el orden, porque $\delta$ depende de $n$. En la segunda, el índice necesario puede cambiar con el punto, porque $N$ depende de $x$; tampoco se afirma una cota común para todos los puntos. El ejemplo plano de la solución 11.17 satisface la primera para cada orden, pero en un $x\ne0$ fijo todos sus restos son el mismo valor positivo $g(x)$, por lo que viola la segunda.

## D. De las leyes diferenciales a las trayectorias

### Solución 11.19 (`EDC-C11-SOL-019`)

En $y'+2y=4$ el factor integrante es $\mu(t)=e^{2t}$. Entonces $(e^{2t}y)'=4e^{2t}$ y, con $y(0)=1$,

$$
e^{2t}y(t)=1+4\int_0^t e^{2s}ds
=1+2(e^{2t}-1).
$$

Por tanto $y(t)=2-e^{-2t}$. La derivada es $y'=2e^{-2t}$, por lo que $y'+2y=2e^{-2t}+4-2e^{-2t}=4$, y $y(0)=1$. Los coeficientes son continuos en toda $\mathbb R$; el Teorema 10.3 prueba tanto que la fórmula **existe globalmente** como que no hay otra solución con el mismo dato.

### Solución 11.20 (`EDC-C11-SOL-020`)

Para $c\ge0$ la función $y_c(t)=0$ si $t\le c$ y $y_c(t)=(t-c)^2/4$ si $t>c$ cumple $y_c(0)=0$. Para $t>c$, su derivada es $(t-c)/2=\sqrt{y_c(t)}$; para $t<c$, ambos lados son cero. En el punto de unión, el cociente incremental es cero para $h<0$ y $h/4$ para $h>0$. Sus límites coinciden en cero, por lo que la derivada existe en $c$. Fuera de ese punto, la derivada es cero a la izquierda y $(t-c)/2$ a la derecha; estas expresiones tienden a cero al acercarse a $c$, verificando también su continuidad. Elija $c=0$ y $c=1$ para dos soluciones diferentes; por ejemplo $y_0(1)=1/4$ y $y_1(1)=0$. El campo $F(y)=\sqrt{|y|}$ no es localmente Lipschitz en cero, pues $|F(h)-F(0)|/h=1/\sqrt h\to\infty$ para $h>0$. Por tanto falla una hipótesis de 10.6 y no aparece contradicción alguna.

### Solución 11.21 (`EDC-C11-SOL-021`)

En la rama $y>0$, separar la ecuación equivale a $B(y)=\int_1^ydu/u^2=1-1/y=t$ cuando $t_0=0$. Así $1/y=1-t$ y

$$
y(t)=\frac1{1-t},\qquad t<1.
$$

La fórmula verifica $y'=1/(1-t)^2=y^2$ y $y(0)=1$. La primitiva $B(u)=1-1/u$ lleva $(0,\infty)$ sobre $(-\infty,1)$: tiende a $-\infty$ en el extremo cero y a uno al crecer $u$. Como aquí $A(t)=t$, la inversa está disponible exactamente para $t<1$. El Teorema 10.5 proporciona unicidad en la rama positiva sobre ese intervalo conectado que contiene el dato. Al acercarse $t\uparrow1$, $y(t)\to+\infty$; una función real continua definida en un intervalo que atravesara uno no podría tener ese comportamiento, de modo que **no existe prolongación clásica finita** a través de $t=1$.

### Solución 11.22 (`EDC-C11-SOL-022`)

La solución exacta de $y'=y$, $y(0)=1$ es $y(t)=e^t$ (C10). El paso de Euler desde cero es $Y_1=1+hF(0,1)=1+h$. Su error exacto es $e^h-1-h$. Taylor–Lagrange de orden uno entre cero y $h$ proporciona un $\xi\in(0,h)$ con

$$
e^h-1-h=\tfrac12e^\xi h^2,
\qquad 0\le e^h-(1+h)\le\tfrac12e^h h^2.
$$

Para avanzar otra vez, Euler usa $Y_1$ en lugar de $e^h$; habría que controlar la diferencia de campos y la propagación de errores. La cota local sola no da una estimación global tras pasos repetidos.

### Solución 11.23 (`EDC-C11-SOL-023`)

Multiplicamos $y'+y=t$ por $e^t$. La derivada del producto es $(e^ty)'=te^t$, cuya integral entre cero y $t$ es $[(s-1)e^s]_0^t=(t-1)e^t+1$. Como $y(0)=0$,

$$
y(t)=t-1+e^{-t}.
$$

La derivada $y'=1-e^{-t}$ verifica $y'+y=(1-e^{-t})+(t-1+e^{-t})=t$. El teorema de EDO lineales C10 prueba unicidad global para **esta** clase, no la existencia de soluciones para cualquier campo continuo arbitrario.

## E. Reconstruir la historia sin anacronismos

### Solución 11.24 (`EDC-C11-SOL-024`)

Un parecido **matemático retrospectivo** es que ambos contextos utilizan aproximaciones geométricas cada vez más refinadas para controlar áreas o volúmenes: el agotamiento asociado a Arquímedes y los procedimientos comentados por Liu Hui sobre subdivisión de figuras. Se puede describir esa analogía sin afirmar que compartían un tratado, un mismo algoritmo o una transmisión directa. Sería anacrónico atribuirles la definición moderna de integral mediante $\sup_P L(f,P)=\inf_P U(f,P)$ o el lenguaje de límites $\varepsilon$–$\delta$. Las notas H1–H2 distinguen la historiografía consultada de los originales no colacionados.

### Solución 11.25 (`EDC-C11-SOL-025`)

Decir «identidades equivalentes» significa que expresiones y procedimientos transmitidos por autores de la escuela de Kerala pueden traducirse **en notación matemática contemporánea** a series de arctangente y funciones trigonométricas. La biografía de Madhava en MacTutor advierte que sus escritos matemáticos originales no se conservan y que parte de la información llega a través de Nilakantha o Jyesthadeva, posteriores. Una traducción moderna de esos resultados **no** demuestra que en ellos apareciera nuestra cuantificación de colas, un radio de convergencia definido como supremo ni el Teorema 8.9. Tampoco acredita por sí misma relaciones de transmisión a Europa: ésa sería otra hipótesis histórica a documentar.

### Solución 11.26 (`EDC-C11-SOL-026`)

La historiografía presenta el concepto newtoniano de *fluxión* en conexión con magnitudes variables en el tiempo y su tasa, mientras que la notación $d$ y $\int$ de Leibniz pone en primer plano la diferencia y la suma como operaciones. Las ideas poseen relación con tangentes y cuadraturas, pero sus documentos, cronologías de elaboración, circulación y publicación no son idénticos. El Teorema Fundamental tal como aparece en C06 presupone nuestras definiciones de integral de Riemann–Darboux, derivada y continuidad sobre reales; atribuir literalmente esa formulación a Newton o Leibniz sin cotejo de los originales produciría un anacronismo. Se trata de reconstrucción actual basada en una genealogía histórica, no de transcripción.

### Solución 11.27 (`EDC-C11-SOL-027`)

El orden correcto es **1715**, Brook Taylor, *Methodus incrementorum directa et inversa*; **1821**, Augustin-Louis Cauchy, *Cours d'analyse*; **1875**, Gaston Darboux, «Mémoire sur les fonctions discontinues». El primero está respaldado por fichas bibliográficas y la biografía secundaria estudiadas para C09; el segundo por la exposición de MacTutor de Cauchy; el tercero por el catálogo documental y metadatos de publicación de Numdam o EuDML, con páginas de revista 57–112. En ningún caso la sola fecha del registro implica que hayamos leído íntegramente el original en su lengua, ni prueba prioridades matemáticas exclusivas.

## F. Un examen de cierre matemático e histórico

### Solución 11.28 (`EDC-C11-SOL-028`)

Cinco falsas implicaciones y controles demostrados son: (1) **Continua $\Rightarrow$ derivable**: $|x|$ en cero la refuta (C01); la derivabilidad, cuando existe, sí implica continuidad (C01). (2) **Acotada $\Rightarrow$ Riemann–Darboux integrable**: indicadora de racionales sobre $[0,1]$ (C05); continuidad en el compacto sí es suficiente para integrabilidad (C05). (3) **$a_n\to0\Rightarrow\sum a_n$ converge**: la armónica (C08); el criterio de Cauchy sobre todas las colas es necesario y suficiente (C08). (4) **$C^\infty\Rightarrow$ Taylor representa a la función**: la función plana (C09); restos que tienden a cero sí aseguran representación en el punto considerado (C09). (5) **Campo continuo $\Rightarrow$ unicidad de PVI**: $y'=\sqrt{|y|}$ (C10); el campo Lipschitz en $y$ asegura unicidad **entre soluciones que ya existen** en el rectángulo correspondiente (C10). Las cinco respuestas tienen sus dominios y no extrapolan resultados más generales no probados.

### Solución 11.29 (`EDC-C11-SOL-029`)

Para $0\le x<1$ la potencia $x^n\to0$, y para $x=1$ vale uno. La función límite es

$$
f(x)=\begin{cases}0,&0\le x<1,\\1,&x=1.\end{cases}
$$

Para cada $n\ge1$, el error $|f_n(x)-f(x)|$ es $x^n$ si $x<1$ y cero si $x=1$. Como se pueden elegir $x<1$ tan próximos a uno como se quiera, $\sup_{x\in[0,1]}|f_n(x)-f(x)|=1$ para **todo** $n$. También podemos elegir un punto explícito para cada índice: $x_n=2^{-1/n}$ pertenece a $(0,1)$ y cumple $x_n^n=1/2$. Así el error sigue valiendo $1/2$ en esos puntos aunque $n$ crezca. Este punto cambia con el índice, por lo que el argumento es compatible con la convergencia para cada $x$ fijo. Si existiesen $\varepsilon_n\to0$ que dominaran el error en todos los puntos, tendríamos además $\varepsilon_n\ge1$ por el supremo calculado, contradicción. C08 obtuvo en cambio una cota común en segmentos $|x-c|\le r<s<R$ **estrictamente interiores**; éste es precisamente el tipo de control que aquí no existe en todo el intervalo hasta la frontera.

### Solución 11.30 (`EDC-C11-SOL-030`)

(a) La función $y(t)=e^{-t}$ es continua, y C06 garantiza

$$
A(x)=\int_0^x e^{-t}dt=1-e^{-x},\qquad A'(x)=e^{-x}=y(x)
$$

para $x\in(0,1)$, con derivadas laterales si se consideran los extremos; además $A(0)=0$.

(b) El integrando $y$ tiene $y'=-e^{-t}$, cuyo módulo no supera uno en $[0,1]$. Con $M=1$, el Teorema 11.3 certifica para **cualquier elección de muestras** en una partición uniforme de $n$ partes

$$
\left|\int_0^1 e^{-t}dt-\frac1n\sum_{i=1}^n e^{-\xi_i}\right|\le\frac1{2n}.
$$

(c) Como $A(x)=\int_0^x y(t)dt$, $y(0)=1$ y $|y'|\le1$, el Teorema 11.4 da $|A(x)-x|\le x^2/2$ para $0\le x\le1$. La desigualdad puede verse directamente en la diferencia de tasas: $|A(x)-x|\le\int_0^x|e^{-t}-1|dt$, y el valor medio aplicado a $e^{-t}$ da $|e^{-t}-1|\le t$ en ese segmento. Integrar produce $x^2/2$. Alternativamente, Taylor–Lagrange controla $1-e^{-x}-x$ con el mismo mayorante.

(d) La derivada $y'=-e^{-t}=-y$ y $y(0)=1$, por lo que existe una solución. El Teorema 10.2, aplicado al coeficiente continuo $a(t)=-1$, demuestra que es la **única** sobre $\mathbb R$ para ese dato.

(e) Las cuatro pruebas contestan preguntas distintas: (a) reconstruye una acumulación, (b) certifica un error de cuadratura, (c) cuantifica un error local de aproximación y (d) afirma existencia y unicidad para un PVI lineal. Ninguna de ellas acredita que un sistema físico real decaiga exactamente según $e^{-t}$: la elección de la ley sigue siendo una hipótesis de modelización que exige contraste experimental externo.

---

**Cobertura:** `EDC-C11-SOL-001--030` corresponde uno a uno a `EDC-C11-EXR-001--030`, sin usar teoría matemática posterior al cierre de C10.
