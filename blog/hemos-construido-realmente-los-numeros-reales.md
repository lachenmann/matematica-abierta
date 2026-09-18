---
title: "¿Hemos construido realmente los números reales?"
subtitle: "Wildberger, la existencia matemática y el problema de la construcción"
description: "Una indagación sobre qué afirmamos al construir los números reales: existencia formal, representación, información efectiva y dependencias lógicas, a partir de las objeciones de Norman J. Wildberger."
content-id: MA-ART-0002
content-type: article
status: published
date-created: 2026-09-15
date-modified: 2026-09-18
areas:
  - fundamentos
  - analisis
  - logica
level: intermedio
topics:
  - numeros-reales
  - dedekind
  - constructivismo
  - computabilidad
  - zfc
  - axioma-de-eleccion
  - wildberger
  - fundamentos-de-la-matematica
related:
  - Tratado de análisis
  - Tratado de álgebra
provenance:
  type: original-synthesis
  sources:
    - Norman J. Wildberger, "Real numbers: A critique and way forward" (versión difundida en ResearchGate, 2015)
    - Norman J. Wildberger, "Set Theory: Should You Believe?" (circulaba en 2006; versión difundida en ResearchGate, 2015)
    - Errett Bishop, "Foundations of Constructive Analysis" (1967)
    - Stanford Encyclopedia of Philosophy, "Constructive Mathematics"
    - Stanford Encyclopedia of Philosophy, "The Axiom of Choice"
license: GFDL-1.3-or-later
publication-target: matematicaabierta.cl/blog
---

Es habitual que, una vez completada la construcción de los números reales, abandonemos el asunto de su existencia y comencemos a trabajar con ellos como si hubiesen estado allí desde siempre. Partimos de los racionales, introducimos cortaduras de Dedekind o clases de equivalencia de sucesiones de Cauchy, definimos las operaciones y el orden, demostramos las propiedades correspondientes y obtenemos, finalmente, un cuerpo ordenado completo. El resultado de este recorrido es extraordinariamente fecundo: sobre él edificamos el análisis, buena parte de la geometría y numerosos modelos de las ciencias. Sin embargo, hay una pregunta que el éxito de la construcción tiende a dejar en segundo plano: ¿qué queremos decir, exactamente, cuando afirmamos que hemos *construido* un número real?

Quizá parezca una pregunta innecesaria. Hemos entregado definiciones, hemos establecido teoremas y sabemos operar dentro del sistema resultante. ¿Qué más podría exigirse? Pero basta examinar con detenimiento el verbo *construir* para advertir que no siempre designa la misma actividad. Una cosa es demostrar que cierto objeto existe de acuerdo con unos axiomas; otra, especificarlo individualmente; otra, disponer de un procedimiento que permita aproximarlo tanto como deseemos; y otra, finalmente, decidir de manera efectiva las propiedades que le atribuimos. Las distinciones pueden pasar inadvertidas mientras utilizamos los números reales de manera ordinaria, pero reaparecen apenas preguntamos qué información contiene, en realidad, una demostración de existencia.

Norman J. Wildberger ha hecho de esta incomodidad una crítica explícita. En *Real numbers: A critique and way forward* cuestiona las presentaciones habituales del continuo mediante decimales infinitos, sucesiones de Cauchy y cortaduras; en *Set Theory: Should You Believe?* extiende sus objeciones a los fundamentos conjuntistas y al tratamiento del infinito actual. Su posición es marcadamente finitista y sus juicios sobre la matemática contemporánea son mucho más radicales que las conclusiones que defenderemos aquí. Conviene, por lo mismo, distinguir sus tesis de las preguntas que permiten formular: atender una objeción no equivale a aceptar el programa filosófico del que procede.

Mi propósito no es sustituir una ortodoxia por otra. Me interesa examinar qué afirma efectivamente una construcción clásica, qué deja abierto desde una perspectiva computacional y de qué manera podemos incorporar esas diferencias a una práctica matemática más explícita. Si logramos hacerlo, la controversia dejará de ser una disputa sobre la respetabilidad de los objetos infinitos y se convertirá en una investigación sobre los diversos sentidos de la palabra *existir*.

