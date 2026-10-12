---
title: 'Capítulo 11. El cálculo como teoría: alcance, historia y fundamentos'
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
source-id: EDC-C11
source-sha256: ed2ec4affb20cc8be2893a12550e75b4c134146d11756e4ff1dc683817f4c78d
content-id: MA-BCH-0237
content-type: book-chapter
related:
- MA-BOK-0015
---

[Índice del libro](index.qmd) · [Prefacio](prefacio.md) · [Itinerarios](itinerarios.md)

[Exposición](capitulo-11.md) · [Ejercicios](capitulo-11-ejercicios.md) · [Soluciones](capitulo-11-soluciones.md) · [Notas históricas](capitulo-11-notas.md)

[← Capítulo 10](capitulo-10.md)

> **Pregunta generadora.** ¿Qué hemos demostrado efectivamente al transformar problemas de tangentes, velocidades, cuadraturas, series y trayectorias en una teoría del cálculo? ¿De qué supuestos depende esa unidad y qué dificultades anuncian el análisis real?

Los capítulos anteriores no son una colección de métodos independientes. Están enlazados por una pregunta matemática recurrente: **¿cuándo está permitido reconstruir un objeto a partir de aproximaciones?** Una secante aproxima una tangente; una suma finita, un área; un polinomio, una función; un paso de un algoritmo, una trayectoria. Lo decisivo no es sólo la aproximación, sino la demostración de que su error puede hacerse pequeño en el sentido y bajo las hipótesis indicadas.

La historia del cálculo no ofrece una sola ruta lineal hacia la notación actual. Existieron tratamientos geométricos antiguos de áreas y volúmenes, procedimientos asiáticos de aproximación y series, investigaciones modernas sobre movimiento y tangentes y sucesivas reformulaciones de los fundamentos. En estas páginas distinguiremos **hecho histórico documentado**, **reconstrucción moderna** y **teorema probado en este libro**. No convertiremos la prehistoria del cálculo en una enumeración de autores que «ya conocían» nuestro lenguaje.

Este capítulo es una **síntesis demostrativa**: formula consecuencias que se prueban usando únicamente C00–C10, confronta afirmaciones falsas mediante contraejemplos y expone los límites del corpus. No añade una teoría abstracta de espacios métricos, medida ni ecuaciones diferenciales generales.

## 11.1. El método del cálculo: una cadena de aproximaciones justificadas

**Definición 11.1 (certificado elemental de aproximación; `EDC-C11-DEF-001`).** Diremos que una familia de aproximantes reales $A_n$ **certifica** el valor $A$ si, además de una regla explícita de construcción de cada $A_n$, se ha demostrado una cota $|A_n-A|\le\varepsilon_n$ donde $\varepsilon_n\to0$. Cuando $A$ aún no se conoce, podrá demostrarse primero que $(A_n)$ es de Cauchy y emplearse la completitud de $\mathbb R$ (C00), identificando después su límite. Ésta es una convención didáctica, no una definición general de convergencia numérica nueva.

El cociente incremental $[f(a+h)-f(a)]/h$ (C01), las sumas de Darboux (C05), las sumas parciales de una serie (C08), los polinomios de Taylor (C09) y las aproximaciones de Euler (C10) no comparten el mismo tipo de error. Unas requieren hacer $h\to0$; otras, refinar una partición; otras, aumentar el orden $n$. No intercambiaremos esos límites sin demostrarlo.

**Proposición 11.1 (de la cota al límite; `EDC-C11-PRP-001`).** Si $A_n,A\in\mathbb R$, $\varepsilon_n\ge0$, $\varepsilon_n\to0$ y $|A_n-A|\le\varepsilon_n$ para todo $n$, entonces $A_n\to A$.

**Demostración.** Dado $\varepsilon>0$, el límite $\varepsilon_n\to0$ proporciona $N$ tal que $n\ge N$ implica $\varepsilon_n<\varepsilon$. Por la desigualdad anunciada, $|A_n-A|<\varepsilon$ para tales $n$. Ésta es exactamente la definición secuencial de límite de C00. $\square$

La proposición parece modesta, pero determina el alcance de muchas afirmaciones del libro: una cota de **error local para un paso** no certifica automáticamente una trayectoria entera; una cota de Taylor para un **orden fijo** no certifica una serie infinita.

