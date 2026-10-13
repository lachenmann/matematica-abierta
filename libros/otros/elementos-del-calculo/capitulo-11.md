---
title: 'Capítulo 11. El cálculo como teoría: alcance, historia y fundamentos'
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
source-id: EDC-C11
source-sha256: ca6e7894c7cafdce5191fb0cd8f3c46a592e44b756a77bd4ca5886855bf47006
content-id: MA-BCH-0342
content-type: book-chapter
related:
  - MA-BOK-0015
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-11.html) · [Ejercicios](capitulo-11-ejercicios.html) · [Soluciones](capitulo-11-soluciones.html) · [Notas históricas](capitulo-11-notas.html)

[← Capítulo 10](capitulo-10.html)

> **Pregunta generadora.** ¿Qué hemos demostrado efectivamente al transformar problemas de tangentes, velocidades, cuadraturas, series y trayectorias en una teoría del cálculo? ¿De qué supuestos depende esa unidad y qué dificultades anuncian el análisis real?

Una secante se acerca a una tangente, una suma de rectángulos aproxima una integral y un polinomio puede acercarse a una función. En cada caso hemos tenido que averiguar qué cambia al mejorar la aproximación y cuánto falta para alcanzar el objeto buscado. La semejanza entre esos problemas se vuelve una relación matemática cuando podemos demostrar que el error tiende a cero y usar después el límite para obtener información nueva.

La derivada permitió controlar la variación de una función en un intervalo; ese control dio cotas para sumas e integrales. El Teorema Fundamental hizo posible reconstruir una función desde su tasa de cambio, y esa reconstrucción sirvió para resolver ecuaciones diferenciales. Al estudiar series y Taylor encontramos una dificultad adicional: disponer de aproximaciones de todos los órdenes todavía no asegura que lleguemos a la función. Los contraejemplos hicieron visibles las condiciones que faltaban.

Este capítulo reúne esas conexiones mediante consecuencias demostradas con C00–C10. Volveremos a las hipótesis allí donde una afirmación parece convincente pero puede fallar. También reconoceremos preguntas semejantes en las cuadraturas antiguas, las aproximaciones geométricas de otras tradiciones y la formación del cálculo moderno. La historia permitirá situar los problemas; las pruebas actuales explicarán el alcance que hemos podido darles en este libro. Las teorías generales de espacios métricos, medida y ecuaciones diferenciales quedan como continuación.

## 11.1. El método del cálculo: una cadena de aproximaciones justificadas

**Definición 11.1 (certificado elemental de aproximación; `EDC-C11-DEF-001`).** Diremos que una familia de aproximantes reales $A_n$ **certifica** el valor $A$ si, además de una regla explícita de construcción de cada $A_n$, se ha demostrado una cota $|A_n-A|\le\varepsilon_n$ donde $\varepsilon_n\to0$. Cuando $A$ aún no se conoce, podrá demostrarse primero que $(A_n)$ es de Cauchy y emplearse la completitud de $\mathbb R$ (C00), identificando después su límite. Ésta es una convención didáctica, no una definición general de convergencia numérica nueva.

El error se controla de distintas maneras según lo que aproximamos. En el cociente incremental de C01, acercamos dos puntos haciendo $h\to0$; para la integral de C05 refinamos una partición; en las series de C08 y los polinomios de C09 aumentamos el número de términos. En el paso de Euler de C10 fijamos un instante de partida y hacemos pequeño el paso temporal. Conviene conservar esa información al escribir una cota: el parámetro que varía y los valores que permanecen fijos determinan qué límite estamos demostrando.

**Proposición 11.1 (de la cota al límite; `EDC-C11-PRP-001`).** Si $A_n,A\in\mathbb R$, $\varepsilon_n\ge0$, $\varepsilon_n\to0$ y $|A_n-A|\le\varepsilon_n$ para todo $n$, entonces $A_n\to A$.

**Demostración.** Dado $\varepsilon>0$, el límite $\varepsilon_n\to0$ proporciona $N$ tal que $n\ge N$ implica $\varepsilon_n<\varepsilon$. Por la desigualdad anunciada, $|A_n-A|<\varepsilon$ para tales $n$. Ésta es exactamente la definición secuencial de límite de C00. $\square$

