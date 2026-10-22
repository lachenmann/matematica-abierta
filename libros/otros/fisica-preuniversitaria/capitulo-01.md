---
title: "1. Medici�n, magnitudes, dimensiones y modelos f�sicos"
status: published
draft: false
author: A. Pe�a
date-modified: '2026-10-21'
license: GFDL-1.3-or-later
areas:
  - fisica-matematica
level: introductorio
topics:
  - fisica-preuniversitaria
  - modelizacion
provenance:
  type: original
  sources:
    - role: idea
      note: 'Obra original de Matem�tica Abierta; fuentes bibliogr�ficas identificadas en cada cap�tulo.'
number-sections: false
content-id: MA-BCH-0396
content-type: book-chapter
book-id: MA-BOK-0016
source-id: FP-C01
---

[�ndice del libro](index.html) � [Cap�tulo siguiente ](capitulo-02.html)

Un problema de f�sica comienza cuando observamos una situaci�n y decidimos qu� queremos averiguar. Pensemos en una pregunta aparentemente sencilla: �cu�nto tarda la luz del Sol en llegar a la Tierra? Podemos responder combinando dos datos: la distancia entre ambos astros y la rapidez de la luz en el vac�o. Una relaci�n entre distancia y tiempo convierte esos datos en una predicci�n. El primer acto f�sico consiste en reconocer qu� magnitudes intervienen y por qu� una relaci�n entre ellas resulta apropiada.

En las p�ginas siguientes aprenderemos a construir esa relaci�n con cuidado. Tambi�n veremos que una f�rmula correcta puede dar una respuesta equivocada si usamos unidades incompatibles, si interpretamos mal los datos o si olvidamos las condiciones del modelo. La comprobaci�n forma parte de la resoluci�n de un problema.

### Pregunta de partida

�C�mo decidimos si una medici�n es suficiente para responder una pregunta f�sica? El n�mero, la unidad, la incertidumbre y el modelo deben leerse juntos.

## De la descripci�n a la explicaci�n

Cuando una persona dice que un veh�culo �va r�pido�, comunica una impresi�n �til en la vida cotidiana. Para calcular cu�ndo llegar� a una ciudad necesitamos una descripci�n cuantitativa del movimiento. Para hacerlo tendremos que especificar una distancia y un tiempo, o una rapidez. Algo similar ocurre con expresiones como �el agua est� caliente� o �el objeto pesa mucho�. La f�sica necesita distinguir la impresi�n cualitativa de la magnitud que podemos comparar y medir.

Usaremos potencias de diez para escribir n�meros grandes o peque�os: $10^3=1000$ y $10^{-2}=1/100=0{,}01$. Una escritura como $3\times10^4$ significa $30\,000$; en cambio, $3\times10^{-4}=0{,}0003$. Al multiplicar potencias de la misma base sumamos exponentes: $10^3\times10^{-2}=10^{3-2}=10$. La potencia afecta tambi�n a las unidades: $\,\mathrm{cm^2}$ es la unidad de �rea de un cuadrado de un cent�metro de lado, mientras que $\,\mathrm{cm^3}$ mide el volumen de un cubo de ese lado.

Una *magnitud f�sica* es una propiedad a la que podemos asignar valores mediante un procedimiento de medici�n o una definici�n operativa adecuada. La longitud, el tiempo, la masa y la temperatura son ejemplos. El resultado de una medida combina un n�mero y una unidad: escribir �la mesa mide 1,2� deja una informaci�n esencial sin indicar; escribir $1{,}2\,\mathrm{m}$ tiene significado f�sico.

Al escoger otra unidad cambia el n�mero que expresa la misma longitud:
$$
1{,}2\,\mathrm{m}=120\,\mathrm{cm}.
$$
Ambas expresiones describen la longitud de la misma mesa. Hemos expresado una misma magnitud de dos maneras.