## 11.2. Variación: de una secante al comportamiento de una función

La derivada fue definida en C01 como un límite bilateral de tasas medias en un punto interior; C02 justificó sus reglas; C03 convirtió esas reglas en información sobre intervalos. Aquí condensamos una consecuencia característica.

**Teorema 11.1 (identidad de derivada e identidad de cambios; `EDC-C11-THM-001`).** Sean $f,g$ continuas en $[a,b]$ y derivables en $(a,b)$, con $a<b$. Entonces

$$
f'(x)=g'(x)\ \text{para todo }x\in(a,b)
\quad\Longleftrightarrow\quad
f(x)-g(x)=C\ \text{para todo }x\in[a,b],
$$

donde $C\in\mathbb R$ es una constante. En particular, una función con derivada nula en el interior de un intervalo es constante en todo el intervalo.

**Demostración.** Si $f'=g'$, la diferencia $h=f-g$ es continua en $[a,b]$, derivable en $(a,b)$ y $h'=0$. Para cualesquiera $u<v$ en $[a,b]$, el teorema del valor medio de C03 proporciona $\xi\in(u,v)$ tal que $h(v)-h(u)=h'(\xi)(v-u)=0$. Así $h$ toma un único valor. La implicación inversa resulta derivando $f-g=C$ en puntos interiores. $\square$

No basta saber que $f'(a)=g'(a)$ en **un único punto** para concluir igualdad salvo constante en un intervalo. Por ejemplo, $f(x)=x^2$ y $g(x)=0$ tienen derivadas iguales en cero, pero no fuera de ese punto. Tampoco puede aplicarse Rolle sin continuidad en el segmento y derivabilidad interior.

## 11.3. Acumulación: el nexo que convierte dos problemas en uno

**Teorema 11.2 (reconstrucción integral de una función; `EDC-C11-THM-002`).** Sea $f\in C^1([a,b])$, entendiendo por ello que $f$ es continua en el segmento, derivable en el interior y que $f'$ se prolonga continuamente hasta los extremos. Para todo $x\in[a,b]$,