Para aplicar la proposición hace falta una sucesión de cotas que efectivamente tienda a cero. Una estimación de Taylor en un orden fijo puede disminuir al acercarnos al centro, sin ofrecer control al aumentar el orden en otro punto. Del mismo modo, el error local de Euler mide un paso desde una posición exacta; para una trayectoria calculada mediante muchos pasos tendremos que estudiar cómo se transmite el error entre ellos. La información que contiene una cota depende del problema para el que se obtuvo.

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

La igualdad de derivadas tiene que cumplirse en todo el interior del intervalo, porque el valor medio puede elegir su punto intermedio en cualquiera de sus partes. Las funciones $f(x)=x^2$ y $g(x)=0$ muestran qué ocurre si sólo conocemos esa igualdad en cero: allí tienen la misma pendiente, pero su diferencia toma valores distintos en cualquier entorno. El teorema permite comparar cambios sobre un intervalo cuando podemos usar continuidad hasta los extremos y derivabilidad entre ellos.

## 11.3. Acumulación: el nexo que convierte dos problemas en uno

**Teorema 11.2 (reconstrucción integral de una función; `EDC-C11-THM-002`).** Sea $f\in C^1([a,b])$, entendiendo por ello que $f$ es continua en el segmento, derivable en el interior y que $f'$ se prolonga continuamente hasta los extremos. Para todo $x\in[a,b]$,

