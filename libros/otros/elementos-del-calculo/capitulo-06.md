---
title: Capítulo 6. El Teorema Fundamental del Cálculo
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
source-id: EDC-C06
source-sha256: 1841eb1bed03cda7d235c93a4664e56ead67822d7026b416be6bf2b8c53eb169
content-id: MA-BCH-0232
content-type: book-chapter
related:
- MA-BOK-0015
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-06.html) · [Ejercicios](capitulo-06-ejercicios.html) · [Soluciones](capitulo-06-soluciones.html) · [Notas históricas](capitulo-06-notas.html)

[← Capítulo 5](capitulo-05.html) · [Capítulo 7 →](capitulo-07.html)

> **Pregunta generadora.** ¿Por qué la acumulación de una magnitud variable puede recuperarse mediante una derivada, y por qué conocer una primitiva permite calcular una integral sin volver a sumar rectángulos?

Durante los capítulos anteriores hemos seguido dos caminos. En el primero, las pendientes de secantes y las velocidades medias dieron lugar a la derivada: una razón de cambio local definida por un límite. En el segundo, las cuadraturas y las sumas de rectángulos condujeron a la integral de Riemann–Darboux: un número definido cuando todas las aproximaciones suficientemente finas son compatibles. Ninguna de estas construcciones necesitó suponer que derivar e integrar fueran operaciones inversas. De hecho, demostrar su relación sería imposible si hubiéramos definido la integral como «la diferencia entre los valores de una primitiva»: tal definición **supondría la conclusión** que queremos obtener.

Ahora contamos con ambas teorías y con el teorema del valor medio. Podemos formular, por primera vez y sin circularidad, su conexión central. La primera parte afirma que la integral acumulada de una función continua es derivable y que su derivada recupera la función. La segunda parte permite evaluar la integral a partir de **cualquier** primitiva apropiada. Veremos por qué son afirmaciones relacionadas, pero lógicamente diferentes, y por qué sus condiciones de aplicación deben permanecer visibles.

## 6.1. El problema de sumar mientras el extremo se mueve

Sea $a<b$ y sea $f:[a,b]\to\mathbb R$ continua. Para cada $x\in[a,b]$ ya tenemos, gracias al Teorema 5.4 (`EDC-C05-THM-004`) y a la aditividad (`EDC-C05-THM-008`), un número bien definido:

$$
F(x)=\int_a^x f(t)\,dt.
$$

La letra $t$ es una **variable muda de integración**: sustituirla por $u$ no modifica el número. En cambio, $x$ es el **extremo variable**; cambiarlo sí modifica la acumulación. Si $f\ge0$, $F(x)$ puede interpretarse como área bajo la gráfica desde $a$ hasta $x$. Si $f$ toma valores negativos, $F$ representa una acumulación *con signo*, no la suma de áreas geométricas sin orientación.

En la parábola $f(t)=t^2$ sobre $[0,1]$, las sumas y sus cotas ya mostraron que $\int_0^x t^2\,dt=x^3/3$ para $0\le x\le1$ (el cambio de escala en las sumas es suficiente). La derivada de $x^3/3$ vale $x^2$. Esta coincidencia es un indicio, **no** una prueba general: debemos explicar por qué sucede para toda función continua, aunque no conozcamos ninguna expresión algebraica para su integral.

## 6.2. Las herramientas: aditividad, orden y orientación

**Lema 6.1 (cotas del incremento; `EDC-C06-LEM-001`).** Sea $f:[a,b]\to\mathbb R$ integrable, $a\le u<v\le b$, y sean

$$
m_{u,v}=\inf_{t\in[u,v]}f(t),\qquad M_{u,v}=\sup_{t\in[u,v]}f(t).
$$

Entonces

$$
m_{u,v}(v-u)\le\int_u^v f(t)\,dt\le M_{u,v}(v-u).
$$

Si $f$ es continua, el ínfimo y el supremo son mínimo y máximo alcanzados. Para $h\ne0$ y $x,x+h\in[a,b]$, el cociente

$$
\frac{1}{h}\int_x^{x+h}f(t)\,dt
$$

