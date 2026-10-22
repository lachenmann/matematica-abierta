---
title: "El oscilador armónico"
subtitle: "Física para matemáticos · Tomo I · Capítulo 10"
author: "A. Peña"
description: "Capítulo 10 de la edición revisada, con problemas y soluciones desarrolladas."
content-id: MA-BCH-0363
source-id: FISPM-r20261021-C10
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
edition: r20261021
canonical-edition: true
date-modified: 2026-10-21
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0354"]
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

[← 9. Impulso, colisiones y centro de masa](fisica-para-matematicos-09-impulso-colisiones-y-centro-de-masa.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [11. Disipación y respuesta forzada →](fisica-para-matematicos-11-disipacion-y-respuesta-forzada.md)

Un carro de dos kilogramos está unido a un resorte horizontal de constante $8\,\mathrm{N/m}$. Lo preparamos doce centímetros a la derecha de la posición donde el resorte tiene su longitud natural y le damos una velocidad de treinta y dos centímetros por segundo hacia la derecha. En ese instante el resorte ya tira hacia la izquierda, pero el carro todavía avanza. Queremos reconstruir el movimiento: cuánto más se alejará, cuándo comenzará a regresar y cuánto tardará en repetir su estado.

Seguiremos al carro como una partícula de masa constante en el marco inercial del laboratorio. El eje $x$ apunta hacia la derecha y su origen coincide con la longitud natural del resorte. El riel es horizontal; peso y normal se compensan. Omitimos rozamiento, resistencia del aire, masa del resorte y rotación del carro. Suponemos que la fuerza del resorte es $F=-kx$ en el intervalo $|x|<0{,}30\,\mathrm m$. Será necesario comprobar que el movimiento calculado permanece allí.

Tomamos $t=0$ cuando termina la preparación. Los datos y la segunda ley de Newton dan

$$
m\ddot x=-kx,\qquad
x(0)=0{,}12\,\mathrm m,\qquad
\dot x(0)=0{,}32\,\mathrm{m/s}.
$$

La aceleración inicial es $-0{,}48\,\mathrm{m/s^2}$. Ese signo no contradice el sentido de la velocidad: significa que, mientras el carro avanza hacia la derecha, pierde rapidez. Las fórmulas de aceleración constante no describen el movimiento completo, porque la fuerza cambia con la posición. Los capítulos anteriores permitían calcular una rapidez mediante energía o un cambio de velocidad mediante impulso; conocer el instante de cada evento exige resolver ahora la ecuación de movimiento.

![El carro se prepara a la derecha del equilibrio con velocidad hacia la derecha y fuerza restauradora hacia la izquierda.](/assets/books/fispm/r20261021/oscilador_preparacion.svg){.fpm-v04-figure}

*Figura 10.1.* Velocidad y fuerza pueden tener sentidos opuestos. Se dibujan con flechas de distinto color y rótulos explícitos; sus longitudes no comparan magnitudes de unidades diferentes. El origen se refiere al equilibrio del modelo horizontal.

## Una función que conserva su forma al derivar dos veces

Al dividir por la masa aparece la razón $k/m$, cuyas unidades son $\mathrm{s^{-2}}$. Su raíz positiva, que denotaremos por $\omega$, tiene unidades de inverso de tiempo. Para el carro, $\omega=\sqrt{k/m}=2\,\mathrm{s^{-1}}$ y buscamos una función que satisfaga $\ddot x=-\omega^2x$. Seno y coseno ofrecen precisamente ese comportamiento: derivarlos dos veces devuelve su negativo, acompañado por el cuadrado de la frecuencia de su argumento.

**Definición.** Un movimiento unidimensional es *armónico simple* respecto de un equilibrio fijo $x_e$ si su desplazamiento $q(t)=x(t)-x_e$ es dos veces continuamente derivable y satisface

$$
\ddot q+\omega^2q=0
$$

para una constante $\omega>0$, llamada *frecuencia angular*. En un resorte ideal horizontal con masa $m>0$ y constante $k>0$, $x_e=0$ y $\omega=\sqrt{k/m}$.

La definición incluye la solución de reposo $q=0$. La palabra oscilación suele reservarse para las soluciones no constantes. El signo positivo de $\omega^2$ en la ecuación es sustantivo: representa una aceleración que apunta hacia el equilibrio. Cambiarlo produciría otra dinámica.

Podemos ensayar una combinación $q(t)=a\cos(\omega t)+b\sin(\omega t)$. En $t=0$, el coseno vale uno y el seno cero, de modo que $a$ debe ser la posición inicial. Al derivar, $\dot q(0)=\omega b$, lo que fija el segundo coeficiente. Esta construcción encuentra una solución, pero todavía debemos justificar que no deja fuera otros movimientos con los mismos datos.

**Proposición.** Dados $\omega>0$, $q_0\in\mathbb R$ y $v_0\in\mathbb R$, la única solución real de clase $C^2$ en $\mathbb R$ de $\ddot q+\omega^2q=0$, $q(0)=q_0$, $\dot q(0)=v_0$, es

$$
q(t)=q_0\cos(\omega t)+\frac{v_0}{\omega}\sin(\omega t).
$$

**Demostración.** Derivar dos veces verifica la ecuación y evaluar en cero verifica ambos datos; la fórmula está definida para todo tiempo real. Para demostrar unicidad, supongamos que $q_1$ y $q_2$ son dos soluciones con esos mismos datos y consideremos su diferencia $d=q_1-q_2$. La linealidad de la ecuación da $\ddot d+\omega^2d=0$, con $d(0)=\dot d(0)=0$. Necesitamos convertir esos datos nulos en una afirmación válida en todo el intervalo, y una suma de cuadrados nos permite aprovechar a la vez la ecuación y el signo de $\omega^2$:

$$
\frac{d}{dt}\left(\frac12\dot d^{\,2}+\frac12\omega^2d^2\right)
=\dot d(\ddot d+\omega^2d)=0.
$$

La expresión es constante y vale cero al principio. Como sus sumandos son no negativos y $\omega>0$, necesariamente $d=0$ y $\dot d=0$ en todos los instantes. Por tanto, las dos soluciones coinciden.

La prueba evita exigir un teorema general de ecuaciones diferenciales como prerrequisito. También muestra por qué fijar sólo la posición inicial sería insuficiente: quedaría libre el coeficiente del seno. Elegir la velocidad inicial determina qué movimiento pasa por esa posición.

Para el carro obtenemos

$$
x(t)=(0{,}12\,\mathrm m)\cos(2t/\mathrm s)
+(0{,}16\,\mathrm m)\sin(2t/\mathrm s).
$$

Escribir el argumento como $2t/\mathrm s$ hace explícito que es adimensional. Cuando se utiliza $\omega t$, el factor $\omega$ lleva las unidades necesarias. La derivación da la velocidad y la aceleración sin nuevas hipótesis:

$$
\begin{aligned}
\dot q(t)&=-\omega q_0\sin(\omega t)+v_0\cos(\omega t),\\
\ddot q(t)&=-\omega^2q(t).
\end{aligned}
$$

## Amplitud, fase y reloj

La combinación anterior es correcta, aunque todavía no muestra de inmediato la mayor separación respecto del equilibrio. La identidad del coseno de una suma permite recogerla en una sola función. Si $A>0$ y $\varphi$ satisfacen

$$
A=\sqrt{q_0^2+(v_0/\omega)^2},\qquad
\cos\varphi=\frac{q_0}{A},\qquad
\sin\varphi=-\frac{v_0}{\omega A},
$$

entonces $q(t)=A\cos(\omega t+\varphi)$. Los dos últimos cocientes son adimensionales y sus cuadrados suman uno, por lo que determinan un ángulo módulo $2\pi$. Utilizar únicamente una tangente perdería la información del cuadrante y fallaría cuando el denominador fuera cero.

**Definición.** Para un movimiento periódico de posición variable, un *período* es un número $T>0$ tal que $q(t+T)=q(t)$ para todo $t$. Si existe el menor de esos números, se llama *período fundamental*. Su inverso $f=1/T$ es la *frecuencia*, medida en ciclos por segundo o hertz. La *amplitud* de un movimiento armónico es el máximo de $|q(t)|$.

**Definición.** En la representación $q(t)=A\cos(\omega t+\varphi)$, con $A>0$, llamamos *fase* al argumento $\omega t+\varphi$, considerado módulo $2\pi$, y *fase inicial* al valor $\varphi$ que corresponde al origen temporal elegido.

**Proposición.** Para toda solución armónica no constante, con $A$ definido arriba,

$$
T=\frac{2\pi}{\omega},\qquad
f=\frac{\omega}{2\pi},\qquad
|q|_{\max}=A,\qquad
|\dot q|_{\max}=\omega A,\qquad
|\ddot q|_{\max}=\omega^2A.
$$

**Demostración.** La representación por un coseno alcanza los valores $\pm A$, y sus dos derivadas tienen factores $\omega A$ y $\omega^2A$ y factores trigonométricos de módulo máximo uno. Aumentar el tiempo en $2\pi/\omega$ repite la fase y la posición. Para verificar que ése es el menor período, tomemos un instante $t_*$ en que $q(t_*)=A$. Si $\tau>0$ es cualquier período, $q(t_*+\tau)=A$ obliga a que $\cos(\omega\tau)=1$. Por tanto, $\omega\tau$ es un múltiplo entero positivo de $2\pi$; el menor corresponde a uno. La fórmula de $f$ resulta de invertir ese período.

El reposo $q=0$ requiere un tratamiento aparte. Cualquier tiempo positivo repite ese estado y no hay un menor período positivo; su fase tampoco queda definida por los cocientes anteriores. Estas excepciones evitan asignar información ficticia al estado que no oscila.

En el carro inicial, $A=0{,}20\,\mathrm m$, porque $0{,}12^2+0{,}16^2=0{,}20^2$. Podemos tomar $\varphi=-\delta$, con $\delta=\arctan(4/3)$ entre cero y $\pi/2$. Su fase inicial es negativa: primero avanza hasta que la fase alcanza cero. La primera detención ocurre en $t=\delta/\omega\approx0{,}464\,\mathrm s$, en $x=A$. El primer paso posterior por el equilibrio ocurre cuando la fase alcanza $\pi/2$, en

$$
t=\frac{\delta+\pi/2}{\omega}\approx1{,}249\,\mathrm s.
$$

Allí la velocidad es $-0{,}40\,\mathrm{m/s}$. El estado completo vuelve a repetirse cada $T=\pi\,\mathrm s$. La amplitud calculada es menor que los treinta centímetros declarados como límite del resorte lineal, de modo que la trayectoria permanece en su dominio supuesto.

![La posición, la velocidad y la aceleración del carro se muestran contra el mismo tiempo.](/assets/books/fispm/r20261021/oscilador_tiempo.svg){.fpm-v04-figure}

*Figura 10.2.* Las tres gráficas representan el mismo movimiento y tienen ejes verticales con unidades distintas. La primera detención, el primer cruce del equilibrio y el período completo se identifican con líneas verticales. Aceleración nula no implica reposo.

La frecuencia angular cuenta radianes de fase por unidad de tiempo; la frecuencia cuenta ciclos. Para este carro, $\omega=2\,\mathrm{rad/s}$ y $f=1/\pi\,\mathrm{Hz}$. El factor $2\pi$ permite convertir una en otra. Cambiar la amplitud conserva ese período dentro del modelo lineal ideal, pero cambia las velocidades, las aceleraciones y la energía.

## La energía dibuja los estados posibles

La misma suma de cuadrados que permitió demostrar unicidad tiene una interpretación física para el resorte. Su potencial, con referencia cero en el equilibrio, es $U=kq^2/2$; la energía cinética es $K=m\dot q^2/2$.

**Proposición.** Para el oscilador ideal con $m,k>0$ y $\omega^2=k/m$, la energía

$$
E=\frac12m\dot q^2+\frac12kq^2
$$

es constante y vale $kA^2/2$. Si $A>0$, sus estados satisfacen

$$
\frac{q^2}{A^2}+\frac{\dot q^2}{\omega^2A^2}=1.
$$

**Demostración.** Derivar la energía da $\dot E=\dot q(m\ddot q+kq)=0$. Al evaluar en el dato inicial obtenemos $2E/k=q_0^2+(m/k)v_0^2=q_0^2+(v_0/\omega)^2=A^2$. Dividir el balance por $kA^2/2$ proporciona la ecuación indicada.

El plano de estados utiliza posición en un eje y velocidad en el otro. La curva de energía es una elipse en esas coordenadas; si representamos $\dot q/\omega$ frente a $q$, ambos ejes tienen unidades de longitud y aparece una circunferencia. La posición por sí sola no fija el estado: en cada punto interior al recorrido puede haber movimiento hacia la derecha o hacia la izquierda. El signo de la velocidad distingue esas dos posibilidades.

![Una elipse de estados muestra dos velocidades opuestas para una misma posición y el sentido de recorrido.](/assets/books/fispm/r20261021/oscilador_estado.svg){.fpm-v04-figure}

*Figura 10.3.* El movimiento del ejemplo pasa inicialmente por $(0{,}12\,\mathrm m,0{,}32\,\mathrm{m/s})$. La misma posición con velocidad negativa pertenece a otro instante. Las flechas de la elipse representan evolución temporal, no fuerzas en el espacio físico.

En los extremos $q=\pm A$, la energía es enteramente potencial y el carro se detiene sólo un instante, porque allí la fuerza no es nula. Al cruzar el equilibrio, toda la energía de este modelo es cinética y la rapidez alcanza su máximo. Para el ejemplo, $E=(8\,\mathrm{N/m})(0{,}20\,\mathrm m)^2/2=0{,}16\,\mathrm J$.

La conservación permite hallar $|\dot q|=\omega\sqrt{A^2-q^2}$, pero deja pendiente el signo. La solución temporal resuelve qué rama sigue el movimiento y cuándo cambia de rama en un extremo. Ambas descripciones se complementan: la energía controla posiciones y rapideces posibles, mientras que la fase sitúa al sistema sobre esa curva en cada instante.

![La energía potencial y la cinética se intercambian durante un período del carro.](/assets/books/fispm/r20261021/oscilador_energia.svg){.fpm-v04-figure}

*Figura 10.4.* Las energías suman $0{,}16\,\mathrm J$. Cada una repite sus valores en medio período del movimiento, porque depende del cuadrado de un seno o un coseno. Esa repetición no significa que posición y velocidad hayan vuelto a su estado inicial.

## Medir desde un equilibrio desplazado

Una fuerza constante puede cambiar el origen adecuado sin cambiar la frecuencia. Para un carro sometido además a un tirón constante $f_0$, la ecuación es $m\ddot x=f_0-kx$. Su equilibrio es $x_e=f_0/k$. La variable $q=x-x_e$ tiene las mismas derivadas temporales que $x$, y lleva la ecuación a $m\ddot q=-kq$.

**Proposición.** Sean $m,k>0$ y $f_0$ constante. Toda solución de $m\ddot x=f_0-kx$ se obtiene trasladando una solución armónica mediante $x=x_e+q$, con $x_e=f_0/k$. Para datos $x(0)=x_0$ y $\dot x(0)=v_0$,

$$
x(t)=x_e+(x_0-x_e)\cos(\omega t)
+\frac{v_0}{\omega}\sin(\omega t),\qquad \omega=\sqrt{k/m}.
$$

**Demostración.** Como $x_e$ es constante, $\ddot q=\ddot x$. Sustituir $x=x_e+q$ cancela $f_0-kx_e$ y deja la ecuación armónica. Los datos de $q$ son $q(0)=x_0-x_e$ y $\dot q(0)=v_0$; el resultado de existencia y unicidad ya probado determina su solución.

En un resorte vertical, tomando $y$ hacia abajo desde la longitud natural, $m\ddot y=mg-ky$. El equilibrio está en $y_e=mg/k$. La gravedad uniforme desplaza la posición de equilibrio y no modifica $\omega$ en este modelo. Soltar el cuerpo desde la longitud natural equivale a comenzar con $q_0=-y_e$, no con amplitud cero.

![Un resorte vertical distingue longitud natural, equilibrio y desplazamiento respecto de ese equilibrio.](/assets/books/fispm/r20261021/oscilador_vertical.svg){.fpm-v04-figure}

*Figura 10.5.* Las coordenadas $y$ y $q=y-y_e$ tienen orígenes diferentes. En $y=y_e$ se equilibran peso y fuerza del resorte. El esquema utiliza gravedad uniforme, resorte ideal y soporte fijo; no identifica la longitud natural con el equilibrio cargado.

Si los apoyos cambian con el tiempo o la fuerza deja de ser constante, esta traslación por un número fijo ya no resuelve el problema. También puede cambiar la inercia relevante: dos masas libres unidas por un resorte no equivalen a una masa con el otro extremo inmóvil. El ejercicio 13 deduce su ecuación relativa utilizando el centro de masa del capítulo anterior.

## Hasta dónde vale una aproximación armónica

Una fuerza restauradora real puede parecer lineal cerca de un equilibrio sin serlo en todo el recorrido. Sea $F(x_e)=0$ y supongamos que, para desplazamientos pequeños,

$$
F(x_e+q)=-k_{\rm ef}q+R(q),\qquad k_{\rm ef}>0.
$$

El término $R(q)$ recoge la parte que estamos omitiendo. Cuando $F$ es derivable, la elección natural es $k_{\rm ef}=-F'(x_e)$, siempre que esa cantidad sea positiva. La definición de derivada asegura $R(q)/q\to0$ al acercarse al equilibrio. Si $F'$ es cero, este argumento no produce una frecuencia armónica positiva; los mínimos planos del capítulo 8 necesitan otro análisis.

La ecuación lineal aproximada tiene $\omega=\sqrt{k_{\rm ef}/m}$. Decir que $R$ es pequeño controla de inmediato la diferencia de aceleraciones evaluadas en una misma posición, pero la posición de cada trayectoria cambia con el tiempo. Para comparar movimientos necesitamos estimar el error acumulado.

**Proposición.** Sea $\omega>0$. En un intervalo $[0,\tau]$, supongamos que $q$ y $q_h$ son funciones de clase $C^2$ con los mismos datos iniciales, que $q_h$ satisface la ecuación armónica y que

$$
\ddot q+\omega^2q=r(t)
$$

con $r$ continua. Entonces

$$
q(t)-q_h(t)=\frac{1}{\omega}\int_0^t
\sin\big(\omega(t-s)\big)r(s)\,ds.
$$

En particular, si $|r(s)|\leq r_*$ en todo el intervalo, se cumple $|q(t)-q_h(t)|\leq r_*t/\omega$ para $0\leq t\leq\tau$.

**Demostración.** Denotemos por $z(t)$ la integral del enunciado. En cero, $z=0$. Al derivar, el término del extremo superior contiene $\sin0=0$, y queda $\dot z(t)=\int_0^t\cos(\omega(t-s))r(s)\,ds$, de modo que también $\dot z(0)=0$. Una segunda derivación introduce el término $r(t)$ y da $\ddot z=r(t)-\omega^2z$. Por otra parte, $d=q-q_h$ satisface esa misma ecuación y tiene datos iniciales nulos. La diferencia $d-z$ satisface la ecuación armónica homogénea con datos nulos y por la unicidad ya probada es cero. Finalmente, usar $|\sin|\leq1$ dentro de la integral da la cota $r_*t/\omega$.

Para la fuerza anterior, $r(t)=R(q(t))/m$. Una cota local sobre $R$ sólo puede usarse mientras la trayectoria real permanezca en el intervalo donde esa cota vale. A veces el balance de energía permite garantizar ese confinamiento; el ejercicio 16 lo hace para una fuerza con un término cúbico. La estimación puede ser conservadora, pero declara qué se controla y durante cuánto tiempo.

Un ejemplo físico familiar es el péndulo simple. Una masa puntual al final de una cuerda ideal de longitud $\ell$ tiene aceleración tangencial $\ell\ddot\theta$. La componente tangencial del peso es $-mg\sin\theta$ y la tensión no tiene componente tangencial. Por tanto,

$$
\ddot\theta+\frac{g}{\ell}\sin\theta=0.
$$

Para ángulos pequeños en radianes, sustituir $\sin\theta$ por $\theta$ produce la ecuación armónica de frecuencia $\sqrt{g/\ell}$. El ejercicio 15 estima la discrepancia de los términos restauradores; esa comparación no es, por sí sola, una cota del error del período. La independencia exacta entre período y amplitud corresponde al oscilador lineal, no al péndulo de amplitud arbitraria.

## Lo que permiten reconstruir unas observaciones

Un registro de posición con suficiente resolución puede dar amplitud, período y fase del modelo. Medir sólo posiciones en instantes muy separados puede dejar ambigua incluso la frecuencia: movimientos que completan ciclos adicionales entre las muestras pueden coincidir en todos los puntos registrados. El ejercicio 18 construye dos ejemplos exactos.

![Dos oscilaciones de frecuencias diferentes coinciden en posiciones registradas cada segundo.](/assets/books/fispm/r20261021/oscilador_muestreo.svg){.fpm-v04-figure}

*Figura 10.6.* Los puntos muestran el mismo registro en tiempos enteros para dos movimientos distintos. Una observación intermedia permite separarlos. Las curvas son modelos matemáticos; los puntos no se presentan como mediciones reales.

El período se estima mejor contando varias oscilaciones equivalentes que cronometrando una sola. Sin embargo, la reducción de una cota temporal por ciclo no elimina otras incertidumbres, como una masa mal conocida o el cambio de amplitud por pérdidas. Del período ideal $T=2\pi\sqrt{m/k}$ se obtiene $k=4\pi^2m/T^2$: una inferencia de rigidez exige conservar las cotas de ambas magnitudes.

La propia prueba de unicidad permite interpretar qué sucede con pequeñas diferencias de preparación. Para dos soluciones del mismo oscilador, su diferencia vuelve a ser armónica y permanece acotada por una amplitud fijada por las diferencias iniciales. En cambio, un pequeño error de frecuencia puede producir un desfase creciente al comparar durante muchos ciclos. Los dos últimos problemas distinguen estas situaciones; la estabilidad frente a los datos iniciales no convierte un modelo aproximado en exacto para todo tiempo.

![En el plano de desplazamiento y velocidad reescalada, las diferencias iniciales quedan dentro de una circunferencia de error.](/assets/books/fispm/r20261021/oscilador_errores.svg){.fpm-v04-figure}

*Figura 10.7.* Ambos ejes tienen unidades de longitud al representar $\Delta v/\omega$ frente a $\Delta q$. Para el mismo valor de $\omega$, el radio de error se conserva. Comparar dos frecuencias distintas es otro problema, que puede acumular fase.

## Ejercicios

Los primeros cinco problemas fijan la traducción entre preparación, solución y reloj. Del 6 al 10 se combinan datos incompletos, energía y elección del equilibrio. Los restantes introducen impulsos, contactos, dos masas libres, aproximaciones y mediciones. Todos los datos son didácticos. Los resortes se consideran ideales y sin masa, y los soportes fijos, salvo donde el enunciado indique lo contrario. Se omiten pérdidas; para gravedad se usa $g=10\,\mathrm{m/s^2}$.

### 1. Soltar desde el reposo {#ejercicio-10-1}

Una masa de $0{,}5\,\mathrm{kg}$ está unida a un resorte horizontal de constante $18\,\mathrm{N/m}$. Se suelta en reposo a $0{,}10\,\mathrm m$ del equilibrio. Obtén posición, período, rapidez máxima y energía.

### 2. Comenzar cruzando el equilibrio {#ejercicio-10-2}

Una masa de un kilogramo, unida a un resorte de $9\,\mathrm{N/m}$, pasa por el equilibrio con velocidad $-0{,}60\,\mathrm{m/s}$ en $t=0$. Encuentra su solución, amplitud y una fase inicial para la convención del coseno. Calcula cuándo llega por primera vez al extremo negativo y cuándo vuelve a cruzar el equilibrio.

### 3. Resolver el reloj del ejemplo inicial {#ejercicio-10-3}

Para el carro de dos kilogramos y resorte de $8\,\mathrm{N/m}$, con $x_0=0{,}12\,\mathrm m$ y $v_0=0{,}32\,\mathrm{m/s}$, reconstruye amplitud, primera detención y primer cruce posterior del equilibrio. Indica el sentido de movimiento en ese cruce.

### 4. Distinguir hertz de radianes por segundo {#ejercicio-10-4}

Un oscilador de masa $0{,}20\,\mathrm{kg}$ tiene amplitud de tres centímetros y frecuencia de dos hertz. Calcula frecuencia angular, constante del resorte, rapidez máxima y energía, conservando el factor $2\pi$.

### 5. Recorrer la mitad de la amplitud {#ejercicio-10-5}

Un oscilador parte del extremo positivo en reposo. ¿Cuánto tarda en alcanzar por primera vez $q=A/2$? Expresa el tiempo como fracción de su período y encuentra la velocidad en ese instante.

### 6. Una rapidez deja dos estados posibles {#ejercicio-10-6}

En un oscilador con $m=2\,\mathrm{kg}$ y $k=8\,\mathrm{N/m}$ se mide $q=0{,}06\,\mathrm m$ y rapidez $0{,}16\,\mathrm{m/s}$. Tomando ese instante como origen temporal, determina la amplitud y las dos soluciones compatibles. ¿Fija la energía cuál de ellas ocurre?

### 7. Una proporción entre energías {#ejercicio-10-7}

Un oscilador se suelta desde $q=A>0$. Determina el primer instante en que su energía potencial es tres veces su energía cinética. Expresa tiempo, posición y velocidad mediante $T$, $A$ y $\omega$.

### 8. Cambiar masa y rigidez {#ejercicio-10-8}

Se comparan dos osciladores con la misma amplitud. El segundo tiene cuatro veces la masa y nueve veces la constante elástica del primero. Compara sus períodos, frecuencias angulares, rapideces máximas y energías. Explica por qué fijar la amplitud no equivale a fijar la energía.

### 9. La longitud natural no es el equilibrio cargado {#ejercicio-10-9}

Una masa de $0{,}5\,\mathrm{kg}$ cuelga de un resorte vertical de $50\,\mathrm{N/m}$. Se suelta desde la longitud natural y en reposo. Con $y$ hacia abajo desde esa longitud, calcula equilibrio, solución, mayor extensión y período.

### 10. Encender una fuerza constante {#ejercicio-10-10}

Un carro de dos kilogramos está inicialmente en reposo en la longitud natural de un resorte horizontal de $8\,\mathrm{N/m}$. Desde $t=0$ se aplica y mantiene un tirón de $0{,}8\,\mathrm N$ hacia la derecha. Encuentra el movimiento, la primera detención posterior y la rapidez máxima.

### 11. Preparar y detener con impulsos {#ejercicio-10-11}

Un oscilador de $0{,}5\,\mathrm{kg}$ y $k=8\,\mathrm{N/m}$ parte en reposo en el equilibrio. Recibe un impulso positivo de $0{,}20\,\mathrm{N\,s}$ de duración idealmente despreciable. Obtén el movimiento posterior. ¿Qué impulso lo detendría definitivamente al regresar por primera vez al equilibrio y cuándo habría que aplicarlo?

### 12. Un impacto que prepara la oscilación {#ejercicio-10-12}

Un proyectil de $0{,}20\,\mathrm{kg}$ llega horizontalmente a $3\,\mathrm{m/s}$ y queda incrustado en un bloque de $0{,}80\,\mathrm{kg}$ unido a un resorte horizontal de $25\,\mathrm{N/m}$. Antes del impacto, el bloque está en reposo en el equilibrio. El choque es tan breve que el desplazamiento durante él y el impulso del resorte pueden despreciarse. Calcula la amplitud posterior y la energía cinética transformada durante el choque. Después suponga que, durante un impacto de duración a lo sumo $0{,}002\,\mathrm s$, se garantiza $|x|\leq0{,}001\,\mathrm m$ para el bloque. Acote el efecto del impulso elástico omitido y obtenga una envolvente de la amplitud posterior, conservando los restantes datos.

### 13. Ambos extremos pueden moverse {#ejercicio-10-13}

Dos masas libres de uno y tres kilogramos están unidas por un resorte de constante $12\,\mathrm{N/m}$ y longitud natural $L>0{,}20\,\mathrm m$. En $t=0$, sus posiciones son $r_1=0$, $r_2=L+0{,}20\,\mathrm m$, y ambas están en reposo. El riel es liso. Deduce la ecuación de la extensión $q=r_2-r_1-L$ y encuentra frecuencia, amplitudes de cada masa respecto de sus posiciones de equilibrio y energía.

### 14. Dos resortes restauran el mismo desplazamiento {#ejercicio-10-14}

Un carro de un kilogramo está entre dos resortes horizontales unidos a paredes fijas, de constantes $6$ y $10\,\mathrm{N/m}$. En el equilibrio sus fuerzas se compensan; al moverlo una distancia $q$ a la derecha, la fuerza de cada resorte cambia en sentido restaurador y ambos siguen conectados. Se suelta desde $q=0{,}05\,\mathrm m$. Calcula frecuencia angular, período y energía respecto del equilibrio.

### 15. Un péndulo y el error de la fuerza aproximada {#ejercicio-10-15}

Un péndulo simple de un metro se suelta desde un ángulo de $0{,}10$ radianes. Obtén la solución armónica aproximada y su período. Demuestra $|\theta-\sin\theta|\leq|\theta|^3/6$ y usa esa desigualdad para acotar la discrepancia del término restaurador respecto de su versión lineal en $|\theta|\leq0{,}10$. ¿Es esa cota automáticamente una cota del error del período?

### 16. Un resorte que no es exactamente lineal {#ejercicio-10-16}

Una masa de un kilogramo recibe la fuerza $F(q)=-kq-\beta q^3$, con $k=9\,\mathrm{N/m}$ y $\beta=9\,\mathrm{N/m^3}$. Parte de $q_0=0{,}10\,\mathrm m$ en reposo; se considera una solución de clase $C^2$ definida al menos hasta dos segundos. Construye el potencial y usa la energía para demostrar $|q(t)|\leq0{,}10\,\mathrm m$ mientras exista la solución. Compara con $q_h(t)=0{,}10\cos(3t/\mathrm s)\,\mathrm m$ y da una cota del error de posición hasta dos segundos.

### 17. Inferir una rigidez con cotas {#ejercicio-10-17}

Se cronometran veinte ciclos completos equivalentes. El intervalo total está entre $39{,}8$ y $40{,}2\,\mathrm s$, y la masa entre $0{,}99$ y $1{,}01\,\mathrm{kg}$. Bajo el modelo ideal, calcula una banda para el período y una banda para la constante elástica. Trata las bandas como cotas, sin añadir un modelo probabilístico.

### 18. Dos frecuencias, el mismo registro {#ejercicio-10-18}

Se toman posiciones cada segundo de un movimiento que parte del extremo positivo con amplitud $0{,}10\,\mathrm m$. Demuestra que $\omega_1=\pi/2\,\mathrm{s^{-1}}$ y $\omega_2=5\pi/2\,\mathrm{s^{-1}}$ producen exactamente los mismos valores en esos instantes. Encuentra una observación entre cero y un segundo que los distinga. Si la masa es un kilogramo, ¿qué rigidez correspondería a cada modelo?

### 19. Un control uniforme de la preparación {#ejercicio-10-19}

Dos soluciones del mismo oscilador tienen diferencias iniciales $\Delta q_0$ y $\Delta v_0$. Demuestra que, para todo tiempo,

$$
|\Delta q(t)|\leq\sqrt{(\Delta q_0)^2+(\Delta v_0/\omega)^2},
\qquad
|\Delta v(t)|\leq\omega\sqrt{(\Delta q_0)^2+(\Delta v_0/\omega)^2}.
$$

Evalúa estas cotas para $\omega=2\,\mathrm{s^{-1}}$, $|\Delta q_0|\leq0{,}001\,\mathrm m$ y $|\Delta v_0|\leq0{,}002\,\mathrm{m/s}$.

### 20. Un pequeño error de frecuencia se acumula {#ejercicio-10-20}

Compara $q_1=A\cos(\omega t)$ y $q_2=A\cos((\omega+\delta\omega)t)$, con $A>0$, $\omega>0$ y $\omega+\delta\omega>0$. Deduce una cota para $|q_2-q_1|$ que muestre su dependencia temporal. Con $\omega=2\,\mathrm{s^{-1}}$ y $\delta\omega=0{,}002\,\mathrm{s^{-1}}$, encuentra un intervalo en que garantice error no mayor que $0{,}01A$. Examina además $t=\pi/(0{,}002\,\mathrm{s^{-1}})$.

## Soluciones

### 1. Soltar desde el reposo {#solucion-10-1}

La frecuencia angular es $\omega=\sqrt{18/0{,}5}\,\mathrm{s^{-1}}=6\,\mathrm{s^{-1}}$. Como la velocidad inicial es cero, el coeficiente del seno se anula y $q(t)=(0{,}10\,\mathrm m)\cos(6t/\mathrm s)$. El dato de reposo inicial simplificó la fase; no corresponde imponerlo en todos los problemas de resorte.

El período es $T=2\pi/6\,\mathrm s=\pi/3\,\mathrm s$. La rapidez máxima vale $\omega A=0{,}60\,\mathrm{m/s}$ y se alcanza al cruzar el equilibrio. La energía es $kA^2/2=(18)(0{,}10)^2/2\,\mathrm J=0{,}09\,\mathrm J$. La aceleración inicial es negativa y el primer movimiento sale hacia el equilibrio, como exige la fuerza del resorte.

### 2. Comenzar cruzando el equilibrio {#solucion-10-2}

La posición inicial nula elimina el coseno. Con $\omega=3\,\mathrm{s^{-1}}$, queda $q(t)=(-0{,}20\,\mathrm m)\sin(3t/\mathrm s)$ y la amplitud es $0{,}20\,\mathrm m$. En la convención del coseno podemos escribir $q=A\cos(\omega t+\pi/2)$: esa fase da posición cero y velocidad inicial negativa.

El primer extremo negativo ocurre cuando $\sin(3t/\mathrm s)=1$, en $t=\pi/6\,\mathrm s$. El siguiente cruce del equilibrio ocurre en $t=\pi/3\,\mathrm s$, con velocidad positiva de $0{,}60\,\mathrm{m/s}$. Es medio período después del estado inicial: la posición se repite, pero la velocidad tiene el signo contrario. Un registro de posición sin dirección no distinguiría esos dos cruces.

### 3. Resolver el reloj del ejemplo inicial {#solucion-10-3}

La solución tiene coeficientes de longitud $0{,}12$ y $0{,}16\,\mathrm m$, de modo que

$$
A=\sqrt{0{,}12^2+0{,}16^2}\,\mathrm m=0{,}20\,\mathrm m.
$$

Para escribirla como $A\cos(\omega t-\delta)$ necesitamos $\cos\delta=3/5$ y $\sin\delta=4/5$; ambas son positivas y determinan $\delta=\arctan(4/3)\approx0{,}92730$.

La fase inicial es $-\delta$. Al avanzar hasta cero, el carro llega al extremo positivo y se detiene por primera vez. Por tanto, $t_1=\delta/\omega\approx0{,}46365\,\mathrm s$. Después la fase llega a $\pi/2$ y la posición se anula: $t_2=(\delta+\pi/2)/\omega\approx1{,}24905\,\mathrm s$. Allí $\dot x=-\omega A=-0{,}40\,\mathrm{m/s}$, hacia la izquierda. Tomar un cuarto de período desde la preparación habría ignorado que no partimos desde un extremo ni desde el equilibrio.

### 4. Distinguir hertz de radianes por segundo {#solucion-10-4}

Dos ciclos por segundo corresponden a $\omega=2\pi f=4\pi\,\mathrm{s^{-1}}$, no a dos radianes por segundo. La constante del resorte resulta

$$
k=m\omega^2=(0{,}20\,\mathrm{kg})(16\pi^2\,\mathrm{s^{-2}})
=3{,}2\pi^2\,\mathrm{N/m}.
$$

La amplitud se convierte a metros: $A=0{,}03\,\mathrm m$. Así, $v_{\max}=0{,}12\pi\,\mathrm{m/s}\approx0{,}377\,\mathrm{m/s}$ y $E=kA^2/2=0{,}00144\pi^2\,\mathrm J\approx0{,}0142\,\mathrm J$. Omitir el factor $2\pi$ alteraría la rigidez por un factor $4\pi^2$, incluso si todas las unidades parecieran consistentes.

### 5. Recorrer la mitad de la amplitud {#solucion-10-5}

El dato inicial da $q=A\cos(\omega t)$. Durante la primera bajada desde $A$ hasta cero, la fase crece de cero a $\pi/2$. La ecuación $\cos(\omega t)=1/2$ tiene en ese tramo la única solución $\omega t=\pi/3$. Por tanto, $t=\pi/(3\omega)=T/6$.

La velocidad es $\dot q=-\omega A\sin(\pi/3)=-\sqrt3\,\omega A/2$. Su signo identifica el regreso hacia el equilibrio. El intervalo no es la mitad de un cuarto de período: la rapidez varía, y el movimiento dedica más tiempo a regiones cercanas al extremo, donde comienza con rapidez cero.

### 6. Una rapidez deja dos estados posibles {#solucion-10-6}

La frecuencia angular es $2\,\mathrm{s^{-1}}$. La amplitud depende del cuadrado de la velocidad y vale $A=\sqrt{0{,}06^2+(0{,}16/2)^2}\,\mathrm m=0{,}10\,\mathrm m$. Si la velocidad medida fuese positiva, la solución sería

$$
q_+(t)=(0{,}06\,\mathrm m)\cos(2t/\mathrm s)
+(0{,}08\,\mathrm m)\sin(2t/\mathrm s).
$$

Con velocidad negativa, el último término cambia de signo y obtenemos $q_-(t)$. Ambas tienen energía $E=kA^2/2=0{,}04\,\mathrm J$ y pasan por la posición observada en $t=0$. Para decidir cuál describe el ensayo hace falta el sentido de movimiento. La conservación de energía deja precisamente esa información fuera de su ecuación.

### 7. Una proporción entre energías {#solucion-10-7}

Desde el extremo positivo, $U=E\cos^2(\omega t)$ y $K=E\sin^2(\omega t)$. La condición $U=3K$ implica $\tan^2(\omega t)=1/3$. En el primer cuarto de período la fase está entre cero y $\pi/2$, y su primer valor admisible es $\pi/6$.

Resulta $t=T/12$, $q=\sqrt3 A/2$ y $\dot q=-\omega A/2$. Comprobamos $U=3E/4$ y $K=E/4$. La elección del primer instante impide usar otra raíz trigonométrica que satisfaga la proporción en un tramo posterior.

### 8. Cambiar masa y rigidez {#solucion-10-8}

La frecuencia angular cambia según $\omega_2/\omega_1=\sqrt{9/4}=3/2$, y el período según $T_2/T_1=2/3$. Con la misma amplitud, la rapidez máxima también se multiplica por $3/2$. La energía depende de $kA^2/2$ y se multiplica por nueve.

La mayor masa por sí sola tendería a alargar el período, pero la rigidez creció más que la masa en la razón relevante $k/m$. La amplitud mide un recorrido geométrico; preparar ese mismo recorrido con un resorte nueve veces más rígido requiere nueve veces la energía, aunque el período se determine mediante otra combinación de parámetros.

### 9. La longitud natural no es el equilibrio cargado {#solucion-10-9}

El equilibrio es $y_e=mg/k=(0{,}5)(10)/50\,\mathrm m=0{,}10\,\mathrm m$. Medir desde él da $q_0=-0{,}10\,\mathrm m$ y $v_0=0$. Con $\omega=\sqrt{50/0{,}5}=10\,\mathrm{s^{-1}}$,

$$
y(t)=(0{,}10\,\mathrm m)\big[1-\cos(10t/\mathrm s)\big].
$$

La mayor extensión es $0{,}20\,\mathrm m$, alcanzada por primera vez en $\pi/10\,\mathrm s$. El período completo es $T=\pi/5\,\mathrm s$. Al soltar, el resorte no ejerce fuerza, pero el peso sí; comenzar en la longitud natural no significa comenzar en un equilibrio de fuerzas. El recorrido calculado mantiene $y\geq0$, sin requerir que un resorte colgante tire en sentido contrario por compresión.

### 10. Encender una fuerza constante {#solucion-10-10}

El tirón desplaza el equilibrio a $x_e=f_0/k=0{,}10\,\mathrm m$. Respecto de ese punto el carro parte en $q_0=-0{,}10\,\mathrm m$ y en reposo. Su movimiento es

$$
x(t)=(0{,}10\,\mathrm m)\big[1-\cos(2t/\mathrm s)\big].
$$

La primera detención después de salir ocurre con fase $\pi$, en $t=\pi/2\,\mathrm s$, a $x=0{,}20\,\mathrm m$. La rapidez máxima es $\omega A=0{,}20\,\mathrm{m/s}$ y se alcanza al cruzar $x_e$. El punto de equilibrio está a mitad del recorrido y no coincide con esa primera detención. La energía cinética más la del resorte aumenta por el trabajo del tirón; la energía armónica constante corresponde al potencial efectivo referido al equilibrio desplazado.

### 11. Preparar y detener con impulsos {#solucion-10-11}

Durante el impulso ideal la posición no cambia y la velocidad salta en $J/m=0{,}40\,\mathrm{m/s}$. La evolución posterior tiene $\omega=\sqrt{8/0{,}5}=4\,\mathrm{s^{-1}}$ y es $q(t)=(0{,}10\,\mathrm m)\sin(4t/\mathrm s)$. El impulso preparó una energía $J^2/(2m)=0{,}04\,\mathrm J$.

El primer regreso al equilibrio ocurre en $t=\pi/4\,\mathrm s$, con velocidad $-0{,}40\,\mathrm{m/s}$. Para llevarla a cero se necesita otro impulso positivo de $0{,}20\,\mathrm{N\,s}$. Tras él, posición y velocidad son cero, y la unicidad de la solución implica reposo permanente mientras el modelo no cambie. Aplicar ese impulso en un extremo produciría otra preparación: allí el carro ya está momentáneamente detenido, pero el resorte todavía tiene fuerza y energía.

### 12. Un impacto que prepara la oscilación {#solucion-10-12}

La fase inicial es un choque y su balance se hace sobre proyectil y bloque. El impulso del resorte se omite sólo durante ese intervalo breve. La conservación aproximada del momento horizontal da la velocidad común $V=(0{,}20)(3)/(1{,}00)\,\mathrm{m/s}=0{,}60\,\mathrm{m/s}$. La posición sigue prácticamente en el equilibrio.

Después del impacto, la masa que oscila es un kilogramo, no la masa original del bloque. Su frecuencia angular es $\omega=\sqrt{25/1}=5\,\mathrm{s^{-1}}$, por lo que $A=V/\omega=0{,}12\,\mathrm m$ y $q(t)=(0{,}12\,\mathrm m)\sin(5t/\mathrm s)$ si reiniciamos el reloj al terminar el contacto.

La energía cinética anterior era $0{,}90\,\mathrm J$ y la inmediatamente posterior $0{,}18\,\mathrm J$. Se transformaron $0{,}72\,\mathrm J$ en el choque; los $0{,}18\,\mathrm J$ restantes son la energía del oscilador ideal posterior. Durante la oscilación ya no se conserva el momento del conjunto proyectil–bloque, porque el resorte ejerce una fuerza externa sobre ese subsistema.

La información adicional permite poner una cota a esa aproximación. Durante el impacto, $|F_s|\leq k|x|\leq0{,}025\,\mathrm N$, y por integración $|J_s|\leq0{,}00005\,\mathrm{N\,s}$. La masa final es un kilogramo, de modo que la velocidad común posterior pertenece a

$$
V\in[0{,}59995;0{,}60005]\,\mathrm{m/s}.
$$

También debemos conservar la posible posición de salida: $|q_0|\leq0{,}001\,\mathrm m$. La amplitud utiliza ambos datos, $A=\sqrt{q_0^2+(V/\omega)^2}$. Como $V$ es positivo en toda su banda,

$$
0{,}11999\,\mathrm m\leq A\leq
\sqrt{(0{,}001\,\mathrm m)^2+(0{,}12001\,\mathrm m)^2}
<0{,}120015\,\mathrm m.
$$

La banda es una envolvente segura: combina todas las cotas disponibles y puede incluir pares de posición y velocidad que un contacto concreto no produzca. El valor inicial $0{,}12\,\mathrm m$ queda así acompañado por una estimación de lo que se omitió. Una duración breve adquiere utilidad física al combinarse con una cota de fuerza y con la tolerancia de la amplitud que queremos predecir.

### 13. Ambos extremos pueden moverse {#solucion-10-13}

La extensión positiva ejerce fuerza hacia la derecha sobre la primera masa y hacia la izquierda sobre la segunda. Sus ecuaciones son $m_1\ddot r_1=kq$ y $m_2\ddot r_2=-kq$. Al restarlas en el orden que define $q$ obtenemos

$$
\ddot q=\ddot r_2-\ddot r_1
=-k\left(\frac1{m_2}+\frac1{m_1}\right)q.
$$

La masa reducida es $\mu=m_1m_2/(m_1+m_2)=3/4\,\mathrm{kg}$ y la frecuencia relativa $\omega=\sqrt{k/\mu}=4\,\mathrm{s^{-1}}$. Los datos dan $q(t)=(0{,}20\,\mathrm m)\cos(4t/\mathrm s)$.

El centro de masa permanece fijo porque no hay fuerza externa horizontal y parte del reposo. Su posición es $R=3(L+0{,}20\,\mathrm m)/4$. Resolver conjuntamente $r_2-r_1=L+q$ y $m_1r_1+m_2r_2=(m_1+m_2)R$ da

$$
r_1=R-\frac34(L+q),\qquad
r_2=R+\frac14(L+q).
$$

La separación es $L+q(t)\geq L-0{,}20\,\mathrm m>0$: la hipótesis sobre $L$ conserva el orden de las masas durante todo el movimiento. Las amplitudes respecto de las posiciones de equilibrio son $0{,}15$ y $0{,}05\,\mathrm m$. Las masas se mueven en sentidos opuestos, y las amplitudes ponderadas satisfacen $1(0{,}15)=3(0{,}05)$, en kilogramos metro. La energía es $k(0{,}20\,\mathrm m)^2/2=0{,}24\,\mathrm J$. Usar $\sqrt{k/m_1}$ habría supuesto inmóvil el otro extremo y habría descrito otro sistema.

### 14. Dos resortes restauran el mismo desplazamiento {#solucion-10-14}

Una vez restadas las fuerzas que se compensan en el equilibrio, cada resorte aporta una variación $-k_iq$. Por tanto, la fuerza neta es $-(k_1+k_2)q$ y la rigidez efectiva es $16\,\mathrm{N/m}$. Esto utiliza la geometría especificada de apoyos fijos: no es una regla para sumar cualquier par de resortes en cualquier conexión.

Con masa de un kilogramo, $\omega=4\,\mathrm{s^{-1}}$ y $T=\pi/2\,\mathrm s$. La solución es $q(t)=(0{,}05\,\mathrm m)\cos(4t/\mathrm s)$ y la energía sobre su valor en el equilibrio es $E=16(0{,}05)^2/2\,\mathrm J=0{,}02\,\mathrm J$. Las posibles deformaciones previas cambian la energía de referencia, pero no esta variación cuadrática si ambos resortes mantienen su comportamiento lineal.

### 15. Un péndulo y el error de la fuerza aproximada {#solucion-10-15}

La ecuación aproximada tiene $\omega=\sqrt{10}\,\mathrm{s^{-1}}$. Los datos proporcionan

$$
\theta_h(t)=0{,}10\cos(\sqrt{10}\,t/\mathrm s),
$$

con período $T_h=2\pi/\sqrt{10}\,\mathrm s\approx1{,}987\,\mathrm s$.

Para $\theta\geq0$, la identidad $\theta-\sin\theta=\int_0^\theta(1-\cos u)\,du$ permite acotar la diferencia. Como $1-\cos u=2\sin^2(u/2)\leq u^2/2$, integrar da $0\leq\theta-\sin\theta\leq\theta^3/6$. La simetría impar extiende el resultado a valores negativos con valores absolutos.

Para $0<|\theta|\leq0{,}10$, dividir por $|\theta|$ da una discrepancia relativa respecto del término lineal no mayor que $\theta^2/6\leq1/600\approx0{,}00167$; en cero ambas fuerzas restauradoras se anulan y la comparación se interpreta por continuidad. Es una cota de los términos de la ecuación en una misma posición angular. Para convertirla en una cota de trayectoria o período hace falta analizar la evolución, de modo que no podemos atribuir al período ese porcentaje sin otro argumento.

### 16. Un resorte que no es exactamente lineal {#solucion-10-16}

Un potencial con referencia cero en el origen es $U(q)=kq^2/2+\beta q^4/4$, porque $-U'(q)=-kq-\beta q^3$. La energía inicial es

$$
E=\frac12(9\,\mathrm{N/m})(0{,}10\,\mathrm m)^2
+\frac14(9\,\mathrm{N/m^3})(0{,}10\,\mathrm m)^4
=0{,}045225\,\mathrm J.
$$

El potencial es par y estrictamente creciente con $|q|$ para $|q|>0$. Como la energía cinética es no negativa y $E=U(0{,}10\,\mathrm m)$, la trayectoria no puede alcanzar $|q|>0{,}10\,\mathrm m$. La energía también acota la velocidad. El enunciado supone que la solución está definida hasta dos segundos; el confinamiento permite usar en todo ese intervalo una única cota del término que se omitió.

La ecuación puede escribirse $\ddot q+(3\,\mathrm{s^{-1}})^2q=r(t)$, con $r=-\beta q^3/m$. El confinamiento recién probado da $|r|\leq0{,}009\,\mathrm{m/s^2}$. El oscilador lineal tiene los mismos datos iniciales; por la estimación del capítulo,

$$
|q(t)-q_h(t)|\leq
\frac{0{,}009\,\mathrm{m/s^2}}{3\,\mathrm{s^{-1}}}\,t.
$$

Hasta dos segundos la diferencia queda acotada por $0{,}006\,\mathrm m$. El término cúbico representa a lo sumo el uno por ciento del término lineal en $0<|q|\leq0{,}10\,\mathrm m$, pero esta cota conservadora de posición llega al seis por ciento de la amplitud en ese tiempo. Son magnitudes distintas; la cota no afirma que el error alcance efectivamente ese máximo.

### 17. Inferir una rigidez con cotas {#solucion-10-17}

Dividir el tiempo total por veinte da $T\in[1{,}99,2{,}01]\,\mathrm s$. En $k=4\pi^2m/T^2$, aumentar la masa aumenta $k$ y aumentar el período lo disminuye. Si no se conoce otra dependencia entre las bandas, una cota válida es

$$
k\in\left[
\frac{4\pi^2(0{,}99\,\mathrm{kg})}{(2{,}01\,\mathrm s)^2},
\frac{4\pi^2(1{,}01\,\mathrm{kg})}{(1{,}99\,\mathrm s)^2}
\right].
$$

Los extremos valen aproximadamente $9{,}674$ y $10{,}069\,\mathrm{N/m}$. Conservar la banda evita presentar la rigidez inferida como un valor exacto de $\pi^2\,\mathrm{N/m}$. Contar más ciclos puede reducir el efecto de una cota fija del cronómetro por ciclo, pero no reduce por ese mecanismo la incertidumbre de la masa ni verifica la idealización lineal.

### 18. Dos frecuencias, el mismo registro {#solucion-10-18}

Las soluciones son $q_1(t)=(0{,}10\,\mathrm m)\cos(\pi t/(2\,\mathrm s))$ y $q_2(t)=(0{,}10\,\mathrm m)\cos(5\pi t/(2\,\mathrm s))$. Para cada entero $n\geq0$, la diferencia de fase en $t=n\,\mathrm s$ es $2\pi n$, y por periodicidad los cosenos coinciden. Ambas soluciones tienen además velocidad inicial cero.

En medio segundo, sus fases son $\pi/4$ y $5\pi/4$. Sus posiciones son respectivamente $+\sqrt2/20\,\mathrm m$ y $-\sqrt2/20\,\mathrm m$, por lo que esa observación las distingue. Para una masa de un kilogramo, las rigideces serían $k_1=\pi^2/4\,\mathrm{N/m}$ y $k_2=25\pi^2/4\,\mathrm{N/m}$. La coincidencia en la malla temporal no identifica una única fuerza restauradora; el segundo movimiento completa un ciclo adicional entre muestras consecutivas.

### 19. Un control uniforme de la preparación {#solucion-10-19}

La diferencia de dos soluciones de la misma ecuación satisface de nuevo la ecuación armónica. Sus coeficientes iniciales son $\Delta q_0$ y $\Delta v_0/\omega$, por lo que su amplitud es $A_\Delta=\sqrt{(\Delta q_0)^2+(\Delta v_0/\omega)^2}$. Aplicar los máximos ya demostrados da $|\Delta q|\leq A_\Delta$ y $|\Delta v|\leq\omega A_\Delta$ para todo tiempo.

Con las cotas indicadas, ambos coeficientes de longitud tienen módulo no mayor que $0{,}001\,\mathrm m$. Así, $|\Delta q(t)|\leq\sqrt2\,0{,}001\,\mathrm m\approx0{,}001414\,\mathrm m$ y $|\Delta v(t)|\leq\sqrt2\,0{,}002\,\mathrm{m/s}\approx0{,}002828\,\mathrm{m/s}$. La comparación utiliza el mismo equilibrio y los mismos parámetros del oscilador. El resultado no cubre una frecuencia ligeramente distinta, que cambiaría la ecuación que satisface la diferencia.

### 20. Un pequeño error de frecuencia se acumula {#solucion-10-20}

La identidad de diferencia de cosenos da

$$
q_2-q_1=-2A\sin\big((\omega+\delta\omega/2)t\big)
\sin(\delta\omega\,t/2).
$$

Usando $|\sin u|\leq\min(1,|u|)$ resulta $|q_2-q_1|\leq\min(2A,A|\delta\omega|t)$ para $t\geq0$. Para garantizar una discrepancia no mayor que $0{,}01A$ basta $|\delta\omega|t\leq0{,}01$. Con el valor dado obtenemos $0\leq t\leq5\,\mathrm s$. Es una garantía suficiente, no una afirmación de que el error aumente monótonamente o exceda la tolerancia inmediatamente después de cinco segundos.

En $t=\pi/(0{,}002\,\mathrm{s^{-1}})=500\pi\,\mathrm s$, la fase del primer movimiento es $1000\pi$ y la del segundo $1001\pi$. Sus posiciones son $+A$ y $-A$; la diferencia alcanza $2A$. Una variación relativa de frecuencia de sólo una milésima permite esta oposición tras muchos ciclos. La cota uniforme del problema anterior y este desfase no se contradicen: el primero compara datos iniciales dentro de una misma dinámica; el segundo compara dos dinámicas distintas.

## Lecturas de apoyo

La interpretación de fuerza restauradora procede de [«Fuerzas y leyes de Newton»](04_Fuerzas_y_leyes_de_Newton.md); el control mediante energía se apoya en [«Trabajo y energía cinética»](07_Trabajo_y_energia_cinetica.md) y [«Potencial, equilibrio y estabilidad»](08_Potencial_equilibrio_y_estabilidad.md). El impulso que prepara una oscilación y la reducción de dos masas utilizan [«Impulso, colisiones y centro de masa»](09_Impulso_colisiones_y_centro_de_masa.md). Las cotas y la identificación de un modelo por observaciones retoman [«El problema de medir»](00_La_medida_fisica.md). La solución, su unicidad y la estimación del residuo se justifican localmente, sin presuponer un curso general de ecuaciones diferenciales.

El contraste selectivo con los clásicos comprende Young y Freedman, *Sears y Zemansky. Física universitaria*, volumen 1, 13.ª edición (Pearson, 2013), §14.2, pp. 439–442; Serway y Jewett, *Física para ciencias e ingeniería*, volumen 1, 10.ª edición española (Cengage, 2019), §15.2, pp. 388–389; y Spivak, *Physics for Mathematicians. Mechanics I* (2010), comienzo del capítulo 8, p. 287. Los problemas, las pruebas y los diagramas de este capítulo son desarrollos propios. La elección de seno o coseno como convención de fase puede variar entre libros; las condiciones iniciales permiten traducir entre ellas.

---

[← 9. Impulso, colisiones y centro de masa](fisica-para-matematicos-09-impulso-colisiones-y-centro-de-masa.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [11. Disipación y respuesta forzada →](fisica-para-matematicos-11-disipacion-y-respuesta-forzada.md)