## 1. Los diversos sentidos de una construcción

Comencemos con una afirmación aparentemente sencilla: existe un objeto $x$ que satisface la propiedad $P$. En el lenguaje de la lógica escribimos

$$
\exists x\,P(x).
$$

Dentro de una teoría clásica, una demostración de esta fórmula establece la existencia de un testigo en el sentido admitido por la teoría. No se sigue de ello que la demostración entregue un algoritmo para encontrarlo; incluso puede ocurrir que el argumento dependa del principio del tercero excluido o de alguna forma de elección sin producir una descripción efectiva del objeto. Nada de esto constituye, por sí solo, un defecto lógico. Constituye una característica de la información que la prueba proporciona.

Pensemos, en contraste, en una construcción que nos permita entregar, para cada precisión solicitada, una aproximación racional acompañada de una cota de error. En ese caso poseemos algo más que una caracterización existencial: contamos con un procedimiento de cálculo. Pero tampoco debemos identificar apresuradamente *ser computable* con *ser decidible*. Podemos calcular aproximaciones de un número sin disponer de un algoritmo uniforme que resuelva todas las preguntas de igualdad entre números dados mediante programas de aproximación.

La diferencia puede expresarse así, sin convertirla en una jerarquía de legitimidad:

$$
\text{existencia formal},\qquad
\text{definición},\qquad
\text{representación},\qquad
\text{computabilidad},\qquad
\text{decidibilidad}.
$$

Son nociones relacionadas, pero ninguna debe sustituirse automáticamente por otra. Además, una definición puede ser finita en su extensión escrita y, sin embargo, determinar un objeto que no sea computable: una fórmula breve no es necesariamente un algoritmo. Del mismo modo, no disponer de una especificación efectiva para un objeto arbitrario no significa que el sistema formal que lo contiene sea inconsistente.

La pregunta que conviene conservar a lo largo de este ensayo no es, entonces, si los reales existen *de verdad*, formulación que mezcla problemas matemáticos y ontológicos antes de haberlos delimitado. Es otra, más precisa: cuando una teoría nos autoriza a afirmar que existe un número real, ¿qué clase de información hemos obtenido y qué principios hicieron posible esa afirmación?

## 2. Dedekind: un corte en los racionales

Recordemos brevemente una de las construcciones clásicas. Una cortadura inferior de Dedekind es un subconjunto $L\subsetneq\mathbb Q$ que no está vacío, es cerrado hacia abajo y carece de máximo. Con la convención usual para las cortaduras inferiores, sus elementos representan los racionales situados estrictamente a la izquierda del real correspondiente. Podemos reunir todas las cortaduras en una colección $\mathbb R_D$, definir sobre ella suma, producto y orden, y demostrar que posee la estructura de un cuerpo ordenado completo. La construcción mediante cortaduras puede desarrollarse en la teoría de conjuntos ZF; **no requiere, por sí sola, añadir el axioma de elección completo**.

Hasta aquí no hay indeterminación alguna en el sentido lógico: las condiciones que debe satisfacer una cortadura son precisas. La dificultad que Wildberger quiere poner en primer plano aparece cuando pasamos de una cortadura especialmente accesible a una cortadura arbitraria.

Tomemos como ejemplo la asociada a $\sqrt 2$:

$$
L_{\sqrt 2}
:=
\bigl\{q\in\mathbb Q:q<0\ \text{o}\ q^2<2\bigr\}.
$$

Si alguien nos entrega un racional $q$, podemos decidir en un número finito de operaciones si pertenece a $L_{\sqrt 2}$. Primero comprobamos si es negativo; si no lo es, comparamos exactamente $q^2$ con $2$. La pertenencia está sometida a una regla efectiva. Más aún: comenzando con el intervalo $[1,2]$, podemos dividirlo sucesivamente por la mitad y conservar en cada paso el subintervalo cuyos extremos encierran la raíz positiva de $2$. Después de $n$ bisecciones obtenemos extremos racionales $a_n,b_n$ tales que

$$
a_n^2\leq 2\leq b_n^2,
\qquad
0\leq b_n-a_n=2^{-n}.
$$

