---
title: "Tiempo, movimiento y curvas"
subtitle: "Física para matemáticos · Tomo I · Capítulo 5"
author: "A. Peña"
description: "Capítulo 5 del Tomo I de Física para matemáticos, con ejercicios y soluciones desarrolladas."
content-id: MA-BCH-0345
source-id: FISPM-T1-C05
editorial-id: FPM-I-05
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
date-modified: 2026-10-17
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0344"]
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

[Capítulo 4](fisica-para-matematicos-capitulo-4-espacio-euclideo-vectores-y-marcos-de-referencia.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [Capítulo 6](fisica-para-matematicos-capitulo-6-modelos-aproximaciones-escalas-y-linealizacion.md)

[]{#fispm-c05-tiempo-movimiento-y-curvas}

[]{#de-una-localización-a-una-historia-temporal}

[]{#fispm-t1-c05-s01}

[]{#fpm-i-05-s01}

## 5.1. De una localización a una historia temporal {#fispm-c05-de-una-localizaciuxf3n-a-una-historia-temporal}

[]{#el-problema-que-deja-abierto-una-posición-aislada}

### 5.1.1. El problema que deja abierto una posición aislada {#fispm-c05-el-problema-que-deja-abierto-una-posiciuxf3n-aislada}

El capítulo 4 construyó el aparato necesario para responder una pregunta estática: **¿dónde está un punto físico y cómo cambia su descripción al cambiar de marco?** Una vez fijado un marco espacial $F$, una ocurrencia puede registrarse mediante una lectura temporal $t$ y unas coordenadas espaciales $x_F(P)$. Pero un registro aislado no describe movimiento. Saber que un objeto estaba en el punto $P_0$ cuando el reloj marcaba $t_0$ sólo proporciona una localización asociada a un instante. Incluso dos registros,

$$(t_0,P_0), \qquad (t_1,P_1),$$

no determinan por sí solos qué ocurrió entre ambos. La nueva dificultad de este capítulo comienza precisamente aquí: **pasar de localizar ocurrencias a organizar una historia temporal de posiciones**.

Activación Si una cámara registra un objeto a las 12:00 en un punto $P_0$ y a las 12:01 en un punto $P_1$, ¿conocemos ya su movimiento durante todo ese minuto? ¿Qué información falta?

[]{#tiempo-y-posición-son-datos-de-tipos-distintos}

### 5.1.2. Tiempo y posición son datos de tipos distintos {#fispm-c05-tiempo-y-posiciuxf3n-son-datos-de-tipos-distintos}

En el marco clásico adoptado en este tomo, una lectura temporal se representa por un número real

$$t\in I\subseteq\mathbb R,$$

mientras que una posición física es un punto

$$P\in\mathcal E.$$

Estos objetos pertenecen a espacios distintos. El tiempo no es una cuarta coordenada añadida a las tres coordenadas espaciales, y el par $(t,P)$ no será interpretado aquí como un vector de espacio-tiempo. Esa construcción pertenece a la relatividad y queda fuera del alcance del capítulo 5. Si además elegimos un marco espacial fijo $F=(O,B)$, el punto $P$ adquiere una representación numérica

$$x_F(P)\in\mathbb R^3.$$

Por tanto, debemos distinguir al menos:

- la lectura temporal $t\in\mathbb R$;

- el punto físico $P\in\mathcal E$;

- la columna de coordenadas $x_F(P)\in\mathbb R^3$;

- el par $(t,P)$ que vincula una lectura temporal con una localización.

La separación de tipos evita una confusión que sería especialmente peligrosa en este capítulo: **una representación numérica del punto no es el punto, y asociar un tiempo a un punto todavía no produce una ley de movimiento**.

[]{#fispm-c05-definir-evento-cluxe1sico-localizado label="fispm-c05-definir-evento-cluxe1sico-localizado"}

**Definición 5.1 --- Evento clásico localizado** Un **evento clásico localizado** es un par

$$(t,P), \qquad t\in I\subseteq\mathbb R, \qquad P\in\mathcal E,$$

que registra que la ocurrencia considerada está localizada en el punto $P$ para la lectura temporal $t$. La palabra *evento* se usa aquí en un sentido estrictamente clásico y operacional: una ocurrencia a la que asociamos una lectura temporal y una posición espacial. No estamos construyendo un espacio-tiempo ni suponiendo que $(t,P)$ posea estructura vectorial. En un marco fijo $F$, el mismo evento puede registrarse numéricamente como $\bigl(t,x_F(P)\bigr).$

La primera componente no cambia por elegir otro marco **espacial** fijo dentro del alcance actual; la segunda sí cambia según la ley afín estudiada en el capítulo 4.

[]{#principio-metodológico-un-registro-no-es-una-historia}

### 5.1.3. Principio metodológico: un registro no es una historia {#fispm-c05-principio-metodoluxf3gico-un-registro-no-es-una-historia}

**Principio metodológico 5.1 --- Una lectura temporal no es todavía una ley de movimiento** Un dato $(t,P)$ ---o su representación $(t,x_F(P))$--- localiza una ocurrencia. Para describir movimiento se necesitará una regla que asigne posiciones a una colección de valores del parámetro temporal; esa regla se definirá formalmente en §2.

Esta distinción también vale para una lista finita de observaciones. Por ejemplo, $(t_0,P_0),\; (t_1,P_1),\; \dots,\; (t_n,P_n)$

puede constituir un conjunto de datos experimentales, pero no determina automáticamente una única historia entre los instantes registrados. Distintas interpolaciones o modelos pueden ser compatibles con los mismos datos. La física añadirá después criterios para decidir qué descripciones son adecuadas; por ahora sólo fijamos la estructura lógica mínima: **los datos temporales localizados son entradas posibles para construir un movimiento, no el movimiento mismo**.[^1]

[]{#reconstruir-el-evento-desde-sus-coordenadas}

### 5.1.4. Reconstruir el evento desde sus coordenadas {#fispm-c05-reconstruir-el-evento-desde-sus-coordenadas}

Recordemos 4.8: una vez fijado un marco $F=(O,B)$, la aplicación de coordenadas espaciales

$$x_F:\mathcal E\longrightarrow\mathbb R^3$$

es biyectiva. Por ello, la representación numérica de un punto en ese marco determina el punto de manera única.

**Proposición 5.1 --- Reconstrucción de un evento desde un registro en marco fijo** Fijado un marco espacial $F$, todo registro numérico

$$(t,y), \qquad t\in I, \qquad y\in\mathbb R^3,$$

determina unívocamente un evento clásico localizado $(t,P)$ cuyas coordenadas espaciales son $y$.

[]{#fispm-t1-c05-p0008}

**Demostración.** La lectura temporal $t$ ya está dada. Como $F$ está fijado, 4.8 proporciona una aplicación de coordenadas biyectiva $x_F:\mathcal E\to\mathbb R^3$. Por tanto, para la columna $y$ existe un único punto

$$P=x_F^{-1}(y)$$

que satisface $x_F(P)=y$. Así, el registro $(t,y)$ determina exactamente un único par $(t,P)$. $\square$ **Autoexplicación de la prueba.** El argumento sólo reconstruye una **ocurrencia individual**. La biyectividad del sistema de coordenadas recupera el punto a partir de sus números, pero no relaciona posiciones correspondientes a tiempos diferentes. La transición de registros aislados a una aplicación temporal será el paso conceptual siguiente.

[]{#balance-del-primer-tramo}

### 5.1.5. Balance del primer tramo {#fispm-c05-balance-del-primer-tramo}

Hasta aquí hemos añadido tiempo sin introducir todavía cinemática diferencial:

$$\boxed{ \text{lectura temporal} + \text{localización espacial} \longrightarrow \text{evento clásico localizado}. }$$

Todavía no hemos definido trayectoria, velocidad ni aceleración. El siguiente paso dentro de §1 será examinar con más cuidado qué puede y qué no puede inferirse de varios registros temporales y preparar, sin anticiparla, la definición de movimiento parametrizado de §2.

[]{#varios-registros-siguen-siendo-sólo-una-muestra}

### 5.1.6. Varios registros siguen siendo sólo una muestra {#fispm-c05-varios-registros-siguen-siendo-suxf3lo-una-muestra}

Supongamos que observamos el mismo objeto en una sucesión finita de lecturas temporales: $(t_0,P_0),\; (t_1,P_1),\; \dots,\; (t_n,P_n),$

con $t_0<t_1<\cdots<t_n$. Esta colección contiene más información que un solo evento: permite comparar localizaciones en instantes distintos. Sin embargo, sigue siendo una **muestra discreta**. Entre $t_i$ y $t_{i+1}$ no hemos especificado todavía qué punto corresponde a cada lectura temporal intermedia. En un marco fijo $F$, los mismos datos pueden escribirse como

$$\bigl(t_0,x_F(P_0)\bigr),\; \bigl(t_1,x_F(P_1)\bigr),\; \dots,\; \bigl(t_n,x_F(P_n)\bigr).$$

La escritura coordenada facilita cálculos e interpolaciones, pero no elimina la subdeterminación. Dos reglas distintas para las coordenadas pueden coincidir exactamente en todos los tiempos observados y diferir entre ellos. De los datos al modelo Un conjunto finito de registros no contiene por sí mismo los valores no observados. Para completar la historia hace falta introducir una regla adicional ---una hipótesis matemática o física--- y distinguirla de los datos que pretende describir.

[]{#un-ejemplo-de-subdeterminación}

### 5.1.7. Un ejemplo de subdeterminación {#fispm-c05-un-ejemplo-de-subdeterminaciuxf3n}

Para no ocultar unidades dentro de un polinomio, fijemos una escala temporal $T_*>0$ y una escala de longitud $L_*>0$, y trabajemos sólo en este ejemplo con las variables adimensionales

$$\tau:=\frac{t}{T_*}, \qquad \xi:=\frac{x}{L_*}.$$

Supongamos que tres registros de la primera coordenada dan

$$\xi(0)=0, \qquad \xi(1)=1, \qquad \xi(2)=0.$$

La regla

$$\xi_1(\tau)=\tau(2-\tau)$$

reproduce los tres datos. Pero también lo hace

$$\xi_2(\tau)=\tau(2-\tau)+\tau(\tau-1)(\tau-2),$$

porque el término añadido se anula para $\tau=0,1,2$. Las dos reglas no coinciden en general; por ejemplo,

$$\xi_1\!\left(\frac12\right)=\frac34, \qquad \xi_2\!\left(\frac12\right)=\frac98.$$

Por tanto, incluso observaciones exactas en varios instantes no seleccionan automáticamente una única historia temporal. El fenómeno es general: si una regla candidata $\xi_0(\tau)$ reproduce observaciones en $\tau_0,\dots,\tau_n$, entonces

$$\xi_\lambda(\tau) = \xi_0(\tau) + \lambda\prod_{k=0}^{n}(\tau-\tau_k)$$

reproduce los mismos datos para cualquier constante adimensional $\lambda$, aunque las reglas sean diferentes cuando $\lambda\ne0$. Esto no significa que todas las reglas sean físicamente igualmente buenas. Significa algo más elemental: **la elección de una historia requiere información o supuestos que no están contenidos en una lista finita de registros**.

### 5.1.7. Auditoría de tipos de un registro temporal {#fispm-c05-e001-auditoruxeda-de-tipos-de-un-registro-temporal .unnumbered}

**Ejercicio 5.1 · Diagnóstico y tipado** En un marco espacial fijo $F$, un registro experimental entrega $t_0$, un punto $P_0$ y sus coordenadas $x_F(P_0)$. Clasifica los objetos

$$t_0,\qquad P_0,\qquad x_F(P_0),\qquad (t_0,P_0),\qquad \bigl(t_0,x_F(P_0)\bigr),$$

indicando en qué conjunto vive cada uno. Explica después por qué el último objeto, aunque, una vez fijadas las unidades, pueda representarse mediante cuatro números reales, no debe identificarse en el capítulo 5 con un vector de espacio-tiempo.

**Solución desarrollada** Los tipos son

$$t_0\in\mathbb R, \qquad P_0\in\mathcal E, \qquad x_F(P_0)\in\mathbb R^3,$$

y por tanto

$$(t_0,P_0)\in I\times\mathcal E, \qquad \bigl(t_0,x_F(P_0)\bigr)\in I\times\mathbb R^3.$$

El primer par es el evento clásico localizado de la definición 5.1; el segundo es su representación numérica en el marco $F$. Que $I\times\mathbb R^3$ sea un subconjunto de $\mathbb R\times\mathbb R^3$ y pueda representarse mediante cuatro números reales no introduce por sí solo una estructura física de espacio-tiempo. En este capítulo no se ha definido una métrica espacio-temporal, una ley de transformación que mezcle tiempo y espacio ni una interpretación vectorial del evento. Tratar automáticamente esos cuatro números como un vector físico añadiría estructura no autorizada por las definiciones vigentes.

### 5.1.7. Los datos discretos no fijan una historia única {#fispm-c05-e002-los-datos-discretos-no-fijan-una-historia-uxfanica .unnumbered}

**Ejercicio 5.2 · Contraejemplo y modelización** Se fijan escalas $T_*>0$ y $L_*>0$ y se usan las variables adimensionales $\tau=t/T_*$ y $\xi=x/L_*$. En un eje de un marco fijo se registran exactamente los datos

$$\xi(0)=0, \qquad \xi(1)=1, \qquad \xi(2)=0.$$

Construye dos reglas continuas distintas que reproduzcan los tres registros. Verifica que coinciden en los tiempos observados y exhibe un valor intermedio de $\tau$ en el que difieran. Explica qué muestra el ejemplo acerca de la relación entre datos e historia temporal.

**Solución desarrollada** Podemos tomar

$$\xi_1(\tau)=\tau(2-\tau),$$

y

$$\xi_2(\tau)=\tau(2-\tau)+\tau(\tau-1)(\tau-2).$$

Para $\tau=0,1,2$, el producto $\tau(\tau-1)(\tau-2)$ vale cero. Por ello ambas reglas satisfacen exactamente los tres registros dados. En cambio, para $\tau=\tfrac12$,

$$\xi_1\!\left(\frac12\right)=\frac34, \qquad \xi_2\!\left(\frac12\right)=\frac98.$$

Así, los mismos datos discretos son compatibles con historias intermedias diferentes. La conclusión no es que no podamos construir una descripción temporal, sino que **la descripción no se deduce únicamente de una muestra finita**: debe añadirse una regla de interpolación, un modelo o una ley física y después contrastarla con observaciones adicionales.

[]{#cierre-conceptual-del-registro-a-la-regla-temporal}

### 5.1.8. Cierre conceptual: del registro a la regla temporal {#fispm-c05-cierre-conceptual-del-registro-a-la-regla-temporal}

La progresión de esta sección puede resumirse así:

$$\boxed{ \text{localización} \longrightarrow \text{evento }(t,P) \longrightarrow \text{familia de registros} \not\Longrightarrow \text{historia única}. }$$

Un evento individual puede reconstruirse desde sus coordenadas en un marco fijo, pero una lista finita de eventos no rellena automáticamente los intervalos entre observaciones. El paso siguiente consiste, por tanto, en introducir explícitamente **una regla que asigne una posición a cada valor del parámetro temporal considerado**. Esa regla será definida formalmente en §2. Allí podremos distinguir, por primera vez con precisión, la aplicación parametrizada de su imagen geométrica. Hasta entonces no necesitamos velocidad, aceleración ni leyes dinámicas.

[]{#movimiento-parametrizado-y-trayectoria-geométrica}

[]{#fispm-t1-c05-s02}

[]{#fpm-i-05-s02}

## 5.2. Movimiento parametrizado y trayectoria geométrica {#fispm-c05-movimiento-parametrizado-y-trayectoria-geomuxe9trica}

[]{#de-una-muestra-de-eventos-a-una-regla-temporal}

### 5.2.1. De una muestra de eventos a una regla temporal {#fispm-c05-de-una-muestra-de-eventos-a-una-regla-temporal}

En §1 vimos que una colección finita de registros

$$(t_0,P_0),\ldots,(t_n,P_n)$$

no determina una historia única. Para describir matemáticamente una historia debemos añadir algo que los datos aislados no contienen: una regla que asigne una posición a cada lectura temporal del intervalo que queremos estudiar. Elegimos, por tanto, un intervalo

$$I\subseteq\mathbb R,$$

y pedimos que para cada $t\in I$ quede especificado un único punto del espacio físico modelado por $\mathcal E$. Éste es el paso mínimo que convierte una colección de ocurrencias en un objeto matemático capaz de representar movimiento.

Activación ¿Qué información contiene una regla $t\mapsto P(t)$ que no contiene una fotografía de la trayectoria dibujada sobre el espacio?

[]{#definir-movimiento-parametrizado}

### 5.2.2. Definir: movimiento parametrizado {#fispm-c05-definir-movimiento-parametrizado}

**Definición 5.2 --- Movimiento parametrizado de un punto material** Sea $I\subseteq\mathbb R$ un intervalo. Un **movimiento parametrizado de un punto material** es una aplicación

$$P:I\longrightarrow\mathcal E, \qquad t\longmapsto P(t).$$

Para cada $t\in I$, el valor $P(t)$ es el punto ocupado por el objeto modelado en la lectura temporal $t$.[^2]

La definición contiene tres piezas que deben mantenerse separadas: el **dominio** $I$, el **codominio** $\mathcal E$ y la **regla de asignación** $t\mapsto P(t)$. Cambiar cualquiera de ellas puede cambiar el objeto matemático. En definición 5.2 no exigimos todavía continuidad ni derivabilidad. Esas propiedades serán hipótesis adicionales cuando hagan falta. Tampoco introducimos masa, fuerza ni ecuaciones de movimiento: aquí sólo describimos una historia de posiciones.

Punto material El término *punto material* indica la idealización en la que sólo seguimos una localización espacial. No afirma todavía nada sobre masa, dinámica interna, rotación o extensión del cuerpo.

[]{#definir-trayectoria-geométrica}

### 5.2.3. Definir: trayectoria geométrica {#fispm-c05-definir-trayectoria-geomuxe9trica}

A partir de una aplicación $P:I\to\mathcal E$ podemos olvidar qué tiempo corresponde a cada posición y conservar únicamente el conjunto de puntos visitados. Esa operación produce la imagen de $P$.

**Definición 5.3 --- Trayectoria geométrica** La **trayectoria geométrica** del movimiento parametrizado $P:I\to\mathcal E$ es su imagen

$$\Gamma_P:=P(I) =\{P(t):t\in I\} \subseteq\mathcal E.$$

La diferencia de tipos es fundamental: $P:I\to\mathcal E$

es una **aplicación**, mientras que

$$\Gamma_P\subseteq\mathcal E$$

es un **conjunto de puntos**. La trayectoria conserva dónde pasó el movimiento, pero no conserva por sí sola cuándo pasó por cada punto ni cuántas veces lo hizo.

[]{#principio-metodológico-aplicación-imagen-y-parámetro}

### 5.2.4. Principio metodológico: aplicación, imagen y parámetro {#fispm-c05-principio-metodoluxf3gico-aplicaciuxf3n-imagen-y-paruxe1metro}

**Principio metodológico 5.2 --- Separar aplicación, imagen y parámetro** Al analizar una curva, distinguir siempre: el parámetro y su dominio, la aplicación $P$ que asigna puntos y la imagen geométrica $\Gamma_P=P(I)$. Una curva parametrizada contiene más información que su trayectoria.

Esta regla evita una identificación muy común: dibujar una curva en el espacio y tratar el dibujo como si ya especificara el movimiento completo. El dibujo puede representar la imagen, pero no registra necesariamente el orden temporal de los puntos ni la correspondencia entre posiciones y valores de $t$.

[]{#una-misma-imagen-puede-provenir-de-reglas-distintas}

### 5.2.5. Una misma imagen puede provenir de reglas distintas {#fispm-c05-una-misma-imagen-puede-provenir-de-reglas-distintas}

Sean $A,B\in\mathcal E$, con $A\ne B$, y fijemos una escala temporal $T>0$. En $I=[0,T]$ consideremos

$$P(t)=A+\frac{t}{T}\,\overrightarrow{AB},$$

y

$$Q(t)=A+\left(\frac{t}{T}\right)^2\overrightarrow{AB}.$$

Los coeficientes $t/T$ y $(t/T)^2$ son adimensionales y recorren todos los valores de $[0,1]$ cuando $t\in[0,T]$. Por ello ambas aplicaciones tienen la misma imagen: el segmento afín de $A$ a $B$. Sin embargo, las aplicaciones no son iguales. Por ejemplo,

$$P\!\left(\frac{T}{2}\right) =A+\frac12\overrightarrow{AB}, \qquad Q\!\left(\frac{T}{2}\right) =A+\frac14\overrightarrow{AB}.$$

Por tanto,

$$\boxed{P(I)=Q(I)\quad\not\Longrightarrow\quad P=Q.}$$

Todavía no necesitamos hablar de velocidad para distinguirlas: basta observar que, para la misma lectura temporal $t=T/2$, las reglas asignan puntos diferentes.

[]{#balance-del-primer-tramo-1}

### 5.2.6. Balance del primer tramo {#fispm-c05-balance-del-primer-tramo-1}

El paso conceptual de esta sección es

$$\boxed{ \text{regla temporal }P:I\to\mathcal E \quad\Longrightarrow\quad \text{imagen }\Gamma_P=P(I), }$$

pero la flecha no puede invertirse de manera única: conocer sólo la imagen no reconstruye la parametrización. Para precisar qué información se pierde, debemos distinguir al menos dos fenómenos adicionales: el **orden** en que se visitan los puntos y la posibilidad de visitar un mismo punto **más de una vez**. Ninguno de ellos requiere todavía introducir derivadas.

[]{#la-imagen-tampoco-conserva-el-orden-temporal}

### 5.2.7. La imagen tampoco conserva el orden temporal {#fispm-c05-la-imagen-tampoco-conserva-el-orden-temporal}

La pérdida de información al pasar de $P$ a $\Gamma_P$ no consiste sólo en olvidar *en qué instante* se visita cada punto. También puede perderse el **orden** en que se recorren los puntos de la imagen. Sean $A,B\in\mathcal E$, $A\ne B$, y fijemos una escala temporal $T>0$. En el intervalo $I=[0,T]$ consideremos

$$P(t)=A+\frac{t}{T}\,\overrightarrow{AB},$$

y

$$Q(t)=A+\left(1-\frac{t}{T}\right)\overrightarrow{AB}.$$

Ambas aplicaciones tienen como imagen el mismo segmento de $A$ a $B$. Sin embargo, $P(0)=A,\qquad P(T)=B,$

mientras que

$$Q(0)=B,\qquad Q(T)=A.$$

La trayectoria geométrica no contiene ninguna marca que permita decidir cuál de estos dos órdenes temporales fue usado. Error plausible «Si dos movimientos tienen la misma trayectoria, entonces pasan por los mismos puntos en el mismo orden». La igualdad $\Gamma_P=\Gamma_Q$ sólo afirma igualdad de imágenes como conjuntos. No relaciona los valores de $P(t)$ y $Q(t)$ para tiempos concretos.

[]{#una-trayectoria-puede-recorrerse-más-de-una-vez}

### 5.2.8. Una trayectoria puede recorrerse más de una vez {#fispm-c05-una-trayectoria-puede-recorrerse-muxe1s-de-una-vez}

Una aplicación tampoco tiene por qué ser inyectiva. El mismo punto de la trayectoria puede corresponder a varios valores del parámetro temporal. Fijemos otra vez $A\ne B$ y una escala $T>0$. Definamos $R:[0,2T]\to\mathcal E$ por

$$R(t)= \begin{cases} A+\dfrac{t}{T}\,\overrightarrow{AB}, &0\le t\le T,\\[1.2ex] A+\left(2-\dfrac{t}{T}\right)\overrightarrow{AB}, &T\le t\le 2T. \end{cases}$$

Durante el primer tramo temporal la regla asigna sucesivamente los puntos del segmento desde $A$ hasta $B$; durante el segundo vuelve a asignarlos en el orden inverso. Su imagen sigue siendo exactamente el mismo segmento: $\Gamma_R=\{A+s\,\overrightarrow{AB}:0\le s\le1\}.$

Pero la parametrización contiene información adicional. Para cada $s\in(0,1)$, el punto

$$X_s=A+s\,\overrightarrow{AB}$$

aparece en dos tiempos distintos: $t_1=sT, \qquad t_2=(2-s)T.$

Además, $R(0)=R(2T)=A, \qquad R(T)=B.$ Por tanto, conocer $\Gamma_R$ no permite saber cuántas veces se visitó un punto ni cuáles fueron los valores temporales correspondientes. Lectura de una parametrización no inyectiva Si $P(t_1)=P(t_2)$ con $t_1\ne t_2$, no concluyas que «el tiempo se repite». Lo que se repite es la **posición espacial** asignada por la aplicación; los dos valores del parámetro siguen siendo distintos.

### 5.2.8. Misma imagen, orden temporal distinto {#fispm-c05-e003-misma-imagen-orden-temporal-distinto .unnumbered}

**Ejercicio 5.3 · Representación y contraejemplo** Sean $A,B\in\mathcal E$, $A\ne B$, y $T>0$. En $I=[0,T]$ se definen

$$P(t)=A+\frac{t}{T}\,\overrightarrow{AB}, \qquad Q(t)=A+\left(1-\frac{t}{T}\right)\overrightarrow{AB}.$$

1.  Demuestra que $P(I)=Q(I)$.

2.  Compara $P(0),P(T),Q(0),Q(T)$.

3.  Explica qué información conserva la trayectoria común y qué información pierde, sin usar velocidad ni derivadas.

**Solución desarrollada** Cuando $t$ recorre $[0,T]$, el cociente $t/T$ recorre $[0,1]$. Por tanto,

$$P(I)=\{A+s\,\overrightarrow{AB}:0\le s\le1\}.$$

Del mismo modo, $1-t/T$ también toma todos los valores de $[0,1]$, aunque en orden inverso, de modo que

$$Q(I)=\{A+s\,\overrightarrow{AB}:0\le s\le1\}=P(I).$$

Sin embargo, $P(0)=A,\qquad P(T)=B,$

mientras

$$Q(0)=B,\qquad Q(T)=A.$$

La trayectoria común conserva el conjunto de puntos visitados, pero no indica cuál se visita primero ni qué lectura temporal corresponde a cada punto. El ejemplo demuestra directamente que una misma imagen geométrica puede admitir parametrizaciones con órdenes temporales opuestos.

### 5.2.8. Recorrido repetido y multiplicidad de paso {#fispm-c05-e004-recorrido-repetido-y-multiplicidad-de-paso .unnumbered}

**Ejercicio 5.4 · Tipado y lectura geométrica** Sean $A,B\in\mathcal E$, $A\ne B$, $T>0$, y sea $R:[0,2T]\to\mathcal E$ la aplicación

$$R(t)= \begin{cases} A+\dfrac{t}{T}\,\overrightarrow{AB}, &0\le t\le T,\\[1.2ex] A+\left(2-\dfrac{t}{T}\right)\overrightarrow{AB}, &T\le t\le 2T. \end{cases}$$

1.  Determina $\Gamma_R$.

2.  Para $s\in(0,1)$, encuentra todos los tiempos $t$ tales que $$R(t)=A+s\,\overrightarrow{AB}.$$

3.  Determina cuántas veces aparecen $A$ y $B$ en el intervalo $[0,2T]$.

4.  Explica por qué esta información no puede recuperarse conociendo solamente $\Gamma_R$.

**Solución desarrollada** En $0\le t\le T$, el coeficiente de $\overrightarrow{AB}$ es $t/T$ y recorre $[0,1]$. En $T\le t\le2T$, el coeficiente es $2-t/T$ y recorre $[1,0]$. Por ello,

$$\Gamma_R = \{A+s\,\overrightarrow{AB}:0\le s\le1\}.$$

Sea $s\in(0,1)$. En el primer tramo, $\frac{t}{T}=s \quad\Longrightarrow\quad t=sT.$ En el segundo,

$$2-\frac{t}{T}=s \quad\Longrightarrow\quad t=(2-s)T.$$

Como $s\in(0,1)$, estos dos tiempos son distintos y pertenecen respectivamente a $(0,T)$ y $(T,2T)$. Así, cada punto interior del segmento aparece dos veces. Para los extremos, $R(0)=R(2T)=A, \qquad R(T)=B.$ Por tanto, $A$ aparece en dos tiempos y $B$ en uno. La trayectoria $\Gamma_R$ sólo registra que todos esos puntos pertenecen a la imagen; no almacena la preimagen temporal de cada punto ni su multiplicidad de paso.

[]{#cierre-conceptual-qué-se-pierde-al-olvidar-la-parametrización}

### 5.2.9. Cierre conceptual: qué se pierde al olvidar la parametrización {#fispm-c05-cierre-conceptual-quuxe9-se-pierde-al-olvidar-la-parametrizaciuxf3n}

La relación entre movimiento y trayectoria puede resumirse así:

$$\boxed{ P:I\to\mathcal E \quad\xrightarrow{\;\text{tomar imagen}\;} \Gamma_P=P(I) }$$

Al aplicar esta operación podemos perder, entre otras cosas:

- qué valor temporal corresponde a cada punto;

- en qué orden se visitan los puntos;

- si un mismo punto se visita una o varias veces.

Por eso la trayectoria geométrica no debe identificarse con el movimiento parametrizado. Esta distinción será indispensable en §3, donde representaremos una misma curva mediante un origen y un marco fijos sin confundir el objeto geométrico con sus coordenadas. Todavía no hemos usado derivadas; tampoco las necesitaremos para establecer esa relación de representación.

[]{#posición-relativa-y-coordenadas-de-una-curva}

[]{#fispm-t1-c05-s03}

[]{#fpm-i-05-s03}

## 5.3. Posición relativa y coordenadas de una curva {#fispm-c05-posiciuxf3n-relativa-y-coordenadas-de-una-curva}

[]{#un-movimiento-tres-niveles-de-descripción}

### 5.3.1. Un movimiento, tres niveles de descripción {#fispm-c05-un-movimiento-tres-niveles-de-descripciuxf3n}

En §2 construimos un movimiento como una aplicación

$$P:I\longrightarrow\mathcal E.$$

Para cada $t\in I$, el valor $P(t)$ es un **punto** del espacio afín. Sin embargo, para calcular conviene traducir esa historia a objetos que vivan en un espacio vectorial y, después, a columnas numéricas. Fijemos un origen espacial $O\in\mathcal E$. Cada punto $P(t)$ determina entonces el vector

$$\overrightarrow{OP(t)}\in V.$$

Si además fijamos una base ordenada $B=(e_1,e_2,e_3)$ y el marco

$$F=(O,B),$$

ese vector posee una columna de componentes en $\mathbb R^3$. Así aparecen tres niveles distintos:

$$P(t)\in\mathcal E, \qquad \overrightarrow{OP(t)}\in V, \qquad x_F(P(t))\in\mathbb R^3.$$

Activación Si dos columnas numéricas cambian porque elegimos otro origen o base, ¿qué objeto físico-geométrico intentaban representar antes y después del cambio?

[]{#fispm-c05-definir-curva-de-posiciuxf3n-relativa-a-un-origen-fijo label="fispm-c05-definir-curva-de-posiciuxf3n-relativa-a-un-origen-fijo"}

**Definición 5.4 --- Curva de posición relativa a un origen fijo** Sea $P:I\to\mathcal E$ un movimiento parametrizado y sea $O\in\mathcal E$ un origen fijo. Definimos

$$r_O:I\longrightarrow V, \qquad r_O(t):=\overrightarrow{OP(t)}.$$

Para cada $t$, $r_O(t)$ es el vector de posición del punto $P(t)$ relativo al origen elegido $O$. El subíndice $O$ es esencial: la curva $r_O$ depende de la elección de origen. El movimiento geométrico $P$, en cambio, ya estaba definido antes de escogerlo. En toda esta sección, $O$ es una elección **fija**: no depende de $t$.

[]{#definir-curva-coordenada-en-un-marco-fijo}

### 5.3.2. Definir: curva coordenada en un marco fijo {#fispm-c05-definir-curva-coordenada-en-un-marco-fijo}

Fijemos ahora un marco afín

$$F=(O,B), \qquad B=(e_1,e_2,e_3),$$

con origen y base independientes de $t$. El capítulo 4 construyó la aplicación de coordenadas

$$x_F:\mathcal E\longrightarrow\mathbb R^3.$$

Aplicarla punto a punto al movimiento produce una nueva función.

**Definición 5.5 --- Curva coordenada en un marco fijo** Sea $P:I\to\mathcal E$ un movimiento y $F=(O,B)$ un marco fijo. Definimos

$$x_F:I\longrightarrow\mathbb R^3, \qquad x_F(t):=x_F(P(t)).$$

Escribiremos

$$x_F(t)= \begin{pmatrix} x^1(t)\\ x^2(t)\\ x^3(t) \end{pmatrix}.$$

La misma letra $x_F$ se usa, por economía notacional, tanto para la aplicación de coordenadas sobre puntos como para su composición con $P$; el argumento distingue ambos usos: $x_F(P)$ recibe un punto, mientras $x_F(t)$ recibe un valor temporal y significa $x_F(P(t))$.

[]{#relación-punto-a-punto-entre-las-tres-descripciones}

### 5.3.3. Relación punto a punto entre las tres descripciones {#fispm-c05-relaciuxf3n-punto-a-punto-entre-las-tres-descripciones}

Por la definición de coordenadas afines del capítulo 4, para cada $t\in I$ se tiene

$$\boxed{x_F(t)=[r_O(t)]_B.}$$

Si

$$x_F(t)= \begin{pmatrix} x^1(t)\\x^2(t)\\x^3(t) \end{pmatrix},$$

entonces la reconstrucción puntual del capítulo 4 da $P(t) = O+x^1(t)e_1+x^2(t)e_2+x^3(t)e_3.$

Estas igualdades no identifican los objetos. Expresan relaciones de representación entre un punto de $\mathcal E$, un vector de $V$ y una columna de $\mathbb R^3$.

[]{#principio-metodológico-conservar-el-tipo-del-objeto}

### 5.3.4. Principio metodológico: conservar el tipo del objeto {#fispm-c05-principio-metodoluxf3gico-conservar-el-tipo-del-objeto}

**Principio metodológico 5.3 --- Mantener el tipado afín** Durante todo el capítulo distinguir explícitamente

$$P(t)\in\mathcal E, \qquad r_O(t)\in V, \qquad x_F(t)\in\mathbb R^3.$$

Un punto, un vector de posición y su columna de componentes pueden representar una misma localización relativa a elecciones declaradas, pero no son el mismo tipo de objeto. Esta disciplina será especialmente importante cuando aparezcan operaciones algebraicas. En $V$ y en $\mathbb R^3$ podemos sumar y restar elementos según sus estructuras; no debemos trasladar automáticamente esas operaciones a los puntos de $\mathcal E$.

Error plausible «Como $x_F(t)$ es una terna, entonces $P(t)$ es una terna». No: $x_F(t)$ es la representación numérica del punto $P(t)$ en el marco $F$. La biyección de coordenadas permite pasar de uno a otra una vez fijado el marco, pero no convierte $\mathcal E$ en $\mathbb R^3$ de manera canónica.

[]{#balance-representar-sin-confundir}

### 5.3.5. Balance: representar sin confundir {#fispm-c05-balance-representar-sin-confundir}

La cadena de representación construida hasta aquí es

$$\boxed{ P:I\to\mathcal E \quad\xrightarrow{\;O\;} r_O:I\to V \quad\xrightarrow{\;B\;} x_F:I\to\mathbb R^3. }$$

El primer paso requiere elegir un origen; el segundo, además, una base. Ninguna de esas elecciones modifica por sí misma la curva geométrica $P$. Todavía no hemos comparado dos orígenes ni dos marcos. Esa comparación permitirá precisar qué cambia en $r_O$ y en $x_F$ cuando cambia la descripción, y qué permanece asociado al mismo movimiento.

[]{#cambiar-el-origen-cambia-la-curva-de-posición-no-el-movimiento}

### 5.3.6. Cambiar el origen cambia la curva de posición, no el movimiento {#fispm-c05-cambiar-el-origen-cambia-la-curva-de-posiciuxf3n-no-el-movimiento}

Sean $O,O'\in\mathcal E$ dos orígenes fijos y definamos

$$c:=\overrightarrow{OO'}\in V, \qquad O'=O+c.$$

Para cada instante $t$, la ley del triángulo aplicada a $O,O',P(t)$ da

$$\overrightarrow{OP(t)} = \overrightarrow{OO'} + \overrightarrow{O'P(t)}.$$

Por tanto,

$$\overrightarrow{O'P(t)} = \overrightarrow{OP(t)}-c.$$

**Proposición 5.2 --- Cambio de origen de una curva de posición** Sean $O$ y $O'$ dos orígenes fijos y sea

$$c=\overrightarrow{OO'}.$$

Entonces, para todo $t\in I$,

$$\boxed{ r_{O'}(t)=r_O(t)-c. }$$

**Demostración.** Por definición 5.4,

$$r_O(t)=\overrightarrow{OP(t)}, \qquad r_{O'}(t)=\overrightarrow{O'P(t)}.$$

La identidad afín anterior da directamente

$$r_{O'}(t) = \overrightarrow{O'P(t)} = \overrightarrow{OP(t)}-\overrightarrow{OO'} = r_O(t)-c.$$

Como $O$ y $O'$ son fijos, $c$ es el mismo vector para todos los valores de $t$. $\square$ **Autoexplicación de la prueba.** No hemos movido la curva $P$. Sólo hemos cambiado el punto desde el cual construimos sus vectores de posición. Por eso todas las posiciones vectoriales se trasladan por el mismo vector constante $-c$.

[]{#reconstruir-una-curva-desde-una-curva-coordenada}

### 5.3.7. Reconstruir una curva desde una curva coordenada {#fispm-c05-reconstruir-una-curva-desde-una-curva-coordenada}

La representación coordenada no pierde información una vez fijado el marco. El capítulo 4 demostró que

$$x_F:\mathcal E\longrightarrow\mathbb R^3$$

es biyectiva. Podemos aplicar su inversa a cada valor temporal de una función con valores en $\mathbb R^3$.

**Proposición 5.3 --- Reconstrucción de una curva desde sus coordenadas en un marco fijo** Fijado un marco $F=(O,B)$, toda aplicación

$$x:I\longrightarrow\mathbb R^3$$

determina una única aplicación

$$P:I\longrightarrow\mathcal E$$

tal que

$$\boxed{x_F(P(t))=x(t)}$$

para todo $t\in I$.

**Demostración.** Como $x_F:\mathcal E\to\mathbb R^3$ es biyectiva, para cada $t\in I$ existe un único punto

$$P(t):=x_F^{-1}(x(t)).$$

Esta asignación define una aplicación $P:I\to\mathcal E$ y satisface

$$x_F(P(t)) = x_F\!\left(x_F^{-1}(x(t))\right) = x(t).$$

Si $Q:I\to\mathcal E$ tuviera las mismas coordenadas, entonces $x_F(Q(t))=x(t)=x_F(P(t))$

para todo $t$. La inyectividad de $x_F$ implica $Q(t)=P(t)$ para cada $t$, luego $Q=P$. $\square$ **Lectura guiada.** La proposición es punto a punto: no necesita continuidad ni derivadas. Fijado el marco, una historia completa de columnas determina una historia completa de puntos.

[]{#dos-marcos-fijos-describen-la-misma-curva-con-columnas-distintas}

### 5.3.8. Dos marcos fijos describen la misma curva con columnas distintas {#fispm-c05-dos-marcos-fijos-describen-la-misma-curva-con-columnas-distintas}

Sean

$$F=(O,B), \qquad F'=(O',B')$$

dos marcos fijos. Introduzcamos los mismos datos de cambio de marco usados en el capítulo 4:

$$c:=\overrightarrow{OO'}, \qquad S:=S_{B\leftarrow B'}.$$

Por proposición 5.2, $r_{O'}(t)=r_O(t)-c.$

Tomando componentes en la base $B$, $[r_{O'}(t)]_B = [r_O(t)]_B-[c]_B = x_F(t)-[c]_B.$ El cambio de componentes de $B$ a $B'$ da $[r_{O'}(t)]_{B'} = S^{-1}[r_{O'}(t)]_B.$ Como $x_{F'}(t)=[r_{O'}(t)]_{B'}$, obtenemos la ley completa.

**Proposición 5.4 --- Ley afín punto a punto entre dos marcos fijos** Sean $F=(O,B)$ y $F'=(O',B')$ marcos fijos, con

$$c=\overrightarrow{OO'}, \qquad S=S_{B\leftarrow B'}.$$

Entonces, para todo $t\in I$,

$$\boxed{ x_{F'}(t) = S^{-1}\!\left(x_F(t)-[c]_B\right). }$$

[]{#fispm-t1-c05-p0051}

**Demostración.** La derivación precedente prueba la fórmula usando proposición 5.2 y la ley de cambio de componentes del capítulo 4. Equivalentemente, puede aplicarse 4.51 al punto $P(t)$ para cada $t\in I$. Como ambos marcos son fijos, $c$ y $S$ no dependen de $t$. $\square$ **Autoexplicación de la prueba.** La traslación del origen produce el término $-[c]_B$; el cambio de base produce el factor lineal $S^{-1}$. La columna cambia, pero el punto $P(t)$ que ambas columnas representan es el mismo.

Error plausible «Si $x_F(t)$ y $x_{F'}(t)$ son funciones distintas, entonces describen movimientos distintos». No necesariamente. Proposición 5.4 muestra precisamente cómo dos funciones coordenadas diferentes pueden representar la **misma** aplicación geométrica $P:I\to\mathcal E$.

[]{#balance-objeto-geométrico-y-descripciones-fijas}

### 5.3.9. Balance: objeto geométrico y descripciones fijas {#fispm-c05-balance-objeto-geomuxe9trico-y-descripciones-fijas}

Las relaciones construidas en esta sección pueden organizarse como

$$\boxed{ P(t) \;\longleftrightarrow\; r_O(t) \;\longleftrightarrow\; x_F(t), }$$

siempre que las elecciones auxiliares correspondientes estén fijadas. Cambiar de origen modifica $r_O$ mediante una traslación vectorial constante; cambiar de marco modifica $x_F$ mediante una ley afín. Ninguna de estas operaciones, por sí sola, cambia el movimiento geométrico $P$. Esta distinción prepara la comparación entre posiciones correspondientes a **dos instantes distintos**. Esa comparación requerirá formar un desplazamiento entre puntos y pertenece a §4.

### 5.3.9. Cambiar origen sin cambiar la curva física {#fispm-c05-e005-cambiar-origen-sin-cambiar-la-curva-fuxedsica .unnumbered}

**Ejercicio 5.5 · Transferencia y prueba** Sea $P:I\to\mathcal E$ un movimiento y sean $O,O'\in\mathcal E$ dos orígenes fijos con

$$c:=\overrightarrow{OO'}.$$

Supón conocida la curva de posición relativa a $O$, $r_O:I\to V.$

1.  Obtén la curva $r_{O'}$ relativa al origen $O'$.

2.  Reconstruye $P(t)$ usando primero $O$ y después $O'$.

3.  Demuestra que ambas reconstrucciones producen el mismo punto para todo $t\in I$.

**Solución desarrollada** Por proposición 5.2,

$$\boxed{r_{O'}(t)=r_O(t)-c.}$$

Respecto de $O$, la reconstrucción del punto es $P(t)=O+r_O(t).$

Respecto de $O'$, debe ser

$$P(t)=O'+r_{O'}(t).$$

Como $O'=O+c$, sustituimos proposición 5.2:

$$\begin{aligned} O'+r_{O'}(t) &=(O+c)+(r_O(t)-c)\\ &=O+r_O(t). \end{aligned}$$

Por tanto, las dos expresiones reconstruyen exactamente el mismo punto $P(t)$ para cada valor temporal. Cambió el origen usado para representar la posición, no la curva física.

### 5.3.9. Una curva, dos marcos fijos {#fispm-c05-e006-una-curva-dos-marcos-fijos .unnumbered}

**Ejercicio 5.6 · Cálculo e invariancia de representación** Sea

$$F=(O,B), \qquad B=(e_1,e_2,e_3),$$

y define un segundo marco fijo por $O'=O+e_1, \qquad B'=(e_2,e_1,e_3).$ En el marco $F$, una curva tiene coordenadas

$$x_F(t)= \begin{pmatrix} \alpha(t)\\ \beta(t)\\ \gamma(t) \end{pmatrix},$$

donde $\alpha,\beta,\gamma:I\to\mathbb R$ son funciones arbitrarias.

1.  Determina $[c]_B$ para $c=\overrightarrow{OO'}$ y la matriz $S=S_{B\leftarrow B'}$.

2.  Usa proposición 5.4 para calcular $x_{F'}(t)$.

3.  Reconstruye $P(t)$ desde ambos marcos y comprueba punto a punto que se obtiene el mismo punto.

**Solución desarrollada** Como $O'=O+e_1$,

$$c=e_1, \qquad [c]_B= \begin{pmatrix} 1\\0\\0 \end{pmatrix}.$$

Las columnas de $S_{B\leftarrow B'}$ son los vectores de $B'$ expresados en $B$. Por tanto,

$$S= \begin{pmatrix} 0&1&0\\ 1&0&0\\ 0&0&1 \end{pmatrix}, \qquad S^{-1}=S.$$

Proposición 5.4 da

$$\begin{aligned} x_{F'}(t) &=S^{-1}\left(x_F(t)-[c]_B\right)\\ &= \begin{pmatrix} 0&1&0\\ 1&0&0\\ 0&0&1 \end{pmatrix} \begin{pmatrix} \alpha(t)-1\\ \beta(t)\\ \gamma(t) \end{pmatrix}\\ &= \boxed{ \begin{pmatrix} \beta(t)\\ \alpha(t)-1\\ \gamma(t) \end{pmatrix}}. \end{aligned}$$

Desde $F$ reconstruimos

$$P(t) =O+\alpha(t)e_1+\beta(t)e_2+\gamma(t)e_3.$$

Desde $F'$ obtenemos

$$\begin{aligned} P(t) &=O' +\beta(t)e_2 +(\alpha(t)-1)e_1 +\gamma(t)e_3\\ &=O+e_1 +\beta(t)e_2 +(\alpha(t)-1)e_1 +\gamma(t)e_3\\ &=O+\alpha(t)e_1+\beta(t)e_2+\gamma(t)e_3. \end{aligned}$$

Las columnas son distintas, pero ambas reconstruyen el mismo punto $P(t)$ en cada instante. La transformación de coordenadas cambia la descripción, no el movimiento geométrico.

[]{#cierre-conceptual-una-curva-varias-descripciones}

### 5.3.10. Cierre conceptual: una curva, varias descripciones {#fispm-c05-cierre-conceptual-una-curva-varias-descripciones}

La sección deja separadas tres capas:

$$\boxed{ P:I\to\mathcal E, \qquad r_O:I\to V, \qquad x_F:I\to\mathbb R^3. }$$

La primera es el movimiento geométrico. Las otras dos dependen de elecciones auxiliares fijas. Proposición 5.2 describe el efecto de cambiar sólo el origen; proposición 5.3 garantiza que una curva coordenada determina unívocamente la curva geométrica cuando el marco está fijado; proposición 5.4 combina cambio de origen y cambio de base. Por tanto, comparar dos descripciones exige preguntar primero **qué objeto está cambiando**: el movimiento, el origen, la base o sólo sus números. En §4 compararemos, en cambio, dos posiciones de la misma curva correspondientes a tiempos distintos y construiremos a partir de ellas un desplazamiento temporal.

[]{#desplazamiento-temporal-y-velocidad-media}

[]{#fispm-t1-c05-s04}

[]{#fpm-i-05-s04}

## 5.4. Desplazamiento temporal y velocidad media {#fispm-c05-desplazamiento-temporal-y-velocidad-media}

[]{#dos-instantes-dos-puntos-y-un-vector-entre-ellos}

### 5.4.1. Dos instantes, dos puntos y un vector entre ellos {#fispm-c05-dos-instantes-dos-puntos-y-un-vector-entre-ellos}

Hasta ahora hemos estudiado una posición a la vez. Para un movimiento

$$P:I\longrightarrow\mathcal E,$$

dos lecturas temporales $t_1,t_2\in I$ seleccionan dos puntos

$$P(t_1),\qquad P(t_2)\in\mathcal E.$$

Comparar estas posiciones no significa restar números ni dividir puntos. La estructura afín del capítulo 4 ya nos proporciona el objeto correcto: el vector de desplazamiento que lleva el primer punto al segundo.

Activación Si el objeto vuelve al mismo punto después de cierto tiempo, ¿qué debe valer su desplazamiento neto entre esos dos instantes aunque durante el intervalo haya recorrido otros lugares?

[]{#fispm-c05-definir-desplazamiento-entre-dos-instantes label="fispm-c05-definir-desplazamiento-entre-dos-instantes"}

**Definición 5.6 --- Desplazamiento entre dos instantes** Sea $P:I\to\mathcal E$ un movimiento y sean $t_1,t_2\in I$. Definimos el **desplazamiento temporal** desde $t_1$ hasta $t_2$ por

$$\boxed{ \Delta P_{t_1,t_2} := \overrightarrow{P(t_1)P(t_2)} \in V. }$$

El orden importa: $\Delta P_{t_1,t_2}$ apunta desde la posición correspondiente a $t_1$ hacia la posición correspondiente a $t_2$. Por las identidades afines ya demostradas en el capítulo 4, $\Delta P_{t_2,t_1}=-\Delta P_{t_1,t_2},$

y, si $t_1=t_2$, $\Delta P_{t_1,t_1}=0.$ En particular, un desplazamiento nulo entre dos instantes distintos no implica que el movimiento haya permanecido inmóvil entre ellos: sólo afirma que las posiciones inicial y final coinciden.

[]{#desplazamiento-no-es-distancia-recorrida}

### 5.4.2. Desplazamiento no es distancia recorrida {#fispm-c05-desplazamiento-no-es-distancia-recorrida}

El desplazamiento $\Delta P_{t_1,t_2}$ es un **vector**. Su norma es la distancia euclídea entre las dos posiciones extremas:

$$\|\Delta P_{t_1,t_2}\| = d\bigl(P(t_1),P(t_2)\bigr).$$

Esta cantidad sólo compara los extremos. No mide todavía cuánto camino se recorrió entre ellos. Un movimiento puede salir de un punto, seguir una trayectoria larga y regresar al mismo lugar; entonces $\Delta P_{t_1,t_2}=0,$

aunque el camino recorrido no haya sido nulo. La longitud del recorrido se construirá más adelante a partir de particiones y longitud geométrica. Extremos frente a recorrido La norma del desplazamiento es la distancia entre las posiciones inicial y final. No debe llamarse automáticamente «distancia recorrida».

[]{#el-intervalo-temporal-y-el-cociente-medio}

### 5.4.3. El intervalo temporal y el cociente medio {#fispm-c05-el-intervalo-temporal-y-el-cociente-medio}

Para $t_1\ne t_2$, definimos el incremento temporal orientado

$$\Delta t_{12}:=t_2-t_1\ne0.$$

Cuando describimos evolución desde un instante anterior a uno posterior tomaremos normalmente $t_1<t_2$, de modo que $\Delta t_{12}>0$. El dato geométrico disponible es $\Delta P_{t_1,t_2}\in V$; dividir ese vector por el escalar temporal produce de nuevo un vector.

**Definición 5.7 --- Velocidad media en un intervalo temporal** Para $t_1,t_2\in I$ con $t_1\ne t_2$, la **velocidad media** del movimiento entre ambos instantes es

$$\boxed{ \bar v_{[t_1,t_2]} := \frac{\Delta P_{t_1,t_2}}{t_2-t_1} \in V. }$$

La palabra *media* no presupone todavía una función de velocidad instantánea que estemos promediando. En este punto significa simplemente **desplazamiento neto por unidad de intervalo temporal**.[^3]

[]{#principio-metodológico-primero-el-vector-después-el-cociente}

### 5.4.4. Principio metodológico: primero el vector, después el cociente {#fispm-c05-principio-metodoluxf3gico-primero-el-vector-despuuxe9s-el-cociente}

**Principio metodológico 5.4 --- Antes de dividir por tiempo, formar un desplazamiento vectorial legítimo** El cociente temporal debe construirse a partir de

$$\overrightarrow{P(t_1)P(t_2)}\in V,$$

no a partir de una división informal de puntos de $\mathcal E$ por números. Primero se forma un vector bien tipado; sólo entonces puede dividirse por un escalar temporal no nulo. Esta regla será decisiva en §5. Allí el paso de un intervalo temporal finito a uno cada vez más pequeño conservará exactamente el mismo principio de tipado: el numerador seguirá siendo un desplazamiento vectorial.

[]{#auditoría-dimensional-y-frontera-con-la-velocidad-instantánea}

### 5.4.5. Auditoría dimensional y frontera con la velocidad instantánea {#fispm-c05-auditoruxeda-dimensional-y-frontera-con-la-velocidad-instantuxe1nea}

Si las posiciones espaciales tienen dimensión de longitud, entonces $[\Delta P]=L, \qquad [\Delta t]=T,$

y por tanto

$$\boxed{[\bar v]=\frac{L}{T}.}$$

La definición definición 5.7 sólo utiliza dos instantes distintos y un cociente finito. No hemos tomado ningún límite ni definido velocidad instantánea. Tampoco hemos introducido aceleración ni leyes dinámicas. El paso conceptual construido hasta aquí es

$$\boxed{ P(t_1),P(t_2) \longrightarrow \Delta P_{t_1,t_2}\in V \longrightarrow \bar v_{[t_1,t_2]}\in V. }$$

Aún debemos demostrar cómo este desplazamiento se expresa mediante $r_O$, cómo se compone al introducir un tercer instante y cómo cambia su representación entre marcos fijos. Esos resultados completarán §4 antes de cualquier paso al límite.

[]{#el-desplazamiento-como-diferencia-de-posiciones-relativas}

### 5.4.6. El desplazamiento como diferencia de posiciones relativas {#fispm-c05-el-desplazamiento-como-diferencia-de-posiciones-relativas}

Sea $O\in\mathcal E$ un origen fijo. Las posiciones relativas a $O$ son

$$r_O(t_1)=\overrightarrow{OP(t_1)}, \qquad r_O(t_2)=\overrightarrow{OP(t_2)}.$$

La ley del triángulo aplicada a $O,P(t_1),P(t_2)$ da

$$\overrightarrow{OP(t_1)} + \overrightarrow{P(t_1)P(t_2)} = \overrightarrow{OP(t_2)}.$$

Por tanto, el desplazamiento temporal puede recuperarse restando dos vectores de posición construidos respecto del mismo origen.

**Proposición 5.5 --- Desplazamiento temporal como diferencia de posiciones relativas** Para cualquier origen fijo $O\in\mathcal E$ y cualesquiera $t_1,t_2\in I$,

$$\boxed{ \Delta P_{t_1,t_2} = r_O(t_2)-r_O(t_1). }$$

**Demostración.** Por definición 5.4 y definición 5.6,

$$r_O(t_i)=\overrightarrow{OP(t_i)}, \qquad \Delta P_{t_1,t_2}=\overrightarrow{P(t_1)P(t_2)}.$$

La identidad afín anterior implica $r_O(t_1)+\Delta P_{t_1,t_2}=r_O(t_2),$

y, como los tres términos viven en $V$, podemos restar $r_O(t_1)$ en el espacio vectorial: $\Delta P_{t_1,t_2}=r_O(t_2)-r_O(t_1).$

$\square$ **Autoexplicación de la prueba.** No hemos restado puntos. Primero convertimos cada punto en un vector de posición respecto del mismo origen; sólo entonces tomamos una diferencia vectorial. El origen desaparecerá de la diferencia porque contribuye del mismo modo a ambos términos.

[]{#aditividad-al-insertar-un-tercer-instante}

### 5.4.7. Aditividad al insertar un tercer instante {#fispm-c05-aditividad-al-insertar-un-tercer-instante}

Sean $t_1,t_2,t_3\in I$. La ley del triángulo entre los tres puntos de la curva produce inmediatamente una composición temporal de desplazamientos.

**Proposición 5.6 --- Aditividad temporal del desplazamiento** Para cualesquiera $t_1,t_2,t_3\in I$,

$$\boxed{ \Delta P_{t_1,t_2} + \Delta P_{t_2,t_3} = \Delta P_{t_1,t_3}. }$$

**Demostración.** Por definición 5.6,

$$\Delta P_{t_1,t_2} = \overrightarrow{P(t_1)P(t_2)}, \qquad \Delta P_{t_2,t_3} = \overrightarrow{P(t_2)P(t_3)}.$$

La ley del triángulo en el espacio afín da

$$\overrightarrow{P(t_1)P(t_2)} + \overrightarrow{P(t_2)P(t_3)} = \overrightarrow{P(t_1)P(t_3)},$$

que es exactamente la identidad afirmada. $\square$ **Lectura guiada.** El resultado no supone que $t_1<t_2<t_3$; es una identidad algebraica de desplazamientos orientados. Cuando los tiempos están ordenados, además admite la lectura física natural de concatenar dos intervalos consecutivos.

[]{#la-velocidad-media-y-los-cambios-de-descripción-fija}

### 5.4.8. La velocidad media y los cambios de descripción fija {#fispm-c05-la-velocidad-media-y-los-cambios-de-descripciuxf3n-fija}

Proposición 5.5 permite escribir, para cualquier origen fijo $O$,

$$\bar v_{[t_1,t_2]} = \frac{r_O(t_2)-r_O(t_1)}{t_2-t_1}.$$

Si cambiamos a otro origen fijo $O'=O+c$, proposición 5.2 da $r_{O'}(t)=r_O(t)-c.$ Por tanto, $r_{O'}(t_2)-r_{O'}(t_1) = r_O(t_2)-r_O(t_1).$ La traslación constante se cancela antes de dividir por el intervalo temporal. Ahora sean $F=(O,B)$ y $F'=(O',B')$ dos marcos fijos, con

$$c=\overrightarrow{OO'}, \qquad S=S_{B\leftarrow B'}.$$

Proposición 5.4 establece

$$x_{F'}(t) = S^{-1}\!\left(x_F(t)-[c]_B\right).$$

Al restar los valores en $t_2$ y $t_1$,

$$x_{F'}(t_2)-x_{F'}(t_1) = S^{-1}\!\left(x_F(t_2)-x_F(t_1)\right).$$

Dividir por el mismo escalar $t_2-t_1$ sólo transforma las componentes por la matriz lineal $S^{-1}$.

**Proposición 5.7 --- Velocidad media bajo cambios de origen y base fijos** Sean $t_1\ne t_2$. La velocidad media

$$\bar v_{[t_1,t_2]} = \frac{\Delta P_{t_1,t_2}}{t_2-t_1} \in V$$

es independiente de la elección de origen fijo usada para representarla. Si $F=(O,B)$ y $F'=(O',B')$ son dos marcos fijos y $S=S_{B\leftarrow B'}$, entonces sus columnas satisfacen

$$\boxed{ [\bar v_{[t_1,t_2]}]_{B'} = S^{-1}[\bar v_{[t_1,t_2]}]_B. }$$

Equivalentemente,

$$\boxed{ [\bar v_{[t_1,t_2]}]_B = \frac{x_F(t_2)-x_F(t_1)}{t_2-t_1}. }$$

**Demostración.** La independencia respecto del origen sigue de la proposición 5.5 y de la cancelación

$$(r_O(t_2)-c)-(r_O(t_1)-c) = r_O(t_2)-r_O(t_1).$$

Para las componentes, definición 5.5 y proposición 5.5 dan

$$[\Delta P_{t_1,t_2}]_B = x_F(t_2)-x_F(t_1).$$

Dividiendo por $t_2-t_1$ obtenemos la segunda fórmula enmarcada. La ley de cambio de marco de la proposición 5.4 implica

$$x_{F'}(t_2)-x_{F'}(t_1) = S^{-1}\!\left(x_F(t_2)-x_F(t_1)\right),$$

y una nueva división por $t_2-t_1$ produce

$$[\bar v_{[t_1,t_2]}]_{B'} = S^{-1}[\bar v_{[t_1,t_2]}]_B.$$

$\square$ **Autoexplicación de la prueba.** El vector medio es el mismo objeto geométrico; lo que cambia de una base a otra es su columna. La parte traslacional del cambio de marco desaparece porque una diferencia de posiciones elimina cualquier término constante común.

[]{#balance-diferencias-temporales-antes-de-los-límites}

### 5.4.9. Balance: diferencias temporales antes de los límites {#fispm-c05-balance-diferencias-temporales-antes-de-los-luxedmites}

Hasta aquí hemos construido tres hechos puramente finitos:

$$\boxed{ \Delta P_{t_1,t_2} = r_O(t_2)-r_O(t_1), }$$

$$\boxed{ \Delta P_{t_1,t_2}+\Delta P_{t_2,t_3} = \Delta P_{t_1,t_3}, }$$

y

$$\boxed{ [\bar v]_{B'}=S^{-1}[\bar v]_B }$$

para marcos fijos. Ninguna de estas identidades utiliza límites ni derivadas. Los ejercicios siguientes aplican estas propiedades y examinan un caso en que el desplazamiento neto ---y por tanto la velocidad media--- es cero aunque el movimiento no sea constante.

### 5.4.9. Composición temporal de desplazamientos {#fispm-c05-e007-composiciuxf3n-temporal-de-desplazamientos .unnumbered}

**Ejercicio 5.7 · Prueba y tipado** Sea $P:I\to\mathcal E$ un movimiento y sean $t_1,t_2,t_3\in I$ cualesquiera.

1.  Usa proposición 5.5 para expresar $\Delta P_{t_1,t_2}$, $\Delta P_{t_2,t_3}$ y $\Delta P_{t_1,t_3}$ mediante una misma curva de posición relativa $r_O$.

2.  Demuestra $$\Delta P_{t_1,t_2} + \Delta P_{t_2,t_3} = \Delta P_{t_1,t_3}.$$

3.  Explica por qué la suma del lado izquierdo está bien definida y por qué no se está sumando ningún punto de $\mathcal E$.

**Solución desarrollada** Fijemos un origen $O$. Por proposición 5.5,

$$\Delta P_{t_1,t_2} = r_O(t_2)-r_O(t_1),$$

$$\Delta P_{t_2,t_3} = r_O(t_3)-r_O(t_2),$$

y

$$\Delta P_{t_1,t_3} = r_O(t_3)-r_O(t_1).$$

Entonces

$$\begin{aligned} \Delta P_{t_1,t_2} + \Delta P_{t_2,t_3} &= \bigl(r_O(t_2)-r_O(t_1)\bigr) + \bigl(r_O(t_3)-r_O(t_2)\bigr)\\ &= r_O(t_3)-r_O(t_1)\\ &= \Delta P_{t_1,t_3}. \end{aligned}$$

Cada desplazamiento pertenece a $V$, de modo que la suma y las restas son operaciones del espacio vectorial. Los puntos $P(t_i)\in\mathcal E$ sólo intervienen al construir los desplazamientos; nunca se suman directamente entre sí.

### 5.4.9. Velocidad media cero en un movimiento no constante {#fispm-c05-e008-velocidad-media-cero-en-un-movimiento-no-constante .unnumbered}

**Ejercicio 5.8 · Contraejemplo e interpretación** Sean $A,B\in\mathcal E$, con $A\ne B$, y sea $T>0$. Define

$$P:[0,T]\longrightarrow\mathcal E, \qquad P(t) = A + 4\frac{t}{T} \left(1-\frac{t}{T}\right) \overrightarrow{AB}.$$

1.  Calcula $P(0)$, $P(T/2)$ y $P(T)$.

2.  Demuestra que el movimiento no es constante.

3.  Calcula $\Delta P_{0,T}$.

4.  Calcula $\bar v_{[0,T]}$.

5.  Explica por qué una velocidad media nula no implica que el punto haya ocupado siempre la misma posición durante el intervalo.

**Solución desarrollada** En los extremos,

$$P(0)=A, \qquad P(T)=A,$$

porque el coeficiente

$$4\frac{t}{T}\left(1-\frac{t}{T}\right)$$

se anula para $t=0$ y $t=T$. En cambio,

$$P\!\left(\frac{T}{2}\right) = A + 4\left(\frac12\right)\left(\frac12\right) \overrightarrow{AB} = A+\overrightarrow{AB} = B.$$

Como $A\ne B$, la aplicación $P$ no es constante. Sin embargo,

$$\Delta P_{0,T} = \overrightarrow{P(0)P(T)} = \overrightarrow{AA} = 0.$$

Por definición 5.7,

$$\boxed{ \bar v_{[0,T]} = \frac{\Delta P_{0,T}}{T} = 0. }$$

La velocidad media sólo usa el desplazamiento neto entre los extremos del intervalo. Aquí el movimiento parte de $A$, alcanza $B$ en $T/2$ y regresa a $A$ en $T$; por eso el desplazamiento total se cancela aunque la historia temporal sea no constante.

[]{#cierre-conceptual-lo-que-un-cociente-finito-sí-afirma}

### 5.4.10. Cierre conceptual: lo que un cociente finito sí afirma {#fispm-c05-cierre-conceptual-lo-que-un-cociente-finito-suxed-afirma}

La sección ha construido una cadena puramente finita:

$$\boxed{ P(t_1),P(t_2) \longrightarrow \Delta P_{t_1,t_2} \longrightarrow \bar v_{[t_1,t_2]}. }$$

El desplazamiento depende sólo de las dos posiciones extremas y vive en $V$; puede expresarse como diferencia de posiciones relativas respecto de cualquier origen fijo y compone aditivamente al insertar instantes intermedios. La velocidad media es ese vector dividido por un intervalo temporal no nulo. En particular, $\bar v_{[t_1,t_2]}=0$

sólo implica $P(t_1)=P(t_2),$

no que $P$ sea constante entre ambos instantes. El siguiente nivel conceptual será preguntar qué ocurre cuando el segundo instante se acerca al primero. Esa pregunta pertenece a §5 y exigirá un límite; no forma parte de las definiciones ni resultados de esta sección.

[]{#velocidad-instantánea-como-derivada-de-una-curva-afín}

[]{#fispm-t1-c05-s05}

[]{#fpm-i-05-s05}

## 5.5. Velocidad instantánea como derivada de una curva afín {#fispm-c05-velocidad-instantuxe1nea-como-derivada-de-una-curva-afuxedn}

[]{#del-cociente-finito-a-una-pregunta-local}

### 5.5.1. Del cociente finito a una pregunta local {#fispm-c05-del-cociente-finito-a-una-pregunta-local}

En §4 definimos, para $t_1\ne t_2$,

$$\bar v_{[t_1,t_2]} = \frac{\overrightarrow{P(t_1)P(t_2)}}{t_2-t_1}.$$

Esta cantidad compara dos posiciones separadas por un intervalo temporal finito. Para preguntar por el comportamiento del movimiento **en un instante** $t$, fijamos la primera posición y hacemos variar la segunda: $t_1=t, \qquad t_2=t+h.$ Mientras $h\ne0$ y $t+h\in I$, el cociente correspondiente es $\frac{\overrightarrow{P(t)P(t+h)}}{h}\in V.$

[]{#fig:I-05-N02}

<figure id="fig-fpm-v04-i-05-n02" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-05-N02.svg" class="lightbox" data-gallery="fpm-v04-c05"><img src="/assets/books/fispm/v04/I-05-N02.svg" alt="De la secante a la tangente. Diagrama del capítulo 5; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="350" height="268" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 5.1.** Para la parábola $Y=X^2/3$, la secante une dos instantes y la tangente tiene pendiente $2X/3$. En $X=1{,}5$, esa pendiente vale uno. Véase §[5.5](#fispm-c05-velocidad-instantuxe1nea-como-derivada-de-una-curva-afuxedn).

</figcaption>

</figure>

La pregunta instantánea no consiste en «poner $h=0$», porque entonces el cociente dejaría de estar definido. Consiste en estudiar si estos vectores se aproximan a un único vector cuando $h\to0$.

Activación ¿Qué debe permanecer bien tipado mientras el intervalo temporal se hace cada vez más pequeño? ¿Por qué el numerador sigue siendo un vector aunque sus extremos sean puntos?

[]{#derivar-una-curva-con-valores-en-v}

### 5.5.2. Derivar una curva con valores en $V$ {#fispm-c05-derivar-una-curva-con-valores-en-v}

M3 proporciona la derivada para funciones escalares. Aquí necesitamos reconstruir la extensión correspondiente a una curva

$$q:I\longrightarrow V.$$

Como $V$ es un espacio euclídeo, dispone de una norma $\|\cdot\|$. Por tanto, tiene sentido preguntar si una familia de vectores converge en esa norma.

**Definición 5.8 --- Derivada de una curva con valores en $V$** Sea $q:I\to V$ y sea $t$ un punto interior de $I$. Si existe el límite

$$\boxed{ q'(t) := \lim_{h\to0} \frac{q(t+h)-q(t)}{h} }$$

en la norma euclídea de $V$, decimos que $q$ es **derivable en $t$** y llamamos a $q'(t)\in V$ su derivada en ese instante.

La condición de punto interior garantiza que podemos considerar valores de $h$ positivos y negativos suficientemente pequeños con $t+h\in I$. Si $t$ es un extremo de un intervalo, sólo hablaremos de derivada lateral cuando esa convención se declare explícitamente. Definición 5.8 no se importa como una caja negra desde M3. La derivada escalar es un prerrequisito; la extensión a una curva con valores en $V$ forma parte de la interfaz matemática que debemos construir en este capítulo. Su relación con las componentes en una base fija se demostrará más adelante en esta misma sección.

[]{#principio-metodológico-derivar-diferencias-no-puntos}

### 5.5.3. Principio metodológico: derivar diferencias, no puntos {#fispm-c05-principio-metodoluxf3gico-derivar-diferencias-no-puntos}

La forma de la definición 5.8 hace visible una operación esencial: antes de dividir por $h$, el numerador debe ser una **diferencia vectorial legítima**. Esto continúa exactamente el principio usado para la velocidad media.

**Principio metodológico 5.5 --- Derivar diferencias, no puntos** Nunca interpretar una expresión como

$$\frac{P(t)}{t}$$

como velocidad. Un punto $P(t)\in\mathcal E$ no puede dividirse por un escalar. El cociente cinemático debe construirse a partir de un desplazamiento

$$\overrightarrow{P(t)P(t+h)}\in V.$$

Error de tipo Escribir $P(t+h)-P(t)$ sólo es legítimo si previamente se ha pasado a una representación vectorial, por ejemplo $r_O(t+h)-r_O(t)$. Intrínsecamente, entre dos puntos del espacio afín usamos el desplazamiento $\overrightarrow{P(t)P(t+h)}$. Esta disciplina evita que la notación de cálculo oculte la diferencia entre un punto del espacio afín y un vector del espacio asociado.

[]{#definir-velocidad-instantánea}

### 5.5.4. Definir: velocidad instantánea {#fispm-c05-definir-velocidad-instantuxe1nea}

Volvamos ahora al movimiento

$$P:I\longrightarrow\mathcal E.$$

Para $h\ne0$, el cociente

$$\frac{\overrightarrow{P(t)P(t+h)}}{h}$$

es precisamente la velocidad media entre $t$ y $t+h$. Si estos vectores poseen un límite cuando el intervalo temporal colapsa sobre $t$, obtenemos una magnitud instantánea.

**Definición 5.9 --- Velocidad instantánea de una curva afín** Sea $P:I\to\mathcal E$ un movimiento y sea $t$ un punto interior de $I$. Si existe el límite

$$\boxed{ v(t) := \lim_{h\to0} \frac{\overrightarrow{P(t)P(t+h)}}{h} \in V, }$$

llamamos a $v(t)$ la **velocidad instantánea** del movimiento en $t$.[^4]

En un extremo del intervalo sólo emplearemos un límite lateral cuando se declare explícitamente. La existencia de $v(t)$ no se presupone para todo movimiento: es una propiedad adicional de la curva en el instante considerado. La definición es intrínseca respecto de la estructura afín: su numerador es el desplazamiento entre dos puntos de la propia curva. Todavía no hemos demostrado su relación con $r_O'(t)$ ni con las derivadas de las coordenadas; esas equivalencias serán resultados de esta sección.

[]{#principio-metodológico-auditar-las-dimensiones-de-una-derivada-física}

### 5.5.5. Principio metodológico: auditar las dimensiones de una derivada física {#fispm-c05-principio-metodoluxf3gico-auditar-las-dimensiones-de-una-derivada-fuxedsica}

El cociente incremental conserva la misma estructura dimensional que la velocidad media. Si el parámetro $t$ representa tiempo físico y el desplazamiento tiene dimensión de longitud,

$$\left[ \frac{\overrightarrow{P(t)P(t+h)}}{h} \right] = \frac{L}{T}.$$

Si el límite existe, no cambia esa dimensión.

**Principio metodológico 5.6 --- Auditar dimensiones en toda derivada física** Para la velocidad,

$$[v]=\frac{L}{T}.$$

Cuando más adelante se introduzca la aceleración como derivada temporal de la velocidad, deberá cumplirse

$$[a]=\frac{L}{T^2}.$$

La segunda igualdad es aquí sólo una **previsión dimensional**; la aceleración no se define en esta sección.

[]{#balance-del-intervalo-finito-al-límite-vectorial}

### 5.5.6. Balance: del intervalo finito al límite vectorial {#fispm-c05-balance-del-intervalo-finito-al-luxedmite-vectorial}

La transición conceptual puede resumirse así:

$$\boxed{ \frac{\Delta P_{t,t+h}}{h} = \frac{\overrightarrow{P(t)P(t+h)}}{h} \quad\xrightarrow[\;h\to0\;]{} \quad v(t)\in V, }$$

cuando el límite existe. La novedad de §5 no es abandonar el tipado construido antes, sino conservarlo durante el paso al límite: el numerador sigue siendo un desplazamiento vectorial, el cociente vive en $V$ y el límite ---si existe--- también vive en $V$. Quedan por demostrar tres hechos fundamentales antes de completar esta sección: cómo se calcula la derivada de una curva $V$-valuada componente a componente, por qué $v(t)=r_O'(t)$ para cualquier origen fijo y cómo se expresan sus componentes en un marco fijo. Ninguno de ellos requiere todavía introducir recta tangente, regularidad o instantes de reposo; esos conceptos pertenecen a §6.

[]{#proposición-derivación-componente-a-componente}

### 5.5.7. Proposición: derivación componente a componente {#fispm-c05-proposiciuxf3n-derivaciuxf3n-componente-a-componente}

**Proposición 5.8 --- Derivación componente a componente en $V$** Sea

$$q:I\longrightarrow V$$

y sea $B=(e_1,e_2,e_3)$ una base fija. Escribamos

$$[q(t)]_B = \begin{pmatrix} q^1(t)\\ q^2(t)\\ q^3(t) \end{pmatrix}.$$

Para un punto interior $t\in I$, la derivada $q'(t)$ existe si y sólo si existen las tres derivadas escalares

$$(q^1)'(t),\qquad (q^2)'(t),\qquad (q^3)'(t).$$

En ese caso,

$$\boxed{ [q'(t)]_B = \begin{pmatrix} (q^1)'(t)\\ (q^2)'(t)\\ (q^3)'(t) \end{pmatrix}. }$$

**Demostración.** Supongamos primero que las tres derivadas escalares existen. Para $h\ne0$ suficientemente pequeño,

$$\frac{q(t+h)-q(t)}{h} = \sum_{i=1}^{3} \frac{q^i(t+h)-q^i(t)}{h}\,e_i.$$

Definamos

$$w := \sum_{i=1}^{3} (q^i)'(t)e_i.$$

Entonces, por la desigualdad triangular,

$$\left\| \frac{q(t+h)-q(t)}{h}-w \right\| \le \sum_{i=1}^{3} \left| \frac{q^i(t+h)-q^i(t)}{h} - (q^i)'(t) \right| \|e_i\|.$$

Cada término escalar del lado derecho tiende a cero cuando $h\to0$. Como sólo hay tres términos y los vectores de la base son fijos, el lado derecho tiende a cero. Por definición 5.8, $q'(t)=w.$ Por tanto,

$$[q'(t)]_B = \begin{pmatrix} (q^1)'(t)\\ (q^2)'(t)\\ (q^3)'(t) \end{pmatrix}.$$

Supongamos ahora que $q'(t)$ existe. Sea

$$E=(f_1,f_2,f_3)$$

una base ortonormal de $V$, cuya existencia quedó construida en el capítulo 4. Si

$$y_h := \frac{q(t+h)-q(t)}{h},$$

entonces $y_h\longrightarrow q'(t)$

en norma. Para cada $j$,

$$\left| \langle y_h-q'(t),f_j\rangle \right| \le \|y_h-q'(t)\|$$

por Cauchy--Schwarz. Por tanto, las componentes de $y_h$ en la base ortonormal $E$ convergen a las componentes de $q'(t)$ en $E$. Sea

$$S=S_{E\leftarrow B}.$$

La ley de cambio de base del capítulo 4 da $[y_h]_B = S^{-1}[y_h]_E.$ Como $S^{-1}$ es una matriz fija, cada componente de $[y_h]_B$ es una combinación lineal fija de las componentes de $[y_h]_E$ y, por las leyes escalares de límites de M3, $[y_h]_B \longrightarrow [q'(t)]_B.$

Pero

$$[y_h]_B = \begin{pmatrix} \dfrac{q^1(t+h)-q^1(t)}{h}\\[6pt] \dfrac{q^2(t+h)-q^2(t)}{h}\\[6pt] \dfrac{q^3(t+h)-q^3(t)}{h} \end{pmatrix}.$$

Luego existen las tres derivadas escalares y sus valores son precisamente las componentes de $q'(t)$. $\square$ El contenido de la proposición 5.8 es importante por una razón metodológica: podemos **calcular** una derivada vectorial componente a componente en cualquier base fija, pero la derivada resultante sigue siendo un vector de $V$, no una columna privilegiada.

[]{#proposición-la-velocidad-es-la-derivada-del-vector-de-posición}

### 5.5.8. Proposición: la velocidad es la derivada del vector de posición {#fispm-c05-proposiciuxf3n-la-velocidad-es-la-derivada-del-vector-de-posiciuxf3n}

Fijemos un origen $O\in\mathcal E$ y consideremos la curva de posición relativa

$$r_O(t)=\overrightarrow{OP(t)}.$$

La diferencia entre dos valores de esta curva es exactamente el desplazamiento temporal de §4.

**Proposición 5.9 --- Equivalencia entre velocidad afín y derivada del vector de posición** Sea $P:I\to\mathcal E$ un movimiento y sea $t$ un punto interior de $I$. Para cualquier origen fijo $O$, la velocidad $v(t)$ existe si y sólo si existe $r_O'(t)$, y en ese caso

$$\boxed{ v(t)=r_O'(t). }$$

**Demostración.** Por proposición 5.5, aplicado a los instantes $t$ y $t+h$,

$$\overrightarrow{P(t)P(t+h)} = r_O(t+h)-r_O(t).$$

Por tanto, para todo $h\ne0$ admisible,

$$\frac{\overrightarrow{P(t)P(t+h)}}{h} = \frac{r_O(t+h)-r_O(t)}{h}.$$

Los dos cocientes incrementales son literalmente el mismo vector de $V$. En consecuencia, uno posee límite cuando $h\to0$ si y sólo si lo posee el otro, y cuando existe el límite sus valores coinciden: $v(t)=r_O'(t).$

$\square$ proposición 5.9 no identifica el punto $P(t)$ con un vector. La derivada aparece después de elegir un origen sólo porque $r_O$ convierte la curva afín en una curva $V$-valuada; el cociente incremental que determina la velocidad ya era intrínseco.

[]{#corolario-cambiar-un-origen-fijo-no-cambia-la-velocidad}

### 5.5.9. Corolario: cambiar un origen fijo no cambia la velocidad {#fispm-c05-corolario-cambiar-un-origen-fijo-no-cambia-la-velocidad}

La fórmula anterior permite separar una dependencia descriptiva de una cantidad geométrica.

**Proposición 5.10 --- Independencia de la velocidad respecto de un cambio de origen fijo** Sean $O,O'\in\mathcal E$ dos orígenes fijos. Si

$$O'=O+c, \qquad c\in V$$

con $c$ independiente de $t$, entonces, donde la velocidad exista,

$$\boxed{ r_{O'}'(t) = r_O'(t) = v(t). }$$

**Demostración.** Por proposición 5.2,

$$r_{O'}(t) = r_O(t)-c.$$

Como $c$ es constante respecto de $t$, $r_{O'}'(t) = r_O'(t)-0 = r_O'(t).$

Proposición 5.9 identifica ambas derivadas con la misma velocidad intrínseca $v(t)$. $\square$ La hipótesis de **origen fijo** es esencial para el alcance de este capítulo. Si el origen dependiera del tiempo aparecería un término adicional al derivar. Ese problema pertenece a los marcos móviles posteriores y no se anticipará aquí.

[]{#proposición-componentes-de-la-velocidad-en-un-marco-fijo}

### 5.5.10. Proposición: componentes de la velocidad en un marco fijo {#fispm-c05-proposiciuxf3n-componentes-de-la-velocidad-en-un-marco-fijo}

Fijemos ahora un marco geométrico

$$F=(O,B)$$

cuyos datos no dependen del tiempo. La curva coordenada es $x_F(t) = [r_O(t)]_B.$

**Proposición 5.11 --- Componentes de la velocidad en un marco fijo** Sea $P:I\to\mathcal E$ derivable en $t$ y sea $F=(O,B)$ un marco fijo. Si

$$x_F(t) = \begin{pmatrix} x^1(t)\\ x^2(t)\\ x^3(t) \end{pmatrix},$$

entonces

$$\boxed{ [v(t)]_B = \frac{d}{dt}x_F(t) = \begin{pmatrix} \dot x^1(t)\\ \dot x^2(t)\\ \dot x^3(t) \end{pmatrix}. }$$

**Demostración.** Por proposición 5.9,

$$v(t)=r_O'(t).$$

Como $B$ es una base fija, proposición 5.8 aplicado a la curva $r_O:I\to V$ permite derivar sus componentes una a una: $[r_O'(t)]_B = \frac{d}{dt}[r_O(t)]_B.$ Pero

$$[r_O(t)]_B=x_F(t).$$

Por tanto, $[v(t)]_B = \frac{d}{dt}x_F(t).$

$\square$ La igualdad anterior no define la velocidad por coordenadas: expresa en una base fija el vector ya definido intrínsecamente por la definición 5.9. Si cambiamos a otra base fija, las columnas cambian según la ley lineal correspondiente, mientras el vector $v(t)\in V$ permanece siendo el mismo objeto geométrico.

[]{#balance}

### 5.5.11. Balance {#fispm-c05-balance}

La cadena construida en §§5.7--5.10 queda cerrada:

$$\boxed{ \text{cociente incremental afín} \longrightarrow v(t) \longleftrightarrow r_O'(t) \longleftrightarrow \frac{d}{dt}x_F(t) }$$

con una condición que debe permanecer visible: el origen y la base usados para derivar coordenadas son **fijos**. Proposición 5.8 justifica la derivación componente a componente sin importar cálculo multivariable. Proposición 5.9 muestra que la velocidad es la derivada de cualquier vector de posición construido desde un origen fijo. Proposición 5.10 demuestra que el origen fijo se elimina al derivar. Proposición 5.11 proporciona la regla práctica de cálculo en coordenadas sin confundir la representación con el vector. Los ejercicios siguientes obligarán a ejecutar esta cadena desde el cociente incremental, comprobar su independencia respecto del origen y reparar una notación de tipo incorrecto. La recta tangente, la regularidad, los instantes de reposo y la aceleración permanecen fuera de §5.

### 5.5.11. Del cociente secante al vector velocidad {#fispm-c05-e009-del-cociente-secante-al-vector-velocidad .unnumbered}

**Ejercicio 5.9 · Derivación y reconstrucción intrínseca** Sea $F=(O,B)$ un marco fijo con $B=(e_1,e_2,e_3)$ y sea $P:\mathbb R\to\mathcal E$ el movimiento definido por

$$r_O(t) = t^2e_1+t^3e_2+2te_3.$$

1.  Escribe $\overrightarrow{P(1)P(1+h)}$ en la base $B$.

2.  Calcula, para $h\ne0$, el cociente $$\frac{\overrightarrow{P(1)P(1+h)}}{h}.$$

3.  Haz $h\to0$ y determina $v(1)$ usando definición 5.9, sin comenzar derivando directamente las coordenadas.

4.  Verifica después el resultado mediante proposición 5.11.

**Solución desarrollada** Por proposición 5.5, el desplazamiento entre los instantes $1$ y $1+h$ es

$$\overrightarrow{P(1)P(1+h)} = r_O(1+h)-r_O(1).$$

Como $r_O(1)=e_1+e_2+2e_3$

y

$$r_O(1+h) = (1+h)^2e_1+(1+h)^3e_2+2(1+h)e_3,$$

obtenemos

$$\begin{aligned} \overrightarrow{P(1)P(1+h)} &=\bigl((1+h)^2-1\bigr)e_1 +\bigl((1+h)^3-1\bigr)e_2 +2he_3\\ &=(2h+h^2)e_1+(3h+3h^2+h^3)e_2+2he_3. \end{aligned}$$

Para $h\ne0$,

$$\frac{\overrightarrow{P(1)P(1+h)}}{h} = (2+h)e_1+(3+3h+h^2)e_2+2e_3.$$

Al tomar el límite en $V$,

$$\boxed{v(1)=2e_1+3e_2+2e_3.}$$

La verificación coordenada usa

$$x_F(t)= \begin{pmatrix} t^2\\ t^3\\ 2t \end{pmatrix},$$

de modo que proposición 5.11 da

$$[v(1)]_B = \left.\frac{d}{dt} \begin{pmatrix} t^2\\ t^3\\ 2t \end{pmatrix}\right|_{t=1} = \begin{pmatrix} 2\\ 3\\ 2 \end{pmatrix},$$

que representa el mismo vector obtenido intrínsecamente.

### 5.5.11. Independencia del origen {#fispm-c05-e010-independencia-del-origen .unnumbered}

**Ejercicio 5.10 · Invariancia y prueba** Conserva el movimiento y la base $B$ del ejercicio 5.9. Elige ahora otro origen fijo

$$O'=O+c, \qquad c=e_1-2e_2+e_3.$$

1.  Determina $r_{O'}(t)$.

2.  Forma directamente $\bigl(r_{O'}(1+h)-r_{O'}(1)\bigr)/h$.

3.  Calcula el límite cuando $h\to0$.

4.  Explica algebraicamente por qué el mismo argumento funciona para cualquier traslación fija $O'=O+c$.

**Solución desarrollada** Por proposición 5.2,

$$r_{O'}(t)=r_O(t)-c.$$

Por tanto, $r_{O'}(t) = (t^2-1)e_1+(t^3+2)e_2+(2t-1)e_3.$

Al formar la diferencia incremental, el vector constante $c$ se cancela:

$$\begin{aligned} r_{O'}(1+h)-r_{O'}(1) &=\bigl(r_O(1+h)-c\bigr)-\bigl(r_O(1)-c\bigr)\\ &=r_O(1+h)-r_O(1). \end{aligned}$$

En consecuencia, para $h\ne0$,

$$\frac{r_{O'}(1+h)-r_{O'}(1)}{h} = \frac{r_O(1+h)-r_O(1)}{h},$$

y ejercicio 5.9 ya calculó el límite del lado derecho. Así,

$$\boxed{r_{O'}'(1)=r_O'(1)=2e_1+3e_2+2e_3.}$$

El argumento no usa ninguna propiedad especial de $c$ salvo que sea **constante respecto de $t$**. Por eso cualquier cambio de origen fijo desaparece al formar la diferencia y, por la proposición 5.10, no altera la velocidad.

### 5.5.12. ejercicio 5.11 --- Por qué $P(t)/t$ no es velocidad {#fispm-c05-e011-por-quuxe9-ptt-no-es-velocidad}

**Ejercicio 5.11 · Error plausible y reparación** Para el movimiento del ejercicio 5.9, un estudiante escribe

$$\text{«}v(t)=\frac{P(t)}{t}\text{».}$$

1.  Explica por qué la expresión está mal tipada en el espacio afín.

2.  Si el estudiante intenta repararla eligiendo un origen $O$ y escribiendo $r_O(t)/t$, explica por qué esa cantidad tampoco es, en general, la velocidad instantánea.

3.  Compara en $t=1$ el vector $r_O(1)/1$ con el valor correcto $v(1)$.

4.  Escribe la fórmula correcta que debe sustituir al razonamiento del estudiante.

**Solución desarrollada** El punto $P(t)$ pertenece a $\mathcal E$, no al espacio vectorial $V$. En la estructura afín no existe una operación de división de puntos por escalares, de modo que $P(t)/t$ no está definida.

Si elegimos un origen, sí podemos formar el vector $r_O(t)=\overrightarrow{OP(t)}$ y dividirlo por un escalar no nulo. Pero

$$\frac{r_O(t)}{t}$$

compara la posición relativa al origen con el valor del parámetro medido desde $0$; no estudia el cambio local de la posición alrededor del instante $t$. Además, depende de la elección de origen. En $t=1$, $\frac{r_O(1)}{1}=e_1+e_2+2e_3,$

mientras ejercicio 5.9 demostró que

$$v(1)=2e_1+3e_2+2e_3.$$

Los vectores son distintos. La reparación correcta consiste en formar primero un desplazamiento entre dos posiciones cercanas y sólo después dividir por el intervalo temporal:

$$\boxed{ v(t) = \lim_{h\to0} \frac{\overrightarrow{P(t)P(t+h)}}{h}. }$$

Equivalentemente, tras elegir cualquier origen **fijo**, proposición 5.9 permite escribir

$$v(t)=r_O'(t).$$

[]{#cierre-conceptual-derivar-sin-perder-la-geometría}

### 5.5.13. Cierre conceptual: derivar sin perder la geometría {#fispm-c05-cierre-conceptual-derivar-sin-perder-la-geometruxeda}

La sección ha construido la velocidad instantánea sin identificar puntos con vectores. El paso fundamental es

$$\boxed{ P(t),P(t+h) \longrightarrow \overrightarrow{P(t)P(t+h)} \longrightarrow \frac{\overrightarrow{P(t)P(t+h)}}{h} \longrightarrow v(t)\in V. }$$

Cuando se elige un origen fijo, el mismo vector puede calcularse como

$$\boxed{v(t)=r_O'(t),}$$

y, en un marco fijo $F=(O,B)$, sus componentes satisfacen

$$\boxed{[v(t)]_B=\frac{d}{dt}x_F(t).}$$

Estas fórmulas no crean tres conceptos distintos de velocidad. Son tres niveles de descripción del mismo objeto: definición afín intrínseca, representación mediante vector de posición y representación mediante componentes. El cambio de origen fijo desaparece al derivar, mientras un cambio de base fija transforma sólo la columna del vector. Ejercicio 5.9 muestra cómo nace el límite desde secantes afines; ejercicio 5.10 hace visible la invariancia respecto del origen; ejercicio 5.11 derrota el falso amigo $P(t)/t$. El capítulo ya puede pasar, en §6, de la existencia del vector velocidad a la geometría de la dirección tangente, la regularidad y los instantes con velocidad nula. Todavía no se define aceleración ni se introduce dinámica.

[]{#tangente-regularidad-e-instantes-de-reposo}

[]{#fispm-t1-c05-s06}

[]{#fpm-i-05-s06}

## 5.6. Tangente, regularidad e instantes de reposo {#fispm-c05-tangente-regularidad-e-instantes-de-reposo}

[]{#activación-una-velocidad-no-nula-determina-una-dirección}

### 5.6.1. Activación: una velocidad no nula determina una dirección {#fispm-c05-activaciuxf3n-una-velocidad-no-nula-determina-una-direcciuxf3n}

En §5 construimos la velocidad instantánea como un vector

$$v(t_0)\in V.$$

Si este vector es no nulo, contiene una dirección geométrica bien determinada. Esa dirección debe compararse con las secantes de la curva que pasan por el punto

$$P(t_0).$$

Para $h\ne0$ y $t_0+h\in I$, la secante entre $P(t_0)$ y $P(t_0+h)$ posee como vector director el desplazamiento

$$\overrightarrow{P(t_0)P(t_0+h)}.$$

El mismo vector director puede reescalarse por cualquier escalar no nulo sin cambiar la recta. En particular, podemos usar

$$q_h := \frac{\overrightarrow{P(t_0)P(t_0+h)}}{h}.$$

Por definición 5.9, $q_h\longrightarrow v(t_0) \qquad(h\to0)$

cuando la velocidad existe. Así, en un instante con velocidad no nula, los vectores directores de las secantes pueden elegirse de modo que converjan al vector velocidad.

[]{#fig:I-05-R02}

<figure id="fig-fpm-v04-i-05-r02" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-05-R02.svg" class="lightbox" data-gallery="fpm-v04-c05"><img src="/assets/books/fispm/v04/I-05-R02.svg" alt="Un instante singular del parámetro. Diagrama del capítulo 5; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="347" height="276" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 5.2.** La curva $r(u)=(u^3,u^2)$ tiene $r^\prime(0)=0$. La fórmula del vector tangente unitario $r^\prime/\lVert r^\prime\rVert$ no está definida allí. El ejemplo obliga a comprobar regularidad antes de usar esa expresión. Véase §[5.6](#fispm-c05-tangente-regularidad-e-instantes-de-reposo).

</figcaption>

</figure>

Activación Si dos vectores directores difieren sólo por un factor escalar no nulo, ¿describen rectas diferentes o la misma recta? ¿Qué información conserva entonces la recta y qué información del movimiento pierde?

[]{#qué-afirmamos-y-qué-no-al-hablar-de-secantes}

### 5.6.2. Qué afirmamos ---y qué no--- al hablar de secantes {#fispm-c05-quuxe9-afirmamos-y-quuxe9-no-al-hablar-de-secantes}

Para cada $h\ne0$, definamos la recta secante afín

$$\mathcal S_h := \left\{ P(t_0)+\lambda\, \overrightarrow{P(t_0)P(t_0+h)} : \lambda\in\mathbb R \right\}.$$

Como $\overrightarrow{P(t_0)P(t_0+h)} = h\,q_h,$

y $h\ne0$, también podemos escribir

$$\mathcal S_h = \left\{ P(t_0)+\mu q_h : \mu\in\mathbb R \right\}.$$

Esta segunda expresión es la útil para el límite porque

$$q_h\to v(t_0).$$

No introduciremos aquí una topología sobre el conjunto de rectas ni afirmaremos una convergencia de conjuntos $\mathcal S_h$. El contenido suficiente para este capítulo es más elemental: **las secantes admiten vectores directores que convergen al vector velocidad**.

[]{#fispm-c05-definir-instante-regular label="fispm-c05-definir-instante-regular"}

**Definición 5.10 --- Instante regular** Sea $P:I\to\mathcal E$ un movimiento derivable en $t_0$. Decimos que $t_0$ es un **instante regular** si

$$\boxed{v(t_0)\ne0.}$$

La condición de regularidad no afirma que la velocidad sea constante ni que la trayectoria sea una recta. Sólo garantiza que, en ese instante, la velocidad proporciona un vector director no nulo. El calificativo «regular» pertenece aquí a la **parametrización**: exige una propiedad de la derivada de la aplicación $P$. No debe confundirse todavía con una clasificación abstracta de la trayectoria como conjunto geométrico.

[]{#definir-recta-tangente-afín}

### 5.6.3. Definir: recta tangente afín {#fispm-c05-definir-recta-tangente-afuxedn}

**Definición 5.11 --- Recta tangente afín en un instante regular** Si $t_0$ es regular, definimos la **recta tangente afín** al movimiento en $t_0$ por

$$\boxed{ \mathcal T_{t_0} := \left\{ P(t_0)+\lambda v(t_0) : \lambda\in\mathbb R \right\}. }$$

La recta tangente contiene el punto $P(t_0)$ y utiliza $v(t_0)$ como vector director. Como toda recta afín, no distingue entre $v(t_0)$ y cualquier múltiplo escalar no nulo de ese vector. Por ello la recta tangente conserva una **dirección geométrica**, pero no retiene por sí sola la magnitud ni el sentido temporal completo de la velocidad.

[]{#proposición-la-dirección-tangente-nace-de-las-secantes}

### 5.6.4. Proposición: la dirección tangente nace de las secantes {#fispm-c05-proposiciuxf3n-la-direcciuxf3n-tangente-nace-de-las-secantes}

**Proposición 5.12 --- Recta tangente en un instante regular** Sea $P:I\to\mathcal E$ derivable en un punto interior $t_0$ y supongamos que

$$v(t_0)\ne0.$$

Para $h\ne0$ suficientemente pequeño, sea

$$q_h := \frac{\overrightarrow{P(t_0)P(t_0+h)}}{h}.$$

Entonces, para $h\ne0$ suficientemente pequeño:

1.  $q_h\ne0$ y es un vector director de la secante $\mathcal S_h$;

2.  $$q_h\longrightarrow v(t_0);$$

3.  la recta afín determinada por $P(t_0)$ y $v(t_0)$ es $$\mathcal T_{t_0} = \{P(t_0)+\lambda v(t_0):\lambda\in\mathbb R\};$$

4.  para todo $c\ne0$, $$\{P(t_0)+\lambda\,c\,v(t_0):\lambda\in\mathbb R\} = \mathcal T_{t_0}.$$

**Demostración.** Por definición 5.9,

$$q_h\longrightarrow v(t_0)\ne0.$$

Tomemos $\varepsilon=\|v(t_0)\|/2$. Existe $\delta>0$ tal que, si $0<|h|<\delta$, $\|q_h-v(t_0)\|<\frac{\|v(t_0)\|}{2}.$ Si para uno de esos valores fuese $q_h=0$, entonces $\|v(t_0)\|=\|q_h-v(t_0)\|<\frac{\|v(t_0)\|}{2},$

una contradicción. Por tanto, $q_h\ne0$ para $h$ suficientemente pequeño. Además, para $h\ne0$, $\overrightarrow{P(t_0)P(t_0+h)} = h\,q_h.$ Como multiplicar un vector director no nulo por un escalar no nulo no cambia la recta que genera,

$$\mathcal S_h = \{P(t_0)+\mu q_h:\mu\in\mathbb R\}.$$

La recta límite se define entonces por el vector no nulo $v(t_0)$, y por la definición 5.11 es precisamente

$$\mathcal T_{t_0} = \{P(t_0)+\lambda v(t_0):\lambda\in\mathbb R\}.$$

Finalmente, si $c\ne0$,

$$\{P(t_0)+\lambda c\,v(t_0):\lambda\in\mathbb R\} = \{P(t_0)+\mu v(t_0):\mu\in\mathbb R\},$$

porque $\mu=\lambda c$ recorre todos los números reales cuando $\lambda$ los recorre. Por tanto, reescalar un vector director no nulo no altera la recta tangente. $\square$ proposición 5.12 justifica la recta tangente al nivel elemental adoptado en este tratado: no necesitamos una teoría general de variedades ni una noción abstracta de convergencia de rectas. Basta la convergencia de los vectores secantes escalados al vector velocidad.

[]{#principio-metodológico-el-dibujo-no-contiene-la-parametrización}

### 5.6.5. Principio metodológico: el dibujo no contiene la parametrización {#fispm-c05-principio-metodoluxf3gico-el-dibujo-no-contiene-la-parametrizaciuxf3n}

**Principio metodológico 5.7 --- No leer la tangente temporal sólo desde el dibujo de la trayectoria** La imagen geométrica de una curva puede sugerir una dirección tangente, pero no determina por sí sola el vector velocidad.

El vector $v(t_0)$ depende de cómo la curva está parametrizada en torno a $t_0$; la recta tangente olvida parte de esa información porque todos los múltiplos no nulos de $v(t_0)$ generan la misma recta.

Así, debemos distinguir:

$$\boxed{ \text{recta tangente} \ne \text{vector velocidad}. }$$

La primera es una recta afín; el segundo es un vector de $V$ con magnitud y sentido. Más adelante formalizaremos cómo cambia la velocidad bajo reparametrización, pero esa teoría no se necesita para definir la recta tangente en el caso regular.

[]{#balance-del-caso-regular}

### 5.6.6. Balance del caso regular {#fispm-c05-balance-del-caso-regular}

Para un instante regular hemos construido la cadena

$$\boxed{ \text{secantes parametrizadas} \longrightarrow q_h \longrightarrow v(t_0)\ne0 \longrightarrow \mathcal T_{t_0}. }$$

El punto clave es que la tangencia se obtiene sin abandonar la estructura afín: las secantes y la tangente son rectas de $\mathcal E$, mientras sus vectores directores viven en $V$. Queda deliberadamente abierto el caso

$$v(t_0)=0.$$

Cuando la velocidad se anula, definición 5.11 no produce un vector director no nulo y debemos separar cuidadosamente «instante de reposo» de «trayectoria geométricamente degenerada». A continuación analizamos ese caso; todavía no se introduce aceleración.

[]{#el-caso-degenerado-cuando-la-velocidad-se-anula}

### 5.6.7. El caso degenerado: cuando la velocidad se anula {#fispm-c05-el-caso-degenerado-cuando-la-velocidad-se-anula}

Supongamos ahora que el movimiento es derivable en $t_0$ pero

$$v(t_0)=0.$$

En este caso, el procedimiento de la definición 5.11 no produce una recta tangente: el vector cero no puede actuar como vector director de una recta afín. Esto no significa, sin embargo, que la trayectoria geométrica tenga necesariamente una esquina, una cúspide o una degeneración como conjunto. La dificultad pertenece primero a la **parametrización**. La velocidad pregunta cómo cambia $P(t)$ respecto del parámetro temporal; la imagen

$$\Gamma=P(I)$$

sólo registra qué puntos fueron recorridos. Dos movimientos pueden tener la misma imagen y comportarse de forma distinta respecto del parámetro.

[]{#fispm-c05-definir-instante-de-reposo label="fispm-c05-definir-instante-de-reposo"}

**Definición 5.12 --- Instante de reposo** Sea $P:I\to\mathcal E$ un movimiento derivable en $t_0$. Decimos que $t_0$ es un **instante de reposo** si

$$\boxed{v(t_0)=0.}$$

La definición es puntual. Afirma que la velocidad se anula en ese instante; no afirma que el movimiento sea constante en un intervalo alrededor de $t_0$. Por tanto,

$$\boxed{ \text{instante de reposo} \not\Rightarrow \text{movimiento constante en un entorno} }$$

sin hipótesis adicionales.

[]{#primer-contraste-reposo-instantáneo-sin-reposo-permanente}

### 5.6.8. Primer contraste: reposo instantáneo sin reposo permanente {#fispm-c05-primer-contraste-reposo-instantuxe1neo-sin-reposo-permanente}

Sea $u\in V$ no nulo y fijemos un punto $A\in\mathcal E$. Consideremos

$$P:\mathbb R\longrightarrow\mathcal E, \qquad P(t)=A+t^3u.$$

Respecto del origen $A$, la curva de posición es $r_A(t)=t^3u,$

y por la proposición 5.9, $v(t)=r_A'(t)=3t^2u.$ En particular,

$$\boxed{v(0)=0,}$$

de modo que $t=0$ es un instante de reposo según la definición 5.12. Pero el movimiento no es constante: si $t\ne0$, entonces $P(t)=A+t^3u\ne A.$ El punto se aproxima a $A$, alcanza velocidad nula en $t=0$ y continúa ocupando posiciones distintas para valores posteriores del parámetro.

[]{#segundo-contraste-la-misma-imagen-puede-admitir-una-parametrización-regular}

### 5.6.9. Segundo contraste: la misma imagen puede admitir una parametrización regular {#fispm-c05-segundo-contraste-la-misma-imagen-puede-admitir-una-parametrizaciuxf3n-regular}

El ejemplo anterior permite aislar la diferencia entre movimiento e imagen. Como la función

$$t\longmapsto t^3$$

recorre todos los números reales, la trayectoria de $P$ es $\Gamma_P = \{A+\lambda u:\lambda\in\mathbb R\},$

es decir, una recta afín completa. Consideremos ahora otro movimiento

$$Q:\mathbb R\longrightarrow\mathcal E, \qquad Q(s)=A+su.$$

Su trayectoria es exactamente la misma:

$$\Gamma_Q = \{A+\lambda u:\lambda\in\mathbb R\} = \Gamma_P.$$

Sin embargo, $v_Q(s)=u\ne0$

para todo $s$, mientras que $P$ satisface

$$v_P(0)=0.$$

Así, una velocidad nula en una parametrización no autoriza a concluir que la **imagen geométrica** sea singular o degenerada. En este ejemplo, la imagen es la misma recta afín que admite la parametrización regular $Q$. Error plausible «Si $v(t_0)=0$, entonces la trayectoria no tiene dirección geométrica en $P(t_0)$.»

La conclusión es demasiado fuerte. Lo único que podemos afirmar con las definiciones 5.10--5.12 es que **esa parametrización**, en ese instante, no suministra un vector velocidad no nulo con el cual definir definición 5.11. La geometría de la imagen puede ser perfectamente simple, como muestra $P(t)=A+t^3u$.

[]{#qué-sí-puede-concluirse-de-vt_00}

### 5.6.10. Qué sí puede concluirse de $v(t_0)=0$ {#fispm-c05-quuxe9-suxed-puede-concluirse-de-vt_00}

De la igualdad $v(t_0)=0$

podemos concluir exactamente:

- $t_0$ no es regular según la definición 5.10;

- $t_0$ es un instante de reposo según la definición 5.12;

- definición 5.11 no define allí una recta tangente usando la velocidad como vector director.

No podemos concluir sólo a partir de esa igualdad:

- que $P$ sea constante cerca de $t_0$;

- que la imagen $P(I)$ sea un punto;

- que la trayectoria tenga una esquina o una cúspide;

- que no exista otra parametrización de la misma imagen con velocidad no nula.

La distinción puede resumirse así:

$$\boxed{ \text{propiedad de la parametrización} \ne \text{propiedad automática de la imagen}. }$$

[]{#balance-del-caso-de-reposo}

### 5.6.11. Balance del caso de reposo {#fispm-c05-balance-del-caso-de-reposo}

§6 distingue ahora dos regímenes:

$$\boxed{ \begin{array}{ll} v(t_0)\ne0 &\Longrightarrow \text{instante regular y recta tangente definida por la definición 5.11},\\[4pt] v(t_0)=0 &\Longrightarrow \text{instante de reposo; definición 5.11 no se aplica directamente}. \end{array} }$$

El segundo caso no debe interpretarse como una afirmación sobre la complejidad geométrica de la trayectoria. El ejemplo $A+t^3u$ muestra que una parametrización puede detenerse instantáneamente sobre una imagen tan simple como una recta. Los ejercicios 5.12--5.13 usarán estas dos ideas: primero calcular una recta tangente en el caso regular; después comparar dos parametrizaciones de una misma recta, una regular y otra con velocidad nula en un instante. La aceleración continúa fuera de §6.

### 5.6.11. Recta tangente desde la velocidad {#fispm-c05-e012-recta-tangente-desde-la-velocidad .unnumbered}

**Ejercicio 5.12 · Geometría y cálculo** Sea $F=(O,B)$ un marco fijo con $B=(e_1,e_2,e_3)$ y sea

$$r_O(t)=t^2e_1+te_2+t^3e_3, \qquad t\in\mathbb R.$$

Considera el instante $t_0=1$.

1.  Calcula $P(1)$ y $v(1)$.

2.  Verifica que $t_0=1$ es regular.

3.  Escribe la recta tangente $\mathcal T_1$ en forma afín.

4.  Sustituye el vector director $v(1)$ por $-2v(1)$ y demuestra directamente que se obtiene la misma recta.

**Solución desarrollada** Como

$$r_O(1)=e_1+e_2+e_3,$$

tenemos $P(1)=O+e_1+e_2+e_3.$ Por proposición 5.11,

$$[v(t)]_B = \frac{d}{dt} \begin{pmatrix} t^2\\ t\\ t^3 \end{pmatrix} = \begin{pmatrix} 2t\\ 1\\ 3t^2 \end{pmatrix}.$$

Por tanto,

$$\boxed{ v(1)=2e_1+e_2+3e_3. }$$

Como $v(1)\ne0$, definición 5.10 implica que $t_0=1$ es regular. Por definición 5.11,

$$\boxed{ \mathcal T_1 = \left\{ O+e_1+e_2+e_3 + \lambda(2e_1+e_2+3e_3) : \lambda\in\mathbb R \right\}. }$$

Si usamos en cambio el vector director

$$-2v(1) = -4e_1-2e_2-6e_3,$$

obtenemos

$$\widetilde{\mathcal T}_1 = \left\{ P(1)+\mu[-2v(1)] : \mu\in\mathbb R \right\}.$$

Si ponemos

$$\lambda=-2\mu,$$

entonces $\lambda$ recorre todo $\mathbb R$ cuando $\mu$ lo recorre, y por ello

$$\boxed{ \widetilde{\mathcal T}_1=\mathcal T_1. }$$

La recta tangente depende de la dirección generada por el vector velocidad, no de una normalización particular de su vector director.

### 5.6.11. Velocidad nula con la misma imagen geométrica {#fispm-c05-e013-velocidad-nula-con-la-misma-imagen-geomuxe9trica .unnumbered}

**Ejercicio 5.13 · Contraejemplo y distinción parametrización--imagen** Sean $A\in\mathcal E$ y $u\in V$ con $u\ne0$. Considera los movimientos

$$P(t)=A+t^3u, \qquad Q(s)=A+su, \qquad t,s\in\mathbb R.$$

1.  Demuestra que $P(\mathbb R)=Q(\mathbb R)$.

2.  Calcula las velocidades $v_P(t)$ y $v_Q(s)$.

3.  Clasifica el parámetro $0$ para cada movimiento usando definición 5.10 y definición 5.12.

4.  Explica por qué $v_P(0)=0$ no permite concluir que la imagen de $P$ tenga una esquina, una cúspide o se reduzca a un punto.

5.  ¿Qué recta tangente proporciona definición 5.11 para $Q$ en $s=0$? ¿Por qué definición 5.11 no puede usarse directamente para $P$ en $t=0$?

**Solución desarrollada** La función real

$$t\longmapsto t^3$$

es sobreyectiva sobre $\mathbb R$. Por tanto,

$$P(\mathbb R) = \{A+t^3u:t\in\mathbb R\} = \{A+\lambda u:\lambda\in\mathbb R\}.$$

Para $Q$,

$$Q(\mathbb R) = \{A+su:s\in\mathbb R\} = \{A+\lambda u:\lambda\in\mathbb R\}.$$

Luego

$$\boxed{ P(\mathbb R)=Q(\mathbb R). }$$

Tomando $A$ como origen auxiliar y usando proposición 5.9, $v_P(t) = \frac{d}{dt}(t^3u) = 3t^2u,$

mientras

$$v_Q(s) = \frac{d}{ds}(su) = u.$$

Así, $v_P(0)=0, \qquad v_Q(0)=u\ne0.$ Por definición 5.12, $t=0$ es un instante de reposo para $P$. Por definición 5.10, $s=0$ es un instante regular para $Q$. Sin embargo, ambos movimientos poseen exactamente la misma imagen: una recta afín completa. Por eso la anulación de $v_P(0)$ no autoriza a atribuir por sí sola una singularidad geométrica a la imagen. Lo que falla en ese instante es la posibilidad de usar la velocidad de **esa parametrización** como vector director no nulo.

Para $Q$, definición 5.11 da

$$\boxed{ \mathcal T^{\,Q}_{0} = \{A+\lambda u:\lambda\in\mathbb R\}, }$$

que coincide con toda la trayectoria geométrica. Para $P$, definición 5.11 no se aplica directamente en $t=0$ porque requeriría un vector director no nulo y

$$v_P(0)=0.$$

El contraste muestra exactamente la separación buscada:

$$\boxed{ \text{misma imagen} \;\not\Rightarrow\; \text{misma regularidad de la parametrización}. }$$

[]{#cierre-conceptual-dirección-tangente-y-fallo-de-la-parametrización}

### 5.6.12. Cierre conceptual: dirección tangente y fallo de la parametrización {#fispm-c05-cierre-conceptual-direcciuxf3n-tangente-y-fallo-de-la-parametrizaciuxf3n}

La sección distingue dos situaciones sin introducir todavía ninguna estructura dinámica. Si

$$v(t_0)\ne0,$$

el instante es regular y la velocidad determina la recta tangente afín

$$\mathcal T_{t_0} = \{P(t_0)+\lambda v(t_0):\lambda\in\mathbb R\}.$$

Las secantes poseen vectores directores escalados que convergen a $v(t_0)$, y cualquier múltiplo no nulo de ese vector genera la misma recta. Si, en cambio, $v(t_0)=0,$

el instante es de reposo y definición 5.11 no suministra una recta tangente mediante la velocidad. Esta afirmación pertenece a la parametrización y no determina por sí sola la geometría de la imagen. Ejercicio 5.12 hizo explícito el caso regular y la irrelevancia del reescalado del vector director. Ejercicio 5.13 mostró el caso complementario: dos movimientos pueden recorrer exactamente la misma recta y, sin embargo, uno de ellos tener velocidad nula en un instante mientras el otro es regular allí. La síntesis de §6 es, por tanto,

$$\boxed{ \text{imagen geométrica} + \text{parametrización} \longrightarrow \text{información tangencial del movimiento}. }$$

La aceleración requiere derivar la curva de velocidades y pertenece íntegramente a §7; no se ha utilizado en esta sección.

[]{#aceleración-como-segunda-derivada}

[]{#fispm-t1-c05-s07}

[]{#fpm-i-05-s07}

## 5.7. Aceleración como segunda derivada {#fispm-c05-aceleraciuxf3n-como-segunda-derivada}

[]{#activación-una-velocidad-también-puede-variar}

### 5.7.1. Activación: una velocidad también puede variar {#fispm-c05-activaciuxf3n-una-velocidad-tambiuxe9n-puede-variar}

Hasta ahora la derivada se aplicó a una curva de posiciones para construir la velocidad

$$v(t)\in V.$$

Pero la velocidad misma puede cambiar con el tiempo. Dos movimientos pueden poseer en un instante velocidades de igual magnitud y, sin embargo, comportarse de manera diferente inmediatamente después porque sus vectores velocidad evolucionan de modo distinto. La pregunta de §7 es, por tanto,

[]{#fig:I-05-R01}

<figure id="fig-fpm-v04-i-05-r01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-05-R01.svg" class="lightbox" data-gallery="fpm-v04-c05"><img src="/assets/books/fispm/v04/I-05-R01.svg" alt="Velocidad tangente y aceleración. Diagrama del capítulo 5; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="343" height="283" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 5.3.** Para $r(u)=(u,u^2/5)$, la velocidad es $(1,2u/5)$ y la aceleración es $(0,2/5)$. La aceleración no tiene por qué ser paralela a la trayectoria ni a la velocidad. Véase §[5.7](#fispm-c05-aceleraciuxf3n-como-segunda-derivada).

</figcaption>

</figure>

$$\boxed{ \text{¿cómo cambia instantáneamente el vector velocidad?} }$$

La respuesta utiliza exactamente la misma noción de derivada vectorial construida en la definición 5.8: ahora la curva que derivamos no toma valores en el espacio afín $\mathcal E$, sino directamente en el espacio vectorial $V$.

Activación Si $v(t)$ ya es un vector de $V$, ¿qué tipo de objeto debe ser su cociente incremental $$\frac{v(t+h)-v(t)}{h}?$$ ¿Qué ventaja de tipado aparece aquí respecto del paso desde posiciones a velocidades?

[]{#del-cambio-de-posición-al-cambio-de-velocidad}

### 5.7.2. Del cambio de posición al cambio de velocidad {#fispm-c05-del-cambio-de-posiciuxf3n-al-cambio-de-velocidad}

Para $h\ne0$, la diferencia

$$v(t+h)-v(t)$$

está definida directamente en $V$. Por tanto, $\frac{v(t+h)-v(t)}{h}\in V.$

Si estos cocientes convergen cuando $h\to0$, el límite vuelve a ser un vector de $V$. No necesitamos construir primero un desplazamiento afín porque estamos comparando dos vectores, no dos puntos. Esta diferencia de tipos conviene hacerla visible:

$$\boxed{ \begin{array}{rcl} P(t+h),P(t)\in\mathcal E &\Longrightarrow& \overrightarrow{P(t)P(t+h)}\in V,\\[4pt] v(t+h),v(t)\in V &\Longrightarrow& v(t+h)-v(t)\in V. \end{array} }$$

La aceleración nacerá de la segunda línea.

[]{#fispm-c05-definir-aceleraciuxf3n label="fispm-c05-definir-aceleraciuxf3n"}

**Definición 5.13 --- Aceleración** Sea $P:I\to\mathcal E$ un movimiento cuya velocidad

$$v:I\longrightarrow V$$

sea derivable en un punto interior $t\in I$. Definimos la **aceleración** en $t$ por

$$\boxed{ a(t) := v'(t) = \lim_{h\to0} \frac{v(t+h)-v(t)}{h} \in V. }$$

La existencia de $v(t)$ no garantiza por sí sola la existencia de $a(t)$. Definición 5.13 exige una condición adicional: la curva de velocidades debe ser derivable en el instante considerado. La aceleración es, por definición, un **vector**. No es todavía una causa, una fuerza ni una ecuación de movimiento.

[]{#control-dimensional}

### 5.7.3. Control dimensional {#fispm-c05-control-dimensional}

Si $t$ representa tiempo físico y

$$[v]=\frac{L}{T},$$

entonces el cociente incremental de la definición 5.13 posee dimensión

$$\left[ \frac{v(t+h)-v(t)}{h} \right] = \frac{L/T}{T} = \frac{L}{T^2}.$$

Por tanto,

$$\boxed{ [a]=\frac{L}{T^2}. }$$

Esta comprobación coincide con la previsión dimensional de principio metodológico 5.6. El análisis dimensional verifica consistencia, pero no sustituye la definición por límite.

[]{#principio-metodológico-cinemática-no-es-dinámica}

### 5.7.4. Principio metodológico: cinemática no es dinámica {#fispm-c05-principio-metodoluxf3gico-cinemuxe1tica-no-es-dinuxe1mica}

**Principio metodológico 5.8 --- Aceleración cinemática no implica todavía fuerza** La afirmación

$$a(t)\ne0$$

describe cómo cambia la velocidad del movimiento. En el capítulo 5 no autoriza a concluir qué causa ese cambio. No introducir todavía expresiones como $F=ma$

ni inferir fuerzas, masas o mecanismos dinámicos a partir de la aceleración. Esas relaciones pertenecen al capítulo 9. Error de nivel estructural «Como el movimiento tiene aceleración no nula, debe existir una fuerza neta no nula.» Esa conclusión pertenece a una teoría dinámica adicional. Definición 5.13 sólo define una propiedad cinemática de una curva parametrizada.[^5]

La separación es deliberada:

$$\boxed{ \text{cinemática: cómo cambia el movimiento} \qquad\ne\qquad \text{dinámica: por qué cambia}. }$$

[]{#qué-falta-demostrar}

### 5.7.5. Qué falta demostrar {#fispm-c05-quuxe9-falta-demostrar}

Definición 5.13 define la aceleración derivando directamente la curva de velocidades. Antes de usarla sistemáticamente debemos demostrar dos conexiones con las representaciones ya construidas:

1.  para cualquier origen fijo $O$, $$a(t)=r_O''(t);$$

2.  en un marco fijo $F=(O,B)$, $$[a(t)]_B=\frac{d^2}{dt^2}x_F(t),$$ y un cambio de origen fijo no altera la aceleración. Estos serán proposición 5.13 y proposición 5.14. Todavía no los usamos como resultados establecidos.

[]{#balance-conceptual}

### 5.7.6. Balance conceptual {#fispm-c05-balance-conceptual}

La nueva cadena conceptual es

$$\boxed{ P(t) \longrightarrow v(t)\in V \longrightarrow \frac{v(t+h)-v(t)}{h} \longrightarrow a(t)\in V. }$$

La aceleración exige una derivada adicional respecto de la velocidad y tiene dimensión $L/T^2$. Su significado en este capítulo es exclusivamente cinemático. Las proposiciones siguientes relacionan $a(t)$ con la segunda derivada del vector de posición y con las coordenadas en un marco fijo. Fuerza, masa, ecuaciones de Newton y marcos móviles permanecen fuera de §7.

[]{#proposición-la-aceleración-es-la-segunda-derivada-de-la-posición-relativa}

### 5.7.7. Proposición: la aceleración es la segunda derivada de la posición relativa {#fispm-c05-proposiciuxf3n-la-aceleraciuxf3n-es-la-segunda-derivada-de-la-posiciuxf3n-relativa}

En §5 demostramos que, para cualquier origen fijo $O$, $v(t)=r_O'(t).$ Si la velocidad es derivable, podemos derivar una vez más esta identidad. El resultado no introduce una nueva noción de aceleración: conecta definición 5.13 con la representación vectorial de la posición.

**Proposición 5.13 --- Aceleración como segunda derivada de la posición relativa** Sea $P:I\to\mathcal E$ un movimiento y sea $O\in\mathcal E$ un origen fijo. Supongamos que $r_O:I\to V$ es dos veces derivable en un punto interior $t\in I$. Entonces la aceleración existe en $t$ y

$$\boxed{ a(t)=r_O''(t). }$$

**Demostración.** Por proposición 5.9,

$$v(t)=r_O'(t).$$

Como $r_O$ es dos veces derivable en $t$, la curva $r_O'$ es derivable allí. Por tanto, la curva de velocidades $v$ es derivable en $t$ y definición 5.13 da $a(t)=v'(t).$ Sustituyendo $v=r_O'$, $a(t) = \frac{d}{dt}r_O'(t) = r_O''(t).$

$\square$ La igualdad

$$a(t)=r_O''(t)$$

es válida para **cualquier origen fijo**. La palabra «fijo» es esencial: si el origen dependiera del tiempo, la relación entre las derivadas contendría términos adicionales que pertenecen al estudio posterior de marcos móviles.

[]{#independencia-del-origen-fijo}

### 5.7.8. Independencia del origen fijo {#fispm-c05-independencia-del-origen-fijo}

Sean dos orígenes fijos

$$O'=O+c, \qquad c\in V.$$

Por proposición 5.2, $r_{O'}(t)=r_O(t)-c.$

Como $c$ no depende del tiempo, $r_{O'}'(t)=r_O'(t)$

y, si existen las segundas derivadas,

$$r_{O'}''(t)=r_O''(t).$$

Junto con la proposición 5.13,

$$\boxed{ r_{O'}''(t) = r_O''(t) = a(t). }$$

Así como una traslación constante del origen desaparece al calcular la velocidad, también desaparece al calcular la aceleración.

[]{#proposición-componentes-de-la-aceleración-en-un-marco-fijo}

### 5.7.9. Proposición: componentes de la aceleración en un marco fijo {#fispm-c05-proposiciuxf3n-componentes-de-la-aceleraciuxf3n-en-un-marco-fijo}

Fijemos un marco

$$F=(O,B), \qquad B=(e_1,e_2,e_3),$$

cuyos datos no dependen del tiempo. En §5 obtuvimos

$$[v(t)]_B = \frac{d}{dt}x_F(t).$$

Como ahora $v:I\to V$ es una curva vectorial derivable, proposición 5.8 permite derivarla componente a componente.

**Proposición 5.14 --- Componentes e independencia del origen de la aceleración** Sea $P:I\to\mathcal E$ un movimiento dos veces derivable en $t$ y sea $F=(O,B)$ un marco fijo. Entonces

$$\boxed{ [a(t)]_B = \frac{d^2}{dt^2}x_F(t). }$$

Además, si $O'=O+c$ con $c\in V$ constante y se conserva la misma base fija $B$, el cambio de origen no altera la aceleración:

$$\boxed{ r_{O'}''(t) = r_O''(t) = a(t). }$$

**Demostración.** Por definición 5.13,

$$a(t)=v'(t).$$

Aplicamos proposición 5.8 a la curva vectorial $v:I\to V$ en la base fija $B$: $[a(t)]_B = [v'(t)]_B = \frac{d}{dt}[v(t)]_B.$ Por proposición 5.11, $[v(t)]_B = \frac{d}{dt}x_F(t).$ Por tanto,

$$[a(t)]_B = \frac{d}{dt} \left( \frac{d}{dt}x_F(t) \right) = \frac{d^2}{dt^2}x_F(t).$$

La independencia respecto del origen fijo ya se obtiene de

$$r_{O'}(t)=r_O(t)-c$$

con $c$ constante. Al derivar dos veces, $r_{O'}''(t)=r_O''(t),$

y proposición 5.13 identifica ambas segundas derivadas con $a(t)$. $\square$ proposición 5.14 permite calcular la aceleración mediante coordenadas sin convertir la columna coordenada en el objeto geométrico. La aceleración sigue siendo un vector de $V$; la columna

$$\frac{d^2}{dt^2}x_F(t)$$

es sólo su representación en la base fija $B$.

[]{#balance-de-las-representaciones}

### 5.7.10. Balance de las representaciones {#fispm-c05-balance-de-las-representaciones}

La aceleración posee ahora tres descripciones coherentes:

$$\boxed{ a(t) = v'(t) = r_O''(t), }$$

y, en cualquier marco fijo $F=(O,B)$,

$$\boxed{ [a(t)]_B = \frac{d^2}{dt^2}x_F(t). }$$

La primera fórmula es la definición cinemática de la definición 5.13; la segunda conecta la aceleración con la posición relativa; la tercera proporciona el cálculo por componentes. Cambiar un origen **fijo** no modifica ninguna de ellas. Todavía no hemos estudiado cómo cambian las componentes al cambiar de base o de marco fijo: esa covariancia pertenece a §8. Tampoco hemos introducido fuerza, masa ni leyes de Newton. Quedan ejercicios 5.14--5.15 para ejercitar el cálculo de $v$ y $a$, auditar dimensiones y distinguir cuidadosamente velocidad nula, velocidad constante y aceleración nula antes del cierre local de §7.

### 5.7.10. Aceleración sin dinámica {#fispm-c05-e014-aceleraciuxf3n-sin-dinuxe1mica .unnumbered}

**Ejercicio 5.14 · Cálculo y análisis dimensional** Sea $F=(O,B)$ un marco fijo con $B=(e_1,e_2,e_3)$. Un movimiento tiene coordenadas

$$x_F(t) = \begin{pmatrix} \alpha t^2\\ \beta t\\ \ell \end{pmatrix},$$

donde

$$[\alpha]=\frac{L}{T^2}, \qquad [\beta]=\frac{L}{T}, \qquad [\ell]=L.$$

1.  Calcula $[v(t)]_B$ y $[a(t)]_B$.

2.  Verifica las dimensiones de cada componente de la velocidad y de la aceleración.

3.  Decide si la aceleración depende del instante $t$.

4.  Explica qué puede afirmarse cinemáticamente cuando $\alpha\ne0$ y qué **no** puede concluirse todavía sobre fuerzas o causas físicas.

**Solución desarrollada** Por proposición 5.11,

$$[v(t)]_B = \frac{d}{dt}x_F(t) = \begin{pmatrix} 2\alpha t\\ \beta\\ 0 \end{pmatrix}.$$

Por proposición 5.14,

$$[a(t)]_B = \frac{d^2}{dt^2}x_F(t) = \begin{pmatrix} 2\alpha\\ 0\\ 0 \end{pmatrix}.$$

Para la primera componente de la velocidad, $[2\alpha t] = \frac{L}{T^2}\,T = \frac{L}{T}.$ La segunda componente ya tiene dimensión $L/T$ y la tercera es nula. Por tanto, $[v]=\frac{L}{T}.$ Para la aceleración, $[2\alpha] = \frac{L}{T^2},$

de modo que

$$[a]=\frac{L}{T^2}.$$

La columna de la aceleración no depende de $t$:

$$\boxed{ [a(t)]_B = \begin{pmatrix} 2\alpha\\0\\0 \end{pmatrix} \quad\text{para todo }t. }$$

Si $\alpha\ne0$, podemos afirmar cinemáticamente que la velocidad cambia y que la aceleración es un vector constante no nulo. No podemos concluir en el capítulo 5 cuál es la causa de ese cambio, ni introducir una fuerza o una masa para explicarlo. Eso requeriría la teoría dinámica posterior.

### 5.7.10. Reposo, aceleración nula y velocidad constante {#fispm-c05-e015-reposo-aceleraciuxf3n-nula-y-velocidad-constante .unnumbered}

**Ejercicio 5.15 · Concepto y contraejemplo** Fija un origen $O$ y considera tres movimientos cuyas curvas de posición relativa son

$$r_A(t)=\frac12 t^2 a_0,$$

$$r_B(t)=t v_0+\frac16 t^3 b_0,$$

$$r_C(t)=r_0+t v_0,$$

donde $a_0,v_0,b_0,r_0\in V$, con

$$a_0\ne0, \qquad v_0\ne0, \qquad b_0\ne0,$$

y las dimensiones son las apropiadas para que cada término de $r_A,r_B,r_C$ tenga dimensión de longitud.

1.  Calcula $v_A,a_A$, $v_B,a_B$ y $v_C,a_C$.

2.  Clasifica el instante $t=0$ en cada movimiento: ¿hay reposo instantáneo?, ¿aceleración nula en ese instante?, ¿aceleración idénticamente nula?

3.  Decide en qué caso la velocidad es constante en todo el intervalo.

4.  Explica por qué $a(0)=0$ no implica $a\equiv0$, y por qué $v(0)=0$ no implica $a(0)=0$.

5.  Formula las conclusiones sin introducir fuerzas ni causas dinámicas.

**Solución desarrollada** Para $A$,

$$v_A(t)=t a_0, \qquad a_A(t)=a_0.$$

En particular, $v_A(0)=0, \qquad a_A(0)=a_0\ne0.$ Por definición 5.12, $t=0$ es un instante de reposo, pero la aceleración no se anula allí. Para $B$, $v_B(t) = v_0+\frac12 t^2 b_0,$

y

$$a_B(t)=t b_0.$$

Luego

$$v_B(0)=v_0\ne0, \qquad a_B(0)=0,$$

pero, para $t\ne0$, $a_B(t)=t b_0\ne0.$ Por tanto, $a_B(0)=0$ no implica $a_B\equiv0$. Para $C$, $v_C(t)=v_0, \qquad a_C(t)=0$

para todo $t$. Aquí sí tenemos

$$\boxed{a_C\equiv0}$$

y la velocidad es constante en todo el intervalo.

El cuadro conceptual es:

$$\boxed{ \begin{array}{c|c|c|c} \text{movimiento} &v(0) &a(0) &a\equiv0\\ \hline A&0&a_0\ne0&\text{no}\\ B&v_0\ne0&0&\text{no}\\ C&v_0\ne0&0&\text{sí} \end{array} }$$

Así, las tres afirmaciones

$$v(t_0)=0, \qquad a(t_0)=0, \qquad a\equiv0$$

son lógicamente distintas. En el tercer ejemplo calculamos directamente $v_C(t)=v_0$ para todo $t$, de modo que la velocidad es constante y $a_C\equiv0$. Ninguna de estas conclusiones necesita todavía una ley dinámica.

[]{#cierre-conceptual-segunda-derivada-sin-causalidad-dinámica}

### 5.7.11. Cierre conceptual: segunda derivada sin causalidad dinámica {#fispm-c05-cierre-conceptual-segunda-derivada-sin-causalidad-dinuxe1mica}

§7 ha construido la aceleración exclusivamente a partir de la evolución temporal de la velocidad:

$$\boxed{ P(t) \longrightarrow v(t) \longrightarrow a(t)=v'(t). }$$

Para cualquier origen fijo $O$,

$$\boxed{ a(t)=r_O''(t), }$$

y, en un marco fijo $F=(O,B)$,

$$\boxed{ [a(t)]_B = \frac{d^2}{dt^2}x_F(t). }$$

La aceleración tiene dimensión $L/T^2$ y un cambio de origen fijo no la altera. Ejercicio 5.14 hizo explícito el cálculo y la auditoría dimensional; ejercicio 5.15 separó tres condiciones que no deben confundirse: reposo instantáneo, aceleración nula en un instante y aceleración idénticamente nula. El resultado pedagógico central es

$$\boxed{ \text{describir }a(t) \ne \text{explicar la causa de }a(t). }$$

Fuerzas, masas y leyes de Newton permanecen fuera del capítulo 5. La siguiente sección estudiará únicamente cómo se representan $v$ y $a$ cuando cambiamos entre **marcos espaciales fijos**; los marcos móviles continuarán reservados para capítulos posteriores.

[]{#marcos-fijos-y-covariancia-de-las-derivadas}

[]{#fispm-t1-c05-s08}

[]{#fpm-i-05-s08}

## 5.8. Marcos fijos y covariancia de las derivadas {#fispm-c05-marcos-fijos-y-covariancia-de-las-derivadas}

[]{#activación-el-mismo-vector-columnas-distintas}

### 5.8.1. Activación: el mismo vector, columnas distintas {#fispm-c05-activaciuxf3n-el-mismo-vector-columnas-distintas}

En §§5 y 7 construimos dos objetos geométricos: $v(t)\in V, \qquad a(t)\in V.$ En un marco fijo

$$F=(O,B),$$

los representamos mediante columnas

$$[v(t)]_B, \qquad [a(t)]_B.$$

Si otro observador matemático usa otro marco fijo

$$F'=(O',B'),$$

las columnas pueden ser distintas aunque los vectores geométricos sean exactamente los mismos. La pregunta central de esta sección es

$$\boxed{ \text{¿qué cambia al cambiar la descripción y qué objeto permanece?} }$$

Activación Si dos columnas numéricas diferentes representan el mismo vector en bases distintas, ¿ha cambiado el movimiento o sólo su descripción? ¿Qué hipótesis necesitamos sobre los marcos antes de derivar sus coordenadas?

[]{#fig:I-05-R05}

<figure id="fig-fpm-v04-i-05-r05" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-05-R05.svg" class="lightbox" data-gallery="fpm-v04-c05"><img src="/assets/books/fispm/v04/I-05-R05.svg" alt="Trasladar la descripción conserva la velocidad. Diagrama del capítulo 5; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="343" height="257" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 5.4.** Entre marcos de igual base y orígenes separados por una constante, las posiciones difieren en esa constante. Derivarla da cero y las velocidades representadas coinciden. El dibujo compara vectores de posición, no dos fuerzas. Véase §[5.8](#fispm-c05-marcos-fijos-y-covariancia-de-las-derivadas).

</figcaption>

</figure>

[]{#recordatorio-la-ley-afín-para-las-posiciones}

### 5.8.2. Recordatorio: la ley afín para las posiciones {#fispm-c05-recordatorio-la-ley-afuxedn-para-las-posiciones}

Sean

$$F=(O,B), \qquad F'=(O',B')$$

dos marcos geométricos. Escribamos

$$O'=O+c, \qquad c\in V,$$

y sea $S$ la matriz cuyas columnas son los vectores de la base $B'$ expresados en la base $B$. El capítulo 4 y proposición 5.4 de este capítulo proporcionan, punto a punto,

$$\boxed{ x_{F'}(t) = S^{-1} \left( x_F(t)-[c]_B \right). }$$

Esta fórmula contiene dos operaciones conceptualmente distintas:

- la traslación del origen, representada por $[c]_B$;

- el cambio de base, representado por $S^{-1}$.

Para posiciones, ambas aparecen. Para derivadas temporales, debemos controlar primero si $S$ y $c$ cambian o no con $t$.

[]{#fispm-c05-definir-marco-espacial-fijo-durante-un-movimiento label="fispm-c05-definir-marco-espacial-fijo-durante-un-movimiento"}

**Definición 5.14 --- Marco espacial fijo durante un movimiento** Sea $P:I\to\mathcal E$ un movimiento. Un marco espacial

$$F=(O,B)$$

se llama **fijo durante el movimiento** si el origen $O$ y todos los vectores de la base ordenada

$$B=(e_1,e_2,e_3)$$

son independientes del parámetro temporal $t\in I$.

La palabra «fijo» se refiere aquí únicamente a la ausencia de dependencia temporal de los datos geométricos del marco. No significa todavía:

- que el marco sea inercial;

- que exista una ley dinámica;

- que el marco esté físicamente en reposo en algún sentido absoluto;

- que hayamos comparado observadores móviles.

Es una hipótesis matemática sobre la descripción usada durante la derivación.

[]{#dos-marcos-fijos-implican-datos-de-cambio-constantes}

### 5.8.3. Dos marcos fijos implican datos de cambio constantes {#fispm-c05-dos-marcos-fijos-implican-datos-de-cambio-constantes}

Supongamos que

$$F=(O,B), \qquad F'=(O',B')$$

son ambos fijos en el sentido de la definición 5.14. Entonces el vector

$$c=\overrightarrow{OO'}$$

es constante respecto de $t$, y la matriz de cambio de base

$$S=S_{B\leftarrow B'}$$

también es constante respecto de $t$. Por tanto, en la ley

$$x_{F'}(t) = S^{-1} \left( x_F(t)-[c]_B \right),$$

los únicos términos que pueden variar temporalmente son las coordenadas de la curva

$$x_F(t).$$

Esta observación será la clave de la proposición 5.15 y proposición 5.16.

[]{#qué-ocurriría-si-el-marco-dependiera-del-tiempo}

### 5.8.4. Qué ocurriría si el marco dependiera del tiempo {#fispm-c05-quuxe9-ocurriruxeda-si-el-marco-dependiera-del-tiempo}

Conviene identificar el límite del método antes de aplicar derivadas. Si permitiéramos, por ejemplo, $c=c(t)$

o

$$S=S(t),$$

la fórmula de coordenadas tomaría la forma

$$x_{F'}(t) = S(t)^{-1} \left( x_F(t)-[c(t)]_B \right).$$

Al derivar ya no sería legítimo tratar $S^{-1}$ y $[c]_B$ como constantes. Aparecerían términos adicionales provenientes de la variación temporal del origen o de la base. No calcularemos esos términos aquí. Ese problema pertenece a la cinemática en marcos móviles y, posteriormente, a los marcos no inerciales. En el capítulo 5 se trabaja únicamente con marcos fijos.

[]{#principio-metodológico-congelar-el-marco-antes-de-derivar}

### 5.8.5. Principio metodológico: congelar el marco antes de derivar {#fispm-c05-principio-metodoluxf3gico-congelar-el-marco-antes-de-derivar}

**Principio metodológico 5.9 --- Congelar el marco antes de derivar coordenadas** Antes de derivar una ley de transformación de coordenadas, declarar explícitamente si el origen y la base dependen de $t$.

En §8 sólo se permite derivar

$$x_{F'}(t) = S^{-1} \left( x_F(t)-[c]_B \right)$$

bajo la hipótesis

$$\boxed{ \frac{dS}{dt}=0, \qquad \frac{dc}{dt}=0. }$$

Estas igualdades expresan abreviadamente que $S$ y $c$ son constantes respecto del parámetro temporal; no introducen una teoría de matrices o marcos dependientes del tiempo.

La finalidad de principio metodológico 5.9 es impedir una manipulación aparentemente inocente:

$$\frac{d}{dt} \left[ S^{-1} \left( x_F-[c]_B \right) \right] = S^{-1}\dot x_F$$

sin haber comprobado antes que $S$ y $c$ son constantes.

[]{#objeto-geométrico-frente-a-representación}

### 5.8.6. Objeto geométrico frente a representación {#fispm-c05-objeto-geomuxe9trico-frente-a-representaciuxf3n}

La velocidad fue definida intrínsecamente por la definición 5.9:

$$v(t) = \lim_{h\to0} \frac{\overrightarrow{P(t)P(t+h)}}{h}.$$

La aceleración fue definida por la definición 5.13: $a(t)=v'(t).$

Estas definiciones no contienen ninguna base. En cambio,

$$[v(t)]_B, \qquad [v(t)]_{B'}, \qquad [a(t)]_B, \qquad [a(t)]_{B'}$$

son representaciones numéricas relativas a bases concretas. Por eso debemos separar dos afirmaciones:

$$\boxed{ \text{el vector geométrico permanece} }$$

y

$$\boxed{ \text{sus componentes se transforman}. }$$

[]{#principio-metodológico-invariancia-de-objeto-y-covariancia-de-representación}

### 5.8.7. Principio metodológico: invariancia de objeto y covariancia de representación {#fispm-c05-principio-metodoluxf3gico-invariancia-de-objeto-y-covariancia-de-representaciuxf3n}

**Principio metodológico 5.10 --- Distinguir invariancia de objeto y covariancia de representación** Cuando dos marcos fijos describan el mismo movimiento:

1.  identificar primero el objeto geométrico, por ejemplo $v(t)\in V$ o $a(t)\in V$;

2.  distinguirlo de sus columnas $[v(t)]_B$, $[v(t)]_{B'}$, $[a(t)]_B$, $[a(t)]_{B'}$;

3.  interpretar el cambio de columnas como una **ley de transformación de la representación**, no como una transformación física automática del vector.

En particular, $[v(t)]_B\ne[v(t)]_{B'}$

puede ocurrir aunque ambos símbolos representen el mismo vector $v(t)$. Esta distinción es la forma elemental de la covariancia que necesitamos aquí: la descripción cambia de acuerdo con una regla precisa, mientras el objeto geométrico descrito no se multiplica ni se desplaza por el mero acto de cambiar de coordenadas.

[]{#un-ejemplo-mínimo-de-representación}

### 5.8.8. Un ejemplo mínimo de representación {#fispm-c05-un-ejemplo-muxednimo-de-representaciuxf3n}

Sea un vector

$$u\in V$$

y dos bases fijas $B$ y $B'$ relacionadas por $[u]_B = S[u]_{B'}.$

Equivalentemente, $[u]_{B'} = S^{-1}[u]_B.$ Si $u=v(t)$ en un instante concreto, la misma regla algebraica relacionará sus componentes. Si $u=a(t)$, ocurrirá lo mismo. La novedad de las proposiciones 5.15--5.16 no será esta regla de cambio de base aislada, ya conocida desdel capítulo 4, sino demostrar que **derivar las coordenadas de una curva en dos marcos fijos produce exactamente columnas compatibles con esa misma ley**.

[]{#balance-conceptual-1}

### 5.8.9. Balance conceptual {#fispm-c05-balance-conceptual-1}

La sección queda preparada sobre tres separaciones:

$$\boxed{ \text{marco fijo} \ne \text{marco móvil}, }$$

$$\boxed{ \text{vector geométrico} \ne \text{columna de componentes}, }$$

y

$$\boxed{ \text{cambio de descripción} \ne \text{cambio físico del movimiento}. }$$

Definición 5.14 garantiza que los datos del marco no dependen de $t$. principio metodológico 5.9 obliga a comprobar esa hipótesis antes de derivar coordenadas. principio metodológico 5.10 impide confundir la transformación de componentes con una transformación del objeto geométrico. Las proposiciones siguientes establecen proposiciones 5.15--5.17: las leyes de transformación de las componentes de $v$ y $a$ entre marcos fijos y la invariancia de $\|v(t)\|$ cuando los cambios de base son ortonormales. El nombre formal **rapidez** sigue reservado para §11.

[]{#proposición-transformación-de-la-velocidad-entre-marcos-fijos}

### 5.8.10. Proposición: transformación de la velocidad entre marcos fijos {#fispm-c05-proposiciuxf3n-transformaciuxf3n-de-la-velocidad-entre-marcos-fijos}

Sean

$$F=(O,B), \qquad F'=(O',B')$$

dos marcos fijos. Escribamos

$$O'=O+c$$

y sea $S$ la matriz cuyas columnas son los vectores de $B'$ expresados en $B$. Por proposición 5.4, $x_{F'}(t) = S^{-1} \left( x_F(t)-[c]_B \right).$ Como $S$ y $c$ son constantes respecto de $t$, podemos derivar esta identidad sin términos adicionales.

**Proposición 5.15 --- Transformación de la velocidad entre marcos fijos** Sean $F=(O,B)$ y $F'=(O',B')$ dos marcos fijos relacionados como arriba. Si el movimiento es derivable en $t$, entonces

$$\boxed{ [v(t)]_{B'} = S^{-1}[v(t)]_B. }$$

La traslación entre los orígenes no aparece en la ley de transformación de la velocidad.

**Demostración.** Derivamos la ley afín de las coordenadas:

$$\frac{d}{dt}x_{F'}(t) = \frac{d}{dt} \left[ S^{-1} \left( x_F(t)-[c]_B \right) \right].$$

Por definición 5.14, $S^{-1}$ y $[c]_B$ son constantes. Luego

$$\frac{d}{dt}x_{F'}(t) = S^{-1} \frac{d}{dt}x_F(t).$$

Aplicando proposición 5.11 en ambos marcos, $[v(t)]_{B'} = S^{-1}[v(t)]_B.$

$\square$ proposición 5.15 expresa covariancia de componentes: las dos columnas pueden ser distintas, pero ambas representan el mismo vector geométrico $v(t)\in V$.

[]{#proposición-transformación-de-la-aceleración-entre-marcos-fijos}

### 5.8.11. Proposición: transformación de la aceleración entre marcos fijos {#fispm-c05-proposiciuxf3n-transformaciuxf3n-de-la-aceleraciuxf3n-entre-marcos-fijos}

La misma hipótesis permite derivar una segunda vez. Como la matriz de cambio sigue siendo constante, la ley lineal de transformación se conserva para la aceleración.

**Proposición 5.16 --- Transformación de la aceleración entre marcos fijos** Bajo las hipótesis de la proposición 5.15, si el movimiento es dos veces derivable en $t$, entonces

$$\boxed{ [a(t)]_{B'} = S^{-1}[a(t)]_B. }$$

**Demostración.** proposición 5.15 vale como identidad de curvas de componentes donde las derivadas necesarias existen:

$$[v(t)]_{B'} = S^{-1}[v(t)]_B.$$

Derivamos respecto de $t$. Como $S^{-1}$ es constante,

$$\frac{d}{dt}[v(t)]_{B'} = S^{-1} \frac{d}{dt}[v(t)]_B.$$

Por proposición 5.8 aplicado a la curva vectorial $v:I\to V$, $\frac{d}{dt}[v(t)]_{B'} = [a(t)]_{B'},$

y

$$\frac{d}{dt}[v(t)]_B = [a(t)]_B.$$

Por tanto, $[a(t)]_{B'} = S^{-1}[a(t)]_B.$

$\square$ La aceleración tampoco adquiere un término de traslación cuando ambos orígenes son fijos. Los términos adicionales aparecen sólo si se permite que el marco varíe con el tiempo, situación excluida por la definición 5.14.

[]{#marcos-ortonormales-y-norma-de-la-velocidad}

### 5.8.12. Marcos ortonormales y norma de la velocidad {#fispm-c05-marcos-ortonormales-y-norma-de-la-velocidad}

Supongamos ahora que las bases $B$ y $B'$ son ortonormales respecto del mismo producto escalar euclídeo de $V$. Entonces la matriz de cambio $S$ es ortogonal: $S^{\mathsf T}S=I, \qquad S^{-1}=S^{\mathsf T}.$ En una base ortonormal, la norma geométrica de un vector coincide con la norma euclídea de su columna: $\|v\|^2 = [v]_B^{\mathsf T}[v]_B.$

Lo mismo vale en $B'$.

**Proposición 5.17 --- Invariancia de la norma de la velocidad entre marcos ortonormales fijos** Sean $F=(O,B)$ y $F'=(O',B')$ dos marcos fijos cuyas bases $B$ y $B'$ son ortonormales respecto del mismo producto escalar. Entonces, para todo instante donde exista la velocidad,

$$\boxed{ \|v(t)\| = \|[v(t)]_B\|_2 = \|[v(t)]_{B'}\|_2. }$$

En particular, cambiar entre esos marcos no altera la norma geométrica de la velocidad.

**Demostración.** Por proposición 5.15,

$$[v(t)]_{B'} = S^{-1}[v(t)]_B.$$

Como $S$ es ortogonal, $(S^{-1})^{\mathsf T}S^{-1} =I.$ Por tanto,

$$\begin{aligned} \|[v(t)]_{B'}\|_2^2 &= [v(t)]_{B'}^{\mathsf T}[v(t)]_{B'}\\ &= [v(t)]_B^{\mathsf T} (S^{-1})^{\mathsf T}S^{-1} [v(t)]_B\\ &= [v(t)]_B^{\mathsf T}[v(t)]_B\\ &= \|[v(t)]_B\|_2^2. \end{aligned}$$

Ambas cantidades son no negativas, de modo que

$$\|[v(t)]_{B'}\|_2 = \|[v(t)]_B\|_2.$$

Como $B$ y $B'$ son ortonormales, cada una de estas normas coordenadas coincide con la norma geométrica $\|v(t)\|$. $\square$ proposición 5.17 no afirma que cualquier norma de cualquier columna sea una magnitud geométrica. La identificación con la norma euclídea ordinaria de las componentes depende aquí de la **ortonormalidad** de la base. En una base no ortonormal debe intervenir la matriz de Gram correspondiente. El nombre formal de $\|v(t)\|$ como **rapidez** continúa reservado para §11.

[]{#balance-de-las-leyes-de-transformación}

### 5.8.13. Balance de las leyes de transformación {#fispm-c05-balance-de-las-leyes-de-transformaciuxf3n}

Para marcos fijos hemos demostrado la cadena

$$\boxed{ x_{F'}(t) = S^{-1}\bigl(x_F(t)-[c]_B\bigr), }$$

$$\boxed{ [v(t)]_{B'} = S^{-1}[v(t)]_B, }$$

y

$$\boxed{ [a(t)]_{B'} = S^{-1}[a(t)]_B. }$$

La traslación del origen aparece en las coordenadas de posición y desaparece al derivar porque es constante. El cambio de base permanece como una transformación lineal de las componentes. Si además las bases son ortonormales,

$$\boxed{ \|[v(t)]_{B'}\|_2 = \|[v(t)]_B\|_2 = \|v(t)\|. }$$

Así queda visible la distinción de principio metodológico 5.10: el objeto geométrico $v(t)$ o $a(t)$ es el mismo; lo que cambia covariantemente es su columna de componentes. Ejercicios 5.16--5.17 aplican estas leyes y contrastan un cambio ortonormal con uno no ortonormal. Los marcos móviles y la reparametrización de §9 permanecen fuera de §8.

### 5.8.13. Transformar posición, velocidad y aceleración en dos marcos fijos {#fispm-c05-e016-transformar-posiciuxf3n-velocidad-y-aceleraciuxf3n-en-dos-marcos-fijos .unnumbered}

**Ejercicio 5.16 · Cálculo y covariancia** Sea $F=(O,B)$ un marco fijo con base ortonormal $B=(e_1,e_2,e_3)$ y sea un movimiento cuyas coordenadas son

$$x_F(t) = \begin{pmatrix} t^2\\ t^3\\ 2t \end{pmatrix}.$$

Considera otro marco fijo $F'=(O',B')$ definido por

$$[c]_B = \begin{pmatrix} 1\\ -2\\ 3 \end{pmatrix}, \qquad O'=O+c,$$

y por la matriz de cambio de base

$$S = \begin{pmatrix} 0&-1&0\\ 1&0&0\\ 0&0&1 \end{pmatrix},$$

cuyas columnas son los vectores de $B'$ expresados en $B$.

1.  Calcula $S^{-1}$.

2.  Obtén $x_{F'}(t)$ usando la ley afín de cambio de marco.

3.  Calcula $[v(t)]_B$ y $[a(t)]_B$.

4.  Calcula $[v(t)]_{B'}$ y $[a(t)]_{B'}$ derivando $x_{F'}(t)$.

5.  Verifica directamente proposición 5.15 y proposición 5.16.

**Solución desarrollada** Como $S$ es ortogonal,

$$S^{-1}=S^{\mathsf T} = \begin{pmatrix} 0&1&0\\ -1&0&0\\ 0&0&1 \end{pmatrix}.$$

La ley afín entre los marcos fijos es $x_{F'}(t) = S^{-1} \left( x_F(t)-[c]_B \right).$

Primero,

$$x_F(t)-[c]_B = \begin{pmatrix} t^2-1\\ t^3+2\\ 2t-3 \end{pmatrix}.$$

Por tanto,

$$\boxed{ x_{F'}(t) = \begin{pmatrix} t^3+2\\ 1-t^2\\ 2t-3 \end{pmatrix}. }$$

En el marco $F$,

$$[v(t)]_B = \frac{d}{dt}x_F(t) = \begin{pmatrix} 2t\\ 3t^2\\ 2 \end{pmatrix},$$

y

$$[a(t)]_B = \frac{d^2}{dt^2}x_F(t) = \begin{pmatrix} 2\\ 6t\\ 0 \end{pmatrix}.$$

Derivando las coordenadas en $F'$,

$$\boxed{ [v(t)]_{B'} = \begin{pmatrix} 3t^2\\ -2t\\ 2 \end{pmatrix}, }$$

y

$$\boxed{ [a(t)]_{B'} = \begin{pmatrix} 6t\\ -2\\ 0 \end{pmatrix}. }$$

Ahora verificamos proposición 5.15:

$$S^{-1}[v(t)]_B = \begin{pmatrix} 0&1&0\\ -1&0&0\\ 0&0&1 \end{pmatrix} \begin{pmatrix} 2t\\ 3t^2\\ 2 \end{pmatrix} = \begin{pmatrix} 3t^2\\ -2t\\ 2 \end{pmatrix} = [v(t)]_{B'}.$$

Del mismo modo,

$$S^{-1}[a(t)]_B = \begin{pmatrix} 6t\\ -2\\ 0 \end{pmatrix} = [a(t)]_{B'},$$

que verifica proposición 5.16. La traslación $[c]_B$ afecta a $x_{F'}$, pero desaparece de las leyes de transformación de $v$ y $a$ porque es constante.

### 5.8.13. Norma geométrica y bases no ortonormales {#fispm-c05-e017-norma-geomuxe9trica-y-bases-no-ortonormales .unnumbered}

**Ejercicio 5.17 · Métrica y error plausible** Conserva el movimiento del ejercicio 5.16 y considera el instante $t=1$. En la base ortonormal $B$,

$$[v(1)]_B = \begin{pmatrix} 2\\ 3\\ 2 \end{pmatrix}.$$

1.  Usa la base ortonormal $B'$ del ejercicio 5.16 para calcular $[v(1)]_{B'}$ y compara las normas euclídeas de ambas columnas.

2.  Introduce ahora la base no ortonormal $$B''=(2e_1,e_2,e_3).$$ Determina $[v(1)]_{B''}$.

3.  Compara $\|[v(1)]_{B''}\|_2$ con la norma geométrica $\|v(1)\|$.

4.  Calcula la matriz de Gram $G''$ de $B''$ y verifica que $$\|v(1)\|^2 = [v(1)]_{B''}^{\mathsf T} G'' [v(1)]_{B''}.$$

5.  Explica por qué el error «la norma de cualquier columna de velocidad es siempre $\|v\|$» es falso.

**Solución desarrollada** En ejercicio 5.16 obtuvimos

$$[v(1)]_{B'} = \begin{pmatrix} 3\\ -2\\ 2 \end{pmatrix}.$$

Como $B$ y $B'$ son ortonormales, $\|[v(1)]_B\|_2^2 = 2^2+3^2+2^2 =17,$

y

$$\|[v(1)]_{B'}\|_2^2 = 3^2+(-2)^2+2^2 =17.$$

Así,

$$\boxed{ \|[v(1)]_B\|_2 = \|[v(1)]_{B'}\|_2 = \sqrt{17} = \|v(1)\|. }$$

Para la base

$$B''=(2e_1,e_2,e_3),$$

la matriz cuyas columnas son los vectores de $B''$ expresados en $B$ es

$$S'' = \begin{pmatrix} 2&0&0\\ 0&1&0\\ 0&0&1 \end{pmatrix}.$$

Como $[v(1)]_{B''} = (S'')^{-1}[v(1)]_B,$

resulta

$$\boxed{ [v(1)]_{B''} = \begin{pmatrix} 1\\ 3\\ 2 \end{pmatrix}. }$$

Su norma euclídea ordinaria es

$$\|[v(1)]_{B''}\|_2 = \sqrt{1^2+3^2+2^2} = \sqrt{14},$$

que **no** coincide con $\|v(1)\|=\sqrt{17}$. La matriz de Gram de $B''$ es

$$G'' = \begin{pmatrix} 4&0&0\\ 0&1&0\\ 0&0&1 \end{pmatrix}.$$

Entonces

$$\begin{aligned} [v(1)]_{B''}^{\mathsf T} G'' [v(1)]_{B''} &= \begin{pmatrix}1&3&2\end{pmatrix} \begin{pmatrix} 4&0&0\\ 0&1&0\\ 0&0&1 \end{pmatrix} \begin{pmatrix} 1\\ 3\\ 2 \end{pmatrix}\\ &=4+9+4\\ &=17. \end{aligned}$$

Por tanto,

$$\boxed{ \|v(1)\|^2 = [v(1)]_{B''}^{\mathsf T} G'' [v(1)]_{B''}. }$$

El error consiste en confundir la columna con el vector geométrico y en olvidar la métrica asociada a la base. La norma euclídea ordinaria de las componentes representa directamente $\|v\|$ sólo cuando la base es ortonormal. El nombre formal de esta norma de la velocidad continúa reservado para §11.

[]{#cierre-conceptual-cambiar-la-descripción-sin-cambiar-el-movimiento}

### 5.8.14. Cierre conceptual: cambiar la descripción sin cambiar el movimiento {#fispm-c05-cierre-conceptual-cambiar-la-descripciuxf3n-sin-cambiar-el-movimiento}

§8 ha separado de manera explícita tres niveles:

$$\boxed{ \text{posición: cambio afín de coordenadas}, }$$

$$\boxed{ \text{velocidad y aceleración: cambio lineal de componentes}, }$$

y

$$\boxed{ \text{norma geométrica: invariante bajo bases ortonormales}. }$$

Para dos marcos fijos, $x_{F'}(t) = S^{-1}\bigl(x_F(t)-[c]_B\bigr),$

mientras

$$[v(t)]_{B'}=S^{-1}[v(t)]_B, \qquad [a(t)]_{B'}=S^{-1}[a(t)]_B.$$

La traslación desaparece al derivar porque es constante. Si las bases son ortonormales, la norma euclídea de las columnas coincide con la norma geométrica del vector; si no lo son, debe incorporarse la matriz de Gram. Ejercicio 5.16 verificó la covariancia de posición, velocidad y aceleración en un ejemplo concreto. Ejercicio 5.17 mostró por qué la métrica no puede olvidarse al pasar a una base no ortonormal. La conclusión metodológica es

$$\boxed{ \text{cambiar coordenadas} \ne \text{cambiar el movimiento físico}. }$$

La sección siguiente cambiará otra cosa distinta: no el marco espacial, sino el **parámetro** con el que se recorre una curva. Esa operación pertenece a §9 y no se ha utilizado en §8.

[]{#reparametrización-y-regla-de-la-cadena}

[]{#fispm-t1-c05-s09}

[]{#fpm-i-05-s09}

## 5.9. Reparametrización y regla de la cadena {#fispm-c05-reparametrizaciuxf3n-y-regla-de-la-cadena}

[]{#activación-una-misma-imagen-puede-recorrerse-con-otro-parámetro}

### 5.9.1. Activación: una misma imagen puede recorrerse con otro parámetro {#fispm-c05-activaciuxf3n-una-misma-imagen-puede-recorrerse-con-otro-paruxe1metro}

Sea

$$P:I\longrightarrow\mathcal E$$

una curva parametrizada. La aplicación contiene dos tipos de información:

- qué puntos del espacio afín son recorridos;

- qué valor del parámetro se asigna a cada punto del recorrido.

Si introducimos otro intervalo $J$ y una función

$$\phi:J\longrightarrow I,$$

podemos formar una nueva curva

$$P\circ\phi:J\longrightarrow\mathcal E.$$

El punto espacial no se obtiene mediante una transformación del espacio: seguimos evaluando la misma curva $P$, pero ahora el valor de su parámetro se determina a partir de $u\in J$ mediante $\phi(u)$. La pregunta central de esta sección será

[]{#fig:I-05-R03}

<figure id="fig-fpm-v04-i-05-r03" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-05-R03.svg" class="lightbox" data-gallery="fpm-v04-c05"><img src="/assets/books/fispm/v04/I-05-R03.svg" alt="Dos relojes y una regla de derivación. Diagrama del capítulo 5; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="403" height="242" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 5.5.** Las leyes $s=u$ y $s=u^2$ recorren el mismo intervalo con velocidades distintas. Bajo un cambio $s=\phi(u)$, la derivada de $r(\phi(u))$ contiene el factor $\phi^\prime(u)$. En $u=0$, el segundo reloj deja de ser regular. Véase §[5.9](#fispm-c05-reparametrizaciuxf3n-y-regla-de-la-cadena).

</figcaption>

</figure>

$$\boxed{ \text{¿qué propiedades cambian cuando cambiamos el parámetro de una curva?} }$$

Antes de responder necesitamos distinguir con precisión qué significa el nuevo parámetro y qué hipótesis imponemos sobre $\phi$.

Activación Si escribimos $\widetilde P(u)=P(\phi(u))$, ¿hemos cambiado necesariamente la trayectoria geométrica? ¿Hemos cambiado necesariamente el movimiento físico? ¿Son la misma pregunta?

[]{#fispm-c05-definir-reparametrizaciuxf3n-de-una-curva label="fispm-c05-definir-reparametrizaciuxf3n-de-una-curva"}

**Definición 5.15 --- Reparametrización de una curva** Sea

$$P:I\to\mathcal E$$

una curva y sea

$$\phi:J\to I$$

una aplicación entre intervalos reales. La curva

$$\boxed{ \widetilde P := P\circ\phi:J\to\mathcal E, \qquad \widetilde P(u)=P(\phi(u)), }$$

se llama una **reparametrización de $P$ por $\phi$**.[^6]

Definición 5.15 no exige todavía que $\phi$ sea biyectiva ni derivable. Por tanto, una reparametrización en este sentido amplio puede:

- recorrer sólo una parte de la imagen de $P$;

- recorrer algunos puntos varias veces;

- detenerse sobre un mismo valor de $P$ durante un intervalo;

- invertir el orden con que se recorren los puntos.

Las propiedades más fuertes aparecerán al imponer condiciones adicionales.

[]{#el-parámetro-nuevo-no-recibe-significado-físico-automáticamente}

### 5.9.2. El parámetro nuevo no recibe significado físico automáticamente {#fispm-c05-el-paruxe1metro-nuevo-no-recibe-significado-fuxedsico-automuxe1ticamente}

La letra usada para parametrizar una curva no determina por sí sola qué magnitud representa. Podemos escribir

$$P(t)$$

cuando $t$ se interpreta como tiempo físico, pero también podemos estudiar la misma aplicación geométrica mediante un parámetro abstracto

$$u.$$

Por ello, al formar

$$\widetilde P(u)=P(\phi(u)),$$

no debemos declarar automáticamente que $u$ es un nuevo tiempo físico. Esta distinción es crucial porque dos situaciones matemáticamente parecidas pueden expresar preguntas físicas distintas:

1.  **cambio de parámetro geométrico:** usamos otra variable para describir el mismo recorrido;

2.  **nueva ley temporal:** interpretamos el nuevo parámetro como tiempo físico y, con ello, potencialmente cambiamos la historia temporal del movimiento.

§9 construirá primero la transformación matemática. La interpretación física del nuevo parámetro deberá declararse explícitamente.

[]{#principio-metodológico-declarar-qué-significa-el-parámetro}

### 5.9.3. Principio metodológico: declarar qué significa el parámetro {#fispm-c05-principio-metodoluxf3gico-declarar-quuxe9-significa-el-paruxe1metro}

**Principio metodológico 5.11 --- Declarar qué significa el parámetro antes de reparametrizar** Antes de interpretar

$$\widetilde P(u)=P(\phi(u)),$$

declarar si $u$ es:

- una variable auxiliar o geométrica;

- una nueva lectura temporal física;

- u otro parámetro con significado previamente especificado.

La igualdad formal

$$\widetilde P=P\circ\phi$$

no decide por sí sola esa interpretación.

principio metodológico 5.11 evita el falso razonamiento:

> «Como $P$ y $\widetilde P$ tienen la misma imagen, describen necesariamente el mismo movimiento físico.»

La imagen geométrica y la ley temporal son niveles diferentes. §10 desarrollará esa distinción con más detalle.

[]{#por-qué-necesitamos-una-clase-de-reparametrizaciones-admisibles}

### 5.9.4. Por qué necesitamos una clase de reparametrizaciones admisibles {#fispm-c05-por-quuxe9-necesitamos-una-clase-de-reparametrizaciones-admisibles}

Si queremos comparar derivadas y conservar un control regular del recorrido, no basta una aplicación arbitraria $\phi$. Por ejemplo, si

$$\phi'(u_0)=0,$$

la variación del nuevo parámetro puede colapsar localmente y alterar la regularidad de la curva reparametrizada. Si $\phi$ no es biyectiva, distintos valores de $u$ pueden corresponder al mismo valor del parámetro original o quedar partes del intervalo $I$ sin alcanzar. Para los resultados estructurales de esta sección necesitaremos una clase más restrictiva.

[]{#definir-reparametrización-regular-admisible}

### 5.9.5. Definir: reparametrización regular admisible {#fispm-c05-definir-reparametrizaciuxf3n-regular-admisible}

En esta sección adoptamos una convención única para intervalos con extremos incluidos: las derivadas en puntos interiores son derivadas ordinarias; en un extremo incluido, una expresión como $\phi'(u)$ designa la derivada lateral correspondiente. Así, $C^1$ en un intervalo cerrado significa que la derivada interior admite las extensiones laterales continuas necesarias en los extremos.

**Definición 5.16 --- Reparametrización regular admisible** Sean $I,J\subseteq\mathbb R$ intervalos. Una aplicación

$$\phi:J\longrightarrow I$$

es una **reparametrización regular admisible** si:

1.  $\phi$ es biyectiva;

2.  $\phi$ es de clase $C^1$;

3.  para todo $u\in J$, $$\boxed{\phi'(u)\ne0.}$$

La condición $\phi'(u)\ne0$ impide que el cambio de parámetro se detenga localmente. Como $J$ es un intervalo y $\phi'$ es continua, esa derivada no puede cambiar de signo sin anularse en algún punto. Por tanto, para una reparametrización regular admisible ocurre exactamente una de las dos posibilidades:

$$\phi'(u)>0 \quad\text{para todo }u\in J,$$

o

$$\phi'(u)<0 \quad\text{para todo }u\in J.$$

Además, en el nivel unidimensional importado de M3, la condición $\phi'(u)\ne0$ permite aplicar el teorema de la función inversa localmente; junto con la biyectividad entre intervalos, obtenemos la regularidad $C^1$ de la inversa en el nivel requerido por este capítulo.

[]{#fispm-c05-definir-orientaciuxf3n-del-paruxe1metro label="fispm-c05-definir-orientaciuxf3n-del-paruxe1metro"}

**Definición 5.17 --- Orientación del parámetro** Sea $\phi:J\to I$ una reparametrización regular admisible.

- Si $$\boxed{\phi'(u)>0\quad\text{para todo }u\in J,}$$ decimos que $\phi$ **preserva la orientación del parámetro**.

- Si $$\boxed{\phi'(u)<0\quad\text{para todo }u\in J,}$$ decimos que $\phi$ **invierte la orientación del parámetro**.

En intervalos, esta definición coincide con el comportamiento monótono esperado:

- $\phi'>0$ corresponde a una parametrización estrictamente creciente;

- $\phi'<0$ corresponde a una parametrización estrictamente decreciente.

La palabra «orientación» se refiere aquí al orden del parámetro, no a la orientación espacial de una base tridimensional estudiada en el capítulo 4.

[]{#ejemplos-mínimos-de-admisibilidad}

### 5.9.6. Ejemplos mínimos de admisibilidad {#fispm-c05-ejemplos-muxednimos-de-admisibilidad}

Consideremos

$$\phi_1(u)=2u+1.$$

Como $\phi_1'(u)=2>0,$

en intervalos adecuados donde sea biyectiva, $\phi_1$ es admisible y preserva orientación. En cambio, $\phi_2(u)=1-u$

satisface $\phi_2'(u)=-1<0,$

de modo que una vez fijados dominio y codominio compatibles es admisible e invierte orientación. Finalmente, $\phi_3(u)=u^3$

es biyectiva de $\mathbb R$ sobre $\mathbb R$, pero

$$\phi_3'(0)=0.$$

Por tanto, **no** es una reparametrización regular admisible según la definición 5.16. Este último ejemplo conecta con §6: la parametrización cúbica puede conservar una imagen geométrica muy simple y, sin embargo, introducir un instante con velocidad nula.

[]{#principio-metodológico-auditar-la-reparametrización-antes-de-derivar}

### 5.9.7. Principio metodológico: auditar la reparametrización antes de derivar {#fispm-c05-principio-metodoluxf3gico-auditar-la-reparametrizaciuxf3n-antes-de-derivar}

**Principio metodológico 5.12 --- Comprobar dominio, biyectividad, signo y no anulación de $\phi'$** Antes de aplicar una regla de transformación a una curva reparametrizada:

1.  declarar los intervalos $J$ e $I$;

2.  comprobar que $\phi:J\to I$ está bien definida;

3.  verificar si $\phi$ es biyectiva cuando se requiera una reparametrización admisible;

4.  comprobar que $\phi$ es $C^1$;

5.  verificar $$\phi'(u)\ne0;$$

6.  determinar el signo de $\phi'$ y, con ello, si la orientación se preserva o se invierte.

No utilizar la frase «sólo cambiamos de parámetro» como sustituto de estas comprobaciones. principio metodológico 5.12 será especialmente importante antes de las proposiciones 5.18--5.21, porque la regla de la cadena puede escribirse algebraicamente para situaciones más amplias, pero las conclusiones sobre regularidad, orientación y conservación controlada del recorrido dependen de hipótesis precisas.

[]{#qué-todavía-no-hemos-demostrado}

### 5.9.8. Qué todavía no hemos demostrado {#fispm-c05-quuxe9-todavuxeda-no-hemos-demostrado}

A partir de

$$\widetilde P=P\circ\phi$$

esperamos relacionar la velocidad de $\widetilde P$ con la velocidad de $P$. La fórmula que deberá demostrarse será $\widetilde v(u) = v(\phi(u))\,\phi'(u).$

Todavía no la usamos como resultado establecido. También quedan por demostrar:

- cuándo la imagen geométrica se conserva exactamente;

- por qué una reparametrización admisible conserva regularidad;

- cómo cambia la norma de la velocidad.

Esos serán proposiciones 5.18--5.21.

[]{#balance-de-definiciones-y-criterios}

### 5.9.9. Balance de definiciones y criterios {#fispm-c05-balance-de-definiciones-y-criterios}

La sección queda preparada mediante la cadena

$$\boxed{ P:I\to\mathcal E \quad+\quad \phi:J\to I \quad\longrightarrow\quad \widetilde P=P\circ\phi:J\to\mathcal E. }$$

Definición 5.15 define la operación general. Definición 5.16 identifica la clase de cambios de parámetro regulares y biyectivos que utilizaremos para los resultados estructurales. Definición 5.17 separa preservación e inversión de orientación mediante el signo de $\phi'$. principio metodológico 5.11 exige declarar el significado físico o geométrico del parámetro. principio metodológico 5.12 obliga a auditar dominio, biyectividad, regularidad y signo antes de extraer conclusiones. Las proposiciones siguientes demuestran proposiciones 5.18--5.21; ejercicios 5.18--5.19 aplican después estas leyes. La distinción física desarrollada en §10 permanece fuera de esta sección hasta su transición final.

[]{#proposición-regla-de-la-cadena-para-la-velocidad-reparametrizada}

### 5.9.10. Proposición: regla de la cadena para la velocidad reparametrizada {#fispm-c05-proposiciuxf3n-regla-de-la-cadena-para-la-velocidad-reparametrizada}

Sea

$$P:I\to\mathcal E$$

una curva derivable y sea

$$\phi:J\to I$$

una función derivable. Definamos

$$\widetilde P=P\circ\phi.$$

La derivada de $\widetilde P$ debe reconstruirse sin tratar puntos de $\mathcal E$ como vectores. Para ello fijamos un origen auxiliar $O$ y pasamos a la curva vectorial

$$r_O:I\to V, \qquad r_O(t)=\overrightarrow{OP(t)}.$$

Entonces

$$\widetilde r_O(u) := \overrightarrow{O\widetilde P(u)} = r_O(\phi(u)).$$

**Proposición 5.18 --- Regla de la cadena para la velocidad reparametrizada** Sea $P:I\to\mathcal E$ derivable en $\phi(u)$ y sea $\phi:J\to I$ derivable en $u$. Entonces $\widetilde P=P\circ\phi$ es derivable en $u$ y

$$\boxed{ \widetilde v(u) = v(\phi(u))\,\phi'(u). }$$

**Demostración.** Fijemos una base $B=(e_1,e_2,e_3)$ de $V$ y escribamos

$$[r_O(t)]_B = \begin{pmatrix} q^1(t)\\ q^2(t)\\ q^3(t) \end{pmatrix}.$$

Por proposición 5.8, como $r_O$ es derivable en $\phi(u)$, las funciones escalares $q^i$ son derivables allí. Además,

$$[\widetilde r_O(u)]_B = \begin{pmatrix} q^1(\phi(u))\\ q^2(\phi(u))\\ q^3(\phi(u)) \end{pmatrix}.$$

Aplicando la regla de la cadena escalar importada de M3 a cada componente,

$$\frac{d}{du}q^i(\phi(u)) = (q^i)'(\phi(u))\,\phi'(u).$$

Por proposición 5.8, esto reconstruye la derivada vectorial: $\widetilde r_O'(u) = r_O'(\phi(u))\,\phi'(u).$

Finalmente, proposición 5.9 identifica

$$\widetilde v(u)=\widetilde r_O'(u)$$

y

$$v(\phi(u))=r_O'(\phi(u)).$$

Por tanto,

$$\boxed{ \widetilde v(u) = v(\phi(u))\,\phi'(u). }$$

$\square$ proposición 5.18 muestra con precisión qué cambia bajo reparametrización: el vector velocidad original se evalúa en el parámetro correspondiente y luego se multiplica por el factor escalar $\phi'(u)$.

[]{#proposición-conservación-de-la-trayectoria-bajo-sobreyectividad}

### 5.9.11. Proposición: conservación de la trayectoria bajo sobreyectividad {#fispm-c05-proposiciuxf3n-conservaciuxf3n-de-la-trayectoria-bajo-sobreyectividad}

La imagen de una curva reparametrizada satisface siempre

$$\widetilde P(J) = P(\phi(J)).$$

Por ello, conservar exactamente la trayectoria geométrica requiere que $\phi$ alcance todo el intervalo original.

**Proposición 5.19 --- Conservación de la trayectoria bajo reparametrización sobreyectiva** Sea $P:I\to\mathcal E$ y sea $\phi:J\to I$ una aplicación sobreyectiva. Si

$$\widetilde P=P\circ\phi,$$

entonces

$$\boxed{ \widetilde P(J)=P(I). }$$

**Demostración.** Por definición,

$$\widetilde P(J) = \{P(\phi(u)):u\in J\} = P(\phi(J)).$$

Como $\phi$ es sobreyectiva, $\phi(J)=I.$ Por tanto, $\widetilde P(J)=P(I).$

$\square$ proposición 5.19 es puramente conjuntista: no requiere derivabilidad ni regularidad. La sobreyectividad basta para conservar la imagen geométrica completa.

[]{#proposición-regularidad-bajo-reparametrización-admisible}

### 5.9.12. Proposición: regularidad bajo reparametrización admisible {#fispm-c05-proposiciuxf3n-regularidad-bajo-reparametrizaciuxf3n-admisible}

Supongamos ahora que $\phi$ es regular admisible en el sentido de la definición 5.16. Si la curva original es regular en el punto correspondiente, $v(\phi(u))\ne0,$

y además

$$\phi'(u)\ne0,$$

Proposición 5.18 expresa $\widetilde v(u)$ como un producto de dos factores no nulos.

**Proposición 5.20 --- Conservación de regularidad bajo reparametrización admisible** Sea $\phi:J\to I$ una reparametrización regular admisible y sea $\widetilde P=P\circ\phi$. Si

$$v(\phi(u))\ne0,$$

entonces

$$\boxed{ \widetilde v(u)\ne0. }$$

**Demostración.** Por proposición 5.18,

$$\widetilde v(u) = v(\phi(u))\,\phi'(u).$$

Por definición 5.16, $\phi'(u)\ne0.$

Como $v(\phi(u))\ne0$, el producto de un vector no nulo por un escalar no nulo tampoco puede ser el vector cero. Luego

$$\widetilde v(u)\ne0.$$

$\square$ Así, una reparametrización regular admisible no crea un instante de reposo allí donde la curva original es regular. El ejemplo $\phi(u)=u^3$ queda deliberadamente fuera de esta conclusión porque $\phi'(0)=0$.

[]{#proposición-transformación-de-la-norma-de-la-velocidad}

### 5.9.13. Proposición: transformación de la norma de la velocidad {#fispm-c05-proposiciuxf3n-transformaciuxf3n-de-la-norma-de-la-velocidad}

La norma euclídea de $V$ es homogénea: $\|\lambda w\| = |\lambda|\,\|w\|.$

Aplicando esta propiedad a proposición 5.18 obtenemos la transformación de la norma de la velocidad.

**Proposición 5.21 --- Transformación de la norma de la velocidad bajo reparametrización** Bajo las hipótesis de la proposición 5.18,

$$\boxed{ \|\widetilde v(u)\| = \|v(\phi(u))\|\,|\phi'(u)|. }$$

**Demostración.** Por proposición 5.18,

$$\widetilde v(u) = v(\phi(u))\,\phi'(u).$$

Por homogeneidad de la norma,

$$\|\widetilde v(u)\| = \|v(\phi(u))\,\phi'(u)\| = |\phi'(u)|\,\|v(\phi(u))\|.$$

$\square$ El valor absoluto es esencial. Si $\phi'(u)<0$, la orientación del parámetro se invierte, pero la norma del vector velocidad sigue siendo no negativa. El nombre formal **rapidez** para $\|v\|$ continúa reservado para §11.

[]{#orientación-y-dirección-del-vector-velocidad}

### 5.9.14. Orientación y dirección del vector velocidad {#fispm-c05-orientaciuxf3n-y-direcciuxf3n-del-vector-velocidad}

Proposición 5.18 permite interpretar el signo de $\phi'$. Si

$$\phi'(u)>0,$$

entonces $\widetilde v(u)$ es un múltiplo positivo de $v(\phi(u))$: la dirección orientada del vector se conserva. Si

$$\phi'(u)<0,$$

entonces $\widetilde v(u)$ es un múltiplo negativo de $v(\phi(u))$: el vector velocidad cambia de sentido. Por tanto,

$$\boxed{ \phi'(u)>0 \Longrightarrow \widetilde v(u)\ \text{conserva el sentido}, }$$

mientras

$$\boxed{ \phi'(u)<0 \Longrightarrow \widetilde v(u)\ \text{invierte el sentido}. }$$

La recta tangente afín, sin embargo, permanece asociada a la misma dirección no orientada siempre que ambos vectores sean no nulos, porque multiplicar un vector director por un escalar no nulo no cambia la recta.

[]{#balance-de-las-leyes-de-reparametrización}

### 5.9.15. Balance de las leyes de reparametrización {#fispm-c05-balance-de-las-leyes-de-reparametrizaciuxf3n}

Hemos demostrado cuatro efectos distintos de una reparametrización:

$$\boxed{ \widetilde v(u) = v(\phi(u))\,\phi'(u), }$$

$$\boxed{ \phi(J)=I \Longrightarrow \widetilde P(J)=P(I), }$$

$$\boxed{ v(\phi(u))\ne0,\ \phi'(u)\ne0 \Longrightarrow \widetilde v(u)\ne0, }$$

y

$$\boxed{ \|\widetilde v(u)\| = \|v(\phi(u))\|\,|\phi'(u)|. }$$

Así quedan separados cuatro niveles:

- imagen geométrica;

- regularidad;

- orientación del parámetro;

- escala del vector velocidad.

Una reparametrización admisible conserva la trayectoria completa y la regularidad, pero puede modificar la velocidad como vector función del parámetro. Si además invierte orientación, invierte el sentido del vector velocidad. Ejercicios 5.18--5.19 aplican estas leyes de forma explícita. La cuestión de si dos parametrizaciones con la misma imagen representan o no el **mismo movimiento físico** pertenece a §10.

### 5.9.15. Regla de la cadena vectorial {#fispm-c05-e018-regla-de-la-cadena-vectorial .unnumbered}

**Ejercicio 5.18 · Prueba y cálculo** Sean $A\in\mathcal E$ y $e_1,e_2\in V$ dos vectores linealmente independientes. Considera

$$P:(0,\infty)\longrightarrow\mathcal E, \qquad P(t)=A+t e_1+t^2e_2,$$

y la función

$$\phi:(0,\infty)\longrightarrow(0,\infty), \qquad \phi(u)=u^2.$$

Define

$$\widetilde P=P\circ\phi.$$

1.  Verifica que $\phi$ es una reparametrización regular admisible y que preserva orientación.

2.  Calcula $v(t)$.

3.  Calcula $\widetilde P(u)$ y deriva directamente para obtener $\widetilde v(u)$.

4.  Verifica proposición 5.18: $$\widetilde v(u) = v(\phi(u))\,\phi'(u).$$

5.  Comprueba proposición 5.21 comparando $\|\widetilde v(u)\|$ con $\|v(\phi(u))\|\,|\phi'(u)|$.

**Solución desarrollada** La función

$$\phi(u)=u^2$$

es biyectiva de $(0,\infty)$ sobre $(0,\infty)$, es de clase $C^1$ y satisface $\phi'(u)=2u>0$

para todo $u>0$. Por definición 5.16 es regular admisible y, por la definición 5.17, preserva orientación.

Tomando $A$ como origen auxiliar, $r_A(t)=te_1+t^2e_2.$ Por proposición 5.9,

$$\boxed{ v(t)=e_1+2te_2. }$$

La curva reparametrizada es $\widetilde P(u) = P(u^2) = A+u^2e_1+u^4e_2.$ Por tanto,

$$\boxed{ \widetilde v(u) = 2u\,e_1+4u^3e_2. }$$

Ahora evaluamos el lado derecho de la proposición 5.18: $v(\phi(u)) = v(u^2) = e_1+2u^2e_2,$

y

$$\phi'(u)=2u.$$

Luego

$$v(\phi(u))\,\phi'(u) = \left(e_1+2u^2e_2\right)2u = 2u\,e_1+4u^3e_2 = \widetilde v(u).$$

Así,

$$\boxed{ \widetilde v(u) = v(\phi(u))\,\phi'(u). }$$

Para la norma, proposición 5.21 da $\|\widetilde v(u)\| = \|v(u^2)\|\,2u,$

porque $u>0$. Esta igualdad también se obtiene directamente por homogeneidad:

$$\|\widetilde v(u)\| = \left\| 2u\left(e_1+2u^2e_2\right) \right\| = 2u\,\|e_1+2u^2e_2\|.$$

El ejercicio muestra que el factor $\phi'(u)$ modifica el vector velocidad aun cuando la imagen geométrica se conserva.

### 5.9.15. Preservar o invertir orientación {#fispm-c05-e019-preservar-o-invertir-orientaciuxf3n .unnumbered}

**Ejercicio 5.19 · Variación y signo** Sean $A\in\mathcal E$ y $e_1,e_2\in V$ linealmente independientes. Considera

$$P:\mathbb R\longrightarrow\mathcal E, \qquad P(t)=A+t e_1+t^2e_2.$$

Define dos reparametrizaciones

$$\phi_+(u)=2u, \qquad \phi_-(u)=-2u, \qquad u\in\mathbb R,$$

y las curvas

$$P_+:=P\circ\phi_+, \qquad P_-:=P\circ\phi_-.$$

1.  Verifica que $\phi_+$ y $\phi_-$ son regulares admisibles.

2.  Determina cuál preserva y cuál invierte la orientación.

3.  Calcula $v(t)$, $v_+(u)$ y $v_-(u)$.

4.  Verifica proposición 5.18 en ambos casos.

5.  Compara $\|v_+(u)\|$ y $\|v_-(u)\|$ con las normas de las velocidades originales en los parámetros correspondientes.

6.  Explica qué cambia en el sentido del vector velocidad y qué ocurre con la recta tangente.

**Solución desarrollada** Ambas funciones son biyectivas de $\mathbb R$ sobre $\mathbb R$ y de clase $C^1$. Sus derivadas son

$$\phi_+'(u)=2>0, \qquad \phi_-'(u)=-2<0.$$

Por definición 5.16, ambas son regulares admisibles. Por definición 5.17, $\phi_+$ preserva orientación y $\phi_-$ la invierte. La velocidad de la curva original es

$$\boxed{ v(t)=e_1+2te_2. }$$

Para $P_+$, $P_+(u) = A+2u\,e_1+4u^2e_2,$

de modo que

$$\boxed{ v_+(u)=2e_1+8u\,e_2. }$$

Proposición 5.18 produce exactamente el mismo resultado:

$$v(\phi_+(u))\,\phi_+'(u) = \left(e_1+4u\,e_2\right)2 = 2e_1+8u\,e_2.$$

Para $P_-$, $P_-(u) = A-2u\,e_1+4u^2e_2,$

por lo que

$$\boxed{ v_-(u)=-2e_1+8u\,e_2. }$$

Nuevamente proposición 5.18 coincide:

$$v(\phi_-(u))\,\phi_-'(u) = \left(e_1-4u\,e_2\right)(-2) = -2e_1+8u\,e_2.$$

Las normas satisfacen

$$\boxed{ \|v_+(u)\| = 2\,\|v(2u)\|, }$$

y

$$\boxed{ \|v_-(u)\| = 2\,\|v(-2u)\|. }$$

El signo negativo de $\phi_-'$ no vuelve negativa una norma: proposición 5.21 introduce el valor absoluto. En el caso $\phi_+$, $v_+(u)$ tiene el mismo sentido que $v(2u)$. En el caso $\phi_-$, $v_-(u)$ tiene el sentido opuesto a $v(-2u)$.

Sin embargo, siempre que los vectores sean no nulos, multiplicarlos por el escalar $2$ o $-2$ no cambia la **recta tangente afín** que generan. Lo que cambia con el signo es la orientación del recorrido, no la dirección no orientada de la recta tangente.

[]{#cierre-conceptual-misma-curva-geométrica-otro-parámetro}

### 5.9.16. Cierre conceptual: misma curva geométrica, otro parámetro {#fispm-c05-cierre-conceptual-misma-curva-geomuxe9trica-otro-paruxe1metro}

§9 ha separado cuatro preguntas que suelen mezclarse:

$$\boxed{ \text{¿qué imagen se recorre?} }$$

$$\boxed{ \text{¿con qué parámetro se recorre?} }$$

$$\boxed{ \text{¿con qué orientación se recorre?} }$$

y

$$\boxed{ \text{¿qué significado físico atribuimos a ese parámetro?} }$$

Para una reparametrización

$$\widetilde P=P\circ\phi,$$

Proposición 5.18 establece

$$\widetilde v = (v\circ\phi)\phi',$$

Proposición 5.19 identifica la condición de sobreyectividad que conserva la trayectoria completa, proposición 5.20 muestra que una reparametrización regular admisible conserva regularidad y proposición 5.21 controla la norma de la velocidad mediante $\|\widetilde v\| = (\|v\|\circ\phi)|\phi'|.$ ejercicio 5.18 mostró cómo una reparametrización no lineal modifica la velocidad según la regla de la cadena. Ejercicio 5.19 separó el caso que preserva orientación del que la invierte y mostró que el signo de $\phi'$ cambia el sentido del vector velocidad, pero no la recta tangente no orientada. La conclusión metodológica es

$$\boxed{ \text{cambiar el parámetro} \ne \text{cambiar automáticamente el significado físico del tiempo}. }$$

§10 estudiará precisamente la diferencia entre compartir una misma trayectoria geométrica y representar el mismo movimiento físico. Esa cuestión no se anticipa aquí.

[]{#la-misma-trayectoria-no-significa-el-mismo-movimiento}

[]{#fispm-t1-c05-s10}

[]{#fpm-i-05-s10}

## 5.10. La misma trayectoria no significa el mismo movimiento {#fispm-c05-la-misma-trayectoria-no-significa-el-mismo-movimiento}

[]{#activación-ver-el-camino-no-basta-para-conocer-el-movimiento}

### 5.10.1. Activación: ver el camino no basta para conocer el movimiento {#fispm-c05-activaciuxf3n-ver-el-camino-no-basta-para-conocer-el-movimiento}

Una trayectoria geométrica es un conjunto de puntos: $\Gamma=P(I)\subseteq\mathcal E.$ Un movimiento, en cambio, es una aplicación parametrizada

$$P:I\to\mathcal E.$$

La imagen responde a la pregunta

$$\boxed{ \text{¿por qué puntos pasa el móvil?} }$$

mientras la aplicación completa responde también a

$$\boxed{ \text{¿qué posición corresponde a cada valor del parámetro?} }$$

Dos curvas pueden dibujar exactamente la misma figura en el espacio y, sin embargo, asignar tiempos distintos a sus puntos, recorrerlos con velocidades diferentes o hacerlo en sentidos opuestos.

[]{#fig:I-05-N01}

<figure id="fig-fpm-v04-i-05-n01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-05-N01.svg" class="lightbox" data-gallery="fpm-v04-c05"><img src="/assets/books/fispm/v04/I-05-N01.svg" alt="Una imagen, dos relojes. Diagrama del capítulo 5; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="395" height="247" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 5.6.** En $0\le u\le1$, las leyes $X_A=u$ y $X_B=u^2$ recorren el mismo segmento. En $u=1/2$ ocupan lugares distintos, y sus velocidades iniciales también difieren. Véase §[5.10](#fispm-c05-la-misma-trayectoria-no-significa-el-mismo-movimiento).

</figcaption>

</figure>

Activación Si sólo conocemos la figura trazada por un movimiento, ¿podemos reconstruir en qué instante se ocupó cada punto? ¿Podemos reconstruir su velocidad?

[]{#fispm-c05-definir-igualdad-de-trayectoria-geomuxe9trica label="fispm-c05-definir-igualdad-de-trayectoria-geomuxe9trica"}

**Definición 5.18 --- Igualdad de trayectoria geométrica** Sean

$$P:I\to\mathcal E, \qquad Q:J\to\mathcal E$$

dos movimientos parametrizados. Decimos que tienen la **misma trayectoria geométrica** si

$$\boxed{ P(I)=Q(J). }$$

Definición 5.18 compara únicamente las imágenes como subconjuntos de $\mathcal E$. No afirma:

- que $I=J$;

- que $P=Q$ como aplicaciones;

- que los mismos valores del parámetro correspondan a los mismos puntos;

- que las velocidades coincidan;

- que el orden temporal de recorrido sea el mismo.

La igualdad de trayectoria es, por tanto, una afirmación geométrica más débil que la igualdad de movimiento parametrizado.

[]{#tres-niveles-que-no-deben-confundirse}

### 5.10.2. Tres niveles que no deben confundirse {#fispm-c05-tres-niveles-que-no-deben-confundirse}

Conviene distinguir explícitamente:

$$\boxed{ \text{imagen geométrica} }$$

$$\boxed{ \text{curva parametrizada} }$$

y

$$\boxed{ \text{movimiento con parámetro interpretado como tiempo físico}. }$$

El primer nivel sólo conserva el conjunto de puntos. El segundo conserva también cómo el parámetro recorre esos puntos. El tercero añade una interpretación física al parámetro: sus valores representan lecturas temporales. Una reparametrización puede ser perfectamente legítima como descripción geométrica y, al mismo tiempo, producir una ley temporal distinta si el nuevo parámetro se declara nuevamente como tiempo físico.

[]{#fispm-c05-principio-metodoluxf3gico-misma-imagen-no-implica-mismo-movimiento-fuxedsico label="fispm-c05-principio-metodoluxf3gico-misma-imagen-no-implica-mismo-movimiento-fuxedsico"}

**Principio metodológico 5.13 --- Misma imagen no implica mismo movimiento físico** De

$$P(I)=Q(J)$$

sólo puede concluirse que ambos movimientos tienen la misma trayectoria geométrica.

Para comparar movimientos físicos hay que preguntar además:

1.  qué significa cada parámetro;

2.  qué punto corresponde a cada lectura temporal;

3.  en qué orden se recorren los puntos;

4.  cómo se transforman las velocidades.

En particular, si ambos parámetros se interpretan como tiempo físico, dos curvas con la misma imagen pueden representar historias distintas. Error plausible «Como dos movimientos recorren exactamente la misma curva, son el mismo movimiento.» La conclusión confunde trayectoria con ley temporal. La trayectoria no contiene por sí sola información suficiente para reconstruir tiempos de paso ni velocidades.

[]{#primer-contraste-misma-recta-distintas-leyes-temporales}

### 5.10.3. Primer contraste: misma recta, distintas leyes temporales {#fispm-c05-primer-contraste-misma-recta-distintas-leyes-temporales}

Sea

$$A\in\mathcal E, \qquad u\in V, \qquad u\ne0.$$

Consideremos

$$P:\mathbb R\to\mathcal E, \qquad P(t)=A+t\,u,$$

y

$$Q:\mathbb R\to\mathcal E, \qquad Q(t)=A+2t\,u.$$

Sus imágenes son

$$P(\mathbb R) = \{A+\lambda u:\lambda\in\mathbb R\},$$

y

$$Q(\mathbb R) = \{A+\mu u:\mu\in\mathbb R\}.$$

Como ambos parámetros recorren todos los números reales,

$$\boxed{ P(\mathbb R)=Q(\mathbb R). }$$

Sin embargo, en la misma lectura numérica $t=1$, $P(1)=A+u,$

mientras

$$Q(1)=A+2u.$$

Por tanto, $P\ne Q$

como aplicaciones. Además, $v_P(t)=u,$

y

$$v_Q(t)=2u.$$

Si el parámetro de ambas curvas se interpreta como tiempo físico, tenemos dos historias temporales distintas sobre la misma trayectoria.

[]{#la-relación-con-la-reparametrización}

### 5.10.4. La relación con la reparametrización {#fispm-c05-la-relaciuxf3n-con-la-reparametrizaciuxf3n}

El ejemplo anterior no es arbitrario. Definamos

$$\phi:\mathbb R\to\mathbb R, \qquad \phi(t)=2t.$$

Entonces $Q=P\circ\phi.$ La función $\phi$ es una reparametrización regular admisible: $\phi'(t)=2>0.$ Por proposición 5.19, la imagen se conserva: $Q(\mathbb R)=P(\mathbb R).$ Por proposición 5.18, $v_Q(t) = v_P(\phi(t))\,\phi'(t).$ Como $v_P\equiv u$, $v_Q(t)=u\cdot2=2u.$

Así, la misma operación matemática puede leerse de dos maneras diferentes:

- como cambio de parámetro de una misma curva geométrica;

- como una nueva ley de movimiento si el nuevo parámetro vuelve a interpretarse como tiempo físico.

La matemática de la composición no decide cuál interpretación física se adopta.

[]{#fispm-c05-proposiciuxf3n-una-trayectoria-no-determina-una-uxfanica-ley-de-movimiento label="fispm-c05-proposiciuxf3n-una-trayectoria-no-determina-una-uxfanica-ley-de-movimiento"}

**Proposición 5.22 --- Una trayectoria no determina una única ley de movimiento** Existen dos movimientos parametrizados con la misma trayectoria geométrica y distintas velocidades como funciones del parámetro.

En particular, una reparametrización regular admisible no trivial puede preservar la imagen y modificar la velocidad.

**Demostración.** Sean

$$P(t)=A+t\,u, \qquad u\ne0,$$

y

$$\phi(t)=2t.$$

Definamos

$$Q=P\circ\phi.$$

Como $\phi$ es biyectiva de $\mathbb R$ sobre $\mathbb R$, proposición 5.19 da $Q(\mathbb R)=P(\mathbb R).$ Por proposición 5.18, $v_Q(t) = v_P(2t)\cdot2.$ Pero

$$v_P(t)=u,$$

de modo que

$$\boxed{ v_Q(t)=2u\ne u=v_P(t). }$$

Así, $P$ y $Q$ tienen la misma trayectoria geométrica pero velocidades distintas como funciones del parámetro. Por tanto, la trayectoria no determina una única ley de movimiento. $\square$ proposición 5.22 es una afirmación de existencia: basta un ejemplo explícito para descartar la identificación

$$\text{trayectoria} = \text{movimiento}.$$

[]{#qué-información-pierde-la-trayectoria}

### 5.10.5. Qué información pierde la trayectoria {#fispm-c05-quuxe9-informaciuxf3n-pierde-la-trayectoria}

Al pasar de

$$P:I\to\mathcal E$$

a su imagen

$$\Gamma=P(I),$$

olvidamos, en general:

- el dominio del parámetro;

- los tiempos de paso;

- el sentido de recorrido;

- la multiplicidad con que pueden visitarse puntos;

- la velocidad;

- la escala temporal local.

La trayectoria retiene geometría espacial, pero no la historia completa del recorrido. Esta pérdida de información puede resumirse como

$$\boxed{ P \longmapsto P(I) }$$

una operación que, en general, no es invertible.

[]{#balance-conceptual-2}

### 5.10.6. Balance conceptual {#fispm-c05-balance-conceptual-2}

§10 fija ahora la distinción central:

$$\boxed{ P(I)=Q(J) \not\Rightarrow P=Q. }$$

Si además los parámetros se interpretan como tiempo físico,

$$\boxed{ \text{misma trayectoria} \not\Rightarrow \text{misma historia temporal}. }$$

Definición 5.18 formaliza la igualdad geométrica de trayectoria. principio metodológico 5.13 obliga a no convertir esa igualdad en una afirmación física más fuerte. Proposición 5.22 demuestra constructivamente que una misma trayectoria admite leyes parametrizadas distintas. Ejercicios 5.20--5.21 harán explícita la diferencia entre varios «relojes» sobre una misma trayectoria y entre reparametrización geométrica y reinterpretación temporal. La noción formal de rapidez pertenece a §11 y no se introduce todavía.

### 5.10.6. Tres relojes sobre el mismo segmento {#fispm-c05-e020-tres-relojes-sobre-el-mismo-segmento .unnumbered}

**Ejercicio 5.20 · Síntesis y contraejemplo** Sean $A,B\in\mathcal E$, con $A\ne B$, y define

$$d:=\overrightarrow{AB}\in V.$$

Considera los tres movimientos

$$P_1:[0,1]\to\mathcal E, \qquad P_1(t)=A+t\,d,$$

$$P_2:[0,2]\to\mathcal E, \qquad P_2(s)=A+\frac{s}{2}\,d,$$

y

$$P_3:\left[0,\frac12\right]\to\mathcal E, \qquad P_3(r)=A+2r\,d.$$

1.  Demuestra que los tres movimientos tienen la misma trayectoria geométrica.

2.  Determina el tiempo total de recorrido de cada uno si sus parámetros se interpretan como tiempo físico.

3.  Sea $$M=A+\frac12d$$ el punto medio del segmento. Determina en qué lectura temporal llega cada movimiento a $M$.

4.  Calcula las velocidades $v_1$, $v_2$ y $v_3$.

5.  Explica por qué conocer sólo el segmento $\overline{AB}$ no permite reconstruir ninguna de estas tres historias temporales.

**Solución desarrollada** En los tres casos, el coeficiente que multiplica a $d$ recorre todo el intervalo $[0,1]$.

$$P_1([0,1]) = P_2([0,2]) = P_3\!\left(\left[0,\frac12\right]\right) = \{A+\lambda d:0\le\lambda\le1\}.$$

Por tanto, los tres movimientos tienen la misma trayectoria geométrica. Si los parámetros se interpretan como tiempo físico,

$$\boxed{ T_1=1,\qquad T_2=2,\qquad T_3=\frac12. }$$

Para alcanzar

$$M=A+\frac12d,$$

los coeficientes de $d$ deben valer $1/2$. Así,

$$\boxed{ t_M=\frac12,\qquad s_M=1,\qquad r_M=\frac14. }$$

Las velocidades son

$$\boxed{v_1(t)=d,}$$

$$\boxed{v_2(s)=\frac12d,}$$

y

$$\boxed{v_3(r)=2d.}$$

Los tres movimientos comparten exactamente el mismo segmento como trayectoria, pero asignan distintos tiempos de paso a sus puntos y poseen velocidades distintas. La trayectoria geométrica, por sí sola, no contiene la escala temporal del recorrido.

### 5.10.6. Reparametrización geométrica versus reinterpretación temporal {#fispm-c05-e021-reparametrizaciuxf3n-geomuxe9trica-versus-reinterpretaciuxf3n-temporal .unnumbered}

**Ejercicio 5.21 · Auditoría conceptual** Sean $A,B\in\mathcal E$, con $A\ne B$, y

$$d:=\overrightarrow{AB}.$$

Considera

$$P:[0,1]\to\mathcal E, \qquad P(t)=A+t\,d,$$

y

$$\phi:\left[0,\frac12\right]\to[0,1], \qquad \phi(u)=2u.$$

Define

$$\widetilde P=P\circ\phi, \qquad \widetilde P(u)=A+2u\,d.$$

Analiza por separado:

**A.** $u$ es sólo un parámetro auxiliar.

**B.** $u$ se declara un nuevo tiempo físico, medido en la misma unidad que $t$.

Decide qué ocurre con:

1.  igualdad de trayectoria geométrica;

2.  orden de recorrido;

3.  relación $t=2u$;

4.  identidad $$\widetilde v(u)=2\,v(2u);$$

5.  duración física total del recorrido;

6.  igualdad como movimientos físicos.

**Solución desarrollada** Como $\phi$ es biyectiva y

$$\phi'(u)=2>0,$$

es una reparametrización regular admisible que preserva orientación. Por proposición 5.19,

$$\boxed{ \widetilde P\!\left(\left[0,\frac12\right]\right) = P([0,1]). }$$

Por tanto, la trayectoria geométrica es la misma en ambas interpretaciones. Como $\phi'(u)>0$, también se conserva el orden del recorrido. La relación

$$\boxed{t=2u}$$

es simplemente la definición de $\phi$. Por proposición 5.18,

$$\widetilde v(u) = v(\phi(u))\,\phi'(u) = 2\,v(2u).$$

Esta identidad es matemática y vale con independencia de la interpretación física de $u$.

**Interpretación A: $u$ es auxiliar.**

$\widetilde P$ es una descripción geométrica alternativa. El tiempo físico sigue siendo $t$, de modo que el intervalo $\left[0,\frac12\right]$ de $u$ no representa una nueva duración física. Tampoco se ha definido una nueva ley temporal física.

**Interpretación B: $u$ es un nuevo tiempo físico.**

Entonces sí tenemos una nueva historia temporal. El movimiento original tarda

$$T_P=1,$$

mientras el nuevo tarda

$$T_{\widetilde P}=\frac12.$$

Además, $v_P(t)=d, \qquad v_{\widetilde P}(u)=2d.$ Por tanto, si ambos parámetros son tiempos físicos medidos en la misma unidad, los movimientos son distintos aunque la trayectoria sea la misma.

La diferencia puede resumirse así:

[]{#cierre-conceptual-la-trayectoria-no-contiene-un-reloj}

### 5.10.7. Cierre conceptual: la trayectoria no contiene un reloj {#fispm-c05-cierre-conceptual-la-trayectoria-no-contiene-un-reloj}

§10 ha hecho explícita una pérdida de información fundamental:

$$P:I\to\mathcal E \quad\longmapsto\quad P(I)\subseteq\mathcal E$$

olvida la ley que asigna valores del parámetro a los puntos de la trayectoria. Por eso,

$$\boxed{ \text{misma trayectoria} \not\Rightarrow \text{mismo movimiento parametrizado}, }$$

y, cuando los parámetros se interpretan como tiempo físico,

$$\boxed{ \text{misma trayectoria} \not\Rightarrow \text{misma historia temporal}. }$$

Proposición 5.22 mostró constructivamente que una misma trayectoria admite velocidades distintas. Ejercicio 5.20 añadió tres escalas temporales diferentes sobre un mismo segmento. Ejercicio 5.21 separó reparametrización geométrica de reinterpretación temporal. La conclusión de la sección puede expresarse como

$$\boxed{ \text{la trayectoria describe dónde;} \qquad \text{la parametrización añade cómo y cuándo.} }$$

§11 introducirá formalmente la norma de la velocidad como magnitud escalar y comenzará a comparar desplazamiento neto con aproximaciones al camino recorrido.

[]{#rapidez-desplazamiento-y-aproximaciones-al-camino-recorrido}

[]{#fispm-t1-c05-s11}

[]{#fpm-i-05-s11}

## 5.11. Rapidez, desplazamiento y aproximaciones al camino recorrido {#fispm-c05-rapidez-desplazamiento-y-aproximaciones-al-camino-recorrido}

[]{#activación-un-vector-y-una-magnitud-escalar-no-responden-a-la-misma-pregunta}

### 5.11.1. Activación: un vector y una magnitud escalar no responden a la misma pregunta {#fispm-c05-activaciuxf3n-un-vector-y-una-magnitud-escalar-no-responden-a-la-misma-pregunta}

La velocidad instantánea es un vector

$$v(t)\in V.$$

Por tanto, contiene información de magnitud y dirección. Sin embargo, muchas preguntas físicas requieren sólo una magnitud escalar: cuánto vale el tamaño de ese vector, independientemente de la dirección espacial que tenga. La estructura euclídea de $V$ ya proporciona una norma $\|\cdot\|:V\to[0,\infty).$

Aplicarla a la velocidad produce una función escalar del parámetro.

Activación ¿Qué información se pierde cuando reemplazamos $v(t)$ por $\|v(t)\|$? ¿Puede haber dos velocidades distintas con la misma norma?

[]{#fispm-c05-definir-rapidez label="fispm-c05-definir-rapidez"}

**Definición 5.19 --- Rapidez** Sea $P:I\to\mathcal E$ un movimiento derivable y sea

$$v:I\to V$$

su velocidad. Definimos la **rapidez** por

$$\boxed{ \sigma(t) := \|v(t)\| \ge0. }$$

La rapidez es un **escalar no negativo**. En cambio, la velocidad es un vector.[^7] Por tanto,

$$\boxed{ \sigma(t)\in\mathbb R_{\ge0}, \qquad v(t)\in V. }$$

Si $t$ representa tiempo físico, $[\sigma] = [v] = \frac{L}{T}.$ La norma elimina la dirección, pero conserva la magnitud del vector velocidad.

[]{#fispm-c05-principio-metodoluxf3gico-rapidez-es-norma-velocidad-conserva-direcciuxf3n label="fispm-c05-principio-metodoluxf3gico-rapidez-es-norma-velocidad-conserva-direcciuxf3n"}

**Principio metodológico 5.14 --- Rapidez es norma; velocidad conserva dirección** No usar «rapidez» y «velocidad» como sinónimos.

La velocidad

$$v(t)\in V$$

es vectorial. La rapidez

$$\sigma(t)=\|v(t)\|$$

es escalar.

Dos movimientos pueden satisfacer

$$\|v_1(t)\|=\|v_2(t)\|$$

y, sin embargo, $v_1(t)\ne v_2(t)$

porque sus direcciones o sentidos son distintos. Este principio será importante cuando comparemos recorridos: una suma de **distancias** entre puntos produce escalares, mientras una suma de **desplazamientos** produce vectores.

[]{#desplazamiento-neto-y-recorrido-intermedio}

### 5.11.2. Desplazamiento neto y recorrido intermedio {#fispm-c05-desplazamiento-neto-y-recorrido-intermedio}

Sean $a<b$ dos instantes. El desplazamiento neto entre los extremos es

$$\Delta P_{a,b} = \overrightarrow{P(a)P(b)} \in V.$$

Su norma es la distancia entre los puntos extremos: $\|\Delta P_{a,b}\| = d(P(a),P(b)).$ Pero conocer sólo los extremos no registra por dónde pasó la curva entre $a$ y $b$. Para recuperar información intermedia podemos insertar tiempos adicionales

$$a=t_0<t_1<\cdots<t_n=b$$

y considerar la sucesión de posiciones

$$P(t_0),P(t_1),\ldots,P(t_n).$$

Uniendo posiciones consecutivas mediante segmentos obtenemos un recorrido poligonal que aproxima la curva observada en esos instantes.

[]{#fispm-c05-definir-particiuxf3n-temporal label="fispm-c05-definir-particiuxf3n-temporal"}

**Definición 5.20 --- Partición temporal** Sea $[a,b]\subseteq I$. Si $a<b$, una **partición temporal** de $[a,b]$ es una colección finita ordenada

$$\boxed{ \Pi: a=t_0<t_1<\cdots<t_n=b. }$$

Si $a=b$, admitimos la **partición trivial**

$$\boxed{\Pi=\{a\}.}$$

Los puntos $t_i$ pertenecen al dominio del parámetro; no son puntos del espacio físico. Cada partición selecciona una muestra finita de posiciones sobre la curva. Una partición puede ser gruesa, con pocos instantes, o más fina, incorporando tiempos intermedios adicionales. La comparación sistemática entre refinamientos pertenecerá a §12.

[]{#fispm-c05-definir-longitud-poligonal-asociada-a-una-particiuxf3n label="fispm-c05-definir-longitud-poligonal-asociada-a-una-particiuxf3n"}

**Definición 5.21 --- Longitud poligonal asociada a una partición** Sea $P:[a,b]\to\mathcal E$ y sea

$$\Pi: a=t_0<t_1<\cdots<t_n=b$$

una partición. Definimos la **longitud poligonal de $P$ asociada a $\Pi$** por

$$\boxed{ L_\Pi(P) := \sum_{i=1}^{n} d\bigl(P(t_{i-1}),P(t_i)\bigr). }$$

Cuando $a=b$ y $\Pi=\{a\}$, la suma de la definición 5.21 es vacía y, por convención, vale $0$. Cada término es un escalar no negativo con dimensión de longitud. Por tanto, $L_\Pi(P)\ge0, \qquad [L_\Pi]=L.$ También podemos escribir

$$d\bigl(P(t_{i-1}),P(t_i)\bigr) = \left\| \overrightarrow{P(t_{i-1})P(t_i)} \right\|.$$

Así,

$$L_\Pi(P) = \sum_{i=1}^{n} \left\| \Delta P_{t_{i-1},t_i} \right\|.$$

La norma se aplica **antes** de sumar.

[]{#sumar-desplazamientos-no-es-sumar-distancias}

### 5.11.3. Sumar desplazamientos no es sumar distancias {#fispm-c05-sumar-desplazamientos-no-es-sumar-distancias}

Por proposición 5.6,

$$\sum_{i=1}^{n} \Delta P_{t_{i-1},t_i} = \Delta P_{a,b}.$$

El lado izquierdo es una suma de vectores y las cancelaciones de dirección son posibles. En cambio,

$$L_\Pi(P) = \sum_{i=1}^{n} \left\| \Delta P_{t_{i-1},t_i} \right\|$$

es una suma de escalares no negativos. Por eso no debemos confundir

$$\left\| \sum_{i=1}^{n} \Delta P_{t_{i-1},t_i} \right\|$$

con

$$\sum_{i=1}^{n} \left\| \Delta P_{t_{i-1},t_i} \right\|.$$

La primera expresión mide la norma del desplazamiento neto; la segunda mide la longitud del recorrido poligonal determinado por la partición.

[]{#fispm-c05-principio-metodoluxf3gico-no-confundir-desplazamiento-neto-con-camino-recorrido label="fispm-c05-principio-metodoluxf3gico-no-confundir-desplazamiento-neto-con-camino-recorrido"}

**Principio metodológico 5.15 --- No confundir desplazamiento neto con camino recorrido** Para un intervalo $[a,b]$ distinguir siempre:

$$\boxed{ \Delta P_{a,b} = \overrightarrow{P(a)P(b)} }$$

del escalar

$$\boxed{ L_\Pi(P) = \sum_i d(P(t_{i-1}),P(t_i)). }$$

El desplazamiento neto depende sólo de los extremos y vive en $V$. La longitud poligonal depende de la partición, usa posiciones intermedias y es un escalar no negativo. Todavía no llamamos a $L_\Pi(P)$ «longitud de la curva». Para una partición fija es sólo una aproximación poligonal finita.

[]{#ejemplo-mínimo-regresar-al-punto-de-partida}

### 5.11.4. Ejemplo mínimo: regresar al punto de partida {#fispm-c05-ejemplo-muxednimo-regresar-al-punto-de-partida}

Supongamos que

$$P(a)=P(b),$$

pero que existe un instante intermedio $c\in(a,b)$ tal que

$$P(c)\ne P(a).$$

Entonces $\Delta P_{a,b}=0$

y

$$d(P(a),P(b))=0.$$

Sin embargo, para la partición

$$\Pi=\{a,c,b\},$$

tenemos $L_\Pi(P) = d(P(a),P(c)) + d(P(c),P(b)).$

Como $P(c)\ne P(a)=P(b)$, $L_\Pi(P)>0.$ El ejemplo hace visible que un desplazamiento neto nulo no implica un recorrido poligonal nulo.

[]{#qué-todavía-no-hemos-demostrado-1}

### 5.11.5. Qué todavía no hemos demostrado {#fispm-c05-quuxe9-todavuxeda-no-hemos-demostrado-1}

La desigualdad triangular sugiere que, para cualquier partición, $d(P(a),P(b)) \le L_\Pi(P).$ Éste será proposición 5.23 y todavía no lo usamos como resultado establecido. También esperamos relacionar rapidez nula e instante de reposo mediante $\sigma(t)=0 \Longleftrightarrow v(t)=0.$

Éste será proposición 5.24. Finalmente, una sola partición no define todavía una longitud geométrica exacta de la curva. Para ello tendremos que considerar **todas** las particiones y una operación de supremo. Esa construcción pertenece a §12.

[]{#balance-de-definiciones}

### 5.11.6. Balance de definiciones {#fispm-c05-balance-de-definiciones}

La sección introduce tres objetos de tipos distintos:

$$\boxed{ v(t)\in V, \qquad \sigma(t)=\|v(t)\|\in\mathbb R_{\ge0}, }$$

$$\boxed{ \Delta P_{a,b}\in V, }$$

y

$$\boxed{ L_\Pi(P)\in\mathbb R_{\ge0}. }$$

Definición 5.19 convierte la velocidad en una magnitud escalar mediante la norma. Definición 5.20 selecciona una muestra temporal finita. Definición 5.21 mide la longitud del recorrido poligonal que une las posiciones seleccionadas. principio metodológico 5.14 impide identificar rapidez y velocidad. principio metodológico 5.15 impide identificar desplazamiento neto y camino aproximado. Las proposiciones siguientes demuestran proposiciones 5.23--5.24 y ejercicios 5.22--5.23 aplican después esas relaciones. La longitud geométrica exacta continúa reservada para §12.

[]{#proposición-toda-longitud-poligonal-domina-el-desplazamiento-neto}

### 5.11.7. Proposición: toda longitud poligonal domina el desplazamiento neto {#fispm-c05-proposiciuxf3n-toda-longitud-poligonal-domina-el-desplazamiento-neto}

La relación entre desplazamiento neto y longitud poligonal se obtiene combinando dos hechos ya establecidos:

1.  los desplazamientos sucesivos se suman telescópicamente;

2.  la norma satisface la desigualdad triangular.

**Proposición 5.23 --- Toda longitud poligonal domina el desplazamiento neto** Sea

$$\Pi: a=t_0<t_1<\cdots<t_n=b$$

una partición temporal. Entonces

$$\boxed{ d(P(a),P(b)) \le L_\Pi(P). }$$

**Demostración.** Por proposición 5.6, aplicado sucesivamente,

$$\Delta P_{a,b} = \sum_{i=1}^{n} \Delta P_{t_{i-1},t_i}.$$

Tomando normas,

$$d(P(a),P(b)) = \|\Delta P_{a,b}\| = \left\| \sum_{i=1}^{n} \Delta P_{t_{i-1},t_i} \right\|.$$

Por la desigualdad triangular finita,

$$\left\| \sum_{i=1}^{n} \Delta P_{t_{i-1},t_i} \right\| \le \sum_{i=1}^{n} \left\| \Delta P_{t_{i-1},t_i} \right\|.$$

Por definición 5.21,

$$\sum_{i=1}^{n} \left\| \Delta P_{t_{i-1},t_i} \right\| = L_\Pi(P).$$

Luego

$$\boxed{ d(P(a),P(b)) \le L_\Pi(P). }$$

$\square$ proposición 5.23 formaliza una idea geométrica básica: cualquier camino poligonal construido con puntos intermedios de la curva no puede ser más corto que la cuerda que une directamente los extremos. La desigualdad no afirma todavía que exista una «longitud de la curva» independiente de la partición. Sólo compara una partición concreta con el desplazamiento neto.

[]{#consecuencia-conceptual-los-extremos-no-contienen-el-recorrido}

### 5.11.8. Consecuencia conceptual: los extremos no contienen el recorrido {#fispm-c05-consecuencia-conceptual-los-extremos-no-contienen-el-recorrido}

Proposición 5.23 permite ordenar dos cantidades escalares: $d(P(a),P(b)) \le L_\Pi(P).$ El lado izquierdo depende únicamente de los extremos. El lado derecho depende también de los puntos intermedios seleccionados por $\Pi$. Por tanto, incluso cuando ambas cantidades tienen la misma dimensión física, no contienen la misma información. En particular, si

$$P(a)=P(b),$$

entonces $d(P(a),P(b))=0,$

pero proposición 5.23 sólo obliga a

$$0\le L_\Pi(P),$$

y una partición con posiciones intermedias distintas puede dar una longitud poligonal estrictamente positiva.

[]{#proposición-rapidez-nula-e-instante-de-reposo}

### 5.11.9. Proposición: rapidez nula e instante de reposo {#fispm-c05-proposiciuxf3n-rapidez-nula-e-instante-de-reposo}

La rapidez se definió como la norma de la velocidad: $\sigma(t)=\|v(t)\|.$ En un espacio euclídeo, la norma es definida positiva: $\|w\|=0 \Longleftrightarrow w=0.$

**Proposición 5.24 --- Rapidez nula e instante de reposo** Para todo instante donde exista la velocidad,

$$\boxed{ \sigma(t)=0 \Longleftrightarrow v(t)=0. }$$

En consecuencia,

$$\boxed{ \sigma(t)=0 \Longleftrightarrow t\text{ es un instante de reposo}. }$$

**Demostración.** Por definición 5.19,

$$\sigma(t)=\|v(t)\|.$$

Si

$$\sigma(t)=0,$$

entonces $\|v(t)\|=0.$ Por definitud positiva de la norma, $v(t)=0.$

Recíprocamente, si

$$v(t)=0,$$

entonces $\sigma(t)=\|0\|=0.$

Así, $\sigma(t)=0 \Longleftrightarrow v(t)=0.$

Por definición 5.12, la condición $v(t)=0$ equivale exactamente a que $t$ sea un instante de reposo. $\square$ proposición 5.24 no añade una nueva noción de reposo: sólo expresa la misma condición mediante la magnitud escalar de la velocidad.

[]{#balance-de-las-desigualdades-y-equivalencias}

### 5.11.10. Balance de las desigualdades y equivalencias {#fispm-c05-balance-de-las-desigualdades-y-equivalencias}

La sección dispone ahora de dos relaciones fundamentales:

$$\boxed{ d(P(a),P(b)) \le L_\Pi(P), }$$

y

$$\boxed{ \sigma(t)=0 \Longleftrightarrow v(t)=0. }$$

Proposición 5.23 separa la distancia entre extremos de una aproximación al camino recorrido. Proposición 5.24 conecta una condición vectorial de reposo con una condición escalar de rapidez nula. La arquitectura sigue siendo deliberadamente finita:

$$\text{partición} \longrightarrow \text{longitud poligonal}$$

y todavía no

$$\text{todas las particiones} \longrightarrow \text{supremo}.$$

Ese paso pertenece a §12. Ejercicios 5.22--5.23 aplicarán la distinción velocidad/rapidez y la desigualdad entre cuerda y recorrido poligonal antes del cierre local de §11.

### 5.11.10. Velocidad versus rapidez {#fispm-c05-e022-velocidad-versus-rapidez .unnumbered}

**Ejercicio 5.22 · Tipado y métrica** Sea $B=(e_1,e_2,e_3)$ una base ortonormal de $V$. Considera dos movimientos con velocidades constantes

$$v_1=3e_1+4e_2,$$

y

$$v_2=4e_1-3e_2.$$

1.  Calcula las rapidez $\sigma_1$ y $\sigma_2$.

2.  Decide si $v_1=v_2$.

3.  Compara sus direcciones y explica por qué tener igual rapidez no implica tener igual velocidad.

4.  Si las componentes están expresadas en unidades de longitud/tiempo, audita las unidades de $v_1$, $v_2$, $\sigma_1$ y $\sigma_2$.

5.  Construye un tercer vector velocidad $v_3$ con la misma rapidez pero sentido opuesto a $v_1$.

**Solución desarrollada** Como $B$ es ortonormal,

$$\sigma_1 = \|v_1\| = \sqrt{3^2+4^2} = 5,$$

y

$$\sigma_2 = \|v_2\| = \sqrt{4^2+(-3)^2} = 5.$$

Por tanto,

$$\boxed{ \sigma_1=\sigma_2=5. }$$

Sin embargo, $v_1=3e_1+4e_2$

y

$$v_2=4e_1-3e_2$$

tienen componentes diferentes y, por tanto,

$$\boxed{ v_1\ne v_2. }$$

De hecho, sus direcciones no orientadas también son diferentes: no existe un escalar no nulo $\lambda$ tal que $v_2=\lambda v_1$. Así,

$$\boxed{ \|v_1\|=\|v_2\| \not\Rightarrow v_1=v_2. }$$

La rapidez conserva sólo la magnitud de la velocidad; la dirección y el sentido pertenecen al vector velocidad. Si las componentes de $v_1$ y $v_2$ se miden en unidades de longitud/tiempo, entonces $[v_1]=[v_2]=\frac{L}{T},$

y, por la definición 5.19, $[\sigma_1]=[\sigma_2]=\frac{L}{T}.$ Para obtener la misma rapidez con sentido opuesto a $v_1$, basta tomar

$$\boxed{ v_3=-v_1=-3e_1-4e_2. }$$

Entonces $\|v_3\|=\|-v_1\|=\|v_1\|=5,$

pero $v_3$ apunta en sentido opuesto.

### 5.11.10. Camino poligonal versus desplazamiento neto {#fispm-c05-e023-camino-poligonal-versus-desplazamiento-neto .unnumbered}

**Ejercicio 5.23 · Geometría y desigualdad** Sea $B=(e_1,e_2,e_3)$ una base ortonormal de $V$ y sea $A\in\mathcal E$. Considera un movimiento $P:[0,2]\to\mathcal E$ que pasa por

$$P(0)=A,$$

$$P(1)=A+3e_1,$$

y

$$P(2)=A+3e_1+4e_2.$$

Para la partición

$$\Pi=\{0,1,2\},$$

1.  calcula los dos desplazamientos parciales;

2.  calcula $L_\Pi(P)$;

3.  calcula el desplazamiento neto $\Delta P_{0,2}$ y su norma;

4.  verifica explícitamente proposición 5.23;

5.  explica qué información distingue $L_\Pi(P)$ de $d(P(0),P(2))$.

**Solución desarrollada** Los desplazamientos parciales son

$$\Delta P_{0,1} = \overrightarrow{P(0)P(1)} = 3e_1,$$

y

$$\Delta P_{1,2} = \overrightarrow{P(1)P(2)} = 4e_2.$$

Sus normas son

$$\|\Delta P_{0,1}\|=3, \qquad \|\Delta P_{1,2}\|=4.$$

Por definición 5.21,

$$L_\Pi(P) = 3+4 = \boxed{7}.$$

El desplazamiento neto es $\Delta P_{0,2} = 3e_1+4e_2.$

Como la base es ortonormal,

$$d(P(0),P(2)) = \|\Delta P_{0,2}\| = \sqrt{3^2+4^2} = \boxed{5}.$$

Así,

$$\boxed{ d(P(0),P(2)) = 5 \le 7 = L_\Pi(P), }$$

lo que verifica proposición 5.23.

La diferencia entre ambas cantidades es conceptual:

- $d(P(0),P(2))$ depende sólo de los extremos;

- $L_\Pi(P)$ incorpora también la posición intermedia $P(1)$.

En este ejemplo, el recorrido poligonal obliga a avanzar primero $3$ unidades en la dirección $e_1$ y luego $4$ unidades en la dirección $e_2$, mientras la cuerda entre los extremos mide sólo $5$ unidades. Por tanto,

$$\boxed{ \text{desplazamiento neto} \ne \text{camino poligonal asociado a }\Pi. }$$

[]{#cierre-conceptual-magnitud-instantánea-y-camino-finito}

### 5.11.11. Cierre conceptual: magnitud instantánea y camino finito {#fispm-c05-cierre-conceptual-magnitud-instantuxe1nea-y-camino-finito}

§11 ha conectado dos escalas de descripción. En un instante,

$$\boxed{ \sigma(t)=\|v(t)\| }$$

extrae la magnitud escalar de la velocidad. Sobre un intervalo y una partición,

$$\boxed{ L_\Pi(P) = \sum_i d(P(t_{i-1}),P(t_i)) }$$

mide un recorrido poligonal finito construido a partir de posiciones muestreadas. Proposición 5.23 establece que

$$d(P(a),P(b)) \le L_\Pi(P),$$

mientras proposición 5.24 identifica

$$\sigma(t)=0 \Longleftrightarrow v(t)=0.$$

Ejercicio 5.22 mostró que igual rapidez no implica igual velocidad. Ejercicio 5.23 mostró que la longitud de un recorrido poligonal puede superar estrictamente la distancia entre los extremos. La sección queda cerrada sin identificar todavía ninguna longitud poligonal concreta con la **longitud geométrica de la curva**. Ese paso exige considerar todas las particiones y definir un supremo. Pertenece íntegramente a §12.

[]{#longitud-geométrica-de-una-curva}

[]{#fispm-t1-c05-s12}

[]{#fpm-i-05-s12}

## 5.12. Longitud geométrica de una curva {#fispm-c05-longitud-geomuxe9trica-de-una-curva}

[]{#activación-una-sola-partición-no-basta}

### 5.12.1. Activación: una sola partición no basta {#fispm-c05-activaciuxf3n-una-sola-particiuxf3n-no-basta}

En §11, una partición temporal

$$\Pi: a=t_0<t_1<\cdots<t_n=b$$

produce una longitud poligonal

$$L_\Pi(P) = \sum_{i=1}^{n} d\bigl(P(t_{i-1}),P(t_i)\bigr).$$

Pero esta cantidad depende de la partición elegida. Una partición gruesa puede ignorar parte del recorrido intermedio. Si añadimos nuevos instantes, el polígono puede seguir más de cerca la curva y revelar una longitud mayor. La pregunta geométrica es, por tanto,

[]{#fig:I-05-N03}

<figure id="fig-fpm-v04-i-05-n03" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-05-N03.svg" class="lightbox" data-gallery="fpm-v04-c05"><img src="/assets/books/fispm/v04/I-05-N03.svg" alt="Camino y desplazamiento. Diagrama del capítulo 5; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="352" height="231" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 5.7.** Una semicircunferencia de radio $R$ tiene longitud $\pi R$. El desplazamiento une sus extremos y tiene norma $2R$; ambas cantidades miden objetos distintos. Véase §[5.12](#fispm-c05-longitud-geomuxe9trica-de-una-curva).

</figcaption>

</figure>

$$\boxed{ \text{¿cómo extraer una longitud de la curva que no dependa de una partición concreta?} }$$

La respuesta no será una fórmula integral. Primero construiremos una definición puramente geométrica a partir de **todas** las longitudes poligonales.

[]{#la-familia-de-todas-las-longitudes-poligonales}

### 5.12.2. La familia de todas las longitudes poligonales {#fispm-c05-la-familia-de-todas-las-longitudes-poligonales}

Sea

$$P:[a,b]\to\mathcal E.$$

Consideremos el conjunto

$$\mathscr L(P;[a,b]) := \left\{ L_\Pi(P): \Pi\text{ partición de }[a,b] \right\}.$$

Cada elemento de $\mathscr L(P;[a,b])$ es un número real no negativo. Por proposición 5.23, toda partición satisface $d(P(a),P(b)) \le L_\Pi(P).$ Así, las aproximaciones poligonales están acotadas inferiormente por la distancia entre los extremos. Lo que todavía no sabemos es si están acotadas superiormente. Puede ocurrir que las longitudes poligonales crezcan sin cota al considerar particiones cada vez más finas. Por eso la definición deberá permitir tanto un valor real finito como la posibilidad de longitud infinita.

[]{#principio-metodológico-definir-longitud-geométricamente-antes-de-integrar}

### 5.12.3. Principio metodológico: definir longitud geométricamente antes de integrar {#fispm-c05-principio-metodoluxf3gico-definir-longitud-geomuxe9tricamente-antes-de-integrar}

**Principio metodológico 5.16 --- Definir longitud geométricamente antes de usar una fórmula integral** La longitud de una curva no se introduce mediante

$$\int_a^b\|v(t)\|\,dt.$$

Primero se define geométricamente a partir de las longitudes poligonales

$$L_\Pi(P).$$

Sólo más adelante, bajo hipótesis de regularidad suficientes, se demostrará que esa definición geométrica coincide con una fórmula integral.

principio metodológico 5.16 fija una prioridad lógica importante:

$$\boxed{ \text{definición geométrica} \longrightarrow \text{teorema integral}, }$$

y no al revés. Esto evita que la integral oculte qué cantidad geométrica está midiendo.

[]{#definir-longitud-geométrica-de-una-curva}

### 5.12.4. Definir: longitud geométrica de una curva {#fispm-c05-definir-longitud-geomuxe9trica-de-una-curva}

**Definición 5.22 --- Longitud geométrica de una curva sobre $[a,b]$** Sea

$$P:[a,b]\to\mathcal E.$$

Definimos la **longitud geométrica** de $P$ sobre $[a,b]$ por

$$\boxed{ L(P;[a,b]) := \sup_{\Pi} L_\Pi(P), }$$

donde el supremo se toma sobre todas las particiones temporales finitas de $[a,b]$. Si el conjunto de longitudes poligonales no está acotado superiormente, escribimos

$$L(P;[a,b])=+\infty.$$

La definición no requiere que $P$ sea derivable. Tampoco depende de una base ni de coordenadas: sólo usa distancias entre puntos del espacio euclídeo afín. Por tanto, definición 5.22 es una definición geométrica primaria.

[]{#qué-significa-el-supremo-en-esta-definición}

### 5.12.5. Qué significa el supremo en esta definición {#fispm-c05-quuxe9-significa-el-supremo-en-esta-definiciuxf3n}

El valor

$$L(P;[a,b]) = \sup_\Pi L_\Pi(P)$$

es el menor número ---si existe finito--- que domina todas las longitudes poligonales. Equivale a exigir:

1.  para toda partición $\Pi$, $$L_\Pi(P) \le L(P;[a,b]);$$

2.  si $M<L(P;[a,b])$, entonces existe alguna partición $\Pi$ tal que $$L_\Pi(P)>M.$$

La longitud geométrica no tiene por qué coincidir con la longitud poligonal de una partición particular. Puede ser aproximada desde abajo por longitudes poligonales cada vez mayores, pero la existencia de una partición que alcance exactamente el supremo no forma parte de la definición.

[]{#fispm-c05-definir-curva-rectificable label="fispm-c05-definir-curva-rectificable"}

**Definición 5.23 --- Curva rectificable** Una curva

$$P:[a,b]\to\mathcal E$$

se llama **rectificable** si

$$\boxed{ L(P;[a,b])<\infty. }$$

Ser rectificable significa, por tanto, que todas las longitudes poligonales de la curva están acotadas superiormente por una constante finita. La definición no afirma todavía que la longitud pueda calcularse mediante una integral ni que la curva sea derivable.

[]{#una-jerarquía-de-cantidades}

### 5.12.6. Una jerarquía de cantidades {#fispm-c05-una-jerarquuxeda-de-cantidades}

En §§11--12 aparecen ahora tres cantidades escalares distintas:

$$d(P(a),P(b)),$$

$$L_\Pi(P),$$

y

$$L(P;[a,b]).$$

La primera depende sólo de los extremos. La segunda depende de una partición concreta. La tercera reúne la información de **todas** las particiones mediante el supremo. Conceptualmente,

$$\boxed{ \text{cuerda} \;\longrightarrow\; \text{polígono asociado a }\Pi \;\longrightarrow\; \text{longitud geométrica}. }$$

Proposición 5.23 ya garantiza, para toda partición, $d(P(a),P(b)) \le L_\Pi(P).$

Más adelante proposición 5.26 hará explícita la consecuencia

$$d(P(a),P(b)) \le L(P;[a,b]).$$

Todavía no la usamos como resultado formal.

[]{#refinar-una-partición-intuición-antes-del-teorema}

### 5.12.7. Refinar una partición: intuición antes del teorema {#fispm-c05-refinar-una-particiuxf3n-intuiciuxf3n-antes-del-teorema}

Supongamos que una partición $\Pi'$ se obtiene de $\Pi$ añadiendo uno o más instantes intermedios. Geométricamente, cada segmento del polígono original se reemplaza por una cadena de segmentos que pasa por más puntos de la curva. La desigualdad triangular sugiere que esa operación no puede disminuir la suma total de longitudes. Es decir, esperamos demostrar

$$L_{\Pi'}(P) \ge L_\Pi(P)$$

cuando $\Pi'$ refina $\Pi$. Éste será proposición 5.25. La monotonía bajo refinamiento explica por qué las aproximaciones poligonales pueden entenderse como aproximaciones **desde abajo** a la longitud geométrica.

[]{#principio-metodológico-las-particiones-aproximan-desde-abajo}

### 5.12.8. Principio metodológico: las particiones aproximan desde abajo {#fispm-c05-principio-metodoluxf3gico-las-particiones-aproximan-desde-abajo}

**Principio metodológico 5.17 --- Las particiones aproximan desde abajo la longitud; refinar no debe acortarlas** Al comparar particiones:

1.  declarar cuál refina a cuál;

2.  comparar localmente un segmento con la cadena de segmentos que lo sustituye;

3.  usar la desigualdad triangular;

4.  concluir que el refinamiento no reduce la longitud poligonal.

No interpretar una partición concreta como si ya fuese la longitud geométrica. La idea central es

$$\boxed{ \Pi'\text{ refina }\Pi \quad\Longrightarrow\quad L_{\Pi'}(P)\ge L_\Pi(P), }$$

pero esta implicación seguirá siendo una **expectativa** hasta demostrar proposición 5.25.

[]{#curvas-rectificables-y-no-rectificables}

### 5.12.9. Curvas rectificables y no rectificables {#fispm-c05-curvas-rectificables-y-no-rectificables}

Definición 5.23 permite dos regímenes. Si existe una cota finita común para todas las longitudes poligonales, entonces $L(P;[a,b])<\infty$

y la curva es rectificable. Si, en cambio, para todo $M>0$ podemos encontrar una partición $\Pi$ con

$$L_\Pi(P)>M,$$

entonces $L(P;[a,b])=+\infty$

y la curva no es rectificable. En este capítulo no necesitamos todavía construir ejemplos patológicos sofisticados. Lo importante es que la definición definición 5.22 admite ambas posibilidades.

[]{#qué-todavía-no-hemos-demostrado-2}

### 5.12.10. Qué todavía no hemos demostrado {#fispm-c05-quuxe9-todavuxeda-no-hemos-demostrado-2}

Quedan tres resultados estructurales:

1.  **proposición 5.25 --- monotonía bajo refinamiento** $$\Pi'\text{ refina }\Pi \Longrightarrow L_{\Pi'}(P)\ge L_\Pi(P);$$

2.  **proposición 5.26 --- la longitud geométrica domina la cuerda** $$L(P;[a,b]) \ge d(P(a),P(b));$$

3.  **proposición 5.27 --- invariancia bajo reparametrización monótona y biyectiva** la longitud geométrica debe depender del recorrido geométrico, no de una parametrización monótona elegida para describirlo. Ninguno de estos resultados requiere todavía la fórmula integral de §13.

[]{#balance-de-la-definición-geométrica}

### 5.12.11. Balance de la definición geométrica {#fispm-c05-balance-de-la-definiciuxf3n-geomuxe9trica}

La arquitectura conceptual queda fijada:

$$\boxed{ \Pi \longmapsto L_\Pi(P) }$$

y después

$$\boxed{ L(P;[a,b]) = \sup_\Pi L_\Pi(P). }$$

Definición 5.22 define la longitud geométrica sin derivadas ni integrales. Definición 5.23 distingue las curvas cuya longitud es finita. principio metodológico 5.16 protege la prioridad de la definición geométrica frente a la futura fórmula integral. principio metodológico 5.17 prepara la idea de que refinamientos sucesivos producen mejores aproximaciones poligonales desde abajo. Las proposiciones siguientes demuestran proposiciones 5.25--5.27 y ejercicios 5.24--5.26 aplican después esas propiedades. La fórmula integral permanece reservada para §13.

[]{#proposición-monotonía-de-la-longitud-poligonal-bajo-refinamiento}

### 5.12.12. Proposición: monotonía de la longitud poligonal bajo refinamiento {#fispm-c05-proposiciuxf3n-monotonuxeda-de-la-longitud-poligonal-bajo-refinamiento}

Recordemos que una partición

$$\Pi': a=s_0<s_1<\cdots<s_m=b$$

**refina** a

$$\Pi: a=t_0<t_1<\cdots<t_n=b$$

si todo punto de $\Pi$ pertenece también a $\Pi'$. La afirmación que debemos demostrar es que añadir puntos intermedios nunca disminuye la suma de distancias.

**Proposición 5.25 --- Monotonía bajo refinamiento** Si $\Pi'$ refina a $\Pi$, entonces

$$\boxed{ L_{\Pi'}(P) \ge L_\Pi(P). }$$

**Demostración.** Comenzamos con el caso elemental en que $\Pi'$ se obtiene de $\Pi$ insertando un único punto

$$\tau\in(t_{k-1},t_k).$$

Todos los términos de la suma poligonal permanecen iguales excepto

$$d\bigl(P(t_{k-1}),P(t_k)\bigr),$$

que en la partición refinada se reemplaza por

$$d\bigl(P(t_{k-1}),P(\tau)\bigr) + d\bigl(P(\tau),P(t_k)\bigr).$$

Por la desigualdad triangular,

$$d\bigl(P(t_{k-1}),P(t_k)\bigr) \le d\bigl(P(t_{k-1}),P(\tau)\bigr) + d\bigl(P(\tau),P(t_k)\bigr).$$

Por tanto, $L_{\Pi'}(P) \ge L_\Pi(P).$ Si $\Pi'$ contiene varios puntos nuevos, podemos obtenerla a partir de $\Pi$ mediante una sucesión finita de inserciones de un solo punto. Aplicando el argumento anterior en cada paso,

$$L_{\Pi}(P) \le L_{\Pi_1}(P) \le \cdots \le L_{\Pi'}(P).$$

Luego

$$\boxed{ L_{\Pi'}(P) \ge L_\Pi(P). }$$

$\square$ proposición 5.25 justifica rigurosamente la lectura de principio metodológico 5.17: un refinamiento puede mantener o aumentar la longitud poligonal, pero nunca acortarla.

[]{#proposición-la-longitud-geométrica-domina-la-cuerda}

### 5.12.13. Proposición: la longitud geométrica domina la cuerda {#fispm-c05-proposiciuxf3n-la-longitud-geomuxe9trica-domina-la-cuerda}

Proposición 5.23 ya estableció que, para toda partición $\Pi$, $d(P(a),P(b)) \le L_\Pi(P).$

Como la longitud geométrica es el supremo de todas las longitudes poligonales, la misma cota inferior debe valer también para el supremo.

**Proposición 5.26 --- La longitud geométrica domina la cuerda** Para toda curva

$$P:[a,b]\to\mathcal E,$$

se tiene

$$\boxed{ L(P;[a,b]) \ge d(P(a),P(b)). }$$

**Demostración.** Por proposición 5.23, para toda partición $\Pi$,

$$d(P(a),P(b)) \le L_\Pi(P).$$

Por definición 5.22, $L(P;[a,b]) = \sup_\Pi L_\Pi(P).$

Todo elemento $L_\Pi(P)$ es menor o igual que ese supremo: $L_\Pi(P) \le L(P;[a,b]).$ Por transitividad, $d(P(a),P(b)) \le L(P;[a,b]).$ Por tanto,

$$\boxed{ L(P;[a,b]) \ge d(P(a),P(b)). }$$

$\square$ La desigualdad sigue siendo válida cuando

$$L(P;[a,b])=+\infty.$$

Proposición 5.26 expresa que ninguna curva que une dos puntos puede tener longitud geométrica menor que la distancia euclídea entre ellos.

[]{#proposición-invariancia-bajo-reparametrización-monótona}

### 5.12.14. Proposición: invariancia bajo reparametrización monótona {#fispm-c05-proposiciuxf3n-invariancia-bajo-reparametrizaciuxf3n-monuxf3tona}

Sea

$$P:[a,b]\to\mathcal E$$

y sea

$$\phi:[c,d]\to[a,b]$$

una biyección estrictamente monótona. Definimos $Q:=P\circ\phi:[c,d]\to\mathcal E.$ Queremos demostrar que $P$ y $Q$ tienen la misma longitud geométrica. La idea no usa derivadas. Basta comprobar que cada partición de un intervalo produce una partición correspondiente del otro con exactamente la misma suma poligonal.

**Proposición 5.27 --- Invariancia de la longitud geométrica bajo reparametrización estrictamente monótona y biyectiva** Sea

$$P:[a,b]\to\mathcal E,$$

y sea

$$\phi:[c,d]\to[a,b]$$

una biyección estrictamente monótona. Si

$$Q=P\circ\phi,$$

entonces

$$\boxed{ L(Q;[c,d]) = L(P;[a,b]). }$$

**Demostración.** Distinguimos dos casos.

[]{#caso-1-phi-es-estrictamente-creciente}

#### 5.12.14.1. Caso 1: $\phi$ es estrictamente creciente {#fispm-c05-caso-1-phi-es-estrictamente-creciente}

Como $\phi$ es biyectiva entre los intervalos compactos, $\phi(c)=a, \qquad \phi(d)=b.$

Sea

$$\Sigma: c=u_0<u_1<\cdots<u_n=d$$

una partición de $[c,d]$. Como $\phi$ es estrictamente creciente,

$$a = \phi(u_0) < \phi(u_1) < \cdots < \phi(u_n) = b.$$

Por tanto, $\Phi(\Sigma) := \{\phi(u_0),\ldots,\phi(u_n)\}$

es una partición de $[a,b]$. Además,

$$\begin{aligned} L_\Sigma(Q) &= \sum_{i=1}^{n} d\bigl(Q(u_{i-1}),Q(u_i)\bigr)\\ &= \sum_{i=1}^{n} d\bigl(P(\phi(u_{i-1})),P(\phi(u_i))\bigr)\\ &= L_{\Phi(\Sigma)}(P). \end{aligned}$$

Como $\phi^{-1}$ también es estrictamente creciente, toda partición de $[a,b]$ se obtiene de manera única a partir de una partición de $[c,d]$ mediante este procedimiento. Por tanto, los conjuntos de longitudes poligonales coinciden:

$$\left\{ L_\Sigma(Q): \Sigma\text{ partición de }[c,d] \right\} = \left\{ L_\Pi(P): \Pi\text{ partición de }[a,b] \right\}.$$

[]{#caso-2-phi-es-estrictamente-decreciente}

#### 5.12.14.2. Caso 2: $\phi$ es estrictamente decreciente {#fispm-c05-caso-2-phi-es-estrictamente-decreciente}

Ahora

$$\phi(c)=b, \qquad \phi(d)=a.$$

Sea de nuevo

$$\Sigma: c=u_0<u_1<\cdots<u_n=d.$$

Entonces

$$b = \phi(u_0) > \phi(u_1) > \cdots > \phi(u_n) = a.$$

Para obtener una partición ordenada de $[a,b]$, invertimos el orden:

$$\Phi(\Sigma): a = \phi(u_n) < \phi(u_{n-1}) < \cdots < \phi(u_0) = b.$$

La longitud poligonal correspondiente es

$$L_{\Phi(\Sigma)}(P) = \sum_{i=1}^{n} d\bigl(P(\phi(u_i)),P(\phi(u_{i-1}))\bigr).$$

Por simetría de la distancia,

$$d\bigl(P(\phi(u_i)),P(\phi(u_{i-1}))\bigr) = d\bigl(P(\phi(u_{i-1})),P(\phi(u_i))\bigr).$$

Luego

$$L_{\Phi(\Sigma)}(P) = L_\Sigma(Q).$$

La inversa $\phi^{-1}$ es también estrictamente decreciente, de modo que nuevamente obtenemos una correspondencia biyectiva entre las particiones de ambos intervalos que conserva exactamente las longitudes poligonales. En ambos casos, los conjuntos de longitudes poligonales de $P$ y $Q$ son iguales. Sus supremos, por tanto, son iguales:

$$\boxed{ L(Q;[c,d]) = L(P;[a,b]). }$$

$\square$ proposición 5.27 muestra que la longitud geométrica es independiente de una reparametrización monótona y biyectiva: cambiar el «reloj» de la curva, incluso invirtiendo el sentido de recorrido, no cambia su longitud geométrica.

[]{#balance-de-las-propiedades-estructurales}

### 5.12.15. Balance de las propiedades estructurales {#fispm-c05-balance-de-las-propiedades-estructurales}

Quedan ahora demostradas tres propiedades estructurales:

$$\boxed{ \Pi'\text{ refina }\Pi \Longrightarrow L_{\Pi'}(P)\ge L_\Pi(P), }$$

$$\boxed{ L(P;[a,b]) \ge d(P(a),P(b)), }$$

y

$$\boxed{ L(P\circ\phi;[c,d]) = L(P;[a,b]) }$$

para toda biyección estrictamente monótona

$$\phi:[c,d]\to[a,b].$$

Proposición 5.25 formaliza la aproximación desde abajo por refinamientos. Proposición 5.26 relaciona la longitud geométrica con la cuerda entre los extremos. Proposición 5.27 establece que la longitud geométrica no depende de la parametrización monótona elegida para recorrer la misma curva. Ninguna de estas pruebas usa derivadas ni integrales. Ejercicios 5.24--5.26 aplicarán estas propiedades antes del cierre local de §12. La fórmula integral y el parámetro natural siguen reservados para §13.

### 5.12.15. Refinar una partición {#fispm-c05-e024-refinar-una-particiuxf3n .unnumbered}

**Ejercicio 5.24 · Prueba** Sea $B=(e_1,e_2,e_3)$ una base ortonormal de $V$ y sea $A\in\mathcal E$. Considera una curva $P:[0,2]\to\mathcal E$ tal que

$$P(0)=A,$$

$$P(1)=A+3e_1,$$

y

$$P(2)=A+3e_1+4e_2.$$

Compara las particiones

$$\Pi=\{0,2\}, \qquad \Pi'=\{0,1,2\}.$$

1.  Calcula $L_\Pi(P)$.

2.  Calcula $L_{\Pi'}(P)$.

3.  Verifica directamente proposición 5.25.

4.  Identifica en qué paso aparece la desigualdad triangular.

**Solución desarrollada** Para la partición gruesa,

$$L_\Pi(P) = d(P(0),P(2)).$$

Como $\overrightarrow{P(0)P(2)} = 3e_1+4e_2,$

y la base es ortonormal,

$$\boxed{ L_\Pi(P) = \sqrt{3^2+4^2} = 5. }$$

Para la partición refinada, $L_{\Pi'}(P) = d(P(0),P(1)) + d(P(1),P(2)).$

Como $d(P(0),P(1))=3$

y

$$d(P(1),P(2))=4,$$

obtenemos

$$\boxed{ L_{\Pi'}(P)=3+4=7. }$$

Así,

$$\boxed{ L_{\Pi'}(P)=7\ge5=L_\Pi(P), }$$

lo que verifica proposición 5.25. La desigualdad triangular aparece precisamente al comparar el segmento directo entre $P(0)$ y $P(2)$ con la cadena que pasa por $P(1)$: $d(P(0),P(2)) \le d(P(0),P(1)) + d(P(1),P(2)).$

### 5.12.15. Cuerda y longitud geométrica {#fispm-c05-e025-cuerda-y-longitud-geomuxe9trica .unnumbered}

**Ejercicio 5.25 · Transferencia y desigualdad** Conserva los mismos puntos del ejercicio 5.24 y supón ahora que la curva completa es el recorrido quebrado

$$P(t)= \begin{cases} A+3t\,e_1, & 0\le t\le1,\\[4pt] A+3e_1+4(t-1)e_2, & 1\le t\le2. \end{cases}$$

1.  Calcula la distancia entre los extremos.

2.  Usa la partición $\{0,1,2\}$ para obtener una cota inferior de $L(P;[0,2])$.

3.  Demuestra que, para cualquier partición $\Pi$ de $[0,2]$, $$L_\Pi(P)\le7.$$

4.  Concluye el valor exacto de $L(P;[0,2])$.

5.  Compara la cuerda con la longitud geométrica.

**Solución desarrollada** Los extremos son

$$P(0)=A, \qquad P(2)=A+3e_1+4e_2.$$

Por tanto,

$$d(P(0),P(2)) = \sqrt{3^2+4^2} = \boxed{5}.$$

Para

$$\Pi_0=\{0,1,2\},$$

Ejercicio 5.24 dio

$$L_{\Pi_0}(P)=7.$$

Como la longitud geométrica es el supremo de todas las longitudes poligonales, $L(P;[0,2])\ge7.$

Falta demostrar la cota superior.

Sea $\Pi$ una partición arbitraria. Añadamos, si es necesario, el instante $1$ y obtengamos un refinamiento $\Pi'$. Por proposición 5.25, $L_\Pi(P)\le L_{\Pi'}(P).$ En el intervalo $[0,1]$, todos los puntos de la curva están sobre el mismo segmento y en el mismo orden. Por tanto, las distancias sucesivas telescopan escalarmente y su suma es exactamente

$$d(P(0),P(1))=3.$$

Del mismo modo, en $[1,2]$ la suma de las distancias sucesivas es exactamente

$$d(P(1),P(2))=4.$$

Luego

$$L_{\Pi'}(P)=3+4=7.$$

Así, $L_\Pi(P)\le7$

para toda partición $\Pi$.

Como ya existe una partición con longitud poligonal igual a $7$,

$$\boxed{ L(P;[0,2])=7. }$$

Finalmente,

$$\boxed{ d(P(0),P(2))=5<7=L(P;[0,2]). }$$

La cuerda mide la distancia directa entre los extremos; la longitud geométrica mide el recorrido completo de la curva.

### 5.12.15. Longitud bajo una reparametrización monótona no lineal {#fispm-c05-e026-longitud-bajo-una-reparametrizaciuxf3n-monuxf3tona-no-lineal .unnumbered}

**Ejercicio 5.26 · Invariancia y prueba** Sean $A\in\mathcal E$ y $d\in V$, con $d\ne0$. Considera

$$P:[0,1]\to\mathcal E, \qquad P(t)=A+t\,d,$$

y la biyección estrictamente creciente

$$\phi:[0,1]\to[0,1], \qquad \phi(u)=u^2.$$

Define

$$Q=P\circ\phi, \qquad Q(u)=A+u^2d.$$

1.  Sea $$\Sigma: 0=u_0<u_1<\cdots<u_n=1$$ una partición de $[0,1]$. Construye la partición correspondiente de $P$.

2.  Verifica que $$L_\Sigma(Q) = L_{\Phi(\Sigma)}(P).$$

3.  Comprueba directamente que ambas longitudes poligonales valen $\|d\|$.

4.  Concluye que $$L(Q;[0,1]) = L(P;[0,1]) = \|d\|.$$

5.  Explica por qué este ejercicio no necesita derivar $\phi$.

**Solución desarrollada** Como $\phi(u)=u^2$ es estrictamente creciente y biyectiva en $[0,1]$, la imagen de la partición

$$\Sigma: 0=u_0<u_1<\cdots<u_n=1$$

es $\Phi(\Sigma): 0=u_0^2<u_1^2<\cdots<u_n^2=1.$

Ésta es una partición de $[0,1]$.

Además, $Q(u_i) = P(u_i^2).$ Por tanto,

$$\begin{aligned} L_\Sigma(Q) &= \sum_{i=1}^{n} d\bigl(Q(u_{i-1}),Q(u_i)\bigr)\\ &= \sum_{i=1}^{n} d\bigl(P(u_{i-1}^2),P(u_i^2)\bigr)\\ &= L_{\Phi(\Sigma)}(P). \end{aligned}$$

Como $P(t)=A+td,$

para $0\le s<t\le1$, $d(P(s),P(t)) = \|(t-s)d\| = (t-s)\|d\|.$

Luego

$$\begin{aligned} L_{\Phi(\Sigma)}(P) &= \sum_{i=1}^{n} (u_i^2-u_{i-1}^2)\|d\|\\ &= (1-0)\|d\|\\ &= \|d\|. \end{aligned}$$

En consecuencia, $L_\Sigma(Q)=\|d\|$

para toda partición $\Sigma$. Por definición 5.22,

$$\boxed{ L(Q;[0,1]) = L(P;[0,1]) = \|d\|. }$$

No fue necesario calcular $\phi'(u)$. Proposición 5.27 es un resultado geométrico sobre correspondencia de particiones, no una consecuencia de la fórmula integral de longitud de arco.

[]{#cierre-conceptual-longitud-antes-que-integral}

### 5.12.16. Cierre conceptual: longitud antes que integral {#fispm-c05-cierre-conceptual-longitud-antes-que-integral}

§12 ha construido la longitud de una curva sin usar derivadas ni integrales. La secuencia lógica completa es

$$\boxed{ \Pi \longmapsto L_\Pi(P) \longmapsto \sup_\Pi L_\Pi(P) = L(P;[a,b]). }$$

Proposición 5.25 garantiza que refinar una partición no acorta la aproximación poligonal. Proposición 5.26 establece

$$d(P(a),P(b)) \le L(P;[a,b]).$$

Proposición 5.27 muestra que la longitud geométrica es invariante bajo reparametrizaciones estrictamente monótonas y biyectivas. Ejercicio 5.24 verificó el crecimiento bajo refinamiento. Ejercicio 5.25 distinguió con un ejemplo exacto una cuerda de longitud $5$ y un recorrido geométrico de longitud $7$. Ejercicio 5.26 comprobó la invariancia bajo la reparametrización no lineal $u\mapsto u^2$ sin derivadas. La sección queda cerrada con una definición puramente geométrica de longitud. Sólo en §13 demostraremos, bajo hipótesis de regularidad suficientes, que esta cantidad coincide con una integral de la rapidez.

[]{#fórmula-de-longitud-de-arco-y-parámetro-natural}

[]{#fispm-t1-c05-s13}

[]{#fpm-i-05-s13}

## 5.13. Fórmula de longitud de arco y parámetro natural {#fispm-c05-fuxf3rmula-de-longitud-de-arco-y-paruxe1metro-natural}

[]{#activación-de-una-definición-geométrica-a-una-fórmula-de-cálculo}

### 5.13.1. Activación: de una definición geométrica a una fórmula de cálculo {#fispm-c05-activaciuxf3n-de-una-definiciuxf3n-geomuxe9trica-a-una-fuxf3rmula-de-cuxe1lculo}

En §12 definimos la longitud geométrica mediante $L(P;[a,b]) = \sup_{\Pi}L_\Pi(P),$

sin usar derivadas ni integrales. Ahora suponemos que, para un origen fijo $O$, $r_O:[a,b]\to V$

es de clase $C^1$. En un intervalo cerrado usamos la misma convención de §9: las derivadas en los extremos son laterales y $C^1$ significa que la derivada interior se extiende continuamente hasta los extremos mediante esas derivadas laterales. Por proposición 5.9, $v(t)=r_O'(t).$

[]{#fig:I-05-R04}

<figure id="fig-fpm-v04-i-05-r04" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-05-R04.svg" class="lightbox" data-gallery="fpm-v04-c05"><img src="/assets/books/fispm/v04/I-05-R04.svg" alt="Longitud como límite de cuerdas. Diagrama del capítulo 5; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="343" height="283" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 5.8.** Las cuerdas de una partición aproximan la longitud de una curva regular. El límite es $\int\lVert r^\prime(u)\rVert\,du$; la norma se integra antes de confundirla con el desplazamiento entre extremos. Véase §[5.13](#fispm-c05-fuxf3rmula-de-longitud-de-arco-y-paruxe1metro-natural).

</figcaption>

</figure>

Como $v$ es continua, la rapidez

$$\sigma(t)=\|v(t)\|$$

también es continua y, por tanto, integrable en $[a,b]$. La pregunta de esta sección es si la cantidad analítica

$$\int_a^b\|v(t)\|\,dt$$

coincide con la longitud geométrica ya definida.

[]{#la-hipótesis-c1-no-depende-del-origen-fijo}

### 5.13.2. La hipótesis $C^1$ no depende del origen fijo {#fispm-c05-la-hipuxf3tesis-c1-no-depende-del-origen-fijo}

Sean $O$ y $O'$ dos orígenes fijos y sea

$$c=\overrightarrow{OO'}.$$

Por proposición 5.2, $r_{O'}(t)=r_O(t)-c.$

Como $c$ es constante, $r_{O'}'(t)=r_O'(t).$ Por tanto, $r_O$ es $C^1$ si y sólo si $r_{O'}$ es $C^1$. La hipótesis de la proposición 5.28 es, pues, geométricamente bien definida aunque usemos un origen auxiliar para representar la curva en $V$.[^8]

[]{#principio-metodológico-la-fórmula-integral-es-un-teorema}

### 5.13.3. Principio metodológico: la fórmula integral es un teorema {#fispm-c05-principio-metodoluxf3gico-la-fuxf3rmula-integral-es-un-teorema}

**Principio metodológico 5.18 --- La fórmula $\int\|v\|$ es un teorema, no la definición primaria de longitud** La igualdad

$$L(P;[a,b]) = \int_a^b\|v(t)\|\,dt$$

debe demostrarse a partir de la definición 5.22. La prueba deberá establecer por separado: $L(P;[a,b]) \le \int_a^b\|v(t)\|\,dt,$

y

$$\int_a^b\|v(t)\|\,dt \le L(P;[a,b]).$$

Ninguna de estas desigualdades puede suponerse por interpretación física o por una fórmula memorizada. Esta doble estimación será la estructura completa de la proposición 5.28.

[]{#paso-técnico-interno-norma-de-una-integral-vectorial}

### 5.13.4. Paso técnico interno: norma de una integral vectorial {#fispm-c05-paso-tuxe9cnico-interno-norma-de-una-integral-vectorial}

Necesitaremos una desigualdad elemental para funciones continuas

$$w:[\alpha,\beta]\to V.$$

La integral vectorial se entiende componente a componente en una base fija. Esta construcción no depende de la base elegida. En efecto, si $B$ y $B'$ son bases fijas y

$$[w(t)]_B=S[w(t)]_{B'},$$

con $S$ constante, la linealidad de la integral escalar da

$$\int_\alpha^\beta [w(t)]_B\,dt = S\int_\alpha^\beta [w(t)]_{B'}\,dt.$$

Las dos integraciones componente a componente satisfacen exactamente la ley de cambio de componentes del mismo vector de $V$; por tanto, definen una integral vectorial intrínseca. Afirmamos que

$$\boxed{ \left\| \int_\alpha^\beta w(t)\,dt \right\| \le \int_\alpha^\beta\|w(t)\|\,dt. }$$

No asignamos un ID formal a este resultado: es un paso técnico interno de la proposición 5.28.

**Demostración.** Sea

$$z = \int_\alpha^\beta w(t)\,dt.$$

Si $z=0$, la desigualdad es inmediata. Supongamos $z\ne0$ y definamos

$$e=\frac{z}{\|z\|}.$$

Entonces $\|e\|=1$ y

$$\|z\| = \langle e,z\rangle.$$

Por linealidad de la integral componente a componente,

$$\langle e,z\rangle = \int_\alpha^\beta \langle e,w(t)\rangle\,dt.$$

Por Cauchy--Schwarz,

$$\langle e,w(t)\rangle \le |\langle e,w(t)\rangle| \le \|e\|\,\|w(t)\| = \|w(t)\|.$$

Integrando, $\|z\| \le \int_\alpha^\beta\|w(t)\|\,dt.$

Así,

$$\boxed{ \left\| \int_\alpha^\beta w(t)\,dt \right\| \le \int_\alpha^\beta\|w(t)\|\,dt. }$$

[]{#primera-desigualdad-la-longitud-geométrica-no-supera-la-integral-de-la-rapidez}

### 5.13.5. Primera desigualdad: la longitud geométrica no supera la integral de la rapidez {#fispm-c05-primera-desigualdad-la-longitud-geomuxe9trica-no-supera-la-integral-de-la-rapidez}

Sea

$$\Pi: a=t_0<t_1<\cdots<t_n=b$$

una partición arbitraria. Por el teorema fundamental del cálculo aplicado componente a componente,

$$r_O(t_i)-r_O(t_{i-1}) = \int_{t_{i-1}}^{t_i}v(t)\,dt.$$

Por tanto,

$$d(P(t_{i-1}),P(t_i)) = \left\| \int_{t_{i-1}}^{t_i}v(t)\,dt \right\|.$$

Usando la desigualdad del paso anterior,

$$d(P(t_{i-1}),P(t_i)) \le \int_{t_{i-1}}^{t_i}\|v(t)\|\,dt.$$

Sumando sobre todos los subintervalos,

$$L_\Pi(P) \le \sum_{i=1}^{n} \int_{t_{i-1}}^{t_i}\|v(t)\|\,dt = \int_a^b\|v(t)\|\,dt.$$

Como esta desigualdad vale para toda partición, $\sup_\Pi L_\Pi(P) \le \int_a^b\|v(t)\|\,dt.$ Por definición 5.22,

$$\boxed{ L(P;[a,b]) \le \int_a^b\|v(t)\|\,dt. }$$

En particular, la integral es finita y la curva resulta rectificable.

[]{#preparación-de-la-desigualdad-inversa-continuidad-uniforme-de-v}

### 5.13.6. Preparación de la desigualdad inversa: continuidad uniforme de $v$ {#fispm-c05-preparaciuxf3n-de-la-desigualdad-inversa-continuidad-uniforme-de-v}

Falta demostrar que la longitud geométrica no es menor que la integral. Como $v$ es continua en el intervalo compacto $[a,b]$, es uniformemente continua. Si $a=b$, ambas cantidades son cero y no hay nada que demostrar. Supongamos $a<b.$

Sea

$$\varepsilon>0.$$

Definimos $\eta = \frac{\varepsilon}{2(b-a)}.$ Por continuidad uniforme de $v$, existe

$$\delta>0$$

tal que

$$|s-t|<\delta \Longrightarrow \|v(s)-v(t)\|<\eta.$$

Elegimos una partición

$$\Pi: a=t_0<t_1<\cdots<t_n=b$$

cuya malla satisfaga

$$\max_i(t_i-t_{i-1})<\delta.$$

En cada subintervalo elegimos un punto

$$\tau_i\in[t_{i-1},t_i].$$

Escribimos

$$h_i=t_i-t_{i-1}.$$

Entonces, para todo $t\in[t_{i-1},t_i]$,

$$\|v(t)-v(\tau_i)\|<\eta.$$

[]{#paso-técnico-interno-comparar-incremento-e-integral-local-de-la-rapidez}

### 5.13.7. Paso técnico interno: comparar incremento e integral local de la rapidez {#fispm-c05-paso-tuxe9cnico-interno-comparar-incremento-e-integral-local-de-la-rapidez}

Por el teorema fundamental del cálculo,

$$r_O(t_i)-r_O(t_{i-1}) = \int_{t_{i-1}}^{t_i}v(t)\,dt.$$

Separamos el valor constante $v(\tau_i)$:

$$\int_{t_{i-1}}^{t_i}v(t)\,dt = h_i v(\tau_i) + \int_{t_{i-1}}^{t_i} \bigl(v(t)-v(\tau_i)\bigr)\,dt.$$

Por la desigualdad triangular inversa,

$$\begin{aligned} d(P(t_{i-1}),P(t_i)) &= \left\| h_i v(\tau_i) + \int_{t_{i-1}}^{t_i} (v(t)-v(\tau_i))\,dt \right\|\\ &\ge h_i\|v(\tau_i)\| - \left\| \int_{t_{i-1}}^{t_i} (v(t)-v(\tau_i))\,dt \right\|. \end{aligned}$$

Aplicando la desigualdad de §13.4 al término de error,

$$\left\| \int_{t_{i-1}}^{t_i} (v(t)-v(\tau_i))\,dt \right\| \le \int_{t_{i-1}}^{t_i} \|v(t)-v(\tau_i)\|\,dt < \eta h_i.$$

Así,

$$d(P(t_{i-1}),P(t_i)) \ge h_i\|v(\tau_i)\|-\eta h_i.$$

Por otro lado,

$$\|v(t)\| \le \|v(\tau_i)\| + \|v(t)-v(\tau_i)\| < \|v(\tau_i)\|+\eta.$$

Integrando,

$$\int_{t_{i-1}}^{t_i}\|v(t)\|\,dt \le h_i\|v(\tau_i)\|+\eta h_i.$$

Combinando ambas estimaciones,

$$\boxed{ \int_{t_{i-1}}^{t_i}\|v(t)\|\,dt \le d(P(t_{i-1}),P(t_i)) + 2\eta h_i. }$$

Éste es el segundo paso técnico interno requerido para proposición 5.28.

[]{#segunda-desigualdad-la-integral-de-la-rapidez-no-supera-la-longitud-geométrica}

### 5.13.8. Segunda desigualdad: la integral de la rapidez no supera la longitud geométrica {#fispm-c05-segunda-desigualdad-la-integral-de-la-rapidez-no-supera-la-longitud-geomuxe9trica}

Sumamos la desigualdad anterior sobre todos los subintervalos:

$$\int_a^b\|v(t)\|\,dt \le L_\Pi(P) + 2\eta \sum_{i=1}^{n}h_i.$$

Como $\sum_{i=1}^{n}h_i=b-a,$

obtenemos $\int_a^b\|v(t)\|\,dt \le L_\Pi(P) + 2\eta(b-a).$ Por la elección de $\eta$, $2\eta(b-a)=\varepsilon.$ Luego

$$\int_a^b\|v(t)\|\,dt \le L_\Pi(P)+\varepsilon.$$

Y, como $L_\Pi(P)\le L(P;[a,b]),$

resulta $\int_a^b\|v(t)\|\,dt \le L(P;[a,b])+\varepsilon.$ Esta desigualdad vale para todo $\varepsilon>0$. Por tanto,

$$\boxed{ \int_a^b\|v(t)\|\,dt \le L(P;[a,b]). }$$

[]{#proposición-fórmula-de-longitud-de-arco-para-curvas-c1}

### 5.13.9. Proposición: fórmula de longitud de arco para curvas $C^1$ {#fispm-c05-proposiciuxf3n-fuxf3rmula-de-longitud-de-arco-para-curvas-c1}

**Proposición 5.28 --- Fórmula de longitud de arco para curvas $C^1$** Sea

$$P:[a,b]\to\mathcal E.$$

Supongamos que, para un origen fijo $O$, la curva vectorial

$$r_O:[a,b]\to V$$

es de clase $C^1$. Entonces $P$ es rectificable y

$$\boxed{ L(P;[a,b]) = \int_a^b\|v(t)\|\,dt. }$$

La hipótesis $C^1$ es independiente de la elección del origen fijo.

**Demostración.** En §13.5 demostramos

$$L(P;[a,b]) \le \int_a^b\|v(t)\|\,dt.$$

En §13.8 demostramos

$$\int_a^b\|v(t)\|\,dt \le L(P;[a,b]).$$

Por antisimetría del orden real,

$$\boxed{ L(P;[a,b]) = \int_a^b\|v(t)\|\,dt. }$$

Como la rapidez es continua en el compacto $[a,b]$, la integral es finita. Por definición 5.23, $P$ es rectificable. $\square$

### 5.13.10. Qué proposición 5.28 permite afirmar ---y qué todavía no {#fispm-c05-quuxe9-p28-permite-afirmar-y-quuxe9-todavuxeda-no}

Proposición 5.28 cierra el puente entre la definición geométrica de §12 y el cálculo de una variable:

$$\boxed{ \sup_{\Pi}L_\Pi(P) = \int_a^b\|v(t)\|\,dt }$$

para curvas $C^1$. La integral aparece ahora como **fórmula demostrada** para una cantidad ya definida geométricamente. Todavía no definimos $s(t) = \int_a^t\|v(\tau)\|\,d\tau.$ Ese objeto recibirá el nombre de longitud de arco acumulada sólo en la definición 5.24, después de la proposición 5.28, tal como exige el orden canónico. Tampoco introducimos todavía parametrización por longitud de arco ni velocidad unitaria.

[]{#balance-de-la-fórmula-de-longitud}

### 5.13.11. Balance de la fórmula de longitud {#fispm-c05-balance-de-la-fuxf3rmula-de-longitud}

La construcción respeta el orden

$$\boxed{ \text{definición 5.22} \longrightarrow \text{proposición 5.28} }$$

antes de cualquier definición de parámetro natural. La prueba de la proposición 5.28 contiene exactamente los dos controles internos exigidos por la arquitectura:

1.  la desigualdad $$\left\|\int w\right\| \le \int\|w\|;$$

2.  la estimación inversa obtenida por continuidad uniforme de $v$.

No se han creado IDs adicionales para estos pasos técnicos. A continuación se introducen, en este orden, `definición 5.24 → definición 5.25 → proposición 5.29`; ejercicios 5.27--5.29 aplican después estos resultados. La síntesis transversal pertenece a §14.

[]{#definir-función-longitud-de-arco-acumulada}

### 5.13.12. Definir: función longitud de arco acumulada {#fispm-c05-definir-funciuxf3n-longitud-de-arco-acumulada}

Proposición 5.28 permite ahora interpretar integralmente una longitud que ya fue definida geométricamente.

**Definición 5.24 --- Función longitud de arco acumulada** Sea

$$P:[a,b]\to\mathcal E$$

una curva de clase $C^1$. Definimos su **función longitud de arco acumulada desde $a$** por

$$\boxed{ s(t) := \int_a^t\|v(\tau)\|\,d\tau, \qquad t\in[a,b]. }$$

Por proposición 5.28 aplicado a la restricción de $P$ al intervalo $[a,t]$,

$$\boxed{ s(t) = L(P;[a,t]). }$$

Así, $s(t)$ no es sólo una integral auxiliar: mide exactamente la longitud geométrica recorrida desde el extremo inicial $a$ hasta el instante $t$. En particular, $s(a)=0$

y

$$s(b)=L(P;[a,b]).$$

[]{#propiedades-inmediatas-de-la-función-s}

### 5.13.13. Propiedades inmediatas de la función $s$ {#fispm-c05-propiedades-inmediatas-de-la-funciuxf3n-s}

Como la rapidez es continua, $s(t) = \int_a^t\|v(\tau)\|\,d\tau$

es de clase $C^1$. Por el teorema fundamental del cálculo,

$$\boxed{ s'(t) = \|v(t)\|. }$$

Como la rapidez es no negativa, $s'(t)\ge0.$ Por tanto, $s$ es no decreciente. Si además

$$v(t)\ne0$$

para todo $t\in[a,b]$, entonces

$$\|v(t)\|>0$$

y, por tanto, $s'(t)>0.$ En ese caso, $s$ es estrictamente creciente.

[]{#definir-parametrización-por-longitud-de-arco}

### 5.13.14. Definir: parametrización por longitud de arco {#fispm-c05-definir-parametrizaciuxf3n-por-longitud-de-arco}

**Definición 5.25 --- Parametrización por longitud de arco / velocidad unitaria** Una parametrización derivable

$$\widehat P:J\to\mathcal E$$

se llama una **parametrización por longitud de arco** o **parametrización de velocidad unitaria** si

$$\boxed{ \|\widehat v(\ell)\|=1 }$$

en todo punto del dominio donde esté definida su derivada. El parámetro $\ell$ tiene entonces significado geométrico de longitud acumulada. La condición $\|\widehat v(\ell)\|=1$

no significa que el vector velocidad sea constante. Sólo fija su norma. La dirección puede variar a lo largo de la curva.

[]{#fispm-c05-principio-metodoluxf3gico-declarar-regularidad-e-invertibilidad-antes-de-usar-paruxe1metro-natural label="fispm-c05-principio-metodoluxf3gico-declarar-regularidad-e-invertibilidad-antes-de-usar-paruxe1metro-natural"}

**Principio metodológico 5.19 --- Declarar regularidad e invertibilidad antes de usar parámetro natural** Antes de construir una parametrización por longitud de arco:

1.  comprobar que la curva es $C^1$;

2.  verificar $$v(t)\ne0$$ en todo el intervalo;

3.  concluir $$s'(t)=\|v(t)\|>0;$$

4.  justificar que $s$ es estrictamente creciente;

5.  invocar explícitamente el teorema inverso unidimensional para obtener $s^{-1}$;

6.  sólo entonces definir la curva reparametrizada por longitud de arco.

No escribir $t=t(s)$ ni usar $$\frac{dt}{ds}$$ antes de justificar la invertibilidad de $s$.

principio metodológico 5.19 evita que la construcción del parámetro natural oculte su hipótesis decisiva: la ausencia de instantes de reposo.

### 5.13.15. Preparación de la proposición 5.29: invertir la longitud acumulada {#fispm-c05-preparaciuxf3n-de-p29-invertir-la-longitud-acumulada}

Supongamos desde ahora que

$$v(t)\ne0$$

para todo

$$t\in[a,b].$$

Entonces $s'(t)=\|v(t)\|>0.$ Por tanto, $s$ es estrictamente creciente y lleva biyectivamente

$$[a,b]$$

sobre

$$[0,L],$$

donde

$$L:=L(P;[a,b])=s(b).$$

Así, $s:[a,b]\to[0,L]$

posee una inversa

$$s^{-1}:[0,L]\to[a,b].$$

Por el teorema inverso unidimensional importado de M3, esta inversa es $C^1$ en el nivel requerido y satisface, en puntos interiores,

$$\boxed{ \frac{d}{d\ell}s^{-1}(\ell) = \frac{1}{ s'\bigl(s^{-1}(\ell)\bigr) }. }$$

Como $s'(t)=\|v(t)\|,$

obtenemos

$$\boxed{ \frac{d}{d\ell}s^{-1}(\ell) = \frac{1}{ \|v(s^{-1}(\ell))\| }. }$$

[]{#construir-la-curva-parametrizada-por-longitud-de-arco}

### 5.13.16. Construir la curva parametrizada por longitud de arco {#fispm-c05-construir-la-curva-parametrizada-por-longitud-de-arco}

Definimos $\widehat P:[0,L]\to\mathcal E$

por

$$\boxed{ \widehat P(\ell) = P\bigl(s^{-1}(\ell)\bigr). }$$

Esta curva tiene la misma trayectoria geométrica que $P$ porque $s^{-1}$ es biyectiva. Además, proposición 5.18 da la transformación de la velocidad:

$$\widehat v(\ell) = v\bigl(s^{-1}(\ell)\bigr) \frac{d}{d\ell}s^{-1}(\ell).$$

Sustituyendo la derivada de la inversa,

$$\widehat v(\ell) = \frac{ v\bigl(s^{-1}(\ell)\bigr) }{ \|v(s^{-1}(\ell))\| }.$$

Por tanto,

$$\boxed{ \|\widehat v(\ell)\| = 1. }$$

La nueva parametrización conserva la dirección orientada de la velocidad y normaliza su magnitud.

[]{#fispm-c05-proposiciuxf3n-paruxe1metro-de-arco-y-velocidad-unitaria label="fispm-c05-proposiciuxf3n-paruxe1metro-de-arco-y-velocidad-unitaria"}

**Proposición 5.29 --- Parámetro de arco y velocidad unitaria** Sea

$$P:[a,b]\to\mathcal E$$

una curva tal que, para un origen fijo $O$, $r_O:[a,b]\to V$

es de clase $C^1$, y supongamos $v(t)\ne0$

para todo $t\in[a,b]$.

Definamos

$$s(t) = \int_a^t\|v(\tau)\|\,d\tau.$$

Entonces:

1.  $s$ es estrictamente creciente;

2.  $$\boxed{ s'(t)=\|v(t)\|>0; }$$

3.  $s$ es biyectiva de $[a,b]$ sobre $$[0,L(P;[a,b])];$$

4.  la reparametrización $$\widehat P(\ell) := P(s^{-1}(\ell))$$ satisface $$\boxed{ \|\widehat v(\ell)\|=1. }$$

Por tanto, $\widehat P$ es una parametrización por longitud de arco en el sentido de la definición 5.25.

**Demostración.** Por definición 5.24 y el teorema fundamental del cálculo,

$$s'(t)=\|v(t)\|.$$

Como $v(t)\ne0,$

tenemos $\|v(t)\|>0,$

y por tanto

$$s'(t)>0.$$

Así, $s$ es estrictamente creciente. Además, $s(a)=0$

y, por la proposición 5.28, $s(b) = \int_a^b\|v(t)\|\,dt = L(P;[a,b]).$ Por continuidad y monotonía estricta, $s:[a,b]\to[0,L(P;[a,b])]$

es biyectiva. Por el teorema inverso unidimensional,

$$\frac{d}{d\ell}s^{-1}(\ell) = \frac{ 1 }{ s'(s^{-1}(\ell)) } = \frac{ 1 }{ \|v(s^{-1}(\ell))\| }.$$

Aplicando proposición 5.18 a

$$\widehat P=P\circ s^{-1},$$

obtenemos

$$\widehat v(\ell) = v(s^{-1}(\ell)) \frac{d}{d\ell}s^{-1}(\ell).$$

Por tanto,

$$\widehat v(\ell) = \frac{ v(s^{-1}(\ell)) }{ \|v(s^{-1}(\ell))\| }.$$

Tomando normas,

$$\boxed{ \|\widehat v(\ell)\|=1. }$$

Luego $\widehat P$ es una parametrización por longitud de arco. $\square$

[]{#qué-significa-realmente-el-parámetro-de-arco}

### 5.13.17. Qué significa realmente el parámetro de arco {#fispm-c05-quuxe9-significa-realmente-el-paruxe1metro-de-arco}

En la parametrización original, $s(t) = L(P;[a,t]).$ En la nueva parametrización, $\widehat P(\ell) = P(s^{-1}(\ell)),$

el propio parámetro mide longitud geométrica acumulada desde el punto inicial. Por eso, para

$$0\le\ell_1<\ell_2\le L,$$

la longitud geométrica del tramo correspondiente es

$$\boxed{ L(\widehat P;[\ell_1,\ell_2]) = \ell_2-\ell_1. }$$

En efecto, por la proposición 5.28 aplicado a $\widehat P$,

$$L(\widehat P;[\ell_1,\ell_2]) = \int_{\ell_1}^{\ell_2} \|\widehat v(\ell)\|\,d\ell = \int_{\ell_1}^{\ell_2}1\,d\ell = \ell_2-\ell_1.$$

Ésta es la razón geométrica por la cual $\ell$ recibe el nombre de parámetro de longitud de arco.

[]{#balance-del-parámetro-natural}

### 5.13.18. Balance del parámetro natural {#fispm-c05-balance-del-paruxe1metro-natural}

El orden canónico queda ahora completado:

$$\boxed{ \text{proposición 5.28} \longrightarrow \text{definición 5.24} \longrightarrow \text{definición 5.25} \longrightarrow \text{proposición 5.29}. }$$

Proposición 5.28 justificó la fórmula integral. Definición 5.24 permitió definir

$$s(t)=L(P;[a,t]).$$

Definición 5.25 fijó qué significa estar parametrizado por longitud de arco. principio metodológico 5.19 obligó a declarar regularidad e invertibilidad antes de usar $s^{-1}$. Proposición 5.29 demostró que, para una curva $C^1$ sin instantes de reposo, la función $s$ produce una reparametrización con

$$\|\widehat v\|=1.$$

Ejercicios 5.27--5.29 aplicarán proposición 5.28 y proposición 5.29 antes del cierre local de §13. §14 continúa cerrado.

### 5.13.18. Comprobar la fórmula integral de longitud {#fispm-c05-e027-comprobar-la-fuxf3rmula-integral-de-longitud .unnumbered}

**Ejercicio 5.27 · Cálculo y comprobación** Sea $B=(e_1,e_2,e_3)$ una base ortonormal de $V$, sea $A\in\mathcal E$ y considera

$$P:[0,2]\to\mathcal E, \qquad P(t)=A+3t\,e_1+4t\,e_2.$$

1.  Calcula $v(t)$ y la rapidez $\sigma(t)$.

2.  Usa proposición 5.28 para calcular $L(P;[0,2])$.

3.  Contrasta el resultado con la geometría de la trayectoria.

**Solución desarrollada** La velocidad es constante:

$$v(t)=3e_1+4e_2.$$

Como $B$ es ortonormal, $\sigma(t) = \|v(t)\| = \sqrt{3^2+4^2} = 5.$ Por proposición 5.28,

$$L(P;[0,2]) = \int_0^2 5\,dt = \boxed{10}.$$

Geométricamente, la trayectoria es el segmento que une

$$P(0)=A$$

con

$$P(2)=A+6e_1+8e_2.$$

Su longitud euclídea es $\sqrt{6^2+8^2} = 10,$

de modo que la fórmula integral coincide con la longitud geométrica esperada.

### 5.13.18. Construir la función longitud de arco acumulada {#fispm-c05-e028-construir-la-funciuxf3n-longitud-de-arco-acumulada .unnumbered}

**Ejercicio 5.28 · FTC e inversa** Sea $e_1$ un vector unitario y considera

$$P:[1,2]\to\mathcal E, \qquad P(t)=A+t^2e_1.$$

1.  Calcula $v(t)$ y $\|v(t)\|$.

2.  Construye $$s(t)=\int_1^t\|v(\tau)\|\,d\tau.$$

3.  Verifica que $s$ es estrictamente creciente.

4.  Determina $s([1,2])$.

5.  Obtén explícitamente $s^{-1}$.

**Solución desarrollada** La velocidad es

$$v(t)=2t\,e_1.$$

Como $t\in[1,2]$ y $\|e_1\|=1$, $\|v(t)\| = 2t.$

Entonces $s(t) = \int_1^t 2\tau\,d\tau = t^2-1.$ Por tanto,

$$\boxed{ s(t)=t^2-1. }$$

Además, $s'(t)=2t>0$

en todo $[1,2]$, de modo que $s$ es estrictamente creciente. Sus valores extremos son $s(1)=0, \qquad s(2)=3.$ Por tanto,

$$\boxed{ s:[1,2]\to[0,3] }$$

es biyectiva.

Si

$$\ell=s(t)=t^2-1,$$

entonces $t=\sqrt{\ell+1},$

porque $t>0$ en el dominio.

Así,

$$\boxed{ s^{-1}(\ell)=\sqrt{\ell+1}, \qquad 0\le\ell\le3. }$$

### 5.13.18. Parametrización unitaria {#fispm-c05-e029-parametrizaciuxf3n-unitaria .unnumbered}

**Ejercicio 5.29 · Prueba y síntesis** Conserva la curva del ejercicio 5.28:

$$P(t)=A+t^2e_1, \qquad 1\le t\le2.$$

Usa

$$s^{-1}(\ell)=\sqrt{\ell+1}$$

para construir

$$\widehat P(\ell)=P(s^{-1}(\ell)).$$

1.  Obtén una fórmula explícita para $\widehat P(\ell)$.

2.  Calcula $\widehat v(\ell)$.

3.  Verifica directamente que $$\|\widehat v(\ell)\|=1.$$

4.  Comprueba que el parámetro $\ell$ mide longitud geométrica acumulada.

**Solución desarrollada** Sustituyendo

$$t=s^{-1}(\ell)=\sqrt{\ell+1}$$

en $P$,

$$\widehat P(\ell) = A+\bigl(\sqrt{\ell+1}\bigr)^2e_1 = A+(\ell+1)e_1.$$

Por tanto,

$$\boxed{ \widehat P(\ell) = A+(\ell+1)e_1, \qquad 0\le\ell\le3. }$$

Derivando, $\widehat v(\ell)=e_1.$

Como $\|e_1\|=1$,

$$\boxed{ \|\widehat v(\ell)\|=1. }$$

Por proposición 5.28,

$$L(\widehat P;[0,\ell]) = \int_0^\ell \|\widehat v(\lambda)\|\,d\lambda = \int_0^\ell 1\,d\lambda = \ell.$$

Así, el propio parámetro $\ell$ coincide con la longitud geométrica acumulada desde el punto inicial de la nueva parametrización.

[]{#cierre-conceptual-de-la-definición-geométrica-al-parámetro-natural}

### 5.13.19. Cierre conceptual: de la definición geométrica al parámetro natural {#fispm-c05-cierre-conceptual-de-la-definiciuxf3n-geomuxe9trica-al-paruxe1metro-natural}

§13 completa una cadena que comenzó en §11:

$$\boxed{ \text{longitudes poligonales} \longrightarrow \text{longitud geométrica} \longrightarrow \int\|v\| \longrightarrow \text{parámetro de arco}. }$$

Proposición 5.28 demostró que, para curvas $C^1$, $L(P;[a,b]) = \int_a^b\|v(t)\|\,dt.$

Definición 5.24 convirtió esa fórmula en una función acumulada

$$s(t)=L(P;[a,t]).$$

Definición 5.25 fijó el significado de parametrización por longitud de arco. Proposición 5.29 mostró que una curva $C^1$ sin instantes de reposo puede reparametrizarse de modo que

$$\|\widehat v\|=1.$$

Ejercicio 5.27 verificó la fórmula integral en una curva lineal elemental. Ejercicio 5.28 construyó e invirtió una función de arco no lineal. Ejercicio 5.29 verificó directamente que la reparametrización resultante tiene velocidad unitaria y que el nuevo parámetro mide longitud geométrica. La sección queda cerrada con la distinción lógica preservada:

$$\boxed{ \text{la integral calcula una longitud previamente definida;} \quad \text{no la define retrospectivamente}. }$$

§14 integrará los distintos niveles construidos a lo largo del capítulo sin introducir nueva matemática estructural.

[]{#integración-una-curva-varios-relojes-y-varias-descripciones}

[]{#fispm-t1-c05-s14}

[]{#fpm-i-05-s14}

## 5.14. Integración: una curva, varios relojes y varias descripciones {#fispm-c05-integraciuxf3n-una-curva-varios-relojes-y-varias-descripciones}

[]{#activación-una-misma-curva-puede-cambiar-de-descripción-de-varias-maneras}

### 5.14.1. Activación: una misma curva puede cambiar de descripción de varias maneras {#fispm-c05-activaciuxf3n-una-misma-curva-puede-cambiar-de-descripciuxf3n-de-varias-maneras}

A lo largo del capítulo aparecieron tres operaciones conceptualmente diferentes:

1.  cambiar el **marco espacial fijo**;

2.  cambiar el **parámetro** de una curva;

3.  olvidar la parametrización y conservar sólo la **trayectoria geométrica**.

Estas operaciones no afectan de la misma manera a todos los objetos. Un punto puede recibir coordenadas distintas. Un vector velocidad puede recibir columnas distintas. Una reparametrización puede modificar la velocidad como función del nuevo parámetro. La trayectoria geométrica puede permanecer igual. La longitud geométrica puede permanecer invariante. La tarea final del capítulo es separar sistemáticamente esos niveles.

[]{#principio-metodológico-final}

### 5.14.2. Principio metodológico final {#fispm-c05-principio-metodoluxf3gico-final}

**Principio metodológico 5.20 --- En toda comparación final preguntar: objeto, parámetro, marco y magnitud invariante** Antes de afirmar que dos descripciones «son iguales» o «son distintas», responder:

1.  **Objeto:** ¿se compara un punto, un vector, una columna de componentes, una curva parametrizada o una trayectoria?

2.  **Parámetro:** ¿se conserva el mismo parámetro o se usa una reparametrización?

3.  **Marco:** ¿se usa el mismo marco espacial fijo o se cambia de marco?

4.  **Invariante:** ¿qué magnitud geométrica debe permanecer igual bajo el cambio considerado?

No mezclar una transformación de representación con una transformación física.

principio metodológico 5.20 resume la disciplina tipológica del capítulo.

[]{#matriz-de-transformación-y-permanencia}

### 5.14.3. Matriz de transformación y permanencia {#fispm-c05-matriz-de-transformaciuxf3n-y-permanencia}

Para dos marcos fijos

$$F=(O,B), \qquad F'=(O',B'),$$

con ley

$$x_{F'}(t) = S^{-1}\bigl(x_F(t)-[c]_B\bigr),$$

tenemos:

- punto físico $P(t)$: **permanece**;

- coordenadas del punto: **cambian afínmente**;

- velocidad $v(t)\in V$: **permanece como vector geométrico**;

- componentes de velocidad: $$[v(t)]_{B'} = S^{-1}[v(t)]_B;$$

- aceleración $a(t)\in V$: **permanece como vector geométrico**;

- componentes de aceleración: $$[a(t)]_{B'} = S^{-1}[a(t)]_B.$$

Si ambos marcos son ortonormales, $\|v(t)\|$

permanece invariante.

[]{#efecto-de-una-reparametrización}

### 5.14.4. Efecto de una reparametrización {#fispm-c05-efecto-de-una-reparametrizaciuxf3n}

Sea

$$\widetilde P=P\circ\phi.$$

Entonces proposición 5.18 establece

$$\widetilde v(u) = v(\phi(u))\phi'(u).$$

Por proposición 5.21,

$$\|\widetilde v(u)\| = \|v(\phi(u))\|\,|\phi'(u)|.$$

Si $\phi$ es biyectiva y estrictamente monótona, proposición 5.27 garantiza

$$L(\widetilde P;J) = L(P;I).$$

Por tanto, una reparametrización puede cambiar la velocidad y la rapidez como funciones del parámetro sin cambiar la longitud geométrica total.

[]{#proposición-de-síntesis}

### 5.14.5. Proposición de síntesis {#fispm-c05-proposiciuxf3n-de-suxedntesis}

**Proposición 5.30 --- Coherencia de las descripciones fijas de un mismo movimiento** Considérese un movimiento

$$P:I\to\mathcal E$$

descrito en dos marcos euclídeos fijos $F=(O,B)$ y $F'=(O',B')$. Las afirmaciones sobre posición y trayectoria no requieren derivabilidad; las afirmaciones sobre velocidad y rapidez se entienden en los instantes donde $P$ sea derivable, y las afirmaciones sobre aceleración en los instantes donde $P$ sea dos veces derivable.

Entonces:

1.  las coordenadas de posición cambian afínmente: $$x_{F'}(t) = S^{-1}\bigl(x_F(t)-[c]_B\bigr);$$

2.  las componentes de velocidad y aceleración cambian linealmente: $$[v(t)]_{B'} = S^{-1}[v(t)]_B,$$ $$[a(t)]_{B'} = S^{-1}[a(t)]_B;$$

3.  si $B$ y $B'$ son ortonormales, $$\|v(t)\|$$ es independiente del marco;

4.  la trayectoria geométrica $$P(I)$$ es independiente del marco;

5.  la longitud geométrica es independiente del marco y, además, permanece invariante bajo reparametrizaciones estrictamente monótonas y biyectivas.

En consecuencia, cambiar una descripción fija no modifica por sí mismo el movimiento geométrico descrito.

**Demostración.** La afirmación 1 es proposición 5.4.

Las afirmaciones 2 son proposición 5.15 y proposición 5.16. La afirmación 3 es proposición 5.17. La trayectoria

$$P(I)\subseteq\mathcal E$$

está formada por puntos del espacio afín y no por sus columnas de coordenadas; por tanto, cambiar de marco no cambia el conjunto de puntos recorridos. La longitud geométrica definición 5.22 se construye únicamente mediante distancias

$$d(P(t_{i-1}),P(t_i)),$$

que son magnitudes geométricas independientes de un marco ortonormal fijo. Por ello un cambio de marco euclídeo fijo no altera las longitudes poligonales ni su supremo. Finalmente, proposición 5.27 establece la invariancia de la longitud bajo una reparametrización estrictamente monótona y biyectiva. Todas estas transformaciones son compatibles: cambian la representación o el parámetro según reglas precisas, sin confundir esos cambios con una modificación automática del objeto físico. $\square$

[]{#qué-cambia-y-qué-permanece-tabla-conceptual}

### 5.14.6. Qué cambia y qué permanece: tabla conceptual {#fispm-c05-quuxe9-cambia-y-quuxe9-permanece-tabla-conceptual}

  Objeto o magnitud     Cambio de marco fijo                   Reparametrización
  --------------------- -------------------------------------- ----------------------------------------------------------------------
  Punto $P$             no cambia                              se evalúa en otro parámetro
  Coordenadas $x_F$     cambio afín                            composición con $\phi$
  Trayectoria $P(I)$    no cambia                              se conserva si $\phi$ es sobreyectiva
  Velocidad $v$         mismo vector, otras componentes        se multiplica por $\phi'$
  Aceleración $a$       mismo vector, otras componentes        su transformación requiere derivar nuevamente; no se desarrolla aquí
  Rapidez $\|v\|$       invariante entre marcos ortonormales   se multiplica por $|\phi'|$
  Longitud geométrica   invariante                             invariante bajo $\phi$ monótona y biyectiva

La fila de aceleración bajo reparametrización marca deliberadamente una frontera: el capítulo no necesita desarrollar una fórmula adicional para cerrar su arquitectura.

### 5.14.6. Auditoría global de un movimiento en dos marcos y dos parametrizaciones {#fispm-c05-e030-auditoruxeda-global-de-un-movimiento-en-dos-marcos-y-dos-parametrizaciones .unnumbered}

**Ejercicio 5.30 · Síntesis, transferencia y frontera** Sea $F=(O,B)$ un marco ortonormal con

$$B=(e_1,e_2,e_3),$$

y considera el movimiento

$$P:[0,1]\to\mathcal E$$

definido por $P(t)=O+t\,e_1+t^2e_2.$

Considera un segundo marco ortonormal fijo

$$F'=(O',B'),$$

con

$$O'=O+c, \qquad [c]_B= \begin{pmatrix} 1\\ -1\\ 0 \end{pmatrix},$$

y

$$S= \begin{pmatrix} 0&-1&0\\ 1&0&0\\ 0&0&1 \end{pmatrix}.$$

Además, introduce

$$\phi:[0,2]\to[0,1], \qquad \phi(u)=\frac{u}{2},$$

y

$$\widetilde P=P\circ\phi.$$

Audita:

1.  $x_F(t)$ y $x_{F'}(t)$;

2.  $v(t)$, $a(t)$ y sus componentes en ambos marcos;

3.  la rapidez en ambos marcos;

4.  la trayectoria de $P$ y $\widetilde P$;

5.  $\widetilde v(u)$ y su rapidez;

6.  la longitud geométrica total de $P$ y $\widetilde P$;

7.  qué cambia si $u$ se interpreta como nuevo tiempo físico;

8.  qué preguntas quedan fuera del capítulo 5 y pertenecen a capítulos 6--9.

**Solución desarrollada** En el marco $F$,

$$\boxed{ x_F(t) = \begin{pmatrix} t\\ t^2\\ 0 \end{pmatrix}. }$$

Como

$$S^{-1} = S^{\mathsf T} = \begin{pmatrix} 0&1&0\\ -1&0&0\\ 0&0&1 \end{pmatrix},$$

la ley afín da

$$x_{F'}(t) = S^{-1} \left[ \begin{pmatrix} t\\ t^2\\ 0 \end{pmatrix} - \begin{pmatrix} 1\\ -1\\ 0 \end{pmatrix} \right].$$

Por tanto,

$$\boxed{ x_{F'}(t) = \begin{pmatrix} t^2+1\\ 1-t\\ 0 \end{pmatrix}. }$$

La velocidad y la aceleración geométricas son

$$\boxed{ v(t)=e_1+2t\,e_2, }$$

y

$$\boxed{ a(t)=2e_2. }$$

En $B$,

$$[v(t)]_B = \begin{pmatrix} 1\\ 2t\\ 0 \end{pmatrix}, \qquad [a(t)]_B = \begin{pmatrix} 0\\ 2\\ 0 \end{pmatrix}.$$

En $B'$,

$$[v(t)]_{B'} = S^{-1}[v(t)]_B = \boxed{ \begin{pmatrix} 2t\\ -1\\ 0 \end{pmatrix} },$$

y

$$[a(t)]_{B'} = S^{-1}[a(t)]_B = \boxed{ \begin{pmatrix} 2\\ 0\\ 0 \end{pmatrix} }.$$

Como ambas bases son ortonormales,

$$\boxed{ \|v(t)\| = \sqrt{1+4t^2} }$$

en ambos marcos. La reparametrización es $\widetilde P(u) = P\left(\frac u2\right).$

Como $\phi$ es biyectiva,

$$\boxed{ \widetilde P([0,2]) = P([0,1]). }$$

Por proposición 5.18, $\widetilde v(u) = v\left(\frac u2\right)\frac12.$

Como $v\left(\frac u2\right) = e_1+u\,e_2,$

obtenemos

$$\boxed{ \widetilde v(u) = \frac12e_1+\frac u2e_2. }$$

Su rapidez es

$$\boxed{ \|\widetilde v(u)\| = \frac12\sqrt{1+u^2}. }$$

La rapidez no permanece igual como función del nuevo parámetro: se transforma con el factor $|\phi'|=1/2$.

La longitud geométrica total sí permanece:

$$\boxed{ L(\widetilde P;[0,2]) = L(P;[0,1]). }$$

Esto sigue directamente de la proposición 5.27. Si se desea calcularla, proposición 5.28 permite escribir

$$L(P;[0,1]) = \int_0^1\sqrt{1+4t^2}\,dt,$$

mientras

$$L(\widetilde P;[0,2]) = \int_0^2 \frac12\sqrt{1+u^2}\,du.$$

La sustitución $u=2t$ muestra que ambas integrales son iguales, en concordancia con la invariancia geométrica. Si $u$ se interpreta como nuevo tiempo físico medido en la misma unidad que $t$, la nueva historia temporal dura $2$ unidades en lugar de $1$. La trayectoria es la misma, pero la ley temporal cambia.

Finalmente, la frontera del capítulo es:

- **capítulo 6:** modelización física, aproximaciones, escalas, linealización de modelos y control sistemático de regímenes;

- **capítulo 7:** cinemática sistemática en una dimensión, gráficas $x(t),v(t),a(t)$, condiciones iniciales y problemas inversos;

- **capítulo 8:** cinemática en varias dimensiones, coordenadas polares/cilíndricas, bases móviles y composición de movimientos;

- **capítulo 9:** masa, fuerza, leyes de Newton, ecuaciones de movimiento y causalidad dinámica.

El capítulo 5 termina antes de introducir cualquiera de esas estructuras.

[]{#cierre-conceptual-del-capítulo}

### 5.14.7. Cierre conceptual del capítulo {#fispm-c05-cierre-conceptual-del-capuxedtulo}

El capítulo 5 comenzó con una localización temporalmente etiquetada y terminó con una teoría elemental de curvas afines parametrizadas. La cadena conceptual construida es

$$\boxed{\begin{gathered} \text{evento} \to \text{movimiento}\\[2pt]\Downarrow\\[2pt]\text{trayectoria} \to \text{desplazamiento}\\[2pt]\Downarrow\\[2pt]v \to a\\[2pt]\Downarrow\\[2pt]\text{reparametrización} \to \text{rapidez}\\[2pt]\Downarrow\\[2pt]\text{longitud} \to \text{parámetro natural}. \end{gathered}}$$

A lo largo de esa cadena se mantuvieron tres separaciones fundamentales:

$$\boxed{ \text{objeto geométrico} \ne \text{representación coordenada}, }$$

$$\boxed{ \text{trayectoria} \ne \text{ley temporal}, }$$

y

$$\boxed{ \text{cinemática} \ne \text{dinámica}. }$$

La salida del capítulo no es todavía un catálogo de movimientos físicos, sino una infraestructura matemática y conceptual para construirlos después con control de tipos, parámetros, marcos e invariantes.

[^1]: R. Shankar, *Fundamentals of Physics I: Mechanics, Relativity, and Thermodynamics*, Expanded ed., Yale University Press, 2019, cap. 1, §1.2 «Kinematics and dynamics», pp. 2--3. Se usa aquí como control de la frontera entre descripción cinemática y explicación dinámica.

[^2]: Michael Spivak, *Physics for Mathematicians: Mechanics I*, Publish or Perish, 2010, cap. 1, pp. 9--10; véase también Michael Spivak, *Calculus*, 4.ª ed., Publish or Perish, 2008, cap. 12, apéndice «Parametric Representation of Curves», pp. 244--248.

[^3]: R. Shankar, *Fundamentals of Physics I*, Expanded ed., Yale University Press, 2019, cap. 1, §1.3 «Average and instantaneous quantities», pp. 4--6; D. Kleppner y R. J. Kolenkow, *An Introduction to Mechanics*, 2.ª ed., Cambridge University Press, 2010, cap. 1, §§1.5--1.6, pp. 11--18.

[^4]: Shankar, *Fundamentals of Physics I*, cap. 2, §2.5 «Derivatives of the position vector $\mathbf r$», pp. 26--27; Kleppner--Kolenkow, *An Introduction to Mechanics*, cap. 1, §1.6 «Velocity and Acceleration», pp. 13--18.

[^5]: Shankar, *Fundamentals of Physics I*, cap. 1, §1.2 «Kinematics and dynamics», pp. 2--3; §1.3, pp. 4--6. La referencia documenta la separación entre descripción del movimiento y explicación dinámica.

[^6]: Michael Spivak, *Calculus*, 4.ª ed., Publish or Perish, 2008, cap. 12, apéndice «Parametric Representation of Curves», especialmente p. 247; para la regla de la cadena escalar, cap. 10, p. 178.

[^7]: Kleppner--Kolenkow, *An Introduction to Mechanics*, 2.ª ed., cap. 1, §1.6 «Velocity and Acceleration», pp. 13--18; Shankar, *Fundamentals of Physics I*, cap. 1, §1.3, pp. 4--6.

[^8]: Sadri Hassani, *Mathematical Methods for Students of Physics and Related Fields*, 2.ª ed., Springer, 2009, cap. 11, §11.1.4, pp. 322--323, como control de la fórmula estándar de longitud de arco; Spivak, *Calculus*, cap. 13, p. 253 y ss., y cap. 14, p. 285 y ss., para integral de Riemann y teorema fundamental del cálculo.