$$
\boxed{f(x)=f(a)+\int_a^x f'(t)\,dt.}
$$

Recíprocamente, para toda $g\in C([a,b])$, la función $G(x)=c+\int_a^x g(t)dt$ satisface $G'=g$ en $(a,b)$ y $G(a)=c$.

**Demostración.** La primera identidad es la segunda parte del Teorema Fundamental (C06) aplicada a la primitiva $f$ del integrando continuo $f'$. Para la recíproca, C05 garantiza la integral y la primera parte de C06 afirma que su función de acumulación tiene derivada $g$ en cada punto interior; en $a$, la integral tiene valor cero. $\square$

Las dos direcciones requieren distinguir objetos y premisas: en la primera partimos de una función derivable cuya derivada es integrable; en la segunda partimos de un integrando continuo y **construimos** su primitiva. Es precisamente esta doble posibilidad —pasar de variación a acumulación y retornar— la que organiza C06, y no una cancelación formal de $d$ y $\int$ sin hipótesis.

**Corolario 11.1 (una sola primitiva tras fijar el dato; `EDC-C11-COR-001`).** Si $g$ es continua en $[a,b]$, el problema $y'=g$ en $(a,b)$, $y(a)=y_0$, con $y$ continua en $[a,b]$, tiene la única solución $y(x)=y_0+\int_a^xg(t)dt$.

**Demostración.** La existencia proviene de la segunda mitad del Teorema 11.2. Si $z$ es otra solución, el Teorema 11.1 aplicado a $z$ y a la solución construida dice que difieren por una constante; el dato en $a$ la hace cero. $\square$

## 11.4. El control cuantitativo une sumas, integrales y derivadas

No basta reconocer una integral como límite: podemos **medir** el error de las sumas empleadas para calcularla.

**Teorema 11.3 (cuadratura con error explícito; `EDC-C11-THM-003`).** Sea $f$ continua en $[a,b]$ y derivable en $(a,b)$, $a<b$, con $|f'(x)|\le M$ en todo punto interior, donde $M\ge0$. Para una partición $P:a=x_0<\cdots <x_n=b$ y muestras $\xi_i\in[x_{i-1},x_i]$,

$$
\boxed{\left|\int_a^bf(x)\,dx-
\sum_{i=1}^n f(\xi_i)(x_i-x_{i-1})\right|
\le\frac M2\sum_{i=1}^n(x_i-x_{i-1})^2.}
$$

En particular, para $n$ subintervalos iguales, el error no supera $M(b-a)^2/(2n)$.

**Demostración.** Por el valor medio de C03, para $t,\xi_i$ dentro del $i$-ésimo subintervalo, $|f(t)-f(\xi_i)|\le M|t-\xi_i|$. La linealidad, aditividad y desigualdad triangular de C05 dan

$$
\left|\int_{x_{i-1}}^{x_i}f(t)dt-f(\xi_i)\Delta x_i\right|
\le M\int_{x_{i-1}}^{x_i}|t-\xi_i|dt.
$$

Escribiendo $u=\xi_i-x_{i-1}$ y $v=x_i-\xi_i$, tenemos $u,v\ge0$ y $u+v=\Delta x_i$. La integral de la distancia al punto muestral vale $(u^2+v^2)/2\le(u+v)^2/2=(\Delta x_i)^2/2$, por integración de potencias (C06). Sumamos las desigualdades finitas. Para una partición uniforme $\Delta x_i=(b-a)/n$ y la suma de cuadrados vale $(b-a)^2/n$. $\square$

**Consecuencia.** Si $b-a=1$, $M=2$ y elegimos $n=100$, cualquier muestra en cada subintervalo produce un error no mayor que $0.01$. Este control vale sin conocer previamente el valor exacto de la integral. Es una aplicación de C03 y C05, no un nuevo postulado de integración.

**Teorema 11.4 (error de acumulación local; `EDC-C11-THM-004`).** Sea $f\in C^1([a,b])$ y $|f'(t)|\le M$ en el segmento. Definamos $A(x)=\int_a^x f(t)dt$. Para $x\in[a,b]$,

$$
\boxed{|A(x)-f(a)(x-a)|\le\tfrac M2(x-a)^2.}
$$

**Demostración.** Por aditividad y linealidad, $A(x)-f(a)(x-a)=\int_a^x[f(t)-f(a)]dt$. El teorema del valor medio proporciona $|f(t)-f(a)|\le M(t-a)$ para $t\in[a,x]$; integramos esta cota y obtenemos $M(x-a)^2/2$. $\square$

La afirmación aproxima una **acumulación** mediante la tasa inicial y certifica el error usando la variación de esa misma tasa. En este ejemplo las tres grandes operaciones del cálculo no sólo coexisten: sus pruebas se encadenan.

## 11.5. Series y Taylor: qué representa realmente una aproximación

C08 permite sumar, multiplicar, derivar e integrar series de potencias *dentro de su radio* con estimaciones de colas. C09 construye el polinomio de Taylor de una función $f$ y demuestra un resto. Estos dos resultados no deben confundirse.

**Proposición 11.2 (tres preguntas diferentes; `EDC-C11-PRP-002`).** Supongamos que $f$ admite derivadas de todos los órdenes cerca de $a$. Las siguientes afirmaciones son distintas: (i) para cada $n$ existe $T_{n,a}f$; (ii) para cierto $x$, la serie $\sum_{n\ge0} f^{(n)}(a)(x-a)^n/n!$ converge; (iii) la suma de esa serie vale $f(x)$. La primera es una construcción finita y la segunda no implica la tercera.

**Demostración.** Los coeficientes de $T_{n,a}f$ están definidos por derivadas finitas: eso prueba (i). Consideremos la función de C09,

$$
g(x)=\begin{cases}e^{-1/x^2},&x\ne0,\\0,&x=0.\end{cases}
$$

C09 demostró que $g\in C^\infty(\mathbb R)$ y $g^{(k)}(0)=0$ para todo $k$. Su serie en cero converge a cero para **cada** $x$, pero para $x\ne0$ se tiene $g(x)>0$. Luego (ii) no implica (iii). $\square$

**Teorema 11.5 (certificación de Taylor por el resto; `EDC-C11-THM-005`).** Sea $f\in C^\infty$ en un intervalo que contiene $a$ y $x$. Escribamos $T_{n,a}f(x)$ y $R_n(x)=f(x)-T_{n,a}f(x)$. Se tiene

$$
f(x)=\sum_{k=0}^{\infty}\frac{f^{(k)}(a)}{k!}(x-a)^k
\quad\Longleftrightarrow\quad R_n(x)\longrightarrow0.
$$

Si sobre el segmento entre $a$ y $x$ se cumple $|f^{(n+1)}|\le M_{n+1}$, una condición suficiente es

$$
\frac{M_{n+1}|x-a|^{n+1}}{(n+1)!}\longrightarrow0.
$$

**Demostración.** Las sumas parciales de la serie de Taylor son, por definición, los polinomios $T_{n,a}f(x)$. Su convergencia al valor $f(x)$ equivale exactamente a $R_n(x)\to0$. La cota de Taylor–Lagrange de C09 aplicada para cada orden $n$ da $|R_n(x)|\le M_{n+1}|x-a|^{n+1}/(n+1)!$. Si el mayorante tiende a cero, la Proposición 11.1 concluye. $\square$

Un resto $o(|x-a|^n)$ de **orden fijo** cuando $x\to a$ no prueba el límite de restos cuando $n\to\infty$ con $x$ fijo. Tampoco el radio de convergencia de una serie obliga a que ésta represente una función externa: el radio responde únicamente a una pregunta sobre los coeficientes.

## 11.6. Leyes de cambio: resolver, verificar, demostrar unicidad

C10 convierte el nexo entre derivada e integral en una herramienta para buscar **funciones desconocidas**. Si $p,q$ son continuas en un intervalo $J$ y $t_0\in J$, el PVI lineal $y'+p(t)y=q(t)$, $y(t_0)=y_0$ tiene una solución explícita y única:

$$
y(t)=e^{-P(t)}\left(y_0+\int_{t_0}^t e^{P(s)}q(s)ds\right),
\qquad P(t)=\int_{t_0}^t p(u)du.
$$

La **existencia** se prueba derivando esa función; la **unicidad**, comprobando que cualquier otra satisface la misma identidad después de multiplicar por el factor integrante. En cambio, la condición Lipschitz de C10 se utilizó para demostrar sólo la unicidad **entre soluciones ya existentes** de campos más generales.

**Proposición 11.3 (existencia, unicidad y globalidad no son sinónimos; `EDC-C11-PRP-003`).** Las siguientes situaciones, todas probadas en C10, son posibles: (a) un PVI tiene exactamente una solución global; (b) un PVI tiene varias soluciones globales; (c) un PVI tiene solución única en la rama inicial, pero ésta no se prolonga como solución real finita por todo tiempo.

**Demostración.** (a) $y'=-y$, $y(0)=1$ admite únicamente $y(t)=e^{-t}$ sobre $\mathbb R$, por 10.2. (b) $y'=\sqrt{|y|}$, $y(0)=0$ admite las infinitas funciones $y_c$ de la Proposición 10.3, todas globales. (c) $y'=y^2$, $y(0)=1$ posee la fórmula $y(t)=1/(1-t)$ mientras $t<1$. La separación sobre $y>0$, o una comparación entre soluciones usando $1/y$, prueba unicidad en su rama; la divergencia a $+\infty$ cuando $t\uparrow1$ impide prolongación clásica finita a través del punto. $\square$

**Corolario 11.2 (modelo y teorema; `EDC-C11-COR-002`).** Si una ley física o biológica conduce a una EDO lineal con parámetros que cumplen las hipótesis del Teorema 10.3, queda demostrada la existencia y unicidad **matemáticas** de su trayectoria; no queda demostrada por ello la validez empírica de la ley.

**Justificación.** El Teorema 10.3 parte de los coeficientes como hipótesis y deduce propiedades lógicas de una función. La afirmación de que temperatura, resistencia o población satisfacen efectivamente esos coeficientes requiere observaciones externas a las premisas del teorema. $\square$

## 11.7. Contraejemplos: el mapa de las fronteras

La solidez del cálculo depende tanto de sus teoremas como de saber **cuándo dejan de poder aplicarse**.

**Proposición 11.4 (fronteras de la inferencia; `EDC-C11-PRP-004`).** Son falsas, sin hipótesis adicionales, las implicaciones «continua $\Rightarrow$ derivable», «acotada $\Rightarrow$ integrable», «$a_n\to0\Rightarrow\sum a_n$ convergente», «$C^\infty\Rightarrow$ analítica» y «campo continuo de EDO $\Rightarrow$ unicidad del PVI».

**Demostración.** La función $|x|$ es continua y no derivable en cero (C01). La indicadora de $\mathbb Q\cap[0,1]$ es acotada y no integrable por Darboux, pues en cada subintervalo el ínfimo es cero y el supremo uno (C05). La serie $\sum_{n=1}^{\infty}1/n$ diverge por bloques aunque $1/n\to0$ (C08). La función plana de §11.5 es $C^\infty$ y no analítica en cero (C09). La ecuación $y'=\sqrt{|y|}$ tiene infinitas soluciones para el mismo dato (C10). Cada contraejemplo niega exactamente la implicación correspondiente. $\square$

**Lema 11.1 (una discontinuidad no destruye siempre la integral; `EDC-C11-LEM-001`).** Sea $f:[a,b]\to\mathbb R$ la función que vale cero salvo en un único punto $c\in[a,b]$, donde vale $d$. Entonces $f$ es Riemann–Darboux integrable y su integral es cero.

**Demostración.** Si $d=0$, es inmediata. Si $d\ne0$, para cualquier $\varepsilon>0$ construimos una partición en la que la suma de las longitudes de los subintervalos que contienen $c$ es menor que $\varepsilon/|d|$ (en un extremo basta un intervalo corto; en un punto interior se eligen dos vecinos próximos). Fuera de esos intervalos $f=0$; dentro de ellos la oscilación no supera $|d|$. Por tanto $U(f,P)-L(f,P)\le |d|\cdot\text{longitud afectada}<\varepsilon$. El criterio de Darboux C05 prueba integrabilidad. Además, las sumas inferiores y superiores en magnitud quedan entre $-|d|\cdot\text{longitud afectada}$ y $|d|\cdot\text{longitud afectada}$; al dejar decrecer la longitud obtenemos integral cero. $\square$

El lema muestra por qué «discontinua» y «no integrable» no son sinónimos. En este volumen hemos probado resultados suficientes específicos; **no** hemos demostrado el criterio de medida nula de discontinuidades, que pertenece a una ampliación del análisis.

## 11.8. Geometrías de aproximación antes del cálculo moderno

Para comprender la amplitud del problema, debemos distinguir los métodos de aproximación **según sus contextos**, no clasificarlos retrospectivamente como si fuesen capítulos de un manual moderno.

En la tradición griega, los argumentos de agotamiento asociados a Eudoxo y las demostraciones de Arquímedes atacaron problemas de área y volumen mediante comparaciones con figuras conocidas. El caso paradigmático de C04 —el segmento de parábola que mide $4T/3$— procede de una investigación geométrica, no de la definición de integral de Riemann. La formulación cuantitativa con sumas finitas y restos de C04 es una reconstrucción matemática propia que permite enlazar aquellas preguntas con C05.

En la tradición china, los comentarios de Liu Hui a los *Nueve capítulos sobre el arte matemático*, fechados convencionalmente en el siglo III, documentan razonamientos por subdivisión y aproximación geométrica. Es históricamente más cuidadoso hablar de **procedimientos comparables de refinamiento**, no identificarlos con la integral de Darboux ni postular una transmisión entre tradiciones sin prueba.

En Kerala, al sur de la India, la historiografía reconoce resultados de series trigonométricas atribuidos a Madhava, de fines del siglo XIV y comienzos del XV, preservados en obras posteriores de su escuela. Nuestra expresión $\arctan x=\sum(-1)^n x^{2n+1}/(2n+1)$ es una **traducción moderna de una identidad**; no es transcripción de un manuscrito conservado de Madhava ni se equipara sin examen con nuestras pruebas de convergencia. El problema historiográfico incluye la transmisión indirecta a través de autores posteriores y la diferencia entre descubrir fórmulas y desarrollar una teoría general de funciones analíticas.

Estas tres historias demuestran que las preguntas por acumulaciones y aproximaciones no pertenecen en exclusiva a una secuencia europea única. Tampoco autorizan sustituir el estudio de fuentes por una narrativa de «primeros inventores». La procedencia de cada afirmación se registra en [las notas históricas H1–H3](capitulo-11-notas.md).

## 11.9. La síntesis moderna: tangente, cuadratura y movimiento

Los siglos XVI y XVII intensificaron la investigación de tangentes, máximos, indivisibles, áreas, movimiento y problemas inversos. En la historiografía consultada aparecen Fermat, Cavalieri, Torricelli, Barrow, Newton y Leibniz como participantes de tradiciones que se superponen pero no se reducen a una formulación unitaria previa.

Newton organizó parte de su trabajo en torno a magnitudes que *fluyen* y sus tasas, denominadas *fluxiones*. Leibniz elaboró una notación diferencial e integral con fuerte orientación operatoria. La relación inversa entre derivar y acumular figura en ambas genealogías, pero nuestra demostración del Teorema Fundamental para funciones continuas sobre un intervalo real es una **reformulación contemporánea**. No debemos adjudicar a ninguno de estos matemáticos la formulación literal en términos de $\sup_PL$, $\inf_PU$ o $\varepsilon$–$\delta$.

La controversia de prioridad entre Newton y Leibniz ha recibido numerosas reconstrucciones historiográficas; la finalidad de C11 no es resolverla mediante un criterio arbitrario de primacía, sino reconocer la diferencia entre creación de procedimientos, manuscritos, circulación, publicación, notación y posterior rigor. Lo mismo ocurre con el nombre «Taylor» para series que poseen antecedentes en tradiciones diferentes. En el arco de este libro, la **unidad conceptual demostrada** proviene del Teorema Fundamental, independientemente de la prioridad histórica de una notación.

## 11.10. El rigor del siglo XIX no consistió en cambiar nombres

Con Cauchy, en particular en el *Cours d'analyse* de 1821, la exposición de límites, continuidad y series adquiere un programa explícito de control de condiciones. El uso de infinitésimos y límites en su obra debe leerse históricamente y no identificarse sin reservas con nuestra formalización de sucesiones, cuantificadores y intervalos. Incluso formulaciones prestigiosas podían contener errores cuando se transferían propiedades desde sucesiones de funciones a sus límites sin el control requerido.

La teoría moderna de integración distingue el papel de las sumas de Riemann y la presentación por sumas superior e inferior de Darboux. El artículo de Gaston Darboux, «Mémoire sur les fonctions discontinues» (1875), constituye un hito bibliográfico verificable. El criterio de C05 es nuestro teorema moderno en $[a,b]$; no es una transcripción del francés original. El surgimiento del análisis del siglo XIX también amplió notablemente los problemas de continuidad, diferenciabilidad, aproximación y convergencia.

**Lema 11.2 (una distinción entre límite puntual y cota común; `EDC-C11-LEM-002`).** En $[0,1]$, la sucesión $f_n(x)=x^n$ converge puntualmente a la función $f$ dada por $f(x)=0$ si $0\le x<1$ y $f(1)=1$, pero no admite aproximación con un error $\varepsilon_n\to0$ válido para **todos** los $x\in[0,1]$.

**Demostración.** Si $x<1$, la sucesión geométrica $x^n$ tiende a cero; en $x=1$ vale siempre uno. Para cada $n$ y $x<1$ se tiene $|f_n(x)-f(x)|=x^n$, cuyo supremo sobre $0\le x<1$ es uno, pues se pueden tomar $x$ arbitrariamente próximos a uno. Por tanto $\sup_{x\in[0,1]}|f_n(x)-f(x)|=1$ para todos los $n$, y no existe la cota decreciente indicada. $\square$

Este ejemplo explica **por qué** la cota interior del Teorema 8.8 se formuló sobre segmentos estrictamente contenidos en el radio. No construimos aquí una teoría general de convergencia uniforme, pero sabemos distinguir rigurosamente una convergencia punto por punto de una estimación que funciona en todos los puntos de un intervalo.

## 11.11. El umbral del análisis real: problemas legítimamente abiertos

El cálculo elemental que hemos construido descansa en la completitud de $\mathbb R$ (C00) y en condiciones precisas. Queda fuera de su alcance demostrar el criterio general de integrabilidad de una función acotada mediante conjuntos de discontinuidad de medida nula; exigiría herramientas de medida. Queda asimismo pendiente desarrollar la convergencia uniforme para familias arbitrarias de funciones, intercambios generales de límites y derivadas, integración impropia, funciones de varias variables y espacios métricos generales.

Para EDO, C10 resolvió explícitamente clases lineales y ciertas ecuaciones separables, y estableció un principio de unicidad bajo Lipschitz para soluciones preexistentes. No probó la existencia general de soluciones bajo hipótesis Lipschitz ni su continuación máxima en sistemas. Para algoritmos, sólo demostró el error **local** de un paso de Euler, no un teorema global de convergencia numérica.

**Proposición 11.5 (lo que el error local no dice; `EDC-C11-PRP-005`).** Una cota $|y(t+h)-[y(t)+hF(t,y(t))]|\le Mh^2/2$ válida para cada paso que comienza en el valor **exacto** no contiene, por sí misma, una cota para el error después de $N$ pasos de Euler que comienzan en los valores **aproximados**.

**Justificación.** El segundo paso numérico utiliza $Y_1$ en lugar de $y(t_1)$. La hipótesis del lema local se aplica a $F(t_1,y(t_1))$, no controla la diferencia $F(t_1,Y_1)-F(t_1,y(t_1))$. Para acotar ésta hay que imponer y emplear una regularidad en la segunda variable, y luego propagar recursivamente los errores. Esa premisa y ese argumento son adicionales; no están contenidos en el mero resto de Taylor de un paso. $\square$

## 11.12. La unidad alcanzada y el trabajo de lectura

El proyecto unificador del libro puede escribirse, ahora con referencias a pruebas completas, de este modo:

| Pregunta | Construcción | Resultado y límite probado |
|---|---|---|
| ¿Cómo cambia una función cerca de un punto? | Cociente incremental | Derivada interior y aproximación afín (C01–C02); no toda función continua es derivable |
| ¿Qué dice su tasa sobre todo un intervalo? | Valor medio y cotas | Monotonía, extremos y variaciones controladas (C03) |
| ¿Qué significa acumular? | Agotamiento, particiones y sumas | Integral de Riemann–Darboux (C04–C05); no toda función acotada es integrable |
| ¿Cómo regresamos de una tasa a un valor? | Dos partes del Teorema Fundamental | Reconstrucción por acumulación y primitivas bajo hipótesis (C06–C07) |
| ¿Cuándo representa una suma infinita a una función? | Series y control interior | Radio, colas y operaciones justificadas (C08); fronteras independientes |
| ¿Cuándo aproxima Taylor de verdad? | Polinomio y resto | Resto finito demostrado; representación cuando $R_n\to0$ (C09) |
| ¿Puede una ley determinar una trayectoria? | EDO, dato inicial, integración y unicidad | Clases explícitas; unicidad condicional, excepciones y dominio (C10) |

La continuidad, las derivadas, las integrales y las soluciones de ecuaciones diferenciales no son «el mismo objeto». Su **unidad matemática** consiste en que una cadena de teoremas hace posible pasar de unas preguntas a otras con las condiciones bajo control. La unidad histórica es más compleja: métodos con parecidos matemáticos se desarrollaron en tradiciones y épocas diferentes, y sus conceptos fueron transformados por la escritura posterior.

El libro se cierra con una disciplina intelectual, no con una fórmula mágica: **identificar el objeto, declarar el dominio, explicitar el límite, demostrar el error y comprobar cada hipótesis antes de usar un teorema**. Los [treinta ejercicios de síntesis](capitulo-11-ejercicios.md) y sus [treinta soluciones separadas](capitulo-11-soluciones.md) permiten verificar si esa disciplina se ha adquirido. Las [notas H1–H9](capitulo-11-notas.md) preservan el estado real de consulta de las fuentes, y la auditoría transversal posterior determinará si los doce capítulos forman una edición íntegra coherente.

### Dependencias y límites editoriales

- **Resultados usados:** C00–C10, en particular C03 (valor medio), C05 (Darboux), C06 (Teorema Fundamental), C08 (series), C09 (Taylor) y C10 (EDO).
- **Aportaciones demostradas de C11:** cinco teoremas `EDC-C11-THM-001--005`, cinco proposiciones `PRP-001--005`, dos lemas `LEM-001--002`, dos corolarios `COR-001--002` y una definición `DEF-001`.
- **Resultados no reivindicados:** teoría de medida, convergencia uniforme general, Picard–Lindelöf completo, integración de Lebesgue, EDP, cálculo multivariable y análisis funcional.
- **Frontera editorial:** el cierre sustantivo de C11 no equivale por sí solo a auditoría transversal completa, edición web ni pruebas tipográficas de un volumen integral.