Hemos producido una representación que permite aproximar $\sqrt 2$ con un error controlado. La cortadura no se limita, en este caso, a decirnos qué objeto existe: nos proporciona una puerta de entrada al cálculo.

Ahora consideremos una cortadura $L$ cualquiera. La definición estructural nos dice qué condiciones satisface, pero no nos entrega necesariamente un algoritmo que, para cada $q\in\mathbb Q$, decida

$$
q\in L\;?
$$

En la teoría clásica podemos cuantificar sobre esas cortaduras sin imponerles un procedimiento uniforme de pertenencia. Esta es una distinción genuina: *definir la clase de todas las cortaduras* no equivale a *poseer un programa que reconozca la pertenencia a cada cortadura que la integra*.

La objeción finitista cuestiona el tratamiento de tales totalidades como objetos ya dados. La respuesta clásica consiste en señalar que sus criterios de existencia y de definición no incluyen la exigencia de computabilidad. Ambas posiciones divergen, por tanto, en sus condiciones de admisión de los objetos, no en una contradicción descubierta dentro de la construcción de Dedekind. Si queremos avanzar, debemos hacer explícito ese desacuerdo en lugar de presentarlo como si alguna de las partes hubiese probado más de lo que realmente probó.

## 3. Cauchy: una sucesión que se aproxima a algo

La segunda construcción usual parece, a primera vista, más cercana a la actividad de calcular. Consideramos sucesiones de números racionales $(a_n)$ que satisfacen la condición de Cauchy y declaramos equivalentes dos de ellas cuando su diferencia converge a cero:

$$
(a_n)\sim(b_n)
\quad\Longleftrightarrow\quad
\lim_{n\to\infty}|a_n-b_n|=0.
$$

Un número real queda representado por una clase de equivalencia $[(a_n)]$. En el marco clásico habitual, esta construcción y la de Dedekind conducen al cuerpo ordenado completo de los reales. En contextos constructivos, sin embargo, la relación entre ambas exige prestar atención a la representación elegida y a los principios de elección disponibles: no conviene trasladar sin examen todas las equivalencias de un marco lógico a otro.

La propia condición de Cauchy nos permite localizar el problema de la información. Saber que

$$
\forall\varepsilon>0\;\exists N\;\forall m,n\geq N,
\qquad |a_m-a_n|<\varepsilon
$$

no significa, por sí mismo, que podamos *calcular* un valor adecuado de $N$ a partir de $\varepsilon$. Para ello necesitamos información adicional: un **módulo efectivo de Cauchy**, por ejemplo una función computable $N:\mathbb N\to\mathbb N$ que cumpla

$$
\forall k\in\mathbb N\;\forall m,n\geq N(k),
\qquad |a_m-a_n|<2^{-k}.
$$

Si podemos calcular también los términos racionales $a_n$, un módulo de esta clase nos permite producir aproximaciones al límite con precisión prescrita. Sin él, el simple hecho de generar uno tras otro los términos de una sucesión no asegura que podamos calcular su límite.

No se trata de una sutileza vacía. Las **sucesiones de Specker** son sucesiones computables de racionales, monótonamente crecientes y acotadas, cuyo límite clásico no es un real computable. Cada término puede calcularse; el límite, en cambio, no admite aproximación algorítmica uniforme con error arbitrariamente prescrito. La completitud clásica garantiza el límite; la información efectiva disponible en la sucesión no alcanza para calcularlo.

Aquí aparece una diferencia que merece acompañarnos cuando estudiemos el análisis: la afirmación de que toda sucesión de Cauchy converge pertenece a la estructura de completitud que hemos construido, mientras que la extracción de un límite computable a partir de datos computables exige examinar cómo se presenta esa sucesión y qué control de convergencia se conoce. Hablar simplemente de *completitud efectiva* sin fijar las representaciones y los datos de entrada sería trasladar la ambigüedad de una palabra a otra.

## 4. Una totalidad mayor que nuestros programas