queda entre el ínfimo y el supremo de $f$ en el intervalo cerrado comprendido entre $x$ y $x+h$, **tanto si $h>0$ como si $h<0$**.

**Demostración.** Las constantes $m_{u,v}\le f\le M_{u,v}$ son integrables. Aplicamos la monotonía y la integral de una constante demostradas en C05. Si $h>0$, dividimos la desigualdad resultante por $h>0$. Si $h<0$, escribimos $\int_x^{x+h}f=-\int_{x+h}^x f$ y dividimos por $h<0$; ambos cambios de signo se compensan. $\square$

Este lema concentra el argumento sin pedir un teorema de derivación: **se apoya exclusivamente en la integral previamente construida**. Es la versión exacta de encerrar una franja de acumulación entre dos rectángulos.

**Lema 6.2 (oscilación local; `EDC-C06-LEM-002`).** Si $f$ es continua en $c\in[a,b]$, entonces, para todo $\varepsilon>0$, existe $\delta>0$ tal que cualquier intervalo $J\subseteq[a,b]$ que contenga a $c$ y esté contenido en $(c-\delta,c+\delta)$ satisface

$$
\sup_{t\in J}|f(t)-f(c)|<\varepsilon.
$$

**Demostración.** Por continuidad relativa en $c$, elegimos $\delta$ de manera que $|f(t)-f(c)|<\varepsilon/2$ para todos los $t\in[a,b]$ con $|t-c|<\delta$. Entonces el supremo sobre $J$ no excede $\varepsilon/2<\varepsilon$. $\square$

![Gráfica de f(x)=x−1/2 entre cero y uno, área negativa de −1/8 bajo el eje a la izquierda y área positiva de +1/8 a la derecha.](/assets/books/elementos-del-calculo/EDC-C06-F01_ACUMULACION_ORIENTADA.svg)

*Figura 6.1.* La integral con signo suma las contribuciones orientadas y puede anularse sin que desaparezca el área geométrica total.

## 6.3. La función de acumulación es continua, aun antes de derivarla

**Definición 6.1 (función de acumulación; `EDC-C06-DEF-001`).** Para una función Riemann–Darboux integrable $f:[a,b]\to\mathbb R$, denominamos **función de acumulación con origen $a$** a

$$
\mathcal A_a f:[a,b]\to\mathbb R,\qquad (\mathcal A_a f)(x)=\int_a^x f(t)\,dt.
$$

En esta definición no exigimos que $f$ sea continua: la integrabilidad es suficiente para definir cada subintegral por el Teorema 5.8. Fijamos $F=\mathcal A_af$.

**Teorema 6.1 (continuidad de la acumulación; `EDC-C06-THM-001`).** Si $f$ es integrable y $|f(t)|\le M$ para todo $t\in[a,b]$, donde $M\ge0$, entonces

$$
|F(y)-F(x)|\le M|y-x|\qquad (x,y\in[a,b]).
$$

En consecuencia, $F$ es continua en $[a,b]$, incluso cuando $f$ no lo sea.

**Demostración.** Por aditividad orientada de la integral en C05,

$$
F(y)-F(x)=\int_x^y f(t)\,dt.
$$

Si $x<y$, la monotonía de la integral aplicada a $-M\le f\le M$ produce

$$
-M(y-x)\le F(y)-F(x)\le M(y-x).
$$

Para $y<x$ intercambiamos los puntos y usamos la orientación; para $x=y$ la diferencia es cero. Tomando valores absolutos resulta la estimación. Dado $\varepsilon>0$, si $M>0$ basta imponer $|x-y|<\varepsilon/M$; si $M=0$, $F$ es constante. $\square$

**Proposición 6.1 (monotonía de la acumulación; `EDC-C06-PRP-001`).** Si $f\ge0$, la función $F$ es no decreciente. Si $f\le0$, es no creciente. Más generalmente, si $m\le f\le M$, para $x<y$ se cumple

$$
m(y-x)\le F(y)-F(x)\le M(y-x).
$$

**Demostración.** Aplíquese el Lema 6.1 y la aditividad, sin derivar ninguna expresión. $\square$

