---
title: Capítulo 7. Integrar como método
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
source-id: EDC-C07
source-sha256: c06e3900d3c664ad80382e9538ebc43985874499786556080e4e3e3e1d44ea50
content-id: MA-BCH-0338
content-type: book-chapter
related:
  - MA-BOK-0015
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-07.html) · [Ejercicios](capitulo-07-ejercicios.html) · [Soluciones](capitulo-07-soluciones.html)

[← Capítulo 6](capitulo-06.html) · [Capítulo 8 →](capitulo-08.html)

> **Pregunta generadora.** Conocemos la definición rigurosa de integral y sabemos calcularla mediante primitivas. ¿Cómo reconocer una primitiva cuando el integrando es una composición, un producto o una función racional que no aparece en una tabla elemental?

El Teorema Fundamental nos permite calcular una integral si encontramos una función cuya derivada sea el integrando. Para algunas expresiones basta reconocer una potencia o una exponencial, pero una composición o un producto puede ocultar la derivada que buscamos. La diferencia se aprecia en $e^{x^2}$: derivarla da $2xe^{x^2}$ de inmediato, mientras que buscar una primitiva de $e^{x^2}$ nos deja ante otro problema. El factor $2x$ convierte una de esas expresiones en una derivada reconocible.

Las reglas de derivación ofrecen varias maneras de buscar. La cadena explica qué factor debe acompañar a una composición; el producto permite intercambiar la derivación de dos factores, a veces simplificando uno de ellos. Para las funciones racionales, el trabajo comienza antes, en el álgebra: descomponer un cociente puede revelar términos cuyas primitivas ya conocemos. Estudiaremos cómo se justifican estos procedimientos y qué dificultades resuelve cada uno, manteniendo los intervalos y extremos de la integral que queremos calcular.

## 7.1. De una integral existente a una estrategia de cálculo

Consideremos

$$
I=\int_0^1 2x\,e^{x^2}\,dx.
$$

Por C02, la derivada de $x\mapsto e^{x^2}$ es $2xe^{x^2}$. Por C05 el integrando es continuo, luego integrable; por C06,

$$
I=[e^{x^2}]_0^1=e-1.
$$

El factor $2x$ permite reconocer la cadena: es la derivada de $x^2$, el argumento de la exponencial. Si cambiásemos esa expresión interior, cambiaría también el factor necesario para recuperar la derivada compuesta. Una técnica de integración útil tendrá que conservar esa relación, además de identificar la función que aparece por fuera.

**Definición 7.1 (`EDC-C07-DEF-001`; primitiva sobre un intervalo).** Si $I\subseteq\mathbb R$ es un intervalo abierto y $f:I\to\mathbb R$, una primitiva de $f$ sobre $I$ es una función derivable $F:I\to\mathbb R$ tal que $F'=f$ en todos los puntos de $I$. Denotamos informalmente la familia de primitivas por

$$
\int f(x)\,dx=F(x)+C,\qquad C\in\mathbb R,
$$

cuando se sabe que $F$ existe. Esta notación **no define una segunda integral**: resume la afirmación sobre una familia de funciones cuya diferencia es constante, demostrada en C06 por el valor medio. En cada componente separada del dominio, la constante puede elegirse independientemente.

La familia de primitivas describe funciones, mientras una integral definida tiene un valor y unos extremos. Antes de usar una primitiva para evaluarla comprobamos que el integrando esté definido y sea integrable en todo el tramo. Esa comprobación puede decidir el problema antes de cualquier cálculo: $1/x$ tiene primitivas en cada semieje, pero ninguna de ellas convierte una expresión que atraviesa cero en una integral propia de C05.

## 7.2. El teorema de sustitución: deshacer la regla de la cadena

**Teorema 7.1 (sustitución orientada; `EDC-C07-THM-001`).** Sean $J\subseteq\mathbb R$ un intervalo abierto, $f:J\to\mathbb R$ continua, y $\phi:[\alpha,\beta]\to J$ una función continuamente derivable, con $\alpha<\beta$. Entonces