Podemos contemplar la distancia entre existencia clásica y computabilidad desde otro ángulo. Todo programa es un texto finito escrito sobre un alfabeto finito. En consecuencia, el conjunto de programas posibles es numerable. Si cada programa que calcula un real determina, a lo sumo, un número real, la colección de los reales computables también es numerable. Los números reales clásicos, en cambio, no lo son: el argumento diagonal de Cantor permite demostrar que no pueden ponerse en correspondencia biunívoca con los naturales.

La conclusión, dentro de la matemática clásica, es inmediata: existen reales que no son computables. Obsérvese el sentido de esta frase. No afirma que alguien haya fabricado una máquina imposible, ni que nuestra notación decimal esconda una contradicción. Afirma que una colección definida con criterios conjuntistas contiene más elementos que los que pueden ser producidos por programas finitos. Precisamente aquí se separan los horizontes de dos concepciones de existencia.

Wildberger considera problemático admitir esa totalidad como si todos sus integrantes estuvieran matemáticamente disponibles. El matemático clásico puede responder que *estar definido por una teoría* y *ser individualmente calculable* son condiciones distintas. Sin embargo, esa respuesta no debería borrar la cuestión práctica: cuando un teorema trabaja con un real particular, vale la pena preguntar si ese real puede representarse, aproximarse o reconocerse de manera efectiva, y cuál de esas tareas exige realmente el problema que tenemos delante.

## 5. La función: objeto extensional y regla de cálculo

La controversia alcanza también un concepto anterior al de número real: el de función. En teoría de conjuntos, podemos representar una función $f:A\to B$ como una relación $f\subseteq A\times B$ para la cual se verifica

$$
\forall x\in A\;\exists!y\in B
\quad (x,y)\in f.
$$

En este sentido, ZF y ZFC formalizan perfectamente las funciones. Los pares ordenados y las relaciones pueden codificarse mediante conjuntos; afirmar que la teoría de conjuntos es incapaz de definir una función sería, por tanto, un error.

Pero nuestro uso cotidiano de la palabra *función* reúne dos perspectivas que no siempre coinciden. Consideremos

$$
f:\mathbb N\longrightarrow\mathbb N,
\qquad f(n)=n^2+1.
$$

Podemos identificar $f$ con el conjunto de pares

$$
\{(0,1),(1,2),(2,5),(3,10),\ldots\},
$$

o describirla mediante la instrucción «elevar el argumento al cuadrado y sumar uno». La primera presentación atiende a los valores de la función; la segunda exhibe un procedimiento para obtenerlos. En un enfoque extensional, dos funciones con el mismo dominio y los mismos valores son una sola función. En una perspectiva computacional puede interesarnos distinguir, además, entre diferentes algoritmos que realizan esa misma correspondencia, o averiguar si existe alguno.

Ninguna de estas observaciones invalida la formalización conjuntista. Nos impide, simplemente, confundir un objeto extensional con una regla efectiva. Una función puede estar determinada como conjunto de pares sin que dispongamos de un algoritmo que transforme una representación de $x$ en una de $f(x)$. Y una fórmula que describe cierta correspondencia tampoco garantiza, por el solo hecho de ser breve, que exista un procedimiento de cálculo para sus valores.

Conviene llevar esta distinción todavía más lejos: la existencia de un algoritmo depende también de *cómo* se representan las entradas y las salidas. Preguntar «¿es computable esta función?» sin precisar esos datos puede ser tan insuficiente como preguntar «¿cuánto mide este objeto?» sin indicar qué magnitud deseamos medir. La computabilidad no es una propiedad que debamos adjudicar descuidadamente a cualquier expresión que contenga la letra $f$.

## 6. Qué dicen los axiomas y qué dicen nuestras paráfrasis

En *Set Theory: Should You Believe?*, Wildberger dirige parte de su crítica a las explicaciones habituales de los axiomas conjuntistas y pregunta qué significan términos como *propiedad*, *función* o *familia*. El cuestionamiento merece una respuesta precisa, porque una exposición informal y un sistema formal no operan en el mismo nivel.

