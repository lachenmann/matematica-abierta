---
title: "Impulso, colisiones y centro de masa"
subtitle: "Física para matemáticos · Tomo I · Capítulo 9"
author: "A. Peña"
description: "Capítulo 9 de la edición revisada, con problemas y soluciones desarrolladas."
content-id: MA-BCH-0354
source-id: FISPM-r20261021-C09
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
edition: r20261021
canonical-edition: true
date-modified: 2026-10-21
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0353"]
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

[← 8. Potencial, equilibrio y estabilidad](fisica-para-matematicos-08-potencial-equilibrio-y-estabilidad.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [10. El oscilador armónico →](fisica-para-matematicos-10-el-oscilador-armonico.md)

Un carro de dos kilogramos avanza a tres metros por segundo por un riel horizontal. Alcanza a otro carro de un kilogramo que está en reposo; sus enganches se traban y ambos continúan juntos. Conocer la fuerza que se ejercen durante el contacto exigiría describir la deformación de los enganches. Sin embargo, podemos averiguar su velocidad común sin reconstruir esa fuerza.

Tomaremos el laboratorio como marco inercial y el sentido inicial del primer carro como positivo. Representaremos cada carro por una partícula de masa constante. Los instantes de comparación estarán inmediatamente antes y después del choque; durante ese intervalo omitiremos el impulso horizontal del riel y del aire. El peso y la normal se compensan verticalmente. La hipótesis decisiva se refiere al sistema de los dos carros: las fuerzas de contacto son internas, y sus contribuciones a la variación del movimiento total se cancelan por la tercera ley de Newton.

Si llamamos $F(t)$ a la fuerza que el segundo carro ejerce sobre el primero, las ecuaciones horizontales son $m_1\dot v_1=F$ y $m_2\dot v_2=-F$. Sumarlas elimina precisamente la función desconocida:

$$
\frac{d}{dt}(m_1v_1+m_2v_2)=0.
$$

La combinación entre paréntesis conserva su valor. Antes del contacto vale $(2\,\mathrm{kg})(3\,\mathrm{m/s})=6\,\mathrm{kg\,m/s}$. Después, ambos carros tienen una misma velocidad $V$, y obtenemos

$$
(2\,\mathrm{kg}+1\,\mathrm{kg})V=6\,\mathrm{kg\,m/s},
\qquad V=2\,\mathrm{m/s}.
$$

La energía cinética inicial era nueve joules; la final es seis. Los tres joules de diferencia pueden convertirse en deformación, vibración y energía interna. La hipótesis que permitió sumar las ecuaciones de Newton sigue siendo válida aunque la energía cinética cambie. El choque ha dado una ocasión concreta para separar dos balances que hasta aquí podían parecer inseparables.

![Los dos carros antes y después del enganche, con sus velocidades y el balance de energía cinética.](/assets/books/fispm/r20261021/impulso_carros.svg){.fpm-v04-figure}

*Figura 9.1.* Los instantes dibujados delimitan el choque. El momento horizontal total vale seis kilogramos metro por segundo en ambos; la energía cinética disminuye tres joules. Las flechas indican sentidos, sin fijar una escala de fuerza.

## Acumular una fuerza durante un intervalo

Para el primer carro, la interacción cambió la velocidad de tres a dos metros por segundo. Su masa permite expresar ese cambio como una variación de $-2\,\mathrm{kg\,m/s}$. El segundo adquirió $+2\,\mathrm{kg\,m/s}$. Esas cantidades se obtienen integrando las fuerzas respectivas durante el contacto, incluso si sus valores instantáneos son desconocidos.

**Definición.** El *momento lineal*, o cantidad de movimiento, de una partícula newtoniana de masa $m>0$ y velocidad $\mathbf v$ es $\mathbf p=m\mathbf v$. El *impulso* de una fuerza $\mathbf F$ en el intervalo $[t_a,t_b]$, con $t_b>t_a$, es

$$
\mathbf J=\int_{t_a}^{t_b}\mathbf F(t)\,dt,
$$

si sus componentes son integrables. El momento tiene unidades de $\mathrm{kg\,m/s}$ y el impulso de $\mathrm{N\,s}$; ambas unidades son equivalentes. Los dos son vectores. Un valor negativo de una componente indica sentido respecto del eje elegido.

**Proposición.** Para una partícula de masa constante que satisface $m\dot{\mathbf v}=\mathbf F_{\rm neta}$ en un marco inercial, con velocidad continua y fuerza neta continua por tramos en una partición finita del intervalo, satisfaciendo la ecuación en cada tramo,

$$
\mathbf p(t_b)-\mathbf p(t_a)=\int_{t_a}^{t_b}\mathbf F_{\rm neta}(t)\,dt.
$$

**Demostración.** La masa constante permite escribir $\dot{\mathbf p}=m\dot{\mathbf v}=\mathbf F_{\rm neta}$. Integramos cada componente en cada tramo de continuidad de la fuerza y aplicamos el teorema fundamental del cálculo. Al sumar los tramos, las velocidades en sus extremos comunes se cancelan porque la velocidad es continua. Queda la diferencia de momentos entre los extremos del intervalo completo. No se exige continuidad de la aceleración en las uniones.

La integral es un área con signo cuando la fuerza tiene una sola componente. Dos pulsos pueden tener la misma área y producir el mismo cambio de momento, aunque difieran mucho sus máximos. La fuerza media vectorial queda definida por $\overline{\mathbf F}=\mathbf J/(t_b-t_a)$. Por tanto, un impulso y una duración conocidos determinan la media, pero dejan indeterminado el máximo. Si la fuerza cambia de dirección, las contribuciones pueden cancelarse y la media puede ser cero pese a una interacción intensa.

![Dos perfiles temporales, rectangular y triangular, tienen áreas iguales y máximos distintos.](/assets/books/fispm/r20261021/impulso_perfiles.svg){.fpm-v04-figure}

*Figura 9.2.* En el ejemplo de la figura, ambos pulsos positivos duran medio segundo y entregan dos newton segundo. Sus máximos son cuatro y ocho newtons. El área determina la variación de momento; el detalle temporal exige información adicional.

El modelo de choque instantáneo resume un intervalo corto mediante velocidades anteriores y posteriores. El salto ideal de velocidad representa un impulso finito: no se obtiene sustituyendo una fuerza ordinaria finita en un intervalo de duración cero. Para calcular una fuerza media o un máximo hay que recuperar información sobre la duración o el perfil del contacto.

## La frontera del sistema decide qué se cancela

La fuerza que un carro ejerce sobre el otro es externa al carro que la recibe y resulta interna al conjunto de ambos. Por eso la elección del sistema debe preceder al uso de una conservación.

**Definición.** Para un sistema cerrado de $N$ partículas con masas constantes $m_i>0$, su momento lineal total es $\mathbf P=\sum_{i=1}^N m_i\mathbf v_i$. Diremos que el sistema es cerrado en este análisis si seguimos las mismas partículas durante todo el intervalo. Separaremos la fuerza sobre cada una en la fuerza externa $\mathbf F_i^{\rm ext}$ y las fuerzas internas $\mathbf F_{ij}$ recibidas de las otras partículas.

**Proposición.** Si las partículas obedecen las leyes de Newton en el mismo marco inercial y las fuerzas internas satisfacen $\mathbf F_{ij}=-\mathbf F_{ji}$, entonces

$$
\dot{\mathbf P}=\mathbf F^{\rm ext},
\qquad
\mathbf F^{\rm ext}=\sum_i\mathbf F_i^{\rm ext},
\qquad
\mathbf P_b-\mathbf P_a=\mathbf J^{\rm ext}.
$$

Aquí la última igualdad requiere integrar sobre el intervalo, con la regularidad del resultado anterior. Si $\mathbf F^{\rm ext}=0$ durante todo él, $\mathbf P$ es constante.

**Demostración.** Sumamos las ecuaciones de todas las partículas. En la doble suma interna, cada par aparece como $\mathbf F_{ij}+\mathbf F_{ji}=0$, de modo que

$$
\dot{\mathbf P}
=\sum_i\mathbf F_i^{\rm ext}
+\sum_{i<j}(\mathbf F_{ij}+\mathbf F_{ji})
=\mathbf F^{\rm ext}.
$$

La integración proporciona el balance entre extremos. Cuando la resultante externa se anula, cada componente de $\mathbf P$ tiene derivada cero y permanece constante.

Para este resultado basta la igualdad vectorial entre fuerzas opuestas; no necesitamos suponer que sean centrales. El alcance declarado es el de un sistema newtoniano de partículas con masas constantes y acción y reacción de esa forma. Un sistema abierto que incorpora o expulsa materia necesita contabilizar también el momento que cruza su frontera; aplicar sin más esta suma a un cohete omitiría ese intercambio.

La conservación puede ser parcial. Si $F_x^{\rm ext}=0$, se conserva $P_x$, aunque otra componente cambie. Además, una integral externa nula sólo asegura igualdad entre los momentos de los dos extremos: puede haber variaciones intermedias que se compensen. El ejercicio 19 construye un caso así.

En un choque real, la aproximación relevante puede medirse. Para cualquier norma euclídea,

$$
\|\mathbf P_b-\mathbf P_a\|
\leq\int_{t_a}^{t_b}\|\mathbf F^{\rm ext}(t)\|\,dt.
$$

Si la resultante externa tiene módulo a lo sumo $B$ durante $\Delta t$, el error de tratar el momento total como constante no supera $B\Delta t$. Esta cota se compara con la tolerancia del problema. Dividir por el momento inicial puede ser una mala elección: ese momento podría ser cero por cancelación de dos movimientos grandes. Para una velocidad común de una masa total $M$, la cota de error correspondiente es $B\Delta t/M$.

## Un punto que reúne el movimiento colectivo

El valor dos metros por segundo que hallamos para los carros ya estaba presente antes del enganche. Era la velocidad media ponderada por sus masas: el primer carro contribuía dos partes de tres y el segundo una parte de tres. Podemos hacer la misma construcción con sus posiciones.

**Definición.** Para las mismas $N$ partículas y masa total $M=\sum_i m_i$, el *centro de masa* es el punto de posición

$$
\mathbf R=\frac{1}{M}\sum_i m_i\mathbf r_i.
$$

Se trata de una media de posiciones, con pesos positivos que suman uno. Para dos partículas está sobre el segmento que las une, más cerca de la de mayor masa. Puede no coincidir con ninguna partícula ni con un punto material del cuerpo: el centro de un aro uniforme está en su hueco.

**Proposición.** En un sistema cerrado de masas constantes se cumple $\mathbf P=M\dot{\mathbf R}$. Bajo las hipótesis del balance de momento, además,

$$
M\ddot{\mathbf R}=\mathbf F^{\rm ext}.
$$

**Demostración.** Derivamos la suma finita que define $M\mathbf R$. Como sus masas son constantes, resulta $M\dot{\mathbf R}=\sum_i m_i\mathbf v_i=\mathbf P$. Una segunda derivación y el balance anterior dan la ecuación anunciada.

El resultado explica por qué el centro de masa sigue un movimiento sencillo cuando las partes se separan o se deforman. Si la única resultante externa es la gravedad uniforme, $\mathbf F^{\rm ext}=M\mathbf g$ y $\ddot{\mathbf R}=\mathbf g$, aunque el cuerpo gire o estalle. Para fuerzas externas que dependan de cada posición, la suma puede requerir conocer la configuración; la ecuación del centro de masa no garantiza por sí sola un problema cerrado para $\mathbf R$.

![Dos partículas de masas distintas se sitúan respecto de su centro de masa.](/assets/books/fispm/r20261021/impulso_centro.svg){.fpm-v04-figure}

*Figura 9.3.* Para masas de uno y tres kilogramos situadas en cero y cuatro metros, el centro está en tres metros. Las separaciones ponderadas se compensan: $1(0-3)+3(4-3)=0$, en kilogramos metro.

Elegir un observador que se traslada con velocidad constante $\mathbf U$ reemplaza cada velocidad por $\mathbf v_i'=\mathbf v_i-\mathbf U$. Entonces $\mathbf P'=\mathbf P-M\mathbf U$. El valor de $\mathbf P$ depende del observador, pero su cambio entre dos instantes es el mismo porque $M$ y $\mathbf U$ son constantes. En ausencia de impulso externo podemos tomar $\mathbf U=\dot{\mathbf R}$ y describir el choque en el marco del centro de masa, donde el momento total es cero.

## La energía del movimiento relativo

Los tres joules que dejaron de ser energía cinética en el enganche inicial corresponden al movimiento que un carro tenía respecto del otro. Para precisar esa idea, separaremos de cada velocidad la velocidad del centro de masa.

**Proposición.** Sean $\mathbf V=\dot{\mathbf R}$ y $\mathbf w_i=\mathbf v_i-\mathbf V$. La energía cinética total satisface

$$
K=\sum_i\frac12m_i\|\mathbf v_i\|^2
=\frac12M\|\mathbf V\|^2+\sum_i\frac12m_i\|\mathbf w_i\|^2.
$$

Para dos partículas, si $\mu=m_1m_2/(m_1+m_2)$, la expresión se reduce a

$$
K=\frac12M\|\mathbf V\|^2
+\frac12\mu\|\mathbf v_1-\mathbf v_2\|^2.
$$

**Demostración.** Al desarrollar $\|\mathbf V+\mathbf w_i\|^2$, los términos cruzados suman $\mathbf V\cdot\sum_i m_i\mathbf w_i$. Esta suma ponderada es $\mathbf P-M\mathbf V=0$, de modo que sólo quedan los dos términos indicados. Para dos partículas, la propia definición de $\mathbf V$ da

$$
\mathbf w_1=\frac{m_2}{M}(\mathbf v_1-\mathbf v_2),
\qquad
\mathbf w_2=-\frac{m_1}{M}(\mathbf v_1-\mathbf v_2).
$$

Al sustituir las dos igualdades, el coeficiente de la energía relativa queda

$$
[m_1m_2^2+m_2m_1^2]/(2M^2)=\mu/2.
$$

Todos los sumandos del movimiento relativo son no negativos. Para un momento total fijado, $\mathbf V=\mathbf P/M$ también está fijada y el menor valor posible de $K$ es $\|\mathbf P\|^2/(2M)$. Se alcanza exactamente cuando todas las partículas tienen la misma velocidad. Es una afirmación sobre energía cinética de traslación del modelo de partículas: en cuerpos extensos deben incluirse los movimientos de sus partes para contabilizar rotación y vibración.

En nuestros carros, $\mu=2/3\,\mathrm{kg}$ y la rapidez relativa inicial era tres metros por segundo. Su energía relativa era $\mu(3\,\mathrm{m/s})^2/2=3\,\mathrm J$. El enganche la elimina por completo, mientras la energía del centro de masa permanece en seis joules.

![La energía cinética se descompone en movimiento del centro de masa y movimiento relativo.](/assets/books/fispm/r20261021/impulso_energia.svg){.fpm-v04-figure}

*Figura 9.4.* Las barras representan el ejemplo inicial. El enganche conserva la parte asociada al centro de masa y lleva a cero la energía cinética relativa. El balance de energía total debe incluir los otros modos que reciben los tres joules.

Si dos cuerpos se separan mediante un resorte que estaba comprimido, el proceso inverso puede aumentar su energía cinética a momento total constante. La energía procede del resorte. Por eso una ley de conservación del momento no decide, por sí sola, si la energía cinética aumenta, disminuye o permanece igual.

## Qué condición falta para resolver un choque

En una recta, la conservación proporciona $m_1u_1+m_2u_2=m_1v_1+m_2v_2$, donde $u_i$ y $v_i$ son las velocidades anteriores y posteriores. Hay dos incógnitas y una sola ecuación. La condición de enganche añadió $v_1=v_2$ y cerró el problema inicial. Otro tipo de contacto necesita otra información.

**Definición.** Llamaremos *elástico* a un choque si la energía cinética total del sistema considerado tiene el mismo valor antes y después. En el modelo de dos partículas, un choque *perfectamente inelástico* tiene una velocidad final común: la velocidad relativa final es nula. Las comparaciones se hacen entre estados en que ya terminó la interacción transitoria; el término elástico no obliga a que la energía cinética sea constante durante la compresión.

Para estudiar un contacto frontal unidimensional, situemos el cuerpo 1 a la izquierda del 2 antes del encuentro y supongamos $u_1-u_2>0$, de modo que se acercan. Si después se separan o quedan unidos, $v_2-v_1\geq0$. El cociente

$$
e=\frac{v_2-v_1}{u_1-u_2}
$$

es el *coeficiente de restitución* de ese encuentro. El valor debe medirse o deducirse de un modelo de contacto. No es una consecuencia de las leyes de conservación. En esta descripción, $e=0$ expresa velocidad final común; no afirma por sí solo que un adhesivo mantendrá unidos los cuerpos para siempre.

**Proposición.** Para dos partículas de masas positivas en un choque frontal, sin impulso externo, con acercamiento inicial $u_1-u_2>0$ y restitución $e\geq0$, sean

$$
V=\frac{m_1u_1+m_2u_2}{M},\qquad M=m_1+m_2.
$$

Las velocidades finales y la disminución de energía cinética son

$$
\begin{aligned}
v_1&=V-\frac{m_2}{M}e(u_1-u_2),\\
v_2&=V+\frac{m_1}{M}e(u_1-u_2),\\
K_a-K_b&=\frac12\mu(1-e^2)(u_1-u_2)^2.
\end{aligned}
$$

**Demostración.** La conservación fija la media ponderada final en $V$, y la restitución fija $v_2-v_1=e(u_1-u_2)$. Sustituir $v_2=v_1+e(u_1-u_2)$ en la media determina $v_1$; sumar la diferencia proporciona $v_2$. La descomposición de energía cancela la contribución del centro de masa entre ambos estados y deja la diferencia entre los cuadrados de las velocidades relativas, con coeficiente $\mu/2$.

Si el contacto es pasivo en el sentido de que no aumenta esa energía cinética, el resultado exige $0\leq e\leq1$. El caso $e=1$ invierte la velocidad relativa sin cambiar su módulo y es elástico. Un valor mayor que uno indica liberación de energía de otros modos o fallo del modelo y los datos utilizados. La restitución puede depender de la rapidez de impacto y de los materiales; un único ensayo no establece una constante universal.

Con masas iguales y $e=1$, las velocidades se intercambian. Con una masa receptora mucho mayor y en reposo, el cuerpo ligero casi invierte su velocidad mientras el pesado adquiere una velocidad muy pequeña. Esta pequeña velocidad no autoriza a omitir su cambio de momento: su masa es precisamente grande. Una pared anclada requiere incluir la Tierra o contabilizar el impulso de su apoyo.

## Cambiar de balance cuando cambia la etapa

Un proyectil que se incrusta en un bloque suspendido ofrece dos intervalos con información diferente. Durante el impacto, si el bloque está en la posición más baja y el impulso horizontal del soporte es despreciable, el momento horizontal del proyectil y del bloque permite obtener la velocidad común inmediatamente posterior. Durante la elevación siguiente, la gravedad cambia ese momento, pero la tensión ideal no realiza trabajo y el balance de energía mecánica relaciona la rapidez inicial de la subida con su altura máxima. La solución 16 desarrolla ambos intervalos.

![Impacto de un proyectil contra un bloque y ascenso posterior del conjunto.](/assets/books/fispm/r20261021/impulso_etapas.svg){.fpm-v04-figure}

*Figura 9.5.* El estado inmediatamente posterior al choque conecta dos balances. La subida recupera la energía cinética que quedó después del impacto; no recupera la energía transformada durante la incrustación. Se supone traslación del bloque sin rotación apreciable.

En el plano, conservar el momento proporciona dos ecuaciones escalares. Si ambos cuerpos quedan juntos, esas ecuaciones determinan las dos componentes de la velocidad común. Si salen separados, hay cuatro componentes finales desconocidas; añadir conservación de energía deja todavía, en general, una libertad. Una dirección de salida medida o un modelo geométrico de contacto puede aportar la condición restante. El ejercicio 15 muestra un caso en que una dirección observada permite completar la predicción.

![Dos velocidades finales perpendiculares suman vectorialmente la velocidad inicial en un choque elástico de masas iguales.](/assets/books/fispm/r20261021/impulso_plano.svg){.fpm-v04-figure}

*Figura 9.6.* En el ejercicio 15, una partícula sale a treinta grados y la otra a menos sesenta grados respecto del eje inicial. La perpendicularidad se deduce de momento y energía para masas iguales, con una de ellas inicialmente en reposo y ambas velocidades finales no nulas.

## Del balance a una medición

Para contrastar una conservación necesitamos masas y velocidades con signos, componentes y cotas. Sumar módulos de momentos destruiría las cancelaciones que el balance utiliza. Una comparación tampoco se vuelve concluyente por dar valores centrales cercanos: debe examinarse si los intervalos admiten al menos un balance compatible.

En el ejemplo de enganche, si las masas se tratan como exactas y se sabe que $u_1\in[2{,}9,3{,}1]\,\mathrm{m/s}$ y $u_2\in[-0{,}1,0{,}1]\,\mathrm{m/s}$, la velocidad común predicha sin impulso externo pertenece a $[1{,}9,2{,}1]\,\mathrm{m/s}$. Una medición posterior entre $2{,}15$ y $2{,}19\,\mathrm{m/s}$ queda separada de esa banda. El ejercicio 18 cuantifica el menor impulso externo que permitiría cerrar esa discrepancia si las demás hipótesis se conservan.

![Bandas de velocidad predicha y observada que no se intersectan.](/assets/books/fispm/r20261021/impulso_bandas.svg){.fpm-v04-figure}

*Figura 9.7.* La separación mínima de las bandas es $0{,}05\,\mathrm{m/s}$. Son cotas didácticas, sin interpretación probabilística. Una discrepancia obliga a revisar medición, sistema e intercambios; no identifica automáticamente cuál de ellos falló.

La reconstrucción puede detenerse antes de obtener una solución única. Conocer el momento final de dos cuerpos separados sólo fija una combinación de sus velocidades. La solución 20 conserva esa indeterminación hasta que se incorpora una condición física adicional. Reconocer ese punto forma parte de resolver el problema.

## Ejercicios

Los primeros cuatro problemas trabajan impulso, signos y cotas del entorno. Del 5 al 10 se decide qué información cierra un choque o una separación. Los restantes desarrollan el centro de masa, los cambios de etapa y la lectura crítica de datos. En los datos numéricos de caída se adopta $g=10\,\mathrm{m/s^2}$; son valores didácticos, no registros experimentales. Se omiten aire y rotación salvo indicación contraria, y se trabaja en el marco inercial del laboratorio.

### 1. Un pulso que cambia de signo {#ejercicio-9-1}

Una partícula de $0{,}6\,\mathrm{kg}$ tiene velocidad inicial $-1\,\mathrm{m/s}$. La fuerza neta horizontal vale $12\,\mathrm N$ durante $0{,}2\,\mathrm s$ y luego $-6\,\mathrm N$ durante otros $0{,}2\,\mathrm s$. Calcula el impulso total, la velocidad intermedia y la final. Compara las energías cinéticas inicial y final.

### 2. Un área, dos máximos {#ejercicio-9-2}

Dos aparatos aplican por separado a una partícula de $0{,}5\,\mathrm{kg}$ inicialmente en reposo pulsos horizontales positivos de medio segundo. Uno entrega fuerza constante de cuatro newtons y el otro un pulso triangular con máximo de ocho newtons. Compara impulso, velocidad final, fuerza media y fuerza máxima.

### 3. La fuerza del suelo durante un rebote {#ejercicio-9-3}

Una pelota de $0{,}2\,\mathrm{kg}$ llega verticalmente al suelo a $3\,\mathrm{m/s}$ hacia abajo y sale a $2\,\mathrm{m/s}$ hacia arriba. El contacto dura $0{,}05\,\mathrm s$. Calcula el impulso neto y la fuerza media del suelo sobre ella, incluyendo el peso durante el contacto.

### 4. Cuánto error admite un choque breve {#ejercicio-9-4}

En un enganche de masa total $3\,\mathrm{kg}$, el módulo de la resultante externa horizontal está acotado por $0{,}6\,\mathrm N$ y el choque dura a lo sumo $0{,}01\,\mathrm s$. ¿Con qué error absoluto puede calcularse la velocidad común despreciando ese impulso? ¿Basta la cota para exigir error no mayor que $0{,}001\,\mathrm{m/s}$?

### 5. Seguir por separado a los carros {#ejercicio-9-5}

Para el enganche inicial del capítulo, calcula el impulso que recibió cada carro y la disminución de energía cinética. Explica por qué el momento de cada carro cambia aunque el total se conserve.

### 6. Los mismos carros con otro contacto {#ejercicio-9-6}

Los carros de dos y un kilogramos llegan con velocidades $3\,\mathrm{m/s}$ y cero, respectivamente. El contacto es frontal y tiene $e=1/2$. Sin impulso externo horizontal, calcula velocidades finales y disminución de energía cinética; comprueba que se separan.

### 7. Retroceder tras un choque elástico {#ejercicio-9-7}

Una partícula de un kilogramo alcanza a cuatro metros por segundo a otra de tres kilogramos en reposo. El choque es frontal y elástico, sin impulso externo. Obtén las velocidades finales y comprueba ambos balances.

### 8. Un encuentro de masas iguales {#ejercicio-9-8}

Dos carros de la misma masa llegan uno hacia el otro con velocidades $2\,\mathrm{m/s}$ y $-1\,\mathrm{m/s}$. Para un choque elástico frontal, encuentra las velocidades finales y describe el mismo encuentro desde el marco del centro de masa.

### 9. Una pared que puede moverse {#ejercicio-9-9}

Una partícula de masa $m$ y velocidad $u>0$ choca elásticamente en una recta con un cuerpo libre de masa $M$ inicialmente en reposo. Obtén ambas velocidades finales y estudia el límite $M/m\to\infty$, manteniendo $m$ y $u$ fijos. Calcula el límite del momento adquirido por el cuerpo grande.

### 10. Separarse desde el reposo {#ejercicio-9-10}

Dos carros de masas dos y tres kilogramos están inicialmente en reposo. Un resorte interno los separa en un riel liso hasta que se alejan a una rapidez relativa de cinco metros por segundo, con el primero hacia la izquierda. Encuentra sus velocidades y el aumento total de energía cinética.

### 11. Un centro de masa en el plano {#ejercicio-9-11}

Tres partículas tienen masas $1$, $2$ y $3\,\mathrm{kg}$ y posiciones $(0,0)$, $(3,0)$ y $(0,2)\,\mathrm m$. En ese instante sus velocidades son $(2,0)$, $(0,3)$ y $(-1,0)\,\mathrm{m/s}$. Calcula posición y velocidad del centro de masa, y el momento total.

### 12. Caminar dentro de una barca {#ejercicio-9-12}

Una persona de $60\,\mathrm{kg}$ camina dos metros respecto de una barca de $180\,\mathrm{kg}$ que sólo puede trasladarse horizontalmente. Al principio todo está en reposo; la resultante externa horizontal sobre persona y barca se toma nula durante toda la marcha. ¿Cuánto se desplazan respecto de la orilla la barca y la persona? Modela el desplazamiento del centro de masa de la persona mediante el recorrido indicado.

### 13. Una explosión no cambia la parábola colectiva {#ejercicio-9-13}

Un cuerpo se divide en fragmentos de uno y dos kilogramos en $t=0$, cuando su centro de masa está en el origen y lleva velocidad $(3,4)\,\mathrm{m/s}$. Después sólo actúa gravedad uniforme, con eje vertical hacia arriba. A los $0{,}2\,\mathrm s$, el fragmento ligero está en $(1{,}4,0{,}2)\,\mathrm m$. Determina dónde está el otro.

### 14. Engancharse desde direcciones distintas {#ejercicio-9-14}

En una mesa lisa, una partícula de dos kilogramos llega con velocidad $(3,0)\,\mathrm{m/s}$ y otra de un kilogramo con $(0,3)\,\mathrm{m/s}$. Se enganchan sin rotación en el modelo. Calcula la velocidad común, su módulo y la disminución de energía cinética.

### 15. Una dirección medida cierra el problema {#ejercicio-9-15}

Dos partículas de la misma masa tienen velocidades iniciales $(4,0)\,\mathrm{m/s}$ y cero. El choque es elástico, sin impulso externo, y ambas salen con rapidez positiva. Se mide que la primera sale a $30^\circ$ sobre el eje inicial. Determina ambas velocidades finales y demuestra que son perpendiculares.

### 16. Leer la altura de un péndulo balístico {#ejercicio-9-16}

Un proyectil de $0{,}02\,\mathrm{kg}$ se incrusta horizontalmente en un bloque de $0{,}98\,\mathrm{kg}$ suspendido mediante cuerdas paralelas, inicialmente en reposo en la posición más baja. El conjunto asciende $0{,}20\,\mathrm m$. Durante el choque las cuerdas se mantienen casi verticales y se desprecia su impulso horizontal; en la subida no hay pérdidas y el bloque conserva su orientación. Reconstruye la rapidez del proyectil y la energía cinética transformada en el impacto. En un segundo análisis, conserve exactas las masas y tome $h\in[0{,}19,0{,}21]\,\mathrm m$ y un impulso externo horizontal durante el choque $J\in[-0{,}01,0{,}01]\,\mathrm{N\,s}$, positivo hacia el disparo. Todas las combinaciones se admiten y la subida mantiene sus hipótesis ideales. Obtenga una envolvente de la rapidez inicial y cuantifique la contribución máxima de ese impulso a su error.

### 17. Lo que ocurre en la máxima compresión {#ejercicio-9-17}

Una partícula de un kilogramo, a $4\,\mathrm{m/s}$, comprime un resorte ideal sin masa unido a otra de tres kilogramos inicialmente en reposo. El riel es liso y $k=300\,\mathrm{N/m}$. El resorte comienza sin comprimir y sólo transmite interacción durante el contacto. Calcula la compresión máxima y las velocidades cuando el resorte recupera su longitud natural y termina el contacto.

### 18. Una discrepancia entre bandas {#ejercicio-9-18}

Dos carros de masas exactas dos y un kilogramos se enganchan. Las velocidades iniciales están acotadas por $u_1\in[2{,}9,3{,}1]\,\mathrm{m/s}$ y $u_2\in[-0{,}1,0{,}1]\,\mathrm{m/s}$. La velocidad común medida pertenece a $[2{,}15,2{,}19]\,\mathrm{m/s}$. Decide si existe compatibilidad sin impulso externo y encuentra una cota inferior para el impulso horizontal requerido si se conservan las demás hipótesis.

### 19. Los extremos ocultan un cambio intermedio {#ejercicio-9-19}

Una partícula de un kilogramo parte del reposo. La fuerza neta vale $2\,\mathrm N$ durante un segundo y $-2\,\mathrm N$ durante el segundo siguiente. Calcula el momento en $t=0,1,2\,\mathrm s$, el desplazamiento total y el trabajo neto. ¿Permite la igualdad de momentos inicial y final afirmar que hubo conservación durante el intervalo?

### 20. Todas las salidas que admite el balance {#ejercicio-9-20}

Dos partículas de masas dos y un kilogramos se acercan en una recta con velocidades iniciales tres metros por segundo y cero. Sin impulso externo, se sabe que la energía cinética no aumenta y que al terminar el encuentro ya no se acercan. Describe todas las velocidades finales compatibles con esos datos. Identifica los extremos elástico y de velocidad común. ¿Es única la predicción?

## Soluciones

### 1. Un pulso que cambia de signo {#solucion-9-1}

La integral debe conservar el signo de cada tramo. Los impulsos sucesivos son $J_1=(12\,\mathrm N)(0{,}2\,\mathrm s)=2{,}4\,\mathrm{N\,s}$ y $J_2=-1{,}2\,\mathrm{N\,s}$, de modo que $J=1{,}2\,\mathrm{N\,s}$. El momento inicial vale $-0{,}6\,\mathrm{kg\,m/s}$. Tras el primer tramo es $1{,}8\,\mathrm{kg\,m/s}$, que corresponde a $v=3\,\mathrm{m/s}$; tras el segundo es $0{,}6\,\mathrm{kg\,m/s}$ y $v_f=1\,\mathrm{m/s}$.

Las energías inicial y final son ambas $0{,}3\,\mathrm J$, aunque el impulso neto no es cero. El cambio de sentido permite que dos velocidades distintas tengan el mismo cuadrado. La energía intermedia alcanza $2{,}7\,\mathrm J$: tampoco permaneció constante durante el proceso. Sumar módulos de los impulsos habría dado una velocidad final errónea.

### 2. Un área, dos máximos {#solucion-9-2}

El aparato constante proporciona $J=(4\,\mathrm N)(0{,}5\,\mathrm s)=2\,\mathrm{N\,s}$. El triángulo da la mitad de base por altura, $J=(0{,}5\,\mathrm s)(8\,\mathrm N)/2=2\,\mathrm{N\,s}$. Como la partícula parte del reposo, en ambos casos $v_f=J/m=4\,\mathrm{m/s}$.

La fuerza media es cuatro newtons para ambos perfiles. El máximo coincide con esa media sólo en el pulso constante; en el triangular alcanza ocho. El balance entre extremos no reconstruye la historia temporal, aunque los datos basten para obtener la misma velocidad final y la misma energía de cuatro joules.

### 3. La fuerza del suelo durante un rebote {#solucion-9-3}

Elegimos hacia arriba como sentido positivo, de modo que $u=-3\,\mathrm{m/s}$ y $v=2\,\mathrm{m/s}$. El impulso neto es

$$
J_{\rm neto}=m(v-u)=(0{,}2\,\mathrm{kg})(5\,\mathrm{m/s})=1\,\mathrm{N\,s}.
$$

En el contacto actúan el suelo y el peso. El impulso de la gravedad vale $-mg\Delta t=-0{,}1\,\mathrm{N\,s}$; por tanto, $J_{\rm suelo}=1{,}1\,\mathrm{N\,s}$ y la fuerza media del suelo es $22\,\mathrm N$ hacia arriba. Dividir solamente el impulso neto por la duración daría veinte newtons, que es la fuerza neta media, no la fuerza de contacto solicitada. El dato no determina el máximo de la normal.

### 4. Cuánto error admite un choque breve {#solucion-9-4}

El impulso externo puede tener cualquier perfil compatible con la cota. La desigualdad integral asegura $|J^{\rm ext}|\leq(0{,}6\,\mathrm N)(0{,}01\,\mathrm s)=0{,}006\,\mathrm{N\,s}$. La ecuación exacta para la velocidad común es $MV=P_a+J^{\rm ext}$; la aproximada usa $MV_0=P_a$. Al restar y dividir por tres kilogramos obtenemos

$$
|V-V_0|\leq0{,}002\,\mathrm{m/s}.
$$

La cota no basta para garantizar la tolerancia pedida de una milésima de metro por segundo. Podría haber compensaciones y un error menor en un ensayo particular, pero los datos suministrados no las aseguran. Una cota $B\Delta t\leq0{,}003\,\mathrm{N\,s}$ sería suficiente para esa tolerancia.

### 5. Seguir por separado a los carros {#solucion-9-5}

La velocidad común es $V=2\,\mathrm{m/s}$. El primero recibe $J_1=m_1(V-u_1)=-2\,\mathrm{N\,s}$; el segundo recibe $J_2=m_2(V-u_2)=2\,\mathrm{N\,s}$. La suma es cero porque el contacto es interno al sistema conjunto, aunque cada carro recibe de su compañero un impulso externo a su propio subsistema.

La energía inicial es $K_a=\tfrac12(2)(3)^2\,\mathrm J=9\,\mathrm J$, y la final $K_b=\tfrac12(3)(2)^2\,\mathrm J=6\,\mathrm J$. Disminuye tres joules. La cancelación de impulsos no implica cancelación de trabajos: las fuerzas se aplican a cuerpos cuyos desplazamientos durante el contacto pueden diferir, y el modelo de enganche admite transformación en otros modos de energía.

### 6. Los mismos carros con otro contacto {#solucion-9-6}

La media ponderada sigue siendo $V=2\,\mathrm{m/s}$ porque el momento inicial sigue siendo seis kilogramos metro por segundo. La restitución impone $v_2-v_1=(1/2)(3\,\mathrm{m/s})=1{,}5\,\mathrm{m/s}$. Por tanto,

$$
v_1=2-\frac13\frac12(3)=1{,}5\,\mathrm{m/s},
\qquad
v_2=2+\frac23\frac12(3)=3\,\mathrm{m/s}.
$$

El carro delantero queda más rápido y los cuerpos se separan. La energía final es $\tfrac12(2)(1{,}5)^2+\tfrac12(1)(3)^2=6{,}75\,\mathrm J$, por lo que se transforman $2{,}25\,\mathrm J$. También lo da $\mu(1-e^2)(u_1-u_2)^2/2=(2/3)(3/4)(9)/2\,\mathrm J$. Cambiar el contacto modificó el reparto final, sin modificar el momento colectivo.

### 7. Retroceder tras un choque elástico {#solucion-9-7}

Las masas suman cuatro kilogramos y el momento inicial es $4\,\mathrm{kg\,m/s}$; por tanto $V=1\,\mathrm{m/s}$. Con $e=1$ las velocidades son $v_1=1-(3/4)4=-2\,\mathrm{m/s}$ y $v_2=1+(1/4)4=2\,\mathrm{m/s}$. El signo del primer resultado expresa un retroceso físicamente permitido.

Comprobamos $m_1v_1+m_2v_2=-2+6=4\,\mathrm{kg\,m/s}$ y $K_b=\tfrac12(1)(2)^2+\tfrac12(3)(2)^2=8\,\mathrm J=K_a$. Las velocidades relativas pasan de $u_1-u_2=4\,\mathrm{m/s}$ a $v_1-v_2=-4\,\mathrm{m/s}$. Resolver sólo las dos ecuaciones de conservación también admite las velocidades iniciales como solución algebraica; la condición de salida, con los cuerpos separándose, selecciona la rama del choque realizado.

### 8. Un encuentro de masas iguales {#solucion-9-8}

La velocidad del centro de masa es $V=(2-1)/2=0{,}5\,\mathrm{m/s}$. Respecto de él, los carros llegan con velocidades $+1{,}5$ y $-1{,}5\,\mathrm{m/s}$. El choque elástico invierte esas velocidades y conserva el momento nulo. Al sumar nuevamente $0{,}5\,\mathrm{m/s}$ recuperamos $v_1=-1\,\mathrm{m/s}$ y $v_2=2\,\mathrm{m/s}$.

Las velocidades del laboratorio se intercambiaron. La simetría aparece en el marco del centro de masa aunque en el laboratorio las rapideces iniciales fueran distintas. El momento total cambia de valor al cambiar de marco, pero su constancia se mantiene.

### 9. Una pared que puede moverse {#solucion-9-9}

El sistema debe incluir ambos cuerpos para eliminar la fuerza de contacto. Con $V=mu/(m+M)$ y $e=1$, se obtiene

$$
v_m=\frac{m-M}{m+M}u,
\qquad
v_M=\frac{2m}{m+M}u.
$$

Cuando $M/m\to\infty$, $v_m\to-u$ y $v_M\to0$. Sin embargo,

$$
Mv_M=\frac{2mM}{m+M}u\longrightarrow2mu.
$$

El cuerpo pesado recibe un momento finito mientras su energía cinética $Mv_M^2/2=2m^2Mu^2/(m+M)^2$ tiende a cero. Por eso el límite reproduce un rebote que casi conserva la energía del cuerpo ligero, pero no su momento. Si se analiza sólo ese cuerpo, el impulso de la pared es externo y tiende a $-2mu$. El modelo de pared libre pesada no describe todos los detalles de una pared fijada a la Tierra; explica este límite mecánico concreto.

### 10. Separarse desde el reposo {#solucion-9-10}

El momento inicial es cero. Las velocidades finales deben satisfacer $2v_1+3v_2=0$ en unidades de kilogramos metro por segundo y $v_2-v_1=5\,\mathrm{m/s}$. La segunda ecuación usa la rapidez relativa de separación, no la rapidez de uno de los carros. Al resolver, $v_1=-3\,\mathrm{m/s}$ y $v_2=2\,\mathrm{m/s}$.

La energía cinética adquirida es $\tfrac12(2)(3)^2+\tfrac12(3)(2)^2=15\,\mathrm J$. Como $V=0$, toda ella es relativa; la misma cuenta resulta de $\mu(5\,\mathrm{m/s})^2/2$ con $\mu=6/5\,\mathrm{kg}$. El resorte y sus posibles pérdidas deben suministrar al menos esos quince joules. El movimiento de separación no exige una fuerza externa que acelere el centro de masa.

### 11. Un centro de masa en el plano {#solucion-9-11}

La masa total es seis kilogramos. Ponderamos cada coordenada con la masa correspondiente:

$$
\mathbf R=\frac{1(0,0)+2(3,0)+3(0,2)}6\,\mathrm m
=(1,1)\,\mathrm m.
$$

Para el momento sumamos las velocidades ponderadas, que son objetos diferentes de las posiciones:

$$
\mathbf P=[1(2,0)+2(0,3)+3(-1,0)]\,\mathrm{kg\,m/s}
=(-1,6)\,\mathrm{kg\,m/s}.
$$

Por tanto, $\mathbf V=\mathbf P/M=(-1/6,1)\,\mathrm{m/s}$. El centro de masa puede moverse hacia la izquierda aunque dos de las tres partículas no tengan componente izquierda: la tercera concentra la mayor masa.

### 12. Caminar dentro de una barca {#solucion-9-12}

Sea $b$ el desplazamiento horizontal de la barca respecto de la orilla, positivo en el sentido de la marcha. El desplazamiento de la persona respecto de la orilla será $b+2\,\mathrm m$. Como el sistema conjunto parte con momento horizontal cero y su resultante externa horizontal es nula durante toda la marcha, su momento permanece cero en cada instante. La velocidad del centro de masa es, por tanto, cero durante todo el recorrido y éste mantiene su posición. Así,

$$
(60\,\mathrm{kg})(b+2\,\mathrm m)+(180\,\mathrm{kg})b=0,
$$

de donde $b=-0{,}5\,\mathrm m$ y el desplazamiento de la persona es $1{,}5\,\mathrm m$. El resultado no requiere conocer el modo de caminar ni su velocidad en cada instante. Esos detalles sí importarían para estimar el impulso del agua; si resulta apreciable, la posición colectiva dejaría de ser constante y habría que corregir la ecuación.

### 13. Una explosión no cambia la parábola colectiva {#solucion-9-13}

La gravedad es externa y cambia el momento vertical; sería incorrecto conservar el vector momento entre la división y la observación posterior. En cambio, sabemos exactamente cómo acelera el centro de masa:

$$
\mathbf R(t)=\big((3\,\mathrm{m/s})t,
(4\,\mathrm{m/s})t-\tfrac12gt^2\big).
$$

A los $0{,}2\,\mathrm s$ resulta $\mathbf R=(0{,}6,0{,}6)\,\mathrm m$. La definición de centro de masa sigue siendo válida después de la explosión, y exige $3\mathbf R=\mathbf r_1+2\mathbf r_2$ al insertar las masas en kilogramos. Por tanto,

$$
\mathbf r_2=\frac{3(0{,}6,0{,}6)-(1{,}4,0{,}2)}2\,\mathrm m
=(0{,}2,0{,}8)\,\mathrm m.
$$

No hemos supuesto que los fragmentos tengan energías cinéticas constantes, ni que cada uno siga la trayectoria que habría seguido el cuerpo sin dividirse.

### 14. Engancharse desde direcciones distintas {#solucion-9-14}

El momento inicial es $\mathbf P=(6,3)\,\mathrm{kg\,m/s}$. La velocidad común final se obtiene componente a componente dividiendo por la masa total: $\mathbf V=(2,1)\,\mathrm{m/s}$, cuyo módulo es $\sqrt5\,\mathrm{m/s}$. Se orienta a un ángulo $\arctan(1/2)$ sobre el eje horizontal.

La energía inicial es $K_a=\tfrac12(2)(3)^2+\tfrac12(1)(3)^2=13{,}5\,\mathrm J$, y la final $K_b=\tfrac12(3)(2^2+1^2)=7{,}5\,\mathrm J$. La disminución es seis joules. La rapidez relativa inicial es $\sqrt{3^2+(-3)^2}=\sqrt{18}\,\mathrm{m/s}$, por lo que la fórmula con $\mu=2/3\,\mathrm{kg}$ proporciona la misma disminución. Sumar las rapideces iniciales en lugar de los vectores habría perdido la dirección final.

### 15. Una dirección medida cierra el problema {#solucion-9-15}

Al dividir el balance de momento por la masa común obtenemos $\mathbf u=\mathbf v_1+\mathbf v_2$, con $\mathbf u=(4,0)\,\mathrm{m/s}$. La conservación de energía da $\|\mathbf u\|^2=\|\mathbf v_1\|^2+\|\mathbf v_2\|^2$. Pero el cuadrado de la primera igualdad tiene además el término $2\mathbf v_1\cdot\mathbf v_2$. Compararlas obliga a que el producto escalar sea cero. Como ambas velocidades son no nulas, forman un ángulo recto.

Escribimos $\mathbf v_1=a(\cos30^\circ,\sin30^\circ)$ con $a>0$. La condición $\mathbf v_1\cdot(\mathbf u-\mathbf v_1)=0$ da $4a\cos30^\circ-a^2=0$ en unidades coherentes; su raíz positiva es $a=2\sqrt3\,\mathrm{m/s}$. Luego

$$
\mathbf v_1=(3,\sqrt3)\,\mathrm{m/s},
\qquad
\mathbf v_2=(1,-\sqrt3)\,\mathrm{m/s}.
$$

La segunda rapidez vale $2\,\mathrm{m/s}$ y su dirección es $-60^\circ$. Sus cuadrados suman $12+4=16\,\mathrm{m^2/s^2}$ y los vectores suman $(4,0)\,\mathrm{m/s}$. Sin la dirección medida habría una familia de salidas; la perpendicularidad por sí sola no escogería la orientación del par.

### 16. Leer la altura de un péndulo balístico {#solucion-9-16}

La altura informa sobre el estado inmediatamente posterior al impacto. En la subida, incluimos la interacción gravitatoria y elegimos potencial cero abajo. La tensión ideal es perpendicular al movimiento y no realiza trabajo, por lo que

$$
\frac12(m+M)V^2=(m+M)gh,
\qquad V=\sqrt{2gh}=2\,\mathrm{m/s}.
$$

Retrocedemos al impacto, intervalo durante el cual la hipótesis de cuerdas casi verticales permite omitir su impulso horizontal. Para proyectil y bloque, $mu=(m+M)V$, de donde $u=(1/0{,}02)(2)\,\mathrm{m/s}=100\,\mathrm{m/s}$. El bloque no estaba moviéndose antes del choque.

La energía cinética anterior era $\tfrac12(0{,}02)(100)^2=100\,\mathrm J$; la inmediatamente posterior, $\tfrac12(1)(2)^2=2\,\mathrm J$. Se transformaron noventa y ocho joules en el impacto. Los dos joules restantes se convierten en energía potencial durante la subida. Igualar directamente los cien joules iniciales con la energía potencial final borraría la transformación principal y daría una rapidez incorrecta.

Con las cotas del segundo análisis conservamos el mismo orden de inferencia. La subida determina $V=\sqrt{2gh}$ y el impacto satisface $mu+J=(m+M)V$. Por tanto,

$$
u(h,J)=\frac{(m+M)\sqrt{2gh}-J}{m}.
$$

Esta expresión crece con $h>0$ y disminuye con $J$. Las masas suman un kilogramo y el intervalo exacto que resulta es

$$
\begin{aligned}
u_-&=\frac{(1\,\mathrm{kg})\sqrt{3{,}8}\,\mathrm{m/s}-0{,}01\,\mathrm{N\,s}}{0{,}02\,\mathrm{kg}},\\
u_+&=\frac{(1\,\mathrm{kg})\sqrt{4{,}2}\,\mathrm{m/s}+0{,}01\,\mathrm{N\,s}}{0{,}02\,\mathrm{kg}}.
\end{aligned}
$$

Por tanto, $u\in[u_-,u_+]\subset[96{,}96;102{,}97]\,\mathrm{m/s}$. La envolvente se redondeó hacia fuera. Para una misma altura, omitir el impulso cambia la rapidez inferida en $J/m$, cuyo módulo está acotado por $0{,}50\,\mathrm{m/s}$. La pequeña masa del proyectil amplifica ese efecto: la misma cota de impulso produciría sólo $0{,}01\,\mathrm{m/s}$ de error al predecir la velocidad común del conjunto. La tolerancia debe compararse con la magnitud que queremos reconstruir. Las cotas de altura e impulso contienen aquí toda la información declarada; asignarles probabilidades exigiría otro modelo.

### 17. Lo que ocurre en la máxima compresión {#solucion-9-17}

Durante el contacto conservamos el momento del conjunto y la suma de energía cinética y energía del resorte. La velocidad del centro de masa es $V=(1\cdot4+3\cdot0)/4=1\,\mathrm{m/s}$. En la máxima compresión la derivada de la separación es cero y ambas partículas tienen esa misma velocidad. Su energía cinética conjunta es entonces $K_{\rm cm}=\tfrac12(4)(1)^2=2\,\mathrm J$.

La energía cinética inicial era ocho joules. Por tanto, el resorte almacena seis joules y

$$
\frac12k\delta_{\max}^2=6\,\mathrm J,
\qquad
\delta_{\max}=\sqrt{\frac{12\,\mathrm J}{300\,\mathrm{N/m}}}
=0{,}20\,\mathrm m.
$$

Cuando recupera su longitud natural, devuelve esa energía y la interacción termina; el encuentro es elástico entre sus estados inicial y final. Las velocidades finales son $-2$ y $2\,\mathrm{m/s}$, como en el ejercicio 7. Detener la cuenta en la máxima compresión habría confundido un estado intermedio con el final. El valor de $k$ fija la compresión, pero no las velocidades de salida del modelo ideal.

### 18. Una discrepancia entre bandas {#solucion-9-18}

La velocidad predicha es la combinación creciente $V_0=(2u_1+u_2)/3$. Sus extremos se obtienen usando a la vez los extremos inferiores o superiores de ambas cotas:

$$
V_0\in\left[\frac{2(2{,}9)-0{,}1}{3},
\frac{2(3{,}1)+0{,}1}{3}\right]\,\mathrm{m/s}
=[1{,}9,2{,}1]\,\mathrm{m/s}.
$$

No hay intersección con la banda observada. La menor discrepancia es $2{,}15-2{,}1=0{,}05\,\mathrm{m/s}$; multiplicarla por la masa total da $J^{\rm ext}\geq0{,}15\,\mathrm{N\,s}$ hacia el sentido positivo. De hecho, al combinar las bandas se obtiene $J^{\rm ext}\in[0{,}15,0{,}87]\,\mathrm{N\,s}$ si todos sus extremos son admisibles independientemente.

La cota inferior es condicional: supone correctas las masas, las bandas y el enganche. La separación entre bandas detecta incompatibilidad con el paquete completo de hipótesis de impulso externo nulo; no demuestra por sí sola que el riel haya ejercido ese impulso.

### 19. Los extremos ocultan un cambio intermedio {#solucion-9-19}

Los impulsos de los dos tramos son $+2$ y $-2\,\mathrm{N\,s}$. Los momentos en los tres instantes son, respectivamente, cero, $2\,\mathrm{kg\,m/s}$ y cero. Durante el primer segundo la velocidad aumenta linealmente de cero a $2\,\mathrm{m/s}$, y durante el segundo disminuye hasta cero. Las áreas de los dos triángulos bajo la velocidad valen un metro cada una; el desplazamiento total es dos metros.

El trabajo neto es cero porque las energías cinéticas de los extremos coinciden. En el primer tramo se entregan dos joules y en el segundo se retiran dos. El momento tampoco fue constante, aunque sus extremos coincidan: tuvo una variación intermedia medible. El impulso nulo sobre todo el intervalo expresa un balance entre extremos; la conservación durante un intervalo exige constancia en todos sus instantes.

### 20. Todas las salidas que admite el balance {#solucion-9-20}

Escribamos $v_1=a\,\mathrm{m/s}$, con $a$ adimensional. La conservación fija $v_2=(6-2a)\,\mathrm{m/s}$. La energía cinética final es

$$
K_b=\big[a^2+\tfrac12(6-2a)^2\big]\,\mathrm J
=(3a^2-12a+18)\,\mathrm J.
$$

Exigir $K_b\leq9\,\mathrm J$ equivale a $(a-1)(a-3)\leq0$, por lo que $1\leq a\leq3$. Falta aplicar la condición de salida: el cuerpo 1 estaba detrás y los cuerpos ya no se acercan, así que $v_2-v_1\geq0$. Esto requiere $6-3a\geq0$ y restringe la familia a

$$
1\leq a\leq2,\qquad
(v_1,v_2)=(a,6-2a)\,\mathrm{m/s}.
$$

En $a=1$ salen a uno y cuatro metros por segundo y el choque es elástico. En $a=2$ comparten dos metros por segundo y la energía final es mínima. Los valores intermedios corresponden a restitución $e=(6-3a)/3=2-a$, entre cero y uno. El valor $a=3$, que conservaba energía en la cuenta algebraica, describe todavía acercamiento y no satisface la condición final del problema. Los datos permiten toda una familia física de salidas; medir la restitución o una velocidad final proporcionaría la información que falta.

## Lecturas de apoyo

La distinción entre datos, cotas y modelos se desarrolla desde [el capítulo 0, «El problema de medir»](00_La_medida_fisica.md). Las sumas de fuerzas y la identificación de sus agentes provienen de [«Fuerzas y leyes de Newton»](04_Fuerzas_y_leyes_de_Newton.md); los balances que permiten enlazar impacto, compresión y subida requieren [«Trabajo y energía cinética»](07_Trabajo_y_energia_cinetica.md) y [«Potencial, equilibrio y estabilidad»](08_Potencial_equilibrio_y_estabilidad.md). Se utilizan integrales por tramos, sumas vectoriales y productos escalares; la descomposición del movimiento relativo queda demostrada en el propio capítulo.

Como contraste de teoría y método se consultan Young y Freedman, *Sears y Zemansky. Física universitaria*, volumen 1, 13.ª edición (Pearson, 2013), capítulo 8, en particular §§8.1–8.5; Serway y Jewett, *Física para ciencias e ingeniería*, volumen 1, 10.ª edición española (Cengage, 2019), capítulo 9, particularmente §§9.3–9.6; y Spivak, *Physics for Mathematicians. Mechanics I* (2010), capítulo 3, discusión inicial de momento y centro de masa, pp. 80–81. El cotejo es selectivo y no reemplaza la lectura de esas obras. Los enunciados, datos, soluciones y figuras de este capítulo son desarrollos propios a partir de familias habituales de problemas.

---

[← 8. Potencial, equilibrio y estabilidad](fisica-para-matematicos-08-potencial-equilibrio-y-estabilidad.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [10. El oscilador armónico →](fisica-para-matematicos-10-el-oscilador-armonico.md)