![Apoyo visual: De la descripci�n a la explicaci�n.](../../../assets/books/fisica-preuniversitaria/figuras/AV-EJ-1-01.svg){#fig-fp-av-ej-1-01 fig-alt="Ilustraci�n de De la descripci�n a la explicaci�n. Al escoger otra unidad cambia el n�mero que expresa la misma longitud: 1,2\\,m=120\\,cm. Ambas expresiones describen la longitud de la misma mesa. Hemos expresado una misma magnitud de dos maneras."}

Una magnitud *escalar* se describe mediante un valor en una escala y su unidad cuando corresponde; ese valor se conserva al cambiar la orientaci�n de los ejes espaciales. La temperatura en grados Celsius, la carga el�ctrica y el trabajo proporcionan ejemplos de valores positivos, cero o negativos seg�n la situaci�n. Los desplazamientos, las velocidades y las fuerzas incorporan adem�s informaci�n direccional, que desarrollaremos mediante vectores en el cap�tulo 2.

## Las unidades revelan la estructura de las relaciones

Trabajaremos principalmente con el Sistema Internacional de Unidades (SI). Tres unidades nos acompa�ar�n desde el comienzo: el metro ($\,\mathrm{m}$), el segundo ($\,\mathrm{s}$) y el kilogramo ($\,\mathrm{kg}$). Otras magnitudes usan combinaciones de estas unidades. Una rapidez, por ejemplo, puede medirse en metros por segundo, $\,\mathrm{m/s}$; una aceleraci�n, en $\,\mathrm{m/s^2}$.

La *dimensi�n* expresa c�mo una magnitud depende de magnitudes b�sicas, como longitud, masa y tiempo. Para representarla combinamos sus s�mbolos mediante potencias: una rapidez tiene dimensi�n $L/T$ y una aceleraci�n, $L/T^2$. La unidad establece la referencia con que expresamos su valor. Una longitud conserva su dimensi�n $L$ al expresarse en metros o cent�metros; un tiempo conserva su dimensi�n $T$ al expresarse en segundos u horas.

Toda igualdad f�sica entre cantidades de la misma naturaleza debe ser *dimensionalmente homog�nea*. Esto significa que ambos lados de una ecuaci�n deben tener la misma dimensi�n, y que los t�rminos que se suman deben ser compatibles. La suma $3\,\mathrm{m}+4\,\mathrm{s}$ re�ne magnitudes de dimensiones distintas y carece de significado como longitud.

La homogeneidad dimensional permite detectar muchos errores; la validez f�sica de una ecuaci�n requiere adem�s examinar el modelo y contrastar sus predicciones. La relaci�n $d=vt$ posee las dimensiones de una distancia; la expresi�n $d=2vt$ tambi�n. La elecci�n entre ellas requiere informaci�n f�sica sobre la situaci�n particular. Para eso necesitamos comprender el movimiento.

### Problema resuelto 1.1 � Una rapidez expresada en dos sistemas de unidades {#r1-1}

Un autom�vil se desplaza con una rapidez constante de $72\,\mathrm{km/h}$. Expresar esa rapidez en $\,\mathrm{m/s}$ y calcular cu�ntos metros recorre en $15\,\mathrm{s}$.

*Resoluci�n.* Lo que queremos convertir es una raz�n entre longitud y tiempo. Un kil�metro equivale a mil metros y una hora a $3600\,\mathrm{s}$. Por tanto,
$$
72\frac{\,\mathrm{km}}{\,\mathrm{h}}
=72\frac{1000\,\mathrm{m}}{3600\,\mathrm{s}}
=20\,\mathrm{m/s}.
$$
Ahora s� podemos multiplicar por un tiempo expresado en segundos:
$$
d=vt=(20\,\mathrm{m/s})(15\,\mathrm{s})=300\,\mathrm{m}.
$$
La unidad segundo se cancela, como debe ocurrir si el resultado es una longitud. Una comprobaci�n mental adicional: a $20\,\mathrm{m/s}$ el autom�vil recorre $200\,\mathrm{m}$ en diez segundos y $100\,\mathrm{m}$ en otros cinco. La respuesta $300\,\mathrm{m}$ es coherente.

![Apoyo visual: Problema resuelto 1.1 � Una rapidez expresada en dos sistemas de unidades.](../../../assets/books/fisica-preuniversitaria/figuras/AV-R1-1.svg){#fig-fp-av-r1-1 fig-alt="Ilustraci�n de Problema resuelto 1.1 � Una rapidez expresada en dos sistemas de unidades. Resoluci�n. Lo que queremos convertir es una raz�n entre longitud y tiempo. Un kil�metro equivale a mil metros y una hora a 3600\\,s. Por tanto, 72frac\\,km\\,h =72frac1000\\,m3600\\,s =20\\,m/s. Ahora s� podemos multiplicar por un tiempo expresado en segundos: d=vt=(20\\,m/s)(15\\,s)=300\\,m. La unidad segundo se cancela,"}

## La medida y su incertidumbre

Medir es comparar una propiedad con un patr�n por medio de un procedimiento concreto. Si apoyamos una regla sobre una mesa, necesitamos decidir d�nde empieza y termina la longitud, c�mo alineamos el instrumento y qu� graduaci�n puede distinguirse. La resoluci�n del instrumento y el procedimiento empleado limitan las cifras que podemos informar. Por eso una cifra como $1{,}247391\,\mathrm{m}$ puede atribuir al instrumento una precisi�n excesiva; $1{,}25\,\mathrm{m}$ puede comunicar mejor el alcance de la medici�n.

La *resoluci�n* indica el menor incremento que el instrumento distingue o muestra. La *precisi�n* describe la proximidad de resultados obtenidos al repetir una operaci�n en condiciones especificadas; una colecci�n de valores puede ser muy semejante internamente y estar desplazada respecto de un valor de referencia. La *exactitud* se refiere a cu�n pr�ximo est� un resultado a un valor de referencia aceptado. Un efecto sistem�tico puede desplazar los resultados de manera constante o predecible al repetir la medici�n. El *sesgo* es una estimaci�n del error sistem�tico, obtenida mediante una comparaci�n apropiada con una referencia. Para juzgar la exactitud de una serie con poca dispersi�n necesitamos contrastarla con un patr�n adecuado.

La incertidumbre expresa el margen de conocimiento asociado a la medici�n. Es una forma expl�cita de comunicar qu� variaci�n de resultados resulta compatible con los datos y con el m�todo utilizado. Las fuentes de incertidumbre pueden ser la calibraci�n, la lectura, las condiciones ambientales, la variabilidad del objeto y el procedimiento. La mitad de una divisi�n de una regla *puede* proporcionar una estimaci�n de lectura bajo condiciones apropiadas; las dem�s fuentes de incertidumbre requieren una evaluaci�n propia.

### Problema resuelto 1.2 � Precisi�n de una serie y exactitud de sus resultados {#r1-2}

Dos equipos miden repetidamente una longitud cuyo valor de referencia es $2{,}00\,\mathrm{m}$. El equipo A obtiene $2{,}01$, $2{,}02$ y $2{,}01\,\mathrm{m}$; el B, $2{,}11$, $2{,}12$ y $2{,}11\,\mathrm{m}$. �Cu�l es m�s exacto? �Se distingue claramente cu�l es m�s preciso solo con estos datos?

*Resoluci�n.* Las tres lecturas del equipo A est�n mucho m�s cerca de $2{,}00\,\mathrm{m}$, por lo que sus resultados son m�s *exactos* respecto de ese valor de referencia. En cambio, la dispersi�n observable en ambos equipos es la misma: cada serie abarca $0{,}01\,\mathrm{m}$ entre sus extremos. Los datos muestran una precisi�n repetitiva semejante en ambos grupos. Podr�a existir un error sistem�tico en el equipo B. Para identificar la causa de esa diferencia -por ejemplo, una mala calibraci�n o un desplazamiento del cero- necesitamos informaci�n adicional sobre el procedimiento.

![Apoyo visual: Problema resuelto 1.2 � Precisi�n de una serie y exactitud de sus resultados.](../../../assets/books/fisica-preuniversitaria/figuras/AV-R1-4.svg){#fig-fp-av-r1-4 fig-alt="Ilustraci�n de Problema resuelto 1.2 � Precisi�n de una serie y exactitud de sus resultados. Resoluci�n. Las tres lecturas del equipo A est�n mucho m�s cerca de 2,00\\,m, por lo que sus resultados son m�s exactos respecto de ese valor de referencia. En cambio, la dispersi�n observable en ambos equipos es la misma: cada serie abarca 0,01\\,m entre sus extremos. Los datos muestran una precisi�n repetitiva"}

### Una medici�n repetida

Mide cinco veces la longitud de un l�piz utilizando una regla graduada en mil�metros. Anota todas las lecturas, la resoluci�n del instrumento y la diferencia entre los valores extremos. Compara esa dispersi�n con la resoluci�n de la regla: �qu� informaci�n aporta cada una? Si las cinco lecturas coinciden, �puedes asegurar que la medici�n es exacta?

## C�mo comunicar el resultado y su incertidumbre

Cuando interpretamos un dato $L=(12{,}34\pm0{,}05)\,\mathrm{cm}$ como un intervalo acotado, estamos comunicando que la longitud se encuentra, seg�n el procedimiento y la interpretaci�n adoptada, entre $12{,}29\,\mathrm{cm}$ y $12{,}39\,\mathrm{cm}$. El s�mbolo $\pm$ solo es �til si decimos qu� representa el margen: una cota instrumental, una desviaci�n estad�stica, una incertidumbre expandida u otra convenci�n. En este cap�tulo emplearemos, salvo indicaci�n contraria, *cotas m�ximas de un intervalo compatible*.

![Apoyo visual: C�mo comunicar el resultado y su incertidumbre.](../../../assets/books/fisica-preuniversitaria/figuras/AV-EJ-1-02.svg){#fig-fp-av-ej-1-02 fig-alt="Ilustraci�n de C�mo comunicar el resultado y su incertidumbre. Cuando interpretamos un dato L=(12,34pm0,05)\\,cm como un intervalo acotado, estamos comunicando que la longitud se encuentra, seg�n el procedimiento y la interpretaci�n adoptada, entre 12,29\\,cm y 12,39\\,cm. El s�mbolo pm solo es �til si decimos qu� representa el margen: una cota instrumental, una desviaci�n"}

La escritura $L\in[a,b]$ abrevia $a\leq L\leq b$: ambos extremos est�n incluidos. En $d/t$, mantener $t>0$ y aumentar $d$ aumenta el resultado; mantener $d>0$ y aumentar $t$ lo disminuye. Por ejemplo, recorrer la misma distancia en m�s tiempo reduce la rapidez media. Esta comparaci�n explica qu� extremos debemos elegir para construir las cotas del cociente.

Para sumar dos longitudes positivas con cotas $L_1\in[a_1,b_1]$ y $L_2\in[a_2,b_2]$, el total estar� entre $a_1+a_2$ y $b_1+b_2$. Si los extremos tienen el mismo origen sistem�tico, debemos conservar esa contribuci�n com�n al evaluar los m�rgenes. Para dividir longitudes o tiempos *positivos* acotados, obtenemos cotas seguras tomando los extremos que hacen m�nimo y m�ximo el cociente. En problemas de mayor nivel aprenderemos otros tratamientos estad�sticos, que requieren hip�tesis adicionales.

### Problema resuelto 1.3 � Una rapidez media con datos acotados {#r1-3}

Un corredor recorre una distancia entre $9{,}9\,\mathrm{m}$ y $10{,}1\,\mathrm{m}$ en un tiempo entre $1{,}9\,\mathrm{s}$ y $2{,}1\,\mathrm{s}$. Encontrar la rapidez media central y un intervalo conservador compatible con estos datos.

*Resoluci�n.* El modelo central, usando $10{,}0\,\mathrm{m}$ y $2{,}0\,\mathrm{s}$, da $5{,}0\,\mathrm{m/s}$. Como las cantidades son positivas, el cociente m�s peque�o se produce con la menor distancia y el mayor tiempo, mientras que el m�ximo procede del extremo opuesto:
$$
\frac{9{,}9\,\mathrm{m}}{2{,}1\,\mathrm{s}}\leq v_{\mathrm{media}}\leq
\frac{10{,}1\,\mathrm{m}}{1{,}9\,\mathrm{s}},
\qquad
4{,}71\,\mathrm{m/s}\lesssim v_{\mathrm{media}}\lesssim5{,}32\,\mathrm{m/s}.
$$
Informar $v=5{,}000000\,\mathrm{m/s}$ atribuir�a a la medici�n m�s cifras de las que respalda el procedimiento. Asignar una probabilidad al intervalo requerir�a adem�s una distribuci�n estad�stica. La incertidumbre pertenece a nuestra informaci�n sobre la rapidez media, cuya definici�n f�sica permanece fija.

![Apoyo visual: Problema resuelto 1.3 � Una rapidez media con datos acotados.](../../../assets/books/fisica-preuniversitaria/figuras/AV-R1-5.svg){#fig-fp-av-r1-5 fig-alt="Ilustraci�n de Problema resuelto 1.3 � Una rapidez media con datos acotados. Resoluci�n. El modelo central, usando 10,0\\,m y 2,0\\,s, da 5,0\\,m/s. Como las cantidades son positivas, el cociente m�s peque�o se produce con la menor distancia y el mayor tiempo, mientras que el m�ximo procede del extremo opuesto: frac9,9\\,m2,1\\,sleq vmedialeq frac10,1\\,m1,9\\,s, qquad 4,71\\,m/slesssim"}

Una regla pr�ctica de comunicaci�n consiste en redondear primero la incertidumbre a una o dos cifras significativas seg�n el caso y presentar el valor central en la misma posici�n decimal. As�, si una evaluaci�n justific� $12{,}34\pm0{,}05\,\mathrm{cm}$, esos dos n�meros se leen juntos. Los ceros finales pueden transmitir resoluci�n: $2{,}50\,\mathrm{m}$ puede comunicar una resoluci�n distinta de $2{,}5\,\mathrm{m}$. Conservamos las cifras que sustenta el procedimiento.

### Problema resuelto 1.4 � Densidad estimada y l�mites de dos mediciones {#r1-4}

La masa de una muestra homog�nea se informa como $(20{,}0\pm0{,}2)\,\mathrm{g}$ y su volumen como $(8{,}0\pm0{,}1)\,\mathrm{cm^3}$, interpretando los m�rgenes como cotas. Estimar la densidad y dar un intervalo de valores compatibles.

*Resoluci�n.* La densidad central es $\rho=m/V=2{,}50\,\mathrm{g/cm^3}$. Como $m$ y $V$ son positivos, sus extremos proporcionan
$$
\frac{19{,}8\,\mathrm{g}}{8{,}1\,\mathrm{cm^3}}\leq\rho\leq
\frac{20{,}2\,\mathrm{g}}{7{,}9\,\mathrm{cm^3}},
\qquad
2{,}44\,\mathrm{g/cm^3}\lesssim\rho\lesssim2{,}56\,\mathrm{g/cm^3}.
$$
El resultado central $2{,}50\,\mathrm{g/cm^3}$ puede acompa�arse de estos l�mites. Si deseamos un solo margen sim�trico conservador, $\rho\approx(2{,}50\pm0{,}06)\,\mathrm{g/cm^3}$ resume el intervalo con el redondeo indicado. Estas cotas proceden de los extremos compatibles; calcular una desviaci�n est�ndar o emplear una propagaci�n estad�stica requerir�a otras hip�tesis.

![Apoyo visual: Problema resuelto 1.4 � Densidad estimada y l�mites de dos mediciones.](../../../assets/books/fisica-preuniversitaria/figuras/AV-R1-6.svg){#fig-fp-av-r1-6 fig-alt="Ilustraci�n de Problema resuelto 1.4 � Densidad estimada y l�mites de dos mediciones. Resoluci�n. La densidad central es rho=m/V=2,50\\,g/cm^3. Como m y V son positivos, sus extremos proporcionan frac19,8\\,g8,1\\,cm^3leqrholeq frac20,2\\,g7,9\\,cm^3, qquad 2,44\\,g/cm^3lesssimrholesssim2,56\\,g/cm^3. El resultado central 2,50\\,g/cm^3 puede acompa�arse de estos l�mites. Si deseamos un solo margen sim�trico"}

## Medir exige tambi�n saber cu�ndo falta informaci�n

En una recta elegimos un origen y un sentido positivo. El *desplazamiento* es la posici�n final menos la inicial; la *velocidad media* es ese desplazamiento dividido por el tiempo transcurrido. La *rapidez media* relaciona la longitud del recorrido completo con el mismo tiempo. Si conocemos las posiciones inicial y final de un autom�vil y la duraci�n del viaje, podemos calcular su velocidad media; para reconstruir las posiciones intermedias necesitamos m�s informaci�n. Dos evoluciones muy distintas pueden tener los mismos extremos. Reconocer una *pregunta subdeterminada* consiste en identificar qu� datos faltan para decidir entre las respuestas compatibles.

### Problema resuelto 1.5 � Movimientos distintos entre los mismos extremos {#r1-5}

Se observa un veh�culo en $x=0$ cuando $t=0$ y en $x=30\,\mathrm{m}$ cuando $t=10\,\mathrm{s}$. �Podemos asegurar que viaj� siempre a $3\,\mathrm{m/s}$?

*Resoluci�n.* Sabemos que la velocidad media fue $30\,\mathrm{m}/10\,\mathrm{s}=3\,\mathrm{m/s}$, pero son compatibles, por ejemplo, dos modelos distintos:
$$
x_A(t)=(3\,\mathrm{m/s})t,\qquad
x_B(t)=(0{,}3\,\mathrm{m/s^2})t^2,\quad 0\leq t\leq10\,\mathrm{s}.
$$
Ambos comienzan en $0$ y terminan en $30\,\mathrm{m}$. En el primero la velocidad es constante; en el segundo aumenta con el tiempo. Una medici�n adicional en un instante intermedio permitir�a distinguir estos modelos concretos, pero ni siquiera un n�mero finito de posiciones determina, sin hip�tesis suplementarias, una funci�n de movimiento �nica para todos los instantes.

![Apoyo visual: Problema resuelto 1.5 � Movimientos distintos entre los mismos extremos.](../../../assets/books/fisica-preuniversitaria/figuras/AV-R1-7.svg){#fig-fp-av-r1-7 fig-alt="Ilustraci�n de Problema resuelto 1.5 � Movimientos distintos entre los mismos extremos. Resoluci�n. Sabemos que la velocidad media fue 30\\,m/10\\,s=3\\,m/s, pero son compatibles, por ejemplo, dos modelos distintos: xA(t)=(3\\,m/s)t,qquad xB(t)=(0,3\\,m/s^2)t^2,quad 0leq tleq10\\,s. Ambos comienzan en 0 y terminan en 30\\,m. En el primero la velocidad es constante; en el segundo aumenta con el tiempo. Una"}

Una estimaci�n de Fermi descompone una cantidad dif�cil de medir en factores sencillos y declara los supuestos que permiten estimar su escala. Con pocas mediciones podemos obtener as� una orientaci�n cuantitativa y reconocer qu� datos mejorar�an la respuesta.

### Problema resuelto 1.6 � Una estimaci�n de Fermi: latidos a lo largo de una vida {#r1-6}

Estimar cu�ntos latidos realiza un coraz�n humano durante una vida de $80$ a�os, suponiendo a efectos de la estimaci�n una frecuencia media de $70$ latidos por minuto. El resultado ser� una estimaci�n de escala basada en los supuestos elegidos.

*Resoluci�n.* Multiplicamos factores correspondientes al mismo per�odo:
$$
\begin{aligned}
N&\approx70\frac{\text{latidos}}{\,\mathrm{min}}\,
60\frac{\,\mathrm{min}}{\,\mathrm{h}}\,
24\frac{\,\mathrm{h}}{\text{d�a}}\\
&\quad\times365\frac{\text{d�as}}{\text{a�o}}\,
80\text{ a�os}\approx2{,}9\times10^{9}\text{ latidos}.
\end{aligned}
$$
La estimaci�n vale del orden de unos pocos miles de millones. La estimaci�n mantiene fijos los factores elegidos y deja fuera variaciones diarias, edad, salud y cambios vitales; muestra c�mo abordar una pregunta de escala enorme descomponi�ndola en factores comprensibles.

![Apoyo visual: Problema resuelto 1.6 � Una estimaci�n de Fermi: latidos a lo largo de una vida.](../../../assets/books/fisica-preuniversitaria/figuras/AV-R1-8.svg){#fig-fp-av-r1-8 fig-alt="Ilustraci�n de Problema resuelto 1.6 � Una estimaci�n de Fermi: latidos a lo largo de una vida. Resoluci�n. Multiplicamos factores correspondientes al mismo per�odo: beginaligned N&approx70fraclatidos\\,min\\, 60frac\\,min\\,h\\, 24frac\\,hd�a\\\\ &quadtimes365fracd�asa�o\\, 80 a�osapprox2,9times10^9 latidos. endaligned La estimaci�n vale del orden de unos pocos miles de millones. La estimaci�n mantiene fijos los"}

## Elegir un modelo es elegir qu� importa

Los objetos reales tienen extensi�n, el aire ejerce resistencia y las superficies suelen presentar rozamiento. Si intent�ramos describir todos esos factores desde el primer minuto, ni siquiera podr�amos analizar el trayecto de una pelota lanzada hacia arriba. La f�sica avanza mediante *modelos*: representaciones deliberadamente parciales de la realidad que conservan los rasgos relevantes para una pregunta.

Podemos estudiar la trayectoria de una pelota como si toda su masa estuviera concentrada en un punto. Esa idealizaci�n permite concentrarnos en la posici�n de la pelota cuando su forma y tama�o tienen una influencia despreciable en la pregunta elegida. Al estudiar c�mo gira la misma pelota, su forma y distribuci�n de masa adquieren importancia.

De modo semejante, cuando suponemos que un cuerpo se mueve con rapidez constante, estamos afirmando algo sobre la situaci�n analizada. Si la rapidez var�a, el uso de $d=vt$ requiere que $v$ sea la rapidez media apropiada al intervalo. M�s adelante distinguiremos rapidez instant�nea, rapidez media y movimiento con aceleraci�n.

La calidad de un modelo se aprecia en la precisi�n con que responde la pregunta planteada dentro de un dominio de validez identificable. Un modelo simple puede proporcionar una estimaci�n �til cuando sus supuestos permiten evaluar tambi�n el margen de esa respuesta.

## Estimar antes de calcular

Una estimaci�n proporciona una primera orientaci�n y evita que aceptemos como razonable cualquier cifra producida por una calculadora. Supongamos que una persona camina $4\,\mathrm{km}$ con una rapidez pr�xima a $1{,}2\,\mathrm{m/s}$. Sin efectuar todav�a una divisi�n precisa, sabemos que cuatro kil�metros son cuatro mil metros y que avanzar poco m�s de un metro por segundo requerir� cerca de una hora.

El c�lculo confirma esa intuici�n:
$$
t\approx\frac{4000\,\mathrm{m}}{1{,}2\,\mathrm{m/s}}
\approx3333\,\mathrm{s}\approx56\,\mathrm{min}.
$$
Si hubi�ramos obtenido $56\,\mathrm{s}$ o $56\,\mathrm{h}$, deber�amos sospechar inmediatamente una conversi�n incorrecta.

![Apoyo visual: Estimar antes de calcular.](../../../assets/books/fisica-preuniversitaria/figuras/AV-EJ-1-03.svg){#fig-fp-av-ej-1-03 fig-alt="Ilustraci�n de Estimar antes de calcular. El c�lculo confirma esa intuici�n: tapproxfrac4000\\,m1,2\\,m/s approx3333\\,sapprox56\\,min. Si hubi�ramos obtenido 56\\,s o 56\\,h, deber�amos sospechar inmediatamente una conversi�n incorrecta."}

Las estimaciones tambi�n permiten decidir qu� datos necesitan medirse con precisi�n. Si solo pretendemos saber si una caminata durar� media hora o toda una tarde, probablemente basta un modelo de rapidez aproximadamente constante. Si queremos programar la llegada de una nave espacial, har�n falta hip�tesis y datos m�s espec�ficos.

## Un primer problema astron�mico

La luz permite obtener informaci�n de objetos lejanos mediante observaciones a distancia. A grandes distancias, ese hecho tiene una consecuencia profunda: observar el universo tambi�n significa observarlo en el pasado. Antes de estudiar telescopios y �rbitas, podemos comprender cuantitativamente la idea mediante una operaci�n elemental.

### Problema resuelto 1.7 � La distancia al Sol a partir del tiempo de viaje de la luz {#r1-7}

Supongamos que la luz tarda aproximadamente $8\,\mathrm{min}\,20\,\mathrm{s}$ en viajar desde el Sol hasta la Tierra. Usando $c\approx3{,}00\times10^8\,\mathrm{m/s}$ para la rapidez de la luz en el vac�o, estimar la distancia recorrida.

*Resoluci�n.* Convertimos primero el tiempo a una sola unidad:
$$
t=8(60\,\mathrm{s})+20\,\mathrm{s}=500\,\mathrm{s}.
$$
En el modelo de propagaci�n a rapidez constante, la distancia es el producto de rapidez por tiempo:
$$
\begin{aligned}
d&=ct\\
&=(3{,}00\times10^8\,\mathrm{m/s})(500\,\mathrm{s})\\
&=1{,}50\times10^{11}\,\mathrm{m}\\
&=1{,}50\times10^8\,\mathrm{km}.
\end{aligned}
$$
El valor corresponde a unos $150$ millones de kil�metros. El tiempo suministrado es aproximado; conviene expresar la distancia con una cantidad de cifras acorde con ese dato.

*Control.* Una se�al capaz de recorrer $300\,000\,\mathrm{km}$ en un segundo debe recorrer unos $150$ millones de kil�metros en quinientos segundos: el orden de magnitud es correcto. Adem�s, la distancia Sol--Tierra var�a durante el a�o; nuestra estimaci�n corresponde al tiempo de viaje suministrado.

![Apoyo visual: Problema resuelto 1.7 � La distancia al Sol a partir del tiempo de viaje de la luz.](../../../assets/books/fisica-preuniversitaria/figuras/AV-R1-2.svg){#fig-fp-av-r1-2 fig-alt="Ilustraci�n de Problema resuelto 1.7 � La distancia al Sol a partir del tiempo de viaje de la luz. Control. Una se�al capaz de recorrer 300\\,000\\,km en un segundo debe recorrer unos 150 millones de kil�metros en quinientos segundos: el orden de magnitud es correcto. Adem�s, la distancia Sol--Tierra var�a durante el a�o; nuestra estimaci�n corresponde al tiempo de viaje suministrado."}

## Los gr�ficos tambi�n son relaciones matem�ticas

Un gr�fico bien construido permite ver regularidades que una tabla puede ocultar. Imaginemos una sustancia homog�nea de densidad aproximadamente constante. Si disponemos de varias muestras, esperamos que su masa crezca con el volumen. En una representaci�n de masa $m$ frente a volumen $V$, los puntos aparecer�n aproximadamente sobre una recta que pasa por el origen, con ecuaci�n
$$
m=\rho V,
$$
donde $\rho$ es la densidad del material.


![Apoyo visual: Los gr�ficos tambi�n son relaciones matem�ticas.](../../../assets/books/fisica-preuniversitaria/figuras/FIG-C01-01.svg){#fig-fp-fig-c01-01 fig-alt="Ilustraci�n de Los gr�ficos tambi�n son relaciones matem�ticas. Un gr�fico bien construido permite ver regularidades que una tabla puede ocultar. Imaginemos una sustancia homog�nea de densidad aproximadamente constante. Si disponemos de varias muestras, esperamos que su masa crezca con el volumen. En una representaci�n de masa m frente a volumen V, los puntos aparecer�n"}


### Problema resuelto 1.8 � Obtener una propiedad f�sica de un gr�fico {#r1-8}

En un experimento idealizado, una muestra de volumen $2\,\mathrm{cm^3}$ tiene masa $18\,\mathrm{g}$, mientras que otra de volumen $6\,\mathrm{cm^3}$ tiene masa $54\,\mathrm{g}$. Suponiendo densidad constante, determinar la densidad en $\,\mathrm{g/cm^3}$ y $\,\mathrm{kg/m^3}$.

*Resoluci�n.* Como la relaci�n entre masa y volumen es proporcional, el cociente es constante:
$$
\rho=\frac{m}{V}=\frac{18\,\mathrm{g}}{2\,\mathrm{cm^3}}=9\,\mathrm{g/cm^3}.
$$
Comprobamos la otra pareja: $54/6=9$, de modo que los datos son consistentes con nuestro modelo. Para cambiar de unidades debemos convertir tambi�n el denominador:
$$
1\,\mathrm{g/cm^3}=\frac{10^{-3}\,\mathrm{kg}}{(10^{-2}\,\mathrm{m})^3}=10^3\,\mathrm{kg/m^3}.
$$
Por consiguiente, $\rho=9\times10^3\,\mathrm{kg/m^3}$. El resultado describe el modelo de las muestras; identificar el material requiere informaci�n adicional.

![Apoyo visual: Problema resuelto 1.8 � Obtener una propiedad f�sica de un gr�fico.](../../../assets/books/fisica-preuniversitaria/figuras/AV-R1-3.svg){#fig-fp-av-r1-3 fig-alt="Ilustraci�n de Problema resuelto 1.8 � Obtener una propiedad f�sica de un gr�fico. Resoluci�n. Como la relaci�n entre masa y volumen es proporcional, el cociente es constante: rho=fracmV=frac18\\,g2\\,cm^3=9\\,g/cm^3. Comprobamos la otra pareja: 54/6=9, de modo que los datos son consistentes con nuestro modelo. Para cambiar de unidades debemos convertir tambi�n el denominador:"}

## El an�lisis dimensional puede sugerir una ley

A veces podemos deducir la forma de una relaci�n antes de conocer toda la f�sica que la explica. Consideremos el per�odo $P$ de un p�ndulo simple y supongamos que, para oscilaciones peque�as y en un modelo ideal, depende de la longitud $\ell$ y de la aceleraci�n de la gravedad $g$. Intentemos una relaci�n de potencias:
$$
P=C\ell^{\alpha}g^{\beta},
$$
donde $C$ es una constante sin dimensiones. La dimensi�n de la izquierda es $T$. A la derecha tenemos
$$
[\ell^{\alpha}g^{\beta}]=L^{\alpha}(LT^{-2})^{\beta}
=L^{\alpha+\beta}T^{-2\beta}.
$$
Los exponentes indican cu�ntas veces aparece cada dimensi�n. A la izquierda, $T=L^0T^1$: no aparece longitud y el tiempo tiene exponente uno. Para que ambos miembros coincidan, los exponentes de cada dimensi�n deben coincidir por separado. Igualar las potencias correspondientes de $L$ y $T$ exige
$$
\alpha+\beta=0,\qquad -2\beta=1.
$$
De $-2\beta=1$ obtenemos $\beta=-\tfrac12$; sustituir en $\alpha+\beta=0$ da $\alpha=\tfrac12$. Para cantidades positivas, una potencia de exponente $1/2$ representa una ra�z cuadrada: $\ell^{1/2}g^{-1/2}=\sqrt\ell/\sqrt g=\sqrt{\ell/g}$. La expresi�n compatible con esas dimensiones es
$$
\boxed{P=C\sqrt{\frac{\ell}{g}}.}
$$

La determinaci�n de $C$ y la selecci�n de todas las variables relevantes requieren informaci�n f�sica adicional. Para un p�ndulo simple ideal en la aproximaci�n de peque�a amplitud, un an�lisis din�mico m�s completo da $C=2\pi$. Para oscilaciones grandes, el per�odo tambi�n depende de la amplitud angular. El an�lisis dimensional propone una forma que una teor�a f�sica puede fundamentar y precisar.

![Apoyo visual: El an�lisis dimensional puede sugerir una ley.](../../../assets/books/fisica-preuniversitaria/figuras/AV-EJ-1-04.svg){#fig-fp-av-ej-1-04 fig-alt="Ilustraci�n de El an�lisis dimensional puede sugerir una ley. La determinaci�n de C y la selecci�n de todas las variables relevantes requieren informaci�n f�sica adicional. Para un p�ndulo simple ideal en la aproximaci�n de peque�a amplitud, un an�lisis din�mico m�s completo da C=2pi. Para oscilaciones grandes, el per�odo tambi�n depende de la amplitud angular. El an�lisis"}

## Qu� hacer cuando una respuesta parece correcta

Una vez completado un c�lculo, conviene formular al menos tres preguntas: �la unidad corresponde a la magnitud que me pidieron? �el orden de magnitud resulta razonable? �respet� las hip�tesis del modelo? Si estamos calculando una masa y el resultado termina expresado en $\,\mathrm{m/s}$, hay un error que puede reconocerse sin repetir ninguna operaci�n. Si la distancia a una estrella resulta menor que la longitud de una sala, probablemente confundimos las unidades. Aplicar una f�rmula de rapidez constante a un cuerpo que acelera exige justificar el valor de rapidez elegido, aunque el c�lculo algebraico est� bien realizado.

En el p�ndulo, las dimensiones fijaron la dependencia $\sqrt{\ell/g}$; el modelo de peque�a amplitud aport� el factor $2\pi$ y delimit� cu�ndo utilizarlo. Unidades, estimaci�n y supuestos intervienen juntos en la interpretaci�n de esa respuesta.

## Ejercicios de pr�ctica

Los problemas siguientes deben intentarse antes de consultar sus soluciones. Cada uno propone un razonamiento espec�fico que da sentido al uso de las f�rmulas.

### Ejercicio 1.1 � Una se�al entre la Tierra y la Luna {#e1-1}

La distancia aproximada a la Luna es $384\,400\,\mathrm{km}$. Si una se�al de radio viaja aproximadamente a $300\,000\,\mathrm{km/s}$, �cu�nto tarda en llegar? Indica si has calculado el viaje de ida o de ida y vuelta.

### Ejercicio 1.2 � Conversi�n de magnitudes diferentes {#e1-2}

Convierte $54\,\mathrm{km/h}$ a $\,\mathrm{m/s}$ y $3\,\mathrm{cm^2}$ a $\,\mathrm{m^2}$. Explica por qu� en el segundo caso el factor de escala aparece elevado al cuadrado.

### Ejercicio 1.3 � Una ecuaci�n sospechosa {#e1-3}

Para estimar el tiempo de ca�da desde una altura $h$ bajo una aceleraci�n de magnitud $g$, alguien propone $t=2h/g$. Otra persona propone $t=\sqrt{2h/g}$. Determina cu�l expresi�n tiene las unidades correctas de tiempo. �Basta esa comprobaci�n para demostrar que describe la ca�da?

### Ejercicio 1.4 � El alcance de una medici�n {#e1-4}

Una persona recorre una distancia estimada de $(5{,}0\pm0{,}1)\,\mathrm{m}$ en un tiempo de $(4{,}0\pm0{,}1)\,\mathrm{s}$. Calcula la rapidez media central y, interpretando los intervalos indicados como cotas compatibles sin suponer ninguna distribuci�n estad�stica, encuentra una cota inferior y otra superior usando los valores extremos compatibles con la informaci�n.

### Ejercicio 1.5 � De la tabla a una propiedad {#e1-5}

Dos muestras de un material homog�neo tienen los pares de valores $(V,m)=(3\,\mathrm{cm^3},21\,\mathrm{g})$ y $(7\,\mathrm{cm^3},49\,\mathrm{g})$. Calcula la densidad y expresa el resultado en el SI. �Qu� tendr�a que pasar con la masa si el volumen se duplicara y la densidad permaneciera constante?

### Ejercicio 1.6 � Una predicci�n antes del experimento {#e1-6}

En el modelo de p�ndulo de peque�a amplitud, �c�mo cambia el per�odo si se cuadruplica la longitud mientras $g$ permanece constante? Explica por qu� la respuesta no requiere conocer el valor num�rico de la constante $C$.

### Ejercicio 1.7 � La resoluci�n de una regla {#e1-7}

Una regla cuyas divisiones est�n separadas por $1\,\mathrm{mm}$ se utiliza para leer una longitud de $127\,\mathrm{mm}$. Bajo el supuesto expl�cito de que el error de redondeo es como m�ximo media divisi�n y no hay errores adicionales, indica el intervalo compatible en mil�metros y en metros. �Es una incertidumbre universal para toda regla?

### Ejercicio 1.8 � Otra densidad con cotas {#e1-8}

Una masa est� entre $49$ y $51\,\mathrm{g}$ y el volumen entre $19$ y $21\,\mathrm{cm^3}$. Calcula la densidad central, el m�nimo y el m�ximo compatibles. Identifica qu� hip�tesis has utilizado.

### Ejercicio 1.9 � Precisi�n frente a exactitud {#e1-9}

Un patr�n tiene valor $10{,}0\,\mathrm{cm}$. El grupo A obtiene $9{,}8$, $9{,}8$ y $9{,}8\,\mathrm{cm}$; el B obtiene $9{,}9$, $10{,}0$ y $10{,}1\,\mathrm{cm}$. Explica qu� grupo tiene menor dispersi�n y cu�l tiene resultados m�s pr�ximos al patr�n en promedio.

### Ejercicio 1.10 � Una escala enorme {#e1-10}

Un haz tarda aproximadamente $2\times10^{-8}\,\mathrm{s}$ en cruzar un dispositivo a velocidad $3\times10^8\,\mathrm{m/s}$. Estima su longitud y explica la cantidad de cifras que tiene sentido conservar.

### Ejercicio 1.11 � La misma velocidad media; velocidades distintas {#e1-11}

Entre $t=0$ y $t=4\,\mathrm{s}$ se proponen $x_1(t)=(2\,\mathrm{m/s})t$ y $x_2(t)=(0{,}5\,\mathrm{m/s^2})t^2$. Verifica que ambas posiciones coinciden al comienzo y al final. Determina la velocidad media en cada caso y compara los desplazamientos del �ltimo segundo. �Por qu� los dos datos extremos no permiten afirmar que ambos movimientos fueron iguales? La velocidad instant�nea se estudiar� en el cap�tulo 3.

### Ejercicio 1.12 � Alcance del an�lisis dimensional {#e1-12}

Suponiendo un per�odo $P$ que depende solo de una longitud $\ell$, una masa $m$ y una aceleraci�n $g$, busca los exponentes en $P=Cm^{\alpha}\ell^{\beta}g^{\gamma}$ utilizando dimensiones de masa, longitud y tiempo. �Qu� informaci�n sobre $C$ permanece indeterminada?

### Ejercicio 1.13 � Pendiente e intercepto de una medici�n {#e1-13}

Una muestra ocupa vol�menes $V=(0,10,20,30)\,\mathrm{cm^3}$ y las lecturas correspondientes de masa son $m=(5,25,45,65)\,\mathrm{g}$. La lectura incluye un recipiente vac�o. Representa los datos con volumen en el eje horizontal y lectura de masa en el vertical. Obt�n el aumento de masa por unidad de volumen, identifica la masa del recipiente y calcula la masa de la muestra para $V=15\,\mathrm{cm^3}$. Explica qu� representa $m/V$ en estos registros.

### Ejercicio 1.14 � Estimar una demanda de agua {#e1-14}

Un curso re�ne 30 estudiantes durante 200 jornadas. Para una primera planificaci�n se adopta un consumo de bebida de $0{,}5$ a $1{,}0\,\mathrm{L}$ por estudiante y jornada. Estima el consumo anual del curso, expresa el intervalo en $\,\mathrm{m^3}$ e identifica dos datos que permitir�an revisar la estimaci�n. Los consumos son supuestos de este ejercicio.

## Soluciones completas

### Soluci�n 1.1 {#sol-e1-1}
 La propagaci�n se aproxima por $d=ct$, de donde $t=d/c$. Con las mismas unidades de longitud en numerador y denominador:
$$
t=\frac{384\,400\,\mathrm{km}}{300\,000\,\mathrm{km/s}}\approx1{,}28\,\mathrm{s}.
$$
Es el tiempo de *ida*. Si la se�al se reflejara de inmediato y regresara por el mismo trayecto, la duraci�n aproximada ser�a $2t\approx2{,}56\,\mathrm{s}$. La distancia var�a durante la �rbita de la Luna, por lo que el c�lculo es aproximado.

### Soluci�n 1.2 {#sol-e1-2}
 Para la rapidez,
$$
54\,\mathrm{km/h}=54\frac{1000\,\mathrm{m}}{3600\,\mathrm{s}}=15\,\mathrm{m/s}.
$$
Para un �rea,
$$
3\,\mathrm{cm^2}=3(10^{-2}\,\mathrm{m})^2=3\times10^{-4}\,\mathrm{m^2}.
$$
Un cent�metro es la cent�sima parte de un metro, pero un cent�metro cuadrado es la diezmil�sima parte de un metro cuadrado.

### Soluci�n 1.3 {#sol-e1-3}
 El cociente $h/g$ tiene dimensi�n $L/(LT^{-2})=T^2$. Por consiguiente, $2h/g$ tiene dimensi�n $T^2$ y no puede representar directamente un tiempo. En cambio, $\sqrt{2h/g}$ tiene dimensi�n $T$. Esta segunda expresi�n supera el control dimensional; su fundamentaci�n requiere una ley f�sica y las hip�tesis pertinentes. La f�rmula se deduce para un cuerpo soltado desde el reposo que cae verticalmente con aceleraci�n constante de magnitud $g$, despreciando la resistencia del aire y fijando la altura inicial $h$.

### Soluci�n 1.4 {#sol-e1-4}
 El valor central es
$$
\bar v=\frac{5{,}0\,\mathrm{m}}{4{,}0\,\mathrm{s}}=1{,}25\,\mathrm{m/s}.
$$
El cociente ser� menor con el menor numerador y el mayor denominador, y mayor con el mayor numerador y menor denominador:
$$
\frac{4{,}9}{4{,}1}\,\mathrm{m/s}\leq \bar v\leq\frac{5{,}1}{3{,}9}\,\mathrm{m/s}.
$$
Redondeando las cotas hacia fuera para no estrechar el intervalo, obtenemos $[1{,}19,1{,}31]\,\mathrm{m/s}$. Son cotas derivadas directamente de los m�rgenes especificados, con una interpretaci�n de intervalo compatible.

### Soluci�n 1.5 {#sol-e1-5}
 Ambos pares proporcionan la misma raz�n: $21/3=49/7=7\,\mathrm{g/cm^3}$. Como $1\,\mathrm{g/cm^3}=1000\,\mathrm{kg/m^3}$, la densidad es $7000\,\mathrm{kg/m^3}$. Si $m=\rho V$ con $\rho$ constante, duplicar $V$ duplica $m$; el resultado depende precisamente de esa hip�tesis.

### Soluci�n 1.6 {#sol-e1-6}
 De $P=C\sqrt{\ell/g}$ se sigue que
$$
P'=C\sqrt{\frac{4\ell}{g}}=2C\sqrt{\frac{\ell}{g}}=2P.
$$
El per�odo se duplica. No es necesario determinar $C$ porque aparece del mismo modo en ambos cocientes; basta mantener el mismo modelo de peque�as oscilaciones.

### Soluci�n 1.7 {#sol-e1-7}
 Con la hip�tesis indicada, $L\in[126{,}5,127{,}5]\,\mathrm{mm}$. Como $1\,\mathrm{mm}=10^{-3}\,\mathrm{m}$, los extremos en SI son $0{,}1265\,\mathrm{m}$ y $0{,}1275\,\mathrm{m}$. El resultado describe �nicamente el redondeo bajo las hip�tesis indicadas; la mala alineaci�n, calibraci�n o deformaci�n requieren contribuciones adicionales.

### Soluci�n 1.8 {#sol-e1-8}
 Con los puntos medios, $\rho_c=50/20=2{,}50\,\mathrm{g/cm^3}$. Al considerar todos los valores positivos de los intervalos, $\rho_{\min}=49/21\approx2{,}33\,\mathrm{g/cm^3}$ y $\rho_{\max}=51/19\approx2{,}6842\,\mathrm{g/cm^3}$. Un intervalo conservador redondeado a cent�simas es $[2{,}33,2{,}69]\,\mathrm{g/cm^3}$. Se emplea el modelo $\rho=m/V$ con masa y volumen positivos y cotas que pueden coexistir; el c�lculo utiliza directamente los extremos compatibles.

### Soluci�n 1.9 {#sol-e1-9}
 El grupo A tiene dispersi�n observada nula, pero sus valores se apartan del patr�n en $0{,}2\,\mathrm{cm}$. El promedio de B es $10{,}0\,\mathrm{cm}$, igual al patr�n; el rango de B mide $0{,}2\,\mathrm{cm}$. As�, A muestra mejor repetibilidad en esta muestra, mientras que B tiene promedio m�s exacto respecto de la referencia. La dispersi�n nula describe la repetibilidad de la serie; evaluar el error sistem�tico exige un contraste con un patr�n.

### Soluci�n 1.10 {#sol-e1-10}
 Con un modelo de rapidez constante, $d=ct=(3\times10^8\,\mathrm{m/s})(2\times10^{-8}\,\mathrm{s})\approx6\,\mathrm{m}$. Como los datos se proporcionan con una sola cifra significativa, informar muchos decimales carecer�a de justificaci�n. Se trata de una estimaci�n de escala sustentada en los supuestos declarados.

### Soluci�n 1.11 {#sol-e1-11}
 Para ambas funciones $x(0)=0$ y $x(4\,\mathrm{s})=8\,\mathrm{m}$, por lo que sus velocidades medias en el intervalo completo son $2\,\mathrm{m/s}$. En $t=3\,\mathrm{s}$, sin embargo, $x_1=6\,\mathrm{m}$ y $x_2=4{,}5\,\mathrm{m}$. Durante el �ltimo segundo los desplazamientos son, respectivamente, $2\,\mathrm{m}$ y $3{,}5\,\mathrm{m}$, y sus velocidades medias en ese tramo son $2$ y $3{,}5\,\mathrm{m/s}$. Los mismos extremos del intervalo completo admiten movimientos intermedios distintos. En el cap�tulo 3 calcularemos, adem�s, las velocidades instant�neas finales: $2$ y $4\,\mathrm{m/s}$.

### Soluci�n 1.12 {#sol-e1-12}
 Usamos $[m]=M$, $[\ell]=L$, $[g]=LT^{-2}$ y $[P]=T$. La expresi�n propuesta tiene dimensi�n $M^\alpha L^{\beta+\gamma}T^{-2\gamma}$, por lo que $\alpha=0$, $\beta+\gamma=0$ y $-2\gamma=1$. De aqu� $\gamma=-1/2$ y $\beta=1/2$. Obtenemos $P=C\sqrt{\ell/g}$; hallar la constante adimensional $C$ y validar las variables escogidas requiere una descripci�n f�sica adicional. Para un p�ndulo simple de peque�a amplitud se encuentra $C=2\pi$ mediante un modelo din�mico.


### Soluci�n 1.13 {#sol-e1-13}
 La pendiente es $\Delta m/\Delta V=20/10=2\,\mathrm{g/cm^3}=2000\,\mathrm{kg/m^3}$. La recta de lecturas es $m=5\,\mathrm{g}+(2\,\mathrm{g/cm^3})V$. El recipiente aporta $5\,\mathrm{g}$; a $V=15\,\mathrm{cm^3}$ la muestra tiene $30\,\mathrm{g}$ y la lectura conjunta ser�a $35\,\mathrm{g}$. El cociente $m/V$ incluye la contribuci�n del recipiente y var�a con $V$; en $V=0$ esa raz�n queda fuera de su dominio. La densidad de la muestra se obtiene de la pendiente bajo el modelo lineal y tras separar el recipiente.

![Apoyo visual: Soluci�n 1.13.](../../../assets/books/fisica-preuniversitaria/figuras/AV-E1-13.svg){#fig-fp-av-e1-13 fig-alt="Ilustraci�n de Soluci�n 1.13. Un curso re�ne 30 estudiantes durante 200 jornadas. Para una primera planificaci�n se adopta un consumo de bebida de 0,5 a 1,0\\,L por estudiante y jornada. Estima el consumo anual del curso, expresa el intervalo en \\,m^3 e identifica dos datos que permitir�an revisar la estimaci�n. Los consumos son supuestos de este"}

La pendiente es $\Delta m/\Delta V=20/10=2\,\mathrm{g/cm^3}=2000\,\mathrm{kg/m^3}$. La recta de lecturas es $m=5\,\mathrm{g}+(2\,\mathrm{g/cm^3})V$. El recipiente aporta $5\,\mathrm{g}$; a $V=15\,\mathrm{cm^3}$ la muestra tiene $30\,\mathrm{g}$ y la lectura conjunta ser�a $35\,\mathrm{g}$. El cociente $m/V$ incluye la contribuci�n del recipiente y var�a con $V$; en $V=0$ esa raz�n queda fuera de su dominio. La densidad de la muestra se obtiene de la pendiente bajo el modelo lineal y tras separar el recipiente.

### Soluci�n 1.14 {#sol-e1-14}

Hay $30(200)=6000$ estudiante-jornadas. El intervalo es $[3000,6000]\,\mathrm{L}=[3,6]\,\mathrm{m^3}$, con $4{,}5\,\mathrm{m^3}$ al usar el punto medio del supuesto de consumo. La asistencia efectiva y un registro de consumo permiten ajustar la estimaci�n. El resultado corresponde al agua bebida; las dem�s actividades requieren partidas propias.

## Diagn�stico de salida: antes de estudiar �lgebra y vectores

Para avanzar con seguridad, explica por escrito la diferencia entre magnitud, unidad y dimensi�n; reconoce en qu� condiciones una estimaci�n es aceptable; distingue exactitud y precisi�n; y aprende a identificar cu�ndo una respuesta exige datos que no conocemos. Las cuestiones 1.3, 1.4, 1.7, 1.9 y 1.11 permiten comprobar estas capacidades.

**Tres controles de transferencia.**

1. Convierte $2{,}5\,\mathrm{g/cm^3}$ al SI y explica el factor usado.
2. Para una distancia $[4{,}8,5{,}2]\,\mathrm{m}$ y un tiempo $[1{,}9,2{,}1]\,\mathrm{s}$, encuentra un intervalo conservador de rapidez media, redondeado a cent�simas.
3. Si dos movimientos comparten posiciones inicial y final, �queda fijada la distancia recorrida? Justifica con un recorrido posible.


**Contraste despu�s del intento.** (1) $2500\,\mathrm{kg/m^3}$: al dividir el factor $10^{-3}$ de masa por $10^{-6}$ de volumen queda $10^3$. (2) Los extremos exactos son $4{,}8/2{,}1$ y $5{,}2/1{,}9$ en $\,\mathrm{m/s}$; redondeando hacia fuera, $[2{,}28,2{,}74]\,\mathrm{m/s}$. (3) Un recorrido directo y otro que incluya una ida y vuelta adicional pueden compartir extremos y tener longitudes diferentes.
**Criterio para avanzar.** Explica las hip�tesis, elige un modelo y revisa las unidades y los �rdenes de magnitud de tus resultados. Si falla la conversi�n, vuelve al problema 1.8; si fallan las cotas, al problema 1.3; si confundes los extremos con la historia completa, al ejercicio 1.11. Repite luego el control con otros datos y explica por qu� tu m�todo sigue funcionando.

---

[�ndice del libro](index.html) � [Cap�tulo siguiente ](capitulo-02.html)