$$
\boxed{\int_\alpha^\beta f(\phi(t))\phi'(t)\,dt
=\int_{\phi(\alpha)}^{\phi(\beta)}f(u)\,du.}
$$

La función $\phi$ **no tiene que ser inyectiva ni monótona**. Los extremos de la derecha pueden coincidir o estar en orden inverso. En la izquierda y en la derecha las integrales existen en sentido propio.

**Demostración.** Buscamos una primitiva de $f$ que podamos componer con $\phi$. Elegimos $u_0\in J$ y definimos $F(u)=\int_{u_0}^{u}f(s)\,ds$ para todo $u\in J$. Como $J$ es un intervalo, contiene el segmento entre $u_0$ y $u$; ese segmento es compacto y $f$ es continua en él, así que la integral orientada existe.

Para derivar $F$ en un punto de $J$, podemos rodear ese punto por un intervalo cerrado contenido en $J$. La aditividad expresa allí $F$ como una constante más una acumulación local, y la primera parte del Teorema Fundamental (`EDC-C06-THM-002`) da $F'=f$. Por tanto tenemos la primitiva sobre todo $J$, incluso si no conocemos una fórmula para ella.

La regla de la cadena (`EDC-C02-THM-002`) proporciona

$$
(F\circ\phi)'(t)=f(\phi(t))\phi'(t),\qquad \alpha<t<\beta.
$$

El recorrido de $\phi$ es compacto y permanece en $J$. El integrando izquierdo es continuo en $[\alpha,\beta]$, porque lo son $f\circ\phi$ y la prolongación de $\phi'$. La composición $F\circ\phi$ es continua hasta los extremos y es una primitiva de ese integrando en el interior. La segunda parte del Teorema Fundamental (`EDC-C06-THM-005`) permite evaluar:

$$
\int_\alpha^\beta f(\phi(t))\phi'(t)\,dt
=F(\phi(\beta))-F(\phi(\alpha))
=\int_{\phi(\alpha)}^{\phi(\beta)}f(u)\,du.
$$

La última igualdad usa aditividad orientada de C05, que cubre también extremos invertidos o coincidentes. La prueba sólo necesitó componer y derivar $F$; no buscó una inversa de $\phi$. Por eso el resultado conserva su validez si el cambio retrocede o recorre varias veces un mismo valor. $\square$

**Corolario 7.1 (sustitución en una primitiva; `EDC-C07-COR-001`).** Bajo las hipótesis locales de la regla de la cadena, si $F'=f$ en un intervalo que contiene $\phi(I)$, entonces

$$
\int f(\phi(x))\phi'(x)\,dx=F(\phi(x))+C
$$

sobre cada intervalo abierto $I$ donde la expresión esté definida. **Demostración.** Derivamos $F\circ\phi$ mediante la cadena; la descripción de todas las primitivas sigue del valor medio de C03. $\square$

Si $\phi(t)=1-t$ en $[0,1]$, el nuevo extremo pasa de uno a cero mientras el antiguo pasa de cero a uno. La derivada $\phi'=-1$ registra esa inversión:

$$
\int_0^1 -f(1-t)\,dt=\int_1^0 f(u)\,du
=-\int_0^1 f(u)\,du.
$$

El signo de la derivada y el orden de los extremos pertenecen a una misma fórmula. Reemplazar la derivada por su módulo quitaría la orientación de las contribuciones y cambiaría la integral.

## 7.3. Transformar correctamente los extremos

En una integral definida, el cambio $u=\phi(x)$ convierte cada extremo en su imagen. Podemos verlo con $u=1+x^2$: para $x\in[0,1]$ los valores de $u$ están entre uno y dos, y la derivada $2x$ permite escribir $x\sqrt{1+x^2}$ como la mitad de la composición acompañada por el factor de la cadena. Así,