El lenguaje usual de primer orden para ZF contiene la relación de pertenencia $\in$ y la igualdad lógica. Los llamados esquemas axiomáticos de separación y reemplazo se formulan mediante expresiones de ese lenguaje. Así, el esquema de reemplazo puede considerar una fórmula $\varphi(x,y,\vec p)$ que, para cada $x$ perteneciente a un conjunto $A$, determine un único $y$, y asegurar que esos valores forman un conjunto. No es necesario postular la palabra *función* como un símbolo primitivo adicional para que el esquema tenga sentido formal.

Cuando explicamos informalmente el reemplazo diciendo «la imagen de un conjunto bajo una función también es un conjunto», estamos utilizando una paráfrasis. Puede ser pedagógicamente provechosa, pero no debe confundirse con la formulación completa del esquema. Una crítica que encuentre indefiniciones en la paráfrasis no habrá demostrado, sin más, que la formulación formal es incoherente. El rigor exige examinar cada afirmación en el nivel donde efectivamente se formula.

Ahora bien, ¿significa esto que la pregunta por el significado de los axiomas desaparece? De ninguna manera. La sintaxis establece qué fórmulas están bien formadas y las reglas de inferencia fijan cómo derivamos unas de otras; todavía podemos investigar sus modelos, su consistencia relativa, su fuerza y las razones filosóficas para aceptarlas como fundamentos. Pero esas investigaciones no son intercambiables. Una objeción al criterio ontológico de una teoría, una dificultad de computabilidad y una contradicción formal constituyen problemas distintos y requieren argumentos distintos.

La propia teoría de conjuntos nos permite aprender esta lección: para estudiar críticamente sus fundamentos no necesitamos describirlos como una caja negra, pero tampoco basta con impugnar el vocabulario de una explicación divulgativa. Debemos reconstruir sus afirmaciones con la misma exigencia de precisión que pediríamos a cualquier otro campo de la matemática.

## 7. El axioma de elección y las formas de la existencia

Hay un caso en que la distancia entre afirmar una existencia y exhibir una construcción se vuelve especialmente visible. Sea $(A_i)_{i\in I}$ una familia de conjuntos no vacíos. El axioma de elección asegura que existe una función $c$ definida sobre $I$ tal que

$$
\forall i\in I,
\qquad c(i)\in A_i.
$$

No exige que hayamos proporcionado una regla uniforme y efectiva que efectúe cada elección. Por ello, cuando una demostración depende de este principio, puede establecer una existencia sin producir un procedimiento de selección. Esta es una característica lógica reconocible de su argumento y no una prueba de que el axioma incurra en contradicción.

Un resultado que muestra su alcance es el teorema según el cual **todo espacio vectorial tiene una base**. Formulado para todos los espacios vectoriales, sobre todos los cuerpos, este enunciado es equivalente al axioma de elección sobre ZF. Su demostración habitual mediante el lema de Zorn nos garantiza la existencia de una base en el marco apropiado; no convierte automáticamente esa demostración en un algoritmo para calcular una base de un espacio arbitrario.

Sería un error trasladar esta observación indiscriminadamente a todos los casos. Para un espacio vectorial de dimensión finita, dado mediante información efectiva adecuada, podemos obtener una base mediante procedimientos de álgebra lineal. La afirmación universal y un caso efectivamente presentado no contienen necesariamente la misma clase de información. Tampoco debemos suponer que toda construcción de números reales usa elección: como ya señalamos, las cortaduras de Dedekind pueden organizarse en ZF sin añadir el axioma completo.

La consecuencia metodológica es concreta. Cuando un teorema utiliza elección, necesitamos saber qué principio se ha empleado y dónde. El axioma completo, la elección numerable y la elección dependiente no son nombres distintos de una única hipótesis indiferenciada; su fuerza y sus aplicaciones deben examinarse por separado. También conviene averiguar si el principio es necesario para el enunciado, o solamente para la demostración que hemos elegido. Una prueba puede necesitar más recursos que el resultado mismo.

La pregunta no es, pues, cómo desterrar la elección de la matemática, sino cómo impedir que su intervención quede confundida con una construcción explícita.

## 8. Entre el finitismo y la matemática clásica hay más de un camino

