---
title: "Trabajo, potencia y energía cinética"
subtitle: "Física para matemáticos · Tomo I · Capítulo 12"
author: "A. Peña"
description: "Capítulo 12 del Tomo I de Física para matemáticos, con ejercicios y soluciones desarrolladas."
content-id: MA-BCH-0352
source-id: FISPM-T1-C12
editorial-id: FPM-I-12
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
date-modified: 2026-10-17
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0351"]
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

[Capítulo 11](fisica-para-matematicos-capitulo-11-restricciones-elementales-y-grados-de-libertad.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [Capítulo 13](fisica-para-matematicos-capitulo-13-energia-potencial-fuerzas-conservativas-y-estabilidad.md)

[]{#fispm-c12-trabajo-potencia-y-energuxeda-cinuxe9tica}

Newton relaciona la fuerza resultante con el cambio de velocidad. En este capítulo extraeremos de esa relación una igualdad escalar que permite comparar rapidez y trabajo a lo largo de una trayectoria. Ganaremos una forma de calcular ciertos resultados sin reconstruir primero toda la historia temporal; habrá que reconocer también qué información se pierde al pasar de vectores a escalares.

[]{#fuerza-desplazamiento-y-trabajo-constante}

[]{#fispm-t1-c12-s01}

[]{#fpm-i-12-s01}

## 12.1. Fuerza, desplazamiento y trabajo constante {#fispm-c12-fuerza-desplazamiento-y-trabajo-constante}

Empujar un cuerpo no produce el mismo efecto sobre su rapidez en cualquier dirección. Una fuerza puede acompañar el movimiento, oponerse a él o desviarlo sin cambiar instantáneamente la rapidez. El producto escalar del capítulo 4 permite distinguir esas situaciones. Para comenzar, tomemos una fuerza constante y un tramo recto de desplazamiento $\Delta\mathbf r$.[^1]

[]{#fig:I-12-N01}

<figure id="fig-fpm-v04-i-12-n01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-12-N01.svg" class="lightbox" data-gallery="fpm-v04-c12"><img src="/assets/books/fispm/v04/I-12-N01.svg" alt="Trabajo y proyección. Diagrama del capítulo 12; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="299" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 12.1.** Sólo la componente paralela al desplazamiento contribuye al trabajo de una fuerza constante. La flecha discontinua es un desplazamiento y no una fuerza adicional. Véase §[12.1](#fispm-c12-fuerza-desplazamiento-y-trabajo-constante).

</figcaption>

</figure>

[]{#fispm-t1-c12-d0001}

**Definición 12.1 --- Trabajo de una fuerza constante en un tramo recto.** El trabajo de la fuerza $\mathbf F$ sobre el punto material durante ese desplazamiento es el escalar

$$W=\mathbf F\cdot\Delta\mathbf r.$$

Para magnitudes no nulas, $W=|\mathbf F|\,|\Delta\mathbf r|\cos\alpha$, donde $\alpha$ es el ángulo entre ambos vectores. La definición incluye trabajo cero si uno de ellos es nulo.

El signo se refiere a la contribución de esa fuerza durante el desplazamiento elegido. Una fuerza en el sentido del tramo tiene trabajo positivo; una fuerza contraria tiene trabajo negativo. Si es perpendicular al tramo, su trabajo es cero. No estamos identificando todavía el trabajo de una fuerza con el cambio de rapidez: sobre el cuerpo pueden actuar otras fuerzas que también hagan trabajo.

La dimensión de trabajo es fuerza por longitud, $ML^2T^{-2}$. Su unidad SI es el joule: $1\,\mathrm J=1\,\mathrm{N\,m}=1\,\mathrm{kg\,m^2\,s^{-2}}$. Que una cantidad tenga esa dimensión no demuestra que sea trabajo; la definición necesita el producto escalar y un receptor. La dimensión permite comprobar un cálculo una vez declarada la magnitud.

«Trabajo» tiene aquí un significado físico preciso. Sostener un objeto inmóvil puede resultar fatigoso para una persona, pero la fuerza ejercida sobre ese punto material realiza trabajo mecánico nulo durante un intervalo en que su posición no cambia. La actividad fisiológica de quien lo sostiene requiere otro sistema y otras formas de intercambio. Tampoco se mide trabajo contando cuánto tiempo se aplica una fuerza: una fuerza puede mantenerse mucho tiempo sin desplazamiento del receptor.

[]{#fispm-t1-c12-p0001}

**Proposición 12.1 --- Trabajo constante sobre un recorrido poligonal.** Si la misma fuerza constante $\mathbf F$ actúa durante todos los tramos de un recorrido poligonal de $A$ a $B$, la suma de sus trabajos es

$$W=\mathbf F\cdot(\mathbf r_B-\mathbf r_A).$$

No depende de la longitud total de ese recorrido.

**Demostración.** Sean $\mathbf r_0=\mathbf r_A,\ldots,\mathbf r_n=\mathbf r_B$ los vértices. La suma es $\sum_{j=1}^n\mathbf F\cdot(\mathbf r_j-\mathbf r_{j-1})$. Por linealidad del producto escalar, es $\mathbf F\cdot\sum_{j=1}^n(\mathbf r_j-\mathbf r_{j-1})$. La suma interior telescopa y deja $\mathbf r_B-\mathbf r_A$. $\square$

La hipótesis de una fuerza constante es decisiva. No se puede sacar de la suma una fuerza que cambie de dirección o magnitud entre tramos. En particular, una resistencia siempre opuesta al movimiento cambia de dirección cuando el cuerpo regresa, aunque su magnitud sea constante. Ese caso no cumple proposición 12.1 y no tiene trabajo neto necesariamente nulo en una ida y vuelta.

Proposición 12.1 distingue desplazamiento neto y distancia recorrida. La fuerza fija $F e_x$ hace trabajo $F\Delta x$, no $F$ multiplicado por toda la distancia. Un tramo vertical contribuye cero; un tramo hacia la izquierda contribuye negativamente si $F>0$. Un rodeo puede aumentar la distancia y dejar igual la suma de trabajo de esta fuerza concreta.

[]{#fispm-t1-c12-mp0001}

**Principio metodológico 12.1 --- Identificar fuerza, receptor y tramo.** Antes de multiplicar fuerza por distancia, escribe los vectores o la componente en el sentido del desplazamiento. Declara si la fuerza permanece constante en todo el recorrido. Conserva el signo y distingue trabajo de una contribución de trabajo total.

[]{#ejercicios}

### 12.1.1. Ejercicios {#fispm-c12-ejercicios}

[]{#fispm-t1-c12-e0001}

[]{#fispm-t1-c12-e0012}

**Ejercicio 12.1.** Una fuerza constante $(3,-4)\,\mathrm N$ actúa sobre una partícula que se desplaza $(2,1)\,\mathrm m$. Calcula el trabajo y compara con multiplicar las magnitudes.

**Solución.** El producto escalar da $W=3(2)-4(1)=2\,\mathrm J$. El producto de magnitudes sería $5\sqrt5\,\mathrm J$, y no coincide porque los vectores no son paralelos. El desplazamiento contiene una contribución horizontal de $6\,\mathrm J$ y una vertical de $-4\,\mathrm J$. Su suma es positiva; no se puede inferir aún el cambio de energía cinética sin conocer el trabajo de las demás fuerzas.

[]{#fispm-t1-c12-e0002}

**Ejercicio 12.2.** La fuerza constante $(5,0)\,\mathrm N$ actúa durante el recorrido $(0,0)\to(0,3)\to(4,3)\to(4,0)$, con coordenadas en metros. Calcula el trabajo por tramos y por desplazamiento neto. ¿Qué ocurriría en un recorrido cerrado?

**Solución.** Los tramos dan $0$, $20$ y $0$ joules. El desplazamiento neto es $(4,0)\,\mathrm m$ y proposición 12.1 da también $20\,\mathrm J$. La distancia total es $10\,\mathrm m$, pero multiplicarla por $5\,\mathrm N$ produciría un resultado incorrecto. En cualquier polígono cerrado bajo esa misma fuerza constante, el desplazamiento neto es cero y el trabajo de la fuerza es cero. Esto no afirma que el cuerpo no se haya movido ni que cada tramo tenga trabajo nulo.

[]{#trabajo-de-una-fuerza-variable-en-una-dimensión}

[]{#fispm-t1-c12-s02}

[]{#fpm-i-12-s02}

## 12.2. Trabajo de una fuerza variable en una dimensión {#fispm-c12-trabajo-de-una-fuerza-variable-en-una-dimensiuxf3n}

Cuando la fuerza cambia a lo largo de una línea, una sola multiplicación no incorpora la variación. Dividimos el recorrido en pequeños tramos, multiplicamos en cada uno la componente firmada de fuerza por el desplazamiento firmado y pasamos a una integral. Las herramientas son las sumas y el teorema fundamental del cálculo de M2--M3; no hace falta introducir aún campos potenciales.[^2]

[]{#fig:I-12-R01}

<figure id="fig-fpm-v04-i-12-r01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-12-R01.svg" class="lightbox" data-gallery="fpm-v04-c12"><img src="/assets/books/fispm/v04/I-12-R01.svg" alt="El trabajo es un área firmada. Diagrama del capítulo 12; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="403" height="353" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 12.2.** Con $F(x)=1+x$ y desplazamiento desde $0$ hasta $2$, el trabajo normalizado vale $\int_0^2(1+x)\,dx=4$. Invertir el sentido de integración cambia su signo. Véase §[12.2](#fispm-c12-trabajo-de-una-fuerza-variable-en-una-dimensiuxf3n).

</figcaption>

</figure>

[]{#fig:I-12-N02}

<figure id="fig-fpm-v04-i-12-n02" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-12-N02.svg" class="lightbox" data-gallery="fpm-v04-c12"><img src="/assets/books/fispm/v04/I-12-N02.svg" alt="Trabajo como integral. Diagrama del capítulo 12; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="423" height="253" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 12.3.** Para $F(x)=kx$ y $0\le x\le a$, el área bajo la gráfica es $ka^2/2$. Los ejes normalizados son $x/a$ y $F/(ka)$. Véase §[12.2](#fispm-c12-trabajo-de-una-fuerza-variable-en-una-dimensiuxf3n).

</figcaption>

</figure>

[]{#fispm-t1-c12-d0002}

**Definición 12.2 --- Trabajo unidimensional de una fuerza de posición.** Para una componente de fuerza continua $F(x)$ sobre una línea, el trabajo orientado desde $x_a$ hasta $x_b$ es

$$W_{a\to b}=\int_{x_a}^{x_b}F(\xi)\,d\xi.$$

La variable $\xi$ identifica el argumento de integración y se distingue de los extremos. Los límites fijan la orientación; no se ordenan por tamaño para hacer positivo el resultado.

Si $x_b>x_a$, una fuerza negativa aporta trabajo negativo. Si el desplazamiento se invierte, el signo cambia para ese mismo campo $F(x)$. El área entre la gráfica y el eje horizontal sólo coincide con el trabajo cuando se conservan sus signos. Sumar áreas geométricas positivas borraría la diferencia entre acelerar y frenar.

Para una fuerza lineal $F(x)=f_0+kx$, con $f_0$ de dimensión fuerza y $k$ de dimensión fuerza por longitud, $W_{a\to b}=f_0(x_b-x_a)+\frac{k}{2}(x_b^2-x_a^2).$ En un tramo con fuerza variable, evaluar sólo $F(x_b)$ y multiplicar por $x_b-x_a$ no es exacto en general. Para esa función lineal, la media de los valores extremos sí produce la integral porque el área firmada es la de un trapecio. Esa propiedad pertenece a la forma lineal; no se transfiere a cualquier gráfica.

[]{#fispm-t1-c12-p0002}

**Proposición 12.2 --- Trabajo de posición y retrocesos en una línea.** Si $F$ es continua y $x(t)$ es una historia continuamente diferenciable, entonces

$$\int_{t_a}^{t_b}F(x(t))\dot x(t)\,dt=\int_{x(t_a)}^{x(t_b)}F(\xi)\,d\xi,$$

aunque $x(t)$ tenga retrocesos o instantes con $\dot x=0$.

**Demostración.** Fijemos una referencia $x_*$ y sea $G(x)=\int_{x_*}^{x}F(\xi)\,d\xi$. Por el teorema fundamental, $G'=F$. La regla de la cadena da $\frac d{dt}G(x(t))=F(x(t))\dot x(t)$. Integrar en el tiempo produce $G(x(t_b))-G(x(t_a))$, igual a la integral entre las posiciones extremas. No se divide por $\dot x$ ni se exige que $x$ sea invertible como función del tiempo. $\square$

El resultado usa que la componente de fuerza es una función fija de la posición. Una resistencia que cambie de signo con la velocidad no es ese mismo $F(x)$. Una fuerza controlada externamente que varíe con el tiempo tampoco queda descrita por la gráfica única usada en la definición 12.2. En esos casos habrá que conservar la historia temporal en la integral.

El argumento de la primitiva es aquí una herramienta de cálculo. La generalización del trabajo independiente del camino en varias dimensiones, su relación con energía potencial y las condiciones de integrabilidad se estudiarán en el capítulo 13. Una línea con una función continua no justifica anunciar el mismo resultado para cualquier campo vectorial.

[]{#fispm-t1-c12-mp0002}

**Principio metodológico 12.2 --- Integrar con orientación.** Usa la componente firmada de fuerza y los extremos en el orden del movimiento. Para retrocesos, identifica si la fuerza sigue siendo el mismo campo de posición; sólo entonces se cancelan las contribuciones de ida y vuelta. No sustituyas una integral por fuerza final multiplicada por distancia sin una hipótesis que lo permita.

[]{#ejercicios-1}

### 12.2.1. Ejercicios {#fispm-c12-ejercicios-1}

[]{#fispm-t1-c12-e0003}

**Ejercicio 12.3.** Sobre una línea, $F(x)=kx$ con $k=4\,\mathrm{N\,m^{-1}}$. Calcula el trabajo desde $1\,\mathrm m$ hasta $3\,\mathrm m$ y en el recorrido inverso. Compara con usar la fuerza final en el primer tramo.

**Solución.** $W_{1\to3}=\tfrac42(3^2-1^2)=16\,\mathrm J$ y $W_{3\to1}=-16\,\mathrm J$. Usar $F(3)=12\,\mathrm N$ durante todo el primer desplazamiento daría $24\,\mathrm J$, que sobreestima la integral. La fuerza media lineal es $(4+12)/2=8\,\mathrm N$ y multiplicarla por $2\,\mathrm m$ sí da $16\,\mathrm J$. El signo inverso corresponde al mismo campo, no a una fuerza que se oponga siempre al movimiento.

[]{#fispm-t1-c12-e0004}

**Ejercicio 12.4.** Una partícula sigue $x(t)=a\sin(\omega t)$ entre $t=0$ y $t=\pi/\omega$, con $a,\omega>0$, bajo la contribución de fuerza $F(x)=kx$. Calcula su trabajo por la proposición 12.2 y directamente en el tiempo. ¿Debe ser nulo en cada mitad?

**Solución.** Los extremos tienen $x=0$, por lo que proposición 12.2 da trabajo total cero. Directamente, $F\dot x=ka^2\omega\sin(\omega t)\cos(\omega t)$; una primitiva es $ka^2\sin^2(\omega t)/2$. Entre los extremos también da cero. La primera mitad aporta $ka^2/2$ y la segunda $-ka^2/2$. La suma se anula, pero los trabajos parciales no. Se está evaluando una contribución sobre una historia dada: no se afirma que $F=kx$ sea por sí sola la fuerza que produce esa historia sinusoidal.

[]{#energía-cinética-y-cambio-de-rapidez}

[]{#fispm-t1-c12-s03}

[]{#fpm-i-12-s03}

## 12.3. Energía cinética y cambio de rapidez {#fispm-c12-energuxeda-cinuxe9tica-y-cambio-de-rapidez}

El factor cuadrático de la velocidad aparece al multiplicar aceleración por velocidad. Antes de usar Newton conviene establecer la identidad matemática que lo produce. Esto permitirá demostrar el teorema sin dividir por rapidez y conservar su validez en instantes de reposo.

[]{#fispm-t1-c12-d0003}

**Definición 12.3 --- Energía cinética de un punto material.** Para una masa constante $m>0$ con velocidad $\mathbf v$ medida en el marco elegido, definimos

$$K=\frac12m\|\mathbf v\|^2.$$

En coordenadas cartesianas ortonormales, $K=\tfrac12m(v_x^2+v_y^2+v_z^2)$. Es un escalar de dimensión $ML^2T^{-2}$ y se expresa en joules. El modelo es el de una partícula newtoniana de masa constante, no un cuerpo con rotación o deformación interna.

[]{#fispm-t1-c12-p0003}

**Proposición 12.3 --- Positividad y pérdida de información direccional.** La energía cinética es no negativa y es cero exactamente cuando $\mathbf v=0$. Velocidades distintas pueden tener la misma energía cinética; para una masa fijada, $K$ determina la rapidez pero no la dirección.

**Demostración.** La norma al cuadrado es suma de cuadrados no negativos y sólo se anula cuando todas las componentes son cero. Como $m>0$, se conservan esas propiedades al multiplicar por $m/2$. Dado $K\geq0$, la rapidez es $\sqrt{2K/m}$. Cualquier vector con esa magnitud produce el mismo valor; por ejemplo, $\mathbf v$ y $-\mathbf v$ lo comparten. $\square$

Que $K$ sea escalar significa que no cambia al girar los ejes ortonormales de un mismo marco. No significa que sea independiente del observador en movimiento. Un cuerpo en reposo en un marco puede desplazarse en otro y tener otra energía cinética. La comparación entre marcos se retomará después de establecer el trabajo y el teorema dentro de un marco inercial declarado.

[]{#fispm-t1-c12-p0004}

**Proposición 12.4 --- Derivada de la energía cinética.** Para una velocidad diferenciable y masa constante,

$$\frac{dK}{dt}=m\mathbf a\cdot\mathbf v.$$

La identidad sigue siendo válida cuando $\mathbf v=0$.

**Demostración.** Por la regla del producto, $\frac d{dt}(\mathbf v\cdot\mathbf v)=\dot{\mathbf v}\cdot\mathbf v+\mathbf v\cdot\dot{\mathbf v}=2\mathbf a\cdot\mathbf v$. Multiplicar por $m/2$ produce la fórmula. Ningún paso exige dividir por la norma de velocidad, de modo que el instante de reposo no queda excluido. $\square$

Esta identidad separa cambio de rapidez y cambio de dirección. Una aceleración perpendicular a la velocidad puede desviar el movimiento y dejar $dK/dt=0$. Una aceleración paralela o antiparalela produce una contribución de signo definido mientras la velocidad sea no nula. El movimiento circular uniforme del capítulo 8 tiene aceleración no nula y energía cinética constante.

En un instante de reposo, proposición 12.4 da $dK/dt=0$ aunque la aceleración no sea cero. No hay contradicción: el crecimiento inicial de $K$ puede ser cuadrático. Si una aceleración constante $\mathbf a_0$ inicia el movimiento desde reposo, $\mathbf v=\mathbf a_0t$ y $K=\tfrac12m\|\mathbf a_0\|^2t^2$. Su derivada vale cero en $t=0$ y es positiva inmediatamente después si $\mathbf a_0\ne0$. Una tasa instantánea nula no obliga a una función constante en un intervalo.

[]{#fispm-t1-c12-mp0003}

**Principio metodológico 12.3 --- Recuperar sólo lo que el escalar determina.** Usa $K$ para calcular rapidez y comprueba $K\geq0$. Conserva los datos de dirección y la cinemática cuando se necesite reconstruir velocidad o trayectoria. Un cambio nulo de energía cinética no implica aceleración nula.

[]{#ejercicios-2}

### 12.3.1. Ejercicios {#fispm-c12-ejercicios-2}

[]{#fispm-t1-c12-e0005}

**Ejercicio 12.5.** Una masa de $2\,\mathrm{kg}$ tiene velocidad $(3,4)\,\mathrm{m\,s^{-1}}$. Calcula $K$ y propone otras dos velocidades con ese mismo valor. ¿Las tres tienen que corresponder al mismo movimiento?

**Solución.** La rapidez es $5\,\mathrm{m\,s^{-1}}$ y $K=\tfrac12(2)(9+16)=25\,\mathrm J$. Las velocidades $(-3,-4)$ y $(5,0)$, en las mismas unidades, dan también $25\,\mathrm J$. Difieren en dirección y pueden producir trayectorias distintas desde la misma posición. La coincidencia del escalar no identifica los datos iniciales vectoriales ni las fuerzas que los acompañan.

[]{#fispm-t1-c12-e0006}

**Ejercicio 12.6.** Una masa $m$ parte del reposo con aceleración constante $(a,0)$, $a\ne0$. Calcula $K(t)$ y su derivada. Compara el instante inicial con un movimiento circular uniforme de rapidez $V>0$.

**Solución.** $\mathbf v(t)=(at,0)$, luego $K(t)=ma^2t^2/2$ y $dK/dt=ma^2t$. En $t=0$, la derivada es cero pese a la aceleración no nula. En el círculo uniforme, $K=mV^2/2$ es constante durante el intervalo porque aceleración y velocidad son perpendiculares en cada instante. El primer caso tiene tasa nula sólo inicialmente; el segundo, en todo el régimen. Ninguno permite identificar tasa nula con fuerza resultante nula.

[]{#trabajo-a-lo-largo-de-una-trayectoria}

[]{#fispm-t1-c12-s04}

[]{#fpm-i-12-s04}

## 12.4. Trabajo a lo largo de una trayectoria {#fispm-c12-trabajo-a-lo-largo-de-una-trayectoria}

Para recorrer una curva debemos sumar contribuciones locales, usando en cada una la fuerza y el desplazamiento correspondientes. La posición final menos la inicial no basta para un campo variable general. Podemos formular la integral directamente con una parametrización, de modo que todos sus elementos se reduzcan a operaciones de una variable.[^3]

[]{#fispm-t1-c12-d0004}

**Definición 12.4 --- Trayectoria parametrizada y orientación.** Una trayectoria se describe por una aplicación $\boldsymbol\gamma:[a,b]\to\mathbb R^d$ continuamente diferenciable por tramos. Su orientación corresponde a recorrer el parámetro de $a$ hacia $b$. Se permite dividir el intervalo en un número finito de partes suaves; el trabajo total se define sumando las integrales de esas partes.

[]{#fispm-t1-c12-d0005}

**Definición 12.5 --- Trabajo sobre una historia de movimiento.** Si $\mathbf r(t)$ describe al punto material y $\mathbf f(t)$ es el valor de una fuerza concreta sobre él a lo largo de esa historia, definimos

$$W_{t_a\to t_b}=\int_{t_a}^{t_b}\mathbf f(t)\cdot\dot{\mathbf r}(t)\,dt.$$

Suponemos funciones continuas por tramos e integral existente. Si la fuerza procede de un campo fijo de posición $\mathbf F(\mathbf r)$, la integral sobre una curva parametrizada se escribe

$$W_C=\int_a^b\mathbf F(\boldsymbol\gamma(u))\cdot\boldsymbol\gamma'(u)\,du=\int_C\mathbf F\cdot d\mathbf r.$$

La segunda expresión abrevia la primera; el diferencial vectorial representa $\boldsymbol\gamma'(u)\,du$ y no una dirección constante. La versión temporal permite fuerzas dependientes de tiempo o velocidad: se evalúa su valor real $\mathbf f(t)$ sobre la historia. La versión de campo fijo permite cambiar el parámetro de recorrido sin cambiar la ley espacial. No deben confundirse. Si una fuerza cambia con el tiempo, recorrer la misma curva a otra hora o con otro ritmo puede modificar el trabajo.

[]{#fispm-t1-c12-p0005}

**Proposición 12.5 --- Suma de fuerzas y unión de recorridos.** El trabajo es lineal respecto de las fuerzas evaluadas sobre una misma historia. Además, si se divide el recorrido en dos partes consecutivas, su trabajo es la suma de los trabajos parciales.

**Demostración.** Para $\mathbf f=\sum_i\mathbf f_i$, la distributividad del producto escalar da $\mathbf f\cdot\dot{\mathbf r}=\sum_i\mathbf f_i\cdot\dot{\mathbf r}$. La linealidad de la integral permite sumar sus trabajos. Para una división en $t_c$, la aditividad de la integral da $\int_{t_a}^{t_b}=\int_{t_a}^{t_c}+\int_{t_c}^{t_b}$. Las mismas identidades se aplican por tramos a una parametrización espacial. $\square$

[]{#fispm-t1-c12-p0006}

**Proposición 12.6 --- Cambio de parámetro y orientación para un campo fijo.** Sea $\mathbf F$ un campo continuo sobre la curva. Un cambio de parámetro continuamente diferenciable, creciente, con extremos correspondientes, conserva $W_C$. Recorrer la curva en sentido inverso cambia su signo.

**Demostración.** Si $u=\phi(s)$ es creciente, con $\phi(c)=a$ y $\phi(d)=b$, la curva nueva es $\boldsymbol\gamma(\phi(s))$. Su derivada es $\boldsymbol\gamma'(\phi(s))\phi'(s)$. Sustituir en la integral y efectuar el cambio de variable $u=\phi(s)$ recupera $W_C$. Para el sentido inverso usamos $u=a+b-s$, con $s$ de $a$ a $b$; los extremos de $u$ van de $b$ a $a$ y la integral resulta $\int_b^a\mathbf F(\boldsymbol\gamma(u))\cdot\boldsymbol\gamma'(u)\,du=-W_C$. $\square$

Proposición 12.6 compara el mismo campo espacial, no una resistencia que invierta su dirección al invertir la velocidad. Tampoco afirma que cambiar el ritmo de la trayectoria mantenga su validez dinámica: una curva recorrida con otra velocidad puede exigir otra fuerza resultante. La igualdad es una propiedad del cálculo de trabajo de esa contribución sobre los recorridos dados.

Para una fuerza constante, la integral espacial da $\mathbf F\cdot\int_a^b\boldsymbol\gamma'(u)du=\mathbf F\cdot(\mathbf r_B-\mathbf r_A)$, lo que extiende proposición 12.1 a curvas suaves por tramos. Para un campo variable, se debe conservar $\boldsymbol\gamma$ en el integrando. Cada componente de fuerza se evalúa sobre toda la curva, no sobre un eje independiente inventado.

[]{#fispm-t1-c12-mp0004}

**Principio metodológico 12.4 --- Escribir primero la parametrización.** Sustituye la curva en todas las componentes del campo y deriva su posición respecto del parámetro. Multiplica escalarmente antes de integrar. Si la fuerza depende de tiempo o velocidad, conserva la historia necesaria para evaluarla; no reemplaces esa historia por los extremos espaciales.

[]{#ejercicios-3}

### 12.4.1. Ejercicios {#fispm-c12-ejercicios-3}

[]{#fispm-t1-c12-e0007}

**Ejercicio 12.7.** Sea $\mathbf F(x,y)=(0,\kappa x)$, con $\kappa$ de dimensión fuerza por longitud. Calcula su trabajo sobre $\boldsymbol\gamma(u)=(Lu,Hu)$, $0\leq u\leq1$, con $L,H>0$. Repite con $\boldsymbol\eta(s)=(Ls^2,Hs^2)$, $0\leq s\leq1$.

**Solución.** En la primera curva, $\mathbf F=(0,\kappa Lu)$ y $\boldsymbol\gamma'=(L,H)$; el integrando es $\kappa LHu$, cuya integral da $\kappa LH/2$. En la segunda, $\mathbf F=(0,\kappa Ls^2)$ y $\boldsymbol\eta'=(2Ls,2Hs)$; el integrando es $2\kappa LHs^3$ y da también $\kappa LH/2$. La derivada del cambio de parámetro se anula en un extremo, pero el cálculo directo sigue siendo válido. Ambas curvas recorren el mismo segmento con orientación igual; no se ha afirmado que ambas sean soluciones de Newton con la misma fuerza total.

[]{#fispm-t1-c12-e0008}

**Ejercicio 12.8.** En una historia de $0$ a $T>0$, un cuerpo se mueve con $\mathbf r(t)=(vt,0)$, $v>0$, y una contribución externa es $\mathbf f(t)=(\beta t,0)$, con $\beta$ de dimensión fuerza por tiempo. Calcula el trabajo y compara con recorrer el mismo segmento en tiempo $T/2$, desde la misma hora inicial, con rapidez $2v$.

**Solución.** El primer trabajo es $\int_0^T\beta tv\,dt=\beta vT^2/2$. El segundo es $\int_0^{T/2}\beta t(2v)\,dt=\beta vT^2/4$. Los extremos espaciales son los mismos, pero la fuerza temporal se evalúa durante intervalos distintos. Proposición 12.6 no iguala ambos resultados. Se trata de una contribución sobre historias prescritas; otras fuerzas deben compensarla si se quiere mantener la rapidez constante indicada.

[]{#teorema-trabajoenergía-para-una-partícula}

[]{#fispm-t1-c12-s05}

[]{#fpm-i-12-s05}

## 12.5. Teorema trabajo--energía para una partícula {#fispm-c12-teorema-trabajoenerguxeda-para-una-partuxedcula}

Disponemos de dos expresiones con el mismo integrando: la derivada de energía cinética contiene $m\mathbf a\cdot\mathbf v$ y la integral de trabajo contiene $\mathbf F\cdot\mathbf v$. Newton identifica ambas cuando $\mathbf F$ es la fuerza resultante. La demostración consiste en hacer esa identificación y después integrar; el alcance físico depende de las hipótesis conservadas.[^4]

[]{#fispm-t1-c12-p0007}

**Proposición 12.7 --- Teorema trabajo--energía.** Sea un punto material de masa constante $m>0$, con posición dos veces continuamente diferenciable en un marco inercial. Si $\mathbf F_{\mathrm{tot}}(t)=m\ddot{\mathbf r}(t)$ es la suma de todas las fuerzas sobre él durante $[t_a,t_b]$, entonces

$$W_{\mathrm{tot}}=\int_{t_a}^{t_b}\mathbf F_{\mathrm{tot}}(t)\cdot\mathbf v(t)\,dt =K(t_b)-K(t_a).$$

El trabajo total puede escribirse como suma de los trabajos de las fuerzas individuales sobre esa misma historia.

**Demostración.** proposición 12.4 da $\frac{dK}{dt}=m\mathbf a\cdot\mathbf v$. Por Newton, $m\mathbf a=\mathbf F_{\mathrm{tot}}$, de modo que $\frac{dK}{dt}=\mathbf F_{\mathrm{tot}}\cdot\mathbf v$. Integrar en $[t_a,t_b]$ y usar el teorema fundamental produce la igualdad. La suma de contribuciones procede de la proposición 12.5 aplicado a la descomposición de la fuerza resultante. La demostración no divide por velocidad ni presupone que la fuerza dependa sólo de la posición. $\square$

El teorema es una consecuencia de Newton para este modelo. Una fuerza temporal, una resistencia dependiente de velocidad o una reacción de vínculo siguen incluidas si se evalúan sobre la historia y satisfacen sus hipótesis. No hace falta suponer que cada fuerza tenga trabajo independiente del camino. El teorema compara la energía cinética con el trabajo total realmente efectuado; no afirma que esa energía cinética sea constante.

La condición $W_{\mathrm{tot}}>0$ entre dos instantes implica rapidez final mayor que inicial, para la misma masa. Un trabajo total negativo implica rapidez final menor. Un trabajo total cero implica rapideces iguales en los extremos, pero permite variaciones intermedias. Si el integrando total se anula en todo un intervalo, entonces $K$ permanece constante durante él; ésa es una afirmación más fuerte que una integral total nula.

Una aplicación correcta exige mantener el receptor. Para la partícula que sube con rapidez constante, el peso tiene trabajo negativo y la fuerza de elevación positivo; sus trabajos se cancelan. Si sólo se escribe el de elevación como $\Delta K$, se concluye un aumento de rapidez que no ocurrió. En sentido inverso, un trabajo positivo del peso durante una bajada puede compensarse con un trabajo negativo del freno. Es la suma la que decide la variación cinética.

También hay que mantener el modelo de masa constante. La derivada de $mv^2/2$ adquiere otro término si $m$ varía, y un sistema abierto con transferencia de materia requiere balances adicionales. No basta sustituir una masa dependiente de tiempo en la fórmula probada. Del mismo modo, un cuerpo que gira puede recibir trabajo que cambie su energía cinética rotacional; representarlo sólo por una partícula no recoge esa contribución.

El procedimiento evita a veces integrar dos veces Newton, pero no elimina todas las incógnitas. Para evaluar trabajo necesitamos conocer la trayectoria o alguna propiedad de la fuerza que permita calcular la integral. Si la trayectoria está fijada por una guía, la geometría del capítulo 11 proporciona parte de esa información. Si está desconocida y el campo es general, el teorema no permite reemplazar la integral por una función arbitraria de los extremos.

[]{#fispm-t1-c12-mp0005}

**Principio metodológico 12.5 --- Sumar antes de interpretar el cambio cinético.** Declara el marco, la masa y el punto material elegido. Enumera todas las fuerzas y sus trabajos, incluidos los de signo negativo. Escribe después $\Delta K=W_{\mathrm{tot}}$. Comprueba si el resultado determina sólo rapidez o si hacen falta dirección, trayectoria y datos temporales.

[]{#ejercicios-4}

### 12.5.1. Ejercicios {#fispm-c12-ejercicios-4}

[]{#fispm-t1-c12-e0009}

**Ejercicio 12.9.** Una masa de $2\,\mathrm{kg}$ tiene rapidez inicial $3\,\mathrm{m\,s^{-1}}$. Durante un tramo, una fuerza hace $20\,\mathrm J$ y otra $-4\,\mathrm J$; las demás hacen trabajo nulo. Calcula la rapidez final. Evalúa la solución que usa sólo los $20\,\mathrm J$.

**Solución.** La energía inicial es $K_a=9\,\mathrm J$. El trabajo total es $16\,\mathrm J$, luego $K_b=25\,\mathrm J$ y la rapidez final es $\sqrt{2(25)/2}=5\,\mathrm{m\,s^{-1}}$. Usar sólo la contribución positiva daría $K_b=29\,\mathrm J$ y rapidez $\sqrt{29}\,\mathrm{m\,s^{-1}}$, incorrecta para los trabajos declarados. El resultado correcto no fija la dirección final: ésta requiere otra información del movimiento.

[]{#fispm-t1-c12-e0010}

**Ejercicio 12.10.** Una partícula recorre una circunferencia fija con rapidez constante $V>0$. Su fuerza resultante es radial, dirigida hacia el centro. Calcula su trabajo en una vuelta y explica por qué el resultado no significa fuerza resultante cero.

**Solución.** La velocidad es tangencial y la resultante radial, por lo que $\mathbf F_{\mathrm{tot}}\cdot\mathbf v=0$ en cada instante. El trabajo es cero y proposición 12.7 da $\Delta K=0$, compatible con $K=mV^2/2$. La resultante tiene magnitud $mV^2/R>0$ y cambia la dirección de velocidad. No contribuye a la tasa de cambio de rapidez. Una fuerza de trabajo nulo puede ser indispensable para mantener la trayectoria.

[]{#componente-tangencial-y-dependencia-del-recorrido}

[]{#fispm-t1-c12-s06}

[]{#fpm-i-12-s06}

## 12.6. Componente tangencial y dependencia del recorrido {#fispm-c12-componente-tangencial-y-dependencia-del-recorrido}

El producto escalar selecciona la componente de fuerza en el sentido local del movimiento. Podemos expresar esa selección usando longitud de arco, siempre que conservemos la tangente orientada de la curva. En una curva, «distancia» y «desplazamiento vectorial» cumplen funciones diferentes.

[]{#fispm-t1-c12-d0006}

**Definición 12.6 --- Longitud recorrida y componente tangencial de fuerza.** En un tramo regular parametrizado por $\boldsymbol\gamma(u)$, con $\boldsymbol\gamma'(u)\ne0$, escribimos $ds=\|\boldsymbol\gamma'(u)\|\,du$ para el incremento de longitud en el sentido creciente del parámetro. La tangente unitaria orientada es $\mathbf t=\boldsymbol\gamma'/\|\boldsymbol\gamma'\|$ y la componente de fuerza sobre ella es $F_\parallel=\mathbf F\cdot\mathbf t$.

[]{#fispm-t1-c12-p0008}

**Proposición 12.8 --- Trabajo como integral tangencial.** Sobre los tramos regulares de un recorrido orientado,

$$W_C=\int_C F_\parallel\,ds.$$

En particular, una fuerza perpendicular a la tangente en todo el tramo tiene trabajo cero en él.

**Demostración.** La definición de tangente da $d\mathbf r=\boldsymbol\gamma'(u)\,du=\mathbf t\,ds$. Por tanto, $\mathbf F\cdot d\mathbf r=(\mathbf F\cdot\mathbf t)\,ds=F_\parallel\,ds$. Integrar prueba la igualdad y la afirmación de perpendicularidad. Si la descripción temporal tiene un instante de reposo, se usa directamente definición 12.5: el integrando es cero allí sin definir una tangente a partir de una velocidad nula. $\square$

$ds$ es no negativo en el sentido del recorrido; el signo del trabajo queda en $F_\parallel$. Para una resistencia de magnitud fija $f>0$ que se opone a la velocidad, $F_\parallel=-f$ durante los tramos móviles y $W=-fS$, donde $S$ es la longitud total recorrida. Esa fuerza puede hacer trabajo negativo en la ida y en la vuelta. La orientación de la fuerza se adapta al movimiento, de modo que no es el mismo campo espacial en ambos sentidos.

Para una guía fija lisa, la reacción normal es perpendicular al desplazamiento y no hace trabajo mientras se mantenga ese modelo. La palabra «fija» importa: un soporte móvil puede tener una reacción perpendicular al deslizamiento relativo y, sin embargo, realizar trabajo sobre el movimiento inercial del cuerpo. Los casos móviles se estudiarán en el segundo macrotramo. No debemos extender la conclusión de una guía fija a todos los vínculos del capítulo 11.

Tampoco un campo que dependa sólo de la posición tiene automáticamente el mismo trabajo entre dos extremos. La dependencia del recorrido puede mostrarse mediante dos parametrizaciones y sus integrales; no hace falta introducir todavía una condición de rotacional ni el lenguaje de energía potencial.

[]{#fispm-t1-c12-p0009}

**Proposición 12.9 --- Un campo espacial puede tener trabajos distintos entre los mismos extremos.** Para $\mathbf F(x,y)=\kappa(-y,x)$, con $\kappa>0$, consideremos $A=(0,0)$ y $B=(L,H)$, $L,H>0$. El camino que va primero horizontalmente hasta $(L,0)$ y luego verticalmente hasta $B$ tiene trabajo $\kappa LH$. El que va primero hasta $(0,H)$ y luego horizontalmente hasta $B$ tiene trabajo $-\kappa LH$.

**Demostración.** En el primer tramo horizontal, $y=0$ y $dy=0$, así que $\mathbf F\cdot d\mathbf r=-\kappa y\,dx+\kappa x\,dy=0$. En el vertical siguiente, $x=L$ y el trabajo es $\int_0^H\kappa L\,dy=\kappa LH$. Para el otro camino, el primer tramo vertical tiene $x=0$ y trabajo cero; el horizontal superior da $\int_0^L-\kappa H\,dx=-\kappa LH$. La diferencia es $2\kappa LH\ne0$ pese a los extremos comunes. $\square$

Si se recorre el primer camino y se vuelve por el inverso del segundo, proposiciones 12.5--12.6 dan trabajo cerrado $2\kappa LH$. No se contradice proposición 12.1: aquí la fuerza varía con la posición. Tampoco se contradice proposición 12.7: si ésa fuera la fuerza total sobre un cuerpo que realmente completara el camino, el trabajo no nulo exigiría otro valor de energía cinética al terminar. Volver al mismo punto no significa volver con la misma velocidad.

La evaluación de una integral sobre una curva prescrita no demuestra por sí sola que esa curva sea una trayectoria realizable bajo el campo como única fuerza. Se podrían necesitar guías, actuadores o condiciones iniciales adicionales. Proposición 12.9 prueba una propiedad del trabajo del campo; los balances de Newton determinan su realización física. Separar ambos problemas evita utilizar una figura geométrica como solución dinámica sin demostrarlo.

[]{#fispm-t1-c12-mp0006}

**Principio metodológico 12.6 --- Comprobar el camino antes de reducir a extremos.** Una fuerza constante permite la reducción de la proposición 12.1; un campo variable exige una prueba adicional o el cálculo sobre la trayectoria. En curvas, usa la tangente local. Si se afirma que una reacción no hace trabajo, identifica el movimiento respecto del cual es perpendicular.

[]{#ejercicios-5}

### 12.6.1. Ejercicios {#fispm-c12-ejercicios-5}

[]{#fispm-t1-c12-e0011}

**Ejercicio 12.11.** En proposición 12.9, toma $\kappa=2\,\mathrm{N\,m^{-1}}$, $L=3\,\mathrm m$ y $H=4\,\mathrm m$. Calcula ambos trabajos y el del circuito formado por el primer camino de ida y el segundo de vuelta. ¿Puede obtenerse el trabajo multiplicando la fuerza en $B$ por el desplazamiento neto?

**Solución.** Los trabajos son $24\,\mathrm J$ y $-24\,\mathrm J$. Al invertir el segundo, su contribución es $+24\,\mathrm J$, de modo que el circuito da $48\,\mathrm J$. En $B$, la fuerza vale $(-8,6)\,\mathrm N$, cuyo producto con $(3,4)\,\mathrm m$ da cero. Esa multiplicación ignora la variación de campo y no reproduce ninguno de los dos trabajos. El desplazamiento neto del circuito es cero, pero su integral no lo es.

**Ejercicio 12.12.** Calcula el trabajo del mismo campo $\mathbf F=\kappa(-y,x)$ sobre el arco $\mathbf r(\theta)=R(\cos\theta,\sin\theta)$, de $\theta=0$ a $\pi/2$, con $R>0$. Compara con una contribución puramente radial sobre ese arco.

**Solución.** Sobre la curva, $\mathbf F=\kappa R(-\sin\theta,\cos\theta)$ y $d\mathbf r=R(-\sin\theta,\cos\theta)d\theta$. El producto es $\kappa R^2d\theta$, luego $W=\kappa R^2\pi/2$. La fuerza es tangencial y favorece el recorrido elegido. Una fuerza puramente radial es perpendicular a $d\mathbf r$ y tiene trabajo cero. Si el campo tangencial forma parte de la resultante, la rapidez no será constante salvo que otra contribución compense su trabajo; no se impuso un ritmo de recorrido al evaluar la integral.

[]{#potencia-media-e-instantánea}

[]{#fispm-t1-c12-s07}

[]{#fpm-i-12-s07}

## 12.7. Potencia media e instantánea {#fispm-c12-potencia-media-e-instantuxe1nea}

Dos procesos pueden realizar el mismo trabajo y requerir tiempos distintos. La potencia expresa la tasa de trabajo, de modo que añade una información temporal que la integral total no contiene.[^5]

[]{#fig:I-12-N03}

<figure id="fig-fpm-v04-i-12-n03" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-12-N03.svg" class="lightbox" data-gallery="fpm-v04-c12"><img src="/assets/books/fispm/v04/I-12-N03.svg" alt="Potencia instantánea. Diagrama del capítulo 12; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="446" height="255" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 12.4.** Una fuerza constante paralela al movimiento produce $v=Ft/m$ desde el reposo y potencia $P=F^2t/m$. El trabajo acumulado es el área bajo esta recta. Véase §[12.7](#fispm-c12-potencia-media-e-instantuxe1nea).

</figcaption>

</figure>

[]{#fispm-t1-c12-d0007}

**Definición 12.7 --- Potencia media.** Para el trabajo $W$ de una fuerza durante un intervalo de duración $\Delta t>0$, definimos su potencia media como $\overline P=W/\Delta t$. Su signo es el del trabajo neto durante ese intervalo.

[]{#fispm-t1-c12-d0008}

**Definición 12.8 --- Potencia instantánea.** Sea $W(t)=\int_{t_0}^t\mathbf f(\tau)\cdot\mathbf v(\tau)\,d\tau$ el trabajo acumulado. Donde el integrando es continuo, la potencia instantánea de esa fuerza es $P(t)=dW/dt$. La unidad SI es el watt: $1\,\mathrm W=1\,\mathrm{J\,s^{-1}}$, de dimensión $ML^2T^{-3}$.

[]{#fispm-t1-c12-p0010}

**Proposición 12.10 --- Potencia de fuerza y tasa cinética.** Bajo las hipótesis de la definición 12.8,

$$P=\mathbf f\cdot\mathbf v,\qquad |P|\leq\|\mathbf f\|\,\|\mathbf v\|.$$

Para la resultante de una partícula de la proposición 12.7, $P_{\mathrm{tot}}=dK/dt$.

**Demostración.** El teorema fundamental aplicado al trabajo acumulado da $P=\mathbf f\cdot\mathbf v$. Cauchy--Schwarz proporciona la cota de magnitudes. Newton y proposición 12.4 dan la igualdad de la potencia total con la derivada cinética. La suma de potencias individuales coincide con la total por distributividad del producto escalar. $\square$

La potencia depende tanto de fuerza como de velocidad. Una fuerza grande sobre un punto inmóvil tiene potencia mecánica cero en ese instante. La misma fuerza sobre un punto que avanza rápidamente en su dirección tiene potencia positiva mayor. Una fuerza perpendicular a la velocidad tiene potencia cero y puede cambiar la dirección del movimiento.

Para elevar una masa puntual a rapidez vertical constante $V>0$, sin resistencia y con gravedad uniforme, la tracción debe ser $T=mg$. La potencia de elevación es $mgV$ y la del peso $-mgV$. La suma es cero porque la energía cinética no cambia. La potencia del motor entregada al punto material no es la potencia neta sobre él. Si se quisiera calcular consumo eléctrico, eficiencia o pérdidas del motor, habría que declarar otro modelo; $mgV$ sólo responde al intercambio mecánico especificado.

Una potencia media tampoco fija la instantánea. Si $P(t)$ varía, el trabajo es $\int P(t)dt$, no necesariamente el valor final de $P$ multiplicado por la duración. La media recoge esa integral dividida por tiempo. Dos historias con igual integral pueden tener demandas máximas distintas, lo que importa para seleccionar un actuador, aunque ese problema de ingeniería quede fuera del cálculo elemental.

En una fuerza paralela al movimiento, escribir $F=P/v$ sólo es lícito cuando $v\ne0$. Un modelo que prescribe potencia positiva constante y pretende iniciar desde reposo exige una fuerza que crezca sin cota al acercarse a ese instante. La identidad $P=Fv$ sigue siendo válida; es la hipótesis simultánea de potencia positiva y fuerza finita en reposo la que resulta incompatible. No se resuelve el problema dividiendo por cero.

[]{#fispm-t1-c12-mp0007}

**Principio metodológico 12.7 --- Distinguir potencia entregada y potencia neta.** Escribe el producto escalar con la velocidad del receptor. Declara el intervalo si se pide una media y conserva cada contribución de signo contrario. Antes de despejar fuerza como potencia dividida por rapidez, comprueba que ésta sea no nula y que la fuerza tenga la dirección supuesta.

[]{#ejercicios-6}

### 12.7.1. Ejercicios {#fispm-c12-ejercicios-6}

[]{#fispm-t1-c12-e0013}

**Ejercicio 12.13.** Una masa de $50\,\mathrm{kg}$ sube $2\,\mathrm m$ con rapidez constante $0{,}4\,\mathrm{m\,s^{-1}}$. Usa $g=10\,\mathrm{m\,s^{-2}}$ y desprecia resistencia. Calcula la potencia de elevación, el trabajo, la duración y la potencia neta sobre la masa.

**Solución.** La tracción es $500\,\mathrm N$, su potencia $500(0{,}4)=200\,\mathrm W$ y su trabajo $500(2)=1000\,\mathrm J$. La duración es $2/0{,}4=5\,\mathrm s$, y $1000/5=200\,\mathrm W$ confirma la media. El peso hace $-1000\,\mathrm J$ y tiene potencia $-200\,\mathrm W$. La potencia neta es cero, como exige la rapidez constante. El ascenso presupone aquí un tramo uniforme, sin incluir las fases de inicio o frenado.

[]{#fispm-t1-c12-e0014}

**Ejercicio 12.14.** Una contribución de fuerza es $(3,4)\,\mathrm N$ y la velocidad del cuerpo $(4,-3)\,\mathrm{m\,s^{-1}}$. Calcula su potencia. Después, una fuerza temporal tiene potencia $P(t)=ct$, $c>0$, en $0\leq t\leq T$. Calcula trabajo y potencia media y compáralos con usar la potencia final durante todo el intervalo.

**Solución.** El producto escalar de los primeros vectores es $12-12=0\,\mathrm W$: fuerza y velocidad son perpendiculares. Para la segunda historia, $W=\int_0^Tct\,dt=cT^2/2$ y $\overline P=cT/2$. El producto $P(T)T=cT^2$ duplica el trabajo porque trata una tasa creciente como constante. La dimensión de $c$ es potencia por tiempo; por tanto, ambas expresiones de trabajo tienen dimensión de energía aunque sólo una respete la historia.

[]{#rapidez-frenado-y-límites-de-la-ecuación-escalar}

[]{#fispm-t1-c12-s08}

[]{#fpm-i-12-s08}

## 12.8. Rapidez, frenado y límites de la ecuación escalar {#fispm-c12-rapidez-frenado-y-luxedmites-de-la-ecuaciuxf3n-escalar}

Una aplicación frecuente del teorema consiste en calcular la rapidez en una posición conocida de una línea. La reducción funciona especialmente bien si la fuerza total está dada como función de posición. Los instantes de reposo requieren atención: la energía cinética debe seguir siendo no negativa, pero su valor cero no determina por sí solo la continuación.

[]{#fispm-t1-c12-p0011}

**Proposición 12.11 --- Rapidez en una fuerza unidimensional de posición.** Sea una partícula de masa constante $m>0$ que satisface $m\ddot x=F(x)$ en un marco inercial, con $F$ continua y datos iniciales $x(t_a)=x_a$, $\dot x(t_a)=v_a$. Durante la historia,

$$\dot x(t)^2=v_a^2+\frac2m\int_{x_a}^{x(t)}F(\xi)\,d\xi.$$

El lado derecho debe ser no negativo en toda posición alcanzada.

**Demostración.** proposición 12.7 da $\tfrac12m\dot x(t)^2-\tfrac12mv_a^2=\int_{t_a}^{t}F(x(\tau))\dot x(\tau)d\tau$. Proposición 12.2 transforma el trabajo en la integral entre posiciones, sin exigir movimiento monótono. Multiplicar por $2/m$ produce la fórmula. La no negatividad procede del cuadrado de una velocidad real. $\square$

La fórmula determina magnitud, no signo de velocidad. En un tramo donde no hay reposo, el signo se fija con el dato inicial de dirección y la continuidad. Entonces se puede escribir $\dot x=\sigma\sqrt{v_a^2+(2/m)\int_{x_a}^{x}F\,d\xi}$, con $\sigma=+1$ o $-1$, y buscar tiempo por una integración adicional. El signo no puede cambiar durante ese tramo sin pasar por velocidad cero.

En un punto donde el lado derecho se anula, hay que examinar Newton y el régimen de fuerzas. Puede ocurrir un retorno, un equilibrio o un cambio de modelo como el fin de un deslizamiento. La igualdad escalar no distingue automáticamente esas posibilidades. Una región con lado derecho negativo es incompatible con la historia declarada, pero una región positiva tampoco garantiza por sí sola que se alcance desde los datos iniciales: faltan orientación y evolución.

[]{#fispm-t1-c12-p0012}

**Proposición 12.12 --- Distancia de frenado con resistencia constante.** En una línea horizontal, una partícula de masa $m>0$ parte de $x=0$ con velocidad $v_0>0$. Mientras se mueve hacia la derecha, la fuerza horizontal total es $-f$, con $f>0$ constante. La primera detención ocurre a distancia

$$d=\frac{mv_0^2}{2f}.$$

**Demostración.** Hasta la detención, proposición 12.11 da $v^2=v_0^2-2fx/m$. Al imponer $v=0$ se obtiene la distancia indicada. Para comprobar que se alcanza, Newton produce $v(t)=v_0-ft/m$, cuya primera anulación es $t_*=mv_0/f$. Integrar da $x(t)=v_0t-ft^2/(2m)$; evaluarla en $t_*$ recupera $d$. Antes de ese instante, $v>0$ y la rama de fuerza supuesta es válida. $\square$

La verificación temporal evita tratar un cero algebraico como un evento que nunca se alcanza. También impide extender $v^2=v_0^2-2fx/m$ a $x>d$ como si una rapidez imaginaria describiera el movimiento. El modelo de resistencia especificó sólo el tramo de avance. Después de detenerse, una fricción que se opone al deslizamiento no sigue empujando necesariamente hacia la izquierda: hay que declarar las fuerzas y el régimen posterior.

La distancia de frenado aumenta cuadráticamente con la rapidez inicial y linealmente con la masa si $f$ está fijada. Si la resistencia fuese $f=\mu mg$, la masa se cancelaría y quedaría $d=v_0^2/(2\mu g)$ bajo esas hipótesis. La diferencia no es una contradicción: en un caso se mantiene fija la fuerza y en el otro cambia proporcionalmente con la masa. Toda comparación debe indicar qué magnitudes permanecen constantes.

[]{#fispm-t1-c12-mp0008}

**Principio metodológico 12.8 --- Comprobar alcance y continuación.** Usa la ecuación escalar para rapidez y para excluir valores negativos de energía cinética. Conserva el sentido inicial del movimiento y comprueba que los eventos calculados se alcanzan. En detenciones o cambios de contacto, vuelve a Newton y a las condiciones del vínculo antes de prolongar la misma rama.

[]{#ejercicios-7}

### 12.8.1. Ejercicios {#fispm-c12-ejercicios-7}

[]{#fispm-t1-c12-e0015}

**Ejercicio 12.15.** Una masa $m$ parte de $x=0$ con velocidad $v_0>0$. Durante su avance, la fuerza horizontal total es $-(f_0+\kappa x)$, con $f_0,\kappa>0$. Obtén la rapidez como función de posición, la distancia candidata de detención y una comprobación de que esa detención se alcanza en tiempo finito.

**Solución.** La integral de trabajo es $-f_0x-\kappa x^2/2$, por lo que $v^2=v_0^2-2f_0x/m-\kappa x^2/m$. La raíz positiva que anula ese valor es

$$d=\frac{\sqrt{f_0^2+\kappa mv_0^2}-f_0}{\kappa}.$$

La otra raíz es negativa y no corresponde al avance inicial. Para $0\leq x<d$, el cuadrado es positivo y se toma la rama $v=+\sqrt{v_0^2-2f_0x/m-\kappa x^2/m}$. Su tiempo hasta $d$ es la integral de $dx/v$. Si $q(x)$ denota el radicando, $q(d)=0$ y $q'(d)=-2(f_0+\kappa d)/m<0$. Así, cerca de $d$, $q(x)$ es comparable con una constante positiva multiplicada por $d-x$. La integral local de $(d-x)^{-1/2}$ es finita, y lejos de $d$ el integrando es continuo. La detención se alcanza en tiempo finito. La ley de fuerza posterior al reposo no se ha especificado; no se prolonga esa resistencia como empuje automático hacia la izquierda.

[]{#fispm-t1-c12-e0016}

**Ejercicio 12.16.** En una línea sin fuerza resultante, una masa parte de $x=0$ con rapidez $V>0$. Compara las historias $x_+(t)=Vt$ y $x_-(t)=-Vt$. Después examina $x_c(t)=Vt+c\,t^2$, con $c\ne0$, cerca de $t=0$. ¿Compartir el valor inicial de energía cinética basta para resolver Newton?

**Solución.** Las dos primeras historias tienen aceleración cero, energía cinética $mV^2/2$ constante y trabajo total cero. Satisfacen el teorema y Newton, pero se seleccionan mediante signos distintos de la velocidad inicial. La tercera tiene la misma velocidad inicial $V$ y el mismo valor inicial de $K$, pero aceleración $2c\ne0$, incompatible con fuerza resultante cero. Además, su energía cinética $m(V+2ct)^2/2$ no permanece constante en un intervalo, lo que contradice el trabajo nulo. Coincidir en un dato escalar inicial no resuelve la historia ni sustituye las ecuaciones. Para fijar posición y dirección hay que conservar los datos cinemáticos correspondientes.

Las ocho secciones establecen el cálculo del trabajo y su relación con la energía cinética, incluyendo su tasa temporal. Las secciones siguientes aplicarán esas herramientas al peso, las fuerzas elásticas, el rozamiento, los vínculos móviles y los sistemas de partículas; examinará además el cambio de marco y los límites de la reducción escalar. La energía potencial y las condiciones generales de conservación se desarrollarán en el capítulo 13.

[]{#trabajo-del-peso-y-de-fuerzas-elásticas}

[]{#fispm-t1-c12-s09}

[]{#fpm-i-12-s09}

## 12.9. Trabajo del peso y de fuerzas elásticas {#fispm-c12-trabajo-del-peso-y-de-fuerzas-eluxe1sticas}

El peso uniforme y el resorte lineal permiten calcular trabajo sin reconstruir todos los instantes del movimiento. La simplificación procede de sus leyes de fuerza. El trabajo del peso sólo requiere el cambio de altura; el de un resorte fijo unidimensional requiere las deformaciones inicial y final. Ninguna de esas fórmulas autoriza a omitir las demás fuerzas cuando se busca el cambio de energía cinética.[^6]

Tomemos un eje vertical $y$ positivo hacia arriba y un campo gravitatorio uniforme $\mathbf g=-g\mathbf e_y$, con $g>0$. La masa es constante. La aproximación se aplica en una región donde variar la altura no modifica apreciablemente $g$; no describe ascensos comparables con el radio terrestre ni campos arbitrarios. Una trayectoria puede tener desplazamientos horizontales y retrocesos verticales: el producto escalar selecciona su componente vertical.

[]{#fispm-t1-c12-p0013}

**Proposición 12.13 --- Trabajo del peso uniforme.** Para una historia $\mathbf r(t)$ de clase $C^1$ por tramos, el trabajo del peso $-mg\mathbf e_y$ entre dos instantes es

$$W_g=-mg(y_b-y_a).$$

**Demostración.** definición 12.5 da $W_g=\int_{t_a}^{t_b}(-mg\mathbf e_y)\cdot\dot{\mathbf r}\,dt=-mg\int_{t_a}^{t_b}\dot y\,dt$. El teorema fundamental del cálculo, aplicado en los tramos y sumado en sus extremos comunes, produce $-mg(y_b-y_a)$. Las componentes horizontales no intervienen. $\square$

Un descenso da trabajo positivo y un ascenso da trabajo negativo. Si la partícula vuelve a la altura inicial, el trabajo total del peso es cero aunque haya recorrido una longitud considerable. En el ascenso y descenso aparecen contribuciones de signos opuestos. Esta cancelación es propia de la fuerza declarada; no implica que el trabajo total de todas las fuerzas se cancele.

Para el resorte elegimos una coordenada $x$ sobre una guía recta fija. Su origen es la posición sin deformación del resorte; $x$ es una deformación con signo, no la longitud del resorte. Suponemos la ley de Hooke $F_s(x)=-kx$, con $k>0$ constante, dentro de su rango de validez. El signo invierte la fuerza al pasar de extensión a compresión. Un resorte que sólo puede tirar, o que se destensa, requiere un modelo por regímenes diferente.

[]{#fispm-t1-c12-p0014}

**Proposición 12.14 --- Trabajo del resorte lineal fijo.** Bajo la ley anterior, el trabajo del resorte sobre la partícula es

$$W_s=-\frac{k}{2}(x_b^2-x_a^2),$$

incluso si la partícula invierte su movimiento durante el intervalo.

**Demostración.** proposición 12.2 expresa el trabajo como $\int_{x_a}^{x_b}(-k\xi)\,d\xi$. Una primitiva es $-k\xi^2/2$ y su evaluación en los extremos da la fórmula. Alternativamente, $-kx\dot x$ es la derivada temporal de $-kx^2/2$, sin dividir por $\dot x$. Ambas pruebas incluyen instantes de reposo y retrocesos. $\square$

Reducir la magnitud de la deformación da trabajo positivo del resorte; aumentarla da trabajo negativo. Ir de $a$ a $-a$ da trabajo neto cero, pero el resorte puede aumentar la rapidez al acercarse al origen y reducirla después. El trabajo neto sólo compara los extremos: no afirma que la potencia sea cero en los instantes intermedios.

Si el extremo de apoyo se mueve y la ley toma la forma $F_s=-k[x-c(t)]$, no puede sustituirse directamente $x$ por la deformación $q=x-c(t)$ en la proposición 12.14. El trabajo sobre la partícula utiliza su velocidad $\dot x=\dot q+\dot c$, de modo que

$$W_s=-\frac{k}{2}(q_b^2-q_a^2)-k\int_{t_a}^{t_b}q(t)\dot c(t)\,dt.$$

Esta identidad sale al desarrollar $-kq\dot x$ e integrar $q\dot q$. El segundo término registra la influencia del movimiento del apoyo. Para $c$ constante recuperamos proposición 12.14, con el origen trasladado. La fuerza se evalúa en la deformación, pero el desplazamiento del receptor se mide en el marco elegido.

[]{#fispm-t1-c12-mp0009}

**Principio metodológico 12.9 --- Fijar el origen y el soporte.** Al usar el trabajo del peso, declara el sentido vertical y la aproximación de campo uniforme. Al usar un resorte, identifica la deformación y comprueba que el apoyo es fijo. Escribe después la suma de trabajos que modifica $K$; una contribución conocida no representa por sí sola la fuerza resultante.

[]{#ejercicios-8}

### 12.9.1. Ejercicios {#fispm-c12-ejercicios-8}

[]{#fispm-t1-c12-e0017}

**Ejercicio 12.17.** Una masa de $2\,\mathrm{kg}$ sube de $y=1\,\mathrm m$ a $y=4\,\mathrm m$ y luego baja a $y=2\,\mathrm m$, recorriendo además varios tramos horizontales. Usa $g=10\,\mathrm{m/s^2}$. Calcula el trabajo del peso en cada tramo vertical y en la historia completa. Si parte con $K_a=30\,\mathrm J$ y una fuerza aplicada realiza $50\,\mathrm J$, sin otros trabajos, calcula $K_b$.

**Solución.** En el ascenso, $W_{g,1}=-20(4-1)=-60\,\mathrm J$; en el descenso, $W_{g,2}=-20(2-4)=40\,\mathrm J$. Los tramos horizontales dan cero. La suma es $-20\,\mathrm J$, igual a $-mg(2-1)$. El balance total produce $K_b=30-20+50=60\,\mathrm J$ y rapidez final $\sqrt{2K_b/m}=\sqrt{60}\,\mathrm{m/s}$. Los datos de trabajo total no permiten calcular la rapidez en la altura máxima, porque no dicen cómo se distribuyó el trabajo aplicado antes de alcanzarla. El resultado final es condicional a una historia que cumpla esos datos y Newton.

[]{#fispm-t1-c12-e0018}

**Ejercicio 12.18.** Una masa de $1\,\mathrm{kg}$ sobre una guía horizontal lisa está unida a un resorte fijo de constante $k=100\,\mathrm{N/m}$. Se suelta desde $x_a=0{,}20\,\mathrm m$. Calcula la rapidez cuando cruza $x=0$ y cuando alcanza $x_b=-0{,}10\,\mathrm m$. Justifica que ambas posiciones pertenecen al movimiento.

**Solución.** Peso y normal realizan trabajo cero. Hasta el origen, el resorte realiza $100(0{,}20)^2/2=2\,\mathrm J$; así, $v^2=4$ y la rapidez es $2\,\mathrm{m/s}$. Hasta $-0{,}10\,\mathrm m$, realiza $50[(0{,}20)^2-(0{,}10)^2]=1{,}5\,\mathrm J$, por lo que la rapidez es $\sqrt3\,\mathrm{m/s}$. Newton tiene la solución $x(t)=0{,}20\cos(10t)$, que verifica la ecuación y los datos iniciales. Cruza el origen en $t=\pi/20$ y alcanza por primera vez $-0{,}10$ en $t=\pi/15$, con velocidad negativa en ambos cruces. La solución temporal comprueba alcance y dirección; el balance por sí solo entregaba las magnitudes.

[]{#rozamiento-y-longitud-recorrida}

[]{#fispm-t1-c12-s10}

[]{#fpm-i-12-s10}

## 12.10. Rozamiento y longitud recorrida {#fispm-c12-rozamiento-y-longitud-recorrida}

El rozamiento cinético muestra por qué la longitud recorrida puede importar aunque los extremos coincidan. En una superficie fija, la fuerza se opone a la velocidad de deslizamiento: al invertir el movimiento se invierte también la fuerza. Los trabajos de ida y vuelta tienen entonces el mismo signo negativo. No se cancelan como los del peso o los de un resorte fijo.[^7]

Consideremos una partícula que desliza por una guía fija. En los intervalos de deslizamiento, escribamos $\mathbf f=-f\mathbf v/|\mathbf v|$, donde $f\geq0$ puede variar a lo largo de la historia. La relación sólo se prescribe para $\mathbf v\ne0$. Los instantes de detención se tratan mediante el modelo de contacto correspondiente; no se define una dirección de fricción cinética dividiendo por cero. Basta para integrar que las fuerzas y velocidades sean regulares por tramos y que los intervalos de reposo tengan velocidad nula.

[]{#fispm-t1-c12-p0015}

**Proposición 12.15 --- Trabajo de una resistencia al deslizamiento sobre una guía fija.** Bajo el modelo anterior, la potencia durante el deslizamiento es $P_f=-f|\mathbf v|$. El trabajo sobre toda la historia es

$$W_f=-\int_{t_a}^{t_b} f(t)|\mathbf v(t)|\,dt=-\int f\,ds\leq0.$$

Si $f$ es constante, $W_f=-fS$, donde $S$ es la longitud total recorrida, con todas las repeticiones.

**Demostración.** proposición 12.10 da $P_f=\mathbf f\cdot\mathbf v=-f\mathbf v\cdot\mathbf v/|\mathbf v|=-f|\mathbf v|$ en cada tramo de deslizamiento. Integrar y usar $ds=|\mathbf v|dt$ produce la primera igualdad y su forma por longitud. Los intervalos de reposo contribuyen cero. Si $f$ es constante, sale de la integral y queda $-f\int ds=-fS$. La desigualdad procede de $f\geq0$ y $ds\geq0$. $\square$

La notación $\int f\,ds$ integra sobre el recorrido realizado, no sobre el conjunto geométrico de puntos visitados. Una vuelta completa cuenta toda su longitud; recorrerla dos veces cuenta el doble. Conocer únicamente $\mathbf r_b-\mathbf r_a$ no basta. Tampoco se puede emplear una integral orientada de $-f\,dx$ para una historia con retrocesos manteniendo el mismo signo de fuerza: al cambiar la dirección cambia el régimen.

Sobre un plano horizontal fijo, sin otras fuerzas verticales, $N=mg$ y la ley cinética de Coulomb da $f=\mu_kmg$. En un plano inclinado recto, bajo las mismas condiciones de contacto, $N=mg\cos\theta$. En una curva vertical la reacción puede depender de rapidez y curvatura; allí no debe sustituirse automáticamente por $mg$. El balance tangencial puede ahorrar cálculo, pero la componente normal de Newton sigue determinando el contacto.

Para un soporte móvil de velocidad local $\mathbf u$, la fricción se opone a la velocidad relativa tangencial $\mathbf w=\mathbf v-\mathbf u$ en el modelo de deslizamiento plano que consideramos. Su potencia sobre la partícula es $\mathbf f\cdot\mathbf v$, que puede ser positiva. Una cinta puede acelerar un bloque: el hecho de que exista deslizamiento no exige que disminuya su energía cinética en el laboratorio.

Si la reacción sobre el soporte es $-\mathbf f$, la suma de potencias de ambas fuerzas es

$$\mathbf f\cdot\mathbf v-\mathbf f\cdot\mathbf u=\mathbf f\cdot\mathbf w=-f|\mathbf w|\leq0.$$

Esta desigualdad se refiere al par de cuerpos y a su deslizamiento relativo. No identifica el trabajo sobre un solo cuerpo con toda la producción térmica. Describir temperatura, deformaciones y energía interna requiere ampliar el modelo; el teorema del punto material sólo contabiliza su energía cinética. La elección del sistema determina qué fuerzas y trabajos figuran en el balance.

[]{#fispm-t1-c12-mp0010}

**Principio metodológico 12.10 --- Distinguir desplazamiento, longitud y deslizamiento relativo.** Para una superficie fija, integra la resistencia con la longitud recorrida. Para un soporte móvil, calcula primero la velocidad relativa que fija la dirección de la fricción y luego la potencia con la velocidad del receptor en el marco elegido. Verifica aparte la normal, la permanencia del contacto y el régimen al detenerse.

[]{#ejercicios-9}

### 12.10.1. Ejercicios {#fispm-c12-ejercicios-9}

[]{#fispm-t1-c12-e0019}

**Ejercicio 12.19.** Una fuerza externa arrastra una partícula de $1\,\mathrm{kg}$ sobre una mesa horizontal fija, primero de $x=0$ a $x=3\,\mathrm m$ y luego hasta $x=1\,\mathrm m$. La fricción cinética tiene magnitud $2\,\mathrm N$. Los tramos se recorren con deslizamiento y la detención de inversión no añade trabajo. Calcula el trabajo de fricción. Si las energías cinéticas inicial y final son iguales, ¿cuánto trabajo realizó la fuerza externa?

**Solución.** La ida mide $3\,\mathrm m$ y la vuelta $2\,\mathrm m$, por lo que $S=5\,\mathrm m$. En la ida la fricción apunta a la izquierda y realiza $-6\,\mathrm J$; en la vuelta apunta a la derecha y realiza $-4\,\mathrm J$. El total es $-10\,\mathrm J$. Usar $-2(1-0)=-2\,\mathrm J$ sería mantener indebidamente la dirección de fuerza. Como peso y normal no hacen trabajo y $\Delta K=0$, el agente externo realizó $10\,\mathrm J$. La igualdad de energías en los extremos no exige rapidez constante durante la inversión.

[]{#fispm-t1-c12-e0020}

**Ejercicio 12.20.** Una partícula desliza hacia abajo por un plano fijo de inclinación $0<\theta<\pi/2$, con rapidez inicial $v_0>0$. El coeficiente cinético es $\mu_k$ y el descenso vertical es $h>0$. Obtén la rapidez candidata al final y las condiciones para alcanzar ese descenso en el régimen supuesto.

**Solución.** La longitud es $s=h/\sin\theta$, el peso realiza $mgh$ y la fricción $-\mu_kmg\cos\theta\,s$. La normal realiza cero. Por tanto,

$$v_b^2=v_0^2+2gh(1-\mu_k\cot\theta).$$

Newton tangencial da aceleración constante $a=g(\sin\theta-\mu_k\cos\theta)$. Si $a\geq0$, todo descenso finito se alcanza con movimiento descendente; para $a=0$ la rapidez permanece $v_0$. Si $a<0$, la primera detención está a $s_*=v_0^2/(2|a|)$, y se alcanza el extremo en la misma rama sólo si $s\leq s_*$. La igualdad da llegada con rapidez cero; después se debe comprobar el modelo estático o el reinicio. Un radicando negativo indica que el extremo no se alcanza por deslizamiento descendente continuo. No se presupone que un bloque en reposo arranque: eso requeriría información sobre fricción estática.

[]{#fispm-t1-c12-e0021}

**Ejercicio 12.21.** Una cinta horizontal se mueve hacia la derecha con velocidad constante $U=4\,\mathrm{m/s}$. Sobre ella se deposita un bloque de masa $m=2\,\mathrm{kg}$, inicialmente en reposo en el laboratorio. Mientras desliza, recibe fricción de magnitud $f=2\,\mathrm N$. Calcula el tiempo hasta igualar velocidades, el trabajo sobre el bloque y el trabajo de la reacción sobre la cinta. Compara su suma con el deslizamiento relativo.

**Solución.** La fricción sobre el bloque apunta a la derecha mientras $v<U$. Newton da $v=ft/m=t$ y $t_*=mU/f=4\,\mathrm s$. El desplazamiento del bloque es $ft_*^2/(2m)=8\,\mathrm m$, así que $W_b=f\Delta x=16\,\mathrm J$, igual a $mU^2/2$. La cinta recorre $Ut_*=16\,\mathrm m$ y recibe la reacción $-f$: su trabajo de contacto es $W_c=-32\,\mathrm J$. La suma vale $-16\,\mathrm J$. La longitud relativa es $\int_0^{t_*}(U-v)dt=8\,\mathrm m$, que multiplicada por $-f$ da el mismo resultado. El motor que mantiene la cinta a velocidad constante debe compensar la reacción; su trabajo no se incluyó entre los dos trabajos de contacto. Tras igualar velocidades termina el régimen cinético supuesto.

[]{#trabajo-de-vínculos-fijos-y-móviles}

[]{#fispm-t1-c12-s11}

[]{#fpm-i-12-s11}

## 12.11. Trabajo de vínculos fijos y móviles {#fispm-c12-trabajo-de-vuxednculos-fijos-y-muxf3viles}

En el capítulo 11 distinguimos la condición geométrica de un vínculo y la fuerza que la hace efectiva. Para calcular trabajo interesa una propiedad concreta: la relación entre la reacción y la velocidad del punto que la recibe. Una guía fija lisa suele imponer perpendicularidad y entonces su reacción no cambia $K$. Una guía móvil puede entregar o retirar energía cinética aun siendo lisa.[^8]

[]{#fig:I-12-R02}

<figure id="fig-fpm-v04-i-12-r02" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-12-R02.svg" class="lightbox" data-gallery="fpm-v04-c12"><img src="/assets/books/fispm/v04/I-12-R02.svg" alt="Un vínculo móvil puede suministrar energía. Diagrama del capítulo 12; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="162" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 12.5.** Una fuerza de vínculo tiene potencia $F\cdot v$ evaluada en el punto sobre el cuerpo. Cuando su punto de aplicación se mueve en la dirección de la fuerza, esa potencia puede ser positiva. No basta invocar idealidad para imponer trabajo nulo. Véase §[12.11](#fispm-c12-trabajo-de-vuxednculos-fijos-y-muxf3viles).

</figcaption>

</figure>

La palabra «lisa» elimina la componente tangencial de contacto en el modelo ideal. No elimina la reacción normal ni garantiza trabajo nulo en todos los marcos. Tampoco la palabra «restricción» determina por sí sola la potencia. Necesitamos conocer la velocidad efectiva del receptor y cómo se mueve el soporte.

[]{#fispm-t1-c12-p0016}

**Proposición 12.16 --- Reacción normal de una guía fija lisa.** Sea una partícula que permanece sobre una curva regular fija $\mathbf r(t)=\boldsymbol\gamma(q(t))$, con $\boldsymbol\gamma'(q)\ne0$. Si su reacción $\mathbf R$ satisface $\mathbf R\cdot\boldsymbol\gamma'=0$, entonces su potencia y su trabajo son cero.

**Demostración.** La regla de la cadena da $\mathbf v=\boldsymbol\gamma'(q)\dot q$. Por proposición 12.10, $P_R=\mathbf R\cdot\mathbf v=(\mathbf R\cdot\boldsymbol\gamma')\dot q=0$. Integrar produce $W_R=0$. El argumento también vale cuando $\dot q=0$ y no exige dividir por rapidez. $\square$

La misma idea vale sobre una superficie fija si la reacción es normal y la velocidad es tangente. En una cuerda inextensible con centro fijo, la tensión radial es perpendicular a la velocidad mientras el hilo permanece tenso. Estos resultados no afirman que la reacción sea pequeña ni irrelevante: puede determinar una aceleración normal grande y decidir si el contacto es posible.

Para una guía que se traslada sin cambiar de forma, escribamos $\mathbf r(t)=\mathbf c(t)+\boldsymbol\gamma(q(t))$. El punto de la guía con etiqueta $q$ tiene velocidad $\dot{\mathbf c}$; la partícula añade su movimiento relativo sobre ella. Supondremos una reacción ideal perpendicular al vector tangente de la guía, sin fricción.

[]{#fispm-t1-c12-p0017}

**Proposición 12.17 --- Potencia de una guía lisa trasladada.** Bajo las hipótesis anteriores,

$$P_R=\mathbf R\cdot\dot{\mathbf c},\qquad W_R=\int_{t_a}^{t_b}\mathbf R\cdot\dot{\mathbf c}\,dt.$$

**Demostración.** Derivar la parametrización da $\mathbf v=\dot{\mathbf c}+\boldsymbol\gamma'\dot q$. El producto escalar con $\mathbf R$ elimina el segundo término porque $\mathbf R\cdot\boldsymbol\gamma'=0$. Proposición 12.10 da la potencia y definición 12.5 su integral. $\square$

La perpendicularidad se establece con la velocidad relativa sobre la guía, no necesariamente con la velocidad del laboratorio. Si la traslación es tangente a una guía recta, la reacción normal sigue realizando trabajo cero; si tiene componente normal puede hacer trabajo. Para un soporte que gira o se deforma, $\dot{\mathbf c}$ no describe toda la velocidad de sus puntos: hay que usar la parametrización temporal completa. Proposición 12.17 se limita deliberadamente a la traslación de una forma fija.

Un caso elemental es una plataforma horizontal lisa que sube con velocidad $U>0$ constante. Una masa que permanece sobre ella comparte la velocidad vertical $U$. Sin otras fuerzas verticales, Newton da $N=mg$. La normal entrega potencia $mgU$ y el peso entrega $-mgU$; la energía cinética permanece constante. La normal realiza trabajo positivo durante el ascenso, aunque no exista rozamiento.

En una plataforma acelerada con altura $c(t)$, la permanencia del contacto exige $N=m[g+\ddot c(t)]\geq0$. Si la expresión necesaria es negativa, una plataforma que sólo empuja no puede ejercerla: se pierde el contacto y cesa la parametrización impuesta. El balance escalar no reemplaza esa desigualdad. Una reacción calculada algebraicamente debe pertenecer al conjunto de fuerzas que el contacto puede realizar.

[]{#fispm-t1-c12-mp0011}

**Principio metodológico 12.11 --- Justificar cada trabajo nulo.** Para omitir una reacción del balance, demuestra que su producto escalar con la velocidad del receptor es cero. En un vínculo móvil, separa movimiento del soporte y movimiento relativo. Después verifica con Newton la reacción y la admisibilidad del contacto; una cuenta correcta de trabajo no sostiene por sí sola una guía unilateral.

[]{#ejercicios-10}

### 12.11.1. Ejercicios {#fispm-c12-ejercicios-10}

[]{#fispm-t1-c12-e0022}

**Ejercicio 12.22.** Una partícula recorre una circunferencia fija lisa de radio $R$, bajo una fuerza tangencial aplicada y una reacción normal. Entre dos puntos, el trabajo tangencial aplicado es $A$. ¿Qué determina ese dato si la rapidez inicial es $v_a$? ¿Permite calcular la reacción?

**Solución.** proposición 12.16 da trabajo normal cero y proposición 12.7 produce $v_b^2=v_a^2+2A/m$, siempre que no haya otras fuerzas con trabajo. Ese valor es necesario y debe ser no negativo. La reacción no sale del trabajo porque es perpendicular a la velocidad. Si la fuerza aplicada es puramente tangencial y no hay otras fuerzas radiales, Newton radial requiere una fuerza hacia el centro de magnitud $mv^2/R$ en cada instante. Para conocer su historia se necesita la rapidez a lo largo de la circunferencia, no sólo su valor final. Una guía capaz de empujar en un único sentido requiere además comprobar el signo de la reacción. El dato $A$ tampoco fija el tiempo empleado ni el punto de llegada por sí mismo.

[]{#fispm-t1-c12-e0023}

**Ejercicio 12.23.** Una masa de $3\,\mathrm{kg}$ permanece sobre una plataforma horizontal lisa cuya altura es $c(t)=t^2/2$ metros durante $0\leq t\leq2\,\mathrm s$. Usa $g=10\,\mathrm{m/s^2}$. Calcula reacción, trabajos del peso y de la normal, y cambio cinético. Comprueba el contacto.

**Solución.** La aceleración vertical es $1\,\mathrm{m/s^2}$ y $N-mg=m\ddot c$ da $N=33\,\mathrm N>0$. La subida es $2\,\mathrm m$, por lo que $W_N=66\,\mathrm J$ y $W_g=-60\,\mathrm J$. La suma vale $6\,\mathrm J$. La velocidad vertical pasa de $0$ a $2\,\mathrm{m/s}$ y $\Delta K=3(2)^2/2=6\,\mathrm J$. La normal es compatible con un contacto que sólo empuja. La energía cinética aumenta por el trabajo neto; eliminar la normal por ser un vínculo liso habría dado un cambio negativo imposible desde el reposo.

[]{#balance-cinético-de-sistemas-de-partículas}

[]{#fispm-t1-c12-s12}

[]{#fpm-i-12-s12}

## 12.12. Balance cinético de sistemas de partículas {#fispm-c12-balance-cinuxe9tico-de-sistemas-de-partuxedculas}

El teorema trabajo--energía puede sumarse sobre un conjunto finito de partículas. La suma exige conservar el receptor de cada fuerza: dos fuerzas iguales y opuestas no realizan necesariamente trabajos opuestos, porque actúan sobre partículas con velocidades distintas. Esta diferencia impide trasladar al trabajo la cancelación de fuerzas internas usada en otros balances.[^9]

Elegimos un sistema de $n$ partículas de masas constantes $m_i>0$, todas medidas en el mismo marco inercial. La lista de partículas es fija durante el intervalo: no entran ni salen cuerpos y no cambia la masa de sus miembros. Suponemos trayectorias de clase $C^2$ y fuerzas continuas por tramos que satisfacen Newton. Un flujo de materia o una masa variable requeriría otro balance.

[]{#fispm-t1-c12-d0009}

**Definición 12.9 --- Energía cinética de un sistema finito.** La energía cinética del sistema es la suma

$$K_{\mathrm{sis}}=\sum_{i=1}^{n}\frac12m_i|\mathbf v_i|^2.$$

Cada término utiliza la velocidad de su partícula. La definición no sustituye todas esas velocidades por una velocidad común ni supone rigidez. Denotemos por $\mathbf F_i^{\mathrm{ext}}$ la suma de fuerzas sobre la partícula $i$ debidas a agentes exteriores al sistema. Denotemos por $\mathbf F_{ij}$ la fuerza sobre $i$ ejercida por $j$. Esta convención fija el receptor en el primer índice y evita intercambiar signos durante la suma. Suponemos que las interacciones internas admiten esta descomposición por pares.

[]{#fispm-t1-c12-p0018}

**Proposición 12.18 --- Balance cinético por suma de partículas.** Si

$$m_i\mathbf a_i=\mathbf F_i^{\mathrm{ext}}+\sum_{j\ne i}\mathbf F_{ij},$$

entonces

$$\frac{dK_{\mathrm{sis}}}{dt}=\sum_i\mathbf F_i^{\mathrm{ext}}\cdot\mathbf v_i+\sum_i\sum_{j\ne i}\mathbf F_{ij}\cdot\mathbf v_i.$$

Al integrar, $\Delta K_{\mathrm{sis}}$ es la suma de los trabajos externos e internos sobre sus respectivos receptores.

**Demostración.** proposición 12.4 aplicado a cada partícula da $dK_i/dt=m_i\mathbf a_i\cdot\mathbf v_i$. Sustituir Newton y distribuir el producto escalar produce la expresión individual. La suma es finita, así que se puede intercambiar con la derivación y la integración. Definición 12.9 identifica la suma de derivadas y definición 12.5 identifica cada integral de potencia con su trabajo. $\square$

Esta identidad no usa todavía la tercera ley. Si además las fuerzas de cada par cumplen $\mathbf F_{ji}=-\mathbf F_{ij}$, las contribuciones internas se agrupan en pares no ordenados. La cancelación vectorial de las fuerzas sigue siendo verdadera, pero las velocidades permanecen en los productos escalares.

[]{#fispm-t1-c12-p0019}

**Proposición 12.19 --- Potencia de un par interno y condición de anulación.** Para un par que satisface acción y reacción,

$$P_{ij}=\mathbf F_{ij}\cdot(\mathbf v_i-\mathbf v_j).$$

Si la fuerza es central y la distancia entre las partículas permanece constante y no nula, esa potencia es cero. En general, acción y reacción por sí solas no la anulan.

**Demostración.** La potencia de las dos fuerzas es $\mathbf F_{ij}\cdot\mathbf v_i+\mathbf F_{ji}\cdot\mathbf v_j=\mathbf F_{ij}\cdot(\mathbf v_i-\mathbf v_j)$. Para una fuerza central escribimos $\mathbf F_{ij}=\lambda(t)(\mathbf r_i-\mathbf r_j)$. La distancia constante implica, al derivar su cuadrado, $(\mathbf r_i-\mathbf r_j)\cdot(\mathbf v_i-\mathbf v_j)=0$. Su producto por $\lambda$ da potencia cero. Sin esa condición, el producto puede tener cualquier signo. $\square$

Así, un resorte entre dos masas puede modificar la suma de sus energías cinéticas aunque no exista fuerza externa. Al reducirse o crecer su deformación, las fuerzas internas pueden realizar trabajo neto positivo o negativo. La condición «aislado» significa aquí ausencia de agentes externos; no significa automáticamente $K_{\mathrm{sis}}$ constante.

Para un modelo de partículas con separaciones rígidas y fuerzas internas centrales, proposición 12.19 permite omitir esas potencias internas. No permite reemplazar el trabajo externo por la resultante externa multiplicada por el desplazamiento de un punto arbitrario: las fuerzas externas pueden actuar en receptores distintos con desplazamientos distintos. La simplificación adicional requiere una relación cinemática justificada.

La frontera del sistema también importa. Si elegimos sólo una masa unida a otra por un resorte, la fuerza del resorte cuenta como externa para esa masa. Si incluimos ambas partículas, pasa al balance interno de pares. Los cálculos físicos son compatibles, pero las listas de trabajos cambian. Una partícula equivalente que represente un cuerpo extenso tampoco describe automáticamente su calentamiento o deformación: el nivel de detalle debe declararse.

[]{#fispm-t1-c12-mp0012}

**Principio metodológico 12.12 --- Elegir el sistema antes de sumar.** Fija sus miembros y calcula la potencia de cada fuerza con la velocidad de su receptor. Agrupa fuerzas internas por pares sólo después de escribir sus dos potencias. Para omitirlas, comprueba una condición que anule el producto con la velocidad relativa; no basta citar acción y reacción.

[]{#ejercicios-11}

### 12.12.1. Ejercicios {#fispm-c12-ejercicios-11}

[]{#fispm-t1-c12-e0024}

**Ejercicio 12.24.** Dos partículas en una línea reciben sólo un par de fuerzas internas. En un instante, la fuerza sobre la primera es $F_{12}=5\,\mathrm N$ hacia la derecha y la de la segunda es $F_{21}=-5\,\mathrm N$. Sus velocidades son $v_1=3\,\mathrm{m/s}$ y $v_2=1\,\mathrm{m/s}$. Calcula las potencias individuales y la tasa de cambio de $K_{\mathrm{sis}}$. ¿Qué ocurriría si ambas velocidades fueran iguales?

**Solución.** La primera potencia es $5\cdot3=15\,\mathrm W$ y la segunda $-5\cdot1=-5\,\mathrm W$. La suma es $10\,\mathrm W$, también $5(3-1)$, por lo que $K_{\mathrm{sis}}$ aumenta a esa tasa pese a que la fuerza total del sistema es cero. El dato corresponde a un instante y no determina un trabajo finito sin conocer la evolución. Si $v_1=v_2$, la potencia del par sería cero en ese instante. Para asegurar trabajo nulo en todo un intervalo tendría que mantenerse esa condición, o una perpendicularidad equivalente, durante el intervalo.

[]{#fispm-t1-c12-e0025}

**Ejercicio 12.25.** Dos partículas están unidas por un resorte ideal sin masa de constante $k$. Sea $q=x_2-x_1-\ell_0$ su deformación con signo. El resorte ejerce $F_{12}=kq$ sobre la primera y $F_{21}=-kq$ sobre la segunda. No hay trabajos externos. Si $q$ pasa de $a$ a $b$, obtén $\Delta K_{\mathrm{sis}}$ y explica por qué no hacen falta velocidades iguales.

**Solución.** La potencia del par es $kq\dot x_1-kq\dot x_2=-kq\dot q$, ya que $\dot q=\dot x_2-\dot x_1$. Integrarla da

$$\Delta K_{\mathrm{sis}}=-\frac{k}{2}(b^2-a^2).$$

El resultado depende de la variación de deformación y permite velocidades diferentes. Si $|b|<|a|$, aumenta la suma cinética. Si las dos velocidades fueran idénticas durante todo el intervalo, $q$ permanecería constante y el trabajo del par sería cero. En este modelo ideal, el resorte se representa mediante las dos fuerzas y no añade un término de energía cinética propio. Las deformaciones propuestas deben pertenecer a la solución dinámica; el balance no garantiza cualquier cambio elegido de $a$ a $b$.

[]{#trabajo-y-energía-cinética-entre-marcos-inerciales}

[]{#fispm-t1-c12-s13}

[]{#fpm-i-12-s13}

## 12.13. Trabajo y energía cinética entre marcos inerciales {#fispm-c12-trabajo-y-energuxeda-cinuxe9tica-entre-marcos-inerciales}

La energía cinética usa velocidades y por eso depende del marco de referencia. El trabajo también depende del marco: el mismo punto receptor puede recorrer desplazamientos diferentes para dos observadores. La igualdad entre trabajo total y cambio cinético se mantiene si ambos lados se calculan coherentemente en cada marco.[^10]

Comparemos marcos inerciales $S$ y $S'$ con ejes paralelos, sin rotación relativa. Elegimos un origen común en $t=0$ y suponemos que el origen de $S'$ se mueve con velocidad constante $\mathbf U$ respecto de $S$. La transformación es $\mathbf r'=\mathbf r-\mathbf U t$, con el mismo tiempo en ambos marcos. Entonces $\mathbf v'=\mathbf v-\mathbf U$ y $\mathbf a'=\mathbf a$. La masa clásica permanece igual.

[]{#fispm-t1-c12-p0020}

**Proposición 12.20 --- Cambio de energía cinética por traslación uniforme.** Para una partícula de masa constante $m$,

$$K'=K-m\mathbf U\cdot\mathbf v+\frac12m|\mathbf U|^2,$$

y entre dos instantes correspondientes, $\Delta K'=\Delta K-m\mathbf U\cdot(\mathbf v_b-\mathbf v_a).$

**Demostración.** definición 12.3 en $S'$ da $K'=m|\mathbf v-\mathbf U|^2/2$. Desarrollar el cuadrado produce $m|\mathbf v|^2/2-m\mathbf U\cdot\mathbf v+m|\mathbf U|^2/2$. Al restar los valores final e inicial, el término constante se cancela y queda la segunda identidad. $\square$

No existe contradicción si una partícula está en reposo para un observador y tiene energía cinética positiva para otro. Tampoco tienen que coincidir los signos de $\Delta K$ y $\Delta K'$. La diferencia incorpora la variación de velocidad proyectada sobre $\mathbf U$, que el balance en un solo marco no elimina.

Para comparar trabajos necesitamos transformar también la ley de fuerza. En la mecánica newtoniana considerada suponemos que la fuerza sobre el mismo receptor tiene el mismo vector en ambos marcos de ejes paralelos, una vez expresados correctamente sus argumentos. Si en $S$ es $\mathbf F(\mathbf r,\mathbf v,t)$, la ley correspondiente en $S'$ es

$$\mathbf F'(\mathbf r',\mathbf v',t)=\mathbf F(\mathbf r'+\mathbf U t,\mathbf v'+\mathbf U,t).$$

No se mantiene por comodidad una dependencia espacial que cambió al mover el origen. Un resorte anclado en reposo en $S$ tiene un apoyo móvil en $S'$. Una fricción debe seguir calculándose con respecto a su superficie: restar $\mathbf U$ tanto al bloque como al soporte conserva su velocidad relativa.

[]{#fispm-t1-c12-p0021}

**Proposición 12.21 --- Transformación del trabajo y coherencia del teorema.** Para una historia de fuerza $\mathbf f(t)$ que representa el mismo vector físico en los dos marcos,

$$W'=W-\mathbf U\cdot\int_{t_a}^{t_b}\mathbf f(t)\,dt.$$

Si $\mathbf f$ es la fuerza total que cumple Newton, entonces $W'=\Delta K'$ cuando $W=\Delta K$.

**Demostración.** definición 12.5 y $\mathbf v'=\mathbf v-\mathbf U$ dan $W'=\int\mathbf f\cdot(\mathbf v-\mathbf U)dt=W-\mathbf U\cdot\int\mathbf fdt$. Para la fuerza total, Newton implica $\int\mathbf fdt=m(\mathbf v_b-\mathbf v_a)$. Sustituir y usar proposición 12.20 prueba $W'=\Delta K-m\mathbf U\cdot(\mathbf v_b-\mathbf v_a)=\Delta K'$. $\square$

El paso que usa Newton se refiere a la fuerza total. Para una contribución individual permanece la primera identidad, pero su integral temporal no puede reemplazarse automáticamente por todo $m(\mathbf v_b-\mathbf v_a)$. Si varias fuerzas actúan, sus correcciones se suman y sólo la suma cumple esa sustitución.

Una fuerza que hace trabajo cero en $S$ puede hacerlo en $S'$. La reacción de una guía fija, por ejemplo, es perpendicular al movimiento relativo sobre esa guía. Para el observador que se traslada, la guía se mueve y la reacción puede tener potencia. Esto concuerda con la proposición 12.17: la velocidad del soporte y la del receptor deben medirse en el mismo marco.

La velocidad relativa entre dos partículas sí permanece igual: $\mathbf v_i'-\mathbf v_j'=\mathbf v_i-\mathbf v_j$. Por eso, para un par interno con fuerzas iguales y opuestas que se transforman según lo supuesto, proposición 12.19 da la misma potencia conjunta en ambos marcos. Cada potencia individual puede cambiar. La anulación de la fuerza total del par hace cancelar las correcciones del trabajo conjunto, sin imponer que su potencia original sea cero.

Estas propiedades requieren traslación uniforme. En un marco acelerado, $\mathbf a'$ ya no coincide con $\mathbf a$ y Newton adopta otra forma. No se debe aplicar proposición 12.21 como si toda elección de observador conservara las mismas ecuaciones sin términos adicionales.

[]{#fispm-t1-c12-mp0013}

**Principio metodológico 12.13 --- Transformar ambos lados del balance.** Declara el marco antes de calcular velocidades, energías y trabajos. Al cambiarlo, transforma la historia del receptor y la ley de fuerza, incluidos los soportes. Compara instantes que representan los mismos eventos físicos y calcula el trabajo y $\Delta K$ íntegramente en el marco solicitado.

[]{#ejercicios-12}

### 12.13.1. Ejercicios {#fispm-c12-ejercicios-12}

[]{#fispm-t1-c12-e0026}

**Ejercicio 12.26.** Una masa de $2\,\mathrm{kg}$ recibe una fuerza horizontal total constante de $2\,\mathrm N$ durante $2\,\mathrm s$. En $S$ parte con velocidad $1\,\mathrm{m/s}$ hacia la derecha. Calcula el trabajo y el cambio cinético en $S$ y en un marco $S'$ que se mueve con $U=2\,\mathrm{m/s}$ hacia la derecha.

**Solución.** La aceleración es $1\,\mathrm{m/s^2}$ y la velocidad final $3\,\mathrm{m/s}$. En $S$, el desplazamiento es $1\cdot2+(1/2)1\cdot2^2=4\,\mathrm m$, así que $W=8\,\mathrm J$. Las energías son $1\,\mathrm J$ y $9\,\mathrm J$, con diferencia $8\,\mathrm J$. En $S'$, las velocidades pasan de $-1$ a $1\,\mathrm{m/s}$ y ambas energías son $1\,\mathrm J$. Su desplazamiento neto es $4-U\cdot2=0$ y $W'=0$. La partícula retrocede y luego avanza en ese marco; el trabajo constante se cancela entre ambos tramos. Proposición 12.21 da igualmente $W'=8-2(2\cdot2)=0$.

[]{#fispm-t1-c12-e0027}

**Ejercicio 12.27.** Una masa de $1\,\mathrm{kg}$ asciende verticalmente en una plataforma lisa a velocidad constante $V=2\,\mathrm{m/s}$ durante $3\,\mathrm s$. Usa $g=10\,\mathrm{m/s^2}$. Compara los trabajos de peso y normal en el laboratorio y en el marco inercial que asciende con la plataforma.

**Solución.** En el laboratorio, $N=mg=10\,\mathrm N$ y el ascenso es $6\,\mathrm m$. La normal realiza $60\,\mathrm J$ y el peso $-60\,\mathrm J$; el trabajo total y $\Delta K$ son cero. En el marco que sube con $V$, la partícula permanece en reposo y ambos trabajos son cero. Proposición 12.21 aplicada a cada contribución resta $V\int Ndt=60\,\mathrm J$ a la normal y resta $V\int(-mg)dt=-60\,\mathrm J$ al peso: se recuperan los dos ceros. La energía cinética vale $2\,\mathrm J$ en el laboratorio y cero en el otro marco, pero sus variaciones coinciden porque la velocidad no cambia. El marco de la plataforma es inercial sólo porque $V$ es constante.

[]{#síntesis-del-método-y-sus-límites}

[]{#fispm-t1-c12-s14}

[]{#fpm-i-12-s14}

## 12.14. Síntesis del método y sus límites {#fispm-c12-suxedntesis-del-muxe9todo-y-sus-luxedmites}

El trabajo relaciona una fuerza con el desplazamiento de su receptor. El teorema trabajo--energía integra la componente de Newton que modifica la rapidez. Esa reducción es especialmente útil cuando se conoce la ley de fuerza a lo largo del recorrido y se busca una magnitud escalar, como una rapidez final o una distancia de frenado. Su utilidad no elimina las componentes de Newton que deciden dirección, curvatura y contacto.

Para organizar un problema, fijamos primero sistema, marco y régimen de fuerzas. Identificamos después el tramo real o la trayectoria supuesta y calculamos cada trabajo con el desplazamiento correspondiente. La suma produce $K_b-K_a$. Sólo entonces interpretamos los valores: verificamos no negatividad, dirección compatible con los datos iniciales, alcance de los eventos y validez de los vínculos. Si se busca tiempo o trayectoria, debemos recuperar la información adicional que el escalar no conserva.

Una fuerza individual puede efectuar trabajo positivo mientras la energía cinética disminuye, si otras contribuciones negativas predominan. Un trabajo neto cero en todo un intervalo asegura igualdad de energías en sus extremos, pero no rapidez constante dentro de él. Para asegurar esta última durante un intervalo basta que la potencia total sea cero en cada instante. La diferencia entre una igualdad integral y una igualdad puntual evita conclusiones temporales que los datos no sostienen.

La reducción también puede aceptar historias que no resuelven Newton. Incluso si una curva satisface exactamente el balance cinético para todos los tiempos, puede tener una aceleración normal que ninguna fuerza declarada produce. El siguiente resultado exhibe esa pérdida de información de manera explícita.

[]{#fispm-t1-c12-p0022}

**Proposición 12.22 --- El balance cinético no determina la ecuación vectorial.** En dimensión al menos dos, la igualdad $dK/dt=\mathbf F\cdot\mathbf v$ no implica en general $m\mathbf a=\mathbf F$, ni siquiera si $\mathbf v$ nunca se anula.

**Demostración.** En el plano tomemos $\mathbf F=\mathbf0$ y la curva $\mathbf r(t)=R(\cos\omega t,\sin\omega t)$, con $R,\omega>0$. Su rapidez es $R\omega$ constante y no nula, por lo que $dK/dt=0=\mathbf F\cdot\mathbf v$ para todo $t$. Sin embargo, $m\mathbf a=-mR\omega^2(\cos\omega t,\sin\omega t)\ne\mathbf0$. La historia satisface la igualdad escalar pero no Newton con la fuerza indicada. $\square$

En términos generales, el balance diferencial sólo exige $(m\mathbf a-\mathbf F)\cdot\mathbf v=0$. Un residuo perpendicular a $\mathbf v$ queda invisible en él. En una línea, donde no existe dirección normal independiente y $v\ne0$, la igualdad $mv\dot v=Fv$ sí permite deducir $m\dot v=F$ al dividir por $v$. En un instante de reposo esa inferencia deja de funcionar: ambos lados del balance de potencia pueden ser cero para aceleraciones diferentes. Debemos volver a la ecuación original o a una prolongación continua justificada.

La hipótesis de masa constante aparece en todas las pruebas cinéticas del capítulo. Si cambia la masa, derivar $m(t)|\mathbf v|^2/2$ añade el término $\dot m|\mathbf v|^2/2$, y el intercambio de materia exige definir qué sistema seguimos. No se puede extender el teorema reemplazando simplemente $m$ por $m(t)$ en sus fórmulas. Del mismo modo, la traslación de marco usada en §13 es uniforme y no representa un observador arbitrariamente acelerado.

[]{#fispm-t1-c12-mp0014}

**Principio metodológico 12.14 --- Usar el balance con sus condiciones de validez.** Selecciona el método de trabajo para la información escalar que permite obtener. Conserva Newton para dirección, reacción y continuación. En cada resultado distingue lo calculado de lo aún necesario: una rapidez candidata, un punto efectivamente alcanzado y un contacto físicamente admisible son conclusiones distintas.

[]{#ejercicios-13}

### 12.14.1. Ejercicios {#fispm-c12-ejercicios-13}

[]{#fispm-t1-c12-e0028}

**Ejercicio 12.28.** Una masa $m$ se declara libre de fuerzas en el plano. Se propone la historia circular de la proposición 12.22. Calcula trabajo total y energía cinética, identifica la fuerza que haría válida la historia y explica por qué la igualdad integral tampoco detecta el error.

**Solución.** Con la fuerza declarada, todo trabajo es cero. La energía cinética de la historia es $mR^2\omega^2/2$ constante, de modo que cualquier comparación entre instantes cumple $W=\Delta K=0$. Para que la historia resuelva Newton se necesita $\mathbf F_{\mathrm{req}}=-m\omega^2\mathbf r(t)$, dirigida hacia el centro. Esa fuerza también realiza trabajo cero porque $\mathbf r\cdot\dot{\mathbf r}=0$. Por tanto, ambas declaraciones producen la misma información cinética, aunque sólo la segunda sostiene la curva. La componente normal no se recupera comparando más pares de instantes del mismo balance escalar.

[]{#fispm-t1-c12-e0029}

**Ejercicio 12.29.** Un bloque de masa $m$ llega con rapidez $v_0>0$ al extremo sin deformar de un resorte fijo horizontal de constante $k>0$. Mientras lo comprime, desliza sobre una mesa con fricción cinética de magnitud constante $f>0$. Usa $x\geq0$ para la compresión. Calcula su primera compresión máxima y justifica que se alcanza. ¿Puede deducirse del balance si el bloque empieza a regresar?

**Solución.** Durante el avance, resorte y fricción realizan $-kx^2/2$ y $-fx$. La normal y el peso realizan cero. La rapidez satisface

$$v^2=v_0^2-\frac{k}{m}x^2-\frac{2f}{m}x.$$

La raíz positiva es $d=[\sqrt{f^2+kmv_0^2}-f]/k$. El radicando $q(x)$ es positivo para $0\leq x<d$ y tiene derivada $q'(d)=-2(kd+f)/m<0$. La rama inicial es $v=+\sqrt{q(x)}$; su tiempo de llegada es $\int_0^d dx/\sqrt{q(x)}$, finito porque cerca de $d$ el integrando es comparable con $(d-x)^{-1/2}$. Así se alcanza la primera detención dentro del régimen supuesto. En ella el resorte empuja hacia el regreso con magnitud $kd$. Si la fricción estática máxima es $f_{s,\max}$, puede sostenerse el reposo cuando $kd\leq f_{s,\max}$; si $kd>f_{s,\max}$ no puede sostenerlo. Sin ese dato no se decide el reinicio. Al regresar, la fricción cinética cambia de signo y debe recalcularse el trabajo con el nuevo tramo.

[]{#fispm-t1-c12-e0030}

**Ejercicio 12.30.** Una partícula desliza sin rozamiento sobre el exterior de un círculo vertical fijo de radio $R$. Parte del punto más alto con rapidez tangencial $v_0>0$, con $v_0^2<gR$. La guía sólo puede empujar hacia afuera. Usa $\theta$ medido desde la vertical superior en el sentido de descenso. Determina la rapidez mientras hay contacto y el primer punto en que se pierde. Comprueba que ese punto se alcanza.

**Solución.** La altura es $y=R\cos\theta$. La normal es radial y proposición 12.16 da trabajo cero. El peso realiza $mgR(1-\cos\theta)$, por lo que

$$v^2=v_0^2+2gR(1-\cos\theta).$$

En dirección hacia el centro, el peso tiene componente $mg\cos\theta$ y la normal, dirigida hacia afuera, componente $-N$. Newton exige $mg\cos\theta-N=mv^2/R$, así que

$$N=mg(3\cos\theta-2)-\frac{mv_0^2}{R}.$$

Inicialmente $N=m(g-v_0^2/R)>0$. La primera anulación ocurre en $\cos\theta_*=(2+v_0^2/(gR))/3$, número entre $2/3$ y $1$. Antes de ella, $N>0$ y $v\geq v_0>0$. Como $\dot\theta=v/R$, el tiempo $\int_0^{\theta_*}R\,d\theta/v(\theta)$ es finito y el punto se alcanza. Una prolongación sobre el círculo más allá requeriría $N<0$, imposible para la guía unilateral. Desde la pérdida de contacto se inicia otra historia con el peso como fuerza, posición y velocidad de separación como datos iniciales. El balance cinético sobre el círculo por sí solo no habría detectado el límite del contacto.

El capítulo completa el cálculo de trabajo, potencia y energía cinética en modelos newtonianos de masa constante. Hemos obtenido trabajos que dependen sólo de extremos en ejemplos específicos y trabajos que dependen del recorrido, del soporte o del marco. El capítulo 13 estudiará cuándo esos cálculos permiten definir una energía potencial, qué condiciones aseguran independencia del camino y cómo se relacionan con conservación y estabilidad. Las pruebas de este capítulo permiten llegar a esa discusión sin confundir el balance de rapidez con la solución completa de la dinámica.

[^1]: Daniel Kleppner y Robert Kolenkow, *An Introduction to Mechanics*, copia Cambridge University Press, 2010, cap. 4, §4.6, ejemplo 4.7, p. 165: trabajo de una fuerza uniforme. La suma poligonal se demuestra localmente y se distingue distancia de desplazamiento.

[^2]: Kleppner--Kolenkow, obra citada, cap. 4, §§4.2--4.3, pp. 153--156; David Morin, *Introduction to Classical Mechanics: With Problems and Solutions*, Cambridge University Press, 2008, cap. 5, §5.1, pp. 140--141, ecuación 5.5 y teorema 5.1. El argumento de la proposición 12.2 usa una primitiva y no divide por velocidad ni exige monotonicidad.

[^3]: Kleppner--Kolenkow, obra citada, cap. 4, §§4.4--4.6, pp. 158--165; Morin, obra citada, cap. 5, §5.3, pp. 148--149, producto escalar y trabajo sobre un camino. Las integrales se definen mediante parametrizaciones explícitas; no se traslada una integración por componentes como si cada eje fuese un recorrido independiente.

[^4]: Kleppner--Kolenkow, obra citada, cap. 4, §§4.4--4.6, pp. 158--164. Proposición 12.7 se prueba mediante Newton y la derivada temporal de $K$, con masa constante y marco inercial. La afirmación sobre trabajo nulo de vínculos se restringe a la perpendicularidad efectiva de una guía fija lisa; no se generaliza a soportes móviles.

[^5]: Kleppner--Kolenkow, obra citada, cap. 4, §4.13, p. 186: definición de potencia y relación $P=\mathbf F\cdot\mathbf v$. Se toma el desarrollo mecánico, sin incorporar como información actual las cifras históricas de rendimiento humano, baterías o consumo nacional del pasaje.

[^6]: Kleppner--Kolenkow, *An Introduction to Mechanics*, copia Cambridge University Press, 2010, cap. 4, §4.2, ejemplos 4.1--4.2, pp. 154--156. Se desarrollan directamente las integrales del peso uniforme y de Hooke, sin introducir todavía el formalismo general de energía potencial. La corrección para un apoyo móvil se deduce localmente de la velocidad del receptor.

[^7]: Kleppner--Kolenkow, obra citada, cap. 4, §4.6, p. 166 y §4.11, ejemplo 4.17, pp. 183--184; Morin, *Introduction to Classical Mechanics*, 2008, cap. 5, §5.1, p. 143. Los argumentos de longitud se restringen a una superficie fija. El balance del par bloque--cinta y la distinción entre trabajo individual y relativo se desarrollan localmente.

[^8]: Kleppner--Kolenkow, obra citada, cap. 4, §4.5, p. 161, trata fuerzas de restricción perpendiculares al movimiento. Proposición 12.16 explicita las condiciones de guía fija y regular; proposición 12.17 y el ejemplo de plataforma se deducen aquí por regla de la cadena y Newton. No se extiende el trabajo nulo a soportes móviles ni se usa el formalismo de d'Alembert.

[^9]: El balance proposición 12.18 y el agrupamiento proposición 12.19 se deducen localmente de Newton, proposición 12.4 y sumas finitas. Morin, obra citada, cap. 5, §5.1, apartado «Work vs. potential energy», pp. 144--146, distingue la descripción de un punto material y la de un cuerpo deformable. Se conserva esa distinción de modelo sin anticipar centro de masa, impulso ni descomposición rotacional.

[^10]: Morin, obra citada, cap. 5, §5.6.1, p. 161, ecuación 5.55: relación galileana de velocidades. Proposición 12.20 y proposición 12.21 se deducen localmente por desarrollo del cuadrado y transformación de la integral de trabajo. No se introduce el marco de centro de masa ni la teoría de impulso de las secciones posteriores.