$$
\begin{aligned}
\int_0^1 x\sqrt{1+x^2}\,dx
&=\frac12\int_1^2\sqrt{u}\,du\\
&=\frac12\left[\frac23u^{3/2}\right]_1^2
=\frac{2\sqrt2-1}{3}.
\end{aligned}
$$

Los extremos uno y dos corresponden a $u(0)$ y $u(1)$. La función $u^{1/2}$ es continua en un intervalo abierto positivo que contiene todo el recorrido, por lo que el Teorema 7.1 justifica la transformación. La evaluación final usa una primitiva de esa potencia.

Para $\phi(t)=t^2$ en $[-1,1]$, el nuevo argumento comienza en uno, baja hasta cero y vuelve a uno. Su derivada es negativa en la primera mitad y positiva en la segunda. El teorema da

$$
\int_{-1}^1 2t\,e^{t^2}\,dt=\int_1^1e^u\,du=0.
$$

Las contribuciones de los dos recorridos se cancelan. Si quisiéramos sumar sus magnitudes, tendríamos que integrar otro integrando, con $|2t|$ en lugar de $2t$. El teorema orientado permite retrocesos precisamente porque conserva sus signos.

**Proposición 7.1 (invariancia por traslación y escala afín; `EDC-C07-PRP-001`).** Sean $f$ continua en un intervalo abierto $J$ y $\phi(t)=ct+d$ con $c\ne0$. Para $\alpha<\beta$ tales que $\phi([\alpha,\beta])\subset J$,

$$
\int_\alpha^\beta f(ct+d)\,dt
=\frac1c\int_{c\alpha+d}^{c\beta+d}f(u)\,du.
$$

**Demostración.** La función afín es continuamente derivable y tiene derivada constante $c$. El Teorema 7.1 identifica la integral de $c f(ct+d)$ con la integral de $f$ entre las imágenes de los extremos. La linealidad permite sacar $c$ como factor y, puesto que no es cero, dividir ambos lados por él. Si $c<0$, las imágenes quedan en orden inverso y la orientación conserva la igualdad. $\square$

La escritura $du=\phi'(x)\,dx$ sirve para recordar el factor de la cadena. Al usarla en una integral definida anotamos también de dónde viene y a dónde va $u$: mantener los extremos antiguos después de transformar el integrando conduciría a evaluar otra integral.

## 7.4. La regla del producto conduce a integración por partes

**Teorema 7.2 (integración por partes; `EDC-C07-THM-002`).** Sean $u,v:[a,b]\to\mathbb R$ funciones de clase $C^1$, con $a<b$; esto significa continuas en $[a,b]$, derivables en $(a,b)$ y con derivadas interiores que se prolongan continuamente a $[a,b]$. Entonces

