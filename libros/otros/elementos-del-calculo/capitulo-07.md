---
title: Capítulo 7. Integrar como método
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
source-id: EDC-C07
source-sha256: 41fddfc0c45c6e520f09af66d2fd218d67e3ef2c0d9d4f81c14c7727cb49702f
content-id: MA-BCH-0233
content-type: book-chapter
related:
- MA-BOK-0015
---

[Índice del libro](index.qmd) · [Prefacio](prefacio.md) · [Itinerarios](itinerarios.md)

[Exposición](capitulo-07.md) · [Ejercicios](capitulo-07-ejercicios.md) · [Soluciones](capitulo-07-soluciones.md) · [Notas históricas](capitulo-07-notas.md)

[← Capítulo 6](capitulo-06.md) · [Capítulo 8 →](capitulo-08.md)

> **Pregunta generadora.** Conocemos la definición rigurosa de integral y sabemos calcularla mediante primitivas. ¿Cómo reconocer una primitiva cuando el integrando es una composición, un producto o una función racional que no aparece en una tabla elemental?

Una definición no es por sí sola un procedimiento de cálculo. La integral de Riemann–Darboux, construida en el capítulo 5, determina un valor mediante cotas inferiores y superiores; el Teorema Fundamental, demostrado en el capítulo 6, permite reemplazar esa tarea por otra: buscar una función cuya derivada sea el integrando. Surge entonces un problema nuevo. La derivada de $e^{x^2}$ se obtiene en una línea, pero la función $e^{x^2}$ no entrega de inmediato una primitiva reconocible. La derivada de $x e^x$ obedece una regla sencilla, pero integrar $xe^x$ parece pedir una operación inversa.

En este capítulo no aprenderemos «trucos» aislados. **Reconstruiremos tres procedimientos a partir de identidades ya demostradas:** la sustitución desde la regla de la cadena, la integración por partes desde la regla del producto y las fracciones parciales desde el álgebra de polinomios. Cada operación se formulará en un intervalo en el que los objetos estén definidos, y cada integral definida conservará sus extremos y su orientación. Veremos, además, cómo decidir entre métodos, cómo medir acumulaciones físicas y qué límites tiene la búsqueda de expresiones elementales.

## 7.1. De una integral existente a una estrategia de cálculo

Consideremos

$$
I=\int_0^1 2x\,e^{x^2}\,dx.
$$

Por C02, la derivada de $x\mapsto e^{x^2}$ es $2xe^{x^2}$. Por C05 el integrando es continuo, luego integrable; por C06,

$$
I=[e^{x^2}]_0^1=e-1.
$$

La observación fundamental es que la expresión $2x$ no es un factor decorativo: es la derivada de la expresión $x^2$ que aparece dentro de la exponencial. La *estructura* del integrando nos conduce a su primitiva.

**Definición 7.1 (`EDC-C07-DEF-001`; primitiva sobre un intervalo).** Si $I\subseteq\mathbb R$ es un intervalo abierto y $f:I\to\mathbb R$, una primitiva de $f$ sobre $I$ es una función derivable $F:I\to\mathbb R$ tal que $F'=f$ en todos los puntos de $I$. Denotamos informalmente la familia de primitivas por

$$
\int f(x)\,dx=F(x)+C,\qquad C\in\mathbb R,
$$

cuando se sabe que $F$ existe. Esta notación **no define una segunda integral**: resume la afirmación sobre una familia de funciones cuya diferencia es constante, demostrada en C06 por el valor medio. En cada componente separada del dominio, la constante puede elegirse independientemente.

No toda expresión admite evaluación aplicando una única fórmula de potencias. Antes de transformar una integral conviene responder tres preguntas: ¿existe como integral propia sobre los extremos indicados?, ¿qué derivada conocida se oculta en el integrando?, ¿en qué intervalo puede realizarse el cálculo sin atravesar una singularidad? El orden importa. La identidad algebraica correcta no convierte en integrable una función no acotada en el intervalo cerrado.

## 7.2. El teorema de sustitución: deshacer la regla de la cadena

**Teorema 7.1 (sustitución orientada; `EDC-C07-THM-001`).** Sean $J\subseteq\mathbb R$ un intervalo abierto, $f:J\to\mathbb R$ continua, y $\phi:[\alpha,\beta]\to J$ una función continuamente derivable, con $\alpha<\beta$. Entonces

