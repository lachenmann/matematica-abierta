---
title: "Momento lineal, impulso y centro de masa"
subtitle: "Física para matemáticos · Tomo I · Capítulo 14"
author: "A. Peña"
description: "Capítulo 14 del Tomo I de Física para matemáticos, con ejercicios y soluciones desarrolladas."
archived-content-id: MA-BCH-0354
source-id: FISPM-T1-C14
editorial-id: FPM-I-14
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
date-modified: 2026-10-17
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

[Capítulo 13](fisica-para-matematicos-capitulo-13-energia-potencial-fuerzas-conservativas-y-estabilidad.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos-v04-archivo.md#tomo-i-fundamentos-y-mecanica) · [Capítulo 15](fisica-para-matematicos-capitulo-15-momento-angular-y-torque.md)

[]{#fispm-c14-momento-lineal-impulso-y-centro-de-masa}

Este capítulo estudia balances vectoriales de momento para partículas y sistemas materiales, su integración temporal y la separación del movimiento colectivo y relativo. Prerrequisitos físicos capítulo 9--10; matemática M2--M3 y M6 elemental. La comparación con energía enlaza con el capítulo 12. La segunda parte desarrolla colisiones y sistemas abiertos.

[]{#momento-lineal-de-una-partícula}

[]{#fispm-t1-c14-s01}

[]{#fpm-i-14-s01}

## 1. Momento lineal de una partícula {#fispm-c14-momento-lineal-de-una-partuxedcula}

El balance de energía cinética compara rapidez y trabajo. Para conservar información direccional conviene introducir una magnitud vectorial que relaciona masa y velocidad: el momento lineal. Su variación se obtiene directamente de Newton y permitirá después sumar las ecuaciones de muchas partículas sin reconstruir primero sus interacciones.[^1]

[]{#fispm-t1-c14-d0001}

**Definición 14.1 --- Momento lineal de una partícula.** Una partícula de masa constante $m>0$, con velocidad $\mathbf v$ medida en un marco inercial elegido, tiene momento lineal $\mathbf p=m\mathbf v$. Sus unidades SI son $\mathrm{kg\,m/s}$, equivalentes a $\mathrm{N\,s}$.

El momento apunta en la dirección de velocidad. No es fuerza: sus unidades y su función en la ecuación son distintas. Tampoco es energía cinética: dos velocidades opuestas producen momentos opuestos y la misma energía $m|\mathbf v|^2/2$. Con masa conocida, el momento determina la velocidad completa mediante $\mathbf v=\mathbf p/m$.

[]{#fispm-t1-c14-p0001}

**Proposición 14.1 --- Fuerza total y derivada del momento.** Para masa constante en un marco inercial, Newton $m\mathbf a=\mathbf F_{\mathrm{tot}}$ equivale a $\dot{\mathbf p}=\mathbf F_{\mathrm{tot}}$.

**Demostración.** Derivar definición 14.1 con $m$ constante da $\dot{\mathbf p}=m\dot{\mathbf v}=m\mathbf a$. Sustituir una de las dos ecuaciones produce la otra. $\square$

La igualdad usa la fuerza total sobre la partícula. Si actúan peso, tensión y contacto, se suman antes de identificar $\dot{\mathbf p}$. Una fuerza particular modifica el momento junto con las demás; no puede atribuirse todo el cambio a ella sin verificar que las otras contribuciones se anulan.

La formulación vectorial contiene una igualdad por componente. Si $\mathbf F_{\mathrm{tot}}$ es perpendicular a una dirección fija $\mathbf e$, entonces $d(\mathbf p\cdot\mathbf e)/dt=0$ aunque las otras componentes varíen. Si la dirección elegida gira con el tiempo, derivar $\mathbf p\cdot\mathbf e(t)$ añade $\mathbf p\cdot\dot{\mathbf e}$; no se puede omitir ese término. Trabajaremos inicialmente con ejes fijos de un marco inercial.

El momento depende del marco porque la velocidad depende de él. Bajo una traslación uniforme de velocidad $\mathbf U$, $\mathbf v'=\mathbf v-\mathbf U$ y $\mathbf p'=\mathbf p-m\mathbf U$. La diferencia entre dos instantes permanece igual cuando $m$ y $\mathbf U$ son constantes. Esto anticipa una propiedad útil: observadores inerciales relacionados de ese modo coinciden en el cambio de momento, aunque no en su valor absoluto.

Para masa constante, la energía cinética puede expresarse como $K=|\mathbf p|^2/(2m)$. Esta expresión pierde la dirección al tomar el cuadrado del módulo. Conocer $K$ no permite reconstruir $\mathbf p$; conocer $\mathbf p$ y $m$ sí permite calcular $K$. Los dos balances ofrecen información diferente y pueden combinarse cuando sus hipótesis son compatibles.

Si una descripción hace variar la masa que pertenece al objeto elegido, derivar formalmente $m(t)\mathbf v(t)$ añade $\dot m\mathbf v$. Pero ese cálculo no decide qué materia entra o sale ni qué momento transporta. Proposición 14.1 se ha probado para una partícula de masa constante; el balance de un sistema abierto requiere otra formulación que reservamos para §13.

[]{#fispm-t1-c14-mp0001}

**Principio metodológico 14.1 --- Fijar receptor, masa y marco.** Declara sobre qué partícula actúan las fuerzas y en qué marco mides su velocidad. Conserva el carácter vectorial del momento y usa la resultante para su derivada. No extiendas la prueba de masa constante a un objeto con transferencia de materia.

[]{#ejercicios}

### Ejercicios {#fispm-c14-ejercicios}

[]{#fispm-t1-c14-e0001}

[]{#fispm-t1-c14-e0014}

**Ejercicio 14.1.** Una masa de $2\,\mathrm{kg}$ pasa de velocidad $(3,-1)\,\mathrm{m/s}$ a $(-1,2)\,\mathrm{m/s}$. Calcula los momentos inicial y final, su cambio y el cambio de energía cinética. ¿Permite el signo de este último deducir la dirección del cambio de momento?

**Solución.** Los momentos son $(6,-2)$ y $(-2,4)\,\mathrm{kg\,m/s}$; su cambio es $(-8,6)\,\mathrm{kg\,m/s}$. La energía inicial es $2(3^2+(-1)^2)/2=10\,\mathrm J$ y la final $2((-1)^2+2^2)/2=5\,\mathrm J$, por lo que $\Delta K=-5\,\mathrm J$. Ese signo dice que disminuyó la rapidez, pero no determina el vector $\Delta\mathbf p$. Aquí cambia tanto su componente horizontal como la vertical. Una igualdad escalar no sustituye los datos vectoriales.

[]{#fispm-t1-c14-e0002}

**Ejercicio 14.2.** En una línea, una masa $m$ parte con momento $p_0$ y recibe fuerza total constante $F_0$ durante $0\leq t\leq T$. Obtén momento, velocidad y posición, suponiendo posición inicial $x_0$. Indica qué información inicial no aparece en la ecuación del momento.

**Solución.** proposición 14.1 da $p(t)=p_0+F_0t$, así que $v(t)=p_0/m+F_0t/m$. Integrar produce $x(t)=x_0+(p_0/m)t+F_0t^2/(2m)$. El momento y la ley de fuerza permiten obtener velocidad, pero la posición requiere además $x_0$. Si la fuerza dependiera de posición, ambas ecuaciones tendrían que resolverse conjuntamente; no basta integrar una fuerza temporal que todavía no conocemos sobre la historia.

[]{#impulso-y-fuerza-media}

[]{#fispm-t1-c14-s02}

[]{#fpm-i-14-s02}

## 2. Impulso y fuerza media {#fispm-c14-impulso-y-fuerza-media}

Una fuerza puede variar mucho durante un contacto breve. Si buscamos el cambio de momento entre dos instantes, basta su integral temporal. Esa magnitud se llama impulso y se define también para fuerzas suaves que actúan durante largo tiempo: no presupone un golpe instantáneo ni una discontinuidad de velocidad.[^2]

[]{#fig:I-14-N02}

<figure id="fig-fpm-v04-i-14-n02" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-14-N02.svg" class="lightbox" data-gallery="fpm-v04-c14"><img src="/assets/books/fispm/v04/I-14-N02.svg" alt="Impulso de un pulso. Diagrama del capítulo 14; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="424" height="253" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 14.1.** Un pulso triangular de duración $2T$ y altura $F_0$ tiene impulso $F_0T$. Su fuerza media es $F_0/2$; el área, y no la altura máxima por sí sola, determina el cambio de momento. Véase §[2](#fispm-c14-impulso-y-fuerza-media).

</figcaption>

</figure>

[]{#fispm-t1-c14-d0002}

**Definición 14.2 --- Impulso de una fuerza.** Para una historia de fuerza integrable $\mathbf F(t)$ en $[t_a,t_b]$, su impulso es $\mathbf J=\int_{t_a}^{t_b}\mathbf F(t)dt$. Es un vector con unidades de momento. La integral es temporal, no espacial.

[]{#fispm-t1-c14-d0003}

**Definición 14.3 --- Fuerza media temporal.** Si $\Delta t=t_b-t_a>0$, la fuerza media es $\overline{\mathbf F}=\mathbf J/\Delta t$. Representa el vector constante que tendría el mismo impulso en ese intervalo, sin afirmar que coincidan sus picos ni la posición del receptor.

[]{#fispm-t1-c14-p0002}

**Proposición 14.2 --- Teorema impulso--momento.** Para una partícula de masa constante que cumple Newton, $\mathbf p_b-\mathbf p_a=\mathbf J_{\mathrm{tot}}$. El impulso total es la suma de los impulsos de todas las fuerzas que actúan durante el intervalo.

**Demostración.** Integrar proposición 14.1 da $\int_{t_a}^{t_b}\dot{\mathbf p}\,dt=\int_{t_a}^{t_b}\mathbf F_{\mathrm{tot}}dt$. El lado izquierdo es la diferencia de momentos. Para una suma finita de fuerzas, la linealidad de la integral permite sumar sus impulsos. El argumento se aplica también por tramos con extremos comunes. $\square$

El trabajo y el impulso integran información distinta. El primero usa $\mathbf F\cdot\mathbf v\,dt$ y tiene unidades de energía; el segundo usa $\mathbf Fdt$ y tiene unidades de momento. Un impulso no nulo puede cambiar la dirección de velocidad sin cambiar la energía entre extremos. Un trabajo conocido tampoco determina todas las componentes del impulso.

[]{#fispm-t1-c14-p0003}

**Proposición 14.3 --- Cota del impulso y error de una omisión.** Si $|\mathbf F(t)|\leq F_{\max}$ en un intervalo de duración $\Delta t$, entonces $|\mathbf J|\leq F_{\max}\Delta t$. Si una fuerza omitida cumple esa cota, el error vectorial en el momento final calculado con las otras fuerzas es a lo sumo $F_{\max}\Delta t$, siempre que se usen sus impulsos sobre la historia real.

**Demostración.** La desigualdad triangular de la integral da $|\int\mathbf Fdt|\leq\int|\mathbf F|dt\leq F_{\max}\Delta t$. El balance exacto difiere del que omite esa contribución en su impulso; se aplica la misma cota. $\square$

La última precisión evita una confusión: omitir una fuerza al resolver la dinámica también puede cambiar la historia y los impulsos de las fuerzas restantes. Proposición 14.3 acota directamente la contribución omitida sobre la historia considerada, no un error global arbitrario de modelización. Para comparar dos historias habría que controlar esa dependencia adicional.

Durante un contacto breve, el impulso del peso tiene magnitud $mg\Delta t$. Puede ser pequeño frente al impulso de contacto, pero debe compararse con una escala de momento y una tolerancia. La brevedad por sí sola no garantiza un error relativo pequeño si el cambio total es casi cero por cancelación. En ese caso sigue siendo válida una cota absoluta.

Para un impulso fijo, alargar la duración reduce el módulo de la fuerza media. No obliga a reducir cualquier pico instantáneo imaginable: una historia larga puede contener un pulso muy alto y estrecho. Una afirmación sobre picos requiere fijar además la forma temporal o una familia de modelos de contacto.

[]{#fispm-t1-c14-mp0002}

**Principio metodológico 14.2 --- Integrar todas las contribuciones y controlar la aproximación.** Usa el impulso total para el cambio de momento. Si desprecias una fuerza, estima su impulso y declara la escala de comparación. Distingue fuerza media, pico y ley temporal; no deduzcas una historia completa sólo de su área bajo la curva.

[]{#ejercicios-1}

### Ejercicios {#fispm-c14-ejercicios-1}

[]{#fispm-t1-c14-e0003}

**Ejercicio 14.3.** Una masa de $0{,}5\,\mathrm{kg}$ cambia de velocidad vertical $-4\,\mathrm{m/s}$ a $3\,\mathrm{m/s}$ durante un contacto de $0{,}02\,\mathrm s$. Usa $g=10\,\mathrm{m/s^2}$ y sentido positivo hacia arriba. Calcula impulso y fuerza media de contacto, incluyendo el peso.

**Solución.** El cambio de momento es $0{,}5[3-(-4)]=3{,}5\,\mathrm{N\,s}$ hacia arriba. El peso aporta $-mg\Delta t=-0{,}1\,\mathrm{N\,s}$. Por tanto, el contacto aporta $J_c=3{,}6\,\mathrm{N\,s}$ y su fuerza media es $180\,\mathrm N$ hacia arriba. La fuerza total media es $175\,\mathrm N$. Confundir las dos omitiría los $5\,\mathrm N$ de peso. Estos datos no determinan el pico de contacto ni su distribución temporal.

[]{#fispm-t1-c14-e0004}

**Ejercicio 14.4.** Una fuerza unidimensional sobre $0\leq t\leq T$ tiene perfil triangular: $F(t)=2F_pt/T$ hasta $T/2$ y $F(t)=2F_p(1-t/T)$ después, con $F_p>0$. Calcula impulso y fuerza media. Compara con una fuerza constante de igual impulso.

**Solución.** Cada mitad aporta el área de un triángulo de base $T/2$ y altura $F_p$, igual a $F_pT/4$. El impulso es $F_pT/2$ y la fuerza media $F_p/2$. La fuerza constante correspondiente es $F_p/2$ durante todo el intervalo, y produce el mismo cambio de momento si ambas son fuerzas totales. Sus picos difieren: $F_p$ para el triángulo y $F_p/2$ para la constante. Sus posiciones intermedias difieren; para estos dos perfiles simétricos y los mismos datos iniciales, el desplazamiento final coincide: $v_0T+F_pT^2/(4m)$ para una partícula de masa constante $m$. En general, el impulso total no fija el desplazamiento: éste depende también de la distribución temporal de la fuerza, mediante $\Delta x=v_0T+m^{-1}\int_0^T(T-t)F(t)dt$.

[]{#momento-de-un-sistema-material}

[]{#fispm-t1-c14-s03}

[]{#fpm-i-14-s03}

## 3. Momento de un sistema material {#fispm-c14-momento-de-un-sistema-material}

Para sumar las ecuaciones de partículas hay que fijar cuáles pertenecen al sistema. La elección puede ser amplia o estrecha, pero debe mantenerse durante el intervalo. Una interacción entre miembros cuenta como interna; la misma fuerza pasa a ser externa si uno de los cuerpos queda fuera. La cancelación interna es una consecuencia de la tercera ley dentro del modelo elegido.[^3]

[]{#fispm-t1-c14-d0004}

**Definición 14.4 --- Momento total de un sistema material finito.** Un sistema formado por una lista fija de $n$ partículas de masas constantes $m_i>0$ tiene masa total $M=\sum_i m_i$ y momento total $\mathbf P=\sum_i\mathbf p_i=\sum_i m_i\mathbf v_i$. Todas las velocidades se miden en el mismo marco inercial.

La palabra «material» significa aquí que seguimos los mismos miembros. No se sustituye una partícula por otra porque una atraviese una región del espacio. El sistema puede deformarse, separarse y cambiar su distribución; esas posibilidades no modifican la lista de masas que sumamos. Un conjunto definido por la materia que ocupa una caja fija puede tener entradas y salidas y necesitar otro balance.

Denotemos por $\mathbf F_i^{\mathrm{ext}}$ la resultante sobre $i$ debida a agentes fuera del sistema, y por $\mathbf F_{ij}$ la fuerza que $j$ ejerce sobre $i$. El primer índice identifica al receptor. Supondremos interacciones internas por pares que cumplen $\mathbf F_{ji}=-\mathbf F_{ij}$ al mismo tiempo en este modelo newtoniano.

[]{#fispm-t1-c14-p0004}

**Proposición 14.4 --- Balance externo del momento total.** Si cada miembro cumple Newton con las fuerzas anteriores, entonces

$$\dot{\mathbf P}=\mathbf F_{\mathrm{ext}},\qquad \mathbf F_{\mathrm{ext}}=\sum_i\mathbf F_i^{\mathrm{ext}},\qquad \mathbf P_b-\mathbf P_a=\int_{t_a}^{t_b}\mathbf F_{\mathrm{ext}}dt.$$

**Demostración.** proposición 14.1 para cada partícula da $\dot{\mathbf p}_i=\mathbf F_i^{\mathrm{ext}}+\sum_{j\ne i}\mathbf F_{ij}$. Sumamos las igualdades. La suma interna se agrupa como $\sum_{i<j}(\mathbf F_{ij}+\mathbf F_{ji})=0$ por la tercera ley. La derivada de la suma finita es $\dot{\mathbf P}$ y permanece únicamente la resultante externa. Integrar en tiempo da la última identidad. $\square$

No se ha supuesto que las fuerzas internas sean pequeñas ni que las partículas tengan velocidades iguales. Tampoco se ha exigido que las fuerzas de cada par estén sobre la línea que une sus posiciones. Para este balance de momento basta la igualdad y oposición vectorial declarada. Otras magnitudes, como el momento angular, pueden requerir propiedades adicionales, que se tratarán en el capítulo 15.

La cancelación de fuerzas no equivale a cancelación de trabajo. Para un par interno, la potencia conjunta es $\mathbf F_{ij}\cdot(\mathbf v_i-\mathbf v_j)$, como se probó en el capítulo 12. Puede ser no nula aunque $\mathbf F_{ij}+\mathbf F_{ji}=0$. Un resorte entre masas puede modificar su energía cinética total mientras deja constante su momento total si no hay resultante externa. Los balances se complementan porque suman objetos distintos.

La tercera ley es una hipótesis del modelo de partículas e interacciones. Si una descripción omite un medio que transporta momento o no satisface la oposición instantánea por pares, no puede aplicarse esta prueba por costumbre. Habría que ampliar el sistema o escribir el término de balance que falta. Aquí trabajaremos con los modelos mecánicos elementales de Newton ya establecidos.

[]{#fispm-t1-c14-mp0003}

**Principio metodológico 14.3 --- Fijar miembros antes de cancelar fuerzas.** Escribe la lista del sistema y separa sus interacciones internas de los agentes externos. Usa acción y reacción sobre receptores distintos para cancelar la suma de fuerzas. No deduzcas de esa cancelación un trabajo interno nulo ni conservación de cada momento individual.

[]{#ejercicios-2}

### Ejercicios {#fispm-c14-ejercicios-2}

[]{#fispm-t1-c14-e0005}

**Ejercicio 14.5.** Dos masas $m_1=1\,\mathrm{kg}$ y $m_2=3\,\mathrm{kg}$ se mueven en una línea con velocidades iniciales $2$ y $-1\,\mathrm{m/s}$. Reciben fuerzas internas iguales y opuestas, y fuerzas externas constantes $4\,\mathrm N$ sobre la primera y $-1\,\mathrm N$ sobre la segunda durante $2\,\mathrm s$. Obtén el momento final total. ¿Quedan determinadas ambas velocidades finales?

**Solución.** El momento inicial es $1\cdot2+3(-1)=-1\,\mathrm{kg\,m/s}$. La resultante externa es $3\,\mathrm N$ y su impulso $6\,\mathrm{N\,s}$, por lo que $P_b=5\,\mathrm{kg\,m/s}$. Las velocidades finales sólo satisfacen $v_{1,b}+3v_{2,b}=5$. Sin información sobre las fuerzas internas y la evolución, esa igualdad no las determina por separado. Por ejemplo, $(5,0)$ y $(2,1)$ producen el mismo momento total, aunque corresponden a historias y energías distintas.

[]{#fispm-t1-c14-e0006}

**Ejercicio 14.6.** Sobre dos partículas actúa únicamente un par interno $\mathbf F_{12}=\mathbf f(t)$, $\mathbf F_{21}=-\mathbf f(t)$. Calcula sus cambios de momento en función del impulso del par y decide qué se conserva. Explica por qué no se ha probado conservación de energía cinética.

**Solución.** Si $\mathbf J=\int\mathbf f(t)dt$, entonces $\Delta\mathbf p_1=\mathbf J$ y $\Delta\mathbf p_2=-\mathbf J$. La suma da $\Delta\mathbf P=0$ en cada intervalo, y proposición 14.4 mantiene $\mathbf P$ constante. Cada momento puede cambiar. La potencia total interna es $\mathbf f\cdot(\mathbf v_1-\mathbf v_2)$ y no tiene por qué anularse. La oposición de fuerzas controla el momento; no elimina por sí sola la variación cinética causada por una deformación o por movimiento relativo.

[]{#conservación-y-componentes}

[]{#fispm-t1-c14-s04}

[]{#fpm-i-14-s04}

## 4. Conservación y componentes {#fispm-c14-conservaciuxf3n-y-componentes}

Una resultante externa nula mantiene constante el momento total. Una resultante con una componente nula conserva sólo la componente correspondiente. Y un impulso total nulo entre dos instantes garantiza igualdad de los momentos extremos, sin afirmar que el momento se mantuvo constante entre ellos. Conviene separar esos tres enunciados antes de usar una ley de conservación.[^4]

[]{#fispm-t1-c14-p0005}

**Proposición 14.5 --- Conservación vectorial y por proyecciones fijas.** Bajo las hipótesis de la proposición 14.4, si $\mathbf F_{\mathrm{ext}}=0$ en todo un intervalo, $\mathbf P$ es constante allí. Si una dirección fija $\mathbf e$ satisface $\mathbf F_{\mathrm{ext}}\cdot\mathbf e=0$ en todo el intervalo, entonces $\mathbf P\cdot\mathbf e$ es constante aunque las otras componentes puedan cambiar.

**Demostración.** En el primer caso proposición 14.4 da $\dot{\mathbf P}=0$ y su integración mantiene el valor inicial. En el segundo, por ser $\mathbf e$ constante, $d(\mathbf P\cdot\mathbf e)/dt=\dot{\mathbf P}\cdot\mathbf e=\mathbf F_{\mathrm{ext}}\cdot\mathbf e=0$. Integrar da la conservación de la proyección. $\square$

Ausencia de interacción externa es una condición suficiente, pero no necesaria: varias fuerzas externas pueden tener resultante cero. Un sistema que recibe peso y una reacción equilibrada puede conservar el momento en un régimen concreto aunque existan agentes externos. La prueba depende de la suma efectiva y del intervalo, no de la etiqueta «aislado» aplicada sin inspección de fuerzas.

[]{#fispm-t1-c14-p0006}

**Proposición 14.6 --- Impulso nulo entre extremos frente a conservación durante un intervalo.** La igualdad $\int_{t_a}^{t_b}\mathbf F_{\mathrm{ext}}dt=0$ implica $\mathbf P_b=\mathbf P_a$, pero no implica que $\mathbf P$ sea constante durante todo el intervalo.

**Demostración.** La primera afirmación es proposición 14.4. Para refutar la segunda basta una partícula que recibe en una línea $F(t)=F_0\cos(\omega t)$, con $F_0\ne0$, $\omega>0$, durante $0\leq t\leq2\pi/\omega$. Su impulso total es cero, mientras proposición 14.1 da $p(t)=p_0+(F_0/\omega)\sin(\omega t)$, que no es constante. La velocidad $p(t)/m$ y su integral definen una historia que cumple Newton. $\square$

La conservación puede servir para calcular un retroceso sin conocer la duración ni la ley detallada de interacción interna. Sin embargo, las velocidades de entrada deben pertenecer al mismo marco. Un dato medido respecto de un dispositivo que retrocede no coincide automáticamente con la velocidad respecto del laboratorio. Esa diferencia altera la ecuación de momento aunque la conservación siga siendo correcta.

Elegir sólo el objeto expulsado hace externa la fuerza del dispositivo. Elegir objeto y dispositivo permite que esa interacción se cancele, pero obliga a incluir las masas y velocidades de ambos. Si el dispositivo está anclado al suelo, puede recibir un impulso externo del anclaje y el momento del conjunto objeto--dispositivo no tiene por qué conservarse. Ampliar el sistema no elimina de manera automática toda interacción exterior.

[]{#fispm-t1-c14-mp0004}

**Principio metodológico 14.4 --- Conservar sólo lo acreditado.** Comprueba la resultante externa o su proyección durante el intervalo relevante. Si sólo conoces impulso nulo, limita la conclusión a los extremos. Convierte todos los datos de velocidad al mismo marco y verifica si apoyos o anclajes aportan impulso al sistema elegido.

[]{#ejercicios-3}

### Ejercicios {#fispm-c14-ejercicios-3}

[]{#fispm-t1-c14-e0007}

**Ejercicio 14.7.** Dos cuerpos de masas $M$ y $m$ están inicialmente en reposo sobre una guía horizontal fija lisa. Un mecanismo interno los separa. Al terminar, el cuerpo $m$ tiene velocidad relativa al cuerpo $M$ igual a $u>0$ hacia la derecha. Calcula las velocidades de ambos respecto del laboratorio.

**Solución.** Las fuerzas externas no tienen componente horizontal, de modo que $MV+mv=0$. El dato relativo es $v-V=u$. Sustituir $v=V+u$ da $(M+m)V+mu=0$, por lo que $V=-mu/(M+m)$ y $v=Mu/(M+m)$. Usar $v=u$ como dato de laboratorio habría ignorado el retroceso. Las velocidades satisfacen ambas ecuaciones. El trabajo del mecanismo puede modificar la energía cinética total; la conservación horizontal de momento no afirma que ésta permanezca en cero.

[]{#fispm-t1-c14-e0008}

**Ejercicio 14.8.** Un sistema material de masa total $M$ recibe sólo peso uniforme y fuerzas internas que cumplen tercera ley, sin resistencia. Su momento inicial es $(P_{x,0},P_{y,0})$ en el plano vertical. Obtén su momento en el tiempo e identifica las componentes conservadas.

**Solución.** La resultante externa es $(0,-Mg)$, de modo que $P_x(t)=P_{x,0}$ y $P_y(t)=P_{y,0}-Mgt$. Se conserva la componente horizontal y cambia la vertical. Que la resultante interna sea cero no elimina el peso. Este balance todavía no proporciona las posiciones de cada miembro ni su movimiento relativo. Tampoco basta conocer que la componente vertical vuelva a un valor anterior en alguna historia con otras fuerzas: eso sería una comparación entre extremos, no conservación acreditada durante todo el intervalo.

[]{#centro-de-masa-como-promedio-afín}

[]{#fispm-t1-c14-s05}

[]{#fpm-i-14-s05}

## 5. Centro de masa como promedio afín {#fispm-c14-centro-de-masa-como-promedio-afuxedn}

La suma de momentos combina velocidades, pero todavía no identifica una posición colectiva. Para masas constantes, el mismo promedio que aparece en el momento total define un punto cuya derivada reproduce esa suma. Este punto es el centro de masa. Su construcción pertenece primero a la geometría: puede definirse para cualquier configuración, sin conocer las fuerzas ni afirmar que allí exista una partícula.[^5]

[]{#fig:I-14-N01}

<figure id="fig-fpm-v04-i-14-n01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-14-N01.svg" class="lightbox" data-gallery="fpm-v04-c14"><img src="/assets/books/fispm/v04/I-14-N01.svg" alt="Promedio afín ponderado. Diagrama del capítulo 14; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="160" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 14.2.** El centro de masa divide la separación en razón inversa a las masas. Con masas $m$ y $3m$, se sitúa a un cuarto de la distancia desde la masa mayor. Véase §[5](#fispm-c14-centro-de-masa-como-promedio-afuxedn).

</figcaption>

</figure>

[]{#fispm-t1-c14-d0005}

**Definición 14.5 --- Centro de masa de un sistema material finito.** Para las masas positivas constantes de la definición 14.4 y posiciones $\mathbf r_i$ medidas desde un mismo origen, se define

$$\mathbf R=\frac{1}{M}\sum_{i=1}^n m_i\mathbf r_i, \qquad M=\sum_{i=1}^n m_i.$$

Los coeficientes $m_i/M$ son positivos y suman uno. Por eso la fórmula representa un promedio de puntos y no una suma arbitraria de vectores. La dimensión de $\mathbf R$ es longitud. Multiplicar todas las masas por el mismo factor positivo no modifica el punto, aunque sí cambia la masa total y la respuesta dinámica a una fuerza dada. Dos configuraciones distintas pueden tener el mismo centro de masa; el promedio pierde información sobre su distribución interna.

[]{#fispm-t1-c14-p0007}

**Proposición 14.7 --- Cambio de origen y agrupación.** Si el origen se desplaza por un vector fijo $\mathbf a$, de modo que $\mathbf r_i'=\mathbf r_i-\mathbf a$, entonces $\mathbf R'=\mathbf R-\mathbf a$. Si el sistema se divide en grupos disjuntos de masas $M_\alpha$ y centros $\mathbf R_\alpha$, entonces $\mathbf R=\sum_\alpha M_\alpha\mathbf R_\alpha/M$.

**Demostración.** Sustituir el cambio de origen en la definición 14.5 da $\sum_i m_i(\mathbf r_i-\mathbf a)/M=\mathbf R-\mathbf a\sum_i m_i/M=\mathbf R-\mathbf a$. Para agrupar, la definición del centro de cada grupo da $M_\alpha\mathbf R_\alpha=\sum_{i\in\alpha}m_i\mathbf r_i$. Sumar sobre la partición cuenta cada miembro una vez y produce $M\mathbf R$. $\square$

La primera identidad prueba que el centro es un punto geométrico consistente: cambiar el origen cambia su vector de posición exactamente como el de cualquier otro punto. La segunda permite sustituir un grupo por su masa concentrada en su centro para calcular el centro del conjunto. Esa sustitución preserva este promedio; no preserva automáticamente fuerzas, energía interna ni movimiento de los miembros.

[]{#fispm-t1-c14-p0008}

**Proposición 14.8 --- Localización en el envolvente convexo.** El centro de masa pertenece al envolvente convexo de las posiciones de los miembros. En particular, cada una de sus coordenadas está entre la menor y la mayor coordenada de esos miembros.

**Demostración.** El envolvente convexo es el conjunto de todas las combinaciones $\sum_i\lambda_i\mathbf r_i$ con $\lambda_i\geq0$ y $\sum_i\lambda_i=1$. Definición 14.5 tiene esa forma con $\lambda_i=m_i/M$. Para una coordenada $x$, de $x_{\min}\leq x_i\leq x_{\max}$ se obtiene, multiplicando por esos pesos y sumando, $x_{\min}\leq R_x\leq x_{\max}$. Lo mismo vale para cualquier proyección fija. $\square$

Pertenecer al envolvente convexo no significa pertenecer al material. Dos masas separadas tienen un centro en el segmento que las une, posiblemente en el vacío. Tampoco la simetría geométrica basta si las masas no respetan esa simetría. Una configuración y su distribución de masa invariantes bajo reflexión tienen un centro en el plano de reflexión: los términos de cada par se cancelan en la coordenada normal y los puntos del plano aportan cero allí.

[]{#fispm-t1-c14-mp0005}

**Principio metodológico 14.5 --- Calcular y controlar el promedio.** Usa posiciones en un mismo sistema de coordenadas, conserva las masas como pesos y comprueba la suma de pesos. Agrupa sólo conjuntos disjuntos que cubran el sistema. Contrasta el resultado con cotas de coordenadas y simetrías de la distribución de masa; interpreta el punto sin suponer que contiene material.

[]{#ejercicios-4}

### Ejercicios {#fispm-c14-ejercicios-4}

[]{#fispm-t1-c14-e0009}

**Ejercicio 14.9.** Tres partículas de masas $m$, $2m$ y $m$ ocupan $(0,0)$, $(3a,0)$ y $(0,2a)$, con $a>0$. Calcula su centro y verifica el cambio a un origen situado en $(a,a)$.

**Solución.** La masa total es $4m$ y $\mathbf R=(6ma,2ma)/(4m)=(3a/2,a/2)$. Las nuevas posiciones son $(-a,-a)$, $(2a,-a)$ y $(-a,a)$. Su promedio ponderado es $(3a/2,a/2)-(a,a)=(a/2,-a/2)$, como predice proposición 14.7. En las coordenadas originales el resultado cae dentro de los intervalos $[0,3a]$ y $[0,2a]$. Más precisamente, sus pesos $1/4,1/2,1/4$ lo sitúan dentro del triángulo de los tres puntos. El promedio simple de los tres vértices daría otro punto porque ignoraría la masa doble.

[]{#fispm-t1-c14-e0010}

**Ejercicio 14.10.** Un grupo A de masa $3m$ tiene centro en $x_A=-2a$ y un grupo B de masa $m$ tiene centro en $x_B=6a$. Encuentra el centro del conjunto. ¿Obliga el resultado a que algún miembro esté allí?

**Solución.** proposición 14.7 da $R_x=[3m(-2a)+m(6a)]/(4m)=0$. El centro está entre los centros de los grupos y más cerca del más pesado: sus distancias son $2a$ y $6a$. No exige que exista material en $x=0$. Por ejemplo, si cada grupo se representa por una partícula situada en su centro, ambas están fuera del origen y éste sigue siendo el centro del conjunto. La información tampoco determina el tamaño ni la distribución interna de los grupos. Concentrarlos en sus centros es suficiente para este cálculo, pero no convierte al conjunto en una sola partícula en todos los aspectos.

[]{#dinámica-del-centro-de-masa}

[]{#fispm-t1-c14-s06}

[]{#fpm-i-14-s06}

## 6. Dinámica del centro de masa {#fispm-c14-dinuxe1mica-del-centro-de-masa}

El centro de masa se definió sin dinámica. Ahora su utilidad se obtiene al diferenciar el promedio: como las masas y la lista de miembros son constantes, las derivadas pasan a las posiciones. El resultado conecta la suma de Newton con una ecuación para un solo punto. Esa ecuación gobierna el movimiento colectivo y deja pendiente el movimiento de cada miembro alrededor de ese punto.[^6]

[]{#fispm-t1-c14-p0009}

**Proposición 14.9 --- Ecuación del centro de masa.** Para el sistema de las definiciones 14.4--14.5, en el marco inercial de la proposición 14.4 y bajo su hipótesis de cancelación interna,

$$\mathbf P=M\dot{\mathbf R},\qquad M\ddot{\mathbf R}=\mathbf F_{\mathrm{ext}}.$$

**Demostración.** Diferenciar $M\mathbf R=\sum_i m_i\mathbf r_i$ da $M\dot{\mathbf R}=\sum_i m_i\dot{\mathbf r}_i=\mathbf P$. Otra derivada y proposición 14.4 dan $M\ddot{\mathbf R}=\dot{\mathbf P}=\mathbf F_{\mathrm{ext}}$. La constancia de las masas y de la pertenencia al sistema justifica ambas derivadas sin términos adicionales. $\square$

Si la resultante externa se conoce como función del tiempo, la ecuación puede integrarse con $\mathbf R(t_0)$ y $\dot{\mathbf R}(t_0)$. En cambio, una identidad para el centro no es necesariamente una ecuación cerrada para él. La suma externa puede depender de las posiciones individuales. En ese caso conocer $\mathbf R$ no basta para evaluarla; pueden requerirse variables internas y sus propias ecuaciones.

Un caso que sí cierra es un campo gravitatorio uniforme. Cada miembro recibe $m_i\mathbf g$, con el mismo vector $\mathbf g$, y la suma vale $M\mathbf g$. Si no hay otras fuerzas externas, $\ddot{\mathbf R}=\mathbf g$. Fragmentar internamente el sistema puede cambiar por completo la disposición de sus partes, pero no esta trayectoria colectiva. El argumento presupone que las partes siguen en el sistema, conserva la masa total y omite de manera declarada resistencia e impulsos externos asociados a la fragmentación.

En un campo no uniforme, $\sum_i m_i\mathbf g(\mathbf r_i)$ no es en general $M\mathbf g(\mathbf R)$. Hay una excepción útil: si $\mathbf g(\mathbf r)=\mathbf b+A\mathbf r$, con matriz constante $A$, la suma es $M\mathbf b+A M\mathbf R=M\mathbf g(\mathbf R)$. Fuera de esa forma, reemplazar todas las posiciones por el centro exige una aproximación cuyo error depende del tamaño y de la variación del campo. La ecuación exacta de la proposición 14.9 no otorga por sí sola esa aproximación.

[]{#fispm-t1-c14-mp0006}

**Principio metodológico 14.6 --- Separar identidad colectiva y cierre dinámico.** Deriva primero la resultante externa del sistema material. Comprueba después si puede expresarse con el centro y datos conocidos. Usa la ecuación colectiva para su trayectoria, sin atribuirle posiciones relativas ni energía interna. En un campo uniforme puedes factorizar la masa; en uno variable debes justificar cualquier sustitución por el valor en el centro.

[]{#ejercicios-5}

### Ejercicios {#fispm-c14-ejercicios-5}

[]{#fispm-t1-c14-e0011}

**Ejercicio 14.11.** Un sistema de masa $M$ tiene centro inicial $\mathbf R_0$ y velocidad colectiva inicial $\mathbf V_0$. Durante $0\leq t\leq T$ recibe una resultante externa constante $\mathbf F_0$. Obtén su centro y momento. ¿Qué información falta para reconstruir sus miembros?

**Solución.** Integrar proposición 14.9 da $\dot{\mathbf R}=\mathbf V_0+\mathbf F_0t/M$, $\mathbf R=\mathbf R_0+\mathbf V_0t+\mathbf F_0t^2/(2M)$ y $\mathbf P=M\mathbf V_0+\mathbf F_0t$. Los cambios tienen las dimensiones de velocidad, longitud y momento respectivas. Para posiciones individuales hacen falta datos iniciales relativos y leyes de interacción, además de la distribución de fuerzas externas entre miembros. Distintas evoluciones internas pueden compartir esta trayectoria del centro. Si la fuerza sólo es constante durante el intervalo indicado, las fórmulas no se prolongan fuera de él sin especificar el régimen siguiente.

[]{#fispm-t1-c14-e0012}

**Ejercicio 14.12.** Dos masas iguales $m$ están instantáneamente en una línea en $x_1=R-a$ y $x_2=R+a$. Cada una recibe una fuerza externa $F(x)=-kx^3$, con $k>0$. Calcula la aceleración del centro y compárala con la de una partícula de masa $2m$ sometida a la fuerza total modelada como $-2kR^3$.

**Solución.** La resultante exacta es $-k[(R-a)^3+(R+a)^3]=-2kR^3-6kRa^2$. Por proposición 14.9, $\ddot R=-(k/m)(R^3+3Ra^2)$. El modelo concentrado daría $\ddot R=-(k/m)R^3$ y perdería el término dependiente de la separación. Coinciden si $a=0$ o $R=0$ en ese instante. La coincidencia instantánea en $R=0$ no prueba equivalencia de historias completas. Si $a$ cambia durante el movimiento, también cambia el término adicional y la ecuación de $R$ requiere conocer esa evolución. Aquí $k$ tiene unidades fuerza/longitud cúbica, por lo que ambos términos de aceleración son dimensionalmente consistentes.

El impulso externo puede escribirse también como $M\Delta\dot{\mathbf R}$. Esto permite medir un cambio colectivo sin seguir cada intercambio interno, pero no localiza el centro durante el contacto a partir del impulso total solamente. Para la posición se necesita la historia temporal de su velocidad, igual que en la partícula de §2. La reducción colectiva mantiene esa distinción entre balance de extremos y trayectoria.

[]{#marco-del-centro-de-masa-y-energía-cinética}

[]{#fispm-t1-c14-s07}

[]{#fpm-i-14-s07}

## 7. Marco del centro de masa y energía cinética {#fispm-c14-marco-del-centro-de-masa-y-energuxeda-cinuxe9tica}

El centro reúne el movimiento colectivo. Para estudiar qué queda al retirarlo, escribimos $\mathbf V=\dot{\mathbf R}$ y $\mathbf u_i=\mathbf v_i-\mathbf V$. Estas velocidades relativas satisfacen $\sum_i m_i\mathbf u_i=\mathbf P-M\mathbf V=0$ por la proposición 14.9. La igualdad es instantánea y algebraica; no requiere que el centro se mueva uniformemente. Su interpretación como cambio entre marcos inerciales sí requiere una condición adicional.[^7]

[]{#fispm-t1-c14-d0006}

**Definición 14.6 --- Coordenadas y marco del centro de masa.** Las coordenadas centradas son $\boldsymbol\rho_i=\mathbf r_i-\mathbf R$ y sus velocidades $\dot{\boldsymbol\rho}_i=\mathbf u_i$, usando ejes paralelos y sin rotación respecto del laboratorio. Si $\mathbf V$ es constante, este cambio define un marco inercial del centro de masa. Si $\mathbf V$ varía, define coordenadas en traslación acelerada y no un segundo marco inercial.

En las coordenadas centradas se cumple $\sum_i m_i\boldsymbol\rho_i=0$. Las posiciones y velocidades relativas no son variables independientes arbitrarias: tienen estas restricciones ponderadas. Si el centro acelera, Newton para cada miembro se escribe $m_i\ddot{\boldsymbol\rho}_i=\mathbf F_i-m_i\ddot{\mathbf R}$. El término adicional no es una nueva interacción entre miembros, sino la corrección debida al movimiento del origen. Mantener ejes paralelos evita aquí términos asociados a rotación.

[]{#fispm-t1-c14-p0010}

**Proposición 14.10 --- Transformación galileana del momento.** Entre dos marcos inerciales de ejes paralelos, uno con velocidad constante $\mathbf U$ respecto del otro, $\mathbf v_i'=\mathbf v_i-\mathbf U$ y $\mathbf P'=\mathbf P-M\mathbf U$. En un instante dado, la elección $\mathbf U=\mathbf P/M$ hace $\mathbf P'=0$ en ese instante. Si $\mathbf P$ es constante, esa elección lo mantiene cero durante el intervalo.

**Demostración.** Sumar $m_i(\mathbf v_i-\mathbf U)$ da $\mathbf P-M\mathbf U$. Como $M>0$, el valor indicado anula la suma. Si $\mathbf P$ cambia mientras $\mathbf U$ sigue constante, la anulación no se conserva; si $\mathbf P$ permanece constante, sí. Proposición 14.9 identifica $\mathbf P/M$ con la velocidad del centro. $\square$

[]{#fispm-t1-c14-p0011}

**Proposición 14.11 --- Separación de la energía cinética.** Para las mismas masas y velocidades,

$$K=\sum_i\frac12m_i|\mathbf v_i|^2 =\frac12M|\mathbf V|^2+K_{\mathrm{rel}}, \qquad K_{\mathrm{rel}}=\sum_i\frac12m_i|\mathbf u_i|^2\geq0.$$

**Demostración.** Sustituir $\mathbf v_i=\mathbf V+\mathbf u_i$ en cada cuadrado da una suma colectiva $M|\mathbf V|^2/2$, la suma relativa y el término cruzado $\mathbf V\cdot\sum_i m_i\mathbf u_i$. Este último es cero por la proposición 14.9 y la definición de $\mathbf u_i$. La positividad de las masas da la desigualdad. La prueba vale en cada instante aunque $\mathbf V$ varíe. $\square$

El término colectivo es $|\mathbf P|^2/(2M)$. Por ello, con masa y momento total fijados, $K\geq |\mathbf P|^2/(2M)$, con igualdad exactamente cuando todas las velocidades coinciden con $\mathbf V$. El momento fija una cota inferior, no toda la energía cinética. Las partes pueden moverse una respecto de otra y elevar $K_{\mathrm{rel}}$ sin cambiar la suma de momentos.

La cantidad $K_{\mathrm{rel}}$ es invariante bajo cambios galileanos: tanto $\mathbf v_i$ como $\mathbf V$ pierden el mismo $\mathbf U$, de modo que $\mathbf u_i$ no cambia. La energía total transforma como $K'=K-\mathbf U\cdot\mathbf P+M|\mathbf U|^2/2$, al expandir $|\mathbf v_i-\mathbf U|^2$. En general, $K$ no es invariante. Nada de esto afirma conservación de $K_{\mathrm{rel}}$: interacciones internas pueden convertir otras formas de energía en movimiento relativo o hacer la conversión inversa.

[]{#fispm-t1-c14-mp0007}

**Principio metodológico 14.7 --- Retirar la traslación con hipótesis visibles.** Calcula $\mathbf V=\mathbf P/M$ y comprueba la suma relativa nula. Separa la energía mediante proposición 14.11 antes de comparar historias. Declara si el origen del centro acelera; usa Newton ordinario en ese marco sólo si es inercial, o incorpora la corrección de aceleración. La identidad cinética sigue siendo válida en ambos casos.

[]{#ejercicios-6}

### Ejercicios {#fispm-c14-ejercicios-6}

[]{#fispm-t1-c14-e0013}

**Ejercicio 14.13.** Dos partículas de masas $m$ y $3m$ tienen velocidades colineales $4u$ y $0$, con $u>0$. Calcula momento, velocidad del centro y los dos términos cinéticos. Comprueba el resultado en un marco que se mueve con velocidad $u$.

**Solución.** $M=4m$, $P=4mu$ y $V=u$. Las velocidades relativas son $3u$ y $-u$, cuya suma ponderada es $3mu-3mu=0$. La energía del laboratorio es $8mu^2$; la colectiva vale $2mu^2$ y la relativa $[9mu^2+3mu^2]/2=6mu^2$. En el marco de velocidad $u$, las velocidades son precisamente $3u$ y $-u$, el momento es cero y la energía es $6mu^2$. Si las fuerzas posteriores cambian $P$, este marco fijo deja de seguir al centro; el cálculo corresponde al instante dado y no implica conservación futura.

**Ejercicio 14.14.** Un sistema de masas positivas tiene momento total $\mathbf P_0$. Determina el menor valor posible de su energía cinética y caracteriza todas las velocidades que lo realizan. ¿Puede un sistema de momento cero tener energía cinética positiva?

**Solución.** proposición 14.11 da $K\geq|\mathbf P_0|^2/(2M)$. La igualdad exige que cada término positivo $m_i|\mathbf u_i|^2/2$ sea cero, luego todas las velocidades son $\mathbf P_0/M$. Esas velocidades cumplen la restricción de momento y realizan la cota, por lo que el mínimo existe. Con momento cero, dos masas iguales con velocidades opuestas no nulas tienen $P=0$ y energía positiva $m|\mathbf v|^2$. Su centro está en reposo mientras hay movimiento relativo. La minimización es sobre velocidades compatibles con el momento; no incluye restricciones adicionales que podrían impedir esas velocidades en un modelo concreto.

[]{#dos-partículas-y-movimiento-relativo}

[]{#fispm-t1-c14-s08}

[]{#fpm-i-14-s08}

## 8. Dos partículas y movimiento relativo {#fispm-c14-dos-partuxedculas-y-movimiento-relativo}

Para dos miembros, una posición colectiva y una separación contienen toda la información posicional. La transformación permite conservar el balance del conjunto mientras se estudia la interacción en una ecuación relativa. La masa que aparece en esta segunda ecuación se obtiene al restar aceleraciones, no al retirar físicamente una parte de la masa total.[^8]

[]{#fispm-t1-c14-d0007}

**Definición 14.7 --- Coordenada relativa de dos partículas.** Para dos masas positivas constantes $m_1,m_2$, con $M=m_1+m_2$, fijamos $\mathbf r=\mathbf r_1-\mathbf r_2$. Su derivada es $\dot{\mathbf r}=\mathbf v_1-\mathbf v_2$. Esta orientación se mantiene en fuerzas, reconstrucción y condiciones iniciales.

[]{#fispm-t1-c14-d0008}

**Definición 14.8 --- Masa reducida.** La masa reducida de ese par es $\mu=m_1m_2/M$, positiva y con dimensión de masa. Equivalentemente, $1/\mu=1/m_1+1/m_2$.

Sea $\mathbf f$ la fuerza interna sobre el miembro 1 debida al 2, y $-\mathbf f$ la fuerza sobre el 2. Sean $\mathbf F_1,\mathbf F_2$ las fuerzas externas respectivas. No se supone aquí que $\mathbf f$ sea central, conservativa ni independiente de las velocidades. Se necesita tercera ley en la forma declarada y un marco inercial común.

[]{#fispm-t1-c14-p0012}

**Proposición 14.12 --- Reconstrucción y ecuación relativa.** Con las convenciones anteriores,

$$\mathbf r_1=\mathbf R+\frac{m_2}{M}\mathbf r, \qquad \mathbf r_2=\mathbf R-\frac{m_1}{M}\mathbf r,$$

$$M\ddot{\mathbf R}=\mathbf F_1+\mathbf F_2, \qquad \mu\ddot{\mathbf r}=\mathbf f+ \frac{m_2}{M}\mathbf F_1-\frac{m_1}{M}\mathbf F_2,$$

$$K=\frac12M|\dot{\mathbf R}|^2+ \frac12\mu|\dot{\mathbf r}|^2.$$

**Demostración.** Resolver $M\mathbf R=m_1\mathbf r_1+m_2\mathbf r_2$ y $\mathbf r=\mathbf r_1-\mathbf r_2$ da las dos posiciones. Proposición 14.9 da la ecuación colectiva. Newton individual da $\ddot{\mathbf r}=(\mathbf F_1+\mathbf f)/m_1-(\mathbf F_2-\mathbf f)/m_2$. Multiplicar por $\mu$ y usar $\mu/m_1=m_2/M$, $\mu/m_2=m_1/M$ y $\mu(1/m_1+1/m_2)=1$ produce la ecuación relativa. Finalmente, derivar las posiciones da $\mathbf u_1=(m_2/M)\dot{\mathbf r}$ y $\mathbf u_2=-(m_1/M)\dot{\mathbf r}$. Sustituirlas en la proposición 14.11 produce un coeficiente $[m_1m_2^2+m_2m_1^2]/M^2=\mu$ para el cuadrado relativo. $\square$

Sin fuerzas externas, el centro se mueve uniformemente y el movimiento relativo satisface $\mu\ddot{\mathbf r}=\mathbf f$. Esto reduce la interacción a una ecuación, pero todavía necesita una ley para $\mathbf f$ y condiciones iniciales. Si la fuerza depende de $\mathbf R$ o de variables adicionales, la reducción algebraica sigue válida sin garantizar desacoplamiento. La sencillez de las coordenadas no sustituye el cierre físico.

Un campo uniforme común $\mathbf F_i=m_i\mathbf g$ acelera el centro con $\mathbf g$ y desaparece de la ecuación relativa: los dos términos externos son $m_1m_2\mathbf g/M$ y su opuesto. Por tanto, las partes pueden cambiar su movimiento interno bajo $\mathbf f$ mientras el conjunto cae. En campos variables puede quedar una diferencia de aceleraciones externas. No basta que ambas fuerzas sean «gravitatorias» para cancelarlas en la ecuación relativa.

La masa reducida es menor que cada masa individual. Para masas iguales vale $m/2$; si $m_2$ crece sin límite con $m_1$ fijo, $\mu$ tiende a $m_1$. Ese límite explica por qué una partícula frente a un cuerpo mucho más pesado puede tratarse aproximadamente con un centro casi fijo. La aproximación necesita controlar además el impulso recibido por el cuerpo pesado y el intervalo considerado. Una masa finita grande no impone velocidad exactamente cero.

[]{#fispm-t1-c14-mp0008}

**Principio metodológico 14.8 --- Resolver colectivo y relativo antes de reconstruir.** Congela la orientación de $\mathbf r$ y el significado de la fuerza $\mathbf f$. Escribe las ecuaciones de la proposición 14.12, examina sus dependencias y transforma también los datos iniciales. Reconstruye cada posición y velocidad al final. Usa $M$ en el movimiento colectivo y $\mu$ en el relativo; verifica que las energías sumen la cinética original.

[]{#ejercicios-7}

### Ejercicios {#fispm-c14-ejercicios-7}

[]{#fispm-t1-c14-e0015}

**Ejercicio 14.15.** Dos masas iguales $m$ reciben sólo una interacción interna $\mathbf f=-k\mathbf r$, con $k>0$. Al inicio su centro está en $\mathbf R_0$ con velocidad $\mathbf V_0$, y $\mathbf r(0)=\mathbf r_0$, $\dot{\mathbf r}(0)=0$. Obtén las posiciones en el tiempo y verifica su energía cinética relativa.

**Solución.** Aquí $\mu=m/2$, $\ddot{\mathbf R}=0$ y $\ddot{\mathbf r}=-(2k/m)\mathbf r$. Con $\omega=\sqrt{2k/m}$, la función $\mathbf r(t)=\mathbf r_0\cos(\omega t)$ satisface la ecuación y ambos datos. Entonces $\mathbf r_1=\mathbf R_0+\mathbf V_0t+\mathbf r_0\cos(\omega t)/2$ y $\mathbf r_2=\mathbf R_0+\mathbf V_0t-\mathbf r_0\cos(\omega t)/2$. Sus velocidades relativas son opuestas, cada una de módulo $|\dot{\mathbf r}|/2$, y su energía relativa suma $m|\dot{\mathbf r}|^2/4=\mu|\dot{\mathbf r}|^2/2$. También $K_{\mathrm{rel}}+k|\mathbf r|^2/2=k|\mathbf r_0|^2/2$, por sustitución de seno y coseno. La frecuencia se verifica aquí como solución de una ecuación concreta; el tratamiento sistemático de oscilaciones queda para el capítulo 23.

[]{#fispm-t1-c14-e0016}

**Ejercicio 14.16.** Dos partículas de masas $m$ y $3m$ reciben sólo fuerzas internas opuestas durante un intervalo. Sus velocidades iniciales en una línea son $2u$ y $0$. El impulso interno sobre la primera es $J=mu$ hacia la derecha. Calcula las velocidades finales mediante el cambio relativo y comprueba el balance de momento y la variación cinética.

**Solución.** $M=4m$, $\mu=3m/4$, $V=P/M=u/2$ y $\dot r_i=2u$. Integrar la ecuación relativa da $\mu\Delta\dot r=J$, luego $\dot r_f=2u+4u/3=10u/3$. Reconstruir produce $v_{1,f}=V+(3/4)\dot r_f=3u$ y $v_{2,f}=V-(1/4)\dot r_f=-u/3$. El momento final es $3mu-mu=2mu$, igual al inicial. La cinética inicial vale $2mu^2$ y la final $9mu^2/2+mu^2/6=14mu^2/3$; aumenta en $8mu^2/3$. El mismo cambio sale de $\mu[(10u/3)^2-(2u)^2]/2$. La interacción suministra energía al movimiento relativo; momento conservado no obliga a cinética conservada. El dato de impulso no determina una ley temporal única ni las posiciones finales.

Las secciones siguientes usan estas herramientas para colisiones: decidir el sistema, controlar impulsos externos y declarar qué información adicional aporta el modelo de interacción. El balance de momento por sí solo deja indeterminadas muchas velocidades finales. Energía cinética, unión o restitución serán hipótesis distintas, cada una con su alcance, y no consecuencias automáticas de tercera ley.

[]{#modelos-de-colisión-y-aislamiento-impulsivo}

[]{#fispm-t1-c14-s09}

[]{#fpm-i-14-s09}

## 9. Modelos de colisión y aislamiento impulsivo {#fispm-c14-modelos-de-colisiuxf3n-y-aislamiento-impulsivo}

Una colisión se describe comparando estados anteriores y posteriores a una interacción. No exige suponer que el contacto dura exactamente cero: elegimos un intervalo que contiene la interacción relevante y declaramos qué fuerzas actúan allí. Las velocidades de entrada y salida son datos de sus extremos, medidos en un mismo marco inercial. Si la interacción sigue almacenando energía en el estado final, tampoco puede identificarse automáticamente el cambio cinético con una pérdida definitiva.[^9]

[]{#fispm-t1-c14-d0009}

**Definición 14.9 --- Modelo de colisión de dos miembros.** Consideraremos dos masas positivas constantes $m_1,m_2$, conservadas como miembros del sistema durante el intervalo $[t_a,t_b]$. Escribiremos $\mathbf v_{1,a},\mathbf v_{2,a}$ para las velocidades iniciales y $\mathbf v_{1,b},\mathbf v_{2,b}$ para las finales; $M=m_1+m_2$, $\mu=m_1m_2/M$ y $\mathbf g_a=\mathbf v_{1,a}-\mathbf v_{2,a}$, $\mathbf g_b=\mathbf v_{1,b}-\mathbf v_{2,b}$. La interacción interna cumple tercera ley. El impulso externo total es $\mathbf J_{\mathrm{ext}}$.

En este modelo, $\mathbf P_b=\mathbf P_a+\mathbf J_{\mathrm{ext}}$ por la proposición 14.4. Una interacción interna muy intensa no cancela el impulso de un apoyo, del peso o de un agente adicional. Su corta duración puede volver pequeño alguno de esos impulsos, pero la escala pertinente es su integral temporal y la precisión requerida. Para conservar una componente basta controlar su impulso externo, aunque otras componentes reciban impulsos grandes.

[]{#fispm-t1-c14-p0013}

**Proposición 14.13 --- Control del balance impulsivo externo.** Si $|\mathbf F_{\mathrm{ext}}(t)|\leq B$ durante una colisión de duración $\tau$, entonces $|\mathbf P_b-\mathbf P_a|\leq B\tau$ y $|\mathbf V_b-\mathbf V_a|\leq B\tau/M$. Una resultante externa nula en todo el intervalo conserva el momento durante él; un impulso externo nulo sólo acredita la igualdad entre extremos.

**Demostración.** proposición 14.4 expresa la diferencia de momentos como la integral de la resultante. La desigualdad integral de la proposición 14.3 da $|\mathbf J_{\mathrm{ext}}|\leq B\tau$. Dividir por $M$ y usar proposición 14.9 da la cota colectiva. La última distinción es proposiciones 14.5--14.6. $\square$

Esta cota controla el momento total y la velocidad del centro. No controla por sí sola el error de cada velocidad final al reemplazar un modelo forzado por otro aislado: la interacción relativa puede cambiar y requerir un análisis adicional. Tampoco asegura una pequeña variación relativa de momento si el valor con que se compara es cero o muy pequeño. Puede formularse una tolerancia absoluta $\varepsilon_P$ y exigir $B\tau\leq\varepsilon_P$, evitando esa división.

[]{#fispm-t1-c14-p0014}

**Proposición 14.14 --- Cambio cinético entre marcos y papel del impulso.** Bajo un cambio galileano de velocidad constante $\mathbf U$, el mismo par de estados satisface

$$\Delta K'=\Delta K-\mathbf U\cdot\mathbf J_{\mathrm{ext}}.$$

Si el impulso externo total es cero, la variación cinética entre esos extremos es igual en ambos marcos.

**Demostración.** La transformación obtenida en §7 es $K'=K-\mathbf U\cdot\mathbf P+M|\mathbf U|^2/2$. Restar sus valores final e inicial cancela el último término, pues $M$ es constante. Proposición 14.4 identifica $\Delta\mathbf P$ con $\mathbf J_{\mathrm{ext}}$. $\square$

La identidad permite comparar pérdidas cinéticas en marcos distintos cuando el momento del sistema se conserva entre extremos. Si el sistema recibe impulso externo, esa comparación necesita la corrección indicada. Por ejemplo, una pared fija puede cambiar el momento de una pelota: si elegimos sólo la pelota, el impulso de la pared es externo y no se cumplen las hipótesis del par aislado. Elegir pelota y pared cambia las masas y los datos que deben incluirse; idealizar la pared como fija es una aproximación diferente.

[]{#fispm-t1-c14-mp0009}

**Principio metodológico 14.9 --- Declarar el intervalo y el aislamiento impulsivo.** Identifica miembros, marco y estados extremos. Calcula o acota los impulsos externos, por componente si procede. Escribe el balance exacto antes de omitir términos y fija una tolerancia. Añade por separado la ley de interacción que decidirá las velocidades relativas.

[]{#ejercicios-8}

### Ejercicios {#fispm-c14-ejercicios-8}

[]{#fispm-t1-c14-e0017}

**Ejercicio 14.17.** Durante un contacto de $0,010\,\mathrm s$, un sistema material de masa $2\,\mathrm{kg}$ recibe una resultante externa cuyo módulo no excede $20\,\mathrm N$. ¿Qué error absoluto máximo introduce imponer igualdad de momentos extremos? ¿Y tratar la velocidad del centro como constante entre extremos?

**Solución.** proposición 14.13 da $|\Delta\mathbf P|\leq0,20\,\mathrm{N\,s}$ y $|\Delta\mathbf V|\leq0,10\,\mathrm{m/s}$. Son cotas del cambio que se omite en cada balance, no errores relativos ni garantías para las velocidades individuales. Si se exige un error de momento inferior a $0,05\,\mathrm{N\,s}$, la información suministrada no basta para justificar la omisión: la cota supera la tolerancia, aunque el impulso real podría ser menor por cancelación temporal. Hace falta conocer mejor la resultante o elegir otra aproximación.

[]{#fispm-t1-c14-e0018}

**Ejercicio 14.18.** Una partícula de masa $m$ llega a una pared fija con velocidad $u>0$ y sale con $-u$. Calcula su impulso y cambio cinético en el laboratorio. Calcula luego el cambio cinético en un marco de velocidad $U$ hacia la derecha.

**Solución.** Para la partícula sola, $J=-2mu$ y $\Delta K=0$. En el otro marco las velocidades son $u-U$ y $-u-U$, por lo que $\Delta K'=m[(-u-U)^2-(u-U)^2]/2=2muU$. Proposición 14.14 da lo mismo: $0-U(-2mu)$. La igualdad cinética del laboratorio no se transporta como igualdad cinética de la partícula a todos los marcos porque ésta recibe impulso externo. En el nuevo marco la pared se mueve y puede transferir trabajo. No hay contradicción entre los observadores ni conservación de momento de la pelota sola.

[]{#colisiones-elásticas-en-una-dimensión}

[]{#fispm-t1-c14-s10}

[]{#fpm-i-14-s10}

## 10. Colisiones elásticas en una dimensión {#fispm-c14-colisiones-eluxe1sticas-en-una-dimensiuxf3n}

En una línea, conservar momento ofrece una ecuación para dos velocidades finales. Una segunda condición puede obtenerse si el modelo afirma igualdad de la energía cinética entre los estados elegidos. Esa condición no proviene de tercera ley: debe justificarse mediante la interacción y sus estados o adoptarse explícitamente como idealización de la colisión.[^10]

[]{#fig:I-14-R01}

<figure id="fig-fpm-v04-i-14-r01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-14-R01.svg" class="lightbox" data-gallery="fpm-v04-c14"><img src="/assets/books/fispm/v04/I-14-R01.svg" alt="Una colisión intercambia velocidades iguales. Diagrama del capítulo 14; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="343" height="341" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 14.3.** En una colisión elástica frontal de dos masas iguales, la masa incidente se detiene y la inicialmente quieta adquiere su velocidad. Se conservan momento y energía cinética; las viñetas comparan velocidades, con separaciones esquemáticas, sin resolver la fuerza de contacto. Véase §[10](#fispm-c14-colisiones-eluxe1sticas-en-una-dimensiuxf3n).

</figcaption>

</figure>

[]{#fig:I-14-N03}

<figure id="fig-fpm-v04-i-14-n03" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-14-N03.svg" class="lightbox" data-gallery="fpm-v04-c14"><img src="/assets/books/fispm/v04/I-14-N03.svg" alt="Choque de masas iguales. Diagrama del capítulo 14; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="415" height="181" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 14.4.** En un choque elástico unidimensional de masas iguales, con la segunda inicialmente en reposo, las velocidades se intercambian. Se conservan momento lineal y energía cinética. Véase §[10](#fispm-c14-colisiones-eluxe1sticas-en-una-dimensiuxf3n).

</figcaption>

</figure>

[]{#fispm-t1-c14-d0010}

**Definición 14.10 --- Colisión elástica en el modelo de dos partículas.** Una colisión es elástica entre los extremos elegidos si $K_b=K_a$, donde $K$ es la suma de las energías cinéticas traslacionales de los dos miembros. En esta sección suponemos además $J_{\mathrm{ext}}=0$ y movimiento colineal. Usamos velocidades con signo $v_{1,a},v_{2,a},v_{1,b},v_{2,b}$, y $g=v_1-v_2$.

Una interacción conservativa puede convertir cinética en potencial durante el acercamiento y devolverla durante la separación. Para deducir $K_b=K_a$ a partir de conservación mecánica debe verificarse que la energía potencial interna tiene el mismo valor en los extremos y que no hay otros trabajos o transferencias. Conservación mecánica durante todo el proceso no significa cinética constante durante la compresión. Además, cuerpos extensos pueden retener vibración o rotación; aquí sus grados internos no se incluyen en las dos energías traslacionales.

[]{#fispm-t1-c14-p0015}

**Proposición 14.15 --- Ramas permitidas por momento y elasticidad.** Para el par colineal con impulso externo nulo, $K_b=K_a$ equivale a $g_b^2=g_a^2$. Las velocidades finales admiten la rama $g_b=g_a$, que reproduce las iniciales, y la rama $g_b=-g_a$. Para un encuentro con acercamiento no nulo y separación posterior, esta última es la rama de colisión.

**Demostración.** El momento conservado mantiene $V=P/M$ igual en ambos extremos. Proposición 14.12 expresa $K=MV^2/2+\mu g^2/2$, con $\mu>0$. Por tanto, igualdad de energías equivale a igualdad de cuadrados relativos. En números reales, $(g_b-g_a)(g_b+g_a)=0$. Si $g_b=g_a$, las fórmulas $v_1=V+(m_2/M)g$, $v_2=V-(m_1/M)g$ reproducen ambas velocidades. Si el miembro 1 está a la izquierda del 2 antes del encuentro, acercamiento significa $g_a>0$ y separación posterior significa $g_b<0$, lo que selecciona $g_b=-g_a$. Con el orden opuesto se invierten ambos signos y la misma selección vale. $\square$

El caso $g_a=0$ tiene ambas ramas coincidentes y no describe un acercamiento relativo. Los balances tampoco prueban que dos cuerpos lleguen a encontrarse: sus posiciones iniciales y la interacción determinan si el proceso ocurre. La rama trivial puede describir ausencia de encuentro; otras dinámicas también pueden devolver las velocidades iniciales. Seleccionar la rama requiere el modelo geométrico y temporal del choque, además de las ecuaciones de conservación.

[]{#fispm-t1-c14-p0016}

**Proposición 14.16 --- Velocidades finales del choque elástico colineal.** Para la rama de acercamiento y separación de la proposición 14.15,

$$v_{1,b}=\frac{m_1-m_2}{M}v_{1,a}+\frac{2m_2}{M}v_{2,a}, \qquad v_{2,b}=\frac{2m_1}{M}v_{1,a}+\frac{m_2-m_1}{M}v_{2,a}.$$

**Demostración.** Con $V=(m_1v_{1,a}+m_2v_{2,a})/M$ y $g_b=-(v_{1,a}-v_{2,a})$, la reconstrucción de la proposición 14.12 da $v_{1,b}=V-(m_2/M)(v_{1,a}-v_{2,a})$ y $v_{2,b}=V+(m_1/M)(v_{1,a}-v_{2,a})$. Agrupar coeficientes produce las fórmulas. La reconstrucción garantiza el momento inicial y proposición 14.15 garantiza la energía. $\square$

Para masas iguales se intercambian las velocidades. Eso no exige que se intercambien las posiciones o la identidad de los miembros. Para un blanco inicialmente en reposo, la primera velocidad final cambia de signo si el blanco es más pesado que el incidente; es cero para masas iguales y conserva signo si el blanco es más ligero. Estas conclusiones usan velocidades con signo, no módulos introducidos antes de resolver.

[]{#fispm-t1-c14-mp0010}

**Principio metodológico 14.10 --- Resolver sin dividir por una diferencia que puede anularse.** Conserva momento y separa la energía relativa. Factoriza la igualdad de cuadrados, conserva las dos ramas y selecciona la física mediante acercamiento y separación. Usa signos hasta el final y comprueba el resultado en ambos balances. La elasticidad es una hipótesis adicional del modelo.

[]{#ejercicios-9}

### Ejercicios {#fispm-c14-ejercicios-9}

[]{#fispm-t1-c14-e0019}

**Ejercicio 14.19.** Una masa $2m$, con velocidad $3u$ hacia la derecha, alcanza a una masa $m$ con velocidad $u$ en la misma dirección. El choque es elástico y colineal, sin impulso externo. Calcula las velocidades finales y verifica la separación.

**Solución.** $V=(6mu+mu)/(3m)=7u/3$ y $g_a=2u$. La rama física da $g_b=-2u$. Por proposición 14.16, $v_{1,b}=5u/3$ y $v_{2,b}=11u/3$. El momento final es $2m(5u/3)+m(11u/3)=7mu$. La cinética inicial es $[2m(3u)^2+mu^2]/2=19mu^2/2$ y la final $[2m(5u/3)^2+m(11u/3)^2]/2=19mu^2/2$. El miembro 2 queda más rápido y se aleja del primero, que estaba detrás. Ambos siguen hacia la derecha; separación relativa no significa velocidades absolutas opuestas.

[]{#fispm-t1-c14-e0020}

**Ejercicio 14.20.** Una partícula de masa $m$ y velocidad $u>0$ choca elásticamente en una línea con una masa $9m$ inicialmente en reposo. Calcula las velocidades y la fracción de cinética inicial transferida al blanco.

**Solución.** proposición 14.16 da $v_{1,b}=-4u/5$ y $v_{2,b}=u/5$. La energía del blanco es $9m(u/5)^2/2$, y al dividir por $mu^2/2$ se obtiene $9/25$. La partícula incidente conserva la fracción $16/25$, con velocidad invertida. Las fracciones suman uno. El blanco pesado retrocede con una velocidad positiva finita: no es exactamente una pared fija. En el límite de masa del blanco creciente, su velocidad tiende a cero y la del incidente a $-u$, manteniendo el balance del sistema material para cada masa finita.

[]{#fispm-t1-c14-e0021}

**Ejercicio 14.21.** Dos masas iguales tienen velocidades iniciales $2u$ y $-u$, con la primera a la izquierda y $u>0$. Resuelve sólo los balances de momento y energía. Identifica luego la rama que describe una colisión con separación posterior.

**Solución.** $V=u/2$, $g_a=3u$ y la igualdad cinética exige $g_b=\pm3u$. Para el signo positivo, reconstruir da $(v_{1,b},v_{2,b})=(2u,-u)$, exactamente los datos iniciales. Para el negativo, da $(-u,2u)$, intercambio de velocidades. La primera mantiene acercamiento y no describe el estado de salida de este choque; la segunda separa los miembros. Ambas satisfacen los balances. El hecho de que una solución conserve las cantidades requeridas es necesario, pero no suficiente para identificarla con la historia física declarada.

[]{#unión-y-colisiones-inelásticas}

[]{#fispm-t1-c14-s11}

[]{#fpm-i-14-s11}

## 11. Unión y colisiones inelásticas {#fispm-c14-uniuxf3n-y-colisiones-ineluxe1sticas}

Conservar momento no obliga a conservar energía cinética. Si los dos miembros terminan con la misma velocidad, el balance de momento basta para determinarla, mientras la separación cinética muestra cuánto movimiento relativo ha desaparecido. Se trata de una condición final del modelo, distinta de la elasticidad y también distinta de conservar la energía total con todos sus modos internos.[^11]

[]{#fispm-t1-c14-d0011}

**Definición 14.11 --- Unión traslacional y variación cinética.** En el modelo de la definición 14.9, una unión traslacional impone $\mathbf v_{1,b}=\mathbf v_{2,b}$. Una colisión es inelástica entre los extremos elegidos si $K_b\ne K_a$. Denotaremos $Q=K_a-K_b$ a la disminución cinética algebraica: $Q>0$ significa disminución y $Q<0$ aumento. Cuando se usa el nombre «perfectamente inelástica» para una unión, se entenderá este modelo de velocidades finales comunes.

Para cuerpos extensos, que se unan no significa que todas sus partes tengan una misma velocidad: un conjunto adherido puede rotar o vibrar. Definición 14.11 se limita al modelo traslacional de dos miembros sin esos grados adicionales. Su condición también puede cumplirse instantáneamente durante una compresión sin que haya unión permanente. Para describir adhesión posterior hace falta afirmar que los miembros permanecen juntos; la igualdad de velocidades en un solo instante no lo demuestra.

[]{#fispm-t1-c14-p0017}

**Proposición 14.17 --- Velocidad común y disminución cinética de una unión aislada.** Si el impulso externo total es cero y los miembros terminan con una velocidad común, entonces

$$\mathbf v_{1,b}=\mathbf v_{2,b}=\mathbf V_a, \qquad Q=\frac12\mu|\mathbf g_a|^2.$$

**Demostración.** La velocidad común $\mathbf w$ produce momento final $M\mathbf w$. Conservarlo da $\mathbf w=\mathbf P_a/M=\mathbf V_a$. La energía colectiva es igual en ambos extremos y la energía relativa final es cero. Restar las expresiones de la proposición 14.12 deja $Q=\mu|\mathbf g_a|^2/2$. $\square$

En el conjunto de estados de velocidad con el mismo momento, éste realiza la menor energía cinética posible por la proposición 14.11. Por eso la unión traslacional elimina toda la energía cinética relativa disponible, aunque no elimina la energía colectiva medida en el laboratorio. En un marco que se mueve con el centro, la cinética final del modelo es cero. Conservar momento es compatible con esa diferencia entre observadores, y proposición 14.14 garantiza que ambos calculan el mismo $Q$ para el par de estados aislado.

[]{#fispm-t1-c14-p0018}

**Proposición 14.18 --- Cambio cinético de un par con momento conservado.** Para cualquier estado final del mismo par con $\mathbf J_{\mathrm{ext}}=0$,

$$Q=\frac12\mu\bigl(|\mathbf g_a|^2-|\mathbf g_b|^2\bigr).$$

Por tanto, momento conservado permite tanto disminución como aumento cinético; el signo lo decide el cambio del movimiento relativo.

**Demostración.** El momento conservado mantiene $\mathbf V_b=\mathbf V_a$. Restar las energías de la proposición 14.12 cancela el término colectivo y da la fórmula. Si el módulo relativo disminuye, $Q$ es positivo; si aumenta, es negativo; si se mantiene, es cero. $\square$

Cuando $Q>0$, el balance traslacional no decide qué parte pasó a energía interna, deformación, sonido u otros modos. Llamarlo todo «calor» sin un modelo adicional sería atribuir un destino no establecido. Si el sistema completo está aislado energéticamente, la disminución cinética se compensa en sus otras formas de energía. Si hay transferencias con el exterior, deben incluirse en el balance total. Tampoco una interacción que libera energía interna contradice momento conservado cuando produce $Q<0$.

[]{#fispm-t1-c14-mp0011}

**Principio metodológico 14.11 --- Separar la captura de la evolución posterior.** En una unión, usa primero impulso y momento durante el contacto. Calcula la cinética que queda y la variación relativa. Para la etapa posterior aplica su propio balance de fuerzas o energía con nuevos datos iniciales. No prolongues conservación de momento a un intervalo donde aparecen fuerzas externas, ni conserves cinética durante una captura que impone velocidad común.

[]{#ejercicios-10}

### Ejercicios {#fispm-c14-ejercicios-10}

[]{#fispm-t1-c14-e0022}

**Ejercicio 14.22.** Una masa $m$ con velocidad $u>0$ se une a una masa $4m$ inicialmente en reposo sobre una guía horizontal lisa. El impulso externo horizontal es cero durante la captura. Calcula la velocidad común, la cinética final y la disminución cinética.

**Solución.** El momento horizontal inicial es $mu$, así que $w=u/5$. La energía final es $5m(u/5)^2/2=mu^2/10$, mientras la inicial es $mu^2/2$. Entonces $Q=2mu^2/5$, el 80% de la inicial. La masa reducida es $4m/5$ y proposición 14.17 da también $Q=\mu u^2/2=2mu^2/5$. La energía colectiva restante no se ha perdido. Si se conservara indebidamente la cinética de captura, se obtendría un módulo $u/\sqrt5$, incompatible con el momento. El destino de $Q$ necesita información sobre la unión.

[]{#fispm-t1-c14-e0023}

**Ejercicio 14.23.** Una masa $m$ llega horizontalmente con velocidad $u$ a un bloque de masa $M$ inicialmente en reposo y queda adherida. El bloque cuelga de una suspensión ideal y está en el punto más bajo. Durante el contacto breve se desprecia el impulso horizontal externo; después el conjunto sube sin resistencia hasta que su centro ha ganado altura $h$. Obtén $u$ en función de $h$ y explica qué conservación corresponde a cada etapa.

**Solución.** Durante la captura, el momento horizontal da $(M+m)w=mu$. No se conserva la cinética: la disminución es $mMu^2/[2(M+m)]$. En la subida posterior, bajo la idealización de un conjunto que se mueve como una sola masa, la suspensión no realiza trabajo y $\tfrac12(M+m)w^2=(M+m)gh$. Así $w=\sqrt{2gh}$ y $u=(M+m)\sqrt{2gh}/m$. El impulso horizontal despreciado sólo se justifica para el intervalo breve junto al punto más bajo; durante la subida la suspensión puede tener componente horizontal y no se usa conservación de momento. La energía conservada en la subida no puede aplicarse retrospectivamente como cinética conservada durante la captura. Si el conjunto retiene movimiento interno o rotación relevante, el modelo requiere términos adicionales.

[]{#restitución-y-colisiones-vectoriales}

[]{#fispm-t1-c14-s12}

[]{#fpm-i-14-s12}

## 12. Restitución y colisiones vectoriales {#fispm-c14-restituciuxf3n-y-colisiones-vectoriales}

Entre el choque elástico y la unión puede introducirse una regla para la velocidad relativa de salida. En una línea esa regla cierra el balance de momento. En varias dimensiones debe señalar además qué componente modifica y qué ocurre con las demás. El coeficiente de restitución describe una relación entre estados extremos; no reconstruye la fuerza de contacto ni su duración.[^12]

[]{#fispm-t1-c14-d0012}

**Definición 14.12 --- Restitución relativa normal.** Sea $\mathbf n$ un vector unitario orientado, durante un impacto idealizado, del miembro 2 al miembro 1. Para una velocidad relativa incidente con $g_{n,a}=\mathbf g_a\cdot\mathbf n<0$, se define el coeficiente $e$ por $g_{n,b}=-e g_{n,a}$. En el modelo pasivo usual se adopta $0\leq e\leq1$. En una línea con el miembro 1 a la izquierda del 2, esto equivale a $g_b=-e g_a$ con la convención de la definición 14.7.

La normal se trata como fija durante el impulso del modelo. Se necesita la geometría de contacto para conocerla. Si cambia apreciablemente, una sola regla escalar no sustituye la integración del contacto real. Para cuerpos con rotación, la velocidad relativa de sus puntos de contacto puede diferir de la de sus centros; las fórmulas siguientes corresponden a partículas o miembros traslacionales sin esa contribución. El rango pasivo es una hipótesis: liberación de energía interna puede producir valores efectivos mayores que uno.

[]{#fispm-t1-c14-p0019}

**Proposición 14.19 --- Restitución colineal con momento conservado.** Si $J_{\mathrm{ext}}=0$ y $g_b=-e g_a$, entonces

$$v_{1,b}=V-e\frac{m_2}{M}g_a, \qquad v_{2,b}=V+e\frac{m_1}{M}g_a, \qquad Q=\frac12\mu(1-e^2)g_a^2.$$

**Demostración.** El momento fija $V$ en ambos extremos. Sustituir $g_b=-e g_a$ en la reconstrucción de la proposición 14.12 da las velocidades. Proposición 14.18 da $Q=\mu(g_a^2-e^2g_a^2)/2$. $\square$

Para $e=1$ se obtiene la rama elástica de separación. Para $e=0$ las velocidades finales colineales coinciden; la regla por sí sola no afirma adhesión permanente. Si $e>1$, la cinética aumenta y hace falta una fuente de energía compatible con el modelo. En todos los casos el momento puede conservarse. Un único valor de $e$ medido en un encuentro no acredita que sea constante para otros materiales, velocidades o geometrías.

[]{#fispm-t1-c14-p0020}

**Proposición 14.20 --- Impulso normal sin fricción y pérdida cinética.** Supongamos impulso externo nulo, un único impulso interno $j\mathbf n$ sobre el miembro 1 y $-j\mathbf n$ sobre el 2, normal fija y restitución de la definición 14.12. Entonces

$$j=-\mu(1+e)g_{n,a},\qquad \mathbf g_b=\mathbf g_a-(1+e)g_{n,a}\mathbf n, \qquad Q=\frac12\mu(1-e^2)g_{n,a}^2.$$

La componente tangencial relativa no cambia.

**Demostración.** Los impulsos individuales dan $\Delta\mathbf v_1=j\mathbf n/m_1$ y $\Delta\mathbf v_2=-j\mathbf n/m_2$. Restarlos produce $\Delta\mathbf g=(j/\mu)\mathbf n$. Proyectar y exigir $g_{n,b}=-e g_{n,a}$ da $j/\mu=-(1+e)g_{n,a}$. Sustituir da el vector final. Su parte tangencial coincide con la inicial, mientras la normal cambia de $g_{n,a}$ a $-e g_{n,a}$. Por ortogonalidad, $|\mathbf g_a|^2-|\mathbf g_b|^2=(1-e^2)g_{n,a}^2$, y proposición 14.18 da la última fórmula. $\square$

Si $g_{n,a}<0$ y $e\geq0$, $j\geq0$: el impulso sobre el miembro 1 apunta alejándolo del 2, como corresponde a un contacto repulsivo. Para $e=0$ desaparece sólo la velocidad relativa normal; puede sobrevivir deslizamiento tangencial. Por ello no se deduce unión vectorial ni desaparición de toda la energía relativa. Si hay impulso tangencial por fricción, hace falta otra ley y proposición 14.20 deja de ser el modelo completo.

Sin normal conocida, momento y elasticidad tampoco determinan por sí solos las direcciones finales. En dos dimensiones hay cuatro componentes finales y sólo tres ecuaciones escalares independientes de esos balances, en el caso genérico. Puede especificarse una dirección o resolver la interacción. El centro de masa conserva la magnitud relativa en un choque elástico, pero la orientación de salida queda pendiente.

[]{#fispm-t1-c14-p0021}

**Proposición 14.21 --- Ortogonalidad para masas iguales con blanco en reposo.** En una colisión elástica de dos masas iguales, con impulso externo nulo y velocidad inicial del segundo miembro cero, $\mathbf v_{1,b}\cdot\mathbf v_{2,b}=0$. Si ambas velocidades finales son no nulas, sus direcciones son perpendiculares.

**Demostración.** El momento da $\mathbf v_{1,a}=\mathbf v_{1,b}+\mathbf v_{2,b}$. Tomar el cuadrado produce $|\mathbf v_{1,a}|^2=|\mathbf v_{1,b}|^2+|\mathbf v_{2,b}|^2+2\mathbf v_{1,b}\cdot\mathbf v_{2,b}$. La elasticidad identifica el primer término con la suma de los dos cuadrados finales, así que el producto es cero. Si una velocidad final es cero, sigue valiendo el producto nulo, pero su dirección no está definida. $\square$

[]{#fispm-t1-c14-mp0012}

**Principio metodológico 14.12 --- Declarar qué cierra cada componente.** Usa restitución para la componente normal indicada y una hipótesis separada para la tangencial. Comprueba el signo repulsivo del impulso y la separación final. Con impulso externo nulo, reconstruye desde el centro; sin geometría o datos suficientes, conserva explícitamente la indeterminación direccional.

[]{#ejercicios-11}

### Ejercicios {#fispm-c14-ejercicios-11}

[]{#fispm-t1-c14-e0024}

**Ejercicio 14.24.** Una masa $m$ llega con velocidad $4u$ a una masa $3m$ en reposo. El impacto colineal tiene $e=1/2$ y no recibe impulso externo. Calcula las velocidades finales y $Q$.

**Solución.** $V=u$, $g_a=4u$, $\mu=3m/4$. Proposición 14.19 da $v_{1,b}=u-(1/2)(3/4)(4u)=-u/2$ y $v_{2,b}=u+(1/2)(1/4)(4u)=3u/2$. Se verifica $g_b=-2u$ y momento final $-mu/2+9mu/2=4mu$. La cinética inicial es $8mu^2$; la final es $mu^2/8+27mu^2/8=7mu^2/2$. Así $Q=9mu^2/2$, igual a $\mu(1-1/4)(4u)^2/2$. La disminución es el 56,25% de la cinética inicial, no el 75%: este último porcentaje corresponde a la cinética relativa.

[]{#fispm-t1-c14-e0025}

**Ejercicio 14.25.** Dos masas iguales $m$ tienen $\mathbf v_{1,a}=(-2u,u)$, $\mathbf v_{2,a}=(0,0)$ y normal fija $\mathbf n=(1,0)$. El impulso es sólo normal y $e=0$. Obtén las velocidades finales y decide si hay unión traslacional.

**Solución.** $g_{n,a}=-2u$, $\mu=m/2$, de modo que $j=mu$. El primer miembro gana $(u,0)$ y el segundo pierde $(u,0)$: $\mathbf v_{1,b}=(-u,u)$ y $\mathbf v_{2,b}=(-u,0)$. Su diferencia final es $(0,u)$, tangencial y no nula. No hay unión traslacional. Proposición 14.20 da $Q=mu^2$; directamente $K_a=5mu^2/2$ y $K_b=3mu^2/2$. La cinética tangencial relativa permanece. Una restitución normal nula no autoriza poner todas las velocidades finales iguales.

[]{#fispm-t1-c14-e0026}

**Ejercicio 14.26.** Dos masas iguales en un plano tienen velocidades iniciales $(u,0)$ y cero. Se sabe que el choque es elástico y de impulso externo nulo. Exhibe dos pares finales distintos compatibles con esos balances y comprueba proposición 14.21.

**Solución.** Un par es $\mathbf v_{1,b}=0$, $\mathbf v_{2,b}=(u,0)$: conserva momento y cinética, pero no define dirección para el primer miembro. Otro es $\mathbf v_{1,b}=(u/2,u/2)$, $\mathbf v_{2,b}=(u/2,-u/2)$. Suman $(u,0)$ y sus cuadrados suman $u^2/2+u^2/2=u^2$. Su producto escalar es $u^2/4-u^2/4=0$. Ambos estados son compatibles, por lo que esos balances no eligen la dirección. El segundo también puede realizarse en el modelo normal elástico con $\mathbf n=(-1,1)/\sqrt2$: proposición 14.20 da el cambio $(-u/2,u/2)$ del primer miembro. La geometría del encuentro distingue ambos casos.

[]{#sistemas-abiertos-y-transferencia-de-masa}

[]{#fispm-t1-c14-s13}

[]{#fpm-i-14-s13}

## 13. Sistemas abiertos y transferencia de masa {#fispm-c14-sistemas-abiertos-y-transferencia-de-masa}

Proposición 14.4 suma Newton para una lista fija de miembros. Un cuerpo que incorpora o expulsa materia no conserva esa lista. La derivada de su momento puede calcularse, pero ya no coincide por sí sola con la fuerza externa: la materia que cruza lleva momento. Para obtener el balance elegimos, durante un intervalo pequeño, un conjunto material que incluye el cuerpo y las parcelas transferidas. Sólo después pasamos a la descripción abierta.[^13]

[]{#fispm-t1-c14-d0013}

**Definición 14.13 --- Modelo concentrado de transferencia.** El cuerpo retenido tiene masa $m(t)>0$ y una velocidad traslacional común $\mathbf v(t)$ en un marco inercial. Una entrada incorpora masa a tasa $q_{\mathrm{in}}\geq0$, con velocidad $\mathbf w_{\mathrm{in}}$ inmediatamente antes de transferirse; una salida retira masa a tasa $q_{\mathrm{out}}\geq0$, con velocidad $\mathbf w_{\mathrm{out}}$ al salir. Las tasas son masas por tiempo que cruzan la frontera elegida, no derivadas de masas de parcelas individuales. Se supone $\dot m=q_{\mathrm{in}}-q_{\mathrm{out}}$.

Todas las velocidades de la definición 14.13 se miden respecto del mismo laboratorio inercial. Las tasas se refieren a la frontera del cuerpo, que puede moverse. En el modelo elemental, la incorporación o expulsión se resuelve en un intervalo pequeño sin almacenamiento intermedio de masa o momento que tenga que describirse aparte. Las fuerzas aplicadas por otros agentes aportan una resultante $\mathbf F$; el intercambio entre el cuerpo y las parcelas durante la transferencia queda dentro del conjunto material usado para el balance. No se cuenta de nuevo esa interacción como una fuerza adicional sobre dicho conjunto.

[]{#fispm-t1-c14-p0022}

**Proposición 14.22 --- Balance de momento con flujo.** Bajo definición 14.13, con tasas y velocidades finitas y regularidad suficiente para el límite de primer orden,

$$\frac{d}{dt}(m\mathbf v)=\mathbf F+ q_{\mathrm{in}}\mathbf w_{\mathrm{in}}- q_{\mathrm{out}}\mathbf w_{\mathrm{out}},$$

$$m\dot{\mathbf v}=\mathbf F+ q_{\mathrm{in}}(\mathbf w_{\mathrm{in}}-\mathbf v)- q_{\mathrm{out}}(\mathbf w_{\mathrm{out}}-\mathbf v).$$

**Demostración.** Durante $dt>0$, elegimos el conjunto material formado por el cuerpo inicial y la parcela que entrará. Su momento inicial es $m\mathbf v+q_{\mathrm{in}}dt\,\mathbf w_{\mathrm{in}}+o(dt)$. Al final el conjunto se divide en el cuerpo retenido y la parcela expulsada. Su momento es $(m+\dot mdt)(\mathbf v+\dot{\mathbf v}dt)+q_{\mathrm{out}}dt\,\mathbf w_{\mathrm{out}}+o(dt)$. La fuerza aplicada entrega impulso $\mathbf Fdt+o(dt)$. Restar los momentos, dividir por $dt$ y pasar al límite da $m\dot{\mathbf v}+\dot m\mathbf v=\mathbf F+q_{\mathrm{in}}\mathbf w_{\mathrm{in}}-q_{\mathrm{out}}\mathbf w_{\mathrm{out}}$. Usar la tasa de masa de la definición 14.13 produce la segunda forma. Los productos de incrementos desaparecen por ser de orden superior. $\square$

La primera ecuación registra el momento que permanece dentro y el que cruza. La segunda destaca velocidades relativas a la materia retenida. Ambas son equivalentes, pero ninguna permite ignorar la velocidad de entrada o salida. Si se toma $\mathbf F=d(m\mathbf v)/dt$ sin flujo, se está usando el balance de otro sistema. No es una corrección de Newton para una partícula individual de masa cambiante: es un balance de pertenencia variable deducido con parcelas materiales de masa constante.

Con varias entradas o salidas se suman sus términos. Para un flujo con distribución de velocidades, el momento transportado requiere su promedio ponderado por la tasa de masa. Un cuerpo extendido con movimiento interno exige también una descripción más amplia que una única $\mathbf v$. Presiones, fuerzas de superficies y almacenamiento interno deben incorporarse cuando sean relevantes; el modelo concentrado no es una fórmula universal para toda corriente de fluido.

Las dos ecuaciones son compatibles con un cambio galileano. En la primera, $\mathbf v'=\mathbf v-\mathbf U$ cambia el lado izquierdo en $-\dot m\mathbf U$; el flujo cambia en $-(q_{\mathrm{in}}-q_{\mathrm{out}})\mathbf U$, igual por la definición 14.13. En la segunda las diferencias de velocidades ya son invariantes y la aceleración no cambia. La constancia de $m$ que exigía proposición 14.14 falta aquí: las comparaciones cinéticas de sistemas abiertos necesitan incluir el flujo energético y no se deducen de aquella fórmula para un par material fijo.

[]{#fispm-t1-c14-p0023}

**Proposición 14.23 --- Cohete ideal en una línea.** Un cuerpo sin entrada expulsa masa a tasa $q>0$, con velocidad relativa de salida $-c$, donde $c>0$ es constante. Si no hay otras fuerzas aplicadas y $m>0$, entonces

$$m\dot v=qc=-c\dot m, \qquad v_b-v_a=c\ln\frac{m_a}{m_b}.$$

**Demostración.** La salida tiene velocidad de laboratorio $w_{\mathrm{out}}=v-c$ y $\dot m=-q$. Proposición 14.22 da $m\dot v=-q[(v-c)-v]=qc=-c\dot m$. Dividir por $m>0$ e integrar produce $\int dv=-c\int dm/m=c\ln(m_a/m_b)$. $\square$

El aumento de velocidad no depende de la tasa temporal para esta idealización sin fuerza externa y con $c$ constante. El momento del cohete solo sí cambia; se conserva el del conjunto material que incluye todo el gas eyectado si está aislado. La energía para acelerar las partes procede del mecanismo de expulsión y no se impone conservación de cinética del cohete. Añadir una «fuerza del chorro» a la derecha de la proposición 14.22 cuando ya se incluyó su velocidad de salida contaría dos veces el mismo intercambio. Puede usarse una descripción por fuerza efectiva en lugar del flujo, siempre que se deduzca coherentemente y se evite esa duplicación.

Si la masa sale con la misma velocidad del cuerpo, $\mathbf w_{\mathrm{out}}=\mathbf v$, no produce aceleración por ese flujo en el modelo. El momento retenido disminuye porque contiene menos masa, aunque la velocidad permanezca constante. Esta situación se diferencia de recibir materia en reposo respecto del laboratorio: la incorporación obliga a cambiar su momento y puede reducir la velocidad del cuerpo si no hay fuerza aplicada.

[]{#fispm-t1-c14-mp0013}

**Principio metodológico 14.13 --- Seguir la materia que cruza.** Declara la frontera, las tasas positivas de entrada y salida y sus velocidades en un mismo marco. Construye un conjunto material para el intervalo pequeño y deriva el flujo antes de simplificar. Distingue masa retenida de masa total del conjunto ampliado. No combines flujo y una fuerza efectiva que represente otra vez la misma transferencia.

[]{#ejercicios-12}

### Ejercicios {#fispm-c14-ejercicios-12}

[]{#fispm-t1-c14-e0027}

**Ejercicio 14.27.** Un carro de masa inicial $m_0$ se mueve horizontalmente con velocidad $v_0$. Incorpora materia a tasa constante $q>0$, con velocidad horizontal de entrada $w$ constante. No hay fuerza aplicada horizontal y toda la materia capturada acaba con la velocidad del carro. Obtén $v(t)$ y determina qué momento se conserva si $w=0$.

**Solución.** $m=m_0+qt$ y proposición 14.22 da $d(mv)/dt=qw$. Integrar produce $mv=m_0v_0+qwt$ y $v(t)=(m_0v_0+qwt)/(m_0+qt)$. También $m\dot v=q(w-v)$, por lo que el carro tiende hacia $w$ mientras aumenta su masa. Si $w=0$, el momento horizontal de la materia retenida es $m_0v_0$, constante en este caso particular de entrada con momento horizontal nulo. Esa coincidencia no valida ignorar el flujo en general: para $w\ne0$ el momento retenido varía. Conservar cinética daría otra historia incorrecta para una captura. Las fuerzas verticales que sostienen el carro quedan fuera de este balance horizontal; $q$ se ha dado como tasa real de incorporación en su frontera móvil.

[]{#fispm-t1-c14-e0028}

**Ejercicio 14.28.** Un cohete ideal asciende en un campo uniforme de aceleración $-g$, sin resistencia. Parte con masa $m_0$ y velocidad $v_0$, expulsa a tasa constante $q>0$ y rapidez relativa $c>0$ hacia abajo. La masa seca es $m_d>0$. Obtén su velocidad durante la combustión y compara dos duraciones con igual masa inicial y final y el mismo $c$.

**Solución.** La fuerza aplicada es $-mg$ y $m=m_0-qt$. Proposición 14.22 da $\dot v=cq/(m_0-qt)-g$. Integrar produce $v(t)=v_0+c\ln[m_0/(m_0-qt)]-gt$, para $0\leq t\leq(m_0-m_d)/q$, suponiendo que sigue vigente el modelo de ascenso y expulsión. Para iguales masas extremas, $\Delta v=c\ln(m_0/m_b)-gT$: la duración mayor deja menor velocidad final por el término gravitatorio, aunque la contribución de expulsión sea la misma. Después de agotar el combustible, $q=0$ y la ecuación cambia. No se prolonga el logaritmo hasta masa cero ni se infiere de este modelo una tasa físicamente ilimitada de combustión. Si hay apoyo del suelo antes del despegue, su fuerza debe incluirse durante esa etapa.

[]{#síntesis-del-método}

[]{#fispm-t1-c14-s14}

[]{#fpm-i-14-s14}

## 14. Síntesis del método {#fispm-c14-suxedntesis-del-muxe9todo}

El balance de momento compara una suma vectorial y un impulso externo. El centro de masa convierte esa suma en una velocidad colectiva. La energía cinética añade información sobre el movimiento relativo, pero su cambio requiere conocer el modelo de interacción y las transferencias energéticas. En una colisión, estos tres elementos se combinan sin intercambiar sus hipótesis; en un sistema abierto se añade el momento transportado por la materia.[^14]

[]{#fispm-t1-c14-p0024}

**Proposición 14.24 --- Separación del cambio cinético con impulso externo.** Para el par material de la definición 14.9, sin exigir que el impulso externo se anule, sea $\overline{\mathbf V}=(\mathbf V_a+\mathbf V_b)/2$. Entonces

$$\Delta K=\overline{\mathbf V}\cdot\mathbf J_{\mathrm{ext}} +\frac12\mu\bigl(|\mathbf g_b|^2-|\mathbf g_a|^2\bigr).$$

**Demostración.** proposición 14.12 da $\Delta K=M(|\mathbf V_b|^2-|\mathbf V_a|^2)/2+\mu(|\mathbf g_b|^2-|\mathbf g_a|^2)/2$. La diferencia de cuadrados colectivos es $(\mathbf V_b+\mathbf V_a)\cdot(\mathbf V_b-\mathbf V_a)$. Por proposiciones 14.4--14.9, $M(\mathbf V_b-\mathbf V_a)=\mathbf J_{\mathrm{ext}}$. Sustituir produce el primer término indicado. $\square$

La proposición es una identidad entre estados. El producto de la velocidad media de los extremos y el impulso no representa en general el trabajo físico de las fuerzas externas sobre sus puntos de aplicación. Sí representa exactamente el cambio de la energía cinética colectiva. Para masa constante, integrar $\mathbf V\cdot\mathbf F_{\mathrm{ext}}$ también da ese cambio, pero el trabajo externo real puede incluir movimiento de los miembros respecto del centro. El balance de trabajo del capítulo 12 conserva esa información adicional.

Esta distinción impide deducir que «impulso externo nulo» significa «trabajo externo nulo». Un par puede recibir fuerzas externas opuestas que mantengan su centro mientras cambian la separación y la energía relativa. También fuerzas internas opuestas pueden modificar esa energía sin modificar el momento total. La resultante y la potencia son sumas distintas: una suma de fuerzas cero no obliga a que sus productos con velocidades diferentes sumen cero.

El recorrido de resolución puede organizarse según lo que se necesita determinar:

  Pregunta                          Balance o información necesaria                                 Límite de la conclusión
  --------------------------------- --------------------------------------------------------------- -------------------------------------------------
  Cambio de momento total           Impulso externo sobre un sistema material fijo                  No fija velocidades relativas
  Trayectoria del centro            Resultante externa, posición y velocidad colectivas iniciales   Necesita cierre de la resultante
  Velocidades finales de un par     Momento y ley relativa de la interacción                        Balances solos pueden dejar ramas o direcciones
  Cambio de cinética                Movimiento colectivo y relativo, o trabajo y energía            Momento conservado no conserva cinética
  Movimiento con entrada o salida   Tasas y velocidades de transferencia, fuerzas aplicadas         La lista material retenida cambia

En todos los casos los datos iniciales deben pertenecer al mismo marco. La velocidad de expulsión respecto de un dispositivo o la velocidad relativa de separación de dos miembros son diferencias de velocidades, no velocidades de laboratorio. Convertirlas antes de resolver evita una inconsistencia que puede pasar inadvertida en un cálculo dimensionalmente correcto. También debe conservarse la orientación elegida de cada coordenada relativa.

[]{#fispm-t1-c14-mp0014}

**Principio metodológico 14.14 --- Cerrar sólo con información acreditada.** Define primero sistema, marco, intervalo y datos. Escribe el balance de momento con todos los impulsos o flujos relevantes. Decide después qué ecuación determina el movimiento relativo: fuerza, elasticidad, unión, restitución o datos medidos. Comprueba signos, unidades, estados extremos y energía, y conserva explícitas las variables que siguen indeterminadas. Separa etapas si cambian fuerzas, pertenencia material o modelo de contacto.

[]{#ejercicios-13}

### Ejercicios {#fispm-c14-ejercicios-13}

[]{#fispm-t1-c14-e0029}

**Ejercicio 14.29.** Dos masas $m$ y $2m$ tienen velocidades colineales iniciales $3u$ y cero, y finales cero y $u$, con $u>0$. Calcula el impulso externo requerido por esos datos y separa el cambio cinético mediante proposición 14.24. ¿Son compatibles con un choque aislado?

**Solución.** $P_a=3mu$, $P_b=2mu$ y por tanto $J_{\mathrm{ext}}=-mu$. No son compatibles con impulso externo nulo. Las velocidades colectivas son $V_a=u$, $V_b=2u/3$, así que $\overline VJ=(5u/6)(-mu)=-5mu^2/6$. La masa reducida es $2m/3$, $g_a=3u$ y $g_b=-u$, por lo que el término relativo es $(m/3)(u^2-9u^2)=-8mu^2/3$. Suman $-7mu^2/2$, igual a $K_b-K_a=mu^2-9mu^2/2$. El cociente de rapidez relativa de salida y entrada es $1/3$, pero no permite aplicar proposición 14.19: sus fórmulas también exigían momento conservado. El impulso total conocido tampoco dice cómo se distribuyó entre los miembros ni cuál fue la fuerza interna.

[]{#fispm-t1-c14-e0030}

**Ejercicio 14.30.** Dos masas $m$ y $2m$, inicialmente en reposo en una línea, reciben fuerzas externas constantes $F_1=f>0$ y $F_2=-f$ durante un tiempo $T$. No interactúan internamente en ese intervalo. Calcula las velocidades finales, el centro y la energía. Determina si el producto de la proposición 14.24 puede identificarse aquí con el trabajo externo total.

**Solución.** Newton da $v_{1,b}=fT/m$ y $v_{2,b}=-fT/(2m)$. La resultante externa es cero durante todo el intervalo, así que $P=0$ y el centro permanece en su posición inicial. La energía final es $f^2T^2/(2m)+f^2T^2/(4m)=3f^2T^2/(4m)$, positiva. Toda es relativa: $\mu=2m/3$ y $g_b=3fT/(2m)$ producen $\mu g_b^2/2=3f^2T^2/(4m)$. Los desplazamientos son $fT^2/(2m)$ y $-fT^2/(4m)$, de modo que el trabajo externo total es $f[fT^2/(2m)]+(-f)[-fT^2/(4m)]=3f^2T^2/(4m)$. En proposición 14.24 el término colectivo vale cero porque $J_{\mathrm{ext}}=0$; por ello no coincide con ese trabajo externo positivo. El ejemplo conserva momento y modifica cinética mediante agentes externos que actúan a velocidades distintas.

La reducción al centro de masa conserva la información de traslación, y la reducción de dos partículas conserva además la coordenada relativa necesaria para reconstruirlas. Cuando se estudien momentos angulares y cuerpos rígidos habrá que describir otras partes del movimiento. El balance lineal seguirá siendo válido bajo sus hipótesis, pero no reemplazará las ecuaciones que gobiernen esas variables.

[^1]: Kleppner--Kolenkow, *An Introduction to Mechanics*, copia Cambridge University Press, 2010, cap. 3, §3.1, pp. 111--113; Morin, *Introduction to Classical Mechanics*, Cambridge University Press, 2008, cap. 5, §5.5.1, pp. 156--157. La equivalencia con Newton se prueba aquí para masa constante y marco inercial.

[^2]: Kleppner--Kolenkow, obra citada, cap. 3, §3.4, pp. 130--132; Morin, obra citada, cap. 5, §5.5.1, p. 157, ecuación 5.48. Se desarrolla la cota del impulso y se distingue fuerza total de fuerza de contacto, sin atribuir el pico a partir de la media.

[^3]: Kleppner--Kolenkow, obra citada, cap. 3, §3.2, pp. 113--115; Morin, obra citada, cap. 5, §5.5.1, pp. 156--157. La suma se hace para una lista material fija y masas constantes; la distinción entre suma de fuerzas y suma de potencias enlaza con el capítulo 12.

[^4]: Kleppner--Kolenkow, obra citada, cap. 3, §3.3, pp. 122--123; Morin, obra citada, cap. 5, §5.5.1, p. 157. Los ejemplos usan sistema material fijo y velocidades en un mismo marco; el dato relativo del retroceso se convierte explícitamente.

[^5]: Kleppner--Kolenkow, obra citada, cap. 3, §3.2, pp. 116--118. Las propiedades afines, la agrupación y la cota convexa se demuestran aquí para un sistema material finito de masas positivas constantes.

[^6]: Kleppner--Kolenkow, obra citada, cap. 3, §3.2, pp. 116--118; Morin, obra citada, cap. 5, §5.6.1, pp. 161--162. El cierre en campos uniformes o afines y el contraejemplo cúbico se desarrollan explícitamente a partir de la suma de fuerzas.

[^7]: Morin, obra citada, cap. 5, §§5.6.1--5.6.2, pp. 161--163. Se explicita la diferencia entre un cambio galileano de velocidad constante y coordenadas centradas aceleradas; la identidad cinética se prueba sin confundir ambos casos.

[^8]: Desarrollo original por reconstrucción afín, Newton y proposición 14.11. La separación cinética emplea el marco conceptual consultado en Morin, cap. 5, §§5.6.1--5.6.2, pp. 161--163; las ecuaciones con fuerzas externas se deducen aquí sin suponer colisión ni conservación cinética.

[^9]: Kleppner--Kolenkow, obra citada, cap. 3, §3.4, pp. 130--132, y cap. 4, §4.14, pp. 187--189; Morin, obra citada, cap. 5, §§5.5.1 y 5.7.1, pp. 156--157 y 164--165. Las cotas se aplican al balance colectivo y la transformación cinética se deduce en el texto para masa material constante.

[^10]: Kleppner--Kolenkow, obra citada, cap. 4, §4.14, pp. 188--191; Morin, obra citada, cap. 5, §5.7.1, pp. 164--165. La prueba utiliza la energía relativa y conserva explícitamente la rama trivial, sin dividir por cambios de velocidad posiblemente nulos.

[^11]: Kleppner--Kolenkow, obra citada, cap. 4, §4.14, pp. 188--189; Morin, obra citada, cap. 5, §5.8, pp. 167--168. La disminución se expresa mediante energía relativa y se distingue de una atribución automática a calor; la unión se limita al modelo traslacional declarado.

[^12]: Kleppner--Kolenkow, obra citada, cap. 4, §4.14, pp. 190--194; Morin, obra citada, cap. 5, §5.7.2, pp. 166--167. Los pasajes fundamentan la descripción vectorial, la libertad direccional y la separación en el centro de masa. La regla de restitución normal se declara como modelo adicional y sus fórmulas se deducen aquí por impulso; no se atribuye a esas fuentes una ley universal de contacto.

[^13]: Kleppner--Kolenkow, obra citada, cap. 3, §3.5, pp. 133--139; Morin, obra citada, cap. 5, §5.5.2, pp. 159--160. Se usa un conjunto material durante la transferencia y velocidades de un marco inercial. Las tasas se definen positivas y el escape del cohete tiene velocidad relativa $-c$, evitando mezclar convenciones de signo.

[^14]: Síntesis de las demostraciones del capítulo, con bases consultadas en Kleppner--Kolenkow, cap. 3, §§3.2--3.5, y cap. 4, §4.14; Morin, cap. 5, §§5.5--5.8. Proposición 14.24 se deduce localmente de la proposición 14.4, proposición 14.9 y proposición 14.12; su término colectivo se distingue explícitamente del trabajo externo real sobre los miembros.