Hasta este punto podría parecer que sólo tenemos dos alternativas: aceptar todas las construcciones clásicas sin interrogar su contenido efectivo o renunciar a los objetos cuya existencia no pueda reducirse a un procedimiento finito. La historia y la práctica contemporánea de los fundamentos muestran que ese dilema es insuficiente.

En *Foundations of Constructive Analysis*, Errett Bishop desarrolla un análisis en el que las afirmaciones de existencia se entienden en términos constructivos. Otras tradiciones —el intuicionismo, distintas teorías de tipos y el análisis computable, entre ellas— estudian con herramientas y compromisos diferentes las relaciones entre prueba, existencia y cálculo. No forman una escuela única: divergen en su interpretación de las sucesiones, sus principios lógicos y las formas de elección que admiten. Lo que comparten, en distintos grados, es la importancia concedida a la información contenida en las construcciones.

La enseñanza que extraigo de estas tradiciones no consiste en prometer que cada teorema clásico podrá traducirse, intacto, a un resultado efectivo. Sabemos que esa promesa sería falsa: el ejemplo de Specker ya nos advierte que ciertas conclusiones clásicas no sobreviven cuando exigimos algoritmos para los límites. Pero el fracaso de una traslación automática es también una fuente de conocimiento. Nos obliga a determinar qué hipótesis adicionales son necesarias, qué resultados pueden reformularse y qué noción de número real estamos utilizando.

De hecho, incluso la equivalencia que en un curso clásico parece transparente entre reales de Dedekind y reales de Cauchy exige cuidado al modificar la lógica de fondo. En determinados sistemas constructivos sin elección numerable, las dos construcciones pueden diferir y los reales de Cauchy pueden no ser completos en el sentido correspondiente. La cuestión que parecía puramente filosófica desemboca, de esta manera, en enunciados matemáticos precisos acerca de modelos y principios de elección.

No hay necesidad de convertir a Wildberger en árbitro del análisis para aprovechar este tipo de preguntas. Sus objeciones pueden servir como punto de partida; las respuestas deben buscarse en demostraciones, contraejemplos y delimitaciones lógicas, allí donde cada afirmación admite un examen propio.

## 9. No ocultar los fundamentos: una propuesta para nuestra práctica matemática

¿Qué cambiaría, concretamente, en la manera de enseñar y escribir matemáticas si tomáramos en serio estas distinciones? No creo que debamos interrumpir cada demostración para discutir la naturaleza última de los objetos. Bastaría, para comenzar, con exigir a nuestras exposiciones una honestidad adicional respecto de sus propias construcciones.

Al introducir un número, una función o un espacio, podemos señalar cuál es su definición, en qué teoría trabajamos y qué garantiza su existencia. Si el objeto se presenta mediante una sucesión, conviene saber si sus términos se calculan y si contamos con un módulo efectivo de convergencia. Si aparece una igualdad entre objetos descritos algorítmicamente, debemos distinguir su significado matemático de la posibilidad de decidirla mediante un procedimiento general. Si una prueba utiliza un principio de elección, interesa identificarlo, en lugar de dejarlo oculto bajo la expresión «tomemos un elemento para cada caso».

Nada de esto obliga a que todos los artículos se conviertan en tratados de lógica. La profundidad de la discusión debe ser proporcional a su relevancia para el resultado. Una demostración elemental que construye una base de un espacio de dimensión finita no requiere un excursus sobre el axioma de elección; un teorema acerca de las bases de espacios arbitrarios, en cambio, gana precisión cuando identifica su dependencia. Un algoritmo de aproximación racional necesita declarar la precisión que garantiza; una afirmación puramente estructural no debe simular que entrega ese algoritmo si no lo hace.

Propongo, por tanto, una regla editorial para *Matemática Abierta*: **mantener visible la distancia —cuando exista— entre lo que un teorema asegura y lo que su demostración permite efectuar**. Es una regla que alcanza tanto a la matemática clásica como a los enfoques constructivos. No debe utilizarse para insinuar que un resultado no computacional carece de rigor, ni para atribuir a una construcción efectiva propiedades que todavía no hemos demostrado. Su función es más modesta y, por ello mismo, más exigente: impedir que una palabra conveniente haga desaparecer una diferencia matemática real.