Esta conclusión distingue **acumulación** de **derivación**: ya conocemos continuidad y variación global de $F$ sin haber probado que su derivada exista en un punto dado.

## 6.4. Primera parte: derivar una acumulación continua

**Teorema 6.2 (Teorema Fundamental, primera parte; `EDC-C06-THM-002`).** Sean $a<b$ y $f:[a,b]\to\mathbb R$ continua. Definamos

$$
F(x)=\int_a^x f(t)\,dt,\qquad a\le x\le b.
$$

Entonces $F$ es continua en $[a,b]$, derivable en $(a,b)$ y

$$
\boxed{F'(x)=f(x)\quad\text{para todo }x\in(a,b).}
$$

En los extremos existen las derivadas **relativas al intervalo**, $F'_+(a)=f(a)$ y $F'_-(b)=f(b)$; no se afirma una derivada bilateral en $a$ o en $b$ si $F$ sólo está definida sobre $[a,b]$.

**Demostración.** La continuidad se sigue del Teorema 6.1, pues $f$ es acotada por el teorema de valores extremos de C00. Fijemos $x\in(a,b)$ y tomemos $h\ne0$ tan pequeño que $x+h\in[a,b]$. La aditividad da

$$
\frac{F(x+h)-F(x)}h
=\frac1h\int_x^{x+h}f(t)\,dt.
$$

Por el Lema 6.1, este cociente está entre el menor y el mayor valor de $f$ en el intervalo $J_h$ determinado por $x$ y $x+h$. En particular,

$$
\left|\frac{F(x+h)-F(x)}h-f(x)\right|
\le\sup_{t\in J_h}|f(t)-f(x)|.
$$

Como $f$ es continua en $x$, el Lema 6.2 hace el miembro derecho menor que cualquier $\varepsilon>0$ cuando $|h|$ es suficientemente pequeño. Por definición de derivada (`EDC-C01-DEF-002`), $F'(x)=f(x)$. La misma estimación con $h>0$ en $a$ y con $h<0$ en $b$ prueba las derivadas laterales declaradas. $\square$

El teorema establece un vínculo **local**: una acumulación globalmente definida recupera la altura de la función justamente porque, en una franja muy estrecha, sus valores son cercanos a la altura en el punto considerado. La geometría sugiere el argumento; las desigualdades de Darboux lo demuestran.

### 6.4.1. Dos controles inmediatos

Para $f(t)=1$ en $[a,b]$, $F(x)=x-a$ y $F'(x)=1$. Si $f(t)=t^2$ sobre $[0,1]$, el cálculo por sumas establecido en C04–C05 da $F(x)=x^3/3$ y el teorema garantiza $F'(x)=x^2$. Pero su alcance es mucho mayor: para $f(t)=e^{-t^2}$ sobre $[0,1]$, la función

$$
H(x)=\int_0^x e^{-t^2}\,dt
$$

es derivable y $H'(x)=e^{-x^2}$, aunque **no hayamos hallado una expresión cerrada** para $H$. No hace falta demostrar aquí si esa primitiva admite o no una expresión mediante funciones elementales: la existencia y su derivada ya son consecuencias rigurosas del teorema.

## 6.5. Qué sucede si la función no es continua

**Teorema 6.3 (primera parte, versión puntual; `EDC-C06-THM-003`).** Sea $f:[a,b]\to\mathbb R$ integrable, y sea $c\in(a,b)$ un punto donde $f$ es continua. Entonces $F=\mathcal A_af$ es derivable en $c$ y $F'(c)=f(c)$.

**Demostración.** El Lema 6.1 sólo necesitó integrabilidad, no continuidad. Aplicamos a $c$ exactamente la estimación de la prueba anterior; la continuidad **en ese único punto** hace tender a cero la oscilación de $f$ sobre $J_h$. $\square$

La continuidad global es, pues, una condición suficiente cómoda para obtener derivabilidad **en todos** los puntos interiores, pero no es una condición necesaria para que exista la integral ni para derivar la acumulación en un punto particular.

**Contraejemplo A (una discontinuidad removible).** En $[-1,1]$ fijemos

$$
r(t)=\begin{cases}0,&t=0,\\1,&t\ne0.\end{cases}
$$

Por el Lema 5.3 y linealidad, $r$ es integrable; además, $\int_{-1}^x r(t)\,dt=x+1$ para todos los $x\in[-1,1]$. La acumulación tiene derivada $1$ en $0$, pero $r(0)=0$. **Ser integrable no obliga a que la derivada de la acumulación coincida con el valor del integrando en un punto de discontinuidad.**

**Contraejemplo B (un salto).** Sea $s(t)=0$ si $t<0$ y $s(t)=1$ si $t\ge0$, sobre $[-1,1]$. La función es monótona e integrable por C05. Su acumulación es

$$
S(x)=\int_{-1}^x s(t)\,dt=
\begin{cases}0,&-1\le x\le0,\\x,&0\le x\le1.\end{cases}
$$

En $x=0$, las derivadas laterales de $S$ son $0$ y $1$. No existe derivada bilateral allí. La continuidad de $S$ no está en duda: fue demostrada para todas las acumulaciones de funciones acotadas integrables.

No debe confundirse el significado de estos ejemplos: un integrando discontinuo puede producir una acumulación derivable o no derivable en el punto conflictivo. La hipótesis de continuidad **asegura** el resultado general; su falta obliga a examinar cada caso.

## 6.6. Primitivas y constantes de integración

**Definición 6.2 (primitiva; `EDC-C06-DEF-002`).** Una función $G:[a,b]\to\mathbb R$ es una **primitiva** de $f:[a,b]\to\mathbb R$ en el intervalo si $G$ es continua en $[a,b]$, derivable en $(a,b)$ y satisface $G'(x)=f(x)$ para todo $x\in(a,b)$. La definición sólo exige derivadas interiores; los valores de $f$ en los extremos no intervienen en esa ecuación.

**Teorema 6.4 (unicidad salvo una constante; `EDC-C06-THM-004`).** Si $G$ y $H$ son primitivas de la misma función $f$ en $[a,b]$, entonces existe $C\in\mathbb R$ tal que

$$
G(x)=H(x)+C\qquad (a\le x\le b).
$$

**Demostración.** La diferencia $K=G-H$ es continua en el intervalo cerrado, derivable en su interior y tiene $K'(x)=0$. Para cualesquiera $u<v$ de $[a,b]$, el teorema del valor medio de C03 da un $c\in(u,v)$ con

$$
K(v)-K(u)=K'(c)(v-u)=0.
$$

Por tanto, $K$ es constante, incluso en los extremos por el mismo argumento. $\square$

**Corolario 6.1 (existencia para integrandos continuos; `EDC-C06-COR-001`).** Toda función continua $f:[a,b]\to\mathbb R$ posee una primitiva en el sentido anterior, a saber, $F(x)=\int_a^x f(t)\,dt$. Todas las demás tienen la forma $F+C$.

**Demostración.** La primera afirmación es la primera parte del Teorema Fundamental, que incluye continuidad en el intervalo cerrado; la segunda procede del Teorema 6.4. $\square$

La expresión «más una constante» no es una convención sin fundamento: es una **afirmación matemática sobre la diferencia de dos funciones**. Además, depende de que el dominio sea un intervalo; sobre dos intervalos separados podrían aparecer constantes diferentes.

## 6.7. Segunda parte: calcular una integral por una primitiva

**Teorema 6.5 (Teorema Fundamental, segunda parte; `EDC-C06-THM-005`).** Sean $a<b$ y $f:[a,b]\to\mathbb R$ continua. Si $G$ es una primitiva de $f$ en $[a,b]$, entonces

$$
\boxed{\int_a^b f(t)\,dt=G(b)-G(a).}
$$

**Demostración.** La primera parte construyó, sin emplear previamente esta fórmula, una primitiva $F(x)=\int_a^x f(t)\,dt$. Por el Teorema 6.4, $G(x)=F(x)+C$ en todo $[a,b]$. En particular,

$$
G(b)-G(a)=F(b)-F(a).
$$

Pero $F(a)=\int_a^a f=0$ por la convención de intervalo degenerado de C05, y $F(b)=\int_a^b f$. Se obtiene la identidad. $\square$

**Orden lógico de la demostración:** primero construimos la integral por Darboux (C05); después demostramos que la acumulación de un integrando continuo tiene derivada igual al integrando (Teorema 6.2); por último aplicamos el valor medio para establecer que dos primitivas difieren en una constante. No hemos utilizado la segunda parte para fundamentar la primera.

### 6.7.1. Una demostración directa por sumas

Existe otra vía instructiva que tampoco utiliza la primera parte. Sea $G$ continua en $[a,b]$, derivable en $(a,b)$, y $G'=f$ allí, con $f$ continua en $[a,b]$. Para **cada** partición $P:a=x_0<\cdots<x_n=b$, el teorema del valor medio aplicado a $G$ en cada subintervalo proporciona $\xi_i\in(x_{i-1},x_i)$ tal que

$$
G(x_i)-G(x_{i-1})=G'(\xi_i)(x_i-x_{i-1})=f(\xi_i)\Delta_i.
$$

Sumando las igualdades finitas se obtiene

$$
G(b)-G(a)=\sum_{i=1}^n f(\xi_i)\Delta_i.
$$

Como $f$ es integrable por continuidad, la equivalencia Darboux–Riemann del Teorema 5.3 garantiza que **cualquier** sucesión de tales sumas con finura tendente a cero converge a $\int_a^b f$. El lado izquierdo es el mismo para todas las particiones, así que coincide con la integral. Es una demostración independiente de la primera parte, y hace explícito el papel de las *sumas de Riemann* y del *teorema del valor medio*.

## 6.8. Una ampliación controlada: derivadas integrables

**Teorema 6.6 (versión para una derivada integrable; `EDC-C06-THM-006`).** Si $G:[a,b]\to\mathbb R$ es continua en $[a,b]$, derivable en $(a,b)$ y existe una función $f:[a,b]\to\mathbb R$ **integrable** con $f(x)=G'(x)$ para todos los $x\in(a,b)$, entonces

$$
\int_a^b f(t)\,dt=G(b)-G(a).
$$

No se exige continuidad de $f$; sus valores en $a$ y $b$ pueden elegirse arbitrariamente, siempre que la función resultante sea integrable.

**Demostración.** La demostración directa del §6.7.1 utilizó la continuidad de $f$ sólo para asegurar su integrabilidad. Aquí esta última es una hipótesis explícita. El teorema del valor medio proporciona de nuevo, en toda partición, una suma etiquetada que vale exactamente $G(b)-G(a)$, y el Teorema 5.3 obliga a su convergencia a la integral cuando la finura tiende a cero. $\square$

No afirmamos que la derivada de **toda** función derivable sea Riemann-integrable: semejante conclusión no se ha demostrado y, en general, es falsa. El teorema anterior vale precisamente cuando la integrabilidad está acreditada. La distinción importa porque una derivada puede ser discontinua, incluso en un punto donde la función original sí es derivable (ejemplo de C02).

## 6.9. Ejemplos: áreas, desplazamientos y acumulación

Las reglas de derivación de C02 permiten reconocer primitivas y, gracias al teorema, evaluar integrales ya construidas.

**Potencias.** Para un entero $n\ge0$ y $a<b$ reales, $G(x)=x^{n+1}/(n+1)$ es primitiva de $x^n$. Luego

$$
\int_a^b x^n\,dx=\frac{b^{n+1}-a^{n+1}}{n+1}.
$$

La fórmula no tiene excepción en $x=0$ cuando $n$ es entero no negativo. Para potencias reales $x^r$ con $x>0$ y $r\ne-1$ se obtiene la expresión análoga, siempre manteniendo el intervalo dentro de $(0,\infty)$. Para $r=-1$ interviene el logaritmo.

**Exponencial y logaritmo.** Dado que $(e^x)'=e^x$,

$$
\int_a^b e^x\,dx=e^b-e^a.
$$

Y, para $0<a<b$, como $(\ln x)'=1/x$,

$$
\int_a^b\frac{dx}{x}=\ln b-\ln a.
$$

**Trigonometría.** En cualquier intervalo real,

$$
\int_a^b\cos x\,dx=\sin b-\sin a,\qquad
\int_a^b\sin x\,dx=-\cos b+\cos a.
$$

En particular, $\int_0^{\pi}\sin x\,dx=2$. La interpretación geométrica coincide con el área sólo porque $\sin x\ge0$ en ese intervalo; en un intervalo con cambio de signo el valor integral puede registrar cancelaciones.

**Desplazamiento frente a distancia.** Si $s(t)$ es una posición diferenciable y $v(t)=s'(t)$ es continua, entonces

$$
\int_{t_0}^{t_1}v(t)\,dt=s(t_1)-s(t_0).
$$

Esta integral expresa el **desplazamiento neto**, no necesariamente la distancia recorrida. Cuando $v$ es continua, la distancia recorrida sin saltos de posición y con el movimiento representado por esta velocidad se calcula mediante $\int_{t_0}^{t_1}|v(t)|\,dt$; justificarlo en un modelo físico exige entender la distancia como suma de variaciones absolutas, no confundirla con el valor absoluto del desplazamiento.

## 6.10. Extremos variables e información de la regla de la cadena

La primera parte también permite diferenciar ciertas expresiones integrales compuestas, *sin* haber formulado todavía la técnica general de sustitución que estudiaremos en C07.

**Proposición 6.2 (extremos variables; `EDC-C06-PRP-002`).** Sea $f$ continua sobre un intervalo cerrado $[a,b]$. Sean $\alpha,\beta:J\to[a,b]$ derivables en un intervalo abierto $J\subseteq\mathbb R$. Entonces

$$
H(x)=\int_{\alpha(x)}^{\beta(x)}f(t)\,dt
$$

es derivable en $J$ y

$$
\boxed{H'(x)=f(\beta(x))\beta'(x)-f(\alpha(x))\alpha'(x).}
$$

**Demostración.** Fijemos $F(u)=\int_a^u f(t)\,dt$. En el interior de $[a,b]$ conocemos $F'=f$; en los extremos conocemos las derivadas laterales. Por aditividad,

$$
H(x)=F(\beta(x))-F(\alpha(x)).
$$

Cuando $\alpha(x),\beta(x)$ son interiores, la regla de la cadena de C02 prueba inmediatamente la fórmula. Si, por ejemplo, $\beta(x)=a$ en un punto interior de $J$, como $\beta(J)\subset[a,b]$, la función derivable $\beta$ tiene allí un mínimo local, de modo que $\beta'(x)=0$ por Fermat (C03). Por continuidad de $f$ y la versión lateral del Teorema 6.2, la expansión $F(a+u)-F(a)=f(a)u+o(|u|)$ para $u\ge0$ muestra que $(F\circ\beta)'(x)=f(a)\beta'(x)=0$. Se razona igual en $b$ y para $\alpha$. Así se justifican también los valores de frontera, en lugar de aplicar a ciegas una regla de la cadena bilateral fuera de su dominio. $\square$

**Ejemplo.** Para $-1<x<1$,

$$
\frac{d}{dx}\int_0^{x^2}e^{t^2}\,dt=2x e^{x^4}.
$$

No hemos encontrado una primitiva elemental de $e^{t^2}$; la fórmula se debe a la composición de la acumulación con el extremo $x^2$.

## 6.11. Condiciones y fronteras: qué permite y qué no permite el teorema

Las dos partes del Teorema Fundamental **no** dicen «toda integral se obtiene derivando» ni «toda derivada se integra sin condiciones».

Primero, la integral debe existir en el sentido desarrollado en C05. La función de Dirichlet, que vale $1$ sobre racionales y $0$ sobre irracionales, no es Riemann-integrable en $[0,1]$: no puede utilizarse para definir $F(x)=\int_0^x f$ mediante esa teoría. Segundo, aunque una función sí sea integrable, la identidad $F'(c)=f(c)$ requiere continuidad en $c$ para nuestro teorema puntual, y puede fallar en una discontinuidad (como en §6.5). Tercero, tener una primitiva derivable no basta *por sí solo* para afirmar la fórmula integral si no se ha justificado la integrabilidad de su derivada; el Teorema 6.6 explicita el requisito.

Hay una distinción geométrica igualmente decisiva. Para $f\ge0$, la integral mide el área bajo la gráfica sobre un intervalo; para $f$ con signos diferentes, mide una acumulación orientada. Además, las fórmulas valen en intervalos compactos donde las funciones cumplen sus hipótesis. Los límites infinitos y las singularidades internas se estudian mediante **integrales impropias**, que no se definen en este capítulo. Por ejemplo, $1/x$ no es una función acotada en $[0,1]$ y el teorema de hoy no autoriza escribir directamente $\int_0^1(1/x)\,dx$ como una integral propia.

La idea del Teorema Fundamental no es que ambos operadores se cancelen como símbolos formales en cualquier contexto; es que **dos construcciones matemáticas independientes se vuelven recíprocas bajo hipótesis verificables**.

## 6.12. Del parentesco histórico a la unidad demostrada

El problema de la relación entre tangentes y cuadraturas antecede a nuestras definiciones del siglo XIX. En el siglo XVII se discutieron curvas asociadas a áreas, métodos de tangentes, magnitudes fluyentes y sumaciones infinitesimales. Isaac Barrow articuló relaciones geométricas entre curvas y sus tangentes; Newton formuló métodos de fluxiones y cuadraturas; Leibniz elaboró una notación diferencial e integral de gran alcance. También James Gregory aparece en estudios especializados de la genealogía del teorema. **No** identificaremos sin más esas construcciones con las dos afirmaciones modernas en lenguaje de funciones continuas e integrales de Riemann–Darboux.

Esta cautela no debilita el interés histórico: muestra precisamente la transformación. Un vínculo que surgió de problemas geométricos y mecánicos encuentra ahora una demostración dentro de un sistema de definiciones explícitas. Los testimonios y las interpretaciones de la historiografía, incluidos desacuerdos en la manera de atribuir las primeras formulaciones, se consignan en [las notas históricas y de fuentes](capitulo-06-notas.html).

La identidad que reúne ambos caminos puede escribirse con toda su carga lógica:

$$
\boxed{\begin{gathered}
f\in C([a,b])\ \Longrightarrow\ F(x)=\int_a^x f(t)\,dt,\\[2pt]
F'(x)=f(x)\ (a<x<b),\\[2pt]
G'=f\ \Longrightarrow\ \int_a^b f(t)\,dt=G(b)-G(a).
\end{gathered}}
$$

Aquí $C([a,b])$ significa simplemente «funciones continuas sobre $[a,b]$», sin introducir espacios funcionales abstractos. La segunda implicación presupone que $G$ es continua en $[a,b]$ y derivable en $(a,b)$, como se precisó en el teorema.

### Mapa de dependencias

- **De C00:** continuidad, teoremas de extremos, límites y estimaciones puntuales.
- **De C01–C02:** derivada y aproximación lineal, reglas algebraicas, cadena y primitivas elementales reconocibles.
- **De C03:** teorema del valor medio y principio de Fermat, empleados para unicidad, sumas telescópicas y extremos variables.
- **De C05:** definición independiente de integral, integrabilidad de continuas, orden, aditividad y convergencia de sumas etiquetadas; esta es la base **no circular** de toda la construcción.
- **Aportaciones C06:** `EDC-C06-THM-001--006`, `LEM-001--002`, `PRP-001--002` y el Corolario 6.1.
- **No utilizado:** sustitución general ni integración por partes de C07; series de potencias/Taylor de C08–C09; teoría general de EDO, integración impropia, Lebesgue o análisis funcional.

### Trabajo del lector

Los [ejercicios](capitulo-06-ejercicios.html) trabajan separadamente las dos direcciones del teorema, el control de hipótesis, las orientaciones, los extremos variables y la crítica de inferencias inválidas. Se entregan [soluciones completas](capitulo-06-soluciones.html) con la misma numeración. Las fuentes históricas y sus distintos niveles de verificación aparecen en [las notas](capitulo-06-notas.html).
