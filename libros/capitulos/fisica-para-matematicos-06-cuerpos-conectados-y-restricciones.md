---
title: "Cuerpos conectados y restricciones"
subtitle: "Física para matemáticos · Tomo I · Capítulo 6"
author: "A. Peña"
description: "Capítulo 6 de la edición revisada, con problemas y soluciones desarrolladas."
content-id: MA-BCH-0351
source-id: FISPM-r20261021-C06
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
edition: r20261021
canonical-edition: true
date-modified: 2026-10-21
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0350"]
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

[← 5. Contactos, tensiones y rozamiento](fisica-para-matematicos-05-contactos-tensiones-y-rozamiento.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [7. Trabajo y energía cinética →](fisica-para-matematicos-07-trabajo-y-energia-cinetica.md)

Una carga de seis kilogramos cuelga del eje de una polea móvil. Una cuerda tiene un extremo fijo al techo, baja alrededor de esa polea, vuelve a subir hasta una polea fija y termina en una pesa de dos kilogramos. Soltamos el conjunto desde el reposo. ¿Bajará la carga más pesada? ¿Cuánto avanzará la pesa mientras la carga desciende un metro?

La segunda pregunta puede resolverse antes de conocer las masas. Cuando la polea móvil baja, se alargan los dos ramales que la sostienen. Esa longitud tiene que salir del ramal de la pesa. Necesitamos contar cuánto cambia cada parte de la cuerda antes de relacionar las aceleraciones de sus extremos.

El laboratorio será nuestro marco inercial y tomaremos $g=10\,\mathrm{m/s^2}$. La cuerda es inextensible y de masa despreciable; las poleas tienen masa despreciable y funcionan sin pérdidas. Los tramos rectos permanecen verticales y los arcos de contacto conservan su longitud. La carga está unida al eje móvil por un enganche corto, rígido y de masa despreciable. Describiremos la traslación del conjunto móvil mediante la posición de la carga. Estas hipótesis excluyen el balanceo, la elasticidad y la inercia de rotación de las poleas.

![Una cuerda baja del anclaje A, rodea la polea móvil P, sube a la polea fija F y desciende hasta la pesa m.](/assets/books/fispm/r20261021/restriccion_polea_movil.svg){.fpm-v04-figure}

*Figura 6.1.* La carga $M$ acompaña al eje móvil. Las dos distancias verticales asociadas a ese eje aumentan cuando desciende. Las coordenadas de los cuerpos se miden hacia abajo desde un nivel fijo; las diferencias entre ejes, tangencias y enganches quedan absorbidas en constantes. El esquema representa conexiones y sentidos, sin escala de fuerzas.

## La longitud antes que las fuerzas

Escribamos $y$ para la coordenada de la carga y $z$ para la de la pesa, ambas positivas hacia abajo desde un nivel fijo. Cada uno de los ramales que llegan a la polea móvil aporta una longitud que crece en la misma cantidad que $y$. El ramal final crece como $z$. Las partes restantes suman una constante $c$. Si $L$ es la longitud total de la cuerda,

$$
2y+z+c=L.
$$

No necesitamos conocer $c$ para comparar dos configuraciones. Restar sus ecuaciones da $2\Delta y+\Delta z=0$. Por tanto, un descenso de un metro de la carga exige un ascenso de dos metros de la pesa, siempre que haya espacio suficiente para ambos movimientos.

Como la igualdad se cumple durante todo un intervalo de movimiento suave, podemos derivarla:

$$
2\dot y+\dot z=0,\qquad 2\ddot y+\ddot z=0.
$$

Si llamamos $a=\ddot y$, la aceleración de la pesa es $\ddot z=-2a$. El factor dos cuenta ramales cuya longitud cambia; no procede de que una masa sea el doble de otra. Las velocidades y las aceleraciones son componentes respecto de los ejes declarados. El signo negativo significa que sus componentes tienen sentidos contrarios.

La relación $\ddot z=-a$, válida para dos masas colgadas de una polea fija sencilla con estos mismos sentidos de coordenadas, describiría aquí otra máquina. Conservar la fórmula de una geometría anterior cambiaría el problema antes de empezar a resolverlo.

## Dos ramales sostienen la carga

En una misma cuerda ideal, guiada por poleas ideales, utilizamos una tensión de módulo $T$. Sobre la pesa actúan su peso $mg$ hacia abajo y una fuerza $T$ hacia arriba. Sobre el conjunto formado por la polea móvil, su enganche y la carga actúan $Mg$ hacia abajo y dos fuerzas $T$ hacia arriba. La masa del conjunto es $M$ por la idealización de sus accesorios. Las ecuaciones son

$$
Mg-2T=Ma,\qquad mg-T=m(-2a).
$$

De la segunda obtenemos $T=m(g+2a)$. Sustituir en la primera permite reunir los términos que contienen $a$:

$$
(M-2m)g=(M+4m)a.
$$

Así,

$$
a=\frac{M-2m}{M+4m}g,
\qquad \ddot z=-2\frac{M-2m}{M+4m}g,
\qquad T=\frac{3Mm}{M+4m}g.
$$

Con $M=6\,\mathrm{kg}$ y $m=2\,\mathrm{kg}$,

$$
a=\frac{10}{7}\,\mathrm{m/s^2},\qquad
\ddot z=-\frac{20}{7}\,\mathrm{m/s^2},\qquad
T=\frac{180}{7}\,\mathrm N.
$$

La carga desciende y la pesa sube con el doble de aceleración en módulo. La tensión es mayor que el peso de la pesa, $20\,\mathrm N$, como requiere su aceleración hacia arriba. Las dos fuerzas que sostienen el conjunto móvil suman $360/7\,\mathrm N$, menos que sus sesenta newtons de peso. Ambas comprobaciones dan el mismo sentido de movimiento.

![Diagramas separados para el conjunto móvil y la pesa, con dos tensiones sobre el primero y una sobre la segunda.](/assets/books/fispm/r20261021/restriccion_fuerzas.svg){.fpm-v04-figure}

*Figura 6.2.* Cada panel contiene fuerzas recibidas por su sistema. Las flechas son esquemáticas: la igualdad de los dos módulos $T$ corresponde a la cuerda ideal. La fuerza del enganche sobre la carga aislada sería $2T$; al incluir el enganche en el conjunto móvil, esa interacción es interna y no se agrega al diagrama.

Partiendo del reposo, los desplazamientos son

$$
y(t)-y(0)=\frac{5}{7}\,\mathrm{m/s^2}\,t^2,
\qquad z(t)-z(0)=-\frac{10}{7}\,\mathrm{m/s^2}\,t^2.
$$

Cuando la carga ha bajado un metro han transcurrido $\sqrt{7/5}\,\mathrm s$ y la pesa ha subido dos metros. El cálculo presupone que no alcanza antes una polea, el suelo o un tope. Una solución de ecuaciones puede continuar más allá de un choque; la historia física descrita por esas ecuaciones termina en el primer encuentro no incluido en el modelo.

## Posiciones que pueden coexistir

Dos coordenadas aparecen en el dibujo, pero sólo una puede elegirse libremente. Fijado $y$, la longitud determina $z=L-c-2y$. Las dos ecuaciones de Newton aportan información sobre cuerpos distintos; la restricción impide asignarles movimientos independientes.

**Definición.** Una *restricción de posición* es una relación entre las coordenadas y, eventualmente, el tiempo que deben satisfacer las configuraciones admitidas por un modelo. Una configuración es *admisible* si satisface esas relaciones y las condiciones geométricas de su régimen, como las separaciones entre superficies mayores o iguales que cero y la existencia de los ramales representados.

La igualdad de longitud no impone por sí sola todas esas condiciones. También debemos conservar el orden de los puntos que permitió escribir cada longitud como una diferencia de coordenadas. Un ramal que desaparece al llegar la pesa a una polea señala el límite de esta descripción.

**Definición.** En una región de configuraciones, unas *coordenadas independientes* son variables cuya elección determina las restantes de forma única y permite recorrer las configuraciones de esa región. Su número se llama aquí *número de grados de libertad*. El tiempo impuesto desde fuera actúa como parámetro de la descripción.

Para $2y+z=C$, con $C=L-c$ fijo, podemos escoger $y$ o $z$ como única coordenada independiente. No escogemos ambos a voluntad. Para dos partículas que se desplazan por rectas separadas y no están conectadas, en cambio, se necesitan dos coordenadas.

**Proposición.** Sean $y,z$ funciones dos veces continuamente derivables en un intervalo que contiene $t_0$. La igualdad $2y+z=C$ en todo el intervalo equivale a las tres condiciones

$$
2\ddot y+\ddot z=0,\qquad
2\dot y(t_0)+\dot z(t_0)=0,\qquad
2y(t_0)+z(t_0)=C.
$$

**Demostración.** La igualdad de posiciones produce las otras condiciones al derivar y evaluar en $t_0$. Para la dirección inversa, consideremos $h(t)=2y(t)+z(t)-C$. Su segunda derivada es cero, de modo que $h'$ es constante. La condición inicial de velocidades hace que esa constante sea cero. Entonces $h$ también es constante, y la condición inicial de posiciones fija su valor en cero. Por tanto, la igualdad original se conserva en todo el intervalo.

Resolver sólo la ecuación de aceleraciones conserva cualquier error inicial de posición y permite que un error inicial de velocidad crezca linealmente. Esos movimientos adicionales satisfacen una consecuencia de la restricción, pero no la restricción que queríamos imponer.

![Las configuraciones forman una recta en el plano de coordenadas; las velocidades compatibles siguen su dirección.](/assets/books/fispm/r20261021/restriccion_configuraciones.svg){.fpm-v04-figure}

*Figura 6.3.* Para el ejemplo geométrico $2y+z=8\,\mathrm m$, cada punto del segmento dibujado es una pareja admisible dentro del dominio $y,z\geq0$. Las velocidades compatibles son tangentes a la recta. Los extremos pueden corresponder a límites físicos que requieren información adicional del aparato.

La misma idea sirve para una relación lineal $b_1q_1+\cdots+b_nq_n=C(t)$, con coeficientes constantes: se deriva una o dos veces y se conservan los datos iniciales correspondientes. Si la geometría obliga a usar coeficientes variables, también hay que derivarlos. No toda restricción tiene la sencillez de una suma de longitudes verticales.

## Qué significa que una cuerda siga tensa

Las relaciones anteriores suponen que los tramos de la cuerda ocupan el recorrido representado. Una cuerda flexible puede tirar, pero no mantener ese recorrido empujando a sus extremos para separarlos.

**Definición.** Para un recorrido de longitud geométrica $\ell(q,t)$ y una cuerda inextensible de longitud $L$, llamaremos *holgura* a $s=L-\ell$. En el modelo de cuerda flexible que transmite tracción se exige

$$
s\geq0,\qquad T\geq0,\qquad sT=0.
$$

Aquí $\ell$ es la longitud que se necesitaría para unir los puntos siguiendo las guías indicadas, con los ramales rectos supuestos. Cuando hay holgura, la forma concreta de la cuerda queda fuera de esta descripción y $T=0$. En la configuración tensa, $s=0$, la fuerza puede ser positiva o alcanzar cero en un límite. Las igualdades de posición, velocidad y aceleración de la cuerda tensa sólo se utilizan mientras ese régimen sea compatible.

En el problema inicial, $M,m>0$ producen $T>0$. Los datos de reposo son compatibles y la evolución mantiene la longitud hasta un límite geométrico. Si un movimiento impuesto desde fuera exigiera $T<0$, tendríamos que abandonar la hipótesis de cuerda tensa y estudiar la separación o la holgura.

Una velocidad inicial incompatible tampoco se corrige simplemente borrando su componente inconveniente. Una cuerda que se tensa bruscamente puede provocar un cambio de velocidad, pero calcularlo requiere un modelo de impulso, elasticidad o choque. Las ecuaciones suaves de este capítulo no describen ese proceso.

## Una masa que se mueve y un extremo que alguien controla

Sustituyamos la pesa por una mano o un motor que impone la posición $z(t)$ del extremo libre. Sigue cumpliéndose $2y+z=C$, pero ya no existe una ecuación $mg-T=m\ddot z$ para una pesa. El movimiento impuesto suministra la información que antes aportaba esa ecuación de Newton.

Si el extremo tiene aceleración $\ddot z=-4\,\mathrm{m/s^2}$, la carga acelera hacia abajo a $2\,\mathrm{m/s^2}$. Para $M=5\,\mathrm{kg}$,

$$
Mg-2T=M\ddot y
\quad\Longrightarrow\quad
T=\frac{M}{2}(g-\ddot y)=20\,\mathrm N.
$$

El agente debe ejercer sobre la cuerda una fuerza de veinte newtons dirigida hacia abajo. Si el extremo parte del reposo y mantiene esa aceleración, sube mientras esa fuerza apunta hacia abajo. La aceleración fijada determina cómo cambia la velocidad; su sentido en un instante también depende de la velocidad inicial. El resultado describe un movimiento suave que parte de velocidades compatibles.

Si el agente intentara imponer $\ddot z=-24\,\mathrm{m/s^2}$, la restricción pediría $\ddot y=12\,\mathrm{m/s^2}$ y la ecuación de la carga daría $T=-5\,\mathrm N$. La cuerda no puede acelerar hacia abajo a la carga más que la gravedad cuando sólo puede tirar de ella hacia arriba. El movimiento impuesto dejaría holgura; no realizaría la historia tensa calculada.

También puede moverse el anclaje. Llamemos $u(t)$ a su coordenada hacia abajo y mantengamos fija la polea superior. Mientras el anclaje permanezca por encima de la polea móvil, uno de los ramales tiene longitud $y-u$ más una constante, el segundo crece como $y$ y el último como $z$. Ahora

$$
2y+z-u=C,\qquad 2\ddot y+\ddot z=\ddot u.
$$

Mover un punto que antes era fijo cambia la ecuación geométrica. La figura siguiente permite identificar qué longitud cambia con $u$ y comprobar su signo.

![El anclaje desciende y acorta únicamente el primer ramal de la polea móvil.](/assets/books/fispm/r20261021/restriccion_anclaje.svg){.fpm-v04-figure}

*Figura 6.4.* Con los tres ejes positivos hacia abajo, el ramal entre anclaje y polea móvil depende de $y-u$. El descenso del anclaje acorta ese tramo cuando la polea móvil permanece en su lugar. Los otros dos tramos no contienen $u$.

## Varias cuerdas: reconocer relaciones diferentes

Tres carros sobre una mesa sin rozamiento están unidos en fila por dos cuerdas horizontales tensas. Una fuerza $F$ tira del último carro. Si sus posiciones crecen hacia la derecha, las longitudes imponen $x_2-x_1=d_1$ y $x_3-x_2=d_2$. Al derivar, las tres aceleraciones coinciden. Eso no obliga a que las tensiones de las dos cuerdas sean iguales.

Para masas $m_1,m_2,m_3$ y tensiones $T_1$ entre los dos primeros carros y $T_2$ entre los dos últimos,

$$
T_1=m_1a,\qquad T_2-T_1=m_2a,\qquad F-T_2=m_3a.
$$

La suma da $a=F/(m_1+m_2+m_3)$. Entonces $T_1=m_1a$ y $T_2=(m_1+m_2)a$. La segunda cuerda acelera a los dos primeros carros, mientras que la primera sólo acelera al primero. La igualdad de tensión se refiere a una cuerda ideal continua bajo las hipótesis adecuadas; no se extiende a cuerdas distintas por estar en un mismo aparato.

![Tres carros unidos por dos cuerdas presentan aceleración común y tensiones distintas.](/assets/books/fispm/r20261021/restriccion_tres_carros.svg){.fpm-v04-figure}

*Figura 6.5.* Para $m_1=1\,\mathrm{kg}$, $m_2=2\,\mathrm{kg}$, $m_3=3\,\mathrm{kg}$ y $F=12\,\mathrm N$, resulta $a=2\,\mathrm{m/s^2}$, $T_1=2\,\mathrm N$ y $T_2=6\,\mathrm N$. Se muestran conexiones y fuerza aplicada; los diagramas de cada receptor se reconstruyen en las ecuaciones.

Contar restricciones requiere comprobar que aportan información distinta. Las ecuaciones $x+2y=C_1$ y $2x+4y=C_2$ describen una sola condición si $C_2=2C_1$. Si las constantes no guardan esa relación, no hay ninguna configuración que las cumpla a la vez. Dos ecuaciones escritas no garantizan dos reducciones independientes de las coordenadas.

## Cuando la geometría es curva

Una barra de longitud $\ell$ mantiene un extremo sobre un piso horizontal y el otro sobre una pared vertical. Si las distancias al rincón son $x>0$ e $y>0$, la geometría impone

$$
x^2+y^2=\ell^2.
$$

Aquí sólo describimos el movimiento de los extremos; no estamos deduciendo con fuerzas la caída de una barra real. Para eso habrá que estudiar su rotación. Derivar esta igualdad ya permite descubrir qué información cinemática exige la rigidez.

**Proposición.** Si $x,y$ son dos veces continuamente derivables y satisfacen $x^2+y^2=\ell^2$ con $\ell$ constante, entonces

$$
x\dot x+y\dot y=0,
\qquad
x\ddot x+y\ddot y+\dot x^2+\dot y^2=0.
$$

**Demostración.** La derivada de $x^2+y^2$ es $2x\dot x+2y\dot y$, mientras que la de $\ell^2$ es cero. Dividir por dos da la primera igualdad. Al derivarla, la regla del producto introduce $\dot x^2+x\ddot x$ y $\dot y^2+y\ddot y$, cuya suma debe ser cero. Esos términos cuadráticos son necesarios porque los coeficientes $x$ e $y$ también cambian durante el movimiento.

Cuando $y>0$, la primera relación permite despejar $\dot y=-x\dot x/y$. La segunda da

$$
\ddot y=-\frac{x\ddot x+\dot x^2+\dot y^2}{y}.
$$

Para $\ell=5\,\mathrm m$, $x=3\,\mathrm m$, $y=4\,\mathrm m$, $\dot x=1\,\mathrm{m/s}$ y $\ddot x=0$, resulta

$$
\dot y=-\frac34\,\mathrm{m/s},\qquad
\ddot y=-\frac{25}{64}\,\mathrm{m/s^2}.
$$

El extremo horizontal conserva su rapidez, pero el vertical acelera. La geometría cambia la proporción entre sus desplazamientos. Igualar los módulos de sus aceleraciones contradiría la longitud de la barra.

![Barra entre pared y piso y curva de configuraciones admisibles en el primer cuadrante.](/assets/books/fispm/r20261021/restriccion_barra.svg){.fpm-v04-figure}

*Figura 6.6.* En este dibujo $y$ crece hacia arriba y $x$ hacia la derecha: son las distancias positivas al rincón. La curva $x^2+y^2=\ell^2$ permite leer cómo cambia la razón entre velocidades. Estas coordenadas no son las coordenadas hacia abajo de la polea inicial.

Para una partícula unida a un pivote fijo por una cuerda tensa de longitud $\ell$, el vector posición relativo $\mathbf r$ satisface $\mathbf r\cdot\mathbf r=\ell^2$. Las mismas derivaciones dan $\mathbf r\cdot\mathbf v=0$ y $\mathbf r\cdot\mathbf a=-\|\mathbf v\|^2$. La componente de aceleración dirigida hacia el pivote es, por tanto, $v^2/\ell$. La aceleración puede tener además una componente tangencial. Esta conclusión combina la geometría del círculo del capítulo 3 con la necesidad de una fuerza radial del capítulo 4; no supone rapidez constante.

En el punto más bajo de un círculo vertical, el peso apunta alejándose del centro y la tensión hacia él. Así, $T-mg=mv^2/\ell$. En el punto más alto, ambos apuntan hacia el centro y $T+mg=mv^2/\ell$. Un valor negativo de esta última tensión rechaza el círculo tenso para esos datos. No calcula la trayectoria posterior de la cuerda floja.

![En los puntos inferior y superior de un círculo vertical cambian la dirección del peso respecto del centro y el valor admisible de la tensión.](/assets/books/fispm/r20261021/restriccion_circulo.svg){.fpm-v04-figure}

*Figura 6.7.* Las fuerzas se dibujan sobre la partícula, y las flechas radiales auxiliares indican hacia dónde queda el centro. El dato de rapidez se refiere al instante considerado; no se presupone que dos estados mostrados pertenezcan a la misma trayectoria.

## Qué aprendemos del aparato

En la polea móvil, la geometría fijó la razón entre movimientos y las ecuaciones de Newton determinaron la aceleración y la tensión. Medir una razón de desplazamientos cercana a dos pone a prueba la descripción del recorrido; por sí sola no identifica las masas ni mide la tensión. Con masas diferentes, el mismo aparato ideal conserva esa razón y cambia su aceleración.

También hay una diferencia entre preparar el sistema en reposo y encontrar aceleración nula. La expresión obtenida da $a=0$ cuando $M=2m$. Si las velocidades iniciales compatibles no son cero, los cuerpos continúan moviéndose uniformemente mientras el recorrido lo permita. El equilibrio de fuerzas no borra el movimiento anterior.

Cuando tengamos varias conexiones, convendrá volver a las longitudes que realmente cambian, elegir coordenadas que podamos interpretar y distinguir las fuerzas que recibe cada cuerpo. La derivación de una restricción añade relaciones entre movimientos; no reemplaza las leyes de interacción ni garantiza por sí sola que el régimen pueda sostenerse. Los ejercicios siguientes alternan esas decisiones para que la misma fórmula no oculte preguntas físicas distintas.

## Ejercicios

En todos los problemas se usa $g=10\,\mathrm{m/s^2}$. Las cuerdas y poleas son ideales, salvo indicación contraria, y los movimientos se estudian antes de cualquier choque o desaparición de un ramal. La «polea móvil inicial» designa exactamente el aparato de la figura 6.1; $y,z$ crecen hacia abajo. Las condiciones iniciales de posición se suponen compatibles cuando no se discuten expresamente.

### 1. Contar lo que cambia {#ejercicio-6-1}

En la polea móvil inicial, la carga desciende $0{,}30\,\mathrm m$. Determine el desplazamiento de la pesa. Si en un instante $\dot y=0{,}40\,\mathrm{m/s}$ y $\ddot y=-0{,}20\,\mathrm{m/s^2}$, encuentre $\dot z$ y $\ddot z$. ¿En qué sentido se mueve y se acelera cada cuerpo?

### 2. Cambiar las masas {#ejercicio-6-2}

Resuelva la polea móvil inicial con $M=4\,\mathrm{kg}$ y $m=1\,\mathrm{kg}$, soltada desde el reposo. Obtenga ambas aceleraciones, la tensión y la fuerza del enganche sobre la carga aislada. Compruebe el signo de cada fuerza neta.

### 3. Fuerzas equilibradas, cuerpos en marcha {#ejercicio-6-3}

La carga tiene $M=8\,\mathrm{kg}$. Elija $m$ para que las aceleraciones sean nulas. Calcule $T$. Si inicialmente $\dot y=0{,}25\,\mathrm{m/s}$, determine $\dot z$ y los desplazamientos durante dos segundos. Explique qué cambiaría al preparar los cuerpos en reposo.

### 4. El primer límite del recorrido {#ejercicio-6-4}

En el aparato inicial con $M=6\,\mathrm{kg}$ y $m=2\,\mathrm{kg}$, se parte con $\dot y(0)=1\,\mathrm{m/s}$ y velocidad compatible de la pesa. La pesa dispone de dos metros de ascenso antes de tocar la polea fija y la carga puede bajar al menos tres metros sin encontrar obstáculos. ¿Cuándo termina este tramo del modelo? Calcule las velocidades justo antes de ese instante.

### 5. Una respuesta que describe otra máquina {#ejercicio-6-5}

Para $M=6\,\mathrm{kg}$ y $m=2\,\mathrm{kg}$, una solución usa $Mg-2T=Ma$ y $mg-T=-ma$. Obtiene $a=2\,\mathrm{m/s^2}$ y $T=24\,\mathrm N$. Compruebe ese álgebra y localice el error físico. ¿Qué velocidad de cambio de longitud produciría al cabo de un segundo desde el reposo?

### 6. Datos iniciales incompatibles {#ejercicio-6-6}

En una configuración tensa admisible se prescribe $\dot y(0)=1\,\mathrm{m/s}$ y $\dot z(0)=-1\,\mathrm{m/s}$. Demuestre que no hay un movimiento suave de cuerda tensa con esos datos. Si después se utiliza $2\ddot y+\ddot z=0$, ¿cómo evoluciona el error de longitud? ¿Puede corregirse el problema sin añadir información física?

### 7. Un motor en el extremo {#ejercicio-6-7}

Una carga de cinco kilogramos ocupa el lugar de $M$ y el extremo libre se acciona con un motor. Compare los movimientos impuestos $\ddot z=-4\,\mathrm{m/s^2}$ y $\ddot z=-24\,\mathrm{m/s^2}$, iniciados con velocidades compatibles. Calcule la tensión que pediría cada régimen tenso. En el segundo caso, compruebe por aceleraciones si empieza a aparecer holgura desde el reposo.

### 8. El anclaje también se mueve {#ejercicio-6-8}

En la figura 6.4, el extremo $z$ permanece fijo y el anclaje tiene aceleración $\ddot u=3\,\mathrm{m/s^2}$ hacia abajo. Para $M=4\,\mathrm{kg}$, determine la aceleración de la carga y la tensión. Las velocidades iniciales son cero. Compruebe qué pasa con las longitudes de los tres ramales durante un intervalo corto.

### 9. Antes de elegir rozamiento cinético {#ejercicio-6-9}

Un bloque de cuatro kilogramos sobre un plano con $\sin\theta=3/5$ y $\cos\theta=4/5$ está conectado por una cuerda sobre una polea fija a una masa colgante $h$. El ramal del bloque es paralelo al plano. Se suelta desde el reposo; $\mu_s=0{,}20$ y $\mu_k=0{,}10$. Determine si se mueve para $h=3\,\mathrm{kg}$ y para $h=4\,\mathrm{kg}$. Cuando se mueva, calcule aceleración y tensión. Deduzca la relación de movimiento desde las longitudes.

### 10. Dos cuerdas entre tres carros {#ejercicio-6-10}

Resuelva el sistema de la figura 6.5. Escriba primero las restricciones y después las ecuaciones de cada carro. Calcule las tensiones. Compruebe $T_2$ usando como sistema los dos primeros carros juntos.

### 11. Cambiar el lugar del tirón {#ejercicio-6-11}

Los mismos carros del ejercicio 10 se mantienen en el orden $1,2,3$, pero ahora una fuerza de doce newtons tira del carro 1 hacia la izquierda. Parten del reposo con cuerdas tensas. Determine aceleración y tensiones usando un eje positivo hacia la derecha. ¿Por qué los resultados de tensión no coinciden con los del tirón sobre el carro 3?

### 12. El soporte que sostiene todo el aparato {#ejercicio-6-12}

En el problema inicial, el mismo techo sostiene el anclaje y el eje de la polea fija. Desprecie las masas de ambas poleas y sus accesorios. Calcule la fuerza vertical total que la cuerda transmite al techo. Compruebe que el peso total de los dos cuerpos menos esa fuerza coincide con $M\ddot y+m\ddot z$. ¿Por qué no coincide con $(M+m)\ddot y$?

### 13. Dos ecuaciones que pueden ser una {#ejercicio-6-13}

Se proponen las restricciones $x+2y=6\,\mathrm m$ y $2x+4y=12\,\mathrm m$. Determine las coordenadas independientes y parametrice las configuraciones con $x,y>0$. Repita si la segunda constante se cambia a trece metros. Explique por qué no basta contar ecuaciones.

### 14. Una barra con un extremo controlado {#ejercicio-6-14}

Una barra de diez metros mantiene sus extremos en pared y piso. En un instante $x=6\,\mathrm m$, $y=8\,\mathrm m$ y el extremo del piso se aleja del rincón con rapidez constante de dos metros por segundo. Calcule la velocidad y la aceleración del extremo de la pared. Delimite el intervalo futuro de esta descripción geométrica si se conserva esa rapidez. No se pide un análisis dinámico de la barra.

### 15. Olvidar un término de la derivada {#ejercicio-6-15}

En la barra de cinco metros del texto, alguien deriva $x\dot x+y\dot y=0$ como $x\ddot x+y\ddot y=0$ y concluye $\ddot y=0$ cuando $\ddot x=0$. Explique el error y calcule el valor de $x\ddot x+y\ddot y$ en el estado $x=3\,\mathrm m$, $y=4\,\mathrm m$, $\dot x=1\,\mathrm{m/s}$. Incluya unidades.

### 16. La tensión en dos puntos del círculo {#ejercicio-6-16}

Una partícula de dos kilogramos está unida a un pivote fijo por una cuerda de dos metros. Estudie por separado un estado en el punto inferior y otro en el punto superior de un círculo vertical, ambos con rapidez de tres metros por segundo. Calcule la tensión requerida y decida la admisibilidad de cada estado tenso. Obtenga la rapidez mínima admisible en el punto superior y explique el alcance del caso de igualdad.

### 17. Una restricción que depende del reloj {#ejercicio-6-17}

Un mecanismo impone $x+2y=\ell_0+ct^2$, donde $\ell_0$ es una longitud y $c=1\,\mathrm{m/s^2}$. Además prescribe $x(t)=x_0+(2\,\mathrm{m/s})t$. Determine $y(t)$, sus datos iniciales y su aceleración. Pruebe qué datos iniciales hacen que la ecuación $\ddot x+2\ddot y=2c$ conserve la restricción original.

### 18. Poner a prueba la razón de desplazamientos {#ejercicio-6-18}

En dos configuraciones del aparato inicial se mide un descenso de la carga $\Delta y\in[0{,}198;0{,}202]\,\mathrm m$ y un ascenso de la pesa de módulo $h\in[0{,}397;0{,}403]\,\mathrm m$. Trate los intervalos como cotas deterministas independientes. Acote el residuo $R=2\Delta y-h$ y determine si los datos contradicen la relación de cuerda inextensible. ¿Demuestran que el modelo es exacto? ¿Identifican las masas?

### 19. Recuperar una masa a partir de la aceleración {#ejercicio-6-19}

Se conoce $m=2\,\mathrm{kg}$ y se mide $\ddot y=2\,\mathrm{m/s^2}$ en la polea móvil inicial. Suponiendo válidos los modelos ideales y el valor de $g$, determine $M$, la tensión y la aceleración de la pesa. Compruebe ambas ecuaciones de Newton. ¿Se podría obtener $M$ midiendo sólo la razón $\Delta z/\Delta y$? Si la aceleración de la carga sólo está acotada por $a\in[1{,}9,2{,}1]\,\mathrm{m/s^2}$, manteniendo exactos los demás datos dentro del problema, obtenga una envolvente para $M$.

### 20. Repartir el movimiento sin resolver fuerzas {#ejercicio-6-20}

Una cuerda pasa por una polea de centro $P$ que se mueve verticalmente; sus dos extremos cuelgan hacia abajo y tienen coordenadas $y_1,y_2$. Los ramales permanecen verticales, los extremos están por debajo de $P$ y todas las coordenadas crecen hacia abajo. La longitud de la cuerda impone $y_1+y_2-2y_P=C$. Si $\ddot y_P=1\,\mathrm{m/s^2}$, ¿quedan determinadas las aceleraciones de los extremos? Compare las parejas $(\ddot y_1,\ddot y_2)=(0,2)$ y $(1,1)$ en unidades SI. Suponga además que la polea tiene masa despreciable y una segunda cuerda tira de su eje hacia arriba con tensión $S$: deduzca su relación con la tensión $T$ de la cuerda inferior. Explique qué información falta para resolver un aparato completo.

## Soluciones

### 1. Contar lo que cambia {#solucion-6-1}

Al descender la carga treinta centímetros, cada ramal de apoyo gana esa longitud. El ramal final debe perder sesenta centímetros: $\Delta z=-0{,}60\,\mathrm m$. Derivando la misma igualdad obtenemos $\dot z=-0{,}80\,\mathrm{m/s}$ y $\ddot z=+0{,}40\,\mathrm{m/s^2}$. La carga baja, pero acelera hacia arriba; está reduciendo su rapidez en ese instante. La pesa sube y acelera hacia abajo, también reduciendo su rapidez. No hemos deducido masas ni tensiones de estos datos cinemáticos.

### 2. Cambiar las masas {#solucion-6-2}

La longitud conserva $\ddot z=-2a$. La pesa exige $T=(1\,\mathrm{kg})(10\,\mathrm{m/s^2}+2a)$ y el conjunto móvil satisface $40\,\mathrm N-2T=(4\,\mathrm{kg})a$. Sustituir da $20\,\mathrm N=(8\,\mathrm{kg})a$, de donde $a=2{,}5\,\mathrm{m/s^2}$, $\ddot z=-5\,\mathrm{m/s^2}$ y $T=15\,\mathrm N$.

El enganche transmite treinta newtons hacia arriba a la carga aislada, porque sobre la polea móvil sin masa las dos tensiones deben equilibrar la fuerza hacia abajo del enganche. La carga recibe una fuerza neta de diez newtons hacia abajo; la pesa recibe cinco hacia arriba. Sus cocientes por cuatro y por un kilogramo reproducen las aceleraciones. Todas las tensiones son positivas.

### 3. Fuerzas equilibradas, cuerpos en marcha {#solucion-6-3}

Para que $a=0$, el numerador $M-2m$ debe anularse, así que $m=4\,\mathrm{kg}$. La pesa requiere $T=mg=40\,\mathrm N$ y la carga recibe $2T=80\,\mathrm N$, igual a su peso.

La compatibilidad da $\dot z=-0{,}50\,\mathrm{m/s}$. Como las aceleraciones son nulas, los desplazamientos durante dos segundos son $\Delta y=0{,}50\,\mathrm m$ y $\Delta z=-1\,\mathrm m$. Las fuerzas equilibradas conservan esas velocidades. Si se preparan ambos cuerpos en reposo, las mismas fuerzas conservan el reposo. Se necesita espacio para el primer experimento; los equilibrios de fuerza no eliminan los límites del recorrido.

### 4. El primer límite del recorrido {#solucion-6-4}

Las masas fijan $a=10/7\,\mathrm{m/s^2}$ y la compatibilidad inicial impone $\dot z(0)=-2\,\mathrm{m/s}$. En cuanto la pesa suba dos metros, la carga habrá descendido uno, mucho antes de agotar sus tres metros disponibles. El tiempo satisface

$$
(1\,\mathrm{m/s})t+\frac57\,\mathrm{m/s^2}\,t^2=1\,\mathrm m.
$$

Al escribir $\tau=t/(1\,\mathrm s)$, la raíz positiva es $\tau=(-7+\sqrt{189})/10\approx0{,}675$. Justo antes del encuentro, $\dot y=\sqrt{189}/7\,\mathrm{m/s}\approx1{,}964\,\mathrm{m/s}$ y $\dot z=-2\sqrt{189}/7\,\mathrm{m/s}\approx-3{,}928\,\mathrm{m/s}$. La raíz negativa no pertenece a la evolución futura. No prolongamos estas expresiones a través del choque de la pesa con la polea.

### 5. Una respuesta que describe otra máquina {#solucion-6-5}

Las ecuaciones propuestas dan $T=20\,\mathrm N+(2\,\mathrm{kg})a$ y luego $20\,\mathrm N=(10\,\mathrm{kg})a$. Los números $a=2\,\mathrm{m/s^2}$ y $T=24\,\mathrm N$ satisfacen ese sistema algebraico. El fallo consiste en asignar $\ddot z=-a$ a la pesa, aunque los dos ramales móviles exigen $\ddot z=-2a$.

Con las aceleraciones equivocadas y reposo inicial, al segundo las velocidades serían $\dot y=2\,\mathrm{m/s}$ y $\dot z=-2\,\mathrm{m/s}$. La longitud modelada cambiaría a razón de $2\dot y+\dot z=2\,\mathrm{m/s}$. Además habría aumentado un metro desde el inicio: $2\Delta y+\Delta z=1\,\mathrm m$. Una cuerda inextensible no puede realizar esa evolución. Comprobar sólo las ecuaciones de fuerza no habría detectado el cambio de geometría.

### 6. Datos iniciales incompatibles {#solucion-6-6}

La derivada de la restricción exige $2\dot y(0)+\dot z(0)=0$, pero los datos dan $1\,\mathrm{m/s}$. Por ello no existe la evolución suave tensa solicitada. Si se resuelve después la condición de aceleraciones, el residuo $h=2y+z-C$ tiene $h''=0$, $h(0)=0$ y $h'(0)=1\,\mathrm{m/s}$. Resulta $h(t)=(1\,\mathrm{m/s})t$.

El signo positivo pide una longitud mayor que la disponible inmediatamente después del inicio; no describe una holgura que lo vuelva aceptable. Cambiar las velocidades iniciales, permitir extensión o estudiar un tirón impulsivo son problemas físicos diferentes. Sin especificar cuál ocurre, no hay una corrección determinada por los datos originales.

### 7. Un motor en el extremo {#solucion-6-7}

En el primer caso, $\ddot y=-\ddot z/2=2\,\mathrm{m/s^2}$ y $T=M(g-\ddot y)/2=20\,\mathrm N$. La tensión positiva admite el régimen. En el segundo, la geometría tensa pediría $\ddot y=12\,\mathrm{m/s^2}$ y $T=-5\,\mathrm N$, que la cuerda no puede ejercer.

Para comprobar el comienzo de la holgura, partamos de reposo en la configuración tensa. Al quedar sin tirón la carga cae con $\ddot y=g=10\,\mathrm{m/s^2}$, mientras el motor impone $\ddot z=-24\,\mathrm{m/s^2}$. La longitud requerida tiene $\ddot\ell=2\ddot y+\ddot z=-4\,\mathrm{m/s^2}$. Por tanto, la holgura cumple $\ddot s=+4\,\mathrm{m/s^2}$ y empieza como $s=(2\,\mathrm{m/s^2})t^2>0$. Esta comprobación es local: tras perder tensión no seguimos afirmando que la cuerda tenga la forma recta dibujada.

### 8. El anclaje también se mueve {#solucion-6-8}

El extremo fijo cumple $\ddot z=0$, por lo que $2\ddot y=\ddot u$ y $\ddot y=1{,}5\,\mathrm{m/s^2}$ hacia abajo. La ecuación $40\,\mathrm N-2T=(4\,\mathrm{kg})(1{,}5\,\mathrm{m/s^2})$ da $T=17\,\mathrm N$.

Desde el reposo, $\Delta u=(1{,}5\,\mathrm{m/s^2})t^2$ y $\Delta y=(0{,}75\,\mathrm{m/s^2})t^2$. El primer ramal cambia como $\Delta y-\Delta u=-(0{,}75\,\mathrm{m/s^2})t^2$; el segundo aumenta en la cantidad contraria y el tercero no cambia. La suma es cero. La respuesta requiere que el anclaje siga por encima de la polea móvil y que los dispositivos externos sostengan las fuerzas calculadas.

### 9. Antes de elegir rozamiento cinético {#solucion-6-9}

Tomemos $x$ hacia arriba del plano e $y$ hacia abajo para la masa colgante. El primer ramal pierde longitud cuando aumenta $x$ y el segundo la gana cuando aumenta $y$; así, $-x+y=C$ y $\ddot x=\ddot y=a$. La normal del bloque es $N=(4\,\mathrm{kg})g\cos\theta=32\,\mathrm N$. Su peso paralelo al plano vale $24\,\mathrm N$ hacia abajo y la fricción estática admite hasta $6{,}4\,\mathrm N$.

Para $h=3\,\mathrm{kg}$, el reposo de la pesa pide $T=30\,\mathrm N$. El bloque requiere fricción de seis newtons hacia abajo del plano, inferior al límite. La preparación de reposo se mantiene según la convención del capítulo 5: $a=0$ y $T=30\,\mathrm N$.

Para $h=4\,\mathrm{kg}$, el reposo pediría dieciséis newtons de fricción, imposibles. La pesa empieza a bajar y el bloque a subir; la fricción cinética sobre el bloque es $3{,}2\,\mathrm N$ hacia abajo del plano. Las ecuaciones son $T-24\,\mathrm N-3{,}2\,\mathrm N=(4\,\mathrm{kg})a$ y $40\,\mathrm N-T=(4\,\mathrm{kg})a$. Sumarlas da $a=1{,}6\,\mathrm{m/s^2}$ y sustituir en la pesa da $T=33{,}6\,\mathrm N$. El signo confirma el deslizamiento supuesto. Usar desde el inicio $\mu_kN$ en el primer ensayo habría inventado movimiento.

### 10. Dos cuerdas entre tres carros {#solucion-6-10}

Las restricciones $x_2-x_1=d_1$ y $x_3-x_2=d_2$ conservan distancias, de modo que las tres aceleraciones son $a$. Las ecuaciones respectivas son $T_1=(1\,\mathrm{kg})a$, $T_2-T_1=(2\,\mathrm{kg})a$ y $12\,\mathrm N-T_2=(3\,\mathrm{kg})a$. Su suma produce $a=2\,\mathrm{m/s^2}$. Entonces $T_1=2\,\mathrm N$ y $T_2=6\,\mathrm N$.

Al reunir los dos primeros carros, $T_1$ y su reacción son internas y se cancelan. La única fuerza horizontal externa sobre ese conjunto es $T_2$, que debe acelerar tres kilogramos a dos metros por segundo cuadrado: seis newtons. Las dos cuerdas siguen tensas. La tensión mayor corresponde a la cuerda que arrastra más masa en esta preparación.

### 11. Cambiar el lugar del tirón {#solucion-6-11}

Las distancias siguen constantes, por lo que la aceleración común tiene ahora valor $a=-2\,\mathrm{m/s^2}$. Con el eje positivo hacia la derecha, las ecuaciones de los carros son

$$
-12\,\mathrm N+T_1=(1\,\mathrm{kg})a,\qquad
-T_1+T_2=(2\,\mathrm{kg})a,\qquad
-T_2=(3\,\mathrm{kg})a.
$$

Se obtiene $T_2=6\,\mathrm N$ y $T_1=10\,\mathrm N$. La primera cuerda arrastra ahora los carros 2 y 3, de masa conjunta cinco kilogramos. La segunda arrastra sólo el carro 3. La masa total fija el mismo módulo de aceleración bajo el mismo módulo de fuerza, pero el reparto de fuerzas internas depende del lugar donde se tira. Ambas tensiones siguen siendo positivas; el signo negativo de $a$ no convierte una tensión en compresión.

### 12. El soporte que sostiene todo el aparato {#solucion-6-12}

La cuerda tira del anclaje hacia abajo con módulo $T$. Sobre la polea fija actúan dos ramales verticales que tiran hacia abajo con módulo total $2T$. Al despreciar el peso de los accesorios, la carga vertical transmitida al techo es $3T=540/7\,\mathrm N$.

Los cuerpos pesan ochenta newtons y la diferencia es $80-540/7=20/7\,\mathrm N$ hacia abajo. Por otra parte,

$$
M\ddot y+m\ddot z
=(6\,\mathrm{kg})\frac{10}{7}\,\mathrm{m/s^2}
-(2\,\mathrm{kg})\frac{20}{7}\,\mathrm{m/s^2}
=\frac{20}{7}\,\mathrm N.
$$

Podemos sumar las componentes verticales porque comparten dirección y sentido de referencia. No podemos reemplazar esa suma por $(M+m)\ddot y$: las dos masas no tienen una aceleración común. La restricción produce una razón entre aceleraciones, no la traslación rígida de ambos cuerpos.

### 13. Dos ecuaciones que pueden ser una {#solucion-6-13}

La segunda igualdad inicial es el doble de la primera y no agrega información. Podemos elegir $y=q$ y escribir $x=6\,\mathrm m-2q$, con $0<q<3\,\mathrm m$. Hay una coordenada independiente. También podríamos escoger $x$, con el intervalo correspondiente.

Si la segunda constante fuera trece metros, duplicar la primera igualdad exigiría simultáneamente $2x+4y=12\,\mathrm m$ y $2x+4y=13\,\mathrm m$. No hay configuraciones admisibles. No es un mecanismo con menos grados de libertad: es una especificación incompatible. La eliminación de variables distingue una repetición de una condición nueva y de una contradicción.

### 14. Una barra con un extremo controlado {#solucion-6-14}

La condición de velocidades da $\dot y=-x\dot x/y=-1{,}5\,\mathrm{m/s}$. El extremo superior baja. Como $\ddot x=0$, la segunda derivada de la longitud exige

$$
\ddot y=-\frac{(2\,\mathrm{m/s})^2+(-1{,}5\,\mathrm{m/s})^2}{8\,\mathrm m}
=-\frac{25}{32}\,\mathrm{m/s^2}.
$$

Si el instante dado se llama $t=0$, entonces $x=6\,\mathrm m+(2\,\mathrm{m/s})t$ y $y=\sqrt{(10\,\mathrm m)^2-x^2}$. El intervalo futuro regular es $0\leq t<2\,\mathrm s$. Cuando $t$ tiende a dos segundos, $y$ tiende a cero y el módulo de $\dot y$ diverge. No puede prolongarse esta prescripción suave con rapidez horizontal constante a través de ese extremo. Tampoco hemos probado que un conjunto de fuerzas reales pueda sostenerla hasta allí: es un análisis de compatibilidad geométrica.

### 15. Olvidar un término de la derivada {#solucion-6-15}

La derivada de $x\dot x$ contiene $\dot x^2$ además de $x\ddot x$; análogamente ocurre con $y\dot y$. En el estado dado, $\dot y=-3/4\,\mathrm{m/s}$, así que

$$
x\ddot x+y\ddot y
=-(\dot x^2+\dot y^2)
=-\frac{25}{16}\,\mathrm{m^2/s^2}.
$$

Como $\ddot x=0$ e $y=4\,\mathrm m$, resulta $\ddot y=-25/64\,\mathrm{m/s^2}$. El término no es una fuerza ni una aceleración por sí solo: sus unidades son longitud por aceleración, iguales a las de una rapidez al cuadrado. La regla del producto conserva esa correspondencia dimensional y la curvatura de la configuración.

### 16. La tensión en dos puntos del círculo {#solucion-6-16}

La aceleración hacia el centro tiene módulo $v^2/\ell=4{,}5\,\mathrm{m/s^2}$. Abajo, $T-20\,\mathrm N=(2\,\mathrm{kg})(4{,}5\,\mathrm{m/s^2})$, de donde $T=29\,\mathrm N$, admisible. Arriba, $T+20\,\mathrm N=9\,\mathrm N$ exigiría $T=-11\,\mathrm N$. Ese estado no admite una cuerda tensa que mantenga el círculo.

La desigualdad $T=m(v^2/\ell-g)\geq0$ pide $v\geq\sqrt{g\ell}=\sqrt{20}\,\mathrm{m/s}$. La igualdad produce $T=0$ en ese instante. Es una condición límite instantánea; para decidir la continuación hay que examinar las ecuaciones y los datos alrededor del punto. Tampoco relacionamos las dos rapideces propuestas mediante una ley de conservación: los estados se plantearon como experimentos separados.

### 17. Una restricción que depende del reloj {#solucion-6-17}

Despejar la posición evita perder constantes:

$$
y(t)=\frac{\ell_0-x_0}{2}-(1\,\mathrm{m/s})t+\frac{c}{2}t^2.
$$

Por tanto, $y(0)=(\ell_0-x_0)/2$, $\dot y(0)=-1\,\mathrm{m/s}$ y $\ddot y=c=1\,\mathrm{m/s^2}$. Al principio $y$ disminuye y luego invierte ese movimiento si la geometría del mecanismo sigue permitiéndolo.

Para probar la conservación en general, definimos $h=x+2y-\ell_0-ct^2$. La ecuación de aceleraciones implica $h''=0$, de donde $h(t)=h(0)+h'(0)t$. Recuperamos la igualdad original exactamente cuando $x(0)+2y(0)=\ell_0$ y $\dot x(0)+2\dot y(0)=0$. En otro instante inicial $t_0$ la segunda condición sería $\dot x(t_0)+2\dot y(t_0)=2ct_0$. El reloj del mecanismo forma parte de la restricción.

### 18. Poner a prueba la razón de desplazamientos {#solucion-6-18}

La cota inferior del residuo usa el menor descenso y el mayor ascenso; la superior usa los extremos contrarios:

$$
R\in[2(0{,}198)-0{,}403;\ 2(0{,}202)-0{,}397]\,\mathrm m
=[-0{,}007;0{,}007]\,\mathrm m.
$$

El intervalo contiene cero. Hay parejas de valores dentro de las cotas que satisfacen exactamente la relación ideal, de modo que las mediciones no la contradicen con esa resolución y esas hipótesis de error. No demuestran inextensibilidad exacta: también caben pequeñas desviaciones, errores de alineación u otros modelos compatibles. Una razón geométrica no identifica las masas. Harían falta observaciones dinámicas y un modelo de fuerzas para esa inferencia.

### 19. Recuperar una masa a partir de la aceleración {#solucion-6-19}

La ecuación de la pesa da inmediatamente $T=m(g+2a)=(2\,\mathrm{kg})(14\,\mathrm{m/s^2})=28\,\mathrm N$. En la carga, $M(g-a)=2T$, por lo que $M=56\,\mathrm N/(8\,\mathrm{m/s^2})=7\,\mathrm{kg}$. La aceleración de la pesa es $-4\,\mathrm{m/s^2}$.

Las comprobaciones son $70\,\mathrm N-56\,\mathrm N=14\,\mathrm N=(7\,\mathrm{kg})(2\,\mathrm{m/s^2})$ y $20\,\mathrm N-28\,\mathrm N=-8\,\mathrm N=(2\,\mathrm{kg})(-4\,\mathrm{m/s^2})$. La tensión es positiva. La razón $\Delta z/\Delta y=-2$, cuando el denominador no es cero, se conserva para cualquier par de masas positivas de esta máquina ideal; por ello no puede seleccionar los siete kilogramos. La inferencia depende además del valor supuesto de $g$ y de la ausencia de efectos no modelados.

Para propagar una cota de aceleración conviene conservar la inferencia en forma simbólica. Sustituir $T=m(g+2a)$ en la ecuación de la carga da

$$
M(a)=\frac{2m(g+2a)}{g-a}.
$$

Las masas positivas de esta máquina permiten $-g/2<a<g$. En efecto, esos signos hacen positivos tanto el numerador como el denominador; la fórmula directa de $a$ del ejemplo inicial también sitúa su valor entre esos límites. En ese intervalo,

$$
\frac{dM}{da}=\frac{6mg}{(g-a)^2}>0.
$$

Por tanto, la cota más ajustada que permiten los datos del problema se obtiene en los extremos:

$$
M\in\left[\frac{184}{27},\frac{568}{79}\right]\,\mathrm{kg}
\subset[6{,}814;7{,}190]\,\mathrm{kg}.
$$

La envolvente decimal se redondeó hacia fuera. La derivada también explica una limitación del ensayo: al acercarse $a$ a $g$, una pequeña variación de la aceleración puede producir una variación grande en la masa inferida. Elegir una observación que identifica un parámetro y elegir una observación que lo determina con una cota útil son decisiones relacionadas que conviene examinar juntas.

### 20. Repartir el movimiento sin resolver fuerzas {#solucion-6-20}

Las longitudes rectas son $y_1-y_P$ y $y_2-y_P$, más constantes de tangencia y un arco constante. Al derivar dos veces obtenemos $\ddot y_1+\ddot y_2=2\ddot y_P=2\,\mathrm{m/s^2}$. La ecuación fija la suma, pero permite infinitos repartos. Las dos parejas propuestas satisfacen esa misma suma. Cada una puede generar, al menos localmente, posiciones compatibles si se eligen posiciones y velocidades iniciales que también cumplan la longitud y su primera derivada.

La cuerda inferior tira de la polea hacia abajo con dos fuerzas $T$. La segunda cuerda tira de su eje hacia arriba con $S$. La idealización de masa despreciable impone fuerza neta nula sobre la polea: $S=2T$. No se sigue $S=T$, porque son cuerdas distintas y la primera actúa mediante dos ramales.

Para escoger un reparto dinámico hacen falta las masas y fuerzas de los cuerpos conectados a los extremos, las condiciones de la segunda cuerda y los datos iniciales compatibles. La aceleración prescrita del centro y el balance de una polea sin masa no suministran por sí solos toda esa información. Lo que sí hemos obtenido son condiciones que cualquier solución del aparato completo tendría que respetar.

## Lecturas de apoyo

Sears y Zemansky, *Física universitaria*, volumen 1, Young y Freedman, 13.ª edición, §5.2, ejemplo 5.12, pp. 145–146, desarrolla el enlace entre longitud de cuerda y aceleraciones en el caso de una polea fija. Serway y Jewett, *Física para ciencias e ingeniería*, volumen 1, 10.ª edición española, ejemplos 5.9 y 5.10, pp. 112–114, permite cotejar la máquina de Atwood y los ejes de dos cuerpos conectados. La igualdad de módulos de esos casos se interpreta aquí a partir del recorrido concreto antes de pasar a una polea móvil.

Spivak, *Physics for Mathematicians. Mechanics I*, capítulo 6, pp. 241–246, analiza la máquina de Atwood, la idealización de una cuerda sin masa y el significado de la tensión; pp. 246–248 distingue el problema con una polea de inercia apreciable. Esa distinción delimita el modelo utilizado en este capítulo: no extendemos la igualdad de tensiones a una rueda masiva sin añadir su ecuación de rotación. Los desarrollos, datos y ejercicios de este capítulo son propios; el cotejo es selectivo y no constituye una revisión completa de esos libros.

---

[← 5. Contactos, tensiones y rozamiento](fisica-para-matematicos-05-contactos-tensiones-y-rozamiento.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [7. Trabajo y energía cinética →](fisica-para-matematicos-07-trabajo-y-energia-cinetica.md)