$$
\boxed{\int_a^b u(x)v'(x)\,dx
=\bigl[u(x)v(x)\bigr]_a^b-\int_a^b u'(x)v(x)\,dx.}
$$

**Demostración.** La regla del producto de C02 da $(uv)'=u'v+uv'$ en el interior. Las prolongaciones continuas de $u'$ y $v'$, junto con la continuidad de $u$ y $v$, hacen continuos ambos productos y su suma en $[a,b]$. Sus integrales existen por C05.

La función $uv$ es continua hasta los extremos y su derivada interior coincide con la suma indicada. La segunda parte del Teorema Fundamental de C06 y la linealidad de la integral dan

$$
[uv]_a^b=\int_a^b(u'v+uv')\,dx
=\int_a^b u'v\,dx+\int_a^b uv'\,dx.
$$

Restamos la integral de $u'v$ y queda la fórmula. Los valores terminales del producto conservan la parte que se separa al intercambiar la derivación entre los factores. $\square$

**Corolario 7.2 (forma indefinida; `EDC-C07-COR-002`).** En un intervalo abierto en el que $u,v$ sean derivables y los productos estén definidos, $uv$ es una primitiva de $u'v+uv'$. Siempre que alguno de los sumandos tenga primitiva, se puede escribir

$$
\int uv'\,dx=uv-\int u'v\,dx+C.
$$

**Demostración.** La regla del producto da $(uv)'=u'v+uv'$. Si $A$ es una primitiva de $u'v$, entonces $(uv-A)'=uv'$. Si comenzamos con una primitiva $B$ de $uv'$, la diferencia $uv-B$ es a su vez una primitiva de $u'v$. En cualquiera de los casos la fórmula describe las primitivas, y el valor medio asegura que todas difieren en una constante sobre el intervalo. $\square$

La elección de factores decide si el intercambio ayuda. Derivar un polinomio disminuye su grado, mientras que integrar una exponencial conserva una forma sencilla. Otras veces el intercambio trae de vuelta la integral inicial y permite resolver una igualdad algebraica. Conviene examinar la integral que aparecerá antes de escoger $u$ y $v'$.

::: {.callout-note appearance="simple" icon="false" collapse="false" title="Historia — Leibniz: una notación que acompaña al cambio"}
*Lectura opcional.*

Al final de su artículo de 1686, Leibniz advierte que retirar demasiado pronto una cantidad diferencial puede quitar generalidad al cálculo. Le interesa conservar la posibilidad de que la variable avance de distintas maneras. Unas páginas antes explica también su preferencia por una escritura como $dx$, vinculada a la propia letra $x$, y presenta diferencias y sumaciones como operaciones recíprocas.

Esa atención a la escritura ayuda a entender por qué un cambio de variable debe registrar algo más que el nombre nuevo del argumento. Si $u=3x+1$, una variación de $x$ produce una variación triple de $u$. La integral de $e^{3x+1}$ se convierte en la de $e^u$ con un factor $1/3$; olvidar ese factor cambiaría el valor. Cuando el cambio retrocede, su derivada conserva además el signo que vimos en la sustitución orientada.

La fórmula de nuestro teorema justifica estos cambios mediante la cadena y una primitiva. La escritura diferencial permite recordar qué expresión cambia y cómo cambia, una ayuda especialmente valiosa cuando el cálculo reúne varias composiciones. Conservar esa información fue parte del interés de Leibniz por una notación que pudiera acompañar el razonamiento.

**Para seguir leyendo:** [Leibniz, *De geometria recondita* (1686), traducción de Thiago Dourado, pp. 6–7 y 9 (2022)](https://www.rbhm.org.br/index.php/RBHM/article/view/379).
:::

## 7.5. Dos integraciones por partes reveladoras

**Primera: un polinomio por una exponencial.** En $xe^x$ elegimos derivar $x$, que se convierte en uno, e integrar $e^x$, que permanece igual. Con $u=x$, $v'=e^x$ y $v=e^x$ en $[0,1]$,

$$
\int_0^1 xe^x\,dx=[xe^x]_0^1-\int_0^1e^x\,dx=e-(e-1)=1.
$$

La integral restante se evalúa directamente. La forma indefinida es $(x-1)e^x+C$, cuya derivada recupera $xe^x$. Si comenzamos con $x^2e^x$, el mismo intercambio deja una integral con $2xe^x$; repetirlo elimina finalmente el factor polinómico. Obtenemos

$$
\int x^2e^x\,dx=e^x(x^2-2x+2)+C.
$$

**Segunda: un logaritmo que no presenta producto.** Podemos escribir $\ln x=(\ln x)\cdot1$. Elegimos $u=\ln x$ y $v'=1$ porque $u'=1/x$ se simplifica al multiplicarse por $v=x$. En el intervalo positivo $[1,e]$,

$$
\int_1^e\ln x\,dx=[x\ln x]_1^e-\int_1^e1\,dx=e-(e-1)=1.
$$

La elección convierte la integral restante en la de una constante. La misma cuenta proporciona $x\ln x-x$ como primitiva sobre $(0,\infty)$; el intervalo conserva el dominio del logaritmo real definido en C02.

**Proposición 7.2 (reducción polinomio–exponencial; `EDC-C07-PRP-002`).** Si $p$ es un polinomio de grado $n\ge0$, la función $p(x)e^x$ tiene sobre $\mathbb R$ una primitiva de la forma $e^x q(x)$ con $q$ polinomio de grado a lo sumo $n$. En particular se obtiene mediante un número finito de integraciones por partes.

**Demostración.** Una candidata $e^xq(x)$ tiene derivada $e^x(q+q')$. Para obtener $e^xp$ necesitamos por tanto un polinomio $q$ que satisfaga $q+q'=p$. Comenzar con $q=p$ deja el término adicional $p'$; restarlo de $q$ lo cancela, pero aparece entonces $-p''$. La alternancia continúa hasta que las derivadas se anulan.

Esto lleva a elegir $q=p-p'+p''-\cdots+(-1)^np^{(n)}$. Cada término tiene grado a lo sumo $n$ y la suma termina porque $p^{(n+1)}=0$. Al sumar $q'$ a $q$, cada derivada de orden positivo aparece con signos opuestos y sólo queda $p$. Por la regla del producto,

$$
\frac{d}{dx}(e^xq)=e^x(q+q')=e^xp,
$$

que demuestra que es una primitiva sobre toda la recta. Integrar por partes primero $p e^x$, después $p'e^x$ y así sucesivamente produce la misma suma alternada, con un número finito de pasos. Para un polinomio constante, la elección se reduce a $q=p$. $\square$

## 7.6. Cuando la integral reaparece: el método cíclico

En $e^x\cos x$, derivar el coseno lo convierte en un seno; repetir el proceso devuelve el coseno con otro signo. Las integraciones por partes pueden aprovechar ese ciclo. Si escribimos $I=\int e^x\cos x\,dx$, la primera aplicación con $u=\cos x$ y $v'=e^x$ da

$$
I=e^x\cos x+\int e^x\sin x\,dx.
$$

La integral nueva $J=\int e^x\sin x\,dx$, con $u=\sin x$ y $v'=e^x$, satisface

$$
J=e^x\sin x-\int e^x\cos x\,dx.
$$

Estas escrituras de primitivas incluyen elecciones de constantes. Para efectuar el despeje sin ambigüedad, tomemos $I(x)=\int_0^xe^t\cos t\,dt$ y $J(x)=\int_0^xe^t\sin t\,dt$. La primera igualdad se vuelve $I(x)=e^x\cos x-1+J(x)$; la segunda, $J(x)=e^x\sin x-I(x)$. Los términos en cero son respectivamente uno y cero. Sustituimos la segunda relación en la primera y reunimos las dos apariciones de $I(x)$: $2I(x)=e^x(\sin x+\cos x)-1$.

La acumulación difiere en una constante de la función que aparece a continuación, por lo que la familia de primitivas es

$$
\boxed{\int e^x\cos x\,dx=\frac{e^x}{2}(\sin x+\cos x)+C.}
$$

Al derivar, los términos con seno se cancelan y los dos términos con coseno compensan el factor $1/2$. El procedimiento cerró un sistema de dos integrales. En el caso polinómico reducía un grado; aquí aprovechó que la repetición regresaba al punto inicial con un coeficiente que permitía despejar.

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

**Demostración.** Multiplicar una descomposición por $Q$ convierte el problema racional en una identidad de polinomios. Al evaluar esa identidad en una raíz $r_i$, todos los factores que aún contienen $x-r_i$ desaparecen. Sólo sobrevive el sumando cuyo denominador era $x-r_i$, lo que permite determinar su coeficiente por separado.

Como las raíces son distintas, $Q'(r_j)=c\prod_{k\ne j}(r_j-r_k)\ne0$. Con los coeficientes del enunciado, definimos

$$
H(x)=P(x)-\sum_{j=1}^m A_j\frac{Q(x)}{x-r_j}.
$$

Aquí $Q(x)/(x-r_j)$ designa el polinomio obtenido al retirar ese factor, de grado $m-1$; podemos evaluarlo incluso en $r_j$. Su valor allí es $Q'(r_j)$. Así $H$ es un polinomio de grado menor que $m$, y al evaluar en $r_i$ los términos con $j\ne i$ son cero, mientras el restante vale $A_iQ'(r_i)=P(r_i)$. Tenemos $H(r_i)=0$ para todas las raíces.

Queda comprobar que esas evaluaciones determinan la identidad entera. Si un polinomio se anula en $r_1$, es divisible por $x-r_1$. Al evaluar el cociente en otra raíz distinta, el factor retirado no es cero, por lo que también ese cociente se anula allí. Repetimos para las $m$ raíces: un polinomio no nulo con esas raíces tendría grado al menos $m$, pero $H$ tiene grado menor. Debe ser el polinomio cero.

La identidad polinómica queda probada. Dividimos por $Q(x)$ sólo donde no se anula y obtenemos la descomposición racional en el dominio declarado. $\square$

**Corolario 7.3 (primitiva racional en raíces simples; `EDC-C07-COR-003`).** Bajo las hipótesis del Teorema 7.3, en **cada intervalo abierto** que no contenga raíces de $Q$,

$$
\int\frac{P(x)}{Q(x)}\,dx
=\sum_{j=1}^m A_j\ln|x-r_j|+C.
$$

**Demostración.** En un intervalo que no contiene $r_j$, la diferencia $x-r_j$ mantiene su signo. Si es positiva, la cadena da la derivada de $\ln(x-r_j)$; si es negativa, derivamos $\ln(r_j-x)$. En ambos casos $\frac{d}{dx}\ln|x-r_j|=1/(x-r_j)$, según C02. Derivamos la suma finita del enunciado y la identidad del Teorema 7.3 recupera $P/Q$. El valor medio describe todas las demás primitivas mediante una constante en ese intervalo. $\square$

**Ejemplo.** Para $x\ne0,1$,

$$
\frac1{x(x-1)}=-\frac1x+\frac1{x-1},
$$

por lo que en $(-\infty,0)$, $(0,1)$ y $(1,\infty)$, por separado,

$$
\int\frac{dx}{x(x-1)}=\ln|x-1|-\ln|x|+C.
$$

Cada uno de esos intervalos es un componente del dominio. Dentro de él, el valor medio obliga a que dos primitivas difieran en una constante; entre componentes separados por los polos, las constantes pueden elegirse independientemente.

## 7.8. Factores repetidos, cuadráticos y dominio original

En el Teorema 7.3 fue esencial que $Q'(r_j)$ no se anulara. Una raíz repetida hace cero esa derivada y requiere otros términos en la descomposición. Un factor cuadrático sin raíces reales tampoco proporciona puntos reales donde aislar coeficientes de la misma manera. Estudiaremos ambos casos mediante identidades que pueden comprobarse por denominador común, sin necesitar un teorema general de descomposición.

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

**Demostración.** Fijamos $x\in I$. La identidad racional es válida allí y la candidata tiene la derivada indicada, de modo que $G'(x)=S(x)=R(x)$. Como el argumento vale en todos los puntos del intervalo, $G$ satisface la definición de primitiva de $R$ sobre él. $\square$

El control final conserva el dominio donde se efectuó el cálculo. Una simplificación puede dejar una expresión que admita valores en puntos antes excluidos; derivarla allí no convierte esos puntos en parte del dominio de la función original.

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

El repertorio ayuda a reconocer una derivada, pero cada uso conserva sus condiciones. El denominador de una fórmula, el argumento de un logaritmo y el intervalo elegido pueden decidir si la candidata es una primitiva válida para la integral concreta.

## 7.10. Acumulaciones geométricas: área entre curvas

Supongamos que $f,g:[a,b]\to\mathbb R$ son continuas. Si $f(x)\ge g(x)$ para todo $x$, el área de la región vertical entre ambas gráficas está dada por la integral de la **altura no negativa** $f-g$:

$$
\boxed{A=\int_a^b [f(x)-g(x)]\,dx.}
$$

Esta interpretación de área se apoya en las aproximaciones rectangulares de C04 y en la definición integrable de C05. Si las gráficas se cruzan y ninguna queda arriba en todo el intervalo, el área total es

$$
A=\int_a^b|f(x)-g(x)|\,dx.
$$

La continuidad de $|f-g|$ garantiza integrabilidad incluso si hay cruces. Para calcular el módulo podemos localizar los puntos donde cambia el orden de las gráficas y usar en cada tramo la diferencia entre la superior y la inferior. Integrar primero $f-g$ y tomar después el módulo del resultado permitiría cancelaciones entre tramos; el área total suma sus alturas no negativas.

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

**Demostración.** La diferencia de dos funciones continuas y su módulo son continuos, luego integrables en $[a,b]$. El orden de C05 aplicado a $0\le|f-g|\le M$ compara su integral con las de las constantes cero y $M$. Éstas valen cero y $M(b-a)$, respectivamente, y dan la cota. $\square$

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

La relación $Q'=r$ procede del modelo: expresa qué tasa representa el cambio de la magnitud. Bajo las condiciones del Teorema Fundamental, integrar esa tasa recupera la diferencia entre los valores terminales. Para determinar además el valor final de $Q$, necesitamos conocer su valor inicial; la integral aporta el cambio ocurrido durante el intervalo.

## 7.12. Estrategia, límites e historia de un oficio matemático

Una elección de método responde a la estructura del integrando. En una composición buscamos el factor de la cadena; en un producto examinamos qué factor se simplifica al derivarlo y qué primitiva podemos hallar para el otro. El ciclo exponencial–trigonométrico mostró que también puede ayudar una integral que reaparece. En un cociente racional, la división y la factorización preparan el trabajo analítico, siempre conservando los puntos excluidos del dominio.

Estos procedimientos permiten calcular muchas acumulaciones, pero no determinan por sí solos una expresión elemental para cualquier primitiva. La primera parte del Teorema Fundamental ya nos da, para el integrando continuo $e^{-t^2}$, la función

$$
H(x)=\int_0^xe^{-t^2}\,dt
$$

definida para cada $x$ mediante una integral sobre un segmento finito, con $H'(x)=e^{-x^2}$. La pregunta por una expresión finita en términos de un repertorio previo de funciones queda abierta aquí. La existencia y la variación de $H$ están determinadas aunque nuestros métodos no hayan producido esa expresión.

En el capítulo, el Teorema Fundamental permite reunir esos procedimientos mediante identidades de derivación y de polinomios. Para estudiar después aproximaciones dadas por sumas con un número creciente de términos, necesitaremos averiguar qué condiciones permiten pasar de esas sumas a un límite; ésa será la nueva dificultad de C08.

### Mapa de dependencias y alcance

- **C00–C01:** límites, continuidad, intervalos, derivadas puntuales y dominios de funciones.
- **C02:** producto, cadena, derivación de logaritmos, exponenciales, potencias y trigonometría; división algebraica básica de polinomios.
- **C03:** teorema del valor medio y unicidad de primitivas salvo constante.
- **C04–C05:** sumas geométricas, definición independiente de integral, linealidad, orden, aditividad, integral orientada e integrabilidad de funciones continuas.
- **C06:** Teorema Fundamental en sus dos partes, primitivas, y justificación de acumulaciones con extremos variables.
- **Aportaciones de C07:** `EDC-C07-THM-001--003`, `PRP-001--004`, `COR-001--003`, dos definiciones y procedimientos justificados de sustitución, partes y fracciones racionales en casos controlados.
- **No utilizado:** series generales de C08, Taylor de C09, teoría de EDO de C10, Lebesgue, integrales impropias o cambio de variables multivariado.

### Trabajo del lector

Los [ejercicios de C07](capitulo-07-ejercicios.html) incluyen diagnóstico de hipótesis, cálculo mediante distintos métodos, pruebas de las reglas, aplicaciones y un desafío de síntesis. Sus [soluciones](capitulo-07-soluciones.html) se entregan separadas de la exposición; cada resolución especifica el intervalo real y la técnica empleada.
