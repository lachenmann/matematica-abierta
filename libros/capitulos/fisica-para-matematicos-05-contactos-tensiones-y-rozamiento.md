---
title: "Contactos, tensiones y rozamiento"
subtitle: "Física para matemáticos · Tomo I · Capítulo 5"
author: "A. Peña"
description: "Capítulo 5 de la edición revisada, con problemas y soluciones desarrolladas."
content-id: MA-BCH-0350
source-id: FISPM-r20261021-C05
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
edition: r20261021
canonical-edition: true
date-modified: 2026-10-21
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
---

[← 4. Fuerzas y leyes de Newton](fisica-para-matematicos-04-fuerzas-y-leyes-de-newton.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [6. Cuerpos conectados y restricciones →](fisica-para-matematicos-06-cuerpos-conectados-y-restricciones.md)

Una caja de cuatro kilogramos descansa sobre una mesa horizontal. Tiramos de ella con una cuerda horizontal que ejerce dieciséis newtons, pero la caja no se mueve. Aumentamos la fuerza hasta veinticuatro newtons y comienza a deslizar. Queremos saber cuánto avanzará si mantenemos ese tirón durante dos segundos y después soltamos la cuerda. La ecuación de Newton sigue siendo la misma; lo que necesitamos determinar es cómo responde el contacto con la mesa en cada parte de la historia.

Representaremos la caja por una partícula y despreciaremos su posible vuelco. La mesa permanece fija respecto del laboratorio, que tratamos como inercial, y la cuerda tira sin levantar la caja. Usaremos $g=10\,\mathrm{m/s^2}$. Un ensayo previo del par de superficies proporciona, dentro del modelo que vamos a utilizar, un coeficiente de rozamiento estático $\mu_s=0{,}50$ y uno cinético $\mu_k=0{,}30$. Son parámetros didácticos que aquí tratamos como exactos, no constantes universales de una clase de material.

## La fuerza que permite seguir en reposo

Elegimos la caja como sistema, $x$ horizontal en el sentido del tirón e $y$ hacia arriba. La mesa ejerce una fuerza de contacto con una componente normal $N$ y otra tangencial $f$, a la que llamaremos rozamiento o fricción. Son componentes de una misma interacción entre caja y mesa; las dibujamos por separado porque las ecuaciones distinguen sus direcciones. Sobre la caja actúan además el peso y el tirón $F$ de la cuerda.

Mientras la caja mantiene su altura, la ecuación vertical es $N-mg=0$, de donde $N=40\,\mathrm N$. En la dirección horizontal,

$$
F+f=m\ddot x.
$$

La observación de reposo exige $\ddot x=0$, por lo que con el primer tirón se necesita $f=-16\,\mathrm N$. El signo expresa que la mesa ejerce esa componente hacia la izquierda. Para saber si puede hacerlo tenemos que añadir una ley del contacto: en el régimen sin deslizamiento, el modelo admite cualquier fuerza tangencial cuyo módulo no exceda $\mu_sN$. El límite es aquí veinte newtons, así que los dieciséis requeridos son admisibles.

La igualdad $|f|=\mu_sN$ daría veinte newtons de fricción y una fuerza neta de cuatro hacia la izquierda, pese a que la caja permanece en reposo. Ese resultado diagnostica la elección equivocada de la ley: hemos utilizado el máximo disponible como si fuera el valor que el contacto debe ejercer siempre. La ecuación del movimiento determina cuánto rozamiento se necesita; el límite decide si esa demanda puede satisfacerse.

![Dos diagramas de la misma caja distinguen el tirón de dieciséis newtons en reposo y el de veinticuatro durante el deslizamiento.](/assets/books/fispm/r20261021/contacto_caja_regimenes.svg){.fpm-v04-figure}

*Figura 5.1.* En reposo, el rozamiento requerido es de dieciséis newtons, inferior a su límite de veinte. Al deslizar hacia la derecha se utiliza otro parámetro y su módulo es de doce newtons. El peso y la normal se equilibran en ambos diagramas; las escalas de las flechas de cada panel son comunes.

## Seguir la caja hasta que vuelva a detenerse

Con $F=24\,\mathrm N$, mantener el reposo exigiría $f=-24\,\mathrm N$, fuera del intervalo admisible. La caja empieza a deslizar hacia la derecha. En ese régimen el modelo aproxima el módulo de la fricción por $\mu_kN=12\,\mathrm N$, opuesta al deslizamiento respecto de la mesa. La aceleración pasa a ser

$$
a_x=\frac{24\,\mathrm N-12\,\mathrm N}{4\,\mathrm{kg}}
=3\,\mathrm{m/s^2}.
$$

Fijemos $t=0$ en el comienzo de este tirón, con $x(0)=0$ y $v(0)=0$. Durante los dos primeros segundos,

$$
v(t)=(3\,\mathrm{m/s^2})t,
\qquad x(t)=\frac12(3\,\mathrm{m/s^2})t^2.
$$

Al soltar la cuerda, la caja está en seis metros y lleva seis metros por segundo. La tensión desaparece, pero no desaparece el contacto con la mesa: mientras continúe deslizando a la derecha queda una fuerza horizontal de doce newtons hacia la izquierda. Para $\tau=t-2\,\mathrm s$,

$$
v=6\,\mathrm{m/s}-(3\,\mathrm{m/s^2})\tau,
\qquad
x=6\,\mathrm m+(6\,\mathrm{m/s})\tau
-\frac12(3\,\mathrm{m/s^2})\tau^2.
$$

La primera velocidad nula de este segundo tramo ocurre en $\tau=2\,\mathrm s$, a los cuatro segundos del reloj original, en $x=12\,\mathrm m$. En ese instante hay que revisar el régimen. Ya no existe tirón ni otra fuerza tangencial: el reposo sólo requiere $f=0$, que el modelo estático permite. La caja queda detenida.

Mantener después $f=-12\,\mathrm N$ produciría una velocidad negativa, pero esa prolongación asignaría a la fricción el mismo sentido que el nuevo deslizamiento. El signo de la ley cinética había sido elegido para velocidades positivas. El cero de la velocidad obliga a volver al problema físico; no autoriza a seguir usando la misma recta indefinidamente.

![La fuerza aplicada se retira a los dos segundos; la fricción permanece hasta los cuatro, cuando la caja se detiene. La velocidad y la posición enlazan de forma continua.](/assets/books/fispm/r20261021/contacto_historia_caja.svg){.fpm-v04-figure}

*Figura 5.2.* Los cambios de ley están alineados en el mismo reloj. La posición llega a doce metros y permanece allí. En los instantes de cambio representamos límites laterales; el modelo no describe la transición microscópica del contacto.

## Qué contiene el modelo de rozamiento

La mesa y la caja pueden moverse ambas respecto del laboratorio. Para identificar el régimen importa su movimiento relativo en el contacto. En una dirección tangencial elegida, escribiremos $u=v_{\text{caja}}-v_{\text{superficie}}$. La velocidad de la superficie se evalúa en la región de contacto; no tiene que ser la de un origen distante de un cuerpo que gira.

**Definición.** Hay *adherencia* en el contacto cuando la velocidad tangencial relativa de las superficies es nula, $u=0$. Hay *deslizamiento* cuando esa velocidad tiene módulo positivo, $|u|>0$.

Ambos términos describen el movimiento tangencial relativo. La fuerza normal se determina mediante el modelo de compresión entre las superficies; la adherencia puede mantenerse mientras ese contacto transmite una fuerza tangencial dentro de su límite estático.

Para un contacto seco, sin adhesión normal, utilizaremos la siguiente ley idealizada de Coulomb, con coeficientes adimensionales $0\leq\mu_k\leq\mu_s$:

$$
\begin{cases}
|f|\leq\mu_sN,&u=0,\\
f=-\mu_kN,&u>0,\\
f=+\mu_kN,&u<0.
\end{cases}
$$

En una superficie con dos direcciones tangenciales, la condición estática pasa a ser $\|\mathbf f\|\leq\mu_sN$, y durante el deslizamiento $\mathbf f$ apunta en sentido opuesto a la velocidad relativa tangencial. Los coeficientes pertenecen al par de superficies y al régimen de calibración. Humedad, temperatura, desgaste o rapidez pueden hacer insuficiente la aproximación de coeficientes constantes.

La primera línea es una desigualdad que debe combinarse con las ecuaciones de movimiento. Por sí sola no selecciona una historia completa cuando $u=0$. En los problemas de este capítulo supondremos que, si la adherencia es compatible con los datos y las ecuaciones, se mantiene sin una perturbación que inicie el deslizamiento; cuando deja de ser admisible, examinaremos el régimen deslizante. No deducimos de esta convención un teorema general de existencia o unicidad para todo sistema con fricción.

En el valor límite $|f|=\mu_sN$, la adherencia todavía es admisible. Alcanzarlo no demuestra que el cuerpo deba empezar a moverse exactamente entonces. Describe una frontera que una demanda mayor ya no puede satisfacer. Con $\mu_k<\mu_s$, un cuerpo que ya desliza puede tener un rozamiento menor que el requerido para sostener en reposo otra historia bajo la misma fuerza aplicada. El ejercicio 19 compara esas dos preparaciones.

## Separar la normal de la condición de contacto

El capítulo anterior encontró normales negativas al imponer contactos que no podían mantenerse. Podemos expresar con más precisión la restricción que estaba detrás de ese diagnóstico.

**Definición.** En un contacto unilateral sin adhesión, llamaremos $d\geq0$ a la separación normal entre las superficies y $N\geq0$ al módulo de la fuerza normal de compresión. El modelo exige

$$
d\geq0,\qquad N\geq0,\qquad Nd=0.
$$

Una separación positiva implica fuerza normal nula. Cuando las superficies están juntas, puede haber compresión o una normal nula en el límite. Estas condiciones describen admisibilidad geométrica y de fuerza; para decidir si se separan también importan sus velocidades, aceleraciones y fuerzas restantes. No resuelven un choque ni una deformación del apoyo.

Si tiramos de la caja oblicuamente hacia arriba, una parte de la fuerza reduce la normal. Para una fuerza de módulo $F$ que forma un ángulo $\alpha$ con la horizontal, mientras se conserve el contacto con una mesa fija,

$$
N=mg-F\sin\alpha,
\qquad F_x=F\cos\alpha.
$$

Con $m=4\,\mathrm{kg}$, $F=20\,\mathrm N$, $\sin\alpha=3/5$ y $\cos\alpha=4/5$, obtenemos $N=28\,\mathrm N$. Mantener el reposo exige dieciséis newtons tangenciales, mientras que $\mu_sN=14\,\mathrm N$: no basta. Una vez que desliza hacia la derecha, la fricción es $8{,}4\,\mathrm N$ y la aceleración horizontal, $(16-8{,}4)/4=1{,}9\,\mathrm{m/s^2}$.

Usar $N=mg$ habría dado un límite estático de veinte newtons y una conclusión equivocada de reposo. La dirección del tirón modifica simultáneamente la demanda tangencial y la capacidad del contacto. Si una cuenta diera $N<0$, antes de usarla en $\mu N$ habría que abandonar la hipótesis de apoyo mantenido.

![El tirón oblicuo tiene componentes dieciséis y doce newtons. La normal resultante es veintiocho newtons y la fricción cinética, ocho coma cuatro.](/assets/books/fispm/r20261021/contacto_tiron_oblicuo.svg){.fpm-v04-figure}

*Figura 5.3.* El diagrama contiene la fuerza oblicua completa. Sus proyecciones se muestran en otro panel para evitar contarlas como dos fuerzas adicionales. La normal se obtiene de la ecuación vertical.

## La pendiente decide qué fricción se necesita

Coloquemos un bloque de tres kilogramos sobre un plano fijo con $\sin\alpha=3/5$ y $\cos\alpha=4/5$. Elegimos el eje tangencial hacia arriba y el normal hacia afuera. Mientras se mantenga el apoyo, $N=mg\cos\alpha=24\,\mathrm N$. La componente del peso hacia abajo del plano es de dieciocho newtons. Para permanecer en reposo necesita una fuerza de fricción de dieciocho newtons hacia arriba.

Con $\mu_s=0{,}80$, el límite estático es $19{,}2\,\mathrm N$ y esa situación es admisible. Si otro par de superficies tuviera $\mu_s=0{,}50$ y $\mu_k=0{,}40$, el límite sería doce newtons: el bloque comenzaría a bajar. Durante ese descenso, la fricción sería $9{,}6\,\mathrm N$ hacia arriba y la aceleración tendría módulo $(18-9{,}6)/3=2{,}8\,\mathrm{m/s^2}$ hacia abajo.

El signo de la fricción se decide comprobando la tendencia al deslizamiento o el deslizamiento que ya existe. Si el bloque llegara moviéndose hacia arriba, la fricción cinética apuntaría hacia abajo junto con la componente del peso. La condición de reposo debe revisarse después de la primera detención; no se puede tomar sin examen la solución de bajada para describir la subida.

![El peso vertical se proyecta sobre ejes paralelo y normal al plano; la fricción estática necesaria apunta hacia arriba y vale dieciocho newtons.](/assets/books/fispm/r20261021/contacto_plano_inclinado.svg){.fpm-v04-figure}

*Figura 5.4.* En este ejemplo la normal es de veinticuatro newtons y el peso, de treinta. La fricción requerida se compara con su límite; sus componentes no se añaden como otras fuerzas al diagrama.

**Proposición.** Sea un bloque de masa $m>0$ sobre un plano fijo de inclinación $0\leq\alpha<\pi/2$. Supongamos un modelo de partícula, contacto mantenido, peso, una fuerza aplicada de componente $F$ paralela al plano hacia arriba —sin componente normal— y rozamiento estático de coeficiente $\mu_s\geq0$. El reposo es admisible exactamente cuando

$$
mg(\sin\alpha-\mu_s\cos\alpha)
\leq F\leq
mg(\sin\alpha+\mu_s\cos\alpha).
$$

*Demostración.* La ecuación normal fija $N=mg\cos\alpha>0$. En la dirección tangencial, el reposo exige $F+f-mg\sin\alpha=0$, por lo que sólo hay un valor posible de la fuerza estática: $f=mg\sin\alpha-F$. Ese valor pertenece al intervalo $[-\mu_sN,\mu_sN]$ exactamente cuando se cumplen las dos desigualdades enunciadas. Si se cumplen, las fuerzas así asignadas satisfacen ambas ecuaciones y el límite del contacto; si alguna falla, ninguna otra elección de $f$ puede producir reposo. $\square$

La fuerza $F$ de este enunciado es una componente con signo, no un módulo que deba ser positivo. Si procede de una cuerda que sólo tira hacia arriba, hay que intersectar el intervalo obtenido con $F\geq0$. Sin fuerza aplicada, el criterio se reduce a $\tan\alpha\leq\mu_s$. Aumentar lentamente el ángulo hasta el umbral permite estimar $\mu_s$, siempre que el ensayo corresponda al régimen del modelo. Una medición del ángulo crítico no justifica usar el mismo coeficiente en deslizamiento.

## Lo que una cuerda puede transmitir

Una cuerda flexible tira de los cuerpos unidos a sus extremos a lo largo de su dirección local. Una cuerda floja no sostiene una fuerza de compresión que empuje sus extremos separándolos. Llamaremos $T\geq0$ a su tensión; si la hipótesis de cuerda tensa exige $T<0$, habrá que cambiar de régimen. Un tirante rígido capaz de empujar sería otro elemento mecánico.

**Definición.** En este capítulo, una *cuerda ideal* tiene masa despreciable, longitud constante cuando está tensa y resistencia nula a la flexión. Una *polea fija ideal* sólo redirige la cuerda: despreciamos su inercia y el rozamiento que pudiera exigir tensiones distintas a ambos lados. Estas hipótesis permiten utilizar un mismo módulo $T$ en los tramos de una misma cuerda que pasa por esa polea.

La igualdad de tensiones y la relación entre movimientos proceden de hipótesis diferentes. La masa despreciable y la guía ideal permiten igualar los módulos transmitidos; la longitud constante relaciona desplazamientos. Una cuerda con masa puede necesitar tensiones diferentes para sostener y acelerar sus partes. Una guía rugosa puede ejercer fuerzas tangenciales sobre la cuerda. En cualquiera de esos casos no bastaría afirmar que se trata de «la misma cuerda» para igualar las tensiones.

La tensión tampoco se iguala automáticamente al peso de la masa que cuelga. Si esa masa acelera hacia abajo, su ecuación es $Mg-T=Ma_y$; con $a_y>0$, la tensión es menor que $Mg$. El peso y la tensión recibidos por la masa no forman una pareja de tercera ley. La pareja de la tensión sobre la masa es la fuerza que esa masa ejerce sobre la cuerda.

## Unir dos ecuaciones sin perder sus direcciones

Un bloque de masa $m=3\,\mathrm{kg}$ descansa sobre una mesa y está unido, por una cuerda ideal sobre una polea fija ideal en su borde, a una masa colgante $M=2\,\mathrm{kg}$. El tramo de cuerda sobre la mesa es horizontal. Para ese contacto tomamos $\mu_s=0{,}40$ y $\mu_k=0{,}20$. La guía es suficientemente larga y la masa colgante no toca el suelo durante el intervalo que analizamos.

Antes de suponer movimiento, probamos el reposo. La masa colgante necesitaría $T=Mg=20\,\mathrm N$. El bloque sobre la mesa necesitaría una fricción opuesta de veinte newtons, pero su normal es treinta y el límite estático, doce. El reposo es imposible dentro de esas hipótesis. La masa colgante comenzará a bajar y el bloque se moverá hacia la polea.

Elegimos $x$ positivo hacia la polea para el bloque e $y$ positivo hacia abajo para la masa. Si el tramo horizontal tiene longitud $b-x$ y el vertical longitud $y$, la longitud total satisface

$$
b-x+y+c=L,
$$

donde $b,c,L$ son constantes que incorporan la geometría fija. Por tanto, $\dot y=\dot x$ y $\ddot y=\ddot x=a$. Las componentes coinciden con estos ejes; los vectores de aceleración siguen apuntando en direcciones distintas.

El rozamiento cinético del bloque es de seis newtons. Escribimos una ecuación para cada receptor:

$$
T-\mu_kmg=ma,
\qquad Mg-T=Ma.
$$

Al sumarlas se elimina la incógnita $T$. Estamos sumando ecuaciones escalares proyectadas sobre ejes diferentes; las fuerzas de tensión sobre esos dos cuerpos no son vectores opuestos en el laboratorio. La polea y su soporte cambian la dirección de la interacción transmitida. El cálculo da

$$
a=\frac{Mg-\mu_kmg}{m+M}
=\frac{14}{5}\,\mathrm{m/s^2},
\qquad T=ma+\mu_kmg=\frac{72}{5}\,\mathrm N.
$$

La tensión es positiva y menor que los veinte newtons del peso colgante. La aceleración positiva confirma el sentido de deslizamiento supuesto. El sistema se puede seguir con esa ley hasta que cambie una condición: la masa llegue al suelo, el bloque alcance la polea, se retire un agente o aparezca holgura. La relación de longitud seguirá siendo necesaria en otras geometrías, pero ya no se puede anticipar que todas las aceleraciones tendrán el mismo módulo.

![Una polea fija conecta un bloque horizontal con una masa colgante. Los diagramas individuales usan ejes distintos y conservan el mismo módulo de tensión.](/assets/books/fispm/r20261021/contacto_polea_fija.svg){.fpm-v04-figure}

*Figura 5.5.* La cuerda tensa impone una relación entre sus tramos. Las ecuaciones usan el mismo valor de $a$ después de derivar esa relación; no porque ambos cuerpos reciban las mismas fuerzas. Las longitudes de las flechas de fuerza son esquemáticas.

## Fricción que acelera en el sentido de la marcha

Una caja se transporta sobre la plataforma horizontal de un vehículo que acelera hacia la derecha. Si la caja acompaña al vehículo sin deslizar, también debe acelerar hacia la derecha. Cuando la única fuerza horizontal sobre ella es el contacto con la plataforma, la segunda ley exige $f=ma$ hacia la derecha. La fricción estática puede apuntar en el mismo sentido que la velocidad de la caja respecto del suelo.

Con una plataforma que se traslada horizontalmente, sin otras fuerzas verticales sobre la caja, $N=mg$. La adherencia exige

$$
|ma|\leq\mu_smg,
\qquad |a|\leq\mu_sg.
$$

**Proposición.** Sea una caja de masa $m>0$, inicialmente en reposo relativo sobre una plataforma horizontal que realiza una traslación horizontal de clase $C^2$ respecto de un marco inercial. Supongamos contacto mantenido, peso y contacto como únicas fuerzas sobre la caja, con coeficiente estático $\mu_s$. La historia que conserva la posición de la caja respecto de la plataforma es admisible en un intervalo exactamente cuando $|a_{\mathrm{plataforma}}(t)|\leq\mu_sg$ para todos sus instantes.

*Demostración.* Conservar la posición relativa implica igualdad de velocidades y aceleraciones horizontales. La ecuación de la caja determina $f(t)=ma_{\mathrm{plataforma}}(t)$ y la vertical fija $N=mg$. Aplicar el límite estático da la condición necesaria. Recíprocamente, si esa condición vale en todo el intervalo, asignar esa fuerza de contacto a la historia de traslación compartida satisface Newton y la ley estática, con las condiciones iniciales relativas dadas. Se ha demostrado admisibilidad de esa historia, sin formular un resultado general de unicidad para otras leyes de contacto. $\square$

Si se supera la cota, la caja puede deslizar hacia atrás respecto del vehículo mientras todavía avanza respecto del suelo. Una cinta transportadora ofrece otro ejemplo: una caja inicialmente quieta respecto del laboratorio es acelerada por la fricción de una cinta que pasa bajo ella. El sentido se decide comparando velocidades de las dos superficies, no mirando sólo la flecha de velocidad de la caja.

![Una caja que se mueve hacia la derecha más lentamente que la cinta desliza hacia la izquierda respecto de ella y recibe fricción hacia la derecha.](/assets/books/fispm/r20261021/contacto_velocidad_relativa.svg){.fpm-v04-figure}

*Figura 5.6.* Las velocidades están expresadas respecto del laboratorio y utilizan su propia escala. La fuerza pertenece al diagrama de la caja. La comparación de velocidades determina el signo del deslizamiento relativo.

## Una desigualdad también puede resolver un problema

En una cuenta de equilibrio, la fricción desconocida se obtiene de una igualdad y luego se comprueba mediante una desigualdad. Esa comprobación puede producir un intervalo completo de fuerzas aplicadas, en lugar de un único número. El criterio de reposo demostrado para el plano inclinado identifica precisamente ese intervalo. Sus extremos indican fricción estática límite en sentidos contrarios; en su interior puede cambiar incluso el signo de la fuerza requerida.

![Un intervalo de fuerzas paralelas permite el reposo en una pendiente. La fricción requerida cambia de sentido al pasar por la componente tangencial del peso.](/assets/books/fispm/r20261021/contacto_intervalo_estatico.svg){.fpm-v04-figure}

*Figura 5.7.* Para $m=3\,\mathrm{kg}$, $\sin\alpha=3/5$, $\cos\alpha=4/5$ y $\mu_s=0{,}50$, el reposo admite $6\leq F/(1\,\mathrm N)\leq30$. En $F=18\,\mathrm N$ no se necesita fricción; en los extremos se requieren doce newtons en sentidos opuestos. Si el agente es una cuerda, también hay que respetar que sólo puede tirar.

Esta forma de resolver conserva la pregunta física: qué debe proporcionar un contacto y qué valores permite su modelo. La masa no necesita empezar a deslizar para que aprendamos algo sobre ella. Un reposo observado sólo impone una cota inferior a la fricción máxima disponible; una historia deslizante permite investigar otro parámetro. Para distinguirlos harán falta ensayos preparados en regímenes distintos y mediciones cuyas incertidumbres no se confundan con un cambio real de contacto.

## Ejercicios

Utiliza $g=10\,\mathrm{m/s^2}$ y el modelo de Coulomb del capítulo. Los coeficientes y demás datos son exactos dentro de cada problema, salvo indicación contraria. Los cuerpos se modelan como partículas o como bloques en traslación sin vuelco; se desprecian aire y deformaciones. Las cuerdas y poleas son ideales cuando se indica, y los apoyos no ejercen tracción normal. Los cambios instantáneos de fuerzas se interpretan mediante límites laterales. En las expresiones temporales, $\theta=t/(1\,\mathrm s)$.

Los problemas 1–7 permiten consolidar el cambio entre reposo y deslizamiento con una sola masa. El 8 y el 9 introducen tensiones antes de combinarlas con rozamiento en el 10. Los restantes requieren elegir el movimiento relativo, comparar restricciones o utilizar datos acotados. Antes de mirar las soluciones de 3, 10 y 13, conviene dejar escrito qué régimen se está suponiendo y qué resultado obligaría a rechazarlo.

### 1. Una fricción que todavía no llegó al límite {#ejercicio-5-1}

Un bloque de tres kilogramos está inicialmente en reposo sobre una mesa horizontal. Se aplica una fuerza horizontal de ocho newtons hacia la derecha. Los coeficientes son $\mu_s=0{,}40$ y $\mu_k=0{,}25$. Determina la normal, la fricción y la aceleración. Un estudiante calcula primero $f=\mu_smg$ y obtiene aceleración hacia la izquierda. Explica qué condición dejó de comprobar.

### 2. Retirar el tirón {#ejercicio-5-2}

Un bloque de dos kilogramos parte del reposo en $x=0$ sobre una mesa horizontal, con $\mu_s=0{,}40$ y $\mu_k=0{,}30$. Desde $t=0$ recibe una fuerza horizontal de diez newtons hacia la derecha durante un segundo; después se retira. Obtén velocidad y posición hasta la detención definitiva, su tiempo y la distancia total. Justifica el régimen posterior al primer cero de la velocidad.

### 3. Frenar mientras la fuerza apunta hacia la derecha {#ejercicio-5-3}

Un bloque de dos kilogramos desliza inicialmente hacia la izquierda a tres metros por segundo sobre una mesa fija. Actúa una fuerza horizontal constante de dos newtons hacia la derecha. Se conocen $\mu_s=0{,}30$ y $\mu_k=0{,}20$. Determina la fricción inicial, el instante y la posición de la primera detención, tomando $x(0)=0$, y decide qué ocurre después. Explica por qué el rozamiento inicial no apunta hacia la izquierda.

### 4. Tirar y empujar en ángulo {#ejercicio-5-4}

Un bloque de cinco kilogramos está en reposo sobre una mesa, con $\mu_s=0{,}50$ y $\mu_k=0{,}40$. Se aplica una fuerza de veinticinco newtons con componente horizontal hacia la derecha y formando un ángulo cuyo seno es $3/5$ y coseno $4/5$. Estudia primero un tirón hacia arriba y después un empuje hacia abajo con el mismo módulo y ángulo. Calcula en cada ensayo la normal, el régimen inicial y la fricción; si empieza a deslizar, calcula la aceleración.

### 5. Reposo en una pendiente {#ejercicio-5-5}

Un bloque de dos kilogramos está inicialmente en reposo sobre un plano de $30^\circ$, con $\mu_s=0{,}70$. No hay cuerda ni otra fuerza aplicada. Calcula la normal y la fricción necesaria, comprueba si se mantiene el reposo y decide si observarlo basta para identificar exactamente $\mu_s$.

### 6. Subir, detenerse y decidir si vuelve {#ejercicio-5-6}

Un bloque se lanza hacia arriba de un plano largo con rapidez inicial de cinco metros por segundo. La inclinación tiene seno $3/5$ y coseno $4/5$; los coeficientes son $\mu_k=0{,}25$ y $\mu_s=0{,}80$. No actúa otra fuerza que peso y contacto. Determina la aceleración durante la subida, el tiempo y la distancia hasta detenerse. Decide si inicia un descenso después.

### 7. Sostener un bloque contra una pared {#ejercicio-5-7}

Una fuerza horizontal presiona un bloque de dos kilogramos contra una pared vertical fija. Los coeficientes son $\mu_s=0{,}50$ y $\mu_k=0{,}30$. Encuentra el módulo mínimo del empuje que permite sostenerlo en reposo. Si se mantiene un empuje de treinta newtons y el bloque se libera desde el reposo, determina el sentido de la fricción y la aceleración inicial de deslizamiento. No hay ningún apoyo por debajo.

### 8. Una tensión horizontal {#ejercicio-5-8}

Dos bloques A y B, de dos y tres kilogramos respectivamente, están unidos por una cuerda ideal horizontal y tensa sobre una mesa lisa. A está a la izquierda de B. Se aplica sobre B una fuerza de quince newtons hacia la derecha, partiendo ambos del reposo. Halla la aceleración común y la tensión. Identifica los dos receptores de las fuerzas que ejerce la cuerda y explica por qué su tensión no es el peso de ninguno de los bloques.

### 9. Dos masas a ambos lados de una polea {#ejercicio-5-9}

Dos masas de dos y tres kilogramos cuelgan de los extremos de una misma cuerda ideal sobre una polea fija ideal. Parten del reposo y no encuentran obstáculos durante el intervalo de estudio. Calcula sus aceleraciones y la tensión. Escribe claramente los sentidos positivos y comprueba que la tensión obtenida satisface las dos ecuaciones.

### 10. Probar el reposo antes de despejar una aceleración {#ejercicio-5-10}

Un bloque de cuatro kilogramos está sobre una mesa con $\mu_s=0{,}40$ y $\mu_k=0{,}25$. Una cuerda ideal horizontal pasa por una polea fija ideal y sostiene una masa colgante. Determina tensión y fricción si esa masa es de un kilogramo y todo parte del reposo. Repite el análisis si se sustituye por una masa de tres kilogramos: decide el régimen y calcula la aceleración y la tensión antes de que algún cuerpo alcance un obstáculo.

### 11. Una caja que acompaña a un vehículo {#ejercicio-5-11}

Una caja de cinco kilogramos está inicialmente en reposo relativo sobre una plataforma horizontal que se traslada hacia la derecha. El contacto tiene $\mu_s=0{,}40$ y $\mu_k=0{,}30$. Calcula la fricción cuando la plataforma acelera a $3\,\mathrm{m/s^2}$. Examina después un ensayo que comienza con la misma velocidad de caja y plataforma y aceleración de ésta de $5\,\mathrm{m/s^2}$. Si pierde adherencia, determina la aceleración de la caja respecto del laboratorio y la aceleración horizontal relativa respecto de la plataforma. La caja permanece sobre ella durante el tramo considerado.

### 12. Alcanzar la velocidad de una cinta {#ejercicio-5-12}

Una cinta horizontal muy larga se mueve uniformemente hacia la derecha a tres metros por segundo. En $t=0$ una caja de dos kilogramos entra en contacto con ella, con velocidad horizontal nula respecto del laboratorio. El establecimiento del apoyo no aporta impulso horizontal. Los coeficientes son $\mu_k=0{,}20$ y $\mu_s=0{,}40$. Calcula cuándo deja de deslizar respecto de la cinta, la distancia que ha recorrido hasta entonces y su posición en $t=3\,\mathrm s$, tomando $x(0)=0$. Determina la fricción una vez que comparten velocidad.

### 13. Arrastrar dos bloques apilados {#ejercicio-5-13}

Un bloque superior de dos kilogramos descansa sobre otro inferior de tres, sobre una mesa horizontal lisa. Entre los dos bloques hay $\mu_s=0{,}50$ y $\mu_k=0{,}40$. Ambos parten del reposo. Se tira horizontalmente del bloque inferior hacia la derecha. Encuentra el mayor módulo de fuerza aplicada compatible con que se muevan juntos. Para una fuerza de treinta newtons, calcula las aceleraciones de ambos durante el deslizamiento relativo y comprueba su sentido. Supón que los bloques siguen solapándose y no vuelcan en el intervalo estudiado.

### 14. Una cuerda que tendría que empujar {#ejercicio-5-14}

Dos partículas A y B están sobre una guía horizontal lisa, con A a la izquierda de B y una cuerda ideal de un metro entre ellas, inicialmente recta y tensa. Sus masas son dos y un kilogramo. Parten del reposo; sólo se aplica a A una fuerza de seis newtons hacia la derecha. Prueba la hipótesis de cuerda tensa y examina el signo de la tensión. Determina las aceleraciones inmediatamente después de comenzar la fuerza si la cuerda no puede empujar, y describe cómo cambia la separación antes de que se produzca cualquier otro contacto.

### 15. Cuándo no hay una sola tensión {#ejercicio-5-15}

Una cuerda vertical uniforme de masa un kilogramo y longitud dos metros sostiene en su extremo inferior una masa de tres kilogramos. Un agente tira del extremo superior y todo acelera hacia arriba a $2\,\mathrm{m/s^2}$, sin estiramiento apreciable. Calcula las tensiones en los extremos inferior y superior de la cuerda, y en una sección situada a una distancia $z\in[0,2]\,\mathrm m$ por encima del extremo inferior. Explica qué idealización del capítulo ya no puede utilizarse.

### 16. Una decisión con datos acotados {#ejercicio-5-16}

Un bloque de cuatro kilogramos está inicialmente en reposo en una mesa horizontal. El coeficiente estático pertenece a $[0{,}35,0{,}45]$ y el tirón horizontal aplicado a $[14,18]\,\mathrm N$; todas las combinaciones son admisibles. Decide si se garantiza el reposo para toda la familia. Construye una elección compatible con reposo y otra incompatible. Explica qué se concluye en una combinación que satisface exactamente $F=\mu_smg$ y si las cotas permiten asignar una probabilidad de deslizamiento.

### 17. Medir dos coeficientes mediante dos ensayos {#ejercicio-5-17}

En un ensayo cuasiestático, el ángulo crítico de inicio del deslizamiento de un bloque está acotado por $\alpha_c\in[20^\circ,22^\circ]$. Adopta el criterio límite de Coulomb para inferir una banda de $\mu_s$. En otro ensayo, el bloque ya desliza hacia abajo por un plano fijo de $30^\circ$ y su aceleración hacia abajo pertenece a $[2{,}0,2{,}2]\,\mathrm{m/s^2}$. El ángulo y $g$ se tratan como exactos en este segundo ensayo. Obtén una banda para $\mu_k$ y explica por qué no basta el primer ensayo para medir ambos coeficientes.

### 18. Reposo relativo en una plataforma que gira {#ejercicio-5-18}

Una pieza de dos kilogramos descansa a dos metros del centro de una plataforma horizontal que gira con velocidad angular constante alrededor de un eje vertical. Inicialmente la pieza comparte su giro y no desliza. El coeficiente estático es $\mu_s=0{,}45$; no hay cuerda ni tope lateral. Calcula la fricción requerida para $\omega=1\,\mathrm{s^{-1}}$ y el mayor $|\omega|$ compatible con la trayectoria circular sin deslizamiento. Decide qué puede afirmarse para $\omega=2\,\mathrm{s^{-1}}$ sin suponer que la pieza sigue obligatoriamente en el mismo círculo.

### 19. La misma fuerza y dos preparaciones {#ejercicio-5-19}

Sobre un bloque de dos kilogramos en una mesa fija actúa una fuerza horizontal constante de seis newtons hacia la derecha. Se conocen $\mu_s=0{,}40$ y $\mu_k=0{,}20$. Compara un ensayo en que comienza en reposo con otro en que comienza deslizando hacia la derecha a un metro por segundo. Determina la fricción y el movimiento en cada uno durante dos segundos. Aplica la convención de mantener la adherencia cuando sea admisible. Explica por qué la fuerza aplicada no determina por sí sola la respuesta.

### 20. Elegir el ángulo del tirón {#ejercicio-5-20}

Se quiere iniciar el deslizamiento hacia la derecha de un bloque de masa $m>0$, inicialmente en reposo sobre una mesa, tirando mediante una cuerda que forma un ángulo $0\leq\alpha<\pi/2$ hacia arriba. El coeficiente estático es $\mu_s>0$ y se exige conservar normal positiva. Obtén el módulo crítico $F_c(\alpha)$ en que la fricción requerida alcanza su máximo y encuentra el ángulo que minimiza ese módulo. Evalúa el resultado para $m=4\,\mathrm{kg}$ y $\mu_s=0{,}50$, comprueba la normal en ese umbral y distingue alcanzar el límite de sobrepasarlo.

## Soluciones

### 1. Una fricción que todavía no llegó al límite {#solucion-5-1}

El reposo es la primera hipótesis que debemos comprobar porque el bloque parte sin deslizamiento. En vertical, la mesa impide el movimiento y no hay otra fuerza con componente vertical: $N=mg=30\,\mathrm N$. En horizontal, el reposo exige $8\,\mathrm N+f=0$, por lo que $f=-8\,\mathrm N$.

El máximo estático es $\mu_sN=12\,\mathrm N$. El valor requerido tiene módulo menor, así que es admisible y la aceleración es cero. El coeficiente cinético no interviene en esta historia. Usar siempre doce newtons hacia la izquierda produciría $(8-12)/3=-4/3\,\mathrm{m/s^2}$: esa cuenta cumple Newton para una fuerza mal asignada, pero no la condición de contacto estático ajustado a los datos. La caja no necesita que la mesa ejerza su fuerza tangencial máxima.

### 2. Retirar el tirón {#solucion-5-2}

La normal es veinte newtons y el máximo estático, ocho. Como la fuerza aplicada es diez, el reposo no puede mantenerse. Al deslizar a la derecha, la fricción es seis newtons hacia la izquierda y la aceleración, $(10-6)/2=2\,\mathrm{m/s^2}$. Durante el primer segundo,

$$
v=2\theta\,\mathrm{m/s},\qquad x=\theta^2\,\mathrm m.
$$

En el cambio de fuerza, $v=2\,\mathrm{m/s}$ y $x=1\,\mathrm m$. Después sólo queda fricción horizontal, de modo que $a=-3\,\mathrm{m/s^2}$. Con $\tau=t-1\,\mathrm s$,

$$
v=2\,\mathrm{m/s}-(3\,\mathrm{m/s^2})\tau,
\qquad x=1\,\mathrm m+(2\,\mathrm{m/s})\tau
-\frac12(3\,\mathrm{m/s^2})\tau^2.
$$

La velocidad se anula después de $2/3\,\mathrm s$. La caja avanza en este tramo $2/3\,\mathrm m$, por lo que queda en $x=5/3\,\mathrm m$ a los $5/3\,\mathrm s$ del reloj original. No cambió de sentido antes de detenerse, así que esa posición también es la distancia total desde el origen.

Al llegar a velocidad cero, el tirón ya no actúa y la fricción necesaria para conservar reposo es cero, dentro de la banda estática. Para tiempos posteriores, $v=0$ y $x=5/3\,\mathrm m$. La prolongación del segundo polinomio predeciría regreso y utilizaría una ley de fricción cuyo signo ya no correspondería al movimiento.

### 3. Frenar mientras la fuerza apunta hacia la derecha {#solucion-5-3}

El bloque desliza hacia la izquierda respecto de una mesa fija: su velocidad relativa es negativa. La fricción cinética apunta a la derecha, con módulo $\mu_kmg=4\,\mathrm N$. Junto con los dos newtons aplicados produce seis newtons hacia la derecha y $a=3\,\mathrm{m/s^2}$.

Hasta la primera detención,

$$
v=(-3+3\theta)\,\mathrm{m/s},
\qquad x=(-3\theta+\tfrac32\theta^2)\,\mathrm m.
$$

La raíz admisible es $t=1\,\mathrm s$, en $x=-1{,}5\,\mathrm m$. La aceleración positiva redujo una rapidez asociada a una velocidad negativa. Para decidir el tramo siguiente escribimos otra vez la ecuación de reposo: ahora basta una fricción de dos newtons hacia la izquierda, menor que el máximo estático de seis. El bloque queda allí detenido bajo la convención de adherencia adoptada. La fricción cambia de sentido entre el deslizamiento y el reposo; el signo del tirón no bastaba para determinar su signo inicial.

### 4. Tirar y empujar en ángulo {#solucion-5-4}

En ambos ensayos la componente horizontal aplicada es veinte newtons y el módulo de la vertical, quince. Al tirar hacia arriba, $N=50-15=35\,\mathrm N$. El reposo requeriría $f=-20\,\mathrm N$, pero el límite estático es $17{,}5\,\mathrm N$. Empieza a deslizar a la derecha, la fricción pasa a catorce newtons hacia la izquierda y

$$
a=\frac{20-14}{5}\,\mathrm{m/s^2}=1{,}2\,\mathrm{m/s^2}.
$$

Al empujar hacia abajo, la normal aumenta a $N=50+15=65\,\mathrm N$. Su límite estático es $32{,}5\,\mathrm N$, suficiente para proporcionar los veinte requeridos. La fricción es veinte hacia la izquierda y la aceleración es cero. Ambas normales son positivas; no se pierde contacto. Comparar sólo la componente horizontal habría ocultado que el empuje cambia la capacidad de la mesa para mantener adherencia.

### 5. Reposo en una pendiente {#solucion-5-5}

Los ejes paralelo y normal al plano separan la tendencia a bajar de la compresión contra la superficie. La normal es $mg\cos30^\circ=10\sqrt3\,\mathrm N$. La componente del peso hacia abajo es $mg\sin30^\circ=10\,\mathrm N$, por lo que la fricción requerida apunta hacia arriba con ese mismo módulo.

El límite vale $\mu_sN=7\sqrt3\,\mathrm N\approx12{,}124\,\mathrm N$, superior a diez. El reposo es admisible. Ese resultado no significa que la fricción real sea $7\sqrt3$; sigue siendo diez. Observar el reposo bajo estas condiciones sólo permite inferir $\mu_s\geq\tan30^\circ=1/\sqrt3$. Todos los valores superiores satisfacen la misma observación; identificar exactamente el coeficiente requeriría información adicional de umbral.

### 6. Subir, detenerse y decidir si vuelve {#solucion-5-6}

Orientamos el eje hacia arriba del plano. Durante la subida, tanto la componente del peso como la fricción apuntan hacia abajo. La normal es $mg(4/5)$ y, al dividir la ecuación tangencial por la masa,

$$
a=-g\left(\frac35+\mu_k\frac45\right)
=-8\,\mathrm{m/s^2}.
$$

La masa se cancela porque ambas contribuciones de fuerza son proporcionales a ella en este modelo. Integrar desde $v_0=5\,\mathrm{m/s}$ da el primer cero en $t_*=5/8\,\mathrm s$ y una distancia de subida

$$
s_* =\frac{v_0^2}{2(8\,\mathrm{m/s^2})}
=\frac{25}{16}\,\mathrm m.
$$

En la detención, permanecer allí requiere fricción hacia arriba de módulo $(3/5)mg$. El máximo estático es $\mu_sN=(16/25)mg$, y $3/5=15/25<16/25$. Por tanto, puede quedarse en reposo y así continúa según la convención del capítulo. La cuenta de bajada no debe iniciarse hasta haber comprobado esta condición. Una aceleración dirigida hacia abajo durante la subida no garantiza que exista después un descenso.

### 7. Sostener un bloque contra una pared {#solucion-5-7}

La normal es horizontal: la proporciona la pared y equilibra el empuje. Si su módulo es $F$, entonces $N=F$. En vertical el peso de veinte newtons debe ser equilibrado por fricción estática hacia arriba. Se exige $20\,\mathrm N\leq0{,}50F$, es decir, $F\geq40\,\mathrm N$. Cuarenta es el mínimo admisible; en ese umbral el reposo sigue siendo posible.

Con $F=30\,\mathrm N$, el límite estático es quince, insuficiente para sostener el bloque. Empieza a bajar. La fricción cinética apunta hacia arriba y vale $0{,}30(30)=9\,\mathrm N$. Quedan once newtons hacia abajo, de modo que la aceleración de deslizamiento es $11/2=5{,}5\,\mathrm{m/s^2}$ hacia abajo. No se utiliza $N=mg$: aquí normal y peso apuntan en direcciones perpendiculares.

### 8. Una tensión horizontal {#solucion-5-8}

El sistema A y B recibe quince newtons externos en horizontal; sobre la mesa lisa no hay rozamiento. La cuerda tensa y de longitud constante obliga a conservar la separación, así que ambos comparten aceleración. Al sumar sus ecuaciones,

$$
(2+3)\,\mathrm{kg}\,a=15\,\mathrm N,
\qquad a=3\,\mathrm{m/s^2}.
$$

Para recuperar la tensión escogemos A solo: su única fuerza horizontal es la que la cuerda ejerce hacia la derecha. Por tanto, $T=(2\,\mathrm{kg})a=6\,\mathrm N$. En B, la cuerda tira hacia la izquierda y la ecuación es $15-6=3(3)$ en newtons, que comprueba el resultado.

La cuerda ejerce seis newtons sobre cada bloque, con receptores y sentidos diferentes. La igualdad de módulos responde a su idealización. Ninguno de esos módulos se obtiene del equilibrio vertical: los pesos, veinte y treinta newtons, son equilibrados por las normales. Aquí la tensión es una fuerza horizontal necesaria para acelerar A.

### 9. Dos masas a ambos lados de una polea {#solucion-5-9}

La masa mayor bajará y la menor subirá si la tensión que resulte es admisible. Elegimos positivo hacia arriba para la masa de dos kilogramos y hacia abajo para la de tres. La cuerda tensa sobre una polea fija conserva la suma de las longitudes verticales: los desplazamientos tienen el mismo módulo en sentidos contrarios, y las componentes en estos dos ejes comparten un valor $a$.

Las ecuaciones son

$$
T-20\,\mathrm N=(2\,\mathrm{kg})a,
\qquad 30\,\mathrm N-T=(3\,\mathrm{kg})a.
$$

Sumarlas da $a=2\,\mathrm{m/s^2}$. La primera proporciona $T=24\,\mathrm N$; la segunda comprueba $30-24=3(2)$ en newtons. Es positiva, mayor que el peso de la masa que sube y menor que el de la que baja. Esas desigualdades permiten que ambas aceleren en los sentidos elegidos. Suponer $T=30\,\mathrm N$ habría dejado a la masa mayor sin aceleración y habría resultado incompatible con la primera ecuación y la restricción de cuerda.

### 10. Probar el reposo antes de despejar una aceleración {#solucion-5-10}

Con la masa colgante de un kilogramo, el reposo de ésta requiere $T=10\,\mathrm N$. El bloque horizontal necesita una fricción de diez newtons que se oponga al tirón. Su normal es cuarenta y su límite estático, dieciséis: esa fricción es admisible. Ambos permanecen en reposo, $f=-10\,\mathrm N$ tomando positivo hacia la polea. El coeficiente cinético no interviene.

Con la masa colgante de tres kilogramos, la prueba de reposo exigiría $T=30\,\mathrm N$ y una fricción horizontal del mismo módulo, superior a dieciséis. En el nuevo régimen el bloque desliza hacia la polea y la fricción es diez newtons. Elegimos ese sentido positivo para él y hacia abajo para la masa. La longitud de la cuerda relaciona sus aceleraciones como en el texto. Resulta

$$
T-10\,\mathrm N=(4\,\mathrm{kg})a,
\qquad 30\,\mathrm N-T=(3\,\mathrm{kg})a.
$$

Por tanto, $a=20/7\,\mathrm{m/s^2}$ y $T=150/7\,\mathrm N$. La aceleración confirma el sentido supuesto y la tensión es positiva. Su sustitución produce veinte newtons de fuerza motriz conjunta sobre siete kilogramos en estas ecuaciones escalares. Aplicar fricción cinética desde el comienzo del primer ensayo habría predicho un movimiento que sus condiciones iniciales y su contacto no exigen.

### 11. Una caja que acompaña a un vehículo {#solucion-5-11}

Para acompañar la primera aceleración, la caja necesita $f=ma=15\,\mathrm N$ hacia la derecha. La normal es cincuenta y el límite estático, veinte; no desliza. La fuerza no apunta contra la velocidad de la caja respecto del suelo: proporciona precisamente su aumento hacia la derecha.

En el segundo ensayo, la adherencia requeriría veinticinco newtons, más de los veinte permitidos. La plataforma comienza a adelantarse a la caja y el deslizamiento de ésta respecto de aquélla es hacia atrás. La fricción cinética sobre la caja apunta hacia la derecha y vale quince newtons. Su aceleración en el laboratorio es $15/5=3\,\mathrm{m/s^2}$, mientras que la aceleración relativa es

$$
a_{\text{caja/plataforma}}=3-5=-2\,\mathrm{m/s^2}.
$$

Parten con velocidad relativa cero y esa aceleración negativa genera la velocidad relativa hacia atrás que utilizamos para escoger el signo. El cálculo es consistente hasta que cambie la aceleración del vehículo o la caja deje de apoyarse en su plataforma. Todas las ecuaciones de fuerzas de esta solución se escribieron en el laboratorio inercial.

### 12. Alcanzar la velocidad de una cinta {#solucion-5-12}

Al comienzo, $u=0-3=-3\,\mathrm{m/s}$. La fricción cinética sobre la caja apunta hacia la derecha y tiene módulo $\mu_kmg=4\,\mathrm N$, con aceleración $2\,\mathrm{m/s^2}$. Hasta compartir la velocidad de la cinta,

$$
v=2\theta\,\mathrm{m/s},\qquad x=\theta^2\,\mathrm m.
$$

La igualdad $v=3\,\mathrm{m/s}$ ocurre en $t=1{,}5\,\mathrm s$, con $x=2{,}25\,\mathrm m$. En ese instante desaparece el deslizamiento relativo. Para conservar la velocidad común, constante, la fricción requerida es cero, admisible en el régimen estático. Después $v=3\,\mathrm{m/s}$ y

$$
x=2{,}25\,\mathrm m+(3\,\mathrm{m/s})(t-1{,}5\,\mathrm s).
$$

En tres segundos la posición es $6{,}75\,\mathrm m$. La caja nunca estuvo en reposo respecto del laboratorio durante este segundo tramo; lo está respecto de la cinta. Continuar aplicando cuatro newtons la haría superar la velocidad de ésta y contradiría la ley elegida para el deslizamiento anterior.

### 13. Arrastrar dos bloques apilados {#solucion-5-13}

Si no deslizan entre sí, los dos bloques comparten $a=F/[(2+3)\,\mathrm{kg}]$. La única fuerza horizontal sobre el superior es la fricción que le transmite el inferior, por lo que requiere $f=2\,\mathrm{kg}\,a=2F/5$ hacia la derecha. La normal entre ambos es veinte newtons y el máximo estático, diez. Así, $2F/5\leq10\,\mathrm N$ equivale a $F\leq25\,\mathrm N$. Para fuerzas hacia la derecha, el mayor módulo compatible es veinticinco newtons.

Con treinta, la aceleración común supuesta requeriría doce newtons sobre el superior, que el contacto no puede proporcionar estáticamente. El inferior comienza a adelantarse y la fricción cinética sobre el superior es ocho newtons hacia la derecha. Sobre el inferior actúa la fuerza opuesta de ocho hacia la izquierda. Las aceleraciones son

$$
a_{\mathrm{sup}}=\frac8{2}\,\mathrm{m/s^2}=4\,\mathrm{m/s^2},
\qquad a_{\mathrm{inf}}=\frac{30-8}{3}\,\mathrm{m/s^2}
=\frac{22}{3}\,\mathrm{m/s^2}.
$$

Su diferencia es $a_{\mathrm{sup}}-a_{\mathrm{inf}}=-10/3\,\mathrm{m/s^2}$, que produce desde el reposo relativo un deslizamiento del superior hacia atrás respecto del inferior. La dirección escogida queda comprobada. La normal de la mesa bajo el bloque inferior es cincuenta newtons, pero no se utiliza para la fricción entre bloques: esa interacción depende de su propia normal, de veinte.

### 14. Una cuerda que tendría que empujar {#solucion-5-14}

Tomemos positivo hacia la derecha para ambos. Una cuerda tensa tiraría de A hacia B, con fuerza $+T$, y de B hacia A, con $-T$. Si se mantuviera la separación, compartirían aceleración y deberían satisfacer

$$
6\,\mathrm N+T=(2\,\mathrm{kg})a,
\qquad -T=(1\,\mathrm{kg})a.
$$

Sumar da $a=2\,\mathrm{m/s^2}$ y la segunda ecuación, $T=-2\,\mathrm N$. Es una compresión, excluida para la cuerda flexible. El resultado rechaza la hipótesis de cuerda tensa.

Con holgura, $T=0$. A tiene aceleración $3\,\mathrm{m/s^2}$ y B permanece con aceleración cero. Mientras no se produzca otro contacto, la separación inicial disminuye según $x_B-x_A=1\,\mathrm m-(3/2\,\mathrm{m/s^2})t^2$. Es menor que la longitud disponible de cuerda para tiempos positivos pequeños, consistente con la holgura. Para fijar ese intervalo exigimos $x_B-x_A>0$. Escribiendo $\theta=t/(1\,\mathrm s)$, la condición es $1-3\theta^2/2>0$, por lo que el tramo de holgura con A a la izquierda de B corresponde a $0<t<\sqrt{2/3}\,\mathrm s$. La separación tiende a cero en el extremo superior: las partículas llegan a una coincidencia espacial y la continuación exigiría precisar su interacción en ese encuentro. En todo el intervalo abierto la separación permanece entre cero y un metro, de modo que la tensión nula es consistente con una cuerda cuya longitud es un metro.

### 15. Cuándo no hay una sola tensión {#solucion-5-15}

Para la masa inferior, la ecuación hacia arriba es $T_0-(3\,\mathrm{kg})g=(3\,\mathrm{kg})a$. Resulta $T_0=(3\,\mathrm{kg})(g+a)=36\,\mathrm N$. Para el sistema formado por masa y cuerda, la fuerza superior debe acelerar cuatro kilogramos y sostener su peso: $T_{\mathrm{sup}}=(4\,\mathrm{kg})(g+a)=48\,\mathrm N$.

En una sección intermedia elegimos todo lo situado debajo. La densidad lineal de la cuerda es $\lambda=1\,\mathrm{kg}/(2\,\mathrm m)=0{,}5\,\mathrm{kg/m}$. La masa del sistema inferior es $3\,\mathrm{kg}+\lambda z$. Su ecuación da

$$
T(z)=(3\,\mathrm{kg}+\lambda z)(g+a)
=36\,\mathrm N+(6\,\mathrm{N/m})z.
$$

En $z=0$ y $z=2\,\mathrm m$ se recuperan los dos extremos. La diferencia de tensiones proporciona el peso y la aceleración de la parte de cuerda que queda entre las secciones. La aproximación de masa despreciable ya no es válida. Una cuerda puede ser prácticamente inextensible y, sin embargo, tener masa suficiente para que la tensión varíe a lo largo de ella.

### 16. Una decisión con datos acotados {#solucion-5-16}

La normal es cuarenta newtons y el máximo estático varía entre catorce y dieciocho. Para garantizar el reposo en todas las combinaciones, el mayor tirón tendría que ser a lo sumo el menor límite disponible: $18\leq14$ en newtons. La condición no se cumple.

Hay reposo admisible, por ejemplo, con $F=14\,\mathrm N$ y $\mu_s=0{,}45$, pues se requieren catorce y se permiten dieciocho. Con $F=18\,\mathrm N$ y $\mu_s=0{,}35$, se requieren dieciocho y sólo se permiten catorce: no puede mantenerse adherencia. Las dos elecciones pertenecen al rectángulo declarado, por lo que tampoco puede afirmarse que toda la familia desliza.

Cuando $F=\mu_smg$, el reposo pertenece al límite admisible; esa igualdad no obliga por sí sola a iniciar movimiento. No se pueden asignar probabilidades a las partes de este rectángulo sin un modelo probabilístico adicional. Las bandas sólo especifican restricciones deterministas.

Podemos reunir la decisión en el margen $S=\mu_smg-F$. La adherencia requiere $S\geq0$. Como el margen aumenta con $\mu_s$ y disminuye con $F$, sus extremos sobre el rectángulo son $S_{\min}=-4\,\mathrm N$ y $S_{\max}=4\,\mathrm N$. Una familia con margen mínimo no negativo admitiría reposo en todas sus combinaciones; una con margen máximo negativo lo excluiría en todas. Los signos opuestos de este caso explican por qué hacen falta datos más precisos para decidir el régimen de un ensayo particular. La comparación utiliza la misma propagación de cotas del capítulo 0, aplicada ahora a una desigualdad física.

### 17. Medir dos coeficientes mediante dos ensayos {#solucion-5-17}

En el primer ensayo, el criterio de reposo sin fuerza aplicada es $\tan\alpha\leq\mu_s$, con el límite en $\mu_s=\tan\alpha_c$. La tangente es creciente entre veinte y veintidós grados. Por tanto,

$$
\mu_s\in[\tan20^\circ,\tan22^\circ]
\subset[0{,}363,0{,}405].
$$

La última banda está redondeada hacia fuera. La inferencia utiliza el ensayo cuasiestático y el criterio límite adoptado; si la inclinación se cambiara deprisa o el inicio no se identificara adecuadamente, habría que revisar el procedimiento.

En el ensayo deslizante, elegimos positivo hacia abajo. La segunda ley da $a=g\sin30^\circ-\mu_kg\cos30^\circ$. Despejando,

$$
\mu_k=\frac{5\,\mathrm{m/s^2}-a}{5\sqrt3\,\mathrm{m/s^2}}
\in\left[\frac{2{,}8}{5\sqrt3},\frac{3{,}0}{5\sqrt3}\right]
\subset[0{,}323,0{,}347].
$$

Aumentar la aceleración observada reduce el coeficiente inferido, por lo que los extremos cambian de orden al despejar. Se conserva $\mu_k<\mu_s$ en toda esta pareja de bandas. El primer ensayo investiga el umbral estático; no contiene una medición de la fuerza mientras las superficies deslizan. Los dos parámetros requieren información de regímenes diferentes.

### 18. Reposo relativo en una plataforma que gira {#solucion-5-18}

La pieza está en reposo respecto de la plataforma, pero en el laboratorio describe un círculo. Su aceleración es radial hacia el centro, de módulo $\omega^2R$. La normal es veinte newtons y el máximo estático, nueve. La única fuerza horizontal es la fricción, por lo que, con $\omega=1\,\mathrm{s^{-1}}$,

$$
\|\mathbf f\|=m\omega^2R=4\,\mathrm N,
$$

dirigida hacia el centro. Es menor que nueve y la trayectoria sin deslizamiento es admisible. En general se requiere $m\omega^2R\leq\mu_smg$, de donde

$$
|\omega|\leq\sqrt{\frac{\mu_sg}{R}}=1{,}5\,\mathrm{s^{-1}}.
$$

Para $\omega=2\,\mathrm{s^{-1}}$ se necesitarían dieciséis newtons, más de los nueve disponibles estáticamente. La historia circular compartida es inadmisible. No se ha dado el coeficiente cinético ni se ha resuelto el movimiento relativo posterior, así que no podemos deducir de esa prueba una trayectoria completa después de perder adherencia. Tampoco se añade otra fuerza llamada centrípeta: el módulo calculado era la demanda radial sobre el contacto.

### 19. La misma fuerza y dos preparaciones {#solucion-5-19}

La normal es veinte newtons, el máximo estático ocho y el módulo cinético cuatro. En la preparación en reposo se necesita $f=-6\,\mathrm N$, dentro de la banda estática. Bajo la convención de conservar adherencia, $v=0$ y la posición no cambia durante los dos segundos.

En la preparación que ya desliza a la derecha, $f=-4\,\mathrm N$ y la fuerza neta es dos newtons hacia la derecha. La aceleración es $1\,\mathrm{m/s^2}$. Midiendo la posición desde el lugar inicial de ese ensayo,

$$
v=(1+\theta)\,\mathrm{m/s},
\qquad x=(\theta+\theta^2/2)\,\mathrm m.
$$

En dos segundos la velocidad es tres metros por segundo y el desplazamiento, cuatro metros. La velocidad se conserva positiva en todo el tramo y no hay cambio de régimen. La fuerza aplicada y las propiedades del contacto coinciden entre ensayos, pero el estado inicial selecciona situaciones diferentes. Una curva que pretendiera asignar una única fricción a cada fuerza aplicada, sin indicar la preparación y el movimiento relativo, perdería esa información.

### 20. Elegir el ángulo del tirón {#solucion-5-20}

Para conservar contacto sin aceleración vertical, $N=mg-F\sin\alpha$. El reposo horizontal exige una fricción opuesta de módulo $F\cos\alpha$. En el límite estático,

$$
F\cos\alpha=\mu_s(mg-F\sin\alpha),
\qquad
F_c(\alpha)=\frac{\mu_smg}{\cos\alpha+\mu_s\sin\alpha}.
$$

El denominador es positivo en el dominio. Minimizar el cociente equivale a maximizar ese denominador, porque el numerador permanece fijo y positivo. El producto escalar de $(\cos\alpha,\sin\alpha)$ con $(1,\mu_s)$ es a lo sumo $\sqrt{1+\mu_s^2}$, ya que el primer vector es unitario. La igualdad se alcanza cuando ambos tienen la misma dirección, es decir, cuando $\tan\alpha=\mu_s$. Ese ángulo pertenece al dominio, por lo que

$$
\alpha_* =\arctan\mu_s,
\qquad F_{c,\min}=\frac{\mu_smg}{\sqrt{1+\mu_s^2}}.
$$

La desigualdad utilizada también se comprueba expandiendo $(\sin\alpha-\mu_s\cos\alpha)^2\geq0$, que da $(\cos\alpha+\mu_s\sin\alpha)^2\leq1+\mu_s^2$. El argumento identifica el máximo global y su igualdad, no sólo un punto crítico local.

Con los datos numéricos, $\alpha_*\approx26{,}565^\circ$ y $F_{c,\min}=8\sqrt5\,\mathrm N\approx17{,}889\,\mathrm N$, frente a veinte newtons para un tirón horizontal. En el óptimo, $\sin\alpha_*=1/\sqrt5$ y $\cos\alpha_*=2/\sqrt5$. La componente vertical es ocho newtons, de modo que $N=32\,\mathrm N>0$; la horizontal vale dieciséis y coincide con $\mu_sN$.

En general, al sustituir $F_c(\alpha)$, la normal es $mg\cos\alpha/(\cos\alpha+\mu_s\sin\alpha)>0$ en todo el dominio dado. El mínimo no se ha obtenido levantando el bloque. En la igualdad crítica aún existe un reposo admisible; para excluirlo con ese ángulo hay que superar el umbral, manteniendo la normal positiva. La cuenta determina la frontera de adherencia y la dirección que exige el menor tirón para llegar a ella.

## Lecturas de apoyo

El inventario de fuerzas, los sistemas y las normales admisibles se construyen en el [capítulo 4, «Fuerzas y leyes de Newton»](04_Fuerzas_y_leyes_de_Newton.md). Las historias por tramos y sus fronteras retoman los capítulos 1 y 2; las velocidades relativas y la aceleración circular, el capítulo 3. El capítulo 0 permite interpretar las cotas de los ejercicios 16 y 17. Se utilizan álgebra, proyecciones, derivadas e integrales elementales. Los dos criterios formales de admisibilidad se demuestran en el texto; la ley de Coulomb y la cuerda ideal son modelos físicos declarados.

Se consultaron pasajes de Young y Freedman, *Sears y Zemansky. Física universitaria*, vol. 1, 13.ª ed. (Pearson, 2013), §5.2 en el ejemplo del deslizador y la pesa, y §5.3 sobre contacto, fricción estática y cinética; y de Serway y Jewett, *Física para ciencias e ingeniería*, vol. 1, 10.ª ed. española (Cengage, 2019 según créditos), ejemplo 5.9, sobre dos masas unidas por una polea fija, y el apartado de fuerzas de fricción con ecuaciones 5.9–5.10 y ejemplo 5.11. Los enunciados, datos, soluciones y figuras de este capítulo se desarrollaron para esta obra; no son traducciones ni reproducciones de ejercicios específicos de esas fuentes.

El cotejo con Michael Spivak, *Physics for Mathematicians. Mechanics I* (Publish or Perish, 2010), se concentra en el capítulo 6, pp. 241–243, sobre restricciones de cuerda y el límite de masa despreciable, y el comienzo del capítulo 11, pp. 409–412, sobre el carácter empírico y simplificado de las leyes de fricción. Esos pasajes ayudan a precisar las hipótesis del elemento mecánico y el alcance del modelo; no se trasladan aquí sus desarrollos posteriores sobre cuerpos rígidos o paradojas de contacto.

---

[← 4. Fuerzas y leyes de Newton](fisica-para-matematicos-04-fuerzas-y-leyes-de-newton.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [6. Cuerpos conectados y restricciones →](fisica-para-matematicos-06-cuerpos-conectados-y-restricciones.md)