$$
\boxed{f(x)=f(a)+\int_a^x f'(t)\,dt.}
$$

Recíprocamente, para toda $g\in C([a,b])$, la función $G(x)=c+\int_a^x g(t)dt$ satisface $G'=g$ en $(a,b)$ y $G(a)=c$.

**Demostración.** La derivada de $f$ se prolonga como función continua al segmento y, por C05, es integrable. La función $f$ es una primitiva de ese integrando en el interior. La segunda parte del Teorema Fundamental de C06 evalúa entonces su integral como $f(x)-f(a)$, lo que da la identidad anunciada, incluidos los extremos por continuidad.

Para la recíproca, partimos del integrando continuo $g$. C05 asegura que podemos acumularlo desde $a$ hasta cada $x$ del segmento, y la primera parte de C06 da $G'(x)=g(x)$ en el interior. En $a$, la integral sobre el segmento de longitud cero vale cero, de modo que $G(a)=c$. $\square$

La primera dirección parte de una función y permite recuperar la diferencia entre dos de sus valores integrando su derivada. En la segunda tenemos una tasa continua y construimos una función que posee esa tasa, dejando libre su valor inicial. El dato $c$ no cambia la derivada, pero fija la altura de la primitiva. Esta posibilidad de ir y volver entre tasas y valores explica el uso conjunto de las dos partes del Teorema Fundamental.

**Corolario 11.1 (una sola primitiva tras fijar el dato; `EDC-C11-COR-001`).** Si $g$ es continua en $[a,b]$, el problema $y'=g$ en $(a,b)$, $y(a)=y_0$, con $y$ continua en $[a,b]$, tiene la única solución $y(x)=y_0+\int_a^xg(t)dt$.

**Demostración.** La existencia proviene de la segunda mitad del Teorema 11.2. Si $z$ es otra solución, el Teorema 11.1 aplicado a $z$ y a la solución construida dice que difieren por una constante; el dato en $a$ la hace cero. $\square$

## 11.4. El control cuantitativo une sumas, integrales y derivadas

Una suma de rectángulos aproxima la integral al refinar una partición. Si además sabemos cuánto puede variar el integrando, podemos decidir antes de calcular cuántos rectángulos bastarán para alcanzar una tolerancia. Una cota de la derivada proporciona precisamente esa información: limita la diferencia entre el valor muestral y los demás valores del integrando en cada subintervalo.

**Teorema 11.3 (cuadratura con error explícito; `EDC-C11-THM-003`).** Sea $f$ continua en $[a,b]$ y derivable en $(a,b)$, $a<b$, con $|f'(x)|\le M$ en todo punto interior, donde $M\ge0$. Para una partición $P:a=x_0<\cdots <x_n=b$ y muestras $\xi_i\in[x_{i-1},x_i]$,

$$
\boxed{\left|\int_a^bf(x)\,dx-
\sum_{i=1}^n f(\xi_i)(x_i-x_{i-1})\right|
\le\frac M2\sum_{i=1}^n(x_i-x_{i-1})^2.}
$$

En particular, para $n$ subintervalos iguales, el error no supera $M(b-a)^2/(2n)$.

**Demostración.** Consideremos un subintervalo y el punto muestral $\xi_i$. La diferencia entre su integral y el rectángulo correspondiente es la integral de $f(t)-f(\xi_i)$. Para dos puntos distintos del subintervalo, el valor medio de C03 permite acotar esa diferencia por $M|t-\xi_i|$; si coinciden, la misma desigualdad vale porque ambos lados son cero. La continuidad en los extremos permite usar también muestras situadas allí. Por linealidad y desigualdad triangular de C05,

$$
\left|\int_{x_{i-1}}^{x_i}f(t)dt-f(\xi_i)\Delta x_i\right|
\le M\int_{x_{i-1}}^{x_i}|t-\xi_i|dt.
$$

Para integrar la distancia a $\xi_i$, dividimos el subintervalo en ese punto. A su izquierda la distancia es $\xi_i-t$ y a su derecha es $t-\xi_i$. Si $u=\xi_i-x_{i-1}$ y $v=x_i-\xi_i$, ambas longitudes son no negativas y $u+v=\Delta x_i$. Las dos integrales suman $(u^2+v^2)/2$. Como $2uv\ge0$, esta cantidad no supera $(u+v)^2/2=(\Delta x_i)^2/2$. El mismo cálculo incluye una muestra en un extremo, pues una de las longitudes es cero.

La aditividad descompone la integral total en esos subintervalos, y la desigualdad triangular permite sumar sus errores. Obtenemos la primera cota. Para una partición uniforme, cada ancho vale $(b-a)/n$; al sumar sus $n$ cuadrados obtenemos $(b-a)^2/n$, que da la estimación anunciada. $\square$

**Consecuencia.** Si $b-a=1$, $M=2$ y elegimos $n=100$, cualquier muestra en cada subintervalo produce un error no mayor que $0.01$. Este control vale sin conocer previamente el valor exacto de la integral. Es una aplicación de C03 y C05, no un nuevo postulado de integración.

**Teorema 11.4 (error de acumulación local; `EDC-C11-THM-004`).** Sea $f\in C^1([a,b])$ y $|f'(t)|\le M$ en el segmento. Definamos $A(x)=\int_a^x f(t)dt$. Para $x\in[a,b]$,

$$
\boxed{|A(x)-f(a)(x-a)|\le\tfrac M2(x-a)^2.}
$$

**Demostración.** Reemplazar la tasa $f(t)$ por su valor inicial da la acumulación $f(a)(x-a)$. Al restarla de $A(x)$ y usar linealidad, el error es $\int_a^x[f(t)-f(a)]dt$. Para $t>a$, el valor medio acota $|f(t)-f(a)|$ por $M(t-a)$; en $t=a$ la diferencia es cero. La desigualdad triangular permite integrar esa cota no negativa sobre $[a,x]$, y su integral vale $M(x-a)^2/2$. Si $x=a$, la acumulación y la aproximación se anulan, por lo que la misma estimación sigue siendo válida. $\square$

La derivada limita cuánto cambia la tasa; esa variación limita, a su vez, el error de la acumulación que obtuvimos al mantener la tasa inicial. Por eso aparece una potencia cuadrática de la longitud: la cota lineal $M(t-a)$ se integra a lo largo del segmento. Las reglas de variación y acumulación intervienen en una misma estimación.

## 11.5. Series y Taylor: qué representa realmente una aproximación

Una serie de potencias comienza con coeficientes dados y exige estudiar para qué valores de la variable tiene suma. Un polinomio de Taylor comienza con una función y utiliza sus derivadas en un punto para formar una aproximación finita. Si prolongamos ese procedimiento a todos los órdenes, obtenemos una serie, pero todavía queda por averiguar si su suma recupera la función de partida. El ejemplo plano de C09 permite ver la separación entre esas preguntas.

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

**Demostración.** Para un $x$ fijo, las sumas parciales de la serie son exactamente los valores $T_{n,a}f(x)$. Afirmar que la serie suma $f(x)$ significa que estos valores tienden a $f(x)$; al restar de $f(x)$, esa afirmación equivale a $R_n(x)\to0$.

Taylor–Lagrange de C09 acota, para cada orden, $|R_n(x)|$ por $M_{n+1}|x-a|^{n+1}/(n+1)!$. Si esos mayorantes tienden a cero al crecer $n$, la Proposición 11.1 aplica a las sumas parciales y prueba que convergen a $f(x)$. En $x=a$, los polinomios ya valen $f(a)$ y todos los restos son cero. $\square$

En el resto $o(|x-a|^n)$ de orden fijo, acercamos $x$ al centro después de escoger $n$. Para representar la función mediante la serie, mantenemos $x$ fijo y hacemos crecer $n$. La función plana satisface las aproximaciones locales de todos los órdenes, pero sus restos en un $x\ne0$ permanecen iguales a $g(x)>0$, cualquiera que sea $n$. Por eso hace falta examinar el segundo límite por separado. El radio de convergencia informa sobre la serie formada por los coeficientes; identificar su suma con una función dada requiere el argumento adicional de los restos.

## 11.6. Leyes de cambio: resolver, verificar, demostrar unicidad

C10 convierte el nexo entre derivada e integral en una herramienta para buscar **funciones desconocidas**. Si $p,q$ son continuas en un intervalo $J$ y $t_0\in J$, el PVI lineal $y'+p(t)y=q(t)$, $y(t_0)=y_0$ tiene una solución explícita y única:

$$
y(t)=e^{-P(t)}\left(y_0+\int_{t_0}^t e^{P(s)}q(s)ds\right),
\qquad P(t)=\int_{t_0}^t p(u)du.
$$

La **existencia** se prueba derivando esa función; la **unicidad**, comprobando que cualquier otra satisface la misma identidad después de multiplicar por el factor integrante. En cambio, la condición Lipschitz de C10 se utilizó para demostrar sólo la unicidad **entre soluciones ya existentes** de campos más generales.

**Proposición 11.3 (existencia, unicidad y globalidad no son sinónimos; `EDC-C11-PRP-003`).** Las siguientes situaciones, todas probadas en C10, son posibles: (a) un PVI tiene exactamente una solución global; (b) un PVI tiene varias soluciones globales; (c) un PVI tiene solución única en la rama inicial, pero ésta no se prolonga como solución real finita por todo tiempo.

**Demostración.** Para (a), el Teorema 10.2 aplicado a $y'=-y$, $y(0)=1$ proporciona $y(t)=e^{-t}$ y prueba que es la única solución en toda la recta. Para (b), la Proposición 10.3 construye las funciones $y_c$ que permanecen en cero hasta $c\ge0$ y después valen $(t-c)^2/4$. Son distintas, todas están definidas en $\mathbb R$ y todas tienen el mismo dato inicial.

Para (c), en la rama positiva de $y'=y^2$ tomamos la primitiva $B(u)=\int_1^u dv/v^2=1-1/u$. La separación da $B(y(t))=t$, por lo que $y(t)=1/(1-t)$ para $t<1$. La fórmula se verifica derivando y toma el valor uno en cero. El Teorema 10.5 la hace única entre las soluciones de esa rama en el intervalo común conectado que contiene el dato. Cuando $t\uparrow1$, diverge a $+\infty$; cualquier prolongación real continua a través de uno tendría que poseer allí un valor finito compatible con el límite, lo que es imposible. $\square$

**Corolario 11.2 (modelo y teorema; `EDC-C11-COR-002`).** Si una ley física o biológica conduce a una EDO lineal con parámetros que cumplen las hipótesis del Teorema 10.3, queda demostrada la existencia y unicidad **matemáticas** de su trayectoria; no queda demostrada por ello la validez empírica de la ley.

**Justificación.** El Teorema 10.3 parte de los coeficientes como hipótesis y deduce propiedades lógicas de una función. La afirmación de que temperatura, resistencia o población satisfacen efectivamente esos coeficientes requiere observaciones externas a las premisas del teorema. $\square$

## 11.7. Contraejemplos: el mapa de las fronteras

Una hipótesis puede parecer accesoria hasta que encontramos un ejemplo que la necesita. La continuidad, la acotación o la existencia de muchas derivadas ofrecen información valiosa, pero cada una deja abiertas preguntas distintas. Los contraejemplos que hemos visto permiten reconocer esas diferencias antes de intentar una operación que el teorema no autoriza.

**Proposición 11.4 (fronteras de la inferencia; `EDC-C11-PRP-004`).** Son falsas, sin hipótesis adicionales, las implicaciones «continua $\Rightarrow$ derivable», «acotada $\Rightarrow$ integrable», «$a_n\to0\Rightarrow\sum a_n$ convergente», «$C^\infty\Rightarrow$ analítica» y «campo continuo de EDO $\Rightarrow$ unicidad del PVI».

**Demostración.** La función $|x|$ es continua y no derivable en cero (C01). La indicadora de $\mathbb Q\cap[0,1]$ es acotada y no integrable por Darboux, pues en cada subintervalo el ínfimo es cero y el supremo uno (C05). La serie $\sum_{n=1}^{\infty}1/n$ diverge por bloques aunque $1/n\to0$ (C08). La función plana de §11.5 es $C^\infty$ y no analítica en cero (C09). La ecuación $y'=\sqrt{|y|}$ tiene infinitas soluciones para el mismo dato (C10). Cada contraejemplo niega exactamente la implicación correspondiente. $\square$

**Lema 11.1 (una discontinuidad no destruye siempre la integral; `EDC-C11-LEM-001`).** Sea $f:[a,b]\to\mathbb R$ la función que vale cero salvo en un único punto $c\in[a,b]$, donde vale $d$. Entonces $f$ es Riemann–Darboux integrable y su integral es cero.

**Demostración.** Si el segmento es degenerado, su integral es cero por la convención de C05. Supongamos $a<b$. Si $d=0$, la función es nula. Para $d\ne0$, fijemos $\varepsilon>0$ y rodeemos el punto $c$ con subintervalos cuya longitud total sea menor que $\varepsilon/|d|$. Si $c$ es interior, podemos incluirlo como punto de la partición y elegir un vecino próximo a cada lado; como los subintervalos son cerrados, ambos adyacentes contienen el valor excepcional. Si $c$ es un extremo, basta un vecino interior próximo.

Fuera de esos subintervalos la función es cero. En los afectados, el ínfimo y el supremo están entre $\min(0,d)$ y $\max(0,d)$, de modo que la oscilación es a lo sumo $|d|$. Al multiplicar por sus longitudes y sumar, obtenemos $U(f,P)-L(f,P)<\varepsilon$. El criterio de Darboux de C05 prueba integrabilidad.

Las mismas particiones sitúan las sumas inferior y superior entre $-|d|$ y $|d|$ multiplicados por la longitud afectada. La integral queda entre esas sumas. Como la longitud puede hacerse arbitrariamente pequeña, su módulo debe ser cero. El signo de $d$ no cambia el argumento. $\square$

La función tiene una discontinuidad cuando $d\ne0$, pero podemos encerrar su contribución a las sumas en un intervalo tan corto como queramos. En la indicadora de los racionales, por el contrario, cada subintervalo contiene ambos valores y el refinamiento no reduce la diferencia de sumas. La localización de la variación importa para la integral. Un criterio general mediante la medida del conjunto de discontinuidades exige herramientas que quedan fuera de este volumen.

## 11.8. Geometrías de aproximación antes del cálculo moderno

En el segmento parabólico de C04, cada etapa de la construcción geométrica añade triángulos y deja regiones menores por cubrir. Arquímedes estudió esa cuadratura dentro de la geometría de su tiempo; los métodos de agotamiento asociados a Eudoxo y usados en sus obras comparaban áreas y volúmenes con figuras conocidas. El resultado $4T/3$ conserva el interés de aquella pregunta. La prueba por sumas finitas y restos de C04 nos permitió reconstruirla con herramientas actuales y preparar la construcción de la integral.

Los comentarios de Liu Hui a los *Nueve capítulos sobre el arte matemático*, fechados convencionalmente en el siglo III, ofrecen otra ocasión para estudiar cómo una figura puede refinarse para obtener información sobre áreas y volúmenes. La subdivisión permite comparar lo conocido con lo que aún se busca. Ese parecido matemático hace interesante leer ambos contextos, aunque no establece por sí mismo una transmisión entre las tradiciones griega y china ni les adjudica una definición común de integral.

En Kerala, al sur de la India, la historia de las series presenta además una dificultad textual. Resultados trigonométricos atribuidos a Madhava, de fines del siglo XIV y comienzos del XV, se conocen mediante obras posteriores de su escuela. Al expresarlos en nuestra notación reconocemos identidades relacionadas con las que hemos estudiado para la arctangente y otras funciones. Para comprender cómo se obtenían y justificaban, necesitamos atender a los textos transmitidos y a las explicaciones de los autores posteriores, en lugar de tomar una fórmula moderna como reproducción de un manuscrito de Madhava.

La acumulación y el refinamiento de aproximaciones dieron lugar a investigaciones en tradiciones distintas. Comparar sus problemas permite ampliar la lectura del cálculo; establecer relaciones históricas entre ellas requiere examinar testimonios y cronologías. Las [las notas históricas H1–H3](capitulo-11-notas.html) registran las fuentes de estas aproximaciones y el alcance documental de la comparación.

## 11.9. La síntesis moderna: tangente, cuadratura y movimiento

Los siglos XVI y XVII intensificaron la investigación de tangentes, máximos, indivisibles, áreas, movimiento y problemas inversos. En la historiografía consultada aparecen Fermat, Cavalieri, Torricelli, Barrow, Newton y Leibniz como participantes de tradiciones que se superponen pero no se reducen a una formulación unitaria previa.

Newton organizó parte de su trabajo en torno a magnitudes que *fluyen* y sus tasas, denominadas *fluxiones*. Leibniz elaboró una notación diferencial e integral con fuerte orientación operatoria. La relación inversa entre derivar y acumular figura en ambas genealogías, pero nuestra demostración del Teorema Fundamental para funciones continuas sobre un intervalo real es una **reformulación contemporánea**. No debemos adjudicar a ninguno de estos matemáticos la formulación literal en términos de $\sup_PL$, $\inf_PU$ o $\varepsilon$–$\delta$.

Los manuscritos, la circulación entre matemáticos, la publicación y la adopción de una notación corresponden a momentos distintos de esa historia. La controversia entre Newton y Leibniz ha sido estudiada desde esas diferencias, y el nombre de Taylor reúne también procedimientos de expansión con antecedentes diversos. Para seguir el razonamiento de este libro, la relación decisiva es la que demostramos entre derivar y acumular: el Teorema Fundamental enlaza los problemas aun cuando su historia no se reduzca a una sola fecha o a una sola forma de escritura.

::: {.callout-note appearance="simple" icon="false" collapse="false" title="Historia — Hasta dónde llega una fórmula"}
*Lectura opcional.*

En la introducción del *Cours d’analyse* de 1821, Cauchy cuenta una dificultad que acompaña al uso de fórmulas: podemos atribuirles un alcance mayor del que realmente tienen. Propone precisar las condiciones y los valores para los que una relación es válida, y explica que antes de sumar series ha tenido que estudiar su convergencia.

La serie geométrica permite reconocer el problema con una cuenta familiar. Dentro de $|x|<1$, su suma es $(1-x)^{-1}$. En $x=-1$, la expresión racional todavía tiene valor, pero las sumas parciales de la serie oscilan. Escribir la fórmula correctamente exige recordar el intervalo donde hemos probado la igualdad.

Los problemas de cuadratura, tangencia y movimiento habían impulsado la búsqueda de métodos capaces de pasar de un cálculo particular a muchos otros. Esa capacidad abre preguntas nuevas sobre su alcance: qué funciones podemos derivar, cuándo podemos acumularlas y qué conserva un límite. Las pruebas y los contraejemplos de este capítulo permiten explorar esas preguntas con las herramientas que hemos construido.

**Para seguir leyendo:** Notas históricas del capítulo 11, apartados H1–H8.
:::

## 11.10. El rigor del siglo XIX no consistió en cambiar nombres

Con Cauchy, en particular en el *Cours d'analyse* de 1821, la exposición de límites, continuidad y series adquiere un programa explícito de control de condiciones. El uso de infinitésimos y límites en su obra debe leerse históricamente y no identificarse sin reservas con nuestra formalización de sucesiones, cuantificadores y intervalos. Incluso formulaciones prestigiosas podían contener errores cuando se transferían propiedades desde sucesiones de funciones a sus límites sin el control requerido.

La teoría moderna de integración distingue el papel de las sumas de Riemann y la presentación por sumas superior e inferior de Darboux. El artículo de Gaston Darboux, «Mémoire sur les fonctions discontinues» (1875), constituye un hito bibliográfico verificable. El criterio de C05 es nuestro teorema moderno en $[a,b]$; no es una transcripción del francés original. El surgimiento del análisis del siglo XIX también amplió notablemente los problemas de continuidad, diferenciabilidad, aproximación y convergencia.

**Lema 11.2 (una distinción entre límite puntual y cota común; `EDC-C11-LEM-002`).** En $[0,1]$, la sucesión $f_n(x)=x^n$ converge puntualmente a la función $f$ dada por $f(x)=0$ si $0\le x<1$ y $f(1)=1$, pero no admite aproximación con un error $\varepsilon_n\to0$ válido para **todos** los $x\in[0,1]$.

**Demostración.** Para un $x$ fijo con $0\le x<1$, la sucesión geométrica $x^n$ tiende a cero; en $x=1$, todos sus valores son uno. Ése es el límite puntual anunciado. Para cada $n\ge1$, el error en $x<1$ vale $x^n$, mientras en $x=1$ es cero. Aunque cada uno de los valores con $x<1$ es menor que uno, podemos hacerlos tan próximos a uno como queramos eligiendo $x$ suficientemente próximo a uno. El supremo del error sobre todo el segmento es, por tanto, uno para cada $n$.

Si existiese una cota $\varepsilon_n$ válida para todos los puntos, tendría que dominar ese supremo y cumplir $\varepsilon_n\ge1$. Esto contradice $\varepsilon_n\to0$. La ausencia de una cota común no impide el límite en cada punto fijo; muestra que el punto donde el error sigue siendo grande puede cambiar con $n$. $\square$

En un segmento $[0,r]$ con $r<1$, el mismo error queda acotado por $r^n$, que sí tiende a cero para todos los puntos a la vez. Al incluir valores arbitrariamente próximos a uno perdemos ese control. En C08 trabajamos de modo semejante con segmentos estrictamente interiores al radio de una serie de potencias, escogiendo una distancia intermedia para obtener una cota de colas común. El ejemplo permite entender la necesidad de esa elección sin desarrollar todavía una teoría general de convergencia uniforme.

## 11.11. El umbral del análisis real: problemas legítimamente abiertos

El cálculo elemental que hemos construido descansa en la completitud de $\mathbb R$ (C00) y en condiciones precisas. Queda fuera de su alcance demostrar el criterio general de integrabilidad de una función acotada mediante conjuntos de discontinuidad de medida nula; exigiría herramientas de medida. Queda asimismo pendiente desarrollar la convergencia uniforme para familias arbitrarias de funciones, intercambios generales de límites y derivadas, integración impropia, funciones de varias variables y espacios métricos generales.

Para EDO, C10 resolvió explícitamente clases lineales y ciertas ecuaciones separables, y estableció un principio de unicidad bajo Lipschitz para soluciones preexistentes. No probó la existencia general de soluciones bajo hipótesis Lipschitz ni su continuación máxima en sistemas. Para algoritmos, sólo demostró el error **local** de un paso de Euler, no un teorema global de convergencia numérica.

**Proposición 11.5 (lo que el error local no dice; `EDC-C11-PRP-005`).** Una cota $|y(t+h)-[y(t)+hF(t,y(t))]|\le Mh^2/2$ válida para cada paso que comienza en el valor **exacto** no contiene, por sí misma, una cota para el error después de $N$ pasos de Euler que comienzan en los valores **aproximados**.

**Justificación.** El segundo paso numérico utiliza $Y_1$ en lugar de $y(t_1)$. La hipótesis del lema local se aplica a $F(t_1,y(t_1))$, no controla la diferencia $F(t_1,Y_1)-F(t_1,y(t_1))$. Para acotar ésta hay que imponer y emplear una regularidad en la segunda variable, y luego propagar recursivamente los errores. Esa premisa y ese argumento son adicionales; no están contenidos en el mero resto de Taylor de un paso. $\square$

## 11.12. La unidad alcanzada y el trabajo de lectura

Podemos reunir las conexiones demostradas a lo largo del libro junto con las condiciones que han marcado su alcance:

| Pregunta | Construcción | Resultado y límite probado |
|---|---|---|
| ¿Cómo cambia una función cerca de un punto? | Cociente incremental | Derivada interior y aproximación afín (C01–C02); no toda función continua es derivable |
| ¿Qué dice su tasa sobre todo un intervalo? | Valor medio y cotas | Monotonía, extremos y variaciones controladas (C03) |
| ¿Qué significa acumular? | Agotamiento, particiones y sumas | Integral de Riemann–Darboux (C04–C05); no toda función acotada es integrable |
| ¿Cómo regresamos de una tasa a un valor? | Dos partes del Teorema Fundamental | Reconstrucción por acumulación y primitivas bajo hipótesis (C06–C07) |
| ¿Cuándo representa una suma infinita a una función? | Series y control interior | Radio, colas y operaciones justificadas (C08); fronteras independientes |
| ¿Cuándo aproxima Taylor de verdad? | Polinomio y resto | Resto finito demostrado; representación cuando $R_n\to0$ (C09) |
| ¿Puede una ley determinar una trayectoria? | EDO, dato inicial, integración y unicidad | Clases explícitas; unicidad condicional, excepciones y dominio (C10) |

Cada paso de este recorrido hace posible una nueva pregunta. La derivada describe un cambio local; el valor medio lo extiende a una comparación entre puntos; la integral acumula una tasa, y el Teorema Fundamental permite recuperar la función. Las series y los restos introducen aproximaciones que podemos controlar, mientras las ecuaciones diferenciales muestran cómo una relación de cambio puede determinar una trayectoria. La unidad del cálculo vive en esas relaciones demostradas.

Los [treinta ejercicios de síntesis](capitulo-11-ejercicios.html) y sus [treinta soluciones separadas](capitulo-11-soluciones.html) vuelven sobre los puntos donde una inferencia puede perder su justificación: el dominio de una fórmula, la condición que permite derivarla o integrarla, el límite que debe alcanzarse y el dato que selecciona una función. Las [notas H1–H9](capitulo-11-notas.html) acompañan el recorrido histórico con sus fuentes y límites de lectura. La auditoría transversal posterior revisará la coherencia editorial de los doce capítulos como conjunto.

### Dependencias y límites editoriales

- **Resultados usados:** C00–C10, en particular C03 (valor medio), C05 (Darboux), C06 (Teorema Fundamental), C08 (series), C09 (Taylor) y C10 (EDO).
- **Aportaciones demostradas de C11:** cinco teoremas `EDC-C11-THM-001--005`, cinco proposiciones `PRP-001--005`, dos lemas `LEM-001--002`, dos corolarios `COR-001--002` y una definición `DEF-001`.
- **Resultados no reivindicados:** teoría de medida, convergencia uniforme general, Picard–Lindelöf completo, integración de Lebesgue, EDP, cálculo multivariable y análisis funcional.
- **Frontera editorial:** el cierre sustantivo de C11 no equivale por sí solo a auditoría transversal completa, edición web ni pruebas tipográficas de un volumen integral.