$$
\boxed{\int_\alpha^\beta f(\phi(t))\phi'(t)\,dt
=\int_{\phi(\alpha)}^{\phi(\beta)}f(u)\,du.}
$$

La función $\phi$ **no tiene que ser inyectiva ni monótona**. Los extremos de la derecha pueden coincidir o estar en orden inverso. En la izquierda y en la derecha las integrales existen en sentido propio.

**Demostración.** El recorrido compacto de $\phi$ está contenido en $J$. Elegimos $u_0\in J$ y definimos, para $u\in J$, $F(u)=\int_{u_0}^{u}f(s)\,ds$; la integral orientada existe porque el segmento entre $u_0$ y $u$ es compacto y está contenido en $J$. La primera parte del Teorema Fundamental (`EDC-C06-THM-002`) prueba que $F'(u)=f(u)$ para todo $u\in J$. Por la regla de la cadena (`EDC-C02-THM-002`),

$$
(F\circ\phi)'(t)=f(\phi(t))\phi'(t),\qquad \alpha<t<\beta.
$$

El producto de funciones continuas $f\circ\phi$ y $\phi'$ es continuo en $[\alpha,\beta]$; además, $F\circ\phi$ es continuo hasta los extremos. La segunda parte del Teorema Fundamental (`EDC-C06-THM-005`) da

$$
\int_\alpha^\beta f(\phi(t))\phi'(t)\,dt
=F(\phi(\beta))-F(\phi(\alpha))
=\int_{\phi(\alpha)}^{\phi(\beta)}f(u)\,du.
$$

La última igualdad usa la aditividad orientada demostrada en C05. No hubo sustitución formal de símbolos diferenciales sin justificación. $\square$

**Corolario 7.1 (sustitución en una primitiva; `EDC-C07-COR-001`).** Bajo las hipótesis locales de la regla de la cadena, si $F'=f$ en un intervalo que contiene $\phi(I)$, entonces

$$
\int f(\phi(x))\phi'(x)\,dx=F(\phi(x))+C
$$

sobre cada intervalo abierto $I$ donde la expresión esté definida. **Demostración.** Derivamos $F\circ\phi$ mediante la cadena; la descripción de todas las primitivas sigue del valor medio de C03. $\square$

La regla incluye cambios de variable que invierten la orientación. Si $\phi(t)=1-t$ para $t\in[0,1]$, entonces $\phi'(t)=-1$ y

$$
\int_0^1 -f(1-t)\,dt=\int_1^0 f(u)\,du
=-\int_0^1 f(u)\,du.
$$

La función compuesta se integra aquí con su derivada, **no con el valor absoluto** de ella. El valor absoluto aparece en otros problemas de medida geométrica, no en la fórmula orientada del teorema.

## 7.3. Transformar correctamente los extremos

El procedimiento operativo es útil precisamente porque deja ver qué se conserva. Si $u=\phi(x)$ en una integral **definida**, se convierten *ambos* extremos y se integra con respecto a $u$. Por ejemplo,

$$
\begin{aligned}
\int_0^1 x\sqrt{1+x^2}\,dx
&=\frac12\int_1^2\sqrt{u}\,du\\
&=\frac12\left[\frac23u^{3/2}\right]_1^2
=\frac{2\sqrt2-1}{3}.
\end{aligned}
$$

Se usó $u=1+x^2$, $du/dx=2x$ y $u(0)=1$, $u(1)=2$. La potencia $u^{1/2}$ es continua para $u>0$, de modo que todas las integrales escritas son propias.

Un cambio no monótono tampoco rompe el teorema. Tomemos $\phi(t)=t^2$ para $-1\le t\le1$. Entonces

$$
\int_{-1}^1 2t\,e^{t^2}\,dt=\int_1^1e^u\,du=0.
$$

Este resultado se entiende porque las contribuciones para $t<0$ y $t>0$ tienen signos opuestos. **No** describe el área sin signo bajo $2t e^{t^2}$. Si se hubiera reemplazado $2t$ por $|2t|$, se habría cambiado el problema.

