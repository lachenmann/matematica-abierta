---
title: "Leyes de Newton y estructura de la dinámica"
subtitle: "Física para matemáticos · Tomo I · Capítulo 9"
author: "A. Peña"
description: "Capítulo 9 del Tomo I de Física para matemáticos, con ejercicios y soluciones desarrolladas."
archived-content-id: MA-BCH-0349
source-id: FISPM-T1-C09
editorial-id: FPM-I-09
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
date-modified: 2026-10-17
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0348"]
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

[Capítulo 8](fisica-para-matematicos-capitulo-8-cinematica-en-varias-dimensiones.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos-v04-archivo.md#tomo-i-fundamentos-y-mecanica) · [Capítulo 10](fisica-para-matematicos-capitulo-10-fuerzas-elementales-y-diagramas-de-cuerpo-libre.md)

[]{#fispm-c09-leyes-de-newton-y-estructura-de-la-dinuxe1mica}

[]{#prerrequisitos-y-propósito}

## Prerrequisitos y propósito {#fispm-c09-prerrequisitos-y-propuxf3sito .unnumbered}

Se utilizan las historias y derivadas del capítulo 5, las aproximaciones del capítulo 6 y la reconstrucción cinemática y los cambios de marco del capítulo 7--08. La matemática requerida es M2--M3 y M6 elemental: vectores, normas, derivadas, integrales y la formulación de ecuaciones diferenciales. El capítulo introduce el estado, demuestra existencia y unicidad local bajo condiciones explícitas y distingue esas propiedades de la adecuación física del modelo.

La cinemática nos permitió reconstruir una historia desde su aceleración. La dinámica introduce una exigencia nueva: explicar qué interacciones permiten calcular esa aceleración antes de conocer la historia. Estudiaremos partículas de masa constante, en un espacio euclídeo y con un tiempo clásico compartido. Las leyes de Newton se tratarán como postulados físicos; sus consecuencias, una vez fijado un modelo, se demostrarán como afirmaciones matemáticas.

Las leyes particulares de gravedad uniforme, contacto, tensión, fricción, resistencia y resortes, y los diagramas de cuerpo libre, pertenecen al capítulo 10. Los modelos de fuerza empleados aquí tienen la función de enseñar estructura, hipótesis y resolución, sin anticipar ese catálogo. No se introduce el formalismo de energía ni los balances de momento.

[]{#de-una-historia-observada-a-una-pregunta-dinámica}

[]{#fispm-t1-c09-s01}

[]{#fpm-i-09-s01}

## 1. De una historia observada a una pregunta dinámica {#fispm-c09-de-una-historia-observada-a-una-pregunta-dinuxe1mica}

Un carro recorre una pista casi horizontal. Durante unos segundos su velocidad parece constante; después aumenta y finalmente disminuye. El capítulo 7 permite describir los tres tramos y estimar sus aceleraciones. Pero una gráfica de posición, por completa que sea, no explica por qué cambió la velocidad. Para responder necesitamos información sobre el carro, sobre su entorno y sobre las interacciones que actuaron durante cada tramo.

Conviene comenzar por esta diferencia porque la ecuación que dominará el capítulo es tan breve que puede ocultarla. Si una historia ya es conocida, calcular su segunda derivada es una operación cinemática. Si queremos predecir una historia desconocida, escribir su segunda derivada en términos de interacciones es una propuesta física. El mismo símbolo de aceleración interviene en ambos trabajos, pero la dirección del razonamiento cambia.

Fijamos un espacio afín euclídeo $\mathcal E$, de dimensión $d=1,2$ o $3$, cuyo espacio de desplazamientos es $V$. Una partícula representa un cuerpo mediante un punto $P(t)$; se omiten por ahora su extensión, orientación y deformación. En un marco con origen $O$ y base ortonormal fija escribimos $P(t)=O+\mathbf r(t)$. Las derivadas temporales $\mathbf v=\mathbf r'$ y $\mathbf a=\mathbf r''$ conservan el significado del capítulo 5--08.

[]{#fispm-t1-c09-d0001}

**Definición 9.1 --- Sistema mecánico y entorno.** El sistema mecánico es el conjunto de partículas que se ha decidido describir. El entorno comprende los agentes y cuerpos excluidos de ese conjunto cuya influencia se conserva en el modelo. La frontera entre ambos forma parte de la elección de modelización.

Elegir una partícula como sistema no afirma que el cuerpo carezca de partes. Afirma que, para la pregunta planteada y dentro de una escala determinada, una posición basta para representar el movimiento que interesa. Si necesitamos describir cómo gira una rueda, su posición no basta; si queremos localizar el centro de una rueda en un trayecto, la representación puntual puede ser útil. La suficiencia de las variables depende de la pregunta.

Usaremos tres marcas de procedencia. $[DEF]$ introduce una definición; $[POST]$ identifica una ley física asumida en el régimen newtoniano; $[MOD]$ identifica una idealización o una ley particular de interacción elegida para un problema. Una proposición demostrada será una consecuencia matemática bajo las hipótesis indicadas. Las marcas impiden presentar una elección de modelo como teorema acerca de todos los cuerpos.

[]{#fispm-t1-c09-p0001}

**Proposición 9.1 --- Una historia no identifica sus interacciones por sí sola.** Dada una historia $C^2$ y una masa constante $m>0$, el vector $\mathbf G(t)=m\mathbf r''(t)$ queda determinado por la historia y por $m$. Sin información adicional, ese vector no determina una descomposición única en dos contribuciones vectoriales continuas.

**Demostración.** Para cualquier función continua $\mathbf H:I\to V$, definimos $\mathbf G_1=\mathbf H$ y $\mathbf G_2=\mathbf G-\mathbf H$. Entonces $\mathbf G_1+\mathbf G_2=\mathbf G$. Escoger dos funciones $\mathbf H$ diferentes produce dos descomposiciones diferentes con la misma suma. Como $\mathbf r$ es $C^2$, todas las contribuciones construidas son continuas. $\square$

El argumento no acredita que cada contribución construida corresponda a una interacción realizable. Precisamente muestra lo que falta: una restricción física que identifique agentes, mecanismos y dependencias. Más adelante la segunda ley relacionará $\mathbf G$ con una resultante; todavía no podemos inferir de la curva qué parte provino de cada agente.

[]{#fispm-t1-c09-mp0001}

**Principio metodológico 9.1 --- Declarar la información disponible.** Antes de formular una ecuación dinámica, distingue la historia observada, los parámetros del cuerpo, las interacciones propuestas y los datos iniciales. Si una fuerza se reconstruye desde una historia medida, no la presentes como una predicción independiente de esa misma historia.

[]{#ejercicios}

### Ejercicios {#fispm-c09-ejercicios}

[]{#fispm-t1-c09-e0001}

[]{#fispm-t1-c09-e0009}

**Ejercicio 9.1.** En una recta fija se observa $x(t)=L(t/T)^2$ para $0\le t\le T$, donde $L,T>0$. Calcula $m x''$. Produce dos descomposiciones distintas en contribuciones constantes y explica qué se ha aprendido acerca de los agentes físicos.

**Solución.** La segunda derivada es $2L/T^2$, de modo que $G=2mL/T^2$. Una descomposición es $G_1=G$, $G_2=0$; otra es $G_1=3G$, $G_2=-2G$. Las sumas son iguales y las dimensiones de cada término son masa por longitud por tiempo a la potencia $-2$. No hemos identificado agentes: sólo calculamos la combinación que una futura ecuación dinámica debe reproducir. Distinguir las descomposiciones exige observaciones o leyes de interacción adicionales.

[]{#fispm-t1-c09-e0002}

**Ejercicio 9.2.** Se conoce la imagen espacial de una trayectoria circular de radio $b>0$, pero no su parametrización. ¿Puede calcularse $m\mathbf r''$ a partir de esa información? Compara dos movimientos uniformes que recorren la misma circunferencia.

**Solución.** Tomemos $\mathbf r_1=b(\cos\omega t,\sin\omega t)$ y $\mathbf r_2=b(\cos2\omega t,\sin2\omega t)$, con $\omega\ne0$. Ambas imágenes son la misma circunferencia, pero $\mathbf r_1''=-\omega^2\mathbf r_1$ y $\mathbf r_2''=-4\omega^2\mathbf r_2$. Cuando ambas partículas están en el mismo punto, las aceleraciones tienen dirección igual y magnitudes distintas en razón cuatro. La curva espacial no fija la derivación temporal. Además de la masa necesitamos la historia parametrizada; incluso con ella, proposición 9.1 advierte que no conoceríamos por ese solo cálculo cada interacción.

[]{#inercia-y-elección-del-marco}

[]{#fispm-t1-c09-s02}

[]{#fpm-i-09-s02}

## 2. Inercia y elección del marco {#fispm-c09-inercia-y-elecciuxf3n-del-marco}

Una partícula sin interacciones apreciables no necesita una intervención permanente para conservar su velocidad. Esta afirmación puede resultar poco intuitiva porque muchos objetos cotidianos se frenan. Un carro sobre una pista pierde velocidad al interactuar con la pista y con el aire; reducir esas influencias prolonga el movimiento aproximadamente uniforme. La extrapolación a un cuerpo aislado pertenece al modelo físico, no a una identidad del cálculo diferencial.

También importa desde dónde observamos. En un marco cuyo origen acelera hacia la derecha, un cuerpo que conserva su velocidad respecto de un marco fijo adquiere una aceleración hacia la izquierda en las coordenadas móviles. El capítulo 8 ya calculó ese cambio. La primera ley selecciona ahora los marcos en los que el movimiento libre tiene la forma que la dinámica considera básica.[^1]

[]{#fispm-t1-c09-d0002}

**Definición 9.2 --- Marco inercial.** Dentro del régimen y la precisión del modelo, un marco es inercial si toda partícula libre conserva en él una velocidad vectorial constante. Una partícula libre es aquella cuyas interacciones relevantes se han eliminado o pueden despreciarse en ese régimen. La condición se refiere a una clase de partículas de prueba, no únicamente a un cuerpo elegido.

**Primera ley $[POST]$.** Existen marcos inerciales en los que la descripción newtoniana de los movimientos resulta válida. En ellos una partícula libre satisface $\mathbf a=0$ y, por tanto, $\mathbf r(t)=\mathbf r_0+(t-t_0)\mathbf v_0$.

La definición establece qué significa «inercial»; el postulado afirma que esa clase de marcos describe adecuadamente una parte del mundo físico. Las dos afirmaciones cumplen funciones diferentes. Tampoco existe un procedimiento experimental que observe directamente un aislamiento perfecto durante un tiempo infinito. Se comparan partículas y escalas, se reducen interacciones conocidas y se examina la consistencia de la aproximación.

[]{#fispm-t1-c09-p0002}

**Proposición 9.2 --- Traslaciones uniformes de un marco inercial.** Sea un marco inercial y otro con ejes paralelos fijos, reloj común y origen $\mathbf c(t)=\mathbf c_0+(t-t_0)\mathbf u$, donde $\mathbf u$ es constante. Si $\mathbf r=\mathbf c+\mathbf y$, entonces $\mathbf y''=\mathbf r''$. En particular, el segundo marco también es inercial para la misma clase de partículas libres.

**Demostración.** Derivando dos veces la relación de posiciones, obtenemos $\mathbf r''=\mathbf c''+\mathbf y''$. La función afín $\mathbf c$ tiene segunda derivada nula. Así, una historia con $\mathbf r''=0$ tiene también $\mathbf y''=0$; su velocidad en el segundo marco es constante. El argumento se aplica a todas las partículas libres consideradas, no sólo a una de ellas. $\square$

La primera ley no selecciona un reposo absoluto: $\mathbf v$ y $\mathbf v-\mathbf u$ pueden ser diferentes y ambas constantes. Una rotación fija de los ejes conserva igualmente la condición de aceleración nula, pues multiplica sus componentes por una matriz ortogonal constante. Una rotación dependiente del tiempo requiere otro cálculo y no queda incluida en la proposición 9.2.

[]{#fispm-t1-c09-mp0002}

**Principio metodológico 9.2 --- No adaptar el marco a una sola trayectoria.** Hacer que un objeto permanezca en el origen no demuestra que el marco sea inercial. Hay que comprobar el comportamiento de una clase de movimientos libres y declarar las escalas en las que se desprecia la aceleración del marco.

Una mesa de laboratorio puede constituir un marco aproximadamente inercial en un experimento breve. Esa utilidad no convierte a la Tierra en un marco exactamente inercial para toda pregunta. La precisión de la descripción debe compararse con el tamaño de los términos omitidos; recuperamos así el criterio del capítulo 6 sin introducir todavía la dinámica completa de marcos giratorios.

[]{#ejercicios-1}

### Ejercicios {#fispm-c09-ejercicios-1}

[]{#fispm-t1-c09-e0003}

**Ejercicio 9.3.** Una partícula libre tiene $\mathbf r=\mathbf r_0+\tau\mathbf v_0$, con $\tau=t-t_0$. Otro origen sigue $\mathbf c=\mathbf c_0+\tau\mathbf u+\tfrac12\tau^2\mathbf A$, con $\mathbf A$ constante. Calcula la velocidad y la aceleración relativas. ¿Cuándo es compatible este marco con la definición 9.2?

**Solución.** La resta de posiciones da $\mathbf y=\mathbf r_0-\mathbf c_0+\tau(\mathbf v_0-\mathbf u)-\tfrac12\tau^2\mathbf A$. Por derivación, $\mathbf y'=\mathbf v_0-\mathbf u-\tau\mathbf A$ y $\mathbf y''=-\mathbf A$. Si $\mathbf A=0$, proposición 9.2 garantiza la compatibilidad para toda partícula libre. Si $\mathbf A\ne0$, incluso esta partícula libre acelera en las coordenadas móviles, de modo que el marco no cumple definición 9.2. La aceleración calculada procede del marco y no demuestra que haya aparecido una interacción sobre la partícula.

[]{#fispm-t1-c09-e0004}

**Ejercicio 9.4.** Se propone el siguiente argumento: «Elijo como origen un cuerpo y sus coordenadas son siempre cero; entonces su aceleración es cero y el marco es inercial». Localiza la falla y construye un contraejemplo.

**Solución.** El argumento comprueba una sola historia, mientras que definición 9.2 exige la propiedad para una clase de partículas libres. Además, el cuerpo usado como origen podría estar sometido a interacciones. En una recta, elijamos un origen $c(t)=At^2/2$ con $A\ne0$ respecto de un marco inercial. El cuerpo que define ese origen tiene coordenada relativa cero. Otra partícula libre con $x(t)=0$ tiene coordenada $y(t)=-At^2/2$ y aceleración $-A$. La propiedad universal fracasa. Para reparar el argumento hay que establecer el movimiento uniforme del origen y la constancia de la orientación, o verificar la condición con partículas libres independientes.

[]{#masa-inercial-y-comparación-de-respuestas}

[]{#fispm-t1-c09-s03}

[]{#fpm-i-09-s03}

## 3. Masa inercial y comparación de respuestas {#fispm-c09-masa-inercial-y-comparaciuxf3n-de-respuestas}

Dos carros reciben una intervención reproducible y sus aceleraciones iniciales son diferentes. Un modo de organizar esa diferencia consiste en asignar a cada carro una masa inercial: para una misma fuerza resultante, el cuerpo con mayor masa tiene menor aceleración. El adjetivo «inercial» recuerda que hablamos de respuesta a un cambio de velocidad, no de cuánto pesa el cuerpo en un lugar determinado.[^2]

[]{#fig:I-09-N01}

<figure id="fig-fpm-v04-i-09-n01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-09-N01.svg" class="lightbox" data-gallery="fpm-v04-c09"><img src="/assets/books/fispm/v04/I-09-N01.svg" alt="Masa y respuesta. Diagrama del capítulo 9; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="523" height="228" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 9.1.** Una misma fuerza sobre dos cuerpos separados de masas $m$ y $2m$ produce aceleraciones en razón dos a uno. Cada dibujo contiene la única fuerza externa supuesta. Véase §[3](#fispm-c09-masa-inercial-y-comparaciuxf3n-de-respuestas).

</figcaption>

</figure>

La comparación exige declarar qué significa repetir la intervención. Podemos usar un dispositivo cuya configuración inicial y respuesta hayan sido contrastadas con un cuerpo de referencia. La reproducibilidad no se demuestra con una ecuación de Newton; es una hipótesis experimental sujeta a comprobación. Importan, por ejemplo, cambios del dispositivo, interacciones residuales y diferencias de configuración.

[]{#fispm-t1-c09-d0003}

**Definición 9.3 --- Masa inercial en el modelo puntual.** La masa inercial $m$ es un parámetro escalar positivo del cuerpo que relaciona su aceleración con la fuerza resultante en la segunda ley. En este capítulo se supone constante durante el movimiento. Una calibración comparativa usa, bajo una intervención resultante igual y no nula, la razón inversa de las magnitudes de aceleración.

Si el cuerpo de referencia tiene masa $m_*$ y aceleración de magnitud $a_*$, mientras otro responde con magnitud $a$, la calibración propone $m=m_*a_*/a$. Esta expresión necesita $a>0$ y que ambas aceleraciones correspondan realmente a la misma fuerza. No proporciona una medida útil cuando la resultante es nula. La consistencia entre dispositivos distintos es contenido físico adicional: una definición formal no garantiza que todas las comparaciones den el mismo resultado.

[]{#fispm-t1-c09-p0003}

**Proposición 9.3 --- Consistencia algebraica de las razones.** Si tres cuerpos con masas positivas $m_A,m_B,m_C$ responden a una misma resultante no nula mediante $m_A\mathbf a_A=m_B\mathbf a_B=m_C\mathbf a_C$, sus aceleraciones son paralelas con igual sentido y $$\frac{m_B}{m_A}=\frac{\|\mathbf a_A\|}{\|\mathbf a_B\|},\qquad \frac{m_C}{m_A}=\frac{m_C}{m_B}\frac{m_B}{m_A}.$$

**Demostración.** Denotemos la resultante común por $\mathbf F\ne0$. Cada aceleración es $\mathbf F/m_i$. Como $m_i>0$, el sentido coincide y su norma es $\|\mathbf F\|/m_i$. Dividir dos expresiones de norma da la primera igualdad. La segunda es la cancelación algebraica de $m_B>0$ en el producto de razones. $\square$

La transitividad es necesaria para que una escala de masas pueda usarse coherentemente. Si las razones medidas violan esta propiedad más allá de la incertidumbre, hay que examinar el dispositivo, el aislamiento, la constancia de los parámetros o la pertinencia del modelo. No procede corregir la discrepancia sólo cambiando el nombre de una variable.

[]{#fispm-t1-c09-mp0003}

**Principio metodológico 9.3 --- Separar calibración y contraste.** Una comparación puede fijar la escala de masa y fuerza; los ensayos posteriores deben comprobar la consistencia de esa escala entre cuerpos, dispositivos y configuraciones. No uses la misma igualdad simultáneamente como definición de todos sus términos y como contraste independiente.

La unidad SI de masa es el kilogramo, simbolizado $\mathrm{kg}$. Esta unidad no debe confundirse con una fuerza. El peso será una interacción gravitatoria, tratada con su ley particular en el capítulo 10; masa inercial y respuesta gravitatoria requieren una conexión física, no una identificación obtenida por análisis dimensional. Tampoco se admite aquí sustituir $m$ por una función arbitraria del tiempo: una partícula que intercambia materia exige especificar el flujo y cambiar la descripción del sistema.

[]{#ejercicios-2}

### Ejercicios {#fispm-c09-ejercicios-2}

[]{#fispm-t1-c09-e0005}

**Ejercicio 9.5.** En un ensayo con una misma resultante, un cuerpo de referencia de $2\,\mathrm{kg}$ acelera a $3\,\mathrm{m\,s^{-2}}$ y otro a $1.2\,\mathrm{m\,s^{-2}}$. Calcula la masa propuesta para el segundo. En otro dispositivo el primero acelera a $4\,\mathrm{m\,s^{-2}}$. ¿Qué aceleración debe producirse en el segundo para mantener la calibración?

**Solución.** La razón de masas es $3/1.2=2.5$, así que el segundo tendría $5\,\mathrm{kg}$. El nuevo dispositivo debe aplicar a ambos una misma resultante, aunque ésta puede diferir de la del primer ensayo. La razón inversa de aceleraciones debe seguir siendo $2.5$, por lo que la aceleración del segundo será $4/2.5=1.6\,\mathrm{m\,s^{-2}}$. Si no ocurre así, el dato no prueba automáticamente una variación de masa: primero debe comprobarse la hipótesis de intervención igual y la incertidumbre de cada medición.

[]{#fispm-t1-c09-e0006}

**Ejercicio 9.6.** Un estudiante afirma que un cuerpo cuya aceleración es cero tiene masa infinita, porque $m=F/a$. Explica por qué la inferencia es inválida y ofrece dos situaciones con masa positiva finita y aceleración nula.

**Solución.** La fórmula comparativa se obtuvo bajo una resultante no nula y una aceleración de magnitud positiva. No se puede dividir por cero. Una partícula libre de masa finita puede moverse con velocidad constante; también un cuerpo de masa finita puede tener varias interacciones cuya suma sea nula. En ambos casos la futura segunda ley tendrá $0=m\,0$, que no identifica la masa. Si una resultante conocida no nula coexistiera con aceleración exactamente nula en un marco inercial, habría una incompatibilidad del modelo; asignar masa infinita no es una reparación dentro de la definición 9.3.

[]{#fuerza-agente-y-resultante}

[]{#fispm-t1-c09-s04}

[]{#fpm-i-09-s04}

## 4. Fuerza, agente y resultante {#fispm-c09-fuerza-agente-y-resultante}

Decir que un cuerpo está sometido a una fuerza exige más información que dar un número. Hay que identificar el cuerpo receptor, el agente que actúa sobre él, la dirección del vector y las condiciones bajo las que la interacción tiene el valor propuesto. Una fuerza de magnitud $5\,\mathrm N$ puede aumentar una componente de velocidad, reducirla o cambiar sólo la dirección instantánea del movimiento, según su orientación y el estado del cuerpo.

[]{#fispm-t1-c09-d0004}

**Definición 9.4 --- Fuerza sobre un receptor.** En el modelo newtoniano, una fuerza $\mathbf F_{A\leftarrow B}$ es una contribución vectorial a la ecuación de movimiento del receptor $A$, atribuida a su interacción con el agente $B$. La flecha apunta hacia el receptor. Una fuerza resultante sobre $A$ es la suma de todas las contribuciones incluidas que actúan sobre ese mismo receptor.

Los vectores de fuerza viven en el espacio de direcciones $V$ y tienen dimensión $MLT^{-2}$. En unidades SI, $1\,\mathrm N=1\,\mathrm{kg\,m\,s^{-2}}$. Las componentes de una fuerza se escriben en una base común antes de sumarlas. No se suman directamente las listas de componentes obtenidas con ejes distintos sin efectuar antes el cambio de base correspondiente.

**Superposición de contribuciones $[MOD]$.** Para las interacciones que se incluyen en nuestros modelos, la resultante sobre una partícula es $$\mathbf F_{\mathrm{res}}=\sum_{\alpha=1}^k\mathbf F_{\alpha}.$$ La aditividad es una hipótesis física acerca de cómo se combinan las contribuciones. Definir la palabra «resultante» mediante una suma no demuestra por sí solo que la respuesta del cuerpo a intervenciones simultáneas esté descrita por esa suma.[^3]

Una resultante puede anularse aunque cada contribución sea distinta de cero. En una recta, $F_1=5\,\mathrm N$ y $F_2=-5\,\mathrm N$ suman cero; ninguna de las dos fuerzas desaparece. Esto tiene importancia experimental: retirar una contribución altera el movimiento, aunque antes el cuerpo conservara una velocidad constante. Por eso conviene distinguir un cuerpo libre de un cuerpo sometido a interacciones equilibradas.

[]{#fispm-t1-c09-p0004}

**Proposición 9.4 --- La cancelación debe efectuarse en un receptor común.** Si $\mathbf F_1,\ldots,\mathbf F_k$ actúan sobre un receptor y $Q$ es una matriz ortogonal constante que cambia sus componentes, entonces la nueva resultante es $Q\sum_\alpha\mathbf F_\alpha=\sum_\alpha Q\mathbf F_\alpha$. Su anulación es independiente de esa elección de base. En cambio, dos fuerzas opuestas sobre receptores distintos no constituyen por sí mismas una resultante nula sobre ninguno de ellos.

**Demostración.** La primera igualdad es la linealidad de $Q$. Como $Q$ es invertible, $Q\mathbf F_{\mathrm{res}}=0$ equivale a $\mathbf F_{\mathrm{res}}=0$. Para la última afirmación, la resultante sobre $A$ sólo suma términos cuyo receptor es $A$, según la definición 9.4. Un término con receptor $B\ne A$ no pertenece a esa suma; la oposición entre los vectores no cambia sus receptores. $\square$

La última parte es una regla de tipado físico. Al escribir una ecuación para un cuerpo, no basta con que dos vectores tengan dimensiones compatibles: también deben pertenecer a la misma lista de contribuciones sobre ese cuerpo. En §7 volveremos sobre esta precisión al formular la tercera ley.

[]{#fispm-t1-c09-mp0004}

**Principio metodológico 9.4 --- Conservar el receptor en la notación.** Identifica primero sobre quién actúa cada fuerza y sólo después decide qué contribuciones sumar. Dos flechas de sentidos opuestos pueden describir un equilibrio o una pareja de interacción entre cuerpos diferentes; su geometría aislada no distingue ambas situaciones.

Para predecir una historia necesitaremos además una regla que evalúe la fuerza. Una ley de interacción puede depender de posición, velocidad, tiempo y parámetros de otros cuerpos. La identificación del agente no fija todavía esa regla. Tampoco la velocidad es una fuerza: un cuerpo que se mueve hacia la derecha puede estar sometido a una resultante hacia la izquierda y continuar moviéndose hacia la derecha durante cierto tiempo.

[]{#ejercicios-3}

### Ejercicios {#fispm-c09-ejercicios-3}

[]{#fispm-t1-c09-e0007}

**Ejercicio 9.7.** Sobre $A$ actúan $\mathbf F_{A\leftarrow B}=(3,4)\,\mathrm N$ y $\mathbf F_{A\leftarrow C}=(-3,1)\,\mathrm N$ en una base ortonormal. Se conoce también $\mathbf F_{B\leftarrow A}=(-3,-4)\,\mathrm N$. Calcula la resultante de las contribuciones indicadas sobre $A$ y su magnitud. ¿Qué suma incorrecta podría sugerir la tercera contribución?

**Solución.** definición 9.4 exige sumar sólo las dos contribuciones cuyo receptor es $A$. La resultante es $(0,5)\,\mathrm N$, de magnitud $5\,\mathrm N$. La tercera fuerza actúa sobre $B$; sumarla a las anteriores produciría $(-3,1)\,\mathrm N$, pero esa suma no sería la resultante sobre $A$. La igualdad $\mathbf F_{B\leftarrow A}=-\mathbf F_{A\leftarrow B}$ anticipa una pareja de interacción y no un equilibrio de $A$.

[]{#fispm-t1-c09-e0008}

**Ejercicio 9.8.** Dos fuerzas de igual magnitud $F>0$ actúan sobre el mismo cuerpo y forman un ángulo $\theta\in[0,\pi]$. Encuentra la magnitud de su suma. Determina cuándo la suma vale cero, cuándo tiene magnitud $F$ y cuándo tiene magnitud $2F$.

**Solución.** El producto escalar da $\|\mathbf F_1+\mathbf F_2\|^2=2F^2(1+\cos\theta)=4F^2\cos^2(\theta/2)$. En el intervalo indicado el coseno de medio ángulo es no negativo, por lo que la magnitud es $2F\cos(\theta/2)$. Se anula en $\theta=\pi$, vale $F$ en $\theta=2\pi/3$ y alcanza $2F$ en $\theta=0$. La suma de las magnitudes coincide con la magnitud de la suma únicamente en el último caso. La dirección de las fuerzas contiene información indispensable.

[]{#segunda-ley-y-contenido-de-una-ley-de-interacción}

[]{#fispm-t1-c09-s05}

[]{#fpm-i-09-s05}

## 5. Segunda ley y contenido de una ley de interacción {#fispm-c09-segunda-ley-y-contenido-de-una-ley-de-interacciuxf3n}

Ya disponemos de una clase de marcos, una escala de masas y una representación vectorial de las interacciones. La segunda ley reúne esas piezas. En su forma de masa constante se escribe como una relación entre la resultante sobre una partícula y su aceleración respecto de un marco inercial.

**Segunda ley $[POST]$.** Para una partícula de masa constante $m>0$, en un marco inercial y dentro del dominio del modelo, $$m\mathbf r''(t)=\mathbf F_{\mathrm{res}}(t).$$ El lado derecho puede ser una función prescrita del tiempo o puede depender del estado del sistema. En ese segundo caso aún no conocemos sus valores a lo largo del movimiento: sólo conocemos una regla para calcularlos cuando la posición y la velocidad sean dadas.

Supongamos, como modelo matemático de ejemplo, que en una recta $F(t,x,v)=F_0\cos(\Omega t)$. La ecuación queda $mx''=F_0\cos(\Omega t)$ y podemos integrar dos veces. Si en cambio elegimos $F(t,x,v)=-\lambda v$, con $\lambda>0$, la ecuación es $mx''=-\lambda x'$. Aquí la propia velocidad desconocida interviene en la fuerza; no corresponde sustituir una aceleración arbitraria y usar únicamente la reconstrucción del capítulo 8.

[]{#fispm-t1-c09-d0005}

**Definición 9.5 --- Ley de fuerza del modelo.** Una ley de fuerza es una función especificada antes de resolver el movimiento, por ejemplo $\mathbf F(t,\mathbf r,\mathbf v;\eta)$, donde $\eta$ reúne parámetros fijados. Su dominio declara las configuraciones y estados donde se admite la regla. Al evaluar esa función sobre una historia se obtiene la resultante prevista para esa historia.

La ley de fuerza y la segunda ley tienen alcances distintos. La primera dice cómo una interacción particular depende de variables; la segunda establece cómo la resultante entra en la aceleración. Las dos son necesarias para cerrar un problema predictivo. Esta separación constituye uno de los controles conceptuales centrales de Shankar y Kleppner--Kolenkow.[^4]

[]{#fispm-t1-c09-p0005}

**Proposición 9.5 --- Respuesta instantánea a una resultante.** Bajo la segunda ley con $m>0$, la aceleración es nula si y sólo si la resultante es nula. Si la resultante es distinta de cero, ambos vectores son paralelos, con el mismo sentido, y $\|\mathbf a\|=\|\mathbf F_{\mathrm{res}}\|/m$. Esta afirmación no impone que la velocidad sea paralela a la resultante.

**Demostración.** Dividir la segunda ley por el escalar positivo $m$ da $\mathbf a=\mathbf F_{\mathrm{res}}/m$. Las tres primeras conclusiones siguen de multiplicar un vector por un escalar positivo. Para comprobar que la última restricción no es una consecuencia, fijemos $\mathbf F_{\mathrm{res}}=Fe_2$, con $F>0$, y una historia $\mathbf r(t)=Ut e_1+(F/2m)t^2e_2$, donde $U\ne0$. Satisface la segunda ley y en $t=0$ su velocidad es $Ue_1$, perpendicular a la fuerza. $\square$

El cambio de rapidez requiere una lectura más cuidadosa que el cambio de velocidad. En un instante con $\mathbf v\ne0$, capítulo 8 dio $$\frac{d}{dt}\|\mathbf v\|=\frac{\mathbf v\cdot\mathbf a}{\|\mathbf v\|} =\frac{\mathbf v\cdot\mathbf F_{\mathrm{res}}}{m\|\mathbf v\|}.$$ Una fuerza perpendicular a la velocidad cambia su dirección instantánea sin cambiar la rapidez en ese instante. Una fuerza opuesta a la velocidad reduce la rapidez mientras la velocidad siga teniendo ese sentido. La fórmula no se usa dividiendo por la rapidez cuando ésta es cero; allí hay que estudiar la historia directamente.

[]{#fispm-t1-c09-mp0005}

**Principio metodológico 9.5 --- Cerrar el lado de las interacciones.** Antes de integrar $m\mathbf r''=\mathbf F$, especifica cómo se obtiene $\mathbf F$ sin conocer de antemano la solución. Escribir $\mathbf F=m\mathbf r''$ como reconstrucción es legítimo, pero no reemplaza una ley predictiva independiente.

La primera ley aporta la selección del marco y la existencia física de movimientos libres adecuados. Después de fijar ese marco y admitir la segunda ley, la consecuencia $\mathbf F_{\mathrm{res}}=0\Rightarrow\mathbf a=0$ es inmediata. Esa consecuencia algebraica no elimina el papel físico de la primera ley. Del mismo modo, las componentes de una igualdad vectorial no hacen desaparecer su dependencia respecto del marco.

[]{#ejercicios-4}

### Ejercicios {#fispm-c09-ejercicios-4}

**Ejercicio 9.9.** Una partícula tiene masa $2\,\mathrm{kg}$, velocidad instantánea $(3,4)\,\mathrm{m\,s^{-1}}$ y resultante $(8,-6)\,\mathrm N$. Calcula su aceleración y la derivada instantánea de su rapidez. ¿Es uniforme su velocidad?

**Solución.** La segunda ley da $\mathbf a=(4,-3)\,\mathrm{m\,s^{-2}}$. La rapidez vale $5\,\mathrm{m\,s^{-1}}$ y $\mathbf v\cdot\mathbf a=3\cdot4+4\cdot(-3)=0$, de modo que su derivada es cero. La velocidad no es constante en ese instante, porque su derivada vectorial es $\mathbf a\ne0$. La información es instantánea: no demuestra que la rapidez vaya a conservarse durante un intervalo. Para esa conclusión se necesitaría una ley que mantuviera la perpendicularidad a lo largo de toda la historia.

[]{#fispm-t1-c09-e0010}

**Ejercicio 9.10.** Un informe propone medir una historia $\mathbf r$ de un cuerpo de masa conocida, definir $\mathbf F=m\mathbf r''$ y luego anunciar que la igualdad $m\mathbf r''=\mathbf F$ verifica la segunda ley. Repara el diseño de contraste sin descartar la reconstrucción cinemática.

**Solución.** La igualdad anunciada sigue de la definición de $\mathbf F$, así que el ensayo no confronta dos predicciones independientes. Puede conservarse la reconstrucción como estimación de la resultante dinámica, pero hay que compararla con una ley de fuerza calibrada en otros ensayos o con la respuesta de un dispositivo cuyo comportamiento esté especificado. El informe debe declarar marco, masa, agentes, parámetros e incertidumbre, calcular la fuerza prevista por ese modelo y confrontarla con $m\mathbf r''$ en datos que no hayan servido únicamente para ajustar esa misma curva. Una discrepancia permite entonces examinar el modelo o sus hipótesis; una identidad construida no lo permite.

[]{#componentes-y-reconstrucción-con-fuerza-prescrita}

[]{#fispm-t1-c09-s06}

[]{#fpm-i-09-s06}

## 6. Componentes y reconstrucción con fuerza prescrita {#fispm-c09-componentes-y-reconstrucciuxf3n-con-fuerza-prescrita}

Para pasar de la ley vectorial al cálculo conviene conservar una distinción del capítulo 8: las componentes cartesianas en una base fija se derivan sin términos adicionales, mientras que una base móvil exige derivar también sus vectores. Trabajaremos primero en una base ortonormal fija de un marco inercial. Si $\mathbf r=\sum_i x_i e_i$ y $\mathbf F=\sum_i F_i e_i$, la segunda ley equivale a $mx_i''=F_i$ para cada $i$.

La equivalencia coordenada no significa siempre independencia dinámica. Si $F_1=-\kappa x_2$ y $F_2=\kappa x_1$, las ecuaciones son dos, pero están acopladas. Resolver una componente requiere información sobre la otra. En cambio, cuando cada $F_i(t)$ está prescrita sólo como función del tiempo, todas las componentes pueden reconstruirse por integración y se reúnen después en una historia vectorial.

[]{#fispm-t1-c09-d0006}

**Definición 9.6 --- Fuerza prescrita.** Una resultante es prescrita si sus valores $\mathbf f(t)$ se dan como función del tiempo independiente de la posición y velocidad desconocidas. Esta propiedad se refiere al modelo escogido, no a una clasificación universal de la interacción.

[]{#fispm-t1-c09-p0006}

**Proposición 9.6 --- Solución para resultante continua prescrita.** Sean $m>0$ constante, $\mathbf f:I\to V$ continua y $t_0\in I$. Dados $\mathbf r_0,\mathbf v_0\in V$, existe una única historia $C^2$ en $I$ que satisface $m\mathbf r''=\mathbf f$, $\mathbf r(t_0)=\mathbf r_0$ y $\mathbf r'(t_0)=\mathbf v_0$. Es $$\mathbf r(t)=\mathbf r_0+(t-t_0)\mathbf v_0+ \frac1m\int_{t_0}^t(t-s)\mathbf f(s)\,ds.$$

**Estrategia.** capítulo 8 reconstruyó una historia desde una aceleración continua. La segunda ley permite ahora identificar esa aceleración con $\mathbf f/m$. Es útil repetir la verificación porque deja visible qué aporta la fuerza y qué aportan los datos iniciales.

**Demostración.** Las integrales se entienden componente a componente y con orientación usual si $t<t_0$. La derivada del término integral es $\int_{t_0}^t\mathbf f(s)\,ds$: el término de borde contiene $t-t=0$. Una segunda derivación, por continuidad y el teorema fundamental del cálculo, da $\mathbf f(t)$. Por tanto $\mathbf r'=\mathbf v_0+m^{-1}\int_{t_0}^t\mathbf f(s)\,ds$ y $\mathbf r''=\mathbf f/m$. En $t=t_0$ las integrales se anulan y se recuperan ambos datos. Si hubiera dos soluciones, su diferencia tendría segunda derivada cero y posición y primera derivada nulas en $t_0$. Integrando dos veces, la diferencia sería cero en todo el intervalo. $\square$

Cuando $\mathbf f$ es constante obtenemos la historia cuadrática $\mathbf r=\mathbf r_0+\tau\mathbf v_0+\tau^2\mathbf f/(2m)$. La resultante fija la curvatura temporal de la posición; los datos iniciales fijan el término constante y el lineal. Dos cuerpos sometidos a la misma resultante y con masas distintas no tienen la misma aceleración, y aun con igual masa sus historias pueden diferir por sus datos iniciales.

[]{#fispm-t1-c09-mp0006}

**Principio metodológico 9.6 --- Distinguir equivalencia coordenada de desacoplamiento.** Escribe todas las dependencias de cada $F_i$. Separar una ecuación vectorial en componentes siempre es posible en una base fija; resolver cada componente aisladamente sólo es posible cuando sus dependencias lo permiten.

[]{#ejercicios-5}

### Ejercicios {#fispm-c09-ejercicios-5}

[]{#fispm-t1-c09-e0011}

**Ejercicio 9.11.** En un plano, $\mathbf f(t)=F_0(e_1+(t/T)e_2)$, con $F_0,T>0$, y se imponen $\mathbf r(0)=0$, $\mathbf v(0)=Ve_2$. Encuentra posición y velocidad y verifica la ecuación de Newton.

**Solución.** La integración de $\mathbf f/m$ produce $\mathbf v=(F_0/m)t e_1+(V+F_0t^2/(2mT))e_2$. Una segunda integración da $\mathbf r=F_0t^2 e_1/(2m)+(Vt+F_0t^3/(6mT))e_2$. Derivando dos veces, $m\mathbf r''=F_0e_1+(F_0t/T)e_2$; en cero se recuperan los dos datos. El factor $t^3/T$ tiene dimensión de tiempo al cuadrado, de modo que cada término de posición tiene dimensión de longitud. La fuerza fue prescrita; por ello no hizo falta resolver un acoplamiento entre coordenadas.

[]{#fispm-t1-c09-e0012}

**Ejercicio 9.12.** Una partícula recibe una fuerza constante $F e_1$, con $F>0$, durante $0\le t\le T$. Parte de $\mathbf r(0)=0$ y $\mathbf v(0)=Ue_2$, con $U>0$. Calcula su posición al final y la ecuación espacial del arco recorrido. Explica por qué no basta anunciar «se mueve en la dirección de la fuerza».

**Solución.** proposición 9.6 da $x=Ft^2/(2m)$, $y=Ut$. El punto final tiene coordenadas $(FT^2/(2m),UT)$. Como $U>0$, eliminamos $t=y/U$ y obtenemos $x=Fy^2/(2mU^2)$, con $0\le y\le UT$. La trayectoria es un arco de parábola y la velocidad es $(Ft/m,U)$; no es paralela a la fuerza. La aceleración sí lo es, tal como afirma proposición 9.5. El movimiento conserva una componente de velocidad que procede del dato inicial y que la fuerza horizontal no modifica.

[]{#tercera-ley-y-parejas-de-interacción}

[]{#fispm-t1-c09-s07}

[]{#fpm-i-09-s07}

## 7. Tercera ley y parejas de interacción {#fispm-c09-tercera-ley-y-parejas-de-interacciuxf3n}

Si dos cuerpos interactúan, la descripción de uno solo deja fuera una parte de la escena. Una fuerza que atribuimos a $B$ sobre $A$ tiene, en el modelo newtoniano de interacción por pares que adoptaremos, una pareja que actúa sobre $B$. Las magnitudes son iguales y los sentidos opuestos, pero los receptores son distintos. Esta última precisión explica por qué la tercera ley no obliga a que cada cuerpo tenga aceleración nula.[^5]

[]{#fig:I-09-R01}

<figure id="fig-fpm-v04-i-09-r01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-09-R01.svg" class="lightbox" data-gallery="fpm-v04-c09"><img src="/assets/books/fispm/v04/I-09-R01.svg" alt="La pareja actúa sobre cuerpos distintos. Diagrama del capítulo 9; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="403" height="168" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 9.2.** Las fuerzas internas $f$ y $-f$ se cancelan al sumar los balances de $A$ y $B$. La fuerza externa queda en $\dot P=F_{\rm ext}$. La frontera discontinua declara qué cuerpos se han incluido; cada balance individual conserva su fuerza interna. Véase §[7](#fispm-c09-tercera-ley-y-parejas-de-interacciuxf3n).

</figcaption>

</figure>

[]{#fig:I-09-N02}

<figure id="fig-fpm-v04-i-09-n02" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-09-N02.svg" class="lightbox" data-gallery="fpm-v04-c09"><img src="/assets/books/fispm/v04/I-09-N02.svg" alt="Pareja de interacción. Diagrama del capítulo 9; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="356" height="179" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 9.3.** Las fuerzas de la pareja actúan sobre cuerpos distintos y son opuestas. No se cancelan en el balance de cada cuerpo por separado; sí en el del sistema $A+B$. Véase §[7](#fispm-c09-tercera-ley-y-parejas-de-interacciuxf3n).

</figcaption>

</figure>

**Tercera ley $[POST]$.** Para una interacción por pares entre partículas $A$ y $B$, admitida en este modelo y evaluada en un mismo instante del tiempo clásico, $$\mathbf F_{A\leftarrow B}(t)=-\mathbf F_{B\leftarrow A}(t).$$ La igualdad expresa una relación física entre dos contribuciones. No se deduce de la definición de fuerza resultante ni de la segunda ley aplicada a un cuerpo. «Acción» y «reacción» son nombres tradicionales para la pareja; no indican que una fuerza se produzca después de la otra.

[]{#fispm-t1-c09-d0007}

**Definición 9.7 --- Fuerzas internas y externas.** Respecto de un sistema elegido, una fuerza es interna si receptor y agente pertenecen al sistema. Es externa si su receptor pertenece al sistema y su agente al entorno. La clasificación cambia cuando cambia la frontera del sistema.

Una fuerza de $B$ sobre $A$ es externa para el sistema formado sólo por $A$ e interna para el sistema formado por $A$ y $B$. Su vector no cambia por ese cambio de clasificación. Lo que cambia es la ecuación o conjunto de ecuaciones que pretendemos reunir. La contabilidad de agentes precede a la simplificación algebraica.

[]{#fispm-t1-c09-p0007}

**Proposición 9.7 --- Cancelación de una pareja al reunir dos ecuaciones.** Sean $A,B$ partículas de masas constantes positivas, con fuerzas externas resultantes $\mathbf E_A,\mathbf E_B$. Supongamos que su única interacción interna forma una pareja de tercera ley. Entonces $$m_A\mathbf a_A=\mathbf E_A+\mathbf F_{A\leftarrow B},\qquad m_B\mathbf a_B=\mathbf E_B+\mathbf F_{B\leftarrow A}$$ implican $$m_A\mathbf a_A+m_B\mathbf a_B=\mathbf E_A+\mathbf E_B.$$ Si las fuerzas externas son nulas y la interacción interna no es nula, las dos aceleraciones son no nulas, opuestas y sus magnitudes están en razón $\|\mathbf a_A\|/\|\mathbf a_B\|=m_B/m_A$.

**Demostración.** Sumamos las dos igualdades vectoriales en una base común. La tercera ley anula la suma de los términos internos y deja la igualdad anunciada. Si $\mathbf E_A=\mathbf E_B=0$, ponemos $\mathbf F=\mathbf F_{A\leftarrow B}\ne0$. Entonces $\mathbf a_A=\mathbf F/m_A$ y $\mathbf a_B=-\mathbf F/m_B$. La positividad de ambas masas determina los sentidos y permite dividir sus normas. $\square$

La cancelación ocurre al reunir ecuaciones de cuerpos diferentes; no dentro de la ecuación de cada cuerpo. Tampoco autoriza sustituir ambas aceleraciones por una aceleración común. Dos partículas que se repelen pueden alejarse con aceleraciones de magnitudes distintas. Introducir una misma aceleración requiere una relación cinemática adicional y su justificación, asunto que estudiaremos con vínculos y contacto.

Hay otra distinción necesaria. La forma que hemos postulado exige fuerzas opuestas, pero no exige por sí sola que su dirección sea la línea que une las posiciones. Una fuerza central añade precisamente esa condición de dirección. No derivaremos consecuencias asociadas a fuerzas centrales sin declararla. Las leyes de conservación y el centro de masa se desarrollarán en el capítulo 14--15, con sus propias hipótesis.

[]{#fispm-t1-c09-mp0007}

**Principio metodológico 9.7 --- Aplicar la pareja sin duplicar la fuerza.** En la ecuación de $A$ incluye $\mathbf F_{A\leftarrow B}$; en la de $B$, su pareja. No añadas ambas a cada receptor ni supongas aceleraciones iguales sólo porque las magnitudes de fuerza son iguales.

El alcance del postulado también debe conservarse. Usaremos modelos de interacción por pares que satisfacen la relación escrita. No extenderemos sin examen esa forma instantánea a toda descripción de materia y campos. Una teoría que incluya grados de libertad del campo puede requerir ampliar el sistema para expresar los balances relevantes. Esta reserva delimita el modelo que estamos construyendo, sin restarle utilidad en los problemas presentes.

[]{#ejercicios-6}

### Ejercicios {#fispm-c09-ejercicios-6}

[]{#fispm-t1-c09-e0013}

**Ejercicio 9.13.** Dos partículas de masas $m_A=2\,\mathrm{kg}$ y $m_B=5\,\mathrm{kg}$ no tienen fuerzas externas. En cierto instante $\mathbf F_{A\leftarrow B}=10e_1\,\mathrm N$. Calcula ambas aceleraciones y comprueba proposición 9.7. ¿Está cada partícula en equilibrio?

**Solución.** La tercera ley da $\mathbf F_{B\leftarrow A}=-10e_1\,\mathrm N$. Por la segunda ley, $\mathbf a_A=5e_1\,\mathrm{m\,s^{-2}}$ y $\mathbf a_B=-2e_1\,\mathrm{m\,s^{-2}}$. La suma ponderada por masas es $2\cdot5e_1+5\cdot(-2)e_1=0$, con unidades de fuerza. Ninguna partícula tiene aceleración nula. La ausencia de fuerzas externas sobre el par no elimina la interacción interna ni implica que cada posición evolucione linealmente. La razón de magnitudes es $5/2=m_B/m_A$, como exige proposición 9.7.

[]{#fispm-t1-c09-e0014}

**Ejercicio 9.14.** Tres cuerpos $A,B,C$ interactúan por pares y satisfacen la tercera ley. Escribe las contribuciones de $B,C$ en la ecuación de $A$. Clasifica $\mathbf F_{A\leftarrow C}$ para los sistemas $\{A\}$, $\{A,B\}$ y $\{A,B,C\}$. Comprueba qué términos se cancelan al sumar las ecuaciones del sistema $\{A,B\}$.

**Solución.** En la ecuación de $A$ aparecen $\mathbf F_{A\leftarrow B}+\mathbf F_{A\leftarrow C}$; no aparecen sus parejas, pues éstas tienen otros receptores. La contribución de $C$ sobre $A$ es externa para $\{A\}$ y para $\{A,B\}$ e interna para $\{A,B,C\}$. Al sumar las ecuaciones de $A$ y $B$, $\mathbf F_{A\leftarrow B}+\mathbf F_{B\leftarrow A}=0$. Permanecen $\mathbf F_{A\leftarrow C}+\mathbf F_{B\leftarrow C}$ como contribuciones externas sobre ese sistema. No tienen por qué cancelarse entre sí: sus parejas actúan sobre $C$, que quedó fuera de la suma. La frontera elegida determina la contabilidad.

[]{#estado-ecuación-de-movimiento-y-datos-iniciales}

[]{#fispm-t1-c09-s08}

[]{#fpm-i-09-s08}

## 8. Estado, ecuación de movimiento y datos iniciales {#fispm-c09-estado-ecuaciuxf3n-de-movimiento-y-datos-iniciales}

Cuando una fuerza depende de la posición o de la velocidad, la ecuación de Newton deja de ser una instrucción para integrar una función temporal conocida. Se convierte en una relación que la historia desconocida debe satisfacer. El cálculo de una trayectoria pasa entonces por un problema de ecuaciones diferenciales: necesitamos saber qué variables evolucionan, cuál es la regla de evolución y qué datos fijan el movimiento que interesa.

[]{#fig:I-09-R02}

<figure id="fig-fpm-v04-i-09-r02" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-09-R02.svg" class="lightbox" data-gallery="fpm-v04-c09"><img src="/assets/books/fispm/v04/I-09-R02.svg" alt="El estado incluye posición y velocidad. Diagrama del capítulo 9; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="343" height="265" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 9.4.** En el movimiento libre, cada recta horizontal del plano $(x,v)$ conserva una velocidad. Conocer sólo $x$ deja muchos estados posibles; especificar $(x_0,v_0)$ selecciona una trayectoria del sistema de primer orden. Véase §[8](#fispm-c09-estado-ecuaciuxf3n-de-movimiento-y-datos-iniciales).

</figcaption>

</figure>

El estado instantáneo de una partícula no se reduce a su posición. Dos cuerpos pueden pasar por el mismo punto con velocidades distintas y seguir historias diferentes bajo una misma ley de fuerza. En la formulación de segundo orden aparecen dos datos vectoriales; podemos reunirlos en una sola variable de estado para escribir una ecuación de primer orden.

[]{#fispm-t1-c09-d0008}

**Definición 9.8 --- Estado mecánico puntual.** Para una partícula de masa constante, con una ley de fuerza que depende sólo de $t,\mathbf r,\mathbf v$ y parámetros fijados, el estado es la pareja $z=(\mathbf r,\mathbf v)\in V\times V$. Las dos entradas tienen dimensiones físicas distintas. Las coordenadas de $V\times V$ sirven para organizar la evolución, sin identificar una longitud con una velocidad.

[]{#fispm-t1-c09-d0009}

**Definición 9.9 --- Problema de valores iniciales newtoniano.** Sea $\mathcal D\subset\mathbb R\times V\times V$ un dominio donde está definida una ley continua $\mathbf F$. Dados $m>0$ y un dato $(t_0,\mathbf r_0,\mathbf v_0)\in\mathcal D$, el problema consiste en encontrar una historia $C^2$ en un intervalo que contiene $t_0$, permanece en el dominio y satisface $$m\mathbf r''=\mathbf F(t,\mathbf r,\mathbf r'),\qquad \mathbf r(t_0)=\mathbf r_0,\quad \mathbf r'(t_0)=\mathbf v_0.$$ La definición plantea el problema; todavía no asegura que exista una solución o que sea única.

[]{#fispm-t1-c09-p0008}

**Proposición 9.8 --- Reducción exacta a primer orden.** Bajo las hipótesis de la definición 9.9, una solución $\mathbf r$ del problema de segundo orden determina una solución $C^1$ $z=(\mathbf r,\mathbf v)$ del sistema $$\mathbf r'=\mathbf v,\qquad \mathbf v'=\frac1m\mathbf F(t,\mathbf r,\mathbf v),\qquad z(t_0)=(\mathbf r_0,\mathbf v_0).$$ Recíprocamente, toda solución $C^1$ de este sistema determina una solución $C^2$ de la definición 9.9 mediante su primera componente.

**Demostración.** Si $\mathbf r$ resuelve definición 9.9, definimos $\mathbf v=\mathbf r'$. Como $\mathbf r$ es $C^2$, la pareja es $C^1$ y cumple ambas ecuaciones y ambos datos. En sentido inverso, la primera ecuación identifica $\mathbf r'$ con $\mathbf v$. Puesto que $\mathbf v$ es $C^1$, la primera componente es $C^2$ y su segunda derivada es $\mathbf v'$. Sustituyendo la segunda ecuación obtenemos $m\mathbf r''=\mathbf F(t,\mathbf r,\mathbf r')$. El dato inicial de la pareja recupera posición y velocidad. Las dos construcciones se invierten mutuamente. $\square$

En notación compacta, el campo de evolución es $f(t,z)=(\mathbf v,\mathbf F(t,\mathbf r,\mathbf v)/m)$ y el sistema es $z'=f(t,z)$. Cada componente de $f$ tiene la dimensión de la componente correspondiente de $z$ dividida por tiempo. Esta precisión será útil al medir diferencias entre estados: una norma que mezcle posiciones y velocidades necesita escalas o una convención adimensional, que introduciremos cuando haga falta.

[]{#fispm-t1-c09-p0009}

**Proposición 9.9 --- Forma integral del problema de estado.** Para un campo continuo $f$ y una historia continua $z$ que permanece en su dominio, resolver el problema $z'=f(t,z)$ con $z(t_0)=z_0$ equivale a satisfacer $$z(t)=z_0+\int_{t_0}^t f(s,z(s))\,ds$$ en todo el intervalo de la historia.

**Demostración.** Si $z$ es una solución $C^1$, el teorema fundamental del cálculo da $z(t)-z(t_0)=\int_{t_0}^t z'(s)\,ds$ y la ecuación permite sustituir el integrando por $f(s,z(s))$. Recíprocamente, la continuidad de $z$ y de $f$ hace continuo el integrando. La fórmula integral es entonces $C^1$, tiene derivada $f(t,z(t))$ y en $t_0$ toma el valor $z_0$. $\square$

Esta forma integral no es una solución explícita: la función desconocida aparece dentro de la integral. Sí muestra la estructura del problema y prepara las estimaciones de unicidad. En §6 el integrando no dependía de la historia, lo que permitía calcularlo directamente; aquí esa dependencia es precisamente la dificultad nueva.

[]{#fispm-t1-c09-mp0008}

**Principio metodológico 9.8 --- Formular antes de prometer determinismo.** Declara variables de estado, dominio, parámetros y datos iniciales antes de hablar de una evolución determinada. La segunda ley proporciona la forma de la ecuación; la existencia y unicidad de sus soluciones requieren hipótesis matemáticas sobre la ley de fuerza.

Una ley puede ser continua y no tener suficiente regularidad para garantizar unicidad; puede ser suave en su dominio y conducir a que una solución alcance su frontera en un tiempo finito. Tampoco la unicidad significa que una predicción permanezca precisa ante incertidumbres arbitrariamente pequeñas durante tiempos arbitrariamente grandes. Desarrollaremos estas diferencias en el siguiente macrotramo, con pruebas y ejemplos, sin atribuirlas automáticamente a $F=ma$.

La suficiencia del estado también pertenece al modelo. Si una fuerza depende de otra partícula móvil desconocida, habrá que añadir su posición y velocidad al sistema. Si depende de una variable interna con evolución propia, habrá que incluirla o justificar su eliminación. Mantenerla oculta dentro de un parámetro fijo no convierte un problema incompleto en un problema determinado.

[]{#ejercicios-7}

### Ejercicios {#fispm-c09-ejercicios-7}

[]{#fispm-t1-c09-e0015}

**Ejercicio 9.15.** Una partícula en una recta cumple el modelo $F(t,x,v)=-\lambda v$, con $\lambda>0$ constante. Escribe el sistema de estado y encuentra una historia que satisfaga $x(0)=x_0$, $v(0)=v_0$. Verifica directamente ambas ecuaciones.

**Solución.** El sistema es $x'=v$, $v'=-(\lambda/m)v$. Definamos $\gamma=\lambda/m>0$, con dimensión $T^{-1}$. La función $v(t)=v_0e^{-\gamma t}$ tiene derivada $-\gamma v(t)$ y valor inicial $v_0$. Su integral da $x(t)=x_0+(v_0/\gamma)(1-e^{-\gamma t})$. Derivando esta expresión obtenemos $x'=v_0e^{-\gamma t}=v$, y al derivar nuevamente se cumple $mx''=-\lambda x'$. También se recupera $x(0)=x_0$. Hemos construido y verificado una solución; para este ejemplo puede probarse su unicidad multiplicando la ecuación de velocidad por $e^{\gamma t}$: la derivada de $e^{\gamma t}v(t)$ es cero, de modo que cualquier solución tiene la velocidad encontrada y luego la misma posición inicial fija su integral. La fuerza depende del estado; su historia temporal se conoce después de resolver.

[]{#fispm-t1-c09-e0016}

**Ejercicio 9.16.** En un marco inercial, dos partículas de la misma masa obedecen la ley prescrita $\mathbf F(t)=\mathbf f(t)$ y pasan por la misma posición en $t_0$. Sus velocidades iniciales son $\mathbf v_A$ y $\mathbf v_B$. Encuentra la diferencia de posiciones en otro instante. ¿Qué dato falta si un enunciado pide una trayectoria única y sólo proporciona la posición inicial?

**Solución.** proposición 9.6 da la misma contribución integral de fuerza para ambas historias. Al restar, se obtiene $\mathbf r_A(t)-\mathbf r_B(t)=(t-t_0)(\mathbf v_A-\mathbf v_B)$. Si las velocidades difieren, las posiciones difieren para todo $t\ne t_0$. La posición inicial no determina la velocidad inicial, y ese es el dato que falta en el problema descrito. Esto no constituye una falla de unicidad de un problema de valores iniciales completo: son problemas con datos distintos. Separar datos ausentes de una posible falta de unicidad con datos iguales será decisivo al discutir el determinismo clásico.

Las ocho secciones fijan ahora el lenguaje necesario para continuar: sistema y entorno, marco inercial, masa constante, receptor de cada fuerza, ley de interacción, resultante, estado y datos iniciales. La siguiente etapa estudiará qué condiciones convierten esa formulación en una evolución local única y hasta dónde puede prolongarse la solución.

[]{#regularidad-de-la-fuerza-y-unicidad-local}

[]{#fispm-t1-c09-s09}

[]{#fpm-i-09-s09}

## 9. Regularidad de la fuerza y unicidad local {#fispm-c09-regularidad-de-la-fuerza-y-unicidad-local}

La palabra «determinismo» resume una expectativa: una vez fijados el modelo y el estado inicial, la evolución no debería admitir elecciones adicionales. En §8 aprendimos a formular esa expectativa como un problema de valores iniciales. Nos falta justificarla. La segunda ley no impone por sí sola cuán regular es la función de fuerza, y distintas funciones continuas pueden conducir a comportamientos matemáticos diferentes.

Antes de comparar dos estados hay que resolver una pequeña dificultad dimensional. La posición tiene dimensión de longitud y la velocidad de longitud dividida por tiempo; sumar directamente sus normas no define una magnitud físicamente homogénea. Elegiremos escalas positivas y compararemos variables adimensionales. El cambio no altera la pregunta de unicidad, pero evita esconder unidades dentro de una norma.

[]{#fispm-t1-c09-d0010}

**Definición 9.10 --- Estado normalizado y norma de comparación.** Elegidas escalas $L,T>0$ y un instante de referencia $t_*$, ponemos $$u=\frac{t-t_*}{T},\qquad X=\frac{\mathbf r}{L},\qquad W=\frac{T\mathbf v}{L},\qquad w=(X,W).$$ En $\mathbb R^{2d}$ usamos la norma $\|w\|_*=\max\{\|X\|,\|W\|\}$, donde las normas de cada entrada son euclídeas. El sistema físico se transforma en $$\frac{dw}{du}=g(u,w),\qquad g(u,X,W)=\left(W,\frac{T^2}{mL}\mathbf F(t_*+Tu,LX,(L/T)W)\right).$$ Las primas de las variables normalizadas se referirán a $u$. La primera componente de $g$ es $W$ porque $d(\mathbf r/L)/du=T\mathbf v/L$; la segunda resulta de derivar $T\mathbf v/L$ con respecto a $u$. Todos los componentes de esta nueva ecuación son adimensionales. Al deshacer el cambio recuperamos exactamente el problema físico.

[]{#fispm-t1-c09-d0011}

**Definición 9.11 --- Control de Lipschitz local en el estado.** Un campo continuo $g$ en un abierto $U\subset\mathbb R\times\mathbb R^{2d}$ es localmente Lipschitz en el estado, uniformemente en el tiempo local, si alrededor de cada $(u_0,w_0)\in U$ existe un cilindro $[u_0-a,u_0+a]\times\overline B_r(w_0)\subset U$ y una constante $K\ge0$ tales que $$\|g(u,w)-g(u,\widetilde w)\|_*\le K\|w-\widetilde w\|_*$$ para todo $u$ y todo par de estados del cilindro. Aquí $a,r>0$ y la bola se toma en la norma de la definición 9.10.

La desigualdad controla cuánto cambia el campo cuando se modifica el estado. No exige que $g$ sea diferenciable. Una dependencia continuamente diferenciable en el estado, con derivada continua conjuntamente en tiempo y estado, proporciona ese control en cilindros pequeños: la derivada queda acotada en un cilindro compacto y el segmento entre estados permanece en su bola convexa. No basta con saber que cada corte temporal es Lipschitz si las constantes carecen de control común cerca del instante inicial.

[]{#fispm-t1-c09-p0010}

**Proposición 9.10 --- Estimación de separación y unicidad.** Sean $w,\widetilde w$ dos soluciones en un mismo intervalo que contiene $u_0$, con sus gráficos en un cilindro donde vale definición 9.11 con constante $K$. Entonces $$\|w(u)-\widetilde w(u)\|_*\le \|w(u_0)-\widetilde w(u_0)\|_*e^{K|u-u_0|}.$$ En particular, si sus datos iniciales coinciden, las historias coinciden mientras se mantengan estas hipótesis.

**Estrategia.** proposición 9.9 permite comparar integrales en lugar de derivar una norma, que puede no ser diferenciable. Después dominaremos la distancia por una función auxiliar cuya derivada sí podemos calcular.

**Demostración.** Para $u\ge u_0$, sea $d(u)=\|w(u)-\widetilde w(u)\|_*$ y $A=d(u_0)$. Restando las fórmulas integrales y usando definición 9.11, $$d(u)\le A+K\int_{u_0}^u d(s)\,ds=:h(u).$$ La función $h$ es $C^1$, no negativa y satisface $h'=Kd\le Kh$. Por la regla del producto, la derivada de $e^{-K(u-u_0)}h(u)$ es no positiva. Como $h(u_0)=A$, resulta $d(u)\le h(u)\le Ae^{K(u-u_0)}$. El argumento incluye $K=0$. Para $u\le u_0$ introducimos $q=u_0-u$ y las historias con tiempo invertido; su campo es $-g(u_0-q,\cdot)$, que conserva la constante $K$. Aplicando el mismo argumento obtenemos el valor absoluto del tiempo. Si $A=0$, la cota obliga a $d=0$. $\square$

La prueba es una forma elemental de la desigualdad de Gronwall. Su interés físico no se limita a demostrar unicidad: compara historias con datos ligeramente distintos durante un intervalo en el que el modelo y la cota siguen siendo válidos. El factor exponencial es una cota superior, no una afirmación de que toda separación crezca exponencialmente ni una prueba de caos.[^6]

[]{#fispm-t1-c09-mp0009}

**Principio metodológico 9.9 --- Precisar el alcance de la unicidad.** Comprueba el control local de la fuerza, el dominio y la coincidencia de todos los datos antes de afirmar una historia única. Una desigualdad de separación necesita que ambas soluciones permanezcan en la región donde se obtuvo su constante.

[]{#ejercicios-8}

### Ejercicios {#fispm-c09-ejercicios-8}

[]{#fispm-t1-c09-e0017}

**Ejercicio 9.17.** En una dimensión, considera el modelo adimensional $X''=\sqrt{\max\{X,0\}}$, con $X(0)=X'(0)=0$. Para cada $a\ge0$, verifica que $$X_a(u)=\begin{cases}0,&u\le a,\\(u-a)^4/144,&u\ge a\end{cases}$$ es una solución $C^2$. Explica por qué no contradice proposición 9.10 y escribe una fuerza física dimensionalmente compatible.

**Solución.** A la derecha de $a$, $X_a'=(u-a)^3/36$ y $X_a''=(u-a)^2/12$. A la izquierda ambas derivadas son cero. Sus valores laterales coinciden en $a$, así que la historia es $C^2$ allí. Como $X_a\ge0$, su raíz cuadrada a la derecha es $(u-a)^2/12$, igual a $X_a''$; a la izquierda ambos lados se anulan. Todos los datos en cero coinciden, pero las historias comienzan a apartarse de cero en tiempos diferentes. El campo de estado es $g(X,W)=(W,\sqrt{\max\{X,0\}})$. No es Lipschitz cerca de cero: el cociente $\sqrt h/h=1/\sqrt h$ no permanece acotado cuando $h\downarrow0$. Una fuerza compatible es $F(x)=mL T^{-2}\sqrt{\max\{x/L,0\}}$. La multiplicidad pertenece a este modelo continuo no Lipschitz; el ejercicio no establece que un dispositivo físico real pueda permanecer y arrancar de ese modo.

[]{#fispm-t1-c09-e0018}

**Ejercicio 9.18.** Para $g(X,W)=(W,-\alpha X-\beta W)$, con $\alpha,\beta\ge0$ adimensionales, encuentra una constante de Lipschitz en la norma de la definición 9.10. Usa proposición 9.10 para acotar la separación de dos estados cuya diferencia inicial tiene norma $\varepsilon$.

**Solución.** La primera componente de la diferencia tiene magnitud $|\Delta W|\le\|\Delta w\|_*$. La segunda tiene magnitud a lo sumo $\alpha|\Delta X|+\beta|\Delta W|\le(\alpha+\beta)\|\Delta w\|_*$. Por tanto sirve $K=\max\{1,\alpha+\beta\}$. Proposición 9.10 da $\|\Delta w(u)\|_*\le\varepsilon e^{K|u-u_0|}$ en todo intervalo común de existencia. La constante es global para este campo, aunque la proposición por sí sola no construye soluciones ni demuestra existencia global. Si $\varepsilon=0$, ya sabemos que dos soluciones existentes coinciden; aún falta la construcción que abordaremos ahora.

[]{#existencia-local-prolongación-y-frontera-del-dominio}

[]{#fispm-t1-c09-s10}

[]{#fpm-i-09-s10}

## 10. Existencia local, prolongación y frontera del dominio {#fispm-c09-existencia-local-prolongaciuxf3n-y-frontera-del-dominio}

Una prueba de unicidad responde qué ocurriría si dos soluciones existieran. No construye una. Para completar el determinismo local necesitaremos producir al menos una historia que satisfaga la ecuación y el dato inicial. La forma integral de §8 sugiere un procedimiento: comenzar con una historia sencilla, evaluar en ella el campo y usar esa integral para mejorar la historia. La regularidad nos permitirá controlar las diferencias entre mejoras sucesivas.

[]{#fispm-t1-c09-p0011}

**Proposición 9.11 --- Existencia y unicidad local.** Sea $g$ continuo en un abierto $U$ y localmente Lipschitz en el estado según la definición 9.11. Para cada $(u_0,w_0)\in U$ existe $h>0$ y una solución $C^1$ en $[u_0-h,u_0+h]$ con $w(u_0)=w_0$. Dos soluciones con ese dato coinciden en un entorno de $u_0$ y, por continuación de la comparación local, en todo intervalo común de sus dominios.

**Estrategia.** Escogeremos un cilindro seguro, acortaremos el tiempo para que integrar no saque las historias de él y probaremos la convergencia de las iteraciones mediante una serie geométrica. Así no necesitamos invocar sin explicación un teorema general de punto fijo.

**Demostración.** Tomemos el cilindro de la definición 9.11, con radios $a,r$ y constante $K$. La continuidad en ese compacto da una cota $M$ para $\|g\|_*$. Elegimos $0<h\le a$ de modo que $hM\le r$ y $q=hK<1$; si $M$ o $K$ son cero, la restricción correspondiente es automática. Para una historia continua $\phi$ con valores en $\overline B_r(w_0)$, definimos $$(\mathcal A\phi)(u)=w_0+\int_{u_0}^u g(s,\phi(s))\,ds.$$ La cota $hM\le r$ muestra que $\mathcal A\phi$ sigue en la bola. Con la norma uniforme $\|\phi\|_\infty=\sup_{|u-u_0|\le h}\|\phi(u)\|_*$, el control de Lipschitz da $$\|\mathcal A\phi-\mathcal A\psi\|_\infty\le q\|\phi-\psi\|_\infty.$$ Partimos de $\phi_0(u)=w_0$ y ponemos $\phi_{n+1}=\mathcal A\phi_n$. Por inducción, $\|\phi_{n+1}-\phi_n\|_\infty\le q^n\|\phi_1-\phi_0\|_\infty$. Al sumar diferencias desde $n$ hasta un índice posterior, la serie geométrica acota toda cola por $q^n\|\phi_1-\phi_0\|_\infty/(1-q)$. Las historias forman una sucesión uniformemente de Cauchy. La completitud de $\mathbb R^{2d}$ proporciona límites puntuales, y la cota uniforme de las colas asegura convergencia uniforme a una historia continua $\phi$; la bola cerrada contiene sus valores.

La desigualdad de contracción implica $\mathcal A\phi_n\to\mathcal A\phi$ uniformemente. Como $\mathcal A\phi_n=\phi_{n+1}\to\phi$, tenemos $\phi=\mathcal A\phi$. Proposición 9.9 convierte esta igualdad integral en la solución $C^1$ buscada. Dos puntos fijos en la bola coinciden porque su distancia uniforme $D$ satisface $D\le qD$ con $q<1$. Cualquier otra solución con el dato inicial permanece en ese cilindro durante un tiempo pequeño por continuidad y coincide allí por la proposición 9.10.

Finalmente, para comparar dos soluciones en un intervalo común, el conjunto de tiempos donde sus estados coinciden es cerrado por continuidad y abierto, relativamente al intervalo, por la unicidad local recién probada. Contiene $u_0$; la conexión de un intervalo obliga a que sea todo el intervalo. $\square$

La construcción asegura un tiempo pequeño, no el mayor tiempo posible. Las restricciones sobre $h$ bastan para la prueba y pueden ser muy conservadoras. Si el campo crece cerca de una frontera o la solución se desplaza fuera del cilindro, se elige otro cilindro y se repite el argumento. La unicidad permite pegar las historias obtenidas sin escoger entre continuaciones incompatibles.

[]{#fispm-t1-c09-d0012}

**Definición 9.12 --- Solución maximal.** Una solución con dato inicial fijo es maximal si no puede extenderse a un intervalo abierto mayor que contiene su dominio, conservando la ecuación, el dato y la pertenencia a $U$. Se entiende que las soluciones de la proposición 9.11 se restringen primero a intervalos abiertos. La unión de todas las prolongaciones compatibles produce una solución maximal, pues proposición 9.11 hace coincidir las historias en sus solapamientos.

[]{#fispm-t1-c09-p0012}

**Proposición 9.12 --- Criterio de prolongación en un extremo finito.** Bajo proposición 9.11, sea una solución definida hasta un extremo derecho finito $b$. Si su gráfico en un tramo final permanece en un compacto $C\subset U$, entonces se prolonga más allá de $b$. En consecuencia, una solución maximal con extremo finito no puede permanecer en ningún compacto interior de su dominio de ecuación.

**Demostración.** El campo continuo está acotado en $C$ por algún $M$. Para tiempos $u,v$ del tramo final, la fórmula integral da $\|w(u)-w(v)\|_*\le M|u-v|$. Por ello $w(u)$ tiene un límite $w_b$ al acercarse a $b$; se usa la completitud del espacio de estados. Como $C$ es cerrado, $(b,w_b)\in C\subset U$. Proposición 9.11 construye una solución nueva alrededor de ese punto. La historia anterior, extendida hasta $b$ mediante su límite, sigue satisfaciendo la fórmula integral: el integrando converge a $g(b,w_b)$ y es continuo hasta el extremo. Las dos historias coinciden a la izquierda de $b$ por la unicidad local y pueden pegarse. El resultado prolonga la solución. El argumento contradice la maximalidad si ésta se suponía. $\square$

[]{#fispm-t1-c09-mp0010}

**Principio metodológico 9.10 --- Separar tiempo matemático y validez física.** Una solución puede alcanzar una singularidad o la frontera de la ecuación; también puede seguir existiendo matemáticamente cuando el modelo físico ha dejado de ser adecuado. Declara cuál de esas causas limita la predicción. «Única» no significa «global» ni «válida para cualquier tiempo».

[]{#ejercicios-9}

### Ejercicios {#fispm-c09-ejercicios-9}

[]{#fispm-t1-c09-e0019}

**Ejercicio 9.19.** Considera $X'=W$, $W'=W^2$, con $X(0)=0$, $W(0)=1$. Encuentra su solución y su intervalo maximal que contiene cero. ¿Cómo se reconcilia el resultado con que el campo sea suave en todo $\mathbb R^2$?

**Solución.** La función $W(u)=1/(1-u)$ satisface $W'=W^2$ y el dato inicial. Integrando $X'=W$, resulta $X(u)=-\log(1-u)$ para $u<1$. Proposición 9.11 garantiza que ésta es la única solución con esos datos. Está definida en $(-\infty,1)$, y cuando $u\uparrow1$ tanto $W$ como $X$ crecen sin cota. No admite prolongación con estado finito a través de uno, de modo que ese intervalo es maximal. El campo suave garantiza Lipschitz local, pero no una cota global de crecimiento. Proposición 9.12 no fuerza una prolongación porque el gráfico abandona todo compacto. El modelo físico asociado sería $F(v)=(m/T)(L/T)(Tv/L)^2$; su validez a velocidades ilimitadas no se afirma.

[]{#fispm-t1-c09-e0020}

**Ejercicio 9.20.** El modelo $X''=0$ se declara sólo en el dominio $X<1$, con $X(0)=0$, $X'(0)=1$. Encuentra su historia y su intervalo maximal dentro del dominio. Compara la obstrucción con la del ejercicio 9.19.

**Solución.** La historia es $X(u)=u$, $W(u)=1$, por integración o por la proposición 9.6. Permanece en el dominio exactamente para $u<1$, así que el intervalo maximal que contiene cero es $(-\infty,1)$. El estado tiene un límite finito $(1,1)$, pero ese límite está fuera del dominio declarado. No hay un compacto interior que contenga el gráfico del tramo final, por lo que proposición 9.12 no impone una prolongación. A diferencia del ejercicio 9.19, no aparece divergencia del estado: aparece una frontera del modelo. Podríamos escribir la misma fórmula más allá de uno si ampliáramos el dominio de la ecuación, pero eso sería un problema distinto que requiere justificar la ampliación.

[]{#cambios-galileanos-y-covariancia-del-modelo}

[]{#fispm-t1-c09-s11}

[]{#fpm-i-09-s11}

## 11. Cambios galileanos y covariancia del modelo {#fispm-c09-cambios-galileanos-y-covariancia-del-modelo}

La primera ley admite una familia de marcos inerciales relacionados por traslaciones uniformes y cambios fijos de orientación. La segunda ley debe leerse con esa libertad en mente. Dos observadores pueden atribuir velocidades diferentes a una misma partícula, sin discrepar acerca de su aceleración vectorial después de traducir componentes. Pero una función de fuerza que depende de la velocidad también necesita transformarse: la igualdad de aceleraciones no autoriza a conservar sin examen la misma expresión del lado derecho.

[]{#fig:I-09-N03}

<figure id="fig-fpm-v04-i-09-n03" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-09-N03.svg" class="lightbox" data-gallery="fpm-v04-c09"><img src="/assets/books/fispm/v04/I-09-N03.svg" alt="Cambiar de observador. Diagrama del capítulo 9; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="395" height="252" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 9.5.** Para un movimiento uniforme $X=2u$, el marco que avanza con velocidad normalizada uno mide $X\prime=u$. Las pendientes cambian; la aceleración es cero en ambos marcos. Véase §[11](#fispm-c09-cambios-galileanos-y-covariancia-del-modelo).

</figcaption>

</figure>

Sea un cambio de coordenadas con reloj común, $$\mathbf r=\mathbf c_0+(t-t_0)\mathbf u+Q\mathbf y,$$ donde $Q$ es ortogonal constante y $\mathbf u$ constante. El vector $\mathbf y$ contiene las coordenadas de posición en el nuevo marco. Si denotamos $\mathbf w=\mathbf y'$, entonces $\mathbf v=\mathbf u+Q\mathbf w$ y $\mathbf a=Q\mathbf y''$. Aquí $\mathbf w$ es una velocidad física, distinta del estado normalizado $w$ sin negrita de §§9--10.

[]{#fispm-t1-c09-p0013}

**Proposición 9.13 --- Transformación de una ecuación newtoniana.** Una historia satisface $m\mathbf r''=\mathbf F(t,\mathbf r,\mathbf r')$ si y sólo si su representación $\mathbf y$ satisface $m\mathbf y''=\widetilde{\mathbf F}(t,\mathbf y,\mathbf y')$, donde $$\widetilde{\mathbf F}(t,\mathbf y,\mathbf w)= Q^{\mathsf T}\mathbf F\bigl(t,\mathbf c_0+(t-t_0)\mathbf u+Q\mathbf y,\mathbf u+Q\mathbf w\bigr).$$ Sus datos iniciales se transforman en $\mathbf y_0=Q^{\mathsf T}(\mathbf r_0-\mathbf c_0)$ y $\mathbf w_0=Q^{\mathsf T}(\mathbf v_0-\mathbf u)$.

**Demostración.** Derivar dos veces el cambio afín da $\mathbf r''=Q\mathbf y''$. Sustituimos posiciones y velocidades en la fuerza y multiplicamos la ecuación por $Q^{\mathsf T}$. La igualdad $Q^{\mathsf T}Q=\mathrm{Id}$ produce la ecuación anunciada. Cada paso es reversible porque $Q$ es invertible y el cambio temporal es el mismo reloj. Evaluar posición y velocidad en $t_0$ proporciona los datos escritos. El dominio nuevo es la preimagen del dominio original bajo el cambio de tiempo y estado. $\square$

La masa se conserva como escalar del modelo y la fuerza cambia sus componentes con $Q^{\mathsf T}$. Esto es covariancia: ambas representaciones describen la misma ecuación física con sus argumentos correctamente transformados. Una exigencia diferente es que una familia de leyes conserve la misma forma funcional al efectuar el cambio. Esa propiedad requiere examinar la interacción, incluidas las variables de su entorno.[^7]

[]{#fispm-t1-c09-p0014}

**Proposición 9.14 --- Misma forma para interacciones relativas equivariantes.** Supongamos que las fuerzas internas de un sistema son $\mathbf F_{i\leftarrow j}=\Phi_{ij}(\mathbf r_i-\mathbf r_j,\mathbf v_i-\mathbf v_j)$, y que para todo cambio ortogonal considerado la función satisface $$\Phi_{ij}(Q\rho,Q\nu)=Q\Phi_{ij}(\rho,\nu).$$ Entonces, bajo el cambio común de la proposición 9.13, las componentes de cada fuerza tienen la misma regla $\Phi_{ij}(\mathbf y_i-\mathbf y_j,\mathbf w_i-\mathbf w_j)$ en el nuevo marco.

**Demostración.** Restar dos posiciones elimina $\mathbf c_0+(t-t_0)\mathbf u$ y deja $Q(\mathbf y_i-\mathbf y_j)$. Restar dos velocidades elimina $\mathbf u$ y deja $Q(\mathbf w_i-\mathbf w_j)$. La hipótesis de equivariancia convierte la fuerza original en $Q\Phi_{ij}(\mathbf y_i-\mathbf y_j,\mathbf w_i-\mathbf w_j)$. Multiplicar por $Q^{\mathsf T}$, como prescribe proposición 9.13, elimina $Q$ y prueba la afirmación. $\square$

La hipótesis acerca de $\Phi_{ij}$ no se deduce de que la fuerza sea un vector. Una ley que incluya una dirección externa fija debe transformar también esa dirección. Además, la equivariancia no establece por sí sola la tercera ley: para la pareja habría que comprobar una relación entre $\Phi_{ij}$ y $\Phi_{ji}$. Los postulados y simetrías son obligaciones distintas.

[]{#fispm-t1-c09-mp0011}

**Principio metodológico 9.11 --- Transformar el entorno con la partícula.** Al cambiar de marco, transforma las velocidades, posiciones y direcciones de los agentes que aparecen en la ley. No conviertas una dependencia respecto de un medio en una dependencia respecto de un reposo absoluto por omitir el parámetro del medio.

[]{#ejercicios-10}

### Ejercicios {#fispm-c09-ejercicios-10}

[]{#fispm-t1-c09-e0021}

**Ejercicio 9.21.** En un plano, $Q$ gira $90^\circ$ en sentido positivo, $\mathbf c_0=0$, $\mathbf u=Ue_1$ y la fuerza original es $Fe_1$ constante. Si $\mathbf r_0=ae_1$ y $\mathbf v_0=Ve_2$, encuentra la fuerza y los datos en el nuevo marco.

**Solución.** En las coordenadas originales $Q=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)$, por lo que $Q^{\mathsf T}e_1=-e_2$ y $Q^{\mathsf T}e_2=e_1$. Proposición 9.13 da $\widetilde{\mathbf F}=-Fe_2$, $\mathbf y_0=-ae_2$ y $\mathbf w_0=Ve_1+Ue_2$. La aceleración nueva es $-(F/m)e_2$. La traslación uniforme modifica la velocidad inicial; la rotación fija modifica las componentes de fuerza y aceleración. Ninguna de ambas produce términos adicionales de aceleración.

[]{#fispm-t1-c09-e0022}

**Ejercicio 9.22.** Se declara el modelo $\mathbf F=-\lambda(\mathbf v-\mathbf V_m)$, con $\lambda>0$ y velocidad constante del medio $\mathbf V_m$. Transfórmalo mediante proposición 9.13. Explica el error de conservar $\mathbf F=-\lambda\mathbf v$ en dos marcos con velocidad relativa no nula cuando sólo en el primero el medio está en reposo.

**Solución.** La velocidad del medio en el segundo marco es $\widetilde{\mathbf V}_m=Q^{\mathsf T}(\mathbf V_m-\mathbf u)$. Sustituyendo $\mathbf v=\mathbf u+Q\mathbf w$ y multiplicando por $Q^{\mathsf T}$, resulta $\widetilde{\mathbf F}=-\lambda(\mathbf w-\widetilde{\mathbf V}_m)$. La regla conserva su forma en términos de velocidad relativa al medio. Si $\mathbf V_m=0$ en el primer marco, en el segundo vale $-Q^{\mathsf T}\mathbf u$, que no es cero si $\mathbf u\ne0$. Omitirla cambia el modelo y las fuerzas predichas; no es otra representación del mismo experimento.

[]{#fispm-t1-c09-e0023}

**Ejercicio 9.23.** Una pareja admite el modelo $\Phi(\rho,\nu)=\kappa\rho+\mu\nu$, con $\rho=\mathbf r_A-\mathbf r_B$, $\nu=\mathbf v_A-\mathbf v_B$, $\kappa,\mu$ escalares constantes y pareja opuesta. Comprueba la equivariancia y la tercera ley débil. ¿La fuerza es necesariamente central?

**Solución.** La linealidad da $\Phi(Q\rho,Q\nu)=\kappa Q\rho+\mu Q\nu=Q\Phi(\rho,\nu)$, de modo que proposición 9.14 se aplica. Intercambiar cuerpos cambia $(\rho,\nu)$ por $(-\rho,-\nu)$ y la función por su negativo; la pareja cumple la tercera ley. Si $\mu\ne0$ y $\nu$ no es paralela a $\rho$, la fuerza no es paralela a la separación y no es central. Para unidades compatibles, $[\kappa]=MT^{-2}$ y $[\mu]=MT^{-1}$. El ejemplo prueba compatibilidades algebraicas del modelo propuesto, no su realización para cualquier interacción material.

[]{#equilibrio-reposo-y-movimiento-uniforme}

[]{#fispm-t1-c09-s12}

[]{#fpm-i-09-s12}

## 12. Equilibrio, reposo y movimiento uniforme {#fispm-c09-equilibrio-reposo-y-movimiento-uniforme}

Un cuerpo que se detiene por un instante puede empezar a moverse de inmediato. Un cuerpo que tiene aceleración cero en cierto instante puede tener aceleración no nula un momento después. Y un cuerpo cuya resultante se anula durante un intervalo puede estar moviéndose uniformemente. Las tres afirmaciones son compatibles con Newton; la confusión aparece cuando una condición puntual se interpreta como una historia completa.

[]{#fispm-t1-c09-d0013}

**Definición 9.13 --- Equilibrio de una partícula en un marco.** En el modelo de masa constante y marco inercial, una historia de equilibrio es una posición constante $\mathbf r(t)=\mathbf r_e$ que satisface la ecuación de movimiento en todo el intervalo considerado. Por tanto su velocidad y aceleración son nulas allí. La definición se refiere a ese marco y a ese modelo; no incluye aquí la estabilidad frente a perturbaciones.

[]{#fispm-t1-c09-p0015}

**Proposición 9.15 --- Criterio de equilibrio.** Para una ley $\mathbf F(t,\mathbf r,\mathbf v)$, la historia constante $\mathbf r_e$ es solución en un intervalo $I$ si y sólo si $\mathbf F(t,\mathbf r_e,0)=0$ para todo $t\in I$ y sus estados pertenecen al dominio. Si la ley es autónoma, el criterio se reduce a $\mathbf F(\mathbf r_e,0)=0$. Bajo las hipótesis de la proposición 9.11, el dato inicial $(\mathbf r_e,0)$ tiene esa historia como su única solución mientras pueda continuarse en el intervalo.

**Demostración.** La historia constante tiene segunda derivada cero. Sustituirla en Newton muestra que la condición es necesaria y suficiente, conservando la exigencia de dominio. Si no hay dependencia temporal, la misma igualdad se comprueba una sola vez en el estado fijo. La última afirmación resulta de la unicidad de la proposición 9.11, aplicada después de la normalización invertible de la definición 9.10. $\square$

La igualdad de la fuerza con cero en un único estado y un único tiempo no basta para el caso no autónomo. El entorno puede cambiar más tarde. Incluso en el caso autónomo, fijar la posición sin fijar velocidad cero tampoco selecciona una historia de equilibrio. Ejercicio 9.16 ya mostró que posiciones iniciales iguales pueden dar historias distintas.

[]{#fispm-t1-c09-p0016}

**Proposición 9.16 --- Criterio de movimiento uniforme.** La historia $\mathbf r(t)=\mathbf r_0+(t-t_0)\mathbf v_0$ satisface la segunda ley si y sólo si pertenece al dominio y $$\mathbf F(t,\mathbf r_0+(t-t_0)\mathbf v_0,\mathbf v_0)=0$$ para todo instante del intervalo. En un cambio galileano, una historia de equilibrio puede transformarse en un movimiento uniforme con velocidad no nula.

**Demostración.** La segunda derivada de la historia afín es cero; sustituirla en la ecuación prueba ambas direcciones. Para la última afirmación, la transformación de la proposición 9.13 aplicada a $\mathbf r(t)=\mathbf r_e$ da $\mathbf y(t)=Q^{\mathsf T}(\mathbf r_e-\mathbf c_0)-(t-t_0)Q^{\mathsf T}\mathbf u$. Su velocidad es constante y no nula cuando $\mathbf u\ne0$. Proposición 9.13 garantiza que esa historia satisface el modelo transformado. $\square$

[]{#fispm-t1-c09-mp0012}

**Principio metodológico 9.12 --- Conservar el cuantificador temporal.** Distingue «en este instante» de «en todo el intervalo». Para demostrar equilibrio verifica la resultante sobre el estado constante durante el intervalo; para movimiento uniforme verifícala a lo largo de la historia afín. No confundas ninguno de esos criterios con estabilidad.

En un sistema de varias partículas, que se anule la suma de fuerzas externas no establece por sí solo equilibrio de cada partícula. Proposición 9.7 y ejercicio 9.13 ya exhibieron aceleraciones internas opuestas. También habrá que controlar las condiciones particulares de cada receptor. Las restricciones y fuerzas de contacto se introducirán en los capítulos siguientes antes de aplicarlas como si fueran datos evidentes.

[]{#ejercicios-11}

### Ejercicios {#fispm-c09-ejercicios-11}

[]{#fispm-t1-c09-e0024}

**Ejercicio 9.24.** Sobre una partícula actúan dos contribuciones constantes $\mathbf F_1=Fe_1$ y $\mathbf F_2=-Fe_1$. Su velocidad inicial es $Ue_2$, con $U\ne0$. ¿Tiene aceleración nula? ¿Es una historia de equilibrio en este marco? ¿Hay un marco galileano en que lo sea?

**Solución.** La resultante se anula en todo instante y proposición 9.6 da $\mathbf r=\mathbf r_0+(t-t_0)Ue_2$. Su aceleración es nula, pero su posición no es constante: no es equilibrio según la definición 9.13. Elegimos un origen que se traslada con velocidad $Ue_2$ y ejes paralelos; en ese marco la velocidad de la partícula es cero y su posición constante. Al transformar ambas contribuciones y sus agentes, la resultante sigue siendo cero y la historia sí es de equilibrio. El cuerpo no es libre por tener resultante nula: siguen existiendo dos interacciones incluidas.

[]{#fispm-t1-c09-e0025}

**Ejercicio 9.25.** En una recta, $F(t,x,v)=F_0t/T$, con $F_0,T>0$, y $x(0)=v(0)=0$. Verifica que posición, velocidad, aceleración y fuerza son cero en el instante inicial. ¿La historia es de equilibrio?

**Solución.** proposición 9.6 da $v(t)=F_0t^2/(2mT)$ y $x(t)=F_0t^3/(6mT)$. Su aceleración es $F_0t/(mT)$ y su fuerza $F_0t/T$, de modo que todas las cantidades indicadas se anulan en cero. Para cualquier tiempo positivo, la posición y velocidad son positivas, así que no hay equilibrio. Proposición 9.15 habría exigido $F(t,0,0)=0$ en todo el intervalo; esa condición fracasa. El ejercicio muestra que acumular ceros instantáneos no reemplaza el cuantificador temporal del criterio.

[]{#reconstrucción-dinámica-y-contraste-de-modelos}

[]{#fispm-t1-c09-s13}

[]{#fpm-i-09-s13}

## 13. Reconstrucción dinámica y contraste de modelos {#fispm-c09-reconstrucciuxf3n-dinuxe1mica-y-contraste-de-modelos}

Una ecuación bien planteada puede producir una solución única y, aun así, describir mal el experimento. La existencia y unicidad pertenecen a la estructura matemática del modelo; su adecuación física exige confrontar las interacciones propuestas con información independiente. Ahora reuniremos esa distinción con los problemas inversos de §1 y con el control de aproximaciones del capítulo 6.

Hay dos comparaciones diferentes. Podemos mantener la misma ley y cambiar el dato inicial, como en la proposición 9.10. También podemos cambiar la ley misma: sustituir una fuerza por una aproximación, modificar un parámetro o incluir una contribución omitida. Para distinguir sus efectos conservaremos por separado una diferencia inicial y una cota sobre la diferencia entre campos de evolución normalizados.

[]{#fispm-t1-c09-p0017}

**Proposición 9.17 --- Comparación entre dos modelos de evolución.** Sean $w,\widetilde w$ soluciones de $w'=g(u,w)$ y $\widetilde w'=\widetilde g(u,\widetilde w)$ en un intervalo común que contiene $u_0$. Supongamos que ambas permanecen en una región donde $g$ tiene constante de Lipschitz $K\ge0$ y donde $\|g(u,z)-\widetilde g(u,z)\|_*\le\delta$ para todos los estados relevantes. Si $A=\|w(u_0)-\widetilde w(u_0)\|_*$ y $\tau=|u-u_0|$, entonces $$\|w(u)-\widetilde w(u)\|_*\le \begin{cases} Ae^{K\tau}+\dfrac{\delta}{K}(e^{K\tau}-1),&K>0,\\ A+\delta\tau,&K=0. \end{cases}$$

**Demostración.** Para tiempos posteriores a $u_0$, la fórmula integral y la suma y resta de $g(s,\widetilde w(s))$ dan $$d(u)\le A+\delta(u-u_0)+K\int_{u_0}^u d(s)\,ds=:h(u),$$ donde $d$ es la norma de la diferencia. La función auxiliar satisface $h'=\delta+Kd\le\delta+Kh$. Así, $$\frac{d}{du}\bigl(e^{-K(u-u_0)}h(u)\bigr)\le\delta e^{-K(u-u_0)}.$$ Integrando entre $u_0$ y $u$ y multiplicando por el exponencial, obtenemos la primera cota si $K>0$ y la segunda si $K=0$. En ambos casos $d\le h$. Para tiempos anteriores, invertimos el tiempo como en la proposición 9.10; cambian los signos de los campos pero no las cotas de Lipschitz ni de diferencia. $\square$

La cota separa el error en el dato del error en la ecuación. Si la diferencia de fuerzas físicas está acotada por $\Delta F$ y se conservan masa y escalas, la diferencia de campos normalizados debida a esa fuerza queda acotada por $\delta=T^2\Delta F/(mL)$. Una diferencia de masa exige recalcular también la aceleración; no puede introducirse como si fuera sólo una fuerza adicional sin justificarlo. La estructura de la proposición 9.17 se apoya en el mismo mecanismo de Gronwall presentado por Spivak para comparar ecuaciones.[^8]

Volvamos ahora a una historia medida. Si posee la regularidad suficiente y la masa es conocida, podemos reconstruir $m\mathbf r''$ y compararlo con una fuerza propuesta. La discrepancia es una magnitud útil, pero su interpretación requiere conservar la procedencia de cada término.

[]{#fispm-t1-c09-d0014}

**Definición 9.14 --- Residuo dinámico de una historia.** Para una historia $C^2$ dentro del dominio de una ley de fuerza, definimos $$\mathbf R(t)=m\mathbf r''(t)-\mathbf F(t,\mathbf r(t),\mathbf r'(t)).$$ Tiene dimensiones de fuerza. Se anula idénticamente si y sólo si la historia satisface la ecuación de Newton del modelo en ese intervalo.

Un residuo no nulo puede deberse a una interacción omitida, una calibración incorrecta, un marco inadecuado o un error de estimación de derivadas. Identificar una causa requiere más información. Un residuo nulo sobre una historia tampoco identifica la función de fuerza fuera de los estados visitados. La curva en el espacio de estados suele proporcionar menos información que una función definida en una región entera.

[]{#fispm-t1-c09-p0018}

**Proposición 9.18 --- Una historia exacta no identifica una ley de fuerza completa.** Supongamos que una historia $\mathbf r_*(t)$ resuelve una ley continua $\mathbf F$ en un dominio abierto sobre un intervalo abierto $I$. Para cualquier escalar constante $\kappa$ de dimensión $MT^{-2}$, la ley $$\mathbf F_\kappa(t,\mathbf r,\mathbf v)= \mathbf F(t,\mathbf r,\mathbf v)+\kappa(\mathbf r-\mathbf r_*(t))$$ produce residuo cero sobre esa misma historia. Para $\kappa$ diferentes, las leyes son distintas en estados del dominio situados fuera de $\mathbf r=\mathbf r_*(t)$.

**Demostración.** La contribución añadida es continua y, al evaluar $\mathbf r=\mathbf r_*(t)$, se anula. Por tanto la igualdad dinámica de la historia original sigue siendo válida para cada $\kappa$. Si $\kappa_1\ne\kappa_2$, la diferencia de las leyes es $(\kappa_1-\kappa_2)(\mathbf r-\mathbf r_*(t))$. Un dominio abierto alrededor de un estado de la historia contiene estados con posiciones diferentes a tiempo y velocidad fijados, donde esa diferencia es no nula. $\square$

El resultado es una obstrucción de identificación, no una propuesta de nuevos mecanismos físicos. Las restricciones experimentales pueden excluir muchas funciones de esta familia. Su utilidad consiste en mostrar por qué una trayectoria perfectamente ajustada no demuestra una ley universal. Para identificar parámetros o dependencias hacen falta variaciones de datos, posiciones, velocidades o configuraciones del entorno.[^9]

[]{#fispm-t1-c09-mp0013}

**Principio metodológico 9.13 --- Contrastar más allá del ajuste.** Separa los datos usados para calibrar la ley de los que ponen a prueba sus predicciones. Informa el residuo y la incertidumbre de su estimación; no conviertas un ajuste sobre una sola historia en evidencia de identificación global ni una cota de estados en una cota automática de tiempos de encuentro.

[]{#ejercicios-12}

### Ejercicios {#fispm-c09-ejercicios-12}

[]{#fispm-t1-c09-e0026}

**Ejercicio 9.26.** Se observa $x_*(t)=L\cos(t/T)$ para una masa $m>0$. Calcula la fuerza reconstruida y encuentra dos leyes diferentes que produzcan residuo cero sobre esa historia. Explica qué nuevo ensayo podría distinguirlas.

**Solución.** Como $x_*''=-(L/T^2)\cos(t/T)$, la fuerza reconstruida es $-(m/T^2)x_*(t)$. Una ley es $F_1(t,x,v)=-(m/T^2)x$. Otra, para $\kappa\ne0$, es $F_2=F_1+\kappa(x-L\cos(t/T))$. Ambas coinciden sobre la historia, pero difieren si se cambia la posición inicial manteniendo el mismo instante y velocidad. En ese nuevo ensayo su diferencia inicial de fuerza sería $\kappa(x_0-L)$ si empieza en cero. El diseño exigiría además comprobar la reproducibilidad del entorno y las hipótesis de cada ley; el cálculo sólo señala una configuración capaz de distinguir sus predicciones.

[]{#fispm-t1-c09-e0027}

**Ejercicio 9.27.** Una historia libre rectilínea $x_*(t)=x_0+v_0t$ se aproxima por $x_\varepsilon(t)=x_*(t)+\varepsilon L\sin(Nt/T)$, donde $\varepsilon>0$ es adimensional y $N$ es un entero positivo. Acota el error de posición y calcula el residuo frente a la ley $F=0$. ¿Un error pequeño de posición garantiza un residuo pequeño?

**Solución.** El error de posición tiene magnitud a lo sumo $\varepsilon L$. Dos derivaciones dan $R_\varepsilon(t)=-m\varepsilon L N^2T^{-2}\sin(Nt/T)$, cuya amplitud es $m\varepsilon L N^2/T^2$. Para $\varepsilon=10^{-3}$ y $N=100$, la posición difiere a lo sumo en una milésima de $L$, pero la amplitud del residuo es $10mL/T^2$. La segunda derivada amplifica las variaciones rápidas. Una reconstrucción desde datos discretos debe especificar cómo estima derivadas y cómo controla su incertidumbre; una cota uniforme de posiciones no proporciona por sí sola esa información.

[]{#fispm-t1-c09-e0028}

**Ejercicio 9.28.** En variables normalizadas se tienen $K=2$, $A=0.01$ y $\delta=0.02$, y ambas historias permanecen en la región de control durante $0\le u-u_0\le0.5$. Aplica proposición 9.17 al final. Traduce la cota a errores de posición y velocidad con las escalas $L,T$ de la definición 9.10.

**Solución.** En $\tau=0.5$ obtenemos $d\le0.01e+(0.02/2)(e-1)=0.02e-0.01$, aproximadamente $0.0444$. Como la norma es el máximo de las dos entradas normalizadas, $\|\Delta\mathbf r\|\le L(0.02e-0.01)$ y $\|\Delta\mathbf v\|\le(L/T)(0.02e-0.01)$. La misma cifra adimensional produce dos cotas con unidades diferentes. La condición de permanencia en la región es parte de la hipótesis; si no se demuestra o comprueba, no podemos extrapolar la estimación a otro tramo.

[]{#síntesis-de-un-problema-newtoniano-completo}

[]{#fispm-t1-c09-s14}

[]{#fpm-i-09-s14}

## 14. Síntesis de un problema newtoniano completo {#fispm-c09-suxedntesis-de-un-problema-newtoniano-completo}

Podemos ahora recorrer un problema desde sus hipótesis hasta su predicción sin confundir los niveles. Elegimos una partícula, un marco inercial y una masa constante. Especificamos una ley de fuerza y los parámetros de su entorno. Comprobamos que los datos pertenecen al dominio, formulamos la ecuación y justificamos la existencia y unicidad donde corresponda. Después calculamos una historia y la verificamos por sustitución; finalmente preguntamos por la validez del modelo y por el contraste con observaciones.

Para dar a esa secuencia un referente concreto, consideremos la clase de modelos $$\mathbf F(t,\mathbf r,\mathbf v)=\mathbf A(t)-\lambda(\mathbf v-\mathbf V_m),$$ con $\lambda>0$, una velocidad de entorno constante $\mathbf V_m$ y una contribución externa prescrita continua $\mathbf A:I\to V$. El origen físico de esas contribuciones tendría que calibrarse en un problema experimental. Aquí la ley es una hipótesis de trabajo para estudiar un problema completo, no una afirmación de que toda resistencia o todo dispositivo tenga esa forma. La fuerza no depende de posición, pero sí de velocidad; no es una fuerza prescrita en el sentido de la definición 9.6.

[]{#fispm-t1-c09-p0019}

**Proposición 9.19 --- Solución de una clase afín dependiente de velocidad.** Sea $\gamma=\lambda/m>0$. Dados $\mathbf r_0,\mathbf v_0$ en $t_0\in I$, el modelo anterior tiene una única solución en $I$, con $$\mathbf v(t)=\mathbf V_m+e^{-\gamma\tau}(\mathbf v_0-\mathbf V_m) +\frac1m\int_{t_0}^t e^{-\gamma(t-s)}\mathbf A(s)\,ds, \qquad \tau=t-t_0,$$ y $$\mathbf r(t)=\mathbf r_0+\tau\mathbf V_m+ \frac{1-e^{-\gamma\tau}}{\gamma}(\mathbf v_0-\mathbf V_m) +\frac1{m\gamma}\int_{t_0}^t\bigl(1-e^{-\gamma(t-s)}\bigr)\mathbf A(s)\,ds.$$

**Estrategia.** Restar la velocidad del medio convierte la ecuación de velocidad en una ecuación lineal con coeficiente constante. Un factor integrante produce la primera fórmula; la segunda se comprueba derivando, sin necesitar intercambiar integrales dobles.

**Demostración.** La segunda ley es $\mathbf v'+\gamma(\mathbf v-\mathbf V_m)=\mathbf A/m$. Multiplicar por $e^{\gamma(t-t_0)}$ convierte el lado izquierdo en la derivada de $e^{\gamma(t-t_0)}(\mathbf v-\mathbf V_m)$. Integrar y recuperar el dato inicial da la fórmula de velocidad. La continuidad de $\mathbf A$ hace que esa expresión sea $C^1$ y satisfaga la ecuación.

Derivamos la expresión de posición. El término lineal aporta $\mathbf V_m$ y el exponencial aporta $e^{-\gamma\tau}(\mathbf v_0-\mathbf V_m)$. El término de borde de la integral es cero, porque su núcleo vale $1-e^0=0$; la derivada del núcleo es $\gamma e^{-\gamma(t-s)}$. Tras cancelar $\gamma$, se obtiene la contribución integral de la velocidad. Así $\mathbf r'=\mathbf v$, la posición es $C^2$ y en $t_0$ toma el valor $\mathbf r_0$. Una segunda derivación recupera Newton.

Para la unicidad, la diferencia de dos velocidades con el mismo dato satisface $\Delta\mathbf v'+\gamma\Delta\mathbf v=0$. El mismo factor integrante tiene derivada cero y valor inicial cero, por lo que las velocidades coinciden. Las posiciones, con igual derivada e igual dato inicial, también coinciden. Las fórmulas están definidas en todo $I$: para cada instante la continuidad garantiza integrales finitas en el segmento entre ese instante y $t_0$, incluidas las integrales orientadas si $t<t_0$. $\square$

En este caso no sólo contamos con un teorema local: la fórmula muestra existencia en todo el intervalo donde se ha dado la contribución continua $\mathbf A$. Esa afirmación matemática no amplía el dominio empírico del modelo. Si el medio cambia, la ley deja de ser lineal en la velocidad o una contribución se vuelve relevante, hay que revisar la hipótesis que permitió el cálculo.[^10]

La constante $\gamma$ tiene dimensión de tiempo inverso; $1/\gamma=m/\lambda$ es la escala temporal que organiza el efecto de la dependencia lineal. Las integrales de velocidad tienen dimensión $F T/m=L/T$ y las de posición dimensión $F T/(m\gamma)=L$. Comprobar esas dimensiones no prueba las fórmulas, pero permite detectar factores ausentes después de haberlas obtenido.

[]{#fispm-t1-c09-mp0014}

**Principio metodológico 9.14 --- Cerrar el ciclo de predicción.** Una solución completa conserva la cadena entre sistema, marco, ley, parámetros, dominio, datos, ecuación, justificación matemática y contraste. La comprobación por sustitución acredita la solución del modelo; la comparación con un experimento acredita, dentro de incertidumbres y escalas, su adecuación física.

[]{#ejercicios-13}

### Ejercicios {#fispm-c09-ejercicios-13}

[]{#fispm-t1-c09-e0029}

**Ejercicio 9.29.** En el modelo de la proposición 9.19 toma $\mathbf A(t)=A_0e_1$, $\mathbf V_m=Ue_2$, $\mathbf r(0)=0$ y $\mathbf v(0)=0$, con $A_0>0$. Define $\mathbf B=(A_0/\lambda)e_1+Ue_2$. Encuentra la historia, verifica su resultante y estudia los regímenes $\gamma t\ll1$ y $\gamma t\gg1$. ¿La velocidad límite representa equilibrio en el marco inicial?

**Solución.** La integral constante de la proposición 9.19 produce $\mathbf v(t)=\mathbf B(1-e^{-\gamma t})$ y $\mathbf r(t)=\mathbf B[t-(1-e^{-\gamma t})/\gamma]$. La resultante es $$A_0e_1-\lambda(\mathbf v-Ue_2)=\lambda\mathbf B e^{-\gamma t},$$ igual a $m\mathbf v'=m\gamma\mathbf B e^{-\gamma t}$. Los datos iniciales se recuperan en cero. Para $\gamma t\ll1$, la expansión del exponencial da $\mathbf v=\gamma\mathbf B t+O(\|\mathbf B\|\gamma^2t^2)$ y $\mathbf r=\tfrac12\gamma\mathbf B t^2+O(\|\mathbf B\|\gamma^2|t|^3)$, entendiendo los restos como cotas en norma para $|\gamma t|$ pequeño. Para tiempos positivos con $\gamma t\gg1$, la velocidad se aproxima a $\mathbf B$ y la posición a $\mathbf B(t-1/\gamma)$, con error exponencialmente pequeño. Como $A_0>0$, $\mathbf B\ne0$: la velocidad límite es la de un movimiento uniforme, no un equilibrio en el marco inicial. Partir directamente con velocidad $\mathbf B$ daría resultante cero y movimiento uniforme exacto; la historia que parte de reposo se aproxima a ese régimen sin alcanzarlo en tiempo finito.

[]{#fispm-t1-c09-e0030}

**Ejercicio 9.30.** Audita este informe: «La fuerza de la proposición 9.19 es prescrita porque sus parámetros son conocidos. Con posición inicial basta para determinar la historia. Como la fuerza es continua, la unicidad y la existencia global quedan garantizadas. En otro marco basta escribir la misma fórmula con la nueva velocidad sin modificar $\mathbf V_m$. Las parejas de tercera ley se cancelan sobre la partícula. La verificación por sustitución demuestra que el modelo describe el experimento». Repara cada afirmación y determina qué conclusión matemática sí está acreditada para el modelo concreto de la proposición 9.19.

**Solución.** Conocer parámetros no equivale a conocer la fuerza como función del tiempo: ésta depende de la velocidad desconocida y no cumple definición 9.6. El problema necesita además la velocidad inicial, como muestran definición 9.9 y ejercicio 9.16. La continuidad sola no garantiza unicidad, según el ejercicio 9.17; aun la suavidad local no garantiza existencia global, según el ejercicio 9.19. Para este modelo particular, proposición 9.19 sí prueba una solución única en todo el intervalo donde $\mathbf A$ sea continua, mediante una fórmula explícita y un factor integrante.

El cambio de marco debe transformar la velocidad del medio, $\widetilde{\mathbf V}_m=Q^{\mathsf T}(\mathbf V_m-\mathbf u)$, y la contribución prescrita, $\widetilde{\mathbf A}=Q^{\mathsf T}\mathbf A$. Con esos parámetros la ley conserva su forma; omitir la velocidad transformada del medio cambia el problema. La pareja de una fuerza externa actúa sobre su agente, fuera de la ecuación de la partícula; no cancela la contribución sobre el receptor. Sólo al ampliar el sistema y sumar ecuaciones podrían cancelarse los pares internos apropiados.

Por último, sustituir la historia en la ecuación demuestra que es una solución de la ley escogida. Para evaluar el experimento se necesitan calibraciones y observaciones independientes, con incertidumbre y dominio de validez. La conclusión acreditada es concreta: dadas la ley afín, sus parámetros, el intervalo de continuidad y ambos datos iniciales, las fórmulas de la proposición 9.19 constituyen la única historia matemática del modelo en ese intervalo. Ninguna de las correcciones exige renunciar a esa predicción; exige expresar exactamente de qué depende.

[]{#puente-hacia-las-fuerzas-concretas}

### Puente hacia las fuerzas concretas {#fispm-c09-puente-hacia-las-fuerzas-concretas}

El capítulo ha separado las leyes estructurales de Newton de las leyes particulares de interacción. Podemos identificar receptores, formular un estado completo, transformar marcos y justificar una evolución bajo hipótesis explícitas. El siguiente capítulo pondrá contenido físico en el lado de las fuerzas: gravedad uniforme, contacto, tensión, fricción, resistencia y resortes, junto con los diagramas de cuerpo libre. Esa transición requiere conservar las distinciones ya establecidas, porque una ecuación diferencial impecable puede comenzar con una lista de fuerzas equivocada.

[]{#fispm-c09-notas-bibliogruxe1ficas label="fispm-c09-notas-bibliogruxe1ficas"}

[^1]: R. Shankar, *Fundamentals of Physics I: Mechanics, Relativity, and Thermodynamics*, Expanded Edition, Yale University Press, 2019, cap. 3, §3.1, pp. 36--38; D. Kleppner y R. Kolenkow, *An Introduction to Mechanics*, copia Cambridge University Press, 2010, cap. 2, §2.2, pp. 55--56. Control de la distinción entre definición de marco inercial y afirmación física de su existencia. Redacción y ejercicios propios.

[^2]: Shankar, cap. 3, §3.2, pp. 38--41; Kleppner--Kolenkow, cap. 2, §2.2, pp. 56--58. Comparación de aceleraciones bajo intervención reproducible, masa inercial y consistencia de calibraciones. No se adopta la descripción histórica de patrones de masa como definición SI vigente.

[^3]: Kleppner--Kolenkow, cap. 2, §2.2, pp. 58--59. Fuerza, interacción y superposición vectorial; se distingue la definición de suma de su adecuación física.

[^4]: Shankar, cap. 3, §3.3, pp. 41--45; Kleppner--Kolenkow, cap. 2, §2.2, pp. 58--59. Diferencia entre segunda ley y ley particular de fuerza. Los ejemplos aquí usados no reproducen los problemas de esos libros.

[^5]: Shankar, cap. 3, §3.4, pp. 45--47; Kleppner--Kolenkow, cap. 2, §2.2, pp. 59--60. Parejas de fuerzas sobre cuerpos distintos. La redacción delimita el modelo de interacción instantánea por pares y no atribuye a la tercera ley débil la condición de fuerza central.

[^6]: M. Spivak, *Physics for Mathematicians: Mechanics I*, Publish or Perish, 2010, cap. 4, problema 12, pp. 164--165. Control de la desigualdad de Gronwall y comparación entre ecuaciones. Proposición 9.10 y proposición 9.17 desarrollan aquí el argumento con dominio común, normalización y datos iniciales distintos; no se reproduce literalmente el problema. La prueba constructiva de existencia local proposición 9.11 se incluye completa y no se atribuye a ese pasaje.

[^7]: Spivak, cap. 1, «The first law» y comienzo de «The second law», pp. 10--13; D. Morin, *Introduction to Classical Mechanics: With Problems and Solutions*, Cambridge University Press, 2008, cap. 3, §3.1, pp. 51--53. Control del papel del marco inercial y de la masa constante. Las fórmulas de transformación de las proposiciones 9.13--9.14 se derivan en el texto a partir de la cinemática del capítulo 8; no se atribuyen a una página no consultada.

[^8]: M. Spivak, *Physics for Mathematicians: Mechanics I*, Publish or Perish, 2010, cap. 4, problema 12, pp. 164--165. Control de la desigualdad de Gronwall y comparación entre ecuaciones. Proposición 9.10 y proposición 9.17 desarrollan aquí el argumento con dominio común, normalización y datos iniciales distintos; no se reproduce literalmente el problema. La prueba constructiva de existencia local proposición 9.11 se incluye completa y no se atribuye a ese pasaje.

[^9]: Morin, cap. 3, §3.3, pp. 60--62. Control de la formulación $mx''=F(t,x,v)$ y de la necesidad de ambos datos iniciales. La obstrucción de identificación de la proposición 9.18 y el ejercicio de diferenciación de errores ejercicio 9.27 se demuestran aquí; no se presentan como resultados citados de Morin.

[^10]: Morin, cap. 3, §3.3, pp. 62--64. Contraste del procedimiento de integración de modelos dependientes de velocidad. Proposición 9.19 usa una clase vectorial afín con contribución temporal continua y velocidad del entorno; sus fórmulas y la prueba de unicidad se desarrollan en el capítulo. No se adopta ninguna cifra empírica de validez de resistencia para el modelo formal aquí declarado.