En ocasiones, el resultado de esta práctica será una segunda prueba, ahora constructiva. En otras, un algoritmo acompañado de su cota de error. Tal vez encontremos un contraejemplo que demuestre que no existe la generalización efectiva que esperábamos. O quizá descubramos que la prueba conocida usa una hipótesis más fuerte de lo necesario. Todos estos desenlaces aumentan nuestro conocimiento: ninguno requiere desacreditar de antemano la teoría de la que partimos.

## Conclusión. ¿Qué hemos construido?

Regresemos a la pregunta inicial. ¿Hemos construido realmente los números reales? Si por construcción entendemos una definición rigurosa acompañada de la demostración de sus propiedades dentro de un marco clásico, la respuesta es afirmativa. Las cortaduras de Dedekind proporcionan esa construcción y no necesitan, por sí solas, el axioma de elección completo. Si por construcción entendemos disponer de una representación efectiva de cada real arbitrario, la respuesta cambia: la totalidad clásica contiene números no computables, y la propia noción de representación exige distinguir datos y procedimientos.

No hay contradicción entre ambas respuestas una vez que advertimos que contestan preguntas diferentes. La confusión aparece cuando atribuimos a la primera todo el contenido de la segunda, o cuando tomamos la ausencia de un algoritmo como prueba de una inconsistencia que nadie ha establecido. El rigor matemático no consiste en exigir que todas las escuelas admitan idénticos objetos, sino en formular con exactitud las hipótesis, los métodos y las conclusiones de cada argumento.

Las críticas de Wildberger resultan útiles en la medida en que nos obligan a hacer esas distinciones. No es indispensable aceptar su concepción finitista, ni tampoco basta invocar la autoridad de una tradición para declarar resuelto el problema. Hay que volver a las definiciones, examinar las demostraciones y determinar qué información obtenemos al afirmar que un objeto existe.

En el fondo, esta controversia nos devuelve a una cuestión más amplia que atraviesa toda la actividad matemática. Cuando introducimos una noción y comenzamos a operar con ella, no sólo ampliamos nuestro repertorio de objetos; también adoptamos criterios acerca de qué cuenta como descripción, qué cuenta como prueba y qué cuenta como construcción. Hacer explícitos esos criterios no empobrece la disciplina. Nos permite comprender, con mayor precisión, qué hemos logrado y qué permanece todavía por investigar.

---

## Referencias y lecturas

- Bishop, Errett. *Foundations of Constructive Analysis*. McGraw-Hill, 1967.
- Bridges, Douglas; Richman, Fred. *Varieties of Constructive Mathematics*. Cambridge University Press, 1987.
- Lubarsky, Robert. «On the Cauchy Completeness of the Constructive Cauchy Reals». *Mathematical Logic Quarterly* 53, n.os 4–5 (2007): 396–414. DOI: [10.1002/malq.200710007](https://doi.org/10.1002/malq.200710007).
- Powell, Thomas. «A note on the finitization of Abelian and Tauberian theorems». *Mathematical Logic Quarterly* (2020), sección 3, dedicada a las sucesiones de Specker. [DOI: 10.1002/malq.201900076](https://doi.org/10.1002/malq.201900076).
- *Stanford Encyclopedia of Philosophy*. [«Constructive Mathematics»](https://plato.stanford.edu/entries/mathematics-constructive/), revisión de 2022.
- *Stanford Encyclopedia of Philosophy*. [«The Axiom of Choice»](https://plato.stanford.edu/entries/axiom-choice/), revisión de 2021.
- Wildberger, Norman J. [«Real numbers: A critique and way forward»](https://www.researchgate.net/publication/280387376_Real_numbers_A_critique_and_way_forward). Versión difundida en ResearchGate, julio de 2015. DOI: 10.13140/RG.2.1.3673.8406.
- Wildberger, Norman J. [«Set Theory: Should You Believe?»](https://web.maths.unsw.edu.au/~norman/papers/SetTheory.pdf). Texto documentado en circulación en 2006; versión difundida en ResearchGate en julio de 2015, DOI: 10.13140/RG.2.1.1314.5445.