**Proposición 7.1 (invariancia por traslación y escala afín; `EDC-C07-PRP-001`).** Sean $f$ continua en un intervalo abierto $J$ y $\phi(t)=ct+d$ con $c\ne0$. Para $\alpha<\beta$ tales que $\phi([\alpha,\beta])\subset J$,

$$
\int_\alpha^\beta f(ct+d)\,dt
=\frac1c\int_{c\alpha+d}^{c\beta+d}f(u)\,du.
$$

**Demostración.** En el Teorema 7.1 sustituimos $\phi'(t)=c$ y dividimos por $c\ne0$. Cuando $c<0$, la orientación de los nuevos extremos explica el signo final. $\square$

**Error a evitar.** No es correcto cambiar el integrando a $f(u)$ y conservar simultáneamente los viejos extremos de $x$; tampoco es correcto poner $du=\phi'(x)dx$ como una ecuación entre números independientes de la demostración. Esa abreviatura se admite sólo como memoria del teorema ya probado.

## 7.4. La regla del producto conduce a integración por partes

**Teorema 7.2 (integración por partes; `EDC-C07-THM-002`).** Sean $u,v:[a,b]\to\mathbb R$ funciones de clase $C^1$, con $a<b$; esto significa continuas en $[a,b]$, derivables en $(a,b)$ y con derivadas interiores que se prolongan continuamente a $[a,b]$. Entonces

