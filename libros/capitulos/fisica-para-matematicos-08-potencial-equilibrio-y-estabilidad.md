---
title: "Potencial, equilibrio y estabilidad"
subtitle: "Física para matemáticos · Tomo I · Capítulo 8"
author: "A. Peña"
description: "Capítulo 8 de la edición revisada, con problemas y soluciones desarrolladas."
content-id: MA-BCH-0353
source-id: FISPM-r20261021-C08
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
edition: r20261021
canonical-edition: true
date-modified: 2026-10-21
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0352"]
related: [MA-BOK-0005]
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
include-in-header:
  - ../../assets/includes/ma-math-font-ready.html
  - ../../assets/books/fispm/fispm-lightbox-focus.html
format:
  html:
    css: ../../assets/books/fispm/fispm-reader.css
    lightbox: true
number-sections: false
---

[← 7. Trabajo y energía cinética](fisica-para-matematicos-07-trabajo-y-energia-cinetica.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [9. Impulso, colisiones y centro de masa →](fisica-para-matematicos-09-impulso-colisiones-y-centro-de-masa.md)

Un carro de dos kilogramos está unido a un resorte horizontal sobre un riel liso. Al principio el resorte tiene su longitud natural y el carro está en reposo. Un mecanismo comienza a tirar de él hacia la derecha con una fuerza constante de ocho newtons. El resorte ejerce una fuerza contraria que crece ocho newtons por cada metro de extensión. ¿Dónde volverá a detenerse el carro? ¿Coincide ese lugar con la posición donde se equilibran las fuerzas?

Tomaremos el laboratorio como marco inercial y la extensión del resorte como coordenada $x$, positiva hacia la derecha. El carro se representa por una partícula de masa constante $m=2\,\mathrm{kg}$; el peso y la normal se equilibran verticalmente. El resorte obedece $F_s=-kx$, con $k=8\,\mathrm{N/m}$, en el intervalo $-1\,\mathrm m<x<3\,\mathrm m$. Omitimos rozamiento, aire y rotación. El mecanismo sostiene $f_0=8\,\mathrm N$ durante todo el movimiento estudiado. Su fuerza neta horizontal es

$$
F(x)=f_0-kx.
$$

En un metro de extensión ambas fuerzas se equilibran. Pero el carro ha sido acelerado antes de llegar allí: no hay motivo para que pierda de golpe la velocidad que adquirió.

![Un resorte y un tirón constante actúan sobre un carro en un riel horizontal liso.](/assets/books/fispm/r20261021/potencial_carro.svg){.fpm-v04-figure}

*Figura 8.1.* El eje mide extensión respecto de la longitud natural. La posición $x=1\,\mathrm m$ equilibra el tirón y la fuerza elástica. La posición de reposo inicial es $x=0$, donde la fuerza neta apunta a la derecha. El esquema no representa módulos mediante longitudes de flecha.

## La misma integral, leída desde sus extremos

El trabajo acumulado desde el origen es

$$
W(0\to x)=\int_0^x(f_0-k\xi)\,d\xi
=f_0x-\frac12kx^2.
$$

Como el carro parte del reposo, el teorema del capítulo anterior da $K(x)=f_0x-kx^2/2$. Esta expresión se anula en $x=0$ y en $x=2f_0/k=2\,\mathrm m$. Entre esos puntos es positiva. El segundo cero corresponde a la primera detención después de salir del origen. Allí la fuerza neta es ocho newtons hacia la izquierda, de modo que el carro inicia el regreso; no permanece en reposo.

Podemos recoger la integral en una función

$$
U(x)=\frac12kx^2-f_0x,
$$

que satisface $F(x)=-U'(x)$. El trabajo entre dos posiciones cualesquiera del intervalo es entonces $W(x_i\to x_f)=U(x_i)-U(x_f)$. En vez de calcular una nueva integral para cada recorrido, evaluamos la misma función en sus extremos.

En el estado inicial, $K=0$ y $U(0)=0$. Por tanto, durante este movimiento

$$
K(x)+U(x)=0.
$$

La gráfica de $U$ es una parábola cuyo mínimo está en un metro y vale menos cuatro joules. La separación vertical entre la línea horizontal $E=0$ y esa parábola es $K=E-U$. En el mínimo la energía cinética es máxima, cuatro joules, y la rapidez es dos metros por segundo. El carro cruza la posición de fuerzas equilibradas con su mayor rapidez.

![La parábola del potencial efectivo y la recta de energía delimitan los extremos del movimiento y la energía cinética intermedia.](/assets/books/fispm/r20261021/potencial_parabola.svg){.fpm-v04-figure}

*Figura 8.2.* La ordenada es energía, no altura física del riel. Los extremos $x=0$ y $x=2\,\mathrm m$ tienen rapidez nula; en $x=1\,\mathrm m$ la pendiente del potencial y la fuerza neta son cero, pero la rapidez no lo es. La diferencia $E-U$ se mide en joules.

La función $U$ incorpora tanto el resorte como el tirón constante: $U=U_s+U_f$, con $U_s=kx^2/2$ y $U_f=-f_0x$. Esta elección no borra el trabajo del mecanismo. Para el subsistema carro–resorte, $K+U_s$ aumenta en $f_0x$ mientras el carro avanza. Al incluir también $U_f$ obtenemos una constante matemática del modelo de fuerzas considerado. Debemos indicar qué interacciones están incluidas antes de interpretar una energía mecánica como la de un sistema físicamente aislado.

## Construir un potencial y elegir su referencia

**Definición.** En un intervalo abierto $I$ de posiciones, una función diferenciable $U:I\to\mathbb R$ es un *potencial* para la componente de fuerza $F(x)$ si

$$
F(x)=-\frac{dU}{dx}(x).
$$

Sus valores tienen unidades de energía. El potencial describe la interacción representada por esa fuerza en las condiciones fijadas del modelo. Para la gravedad terrestre uniforme puede utilizarse $U_g=mgy$, con $y$ hacia arriba; para un resorte lineal, $U_s=kx^2/2$. En ambos casos se mantienen fijos los parámetros y apoyos supuestos. Cuando se usa un campo gravitatorio externo, esta descripción recoge la interacción con su fuente sin calcular el movimiento de esa fuente.

Si $F$ es continua en $I$, el teorema fundamental del cálculo proporciona un potencial:

$$
U(x)=U(x_*)-\int_{x_*}^{x}F(\xi)\,d\xi,
$$

con $x_*\in I$ como referencia. Además,

$$
\int_{x_i}^{x_f}F(x)\,dx=U(x_i)-U(x_f).
$$

**Proposición.** Dos potenciales de una misma fuerza en un intervalo difieren en una constante. Recíprocamente, añadir una constante a un potencial conserva la fuerza y todos sus trabajos.

**Demostración.** Si $U_1'=-F=U_2'$, la diferencia $U_1-U_2$ tiene derivada nula. Por el teorema del valor medio es constante en el intervalo. En sentido inverso, la derivada de $U+C$ es $U'$, mientras que $(U(x_i)+C)-(U(x_f)+C)=U(x_i)-U(x_f)$. Ni la fuerza ni el trabajo cambian.

En el ejemplo inicial podemos sumar cuatro joules y escribir

$$
\widetilde U(x)=\frac12k(x-1\,\mathrm m)^2,
\qquad \widetilde E=4\,\mathrm J.
$$

La nueva parábola tiene mínimo cero, pero conserva las pendientes y la diferencia $\widetilde E-\widetilde U=E-U$. Las detenciones, rapideces y fuerzas son las mismas. Un potencial negativo no significa fuerza hacia la izquierda ni energía cinética negativa: el sentido de la fuerza se obtiene de la pendiente con signo contrario.

Para un potencial con unidades de joules y una coordenada en metros, $U'$ tiene unidades $\mathrm{J/m}=\mathrm N$ y $U''$ unidades $\mathrm{N/m}$. Una derivada numérica sin respetar las escalas de los ejes puede dar un módulo de fuerza equivocado aunque reconozca bien su signo.

## Cuándo el trabajo depende sólo de los extremos

**Definición.** Una fuerza que depende únicamente de la posición es *conservativa* en un dominio si su trabajo es el mismo para todos los recorridos suaves a trozos de ese dominio que unen los mismos extremos. El dominio y los recorridos permitidos forman parte de la afirmación.

En un intervalo rectilíneo, una fuerza continua $F(x)$ tiene el potencial que acabamos de construir. Si la partícula va y vuelve por la misma recta, el trabajo de esa fuerza en el recorrido cerrado es cero: las integrales de ida y vuelta tienen límites opuestos. El rozamiento cinético no contradice esta conclusión. Su componente cambia con el sentido del deslizamiento; no es una única función $F(x)$ que conserve los mismos valores al invertir la marcha. Sobre una mesa fija, una ida y vuelta de distancia $d$ en cada sentido disipa trabajo $-2\mu_kmgd$.

En un plano hay recorridos distintos que pueden dar trabajos diferentes. En el capítulo 7 encontramos ese comportamiento para $\mathbf F=(\kappa y,0)$: cambiar el orden de un tramo horizontal y uno vertical cambió su trabajo. No existe un potencial de posición que reproduzca ambos resultados mediante una misma diferencia de extremos.

Para comprobar un potencial explícito $U(x,y)$ se derivan sus componentes manteniendo fija la otra coordenada:

$$
F_x=-\frac{\partial U}{\partial x},\qquad
F_y=-\frac{\partial U}{\partial y}.
$$

La notación $\partial U/\partial x$ designa la derivada de $U$ respecto de $x$ con $y$ constante. Si estas relaciones se cumplen y $U$ es continuamente diferenciable, la regla de la cadena a lo largo de un recorrido da $dU/dt=-\mathbf F\cdot\mathbf v$. Su integral produce otra vez $W=U_i-U_f$. Basta verificar esas derivadas para el ejercicio 19; no necesitamos todavía un criterio general de cálculo vectorial para decidir la existencia de potenciales en dominios arbitrarios.

## Energía mecánica y trabajo de las otras fuerzas

**Definición.** Para una partícula de masa constante $m>0$, con un potencial de posición $U$ elegido para ciertas fuerzas, llamaremos *energía mecánica* de esta descripción a

$$
E=K+U=\frac12m\dot x^2+U(x).
$$

Se declara qué fuerzas están representadas en $U$ y cuál es su referencia. Varias fuerzas conservativas se incorporan sumando sus potenciales. Las fuerzas restantes se contabilizan por su trabajo.

**Teorema.** Supongamos que $U$ no depende explícitamente del tiempo, que el movimiento satisface $m\ddot x=-U'(x)+F_o$ y que cumple las condiciones de regularidad del teorema del trabajo del capítulo 7. Entonces

$$
E(t_1)-E(t_0)=W_o,
$$

con $W_o=\int_{t_0}^{t_1}F_o\dot x\,dt$. En particular, si $W_o=0$ en cada subintervalo del movimiento, $E$ permanece constante.

**Demostración.** El teorema del trabajo da $K_f-K_i=W_U+W_o$. La fuerza representada por $U$ realiza $W_U=U_i-U_f$. Sustituir y reunir los valores del mismo estado produce $(K_f+U_f)-(K_i+U_i)=W_o$. Aplicar esta identidad a cualquier subintervalo da la constancia cuando su segundo miembro es cero. De forma local, la misma igualdad se lee $dE/dt=F_o\dot x$.

La fricción viscosa $F_o=-b\dot x$, con $b>0$, produce $dE/dt=-b\dot x^2\leq0$. La energía mecánica de esta descripción no aumenta, aunque el sistema ampliado requiera contabilizar la energía interna y sus intercambios. Decrecer tampoco significa que el movimiento deba terminar exactamente en el mínimo del potencial: esa conclusión necesita información adicional sobre las fuerzas y la evolución. Con rozamiento estático, por ejemplo, pueden existir estados de reposo alejados del mínimo.

Las guías fijas ideales y las tensiones que no hacen trabajo, bajo las condiciones ya justificadas, pueden quedar entre las otras fuerzas con trabajo nulo. Si cambian los apoyos, los parámetros o el régimen de contacto, se revisa el balance. La mera presencia de un resorte no autoriza a escribir conservación de energía mecánica ignorando un motor o una resistencia.

El cambio de un apoyo puede modificar el potencial incluso si la ley elástica conserva la misma constante. Para seguir esa modificación necesitamos mantener las dos dependencias de la función: la posición de la partícula y el tiempo del aparato que la rodea.

**Proposición (potencial con dependencia temporal).** Sea $U(x,t)$ una función con derivadas parciales primeras continuas, y supongamos que una partícula de masa constante satisface $m\ddot x=-\partial U/\partial x+F_o$ en un intervalo de movimiento suave. La función $E(t)=m\dot x^2/2+U(x(t),t)$ cumple

$$
\frac{dE}{dt}=F_o\dot x+\frac{\partial U}{\partial t}(x(t),t).
$$

**Demostración.** La regla de la cadena da $\dot E=m\dot x\ddot x+(\partial U/\partial x)\dot x+\partial U/\partial t$. Sustituir Newton cancela los términos que contienen la derivada espacial y deja la identidad. Integrarla proporciona el balance entre dos instantes.

La derivada parcial temporal mantiene fija la posición $x$ mientras cambia el aparato. Si el extremo de un resorte está en una posición prescrita $X(t)$, con $k$ constante, podemos elegir $U=k(x-X(t))^2/2$. Entonces $\partial U/\partial t=-k(x-X)\dot X$. Esa cantidad describe, con esta elección de energía elástica, la potencia que el movimiento del apoyo entrega al conjunto formado por partícula y resorte ideal. El ejercicio 21 calcula un movimiento completo en el que esa entrega cambia de signo.

La referencia también debe quedar declarada. Reemplazar $U(x,t)$ por $U(x,t)+C(t)$ conserva la fuerza y suma $\dot C(t)$ a la derivada de la energía escrita. Una referencia temporal arbitraria cambia la contabilidad de esa función. Para interpretar la tasa como energía transferida por un agente utilizamos la reserva física especificada y una referencia fija, como la energía elástica nula en un resorte sin deformación. El ejercicio 20 estudia otra modificación física: una rigidez que cambia con el tiempo.

## Leer una línea de energía sin confundirla con una trayectoria

Cuando $E$ es constante,

$$
\frac12m\dot x^2=E-U(x).
$$

La desigualdad $U(x)\leq E$ es necesaria para una posición visitada. En un punto donde $U(x)<E$, la rapidez es $\sqrt{2(E-U(x))/m}$. La ecuación admite ambos signos de velocidad: el sentido inicial y los cambios de tramo seleccionan cuál corresponde al movimiento. Una línea de energía no reemplaza el estado inicial completo.

Si un intervalo con $U>E$ separa dos regiones permitidas, la partícula clásica de este modelo no puede atravesarlo. La continuidad de la posición la obligaría a visitar puntos con energía cinética negativa. Aun cuando no haya un intervalo prohibido, puede existir un equilibrio que se alcanza sólo como límite para tiempo infinito.

Consideremos el potencial de dos pozos

$$
U(x)=U_b\left[\left(\frac{x}{a}\right)^2-1\right]^2,
\qquad U_b=4\,\mathrm J,\quad a=1\,\mathrm m,
$$

para una partícula de dos kilogramos. Es una interacción idealizada definida por esta función; no suponemos que la curva sea la forma de una pista. Los mínimos están en $x=\pm a$, donde $U=0$, y entre ellos aparece una barrera en $x=0$, donde $U=U_b$.

Con $E=1\,\mathrm J$, una partícula que comienza en el pozo derecho queda entre $a/\sqrt2$ y $a\sqrt{3/2}$. Hay otra región permitida a la izquierda, pero el intervalo alrededor del origen está prohibido y la separa de ella. Con $E=5\,\mathrm J$, en cambio, la energía cinética en el origen vale un joule. Una partícula que se dirige hacia la barrera desde el pozo derecho puede cruzarla con rapidez de un metro por segundo.

![El mismo potencial de dos pozos se compara con tres líneas de energía: por debajo, en la altura y por encima de la barrera.](/assets/books/fispm/r20261021/potencial_dos_pozos.svg){.fpm-v04-figure}

*Figura 8.3.* A energía de un joule hay dos intervalos permitidos separados. A cinco joules el origen se atraviesa con rapidez positiva. La línea de cuatro joules toca el máximo: requiere examinar el tiempo de aproximación antes de afirmar que hay cruce.

En el caso límite $E=U_b$, escribir $\xi=x/a$ da

$$
E-U(x)=U_b\,\xi^2(2-\xi^2).
$$

Para aproximarse al origen desde la derecha, el tiempo contiene la integral

$$
\sqrt{\frac{m}{2U_b}}\,a
\int_{\xi}^{\xi_0}\frac{d\eta}{\eta\sqrt{2-\eta^2}},
\qquad 0<\xi<\xi_0<\sqrt2.
$$

Cerca de cero, el factor $\sqrt{2-\eta^2}$ tiende a $\sqrt2$, por lo que el integrando crece como $1/(\sqrt2\eta)$. La integral diverge logarítmicamente cuando $\xi\to0^+$. La partícula se acerca al equilibrio superior sin alcanzarlo en tiempo finito. El punto satisface $U=E$, pero no es una detención ordinaria seguida de un regreso o un cruce en un instante finito.

En una detención ordinaria con $U(x_t)=E$ y $U'(x_t)\ne0$, la diferencia $E-U$ tiene un cero simple en el lado permitido. La rapidez se anula como la raíz cuadrada de la distancia al extremo y la integral de tiempo converge localmente. La fuerza no nula indica el sentido de la continuación. Esta es la situación de las detenciones del carro inicial, en contraste con la aproximación al máximo del doble pozo.

## Qué se perturba cuando se habla de estabilidad

En un sistema sin otras fuerzas tangenciales, una posición de equilibrio satisface $U'(x_e)=0$. El estado de equilibrio incluye además $\dot x=0$. Pasar por $x_e$ con velocidad distinta de cero no es permanecer en equilibrio, como mostró el carro en un metro de extensión.

**Definición.** El equilibrio $(x_e,0)$ es *estable* si, para cualesquiera tolerancias positivas $\varepsilon_x$ de posición y $\varepsilon_v$ de velocidad, existen tolerancias iniciales positivas $\delta_x,\delta_v$ tales que todos los movimientos con

$$
|x(0)-x_e|<\delta_x,\qquad |\dot x(0)|<\delta_v
$$

satisfacen $|x(t)-x_e|<\varepsilon_x$ y $|\dot x(t)|<\varepsilon_v$ para todo tiempo futuro, con soluciones definidas durante ese futuro. El equilibrio es *inestable* si existe una tolerancia fija de posición o de velocidad para la cual datos iniciales arbitrariamente próximos al equilibrio producen una trayectoria que alcanza o supera esa tolerancia en algún tiempo futuro.

Las tolerancias de posición y velocidad tienen unidades distintas; no las sumamos sin introducir una escala de comparación. La definición exige elegir los datos iniciales una vez para controlar todos los tiempos posteriores. No basta demostrar que la trayectoria permanece cerca durante un tiempo breve.

Para los criterios siguientes suponemos que $U$ es dos veces continuamente diferenciable cerca del equilibrio, que no hay otras fuerzas tangenciales y que las soluciones de Newton existen, son únicas y pueden continuarse mientras posición y velocidad permanezcan en una región compacta del dominio regular. Esta propiedad usual para fuerzas continuamente diferenciables fija el marco de los argumentos; no desarrollaremos aquí una teoría general de existencia de ecuaciones diferenciales.

**Teorema del mínimo estricto.** Bajo esas hipótesis, si $U$ tiene un mínimo local estricto en $x_e$, el equilibrio $(x_e,0)$ es estable.

**Demostración.** Un mínimo estricto significa que $U(x)>U(x_e)$ para todo $x\ne x_e$ suficientemente próximo. Dadas las dos tolerancias de la definición, elegimos $r<\varepsilon_x$ tan pequeño que el intervalo cerrado $[x_e-r,x_e+r]$ quede dentro de esa región. La diferencia de potencial en cada uno de sus dos extremos es positiva. Llamemos $B$ a la menor de esas diferencias.

Elegimos un incremento de energía $h>0$ menor que $B$ y que $m\varepsilon_v^2/2$. Para construir las tolerancias iniciales, repartimos ese margen entre las dos contribuciones a la energía. Por continuidad de $U$, existe $0<\delta_x<r$ tal que $|x(0)-x_e|<\delta_x$ implica $0\leq U(x(0))-U(x_e)<h/2$. Elegimos además $\delta_v=\sqrt{h/m}$: si $|\dot x(0)|<\delta_v$, entonces $m\dot x(0)^2/2<h/2$. Al sumar, obtenemos $E(0)-U(x_e)<h$ para todos esos datos iniciales. La energía se conserva. Si la posición alcanzara uno de sus extremos, tendría que cumplir $E\geq U(x_e)+B$, contradiciendo la elección de $h$. Por continuidad del movimiento no puede salir sin alcanzar antes un extremo, de modo que $|x(t)-x_e|<r<\varepsilon_x$.

Dentro del intervalo, $U(x)\geq U(x_e)$; por tanto, $m\dot x^2/2=E-U(x)\leq E-U(x_e)<h<m\varepsilon_v^2/2$. También la velocidad permanece dentro de su tolerancia. Posición y velocidad quedan acotadas en una región compacta regular, lo que permite continuar la solución según la hipótesis declarada. Esas dos cotas prueban la estabilidad para todo tiempo futuro.

El argumento encierra la trayectoria mediante barreras de energía. No demuestra que termine en el equilibrio. Un resorte ideal, después de una pequeña perturbación, puede continuar oscilando indefinidamente sin alejarse mucho y sin asentarse. La aproximación al reposo requiere otra pregunta y otras hipótesis.

Podemos expresar las dos tolerancias en un estado con coordenadas adimensionales: elegimos una longitud de referencia $a>0$ y una rapidez de referencia $b>0$, y escribimos $z=((x-x_e)/a,\dot x/b)$. Una cota de la norma de $z$ controla posición y velocidad, y sendas cotas de ambas componentes controlan esa norma. Esta equivalencia permitirá conservar la misma definición cuando el capítulo 19 compare componentes de velocidad angular y el 26 estudie estados de varias variables. En cada caso habrá que indicar cuáles son las variables cuya proximidad se desea controlar.

![Un mínimo estricto ofrece dos barreras positivas alrededor del equilibrio; una energía inicial suficientemente pequeña no permite alcanzarlas.](/assets/books/fispm/r20261021/potencial_barreras.svg){.fpm-v04-figure}

*Figura 8.4.* La prueba utiliza el menor de los incrementos de potencial en los dos extremos de un intervalo. La condición de energía también controla la velocidad. El dibujo ilustra la barrera del argumento, no supone que todo potencial sea parabólico.

## La segunda derivada y los casos que deja abiertos

**Proposición.** Si $U'(x_e)=0$ y $U$ es dos veces continuamente diferenciable, entonces $U''(x_e)>0$ implica estabilidad y $U''(x_e)<0$ implica inestabilidad, bajo las hipótesis dinámicas anteriores. La igualdad $U''(x_e)=0$ no decide por sí sola.

**Demostración.** Si $U''(x_e)>0$, la continuidad conserva su signo positivo en un intervalo suficientemente pequeño. Por ello $U'$ crece desde cero: es negativa a la izquierda de $x_e$ y positiva a la derecha. Integrar esos signos muestra que $U$ tiene un mínimo estricto en $x_e$. Se aplica el teorema anterior.

Si $U''(x_e)<0$, podemos elegir una constante $k>0$, con unidades de fuerza por longitud, y un intervalo $|q|\leq r$, donde $q=x-x_e$, tales que $U''(x_e+q)\leq-k$. Para $0<q\leq r$, integrar desde cero da $-U'(x_e+q)\geq kq$. Preparemos $q(0)=q_0>0$ arbitrariamente pequeño y velocidad inicial cero. Mientras permanezca en ese lado del intervalo, la aceleración es positiva, la posición crece y

$$
\ddot q\geq\frac{kq_0}{m},\qquad
q(t)\geq q_0+\frac{kq_0}{2m}t^2.
$$

Esta cota obliga a llegar a $r$ en un tiempo finito o a haber salido antes. Por pequeños que sean los datos iniciales, hay perturbaciones que abandonan una misma vecindad fijada del equilibrio. Esto niega la estabilidad. Finalmente, los potenciales $+\beta q^4$ y $-\beta q^4$, con $\beta>0$, tienen ambos segunda derivada nula en cero, pero el primero tiene mínimo estricto y el segundo empuja hacia fuera cualquier desplazamiento no nulo. Sus comportamientos distintos muestran que la igualdad no decide.

![Potenciales con mínimo, máximo y extremos degenerados muestran qué informa el signo de la segunda derivada y cuándo resulta insuficiente.](/assets/books/fispm/r20261021/potencial_estabilidad.svg){.fpm-v04-figure}

*Figura 8.5.* Las curvas representan energía frente a posición. El mínimo cuártico tiene equilibrio estable aunque su segunda derivada sea cero. Los ejemplos se comparan con escalas normalizadas y no representan la misma ley de fuerza.

En los textos elementales suele llamarse *equilibrio neutro* a una región de potencial constante: trasladar una partícula y volver a dejarla en reposo produce otro reposo. Conviene distinguir esa clasificación estática de la definición anterior. Con $U$ constante, una velocidad inicial no nula, por pequeña que sea, produce $x(t)=x(0)+v_0t$. En una recta libre acaba por salir de cualquier vecindad acotada de una posición individual. Por tanto, ese estado individual no es estable frente a todas las perturbaciones de posición y velocidad. Al hablar de estabilidad debemos mantener explícitas las perturbaciones que admitimos.

La energía también deja de ser un criterio completo si agregamos contactos o fricción. Un resorte que tira de un bloque puede quedar equilibrado por rozamiento estático en varias posiciones. Se resuelve entonces la admisibilidad de las fuerzas, no sólo $U'=0$. Los potenciales organizan una parte de la dinámica; las restricciones y leyes del contacto siguen determinando qué estados pertenecen al modelo.

## Ejercicios

Se usa $g=10\,\mathrm{m/s^2}$. Salvo indicación contraria, las partículas tienen masa constante, se mueven sobre una recta sin rozamiento y sólo reciben la fuerza $F=-U'$. Las funciones de potencial no dependen del tiempo. Un cambio de referencia se aplica a $U$ y a $E$ conjuntamente. Los ejemplos polinómicos se consideran modelos ideales dentro de las regiones utilizadas.

### 1. Cambiar el estado inicial del carro {#ejercicio-8-1}

En el carro inicial, prepare $x(0)=1\,\mathrm m$ y $v(0)=+3\,\mathrm{m/s}$. Calcule la energía con la referencia $U(0)=0$, los dos extremos de posición y la rapidez al cruzar el mínimo. Compruebe el intervalo de validez declarado para el resorte.

### 2. Una fuerza con potencial cuártico {#ejercicio-8-2}

Una partícula recibe $F(x)=-(4\,\mathrm{N/m^3})x^3$. Construya un potencial con $U(0)=0$ y calcule el trabajo de la fuerza entre uno y dos metros. Si parte de un metro hacia la derecha con cinco joules de energía cinética, determine si puede llegar a dos metros y localice su primera detención futura.

### 3. Subir bajo gravedad uniforme {#ejercicio-8-3}

Una partícula de dos kilogramos se lanza verticalmente hacia arriba con rapidez de ocho metros por segundo desde $y=2\,\mathrm m$. Sólo actúa el peso. Use $U=mgy$ para calcular su rapidez al pasar por $y=5\,\mathrm m$ durante la subida y la altura máxima. Repita la interpretación usando como cero del potencial el punto de lanzamiento.

### 4. La mayor extensión no es el equilibrio {#ejercicio-8-4}

Una masa de dos kilogramos cuelga de un resorte vertical de $k=100\,\mathrm{N/m}$ cuyo extremo superior está fijo. Se libera del reposo cuando el resorte no está deformado. Tome $y$ hacia abajo desde esa posición y suponga válida la ley lineal hasta $y=0{,}50\,\mathrm m$. Calcule el potencial total, la extensión de equilibrio, la primera extensión máxima y la rapidez en el equilibrio.

### 5. Dos intervalos permitidos {#ejercicio-8-5}

En el doble pozo del texto, una partícula de dos kilogramos está en $x=a$ con velocidad hacia la derecha de un metro por segundo. Calcule la energía, todos los intervalos con $U\leq E$ y los extremos del movimiento que parte de ese estado. ¿Puede visitar un punto del intervalo permitido izquierdo?

### 6. Cruzar con energía superior a la barrera {#ejercicio-8-6}

En el mismo potencial, una partícula tiene $E=5\,\mathrm J$ y cruza $x=a$ hacia la izquierda. Calcule su rapidez allí, su rapidez en el origen y los extremos exteriores permitidos. Explique por qué el origen se cruza en un tiempo finito.

### 7. Llegar al máximo con la energía justa {#ejercicio-8-7}

En el doble pozo, prepare $x=a$ y velocidad hacia la izquierda de dos metros por segundo. Determine $E$ y pruebe que el tiempo para llegar al origen es infinito. ¿Hay contradicción entre esa conclusión y la desigualdad $U(0)\leq E$?

### 8. Una detención en tiempo finito {#ejercicio-8-8}

Una partícula de dos kilogramos entra en $x=0$ con velocidad de tres metros por segundo y potencial $U(x)=(3\,\mathrm N)x$. Calcule la posición y el tiempo de la primera detención. Compruebe la convergencia de la integral temporal y determine hacia dónde continúa el movimiento.

### 9. Dos sentidos en la misma línea de energía {#ejercicio-8-9}

Para $U(x)=(4\,\mathrm{N/m})x^2$, una partícula de dos kilogramos tiene $E=4\,\mathrm J$ y se encuentra en $x=0{,}50\,\mathrm m$. Halle las dos velocidades posibles, el equilibrio y los extremos permitidos. Determine cuál extremo visita primero en cada caso. ¿Qué dato falta si sólo conocemos posición y energía?

### 10. Una cota concreta de estabilidad {#ejercicio-8-10}

Alrededor de un equilibrio escriba $q=x-x_e$ y $U-U(x_e)=kq^2/2$, con $m=2\,\mathrm{kg}$ y $k=8\,\mathrm{N/m}$. Se preparan $|q(0)|\leq0{,}05\,\mathrm m$ y $|v(0)|\leq0{,}10\,\mathrm{m/s}$. Obtenga cotas válidas para todo tiempo de $|q|$ y $|v|$. ¿Garantizan $|q|<0{,}10\,\mathrm m$ y $|v|<0{,}30\,\mathrm{m/s}$?

### 11. Salir de la vecindad de un máximo {#ejercicio-8-11}

Considere $U(q)=-(4\,\mathrm{N/m})q^2$ y $m=2\,\mathrm{kg}$. Prepare $q(0)=q_0>0$ y $v(0)=0$. Sin resolver la ecuación diferencial de forma explícita, pruebe que abandona $0\leq q<r$ para cualquier $r>q_0$. Para $q_0=0{,}001\,\mathrm m$ y $r=0{,}10\,\mathrm m$, dé una cota superior del tiempo de llegada a $r$ y explique la conclusión de inestabilidad.

### 12. Cuando la segunda derivada se anula {#ejercicio-8-12}

En una recta, clasifique el equilibrio en $q=0$ para $U_1=\beta q^4$, $U_2=-\beta q^4$, $U_3=\gamma q^3$ y $U_4=0$, con $\beta>0$ en $\mathrm{J/m^4}$ y $\gamma>0$ en $\mathrm{J/m^3}$. Distinga estabilidad frente a posición y velocidad de la denominación estática de equilibrio neutro. Justifique las inestabilidades mediante perturbaciones concretas.

### 13. Un potencial y una resistencia viscosa {#ejercicio-8-13}

Una partícula de dos kilogramos tiene $U(q)=kq^2/2$, con $k=8\,\mathrm{N/m}$, y recibe además $F_o=-bv$, con $b=1\,\mathrm{kg/s}$. En un instante $q=0{,}50\,\mathrm m$ y $v=2\,\mathrm{m/s}$. Calcule la energía mecánica, la aceleración y $dE/dt$. ¿Puede tratarse esa energía como una constante para calcular otro estado?

### 14. Preparar una partícula para cruzar la barrera {#ejercicio-8-14}

En el doble pozo, una preparación mediante un actuador comienza en reposo en $x=a$ y termina de nuevo allí con velocidad hacia la izquierda. El actuador realiza tres joules de trabajo en un caso y cinco en otro; no hay otras fuerzas adicionales. Después se desconecta. Determine si la partícula puede cruzar al pozo izquierdo y su rapidez en el origen cuando el cruce sea posible. Explique por qué se compara trabajo con una diferencia de potencial.

### 15. Una interacción atractiva que se debilita {#ejercicio-8-15}

Una partícula de un kilogramo se mueve sobre una semirrecta $r>0$ con $U(r)=-A/r$, donde $A=20\,\mathrm{J\,m}$. Parte de $r_0=2\,\mathrm m$ hacia fuera con rapidez de tres metros por segundo. Obtenga la fuerza, la energía y la distancia máxima. Halle el umbral de rapidez inicial para no tener un extremo exterior finito. No se incluye el movimiento angular ni un paso por $r=0$.

### 16. Reposo fuera del mínimo por rozamiento {#ejercicio-8-16}

Un bloque de un kilogramo sobre una mesa horizontal está unido a un resorte de $k=20\,\mathrm{N/m}$. La extensión es $x$, $\mu_s=0{,}40$ y $\mu_k=0{,}30$. Determine todas las extensiones que permiten reposo. Calcule la fricción requerida en $x=0{,}10\,\mathrm m$. Si se libera en reposo desde $x=0{,}30\,\mathrm m$, determine si puede quedarse allí y el sentido y aceleración inicial del deslizamiento que comienza.

### 17. Un umbral con incertidumbre {#ejercicio-8-17}

En una preparación del doble pozo, la energía es $E\in[3{,}90;4{,}10]\,\mathrm J$ y la altura de la barrera respecto de la misma referencia es $U_b\in[3{,}95;4{,}05]\,\mathrm J$. Trate las cotas como independientes. Acote $E-U_b$ y decida si se puede afirmar un cruce con rapidez positiva. ¿Qué desigualdad entre cotas permitiría garantizarlo para una partícula que se dirige hacia la barrera sin otros obstáculos?

### 18. Tres valores de potencial no fijan la fuerza {#ejercicio-8-18}

Se conoce $U(-a)=U(a)=4\,\mathrm J$ y $U(0)=0$, con $a=1\,\mathrm m$. Compare las funciones

$$
U_A(x)=4\,\mathrm J\left(\frac{x}{a}\right)^2,
\qquad
U_B(x)=U_A(x)+(1\,\mathrm J)\frac{x}{a}\left[\left(\frac{x}{a}\right)^2-1\right].
$$

Compruebe los tres valores y calcule la fuerza de cada modelo en el origen. ¿Permiten esas tres mediciones demostrar que el origen es un equilibrio?

### 19. Reconocer un potencial en el plano {#ejercicio-8-19}

Sean $\mathbf F_A=(\kappa y,\kappa x)$ y $\mathbf F_B=(\kappa y,0)$, con $\kappa=2\,\mathrm{N/m}$. Compruebe que $U_A=-\kappa xy$ reproduce la primera fuerza. Calcule los trabajos de ambas fuerzas de $(0,0)$ a $(2\,\mathrm m,1\,\mathrm m)$ por los dos recorridos rectangulares del capítulo 7. Para la segunda, obtenga el trabajo sobre el rectángulo cerrado recorrido primero hacia la derecha, luego arriba, izquierda y abajo, y decida si puede tener un potencial de posición en todo ese dominio.

### 20. El parámetro del potencial cambia con el tiempo {#ejercicio-8-20}

Una partícula de masa constante satisface $m\ddot x=-k(t)x$. Se elige $U(x,t)=k(t)x^2/2$, con $k$ diferenciable y positivo. Derive $d(K+U)/dt$. En un instante con $x=1\,\mathrm m$, $v=0$ y $\dot k=2\,\mathrm{N/(m\,s)}$, calcule esa tasa de cambio. Explique por qué la conservación anterior no se aplica pese a que la fuerza es el negativo de una derivada espacial del potencial en cada instante.

### 21. Un apoyo que entrega y recupera energía {#ejercicio-8-21}

Un carro de masa $m=1\,\mathrm{kg}$ se mueve sobre una guía horizontal lisa. Un resorte ideal de constante $k=4\,\mathrm{N/m}$ conecta el carro con un apoyo cuyo movimiento se prescribe desde fuera. La coordenada $X(t)$ representa la posición que tendría el carro con el resorte sin deformar; así, la extensión con signo es $x-X$ y la fuerza sobre el carro es $-k(x-X)$. Desde $t=0$ se impone $X(t)=ut$, con $u=0{,}20\,\mathrm{m/s}$, y el carro parte de $x(0)=\dot x(0)=0$. La fuerza es finita al conectar el movimiento; la preparación no comunica un impulso al carro. Suponga válida la ley lineal para $|x-X|<0{,}15\,\mathrm m$.

Obtenga la extensión y el movimiento del carro. Calcule la energía $E=K+k(x-X)^2/2$ y la potencia entregada por el apoyo. Compare los estados en $t=\pi/2\,\mathrm s$ y $t=\pi\,\mathrm s$, e identifique los intervalos de entrega y recuperación de energía durante ese primer ciclo. Compruebe el régimen del resorte y explique cómo puede ser nulo el trabajo neto del ciclo aunque haya transferencia intermedia.

## Soluciones

### 1. Cambiar el estado inicial del carro {#solucion-8-1}

En el mínimo $U(1\,\mathrm m)=-4\,\mathrm J$. La energía cinética inicial es nueve joules, de modo que $E=5\,\mathrm J$. Completar el cuadrado da

$$
U(x)=(4\,\mathrm{N/m})(x-1\,\mathrm m)^2-4\,\mathrm J.
$$

Las detenciones cumplen $(x-1\,\mathrm m)^2=9\,\mathrm J/(4\,\mathrm{N/m})=(1{,}5\,\mathrm m)^2$. Los extremos son $-0{,}50\,\mathrm m$ y $2{,}50\,\mathrm m$, ambos dentro del intervalo de validez del resorte. La velocidad inicial positiva lleva primero al extremo derecho. Al cruzar de nuevo el mínimo, la rapidez vuelve a ser tres metros por segundo, porque allí $K=E-U=9\,\mathrm J$. Puede cruzarlo en ambos sentidos; su velocidad cambia de signo entre cruces.

### 2. Una fuerza con potencial cuártico {#solucion-8-2}

La integral con signo opuesto da $U(x)=(1\,\mathrm{J/m^4})x^4$ con la referencia pedida. Entre uno y dos metros, el trabajo es $U(1)-U(2)=1\,\mathrm J-16\,\mathrm J=-15\,\mathrm J$.

La preparación tiene $E=5\,\mathrm J+1\,\mathrm J=6\,\mathrm J$. En dos metros necesitaría $K=6-16=-10\,\mathrm J$, imposible. En el sentido inicial, el primer cero de $E-U$ aparece en $x=6^{1/4}\,\mathrm m\approx1{,}565\,\mathrm m$. Allí la fuerza es negativa y no nula, por lo que se inicia un regreso. Este potencial tiene mínimo estricto en el origen pese a que su segunda derivada se anula allí.

### 3. Subir bajo gravedad uniforme {#solucion-8-3}

Al partir, $K_0=64\,\mathrm J$ y $U_0=(2\,\mathrm{kg})(10\,\mathrm{m/s^2})(2\,\mathrm m)=40\,\mathrm J$. La energía es $E=104\,\mathrm J$. En cinco metros, $U=100\,\mathrm J$, por lo que $K=4\,\mathrm J$ y la rapidez es dos metros por segundo. Durante el primer paso por esa altura la velocidad sigue apuntando hacia arriba.

El máximo satisface $mgy_{\max}=104\,\mathrm J$, de donde $y_{\max}=5{,}20\,\mathrm m$. Si se cambia a $\widetilde U=mg(y-2\,\mathrm m)$, se resta cuarenta joules tanto a $U$ como a $E$. La nueva energía es sesenta y cuatro joules; la subida máxima respecto del lanzamiento es $3{,}20\,\mathrm m$. Las alturas y rapideces físicas no cambian.

### 4. La mayor extensión no es el equilibrio {#solucion-8-4}

Como $y$ crece hacia abajo, la gravedad tiene potencial $-mgy$. Con $U(0)=0$,

$$
U(y)=\frac12ky^2-mgy
=(50\,\mathrm{N/m})y^2-(20\,\mathrm N)y.
$$

La fuerza se anula en $y_e=mg/k=0{,}20\,\mathrm m$. La liberación desde el reposo no da $E=U(y_e)$, sino $E=U(0)=0$. El segundo cero de $U$ está en $y_t=2mg/k=0{,}40\,\mathrm m$, la primera extensión máxima. Ambos puntos están dentro del régimen lineal declarado.

En el equilibrio, $U(y_e)=-2\,\mathrm J$, así que $K=2\,\mathrm J$ y la rapidez es $\sqrt2\,\mathrm{m/s}$. Igualar $mg=ky$ identifica el equilibrio de fuerzas, no una detención de esta historia. En la extensión máxima, el resorte tira hacia arriba con cuarenta newtons mientras el peso tira hacia abajo con veinte; esa fuerza neta inicia el retorno.

### 5. Dos intervalos permitidos {#solucion-8-5}

En $x=a$, $U=0$ y $K=(2\,\mathrm{kg})(1\,\mathrm{m/s})^2/2=1\,\mathrm J$. Por tanto, $E=1\,\mathrm J$. La desigualdad $U\leq E$ equivale a

$$
\left|\left(\frac{x}{a}\right)^2-1\right|\leq\frac12,
$$

es decir, $a/\sqrt2\leq|x|\leq a\sqrt{3/2}$. Existen los dos intervalos cerrados

$$
[-a\sqrt{3/2},-a/\sqrt2]\ \cup\ [a/\sqrt2,a\sqrt{3/2}].
$$

La preparación está en el derecho. Visita primero su extremo exterior por llevar velocidad positiva y permanece entre esos dos extremos. Sus ceros de energía cinética tienen fuerza no nula y son retornos ordinarios. No alcanza el intervalo izquierdo: tendría que atravesar el intervalo central prohibido. La palabra «permitido» por la desigualdad no significa accesible desde cualquier estado con esa energía.

### 6. Cruzar con energía superior a la barrera {#solucion-8-6}

En el mínimo derecho, $K=5\,\mathrm J$, por lo que la rapidez es $\sqrt5\,\mathrm{m/s}$ y la velocidad apunta a la izquierda. En el origen, $K=5-4=1\,\mathrm J$ y la rapidez es un metro por segundo, todavía hacia la izquierda en el primer cruce.

Los extremos cumplen $[(x/a)^2-1]^2=5/4$. La solución con $(x/a)^2=1-\sqrt5/2$ es negativa y se descarta; los extremos reales son

$$
x_\pm=\pm a\sqrt{1+\frac{\sqrt5}{2}}.
$$

No hay barrera intermedia con $U>E$. Además, la rapidez es continua y positiva alrededor del origen: no aparece una divergencia de $\int dx/|v|$ allí. Desde $a$ hasta cero, la energía cinética es al menos un joule, de modo que la rapidez es al menos un metro por segundo y el tiempo de ese tramo es finito.

### 7. Llegar al máximo con la energía justa {#solucion-8-7}

La preparación da $E=(2\,\mathrm{kg})(2\,\mathrm{m/s})^2/2=4\,\mathrm J=U_b$. En el lado derecho, con $\xi=x/a$, la rapidez vale $\sqrt{2U_b/m}\,\xi\sqrt{2-\xi^2}$. El sentido inicial selecciona velocidad negativa.

El tiempo hasta $\xi>0$ desde $\xi_0=1$ es la integral del texto. Para $0<\eta\leq1$ se tiene $\sqrt{2-\eta^2}\leq\sqrt2$, así que su integrando es al menos $1/(\sqrt2\eta)$. La integral de esta cota diverge al aproximarse a cero. Por tanto, ningún tiempo finito lleva al origen.

La desigualdad $U(0)\leq E$ es necesaria, pero no afirma un tiempo de llegada. El estado $(0,0)$ es por sí mismo otro movimiento posible: el equilibrio superior exacto. La historia preparada en $x=a$ se aproxima a ese estado sin coincidir con él en tiempo finito.

![La posición positiva disminuye hacia el origen sin alcanzarlo en ningún tiempo finito.](/assets/books/fispm/r20261021/potencial_tiempo_critico.svg){.fpm-v04-figure}

*Figura 8.6.* Aproximación crítica para la masa y el doble pozo del problema. El eje horizontal es tiempo, a diferencia de los diagramas de energía anteriores. El extremo dibujado de la curva todavía tiene posición positiva; el recorte de la gráfica no representa un instante de llegada al origen.

### 8. Una detención en tiempo finito {#solucion-8-8}

La energía inicial es nueve joules. Como $U=3\,\mathrm N\,x$, el primer cero de $K=9\,\mathrm J-(3\,\mathrm N)x$ ocurre en $x_t=3\,\mathrm m$. La fuerza constante es $-3\,\mathrm N$ y la aceleración $-1{,}5\,\mathrm{m/s^2}$. Por Newton, el reposo se alcanza en dos segundos.

La comprobación energética utiliza

$$
\Delta t=\int_0^{3\,\mathrm m}\frac{dx}{\sqrt{9\,\mathrm{m^2/s^2}-(3\,\mathrm{m/s^2})x}}=2\,\mathrm s.
$$

El integrando tiene una singularidad de tipo $(x_t-x)^{-1/2}$, cuya integral converge. En el extremo la fuerza permanece hacia la izquierda, así que comienza el regreso. Una rapidez nula no implica fuerza nula; en este ejemplo tampoco significa un estado de equilibrio.

### 9. Dos sentidos en la misma línea de energía {#solucion-8-9}

En medio metro, $U=1\,\mathrm J$ y $K=3\,\mathrm J$. Las dos velocidades son $v=\pm\sqrt3\,\mathrm{m/s}$. El equilibrio es $x=0$ y los extremos de energía son $x=\pm1\,\mathrm m$.

Con velocidad positiva se visita primero el extremo derecho; con velocidad negativa, el izquierdo. No hay otros ceros interiores de $K$ que puedan cambiar el sentido antes. La posición y la energía no distinguen las dos preparaciones: falta el signo de la velocidad. En el equilibrio podría además haber movimiento con rapidez máxima; «posición de equilibrio» identifica dónde puede existir reposo, no obliga a que todo paso por ella sea reposo.

### 10. Una cota concreta de estabilidad {#solucion-8-10}

El incremento de energía respecto del mínimo satisface

$$
E-U(x_e)\leq\frac12(2\,\mathrm{kg})(0{,}10\,\mathrm{m/s})^2
+\frac12(8\,\mathrm{N/m})(0{,}05\,\mathrm m)^2
=0{,}02\,\mathrm J.
$$

Como cada término de $mv^2/2+kq^2/2$ es no negativo, la conservación da $|q|\leq\sqrt{2(0{,}02\,\mathrm J)/k}=\sqrt{0{,}005}\,\mathrm m\approx0{,}07071\,\mathrm m$ y $|v|\leq\sqrt{2(0{,}02\,\mathrm J)/m}=\sqrt{0{,}02}\,\mathrm{m/s}\approx0{,}14142\,\mathrm{m/s}$ para todo tiempo. Son menores que las dos tolerancias pedidas.

Controlar sólo la posición inicial no habría bastado. Una velocidad inicial grande puede aportar una energía cinética grande incluso en $q=0$ y producir una excursión muy extensa. La prueba del mínimo estricto necesita la cercanía del estado completo.

![El rectángulo de preparaciones iniciales está dentro de una elipse de energía, y ésta queda dentro de las tolerancias de posición y velocidad.](/assets/books/fispm/r20261021/potencial_estado.svg){.fpm-v04-figure}

*Figura 8.7.* Cada punto del plano representa un estado $(q,v)$. Las dos coordenadas tienen unidades y escalas distintas. La región de energía no mayor de $0{,}02\,\mathrm J$ encierra todas las preparaciones dadas y controla su evolución posterior; no se afirma que los movimientos recorran el borde de los rectángulos.

### 11. Salir de la vecindad de un máximo {#solucion-8-11}

La fuerza es $(8\,\mathrm{N/m})q$ y la ecuación da $\ddot q=(4\,\mathrm{s^{-2}})q$. Desde $q_0>0$ y reposo, la aceleración es positiva y $q$ crece. Mientras permanezca antes de $r$,

$$
q(t)\geq q_0+(2\,\mathrm{s^{-2}})q_0t^2.
$$

Por tanto, el tiempo de llegada a $r$ no puede superar

$$
t_r\leq\sqrt{\frac{r/q_0-1}{2\,\mathrm{s^{-2}}}}.
$$

Para los datos, la cota es $\sqrt{49{,}5}\,\mathrm s\approx7{,}036\,\mathrm s$. Es una cota, no el tiempo exacto. Al elegir $q_0$ cada vez menor la cota aumenta, pero para cada $q_0>0$ sigue siendo finita. Una misma vecindad se abandona mediante datos iniciales arbitrariamente próximos al equilibrio. La definición de estabilidad exige control para todo tiempo y por eso falla.

### 12. Cuando la segunda derivada se anula {#solucion-8-12}

En los cuatro modelos $U'(0)=0$ y $U''(0)=0$. Para $U_1$, el mínimo es estricto, por lo que el teorema garantiza estabilidad frente a posición y velocidad. La restauración es débil cerca del origen, pero la barrera energética basta para la conclusión.

Para $U_2$, prepare $q_0>0$ y reposo. La fuerza es $4\beta q^3>0$ y, mientras $q\geq q_0$, la aceleración es al menos $4\beta q_0^3/m$. La cota $q(t)\geq q_0+(2\beta q_0^3/m)t^2$ obliga a salir de cualquier intervalo derecho fijo en tiempo finito. Como $q_0$ puede ser arbitrariamente pequeño, el equilibrio es inestable.

Para $U_3$, la fuerza $-3\gamma q^2$ apunta hacia la izquierda a ambos lados. Elija $q(0)=-q_0<0$ y reposo, con $q_0>0$. La partícula empieza a alejarse hacia la izquierda; mientras $q\leq-q_0$, su aceleración es como máximo $-3\gamma q_0^2/m$. De nuevo una cota cuadrática en el tiempo obliga a abandonar una vecindad izquierda fija. El equilibrio es inestable aunque no sea un máximo local.

Para $U_4$, una traslación con nueva velocidad inicial cero deja otro reposo: es el caso llamado neutro en la clasificación estática. Sin embargo, la preparación $q(0)=0$, $v(0)=v_0\ne0$ produce $q=v_0t$ y acaba por abandonar cualquier intervalo acotado, por pequeño que sea $v_0$. El estado individual es inestable con la definición dinámica del capítulo. El criterio de segunda derivada nula no identifica un comportamiento único.

### 13. Un potencial y una resistencia viscosa {#solucion-8-13}

La energía cinética vale cuatro joules y el potencial un joule: $E=5\,\mathrm J$. La fuerza elástica es menos cuatro newtons y la resistencia menos dos, ambas hacia la izquierda. La aceleración es $(-6\,\mathrm N)/(2\,\mathrm{kg})=-3\,\mathrm{m/s^2}$.

El balance da $dE/dt=-bv^2=-4\,\mathrm W$. Como comprobación, $dK/dt=mv\ddot q=-12\,\mathrm W$ y $dU/dt=kqv=+8\,\mathrm W$; su suma es menos cuatro watts. El potencial está creciendo en ese instante porque la partícula se aleja del mínimo, pero la energía mecánica total disminuye. No podemos conservar los cinco joules para otro estado sin contabilizar el trabajo posterior de la resistencia.

### 14. Preparar una partícula para cruzar la barrera {#solucion-8-14}

Al principio $K=0$ y $U(a)=0$, de modo que $E_i=0$. El trabajo del actuador cambia la energía mecánica en tres o cinco joules. Al terminar otra vez en $x=a$, ese incremento está en la energía cinética, pues el potencial tiene el mismo valor inicial y final.

Con $E=3\,\mathrm J$, la barrera de cuatro joules deja un intervalo central prohibido; no hay cruce. Con $E=5\,\mathrm J$ y velocidad hacia la izquierda, el movimiento sí cruza el origen con $K=1\,\mathrm J$ y rapidez de un metro por segundo. Se compara el trabajo con $U(0)-U(a)$, que no cambia si se añade una constante a todo el potencial. Compararlo con un valor absoluto de $U(0)$ sin declarar la referencia podría cambiar falsamente la conclusión.

### 15. Una interacción atractiva que se debilita {#solucion-8-15}

La derivada es $U'=A/r^2$, así que $F_r=-A/r^2$ apunta hacia la fuente. La energía inicial es $E=(1\,\mathrm{kg})(3\,\mathrm{m/s})^2/2-20\,\mathrm{J\,m}/(2\,\mathrm m)=-5{,}5\,\mathrm J$. Al salir, $U$ aumenta y la rapidez disminuye. La detención cumple $-A/r_{\max}=E$, de donde $r_{\max}=40/11\,\mathrm m\approx3{,}636\,\mathrm m$.

Para no encontrar un extremo exterior finito se requiere $E\geq0$, que en la preparación dada equivale a $v_0\geq\sqrt{2A/(mr_0)}=\sqrt{20}\,\mathrm{m/s}$. En la igualdad la rapidez tiende a cero cuando $r$ tiende a infinito, sin anularse a una distancia finita. Esto no afirma una llegada a infinito en tiempo finito. Para $E>0$, la rapidez tiene un límite positivo hacia fuera. Todo el argumento se limita al movimiento radial sobre $r>0$.

### 16. Reposo fuera del mínimo por rozamiento {#solucion-8-16}

La normal es diez newtons y la fricción estática puede tener módulo hasta cuatro. Mantener reposo exige $f=kx$, de sentido contrario a la fuerza del resorte. Es admisible exactamente cuando $|kx|\leq4\,\mathrm N$, es decir, $|x|\leq0{,}20\,\mathrm m$.

En $x=0{,}10\,\mathrm m$ se necesitan dos newtons hacia la derecha, admisibles. El bloque está en reposo aunque no esté en el mínimo del potencial elástico. En $x=0{,}30\,\mathrm m$ harían falta seis newtons estáticos, imposibles. Empieza a deslizar hacia la izquierda; la fricción cinética pasa a tres newtons hacia la derecha. La fuerza neta inicial del régimen deslizante es $-6+3=-3\,\mathrm N$ y su aceleración $-3\,\mathrm{m/s^2}$. La ecuación $U'=0$ sola habría ignorado la interacción adicional que permite todo el intervalo de reposos.

![La fricción requerida kx sólo pertenece al intervalo estático permitido cuando la extensión está entre menos y más veinte centímetros.](/assets/books/fispm/r20261021/potencial_reposo_rozamiento.svg){.fpm-v04-figure}

*Figura 8.8.* La banda horizontal corresponde a fuerzas entre menos y más cuatro newtons. Su intersección con $f_{\mathrm{requerida}}=kx$ determina el intervalo de reposos. El modelo admite los extremos de la banda; superarlos obliga a revisar el régimen.

### 17. Un umbral con incertidumbre {#solucion-8-17}

Restar las cotas en los sentidos correspondientes da

$$
E-U_b\in[3{,}90-4{,}05;\ 4{,}10-3{,}95]\,\mathrm J
=[-0{,}15;0{,}15]\,\mathrm J.
$$

Los datos admiten energías por debajo, por encima y exactamente en el umbral. No permiten afirmar un cruce con rapidez positiva. Para garantizarlo con estas hipótesis se necesita $E_{\min}>U_{b,\max}$, además del sentido inicial hacia la barrera y de la ausencia de otros límites del recorrido. La igualdad entre las cotas no basta: la preparación crítica puede aproximarse al máximo sólo en tiempo infinito. Las cotas se refieren a una misma referencia de energía; un desplazamiento común de ese cero no cambia la comparación.

### 18. Tres valores de potencial no fijan la fuerza {#solucion-8-18}

El término añadido a $U_A$ se anula en $x=-a,0,a$, de modo que ambos modelos reproducen los tres valores. Sus derivadas en cero son distintas. Para $U_A$, $U_A'(0)=0$ y $F_A(0)=0$. El término añadido tiene derivada $(1\,\mathrm J)[3(x/a)^2-1]/a$, así que $U_B'(0)=-1\,\mathrm J/a$ y $F_B(0)=+1\,\mathrm N$.

Por tanto, las mediciones finitas indicadas no demuestran equilibrio en el origen. Permiten modelos que coinciden en esos puntos y tienen pendientes diferentes entre ellos. Para inferir la fuerza local harían falta más información sobre la función, un modelo de interpolación justificado o mediciones dinámicas. Elegir una parábola que ajuste los tres valores no la convierte en una predicción independiente de esos mismos datos.

### 19. Reconocer un potencial en el plano {#solucion-8-19}

Las derivadas de $U_A=-\kappa xy$ son $\partial_xU_A=-\kappa y$ y $\partial_yU_A=-\kappa x$, de modo que su negativo reproduce ambas componentes de $\mathbf F_A$. El trabajo de cero al punto final es $-\Delta U_A=\kappa(2\,\mathrm m)(1\,\mathrm m)=4\,\mathrm J$.

Por el recorrido horizontal y luego vertical, el primer tramo de $\mathbf F_A$ da cero porque $y=0$; el segundo tiene $F_y=\kappa(2\,\mathrm m)=4\,\mathrm N$ y aporta cuatro joules. Por el orden contrario, el tramo vertical inicial da cero porque $x=0$ y el horizontal superior aporta también cuatro joules. La coincidencia aquí está justificada por el potencial explícito, no sólo por haber comprobado dos caminos.

Para $\mathbf F_B$, el recorrido horizontal inferior y luego vertical da cero; el vertical inicial y luego horizontal superior da cuatro joules. En el rectángulo cerrado indicado, sólo el tramo superior hacia la izquierda contribuye: $W=-4\,\mathrm J$. Si existiera un potencial en todo ese dominio, su diferencia entre el inicio y el final del recorrido cerrado sería cero, contradiciendo el trabajo calculado. Por tanto, no existe ese potencial global para la segunda fuerza.

### 20. El parámetro del potencial cambia con el tiempo {#solucion-8-20}

La regla del producto y la ecuación de Newton dan

$$
\frac{d}{dt}\left(\frac12mv^2+\frac12k(t)x^2\right)
=mv\dot v+k(t)xv+\frac12\dot k(t)x^2
=\frac12\dot k(t)x^2.
$$

Los dos primeros términos se cancelan, pero queda el cambio explícito del parámetro. Con los datos indicados la tasa es $1\,\mathrm{J/s}=1\,\mathrm W$. La potencia de la fuerza sobre la partícula es cero en ese instante porque $v=0$, mientras cambia el valor del potencial elegido.

El teorema de conservación suponía que $U$ no dependía explícitamente del tiempo. Aquí un agente modifica el parámetro del modelo y esa hipótesis falla. La identidad obtenida corresponde a la función $U(x,t)$ especificada y obliga a contabilizar esa modificación al interpretar el sistema ampliado. Ser el negativo de una derivada espacial en cada instante no basta para conservar $K+U$ a lo largo de una evolución con parámetros variables.

### 21. Un apoyo que entrega y recupera energía {#solucion-8-21}

La fuerza depende de la separación respecto del apoyo, de modo que elegimos esa separación como incógnita: $q=x-X$. Como $\ddot X=0$ para $t>0$, Newton da $\ddot q+\omega^2q=0$, con $\omega=\sqrt{k/m}=2\,\mathrm{s^{-1}}$. Sus datos son $q(0)=0$ y $\dot q(0)=-u$. La solución es

$$
q(t)=-\frac{u}{\omega}\sin(\omega t),\qquad
x(t)=ut-\frac{u}{\omega}\sin(\omega t),\qquad
\dot x(t)=u[1-\cos(\omega t)].
$$

Estas fórmulas se comprueban derivando: $m\ddot x=mu\omega\sin(\omega t)=-kq$, y en cero se recuperan posición y velocidad nulas. La extensión tiene módulo máximo $u/\omega=0{,}10\,\mathrm m$, dentro del intervalo lineal declarado. El movimiento ideal del apoyo está prescrito; la fuerza necesaria para producir su cambio inicial de velocidad pertenece a ese mecanismo externo.

Sustituir en las dos reservas de energía da

$$
\begin{aligned}
E(t)&=\frac12mu^2[1-\cos(\omega t)]^2
      +\frac12mu^2\sin^2(\omega t)\\
&=mu^2[1-\cos(\omega t)].
\end{aligned}
$$

La potencia del apoyo se obtiene manteniendo fija $x$ al derivar el potencial:

$$
P_{\mathrm{apoyo}}=-kq\dot X
=mu^2\omega\sin(\omega t)=\frac{dE}{dt}.
$$

En $t=\pi/2\,\mathrm s$, la extensión vuelve a cero, el carro lleva velocidad $2u=0{,}40\,\mathrm{m/s}$ y $E=2mu^2=0{,}08\,\mathrm J$. Su posición es $x=\pi/10\,\mathrm m$. En $t=\pi\,\mathrm s$, la extensión y la velocidad del carro son cero y $E=0$, aunque carro y apoyo han avanzado hasta $x=X=\pi/5\,\mathrm m$.

Durante la primera mitad, $0<t<\pi/2\,\mathrm s$, la potencia es positiva; durante la segunda, $\pi/2\,\mathrm s<t<\pi\,\mathrm s$, es negativa. El agente entrega ocho centésimas de joule y después las recupera. La integral del ciclo vale cero porque las energías extremas coinciden. La identidad instantánea conserva la información sobre los intercambios interiores que esa comparación de extremos resume.

![La energía crece hasta ocho centésimas de joule y vuelve a cero, mientras la potencia del apoyo cambia de positiva a negativa a mitad del ciclo.](/assets/books/fispm/r20261021/potencial_apoyo_movil.svg){.fpm-v04-figure}

*Figura 8.9.* La energía corresponde al carro y al resorte ideal. La potencia positiva entrega energía a ese conjunto y la negativa la devuelve al mecanismo que mueve el apoyo. Las ordenadas tienen unidades distintas y comparten el mismo reloj. El área con signo de la potencia da el cambio de energía; las áreas de ambos medios ciclos se compensan.

## Lecturas de apoyo

Sears y Zemansky, *Física universitaria*, volumen 1, Young y Freedman, 13.ª edición, §§7.4–7.5, pp. 225–229, permite cotejar la relación entre fuerza y pendiente del potencial y la lectura de diagramas de energía. Serway y Jewett, *Física para ciencias e ingeniería*, volumen 1, 10.ª edición española, §§7.8–7.9, pp. 171–174, desarrolla la relación fuerza–potencial y la clasificación elemental del equilibrio. La definición dinámica utilizada aquí precisa las perturbaciones admitidas y distingue el mínimo estricto de una región plana.

Spivak, *Physics for Mathematicians. Mechanics I*, capítulo 6, pp. 213–215, destaca el estado de reposo y las perturbaciones de posición y velocidad al discutir equilibrio y estabilidad. Nuestro tratamiento se limita a la recta y construye el argumento de barrera energética sin usar el formalismo general de restricciones ni criterios multidimensionales antes de introducirlos. Los desarrollos, datos y ejercicios son propios; el cotejo es selectivo y no una auditoría completa de las obras.

---

[← 7. Trabajo y energía cinética](fisica-para-matematicos-07-trabajo-y-energia-cinetica.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [9. Impulso, colisiones y centro de masa →](fisica-para-matematicos-09-impulso-colisiones-y-centro-de-masa.md)
