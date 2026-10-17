---
title: "Teorías físicas: fenómenos, modelos y leyes"
subtitle: "Física para matemáticos · Tomo I · Capítulo 1"
author: "A. Peña"
description: "Capítulo 1 del Tomo I de Física para matemáticos, con ejercicios y soluciones desarrolladas."
content-id: MA-BCH-0009
source-id: FISPM-T1-C01
editorial-id: FPM-I-01
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
date-modified: 2026-10-17
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: []
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

[Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [Capítulo 2](fisica-para-matematicos-capitulo-2-magnitudes-unidades-y-analisis-dimensional.md)

[]{#fispm-c01-teoruxedas-fuxedsicas-fenuxf3menos-modelos-y-leyes}

[]{#una-pregunta-física-no-es-todavía-una-ecuación}

[]{#fispm-t1-c01-s01}

[]{#fpm-i-01-s01}

## 1.1. Una pregunta física no es todavía una ecuación {#fispm-c01-una-pregunta-fuxedsica-no-es-todavuxeda-una-ecuaciuxf3n}

[]{#el-primer-problema}

### 1.1.1. El primer problema {#fispm-c01-el-primer-problema}

Supongamos que frente a nosotros cuelga una pequeña esfera metálica de un hilo. La apartamos de la vertical y la soltamos. La esfera va hacia un lado, regresa, atraviesa la posición central, sube por el otro lado, vuelve otra vez y continúa oscilando.

[]{#fig:I-01-R01}

![**Figura 1.1.** Una curva de posición contiene una historia cinemática. La tangente expresa velocidad; para explicar por qué cambia hacen falta interacciones y un modelo dinámico. El ejemplo usa $x=t^2/4{,}5$ en unidades normalizadas. Véase §[1.1](#fispm-c01-una-pregunta-fuxedsica-no-es-todavuxeda-una-ecuaciuxf3n).](/assets/books/fispm/v04/I-01-R01.svg "fig:"){.fpm-v04-figure fig-alt="Historia, estado y pregunta física" width="340px" fig-cap=""}

La pregunta parece inmediata:

> **¿Cómo se mueve el péndulo?**

Para quien ya ha estudiado algo de física, la tentación es casi automática: buscar una fórmula conocida. Quizá recuerde una ecuación para el péndulo, una expresión para su período o una aproximación válida cuando el ángulo es pequeño. Pero en este libro queremos detenernos **antes** de ese paso.

La pregunta «¿cómo se mueve el péndulo?» todavía no es una pregunta matemática bien determinada. Ni siquiera es aún una pregunta física suficientemente precisa.

¿Qué llamamos *el péndulo*?

¿La esfera? ¿La esfera y el hilo? ¿Incluimos el soporte? ¿Incluimos la Tierra, cuya atracción influye en el movimiento? ¿Incluimos el aire, que frena lentamente la oscilación? ¿Incluimos la rotación terrestre? ¿La elasticidad del hilo? ¿La temperatura, que puede cambiar mínimamente sus dimensiones? ¿El aparato con que medimos? ¿La persona que lo soltó?

Y, aun si acordamos qué sistema estudiaremos, queda otra cuestión: ¿qué significa exactamente «cómo se mueve»?

Podríamos querer conocer:

- cuánto tarda en ir y volver;

- la posición de la esfera en distintos instantes;

- la amplitud de cada oscilación;

- cuánto disminuye esa amplitud con el tiempo;

- cómo cambia el comportamiento si modificamos la longitud del hilo;

- si dos péndulos aparentemente iguales se comportan de manera indistinguible;

- cuánto cambia el movimiento si lo llevamos a otro lugar de la Tierra;

- qué aspectos del movimiento permanecen iguales aunque cambiemos el tamaño del aparato.

Cada una de estas preguntas selecciona aspectos distintos del mismo objeto físico.

Este será nuestro punto de partida:

**Principio 1.1 --- La modelización comienza antes de la primera fórmula** Antes de escribir una ecuación física ya hemos tomado decisiones acerca de qué sistema consideramos, qué pregunta formulamos, qué propiedades describiremos y qué efectos trataremos como relevantes o irrelevantes.

No se trata de una precaución filosófica externa a la física. Es una parte del trabajo físico mismo.

### 1.1.2. El objeto real contiene más física que nuestro primer modelo {#fispm-c01-el-objeto-real-contiene-muxe1s-fuxedsica-que-nuestro-primer-modelo}

Observemos con mayor cuidado el péndulo que tenemos delante. La esfera no es un punto: posee radio, densidad, rugosidad y distribución de masa. El hilo tampoco es una línea geométrica: tiene masa, grosor, elasticidad y puede torcerse. El punto de suspensión puede ceder o vibrar. El aire ejerce fuerzas sobre el conjunto. La Tierra gira. El campo gravitatorio no es perfectamente uniforme. El laboratorio vibra. La esfera intercambia calor con el ambiente. El dispositivo utilizado para medir el tiempo tiene resolución finita.

Nada de eso es imaginario. Todos son aspectos físicos reales.

Sin embargo, si intentáramos incluir desde el comienzo todos los detalles que pudieran tener alguna influencia, probablemente no avanzaríamos. Un modelo físico no pretende copiar el mundo en miniatura. Su tarea es más selectiva:

$$\boxed{\text{un modelo conserva ciertos rasgos del sistema y omite otros}}$$ de acuerdo con una pregunta.

La palabra importante es **de acuerdo con una pregunta**. La masa del hilo puede ser irrelevante si solo queremos una primera descripción aproximada de la oscilación de una esfera pesada sostenida por un hilo muy ligero. Pero esa misma masa puede ser decisiva si estudiamos vibraciones del hilo. La deformación del soporte puede ser despreciable en una experiencia de aula y esencial en un experimento de precisión. La resistencia del aire puede no importar durante dos oscilaciones y volverse evidente después de cientos.

No existen, por tanto, detalles «irrelevantes en sí mismos». Hay detalles irrelevantes **para una pregunta y dentro de una precisión determinada**.

### 1.1.3. Una escalera de representaciones {#fispm-c01-una-escalera-de-representaciones}

Podemos ordenar varias descripciones posibles del mismo dispositivo.

[]{#nivel-a-el-péndulo-real}

#### 1.1.3.1. Nivel A --- El péndulo real {#fispm-c01-nivel-a-el-puxe9ndulo-real}

Tenemos un cuerpo extendido suspendido de un hilo real, dentro de aire, unido a un soporte real, en un laboratorio situado sobre una Tierra real. Esta descripción es físicamente rica, pero todavía demasiado abierta para calcular o predecir algo concreto.

[]{#nivel-b-selección-del-sistema}

#### 1.1.3.2. Nivel B --- Selección del sistema {#fispm-c01-nivel-b-selecciuxf3n-del-sistema}

Decidimos estudiar principalmente:

- el cuerpo suspendido;

- el hilo;

- la interacción con la Tierra.

Tratamos el resto como **entorno**.

Todavía no hemos convertido el sistema en un objeto matemático. Solo hemos trazado una primera frontera conceptual.

[]{#nivel-c-idealización-geométrica}

#### 1.1.3.3. Nivel C --- Idealización geométrica {#fispm-c01-nivel-c-idealizaciuxf3n-geomuxe9trica}

Representamos la esfera por un punto y el hilo por un segmento de longitud fija.

Aquí ya hemos hecho dos operaciones fuertes:

1.  ignoramos el tamaño y la forma del cuerpo;

2.  ignoramos las deformaciones del hilo.

El objeto matemático que aparece no existe literalmente en el laboratorio. No hay masas puntuales ni segmentos materiales de grosor cero. Son **idealizaciones**.

[]{#nivel-d-omisión-de-disipación}

#### 1.1.3.4. Nivel D --- Omisión de disipación {#fispm-c01-nivel-d-omisiuxf3n-de-disipaciuxf3n}

Decidimos ignorar, en una primera descripción, la pérdida de energía asociada al aire y a la fricción del soporte.

No estamos diciendo que esas pérdidas sean cero en el mundo. Estamos diciendo:

> «Para la pregunta actual, construiremos un modelo en el que no aparezcan.»

[]{#nivel-e-modelo-ulterior-de-pequeñas-oscilaciones}

#### 1.1.3.5. Nivel E --- Modelo ulterior de pequeñas oscilaciones {#fispm-c01-nivel-e-modelo-ulterior-de-pequeuxf1as-oscilaciones}

En un capítulo posterior podremos hacer una aproximación adicional válida bajo condiciones específicas para simplificar todavía más el modelo. Pero no debemos saltar a ella ahora. Primero tendremos que aprender qué significa justificar una aproximación y cómo se especifica su régimen de validez.

La secuencia conceptual es, por tanto,

$$\begin{gathered} \text{objeto real} \longrightarrow \text{sistema seleccionado}\\[2pt]\Downarrow\\[2pt]\text{idealización} \longrightarrow \text{modelo}\\[2pt]\Downarrow\\[2pt]\text{aproximaciones adicionales}. \end{gathered}$$ No todos estos pasos son matemáticos. Algunos son decisiones físicas acerca de qué aspectos del mundo vamos a representar.

### 1.1.4. Primera distinción fundamental: sistema real y objeto matemático {#fispm-c01-primera-distinciuxf3n-fundamental-sistema-real-y-objeto-matemuxe1tico}

Consideremos una esfera de acero que cuelga de un hilo. La esfera que tocamos pertenece al mundo físico. Podemos pesarla, calentarla, rayarla o reemplazarla.

Un punto geométrico no tiene esas propiedades. Carece de volumen y de estructura interna. Sin embargo, para ciertas preguntas podemos representar la esfera mediante un punto cuya posición simboliza la posición del cuerpo.

Es importante no confundir ambas cosas.

**Definición operativa 1.1 --- Sistema físico (primera formulación)** Llamaremos **sistema físico** a la porción o colección de aspectos del mundo que elegimos como objeto principal de estudio para una pregunta determinada.

La expresión «elegimos» es deliberada. La frontera de un sistema no siempre viene impuesta por la naturaleza.

**Definición operativa 1.2 --- Representación matemática** Una **representación matemática** asigna a aspectos seleccionados de un sistema físico objetos matemáticos ---números, puntos, vectores, funciones, espacios, operadores, probabilidades u otras estructuras--- junto con una interpretación que indica qué significan físicamente.

La representación no es simplemente una traducción de palabras a símbolos. Implica una correspondencia. Si escribimos un símbolo $x$, todavía no hemos hecho física. Necesitamos saber **qué representa $x$** y mediante qué procedimiento podría relacionarse con una observación.

### 1.1.5. El problema del mapa {#fispm-c01-el-problema-del-mapa}

Hay una manera útil de pensar la relación entre realidad y modelo. Un mapa de una ciudad no reproduce la ciudad. No contiene los mismos edificios, personas, sonidos, temperaturas ni materiales. Contiene líneas, nombres, símbolos y escalas.

Un buen mapa omite casi todo. Y precisamente por omitir casi todo puede ser útil. Un plano del metro y un mapa topográfico del mismo territorio pueden ser excelentes aunque sean muy diferentes. El primero representa conexiones entre estaciones y simplifica distancias y direcciones; el segundo conserva información geométrica que el plano del metro descarta.

Preguntar cuál de los dos es «el mapa verdadero» sería formular mal la cuestión. Debemos preguntar:

> **¿verdadero o adecuado para qué tarea?**

Algo semejante ocurre con los modelos físicos.

La Tierra puede ser representada como:

- un plano, para ciertos problemas locales;

- una esfera, para una primera descripción global;

- un geoide, para geodesia;

- un cuerpo rígido en rotación, para ciertos problemas dinámicos;

- una masa puntual, para ciertas cuestiones orbitales;

- una distribución continua de materia, para estudiar su campo interior.

Ninguna de esas representaciones agota lo que la Tierra es. El modelo adecuado depende de la pregunta, de la escala y de la precisión exigida.

### 1.1.6. ¿Podemos incluir todo? {#fispm-c01-podemos-incluir-todo}

Podría parecer que la solución más rigurosa consiste simplemente en introducir un modelo cada vez más detallado hasta incluir «todo lo importante». Pero esta idea contiene varios problemas.

[]{#no-sabemos-de-antemano-qué-es-todo-lo-importante}

### 1.1.7. No sabemos de antemano qué es «todo lo importante» {#fispm-c01-no-sabemos-de-antemano-quuxe9-es-todo-lo-importante}

Precisamente uno de los objetivos de un experimento puede ser descubrir que un efecto considerado insignificante no lo era.

[]{#un-modelo-más-complejo-no-es-automáticamente-mejor}

### 1.1.8. Un modelo más complejo no es automáticamente mejor {#fispm-c01-un-modelo-muxe1s-complejo-no-es-automuxe1ticamente-mejor}

Añadir parámetros y mecanismos puede permitir describir más detalles, pero también puede:

- dificultar la interpretación;

- introducir cantidades que no sabemos medir;

- ocultar regularidades simples;

- volver inestable una inferencia;

- hacer imposible distinguir qué mecanismo produce qué efecto.

[]{#la-pregunta-puede-no-necesitar-esa-complejidad}

### 1.1.9. La pregunta puede no necesitar esa complejidad {#fispm-c01-la-pregunta-puede-no-necesitar-esa-complejidad}

Si queremos saber aproximadamente cuánto tarda un péndulo en completar una oscilación, modelar el intercambio térmico de la esfera con el aire puede aportar una precisión completamente irrelevante.

[]{#un-ejemplo-extremo-la-esfera-perfectamente-rígida}

### 1.1.10. Un ejemplo extremo: la esfera perfectamente rígida {#fispm-c01-un-ejemplo-extremo-la-esfera-perfectamente-ruxedgida}

Imaginemos que en un modelo llamamos «rígida» a una esfera.

Dentro del modelo, «rígida» puede significar que las distancias entre sus puntos no cambian. Esta hipótesis puede simplificar enormemente el problema. Pero ninguna esfera material es perfectamente rígida. Todos los cuerpos reales se deforman en alguna medida.

¿Significa esto que el modelo de cuerpo rígido es falso y debe abandonarse?

No.

La pregunta correcta es:

> **¿Son las deformaciones suficientemente pequeñas para que ignorarlas no cambie las conclusiones que nos interesan?**

La física trabaja continuamente con objetos que no existen literalmente:

- partículas puntuales;

- cuerpos perfectamente rígidos;

- hilos sin masa;

- superficies sin rozamiento;

- gases ideales;

- campos uniformes;

- lentes delgadas;

- medios continuos.

Su utilidad no depende de que existan exactamente, sino de que exista un **régimen** en el cual proporcionen una representación adecuada para determinadas preguntas. Más adelante aprenderemos a expresar cuantitativamente algunos de esos regímenes.

### 1.1.11. Preguntas diferentes, modelos diferentes {#fispm-c01-preguntas-diferentes-modelos-diferentes}

Volvamos al péndulo.

[]{#pregunta-1}

#### 1.1.11.1. Pregunta 1 {#fispm-c01-pregunta-1}

**¿El cuerpo vuelve aproximadamente al mismo lugar después de ir hacia un lado y hacia el otro?**

Tal vez baste una descripción geométrica muy elemental.

[]{#pregunta-2}

#### 1.1.11.2. Pregunta 2 {#fispm-c01-pregunta-2}

**¿Cuánto tarda en completar una oscilación?**

Necesitaremos representar el tiempo y ciertas propiedades del sistema.

[]{#pregunta-3}

#### 1.1.11.3. Pregunta 3 {#fispm-c01-pregunta-3}

**¿Disminuye la amplitud?**

Ya no podemos ignorar indefinidamente los mecanismos de disipación.

[]{#pregunta-4}

#### 1.1.11.4. Pregunta 4 {#fispm-c01-pregunta-4}

**¿El plano de oscilación cambia lentamente durante muchas horas?**

La rotación terrestre, irrelevante para una pregunta elemental, puede volverse central.

[]{#pregunta-5}

#### 1.1.11.5. Pregunta 5 {#fispm-c01-pregunta-5}

**¿Cómo cambia el comportamiento si el soporte se mueve?**

La frontera misma del sistema puede requerir una reformulación. La lección no es que «todo sea relativo» en un sentido impreciso. Es exactamente lo contrario: debemos hacer explícita la dependencia del modelo respecto de la pregunta.

**Principio 1.2 --- Adecuación relativa a una pregunta** Un modelo físico debe evaluarse en relación con las preguntas que pretende responder, las escalas relevantes y la precisión exigida.

### 1.1.12. Lo que una ecuación no nos dice por sí sola {#fispm-c01-lo-que-una-ecuaciuxf3n-no-nos-dice-por-suxed-sola}

Supongamos que más adelante encontramos una expresión matemática

$$F(a,b,c)=0.$$ La ecuación, considerada únicamente como objeto matemático, no nos informa:

- qué representan $a,b,c$;

- cómo se miden;

- qué unidades poseen;

- si $F=0$ es una definición, una ley empírica o una consecuencia;

- qué hipótesis físicas se utilizaron;

- si la relación es exacta dentro del modelo o aproximada;

- para qué sistemas se propone;

- bajo qué condiciones deja de ser adecuada.

Por eso, durante este libro, una ecuación física nunca será tratada como una fórmula autosuficiente.

Preguntaremos siempre:

1.  **¿Qué objetos físicos están representados?**

2.  **¿Qué significan los símbolos?**

3.  **¿Cuál es el estatus de la relación?**

4.  **¿Qué hipótesis la acompañan?**

5.  **¿Qué observación permitiría ponerla a prueba?**

6.  **¿Cuál es su dominio de validez?**

Más adelante introduciremos una notación editorial para distinguir definiciones, leyes, postulados, hipótesis de modelo, aproximaciones, condiciones y consecuencias matemáticas.

### 1.1.13. Un entrenamiento especialmente importante para matemáticos {#fispm-c01-un-entrenamiento-especialmente-importante-para-matemuxe1ticos}

Quien estudia matemáticas aprende, con razón, a exigir definiciones claras, hipótesis explícitas y demostraciones correctas. En una proposición matemática, una vez fijados los objetos y las hipótesis, la tarea central es determinar qué se deduce lógicamente de ellos.

En física aparece una tarea adicional:

> **decidir qué objetos e hipótesis son apropiados para representar un fenómeno.**

Esta tarea no es una demostración. No se demuestra, a partir de axiomas puramente matemáticos, que un cuerpo pueda tratarse como punto material, que cierto rozamiento sea despreciable o que un modelo continuo sea adecuado. Estas afirmaciones requieren argumentos físicos: comparación de escalas, observaciones, experimentos, simetrías, experiencias anteriores y análisis de sensibilidad.

La secuencia completa posee entonces dos tipos de razonamiento:

$$\text{mundo físico} \longrightarrow \boxed{\text{elección del modelo}} \longrightarrow \text{matemática} \longrightarrow \boxed{\text{interpretación y contraste}}.$$ Los recuadros indican los pasos que no pueden reemplazarse simplemente por manipulación formal.

Este será uno de los hábitos centrales de *Física para matemáticos*.

### 1.1.14. Ejemplo desarrollado 1 --- ¿Qué debemos ignorar? {#fispm-c01-ejemplo-desarrollado-1-quuxe9-debemos-ignorar}

Consideremos este problema:

> Una pequeña esfera cuelga de un hilo de un metro. Se la aparta ligeramente y se la suelta. Queremos comparar el tiempo de una oscilación hoy y mañana.

Antes de calcular nada, clasifiquemos posibles aspectos del sistema.

  Aspecto                ¿Podría influir físicamente?                     ¿Lo incluimos de inmediato?                     Motivo
  ---------------------- ------------------------------------------------ ----------------------------------------------- ---------------------------------------------------
  longitud del hilo      sí                                               sí                                              define geométricamente el dispositivo
  masa de la esfera      sí, en general                                   registrar                                       todavía no sabemos qué dependerá de ella
  tamaño de la esfera    sí                                               quizá                                           puede afectar resistencia del aire
  masa del hilo          sí                                               quizá no                                        puede ser pequeña frente a la esfera
  resistencia del aire   sí                                               quizá no al inicio                              el efecto puede ser pequeño en pocas oscilaciones
  temperatura            sí                                               registrar si buscamos alta precisión            puede cambiar dimensiones
  rotación terrestre     sí                                               probablemente no para esta pregunta elemental   efecto acumulativo pequeño en pocos ciclos
  color de la esfera     puede correlacionarse con material/temperatura   no por sí mismo                                 no hay aún mecanismo relevante propuesto

La columna importante es la segunda: **no debemos confundir «lo ignoro en este modelo» con «no puede tener ningún efecto».**

[]{#paso-1-formulamos-la-pregunta}

#### 1.1.14.1. Paso 1 --- Formulamos la pregunta {#fispm-c01-paso-1-formulamos-la-pregunta}

Queremos comparar tiempos de oscilación.

[]{#paso-2-elegimos-variables-observables}

#### 1.1.14.2. Paso 2 --- Elegimos variables observables {#fispm-c01-paso-2-elegimos-variables-observables}

Necesitamos, como mínimo, un procedimiento para identificar comienzo y final de una oscilación y un procedimiento para medir tiempo.

[]{#paso-3-elegimos-una-primera-representación}

#### 1.1.14.3. Paso 3 --- Elegimos una primera representación {#fispm-c01-paso-3-elegimos-una-primera-representaciuxf3n}

Tratamos provisionalmente el cuerpo como concentrado en una posición y el hilo como de longitud fija.

[]{#paso-4-registramos-omisiones}

#### 1.1.14.4. Paso 4 --- Registramos omisiones {#fispm-c01-paso-4-registramos-omisiones}

Aire, deformación del soporte, masa del hilo y otros efectos quedan fuera de la primera descripción.

[]{#paso-5-dejamos-abierta-la-revisión}

#### 1.1.14.5. Paso 5 --- Dejamos abierta la revisión {#fispm-c01-paso-5-dejamos-abierta-la-revisiuxf3n}

Si las observaciones no concuerdan con la precisión buscada, las omisiones se convierten en candidatas a revisión.

Este es el patrón que repetiremos muchas veces:

$$\boxed{ \text{pregunta} \to \text{selección} \to \text{modelo} \to \text{predicción} \to \text{contraste} \to \text{revisión} }$$

### 1.1.15. Ejemplo desarrollado 2 --- La Tierra no tiene un único modelo {#fispm-c01-ejemplo-desarrollado-2-la-tierra-no-tiene-un-uxfanico-modelo}

La afirmación «modelaremos la Tierra» está incompleta.

[]{#caso-a-una-cancha-de-fútbol}

#### 1.1.15.1. Caso A --- Una cancha de fútbol {#fispm-c01-caso-a-una-cancha-de-fuxfatbol}

Si queremos describir posiciones sobre una cancha, podemos usar un plano. La curvatura terrestre no tiene relevancia práctica para esa tarea.

[]{#caso-b-una-ruta-aérea-transcontinental}

#### 1.1.15.2. Caso B --- Una ruta aérea transcontinental {#fispm-c01-caso-b-una-ruta-auxe9rea-transcontinental}

Ahora la geometría global importa. Un modelo plano puede distorsionar distancias y trayectorias.

[]{#caso-c-el-movimiento-de-un-satélite-lejano}

#### 1.1.15.3. Caso C --- El movimiento de un satélite lejano {#fispm-c01-caso-c-el-movimiento-de-un-satuxe9lite-lejano}

Para ciertos cálculos iniciales, la Tierra puede representarse aproximadamente por una masa concentrada en un punto.

[]{#caso-d-distribución-de-gravedad-en-la-superficie}

#### 1.1.15.4. Caso D --- Distribución de gravedad en la superficie {#fispm-c01-caso-d-distribuciuxf3n-de-gravedad-en-la-superficie}

La forma real, la rotación y la distribución de masa pueden importar.

La secuencia enseña algo general:

$$\boxed{ \text{mismo objeto físico} \not\Rightarrow \text{mismo modelo para toda pregunta} }$$

### 1.1.16. Primer protocolo de lectura {#fispm-c01-primer-protocolo-de-lectura}

Desde este momento, ante cualquier problema físico, comenzaremos con cinco preguntas.

**Protocolo FPM de premodelización --- versión inicial** 1. ¿Cuál es la pregunta física concreta? 2. ¿Qué tomaremos como sistema? 3. ¿Qué propiedades necesitamos representar? 4. ¿Qué efectos estamos omitiendo o idealizando? 5. ¿Qué observación permitiría decidir si el modelo sirve para la pregunta?

Todavía faltan elementos ---unidades, escalas, parámetros, condiciones y dominio de validez cuantitativo--- que añadiremos en capítulos posteriores.

### 1.1.17. Ejercicios de §1 {#fispm-c01-ejercicios-de-1}

[]{#fispm-t1-c01-e0001}

**Ejercicio 1.1 --- Un vaso de agua.**

Queremos estudiar un vaso con agua. Propón **tres preguntas físicas distintas** para las cuales convenga utilizar modelos diferentes. Para cada una, indica al menos dos aspectos que incluirías y dos que probablemente omitirías en una primera aproximación.

**Solución.**

Una posible respuesta es:

**Pregunta A:** ¿cuánta agua contiene el vaso?

- incluir: volumen interior, nivel del agua;

- omitir inicialmente: viscosidad, rotación terrestre.

**Pregunta B:** ¿cómo oscila la superficie si movemos el vaso lateralmente?

- incluir: geometría del recipiente, movimiento del agua, gravedad;

- omitir inicialmente: evaporación, composición isotópica del agua.

**Pregunta C:** ¿cuánto tarda el agua caliente en enfriarse?

- incluir: temperatura, intercambio térmico con el ambiente, material del vaso;

- omitir inicialmente: movimiento de la Tierra alrededor del Sol, pequeñas irregularidades geométricas que no afecten apreciablemente al intercambio térmico.

[]{#fispm-t1-c01-e0002}

La enseñanza no está en que estas elecciones sean únicas. Deben justificarse respecto de cada pregunta. **Ejercicio 1.2 --- Modelo más detallado.**

Un estudiante afirma:

> «Entre dos modelos, siempre es físicamente mejor el que incluye más detalles.»

Explica por qué la afirmación es falsa. Da un ejemplo.

**Solución.**

Más detalle no garantiza mayor adecuación para una pregunta concreta. Un modelo puede introducir parámetros desconocidos, ocultar la estructura relevante o resolver con gran precisión efectos que son insignificantes frente a la precisión requerida. Ejemplo: para estimar la distancia recorrida por una persona al caminar cien metros por una calle, un modelo que incorpore la curvatura del espacio-tiempo terrestre es muchísimo más detallado que un modelo euclídeo local, pero esa complejidad no mejora de manera útil la respuesta.

La comparación correcta no es «más detalles frente a menos detalles», sino:

[]{#fispm-t1-c01-e0003}

$$\text{adecuación para la pregunta y precisión buscada}.$$ **Ejercicio 1.3 --- ¿Qué significa «sin rozamiento»?.**

En un problema se dice que un bloque se mueve sobre una superficie «sin rozamiento».

¿Es esto una afirmación acerca de una superficie real o una hipótesis de modelo? Explica qué información adicional necesitaríamos para decidir si esa idealización es adecuada.

**Solución.**

«Sin rozamiento» funciona aquí como una **hipótesis de modelo**. No implica que exista una superficie material con rozamiento exactamente cero.

Para evaluar su adecuación necesitamos saber, entre otras cosas:

- qué magnitud queremos predecir;

- durante cuánto tiempo o distancia;

- qué precisión exigimos;

- qué tan pequeño es el efecto del rozamiento en comparación con los efectos conservados en el modelo.

[]{#fispm-t1-c01-e0004}

La idealización puede ser excelente para una pregunta y mala para otra. **Ejercicio 1.4 --- Una fotografía no es una trayectoria.**

Se toma una única fotografía de una pelota en el aire.

¿Basta esa imagen para responder «cómo se mueve la pelota»? Enumera información que falta.

**Solución.**

No. Una fotografía registra, como máximo, cierta información espacial en un instante y bajo una proyección particular.

Faltan, por ejemplo:

- una escala espacial;

- el instante o una referencia temporal;

- información sobre posiciones en otros instantes;

- información sobre profundidad si la imagen es bidimensional;

- identificación del sistema de referencia;

- procedimiento que conecte píxeles con posiciones físicas;

- datos sobre el entorno y el mecanismo que produjo el movimiento.

Incluso el significado de «posición» requiere una regla de reconstrucción a partir de la imagen.

### 1.1.18. Cierre de la sección {#fispm-c01-cierre-de-la-secciuxf3n}

Todavía no hemos escrito la ecuación de un péndulo.

Eso no significa que aún no hayamos hecho física.

Ya hemos aprendido que antes de una ecuación debemos:

- formular una pregunta;

- seleccionar un sistema;

- elegir qué propiedades representar;

- idealizar;

- registrar omisiones;

- decidir qué observaciones serían relevantes.

En la sección siguiente examinaremos precisamente el último punto.

¿Qué cuenta como observación física?

Ver que «el péndulo se mueve» no es lo mismo que producir un dato que pueda compararse con una predicción. Pasaremos, por tanto, de

$$\boxed{\text{¿qué queremos representar?}}$$ a

$$\boxed{\text{¿cómo se conecta esa representación con una observación?}}$$

[]{#fenómeno-observación-y-experimento}

[]{#fispm-t1-c01-s02}

[]{#fpm-i-01-s02}

## 1.2. Fenómeno, observación y experimento {#fispm-c01-fenuxf3meno-observaciuxf3n-y-experimento}

[]{#ver-no-es-todavía-medir}

### 1.2.1. Ver no es todavía medir {#fispm-c01-ver-no-es-todavuxeda-medir}

Volvamos al péndulo.

Lo apartamos y lo soltamos. Podemos decir:

> «Oscila.»

Esta frase registra algo real. Pero si queremos confrontar un modelo con el mundo necesitamos avanzar.

Podríamos preguntar:

- ¿cuánto dura una oscilación?;

- ¿hasta qué altura llega?;

- ¿la amplitud disminuye?;

- ¿dos oscilaciones sucesivas duran lo mismo?;

- ¿cambia el resultado si usamos otra esfera?;

- ¿cambia si repetimos el experimento mañana?

Responder estas preguntas exige algo más que mirar.

Debemos especificar **qué observaremos y cómo**.

Esta es la segunda idea rectora del capítulo:

**Principio 1.3 --- Una observación física requiere una regla de conexión** Para comparar una teoría o un modelo con el mundo necesitamos un procedimiento que conecte algún objeto de la representación matemática con un resultado observable.

No basta con que aparezca un número en una ecuación. Debemos saber qué procedimiento físico produciría el número correspondiente.

### 1.2.2. Fenómeno {#fispm-c01-fenuxf3meno}

Usaremos la palabra **fenómeno** de manera amplia pero operativa.

**Definición operativa 1.3 --- Fenómeno** Un **fenómeno físico** es un proceso, comportamiento o regularidad del mundo físico que seleccionamos para describir, comparar, predecir o explicar.

Ejemplos:

- la oscilación de un péndulo;

- la caída de un cuerpo;

- la expansión de un gas al calentarse;

- la desviación de la luz al atravesar ciertos medios;

- una corriente eléctrica;

- la interferencia de ondas;

- la desintegración de una partícula.

Un fenómeno no tiene por qué ser un «objeto». La oscilación no es la esfera; es un comportamiento del sistema.

Tampoco es necesario que sea un acontecimiento único. Podemos estudiar regularidades:

> cuerpos soltados de manera semejante muestran ciertos patrones de caída;

o transiciones:

> cierta sustancia cambia de fase bajo determinadas condiciones.

La selección del fenómeno ya contiene una pregunta implícita: de todo lo que ocurre, decidimos prestar atención a cierta estructura.

### 1.2.3. Observación {#fispm-c01-observaciuxf3n}

Consideremos dos afirmaciones:

1.  «La esfera pasó por el centro.»

2.  «La esfera cruzó la marca central cuando el reloj indicaba $12.4\ \mathrm{s}$.»

La segunda contiene una especificación mayor. Pero incluso ella deja preguntas:

- ¿qué marca se considera «el centro»?;

- ¿qué instante asociamos al cruce si la esfera tiene tamaño finito?;

- ¿qué reloj utilizamos?;

- ¿quién leyó el reloj?;

- ¿cómo se sincronizó el comienzo?;

- ¿qué resolución posee el aparato?

No resolveremos todavía todos estos problemas. El objetivo del capítulo 3 será precisamente desarrollar medición e incertidumbre. Por ahora necesitamos una definición de trabajo.

**Definición operativa 1.4 --- Observación** Una **observación física** es un registro obtenido mediante un procedimiento especificado que asigna al sistema una descripción, clasificación o valor susceptible de comparación.

La expresión **mediante un procedimiento especificado** es esencial. Una observación física no es únicamente una sensación privada. Debe existir alguna regla suficientemente clara para que podamos preguntar si dos procedimientos registran lo mismo o si producen resultados comparables.

### 1.2.4. Del fenómeno al dato {#fispm-c01-del-fenuxf3meno-al-dato}

Supongamos que queremos medir el tiempo de una oscilación.

Necesitamos definir al menos:

1.  **evento inicial**;

2.  **evento final**;

3.  **procedimiento temporal**.

Por ejemplo:

- inicio: primer cruce de una marca central en una dirección determinada;

- final: siguiente cruce de la misma marca en la misma dirección;

- tiempo: diferencia entre dos lecturas de un reloj.

Esta descripción ya convierte una pregunta vaga en una operación más precisa.

Podemos simbolizar las lecturas como

$$t_{\mathrm{i}},\qquad t_{\mathrm{f}},$$ y definir

$$T := t_{\mathrm{f}}-t_{\mathrm{i}}.$$ Aquí debemos leer cuidadosamente el estatus de cada relación.

$$[\mathrm{DEF}]\qquad T:=t_{\mathrm{f}}-t_{\mathrm{i}}.$$ Esta ecuación no es una ley de la naturaleza. Es una **definición** de la cantidad $T$ a partir de las lecturas especificadas.

Aún no hemos afirmado que $T$ sea constante, que dependa de la longitud o que obedezca alguna ley. Esto muestra por qué dos ecuaciones algebraicamente similares pueden tener papeles físicos muy distintos.

### 1.2.5. Observable y procedimiento {#fispm-c01-observable-y-procedimiento}

En física se habla con frecuencia de **observables**. La noción adquirirá significados técnicos diferentes en teorías posteriores, especialmente en mecánica cuántica. Aquí necesitamos solamente una versión inicial.

**Definición operativa 1.5 --- Observable** Un **observable**, en este nivel, es una propiedad del sistema que el modelo conecta con un procedimiento de observación o medición.

Ejemplos elementales pueden ser:

- una posición respecto de referencias definidas;

- un intervalo temporal;

- una masa determinada por un procedimiento de pesaje;

- una temperatura indicada por un instrumento calibrado;

- el número de eventos detectados en cierto intervalo.

La palabra «conecta» evita una simplificación importante.

No siempre «leemos directamente» una propiedad de la naturaleza. Muchas veces inferimos una cantidad mediante una cadena:

$$\text{sistema} \to \text{interacción con instrumento} \to \text{señal} \to \text{procesamiento} \to \text{valor registrado}.$$ Por ejemplo, una cámara digital no entrega «posición» en metros. Produce datos en una matriz de detectores. Para convertirlos en posiciones físicas necesitamos calibración, geometría y convenciones.

### 1.2.6. Microcaso: una pelota que cae {#fispm-c01-microcaso-una-pelota-que-cae}

Queremos estudiar la caída de una pelota.

Parece obvio qué observar: «la altura». Pero debemos construirla.

[]{#opción-a-marcas-sobre-una-pared}

#### 1.2.6.1. Opción A --- Marcas sobre una pared {#fispm-c01-opciuxf3n-a-marcas-sobre-una-pared}

Colocamos referencias de altura y registramos visualmente la posición.

[]{#opción-b-video}

#### 1.2.6.2. Opción B --- Video {#fispm-c01-opciuxf3n-b-video}

Filmamos la caída y relacionamos píxeles con una escala física.

[]{#opción-c-barreras-ópticas}

#### 1.2.6.3. Opción C --- Barreras ópticas {#fispm-c01-opciuxf3n-c-barreras-uxf3pticas}

Colocamos sensores a alturas determinadas y registramos los instantes de paso.

Cada método produce datos de forma diferente.

Esto tiene consecuencias:

- los procedimientos pueden tener resoluciones distintas;

- pueden perturbar el sistema de manera diferente;

- requieren distintas calibraciones;

- pueden definir de manera ligeramente distinta el evento «la pelota está a altura $h$».

La variable matemática «altura» no llega al experimento sin mediación.

### 1.2.7. ¿Qué observar en la caída? {#fispm-c01-quuxe9-observar-en-la-cauxedda}

Imaginemos ahora que soltamos dos hojas de papel, una extendida y otra arrugada.

Podemos registrar:

- tiempo de caída;

- orientación;

- forma;

- velocidad del aire;

- trayectoria lateral;

- rotación.

Si solo registramos el instante en que tocan el suelo, quizá concluyamos que una cae más rápido. Pero esa conclusión no nos dice por sí sola **por qué**.

Podrían importar:

- la resistencia del aire;

- la geometría;

- las corrientes;

- el procedimiento de liberación.

El experimento necesita entonces distinguir hipótesis.

Esto nos lleva a una idea más fuerte que la mera observación.

### 1.2.8. Experimento {#fispm-c01-experimento}

**Definición operativa 1.6 --- Experimento** Un **experimento** es una disposición o intervención controlada diseñada para producir observaciones que permitan estimar cantidades, comparar comportamientos o discriminar entre hipótesis.

La palabra «controlada» no significa que absolutamente todo esté bajo control.

Significa que intentamos:

- fijar ciertas condiciones;

- variar otras;

- registrar qué se hizo;

- establecer qué diferencias entre resultados pueden atribuirse razonablemente a los cambios introducidos.

Un experimento no es simplemente «hacer algo y mirar qué ocurre».

### 1.2.9. Ejemplo desarrollado 3 --- Diseñar una comparación {#fispm-c01-ejemplo-desarrollado-3-diseuxf1ar-una-comparaciuxf3n}

Pregunta:

> ¿Influye de manera apreciable la amplitud inicial en el tiempo de oscilación de nuestro péndulo?

No responderemos todavía con una fórmula. Diseñaremos el razonamiento experimental.

[]{#paso-1-identificar-lo-que-variaremos}

#### 1.2.9.1. Paso 1 --- Identificar lo que variaremos {#fispm-c01-paso-1-identificar-lo-que-variaremos}

Variamos la posición inicial del cuerpo.

[]{#paso-2-identificar-lo-que-intentaremos-mantener-fijo}

#### 1.2.9.2. Paso 2 --- Identificar lo que intentaremos mantener fijo {#fispm-c01-paso-2-identificar-lo-que-intentaremos-mantener-fijo}

- mismo péndulo;

- mismo punto de suspensión;

- misma definición de período;

- mismo procedimiento temporal;

- condiciones ambientales tan semejantes como sea razonable.

[]{#paso-3-definir-grupos-de-observaciones}

#### 1.2.9.3. Paso 3 --- Definir grupos de observaciones {#fispm-c01-paso-3-definir-grupos-de-observaciones}

Realizamos varias mediciones para distintas amplitudes iniciales.

[]{#paso-4-evitar-una-conclusión-prematura}

#### 1.2.9.4. Paso 4 --- Evitar una conclusión prematura {#fispm-c01-paso-4-evitar-una-conclusiuxf3n-prematura}

Si obtenemos valores diferentes, todavía debemos preguntar:

- ¿las diferencias son mayores que la variación propia del procedimiento?;

- ¿cambiamos inadvertidamente otra condición?;

- ¿el modo de soltar el péndulo introduce perturbaciones?;

- ¿el instrumento permite distinguir la diferencia?

Estas preguntas pertenecen a la estructura experimental, no a la solución matemática de una ecuación.

### 1.2.10. Observación y teoría no son mundos aislados {#fispm-c01-observaciuxf3n-y-teoruxeda-no-son-mundos-aislados}

Podría parecer que primero existen «datos puros» y después una teoría se limita a explicarlos. La situación real es más sutil.

Para producir un dato ya utilizamos conceptos:

- elegimos qué cuenta como evento;

- decidimos qué magnitud registrar;

- elegimos un instrumento;

- aplicamos una calibración;

- organizamos señales según un procedimiento.

Esto no significa que los datos sean arbitrarios o que una teoría pueda imponer cualquier resultado. Significa que la conexión entre mundo y representación posee estructura.

En este libro la indicaremos con la etiqueta:

$$[\mathrm{OBS}]$$ para relaciones que especifican cómo una cantidad del modelo se conecta con un procedimiento de observación.

Por ejemplo:

$$[\mathrm{OBS}]$$ «La coordenada registrada de la esfera se obtiene convirtiendo la posición de su centro en la imagen mediante una calibración espacial previamente fijada.»

No es todavía una ecuación universal; es una **regla de conexión** entre aparato y modelo.

### 1.2.11. Repetición: ¿por qué medir más de una vez? {#fispm-c01-repeticiuxf3n-por-quuxe9-medir-muxe1s-de-una-vez}

Si repetimos un procedimiento aparentemente idéntico, rara vez obtenemos resultados numéricamente idénticos con precisión ilimitada.

Puede haber diferencias debidas a:

- resolución del instrumento;

- variaciones del ambiente;

- pequeñas diferencias en las condiciones iniciales;

- ruido;

- fluctuaciones físicas;

- intervención humana;

- cambios del propio sistema.

Todavía no clasificaremos formalmente estas variaciones. Ese trabajo corresponde al capítulo 3.

Pero sí fijaremos una norma:

**Principio 1.4 --- Una observación aislada no caracteriza por sí sola la estabilidad de un procedimiento** Cuando la pregunta exige comparar o estimar una magnitud, debemos considerar si el resultado persiste al repetir el procedimiento bajo condiciones declaradas.

### 1.2.12. Repetibilidad y reproducibilidad: primera aproximación {#fispm-c01-repetibilidad-y-reproducibilidad-primera-aproximaciuxf3n}

Usaremos dos palabras de manera preliminar.

[]{#repetibilidad}

#### 1.2.12.1. Repetibilidad {#fispm-c01-repetibilidad}

Preguntamos si un procedimiento produce resultados compatibles cuando se repite bajo condiciones tan semejantes como sea posible.

[]{#reproducibilidad}

#### 1.2.12.2. Reproducibilidad {#fispm-c01-reproducibilidad}

Preguntamos si el resultado se mantiene cuando cambia razonablemente el realizador, el instrumento, el laboratorio o alguna parte del procedimiento, según el tipo de afirmación que se quiere sostener.

No fijaremos todavía definiciones metrológicas internacionales precisas. Nos basta comprender la diferencia conceptual:

- repetir es volver a hacer algo en condiciones cercanas;

- reproducir pone a prueba si el resultado sobrevive a cambios controlados del contexto experimental.

### 1.2.13. Un dato necesita contexto {#fispm-c01-un-dato-necesita-contexto}

Supongamos que encontramos escrito:

$$T=2.01.$$ ¿Es un dato físico?

No todavía.

Falta saber:

- qué representa $T$;

- en qué unidades está expresado;

- cómo se obtuvo;

- qué sistema se midió;

- bajo qué condiciones;

- con qué procedimiento;

- con qué precisión.

Un número descontextualizado no es un resultado experimental completo.

Incluso

$$T=2.01\ \mathrm{s}$$ sigue siendo insuficiente para muchas preguntas.

La física no opera con números desnudos, sino con resultados insertos en procedimientos y modelos.

### 1.2.14. El papel del instrumento {#fispm-c01-el-papel-del-instrumento}

Un instrumento físico es también un sistema físico. Un reloj puede atrasarse. Una regla se expande térmicamente. Un sensor tiene umbral. Una cámara posee distorsión. Un detector puede dejar de registrar ciertos eventos.

Por eso, cuando conectamos una variable teórica con una observación, incorporamos indirectamente un modelo del instrumento. No siempre necesitaremos describir ese modelo con detalle. Pero debemos recordar que existe.

Esta idea será crucial mucho más adelante. En mecánica cuántica, por ejemplo, el problema de la medición no podrá tratarse como un simple detalle administrativo.

Aquí solo sembramos el hábito:

> **¿Qué interacción física convierte la propiedad que quiero conocer en la señal que efectivamente registro?**

### 1.2.15. Ejemplo desarrollado 4 --- Medir el período sin cronómetro perfecto {#fispm-c01-ejemplo-desarrollado-4-medir-el-peruxedodo-sin-cronuxf3metro-perfecto}

Imaginemos que nuestro cronómetro tiene una resolución limitada. En vez de medir una sola oscilación, podemos medir el tiempo de diez oscilaciones y luego dividir por diez. Si el tiempo total registrado es $T_{10}$, definimos

$$[\mathrm{DEF}] \qquad \overline T:=\frac{T_{10}}{10}.$$ ¿Por qué podría ayudar?

Porque ciertos errores asociados al inicio y al final de la medición pueden representar una fracción menor del tiempo total cuando observamos muchas oscilaciones. No cuantificaremos aún esta mejora; eso corresponde al capítulo de incertidumbre.

Lo importante ahora es metodológico:

> el diseño del procedimiento de observación puede cambiar la calidad de la información obtenida.

La medición no es una ventana transparente e indiferente.

### 1.2.16. Experimentos que discriminan hipótesis {#fispm-c01-experimentos-que-discriminan-hipuxf3tesis}

Supongamos que dos explicaciones predicen lo mismo para todas las situaciones que hemos observado.

Entonces los datos disponibles no permiten distinguirlas.

Necesitamos una situación en la que sus predicciones difieran.

Esta es una función fundamental del experimento:

$$\boxed{ \text{diseñar condiciones en las que hipótesis rivales produzcan consecuencias distinguibles} }$$ No siempre es posible. Algunas hipótesis pueden ser empíricamente indistinguibles dentro del régimen accesible.

Pero cuando sí es posible, el buen experimento no se limita a acumular datos: **busca información que discrimine**.

### 1.2.17. Ejemplo desarrollado 5 --- Dos hipótesis sobre hojas de papel {#fispm-c01-ejemplo-desarrollado-5-dos-hipuxf3tesis-sobre-hojas-de-papel}

Consideremos:

- **Hipótesis A:** el tiempo de caída depende principalmente de la masa.

- **Hipótesis B:** para hojas de masa semejante, la forma y la interacción con el aire pueden modificar fuertemente el tiempo de caída.

Diseñemos comparaciones.

[]{#experimento-1}

#### 1.2.17.1. Experimento 1 {#fispm-c01-experimento-1}

Una hoja extendida frente a la misma hoja arrugada. La masa prácticamente no cambia; la forma sí. Si los tiempos cambian mucho, la comparación proporciona evidencia contra una explicación puramente basada en la masa.

[]{#experimento-2}

#### 1.2.17.2. Experimento 2 {#fispm-c01-experimento-2}

Dos objetos de distinta masa pero formas muy semejantes. Ahora variamos masa manteniendo aproximadamente la geometría.

[]{#experimento-3}

#### 1.2.17.3. Experimento 3 {#fispm-c01-experimento-3}

Repetir en un entorno con mucho menos aire. La diferencia entre ciertos comportamientos puede reducirse. No estamos derivando todavía una teoría de la caída. Estamos aprendiendo a **separar variables mediante diseño experimental**.

### 1.2.18. Control y comparación {#fispm-c01-control-y-comparaciuxf3n}

La palabra «control» tiene varios usos en ciencia. Aquí la utilizaremos informalmente para cualquier disposición que nos ayude a atribuir diferencias observadas a un cambio específico. Si modificamos simultáneamente diez aspectos de un experimento y el resultado cambia, será difícil saber cuál produjo el efecto.

La comparación más informativa suele intentar:

$$\text{cambiar lo que queremos estudiar} \quad\text{y}\quad \text{mantener el resto suficientemente controlado}.$$ En la práctica nunca se mantiene «todo lo demás exactamente igual». Lo que hacemos es justificar que las variaciones restantes no dominan el efecto investigado.

Esta frase ---**no dominan el efecto**--- anticipa el lenguaje de escalas que aprenderemos después.

### 1.2.19. Una observación negativa también necesita procedimiento {#fispm-c01-una-observaciuxf3n-negativa-tambiuxe9n-necesita-procedimiento}

Supongamos que afirmamos:

> «No observamos desviación.»

La frase puede significar muchas cosas.

¿No hubo desviación exactamente? ¿O fue menor que la capacidad del instrumento para detectarla?

Una afirmación negativa debería leerse como:

> «Bajo este procedimiento y dentro de su sensibilidad, no se registró una desviación distinguible.»

Esta forma de hablar evita convertir limitaciones instrumentales en afirmaciones ontológicas. El principio será importante en toda la física experimental.

### 1.2.20. Predicción observable y predicción matemática {#fispm-c01-predicciuxf3n-observable-y-predicciuxf3n-matemuxe1tica}

Imaginemos que un modelo produce exactamente el número

$$1.003847261\ldots$$ para cierta cantidad.

El instrumento solo distingue cambios del orden de una centésima.

Entonces muchas cifras de la predicción matemática no tienen contraparte experimental accesible en ese montaje.

Aquí reaparece nuestra distinción central:

$$\text{precisión matemática} \not\Rightarrow \text{precisión experimental}.$$ Y también su recíproca:

un experimento muy preciso puede revelar que un modelo matemáticamente elegante es físicamente insuficiente.

### 1.2.21. El péndulo como experimento {#fispm-c01-el-puxe9ndulo-como-experimento}

Construyamos una ficha experimental mínima.

[]{#sistema}

#### 1.2.21.1. Sistema {#fispm-c01-sistema}

Esfera suspendida por un hilo de un soporte.

[]{#fenómeno}

#### 1.2.21.2. Fenómeno {#fispm-c01-fenuxf3meno-1}

Oscilación después de separar la esfera de su posición de equilibrio aparente.

[]{#pregunta}

#### 1.2.21.3. Pregunta {#fispm-c01-pregunta}

¿Cómo varía el tiempo de oscilación al modificar una condición determinada?

[]{#observable-principal}

#### 1.2.21.4. Observable principal {#fispm-c01-observable-principal}

Intervalo temporal asociado a una oscilación según un procedimiento definido.

[]{#procedimiento}

#### 1.2.21.5. Procedimiento {#fispm-c01-procedimiento}

1.  fijar una marca de referencia;

2.  definir un evento de inicio;

3.  definir el evento final correspondiente;

4.  registrar tiempo;

5.  repetir.

[]{#variables-que-podemos-modificar}

#### 1.2.21.6. Variables que podemos modificar {#fispm-c01-variables-que-podemos-modificar}

- longitud;

- amplitud inicial;

- masa;

- geometría del cuerpo;

- medio circundante.

[]{#condiciones-que-intentamos-controlar}

#### 1.2.21.7. Condiciones que intentamos controlar {#fispm-c01-condiciones-que-intentamos-controlar}

- soporte;

- procedimiento de liberación;

- instrumento temporal;

- localización;

- definición de una oscilación.

Todavía no sabemos qué variables **deben** aparecer en la ley. Precisamente el experimento puede ayudarnos a descubrirlo.

### 1.2.22. De la observación al modelo y del modelo a la observación {#fispm-c01-de-la-observaciuxf3n-al-modelo-y-del-modelo-a-la-observaciuxf3n}

La relación entre teoría y experimento no es una flecha única.

No hacemos simplemente:

$$\text{observación}\to\text{teoría}.$$ Tampoco:

$$\text{teoría}\to\text{observación}.$$ El trabajo real forma un ciclo:

$$\boxed{ \text{observación} \to \text{modelo} \to \text{predicción} \to \text{nuevo experimento} \to \text{revisión del modelo} }$$ Cada vuelta puede modificar:

- qué variables consideramos;

- qué precisión necesitamos;

- qué experimento es informativo;

- qué idealización aceptamos.

Este ciclo será más importante que cualquier fórmula aislada del libro.

### 1.2.23. Ejercicios de §2 {#fispm-c01-ejercicios-de-2}

[]{#fispm-t1-c01-e0005}

**Ejercicio 1.5 --- Definir una oscilación.**

Propón dos definiciones experimentales distintas de «una oscilación completa» de un péndulo. Explica por qué ambas pueden ser válidas si se usan consistentemente.

**Solución.**

**Definición A:** intervalo entre dos cruces sucesivos del centro en la misma dirección.

**Definición B:** intervalo entre dos máximos sucesivos alcanzados en el mismo lado.

Ambas intentan identificar dos estados equivalentes dentro del ciclo. Pueden producir estimaciones compatibles si el movimiento es suficientemente regular y el procedimiento está bien definido.

[]{#fispm-t1-c01-e0006}

La lección es que una magnitud experimental necesita una regla de identificación de eventos. No basta el nombre «período». **Ejercicio 1.6 --- Video y calibración.**

Una cámara registra una pelota que cae. El centro de la pelota aparece en la fila $420$ de la imagen. Explica por qué el número $420$ no es todavía una altura física.

**Solución.**

El número $420$ es una coordenada en la matriz de imagen. Para transformarla en una altura física necesitamos, como mínimo:

- conocer la geometría de la cámara;

- establecer una escala mediante objetos de longitud conocida;

- fijar un origen;

- conocer la orientación de la imagen;

- decidir qué punto de la pelota representa su posición;

- controlar o corregir distorsiones relevantes.

[]{#fispm-t1-c01-e0007}

Solo después puede construirse una relación `[``OBS``]` entre coordenada de imagen y altura. **Ejercicio 1.7 --- Un experimento poco discriminante.**

Queremos decidir si el color de una esfera afecta el período de un péndulo. Un estudiante reemplaza una esfera pequeña de acero pintada de rojo por una esfera grande de madera azul y encuentra una diferencia.

¿Por qué el experimento no discrimina adecuadamente la hipótesis «el color importa»?

**Solución.**

Se modificaron simultáneamente muchas propiedades:

- color;

- material;

- masa;

- tamaño;

- geometría superficial;

- posiblemente distribución de masa.

Por tanto, aunque aparezca una diferencia, el experimento no permite atribuirla específicamente al color.

[]{#fispm-t1-c01-e0008}

Un diseño mejor cambiaría el color manteniendo tanto como sea posible las demás propiedades relevantes, por ejemplo usando el mismo cuerpo antes y después de aplicar una capa de pintura cuyo efecto adicional se evalúe. **Ejercicio 1.8 --- «No vimos ningún efecto».**

Un detector puede registrar desplazamientos mayores que $1\ \mathrm{mm}$. En un experimento no registra ningún cambio.

¿Cuál de las siguientes conclusiones está justificada?

1.  El desplazamiento es exactamente cero.

2.  El desplazamiento, si existe, no fue distinguible con ese procedimiento.

3.  La teoría que predice desplazamiento es necesariamente falsa.

**Solución.**

La conclusión justificada es **2**. El resultado experimental informa sobre lo que el procedimiento puede distinguir.

[]{#fispm-t1-c01-e0009}

No podemos inferir que el desplazamiento sea matemáticamente exactamente cero. Tampoco podemos rechazar automáticamente toda teoría que prediga un desplazamiento, porque esta podría predecir un valor inferior al umbral de detección o porque habría que revisar otros aspectos del experimento. **Ejercicio 1.9 --- Repetición.**

Se mide cinco veces el tiempo asociado a un mismo procedimiento y se obtienen valores ligeramente distintos.

¿Por qué no es correcto escoger simplemente el valor que «parece más razonable» y descartar los otros?

**Solución.**

Las diferencias contienen información acerca del procedimiento y del sistema. Antes de descartar datos necesitamos criterios explícitos: fallo instrumental identificado, violación de una condición experimental, error de transcripción u otra causa justificable. Elegir el valor preferido porque coincide mejor con una expectativa introduce un sesgo.

[]{#fispm-t1-c01-e0010}

En el capítulo 3 aprenderemos a resumir conjuntos de mediciones y tratar incertidumbres de forma cuantitativa. **Ejercicio 1.10 --- Diseñar una prueba.**

Hipótesis:

> «El tiempo de oscilación de nuestro péndulo cambia apreciablemente si reemplazamos la esfera por otra de masa distinta, manteniendo lo demás igual.»

Diseña un experimento conceptual para poner a prueba la afirmación.

**Solución.**

Una estrategia:

1.  utilizar el mismo hilo y soporte;

2.  preparar varias esferas de geometría exterior lo más semejante posible pero masas distintas;

3.  fijar un procedimiento de liberación;

4.  definir una oscilación mediante eventos reproducibles;

5.  utilizar el mismo método temporal;

6.  medir varias veces para cada esfera;

7.  alternar el orden de las mediciones para reducir efectos de deriva temporal;

8.  comparar los resultados.

Todavía no podemos decidir aquí qué diferencia cuenta como «apreciable» en sentido metrológico riguroso; eso requerirá incertidumbre y escalas.

### 1.2.24. Síntesis de §1--§2 {#fispm-c01-suxedntesis-de-12}

Ya podemos describir una primera parte del trabajo físico.

Comenzamos con un fenómeno:

$$\text{péndulo oscilando}.$$ Formulamos una pregunta:

$$\text{¿qué aspecto queremos explicar o predecir?}$$ Seleccionamos un sistema:

$$\text{¿qué incluimos y qué tratamos como entorno?}$$ Construimos una representación:

$$\text{¿qué objetos matemáticos simbolizarán propiedades físicas?}$$ Definimos observaciones:

$$\text{¿mediante qué procedimiento obtenemos datos comparables?}$$ Y diseñamos experimentos:

$$\text{¿qué debemos controlar o variar para obtener información discriminante?}$$ La cadena que empieza a formarse es

$$\boxed{ \text{fenómeno} \to \text{pregunta} \to \text{sistema} \to \text{representación} \leftrightarrow \text{observación} \to \text{experimento} }.$$ Todavía falta algo decisivo.

¿Qué partes del sistema quedan dentro y cuáles fuera?

¿Cómo distinguimos **estado**, **parámetro** y **observable**?

Ése será el objeto de la sección siguiente (§[1.3](#fispm-c01-sistema-entorno-estado-y-observables)).

[]{#sistema-entorno-estado-y-observables}

[]{#fispm-t1-c01-s03}

[]{#fpm-i-01-s03}

## 1.3. Sistema, entorno, estado y observables {#fispm-c01-sistema-entorno-estado-y-observables}

[]{#elegir-el-sistema-es-trazar-una-frontera}

### 1.3.1. Elegir el sistema es trazar una frontera {#fispm-c01-elegir-el-sistema-es-trazar-una-frontera}

En las dos secciones anteriores hemos usado varias veces la palabra **sistema**. Ahora necesitamos precisar qué trabajo realiza ese concepto. Volvamos al péndulo.

[]{#fig:I-01-N01}

![**Figura 1.2.** La frontera selecciona las variables del sistema y los intercambios con su entorno; cambiarla cambia el balance que habrá que formular. Véase §[1.3](#fispm-c01-sistema-entorno-estado-y-observables).](/assets/books/fispm/v04/I-01-N01.svg "fig:"){.fpm-v04-figure fig-alt="Frontera del sistema" width="374px" fig-cap=""}

Frente a nosotros hay una esfera, un hilo, un soporte, aire, una mesa, un edificio y la Tierra. Todo ello forma parte de una única realidad física continua. Sin embargo, para construir un problema no intentamos describir simultáneamente el universo completo. Seleccionamos una parte.

Podemos decidir, por ejemplo, que nuestro sistema sea:

1.  solo la esfera;

2.  esfera + hilo;

3.  esfera + hilo + soporte;

4.  esfera + hilo + Tierra;

5.  esfera + hilo + aire + Tierra.

Cada elección produce una frontera distinta entre aquello que describiremos **dentro** del modelo y aquello que trataremos como **entorno**.

**Definición operativa 1.7 --- Sistema físico (formulación refinada)** Para una pregunta dada, llamaremos **sistema físico** al conjunto de objetos, componentes o procesos que elegimos describir explícitamente como objeto principal del modelo.

**Definición operativa 1.8 --- Entorno** Llamaremos **entorno** a aquello que queda fuera de la frontera elegida del sistema pero que puede influir en él, recibir influencia de él o ser relevante para interpretar las observaciones.

La frontera puede coincidir con una superficie material, pero no tiene por qué hacerlo.

Si estudiamos la temperatura de una taza de café, podríamos tomar como sistema:

- solo el líquido;

- líquido + taza;

- líquido + taza + una capa de aire circundante.

La frontera del sistema es, en primer lugar, una **decisión de modelización**.

### 1.3.2. La frontera no separa «lo real» de «lo irreal» {#fispm-c01-la-frontera-no-separa-lo-real-de-lo-irreal}

Cuando dejamos el aire fuera del sistema del péndulo, el aire no deja de existir. Cuando modelamos la Tierra como parte del entorno, la gravedad no desaparece. Esto parece obvio, pero evita un error frecuente: interpretar la frontera del modelo como una frontera ontológica.

El esquema correcto es:

$$\boxed{ \text{fuera del sistema} \not\Rightarrow \text{sin efecto} }$$ Un efecto externo puede aparecer en el modelo mediante una cantidad prescrita, una condición o una interacción efectiva, aun cuando el mecanismo que la produce no sea descrito en detalle.

Más adelante, por ejemplo, podremos representar la influencia de un entorno mediante campos externos, fuerzas externas, condiciones de frontera, fuentes o depósitos. Todavía no necesitamos ese formalismo.

Por ahora basta distinguir dos operaciones:

- **incluir** un componente significa modelar explícitamente parte de su estado o dinámica;

- **externalizar** un componente significa no seguir todos sus detalles internos, aunque podamos representar algunos de sus efectos.

### 1.3.3. Tres fronteras para el mismo péndulo {#fispm-c01-tres-fronteras-para-el-mismo-puxe9ndulo}

Consideremos tres elecciones.

[]{#modelo-a-la-esfera-como-sistema}

#### 1.3.3.1. Modelo A --- La esfera como sistema {#fispm-c01-modelo-a-la-esfera-como-sistema}

El hilo, el soporte, el aire y la Tierra pertenecen al entorno. Este modelo puede ser útil si nuestro interés está concentrado en la trayectoria de la esfera y representamos los demás efectos de forma externa.

[]{#modelo-b-esfera-hilo-como-sistema}

#### 1.3.3.2. Modelo B --- Esfera + hilo como sistema {#fispm-c01-modelo-b-esfera-hilo-como-sistema}

Ahora la tensión, deformación o movimiento del hilo pueden convertirse en parte explícita de la descripción.

[]{#modelo-c-esfera-hilo-tierra-como-sistema}

#### 1.3.3.3. Modelo C --- Esfera + hilo + Tierra como sistema {#fispm-c01-modelo-c-esfera-hilo-tierra-como-sistema}

Esta elección puede ser útil si nos interesa contabilizar intercambios internos entre el cuerpo suspendido y la Tierra en una descripción más global. Las tres fronteras son legítimas. No existe una regla general según la cual «el sistema más grande sea el más correcto».

**Principio 1.5 --- La frontera del sistema se elige para la pregunta** Una buena frontera incluye la estructura necesaria para responder la pregunta sin obligarnos a modelar detalles que no aportan información relevante en el régimen considerado.

Esta es una forma temprana del principio de **modelo mínimo suficiente** que usaremos repetidamente.

### 1.3.4. ¿Qué significa conocer el estado de un sistema? {#fispm-c01-quuxe9-significa-conocer-el-estado-de-un-sistema}

Supongamos que vemos un péndulo en una fotografía. La esfera aparece a la derecha de la vertical.

¿Sabemos cómo continuará el movimiento?

No necesariamente.

Podría estar moviéndose hacia la derecha y acercándose a su punto de retorno. O podría estar moviéndose hacia la izquierda después de haberlo alcanzado. La misma posición visible puede corresponder a evoluciones posteriores diferentes.

La lección es fundamental:

$$\boxed{ \text{describir dónde está algo} \neq \text{describir completamente su estado} }$$ En mecánica elemental aprenderemos que cierta información adicional ---por ejemplo, información asociada al movimiento--- resulta necesaria.

Pero queremos formular ahora una noción suficientemente general para que sobreviva a teorías posteriores.

**Definición operativa 1.9 --- Estado** Dado un modelo físico, un **estado** es una especificación matemática de la condición del sistema que contiene la información que ese modelo considera suficiente para formular sus predicciones, una vez fijados los parámetros, las leyes y las influencias externas pertinentes.

Hay dos palabras que no debemos omitir:

$$\boxed{\text{dado un modelo}}$$ La noción de estado no se define independientemente de la teoría.

### 1.3.5. El estado es relativo al nivel de descripción {#fispm-c01-el-estado-es-relativo-al-nivel-de-descripciuxf3n}

Consideremos un gas dentro de un recipiente.

Podríamos construir una descripción microscópica en la que intentamos seguir una enorme cantidad de información sobre sus constituyentes. También podemos construir una descripción macroscópica mediante unas pocas magnitudes globales. Ambas pueden hablar de «estado», pero no contienen la misma información.

Más adelante distinguiremos con precisión **microestado** y **macroestado**. Aquí basta extraer la regla:

$$\boxed{ \text{qué cuenta como estado depende de qué estructura conserva el modelo} }$$ Lo mismo ocurre con un cuerpo extenso.

En un modelo de partícula puntual, su orientación puede no formar parte del estado. En un modelo de cuerpo rígido, la orientación puede ser esencial. En un modelo que además permite deformaciones, necesitaremos todavía más información.

Por tanto, preguntar simplemente «¿cuál es el estado real del objeto?» sin especificar una teoría o nivel de descripción puede ser demasiado ambiguo para nuestro propósito.

### 1.3.6. Espacio de estados: primera aparición {#fispm-c01-espacio-de-estados-primera-apariciuxf3n}

El lector matemático reconocerá inmediatamente una estructura útil. Si llamamos $\mathcal S$ al conjunto de todos los estados admitidos por un modelo, podemos escribir

$$s\in\mathcal S.$$ **Definición operativa 1.10 --- Espacio de estados** El **espacio de estados** de un modelo es el conjunto ---dotado más adelante de la estructura matemática que corresponda--- cuyos elementos representan los estados admitidos por ese modelo.

Por ahora, la palabra «espacio» no presupone topología, métrica, estructura vectorial ni variedad diferenciable.

Solo estamos diciendo:

$$\mathcal S=\{\text{estados permitidos por el modelo}\}.$$ En capítulos posteriores veremos ejemplos muy distintos:

- espacios de configuraciones;

- espacios de fases;

- espacios de estados termodinámicos;

- espacios de Hilbert.

No debemos confundirlos de antemano.

### 1.3.7. Variable: una palabra demasiado amplia {#fispm-c01-variable-una-palabra-demasiado-amplia}

En física usamos constantemente la palabra **variable**.

Puede referirse a:

- una coordenada que cambia con el estado;

- una magnitud que registramos;

- una cantidad que controlamos experimentalmente;

- un parámetro que variamos de un experimento a otro;

- incluso una variable matemática auxiliar.

Por eso necesitamos distinguir funciones.

**Definición operativa 1.11 --- Variable de estado** Una **variable de estado** es una cantidad utilizada por el modelo para describir o distinguir estados del sistema.

Si dos estados pueden diferir en una cantidad $q$, podemos representarla esquemáticamente mediante

$$q:\mathcal S\to V,$$ donde $V$ es el conjunto de valores posibles.

Esta escritura no afirma todavía que toda variable física sea una función ordinaria en todas las teorías. Es una plantilla apropiada para los modelos clásicos elementales que comenzaremos a estudiar.

### 1.3.8. Parámetro: fijo dentro del problema, variable entre modelos o realizaciones {#fispm-c01-paruxe1metro-fijo-dentro-del-problema-variable-entre-modelos-o-realizaciones}

Consideremos un péndulo idealizado de longitud $\ell$. En un experimento concreto podemos fijar $\ell=1\,\mathrm{m}$ y estudiar cómo cambia el estado del péndulo con el tiempo. Entonces $\ell$ funciona como un **parámetro** del modelo, no como una variable que necesitemos actualizar para describir cada instante.

**Definición operativa 1.12 --- Parámetro** Un **parámetro** es una cantidad que caracteriza al sistema o al modelo y que se trata como fija al describir una realización determinada, aunque pueda tomar otros valores al comparar sistemas, experimentos o miembros de una familia de modelos.

Podemos escribir una familia de modelos como

$$\mathcal M_\theta,$$ donde $\theta$ representa uno o varios parámetros.

La distinción importante no es:

$$\text{variable}=\text{cambia realmente},\qquad \text{parámetro}=\text{no cambia realmente}.$$ Es una distinción de **papel dentro del modelo**.

La longitud de una barra puede tratarse como parámetro en un problema y convertirse en variable de estado en otro problema donde estudiamos su dilatación.

### 1.3.9. La misma magnitud puede cambiar de papel {#fispm-c01-la-misma-magnitud-puede-cambiar-de-papel}

Este punto merece un ejemplo explícito.

[]{#problema-a-péndulo-de-longitud-fija}

#### 1.3.9.1. Problema A --- Péndulo de longitud fija {#fispm-c01-problema-a-puxe9ndulo-de-longitud-fija}

La longitud $\ell$ se mide antes del experimento y se mantiene fija.

Rol: $\ell \quad \text{parámetro}.$

#### 1.3.9.2. Problema B --- Hilo elástico {#fispm-c01-problema-b-hilo-eluxe1stico}

Ahora la longitud puede cambiar durante el movimiento.

Rol: $\ell \quad \text{variable de estado}.$

#### 1.3.9.3. Problema C --- Calibración de una regla {#fispm-c01-problema-c-calibraciuxf3n-de-una-regla}

La longitud del objeto puede ser precisamente la cantidad que queremos inferir de una observación.

Rol:

$$\ell \quad \text{cantidad observada o estimada}.$$ La magnitud física no lleva escrita una etiqueta eterna.

**Principio 1.6 --- Los roles pertenecen al modelo** «Variable», «parámetro», «observable» y «dato de control» describen el papel que una cantidad cumple dentro de una modelización o experimento; una misma magnitud puede desempeñar papeles distintos en problemas diferentes.

### 1.3.10. Observable: ahora podemos precisar la definición {#fispm-c01-observable-ahora-podemos-precisar-la-definiciuxf3n}

En §2 dijimos que un observable es una propiedad que el modelo conecta con un procedimiento de observación o medición. Ahora podemos expresarlo matemáticamente en el caso clásico elemental. Si el sistema está en un estado $s\in\mathcal S$, un observable puede representarse por una función

$$O:\mathcal S\to\mathcal V,$$ de modo que

$$O(s)$$ sea el valor que el modelo asocia al estado.

Pero todavía falta la física. La función matemática por sí sola no nos dice cómo obtener un dato.

Necesitamos una regla `[``OBS``]` que conecte:

$$O(s) \quad\longleftrightarrow\quad \text{procedimiento experimental}.$$ Por tanto, un observable físico posee dos caras:

$$\boxed{ \text{estructura matemática} + \text{interpretación operacional} }.$$ En mecánica cuántica esta descripción mediante funciones ordinarias sobre estados dejará de ser adecuada y la noción de observable adquirirá una estructura distinta. No adelantaremos esa teoría, pero evitaremos construir una definición que después debamos deshacer.

### 1.3.11. Estado y observable tampoco son lo mismo {#fispm-c01-estado-y-observable-tampoco-son-lo-mismo}

Supongamos que un modelo necesita dos variables para especificar el estado:

$$s=(q_1,q_2).$$ Podemos medir solamente una combinación

$$O(s)=q_1+q_2.$$ Dos estados diferentes pueden producir el mismo valor observable:

$$(q_1,q_2)=(1,2)$$ y

$$(q_1,q_2)=(2,1)$$ dan en ambos casos

$$O=3.$$ Por tanto,

$$\boxed{ \text{un valor observable no tiene por qué determinar el estado} }.$$ Este ejemplo algebraico elemental anticipa un problema muy general: **reconstruir estados a partir de observaciones**.

Más adelante aparecerá bajo formas mucho más sofisticadas.

### 1.3.12. Ejemplo desarrollado 6 --- La Tierra bajo cinco preguntas {#fispm-c01-ejemplo-desarrollado-6-la-tierra-bajo-cinco-preguntas}

La Tierra ofrece un excelente laboratorio conceptual porque el mismo objeto admite modelos radicalmente distintos.

[]{#pregunta-a-dónde-está-una-persona-dentro-de-una-habitación}

#### 1.3.12.1. Pregunta A --- ¿Dónde está una persona dentro de una habitación? {#fispm-c01-pregunta-a-duxf3nde-estuxe1-una-persona-dentro-de-una-habitaciuxf3n}

Podemos tratar el suelo local como un plano. La curvatura global de la Tierra queda fuera del modelo.

[]{#pregunta-b-cuál-es-una-ruta-aproximada-entre-ciudades-lejanas}

#### 1.3.12.2. Pregunta B --- ¿Cuál es una ruta aproximada entre ciudades lejanas? {#fispm-c01-pregunta-b-cuuxe1l-es-una-ruta-aproximada-entre-ciudades-lejanas}

La geometría esférica se vuelve relevante.

[]{#pregunta-c-cuál-es-la-forma-de-referencia-necesaria-para-geodesia-precisa}

#### 1.3.12.3. Pregunta C --- ¿Cuál es la forma de referencia necesaria para geodesia precisa? {#fispm-c01-pregunta-c-cuuxe1l-es-la-forma-de-referencia-necesaria-para-geodesia-precisa}

Una esfera perfecta puede no bastar; entran modelos más refinados como el geoide y el elipsoide de referencia.

[]{#pregunta-d-cómo-describimos-ciertos-efectos-de-la-rotación-terrestre}

#### 1.3.12.4. Pregunta D --- ¿Cómo describimos ciertos efectos de la rotación terrestre? {#fispm-c01-pregunta-d-cuxf3mo-describimos-ciertos-efectos-de-la-rotaciuxf3n-terrestre}

La Tierra debe poseer orientación y movimiento de rotación; un simple punto deja de contener la información necesaria.

[]{#pregunta-e-cómo-aproximamos-su-influencia-gravitatoria-sobre-un-objeto-muy-lejano}

#### 1.3.12.5. Pregunta E --- ¿Cómo aproximamos su influencia gravitatoria sobre un objeto muy lejano? {#fispm-c01-pregunta-e-cuxf3mo-aproximamos-su-influencia-gravitatoria-sobre-un-objeto-muy-lejano}

En ciertas circunstancias puede bastar un modelo de masa concentrada.

Podemos resumir:

  Pregunta             Modelo de Tierra             Información retenida
  -------------------- ---------------------------- -----------------------------
  habitación           plano local                  geometría local
  navegación global    esfera                       curvatura global aproximada
  geodesia             geoide/elipsoide             forma refinada
  rotación             cuerpo extenso en rotación   orientación y rotación
  interacción lejana   masa puntual aproximada      masa y posición

El cambio de modelo cambia también qué entendemos por **estado** de la Tierra. Una masa puntual necesita mucha menos información que un cuerpo extenso en rotación.

### 1.3.13. Ejemplo desarrollado 7 --- Una habitación y su temperatura {#fispm-c01-ejemplo-desarrollado-7-una-habitaciuxf3n-y-su-temperatura}

Consideremos la pregunta:

> ¿Cómo cambia la temperatura de una habitación cuando encendemos un calefactor?

Podemos elegir varios sistemas.

[]{#sistema-1-el-aire-de-la-habitación}

#### 1.3.13.1. Sistema 1 --- El aire de la habitación {#fispm-c01-sistema-1-el-aire-de-la-habitaciuxf3n}

Paredes, ventanas, calefactor y exterior pertenecen al entorno.

[]{#sistema-2-aire-paredes-muebles}

#### 1.3.13.2. Sistema 2 --- Aire + paredes + muebles {#fispm-c01-sistema-2-aire-paredes-muebles}

Ahora parte del almacenamiento de energía térmica queda dentro de la frontera.

[]{#sistema-3-habitación-calefactor}

#### 1.3.13.3. Sistema 3 --- Habitación + calefactor {#fispm-c01-sistema-3-habitaciuxf3n-calefactor}

El mecanismo de producción y transferencia de energía puede representarse con mayor detalle. Una variable que en un modelo era externa puede convertirse en variable interna al ampliar el sistema. La frontera reorganiza la descripción.

### 1.3.14. Ejemplo desarrollado 8 --- ¿Parámetro u observable? {#fispm-c01-ejemplo-desarrollado-8-paruxe1metro-u-observable}

Supongamos un bloque cuya masa $m$ ha sido medida antes de comenzar un experimento.

Durante una serie de movimientos tratamos

$$m=0.50\,\mathrm{kg}$$ como valor fijo.

En el modelo dinámico:

$$m \quad \text{es parámetro}.$$ Pero para obtener ese valor realizamos previamente una medición.

En el experimento de calibración:

$$m \quad \text{fue una cantidad inferida observacionalmente}.$$ No hay contradicción.

Debemos distinguir:

- **estatus epistemológico:** ¿cómo conocemos el valor?;

- **rol matemático dentro del modelo:** ¿se actualiza con el estado o se mantiene fijo?;

- **rol experimental:** ¿es control, entrada o resultado?

Esta triple distinción será útil en todo el libro.

### 1.3.15. Una ficha mínima de sistema {#fispm-c01-una-ficha-muxednima-de-sistema}

Desde ahora podremos construir una ficha preliminar:

**Ficha FPM de sistema --- versión 1** - **Pregunta:** ¿qué queremos explicar, calcular o comparar? - **Sistema:** ¿qué queda dentro? - **Entorno:** ¿qué queda fuera y puede influir? - **Estado:** ¿qué información considera suficiente el modelo? - **Variables de estado:** ¿qué cantidades distinguen estados? - **Parámetros:** ¿qué cantidades se mantienen fijas dentro de una realización? - **Observables:** ¿qué propiedades se conectan con procedimientos de medida? - **Controles experimentales:** ¿qué fijamos deliberadamente? - **Omisiones:** ¿qué estructura real no estamos representando?

En capítulos posteriores añadiremos:

- unidades;

- escalas;

- incertidumbres;

- condiciones iniciales y de frontera;

- leyes;

- simetrías;

- aproximaciones;

- dominios de validez.

### 1.3.16. Ejercicios de §3 {#fispm-c01-ejercicios-de-3}

[]{#fispm-t1-c01-e0011}

**Ejercicio 1.11 --- Tres fronteras para un péndulo.**

Construye tres elecciones distintas de sistema para estudiar un péndulo:

1.  una en la que el sistema sea mínimo;

2.  una en la que el hilo forme parte explícita del sistema;

3.  una en la que también la Tierra quede dentro de la frontera.

Para cada elección, indica qué elementos pasan al entorno y qué preguntas podrían justificar esa frontera.

**Solución.**

**Modelo A: esfera únicamente.**

Entorno: hilo, soporte, aire, Tierra.

Puede ser adecuado para una primera descripción de la posición de la esfera cuando los efectos del hilo y de la Tierra se representan de manera externa.

**Modelo B: esfera + hilo.**

Entorno: soporte, aire, Tierra.

Puede ser necesario si nos interesa la masa, elasticidad o vibración del hilo.

**Modelo C: esfera + hilo + Tierra.**

Entorno: aire, soporte y resto del universo, según el problema.

Puede ser útil si queremos tratar la interacción esfera--Tierra como interna al sistema, por ejemplo en una contabilidad global de intercambios.

[]{#fispm-t1-c01-e0012}

No hay una frontera universalmente correcta. La justificación depende de la pregunta. **Ejercicio 1.12 --- Cinco Tierras.**

Elige entre los modelos **plano local**, **esfera**, **geoide/elipsoide**, **cuerpo extenso en rotación** y **masa puntual** para las siguientes preguntas:

1.  posiciones dentro de una cancha;\

2.  navegación intercontinental;\

3.  geodesia de alta precisión;\

4.  efectos asociados a la rotación terrestre;\

5.  primera aproximación a la interacción gravitatoria con un objeto muy lejano.

Justifica cada elección.

**Solución.**

1.  **Plano local.** La curvatura es irrelevante para la precisión ordinaria de una cancha.

2.  **Esfera.** La curvatura global afecta distancias y rutas.

3.  **Geoide/elipsoide.** La forma real necesita mayor precisión que una esfera.

4.  **Cuerpo extenso en rotación.** Debemos conservar orientación y rotación.

5.  **Masa puntual**, bajo un régimen en el que la estructura interna y el tamaño sean despreciables para la pregunta.

[]{#fispm-t1-c01-e0013}

La solución muestra que el mismo objeto físico puede exigir distintos espacios de estados y parámetros según el modelo. **Ejercicio 1.13 --- Estado, parámetro u observable.**

En cada caso clasifica la cantidad por su **rol principal dentro del modelo indicado**.

1.  La longitud fija $\ell$ de un péndulo ideal durante una serie de oscilaciones.

2.  La posición instantánea de la esfera.

3.  La lectura temporal obtenida por un sensor.

4.  La longitud de un hilo elástico cuando precisamente estudiamos su estiramiento.

5.  La masa de una esfera medida antes del experimento y tratada después como fija.

**Solución.**

1.  **Parámetro.** Se fija para esa realización.

2.  **Variable de estado.** Ayuda a distinguir estados.

3.  **Dato asociado a un observable.** Es un resultado del procedimiento de medición.

4.  **Variable de estado** en ese modelo, porque cambia durante el proceso estudiado.

5.  **Parámetro** dentro del modelo dinámico, aunque su valor haya sido obtenido mediante una observación previa.

[]{#fispm-t1-c01-e0014}

La pregunta se refiere al rol en el modelo, no a una naturaleza absoluta de la magnitud. **Ejercicio 1.14 --- Una observación no determina el estado.**

Sea un modelo con estados

$$s=(q_1,q_2)\in\mathbb R^2$$ y un observable

$$O(s)=q_1+q_2.$$ a) Encuentra dos estados distintos con el mismo valor $O=5$.\
b) Explica qué demuestra este ejemplo acerca de la reconstrucción de un estado a partir de una sola observación.

**Solución.**

1.  Por ejemplo,

$$s_1=(2,3),\qquad s_2=(1,4).$$ Son estados distintos porque

$$s_1\neq s_2,$$ pero

$$O(s_1)=2+3=5,$$ y

$$O(s_2)=1+4=5.$$ b) La aplicación $O$ no es inyectiva. Por tanto, conocer un único valor observable no permite distinguir todos los estados del modelo.

Físicamente:

$$\boxed{\text{mismo dato observable}\not\Rightarrow\text{mismo estado}}$$ a menos que tengamos información adicional que garantice una correspondencia unívoca.

[]{#síntesis}

### 1.3.17. Síntesis {#fispm-c01-suxedntesis}

La frontera de un sistema, su estado y sus observables no vienen determinados por el objeto material considerado aisladamente. Dependen de la pregunta y del modelo. Hemos construido ahora la cadena

$$\boxed{ \text{pregunta} \to \text{sistema/entorno} \to \text{estado} \to \text{variables y parámetros} \to \text{observables} \to \text{datos} }.$$ También hemos aprendido cuatro distinciones que reaparecerán continuamente:

$$\boxed{ \text{sistema}\neq\text{entorno} }$$ $$\boxed{ \text{estado}\neq\text{observación individual} }$$ $$\boxed{ \text{variable de estado}\neq\text{parámetro} }$$ y

$$\boxed{ \text{observable}\neq\text{dato}. }$$ La siguiente pregunta es inevitable.

Para obtener un modelo manejable hemos omitido estructura real, sustituido objetos por representaciones simplificadas y, en ocasiones, reemplazaremos relaciones exactas por otras más simples. Pero esas operaciones no son todas iguales.

La sección siguiente distinguirá cuidadosamente:

$$\boxed{ \text{abstracción} \neq \text{idealización} \neq \text{aproximación}. }$$

[]{#idealización-abstracción-y-aproximación}

[]{#fispm-t1-c01-s04}

[]{#fpm-i-01-s04}

## 1.4. Idealización, abstracción y aproximación {#fispm-c01-idealizaciuxf3n-abstracciuxf3n-y-aproximaciuxf3n}

[]{#tres-operaciones-que-no-debemos-confundir}

### 1.4.1. Tres operaciones que no debemos confundir {#fispm-c01-tres-operaciones-que-no-debemos-confundir}

En las secciones anteriores hemos construido modelos seleccionando sistemas, variables, parámetros y observables. Para hacerlo hemos simplificado. Pero **simplificar** no nombra una sola operación.

[]{#fig:I-01-R02}

![**Figura 1.3.** Las expresiones normalizadas $e^{-u}$ y $1-u$ comparten valor y derivada en $u=0$. La segunda sirve localmente y se vuelve negativa para $u>1$; esa extrapolación puede contrariar el significado físico de una cantidad positiva. Véase §[1.4](#fispm-c01-idealizaciuxf3n-abstracciuxf3n-y-aproximaciuxf3n).](/assets/books/fispm/v04/I-01-R02.svg "fig:"){.fpm-v04-figure fig-alt="Modelo exacto y aproximación local" width="403px" fig-cap=""}

Cuando decimos que una esfera se representa mediante un punto, que ignoramos el color de una pelota o que reemplazamos una expresión por otra numéricamente cercana, estamos haciendo cosas conceptualmente distintas.

En este libro distinguiremos tres operaciones:

$$\boxed{ \text{abstracción} \neq \text{idealización} \neq \text{aproximación}. }$$ La separación será importante porque cada una exige una pregunta de control diferente.

- Ante una **abstracción** preguntaremos:\
  **¿qué estructura conservamos y qué particularidades dejamos fuera?**

- Ante una **idealización** preguntaremos:\
  **¿qué propiedad imposible o límite estamos suponiendo exactamente?**

- Ante una **aproximación** preguntaremos:\
  **¿qué diferencia estamos despreciando, comparada con qué, y en qué régimen?**

Estas tres preguntas reaparecerán durante los cuatro tomos.

### 1.4.2. Abstracción: conservar estructura y olvidar particulares {#fispm-c01-abstracciuxf3n-conservar-estructura-y-olvidar-particulares}

Consideremos tres objetos:

- una esfera metálica;

- una pelota de goma;

- una piedra redondeada.

Para una pregunta acerca de su color, debemos distinguirlos. Para una pregunta acerca de su volumen, quizá debamos conservar forma y tamaño. Para una primera pregunta sobre la trayectoria de sus centros, podríamos representar los tres mediante posiciones en el espacio y olvidar temporalmente color, textura y composición.

**Definición operativa 1.13 --- Abstracción** Una **abstracción** es la operación mediante la cual seleccionamos ciertas relaciones, propiedades o estructuras como relevantes para una pregunta y dejamos de representar explícitamente otras particularidades del sistema.

Abstraer no significa afirmar que las propiedades omitidas sean nulas. Si en un problema representamos una pelota únicamente por su posición, no estamos afirmando que no tenga color o temperatura. Estamos diciendo que esas propiedades **no forman parte de la descripción actual**.

En forma esquemática:

$$\text{sistema concreto} \longrightarrow \text{estructura seleccionada}.$$ La flecha pierde información deliberadamente.

### 1.4.3. Abstracción no significa falsificación {#fispm-c01-abstracciuxf3n-no-significa-falsificaciuxf3n}

Un mapa vial omite la composición química del asfalto. Esa omisión no convierte al mapa en falso. Una lista de temperaturas de una ciudad omite la forma de cada edificio. Tampoco por ello es falsa.

El criterio es funcional:

> ¿la estructura conservada es la que necesitamos para responder la pregunta?

Podemos llamar a esta idea **pérdida controlada de información**.

No toda pérdida es aceptable. Si queremos estudiar cómo gira un cuerpo rígido, abstraer toda información acerca de su orientación destruiría precisamente la estructura que necesitamos.

**Principio 1.7 --- Una abstracción es adecuada si conserva las distinciones relevantes para la pregunta** Omitir información es legítimo solo en la medida en que las distinciones eliminadas no sean necesarias para las predicciones, comparaciones o explicaciones que el modelo pretende realizar.

### 1.4.4. Idealización: introducir un objeto que no existe exactamente {#fispm-c01-idealizaciuxf3n-introducir-un-objeto-que-no-existe-exactamente}

La idealización hace algo más fuerte.

Pensemos en una **partícula puntual**. Un cuerpo material ocupa una región del espacio. Una partícula puntual, en cambio, se representa como si toda la estructura espacial relevante estuviera concentrada en un punto.

No hemos simplemente dejado de hablar del radio.

Hemos reemplazado el cuerpo por un objeto con una propiedad exacta que ningún cuerpo macroscópico posee literalmente: extensión espacial nula.

**Definición operativa 1.14 --- Idealización** Una **idealización** sustituye un sistema o una de sus propiedades por un objeto, condición o comportamiento simplificado que se trata como exacto dentro del modelo, aunque no se realice exactamente en el sistema físico.

Ejemplos típicos:

- partícula puntual;

- hilo sin masa;

- cuerpo perfectamente rígido;

- superficie sin rozamiento;

- gas ideal;

- lente infinitamente delgada;

- campo exactamente uniforme;

- recipiente perfectamente aislado.

La marca conceptual es:

$$\boxed{\text{«exacto en el modelo» no significa «exacto en el mundo».}}$$

### 1.4.5. Una idealización puede ser excelente sin ser literalmente realizable {#fispm-c01-una-idealizaciuxf3n-puede-ser-excelente-sin-ser-literalmente-realizable}

Supongamos que modelamos una esfera pequeña como partícula puntual. Si la pregunta concierne a una trayectoria cuya escala espacial es enorme comparada con el tamaño de la esfera, la estructura interna puede tener un efecto despreciable sobre la cantidad que queremos calcular.

Entonces la idealización puede ser extraordinariamente útil.

Pero si preguntamos por:

- su rotación;

- su deformación;

- el momento en que una parte de su superficie toca otra superficie;

- su resistencia aerodinámica;

la extensión espacial deja de ser irrelevante. La misma idealización puede pasar de buena a mala sin que el objeto físico haya cambiado. Ha cambiado la **pregunta**.

### 1.4.6. Idealización y abstracción: diferencia mediante un mismo cuerpo {#fispm-c01-idealizaciuxf3n-y-abstracciuxf3n-diferencia-mediante-un-mismo-cuerpo}

Tomemos una pelota real.

[]{#abstracción}

#### 1.4.6.1. Abstracción {#fispm-c01-abstracciuxf3n}

Decidimos no registrar su color. La pelota del modelo todavía puede conservar tamaño, masa y forma.

No hemos afirmado:

$$\text{color}=0.$$ Simplemente no hay una variable «color» en nuestra descripción.

[]{#idealización}

#### 1.4.6.2. Idealización {#fispm-c01-idealizaciuxf3n}

Representamos la pelota como un punto.

Ahora introducimos una condición exacta del modelo:

$$\text{extensión espacial}=0.$$ Esta condición no describe literalmente la pelota.

Por tanto:

$$\boxed{ \text{abstracción}=\text{no representar cierta información} }$$ mientras que

$$\boxed{ \text{idealización}=\text{representar mediante una condición simplificada tratada como exacta}. }$$ La frontera entre ambas puede depender del formalismo, pero la distinción es metodológicamente útil.

### 1.4.7. Aproximación: reemplazar por algo cercano {#fispm-c01-aproximaciuxf3n-reemplazar-por-algo-cercano}

Pasemos ahora a una operación diferente.

Supongamos que una relación exacta dentro de un modelo es

$$Q=1-2\varepsilon+\varepsilon^2.$$ Podemos decidir usar

$$Q\approx 1-2\varepsilon$$ cuando $\varepsilon$ es suficientemente pequeño para la precisión que buscamos.

Aquí no hemos cambiado necesariamente el objeto físico ni la frontera del sistema.

Hemos reemplazado una expresión por otra que esperamos que sea **cercana** en cierto régimen.

**Definición operativa 1.15 --- Aproximación** Una **aproximación** reemplaza una cantidad, relación o modelo por otro más simple cuya diferencia respecto del original se considera suficientemente pequeña para una pregunta y un régimen especificados.

La palabra decisiva es **diferencia**. Una aproximación exige, al menos conceptualmente, alguna manera de comparar.

### 1.4.8. Primera aproximación controlada sin cálculo {#fispm-c01-primera-aproximaciuxf3n-controlada-sin-cuxe1lculo}

Consideremos la identidad exacta

$$(1-\varepsilon)^2 = 1-2\varepsilon+\varepsilon^2.$$ Supongamos que usamos

$$(1-\varepsilon)^2 \approx 1-2\varepsilon.$$ ¿Qué hemos hecho?

El término omitido es exactamente

$$\varepsilon^2.$$ Por tanto, el error algebraico introducido por esta sustitución es

$$E=\varepsilon^2.$$ Si queremos comparar el término omitido con el término lineal $\varepsilon$, para $\varepsilon\neq0$,

$$\frac{|\varepsilon^2|}{|\varepsilon|} = |\varepsilon|.$$ Así, si

$$|\varepsilon|=0.01,$$ entonces

$$\frac{|\varepsilon^2|}{|\varepsilon|} = 0.01.$$ El término cuadrático posee solo una centésima parte del tamaño de un término proporcional a $\varepsilon$.

No necesitamos todavía series de Taylor para comprender la idea.

**Principio 1.8 --- Una aproximación debe hacer visible qué se omite** Siempre que sea posible, registraremos la cantidad o término despreciado y explicaremos por qué es pequeño respecto de la escala relevante.

### 1.4.9. «Pequeño» no es una propiedad absoluta {#fispm-c01-pequeuxf1o-no-es-una-propiedad-absoluta}

Supongamos que alguien afirma:

> «Un centímetro es pequeño.»

La frase está incompleta. Un centímetro es pequeño comparado con el radio de la Tierra.

Puede ser enorme comparado con el grosor de una célula.

Puede ser decisivo en el ajuste de una pieza mecánica. Por eso, la palabra **pequeño** necesita una comparación.

Sin desarrollar todavía análisis dimensional, podemos formular la regla conceptual:

$$\boxed{ \text{pequeño} = \text{pequeño respecto de una escala relevante}. }$$ Del mismo modo, decir que «el aire tiene poco efecto» exige preguntar:

> ¿poco efecto sobre qué magnitud, durante qué intervalo y con qué precisión?

### 1.4.10. Aproximación no significa simplemente redondeo {#fispm-c01-aproximaciuxf3n-no-significa-simplemente-redondeo}

Si

$$\pi\approx3.14,$$ hemos realizado una aproximación numérica.

Pero en física las aproximaciones importantes suelen ser estructurales.

Podemos:

- despreciar un término;

- reemplazar una geometría por otra;

- usar una ley límite;

- linealizar una relación;

- separar escalas;

- reemplazar una interacción compleja por una efectiva.

Algunas de estas operaciones se combinan con idealizaciones. Por eso debemos registrar el nivel exacto en que ocurre la simplificación.

### 1.4.11. El péndulo: una escalera de operaciones distintas {#fispm-c01-el-puxe9ndulo-una-escalera-de-operaciones-distintas}

Volvamos a nuestro caso conductor.

[]{#paso-1-no-registrar-el-color-del-cuerpo}

#### 1.4.11.1. Paso 1 --- No registrar el color del cuerpo {#fispm-c01-paso-1-no-registrar-el-color-del-cuerpo}

**Tipo:** abstracción.

El color queda fuera de las variables del modelo.

[]{#paso-2-representar-el-cuerpo-como-masa-puntual}

#### 1.4.11.2. Paso 2 --- Representar el cuerpo como masa puntual {#fispm-c01-paso-2-representar-el-cuerpo-como-masa-puntual}

**Tipo:** idealización.

La extensión espacial se hace exactamente nula dentro del modelo.

[]{#paso-3-representar-el-hilo-como-inextensible-y-sin-masa}

#### 1.4.11.3. Paso 3 --- Representar el hilo como inextensible y sin masa {#fispm-c01-paso-3-representar-el-hilo-como-inextensible-y-sin-masa}

**Tipo:** idealización.

No estamos diciendo que el hilo real tenga literalmente esas propiedades.

[]{#paso-4-ignorar-la-resistencia-del-aire}

#### 1.4.11.4. Paso 4 --- Ignorar la resistencia del aire {#fispm-c01-paso-4-ignorar-la-resistencia-del-aire}

Puede formularse de dos maneras distintas:

- como **idealización**, si el modelo declara exactamente nula la disipación;

- como **aproximación**, si partimos de un modelo con disipación y mostramos que su contribución es pequeña en cierto régimen.

La misma frase coloquial ---«despreciamos el aire»--- puede esconder operaciones conceptuales diferentes.

[]{#paso-5-reemplazar-una-relación-angular-por-una-relación-más-simple-para-ángulos-pequeños}

#### 1.4.11.5. Paso 5 --- Reemplazar una relación angular por una relación más simple para ángulos pequeños {#fispm-c01-paso-5-reemplazar-una-relaciuxf3n-angular-por-una-relaciuxf3n-muxe1s-simple-para-uxe1ngulos-pequeuxf1os}

**Tipo:** aproximación.

No la utilizaremos todavía. La estudiaremos de manera controlada en el capítulo 6. Esta escalera muestra por qué no basta escribir «hacemos las aproximaciones usuales».

### 1.4.12. La etiqueta `[``MOD``]` y la etiqueta `[``APPROX``]` {#fispm-c01-la-etiqueta-mod-y-la-etiqueta-approx}

El protocolo global de este libro distingue:

$$[\mathrm{MOD}]$$ para una hipótesis de modelización o idealización, y

$$[\mathrm{APPROX}]$$ para una aproximación.

Ejemplo:

$$[\mathrm{MOD}] \qquad \text{El hilo se considera inextensible.}$$ Esto define una propiedad exacta **del modelo**.

En cambio:

Aquí existe una diferencia explícita entre dos expresiones.

### 1.4.13. Una aproximación debe tener régimen {#fispm-c01-una-aproximaciuxf3n-debe-tener-ruxe9gimen}

La expresión

$$1-2\varepsilon+\varepsilon^2 \approx 1-2\varepsilon$$ no es una identidad.

Para

$$\varepsilon=0.01$$ el término omitido es

$$10^{-4}.$$ Para

$$\varepsilon=1$$ el término omitido es

$$1.$$ La misma sustitución puede ser excelente en un caso y desastrosa en otro.

Por eso toda aproximación física seria viene acompañada, explícita o implícitamente, por un **régimen de validez**.

**Definición operativa 1.16 --- Régimen de validez de una aproximación** El **régimen de validez** de una aproximación es el conjunto de condiciones bajo las cuales el error o los efectos omitidos permanecen suficientemente pequeños para el propósito declarado.

Todavía no sabemos formular regímenes de manera sistemática.

Eso será tarea del capítulo 6.

### 1.4.14. «Suficientemente pequeño» depende de la pregunta {#fispm-c01-suficientemente-pequeuxf1o-depende-de-la-pregunta}

Imaginemos dos usos de una misma predicción.

[]{#uso-a-demostración-de-aula}

#### 1.4.14.1. Uso A --- Demostración de aula {#fispm-c01-uso-a-demostraciuxf3n-de-aula}

Queremos distinguir si un tiempo es aproximadamente de uno o de diez segundos. Un error de unas pocas centésimas puede ser irrelevante.

[]{#uso-b-instrumento-de-precisión}

#### 1.4.14.2. Uso B --- Instrumento de precisión {#fispm-c01-uso-b-instrumento-de-precisiuxf3n}

Queremos detectar una variación relativa de una parte en cien mil. El mismo error puede arruinar completamente el experimento.

Por tanto:

$$\boxed{ \text{validez práctica} = \text{error} + \text{precisión requerida} + \text{pregunta}. }$$ No existe una tolerancia universal para todas las aplicaciones.

### 1.4.15. El peligro contrario: aproximar demasiado pronto {#fispm-c01-el-peligro-contrario-aproximar-demasiado-pronto}

Las aproximaciones son útiles, pero pueden destruir precisamente el fenómeno que queremos estudiar.

Supongamos que dos términos pequeños casi se cancelan y el resultado observable depende de su diferencia. Si eliminamos uno de ellos por considerarlo «pequeño» de manera aislada, podemos cambiar por completo la respuesta. O supongamos que una cantidad pequeña actúa durante muchísimo tiempo y su efecto acumulado se vuelve importante.

Por tanto:

$$\boxed{ \text{término pequeño} \not\Rightarrow \text{efecto siempre despreciable}. }$$ Necesitamos conocer cómo entra ese término en la estructura completa del problema.

### 1.4.16. Ejemplo: la rotación terrestre en un péndulo {#fispm-c01-ejemplo-la-rotaciuxf3n-terrestre-en-un-puxe9ndulo}

Durante unas pocas oscilaciones ordinarias, ciertos efectos asociados con la rotación terrestre pueden resultar irrelevantes para una pregunta elemental sobre el período. Pero si preguntamos por una modificación lenta del plano de oscilación durante muchas horas, precisamente esos efectos pueden convertirse en el fenómeno central.

Lo que parecía una corrección pequeña deja de ser despreciable porque:

1.  cambia la pregunta;

2.  cambia la escala temporal;

3.  cambia la precisión buscada.

Esta observación preparará nuestros estudios de sistemas no inerciales mucho más adelante.

### 1.4.17. Modelo mínimo suficiente {#fispm-c01-modelo-muxednimo-suficiente}

Podemos formular una regla de trabajo:

**Principio 1.9 --- Modelo mínimo suficiente** Entre modelos que responden adecuadamente una pregunta con la precisión exigida, preferiremos inicialmente aquel que haga explícita la menor cantidad de estructura necesaria para comprender qué produce el resultado.

No es una ley universal de la ciencia. Es una estrategia pedagógica y metodológica. Un modelo más rico se justifica cuando el modelo mínimo deja de responder la pregunta o cuando buscamos fenómenos nuevos.

### 1.4.18. Ejemplo desarrollado 9 --- Clasificar una simplificación {#fispm-c01-ejemplo-desarrollado-9-clasificar-una-simplificaciuxf3n}

Consideremos cuatro frases.

[]{#a}

#### 1.4.18.1. A {#fispm-c01-a}

«No registraremos el color del proyectil.»

**Clasificación:** abstracción.

No se introduce la afirmación «el proyectil carece de color». El color queda fuera del lenguaje del modelo.

[]{#b}

#### 1.4.18.2. B {#fispm-c01-b}

«El proyectil se tratará como una partícula puntual.»

**Clasificación:** idealización.

Se sustituye el cuerpo extendido por un objeto de extensión nula.

[]{#c}

#### 1.4.18.3. C {#fispm-c01-c}

«La resistencia del aire se toma exactamente igual a cero.»

**Clasificación:** idealización de modelo.

[]{#d}

#### 1.4.18.4. D {#fispm-c01-d}

«La resistencia del aire produce una corrección menor que la precisión que buscamos y por eso omitiremos su contribución.»

**Clasificación:** aproximación, siempre que exista una comparación que justifique la afirmación.

Las frases C y D pueden conducir a ecuaciones semejantes, pero su **estatus epistemológico** es diferente.

### 1.4.19. Ejemplo desarrollado 10 --- El término cuadrático {#fispm-c01-ejemplo-desarrollado-10-el-tuxe9rmino-cuadruxe1tico}

Sea

$$Q(\varepsilon)=1-2\varepsilon+\varepsilon^2.$$ Queremos sustituirlo por

$$Q_1(\varepsilon)=1-2\varepsilon.$$

#### 1.4.19.1. Paso 1 --- Diferencia exacta {#fispm-c01-paso-1-diferencia-exacta}

$$Q(\varepsilon)-Q_1(\varepsilon) = \varepsilon^2.$$

#### 1.4.19.2. Paso 2 --- Comparación con el término lineal {#fispm-c01-paso-2-comparaciuxf3n-con-el-tuxe9rmino-lineal}

Para $\varepsilon\neq0$,

$$\frac{|\varepsilon^2|}{|2\varepsilon|} = \frac{|\varepsilon|}{2}.$$

#### 1.4.19.3. Paso 3 --- Casos {#fispm-c01-paso-3-casos}

Si

$$|\varepsilon|=10^{-2},$$ entonces

$$\frac{|\varepsilon^2|}{|2\varepsilon|} = 5\times10^{-3}.$$ Si

$$|\varepsilon|=1,$$ entonces

$$\frac{|\varepsilon^2|}{|2\varepsilon|} = \frac12.$$ La omisión que era pequeña en el primer caso ya no lo es en el segundo.

[]{#conclusión}

#### 1.4.19.4. Conclusión {#fispm-c01-conclusiuxf3n}

No existe «la aproximación» sin su régimen.

### 1.4.20. Ejercicios de §4 {#fispm-c01-ejercicios-de-4}

[]{#fispm-t1-c01-e0015}

**Ejercicio 1.15 --- Idealización no es aproximación.**

Clasifica cada operación como **abstracción**, **idealización** o **aproximación** y justifica.

1.  No incluir el color de una esfera entre las variables del modelo.\

2.  Tratar la esfera como partícula puntual.\

3.  Reemplazar $1+\varepsilon+\varepsilon^2$ por $1+\varepsilon$ para $|\varepsilon|$ pequeño.\

4.  Tratar una barra como perfectamente rígida.\

5.  No distinguir químicamente dos cuerpos porque la pregunta solo utiliza su masa y posición.

**Solución.**

1.  **Abstracción.** El color queda fuera de la descripción; no se afirma que sea cero o inexistente.

2.  **Idealización.** Un cuerpo extendido se sustituye por un punto.

3.  **Aproximación.** Se reemplaza una expresión por otra cercana bajo una condición de pequeñez.

4.  **Idealización.** La rigidez perfecta se trata como exacta en el modelo aunque ningún material real la posea exactamente.

5.  **Abstracción.** Se conserva solo la estructura relevante para la pregunta y se omite la composición química.

[]{#fispm-t1-c01-e0016}

La clave es preguntar qué operación se realiza sobre la representación. **Ejercicio 1.16 --- Escalera del péndulo.**

Ordena conceptualmente los siguientes pasos y clasifica cada uno:

1.  cuerpo real + hilo real + aire + Tierra;

2.  no registrar el color de la esfera;

3.  representar la esfera como masa puntual;

4.  tratar el hilo como inextensible y sin masa;

5.  tomar la disipación exactamente nula;

6.  más adelante, reemplazar una relación exacta por otra válida para pequeñas oscilaciones.

Explica qué información o efecto se pierde en cada paso.

**Solución.**

Un orden razonable es:

$$1\to2\to3\to4\to5\to6.$$ **1 → 2:** abstracción. Se elimina de la descripción una propiedad que no se considera relevante.

**2 → 3:** idealización. Se pierde tamaño, forma y estructura interna.

**3 → 4:** idealización. Se eliminan masa y extensibilidad del hilo.

**4 → 5:** idealización. El modelo declara exactamente ausente la disipación.

**5 → 6:** aproximación. Una relación del modelo se reemplaza por otra más simple dentro de un régimen que deberá justificarse.

[]{#fispm-t1-c01-e0017}

El ejercicio muestra que varias simplificaciones pueden acumularse y que cada una tiene una justificación diferente. **Ejercicio 1.17 --- Más complicado no es siempre mejor.**

Un equipo quiere estimar el tiempo aproximado que tarda una pelota en caer desde una altura moderada. El **Modelo A** utiliza pocas propiedades macroscópicas. El **Modelo B** añade cuarenta parámetros: composición microscópica, distribución térmica interna, rugosidad detallada, pequeñas vibraciones y muchas propiedades adicionales que el equipo no puede medir con precisión.

Explica por qué no se sigue que B sea mejor que A. Indica qué evidencia justificaría pasar de A a B o a un modelo intermedio.

**Solución.**

El número de detalles no establece por sí solo la calidad del modelo.

B puede resultar peor porque:

- contiene parámetros desconocidos;

- aumenta la incertidumbre de las entradas;

- dificulta identificar qué mecanismo controla el resultado;

- puede no mejorar la predicción a la escala requerida;

- puede ser imposible de contrastar con los datos disponibles.

A puede ser preferible si responde la pregunta dentro de la precisión necesaria.

Pasar a un modelo más rico se justificaría si observamos, por ejemplo:

1.  discrepancias sistemáticas mayores que la precisión requerida;

2.  dependencia del resultado respecto de una propiedad omitida;

3.  un nuevo experimento que necesite explicar estructura que A no representa;

4.  necesidad de mayor precisión.

El criterio es **suficiencia para la pregunta**, no cantidad de detalles.

### 1.4.21. Síntesis {#fispm-c01-suxedntesis-1}

Ahora podemos distinguir tres maneras de simplificar.

$$\boxed{ \text{abstracción} = \text{seleccionar estructura y omitir particulares} }$$ $$\boxed{ \text{idealización} = \text{tratar como exacta una condición simplificada del modelo} }$$ $$\boxed{ \text{aproximación} = \text{reemplazar por algo cercano en un régimen controlado} }$$ Y podemos asociar una pregunta de auditoría a cada una:

$$\begin{array}{c|c} \text{operación} & \text{pregunta}\\ \hline \text{abstracción} & \text{¿qué información se omite?}\\ \text{idealización} & \text{¿qué se declara exacto solo en el modelo?}\\ \text{aproximación} & \text{¿qué error se acepta y en qué régimen?} \end{array}$$ La siguiente sección dará un paso más.

Hasta ahora hemos hablado de sistemas, estados, variables y simplificaciones.

Debemos reunir todo eso en una plantilla matemática suficientemente precisa para leer un modelo sin confundir el formalismo con su interpretación.

Entraremos entonces en el §[1.5](#fispm-c01-de-la-representaciuxf3n-fuxedsica-al-objeto-matemuxe1tico).

[]{#de-la-representación-física-al-objeto-matemático}

[]{#fispm-t1-c01-s05}

[]{#fpm-i-01-s05}

## 1.5. De la representación física al objeto matemático {#fispm-c01-de-la-representaciuxf3n-fuxedsica-al-objeto-matemuxe1tico}

[]{#el-símbolo-no-trae-consigo-su-significado-físico}

### 1.5.1. El símbolo no trae consigo su significado físico {#fispm-c01-el-suxedmbolo-no-trae-consigo-su-significado-fuxedsico}

Supongamos que encontramos escrita la ecuación $x^2+y^2=L^2.$

Como objeto matemático, podemos estudiarla sin saber nada de física. Podemos preguntar por sus soluciones, despejar una variable o reconocer una estructura geométrica. Pero ninguna de esas operaciones nos dice por sí sola qué representan $x$, $y$ y $L$.

[]{#fig:I-01-N02}

![**Figura 1.4.** La aplicación de observación vincula el estado matemático con una cantidad medible. Un mismo observable puede tomar igual valor en estados distintos. Véase §[1.5](#fispm-c01-de-la-representaciuxf3n-fuxedsica-al-objeto-matemuxe1tico).](/assets/books/fispm/v04/I-01-N02.svg "fig:"){.fpm-v04-figure fig-alt="Estado y medición" width="390px" fig-cap=""}

La misma ecuación podría aparecer para describir una restricción geométrica, una trayectoria idealizada, dos componentes de una cantidad, una relación entre magnitudes reescaladas o un problema puramente matemático sin interpretación física. La sintaxis no determina la semántica.

$$\boxed{ \text{expresión matemática} + \text{interpretación física} = \text{enunciado físico modelado} }$$

Este es el punto de partida de la sección. Un matemático puede manipular correctamente una expresión y, sin embargo, no saber todavía qué pregunta física está respondiendo.

[]{#dos-tareas-diferentes}

### 1.5.2. Dos tareas diferentes {#fispm-c01-dos-tareas-diferentes}

Cuando construimos un modelo físico realizamos al menos dos tareas.

[]{#tarea-matemática}

#### 1.5.2.1. Tarea matemática {#fispm-c01-tarea-matemuxe1tica}

Elegimos objetos como conjuntos, números, funciones, relaciones, espacios, ecuaciones y parámetros.

[]{#tarea-física}

#### 1.5.2.2. Tarea física {#fispm-c01-tarea-fuxedsica}

Decidimos qué sistema representa cada objeto, qué magnitud corresponde a cada símbolo, qué procedimientos conectan ciertos símbolos con observaciones, qué hipótesis permiten usar esas relaciones y en qué régimen esperamos que el modelo sea adecuado. Estas tareas se necesitan mutuamente, pero no son idénticas.

La matemática organiza la estructura. La física asigna significado y la conecta con el mundo.

**Principio 1.10 --- Ningún símbolo físico se interpreta a sí mismo** El significado físico de un objeto matemático debe declararse mediante el modelo, una definición, una regla de observación o una convención explícita; no puede deducirse únicamente de la forma del símbolo o de la ecuación en la que aparece.

[]{#el-diccionario-de-interpretación}

### 1.5.3. El diccionario de interpretación {#fispm-c01-el-diccionario-de-interpretaciuxf3n}

Usaremos la expresión **diccionario de interpretación** para referirnos al conjunto de correspondencias que explican cómo leer físicamente el formalismo.

Por ejemplo, un modelo podría declarar:

$$x \longleftrightarrow \text{posición de una marca del sistema respecto de un origen especificado}.$$

Esto todavía no dice cómo se mide $x$.

Una regla adicional podría especificar:

$$[\mathrm{OBS}] \qquad x \longleftrightarrow \text{\parbox{.66\linewidth}{\centering valor obtenido al convertir una coordenada de imagen mediante una calibración}}.$$

La primera correspondencia otorga significado físico al símbolo. La segunda lo conecta con un procedimiento de observación.

**Definición operativa 1.17 --- Diccionario de interpretación** El **diccionario de interpretación** de un modelo es el conjunto de correspondencias, convenciones y reglas que asignan significado físico a sus objetos matemáticos y, cuando corresponde, los conectan con procedimientos de observación.

No debemos imaginar necesariamente este diccionario como una única función matemática bien definida. Es una estructura semántica que puede incluir definiciones, convenciones, calibraciones, identificaciones, reglas experimentales y elecciones de sistema de referencia.

[]{#representar-no-significa-copiar}

### 1.5.4. Representar no significa copiar {#fispm-c01-representar-no-significa-copiar}

Una representación matemática no es una réplica del sistema físico. El número

$$2.3$$

no posee masa, temperatura ni ubicación espacial. Una función no «es» una cuerda. Un punto no «es» una partícula material. Lo que hacemos es establecer una correspondencia útil entre aspectos del sistema y estructuras matemáticas.

Por eso conviene evitar frases como:

> «La partícula es el punto $P$.»

Es más preciso decir:

> «En este modelo, la posición de la partícula se representa mediante el punto $P$.»

La diferencia verbal protege una diferencia conceptual:

$$\boxed{ \text{objeto físico} \neq \text{objeto matemático que lo representa}. }$$

[]{#una-representación-puede-perder-información}

### 1.5.5. Una representación puede perder información {#fispm-c01-una-representaciuxf3n-puede-perder-informaciuxf3n}

En §4 vimos que toda abstracción puede omitir estructura. La representación matemática hereda esa selección. Si modelamos un cuerpo por un punto,

$$\text{cuerpo extendido} \longrightarrow P,$$

ya no podemos recuperar del punto la forma del cuerpo, su orientación, su distribución interna, su color o su textura. La representación es deliberadamente no invertible. Esto no es un defecto accidental. Es parte del propósito del modelo.

Una representación útil puede olvidar precisamente aquello que no necesitamos.

[]{#una-representación-puede-introducir-estructura-adicional}

### 1.5.6. Una representación puede introducir estructura adicional {#fispm-c01-una-representaciuxf3n-puede-introducir-estructura-adicional}

También puede ocurrir lo contrario. Al elegir coordenadas, bases, parámetros o variables auxiliares podemos introducir estructura matemática que no corresponde directamente a una propiedad física independiente. Por ejemplo, dos descripciones matemáticas distintas pueden representar la misma situación física.

Más adelante veremos esto con gran profundidad: distintos sistemas de coordenadas, distintas bases, transformaciones de referencia y, mucho más adelante, representaciones matemáticas diferentes que conservan los mismos observables físicos.

Por ahora fijamos una advertencia:

$$\boxed{ \text{diferencia entre descripciones matemáticas} \not\Rightarrow \text{diferencia física}. }$$

La cuestión «¿qué parte del formalismo representa algo físicamente distinguible?» será recurrente.

[]{#una-plantilla-mínima-de-lectura}

### 1.5.7. Una plantilla mínima de lectura {#fispm-c01-una-plantilla-muxednima-de-lectura}

Necesitamos ahora una manera compacta de preguntar qué contiene un modelo.

Introduciremos la notación

$$\boxed{ \mathcal M = (\mathcal S,\,X,\,\theta,\,\mathcal L,\,I,\,B,\,\mathcal R) }$$

como **plantilla provisional de lectura**.

No es una definición axiomática universal de «modelo físico».

No afirmamos que toda teoría física pueda o deba reducirse literalmente a una séptupla de esta forma. La notación funciona como una lista de control. Nos obliga a preguntar si hemos especificado los componentes necesarios para comprender un problema.

[]{#mathcal-s-estados-admitidos}

### 1.5.8. $\mathcal S$: estados admitidos {#fispm-c01-mathcal-s-estados-admitidos}

Ya introdujimos el espacio de estados en §3.

Aquí lo situamos dentro de la plantilla:

$$\mathcal S = \{\text{estados admitidos por el modelo}\}.$$

El adjetivo **admitidos** importa. Un modelo no tiene por qué permitir toda asignación imaginable de números a sus variables. Puede haber restricciones.

Si dos variables $x$ e $y$ deben satisfacer

$$x^2+y^2=L^2,$$

entonces el estado

$$(x,y)=(0,0)$$

no es admisible cuando $L\neq0$. Por tanto, especificar variables no basta. Debemos especificar qué combinaciones representan estados físicamente permitidos **dentro del modelo**.

[]{#x-variables-y-observables-modelados}

### 1.5.9. $X$: variables y observables modelados {#fispm-c01-x-variables-y-observables-modelados}

Usaremos $X$ como símbolo colectivo para la familia de cantidades que el modelo emplea para describir o interrogar el sistema. Puede incluir variables de estado, observables, variables de control y cantidades derivadas. No exigiremos que todos estos objetos tengan la misma estructura matemática.

En un modelo elemental, un observable puede ser una función

$$O:\mathcal S\to V.$$

En teorías posteriores esta representación tendrá que modificarse. Por eso $X$ no es una «lista universal de coordenadas». Es un contenedor conceptual para las cantidades relevantes del modelo.

[]{#theta-parámetros}

### 1.5.10. $\theta$: parámetros {#fispm-c01-theta-paruxe1metros}

Escribiremos esquemáticamente

$$\theta=(\theta_1,\ldots,\theta_k)$$

para reunir parámetros. Por ejemplo, distintos miembros de una familia de modelos pueden diferir en una longitud, una masa, una constante de acoplamiento o una propiedad material. La plantilla distingue

$$s\in\mathcal S$$

como estado de una realización, de

$$\theta$$

como parámetros que caracterizan la familia o que se consideran fijos durante el problema. Pero recordemos §3: la misma magnitud puede cambiar de papel en otro modelo.

[]{#mathcal-l-leyes-y-relaciones-del-modelo}

### 1.5.11. $\mathcal L$: leyes y relaciones del modelo {#fispm-c01-mathcal-l-leyes-y-relaciones-del-modelo}

El símbolo

$$\mathcal L$$

reunirá las relaciones que el modelo utiliza para vincular estados, variables y parámetros.

Todavía no definiremos formalmente qué diferencia una **ley**, un **principio**, un **postulado** o una **ecuación constitutiva**. Eso corresponde a §§6--7.

Por ahora basta advertir que $\mathcal L$ puede contener relaciones de estatus muy distinto. Una relación puede ser empírica, postulada, definitoria o derivada matemáticamente de otras. Por eso nunca debemos leer

$$\mathcal L=\{\text{ecuaciones}\}$$

como si todas las ecuaciones tuvieran el mismo origen epistemológico. La sección siguiente desarrollará precisamente este problema.

[]{#i-condiciones-iniciales}

### 1.5.12. $I$: condiciones iniciales {#fispm-c01-i-condiciones-iniciales}

Muchos modelos dinámicos necesitan especificar una condición del sistema en un instante elegido como inicial. Representaremos ese bloque mediante

$$I.$$

La etiqueta canónica será $[\mathrm{IC}].$ Pero no toda condición inicial es una ley. Si escribimos

$$x(0)=a,$$

la forma algebraica no nos dice si se trata de un dato experimental, una elección de ejemplo, una condición impuesta o una consecuencia de otra relación. La expresión se vuelve condición inicial por el papel que cumple en el problema. No desarrollaremos todavía teoría de problemas de valor inicial. Solo fijamos el casillero conceptual.

[]{#b-condiciones-de-frontera}

### 1.5.13. $B$: condiciones de frontera {#fispm-c01-b-condiciones-de-frontera}

En problemas extendidos espacialmente puede ser necesario especificar qué ocurre en una frontera.

Representaremos esas condiciones por

$$B.$$

La etiqueta canónica será $[\mathrm{BC}].$

Ejemplos conceptuales posteriores incluirán preguntas como: ¿los extremos están fijos?, ¿qué valor se prescribe en la superficie?, ¿puede atravesar algo la frontera?, ¿qué ocurre en la interfaz entre dos medios?

No necesitamos todavía resolver ninguna ecuación con estas condiciones. El punto es comprender que

$$\boxed{ \text{ley} + \text{condiciones} }$$

suele contener más información que la ley aislada.

[]{#mathcal-r-régimen-de-validez}

### 1.5.14. $\mathcal R$: régimen de validez {#fispm-c01-mathcal-r-ruxe9gimen-de-validez}

El componente

$$\mathcal R$$

recoge las condiciones bajo las cuales esperamos que el modelo represente adecuadamente el fenómeno para la pregunta planteada. Puede incluir restricciones sobre escalas, velocidades, amplitudes, intensidades, tiempos, precisión o propiedades del medio. En §4 introdujimos el concepto cualitativamente. En el capítulo 6 aprenderemos a formular muchos regímenes cuantitativamente.

Por ahora queremos que ningún modelo aparezca como si afirmara:

> «Esta descripción vale para todo sistema, en toda escala y con precisión ilimitada.»

[]{#la-tupla-no-contiene-todavía-toda-la-semántica}

### 1.5.15. La tupla no contiene todavía toda la semántica {#fispm-c01-la-tupla-no-contiene-todavuxeda-toda-la-semuxe1ntica}

La plantilla

$$\mathcal M = (\mathcal S,X,\theta,\mathcal L,I,B,\mathcal R)$$

es útil, pero sería un error pensar que ya hemos capturado toda la física.

Falta algo esencial:

$$\boxed{\text{¿qué significa cada componente?}}$$

Por eso la tupla debe viajar acompañada de un diccionario de interpretación

$$\mathfrak I_{\mathcal M}.$$

Usaremos esta notación de manera informal:

$$\mathfrak I_{\mathcal M} = \{\text{significados físicos y reglas de conexión asociados a }\mathcal M\}.$$

Así, la unidad mínima de lectura será más bien

$$\boxed{ (\mathcal M,\mathfrak I_{\mathcal M}) }$$

y no la tupla matemática desnuda.

Esto incorpora una consecuencia de §2: una teoría física necesita conexiones con observaciones, no solo ecuaciones.

[]{#un-modelo-puede-estar-incompleto}

### 1.5.16. Un modelo puede estar incompleto {#fispm-c01-un-modelo-puede-estar-incompleto}

También debemos distinguir

$$\text{componente innecesario}$$

de

$$\text{componente necesario pero todavía no especificado}.$$

Supongamos que queremos predecir la evolución de un sistema y conocemos su espacio de estados y parámetros, pero no hemos declarado ninguna ley dinámica. Entonces el modelo está incompleto para esa pregunta. De manera semejante, una ecuación dinámica puede estar especificada pero las condiciones iniciales necesarias pueden faltar.

**Principio 1.11 --- La suficiencia de un modelo depende de la tarea** Un conjunto de objetos matemáticos constituye una descripción suficiente solo si contiene la información necesaria para responder la pregunta física planteada; que una fórmula sea correcta no implica que el problema esté completamente especificado.

[]{#ejemplo-desarrollado-11-un-sistema-físico-de-dos-estados}

### 1.5.17. Ejemplo desarrollado 11 --- Un sistema físico de dos estados {#fispm-c01-ejemplo-desarrollado-11-un-sistema-fuxedsico-de-dos-estados}

Construyamos un modelo deliberadamente sencillo.

Tenemos un dispositivo idealizado que puede estar en dos configuraciones distinguibles:

$$\text{cerrado},\qquad \text{abierto}.$$

Representamos los estados mediante $\mathcal S=\{0,1\},$

con el diccionario

$$0\longleftrightarrow\text{cerrado}, \qquad 1\longleftrightarrow\text{abierto}.$$

Definimos un observable

$$O:\mathcal S\to\{0,1\}, \qquad O(s)=s.$$

La fórmula es trivial. La física no está en la dificultad algebraica. Está en declarar qué diferencia física corresponde a $0$ y $1$, cómo determinamos experimentalmente si el dispositivo está abierto o cerrado, qué estados intermedios hemos excluido por idealización y para qué pregunta esa idealización es adecuada.

La estructura

$$\{0,1\}$$

puede modelar innumerables sistemas distintos. El conjunto por sí solo no especifica cuál.

[]{#ejemplo-desarrollado-12-esqueleto-del-modelo-del-péndulo}

### 1.5.18. Ejemplo desarrollado 12 --- Esqueleto del modelo del péndulo {#fispm-c01-ejemplo-desarrollado-12-esqueleto-del-modelo-del-puxe9ndulo}

Volvamos al péndulo, pero sin escribir todavía su ecuación de movimiento.

Podemos preparar una ficha.

[]{#sistema-físico}

#### 1.5.18.1. Sistema físico {#fispm-c01-sistema-fuxedsico}

Una pequeña esfera suspendida mediante un hilo.

[]{#mathcal-s}

#### 1.5.18.2. $\mathcal S$ {#fispm-c01-mathcal-s}

Estados admitidos por la idealización elegida.

No los parametrizaremos técnicamente todavía.

[]{#x}

#### 1.5.18.3. $X$ {#fispm-c01-x}

Cantidades que deseamos representar, por ejemplo la posición angular, información sobre el movimiento y el tiempo de oscilación como observable derivado. Las definiciones precisas se darán en capítulos posteriores.

[]{#theta}

#### 1.5.18.4. $\theta$ {#fispm-c01-theta}

Parámetros como la longitud del hilo y otras propiedades que el modelo trate como fijas.

[]{#mathcal-l}

#### 1.5.18.5. $\mathcal L$ {#fispm-c01-mathcal-l}

Todavía no especificado. La ley dinámica aparecerá después de desarrollar la mecánica necesaria.

[]{#i}

#### 1.5.18.6. $I$ {#fispm-c01-i}

Condición inicial: cómo se prepara el péndulo al comenzar el experimento.

[]{#b-1}

#### 1.5.18.7. $B$ {#fispm-c01-b-1}

No necesitamos aquí una condición de frontera espacial independiente.

[]{#mathcal-r}

#### 1.5.18.8. $\mathcal R$ {#fispm-c01-mathcal-r}

Régimen en el cual las idealizaciones adoptadas sean adecuadas.

[]{#mathfrak-i_mathcal-m}

#### 1.5.18.9. $\mathfrak I_{\mathcal M}$ {#fispm-c01-mathfrak-i_mathcal-m}

Reglas que explican qué representa la posición angular, cómo se identifica experimentalmente una oscilación y cómo se mide el tiempo correspondiente. La ficha es útil precisamente porque muestra qué sabemos y qué **todavía falta**.

[]{#ejemplo-desarrollado-13-una-ecuación-dos-modelos}

### 1.5.19. Ejemplo desarrollado 13 --- Una ecuación, dos modelos {#fispm-c01-ejemplo-desarrollado-13-una-ecuaciuxf3n-dos-modelos}

Consideremos

$$x+y=1.$$

[]{#modelo-a-dos-fracciones-de-composición}

#### 1.5.19.1. Modelo A --- Dos fracciones de composición {#fispm-c01-modelo-a-dos-fracciones-de-composiciuxf3n}

Interpretamos

$$x=\text{fracción del componente A},$$

$$y=\text{fracción del componente B}.$$

La ecuación expresa que el modelo solo admite esos dos componentes y que las fracciones están normalizadas.

[]{#modelo-b-distribución-idealizada-de-un-recurso}

#### 1.5.19.2. Modelo B --- Distribución idealizada de un recurso {#fispm-c01-modelo-b-distribuciuxf3n-idealizada-de-un-recurso}

Interpretamos

$$x=\text{fracción asignada al subsistema 1},$$

$$y=\text{fracción asignada al subsistema 2}.$$

La misma ecuación posee otra semántica.

Matemáticamente, $x+y=1$

es idéntica.

Físicamente, los modelos son diferentes porque cambia

$$\mathfrak I_{\mathcal M}.$$

Por tanto,

$$\boxed{ \text{misma estructura matemática} \not\Rightarrow \text{mismo modelo físico}. }$$

**Ejercicio de §5.**

[]{#fispm-t1-c01-e0018}

**Ejercicio 1.18 --- Construir la ficha matemática mínima de un modelo.**

Considera un depósito idealizado que solo puede registrarse como **vacío** o **lleno** mediante un sensor binario. Construye una ficha mínima utilizando

$$\mathcal M=(\mathcal S,X,\theta,\mathcal L,I,B,\mathcal R)$$

y un diccionario $\mathfrak I_{\mathcal M}$.

No es necesario inventar una ley dinámica si la pregunta solo es:

> «¿Qué estado registra el sensor en el instante de observación?»

Explica también qué información física real elimina este modelo.

**Solución.**

Una ficha posible es la siguiente.

[]{#sistema-físico-1}

#### 1.5.19.3. Sistema físico {#fispm-c01-sistema-fuxedsico-1}

El depósito y el mecanismo relevante para decidir si el sensor lo clasifica como vacío o lleno.

[]{#pregunta-6}

#### 1.5.19.4. Pregunta {#fispm-c01-pregunta-6}

Determinar cuál de los dos estados registra el sensor.

[]{#espacio-de-estados}

#### 1.5.19.5. Espacio de estados {#fispm-c01-espacio-de-estados}

$$\mathcal S=\{0,1\}.$$

[]{#diccionario-de-estados}

#### 1.5.19.6. Diccionario de estados {#fispm-c01-diccionario-de-estados}

$$0\longleftrightarrow \text{vacío según el criterio del sensor},$$

$$1\longleftrightarrow \text{lleno según el criterio del sensor}.$$

Es importante añadir «según el criterio del sensor»: un depósito real puede contener cantidades intermedias.

[]{#variablesobservables}

#### 1.5.19.7. Variables/observables {#fispm-c01-variablesobservables}

Podemos tomar

$$X=\{O\},$$

con

$$O:\mathcal S\to\{0,1\}, \qquad O(s)=s.$$

[]{#parámetros}

#### 1.5.19.8. Parámetros {#fispm-c01-paruxe1metros}

Si el sensor utiliza un umbral fijo para decidir la clasificación, ese umbral puede formar parte de

$$\theta.$$

No necesitamos asignarle un valor numérico concreto.

[]{#leyes-o-relaciones}

#### 1.5.19.9. Leyes o relaciones {#fispm-c01-leyes-o-relaciones}

Para la pregunta instantánea no necesitamos especificar una ley dinámica. Por tanto, $\mathcal L$ puede quedar sin componente dinámico relevante para esta tarea. Esto no significa que el depósito real carezca de dinámica.

[]{#condición-inicial}

#### 1.5.19.10. Condición inicial {#fispm-c01-condiciuxf3n-inicial}

No es necesaria si solo preguntamos por el estado registrado en el instante actual.

[]{#condiciones-de-frontera}

#### 1.5.19.11. Condiciones de frontera {#fispm-c01-condiciones-de-frontera}

No se requieren para este modelo binario elemental.

[]{#régimen-de-validez}

#### 1.5.19.12. Régimen de validez {#fispm-c01-ruxe9gimen-de-validez}

El modelo sirve únicamente para preguntas cuya respuesta dependa de la clasificación binaria y no de la cantidad exacta de contenido.

[]{#diccionario-de-interpretación}

#### 1.5.19.13. Diccionario de interpretación {#fispm-c01-diccionario-de-interpretaciuxf3n}

$\mathfrak I_{\mathcal M}$ debe incluir qué significa «vacío», qué significa «lleno», cómo funciona la regla de clasificación del sensor y qué señal corresponde a $0$ y cuál a $1$.

[]{#información-omitida}

#### 1.5.19.14. Información omitida {#fispm-c01-informaciuxf3n-omitida}

El modelo elimina, entre otras cosas, todos los niveles intermedios, la forma de la superficie del contenido, temperatura, presión, composición y la dinámica de llenado o vaciado.

La conclusión metodológica es importante:

$$\boxed{ \text{\parbox{.66\linewidth}{\centering un modelo puede ser suficiente para una pregunta aunque omita casi toda la física del sistema}}. }$$

La suficiencia depende de la tarea.

### 1.5.20. Síntesis {#fispm-c01-suxedntesis-2}

Ya podemos distinguir cuatro niveles:

$$\boxed{\text{sistema físico}}$$

$$\boxed{ \text{núcleo formal } \mathcal M = (\mathcal S,X,\theta,\mathcal L,I,B,\mathcal R) }$$

$$\boxed{ \text{diccionario de interpretación } \mathfrak I_{\mathcal M} }$$

$$\boxed{\text{observaciones y contraste}}$$

La tupla organiza la matemática. El diccionario explica qué significa físicamente.

Las reglas `[``OBS``]` conectan parte de ese significado con procedimientos de observación. El régimen $\mathcal R$ recuerda que la representación no reclama validez ilimitada.

Por tanto, la fórmula central de esta sección no debe leerse como una axiomatización de la física, sino como una disciplina de lectura:

$$\boxed{ \text{\parbox{.66\linewidth}{\centering no preguntes solo «¿qué ecuación tengo?»; pregunta «¿qué modelo está representando esta ecuación?»}} }$$

Ahora podemos abordar el problema que hemos aplazado deliberadamente. Dentro de $\mathcal L$ aparecen ecuaciones de tipos muy diferentes. Algunas definen. Algunas resumen regularidades empíricas. Algunas expresan postulados. Algunas son hipótesis del modelo. Algunas son aproximaciones. Y otras se deducen matemáticamente.

La forma algebraica no permite distinguirlas.

Este será el objeto de (§[1.6](#fispm-c01-el-estatus-de-una-ecuaciuxf3n)).

[]{#el-estatus-de-una-ecuación}

[]{#fispm-t1-c01-s06}

[]{#fpm-i-01-s06}

## 1.6. El estatus de una ecuación {#fispm-c01-el-estatus-de-una-ecuaciuxf3n}

[]{#la-misma-fórmula-puede-cumplir-funciones-distintas}

### 1.6.1. La misma fórmula puede cumplir funciones distintas {#fispm-c01-la-misma-fuxf3rmula-puede-cumplir-funciones-distintas}

Consideremos la fórmula

$$y=kx.$$ Aislada en una página, es solo una relación matemática entre símbolos.

Pero dentro de distintos contextos puede desempeñar papeles muy diferentes.

[]{#contexto-a-definición}

#### 1.6.1.1. Contexto A --- Definición {#fispm-c01-contexto-a-definiciuxf3n}

Podemos decidir definir una nueva cantidad $y$ mediante

$$y:=kx.$$ Entonces la relación fija el significado de $y$.

Su estatus es:

$$[\mathrm{DEF}].$$

#### 1.6.1.2. Contexto B --- Regularidad empírica {#fispm-c01-contexto-b-regularidad-empuxedrica}

Podemos medir dos magnitudes $x$ e $y$ y descubrir que, dentro de cierto intervalo experimental,

$$y\approx kx.$$ Ahora la relación resume un patrón observado.

Su respaldo depende de datos. Su estatus puede ser: $[\mathrm{EMP}].$

#### 1.6.1.3. Contexto C --- Hipótesis de modelo {#fispm-c01-contexto-c-hipuxf3tesis-de-modelo}

Podemos construir deliberadamente un modelo en el que supongamos que dos cantidades obedecen exactamente

$$y=kx,$$ aunque sepamos que el sistema real solo se comporta así aproximadamente.

Entonces tenemos: $[\mathrm{MOD}].$

#### 1.6.1.4. Contexto D --- Consecuencia matemática {#fispm-c01-contexto-d-consecuencia-matemuxe1tica}

Podemos partir de premisas anteriores y demostrar algebraicamente que

$$y=kx.$$ Entonces la relación no introduce nuevo contenido físico.

Su estatus es:

$$[\mathrm{MATH}].$$ La forma algebraica es idéntica.

El estatus no.

$$\boxed{ \text{estatus físico} \not= \text{forma algebraica} }$$ Esta es la regla central de la sección. La cuestión decisiva no es la forma gráfica de la ecuación, sino su **procedencia y función dentro del argumento**. Por eso, al leer una derivación física, la primera pregunta será: «¿de dónde viene esta afirmación?».

**Definición operativa 1.18 --- Estatus de una afirmación** El **estatus** de una afirmación dentro de un modelo o teoría indica el papel epistemológico y lógico que cumple: si fija significado, resume evidencia empírica, introduce un postulado, especifica una idealización, declara una aproximación, fija condiciones, conecta con observaciones o se deduce matemáticamente de premisas ya aceptadas.

La palabra **dentro** es esencial. Una expresión puede cambiar de estatus cuando cambia el contexto. No clasificamos fórmulas por su aspecto, sino **afirmaciones situadas**.

### 1.6.2. Las nueve etiquetas canónicas {#fispm-c01-las-nueve-etiquetas-canuxf3nicas}

Usaremos las siguientes etiquetas:

  Etiqueta         Estatus                              Pregunta principal
  ---------------- ------------------------------------ -------------------------------------------------------------------
  `[``DEF``]`      definición                           ¿estamos fijando el significado de algo?
  `[``EMP``]`      ley o relación empírica              ¿su respaldo depende de observación o experimento?
  `[``POST``]`     postulado o principio físico         ¿se introduce como hipótesis estructural de la teoría?
  `[``MOD``]`      hipótesis de modelo / idealización   ¿qué rasgo del sistema real estamos sustituyendo o simplificando?
  `[``APPROX``]`   aproximación                         ¿qué diferencia o efecto despreciamos y en qué régimen?
  `[``IC``]`       condición inicial                    ¿qué se fija al comienzo del problema dinámico?
  `[``BC``]`       condición de frontera                ¿qué se prescribe en una frontera?
  `[``MATH``]`     consecuencia matemática              ¿se deduce sin introducir una nueva premisa física?
  `[``OBS``]`      relación de observación o medición   ¿cómo se conecta el formalismo con un procedimiento experimental?

No todas aparecerán en todos los problemas. Pero cuando una relación importante aparece por primera vez, el lector debe poder identificar su tipo. Las etiquetas forman un vocabulario de lectura. Conviene reunir aquí sus diferencias esenciales sin repetir nueve veces el mismo esquema.

[]{#def-emp-y-post}

#### 1.6.2.1. `[``DEF``]`, `[``EMP``]` y `[``POST``]` {#fispm-c01-def-emp-y-post}

Una definición fija significado. Por ejemplo, si dos instantes registrados son $t_i$ y $t_f$, podemos definir

$$[\mathrm{DEF}] \qquad \Delta t:=t_f-t_i.$$ No hemos descubierto experimentalmente que

$$\Delta t=t_f-t_i.$$ Hemos decidido usar el símbolo $\Delta t$ para esa diferencia.

La definición puede estar motivada físicamente, pero su verdad no se contrasta como una ley. Una vez aceptada, podemos usarla en deducciones.

[]{#pregunta-de-control}

##### Pregunta de control {#fispm-c01-pregunta-de-control}

> ¿la ecuación afirma algo sobre el comportamiento del mundo, o está fijando el significado de un símbolo? Una relación empírica obtiene su respaldo de observaciones o experimentos.

Esquemáticamente:

$$[\mathrm{EMP}] \qquad Y=f(X;\theta)$$ significa que la relación se acepta porque describe, dentro de cierto dominio, una regularidad del mundo físico.

No necesitamos todavía estudiar una ley concreta.

Lo importante es reconocer que:

$$\boxed{ \text{una ley empírica no se demuestra solo con álgebra} }$$ Podemos demostrar consecuencias **a partir** de ella.

Pero su conexión con la realidad requiere contraste.

[]{#pregunta-de-control-1}

##### Pregunta de control {#fispm-c01-pregunta-de-control-1}

> si ninguna observación del mundo pudiera contar a favor o en contra de esta relación, ¿seguiríamos llamándola empírica? Un postulado no es una simple abreviatura ni una observación aislada.

Es una hipótesis estructural que se adopta como parte de una teoría.

Podemos representarlo esquemáticamente:

$$[\mathrm{POST}] \qquad P.$$ Después podremos derivar consecuencias:

$$P\Longrightarrow Q.$$ Entonces $Q$ puede tener estatus `[``MATH``]` relativo al postulado $P$.

La teoría no «demuestra» $P$ usando sus propias consecuencias. Su justificación física proviene de la coherencia del marco, sus éxitos, su relación con experimentos y su integración con otras estructuras.

[]{#pregunta-de-control-2}

##### Pregunta de control {#fispm-c01-pregunta-de-control-2}

> ¿esta afirmación funciona como una premisa estructural del marco teórico?

#### 1.6.2.2. `[``MOD``]` y `[``APPROX``]` {#fispm-c01-mod-y-approx}

En §4 vimos ejemplos:

$$[\mathrm{MOD}] \qquad \text{«el cuerpo se trata como partícula puntual».}$$ o

$$[\mathrm{MOD}] \qquad \text{«el hilo se considera inextensible».}$$ Estas afirmaciones no pretenden ser literalmente verdaderas del objeto real.

Son exactas **dentro del modelo**.

Cada `[``MOD``]` debe permitir responder:

1.  ¿qué propiedad real se omite o idealiza?;

2.  ¿por qué creemos que no importa para la pregunta?;

3.  ¿qué observación podría mostrar que sí importa?

Esta es una de las reglas de auditoría más importantes de la obra. Una aproximación declara una sustitución:

$$A\approx B.$$ Pero el símbolo $\approx$ no constituye una justificación.

Debemos registrar, cuando sea posible:

- qué término o efecto se desprecia;

- qué cantidad controla su tamaño;

- respecto de qué escala es pequeño;

- cuándo esperamos que el reemplazo falle.

Por ejemplo:

$$[\mathrm{APPROX}] \qquad 1-2\varepsilon+\varepsilon^2 \approx 1-2\varepsilon$$ solo es informativo si añadimos un régimen en el que $|\varepsilon|$ sea suficientemente pequeño para la precisión buscada.

[]{#pregunta-de-control-3}

##### Pregunta de control {#fispm-c01-pregunta-de-control-3}

> ¿qué diferencia concreta estamos aceptando? Este es un punto especialmente delicado.

Supongamos que una ecuación final no contiene cierto efecto $D$.

Podemos llegar a ella de dos maneras:

[]{#ruta-a-idealización}

##### Ruta A --- Idealización {#fispm-c01-ruta-a-idealizaciuxf3n}

Declaramos:

$$[\mathrm{MOD}] \qquad D=0.$$ Dentro del modelo, el efecto es exactamente nulo.

[]{#ruta-b-aproximación}

##### Ruta B --- Aproximación {#fispm-c01-ruta-b-aproximaciuxf3n}

Partimos de

$$D\neq0$$ pero mostramos que, en el régimen estudiado,

$$|D| \ll \text{escala relevante},$$ y entonces escribimos

$$[\mathrm{APPROX}] \qquad D\approx0.$$ La ecuación simplificada puede ser la misma.

El razonamiento físico no.

#### 1.6.2.3. `[``IC``]`, `[``BC``]`, `[``MATH``]` y `[``OBS``]` {#fispm-c01-ic-bc-math-y-obs}

Una condición inicial especifica información del estado en un instante elegido como inicial.

Por ejemplo:

$$[\mathrm{IC}] \qquad x(0)=a.$$ La relación no es una ley universal.

No afirma que todos los sistemas tengan $x(0)=a$.

Describe una realización o preparación particular.

Una condición inicial puede provenir de:

- una medición;

- una preparación experimental;

- un enunciado de problema;

- una elección hipotética.

[]{#pregunta-de-control-4}

##### Pregunta de control {#fispm-c01-pregunta-de-control-4}

> ¿esta ecuación describe la regla de evolución o especifica desde qué estado comenzamos? Una condición de frontera especifica información en el borde de un dominio.

Por ejemplo, en un problema posterior podríamos encontrar simbólicamente

$$[\mathrm{BC}] \qquad u=0 \quad \text{en una frontera}.$$ No necesitamos saber todavía resolver una ecuación de frontera.

Solo distinguir:

$$\boxed{ \text{ley en el interior} \neq \text{condición prescrita en el borde}. }$$ La misma fórmula $u=0$ puede ser una condición de frontera, una condición inicial o una solución, dependiendo del contexto. Esta es la categoría más familiar para un lector matemático.

Supongamos que ya hemos declarado:

$$A=B,$$ $$B=C.$$ Entonces, por transitividad de la igualdad,

$$[\mathrm{MATH}] \qquad A=C.$$ No hemos añadido nueva física.

Hemos deducido una consecuencia lógica.

La regla crítica del proyecto es:

$$\boxed{ \text{la prueba matemática comienza después de declarar las premisas físicas}. }$$ Una derivación física completa puede mezclar varios estatus, pero cada tramo deductivo debe dejar claro qué usa como premisa. Si de un modelo obtenemos matemáticamente

$$P,$$ entonces $P$ es una consecuencia del modelo.

Pero todavía debemos distinguir:

$$\boxed{ \text{«el modelo implica }P\text{»} }$$ de

$$\boxed{ \text{«el experimento observa }P\text{».} }$$ La primera afirmación puede estar demostrada.

La segunda requiere contraste físico. Esta separación será decisiva en §13. Supongamos que un modelo contiene una cantidad $x$. Para compararla con el laboratorio necesitamos alguna conexión como

$$[\mathrm{OBS}] \qquad x \longleftrightarrow \text{procedimiento de medición}.$$ En un experimento con video, por ejemplo, una coordenada física puede inferirse a partir de píxeles mediante una calibración.

La regla que convierte señal instrumental en valor físico no es automáticamente una ley dinámica. Es una **relación de observación**.

[]{#pregunta-de-control-5}

##### Pregunta de control {#fispm-c01-pregunta-de-control-5}

> ¿esta relación nos dice cómo evoluciona el sistema o cómo obtenemos un dato sobre él?

### 1.6.3. Leer una derivación como una cadena de estatus {#fispm-c01-leer-una-derivaciuxf3n-como-una-cadena-de-estatus}

Construyamos una cadena deliberadamente elemental.

Supongamos que registramos dos instantes $t_i$ y $t_f$.

[]{#paso-1-definición}

#### 1.6.3.1. Paso 1 --- Definición {#fispm-c01-paso-1-definiciuxf3n}

$$[\mathrm{DEF}] \qquad \Delta t:=t_f-t_i.$$

#### 1.6.3.2. Paso 2 --- Observación {#fispm-c01-paso-2-observaciuxf3n}

El aparato produce lecturas:

$$[\mathrm{OBS}] \qquad t_i=2.0, \qquad t_f=5.0.$$ No discutimos todavía incertidumbres.

[]{#paso-3-consecuencia-matemática}

#### 1.6.3.3. Paso 3 --- Consecuencia matemática {#fispm-c01-paso-3-consecuencia-matemuxe1tica}

Sustituimos:

$$[\mathrm{MATH}] \qquad \Delta t=5.0-2.0.$$ Entonces:

$$[\mathrm{MATH}] \qquad \Delta t=3.0.$$ La cadena es transparente porque vemos dónde entró el dato y dónde comenzó la deducción.

Si escribiéramos simplemente

$$\Delta t=t_f-t_i=5.0-2.0=3.0,$$ la matemática sería correcta, pero el origen epistemológico de cada parte quedaría oculto. Podemos representar una derivación física típica como una secuencia:

$$[\mathrm{POST}] \to [\mathrm{MOD}] \to [\mathrm{EMP}] \to [\mathrm{IC}] \to [\mathrm{MATH}] \to [\mathrm{APPROX}] \to [\mathrm{MATH}] \to [\mathrm{OBS}].$$ No todas las derivaciones siguen este orden.

El esquema solo muestra que una solución física puede combinar:

- premisas teóricas;

- hipótesis sobre el sistema;

- datos;

- aproximaciones;

- deducciones.

Por eso llamaremos **demostración** únicamente al tramo matemático apropiado.

La argumentación física completa es más amplia. Supongamos que un texto parte de una relación física $L$ y mediante álgebra obtiene otra relación $R$.

Si $L$ es empírica o postulada, podemos demostrar:

$$L\Longrightarrow R.$$ Pero no hemos demostrado que $L$ describa la naturaleza.

Hemos demostrado una implicación dentro del marco. Esta es una diferencia especialmente importante para el lector formado en matemática pura. En matemáticas, las premisas suelen presentarse explícitamente como axiomas, definiciones o hipótesis.

En física, parte de esas premisas puede estar escondida en frases aparentemente inocentes como:

- «despreciemos el rozamiento»;

- «supongamos un cuerpo rígido»;

- «experimentalmente se encuentra que...»;

- «tomemos el sistema inicialmente en reposo».

Nuestro protocolo hace visibles esas entradas. Cuando una ecuación sea ambigua, seguiremos esta secuencia.

[]{#pregunta-1-1}

#### 1.6.3.4. Pregunta 1 {#fispm-c01-pregunta-1-1}

¿Está fijando significado?

Sí:

$$[\mathrm{DEF}].$$

#### 1.6.3.5. Pregunta 2 {#fispm-c01-pregunta-2-1}

¿Conecta el formalismo con un procedimiento de medida?

Sí: $[\mathrm{OBS}].$

#### 1.6.3.6. Pregunta 3 {#fispm-c01-pregunta-3-1}

¿Es una condición particular de preparación o de borde?

Inicial:

$$[\mathrm{IC}].$$ Frontera:

$$[\mathrm{BC}].$$

#### 1.6.3.7. Pregunta 4 {#fispm-c01-pregunta-4-1}

¿Introduce una simplificación del sistema real?

Exacta dentro del modelo:

$$[\mathrm{MOD}].$$ Como reemplazo cercano:

$$[\mathrm{APPROX}].$$

#### 1.6.3.8. Pregunta 5 {#fispm-c01-pregunta-5-1}

¿Funciona como premisa estructural de la teoría?

$$[\mathrm{POST}].$$

#### 1.6.3.9. Pregunta 6 {#fispm-c01-pregunta-6-1}

¿Su respaldo es primordialmente empírico?

$$[\mathrm{EMP}].$$

#### 1.6.3.10. Pregunta 7 {#fispm-c01-pregunta-7}

¿Se sigue lógicamente de premisas ya declaradas?

$$[\mathrm{MATH}].$$ La clasificación puede requerir contexto histórico o teórico adicional.

No siempre será mecánica. Tres casos fronterizos merecen quedar visibles porque reaparecerán en el resto del tratado:

La frontera entre `[``EMP``]` y `[``POST``]` no siempre coincide con una frontera filosófica absoluta. Una relación históricamente descubierta como regularidad empírica puede ser incorporada después como parte estructural de un marco.

Para nuestro uso:

- `[``EMP``]` enfatiza su papel como regularidad respaldada experimentalmente;

- `[``POST``]` enfatiza su papel como premisa organizadora del formalismo.

En los casos dudosos, la solución deberá explicar **por qué** adopta una etiqueta. El objetivo del protocolo no es fingir que toda epistemología de la física cabe en nueve casillas. Es impedir que diferencias importantes desaparezcan bajo una sola palabra: «ecuación». Supongamos que definimos una magnitud $T$ mediante una construcción teórica.

Eso puede ser `[``DEF``]`. Pero si además especificamos que cierto instrumento produce una lectura utilizada para estimar $T$, esa conexión es `[``OBS``]`.

Una misma magnitud puede tener:

$$[\mathrm{DEF}] \qquad \text{significado teórico}$$ y

$$[\mathrm{OBS}] \qquad \text{procedimiento de acceso experimental}.$$ Confundir ambos niveles puede ocultar problemas de calibración. Una observación individual como

$$x=4.2$$ no es una ley física.

Es un dato o resultado de medición. Una colección de datos puede sugerir una relación. Pero el salto

$$\{(x_i,y_i)\} \longrightarrow y=f(x)$$ no es una deducción puramente lógica.

En §9 demostraremos que un conjunto finito de datos puede ser compatible con infinitas funciones distintas. Esta sección prepara la distinción. La regla práctica será sencilla: una demostración matemática comienza una vez declaradas las premisas físicas. Si durante la derivación aparece una nueva premisa empírica, de modelo, de aproximación o de observación, debe marcarse como tal.

[]{#ejercicios}

### 1.6.4. Ejercicios {#fispm-c01-ejercicios}

[]{#fispm-t1-c01-e0019}

**Ejercicio 1.19 --- ¿Qué tipo de afirmación es?.**

Clasifica cada afirmación con la etiqueta más adecuada y justifica.

1.  $\Delta t:=t_f-t_i$.

2.  «El cuerpo se tratará como partícula puntual».

3.  $x(0)=3$, cuando el problema especifica que el sistema se prepara inicialmente con ese valor.

4.  $u=0$ sobre el borde de una región.

5.  $1-2\varepsilon+\varepsilon^2\approx1-2\varepsilon$ para $|\varepsilon|$ suficientemente pequeño.

6.  $A=C$, obtenido únicamente a partir de $A=B$ y $B=C$.

7.  Una relación $Y=kX$ que resume un patrón experimental dentro de un intervalo medido.

8.  Una regla que convierte píxeles de una imagen calibrada en una posición física.

9.  Un principio estructural que la teoría adopta como premisa y del que se derivan consecuencias.

**Solución.**

1.  **`[``DEF``]`.** Fija el significado de $\Delta t$.

2.  **`[``MOD``]`.** Introduce una idealización: un cuerpo extendido se modela como punto.

3.  **`[``IC``]`.** Fija el estado inicial de una realización particular; no es una ley general.

4.  **`[``BC``]`.** Prescribe información en la frontera del dominio.

5.  **`[``APPROX``]`.** Reemplaza una relación por otra cercana en un régimen declarado.

6.  **`[``MATH``]`.** Es consecuencia de la transitividad de la igualdad y no añade una premisa física.

7.  **`[``EMP``]`.** Su respaldo depende del patrón observado experimentalmente.

8.  **`[``OBS``]`.** Conecta el formalismo con un procedimiento de medición.

9.  **`[``POST``]`.** Funciona como premisa estructural del marco.

La estrategia general es:

[]{#fispm-t1-c01-e0020}

$$\boxed{ \text{preguntar por origen y función, no por apariencia algebraica}. }$$ **Ejercicio 1.20 --- La misma fórmula, distinto estatus.**

Construye cuatro contextos distintos en los que la fórmula

$$y=kx$$ tenga respectivamente estatus:

1.  `[``DEF``]`;

2.  `[``EMP``]`;

3.  `[``MOD``]`;

4.  `[``MATH``]`.

Después explica por qué no existe una función que, leyendo únicamente la cadena de símbolos $y=kx$, determine correctamente su estatus físico.

**Solución.**

[]{#como-definición}

##### 1. Como definición {#fispm-c01-como-definiciuxf3n}

Definimos una nueva variable:

$$[\mathrm{DEF}] \qquad y:=kx.$$ La ecuación fija qué significa $y$.

[]{#como-relación-empírica}

##### 2. Como relación empírica {#fispm-c01-como-relaciuxf3n-empuxedrica}

Medimos $x$ e $y$ y encontramos experimentalmente que, dentro de cierto intervalo,

$$[\mathrm{EMP}] \qquad y\approx kx.$$ La relación resume la evidencia.

[]{#como-hipótesis-de-modelo}

##### 3. Como hipótesis de modelo {#fispm-c01-como-hipuxf3tesis-de-modelo}

Decidimos idealizar un sistema mediante una dependencia exactamente lineal:

$$[\mathrm{MOD}] \qquad y=kx.$$ La linealidad exacta pertenece al modelo.

[]{#como-consecuencia-matemática}

##### 4. Como consecuencia matemática {#fispm-c01-como-consecuencia-matemuxe1tica}

Partimos de

$$y=ka$$ y de

$$a=x.$$ Por sustitución:

$$[\mathrm{MATH}] \qquad y=kx.$$

[]{#conclusión-1}

##### Conclusión {#fispm-c01-conclusiuxf3n-1}

La secuencia de caracteres

$$y=kx$$ es la misma en los cuatro casos.

Por tanto, ninguna regla que inspeccione **solo** la sintaxis puede distinguirlos.

El estatus depende de información contextual:

- cómo se introdujo la ecuación;

- qué premisas la sostienen;

- qué papel cumple;

- cómo se conecta con observaciones.

En términos de §5:

$$\boxed{ \text{\parbox{.66\linewidth}{\centering la sintaxis pertenece al núcleo formal; el estatus exige también el diccionario de interpretación y la historia lógica del argumento}}. }$$

### 1.6.5. Síntesis {#fispm-c01-suxedntesis-3}

A partir de ahora no leeremos una ecuación física como una entidad homogénea.

Preguntaremos:

$$\boxed{ \text{¿qué clase de afirmación es?} }$$ La taxonomía canónica es:

$$\boxed{ [\mathrm{DEF}],\, [\mathrm{EMP}],\, [\mathrm{POST}],\, [\mathrm{MOD}],\, [\mathrm{APPROX}],\, [\mathrm{IC}],\, [\mathrm{BC}],\, [\mathrm{MATH}],\, [\mathrm{OBS}] }$$ y la regla fundamental es:

$$\boxed{ \text{la forma matemática no determina el estatus físico}. }$$ Una derivación físicamente rigurosa debe distinguir:

Con esta herramienta ya podemos abordar una distinción más macroscópica.

¿Qué diferencia hay entre una **ley**, un **modelo** y una **teoría**?

Ése será el objeto de (§[1.7](#fispm-c01-ley-modelo-y-teoruxeda)).

[]{#ley-modelo-y-teoría}

[]{#fispm-t1-c01-s07}

[]{#fpm-i-01-s07}

## 1.7. Ley, modelo y teoría {#fispm-c01-ley-modelo-y-teoruxeda}

[]{#tres-niveles-de-organización}

### 1.7.1. Tres niveles de organización {#fispm-c01-tres-niveles-de-organizaciuxf3n}

En física encontramos continuamente expresiones como:

- «ley de...»;

- «modelo de...»;

- «teoría de...».

Es fácil tratarlas como sinónimos vagos de «conjunto de ecuaciones». Pero las seis secciones anteriores ya nos permiten ver que no cumplen la misma función.

Una **ley** suele expresar una regularidad, relación o principio físico.

Un **modelo** representa un sistema o una clase de sistemas bajo determinadas hipótesis. Una **teoría** proporciona una arquitectura más amplia dentro de la cual pueden construirse muchos modelos y derivarse muchas relaciones.

Por tanto, nuestra primera imagen será:

$$\boxed{ \text{ley} \longrightarrow \text{ingrediente estructural} }$$

$$\boxed{ \text{modelo} \longrightarrow \text{representación situada de un sistema} }$$

$$\boxed{ \text{teoría} \longrightarrow \text{marco que organiza familias de modelos} }$$

Estas flechas no expresan una inclusión conjuntista literal.

No estamos diciendo:

$$\text{ley}\subset\text{modelo}\subset\text{teoría}$$

como si cada palabra designara simplemente un conjunto matemático contenido en otro. La relación es **funcional**: una teoría puede contener o motivar leyes, y sus principios permiten construir modelos; un modelo puede emplear leyes y postulados, pero además necesita sistema, interpretación, parámetros, condiciones, idealizaciones y régimen de validez.

#### 1.7.1.1. Ley física {#fispm-c01-ley-fuxedsica}

**Definición operativa 1.19 --- Ley física** Llamaremos **ley física**, en sentido operativo, a una relación, regularidad o principio que expresa una estructura estable del comportamiento físico dentro de un dominio declarado y que puede emplearse como parte de la descripción o predicción de una clase de fenómenos.

Esta definición es deliberadamente amplia.

No exige que toda ley sea:

- una ecuación;

- una relación exacta;

- puramente empírica;

- universal;

- independiente de una teoría;

- válida en todas las escalas.

La palabra «ley» tiene una historia compleja en física. Nuestro objetivo no es imponer una única filosofía de las leyes naturales, sino poder leer correctamente un texto físico. La taxonomía de §6 no desaparece cuando usamos la palabra «ley».

Una relación llamada históricamente «ley» puede aparecer principalmente como: $[\mathrm{EMP}]$

si enfatizamos que resume una regularidad observada.

Otra relación puede aparecer como: $[\mathrm{POST}]$

si dentro de cierta presentación funciona como principio estructural de una teoría. Y una relación llamada «ley» en lenguaje informal puede resultar, dentro de otra formulación, una consecuencia matemática: $[\mathrm{MATH}]$

de principios más generales.

Por eso:

$$\boxed{ \text{«ley» no reemplaza la etiqueta de estatus} }$$

Cuando una ley importante aparezca en este libro, seguiremos preguntando:

> **¿qué estatus tiene aquí?** La palabra «ley» puede sugerir algo sin excepciones y válido en todo contexto.

En física esto sería peligroso. Una ley puede describir con enorme precisión un régimen y dejar de ser adecuada fuera de él.

Por eso una afirmación física debe viajar junto con algún dominio o régimen:

$$\boxed{ \text{ley física utilizada} + \text{régimen de aplicación} }$$

Una relación válida para cierto tipo de sistema, intervalo de variables o escala no queda desacreditada simplemente porque exista un régimen donde deje de funcionar. Lo correcto es especificar **dónde** y **para qué** se utiliza. Esta idea se desarrollará sistemáticamente en §11.

#### 1.7.1.2. Modelo físico {#fispm-c01-modelo-fuxedsico}

En §5 construimos la plantilla formal

$$\mathcal M = (\mathcal S,X,\theta,\mathcal L,I,B,\mathcal R)$$

acompañada por un diccionario de interpretación

$$\mathfrak I_{\mathcal M}.$$

Ahora podemos condensar esa arquitectura.

**Definición operativa 1.20 --- Modelo físico** Un **modelo físico** es una representación estructurada de un sistema o de una clase de sistemas que selecciona estados, variables, parámetros, relaciones, condiciones, idealizaciones, aproximaciones y reglas de interpretación suficientes para responder determinadas preguntas dentro de un régimen de validez.

La frase **suficientes para responder determinadas preguntas** conecta directamente con `1.11`.

Un modelo no es simplemente:

$$\text{ecuación} + \text{números}.$$

Es una arquitectura de representación. Consideremos de nuevo la Tierra.

Según la pregunta podemos utilizar modelos muy diferentes:

- plano local;

- esfera;

- cuerpo rígido;

- masa puntual;

- distribución continua.

No hemos cambiado de planeta.

Hemos cambiado de representación.

Por tanto:

$$\boxed{ \text{un sistema físico} \not\longrightarrow \text{un único modelo obligatorio} }$$

La multiplicidad de modelos no es necesariamente una deficiencia.

Puede reflejar el hecho de que distintas preguntas seleccionan estructuras distintas.

#### 1.7.1.3. Teoría física {#fispm-c01-teoruxeda-fuxedsica}

Una teoría física debe permitir algo más general que describir una única realización.

Debe proporcionar una organización estable que nos diga, por ejemplo:

- qué tipos de sistemas o entidades consideramos;

- qué cantidades pueden representar sus estados;

- qué principios estructurales aceptamos;

- qué relaciones están permitidas;

- cómo construir modelos particulares;

- qué transformaciones dejan intacta la descripción física;

- qué observables pueden compararse con experimentos;

- qué clases de problemas quedan dentro del dominio de la teoría.

No todas las teorías responden estas preguntas del mismo modo.

Pero esta lista muestra una diferencia de escala conceptual. **Definición operativa 1.21 --- Teoría física** Una **teoría física** es un marco conceptual y matemático que organiza una familia de modelos mediante conceptos, principios, estructuras, reglas de construcción e interpretación compartidos, y que permite formular consecuencias contrastables para una clase amplia de fenómenos.

Una teoría no tiene por qué presentarse como una lista finita de axiomas. Tampoco toda la física se organiza históricamente con una única forma lógica. La definición es una guía de lectura. Una teoría útil debe sobrevivir al cambio de problema.

Dentro de un mismo marco podremos estudiar, más adelante:

- partículas;

- sistemas de varias partículas;

- cuerpos rígidos;

- osciladores;

- sistemas sometidos a restricciones;

- campos.

Los modelos pueden parecer matemáticamente muy diferentes. Lo que los reúne es que comparten parte de la arquitectura teórica.

Por eso:

$$\boxed{ \text{unidad teórica} \neq \text{uniformidad superficial de las ecuaciones} }$$

La unidad puede encontrarse en principios, simetrías, estructuras o reglas de construcción.

### 1.7.2. Cómo se relacionan sin confundirse {#fispm-c01-cuxf3mo-se-relacionan-sin-confundirse}

Una ley puede ser ingrediente de un modelo; un modelo representa un sistema o una clase de sistemas; una teoría organiza familias de modelos mediante principios, estructuras y reglas de interpretación. Esta relación es funcional, no una inclusión conjuntista literal.

Supongamos que conocemos una ley esquemática: $Y=kX.$

¿Podemos predecir ya un experimento concreto?

No necesariamente.

Todavía puede faltar:

- qué sistema estudiamos;

- qué valor tiene $k$ para ese sistema;

- cuál es el estado inicial;

- qué cantidad controlamos;

- cómo medimos $X$;

- cómo medimos $Y$;

- qué idealizaciones hemos hecho;

- si el régimen experimental está dentro del dominio de validez.

Así aparece el siguiente nivel:

$$\boxed{ \text{una ley puede ser un ingrediente de un modelo, pero no sustituye al modelo completo} }$$ Podemos distinguir tres niveles.

[]{#nivel-1-teoría}

#### 1.7.2.1. Nivel 1 --- Teoría {#fispm-c01-nivel-1-teoruxeda}

Proporciona una arquitectura general.

[]{#nivel-2-modelo}

#### 1.7.2.2. Nivel 2 --- Modelo {#fispm-c01-nivel-2-modelo}

Selecciona una clase concreta de sistemas, variables, parámetros, hipótesis y condiciones.

[]{#nivel-3-realización}

#### 1.7.2.3. Nivel 3 --- Realización {#fispm-c01-nivel-3-realizaciuxf3n}

Fija valores o datos particulares.

Esquemáticamente:

$$\text{teoría} \longrightarrow \text{familia de modelos} \longrightarrow \text{realización concreta} \longrightarrow \text{predicciones}.$$

Pero para llegar al experimento debemos añadir la capa de observación:

$$\text{predicciones del modelo} \longleftrightarrow [\mathrm{OBS}] \longleftrightarrow \text{datos}.$$ Nuestro péndulo sirve para visualizar la jerarquía sin usar todavía leyes de movimiento.

[]{#sistema-físico-2}

#### 1.7.2.4. Sistema físico {#fispm-c01-sistema-fuxedsico-2}

Esfera, hilo y entorno seleccionado.

[]{#modelo}

#### 1.7.2.5. Modelo {#fispm-c01-modelo}

Decidimos:

- qué pertenece al sistema;

- si la esfera se trata como partícula puntual;

- si el hilo se considera inextensible;

- qué cantidades describen el estado;

- qué parámetros permanecen fijos;

- qué condiciones iniciales se preparan;

- qué efectos se omiten;

- qué observables registramos.

[]{#teoría}

#### 1.7.2.6. Teoría {#fispm-c01-teoruxeda}

Más adelante introduciremos un marco mecánico general que proporcionará principios para construir la dinámica de muchos sistemas distintos, no solo de este péndulo.

El punto importante es:

$$\boxed{ \text{\parbox{.66\linewidth}{\centering la teoría no es «la teoría del péndulo»; el péndulo es un modelo particular construido dentro de un marco más general}} }$$

Todavía no necesitamos conocer ese marco para comprender la jerarquía. La misma situación experimental puede admitir representaciones de distinto nivel sin que las palabras históricas «ley», «modelo» o «teoría» se utilicen siempre con idéntico alcance. Consideremos un dispositivo óptico.

Podemos describir ciertos fenómenos mediante **rayos**. En otras preguntas necesitamos una descripción **ondulatoria**. Más adelante, para otros fenómenos, necesitaremos una descripción **cuántica**.

No desarrollaremos todavía ninguna de esas teorías.

Solo observaremos la arquitectura.

El mismo dispositivo físico puede admitir descripciones diferentes porque cambian:

- las escalas relevantes;

- los observables;

- el tipo de pregunta;

- la precisión;

- los fenómenos que queremos capturar.

Así:

$$\boxed{ \text{cambiar de modelo o de marco teórico} \not\Rightarrow \text{que una descripción anterior haya sido inútil} }$$

Puede seguir siendo excelente dentro de su régimen. Hay nombres establecidos por tradición que pueden resultar engañosos. Algo llamado «modelo» puede ser un marco teórico extraordinariamente amplio.

Algo llamado «ley» puede ocupar el papel de postulado.

Algo llamado «teoría» puede designar una familia histórica de formulaciones distintas. Por eso no corregiremos automáticamente el vocabulario histórico de la física.

Haremos algo más útil:

> **preguntaremos qué función cumple el objeto en el argumento presente.**

La taxonomía es una herramienta de lectura, no una policía terminológica. Una predicción concreta está más situada que la teoría que la hace posible, y la teoría tampoco es un formalismo sin semántica:

Podemos escribir de forma esquemática: $T \longrightarrow M \longrightarrow P,$

donde:

- $T$ representa una teoría;

- $M$ un modelo particular;

- $P$ una predicción.

Pero normalmente una predicción concreta requiere además datos y condiciones:

$$T + M + I + B + \theta + \text{aproximaciones} \longrightarrow P.$$

Por eso, si la predicción falla, no podemos concluir inmediatamente:

$$\text{«la teoría completa es falsa».}$$

En §12 analizaremos formalmente esta lógica de revisión. Podríamos imaginar una teoría como una estructura puramente formal. Pero para ser teoría **física** debe existir alguna manera de conectar parte del formalismo con fenómenos y observaciones.

En términos de §5, una teoría debe permitir construir diccionarios como $\mathfrak I_{\mathcal M}$

para sus modelos. En términos de §6, debe haber relaciones `[``OBS``]` suficientes para confrontar consecuencias con datos.

Por eso:

$$\boxed{ \text{formalismo sin interpretación} \neq \text{teoría física completa} }$$

aunque el formalismo pueda constituir un objeto matemático perfectamente interesante por sí mismo. Feynman insiste en una idea que conviene conservar metodológicamente: el experimento pone a prueba las leyes, pero los datos no generan por sí solos las grandes generalizaciones.[^1]

Hay un salto creativo y estructural:

$$\begin{gathered} \text{observaciones} \longrightarrow \text{regularidades sugeridas}\\[2pt]\Downarrow\\[2pt]\text{hipótesis y generalizaciones}\\[2pt]\Downarrow\\[2pt]\text{nuevas predicciones}. \end{gathered}$$

La flecha central no es una inferencia lógica automática. En §9 veremos una razón matemática elemental: los datos finitos no determinan una función única. Por tanto, una teoría no es una simple compresión mecánica de una tabla experimental. Hassani subraya que las estructuras matemáticas utilizadas en física poseen simultáneamente poder y límites.[^2]

Para nuestro libro esto implica dos reglas.

[]{#regla-1}

##### Regla 1 {#fispm-c01-regla-1}

No presentar una estructura matemática como si su aplicabilidad física fuera automática.

[]{#regla-2}

##### Regla 2 {#fispm-c01-regla-2}

No reducir la matemática a una calculadora.

Una estructura matemática puede revelar:

- invariantes;

- relaciones ocultas;

- posibilidades;

- imposibilidades;

- equivalencias;

- límites;

- nuevas variables naturales.

Así, la relación entre teoría y matemática es bidireccional:

$$\text{estructura física} \longrightarrow \text{formalismo matemático} \longrightarrow \text{nueva comprensión física}.$$

### 1.7.3. Matriz de lectura {#fispm-c01-matriz-de-lectura}

  Pregunta                                     Ley                                     Modelo                                                          Teoría
  -------------------------------------------- --------------------------------------- --------------------------------------------------------------- ------------------------------------------
  ¿Qué organiza?                               una regularidad, relación o principio   un sistema o clase de sistemas                                  una familia de modelos
  ¿Qué necesita además?                        interpretación y dominio                estados, parámetros, condiciones, idealizaciones, observación   principios, estructuras y reglas comunes
  ¿Está situada en una realización concreta?   no necesariamente                       sí, o en una clase bien especificada                            normalmente no
  ¿Su nombre histórico fija su función?        no                                      no                                                              no

**Principio 1.12 --- No colapsar los niveles de organización** Al analizar una afirmación física distinguiremos entre la relación o principio que funciona como ley, el modelo concreto en el que se aplica y la teoría que organiza una familia de modelos. Las tres capas pueden estar estrechamente conectadas, pero no son intercambiables.

Este principio será especialmente útil cuando una derivación parezca decir:

> «La teoría predice...»

Preguntaremos entonces:

1.  ¿qué modelo particular de la teoría se está usando?;

2.  ¿qué condiciones se han fijado?;

3.  ¿qué aproximaciones se han introducido?;

4.  ¿qué observable se compara con el experimento? **Ejercicio.**

[]{#fispm-t1-c01-e0021}

**Ejercicio 1.21 --- Ley, modelo o teoría.**

Clasifica cada descripción principalmente como **ley**, **modelo** o **teoría**, justificando la respuesta. Si el caso admite más de una lectura, explica qué información adicional necesitarías.

1.  Una relación experimental entre dos magnitudes, válida en cierto intervalo, escrita como $Y=kX$.

2.  Una descripción de un péndulo que especifica sistema, masa puntual, hilo inextensible, variables, parámetros, preparación inicial, observables y régimen de validez.

3.  Un marco general que establece conceptos y principios con los que se construyen modelos de muchos sistemas mecánicos diferentes.

4.  La ecuación $Y=kX$ escrita sin ninguna interpretación física.

5.  Un conjunto de reglas para representar un instrumento concreto y convertir su señal en un valor medido.

6.  Un texto histórico titulado «modelo de X» que, al examinarlo, contiene principios generales y permite construir una amplia familia de modelos.

**Solución.**

[]{#relación-experimental-ykx}

##### 1. Relación experimental $Y=kX$ {#fispm-c01-relaciuxf3n-experimental-ykx}

La clasificación principal es:

$$\boxed{\text{ley}}$$

porque se presenta como una regularidad física entre magnitudes dentro de un dominio. Su estatus en el sentido de §6 sería principalmente: $[\mathrm{EMP}].$ Pero para usarla en un problema concreto todavía necesitamos un modelo.

##### 2. Descripción detallada del péndulo {#fispm-c01-descripciuxf3n-detallada-del-puxe9ndulo}

La clasificación principal es:

$$\boxed{\text{modelo}}$$

porque la descripción especifica un sistema particular y organiza:

- idealizaciones;

- variables;

- parámetros;

- condiciones;

- observables;

- régimen.

No basta con que utilice leyes: la característica decisiva es que **sitúa** esas relaciones en una representación concreta.

##### 3. Marco general para muchos sistemas mecánicos {#fispm-c01-marco-general-para-muchos-sistemas-mecuxe1nicos}

La clasificación principal es:

$$\boxed{\text{teoría}}$$

porque proporciona una arquitectura común capaz de generar o estructurar muchos modelos.

##### 4. $Y=kX$ sin interpretación {#fispm-c01-ykx-sin-interpretaciuxf3n}

No podemos clasificarla todavía como ley física.

Es únicamente una relación matemática:

$$\boxed{\text{estructura formal sin estatus físico determinado}}.$$

Necesitamos saber:

- qué significan los símbolos;

- cómo se obtuvo la relación;

- qué función cumple.

Este es exactamente el aprendizaje de §§5--6.

##### 5. Reglas para un instrumento concreto {#fispm-c01-reglas-para-un-instrumento-concreto}

La clasificación principal es:

$$\boxed{\text{modelo}}$$

más precisamente, **modelo del instrumento**.

Puede incluir relaciones `[``OBS``]`, calibraciones e idealizaciones.

No constituye necesariamente una teoría física amplia.

##### 6. Un «modelo» histórico que funciona como marco general {#fispm-c01-un-modelo-histuxf3rico-que-funciona-como-marco-general}

Aquí la respuesta correcta exige separar **nombre histórico** y **función**.

Si realmente contiene principios generales y organiza una amplia familia de modelos, cumple en nuestra taxonomía operativa una función cercana a:

$$\boxed{\text{teoría}}.$$

Sin embargo, no renombraríamos obligatoriamente la construcción histórica.

Diríamos:

> «Se llama tradicionalmente modelo, pero en este contexto desempeña una función teórica más amplia.»

##### Conclusión {#fispm-c01-conclusiuxf3n-2}

[]{#referencias}

[]{#refs}

La clasificación no depende del título.

Depende de la función:

$$\boxed{ \text{ley}:\text{ relación}; \qquad \text{modelo}:\text{ representación situada}; \qquad \text{teoría}:\text{ marco organizador}. }$$

### 1.7.4. Síntesis {#fispm-c01-suxedntesis-4}

Podemos resumir la arquitectura así:

$$\boxed{ \text{teoría} \longrightarrow \text{familias de modelos} \longrightarrow \text{realizaciones} \longrightarrow \text{predicciones} \longleftrightarrow \text{observaciones} }$$

Las leyes aparecen como relaciones o principios dentro de esta arquitectura. Una ley no es todavía un modelo completo. Un modelo no es todavía una teoría general.

Una teoría no produce por sí sola una predicción concreta sin especificar un modelo, datos, condiciones, parámetros y reglas de interpretación.

El principio que conservará el lector es:

$$\boxed{ \text{\parbox{.66\linewidth}{\centering no confundir una relación física, una representación de un sistema y el marco que organiza muchas representaciones}} }$$

Con esta distinción ya podemos formular una nueva pregunta.

Una vez fijados teoría, modelo y condiciones, ¿qué significa **predecir**?

¿Es lo mismo ajustar datos, reconstruir el pasado, predecir una observación nueva y explicar un fenómeno?

Este será el objeto de (§[1.8](#fispm-c01-predicciuxf3n-retrodicciuxf3n-y-explicaciuxf3n)).

[]{#predicción-retrodicción-y-explicación}

[]{#fispm-t1-c01-s08}

[]{#fpm-i-01-s08}

## 1.8. Predicción, retrodicción y explicación {#fispm-c01-predicciuxf3n-retrodicciuxf3n-y-explicaciuxf3n}

[]{#ajustar-y-predecir-no-son-la-misma-operación}

### 1.8.1. Ajustar y predecir no son la misma operación {#fispm-c01-ajustar-y-predecir-no-son-la-misma-operaciuxf3n}

En §7 construimos la cadena

$$\text{teoría} \longrightarrow \text{modelos} \longrightarrow \text{realizaciones} \longrightarrow \text{predicciones} \longleftrightarrow \text{observaciones}.$$

Ahora debemos detenernos en la palabra **predicción**.

Supongamos que un modelo produce el valor

$$y=12.$$

¿Hemos hecho una predicción?

No podemos saberlo todavía. Tal vez el valor $12$ fue calculado antes de realizar una observación nueva.

Pero también podría haber ocurrido lo contrario:

1.  observamos primero el valor $12$;

2.  elegimos después los parámetros del modelo para reproducirlo;

3.  finalmente mostramos que el modelo devuelve precisamente $12$.

La igualdad matemática es la misma. La situación metodológica no.

Por tanto:

$$\boxed{ \text{reproducir un dato conocido} \neq \text{predecir un dato nuevo}. }$$

Esta será nuestra primera distinción. Consideremos una relación elemental: $y=kx.$

Realizamos una observación: $x=2, \qquad y=6.$ Si elegimos $k$ de modo que la relación reproduzca ese dato, obtenemos $k=\frac{6}{2}=3.$ Entonces el modelo

$$y=3x$$

reproduce automáticamente el dato utilizado para fijar $k$: $6=3\cdot2.$

Eso puede ser útil. Pero no constituye todavía una prueba independiente del modelo.

**Definición operativa 1.22 --- Ajuste** Llamaremos **ajuste** al proceso mediante el cual seleccionamos parámetros, condiciones o alguna parte de la forma de un modelo utilizando datos que queremos que el propio modelo reproduzca.

No suponemos aquí ningún método estadístico específico. El ajuste puede ser tan sencillo como determinar una constante a partir de una observación. En el ejemplo anterior, $(x_1,y_1)=(2,6)$

se utilizó para fijar

$$k=3.$$

Por eso, obtener luego

$$y_1=kx_1$$

no es un éxito predictivo independiente.

Era parte del procedimiento de construcción.

**Principio 1.13 --- No confundir ajuste con predicción** Un dato utilizado para seleccionar parámetros, condiciones o estructura de un modelo no debe contarse después como una predicción independiente del mismo modelo.

Esta regla parece obvia cuando el ejemplo contiene una sola constante. En problemas reales puede quedar mucho más escondida. Un modelo puede contener muchos parámetros y haber sido diseñado tras observar una gran cantidad de datos.

Si evaluamos después su «éxito» únicamente sobre esos mismos datos, podemos estar midiendo principalmente su capacidad de ajuste. Shankar formula, en esencia, una de las preguntas clásicas de la mecánica: dada suficiente información sobre el estado presente de un sistema, ¿qué puede decirse de su evolución futura?[^3]

Este es el sentido temporal habitual de **predicción**:

$$\text{estado presente} \longrightarrow \text{estado futuro}.$$

Pero para nuestro método necesitamos una noción un poco más amplia.

Una teoría puede producir una consecuencia acerca de:

- un experimento que todavía no hemos realizado;

- una condición todavía no ensayada;

- una observación pasada que no fue utilizada para construir el modelo;

- una cantidad desconocida aunque no esté en el futuro cronológico.

La distinción relevante es entonces **informacional** además de temporal.

**Definición operativa 1.23 --- Predicción** Una **predicción** es una consecuencia físicamente interpretable de un modelo para una observación, condición o caso cuyo resultado no ha sido utilizado para fijar precisamente esa consecuencia mediante el ajuste del modelo.

Esta definición incluye la predicción temporal como caso central, pero no la reduce a ella. La predicción física requiere además una conexión observacional:

Supongamos que un modelo, ya fijado, implica:

$$[\mathrm{MATH}] \qquad Y_{\mathrm{pred}}=f(X_0;\theta).$$

Mientras $Y_{\mathrm{pred}}$ siga siendo solo un objeto del formalismo, todavía falta la conexión experimental.

Necesitamos:

$$[\mathrm{OBS}] \qquad Y \longleftrightarrow \text{procedimiento de medición}.$$

Entonces podemos comparar

$$Y_{\mathrm{pred}}$$

con

$$Y_{\mathrm{obs}}.$$

La cadena completa es:

$$\boxed{ \text{modelo fijado} \to [\mathrm{MATH}] \ \text{predicción} \to [\mathrm{OBS}] \ \text{dato} \to \text{comparación}. }$$

Una predicción física no termina al obtener una fórmula.

Debe poder traducirse en algo contrastable. Tomemos otra vez

$$y=kx.$$

[]{#paso-1-dato-de-ajuste}

#### 1.8.1.1. Paso 1 --- Dato de ajuste {#fispm-c01-paso-1-dato-de-ajuste}

Observamos: $x_1=2, \qquad y_1=6.$

[]{#paso-2-ajuste}

#### 1.8.1.2. Paso 2 --- Ajuste {#fispm-c01-paso-2-ajuste}

Fijamos: $k=3.$

[]{#paso-3-nuevo-caso}

#### 1.8.1.3. Paso 3 --- Nuevo caso {#fispm-c01-paso-3-nuevo-caso}

Antes de observar el resultado para

$$x_2=5,$$

el modelo produce:

$$[\mathrm{MATH}] \qquad y_{2,\mathrm{pred}}=3\cdot5=15.$$

[]{#paso-4-observación-nueva}

#### 1.8.1.4. Paso 4 --- Observación nueva {#fispm-c01-paso-4-observaciuxf3n-nueva}

Realizamos el procedimiento experimental y obtenemos cierto

$$y_{2,\mathrm{obs}}.$$

Ahora sí existe un contraste entre una consecuencia obtenida **sin usar ese resultado** y una observación posterior. Si ocurre que

$$y_{2,\mathrm{obs}}=15$$

dentro de la precisión pertinente, el nuevo dato es compatible con la predicción.

No hemos demostrado que el modelo sea verdadero.

Hemos superado una prueba nueva. Una predicción acertada apoya un modelo, pero no lo convierte en teorema:

Supongamos que un modelo predice correctamente un dato.

Podemos concluir:

> el modelo ha producido una consecuencia compatible con esa observación.

No podemos concluir automáticamente:

> ninguna otra descripción física podría producirla.

Ni:

> todas las hipótesis del modelo han quedado demostradas.

Ni:

> el modelo funcionará fuera del régimen contrastado.

La lógica es asimétrica. Una predicción acertada proporciona apoyo. Pero no convierte una hipótesis física en un teorema.

En §9 veremos una razón matemática elemental para mantener esta cautela: datos finitos pueden ser compatibles con muchas leyes funcionales distintas. La predicción temporal conserva una estructura especialmente importante para la mecánica:

Supongamos que el modelo posee un conjunto de estados

$$\mathcal S$$

y una regla de evolución de un paso: $E:\mathcal S\to\mathcal S.$ Si el estado actual es $s_0\in\mathcal S,$

el modelo predice: $s_1=E(s_0).$ Y después: $s_2=E(s_1).$

No necesitamos ecuaciones diferenciales para comprender la estructura lógica.

La predicción temporal consiste en combinar:

- un estado inicial;

- una regla de evolución;

- parámetros;

- condiciones externas pertinentes.

Esquemáticamente:

$$\boxed{ (s_0,\theta,\mathcal L) \longrightarrow s_1. }$$ En §3 vimos que una fotografía del péndulo puede mostrar la misma posición para dos estados dinámicamente diferentes.

Esto significa que una descripción insuficiente del presente puede producir ambigüedad futura. Si dos estados

$$s_a\neq s_b$$

comparten la misma observación: $O(s_a)=O(s_b),$

pero evolucionan de manera distinta: $E(s_a)\neq E(s_b),$

entonces el dato observable actual no basta para una predicción única. La dificultad no está en «resolver mal la ecuación». Está en que no conocemos suficiente estado. En §3 dejamos abierto un punto importante.

No toda teoría predice un único resultado.

Podemos encontrar:

[]{#predicción-determinista}

##### Predicción determinista {#fispm-c01-predicciuxf3n-determinista}

$$s_0 \longrightarrow s_1.$$

[]{#predicción-probabilística}

##### Predicción probabilística {#fispm-c01-predicciuxf3n-probabiluxedstica}

$$s_0 \longrightarrow \{\text{probabilidades para resultados posibles}\}.$$

Por tanto:

$$\boxed{ \text{predecir} \neq \text{afirmar siempre un único valor futuro}. }$$

Más adelante desarrollaremos formalmente la probabilidad física. Aquí solo preservamos una definición suficientemente general. La palabra «nuevo» no significa siempre «futuro» ni garantiza el mismo nivel de riesgo. Una predicción dentro de la región ya contrastada y una extrapolación lejana son metodológicamente diferentes.

Usaremos informalmente:

- **interpolación**: predecir dentro de una región rodeada o cubierta por condiciones previamente observadas;

- **extrapolación**: extender la predicción más allá del dominio donde el modelo fue ajustado o contrastado.

No fijaremos todavía una definición matemática general.

Lo importante es:

$$\boxed{ \text{dato nuevo} \not\Rightarrow \text{mismo nivel de riesgo}. }$$

Una extrapolación puede poner a prueba una estructura de manera particularmente fuerte, pero también puede simplemente abandonar el régimen de validez del modelo. Por eso toda extrapolación exige revisar

$$\mathcal R.$$

### 1.8.2. Retrodicción {#fispm-c01-retrodicciuxf3n}

A veces conocemos información actual y queremos reconstruir un estado anterior.

La dirección de la pregunta cambia:

$$\text{presente} \longrightarrow \text{pasado posible}.$$

**Definición operativa 1.24 --- Retrodicción** Una **retrodicción** es una inferencia, realizada mediante un modelo, desde datos o estados posteriores hacia estados, condiciones o acontecimientos anteriores compatibles con ellos.

No es simplemente «recordar el pasado». Es usar una estructura física para reconstruirlo. Supongamos que

$$E:\mathcal S\to\mathcal S$$

es una regla de evolución.

Dado un estado final

$$s_1,$$

queremos encontrar estados $s_0$ tales que

$$E(s_0)=s_1.$$

Puede ocurrir que exista:

- ningún estado previo compatible;

- un único estado previo;

- varios estados previos.

La retrodicción no es automáticamente única. Sea

$$\mathcal S=\{a,b,c\}$$

y definamos:

$$E(a)=c,$$

$$E(b)=c,$$

$$E(c)=b.$$

Supongamos que observamos actualmente: $s_1=c.$

¿Qué estados anteriores son compatibles?

Buscamos soluciones de: $E(s_0)=c.$

Tenemos: $E(a)=c$

y

$$E(b)=c.$$

Por tanto, el pasado compatible puede ser: $s_0=a$

o

$$s_0=b.$$

La información actual no determina cuál ocurrió.

Así:

$$\boxed{ \text{evolución bien definida hacia adelante} \not\Rightarrow \text{retrodicción única}. }$$ En la práctica quizá ni siquiera conozcamos el estado final completo.

Conocemos un dato: $O(s_1)=d.$ Si el observable

$$O:\mathcal S\to\mathcal V$$

no es inyectivo, varios estados presentes pueden producir el mismo dato.

Entonces existen dos fuentes de ambigüedad:

1.  varios estados presentes compatibles con el dato;

2.  varios estados pasados compatibles con cada estado presente.

Por eso reconstruir el pasado puede ser un problema mucho más delicado que simplemente «poner tiempo negativo». Imaginemos que un modelo, a partir de datos actuales, retrodice:

> en una etapa anterior debía haber ocurrido cierto evento observable.

Si posteriormente encontramos un registro independiente de ese pasado ---un archivo experimental, una huella material, una observación astronómica conservada--- podemos contrastar la retrodicción. Así, el valor metodológico de una consecuencia física no depende solamente de que apunte hacia el futuro cronológico.

También puede depender de que alcance información **no utilizada para producirla**.

### 1.8.3. Explicación {#fispm-c01-explicaciuxf3n}

Ahora aparece una cuarta palabra.

Supongamos que un modelo:

- ajusta correctamente los datos;

- predice correctamente una observación nueva;

- permite reconstruir estados anteriores.

¿Hemos explicado el fenómeno?

Tal vez. Pero no automáticamente.

La palabra **explicación** exige preguntar qué parte de la estructura del modelo hace inteligible el resultado. **Definición operativa 1.25 --- Explicación física** Llamaremos **explicación física**, en sentido operativo, a un argumento que muestra cómo un fenómeno, regularidad o resultado depende de estructuras, mecanismos, principios, condiciones o relaciones del modelo o de la teoría, de modo que podamos identificar qué elementos son responsables de que el resultado tenga la forma observada.

Esta definición no pretende resolver toda la filosofía de la explicación científica.

Nos basta para distinguir:

$$\text{«el modelo da el número correcto»}$$

de:

$$\text{«podemos identificar por qué el modelo produce este comportamiento»}.$$ Consideremos un resultado esquemático:

$$Q=f(a,b,c).$$

Una explicación útil puede preguntar:

- ¿qué ocurre si cambiamos $a$?;

- ¿el resultado depende realmente de $b$?;

- ¿qué término domina?;

- ¿qué simetría obliga a cierta forma?;

- ¿qué mecanismo produce el signo?;

- ¿qué hipótesis es responsable de la regularidad?;

- ¿qué cambiaría si eliminamos una interacción?

La explicación no consiste solamente en repetir la derivación.

Consiste en reconocer **qué estructura produce qué consecuencia**.

**Principio 1.14 --- Explicar exige identificar dependencias** Una explicación física no queda completa por el solo hecho de reproducir o predecir un resultado; debe hacer visible qué estructura, hipótesis, mecanismo o principio del modelo es responsable del comportamiento que se quiere comprender. Una derivación correcta puede ser poco explicativa si oculta qué dependencia produce el resultado:

Imaginemos una cadena algebraica de cincuenta pasos que termina en el número observado.

Puede ser matemáticamente impecable.

Pero quizá no sepamos todavía:

- qué hipótesis controla el resultado;

- por qué cambia de signo;

- por qué una variable no aparece;

- qué efecto es dominante;

- qué simplificación sería fatal.

En ese sentido, una derivación larga puede proporcionar una consecuencia sin proporcionar todavía una buena explicación física.

Esto conecta con §4:

una aproximación bien elegida puede ser más explicativa que una fórmula exacta si hace visible la jerarquía de efectos. Una explicación puede ser mecanística, estructural o unificadora, pero en todos los casos debe mostrar una dependencia que vaya más allá de reproducir un dato conocido.

No todas las explicaciones físicas tienen la misma forma.

[]{#explicación-causal-o-mecanística}

#### 1.8.3.1. Explicación causal o mecanística {#fispm-c01-explicaciuxf3n-causal-o-mecanuxedstica}

Identifica una cadena de interacciones o procesos.

[]{#explicación-estructural}

#### 1.8.3.2. Explicación estructural {#fispm-c01-explicaciuxf3n-estructural}

Muestra que un resultado está obligado por cierta geometría, restricción, invariancia o estructura matemática.

[]{#explicación-por-unificación}

#### 1.8.3.3. Explicación por unificación {#fispm-c01-explicaciuxf3n-por-unificaciuxf3n}

Muestra que fenómenos aparentemente distintos son casos de un mismo principio.

No fijaremos fronteras rígidas entre estas categorías.

Solo queremos evitar identificar «explicación» con una única clase de relato. El peligro contrario también existe. Podemos contar una historia intuitiva y llamarla «explicación».

Pero una explicación física debe estar conectada con el modelo y sus consecuencias.

Si afirmamos que cierto mecanismo produce un resultado, debemos poder preguntar:

> ¿qué cambiaría si ese mecanismo no estuviera presente?

La explicación gana contenido cuando produce diferencias contrastables.

Por eso:

$$\boxed{ \text{explicación física} \leftrightarrow \text{estructura del modelo} \leftrightarrow \text{consecuencias}. }$$ Supongamos que dos modelos $M_1$ y $M_2$ producen, para todos los datos disponibles:

$$P_1=P_2.$$

No se sigue que posean la misma explicación.

Pueden atribuir el comportamiento a estructuras distintas.

Mientras no encontremos una observación capaz de distinguirlas, los datos no seleccionan necesariamente una interpretación única. Esta situación prepara §9. Allí mostraremos matemáticamente, en un caso elemental, que una colección finita de datos no determina una única ley funcional. Existen al menos cuatro situaciones conceptuales.

  Caso   Predice           Explica
  ------ ----------------- -------------------
  A      sí                sí
  B      sí                débilmente
  C      no todavía        propone mecanismo
  D      reproduce datos   no necesariamente

[]{#caso-a}

#### 1.8.3.4. Caso A {#fispm-c01-caso-a}

Un modelo predice observaciones nuevas y muestra qué estructura las produce.

[]{#caso-b}

#### 1.8.3.5. Caso B {#fispm-c01-caso-b}

Un modelo entrega resultados precisos, pero su mecanismo físico permanece poco transparente.

[]{#caso-c}

#### 1.8.3.6. Caso C {#fispm-c01-caso-c}

Una hipótesis ofrece una explicación plausible, pero todavía no produce predicciones suficientemente precisas.

[]{#caso-d}

#### 1.8.3.7. Caso D {#fispm-c01-caso-d}

Una fórmula flexible reproduce datos conocidos sin revelar por qué el fenómeno ocurre. La ciencia intenta, idealmente, mejorar simultáneamente capacidad predictiva y comprensión.

Pero no son la misma propiedad. Supongamos que observamos:

> dos configuraciones aparentemente diferentes producen el mismo resultado.

Proponemos una explicación:

> ambas comparten una estructura relevante $S$ y las diferencias restantes no intervienen en el fenómeno.

Esta explicación debería permitir una prueba.

Buscamos una tercera configuración que:

- conserve $S$;

- cambie otros aspectos;

- no haya sido usada para construir la hipótesis.

Si el modelo predice que el resultado permanecerá igual y la observación coincide, la explicación gana apoyo.

La idea es:

$$\boxed{ \text{una buena explicación abre nuevas preguntas contrastables}. }$$

### 1.8.4. Separar construcción y contraste {#fispm-c01-separar-construcciuxf3n-y-contraste}

Recordemos:

$$\mathcal M = (\mathcal S,X,\theta,\mathcal L,I,B,\mathcal R),$$

junto con

$$\mathfrak I_{\mathcal M}.$$

Podemos situar nuestras nuevas operaciones.

[]{#ajuste}

#### 1.8.4.1. Ajuste {#fispm-c01-ajuste}

Usa observaciones para fijar parte de: $\theta,\quad I,\quad \mathcal L$

o incluso elecciones de estructura.

[]{#predicción}

#### 1.8.4.2. Predicción {#fispm-c01-predicciuxf3n}

Con el modelo ya fijado, deriva consecuencias para casos no utilizados en ese ajuste.

[]{#retrodicción}

#### 1.8.4.3. Retrodicción {#fispm-c01-retrodicciuxf3n-1}

Busca estados o condiciones anteriores compatibles con datos posteriores.

[]{#explicación}

#### 1.8.4.4. Explicación {#fispm-c01-explicaciuxf3n-1}

Identifica qué componentes de

$$\mathcal M$$

y de

$$\mathfrak I_{\mathcal M}$$

son responsables de la forma del fenómeno. Podemos representar un buen procedimiento mediante dos conjuntos de datos conceptualmente separados.

[]{#datos-de-construcción}

#### 1.8.4.5. Datos de construcción {#fispm-c01-datos-de-construcciuxf3n}

$$D_{\mathrm{ajuste}}.$$

Se usan para elegir parámetros o estructura.

[]{#datos-de-contraste}

#### 1.8.4.6. Datos de contraste {#fispm-c01-datos-de-contraste}

$$D_{\mathrm{nuevo}}.$$

No se utilizan para fijar aquello que se va a poner a prueba.

Entonces:

$$D_{\mathrm{ajuste}} \longrightarrow M_{\mathrm{fijado}} \longrightarrow P(D_{\mathrm{nuevo}}) \longleftrightarrow D_{\mathrm{nuevo}}.$$

No introducimos todavía estadística. La separación es puramente lógica. A veces tenemos pocos datos y necesitamos utilizarlos todos para construir el modelo.

Eso puede ser razonable. Pero debemos describir correctamente lo que hemos logrado.

Podemos afirmar:

> «El modelo es compatible con los datos utilizados para construirlo.»

No debemos exagerar:

> «El modelo ha predicho independientemente todos esos datos.»

Entonces la siguiente tarea científica puede ser buscar:

- nuevos casos;

- nuevas escalas;

- nuevos observables;

- nuevas condiciones experimentales. Supongamos que un modelo ha funcionado para:

$$x\in[0,10].$$

Ahora predecimos para: $x=10.1.$ Tal vez sea razonable. Pero predecir para: $x=10^{12}$

puede exigir una justificación completamente distinta.

Antes de aceptar una extrapolación debemos preguntar:

$$\boxed{ \text{¿seguimos dentro de }\mathcal R\text{?} }$$

Una predicción algebraicamente bien calculada puede ser físicamente irrelevante si abandona el régimen de validez. Supongamos:

$$P_{\mathrm{modelo}} \neq O_{\mathrm{experimento}}.$$

¿Qué ha fallado?

Todavía no podemos decir.

Podrían estar implicados:

- la teoría;

- el modelo particular;

- un parámetro;

- una condición inicial;

- una aproximación;

- una idealización;

- una regla `[``OBS``]`;

- el procedimiento experimental.

En §12 formalizaremos esta lógica.

Por ahora la lección es:

$$\boxed{ \text{fallo predictivo} \neq \text{diagnóstico automático}. }$$ **Ficha FPM --- Ajuste, predicción, retrodicción y explicación** 1. **Datos usados:** ¿qué observaciones ya conocíamos? 2. **Ajuste:** ¿qué parámetros o elecciones se fijaron con esos datos? 3. **Predicción:** ¿qué resultado no fue utilizado para fijar la consecuencia? 4. **Régimen:** ¿la nueva condición pertenece a $\mathcal R$? 5. **Observación:** ¿qué regla `[``OBS``]` conecta la predicción con un dato? 6. **Retrodicción:** si inferimos el pasado, ¿la reconstrucción es única? 7. **Explicación:** ¿qué estructura concreta del modelo produce el resultado? 8. **Alternativas:** ¿otra estructura podría producir observaciones semejantes? 9. **Nueva prueba:** ¿qué observación distinguiría las alternativas? Esta separación prepara §9: incluso un ajuste perfecto sobre datos finitos no determina por sí solo una ley única. La fuerza de una prueba aumenta cuando el modelo se compromete con resultados que no fueron utilizados para construir precisamente esa consecuencia.

**Ejercicio.**

[]{#fispm-t1-c01-e0022}

**Ejercicio 1.22 --- Ajuste, predicción, retrodicción y explicación.**

Considera el modelo

$$y=kx.$$

Se observa primero: $(x_1,y_1)=(2,6).$ Con ese dato se fija: $k=3.$

[]{#parte-a}

##### Parte A {#fispm-c01-parte-a}

Clasifica cada operación.

1.  Verificar que $6=3\cdot2$.

2.  Antes de medir un segundo caso, calcular que para $x_2=5$ el modelo da $y_2=15$.

3.  Medir después $y_2$ y compararlo con $15$.

4.  Usar también el segundo dato para modificar $k$ y después presentar ambos datos como «predicciones independientes».

[]{#parte-b}

##### Parte B {#fispm-c01-parte-b}

Sea ahora

$$\mathcal S=\{a,b,c\}$$

con evolución

$$E(a)=c, \qquad E(b)=c, \qquad E(c)=b.$$

Si el estado actual es $c$, determina todos los estados anteriores posibles.

[]{#parte-c}

##### Parte C {#fispm-c01-parte-c}

Un estudiante afirma:

> «Como el modelo reproduce correctamente todos los datos con los que fue construido, ya hemos explicado el fenómeno.»

Analiza la afirmación. **Solución.**

[]{#parte-a.1}

##### Parte A.1 {#fispm-c01-parte-a.1}

Comprobar

$$6=3\cdot2$$

es verificar que el modelo ajustado reproduce el dato utilizado para fijar $k$.

Clasificación:

$$\boxed{\text{reproducción de dato de ajuste}}.$$

No es una predicción independiente.

[]{#parte-a.2}

##### Parte A.2 {#fispm-c01-parte-a.2}

El cálculo

$$y_{2,\mathrm{pred}} = 3\cdot5 = 15$$

se hace antes de usar el resultado del segundo caso.

Clasificación:

$$\boxed{\text{predicción}}.$$

Es una consecuencia `[``MATH``]` del modelo ya fijado.

[]{#parte-a.3}

##### Parte A.3 {#fispm-c01-parte-a.3}

Medir $y_2$ y compararlo con $15$ es:

$$\boxed{\text{contraste experimental de una predicción}}.$$

La comparación necesita una regla `[``OBS``]`. Si la observación coincide, el nuevo dato apoya el modelo dentro del régimen considerado. Si no coincide, habrá que diagnosticar qué componente falla.

[]{#parte-a.4}

##### Parte A.4 {#fispm-c01-parte-a.4}

Si utilizamos también el segundo dato para volver a escoger $k$, ese dato deja de ser independiente respecto del ajuste resultante. Presentarlo después como si hubiera sido predicho sin haber intervenido en la construcción viola principio 1.13.

Clasificación:

$$\boxed{\text{nuevo ajuste, no predicción independiente}}.$$

[]{#parte-b-1}

##### Parte B {#fispm-c01-parte-b-1}

Buscamos todos los $s_0\in\mathcal S$ tales que

$$E(s_0)=c.$$

Como $E(a)=c$

y

$$E(b)=c,$$

los estados pasados compatibles son:

$$\boxed{s_0\in\{a,b\}}.$$

No podemos distinguirlos utilizando solo el estado actual $c$. Por tanto, la retrodicción no es única.

[]{#parte-c-1}

##### Parte C {#fispm-c01-parte-c-1}

La afirmación es demasiado fuerte.

Que el modelo reproduzca los datos utilizados para construirlo muestra, como mínimo, **compatibilidad con esos datos**.

No demuestra por sí solo:

- capacidad predictiva independiente;

- unicidad del modelo;

- corrección de todas sus idealizaciones;

- adecuación fuera del régimen contrastado;

- explicación física del mecanismo.

Para hablar de explicación necesitamos identificar qué estructura del modelo produce el fenómeno y qué diferencias observables esperaríamos si esa estructura cambiara.

Además, una prueba más fuerte debería reservar algún resultado nuevo:

$$D_{\mathrm{ajuste}} \longrightarrow M \longrightarrow P(D_{\mathrm{nuevo}}) \longleftrightarrow D_{\mathrm{nuevo}}.$$

La conclusión correcta es:

$$\boxed{ \text{ajustar} \neq \text{predecir} \neq \text{explicar}. }$$

### 1.8.5. Síntesis {#fispm-c01-suxedntesis-5}

Ya podemos distinguir cuatro operaciones.

$$\boxed{ \text{ajuste} = \text{usar datos para fijar el modelo} }$$

$$\boxed{ \text{predicción} = \text{obtener una consecuencia para un caso no usado para fijarla} }$$

$$\boxed{ \text{retrodicción} = \text{inferir estados o condiciones anteriores desde información posterior} }$$

$$\boxed{ \text{explicación} = \text{hacer visible qué estructura produce el fenómeno} }$$

La relación entre ellas puede representarse como:

$$D_{\mathrm{ajuste}} \to M \to \begin{cases} \text{predicción},\\ \text{retrodicción},\\ \text{explicación} \end{cases} \longleftrightarrow D_{\mathrm{nuevo}}.$$

Y conservaremos dos reglas:

$$\boxed{ \text{dato usado para ajustar} \neq \text{predicción independiente} }$$

y

$$\boxed{ \text{éxito predictivo} \neq \text{explicación automática}. }$$

Ahora podemos enfrentar una pregunta más profunda.

Si observamos una colección finita de datos y encontramos una función que pasa exactamente por todos ellos, ¿hemos descubierto **la** ley?

La respuesta matemática será no. En la sección siguiente lo demostraremos.

Entramos así en el §[1.9](#fispm-c01-datos-finitos-no-determinan-una-ley-uxfanica).

[]{#datos-finitos-no-determinan-una-ley-única}

[]{#fispm-t1-c01-s09}

[]{#fpm-i-01-s09}

## 1.9. Datos finitos no determinan una ley única {#fispm-c01-datos-finitos-no-determinan-una-ley-uxfanica}

[]{#una-tabla-no-trae-escrita-su-ley}

### 1.9.1. Una tabla no trae escrita su ley {#fispm-c01-una-tabla-no-trae-escrita-su-ley}

Supongamos que realizamos un experimento y obtenemos los pares

$$(x_1,y_1),\ldots,(x_n,y_n).$$

Imaginemos además que encontramos una función $f$ que reproduce exactamente todos los datos: $f(x_i)=y_i$

para cada

$$i=1,\ldots,n.$$

La tentación es decir:

> «Hemos encontrado la ley que generan los datos».

Pero esa conclusión contiene más información que las observaciones.

Los datos nos dicen qué debe ocurrir en los puntos medidos: $x_1,\ldots,x_n.$

No nos dicen directamente qué debe ocurrir en los demás valores de $x$.

Entre dos puntos observados, o fuera del intervalo observado, quedan infinitas posibilidades. Esta sección convertirá esa cautela en un resultado matemático exacto.

[]{#fig:I-01-N03}

![**Figura 1.5.** Las curvas $y=x$ (continua) y $y=x+x(x-1)(x-2)/3$ (discontinua) coinciden en $x=0,1,2$. Los tres datos no fijan la interpolación entre ellos. Véase §[1.9](#fispm-c01-datos-finitos-no-determinan-una-ley-uxfanica).](/assets/books/fispm/v04/I-01-N03.svg "fig:"){.fpm-v04-figure fig-alt="Datos y leyes compatibles" width="395px" fig-cap=""}

### 1.9.2. Compatibilidad no es unicidad {#fispm-c01-compatibilidad-no-es-unicidad}

Conviene separar dos afirmaciones.

[]{#afirmación-a}

#### 1.9.2.1. Afirmación A {#fispm-c01-afirmaciuxf3n-a}

La función $f$ es **compatible** con los datos: $f(x_i)=y_i$

para todos los $i$.

[]{#afirmación-b}

#### 1.9.2.2. Afirmación B {#fispm-c01-afirmaciuxf3n-b}

La función $f$ es la **única** función compatible con los datos. La primera no implica la segunda.

En símbolos:

$$\boxed{ f(x_i)=y_i\ \text{para todos los datos} \not\Rightarrow f\ \text{es la única ley compatible}. }$$

El salto de compatibilidad a unicidad necesita hipótesis adicionales.

### 1.9.3. Dos puntos: la intuición geométrica más simple {#fispm-c01-dos-puntos-la-intuiciuxf3n-geomuxe9trica-muxe1s-simple}

Tomemos dos observaciones: $(0,0), \qquad (1,1).$ La función

$$p(x)=x$$

pasa por ambos puntos.

Podríamos pensar que los datos sugieren la recta

$$y=x.$$

Pero consideremos ahora

$$q(x)=x+c\,x(x-1),$$

donde $c$ es cualquier constante. En $x=0$, $q(0) = 0+c\cdot0\cdot(-1) = 0.$ En $x=1$, $q(1) = 1+c\cdot1\cdot0 = 1.$ Por tanto, **todos** los valores de $c$ producen funciones que pasan por los dos mismos puntos. Para $c=0$: $q(x)=x.$ Para $c=1$: $q(x)=x+x(x-1)=x^2.$

Para $c=-1$: $q(x)=x-x(x-1)=2x-x^2.$

Las tres funciones coinciden en los datos: $q(0)=0, \qquad q(1)=1,$

pero no coinciden, por ejemplo, en

$$x=\frac12.$$

Así aparecen muchas continuaciones posibles de la misma evidencia finita.

### 1.9.4. El truco algebraico {#fispm-c01-el-truco-algebraico}

¿Qué hizo funcionar el ejemplo?

Añadimos a $p(x)$ un término que vale cero exactamente en todos los puntos observados. Con dos datos usamos: $x(x-1).$

Este producto se anula cuando:

$$x=0$$

o

$$x=1.$$

Por eso modificar

$$p(x)$$

mediante $p(x)+c\,x(x-1)$

no altera ninguno de los datos. La idea general será construir un polinomio que se anule en todos los valores observados.

### 1.9.5. El polinomio que desaparece en los datos {#fispm-c01-el-polinomio-que-desaparece-en-los-datos}

Sean

$$x_1,\ldots,x_n\in\mathbb R$$

valores distintos de la variable independiente.

Definimos $Z(x) = \prod_{i=1}^{n}(x-x_i).$

No necesitamos ninguna teoría avanzada de polinomios para observar que, para cada índice $j$, $Z(x_j) = \prod_{i=1}^{n}(x_j-x_i).$ En ese producto aparece el factor correspondiente a $i=j$: $x_j-x_j=0.$ Por tanto,

$$\boxed{ Z(x_j)=0 }$$

para todo

$$j=1,\ldots,n.$$

Esta es toda la idea algebraica que necesitaremos.

### 1.9.6. Primera proposición formal del capítulo {#fispm-c01-primera-proposiciuxf3n-formal-del-capuxedtulo}

**1.1 --- Datos finitos no determinan una ley polinómica única**

Sean $x_1,\ldots,x_n\in\mathbb R$ valores distintos y sean $y_1,\ldots,y_n\in\mathbb R$. Supongamos que un polinomio

$$p\in\mathbb R[x]$$

satisface $p(x_i)=y_i$

para todo

$$i=1,\ldots,n.$$

Entonces, para toda constante

$$c\in\mathbb R,$$

el polinomio

$$p_c(x) = p(x) + c\prod_{i=1}^{n}(x-x_i)$$

satisface exactamente los mismos datos: $p_c(x_i)=y_i$

para todo

$$i=1,\ldots,n.$$

Además, si $c_1\neq c_2$, entonces $p_{c_1}\neq p_{c_2}.$ Por tanto, una vez que existe un polinomio compatible con los datos, existen infinitos polinomios distintos compatibles con esos mismos datos.

[]{#demostración-de-fpm-i-01-p01}

[]{#fispm-t1-c01-p0001}

### 1.9.7. Demostración de 1.1 {#fispm-c01-demostraciuxf3n-de-1.1}

[]{#paso-1-fijar-uno-de-los-datos}

#### 1.9.7.1. Paso 1 --- Fijar uno de los datos {#fispm-c01-paso-1-fijar-uno-de-los-datos}

Sea

$$j\in\{1,\ldots,n\}.$$

Queremos evaluar

$$p_c(x_j).$$

Por definición: $p_c(x_j) = p(x_j) + c\prod_{i=1}^{n}(x_j-x_i).$

[]{#paso-2-usar-el-dato-conocido}

#### 1.9.7.2. Paso 2 --- Usar el dato conocido {#fispm-c01-paso-2-usar-el-dato-conocido}

Como $p$ es compatible con los datos, $p(x_j)=y_j.$ Por tanto: $p_c(x_j) = y_j + c\prod_{i=1}^{n}(x_j-x_i).$

[]{#paso-3-detectar-el-factor-nulo}

#### 1.9.7.3. Paso 3 --- Detectar el factor nulo {#fispm-c01-paso-3-detectar-el-factor-nulo}

En el producto aparece el factor

$$x_j-x_j=0.$$

Luego: $\prod_{i=1}^{n}(x_j-x_i)=0.$

Así, $p_c(x_j) = y_j+c\cdot0 = y_j.$

Como $j$ era arbitrario,

$$\boxed{ p_c(x_i)=y_i \quad \text{para todo }i=1,\ldots,n. }$$

[]{#paso-4-mostrar-que-la-familia-contiene-polinomios-distintos}

#### 1.9.7.4. Paso 4 --- Mostrar que la familia contiene polinomios distintos {#fispm-c01-paso-4-mostrar-que-la-familia-contiene-polinomios-distintos}

Sean

$$c_1\neq c_2.$$

Entonces:

$$p_{c_1}(x)-p_{c_2}(x) = (c_1-c_2) \prod_{i=1}^{n}(x-x_i).$$

Como $c_1-c_2\neq0$

y

$$\prod_{i=1}^{n}(x-x_i)$$

no es el polinomio cero, tenemos: $p_{c_1}-p_{c_2} \neq 0.$ Por tanto: $p_{c_1}\neq p_{c_2}.$

Finalmente, como existen infinitos números reales $c$, obtenemos infinitos polinomios distintos compatibles con los mismos datos.

$$\boxed{\text{QED}}$$

### 1.9.8. Qué se demostró exactamente {#fispm-c01-quuxe9-se-demostruxf3-exactamente}

La proposición **no** dice que cualquier polinomio pase por los datos.

Dice algo más preciso.

Partimos de **un** polinomio compatible:

$$p.$$

Después construimos una familia: $\{p_c\}.$

Todos los miembros conservan las observaciones porque la modificación añadida desaparece en los puntos medidos.

La estructura es:

$$\boxed{ \text{ajuste conocido} + \text{término invisible en los datos} = \text{nuevo ajuste igualmente compatible}. }$$

Ésa es la idea que debemos conservar.

### 1.9.9. La demostración es matemática; la conclusión física necesita interpretación {#fispm-c01-la-demostraciuxf3n-es-matemuxe1tica-la-conclusiuxf3n-fuxedsica-necesita-interpretaciuxf3n}

`1.1` es una proposición matemática. Su estatus es: $[\mathrm{MATH}].$

La proposición no afirma por sí sola:

> «Las leyes de la naturaleza son polinomios».

Tampoco afirma:

> «Nunca podemos conocer ninguna ley física».

Lo que demuestra es más limitado y más útil:

> una colección finita de valores no basta, por sí sola, para seleccionar una única función polinómica entre todas las que podrían reproducirlos.

La inferencia física será:

$$\boxed{ \text{ajuste exacto a datos finitos} \not\Rightarrow \text{identificación lógica de una ley única}. }$$

### 1.9.10. El papel de las hipótesis adicionales {#fispm-c01-el-papel-de-las-hipuxf3tesis-adicionales}

¿Cómo puede la física elegir entre funciones compatibles?

Necesitamos información adicional.

Por ejemplo, podemos imponer:

- una clase restringida de funciones;

- una simetría;

- una estructura teórica;

- un mecanismo;

- un principio de conservación;

- un régimen de validez;

- restricciones sobre parámetros;

- nuevas observaciones.

La función no se elige solamente preguntando:

> «¿pasa por los puntos?»

También preguntamos:

> «¿qué estructura física la justifica?»

Este será precisamente el tema de §10.

### 1.9.11. Si restringimos la clase, la situación puede cambiar {#fispm-c01-si-restringimos-la-clase-la-situaciuxf3n-puede-cambiar}

Supongamos que tenemos los dos puntos

$$(0,0), \qquad (1,1).$$

Entre **todas** las funciones hay innumerables posibilidades.

Entre todos los polinomios también.

Pero si imponemos la hipótesis adicional:

> «la relación debe ser lineal y de la forma $y=mx+b$»,

entonces los dos datos pueden determinar $m$ y $b$. La unicidad no proviene solamente de los dos puntos.

Proviene de:

$$\boxed{ \text{datos} + \text{restricción de clase}. }$$

Por tanto, cuando un conjunto de datos parece «determinar» una ley debemos preguntar:

> **¿dentro de qué clase de modelos?**

### 1.9.12. Ajuste perfecto y complejidad {#fispm-c01-ajuste-perfecto-y-complejidad}

Imaginemos cien datos experimentales. Una función muy flexible podría construirse para pasar exactamente por todos ellos.

¿Debemos preferirla automáticamente?

No.

Un ajuste perfecto puede ocultar varios problemas:

- sensibilidad excesiva;

- mala extrapolación;

- gran cantidad de parámetros;

- ausencia de interpretación;

- adaptación a irregularidades accidentales;

- falta de conexión con una teoría física.

Todavía no desarrollaremos estos problemas estadísticamente.

Solo fijaremos la diferencia lógica:

$$\boxed{ \text{capacidad de reproducir datos} \neq \text{calidad física automática del modelo}. }$$

### 1.9.13. Volver a §8: ajuste frente a predicción {#fispm-c01-volver-a-8-ajuste-frente-a-predicciuxf3n}

La proposición explica por qué principio 1.13 era necesaria.

Supongamos que elegimos $p_c$ después de conocer todos los datos.

Entonces todos los miembros de la familia pueden ajustarlos perfectamente. Pero en un valor nuevo

$$x_\ast \notin \{x_1,\ldots,x_n\},$$

tenemos:

$$p_c(x_\ast) = p(x_\ast) + c\prod_{i=1}^{n}(x_\ast-x_i).$$

Como ningún factor es necesariamente cero, el resultado depende de $c$.

Distintos modelos compatibles con los mismos datos pueden producir predicciones diferentes. Por eso un nuevo experimento puede ser discriminante.

### 1.9.14. Ejemplo desarrollado 14 --- Dos datos, infinitas predicciones {#fispm-c01-ejemplo-desarrollado-14-dos-datos-infinitas-predicciones}

Retomemos: $(0,0), \qquad (1,1).$ La familia es: $p_c(x) = x+c\,x(x-1).$

Preguntemos qué predice cada modelo para: $x=2.$

Tenemos: $p_c(2) = 2+c\cdot2\cdot1 = 2+2c.$

Si: $c=0,$

obtenemos: $p_0(2)=2.$

Si: $c=1,$

obtenemos: $p_1(2)=4.$

Si: $c=-1,$

obtenemos: $p_{-1}(2)=0.$

Tres funciones indistinguibles en los datos originales producen tres predicciones completamente distintas en el nuevo punto.

Por tanto:

$$\boxed{ \text{nuevo dato} \longrightarrow \text{posible discriminación entre modelos}. }$$

### 1.9.15. Un dato nuevo elimina modelos, pero no necesariamente deja uno solo {#fispm-c01-un-dato-nuevo-elimina-modelos-pero-no-necesariamente-deja-uno-solo}

Supongamos que el nuevo experimento produce: $(2,4).$

Dentro de nuestra familia: $p_c(2)=2+2c.$ Para reproducir $4$ necesitamos: $2+2c=4.$

Entonces: $c=1.$

Parece que hemos seleccionado: $p(x)=x^2.$ Pero debemos ser cuidadosos.

Hemos seleccionado $c=1$ **dentro de esta familia particular**.

Todavía podemos construir otras funciones que coincidan en: $x=0,\quad x=1,\quad x=2$

y difieran en otra parte. De hecho, podemos añadir: $d\,x(x-1)(x-2).$

Por tanto:

$$\boxed{ \text{más datos restringen} \neq \text{datos finitos garantizan unicidad absoluta}. }$$

### 1.9.16. Tres datos y la misma construcción {#fispm-c01-tres-datos-y-la-misma-construcciuxf3n}

Supongamos ahora: $(0,0), \qquad (1,1), \qquad (2,4).$ El polinomio

$$p(x)=x^2$$

reproduce los tres datos.

Construimos: $p_c(x) = x^2 + c\,x(x-1)(x-2).$ En cada punto observado, uno de los factores del producto se anula.

Por tanto:

$$p_c(0)=0,$$

$$p_c(1)=1,$$

$$p_c(2)=4.$$

Pero en

$$x=3$$

obtenemos: $p_c(3) = 9+6c.$

Así, los tres datos tampoco fijan una predicción única para $x=3$.

### 1.9.17. Lo que los datos sí hacen {#fispm-c01-lo-que-los-datos-suxed-hacen}

No debemos ir al extremo contrario.

Los datos finitos no son inútiles.

Cada nuevo dato puede:

- eliminar modelos incompatibles;

- restringir parámetros;

- reducir familias posibles;

- revelar fallos de una aproximación;

- sugerir nuevas regularidades;

- distinguir hipótesis rivales.

La conclusión correcta no es:

> «Los datos no dicen nada».

Es:

> «Los datos no seleccionan una ley sin ayuda de hipótesis, estructura y nuevas pruebas».

### 1.9.18. La subdeterminación es concreta, no retórica {#fispm-c01-la-subdeterminaciuxf3n-es-concreta-no-retuxf3rica}

La palabra **subdeterminación** se utiliza en filosofía de la ciencia para problemas mucho más generales. No necesitamos adoptarla aquí como término técnico. Nuestro resultado es completamente concreto: $\{(x_i,y_i)\}_{i=1}^{n}$

puede ser compatible con una familia infinita de polinomios.

No estamos formulando una tesis metafísica.

Estamos exhibiendo las funciones.

### 1.9.19. El papel del matemático {#fispm-c01-el-papel-del-matemuxe1tico}

Para un lector matemático aparece una lección importante. La demostración de la proposición 1.1 es sencilla. La dificultad física comienza después.

La matemática nos dice:

$$\text{hay no unicidad}.$$

La física debe preguntar:

> ¿qué criterio permite seleccionar una familia relevante?

Es aquí donde vuelven:

- fenómeno;

- sistema;

- estado;

- idealización;

- aproximación;

- teoría;

- interpretación;

- predicción;

- experimento.

El teorema no reemplaza esas decisiones.

Las hace necesarias de manera explícita.

### 1.9.20. El planteamiento correcto del problema {#fispm-c01-el-planteamiento-correcto-del-problema}

Arnold insiste en que una contribución matemática esencial a las ciencias naturales ocurre antes del cálculo rutinario: al formular correctamente la pregunta y elegir el modelo apropiado.[^4]

Proposición 1.1 muestra una razón elemental para esa insistencia. Una tabla finita no contiene instrucciones suficientes para producir automáticamente su continuación. Debemos añadir estructura.

Así:

$$\boxed{ \text{datos} + \text{elección de modelo} \longrightarrow \text{predicciones}. }$$

La elección de modelo no es una operación puramente mecánica escondida dentro del álgebra.

### 1.9.21. Principio metodológico {#fispm-c01-principio-metodoluxf3gico}

**Principio 1.15 --- Ajuste exacto no implica identificación única** Que un modelo reproduzca exactamente un conjunto finito de datos no basta para identificarlo como la única ley compatible. La selección requiere restricciones adicionales, estructura física o nuevas observaciones capaces de discriminar entre alternativas.

Este principio no añade contenido al teorema.

Registra su consecuencia metodológica para el resto del libro.

### 1.9.22. Qué no demuestra proposición 1.1 {#fispm-c01-quuxe9-no-demuestra-p01}

Conviene cerrar varias interpretaciones incorrectas.

#### 1.9.22.1. proposición 1.1 no demuestra que todas las teorías sean igualmente buenas {#fispm-c01-p01-no-demuestra-que-todas-las-teoruxedas-sean-igualmente-buenas}

Los modelos pueden diferir en:

- coherencia;

- simplicidad;

- alcance;

- capacidad predictiva;

- compatibilidad con otros fenómenos;

- estructura teórica;

- adecuación física.

#### 1.9.22.2. proposición 1.1 no demuestra que nunca haya unicidad {#fispm-c01-p01-no-demuestra-que-nunca-haya-unicidad}

Puede haber unicidad **dentro de una clase restringida**.

#### 1.9.22.3. proposición 1.1 no demuestra que la predicción sea imposible {#fispm-c01-p01-no-demuestra-que-la-predicciuxf3n-sea-imposible}

Precisamente las distintas predicciones permiten diseñar experimentos discriminantes.

#### 1.9.22.4. proposición 1.1 no demuestra que la matemática sea insuficiente {#fispm-c01-p01-no-demuestra-que-la-matemuxe1tica-sea-insuficiente}

La matemática es la que hace visible la no unicidad. Lo que no puede hacer, sin premisas adicionales, es inventar qué estructura física debemos imponer.

### 1.9.23. De la no unicidad al diseño experimental {#fispm-c01-de-la-no-unicidad-al-diseuxf1o-experimental}

Supongamos que dos candidatos:

$$f$$

y

$$g$$

coinciden en todos los datos conocidos: $f(x_i)=g(x_i).$ Para distinguirlos debemos buscar algún $x_\ast$ tal que: $f(x_\ast)\neq g(x_\ast).$ Entonces diseñamos una observación en esa condición.

La lógica es:

$$\boxed{ f(x_\ast)\neq g(x_\ast) \longrightarrow \text{experimento potencialmente discriminante}. }$$

Este es el puente entre §9 y §10.

No basta saber que existen muchos modelos.

Debemos aprender **cómo elegir dónde mirar** para separarlos.

### 1.9.24. Ejercicios de §9 {#fispm-c01-ejercicios-de-9}

[]{#fispm-t1-c01-e0023}

**Ejercicio 1.23 --- Demostrar la familia de no unicidad.**

Sean $x_1,\ldots,x_n$ distintos y supón que

$$p(x_i)=y_i$$

para todo $i$.

Define

$$q(x) = p(x) + 7\prod_{i=1}^{n}(x-x_i).$$

Demuestra directamente que: $q(x_i)=y_i$

para todo $i$.

**Solución.**

Fijemos un índice $j$. Por definición: $q(x_j) = p(x_j) + 7\prod_{i=1}^{n}(x_j-x_i).$

Como: $p(x_j)=y_j,$

tenemos: $q(x_j) = y_j + 7\prod_{i=1}^{n}(x_j-x_i).$ En el producto aparece el factor: $x_j-x_j=0.$ Por tanto: $\prod_{i=1}^{n}(x_j-x_i)=0.$ Luego: $q(x_j)=y_j.$

Como $j$ era arbitrario:

$$\boxed{ q(x_i)=y_i \quad \text{para todo }i. }$$

[]{#fispm-t1-c01-e0024}

La constante $7$ no desempeña ningún papel especial. Podría sustituirse por cualquier $c$. **Ejercicio 1.24 --- Dos puntos, infinitas leyes.**

Considera los datos: $(0,1), \qquad (1,2).$

1.  Encuentra un polinomio lineal $p$ que pase por ambos puntos.

2.  Construye una familia $p_c$ de polinomios que pase por los mismos puntos.

3.  Calcula las predicciones para $x=2$ cuando $c=0$, $c=1$ y $c=-1$.

4.  Explica qué demuestra el ejercicio.

**Solución.**

[]{#polinomio-lineal}

#### 1.9.24.0. 1. Polinomio lineal {#fispm-c01-polinomio-lineal .unnumbered}

La recta: $p(x)=x+1$

satisface:

$$p(0)=1,$$

$$p(1)=2.$$

[]{#familia}

#### 1.9.24.0. 2. Familia {#fispm-c01-familia .unnumbered}

El factor que se anula en los puntos observados es: $x(x-1).$ Por tanto: $p_c(x) = x+1+c\,x(x-1).$ Para $x=0$: $p_c(0)=1.$ Para $x=1$: $p_c(1)=2.$

[]{#predicción-en-x2}

#### 1.9.24.1. 3. Predicción en $x=2$ {#fispm-c01-predicciuxf3n-en-x2}

Tenemos: $p_c(2) = 3+2c.$

Entonces:

$$p_0(2)=3,$$

$$p_1(2)=5,$$

$$p_{-1}(2)=1.$$

[]{#interpretación}

#### 1.9.24.1. 4. Interpretación {#fispm-c01-interpretaciuxf3n .unnumbered}

Los datos originales no distinguen entre estas funciones. Pero un nuevo dato en $x=2$ podría hacerlo.

Por tanto:

[]{#fispm-t1-c01-e0025}

$$\boxed{ \text{mismo ajuste} \not\Rightarrow \text{misma predicción}. }$$ **Ejercicio 1.25 --- Tres puntos y una nueva familia.**

Considera los datos: $(0,1), \qquad (1,1), \qquad (2,3).$ El polinomio

$$p(x)=x^2-x+1$$

es compatible con ellos.

1.  Verifica los tres datos.

2.  Construye la familia

$$p_c(x) = p(x)+c\,x(x-1)(x-2).$$

1.  Demuestra que todos los miembros de la familia conservan los tres datos.

2.  Calcula $p_c(3)$.

3.  Si una nueva observación produce $(3,7)$, determina qué valor de $c$ queda seleccionado **dentro de esta familia**.

4.  Explica por qué ese nuevo dato todavía no demuestra unicidad absoluta entre todas las funciones posibles.

**Solución.**

[]{#verificación}

#### 1.9.24.1. 1. Verificación {#fispm-c01-verificaciuxf3n .unnumbered}

Para $x=0$: $p(0)=1.$ Para $x=1$: $p(1)=1-1+1=1.$ Para $x=2$: $p(2)=4-2+1=3.$ Por tanto, $p$ reproduce los tres datos.

[]{#familia-1}

#### 1.9.24.1. 2. Familia {#fispm-c01-familia-1 .unnumbered}

Definimos: $p_c(x) = x^2-x+1 + c\,x(x-1)(x-2).$

[]{#conservación-de-los-datos}

#### 1.9.24.1. 3. Conservación de los datos {#fispm-c01-conservaciuxf3n-de-los-datos .unnumbered}

En $x=0$, el factor $x$ es cero. En $x=1$, el factor $(x-1)$ es cero. En $x=2$, el factor $(x-2)$ es cero.

Por tanto:

$$p_c(0)=1,$$

$$p_c(1)=1,$$

$$p_c(2)=3$$

para todo $c$.

[]{#valor-en-x3}

#### 1.9.24.2. 4. Valor en $x=3$ {#fispm-c01-valor-en-x3}

Tenemos: $p(3) = 9-3+1 = 7.$

Además: $3(3-1)(3-2) = 3\cdot2\cdot1 = 6.$

Luego: $p_c(3) = 7+6c.$

[]{#nuevo-dato}

#### 1.9.24.2. 5. Nuevo dato {#fispm-c01-nuevo-dato .unnumbered}

Si observamos: $p_c(3)=7,$

entonces: $7+6c=7.$

Así: $6c=0$

y:

$$\boxed{c=0}.$$

Dentro de esta familia queda seleccionado el polinomio: $p(x)=x^2-x+1.$

[]{#por-qué-no-hay-unicidad-absoluta}

#### 1.9.24.2. 6. Por qué no hay unicidad absoluta {#fispm-c01-por-quuxe9-no-hay-unicidad-absoluta .unnumbered}

Ahora tenemos cuatro datos.

Podemos modificar nuevamente $p$ mediante un término que se anule en los cuatro valores: $d\,x(x-1)(x-2)(x-3).$ Por tanto: $p_d(x) = p(x) + d\,x(x-1)(x-2)(x-3)$

reproduce los cuatro datos para cualquier $d$. La nueva observación restringió la familia anterior, pero los datos siguen siendo finitos.

$$\boxed{ \text{más evidencia} \Rightarrow \text{más restricciones}, }$$

pero no:

$$\boxed{ \text{evidencia finita} \Rightarrow \text{unicidad entre todas las funciones}. }$$

### 1.9.25. Síntesis {#fispm-c01-suxedntesis-6}

La primera proposición formal del capítulo establece:

$$\boxed{ p_c(x) = p(x) + c\prod_{i=1}^{n}(x-x_i) }$$

y:

$$\boxed{ p_c(x_i)=p(x_i)=y_i }$$

para todos los datos observados.

Por tanto:

$$\boxed{ \text{datos finitos} \not\Rightarrow \text{ley funcional única}. }$$

La consecuencia metodológica es principio 1.15:

$$\boxed{ \text{ajuste exacto} \not\Rightarrow \text{identificación única}. }$$

Pero esto abre una pregunta constructiva.

Si muchas funciones son compatibles con los mismos datos, ¿cómo elegimos entre ellas?

La respuesta no puede ser simplemente:

> «escogemos la que nos gusta».

Necesitamos criterios físicos y matemáticos:

- estructura;

- simplicidad relevante;

- simetría;

- mecanismo;

- compatibilidad con teorías;

- régimen;

- capacidad de producir nuevas predicciones;

- experimentos discriminantes.

Ése será el objeto de (§[1.10](#fispm-c01-cuxf3mo-se-elige-entre-modelos-compatibles-con-los-datos)).

[]{#cómo-se-elige-entre-modelos-compatibles-con-los-datos}

[]{#fispm-t1-c01-s10}

[]{#fpm-i-01-s10}

## 1.10. Cómo se elige entre modelos compatibles con los datos {#fispm-c01-cuxf3mo-se-elige-entre-modelos-compatibles-con-los-datos}

[]{#después-de-la-no-unicidad}

### 1.10.1. Después de la no unicidad {#fispm-c01-despuuxe9s-de-la-no-unicidad}

En §9 demostramos que, si un polinomio $p$ reproduce una colección finita de datos

$$(x_1,y_1),\ldots,(x_n,y_n),$$

entonces toda la familia

$$p_c(x) = p(x) + c\prod_{i=1}^{n}(x-x_i)$$

reproduce exactamente esos mismos datos.

Por tanto:

$$\boxed{ \text{ajuste exacto} \not\Rightarrow \text{identificación única}. }$$

Ahora aparece la pregunta físicamente interesante:

> Si varios modelos son compatibles con los datos disponibles, ¿cómo elegimos entre ellos?

Una primera respuesta sería:

> obteniendo más datos.

Eso es correcto, pero incompleto.

Antes de medir algo nuevo debemos decidir **qué** medir. Si dos modelos coinciden en todas las condiciones que volvemos a observar, el nuevo experimento no los distinguirá.

[]{#fig:I-01-R03}

![**Figura 1.6.** El residuo es la diferencia entre la observación y la predicción. Un patrón oscilatorio persistente puede señalar estructura que el modelo no representa. La curva es un esquema de diagnóstico, no una prueba estadística de rechazo. Véase §[1.10](#fispm-c01-cuxf3mo-se-elige-entre-modelos-compatibles-con-los-datos).](/assets/books/fispm/v04/I-01-R03.svg "fig:"){.fpm-v04-figure fig-alt="Los residuos conservan información" width="343px" fig-cap=""}

La selección de modelos exige combinar:

- evidencia;

- estructura física;

- teoría;

- economía de hipótesis;

- régimen de validez;

- capacidad explicativa;

- nuevas predicciones;

- diseño experimental. Sería cómodo disponer de una regla:

$$\text{modelo A} > \text{modelo B}$$

que pudiera decidirse siempre mediante un solo número.

No adoptaremos tal regla. En distintas situaciones pueden importar criterios diferentes.

Un modelo puede ser:

- más simple;

- más preciso;

- más general;

- más fácil de medir;

- más conectado con una teoría;

- más explicativo;

- más robusto;

- más útil para una pregunta concreta.

Y esas ventajas pueden entrar en tensión.

Por tanto:

$$\boxed{ \text{selección de modelos} \neq \text{aplicación mecánica de una única regla}. }$$

La comparación debe conservar visible **para qué pregunta**, **con qué datos** y **en qué régimen** se está eligiendo. **Definición operativa 1.26 --- Criterio de selección de modelos** Un **criterio de selección de modelos** es una propiedad, condición o prueba utilizada para comparar modelos candidatos respecto de una pregunta física, una evidencia disponible y un régimen de aplicación determinados.

La definición es deliberadamente contextual. Un criterio que resulta decisivo para una tarea puede ser secundario para otra. Por ejemplo, si queremos una predicción de baja precisión en un régimen estrecho, un modelo sencillo puede ser suficiente.

Si queremos comprender un nuevo fenómeno fuera de ese régimen, la misma descripción puede dejar de ser adecuada. Recordemos principio 1.2 y principio 1.11:

- la adecuación es relativa a una pregunta;

- la suficiencia depende de la tarea.

No existe «el mejor modelo» sin contexto.

Puede existir:

> el modelo más adecuado para estimar cierta cantidad con determinada precisión en cierto régimen.

Un modelo muy detallado puede ser innecesario para una pregunta.

Uno muy simple puede ser insuficiente para otra.

Por tanto:

**Principio 1.16 --- La preferencia entre modelos es relativa a la tarea** Comparar modelos exige declarar la pregunta, la evidencia y el régimen. Una preferencia metodológica no constituye un orden absoluto entre modelos independiente de su uso.

### 1.10.2. Tres capas de comparación {#fispm-c01-tres-capas-de-comparaciuxf3n}

La comparación entre modelos puede organizarse en tres capas.

[]{#coherencia-mínima}

#### 1.10.2.1. Coherencia mínima {#fispm-c01-coherencia-muxednima}

Antes de comparar virtudes, debemos eliminar candidatos que fallan requisitos básicos.

Podemos pensar esta primera capa como una serie de filtros.

[]{#filtro-1-coherencia-matemática-interna}

##### Filtro 1 --- Coherencia matemática interna {#fispm-c01-filtro-1-coherencia-matemuxe1tica-interna}

El modelo no debe contradecir sus propias definiciones, restricciones y condiciones. Si declara: $s\in\mathcal S$

pero luego exige un estado que no pertenece a $\mathcal S$, el problema es interno.

No necesitamos ningún experimento para detectarlo.

[]{#filtro-2-compatibilidad-con-la-evidencia-relevante}

##### Filtro 2 --- Compatibilidad con la evidencia relevante {#fispm-c01-filtro-2-compatibilidad-con-la-evidencia-relevante}

Si un modelo predice algo incompatible con observaciones fiables dentro del régimen que afirma describir, necesita revisión.

[]{#filtro-3-interpretación-física-suficiente}

##### Filtro 3 --- Interpretación física suficiente {#fispm-c01-filtro-3-interpretaciuxf3n-fuxedsica-suficiente}

Los símbolos que se comparan con datos deben tener una interpretación y una conexión observacional.

[]{#filtro-4-régimen-pertinente}

##### Filtro 4 --- Régimen pertinente {#fispm-c01-filtro-4-ruxe9gimen-pertinente}

No debemos juzgar un modelo usando una condición que él mismo no pretende describir sin antes preguntar si estamos extendiéndolo legítimamente. Estos filtros no garantizan que el modelo sea correcto. Solo impiden mantener candidatos que ya fallan requisitos elementales.

#### 1.10.2.2. Adecuación y estructura {#fispm-c01-adecuaciuxf3n-y-estructura}

Una vez superados los filtros mínimos, pueden importar varios criterios que no forman un algoritmo universal:

  Criterio                 Pregunta de control
  ------------------------ ----------------------------------------------------------------------------------------
  economía de estructura   ¿cuánta estructura independiente se introduce para obtener las consecuencias?
  integración teórica      ¿cómo se relaciona con conocimiento ya bien establecido en el mismo régimen?
  poder explicativo        ¿qué dependencias, mecanismos o estructuras comunes hace visibles?
  alcance                  ¿qué diversidad de fenómenos organiza sin ocultar su régimen?
  robustez                 ¿la conclusión depende críticamente de ajustes irrelevantes o excesivamente delicados?
  acceso observacional     ¿cómo se conectan sus predicciones con procedimientos `[``OBS``]`?

La simplicidad es un criterio metodológico, no una demostración de verdad. Si dos modelos describen igual de bien los fenómenos relevantes, puede ser razonable preferir el que requiere menos estructura no justificada. Pero debemos formular esta idea con cuidado.

**Más simple** no significa necesariamente:

- fórmula más corta;

- menos símbolos impresos;

- cálculo más fácil;

- menor número de páginas.

Una expresión compacta puede ocultar muchas hipótesis. Una expresión larga puede desarrollar explícitamente una estructura sencilla.

La pregunta útil es:

> ¿cuánta estructura independiente debemos introducir para obtener las consecuencias observadas?

Esta idea suele llamarse **parsimonia**. La utilizaremos como criterio metodológico, no como ley lógica de la naturaleza. Un modelo no vive aislado.

Puede compartir estructuras con teorías que ya explican otros fenómenos. Si un candidato requiere abandonar relaciones bien contrastadas en el mismo régimen, ese costo debe ser visible. En cambio, un modelo que surge naturalmente de un marco ya exitoso puede tener una ventaja metodológica.

Esto tampoco constituye una prueba automática. Una teoría nueva puede precisamente mostrar que un marco anterior era limitado.

La regla correcta es más modesta:

$$\boxed{ \text{compatibilidad teórica amplia} = \text{evidencia estructural relevante}, }$$

no:

$$\boxed{ \text{compatibilidad con lo conocido} = \text{imposibilidad de revisión}. }$$ En §8 distinguimos predecir de explicar.

Dos modelos pueden reproducir el mismo dato y, sin embargo, uno puede mostrar por qué ocurre el patrón. Por ejemplo, una relación ajustada puede decir: $Y=f(X).$

Otro modelo puede además mostrar que esa forma surge de:

- una simetría;

- una restricción;

- una interacción;

- una estructura común a varios fenómenos.

El segundo no es mejor únicamente por contar una historia más atractiva. Su explicación gana valor si organiza consecuencias que pueden ponerse a prueba. Por eso el poder explicativo está estrechamente ligado a la capacidad de generar nuevas preguntas. Un modelo que explica varios fenómenos con una misma estructura puede ser preferible a una colección de reglas independientes.

Pero mayor alcance no significa validez ilimitada.

Debemos conservar: $\mathcal R.$ Un modelo puede unificar mucho dentro de cierto régimen y fallar fuera de él.

La pregunta correcta es:

> ¿qué diversidad de fenómenos explica con la misma estructura, y bajo qué condiciones?

No:

> ¿puede aplicarse sin restricciones a todo? Supongamos que una conclusión depende de que un parámetro tenga exactamente el valor:

$$a=1.0000000000.$$

Si un cambio minúsculo de $a$ destruye completamente el fenómeno, debemos preguntarnos si el mecanismo propuesto es físicamente estable frente a las variaciones inevitables de preparación y modelización. No desarrollaremos todavía una teoría matemática de estabilidad.

Usaremos **robustez** en sentido cualitativo:

> una conclusión es robusta si no depende críticamente de elecciones irrelevantes o ajustes excesivamente delicados para el fenómeno estudiado.

La falta de robustez no invalida automáticamente un modelo.

Algunos fenómenos físicos son genuinamente sensibles. Pero, si la sensibilidad es esencial, el modelo debe hacerla visible en lugar de esconderla. Un modelo puede introducir una cantidad que matemáticamente está perfectamente definida.

Pero si la comparación con el mundo depende de ella, necesitamos preguntar:

> ¿cómo se observa?

En términos de §5: $\mathfrak I_{\mathcal M}$

debe ser suficientemente explícito. Y en términos de §6: $[\mathrm{OBS}]$

debe conectar la cantidad con un procedimiento. Un modelo cuyas predicciones no poseen ninguna conexión observacional accesible puede seguir teniendo interés teórico. Pero no podemos contar esas predicciones como contrastes experimentales realizados.

#### 1.10.2.3. Fecundidad predictiva {#fispm-c01-fecundidad-predictiva}

El criterio más fuerte aparece cuando los modelos, compatibles con los datos actuales, divergen en una situación todavía no observada. Volvamos a §9. Supongamos: $f(x_i)=g(x_i)$

para todos los puntos medidos.

Los modelos son indistinguibles en la evidencia disponible. La estrategia natural es buscar un valor $x_\ast$ tal que: $f(x_\ast)\neq g(x_\ast).$ Entonces los modelos producen predicciones rivales. Si podemos realizar una observación en $x_\ast$, obtenemos una prueba potencialmente discriminante.

Esta idea merece una definición propia.

**Definición operativa 1.27 --- Experimento discriminante** Un **experimento discriminante** entre dos o más modelos es un experimento diseñado en condiciones donde los modelos candidatos producen consecuencias observacionales distinguibles, de modo que el resultado pueda favorecer algunos candidatos frente a otros.

La palabra **distinguibles** importa.

No basta que las fórmulas sean diferentes. La diferencia debe poder conectarse, mediante `[``OBS``]`, con una observación capaz de separarlas. Este principio cambia la estrategia experimental.

Si queremos distinguir $M_1$ y $M_2$, no conviene repetir indefinidamente condiciones donde: $P_1=P_2.$ Debemos buscar, cuando sea posible: $P_1\neq P_2.$

**Principio 1.17 --- Para discriminar modelos, buscar divergencia predictiva** Si varios modelos son compatibles con los datos existentes, una prueba informativa debe buscar condiciones accesibles dentro de sus regímenes pertinentes en las que sus predicciones observables difieran.

El principio contiene tres restricciones:

1.  **condiciones accesibles**;

2.  **regímenes pertinentes**;

3.  **diferencias observables**.

Una diferencia puramente formal que no puede medirse no basta todavía.

### 1.10.3. Diseñar una prueba discriminante {#fispm-c01-diseuxf1ar-una-prueba-discriminante}

En §9 vimos los datos: $(0,0), \qquad (1,1).$

Consideremos: $M_1:\quad f(x)=x,$

y: $M_2:\quad g(x)=x^2.$

Ambos reproducen:

$$f(0)=g(0)=0,$$

$$f(1)=g(1)=1.$$

Repetir observaciones únicamente en $x=0$ y $x=1$ no añade capacidad discriminante.

Probemos: $x_\ast=\frac12.$

Entonces: $f\left(\frac12\right) = \frac12,$

mientras: $g\left(\frac12\right) = \frac14.$

Las predicciones son diferentes. Por tanto, una observación en: $x=\frac12$

puede distinguir los modelos, siempre que el procedimiento experimental sea capaz de separar una salida próxima a $1/2$ de una próxima a $1/4$. En §9 también usamos: $x=2.$ Allí las predicciones eran distintas.

¿Por qué ahora preferimos: $x=\frac12?$

Porque los datos originales estaban en:

$$x=0$$

y: $x=1.$ Una medición intermedia puede mantenerse más cerca del régimen ya explorado.

Ir directamente a:

$$x=2$$

podría introducir una dificultad adicional:

> ¿estamos extrapolando fuera del dominio donde ambos modelos eran plausibles?

Un buen experimento discriminante intenta cambiar **lo necesario para separar los modelos** sin introducir simultáneamente nuevas ambigüedades evitables. Supongamos ahora:

$$f(x_\ast)=1.000000,$$

$$g(x_\ast)=1.000001.$$

Matemáticamente: $f(x_\ast)\neq g(x_\ast).$ Pero si el instrumento solo permite distinguir diferencias del orden de: $0.01,$

el experimento no separará operativamente ambos modelos.

No desarrollaremos aquí teoría de errores.

Solo fijamos la lógica:

La capacidad del procedimiento `[``OBS``]` forma parte del diseño. Supongamos tres modelos: $M_1,\quad M_2,\quad M_3.$

En una condición $C$ predicen:

$$P_1=a,$$

$$P_2=b,$$

$$P_3=b.$$

Si el experimento favorece $b$, podemos debilitar $M_1$.

Pero todavía no distinguimos entre:

$$M_2$$

y: $M_3.$ El experimento fue informativo aunque no produjera una selección única.

Así:

$$\boxed{ \text{discriminación} \neq \text{decisión final garantizada}. }$$

La investigación puede proceder por sucesivas particiones de la familia de modelos. Imaginemos tres candidatos que coinciden en los datos iniciales.

[]{#primera-prueba}

#### 1.10.3.1. Primera prueba {#fispm-c01-primera-prueba}

Elegimos una condición $C_1$ donde:

$$M_1$$

predice algo diferente de: $M_2,\ M_3.$ El resultado descarta o debilita $M_1$.

[]{#segunda-prueba}

#### 1.10.3.2. Segunda prueba {#fispm-c01-segunda-prueba}

Ahora buscamos una condición $C_2$ donde:

$$M_2$$

y:

$$M_3$$

difieran.

La selección de experimentos se vuelve adaptativa:

$$\boxed{\begin{gathered} \text{datos} \to \text{familia de candidatos}\\[2pt]\Downarrow\\[2pt]\text{prueba discriminante} \to \text{familia reducida}\\[2pt]\Downarrow\\[2pt]\text{nueva prueba}. \end{gathered}}$$

No necesitamos todavía una teoría estadística para comprender esta arquitectura lógica. Si elegimos puntos de prueba al azar, quizá los modelos sigan coincidiendo. La estructura física puede guiarnos.

Dos modelos pueden diferir especialmente:

- cuando una idealización deja de ser adecuada;

- cerca de una frontera del régimen;

- cuando cambia una simetría;

- cuando un efecto antes despreciado se vuelve importante;

- al variar un parámetro que afecta de modo diferente a los mecanismos rivales.

La teoría no solo produce predicciones.

También ayuda a diseñar **experimentos informativos**. Supongamos que $M_1$:

- requiere menos hipótesis independientes;

- se integra con una teoría más amplia;

- explica varios fenómenos;

- produce nuevas predicciones acertadas.

Mientras $M_2$:

- reproduce solo los datos originales;

- necesita varios ajustes independientes;

- no produce consecuencias nuevas.

Es razonable preferir $M_1$.

Pero la forma correcta de expresarlo es:

> «La evidencia y la estructura disponibles favorecen $M_1$».

No:

> «$M_1$ ha sido demostrado como descripción final de la naturaleza».

La selección física es revisable. Los criterios pueden entrar en tensión; ni la complejidad ni la sencillez merecen premio automático:

Consideremos dos candidatos.

[]{#modelo-a}

#### 1.10.3.3. Modelo A {#fispm-c01-modelo-a}

- muy simple;

- fácil de calcular;

- válido solo en un régimen pequeño.

[]{#modelo-b}

#### 1.10.3.4. Modelo B {#fispm-c01-modelo-b}

- más complejo;

- explica varios regímenes;

- requiere más estructura matemática.

¿Cuál es mejor?

La pregunta está incompleta. Para una estimación rápida dentro del régimen pequeño, A puede ser preferible. Para estudiar la transición entre regímenes, B puede ser necesario.

Esto refuerza:

$$\boxed{ \text{preferencia} = \text{relación entre modelo, pregunta y régimen}. }$$ También debemos evitar el sesgo contrario.

Un modelo no mejora automáticamente al agregar:

- más parámetros;

- más mecanismos;

- más términos;

- más variables;

- más detalle microscópico.

Cada nueva estructura debe responder:

> ¿qué problema resuelve?

Si una ampliación no cambia ninguna predicción relevante, no explica ningún fenómeno nuevo y no extiende el régimen, puede ser innecesaria para la tarea actual.

Esto recupera principio 1.9:

> **modelo mínimo suficiente**. Pero tampoco debemos eliminar estructura necesaria solo para obtener una fórmula elegante.

Si dos efectos observados requieren mecanismos distintos, un modelo que ignora uno de ellos puede ser más corto y peor.

La economía debe entenderse como:

$$\boxed{ \text{no introducir estructura innecesaria} }$$

y no como:

$$\boxed{ \text{eliminar estructura necesaria para que la fórmula sea corta}. }$$ La selección de modelos debe conservar tres preguntas: ¿es coherente?, ¿es adecuada para la tarea?, ¿produce nuevas consecuencias capaces de ser contrastadas?

Podemos organizar los criterios en tres grupos.

[]{#coherencia}

#### 1.10.3.4. 1. Coherencia {#fispm-c01-coherencia .unnumbered}

Preguntas:

- ¿el modelo es matemáticamente consistente?;

- ¿sus definiciones y condiciones son compatibles?;

- ¿su interpretación es clara?

[]{#adecuación}

#### 1.10.3.4. 2. Adecuación {#fispm-c01-adecuaciuxf3n .unnumbered}

Preguntas:

- ¿reproduce los fenómenos relevantes?;

- ¿funciona en el régimen declarado?;

- ¿las magnitudes pueden conectarse con observaciones?

[]{#fecundidad}

#### 1.10.3.4. 3. Fecundidad {#fispm-c01-fecundidad .unnumbered}

Preguntas:

- ¿produce predicciones nuevas?;

- ¿explica varios fenómenos?;

- ¿sugiere experimentos?;

- ¿organiza relaciones antes separadas?;

- ¿muestra dónde debería fallar?

Un modelo científicamente potente no solo encaja lo ya observado.

También abre trabajo nuevo. Puede parecer extraño valorar un modelo porque declara sus límites. Pero un modelo que especifica: $\mathcal R$

y anticipa dónde una aproximación debe dejar de funcionar es más informativo que uno que simplemente se aplica sin control.

Una teoría física madura suele permitir preguntar:

> ¿qué parámetro controla esta aproximación?

y:

> ¿qué fenómeno aparecerá cuando deje de ser pequeño?

Por eso la capacidad de delimitar el propio fracaso puede ser parte de la calidad del modelo. Podemos ahora reunir el proceso:

$$\boxed{\begin{gathered} \text{fenómeno} \to \text{modelos candidatos}\\[2pt]\Downarrow\\[2pt]\text{filtros} \to \text{criterios comparativos}\\[2pt]\Downarrow\\[2pt]\text{predicciones divergentes} \to \text{experimento}\\[2pt]\Downarrow\\[2pt]\text{revisión}. \end{gathered}}$$

El resultado no es necesariamente un modelo definitivo.

Puede ser:

- descartar uno;

- restringir otro;

- modificar una aproximación;

- descubrir un nuevo régimen;

- formular un tercer candidato.

La selección y la revisión forman un proceso continuo. **Ficha FPM --- Comparación y discriminación de modelos** 1. **Pregunta:** ¿qué queremos explicar o predecir? 2. **Candidatos:** ¿qué modelos se comparan? 3. **Datos compartidos:** ¿qué evidencia reproducen todos? 4. **Coherencia:** ¿algún candidato falla internamente? 5. **Interpretación:** ¿qué significa físicamente cada formalismo? 6. **Régimen:** ¿en qué $\mathcal R$ pretende funcionar cada modelo? 7. **Hipótesis:** ¿qué estructura independiente introduce cada uno? 8. **Explicación:** ¿qué mecanismo o estructura hace responsable del fenómeno? 9. **Predicciones rivales:** ¿dónde difieren? 10. **Observabilidad:** ¿esa diferencia puede medirse? 11. **Prueba:** ¿qué experimento discrimina mejor? 12. **Resultado:** ¿qué modelos quedan favorecidos, debilitados o todavía indistinguibles? **Ejercicio.**

[]{#fispm-t1-c01-e0026}

**Ejercicio 1.26 --- Diseñar un experimento discriminante.**

Se han observado únicamente los datos: $(0,0), \qquad (1,1).$

Dos modelos candidatos son:

$$M_1:\quad y=x,$$

$$M_2:\quad y=x^2.$$

Responde:

1.  Verifica que ambos modelos reproducen los datos conocidos.

2.  Explica por qué repetir exactamente las mismas condiciones $x=0$ y $x=1$ no discrimina los modelos.

3.  Propón un valor $x_\ast$ dentro del intervalo $[0,1]$ donde las predicciones difieran.

4.  Calcula ambas predicciones.

5.  Explica qué debe cumplir el procedimiento `[``OBS``]` para que el experimento sea realmente discriminante.

6.  Supón que la observación nueva es compatible con $y=1/4$. ¿Qué modelo queda favorecido dentro de este par?

7.  Explica por qué el resultado no demuestra que el modelo favorecido sea la única función posible compatible con todos los datos.

8.  Indica al menos dos criterios adicionales, distintos del nuevo dato, que sería razonable examinar antes de adoptar el modelo para una aplicación física. **Solución.**

[]{#datos-conocidos}

##### 1. Datos conocidos {#fispm-c01-datos-conocidos}

Para $M_1$:

$$M_1(0)=0,$$

$$M_1(1)=1.$$

Para $M_2$:

$$M_2(0)=0^2=0,$$

$$M_2(1)=1^2=1.$$

Por tanto:

$$\boxed{ M_1\sim D \quad \text{y} \quad M_2\sim D. }$$

##### 2. Repetir los extremos {#fispm-c01-repetir-los-extremos}

En:

$$x=0$$

y: $x=1,$

ambos modelos producen exactamente las mismas predicciones. Por tanto, aunque mejoremos mucho la repetición experimental, esas condiciones no separan la estructura de los candidatos. Necesitamos una condición donde: $M_1(x_\ast)\neq M_2(x_\ast).$

##### 3. Elección de $x_\ast$ {#fispm-c01-elecciuxf3n-de-x_ast}

Una elección sencilla es: $x_\ast=\frac12.$

Está dentro del intervalo ya explorado entre los dos datos originales.

##### 4. Predicciones {#fispm-c01-predicciones}

Para $M_1$: $M_1\left(\frac12\right) = \frac12.$

Para $M_2$:

$$M_2\left(\frac12\right) = \left(\frac12\right)^2 = \frac14.$$

Así:

$$\boxed{ P_1=\frac12, \qquad P_2=\frac14. }$$

##### 5. Papel de `[``OBS``]` {#fispm-c01-papel-de-obs}

No basta que: $\frac12\neq\frac14.$ El procedimiento experimental debe poder distinguir resultados compatibles con ambos valores.

Esto requiere una conexión observacional:

$$[\mathrm{OBS}] \qquad y \longleftrightarrow \text{procedimiento de medición}$$

capaz de separar las dos predicciones con la precisión pertinente.

##### 6. Resultado $y=1/4$ {#fispm-c01-resultado-y14}

Si la nueva observación es compatible con: $y=\frac14,$

entonces, dentro del par considerado, queda favorecido:

$$\boxed{M_2}.$$

El modelo $M_1$ predice: $y=\frac12,$

por lo que la nueva evidencia lo contradice bajo las condiciones y el régimen asumidos.

##### 7. Por qué no hay unicidad absoluta {#fispm-c01-por-quuxe9-no-hay-unicidad-absoluta-1}

Los tres datos:

$$(0,0), \qquad \left(\frac12,\frac14\right), \qquad (1,1)$$

siguen siendo finitos. Por proposición 1.1, una vez conocido un polinomio compatible podemos construir otros añadiendo un término que se anule en los tres valores observados.

Por ejemplo:

$$q_c(x) = x^2 + c\,x \left(x-\frac12\right) (x-1).$$

Todos los $q_c$ conservan los tres datos.

Por tanto:

$$\boxed{ \text{favorecer }M_2\text{ frente a }M_1 \neq \text{demostrar unicidad absoluta de }M_2. }$$

##### 8. Criterios adicionales {#fispm-c01-criterios-adicionales}

Entre otros, podríamos examinar:

- qué estructura física justifica cada relación;

- qué régimen de validez declara;

- cuántas hipótesis independientes requiere;

- si se integra con una teoría más amplia;

- si explica otros fenómenos;

- qué nuevas predicciones produce;

- si sus conclusiones son robustas;

- cómo se conecta cada variable con observaciones.

La selección no termina con un único dato.

### 1.10.4. Síntesis {#fispm-c01-suxedntesis-7}

§9 estableció:

$$\boxed{ \text{datos finitos} \not\Rightarrow \text{modelo único}. }$$

§10 añade:

$$\boxed{ \text{no unicidad} \longrightarrow \text{comparación estructurada} + \text{nuevas pruebas}. }$$

Los criterios principales son:

- coherencia;

- adecuación al fenómeno;

- interpretación;

- régimen;

- economía;

- integración teórica;

- poder explicativo;

- robustez;

- fecundidad predictiva.

Pero ninguno reemplaza por sí solo al contraste.

La estrategia experimental más importante queda resumida por el principio 1.17:

$$\boxed{ \text{si los modelos coinciden donde ya miramos, buscar dónde predicen cosas distintas}. }$$

Esto nos conduce al siguiente problema.

Incluso después de elegir un modelo razonable debemos saber:

> ¿hasta dónde podemos confiar en él?

Ése será el objeto de (§[1.11](#fispm-c01-dominio-de-validez-y-teoruxedas-efectivas)).

[]{#dominio-de-validez-y-teorías-efectivas}

[]{#fispm-t1-c01-s11}

[]{#fpm-i-01-s11}

## 1.11. Dominio de validez y teorías efectivas {#fispm-c01-dominio-de-validez-y-teoruxedas-efectivas}

[]{#dominio-matemático-y-dominio-físico}

### 1.11.1. Dominio matemático y dominio físico {#fispm-c01-dominio-matemuxe1tico-y-dominio-fuxedsico}

Supongamos que un modelo contiene una relación matemática

$$Y=f(X).$$

La función puede estar perfectamente definida para muchos valores de $X$.

Puede incluso ocurrir que el problema matemático asociado tenga una solución exacta. Pero de ahí no se sigue que la relación represente físicamente al sistema para todos esos valores.

[]{#fig:I-01-R04}

![**Figura 1.7.** Las condiciones de régimen seleccionan una parte del espacio de parámetros. Extender una fórmula fuera de esa región exige una justificación nueva. La frontera vertical es esquemática y no representa un umbral universal. Véase §[1.11](#fispm-c01-dominio-de-validez-y-teoruxedas-efectivas).](/assets/books/fispm/v04/I-01-R04.svg "fig:"){.fpm-v04-figure fig-alt="El dominio pertenece al modelo" width="341px" fig-cap=""}

Esta es una de las diferencias más importantes entre:

$$\text{dominio matemático}$$

y:

$$\text{dominio físico de aplicación}.$$

Una expresión puede tener sentido matemático donde el modelo ya no tiene sentido físico.

Por tanto:

$$\boxed{ \text{estar definido matemáticamente} \neq \text{ser físicamente válido}. }$$ Desde §5 hemos escrito el modelo como:

$$\mathcal M = (\mathcal S,X,\theta,\mathcal L,I,B,\mathcal R),$$

acompañado de: $\mathfrak I_{\mathcal M}.$

Hasta ahora $\mathcal R$ aparecía como uno de los componentes de la ficha. A partir de esta sección debemos leerlo como una restricción activa.

No basta preguntar:

> «¿Qué predice el modelo?»

Debemos preguntar:

> «¿Bajo qué condiciones afirma poder predecirlo?»

Así, una predicción físicamente completa tiene la forma conceptual:

$$\boxed{ \text{modelo} + \text{condición perteneciente a }\mathcal R \longrightarrow \text{predicción físicamente interpretable}. }$$ **Definición operativa 1.28 --- Dominio de validez físico** El **dominio de validez físico** de un modelo, una aproximación o una teoría aplicada es el conjunto de condiciones, escalas, clases de sistemas y preguntas para las cuales se considera que sus representaciones y predicciones alcanzan la adecuación requerida.

Esta definición contiene una palabra importante:

> **requerida**.

Un modelo puede ser adecuado para una precisión y no para otra.

Puede ser adecuado para una pregunta cualitativa y no para una medición extremadamente precisa.

Puede describir bien una escala y omitir fenómenos decisivos en otra.

Por eso el dominio de validez no es una etiqueta binaria del tipo:

$$\text{verdadero/falso}.$$

Es una declaración de alcance. Supongamos: $f:\mathbb R\to\mathbb R.$

Matemáticamente podemos evaluar: $f(x)$

para cualquier: $x\in\mathbb R.$ Pero el modelo físico podría haber sido construido solo para: $x\in\mathcal R.$ Entonces: $x_\ast\notin\mathcal R$

no impide necesariamente calcular: $f(x_\ast).$ Lo que impide es interpretar automáticamente ese cálculo como una predicción confiable del sistema real.

Así:

$$\boxed{ x_\ast\in\operatorname{Dom}(f) \not\Rightarrow x_\ast\in\mathcal R. }$$

Esta distinción aparecerá una y otra vez en el resto del libro. Supongamos una cadena:

$$[\mathrm{MOD}] \longrightarrow [\mathrm{APPROX}] \longrightarrow [\mathrm{MATH}] \longrightarrow P.$$

Si la aproximación fue declarada válida solo en cierto régimen: $\mathcal R,$

entonces la predicción $P$ no queda mágicamente liberada de esa restricción porque la derivación matemática sea exacta.

**Principio 1.18 --- Toda predicción hereda el régimen del modelo** Una consecuencia matemática derivada de un modelo conserva las restricciones físicas, idealizaciones y aproximaciones de las premisas que la producen. La exactitud de la derivación no amplía por sí sola el dominio de validez físico.

En símbolos:

$$\boxed{ [\mathrm{MATH}]\ \text{exacto} + [\mathrm{MOD}]/[\mathrm{APPROX}]\ \text{restringidos} \not\Rightarrow \text{validez física universal}. }$$ Imaginemos una aproximación sencilla válida cuando una cantidad adimensional $\varepsilon$ es pequeña:

$$Q_{\mathrm{aprox}} = Q_0(1-\varepsilon).$$

Supongamos que el modelo declara como régimen: $0\le\varepsilon\le0.05.$

Matemáticamente podemos sustituir: $\varepsilon=0.8.$

Obtendremos un número perfectamente definido. Pero el modelo nunca afirmó que la aproximación fuera adecuada allí. Por tanto: $Q_{\mathrm{aprox}}(0.8)$

es un valor matemático de la fórmula, no automáticamente una predicción física autorizada.

La pregunta correcta es:

> ¿Qué control justificaba despreciar los términos omitidos y sigue funcionando para $\varepsilon=0.8$? No siempre existe una frontera brusca:

$$\mathcal R = \{x:x<x_c\}$$

donde todo funciona perfectamente a un lado y deja de funcionar de golpe al otro.

Muchas aproximaciones se degradan progresivamente.

Podemos imaginar:

$$\text{error pequeño} \longrightarrow \text{error apreciable} \longrightarrow \text{modelo inadecuado}.$$

Esto significa que el dominio de validez puede depender de la precisión exigida. Para una tarea basta quizá un error del: $5\%.$ Para otra, incluso: $0.1\%$

puede ser demasiado. Por eso el dominio físico debe leerse junto con el objetivo. Feynman utiliza un ejemplo conceptualmente importante: a velocidades ordinarias puede tratarse la masa como constante con precisión extraordinaria, mientras que a velocidades suficientemente altas esa aproximación deja de ser adecuada.[^5]

La lección que tomaremos no es la teoría relativista ---que estudiaremos mucho después---, sino la estructura metodológica:

$$\boxed{ \text{una relación puede ser excelente en un régimen y equivocada fuera de él}. }$$

Eso no convierte en inútil la relación aproximada. La convierte en una herramienta con dominio declarado.

### 1.11.2. Descripciones efectivas {#fispm-c01-descripciones-efectivas}

Una descripción puede ser excelente dentro de un régimen sin pretender ser fundamental ni universal. Supongamos que una teoría $T_2$ describe un dominio más amplio que una teoría anterior $T_1$.

Sería tentador concluir:

> «Entonces debemos dejar de usar $T_1$.»

Pero no se sigue.

Dentro del régimen donde $T_1$ funciona con la precisión requerida, puede tener ventajas decisivas:

- variables más simples;

- cálculos más cortos;

- interpretación más transparente;

- datos más fáciles de obtener;

- suficiente precisión para la tarea.

Por tanto:

$$\boxed{ \text{teoría más amplia} \not\Rightarrow \text{teoría anterior inútil}. }$$ **Definición operativa 1.29 --- Descripción efectiva** Llamaremos **descripción efectiva** a un modelo o marco físico que retiene las variables, estructuras y relaciones relevantes para un régimen determinado y omite, promedia o sustituye detalles cuya influencia no es necesaria para responder las preguntas planteadas con la precisión requerida.

La palabra «efectiva» no significa:

> «falsa».

Significa:

> «construida para capturar eficazmente cierta física a cierta escala o bajo ciertas condiciones».

En física avanzada, la expresión **teoría efectiva** adquirirá usos técnicos más específicos.

Aquí fijamos solamente esta noción operativa. Sin desarrollar todavía sus teorías, podemos anticipar varios casos.

[]{#un-cuerpo-como-partícula-puntual}

#### 1.11.2.1. Un cuerpo como partícula puntual {#fispm-c01-un-cuerpo-como-partuxedcula-puntual}

La extensión interna del objeto se omite cuando no afecta a la pregunta.

[]{#un-fluido-como-medio-continuo}

#### 1.11.2.2. Un fluido como medio continuo {#fispm-c01-un-fluido-como-medio-continuo}

La estructura molecular puede quedar fuera de la descripción cuando interesan variables macroscópicas.

[]{#la-óptica-de-rayos}

#### 1.11.2.3. La óptica de rayos {#fispm-c01-la-uxf3ptica-de-rayos}

Una descripción mediante rayos puede ser extraordinariamente útil cuando la estructura ondulatoria relevante no se resuelve en la pregunta.

[]{#mecánica-clásica-a-velocidades-ordinarias}

#### 1.11.2.4. Mecánica clásica a velocidades ordinarias {#fispm-c01-mecuxe1nica-cluxe1sica-a-velocidades-ordinarias}

Puede proporcionar predicciones excelentes sin incorporar toda la estructura relativista.

En cada caso:

$$\boxed{ \text{omitir detalle} \neq \text{ignorar arbitrariamente}. }$$

La omisión debe estar justificada por el régimen. Una teoría más amplia también puede cambiar la interpretación que hacemos de una descripción anterior, sin volverla inútil dentro del régimen donde funcionaba:

Feynman subraya una sutileza profunda.[^6]

Una corrección puede ser numéricamente pequeña y, sin embargo, obligarnos a cambiar de manera importante nuestra imagen conceptual.

Esto significa que debemos distinguir:

$$\text{diferencia numérica}$$

de:

$$\text{diferencia estructural}.$$

Dos teorías pueden producir números casi idénticos en cierto régimen y, sin embargo, organizar el mundo mediante conceptos muy diferentes.

Por tanto:

$$\boxed{ \text{aproximación numérica excelente} \not\Rightarrow \text{identidad conceptual}. }$$ No utilizaremos una teoría efectiva para concluir automáticamente qué entidades existen «en último término».

Una descripción macroscópica puede hablar de:

- presión;

- temperatura;

- ondas;

- rayos;

- cuerpos rígidos.

Estas entidades pueden ser extremadamente reales y útiles al nivel de descripción correspondiente aunque una teoría más microscópica utilice otras variables.

La pregunta:

> «¿qué es más fundamental?»

no sustituye a:

> «¿qué variables son adecuadas para esta escala y esta pregunta?» Imaginemos una caja con una enorme cantidad de componentes microscópicos.

Podríamos intentar registrar el estado detallado de cada componente.

Pero nuestra pregunta podría ser solamente:

> «¿cómo cambia una propiedad macroscópica global de la caja?»

Entonces una descripción efectiva puede utilizar pocas variables colectivas.

No afirmamos que los detalles microscópicos hayan desaparecido físicamente.

Afirmamos que:

$$\boxed{ \text{no son variables necesarias para la pregunta efectiva}. }$$

Esto es una aplicación directa del principio 1.9 y principio 1.11. **Principio 1.19 --- Más fundamental no significa más útil para toda tarea** Una descripción más amplia o más fundamental no reemplaza automáticamente a una descripción efectiva dentro del régimen donde esta última es suficientemente precisa, interpretable y eficiente para la pregunta planteada.

Este principio no autoriza a ignorar teorías más amplias.

Obliga a comparar niveles de descripción con la tarea.

### 1.11.3. Escala, control y recuperación de límites {#fispm-c01-escala-control-y-recuperaciuxf3n-de-luxedmites}

La palabra **escala** aparecerá continuamente en física. Una estructura puede ser visible en una escala y prácticamente irrelevante en otra. Imaginemos dos longitudes: $\ell$

y:

$$L.$$

Si: $\ell\ll L,$

ciertos detalles asociados con $\ell$ pueden no afectar a una pregunta formulada a escala $L$.

No convertiremos todavía esta idea en una teoría general de escalas.

Solo conservaremos la regla conceptual:

> la relevancia física de un detalle depende de cómo se compara con las escalas de la pregunta. En §4 vimos que la palabra «pequeño» necesita una referencia.

Una forma común de hacer visible esa referencia es comparar dos cantidades del mismo tipo. Por ejemplo: $\varepsilon = \frac{\ell}{L}.$ Si: $\varepsilon\ll1,$

puede existir una aproximación controlada por esa separación de escalas. La expresión: $\varepsilon\ll1$

no prueba por sí sola cuál aproximación es correcta. Pero nos obliga a declarar **qué comparación** sostiene la simplificación.

Esto anticipa el análisis dimensional del capítulo siguiente sin utilizarlo todavía como técnica formal. Una buena declaración de validez no dice solamente:

> «esto funciona cuando $\varepsilon$ es pequeño».

Debe intentar responder:

1.  ¿qué efecto se omitió?;

2.  ¿por qué era despreciable?;

3.  ¿qué observación indicaría que ya no lo es?;

4.  ¿qué descripción más amplia deberíamos considerar entonces?

Este procedimiento transforma una aproximación en algo auditable. Un modelo puede ser científicamente valioso incluso cuando falla, si sabemos interpretar el fallo. Supongamos que una aproximación predice bien para: $\varepsilon=0.01,$

aceptablemente para: $\varepsilon=0.05,$

y mal para: $\varepsilon=0.5.$ Si el modelo declaraba desde el comienzo: $\varepsilon\ll1,$

el tercer caso no constituye una sorpresa lógica.

Puede ser precisamente la señal esperada de que un efecto omitido se volvió relevante.

Así:

$$\boxed{ \text{fallar fuera del régimen} \neq \text{haber fracasado dentro del régimen}. }$$ La utilidad de una descripción efectiva depende de saber qué cambia al salir de su régimen. Una teoría más amplia debe, cuando corresponda, recuperar la anterior como buena aproximación en las condiciones apropiadas.

En física es frecuente que una descripción más amplia reproduzca una teoría anterior bajo condiciones apropiadas.

Esquemáticamente:

$$T_{\mathrm{amplia}} \longrightarrow T_{\mathrm{efectiva}}$$

cuando ciertas cantidades son pequeñas, grandes o no resolubles a la escala considerada.

Debemos ser cuidadosos con la flecha.

No significa necesariamente inclusión literal:

$$T_{\mathrm{efectiva}} \subset T_{\mathrm{amplia}}.$$

La relación puede requerir:

- aproximaciones;

- reexpresión de variables;

- promedios;

- eliminación de grados de detalle;

- identificación de un régimen. Más adelante estudiaremos relatividad especial.

Por ahora nos basta una relación histórica y metodológica. La mecánica newtoniana funciona extraordinariamente bien para una enorme clase de movimientos ordinarios. La relatividad especial modifica la estructura de espacio, tiempo y movimiento cuando las velocidades dejan de ser pequeñas frente a la velocidad de la luz.

La conclusión correcta no es:

> «Newton era simplemente inútil».

Es:

> «la teoría newtoniana posee un dominio de validez extremadamente importante, pero no universal».

Y la teoría más amplia debe explicar por qué la descripción anterior funcionaba tan bien dentro de ese dominio. El régimen de una aproximación concreta y el dominio de una teoría completa no son necesariamente idénticos; tampoco el dominio puede separarse de observables, condiciones y precisión:

También los observables pueden depender del régimen. Un instrumento diseñado para distinguir estructuras a gran escala puede no detectar detalles microscópicos. Entonces dos modelos que difieren microscópicamente pueden ser observacionalmente equivalentes para ese procedimiento.

La situación es: $M_1\neq M_2$

pero: $O(M_1)=O(M_2)$

para el observable disponible.

Esto conecta §11 con §10:

para discriminar modelos necesitamos no solo una diferencia teórica, sino una diferencia observable en un régimen accesible. Una teoría puede ser muy general y contener dentro de ella varias aproximaciones. Por ejemplo, una teoría $T$ puede ser aplicable en un dominio amplio: $\mathcal R_T,$

pero cierta fórmula aproximada derivada dentro de ella puede requerir: $\mathcal R_A \subset \mathcal R_T.$

Entonces no debemos confundir:

$$\text{fracaso de la aproximación}$$

con:

$$\text{fracaso de la teoría completa}.$$

Este punto será esencial en §12. Tampoco toda discrepancia proviene del régimen.

Podemos estar dentro de: $\mathcal R$

y aun así usar condiciones iniciales incorrectas.

Por eso debemos distinguir:

$$\text{modelo fuera de régimen}$$

de:

$$\text{modelo dentro de régimen con datos de entrada incorrectos}.$$

La diferencia importa porque las revisiones necesarias son distintas. Supongamos dos modelos: $M_A, \qquad M_B.$ En cierto régimen sus predicciones difieren en: $0.01\%.$ Si nuestro instrumento solo resuelve: $1\%,$

ambos pueden ser indistinguibles para la tarea. Si un nuevo instrumento alcanza: $0.001\%,$

la situación cambia. Por tanto, el dominio de utilidad práctica de una descripción puede depender también de la precisión observacional disponible. No estamos introduciendo todavía teoría de incertidumbre.

Solo registramos la dependencia lógica. Dos ejemplos finales muestran por qué «más exactitud» y «más detalle» no son metas independientes de la pregunta:

Supongamos que una tarea exige estimar una cantidad con precisión del: $1\%.$

Tenemos:

[]{#modelo-a-1}

#### 1.11.3.1. Modelo A {#fispm-c01-modelo-a-1}

- error esperado menor que:

$$0.1\%;$$

- cálculo sencillo.

[]{#modelo-b-1}

#### 1.11.3.2. Modelo B {#fispm-c01-modelo-b-1}

- error esperado muchísimo menor;

- cálculo y datos mucho más complejos.

Si ambos están dentro de su régimen, el modelo A puede ser suficiente.

Elegir B no es incorrecto. Pero puede ser innecesario.

El criterio no es:

> «usar siempre la teoría más sofisticada disponible».

Es:

> «usar una descripción cuya adecuación sea controlada para la tarea». Ahora cambiemos la pregunta.

Supongamos que queremos detectar precisamente una corrección del orden de: $0.05\%.$

Entonces el modelo A anterior, cuyo error puede alcanzar: $0.1\%,$

ya no basta.

El mismo modelo ha pasado de:

> adecuado

a:

> insuficiente

sin que haya cambiado su matemática.

Cambió la pregunta.

Esto refuerza:

$$\boxed{ \mathcal R \text{ depende también del criterio de adecuación exigido}. }$$ **Ficha FPM --- Validez y descripción efectiva** 1. **Pregunta:** ¿qué queremos predecir o explicar? 2. **Modelo:** ¿qué descripción estamos usando? 3. **Régimen:** ¿qué condiciones forman $\mathcal R$? 4. **Escalas:** ¿qué comparaciones hacen pequeños o irrelevantes ciertos efectos? 5. **Idealizaciones:** ¿qué se ha omitido exactamente? 6. **Aproximaciones:** ¿qué término o efecto se ha reemplazado o despreciado? 7. **Control:** ¿qué parámetro o condición vigila la aproximación? 8. **Precisión:** ¿qué error es aceptable para la tarea? 9. **Observables:** ¿el instrumento puede detectar la diferencia entre modelos? 10. **Fallo esperado:** ¿qué señal indicaría salida de régimen? 11. **Descripción más amplia:** ¿qué modelo o teoría debería usarse entonces? 12. **Estatus:** ¿el cálculo es exacto dentro de un modelo aproximado?

### 1.11.4. Ejercicios {#fispm-c01-ejercicios-1}

[]{#fispm-t1-c01-e0027}

**Ejercicio 1.27 --- Órbita marciana y perceptibilidad.**

**Fuente del motivo:** adaptación y ampliación del ejemplo de Arnold sobre la excentricidad de la órbita de Marte.[^7]

Una elipse de semieje mayor $a$ y excentricidad $e$ tiene semieje menor: $b=a\sqrt{1-e^2}.$ Para Marte podemos tomar, como orden de magnitud: $e\approx0.1.$

Responde:

1.  Calcula:

$$\frac{b}{a}.$$

1.  Usando la aproximación de §4,

$$\sqrt{1-A} \approx 1-\frac{A}{2},$$

estima: $\frac{b}{a}$

sin calculadora.

1.  Estima la diferencia relativa:

$$1-\frac{b}{a}.$$

1.  Explica por qué una excentricidad de orden $0.1$ puede corresponder a una diferencia visual entre los semiejes de solo alrededor de medio punto porcentual.

2.  Explica por qué este ejemplo distingue:

    - diferencia matemática;

    - perceptibilidad física;

    - régimen de una aproximación. **Solución.**

[]{#razón-exacta}

##### 1. Razón exacta {#fispm-c01-razuxf3n-exacta}

Con: $e=0.1,$

tenemos: $e^2=0.01.$ Por tanto: $\frac{b}{a} = \sqrt{1-0.01} = \sqrt{0.99}.$

Numéricamente: $\sqrt{0.99} \approx0.99499.$

Así:

$$\boxed{ \frac{b}{a} \approx0.995. }$$

##### 2. Aproximación elemental {#fispm-c01-aproximaciuxf3n-elemental}

Tomamos: $A=0.01.$

Entonces: $\sqrt{1-A} \approx 1-\frac{A}{2}.$ Por tanto: $\frac{b}{a} \approx 1-\frac{0.01}{2}.$

Así:

$$\boxed{ \frac{b}{a} \approx0.995. }$$

La aproximación reproduce muy bien el valor anterior.

##### 3. Diferencia relativa {#fispm-c01-diferencia-relativa}

Tenemos: $1-\frac{b}{a} \approx 1-0.995 = 0.005.$

Como porcentaje: $0.005\times100\% = 0.5\%.$

Por tanto:

$$\boxed{ a-b \text{ representa aproximadamente el }0.5\%\text{ de }a. }$$

##### 4. Excentricidad y apariencia {#fispm-c01-excentricidad-y-apariencia}

La excentricidad entra al cuadrado en: $\frac{b}{a} = \sqrt{1-e^2}.$

Así, aunque: $e\approx0.1,$

la corrección geométrica relevante para comparar ambos semiejes es del orden de: $e^2\approx0.01.$ La diferencia final entre $a$ y $b$ es todavía menor, aproximadamente: $0.5\%.$ Por eso una cantidad matemática que no parece extremadamente pequeña puede producir una diferencia visual difícil de percibir directamente.

##### 5. Las tres distinciones {#fispm-c01-las-tres-distinciones}

**Diferencia matemática:** la elipse no es un círculo.

**Perceptibilidad física:** la diferencia entre sus semiejes puede ser demasiado pequeña para distinguirla fácilmente a simple vista o con un procedimiento poco sensible.

**Régimen de aproximación:** la fórmula:

$$\sqrt{1-A} \approx 1-\frac{A}{2}$$

funciona aquí porque: $A=e^2=0.01$

es pequeño.

Por tanto:

[]{#fispm-t1-c01-e0028}

$$\boxed{ \text{diferencia real} \neq \text{diferencia fácilmente observable}. }$$ **Ejercicio 1.28 --- Rayos, ondas y fotones.**

En física aparecen distintas descripciones de la luz:

- rayos;

- ondas;

- fotones.

Sin desarrollar todavía ninguna de estas teorías, responde:

1.  ¿Por qué la existencia de una descripción ondulatoria no vuelve automáticamente inútil la óptica de rayos?

2.  ¿Qué tipo de pregunta puede hacer insuficiente una descripción mediante rayos?

3.  ¿Por qué una descripción cuántica más amplia no implica que debamos usar fotones en todo problema óptico elemental?

4.  Formula la relación entre estas descripciones usando las ideas de:

    - pregunta;

    - escala;

    - observable;

    - dominio de validez;

    - descripción efectiva.

5.  Explica por qué sería incorrecto escribir simplemente:

$$\text{rayos} \subset \text{ondas} \subset \text{fotones}.$$ **Solución.**

[]{#utilidad-de-los-rayos}

##### 1. Utilidad de los rayos {#fispm-c01-utilidad-de-los-rayos}

Una descripción de rayos puede capturar con enorme eficacia:

- propagación aproximada de trayectorias;

- formación geométrica de imágenes;

- direcciones relevantes;

- relaciones entre objetos e instrumentos.

Si la pregunta no resuelve efectos donde la estructura ondulatoria es esencial, la descripción de rayos puede ser suficiente.

Por tanto:

$$\boxed{ \text{descripción más amplia} \not\Rightarrow \text{descripción efectiva inútil}. }$$

##### 2. Cuándo pueden ser insuficientes los rayos {#fispm-c01-cuuxe1ndo-pueden-ser-insuficientes-los-rayos}

Si el fenómeno que queremos comprender depende precisamente de propiedades que una descripción de rayos omite, debemos cambiar de modelo. Por ejemplo, una pregunta donde sean esenciales patrones producidos por la estructura ondulatoria requerirá una descripción capaz de representar esa estructura.

La conclusión correcta es:

> el modelo deja de ser suficiente para la nueva pregunta.

No:

> el modelo nunca fue útil.

##### 3. Por qué no usar siempre la descripción más fundamental {#fispm-c01-por-quuxe9-no-usar-siempre-la-descripciuxf3n-muxe1s-fundamental}

Una descripción cuántica puede contener estructura innecesaria para una tarea geométrica elemental.

Si el objetivo es determinar, por ejemplo, una dirección de propagación aproximada o una construcción geométrica de imagen, una teoría efectiva más simple puede ser:

- suficiente;

- más transparente;

- más eficiente.

Esto es precisamente principio 1.19.

##### 4. Relación entre las descripciones {#fispm-c01-relaciuxf3n-entre-las-descripciones}

Podemos representarla conceptualmente:

$$\text{pregunta} + \text{escala} + \text{observable} \longrightarrow \text{descripción adecuada}.$$

Cada descripción posee un dominio físico donde ciertas variables y estructuras son las relevantes. Una descripción efectiva selecciona justamente esas estructuras sin afirmar que sean la última descripción posible de la luz.

##### 5. Por qué no es inclusión conjuntista {#fispm-c01-por-quuxe9-no-es-inclusiuxf3n-conjuntista}

Las teorías no son simplemente conjuntos de fórmulas colocados unos dentro de otros.

El paso entre descripciones puede requerir:

- nuevas variables;

- nuevas interpretaciones;

- aproximaciones;

- límites físicos;

- cambios en lo que consideramos observable.

Por tanto, la relación correcta es funcional:

$$\boxed{ \text{descripciones distintas} \longleftrightarrow \text{regímenes y preguntas distintas}, }$$

no una cadena literal de inclusión de conjuntos.

### 1.11.5. Síntesis {#fispm-c01-suxedntesis-8}

Esta sección incorpora definitivamente el régimen: $\mathcal R$

a la lectura de cualquier modelo.

La regla central es:

$$\boxed{ \text{fórmula matemáticamente válida} \not\Rightarrow \text{predicción físicamente válida en todo régimen}. }$$

Definimos además una descripción efectiva como aquella que conserva la estructura necesaria para una pregunta y una escala determinadas sin reclamar universalidad.

Por eso:

$$\boxed{ \text{efectivo} \neq \text{falso}. }$$

Y:

$$\boxed{ \text{más fundamental} \neq \text{más útil para toda tarea}. }$$

A partir de ahora, cada aproximación importante deberá venir acompañada por preguntas de control:

- ¿qué se omitió?;

- ¿qué lo hace pequeño?;

- ¿qué precisión necesitamos?;

- ¿qué señal indicará que salimos del régimen?;

- ¿qué descripción más amplia debemos usar entonces?

Esto prepara la siguiente sección.

Cuando una predicción contradice una observación, debemos evitar el salto:

> «la teoría está equivocada».

Una predicción depende de teoría, modelo, condiciones, aproximaciones y reglas de observación.

La lógica de esa revisión será el objeto de (§[1.12](#fispm-c01-cuando-una-predicciuxf3n-falla-luxf3gica-de-revisiuxf3n)).

[]{#cuando-una-predicción-falla-lógica-de-revisión}

[]{#fispm-t1-c01-s12}

[]{#fpm-i-01-s12}

## 1.12. Cuando una predicción falla: lógica de revisión {#fispm-c01-cuando-una-predicciuxf3n-falla-luxf3gica-de-revisiuxf3n}

[]{#el-error-más-tentador}

### 1.12.1. El error más tentador {#fispm-c01-el-error-muxe1s-tentador}

Supongamos que una teoría, junto con un modelo concreto, produce una predicción:

$$P.$$

Realizamos el experimento y obtenemos un resultado incompatible con esa predicción: $\neg P.$

La reacción inmediata puede ser:

> «Entonces la teoría es falsa».

Pero esa inferencia es demasiado rápida. La predicción no provenía de una teoría desnuda.

Para llegar a $P$ tuvimos que combinar:

- principios o hipótesis físicas;

- condiciones iniciales y de frontera;

- parámetros;

- idealizaciones;

- aproximaciones;

- reglas de interpretación;

- procedimientos de medición.

La predicción depende de un **paquete de premisas**. Por eso un fallo predictivo pone en cuestión el paquete completo, no identifica automáticamente qué componente debe abandonarse.

[]{#fig:I-01-R05}

![**Figura 1.8.** Una discrepancia motiva revisar hipótesis, condiciones iniciales y procedimiento de observación. El esquema no adjudica por sí solo el fallo a una ley fundamental. Véase §[1.12](#fispm-c01-cuando-una-predicciuxf3n-falla-luxf3gica-de-revisiuxf3n).](/assets/books/fispm/v04/I-01-R05.svg "fig:"){.fpm-v04-figure fig-alt="El contraste puede revisar varias piezas" width="389px" fig-cap=""}

### 1.12.2. El paquete predictivo {#fispm-c01-el-paquete-predictivo}

Para hacer visible la lógica, comprimiremos temporalmente las premisas en cuatro grupos.

Usaremos:

$$H$$

para las hipótesis, leyes o principios físicos relevantes;

$$I$$

para la información que fija la realización concreta, como condiciones iniciales, condiciones de frontera y parámetros pertinentes;

$$A$$

para las idealizaciones y aproximaciones utilizadas;

y:

$$M$$

para la mediación observacional: interpretación de magnitudes, calibración, procedimiento experimental y reglas `[``OBS``]` necesarias para comparar la consecuencia formal con una observación. La letra $M$ de esta sección significa **mediación observacional** y no debe confundirse con el símbolo: $\mathcal M$

que usamos para el modelo físico completo.

**Definición operativa 1.30 --- Paquete predictivo** Llamaremos **paquete predictivo** a la conjunción de premisas físicas, condiciones, aproximaciones y reglas de observación cuya aceptación conjunta permite derivar una predicción contrastable.

En nuestra notación esquemática: $\Pi = H\land I\land A\land M.$

### 1.12.3. La estructura lógica de una predicción {#fispm-c01-la-estructura-luxf3gica-de-una-predicciuxf3n}

Una derivación física puede representarse esquemáticamente como: $(H\land I\land A\land M)\to P.$ Esta fórmula no significa que toda teoría física real pueda reducirse literalmente a cuatro proposiciones simples. Es un **esqueleto lógico**. La utilidad del esquema consiste en impedir que olvidemos que $P$ depende de más de una premisa.

En términos del protocolo de estatus, una cadena real puede contener:

$$[\mathrm{POST}], \quad [\mathrm{EMP}], \quad [\mathrm{MOD}], \quad [\mathrm{APPROX}], \quad [\mathrm{IC}], \quad [\mathrm{BC}], \quad [\mathrm{OBS}],$$

antes de llegar a las consecuencias: $[\mathrm{MATH}].$

### 1.12.4. La parte matemática empieza después de declarar las premisas {#fispm-c01-la-parte-matemuxe1tica-empieza-despuuxe9s-de-declarar-las-premisas}

El protocolo FPM establece:

> la prueba matemática comienza después de declarar las premisas físicas.

La razón puede verse ahora con claridad. Una vez aceptamos: $H,\ I,\ A,\ M,$

podemos realizar una derivación matemática rigurosa.

Pero esa demostración muestra:

$$\boxed{ H\land I\land A\land M \Longrightarrow P, }$$

no:

$$\boxed{ P\ \text{es una verdad matemática independiente del mundo}. }$$

La consecuencia es exacta **relativamente a las premisas**.

### 1.12.5. El modus tollens elemental {#fispm-c01-el-modus-tollens-elemental}

Recordemos la forma lógica: $Q\to P.$ Si además sabemos: $\neg P,$

podemos concluir: $\neg Q.$

Este es el modus tollens:

$$\boxed{ (Q\to P)\land\neg P \Longrightarrow \neg Q. }$$

En nuestro caso: $Q = H\land I\land A\land M.$

Entonces el resultado será inmediato. Pero sus consecuencias físicas merecen una lectura cuidadosa.

### 1.12.6. Segunda proposición formal del capítulo {#fispm-c01-segunda-proposiciuxf3n-formal-del-capuxedtulo}

**1.2 --- Lógica de revisión de un paquete predictivo**

Sean $H$, $I$, $A$, $M$ y $P$ proposiciones. Si: $(H\land I\land A\land M)\to P$

y: $\neg P,$

entonces: $\neg(H\land I\land A\land M).$

Equivalentemente, por las leyes de De Morgan: $\neg H \lor \neg I \lor \neg A \lor \neg M.$ Por tanto, la falsedad de la predicción no permite concluir lógicamente, a partir de estas premisas solamente, cuál de los componentes $H$, $I$, $A$ o $M$ debe rechazarse.

[]{#demostración-de-fpm-i-01-p02}

[]{#fispm-t1-c01-p0002}

### 1.12.7. Demostración de 1.2 {#fispm-c01-demostraciuxf3n-de-1.2}

Definamos: $Q = H\land I\land A\land M.$ La primera hipótesis se convierte en: $Q\to P.$ La segunda hipótesis es: $\neg P.$ Por modus tollens: $\neg Q.$ Sustituyendo nuevamente la definición de $Q$: $\neg(H\land I\land A\land M).$

Aplicamos ahora la ley de De Morgan para una conjunción finita:

$$\neg(H\land I\land A\land M) \equiv \neg H \lor \neg I \lor \neg A \lor \neg M.$$

Por tanto:

$$\boxed{ \neg H \lor \neg I \lor \neg A \lor \neg M. }$$

Esto demuestra la proposición.

$$\boxed{\text{QED}}$$

### 1.12.8. Qué demuestra realmente proposición 1.2 {#fispm-c01-quuxe9-demuestra-realmente-p02}

La conclusión es una **disyunción**: $\neg H \lor \neg I \lor \neg A \lor \neg M.$

No es: $\neg H.$ Tampoco es: $\neg A.$

Ni: $\neg M.$ Con la información lógica disponible sabemos solamente que **al menos un componente del paquete no puede mantenerse tal como estaba**.

Esta es la diferencia entre:

$$\boxed{ \text{detección de inconsistencia} }$$

y:

$$\boxed{ \text{diagnóstico de la causa}. }$$

### 1.12.9. El teorema no decide por nosotros {#fispm-c01-el-teorema-no-decide-por-nosotros}

El matemático podría sentir cierta frustración.

Tenemos una demostración perfecta y, sin embargo, la conclusión física parece incompleta. Pero esto no es una debilidad de la demostración. Es precisamente lo que la lógica permite concluir.

Para pasar de: $\neg H \lor \neg I \lor \neg A \lor \neg M$

a una afirmación como: $\neg A$

necesitamos información adicional que descarte las demás alternativas. Por ejemplo, podríamos comprobar independientemente: $H, \qquad I, \qquad M.$ Entonces la disyunción obligaría a: $\neg A.$ El diagnóstico requiere **nuevas premisas**.

### 1.12.10. La discrepancia observacional también es una premisa {#fispm-c01-la-discrepancia-observacional-tambiuxe9n-es-una-premisa}

Hemos escrito: $\neg P.$ Pero en un experimento real rara vez recibimos una proposición booleana directamente de la naturaleza.

Recibimos:

- lecturas;

- imágenes;

- conteos;

- señales;

- intervalos;

- resultados procesados.

Para afirmar: $\neg P$

debemos decidir que la observación es suficientemente incompatible con la predicción bajo un criterio pertinente. Ese paso pertenece a: $[\mathrm{OBS}].$ Más adelante estudiaremos incertidumbre y tratamiento cuantitativo de datos.

Aquí simplemente registramos:

$$\boxed{ \text{establecer }\neg P \text{ también requiere una cadena observacional fiable}. }$$

Por eso $M$ forma parte del paquete.

### 1.12.11. Ejemplo desarrollado 15 --- El cronómetro {#fispm-c01-ejemplo-desarrollado-15-el-cronuxf3metro}

Supongamos que un modelo de cierto sistema predice un tiempo: $T_{\mathrm{pred}}.$ La medición produce un valor incompatible con esa predicción. Podemos organizar las posibilidades.

[]{#h-estructura-física}

#### 1.12.11.1. $H$ --- Estructura física {#fispm-c01-h-estructura-fuxedsica}

Tal vez alguna relación física utilizada no sea adecuada para el fenómeno.

[]{#i-condiciones}

#### 1.12.11.2. $I$ --- Condiciones {#fispm-c01-i-condiciones}

Tal vez el estado inicial real no fue el que creíamos.

[]{#a-aproximaciones}

#### 1.12.11.3. $A$ --- Aproximaciones {#fispm-c01-a-aproximaciones}

Tal vez un efecto despreciado se volvió relevante.

[]{#m-medición}

#### 1.12.11.4. $M$ --- Medición {#fispm-c01-m-mediciuxf3n}

Tal vez el cronómetro, la calibración o el procedimiento de detección introdujeron un problema. El resultado experimental, por sí solo, no selecciona una de estas cuatro explicaciones.

### 1.12.12. Un fallo puede localizarse mediante pruebas auxiliares {#fispm-c01-un-fallo-puede-localizarse-mediante-pruebas-auxiliares}

La ambigüedad no significa que el diagnóstico sea imposible.

Significa que requiere trabajo adicional.

Podemos diseñar pruebas independientes.

Por ejemplo:

[]{#prueba-de-i}

#### 1.12.12.1. Prueba de $I$ {#fispm-c01-prueba-de-i}

Repetir el experimento con una preparación mejor controlada.

[]{#prueba-de-m}

#### 1.12.12.2. Prueba de $M$ {#fispm-c01-prueba-de-m}

Calibrar el instrumento mediante un patrón independiente.

[]{#prueba-de-a}

#### 1.12.12.3. Prueba de $A$ {#fispm-c01-prueba-de-a}

Cambiar deliberadamente la escala o condición que controla la aproximación.

[]{#prueba-de-h}

#### 1.12.12.4. Prueba de $H$ {#fispm-c01-prueba-de-h}

Buscar otra predicción que dependa de la misma hipótesis pero no de las mismas aproximaciones. La revisión se convierte así en un problema de **discriminación entre causas posibles**, análogo a §10.

### 1.12.13. El experimento discriminante reaparece {#fispm-c01-el-experimento-discriminante-reaparece}

En §10 definimos un experimento discriminante entre modelos. Ahora podemos extender la idea conceptualmente.

Después de un fallo, nuestras alternativas son:

$$\neg H, \qquad \neg I, \qquad \neg A, \qquad \neg M.$$

Buscamos una nueva prueba cuyo resultado cambie según cuál de esas posibilidades sea la responsable.

Por ejemplo:

$$\text{prueba auxiliar} \longrightarrow \begin{cases} \text{resultado compatible con fallo de }A,\\ \text{resultado compatible con fallo de }M. \end{cases}$$

El diagnóstico es una nueva tarea de modelización.

### 1.12.14. Principio metodológico de auditoría {#fispm-c01-principio-metodoluxf3gico-de-auditoruxeda}

**Principio 1.20 --- Un fallo predictivo exige auditoría, no culpable automático** Si una predicción fiable contradice una observación fiable, debe revisarse el paquete de premisas que produjo la predicción. La discrepancia, por sí sola, no identifica cuál hipótesis, condición, aproximación o regla de observación es responsable.

Este principio es la lectura metodológica directa de la proposición 1.2.

### 1.12.15. Qué ocurre con una solución físicamente absurda {#fispm-c01-quuxe9-ocurre-con-una-soluciuxf3n-fuxedsicamente-absurda}

A veces el problema aparece incluso antes de realizar el experimento. Una derivación matemática produce una solución que contradice una restricción física declarada.

Entonces no debemos decir automáticamente:

> «La matemática falló».

Debemos preguntar:

1.  ¿la solución satisface realmente las ecuaciones?;

2.  ¿pertenece al espacio físico de estados admitido?;

3.  ¿respeta las condiciones iniciales y de frontera?;

4.  ¿viola una idealización o un régimen?;

5.  ¿hemos interpretado correctamente las variables?

Una solución puede ser matemáticamente válida para la ecuación y físicamente inadmisible para el modelo completo. Este punto prepara §13.

### 1.12.16. Ficha FPM de auditoría de una predicción fallida {#fispm-c01-ficha-fpm-de-auditoruxeda-de-una-predicciuxf3n-fallida}

[]{#fispm-t1-c01-e0029}

**Ficha FPM --- Auditoría de fallo predictivo** 1. **Predicción:** ¿qué proposición $P$ estaba realmente implicada? 2. **Hipótesis:** ¿qué contiene $H$? 3. **Condiciones:** ¿qué contiene $I$? 4. **Idealizaciones y aproximaciones:** ¿qué contiene $A$? 5. **Mediación observacional:** ¿qué contiene $M$? 6. **Régimen:** ¿estábamos dentro de $\mathcal R$? 7. **Discrepancia:** ¿qué evidencia autoriza afirmar $\neg P$? 8. **Conclusión lógica mínima:** ¿qué conjunción queda negada? 9. **Alternativas:** ¿qué términos aparecen en la disyunción de De Morgan? 10. **Evidencia independiente:** ¿qué alternativas podemos descartar ya? 11. **Prueba nueva:** ¿qué experimento distinguiría las causas restantes? 12. **Revisión:** ¿qué nivel del modelo o teoría debe modificarse? **Ejercicio 1.29 --- Modus tollens compuesto.**

Demuestra:

$$[(H\land I\land A\land M)\to P] \land \neg P \Longrightarrow \neg(H\land I\land A\land M).$$

Después explica por qué la conclusión: $\neg H$

no se sigue de las premisas. **Solución.**

Definamos: $Q = H\land I\land A\land M.$ La primera parte de la hipótesis es: $Q\to P.$ La segunda es: $\neg P.$ Por modus tollens: $\neg Q.$

Sustituyendo:

$$\boxed{ \neg(H\land I\land A\land M). }$$

Ahora preguntamos si podemos concluir: $\neg H.$

No.

Por De Morgan:

$$\neg(H\land I\land A\land M) \equiv \neg H \lor \neg I \lor \neg A \lor \neg M.$$

La disyunción puede ser verdadera aunque:

$$H$$

sea verdadera.

Por ejemplo, consideremos:

$$H=\text{V}, \qquad I=\text{F}, \qquad A=\text{V}, \qquad M=\text{V}.$$

Entonces: $H\land I\land A\land M = \text{F},$

y por tanto: $\neg(H\land I\land A\land M) = \text{V},$

pero: $\neg H = \text{F}.$ Así existe una valuación donde la conclusión de la proposición 1.2 es verdadera y $\neg H$ es falsa.

Por tanto:

[]{#fispm-t1-c01-e0030}

$$\boxed{ \neg(H\land I\land A\land M) \not\Rightarrow \neg H. }$$ **Ejercicio 1.30 --- De Morgan y diagnóstico físico.**

Un experimento se modela mediante el siguiente paquete:

- $H$: la relación física central utilizada es adecuada;

- $I$: las condiciones iniciales y parámetros fueron correctamente determinados;

- $A$: las aproximaciones e idealizaciones siguen dentro de su régimen;

- $M$: el procedimiento de observación y calibración es correcto.

Se ha demostrado que: $(H\land I\land A\land M)\to P.$ Una observación fiable es incompatible con $P$.

1.  Escribe la conclusión lógica mínima.

2.  Aplica De Morgan.

3.  Un control independiente confirma $I$.

4.  Una calibración independiente confirma $M$.

5.  Una prueba adicional muestra que la aproximación principal está fuera de su régimen.

6.  ¿Qué revisión está entonces directamente justificada?

7.  ¿Se sigue de este diagnóstico que $H$ es falsa?

8.  Explica qué habría ocurrido si se hubiera saltado directamente de $\neg P$ a $\neg H$. **Solución.**

[]{#conclusión-mínima}

#### 1.12.16.0. 1. Conclusión mínima {#fispm-c01-conclusiuxf3n-muxednima .unnumbered}

Tenemos: $(H\land I\land A\land M)\to P$

y: $\neg P.$

Por modus tollens:

$$\boxed{ \neg(H\land I\land A\land M). }$$

#### 1.12.16.0. 2. De Morgan {#fispm-c01-de-morgan .unnumbered}

Aplicamos: $\neg(X\land Y) \equiv \neg X\lor\neg Y.$

Extendida a las cuatro premisas:

$$\boxed{ \neg H \lor \neg I \lor \neg A \lor \neg M. }$$

#### 1.12.16.1. 3. Confirmación de $I$ {#fispm-c01-confirmaciuxf3n-de-i}

La evidencia independiente autoriza mantener:

$$I.$$

Por tanto, dentro del diagnóstico actual podemos eliminar: $\neg I.$ La disyunción se reduce informativamente a: $\neg H \lor \neg A \lor \neg M.$

#### 1.12.16.2. 4. Confirmación de $M$ {#fispm-c01-confirmaciuxf3n-de-m}

La calibración independiente autoriza mantener:

$$M.$$

La disyunción restante es: $\neg H \lor \neg A.$

#### 1.12.16.2. 5. La aproximación está fuera de régimen {#fispm-c01-la-aproximaciuxf3n-estuxe1-fuera-de-ruxe9gimen .unnumbered}

La nueva prueba proporciona evidencia específica para: $\neg A.$ Ahora tenemos una causa concreta capaz de explicar la discrepancia.

#### 1.12.16.2. 6. Revisión justificada {#fispm-c01-revisiuxf3n-justificada .unnumbered}

La revisión directamente justificada es:

> abandonar o modificar la aproximación que produjo $A$, o sustituirla por una descripción válida en el nuevo régimen.

En símbolos, la evidencia favorece:

$$\boxed{\neg A}.$$

#### 1.12.16.3. 7. ¿Implica esto $\neg H$? {#fispm-c01-implica-esto-neg-h}

No. La disyunción: $\neg H\lor\neg A$

queda satisfecha si: $\neg A$

es verdadera.

Por tanto, el fallo de la aproximación no obliga lógicamente a rechazar:

$$H.$$

La relación física central puede continuar siendo adecuada.

#### 1.12.16.3. 8. Error del salto directo {#fispm-c01-error-del-salto-directo .unnumbered}

Si hubiéramos inferido inmediatamente: $\neg P \Longrightarrow \neg H,$

habríamos cometido un error lógico. La predicción dependía de: $H\land I\land A\land M,$

no de $H$ sola.

La inferencia válida era:

$$\neg P \Longrightarrow \neg(H\land I\land A\land M),$$

dado el condicional predictivo. El diagnóstico posterior requirió evidencia nueva.

La lección es:

$$\boxed{ \text{fallo predictivo} \neq \text{identificación automática de la causa}. }$$

### 1.12.17. Síntesis {#fispm-c01-suxedntesis-9}

La segunda proposición formal del capítulo es:

$$\boxed{ [(H\land I\land A\land M)\to P] \land \neg P \Longrightarrow \neg(H\land I\land A\land M). }$$

Por De Morgan:

$$\boxed{ \neg H \lor \neg I \lor \neg A \lor \neg M. }$$

La matemática nos dice exactamente cuánto podemos concluir.

No menos:

> alguna parte del paquete debe revisarse.

Pero tampoco más:

> la lógica por sí sola no identifica cuál.

Por eso proposición 1.2 conduce al principio:

$$\boxed{ \text{predicción fallida} \longrightarrow \text{auditoría de premisas}. }$$

La tarea física comienza entonces de nuevo:

- revisar condiciones;

- revisar régimen;

- revisar aproximaciones;

- revisar observación;

- diseñar pruebas discriminantes;

- y, cuando la evidencia lo exige, revisar la propia teoría.

La sección siguiente afinará una distinción que ya ha aparecido varias veces. Una solución puede ser matemáticamente exacta y, sin embargo, describir mal el mundo. Una aproximación puede ser matemáticamente inexacta y, sin embargo, describirlo extraordinariamente bien en su régimen.

Entramos así en el §[1.13](#fispm-c01-exactitud-matemuxe1tica-y-adecuaciuxf3n-fuxedsica).

[]{#exactitud-matemática-y-adecuación-física}

[]{#fispm-t1-c01-s13}

[]{#fpm-i-01-s13}

## 1.13. Exactitud matemática y adecuación física {#fispm-c01-exactitud-matemuxe1tica-y-adecuaciuxf3n-fuxedsica}

[]{#dos-evaluaciones-que-no-deben-confundirse}

### 1.13.1. Dos evaluaciones que no deben confundirse {#fispm-c01-dos-evaluaciones-que-no-deben-confundirse}

A lo largo del capítulo hemos usado expresiones como:

- «resultado exacto»;

- «aproximación»;

- «modelo adecuado»;

- «predicción compatible con la observación».

Estas expresiones pertenecen a planos diferentes.

Cuando preguntamos:

> ¿La derivación es matemáticamente correcta?

examinamos la relación entre premisas y conclusión.

Cuando preguntamos:

> ¿El modelo describe adecuadamente el sistema físico?

examinamos la relación entre la representación y el mundo.

Por tanto:

$$\boxed{ \text{exactitud matemática} \neq \text{adecuación física}. }$$

Esta es quizá la distinción más importante del capítulo completo. Supongamos que hemos declarado un paquete de premisas: $\Pi.$ Y demostramos rigurosamente: $\Pi\to P.$ Si la demostración es válida, entonces $P$ es una consecuencia matemática exacta de $\Pi$.

[]{#fig:I-01-R06}

![**Figura 1.9.** La igualdad $y=u^2$ define exactamente la curva dibujada. Su uso como ley de un fenómeno requiere declarar qué representan $u$ e $y$, cómo se miden y dónde se ha contrastado la relación. Véase §[1.13](#fispm-c01-exactitud-matemuxe1tica-y-adecuaciuxf3n-fuxedsica).](/assets/books/fispm/v04/I-01-R06.svg "fig:"){.fpm-v04-figure fig-alt="Exactitud interna y significado físico" width="403px" fig-cap=""}

Pero esto no establece todavía que:

$$\Pi$$

sea una descripción físicamente adecuada del sistema real.

La forma lógica es:

$$\boxed{ \Pi\ \text{aceptada} \Longrightarrow P\ \text{exactamente derivada}. }$$

La palabra **exactamente** modifica aquí a la derivación, no al mundo. **Definición operativa 1.31 --- Exactitud matemática relativa al modelo** Diremos que un resultado es **matemáticamente exacto respecto de un modelo** cuando se obtiene sin introducir nuevas aproximaciones matemáticas a partir de las definiciones, hipótesis y relaciones formales declaradas en ese modelo.

Esta definición contiene dos restricciones.

Primera:

> **respecto de un modelo**.

Segunda:

> **sin introducir nuevas aproximaciones matemáticas**.

No afirmamos que el modelo mismo sea exacto como representación de la naturaleza. **Definición operativa 1.32 --- Adecuación física** La **adecuación física** de un modelo es el grado en que sus representaciones, relaciones y predicciones conservan los rasgos relevantes del sistema real para una pregunta, un régimen y una precisión determinados.

No la tratamos aquí como una cantidad numérica. La definición es metodológica.

Obliga a declarar:

- **qué pregunta**;

- **qué régimen**;

- **qué precisión**;

- **qué rasgos son relevantes**.

Sin esos datos, la expresión «modelo correcto» es demasiado vaga. El contraste puede resumirse así:

  Pregunta                                              Evaluación
  ----------------------------------------------------- --------------------------------------------
  ¿La conclusión se sigue de las premisas?              corrección o exactitud matemática relativa
  ¿Las premisas representan adecuadamente el sistema?   adecuación física
  ¿La solución satisface restricciones y condiciones?   admisibilidad física
  ¿La diferencia prevista puede observarse?             accesibilidad observacional

Imaginemos un sensor cuyo modelo ideal es: $[\mathrm{MOD}] \qquad y=2x.$

Dentro del modelo, si: $x=4,$

obtenemos exactamente: $y=8.$

No hay error algebraico.

Ahora supongamos que el dispositivo real posee una limitación física:

> su salida no puede superar $10$.

Entonces, para: $x=8,$

el modelo lineal produce exactamente: $y=16.$ Pero el dispositivo real no puede entregar ese valor. La conclusión: $y=16$

es matemáticamente exacta **dentro del modelo lineal** y físicamente inadecuada **para el dispositivo real en ese régimen**. No hay contradicción.

Las dos evaluaciones pertenecen a niveles diferentes. Ante el ejemplo anterior sería incorrecto decir:

> «La cuenta $2\cdot8=16$ salió mal».

La cuenta es correcta. El problema está en la premisa física: $[\mathrm{MOD}] \qquad y=2x$

aplicada fuera del régimen donde representa adecuadamente al sensor.

Por tanto:

$$\boxed{ \text{predicción físicamente mala} \not\Rightarrow \text{matemática incorrecta}. }$$

Este es exactamente el tipo de diagnóstico que §12 nos enseñó a realizar. Un mapa puede ser excelente sin ser el territorio. De manera análoga, un modelo físico no necesita reproducir todos los detalles del sistema.

La pregunta correcta no es:

> «¿Es idéntico al objeto real?»

Sino:

> «¿Conserva la estructura necesaria para responder la pregunta?»

Esto conecta:

$$\text{definición 1.32}$$

con: $\text{principio 1.9}, \qquad \text{principio 1.11}, \qquad \text{definición 1.29}.$

Una descripción efectiva puede ser muy adecuada precisamente porque **no** intenta representar todo. El matemático puede, por tanto, resolver perfectamente una pregunta mal formulada o un modelo innecesariamente detallado:

Spivak insiste, en su proyecto de física para matemáticos, en una dificultad característica: una vez reducida una situación física a una cuestión matemática, el matemático puede manejar con comodidad el formalismo; el trabajo específicamente físico está en construir correctamente esa reducción.[^8]

Podemos expresarlo así:

Esta no es una crítica a la matemática.

Es una advertencia sobre el paso:

$$\text{fenómeno} \longrightarrow \text{modelo}.$$ Supongamos que agregamos diez variables a un modelo.

¿Se volvió más exacto?

No necesariamente.

Tal vez las nuevas variables:

- no estén bien determinadas;

- representen efectos irrelevantes;

- introduzcan parámetros arbitrarios;

- dificulten la interpretación;

- no mejoren ninguna predicción.

La adecuación física no se mide por el número de componentes del formalismo.

Por eso:

$$\boxed{ \text{más detalle} \neq \text{más adecuación automática}. }$$

### 1.13.2. Exactitud de la solución y calidad del modelo {#fispm-c01-exactitud-de-la-soluciuxf3n-y-calidad-del-modelo}

Supongamos que tenemos dos opciones.

[]{#modelo-a-2}

#### 1.13.2.1. Modelo A {#fispm-c01-modelo-a-2}

Representa muy pobremente el sistema real, pero podemos resolverlo exactamente.

[]{#modelo-b-2}

#### 1.13.2.2. Modelo B {#fispm-c01-modelo-b-2}

Representa mejor el fenómeno relevante, aunque para obtener una predicción usemos una aproximación controlada.

Podría ocurrir que:

$$P_A$$

sea exacta respecto de A, mientras:

$$P_B$$

sea aproximada respecto de B.

Y, sin embargo:

$$P_B$$

puede describir mucho mejor la observación física.

Por tanto:

$$\boxed{ \text{resultado matemáticamente aproximado} \not\Rightarrow \text{descripción físicamente peor}. }$$ Debemos distinguir al menos dos lugares donde puede aparecer una aproximación.

[]{#aproximación-en-la-construcción-del-modelo}

#### 1.13.2.3. Aproximación en la construcción del modelo {#fispm-c01-aproximaciuxf3n-en-la-construcciuxf3n-del-modelo}

Por ejemplo:

$$[\mathrm{MOD}] \qquad \text{objeto real} \mapsto \text{partícula puntual}.$$

[]{#aproximación-en-la-resolución-matemática}

#### 1.13.2.4. Aproximación en la resolución matemática {#fispm-c01-aproximaciuxf3n-en-la-resoluciuxf3n-matemuxe1tica}

Incluso después de fijar un modelo, puede resultar difícil obtener su solución exacta y empleamos: $[\mathrm{APPROX}].$ Así tenemos cuatro combinaciones conceptuales.

  Modelo físico   Solución matemática       Evaluación
  --------------- ------------------------- -----------------------------------------
  adecuado        exacta                    situación favorable
  adecuado        aproximada y controlada   puede ser físicamente excelente
  inadecuado      exacta                    exactitud formal, mala representación
  inadecuado      aproximada                dos fuentes potenciales de discrepancia

La palabra «exacto» no debe ocultar en qué fila estamos. La potencia del formalismo no elimina sus condiciones de interpretación:

Una estructura matemática puede ser extraordinariamente poderosa.

Puede revelar:

- consecuencias no evidentes;

- invariantes;

- relaciones entre variables;

- imposibilidades;

- simetrías;

- familias completas de soluciones.

Pero su poder lógico comienza **después** de fijar la representación. Si aplicamos una estructura fuera de su dominio físico, la matemática puede continuar funcionando perfectamente mientras la interpretación se degrada.

De ahí la regla:

> nunca evaluar la calidad física de un modelo solamente por la elegancia o solvencia de su formalismo. Comparemos dos procedimientos.

[]{#procedimiento-a}

##### Procedimiento A {#fispm-c01-procedimiento-a}

Usamos una aproximación: $Q_{\mathrm{aprox}}$

y declaramos:

- qué efecto omitimos;

- qué parámetro lo controla;

- qué régimen utilizamos;

- dónde esperamos que falle.

[]{#procedimiento-b}

##### Procedimiento B {#fispm-c01-procedimiento-b}

Usamos una fórmula exacta: $Q_{\mathrm{exacta}}$

pero ocultamos que proviene de una idealización inaplicable al sistema real.

Desde el punto de vista del conocimiento físico, A puede ser superior. No porque la aproximación sea mágicamente más verdadera, sino porque sus límites están **controlados y visibles**. En matemáticas, podemos hablar con precisión de igualdad exacta: $a=b.$

En física experimental, las afirmaciones dependen de:

- procedimientos;

- resolución;

- calibración;

- condiciones;

- convenciones de representación.

Por eso evitaremos expresiones vagas como:

> «este valor físico es absolutamente exacto».

Preguntaremos siempre:

> exacto ¿en qué sentido?

Puede significar:

- exacto por definición;

- exacto dentro del modelo;

- obtenido sin aproximación matemática;

- compatible con la observación dentro de cierta precisión.

Son afirmaciones diferentes. Una expresión exacta puede depender de parámetros medidos y una solución exacta puede quedar excluida por restricciones físicas:

Incluso si el modelo produce una expresión exacta: $P=f(\theta),$

el parámetro: $\theta$

puede provenir de una medición.

Entonces debemos separar:

1.  exactitud de la relación formal $P=f(\theta)$;

2.  conocimiento empírico de $\theta$;

3.  adecuación física del modelo;

4.  precisión de la comparación con la observación.

No desarrollaremos todavía propagación de incertidumbre. Pero la estructura lógica debe quedar visible. En §12 vimos el ejemplo abstracto de dos soluciones: $x_1, \qquad x_2,$

cuando una restricción física exige: $x>0.$

Si: $x_2<0,$

$x_2$ puede seguir siendo solución exacta de la ecuación.

Lo que falla es su admisibilidad física.

Así:

$$\boxed{ \text{solución exacta de la ecuación} \neq \text{estado físicamente permitido}. }$$

Esta distinción será esencial cuando aparezcan condiciones de frontera, restricciones y ramas de soluciones. Consideremos dos tareas.

[]{#tarea-a}

##### Tarea A {#fispm-c01-tarea-a}

Necesitamos una estimación cualitativa.

[]{#tarea-b}

##### Tarea B {#fispm-c01-tarea-b}

Queremos detectar una corrección extremadamente pequeña. El mismo modelo puede ser excelente para A e insuficiente para B.

Por tanto, no preguntamos:

> «¿Es exacto el modelo?»

sino:

> «¿Es suficientemente adecuado para esta tarea, en este régimen y con esta precisión?»

Esto conecta directamente con:

$$\text{definición 1.28}$$

y:

$$\text{definición 1.32}.$$ La distinción también alcanza a la observación: dos resultados matemáticamente diferentes pueden quedar por debajo de la capacidad discriminante del procedimiento experimental.

El ejemplo de la órbita marciana nos dio una lección distinta.[^9]

Una elipse puede ser matemáticamente distinta de un círculo. Pero para cierta excentricidad, la diferencia entre sus semiejes puede ser visualmente pequeña.

Entonces tenemos tres planos:

$$\text{distinción matemática},$$

$$\text{magnitud física de la diferencia},$$

$$\text{capacidad observacional para detectarla}.$$

No deben colapsarse.

Un modelo puede distinguir exactamente dos casos que un instrumento o la percepción disponible no puede separar. Supongamos que dos modelos predicen:

$$P_1=1.000000,$$

$$P_2=1.000001.$$

La diferencia matemática es exacta: $P_1\neq P_2.$ Pero si el procedimiento `[``OBS``]` solo discrimina diferencias del orden de: $0.01,$

esa distinción no es experimentalmente accesible.

Por tanto:

$$\boxed{ \text{distinguibilidad matemática} \not\Rightarrow \text{distinguibilidad física disponible}. }$$

La exactitud del formalismo no puede sustituir la resolución del experimento.

### 1.13.3. Dos principios permanentes {#fispm-c01-dos-principios-permanentes}

**Principio 1.21 --- La exactitud matemática no repara una representación física inadecuada** Una derivación exacta puede garantizar que la conclusión se sigue de las premisas del modelo; no puede garantizar por sí sola que esas premisas representen adecuadamente el sistema real, la pregunta o el régimen considerado.

En forma condensada:

$$\boxed{ \text{corrección formal} \not\Rightarrow \text{adecuación física}. }$$

Este principio permanecerá activo en todo el tratado. **Principio 1.22 --- Una aproximación controlada puede ser físicamente superior a una solución exacta de un modelo inadecuado** Al comparar descripciones físicas, la exactitud matemática de la solución debe evaluarse junto con la adecuación del modelo y su régimen. Una aproximación cuyas omisiones y límites están controlados puede representar mejor el fenómeno que una solución exacta obtenida de premisas físicamente inadecuadas.

Este principio resume la tensión central de §13. La consecuencia editorial y metodológica es importante: el texto debe declarar dónde se ha aproximado y qué relación permanece exacta dentro del modelo simplificado. Supongamos que declaramos: $[\mathrm{APPROX}] \qquad F(x)\approx G(x).$

Después definimos un modelo simplificado usando: $G(x).$

Dentro de ese modelo simplificado podemos obtener exactamente: $H=2G(x).$

No hay contradicción entre: $F\approx G$

y: $H=2G.$ La primera relación compara dos niveles de descripción. La segunda es una igualdad exacta **dentro del modelo simplificado**. Este es un patrón que aparecerá continuamente en física. El protocolo de §6 permite mantener la jerarquía visible.

Por ejemplo: $[\mathrm{APPROX}] \qquad F\approx G,$

seguido de: $[\mathrm{MATH}] \qquad G=K,$

no autoriza escribir sin comentario: $F=K.$ La cadena correcta conserva el estatus: $F\approx G=K,$

y por tanto: $F\approx K$

en el régimen pertinente.

La sintaxis matemática también debe reflejar la epistemología del argumento. Como cierre operativo, cualquier cálculo físico debe auditar corrección, estatus, admisibilidad, régimen, observabilidad y adecuación:

[]{#lista-de-control}

#### 1.13.3.1. Lista de control {#fispm-c01-lista-de-control}

Cada vez que obtengamos un resultado, seguiremos este orden.

[]{#corrección-lógica}

##### 1. Corrección lógica {#fispm-c01-correcciuxf3n-luxf3gica}

> ¿La conclusión se sigue de las premisas?

[]{#corrección-algebraica}

##### 2. Corrección algebraica {#fispm-c01-correcciuxf3n-algebraica}

> ¿Las operaciones matemáticas se realizaron correctamente?

[]{#estatus}

##### 3. Estatus {#fispm-c01-estatus}

> ¿Qué pasos eran `[``MATH``]`, `[``MOD``]` o `[``APPROX``]`?

[]{#admisibilidad}

##### 4. Admisibilidad {#fispm-c01-admisibilidad}

> ¿La solución satisface las restricciones físicas?

[]{#régimen}

##### 5. Régimen {#fispm-c01-ruxe9gimen}

> ¿Estamos dentro de $\mathcal R$?

[]{#observabilidad}

##### 6. Observabilidad {#fispm-c01-observabilidad}

> ¿La cantidad calculada corresponde a una medición bien definida?

[]{#adecuación-1}

##### 7. Adecuación {#fispm-c01-adecuaciuxf3n-1}

> ¿La predicción representa el fenómeno con la precisión necesaria?

Una respuesta positiva en el primer nivel no garantiza las restantes. **Ficha FPM --- Exactitud matemática y adecuación física** 1. **Modelo:** ¿qué sistema está siendo representado? 2. **Premisas:** ¿qué se supone exactamente? 3. **Idealizaciones:** ¿qué rasgos reales se han eliminado? 4. **Aproximaciones:** ¿qué reemplazos no exactos se han realizado? 5. **Derivación:** ¿es exacta dentro de esas premisas? 6. **Soluciones:** ¿todas las soluciones matemáticas son físicamente admisibles? 7. **Parámetros:** ¿son definidos, ajustados o medidos? 8. **Régimen:** ¿pertenece el caso a $\mathcal R$? 9. **Observación:** ¿cómo se conecta el resultado con `[``OBS``]`? 10. **Precisión:** ¿qué nivel de adecuación exige la pregunta? 11. **Comparación:** ¿una aproximación controlada representa mejor el fenómeno? 12. **Conclusión:** ¿qué es exactamente lo que podemos afirmar? **Ejercicio.**

[]{#fispm-t1-c01-e0031}

**Ejercicio 1.31 --- Solución exacta de un modelo inadecuado.**

Un dispositivo convierte una entrada física $x\ge0$ en una señal de salida $y$. Un primer modelo ideal propone: $M_1: \qquad y=2x.$ La electrónica real del dispositivo posee, sin embargo, una saturación física: $0\le y\le10.$ Para entradas pequeñas, las mediciones disponibles son compatibles con $M_1$.

Responde:

1.  Calcula exactamente la predicción de $M_1$ para: $$x=3.$$

2.  Calcula exactamente la predicción de $M_1$ para: $$x=8.$$

3.  Explica por qué el segundo cálculo puede ser matemáticamente correcto y físicamente inadmisible.

4.  Propón un modelo efectivo elemental que incorpore la saturación.

5.  Calcula su predicción para $x=3$ y $x=8$.

6.  ¿Cuál de los dos modelos es «más exacto»? Explica por qué la pregunta es ambigua.

7.  Un estudiante afirma: «Como $M_1$ tiene una fórmula más simple y sus cálculos son exactos, es científicamente superior». Analiza el argumento.

8.  Identifica los estatus `[``MOD``]`, `[``MATH``]` y `[``OBS``]` que deberían aparecer en una investigación real del dispositivo. **Solución.**

[]{#predicción-para-x3}

##### 1. Predicción para $x=3$ {#fispm-c01-predicciuxf3n-para-x3}

El modelo declara: $y=2x.$

Entonces: $y=2\cdot3.$

Por tanto:

$$\boxed{y=6}.$$

El cálculo es exacto dentro de $M_1$.

Además: $6\le10,$

por lo que la predicción no viola la restricción de saturación.

##### 2. Predicción para $x=8$ {#fispm-c01-predicciuxf3n-para-x8}

Aplicando la misma relación: $y=2\cdot8.$

Luego:

$$\boxed{y=16}.$$

Nuevamente, la aritmética es exacta.

##### 3. Corrección matemática y admisibilidad física {#fispm-c01-correcciuxf3n-matemuxe1tica-y-admisibilidad-fuxedsica}

La electrónica real exige: $y\le10.$

Pero: $16>10.$ Por tanto, el valor: $y=16$

es una consecuencia matemática exacta de: $M_1,$

pero no es físicamente admisible para el dispositivo descrito.

La conclusión correcta es:

$$\boxed{ \text{el modelo lineal ha sido extrapolado fuera de su régimen adecuado}. }$$

No:

$$\boxed{ 2\cdot8\neq16. }$$

##### 4. Modelo efectivo con saturación {#fispm-c01-modelo-efectivo-con-saturaciuxf3n}

Podemos proponer:

$$M_2: \qquad y= \begin{cases} 2x, & 0\le x\le5,\\ 10, & x>5. \end{cases}$$

Este modelo conserva la relación lineal donde la salida todavía no ha alcanzado el límite y representa la saturación después. No afirmamos que sea una descripción microscópica completa de la electrónica. Es un modelo efectivo para la pregunta.

##### 5. Predicciones de $M_2$ {#fispm-c01-predicciones-de-m_2}

Para: $x=3,$

como: $3\le5,$

tenemos: $y=2\cdot3=6.$

Para: $x=8,$

como: $8>5,$

tenemos: $y=10.$

Por tanto:

$$\boxed{ M_2(3)=6, \qquad M_2(8)=10. }$$

##### 6. ¿Cuál es más exacto? {#fispm-c01-cuuxe1l-es-muxe1s-exacto}

La pregunta mezcla dos sentidos.

Dentro de sus propias fórmulas, ambos modelos permiten cálculos exactos. Pero como representación del dispositivo en el régimen que incluye $x=8$, $M_2$ es físicamente más adecuado porque incorpora la restricción de saturación.

Por tanto:

$$\boxed{ \text{exactitud matemática} \neq \text{adecuación física}. }$$

##### 7. Simplicidad y superioridad científica {#fispm-c01-simplicidad-y-superioridad-cientuxedfica}

El argumento del estudiante es incorrecto. La sencillez de: $y=2x$

puede ser una virtud dentro de su régimen. Pero la simplicidad formal no compensa una predicción físicamente imposible para el sistema.

La comparación debe incluir:

- régimen;

- restricciones físicas;

- observaciones;

- pregunta;

- precisión requerida.

Así:

$$\boxed{ \text{fórmula simple + cálculo exacto} \not\Rightarrow \text{modelo físicamente superior}. }$$

##### 8. Estatus {#fispm-c01-estatus-1}

La relación: $y=2x$

puede aparecer como: $[\mathrm{MOD}]$

cuando se declara como idealización lineal del dispositivo. La derivación: $x=3 \Longrightarrow y=6$

es: $[\mathrm{MATH}].$ La regla que conecta la señal $y$ con una lectura real del instrumento requiere: $[\mathrm{OBS}].$ La existencia y valor de la saturación física deben establecerse mediante la construcción del dispositivo, documentación o evidencia experimental pertinente; no surgen de la ecuación lineal.

La solución completa muestra:

$$\boxed{ \text{\parbox{.66\linewidth}{\centering una matemática impecable puede revelar precisamente que el modelo físico necesita revisión}}. }$$

### 1.13.4. Síntesis {#fispm-c01-suxedntesis-10}

La sección completa puede comprimirse en una pregunta doble:

$$\boxed{\text{¿es correcta la consecuencia matemática?}}$$

y

$$\boxed{\text{¿es físicamente adecuada la representación?}}$$

Responder afirmativamente a la primera no resuelve la segunda. Una aproximación controlada puede representar mejor el fenómeno que una solución exacta de un modelo inadecuado.

[]{#cómo-leer-el-resto-de-física-para-matemáticos}

[]{#fispm-t1-c01-s14}

[]{#fpm-i-01-s14}

## 1.14. Cómo leer el resto de Física para matemáticos {#fispm-c01-cuxf3mo-leer-el-resto-de-fuxedsica-para-matemuxe1ticos}

[]{#este-capítulo-no-era-un-prólogo}

### 1.14.1. Este capítulo no era un prólogo {#fispm-c01-este-capuxedtulo-no-era-un-pruxf3logo}

Podría parecer que hemos dedicado demasiadas páginas a hablar de física antes de empezar a «hacer física». Pero el objetivo de este capítulo nunca fue retrasar las ecuaciones. Fue aprender a leerlas.

A partir del capítulo siguiente comenzarán a aparecer de manera progresiva:

- magnitudes;

- unidades;

- vectores;

- curvas;

- leyes de movimiento;

- energía;

- campos;

- ecuaciones diferenciales;

- principios variacionales;

- operadores;

- probabilidades;

- estructuras geométricas.

Cada una de esas herramientas puede ser estudiada matemáticamente.

Pero en este libro siempre aparecerá además una segunda pregunta:

> **¿qué trabajo físico está realizando aquí esta estructura matemática?**

Este es el contrato de lectura del resto de la obra. Todo tema importante intentará conservar, cuando corresponda, la secuencia:

$$\boxed{ \text{fenómeno físico} \longleftrightarrow \text{modelo matemático} \longleftrightarrow \text{estructura matemática}. }$$

La flecha doble es esencial.

No leeremos la física como una simple aplicación posterior de matemáticas ya terminadas. Tampoco trataremos la matemática como una colección de trucos para producir números. Buscaremos un movimiento en ambas direcciones.

La física plantea problemas que exigen estructuras matemáticas. La matemática reorganiza la comprensión física y permite descubrir consecuencias que no eran visibles al comienzo.

### 1.14.2. El protocolo permanente FPM {#fispm-c01-el-protocolo-permanente-fpm}

En vez de repetir por separado cada una de las quince preguntas desarrolladas a lo largo del capítulo, las reuniremos desde ahora en un único protocolo acumulativo. Podemos condensar todo el capítulo en una secuencia.

**Protocolo permanente de lectura FPM**

**1. Fenómeno**\
¿Qué ocurre físicamente?

**2. Pregunta**\
¿Qué queremos explicar, predecir o comparar?

**3. Sistema**\
¿Qué incluimos y qué dejamos en el entorno?

**4. Estado y variables**\
¿Qué información conserva el modelo?

**5. Representación**\
¿Qué objetos matemáticos utilizamos y qué significan?

**6. Estatus**\
¿Qué es definición, dato empírico, postulado, modelo, aproximación, condición o consecuencia matemática?

**7. Estructura matemática**\
¿Qué teoremas, operaciones o estructuras producen las consecuencias?

**8. Régimen**\
¿Dónde esperamos que la representación sea adecuada?

**9. Observación**\
¿Cómo se conecta el formalismo con una medición?

**10. Predicción o explicación**\
¿Qué resultado nuevo produce y qué estructura lo hace inteligible?

**11. Contraste**\
¿Qué observación podría discriminar esta descripción de alternativas?

**12. Revisión**\
Si falla, ¿qué parte del paquete predictivo debe auditarse?

Esta secuencia no será una plantilla rígida.

No todos los problemas necesitan doce apartados explícitos. Pero todos los pasos relevantes deben poder reconstruirse.

### 1.14.3. Cómo se usará el protocolo en el resto del tratado {#fispm-c01-cuxf3mo-se-usaruxe1-el-protocolo-en-el-resto-del-tratado}

Cuando una teoría física requiera una herramienta matemática todavía no disponible, no la utilizaremos silenciosamente.

El texto deberá:

1.  identificar la necesidad física;

2.  declarar el objeto matemático requerido;

3.  construir o recordar sus definiciones;

4.  demostrar los resultados necesarios;

5.  volver al problema físico;

6.  interpretar qué ganó la descripción.

La progresión será:

$$\boxed{ \text{problema físico} \to \text{necesidad matemática} \to \text{estructura} \to \text{retorno a la física}. }$$

Esta regla evita dos extremos:

- convertir la física en un pretexto para una lista de fórmulas;

- convertir el libro en un tratado abstracto de matemáticas desconectado del fenómeno. Cuando un resultado sea puramente matemático, deberá distinguirse de las premisas físicas que permiten aplicarlo.

Por ejemplo:

$$[\mathrm{POST}] + [\mathrm{MOD}] + [\mathrm{IC}] \longrightarrow [\mathrm{MATH}].$$

El teorema matemático puede tener demostración completa. Pero la aplicación física debe conservar visibles las hipótesis que lo hacen relevante.

Así podremos responder siempre:

> ¿qué parte del argumento está demostrada matemáticamente y qué parte pertenece a la construcción física del modelo? Las aproximaciones no serán tratadas como errores vergonzosos que debamos esconder.

Son una herramienta central de la física. Pero deben estar controladas.

Cuando sea posible, registraremos:

$$\text{efecto omitido},$$

$$\text{parámetro de control},$$

$$\text{régimen},$$

$$\text{criterio de fallo}.$$

El objetivo no es eliminar las aproximaciones. Es saber exactamente qué trabajo realizan. Los ejercicios del tratado pertenecen a familias distintas.

No todos pedirán calcular.

Encontraremos:

- `E-CALC` --- cálculo;

- `E-DER` --- derivación;

- `E-PROOF` --- demostración;

- `E-MOD` --- modelización;

- `E-DIM` --- análisis dimensional;

- `E-EST` --- estimación;

- `E-CON` --- comprensión conceptual;

- `E-LIM` --- límites y regímenes;

- `E-FAIL` --- diagnóstico de fallos;

- `E-NUM` --- exploración numérica;

- `E-HIST` --- reconstrucción histórica o conceptual.

La solución completa no consistirá solamente en producir el resultado final.

Deberá hacer visible qué tipo de razonamiento exige el problema.

### 1.14.4. Señales de alarma {#fispm-c01-seuxf1ales-de-alarma}

A lo largo del libro convendrá detenerse cuando aparezca alguna de estas situaciones:

[]{#una-ecuación-sin-interpretación}

#### 1.14.4.0. 1. Una ecuación sin interpretación {#fispm-c01-una-ecuaciuxf3n-sin-interpretaciuxf3n .unnumbered}

Preguntar:

> ¿qué significan los símbolos?

[]{#una-aproximación-sin-régimen}

#### 1.14.4.0. 2. Una aproximación sin régimen {#fispm-c01-una-aproximaciuxf3n-sin-ruxe9gimen .unnumbered}

Preguntar:

> ¿qué la controla?

[]{#una-idealización-sin-omisión-declarada}

#### 1.14.4.0. 3. Una idealización sin omisión declarada {#fispm-c01-una-idealizaciuxf3n-sin-omisiuxf3n-declarada .unnumbered}

Preguntar:

> ¿qué se dejó fuera?

[]{#una-predicción-sin-procedimiento-observacional}

#### 1.14.4.0. 4. Una predicción sin procedimiento observacional {#fispm-c01-una-predicciuxf3n-sin-procedimiento-observacional .unnumbered}

Preguntar:

> ¿cómo se mediría?

[]{#una-solución-matemáticamente-válida-pero-extraña-físicamente}

#### 1.14.4.0. 5. Una solución matemáticamente válida pero extraña físicamente {#fispm-c01-una-soluciuxf3n-matemuxe1ticamente-vuxe1lida-pero-extrauxf1a-fuxedsicamente .unnumbered}

Preguntar:

> ¿es admisible dentro del modelo?

[]{#un-desacuerdo-experimental}

#### 1.14.4.0. 6. Un desacuerdo experimental {#fispm-c01-un-desacuerdo-experimental .unnumbered}

Preguntar:

> ¿qué parte del paquete predictivo debe auditarse?

[]{#una-teoría-más-avanzada-que-reemplaza-otra}

#### 1.14.4.0. 7. Una teoría más avanzada que «reemplaza» otra {#fispm-c01-una-teoruxeda-muxe1s-avanzada-que-reemplaza-otra .unnumbered}

Preguntar:

> ¿qué régimen recupera y qué estructura cambia?

[]{#una-fórmula-muy-elegante}

#### 1.14.4.0. 8. Una fórmula muy elegante {#fispm-c01-una-fuxf3rmula-muy-elegante .unnumbered}

Preguntar:

> ¿su elegancia matemática coincide con adecuación física?

Estas preguntas no son obstáculos.

Son el método.

### 1.14.5. Principio final del capítulo {#fispm-c01-principio-final-del-capuxedtulo}

**Principio 1.23 --- Ningún cálculo físico se cierra al obtener un número** Un cálculo físico termina solamente cuando el resultado ha sido interpretado respecto del sistema, las premisas, el estatus de las relaciones, el régimen de validez, las restricciones físicas y la conexión observacional pertinentes.

En forma esquemática:

$$\boxed{ \text{cálculo} \to \text{interpretación} \to \text{control físico}. }$$

Este será el principio operativo que acompañará todo el tratado. **Ejercicio de síntesis.**

[]{#fispm-t1-c01-e0032}

**Ejercicio 1.32 --- Ficha completa de un modelo.**

Un pequeño carro se desplaza por una pista recta. Una cámara registra su posición en instantes igualmente espaciados.

En una primera serie de observaciones se obtiene:

$$x_0=0,$$

$$x_1=2,$$

$$x_2=4,$$

$$x_3=6.$$

Las posiciones están expresadas en una misma unidad de longitud. No utilizaremos todavía una teoría mecánica para explicar el movimiento. Se propone el modelo empírico discreto: $[\mathrm{MOD}] \qquad x_{n+1}=x_n+d,$

con: $d=2.$

Construye una **ficha FPM completa** respondiendo:

1.  ¿Cuál es el fenómeno?

2.  Formula una pregunta física concreta.

3.  Define sistema y entorno.

4.  Propón un espacio de estados mínimo para la pregunta.

5.  Identifica variable de estado, parámetro y observable.

6.  Explica el estatus de: $$x_{n+1}=x_n+d.$$

7.  Identifica una posible condición inicial.

8.  Formula una predicción para $x_4$.

9.  Explica qué parte de esa predicción es `[``MATH``]`.

10. Explica qué regla `[``OBS``]` sería necesaria para contrastarla.

11. Declara al menos dos idealizaciones o simplificaciones del modelo.

12. Propón un régimen de validez cualitativo.

13. Si la cámara observa $x_4=8$, ¿qué podemos concluir?

14. Si observa $x_4=7.1$, aplica la lógica de §12 y enumera al menos cuatro elementos a auditar.

15. Explica por qué el modelo no constituye todavía una teoría mecánica del carro.

16. Explica qué observación nueva sería útil para probar si la regla continúa funcionando.

17. Evalúa la exactitud matemática y la adecuación física por separado.

18. Resume el modelo usando: $$(\mathcal M,\mathfrak I_{\mathcal M}).$$ **Solución.**

[]{#fenómeno-1}

##### 1. Fenómeno {#fispm-c01-fenuxf3meno-2}

El fenómeno es el cambio de posición de un carro sobre una pista recta observado mediante una cámara en instantes sucesivos. Todavía no afirmamos qué causa el movimiento.

##### 2. Pregunta física {#fispm-c01-pregunta-fuxedsica}

Una pregunta concreta puede ser:

> ¿Qué posición registrará la cámara en el siguiente instante si continúa la regularidad observada?

Esta pregunta es predictiva y deliberadamente modesta.

##### 3. Sistema y entorno {#fispm-c01-sistema-y-entorno}

**Sistema:**

el carro, representado solo mediante la información necesaria para registrar su posición.

**Entorno:**

la pista, la cámara y cualquier agente externo que pueda afectar al movimiento quedan fuera de la frontera inicial del sistema, aunque parte de sus efectos puede estar implícitamente presente en la regularidad empírica. Si más adelante esos efectos importan, la frontera deberá revisarse.

##### 4. Espacio de estados mínimo {#fispm-c01-espacio-de-estados-muxednimo}

Para esta pregunta elemental podemos utilizar:

$$\mathcal S = \{(n,x): n\in\mathbb N,\ x\in\mathbb R\}.$$

El estado modelado conserva:

- el índice temporal discreto $n$;

- la posición $x$.

No afirmamos que esto sea suficiente para toda pregunta mecánica sobre el carro. Es suficiente para la tarea predictiva propuesta.

##### 5. Variable, parámetro y observable {#fispm-c01-variable-paruxe1metro-y-observable}

Una variable de estado es:

$$x.$$

El parámetro del modelo es: $d=2.$ El observable es la posición registrada por la cámara: $O(n,x)=x.$ En una realización experimental, esa cantidad necesita una regla de calibración espacial.

##### 6. Estatus de la regla {#fispm-c01-estatus-de-la-regla}

La relación: $x_{n+1}=x_n+d$

se ha propuesto para representar exactamente, dentro del modelo, la regularidad observada. Por tanto, en este contexto su estatus principal es: $[\mathrm{MOD}].$ Podría haber sido motivada por datos `[``EMP``]`, pero no la hemos derivado de una teoría mecánica.

##### 7. Condición inicial {#fispm-c01-condiciuxf3n-inicial-1}

Podemos tomar: $[\mathrm{IC}] \qquad x_0=0.$

Esto selecciona una realización concreta de la regla.

##### 8. Predicción {#fispm-c01-predicciuxf3n-1}

Como: $x_3=6$

y: $d=2,$

la regla da: $x_4=x_3+d.$

Entonces: $x_4=6+2=8.$

Por tanto:

$$\boxed{x_4=8}.$$

##### 9. Parte matemática {#fispm-c01-parte-matemuxe1tica}

Una vez aceptados:

$$x_3=6,$$

$$d=2$$

y: $x_{n+1}=x_n+d,$

la inferencia: $x_4=8$

es: $[\mathrm{MATH}].$ La aritmética es exacta dentro del modelo.

##### 10. Regla observacional {#fispm-c01-regla-observacional}

Necesitamos una conexión:

$$[\mathrm{OBS}] \qquad x \longleftrightarrow \text{posición inferida de la imagen de la cámara mediante una escala calibrada}.$$

Debemos saber:

- qué punto del carro representa su posición;

- dónde está el origen;

- qué unidad se utiliza;

- cómo la imagen se convierte en una coordenada.

Sin esa mediación, el número $8$ sigue siendo solo parte del formalismo.

##### 11. Idealizaciones o simplificaciones {#fispm-c01-idealizaciones-o-simplificaciones}

Entre otras:

1.  representamos el carro mediante una única coordenada;

2.  ignoramos su orientación y dimensiones;

3.  tratamos los instantes como igualmente espaciados;

4.  suponemos que el mismo incremento $d$ continúa siendo adecuado;

5.  ignoramos explícitamente causas físicas del movimiento.

Estas omisiones son aceptables solo respecto de la pregunta propuesta.

##### 12. Régimen cualitativo {#fispm-c01-ruxe9gimen-cualitativo}

Podemos declarar provisionalmente:

> la regla se utiliza para los próximos registros mientras la pista, la preparación, el intervalo entre imágenes y el comportamiento observado permanezcan comparables con los de la serie inicial.

No es todavía un régimen cuantitativo sofisticado. Pero hace visible que no estamos autorizados a extrapolar indefinidamente.

##### 13. Si observamos $x_4=8$ {#fispm-c01-si-observamos-x_48}

El nuevo dato es compatible con la predicción.

Podemos afirmar:

> el modelo ha superado esta prueba adicional.

No podemos afirmar:

> la regla ha sido demostrada como ley única del movimiento.

Proposición 1.1 ya nos enseñó que datos finitos no determinan una única ley funcional.

##### 14. Si observamos $x_4=7.1$ {#fispm-c01-si-observamos-x_47.1}

Tenemos una discrepancia.

Debemos auditar, por ejemplo:

1.  **regla del modelo:** quizá el incremento dejó de ser constante;

2.  **condición o dato anterior:** quizá $x_3$ fue mal determinado;

3.  **parámetro:** quizá $d$ no era realmente $2$;

4.  **mediación observacional:** quizá la cámara o calibración introdujo un error;

5.  **régimen:** quizá cambió alguna condición de la pista o preparación;

6.  **idealización:** quizá un efecto omitido se volvió relevante.

La observación no identifica automáticamente cuál de estas alternativas es responsable.

##### 15. Por qué no es todavía una teoría mecánica {#fispm-c01-por-quuxe9-no-es-todavuxeda-una-teoruxeda-mecuxe1nica}

El modelo: $x_{n+1}=x_n+2$

describe una regularidad de posiciones.

No proporciona todavía:

- principios generales de movimiento;

- una estructura aplicable a muchas clases de sistemas;

- mecanismos;

- una teoría de interacciones;

- reglas generales para construir otros modelos.

Por tanto:

$$\boxed{ \text{modelo empírico} \neq \text{teoría mecánica}. }$$

##### 16. Nueva prueba {#fispm-c01-nueva-prueba}

Podemos observar: $x_5.$ El modelo predice: $x_5=10.$ Pero una prueba más informativa podría también cambiar deliberadamente una condición del experimento y preguntar si $d$ permanece constante. La elección depende de qué aspecto del modelo queramos poner a prueba.

##### 17. Exactitud y adecuación {#fispm-c01-exactitud-y-adecuaciuxf3n}

**Exactitud matemática:**

dentro de: $x_{n+1}=x_n+2,$

la predicción: $x_4=8$

se obtiene exactamente.

**Adecuación física:**

solo puede evaluarse comparando la regla con nuevas observaciones dentro del régimen pertinente.

Por tanto:

$$\boxed{ \text{predicción algebraicamente exacta} \neq \text{garantía de adecuación física}. }$$

##### 18. Ficha formal {#fispm-c01-ficha-formal}

Podemos escribir esquemáticamente:

$$\mathcal M = (\mathcal S,X,\theta,\mathcal L,I,B,\mathcal R),$$

con:

- $\mathcal S$: estados discretos $(n,x)$;

- $X$: posición $x$ y observable asociado;

- $\theta$: $d=2$;

- $\mathcal L$: regla $x_{n+1}=x_n+d$;

- $I$: $x_0=0$;

- $B$: no intervienen condiciones de frontera relevantes en este modelo mínimo;

- $\mathcal R$: serie de observaciones bajo condiciones comparables.

El diccionario: $\mathfrak I_{\mathcal M}$

declara que:

- $n$ representa el índice de una imagen tomada a intervalos iguales;

- $x$ representa una posición sobre la pista;

- $d$ representa el incremento de posición entre registros;

- `[``OBS``]` conecta píxeles o marcas de la imagen con la coordenada física.

La unidad mínima de lectura es entonces:

$$\boxed{ (\mathcal M,\mathfrak I_{\mathcal M}). }$$

El ejercicio ha recorrido prácticamente todo el protocolo del capítulo.

### 1.14.6. Cierre {#fispm-c01-cierre}

Empezamos con una pregunta:

> **¿Qué convierte una pregunta sobre el mundo en un problema físico matemáticamente tratable?**

La respuesta no fue «una ecuación».

Fue una arquitectura.

$$\boxed{\begin{gathered} \text{fenómeno} \to \text{pregunta}\\[2pt]\Downarrow\\[2pt]\text{sistema} \to \text{modelo}\\[2pt]\Downarrow\\[2pt]\text{matemática} \to \text{predicción}\\[2pt]\Downarrow\\[2pt]\text{observación} \to \text{revisión}. \end{gathered}}$$

Aprendimos que:

$$\boxed{ \text{objeto físico} \neq \text{objeto matemático que lo representa}; }$$

que:

$$\boxed{ \text{ley} \neq \text{modelo} \neq \text{teoría}; }$$

que:

$$\boxed{ \text{ajuste} \neq \text{predicción} \neq \text{explicación}; }$$

que:

$$\boxed{ \text{datos finitos} \not\Rightarrow \text{ley única}; }$$

que:

$$\boxed{ \text{fallo predictivo} \not\Rightarrow \text{culpable único}; }$$

y, finalmente:

$$\boxed{ \text{exactitud matemática} \neq \text{adecuación física}. }$$

Estas distinciones no pertenecen únicamente al capítulo inicial.

Constituyen la gramática del resto del tratado.

A partir del próximo capítulo comenzaremos a construir las primeras herramientas cuantitativas de esa gramática:

$$\boxed{ \text{magnitudes, unidades y análisis dimensional}. }$$

Las ecuaciones podrán ser cada vez más sofisticadas.

La pregunta seguirá siendo la misma:

> **¿Qué relación existe entre el fenómeno, el modelo y la estructura matemática que estamos usando para comprenderlo?**

------------------------------------------------------------------------

[]{#referencias-del-capítulo}

## 1.14. Referencias del capítulo {#fispm-c01-referencias-del-capuxedtulo .unnumbered}

Las fuentes siguientes cumplen dos funciones distintas. Algunas sustentan atribuciones explícitas o ejemplos identificables del capítulo; otras actuaron como **fuentes de control** para el enfoque y la arquitectura, sin que el texto reproduzca su secuencia ni su prosa. Las formulaciones matemáticas proposición 1.1 y proposición 1.2 y el protocolo de lectura FPM son desarrollos propios de este tratado.

- Arnold, V. I. *Mathematical Understanding of Nature: Essays on Amazing Physical Phenomena and Their Understanding by Mathematicians*. Trad. Alexei Sossinsky y Olga Sipacheva. Providence, RI: American Mathematical Society, 2014. Para este capítulo: prefacio, p. xiii; cap. 1, «The Eccentricity of the Keplerian Orbit of Mars», pp. 1--2.

- Feynman, Richard P.; Leighton, Robert B.; Sands, Matthew. *The Feynman Lectures on Physics*. Vol. I. New Millennium Edition. New York: Basic Books, 2011. Para este capítulo: cap. 1, §1-1, pp. 1-1--1-2.

- Hassani, Sadri. *Mathematical Physics: A Modern Introduction to Its Foundations*. 2.ª ed. Cham: Springer, 2013. Para este capítulo: «Preface to First Edition», pp. xi--xiii, especialmente p. xii.

- Schramm, Alec J. *Mathematical Methods and Physical Insights: An Integrated Approach*. Cambridge: Cambridge University Press, 2022. Para este capítulo: cap. 1, «Prelude: Symbiosis», pp. 3--5.

- Shankar, R. *Fundamentals of Physics I: Mechanics, Relativity, and Thermodynamics*. Edición ampliada. New Haven: Yale University Press, 2019. Para este capítulo: cap. 1, §1.2, p. 3.

- Spivak, Michael. *Physics for Mathematicians: Mechanics I*. Houston: Publish or Perish, 2010. Para este capítulo: prefacio, p. vii.

[^1]: Feynman, Leighton y Sands, *The Feynman Lectures on Physics*, vol. I, cap. 1, §1-1, p. 1-1.

[^2]: Hassani, *Mathematical Physics*, 2.ª ed., «Preface to First Edition», p. xii.

[^3]: Shankar, *Fundamentals of Physics I*, edición ampliada, cap. 1, §1.2, p. 3.

[^4]: Arnold, *Mathematical Understanding of Nature*, prefacio, p. xiii.

[^5]: Feynman, Leighton y Sands, *The Feynman Lectures on Physics*, vol. I, cap. 1, §1-1, pp. 1-1--1-2.

[^6]: Feynman, Leighton y Sands, *The Feynman Lectures on Physics*, vol. I, cap. 1, §1-1, p. 1-2.

[^7]: Arnold, *Mathematical Understanding of Nature*, cap. 1, pp. 1--2. El ejercicio conserva el motivo matemático y físico, pero reformula el enunciado, amplía las preguntas y desarrolla una solución propia.

[^8]: Spivak, *Physics for Mathematicians: Mechanics I*, prefacio, p. vii.

[^9]: Arnold, *Mathematical Understanding of Nature*, cap. 1, pp. 1--2.