$$
\boxed{\int_a^b u(x)v'(x)\,dx
=\bigl[u(x)v(x)\bigr]_a^b-\int_a^b u'(x)v(x)\,dx.}
$$

**Demostración.** La regla del producto de C02 produce $(uv)'=u'v+uv'$ en el interior. Los tres términos del lado derecho son continuos en $[a,b]$ según las prolongaciones indicadas; en particular, ambas integrales existen por C05. Como $uv$ es continua hasta los extremos, la segunda parte del Teorema Fundamental de C06 da

$$
[uv]_a^b=\int_a^b(u'v+uv')\,dx
=\int_a^b u'v\,dx+\int_a^b uv'\,dx.
$$

La fórmula sigue despejando el último término. $\square$

**Corolario 7.2 (forma indefinida; `EDC-C07-COR-002`).** En un intervalo abierto en el que $u,v$ sean derivables y los productos estén definidos, $uv$ es una primitiva de $u'v+uv'$. Siempre que alguno de los sumandos tenga primitiva, se puede escribir

$$
\int uv'\,dx=uv-\int u'v\,dx+C.
$$

**Demostración.** Es la igualdad de derivadas $(uv)'=u'v+uv'$ junto con la unicidad de primitivas salvo constante en intervalos. $\square$

La aplicación no consiste en «pasar una derivada al otro factor» sin costo: intercambia un integral por otro. Su valor depende de que el segundo sea más fácil, o de que el mismo integral aparezca otra vez y se pueda despejar algebraicamente.

## 7.5. Dos integraciones por partes reveladoras

**Primera: un polinomio por una exponencial.** Poniendo $u=x$, $v'=e^x$, $v=e^x$ en $[0,1]$,

$$
\int_0^1 xe^x\,dx=[xe^x]_0^1-\int_0^1e^x\,dx=e-(e-1)=1.
$$

La fórmula indefinida correspondiente es $\int xe^x\,dx=(x-1)e^x+C$; derivarla confirma el resultado. Si el factor polinómico tiene grado dos o mayor, repetir el procedimiento disminuye su grado:

$$
\int x^2e^x\,dx=e^x(x^2-2x+2)+C.
$$

**Segunda: un logaritmo que no presenta producto.** En $[1,e]$ escribimos $\ln x=(\ln x)\cdot1$ y elegimos $u=\ln x$, $v'=1$, de donde $u'=1/x$, $v=x$. Resulta

$$
\int_1^e\ln x\,dx=[x\ln x]_1^e-\int_1^e1\,dx=e-(e-1)=1.
$$

Aquí la restricción $x>0$ es indispensable; no existe un $\ln x$ real para $x\le0$ en nuestra definición de C02. Por la misma idea, una primitiva de $\ln x$ sobre $(0,\infty)$ es $x\ln x-x$.

**Proposición 7.2 (reducción polinomio–exponencial; `EDC-C07-PRP-002`).** Si $p$ es un polinomio de grado $n\ge0$, la función $p(x)e^x$ tiene sobre $\mathbb R$ una primitiva de la forma $e^x q(x)$ con $q$ polinomio de grado a lo sumo $n$. En particular se obtiene mediante un número finito de integraciones por partes.

**Demostración.** Escribimos $q=p-p'+p''-\cdots+(-1)^np^{(n)}$. La suma es finita porque $p^{(n+1)}=0$. De la regla del producto,

$$
\frac{d}{dx}(e^xq)=e^x(q+q')=e^xp,
$$

ya que todos los términos intermedios se cancelan. La integración por partes reproduce la misma cancelación paso a paso. $\square$

## 7.6. Cuando la integral reaparece: el método cíclico

Consideremos $I=\int e^x\cos x\,dx$ sobre $\mathbb R$. Aplicamos partes con $u=\cos x$, $v'=e^x$:

$$
I=e^x\cos x+\int e^x\sin x\,dx.
$$

A la integral nueva $J=\int e^x\sin x\,dx$ aplicamos partes con $u=\sin x$, $v'=e^x$:

$$
J=e^x\sin x-\int e^x\cos x\,dx.
$$

Para evitar ambigüedades entre familias que difieren en una constante, puede hacerse primero con integrales de $0$ a $x$. Sus identidades dan $2I(x)=e^x(\sin x+\cos x)-1$ para $I(x)=\int_0^xe^t\cos t\,dt$. De aquí resulta la familia de primitivas

$$
\boxed{\int e^x\cos x\,dx=\frac{e^x}{2}(\sin x+\cos x)+C.}
$$

Un control por derivación directa confirma el factor $1/2$. La repetición aquí **no** reduce el grado de una función: cierra un sistema de dos integrales y permite despejar una de ellas.

La decisión sobre el método es estructural: si aparece $f(g(x))g'(x)$ pensamos en cadena; si aparece $u(x)v'(x)$ cuyo intercambio simplifica, pensamos en producto. No hay un algoritmo universal que garantice una expresión elemental para cualquier integrando continuo.

## 7.7. Fracciones racionales y el trabajo algebraico previo

Una *función racional* es un cociente $R(x)=P(x)/Q(x)$ de polinomios, definido donde $Q(x)\ne0$. Sobre cada intervalo cerrado contenido en su dominio es continua e integrable por C05. Para encontrar primitivas, primero efectuamos la división polinómica si $\deg P\ge\deg Q$. El resto es una fracción propia, con numerador de grado menor que el denominador.

**Definición 7.2 (`EDC-C07-DEF-002`; fracción propia y descomposición parcial).** La fracción $P/Q$ es *propia* si $\deg P<\deg Q$ y $Q$ no es el polinomio nulo. Una *descomposición en fracciones parciales* es una identidad racional que expresa $P/Q$ como suma de fracciones con denominadores de factores más simples de $Q$, válida en el dominio original. La descomposición debe verificarse por una identidad de polinomios; no autoriza a rellenar puntos excluidos del dominio original.

**Teorema 7.3 (denominadores lineales simples; `EDC-C07-THM-003`).** Sea

$$
Q(x)=c\prod_{j=1}^m(x-r_j),\qquad c\ne0,
$$

con raíces reales $r_1,\ldots,r_m$ **distintas**, y sea $\deg P<m$. Entonces, para $x\notin\{r_1,\ldots,r_m\}$,

$$
\frac{P(x)}{Q(x)}=\sum_{j=1}^m\frac{A_j}{x-r_j},
\qquad A_j=\frac{P(r_j)}{Q'(r_j)}.
$$

**Demostración.** Como las raíces son simples, $Q'(r_j)=c\prod_{k\ne j}(r_j-r_k)\ne0$. Multipliquemos la identidad propuesta por $Q(x)$ y definamos

$$
H(x)=P(x)-\sum_{j=1}^m A_j\frac{Q(x)}{x-r_j}.
$$

Cada cociente $Q(x)/(x-r_j)$ es un polinomio de grado $m-1$. Por tanto, $H$ es un polinomio de grado menor que $m$. Al evaluar en $x=r_i$, todos los términos con $j\ne i$ se anulan; el término restante es $A_iQ'(r_i)=P(r_i)$. Así $H(r_i)=0$ para las $m$ raíces distintas. Un polinomio de grado menor que $m$ no puede tener $m$ raíces distintas salvo que sea idénticamente cero, como se prueba reiterando la factorización por $(x-r_i)$. Queda demostrada la identidad. $\square$

**Corolario 7.3 (primitiva racional en raíces simples; `EDC-C07-COR-003`).** Bajo las hipótesis del Teorema 7.3, en **cada intervalo abierto** que no contenga raíces de $Q$,

$$
\int\frac{P(x)}{Q(x)}\,dx
=\sum_{j=1}^m A_j\ln|x-r_j|+C.
$$

**Demostración.** En ese intervalo, $\frac{d}{dx}\ln|x-r_j|=1/(x-r_j)$ por C02. Derivamos la suma y usamos la identidad anterior. $\square$

**Ejemplo.** Para $x\ne0,1$,

$$
\frac1{x(x-1)}=-\frac1x+\frac1{x-1},
$$

por lo que en $(-\infty,0)$, $(0,1)$ y $(1,\infty)$, por separado,

$$
\int\frac{dx}{x(x-1)}=\ln|x-1|-\ln|x|+C.
$$

No existe una constante de integración que, por arte de notación, obligue a enlazar primitivas a través de una singularidad.

## 7.8. Factores repetidos, cuadráticos y dominio original

La presencia de raíces repetidas o factores cuadráticos irreducibles exige más álgebra que el Teorema 7.3. En lugar de introducir sin prueba un teorema general de factorización y descomposición para todo polinomio real, estudiaremos identidades **comprobadas multiplicando denominadores**.

**Raíz repetida.** Para $x\notin\{0,1\}$,

$$
\frac1{x(x-1)^2}=\frac1x-\frac1{x-1}+\frac1{(x-1)^2}.
$$

La suma de las tres fracciones, al llevarla al denominador común, tiene numerador uno. Las primitivas respectivas son $\ln|x|$, $-\ln|x-1|$ y $-1/(x-1)$; así,

$$
\int\frac{dx}{x(x-1)^2}
=\ln|x|-\ln|x-1|-\frac1{x-1}+C.
$$

**Factor cuadrático sin raíces reales.** Para todo real, $(x+1)^2+1>0$ y

$$
\frac{2x+3}{x^2+2x+2}
=\frac{2x+2}{(x+1)^2+1}+\frac1{(x+1)^2+1}.
$$

La primera fracción es la derivada logarítmica del denominador; la segunda se integra con la derivada de $\arctan$. Por tanto,

$$
\int\frac{2x+3}{x^2+2x+2}\,dx
=\ln(x^2+2x+2)+\arctan(x+1)+C.
$$

**División antes de descomponer.** En el dominio $x\ne\pm1$,

$$
\frac{x^3+1}{x^2-1}=x+\frac{x+1}{(x-1)(x+1)}=x+\frac1{x-1}.
$$

Su primitiva en cada componente del **dominio original** es $x^2/2+\ln|x-1|+C$. Aunque la expresión simplificada tenga valor en $x=-1$, la función original no lo tiene allí. Esa exclusión debe conservarse al describir las primitivas.

**Proposición 7.3 (diferenciación como control; `EDC-C07-PRP-003`).** En un intervalo abierto $I$ sobre el que una identidad racional $R=S$ sea válida y una expresión candidata $G$ satisfaga $G'=S$, la misma $G$ es primitiva de $R$ sobre $I$.

**Demostración.** Para cada $x\in I$, las identidades evaluadas en $x$ dan $G'(x)=S(x)=R(x)$. La hipótesis sobre el intervalo evita singularidades. $\square$

Esta proposición aparentemente modesta fija una regla de auditoría: **una antiderivada se verifica derivándola sobre el dominio declarado**, no por semejanza superficial con una fórmula de tabla.

## 7.9. Un repertorio derivado, no memorizado

Las siguientes identidades se justifican aplicando el Teorema Fundamental a las derivadas ya probadas en C02; siempre se entienden en intervalos contenidos en el dominio real del integrando:

$$
\begin{aligned}
\int x^r\,dx&=\frac{x^{r+1}}{r+1}+C
&& (x>0,\ r\in\mathbb R\setminus\{-1\}),\\
\int \frac{dx}{x}&=\ln|x|+C&&(x\ne0),\\
\int e^{kx}\,dx&=\frac{e^{kx}}{k}+C&&(k\ne0),\\
\int\cos(kx)\,dx&=\frac{\sin(kx)}k+C&&(k\ne0),\\
\int\sin(kx)\,dx&=-\frac{\cos(kx)}k+C&&(k\ne0),\\
\int\frac{dx}{1+x^2}&=\arctan x+C,\\
\int\frac{dx}{\cos^2x}&=\tan x+C&&(\cos x\ne0).
\end{aligned}
$$

Para $k=0$, las exponenciales y trigonométricas se tratan como constantes; las fórmulas con $1/k$ **no** son aplicables. Para exponentes enteros no negativos, la regla de potencias vale también en $x\le0$ según C02, y se puede integrar sobre cualquier intervalo real. Para $r=-1$, la primitiva es logarítmica en cada semieje.

La identidad $\sin^2x=(1-\cos2x)/2$, que viene de trigonometría elemental, conduce a

$$
\int\sin^2x\,dx=\frac x2-\frac{\sin2x}{4}+C.
$$

Es esencial reconocer que una *tabla* sólo condensa pruebas disponibles: no reemplaza la verificación de dominio, regularidad o singularidades en la integral concreta.

## 7.10. Acumulaciones geométricas: área entre curvas

Supongamos que $f,g:[a,b]\to\mathbb R$ son continuas. Si $f(x)\ge g(x)$ para todo $x$, el área de la región vertical entre ambas gráficas está dada por la integral de la **altura no negativa** $f-g$:

$$
\boxed{A=\int_a^b [f(x)-g(x)]\,dx.}
$$

Esta interpretación de área se apoya en las aproximaciones rectangulares de C04 y en la definición integrable de C05. Si las gráficas se cruzan y ninguna queda arriba en todo el intervalo, el área total es

$$
A=\int_a^b|f(x)-g(x)|\,dx.
$$

La continuidad hace que el integrando sea Riemann-integrable, pero **para calcular** la expresión habitualmente conviene localizar los cruces y separar los intervalos. No se puede sustituir el área entre curvas por el valor absoluto de la integral orientada en general.

**Ejemplo.** En $[0,2]$, $2x\ge x^2$ y

$$
A=\int_0^2(2x-x^2)\,dx
=\left[x^2-\frac{x^3}{3}\right]_0^2=\frac43.
$$

La fórmula de área no requiere que ambas funciones sean no negativas por separado; sólo exige comparar sus alturas. La geometría del arco parabólico de C04 puede utilizarse como comprobación independiente del valor.

**Proposición 7.4 (cota geométrica del área; `EDC-C07-PRP-004`).** Si $f,g$ son continuas sobre $[a,b]$ y $|f(x)-g(x)|\le M$ allí, entonces

$$
0\le\int_a^b|f-g|\,dx\le M(b-a).
$$

**Demostración.** La continuidad de $|f-g|$ asegura integrabilidad, y el orden de C05 aplicado a $0\le|f-g|\le M$ da la desigualdad. $\square$

## 7.11. Acumulaciones físicas: trabajo y balance

Si una fuerza escalar $F(x)$ actúa a lo largo de una trayectoria unidimensional cuyo desplazamiento se modela por la coordenada $x$, el trabajo orientado en el modelo se escribe

$$
W=\int_a^b F(x)\,dx.
$$

La hipótesis de que la fuerza depende sólo de la posición y es continua en el trayecto asegura existencia de la integral propia. Si $F(x)$ se mide en newtons y $x$ en metros, el trabajo se mide en newton-metros, es decir, joules. **El signo** distingue trabajo que favorece u obstaculiza el desplazamiento según la orientación elegida.

**Ejemplo: resorte lineal.** Para una fuerza aplicada $F(x)=kx$ al extender un resorte desde su posición de equilibrio hasta una elongación $L\ge0$, donde $k>0$ tiene unidades $\mathrm{N}/\mathrm m$,

$$
W=\int_0^L kx\,dx=\frac12kL^2.
$$

La fuerza de restitución del propio resorte tiene signo opuesto, $-kx$, y por tanto su trabajo orientado en el mismo desplazamiento es $-kL^2/2$. Las dos respuestas son coherentes: describen **fuerzas distintas**.

**Balance de tasa.** Si una magnitud $Q(t)$ satisface $Q'=r(t)$ en un intervalo temporal y $r$ es continua, entonces

$$
Q(t_1)-Q(t_0)=\int_{t_0}^{t_1}r(t)\,dt.
$$

Esto no es una nueva ley física: es el Teorema Fundamental aplicado a la relación diferencial postulada por el modelo. El cálculo no determina por sí solo qué tasa describe correctamente un fenómeno; ésa es una hipótesis empírica que debe contrastarse por separado.

## 7.12. Estrategia, límites e historia de un oficio matemático

En el cálculo elemental es tentador interpretar $\int f$ como un problema de reconocimiento visual: «si veo un polinomio, pruebo potencia; si veo un producto, pruebo partes». Pero la elección racional se hace **después** de verificar integrabilidad, dominio y orientación. Se empieza por simplificar álgebra o trigonometría, comprobar si la función es una composición con su derivada, y sólo entonces escoger un método que reduzca de verdad el problema. En integrales definidas hay que transformar los extremos y respetar el signo de la derivada del cambio de variable; en funciones racionales hay que examinar polos, factores repetidos y posibles agujeros del dominio original.

El límite conceptual es tan importante como el método. Toda función continua sobre un intervalo compacto tiene una integral de Riemann y, por C06, una primitiva obtenida como función de acumulación. Sin embargo, **no hemos demostrado que cada primitiva pueda expresarse mediante un número finito de potencias, logaritmos, exponenciales, funciones trigonométricas y operaciones algebraicas**. La función

$$
H(x)=\int_0^xe^{-t^2}\,dt
$$

está perfectamente definida para todo $x$, es derivable y satisface $H'=e^{-x^2}$. No necesitamos decidir aquí qué expresiones elementales existen o no para $H$: el Teorema Fundamental ya asegura lo que importa para su existencia y variación. Tampoco introducimos integrales impropias, integrales múltiples, teoría de medida o técnicas avanzadas de fracciones racionales con raíces complejas.

Históricamente, las cuadraturas, sumaciones y reglas operatorias no surgieron todas con las mismas definiciones actuales. Los problemas geométricos antiguos y las transformaciones de los siglos XVII–XIX dieron lugar a familias de procedimientos que hoy pueden unificarse mediante producto, cadena y Teorema Fundamental. La notación de Leibniz conserva esa genealogía, pero el símbolo $du$ no sustituye la prueba analítica que hemos realizado. La [documentación histórica](capitulo-07-notas.md) distingue las síntesis efectivamente consultadas de las fuentes primarias y libros sólo localizados, sin atribuir a Newton o Leibniz enunciados modernos de Riemann–Darboux.

### Mapa de dependencias y alcance

- **C00–C01:** límites, continuidad, intervalos, derivadas puntuales y dominios de funciones.
- **C02:** producto, cadena, derivación de logaritmos, exponenciales, potencias y trigonometría; división algebraica básica de polinomios.
- **C03:** teorema del valor medio y unicidad de primitivas salvo constante.
- **C04–C05:** sumas geométricas, definición independiente de integral, linealidad, orden, aditividad, integral orientada e integrabilidad de funciones continuas.
- **C06:** Teorema Fundamental en sus dos partes, primitivas, y justificación de acumulaciones con extremos variables.
- **Aportaciones de C07:** `EDC-C07-THM-001--003`, `PRP-001--004`, `COR-001--003`, dos definiciones y procedimientos justificados de sustitución, partes y fracciones racionales en casos controlados.
- **No utilizado:** series generales de C08, Taylor de C09, teoría de EDO de C10, Lebesgue, integrales impropias o cambio de variables multivariado.

### Trabajo del lector

Los [ejercicios de C07](capitulo-07-ejercicios.md) incluyen diagnóstico de hipótesis, cálculo mediante distintos métodos, pruebas de las reglas, aplicaciones y un desafío de síntesis. Sus [soluciones](capitulo-07-soluciones.md) se entregan separadas de la exposición; cada resolución especifica el intervalo real y la técnica empleada. El marco histórico y los niveles efectivos de consulta están en [notas de fuentes](capitulo-07-notas.md).
