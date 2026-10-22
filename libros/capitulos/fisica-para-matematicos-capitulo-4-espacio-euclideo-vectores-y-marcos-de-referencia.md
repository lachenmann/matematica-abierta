---
title: "Espacio euclídeo, vectores y marcos de referencia"
subtitle: "Física para matemáticos · Tomo I · Capítulo 4"
author: "A. Peña"
description: "Capítulo 4 del Tomo I de Física para matemáticos, con ejercicios y soluciones desarrolladas."
content-id: MA-BCH-0344
source-id: FISPM-T1-C04
editorial-id: FPM-I-04
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
date-modified: 2026-10-17
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0343"]
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

[Capítulo 3](fisica-para-matematicos-capitulo-3-medicion-incertidumbre-estimacion-y-ordenes-de-magnitud.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos-v04-archivo.md#tomo-i-fundamentos-y-mecanica) · [Capítulo 5](fisica-para-matematicos-capitulo-5-tiempo-movimiento-y-curvas.md)

[]{#fispm-c04-espacio-eucluxeddeo-vectores-y-marcos-de-referencia}

[]{#un-punto-no-es-un-vector}

[]{#fispm-t1-c04-s01}

[]{#fpm-i-04-s01}

## 1. Un punto no es un vector {#fispm-c04-un-punto-no-es-un-vector}

[]{#la-pregunta-física-antes-de-las-coordenadas}

### La pregunta física antes de las coordenadas {#fispm-c04-la-pregunta-fuxedsica-antes-de-las-coordenadas}

Dos personas describen el mismo objeto. Una coloca el origen de una regla en el extremo izquierdo de una mesa; la otra lo sitúa un metro a su derecha. Sus números para la posición del objeto difieren. Sin embargo, **el objeto no se ha desplazado por el mero cambio de origen**. Este hecho invita a separar tres objetos distintos:

[]{#fig:I-04-N01}

<figure id="fig-fpm-v04-i-04-n01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-04-N01.svg" class="lightbox" data-gallery="fpm-v04-c04"><img src="/assets/books/fispm/v04/I-04-N01.svg" alt="Composición de desplazamientos. Diagrama del capítulo 4; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="275" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 4.1.** Los puntos son extremos y las flechas son desplazamientos: $\overrightarrow{PQ}+\overrightarrow{QR}=\overrightarrow{PR}$. La identidad no requiere elegir un origen. Véase §[1](#fispm-c04-un-punto-no-es-un-vector).

</figcaption>

</figure>

- el **punto** $P$ donde se encuentra el objeto;

- el **origen** $O$ que elegimos para describirlo;

- el **desplazamiento** desde $O$ hasta $P$.

El número que asignamos a una posición requiere una convención. La diferencia geométrica entre dos puntos puede expresarse sin privilegiar un origen.[^1]

Activación Si una persona cambia de habitación la regla con la que mide, ¿se desplaza también el objeto medido? ¿Qué cambió realmente en el procedimiento de descripción?

[]{#representar-puntos-y-flechas-de-desplazamiento}

### Representar: puntos y flechas de desplazamiento {#fispm-c04-representar-puntos-y-flechas-de-desplazamiento}

Imaginemos tres puntos $O,P,Q$ sobre una recta, en ese orden. La flecha de $O$ a $P$ y la flecha de $P$ a $Q$ pueden componerse para dar la flecha de $O$ a $Q$.

$$\overrightarrow{OP}+\overrightarrow{PQ}=\overrightarrow{OQ}.$$

La suma en esta expresión es una suma de **desplazamientos**, no una suma de puntos. Los tres puntos sirven como extremos; las flechas pertenecen a otro tipo de objeto matemático. El dibujo sugiere la ley, pero todavía tenemos que definir la estructura que permite demostrarla.

[]{#definir-espacio-afín}

### Definir: espacio afín {#fispm-c04-definir-espacio-afuxedn}

Un espacio vectorial real $V$ permite sumar vectores y multiplicarlos por escalares reales. Para este capítulo trabajaremos con un espacio vectorial de dimensión tres, aunque las primeras identidades no dependen de esa dimensión.

**Definición 4.1 --- Espacio afín real** Un espacio afín $\mathcal E$ modelado sobre el espacio vectorial real $V$ es un conjunto no vacío de puntos junto con una operación de traslación

$$\mathcal E\times V\longrightarrow\mathcal E, \qquad(P,v)\longmapsto P+v,$$

que satisface: $P+0=P,\qquad (P+u)+v=P+(u+v),$

y para cada par $P,Q\in\mathcal E$ existe un **único** $v\in V$ tal que $P+v=Q$.

Las dos primeras condiciones hacen coherente la traslación por varios desplazamientos. La última garantiza que, entre dos puntos, existe exactamente un vector de desplazamiento. Hipótesis y alcance Esta es una **idealización geométrica** del espacio físico clásico, no una conclusión empírica obtenida por definición. La conveniencia de esa idealización debe contrastarse con el fenómeno y la escala considerados, tal como exige capítulo 1.

[]{#definir-desplazamiento-entre-puntos}

### Definir: desplazamiento entre puntos {#fispm-c04-definir-desplazamiento-entre-puntos}

**Definición 4.2 --- Desplazamiento** Dados $P,Q\in\mathcal E$, definimos $\overrightarrow{PQ}\in V$ como el único vector que satisface

$$P+\overrightarrow{PQ}=Q.$$

En particular, $\overrightarrow{PQ}$ no es el punto $Q$ y no necesita elegir ningún origen global. Es un vector libre cuya interpretación puede ser longitud y dirección cuando añadamos la métrica euclídea. La notación $Q-P$ puede usarse como abreviatura de $\overrightarrow{PQ}$, pero **sólo como diferencia de dos puntos**. No debe interpretarse como una resta entre dos vectores de posición previamente identificados sin origen.

[]{#primera-prueba-la-ley-del-triángulo}

### Primera prueba: la ley del triángulo {#fispm-c04-primera-prueba-la-ley-del-triuxe1ngulo}

**Proposición 4.1 --- Identidades de desplazamiento** En todo espacio afín $\mathcal E$ modelado sobre $V$, para cualesquiera puntos $P,Q,R$:

$$\overrightarrow{PP}=0, \qquad \overrightarrow{QP}=-\overrightarrow{PQ},$$

y

$$\boxed{\overrightarrow{PQ}+\overrightarrow{QR}=\overrightarrow{PR}.}$$

**Demostración.** Por la identidad $P+0=P$ y la unicidad del vector que lleva $P$ a sí mismo, se obtiene $\overrightarrow{PP}=0$. Por definición, $P+\overrightarrow{PQ}=Q$. Trasladamos este punto por el vector opuesto:

$$Q+(-\overrightarrow{PQ}) =(P+\overrightarrow{PQ})+(-\overrightarrow{PQ}) =P.$$

La unicidad del desplazamiento de $Q$ a $P$ implica $\overrightarrow{QP}=-\overrightarrow{PQ}$. Finalmente,

$$P+(\overrightarrow{PQ}+\overrightarrow{QR}) =(P+\overrightarrow{PQ})+\overrightarrow{QR} =Q+\overrightarrow{QR}=R.$$

Como $\overrightarrow{PR}$ es el único vector que lleva $P$ a $R$, ambos deben coincidir. $\square$ **Autoexplicación de la prueba.** El mecanismo no usa una figura particular ni componentes: utiliza la compatibilidad de traslaciones y, al final, la unicidad exigida en la definición 4.1. Por eso la ley vale antes de introducir bases o coordenadas.

[]{#por-qué-no-podemos-sumar-dos-puntos}

### ¿Por qué no podemos sumar dos puntos? {#fispm-c04-por-quuxe9-no-podemos-sumar-dos-puntos}

En $V$ sí existe la operación

$$V\times V\longrightarrow V, \qquad (u,v)\longmapsto u+v.$$

En cambio, definición 4.1 no ofrece ninguna operación intrínseca

$$\mathcal E\times\mathcal E\longrightarrow\mathcal E$$

que merezca llamarse suma de puntos. La expresión $P+Q$ no está definida por nuestra estructura. En contraste, $P+v$ sí está definida y es un punto; $Q-P$ sí está definida y es un vector.

Error plausible «Si dibujé un punto como $(2,3)$ y otro como $(4,5)$, puedo sumarlos y obtener $(6,8)$; por tanto, sumar puntos es una operación geométrica». La terna o pareja numérica ya presupone un origen y ejes; la suma obtenida depende de esa convención. No demuestra la existencia de una suma canónica de puntos.

[]{#el-origen-es-una-elección-no-una-propiedad-del-punto}

### El origen es una elección, no una propiedad del punto {#fispm-c04-el-origen-es-una-elecciuxf3n-no-una-propiedad-del-punto}

**Definición 4.3 --- Origen y vector de posición** Elegido un punto $O\in\mathcal E$ como **origen**, el vector de posición de $P$ relativo a $O$ es

$$r_O(P):=\overrightarrow{OP}\in V.$$

El subíndice recuerda que se eligió un punto de referencia. La elección permite construir una correspondencia entre puntos y vectores, pero no los convierte retroactivamente en objetos idénticos.

**Principio metodológico 4.1 --- Un punto no es un vector** Antes de escribir una posición como un vector o una terna, declarar el origen y, cuando correspondan, los ejes y las unidades.

[]{#segunda-prueba-cambiar-el-origen}

### Segunda prueba: cambiar el origen {#fispm-c04-segunda-prueba-cambiar-el-origen}

Tomemos un origen nuevo $O'=O+a$, donde $a\in V$. Entonces $\overrightarrow{OO'}=a.$ La ley del triángulo aplicada a $O',O,P$ da $\overrightarrow{O'O}+\overrightarrow{OP}=\overrightarrow{O'P}.$ Como $\overrightarrow{O'O}=-a$, obtenemos

$$\boxed{r_{O'}(P)=r_O(P)-a.}$$

La posición **representada** cambia en un vector constante $-a$ para todos los puntos. La geometría no exige que los puntos se hayan movido.

**Proposición 4.2 --- Invariancia del desplazamiento respecto del origen** Para cualesquiera $P,Q,O,O'\in\mathcal E$,

$$\boxed{r_O(Q)-r_O(P)=r_{O'}(Q)-r_{O'}(P)=\overrightarrow{PQ}.}$$

**Demostración.** proposición 4.1 da $r_O(P)+\overrightarrow{PQ}=r_O(Q)$, luego la primera igualdad. Si $a=\overrightarrow{OO'}$, la fórmula de cambio de origen da

$$\begin{aligned} r_{O'}(Q)-r_{O'}(P) &=\bigl(r_O(Q)-a\bigr)-\bigl(r_O(P)-a\bigr)\\ &=r_O(Q)-r_O(P) =\overrightarrow{PQ}. \end{aligned}$$

Por tanto la diferencia entre posiciones es independiente del origen. $\square$

**Principio metodológico 4.2 --- Invariancia frente al origen** Una representación numérica de posición puede cambiar al trasladar el origen; un desplazamiento entre los mismos dos puntos no cambia por esa sola elección.

[]{#ejemplo-físico-dos-personas-describen-el-mismo-desplazamiento}

### Ejemplo físico: dos personas describen el mismo desplazamiento {#fispm-c04-ejemplo-fuxedsico-dos-personas-describen-el-mismo-desplazamiento}

En un modelo unidimensional, asignemos respecto de $O$ las posiciones $x_O(P)=2\,\mathrm m$ y $x_O(Q)=7\,\mathrm m$. La diferencia es $5\,\mathrm m$ hacia el sentido positivo elegido. Si el nuevo origen se sitúa $a=3\,\mathrm m$ a la derecha de $O$, entonces

$$x_{O'}(P)=-1\,\mathrm m, \qquad x_{O'}(Q)=4\,\mathrm m,$$

y

$$x_{O'}(Q)-x_{O'}(P)=5\,\mathrm m.$$

En este ejemplo sólo cambió el origen; los ejes conservaron orientación y unidad. Un cambio de base modificará también las **componentes** de los desplazamientos y se estudiará en §10. No debemos inferir de esta invariancia del desplazamiento que todos los marcos físicos sean equivalentes desde el punto de vista dinámico. Ese problema requiere una teoría del movimiento y leyes físicas posteriores.

[]{#prueba-de-estrés-de-las-definiciones}

### Prueba de estrés de las definiciones {#fispm-c04-prueba-de-estruxe9s-de-las-definiciones}

- **¿Pueden coincidir los vectores de posición del mismo punto respecto de dos orígenes diferentes?** No: $r_{O'}(P)=r_O(P)-a$; si los vectores coinciden, entonces $a=0$ y, por la definición 4.1, $O'=O$. La coincidencia de sus *componentes numéricas* en bases diferentes es una cuestión distinta que trataremos en §10.

- **¿Puede definirse $\overrightarrow{PQ}$ sin producto escalar?** Sí: definición 4.2 sólo necesita traslaciones.

- **¿Puede definirse una distancia sólo con la definición 4.1?** No: falta una noción de longitud en $V$; se introducirá mediante el producto escalar.

- **¿Puede sumarse $P+v$?** Sí, da un punto.

- **¿Puede sumarse $P+Q$ sólo con la definición 4.1?** No.

La pregunta de qué hace especial a una geometría **euclídea**, en vez de meramente afín, se responderá al introducir longitud y ángulos.

### ¿Tiene sentido sumar dos puntos? {#fispm-c04-e001-tiene-sentido-sumar-dos-puntos .unnumbered}

[]{#fispm-t1-c04-e0004}

**Ejercicio 4.1 · Diagnóstico lógico y contraejemplo** Un estudiante elige coordenadas en una recta y asigna a dos puntos $P,Q$ los números $2$ y $5$. Afirma: «su suma es el punto de coordenada $7$; es independiente del origen». Cambia el origen tres unidades hacia la derecha y examina la afirmación.

**Solución desarrollada** Con el origen inicial, las coordenadas son $2$ y $5$ y su suma informal es $7$. Con el origen desplazado tres unidades, las coordenadas son $-1$ y $2$, cuya suma es $1$. Si $7$ describía un punto fijo, con el origen nuevo debería tener coordenada $4$, no $1$. La operación propuesta no respeta el cambio de origen y no pertenece a la estructura afín. En cambio, la diferencia pasa de $5-2=3$ a $2-(-1)=3$: el desplazamiento sí es invariante.

### Cambiar el origen sin mover el objeto {#fispm-c04-e002-cambiar-el-origen-sin-mover-el-objeto .unnumbered}

**Ejercicio 4.2 · Representación, formalización e invariancia** Respecto de un origen $O$, dos puntos de una recta tienen coordenadas $x_O(P)=-2\,\mathrm m$ y $x_O(Q)=4\,\mathrm m$. Se elige un origen $O'$ situado $5\,\mathrm m$ a la izquierda de $O$, sin invertir el eje. Calcula las coordenadas nuevas y el desplazamiento $\overrightarrow{PQ}$ en ambas descripciones.

**Solución desarrollada** El desplazamiento del origen nuevo respecto del antiguo tiene componente $a=-5\,\mathrm m$. Por $x_{O'}=x_O-a$,

$$x_{O'}(P)=3\,\mathrm m, \qquad x_{O'}(Q)=9\,\mathrm m.$$

Las diferencias son $4-(-2)=6\,\mathrm m, \qquad 9-3=6\,\mathrm m.$ El vector desplazamiento es el mismo, y su componente permanece $+6\,\mathrm m$ porque no se cambió ni orientación ni unidad de la base.

### Reconstruir un triángulo de desplazamientos {#fispm-c04-e003-reconstruir-un-triuxe1ngulo-de-desplazamientos .unnumbered}

**Ejercicio 4.3 · Prueba y transferencia** Si $\overrightarrow{AB}=u$ y $\overrightarrow{BC}=v$, expresa $\overrightarrow{AC}$, $\overrightarrow{CA}$ y $\overrightarrow{CB}$. Calcula luego la suma cerrada $\overrightarrow{AB}+\overrightarrow{BC}+\overrightarrow{CA}$ sin asignar coordenadas a los puntos.

**Solución desarrollada** Por proposición 4.1,

$$\overrightarrow{AC}=u+v, \qquad \overrightarrow{CA}=-(u+v), \qquad \overrightarrow{CB}=-v.$$

Por tanto,

$$\overrightarrow{AB}+\overrightarrow{BC}+\overrightarrow{CA} =u+v-(u+v)=0.$$

El vector total de un recorrido cerrado es nulo en un espacio afín: el cálculo sólo emplea las reglas de desplazamiento, no una figura ni un origen privilegiado.

[]{#cierre-conceptual-del-lugar-a-la-estructura}

### Cierre conceptual: del lugar a la estructura {#fispm-c04-cierre-conceptual-del-lugar-a-la-estructura}

Hemos probado que una **posición** expresada por $r_O(P)$ depende de un origen, mientras que el desplazamiento $\overrightarrow{PQ}$ es geométricamente independiente de él. Ésta es la primera invariancia que necesitaremos para comparar observadores.

$$\boxed{\text{puntos}\;\xrightarrow{\text{diferencia}}\;\text{vectores de desplazamiento}}$$

En §2 construiremos sistemáticamente las operaciones afines y la geometría del paralelogramo. Sólo después introduciremos bases y coordenadas, y luego el producto escalar que permite hablar rigurosamente de longitudes y ángulos.

[]{#la-estructura-afín-de-los-desplazamientos}

[]{#fispm-t1-c04-s02}

[]{#fpm-i-04-s02}

## 2. La estructura afín de los desplazamientos {#fispm-c04-la-estructura-afuxedn-de-los-desplazamientos}

[]{#activación-dónde-está-el-punto-medio-si-nadie-fija-el-origen}

### Activación: ¿dónde está el punto medio si nadie fija el origen? {#fispm-c04-activaciuxf3n-duxf3nde-estuxe1-el-punto-medio-si-nadie-fija-el-origen}

Dos marcas físicas ocupan puntos $P,Q\in\mathcal E$. Para indicar una marca intermedia podemos elegir momentáneamente un origen $O$ y calcular el promedio de sus vectores de posición: $r_O(M)=\frac12r_O(P)+\frac12r_O(Q).$ Pero $O$ es una elección. ¿Cambiará el punto $M$ si otro observador coloca su origen en otro lugar? ¿Por qué este promedio sería admisible, mientras que la «suma de puntos» de §1 no lo era? La respuesta exigirá comprobar la **dependencia de la construcción respecto del origen**; una ilustración de dos marcas sobre una regla sugiere dónde situar $M$, pero no demuestra esa independencia.

[]{#fig:I-04-R01}

<figure id="fig-fpm-v04-i-04-r01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-04-R01.svg" class="lightbox" data-gallery="fpm-v04-c04"><img src="/assets/books/fispm/v04/I-04-R01.svg" alt="La composición de desplazamientos. Diagrama del capítulo 4; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="290" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 4.2.** Si $u=\overrightarrow{AB}$ y $v=\overrightarrow{BC}$, entonces $u+v=\overrightarrow{AC}$. El paralelogramo compara la composición de desplazamientos con su representación vectorial. Véase §[2](#fispm-c04-la-estructura-afuxedn-de-los-desplazamientos).

</figcaption>

</figure>

[]{#recuperar-la-estructura-disponible-trasladar-restar-componer}

### Recuperar la estructura disponible: trasladar, restar, componer {#fispm-c04-recuperar-la-estructura-disponible-trasladar-restar-componer}

De definición 4.1 sabemos que la traslación $P+v$ es un punto cuando $v\in V$. De definición 4.2 y proposición 4.1:

$$\overrightarrow{PQ}+\overrightarrow{QR}=\overrightarrow{PR}, \qquad \overrightarrow{QP}=-\overrightarrow{PQ}.$$

Por consiguiente, sí tienen significado intrínseco

$$P+u,\qquad Q-P:=\overrightarrow{PQ}, \qquad \overrightarrow{PQ}+\overrightarrow{QR},$$

pero **no** $P+Q$. La estructura distingue expresiones por su tipo: punto, vector o escalar. Esta disciplina permite construir nuevos puntos sin identificar puntos y vectores.

[]{#una-receta-tentativa-con-varios-puntos}

### Una receta tentativa con varios puntos {#fispm-c04-una-receta-tentativa-con-varios-puntos}

Sean $P_1,\ldots,P_n\in\mathcal E$ y $\lambda_1,\ldots,\lambda_n\in\mathbb R$. Si elegimos un origen auxiliar $O$, la receta

$$A_O:=O+\sum_{i=1}^{n}\lambda_i\overrightarrow{OP_i}$$

produce un punto: la suma del lado derecho pertenece a $V$ y puede trasladar $O$. Sin embargo, que la fórmula produzca **algún** punto no demuestra que produzca el **mismo** punto para todos los orígenes. Trabajo cognitivo Si trasladamos el origen por $a$, cada vector $\overrightarrow{OP_i}$ cambia en $-a$. ¿Cuántas veces aparece esa corrección en la suma? Antes de calcular, predice qué condición sobre los coeficientes puede cancelarla.

[]{#proposición-fundamental-el-origen-desaparece-si-y-sólo-si-la-suma-es-uno}

### Proposición fundamental: el origen desaparece si y sólo si la suma es uno {#fispm-c04-proposiciuxf3n-fundamental-el-origen-desaparece-si-y-suxf3lo-si-la-suma-es-uno}

**Proposición 4.3 --- Criterio de independencia del origen** Sean $P_1,\ldots,P_n\in\mathcal E$, $\lambda_i\in\mathbb R$ y

$$A_O=O+\sum_i\lambda_i\overrightarrow{OP_i}.$$

Si $O'=O+a$, entonces

$$\boxed{\overrightarrow{A_OA_{O'}}= \left(1-\sum_i\lambda_i\right)a.}$$

En particular, $A_O$ es independiente del origen elegido si $\sum_i\lambda_i=1$. Recíprocamente, como $\dim V=3$ y existen traslaciones no nulas, si $A_O$ es independiente de **toda** elección de origen, necesariamente $\sum_i\lambda_i=1$.

**Demostración.** La fórmula de §1 da $\overrightarrow{O'P_i}=\overrightarrow{OP_i}-a$. Sustituyendo en la receta:

$$\begin{aligned} A_{O'} &=O'+\sum_i\lambda_i\overrightarrow{O'P_i}\\ &=(O+a)+\sum_i\lambda_i(\overrightarrow{OP_i}-a)\\ &=A_O+\left(1-\sum_i\lambda_i\right)a. \end{aligned}$$

Definición 4.2 identifica el vector que lleva $A_O$ a $A_{O'}$ con el término entre paréntesis. Si $\sum_i\lambda_i=1$, ese vector es cero para todo $a$. Inversamente, si es cero para todo $a$, escogemos $a\ne0$ y usamos que un escalar multiplicado por un vector no nulo sólo da cero cuando el escalar vale cero. Por tanto $1-\sum_i\lambda_i=0$. $\square$ **Lectura guiada.** La demostración tiene una estrategia (cambiar el origen), un mecanismo (cada vector de posición incorpora $-a$) y un cierre (unicidad del desplazamiento). No se necesitó ninguna fórmula de distancia.

[]{#definir-correctamente-una-combinación-afín}

### Definir correctamente una combinación afín {#fispm-c04-definir-correctamente-una-combinaciuxf3n-afuxedn}

**Definición 4.4 --- Combinación afín de puntos** Dados $P_1,\ldots,P_n\in\mathcal E$ y escalares $\lambda_1,\ldots,\lambda_n$ con $\sum_i\lambda_i=1$, su **combinación afín** es el punto único

$$\boxed{A=O+\sum_i\lambda_i\overrightarrow{OP_i},}$$

donde $O$ es cualquier origen auxiliar. Proposición 4.3 asegura que el punto no depende de esa elección. La expresión abreviada $\sum_i\lambda_iP_i$ se permite **exclusivamente** después de declarar esta definición, y nunca como suma vectorial ordinaria de puntos.

Podemos usar un punto de la propia familia como origen. Para $O=P_1$:

$$\boxed{A=P_1+\sum_{i=2}^{n}\lambda_i\overrightarrow{P_1P_i}.}$$

Esta fórmula ya no necesita elegir un origen exterior a los puntos y facilita los cálculos conceptuales.

**Principio metodológico 4.3 --- Comprobar los tipos y los coeficientes** Antes de combinar puntos, verificar que los coeficientes sumen uno. Antes de sumar, verificar que los sumandos sean vectores; antes de trasladar, verificar que el primer objeto sea un punto y el segundo un vector.

[]{#ejemplos-no-ejemplos-y-cambio-de-origen}

### Ejemplos, no-ejemplos y cambio de origen {#fispm-c04-ejemplos-no-ejemplos-y-cambio-de-origen}

Con dos puntos,

$$A=(1-t)P+tQ=P+t\overrightarrow{PQ}, \qquad t\in\mathbb R,$$

es una combinación afín válida para **todo** $t$, incluso $t<0$ o $t>1$. Por el contrario, la receta $P+Q$ interpretada como «dos posiciones sumadas» tendría coeficientes $1+1=2$; proposición 4.3 muestra que la construcción basada en un origen variaría al trasladarlo. Ejemplo de valores numéricos en una recta ---usados sólo como comprobación de §1, no como definición de coordenadas generales---: si los valores respecto de un origen provisional son $0\,\mathrm m$ y $10\,\mathrm m$, entonces para $t=\tfrac34$ obtenemos $7.5\,\mathrm m$. Trasladando el origen $3\,\mathrm m$ hacia la derecha, los valores de los mismos puntos son $-3\,\mathrm m$ y $7\,\mathrm m$:

$$\frac14(-3)+\frac34(7)=4.5\,\mathrm m.$$

El nuevo valor es $4.5\,\mathrm m$ respecto del nuevo origen, equivalente a $7.5\,\mathrm m$ respecto del antiguo. Cambió la descripción numérica, no el punto obtenido.

[]{#definir-el-baricentro-sin-confundirlo-con-un-promedio-de-puntos}

### Definir el baricentro sin confundirlo con un promedio de puntos {#fispm-c04-definir-el-baricentro-sin-confundirlo-con-un-promedio-de-puntos}

**Definición 4.5 --- Baricentro de pesos de suma no nula** Dados puntos $P_i$ y pesos escalares $w_i$ compatibles entre sí, con suma $W=\sum_iw_i\ne0$, definimos el **baricentro** como la combinación afín

$$\boxed{G=O+\sum_i\frac{w_i}{W}\overrightarrow{OP_i}.}$$

Los coeficientes $w_i/W$ son adimensionales y suman uno; proposición 4.3 garantiza que $G$ es independiente de $O$. Si los pesos representan masas, deben expresarse en unidades compatibles antes de sumarlos. Para dos masas positivas $m_P,m_Q$, colocando $u=\overrightarrow{PQ}$: $G=P+\frac{m_Q}{m_P+m_Q}u.$

Como $m_P,m_Q>0$, los coeficientes $m_P/(m_P+m_Q)$ y $m_Q/(m_P+m_Q)$ están entre $0$ y $1$; en §2.9 formalizaremos esta situación diciendo que $G$ pertenece al segmento afín entre $P$ y $Q$. Pero **definición 4.5 admite también pesos negativos** siempre que $W\ne0$; tal baricentro es una construcción geométrica y no debe interpretarse automáticamente como el centro de masa de cuerpos ordinarios.

[]{#qué-sucede-cuando-la-suma-de-los-pesos-es-cero}

### ¿Qué sucede cuando la suma de los pesos es cero? {#fispm-c04-quuxe9-sucede-cuando-la-suma-de-los-pesos-es-cero}

Si $W=0$, la normalización $w_i/W$ está indefinida. No es una dificultad de la calculadora ni una invitación a escoger arbitrariamente un origen. En cambio, el vector ponderado

$$S_O:=\sum_iw_i\overrightarrow{OP_i}$$

sí es independiente del origen, porque

$$S_{O'}=S_O-Wa=S_O.$$

Esto produce un **vector**, no un baricentro. Para $w_1=1$, $w_2=-1$, resulta $S_O=\overrightarrow{P_2P_1}$; no aparece un punto privilegiado. Prueba de hipótesis La condición $W\ne0$ es esencial para definición 4.5. Que una suma ponderada de vectores permanezca bien definida cuando $W=0$ no autoriza a llamarla punto.

[]{#definir-el-segmento-afín-y-su-punto-medio}

### Definir el segmento afín y su punto medio {#fispm-c04-definir-el-segmento-afuxedn-y-su-punto-medio}

**Definición 4.6 --- Segmento afín y punto medio** Para $P,Q\in\mathcal E$, el segmento afín entre ellos es

$$[P,Q]_{\mathrm{af}}:=\{P+t\overrightarrow{PQ}:0\le t\le1\}.$$

Su **punto medio** es el punto

$$\boxed{M(P,Q):=P+\tfrac12\overrightarrow{PQ}.}$$

La fórmula del punto medio equivale a la combinación afín de coeficientes $1/2,1/2$. Si $P=Q$, el segmento consta de un solo punto y el punto medio coincide con él. No estamos utilizando todavía una distancia: «mitad» significa aquí la mitad del **vector de desplazamiento**. Cuando $t\in[0,1]$, los coeficientes $(1-t),t$ no sólo suman uno: son no negativos. Ésta es una **combinación convexa**. Si $t$ queda fuera del intervalo, la fórmula sigue siendo afín, pero el punto ya no pertenece al segmento definido, salvo el caso degenerado $P=Q$.

[]{#comprobación-la-interpolación-no-depende-del-origen}

### Comprobación: la interpolación no depende del origen {#fispm-c04-comprobaciuxf3n-la-interpolaciuxf3n-no-depende-del-origen}

Sea $X_t=P+t\overrightarrow{PQ}$. Para cualquier origen $O$: $r_O(X_t)=(1-t)r_O(P)+tr_O(Q).$ Esto se deduce de la proposición 4.1 y proposición 4.2: $r_O(Q)-r_O(P)=\overrightarrow{PQ}$. La igualdad representa un punto en función de dos vectores de posición, pero **la definición intrínseca** sigue siendo $P+t\overrightarrow{PQ}$. Además, para $s,t\in\mathbb R$,

$$\boxed{\overrightarrow{X_sX_t}=(t-s)\overrightarrow{PQ}.}$$

Se verifica trasladando $X_s$ por $(t-s)\overrightarrow{PQ}$ y usando la unicidad de la definición 4.1. Si $P\ne Q$, dos parámetros distintos dan puntos distintos. Si $P=Q$, todos los parámetros producen el mismo punto: no hay unicidad de parámetro en el segmento degenerado.

[]{#un-paralelogramo-construido-con-desplazamientos}

### Un paralelogramo construido con desplazamientos {#fispm-c04-un-paralelogramo-construido-con-desplazamientos}

Fijemos un punto $A$ y dos vectores $u,v\in V$. Construyamos sucesivamente

$$B=A+u,\qquad D=A+v,\qquad C=A+u+v.$$

Entonces

$$\overrightarrow{AB}=u=\overrightarrow{DC}, \qquad \overrightarrow{AD}=v=\overrightarrow{BC}.$$

Ésta es la ley del paralelogramo **como identidad afín**, no como consecuencia de medir lados o ángulos. Los pares de lados opuestos representan el mismo desplazamiento libre. Cuando $u$ y $v$ no producen cuatro vértices geométricamente distintos, la construcción puede degenerar; no se necesita introducir todavía independencia lineal ni un producto escalar para que las identidades sean válidas.

[]{#proposición-el-paralelogramo-y-sus-diagonales}

### Proposición: el paralelogramo y sus diagonales {#fispm-c04-proposiciuxf3n-el-paralelogramo-y-sus-diagonales}

**Proposición 4.4 --- Paralelogramo, desplazamientos y puntos medios** Sean $A,B,D\in\mathcal E$. Hay un único punto $C$ tal que

$$\overrightarrow{BC}=\overrightarrow{AD} \quad\text{y}\quad \overrightarrow{DC}=\overrightarrow{AB}.$$

Ese punto es $C=B+\overrightarrow{AD}$ y se caracteriza también por

$$\boxed{M(A,C)=M(B,D).}$$

Recíprocamente, si cuatro puntos $A,B,C,D$ satisfacen esa igualdad de puntos medios, cumplen las identidades de lados opuestos anteriores.

**Demostración.** Escribamos $u=\overrightarrow{AB}$ y $v=\overrightarrow{AD}$. El punto $C=A+u+v=B+v=D+u$ existe. Su unicidad se deduce de la unicidad del traslado de $B$ por $v$. Para los puntos medios:

$$M(A,C)=A+\frac{u+v}{2}.$$

Como $\overrightarrow{BD}=v-u$,

$$M(B,D)=B+\frac{v-u}{2} =A+u+\frac{v-u}{2} =A+\frac{u+v}{2}.$$

Para la recíproca supongamos $M(A,C)=M(B,D)$; tomando $A$ sólo como punto auxiliar y escribiendo $u=\overrightarrow{AB}$, $v=\overrightarrow{AD}$, $w=\overrightarrow{AC}$, se obtiene

$$A+\frac{w}{2}=A+u+\frac{v-u}{2} =A+\frac{u+v}{2}.$$

La unicidad de traslación y la aritmética vectorial implican $w=u+v$. Por tanto $C=A+u+v=B+v=D+u$, que da las dos identidades. $\square$ **Autoexplicación.** El paralelogramo no se define mediante una ilustración de cuatro lados «aparentemente paralelos»; su construcción y su criterio de diagonales se obtienen de la acción afín. Las relaciones métricas sobre las longitudes de las diagonales quedan reservadas para §5.

[]{#aplicación-geométrica-y-frontera-física}

### Aplicación geométrica y frontera física {#fispm-c04-aplicaciuxf3n-geomuxe9trica-y-frontera-fuxedsica}

Tres marcas $A,B,D$ permiten definir una cuarta posición por dos rutas conceptualmente equivalentes: $C=B+\overrightarrow{AD}=D+\overrightarrow{AB}.$

Si un trazado real no hace coincidir físicamente ambas marcas construidas, eso no refuta la identidad afín: invita a estudiar errores de realización, idealización, procedimiento o incertidumbre, conforme al capítulo 3. La identidad pertenece al **modelo exacto**; el traslado y la localización físicos requieren procedimientos. No estamos afirmando que cambiar el origen, recorrer un desplazamiento o representar un paralelogramo determine la evolución temporal de un cuerpo. La cinemática comienza en el capítulo 5.

[]{#prueba-de-estrés-baricentro-segmento-y-promedios}

### Prueba de estrés: baricentro, segmento y promedios {#fispm-c04-prueba-de-estruxe9s-baricentro-segmento-y-promedios}

1.  Si $\lambda_1+\lambda_2=1$ pero uno es negativo, la combinación es afín, aunque no necesariamente pertenece al segmento.

2.  Si dos pesos tienen suma nula, definición 4.5 no define un baricentro; puede quedar definido un vector ponderado.

3.  Para puntos coincidentes $P=Q$, el punto medio existe y coincide con ellos; el parámetro del segmento deja de ser único.

4.  En un paralelogramo degenerado, proposición 4.4 sigue siendo verdadero; no supone longitudes ni ángulos.

5.  No escribiremos $\tfrac12(P+Q)$: contiene una suma de puntos que definición 4.1 no define. La expresión correcta es $M(P,Q)=P+\tfrac12\overrightarrow{PQ}$, o bien la combinación afín definida en la definición 4.4.

Lectura inversa Dado un punto $G$ descrito como «centro», reconstruye qué pesos se eligieron, si suman un valor no nulo, qué fenómeno representan y si la construcción es geométrica o metrológica.

**Ejercicio 4.4 --- Baricentro con un origen auxiliar.**

**Función cognitiva:** `modelización → traducción vectorial → prueba de invariancia`.

Sean $P,Q,R\in\mathcal E$ y $u=\overrightarrow{PQ}$, $v=\overrightarrow{PR}$. Tres pesos de la misma unidad son $2,3,1$.

1.  Calcula el baricentro $G$ mediante definición 4.5, con $P$ como origen auxiliar.

2.  Repite el cálculo con un origen genérico $O$ y demuestra que describe el mismo punto.

3.  Explica por qué el cociente de cada peso respecto de la suma no conserva la unidad de los pesos.

**Solución desarrollada**

La suma es $W=6$ y los coeficientes afines son $\tfrac26,\tfrac36,\tfrac16$. Con $P$ como origen auxiliar, $\overrightarrow{PP}=0$:

$$\boxed{G=P+\frac12u+\frac16v.}$$

Para otro origen $O$, escribimos $r_O(Q)=r_O(P)+u$ y $r_O(R)=r_O(P)+v$. Entonces

$$\begin{aligned} r_O(G)&=\frac26r_O(P)+\frac36r_O(Q)+\frac16r_O(R)\\ &=r_O(P)+\frac12u+\frac16v. \end{aligned}$$

Dado que el último vector traslada $P$ al punto obtenido antes, las dos descripciones coinciden. Cada razón $w_i/W$ es adimensional, porque numerador y denominador tienen la misma unidad. La positividad de los pesos permite interpretarlos como masas **si** se declara un modelo físico adecuado; no convierte por sí sola esta identidad en una medición del centro de masa.

[]{#fispm-t1-c04-e0005}

**Ejercicio 4.5 --- Construir y auditar un paralelogramo.**

**Función cognitiva:** `construcción → demostración → detección de errores`.

Dados un punto $A$ y desplazamientos $u,v$, define $B=A+u$ y $D=A+v$.

1.  Construye el único $C$ que cumple las dos igualdades de lados opuestos de la proposición 4.4.

2.  Demuestra que ambas diagonales tienen el mismo punto medio.

3.  Un compañero propone $C'=A+u-v$. Determina para qué $v$ esa propuesta es correcta.

**Solución desarrollada**

Por construcción y proposición 4.4,

$$\boxed{C=A+u+v=B+v=D+u.}$$

Los puntos medios de $AC$ y $BD$ son, respectivamente,

$$M(A,C)=A+\frac{u+v}{2},$$

$$M(B,D)=B+\frac{v-u}{2} =A+\frac{u+v}{2}.$$

Para que $C'=C$ se requiere $u-v=u+v$, o $2v=0$. Sobre un espacio vectorial real esto equivale a $v=0$: el error sólo desaparece en el caso degenerado $D=A$. Confundir un vector con su opuesto cambia la construcción, aunque un dibujo mal orientado pueda ocultarlo.

[]{#cierre-y-red-matemática}

### Cierre y red matemática {#fispm-c04-cierre-y-red-matemuxe1tica}

La estructura afín permite obtener nuevos puntos **sin declarar un origen absoluto**. Las operaciones que acabamos de construir se organizan así:

$$\boxed{\begin{gathered} \text{puntos y desplazamientos}\ \xrightarrow{\text{definiciones 4.1--4.2}}\ \text{traslaciones}\\ \xrightarrow{\text{proposición 4.3}}\ \text{combinaciones afines y baricentros}\\ \xrightarrow{\text{definición 4.6, proposición 4.4}}\ \text{segmentos y paralelogramos}. \end{gathered}}$$

No obstante, aún no sabemos expresar **cualquier vector de manera única mediante unas direcciones elegidas**. Ésa será la pregunta de §3 --- *Vectores, independencia y bases*. La métrica euclídea seguirá esperando hasta §5.

[]{#vectores-independencia-y-bases}

[]{#fispm-t1-c04-s03}

[]{#fpm-i-04-s03}

## 3. Vectores, independencia y bases {#fispm-c04-vectores-independencia-y-bases}

[]{#activación-una-flecha-distintas-descripciones}

### Activación: una flecha, distintas descripciones {#fispm-c04-activaciuxf3n-una-flecha-distintas-descripciones}

Dos personas registran el mismo desplazamiento físico. Una escoge tres desplazamientos de referencia; la otra escoge otros tres. Sus listas de números pueden diferir sin que cambie el desplazamiento. ¿Cuándo una lista describe un vector de manera completa y sin ambigüedad? La §1 enseñó que $\overrightarrow{PQ}\in V$ no es ni $P$ ni $Q$; la §2 mostró que las sumas y múltiplos escalares corresponden a **vectores**, mientras que combinar puntos exige coeficientes que sumen uno. Ahora estudiaremos cómo expresar cualquier elemento de $V$ a partir de vectores de referencia. La dificultad tiene dos mitades distintas:

- **Existencia:** ¿nuestros vectores de referencia alcanzan para construir cualquier desplazamiento?

- **Unicidad:** ¿cada desplazamiento posee una única receta en términos de ellos?

Un sistema puede satisfacer una mitad y fallar en la otra.

Activación Si tenemos tres instrucciones de desplazamiento pero una de ellas es la suma de las otras dos, ¿obtenemos información nueva? ¿Podrían dos listas numéricas diferentes representar la misma flecha?

[]{#la-estructura-vectorial-ya-disponible}

### La estructura vectorial ya disponible {#fispm-c04-la-estructura-vectorial-ya-disponible}

El espacio real $V$ dispone de una suma $u+v$ y una multiplicación por escalares $\lambda u$. Emplearemos las leyes vectoriales conocidas: asociatividad y conmutatividad de la suma, vector cero, opuestos y distributividad. Para $P\in\mathcal E$, la expresión $P+v$ sigue representando la traslación de un **punto** por un **vector**. Por proposición 4.1, una sucesión de desplazamientos satisface $\overrightarrow{PQ}+\overrightarrow{QR}=\overrightarrow{PR}.$

Que podamos componer flechas no significa que exista una suma intrínseca de puntos. Las combinaciones lineales que definiremos pertenecen siempre a $V$. La dimensión $\dim V=3$ forma parte del modelo del capítulo. Esto significa que existe alguna terna de vectores que constituye una base; **no** significa que cualquier terna no nula lo sea. No necesitamos una métrica para comprender esta dimensión algebraica.

[]{#definir-combinación-lineal-y-espacio-generado}

### Definir: combinación lineal y espacio generado {#fispm-c04-definir-combinaciuxf3n-lineal-y-espacio-generado}

**Definición 4.7 --- Combinación lineal y subespacio generado** Para vectores $v_1,\ldots,v_k\in V$ y escalares $a_1,\ldots,a_k\in\mathbb R$, la expresión

$$a_1v_1+\cdots+a_kv_k$$

es una **combinación lineal**. El conjunto de todas las combinaciones lineales de la familia es

$$\operatorname{span}(v_1,\ldots,v_k) :=\left\{\sum_{i=1}^{k}a_iv_i:a_i\in\mathbb R\right\}.$$

Diremos que la familia **genera** $V$ si su espacio generado coincide con $V$. La familia de un solo vector no nulo genera los vectores de la forma $av$; dos vectores generan los de la forma $au+bw$. Sólo si la familia genera $V$ podremos representar **todo** desplazamiento del modelo.

¿Por qué se llama subespacio? La combinación con todos los coeficientes nulos produce $0$. Si $x=\sum a_iv_i$ e $y=\sum b_iv_i$, entonces $x+y=\sum(a_i+b_i)v_i$ y $cx=\sum(ca_i)v_i$. Así, el conjunto generado contiene el cero y es cerrado bajo suma y multiplicación escalar. No hemos usado longitudes ni ángulos.

[]{#dos-pruebas-de-estrés-para-la-generación}

### Dos pruebas de estrés para la generación {#fispm-c04-dos-pruebas-de-estruxe9s-para-la-generaciuxf3n}

**Familia demasiado pequeña.** Si $u\ne0$, la familia $(u)$ puede representar $2u$ o $-u$, pero no tiene por qué representar cualquier vector de $V$. En un espacio de dimensión tres, su espacio generado es estrictamente menor que $V$. **Familia con instrucciones redundantes.** Añadir $u+v$ a $(u,v)$ no aumenta lo generado:

$$\operatorname{span}(u,v,u+v)=\operatorname{span}(u,v).$$

En efecto, toda combinación $au+bv+c(u+v)$ se reescribe como $(a+c)u+(b+c)v$, y las combinaciones de $(u,v)$ se obtienen tomando $c=0$. La segunda familia tiene más elementos, pero no permite construir vectores adicionales. La cantidad de instrucciones no mide por sí sola la información geométrica.

[]{#fispm-c04-definir-independencia-lineal label="fispm-c04-definir-independencia-lineal"}

**Definición 4.8 --- Independencia lineal** Una familia $(v_1,\ldots,v_k)$ es **linealmente independiente** si

$$\sum_{i=1}^{k}a_iv_i=0 \quad\Longrightarrow\quad a_1=\cdots=a_k=0.$$

Si existen coeficientes, no todos nulos, que producen $0$, la familia es **linealmente dependiente**.

¿Por qué estudiar precisamente una combinación que vale cero? Porque una relación de este tipo permite modificar los coeficientes de una representación sin cambiar el vector obtenido. Algunos no-ejemplos inmediatos: una familia que contiene $0$ es dependiente; una familia en la que se repite un vector es dependiente; la terna $(u,v,u+v)$ es dependiente, pues

$$u+v-(u+v)=0.$$

En particular, que *todos* los vectores de una familia sean no nulos no basta para garantizar independencia.

[]{#la-pregunta-correcta-cuántas-recetas-tiene-el-mismo-vector}

### La pregunta correcta: ¿cuántas recetas tiene el mismo vector? {#fispm-c04-la-pregunta-correcta-cuuxe1ntas-recetas-tiene-el-mismo-vector}

Una familia dependiente proporciona una relación $\sum_i c_iv_i=0$

con algún $c_i\ne0$. Si $w=\sum_i a_iv_i$, entonces también

$$w=\sum_i(a_i+tc_i)v_i$$

para cualquier $t\in\mathbb R$. Si $t\ne0$, la segunda lista de coeficientes es distinta de la primera. Por el contrario, si una familia es independiente, dos listas que representen el mismo vector han de coincidir. Este razonamiento merece una demostración general.

[]{#proposición-independencia-y-unicidad-en-el-espacio-generado}

### Proposición: independencia y unicidad en el espacio generado {#fispm-c04-proposiciuxf3n-independencia-y-unicidad-en-el-espacio-generado}

**Proposición 4.5 --- Caracterización de la independencia por unicidad** Para una familia finita $(v_1,\ldots,v_k)$, son equivalentes:

1.  La familia es linealmente independiente.

2.  Cada vector de $\operatorname{span}(v_1,\ldots,v_k)$ tiene **una única** representación como $\sum_i a_iv_i$.

**Demostración.** Supongamos independencia y que un vector admite dos expresiones:

$$\sum_i a_iv_i=\sum_i b_iv_i.$$

Restando, $\sum_i(a_i-b_i)v_i=0.$

Por independencia, $a_i-b_i=0$ para cada $i$; las listas son iguales. Recíprocamente, supongamos unicidad dentro del espacio generado. El vector $0$ admite la representación con todos los coeficientes nulos. Si $\sum_i c_iv_i=0$, ésta es otra representación de $0$ y, por unicidad, necesariamente $c_i=0$ para todos los índices. La familia es independiente. $\square$ **Lectura guiada.** La estrategia es convertir «dos representaciones» en «una relación que da cero»; la técnica es restarlas; el mecanismo es aplicar definición 4.8. La recíproca prueba la definición examinando exclusivamente las representaciones del vector cero.

[]{#definir-base}

### Definir: base {#fispm-c04-definir-base}

**Definición 4.9 --- Base de un espacio vectorial** Una familia ordenada $B=(e_1,\ldots,e_n)$ es una **base** de $V$ si cumple simultáneamente:

- **generación:** $\operatorname{span}(e_1,\ldots,e_n)=V$;

- **independencia:** $\sum_i a_ie_i=0$ sólo cuando todos los $a_i$ son cero.

En nuestro modelo tridimensional consideraremos bases ordenadas $B=(e_1,e_2,e_3)$. El orden es necesario al escribir componentes: intercambiar $e_1$ y $e_2$ cambia el orden de los números, aunque la colección de vectores siga siendo una base. Un conjunto que sólo genera puede contener instrucciones redundantes. Una familia independiente que no genera no describe todos los desplazamientos. **Una base resuelve los dos problemas a la vez.**

[]{#proposición-el-teorema-fundamental-de-las-representaciones-en-una-base}

### Proposición: el teorema fundamental de las representaciones en una base {#fispm-c04-proposiciuxf3n-el-teorema-fundamental-de-las-representaciones-en-una-base}

**Proposición 4.6 --- Existencia y unicidad de los coeficientes en una base** Sea $B=(e_1,\ldots,e_n)$ una familia finita de vectores. Es una base de $V$ **si y sólo si** cada $v\in V$ posee una única representación

$$\boxed{v=\sum_{i=1}^{n}v^ie_i.}$$

**Demostración.** Si $B$ es una base, la condición de generación asegura la existencia para todo $v$. Proposición 4.5, aplicada a la independencia de $B$, asegura la unicidad. Inversamente, si cada $v\in V$ posee una representación de la forma indicada, $B$ genera $V$. La unicidad para todo $v$, y en particular para los vectores del espacio generado, implica independencia por la proposición 4.5. Ambas condiciones de la definición 4.9 se cumplen. $\square$

**Principio metodológico 4.4 --- Separar existencia de unicidad** Antes de llamar *base* a una familia, demostrar por separado que todo vector se puede construir con ella y que no existen dos listas distintas de coeficientes para un mismo vector. Una sola comprobación numérica no sustituye ninguna de estas pruebas.

[]{#definir-las-componentes-de-un-vector}

### Definir: las componentes de un vector {#fispm-c04-definir-las-componentes-de-un-vector}

**Definición 4.10 --- Componentes relativas a una base** Sea $B=(e_1,e_2,e_3)$ una base ordenada de $V$. Para el vector único

$$v=v^1e_1+v^2e_2+v^3e_3,$$

definimos su columna de **componentes en $B$** como

$$\boxed{[v]_B=\begin{pmatrix}v^1\\v^2\\v^3\end{pmatrix}.}$$

Proposición 4.6 garantiza que esta notación no es ambigua. La columna es un elemento de $\mathbb R^3$; $v$ sigue siendo un elemento de $V$. La igualdad $v=[v]_B$ **no** es una igualdad de objetos tipados como hemos definido, aunque una identificación dependiente de $B$ permita realizar cálculos con la columna.

Punto, vector y columna $P\in\mathcal E$, $\overrightarrow{PQ}\in V$ y $[\overrightarrow{PQ}]_B\in\mathbb R^3$ son objetos distintos. Un origen hará posible representar puntos mediante vectores de posición; esa operación se estudiará sistemáticamente en §4.

[]{#proposición-la-aplicación-de-componentes-respeta-las-operaciones}

### Proposición: la aplicación de componentes respeta las operaciones {#fispm-c04-proposiciuxf3n-la-aplicaciuxf3n-de-componentes-respeta-las-operaciones}

**Proposición 4.7 --- Correspondencia lineal de componentes** Fijada una base $B=(e_1,e_2,e_3)$, la aplicación

$$C_B:V\longrightarrow\mathbb R^3, \qquad C_B(v)=[v]_B$$

es biyectiva y lineal. En particular,

$$\boxed{[au+bv]_B=a[u]_B+b[v]_B.}$$

**Demostración.** Dados $v=\sum_i v^ie_i$ y $w=\sum_i w^ie_i$, las leyes vectoriales dan

$$av+bw=\sum_i(av^i+bw^i)e_i.$$

Por la unicidad de la proposición 4.6, sus componentes son precisamente $(av^i+bw^i)_{i=1}^3$. Esto prueba la linealidad. Para cada columna $(c^1,c^2,c^3)^{\mathsf T}$, el vector $\sum_i c^ie_i$ tiene esa columna: $C_B$ es sobreyectiva. Si dos vectores tienen igual columna, sus expresiones en la base son idénticas y los vectores coinciden: $C_B$ es inyectiva. $\square$ **Autoexplicación.** Una columna es útil porque conserva la suma y la multiplicación escalar. Pero su forma numérica depende de la base; la correspondencia se define **después** de elegir $B$, no antes.

[]{#ejemplo-construido-una-base-no-tiene-por-qué-ser-la-primera-que-vemos}

### Ejemplo construido: una base no tiene por qué ser la primera que vemos {#fispm-c04-ejemplo-construido-una-base-no-tiene-por-quuxe9-ser-la-primera-que-vemos}

Sea $E=(e_1,e_2,e_3)$ una base conocida de un espacio de dimensión tres. Definamos

$$b_1=e_1,\qquad b_2=e_1+e_2,\qquad b_3=e_1+e_2+e_3.$$

Para un vector cualquiera

$$v=ae_1+be_2+ce_3,$$

buscamos escalares $x,y,z$ tales que $v=xb_1+yb_2+zb_3$. Al reordenar:

$$xb_1+yb_2+zb_3 =(x+y+z)e_1+(y+z)e_2+ze_3.$$

La unicidad de las componentes relativas a $E$ obliga a resolver

$$x+y+z=a,\qquad y+z=b,\qquad z=c.$$

El sistema se despeja desde la última ecuación:

$$\boxed{z=c,\qquad y=b-c,\qquad x=a-b.}$$

Existe una solución para todo $v$ y es única; por la proposición 4.6, $B=(b_1,b_2,b_3)$ es una base. **No hemos utilizado determinantes, producto escalar ni ortogonalidad.** Para $v=2e_1+3e_2+4e_3$:

$$[v]_E=\begin{pmatrix}2\\3\\4\end{pmatrix}, \qquad [v]_B=\begin{pmatrix}-1\\-1\\4\end{pmatrix}.$$

Las columnas son diferentes, pero ambas reconstruyen el mismo vector. La teoría general de cambios de base, incluida su convención matricial, aparecerá en §10.

[]{#contraejemplo-tres-vectores-que-no-forman-base}

### Contraejemplo: tres vectores que no forman base {#fispm-c04-contraejemplo-tres-vectores-que-no-forman-base}

Con $E$ como antes, elijamos

$$u=e_1+e_2,\qquad w=e_2+e_3, \qquad z=u+w=e_1+2e_2+e_3.$$

Los tres vectores son no nulos, pero

$$u+w-z=0$$

es una relación no trivial. Además, para el propio vector $z$ tenemos dos representaciones: $z=0u+0w+1z=1u+1w+0z.$ No son componentes legítimas de una base, porque la unicidad falla. Tampoco generan todo $V$: si $e_1=\alpha u+\beta w$, la comparación de coeficientes en $E$ daría $\alpha=1$, $\alpha+\beta=0$ y $\beta=0$, un sistema contradictorio.

Error plausible «Tres vectores no nulos en un espacio tridimensional forman automáticamente una base». Es falso: el problema no es contar flechas, sino verificar independencia y generación. El contraejemplo falla en ambas condiciones.

[]{#cambiar-la-escala-de-un-vector-de-referencia}

### Cambiar la escala de un vector de referencia {#fispm-c04-cambiar-la-escala-de-un-vector-de-referencia}

Si $B=(e_1,e_2,e_3)$ es una base y $s\in\mathbb R$ con $s\ne0$, entonces $B'=(se_1,e_2,e_3)$ también es una base: toda representación $v=v^1e_1+v^2e_2+v^3e_3$ se reescribe unívocamente como $v=\frac{v^1}{s}(se_1)+v^2e_2+v^3e_3.$ Por tanto,

$$\boxed{[v]_{B'}= \begin{pmatrix}v^1/s\\v^2\\v^3\end{pmatrix}.}$$

Este caso particular enseña un fenómeno esencial: cuando se hace $s$ veces mayor el vector de referencia, el coeficiente correspondiente se divide por $s$. No hemos cambiado $v$; hemos cambiado la **escala de su descripción**. Si el contexto físico asigna unidades a los desplazamientos de referencia, las componentes y las unidades se interpretan coherentemente según la convención declarada.

[]{#la-interpretación-física-y-sus-límites}

### La interpretación física y sus límites {#fispm-c04-la-interpretaciuxf3n-fuxedsica-y-sus-luxedmites}

La interpretación dimensional de las componentes depende de la convención declarada. Si los vectores de la base representan desplazamientos de referencia con dimensión de longitud, los coeficientes $v^i$ son números adimensionales; si se trabaja con direcciones adimensionales, las componentes pueden portar la unidad de longitud. En ningún caso los coeficientes solos revelan cuál es la base de referencia ni qué convención de unidades se adoptó. No hemos probado que una base sea ortonormal: ni siquiera hemos definido todavía los ángulos y las longitudes. Tampoco se sigue de la definición 4.9 que los vectores elegidos representen un marco físico inercial o que el espacio físico real satisfaga exactamente el modelo euclídeo. Son cuestiones posteriores. Al igual que en el capítulo 3, los valores medidos que se empleen para realizar una representación física tendrán su propia incertidumbre; las igualdades algebraicas de las proposiciones 4.5--4.7 no son resultados experimentales.

[]{#fispm-t1-c04-e0006}

**Ejercicio 4.6 --- Tres vectores, pero ninguna base.**

**Función pedagógica:** diagnóstico de independencia y generación, prueba de estrés de la definición, reconstrucción de una representación.

Sea $E=(e_1,e_2,e_3)$ una base conocida de $V$ y definamos

$$u=e_1+e_2,\qquad w=e_2+e_3,\qquad z=u+w.$$

1.  Demuestra que $(u,w,z)$ no es independiente.

2.  Exhibe dos listas de coeficientes que representen $z$.

3.  Demuestra, sin determinantes, que la familia tampoco genera $V$.

4.  Explica por qué añadir $z$ a $(u,w)$ no soluciona el problema.

**Solución desarrollada**

1.  $u+w-z=0$ proporciona coeficientes $(1,1,-1)$ no todos nulos: la familia es dependiente.

2.  $z=1u+1w+0z=0u+0w+1z$. La representación no es única.

3.  Si existieran $\alpha,\beta,\gamma$ con $e_1=\alpha u+\beta w+\gamma z$, podríamos absorber $\gamma z$ y escribir $e_1=au+bw$. Esto daría

$$e_1=ae_1+(a+b)e_2+be_3.$$

Como $E$ es base, habría de cumplirse $a=1$, $a+b=0$ y $b=0$, imposible. Por tanto $e_1$ no pertenece al espacio generado. 4. Por definición $z=u+w$ ya pertenecía a $\operatorname{span}(u,w)$: no añade una dirección algebraica nueva ni repara la redundancia.

[]{#fispm-t1-c04-e0007}

**Ejercicio 4.7 --- Probar una base y leer sus componentes.**

**Función pedagógica:** construcción, prueba de existencia y unicidad, traducción símbolo--representación.

Sea $E=(e_1,e_2,e_3)$ una base de $V$, y sean

$$b_1=e_1,\quad b_2=e_1+e_2,\quad b_3=e_1+e_2+e_3.$$

1.  Demuestra que $B=(b_1,b_2,b_3)$ es una base sin invocar determinantes.

2.  Para $v=2e_1+3e_2+4e_3$, calcula $[v]_B$ y verifica reconstruyendo $v$.

3.  Explica por qué la diferencia entre $[v]_E$ y $[v]_B$ no implica un cambio físico del vector.

**Solución desarrollada**

1.  Para $v=ae_1+be_2+ce_3$, una combinación $xb_1+yb_2+zb_3$ reproduce $v$ si y sólo si $x+y+z=a$, $y+z=b$ y $z=c$. La única solución es

$$(x,y,z)=(a-b,b-c,c).$$

Existe y es única para todo vector; proposición 4.6 prueba que $B$ es base. 2. Sustituyendo $(a,b,c)=(2,3,4)$:

$$[v]_B=(-1,-1,4)^{\mathsf T}.$$

Reconstruimos:

$$-b_1-b_2+4b_3 =-e_1-(e_1+e_2)+4(e_1+e_2+e_3) =2e_1+3e_2+4e_3=v.$$

1.  La identidad de reconstrucción muestra que ambas columnas nombran el mismo elemento de $V$. Cambian los vectores que sirven como referencia, no el desplazamiento físico.

[]{#cierre-de-una-base-vectorial-a-las-coordenadas-de-los-puntos}

### Cierre: de una base vectorial a las coordenadas de los puntos {#fispm-c04-cierre-de-una-base-vectorial-a-las-coordenadas-de-los-puntos}

Ya tenemos una cadena demostrada:

$$\boxed{ \text{generación + independencia} \Longleftrightarrow \text{existencia y unicidad de componentes}. }$$

Proposiciones 4.5--4.7 justifican la representación de **vectores** mediante columnas. Aún no hemos asignado una columna a un punto $P$, porque para hacerlo debemos elegir además un origen $O$ y representar el vector $r_O(P)=\overrightarrow{OP}$. El siguiente paso, **§4 --- Coordenadas afines y marcos cartesianos**, incorporará esa elección adicional y distinguirá sistemáticamente punto, vector de posición, desplazamiento y terna de componentes.

[]{#coordenadas-afines-y-marcos-cartesianos}

[]{#fispm-t1-c04-s04}

[]{#fpm-i-04-s04}

## 4. Coordenadas afines y marcos cartesianos {#fispm-c04-coordenadas-afines-y-marcos-cartesianos}

[]{#activación-tres-números-qué-describen}

### Activación: tres números, ¿qué describen? {#fispm-c04-activaciuxf3n-tres-nuxfameros-quuxe9-describen}

Un plano de una sala señala que un sensor ocupa la posición «$(2,-1,3)$». Esa información no determina por sí sola una ubicación física: faltan un origen, tres vectores de referencia ordenados y las convenciones de escala que permiten interpretar los números.[^2] Si otro plano elige el origen en la puerta en vez de una esquina, el mismo sensor recibe otra terna sin moverse. §1 distinguió los puntos de los vectores; §2 construyó combinaciones afines; §3 demostró que una base permite representar **vectores** por columnas únicas. Ahora añadiremos la elección que faltaba para representar **puntos**.

Activación Si dos registros contienen la misma terna $(2,-1,3)$, ¿qué deberíamos comprobar antes de concluir que se refieren al mismo lugar? ¿Puede una diferencia de ternas ser físicamente significativa aunque ambas ternas por separado dependan del origen?

[]{#inventario-de-objetos-no-intercambiar-tipos}

### Inventario de objetos: no intercambiar tipos {#fispm-c04-inventario-de-objetos-no-intercambiar-tipos}

La geometría disponible distingue:

- un punto $P\in\mathcal E$;

- un vector de desplazamiento $v\in V$;

- su columna $[v]_B\in\mathbb R^3$, una vez elegida una base $B$;

- el vector de posición $r_O(P)=\overrightarrow{OP}\in V$, una vez elegido un origen $O$.

La expresión $P=v$ no pertenece a nuestra estructura. Tampoco hay una terna de números atribuida canónicamente a $P$. En cambio, la cadena

$$P\longmapsto r_O(P)\longmapsto [r_O(P)]_B$$

está bien definida cuando se fijan $O$ y $B$. Cada flecha representa una **decisión matemática distinta**; no hay medición ni movimiento implícito en la elección.

[]{#definir-el-marco-afín}

### Definir el marco afín {#fispm-c04-definir-el-marco-afuxedn}

**Definición 4.11 --- Marco afín ordenado** Un **marco afín** de $\mathcal E$ es un par

$$\boxed{\mathfrak F=(O,B),\qquad B=(e_1,e_2,e_3),}$$

donde $O\in\mathcal E$ es un punto elegido como origen y $B$ es una base ordenada del espacio vectorial $V$ de desplazamientos.

La elección de $O$ fija la referencia para las posiciones; la de $B$ fija cómo se descomponen los desplazamientos. En este punto no se exige que los $e_i$ tengan la misma longitud ni que formen ángulos rectos: tales expresiones todavía no están definidas. **No-ejemplos.** Un origen aislado no es un marco completo. Una terna dependiente tampoco lo es, aunque dibujemos tres flechas y la llamemos «tres ejes». Una base sin origen sirve para representar vectores, pero todavía no proporciona coordenadas de puntos.

[]{#definir-las-coordenadas-de-un-punto}

### Definir las coordenadas de un punto {#fispm-c04-definir-las-coordenadas-de-un-punto}

**Definición 4.12 --- Coordenadas afines de un punto** Fijado $\mathfrak F=(O,B)$, las **coordenadas afines** de $P$ son la columna única

$$\boxed{x_{\mathfrak F}(P):=[\overrightarrow{OP}]_B =\begin{pmatrix}x^1\\x^2\\x^3\end{pmatrix}.}$$

Por la definición de componentes y proposición 4.6, el punto satisface la reconstrucción

$$\boxed{P=O+x^1e_1+x^2e_2+x^3e_3.}$$

En la última fórmula, $O+v$ es la acción afín definida en la definición 4.1; no estamos sumando cuatro puntos. Las coordenadas $x^i$ son escalares relativos a la base **declarada**, no propiedades intrínsecas del punto.

**Principio metodológico 4.5 --- Declarar el marco y las unidades** Toda terna que se interprete como posición debe ir acompañada de la elección del origen, la base ordenada y el convenio de unidades. Distinguir explícitamente $P$, $r_O(P)$ y $x_{\mathfrak F}(P)$; no inferir desplazamiento real de un cambio de etiqueta.

[]{#la-proposición-de-existencia-y-unicidad-para-puntos}

### La proposición de existencia y unicidad para puntos {#fispm-c04-la-proposiciuxf3n-de-existencia-y-unicidad-para-puntos}

**Proposición 4.8 --- Coordenadas afines como correspondencia biyectiva** Para cada marco afín fijo $\mathfrak F=(O,B)$, la aplicación

$$x_{\mathfrak F}:\mathcal E\longrightarrow\mathbb R^3, \qquad P\longmapsto [\overrightarrow{OP}]_B$$

es biyectiva. Su inversa es

$$\boxed{(c^1,c^2,c^3)^{\mathsf T}\longmapsto O+c^1e_1+c^2e_2+c^3e_3.}$$

**Demostración.** Para una columna $c$, la combinación $v=\sum_i c^ie_i$ es un vector y definición 4.1 construye el punto $P=O+v$. Por definición 4.2, $\overrightarrow{OP}=v$, y por la proposición 4.6 sus componentes son precisamente $c$: la aplicación es sobreyectiva. Si dos puntos $P,Q$ poseen la misma columna, proposición 4.7 y la unicidad de las componentes dan $\overrightarrow{OP}=\overrightarrow{OQ}$. Definición 4.1 implica entonces $P=O+\overrightarrow{OP}=O+\overrightarrow{OQ}=Q$: es inyectiva. $\square$ **Lectura guiada.** Para existir una posición dada la terna, convertimos la terna en un vector y trasladamos el origen; para probar unicidad, deshacemos ambas operaciones. Ésta es una biyección que **depende del marco**, no una identidad entre los conjuntos $\mathcal E$ y $\mathbb R^3$.

[]{#el-origen-y-los-vectores-de-referencia-tienen-coordenadas-sencillas}

### El origen y los vectores de referencia tienen coordenadas sencillas {#fispm-c04-el-origen-y-los-vectores-de-referencia-tienen-coordenadas-sencillas}

De $\overrightarrow{OO}=0$ y proposición 4.7 se deduce

$$x_{\mathfrak F}(O)=\begin{pmatrix}0\\0\\0\end{pmatrix}.$$

Los puntos $E_i:=O+e_i$ tienen las columnas unitarias habituales:

$$x_{\mathfrak F}(E_1)=\begin{pmatrix}1\\0\\0\end{pmatrix},\quad x_{\mathfrak F}(E_2)=\begin{pmatrix}0\\1\\0\end{pmatrix},\quad x_{\mathfrak F}(E_3)=\begin{pmatrix}0\\0\\1\end{pmatrix}.$$

Estas columnas no afirman que los vectores de referencia midan un metro, que sean perpendiculares o que tengan igual longitud. Sólo codifican su **papel algebraico en la base**.

[]{#definir-los-ejes-afines-sin-presuponer-ángulos-rectos}

### Definir los ejes afines sin presuponer ángulos rectos {#fispm-c04-definir-los-ejes-afines-sin-presuponer-uxe1ngulos-rectos}

**Definición 4.13 --- Ejes afines de un marco** Para $\mathfrak F=(O,(e_1,e_2,e_3))$, el eje afín asociado a $e_i$ es el conjunto de puntos

$$\boxed{\mathcal A_i=\{O+te_i:t\in\mathbb R\}.}$$

Los tres ejes concurren en $O$ y están asociados a desplazamientos linealmente independientes. La construcción es algebraicamente legítima incluso si en una ilustración sus direcciones parecen oblicuas. **Precisión terminológica.** A menudo se llama «sistema cartesiano» a un origen con ejes perpendiculares y una escala declarada. Aquí hemos construido la parte **afín** del sistema de coordenadas; podremos exigir ortogonalidad sólo tras definir producto escalar (§5) y construir bases ortonormales (§7). Por ahora, «marco cartesiano» en el título señala el objetivo del capítulo, no una propiedad métrica ya demostrada.

[]{#proposición-restar-coordenadas-recupera-un-desplazamiento}

### Proposición: restar coordenadas recupera un desplazamiento {#fispm-c04-proposiciuxf3n-restar-coordenadas-recupera-un-desplazamiento}

**Proposición 4.9 --- Diferencias de coordenadas** Fijado $\mathfrak F=(O,B)$, para todos $P,Q\in\mathcal E$ se tiene

$$\boxed{[\overrightarrow{PQ}]_B =x_{\mathfrak F}(Q)-x_{\mathfrak F}(P).}$$

Además, para $v\in V$,

$$\boxed{x_{\mathfrak F}(P+v) =x_{\mathfrak F}(P)+[v]_B.}$$

**Demostración.** proposición 4.2 establece que $\overrightarrow{PQ}=\overrightarrow{OQ}-\overrightarrow{OP}$. Aplicamos la linealidad de la correspondencia de componentes proposición 4.7 y la definición definición 4.12 para obtener la primera identidad. Para la segunda, la ley del triángulo da $\overrightarrow{O(P+v)}=\overrightarrow{OP}+v$; proposición 4.7 vuelve a convertir la suma vectorial en suma de columnas. $\square$ La diferencia de las columnas representa el **desplazamiento entre los puntos**, no una «resta física de posiciones» realizada sobre los objetos. El orden importa:

$$[\overrightarrow{QP}]_B =x_{\mathfrak F}(P)-x_{\mathfrak F}(Q) =-[\overrightarrow{PQ}]_B.$$

[]{#ejemplo-físico-ubicar-un-detector-y-desplazarlo}

### Ejemplo físico: ubicar un detector y desplazarlo {#fispm-c04-ejemplo-fuxedsico-ubicar-un-detector-y-desplazarlo}

Fijamos un origen en una marca del laboratorio y tres desplazamientos de referencia ordenados $B=(e_1,e_2,e_3)$. Sea el punto del detector

$$P=O+2e_1-e_2+3e_3.$$

Su columna es

$$x_{\mathfrak F}(P)=\begin{pmatrix}2\\-1\\3\end{pmatrix}.$$

Si trasladamos **físicamente el detector en el modelo** mediante $v=-e_1+2e_2$, el nuevo punto es $Q=P+v$. Proposición 4.9 proporciona

$$x_{\mathfrak F}(Q) =\begin{pmatrix}2\\-1\\3\end{pmatrix} +\begin{pmatrix}-1\\2\\0\end{pmatrix} =\begin{pmatrix}1\\1\\3\end{pmatrix}.$$

Aquí sí cambió el punto modelado. La comparación con el próximo caso ---un cambio de **origen** sin movimiento--- es la prueba conceptual importante.

[]{#cambiar-sólo-el-origen-conservando-la-base}

### Cambiar sólo el origen, conservando la base {#fispm-c04-cambiar-suxf3lo-el-origen-conservando-la-base}

Supongamos que elegimos $O'=O+a$ con $a\in V$, pero conservamos exactamente la base ordenada $B$. Los marcos son $\mathfrak F=(O,B),\qquad \mathfrak F'=(O',B).$ §1 ya demostró para el vector de posición que

$$r_{O'}(P)=r_O(P)-a.$$

La novedad consiste en expresar esa ley para las **columnas** mediante proposición 4.7. Es un cambio pasivo de descripción; no modifica el punto $P$.

[]{#proposición-ley-de-traslación-de-las-coordenadas}

### Proposición: ley de traslación de las coordenadas {#fispm-c04-proposiciuxf3n-ley-de-traslaciuxf3n-de-las-coordenadas}

**Proposición 4.10 --- Cambio de origen con base fija** Si $O'=O+a$ y $B$ se conserva, entonces para cualquier $P\in\mathcal E$,

$$\boxed{x_{(O',B)}(P)=x_{(O,B)}(P)-[a]_B.}$$

Para cualesquiera $P,Q$, la diferencia de coordenadas no cambia:

$$\boxed{x_{(O',B)}(Q)-x_{(O',B)}(P) =x_{(O,B)}(Q)-x_{(O,B)}(P).}$$

**Demostración.** La primera identidad se obtiene aplicando proposición 4.7 a $r_{O'}(P)=r_O(P)-a$ y usando definición 4.12. Sustraemos esta identidad para $Q$ y para $P$; los términos $-[a]_B$ se cancelan. De manera independiente, proposición 4.9 identifica ambas diferencias con $[\overrightarrow{PQ}]_B$. $\square$ **Prueba de estrés del signo.** Si el nuevo origen se desplaza **hacia** un punto manteniendo la base, la coordenada de ese punto disminuye en la componente correspondiente. Sumar $[a]_B$ sería confundir el desplazamiento del origen con el cambio de coordenada del objeto.

[]{#ejemplo-dos-planos-de-un-mismo-laboratorio}

### Ejemplo: dos planos de un mismo laboratorio {#fispm-c04-ejemplo-dos-planos-de-un-mismo-laboratorio}

Sea

$$x_{(O,B)}(P)=\begin{pmatrix}2\\-1\\3\end{pmatrix}, \qquad [a]_B=\begin{pmatrix}1\\2\\-1\end{pmatrix}.$$

Para $O'=O+a$, sin mover $P$ ni alterar $B$,

$$x_{(O',B)}(P)= \begin{pmatrix}2\\-1\\3\end{pmatrix} -\begin{pmatrix}1\\2\\-1\end{pmatrix} =\begin{pmatrix}1\\-3\\4\end{pmatrix}.$$

Recuperamos la representación antigua sumando $[a]_B$. Dos columnas distintas representan el **mismo punto** en marcos distintos; no se deduce un desplazamiento del detector. Si también cambiásemos $B$, la fórmula anterior sería insuficiente: necesitaríamos además la matriz de cambio de base, que se desarrollará en §10. La composición sistemática de ambos cambios será propia de §12.

[]{#coordenadas-de-las-combinaciones-afines}

### Coordenadas de las combinaciones afines {#fispm-c04-coordenadas-de-las-combinaciones-afines}

**Proposición 4.11 --- Compatibilidad con combinaciones afines** Si $A$ es la combinación afín de puntos $P_1,\ldots,P_n$ con coeficientes $\lambda_i$ tales que $\sum_i\lambda_i=1$, entonces, en cualquier marco fijo $\mathfrak F$,

$$\boxed{x_{\mathfrak F}(A) =\sum_i\lambda_i x_{\mathfrak F}(P_i).}$$

**Demostración.** definición 4.4 permite escribir $A=O+\sum_i\lambda_i\overrightarrow{OP_i}$ porque los coeficientes suman uno. Aplicamos definición 4.12 y la linealidad de la proposición 4.7 al vector $\overrightarrow{OA}$ y obtenemos la fórmula. Para otro origen $O'=O+a$, la suma de las nuevas columnas es $\sum_i\lambda_i(x_{\mathfrak F}(P_i)-[a]_B)=\sum_i\lambda_i x_{\mathfrak F}(P_i)-[a]_B$, exactamente la nueva columna de $A$ por la proposición 4.10. $\square$ Para el punto medio de §2:

$$\boxed{x_{\mathfrak F}(M(P,Q))= \tfrac12x_{\mathfrak F}(P)+\tfrac12x_{\mathfrak F}(Q).}$$

Para un baricentro con $W=\sum_i w_i\ne0$, los coeficientes son $w_i/W$, y la misma fórmula vale. La suma de coeficientes uno no es un detalle cosmético: impide que el punto resultante dependa del origen.

[]{#unidades-y-escalas-qué-miden-los-coeficientes}

### Unidades y escalas: qué miden los coeficientes {#fispm-c04-unidades-y-escalas-quuxe9-miden-los-coeficientes}

La ecuación $\overrightarrow{OP}=\sum_i x^ie_i$ sólo tiene interpretación dimensional después de declarar qué representan los $e_i$. Por ejemplo, si cada $e_i$ es un **desplazamiento de referencia con dimensión de longitud**, los coeficientes $x^i$ son números adimensionales; el producto $x^ie_i$ sí es una cantidad vectorial de longitud. Si se trabaja con símbolos de direcciones adimensionales y componentes dimensionales, es preciso declararlo como una convención diferente, no mezclar ambas escrituras sin aviso. Los tres desplazamientos de referencia no tienen por qué ser de igual longitud física. Una columna como $(2,-1,3)^{\mathsf T}$ no proporciona por sí sola tres medidas en metros ni permite calcular la distancia al origen. La noción métrica aún no existe en el desarrollo deductivo.

El capítulo 2 y capítulo 3 El número escrito en el plano no equivale a una medición sin declarar patrones, instrumentos, mensurando e incertidumbre. Las identidades de esta sección son exactas **en el modelo afín**; la realización física de un sistema de marcas requiere procedimientos y puede tener incertidumbre.

[]{#diagnóstico-de-afirmaciones-plausibles-pero-falsas}

### Diagnóstico de afirmaciones plausibles pero falsas {#fispm-c04-diagnuxf3stico-de-afirmaciones-plausibles-pero-falsas}

**«Tres flechas de referencia cualesquiera definen un marco».** Falso: deben constituir una base, es decir, generar $V$ y ser independientes (definición 4.9). **«El origen tiene coordenadas cero en todos los marcos».** El origen *elegido por cada marco* tiene coordenadas cero en su propio marco. El mismo punto $O$ no tiene necesariamente coordenadas cero respecto de otro origen $O'$. **«Si cambia la terna, el objeto se movió».** Falso: proposición 4.10 exhibe un contraejemplo mediante un mero cambio de origen. **«Si dos ternas son iguales, los puntos son necesariamente iguales».** Sólo si las ternas se interpretan en el **mismo marco**; proposición 4.8 no establece identidad entre columnas procedentes de marcos diferentes. **«La diferencia de ternas es un desplazamiento geométrico absoluto».** Debe precisarse: en un mismo marco, es la **columna en la base declarada** del desplazamiento intrínseco (proposición 4.9). Otra base puede proporcionar una columna diferente para ese mismo vector. **«Llamar cartesiano al marco demuestra ejes perpendiculares».** No: la perpendicularidad necesita un producto escalar (§5), y la ortonormalidad será construida en §7.

[]{#fispm-t1-c04-e0008}

**Ejercicio 4.8 --- Dos orígenes, ningún movimiento.**

**Función cognitiva:** `cambio de representación / control del signo / invariancia`.

En un marco afín $\mathfrak F=(O,B)$, dos marcas tienen columnas

$$x_{\mathfrak F}(P)=\begin{pmatrix}4\\-2\\1\end{pmatrix}, \qquad x_{\mathfrak F}(Q)=\begin{pmatrix}-1\\3\\2\end{pmatrix}.$$

Se elige $O'=O+a$ manteniendo $B$, con $[a]_B=(2,-1,4)^{\mathsf T}$.

1.  Calcula las columnas de ambos puntos respecto de $(O',B)$.

2.  Calcula la columna de $\overrightarrow{PQ}$ por las dos rutas.

3.  Explica si las marcas se movieron y por qué no puede inferirse su distancia geométrica sólo de estas columnas.

**Solución desarrollada** Por proposición 4.10 restamos la columna de $a$ a cada punto:

$$x_{(O',B)}(P)=\begin{pmatrix}2\\-1\\-3\end{pmatrix}, \qquad x_{(O',B)}(Q)=\begin{pmatrix}-3\\4\\-2\end{pmatrix}.$$

En el marco inicial, proposición 4.9 da

$$[\overrightarrow{PQ}]_B= \begin{pmatrix}-1\\3\\2\end{pmatrix} -\begin{pmatrix}4\\-2\\1\end{pmatrix} =\begin{pmatrix}-5\\5\\1\end{pmatrix}.$$

En el marco nuevo,

$$\begin{pmatrix}-3\\4\\-2\end{pmatrix} -\begin{pmatrix}2\\-1\\-3\end{pmatrix} =\begin{pmatrix}-5\\5\\1\end{pmatrix}.$$

Coinciden porque no cambió $B$ ni los puntos, sólo el origen: es una transformación pasiva. No podemos convertir la columna $(-5,5,1)^{\mathsf T}$ en una distancia sin definir una métrica sobre $V$ y especificar el significado de las escalas de la base.

[]{#fispm-t1-c04-e0009}

**Ejercicio 4.9 --- Marco válido, punto medio y errores de tipo.**

**Función cognitiva:** `construcción / no-ejemplo / traducción geometría–columnas`.

Sea $E=(e_1,e_2,e_3)$ una base de $V$ y elijamos un origen $O$. Definimos $b_1=e_1,\qquad b_2=e_1+e_2,\qquad b_3=e_1+e_2+e_3.$ En $\mathfrak F=(O,B)$, $B=(b_1,b_2,b_3)$, dos puntos tienen coordenadas

$$x_{\mathfrak F}(P)=\begin{pmatrix}1\\2\\-1\end{pmatrix}, \qquad x_{\mathfrak F}(Q)=\begin{pmatrix}3\\0\\1\end{pmatrix}.$$

1.  Justifica que $B$ es una base sin usar determinantes.

2.  Calcula las coordenadas de $M(P,Q)$ en $B$ y el vector $\overrightarrow{PQ}$ expresado en $E$.

3.  Analiza las frases «$P=[P]_B$» y «el punto medio es la mitad de la suma vectorial $P+Q$».

**Solución desarrollada** Para $v=ae_1+be_2+ce_3$, buscar $v=xb_1+yb_2+zb_3$ lleva a $x+y+z=a$, $y+z=b$, $z=c$, con solución única $x=a-b$, $y=b-c$, $z=c$. Por proposición 4.6, $B$ es base.

Por proposición 4.11,

$$x_{\mathfrak F}(M)=\frac12 \left(\begin{pmatrix}1\\2\\-1\end{pmatrix} +\begin{pmatrix}3\\0\\1\end{pmatrix}\right) =\begin{pmatrix}2\\1\\0\end{pmatrix}.$$

Por proposición 4.9, $[\overrightarrow{PQ}]_B=(2,-2,2)^{\mathsf T}$. Por la definición de $B$,

$$\begin{aligned} \overrightarrow{PQ} &=2b_1-2b_2+2b_3\\ &=2e_1-2(e_1+e_2)+2(e_1+e_2+e_3)\\ &=2e_1+0e_2+2e_3. \end{aligned}$$

La primera frase confunde un punto $P\in\mathcal E$ con su columna de coordenadas $x_{\mathfrak F}(P)\in\mathbb R^3$; $[P]_B$ ni siquiera es la notación definida para puntos. La segunda frase usa una suma vectorial $P+Q$ que no existe en la definición 4.1: la formulación correcta es $M=P+\tfrac12\overrightarrow{PQ}$, cuya columna puede calcularse por el promedio de la proposición 4.11.

[]{#cierre-y-enlace-deductivo}

### Cierre y enlace deductivo {#fispm-c04-cierre-y-enlace-deductivo}

La representación de un punto necesita dos elecciones:

$$\boxed{\text{marco afín}=\text{origen}+\text{base ordenada}.}$$

Con ambas fijadas, las coordenadas son únicas (proposición 4.8); la resta de columnas representa un desplazamiento (proposición 4.9); trasladar sólo el origen modifica las coordenadas por un término común y conserva las diferencias (proposición 4.10); combinar puntos afínmente es compatible con combinar sus columnas usando coeficientes de suma uno (proposición 4.11). Pero todavía **no** hemos definido la longitud de una flecha ni la distancia entre dos puntos. El siguiente paso será precisamente

(§[5](#fispm-c04-producto-escalar-norma-y-distancia)).

Allí distinguiremos la mera independencia de los ejes de su perpendicularidad y construiremos las herramientas métricas necesarias para hablar con precisión de sistemas cartesianos rectangulares.

[]{#producto-escalar-norma-y-distancia}

[]{#fispm-t1-c04-s05}

[]{#fpm-i-04-s05}

## 5. Producto escalar, norma y distancia {#fispm-c04-producto-escalar-norma-y-distancia}

[]{#activación-las-coordenadas-todavía-no-saben-medir}

### Activación: las coordenadas todavía no saben medir {#fispm-c04-activaciuxf3n-las-coordenadas-todavuxeda-no-saben-medir}

En §4 aprendimos a asignar a un punto una terna de coordenadas una vez fijado un marco afín. Supongamos que dos puntos tienen coordenadas

$$x_{\mathfrak F}(P)= \begin{pmatrix} 0\\0\\0 \end{pmatrix}, \qquad x_{\mathfrak F}(Q)= \begin{pmatrix} 3\\4\\0 \end{pmatrix}.$$

Es tentador concluir inmediatamente que están separados por «$5$ unidades». Pero hasta ahora la base $B=(e_1,e_2,e_3)$ sólo es una base algebraica. No sabemos todavía cuánto mide cada $e_i$, ni si las direcciones asociadas forman ángulos rectos. La columna

$$\begin{pmatrix} 3\\4\\0 \end{pmatrix}$$

describe componentes del desplazamiento; **no contiene por sí sola una regla de longitud**.

Activación ¿Qué estructura matemática debemos añadir a $V$ para comparar longitudes y hablar de distancia sin depender de una base particular?

[]{#la-geometría-afín-y-la-geometría-métrica-son-capas-distintas}

### La geometría afín y la geometría métrica son capas distintas {#fispm-c04-la-geometruxeda-afuxedn-y-la-geometruxeda-muxe9trica-son-capas-distintas}

La estructura afín construida hasta §4 permite distinguir puntos y vectores, trasladar puntos, formar diferencias, elegir bases y representar puntos y desplazamientos por columnas. Nada de esto define todavía longitud, distancia, perpendicularidad o ángulo.

**Principio metodológico 4.6 --- La métrica es estructura adicional** No inferir longitudes, distancias ni perpendicularidad a partir de una terna de componentes sin declarar antes el producto escalar ---o una estructura métrica equivalente--- con el que se interpretan esas componentes.

[]{#fispm-c04-definir-producto-escalar-real label="fispm-c04-definir-producto-escalar-real"}

**Definición 4.14 --- Producto escalar real** Un **producto escalar** sobre $V$ es una aplicación

$$\langle\cdot,\cdot\rangle:V\times V\longrightarrow\mathbb R$$

tal que para todos $u,v,w\in V$ y $\alpha,\beta\in\mathbb R$:

$$\langle \alpha u+\beta v,w\rangle =\alpha\langle u,w\rangle+\beta\langle v,w\rangle,$$

$$\langle u,v\rangle=\langle v,u\rangle,$$

y

$$\langle v,v\rangle\ge0, \qquad \langle v,v\rangle=0\Longleftrightarrow v=0.$$

Por simetría y bilinealidad en la primera entrada, también hay linealidad en la segunda.

[]{#fispm-c04-definir-espacio-afuxedn-eucluxeddeo label="fispm-c04-definir-espacio-afuxedn-eucluxeddeo"}

**Definición 4.15 --- Espacio afín euclídeo** Un **espacio afín euclídeo** es un espacio afín $\mathcal E$ modelado sobre un espacio vectorial real $V$ provisto de un producto escalar positivo definido.

La estructura afín determina desplazamientos; el producto escalar añade la posibilidad de medirlos. Que un sistema físico concreto sea adecuadamente modelado así es una cuestión física y experimental, no una consecuencia de la definición.

[]{#definir-norma-inducida}

### Definir: norma inducida {#fispm-c04-definir-norma-inducida}

**Definición 4.16 --- Norma euclídea inducida** Para $v\in V$ definimos

$$\boxed{\|v\|:=\sqrt{\langle v,v\rangle}.}$$

La positividad garantiza

$$\|v\|\ge0, \qquad \|v\|=0\Longleftrightarrow v=0.$$

Además,

$$\|\lambda v\| =\sqrt{\lambda^2\langle v,v\rangle} =|\lambda|\,\|v\|.$$

[]{#fispm-c04-proposiciuxf3n-desigualdad-de-cauchyschwarz label="fispm-c04-proposiciuxf3n-desigualdad-de-cauchyschwarz"}

**Proposición 4.12 --- Desigualdad de Cauchy--Schwarz** Para todos $u,v\in V$,

$$\boxed{|\langle u,v\rangle|\le\|u\|\,\|v\|.}$$

Hay igualdad si y sólo si $u$ y $v$ son linealmente dependientes.

**Demostración.** Si $v=0$, el resultado es inmediato. Supongamos $v\ne0$ y definamos

$$\lambda=\frac{\langle u,v\rangle}{\langle v,v\rangle}.$$

La positividad da

$$0\le\|u-\lambda v\|^2 =\langle u-\lambda v,u-\lambda v\rangle.$$

Expandiendo,

$$0\le \langle u,u\rangle -2\lambda\langle u,v\rangle +\lambda^2\langle v,v\rangle.$$

Al sustituir $\lambda$,

$$0\le \langle u,u\rangle -\frac{\langle u,v\rangle^2}{\langle v,v\rangle}.$$

Por tanto,

$$\langle u,v\rangle^2 \le \langle u,u\rangle\langle v,v\rangle,$$

y al tomar raíces, $|\langle u,v\rangle| \le \|u\|\,\|v\|.$

La igualdad ocurre exactamente cuando $\|u-\lambda v\|=0$, es decir, cuando $u=\lambda v$; incluyendo los casos nulos, esto equivale a dependencia lineal. $\square$

[]{#proposición-desigualdad-triangular-de-la-norma}

### Proposición: desigualdad triangular de la norma {#fispm-c04-proposiciuxf3n-desigualdad-triangular-de-la-norma}

**Proposición 4.13 --- Desigualdad triangular** Para todos $u,v\in V$,

$$\boxed{\|u+v\|\le\|u\|+\|v\|.}$$

**Demostración.**

$$\begin{aligned} \|u+v\|^2 &=\|u\|^2+2\langle u,v\rangle+\|v\|^2\\ &\le\|u\|^2+2|\langle u,v\rangle|+\|v\|^2\\ &\le(\|u\|+\|v\|)^2. \end{aligned}$$

Como ambos lados son no negativos, tomamos raíces. $\square$ La ley del triángulo de §1 era una identidad vectorial; proposición 4.13 compara longitudes.

[]{#definir-distancia-entre-puntos}

### Definir: distancia entre puntos {#fispm-c04-definir-distancia-entre-puntos}

**Definición 4.17 --- Distancia euclídea** Para $P,Q\in\mathcal E$,

$$\boxed{d(P,Q):=\|\overrightarrow{PQ}\|.}$$

La definición no requiere origen ni base.

[]{#proposición-la-distancia-satisface-los-axiomas-métricos}

### Proposición: la distancia satisface los axiomas métricos {#fispm-c04-proposiciuxf3n-la-distancia-satisface-los-axiomas-muxe9tricos}

**Proposición 4.14 --- Propiedades métricas de $d$** Para cualesquiera $P,Q,R\in\mathcal E$:

$$d(P,Q)\ge0, \qquad d(P,Q)=0\Longleftrightarrow P=Q,$$

$$d(P,Q)=d(Q,P),$$

y

$$\boxed{d(P,R)\le d(P,Q)+d(Q,R).}$$

**Demostración.** Las dos primeras propiedades siguen de la definición 4.16. La simetría usa $\overrightarrow{QP}=-\overrightarrow{PQ}$ y $\|-v\|=\|v\|$. Finalmente,

$$\overrightarrow{PR} = \overrightarrow{PQ}+\overrightarrow{QR},$$

y proposición 4.13 produce la desigualdad triangular de la distancia. $\square$

[]{#la-métrica-en-una-base-general-matriz-de-gram}

### La métrica en una base general: matriz de Gram {#fispm-c04-la-muxe9trica-en-una-base-general-matriz-de-gram}

**Definición 4.18 --- Matriz de Gram de una base** Sea $B=(e_1,e_2,e_3)$ una base. Su **matriz de Gram** es

$$\boxed{ G_B= \begin{pmatrix} \langle e_1,e_1\rangle & \langle e_1,e_2\rangle & \langle e_1,e_3\rangle\\ \langle e_2,e_1\rangle & \langle e_2,e_2\rangle & \langle e_2,e_3\rangle\\ \langle e_3,e_1\rangle & \langle e_3,e_2\rangle & \langle e_3,e_3\rangle \end{pmatrix}. }$$

Si $c=[v]_B$, entonces

$$\boxed{ \|v\|^2=c^{\mathsf T}G_Bc. }$$

[]{#proposición-positividad-de-la-matriz-de-gram}

### Proposición: positividad de la matriz de Gram {#fispm-c04-proposiciuxf3n-positividad-de-la-matriz-de-gram}

**Proposición 4.15 --- Forma cuadrática de Gram** Para toda columna no nula $c\in\mathbb R^3$,

$$\boxed{c^{\mathsf T}G_Bc>0.}$$

**Demostración.** El vector $v=c^1e_1+c^2e_2+c^3e_3$ es no nulo porque $B$ es una base y $c\ne0$. Luego

$$c^{\mathsf T}G_Bc =\langle v,v\rangle>0.$$

$\square$

[]{#no-ejemplo-la-fórmula-pitagórica-no-vale-en-cualquier-base}

### No-ejemplo: la fórmula pitagórica no vale en cualquier base {#fispm-c04-no-ejemplo-la-fuxf3rmula-pitaguxf3rica-no-vale-en-cualquier-base}

Supongamos

$$\langle e_1,e_1\rangle=4, \qquad \langle e_2,e_2\rangle=1, \qquad \langle e_1,e_2\rangle=1.$$

Para $v=2e_1-e_2$,

$$\begin{aligned} \|v\|^2 &=4\langle e_1,e_1\rangle -4\langle e_1,e_2\rangle +\langle e_2,e_2\rangle\\ &=16-4+1=13. \end{aligned}$$

Por tanto, $\|v\|=\sqrt{13},$

no $\sqrt5$.

Coordenadas no son métrica La expresión $\sqrt{(v^1)^2+(v^2)^2+(v^3)^2}$ no es universal. Sólo aparecerá bajo hipótesis adicionales sobre la base, introducidas en §7.

[]{#invariancia-frente-al-origen-y-dependencia-respecto-de-la-métrica}

### Invariancia frente al origen y dependencia respecto de la métrica {#fispm-c04-invariancia-frente-al-origen-y-dependencia-respecto-de-la-muxe9trica}

Si el origen cambia pero la base permanece fija, proposición 4.10 preserva las diferencias de coordenadas. Por ello $\overrightarrow{PQ}$ y $d(P,Q)$ permanecen iguales. Esto no significa que la distancia sea independiente de toda estructura: si sobre $V$ elegimos otro producto escalar, podemos obtener longitudes distintas. La métrica forma parte del modelo.

[]{#interpretación-física-y-unidades}

### Interpretación física y unidades {#fispm-c04-interpretaciuxf3n-fuxedsica-y-unidades}

Si los vectores modelan desplazamientos, entonces $\|v\|$ tiene dimensión de longitud y $\langle u,v\rangle$ dimensión de longitud al cuadrado. Si los vectores base llevan dimensión de longitud, las entradas de $G_B$ también tienen dimensión de longitud al cuadrado y sus componentes pueden ser adimensionales. Las identidades geométricas son exactas dentro del modelo. Una medición experimental de una distancia posee resolución e incertidumbre, según capítulo 3.

[]{#fispm-t1-c04-e0010}

**Ejercicio 4.10 --- Una columna no determina por sí sola la longitud.**

**Función pedagógica:** `Diagnóstico → Matriz de Gram → No-ejemplo`

En una base $B=(e_1,e_2,e_3)$:

$$\langle e_1,e_1\rangle=4\,\mathrm{m^2}, \quad \langle e_2,e_2\rangle=1\,\mathrm{m^2}, \quad \langle e_1,e_2\rangle=1\,\mathrm{m^2}.$$

Si

$$[v]_B= \begin{pmatrix} 2\\-1\\0 \end{pmatrix},$$

calcula $\|v\|$, explica por qué $\sqrt5\,\mathrm m$ es incorrecto e indica qué datos faltan si la tercera componente fuese no nula.

**Solución desarrollada**

$$\|v\|^2 =16-4+1 =13\,\mathrm{m^2},$$

luego

$$\boxed{\|v\|=\sqrt{13}\,\mathrm m.}$$

La raíz $\sqrt5$ presupone condiciones métricas especiales sobre la base que no han sido dadas. Para una tercera componente no nula se requerirían además $\langle e_3,e_3\rangle$, $\langle e_1,e_3\rangle$ y $\langle e_2,e_3\rangle$.

[]{#fispm-t1-c04-e0011}

**Ejercicio 4.11 --- Distancia, cambio de origen y desigualdad triangular.**

**Función pedagógica:** `Integración → Invariancia → Desigualdad triangular`

En un marco $\mathfrak F=(O,B)$:

$$x_{\mathfrak F}(P)= \begin{pmatrix}0\\0\\0\end{pmatrix}, \quad x_{\mathfrak F}(Q)= \begin{pmatrix}1\\1\\0\end{pmatrix}, \quad x_{\mathfrak F}(R)= \begin{pmatrix}3\\1\\0\end{pmatrix}.$$

Además,

$$\langle e_1,e_1\rangle=1\,\mathrm{m^2}, \quad \langle e_2,e_2\rangle=4\,\mathrm{m^2}, \quad \langle e_1,e_2\rangle=0.$$

Calcula las tres distancias, verifica proposición 4.14 y explica por qué un traslado del origen con base fija no las modifica.

**Solución desarrollada**

Las columnas de los desplazamientos son

$$\begin{pmatrix}1\\1\\0\end{pmatrix}, \qquad \begin{pmatrix}2\\0\\0\end{pmatrix}, \qquad \begin{pmatrix}3\\1\\0\end{pmatrix}.$$

Por tanto,

$$\boxed{ d(P,Q)=\sqrt5\,\mathrm m,\qquad d(Q,R)=2\,\mathrm m,\qquad d(P,R)=\sqrt{13}\,\mathrm m. }$$

Y

$$\sqrt{13}\le\sqrt5+2.$$

Bajo un cambio de origen con base fija, proposición 4.10 resta la misma columna a las coordenadas de todos los puntos. Las diferencias permanecen iguales y, por tanto, también las distancias.

[]{#cierre-de-la-estructura-afín-a-la-geometría-euclídea}

### Cierre: de la estructura afín a la geometría euclídea {#fispm-c04-cierre-de-la-estructura-afuxedn-a-la-geometruxeda-eucluxeddea}

La cadena construida es

$$\boxed{ \text{estructura afín} +\langle\cdot,\cdot\rangle \longrightarrow \|v\| \longrightarrow d(P,Q). }$$

Cauchy--Schwarz controla el producto escalar; de ella se obtiene la desigualdad triangular de la norma y después la de la distancia. El siguiente paso será

(§[6](#fispm-c04-proyecciones-uxe1ngulos-y-geometruxeda-de-componentes)).

[]{#proyecciones-ángulos-y-geometría-de-componentes}

[]{#fispm-t1-c04-s06}

[]{#fpm-i-04-s06}

## 6. Proyecciones, ángulos y geometría de componentes {#fispm-c04-proyecciones-uxe1ngulos-y-geometruxeda-de-componentes}

[]{#activación-cuánto-de-un-vector-apunta-en-una-dirección}

### Activación: ¿cuánto de un vector apunta en una dirección? {#fispm-c04-activaciuxf3n-cuuxe1nto-de-un-vector-apunta-en-una-direcciuxf3n}

Una fuerza, un desplazamiento o cualquier otro vector puede compararse con una dirección elegida. La pregunta física típica no es sólo cuánto mide el vector completo, sino **qué parte de él actúa a lo largo de una dirección determinada**. Con sólo componentes algebraicas esta pregunta depende de cómo hayamos elegido la base. Con el producto escalar introducido en §5 podemos formularla sin depender de una representación particular. Sean $u,v\in V$, con $v\ne0$. Queremos construir un múltiplo de $v$ que represente la parte de $u$ alineada con la dirección de $v$, y que el resto sea perpendicular a esa dirección.

[]{#fig:I-04-R02}

<figure id="fig-fpm-v04-i-04-r02" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-04-R02.svg" class="lightbox" data-gallery="fpm-v04-c04"><img src="/assets/books/fispm/v04/I-04-R02.svg" alt="Proyectar conserva una componente. Diagrama del capítulo 4; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="285" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 4.3.** La proyección ortogonal sobre el eje horizontal es $v_\parallel=(v\cdot e_1)e_1$. El residuo perpendicular no desaparece del vector: $v=v_\parallel+v_\perp$. Véase §[6](#fispm-c04-proyecciones-uxe1ngulos-y-geometruxeda-de-componentes).

</figcaption>

</figure>

[]{#fig:I-04-N02}

<figure id="fig-fpm-v04-i-04-n02" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-04-N02.svg" class="lightbox" data-gallery="fpm-v04-c04"><img src="/assets/books/fispm/v04/I-04-N02.svg" alt="Proyectar un vector. Diagrama del capítulo 4; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="373" height="289" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 4.4.** En una base ortonormal, $v=v_1e_1+v_2e_2$ y $v_i=v\cdot e_i$. Las líneas discontinuas sitúan las componentes; no son fuerzas adicionales. Véase §[6](#fispm-c04-proyecciones-uxe1ngulos-y-geometruxeda-de-componentes).

</figcaption>

</figure>

[]{#fispm-c04-definir-ortogonalidad label="fispm-c04-definir-ortogonalidad"}

**Definición 4.19 --- Ortogonalidad** Dos vectores $u,v\in V$ son **ortogonales**, y escribimos

$$u\perp v,$$

si

$$\boxed{\langle u,v\rangle=0.}$$

La definición utiliza el producto escalar, no la apariencia de un dibujo ni la forma de sus columnas en una base arbitraria. En particular, el vector cero es ortogonal a todo vector: $\langle 0,v\rangle=0.$ La afirmación inversa «si $u\perp v$, entonces uno de los dos es cero» es falsa: pueden existir dos vectores no nulos y ortogonales.

[]{#la-condición-que-debe-satisfacer-una-proyección}

### La condición que debe satisfacer una proyección {#fispm-c04-la-condiciuxf3n-que-debe-satisfacer-una-proyecciuxf3n}

Busquemos un vector de la forma $p=\lambda v$

tal que el residuo

$$r:=u-p$$

sea ortogonal a $v$. La condición es $\langle u-\lambda v,v\rangle=0.$ Por bilinealidad, $\langle u,v\rangle-\lambda\langle v,v\rangle=0.$ Como $v\ne0$, definición 4.14 implica $\langle v,v\rangle>0.$

Por tanto el coeficiente queda determinado de manera única:

$$\boxed{ \lambda= \frac{\langle u,v\rangle}{\langle v,v\rangle}. }$$

La construcción no requiere todavía definir un ángulo.

[]{#definir-proyección-ortogonal-sobre-una-dirección}

### Definir: proyección ortogonal sobre una dirección {#fispm-c04-definir-proyecciuxf3n-ortogonal-sobre-una-direcciuxf3n}

**Definición 4.20 --- Proyección ortogonal sobre un vector no nulo** Para $v\ne0$, definimos la **proyección ortogonal de $u$ sobre la dirección de $v$** por

$$\boxed{ \operatorname{proj}_v(u) := \frac{\langle u,v\rangle}{\langle v,v\rangle}\,v. }$$

El resultado pertenece al subespacio generado por $v$: $\operatorname{proj}_v(u)\in\operatorname{span}(v).$ Si reemplazamos $v$ por otro vector no nulo de la misma dirección, por ejemplo $cv$ con $c\ne0$, obtenemos el mismo vector proyectado: $\operatorname{proj}_{cv}(u)=\operatorname{proj}_v(u).$

Por ello la proyección depende de la **dirección** o recta vectorial elegida, no de la longitud particular del representante $v$.

**Principio metodológico 4.7 --- Declarar la dirección y la métrica antes de proyectar** Una «componente en una dirección» no se obtiene tomando una entrada de una columna salvo en situaciones especiales. Primero se fija la dirección geométrica y el producto escalar; después se proyecta.

[]{#proposición-descomposición-ortogonal-y-unicidad}

### Proposición: descomposición ortogonal y unicidad {#fispm-c04-proposiciuxf3n-descomposiciuxf3n-ortogonal-y-unicidad}

**Proposición 4.16 --- Descomposición ortogonal respecto de una dirección** Sean $u,v\in V$ con $v\ne0$. Entonces existe una única descomposición

$$\boxed{ u=p+r }$$

tal que

$$p\in\operatorname{span}(v), \qquad r\perp v.$$

Está dada por

$$\boxed{ p=\operatorname{proj}_v(u), \qquad r=u-\operatorname{proj}_v(u). }$$

**Demostración.** Por definición 4.20, $p$ es un múltiplo de $v$. Además,

$$\begin{aligned} \langle r,v\rangle &= \left\langle u-\frac{\langle u,v\rangle}{\langle v,v\rangle}v, v \right\rangle\\ &= \langle u,v\rangle - \frac{\langle u,v\rangle}{\langle v,v\rangle} \langle v,v\rangle\\ &=0. \end{aligned}$$

Por tanto $r\perp v$. Para la unicidad, supongamos también

$$u=\alpha v+s, \qquad s\perp v.$$

Tomando producto escalar con $v$, $\langle u,v\rangle = \alpha\langle v,v\rangle,$

de donde

$$\alpha= \frac{\langle u,v\rangle}{\langle v,v\rangle}.$$

Así $\alpha v=p$, y entonces $s=u-p=r$. $\square$ La prueba separa con claridad las dos tareas: **existencia**, construyendo explícitamente $p$ y $r$; y **unicidad**, recuperando el coeficiente mediante el producto escalar.

[]{#primera-consecuencia-caso-ortogonal-y-caso-paralelo}

### Primera consecuencia: caso ortogonal y caso paralelo {#fispm-c04-primera-consecuencia-caso-ortogonal-y-caso-paralelo}

Si $u\perp v$, entonces $\langle u,v\rangle=0,$

y por tanto

$$\boxed{\operatorname{proj}_v(u)=0.}$$

En cambio, si $u=cv$, entonces

$$\operatorname{proj}_v(u) = \frac{c\langle v,v\rangle}{\langle v,v\rangle}v =cv=u.$$

La proyección distingue de manera exacta dos extremos:

$$\text{ortogonal a la dirección} \longrightarrow 0,$$

$$\text{contenido enteramente en la dirección} \longrightarrow u.$$

[]{#interpretación-física-y-alcance-de-la-proyección}

### Interpretación física y alcance de la proyección {#fispm-c04-interpretaciuxf3n-fuxedsica-y-alcance-de-la-proyecciuxf3n}

Si $u$ representa un desplazamiento y $v$ fija una dirección de referencia, $\operatorname{proj}_v(u)$ es el desplazamiento vectorial que queda al conservar sólo la parte alineada con esa dirección según la métrica escogida. Esto **no** significa que una proyección matemática sea una nueva medición. En una experiencia real, los datos con que se reconstruyen $u$ y la dirección de $v$ pueden tener incertidumbre; la identidad de la proposición 4.16 pertenece al modelo geométrico. Tampoco hemos definido todavía un número llamado «ángulo entre $u$ y $v$». Ese concepto requiere usar Cauchy--Schwarz para demostrar primero que cierto cociente pertenece a $[-1,1]$.

[]{#cauchyschwarz-legitima-el-coseno}

### Cauchy--Schwarz legitima el coseno {#fispm-c04-cauchyschwarz-legitima-el-coseno}

Sean ahora $u,v\in V$ no nulos. Proposición 4.12 implica $|\langle u,v\rangle| \le \|u\|\,\|v\|.$

Como $\|u\|\,\|v\|>0$, podemos dividir y obtener

$$\boxed{ -1\le \frac{\langle u,v\rangle}{\|u\|\,\|v\|} \le1. }$$

El cociente es adimensional y pertenece exactamente al dominio de la función $\arccos$ real. Esta verificación lógica debe preceder a la definición del ángulo.

[]{#definir-ángulo-entre-vectores-no-nulos}

### Definir: ángulo entre vectores no nulos {#fispm-c04-definir-uxe1ngulo-entre-vectores-no-nulos}

**Definición 4.21 --- Ángulo entre dos vectores no nulos** Para $u\ne0$ y $v\ne0$, definimos el **ángulo** $\theta(u,v)\in[0,\pi]$ por

$$\boxed{ \theta(u,v) := \arccos\!\left( \frac{\langle u,v\rangle}{\|u\|\,\|v\|} \right). }$$

La definición no se extiende al vector cero: si $u=0$ o $v=0$, el denominador se anula y no hay una dirección geométrica determinada por ese vector. El ángulo no viene de las coordenadas La expresión anterior es intrínseca. En una base general, no debe reemplazarse por fórmulas de trigonometría sobre componentes salvo que la métrica de esa base haya sido incorporada correctamente.

[]{#proposición-casos-límite-y-ortogonalidad}

### Proposición: casos límite y ortogonalidad {#fispm-c04-proposiciuxf3n-casos-luxedmite-y-ortogonalidad}

**Proposición 4.17 --- Caracterización métrica de los ángulos límite** Sean $u,v\ne0$. Entonces:

$$u\perp v \Longleftrightarrow \theta(u,v)=\frac{\pi}{2},$$

$$\theta(u,v)=0 \Longleftrightarrow u=cv\ \text{para algún }c>0,$$

y

$$\theta(u,v)=\pi \Longleftrightarrow u=cv\ \text{para algún }c<0.$$

**Demostración.** Por definición 4.21,

$$\cos\theta(u,v) = \frac{\langle u,v\rangle}{\|u\|\,\|v\|}.$$

Como el denominador es positivo, $\cos\theta=0$ si y sólo si $\langle u,v\rangle=0$, lo cual equivale a ortogonalidad por la definición 4.19. Para $\theta=0$ o $\pi$, el valor absoluto del coseno es uno. Por el caso de igualdad de Cauchy--Schwarz, $u$ y $v$ son linealmente dependientes: $u=cv$. El signo de

$$\langle u,v\rangle = c\langle v,v\rangle$$

determina $c>0$ cuando $\cos\theta=1$ y $c<0$ cuando $\cos\theta=-1$. La recíproca se verifica sustituyendo $u=cv$. $\square$ Esta proposición conecta tres lenguajes distintos: producto escalar, dependencia lineal y geometría angular.

[]{#definir-componente-escalar-en-una-dirección}

### Definir: componente escalar en una dirección {#fispm-c04-definir-componente-escalar-en-una-direcciuxf3n}

**Definición 4.22 --- Componente escalar de un vector en una dirección orientada** Para $v\ne0$, definimos la **componente escalar de $u$ en la dirección orientada de $v$** por

$$\boxed{ \operatorname{comp}_v(u) := \frac{\langle u,v\rangle}{\|v\|}. }$$

El signo contiene información de orientación:

$$\operatorname{comp}_{-v}(u) = -\operatorname{comp}_v(u).$$

En cambio, definición 4.20 da

$$\operatorname{proj}_{-v}(u) = \operatorname{proj}_v(u).$$

Por tanto, **la componente escalar depende del sentido elegido en la dirección**, mientras la proyección vectorial sólo depende de la recta vectorial.

**Principio metodológico 4.8 --- No confundir coordenada, componente escalar y proyección** Una entrada $v^i$ de una columna depende de la base; $\operatorname{comp}_w(v)$ depende de una dirección orientada y de la métrica; $\operatorname{proj}_w(v)$ es un vector geométrico. Antes de identificar dos de estas expresiones, demostrar las hipótesis que las relacionan.

[]{#proposición-relación-entre-ángulo-componente-y-proyección}

### Proposición: relación entre ángulo, componente y proyección {#fispm-c04-proposiciuxf3n-relaciuxf3n-entre-uxe1ngulo-componente-y-proyecciuxf3n}

**Proposición 4.18 --- Forma angular de la componente y la proyección** Para $u,v\ne0$,

$$\boxed{ \operatorname{comp}_v(u) = \|u\|\cos\theta(u,v). }$$

Si

$$\widehat v:=\frac{v}{\|v\|},$$

entonces

$$\boxed{ \operatorname{proj}_v(u) = \operatorname{comp}_v(u)\,\widehat v. }$$

En particular,

$$\boxed{ \|\operatorname{proj}_v(u)\| = |\operatorname{comp}_v(u)|. }$$

**Demostración.** De definición 4.21,

$$\langle u,v\rangle = \|u\|\,\|v\|\cos\theta(u,v).$$

Dividir por $\|v\|$ prueba la primera fórmula. Luego

$$\operatorname{comp}_v(u)\widehat v = \frac{\langle u,v\rangle}{\|v\|} \frac{v}{\|v\|} = \frac{\langle u,v\rangle}{\langle v,v\rangle}v = \operatorname{proj}_v(u).$$

Finalmente, $\|\widehat v\|=1$ y la homogeneidad de la norma producen la última igualdad. $\square$

[]{#ejemplo-sin-coordenadas}

### Ejemplo sin coordenadas {#fispm-c04-ejemplo-sin-coordenadas}

Supongamos

$$\|u\|=5, \qquad \|v\|=2, \qquad \langle u,v\rangle=6.$$

Entonces $\cos\theta(u,v) = \frac{6}{5\cdot2} = \frac35,$

y

$$\theta(u,v) = \arccos\!\left(\frac35\right).$$

La componente escalar es $\operatorname{comp}_v(u) = \frac{6}{2} = 3,$

mientras que

$$\operatorname{proj}_v(u) = \frac{6}{4}v = \frac32v.$$

El número $3$ y el vector $\tfrac32v$ codifican aspectos distintos de la misma descomposición: uno es una magnitud escalar con signo y el otro es un vector.

[]{#balance-conceptual-del-ángulo-a-pitágoras}

### Balance conceptual: del ángulo a Pitágoras {#fispm-c04-balance-conceptual-del-uxe1ngulo-a-pituxe1goras}

Ya podemos pasar rigurosamente de

$$\langle u,v\rangle$$

a tres objetos diferentes:

$$\boxed{ \theta(u,v),\qquad \operatorname{comp}_v(u),\qquad \operatorname{proj}_v(u). }$$

La geometría elemental de la proyección todavía necesita una última pieza: cuantificar cómo se reparte la longitud total entre la parte paralela y la parte perpendicular.

[]{#proposición-identidad-pitagórica-de-la-descomposición-ortogonal}

### Proposición: identidad pitagórica de la descomposición ortogonal {#fispm-c04-proposiciuxf3n-identidad-pitaguxf3rica-de-la-descomposiciuxf3n-ortogonal}

**Proposición 4.19 --- Pitágoras para proyección y residuo** Sean $u,v\in V$ con $v\ne0$. Definamos

$$p:=\operatorname{proj}_v(u), \qquad r:=u-p.$$

Entonces $p\perp r$ y

$$\boxed{ \|u\|^2 = \|p\|^2+\|r\|^2. }$$

**Demostración.** proposición 4.16 da $r\perp v$. Como $p$ es múltiplo de $v$, también $r\perp p$. Por tanto,

$$\begin{aligned} \|u\|^2 &=\langle p+r,p+r\rangle\\ &=\langle p,p\rangle +2\langle p,r\rangle +\langle r,r\rangle\\ &=\|p\|^2+\|r\|^2. \end{aligned}$$

$\square$

Esta identidad no es la fórmula pitagórica por **componentes de una base arbitraria**. Se aplica porque aquí las dos partes concretas $p$ y $r$ han sido demostradas ortogonales.

[]{#consecuencia-longitud-perpendicular-a-una-dirección}

### Consecuencia: longitud perpendicular a una dirección {#fispm-c04-consecuencia-longitud-perpendicular-a-una-direcciuxf3n}

De proposición 4.19 y proposición 4.18, $\|p\| = |\operatorname{comp}_v(u)|.$

Así,

$$\boxed{ \|r\|^2 = \|u\|^2 - \operatorname{comp}_v(u)^2. }$$

Usando

$$\operatorname{comp}_v(u) = \|u\|\cos\theta,$$

obtenemos $\|r\|^2 = \|u\|^2(1-\cos^2\theta).$

Como $\theta\in[0,\pi]$ y $\sin\theta\ge0$ en ese intervalo,

$$\boxed{ \|r\| = \|u\|\sin\theta. }$$

La interpretación geométrica es precisa:

- $\|u\|\cos\theta$ es la componente escalar **con signo** en la dirección orientada de $v$;

- $\|u\|\sin\theta$ es la magnitud no negativa de la parte perpendicular.

[]{#geometría-de-componentes-sin-adelantar-7}

### Geometría de componentes sin adelantar §7 {#fispm-c04-geometruxeda-de-componentes-sin-adelantar-7}

Supongamos que una base contiene un vector $e_1$ de norma uno. Para

$$u=u^1e_1+w,$$

si además hemos demostrado que $w\perp e_1$, entonces

$$u^1 = \langle u,e_1\rangle = \operatorname{comp}_{e_1}(u).$$

Pero esta identificación depende de **dos hipótesis**:

1.  $\|e_1\|=1$;

2.  el resto de la descomposición es ortogonal a $e_1$.

Una base general de §3 no garantiza ninguna de las dos. Por eso no podemos concluir todavía que todas las entradas de $[u]_B$ se recuperan mediante productos escalares con los vectores de la base. Anticipación controlada En §7 construiremos precisamente la situación en que todos los vectores de la base son unitarios y mutuamente ortogonales. Sólo entonces aparecerá sistemáticamente

$$u^i=\langle u,e_i\rangle.$$

[]{#fispm-t1-c04-e0012}

**Ejercicio 4.12 --- Proyección, componente y residuo.**

**Función pedagógica:** `Cálculo intrínseco → distinción de tipos → Pitágoras`

Sean $u,v\in V$ con

$$\|u\|=5, \qquad \|v\|=2, \qquad \langle u,v\rangle=6.$$

Calcula:

1.  $\operatorname{comp}_v(u)$;

2.  $\operatorname{proj}_v(u)$;

3.  $\|u-\operatorname{proj}_v(u)\|$;

4.  el ángulo $\theta(u,v)$.

**Solución desarrollada**

La componente escalar es $\operatorname{comp}_v(u) = \frac{6}{2} =3.$ La proyección vectorial es

$$\operatorname{proj}_v(u) = \frac{6}{4}v = \frac32v.$$

Su norma vale $\left\|\operatorname{proj}_v(u)\right\| =3.$ Por proposición 4.19, $\|r\|^2 = 5^2-3^2 = 16,$

de modo que

$$\boxed{\|r\|=4.}$$

Finalmente, $\cos\theta = \frac{6}{5\cdot2} = \frac35,$

y

$$\boxed{ \theta = \arccos\!\left(\frac35\right). }$$

El número $3$, el vector $\tfrac32v$ y la longitud $4$ son objetos distintos: componente escalar, proyección vectorial y magnitud del residuo perpendicular.

[]{#fispm-t1-c04-e0013}

**Ejercicio 4.13 --- La dirección puede reescalarse sin cambiar la proyección.**

**Función pedagógica:** `Invariancia → orientación → prueba algebraica`

Sea $v\ne0$ y sea $c\ne0$.

1.  Demuestra que

$$\operatorname{proj}_{cv}(u) = \operatorname{proj}_v(u).$$

1.  Determina la relación entre $\operatorname{comp}_{cv}(u)$ y $\operatorname{comp}_v(u)$.

2.  Explica qué cambia si $c<0$.

**Solución desarrollada**

Por definición 4.20,

$$\begin{aligned} \operatorname{proj}_{cv}(u) &= \frac{\langle u,cv\rangle}{\langle cv,cv\rangle}(cv)\\ &= \frac{c\langle u,v\rangle}{c^2\langle v,v\rangle}(cv)\\ &= \operatorname{proj}_v(u). \end{aligned}$$

Para la componente escalar,

$$\operatorname{comp}_{cv}(u) = \frac{c\langle u,v\rangle}{|c|\|v\|} = \frac{c}{|c|} \operatorname{comp}_v(u).$$

Por tanto,

$$\boxed{ \operatorname{comp}_{cv}(u) = \begin{cases} \operatorname{comp}_v(u), & c>0,\\ -\operatorname{comp}_v(u), & c<0. \end{cases} }$$

Reescalar una dirección no cambia la recta vectorial y, por tanto, tampoco la proyección vectorial. Si $c<0$, sí se invierte el **sentido orientado** elegido y cambia el signo de la componente escalar.

[]{#cierre-de-6}

### Cierre de §6 {#fispm-c04-cierre-de-6}

La sección ha separado cuatro nociones que suelen mezclarse:

$$\boxed{ \text{ortogonalidad}, \quad \text{proyección vectorial}, \quad \text{componente escalar}, \quad \text{ángulo}. }$$

La cadena conceptual completa es

$$\langle\cdot,\cdot\rangle \longrightarrow \perp \longrightarrow \operatorname{proj}_v(u) \longrightarrow \theta(u,v) \longrightarrow \operatorname{comp}_v(u),$$

con la proposición 4.19 proporcionando el control pitagórico de la descomposición. La conclusión pedagógica decisiva es:

$$\boxed{ \text{una coordenada no es automáticamente una componente métrica}. }$$

Para convertir sistemáticamente las entradas de una columna en componentes métricas necesitamos una base cuyas direcciones sean unitarias y mutuamente ortogonales. El siguiente paso será el §[7](#fispm-c04-bases-ortonormales-y-descomposiciuxf3n).

[]{#bases-ortonormales-y-descomposición}

[]{#fispm-t1-c04-s07}

[]{#fpm-i-04-s07}

## 7. Bases ortonormales y descomposición {#fispm-c04-bases-ortonormales-y-descomposiciuxf3n}

[]{#activación-cuándo-una-coordenada-coincide-con-una-componente-métrica}

### Activación: ¿cuándo una coordenada coincide con una componente métrica? {#fispm-c04-activaciuxf3n-cuuxe1ndo-una-coordenada-coincide-con-una-componente-muxe9trica}

En §3 una base $B=(e_1,e_2,e_3)$ permitió escribir todo vector de manera única: $v=v^1e_1+v^2e_2+v^3e_3.$ En §5 vimos que, para una base general, no podemos calcular la longitud mediante $\sqrt{(v^1)^2+(v^2)^2+(v^3)^2}$

sin conocer la matriz de Gram. En §6 descubrimos además que una componente escalar en una dirección unitaria se obtiene mediante un producto escalar. La pregunta natural es entonces:

Activación ¿Qué condiciones debe satisfacer una base para que sus coeficientes algebraicos $v^i$ sean exactamente las componentes métricas de $v$ en las tres direcciones de la base?

La respuesta combinará dos propiedades:

- cada vector de la base tiene norma uno;

- vectores de base distintos son ortogonales.

[]{#fispm-c04-definir-base-ortonormal label="fispm-c04-definir-base-ortonormal"}

**Definición 4.23 --- Base ortonormal** Una base ordenada

$$B=(e_1,e_2,e_3)$$

de $V$ es **ortonormal** si

$$\boxed{ \langle e_i,e_j\rangle = \delta_{ij}, }$$

donde

$$\delta_{ij} = \begin{cases} 1,& i=j,\\ 0,& i\ne j. \end{cases}$$

Equivalentemente, $\|e_i\|=1$

para cada $i$, y

$$e_i\perp e_j$$

si $i\ne j$. La palabra **orto-normal** recuerda exactamente estas dos condiciones: ortogonalidad mutua y normalización a longitud uno. Unidades y normalización definición 4.23 está formulada para vectores matemáticamente normalizados una vez fijada la convención de unidades. Al realizar físicamente la geometría, puede factorizarse una escala de longitud común $\ell_0$: si $e_i$ es ortonormal en el sentido de la definición 4.23 y se usan desplazamientos de referencia $b_i=\ell_0e_i$, entonces $\langle b_i,b_j\rangle=\ell_0^2\delta_{ij}.$

Las coordenadas respecto de los $b_i$ pueden mantenerse adimensionales, pero deben conservarse los factores de escala de la matriz de Gram de §5. Equivalentemente, puede trabajarse con direcciones normalizadas y portar la escala física en las componentes. Son convenciones distintas y no deben mezclarse.

Base ortogonal no significa todavía ortonormal Una base puede estar formada por vectores mutuamente ortogonales y, sin embargo, tener

$$\|e_i\|\ne1.$$

En ese caso, las fórmulas de esta sección deben conservar los factores de escala correspondientes.

[]{#la-matriz-de-gram-se-simplifica}

### La matriz de Gram se simplifica {#fispm-c04-la-matriz-de-gram-se-simplifica}

Definición 4.18 definió la matriz de Gram de una base: $G_B = \bigl(\langle e_i,e_j\rangle\bigr)_{i,j}.$ Si $B$ es ortonormal, definición 4.23 implica inmediatamente

$$\boxed{ G_B=I_3. }$$

Por eso la fórmula general de §5, $\|v\|^2 = [v]_B^{\mathsf T}G_B[v]_B,$

se reduce a

$$\|v\|^2 = [v]_B^{\mathsf T}[v]_B.$$

Ésta es la razón estructural de la conocida suma de cuadrados. No es una propiedad de cualquier columna: es una consecuencia de que la matriz de Gram de la base sea la identidad.

[]{#proposición-recuperar-componentes-mediante-productos-escalares}

### Proposición: recuperar componentes mediante productos escalares {#fispm-c04-proposiciuxf3n-recuperar-componentes-mediante-productos-escalares}

**Proposición 4.20 --- Componentes y norma en una base ortonormal** Sea

$$B=(e_1,e_2,e_3)$$

una base ortonormal. Si

$$v=v^1e_1+v^2e_2+v^3e_3,$$

entonces, para cada $k=1,2,3$,

$$\boxed{ v^k=\langle v,e_k\rangle. }$$

Por tanto,

$$\boxed{ v = \sum_{k=1}^{3} \langle v,e_k\rangle e_k }$$

y

$$\boxed{ \|v\|^2 = \sum_{k=1}^{3} \langle v,e_k\rangle^2. }$$

**Demostración.** Partimos de la expansión única de la proposición 4.6:

$$v=\sum_{i=1}^{3}v^ie_i.$$

Tomamos producto escalar con $e_k$:

$$\begin{aligned} \langle v,e_k\rangle &= \left\langle \sum_{i=1}^{3}v^ie_i, e_k \right\rangle\\ &= \sum_{i=1}^{3} v^i\langle e_i,e_k\rangle\\ &= \sum_{i=1}^{3} v^i\delta_{ik}\\ &= v^k. \end{aligned}$$

Esto prueba la primera identidad. Sustituir los coeficientes obtenidos en la expansión de $v$ da $v = \sum_{k=1}^{3} \langle v,e_k\rangle e_k.$ Finalmente, como $G_B=I_3$,

$$\|v\|^2 = (v^1)^2+(v^2)^2+(v^3)^2 = \sum_{k=1}^{3} \langle v,e_k\rangle^2.$$

$\square$

**Lectura guiada.** El paso decisivo es que el producto escalar con $e_k$ «selecciona» exactamente un coeficiente porque todos los términos cruzados desaparecen y $\langle e_k,e_k\rangle=1$.

[]{#relación-con-las-proyecciones-de-6}

### Relación con las proyecciones de §6 {#fispm-c04-relaciuxf3n-con-las-proyecciones-de-6}

Como $\|e_k\|=1$, definición 4.22 produce

$$\operatorname{comp}_{e_k}(v) = \frac{\langle v,e_k\rangle}{\|e_k\|} = \langle v,e_k\rangle.$$

Por proposición 4.20,

$$\boxed{ v^k = \operatorname{comp}_{e_k}(v). }$$

Además, definición 4.20 da

$$\operatorname{proj}_{e_k}(v) = \langle v,e_k\rangle e_k = v^ke_k.$$

Por tanto, en una base ortonormal sí coinciden de manera controlada tres lenguajes:

$$\boxed{ \text{coeficiente algebraico} = \text{componente escalar métrica} }$$

y el término vectorial correspondiente es

$$\boxed{ v^ke_k = \operatorname{proj}_{e_k}(v). }$$

La igualdad no era válida de manera automática en una base general; ahora está demostrada bajo una hipótesis precisa.

[]{#principio-metodológico-y-pregunta-constructiva}

### Principio metodológico y pregunta constructiva {#fispm-c04-principio-metodoluxf3gico-y-pregunta-constructiva}

**Principio metodológico 4.9 --- Verificar ortonormalidad antes de leer componentes métricamente** Antes de usar

$$v^i=\langle v,e_i\rangle$$

o

$$\|v\|^2=\sum_i(v^i)^2,$$

comprobar que la base declarada es ortonormal respecto del producto escalar utilizado.

La base ortonormal convierte una lista de coeficientes en una descripción métrica particularmente simple, pero no elimina la distinción de tipos:

- $v\in V$ es el vector;

- $[v]_B\in\mathbb R^3$ es su columna;

- $v^i$ es un escalar;

- $v^ie_i$ es una proyección vectorial.

Todavía falta responder una pregunta constructiva: dado un conjunto de vectores independientes que **no** es ortonormal, ¿cómo podemos producir a partir de él una base ortonormal?

[]{#la-estrategia-quitar-sucesivamente-las-partes-ya-explicadas}

### La estrategia: quitar sucesivamente las partes ya explicadas {#fispm-c04-la-estrategia-quitar-sucesivamente-las-partes-ya-explicadas}

Sean

$$a_1,a_2,a_3$$

vectores linealmente independientes. El primer vector sólo necesita normalización: $u_1:=a_1, \qquad e_1:=\frac{u_1}{\|u_1\|}.$

Para el segundo vector no basta con normalizar $a_2$, porque podría contener una parte paralela a $e_1$. Primero retiramos esa parte:

$$u_2 := a_2-\operatorname{proj}_{e_1}(a_2) = a_2-\langle a_2,e_1\rangle e_1.$$

Entonces $u_2\perp e_1$ por la proposición 4.16, y normalizamos: $e_2:=\frac{u_2}{\|u_2\|}.$

Con el tercer vector debemos retirar las partes ya explicadas por las dos direcciones anteriores:

$$u_3 := a_3 -\langle a_3,e_1\rangle e_1 -\langle a_3,e_2\rangle e_2,$$

y finalmente

$$e_3:=\frac{u_3}{\|u_3\|}.$$

Antes de aceptar estas fórmulas debemos probar dos cuestiones:

1.  que $u_2$ y $u_3$ no se anulan;

2.  que reemplazar $a_k$ por $e_k$ no cambia los subespacios generados acumulativamente.

[]{#definir-procedimiento-de-gramschmidt-en-dimensión-tres}

### Definir: procedimiento de Gram--Schmidt en dimensión tres {#fispm-c04-definir-procedimiento-de-gramschmidt-en-dimensiuxf3n-tres}

**Definición 4.24 --- Procedimiento de Gram--Schmidt** Sea $(a_1,a_2,a_3)$ una familia linealmente independiente. Definimos recursivamente

$$u_1:=a_1, \qquad e_1:=\frac{u_1}{\|u_1\|},$$

$$u_2 := a_2-\langle a_2,e_1\rangle e_1, \qquad e_2:=\frac{u_2}{\|u_2\|},$$

y

$$u_3 := a_3 -\langle a_3,e_1\rangle e_1 -\langle a_3,e_2\rangle e_2, \qquad e_3:=\frac{u_3}{\|u_3\|}.$$

Cuando los denominadores son no nulos, la familia $(e_1,e_2,e_3)$ se denomina la **ortonormalización de Gram--Schmidt** de $(a_1,a_2,a_3)$ en ese orden. La cláusula «cuando los denominadores son no nulos» no quedará como supuesto adicional: la independencia lineal de los $a_i$ permitirá demostrarlo.

[]{#primer-control-los-residuos-no-pueden-anularse}

### Primer control: los residuos no pueden anularse {#fispm-c04-primer-control-los-residuos-no-pueden-anularse}

Para $u_1$ no hay dificultad: $a_1\ne0$ porque la familia es independiente. Supongamos que

$$u_2=0.$$

Entonces $a_2 = \langle a_2,e_1\rangle e_1.$

Como $e_1$ es un múltiplo no nulo de $a_1$, se seguiría

$$a_2\in\operatorname{span}(a_1),$$

contradiciendo la independencia de $(a_1,a_2)$. Para $u_3$, si

$$u_3=0,$$

entonces

$$a_3 = \langle a_3,e_1\rangle e_1 + \langle a_3,e_2\rangle e_2.$$

Una vez que probemos que

$$\operatorname{span}(e_1,e_2) = \operatorname{span}(a_1,a_2),$$

esto implicará

$$a_3\in\operatorname{span}(a_1,a_2),$$

otra contradicción con la independencia original. Por tanto, la preservación del subespacio generado no es un detalle secundario: forma parte del argumento que garantiza que el algoritmo puede continuar.

[]{#proposición-gramschmidt-preserva-los-subespacios-generados}

### Proposición: Gram--Schmidt preserva los subespacios generados {#fispm-c04-proposiciuxf3n-gramschmidt-preserva-los-subespacios-generados}

**Proposición 4.21 --- Preservación de generación por Gram--Schmidt** Para la construcción de la definición 4.24,

$$\boxed{ \operatorname{span}(e_1) = \operatorname{span}(a_1), }$$

$$\boxed{ \operatorname{span}(e_1,e_2) = \operatorname{span}(a_1,a_2), }$$

y

$$\boxed{ \operatorname{span}(e_1,e_2,e_3) = \operatorname{span}(a_1,a_2,a_3). }$$

**Demostración.** Como $e_1=a_1/\|a_1\|$, cada uno es un múltiplo no nulo del otro. Por tanto generan el mismo subespacio. Para la segunda etapa, definición 4.24 da

$$u_2 = a_2-\langle a_2,e_1\rangle e_1.$$

Así, $u_2\in\operatorname{span}(a_1,a_2),$

pues $e_1\in\operatorname{span}(a_1)$. Como $e_2$ es un múltiplo no nulo de $u_2$, $e_2\in\operatorname{span}(a_1,a_2).$ Luego

$$\operatorname{span}(e_1,e_2) \subseteq \operatorname{span}(a_1,a_2).$$

En sentido inverso,

$$a_2 = u_2+\langle a_2,e_1\rangle e_1 = \|u_2\|e_2 + \langle a_2,e_1\rangle e_1,$$

de modo que $a_2\in\operatorname{span}(e_1,e_2)$; junto con $a_1\in\operatorname{span}(e_1)$ obtenemos la igualdad. Para la tercera etapa,

$$u_3 = a_3 -\langle a_3,e_1\rangle e_1 -\langle a_3,e_2\rangle e_2.$$

Por la igualdad ya probada, $e_1,e_2\in\operatorname{span}(a_1,a_2),$

así que

$$u_3\in\operatorname{span}(a_1,a_2,a_3).$$

Luego $e_3$ pertenece al mismo subespacio y obtenemos una inclusión. La inclusión inversa se sigue de

$$a_3 = \|u_3\|e_3 + \langle a_3,e_1\rangle e_1 + \langle a_3,e_2\rangle e_2.$$

Por tanto los tres subespacios acumulativos coinciden. $\square$ Esta proposición completa también el argumento de §7.9: la independencia inicial garantiza que $u_2\ne0$ y $u_3\ne0$.

[]{#proposición-el-resultado-es-ortonormal}

### Proposición: el resultado es ortonormal {#fispm-c04-proposiciuxf3n-el-resultado-es-ortonormal}

**Proposición 4.22 --- Corrección de Gram--Schmidt** Si $(a_1,a_2,a_3)$ es linealmente independiente, el procedimiento definición 4.24 está bien definido y produce una familia

$$B=(e_1,e_2,e_3)$$

ortonormal. Si además $(a_1,a_2,a_3)$ es una base de $V$, entonces $B$ es una base ortonormal de $V$.

**Demostración.** §7.9 y proposición 4.21 garantizan que todos los $u_i$ son no nulos, por lo que cada normalización está definida y

$$\|e_i\|=1.$$

Por proposición 4.16, $u_2\perp e_1,$

y multiplicar $u_2$ por el escalar positivo $1/\|u_2\|$ conserva la ortogonalidad: $e_2\perp e_1.$ Para $u_3$, calculamos

$$\begin{aligned} \langle u_3,e_1\rangle &= \langle a_3,e_1\rangle -\langle a_3,e_1\rangle\langle e_1,e_1\rangle -\langle a_3,e_2\rangle\langle e_2,e_1\rangle\\ &=0, \end{aligned}$$

porque $\|e_1\|=1$ y $e_2\perp e_1$. De manera análoga, $\langle u_3,e_2\rangle=0.$ Al normalizar $u_3$, obtenemos $e_3\perp e_1, \qquad e_3\perp e_2.$ Así los tres vectores son unitarios y mutuamente ortogonales: forman una familia ortonormal. Finalmente, si $(a_1,a_2,a_3)$ genera $V$, proposición 4.21 da $\operatorname{span}(e_1,e_2,e_3)=V.$

Una familia ortonormal de vectores no nulos es linealmente independiente: si

$$c_1e_1+c_2e_2+c_3e_3=0,$$

tomar producto escalar con $e_k$ da $c_k=0$. Por definición 4.9, $B$ es una base. $\square$

[]{#el-orden-importa-el-subespacio-final-no}

### El orden importa, el subespacio final no {#fispm-c04-el-orden-importa-el-subespacio-final-no}

El procedimiento definición 4.24 utiliza un **orden**. Si comenzamos con

$$(a_1,a_2,a_3)$$

o con otra permutación de esos vectores, normalmente obtenemos bases ortonormales distintas. No obstante, proposición 4.21 garantiza que, para cualquier orden al que pueda aplicarse el procedimiento sobre la misma familia independiente completa, el subespacio final generado es el mismo:

$$\boxed{ \operatorname{span}(e_1,e_2,e_3) = \operatorname{span}(a_1,a_2,a_3). }$$

Por tanto Gram--Schmidt no descubre una base ortonormal **canónica** sin datos adicionales. Construye una base ortonormal compatible con el orden elegido.

**Principio metodológico 4.10 --- Ortonormalizar sin perder el espacio generado** En Gram--Schmidt, comprobar en cada etapa dos invariantes: el nuevo residuo es ortogonal a las direcciones ya construidas y el subespacio generado acumulativo coincide con el de los vectores originales procesados.

[]{#balance-antes-de-los-ejemplos-y-ejercicios}

### Balance antes de los ejemplos y ejercicios {#fispm-c04-balance-antes-de-los-ejemplos-y-ejercicios}

Ya sabemos:

1.  reconocer una base ortonormal;

2.  recuperar componentes mediante productos escalares;

3.  construir una base ortonormal a partir de una familia independiente;

4.  demostrar que el procedimiento preserva el subespacio generado.

Todavía falta aplicar el procedimiento en un caso concreto y cerrar el bloque §§4--7 con los ejercicios 4.14--4.15.

[]{#ejemplo-guiado-ortonormalizar-una-base-oblicua-simple}

### Ejemplo guiado: ortonormalizar una base oblicua simple {#fispm-c04-ejemplo-guiado-ortonormalizar-una-base-oblicua-simple}

Sea

$$F=(f_1,f_2,f_3)$$

una base ortonormal conocida. Consideremos la familia

$$a_1=f_1+f_2, \qquad a_2=f_2, \qquad a_3=f_3.$$

Es linealmente independiente: si

$$\alpha a_1+\beta a_2+\gamma a_3=0,$$

entonces $\alpha f_1+(\alpha+\beta)f_2+\gamma f_3=0,$

y la independencia de $F$ obliga a

$$\alpha=0, \qquad \beta=0, \qquad \gamma=0.$$

Aplicamos definición 4.24. Primero, $u_1=a_1=f_1+f_2,$

y

$$\|u_1\| = \sqrt{2}.$$

Por tanto,

$$\boxed{ e_1 = \frac{f_1+f_2}{\sqrt2}. }$$

Para el segundo vector,

$$\langle a_2,e_1\rangle = \left\langle f_2, \frac{f_1+f_2}{\sqrt2} \right\rangle = \frac1{\sqrt2}.$$

Entonces

$$\begin{aligned} u_2 &= a_2-\langle a_2,e_1\rangle e_1\\ &= f_2 - \frac1{\sqrt2} \frac{f_1+f_2}{\sqrt2}\\ &= -\frac12f_1+\frac12f_2. \end{aligned}$$

Su norma es $\|u_2\| = \frac1{\sqrt2},$

de modo que

$$\boxed{ e_2 = \frac{-f_1+f_2}{\sqrt2}. }$$

Finalmente, como $f_3$ es ortogonal a $e_1$ y $e_2$,

$$u_3=f_3, \qquad \boxed{e_3=f_3.}$$

La base obtenida es

$$\boxed{ B= \left( \frac{f_1+f_2}{\sqrt2}, \frac{-f_1+f_2}{\sqrt2}, f_3 \right). }$$

Una comprobación directa da $\langle e_i,e_j\rangle = \delta_{ij}.$

Gram--Schmidt no ha cambiado el espacio generado:

$$\operatorname{span}(a_1,a_2,a_3) = \operatorname{span}(e_1,e_2,e_3) = V.$$

[]{#fispm-t1-c04-e0014}

**Ejercicio 4.14 --- Ejecutar Gram--Schmidt y auditar cada etapa.**

**Función pedagógica:** `Construcción → Verificación → Preservación del generado`

Sea $F=(f_1,f_2,f_3)$ una base ortonormal y

$$a_1=f_1+f_2, \qquad a_2=f_2, \qquad a_3=f_3.$$

1.  Aplica Gram--Schmidt en el orden dado.

2.  Comprueba que los residuos que se normalizan son no nulos.

3.  Verifica directamente que la familia final es ortonormal.

4.  Comprueba que

$$\operatorname{span}(a_1,a_2) = \operatorname{span}(e_1,e_2).$$

**Solución desarrollada**

El primer paso da $e_1 = \frac{f_1+f_2}{\sqrt2}.$

Después,

$$u_2 = f_2-\frac12(f_1+f_2) = -\frac12f_1+\frac12f_2 \ne0,$$

y

$$e_2 = \frac{-f_1+f_2}{\sqrt2}.$$

Como $f_3$ es ortogonal a los dos primeros, $u_3=f_3\ne0, \qquad e_3=f_3.$

Las normas son uno y

$$\langle e_1,e_2\rangle = \frac{-1+1}{2} = 0,$$

mientras

$$\langle e_1,e_3\rangle = \langle e_2,e_3\rangle = 0.$$

Para el generado,

$$e_1,e_2 \in \operatorname{span}(f_1,f_2) = \operatorname{span}(a_1,a_2).$$

Recíprocamente, $a_1 = \sqrt2\,e_1,$

y, usando

$$f_2 = \frac{e_1+e_2}{\sqrt2},$$

obtenemos $a_2 = \frac{e_1+e_2}{\sqrt2}.$ Por tanto,

$$\boxed{ \operatorname{span}(a_1,a_2) = \operatorname{span}(e_1,e_2). }$$

[]{#fispm-t1-c04-e0015}

**Ejercicio 4.15 --- Recuperar componentes y norma en la nueva base.**

**Función pedagógica:** `Producto escalar → Componentes → Reconstrucción → Parseval finito`

En la base ortonormal

$$B= \left( e_1,e_2,e_3 \right) = \left( \frac{f_1+f_2}{\sqrt2}, \frac{-f_1+f_2}{\sqrt2}, f_3 \right),$$

sea

$$v=3f_1+f_2+2f_3.$$

1.  Calcula $\langle v,e_1\rangle$, $\langle v,e_2\rangle$, $\langle v,e_3\rangle$.

2.  Escribe $[v]_B$.

3.  Reconstruye $v$ desde esas componentes.

4.  Verifica

$$\|v\|^2 = \sum_{i=1}^{3} \langle v,e_i\rangle^2.$$

**Solución desarrollada**

Primero,

$$\langle v,e_1\rangle = \frac{3+1}{\sqrt2} = 2\sqrt2.$$

Luego,

$$\langle v,e_2\rangle = \frac{-3+1}{\sqrt2} = -\sqrt2.$$

Finalmente, $\langle v,e_3\rangle = 2.$ Por proposición 4.20,

$$\boxed{ [v]_B = \begin{pmatrix} 2\sqrt2\\ -\sqrt2\\ 2 \end{pmatrix}. }$$

La reconstrucción es

$$\begin{aligned} v &= 2\sqrt2\,e_1 -\sqrt2\,e_2 +2e_3\\ &= 2(f_1+f_2) +(f_1-f_2) +2f_3\\ &= 3f_1+f_2+2f_3. \end{aligned}$$

Finalmente, $\|v\|^2 = 3^2+1^2+2^2 = 14$

en la base ortonormal $F$, mientras que

$$(2\sqrt2)^2+(-\sqrt2)^2+2^2 = 8+2+4 = 14.$$

Por tanto,

$$\boxed{ \|v\|^2 = \sum_{i=1}^{3} \langle v,e_i\rangle^2. }$$

[]{#cierre-de-7}

### Cierre de §7 {#fispm-c04-cierre-de-7}

La secuencia §§5--7 ha construido progresivamente la geometría euclídea:

$$\boxed{ \text{producto escalar} \longrightarrow \text{norma y distancia} \longrightarrow \text{proyección y ángulo} \longrightarrow \text{base ortonormal}. }$$

Una base ortonormal es especial porque reúne la estructura algebraica de una base y la estructura métrica del producto escalar. Sólo bajo esta hipótesis quedan justificadas simultáneamente las fórmulas

$$\boxed{ v^i=\langle v,e_i\rangle, }$$

$$\boxed{ v = \sum_i \langle v,e_i\rangle e_i, }$$

y

$$\boxed{ \|v\|^2 = \sum_i(v^i)^2. }$$

Gram--Schmidt demuestra además que, a partir de una base cualquiera de un espacio euclídeo finito, podemos construir una base ortonormal sin cambiar el espacio generado. Con ello queda cerrada la construcción métrica iniciada en §4. El siguiente paso será el §[8](#fispm-c04-orientaciuxf3n-y-determinantes).

[]{#orientación-y-determinantes}

[]{#fispm-t1-c04-s08}

[]{#fpm-i-04-s08}

## 8. Orientación y determinantes {#fispm-c04-orientaciuxf3n-y-determinantes}

[]{#activación-una-base-ordenada-puede-tener-dos-sentidos}

### Activación: una base ordenada puede tener dos "sentidos" {#fispm-c04-activaciuxf3n-una-base-ordenada-puede-tener-dos-sentidos}

Una base ordenada tridimensional

$$B=(b_1,b_2,b_3)$$

no sólo proporciona tres direcciones independientes. El **orden** de esas direcciones contiene información adicional. Si intercambiamos dos vectores, por ejemplo

$$B'=(b_2,b_1,b_3),$$

seguimos teniendo los mismos tres vectores y el mismo espacio generado. Sin embargo, hemos invertido algo que no puede detectarse mediante longitudes ni ángulos por sí solos. Ese dato adicional es la **orientación**. Para describirlo necesitamos una cantidad algebraica que:

- se anule cuando los tres vectores dejan de ser independientes;

- cambie de signo cuando intercambiamos dos de ellos;

- permita distinguir dos clases de bases ordenadas.

Esa cantidad es el determinante.

[]{#definir-determinante-de-una-matriz-real-3-3}

### Definir: determinante de una matriz real 3 × 3 {#fispm-c04-definir-determinante-de-una-matriz-real-3-3}

**Definición 4.25 --- Determinante tridimensional** Para

$$A= \begin{pmatrix} a_{11}&a_{12}&a_{13}\\ a_{21}&a_{22}&a_{23}\\ a_{31}&a_{32}&a_{33} \end{pmatrix},$$

definimos

$$\boxed{ \begin{aligned} \det A &= a_{11}a_{22}a_{33} +a_{12}a_{23}a_{31} +a_{13}a_{21}a_{32}\\ &\quad -a_{13}a_{22}a_{31} -a_{12}a_{21}a_{33} -a_{11}a_{23}a_{32}. \end{aligned} }$$

Esta expresión es un escalar asociado a una matriz cuadrada de orden tres. En particular, $\det I_3=1.$ Todavía no interpretamos el valor absoluto como volumen; por ahora nos interesa principalmente su **signo**.

[]{#determinante-de-una-terna-de-vectores-respecto-de-una-base}

### Determinante de una terna de vectores respecto de una base {#fispm-c04-determinante-de-una-terna-de-vectores-respecto-de-una-base}

Fijemos temporalmente una base ordenada de referencia

$$E=(e_1,e_2,e_3).$$

Para tres vectores $v_1,v_2,v_3\in V$, formamos la matriz cuyas columnas son sus componentes en $E$:

$$A_E(v_1,v_2,v_3) := \begin{pmatrix} \vert&\vert&\vert\\ {}[v_1]_E&[v_2]_E&[v_3]_E\\ \vert&\vert&\vert \end{pmatrix}.$$

Definimos entonces la abreviatura

$$\boxed{ \det_E(v_1,v_2,v_3) := \det A_E(v_1,v_2,v_3). }$$

Si tomamos precisamente la terna de referencia, $\det_E(e_1,e_2,e_3)=1.$

[]{#primera-propiedad-intercambiar-dos-columnas-cambia-el-signo}

### Primera propiedad: intercambiar dos columnas cambia el signo {#fispm-c04-primera-propiedad-intercambiar-dos-columnas-cambia-el-signo}

**Proposición 4.23 --- Regla de intercambio** Si $A'$ se obtiene de una matriz $A$ intercambiando dos columnas, entonces

$$\boxed{ \det A'=-\det A. }$$

En particular,

$$\boxed{ \det_E(v_2,v_1,v_3) = -\det_E(v_1,v_2,v_3). }$$

**Demostración.** Basta comprobar un intercambio elemental, por ejemplo las dos primeras columnas. Escribimos

$$A= \begin{pmatrix} a&b&c\\ d&e&f\\ g&h&i \end{pmatrix},$$

de modo que

$$\det A = aei+bfg+cdh-ceg-bdi-afh.$$

Tras intercambiar las dos primeras columnas,

$$A'= \begin{pmatrix} b&a&c\\ e&d&f\\ h&g&i \end{pmatrix}.$$

Por definición 4.25, $\det A' = bdi+afh+ceg-cdh-aei-bfg.$

Reordenando términos,

$$\det A' = -\bigl(aei+bfg+cdh-ceg-bdi-afh\bigr) = -\det A.$$

Los demás intercambios se comprueban de la misma manera. $\square$ La regla de signo no depende de longitudes ni de ortogonalidad. Es consecuencia de la estructura algebraica del determinante.

[]{#consecuencia-una-permutación-impar-invierte-el-signo}

### Consecuencia: una permutación impar invierte el signo {#fispm-c04-consecuencia-una-permutaciuxf3n-impar-invierte-el-signo}

Si partimos de

$$(v_1,v_2,v_3)$$

y realizamos un solo intercambio, el determinante cambia de signo. Dos intercambios sucesivos producen

$$(-1)^2=1,$$

por lo que restauran el signo original. Por ejemplo,

$$(v_1,v_2,v_3) \longrightarrow (v_2,v_1,v_3) \longrightarrow (v_2,v_3,v_1)$$

realiza dos intercambios y conserva el signo. Esto anticipa la distinción entre permutaciones **pares** e **impares**, pero no necesitamos todavía formalizar el grupo de permutaciones.

[]{#definir-orientación-relativa-a-una-base-de-referencia}

### Definir: orientación relativa a una base de referencia {#fispm-c04-definir-orientaciuxf3n-relativa-a-una-base-de-referencia}

**Definición 4.26 --- Orientación relativa** Fijemos una base ordenada de referencia

$$E=(e_1,e_2,e_3).$$

Sea

$$B=(b_1,b_2,b_3)$$

otra base ordenada. Diremos que $B$ tiene **orientación positiva respecto de $E$** si

$$\boxed{ \det_E(b_1,b_2,b_3)>0, }$$

y **orientación negativa respecto de $E$** si

$$\boxed{ \det_E(b_1,b_2,b_3)<0. }$$

Como $B$ es una base, esperamos que el determinante no sea cero. La demostración general de la equivalencia

$$\det A\ne0 \Longleftrightarrow \text{columnas independientes}$$

se demostrará en §§8.9--8.12, junto con las propiedades estructurales necesarias del determinante. Por ahora, definición 4.26 se aplica a las bases para las que ya hemos verificado directamente que el determinante es no nulo.

[]{#ejemplo-inmediato-invertir-dos-ejes}

### Ejemplo inmediato: invertir dos ejes {#fispm-c04-ejemplo-inmediato-invertir-dos-ejes}

La base de referencia satisface $\det_E(e_1,e_2,e_3)=1>0.$ Por proposición 4.23, $\det_E(e_2,e_1,e_3)=-1.$ Por tanto, $(e_1,e_2,e_3)$

y

$$(e_2,e_1,e_3)$$

poseen orientaciones relativas opuestas. Sin embargo, ambas bases tienen exactamente los mismos vectores y, si $E$ era ortonormal, la base obtenida al intercambiar dos elementos también es ortonormal. Ortonormalidad no fija la orientación Una base puede conservar todas las longitudes y todos los ángulos entre sus vectores y, aun así, invertir la orientación al intercambiar dos ejes.

[]{#principio-metodológico-y-cuestiones-pendientes}

### Principio metodológico y cuestiones pendientes {#fispm-c04-principio-metodoluxf3gico-y-cuestiones-pendientes}

**Principio metodológico 4.11 --- Separar métrica y orientación** Longitudes, ángulos y ortonormalidad pertenecen a la estructura métrica; la orientación añade un dato de signo asociado al orden de una base. No inferir orientación únicamente a partir de productos escalares.

Hasta aquí hemos introducido:

$$\boxed{ \det A }$$

como escalar algebraico y hemos aislado su papel más elemental:

$$\boxed{ \text{intercambiar dos vectores} \Longrightarrow \text{cambiar el signo del determinante}. }$$

Esto permite hablar de orientación **relativa a una base elegida**, pero todavía falta demostrar de manera sistemática:

- cuándo el determinante es cero;

- cómo se comporta bajo combinaciones lineales;

- cómo se relacionan orientaciones definidas usando distintas bases de referencia.

[]{#proposición-multilinealidad-y-alternancia}

### Proposición: multilinealidad y alternancia {#fispm-c04-proposiciuxf3n-multilinealidad-y-alternancia}

**Proposición 4.24 --- El determinante es trilineal y alternante** Fijada una base de referencia $E$, la aplicación

$$(v_1,v_2,v_3) \longmapsto \det_E(v_1,v_2,v_3)$$

es lineal en cada argumento por separado. Además, si dos argumentos coinciden, entonces

$$\boxed{ \det_E(v_1,v_2,v_3)=0. }$$

**Demostración de la linealidad en el primer argumento.** Sean $u,w,v_2,v_3\in V$ y $\alpha,\beta\in\mathbb R$. Por linealidad de las coordenadas,

$$[\alpha u+\beta w]_E = \alpha[u]_E+\beta[w]_E.$$

Al sustituir esta columna en la fórmula explícita definición 4.25, cada término depende linealmente de las entradas de la primera columna. Por tanto,

$$\boxed{ \det_E(\alpha u+\beta w,v_2,v_3) = \alpha\det_E(u,v_2,v_3) + \beta\det_E(w,v_2,v_3). }$$

La misma inspección de la definición 4.25 prueba linealidad en la segunda y tercera columnas. Para la alternancia, si las dos primeras columnas coinciden, proposición 4.23 da simultáneamente

$$\det_E(v,v,v_3) = -\det_E(v,v,v_3).$$

Luego

$$2\det_E(v,v,v_3)=0,$$

y como trabajamos sobre $\mathbb R$, $\det_E(v,v,v_3)=0.$

Los demás casos se reducen a éste intercambiando columnas. $\square$

[]{#consecuencia-dependencia-lineal-implica-determinante-cero}

### Consecuencia: dependencia lineal implica determinante cero {#fispm-c04-consecuencia-dependencia-lineal-implica-determinante-cero}

**Proposición 4.25 --- Una terna dependiente tiene determinante nulo** Si $v_1,v_2,v_3$ son linealmente dependientes, entonces

$$\boxed{ \det_E(v_1,v_2,v_3)=0. }$$

**Demostración.** Si uno de los vectores es cero, la multilinealidad da inmediatamente determinante cero. Supongamos entonces que ninguno es cero y que, por ejemplo,

$$v_3=\alpha v_1+\beta v_2.$$

Por linealidad en el tercer argumento,

$$\begin{aligned} \det_E(v_1,v_2,v_3) &= \det_E(v_1,v_2,\alpha v_1+\beta v_2)\\ &= \alpha\det_E(v_1,v_2,v_1) + \beta\det_E(v_1,v_2,v_2). \end{aligned}$$

Cada término se anula por alternancia. Luego

$$\det_E(v_1,v_2,v_3)=0.$$

Si la relación de dependencia despeja otro vector, el argumento es idéntico. $\square$ La implicación recíproca todavía requiere una propiedad adicional: la multiplicatividad.

[]{#proposición-multiplicatividad-del-determinante}

### Proposición: multiplicatividad del determinante {#fispm-c04-proposiciuxf3n-multiplicatividad-del-determinante}

**Proposición 4.26 --- Determinante de un producto** Para matrices reales $3\times3$,

$$\boxed{ \det(AB)=\det(A)\det(B). }$$

**Demostración.** Escribamos las columnas de $A$ como

$$A= \begin{pmatrix} \vert&\vert&\vert\\ a_1&a_2&a_3\\ \vert&\vert&\vert \end{pmatrix},$$

y las de $B$ mediante sus entradas $b_{ij}$. La columna $j$ de $AB$ es $b_{1j}a_1+b_{2j}a_2+b_{3j}a_3.$ Por trilinealidad, $\det(AB)$

se expande como suma de términos de la forma $b_{i1}b_{j2}b_{k3}\det(a_i,a_j,a_k).$

Todo término con índices repetidos se anula por alternancia. Sólo sobreviven las seis permutaciones de $(1,2,3)$. Cada permutación aporta

$$\pm b_{i1}b_{j2}b_{k3}\det(a_1,a_2,a_3),$$

donde el signo es precisamente el signo de la permutación, por la proposición 4.23. Factorizando,

$$\det(AB) = \det(A) \Bigl( b_{11}b_{22}b_{33} +b_{21}b_{32}b_{13} +b_{31}b_{12}b_{23} -b_{31}b_{22}b_{13} -b_{21}b_{12}b_{33} -b_{11}b_{32}b_{23} \Bigr).$$

La expresión entre paréntesis es exactamente $\det(B)$ escrita por columnas. Por tanto, $\det(AB)=\det(A)\det(B).$

$\square$

[]{#proposición-determinante-no-nulo-e-independencia}

### Proposición: determinante no nulo e independencia {#fispm-c04-proposiciuxf3n-determinante-no-nulo-e-independencia}

**Proposición 4.27 --- Criterio de base mediante el determinante** Sean $v_1,v_2,v_3\in V$ y sea

$$A= A_E(v_1,v_2,v_3).$$

Entonces

$$\boxed{ \det A\ne0 \Longleftrightarrow (v_1,v_2,v_3) \text{ es linealmente independiente}. }$$

En dimensión tres, esto equivale a que $(v_1,v_2,v_3)$ sea una base de $V$.

**Demostración.** Si la terna es dependiente, proposición 4.25 da

$$\det A=0.$$

Por contraposición,

$$\det A\ne0 \Longrightarrow (v_1,v_2,v_3) \text{ independiente}.$$

Para la otra dirección, supongamos que

$$B=(v_1,v_2,v_3)$$

es una base. Como $E$ también es base, cada $e_j$ posee coordenadas únicas en $B$. Sea $C$ la matriz cuyas columnas son esas coordenadas:

$$C= \begin{pmatrix} \vert&\vert&\vert\\ {}[e_1]_B&[e_2]_B&[e_3]_B\\ \vert&\vert&\vert \end{pmatrix}.$$

La matriz $A$ convierte componentes en $B$ a componentes en $E$, de modo que

$$AC=I_3.$$

Aplicando proposición 4.26, $1 = \det I_3 = \det(A)\det(C).$ Por tanto, $\det(A)\ne0.$

Esto prueba la equivalencia. $\square$ La observación pendiente de §8.6 queda ahora justificada: toda base ordenada tiene determinante no nulo respecto de cualquier base de referencia.

[]{#definir-misma-orientación-entre-bases}

### Definir: misma orientación entre bases {#fispm-c04-definir-misma-orientaciuxf3n-entre-bases}

**Definición 4.27 --- Bases con la misma orientación** Sean

$$B=(b_1,b_2,b_3), \qquad C=(c_1,c_2,c_3)$$

bases ordenadas de $V$. Diremos que $B$ y $C$ tienen la **misma orientación** si la matriz de cambio de componentes de $C$ a $B$ tiene determinante positivo. Equivalentemente, fijada cualquier base de referencia $E$,

$$\boxed{ \det_E(B)\det_E(C)>0. }$$

Tienen **orientaciones opuestas** si ese producto es negativo.

Aquí usamos la abreviatura

$$\det_E(B) := \det_E(b_1,b_2,b_3).$$

La equivalencia entre ambas formulaciones se justificará de inmediato.

[]{#proposición-la-comparación-de-orientación-no-depende-de-la-referencia}

### Proposición: la comparación de orientación no depende de la referencia {#fispm-c04-proposiciuxf3n-la-comparaciuxf3n-de-orientaciuxf3n-no-depende-de-la-referencia}

**Proposición 4.28 --- Invariancia de la comparación de orientación** El signo de

$$\det_E(B)\det_E(C)$$

no depende de la base de referencia $E$.

**Demostración.** Sea $F$ otra base de referencia. Denotemos por $S$ la matriz cuyas columnas son los vectores de $F$ expresados en $E$. Entonces, para cualquier base $B$,

$$A_E(B) = S\,A_F(B).$$

Por proposición 4.26, $\det_E(B) = \det(S)\det_F(B).$

Análogamente, $\det_E(C) = \det(S)\det_F(C).$ Por tanto,

$$\det_E(B)\det_E(C) = \det(S)^2 \det_F(B)\det_F(C).$$

Como $F$ es una base, proposición 4.27 garantiza

$$\det(S)\ne0,$$

y por ello

$$\det(S)^2>0.$$

Multiplicar por un número positivo no cambia el signo. Luego ambas referencias producen la misma comparación de orientación. $\square$

[]{#las-bases-se-separan-en-dos-clases}

### Las bases se separan en dos clases {#fispm-c04-las-bases-se-separan-en-dos-clases}

Definición 4.27 y proposición 4.28 permiten olvidar una base de referencia particular y hablar simplemente de dos clases de bases ordenadas. Fijada una base $E$:

- todas las bases con $$\det_E(B)>0$$ pertenecen a una clase;

- todas las bases con $$\det_E(B)<0$$ pertenecen a la otra. Proposición 4.23 muestra que intercambiar dos vectores de una base pasa de una clase a la otra. Dos intercambios restauran la clase original.

**Principio metodológico 4.12 --- La orientación es una clase, no un número** El valor concreto de un determinante depende de la base usada para expresar los vectores; la orientación conserva sólo la información de signo relativa entre bases. Al cambiar de referencia, distinguir el factor de escala del dato binario de orientación.

[]{#balance-de-la-orientación-al-volumen}

### Balance: de la orientación al volumen {#fispm-c04-balance-de-la-orientaciuxf3n-al-volumen}

Ya disponemos de la estructura mínima necesaria:

$$\boxed{ \text{trilinealidad} + \text{alternancia} + \text{multiplicatividad} }$$

y de sus dos consecuencias centrales:

$$\boxed{ \det A\ne0 \Longleftrightarrow \text{columnas independientes}, }$$

$$\boxed{ \text{las bases ordenadas se dividen en dos clases de orientación}. }$$

Todavía falta interpretar geométricamente el **valor absoluto** del determinante y conectar esa interpretación con volumen, ortonormalidad y los ejercicios de §8.

[]{#reglas-geométricas-que-ya-contiene-el-determinante}

### Reglas geométricas que ya contiene el determinante {#fispm-c04-reglas-geomuxe9tricas-que-ya-contiene-el-determinante}

Proposición 4.24 y proposición 4.23 permiten leer tres operaciones elementales directamente en el determinante. Si multiplicamos una arista por un escalar $\lambda$,

$$\det_E(\lambda v_1,v_2,v_3) = \lambda\det_E(v_1,v_2,v_3).$$

Si añadimos a una arista un múltiplo de otra,

$$\begin{aligned} \det_E(v_1+\lambda v_2,v_2,v_3) &= \det_E(v_1,v_2,v_3) + \lambda\det_E(v_2,v_2,v_3)\\ &= \det_E(v_1,v_2,v_3). \end{aligned}$$

Y si intercambiamos dos aristas, $\det_E(v_2,v_1,v_3) = -\det_E(v_1,v_2,v_3).$

Estas tres reglas anticipan exactamente el comportamiento geométrico esperado de un volumen orientado:

- escalar una arista escala el volumen;

- una cizalla paralela a otra arista no cambia el volumen;

- intercambiar dos aristas conserva el tamaño pero invierte el signo de orientación.

[]{#definir-volumen-orientado-y-volumen-euclídeo}

### Definir: volumen orientado y volumen euclídeo {#fispm-c04-definir-volumen-orientado-y-volumen-eucluxeddeo}

Fijemos ahora una base **ortonormal** y una de las dos clases de orientación como positiva: $E=(e_1,e_2,e_3).$

**Definición 4.28 --- Volumen orientado de una terna** Para $v_1,v_2,v_3\in V$, definimos el **volumen orientado respecto de $E$** por

$$\boxed{ \operatorname{Vol}^{\mathrm{or}}_E(v_1,v_2,v_3) := \det_E(v_1,v_2,v_3). }$$

El **volumen euclídeo** del paralelepípedo generado por la terna es

$$\boxed{ \operatorname{Vol}(v_1,v_2,v_3) := \left| \operatorname{Vol}^{\mathrm{or}}_E(v_1,v_2,v_3) \right|. }$$

La ortonormalidad de $E$ es esencial para esta lectura métrica. Si usáramos una base de referencia oblicua y no normalizada, el determinante de coordenadas mediría el volumen en unidades del paralelepípedo fundamental de esa base, no directamente en la escala euclídea normalizada. **Convención de unidades.** definición 4.28 utiliza la normalización matemática fijada en §7. Cuando una realización física introduce una escala común de longitud $\ell_0$, los desplazamientos de referencia $b_i=\ell_0e_i$ aportan un factor $\ell_0^3$ al volumen físico. Así, el valor numérico $|\det_E(v_1,v_2,v_3)|$ debe interpretarse junto con la escala de longitud declarada; si la unidad normalizada es $1\,\mathrm m$, un valor $24$ corresponde a $24\,\mathrm{m^3}$. Para bases dimensionales no normalizadas, debe conservarse además el volumen de su paralelepípedo fundamental. Por el momento estas expresiones están escritas respecto de $E$. Después de la proposición 4.30 demostraremos que el valor absoluto es independiente de la base ortonormal de referencia y que el signo depende únicamente de la clase de orientación elegida. El signo registra orientación; el valor absoluto registra tamaño.

[]{#proposición-reglas-del-volumen-orientado}

### Proposición: reglas del volumen orientado {#fispm-c04-proposiciuxf3n-reglas-del-volumen-orientado}

**Proposición 4.29 --- Escala, cizalla y orientación del volumen** Para toda terna $v_1,v_2,v_3$ y todo $\lambda\in\mathbb R$:

$$\boxed{ \operatorname{Vol}^{\mathrm{or}}_E(\lambda v_1,v_2,v_3) = \lambda \operatorname{Vol}^{\mathrm{or}}_E(v_1,v_2,v_3), }$$

$$\boxed{ \operatorname{Vol}^{\mathrm{or}}_E(v_1+\lambda v_2,v_2,v_3) = \operatorname{Vol}^{\mathrm{or}}_E(v_1,v_2,v_3), }$$

y

$$\boxed{ \operatorname{Vol}^{\mathrm{or}}_E(v_2,v_1,v_3) = - \operatorname{Vol}^{\mathrm{or}}_E(v_1,v_2,v_3). }$$

En consecuencia, el volumen euclídeo no cambia al intercambiar dos aristas ni al realizar la cizalla anterior.

**Demostración.** Cada identidad es exactamente una aplicación de la proposición 4.24 y proposición 4.23 a definición 4.28. Al tomar valor absoluto, el cambio de signo desaparece. $\square$

[]{#proposición-una-base-ortonormal-tiene-determinante-1}

### Proposición: una base ortonormal tiene determinante ±1 {#fispm-c04-proposiciuxf3n-una-base-ortonormal-tiene-determinante-1}

**Proposición 4.30 --- Determinante de una base ortonormal** Sea

$$B=(b_1,b_2,b_3)$$

una base ortonormal y sea $E$ una base ortonormal de referencia. Entonces

$$\boxed{ \det_E(B)=\pm1. }$$

Por tanto,

$$\boxed{ \operatorname{Vol}(b_1,b_2,b_3)=1. }$$

**Demostración.** Sea

$$Q= A_E(b_1,b_2,b_3).$$

Como $E$ es ortonormal, los productos escalares entre columnas de $Q$ se calculan mediante el producto matricial usual. La ortonormalidad de $B$ equivale a

$$Q^{\mathsf T}Q=I_3.$$

Por inspección directa de la definición 4.25, $\det(Q^{\mathsf T})=\det(Q).$

Aplicando proposición 4.26,

$$1 = \det I_3 = \det(Q^{\mathsf T}Q) = \det(Q^{\mathsf T})\det(Q) = \det(Q)^2.$$

Por tanto, $\det(Q)=\pm1.$

El valor absoluto es uno. $\square$ Esta proposición separa limpiamente dos posibilidades: $\det_E(B)=+1$

si $B$ tiene la misma orientación que $E$, y

$$\det_E(B)=-1$$

si tiene la orientación opuesta.

[]{#proposición-independencia-de-la-referencia-ortonormal}

### Proposición: independencia de la referencia ortonormal {#fispm-c04-proposiciuxf3n-independencia-de-la-referencia-ortonormal}

**Proposición 4.31 --- Invariancia del volumen bajo cambio de referencia ortonormal** Sean

$$E=(e_1,e_2,e_3)$$

y

$$F=(f_1,f_2,f_3)$$

bases ortonormales. Para toda terna $v_1,v_2,v_3$:

1.  si $E$ y $F$ tienen la misma orientación,

$$\boxed{ \det_E(v_1,v_2,v_3) = \det_F(v_1,v_2,v_3); }$$

1.  si tienen orientaciones opuestas,

$$\boxed{ \det_E(v_1,v_2,v_3) = -\det_F(v_1,v_2,v_3); }$$

1.  en ambos casos,

$$\boxed{ |\det_E(v_1,v_2,v_3)| = |\det_F(v_1,v_2,v_3)|. }$$

Por tanto, una vez fijada una clase de orientación positiva, el volumen orientado es independiente de la base ortonormal positiva elegida, y el volumen euclídeo es independiente de cualquier base ortonormal de referencia.

**Demostración.** Sea

$$S=A_E(f_1,f_2,f_3).$$

Para la terna

$$V=(v_1,v_2,v_3),$$

las matrices de componentes satisfacen

$$A_E(V) = S\,A_F(V).$$

Por proposición 4.26, $\det_E(V) = \det(S)\det_F(V).$

Como $E$ y $F$ son ortonormales, proposición 4.30 da $\det(S)=\pm1.$ Si tienen la misma orientación, definición 4.27 implica $\det(S)=+1,$

y los volúmenes orientados coinciden. Si tienen orientaciones opuestas, $\det(S)=-1,$

y los volúmenes orientados cambian de signo. En ambos casos, tomar valor absoluto elimina el signo. $\square$ Esta proposición completa la justificación intrínseca de la definición 4.28: podemos escribir sin ambigüedad

$$\operatorname{Vol}(v_1,v_2,v_3)$$

sin indicar una base ortonormal particular.

[]{#ejemplo-guiado-cizalla-escala-y-orientación}

### Ejemplo guiado: cizalla, escala y orientación {#fispm-c04-ejemplo-guiado-cizalla-escala-y-orientaciuxf3n}

Sea $E=(e_1,e_2,e_3)$ una base ortonormal positivamente orientada y definamos

$$v_1=2e_1, \qquad v_2=e_1+3e_2, \qquad v_3=2e_1-e_2+4e_3.$$

La matriz de columnas es

$$A= \begin{pmatrix} 2&1&2\\ 0&3&-1\\ 0&0&4 \end{pmatrix}.$$

Por definición 4.25, $\det A=2\cdot3\cdot4=24.$ Por tanto,

$$\boxed{ \operatorname{Vol}^{\mathrm{or}}_E(v_1,v_2,v_3)=24, }$$

y

$$\boxed{ \operatorname{Vol}(v_1,v_2,v_3)=24. }$$

Los términos $e_1$ añadidos a $v_2$ y $2e_1-e_2$ añadidos a $v_3$ actúan como cizallas: modifican la forma del paralelepípedo, pero no el producto final de los factores independientes $2$, $3$ y $4$. Si intercambiamos $v_1$ y $v_2$,

$$\operatorname{Vol}^{\mathrm{or}}_E(v_2,v_1,v_3) = -24,$$

mientras

$$\operatorname{Vol}(v_2,v_1,v_3) = 24.$$

[]{#fispm-t1-c04-e0016}

**Ejercicio 4.16 --- Determinante, volumen y orientación.**

**Función pedagógica:** `Cálculo → Interpretación geométrica → Separación signo/magnitud`

Sea $E=(e_1,e_2,e_3)$ una base ortonormal positivamente orientada y

$$v_1=2e_1, \qquad v_2=e_1+3e_2, \qquad v_3=2e_1-e_2+4e_3.$$

1.  Calcula $\det_E(v_1,v_2,v_3)$.

2.  Determina el volumen euclídeo del paralelepípedo.

3.  Decide si la terna tiene la misma orientación que $E$.

4.  Repite las preguntas para $(v_2,v_1,v_3)$.

**Solución desarrollada**

La matriz es

$$A= \begin{pmatrix} 2&1&2\\ 0&3&-1\\ 0&0&4 \end{pmatrix}.$$

Por definición 4.25, $\det A=24.$

Luego

$$\boxed{ \operatorname{Vol}^{\mathrm{or}}_E(v_1,v_2,v_3)=24, }$$

y

$$\boxed{ \operatorname{Vol}(v_1,v_2,v_3)=24. }$$

Como el determinante es positivo, la terna tiene la misma orientación que $E$. Al intercambiar los dos primeros vectores, proposición 4.23 da $\det_E(v_2,v_1,v_3)=-24.$ El volumen euclídeo permanece

$$\boxed{24},$$

pero la orientación se invierte.

[]{#fispm-t1-c04-e0017}

**Ejercicio 4.17 --- Qué operaciones cambian volumen y orientación.**

**Función pedagógica:** `Transformaciones elementales → Invariantes → Diagnóstico`

Partimos de una base ortonormal positivamente orientada

$$E=(e_1,e_2,e_3),$$

cuyo volumen orientado vale $1$. Para cada operación, determina el nuevo volumen orientado, el volumen euclídeo y si la orientación se conserva:

1.  sustituir $e_1$ por $3e_1$;

2.  sustituir $e_1$ por $-e_1$;

3.  sustituir $e_1$ por $e_1+5e_2$;

4.  intercambiar $e_1$ y $e_2$.

**Solución desarrollada**

**1. Escala positiva.**

$$\operatorname{Vol}^{\mathrm{or}}_E(3e_1,e_2,e_3)=3.$$

El volumen euclídeo pasa a $3$ y la orientación se conserva.

**2. Escala negativa.**

$$\operatorname{Vol}^{\mathrm{or}}_E(-e_1,e_2,e_3)=-1.$$

El volumen euclídeo sigue siendo $1$, pero la orientación se invierte.

**3. Cizalla.**

Por proposición 4.29, $\operatorname{Vol}^{\mathrm{or}}_E(e_1+5e_2,e_2,e_3)=1.$

No cambia ni el volumen euclídeo ni la orientación.

**4. Intercambio.**

$$\operatorname{Vol}^{\mathrm{or}}_E(e_2,e_1,e_3)=-1.$$

El volumen euclídeo sigue siendo $1$ y la orientación se invierte.

[]{#cierre-de-8}

### Cierre de §8 {#fispm-c04-cierre-de-8}

La sección ha separado tres capas distintas:

$$\boxed{ \text{independencia lineal} \quad\longleftrightarrow\quad \det\ne0, }$$

$$\boxed{ \text{orientación} \quad\longleftrightarrow\quad \operatorname{sgn}(\det), }$$

y, cuando la referencia es ortonormal,

$$\boxed{ \text{volumen euclídeo} \quad\longleftrightarrow\quad |\det|. }$$

El determinante contiene así simultáneamente información algebraica, orientacional y métrica, pero cada lectura requiere sus hipótesis precisas.

**Principio metodológico 4.13 --- Separar cero, signo y magnitud del determinante** Antes de interpretar un determinante, preguntar qué información se está usando:

- `det = 0`: pérdida de independencia;

- `sgn(det)`: clase de orientación;

- `det`: factor de volumen cuando la referencia métrica está normalizada.

La sección termina exactamente donde comienza la siguiente necesidad tridimensional: construir, a partir de dos vectores y una orientación elegida, un tercer vector perpendicular cuya magnitud codifique un área. Esa construcción será el objeto de §9. El siguiente paso será el §[9](#fispm-c04-producto-vectorial-en-dimensiuxf3n-tres).

[]{#producto-vectorial-en-dimensión-tres}

[]{#fispm-t1-c04-s09}

[]{#fpm-i-04-s09}

## 9. Producto vectorial en dimensión tres {#fispm-c04-producto-vectorial-en-dimensiuxf3n-tres}

[]{#activación-de-dos-vectores-a-una-normal-orientada}

### Activación: de dos vectores a una normal orientada {#fispm-c04-activaciuxf3n-de-dos-vectores-a-una-normal-orientada}

Sean

$$u,v\in V.$$

Los dos vectores determinan, cuando son linealmente independientes, un plano vectorial

$$\operatorname{span}(u,v).$$

En dimensión tres aparece una posibilidad especial: podemos buscar un tercer vector que sea perpendicular a ese plano y cuya magnitud mida el área del paralelogramo generado por $u$ y $v$. Pero quedan dos elecciones que una simple condición de perpendicularidad no resuelve:

[]{#fig:I-04-R03}

<figure id="fig-fpm-v04-i-04-r03" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-04-R03.svg" class="lightbox" data-gallery="fpm-v04-c04"><img src="/assets/books/fispm/v04/I-04-R03.svg" alt="El orden fija la orientación. Diagrama del capítulo 4; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="283" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 4.5.** En una base ortonormal positivamente orientada, $e_1\times e_2=e_3$. El punto dentro del círculo indica una dirección que sale del papel; invertir los factores invierte ese vector. Véase §[9](#fispm-c04-producto-vectorial-en-dimensiuxf3n-tres).

</figcaption>

</figure>

1.  hay dos sentidos opuestos en la recta perpendicular al plano;

2.  la magnitud debe fijarse de manera compatible con el área.

La orientación construida en §8 resuelve el primer problema; el producto escalar resuelve el segundo. Por eso el producto vectorial no pertenece a la estructura lineal desnuda de $V$.

[]{#los-dos-ingredientes-que-necesita-la-construcción}

### Los dos ingredientes que necesita la construcción {#fispm-c04-los-dos-ingredientes-que-necesita-la-construcciuxf3n}

Para definir $u\times v$ necesitamos simultáneamente:

- el producto escalar $$\langle\cdot,\cdot\rangle,$$ que permite identificar vectores con funcionales lineales mediante la regla $$x\longmapsto \langle x,\cdot\rangle;$$

- una clase de orientación positiva, que fija el signo del volumen orientado $$\operatorname{Vol}^{\mathrm{or}}(u,v,w).$$

Proposición 4.31 garantiza que, una vez fijada la orientación positiva, este volumen orientado es independiente de la base ortonormal positiva usada para calcularlo. Así, para $u$ y $v$ fijos, la aplicación

$$w \longmapsto \operatorname{Vol}^{\mathrm{or}}(u,v,w)$$

es un funcional lineal sobre $V$, por la proposición 4.24. La pregunta central es:

Existencia y unicidad ¿Existe un único vector $x\in V$ tal que

$$\langle x,w\rangle = \operatorname{Vol}^{\mathrm{or}}(u,v,w)$$

para todo $w\in V$?

[]{#proposición-representación-vectorial-del-volumen-orientado}

### Proposición: representación vectorial del volumen orientado {#fispm-c04-proposiciuxf3n-representaciuxf3n-vectorial-del-volumen-orientado}

**Proposición 4.32 --- Existencia y unicidad del vector representante** Para cada par $u,v\in V$ existe un único vector $x\in V$ tal que

$$\boxed{ \langle x,w\rangle = \operatorname{Vol}^{\mathrm{or}}(u,v,w) }$$

para todo $w\in V$.

**Demostración de existencia.** Elegimos una base ortonormal positivamente orientada

$$E=(e_1,e_2,e_3).$$

Definimos

$$x := \sum_{k=1}^{3} \operatorname{Vol}^{\mathrm{or}}(u,v,e_k)e_k.$$

Sea ahora

$$w = \sum_{k=1}^{3} w^ke_k.$$

Por proposición 4.20, $w^k=\langle w,e_k\rangle.$

Como $E$ es ortonormal,

$$\begin{aligned} \langle x,w\rangle &= \left\langle \sum_{k=1}^{3} \operatorname{Vol}^{\mathrm{or}}(u,v,e_k)e_k, \sum_{j=1}^{3}w^je_j \right\rangle\\ &= \sum_{k=1}^{3} \operatorname{Vol}^{\mathrm{or}}(u,v,e_k)w^k. \end{aligned}$$

Por linealidad del volumen orientado en el tercer argumento,

$$\begin{aligned} \operatorname{Vol}^{\mathrm{or}}(u,v,w) &= \operatorname{Vol}^{\mathrm{or}} \left( u,v, \sum_{k=1}^{3}w^ke_k \right)\\ &= \sum_{k=1}^{3} w^k \operatorname{Vol}^{\mathrm{or}}(u,v,e_k). \end{aligned}$$

Por tanto,

$$\langle x,w\rangle = \operatorname{Vol}^{\mathrm{or}}(u,v,w).$$

**Demostración de unicidad.** Supongamos que $x$ e $y$ satisfacen la misma condición. Entonces, para todo $w\in V$,

$$\langle x-y,w\rangle=0.$$

Tomamos $w=x-y.$

Así, $\|x-y\|^2 = \langle x-y,x-y\rangle = 0.$ Por positividad definida, $x-y=0,$

y por tanto

$$x=y.$$

$\square$

La construcción utilizó una base ortonormal positiva para demostrar existencia, pero el vector obtenido no depende de esa base: la condición que lo caracteriza es intrínseca y proposición 4.32 asegura unicidad.

[]{#definir-producto-vectorial}

### Definir: producto vectorial {#fispm-c04-definir-producto-vectorial}

**Definición 4.29 --- Producto vectorial en un espacio euclídeo orientado de dimensión tres** Para $u,v\in V$, definimos su **producto vectorial**

$$\boxed{ u\times v }$$

como el único vector cuya existencia y unicidad garantiza proposición 4.32, caracterizado por

$$\boxed{ \langle u\times v,w\rangle = \operatorname{Vol}^{\mathrm{or}}(u,v,w) }$$

para todo $w\in V$. Esta identidad es la definición geométrica fundamental del producto vectorial en este capítulo. No depende de haber elegido una base concreta para escribir componentes.

Tipo físico y unidades definición 4.29 define una operación en el espacio euclídeo abstracto una vez fijadas métrica y orientación. Si, en una realización física, $u$ y $v$ representan desplazamientos con dimensión $L$, entonces proposición 4.37 implica $\|u\times v\|\sim L^2.$ Por tanto, $u\times v$ debe interpretarse dimensionalmente como un **vector de área orientada**, no como otro desplazamiento. Una forma segura de llevar las unidades es escribir $u=\ell_0\bar u$ y $v=\ell_0\bar v$, con $\bar u,\bar v$ en el espacio direccional normalizado; entonces el vector de área físico es $\ell_0^2(\bar u\times\bar v).$

Reutilizar $V$ para codificar su dirección no autoriza a sumar $u\times v$ con un desplazamiento ni a interpretar automáticamente sus componentes en metros. El tipo de magnitud y la escala deben conservarse explícitos.

[]{#primeras-consecuencias-sin-coordenadas}

### Primeras consecuencias sin coordenadas {#fispm-c04-primeras-consecuencias-sin-coordenadas}

Tomemos

$$w=u.$$

Entonces

$$\langle u\times v,u\rangle = \operatorname{Vol}^{\mathrm{or}}(u,v,u).$$

Como el volumen orientado es alternante, $\operatorname{Vol}^{\mathrm{or}}(u,v,u)=0.$ Por tanto,

$$\boxed{ u\times v\perp u. }$$

Análogamente,

$$\boxed{ u\times v\perp v. }$$

Así, el vector definido por la definición 4.29 es perpendicular a los dos factores sin que hayamos impuesto esta condición por separado: surge automáticamente de la alternancia del determinante. También, $\operatorname{Vol}^{\mathrm{or}}(u,u,w)=0$

para todo $w$, luego proposición 4.32 implica

$$\boxed{ u\times u=0. }$$

[]{#qué-ocurre-si-invertimos-la-orientación}

### Qué ocurre si invertimos la orientación {#fispm-c04-quuxe9-ocurre-si-invertimos-la-orientaciuxf3n}

Supongamos que conservamos el mismo producto escalar pero declaramos positiva la orientación opuesta. Entonces el volumen orientado cambia de signo:

$$\operatorname{Vol}^{\mathrm{or}}_{\mathrm{opp}}(u,v,w) = - \operatorname{Vol}^{\mathrm{or}}(u,v,w).$$

Sea $\times_{\mathrm{opp}}$ el producto vectorial definido con esa orientación opuesta. Por definición 4.29,

$$\langle u\times_{\mathrm{opp}}v,w\rangle = - \operatorname{Vol}^{\mathrm{or}}(u,v,w).$$

Pero

$$\left\langle -(u\times v),w \right\rangle = - \operatorname{Vol}^{\mathrm{or}}(u,v,w).$$

Por unicidad en la proposición 4.32,

$$\boxed{ u\times_{\mathrm{opp}}v = -(u\times v). }$$

La orientación no es, por tanto, una decoración terminológica: determina el **signo** del producto vectorial.

[]{#principio-metodológico-y-consecuencias-pendientes}

### Principio metodológico y consecuencias pendientes {#fispm-c04-principio-metodoluxf3gico-y-consecuencias-pendientes}

**Principio metodológico 4.14 --- Declarar métrica y orientación antes de usar el producto vectorial** El producto vectorial tridimensional requiere simultáneamente:

- un producto escalar, para identificar el funcional de volumen con un vector;

- una orientación, para fijar el signo del volumen orientado.

No tratar $u\times v$ como una operación disponible en un espacio vectorial real arbitrario. La definición intrínseca

$$\boxed{ \langle u\times v,w\rangle = \operatorname{Vol}^{\mathrm{or}}(u,v,w) }$$

contiene ya la geometría esencial de la operación. Todavía falta traducir esta caracterización a una base ortonormal positiva y obtener:

- la fórmula usual por componentes;

- antisimetría y bilinealidad;

- el criterio $u\times v=0$;

- la magnitud $$\|u\times v\|$$ en términos del ángulo entre $u$ y $v$.

[]{#proposición-fórmula-en-una-base-ortonormal-positiva}

### Proposición: fórmula en una base ortonormal positiva {#fispm-c04-proposiciuxf3n-fuxf3rmula-en-una-base-ortonormal-positiva}

**Proposición 4.33 --- Fórmula coordenada del producto vectorial** Sea

$$E=(e_1,e_2,e_3)$$

una base ortonormal positivamente orientada. Si

$$u=u^1e_1+u^2e_2+u^3e_3$$

y

$$v=v^1e_1+v^2e_2+v^3e_3,$$

entonces

$$\boxed{ \begin{aligned} u\times v &= (u^2v^3-u^3v^2)e_1\\ &\quad+ (u^3v^1-u^1v^3)e_2\\ &\quad+ (u^1v^2-u^2v^1)e_3. \end{aligned} }$$

**Demostración.** Como $E$ es ortonormal, proposición 4.20 permite recuperar las componentes de $u\times v$ mediante productos escalares:

$$(u\times v)^k = \langle u\times v,e_k\rangle.$$

Por definición 4.29,

$$(u\times v)^k = \operatorname{Vol}^{\mathrm{or}}(u,v,e_k) = \det_E(u,v,e_k).$$

Para $k=1$,

$$\det \begin{pmatrix} u^1&v^1&1\\ u^2&v^2&0\\ u^3&v^3&0 \end{pmatrix} = u^2v^3-u^3v^2.$$

Para $k=2$,

$$\det \begin{pmatrix} u^1&v^1&0\\ u^2&v^2&1\\ u^3&v^3&0 \end{pmatrix} = u^3v^1-u^1v^3.$$

Y para $k=3$,

$$\det \begin{pmatrix} u^1&v^1&0\\ u^2&v^2&0\\ u^3&v^3&1 \end{pmatrix} = u^1v^2-u^2v^1.$$

Reuniendo las tres componentes obtenemos la fórmula. $\square$ La expresión usual por componentes no es, por tanto, el punto de partida conceptual: es la representación de la definición 4.29 en una base ortonormal positiva.[^3]

[]{#tabla-de-la-base-ortonormal-positiva}

### Tabla de la base ortonormal positiva {#fispm-c04-tabla-de-la-base-ortonormal-positiva}

Aplicando proposición 4.33 a los vectores de la propia base,

$$\boxed{ e_1\times e_2=e_3, }$$

$$\boxed{ e_2\times e_3=e_1, }$$

$$\boxed{ e_3\times e_1=e_2. }$$

Al invertir el orden,

$$e_2\times e_1=-e_3,$$

$$e_3\times e_2=-e_1,$$

$$e_1\times e_3=-e_2.$$

Esta tabla incorpora simultáneamente ortonormalidad y orientación. En una base ortonormal de orientación opuesta, los signos se invierten.

[]{#proposición-bilinealidad-y-antisimetría}

### Proposición: bilinealidad y antisimetría {#fispm-c04-proposiciuxf3n-bilinealidad-y-antisimetruxeda}

**Proposición 4.34 --- Bilinealidad y antisimetría del producto vectorial** Para $u,v,w\in V$ y $\alpha,\beta\in\mathbb R$:

$$\boxed{ (\alpha u+\beta v)\times w = \alpha(u\times w) + \beta(v\times w), }$$

$$\boxed{ u\times(\alpha v+\beta w) = \alpha(u\times v) + \beta(u\times w), }$$

y

$$\boxed{ v\times u = -(u\times v). }$$

**Demostración de la linealidad en la primera entrada.** Para todo $z\in V$,

$$\begin{aligned} \left\langle (\alpha u+\beta v)\times w,z \right\rangle &= \operatorname{Vol}^{\mathrm{or}}(\alpha u+\beta v,w,z)\\ &= \alpha\operatorname{Vol}^{\mathrm{or}}(u,w,z) + \beta\operatorname{Vol}^{\mathrm{or}}(v,w,z)\\ &= \left\langle \alpha(u\times w)+\beta(v\times w), z \right\rangle. \end{aligned}$$

Como esto vale para todo $z$, la unicidad de la proposición 4.32 implica la primera identidad. La linealidad en la segunda entrada se demuestra del mismo modo usando la trilinealidad del volumen orientado. Para la antisimetría,

$$\begin{aligned} \langle v\times u,z\rangle &= \operatorname{Vol}^{\mathrm{or}}(v,u,z)\\ &= -\operatorname{Vol}^{\mathrm{or}}(u,v,z)\\ &= \langle -(u\times v),z\rangle. \end{aligned}$$

Otra vez proposición 4.32 da $v\times u=-(u\times v).$

$\square$

La antisimetría contiene como caso particular

$$u\times u=0,$$

que ya habíamos obtenido directamente en §9.5.

[]{#consecuencias-algebraicas-inmediatas}

### Consecuencias algebraicas inmediatas {#fispm-c04-consecuencias-algebraicas-inmediatas}

De proposición 4.34 se sigue

$$u\times0=0,$$

$$0\times v=0,$$

y, para todo $\lambda\in\mathbb R$,

$$(\lambda u)\times v = \lambda(u\times v) = u\times(\lambda v).$$

Además, $(u+v)\times w = u\times w+v\times w,$

y

$$u\times(v+w) = u\times v+u\times w.$$

Estas identidades son algebraicas; no requieren elegir coordenadas una vez que definición 4.29 está establecido.

[]{#proposición-cuándo-se-anula-el-producto-vectorial}

### Proposición: cuándo se anula el producto vectorial {#fispm-c04-proposiciuxf3n-cuuxe1ndo-se-anula-el-producto-vectorial}

**Proposición 4.35 --- Criterio de dependencia mediante el producto vectorial** Para $u,v\in V$,

$$\boxed{ u\times v=0 \Longleftrightarrow u,v \text{ son linealmente dependientes}. }$$

**Demostración.** Si $u$ y $v$ son dependientes, entonces existe una relación lineal entre ellos. En particular, si $v=\lambda u$,

$$u\times v = u\times(\lambda u) = \lambda(u\times u) = 0.$$

Los casos en que uno de los vectores es cero quedan incluidos. Recíprocamente, supongamos $u\times v=0.$ Elegimos una base ortonormal positivamente orientada

$$E=(e_1,e_2,e_3).$$

Por proposición 4.33, las tres componentes de $u\times v$ se anulan, de modo que

$$u^2v^3-u^3v^2=0,$$

$$u^3v^1-u^1v^3=0,$$

y

$$u^1v^2-u^2v^1=0.$$

Si $u=0$, la dependencia es inmediata. Supongamos entonces $u\ne0$. Alguna componente de $u$ es no nula. Si, por ejemplo, $u^1\ne0,$

las dos últimas ecuaciones dan

$$v^2=\frac{u^2}{u^1}v^1, \qquad v^3=\frac{u^3}{u^1}v^1.$$

Por tanto, $[v]_E = \frac{v^1}{u^1}[u]_E,$

y, por la biyección de componentes de la proposición 4.7, $v=\frac{v^1}{u^1}u.$

Así $u$ y $v$ son linealmente dependientes. Si la componente no nula de $u$ es $u^2$ o $u^3$, el mismo argumento se obtiene permutando cíclicamente los índices. $\square$ Así, el producto vectorial detecta exactamente cuándo dos vectores generan un plano genuino.

[]{#advertencia-la-fórmula-coordenada-tiene-hipótesis}

### Advertencia: la fórmula coordenada tiene hipótesis {#fispm-c04-advertencia-la-fuxf3rmula-coordenada-tiene-hipuxf3tesis}

**Principio metodológico 4.15 --- No transportar la fórmula de componentes fuera de una base ortonormal positiva** La expresión

$$\begin{pmatrix} u^2v^3-u^3v^2\\ u^3v^1-u^1v^3\\ u^1v^2-u^2v^1 \end{pmatrix}$$

representa las componentes de $u\times v$ sólo cuando las componentes de $u$ y $v$ están tomadas en una base ortonormal compatible con la orientación positiva elegida. En una base general, esa receta numérica no puede trasladarse sin incorporar correctamente la métrica y la orientación.

Este punto es paralelo a la advertencia de §5 sobre la fórmula pitagórica por componentes: una expresión simple suele esconder hipótesis geométricas fuertes.

[]{#balance-forma-intrínseca-y-forma-coordenada}

### Balance: forma intrínseca y forma coordenada {#fispm-c04-balance-forma-intruxednseca-y-forma-coordenada}

Ya tenemos dos descripciones complementarias: **Descripción intrínseca**

$$\boxed{ \langle u\times v,w\rangle = \operatorname{Vol}^{\mathrm{or}}(u,v,w), }$$

y **descripción coordenada en una base ortonormal positiva**

$$\boxed{ [u\times v]_E = \begin{pmatrix} u^2v^3-u^3v^2\\ u^3v^1-u^1v^3\\ u^1v^2-u^2v^1 \end{pmatrix}. }$$

Además,

$$\boxed{ v\times u=-(u\times v) }$$

y

$$\boxed{ u\times v=0 \Longleftrightarrow u,v \text{ dependientes}. }$$

Todavía falta conectar la **magnitud** de $u\times v$ con el área del paralelogramo y con el ángulo entre $u$ y $v$.

[]{#fispm-c04-proposiciuxf3n-identidad-de-lagrange label="fispm-c04-proposiciuxf3n-identidad-de-lagrange"}

**Proposición 4.36 --- Identidad de Lagrange** Para todo $u,v\in V$,

$$\boxed{ \|u\times v\|^2 = \|u\|^2\|v\|^2 - \langle u,v\rangle^2. }$$

**Demostración.** Elegimos una base ortonormal positivamente orientada

$$E=(e_1,e_2,e_3),$$

y escribimos

$$[u]_E= \begin{pmatrix} u^1\\ u^2\\ u^3 \end{pmatrix}, \qquad [v]_E= \begin{pmatrix} v^1\\ v^2\\ v^3 \end{pmatrix}.$$

Por proposición 4.33,

$$[u\times v]_E = \begin{pmatrix} u^2v^3-u^3v^2\\ u^3v^1-u^1v^3\\ u^1v^2-u^2v^1 \end{pmatrix}.$$

Como $E$ es ortonormal,

$$\begin{aligned} \|u\times v\|^2 &= (u^2v^3-u^3v^2)^2\\ &\quad+ (u^3v^1-u^1v^3)^2\\ &\quad+ (u^1v^2-u^2v^1)^2. \end{aligned}$$

Al expandir y reagrupar,

$$\begin{aligned} \|u\times v\|^2 &= \bigl((u^1)^2+(u^2)^2+(u^3)^2\bigr) \bigl((v^1)^2+(v^2)^2+(v^3)^2\bigr)\\ &\quad- \bigl(u^1v^1+u^2v^2+u^3v^3\bigr)^2. \end{aligned}$$

Por proposición 4.20, los dos factores son $\|u\|^2$ y $\|v\|^2$, mientras el último paréntesis es $\langle u,v\rangle$. Por tanto,

$$\|u\times v\|^2 = \|u\|^2\|v\|^2 - \langle u,v\rangle^2.$$

$\square$

La identidad es intrínseca aunque se haya demostrado en una base ortonormal positiva: ambos lados están definidos geométricamente y no dependen de la base elegida.

[]{#proposición-magnitud-y-ángulo}

### Proposición: magnitud y ángulo {#fispm-c04-proposiciuxf3n-magnitud-y-uxe1ngulo}

**Proposición 4.37 --- Magnitud del producto vectorial** Sean $u,v\ne0$ y sea

$$\theta=\theta(u,v)\in[0,\pi].$$

Entonces

$$\boxed{ \|u\times v\| = \|u\|\,\|v\|\sin\theta. }$$

**Demostración.** Por definición 4.21,

$$\langle u,v\rangle = \|u\|\,\|v\|\cos\theta.$$

Sustituyendo en la proposición 4.36,

$$\begin{aligned} \|u\times v\|^2 &= \|u\|^2\|v\|^2 - \|u\|^2\|v\|^2\cos^2\theta\\ &= \|u\|^2\|v\|^2 \bigl(1-\cos^2\theta\bigr)\\ &= \|u\|^2\|v\|^2\sin^2\theta. \end{aligned}$$

Como $\theta\in[0,\pi]$, $\sin\theta\ge0.$

Tomando raíces no negativas, $\|u\times v\| = \|u\|\,\|v\|\sin\theta.$

$\square$

Los casos extremos son coherentes con la proposición 4.35:

- si $\theta=0$ o $\pi$, entonces $\sin\theta=0$ y $u\times v=0$;

- si $\theta=\pi/2$, entonces $$\|u\times v\| = \|u\|\,\|v\|.$$

[]{#interpretación-como-área}

### Interpretación como área {#fispm-c04-interpretaciuxf3n-como-uxe1rea}

El paralelogramo generado por $u$ y $v$ tiene base de longitud $\|u\|$ y altura perpendicular

$$\|v\|\sin\theta.$$

Por tanto su área euclídea es $\|u\|\,\|v\|\sin\theta.$

Proposición 4.37 permite escribir

$$\boxed{ \operatorname{Area}(u,v) = \|u\times v\|. }$$

Así, el producto vectorial reúne dos informaciones diferentes:

- su **dirección** es perpendicular al plano generado por $u$ y $v$;

- su **magnitud** es el área del paralelogramo generado por ellos.

El signo orientacional no aparece en la norma. Está contenido en el sentido del vector normal.

[]{#proposición-la-normal-elegida-es-positivamente-orientada}

### Proposición: la normal elegida es positivamente orientada {#fispm-c04-proposiciuxf3n-la-normal-elegida-es-positivamente-orientada}

**Proposición 4.38 --- Orientación de la terna $(u,v,u\times v)$** Si $u$ y $v$ son linealmente independientes, entonces

$$\boxed{ \operatorname{Vol}^{\mathrm{or}} (u,v,u\times v) = \|u\times v\|^2 >0. }$$

En particular,

$$\boxed{ (u,v,u\times v) }$$

tiene orientación positiva.

**Demostración.** Por definición 4.29,

$$\operatorname{Vol}^{\mathrm{or}} (u,v,u\times v) = \langle u\times v,u\times v\rangle.$$

Luego

$$\operatorname{Vol}^{\mathrm{or}} (u,v,u\times v) = \|u\times v\|^2.$$

Como $u$ y $v$ son independientes, proposición 4.35 da $u\times v\ne0.$ Por positividad definida, $\|u\times v\|^2>0.$

$\square$

Esta proposición expresa de manera intrínseca la regla de orientación que suele memorizarse mediante la "regla de la mano derecha".

[]{#fispm-t1-c04-e0018}

**Ejercicio 4.18 --- Cálculo, perpendicularidad y área.**

**Función pedagógica:** `Coordenadas → Verificación geométrica → Área`

En una base ortonormal positivamente orientada

$$E=(e_1,e_2,e_3),$$

sean

$$u=2e_1+e_2, \qquad v=e_1+3e_2+2e_3.$$

1.  Calcula $u\times v$.

2.  Comprueba que es perpendicular a $u$ y a $v$.

3.  Calcula el área del paralelogramo generado por $u$ y $v$.

4.  Verifica proposición 4.36 directamente.

**Solución desarrollada**

Las columnas son

$$[u]_E= \begin{pmatrix} 2\\ 1\\ 0 \end{pmatrix}, \qquad [v]_E= \begin{pmatrix} 1\\ 3\\ 2 \end{pmatrix}.$$

Por proposición 4.33,

$$[u\times v]_E = \begin{pmatrix} 2\\ -4\\ 5 \end{pmatrix},$$

es decir,

$$\boxed{ u\times v = 2e_1-4e_2+5e_3. }$$

Verificamos:

$$\langle u\times v,u\rangle = 2\cdot2+(-4)\cdot1+5\cdot0 = 0,$$

y

$$\langle u\times v,v\rangle = 2\cdot1+(-4)\cdot3+5\cdot2 = 0.$$

Su norma al cuadrado es $\|u\times v\|^2 = 2^2+(-4)^2+5^2 = 45.$ Por tanto,

$$\boxed{ \operatorname{Area}(u,v) = 3\sqrt5. }$$

Finalmente,

$$\|u\|^2=5, \qquad \|v\|^2=14, \qquad \langle u,v\rangle=5.$$

Entonces

$$\|u\|^2\|v\|^2 - \langle u,v\rangle^2 = 5\cdot14-25 = 45,$$

coincidiendo con $\|u\times v\|^2$.

[]{#fispm-t1-c04-e0019}

**Ejercicio 4.19 --- Dependencia de la orientación.**

**Función pedagógica:** `Estructura → Orientación → Signo`

Sea

$$E=(e_1,e_2,e_3)$$

una base ortonormal positiva y sean

$$u=e_1+e_2, \qquad v=e_2+e_3.$$

1.  Calcula $u\times v$ con la orientación positiva determinada por $E$.

2.  Invierte la orientación del espacio sin cambiar el producto escalar. ¿Cuál es el nuevo producto vectorial?

3.  Compara las normas y explica qué parte del resultado depende de la orientación.

**Solución desarrollada**

Por proposición 4.33,

$$[u]_E= \begin{pmatrix} 1\\ 1\\ 0 \end{pmatrix}, \qquad [v]_E= \begin{pmatrix} 0\\ 1\\ 1 \end{pmatrix},$$

y

$$[u\times v]_E = \begin{pmatrix} 1\\ -1\\ 1 \end{pmatrix}.$$

Por tanto,

$$\boxed{ u\times v = e_1-e_2+e_3. }$$

Si invertimos la orientación y mantenemos la misma métrica, §9.6 da

$$\boxed{ u\times_{\mathrm{opp}}v = -e_1+e_2-e_3. }$$

En ambos casos,

$$\|u\times v\| = \|u\times_{\mathrm{opp}}v\| = \sqrt3.$$

La magnitud ---y por tanto el área--- depende de la métrica, pero no de cuál clase de orientación declaramos positiva. Lo que cambia con la orientación es el **sentido** de la normal.

[]{#cierre-de-9}

### Cierre de §9 {#fispm-c04-cierre-de-9}

El producto vectorial ha quedado construido a partir de dos estructuras previas:

$$\boxed{ \text{producto escalar} + \text{orientación} \Longrightarrow \text{producto vectorial}. }$$

Su definición intrínseca es

$$\boxed{ \langle u\times v,w\rangle = \operatorname{Vol}^{\mathrm{or}}(u,v,w), }$$

mientras que, en una base ortonormal positiva,

$$\boxed{ [u\times v]_E = \begin{pmatrix} u^2v^3-u^3v^2\\ u^3v^1-u^1v^3\\ u^1v^2-u^2v^1 \end{pmatrix}. }$$

Las propiedades fundamentales quedan resumidas por

$$\boxed{ u\times v\perp u, \qquad u\times v\perp v, }$$

$$\boxed{ v\times u=-(u\times v), }$$

$$\boxed{ u\times v=0 \Longleftrightarrow u,v \text{ dependientes}, }$$

y

$$\boxed{ \|u\times v\| = \|u\|\,\|v\|\sin\theta. }$$

Finalmente,

$$\boxed{ \operatorname{Vol}^{\mathrm{or}} (u,v,u\times v) = \|u\times v\|^2>0 }$$

cuando $u$ y $v$ son independientes. La orientación determina el sentido de la normal; la métrica determina su magnitud. La siguiente sección cambiará de foco: no introducirá una nueva operación geométrica, sino que estudiará cómo una misma entidad vectorial adquiere distintas columnas cuando cambiamos de base. El siguiente paso será el §[10](#fispm-c04-cambios-de-base-y-coordenadas-vectoriales).

[]{#cambios-de-base-y-coordenadas-vectoriales}

[]{#fispm-t1-c04-s10}

[]{#fpm-i-04-s10}

## 10. Cambios de base y coordenadas vectoriales {#fispm-c04-cambios-de-base-y-coordenadas-vectoriales}

[]{#activación-el-vector-no-cambia-porque-cambie-su-columna}

### Activación: el vector no cambia porque cambie su columna {#fispm-c04-activaciuxf3n-el-vector-no-cambia-porque-cambie-su-columna}

Sea

$$v\in V.$$

Elegimos dos bases ordenadas: $B=(e_1,e_2,e_3), \qquad B'=(e'_1,e'_2,e'_3).$ El mismo vector posee dos columnas: $[v]_B \qquad\text{y}\qquad [v]_{B'}.$

Estas columnas pueden ser numéricamente distintas sin que haya ocurrido ninguna transformación física o geométrica del vector. La situación es **pasiva**:

$$\boxed{ v\ \text{permanece fijo}; \qquad \text{cambia la base usada para describirlo}. }$$

El objetivo inicial de esta sección es determinar rigurosamente cómo se relacionan ambas columnas.

[]{#definir-matriz-de-la-nueva-base-expresada-en-la-antigua}

### Definir: matriz de la nueva base expresada en la antigua {#fispm-c04-definir-matriz-de-la-nueva-base-expresada-en-la-antigua}

**Definición 4.30 --- Matriz de cambio de base** Sean

$$B=(e_1,e_2,e_3), \qquad B'=(e'_1,e'_2,e'_3).$$

Definimos

$$\boxed{ S_{B\leftarrow B'} := \begin{pmatrix} \vert&\vert&\vert\\ {}[e'_1]_B&[e'_2]_B&[e'_3]_B\\ \vert&\vert&\vert \end{pmatrix}. }$$

Sus columnas son, por tanto, los vectores de la **base nueva** $B'$ expresados en la **base antigua** $B$. Cuando no haya ambigüedad escribiremos simplemente

[]{#fig:I-04-N03}

<figure id="fig-fpm-v04-i-04-n03" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-04-N03.svg" class="lightbox" data-gallery="fpm-v04-c04"><img src="/assets/books/fispm/v04/I-04-N03.svg" alt="Dos bases en el mismo plano. Diagrama del capítulo 4; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="344" height="264" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 4.6.** La base prima se gira un ángulo $\theta$ positivo. Las coordenadas de un mismo vector se transforman por la rotación inversa; el vector geométrico permanece fijo. Véase §[10](#fispm-c04-cambios-de-base-y-coordenadas-vectoriales).

</figcaption>

</figure>

$$S:=S_{B\leftarrow B'}.$$

La flecha recuerda el sentido de reconstrucción:

$$\boxed{ \text{columnas en }B' \ \xrightarrow{\ S\ }\ \text{columnas en }B. }$$

[]{#proposición-ley-pasiva-de-transformación-de-coordenadas}

### Proposición: ley pasiva de transformación de coordenadas {#fispm-c04-proposiciuxf3n-ley-pasiva-de-transformaciuxf3n-de-coordenadas}

**Proposición 4.39 --- Cambio de componentes entre dos bases** Para todo $v\in V$,

$$\boxed{ [v]_B = S_{B\leftarrow B'}[v]_{B'}. }$$

Como $B'$ es una base, $S_{B\leftarrow B'}$ es invertible y, por tanto,

$$\boxed{ [v]_{B'} = S_{B\leftarrow B'}^{-1}[v]_B. }$$

**Demostración.** Escribimos

$$[v]_{B'} = \begin{pmatrix} v'^1\\ v'^2\\ v'^3 \end{pmatrix}.$$

Por definición de componentes, $v = v'^1e'_1+v'^2e'_2+v'^3e'_3.$

Tomando componentes respecto de $B$ y usando la linealidad de la aplicación de componentes proposición 4.7,

$$[v]_B = v'^1[e'_1]_B + v'^2[e'_2]_B + v'^3[e'_3]_B.$$

Pero el lado derecho es precisamente el producto matricial

$$S_{B\leftarrow B'} \begin{pmatrix} v'^1\\ v'^2\\ v'^3 \end{pmatrix}.$$

Así, $[v]_B = S_{B\leftarrow B'}[v]_{B'}.$ Las columnas de $S_{B\leftarrow B'}$ son las componentes en $B$ de los vectores de la base $B'$. Como $B'$ es linealmente independiente y proposición 4.7 es biyectiva, esas columnas son linealmente independientes. Por proposición 4.27, $\det S_{B\leftarrow B'}\ne0.$

La matriz es, por tanto, invertible, y multiplicar la identidad anterior por su inversa produce $[v]_{B'} = S_{B\leftarrow B'}^{-1}[v]_B.$

$\square$

La aparición de la inversa no es una convención arbitraria: procede del hecho de que las columnas de $S$ describen la base nueva en la antigua.[^4]

[]{#cambio-pasivo-frente-a-transformación-activa}

### Cambio pasivo frente a transformación activa {#fispm-c04-cambio-pasivo-frente-a-transformaciuxf3n-activa}

En un **cambio pasivo de base**:

- el vector geométrico $v$ es el mismo;

- cambia la base de descripción;

- la columna cambia según $$[v]_{B'} = S^{-1}[v]_B.$$

Una situación distinta es aplicar una transformación lineal

$$T:V\longrightarrow V$$

manteniendo fija la base $B$. Entonces el vector generalmente cambia: $v \longmapsto T(v).$ Si $A_B(T)$ es la matriz cuyas columnas son

$$[T(e_1)]_B, \qquad [T(e_2)]_B, \qquad [T(e_3)]_B,$$

la linealidad da

$$\boxed{ [T(v)]_B = A_B(T)[v]_B. }$$

Aquí la matriz multiplica la columna porque estamos describiendo **otro vector en la misma base**. Estas dos operaciones no deben confundirse:

$$\boxed{ \begin{array}{c} \text{pasivo: }v\text{ fijo},\ B\to B', \\ {}[v]_{B'}=S^{-1}[v]_B, \end{array} }$$

mientras

$$\boxed{ \begin{array}{c} \text{activo: }B\text{ fija},\ v\to T(v), \\ {}[T(v)]_B=A_B(T)[v]_B. \end{array} }$$

[]{#la-misma-matriz-puede-aparecer-en-dos-problemas-diferentes}

### La misma matriz puede aparecer en dos problemas diferentes {#fispm-c04-la-misma-matriz-puede-aparecer-en-dos-problemas-diferentes}

Supongamos que definimos una transformación lineal $T_S$ mediante $T_S(e_j)=e'_j.$ Por definición 4.30, la matriz de esta transformación activa en la base $B$ es precisamente

$$A_B(T_S)=S_{B\leftarrow B'}.$$

Por tanto, $[T_S(v)]_B = S[v]_B.$ Pero el cambio **pasivo** desde $B$ hacia $B'$ obedece $[v]_{B'} = S^{-1}[v]_B.$

De modo que la misma matriz geométrica de columnas puede aparecer en dos expresiones opuestas:

$$\boxed{ \text{activo: }S, \qquad \text{pasivo: }S^{-1}. }$$

La diferencia no es algebraica sino conceptual: en un caso cambia el vector; en el otro cambia su descripción.

[]{#ejemplo-diagnóstico}

### Ejemplo diagnóstico {#fispm-c04-ejemplo-diagnuxf3stico}

Sea

$$B=(e_1,e_2,e_3)$$

y definamos

$$B' = (e_1+e_2,\ e_2,\ e_3).$$

Entonces

$$S_{B\leftarrow B'} = \begin{pmatrix} 1&0&0\\ 1&1&0\\ 0&0&1 \end{pmatrix},$$

y

$$S_{B\leftarrow B'}^{-1} = \begin{pmatrix} 1&0&0\\ -1&1&0\\ 0&0&1 \end{pmatrix}.$$

Consideremos el vector

$$v=2e_1+3e_2+e_3.$$

En la base $B$,

$$[v]_B = \begin{pmatrix} 2\\ 3\\ 1 \end{pmatrix}.$$

[]{#lectura-pasiva}

#### Lectura pasiva {#fispm-c04-lectura-pasiva}

El vector no cambia. Sólo buscamos su columna en $B'$:

$$[v]_{B'} = S^{-1}[v]_B = \begin{pmatrix} 1&0&0\\ -1&1&0\\ 0&0&1 \end{pmatrix} \begin{pmatrix} 2\\ 3\\ 1 \end{pmatrix} = \begin{pmatrix} 2\\ 1\\ 1 \end{pmatrix}.$$

En efecto, $2(e_1+e_2)+e_2+e_3 = 2e_1+3e_2+e_3 = v.$

[]{#lectura-activa}

#### Lectura activa {#fispm-c04-lectura-activa}

Definamos ahora $T_S$ por

$$T_S(e_1)=e_1+e_2, \qquad T_S(e_2)=e_2, \qquad T_S(e_3)=e_3.$$

La base $B$ permanece fija, pero el vector cambia:

$$[T_S(v)]_B = S[v]_B = \begin{pmatrix} 1&0&0\\ 1&1&0\\ 0&0&1 \end{pmatrix} \begin{pmatrix} 2\\ 3\\ 1 \end{pmatrix} = \begin{pmatrix} 2\\ 5\\ 1 \end{pmatrix}.$$

Así, $T_S(v) = 2e_1+5e_2+e_3,$

que no es el vector original. Este ejemplo hace visible la diferencia:

$$\boxed{ \begin{aligned} \text{pasivo:}&\quad v\text{ igual},\quad (2,3,1)\to(2,1,1), \\ \text{activo:}&\quad v\text{ cambia},\quad (2,3,1)\to(2,5,1). \end{aligned} }$$

[]{#principio-metodológico-y-convención-de-cambio}

### Principio metodológico y convención de cambio {#fispm-c04-principio-metodoluxf3gico-y-convenciuxf3n-de-cambio}

**Principio metodológico 4.16 --- Preguntar qué está cambiando antes de multiplicar por una matriz** Antes de escribir una fórmula matricial, distinguir explícitamente:

1.  **cambio pasivo de base:** el vector permanece fijo y cambia su columna;

2.  **transformación activa:** la base permanece fija y cambia el vector.

Una misma matriz puede intervenir en ambos problemas, pero las leyes de transformación no son la misma afirmación.

Queda fijada la convención canónica:

$$\boxed{ S_{B\leftarrow B'} = \begin{pmatrix} \vert&\vert&\vert\\ {}[e'_1]_B&[e'_2]_B&[e'_3]_B\\ \vert&\vert&\vert \end{pmatrix}, }$$

$$\boxed{ [v]_B=S_{B\leftarrow B'}[v]_{B'}, }$$

y

$$\boxed{ [v]_{B'} = S_{B\leftarrow B'}^{-1}[v]_B. }$$

Todavía falta estudiar la composición de varios cambios de base, la matriz inversa como cambio en sentido opuesto y la transformación de objetos matriciales asociados.

[]{#la-matriz-identidad-como-cambio-trivial}

### La matriz identidad como cambio trivial {#fispm-c04-la-matriz-identidad-como-cambio-trivial}

Si usamos la misma base como origen y destino, $B=(e_1,e_2,e_3),$

entonces definición 4.30 produce

$$S_{B\leftarrow B} = \begin{pmatrix} \vert&\vert&\vert\\ {}[e_1]_B&[e_2]_B&[e_3]_B\\ \vert&\vert&\vert \end{pmatrix}.$$

Pero

$$[e_1]_B= \begin{pmatrix} 1\\ 0\\ 0 \end{pmatrix}, \qquad [e_2]_B= \begin{pmatrix} 0\\ 1\\ 0 \end{pmatrix}, \qquad [e_3]_B= \begin{pmatrix} 0\\ 0\\ 1 \end{pmatrix}.$$

Por tanto,

$$\boxed{ S_{B\leftarrow B}=I_3. }$$

Un cambio de descripción que no cambia la base debe dejar las columnas intactas.

[]{#proposición-el-cambio-inverso}

### Proposición: el cambio inverso {#fispm-c04-proposiciuxf3n-el-cambio-inverso}

**Proposición 4.40 --- La matriz inversa cambia de vuelta a la base original** Para dos bases ordenadas $B$ y $B'$,

$$\boxed{ S_{B'\leftarrow B} = S_{B\leftarrow B'}^{-1}. }$$

**Demostración.** proposición 4.39 aplicado al cambio de $B'$ hacia $B$ da, para todo $v\in V$,

$$[v]_B = S_{B\leftarrow B'}[v]_{B'}.$$

Aplicado en sentido contrario, $[v]_{B'} = S_{B'\leftarrow B}[v]_B.$

Sustituyendo la primera identidad en la segunda,

$$[v]_{B'} = S_{B'\leftarrow B} S_{B\leftarrow B'} [v]_{B'}.$$

Esto vale para toda columna de componentes en $B'$. Como proposición 4.7 establece una biyección entre $V$ y $\mathbb R^3$, las columnas $[v]_{B'}$ recorren todo $\mathbb R^3$. Luego

$$S_{B'\leftarrow B} S_{B\leftarrow B'} = I_3.$$

Por unicidad de la inversa, $S_{B'\leftarrow B} = S_{B\leftarrow B'}^{-1}.$

$\square$

La notación con flechas se comporta como esperamos:

$$\boxed{ B' \longrightarrow B \quad\text{se deshace con}\quad B\longrightarrow B'. }$$

[]{#proposición-composición-de-cambios-de-base}

### Proposición: composición de cambios de base {#fispm-c04-proposiciuxf3n-composiciuxf3n-de-cambios-de-base}

**Proposición 4.41 --- Regla de composición** Sean $B$, $B'$ y $C$ tres bases ordenadas. Entonces

$$\boxed{ S_{B\leftarrow C} = S_{B\leftarrow B'} S_{B'\leftarrow C}. }$$

**Demostración.** Para todo $v\in V$, proposición 4.39 da

$$[v]_{B'} = S_{B'\leftarrow C}[v]_C.$$

Luego,

$$\begin{aligned} [v]_B &= S_{B\leftarrow B'}[v]_{B'}\\ &= S_{B\leftarrow B'} S_{B'\leftarrow C}[v]_C. \end{aligned}$$

Pero también, por definición del cambio directo de $C$ a $B$, $[v]_B = S_{B\leftarrow C}[v]_C.$ Como las columnas $[v]_C$ recorren todo $\mathbb R^3$,

$$S_{B\leftarrow C} = S_{B\leftarrow B'} S_{B'\leftarrow C}.$$

$\square$

El orden de la multiplicación sigue el orden de las flechas: $C \longrightarrow B' \longrightarrow B.$ Primero actúa

$$S_{B'\leftarrow C},$$

y después

$$S_{B\leftarrow B'}.$$

[]{#consistencia-de-caminos}

### Consistencia de caminos {#fispm-c04-consistencia-de-caminos}

Supongamos que queremos convertir una columna desde $C$ hasta $B$. Podemos hacerlo directamente: $[v]_B = S_{B\leftarrow C}[v]_C.$

O podemos pasar por una base intermedia $B'$:

$$[v]_B = S_{B\leftarrow B'} S_{B'\leftarrow C} [v]_C.$$

Proposición 4.41 garantiza que ambos caminos producen exactamente la misma columna. Por eso un diagrama de cambios de base debe ser **conmutativo**:

$$\boxed{ \text{el resultado no depende del camino de bases intermedias}. }$$

Este criterio es una herramienta práctica de control: si dos rutas producen matrices distintas, alguna convención de flechas o algún orden de multiplicación fue usado incorrectamente.

[]{#ejemplo-con-tres-bases}

### Ejemplo con tres bases {#fispm-c04-ejemplo-con-tres-bases}

Sea

$$B=(e_1,e_2,e_3).$$

Definimos $B' = (e_1+e_2,\ e_2,\ e_3),$

de modo que

$$S_{B\leftarrow B'} = \begin{pmatrix} 1&0&0\\ 1&1&0\\ 0&0&1 \end{pmatrix}.$$

Ahora definimos $C = (e'_1,\ e'_2+e'_3,\ e'_3).$

Respecto de $B'$,

$$S_{B'\leftarrow C} = \begin{pmatrix} 1&0&0\\ 0&1&0\\ 0&1&1 \end{pmatrix}.$$

Por proposición 4.41,

$$S_{B\leftarrow C} = S_{B\leftarrow B'} S_{B'\leftarrow C}.$$

Multiplicando,

$$S_{B\leftarrow C} = \begin{pmatrix} 1&0&0\\ 1&1&0\\ 0&0&1 \end{pmatrix} \begin{pmatrix} 1&0&0\\ 0&1&0\\ 0&1&1 \end{pmatrix} = \begin{pmatrix} 1&0&0\\ 1&1&0\\ 0&1&1 \end{pmatrix}.$$

Podemos verificarlo directamente desde los vectores de $C$:

$$c_1=e_1+e_2,$$

$$c_2=e_2+e_3,$$

$$c_3=e_3.$$

Sus columnas en $B$ son precisamente

$$\begin{pmatrix} 1\\ 1\\ 0 \end{pmatrix}, \qquad \begin{pmatrix} 0\\ 1\\ 1 \end{pmatrix}, \qquad \begin{pmatrix} 0\\ 0\\ 1 \end{pmatrix},$$

que forman la matriz obtenida por composición.

[]{#proposición-compatibilidad-con-determinantes-y-orientación}

### Proposición: compatibilidad con determinantes y orientación {#fispm-c04-proposiciuxf3n-compatibilidad-con-determinantes-y-orientaciuxf3n}

**Proposición 4.42 --- Determinante de un cambio compuesto** Para tres bases $B$, $B'$ y $C$,

$$\boxed{ \det S_{B\leftarrow C} = \det S_{B\leftarrow B'} \det S_{B'\leftarrow C}. }$$

**Demostración.** Es una consecuencia inmediata de la proposición 4.41 y proposición 4.26:

$$\begin{aligned} \det S_{B\leftarrow C} &= \det\left( S_{B\leftarrow B'} S_{B'\leftarrow C} \right)\\ &= \det S_{B\leftarrow B'} \det S_{B'\leftarrow C}. \end{aligned}$$

$\square$

Por tanto, los signos también se componen:

- dos cambios que invierten orientación producen un cambio que la conserva;

- un único cambio de signo negativo invierte orientación;

- cambios de signo positivo conservan la clase de orientación.

Esto conecta la convención matricial de §10 con las clases de orientación construidas en §8.

[]{#principio-metodológico-de-consistencia}

### Principio metodológico de consistencia {#fispm-c04-principio-metodoluxf3gico-de-consistencia}

**Principio metodológico 4.17 --- Leer las flechas antes de multiplicar matrices de cambio** Para una matriz

$$S_{A\leftarrow B},$$

interpretar siempre:

$$\text{componentes en }B \longrightarrow \text{componentes en }A.$$

Dos matrices pueden multiplicarse directamente sólo cuando las flechas intermedias encajan:

$$S_{A\leftarrow B} S_{B\leftarrow C} = S_{A\leftarrow C}.$$

La regla funciona como un control de tipos: $C \to B \to A.$ Si las etiquetas no encajan, el producto no representa la composición pretendida aunque la multiplicación matricial sea algebraicamente posible.

[]{#balance-inversión-composición-y-consistencia}

### Balance: inversión, composición y consistencia {#fispm-c04-balance-inversiuxf3n-composiciuxf3n-y-consistencia}

Ya disponemos de una red coherente de cambios pasivos:

$$\boxed{ S_{B\leftarrow B}=I, }$$

$$\boxed{ S_{B'\leftarrow B} = S_{B\leftarrow B'}^{-1}, }$$

y

$$\boxed{ S_{B\leftarrow C} = S_{B\leftarrow B'} S_{B'\leftarrow C}. }$$

Estas identidades aseguran que la descripción de un vector puede convertirse entre bases sin ambigüedad y sin transformar el vector geométrico. Todavía falta estudiar cómo cambia la **matriz de una transformación lineal** cuando cambiamos la base usada para describirla.

[]{#definir-matriz-de-una-transformación-lineal-en-una-base}

### Definir: matriz de una transformación lineal en una base {#fispm-c04-definir-matriz-de-una-transformaciuxf3n-lineal-en-una-base}

**Definición 4.31 --- Matriz de una transformación lineal** Sea

$$T:V\longrightarrow V$$

lineal y sea

$$B=(e_1,e_2,e_3)$$

una base ordenada. Definimos

$$\boxed{ A_B(T) := \begin{pmatrix} \vert&\vert&\vert\\ {}[T(e_1)]_B&[T(e_2)]_B&[T(e_3)]_B\\ \vert&\vert&\vert \end{pmatrix}. }$$

Entonces, para todo $v\in V$,

$$\boxed{ [T(v)]_B = A_B(T)[v]_B. }$$

La matriz depende de la base. La transformación lineal $T$ no. Por eso no es correcto identificar sin más

$$T \quad\text{con}\quad A_B(T).$$

La matriz es una representación de $T$ una vez elegida una base.

[]{#proposición-ley-de-conjugación}

### Proposición: ley de conjugación {#fispm-c04-proposiciuxf3n-ley-de-conjugaciuxf3n}

**Proposición 4.43 --- Cambio de base de la matriz de un operador** Sean $B$ y $B'$ dos bases y sea

$$S:=S_{B\leftarrow B'}.$$

Entonces

$$\boxed{ A_{B'}(T) = S^{-1}A_B(T)S. }$$

**Demostración.** Para todo $v\in V$,

$$[v]_B = S[v]_{B'}.$$

Aplicamos $T$ y escribimos el resultado en la base $B$: $[T(v)]_B = A_B(T)[v]_B = A_B(T)S[v]_{B'}.$ Ahora convertimos la columna resultante desde $B$ hacia $B'$: $[T(v)]_{B'} = S^{-1}[T(v)]_B.$ Por tanto, $[T(v)]_{B'} = S^{-1}A_B(T)S[v]_{B'}.$ Pero, por la definición 4.31, $[T(v)]_{B'} = A_{B'}(T)[v]_{B'}.$

Como las columnas $[v]_{B'}$ recorren todo $\mathbb R^3$, $A_{B'}(T) = S^{-1}A_B(T)S.$

$\square$

El patrón de la fórmula refleja exactamente el recorrido conceptual:

$$B' \ \xrightarrow{\ S\ }\ B \ \xrightarrow{\ A_B(T)\ }\ B \ \xrightarrow{\ S^{-1}\ }\ B'.$$

[]{#misma-transformación-matrices-distintas}

### Misma transformación, matrices distintas {#fispm-c04-misma-transformaciuxf3n-matrices-distintas}

La igualdad $A_{B'}(T) = S^{-1}A_B(T)S$

no describe tres transformaciones activas sucesivas aplicadas al vector físico. Describe una sola transformación geométrica $T$ expresada en dos sistemas de coordenadas distintos. Por eso las matrices

$$A_B(T) \qquad\text{y}\qquad A_{B'}(T)$$

pueden ser numéricamente diferentes y, sin embargo, representar exactamente el mismo operador.

**Principio metodológico 4.18 --- No confundir el operador con una de sus matrices** Al cambiar de base, mantener fijo el operador geométrico y transformar su representación por conjugación:

$$A_{B'}(T)=S^{-1}A_B(T)S.$$

Una diferencia entre matrices no implica una diferencia entre operadores.

[]{#proposición-el-determinante-del-operador-no-depende-de-la-base}

### Proposición: el determinante del operador no depende de la base {#fispm-c04-proposiciuxf3n-el-determinante-del-operador-no-depende-de-la-base}

**Proposición 4.44 --- Invariancia del determinante bajo cambio de base** Para cualquier transformación lineal $T$ y cualesquiera bases $B,B'$,

$$\boxed{ \det A_{B'}(T) = \det A_B(T). }$$

**Demostración.** Por proposición 4.43,

$$A_{B'}(T) = S^{-1}A_B(T)S.$$

Aplicando proposición 4.26,

$$\det A_{B'}(T) = \det(S^{-1}) \det A_B(T) \det(S).$$

Como $SS^{-1}=I,$

Proposición 4.26 implica $\det(S)\det(S^{-1})=1.$

Luego

$$\det A_{B'}(T) = \det A_B(T).$$

$\square$

Así, aunque la matriz cambie con la base, su determinante es una propiedad intrínseca del operador lineal.

[]{#ejemplo-una-matriz-diagonal-deja-de-ser-diagonal}

### Ejemplo: una matriz diagonal deja de ser diagonal {#fispm-c04-ejemplo-una-matriz-diagonal-deja-de-ser-diagonal}

Sea

$$B=(e_1,e_2,e_3),$$

y definamos

$$T(e_1)=2e_1, \qquad T(e_2)=3e_2, \qquad T(e_3)=4e_3.$$

Entonces

$$A_B(T) = \begin{pmatrix} 2&0&0\\ 0&3&0\\ 0&0&4 \end{pmatrix}.$$

Tomemos la base

$$B' = (e_1+e_2,\ e_2,\ e_3),$$

para la cual

$$S= S_{B\leftarrow B'} = \begin{pmatrix} 1&0&0\\ 1&1&0\\ 0&0&1 \end{pmatrix},$$

y

$$S^{-1} = \begin{pmatrix} 1&0&0\\ -1&1&0\\ 0&0&1 \end{pmatrix}.$$

Por proposición 4.43, $A_{B'}(T) = S^{-1}A_B(T)S.$

Calculando,

$$A_B(T)S = \begin{pmatrix} 2&0&0\\ 3&3&0\\ 0&0&4 \end{pmatrix},$$

y por tanto

$$\boxed{ A_{B'}(T) = \begin{pmatrix} 2&0&0\\ 1&3&0\\ 0&0&4 \end{pmatrix}. }$$

La matriz ya no es diagonal, aunque el operador $T$ sea exactamente el mismo. Además, $\det A_B(T)=24,$

y

$$\det A_{B'}(T)=24,$$

como predice proposición 4.44.

[]{#fispm-t1-c04-e0020}

**Ejercicio 4.20 --- Cambio pasivo y transformación activa.**

**Función pedagógica:** `Diagnóstico conceptual → Conversión de coordenadas → Activo/pasivo`

Sea

$$B=(e_1,e_2,e_3),$$

y

$$B' = (e_1+e_2,\ e_2,\ e_3).$$

Para

$$v=2e_1+3e_2+e_3,$$

realiza dos operaciones distintas:

1.  calcula $[v]_{B'}$ sin cambiar el vector;

2.  define $T_S(e_j)=e'_j$ y calcula $[T_S(v)]_B$.

Explica por qué aparecen $S^{-1}$ y $S$, respectivamente.

**Solución desarrollada**

Tenemos

$$S= \begin{pmatrix} 1&0&0\\ 1&1&0\\ 0&0&1 \end{pmatrix}, \qquad S^{-1} = \begin{pmatrix} 1&0&0\\ -1&1&0\\ 0&0&1 \end{pmatrix},$$

y

$$[v]_B = \begin{pmatrix} 2\\ 3\\ 1 \end{pmatrix}.$$

**Cambio pasivo:**

$$[v]_{B'} = S^{-1}[v]_B = \begin{pmatrix} 2\\ 1\\ 1 \end{pmatrix}.$$

El vector sigue siendo

$$v=2e_1+3e_2+e_3.$$

**Transformación activa:**

$$[T_S(v)]_B = S[v]_B = \begin{pmatrix} 2\\ 5\\ 1 \end{pmatrix}.$$

Ahora el vector sí cambió: $T_S(v)=2e_1+5e_2+e_3.$ El uso de $S^{-1}$ o $S$ responde a preguntas distintas, no a una elección notacional.

[]{#fispm-t1-c04-e0021}

**Ejercicio 4.21 --- Una transformación, dos matrices.**

**Función pedagógica:** `Conjugación → Verificación → Invariante`

En la base

$$B=(e_1,e_2,e_3),$$

una transformación lineal $T$ tiene matriz

$$A_B(T) = \begin{pmatrix} 2&0&0\\ 0&3&0\\ 0&0&4 \end{pmatrix}.$$

Sea

$$B' = (e_1+e_2,\ e_2,\ e_3).$$

1.  Calcula $S_{B\leftarrow B'}$ y su inversa.

2.  Calcula $A_{B'}(T)$.

3.  Verifica la acción sobre $e'_1$ directamente.

4.  Compara los determinantes de ambas matrices.

**Solución desarrollada**

Como antes,

$$S= \begin{pmatrix} 1&0&0\\ 1&1&0\\ 0&0&1 \end{pmatrix}, \qquad S^{-1} = \begin{pmatrix} 1&0&0\\ -1&1&0\\ 0&0&1 \end{pmatrix}.$$

Por proposición 4.43,

$$A_{B'}(T) = S^{-1}A_B(T)S = \boxed{ \begin{pmatrix} 2&0&0\\ 1&3&0\\ 0&0&4 \end{pmatrix} }.$$

Para verificar la primera columna, observamos que

$$e'_1=e_1+e_2,$$

de modo que

$$T(e'_1) = 2e_1+3e_2.$$

Buscamos

$$2e_1+3e_2 = \alpha(e_1+e_2)+\beta e_2.$$

Comparando coeficientes, $\alpha=2, \qquad \beta=1.$ Por tanto,

$$[T(e'_1)]_{B'} = \begin{pmatrix} 2\\ 1\\ 0 \end{pmatrix},$$

que coincide con la primera columna de $A_{B'}(T)$.

Finalmente, $\det A_B(T)=24$

y

$$\det A_{B'}(T)=24.$$

El operador es el mismo; sólo cambia su representación matricial.

[]{#cierre-de-10}

### Cierre de §10 {#fispm-c04-cierre-de-10}

La sección ha distinguido tres objetos que suelen confundirse:

$$\boxed{ \text{vector geométrico}, \qquad \text{columna de coordenadas}, \qquad \text{matriz de un operador}. }$$

Para un cambio pasivo de base,

$$\boxed{ [v]_{B'} = S_{B\leftarrow B'}^{-1}[v]_B. }$$

Para una transformación activa en una base fija,

$$\boxed{ [T(v)]_B = A_B(T)[v]_B. }$$

Y para el mismo operador expresado en dos bases,

$$\boxed{ A_{B'}(T) = S_{B\leftarrow B'}^{-1} A_B(T) S_{B\leftarrow B'}. }$$

Las matrices de cambio satisfacen además

$$\boxed{ S_{B'\leftarrow B} = S_{B\leftarrow B'}^{-1}, }$$

y

$$\boxed{ S_{B\leftarrow C} = S_{B\leftarrow B'} S_{B'\leftarrow C}. }$$

La conclusión metodológica es simple:

$$\boxed{ \text{antes de multiplicar matrices, declarar qué objeto cambia y en qué base se expresa}. }$$

La siguiente sección estudiará transformaciones lineales que preservan la geometría euclídea: rotaciones, reflexiones e isometrías. El siguiente paso será el §[11](#fispm-c04-rotaciones-reflexiones-e-isometruxedas).

[]{#rotaciones-reflexiones-e-isometrías}

[]{#fispm-t1-c04-s11}

[]{#fpm-i-04-s11}

## 11. Rotaciones, reflexiones e isometrías {#fispm-c04-rotaciones-reflexiones-e-isometruxedas}

[]{#activación-transformar-sin-deformar}

### Activación: transformar sin deformar {#fispm-c04-activaciuxf3n-transformar-sin-deformar}

Una transformación lineal general

$$T:V\longrightarrow V$$

puede cambiar longitudes, ángulos y volúmenes. Pero hay transformaciones especiales que mueven los vectores sin deformar la geometría euclídea. Queremos caracterizar las transformaciones lineales que conservan exactamente la norma: $\|T(v)\|=\|v\|$

[]{#fig:I-04-R05}

<figure id="fig-fpm-v04-i-04-r05" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-04-R05.svg" class="lightbox" data-gallery="fpm-v04-c04"><img src="/assets/books/fispm/v04/I-04-R05.svg" alt="Una isometría puede invertir la orientación. Diagrama del capítulo 4; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="342" height="281" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 4.7.** La reflexión $S(x,y)=(-x,y)$ conserva longitudes y ángulos y tiene determinante $-1$. Por ello no es una rotación propia del plano. Véase §[11](#fispm-c04-rotaciones-reflexiones-e-isometruxedas).

</figcaption>

</figure>

para todo $v\in V$. Como $T$ es lineal,

$$T(0)=0,$$

así que estas transformaciones fijan el origen vectorial. Las traslaciones y, más en general, las isometrías afines que no fijan el origen se tratarán al estudiar cambios de marco.

[]{#fispm-c04-definir-isometruxeda-lineal label="fispm-c04-definir-isometruxeda-lineal"}

**Definición 4.32 --- Isometría lineal** Una transformación lineal

$$T:V\longrightarrow V$$

es una **isometría lineal** si

$$\boxed{ \|T(v)\|=\|v\| }$$

para todo $v\in V$. La definición es intrínseca: no requiere elegir una base. Además, para cualesquiera $P,Q$ en el espacio afín modelado sobre $V$, si aplicamos $T$ a sus desplazamientos,

$$\|T(\overrightarrow{PQ})\| = \|\overrightarrow{PQ}\|.$$

Por eso una isometría lineal conserva las longitudes de todos los vectores de desplazamiento.

[]{#polarización-recuperar-el-producto-escalar-desde-la-norma}

### Polarización: recuperar el producto escalar desde la norma {#fispm-c04-polarizaciuxf3n-recuperar-el-producto-escalar-desde-la-norma}

En un espacio euclídeo real, $\|u+v\|^2 = \langle u+v,u+v\rangle.$ Por bilinealidad y simetría,

$$\|u+v\|^2 = \|u\|^2 + 2\langle u,v\rangle + \|v\|^2.$$

Despejando,

$$\boxed{ \langle u,v\rangle = \frac12 \left( \|u+v\|^2 - \|u\|^2 - \|v\|^2 \right). }$$

Esta identidad muestra que, en el caso real, la norma determina completamente el producto escalar.

[]{#proposición-preservar-norma-equivale-a-preservar-producto-escalar}

### Proposición: preservar norma equivale a preservar producto escalar {#fispm-c04-proposiciuxf3n-preservar-norma-equivale-a-preservar-producto-escalar}

**Proposición 4.45 --- Caracterización intrínseca de las isometrías lineales** Sea

$$T:V\longrightarrow V$$

lineal. Son equivalentes:

1.  $T$ preserva la norma:

$$\|T(v)\|=\|v\|$$

para todo $v$;

1.  $T$ preserva el producto escalar:

$$\boxed{ \langle T(u),T(v)\rangle = \langle u,v\rangle }$$

para todos $u,v\in V$.

**Demostración.** Supongamos primero que $T$ preserva la norma. Como $T$ es lineal,

$$T(u+v)=T(u)+T(v).$$

Aplicamos la identidad de polarización:

$$\begin{aligned} \langle T(u),T(v)\rangle &= \frac12 \left( \|T(u)+T(v)\|^2 - \|T(u)\|^2 - \|T(v)\|^2 \right)\\ &= \frac12 \left( \|T(u+v)\|^2 - \|T(u)\|^2 - \|T(v)\|^2 \right)\\ &= \frac12 \left( \|u+v\|^2 - \|u\|^2 - \|v\|^2 \right)\\ &= \langle u,v\rangle. \end{aligned}$$

Recíprocamente, si $T$ preserva el producto escalar, entonces

$$\|T(v)\|^2 = \langle T(v),T(v)\rangle = \langle v,v\rangle = \|v\|^2.$$

Como ambas normas son no negativas, $\|T(v)\|=\|v\|.$

$\square$

Por tanto, una isometría lineal conserva simultáneamente longitudes y ángulos.

[]{#consecuencias-geométricas-inmediatas}

### Consecuencias geométricas inmediatas {#fispm-c04-consecuencias-geomuxe9tricas-inmediatas}

Si $T$ es una isometría lineal, proposición 4.45 da $\langle T(u),T(v)\rangle = \langle u,v\rangle.$

Por tanto:

[]{#ortogonalidad}

#### Ortogonalidad {#fispm-c04-ortogonalidad}

Si

$$u\perp v,$$

entonces $\langle u,v\rangle=0,$

y así $\langle T(u),T(v)\rangle=0.$

Luego

$$\boxed{ u\perp v \Longrightarrow T(u)\perp T(v). }$$

[]{#ángulos}

#### Ángulos {#fispm-c04-uxe1ngulos}

Para $u,v\ne0$,

$$\cos\theta(T(u),T(v)) = \frac{\langle T(u),T(v)\rangle} {\|T(u)\|\|T(v)\|}.$$

Como producto escalar y normas se conservan,

$$\boxed{ \theta(T(u),T(v)) = \theta(u,v). }$$

[]{#distancias-entre-vectores}

#### Distancias entre vectores {#fispm-c04-distancias-entre-vectores}

Por linealidad, $T(u)-T(v) = T(u-v).$

Entonces $\|T(u)-T(v)\| = \|T(u-v)\| = \|u-v\|.$ Así una isometría lineal conserva también la distancia euclídea entre cualesquiera dos vectores considerados como puntos del espacio vectorial.

[]{#matriz-de-una-isometría-en-una-base-ortonormal}

### Matriz de una isometría en una base ortonormal {#fispm-c04-matriz-de-una-isometruxeda-en-una-base-ortonormal}

Sea

$$E=(e_1,e_2,e_3)$$

una base ortonormal y sea

$$Q:=A_E(T).$$

Las columnas de $Q$ son

$$[T(e_1)]_E, \qquad [T(e_2)]_E, \qquad [T(e_3)]_E.$$

Si $T$ es una isometría, proposición 4.45 implica

$$\langle T(e_i),T(e_j)\rangle = \langle e_i,e_j\rangle = \delta_{ij}.$$

Por tanto, las columnas de $Q$ forman una base ortonormal. En coordenadas respecto de $E$, esto equivale a que los productos escalares entre columnas produzcan la matriz identidad.

[]{#proposición-caracterización-matricial}

### Proposición: caracterización matricial {#fispm-c04-proposiciuxf3n-caracterizaciuxf3n-matricial}

**Proposición 4.46 --- Matriz ortogonal de una isometría** Sea $E$ una base ortonormal y

$$Q=A_E(T).$$

Entonces $T$ es una isometría lineal si y sólo si

$$\boxed{ Q^{\mathsf T}Q=I_3. }$$

**Demostración.** Las entradas de

$$Q^{\mathsf T}Q$$

son los productos escalares entre las columnas de $Q$. Como la columna $j$ es $[T(e_j)]_E,$

tenemos

$$(Q^{\mathsf T}Q)_{ij} = \langle T(e_i),T(e_j)\rangle.$$

Si $T$ es isometría, proposición 4.45 da $\langle T(e_i),T(e_j)\rangle = \delta_{ij},$

por lo que

$$Q^{\mathsf T}Q=I_3.$$

Recíprocamente, supongamos $Q^{\mathsf T}Q=I_3.$ Para cualesquiera $u,v\in V$, escribimos

$$x=[u]_E, \qquad y=[v]_E.$$

Como $E$ es ortonormal, $\langle u,v\rangle = x^{\mathsf T}y.$

Además, $[T(u)]_E=Qx, \qquad [T(v)]_E=Qy.$

Entonces

$$\begin{aligned} \langle T(u),T(v)\rangle &= (Qx)^{\mathsf T}(Qy)\\ &= x^{\mathsf T}Q^{\mathsf T}Qy\\ &= x^{\mathsf T}y\\ &= \langle u,v\rangle. \end{aligned}$$

Por proposición 4.45, $T$ es una isometría. $\square$ Una matriz que satisface $Q^{\mathsf T}Q=I_3$

se denomina **matriz ortogonal**.

[]{#consecuencias-algebraicas-de-la-ortogonalidad}

### Consecuencias algebraicas de la ortogonalidad {#fispm-c04-consecuencias-algebraicas-de-la-ortogonalidad}

De

$$Q^{\mathsf T}Q=I_3$$

se sigue que $Q^{\mathsf T}$ es una inversa por la izquierda. Tomando determinantes, $\det(Q^{\mathsf T}Q) = \det I_3 = 1.$ Por proposición 4.26 y por $\det(Q^{\mathsf T})=\det Q,$

obtenemos $(\det Q)^2=1.$ Por tanto,

$$\boxed{ \det Q=\pm1. }$$

En particular, $\det Q\ne0,$

de modo que $Q$ es invertible. Así,

$$\boxed{ Q^{-1}=Q^{\mathsf T}. }$$

Toda isometría lineal es, por tanto, biyectiva. El signo de $\det Q$ permitirá distinguir, más adelante en esta sección, las isometrías que conservan orientación de aquellas que la invierten.

[]{#no-confundir-matriz-ortogonal-con-base-ortonormal}

### No confundir matriz ortogonal con base ortonormal {#fispm-c04-no-confundir-matriz-ortogonal-con-base-ortonormal}

Una **base ortonormal** es una terna ordenada de vectores

$$(e_1,e_2,e_3)$$

que satisface $\langle e_i,e_j\rangle=\delta_{ij}.$ Una **matriz ortogonal** es una matriz cuadrada

$$Q$$

que satisface $Q^{\mathsf T}Q=I.$

La relación es la siguiente:

> las columnas de una matriz ortogonal, interpretadas en una base ortonormal de referencia, forman otra base ortonormal.

Pero los dos objetos no son del mismo tipo.

[]{#cambio-pasivo-frente-a-isometría-activa}

### Cambio pasivo frente a isometría activa {#fispm-c04-cambio-pasivo-frente-a-isometruxeda-activa}

En §10 vimos que una matriz ortogonal también puede aparecer como matriz de cambio entre dos bases ortonormales. Eso no convierte automáticamente el cambio de base en una transformación activa. Si

$$S_{E\leftarrow E'}$$

relaciona dos bases ortonormales, entonces $S^{\mathsf T}S=I.$ En el problema **pasivo**, $[v]_{E'} = S^{-1}[v]_E = S^{\mathsf T}[v]_E,$

mientras el vector $v$ permanece fijo. En un problema **activo**, una isometría $T$ con matriz

$$Q=A_E(T)$$

transforma el vector: $[T(v)]_E = Q[v]_E.$

Aunque $S$ y $Q$ puedan ser numéricamente iguales, describen problemas conceptualmente distintos.

**Principio metodológico 4.19 --- Distinguir ortogonalidad matricial de la naturaleza del proceso** La condición

$$M^{\mathsf T}M=I$$

informa que una matriz preserva el producto escalar en coordenadas ortonormales. No indica por sí sola si la matriz se está usando:

- como cambio pasivo entre bases ortonormales;

- o como representación activa de una isometría lineal.

Declarar siempre qué objeto permanece fijo y qué objeto se transforma.

[]{#balance-de-la-ortogonalidad-matricial-a-la-orientación}

### Balance: de la ortogonalidad matricial a la orientación {#fispm-c04-balance-de-la-ortogonalidad-matricial-a-la-orientaciuxf3n}

Ya tenemos la caracterización esencial:

$$\boxed{ T\text{ isometría lineal} \Longleftrightarrow \langle T(u),T(v)\rangle = \langle u,v\rangle }$$

y, en una base ortonormal,

$$\boxed{ T\text{ isometría lineal} \Longleftrightarrow Q^{\mathsf T}Q=I. }$$

Además,

$$\boxed{ Q^{-1}=Q^{\mathsf T}, \qquad \det Q=\pm1. }$$

Todavía falta interpretar geométricamente las dos posibilidades del determinante:

- $\det Q=+1$: isometrías que conservan orientación;

- $\det Q=-1$: isometrías que invierten orientación.

[]{#definir-isometrías-propias-e-impropias}

### Definir: isometrías propias e impropias {#fispm-c04-definir-isometruxedas-propias-e-impropias}

**Definición 4.33 --- Isometría propia e impropia** Sea $T$ una isometría lineal y sea

$$Q=A_E(T)$$

su matriz en una base ortonormal $E$.

Diremos que $T$ es **propia** si

$$\boxed{ \det Q=+1, }$$

y **impropia** si

$$\boxed{ \det Q=-1. }$$

Proposición 4.44 garantiza que el determinante de la matriz de un operador no depende de la base. Por tanto, esta definición es intrínseca.

[]{#proposición-el-signo-del-determinante-controla-la-orientación}

### Proposición: el signo del determinante controla la orientación {#fispm-c04-proposiciuxf3n-el-signo-del-determinante-controla-la-orientaciuxf3n}

**Proposición 4.47 --- Orientación bajo una isometría** Sea

$$E=(e_1,e_2,e_3)$$

una base ortonormal positivamente orientada y sea $T$ una isometría lineal con matriz $Q=A_E(T)$.

Entonces:

$$\boxed{ \det Q=+1 \Longleftrightarrow (T(e_1),T(e_2),T(e_3)) \text{ tiene orientación positiva}, }$$

mientras

$$\boxed{ \det Q=-1 \Longleftrightarrow (T(e_1),T(e_2),T(e_3)) \text{ tiene orientación negativa}. }$$

**Demostración.** Las columnas de $Q$ son precisamente

$$[T(e_1)]_E, \qquad [T(e_2)]_E, \qquad [T(e_3)]_E.$$

Por definición 4.26, el signo de

$$\det Q$$

es exactamente la orientación relativa de la base imagen respecto de $E$. $\square$ Así, una isometría propia conserva orientación y una impropia la invierte.

[]{#definir-reflexión-ortogonal-respecto-de-un-plano}

### Definir: reflexión ortogonal respecto de un plano {#fispm-c04-definir-reflexiuxf3n-ortogonal-respecto-de-un-plano}

Sea $n$ un vector unitario: $\|n\|=1.$ El plano vectorial perpendicular a $n$ es $n^\perp = \{v\in V:\langle v,n\rangle=0\}.$

**Definición 4.34 --- Reflexión ortogonal respecto del plano perpendicular a n** Definimos

$$\boxed{ H_n(v) := v-2\langle v,n\rangle n. }$$

Por proposición 4.16, todo vector se descompone de manera única como $v=v_\perp+v_\parallel,$

donde

$$v_\parallel=\langle v,n\rangle n$$

y

$$v_\perp\perp n.$$

Entonces $H_n(v) = v_\perp-v_\parallel.$ La reflexión conserva la componente contenida en el plano $n^\perp$ e invierte la componente normal.

[]{#proposición-la-reflexión-es-una-isometría-impropia}

### Proposición: la reflexión es una isometría impropia {#fispm-c04-proposiciuxf3n-la-reflexiuxf3n-es-una-isometruxeda-impropia}

**Proposición 4.48 --- Propiedades de la reflexión ortogonal** Para todo vector unitario $n$, la aplicación $H_n$ satisface:

1.  es lineal;

2.  es una isometría;

3.  fija todo vector de $n^\perp$;

4.  envía $$n\longmapsto -n;$$

5.  satisface $$H_n^2=I;$$

6.  es impropia: $$\boxed{\det H_n=-1.}$$

**Demostración.** La linealidad se sigue directamente de la bilinealidad del producto escalar. Si

$$v=v_\perp+\alpha n,$$

con $v_\perp\perp n$, entonces $H_n(v)=v_\perp-\alpha n.$ Por Pitágoras, $\|H_n(v)\|^2 = \|v_\perp\|^2+\alpha^2 = \|v\|^2.$ Por definición 4.32, $H_n$ es una isometría. Si $v\in n^\perp$, entonces $\langle v,n\rangle=0,$

y por tanto

$$H_n(v)=v.$$

Además, $H_n(n) = n-2n = -n.$

Aplicar dos veces la misma regla devuelve cada componente a su signo inicial, de modo que

$$H_n^2=I.$$

Para el determinante, elegimos una base ortonormal positiva adaptada

$$E=(e_1,e_2,n),$$

con $e_1,e_2\in n^\perp$. Entonces

$$A_E(H_n) = \begin{pmatrix} 1&0&0\\ 0&1&0\\ 0&0&-1 \end{pmatrix}.$$

Por tanto, $\det H_n=-1.$

$\square$

La reflexión conserva todas las longitudes y ángulos, pero invierte la orientación.

[]{#construir-una-base-ortonormal-adaptada-a-un-eje}

### Construir una base ortonormal adaptada a un eje {#fispm-c04-construir-una-base-ortonormal-adaptada-a-un-eje}

Sea ahora $n$ unitario. Elegimos un vector

$$a\notin\operatorname{span}(n).$$

Su residuo perpendicular a $n$ es $r = a-\langle a,n\rangle n.$

Como $a$ no es paralelo a $n$, $r\ne0.$

Definimos $e_1:=\frac{r}{\|r\|}.$

Entonces $e_1\perp n, \qquad \|e_1\|=1.$

Definimos después

$$e_2:=n\times e_1.$$

Como $n$ y $e_1$ son unitarios y ortogonales, proposición 4.37 da $\|e_2\|=1.$

Además, §9 implica $e_2\perp n, \qquad e_2\perp e_1.$

Finalmente, proposición 4.38 muestra que

$$(n,e_1,e_2)$$

tiene orientación positiva. La permutación cíclica

$$(e_1,e_2,n)$$

también es positiva. Así obtenemos una base ortonormal positiva adaptada al eje $n$.

[]{#definir-rotación-axial}

### Definir: rotación axial {#fispm-c04-definir-rotaciuxf3n-axial}

**Definición 4.35 --- Rotación alrededor de un eje** Sea $n$ unitario y sea $\varphi\in\mathbb R$. Definimos

$$\boxed{ R_{n,\varphi}(v) := \cos\varphi\,v +(1-\cos\varphi)\langle n,v\rangle n +\sin\varphi\,(n\times v). }$$

Esta fórmula es intrínseca: utiliza únicamente el producto escalar, el producto vectorial y el eje unitario $n$. Si

$$v=\alpha n+w, \qquad w\perp n,$$

entonces

$$R_{n,\varphi}(v) = \alpha n + \cos\varphi\,w + \sin\varphi\,(n\times w).$$

Por tanto, la componente axial queda fija y la componente perpendicular rota dentro del plano $n^\perp$.

[]{#proposición-matriz-y-propiedades-de-una-rotación-axial}

### Proposición: matriz y propiedades de una rotación axial {#fispm-c04-proposiciuxf3n-matriz-y-propiedades-de-una-rotaciuxf3n-axial}

**Proposición 4.49 --- Rotación axial como isometría propia** Sea

$$E=(e_1,e_2,n)$$

una base ortonormal positivamente orientada adaptada al eje $n$. Entonces

$$\boxed{ A_E(R_{n,\varphi}) = \begin{pmatrix} \cos\varphi&-\sin\varphi&0\\ \sin\varphi&\cos\varphi&0\\ 0&0&1 \end{pmatrix}. }$$

En particular:

1.  $R_{n,\varphi}$ es una isometría lineal;

2.  fija el eje: $$R_{n,\varphi}(n)=n;$$

3.  es propia: $$\boxed{ \det R_{n,\varphi}=+1. }$$

**Demostración.** Por bilinealidad del producto escalar y proposición 4.34, las aplicaciones

$$v\longmapsto v, \qquad v\longmapsto \langle n,v\rangle n, \qquad v\longmapsto n\times v$$

son lineales. Por tanto, definición 4.35 define una transformación lineal

$$R_{n,\varphi}:V\longrightarrow V,$$

y definición 4.31 permite formar su matriz $A_E(R_{n,\varphi})$. Como la base es positiva, $n\times e_1=e_2,$

y por antisimetría, $n\times e_2=-e_1.$

Además, $n\times n=0.$ Por definición 4.35,

$$R_{n,\varphi}(e_1) = \cos\varphi\,e_1 + \sin\varphi\,e_2,$$

$$R_{n,\varphi}(e_2) = -\sin\varphi\,e_1 + \cos\varphi\,e_2,$$

y

$$R_{n,\varphi}(n)=n.$$

Estas tres columnas producen la matriz indicada. Un cálculo directo da

$$A_E(R_{n,\varphi})^{\mathsf T} A_E(R_{n,\varphi}) = I_3,$$

usando

$$\cos^2\varphi+\sin^2\varphi=1.$$

Por proposición 4.46, la transformación es una isometría. Finalmente,

$$\det A_E(R_{n,\varphi}) = \cos^2\varphi+\sin^2\varphi = 1.$$

Por proposición 4.44, este determinante es independiente de la base elegida. $\square$[^5]

[]{#rotación-y-reflexión-no-se-distinguen-por-conservar-distancias}

### Rotación y reflexión no se distinguen por conservar distancias {#fispm-c04-rotaciuxf3n-y-reflexiuxf3n-no-se-distinguen-por-conservar-distancias}

Tanto una rotación axial como una reflexión ortogonal satisfacen

$$\|T(v)\|=\|v\|.$$

Por tanto, ambas conservan:

- longitudes;

- productos escalares;

- ángulos;

- ortogonalidad;

- distancias.

La diferencia aparece en la orientación:

$$\boxed{ \det R_{n,\varphi}=+1, }$$

mientras

$$\boxed{ \det H_n=-1. }$$

Así, "preservar geometría métrica" no implica "preservar orientación".

[]{#principio-metodológico-qué-informa-el-determinante}

### Principio metodológico: qué informa el determinante {#fispm-c04-principio-metodoluxf3gico-quuxe9-informa-el-determinante}

**Principio metodológico 4.20 --- Usar el determinante para orientación, no para identificar toda la isometría** Para una matriz ortogonal $Q$:

$$\det Q=+1$$

indica que la isometría conserva orientación, mientras

$$\det Q=-1$$

indica que la invierte. El signo del determinante no determina por sí solo el ángulo, el eje o el plano geométrico concreto de la isometría. No toda la información de una isometría está contenida en un único escalar.

[]{#balance-rotaciones-y-reflexiones}

### Balance: rotaciones y reflexiones {#fispm-c04-balance-rotaciones-y-reflexiones}

Ya tenemos dos prototipos fundamentales: **Reflexión ortogonal**

$$\boxed{ H_n(v) = v-2\langle v,n\rangle n, \qquad \det H_n=-1, }$$

y **rotación axial**

$$\boxed{ R_{n,\varphi}(v) = \cos\varphi\,v +(1-\cos\varphi)\langle n,v\rangle n +\sin\varphi(n\times v), \qquad \det R_{n,\varphi}=+1. }$$

Ambas son isometrías activas, no meros cambios pasivos de base. Todavía falta completar la estructura algebraica mediante composición e inversa de isometrías y aplicar después estas distinciones en ejercicios.

[]{#proposición-composición-e-inversa-de-isometrías}

### Proposición: composición e inversa de isometrías {#fispm-c04-proposiciuxf3n-composiciuxf3n-e-inversa-de-isometruxedas}

**Proposición 4.50 --- Composición, inversa y signo** Sean $T_1$ y $T_2$ isometrías lineales. Entonces:

1.  la composición

$$T_2\circ T_1$$

es una isometría lineal;

1.  cada $T_i$ es invertible y

$$T_i^{-1}$$

es también una isometría lineal;

1.  los signos de orientación se multiplican:

$$\boxed{ \det(T_2\circ T_1) = \det(T_2)\det(T_1). }$$

**Demostración.** Elegimos una base ortonormal $E$ y escribimos

$$Q_1=A_E(T_1), \qquad Q_2=A_E(T_2).$$

Por proposición 4.46,

$$Q_1^{\mathsf T}Q_1=I, \qquad Q_2^{\mathsf T}Q_2=I.$$

La matriz de la composición es $A_E(T_2\circ T_1) = Q_2Q_1.$

Entonces

$$\begin{aligned} (Q_2Q_1)^{\mathsf T}(Q_2Q_1) &= Q_1^{\mathsf T}Q_2^{\mathsf T}Q_2Q_1\\ &= Q_1^{\mathsf T}IQ_1\\ &= I. \end{aligned}$$

Por proposición 4.46, la composición es una isometría. Además, $Q_i^{-1}=Q_i^{\mathsf T},$

y

$$(Q_i^{\mathsf T})^{\mathsf T}Q_i^{\mathsf T} = Q_iQ_i^{\mathsf T} = I,$$

de modo que la inversa también es ortogonal y representa una isometría. Finalmente, proposición 4.26 da $\det(Q_2Q_1) = \det(Q_2)\det(Q_1).$

Por proposición 4.44, este signo no depende de la base elegida. $\square$ La proposición permite leer inmediatamente:

- propia seguida de propia $\Rightarrow$ propia;

- impropia seguida de impropia $\Rightarrow$ propia;

- propia seguida de impropia, o viceversa, $\Rightarrow$ impropia.

[]{#comparación-estructural-rotación-frente-a-reflexión}

### Comparación estructural: rotación frente a reflexión {#fispm-c04-comparaciuxf3n-estructural-rotaciuxf3n-frente-a-reflexiuxf3n}

Rotaciones axiales y reflexiones ortogonales comparten toda la estructura métrica:

$$\boxed{ \|T(v)\|=\|v\|, \qquad \langle T(u),T(v)\rangle=\langle u,v\rangle. }$$

Pero difieren en tres rasgos fundamentales.

[]{#orientación}

#### Orientación {#fispm-c04-orientaciuxf3n}

Para una rotación axial, $\det R_{n,\varphi}=+1.$ Para una reflexión ortogonal, $\det H_n=-1.$

[]{#conjunto-de-vectores-fijos}

#### Conjunto de vectores fijos {#fispm-c04-conjunto-de-vectores-fijos}

Una rotación axial fija la recta

$$\operatorname{span}(n).$$

Una reflexión ortogonal fija el plano

$$n^\perp.$$

[]{#acción-sobre-la-dirección-normal}

#### Acción sobre la dirección normal {#fispm-c04-acciuxf3n-sobre-la-direcciuxf3n-normal}

La reflexión satisface $H_n(n)=-n.$ La rotación satisface $R_{n,\varphi}(n)=n.$ Por tanto, conocer sólo que una transformación es una isometría no basta para decidir su tipo geométrico.

**Principio metodológico 4.21 --- Clasificar una isometría por capas** Ante una isometría lineal, comprobar en este orden:

1.  ortogonalidad de su matriz;

2.  signo del determinante;

3.  subespacio de vectores fijos;

4.  acción sobre el complemento ortogonal.

No inferir eje, plano o ángulo únicamente a partir de $\det Q$.

[]{#fispm-t1-c04-e0022}

**Ejercicio 4.22 --- Reflexión en un plano.**

**Función pedagógica:** `Fórmula intrínseca → Matriz → Orientación`

Sea

$$E=(e_1,e_2,e_3)$$

una base ortonormal positiva y consideremos la reflexión respecto del plano

$$e_3^\perp.$$

1.  Calcula la matriz de $H_{e_3}$ en $E$.

2.  Verifica que es ortogonal.

3.  Calcula su determinante.

4.  Aplica la reflexión a

$$v=2e_1-e_2+3e_3.$$

1.  Verifica directamente que la norma se conserva.

**Solución desarrollada**

Como

$$H_{e_3}(e_1)=e_1, \qquad H_{e_3}(e_2)=e_2, \qquad H_{e_3}(e_3)=-e_3,$$

tenemos

$$\boxed{ A_E(H_{e_3}) = \begin{pmatrix} 1&0&0\\ 0&1&0\\ 0&0&-1 \end{pmatrix}. }$$

Esta matriz satisface $Q^{\mathsf T}Q=I_3,$

y

$$\boxed{\det Q=-1}.$$

Por tanto, la reflexión es una isometría impropia.

Aplicando la fórmula,

$$\boxed{ H_{e_3}(v) = 2e_1-e_2-3e_3. }$$

Finalmente, $\|v\|^2 = 2^2+(-1)^2+3^2 = 14,$

y

$$\|H_{e_3}(v)\|^2 = 2^2+(-1)^2+(-3)^2 = 14.$$

La norma se conserva, pero la orientación global se invierte.

[]{#fispm-t1-c04-e0023}

**Ejercicio 4.23 --- Rotación de cuarto de vuelta.**

**Función pedagógica:** `Rotación axial → Matriz → Invariantes`

Sea

$$E=(e_1,e_2,e_3)$$

una base ortonormal positiva. Considera la rotación alrededor del eje $e_3$ con ángulo

$$\varphi=\frac{\pi}{2}.$$

1.  Calcula su matriz en $E$.

2.  Verifica que es ortogonal.

3.  Calcula su determinante.

4.  Aplica la rotación a

$$v=2e_1+e_2+3e_3.$$

1.  Comprueba que la norma se conserva.

2.  Determina el resultado de aplicar cuatro veces la rotación.

**Solución desarrollada**

Como $\cos\frac{\pi}{2}=0, \qquad \sin\frac{\pi}{2}=1,$

Proposición 4.49 da

$$\boxed{ Q = \begin{pmatrix} 0&-1&0\\ 1&0&0\\ 0&0&1 \end{pmatrix}. }$$

Un cálculo directo muestra

$$Q^{\mathsf T}Q=I_3.$$

Además,

$$\boxed{\det Q=+1}.$$

La isometría es propia.

Aplicando $Q$ a

$$[v]_E= \begin{pmatrix} 2\\ 1\\ 3 \end{pmatrix},$$

obtenemos

$$[R_{e_3,\pi/2}(v)]_E = \begin{pmatrix} -1\\ 2\\ 3 \end{pmatrix}.$$

Por tanto,

$$\boxed{ R_{e_3,\pi/2}(v) = -e_1+2e_2+3e_3. }$$

Las normas satisfacen

$$\|v\|^2 = 2^2+1^2+3^2 = 14,$$

y

$$\|R_{e_3,\pi/2}(v)\|^2 = (-1)^2+2^2+3^2 = 14.$$

Finalmente,

$$Q^2 = \begin{pmatrix} -1&0&0\\ 0&-1&0\\ 0&0&1 \end{pmatrix},$$

y

$$\boxed{ Q^4=I_3. }$$

Cuatro cuartos de vuelta restauran todo vector.

[]{#cierre-de-11}

### Cierre de §11 {#fispm-c04-cierre-de-11}

La sección ha construido la noción de **transformación lineal que preserva la geometría**:

$$\boxed{ T\text{ isometría} \Longleftrightarrow \|T(v)\|=\|v\| }$$

y, equivalentemente,

$$\boxed{ \langle T(u),T(v)\rangle = \langle u,v\rangle. }$$

En una base ortonormal,

$$\boxed{ Q^{\mathsf T}Q=I, \qquad Q^{-1}=Q^{\mathsf T}, \qquad \det Q=\pm1. }$$

El signo del determinante separa las dos clases:

$$\boxed{ \det Q=+1 \Longrightarrow \text{isometría propia}, }$$

$$\boxed{ \det Q=-1 \Longrightarrow \text{isometría impropia}. }$$

Los prototipos construidos son:

$$\boxed{ R_{n,\varphi} \quad\text{rotación axial, propia}, }$$

y

$$\boxed{ H_n \quad\text{reflexión ortogonal, impropia}. }$$

La composición de isometrías vuelve a ser una isometría y los signos de orientación se multiplican. La siguiente sección volverá del espacio vectorial al espacio afín: estudiaremos simultáneamente cambios de origen y de base en un marco geométrico completo. El siguiente paso será el §[12](#fispm-c04-cambios-de-origen-y-de-marco-geomuxe9trico).

[]{#cambios-de-origen-y-de-marco-geométrico}

[]{#fispm-t1-c04-s12}

[]{#fpm-i-04-s12}

## 12. Cambios de origen y de marco geométrico {#fispm-c04-cambios-de-origen-y-de-marco-geomuxe9trico}

[]{#activación-ahora-cambian-dos-datos-a-la-vez}

### Activación: ahora cambian dos datos a la vez {#fispm-c04-activaciuxf3n-ahora-cambian-dos-datos-a-la-vez}

Hasta aquí hemos estudiado por separado dos operaciones:

1.  cambiar el **origen** manteniendo fija la base;

2.  cambiar la **base** manteniendo fijo el vector geométrico.

Un marco afín completo contiene ambos datos: $F=(O,B).$ Por tanto, al pasar a otro marco

$$F'=(O',B'),$$

pueden cambiar simultáneamente:

- el punto elegido como origen;

- la base usada para describir los desplazamientos.

La pregunta central es:

Cambio completo de marco Dado un punto $P$, ¿cómo se transforma su columna de coordenadas cuando pasamos de

$$F=(O,B)$$

a

$$F'=(O',B')?$$

La respuesta combinará exactamente las leyes de §§4 y 10.

[]{#definir-datos-de-un-cambio-de-marco-afín}

### Definir: datos de un cambio de marco afín {#fispm-c04-definir-datos-de-un-cambio-de-marco-afuxedn}

**Definición 4.36 --- Cambio entre dos marcos afines** Sean

$$F=(O,B), \qquad F'=(O',B')$$

dos marcos afines.

Definimos:

$$\boxed{ a:=\overrightarrow{OO'} }$$

y

$$\boxed{ S:=S_{B\leftarrow B'}. }$$

Es decir:

- $a$ es el desplazamiento desde el origen antiguo al nuevo;

- las columnas de $S$ son los vectores de la base nueva $B'$ expresados en la base antigua $B$.

Usaremos

$$[a]_B$$

para la columna del desplazamiento del origen nuevo respecto del antiguo. La convención de signo queda fijada por

$$\boxed{ O'=O+a. }$$

[]{#derivación-geométrica-antes-de-escribir-matrices}

### Derivación geométrica antes de escribir matrices {#fispm-c04-derivaciuxf3n-geomuxe9trica-antes-de-escribir-matrices}

Para cualquier punto $P$,

$$\overrightarrow{OP} = \overrightarrow{OO'} + \overrightarrow{O'P}.$$

Como $\overrightarrow{OO'}=a,$

obtenemos

$$\boxed{ \overrightarrow{O'P} = \overrightarrow{OP}-a. }$$

Esta identidad es puramente afín y no depende de coordenadas. Ahora expresamos ambos lados en la base antigua $B$:

$$[\overrightarrow{O'P}]_B = [\overrightarrow{OP}]_B-[a]_B.$$

Pero la columna que buscamos en el marco nuevo utiliza la base $B'$: $x_{F'}(P) = [\overrightarrow{O'P}]_{B'}.$ Por proposición 4.39,

$$[\overrightarrow{O'P}]_{B'} = S^{-1} [\overrightarrow{O'P}]_B.$$

Sustituir la relación anterior produce la ley completa.

[]{#proposición-ley-afín-de-cambio-de-marco}

### Proposición: ley afín de cambio de marco {#fispm-c04-proposiciuxf3n-ley-afuxedn-de-cambio-de-marco}

**Proposición 4.51 --- Transformación de las coordenadas de un punto** Sean

$$F=(O,B), \qquad F'=(O',B'),$$

con

$$a=\overrightarrow{OO'}, \qquad S=S_{B\leftarrow B'}.$$

Entonces, para todo punto $P$,

$$\boxed{ x_{F'}(P) = S^{-1} \left( x_F(P)-[a]_B \right). }$$

**Demostración.** Por definición 4.12,

$$x_F(P) = [\overrightarrow{OP}]_B,$$

y

$$x_{F'}(P) = [\overrightarrow{O'P}]_{B'}.$$

La ley del triángulo da $\overrightarrow{O'P} = \overrightarrow{OP}-a.$

Tomando componentes en $B$, $[\overrightarrow{O'P}]_B = x_F(P)-[a]_B.$

Finalmente, proposición 4.39 transforma componentes desde $B$ hacia $B'$:

$$[\overrightarrow{O'P}]_{B'} = S^{-1} [\overrightarrow{O'P}]_B.$$

Por tanto, $x_{F'}(P) = S^{-1} \left( x_F(P)-[a]_B \right).$

$\square$

Ésta será la convención canónica para todos los cambios de marco del capítulo.

[]{#por-qué-la-transformación-de-puntos-es-afín-no-lineal}

### Por qué la transformación de puntos es afín, no lineal {#fispm-c04-por-quuxe9-la-transformaciuxf3n-de-puntos-es-afuxedn-no-lineal}

Definamos la aplicación sobre columnas

$$\Phi_{F'\leftarrow F}(x) := S^{-1}(x-[a]_B).$$

Puede escribirse como

$$\boxed{ \Phi_{F'\leftarrow F}(x) = S^{-1}x - S^{-1}[a]_B. }$$

El primer término es lineal en $x$. El segundo es una traslación constante. Por tanto, si

$$a\ne0,$$

la transformación de coordenadas de puntos no es lineal: $\Phi_{F'\leftarrow F}(0) = -S^{-1}[a]_B \ne0.$ Es una transformación **afín**. Sólo cuando los dos marcos comparten el mismo origen, $a=0,$

[]{#fig:I-04-R04}

<figure id="fig-fpm-v04-i-04-r04" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-04-R04.svg" class="lightbox" data-gallery="fpm-v04-c04"><img src="/assets/books/fispm/v04/I-04-R04.svg" alt="Una traslación cambia la posición representada. Diagrama del capítulo 4; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="289" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 4.8.** Para orígenes separados por $a=\overrightarrow{OO^\prime}$ y bases iguales, los vectores de posición cumplen $r=a+r^\prime$. El punto físico y las diferencias entre puntos permanecen iguales. Véase §[12](#fispm-c04-cambios-de-origen-y-de-marco-geomuxe9trico).

</figcaption>

</figure>

la ley se reduce al cambio lineal de base: $x_{F'}(P)=S^{-1}x_F(P).$

[]{#proposición-los-desplazamientos-no-sienten-el-cambio-de-origen}

### Proposición: los desplazamientos no sienten el cambio de origen {#fispm-c04-proposiciuxf3n-los-desplazamientos-no-sienten-el-cambio-de-origen}

**Proposición 4.52 --- Transformación de un desplazamiento entre marcos** Para cualesquiera puntos $P,Q$,

$$\boxed{ [\overrightarrow{PQ}]_{B'} = S^{-1} [\overrightarrow{PQ}]_B. }$$

El término de traslación asociado al cambio de origen se cancela.

**Demostración.** Por proposición 4.9,

$$[\overrightarrow{PQ}]_B = x_F(Q)-x_F(P),$$

y

$$[\overrightarrow{PQ}]_{B'} = x_{F'}(Q)-x_{F'}(P).$$

Aplicamos proposición 4.51:

$$x_{F'}(Q) = S^{-1} \left( x_F(Q)-[a]_B \right),$$

$$x_{F'}(P) = S^{-1} \left( x_F(P)-[a]_B \right).$$

Restando,

$$\begin{aligned} x_{F'}(Q)-x_{F'}(P) &= S^{-1} \left( x_F(Q)-[a]_B \right)\\ &\quad- S^{-1} \left( x_F(P)-[a]_B \right)\\ &= S^{-1} \left( x_F(Q)-x_F(P) \right). \end{aligned}$$

Luego

$$[\overrightarrow{PQ}]_{B'} = S^{-1} [\overrightarrow{PQ}]_B.$$

$\square$

La traslación afecta las coordenadas absolutas de los puntos, pero no el desplazamiento entre ellos.

[]{#punto-y-vector-obedecen-leyes-distintas}

### Punto y vector obedecen leyes distintas {#fispm-c04-punto-y-vector-obedecen-leyes-distintas}

Para un **punto**:

$$\boxed{ x_{F'}(P) = S^{-1} \left( x_F(P)-[a]_B \right). }$$

Para un **vector** $v\in V$:

$$\boxed{ [v]_{B'} = S^{-1}[v]_B. }$$

La diferencia es exactamente el término

$$-S^{-1}[a]_B.$$

Ese término sólo aparece porque un punto no pertenece al espacio vectorial de desplazamientos. Esta es una de las razones fundamentales por las que §1 insistió en que

$$\boxed{ \text{un punto no es un vector}. }$$

[]{#dos-casos-límite-recuperan-resultados-anteriores}

### Dos casos límite recuperan resultados anteriores {#fispm-c04-dos-casos-luxedmite-recuperan-resultados-anteriores}

[]{#sólo-cambia-el-origen}

#### Sólo cambia el origen {#fispm-c04-suxf3lo-cambia-el-origen}

Si

$$B'=B,$$

entonces $S=I,$

y proposición 4.51 se reduce a

$$\boxed{ x_{F'}(P) = x_F(P)-[a]_B, }$$

que es exactamente proposición 4.10.

[]{#sólo-cambia-la-base}

#### Sólo cambia la base {#fispm-c04-suxf3lo-cambia-la-base}

Si

$$O'=O,$$

entonces $a=0,$

y proposición 4.51 se reduce a

$$\boxed{ x_{F'}(P) = S^{-1}x_F(P). }$$

Es la misma ley lineal que proposición 4.39 aplicada al vector de posición relativo al origen común. Así, proposición 4.51 contiene como casos particulares los dos cambios estudiados anteriormente.

[]{#ejemplo-diagnóstico-de-signo}

### Ejemplo diagnóstico de signo {#fispm-c04-ejemplo-diagnuxf3stico-de-signo}

Sea

$$B=(e_1,e_2,e_3),$$

y supongamos que el nuevo origen satisface $O'=O+2e_1.$

Entonces

$$[a]_B = \begin{pmatrix} 2\\ 0\\ 0 \end{pmatrix}.$$

Tomemos primero la misma base: $B'=B.$ Para un punto con

$$x_F(P) = \begin{pmatrix} 5\\ 1\\ 0 \end{pmatrix},$$

Proposición 4.51 da

$$x_{F'}(P) = \begin{pmatrix} 5\\ 1\\ 0 \end{pmatrix} - \begin{pmatrix} 2\\ 0\\ 0 \end{pmatrix} = \begin{pmatrix} 3\\ 1\\ 0 \end{pmatrix}.$$

El signo negativo es geométricamente inevitable: al mover el origen **hacia** el punto en la dirección $+e_1$, la primera coordenada del punto disminuye. Este control geométrico del signo debe hacerse antes de memorizar la fórmula.

[]{#principio-metodológico}

### Principio metodológico {#fispm-c04-principio-metodoluxf3gico}

**Principio metodológico 4.22 --- Separar la parte traslacional de la parte lineal** En un cambio completo de marco

$$F=(O,B) \longrightarrow F'=(O',B'),$$

identificar por separado:

1.  el desplazamiento del origen $$a=\overrightarrow{OO'};$$

2.  la matriz de cambio de base $$S_{B\leftarrow B'}.$$

Las coordenadas de puntos transforman afínmente, $x_{F'}=S^{-1}(x_F-[a]_B),$

mientras las componentes de vectores transforman linealmente, $[v]_{B'}=S^{-1}[v]_B.$

[]{#balance-ley-afín-y-separación-puntovector}

### Balance: ley afín y separación punto--vector {#fispm-c04-balance-ley-afuxedn-y-separaciuxf3n-puntovector}

Queda establecida la ley conjunta:

$$\boxed{ x_{F'}(P) = S^{-1} \left( x_F(P)-[a]_B \right). }$$

Su estructura contiene dos capas:

$$\boxed{ \text{traslación del origen} + \text{cambio lineal de base}. }$$

Y la diferencia entre puntos elimina automáticamente la parte traslacional:

$$\boxed{ [\overrightarrow{PQ}]_{B'} = S^{-1} [\overrightarrow{PQ}]_B. }$$

Todavía falta estudiar cómo se componen dos cambios completos de marco, cómo se invierte uno de ellos y cómo conviene empaquetarlos algebraicamente sin borrar la distinción entre puntos y vectores.

[]{#tres-marcos-y-dos-cambios-sucesivos}

### Tres marcos y dos cambios sucesivos {#fispm-c04-tres-marcos-y-dos-cambios-sucesivos}

Consideremos tres marcos afines:

$$F=(O,B), \qquad F'=(O',B'), \qquad F''=(O'',B'').$$

Para el primer cambio definimos

$$a:=\overrightarrow{OO'}, \qquad S:=S_{B\leftarrow B'}.$$

Para el segundo cambio definimos

$$b:=\overrightarrow{O'O''}, \qquad R:=S_{B'\leftarrow B''}.$$

Por proposición 4.51, $x_{F'}(P) = S^{-1} \left( x_F(P)-[a]_B \right),$

y después

$$x_{F''}(P) = R^{-1} \left( x_{F'}(P)-[b]_{B'} \right).$$

El objetivo es comparar esta ruta en dos etapas con el cambio directo

$$F\longrightarrow F''.$$

[]{#el-desplazamiento-total-de-los-orígenes}

### El desplazamiento total de los orígenes {#fispm-c04-el-desplazamiento-total-de-los-oruxedgenes}

La ley del triángulo afín da

$$\overrightarrow{OO''} = \overrightarrow{OO'} + \overrightarrow{O'O''}.$$

Definimos $c:=\overrightarrow{OO''}.$

Entonces

$$\boxed{ c=a+b. }$$

Como $a$ está expresado naturalmente en $B$ y $b$ puede venir expresado en $B'$, para sumar sus columnas debemos convertir primero: $[b]_B = S[b]_{B'}.$ Por tanto,

$$\boxed{ [c]_B = [a]_B + S[b]_{B'}. }$$

La suma geométrica de vectores es intrínseca; la suma de columnas sólo es legítima cuando ambas columnas están expresadas en la misma base.

[]{#proposición-composición-de-cambios-completos-de-marco}

### Proposición: composición de cambios completos de marco {#fispm-c04-proposiciuxf3n-composiciuxf3n-de-cambios-completos-de-marco}

**Proposición 4.53 --- Composición de cambios de marco afín** Con las definiciones anteriores,

$$S_{B\leftarrow B''} = SR$$

y

$$\boxed{ x_{F''}(P) = (SR)^{-1} \left( x_F(P)-[c]_B \right), }$$

donde

$$[c]_B = [a]_B+S[b]_{B'}.$$

**Demostración.** Sustituimos la primera transformación en la segunda:

$$\begin{aligned} x_{F''}(P) &= R^{-1} \left[ S^{-1} \left( x_F(P)-[a]_B \right) - [b]_{B'} \right]. \end{aligned}$$

Distribuimos:

$$x_{F''}(P) = R^{-1}S^{-1} \left( x_F(P)-[a]_B \right) - R^{-1}[b]_{B'}.$$

Como $R^{-1}S^{-1} = (SR)^{-1},$

podemos escribir el segundo término como $R^{-1}[b]_{B'} = (SR)^{-1}S[b]_{B'}.$ Por tanto,

$$x_{F''}(P) = (SR)^{-1} \left( x_F(P) - [a]_B - S[b]_{B'} \right).$$

Por §12.13, $[a]_B+S[b]_{B'} = [c]_B.$

Luego

$$x_{F''}(P) = (SR)^{-1} \left( x_F(P)-[c]_B \right).$$

Finalmente, proposición 4.41 da

$$S_{B\leftarrow B''} = S_{B\leftarrow B'} S_{B'\leftarrow B''} = SR.$$

$\square$

La forma de la ley se conserva bajo composición: un cambio de marco seguido de otro sigue siendo un cambio afín del mismo tipo.

[]{#definir-representación-afín-coordenada}

### Definir: representación afín coordenada {#fispm-c04-definir-representaciuxf3n-afuxedn-coordenada}

**Definición 4.37 --- Par afín asociado a un cambio de marco** Para

$$F=(O,B) \longrightarrow F'=(O',B'),$$

definimos $L:=S^{-1},$

y

$$t:=-S^{-1}[a]_B.$$

Entonces la transformación de coordenadas de puntos adopta la forma

$$\boxed{ \Phi_{F'\leftarrow F}(x) = Lx+t. }$$

El par

$$(L,t)$$

separa explícitamente:

- la parte lineal $L$;

- la parte traslacional $t$.

Esta notación no convierte los puntos en vectores: sólo representa la aplicación entre sus columnas de coordenadas.

[]{#proposición-ley-algebraica-de-composición-de-pares-afines}

### Proposición: ley algebraica de composición de pares afines {#fispm-c04-proposiciuxf3n-ley-algebraica-de-composiciuxf3n-de-pares-afines}

**Proposición 4.54 --- Composición de pares afines** Sean

$$\Phi_1(x)=L_1x+t_1$$

y

$$\Phi_2(x)=L_2x+t_2.$$

Entonces

$$\boxed{ (\Phi_2\circ\Phi_1)(x) = (L_2L_1)x + (L_2t_1+t_2). }$$

Por tanto, la composición de los pares es

$$\boxed{ (L_2,t_2)\circ(L_1,t_1) = (L_2L_1,\ L_2t_1+t_2). }$$

**Demostración.**

$$\begin{aligned} (\Phi_2\circ\Phi_1)(x) &= \Phi_2(L_1x+t_1)\\ &= L_2(L_1x+t_1)+t_2\\ &= L_2L_1x+L_2t_1+t_2. \end{aligned}$$

$\square$

Obsérvese que las traslaciones no se suman sin más: la primera debe ser transportada por la parte lineal del segundo cambio antes de combinarse.

[]{#proposición-cambio-inverso-de-marco}

### Proposición: cambio inverso de marco {#fispm-c04-proposiciuxf3n-cambio-inverso-de-marco}

**Proposición 4.55 --- Inversa de un cambio de marco afín** Si

$$\Phi(x) = Lx+t$$

con $L$ invertible, entonces

$$\boxed{ \Phi^{-1}(x') = L^{-1}x' - L^{-1}t. }$$

En términos de pares,

$$\boxed{ (L,t)^{-1} = \left( L^{-1}, -L^{-1}t \right). }$$

**Demostración.** De

$$x'=Lx+t$$

obtenemos $x'-t=Lx.$

Multiplicando por $L^{-1}$, $x = L^{-1}(x'-t) = L^{-1}x'-L^{-1}t.$

$\square$

Para el cambio de marco de la definición 4.36, $L=S^{-1}, \qquad t=-S^{-1}[a]_B.$

Así, $L^{-1}=S,$

y

$$-L^{-1}t = -S\left(-S^{-1}[a]_B\right) = [a]_B.$$

Por tanto, la transformación inversa es

$$\boxed{ x_F(P) = Sx_{F'}(P)+[a]_B. }$$

Esta fórmula es exactamente la resolución de la proposición 4.51 para $x_F(P)$.

[]{#interpretación-geométrica-del-cambio-inverso}

### Interpretación geométrica del cambio inverso {#fispm-c04-interpretaciuxf3n-geomuxe9trica-del-cambio-inverso}

Desde el marco nuevo hacia el antiguo, el desplazamiento del origen es $\overrightarrow{O'O} = -a.$ Su columna en la base nueva es $[-a]_{B'} = -S^{-1}[a]_B.$ Además, $S_{B'\leftarrow B} = S^{-1}.$ Aplicando proposición 4.51 en sentido inverso,

$$x_F(P) = \left(S^{-1}\right)^{-1} \left( x_{F'}(P)-[-a]_{B'} \right).$$

Por tanto,

$$x_F(P) = S \left( x_{F'}(P) + S^{-1}[a]_B \right) = Sx_{F'}(P)+[a]_B.$$

La fórmula algebraica de la proposición 4.55 coincide exactamente con la geometría del cambio de origen invertido.

[]{#ejemplo-de-consistencia-por-dos-caminos}

### Ejemplo de consistencia por dos caminos {#fispm-c04-ejemplo-de-consistencia-por-dos-caminos}

Tomemos

$$S= \begin{pmatrix} 1&0&0\\ 1&1&0\\ 0&0&1 \end{pmatrix},$$

$$R= \begin{pmatrix} 1&0&0\\ 0&1&0\\ 0&1&1 \end{pmatrix},$$

y

$$[a]_B = \begin{pmatrix} 1\\ 0\\ 0 \end{pmatrix}, \qquad [b]_{B'} = \begin{pmatrix} 0\\ 1\\ 0 \end{pmatrix}.$$

Entonces

$$S[b]_{B'} = \begin{pmatrix} 0\\ 1\\ 0 \end{pmatrix},$$

de modo que

$$[c]_B = \begin{pmatrix} 1\\ 1\\ 0 \end{pmatrix}.$$

Además,

$$SR = \begin{pmatrix} 1&0&0\\ 1&1&0\\ 0&1&1 \end{pmatrix}.$$

Sea un punto con

$$x_F(P) = \begin{pmatrix} 4\\ 3\\ 2 \end{pmatrix}.$$

[]{#ruta-en-dos-etapas}

#### Ruta en dos etapas {#fispm-c04-ruta-en-dos-etapas}

Primero,

$$x_{F'}(P) = S^{-1} \left( x_F(P)-[a]_B \right) = \begin{pmatrix} 3\\ 0\\ 2 \end{pmatrix}.$$

Después,

$$x_{F''}(P) = R^{-1} \left( x_{F'}(P)-[b]_{B'} \right) = \begin{pmatrix} 3\\ -1\\ 3 \end{pmatrix}.$$

[]{#ruta-directa}

#### Ruta directa {#fispm-c04-ruta-directa}

Proposición 4.53 da

$$x_{F''}(P) = (SR)^{-1} \left( x_F(P)-[c]_B \right),$$

y el resultado es nuevamente

$$\boxed{ x_{F''}(P) = \begin{pmatrix} 3\\ -1\\ 3 \end{pmatrix}. }$$

La coincidencia no es accidental: es la condición de consistencia del cambio de marcos.

[]{#principio-metodológico-de-tipado}

### Principio metodológico de tipado {#fispm-c04-principio-metodoluxf3gico-de-tipado}

**Principio metodológico 4.23 --- No sumar columnas escritas en bases distintas** Los vectores

$$a \qquad\text{y}\qquad b$$

pueden sumarse intrínsecamente en $V$. Sus columnas, en cambio, sólo pueden sumarse después de expresarlas en una base común: $[c]_B = [a]_B + S[b]_{B'}.$ La notación de bases funciona como un control de tipos: una suma de columnas con etiquetas incompatibles carece de interpretación geométrica hasta efectuar la conversión correspondiente.

Este principio evita uno de los errores más frecuentes al componer traslaciones y cambios de base.

[]{#balance-composición-inversa-y-tipado}

### Balance: composición, inversa y tipado {#fispm-c04-balance-composiciuxf3n-inversa-y-tipado}

Los cambios completos de marco quedan ahora cerrados algebraicamente bajo composición:

$$\boxed{ (L_2,t_2)\circ(L_1,t_1) = (L_2L_1,\ L_2t_1+t_2), }$$

y admiten inversa:

$$\boxed{ (L,t)^{-1} = (L^{-1},-L^{-1}t). }$$

En la notación geométrica de marcos,

$$\boxed{ S_{B\leftarrow B''} = S_{B\leftarrow B'} S_{B'\leftarrow B''}, }$$

y

$$\boxed{ [\overrightarrow{OO''}]_B = [\overrightarrow{OO'}]_B + S_{B\leftarrow B'} [\overrightarrow{O'O''}]_{B'}. }$$

La estructura afín conserva así dos capas inseparables pero distintas:

$$\boxed{ \text{parte lineal} + \text{parte traslacional}. }$$

Todavía falta ejercitar estas leyes y preparar la transición desde un marco geométrico puramente matemático hacia la noción física de marco de referencia.

[]{#proposición-marcos-ortonormales-y-conservación-de-distancias}

### Proposición: marcos ortonormales y conservación de distancias {#fispm-c04-proposiciuxf3n-marcos-ortonormales-y-conservaciuxf3n-de-distancias}

**Proposición 4.56 --- Invariancia métrica entre marcos ortonormales** Sean

$$F=(O,E), \qquad F'=(O',E')$$

dos marcos cuyas bases $E$ y $E'$ son ortonormales.

Entonces, para cualesquiera puntos $P,Q$,

$$\boxed{ \left\| x_{F'}(Q)-x_{F'}(P) \right\| = \left\| x_F(Q)-x_F(P) \right\|. }$$

**Demostración.** Por proposición 4.52,

$$x_{F'}(Q)-x_{F'}(P) = S^{-1} \left( x_F(Q)-x_F(P) \right),$$

donde

$$S=S_{E\leftarrow E'}.$$

Las columnas de

$$S=S_{E\leftarrow E'}$$

son $[e'_1]_E, \qquad [e'_2]_E, \qquad [e'_3]_E.$

Como $E$ y $E'$ son ortonormales, el producto escalar entre las columnas $i$ y $j$ es $\langle e'_i,e'_j\rangle = \delta_{ij}.$ Por tanto, $S^{\mathsf T}S=I.$ Así, $S^{-1}=S^{\mathsf T}$

y la matriz $S^{-1}$ conserva la norma euclídea de las columnas. Por tanto,

$$\left\| x_{F'}(Q)-x_{F'}(P) \right\| = \left\| x_F(Q)-x_F(P) \right\|.$$

$\square$

El cambio de origen modifica las coordenadas individuales de $P$ y $Q$, pero desaparece al formar su diferencia. El cambio ortogonal de base, por su parte, conserva la norma de esa diferencia.

[]{#cambio-de-descripción-no-significa-movimiento-del-punto}

### Cambio de descripción no significa movimiento del punto {#fispm-c04-cambio-de-descripciuxf3n-no-significa-movimiento-del-punto}

En toda esta sección hemos considerado un mismo punto geométrico $P$ descrito desde marcos distintos:

$$P \longmapsto x_F(P), \qquad P \longmapsto x_{F'}(P).$$

La relación $x_{F'}(P) = S^{-1} \left( x_F(P)-[a]_B \right)$

no mueve a $P$. Cambia únicamente su **descripción coordenada**. Esto debe distinguirse de una transformación afín activa

$$P\longmapsto A(P),$$

en la que el punto geométrico sí cambia.

**Principio metodológico 4.24 --- Separar cambio de marco de movimiento geométrico** Una fórmula afín de la forma

$$x'\!=Lx+t$$

no determina por sí sola si estamos ante:

- dos descripciones del mismo punto en marcos diferentes;

- o una transformación activa que envía un punto a otro.

Antes de interpretar la fórmula, declarar explícitamente qué permanece fijo: el punto o el marco. La distinción es la versión afín del principio activo/pasivo establecido en §10.

[]{#fispm-t1-c04-e0024}

**Ejercicio 4.24 --- Cambio simultáneo de origen y base.**

**Función pedagógica:** `Marco afín → Conversión de punto → Desplazamiento → Invariante métrico`

Sea

$$F=(O,E), \qquad E=(e_1,e_2,e_3)$$

un marco ortonormal positivo.

Definimos otro marco

$$F'=(O',E')$$

mediante $\overrightarrow{OO'} = e_1-2e_2+e_3$

y

$$E' = (e_2,-e_1,e_3).$$

Sean los puntos $P,Q$ con

$$x_F(P) = \begin{pmatrix} 4\\ 1\\ 3 \end{pmatrix}, \qquad x_F(Q) = \begin{pmatrix} 2\\ 5\\ 0 \end{pmatrix}.$$

1.  Calcula $S_{E\leftarrow E'}$.

2.  Calcula $x_{F'}(P)$ y $x_{F'}(Q)$.

3.  Calcula $[\overrightarrow{PQ}]_E$ y $[\overrightarrow{PQ}]_{E'}$.

4.  Verifica proposición 4.52.

5.  Verifica proposición 4.56.

**Solución desarrollada**

Las columnas de la base nueva escritas en la antigua son

$$[e'_1]_E = \begin{pmatrix} 0\\ 1\\ 0 \end{pmatrix}, \qquad [e'_2]_E = \begin{pmatrix} -1\\ 0\\ 0 \end{pmatrix}, \qquad [e'_3]_E = \begin{pmatrix} 0\\ 0\\ 1 \end{pmatrix}.$$

Por tanto,

$$S = \begin{pmatrix} 0&-1&0\\ 1&0&0\\ 0&0&1 \end{pmatrix}.$$

Como $S$ es ortogonal,

$$S^{-1} = S^{\mathsf T} = \begin{pmatrix} 0&1&0\\ -1&0&0\\ 0&0&1 \end{pmatrix}.$$

Además,

$$[a]_E = \begin{pmatrix} 1\\ -2\\ 1 \end{pmatrix}.$$

Para $P$,

$$x_F(P)-[a]_E = \begin{pmatrix} 3\\ 3\\ 2 \end{pmatrix},$$

y

$$\boxed{ x_{F'}(P) = \begin{pmatrix} 3\\ -3\\ 2 \end{pmatrix}. }$$

Para $Q$,

$$x_F(Q)-[a]_E = \begin{pmatrix} 1\\ 7\\ -1 \end{pmatrix},$$

y

$$\boxed{ x_{F'}(Q) = \begin{pmatrix} 7\\ -1\\ -1 \end{pmatrix}. }$$

En el marco antiguo,

$$[\overrightarrow{PQ}]_E = x_F(Q)-x_F(P) = \begin{pmatrix} -2\\ 4\\ -3 \end{pmatrix}.$$

En el nuevo,

$$[\overrightarrow{PQ}]_{E'} = x_{F'}(Q)-x_{F'}(P) = \begin{pmatrix} 4\\ 2\\ -3 \end{pmatrix}.$$

Y, efectivamente,

$$S^{-1} \begin{pmatrix} -2\\ 4\\ -3 \end{pmatrix} = \begin{pmatrix} 4\\ 2\\ -3 \end{pmatrix}.$$

Finalmente,

$$\|[\overrightarrow{PQ}]_E\|^2 = (-2)^2+4^2+(-3)^2 = 29,$$

mientras

$$\|[\overrightarrow{PQ}]_{E'}\|^2 = 4^2+2^2+(-3)^2 = 29.$$

La descripción cambia; la distancia geométrica no.

[]{#fispm-t1-c04-e0025}

**Ejercicio 4.25 --- Composición e inversa de pares afines.**

**Función pedagógica:** `Composición afín → Verificación por dos rutas → Inversa`

Considera dos transformaciones de coordenadas

$$\Phi_1(x)=L_1x+t_1,$$

$$\Phi_2(x)=L_2x+t_2,$$

con

$$L_1 = \begin{pmatrix} 0&1&0\\ -1&0&0\\ 0&0&1 \end{pmatrix}, \qquad t_1 = \begin{pmatrix} -2\\ 1\\ 0 \end{pmatrix},$$

y

$$L_2 = \begin{pmatrix} 1&0&0\\ 0&-1&0\\ 0&0&1 \end{pmatrix}, \qquad t_2 = \begin{pmatrix} 0\\ 3\\ -1 \end{pmatrix}.$$

1.  Calcula el par afín de $\Phi_2\circ\Phi_1$.

2.  Evalúa las dos transformaciones sucesivamente sobre

$$x= \begin{pmatrix} 4\\ 2\\ 5 \end{pmatrix}.$$

1.  Verifica que el cambio compuesto da el mismo resultado.

2.  Calcula la inversa del cambio compuesto.

3.  Usa esa inversa para recuperar la columna inicial.

**Solución desarrollada**

La parte lineal compuesta es

$$L = L_2L_1 = \begin{pmatrix} 0&1&0\\ 1&0&0\\ 0&0&1 \end{pmatrix}.$$

La parte traslacional es

$$\begin{aligned} t &= L_2t_1+t_2\\ &= \begin{pmatrix} -2\\ -1\\ 0 \end{pmatrix} + \begin{pmatrix} 0\\ 3\\ -1 \end{pmatrix}\\ &= \begin{pmatrix} -2\\ 2\\ -1 \end{pmatrix}. \end{aligned}$$

Por tanto,

$$\boxed{ (\Phi_2\circ\Phi_1)(x) = Lx+t. }$$

Aplicando primero $\Phi_1$,

$$\Phi_1(x) = \begin{pmatrix} 0\\ -3\\ 5 \end{pmatrix}.$$

Después,

$$\Phi_2(\Phi_1(x)) = \boxed{ \begin{pmatrix} 0\\ 6\\ 4 \end{pmatrix} }.$$

Por la ruta directa,

$$Lx+t = \begin{pmatrix} 2\\ 4\\ 5 \end{pmatrix} + \begin{pmatrix} -2\\ 2\\ -1 \end{pmatrix} = \begin{pmatrix} 0\\ 6\\ 4 \end{pmatrix}.$$

Como $L^{-1}=L,$

Proposición 4.55 da $(\Phi_2\circ\Phi_1)^{-1}(x') = Lx'-Lt.$

Tenemos

$$-Lt = \begin{pmatrix} -2\\ 2\\ 1 \end{pmatrix}.$$

Así,

$$\boxed{ (\Phi_2\circ\Phi_1)^{-1}(x') = Lx' + \begin{pmatrix} -2\\ 2\\ 1 \end{pmatrix}. }$$

Aplicando esta fórmula a

$$x' = \begin{pmatrix} 0\\ 6\\ 4 \end{pmatrix},$$

obtenemos

$$Lx' = \begin{pmatrix} 6\\ 0\\ 4 \end{pmatrix},$$

y finalmente

$$\boxed{ x = \begin{pmatrix} 4\\ 2\\ 5 \end{pmatrix}. }$$

[]{#síntesis-geométrica}

### Síntesis geométrica {#fispm-c04-suxedntesis-geomuxe9trica}

Un marco afín

$$F=(O,B)$$

contiene dos elecciones conceptualmente distintas:

$$\boxed{ \text{un origen }O \quad+\quad \text{una base }B. }$$

Cambiar el origen produce una traslación de las coordenadas de puntos. Cambiar la base produce una transformación lineal de componentes. Cambiar ambas cosas produce una ley afín:

$$\boxed{ x_{F'}(P) = S^{-1} \left( x_F(P)-[a]_B \right). }$$

Para los desplazamientos, la parte traslacional desaparece:

$$\boxed{ [\overrightarrow{PQ}]_{B'} = S^{-1} [\overrightarrow{PQ}]_B. }$$

Por eso un punto y un vector no pueden obedecer exactamente la misma ley de transformación.

[]{#del-marco-geométrico-al-marco-físico}

### Del marco geométrico al marco físico {#fispm-c04-del-marco-geomuxe9trico-al-marco-fuxedsico}

Nada de lo desarrollado en §12 introduce todavía:

- un reloj;

- una variable temporal;

- un observador;

- una trayectoria;

- una velocidad;

- una aceleración;

- una hipótesis de inercialidad.

Un marco afín geométrico especifica únicamente **cómo localizar espacialmente puntos y expresar desplazamientos**. La física exige estructura adicional. Esta frontera es decisiva:

$$\boxed{ \text{marco geométrico} \ne \text{marco físico de referencia}. }$$

La próxima sección incorporará exactamente esa capa conceptual, sin adelantar todavía la dinámica newtoniana.

[]{#cierre-de-12}

### Cierre de §12 {#fispm-c04-cierre-de-12}

La sección ha unificado todos los cambios geométricos de descripción construidos desde §1. Para dos marcos

$$F=(O,B), \qquad F'=(O',B'),$$

con

$$a=\overrightarrow{OO'}, \qquad S=S_{B\leftarrow B'},$$

la ley fundamental es

$$\boxed{ x_{F'}(P) = S^{-1} \left( x_F(P)-[a]_B \right). }$$

Su forma coordenada equivalente es

$$\boxed{ \Phi(x)=Lx+t. }$$

La composición satisface

$$\boxed{ (L_2,t_2)\circ(L_1,t_1) = (L_2L_1,\ L_2t_1+t_2), }$$

y la inversa,

$$\boxed{ (L,t)^{-1} = (L^{-1},-L^{-1}t). }$$

La parte traslacional sólo afecta coordenadas de puntos; las diferencias entre puntos y los vectores de desplazamiento transforman linealmente. Los ejercicios 4.24--4.25 aplican estas leyes antes de pasar de la geometría del marco a su realización física. El siguiente paso será el §[13](#fispm-c04-del-sistema-de-coordenadas-al-marco-fuxedsico-de-referencia).

[]{#del-sistema-de-coordenadas-al-marco-físico-de-referencia}

[]{#fispm-t1-c04-s13}

[]{#fpm-i-04-s13}

## 13. Del sistema de coordenadas al marco físico de referencia {#fispm-c04-del-sistema-de-coordenadas-al-marco-fuxedsico-de-referencia}

[]{#un-sistema-de-coordenadas-no-basta}

### Un sistema de coordenadas no basta {#fispm-c04-un-sistema-de-coordenadas-no-basta}

Un marco geométrico

$$F=(O,B)$$

permite asignar a cada punto $P$ una columna

$$x_F(P).$$

Esa construcción responde a una pregunta matemática:

$$\boxed{ \text{¿cómo describimos un punto mediante números una vez elegidos origen y base?} }$$

Pero un experimento físico exige algo más. Para localizar de manera reproducible una ocurrencia física necesitamos saber, al menos:

- dónde está materializado el origen;

- cómo se realizan las direcciones de referencia;

- qué patrón convierte longitudes en valores medidos;

- qué procedimiento asigna una lectura temporal.

Por tanto,

$$\boxed{ \text{sistema geométrico de coordenadas} \ne \text{marco físico de referencia}. }$$

[]{#de-una-elección-matemática-a-un-procedimiento-de-medición}

### De una elección matemática a un procedimiento de medición {#fispm-c04-de-una-elecciuxf3n-matemuxe1tica-a-un-procedimiento-de-mediciuxf3n}

En geometría podemos elegir formalmente un punto

$$O\in\mathcal E$$

y una base

$$B=(e_1,e_2,e_3)$$

sin preguntar cómo se construirían físicamente. En una situación experimental, en cambio, palabras como "origen", "eje $x$" o "un metro" deben corresponder a procedimientos reproducibles. La referencia física requiere entonces dos capas:

$$\boxed{ \text{estructura geométrica} + \text{realización operacional}. }$$

La primera indica qué objetos matemáticos usamos. La segunda indica cómo se vinculan esos objetos con marcas, instrumentos y lecturas físicas.

[]{#definir-marco-físico-de-referencia-en-sentido-mínimo}

### Definir: marco físico de referencia en sentido mínimo {#fispm-c04-definir-marco-fuxedsico-de-referencia-en-sentido-muxednimo}

**Definición 4.38 --- Marco físico de referencia, nivel operacional mínimo** En el nivel de este capítulo, un **marco físico de referencia** es una realización operacional

$$\boxed{ \mathfrak R=(F,\mathcal L,\mathcal T,\mathcal O), }$$

donde:

1.  $F=(O,B)$ es un marco espacial afín;

2.  $\mathcal L$ es un convenio de **calibración de longitudes**, que fija cómo las longitudes geométricas se expresan mediante una unidad física;

3.  $\mathcal T$ es un convenio de **lectura temporal**, que asigna una lectura escalar $t$ mediante un reloj o procedimiento equivalente;

4.  $\mathcal O$ representa la **realización física reproducible** del origen, las direcciones de referencia y los instrumentos asociados.[^6]

Esta definición es deliberadamente mínima. No afirma que el marco sea inercial. No afirma que el origen esté en reposo respecto de otro marco. No introduce todavía una ley de movimiento.

[]{#el-origen-y-los-ejes-deben-estar-físicamente-realizables}

### El origen y los ejes deben estar físicamente realizables {#fispm-c04-el-origen-y-los-ejes-deben-estar-fuxedsicamente-realizables}

En un dibujo podemos señalar arbitrariamente un punto como origen. En un laboratorio necesitamos una referencia reproducible que permita reconocer qué ubicación corresponde a

$$O.$$

Del mismo modo, las direcciones de la base

$$B=(e_1,e_2,e_3)$$

deben estar asociadas a direcciones físicamente identificables. Esto no significa que los vectores de base sean objetos materiales. Significa que existe un procedimiento para reproducir las direcciones que esos vectores representan. En un marco cartesiano físico se escogerá típicamente una base ortonormal

$$E=(e_1,e_2,e_3),$$

porque entonces las componentes corresponden directamente a proyecciones métricas sobre ejes mutuamente perpendiculares.

[]{#el-patrón-de-longitud-pertenece-al-procedimiento-físico}

### El patrón de longitud pertenece al procedimiento físico {#fispm-c04-el-patruxf3n-de-longitud-pertenece-al-procedimiento-fuxedsico}

La geometría euclídea determina una longitud abstracta

$$\|v\|.$$

Una medición física exige además declarar una unidad. El convenio

$$\mathcal L$$

vincula la longitud geométrica con un valor numérico expresado, por ejemplo, en metros, centímetros u otra unidad convenida. Cambiar la unidad no cambia el vector geométrico ni el punto. Sólo cambia el número utilizado para comunicar la misma magnitud física. Por tanto debemos separar:

$$\boxed{ \text{cambio de unidad} \ne \text{cambio de origen} \ne \text{cambio de base}. }$$

Estas tres operaciones modifican descripciones numéricas por razones conceptualmente diferentes.

[]{#el-convenio-temporal-una-lectura-todavía-no-una-cinemática}

### El convenio temporal: una lectura, todavía no una cinemática {#fispm-c04-el-convenio-temporal-una-lectura-todavuxeda-no-una-cinemuxe1tica}

Para distinguir mediciones realizadas en ocasiones diferentes necesitamos una etiqueta temporal. En este capítulo representaremos esa lectura simplemente por $t\in\mathbb R.$

El símbolo $t$ significa aquí únicamente:

$$\boxed{ \text{lectura asignada por el convenio temporal }\mathcal T. }$$

No suponemos todavía una trayectoria

$$P(t),$$

ni definimos expresiones como $\frac{dP}{dt}.$ Tampoco introducimos velocidad o aceleración. Esas estructuras pertenecen al desarrollo posterior sobre tiempo y movimiento.

[]{#definir-registro-físico-de-localización}

### Definir: registro físico de localización {#fispm-c04-definir-registro-fuxedsico-de-localizaciuxf3n}

**Definición 4.39 --- Registro de localización en un marco físico** Dada una ocurrencia física localizada espacialmente en un punto $P$ y una lectura temporal $t$, su registro en el marco

$$\mathfrak R=(F,\mathcal L,\mathcal T,\mathcal O)$$

es el par

$$\boxed{ \mathcal R_{\mathfrak R}(P,t) := \left( t,\, x_F(P) \right), }$$

acompañado de las unidades determinadas por $\mathcal L$.

Este par es un **registro de medición**. No estamos construyendo todavía un espacio-tiempo ni identificando una ocurrencia física con un vector de dimensión cuatro. La notación sólo conserva juntas dos informaciones:

- una lectura temporal;

- una localización espacial.

[]{#proposición-cambio-espacial-bajo-un-convenio-temporal-común}

### Proposición: cambio espacial bajo un convenio temporal común {#fispm-c04-proposiciuxf3n-cambio-espacial-bajo-un-convenio-temporal-comuxfan}

**Proposición 4.57 --- Registro de una misma ocurrencia en dos marcos con tiempo común** Sean dos marcos físicos

$$\mathfrak R=(F,\mathcal L,\mathcal T,\mathcal O), \qquad \mathfrak R'=(F',\mathcal L,\mathcal T,\mathcal O'),$$

que utilizan el mismo convenio temporal y la misma calibración de longitud.

Si

$$F=(O,B), \qquad F'=(O',B'),$$

con

$$a=\overrightarrow{OO'}, \qquad S=S_{B\leftarrow B'},$$

entonces una misma ocurrencia registrada como $\left( t,\, x_F(P) \right)$

en $\mathfrak R$ se registra en $\mathfrak R'$ como

$$\boxed{ \left( t,\, S^{-1} \left( x_F(P)-[a]_B \right) \right). }$$

**Demostración.** Por hipótesis, ambos marcos asignan la misma lectura temporal

$$t.$$

La parte espacial obedece exactamente a proposición 4.51: $x_{F'}(P) = S^{-1} \left( x_F(P)-[a]_B \right).$ Por tanto,

$$\mathcal R_{\mathfrak R'}(P,t) = \left( t,\, S^{-1} \left( x_F(P)-[a]_B \right) \right).$$

$\square$

El resultado no contiene ninguna afirmación sobre movimiento relativo: sólo compara dos procedimientos de descripción espacial que comparten la misma lectura temporal.

[]{#tres-niveles-que-no-deben-confundirse}

### Tres niveles que no deben confundirse {#fispm-c04-tres-niveles-que-no-deben-confundirse}

Conviene distinguir explícitamente:

[]{#nivel-1-geometría}

#### Nivel 1 --- Geometría {#fispm-c04-nivel-1-geometruxeda}

$$F=(O,B).$$

Es una elección matemática de origen y base.

[]{#nivel-2-medición-espacial}

#### Nivel 2 --- Medición espacial {#fispm-c04-nivel-2-mediciuxf3n-espacial}

$$(F,\mathcal L,\mathcal O).$$

El origen, los ejes y la unidad de longitud tienen una realización operacional.

[]{#nivel-3-marco-físico-mínimo}

#### Nivel 3 --- Marco físico mínimo {#fispm-c04-nivel-3-marco-fuxedsico-muxednimo}

$$\mathfrak R=(F,\mathcal L,\mathcal T,\mathcal O).$$

Además de localizar espacialmente, el procedimiento asigna una lectura temporal. Cada nivel añade estructura. No es correcto atribuir al nivel anterior propiedades que sólo aparecen después.

[]{#no-ejemplos}

### No-ejemplos {#fispm-c04-no-ejemplos}

**Un dibujo con ejes no constituye por sí solo un marco físico** Dibujar tres ejes y escribir coordenadas produce una representación geométrica, pero no especifica cómo se materializan el origen, las direcciones, la unidad ni la lectura temporal.

**Elegir metros no convierte un sistema de coordenadas en un marco físico completo** Una unidad de longitud aporta calibración espacial, pero todavía falta un procedimiento temporal y una realización física de las referencias.

**Un marco físico no es automáticamente un marco inercial** La inercialidad es una propiedad ligada a las leyes de la dinámica. No puede deducirse de la ortogonalidad de los ejes, de la elección del origen ni de la existencia de un reloj.[^7]

Este último error es especialmente importante:

$$\boxed{ \text{sistema cartesiano} \not\Rightarrow \text{marco inercial}. }$$

[]{#principio-metodológico-1}

### Principio metodológico {#fispm-c04-principio-metodoluxf3gico-1}

**Principio metodológico 4.25 --- Declarar la realización física antes de interpretar coordenadas** Cuando una terna de coordenadas se use en física, identificar explícitamente:

1.  qué punto realiza el origen;

2.  qué direcciones realizan los ejes;

3.  qué unidad calibra las longitudes;

4.  qué procedimiento asigna la lectura temporal.

Sólo después interpretar una columna como resultado de una localización física. La matemática de coordenadas no sustituye la especificación del procedimiento de medición.

[]{#balance-del-marco-geométrico-a-la-realización-operacional}

### Balance: del marco geométrico a la realización operacional {#fispm-c04-balance-del-marco-geomuxe9trico-a-la-realizaciuxf3n-operacional}

Queda establecida la diferencia fundamental:

$$\boxed{ F=(O,B) }$$

es un marco geométrico, mientras

$$\boxed{ \mathfrak R=(F,\mathcal L,\mathcal T,\mathcal O) }$$

añade la estructura operacional necesaria para hablar de una referencia física. El registro mínimo de una localización es

$$\boxed{ \mathcal R_{\mathfrak R}(P,t) = \left( t,\, x_F(P) \right). }$$

Si dos marcos comparten calibración y convenio temporal, la lectura $t$ permanece igual y sólo cambia la descripción espacial según la ley afín de §12. Todavía falta precisar qué significa comparar observaciones realizadas desde marcos físicos distintos y por qué ninguna de estas estructuras permite decidir, por sí sola, si un marco es inercial.

[]{#definir-observador-asociado-a-un-marco}

### Definir: observador asociado a un marco {#fispm-c04-definir-observador-asociado-a-un-marco}

**Definición 4.40 --- Observador asociado a un marco físico** En el nivel de este capítulo, un **observador asociado a**

$$\mathfrak R=(F,\mathcal L,\mathcal T,\mathcal O)$$

es el sistema operacional capaz de aplicar de manera reproducible los convenios de $\mathfrak R$ y producir registros

$$\mathcal R_{\mathfrak R}(P,t).$$

La palabra "observador" no designa necesariamente una persona. Puede representar un conjunto de instrumentos, marcas, reglas de calibración y procedimientos de lectura. Tampoco identificaremos al observador con el origen $O$. El origen es un elemento geométrico del marco espacial; el observador es quien ---o aquello que--- realiza el procedimiento completo de referencia.

[]{#una-misma-ocurrencia-puede-tener-registros-numéricos-distintos}

### Una misma ocurrencia puede tener registros numéricos distintos {#fispm-c04-una-misma-ocurrencia-puede-tener-registros-numuxe9ricos-distintos}

Supongamos que dos observadores usan marcos

$$\mathfrak R$$

y

$$\mathfrak R'$$

que comparten el convenio temporal y la calibración de longitud. La misma ocurrencia física localizada en $P$ con lectura $t$ puede producir:

$$\mathcal R_{\mathfrak R}(P,t) = \left( t,\, x_F(P) \right),$$

y

$$\mathcal R_{\mathfrak R'}(P,t) = \left( t,\, x_{F'}(P) \right).$$

En general, $x_F(P) \ne x_{F'}(P).$ Eso no significa que los observadores estén describiendo dos puntos distintos. Significa que el mismo punto recibe etiquetas espaciales diferentes porque cambió el marco utilizado para localizarlo.

[]{#proposición-acuerdo-métrico-entre-observadores-ortonormales}

### Proposición: acuerdo métrico entre observadores ortonormales {#fispm-c04-proposiciuxf3n-acuerdo-muxe9trico-entre-observadores-ortonormales}

**Proposición 4.58 --- Invariancia de la separación espacial registrada** Sean dos observadores asociados a marcos físicos

$$\mathfrak R=(F,\mathcal L,\mathcal T,\mathcal O), \qquad \mathfrak R'=(F',\mathcal L,\mathcal T,\mathcal O'),$$

con la misma calibración de longitud y el mismo convenio temporal.

Supongamos que

$$F=(O,E), \qquad F'=(O',E')$$

utilizan bases ortonormales. Si dos ocurrencias espaciales $P$ y $Q$ reciben la misma lectura temporal $t$, entonces

$$\boxed{ \left\| x_{F'}(Q)-x_{F'}(P) \right\| = \left\| x_F(Q)-x_F(P) \right\|. }$$

**Demostración.** La hipótesis temporal sólo asegura que estamos comparando los dos registros bajo el mismo convenio de lectura. La parte espacial es exactamente proposición 4.56:

$$\left\| x_{F'}(Q)-x_{F'}(P) \right\| = \left\| x_F(Q)-x_F(P) \right\|.$$

Como ambos observadores comparten además la calibración $\mathcal L$, ambas normas representan la misma longitud física expresada en la misma unidad. $\square$ Por tanto, dos observadores pueden discrepar en las columnas de coordenadas y, sin embargo, coincidir en una magnitud geométrica medible.

[]{#desacuerdo-de-coordenadas-no-es-desacuerdo-físico}

### Desacuerdo de coordenadas no es desacuerdo físico {#fispm-c04-desacuerdo-de-coordenadas-no-es-desacuerdo-fuxedsico}

Consideremos, por ejemplo,

$$x_F(P) = \begin{pmatrix} 4\\ 1\\ 0 \end{pmatrix},$$

mientras otro marco asigna

$$x_{F'}(P) = \begin{pmatrix} -1\\ 3\\ 0 \end{pmatrix}.$$

Las columnas son distintas. Sin información adicional, no podemos concluir que se trate de puntos distintos. Debemos preguntar primero cuál es la transformación de marco que relaciona ambas descripciones. La comparación físicamente significativa exige reconstruir los objetos geométricos o sus invariantes, no comparar números aislados.

[]{#el-observador-no-tiene-por-qué-estar-sentado-en-el-origen}

### El observador no tiene por qué estar "sentado en el origen" {#fispm-c04-el-observador-no-tiene-por-quuxe9-estar-sentado-en-el-origen}

En ejemplos elementales se dibuja con frecuencia una persona junto al origen de coordenadas. Ese dibujo puede ser útil, pero no constituye una definición. El marco puede estar realizado mediante una red de marcas y dispositivos distribuidos. Lo esencial es que exista un procedimiento reproducible para producir

$$\left( t,\, x_F(P) \right).$$

Por eso distinguimos:

$$\boxed{ \text{observador} \ne \text{origen geométrico}. }$$

El origen forma parte de la descripción espacial; el observador implementa el sistema de referencia completo.

[]{#todavía-no-hemos-definido-un-marco-en-movimiento}

### Todavía no hemos definido un marco "en movimiento" {#fispm-c04-todavuxeda-no-hemos-definido-un-marco-en-movimiento}

Para afirmar que un marco cambia respecto de otro a medida que transcurre el tiempo necesitaríamos permitir que sus datos espaciales dependieran de la lectura temporal. Por ejemplo, aparecerían objetos del tipo

$$O(t)$$

o

$$B(t).$$

Pero introducir esas dependencias equivaldría a comenzar el estudio del movimiento. En este capítulo no lo haremos. Los cambios de marco tratados hasta ahora relacionan descripciones geométricas ya dadas; no constituyen todavía una teoría de marcos móviles.

[]{#por-qué-la-inercialidad-no-puede-leerse-de-la-geometría}

### Por qué la inercialidad no puede leerse de la geometría {#fispm-c04-por-quuxe9-la-inercialidad-no-puede-leerse-de-la-geometruxeda}

Un marco puede poseer:

- origen bien definido;

- ejes ortonormales;

- patrón de longitud;

- reloj;

- procedimiento reproducible de localización.

Nada de eso decide por sí solo si el marco es **inercial**. La palabra "inercial" exige comparar la descripción del movimiento con leyes dinámicas que todavía no se han introducido. Por tanto, en este punto sólo podemos afirmar:

$$\boxed{ \text{marco físico bien definido} \not\Rightarrow \text{marco inercial}. }$$

La ortogonalidad de los ejes es una propiedad geométrica. La inercialidad es una propiedad físico-dinámica. Confundirlas mezcla niveles de estructura diferentes.

[]{#falsos-criterios-de-inercialidad}

### Falsos criterios de inercialidad {#fispm-c04-falsos-criterios-de-inercialidad}

**"Los ejes son cartesianos, por tanto el marco es inercial."**

Falso. La geometría cartesiana no determina las leyes del movimiento observadas desde ese marco.

**"El origen está materializado por un objeto físico, por tanto el marco es inercial."**

Falso. Tener un origen realizable no especifica cómo se comporta ese origen en el tiempo.

**"Hay un reloj, por tanto podemos decidir si el marco es inercial."**

Falso. Un reloj permite asignar lecturas temporales; la inercialidad requiere estructura dinámica adicional.

[]{#principio-metodológico-2}

### Principio metodológico {#fispm-c04-principio-metodoluxf3gico-2}

**Principio metodológico 4.26 --- Separar diferencias de descripción de diferencias físicas** Cuando dos observadores asignen registros distintos a una misma situación:

1.  identificar primero sus marcos geométricos;

2.  comprobar sus convenios de unidades y lectura temporal;

3.  transformar las coordenadas a una descripción común;

4.  comparar después los invariantes o magnitudes físicas pertinentes.

No interpretar una diferencia entre columnas numéricas como una diferencia física antes de controlar el marco y las convenciones.

[]{#balance-observador-registro-e-inercialidad}

### Balance: observador, registro e inercialidad {#fispm-c04-balance-observador-registro-e-inercialidad}

Un observador queda entendido aquí como la realización operacional de un marco físico, no como un punto geométrico ni necesariamente como una persona. Dos observadores pueden asignar coordenadas diferentes a una misma ocurrencia:

$$\boxed{ x_F(P)\ne x_{F'}(P) }$$

sin discrepar sobre invariantes geométricos como una separación espacial, siempre que sus calibraciones sean compatibles. Además,

$$\boxed{ \text{observador} \ne \text{origen} }$$

y

$$\boxed{ \text{marco físico} \not\Rightarrow \text{marco inercial}. }$$

Todavía falta ejercitar estas distinciones y cerrar la sección sin invadir el estudio del movimiento.

[]{#qué-puede-inferirse-de-un-registro-y-qué-no}

### Qué puede inferirse de un registro y qué no {#fispm-c04-quuxe9-puede-inferirse-de-un-registro-y-quuxe9-no}

Un registro

$$\left( t,\, x_F(P) \right)$$

permite afirmar que, bajo los convenios del marco utilizado:

- se asignó la lectura temporal $t$;

- la localización espacial recibió la columna $x_F(P)$;

- las unidades están determinadas por la calibración declarada.

Pero ese registro, por sí solo, no permite concluir:

- que el punto esté moviéndose o en reposo;

- que el marco se mueva respecto de otro;

- que el marco sea inercial;

- que exista una velocidad;

- que exista una aceleración.

Todas esas afirmaciones requieren estructura adicional.

[]{#principio-metodológico-de-nivel-de-estructura}

### Principio metodológico de nivel de estructura {#fispm-c04-principio-metodoluxf3gico-de-nivel-de-estructura}

**Principio metodológico 4.27 --- Declarar el nivel de estructura antes de inferir física** Antes de extraer una conclusión, identificar qué estructura está realmente disponible:

1.  **coordenadas geométricas:** origen y base;

2.  **marco físico mínimo:** geometría + calibración + lectura temporal + realización operacional;

3.  **cinemática:** dependencia temporal de posiciones;

4.  **dinámica:** leyes que relacionan movimiento e interacciones.

No atribuir a un nivel propiedades que requieren uno posterior. En particular,

$$\boxed{ \text{tener }(t,x_F(P)) \not\Rightarrow \text{tener una ley de movimiento}. }$$

[]{#fispm-t1-c04-e0026}

**Ejercicio 4.26 --- ¿Qué estructura está realmente dada?.**

**Función pedagógica:** `Diagnóstico conceptual → Jerarquía de estructura → Control de inferencias`

Para cada afirmación, indica qué puede concluirse y qué no.

**Caso A.** Se da un origen $O$ y una base ortonormal $E$.

**Caso B.** Además se especifica una unidad de longitud y un reloj.

**Caso C.** Además existe un procedimiento reproducible que materializa el origen, los ejes y las lecturas.

**Caso D.** Se afirma que, como los ejes son ortonormales, el marco es inercial.

**Solución desarrollada**

**Caso A.** Tenemos un marco geométrico

$$F=(O,E).$$

Podemos asignar coordenadas espaciales a puntos. No tenemos todavía un marco físico completo.

**Caso B.** Ahora existen una calibración de longitud y una lectura temporal, pero falta especificar cómo se realizan físicamente el origen y las direcciones. La estructura operacional sigue incompleta.

**Caso C.** Ya disponemos del nivel mínimo de marco físico:

$$\mathfrak R=(F,\mathcal L,\mathcal T,\mathcal O).$$

Podemos producir registros

$$\left( t,\, x_F(P) \right).$$

Sin embargo, aún no hemos definido trayectorias, velocidades, aceleraciones ni inercialidad.

**Caso D.** La inferencia es inválida.

$$\boxed{ E\text{ ortonormal} \not\Rightarrow \mathfrak R\text{ inercial}. }$$

La ortonormalidad pertenece a la geometría; la inercialidad requiere dinámica.

[]{#fispm-t1-c04-e0027}

**Ejercicio 4.27 --- Dos observadores, una misma geometría.**

**Función pedagógica:** `Cambio de marco → Registros distintos → Invariante común`

Dos observadores comparten la misma calibración de longitud y el mismo convenio temporal. El primero usa

$$F=(O,E), \qquad E=(e_1,e_2,e_3).$$

El segundo usa

$$F'=(O',E'),$$

con

$$\overrightarrow{OO'} = e_1-2e_2+e_3$$

y

$$E' = (e_2,-e_1,e_3).$$

A la lectura

$$t=12\,\mathrm{s},$$

se registran dos localizaciones $P$ y $Q$:

$$x_F(P) = \begin{pmatrix} 5\\ 0\\ 2 \end{pmatrix} \mathrm{m}, \qquad x_F(Q) = \begin{pmatrix} 2\\ 4\\ 2 \end{pmatrix} \mathrm{m}.$$

1.  Calcula los registros espaciales de $P$ y $Q$ en $F'$.

2.  Comprueba que las columnas cambian.

3.  Calcula la separación espacial en ambos marcos.

4.  Explica qué puede concluirse y qué no puede concluirse sobre el movimiento.

**Solución desarrollada**

La matriz de cambio es

$$S_{E\leftarrow E'} = \begin{pmatrix} 0&-1&0\\ 1&0&0\\ 0&0&1 \end{pmatrix},$$

por lo que

$$S^{-1} = \begin{pmatrix} 0&1&0\\ -1&0&0\\ 0&0&1 \end{pmatrix}.$$

Además,

$$[a]_E = \begin{pmatrix} 1\\ -2\\ 1 \end{pmatrix} \mathrm{m}.$$

Para $P$:

$$x_F(P)-[a]_E = \begin{pmatrix} 4\\ 2\\ 1 \end{pmatrix} \mathrm{m},$$

y por la proposición 4.57,

$$\boxed{ x_{F'}(P) = \begin{pmatrix} 2\\ -4\\ 1 \end{pmatrix} \mathrm{m}. }$$

Para $Q$:

$$x_F(Q)-[a]_E = \begin{pmatrix} 1\\ 6\\ 1 \end{pmatrix} \mathrm{m},$$

de modo que

$$\boxed{ x_{F'}(Q) = \begin{pmatrix} 6\\ -1\\ 1 \end{pmatrix} \mathrm{m}. }$$

Los registros espaciales son numéricamente distintos en los dos marcos. En $F$,

$$x_F(Q)-x_F(P) = \begin{pmatrix} -3\\ 4\\ 0 \end{pmatrix} \mathrm{m},$$

por lo que

$$\left\| x_F(Q)-x_F(P) \right\| = 5\,\mathrm{m}.$$

En $F'$,

$$x_{F'}(Q)-x_{F'}(P) = \begin{pmatrix} 4\\ 3\\ 0 \end{pmatrix} \mathrm{m},$$

y

$$\left\| x_{F'}(Q)-x_{F'}(P) \right\| = 5\,\mathrm{m}.$$

Así,

$$\boxed{ \text{coordenadas distintas} \quad\text{pero}\quad \text{misma separación física}. }$$

Como sólo disponemos de registros correspondientes a una lectura temporal común, no podemos concluir si $P$ o $Q$ se mueven, ni definir velocidades o aceleraciones.

[]{#síntesis-operacional}

### Síntesis operacional {#fispm-c04-suxedntesis-operacional}

La arquitectura conceptual de la sección puede resumirse como una cadena de estructura creciente:

$$\boxed{ \text{geometría} \longrightarrow \text{medición espacial} \longrightarrow \text{marco físico mínimo}. }$$

En símbolos, $F=(O,B)$

se amplía a

$$\mathfrak R=(F,\mathcal L,\mathcal T,\mathcal O).$$

El marco físico permite producir registros

$$\boxed{ \left( t,\, x_F(P) \right). }$$

Un observador es el sistema operacional capaz de producirlos. Dos observadores pueden asignar coordenadas distintas sin desacuerdo físico, siempre que las cantidades comparadas se transformen correctamente y se atienda a los invariantes relevantes.

[]{#cierre-de-13}

### Cierre de §13 {#fispm-c04-cierre-de-13}

La sección ha mostrado por qué una terna de números no basta para constituir una referencia física. Un marco físico mínimo requiere:

$$\boxed{ \text{origen y ejes} + \text{calibración espacial} + \text{lectura temporal} + \text{realización operacional}. }$$

La misma ocurrencia puede recibir registros diferentes: $\left( t,\, x_F(P) \right)$

y

$$\left( t,\, x_{F'}(P) \right),$$

sin que cambie el punto geométrico descrito. Cuando los marcos espaciales son ortonormales y las calibraciones compatibles, las separaciones geométricas permanecen invariantes. Finalmente, quedan bloqueadas dos inferencias:

$$\boxed{ \text{registro temporal} \not\Rightarrow \text{movimiento} }$$

y

$$\boxed{ \text{marco físico} \not\Rightarrow \text{marco inercial}. }$$

Los ejercicios 4.26--4.27 obligan a separar explícitamente geometría, realización operacional, observador e inercialidad. La última sección del capítulo integrará todas las distinciones construidas ---puntos, vectores, coordenadas, bases, orientación, isometrías y marcos--- antes de entregar el concepto de posición dependiente del tiempo al capítulo 5. El siguiente paso será el §[14](#fispm-c04-integraciuxf3n-una-geometruxeda-varias-descripciones).

[]{#integración-una-geometría-varias-descripciones}

[]{#fispm-t1-c04-s14}

[]{#fpm-i-04-s14}

## 14. Integración: una geometría, varias descripciones {#fispm-c04-integraciuxf3n-una-geometruxeda-varias-descripciones}

[]{#una-geometría-varias-descripciones}

### Una geometría, varias descripciones {#fispm-c04-una-geometruxeda-varias-descripciones}

A lo largo del capítulo hemos repetido una misma operación conceptual:

1.  identificar un objeto geométrico;

2.  elegir una descripción;

3.  traducir el objeto a números;

4.  cambiar la descripción;

5.  reconstruir el mismo objeto.

El principio rector puede escribirse como

$$\boxed{ \text{objeto geométrico} \ne \text{representación numérica}. }$$

Un punto no es su terna de coordenadas. Un vector no es su columna de componentes. Una transformación lineal no es una única matriz. Un marco físico no es un dibujo con ejes. La descripción depende de elecciones; el objeto descrito no queda creado por esas elecciones.

[]{#la-jerarquía-construida-desde-1}

### La jerarquía construida desde §1 {#fispm-c04-la-jerarquuxeda-construida-desde-1}

El capítulo ha introducido una cadena de estructuras:

$$\boxed{ \mathcal E \longrightarrow V \longrightarrow \text{estructura euclídea} \longrightarrow \text{marcos} \longrightarrow \text{registros físicos}. }$$

Más explícitamente:

- $\mathcal E$: puntos del espacio afín;

- $V$: vectores de desplazamiento;

- $\langle\cdot,\cdot\rangle$: producto escalar;

- orientación: elección adicional en dimensión tres;

- $F=(O,B)$: marco geométrico;

- $\mathfrak R=(F,\mathcal L,\mathcal T,\mathcal O)$: marco físico mínimo.

Cada nivel añade estructura. Ningún nivel debe confundirse con la representación coordenada usada para describirlo.

[]{#definir-invariante-de-descripción}

### Definir: invariante de descripción {#fispm-c04-definir-invariante-de-descripciuxf3n}

**Definición 4.41 --- Invariante bajo cambio de descripción** Una cantidad asociada a una configuración geométrica será llamada **invariante de descripción** si su valor no cambia cuando modificamos únicamente el marco o la base usados para describir esa misma configuración, manteniendo fija la estructura geométrica pertinente.

La palabra "invariante" exige declarar **respecto de qué cambios**. Por ejemplo, entre marcos ortonormales compatibles, la distancia entre dos puntos satisface

$$\boxed{ d(P,Q) = \left\| x_F(Q)-x_F(P) \right\| = \left\| x_{F'}(Q)-x_{F'}(P) \right\|. }$$

Las coordenadas cambian; la distancia no.

[]{#no-todo-lo-que-cambia-deja-de-ser-geométricamente-válido}

### No todo lo que cambia deja de ser geométricamente válido {#fispm-c04-no-todo-lo-que-cambia-deja-de-ser-geomuxe9tricamente-vuxe1lido}

Supongamos que

$$[v]_B \ne [v]_{B'}.$$

No hay contradicción. Las dos columnas representan el mismo vector siempre que estén relacionadas por $[v]_{B'} = S_{B\leftarrow B'}^{-1}[v]_B.$ Del mismo modo, $x_F(P) \ne x_{F'}(P)$

puede describir un único punto $P$ cuando

$$x_{F'}(P) = S^{-1} \left( x_F(P)-[a]_B \right).$$

Por tanto, una representación puede cambiar de manera sistemática sin que cambie el objeto geométrico.

[]{#fispm-c04-definir-ley-covariante-de-representaciuxf3n label="fispm-c04-definir-ley-covariante-de-representaciuxf3n"}

**Definición 4.42 --- Ley covariante de representación** En esta sección usaremos **covariante** en un sentido local y operativo:

una familia de representaciones es covariante respecto de un cambio de descripción cuando sus datos numéricos cambian según una ley de transformación compatible con el tipo de objeto y con la composición de cambios de marco o base.

Este uso no introduce todavía cálculo tensorial. Significa simplemente que las representaciones no cambian arbitrariamente. Cada tipo de objeto posee su propia ley:

[]{#vector}

#### Vector {#fispm-c04-vector}

$$\boxed{ [v]_{B'} = S^{-1}[v]_B. }$$

[]{#punto}

#### Punto {#fispm-c04-punto}

$$\boxed{ x_{F'}(P) = S^{-1} \left( x_F(P)-[a]_B \right). }$$

[]{#operador-lineal}

#### Operador lineal {#fispm-c04-operador-lineal}

$$\boxed{ A_{B'}(T) = S^{-1}A_B(T)S. }$$

Las tres fórmulas son diferentes porque describen objetos de tipos diferentes.

[]{#composición-como-prueba-de-coherencia}

### Composición como prueba de coherencia {#fispm-c04-composiciuxf3n-como-prueba-de-coherencia}

Una ley de transformación no es sólo una receta para pasar de una descripción a otra. Debe ser compatible con cambios sucesivos. Para vectores,

$$S_{B\leftarrow C} = S_{B\leftarrow B'} S_{B'\leftarrow C}.$$

Para cambios afines,

$$(L_2,t_2)\circ(L_1,t_1) = (L_2L_1,\, L_2t_1+t_2).$$

Por tanto, pasar directamente o mediante una descripción intermedia debe producir el mismo resultado. Esta consistencia es una de las señales de que estamos cambiando la representación de un mismo objeto y no introduciendo datos arbitrarios.

[]{#proposición-reconstrucción-independiente-de-la-descripción}

### Proposición: reconstrucción independiente de la descripción {#fispm-c04-proposiciuxf3n-reconstrucciuxf3n-independiente-de-la-descripciuxf3n}

**Proposición 4.59 --- El objeto reconstruido no depende de la representación**

**(a) Vectores.** Sean $B$ y $B'$ dos bases de $V$. Si

$$[v]_{B'} = S_{B\leftarrow B'}^{-1}[v]_B,$$

entonces reconstruir el vector desde cualquiera de las dos columnas produce el mismo

$$v\in V.$$

**(b) Puntos.** Sean

$$F=(O,B), \qquad F'=(O',B')$$

dos marcos afines relacionados por

$$a=\overrightarrow{OO'}, \qquad S=S_{B\leftarrow B'}.$$

Si

$$x_{F'}(P) = S^{-1} \left( x_F(P)-[a]_B \right),$$

entonces reconstruir el punto desde $F$ o desde $F'$ produce el mismo

$$P\in\mathcal E.$$

**Demostración.**

[]{#parte-a}

#### Parte (a) {#fispm-c04-parte-a}

Escribamos

$$[v]_B = \begin{pmatrix} v^1\\ v^2\\ v^3 \end{pmatrix}, \qquad [v]_{B'} = \begin{pmatrix} v'^1\\ v'^2\\ v'^3 \end{pmatrix}.$$

Por definición de componentes, $v = v^1e_1+v^2e_2+v^3e_3.$

Proposición 4.39 establece que

$$[v]_B = S_{B\leftarrow B'}[v]_{B'}.$$

Pero las columnas de $S_{B\leftarrow B'}$ son precisamente

$$[e'_1]_B, \qquad [e'_2]_B, \qquad [e'_3]_B.$$

Por tanto,

$$[v]_B = \left[ v'^1e'_1+v'^2e'_2+v'^3e'_3 \right]_B.$$

La unicidad de componentes en $B$ implica $v = v'^1e'_1+v'^2e'_2+v'^3e'_3.$

Ambas columnas reconstruyen el mismo vector.

[]{#parte-b}

#### Parte (b) {#fispm-c04-parte-b}

Desde el marco $F$, $P = O+\overrightarrow{OP},$

con

$$[\overrightarrow{OP}]_B = x_F(P).$$

Desde $F'$, $P = O'+\overrightarrow{O'P},$

con

$$[\overrightarrow{O'P}]_{B'} = x_{F'}(P).$$

Proposición 4.51 equivale a

$$[\overrightarrow{O'P}]_{B'} = S^{-1} \left( [\overrightarrow{OP}]_B-[a]_B \right).$$

Por proposición 4.39, esto significa geométricamente

$$\overrightarrow{O'P} = \overrightarrow{OP}-a.$$

Como $O'=O+a,$

obtenemos

$$O'+\overrightarrow{O'P} = O+a+\overrightarrow{OP}-a = O+\overrightarrow{OP} = P.$$

$\square$

La proposición formaliza la idea central del capítulo:

$$\boxed{ \text{cambiar la descripción no cambia el objeto}. }$$

[]{#qué-cambia-y-qué-permanece}

### Qué cambia y qué permanece {#fispm-c04-quuxe9-cambia-y-quuxe9-permanece}

Podemos resumir los principales objetos así:

  Objeto                                 Representación dependiente de elección   Ley de cambio               Qué permanece
  -------------------------------------- ---------------------------------------- --------------------------- -------------------
  Punto $P$                              $x_F(P)$                                 afín                        el punto $P$
  Vector $v$                             $[v]_B$                                  lineal                      el vector $v$
  Desplazamiento $\overrightarrow{PQ}$   $[\overrightarrow{PQ}]_B$                lineal                      el desplazamiento
  Operador $T$                           $A_B(T)$                                 conjugación                 el operador $T$
  Distancia $d(P,Q)$                     cálculo desde coordenadas                compatible con la métrica   la distancia
  Ángulo $\theta(u,v)$                   cálculo desde componentes                compatible con la métrica   el ángulo

La última columna contiene objetos o cantidades geométricas. Las columnas intermedias contienen representaciones.

[]{#invariante-no-significa-mismo-número-en-cualquier-fórmula-mal-usada}

### Invariante no significa "mismo número en cualquier fórmula mal usada" {#fispm-c04-invariante-no-significa-mismo-nuxfamero-en-cualquier-fuxf3rmula-mal-usada}

La invariancia no permite ignorar las leyes de transformación. Por ejemplo, en una base no ortonormal la norma no se calcula, en general, mediante $(v^1)^2+(v^2)^2+(v^3)^2.$

Debe emplearse la estructura métrica adecuada, representada por la matriz de Gram correspondiente. Por tanto, el contenido correcto es:

Este punto evita confundir invariancia geométrica con invariancia literal de una expresión numérica particular.

[]{#principio-metodológico-3}

### Principio metodológico {#fispm-c04-principio-metodoluxf3gico-3}

**Principio metodológico 4.28 --- Preguntar primero por el objeto, después por sus números** Ante una fórmula con coordenadas o matrices:

1.  identificar el objeto geométrico representado;

2.  identificar las elecciones de origen, base, orientación y unidades;

3.  escribir la ley de transformación correcta para ese tipo de objeto;

4.  distinguir qué datos cambian de representación y qué cantidades permanecen invariantes;

5.  sólo entonces comparar números.

Este principio resume la disciplina conceptual desarrollada desde §1.

[]{#balance-objeto-representación-e-invariancia}

### Balance: objeto, representación e invariancia {#fispm-c04-balance-objeto-representaciuxf3n-e-invariancia}

La síntesis inicial queda organizada por dos ideas complementarias.

[]{#invariancia}

#### Invariancia {#fispm-c04-invariancia}

$$\boxed{ \text{el objeto o la cantidad geométrica pertinente permanece}. }$$

[]{#covariancia-de-representación}

#### Covariancia de representación {#fispm-c04-covariancia-de-representaciuxf3n}

$$\boxed{ \text{los datos numéricos cambian mediante una ley coherente}. }$$

Así, "varias descripciones" no significa "varias geometrías". El mismo punto, vector, desplazamiento u operador puede aparecer mediante números diferentes sin perder identidad geométrica. Todavía falta integrar estas ideas en situaciones completas y reconocer errores de tipo mediante los tres ejercicios finales ejercicios 4.28--4.30.

[]{#invariantes-métricos-bajo-marcos-ortonormales}

### Invariantes métricos bajo marcos ortonormales {#fispm-c04-invariantes-muxe9tricos-bajo-marcos-ortonormales}

Sean

$$F=(O,E), \qquad F'=(O',E')$$

dos marcos con bases ortonormales. Para dos puntos $P,Q$, proposición 4.52 da

$$[\overrightarrow{PQ}]_{E'} = S^{-1} [\overrightarrow{PQ}]_E,$$

y proposición 4.56 ya estableció que, entre bases ortonormales, $S^{\mathsf T}S=I, \qquad S^{-1}=S^{\mathsf T}.$ Por tanto $S^{-1}$ también es ortogonal y,

$$\boxed{ d(P,Q) = \left\| [\overrightarrow{PQ}]_E \right\| = \left\| [\overrightarrow{PQ}]_{E'} \right\|. }$$

Del mismo modo, para dos vectores $u,v$,

$$\boxed{ \langle u,v\rangle = [u]_E^{\mathsf T}[v]_E = [u]_{E'}^{\mathsf T}[v]_{E'}. }$$

En consecuencia, también permanece el ángulo:

$$\boxed{ \theta(u,v) = \theta_E(u,v) = \theta_{E'}(u,v). }$$

Las columnas cambian; las relaciones métricas no.

[]{#la-orientación-requiere-una-capa-adicional}

### La orientación requiere una capa adicional {#fispm-c04-la-orientaciuxf3n-requiere-una-capa-adicional}

La métrica por sí sola no distingue una base ortonormal positiva de una negativa. Si

$$S_{E\leftarrow E'}$$

es ortogonal, entonces $\det S=\pm1.$ El signo informa si el cambio de descripción conserva o invierte la orientación relativa de las bases. Para una terna de vectores

$$(u,v,w),$$

el volumen geométrico no orientado satisface

$$\boxed{ \left| \operatorname{Vol}^{\mathrm{or}}(u,v,w) \right| }$$

independientemente de la base ortonormal usada para calcularlo. Pero el signo de un determinante coordenado sólo puede interpretarse después de declarar la orientación de la base de referencia. Por tanto:

$$\boxed{ \text{métrica} \ne \text{orientación}. }$$

Esta distinción explica por qué una reflexión puede conservar todas las distancias y, sin embargo, invertir orientación.

[]{#triangulación-y-trilateración-no-son-lo-mismo}

### Triangulación y trilateración no son lo mismo {#fispm-c04-triangulaciuxf3n-y-trilateraciuxf3n-no-son-lo-mismo}

En problemas de localización se emplean dos familias de procedimientos que conviene distinguir.

[]{#triangulación}

#### Triangulación {#fispm-c04-triangulaciuxf3n}

Reconstruye una posición a partir de **direcciones o ángulos** medidos desde referencias conocidas.

[]{#trilateración}

#### Trilateración {#fispm-c04-trilateraciuxf3n}

Reconstruye una posición a partir de **distancias** a puntos de referencia conocidos. En esta sección utilizaremos trilateración porque permite expresar la consistencia directamente mediante los invariantes métricos ya desarrollados. No usaremos ambos términos como sinónimos.

[]{#definir-datos-métricos-de-localización}

### Definir: datos métricos de localización {#fispm-c04-definir-datos-muxe9tricos-de-localizaciuxf3n}

**Definición 4.43 --- Datos de trilateración respecto de cuatro referencias** Sean

$$A_0,A_1,A_2,A_3\in\mathcal E$$

cuatro puntos afínmente independientes. Para un punto $P$, definimos sus datos métricos de localización por

$$\boxed{ \Lambda(P) := \begin{pmatrix} d(P,A_0)^2\\ d(P,A_1)^2\\ d(P,A_2)^2\\ d(P,A_3)^2 \end{pmatrix}. }$$

La independencia afín significa que

$$\overrightarrow{A_0A_1}, \qquad \overrightarrow{A_0A_2}, \qquad \overrightarrow{A_0A_3}$$

forman una base de $V$. Los datos $\Lambda(P)$ están formados por cantidades métricas, no por coordenadas del punto.

[]{#proposición-cuatro-distancias-determinan-un-punto-en-dimensión-tres}

### Proposición: cuatro distancias determinan un punto en dimensión tres {#fispm-c04-proposiciuxf3n-cuatro-distancias-determinan-un-punto-en-dimensiuxf3n-tres}

**Proposición 4.60 --- Unicidad de la trilateración en dimensión tres** Sean

$$A_0,A_1,A_2,A_3$$

cuatro puntos afínmente independientes. Si dos puntos $P,Q$ satisfacen

$$\Lambda(P)=\Lambda(Q),$$

entonces

$$\boxed{ P=Q. }$$

**Demostración.** Tomamos

$$O:=A_0,$$

y definimos

$$p:=\overrightarrow{OP}, \qquad q:=\overrightarrow{OQ},$$

$$a_i:=\overrightarrow{OA_i}, \qquad i=1,2,3.$$

Como $\Lambda(P)=\Lambda(Q),$

tenemos para cada $i$: $d(P,A_i)^2-d(P,A_0)^2 = d(Q,A_i)^2-d(Q,A_0)^2.$

Ahora, $d(P,A_i)^2 = \|p-a_i\|^2,$

y

$$d(P,A_0)^2 = \|p\|^2.$$

Por tanto, $\|p-a_i\|^2-\|p\|^2 = \|q-a_i\|^2-\|q\|^2.$

Expandimos:

$$\|p\|^2 - 2\langle p,a_i\rangle + \|a_i\|^2 - \|p\|^2$$

es igual a

$$\|q\|^2 - 2\langle q,a_i\rangle + \|a_i\|^2 - \|q\|^2.$$

Luego, $\langle p-q,a_i\rangle=0$

para

$$i=1,2,3.$$

Como los tres vectores

$$a_1,a_2,a_3$$

forman una base de $V$, el vector

$$p-q$$

es ortogonal a todo $V$. En particular, $\langle p-q,p-q\rangle=0.$ Por positividad del producto escalar, $p-q=0.$ Así, $p=q,$

y por tanto

$$P=Q.$$

$\square$

La proposición no afirma que cualquier cuádrupla de números positivos corresponda a un punto. Afirma únicamente **unicidad** cuando un punto compatible con esos datos existe.

[]{#consistencia-de-los-datos-bajo-cambio-de-marco}

### Consistencia de los datos bajo cambio de marco {#fispm-c04-consistencia-de-los-datos-bajo-cambio-de-marco}

Como cada entrada de

$$\Lambda(P)$$

es una distancia geométrica, un cambio entre marcos ortonormales no modifica el vector de datos:

$$\boxed{ \Lambda_F(P) = \Lambda_{F'}(P). }$$

Lo que sí cambia es la columna coordenada del punto reconstruido: $x_F(P) \ne x_{F'}(P)$

en general. Pero proposición 4.51 relaciona ambas columnas mediante $x_{F'}(P) = S^{-1} \left( x_F(P)-[a]_B \right).$

Así obtenemos dos niveles simultáneos:

$$\boxed{ \text{datos métricos invariantes} }$$

y

$$\boxed{ \text{coordenadas covariantes}. }$$

[]{#proposición-la-reconstrucción-métrica-es-compatible-con-el-cambio-de-marco}

### Proposición: la reconstrucción métrica es compatible con el cambio de marco {#fispm-c04-proposiciuxf3n-la-reconstrucciuxf3n-muxe9trica-es-compatible-con-el-cambio-de-marco}

**Proposición 4.61 --- Consistencia de la trilateración entre marcos ortonormales** Sean

$$A_0,A_1,A_2,A_3$$

cuatro referencias afínmente independientes y sean $F,F'$ dos marcos ortonormales. Si un punto $P$ es compatible con los datos

$$\Lambda(P),$$

entonces la reconstrucción realizada en $F$ y la reconstrucción realizada en $F'$ corresponden al mismo punto geométrico. Sus columnas satisfacen

$$\boxed{ x_{F'}(P) = S^{-1} \left( x_F(P)-[a]_B \right). }$$

**Demostración.** Las distancias que forman

$$\Lambda(P)$$

son invariantes entre $F$ y $F'$. Por proposición 4.60, existe a lo sumo un punto geométrico compatible con esos cuatro valores. Por tanto, si ambos procedimientos reconstruyen un punto compatible, ambos deben reconstruir el mismo $P$. Sus representaciones quedan entonces relacionadas por la proposición 4.51. $\square$ La consistencia entre observadores no requiere que produzcan la misma terna de coordenadas. Requiere que sus ternas representen el mismo objeto y respeten la ley de transformación correspondiente.

[]{#ejemplo-exacto-de-localización-por-distancias}

### Ejemplo exacto de localización por distancias {#fispm-c04-ejemplo-exacto-de-localizaciuxf3n-por-distancias}

Tomemos una base ortonormal

$$E=(e_1,e_2,e_3)$$

y cuatro referencias:

$$A_0=O,$$

$$A_1=O+e_1, \qquad A_2=O+e_2, \qquad A_3=O+e_3.$$

Sea

$$x_F(P) = \begin{pmatrix} 2\\ 3\\ 4 \end{pmatrix}.$$

Entonces:

$$d(P,A_0)^2 = 2^2+3^2+4^2 = 29,$$

$$d(P,A_1)^2 = 1^2+3^2+4^2 = 26,$$

$$d(P,A_2)^2 = 2^2+2^2+4^2 = 24,$$

y

$$d(P,A_3)^2 = 2^2+3^2+3^2 = 22.$$

Así,

$$\boxed{ \Lambda(P) = \begin{pmatrix} 29\\ 26\\ 24\\ 22 \end{pmatrix}. }$$

Si otro marco ortonormal asigna a $P$ una columna diferente, estos cuatro valores permanecen exactamente iguales.

[]{#cómo-se-recuperan-las-coordenadas-en-el-ejemplo}

### Cómo se recuperan las coordenadas en el ejemplo {#fispm-c04-cuxf3mo-se-recuperan-las-coordenadas-en-el-ejemplo}

En el ejemplo anterior, si

$$x_F(P) = \begin{pmatrix} x\\ y\\ z \end{pmatrix},$$

entonces $d(P,A_0)^2 = x^2+y^2+z^2.$

Restando la distancia a $A_1$: $d(P,A_0)^2-d(P,A_1)^2 = 2x-1.$ Por tanto, $x = \frac{ d(P,A_0)^2-d(P,A_1)^2+1 }{2}.$ Análogamente,

$$y = \frac{ d(P,A_0)^2-d(P,A_2)^2+1 }{2},$$

$$z = \frac{ d(P,A_0)^2-d(P,A_3)^2+1 }{2}.$$

Con los datos

$$29,\ 26,\ 24,\ 22,$$

obtenemos $x=2, \qquad y=3, \qquad z=4.$ La reconstrucción coordenada depende del marco elegido. El conjunto de distancias no.

[]{#principio-metodológico-de-consistencia-entre-observadores}

### Principio metodológico de consistencia entre observadores {#fispm-c04-principio-metodoluxf3gico-de-consistencia-entre-observadores}

**Principio metodológico 4.29 --- Comparar invariantes antes de comparar coordenadas** Cuando dos descripciones de una misma configuración parezcan incompatibles:

1.  transformar primero ambas al mismo marco o reconstruir el objeto geométrico;

2.  comparar distancias, ángulos u otros invariantes pertinentes;

3.  verificar la ley covariante de las representaciones;

4.  sólo entonces diagnosticar una discrepancia física o experimental.

Dos columnas diferentes no constituyen por sí solas datos contradictorios.

[]{#balance-reconstrucción-e-invariantes}

### Balance: reconstrucción e invariantes {#fispm-c04-balance-reconstrucciuxf3n-e-invariantes}

La integración geométrica queda ahora organizada en tres niveles:

[]{#objeto}

#### Objeto {#fispm-c04-objeto}

$$\boxed{ P,\ v,\ \overrightarrow{PQ},\ T }$$

[]{#representación-covariante}

#### Representación covariante {#fispm-c04-representaciuxf3n-covariante}

$$\boxed{ x_F(P),\ [v]_B,\ [\overrightarrow{PQ}]_B,\ A_B(T) }$$

[]{#invariantes}

#### Invariantes {#fispm-c04-invariantes}

$$\boxed{ d(P,Q),\ \|v\|,\ \langle u,v\rangle,\ \theta(u,v) }$$

y, cuando la orientación forma parte de la estructura, las cantidades orientadas deben interpretarse respecto de esa elección. La reconstrucción por cuatro distancias muestra concretamente que distintos observadores pueden utilizar coordenadas diferentes y, sin embargo, recuperar una única posición geométrica compatible con los mismos datos métricos. Todavía faltan los tres ejercicios integradores ejercicios 4.28--4.30 y la transición final hacia el capítulo 5.

[]{#fispm-t1-c04-e0028}

**Ejercicio 4.28 --- Un punto y un vector, dos descripciones.**

**Función pedagógica:** `Tipos de objeto → Leyes distintas → Reconstrucción → Invariante`

Sea

$$F=(O,E), \qquad E=(e_1,e_2,e_3)$$

un marco ortonormal positivo.

Definimos $F'=(O',E')$

mediante $\overrightarrow{OO'} = e_1-2e_2+e_3$

y

$$E' = (e_2,-e_1,e_3).$$

Se dan

$$x_F(P) = \begin{pmatrix} 5\\ 0\\ 2 \end{pmatrix}, \qquad [v]_E = \begin{pmatrix} 2\\ -1\\ 2 \end{pmatrix}.$$

1.  Calcula $x_{F'}(P)$.

2.  Calcula $[v]_{E'}$.

3.  Explica por qué el punto y el vector no obedecen la misma fórmula.

4.  Reconstruye $P$ y $v$ desde los datos en $F'$.

5.  Comprueba que $\|v\|$ es invariante.

**Solución desarrollada**

La matriz de cambio es

$$S_{E\leftarrow E'} = \begin{pmatrix} 0&-1&0\\ 1&0&0\\ 0&0&1 \end{pmatrix},$$

por lo que

$$S^{-1} = \begin{pmatrix} 0&1&0\\ -1&0&0\\ 0&0&1 \end{pmatrix}.$$

Además,

$$[a]_E = \begin{pmatrix} 1\\ -2\\ 1 \end{pmatrix}.$$

Para el punto:

$$x_{F'}(P) = S^{-1} \left( x_F(P)-[a]_E \right) = \boxed{ \begin{pmatrix} 2\\ -4\\ 1 \end{pmatrix} }.$$

Para el vector no aparece traslación:

$$[v]_{E'} = S^{-1}[v]_E = \boxed{ \begin{pmatrix} -1\\ -2\\ 2 \end{pmatrix} }.$$

La diferencia entre ambas leyes proviene del tipo de objeto:

$$\boxed{ \text{punto}\to\text{ley afín}, \qquad \text{vector}\to\text{ley lineal}. }$$

Reconstruimos el desplazamiento desde $O'$: $2e'_1-4e'_2+e'_3 = 2e_2+4e_1+e_3.$

Como $O'=O+e_1-2e_2+e_3,$

obtenemos $P = O' + 2e'_1-4e'_2+e'_3 = O+5e_1+2e_3,$

que coincide con la reconstrucción desde

$$x_F(P)= \begin{pmatrix} 5\\ 0\\ 2 \end{pmatrix}.$$

Para el vector, $-e'_1-2e'_2+2e'_3 = -e_2+2e_1+2e_3 = v.$

Finalmente, $\|v\|^2 = 2^2+(-1)^2+2^2 = 9,$

y

$$\|[v]_{E'}\|^2 = (-1)^2+(-2)^2+2^2 = 9.$$

Las representaciones cambian; el punto, el vector y la norma del vector permanecen.

[]{#fispm-t1-c04-e0029}

**Ejercicio 4.29 --- Trilateración en dos marcos.**

**Función pedagógica:** `Datos invariantes → Coordenadas covariantes → Reconstrucción única`

En un marco ortonormal

$$F=(O,E)$$

se toman las referencias

$$A_0=O,$$

$$A_1=O+e_1, \qquad A_2=O+e_2, \qquad A_3=O+e_3.$$

Un punto $P$ tiene

$$x_F(P) = \begin{pmatrix} 2\\ 3\\ 4 \end{pmatrix},$$

y por tanto

$$\Lambda(P) = \begin{pmatrix} 29\\ 26\\ 24\\ 22 \end{pmatrix}.$$

Considera ahora

$$O'=O+e_1,$$

$$E'=(e_2,-e_1,e_3).$$

1.  Calcula las coordenadas de $P$ y de las cuatro referencias en $F'$.

2.  Recalcula las cuatro distancias cuadradas usando únicamente las coordenadas en $F'$.

3.  Explica por qué proposiciones 4.60--4.61 garantizan que ambos marcos reconstruyen el mismo punto.

**Solución desarrollada**

Tenemos

$$S= \begin{pmatrix} 0&-1&0\\ 1&0&0\\ 0&0&1 \end{pmatrix}, \qquad S^{-1} = \begin{pmatrix} 0&1&0\\ -1&0&0\\ 0&0&1 \end{pmatrix},$$

y

$$[a]_E = \begin{pmatrix} 1\\ 0\\ 0 \end{pmatrix}.$$

Para $P$:

$$\boxed{ x_{F'}(P) = \begin{pmatrix} 3\\ -1\\ 4 \end{pmatrix}. }$$

Las referencias quedan:

$$x_{F'}(A_0) = \begin{pmatrix} 0\\ 1\\ 0 \end{pmatrix},$$

$$x_{F'}(A_1) = \begin{pmatrix} 0\\ 0\\ 0 \end{pmatrix},$$

$$x_{F'}(A_2) = \begin{pmatrix} 1\\ 1\\ 0 \end{pmatrix},$$

$$x_{F'}(A_3) = \begin{pmatrix} 0\\ 1\\ 1 \end{pmatrix}.$$

Entonces,

$$x_{F'}(P)-x_{F'}(A_0) = \begin{pmatrix} 3\\ -2\\ 4 \end{pmatrix},$$

y

$$d(P,A_0)^2 = 3^2+(-2)^2+4^2 = 29.$$

Asimismo,

$$d(P,A_1)^2 = 3^2+(-1)^2+4^2 = 26,$$

$$d(P,A_2)^2 = 2^2+(-2)^2+4^2 = 24,$$

y

$$d(P,A_3)^2 = 3^2+(-2)^2+3^2 = 22.$$

Por tanto,

$$\boxed{ \Lambda_{F'}(P) = \Lambda_F(P) = \begin{pmatrix} 29\\ 26\\ 24\\ 22 \end{pmatrix}. }$$

Proposición 4.60 garantiza que esos cuatro datos son compatibles con a lo sumo un punto geométrico.

Proposición 4.61 garantiza que las reconstrucciones en $F$ y $F'$ son representaciones del mismo $P$ y obedecen la ley afín de cambio de marco.

[]{#fispm-t1-c04-e0030}

**Ejercicio 4.30 --- Auditoría conceptual del capítulo.**

**Función pedagógica:** `Integración global → Detección de falsos amigos → Preparación del capítulo siguiente`

Decide si cada afirmación es correcta o incorrecta y justifica brevemente.

1.  Si dos puntos tienen la misma terna numérica en marcos diferentes, representan necesariamente el mismo punto.

2.  Un vector puede tener columnas distintas en dos bases sin cambiar como objeto geométrico.

3.  Cambiar el origen modifica el desplazamiento $\overrightarrow{PQ}$.

4.  Una matriz ortogonal representa necesariamente una transformación activa.

5.  Una reflexión conserva distancias aunque invierta orientación.

6.  Cuatro distancias a referencias afínmente independientes determinan a lo sumo un punto en dimensión tres.

7.  Un marco físico dotado de reloj es automáticamente inercial.

8.  Conocer un único registro $(t,x_F(P))$ basta para decidir si $P$ se mueve.

9.  La invariancia de una cantidad significa que cualquier fórmula coordenada ingenua produce siempre el mismo número.

10. Para comenzar a estudiar movimiento será necesario añadir dependencia temporal a la posición.

**Solución desarrollada**

**1. Incorrecta.** La misma terna numérica puede representar puntos diferentes si cambian origen o base. Debe conocerse la relación entre marcos.

**2. Correcta.** Las columnas obedecen

$$[v]_{B'} = S^{-1}[v]_B,$$

mientras $v$ permanece fijo.

**3. Incorrecta.** El cambio de origen altera coordenadas de puntos, pero el desplazamiento entre dos puntos no depende del origen.

**4. Incorrecta.** Una matriz ortogonal puede aparecer tanto en un cambio pasivo entre bases ortonormales como en la representación activa de una isometría.

**5. Correcta.** Para una reflexión ortogonal,

$$Q^{\mathsf T}Q=I, \qquad \det Q=-1.$$

Conserva la métrica e invierte orientación.

**6. Correcta.** Es exactamente proposición 4.60, bajo la hipótesis de independencia afín de las referencias.

**7. Incorrecta.** Un reloj aporta lectura temporal; la inercialidad requiere estructura dinámica adicional.

**8. Incorrecta.** Un único registro sólo localiza una ocurrencia bajo ciertos convenios. No proporciona una ley de dependencia temporal.

**9. Incorrecta.** La cantidad geométrica puede ser invariante mientras su fórmula coordenada cambia. En una base no ortonormal, por ejemplo, debe usarse la matriz de Gram correspondiente.

**10. Correcta.** El paso siguiente consiste precisamente en permitir que la localización espacial dependa de la lectura temporal. Esa estructura pertenece al capítulo 5 y no se desarrolla aquí.

[]{#la-red-conceptual-completa-del-capítulo}

### La red conceptual completa del capítulo {#fispm-c04-la-red-conceptual-completa-del-capuxedtulo}

El capítulo 4 puede condensarse en la siguiente cadena:

$$\boxed{ \text{puntos} \longrightarrow \text{desplazamientos} \longrightarrow \text{vectores} \longrightarrow \text{métrica} \longrightarrow \text{orientación} }$$

seguida por

$$\boxed{ \text{bases} \longrightarrow \text{coordenadas} \longrightarrow \text{cambios de descripción} \longrightarrow \text{marcos} \longrightarrow \text{registros físicos}. }$$

Cada flecha añade una capa de estructura o de representación. Ninguna permite borrar las distinciones de tipo establecidas antes.

[]{#lo-que-el-capítulo-deja-establecido}

### Lo que el capítulo deja establecido {#fispm-c04-lo-que-el-capuxedtulo-deja-establecido}

Al cerrar capítulo 4 disponemos de:

- espacio afín y desplazamientos;

- espacio vectorial de traslaciones;

- bases y componentes;

- producto escalar, norma, distancia, proyección y ángulo;

- bases ortonormales;

- orientación, determinante y volumen orientado;

- producto vectorial en dimensión tres;

- cambios pasivos de base;

- transformaciones activas e isometrías;

- rotaciones y reflexiones;

- cambios afines de origen y marco;

- realización operacional mínima de un marco físico;

- noción de observador como sistema de referencia operacional;

- invariantes y leyes coherentes de representación.

Todo ello se ha construido sin introducir todavía una ley de movimiento.

### La puerta hacia el capítulo 5 {#fispm-c04-la-puerta-hacia-fpm-i-05}

Hasta aquí, un punto $P$ ha sido considerado como una localización geométrica fija dentro de cada problema. El siguiente paso conceptual será permitir que la posición asignada a un cuerpo dependa de la lectura temporal. Eso exigirá introducir una aplicación temporal del tipo

$$t \longmapsto P(t),$$

y estudiar su geometría. El capítulo 4 no desarrolla todavía esa estructura. Sólo deja preparado el lenguaje necesario para que, cuando aparezca una posición dependiente del tiempo, quede claro:

- qué es el punto geométrico;

- qué es su vector de posición relativo a un origen;

- qué son sus coordenadas;

- cómo cambian esas coordenadas al cambiar de marco;

- qué cantidades geométricas son independientes de la descripción.

### Cierre de §14 y de la redacción del capítulo 4 {#fispm-c04-cierre-de-14-y-de-la-redacciuxf3n-de-fpm-i-04}

La afirmación que organiza todo el capítulo es:

$$\boxed{ \text{una geometría puede admitir muchas descripciones numéricas coherentes}. }$$

Las representaciones cambian de acuerdo con el tipo de objeto:

$$\boxed{ \text{punto: ley afín}, }$$

$$\boxed{ \text{vector: ley lineal}, }$$

$$\boxed{ \text{operador: conjugación}. }$$

Mientras tanto, las cantidades geométricas pertinentes se preservan bajo los cambios de descripción que respetan la estructura correspondiente. Los ejercicios 4.28--4.30 completan la integración conceptual del capítulo mediante comparación de tipos, invariantes y leyes de cambio.

[^1]: V. I. Arnold, *Mathematical Methods of Classical Mechanics*, 2.ª ed., Springer, 1989, parte I, cap. 1, §2.A «Notation», pp. 3--4.

[^2]: R. Shankar, *Fundamentals of Physics I: Mechanics, Relativity, and Thermodynamics*, expanded ed., Yale University Press, 2019, cap. 2, §2.4 «Choice of axes and basis vectors», pp. 22--25.

[^3]: Véanse R. Shankar, *Basic Training in Mathematics: A Fitness Program for Science Students*, Springer, 1995, cap. 7, §7.1 «Review of Vector Analysis», pp. 149--154; y G. B. Arfken, H. J. Weber y F. E. Harris, *Mathematical Methods for Physicists*, 7.ª ed., Academic Press, 2013, cap. 3, §3.2 «Vector in 3-D Spaces», pp. 126--132.

[^4]: G. B. Arfken, H. J. Weber y F. E. Harris, *Mathematical Methods for Physicists*, 7.ª ed., Academic Press, 2013, cap. 3, §3.3 «Coordinate Transformations», pp. 133--138.

[^5]: G. B. Arfken, H. J. Weber y F. E. Harris, *Mathematical Methods for Physicists*, 7.ª ed., Academic Press, 2013, cap. 3, §3.4 «Rotations in $\mathbb R^3$», pp. 139--142.

[^6]: D. Kleppner y R. J. Kolenkow, *An Introduction to Mechanics*, 2.ª ed., Cambridge University Press, 2010, cap. 2, §2.7 «Base Units and Physical Standards», p. 59 y ss.

[^7]: D. Kleppner y R. J. Kolenkow, *An Introduction to Mechanics*, 2.ª ed., Cambridge University Press, 2010, cap. 2, §2.4 «Newton's First Law and Inertial Systems», p. 51 y ss.; véase también el ejemplo 2.1 del mismo capítulo.
