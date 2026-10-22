---
title: "Fuerzas elementales y diagramas de cuerpo libre"
subtitle: "Física para matemáticos · Tomo I · Capítulo 10"
author: "A. Peña"
description: "Capítulo 10 del Tomo I de Física para matemáticos, con ejercicios y soluciones desarrolladas."
archived-content-id: MA-BCH-0350
source-id: FISPM-T1-C10
editorial-id: FPM-I-10
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
date-modified: 2026-10-17
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0349"]
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
archive: true
edition: v04
search: false
sitemap: false
listing: false
---

::: {.callout-note}
## Edición archivada · v04

Esta página conserva la edición de 17 de octubre de 2026. La [edición canónica revisada](/libros/para-matematicos/fisica-para-matematicos.html) reúne los capítulos 0–27 y sus soluciones.
:::

[Capítulo 9](fisica-para-matematicos-capitulo-9-leyes-de-newton-y-estructura-de-la-dinamica.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos-v04-archivo.md#tomo-i-fundamentos-y-mecanica) · [Capítulo 11](fisica-para-matematicos-capitulo-11-restricciones-elementales-y-grados-de-libertad.md)

[]{#fispm-c10-fuerzas-elementales-y-diagramas-de-cuerpo-libre}

El capítulo 9 estableció cómo una resultante determina la aceleración y bajo qué hipótesis puede hablarse de una evolución única. Ahora debemos construir esa resultante a partir de una situación física. Trabajaremos con partículas de masa constante y marcos inerciales, salvo indicación explícita. Las fuerzas elementales serán leyes e idealizaciones del modelo, no consecuencias deducidas de Newton sin información sobre la interacción.

[]{#elegir-el-cuerpo-antes-de-dibujar-fuerzas}

[]{#fispm-t1-c10-s01}

[]{#fpm-i-10-s01}

## 1. Elegir el cuerpo antes de dibujar fuerzas {#fispm-c10-elegir-el-cuerpo-antes-de-dibujar-fuerzas}

Un objeto se apoya sobre una mesa y una mano lo tira mediante una cuerda. La escena contiene mesa, objeto, cuerda, mano y Tierra. Un dibujo de toda la escena ayuda a entender qué ocurre, pero no es todavía la herramienta que necesitamos para escribir una ecuación de Newton. Esa ecuación debe tener un receptor definido. Si mezclamos fuerzas sobre el objeto con fuerzas sobre la mano, la suma dejará de representar la resultante de un cuerpo particular.

El primer paso es elegir qué queremos determinar. Para calcular la aceleración del objeto, lo tomamos como sistema. Para estudiar cuánto se estira la cuerda, la cuerda tendría que entrar en la descripción con variables adicionales. Para averiguar la fuerza que recibe la mano, cambiamos de receptor. Cada elección conserva la misma escena física y cambia la lista de fuerzas que corresponde escribir.

[]{#fispm-t1-c10-d0001}

**Definición 10.1 --- Diagrama de cuerpo libre.** Un diagrama de cuerpo libre representa un sistema seleccionado y las fuerzas externas que actúan sobre él, con dirección, sentido y receptor identificables. En el modelo puntual, cada contribución se representa por un vector asociado al punto que sustituye al cuerpo. El dibujo no incluye como fuerzas las que ese sistema ejerce sobre cuerpos externos.

«Libre» significa aquí separado gráficamente de su entorno; no significa sin interacciones. Una partícula libre en el sentido del capítulo 9 carecía de interacciones relevantes. Un cuerpo representado en un diagrama de cuerpo libre puede tener muchas. La coincidencia de la palabra no identifica ambos conceptos.[^1]

Una lista de agentes proporciona un control eficaz. En el ejemplo, la Tierra ejerce la fuerza gravitatoria, la mesa una fuerza de contacto y la cuerda una fuerza de tracción. La mano no debe añadirse otra vez como una fuerza directa sobre el objeto si sólo actúa sobre él mediante la cuerda y no lo toca. La historia causal de una intervención no coincide con la lista de agentes que interactúan directamente con el receptor en el modelo.

[]{#fispm-t1-c10-p0001}

**Proposición 10.1 --- Componentes y agentes no multiplican interacciones.** Si sobre un receptor actúan contribuciones $\mathbf F_1,\ldots,\mathbf F_k$, representarlas por sus componentes en una base fija no añade nuevas fuerzas a la resultante. Tampoco pertenece a esa resultante la pareja de tercera ley que actúa sobre otro receptor.

**Demostración.** Si $\mathbf F_\alpha=\sum_i F_{\alpha i}e_i$, la linealidad de la suma da $\sum_\alpha\mathbf F_\alpha=\sum_i(\sum_\alpha F_{\alpha i})e_i$. Las componentes son otra representación de las mismas contribuciones; sumarlas además de los vectores originales duplicaría términos. La última afirmación sigue de que una resultante sobre un sistema sólo incluye fuerzas cuyo receptor pertenece a él, como establecieron definición 10.4 y proposición 10.4 del capítulo 9. $\square$

En un modelo de partícula no podemos usar el punto de aplicación para estudiar el efecto de giro de una fuerza: no hemos incluido orientación del cuerpo ni dinámica rotacional. Para las preguntas de este capítulo basta con la suma vectorial que produce la aceleración representada. La posterior distinción entre traslación y rotación exigirá conservar más información geométrica.

[]{#fispm-t1-c10-mp0001}

**Principio metodológico 10.1 --- Seleccionar el receptor y enumerar agentes.** Antes de dibujar flechas, escribe el nombre del sistema y de cada agente externo que actúa sobre él. Una fuerza debe tener una interacción que la justifique; una velocidad, una aceleración o la intención de mover el cuerpo no constituyen agentes adicionales.

[]{#ejercicios}

### Ejercicios {#fispm-c10-ejercicios}

[]{#fispm-t1-c10-e0001}

[]{#fispm-t1-c10-e0010}

**Ejercicio 10.1.** Una caja se apoya en una mesa horizontal y una persona la tira mediante una cuerda. No hay contacto directo persona--caja. Se desprecia la influencia del aire. Identifica los agentes de fuerza sobre la caja y sobre la cuerda. ¿La fuerza de la caja sobre la mesa debe aparecer en el diagrama de la caja?

**Solución.** Sobre la caja actúan la Tierra, la mesa y la cuerda. Sobre la cuerda actúan la persona y la caja; la Tierra también debe incluirse si su peso no se ha despreciado. Declarar una cuerda de peso despreciable elimina esa contribución del modelo, no demuestra que no exista en una cuerda real. La fuerza de la caja sobre la mesa tiene como receptor a la mesa y no pertenece al diagrama de la caja. Su pareja es la fuerza de la mesa sobre la caja, que sí debe aparecer. El inventario precede al cálculo de magnitudes, que todavía desconocemos.

[]{#fispm-t1-c10-e0002}

**Ejercicio 10.2.** Un estudiante dibuja sobre un objeto el peso $m\mathbf g$, sus dos componentes cartesianas y una flecha adicional denominada «fuerza de movimiento» en el sentido de la velocidad. Localiza los errores y repara el diagrama.

**Solución.** El peso y sus componentes representan una sola contribución, no tres. Podemos dibujar el vector peso o dibujar sus componentes indicando que son una descomposición, pero no sumarlos conjuntamente. La flecha «fuerza de movimiento» no tiene agente ni ley de interacción y debe retirarse. Si se desea señalar velocidad, se usa una marca distinguible y se declara que no pertenece a la suma de fuerzas. La reparación no necesita que el objeto esté en reposo: un cuerpo puede conservar una velocidad no nula sin una resultante en ese sentido.

[]{#del-diagrama-a-las-ecuaciones}

[]{#fispm-t1-c10-s02}

[]{#fpm-i-10-s02}

## 2. Del diagrama a las ecuaciones {#fispm-c10-del-diagrama-a-las-ecuaciones}

Un diagrama permite ver direcciones y detectar omisiones, pero no resuelve automáticamente el problema. Después de identificar contribuciones debemos expresar sus componentes, incluir las condiciones cinemáticas admitidas y comprobar que disponemos de información suficiente para las incógnitas. Algunas magnitudes provienen de una ley calibrada; otras se determinan como fuerzas de contacto necesarias para mantener un movimiento permitido.

Elegir ejes no cambia las fuerzas. Cambia la facilidad con que se escriben sus componentes. En una mesa horizontal suele convenir separar direcciones horizontal y vertical; en un plano inclinado, direcciones tangente y normal al plano. En ambos casos usaremos una base ortonormal fija del marco inercial. Una base ligada a una superficie curva y que varía con la posición requeriría el cálculo adicional del capítulo 8.

[]{#fispm-t1-c10-d0002}

**Definición 10.2 --- Componente firmada de una fuerza.** Respecto de una dirección unitaria fija $e_i$, la componente de $\mathbf F$ es $F_i=\mathbf F\cdot e_i$. Puede ser positiva, negativa o cero; la magnitud $\|\mathbf F\|$ es no negativa. Para una base ortonormal completa, $\mathbf F=\sum_iF_i e_i$.

[]{#fispm-t1-c10-p0002}

**Proposición 10.2 --- Ecuaciones por proyección.** Para una partícula de masa constante $m>0$, la ecuación $m\mathbf a=\sum_\alpha\mathbf F_\alpha$ equivale, en una base ortonormal fija, a $$ma_i=\sum_\alpha\mathbf F_\alpha\cdot e_i$$ para cada componente $i$.

**Demostración.** Tomar el producto escalar de la igualdad vectorial con cada $e_i$ proporciona las ecuaciones. Recíprocamente, si todas las componentes coinciden, la diferencia entre ambos vectores tiene producto escalar cero con cada elemento de la base. Sus coeficientes son todos cero y la diferencia es nula. $\square$

Un dibujo esquemático no fija por sí solo magnitudes ni igualdad entre ellas. Dos flechas de longitud semejante pueden representar fuerzas desconocidas. Si la longitud se usa como escala cuantitativa hay que declararlo; en los diagramas del capítulo las longitudes son esquemáticas y las direcciones constituyen la información que debe leerse. Las magnitudes se obtienen de las ecuaciones y las hipótesis.

También hay que distinguir una ecuación dinámica de una condición sobre el movimiento. Escribir $a_y=0$ exige una razón: por ejemplo, que el objeto permanezca a una altura constante durante un intervalo. Tener $v_y=0$ en un instante no basta para inferir $a_y=0$, como mostró capítulo 9. Del mismo modo, si dos objetos tienen la misma aceleración, esa igualdad debe provenir de una relación cinemática o de la solución, no de haberlos dibujado cerca.

[]{#fispm-t1-c10-mp0002}

**Principio metodológico 10.2 --- Separar dibujo, ley y condición cinemática.** Cada término de una ecuación debe proceder de una contribución del diagrama o de una condición declarada. Después de resolver, comprueba signos, dimensiones y admisibilidad del régimen supuesto, además de la igualdad algebraica.

No existe una garantía general de que los problemas de fuerzas produzcan sistemas lineales. Los ejemplos iniciales sí lo harán, pero una fuerza puede depender no linealmente de posición o velocidad, y las condiciones de contacto pueden introducir desigualdades. La estructura del capítulo 9 seguirá siendo necesaria cuando el dibujo desemboque en una ecuación diferencial en vez de una lista de números.

[]{#ejercicios-1}

### Ejercicios {#fispm-c10-ejercicios-1}

[]{#fispm-t1-c10-e0003}

**Ejercicio 10.3.** Sobre una partícula de $2\,\mathrm{kg}$ actúan dos fuerzas, $(6,-2)\,\mathrm N$ y $(-2,8)\,\mathrm N$, en una base ortonormal fija. Calcula la aceleración por proyecciones. Si la velocidad instantánea es $(-3,0)\,\mathrm{m\,s^{-1}}$, ¿debe cambiarse el sentido de alguna fuerza?

**Solución.** Las componentes de la resultante son $(4,6)\,\mathrm N$, de modo que $a_x=2\,\mathrm{m\,s^{-2}}$ y $a_y=3\,\mathrm{m\,s^{-2}}$. La velocidad indicada no obliga a cambiar ninguna fuerza: el dato de velocidad y las interacciones tienen papeles diferentes. La aceleración horizontal positiva modifica una velocidad inicialmente negativa; no supone que la partícula ya se mueva a la derecha. Para decidir una evolución posterior habría que conocer las leyes y los datos completos, no sólo estos valores instantáneos.

[]{#fispm-t1-c10-e0004}

**Ejercicio 10.4.** Se sabe que en una dirección $e_y$ el objeto tiene $v_y(t_0)=0$. Un informe reemplaza inmediatamente la ecuación vertical por $\sum F_y=0$. Da un contraejemplo y formula una condición que sí permita esa sustitución durante un intervalo.

**Solución.** Una historia $y(t)=y_0+\tfrac12A(t-t_0)^2$, con $A\ne0$, tiene velocidad vertical cero en $t_0$ y aceleración vertical $A$. Su resultante vertical es $mA$, no cero. Si en cambio se declara que $y(t)=y_0$ durante un intervalo, entonces $y'=y''=0$ en él y la segunda ley sí exige $\sum F_y=0$. La reparación consiste en aportar la condición temporal que falta, por ejemplo la permanencia en un soporte fijo, y luego comprobar que la fuerza de contacto obtenida permite esa permanencia.

[]{#gravedad-uniforme-y-peso}

[]{#fispm-t1-c10-s03}

[]{#fpm-i-10-s03}

## 3. Gravedad uniforme y peso {#fispm-c10-gravedad-uniforme-y-peso}

Un cuerpo liberado cerca del suelo suele acelerar hacia abajo. Para describir ese movimiento en una región pequeña y durante tiempos adecuados usamos un campo gravitatorio aproximadamente uniforme. «Uniforme» significa aquí que el vector del campo se toma constante en la región y en el tiempo del problema. No significa que la gravitación tenga esa forma en todas las escalas.[^2]

[]{#fig:I-10-N01}

<figure id="fig-fpm-v04-i-10-n01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-10-N01.svg" class="lightbox" data-gallery="fpm-v04-c10"><img src="/assets/books/fispm/v04/I-10-N01.svg" alt="Caída sin contacto. Diagrama del capítulo 10; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="450" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 10.1.** Partícula en caída libre en el campo uniforme: la única fuerza es el peso $P=mg$ hacia abajo. La ausencia de apoyo significa $N=0$, aunque la partícula se aproxime al suelo. Véase §[3](#fispm-c10-gravedad-uniforme-y-peso).

</figcaption>

</figure>

[]{#fispm-t1-c10-d0003}

**Definición 10.3 --- Modelo de gravedad uniforme.** En un marco aproximadamente inercial elegido, se admite una fuerza gravitatoria $$\mathbf P=m\mathbf g,\qquad \mathbf g=-g e_y,\qquad g>0,$$ con $e_y$ vertical hacia arriba y $\mathbf g$ constante. La letra $g$ representa una aceleración, de dimensión $LT^{-2}$; $\mathbf P$ representa una fuerza, de dimensión $MLT^{-2}$.

La expresión usa la misma masa que aparece en la respuesta inercial. Esa identificación incorpora una propiedad empírica de la gravitación, no una deducción de la segunda ley. Si distinguiéramos masa gravitatoria $m_g$ de masa inercial $m_i$, escribiríamos $\mathbf P=m_g\mathbf g$ y obtendríamos $\mathbf a=(m_g/m_i)\mathbf g$ cuando sólo actuara esa contribución. Nuestro modelo adopta la identificación correspondiente a una calibración común; no la demuestra mediante cancelar símbolos iguales.

[]{#fispm-t1-c10-p0003}

**Proposición 10.3 --- Caída libre en el campo uniforme.** Si la única fuerza incluida es $m\mathbf g$, con $m>0$ constante, la aceleración es $\mathbf g$ y, dados posición y velocidad iniciales, $$\mathbf r(t)=\mathbf r_0+(t-t_0)\mathbf v_0+\tfrac12(t-t_0)^2\mathbf g.$$ La historia es única en el intervalo del modelo y su aceleración no depende de $m$.

**Demostración.** Newton da $m\mathbf r''=m\mathbf g$. Dividir por $m>0$ produce $\mathbf r''=\mathbf g$ y la reconstrucción con aceleración prescrita de la proposición 9.6 proporciona la historia y su unicidad. La cancelación de masa es válida porque definición 10.3 puso el mismo parámetro en la fuerza y en la ecuación inercial. $\square$

La caída libre no exige velocidad vertical ni velocidad dirigida hacia abajo. Un objeto lanzado hacia arriba puede estar en caída libre mientras sólo actúe la gravedad: su velocidad apunta inicialmente hacia arriba y su aceleración hacia abajo. Si el aire ejerce una fuerza relevante, el modelo de la proposición 10.3 deja de incluir todas las contribuciones y debe ampliarse.

[]{#fispm-t1-c10-d0004}

**Definición 10.4 --- Peso gravitatorio y lectura de un soporte.** Llamaremos peso gravitatorio al vector $\mathbf P=m\mathbf g$. La lectura de una balanza ideal de apoyo será la magnitud de la fuerza normal que ejerce sobre el cuerpo, en el modelo donde esa lectura se ha calibrado. Se puede denominar peso aparente a esa lectura, pero no se identificará automáticamente con $mg$.

La distinción evita una ambigüedad cotidiana: la masa puede conservarse mientras cambia la lectura del soporte por su aceleración o por otra fuerza aplicada. Una balanza que muestra «kilogramos» transforma una fuerza en una indicación mediante una calibración; no altera las dimensiones de la fuerza de contacto que mide. En §5 calcularemos esa diferencia.

[]{#fispm-t1-c10-mp0003}

**Principio metodológico 10.3 --- Declarar el campo y las contribuciones omitidas.** Usa $m\mathbf g$ como una ley aproximada con dirección y escala de validez especificadas. Antes de aplicar la solución de caída libre, comprueba que se han descartado contacto, tensión y resistencia dentro del modelo del intervalo considerado.

[]{#ejercicios-2}

### Ejercicios {#fispm-c10-ejercicios-2}

[]{#fispm-t1-c10-e0005}

**Ejercicio 10.5.** Dos cuerpos con masas $m$ y $3m$ se liberan con iguales posición y velocidad iniciales en un mismo campo uniforme, despreciando todas las otras interacciones. Compara pesos, aceleraciones e historias. ¿La conclusión permanece si sus masas gravitatorias e inerciales tienen razones diferentes?

**Solución.** Sus pesos tienen magnitudes $mg$ y $3mg$, pero ambas aceleraciones son $\mathbf g$ y las historias de la proposición 10.3 coinciden. La fuerza mayor sobre el segundo cuerpo compensa su mayor respuesta inercial en la proporción admitida por el modelo. Si las razones $m_g/m_i$ fueran diferentes, las aceleraciones serían esas razones multiplicadas por $\mathbf g$ y las historias no coincidirían en general. La independencia de masa usa una hipótesis física, no sólo el nombre «gravedad».

[]{#fispm-t1-c10-e0006}

**Ejercicio 10.6.** Un cuerpo se lanza verticalmente hacia arriba con velocidad $V>0$ desde altura $h$, bajo el modelo de la proposición 10.3. Calcula la velocidad y la altura cuando se anula la velocidad vertical por primera vez. ¿Se anula también el peso o la aceleración en ese instante?

**Solución.** Con $t_0=0$, $v_y=V-gt$ y $y=h+Vt-gt^2/2$. La velocidad se anula en $t=V/g$ y la altura es $h+V^2/(2g)$. El peso sigue siendo $-mg e_y$ y la aceleración $-g e_y$, ambos no nulos. Ese instante es reposo vertical instantáneo, no equilibrio. La fórmula describe el tramo sólo mientras persisten las hipótesis del campo uniforme y ausencia de otras fuerzas; no afirma por sí sola cómo termina el movimiento al encontrar un soporte.

[]{#contacto-normal-y-unilateralidad}

[]{#fispm-t1-c10-s04}

[]{#fpm-i-10-s04}

## 4. Contacto normal y unilateralidad {#fispm-c10-contacto-normal-y-unilateralidad}

Una superficie puede impedir que un cuerpo la atraviese sin sujetarlo a ella. Esta diferencia importa: una mesa ordinaria empuja un objeto apoyado, pero no lo atrae cuando el objeto se eleva. El contacto sin adhesión es, por tanto, una interacción que sólo puede actuar en un sentido. Su magnitud se obtiene de las ecuaciones; su signo permitido forma parte del modelo.

[]{#fig:I-10-R01}

<figure id="fig-fpm-v04-i-10-r01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-10-R01.svg" class="lightbox" data-gallery="fpm-v04-c10"><img src="/assets/books/fispm/v04/I-10-R01.svg" alt="La normal no puede tirar del cuerpo. Diagrama del capítulo 10; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="424" height="223" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 10.2.** Para un contacto unilateral ideal no adhesivo, la separación y la normal satisfacen $h\ge0$, $N\ge0$ y $hN=0$. Los estados admisibles están sobre los ejes: contacto con reacción o separación sin reacción. Véase §[4](#fispm-c10-contacto-normal-y-unilateralidad).

</figcaption>

</figure>

[]{#fispm-t1-c10-d0005}

**Definición 10.5 --- Descomposición de la fuerza de contacto.** Sea $\mathbf n$ la normal unitaria que apunta desde una superficie hacia el lado accesible al cuerpo. Escribimos la fuerza de contacto sobre éste como

$$\mathbf F_c=N\mathbf n+\mathbf f_t,\qquad \mathbf f_t\cdot\mathbf n=0.$$

La componente normal es $N\mathbf n$ y la componente tangencial es $\mathbf f_t$. En un contacto no adhesivo, $N\geq0$. Una superficie lisa ideal se modela mediante $\mathbf f_t=0$.

Que una superficie sea lisa no obliga a que la normal sea vertical. Tampoco convierte una fuerza de contacto general en una fuerza puramente normal: ésta es una idealización que debemos declarar. El nombre «normal» especifica una dirección perpendicular a la superficie local, no una dirección universal del espacio.[^3]

[]{#fispm-t1-c10-d0006}

**Definición 10.6 --- Contacto unilateral sin adhesión.** Para una superficie horizontal de altura $y_s(t)$ y un cuerpo puntual de altura $y(t)$, definimos la separación $h=y-y_s$. El modelo impone

$$h\geq0,\qquad N\geq0,\qquad Nh=0.$$

La primera condición excluye penetración. La segunda excluye tracción normal. La tercera establece que una separación positiva elimina la fuerza normal. Estas condiciones describen los tramos regulares; un choque requiere además una descripción del cambio de velocidad que aquí no estamos desarrollando.

El producto $Nh=0$ no dice que siempre haya una fuerza positiva al tocar la superficie. Permite $h=0$ y $N=0$. Tampoco determina por sí solo la evolución: necesitamos Newton y datos iniciales compatibles. En particular, observar $h=0$ en un instante no autoriza a imponer que $h$ sea constante durante un intervalo. Un objeto puede estar justo abandonando el soporte o llegando a él.

Supongamos que usamos una base inercial con $e_y$ vertical hacia arriba. Sea $A=\ddot y_s$ la aceleración del soporte y sea $C_y$ la componente vertical de las otras fuerzas, excluyendo peso y normal. La ecuación sobre el cuerpo es $m\ddot y=N-mg+C_y.$

[]{#fispm-t1-c10-p0004}

**Proposición 10.4 --- Normal durante un tramo de contacto sostenido.** Si $h=0$ durante un intervalo abierto y las posiciones son dos veces diferenciables, entonces

$$\ddot y=A,\qquad N=m(g+A)-C_y.$$

Esta rama del modelo sólo es admisible si $N\geq0$. Si $h>0$, la normal vale cero y la aceleración vertical debe calcularse sin ella.

**Demostración.** La identidad $y=y_s$ en todo el intervalo permite diferenciarla dos veces. Al sustituir $\ddot y=A$ en Newton resulta la fórmula de $N$. Su no negatividad procede de la definición 10.6 y no de una elección de eje. Para separación positiva, $Nh=0$ exige $N=0$, que debe volver a introducirse en Newton. $\square$

El orden del cálculo tiene una consecuencia práctica. Primero ensayamos el contacto sostenido; después comprobamos el signo de la fuerza obtenida. Un resultado negativo no representa una «normal hacia abajo» sobre una mesa no adhesiva. Indica que la mesa tendría que tirar del cuerpo para producir la aceleración supuesta. Hay que abandonar esa rama y resolver la dinámica sin contacto, si los datos permiten la separación. No basta con sustituir el resultado negativo por cero y conservar la aceleración del soporte: esa combinación incumpliría Newton.

En el límite $N=0$ debemos examinar los datos y la evolución posterior. Una separación inicialmente nula con velocidad relativa positiva conduce a separación. Con velocidad relativa nula, el signo de la aceleración relativa aporta información local. Cuando también ésta se anula, la continuación depende de las fuerzas y del movimiento posteriores. Las desigualdades no reemplazan ese análisis temporal.

[]{#fispm-t1-c10-mp0004}

**Principio metodológico 10.4 --- Comprobar la rama de contacto.** Distingue la igualdad cinemática que ensayas de la desigualdad física que debe satisfacer la fuerza. Resuelve la primera y comprueba la segunda. Si falla, reconstruye las ecuaciones para el régimen admisible.

[]{#ejercicios-3}

### Ejercicios {#fispm-c10-ejercicios-3}

[]{#fispm-t1-c10-e0007}

**Ejercicio 10.7.** Un objeto se encuentra a distancia positiva de una mesa fija. En un instante su velocidad apunta hacia abajo. Sólo actúa la gravedad mientras permanece separado. Determina la normal y la aceleración. ¿La dirección de su velocidad basta para incorporar la mesa al diagrama?

**Solución.** Como $h>0$, definición 10.6 da $N=0$. Newton da $\ddot y=-g$. La mesa puede ser relevante para un evento futuro, pero aún no ejerce una fuerza de contacto dentro del modelo. Si la trayectoria alcanza $h=0$, termina este tramo y habrá que describir el encuentro. Añadir una normal anticipada modificaría indebidamente la aceleración antes del contacto. El diagrama representa las interacciones actuales, aunque la solución también permita predecir cuándo cambia su lista.

[]{#fispm-t1-c10-e0008}

**Ejercicio 10.8.** Una plataforma comienza con un cuerpo apoyado, separación y velocidad relativa nulas. Durante el intervalo siguiente su aceleración vertical es $A=-2g$. No hay otras fuerzas. Decide si puede conservarse el contacto y calcula la separación inicial posterior al cambio.

**Solución.** La rama sostenida produciría $N=m(g-2g)=-mg$, inadmisible. Sin contacto, el cuerpo tiene aceleración $-g$ y la plataforma $-2g$, por lo que $\ddot h=g$. Con $h(0)=\dot h(0)=0$, resulta $h(t)=gt^2/2>0$ para $t>0$. Esta trayectoria verifica la rama separada y confirma $N=0$. Si conserváramos $\ddot y=-2g$ después de fijar $N=0$, Newton exigiría una fuerza adicional que no está presente.

[]{#normal-peso-aparente-y-fuerzas-oblicuas}

[]{#fispm-t1-c10-s05}

[]{#fpm-i-10-s05}

## 5. Normal, peso aparente y fuerzas oblicuas {#fispm-c10-normal-peso-aparente-y-fuerzas-oblicuas}

La lectura de un soporte depende de cuánto debe empujar para acompañar el movimiento requerido. El peso gravitatorio sigue siendo $mg$ en el campo uniforme del modelo, mientras que la normal puede ser mayor, menor o nula. Esta distinción permite interpretar una balanza en un ascensor sin alterar la ley gravitatoria.[^4]

[]{#fispm-t1-c10-p0005}

**Proposición 10.5 --- Lectura de un soporte acelerado.** Si un cuerpo mantiene contacto con un soporte horizontal cuya aceleración vertical es $A$, y sólo recibe peso y normal, la magnitud de la fuerza medida por un soporte ideal es

$$N=m(g+A).$$

La rama exige $A\geq-g$ y datos compatibles con el contacto. Para $A<-g$ no existe contacto sostenido no adhesivo bajo esas fuerzas.

**Demostración.** proposición 10.4 con $C_y=0$ da la fórmula y definición 10.6 exige $N\geq0$. Como $m>0$, esta desigualdad equivale a $A\geq-g$. La demostración usa un marco inercial: $A$ es la aceleración del cuerpo y del soporte respecto de él. $\square$

Una velocidad ascendente no implica lectura mayor. Un ascensor que sube frenando tiene aceleración descendente y puede producir una lectura menor. De igual modo, un ascensor que baja frenando tiene aceleración ascendente y produce una lectura mayor. La velocidad caracteriza cómo se desplaza; la aceleración entra en la ecuación que fija la resultante. Si la aceleración es cero, el movimiento uniforme del soporte no altera $N=mg$.

Consideremos ahora una superficie horizontal fija y lisa. Una fuerza aplicada de magnitud $F\geq0$ forma un ángulo $\varphi$ sobre la horizontal, con $0\leq\varphi<\pi/2$. Su componente vertical ayuda a sostener el cuerpo; su componente horizontal lo acelera. Mientras persiste el contacto, no hay aceleración vertical.

[]{#fig-fispm-c10-f01}

[]{#fig:FPM-I-10_DCL_01_v01}

<figure id="fig-fpm-v04-fpm-i-10-dcl-01-v01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/FPM-I-10_DCL_01_v01.svg" class="lightbox" data-gallery="fpm-v04-c10"><img src="/assets/books/fispm/v04/FPM-I-10_DCL_01_v01.svg" alt="Fuerzas sobre el cuerpo: normal hacia arriba, peso hacia abajo y fuerza aplicada. Diagrama del capítulo 10; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="612" height="428" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 10.3.** Fuerzas sobre el cuerpo: normal hacia arriba, peso hacia abajo y fuerza aplicada oblicua. Las longitudes de las flechas son esquemáticas; no representan magnitudes medidas.

</figcaption>

</figure>

[]{#fispm-t1-c10-p0006}

**Proposición 10.6 --- Tracción oblicua sobre un soporte liso.** En la rama de contacto sostenido,

$$N=mg-F\sin\varphi,\qquad a_x=\frac{F\cos\varphi}{m}.$$

La rama requiere $F\sin\varphi\leq mg$. Si $F\sin\varphi>mg$, la solución sin contacto tiene $N=0$ y $a_y=F\sin\varphi/m-g>0$, mientras siga actuando la misma fuerza.

**Demostración.** Proyectar Newton horizontalmente da $ma_x=F\cos\varphi$. Verticalmente da $0=N+F\sin\varphi-mg$ para contacto sostenido. La desigualdad se obtiene de $N\geq0$. En la rama separada se elimina la normal y Newton vertical da la aceleración indicada. Con separación y velocidad relativa inicialmente nulas, esa aceleración positiva inicia la separación. $\square$

Si $F\sin\varphi=mg$, las fuerzas verticales pueden equilibrarse con normal nula. Bajo fuerzas constantes y datos verticales nulos, el cuerpo permanece a la altura de la mesa en el modelo puntual. Éste es un caso marginal específico. No convierte todo instante de normal nula en contacto garantizado, ni elimina la necesidad de comprobar la trayectoria si las fuerzas cambian.

Una fuerza aplicada hacia abajo produce el efecto opuesto: aumenta la normal necesaria. Basta usar su componente vertical firmada en la proposición 10.4. Esta observación muestra por qué $N=mg$ no es una ley de interacción universal. Es una solución condicionada por fuerzas, orientación del soporte y aceleración normal nula.

La normal y el peso tampoco forman una pareja de tercera ley, aunque coincidan en magnitud en un caso. Ambos actúan sobre el cuerpo. La pareja del peso es la fuerza gravitatoria del cuerpo sobre la Tierra. La pareja de la normal es la fuerza que el cuerpo ejerce sobre el soporte. Sólo las fuerzas con el mismo receptor pueden compensarse dentro de su ecuación de Newton.

[]{#fispm-t1-c10-mp0005}

**Principio metodológico 10.5 --- Separar equilibrio y reciprocidad.** Para decidir si dos fuerzas se compensan, verifica que tengan el mismo receptor y suma sus vectores. Para identificarlas como pareja de tercera ley, verifica que correspondan a una misma interacción y tengan receptores distintos. La igualdad de magnitudes por sí sola no decide ninguna de esas preguntas.

[]{#ejercicios-4}

### Ejercicios {#fispm-c10-ejercicios-4}

[]{#fispm-t1-c10-e0009}

**Ejercicio 10.9.** Una balanza ideal acompaña un soporte vertical. Calcula su lectura para aceleraciones $+g/4$ y $-g/4$. Compara, además, un soporte que sube a velocidad constante con otro que baja a velocidad constante.

**Solución.** En contacto sostenido, proposición 10.5 da respectivamente $N=5mg/4$ y $N=3mg/4$. Ambos valores son admisibles. Los dos movimientos a velocidad constante tienen $A=0$ y lectura $mg$. La lectura distingue aceleraciones, no el signo de la velocidad. Los resultados suponen que el cuerpo acompaña el soporte y que éste mide exclusivamente la fuerza normal; una fuerza vertical adicional cambiaría la ecuación.

**Ejercicio 10.10.** Un cuerpo sobre una mesa lisa recibe una fuerza a $30^\circ$ sobre la horizontal. Compara $F=mg$ con $F=3mg$, partiendo en ambos casos de separación y velocidad vertical nulas.

**Solución.** Para $F=mg$, $N=mg/2$ y $a_x=\sqrt3g/2$. El contacto es admisible. Para $F=3mg$, la rama sostenida daría $N=-mg/2$ y debe rechazarse. En la rama separada, $a_y=g/2$ y $a_x=3\sqrt3g/2$. Si la fuerza permanece constante, la altura sobre la mesa aumenta como $gt^2/4$. El segundo cálculo no es una simple prolongación del primero con normal negativa: cambió la condición cinemática vertical.

[]{#plano-inclinado-sin-fricción}

[]{#fispm-t1-c10-s06}

[]{#fpm-i-10-s06}

## 6. Plano inclinado sin fricción {#fispm-c10-plano-inclinado-sin-fricciuxf3n}

El plano inclinado introduce una orientación distinta sin introducir todavía una ley de rozamiento. Sea $\theta$ su ángulo sobre la horizontal, con $0\leq\theta<\pi/2$. Elegimos una base fija adaptada al plano: $e_t$ hacia arriba de la pendiente y $e_n$ perpendicular al plano hacia el lado accesible. En una base horizontal y vertical $(e_x,e_y)$,

$$e_t=\cos\theta\,e_x+\sin\theta\,e_y,\qquad e_n=-\sin\theta\,e_x+\cos\theta\,e_y.$$

La base facilita las proyecciones, pero no cambia las fuerzas físicas. El peso sigue siendo vertical. Su expresión adaptada al plano es $\mathbf P=-mg\sin\theta\,e_t-mg\cos\theta\,e_n.$

Estas dos componentes reemplazan la representación vertical para el cálculo; no se añaden a ella como interacciones nuevas. El contacto liso aporta $N e_n$. Como el plano es fijo y recto, mantener el contacto durante un intervalo significa posición normal constante y, por tanto, aceleración normal nula. No estamos atribuyendo esa propiedad a cualquier superficie curva: allí la geometría puede exigir una aceleración normal diferente.[^5]

[]{#fig-fispm-c10-f02}

[]{#fig:FPM-I-10_DCL_02_v01}

<figure id="fig-fpm-v04-fpm-i-10-dcl-02-v01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/FPM-I-10_DCL_02_v01.svg" class="lightbox" data-gallery="fpm-v04-c10"><img src="/assets/books/fispm/v04/FPM-I-10_DCL_02_v01.svg" alt="Sobre el cuerpo actúan peso y normal. Las flechas grises indican la base y no so. Diagrama del capítulo 10; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="612" height="453" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 10.4.** Sobre el cuerpo actúan peso y normal. Las flechas grises indican la base y no son fuerzas. La inclinación dibujada es representativa; las fórmulas usan el ángulo declarado en cada problema.

</figcaption>

</figure>

[]{#fispm-t1-c10-p0007}

**Proposición 10.7 --- Movimiento sobre un plano fijo y liso.** Bajo peso y normal, en la rama de contacto sostenido,

$$N=mg\cos\theta,\qquad a_t=-g\sin\theta,\qquad a_n=0.$$

Una fuerza adicional $Qe_t$, con $Q$ firmado, cambia únicamente la ecuación tangencial: $a_t=Q/m-g\sin\theta$.

**Demostración.** Las proyecciones del peso son sus productos escalares con los dos vectores de la base. Newton normal da $0=N-mg\cos\theta$, y Newton tangencial da $ma_t=-mg\sin\theta+Q$. Para el intervalo angular elegido, $\cos\theta>0$, de modo que la normal calculada es positiva. La ausencia de componente normal de la fuerza adicional explica por qué no altera ese resultado. $\square$

La masa desaparece de la aceleración cuando sólo actúan peso y normal. No desaparece de la fuerza normal. Un cuerpo más masivo necesita una fuerza de contacto proporcionalmente mayor para impedir la aceleración hacia el plano. También debemos distinguir la magnitud del peso, $mg$, de su componente tangencial, $mg\sin\theta$. La componente tangencial no es una segunda gravedad ni una fuerza que el plano ejerce hacia abajo.

Si $s$ mide posición hacia arriba de la pendiente, entonces $\ddot s=-g\sin\theta$ para el caso sin fuerza adicional. El signo negativo fija la dirección de la aceleración, pero no la de la velocidad inicial. Un cuerpo lanzado cuesta arriba puede seguir subiendo durante un tiempo mientras su velocidad disminuye. Después del punto de retorno, baja con aceleración en el mismo sentido que antes. La fuerza no necesita invertirse en ese punto.

Una fuerza tangencial constante puede anular la aceleración si $Q=mg\sin\theta$. Ese ajuste permite reposo o velocidad constante, según los datos iniciales; no impone reposo. Si la fuerza fuera oblicua respecto del plano, habría que incluir también su componente normal y comprobar de nuevo la admisibilidad. La fórmula de la proposición 10.7 no se conserva automáticamente al cambiar esa hipótesis.

[]{#fispm-t1-c10-mp0006}

**Principio metodológico 10.6 --- Elegir una base sin duplicar fuerzas.** Escribe primero los agentes y después proyecta en una base que simplifique la geometría. Mantén visible la distinción entre vectores físicos, componentes firmadas y vectores de base. Comprueba qué condición geométrica justifica cada componente de aceleración impuesta.

[]{#ejercicios-5}

### Ejercicios {#fispm-c10-ejercicios-5}

[]{#fispm-t1-c10-e0011}

**Ejercicio 10.11.** Un cuerpo se mueve sobre un plano liso de $30^\circ$, bajo gravedad uniforme. Determina normal, aceleración tangencial y componentes horizontal y vertical de la aceleración. Comprueba que la magnitud del peso no depende de la inclinación.

**Solución.** proposición 10.7 da $N=\sqrt3mg/2$ y $a_t=-g/2$. Como $\mathbf a=a_te_t$, obtenemos $a_x=-\sqrt3g/4$ y $a_y=-g/4$. La componente vertical de la aceleración no es $-g$ porque la normal tiene componente vertical positiva. Las componentes adaptadas del peso son $-mg/2$ y $-\sqrt3mg/2$, cuya norma es $mg$. La rotación de la base conserva la norma del vector, aunque cambie sus componentes.

[]{#fispm-t1-c10-e0012}

**Ejercicio 10.12.** En el mismo plano, una fuerza tangencial constante $Q=3mg/4$ apunta cuesta arriba. El cuerpo comienza con velocidad $-Ue_t$, $U>0$. Calcula la aceleración y el primer instante de velocidad nula. ¿Cambia la normal al detenerse?

**Solución.** La aceleración tangencial es $a_t=3g/4-g/2=g/4$, y $v_t=-U+gt/4$. El primer reposo ocurre en $t=4U/g$. Hasta entonces el cuerpo baja y se frena; después sube, si sigue disponible el mismo plano y la fuerza se mantiene. La normal permanece $\sqrt3mg/2$: ni el cambio de signo de la velocidad ni el reposo instantáneo modifican la ecuación normal. El resultado presupone un tramo suficientemente largo del plano para que el cuerpo no encuentre un borde antes del tiempo calculado.

[]{#tensión-e-idealización-de-la-cuerda}

[]{#fispm-t1-c10-s07}

[]{#fpm-i-10-s07}

## 7. Tensión e idealización de la cuerda {#fispm-c10-tensiuxf3n-e-idealizaciuxf3n-de-la-cuerda}

Una cuerda permite transmitir una tracción entre cuerpos separados. Para incorporarla al diagrama necesitamos conocer la dirección de su tramo próximo al cuerpo y declarar qué propiedades de la cuerda conservamos. Una cuerda flexible ordinaria puede tirar de un extremo, pero no sostener una compresión longitudinal como una barra rígida: al intentar comprimirla, se afloja o cambia de forma.

[]{#fig:I-10-N06}

<figure id="fig-fpm-v04-i-10-n06" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-10-N06.svg" class="lightbox" data-gallery="fpm-v04-c10"><img src="/assets/books/fispm/v04/I-10-N06.svg" alt="Cuerpo suspendido. Diagrama del capítulo 10; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="360" height="284" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 10.5.** Sobre una masa colgante actúan tensión hacia la cuerda y peso hacia abajo. La ecuación vertical es $T-mg=ma_y$; sólo si $a_y=0$ resulta $T=mg$. Véase §[7](#fispm-c10-tensiuxf3n-e-idealizaciuxf3n-de-la-cuerda).

</figcaption>

</figure>

[]{#fispm-t1-c10-d0007}

**Definición 10.7 --- Tensión y fuerza de una cuerda flexible.** La tensión $T$ es una magnitud escalar no negativa que caracteriza la tracción longitudinal en una sección de la cuerda. Sobre un cuerpo unido a un extremo, la cuerda ejerce una fuerza $T\mathbf t$, donde $\mathbf t$ apunta desde el cuerpo hacia el tramo de cuerda que lo tira. En la rama floja sin otras interacciones de la cuerda con ese cuerpo, esta tracción es nula.

Las fuerzas sobre dos extremos pueden tener sentidos opuestos sin que una de las tensiones sea negativa. El signo pertenece a la componente en un eje; la tensión definida como magnitud satisface $T\geq0$. Una solución que exige tensión negativa pide a la cuerda que empuje y queda fuera de esta idealización.

[]{#fispm-t1-c10-d0008}

**Definición 10.8 --- Cuerda ideal tensa e inextensible.** En este capítulo, una cuerda ideal tiene masa despreciable frente a las masas estudiadas y longitud constante mientras está tensa. Para un tramo recto sin fuerzas tangenciales intermedias, se supone además una aceleración acotada al despreciar su masa. La igualdad de tensiones se aplica a ese tramo bajo estas condiciones; no se postula para toda cuerda real ni para cualquier dispositivo que la desvíe.

La inextensibilidad relaciona posiciones de sus extremos cuando la cuerda está tensa. La masa despreciable permite simplificar su balance de fuerzas. Son hipótesis distintas. Una cuerda puede estirarse poco y tener masa importante, o ser liviana y elástica. Confundir las dos hipótesis oculta el origen de la relación que estamos usando.[^6]

[]{#fispm-t1-c10-p0008}

**Proposición 10.8 --- Transmisión de tensión en un tramo recto liviano.** Considérese un tramo recto de masa $\mu>0$, con eje unitario $\mathbf t$ hacia la derecha. Sus fuerzas tangenciales externas son $T_R\mathbf t$ en el extremo derecho y $-T_L\mathbf t$ en el izquierdo. Si no hay otras fuerzas tangenciales,

$$T_R-T_L=\mu a_t,$$

con $a_t$ la aceleración tangencial de su centro de masa. Si se desprecia $\mu$ manteniendo $a_t$ acotada, la diferencia de tensiones tiende a cero.

**Demostración.** Dividimos el tramo en elementos de masa constante y sumamos sus ecuaciones de Newton. Las fuerzas internas se cancelan por pares. La proyección de la resultante externa es $T_R-T_L$ y la suma de masas por aceleraciones es $\mu a_t$, con $a_t=\sum_j m_j a_{jt}/\mu$, la aceleración de la posición media ponderada por las masas. Este balance elemental no requiere desarrollar todavía la teoría general del centro de masa. Para una cota $|a_t|\leq K$, se tiene $|T_R-T_L|\leq\mu K\to0$. No hemos dividido por una masa nula: hemos explicitado el límite que motiva el balance ideal. $\square$

Para un tramo que conserve su forma recta y traslade todos sus puntos con la misma aceleración, $a_t$ coincide con la de cualquier punto. La formulación mediante centro de masa permite expresar el balance sin necesitar esa condición adicional. No usaremos aquí una teoría del movimiento interno de cuerdas: el balance identifica qué se omite al reemplazar un tramo material por uno ideal.

Si una cuerda de masa apreciable cuelga verticalmente, la gravedad aporta fuerzas tangenciales distribuidas y las tensiones varían con la altura. Incluso si está en reposo, los extremos de un tramo deben sostener su peso. Si la cuerda pasa por una polea, la dirección cambia y la polea interactúa con ella. Igualar tensiones a ambos lados exige idealizaciones adicionales sobre ese dispositivo, como ausencia de resistencia y de inercia rotacional relevante. Un dibujo de una cuerda continua no sustituye esas hipótesis.

El balance del tramo también aclara la tercera ley. La cuerda tira del cuerpo; el cuerpo tira de la cuerda con una fuerza opuesta. Esa pareja tiene receptores distintos. Si una cuerda tira de dos cuerpos, las dos fuerzas que ejerce sobre ellos no constituyen entre sí una pareja de tercera ley. Cada una tiene su pareja sobre la cuerda. La igualdad de sus magnitudes procede del balance y de las hipótesis que acabamos de precisar.

[]{#fispm-t1-c10-mp0007}

**Principio metodológico 10.7 --- Declarar qué cuerda se está modelando.** Antes de igualar tensiones o relacionar aceleraciones, indica si desprecias masa y extensibilidad y si mantienes la rama tensa. Comprueba después $T\geq0$. Al cambiar de tramo o introducir un cuerpo intermedio, reconstruye el balance correspondiente.

[]{#ejercicios-6}

### Ejercicios {#fispm-c10-ejercicios-6}

[]{#fispm-t1-c10-e0013}

**Ejercicio 10.13.** Un cuerpo de masa $m$ cuelga de una cuerda vertical y tiene aceleración $A$ hacia arriba, firmada en un eje vertical ascendente. Determina la tensión y su dominio de admisibilidad cuando sólo recibe peso y tracción.

**Solución.** Newton da $T-mg=mA$, por lo que $T=m(g+A)$. La condición $T\geq0$ exige $A\geq-g$. Si $A<-g$, las dos fuerzas declaradas no permiten esa aceleración: la cuerda tendría que empujar hacia abajo. En caída libre $A=-g$, la tensión puede ser cero, pero para decidir si la cuerda sigue geométricamente tensa necesitamos también la trayectoria del otro extremo. La igualdad límite de fuerzas no determina por sí sola la configuración.

[]{#fispm-t1-c10-e0014}

**Ejercicio 10.14.** Una cuerda uniforme de longitud $\ell$ y masa total $M$ cuelga en reposo de su extremo superior; el inferior está libre. Calcula la tensión en una sección situada a distancia $x$ del extremo inferior, con $0\leq x\leq\ell$.

**Solución.** Su densidad lineal es $\rho_\ell=M/\ell$. Elegimos como sistema el tramo inferior de longitud $x$. La sección superior ejerce tracción ascendente $T(x)$ y la Tierra ejerce peso descendente $\rho_\ell xg$. Como el tramo está en reposo, $T(x)=\rho_\ell gx$. En el extremo inferior $T(0)=0$ y en el superior $T(\ell)=Mg$. No contradice proposición 10.8: aquí no se ha despreciado la masa y hay una fuerza tangencial distribuida. El corte usado para escoger el subsistema convierte la interacción con el resto de la cuerda en una fuerza externa de ese subsistema.

[]{#cuerpos-conectados-y-sistemas-compartidos}

[]{#fispm-t1-c10-s08}

[]{#fpm-i-10-s08}

## 8. Cuerpos conectados y sistemas compartidos {#fispm-c10-cuerpos-conectados-y-sistemas-compartidos}

Consideremos dos cuerpos sobre una superficie horizontal lisa y fija. El cuerpo $B$ está a la izquierda y el cuerpo $A$ a la derecha. Una cuerda recta ideal los conecta y una fuerza horizontal externa $F\geq0$ tira de $A$ hacia la derecha. Podemos escribir un diagrama por cuerpo y otro para el conjunto, pero debemos conservar la misma elección de receptores durante cada balance.

[]{#fig-fispm-c10-f03}

[]{#fig:FPM-I-10_DCL_03_v01}

<figure id="fig-fpm-v04-fpm-i-10-dcl-03-v01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/FPM-I-10_DCL_03_v01.svg" class="lightbox" data-gallery="fpm-v04-c10"><img src="/assets/books/fispm/v04/FPM-I-10_DCL_03_v01.svg" alt="Diagramas separados: sobre \(B\), la cuerda tira hacia la derecha; sobre \(A\), . Diagrama del capítulo 10; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="612" height="268" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 10.6.** Diagramas separados: sobre $B$, la cuerda tira hacia la derecha; sobre $A$, hacia la izquierda. Cada cuerpo recibe además su propio peso y normal. Las dos fuerzas rotuladas $T$ tienen receptores distintos y no forman entre sí una pareja de tercera ley.

</figcaption>

</figure>

[]{#fispm-t1-c10-p0009}

**Proposición 10.9 --- Aceleración común en una conexión recta tensa.** Si las posiciones horizontales satisfacen $x_A-x_B=\ell$ durante un intervalo, con $\ell$ constante y posiciones dos veces diferenciables, entonces $v_A=v_B$ y $a_A=a_B$ en ese intervalo.

**Demostración.** Diferenciar una vez la identidad da $v_A-v_B=0$; diferenciarla de nuevo da $a_A-a_B=0$. Las conclusiones proceden de la longitud constante en la rama tensa, no de una igualdad entre fuerzas. $\square$

Imponer la misma aceleración exige datos iniciales compatibles con esa relación. Si la cuerda está floja, las posiciones no satisfacen necesariamente esa igualdad y los cuerpos pueden acelerarse de manera diferente. La relación tampoco se aplica sin modificación a cualquier geometría con poleas: allí habría que expresar primero la longitud mediante las posiciones pertinentes. El tratamiento sistemático de tales restricciones pertenece al capítulo 11.

[]{#fispm-t1-c10-p0010}

**Proposición 10.10 --- Dos cuerpos sobre un soporte liso.** Bajo las hipótesis anteriores, masas positivas $m_A,m_B$ y datos compatibles con la rama tensa,

$$a=\frac{F}{m_A+m_B},\qquad T=\frac{m_BF}{m_A+m_B},\qquad N_A=m_Ag,\qquad N_B=m_Bg.$$

**Demostración.** proposición 10.8 permite una magnitud de tensión común para el tramo recto ideal, y proposición 10.9 una aceleración horizontal común. Newton sobre cada receptor da

$$F-T=m_Aa,\qquad T=m_Ba.$$

Al sumar, $F=(m_A+m_B)a$, y sustituir en la segunda ecuación da $T$. Los balances verticales independientes producen las normales indicadas. Para $F\geq0$, la tensión es no negativa y ambas normales positivas, por lo que las fuerzas calculadas satisfacen las condiciones de admisibilidad. $\square$

Sumar ecuaciones de cuerpos distintos es legítimo si se sabe qué expresa esa suma. En este caso cancela los términos de tracción opuestos ya justificados por la proposición 10.8. Para clasificar todas las interacciones como internas o externas, resulta especialmente claro elegir el conjunto $A+B+$ cuerda y luego despreciar la masa de ésta: las interacciones cuerpo--cuerda son internas y sus parejas se cancelan al sumar todas las ecuaciones. Si se elige sólo $A+B$, la cuerda queda fuera y sus fuerzas son externas a ese sistema, aunque su suma sea cero en el modelo ideal. «Interna» depende de la frontera elegida, no de que una contribución termine cancelándose.

La resultante $F$ determina la aceleración conjunta, pero no basta para encontrar la tensión. La ecuación de uno de los cuerpos conserva información que se pierde al sumar. Ésta es una razón para combinar perspectivas: el balance del conjunto simplifica la aceleración; el de un subsistema revela la interacción transmitida. Para $B$, la tensión es toda la resultante horizontal, mientras que para $A$ la resultante es $F-T$.

La fórmula también muestra cómo aparece un fallo de régimen. Si una fuerza firmada $F<0$ empujara a $A$ hacia $B$, el cálculo tenso produciría $T<0$. La cuerda flexible no puede suministrar esa compresión. Partiendo de longitud máxima y velocidades iguales, una solución inicial floja tiene $T=0$, $a_A=F/m_A$ y $a_B=0$: la distancia entre cuerpos disminuye. Ese tramo continúa hasta que ocurra otro evento relevante. No debemos mantener la aceleración común después de rechazar la fuerza que la hacía posible.

En una cadena vertical, dos cuerdas diferentes pueden tener tensiones diferentes incluso si cada cuerda es ideal. La cuerda superior puede sostener dos masas y la inferior una sola. Hay un cuerpo entre ellas que recibe ambas tracciones; su masa impide usar el balance de un único tramo liviano para igualarlas. El nombre común «tensión» no obliga a introducir una sola incógnita en toda la escena.

[]{#fispm-t1-c10-mp0008}

**Principio metodológico 10.8 --- Combinar balances sin borrar sus hipótesis.** Obtén las relaciones de aceleración desde la geometría declarada y las relaciones de tensión desde el modelo de cuerda. Usa el conjunto para simplificar la resultante y los cuerpos separados para recuperar las fuerzas internas. Comprueba que cada ecuación tenga un receptor inequívoco.

[]{#ejercicios-7}

### Ejercicios {#fispm-c10-ejercicios-7}

[]{#fispm-t1-c10-e0015}

**Ejercicio 10.15.** En la configuración de la proposición 10.10, $m_A=4\,\mathrm{kg}$, $m_B=6\,\mathrm{kg}$ y $F=20\,\mathrm N$. Calcula aceleración, tensión y resultante horizontal sobre cada cuerpo. Verifica los dos balances.

**Solución.** $a=20/10=2\,\mathrm{m\,s^{-2}}$ y $T=6\cdot2=12\,\mathrm N$. Sobre $A$, la resultante es $20-12=8\,\mathrm N=4\cdot2\,\mathrm N$; sobre $B$, es $12\,\mathrm N=6\cdot2\,\mathrm N$. La fuerza aplicada de $20\,\mathrm N$ no es la resultante sobre $A$, porque éste también recibe la tracción hacia la izquierda. Las normales son $4g$ y $6g$ newtons si $g$ se expresa en $\mathrm{m\,s^{-2}}$.

[]{#fispm-t1-c10-e0016}

**Ejercicio 10.16.** Dos cuerpos cuelgan en cadena vertical: $A$ arriba y $B$ abajo. Una cuerda ideal superior tira de $A$; otra, distinta, une $A$ con $B$. Ambos tienen aceleración común $\alpha$ hacia arriba, firmada. Determina las tensiones $T_U$ y $T_L$ y explica por qué no son iguales en general.

**Solución.** Sobre $B$, $T_L-m_Bg=m_B\alpha$, por lo que $T_L=m_B(g+\alpha)$. Sobre $A$, $T_U-T_L-m_Ag=m_A\alpha$. Sustituyendo,

$$T_U=(m_A+m_B)(g+\alpha).$$

Para $\alpha>-g$, ambas tensiones son positivas y $T_U-T_L=m_A(g+\alpha)>0$. La masa $A$ está entre las dos cuerdas y requiere una resultante propia. No se trata de dos extremos del mismo tramo sin fuerzas intermedias. Para $\alpha<-g$, las tensiones calculadas son negativas y la aceleración prescrita no se realiza con estas únicas fuerzas. Para $\alpha=-g$, ambas pueden anularse; la continuidad de la configuración depende además del movimiento del extremo superior y de los datos iniciales.

Con esto queda construido el núcleo de selección del sistema, gravedad, contacto liso y transmisión ideal de tracción. Las secciones siguientes incorporan fuerzas tangenciales de fricción, resistencia y elasticidad. Cada ley añadirá condiciones de aplicación propias; el método de seleccionar receptor, proyectar Newton y comprobar el régimen seguirá siendo el mismo.

[]{#fricción-estática-y-admisibilidad}

[]{#fispm-t1-c10-s09}

[]{#fpm-i-10-s09}

## 9. Fricción estática y admisibilidad {#fispm-c10-fricciuxf3n-estuxe1tica-y-admisibilidad}

Empujar suavemente un cuerpo apoyado puede no producir movimiento relativo respecto del soporte. La ausencia de ese movimiento no implica ausencia de fuerza tangencial. Si una fuerza aplicada intenta desplazar el cuerpo y éste permanece en reposo sobre una mesa fija, el balance exige una contribución que la compense. Su valor se determina por la aceleración requerida y tiene un límite dentro del modelo de contacto seco.[^7]

[]{#fig:I-10-N02}

<figure id="fig-fpm-v04-i-10-n02" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-10-N02.svg" class="lightbox" data-gallery="fpm-v04-c10"><img src="/assets/books/fispm/v04/I-10-N02.svg" alt="Rozamiento estático. Diagrama del capítulo 10; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="349" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 10.7.** En un soporte horizontal, bajo un empuje $F$ y sin aceleración, $f_s=F$ y $N=mg$. Esta rama requiere $F\le\mu_s mg$; $f_s$ no vale siempre su máximo. Véase §[9](#fispm-c10-fricciuxf3n-estuxe1tica-y-admisibilidad).

</figcaption>

</figure>

[]{#fispm-t1-c10-d0009}

**Definición 10.9 --- Modelo de fricción estática seca.** Durante un tramo sin deslizamiento tangencial relativo entre dos superficies en contacto, la fuerza tangencial $\mathbf f_s$ satisface

$$\mathbf f_s\cdot\mathbf n=0,\qquad \|\mathbf f_s\|\leq\mu_sN,$$

con $N\geq0$ y coeficiente estático $\mu_s\geq0$ adimensional. Su valor dentro de ese límite se obtiene del balance que permite el movimiento sin deslizamiento. En una dirección tangencial única, la condición es $|f_s|\leq\mu_sN$.

La definición es una aproximación macroscópica. No afirma que todos los materiales tengan un coeficiente constante bajo cualquier carga, temperatura o historia. En los problemas que siguen declararemos valores constantes para superficies y condiciones dadas. La ley aproxima lo necesario para construir un balance, sin sustituir una descripción microscópica de la interacción.

La igualdad $|f_s|=\mu_sN$ sólo corresponde al límite de admisibilidad. Para fuerzas aplicadas pequeñas, la magnitud de fricción puede ser menor, incluso cero. Usar siempre el máximo fabricaría una aceleración que no corresponde al reposo supuesto. La normal debe calcularse antes: una fuerza oblicua o un soporte acelerado pueden cambiarla, como mostraron proposiciones 10.4--10.6.

[]{#fispm-t1-c10-p0011}

**Proposición 10.11 --- Reposo sobre una mesa fija.** Un cuerpo sobre una mesa horizontal fija recibe peso, normal y una fuerza horizontal constante $Qe_x$, con $Q$ firmado. Existe un balance de reposo compatible con la definición 10.9 si y sólo si

$$|Q|\leq\mu_smg.$$

En él, $N=mg$ y $f_s=-Q$.

**Demostración.** El reposo exige ambas componentes de aceleración nulas. Newton vertical da $N=mg$ y Newton horizontal $0=Q+f_s$. Definición 10.9 exige entonces $|Q|\leq\mu_smg$, de modo que la condición es necesaria. Recíprocamente, si se cumple, elegir $N=mg$ y $f_s=-Q$ satisface Newton y las condiciones de contacto. Con posición inicial apoyada y velocidad inicial nula, la historia constante realiza ese balance. $\square$

El enunciado prueba que el reposo es admisible; no asegura que todo cuerpo sometido a ese $Q$ ya esté en reposo. Si llega deslizando, debemos usar la ley del régimen móvil y examinar si se detiene. Una misma fuerza aplicada puede coexistir con reposo en una historia y con movimiento en otra, porque los datos y el régimen difieren.

[]{#fispm-t1-c10-p0012}

**Proposición 10.12 --- Fricción estática sobre un soporte que acelera horizontalmente.** Sea un soporte horizontal que no acelera verticalmente y tiene aceleración horizontal $A$. Si el cuerpo lo acompaña sin deslizamiento, bajo peso, contacto y fuerza horizontal $Q$, entonces

$$N=mg,\qquad f_s=mA-Q.$$

El acompañamiento sólo es admisible si $|mA-Q|\leq\mu_smg$.

**Demostración.** Durante el acompañamiento, la diferencia de posiciones horizontales del cuerpo y del punto correspondiente del soporte es constante. Diferenciar dos veces da $a_x=A$. Newton horizontal exige $mA=Q+f_s$; el balance vertical mantiene $N=mg$. Sustituir la fuerza requerida en la definición 10.9 produce la desigualdad. $\square$

Si $Q=0$ y $A>0$, la fricción sobre el cuerpo apunta hacia la derecha. Puede acelerar al cuerpo en el mismo sentido que su velocidad respecto del suelo. No hay contradicción: «estática» significa sin deslizamiento relativo, y el soporte también se mueve. En los dibujos se deben distinguir la velocidad respecto del marco inercial y la velocidad respecto de la superficie. Sólo la segunda decide el régimen de contacto tangencial.

Cuando la desigualdad falla, el soporte no puede comunicar la aceleración supuesta con esa interacción. Rechazamos el acompañamiento y calculamos el deslizamiento. La situación se parece al contacto normal inadmisible de §4, pero aquí el límite afecta una componente tangencial y no implica necesariamente separación normal. El cuerpo puede seguir apoyado mientras desliza.

[]{#fispm-t1-c10-mp0009}

**Principio metodológico 10.9 --- Calcular antes de saturar.** En una rama sin deslizamiento, calcula la fricción requerida por Newton y comprueba después su límite. Identifica la superficie respecto de la cual el movimiento relativo es nulo. No reemplaces esa comprobación por una flecha siempre opuesta a la velocidad del laboratorio.

[]{#ejercicios-8}

### Ejercicios {#fispm-c10-ejercicios-8}

[]{#fispm-t1-c10-e0017}

**Ejercicio 10.17.** Sobre una mesa fija, un cuerpo inicialmente en reposo recibe una fuerza horizontal $Q=0{,}3mg$. El coeficiente estático es $\mu_s=0{,}5$. Determina un balance admisible y compara la fricción efectiva con su máximo.

**Solución.** $N=mg$ y la fricción requerida es $f_s=-0{,}3mg$. Como $0{,}3mg<0{,}5mg$, el reposo es admisible y la fricción no alcanza su máximo. Si se escribiera $f_s=-0{,}5mg$, la resultante sería $-0{,}2mg$ y el cuerpo aceleraría en sentido opuesto a la fuerza aplicada: ese resultado contradice la rama que intentábamos resolver. Al retirar $Q$, un balance de reposo tiene $f_s=0$; el coeficiente no obliga a mantener una fuerza tangencial residual.

[]{#fispm-t1-c10-e0018}

**Ejercicio 10.18.** Un cuerpo de $2\,\mathrm{kg}$ debe acompañar un soporte horizontal con aceleración $3\,\mathrm{m\,s^{-2}}$. Una fuerza externa horizontal de $2\,\mathrm N$ apunta en ese sentido. Usa $g=10\,\mathrm{m\,s^{-2}}$ y compara $\mu_s=0{,}3$ con $\mu_s=0{,}1$.

**Solución.** La fricción requerida es $f_s=2\cdot3-2=4\,\mathrm N$ y la normal $20\,\mathrm N$. Con el primer coeficiente, el máximo es $6\,\mathrm N$, de modo que el acompañamiento es admisible. Con el segundo, el máximo es $2\,\mathrm N$ y no alcanza: la rama sin deslizamiento falla. No podemos afirmar que el cuerpo tenga aceleración $3$ y asignarle arbitrariamente $2\,\mathrm N$ de fricción, porque Newton daría sólo $2\,\mathrm{m\,s^{-2}}$. Para la rama móvil necesitamos además un modelo cinético y los datos de velocidad relativa.

[]{#fricción-cinética-y-cambio-de-régimen}

[]{#fispm-t1-c10-s10}

[]{#fpm-i-10-s10}

## 10. Fricción cinética y cambio de régimen {#fispm-c10-fricciuxf3n-cinuxe9tica-y-cambio-de-ruxe9gimen}

Una vez que las superficies deslizan entre sí, el modelo más sencillo asigna una fuerza tangencial opuesta a esa velocidad relativa. Su magnitud se aproxima por un coeficiente cinético multiplicado por la normal. Hay que distinguir este valor de la fricción que se ajustaba al balance estático.

[]{#fig:I-10-N03}

<figure id="fig-fpm-v04-i-10-n03" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-10-N03.svg" class="lightbox" data-gallery="fpm-v04-c10"><img src="/assets/books/fispm/v04/I-10-N03.svg" alt="DCL en plano inclinado. Diagrama del capítulo 10; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="418" height="315" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 10.8.** Para una caja que desliza cuesta arriba en un plano a $30^\circ$, la normal es perpendicular al plano y $f_k$ apunta cuesta abajo. El peso permanece vertical; sus proyecciones no son fuerzas nuevas. Véase §[10](#fispm-c10-fricciuxf3n-cinuxe9tica-y-cambio-de-ruxe9gimen).

</figcaption>

</figure>

[]{#fispm-t1-c10-d0010}

**Definición 10.10 --- Modelo de fricción cinética seca.** Si la velocidad tangencial relativa del cuerpo respecto de la superficie es $\mathbf w_t\ne0$, se admite

$$\mathbf f_k=-\mu_kN\frac{\mathbf w_t}{\|\mathbf w_t\|},\qquad \mu_k\geq0.$$

En una dirección tangencial única, $f_k=-\mu_kN\operatorname{sgn}(w_t)$. La fórmula se aplica al tramo deslizante y no asigna una dirección cuando $w_t=0$. Usaremos coeficientes constantes cuando así se declare. Los valores $\mu_s$ y $\mu_k$ son parámetros diferentes. En varios ejemplos elegiremos $\mu_k<\mu_s$, una idealización frecuente para esos casos; no la deducimos de Newton ni la proclamamos universal para cualquier material. Tampoco afirmamos una ley exacta independiente de velocidad o del estado de las superficies.

[]{#fispm-t1-c10-p0013}

**Proposición 10.13 --- Tramo deslizante sobre una mesa fija.** Bajo peso, normal, fuerza horizontal constante $Q$ y definición 10.10, mientras la velocidad horizontal conserve signo $\sigma\in\{-1,1\}$,

$$N=mg,\qquad a_x=\frac Qm-\sigma\mu_kg,$$

$$v_x(t)=v_0+a_x(t-t_0),\qquad x(t)=x_0+v_0(t-t_0)+\tfrac12a_x(t-t_0)^2.$$

Las fórmulas describen sólo el intervalo en que ese signo y el contacto persisten.

**Demostración.** Para una mesa fija, $w_t=v_x$ y definición 10.10 da $f_k=-\sigma\mu_kmg$. Newton horizontal produce la aceleración constante. Integrar dos veces con los datos iniciales da la historia, cuya validez exige comprobar $\operatorname{sgn}(v_x)=\sigma$ en el tramo. $\square$

Si $v_0>0$ y $Q<\mu_kmg$, la velocidad llega a cero tras

$$\Delta t=\frac{mv_0}{\mu_kmg-Q}.$$

Hasta ese evento, la fricción apunta hacia la izquierda. Continuar la misma aceleración más allá puede predecir una velocidad negativa manteniendo una fricción también negativa, lo que incumple definición 10.10. El evento obliga a reconstruir la rama: se ensaya una continuación estática si es admisible, o se determina el nuevo sentido de deslizamiento con los balances correspondientes. En los ejemplos adoptamos permanencia sin deslizamiento cuando el balance la permite y no se prescribe otro cambio.

En el límite exacto de reposo relativo, la fórmula con signo no es una ley diferencial suave. Las condiciones estáticas admiten un conjunto de valores y las cinéticas seleccionan valores según el sentido de deslizamiento. Por eso no se puede aplicar sin más el teorema de unicidad para un campo regular del capítulo 9 a todo el movimiento con fricción seca. Cada tramo calculado puede ser perfectamente determinado, pero su unión exige condiciones de régimen y una regla de continuación. No atribuir una garantía global evita confundir una solución algebraica local con un teorema de evolución completo.

La fricción opuesta al movimiento relativo puede aumentar la rapidez respecto del suelo. Una cinta que se mueve hacia la derecha más rápido que un cuerpo apoyado sobre ella lo roza hacia la derecha. El cuerpo se desplaza hacia atrás respecto de la cinta aunque avance respecto del suelo. La dirección de la fuerza se fija por esa diferencia de velocidades.

[]{#fispm-t1-c10-mp0010}

**Principio metodológico 10.10 --- Detener el cálculo en el evento.** Declara el signo de la velocidad relativa para cada tramo cinético. Si ésta llega a cero, comprueba el régimen siguiente antes de prolongar la solución. No uses la fórmula de un tramo para decidir automáticamente cómo actúa la fuerza en otro.

[]{#ejercicios-9}

### Ejercicios {#fispm-c10-ejercicios-9}

[]{#fispm-t1-c10-e0019}

**Ejercicio 10.19.** Un cuerpo desliza sobre una mesa fija con velocidad inicial $4\,\mathrm{m\,s^{-1}}$. Sólo recibe peso y contacto, con $\mu_k=0{,}2$, $\mu_s=0{,}3$ y $g=10\,\mathrm{m\,s^{-2}}$. Determina tiempo y distancia hasta detenerse, y una continuación admisible.

**Solución.** Mientras $v_x>0$, $a_x=-2\,\mathrm{m\,s^{-2}}$, de modo que $v_x=4-2t$. El primer cero ocurre a los $2\,\mathrm s$. El desplazamiento es $4\cdot2-2^2=4\,\mathrm m$. En reposo, ninguna otra fuerza tangencial requiere compensación y $f_s=0$ es admisible; el cuerpo permanece detenido bajo la continuación adoptada. Seguir con $v_x=4-2t$ y la misma fricción después de $t=2$ haría que ésta ayudara al supuesto movimiento hacia la izquierda, en contradicción con la ley cinética.

[]{#fispm-t1-c10-e0020}

**Ejercicio 10.20.** Una cinta horizontal avanza a velocidad constante $5\,\mathrm{m\,s^{-1}}$ respecto del suelo. Un cuerpo apoyado tiene inicialmente velocidad $2\,\mathrm{m\,s^{-1}}$ en ese sentido. Con $\mu_k=0{,}1$ y $g=10\,\mathrm{m\,s^{-2}}$, sin otras fuerzas tangenciales, calcula su movimiento hasta igualar la velocidad de la cinta.

**Solución.** La velocidad relativa inicial es $w_t=2-5=-3\,\mathrm{m\,s^{-1}}$. La fricción cinética sobre el cuerpo apunta a la derecha y da $a_x=1\,\mathrm{m\,s^{-2}}$. Así, $v_x=2+t$ mientras $t<3\,\mathrm s$. En ese tiempo recorre $2\cdot3+3^2/2=10{,}5\,\mathrm m$ respecto del suelo. Al igualar velocidades, acompañar la cinta constante exige aceleración cero y fricción estática cero, admisible para cualquier $\mu_s\geq0$. El cuerpo continúa con velocidad $5$ bajo esa rama. Su desplazamiento relativo hasta el evento es $10{,}5-5\cdot3=-4{,}5\,\mathrm m$; la fuerza redujo el deslizamiento hacia atrás, aunque aumentó la rapidez respecto del suelo.

[]{#plano-inclinado-y-umbrales-de-deslizamiento}

[]{#fispm-t1-c10-s11}

[]{#fpm-i-10-s11}

## 11. Plano inclinado y umbrales de deslizamiento {#fispm-c10-plano-inclinado-y-umbrales-de-deslizamiento}

Volvamos al plano fijo de §6, con base $e_t$ cuesta arriba y $e_n$ hacia afuera. El contacto ahora puede aportar una fuerza tangencial $f e_t$. Una fuerza adicional $Qe_t$, firmada, deja intacto el balance normal: $N=mg\cos\theta$. El balance tangencial es $ma_t=Q-mg\sin\theta+f.$

[]{#fig:I-10-R02}

<figure id="fig-fpm-v04-i-10-r02" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-10-R02.svg" class="lightbox" data-gallery="fpm-v04-c10"><img src="/assets/books/fispm/v04/I-10-R02.svg" alt="La fricción estática tiene un conjunto admisible. Diagrama del capítulo 10; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="342" height="275" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 10.9.** Para $\mu_s=1/2$, la cuña representa $|f_s|\le N/2$ y $N\ge0$. En el interior la fricción se ajusta al equilibrio; la frontera corresponde al umbral del modelo de Coulomb. Véase §[11](#fispm-c10-plano-inclinado-y-umbrales-de-deslizamiento).

</figcaption>

</figure>

La ecuación sirve para ambos regímenes; lo que cambia es la ley y la condición de movimiento usada para encontrar $f$.[^8]

[]{#fispm-t1-c10-p0014}

**Proposición 10.14 --- Intervalo de reposo admisible en un plano inclinado.** Con $0\leq\theta<\pi/2$, fuerza tangencial $Q$ y definición 10.9, el reposo sobre el plano es admisible si y sólo si

$$|Q-mg\sin\theta|\leq\mu_smg\cos\theta.$$

Equivale al intervalo

$$mg(\sin\theta-\mu_s\cos\theta)\leq Q\leq mg(\sin\theta+\mu_s\cos\theta).$$

**Demostración.** El reposo requiere $f_s=mg\sin\theta-Q$. El límite estático es $|f_s|\leq\mu_sN$, con $N=mg\cos\theta>0$. Sustituir da la primera desigualdad y despejar sus dos lados da el intervalo. Recíprocamente, esas fuerzas satisfacen Newton y los límites, con datos iniciales de reposo. $\square$

Para $Q=0$, la condición se reduce a $\tan\theta\leq\mu_s$. La fricción requerida apunta cuesta arriba y vale $mg\sin\theta$. Si se aumenta lentamente la inclinación de un plano con un cuerpo inicialmente en reposo, el límite del balance estático ocurre en $\theta_c=\arctan\mu_s$. La igualdad es el borde del conjunto admisible, no una garantía de inicio de movimiento en ese instante sin considerar la perturbación o la evolución posterior.

Si $Q>mg\sin\theta$, la fricción estática requerida apunta cuesta abajo. La fuerza tangencial no tiene una dirección fijada por la inclinación sola: depende de qué movimiento impediría el balance. Este cambio de signo dentro del intervalo estático no obliga a deslizar. En el punto $Q=mg\sin\theta$, la fricción requerida es cero.

[]{#fispm-t1-c10-p0015}

**Proposición 10.15 --- Aceleración deslizante en el plano fijo.** Si el cuerpo desliza con signo tangencial $\sigma$, bajo las mismas fuerzas y definición 10.10,

$$a_t=\frac Qm-g\sin\theta-\sigma\mu_kg\cos\theta.$$

Para descenso, $\sigma=-1$ y la fricción apunta cuesta arriba; para ascenso, $\sigma=1$ y apunta cuesta abajo.

**Demostración.** El plano fijo identifica velocidad tangencial relativa con $v_t$. Definición 10.10 da $f_k=-\sigma\mu_kmg\cos\theta$; sustituir en Newton y dividir por $m>0$ produce la expresión. El sentido del movimiento y el signo de la aceleración pueden diferir: deben comprobarse por separado. $\square$

Un cuerpo que ya baja puede acelerar, mantener su rapidez o frenarse según el signo de $-g\sin\theta+\mu_kg\cos\theta$, cuando $Q=0$. Si se frena hasta detenerse, el balance estático decide si puede quedar allí. En cambio, un cuerpo que sube sin fuerza adicional tiene aceleración cuesta abajo por peso y fricción, ambos en ese sentido. Su descenso posterior requiere cambiar el signo de la contribución cinética y comprobar el evento de reposo.

La fuerza aplicada puede modificar además la normal. Para separar ese efecto, consideremos de nuevo la mesa horizontal, ahora rugosa, con tracción $F$ a ángulo $\varphi$ sobre la horizontal. Mantener reposo exige normal $mg-F\sin\varphi$ y fricción $-F\cos\varphi$.

[]{#fispm-t1-c10-p0016}

**Proposición 10.16 --- Umbral con tracción oblicua.** Para $F\geq0$, $0\leq\varphi<\pi/2$ y $\mu_s\geq0$, el reposo sobre esa mesa es admisible exactamente cuando

$$F\leq F_c:=\frac{\mu_smg}{\cos\varphi+\mu_s\sin\varphi}.$$

Si $\mu_s>0$ y $\sin\varphi>0$, ese umbral es menor que el de pérdida de contacto $mg/\sin\varphi$.

**Demostración.** La desigualdad estática es $F\cos\varphi\leq\mu_s(mg-F\sin\varphi)$, junto con $N\geq0$. Como el denominador es positivo, despejar da $F\leq F_c$. Para esas fuerzas,

$$N\geq mg-F_c\sin\varphi=\frac{mg\cos\varphi}{\cos\varphi+\mu_s\sin\varphi}>0,$$

por lo que el contacto también es admisible. Si $\mu_s=0$, sólo $F=0$ permite reposo. Para los valores positivos indicados, comparar los umbrales equivale a $\mu_s\sin\varphi<\cos\varphi+\mu_s\sin\varphi$, cierto porque $\cos\varphi>0$. $\square$

La comparación muestra que perder el reposo no equivale a perder apoyo. La tracción oblicua puede provocar deslizamiento mientras la normal aún es positiva. También muestra por qué usar $\mu_smg$ como máximo sin calcular la normal daría un umbral incorrecto: parte de la tracción ya está descargando el contacto.

[]{#fispm-t1-c10-mp0011}

**Principio metodológico 10.11 --- Identificar qué límite se alcanza.** Compara por separado el límite de fricción y el de contacto normal. En un plano, conserva los signos de una base declarada al pasar de reposo a ascenso o descenso. Un umbral marca el final de una rama, no especifica por sí solo toda la historia siguiente.

[]{#ejercicios-10}

### Ejercicios {#fispm-c10-ejercicios-10}

[]{#fispm-t1-c10-e0021}

**Ejercicio 10.21.** Un cuerpo inicialmente en reposo se apoya en un plano fijo, sin otra fuerza que peso y contacto. Para $\mu_s=0{,}4$, encuentra la inclinación límite del reposo y la fricción efectiva cuando $\tan\theta=0{,}2$.

**Solución.** El límite es $\theta_c=\arctan(0{,}4)$, aproximadamente $21{,}8^\circ$. Para $\tan\theta=1/5$, $\sin\theta=1/\sqrt{26}$ y $\cos\theta=5/\sqrt{26}$. Así, $f_s=mg/\sqrt{26}$ cuesta arriba y el máximo es $0{,}4\cdot5mg/\sqrt{26}=2mg/\sqrt{26}$. La fricción efectiva es la mitad del máximo. La masa multiplica ambas fuerzas y se cancela al comparar el ángulo admisible, dentro de este modelo de coeficiente constante.

[]{#fispm-t1-c10-e0022}

**Ejercicio 10.22.** En un plano de $30^\circ$, toma $\mu_s=0{,}6$ y $\mu_k=0{,}4$, sin fuerza aplicada adicional. Compara un cuerpo inicialmente en reposo con otro que ya desliza cuesta abajo.

**Solución.** Para el primero, $\tan30^\circ=1/\sqrt3<0{,}6$ y el reposo es admisible con $f_s=mg/2$. Para el segundo, $\sigma=-1$ y

$$a_t=-g\left(\frac12-\frac{\sqrt3}{5}\right)<0.$$

El cuerpo que baja aumenta su rapidez. El balance estático admisible no lo detiene automáticamente porque la ley efectiva durante el deslizamiento tiene otra magnitud. Las dos historias usan los mismos coeficientes, pero datos y regímenes distintos. La normal permanece $\sqrt3mg/2$ en ambas.

[]{#fispm-t1-c10-e0023}

**Ejercicio 10.23.** Sobre una mesa, $\mu_s=1/2$ y la tracción apunta a $30^\circ$ sobre la horizontal. Calcula $F_c$ y la normal en ese umbral. Compáralo con una tracción horizontal.

**Solución.** proposición 10.16 da

$$F_c=\frac{2mg}{2\sqrt3+1},\qquad N_c=mg-\frac{F_c}{2}=\frac{2\sqrt3mg}{2\sqrt3+1}.$$

La normal es positiva y el límite corresponde a fricción, no a separación. Con tracción horizontal, $F_c=mg/2$. En este caso concreto, la tracción a $30^\circ$ tiene umbral menor porque $2/(2\sqrt3+1)<1/2$. No debe extrapolarse que todo aumento del ángulo siempre disminuya el umbral: en la expresión general cambian tanto la descarga normal como la componente horizontal de la fuerza.

[]{#resistencia-lineal-y-cuadrática}

[]{#fispm-t1-c10-s12}

[]{#fpm-i-10-s12}

## 12. Resistencia lineal y cuadrática {#fispm-c10-resistencia-lineal-y-cuadruxe1tica}

Un cuerpo que se mueve en un fluido puede recibir una fuerza que depende de su movimiento respecto del medio. A diferencia del rozamiento seco ideal, las aproximaciones que estudiaremos se anulan al anularse esa velocidad relativa y crecen con ella. La elección entre una ley lineal y una cuadrática debe apoyarse en el régimen físico o en datos; Newton no selecciona el exponente.[^9]

[]{#fig:I-10-N05}

<figure id="fig-fpm-v04-i-10-n05" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-10-N05.svg" class="lightbox" data-gallery="fpm-v04-c10"><img src="/assets/books/fispm/v04/I-10-N05.svg" alt="Resistencia y peso. Diagrama del capítulo 10; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="354" height="343" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 10.10.** Durante la caída con $v_y<0$, la fuerza $-bv_y e_y$ se opone a la velocidad. Al alcanzar $|v_y|=mg/b$ se equilibran ambas fuerzas; antes de ese límite sus módulos pueden diferir. Véase §[12](#fispm-c10-resistencia-lineal-y-cuadruxe1tica).

</figcaption>

</figure>

[]{#fispm-t1-c10-d0011}

**Definición 10.11 --- Velocidad relativa al medio.** En el marco inercial elegido, si el cuerpo tiene velocidad $\mathbf v$ y el medio tiene velocidad local $\mathbf u$, definimos $\mathbf w=\mathbf v-\mathbf u$. Para los ejemplos elementales de esta sección, $\mathbf u$ será constante y uniforme.

Un viento uniforme cambia la velocidad que debe entrar en la ley de resistencia. Un cuerpo en reposo respecto del suelo puede recibir resistencia si el medio se mueve. Usar $\mathbf v$ sin declarar que el medio está en reposo sería omitir una hipótesis física. Si el medio no es uniforme, $\mathbf u$ puede depender de posición y tiempo, y la ecuación necesita conservar esa dependencia.

[]{#fispm-t1-c10-d0012}

**Definición 10.12 --- Dos modelos de resistencia.** Con coeficientes positivos constantes, admitiremos alternativamente

$$\mathbf F_r=-b\mathbf w\quad\text{(lineal)},\qquad \mathbf F_r=-c\|\mathbf w\|\mathbf w\quad\text{(cuadrático)}.$$

Sus dimensiones son $[b]=MT^{-1}$ y $[c]=ML^{-1}$. Ambas fuerzas apuntan contra $\mathbf w$ cuando ésta es no nula y valen cero cuando es nula. En una dirección, la ley cuadrática es $F_r=-c|w|w$, no $-cw^2$ para cualquier signo. Esta última expresión siempre apuntaría hacia el lado negativo del eje y sería incorrecta cuando el movimiento relativo sea negativo. Si se trabaja sólo con rapidez positiva, hay que indicar por separado la dirección del vector.

Estas leyes describen la contribución de resistencia incluida, no necesariamente toda la interacción con el fluido. Un problema puede requerir flotación u otras fuerzas. En los ejemplos de caída de esta sección despreciamos esas contribuciones y conservamos peso y resistencia; la solución es válida mientras esa selección y los coeficientes constantes sigan siendo adecuados. No fijaremos velocidades de transición universales: la geometría y las propiedades del medio también importan.

[]{#fispm-t1-c10-p0017}

**Proposición 10.17 --- Resistencia lineal con fuerza adicional constante.** Sea $m>0$ constante y sean $\mathbf F_0$, $\mathbf u$ y $b>0$ constantes. Bajo

$$m\dot{\mathbf v}=\mathbf F_0-b(\mathbf v-\mathbf u),$$

definimos $\tau=m/b$ y $\mathbf v_\infty=\mathbf u+\mathbf F_0/b$. Dados $\mathbf r_0,\mathbf v_0$ en $t_0$, la historia es

$$\mathbf v(t)=\mathbf v_\infty+(\mathbf v_0-\mathbf v_\infty)e^{-(t-t_0)/\tau},$$

$$\mathbf r(t)=\mathbf r_0+\mathbf v_\infty(t-t_0)+\tau(\mathbf v_0-\mathbf v_\infty)\bigl(1-e^{-(t-t_0)/\tau}\bigr).$$

**Demostración.** Al restar $\mathbf v_\infty$, la ecuación queda $\dot{\mathbf v}=-(\mathbf v-\mathbf v_\infty)/\tau$. Derivar la expresión propuesta verifica esa igualdad y el dato inicial. Integrar la velocidad da la posición y su dato. La diferencia de dos soluciones con igual dato cumple $\dot{\mathbf d}=-\mathbf d/\tau$; multiplicar por $e^{(t-t_0)/\tau}$ da derivada cero, por lo que $\mathbf d=0$. Integrar la diferencia de velocidades con igual posición inicial prueba también unicidad de la posición. $\square$

La velocidad terminal es la que hace nula la resultante, no la velocidad que hace nula cada fuerza. Para caída en un medio quieto, tomando el eje positivo hacia abajo, $F_0=mg$ y $v_\infty=mg/b$. En el límite, resistencia y peso tienen igual magnitud. El cuerpo continúa moviéndose con velocidad no nula aunque su aceleración tienda a cero.

Desde reposo, $v(t)=v_\infty(1-e^{-t/\tau})$. Para tiempos pequeños frente a $\tau$, la pendiente inicial es $g$: al comenzar, la resistencia es cero. Para tiempos grandes frente a $\tau$, la diferencia respecto de $v_\infty$ disminuye exponencialmente. Excepto si se parte ya de la velocidad terminal, el valor exacto no se alcanza en un tiempo finito en este modelo. La aproximación práctica depende de la tolerancia con que se mida la diferencia.

La masa no desaparece de estas expresiones. Si se escribe una ley $F_r=-m\alpha v$, entonces $\alpha=b/m$: cambiar la masa manteniendo $b$ cambia también $\alpha$. La notación puede ocultar un parámetro físico; no autoriza a transferir la independencia de masa de la proposición 10.3 a una caída con resistencia.

[]{#fispm-t1-c10-p0018}

**Proposición 10.18 --- Caída desde reposo con resistencia cuadrática.** En un medio quieto, con eje vertical positivo hacia abajo, peso y resistencia cuadrática, define

$$v_*=\sqrt{\frac{mg}{c}},\qquad \tau_*=\frac{v_*}{g}.$$

La solución de velocidad desde reposo es $v(t)=v_*\tanh(t/\tau_*),\qquad t\geq0.$ Es no negativa, menor que $v_*$ para todo tiempo finito y tiende a $v_*$.

**Demostración.** Para $v\geq0$, Newton es $\dot v=g-(c/m)v^2=g(1-v^2/v_*^2)$. La función $\tanh z=(e^z-e^{-z})/(e^z+e^{-z})$ satisface $(\tanh z)'=1-\tanh^2z$. Derivar la expresión propuesta da precisamente la ecuación, porque $v_*/\tau_*=g$, y $v(0)=0$. Para $z\geq0$, $0\leq\tanh z<1$ y su límite es uno; esto verifica la rama no negativa y las afirmaciones de límite. La ley completa $v\mapsto g-(c/m)|v|v$ es localmente Lipschitz, así que la unicidad local del capítulo 9 identifica la solución con esos datos. La expresión acotada proporciona su continuación para todo $t\geq0$ dentro del modelo. $\square$

Para una velocidad inicial hacia arriba no se usa sin modificación esta fórmula de caída desde reposo. El término $|v|v$ cambia de signo y la resistencia apunta entonces hacia abajo, en el mismo sentido que el peso. Al llegar a velocidad cero, el peso permanece y puede comenzar el descenso. La ley cuadrática vectorial ya incorpora el cambio de dirección; no se introduce una fuerza constante nueva en el punto de retorno.

Los dos modelos tienen velocidades terminales distintas: $mg/b$ y $\sqrt{mg/c}$. Compararlas numéricamente exige coeficientes calibrados y condiciones físicas compatibles; $b$ y $c$ ni siquiera tienen las mismas unidades. Que ambos ejemplos produzcan un límite no permite intercambiar sus parámetros ni sus escalas temporales.

[]{#fispm-t1-c10-mp0012}

**Principio metodológico 10.12 --- Declarar el medio y comprobar los límites.** Especifica la velocidad relativa que entra en la ley, las demás contribuciones y el régimen donde admites los coeficientes. Verifica dimensiones, dirección de resistencia, datos iniciales y límite temporal de cada solución. Una velocidad terminal corresponde a balance de fuerzas, no a ausencia de interacción.

[]{#ejercicios-11}

### Ejercicios {#fispm-c10-ejercicios-11}

[]{#fispm-t1-c10-e0024}

**Ejercicio 10.24.** Un cuerpo cae desde reposo bajo peso y resistencia lineal en un medio quieto. ¿Cuándo alcanza la mitad de su velocidad terminal? ¿Qué cambia si se duplica la masa conservando el mismo coeficiente $b$?

**Solución.** $v/v_\infty=1-e^{-t/\tau}=1/2$ da $t=\tau\ln2=(m/b)\ln2$. Duplicar $m$ duplica $v_\infty=mg/b$, duplica $\tau=m/b$ y duplica el tiempo para alcanzar la mitad de la nueva velocidad terminal. La aceleración inicial sigue siendo $g$ porque la resistencia inicial es cero. La comparación mantiene explícitamente $b$ fijo; si cambiar el cuerpo modifica también su forma o interacción con el medio, habría que recalibrarlo y estos factores ya no se siguen automáticamente.

[]{#fispm-t1-c10-e0025}

**Ejercicio 10.25.** Una partícula se mueve horizontalmente en un medio quieto con velocidad inicial $V>0$. La única fuerza es resistencia cuadrática. Calcula velocidad y desplazamiento, y decide si la distancia total hasta tiempos arbitrariamente grandes es finita.

**Solución.** Mientras $v>0$, $m\dot v=-cv^2$. La expresión

$$v(t)=\frac{V}{1+cVt/m}$$

satisface la ecuación y el dato inicial; sigue positiva para todo tiempo finito. Al integrar,

$$x(t)-x_0=\frac mc\ln\left(1+\frac{cVt}{m}\right).$$

La velocidad tiende a cero, pero el desplazamiento crece sin cota en este modelo mantenido indefinidamente. No hay una detención finita ni una distancia total finita. Con resistencia lineal y ninguna otra fuerza horizontal, proposición 10.17 da en cambio desplazamiento límite $mV/b$. La comparación distingue dos leyes y evita deducir una distancia finita sólo porque la velocidad tienda a cero. Una aplicación real debe comprobar si la aproximación cuadrática sigue siendo válida al disminuir tanto la velocidad.

[]{#resortes-y-ley-de-hooke}

[]{#fispm-t1-c10-s13}

[]{#fpm-i-10-s13}

## 13. Resortes y ley de Hooke {#fispm-c10-resortes-y-ley-de-hooke}

Un resorte puede ejercer una fuerza que depende de cuánto se aparta de su longitud natural. Aquí importa distinguir esa longitud de la posición de equilibrio de un cuerpo sometido a otras fuerzas. Un resorte vertical que sostiene una masa suele estar alargado en equilibrio: la fuerza elástica compensa el peso y no es cero.[^10]

[]{#fig:I-10-N04}

<figure id="fig-fpm-v04-i-10-n04" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-10-N04.svg" class="lightbox" data-gallery="fpm-v04-c10"><img src="/assets/books/fispm/v04/I-10-N04.svg" alt="Fuerza restauradora. Diagrama del capítulo 10; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="226" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 10.11.** El resorte está extendido hacia la derecha respecto del equilibrio $x=0$. Su fuerza sobre la masa apunta hacia la izquierda. En una mesa lisa, peso y normal se compensan verticalmente. Véase §[13](#fispm-c10-resortes-y-ley-de-hooke).

</figcaption>

</figure>

[]{#fispm-t1-c10-d0013}

**Definición 10.13 --- Resorte lineal ideal y deformación.** Sea $\ell_0$ la longitud natural de un resorte y $\ell>0$ su longitud actual. La deformación firmada es $q=\ell-\ell_0$. En un modelo axial lineal, la fuerza sobre el extremo unido al cuerpo es

$$\mathbf F_e=-kq\mathbf n,\qquad k>0,$$

con $\mathbf n$ dirigido desde el anclaje hacia ese extremo. La constante $k$ tiene dimensión $MT^{-2}$, o unidades de fuerza por longitud. En geometría unidimensional con orientación fija, $F_e=-kq$.

Para $q>0$, el resorte estirado tira hacia el anclaje. Para $q<0$, un resorte ideal apto para compresión empuja alejándose de él. Esta última propiedad lo diferencia de la cuerda flexible de §7. No todo dispositivo elástico soporta ambos signos: un elemento que sólo transmite tracción requiere otro modelo y su propia comprobación de admisibilidad.

La ley de Hooke es una aproximación en un intervalo de deformaciones. La constante positiva expresa la respuesta lineal restauradora en ese intervalo; no implica proporcionalidad exacta para deformaciones arbitrarias. También despreciamos aquí la masa del resorte y sus modos internos cuando lo usamos como interacción entre un anclaje y un cuerpo. De conservarlos, necesitaríamos más variables y balances.

En un resorte horizontal guiado, si $x_0$ es la posición del extremo a longitud natural, $q=x-x_0$. La fuerza es $-k(x-x_0)$, no necesariamente $-kx$. Escribir la forma abreviada exige declarar el origen. Cambiar el cero de posición sin cambiar esa expresión modificaría artificialmente la interacción. La fuerza depende de una diferencia geométrica, no del número con que se etiqueta el extremo.

[]{#fispm-t1-c10-p0019}

**Proposición 10.19 --- Equilibrio vertical y desplazamiento respecto de él.** Un cuerpo cuelga de un resorte ideal vertical, con eje positivo hacia abajo, bajo peso y fuerza elástica. Su equilibrio tiene

$$q_{\mathrm{eq}}=\frac{mg}{k}.$$

Si $\delta=q-q_{\mathrm{eq}}$, la ecuación de movimiento es $m\ddot\delta=-k\delta.$ La reducción es válida mientras se mantiene la geometría axial y la ley elástica admitida.

**Demostración.** Como el anclaje y $\ell_0$ están fijos, $\ddot q$ es la aceleración del cuerpo. Newton da $m\ddot q=mg-kq$. El equilibrio exige $0=mg-kq_{\mathrm{eq}}$. Sustituir $q=q_{\mathrm{eq}}+\delta$ cancela los términos constantes y produce la ecuación indicada. $\square$

La fuerza elástica por separado sigue siendo $-k(q_{\mathrm{eq}}+\delta)$; la resultante es $-k\delta$. No se ha eliminado el peso del diagrama: se ha usado su compensación constante al expresar la resultante en una coordenada distinta. En equilibrio, la deformación no es cero y la aceleración sí lo es. En la longitud natural, el resorte no ejerce fuerza y el peso acelera al cuerpo.

La ecuación obtenida anticipa un sistema restaurador, pero no desarrollaremos aquí su teoría temporal completa ni una demostración de estabilidad por energía. El objetivo presente es construir correctamente la fuerza y la ecuación. Los capítulos posteriores tratarán las herramientas correspondientes. No hace falta resolver todas las oscilaciones para saber qué aceleración produce una deformación dada.

[]{#fispm-t1-c10-p0020}

**Proposición 10.20 --- Rigidez equivalente de dos resortes ideales.** Dos resortes lineales de constantes $k_1,k_2>0$, alineados y con geometría axial fija, tienen:

- en paralelo, deformación común $q$ y resultante elástica $F_e=-(k_1+k_2)q$;

- en serie, con unión intermedia de masa despreciable y sin otra fuerza axial, rigidez equivalente $k_{\mathrm{eq}}=k_1k_2/(k_1+k_2)$ respecto de la deformación total $q=q_1+q_2$.

**Demostración.** En paralelo, cada resorte aporta $-k_iq$ sobre el mismo receptor y la suma da la primera expresión. En serie, el balance de la unión ideal exige una fuerza axial transmitida común, de magnitud $S$ para extensión. Entonces $q_i=S/k_i$, por lo que $q=S(1/k_1+1/k_2)$. Despejar da $S=k_{\mathrm{eq}}q$. Las ecuaciones firmadas proporcionan el mismo resultado en compresión si ambos resortes y la guía admiten ese régimen. $\square$

La igualdad de fuerza en serie proviene del balance de la unión, como ocurrió con el tramo liviano de cuerda. Si la unión tiene masa apreciable y acelera, las fuerzas pueden diferir. La deformación común en paralelo proviene de la geometría de anclajes y extremo, no de que los resortes sean idénticos. Las dos equivalencias dejan de ser aplicables si se cambia cualquiera de esas condiciones.

[]{#fispm-t1-c10-mp0013}

**Principio metodológico 10.13 --- Fijar la referencia de deformación.** Separa longitud natural, posición actual y equilibrio bajo otras fuerzas. Declara los signos de deformación admitidos y qué masa o movimiento interno del resorte se desprecia. Al combinar resortes, justifica primero las relaciones de fuerza y deformación.

[]{#ejercicios-12}

### Ejercicios {#fispm-c10-ejercicios-12}

[]{#fispm-t1-c10-e0026}

**Ejercicio 10.26.** Una masa de $2\,\mathrm{kg}$ cuelga de un resorte de $100\,\mathrm{N\,m^{-1}}$, con $g=10\,\mathrm{m\,s^{-2}}$. Determina su deformación de equilibrio y la aceleración cuando la deformación es $0{,}25\,\mathrm m$, usando eje positivo hacia abajo.

**Solución.** $q_{\mathrm{eq}}=20/100=0{,}20\,\mathrm m$. Para $q=0{,}25\,\mathrm m$, el peso es $+20\,\mathrm N$ y la fuerza elástica $-25\,\mathrm N$, de modo que la resultante es $-5\,\mathrm N$ y $a=-2{,}5\,\mathrm{m\,s^{-2}}$, hacia arriba. La velocidad instantánea no cambia esta fuerza en el resorte ideal: el cuerpo podría subir o bajar en ese instante. Usar $-kq$ como resultante omitiendo el peso daría una aceleración incorrecta.

[]{#fispm-t1-c10-e0027}

**Ejercicio 10.27.** Dos resortes de $100$ y $200\,\mathrm{N\,m^{-1}}$ se usan primero en paralelo y luego en serie, bajo las hipótesis de la proposición 10.20. Calcula la fuerza necesaria para una deformación de $0{,}02\,\mathrm m$ en paralelo y $0{,}09\,\mathrm m$ en serie. En este último caso, calcula cada deformación.

**Solución.** En paralelo, $k_{\mathrm{eq}}=300\,\mathrm{N\,m^{-1}}$ y la fuerza de tracción equilibrante tiene magnitud $6\,\mathrm N$. En serie, $k_{\mathrm{eq}}=200/3\,\mathrm{N\,m^{-1}}$ y la fuerza común vuelve a ser $6\,\mathrm N$. Las deformaciones son $q_1=6/100=0{,}06\,\mathrm m$ y $q_2=6/200=0{,}03\,\mathrm m$, cuya suma es $0{,}09\,\mathrm m$. La igualdad de las fuerzas numéricas corresponde a deformaciones totales diferentes; no implica equivalencia entre ambas conexiones.

[]{#fispm-t1-c10-e0028}

**Ejercicio 10.28.** Una masa de $1\,\mathrm{kg}$ se apoya en una mesa horizontal rugosa y está unida a un resorte horizontal de $100\,\mathrm{N\,m^{-1}}$. Usa $g=10\,\mathrm{m\,s^{-2}}$, $\mu_s=0{,}3$ y $\mu_k=0{,}2$. Encuentra las deformaciones que permiten reposo. Desde $q=0{,}05\,\mathrm m$ y reposo, calcula la aceleración inicial de la rama deslizante hacia la longitud natural.

**Solución.** En reposo, la fricción debe ser $f_s=kq$ y la normal $mg=10\,\mathrm N$. La condición $|kq|\leq3\,\mathrm N$ da $|q|\leq0{,}03\,\mathrm m$. Para $q=0{,}05\,\mathrm m$, no hay balance estático. La fuerza elástica es $-5\,\mathrm N$; una rama inicial con velocidad negativa tiene fricción $+2\,\mathrm N$ y aceleración inicial $-3\,\mathrm{m\,s^{-2}}$. El signo calculado es compatible con iniciar movimiento hacia valores menores de $q$. La aceleración no permanecerá constante, pues el resorte cambia de fuerza al cambiar $q$. Tampoco puede prolongarse esta rama sin revisar un posible futuro evento de velocidad nula.

[]{#síntesis-y-auditoría-de-fuerzas}

[]{#fispm-t1-c10-s14}

[]{#fpm-i-10-s14}

## 14. Síntesis y auditoría de fuerzas {#fispm-c10-suxedntesis-y-auditoruxeda-de-fuerzas}

Construir un diagrama reúne información de naturaleza distinta. El peso viene de un campo admitido; el resorte, de una ley de deformación; la resistencia, de una ley de velocidad relativa. La normal, la fricción estática y ciertas tensiones se obtienen como fuerzas necesarias para realizar una geometría o un movimiento permitido. Todas entran en Newton, pero no se determinan de la misma manera.

Una comprobación completa empieza por el receptor. Luego identifica agentes, selecciona leyes con sus parámetros y declara las relaciones cinemáticas usadas. Sólo entonces proyecta y resuelve. Al final debe volver a las hipótesis: signo de normal y tensión, límite estático, sentido de deslizamiento, intervalo elástico y vigencia del modelo del medio. Una solución que verifica una igualdad pero incumple una de esas condiciones no describe la rama anunciada.

  Contribución             Expresión del modelo                   Comprobación decisiva
  ------------------------ -------------------------------------- ---------------------------------------------------------
  Peso uniforme            $m\mathbf g$                           Campo y masa adoptados; región de validez
  Contacto normal          $N\mathbf n$                           $N\geq0$, separación y movimiento normal
  Cuerda flexible          $T\mathbf t$                           $T\geq0$, rama tensa y modelo del tramo
  Fricción estática        Incógnita tangencial                   Ausencia de deslizamiento y $\|\mathbf f_s\|\leq\mu_sN$
  Fricción cinética        $-\mu_kN\mathbf w_t/\|\mathbf w_t\|$   $\mathbf w_t\ne0$ y sentido relativo
  Resistencia lineal       $-b\mathbf w$                          Medio, coeficiente y régimen físico
  Resistencia cuadrática   $-c\|\mathbf w\|\mathbf w$             Medio, signo y régimen físico
  Resorte lineal           $-kq\mathbf n$                         Referencia natural, geometría e intervalo elástico

Las dimensiones ayudan a encontrar errores, pero no garantizan una ley correcta. Tanto $-bv$ como $-c|v|v$ tienen dimensiones de fuerza con coeficientes adecuados. Una aceleración observada en un único instante tampoco identifica por sí sola cuál de las dos leyes actúa. Newton informa sobre la resultante; atribuirla a una interacción exige hipótesis o mediciones adicionales.

[]{#fispm-t1-c10-p0021}

**Proposición 10.21 --- Comparación de dos leyes de resistencia mediante dos velocidades.** Supongamos que la única fuerza en una dirección horizontal es resistencia en un medio quieto, que la masa es constante y que los coeficientes positivos de las leyes candidatas no cambian. Para dos velocidades positivas distintas $v_1,v_2$, las magnitudes de desaceleración satisfacen

$$\frac{|a_2|}{|a_1|}=\frac{v_2}{v_1}\quad\text{en el modelo lineal},\qquad \frac{|a_2|}{|a_1|}=\left(\frac{v_2}{v_1}\right)^2\quad\text{en el cuadrático}.$$

Estas predicciones son distintas; un solo par velocidad--aceleración no basta para distinguir ambas familias.

**Demostración.** Newton da $|a_i|=(b/m)v_i$ para la primera ley y $|a_i|=(c/m)v_i^2$ para la segunda. Dividir elimina los coeficientes y la masa. Si $r=v_2/v_1>0$ y $r\ne1$, entonces $r\ne r^2$. Para un solo dato $v>0$, $|a|>0$, se pueden elegir $b=m|a|/v$ o $c=m|a|/v^2$ y ambas leyes reproducen ese dato. $\square$

La proposición compara dos familias bajo condiciones precisas; no prueba que dos mediciones establezcan una ley universal ni que excluyan toda otra función de velocidad. Si hay una fuerza adicional desconocida, cambios de coeficiente o errores experimentales relevantes, la inferencia debe incorporar esos factores. La diferencia entre resolver un modelo e identificarlo mediante datos forma parte del uso responsable de los diagramas.

También debe mantenerse la frontera del sistema al sumar balances. Para un cuerpo aislado, una cuerda puede ejercer una fuerza externa; para un conjunto que incluye cuerpo y cuerda, esa misma interacción es interna. Dibujar su pareja sobre otro receptor no permite borrarla del balance individual. La cancelación sólo se justifica dentro de la suma apropiada o mediante un balance de transmisión declarado.

[]{#fispm-t1-c10-mp0014}

**Principio metodológico 10.14 --- Auditar el resultado contra el modelo.** Comprueba receptor, agentes, leyes, relaciones cinemáticas, dimensiones y condiciones de régimen. Verifica los datos y los eventos que terminan el tramo. Expresa qué predice el cálculo y qué necesitaría información adicional; conserva las ecuaciones individuales cuando el balance del conjunto haya eliminado una fuerza que aún interesa determinar.

[]{#ejercicios-13}

### Ejercicios {#fispm-c10-ejercicios-13}

[]{#fispm-t1-c10-e0029}

**Ejercicio 10.29.** Dos cuerpos $A$ y $B$ están conectados como en la proposición 10.10. Ahora el soporte de $A$ es liso y el de $B$ rugoso, con $\mu_k=0{,}2$ y $\mu_s=0{,}3$. Toma $m_A=2\,\mathrm{kg}$, $m_B=3\,\mathrm{kg}$, $g=10\,\mathrm{m\,s^{-2}}$ y fuerza $F=5\,\mathrm N$ sobre $A$ hacia la derecha. Ambos comienzan con velocidad común $U>0$ a la derecha y cuerda tensa. Calcula la aceleración y la tensión durante ese tramo, el tiempo hasta el primer reposo y una continuación admisible.

**Solución.** Las normales son $20$ y $30\,\mathrm N$. Sobre $B$ la fricción cinética es $-6\,\mathrm N$. Los balances son

$$5-T=2a,\qquad T-6=3a.$$

Al sumar, $a=-1/5\,\mathrm{m\,s^{-2}}$, y sustituir da $T=27/5\,\mathrm N=5{,}4\,\mathrm N>0$. Las resultantes individuales son $-0{,}4$ y $-0{,}6\,\mathrm N$, compatibles con la aceleración común. La tensión puede superar la fuerza aplicada sobre $A$: la resultante sobre éste apunta hacia atrás. No existe una regla general $T\leq F$ fuera de las hipótesis específicas de la proposición 10.10.

La velocidad común llega a cero tras $t=U/(1/5\,\mathrm{m\,s^{-2}})$. En reposo, el balance de $A$ exige $T=5\,\mathrm N$ y el de $B$ fricción $-5\,\mathrm N$. Su máximo estático es $9\,\mathrm N$, por lo que esta continuación es admisible y la cuerda sigue transmitiendo tracción. Cambian tensión y ley de fricción en el evento; la velocidad permanece continua. El salto de aceleración entre tramos no implica aquí un salto de velocidad ni requiere incorporar una colisión.

[]{#fispm-t1-c10-e0030}

**Ejercicio 10.30.** En un medio quieto, una partícula sólo recibe resistencia horizontal y tiene masa conocida $m$. Cuando su velocidad es $V>0$, su aceleración es $-A$, con $A>0$. Cuando es $2V$, su aceleración es $-2A$. Compara los modelos lineal y cuadrático con coeficientes constantes. ¿Bastaría el primer dato?

**Solución.** La razón de magnitudes observada es dos para una razón de velocidades dos. Proposición 10.21 coincide con el modelo lineal, con $b=mA/V$. El modelo cuadrático ajustado al primer dato tendría $c=mA/V^2$ y predeciría aceleración $-4A$ en el segundo, incompatible con el dato exacto declarado. El primer dato solo permitiría ajustar cualquiera de ambos coeficientes. La conclusión distingue esas dos familias bajo las hipótesis del ejercicio; no excluye otras leyes ni convierte dos datos en una validación ilimitada del modelo.

El capítulo deja una práctica común para fuerzas de formas distintas: escoger el sistema, expresar la interacción, justificar el movimiento admitido y comprobar el régimen. El capítulo 11 organizará las relaciones de restricción y los grados de libertad que aquí aparecieron en ejemplos elementales. El capítulo 12 estudiará trabajo y energía cinética. Ambos desarrollos partirán de las ecuaciones e idealizaciones que ahora podemos construir sin confundir fuerza, velocidad y condición geométrica.

[]{#fispm-c10-notas-y-fuentes label="fispm-c10-notas-y-fuentes"}

[^1]: David Morin, *Introduction to Classical Mechanics: With Problems and Solutions*, Cambridge University Press, 2008, cap. 3, §3.2, pp. 55--58. Se consultó el tratamiento de diagramas separados y selección de subsistemas. Las demostraciones y ejercicios presentes son desarrollos propios.

[^2]: Daniel Kleppner y Robert Kolenkow, *An Introduction to Mechanics*, copia Cambridge 2010, cap. 2, §2.5, pp. 80--84: campo gravitatorio, peso y distinción entre masa gravitatoria e inercial. El campo uniforme se declara como aproximación del modelo.

[^3]: Kleppner--Kolenkow, obra citada, cap. 2, §2.5, p. 92; R. Shankar, *Fundamentals of Physics I*, edición ampliada, Yale University Press, 2019, cap. 4, §4.3, pp. 55--56. Las condiciones unilaterales y el análisis por ramas se explicitan aquí como hipótesis y consecuencias del modelo, sin atribuir toda esa formulación a estos pasajes.

[^4]: Shankar, obra citada, cap. 3, §3.5, pp. 49--50: peso y lectura de soportes acelerados. Se distingue la fuerza gravitatoria de la fuerza normal medida.

[^5]: Shankar, obra citada, cap. 4, §4.5, pp. 57--60; Morin, obra citada, cap. 3, §3.2, pp. 55--56. Las proyecciones, signos y pruebas se desarrollan con la base fijada en el texto.

[^6]: Kleppner--Kolenkow, obra citada, cap. 2, §2.5, pp. 87--88, ejemplos de bloques conectados y cuerda colgante. Se usa un límite de masa despreciable con aceleración acotada y se evita dividir por masa nula. La cuerda con peso del ejercicio 10.14 conserva explícitamente su masa.

[^7]: R. Shankar, *Fundamentals of Physics I*, edición ampliada, Yale University Press, 2019, cap. 4, §4.4, pp. 56--57; Daniel Kleppner y Robert Kolenkow, *An Introduction to Mechanics*, copia Cambridge 2010, cap. 2, §2.5, pp. 92--93. Se distingue el máximo estático de la fuerza efectiva y se separan los coeficientes estático y cinético. No se adopta como universal la desigualdad estricta entre ambos que aparece en una de las exposiciones.

[^8]: Kleppner--Kolenkow, obra citada, cap. 2, §2.5, ejemplo 2.14, pp. 93--94; Shankar, obra citada, cap. 4, §§4.4--4.5, pp. 56--60. Los intervalos con fuerza tangencial, el umbral oblicuo y los ejercicios son desarrollos propios a partir de los balances declarados.

[^9]: Kleppner--Kolenkow, obra citada, cap. 2, §2.5, pp. 95--97; David Morin, *Introduction to Classical Mechanics: With Problems and Solutions*, Cambridge University Press, 2008, cap. 3, §3.3, pp. 62--64. Se consultaron las leyes de velocidad, el ejemplo de caída lineal y las cautelas sobre régimen. La solución cuadrática y la comparación de familias se demuestran aquí; no se atribuyen íntegramente a esos pasajes.

[^10]: Kleppner--Kolenkow, obra citada, cap. 2, §2.5, pp. 97--98; Shankar, obra citada, cap. 4, §4.1, pp. 51--54. Se usa la respuesta elástica lineal con referencia natural declarada. El equilibrio bajo peso, las equivalencias y los ejercicios se desarrollan en el texto; la teoría completa del oscilador queda fuera del alcance actual.
