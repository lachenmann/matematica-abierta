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
date-modified: 2026-10-15
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
---

[Capítulo 3](fisica-para-matematicos-capitulo-3-medicion-incertidumbre-estimacion-y-ordenes-de-magnitud.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [Capítulo 5](fisica-para-matematicos-capitulo-5-tiempo-movimiento-y-curvas.md)

[]{#fispm-t1-c04-s01}

[]{#fpm-i-04-s01}

## §1 — Un punto no es un vector

### 1.1. La pregunta física antes de las coordenadas

Dos personas describen el mismo objeto. Una coloca el origen de una regla en el extremo izquierdo de una mesa; la otra lo sitúa un metro a su derecha. Sus números para la posición del objeto difieren. Sin embargo, **el objeto no se ha desplazado por el mero cambio de origen**.
Este hecho invita a separar tres objetos distintos:

- el **punto** $P$ donde se encuentra el objeto;
- el **origen** $O$ que elegimos para describirlo;
- el **desplazamiento** desde $O$ hasta $P$.

El número que asignamos a una posición requiere una convención. La diferencia geométrica entre dos puntos puede expresarse sin privilegiar un origen.[^arnold-affine]

> Activación
> Si una persona cambia de habitación la regla con la que mide, ¿se desplaza también el objeto medido? ¿Qué cambió realmente en el procedimiento de descripción?

### 1.2. Representar: puntos y flechas de desplazamiento

Imaginemos tres puntos $O,P,Q$ sobre una recta, en ese orden. La flecha de $O$ a $P$ y la flecha de $P$ a $Q$ pueden componerse para dar la flecha de $O$ a $Q$.

$$
\overrightarrow{OP}+\overrightarrow{PQ}=\overrightarrow{OQ}.
$$

La suma en esta expresión es una suma de **desplazamientos**, no una suma de puntos. Los tres puntos sirven como extremos; las flechas pertenecen a otro tipo de objeto matemático.
El dibujo sugiere la ley, pero todavía tenemos que definir la estructura que permite demostrarla.

### 1.3. Definir: espacio afín

Un espacio vectorial real $V$ permite sumar vectores y multiplicarlos por escalares reales. Para este capítulo trabajaremos con un espacio vectorial de dimensión tres, aunque las primeras identidades no dependen de esa dimensión.

> **FPM-I-04-D01 — Espacio afín real**
> Un espacio afín $\mathcal E$ modelado sobre el espacio vectorial real $V$ es un conjunto no vacío de puntos junto con una operación de traslación
>
> $$
> \mathcal E\times V\longrightarrow\mathcal E,
> \qquad(P,v)\longmapsto P+v,
> $$
>
> que satisface:
>
> $$
> P+0=P,\qquad (P+u)+v=P+(u+v),
> $$
>
> y para cada par $P,Q\in\mathcal E$ existe un **único** $v\in V$ tal que $P+v=Q$.

Las dos primeras condiciones hacen coherente la traslación por varios desplazamientos. La última garantiza que, entre dos puntos, existe exactamente un vector de desplazamiento.

> Hipótesis y alcance
> Esta es una **idealización geométrica** del espacio físico clásico, no una conclusión empírica obtenida por definición. La conveniencia de esa idealización debe contrastarse con el fenómeno y la escala considerados, tal como exige FPM-I-01.

### 1.4. Definir: desplazamiento entre puntos

> **FPM-I-04-D02 — Desplazamiento**
> Dados $P,Q\in\mathcal E$, definimos $\overrightarrow{PQ}\in V$ como el único vector que satisface
>
> $$
> P+\overrightarrow{PQ}=Q.
> $$

En particular, $\overrightarrow{PQ}$ no es el punto $Q$ y no necesita elegir ningún origen global. Es un vector libre cuya interpretación puede ser longitud y dirección cuando añadamos la métrica euclídea.
La notación $Q-P$ puede usarse como abreviatura de $\overrightarrow{PQ}$, pero **sólo como diferencia de dos puntos**. No debe interpretarse como una resta entre dos vectores de posición previamente identificados sin origen.

### 1.5. Primera prueba: la ley del triángulo

> **FPM-I-04-P01 — Identidades de desplazamiento**
> En todo espacio afín $\mathcal E$ modelado sobre $V$, para cualesquiera puntos $P,Q,R$:
>
> $$
> \overrightarrow{PP}=0,
> \qquad
> \overrightarrow{QP}=-\overrightarrow{PQ},
> $$
>
> y
>
> $$
> \boxed{\overrightarrow{PQ}+\overrightarrow{QR}=\overrightarrow{PR}.}
> $$

**Demostración.** Por la identidad $P+0=P$ y la unicidad del vector que lleva $P$ a sí mismo, se obtiene $\overrightarrow{PP}=0$.
Por definición, $P+\overrightarrow{PQ}=Q$. Trasladamos este punto por el vector opuesto:

$$
Q+(-\overrightarrow{PQ})
=(P+\overrightarrow{PQ})+(-\overrightarrow{PQ})
=P.
$$

La unicidad del desplazamiento de $Q$ a $P$ implica $\overrightarrow{QP}=-\overrightarrow{PQ}$.
Finalmente,

$$
P+(\overrightarrow{PQ}+\overrightarrow{QR})
=(P+\overrightarrow{PQ})+\overrightarrow{QR}
=Q+\overrightarrow{QR}=R.
$$

Como $\overrightarrow{PR}$ es el único vector que lleva $P$ a $R$, ambos deben coincidir. $\square$
**Autoexplicación de la prueba.** El mecanismo no usa una figura particular ni componentes: utiliza la compatibilidad de traslaciones y, al final, la unicidad exigida en D01. Por eso la ley vale antes de introducir bases o coordenadas.

### 1.6. ¿Por qué no podemos sumar dos puntos?

En $V$ sí existe la operación

$$
V\times V\longrightarrow V,
\qquad (u,v)\longmapsto u+v.
$$

En cambio, D01 no ofrece ninguna operación intrínseca

$$
\mathcal E\times\mathcal E\longrightarrow\mathcal E
$$

que merezca llamarse suma de puntos. La expresión $P+Q$ no está definida por nuestra estructura. En contraste, $P+v$ sí está definida y es un punto; $Q-P$ sí está definida y es un vector.

> Error plausible
> «Si dibujé un punto como $(2,3)$ y otro como $(4,5)$, puedo sumarlos y obtener $(6,8)$; por tanto, sumar puntos es una operación geométrica». La terna o pareja numérica ya presupone un origen y ejes; la suma obtenida depende de esa convención. No demuestra la existencia de una suma canónica de puntos.

### 1.7. El origen es una elección, no una propiedad del punto

> **FPM-I-04-D03 — Origen y vector de posición**
> Elegido un punto $O\in\mathcal E$ como **origen**, el vector de posición de $P$ relativo a $O$ es
>
> $$
> r_O(P):=\overrightarrow{OP}\in V.
> $$

El subíndice recuerda que se eligió un punto de referencia. La elección permite construir una correspondencia entre puntos y vectores, pero no los convierte retroactivamente en objetos idénticos.

> **FPM-I-04-MP01 — Un punto no es un vector**
> Antes de escribir una posición como un vector o una terna, declarar el origen y, cuando correspondan, los ejes y las unidades.

### 1.8. Segunda prueba: cambiar el origen

Tomemos un origen nuevo $O'=O+a$, donde $a\in V$. Entonces

$$
\overrightarrow{OO'}=a.
$$

La ley del triángulo aplicada a $O',O,P$ da

$$
\overrightarrow{O'O}+\overrightarrow{OP}=\overrightarrow{O'P}.
$$

Como $\overrightarrow{O'O}=-a$, obtenemos

$$
\boxed{r_{O'}(P)=r_O(P)-a.}
$$

La posición **representada** cambia en un vector constante $-a$ para todos los puntos. La geometría no exige que los puntos se hayan movido.

> **FPM-I-04-P02 — Invariancia del desplazamiento respecto del origen**
> Para cualesquiera $P,Q,O,O'\in\mathcal E$,
>
> $$
> \boxed{r_O(Q)-r_O(P)=r_{O'}(Q)-r_{O'}(P)=\overrightarrow{PQ}.}
> $$

**Demostración.** P01 da $r_O(P)+\overrightarrow{PQ}=r_O(Q)$, luego la primera igualdad. Si $a=\overrightarrow{OO'}$, la fórmula de cambio de origen da

$$
\begin{aligned}
 r_{O'}(Q)-r_{O'}(P)
 &=\bigl(r_O(Q)-a\bigr)-\bigl(r_O(P)-a\bigr)\\
 &=r_O(Q)-r_O(P)
 =\overrightarrow{PQ}.
\end{aligned}
$$

Por tanto la diferencia entre posiciones es independiente del origen. $\square$

> **FPM-I-04-MP02 — Invariancia frente al origen**
> Una representación numérica de posición puede cambiar al trasladar el origen; un desplazamiento entre los mismos dos puntos no cambia por esa sola elección.

### 1.9. Ejemplo físico: dos personas describen el mismo desplazamiento

En un modelo unidimensional, asignemos respecto de $O$ las posiciones $x_O(P)=2\,\mathrm m$ y $x_O(Q)=7\,\mathrm m$. La diferencia es $5\,\mathrm m$ hacia el sentido positivo elegido. Si el nuevo origen se sitúa $a=3\,\mathrm m$ a la derecha de $O$, entonces

$$
x_{O'}(P)=-1\,\mathrm m,
\qquad x_{O'}(Q)=4\,\mathrm m,
$$

y

$$
x_{O'}(Q)-x_{O'}(P)=5\,\mathrm m.
$$

En este ejemplo sólo cambió el origen; los ejes conservaron orientación y unidad. Un cambio de base modificará también las **componentes** de los desplazamientos y se estudiará en §10.
No debemos inferir de esta invariancia del desplazamiento que todos los marcos físicos sean equivalentes desde el punto de vista dinámico. Ese problema requiere una teoría del movimiento y leyes físicas posteriores.

### 1.10. Prueba de estrés de las definiciones

- **¿Pueden coincidir los vectores de posición del mismo punto respecto de dos orígenes diferentes?** No: $r_{O'}(P)=r_O(P)-a$; si los vectores coinciden, entonces $a=0$ y, por D01, $O'=O$. La coincidencia de sus *componentes numéricas* en bases diferentes es una cuestión distinta que trataremos en §10.
- **¿Puede definirse $\overrightarrow{PQ}$ sin producto escalar?** Sí: D02 sólo necesita traslaciones.
- **¿Puede definirse una distancia sólo con D01?** No: falta una noción de longitud en $V$; se introducirá mediante el producto escalar.
- **¿Puede sumarse $P+v$?** Sí, da un punto.
- **¿Puede sumarse $P+Q$ sólo con D01?** No.

La pregunta de qué hace especial a una geometría **euclídea**, en vez de meramente afín, se responderá al introducir longitud y ángulos.

### 1.11. E001 — ¿Tiene sentido sumar dos puntos?

> **FPM-I-04-E001 · Diagnóstico lógico y contraejemplo**
> Un estudiante elige coordenadas en una recta y asigna a dos puntos $P,Q$ los números $2$ y $5$. Afirma: «su suma es el punto de coordenada $7$; es independiente del origen». Cambia el origen tres unidades hacia la derecha y examina la afirmación.

> **Solución desarrollada**
> Con el origen inicial, las coordenadas son $2$ y $5$ y su suma informal es $7$. Con el origen desplazado tres unidades, las coordenadas son $-1$ y $2$, cuya suma es $1$. Si $7$ describía un punto fijo, con el origen nuevo debería tener coordenada $4$, no $1$. La operación propuesta no respeta el cambio de origen y no pertenece a la estructura afín. En cambio, la diferencia pasa de $5-2=3$ a $2-(-1)=3$: el desplazamiento sí es invariante.

### 1.12. E002 — Cambiar el origen sin mover el objeto

> **FPM-I-04-E002 · Representación, formalización e invariancia**
> Respecto de un origen $O$, dos puntos de una recta tienen coordenadas $x_O(P)=-2\,\mathrm m$ y $x_O(Q)=4\,\mathrm m$. Se elige un origen $O'$ situado $5\,\mathrm m$ a la izquierda de $O$, sin invertir el eje. Calcula las coordenadas nuevas y el desplazamiento $\overrightarrow{PQ}$ en ambas descripciones.

> **Solución desarrollada**
> El desplazamiento del origen nuevo respecto del antiguo tiene componente $a=-5\,\mathrm m$. Por $x_{O'}=x_O-a$,
>
> $$
> x_{O'}(P)=3\,\mathrm m,
> \qquad x_{O'}(Q)=9\,\mathrm m.
> $$
>
> Las diferencias son
>
> $$
> 4-(-2)=6\,\mathrm m,
> \qquad 9-3=6\,\mathrm m.
> $$
>
> El vector desplazamiento es el mismo, y su componente permanece $+6\,\mathrm m$ porque no se cambió ni orientación ni unidad de la base.

### 1.13. E003 — Reconstruir un triángulo de desplazamientos

> **FPM-I-04-E003 · Prueba y transferencia**
> Si $\overrightarrow{AB}=u$ y $\overrightarrow{BC}=v$, expresa $\overrightarrow{AC}$, $\overrightarrow{CA}$ y $\overrightarrow{CB}$. Calcula luego la suma cerrada $\overrightarrow{AB}+\overrightarrow{BC}+\overrightarrow{CA}$ sin asignar coordenadas a los puntos.

> **Solución desarrollada**
> Por P01,
>
> $$
> \overrightarrow{AC}=u+v,
> \qquad \overrightarrow{CA}=-(u+v),
> \qquad \overrightarrow{CB}=-v.
> $$
>
> Por tanto,
>
> $$
> \overrightarrow{AB}+\overrightarrow{BC}+\overrightarrow{CA}
> =u+v-(u+v)=0.
> $$
>
> El vector total de un recorrido cerrado es nulo en un espacio afín: el cálculo sólo emplea las reglas de desplazamiento, no una figura ni un origen privilegiado.

### 1.14. Cierre conceptual: del lugar a la estructura

Hemos probado que una **posición** expresada por $r_O(P)$ depende de un origen, mientras que el desplazamiento $\overrightarrow{PQ}$ es geométricamente independiente de él. Ésta es la primera invariancia que necesitaremos para comparar observadores.

$$
\boxed{\text{puntos}\;\xrightarrow{\text{diferencia}}\;\text{vectores de desplazamiento}}
$$

En §2 construiremos sistemáticamente las operaciones afines y la geometría del paralelogramo. Sólo después introduciremos bases y coordenadas, y luego el producto escalar que permite hablar rigurosamente de longitudes y ángulos.

[^arnold-affine]: V. I. Arnold, *Mathematical Methods of Classical Mechanics*, 2.ª ed., Springer, 1989, parte I, cap. 1, §2.A «Notation», pp. 3–4.

---

[]{#fispm-t1-c04-s02}

[]{#fpm-i-04-s02}

## §2 — La estructura afín de los desplazamientos

### 2.1. Activación: ¿dónde está el punto medio si nadie fija el origen?

Dos marcas físicas ocupan puntos $P,Q\in\mathcal E$. Para indicar una marca intermedia podemos elegir momentáneamente un origen $O$ y calcular el promedio de sus vectores de posición:

$$
r_O(M)=\frac12r_O(P)+\frac12r_O(Q).
$$

Pero $O$ es una elección. ¿Cambiará el punto $M$ si otro observador coloca su origen en otro lugar? ¿Por qué este promedio sería admisible, mientras que la «suma de puntos» de §1 no lo era?
La respuesta exigirá comprobar la **dependencia de la construcción respecto del origen**; una ilustración de dos marcas sobre una regla sugiere dónde situar $M$, pero no demuestra esa independencia.

### 2.2. Recuperar la estructura disponible: trasladar, restar, componer

De D01 sabemos que la traslación $P+v$ es un punto cuando $v\in V$. De D02 y P01:

$$
\overrightarrow{PQ}+\overrightarrow{QR}=\overrightarrow{PR},
\qquad
\overrightarrow{QP}=-\overrightarrow{PQ}.
$$

Por consiguiente, sí tienen significado intrínseco

$$
P+u,\qquad Q-P:=\overrightarrow{PQ},
\qquad \overrightarrow{PQ}+\overrightarrow{QR},
$$

pero **no** $P+Q$. La estructura distingue expresiones por su tipo: punto, vector o escalar. Esta disciplina permite construir nuevos puntos sin identificar puntos y vectores.

### 2.3. Una receta tentativa con varios puntos

Sean $P_1,\ldots,P_n\in\mathcal E$ y $\lambda_1,\ldots,\lambda_n\in\mathbb R$. Si elegimos un origen auxiliar $O$, la receta

$$
A_O:=O+\sum_{i=1}^{n}\lambda_i\overrightarrow{OP_i}
$$

produce un punto: la suma del lado derecho pertenece a $V$ y puede trasladar $O$. Sin embargo, que la fórmula produzca **algún** punto no demuestra que produzca el **mismo** punto para todos los orígenes.

> Trabajo cognitivo
> Si trasladamos el origen por $a$, cada vector $\overrightarrow{OP_i}$ cambia en $-a$. ¿Cuántas veces aparece esa corrección en la suma? Antes de calcular, predice qué condición sobre los coeficientes puede cancelarla.

### 2.4. Proposición fundamental: el origen desaparece si y sólo si la suma es uno

> **FPM-I-04-P03 — Criterio de independencia del origen**
> Sean $P_1,\ldots,P_n\in\mathcal E$, $\lambda_i\in\mathbb R$ y
>
> $$
> A_O=O+\sum_i\lambda_i\overrightarrow{OP_i}.
> $$
>
> Si $O'=O+a$, entonces
>
> $$
> \boxed{\overrightarrow{A_OA_{O'}}=
> \left(1-\sum_i\lambda_i\right)a.}
> $$
>
> En particular, $A_O$ es independiente del origen elegido si $\sum_i\lambda_i=1$. Recíprocamente, como $\dim V=3$ y existen traslaciones no nulas, si $A_O$ es independiente de **toda** elección de origen, necesariamente $\sum_i\lambda_i=1$.

**Demostración.** La fórmula de §1 da $\overrightarrow{O'P_i}=\overrightarrow{OP_i}-a$. Sustituyendo en la receta:

$$
\begin{aligned}
A_{O'}
 &=O'+\sum_i\lambda_i\overrightarrow{O'P_i}\\
 &=(O+a)+\sum_i\lambda_i(\overrightarrow{OP_i}-a)\\
 &=A_O+\left(1-\sum_i\lambda_i\right)a.
\end{aligned}
$$

D02 identifica el vector que lleva $A_O$ a $A_{O'}$ con el término entre paréntesis. Si $\sum_i\lambda_i=1$, ese vector es cero para todo $a$. Inversamente, si es cero para todo $a$, escogemos $a\ne0$ y usamos que un escalar multiplicado por un vector no nulo sólo da cero cuando el escalar vale cero. Por tanto $1-\sum_i\lambda_i=0$. $\square$
**Lectura guiada.** La demostración tiene una estrategia (cambiar el origen), un mecanismo (cada vector de posición incorpora $-a$) y un cierre (unicidad del desplazamiento). No se necesitó ninguna fórmula de distancia.

### 2.5. Definir correctamente una combinación afín

> **FPM-I-04-D04 — Combinación afín de puntos**
> Dados $P_1,\ldots,P_n\in\mathcal E$ y escalares $\lambda_1,\ldots,\lambda_n$ con $\sum_i\lambda_i=1$, su **combinación afín** es el punto único
>
> $$
> \boxed{A=O+\sum_i\lambda_i\overrightarrow{OP_i},}
> $$
>
> donde $O$ es cualquier origen auxiliar. P03 asegura que el punto no depende de esa elección. La expresión abreviada $\sum_i\lambda_iP_i$ se permite **exclusivamente** después de declarar esta definición, y nunca como suma vectorial ordinaria de puntos.

Podemos usar un punto de la propia familia como origen. Para $O=P_1$:

$$
\boxed{A=P_1+\sum_{i=2}^{n}\lambda_i\overrightarrow{P_1P_i}.}
$$

Esta fórmula ya no necesita elegir un origen exterior a los puntos y facilita los cálculos conceptuales.

> **FPM-I-04-MP03 — Comprobar los tipos y los coeficientes**
> Antes de combinar puntos, verificar que los coeficientes sumen uno. Antes de sumar, verificar que los sumandos sean vectores; antes de trasladar, verificar que el primer objeto sea un punto y el segundo un vector.

### 2.6. Ejemplos, no-ejemplos y cambio de origen

Con dos puntos,

$$
A=(1-t)P+tQ=P+t\overrightarrow{PQ},
\qquad t\in\mathbb R,
$$

es una combinación afín válida para **todo** $t$, incluso $t<0$ o $t>1$. Por el contrario, la receta $P+Q$ interpretada como «dos posiciones sumadas» tendría coeficientes $1+1=2$; P03 muestra que la construcción basada en un origen variaría al trasladarlo.
Ejemplo de valores numéricos en una recta —usados sólo como comprobación de §1, no como definición de coordenadas generales—: si los valores respecto de un origen provisional son $0\,\mathrm m$ y $10\,\mathrm m$, entonces para $t=\tfrac34$ obtenemos $7.5\,\mathrm m$. Trasladando el origen $3\,\mathrm m$ hacia la derecha, los valores de los mismos puntos son $-3\,\mathrm m$ y $7\,\mathrm m$:

$$
\frac14(-3)+\frac34(7)=4.5\,\mathrm m.
$$

El nuevo valor es $4.5\,\mathrm m$ respecto del nuevo origen, equivalente a $7.5\,\mathrm m$ respecto del antiguo. Cambió la descripción numérica, no el punto obtenido.

### 2.7. Definir el baricentro sin confundirlo con un promedio de puntos

> **FPM-I-04-D05 — Baricentro de pesos de suma no nula**
> Dados puntos $P_i$ y pesos escalares $w_i$ compatibles entre sí, con suma $W=\sum_iw_i\ne0$, definimos el **baricentro** como la combinación afín
>
> $$
> \boxed{G=O+\sum_i\frac{w_i}{W}\overrightarrow{OP_i}.}
> $$
>
> Los coeficientes $w_i/W$ son adimensionales y suman uno; P03 garantiza que $G$ es independiente de $O$.

Si los pesos representan masas, deben expresarse en unidades compatibles antes de sumarlos. Para dos masas positivas $m_P,m_Q$, colocando $u=\overrightarrow{PQ}$:

$$
G=P+\frac{m_Q}{m_P+m_Q}u.
$$

Como $m_P,m_Q>0$, los coeficientes $m_P/(m_P+m_Q)$ y $m_Q/(m_P+m_Q)$ están entre $0$ y $1$; en §2.9 formalizaremos esta situación diciendo que $G$ pertenece al segmento afín entre $P$ y $Q$. Pero **D05 admite también pesos negativos** siempre que $W\ne0$; tal baricentro es una construcción geométrica y no debe interpretarse automáticamente como el centro de masa de cuerpos ordinarios.

### 2.8. ¿Qué sucede cuando la suma de los pesos es cero?

Si $W=0$, la normalización $w_i/W$ está indefinida. No es una dificultad de la calculadora ni una invitación a escoger arbitrariamente un origen. En cambio, el vector ponderado

$$
S_O:=\sum_iw_i\overrightarrow{OP_i}
$$

sí es independiente del origen, porque

$$
S_{O'}=S_O-Wa=S_O.
$$

Esto produce un **vector**, no un baricentro. Para $w_1=1$, $w_2=-1$, resulta $S_O=\overrightarrow{P_2P_1}$; no aparece un punto privilegiado.

> Prueba de hipótesis
> La condición $W\ne0$ es esencial para D05. Que una suma ponderada de vectores permanezca bien definida cuando $W=0$ no autoriza a llamarla punto.

### 2.9. Definir el segmento afín y su punto medio

> **FPM-I-04-D06 — Segmento afín y punto medio**
> Para $P,Q\in\mathcal E$, el segmento afín entre ellos es
>
> $$
> [P,Q]_{\mathrm{af}}:=\{P+t\overrightarrow{PQ}:0\le t\le1\}.
> $$
>
> Su **punto medio** es el punto
>
> $$
> \boxed{M(P,Q):=P+\tfrac12\overrightarrow{PQ}.}
> $$

La fórmula del punto medio equivale a la combinación afín de coeficientes $1/2,1/2$. Si $P=Q$, el segmento consta de un solo punto y el punto medio coincide con él. No estamos utilizando todavía una distancia: «mitad» significa aquí la mitad del **vector de desplazamiento**.
Cuando $t\in[0,1]$, los coeficientes $(1-t),t$ no sólo suman uno: son no negativos. Ésta es una **combinación convexa**. Si $t$ queda fuera del intervalo, la fórmula sigue siendo afín, pero el punto ya no pertenece al segmento definido, salvo el caso degenerado $P=Q$.

### 2.10. Comprobación: la interpolación no depende del origen

Sea $X_t=P+t\overrightarrow{PQ}$. Para cualquier origen $O$:

$$
r_O(X_t)=(1-t)r_O(P)+tr_O(Q).
$$

Esto se deduce de P01 y P02: $r_O(Q)-r_O(P)=\overrightarrow{PQ}$. La igualdad representa un punto en función de dos vectores de posición, pero **la definición intrínseca** sigue siendo $P+t\overrightarrow{PQ}$.
Además, para $s,t\in\mathbb R$,

$$
\boxed{\overrightarrow{X_sX_t}=(t-s)\overrightarrow{PQ}.}
$$

Se verifica trasladando $X_s$ por $(t-s)\overrightarrow{PQ}$ y usando la unicidad de D01. Si $P\ne Q$, dos parámetros distintos dan puntos distintos. Si $P=Q$, todos los parámetros producen el mismo punto: no hay unicidad de parámetro en el segmento degenerado.

### 2.11. Un paralelogramo construido con desplazamientos

Fijemos un punto $A$ y dos vectores $u,v\in V$. Construyamos sucesivamente

$$
B=A+u,\qquad D=A+v,\qquad C=A+u+v.
$$

Entonces

$$
\overrightarrow{AB}=u=\overrightarrow{DC},
\qquad
\overrightarrow{AD}=v=\overrightarrow{BC}.
$$

Ésta es la ley del paralelogramo **como identidad afín**, no como consecuencia de medir lados o ángulos. Los pares de lados opuestos representan el mismo desplazamiento libre. Cuando $u$ y $v$ no producen cuatro vértices geométricamente distintos, la construcción puede degenerar; no se necesita introducir todavía independencia lineal ni un producto escalar para que las identidades sean válidas.

### 2.12. Proposición: el paralelogramo y sus diagonales

> **FPM-I-04-P04 — Paralelogramo, desplazamientos y puntos medios**
> Sean $A,B,D\in\mathcal E$. Hay un único punto $C$ tal que
>
> $$
> \overrightarrow{BC}=\overrightarrow{AD}
> \quad\text{y}\quad
> \overrightarrow{DC}=\overrightarrow{AB}.
> $$
>
> Ese punto es $C=B+\overrightarrow{AD}$ y se caracteriza también por
>
> $$
> \boxed{M(A,C)=M(B,D).}
> $$
>
> Recíprocamente, si cuatro puntos $A,B,C,D$ satisfacen esa igualdad de puntos medios, cumplen las identidades de lados opuestos anteriores.

**Demostración.** Escribamos $u=\overrightarrow{AB}$ y $v=\overrightarrow{AD}$. El punto $C=A+u+v=B+v=D+u$ existe. Su unicidad se deduce de la unicidad del traslado de $B$ por $v$. Para los puntos medios:

$$
M(A,C)=A+\frac{u+v}{2}.
$$

Como $\overrightarrow{BD}=v-u$,

$$
M(B,D)=B+\frac{v-u}{2}
=A+u+\frac{v-u}{2}
=A+\frac{u+v}{2}.
$$

Para la recíproca supongamos $M(A,C)=M(B,D)$; tomando $A$ sólo como punto auxiliar y escribiendo $u=\overrightarrow{AB}$, $v=\overrightarrow{AD}$, $w=\overrightarrow{AC}$, se obtiene

$$
A+\frac{w}{2}=A+u+\frac{v-u}{2}
=A+\frac{u+v}{2}.
$$

La unicidad de traslación y la aritmética vectorial implican $w=u+v$. Por tanto $C=A+u+v=B+v=D+u$, que da las dos identidades. $\square$
**Autoexplicación.** El paralelogramo no se define mediante una ilustración de cuatro lados «aparentemente paralelos»; su construcción y su criterio de diagonales se obtienen de la acción afín. Las relaciones métricas sobre las longitudes de las diagonales quedan reservadas para §5.

### 2.13. Aplicación geométrica y frontera física

Tres marcas $A,B,D$ permiten definir una cuarta posición por dos rutas conceptualmente equivalentes:

$$
C=B+\overrightarrow{AD}=D+\overrightarrow{AB}.
$$

Si un trazado real no hace coincidir físicamente ambas marcas construidas, eso no refuta la identidad afín: invita a estudiar errores de realización, idealización, procedimiento o incertidumbre, conforme a FPM-I-03. La identidad pertenece al **modelo exacto**; el traslado y la localización físicos requieren procedimientos.
No estamos afirmando que cambiar el origen, recorrer un desplazamiento o representar un paralelogramo determine la evolución temporal de un cuerpo. La cinemática comienza en FPM-I-05.

### 2.14. Prueba de estrés: baricentro, segmento y promedios

1. Si $\lambda_1+\lambda_2=1$ pero uno es negativo, la combinación es afín, aunque no necesariamente pertenece al segmento.
2. Si dos pesos tienen suma nula, D05 no define un baricentro; puede quedar definido un vector ponderado.
3. Para puntos coincidentes $P=Q$, el punto medio existe y coincide con ellos; el parámetro del segmento deja de ser único.
4. En un paralelogramo degenerado, P04 sigue siendo verdadero; no supone longitudes ni ángulos.
5. No escribiremos $\tfrac12(P+Q)$: contiene una suma de puntos que D01 no define. La expresión correcta es $M(P,Q)=P+\tfrac12\overrightarrow{PQ}$, o bien la combinación afín definida en D04.

> Lectura inversa
> Dado un punto $G$ descrito como «centro», reconstruye qué pesos se eligieron, si suman un valor no nulo, qué fenómeno representan y si la construcción es geométrica o metrológica.

[]{#fispm-t1-c04-e0004}

### 2.15. Ejercicio FPM-I-04-E004 — Baricentro con un origen auxiliar

> **Función cognitiva:** `modelización → traducción vectorial → prueba de invariancia`.
>
> Sean $P,Q,R\in\mathcal E$ y $u=\overrightarrow{PQ}$, $v=\overrightarrow{PR}$. Tres pesos de la misma unidad son $2,3,1$.
>
> 1. Calcula el baricentro $G$ mediante D05, con $P$ como origen auxiliar.
> 2. Repite el cálculo con un origen genérico $O$ y demuestra que describe el mismo punto.
> 3. Explica por qué el cociente de cada peso respecto de la suma no conserva la unidad de los pesos.

> **Solución desarrollada**
>
> La suma es $W=6$ y los coeficientes afines son $\tfrac26,\tfrac36,\tfrac16$. Con $P$ como origen auxiliar, $\overrightarrow{PP}=0$:
>
> $$
> \boxed{G=P+\frac12u+\frac16v.}
> $$
>
> Para otro origen $O$, escribimos $r_O(Q)=r_O(P)+u$ y $r_O(R)=r_O(P)+v$. Entonces
>
> $$
> \begin{aligned}
> r_O(G)&=\frac26r_O(P)+\frac36r_O(Q)+\frac16r_O(R)\\
> &=r_O(P)+\frac12u+\frac16v.
> \end{aligned}
> $$
>
> Dado que el último vector traslada $P$ al punto obtenido antes, las dos descripciones coinciden. Cada razón $w_i/W$ es adimensional, porque numerador y denominador tienen la misma unidad. La positividad de los pesos permite interpretarlos como masas **si** se declara un modelo físico adecuado; no convierte por sí sola esta identidad en una medición del centro de masa.

[]{#fispm-t1-c04-e0005}

### 2.16. Ejercicio FPM-I-04-E005 — Construir y auditar un paralelogramo

> **Función cognitiva:** `construcción → demostración → detección de errores`.
>
> Dados un punto $A$ y desplazamientos $u,v$, define $B=A+u$ y $D=A+v$.
>
> 1. Construye el único $C$ que cumple las dos igualdades de lados opuestos de P04.
> 2. Demuestra que ambas diagonales tienen el mismo punto medio.
> 3. Un compañero propone $C'=A+u-v$. Determina para qué $v$ esa propuesta es correcta.

> **Solución desarrollada**
>
> Por construcción y P04,
>
> $$
> \boxed{C=A+u+v=B+v=D+u.}
> $$
>
> Los puntos medios de $AC$ y $BD$ son, respectivamente,
>
> $$
> M(A,C)=A+\frac{u+v}{2},
> $$
>
> $$
> M(B,D)=B+\frac{v-u}{2}
> =A+\frac{u+v}{2}.
> $$
>
> Para que $C'=C$ se requiere $u-v=u+v$, o $2v=0$. Sobre un espacio vectorial real esto equivale a $v=0$: el error sólo desaparece en el caso degenerado $D=A$. Confundir un vector con su opuesto cambia la construcción, aunque un dibujo mal orientado pueda ocultarlo.

### 2.17. Cierre y red matemática

La estructura afín permite obtener nuevos puntos **sin declarar un origen absoluto**. Las operaciones que acabamos de construir se organizan así:

$$
\boxed{\begin{gathered}
\text{puntos y desplazamientos}\ \xrightarrow{\text{D01--D02}}\ \text{traslaciones}\\
\xrightarrow{\text{P03}}\ \text{combinaciones afines y baricentros}\\
\xrightarrow{\text{D06, P04}}\ \text{segmentos y paralelogramos}.
\end{gathered}}
$$

No obstante, aún no sabemos expresar **cualquier vector de manera única mediante unas direcciones elegidas**. Ésa será la pregunta de §3 — *Vectores, independencia y bases*. La métrica euclídea seguirá esperando hasta §5.

---

[]{#fispm-t1-c04-s03}

[]{#fpm-i-04-s03}

## §3 — Vectores, independencia y bases

### 3.1. Activación: una flecha, distintas descripciones

Dos personas registran el mismo desplazamiento físico. Una escoge tres desplazamientos de referencia; la otra escoge otros tres. Sus listas de números pueden diferir sin que cambie el desplazamiento. ¿Cuándo una lista describe un vector de manera completa y sin ambigüedad?
La §1 enseñó que $\overrightarrow{PQ}\in V$ no es ni $P$ ni $Q$; la §2 mostró que las sumas y múltiplos escalares corresponden a **vectores**, mientras que combinar puntos exige coeficientes que sumen uno. Ahora estudiaremos cómo expresar cualquier elemento de $V$ a partir de vectores de referencia.
La dificultad tiene dos mitades distintas:

- **Existencia:** ¿nuestros vectores de referencia alcanzan para construir cualquier desplazamiento?
- **Unicidad:** ¿cada desplazamiento posee una única receta en términos de ellos?

Un sistema puede satisfacer una mitad y fallar en la otra.

> Activación
> Si tenemos tres instrucciones de desplazamiento pero una de ellas es la suma de las otras dos, ¿obtenemos información nueva? ¿Podrían dos listas numéricas diferentes representar la misma flecha?

### 3.2. La estructura vectorial ya disponible

El espacio real $V$ dispone de una suma $u+v$ y una multiplicación por escalares $\lambda u$. Emplearemos las leyes vectoriales conocidas: asociatividad y conmutatividad de la suma, vector cero, opuestos y distributividad. Para $P\in\mathcal E$, la expresión $P+v$ sigue representando la traslación de un **punto** por un **vector**.
Por P01, una sucesión de desplazamientos satisface

$$
\overrightarrow{PQ}+\overrightarrow{QR}=\overrightarrow{PR}.
$$

Que podamos componer flechas no significa que exista una suma intrínseca de puntos. Las combinaciones lineales que definiremos pertenecen siempre a $V$.
La dimensión $\dim V=3$ forma parte del modelo del capítulo. Esto significa que existe alguna terna de vectores que constituye una base; **no** significa que cualquier terna no nula lo sea. No necesitamos una métrica para comprender esta dimensión algebraica.

### 3.3. Definir: combinación lineal y espacio generado

> **FPM-I-04-D07 — Combinación lineal y subespacio generado**
> Para vectores $v_1,\ldots,v_k\in V$ y escalares $a_1,\ldots,a_k\in\mathbb R$, la expresión
>
> $$
> a_1v_1+\cdots+a_kv_k
> $$
>
> es una **combinación lineal**. El conjunto de todas las combinaciones lineales de la familia es
>
> $$
> \operatorname{span}(v_1,\ldots,v_k)
> :=\left\{\sum_{i=1}^{k}a_iv_i:a_i\in\mathbb R\right\}.
> $$
>
> Diremos que la familia **genera** $V$ si su espacio generado coincide con $V$.

La familia de un solo vector no nulo genera los vectores de la forma $av$; dos vectores generan los de la forma $au+bw$. Sólo si la familia genera $V$ podremos representar **todo** desplazamiento del modelo.

> ¿Por qué se llama subespacio?
> La combinación con todos los coeficientes nulos produce $0$. Si $x=\sum a_iv_i$ e $y=\sum b_iv_i$, entonces $x+y=\sum(a_i+b_i)v_i$ y $cx=\sum(ca_i)v_i$. Así, el conjunto generado contiene el cero y es cerrado bajo suma y multiplicación escalar. No hemos usado longitudes ni ángulos.

### 3.4. Dos pruebas de estrés para la generación

**Familia demasiado pequeña.** Si $u\ne0$, la familia $(u)$ puede representar $2u$ o $-u$, pero no tiene por qué representar cualquier vector de $V$. En un espacio de dimensión tres, su espacio generado es estrictamente menor que $V$.
**Familia con instrucciones redundantes.** Añadir $u+v$ a $(u,v)$ no aumenta lo generado:

$$
\operatorname{span}(u,v,u+v)=\operatorname{span}(u,v).
$$

En efecto, toda combinación $au+bv+c(u+v)$ se reescribe como $(a+c)u+(b+c)v$, y las combinaciones de $(u,v)$ se obtienen tomando $c=0$.
La segunda familia tiene más elementos, pero no permite construir vectores adicionales. La cantidad de instrucciones no mide por sí sola la información geométrica.

### 3.5. Definir: independencia lineal

> **FPM-I-04-D08 — Independencia lineal**
> Una familia $(v_1,\ldots,v_k)$ es **linealmente independiente** si
>
> $$
> \sum_{i=1}^{k}a_iv_i=0
> \quad\Longrightarrow\quad
> a_1=\cdots=a_k=0.
> $$
>
> Si existen coeficientes, no todos nulos, que producen $0$, la familia es **linealmente dependiente**.

¿Por qué estudiar precisamente una combinación que vale cero? Porque una relación de este tipo permite modificar los coeficientes de una representación sin cambiar el vector obtenido.
Algunos no-ejemplos inmediatos: una familia que contiene $0$ es dependiente; una familia en la que se repite un vector es dependiente; la terna $(u,v,u+v)$ es dependiente, pues

$$
u+v-(u+v)=0.
$$

En particular, que *todos* los vectores de una familia sean no nulos no basta para garantizar independencia.

### 3.6. La pregunta correcta: ¿cuántas recetas tiene el mismo vector?

Una familia dependiente proporciona una relación

$$
\sum_i c_iv_i=0
$$

con algún $c_i\ne0$. Si $w=\sum_i a_iv_i$, entonces también

$$
w=\sum_i(a_i+tc_i)v_i
$$

para cualquier $t\in\mathbb R$. Si $t\ne0$, la segunda lista de coeficientes es distinta de la primera.
Por el contrario, si una familia es independiente, dos listas que representen el mismo vector han de coincidir. Este razonamiento merece una demostración general.

### 3.7. Proposición: independencia y unicidad en el espacio generado

> **FPM-I-04-P05 — Caracterización de la independencia por unicidad**
> Para una familia finita $(v_1,\ldots,v_k)$, son equivalentes:
>
> 1. La familia es linealmente independiente.
> 2. Cada vector de $\operatorname{span}(v_1,\ldots,v_k)$ tiene **una única** representación como $\sum_i a_iv_i$.

**Demostración.** Supongamos independencia y que un vector admite dos expresiones:

$$
\sum_i a_iv_i=\sum_i b_iv_i.
$$

Restando,

$$
\sum_i(a_i-b_i)v_i=0.
$$

Por independencia, $a_i-b_i=0$ para cada $i$; las listas son iguales.
Recíprocamente, supongamos unicidad dentro del espacio generado. El vector $0$ admite la representación con todos los coeficientes nulos. Si $\sum_i c_iv_i=0$, ésta es otra representación de $0$ y, por unicidad, necesariamente $c_i=0$ para todos los índices. La familia es independiente. $\square$
**Lectura guiada.** La estrategia es convertir «dos representaciones» en «una relación que da cero»; la técnica es restarlas; el mecanismo es aplicar D08. La recíproca prueba la definición examinando exclusivamente las representaciones del vector cero.

### 3.8. Definir: base

> **FPM-I-04-D09 — Base de un espacio vectorial**
> Una familia ordenada $B=(e_1,\ldots,e_n)$ es una **base** de $V$ si cumple simultáneamente:
>
> - **generación:** $\operatorname{span}(e_1,\ldots,e_n)=V$;
> - **independencia:** $\sum_i a_ie_i=0$ sólo cuando todos los $a_i$ son cero.
>
> En nuestro modelo tridimensional consideraremos bases ordenadas $B=(e_1,e_2,e_3)$.

El orden es necesario al escribir componentes: intercambiar $e_1$ y $e_2$ cambia el orden de los números, aunque la colección de vectores siga siendo una base.
Un conjunto que sólo genera puede contener instrucciones redundantes. Una familia independiente que no genera no describe todos los desplazamientos. **Una base resuelve los dos problemas a la vez.**

### 3.9. Proposición: el teorema fundamental de las representaciones en una base

> **FPM-I-04-P06 — Existencia y unicidad de los coeficientes en una base**
> Sea $B=(e_1,\ldots,e_n)$ una familia finita de vectores. Es una base de $V$ **si y sólo si** cada $v\in V$ posee una única representación
>
> $$
> \boxed{v=\sum_{i=1}^{n}v^ie_i.}
> $$

**Demostración.** Si $B$ es una base, la condición de generación asegura la existencia para todo $v$. P05, aplicada a la independencia de $B$, asegura la unicidad.
Inversamente, si cada $v\in V$ posee una representación de la forma indicada, $B$ genera $V$. La unicidad para todo $v$, y en particular para los vectores del espacio generado, implica independencia por P05. Ambas condiciones de D09 se cumplen. $\square$

> **FPM-I-04-MP04 — Separar existencia de unicidad**
> Antes de llamar *base* a una familia, demostrar por separado que todo vector se puede construir con ella y que no existen dos listas distintas de coeficientes para un mismo vector. Una sola comprobación numérica no sustituye ninguna de estas pruebas.

### 3.10. Definir: las componentes de un vector

> **FPM-I-04-D10 — Componentes relativas a una base**
> Sea $B=(e_1,e_2,e_3)$ una base ordenada de $V$. Para el vector único
>
> $$
> v=v^1e_1+v^2e_2+v^3e_3,
> $$
>
> definimos su columna de **componentes en $B$** como
>
> $$
> \boxed{[v]_B=\begin{pmatrix}v^1\\v^2\\v^3\end{pmatrix}.}
> $$

P06 garantiza que esta notación no es ambigua. La columna es un elemento de $\mathbb R^3$; $v$ sigue siendo un elemento de $V$. La igualdad $v=[v]_B$ **no** es una igualdad de objetos tipados como hemos definido, aunque una identificación dependiente de $B$ permita realizar cálculos con la columna.

> Punto, vector y columna
> $P\in\mathcal E$, $\overrightarrow{PQ}\in V$ y $[\overrightarrow{PQ}]_B\in\mathbb R^3$ son objetos distintos. Un origen hará posible representar puntos mediante vectores de posición; esa operación se estudiará sistemáticamente en §4.

### 3.11. Proposición: la aplicación de componentes respeta las operaciones

> **FPM-I-04-P07 — Correspondencia lineal de componentes**
> Fijada una base $B=(e_1,e_2,e_3)$, la aplicación
>
> $$
> C_B:V\longrightarrow\mathbb R^3,
> \qquad C_B(v)=[v]_B
> $$
>
> es biyectiva y lineal. En particular,
>
> $$
> \boxed{[au+bv]_B=a[u]_B+b[v]_B.}
> $$

**Demostración.** Dados $v=\sum_i v^ie_i$ y $w=\sum_i w^ie_i$, las leyes vectoriales dan

$$
av+bw=\sum_i(av^i+bw^i)e_i.
$$

Por la unicidad de P06, sus componentes son precisamente $(av^i+bw^i)_{i=1}^3$. Esto prueba la linealidad. Para cada columna $(c^1,c^2,c^3)^{\mathsf T}$, el vector $\sum_i c^ie_i$ tiene esa columna: $C_B$ es sobreyectiva. Si dos vectores tienen igual columna, sus expresiones en la base son idénticas y los vectores coinciden: $C_B$ es inyectiva. $\square$
**Autoexplicación.** Una columna es útil porque conserva la suma y la multiplicación escalar. Pero su forma numérica depende de la base; la correspondencia se define **después** de elegir $B$, no antes.

### 3.12. Ejemplo construido: una base no tiene por qué ser la primera que vemos

Sea $E=(e_1,e_2,e_3)$ una base conocida de un espacio de dimensión tres. Definamos

$$
b_1=e_1,\qquad
b_2=e_1+e_2,\qquad
b_3=e_1+e_2+e_3.
$$

Para un vector cualquiera

$$
v=ae_1+be_2+ce_3,
$$

buscamos escalares $x,y,z$ tales que $v=xb_1+yb_2+zb_3$. Al reordenar:

$$
xb_1+yb_2+zb_3
=(x+y+z)e_1+(y+z)e_2+ze_3.
$$

La unicidad de las componentes relativas a $E$ obliga a resolver

$$
x+y+z=a,\qquad y+z=b,\qquad z=c.
$$

El sistema se despeja desde la última ecuación:

$$
\boxed{z=c,\qquad y=b-c,\qquad x=a-b.}
$$

Existe una solución para todo $v$ y es única; por P06, $B=(b_1,b_2,b_3)$ es una base. **No hemos utilizado determinantes, producto escalar ni ortogonalidad.**
Para $v=2e_1+3e_2+4e_3$:

$$
[v]_E=\begin{pmatrix}2\\3\\4\end{pmatrix},
\qquad
[v]_B=\begin{pmatrix}-1\\-1\\4\end{pmatrix}.
$$

Las columnas son diferentes, pero ambas reconstruyen el mismo vector. La teoría general de cambios de base, incluida su convención matricial, aparecerá en §10.

### 3.13. Contraejemplo: tres vectores que no forman base

Con $E$ como antes, elijamos

$$
u=e_1+e_2,\qquad w=e_2+e_3,
\qquad z=u+w=e_1+2e_2+e_3.
$$

Los tres vectores son no nulos, pero

$$
u+w-z=0
$$

es una relación no trivial. Además, para el propio vector $z$ tenemos dos representaciones:

$$
z=0u+0w+1z=1u+1w+0z.
$$

No son componentes legítimas de una base, porque la unicidad falla. Tampoco generan todo $V$: si $e_1=\alpha u+\beta w$, la comparación de coeficientes en $E$ daría $\alpha=1$, $\alpha+\beta=0$ y $\beta=0$, un sistema contradictorio.

> Error plausible
> «Tres vectores no nulos en un espacio tridimensional forman automáticamente una base». Es falso: el problema no es contar flechas, sino verificar independencia y generación. El contraejemplo falla en ambas condiciones.

### 3.14. Cambiar la escala de un vector de referencia

Si $B=(e_1,e_2,e_3)$ es una base y $s\in\mathbb R$ con $s\ne0$, entonces $B'=(se_1,e_2,e_3)$ también es una base: toda representación $v=v^1e_1+v^2e_2+v^3e_3$ se reescribe unívocamente como

$$
v=\frac{v^1}{s}(se_1)+v^2e_2+v^3e_3.
$$

Por tanto,

$$
\boxed{[v]_{B'}=
\begin{pmatrix}v^1/s\\v^2\\v^3\end{pmatrix}.}
$$

Este caso particular enseña un fenómeno esencial: cuando se hace $s$ veces mayor el vector de referencia, el coeficiente correspondiente se divide por $s$. No hemos cambiado $v$; hemos cambiado la **escala de su descripción**. Si el contexto físico asigna unidades a los desplazamientos de referencia, las componentes y las unidades se interpretan coherentemente según la convención declarada.

### 3.15. La interpretación física y sus límites

La interpretación dimensional de las componentes depende de la convención declarada. Si los vectores de la base representan desplazamientos de referencia con dimensión de longitud, los coeficientes $v^i$ son números adimensionales; si se trabaja con direcciones adimensionales, las componentes pueden portar la unidad de longitud. En ningún caso los coeficientes solos revelan cuál es la base de referencia ni qué convención de unidades se adoptó.
No hemos probado que una base sea ortonormal: ni siquiera hemos definido todavía los ángulos y las longitudes. Tampoco se sigue de D09 que los vectores elegidos representen un marco físico inercial o que el espacio físico real satisfaga exactamente el modelo euclídeo. Son cuestiones posteriores.
Al igual que en FPM-I-03, los valores medidos que se empleen para realizar una representación física tendrán su propia incertidumbre; las igualdades algebraicas de P05–P07 no son resultados experimentales.

[]{#fispm-t1-c04-e0006}

### 3.16. Ejercicio FPM-I-04-E006 — Tres vectores, pero ninguna base

> **Función pedagógica:** diagnóstico de independencia y generación, prueba de estrés de la definición, reconstrucción de una representación.
>
> Sea $E=(e_1,e_2,e_3)$ una base conocida de $V$ y definamos
>
> $$
> u=e_1+e_2,\qquad w=e_2+e_3,\qquad z=u+w.
> $$
>
> 1. Demuestra que $(u,w,z)$ no es independiente.
> 2. Exhibe dos listas de coeficientes que representen $z$.
> 3. Demuestra, sin determinantes, que la familia tampoco genera $V$.
> 4. Explica por qué añadir $z$ a $(u,w)$ no soluciona el problema.

> **Solución desarrollada**
>
> 1. $u+w-z=0$ proporciona coeficientes $(1,1,-1)$ no todos nulos: la familia es dependiente.
> 2. $z=1u+1w+0z=0u+0w+1z$. La representación no es única.
> 3. Si existieran $\alpha,\beta,\gamma$ con $e_1=\alpha u+\beta w+\gamma z$, podríamos absorber $\gamma z$ y escribir $e_1=au+bw$. Esto daría
>
> $$
> e_1=ae_1+(a+b)e_2+be_3.
> $$
>
> Como $E$ es base, habría de cumplirse $a=1$, $a+b=0$ y $b=0$, imposible. Por tanto $e_1$ no pertenece al espacio generado.
> 4. Por definición $z=u+w$ ya pertenecía a $\operatorname{span}(u,w)$: no añade una dirección algebraica nueva ni repara la redundancia.

[]{#fispm-t1-c04-e0007}

### 3.17. Ejercicio FPM-I-04-E007 — Probar una base y leer sus componentes

> **Función pedagógica:** construcción, prueba de existencia y unicidad, traducción símbolo–representación.
>
> Sea $E=(e_1,e_2,e_3)$ una base de $V$, y sean
>
> $$
> b_1=e_1,\quad b_2=e_1+e_2,\quad b_3=e_1+e_2+e_3.
> $$
>
> 1. Demuestra que $B=(b_1,b_2,b_3)$ es una base sin invocar determinantes.
> 2. Para $v=2e_1+3e_2+4e_3$, calcula $[v]_B$ y verifica reconstruyendo $v$.
> 3. Explica por qué la diferencia entre $[v]_E$ y $[v]_B$ no implica un cambio físico del vector.

> **Solución desarrollada**
>
> 1. Para $v=ae_1+be_2+ce_3$, una combinación $xb_1+yb_2+zb_3$ reproduce $v$ si y sólo si $x+y+z=a$, $y+z=b$ y $z=c$. La única solución es
>
> $$
> (x,y,z)=(a-b,b-c,c).
> $$
>
> Existe y es única para todo vector; P06 prueba que $B$ es base.
> 2. Sustituyendo $(a,b,c)=(2,3,4)$:
>
> $$
> [v]_B=(-1,-1,4)^{\mathsf T}.
> $$
>
> Reconstruimos:
>
> $$
> -b_1-b_2+4b_3
> =-e_1-(e_1+e_2)+4(e_1+e_2+e_3)
> =2e_1+3e_2+4e_3=v.
> $$
>
> 3. La identidad de reconstrucción muestra que ambas columnas nombran el mismo elemento de $V$. Cambian los vectores que sirven como referencia, no el desplazamiento físico.

### 3.18. Cierre: de una base vectorial a las coordenadas de los puntos

Ya tenemos una cadena demostrada:

$$
\boxed{
\text{generación + independencia}
\Longleftrightarrow
\text{existencia y unicidad de componentes}.
}
$$

P05–P07 justifican la representación de **vectores** mediante columnas. Aún no hemos asignado una columna a un punto $P$, porque para hacerlo debemos elegir además un origen $O$ y representar el vector $r_O(P)=\overrightarrow{OP}$.
El siguiente paso, **§4 — Coordenadas afines y marcos cartesianos**, incorporará esa elección adicional y distinguirá sistemáticamente punto, vector de posición, desplazamiento y terna de componentes.

---

[]{#fispm-t1-c04-s04}

[]{#fpm-i-04-s04}

## §4 — Coordenadas afines y marcos cartesianos

### 4.1. Activación: tres números, ¿qué describen?

Un plano de una sala señala que un sensor ocupa la posición «$(2,-1,3)$». Esa información no determina por sí sola una ubicación física: faltan un origen, tres vectores de referencia ordenados y las convenciones de escala que permiten interpretar los números.[^shankar-axes] Si otro plano elige el origen en la puerta en vez de una esquina, el mismo sensor recibe otra terna sin moverse.
§1 distinguió los puntos de los vectores; §2 construyó combinaciones afines; §3 demostró que una base permite representar **vectores** por columnas únicas. Ahora añadiremos la elección que faltaba para representar **puntos**.

> Activación
> Si dos registros contienen la misma terna $(2,-1,3)$, ¿qué deberíamos comprobar antes de concluir que se refieren al mismo lugar? ¿Puede una diferencia de ternas ser físicamente significativa aunque ambas ternas por separado dependan del origen?

### 4.2. Inventario de objetos: no intercambiar tipos

La geometría disponible distingue:

- un punto $P\in\mathcal E$;
- un vector de desplazamiento $v\in V$;
- su columna $[v]_B\in\mathbb R^3$, una vez elegida una base $B$;
- el vector de posición $r_O(P)=\overrightarrow{OP}\in V$, una vez elegido un origen $O$.

La expresión $P=v$ no pertenece a nuestra estructura. Tampoco hay una terna de números atribuida canónicamente a $P$. En cambio, la cadena

$$
P\longmapsto r_O(P)\longmapsto [r_O(P)]_B
$$

está bien definida cuando se fijan $O$ y $B$. Cada flecha representa una **decisión matemática distinta**; no hay medición ni movimiento implícito en la elección.

### 4.3. Definir el marco afín

> **FPM-I-04-D11 — Marco afín ordenado**
> Un **marco afín** de $\mathcal E$ es un par
>
> $$
> \boxed{\mathfrak F=(O,B),\qquad B=(e_1,e_2,e_3),}
> $$
>
> donde $O\in\mathcal E$ es un punto elegido como origen y $B$ es una base ordenada del espacio vectorial $V$ de desplazamientos.

La elección de $O$ fija la referencia para las posiciones; la de $B$ fija cómo se descomponen los desplazamientos. En este punto no se exige que los $e_i$ tengan la misma longitud ni que formen ángulos rectos: tales expresiones todavía no están definidas.
**No-ejemplos.** Un origen aislado no es un marco completo. Una terna dependiente tampoco lo es, aunque dibujemos tres flechas y la llamemos «tres ejes». Una base sin origen sirve para representar vectores, pero todavía no proporciona coordenadas de puntos.

### 4.4. Definir las coordenadas de un punto

> **FPM-I-04-D12 — Coordenadas afines de un punto**
> Fijado $\mathfrak F=(O,B)$, las **coordenadas afines** de $P$ son la columna única
>
> $$
> \boxed{x_{\mathfrak F}(P):=[\overrightarrow{OP}]_B
> =\begin{pmatrix}x^1\\x^2\\x^3\end{pmatrix}.}
> $$
>
> Por la definición de componentes y P06, el punto satisface la reconstrucción
>
> $$
> \boxed{P=O+x^1e_1+x^2e_2+x^3e_3.}
> $$

En la última fórmula, $O+v$ es la acción afín definida en D01; no estamos sumando cuatro puntos. Las coordenadas $x^i$ son escalares relativos a la base **declarada**, no propiedades intrínsecas del punto.

> **FPM-I-04-MP05 — Declarar el marco y las unidades**
> Toda terna que se interprete como posición debe ir acompañada de la elección del origen, la base ordenada y el convenio de unidades. Distinguir explícitamente $P$, $r_O(P)$ y $x_{\mathfrak F}(P)$; no inferir desplazamiento real de un cambio de etiqueta.

### 4.5. La proposición de existencia y unicidad para puntos

> **FPM-I-04-P08 — Coordenadas afines como correspondencia biyectiva**
> Para cada marco afín fijo $\mathfrak F=(O,B)$, la aplicación
>
> $$
> x_{\mathfrak F}:\mathcal E\longrightarrow\mathbb R^3,
> \qquad P\longmapsto [\overrightarrow{OP}]_B
> $$
>
> es biyectiva. Su inversa es
>
> $$
> \boxed{(c^1,c^2,c^3)^{\mathsf T}\longmapsto
> O+c^1e_1+c^2e_2+c^3e_3.}
> $$

**Demostración.** Para una columna $c$, la combinación $v=\sum_i c^ie_i$ es un vector y D01 construye el punto $P=O+v$. Por D02, $\overrightarrow{OP}=v$, y por P06 sus componentes son precisamente $c$: la aplicación es sobreyectiva. Si dos puntos $P,Q$ poseen la misma columna, P07 y la unicidad de las componentes dan $\overrightarrow{OP}=\overrightarrow{OQ}$. D01 implica entonces $P=O+\overrightarrow{OP}=O+\overrightarrow{OQ}=Q$: es inyectiva. $\square$
**Lectura guiada.** Para existir una posición dada la terna, convertimos la terna en un vector y trasladamos el origen; para probar unicidad, deshacemos ambas operaciones. Ésta es una biyección que **depende del marco**, no una identidad entre los conjuntos $\mathcal E$ y $\mathbb R^3$.

### 4.6. El origen y los vectores de referencia tienen coordenadas sencillas

De $\overrightarrow{OO}=0$ y P07 se deduce

$$
x_{\mathfrak F}(O)=\begin{pmatrix}0\\0\\0\end{pmatrix}.
$$

Los puntos $E_i:=O+e_i$ tienen las columnas unitarias habituales:

$$
x_{\mathfrak F}(E_1)=\begin{pmatrix}1\\0\\0\end{pmatrix},\quad
x_{\mathfrak F}(E_2)=\begin{pmatrix}0\\1\\0\end{pmatrix},\quad
x_{\mathfrak F}(E_3)=\begin{pmatrix}0\\0\\1\end{pmatrix}.
$$

Estas columnas no afirman que los vectores de referencia midan un metro, que sean perpendiculares o que tengan igual longitud. Sólo codifican su **papel algebraico en la base**.

### 4.7. Definir los ejes afines sin presuponer ángulos rectos

> **FPM-I-04-D13 — Ejes afines de un marco**
> Para $\mathfrak F=(O,(e_1,e_2,e_3))$, el eje afín asociado a $e_i$ es el conjunto de puntos
>
> $$
> \boxed{\mathcal A_i=\{O+te_i:t\in\mathbb R\}.}
> $$

Los tres ejes concurren en $O$ y están asociados a desplazamientos linealmente independientes. La construcción es algebraicamente legítima incluso si en una ilustración sus direcciones parecen oblicuas.
**Precisión terminológica.** A menudo se llama «sistema cartesiano» a un origen con ejes perpendiculares y una escala declarada. Aquí hemos construido la parte **afín** del sistema de coordenadas; podremos exigir ortogonalidad sólo tras definir producto escalar (§5) y construir bases ortonormales (§7). Por ahora, «marco cartesiano» en el título señala el objetivo del capítulo, no una propiedad métrica ya demostrada.

### 4.8. Proposición: restar coordenadas recupera un desplazamiento

> **FPM-I-04-P09 — Diferencias de coordenadas**
> Fijado $\mathfrak F=(O,B)$, para todos $P,Q\in\mathcal E$ se tiene
>
> $$
> \boxed{[\overrightarrow{PQ}]_B
> =x_{\mathfrak F}(Q)-x_{\mathfrak F}(P).}
> $$
>
> Además, para $v\in V$,
>
> $$
> \boxed{x_{\mathfrak F}(P+v)
> =x_{\mathfrak F}(P)+[v]_B.}
> $$

**Demostración.** P02 establece que $\overrightarrow{PQ}=\overrightarrow{OQ}-\overrightarrow{OP}$. Aplicamos la linealidad de la correspondencia de componentes P07 y la definición D12 para obtener la primera identidad. Para la segunda, la ley del triángulo da $\overrightarrow{O(P+v)}=\overrightarrow{OP}+v$; P07 vuelve a convertir la suma vectorial en suma de columnas. $\square$
La diferencia de las columnas representa el **desplazamiento entre los puntos**, no una «resta física de posiciones» realizada sobre los objetos. El orden importa:

$$
[\overrightarrow{QP}]_B
=x_{\mathfrak F}(P)-x_{\mathfrak F}(Q)
=-[\overrightarrow{PQ}]_B.
$$

### 4.9. Ejemplo físico: ubicar un detector y desplazarlo

Fijamos un origen en una marca del laboratorio y tres desplazamientos de referencia ordenados $B=(e_1,e_2,e_3)$. Sea el punto del detector

$$
P=O+2e_1-e_2+3e_3.
$$

Su columna es

$$
x_{\mathfrak F}(P)=\begin{pmatrix}2\\-1\\3\end{pmatrix}.
$$

Si trasladamos **físicamente el detector en el modelo** mediante $v=-e_1+2e_2$, el nuevo punto es $Q=P+v$. P09 proporciona

$$
x_{\mathfrak F}(Q)
=\begin{pmatrix}2\\-1\\3\end{pmatrix}
+\begin{pmatrix}-1\\2\\0\end{pmatrix}
=\begin{pmatrix}1\\1\\3\end{pmatrix}.
$$

Aquí sí cambió el punto modelado. La comparación con el próximo caso —un cambio de **origen** sin movimiento— es la prueba conceptual importante.

### 4.10. Cambiar sólo el origen, conservando la base

Supongamos que elegimos $O'=O+a$ con $a\in V$, pero conservamos exactamente la base ordenada $B$. Los marcos son

$$
\mathfrak F=(O,B),\qquad \mathfrak F'=(O',B).
$$

§1 ya demostró para el vector de posición que

$$
r_{O'}(P)=r_O(P)-a.
$$

La novedad consiste en expresar esa ley para las **columnas** mediante P07. Es un cambio pasivo de descripción; no modifica el punto $P$.

### 4.11. Proposición: ley de traslación de las coordenadas

> **FPM-I-04-P10 — Cambio de origen con base fija**
> Si $O'=O+a$ y $B$ se conserva, entonces para cualquier $P\in\mathcal E$,
>
> $$
> \boxed{x_{(O',B)}(P)=x_{(O,B)}(P)-[a]_B.}
> $$
>
> Para cualesquiera $P,Q$, la diferencia de coordenadas no cambia:
>
> $$
> \boxed{x_{(O',B)}(Q)-x_{(O',B)}(P)
> =x_{(O,B)}(Q)-x_{(O,B)}(P).}
> $$

**Demostración.** La primera identidad se obtiene aplicando P07 a $r_{O'}(P)=r_O(P)-a$ y usando D12. Sustraemos esta identidad para $Q$ y para $P$; los términos $-[a]_B$ se cancelan. De manera independiente, P09 identifica ambas diferencias con $[\overrightarrow{PQ}]_B$. $\square$
**Prueba de estrés del signo.** Si el nuevo origen se desplaza **hacia** un punto manteniendo la base, la coordenada de ese punto disminuye en la componente correspondiente. Sumar $[a]_B$ sería confundir el desplazamiento del origen con el cambio de coordenada del objeto.

### 4.12. Ejemplo: dos planos de un mismo laboratorio

Sea

$$
x_{(O,B)}(P)=\begin{pmatrix}2\\-1\\3\end{pmatrix},
\qquad [a]_B=\begin{pmatrix}1\\2\\-1\end{pmatrix}.
$$

Para $O'=O+a$, sin mover $P$ ni alterar $B$,

$$
x_{(O',B)}(P)=
\begin{pmatrix}2\\-1\\3\end{pmatrix}
-\begin{pmatrix}1\\2\\-1\end{pmatrix}
=\begin{pmatrix}1\\-3\\4\end{pmatrix}.
$$

Recuperamos la representación antigua sumando $[a]_B$. Dos columnas distintas representan el **mismo punto** en marcos distintos; no se deduce un desplazamiento del detector.
Si también cambiásemos $B$, la fórmula anterior sería insuficiente: necesitaríamos además la matriz de cambio de base, que se desarrollará en §10. La composición sistemática de ambos cambios será propia de §12.

### 4.13. Coordenadas de las combinaciones afines

> **FPM-I-04-P11 — Compatibilidad con combinaciones afines**
> Si $A$ es la combinación afín de puntos $P_1,\ldots,P_n$ con coeficientes $\lambda_i$ tales que $\sum_i\lambda_i=1$, entonces, en cualquier marco fijo $\mathfrak F$,
>
> $$
> \boxed{x_{\mathfrak F}(A)
> =\sum_i\lambda_i x_{\mathfrak F}(P_i).}
> $$

**Demostración.** D04 permite escribir $A=O+\sum_i\lambda_i\overrightarrow{OP_i}$ porque los coeficientes suman uno. Aplicamos D12 y la linealidad de P07 al vector $\overrightarrow{OA}$ y obtenemos la fórmula. Para otro origen $O'=O+a$, la suma de las nuevas columnas es $\sum_i\lambda_i(x_{\mathfrak F}(P_i)-[a]_B)=\sum_i\lambda_i x_{\mathfrak F}(P_i)-[a]_B$, exactamente la nueva columna de $A$ por P10. $\square$
Para el punto medio de §2:

$$
\boxed{x_{\mathfrak F}(M(P,Q))=
\tfrac12x_{\mathfrak F}(P)+\tfrac12x_{\mathfrak F}(Q).}
$$

Para un baricentro con $W=\sum_i w_i\ne0$, los coeficientes son $w_i/W$, y la misma fórmula vale. La suma de coeficientes uno no es un detalle cosmético: impide que el punto resultante dependa del origen.

### 4.14. Unidades y escalas: qué miden los coeficientes

La ecuación $\overrightarrow{OP}=\sum_i x^ie_i$ sólo tiene interpretación dimensional después de declarar qué representan los $e_i$. Por ejemplo, si cada $e_i$ es un **desplazamiento de referencia con dimensión de longitud**, los coeficientes $x^i$ son números adimensionales; el producto $x^ie_i$ sí es una cantidad vectorial de longitud. Si se trabaja con símbolos de direcciones adimensionales y componentes dimensionales, es preciso declararlo como una convención diferente, no mezclar ambas escrituras sin aviso.
Los tres desplazamientos de referencia no tienen por qué ser de igual longitud física. Una columna como $(2,-1,3)^{\mathsf T}$ no proporciona por sí sola tres medidas en metros ni permite calcular la distancia al origen. La noción métrica aún no existe en el desarrollo deductivo.

> FPM-I-02 y FPM-I-03
> El número escrito en el plano no equivale a una medición sin declarar patrones, instrumentos, mensurando e incertidumbre. Las identidades de esta sección son exactas **en el modelo afín**; la realización física de un sistema de marcas requiere procedimientos y puede tener incertidumbre.

### 4.15. Diagnóstico de afirmaciones plausibles pero falsas

**«Tres flechas de referencia cualesquiera definen un marco».** Falso: deben constituir una base, es decir, generar $V$ y ser independientes (D09).
**«El origen tiene coordenadas cero en todos los marcos».** El origen *elegido por cada marco* tiene coordenadas cero en su propio marco. El mismo punto $O$ no tiene necesariamente coordenadas cero respecto de otro origen $O'$.
**«Si cambia la terna, el objeto se movió».** Falso: P10 exhibe un contraejemplo mediante un mero cambio de origen.
**«Si dos ternas son iguales, los puntos son necesariamente iguales».** Sólo si las ternas se interpretan en el **mismo marco**; P08 no establece identidad entre columnas procedentes de marcos diferentes.
**«La diferencia de ternas es un desplazamiento geométrico absoluto».** Debe precisarse: en un mismo marco, es la **columna en la base declarada** del desplazamiento intrínseco (P09). Otra base puede proporcionar una columna diferente para ese mismo vector.
**«Llamar cartesiano al marco demuestra ejes perpendiculares».** No: la perpendicularidad necesita un producto escalar (§5), y la ortonormalidad será construida en §7.

[]{#fispm-t1-c04-e0008}

### 4.16. Ejercicio FPM-I-04-E008 — Dos orígenes, ningún movimiento

> **Función cognitiva:** `cambio de representación / control del signo / invariancia`.
>
> En un marco afín $\mathfrak F=(O,B)$, dos marcas tienen columnas
>
> $$
> x_{\mathfrak F}(P)=\begin{pmatrix}4\\-2\\1\end{pmatrix},
> \qquad x_{\mathfrak F}(Q)=\begin{pmatrix}-1\\3\\2\end{pmatrix}.
> $$
>
> Se elige $O'=O+a$ manteniendo $B$, con $[a]_B=(2,-1,4)^{\mathsf T}$.
>
> 1. Calcula las columnas de ambos puntos respecto de $(O',B)$.
> 2. Calcula la columna de $\overrightarrow{PQ}$ por las dos rutas.
> 3. Explica si las marcas se movieron y por qué no puede inferirse su distancia geométrica sólo de estas columnas.

> **Solución desarrollada**
> Por P10 restamos la columna de $a$ a cada punto:
>
> $$
> x_{(O',B)}(P)=\begin{pmatrix}2\\-1\\-3\end{pmatrix},
> \qquad x_{(O',B)}(Q)=\begin{pmatrix}-3\\4\\-2\end{pmatrix}.
> $$
>
> En el marco inicial, P09 da
>
> $$
> [\overrightarrow{PQ}]_B=
> \begin{pmatrix}-1\\3\\2\end{pmatrix}
> -\begin{pmatrix}4\\-2\\1\end{pmatrix}
> =\begin{pmatrix}-5\\5\\1\end{pmatrix}.
> $$
>
> En el marco nuevo,
>
> $$
> \begin{pmatrix}-3\\4\\-2\end{pmatrix}
> -\begin{pmatrix}2\\-1\\-3\end{pmatrix}
> =\begin{pmatrix}-5\\5\\1\end{pmatrix}.
> $$
>
> Coinciden porque no cambió $B$ ni los puntos, sólo el origen: es una transformación pasiva. No podemos convertir la columna $(-5,5,1)^{\mathsf T}$ en una distancia sin definir una métrica sobre $V$ y especificar el significado de las escalas de la base.

[]{#fispm-t1-c04-e0009}

### 4.17. Ejercicio FPM-I-04-E009 — Marco válido, punto medio y errores de tipo

> **Función cognitiva:** `construcción / no-ejemplo / traducción geometría–columnas`.
>
> Sea $E=(e_1,e_2,e_3)$ una base de $V$ y elijamos un origen $O$. Definimos
>
> $$
> b_1=e_1,\qquad b_2=e_1+e_2,\qquad b_3=e_1+e_2+e_3.
> $$
>
> En $\mathfrak F=(O,B)$, $B=(b_1,b_2,b_3)$, dos puntos tienen coordenadas
>
> $$
> x_{\mathfrak F}(P)=\begin{pmatrix}1\\2\\-1\end{pmatrix},
> \qquad x_{\mathfrak F}(Q)=\begin{pmatrix}3\\0\\1\end{pmatrix}.
> $$
>
> 1. Justifica que $B$ es una base sin usar determinantes.
> 2. Calcula las coordenadas de $M(P,Q)$ en $B$ y el vector $\overrightarrow{PQ}$ expresado en $E$.
> 3. Analiza las frases «$P=[P]_B$» y «el punto medio es la mitad de la suma vectorial $P+Q$».

> **Solución desarrollada**
> Para $v=ae_1+be_2+ce_3$, buscar $v=xb_1+yb_2+zb_3$ lleva a $x+y+z=a$, $y+z=b$, $z=c$, con solución única $x=a-b$, $y=b-c$, $z=c$. Por P06, $B$ es base.
>
> Por P11,
>
> $$
> x_{\mathfrak F}(M)=\frac12
> \left(\begin{pmatrix}1\\2\\-1\end{pmatrix}
> +\begin{pmatrix}3\\0\\1\end{pmatrix}\right)
> =\begin{pmatrix}2\\1\\0\end{pmatrix}.
> $$
>
> Por P09, $[\overrightarrow{PQ}]_B=(2,-2,2)^{\mathsf T}$. Por la definición de $B$,
>
> $$
> \begin{aligned}
> \overrightarrow{PQ}
> &=2b_1-2b_2+2b_3\\
> &=2e_1-2(e_1+e_2)+2(e_1+e_2+e_3)\\
> &=2e_1+0e_2+2e_3.
> \end{aligned}
> $$
>
> La primera frase confunde un punto $P\in\mathcal E$ con su columna de coordenadas $x_{\mathfrak F}(P)\in\mathbb R^3$; $[P]_B$ ni siquiera es la notación definida para puntos. La segunda frase usa una suma vectorial $P+Q$ que no existe en D01: la formulación correcta es $M=P+\tfrac12\overrightarrow{PQ}$, cuya columna puede calcularse por el promedio de P11.

### 4.18. Cierre y enlace deductivo

La representación de un punto necesita dos elecciones:

$$
\boxed{\text{marco afín}=\text{origen}+\text{base ordenada}.}
$$

Con ambas fijadas, las coordenadas son únicas (P08); la resta de columnas representa un desplazamiento (P09); trasladar sólo el origen modifica las coordenadas por un término común y conserva las diferencias (P10); combinar puntos afínmente es compatible con combinar sus columnas usando coeficientes de suma uno (P11).
Pero todavía **no** hemos definido la longitud de una flecha ni la distancia entre dos puntos. El siguiente paso será precisamente

$$
\boxed{\text{§5 — Producto escalar, norma y distancia}.}
$$

Allí distinguiremos la mera independencia de los ejes de su perpendicularidad y construiremos las herramientas métricas necesarias para hablar con precisión de sistemas cartesianos rectangulares.

[^shankar-axes]: R. Shankar, *Fundamentals of Physics I: Mechanics, Relativity, and Thermodynamics*, expanded ed., Yale University Press, 2019, cap. 2, §2.4 «Choice of axes and basis vectors», pp. 22–25.

---

[]{#fispm-t1-c04-s05}

[]{#fpm-i-04-s05}

## §5 — Producto escalar, norma y distancia

### 5.1. Activación: las coordenadas todavía no saben medir

En §4 aprendimos a asignar a un punto una terna de coordenadas una vez fijado un marco afín. Supongamos que dos puntos tienen coordenadas

$$
x_{\mathfrak F}(P)=
\begin{pmatrix}
0\\0\\0
\end{pmatrix},
\qquad
x_{\mathfrak F}(Q)=
\begin{pmatrix}
3\\4\\0
\end{pmatrix}.
$$

Es tentador concluir inmediatamente que están separados por «$5$ unidades». Pero hasta ahora la base $B=(e_1,e_2,e_3)$ sólo es una base algebraica. No sabemos todavía cuánto mide cada $e_i$, ni si las direcciones asociadas forman ángulos rectos.
La columna

$$
\begin{pmatrix}
3\\4\\0
\end{pmatrix}
$$

describe componentes del desplazamiento; **no contiene por sí sola una regla de longitud**.

> Activación
> ¿Qué estructura matemática debemos añadir a $V$ para comparar longitudes y hablar de distancia sin depender de una base particular?

### 5.2. La geometría afín y la geometría métrica son capas distintas

La estructura afín construida hasta §4 permite distinguir puntos y vectores, trasladar puntos, formar diferencias, elegir bases y representar puntos y desplazamientos por columnas. Nada de esto define todavía longitud, distancia, perpendicularidad o ángulo.

> **FPM-I-04-MP06 — La métrica es estructura adicional**
> No inferir longitudes, distancias ni perpendicularidad a partir de una terna de componentes sin declarar antes el producto escalar —o una estructura métrica equivalente— con el que se interpretan esas componentes.

### 5.3. Definir: producto escalar real

> **FPM-I-04-D14 — Producto escalar real**
> Un **producto escalar** sobre $V$ es una aplicación
>
> $$
> \langle\cdot,\cdot\rangle:V\times V\longrightarrow\mathbb R
> $$
>
> tal que para todos $u,v,w\in V$ y $\alpha,\beta\in\mathbb R$:
>
> $$
> \langle \alpha u+\beta v,w\rangle
> =\alpha\langle u,w\rangle+\beta\langle v,w\rangle,
> $$
>
> $$
> \langle u,v\rangle=\langle v,u\rangle,
> $$
>
> y
>
> $$
> \langle v,v\rangle\ge0,
> \qquad
> \langle v,v\rangle=0\Longleftrightarrow v=0.
> $$

Por simetría y bilinealidad en la primera entrada, también hay linealidad en la segunda.

### 5.4. Definir: espacio afín euclídeo

> **FPM-I-04-D15 — Espacio afín euclídeo**
> Un **espacio afín euclídeo** es un espacio afín $\mathcal E$ modelado sobre un espacio vectorial real $V$ provisto de un producto escalar positivo definido.

La estructura afín determina desplazamientos; el producto escalar añade la posibilidad de medirlos. Que un sistema físico concreto sea adecuadamente modelado así es una cuestión física y experimental, no una consecuencia de la definición.

### 5.5. Definir: norma inducida

> **FPM-I-04-D16 — Norma euclídea inducida**
> Para $v\in V$ definimos
>
> $$
> \boxed{\|v\|:=\sqrt{\langle v,v\rangle}.}
> $$

La positividad garantiza

$$
\|v\|\ge0,
\qquad
\|v\|=0\Longleftrightarrow v=0.
$$

Además,

$$
\|\lambda v\|
=\sqrt{\lambda^2\langle v,v\rangle}
=|\lambda|\,\|v\|.
$$

### 5.6. Proposición: desigualdad de Cauchy–Schwarz

> **FPM-I-04-P12 — Desigualdad de Cauchy–Schwarz**
> Para todos $u,v\in V$,
>
> $$
> \boxed{|\langle u,v\rangle|\le\|u\|\,\|v\|.}
> $$
>
> Hay igualdad si y sólo si $u$ y $v$ son linealmente dependientes.

**Demostración.** Si $v=0$, el resultado es inmediato. Supongamos $v\ne0$ y definamos

$$
\lambda=\frac{\langle u,v\rangle}{\langle v,v\rangle}.
$$

La positividad da

$$
0\le\|u-\lambda v\|^2
=\langle u-\lambda v,u-\lambda v\rangle.
$$

Expandiendo,

$$
0\le
\langle u,u\rangle
-2\lambda\langle u,v\rangle
+\lambda^2\langle v,v\rangle.
$$

Al sustituir $\lambda$,

$$
0\le
\langle u,u\rangle
-\frac{\langle u,v\rangle^2}{\langle v,v\rangle}.
$$

Por tanto,

$$
\langle u,v\rangle^2
\le
\langle u,u\rangle\langle v,v\rangle,
$$

y al tomar raíces,

$$
|\langle u,v\rangle|
\le
\|u\|\,\|v\|.
$$

La igualdad ocurre exactamente cuando $\|u-\lambda v\|=0$, es decir, cuando $u=\lambda v$; incluyendo los casos nulos, esto equivale a dependencia lineal. $\square$

### 5.7. Proposición: desigualdad triangular de la norma

> **FPM-I-04-P13 — Desigualdad triangular**
> Para todos $u,v\in V$,
>
> $$
> \boxed{\|u+v\|\le\|u\|+\|v\|.}
> $$

**Demostración.**

$$
\begin{aligned}
\|u+v\|^2
&=\|u\|^2+2\langle u,v\rangle+\|v\|^2\\
&\le\|u\|^2+2|\langle u,v\rangle|+\|v\|^2\\
&\le(\|u\|+\|v\|)^2.
\end{aligned}
$$

Como ambos lados son no negativos, tomamos raíces. $\square$
La ley del triángulo de §1 era una identidad vectorial; P13 compara longitudes.

### 5.8. Definir: distancia entre puntos

> **FPM-I-04-D17 — Distancia euclídea**
> Para $P,Q\in\mathcal E$,
>
> $$
> \boxed{d(P,Q):=\|\overrightarrow{PQ}\|.}
> $$

La definición no requiere origen ni base.

### 5.9. Proposición: la distancia satisface los axiomas métricos

> **FPM-I-04-P14 — Propiedades métricas de $d$**
> Para cualesquiera $P,Q,R\in\mathcal E$:
>
> $$
> d(P,Q)\ge0,
> \qquad
> d(P,Q)=0\Longleftrightarrow P=Q,
> $$
>
> $$
> d(P,Q)=d(Q,P),
> $$
>
> y
>
> $$
> \boxed{d(P,R)\le d(P,Q)+d(Q,R).}
> $$

**Demostración.** Las dos primeras propiedades siguen de D16. La simetría usa $\overrightarrow{QP}=-\overrightarrow{PQ}$ y $\|-v\|=\|v\|$. Finalmente,

$$
\overrightarrow{PR}
=
\overrightarrow{PQ}+\overrightarrow{QR},
$$

y P13 produce la desigualdad triangular de la distancia. $\square$

### 5.10. La métrica en una base general: matriz de Gram

> **FPM-I-04-D18 — Matriz de Gram de una base**
> Sea $B=(e_1,e_2,e_3)$ una base. Su **matriz de Gram** es
>
> $$
> \boxed{
> G_B=
> \begin{pmatrix}
> \langle e_1,e_1\rangle & \langle e_1,e_2\rangle & \langle e_1,e_3\rangle\\
> \langle e_2,e_1\rangle & \langle e_2,e_2\rangle & \langle e_2,e_3\rangle\\
> \langle e_3,e_1\rangle & \langle e_3,e_2\rangle & \langle e_3,e_3\rangle
> \end{pmatrix}.
> }
> $$

Si $c=[v]_B$, entonces

$$
\boxed{
\|v\|^2=c^{\mathsf T}G_Bc.
}
$$

### 5.11. Proposición: positividad de la matriz de Gram

> **FPM-I-04-P15 — Forma cuadrática de Gram**
> Para toda columna no nula $c\in\mathbb R^3$,
>
> $$
> \boxed{c^{\mathsf T}G_Bc>0.}
> $$

**Demostración.** El vector $v=c^1e_1+c^2e_2+c^3e_3$ es no nulo porque $B$ es una base y $c\ne0$. Luego

$$
c^{\mathsf T}G_Bc
=\langle v,v\rangle>0.
$$

$\square$

### 5.12. No-ejemplo: la fórmula pitagórica no vale en cualquier base

Supongamos

$$
\langle e_1,e_1\rangle=4,
\qquad
\langle e_2,e_2\rangle=1,
\qquad
\langle e_1,e_2\rangle=1.
$$

Para $v=2e_1-e_2$,

$$
\begin{aligned}
\|v\|^2
&=4\langle e_1,e_1\rangle
-4\langle e_1,e_2\rangle
+\langle e_2,e_2\rangle\\
&=16-4+1=13.
\end{aligned}
$$

Por tanto,

$$
\|v\|=\sqrt{13},
$$

no $\sqrt5$.

> Coordenadas no son métrica
> La expresión $\sqrt{(v^1)^2+(v^2)^2+(v^3)^2}$ no es universal. Sólo aparecerá bajo hipótesis adicionales sobre la base, introducidas en §7.

### 5.13. Invariancia frente al origen y dependencia respecto de la métrica

Si el origen cambia pero la base permanece fija, P10 preserva las diferencias de coordenadas. Por ello $\overrightarrow{PQ}$ y $d(P,Q)$ permanecen iguales.
Esto no significa que la distancia sea independiente de toda estructura: si sobre $V$ elegimos otro producto escalar, podemos obtener longitudes distintas. La métrica forma parte del modelo.

### 5.14. Interpretación física y unidades

Si los vectores modelan desplazamientos, entonces $\|v\|$ tiene dimensión de longitud y $\langle u,v\rangle$ dimensión de longitud al cuadrado. Si los vectores base llevan dimensión de longitud, las entradas de $G_B$ también tienen dimensión de longitud al cuadrado y sus componentes pueden ser adimensionales.
Las identidades geométricas son exactas dentro del modelo. Una medición experimental de una distancia posee resolución e incertidumbre, según FPM-I-03.

[]{#fispm-t1-c04-e0010}

### 5.15. Ejercicio FPM-I-04-E010 — Una columna no determina por sí sola la longitud

> **Función pedagógica:** `Diagnóstico → Matriz de Gram → No-ejemplo`
>
> En una base $B=(e_1,e_2,e_3)$:
>
> $$
> \langle e_1,e_1\rangle=4\,\mathrm{m^2},
> \quad
> \langle e_2,e_2\rangle=1\,\mathrm{m^2},
> \quad
> \langle e_1,e_2\rangle=1\,\mathrm{m^2}.
> $$
>
> Si
>
> $$
> [v]_B=
> \begin{pmatrix}
> 2\\-1\\0
> \end{pmatrix},
> $$
>
> calcula $\|v\|$, explica por qué $\sqrt5\,\mathrm m$ es incorrecto e indica qué datos faltan si la tercera componente fuese no nula.

> **Solución desarrollada**
>
> $$
> \|v\|^2
> =16-4+1
> =13\,\mathrm{m^2},
> $$
>
> luego
>
> $$
> \boxed{\|v\|=\sqrt{13}\,\mathrm m.}
> $$
>
> La raíz $\sqrt5$ presupone condiciones métricas especiales sobre la base que no han sido dadas. Para una tercera componente no nula se requerirían además $\langle e_3,e_3\rangle$, $\langle e_1,e_3\rangle$ y $\langle e_2,e_3\rangle$.

[]{#fispm-t1-c04-e0011}

### 5.16. Ejercicio FPM-I-04-E011 — Distancia, cambio de origen y desigualdad triangular

> **Función pedagógica:** `Integración → Invariancia → Desigualdad triangular`
>
> En un marco $\mathfrak F=(O,B)$:
>
> $$
> x_{\mathfrak F}(P)=
> \begin{pmatrix}0\\0\\0\end{pmatrix},
> \quad
> x_{\mathfrak F}(Q)=
> \begin{pmatrix}1\\1\\0\end{pmatrix},
> \quad
> x_{\mathfrak F}(R)=
> \begin{pmatrix}3\\1\\0\end{pmatrix}.
> $$
>
> Además,
>
> $$
> \langle e_1,e_1\rangle=1\,\mathrm{m^2},
> \quad
> \langle e_2,e_2\rangle=4\,\mathrm{m^2},
> \quad
> \langle e_1,e_2\rangle=0.
> $$
>
> Calcula las tres distancias, verifica P14 y explica por qué un traslado del origen con base fija no las modifica.

> **Solución desarrollada**
>
> Las columnas de los desplazamientos son
>
> $$
> \begin{pmatrix}1\\1\\0\end{pmatrix},
> \qquad
> \begin{pmatrix}2\\0\\0\end{pmatrix},
> \qquad
> \begin{pmatrix}3\\1\\0\end{pmatrix}.
> $$
>
> Por tanto,
>
> $$
> \boxed{
> d(P,Q)=\sqrt5\,\mathrm m,\qquad
> d(Q,R)=2\,\mathrm m,\qquad
> d(P,R)=\sqrt{13}\,\mathrm m.
> }
> $$
>
> Y
>
> $$
> \sqrt{13}\le\sqrt5+2.
> $$
>
> Bajo un cambio de origen con base fija, P10 resta la misma columna a las coordenadas de todos los puntos. Las diferencias permanecen iguales y, por tanto, también las distancias.

### 5.17. Cierre: de la estructura afín a la geometría euclídea

La cadena construida es

$$
\boxed{
\text{estructura afín}
+\langle\cdot,\cdot\rangle
\longrightarrow
\|v\|
\longrightarrow
d(P,Q).
}
$$

Cauchy–Schwarz controla el producto escalar; de ella se obtiene la desigualdad triangular de la norma y después la de la distancia.
El siguiente paso será

$$
\boxed{\text{§6 — Proyecciones, ángulos y geometría de componentes}.}
$$

---

[]{#fispm-t1-c04-s06}

[]{#fpm-i-04-s06}

## §6 — Proyecciones, ángulos y geometría de componentes

### 6.1. Activación: ¿cuánto de un vector apunta en una dirección?

Una fuerza, un desplazamiento o cualquier otro vector puede compararse con una dirección elegida. La pregunta física típica no es sólo cuánto mide el vector completo, sino **qué parte de él actúa a lo largo de una dirección determinada**.
Con sólo componentes algebraicas esta pregunta depende de cómo hayamos elegido la base. Con el producto escalar introducido en §5 podemos formularla sin depender de una representación particular.
Sean $u,v\in V$, con $v\ne0$. Queremos construir un múltiplo de $v$ que represente la parte de $u$ alineada con la dirección de $v$, y que el resto sea perpendicular a esa dirección.

### 6.2. Definir: ortogonalidad

> **FPM-I-04-D19 — Ortogonalidad**
> Dos vectores $u,v\in V$ son **ortogonales**, y escribimos
>
> $$
> u\perp v,
> $$
>
> si
>
> $$
> \boxed{\langle u,v\rangle=0.}
> $$

La definición utiliza el producto escalar, no la apariencia de un dibujo ni la forma de sus columnas en una base arbitraria.
En particular, el vector cero es ortogonal a todo vector:

$$
\langle 0,v\rangle=0.
$$

La afirmación inversa «si $u\perp v$, entonces uno de los dos es cero» es falsa: pueden existir dos vectores no nulos y ortogonales.

### 6.3. La condición que debe satisfacer una proyección

Busquemos un vector de la forma

$$
p=\lambda v
$$

tal que el residuo

$$
r:=u-p
$$

sea ortogonal a $v$. La condición es

$$
\langle u-\lambda v,v\rangle=0.
$$

Por bilinealidad,

$$
\langle u,v\rangle-\lambda\langle v,v\rangle=0.
$$

Como $v\ne0$, D14 implica

$$
\langle v,v\rangle>0.
$$

Por tanto el coeficiente queda determinado de manera única:

$$
\boxed{
\lambda=
\frac{\langle u,v\rangle}{\langle v,v\rangle}.
}
$$

La construcción no requiere todavía definir un ángulo.

### 6.4. Definir: proyección ortogonal sobre una dirección

> **FPM-I-04-D20 — Proyección ortogonal sobre un vector no nulo**
> Para $v\ne0$, definimos la **proyección ortogonal de $u$ sobre la dirección de $v$** por
>
> $$
> \boxed{
> \operatorname{proj}_v(u)
> :=
> \frac{\langle u,v\rangle}{\langle v,v\rangle}\,v.
> }
> $$

El resultado pertenece al subespacio generado por $v$:

$$
\operatorname{proj}_v(u)\in\operatorname{span}(v).
$$

Si reemplazamos $v$ por otro vector no nulo de la misma dirección, por ejemplo $cv$ con $c\ne0$, obtenemos el mismo vector proyectado:

$$
\operatorname{proj}_{cv}(u)=\operatorname{proj}_v(u).
$$

Por ello la proyección depende de la **dirección** o recta vectorial elegida, no de la longitud particular del representante $v$.

> **FPM-I-04-MP07 — Declarar la dirección y la métrica antes de proyectar**
> Una «componente en una dirección» no se obtiene tomando una entrada de una columna salvo en situaciones especiales. Primero se fija la dirección geométrica y el producto escalar; después se proyecta.

### 6.5. Proposición: descomposición ortogonal y unicidad

> **FPM-I-04-P16 — Descomposición ortogonal respecto de una dirección**
> Sean $u,v\in V$ con $v\ne0$. Entonces existe una única descomposición
>
> $$
> \boxed{
> u=p+r
> }
> $$
>
> tal que
>
> $$
> p\in\operatorname{span}(v),
> \qquad
> r\perp v.
> $$
>
> Está dada por
>
> $$
> \boxed{
> p=\operatorname{proj}_v(u),
> \qquad
> r=u-\operatorname{proj}_v(u).
> }
> $$

**Demostración.** Por D20, $p$ es un múltiplo de $v$. Además,

$$
\begin{aligned}
\langle r,v\rangle
&=
\left\langle
u-\frac{\langle u,v\rangle}{\langle v,v\rangle}v,
v
\right\rangle\\
&=
\langle u,v\rangle
-
\frac{\langle u,v\rangle}{\langle v,v\rangle}
\langle v,v\rangle\\
&=0.
\end{aligned}
$$

Por tanto $r\perp v$.
Para la unicidad, supongamos también

$$
u=\alpha v+s,
\qquad
s\perp v.
$$

Tomando producto escalar con $v$,

$$
\langle u,v\rangle
=
\alpha\langle v,v\rangle,
$$

de donde

$$
\alpha=
\frac{\langle u,v\rangle}{\langle v,v\rangle}.
$$

Así $\alpha v=p$, y entonces $s=u-p=r$. $\square$
La prueba separa con claridad las dos tareas: **existencia**, construyendo explícitamente $p$ y $r$; y **unicidad**, recuperando el coeficiente mediante el producto escalar.

### 6.6. Primera consecuencia: caso ortogonal y caso paralelo

Si $u\perp v$, entonces

$$
\langle u,v\rangle=0,
$$

y por tanto

$$
\boxed{\operatorname{proj}_v(u)=0.}
$$

En cambio, si $u=cv$, entonces

$$
\operatorname{proj}_v(u)
=
\frac{c\langle v,v\rangle}{\langle v,v\rangle}v
=cv=u.
$$

La proyección distingue de manera exacta dos extremos:

$$
\text{ortogonal a la dirección}
\longrightarrow 0,
$$

$$
\text{contenido enteramente en la dirección}
\longrightarrow u.
$$

### 6.7. Interpretación física y alcance de la proyección

Si $u$ representa un desplazamiento y $v$ fija una dirección de referencia, $\operatorname{proj}_v(u)$ es el desplazamiento vectorial que queda al conservar sólo la parte alineada con esa dirección según la métrica escogida.
Esto **no** significa que una proyección matemática sea una nueva medición. En una experiencia real, los datos con que se reconstruyen $u$ y la dirección de $v$ pueden tener incertidumbre; la identidad de P16 pertenece al modelo geométrico.
Tampoco hemos definido todavía un número llamado «ángulo entre $u$ y $v$». Ese concepto requiere usar Cauchy–Schwarz para demostrar primero que cierto cociente pertenece a $[-1,1]$.

### 6.8. Cauchy–Schwarz legitima el coseno

Sean ahora $u,v\in V$ no nulos. P12 implica

$$
|\langle u,v\rangle|
\le
\|u\|\,\|v\|.
$$

Como $\|u\|\,\|v\|>0$, podemos dividir y obtener

$$
\boxed{
-1\le
\frac{\langle u,v\rangle}{\|u\|\,\|v\|}
\le1.
}
$$

El cociente es adimensional y pertenece exactamente al dominio de la función $\arccos$ real. Esta verificación lógica debe preceder a la definición del ángulo.

### 6.9. Definir: ángulo entre vectores no nulos

> **FPM-I-04-D21 — Ángulo entre dos vectores no nulos**
> Para $u\ne0$ y $v\ne0$, definimos el **ángulo** $\theta(u,v)\in[0,\pi]$ por
>
> $$
> \boxed{
> \theta(u,v)
> :=
> \arccos\!\left(
> \frac{\langle u,v\rangle}{\|u\|\,\|v\|}
> \right).
> }
> $$

La definición no se extiende al vector cero: si $u=0$ o $v=0$, el denominador se anula y no hay una dirección geométrica determinada por ese vector.

> El ángulo no viene de las coordenadas
> La expresión anterior es intrínseca. En una base general, no debe reemplazarse por fórmulas de trigonometría sobre componentes salvo que la métrica de esa base haya sido incorporada correctamente.

### 6.10. Proposición: casos límite y ortogonalidad

> **FPM-I-04-P17 — Caracterización métrica de los ángulos límite**
> Sean $u,v\ne0$. Entonces:
>
> $$
> u\perp v
> \Longleftrightarrow
> \theta(u,v)=\frac{\pi}{2},
> $$
>
> $$
> \theta(u,v)=0
> \Longleftrightarrow
> u=cv\ \text{para algún }c>0,
> $$
>
> y
>
> $$
> \theta(u,v)=\pi
> \Longleftrightarrow
> u=cv\ \text{para algún }c<0.
> $$

**Demostración.** Por D21,

$$
\cos\theta(u,v)
=
\frac{\langle u,v\rangle}{\|u\|\,\|v\|}.
$$

Como el denominador es positivo, $\cos\theta=0$ si y sólo si $\langle u,v\rangle=0$, lo cual equivale a ortogonalidad por D19.
Para $\theta=0$ o $\pi$, el valor absoluto del coseno es uno. Por el caso de igualdad de Cauchy–Schwarz, $u$ y $v$ son linealmente dependientes: $u=cv$. El signo de

$$
\langle u,v\rangle
=
c\langle v,v\rangle
$$

determina $c>0$ cuando $\cos\theta=1$ y $c<0$ cuando $\cos\theta=-1$. La recíproca se verifica sustituyendo $u=cv$. $\square$
Esta proposición conecta tres lenguajes distintos: producto escalar, dependencia lineal y geometría angular.

### 6.11. Definir: componente escalar en una dirección

> **FPM-I-04-D22 — Componente escalar de un vector en una dirección orientada**
> Para $v\ne0$, definimos la **componente escalar de $u$ en la dirección orientada de $v$** por
>
> $$
> \boxed{
> \operatorname{comp}_v(u)
> :=
> \frac{\langle u,v\rangle}{\|v\|}.
> }
> $$

El signo contiene información de orientación:

$$
\operatorname{comp}_{-v}(u)
=
-\operatorname{comp}_v(u).
$$

En cambio, D20 da

$$
\operatorname{proj}_{-v}(u)
=
\operatorname{proj}_v(u).
$$

Por tanto, **la componente escalar depende del sentido elegido en la dirección**, mientras la proyección vectorial sólo depende de la recta vectorial.

> **FPM-I-04-MP08 — No confundir coordenada, componente escalar y proyección**
> Una entrada $v^i$ de una columna depende de la base; $\operatorname{comp}_w(v)$ depende de una dirección orientada y de la métrica; $\operatorname{proj}_w(v)$ es un vector geométrico. Antes de identificar dos de estas expresiones, demostrar las hipótesis que las relacionan.

### 6.12. Proposición: relación entre ángulo, componente y proyección

> **FPM-I-04-P18 — Forma angular de la componente y la proyección**
> Para $u,v\ne0$,
>
> $$
> \boxed{
> \operatorname{comp}_v(u)
> =
> \|u\|\cos\theta(u,v).
> }
> $$
>
> Si
>
> $$
> \widehat v:=\frac{v}{\|v\|},
> $$
>
> entonces
>
> $$
> \boxed{
> \operatorname{proj}_v(u)
> =
> \operatorname{comp}_v(u)\,\widehat v.
> }
> $$
>
> En particular,
>
> $$
> \boxed{
> \|\operatorname{proj}_v(u)\|
> =
> |\operatorname{comp}_v(u)|.
> }
> $$

**Demostración.** De D21,

$$
\langle u,v\rangle
=
\|u\|\,\|v\|\cos\theta(u,v).
$$

Dividir por $\|v\|$ prueba la primera fórmula. Luego

$$
\operatorname{comp}_v(u)\widehat v
=
\frac{\langle u,v\rangle}{\|v\|}
\frac{v}{\|v\|}
=
\frac{\langle u,v\rangle}{\langle v,v\rangle}v
=
\operatorname{proj}_v(u).
$$

Finalmente, $\|\widehat v\|=1$ y la homogeneidad de la norma producen la última igualdad. $\square$

### 6.13. Ejemplo sin coordenadas

Supongamos

$$
\|u\|=5,
\qquad
\|v\|=2,
\qquad
\langle u,v\rangle=6.
$$

Entonces

$$
\cos\theta(u,v)
=
\frac{6}{5\cdot2}
=
\frac35,
$$

y

$$
\theta(u,v)
=
\arccos\!\left(\frac35\right).
$$

La componente escalar es

$$
\operatorname{comp}_v(u)
=
\frac{6}{2}
=
3,
$$

mientras que

$$
\operatorname{proj}_v(u)
=
\frac{6}{4}v
=
\frac32v.
$$

El número $3$ y el vector $\tfrac32v$ codifican aspectos distintos de la misma descomposición: uno es una magnitud escalar con signo y el otro es un vector.

### 6.14. Balance conceptual: del ángulo a Pitágoras

Ya podemos pasar rigurosamente de

$$
\langle u,v\rangle
$$

a tres objetos diferentes:

$$
\boxed{
\theta(u,v),\qquad
\operatorname{comp}_v(u),\qquad
\operatorname{proj}_v(u).
}
$$

La geometría elemental de la proyección todavía necesita una última pieza: cuantificar cómo se reparte la longitud total entre la parte paralela y la parte perpendicular.

### 6.15. Proposición: identidad pitagórica de la descomposición ortogonal

> **FPM-I-04-P19 — Pitágoras para proyección y residuo**
> Sean $u,v\in V$ con $v\ne0$. Definamos
>
> $$
> p:=\operatorname{proj}_v(u),
> \qquad
> r:=u-p.
> $$
>
> Entonces $p\perp r$ y
>
> $$
> \boxed{
> \|u\|^2
> =
> \|p\|^2+\|r\|^2.
> }
> $$

**Demostración.** P16 da $r\perp v$. Como $p$ es múltiplo de $v$, también $r\perp p$. Por tanto,

$$
\begin{aligned}
\|u\|^2
&=\langle p+r,p+r\rangle\\
&=\langle p,p\rangle
+2\langle p,r\rangle
+\langle r,r\rangle\\
&=\|p\|^2+\|r\|^2.
\end{aligned}
$$

$\square$

Esta identidad no es la fórmula pitagórica por **componentes de una base arbitraria**. Se aplica porque aquí las dos partes concretas $p$ y $r$ han sido demostradas ortogonales.

### 6.16. Consecuencia: longitud perpendicular a una dirección

De P19 y P18,

$$
\|p\|
=
|\operatorname{comp}_v(u)|.
$$

Así,

$$
\boxed{
\|r\|^2
=
\|u\|^2
-
\operatorname{comp}_v(u)^2.
}
$$

Usando

$$
\operatorname{comp}_v(u)
=
\|u\|\cos\theta,
$$

obtenemos

$$
\|r\|^2
=
\|u\|^2(1-\cos^2\theta).
$$

Como $\theta\in[0,\pi]$ y $\sin\theta\ge0$ en ese intervalo,

$$
\boxed{
\|r\|
=
\|u\|\sin\theta.
}
$$

La interpretación geométrica es precisa:

- $\|u\|\cos\theta$ es la componente escalar **con signo** en la dirección orientada de $v$;
- $\|u\|\sin\theta$ es la magnitud no negativa de la parte perpendicular.

### 6.17. Geometría de componentes sin adelantar §7

Supongamos que una base contiene un vector $e_1$ de norma uno. Para

$$
u=u^1e_1+w,
$$

si además hemos demostrado que $w\perp e_1$, entonces

$$
u^1
=
\langle u,e_1\rangle
=
\operatorname{comp}_{e_1}(u).
$$

Pero esta identificación depende de **dos hipótesis**:

1. $\|e_1\|=1$;
2. el resto de la descomposición es ortogonal a $e_1$.

Una base general de §3 no garantiza ninguna de las dos. Por eso no podemos concluir todavía que todas las entradas de $[u]_B$ se recuperan mediante productos escalares con los vectores de la base.

> Anticipación controlada
> En §7 construiremos precisamente la situación en que todos los vectores de la base son unitarios y mutuamente ortogonales. Sólo entonces aparecerá sistemáticamente
>
> $$
> u^i=\langle u,e_i\rangle.
> $$

[]{#fispm-t1-c04-e0012}

### 6.18. Ejercicio FPM-I-04-E012 — Proyección, componente y residuo

> **Función pedagógica:** `Cálculo intrínseco → distinción de tipos → Pitágoras`
>
> Sean $u,v\in V$ con
>
> $$
> \|u\|=5,
> \qquad
> \|v\|=2,
> \qquad
> \langle u,v\rangle=6.
> $$
>
> Calcula:
>
> 1. $\operatorname{comp}_v(u)$;
> 2. $\operatorname{proj}_v(u)$;
> 3. $\|u-\operatorname{proj}_v(u)\|$;
> 4. el ángulo $\theta(u,v)$.

> **Solución desarrollada**
>
> La componente escalar es
>
> $$
> \operatorname{comp}_v(u)
> =
> \frac{6}{2}
> =3.
> $$
>
> La proyección vectorial es
>
> $$
> \operatorname{proj}_v(u)
> =
> \frac{6}{4}v
> =
> \frac32v.
> $$
>
> Su norma vale
>
> $$
> \left\|\operatorname{proj}_v(u)\right\|
> =3.
> $$
>
> Por P19,
>
> $$
> \|r\|^2
> =
> 5^2-3^2
> =
> 16,
> $$
>
> de modo que
>
> $$
> \boxed{\|r\|=4.}
> $$
>
> Finalmente,
>
> $$
> \cos\theta
> =
> \frac{6}{5\cdot2}
> =
> \frac35,
> $$
>
> y
>
> $$
> \boxed{
> \theta
> =
> \arccos\!\left(\frac35\right).
> }
> $$
>
> El número $3$, el vector $\tfrac32v$ y la longitud $4$ son objetos distintos: componente escalar, proyección vectorial y magnitud del residuo perpendicular.

[]{#fispm-t1-c04-e0013}

### 6.19. Ejercicio FPM-I-04-E013 — La dirección puede reescalarse sin cambiar la proyección

> **Función pedagógica:** `Invariancia → orientación → prueba algebraica`
>
> Sea $v\ne0$ y sea $c\ne0$.
>
> 1. Demuestra que
>
> $$
> \operatorname{proj}_{cv}(u)
> =
> \operatorname{proj}_v(u).
> $$
>
> 2. Determina la relación entre $\operatorname{comp}_{cv}(u)$ y $\operatorname{comp}_v(u)$.
> 3. Explica qué cambia si $c<0$.

> **Solución desarrollada**
>
> Por D20,
>
> $$
> \begin{aligned}
> \operatorname{proj}_{cv}(u)
> &=
> \frac{\langle u,cv\rangle}{\langle cv,cv\rangle}(cv)\\
> &=
> \frac{c\langle u,v\rangle}{c^2\langle v,v\rangle}(cv)\\
> &=
> \operatorname{proj}_v(u).
> \end{aligned}
> $$
>
> Para la componente escalar,
>
> $$
> \operatorname{comp}_{cv}(u)
> =
> \frac{c\langle u,v\rangle}{|c|\|v\|}
> =
> \frac{c}{|c|}
> \operatorname{comp}_v(u).
> $$
>
> Por tanto,
>
> $$
> \boxed{
> \operatorname{comp}_{cv}(u)
> =
> \begin{cases}
> \operatorname{comp}_v(u), & c>0,\\
> -\operatorname{comp}_v(u), & c<0.
> \end{cases}
> }
> $$
>
> Reescalar una dirección no cambia la recta vectorial y, por tanto, tampoco la proyección vectorial. Si $c<0$, sí se invierte el **sentido orientado** elegido y cambia el signo de la componente escalar.

### 6.20. Cierre de §6

La sección ha separado cuatro nociones que suelen mezclarse:

$$
\boxed{
\text{ortogonalidad},
\quad
\text{proyección vectorial},
\quad
\text{componente escalar},
\quad
\text{ángulo}.
}
$$

La cadena conceptual completa es

$$
\langle\cdot,\cdot\rangle
\longrightarrow
\perp
\longrightarrow
\operatorname{proj}_v(u)
\longrightarrow
\theta(u,v)
\longrightarrow
\operatorname{comp}_v(u),
$$

con P19 proporcionando el control pitagórico de la descomposición.
La conclusión pedagógica decisiva es:

$$
\boxed{
\text{una coordenada no es automáticamente una componente métrica}.
}
$$

Para convertir sistemáticamente las entradas de una columna en componentes métricas necesitamos una base cuyas direcciones sean unitarias y mutuamente ortogonales.
El siguiente paso será:

$$
\boxed{
\text{§7 — Bases ortonormales y descomposición}
}
$$

---

[]{#fispm-t1-c04-s07}

[]{#fpm-i-04-s07}

## §7 — Bases ortonormales y descomposición

### 7.1. Activación: ¿cuándo una coordenada coincide con una componente métrica?

En §3 una base $B=(e_1,e_2,e_3)$ permitió escribir todo vector de manera única:

$$
v=v^1e_1+v^2e_2+v^3e_3.
$$

En §5 vimos que, para una base general, no podemos calcular la longitud mediante

$$
\sqrt{(v^1)^2+(v^2)^2+(v^3)^2}
$$

sin conocer la matriz de Gram. En §6 descubrimos además que una componente escalar en una dirección unitaria se obtiene mediante un producto escalar.
La pregunta natural es entonces:

> Activación
> ¿Qué condiciones debe satisfacer una base para que sus coeficientes algebraicos $v^i$ sean exactamente las componentes métricas de $v$ en las tres direcciones de la base?

La respuesta combinará dos propiedades:

- cada vector de la base tiene norma uno;
- vectores de base distintos son ortogonales.

### 7.2. Definir: base ortonormal

> **FPM-I-04-D23 — Base ortonormal**
> Una base ordenada
>
> $$
> B=(e_1,e_2,e_3)
> $$
>
> de $V$ es **ortonormal** si
>
> $$
> \boxed{
> \langle e_i,e_j\rangle
> =
> \delta_{ij},
> }
> $$
>
> donde
>
> $$
> \delta_{ij}
> =
> \begin{cases}
> 1,& i=j,\\
> 0,& i\ne j.
> \end{cases}
> $$

Equivalentemente,

$$
\|e_i\|=1
$$

para cada $i$, y

$$
e_i\perp e_j
$$

si $i\ne j$.
La palabra **orto-normal** recuerda exactamente estas dos condiciones: ortogonalidad mutua y normalización a longitud uno.
> Unidades y normalización
> D23 está formulada para vectores matemáticamente normalizados una vez fijada la convención de unidades. Al realizar físicamente la geometría, puede factorizarse una escala de longitud común $\ell_0$: si $e_i$ es ortonormal en el sentido de D23 y se usan desplazamientos de referencia $b_i=\ell_0e_i$, entonces
>
> $$
> \langle b_i,b_j\rangle=\ell_0^2\delta_{ij}.
> $$
>
> Las coordenadas respecto de los $b_i$ pueden mantenerse adimensionales, pero deben conservarse los factores de escala de la matriz de Gram de §5. Equivalentemente, puede trabajarse con direcciones normalizadas y portar la escala física en las componentes. Son convenciones distintas y no deben mezclarse.

> Base ortogonal no significa todavía ortonormal
> Una base puede estar formada por vectores mutuamente ortogonales y, sin embargo, tener
>
> $$
> \|e_i\|\ne1.
> $$
>
> En ese caso, las fórmulas de esta sección deben conservar los factores de escala correspondientes.

### 7.3. La matriz de Gram se simplifica

D18 definió la matriz de Gram de una base:

$$
G_B
=
\bigl(\langle e_i,e_j\rangle\bigr)_{i,j}.
$$

Si $B$ es ortonormal, D23 implica inmediatamente

$$
\boxed{
G_B=I_3.
}
$$

Por eso la fórmula general de §5,

$$
\|v\|^2
=
[v]_B^{\mathsf T}G_B[v]_B,
$$

se reduce a

$$
\|v\|^2
=
[v]_B^{\mathsf T}[v]_B.
$$

Ésta es la razón estructural de la conocida suma de cuadrados. No es una propiedad de cualquier columna: es una consecuencia de que la matriz de Gram de la base sea la identidad.

### 7.4. Proposición: recuperar componentes mediante productos escalares

> **FPM-I-04-P20 — Componentes y norma en una base ortonormal**
> Sea
>
> $$
> B=(e_1,e_2,e_3)
> $$
>
> una base ortonormal. Si
>
> $$
> v=v^1e_1+v^2e_2+v^3e_3,
> $$
>
> entonces, para cada $k=1,2,3$,
>
> $$
> \boxed{
> v^k=\langle v,e_k\rangle.
> }
> $$
>
> Por tanto,
>
> $$
> \boxed{
> v
> =
> \sum_{k=1}^{3}
> \langle v,e_k\rangle e_k
> }
> $$
>
> y
>
> $$
> \boxed{
> \|v\|^2
> =
> \sum_{k=1}^{3}
> \langle v,e_k\rangle^2.
> }
> $$

**Demostración.** Partimos de la expansión única de P06:

$$
v=\sum_{i=1}^{3}v^ie_i.
$$

Tomamos producto escalar con $e_k$:

$$
\begin{aligned}
\langle v,e_k\rangle
&=
\left\langle
\sum_{i=1}^{3}v^ie_i,
e_k
\right\rangle\\
&=
\sum_{i=1}^{3}
v^i\langle e_i,e_k\rangle\\
&=
\sum_{i=1}^{3}
v^i\delta_{ik}\\
&=
v^k.
\end{aligned}
$$

Esto prueba la primera identidad. Sustituir los coeficientes obtenidos en la expansión de $v$ da

$$
v
=
\sum_{k=1}^{3}
\langle v,e_k\rangle e_k.
$$

Finalmente, como $G_B=I_3$,

$$
\|v\|^2
=
(v^1)^2+(v^2)^2+(v^3)^2
=
\sum_{k=1}^{3}
\langle v,e_k\rangle^2.
$$

$\square$

**Lectura guiada.** El paso decisivo es que el producto escalar con $e_k$ «selecciona» exactamente un coeficiente porque todos los términos cruzados desaparecen y $\langle e_k,e_k\rangle=1$.

### 7.5. Relación con las proyecciones de §6

Como $\|e_k\|=1$, D22 produce

$$
\operatorname{comp}_{e_k}(v)
=
\frac{\langle v,e_k\rangle}{\|e_k\|}
=
\langle v,e_k\rangle.
$$

Por P20,

$$
\boxed{
v^k
=
\operatorname{comp}_{e_k}(v).
}
$$

Además, D20 da

$$
\operatorname{proj}_{e_k}(v)
=
\langle v,e_k\rangle e_k
=
v^ke_k.
$$

Por tanto, en una base ortonormal sí coinciden de manera controlada tres lenguajes:

$$
\boxed{
\text{coeficiente algebraico}
=
\text{componente escalar métrica}
}
$$

y el término vectorial correspondiente es

$$
\boxed{
v^ke_k
=
\operatorname{proj}_{e_k}(v).
}
$$

La igualdad no era válida de manera automática en una base general; ahora está demostrada bajo una hipótesis precisa.

### 7.6. Principio metodológico y pregunta constructiva

> **FPM-I-04-MP09 — Verificar ortonormalidad antes de leer componentes métricamente**
> Antes de usar
>
> $$
> v^i=\langle v,e_i\rangle
> $$
>
> o
>
> $$
> \|v\|^2=\sum_i(v^i)^2,
> $$
>
> comprobar que la base declarada es ortonormal respecto del producto escalar utilizado.

La base ortonormal convierte una lista de coeficientes en una descripción métrica particularmente simple, pero no elimina la distinción de tipos:

- $v\in V$ es el vector;
- $[v]_B\in\mathbb R^3$ es su columna;
- $v^i$ es un escalar;
- $v^ie_i$ es una proyección vectorial.

Todavía falta responder una pregunta constructiva: dado un conjunto de vectores independientes que **no** es ortonormal, ¿cómo podemos producir a partir de él una base ortonormal?

### 7.7. La estrategia: quitar sucesivamente las partes ya explicadas

Sean

$$
a_1,a_2,a_3
$$

vectores linealmente independientes. El primer vector sólo necesita normalización:

$$
u_1:=a_1,
\qquad
e_1:=\frac{u_1}{\|u_1\|}.
$$

Para el segundo vector no basta con normalizar $a_2$, porque podría contener una parte paralela a $e_1$. Primero retiramos esa parte:

$$
u_2
:=
a_2-\operatorname{proj}_{e_1}(a_2)
=
a_2-\langle a_2,e_1\rangle e_1.
$$

Entonces $u_2\perp e_1$ por P16, y normalizamos:

$$
e_2:=\frac{u_2}{\|u_2\|}.
$$

Con el tercer vector debemos retirar las partes ya explicadas por las dos direcciones anteriores:

$$
u_3
:=
a_3
-\langle a_3,e_1\rangle e_1
-\langle a_3,e_2\rangle e_2,
$$

y finalmente

$$
e_3:=\frac{u_3}{\|u_3\|}.
$$

Antes de aceptar estas fórmulas debemos probar dos cuestiones:

1. que $u_2$ y $u_3$ no se anulan;
2. que reemplazar $a_k$ por $e_k$ no cambia los subespacios generados acumulativamente.

### 7.8. Definir: procedimiento de Gram–Schmidt en dimensión tres

> **FPM-I-04-D24 — Procedimiento de Gram–Schmidt**
> Sea $(a_1,a_2,a_3)$ una familia linealmente independiente. Definimos recursivamente
>
> $$
> u_1:=a_1,
> \qquad
> e_1:=\frac{u_1}{\|u_1\|},
> $$
>
> $$
> u_2
> :=
> a_2-\langle a_2,e_1\rangle e_1,
> \qquad
> e_2:=\frac{u_2}{\|u_2\|},
> $$
>
> y
>
> $$
> u_3
> :=
> a_3
> -\langle a_3,e_1\rangle e_1
> -\langle a_3,e_2\rangle e_2,
> \qquad
> e_3:=\frac{u_3}{\|u_3\|}.
> $$
>
> Cuando los denominadores son no nulos, la familia $(e_1,e_2,e_3)$ se denomina la **ortonormalización de Gram–Schmidt** de $(a_1,a_2,a_3)$ en ese orden.

La cláusula «cuando los denominadores son no nulos» no quedará como supuesto adicional: la independencia lineal de los $a_i$ permitirá demostrarlo.

### 7.9. Primer control: los residuos no pueden anularse

Para $u_1$ no hay dificultad: $a_1\ne0$ porque la familia es independiente.
Supongamos que

$$
u_2=0.
$$

Entonces

$$
a_2
=
\langle a_2,e_1\rangle e_1.
$$

Como $e_1$ es un múltiplo no nulo de $a_1$, se seguiría

$$
a_2\in\operatorname{span}(a_1),
$$

contradiciendo la independencia de $(a_1,a_2)$.
Para $u_3$, si

$$
u_3=0,
$$

entonces

$$
a_3
=
\langle a_3,e_1\rangle e_1
+
\langle a_3,e_2\rangle e_2.
$$

Una vez que probemos que

$$
\operatorname{span}(e_1,e_2)
=
\operatorname{span}(a_1,a_2),
$$

esto implicará

$$
a_3\in\operatorname{span}(a_1,a_2),
$$

otra contradicción con la independencia original.
Por tanto, la preservación del subespacio generado no es un detalle secundario: forma parte del argumento que garantiza que el algoritmo puede continuar.

### 7.10. Proposición: Gram–Schmidt preserva los subespacios generados

> **FPM-I-04-P21 — Preservación de generación por Gram–Schmidt**
> Para la construcción de D24,
>
> $$
> \boxed{
> \operatorname{span}(e_1)
> =
> \operatorname{span}(a_1),
> }
> $$
>
> $$
> \boxed{
> \operatorname{span}(e_1,e_2)
> =
> \operatorname{span}(a_1,a_2),
> }
> $$
>
> y
>
> $$
> \boxed{
> \operatorname{span}(e_1,e_2,e_3)
> =
> \operatorname{span}(a_1,a_2,a_3).
> }
> $$

**Demostración.**
Como $e_1=a_1/\|a_1\|$, cada uno es un múltiplo no nulo del otro. Por tanto generan el mismo subespacio.
Para la segunda etapa, D24 da

$$
u_2
=
a_2-\langle a_2,e_1\rangle e_1.
$$

Así,

$$
u_2\in\operatorname{span}(a_1,a_2),
$$

pues $e_1\in\operatorname{span}(a_1)$. Como $e_2$ es un múltiplo no nulo de $u_2$,

$$
e_2\in\operatorname{span}(a_1,a_2).
$$

Luego

$$
\operatorname{span}(e_1,e_2)
\subseteq
\operatorname{span}(a_1,a_2).
$$

En sentido inverso,

$$
a_2
=
u_2+\langle a_2,e_1\rangle e_1
=
\|u_2\|e_2
+
\langle a_2,e_1\rangle e_1,
$$

de modo que $a_2\in\operatorname{span}(e_1,e_2)$; junto con $a_1\in\operatorname{span}(e_1)$ obtenemos la igualdad.
Para la tercera etapa,

$$
u_3
=
a_3
-\langle a_3,e_1\rangle e_1
-\langle a_3,e_2\rangle e_2.
$$

Por la igualdad ya probada,

$$
e_1,e_2\in\operatorname{span}(a_1,a_2),
$$

así que

$$
u_3\in\operatorname{span}(a_1,a_2,a_3).
$$

Luego $e_3$ pertenece al mismo subespacio y obtenemos una inclusión. La inclusión inversa se sigue de

$$
a_3
=
\|u_3\|e_3
+
\langle a_3,e_1\rangle e_1
+
\langle a_3,e_2\rangle e_2.
$$

Por tanto los tres subespacios acumulativos coinciden. $\square$
Esta proposición completa también el argumento de §7.9: la independencia inicial garantiza que $u_2\ne0$ y $u_3\ne0$.

### 7.11. Proposición: el resultado es ortonormal

> **FPM-I-04-P22 — Corrección de Gram–Schmidt**
> Si $(a_1,a_2,a_3)$ es linealmente independiente, el procedimiento D24 está bien definido y produce una familia
>
> $$
> B=(e_1,e_2,e_3)
> $$
>
> ortonormal. Si además $(a_1,a_2,a_3)$ es una base de $V$, entonces $B$ es una base ortonormal de $V$.

**Demostración.** §7.9 y P21 garantizan que todos los $u_i$ son no nulos, por lo que cada normalización está definida y

$$
\|e_i\|=1.
$$

Por P16,

$$
u_2\perp e_1,
$$

y multiplicar $u_2$ por el escalar positivo $1/\|u_2\|$ conserva la ortogonalidad:

$$
e_2\perp e_1.
$$

Para $u_3$, calculamos

$$
\begin{aligned}
\langle u_3,e_1\rangle
&=
\langle a_3,e_1\rangle
-\langle a_3,e_1\rangle\langle e_1,e_1\rangle
-\langle a_3,e_2\rangle\langle e_2,e_1\rangle\\
&=0,
\end{aligned}
$$

porque $\|e_1\|=1$ y $e_2\perp e_1$. De manera análoga,

$$
\langle u_3,e_2\rangle=0.
$$

Al normalizar $u_3$, obtenemos

$$
e_3\perp e_1,
\qquad
e_3\perp e_2.
$$

Así los tres vectores son unitarios y mutuamente ortogonales: forman una familia ortonormal.
Finalmente, si $(a_1,a_2,a_3)$ genera $V$, P21 da

$$
\operatorname{span}(e_1,e_2,e_3)=V.
$$

Una familia ortonormal de vectores no nulos es linealmente independiente: si

$$
c_1e_1+c_2e_2+c_3e_3=0,
$$

tomar producto escalar con $e_k$ da $c_k=0$. Por D09, $B$ es una base. $\square$

### 7.12. El orden importa, el subespacio final no

El procedimiento D24 utiliza un **orden**. Si comenzamos con

$$
(a_1,a_2,a_3)
$$

o con otra permutación de esos vectores, normalmente obtenemos bases ortonormales distintas.
No obstante, P21 garantiza que, para cualquier orden al que pueda aplicarse el procedimiento sobre la misma familia independiente completa, el subespacio final generado es el mismo:

$$
\boxed{
\operatorname{span}(e_1,e_2,e_3)
=
\operatorname{span}(a_1,a_2,a_3).
}
$$

Por tanto Gram–Schmidt no descubre una base ortonormal **canónica** sin datos adicionales. Construye una base ortonormal compatible con el orden elegido.

> **FPM-I-04-MP10 — Ortonormalizar sin perder el espacio generado**
> En Gram–Schmidt, comprobar en cada etapa dos invariantes: el nuevo residuo es ortogonal a las direcciones ya construidas y el subespacio generado acumulativo coincide con el de los vectores originales procesados.

### 7.13. Balance antes de los ejemplos y ejercicios

Ya sabemos:

1. reconocer una base ortonormal;
2. recuperar componentes mediante productos escalares;
3. construir una base ortonormal a partir de una familia independiente;
4. demostrar que el procedimiento preserva el subespacio generado.

Todavía falta aplicar el procedimiento en un caso concreto y cerrar el bloque §§4–7 con los ejercicios E014–E015.

### 7.14. Ejemplo guiado: ortonormalizar una base oblicua simple

Sea

$$
F=(f_1,f_2,f_3)
$$

una base ortonormal conocida. Consideremos la familia

$$
a_1=f_1+f_2,
\qquad
a_2=f_2,
\qquad
a_3=f_3.
$$

Es linealmente independiente: si

$$
\alpha a_1+\beta a_2+\gamma a_3=0,
$$

entonces

$$
\alpha f_1+(\alpha+\beta)f_2+\gamma f_3=0,
$$

y la independencia de $F$ obliga a

$$
\alpha=0,
\qquad
\beta=0,
\qquad
\gamma=0.
$$

Aplicamos D24.
Primero,

$$
u_1=a_1=f_1+f_2,
$$

y

$$
\|u_1\|
=
\sqrt{2}.
$$

Por tanto,

$$
\boxed{
e_1
=
\frac{f_1+f_2}{\sqrt2}.
}
$$

Para el segundo vector,

$$
\langle a_2,e_1\rangle
=
\left\langle
f_2,
\frac{f_1+f_2}{\sqrt2}
\right\rangle
=
\frac1{\sqrt2}.
$$

Entonces

$$
\begin{aligned}
u_2
&=
a_2-\langle a_2,e_1\rangle e_1\\
&=
f_2
-
\frac1{\sqrt2}
\frac{f_1+f_2}{\sqrt2}\\
&=
-\frac12f_1+\frac12f_2.
\end{aligned}
$$

Su norma es

$$
\|u_2\|
=
\frac1{\sqrt2},
$$

de modo que

$$
\boxed{
e_2
=
\frac{-f_1+f_2}{\sqrt2}.
}
$$

Finalmente, como $f_3$ es ortogonal a $e_1$ y $e_2$,

$$
u_3=f_3,
\qquad
\boxed{e_3=f_3.}
$$

La base obtenida es

$$
\boxed{
B=
\left(
\frac{f_1+f_2}{\sqrt2},
\frac{-f_1+f_2}{\sqrt2},
f_3
\right).
}
$$

Una comprobación directa da

$$
\langle e_i,e_j\rangle
=
\delta_{ij}.
$$

Gram–Schmidt no ha cambiado el espacio generado:

$$
\operatorname{span}(a_1,a_2,a_3)
=
\operatorname{span}(e_1,e_2,e_3)
=
V.
$$

[]{#fispm-t1-c04-e0014}

### 7.15. Ejercicio FPM-I-04-E014 — Ejecutar Gram–Schmidt y auditar cada etapa

> **Función pedagógica:** `Construcción → Verificación → Preservación del generado`
>
> Sea $F=(f_1,f_2,f_3)$ una base ortonormal y
>
> $$
> a_1=f_1+f_2,
> \qquad
> a_2=f_2,
> \qquad
> a_3=f_3.
> $$
>
> 1. Aplica Gram–Schmidt en el orden dado.
> 2. Comprueba que los residuos que se normalizan son no nulos.
> 3. Verifica directamente que la familia final es ortonormal.
> 4. Comprueba que
>
> $$
> \operatorname{span}(a_1,a_2)
> =
> \operatorname{span}(e_1,e_2).
> $$

> **Solución desarrollada**
>
> El primer paso da
>
> $$
> e_1
> =
> \frac{f_1+f_2}{\sqrt2}.
> $$
>
> Después,
>
> $$
> u_2
> =
> f_2-\frac12(f_1+f_2)
> =
> -\frac12f_1+\frac12f_2
> \ne0,
> $$
>
> y
>
> $$
> e_2
> =
> \frac{-f_1+f_2}{\sqrt2}.
> $$
>
> Como $f_3$ es ortogonal a los dos primeros,
>
> $$
> u_3=f_3\ne0,
> \qquad
> e_3=f_3.
> $$
>
> Las normas son uno y
>
> $$
> \langle e_1,e_2\rangle
> =
> \frac{-1+1}{2}
> =
> 0,
> $$
>
> mientras
>
> $$
> \langle e_1,e_3\rangle
> =
> \langle e_2,e_3\rangle
> =
> 0.
> $$
>
> Para el generado,
>
> $$
> e_1,e_2
> \in
> \operatorname{span}(f_1,f_2)
> =
> \operatorname{span}(a_1,a_2).
> $$
>
> Recíprocamente,
>
> $$
> a_1
> =
> \sqrt2\,e_1,
> $$
>
> y, usando
>
> $$
> f_2
> =
> \frac{e_1+e_2}{\sqrt2},
> $$
>
> obtenemos
>
> $$
> a_2
> =
> \frac{e_1+e_2}{\sqrt2}.
> $$
>
> Por tanto,
>
> $$
> \boxed{
> \operatorname{span}(a_1,a_2)
> =
> \operatorname{span}(e_1,e_2).
> }
> $$

[]{#fispm-t1-c04-e0015}

### 7.16. Ejercicio FPM-I-04-E015 — Recuperar componentes y norma en la nueva base

> **Función pedagógica:** `Producto escalar → Componentes → Reconstrucción → Parseval finito`
>
> En la base ortonormal
>
> $$
> B=
> \left(
> e_1,e_2,e_3
> \right)
> =
> \left(
> \frac{f_1+f_2}{\sqrt2},
> \frac{-f_1+f_2}{\sqrt2},
> f_3
> \right),
> $$
>
> sea
>
> $$
> v=3f_1+f_2+2f_3.
> $$
>
> 1. Calcula $\langle v,e_1\rangle$, $\langle v,e_2\rangle$, $\langle v,e_3\rangle$.
> 2. Escribe $[v]_B$.
> 3. Reconstruye $v$ desde esas componentes.
> 4. Verifica
>
> $$
> \|v\|^2
> =
> \sum_{i=1}^{3}
> \langle v,e_i\rangle^2.
> $$

> **Solución desarrollada**
>
> Primero,
>
> $$
> \langle v,e_1\rangle
> =
> \frac{3+1}{\sqrt2}
> =
> 2\sqrt2.
> $$
>
> Luego,
>
> $$
> \langle v,e_2\rangle
> =
> \frac{-3+1}{\sqrt2}
> =
> -\sqrt2.
> $$
>
> Finalmente,
>
> $$
> \langle v,e_3\rangle
> =
> 2.
> $$
>
> Por P20,
>
> $$
> \boxed{
> [v]_B
> =
> \begin{pmatrix}
> 2\sqrt2\\
> -\sqrt2\\
> 2
> \end{pmatrix}.
> }
> $$
>
> La reconstrucción es
>
> $$
> \begin{aligned}
> v
> &=
> 2\sqrt2\,e_1
> -\sqrt2\,e_2
> +2e_3\\
> &=
> 2(f_1+f_2)
> +(f_1-f_2)
> +2f_3\\
> &=
> 3f_1+f_2+2f_3.
> \end{aligned}
> $$
>
> Finalmente,
>
> $$
> \|v\|^2
> =
> 3^2+1^2+2^2
> =
> 14
> $$
>
> en la base ortonormal $F$, mientras que
>
> $$
> (2\sqrt2)^2+(-\sqrt2)^2+2^2
> =
> 8+2+4
> =
> 14.
> $$
>
> Por tanto,
>
> $$
> \boxed{
> \|v\|^2
> =
> \sum_{i=1}^{3}
> \langle v,e_i\rangle^2.
> }
> $$

### 7.17. Cierre de §7

La secuencia §§5–7 ha construido progresivamente la geometría euclídea:

$$
\boxed{
\text{producto escalar}
\longrightarrow
\text{norma y distancia}
\longrightarrow
\text{proyección y ángulo}
\longrightarrow
\text{base ortonormal}.
}
$$

Una base ortonormal es especial porque reúne la estructura algebraica de una base y la estructura métrica del producto escalar. Sólo bajo esta hipótesis quedan justificadas simultáneamente las fórmulas

$$
\boxed{
v^i=\langle v,e_i\rangle,
}
$$

$$
\boxed{
v
=
\sum_i
\langle v,e_i\rangle e_i,
}
$$

y

$$
\boxed{
\|v\|^2
=
\sum_i(v^i)^2.
}
$$

Gram–Schmidt demuestra además que, a partir de una base cualquiera de un espacio euclídeo finito, podemos construir una base ortonormal sin cambiar el espacio generado.
Con ello queda cerrada la construcción métrica iniciada en §4.
El siguiente paso será:

$$
\boxed{
\text{§8 — Orientación y determinantes}
}
$$

---

[]{#fispm-t1-c04-s08}

[]{#fpm-i-04-s08}

## §8 — Orientación y determinantes

### 8.1. Activación: una base ordenada puede tener dos “sentidos”

Una base ordenada tridimensional

$$
B=(b_1,b_2,b_3)
$$

no sólo proporciona tres direcciones independientes. El **orden** de esas direcciones contiene información adicional.
Si intercambiamos dos vectores, por ejemplo

$$
B'=(b_2,b_1,b_3),
$$

seguimos teniendo los mismos tres vectores y el mismo espacio generado. Sin embargo, hemos invertido algo que no puede detectarse mediante longitudes ni ángulos por sí solos.
Ese dato adicional es la **orientación**.
Para describirlo necesitamos una cantidad algebraica que:

- se anule cuando los tres vectores dejan de ser independientes;
- cambie de signo cuando intercambiamos dos de ellos;
- permita distinguir dos clases de bases ordenadas.

Esa cantidad es el determinante.

### 8.2. Definir: determinante de una matriz real 3 × 3

> **FPM-I-04-D25 — Determinante tridimensional**
> Para
>
> $$
> A=
> \begin{pmatrix}
> a_{11}&a_{12}&a_{13}\\
> a_{21}&a_{22}&a_{23}\\
> a_{31}&a_{32}&a_{33}
> \end{pmatrix},
> $$
>
> definimos
>
> $$
> \boxed{
> \begin{aligned}
> \det A
> &=
> a_{11}a_{22}a_{33}
> +a_{12}a_{23}a_{31}
> +a_{13}a_{21}a_{32}\\
> &\quad
> -a_{13}a_{22}a_{31}
> -a_{12}a_{21}a_{33}
> -a_{11}a_{23}a_{32}.
> \end{aligned}
> }
> $$

Esta expresión es un escalar asociado a una matriz cuadrada de orden tres.
En particular,

$$
\det I_3=1.
$$

Todavía no interpretamos el valor absoluto como volumen; por ahora nos interesa principalmente su **signo**.

### 8.3. Determinante de una terna de vectores respecto de una base

Fijemos temporalmente una base ordenada de referencia

$$
E=(e_1,e_2,e_3).
$$

Para tres vectores $v_1,v_2,v_3\in V$, formamos la matriz cuyas columnas son sus componentes en $E$:

$$
A_E(v_1,v_2,v_3)
:=
\begin{pmatrix}
\vert&\vert&\vert\\
[v_1]_E&[v_2]_E&[v_3]_E\\
\vert&\vert&\vert
\end{pmatrix}.
$$

Definimos entonces la abreviatura

$$
\boxed{
\det_E(v_1,v_2,v_3)
:=
\det A_E(v_1,v_2,v_3).
}
$$

Si tomamos precisamente la terna de referencia,

$$
\det_E(e_1,e_2,e_3)=1.
$$

### 8.4. Primera propiedad: intercambiar dos columnas cambia el signo

> **FPM-I-04-P23 — Regla de intercambio**
> Si $A'$ se obtiene de una matriz $A$ intercambiando dos columnas, entonces
>
> $$
> \boxed{
> \det A'=-\det A.
> }
> $$
>
> En particular,
>
> $$
> \boxed{
> \det_E(v_2,v_1,v_3)
> =
> -\det_E(v_1,v_2,v_3).
> }
> $$

**Demostración.** Basta comprobar un intercambio elemental, por ejemplo las dos primeras columnas. Escribimos

$$
A=
\begin{pmatrix}
a&b&c\\
d&e&f\\
g&h&i
\end{pmatrix},
$$

de modo que

$$
\det A
=
aei+bfg+cdh-ceg-bdi-afh.
$$

Tras intercambiar las dos primeras columnas,

$$
A'=
\begin{pmatrix}
b&a&c\\
e&d&f\\
h&g&i
\end{pmatrix}.
$$

Por D25,

$$
\det A'
=
bdi+afh+ceg-cdh-aei-bfg.
$$

Reordenando términos,

$$
\det A'
=
-\bigl(aei+bfg+cdh-ceg-bdi-afh\bigr)
=
-\det A.
$$

Los demás intercambios se comprueban de la misma manera. $\square$
La regla de signo no depende de longitudes ni de ortogonalidad. Es consecuencia de la estructura algebraica del determinante.

### 8.5. Consecuencia: una permutación impar invierte el signo

Si partimos de

$$
(v_1,v_2,v_3)
$$

y realizamos un solo intercambio, el determinante cambia de signo.
Dos intercambios sucesivos producen

$$
(-1)^2=1,
$$

por lo que restauran el signo original.
Por ejemplo,

$$
(v_1,v_2,v_3)
\longrightarrow
(v_2,v_1,v_3)
\longrightarrow
(v_2,v_3,v_1)
$$

realiza dos intercambios y conserva el signo.
Esto anticipa la distinción entre permutaciones **pares** e **impares**, pero no necesitamos todavía formalizar el grupo de permutaciones.

### 8.6. Definir: orientación relativa a una base de referencia

> **FPM-I-04-D26 — Orientación relativa**
> Fijemos una base ordenada de referencia
>
> $$
> E=(e_1,e_2,e_3).
> $$
>
> Sea
>
> $$
> B=(b_1,b_2,b_3)
> $$
>
> otra base ordenada. Diremos que $B$ tiene **orientación positiva respecto de $E$** si
>
> $$
> \boxed{
> \det_E(b_1,b_2,b_3)>0,
> }
> $$
>
> y **orientación negativa respecto de $E$** si
>
> $$
> \boxed{
> \det_E(b_1,b_2,b_3)<0.
> }
> $$

Como $B$ es una base, esperamos que el determinante no sea cero. La demostración general de la equivalencia

$$
\det A\ne0
\Longleftrightarrow
\text{columnas independientes}
$$

se demostrará en §§8.9–8.12, junto con las propiedades estructurales necesarias del determinante.
Por ahora, D26 se aplica a las bases para las que ya hemos verificado directamente que el determinante es no nulo.

### 8.7. Ejemplo inmediato: invertir dos ejes

La base de referencia satisface

$$
\det_E(e_1,e_2,e_3)=1>0.
$$

Por P23,

$$
\det_E(e_2,e_1,e_3)=-1.
$$

Por tanto,

$$
(e_1,e_2,e_3)
$$

y

$$
(e_2,e_1,e_3)
$$

poseen orientaciones relativas opuestas.
Sin embargo, ambas bases tienen exactamente los mismos vectores y, si $E$ era ortonormal, la base obtenida al intercambiar dos elementos también es ortonormal.

> Ortonormalidad no fija la orientación
> Una base puede conservar todas las longitudes y todos los ángulos entre sus vectores y, aun así, invertir la orientación al intercambiar dos ejes.

### 8.8. Principio metodológico y cuestiones pendientes

> **FPM-I-04-MP11 — Separar métrica y orientación**
> Longitudes, ángulos y ortonormalidad pertenecen a la estructura métrica; la orientación añade un dato de signo asociado al orden de una base. No inferir orientación únicamente a partir de productos escalares.

Hasta aquí hemos introducido:

$$
\boxed{
\det A
}
$$

como escalar algebraico y hemos aislado su papel más elemental:

$$
\boxed{
\text{intercambiar dos vectores}
\Longrightarrow
\text{cambiar el signo del determinante}.
}
$$

Esto permite hablar de orientación **relativa a una base elegida**, pero todavía falta demostrar de manera sistemática:

- cuándo el determinante es cero;
- cómo se comporta bajo combinaciones lineales;
- cómo se relacionan orientaciones definidas usando distintas bases de referencia.

### 8.9. Proposición: multilinealidad y alternancia

> **FPM-I-04-P24 — El determinante es trilineal y alternante**
> Fijada una base de referencia $E$, la aplicación
>
> $$
> (v_1,v_2,v_3)
> \longmapsto
> \det_E(v_1,v_2,v_3)
> $$
>
> es lineal en cada argumento por separado. Además, si dos argumentos coinciden, entonces
>
> $$
> \boxed{
> \det_E(v_1,v_2,v_3)=0.
> }
> $$

**Demostración de la linealidad en el primer argumento.** Sean $u,w,v_2,v_3\in V$ y $\alpha,\beta\in\mathbb R$. Por linealidad de las coordenadas,

$$
[\alpha u+\beta w]_E
=
\alpha[u]_E+\beta[w]_E.
$$

Al sustituir esta columna en la fórmula explícita D25, cada término depende linealmente de las entradas de la primera columna. Por tanto,

$$
\boxed{
\det_E(\alpha u+\beta w,v_2,v_3)
=
\alpha\det_E(u,v_2,v_3)
+
\beta\det_E(w,v_2,v_3).
}
$$

La misma inspección de D25 prueba linealidad en la segunda y tercera columnas.
Para la alternancia, si las dos primeras columnas coinciden, P23 da simultáneamente

$$
\det_E(v,v,v_3)
=
-\det_E(v,v,v_3).
$$

Luego

$$
2\det_E(v,v,v_3)=0,
$$

y como trabajamos sobre $\mathbb R$,

$$
\det_E(v,v,v_3)=0.
$$

Los demás casos se reducen a éste intercambiando columnas. $\square$

### 8.10. Consecuencia: dependencia lineal implica determinante cero

> **FPM-I-04-P25 — Una terna dependiente tiene determinante nulo**
> Si $v_1,v_2,v_3$ son linealmente dependientes, entonces
>
> $$
> \boxed{
> \det_E(v_1,v_2,v_3)=0.
> }
> $$

**Demostración.** Si uno de los vectores es cero, la multilinealidad da inmediatamente determinante cero.
Supongamos entonces que ninguno es cero y que, por ejemplo,

$$
v_3=\alpha v_1+\beta v_2.
$$

Por linealidad en el tercer argumento,

$$
\begin{aligned}
\det_E(v_1,v_2,v_3)
&=
\det_E(v_1,v_2,\alpha v_1+\beta v_2)\\
&=
\alpha\det_E(v_1,v_2,v_1)
+
\beta\det_E(v_1,v_2,v_2).
\end{aligned}
$$

Cada término se anula por alternancia. Luego

$$
\det_E(v_1,v_2,v_3)=0.
$$

Si la relación de dependencia despeja otro vector, el argumento es idéntico. $\square$
La implicación recíproca todavía requiere una propiedad adicional: la multiplicatividad.

### 8.11. Proposición: multiplicatividad del determinante

> **FPM-I-04-P26 — Determinante de un producto**
> Para matrices reales $3\times3$,
>
> $$
> \boxed{
> \det(AB)=\det(A)\det(B).
> }
> $$

**Demostración.** Escribamos las columnas de $A$ como

$$
A=
\begin{pmatrix}
\vert&\vert&\vert\\
a_1&a_2&a_3\\
\vert&\vert&\vert
\end{pmatrix},
$$

y las de $B$ mediante sus entradas $b_{ij}$. La columna $j$ de $AB$ es

$$
b_{1j}a_1+b_{2j}a_2+b_{3j}a_3.
$$

Por trilinealidad,

$$
\det(AB)
$$

se expande como suma de términos de la forma

$$
b_{i1}b_{j2}b_{k3}\det(a_i,a_j,a_k).
$$

Todo término con índices repetidos se anula por alternancia. Sólo sobreviven las seis permutaciones de $(1,2,3)$.
Cada permutación aporta

$$
\pm
b_{i1}b_{j2}b_{k3}\det(a_1,a_2,a_3),
$$

donde el signo es precisamente el signo de la permutación, por P23. Factorizando,

$$
\det(AB)
=
\det(A)
\Bigl(
b_{11}b_{22}b_{33}
+b_{21}b_{32}b_{13}
+b_{31}b_{12}b_{23}
-b_{31}b_{22}b_{13}
-b_{21}b_{12}b_{33}
-b_{11}b_{32}b_{23}
\Bigr).
$$

La expresión entre paréntesis es exactamente $\det(B)$ escrita por columnas. Por tanto,

$$
\det(AB)=\det(A)\det(B).
$$

$\square$

### 8.12. Proposición: determinante no nulo e independencia

> **FPM-I-04-P27 — Criterio de base mediante el determinante**
> Sean $v_1,v_2,v_3\in V$ y sea
>
> $$
> A=
> A_E(v_1,v_2,v_3).
> $$
>
> Entonces
>
> $$
> \boxed{
> \det A\ne0
> \Longleftrightarrow
> (v_1,v_2,v_3)
> \text{ es linealmente independiente}.
> }
> $$
>
> En dimensión tres, esto equivale a que $(v_1,v_2,v_3)$ sea una base de $V$.

**Demostración.**
Si la terna es dependiente, P25 da

$$
\det A=0.
$$

Por contraposición,

$$
\det A\ne0
\Longrightarrow
(v_1,v_2,v_3)
\text{ independiente}.
$$

Para la otra dirección, supongamos que

$$
B=(v_1,v_2,v_3)
$$

es una base. Como $E$ también es base, cada $e_j$ posee coordenadas únicas en $B$. Sea $C$ la matriz cuyas columnas son esas coordenadas:

$$
C=
\begin{pmatrix}
\vert&\vert&\vert\\
[e_1]_B&[e_2]_B&[e_3]_B\\
\vert&\vert&\vert
\end{pmatrix}.
$$

La matriz $A$ convierte componentes en $B$ a componentes en $E$, de modo que

$$
AC=I_3.
$$

Aplicando P26,

$$
1
=
\det I_3
=
\det(A)\det(C).
$$

Por tanto,

$$
\det(A)\ne0.
$$

Esto prueba la equivalencia. $\square$
La observación pendiente de §8.6 queda ahora justificada: toda base ordenada tiene determinante no nulo respecto de cualquier base de referencia.

### 8.13. Definir: misma orientación entre bases

> **FPM-I-04-D27 — Bases con la misma orientación**
> Sean
>
> $$
> B=(b_1,b_2,b_3),
> \qquad
> C=(c_1,c_2,c_3)
> $$
>
> bases ordenadas de $V$. Diremos que $B$ y $C$ tienen la **misma orientación** si la matriz de cambio de componentes de $C$ a $B$ tiene determinante positivo.
>
> Equivalentemente, fijada cualquier base de referencia $E$,
>
> $$
> \boxed{
> \det_E(B)\det_E(C)>0.
> }
> $$
>
> Tienen **orientaciones opuestas** si ese producto es negativo.

Aquí usamos la abreviatura

$$
\det_E(B)
:=
\det_E(b_1,b_2,b_3).
$$

La equivalencia entre ambas formulaciones se justificará de inmediato.

### 8.14. Proposición: la comparación de orientación no depende de la referencia

> **FPM-I-04-P28 — Invariancia de la comparación de orientación**
> El signo de
>
> $$
> \det_E(B)\det_E(C)
> $$
>
> no depende de la base de referencia $E$.

**Demostración.** Sea $F$ otra base de referencia. Denotemos por $S$ la matriz cuyas columnas son los vectores de $F$ expresados en $E$. Entonces, para cualquier base $B$,

$$
A_E(B)
=
S\,A_F(B).
$$

Por P26,

$$
\det_E(B)
=
\det(S)\det_F(B).
$$

Análogamente,

$$
\det_E(C)
=
\det(S)\det_F(C).
$$

Por tanto,

$$
\det_E(B)\det_E(C)
=
\det(S)^2
\det_F(B)\det_F(C).
$$

Como $F$ es una base, P27 garantiza

$$
\det(S)\ne0,
$$

y por ello

$$
\det(S)^2>0.
$$

Multiplicar por un número positivo no cambia el signo. Luego ambas referencias producen la misma comparación de orientación. $\square$

### 8.15. Las bases se separan en dos clases

D27 y P28 permiten olvidar una base de referencia particular y hablar simplemente de dos clases de bases ordenadas.
Fijada una base $E$:

- todas las bases con
  $$
  \det_E(B)>0
  $$
  pertenecen a una clase;
- todas las bases con
  $$
  \det_E(B)<0
  $$
  pertenecen a la otra.
P23 muestra que intercambiar dos vectores de una base pasa de una clase a la otra.
Dos intercambios restauran la clase original.

> **FPM-I-04-MP12 — La orientación es una clase, no un número**
> El valor concreto de un determinante depende de la base usada para expresar los vectores; la orientación conserva sólo la información de signo relativa entre bases. Al cambiar de referencia, distinguir el factor de escala del dato binario de orientación.

### 8.16. Balance: de la orientación al volumen

Ya disponemos de la estructura mínima necesaria:

$$
\boxed{
\text{trilinealidad}
+
\text{alternancia}
+
\text{multiplicatividad}
}
$$

y de sus dos consecuencias centrales:

$$
\boxed{
\det A\ne0
\Longleftrightarrow
\text{columnas independientes},
}
$$

$$
\boxed{
\text{las bases ordenadas se dividen en dos clases de orientación}.
}
$$

Todavía falta interpretar geométricamente el **valor absoluto** del determinante y conectar esa interpretación con volumen, ortonormalidad y los ejercicios de §8.

### 8.17. Reglas geométricas que ya contiene el determinante

P24 y P23 permiten leer tres operaciones elementales directamente en el determinante.
Si multiplicamos una arista por un escalar $\lambda$,

$$
\det_E(\lambda v_1,v_2,v_3)
=
\lambda\det_E(v_1,v_2,v_3).
$$

Si añadimos a una arista un múltiplo de otra,

$$
\begin{aligned}
\det_E(v_1+\lambda v_2,v_2,v_3)
&=
\det_E(v_1,v_2,v_3)
+
\lambda\det_E(v_2,v_2,v_3)\\
&=
\det_E(v_1,v_2,v_3).
\end{aligned}
$$

Y si intercambiamos dos aristas,

$$
\det_E(v_2,v_1,v_3)
=
-\det_E(v_1,v_2,v_3).
$$

Estas tres reglas anticipan exactamente el comportamiento geométrico esperado de un volumen orientado:

- escalar una arista escala el volumen;
- una cizalla paralela a otra arista no cambia el volumen;
- intercambiar dos aristas conserva el tamaño pero invierte el signo de orientación.

### 8.18. Definir: volumen orientado y volumen euclídeo

Fijemos ahora una base **ortonormal** y una de las dos clases de orientación como positiva:

$$
E=(e_1,e_2,e_3).
$$

> **FPM-I-04-D28 — Volumen orientado de una terna**
> Para $v_1,v_2,v_3\in V$, definimos el **volumen orientado respecto de $E$** por
>
> $$
> \boxed{
> \operatorname{Vol}^{\mathrm{or}}_E(v_1,v_2,v_3)
> :=
> \det_E(v_1,v_2,v_3).
> }
> $$
>
> El **volumen euclídeo** del paralelepípedo generado por la terna es
>
> $$
> \boxed{
> \operatorname{Vol}(v_1,v_2,v_3)
> :=
> \left|
> \operatorname{Vol}^{\mathrm{or}}_E(v_1,v_2,v_3)
> \right|.
> }
> $$

La ortonormalidad de $E$ es esencial para esta lectura métrica. Si usáramos una base de referencia oblicua y no normalizada, el determinante de coordenadas mediría el volumen en unidades del paralelepípedo fundamental de esa base, no directamente en la escala euclídea normalizada.
**Convención de unidades.** D28 utiliza la normalización matemática fijada en §7. Cuando una realización física introduce una escala común de longitud $\ell_0$, los desplazamientos de referencia $b_i=\ell_0e_i$ aportan un factor $\ell_0^3$ al volumen físico. Así, el valor numérico $|\det_E(v_1,v_2,v_3)|$ debe interpretarse junto con la escala de longitud declarada; si la unidad normalizada es $1\,\mathrm m$, un valor $24$ corresponde a $24\,\mathrm{m^3}$. Para bases dimensionales no normalizadas, debe conservarse además el volumen de su paralelepípedo fundamental.
Por el momento estas expresiones están escritas respecto de $E$. Después de P30 demostraremos que el valor absoluto es independiente de la base ortonormal de referencia y que el signo depende únicamente de la clase de orientación elegida.
El signo registra orientación; el valor absoluto registra tamaño.

### 8.19. Proposición: reglas del volumen orientado

> **FPM-I-04-P29 — Escala, cizalla y orientación del volumen**
> Para toda terna $v_1,v_2,v_3$ y todo $\lambda\in\mathbb R$:
>
> $$
> \boxed{
> \operatorname{Vol}^{\mathrm{or}}_E(\lambda v_1,v_2,v_3)
> =
> \lambda
> \operatorname{Vol}^{\mathrm{or}}_E(v_1,v_2,v_3),
> }
> $$
>
> $$
> \boxed{
> \operatorname{Vol}^{\mathrm{or}}_E(v_1+\lambda v_2,v_2,v_3)
> =
> \operatorname{Vol}^{\mathrm{or}}_E(v_1,v_2,v_3),
> }
> $$
>
> y
>
> $$
> \boxed{
> \operatorname{Vol}^{\mathrm{or}}_E(v_2,v_1,v_3)
> =
> -
> \operatorname{Vol}^{\mathrm{or}}_E(v_1,v_2,v_3).
> }
> $$
>
> En consecuencia, el volumen euclídeo no cambia al intercambiar dos aristas ni al realizar la cizalla anterior.

**Demostración.** Cada identidad es exactamente una aplicación de P24 y P23 a D28. Al tomar valor absoluto, el cambio de signo desaparece. $\square$

### 8.20. Proposición: una base ortonormal tiene determinante ±1

> **FPM-I-04-P30 — Determinante de una base ortonormal**
> Sea
>
> $$
> B=(b_1,b_2,b_3)
> $$
>
> una base ortonormal y sea $E$ una base ortonormal de referencia. Entonces
>
> $$
> \boxed{
> \det_E(B)=\pm1.
> }
> $$
>
> Por tanto,
>
> $$
> \boxed{
> \operatorname{Vol}(b_1,b_2,b_3)=1.
> }
> $$

**Demostración.** Sea

$$
Q=
A_E(b_1,b_2,b_3).
$$

Como $E$ es ortonormal, los productos escalares entre columnas de $Q$ se calculan mediante el producto matricial usual. La ortonormalidad de $B$ equivale a

$$
Q^{\mathsf T}Q=I_3.
$$

Por inspección directa de D25,

$$
\det(Q^{\mathsf T})=\det(Q).
$$

Aplicando P26,

$$
1
=
\det I_3
=
\det(Q^{\mathsf T}Q)
=
\det(Q^{\mathsf T})\det(Q)
=
\det(Q)^2.
$$

Por tanto,

$$
\det(Q)=\pm1.
$$

El valor absoluto es uno. $\square$
Esta proposición separa limpiamente dos posibilidades:

$$
\det_E(B)=+1
$$

si $B$ tiene la misma orientación que $E$, y

$$
\det_E(B)=-1
$$

si tiene la orientación opuesta.

### 8.21. Proposición: independencia de la referencia ortonormal

> **FPM-I-04-P31 — Invariancia del volumen bajo cambio de referencia ortonormal**
> Sean
>
> $$
> E=(e_1,e_2,e_3)
> $$
>
> y
>
> $$
> F=(f_1,f_2,f_3)
> $$
>
> bases ortonormales. Para toda terna $v_1,v_2,v_3$:
>
> 1. si $E$ y $F$ tienen la misma orientación,
>
> $$
> \boxed{
> \det_E(v_1,v_2,v_3)
> =
> \det_F(v_1,v_2,v_3);
> }
> $$
>
> 2. si tienen orientaciones opuestas,
>
> $$
> \boxed{
> \det_E(v_1,v_2,v_3)
> =
> -\det_F(v_1,v_2,v_3);
> }
> $$
>
> 3. en ambos casos,
>
> $$
> \boxed{
> |\det_E(v_1,v_2,v_3)|
> =
> |\det_F(v_1,v_2,v_3)|.
> }
> $$
>
> Por tanto, una vez fijada una clase de orientación positiva, el volumen orientado es independiente de la base ortonormal positiva elegida, y el volumen euclídeo es independiente de cualquier base ortonormal de referencia.

**Demostración.** Sea

$$
S=A_E(f_1,f_2,f_3).
$$

Para la terna

$$
V=(v_1,v_2,v_3),
$$

las matrices de componentes satisfacen

$$
A_E(V)
=
S\,A_F(V).
$$

Por P26,

$$
\det_E(V)
=
\det(S)\det_F(V).
$$

Como $E$ y $F$ son ortonormales, P30 da

$$
\det(S)=\pm1.
$$

Si tienen la misma orientación, D27 implica

$$
\det(S)=+1,
$$

y los volúmenes orientados coinciden. Si tienen orientaciones opuestas,

$$
\det(S)=-1,
$$

y los volúmenes orientados cambian de signo. En ambos casos, tomar valor absoluto elimina el signo. $\square$
Esta proposición completa la justificación intrínseca de D28: podemos escribir sin ambigüedad

$$
\operatorname{Vol}(v_1,v_2,v_3)
$$

sin indicar una base ortonormal particular.

### 8.22. Ejemplo guiado: cizalla, escala y orientación

Sea $E=(e_1,e_2,e_3)$ una base ortonormal positivamente orientada y definamos

$$
v_1=2e_1,
\qquad
v_2=e_1+3e_2,
\qquad
v_3=2e_1-e_2+4e_3.
$$

La matriz de columnas es

$$
A=
\begin{pmatrix}
2&1&2\\
0&3&-1\\
0&0&4
\end{pmatrix}.
$$

Por D25,

$$
\det A=2\cdot3\cdot4=24.
$$

Por tanto,

$$
\boxed{
\operatorname{Vol}^{\mathrm{or}}_E(v_1,v_2,v_3)=24,
}
$$

y

$$
\boxed{
\operatorname{Vol}(v_1,v_2,v_3)=24.
}
$$

Los términos $e_1$ añadidos a $v_2$ y $2e_1-e_2$ añadidos a $v_3$ actúan como cizallas: modifican la forma del paralelepípedo, pero no el producto final de los factores independientes $2$, $3$ y $4$.
Si intercambiamos $v_1$ y $v_2$,

$$
\operatorname{Vol}^{\mathrm{or}}_E(v_2,v_1,v_3)
=
-24,
$$

mientras

$$
\operatorname{Vol}(v_2,v_1,v_3)
=
24.
$$

[]{#fispm-t1-c04-e0016}

### 8.23. Ejercicio FPM-I-04-E016 — Determinante, volumen y orientación

> **Función pedagógica:** `Cálculo → Interpretación geométrica → Separación signo/magnitud`
>
> Sea $E=(e_1,e_2,e_3)$ una base ortonormal positivamente orientada y
>
> $$
> v_1=2e_1,
> \qquad
> v_2=e_1+3e_2,
> \qquad
> v_3=2e_1-e_2+4e_3.
> $$
>
> 1. Calcula $\det_E(v_1,v_2,v_3)$.
> 2. Determina el volumen euclídeo del paralelepípedo.
> 3. Decide si la terna tiene la misma orientación que $E$.
> 4. Repite las preguntas para $(v_2,v_1,v_3)$.

> **Solución desarrollada**
>
> La matriz es
>
> $$
> A=
> \begin{pmatrix}
> 2&1&2\\
> 0&3&-1\\
> 0&0&4
> \end{pmatrix}.
> $$
>
> Por D25,
>
> $$
> \det A=24.
> $$
>
> Luego
>
> $$
> \boxed{
> \operatorname{Vol}^{\mathrm{or}}_E(v_1,v_2,v_3)=24,
> }
> $$
>
> y
>
> $$
> \boxed{
> \operatorname{Vol}(v_1,v_2,v_3)=24.
> }
> $$
>
> Como el determinante es positivo, la terna tiene la misma orientación que $E$.
>
> Al intercambiar los dos primeros vectores, P23 da
>
> $$
> \det_E(v_2,v_1,v_3)=-24.
> $$
>
> El volumen euclídeo permanece
>
> $$
> \boxed{24},
> $$
>
> pero la orientación se invierte.

[]{#fispm-t1-c04-e0017}

### 8.24. Ejercicio FPM-I-04-E017 — Qué operaciones cambian volumen y orientación

> **Función pedagógica:** `Transformaciones elementales → Invariantes → Diagnóstico`
>
> Partimos de una base ortonormal positivamente orientada
>
> $$
> E=(e_1,e_2,e_3),
> $$
>
> cuyo volumen orientado vale $1$. Para cada operación, determina el nuevo volumen orientado, el volumen euclídeo y si la orientación se conserva:
>
> 1. sustituir $e_1$ por $3e_1$;
> 2. sustituir $e_1$ por $-e_1$;
> 3. sustituir $e_1$ por $e_1+5e_2$;
> 4. intercambiar $e_1$ y $e_2$.

> **Solución desarrollada**
>
> **1. Escala positiva.**
>
> $$
> \operatorname{Vol}^{\mathrm{or}}_E(3e_1,e_2,e_3)=3.
> $$
>
> El volumen euclídeo pasa a $3$ y la orientación se conserva.
>
> **2. Escala negativa.**
>
> $$
> \operatorname{Vol}^{\mathrm{or}}_E(-e_1,e_2,e_3)=-1.
> $$
>
> El volumen euclídeo sigue siendo $1$, pero la orientación se invierte.
>
> **3. Cizalla.**
>
> Por P29,
>
> $$
> \operatorname{Vol}^{\mathrm{or}}_E(e_1+5e_2,e_2,e_3)=1.
> $$
>
> No cambia ni el volumen euclídeo ni la orientación.
>
> **4. Intercambio.**
>
> $$
> \operatorname{Vol}^{\mathrm{or}}_E(e_2,e_1,e_3)=-1.
> $$
>
> El volumen euclídeo sigue siendo $1$ y la orientación se invierte.

### 8.25. Cierre de §8

La sección ha separado tres capas distintas:

$$
\boxed{
\text{independencia lineal}
\quad\longleftrightarrow\quad
\det\ne0,
}
$$

$$
\boxed{
\text{orientación}
\quad\longleftrightarrow\quad
\operatorname{sgn}(\det),
}
$$

y, cuando la referencia es ortonormal,

$$
\boxed{
\text{volumen euclídeo}
\quad\longleftrightarrow\quad
|\det|.
}
$$

El determinante contiene así simultáneamente información algebraica, orientacional y métrica, pero cada lectura requiere sus hipótesis precisas.

> **FPM-I-04-MP13 — Separar cero, signo y magnitud del determinante**
> Antes de interpretar un determinante, preguntar qué información se está usando:
>
> - `det = 0`: pérdida de independencia;
> - `sgn(det)`: clase de orientación;
> - `|det|`: factor de volumen cuando la referencia métrica está normalizada.

La sección termina exactamente donde comienza la siguiente necesidad tridimensional: construir, a partir de dos vectores y una orientación elegida, un tercer vector perpendicular cuya magnitud codifique un área.
Esa construcción será el objeto de §9.
El siguiente paso será:

$$
\boxed{
\text{§9 — Producto vectorial en dimensión tres}
}
$$

---

[]{#fispm-t1-c04-s09}

[]{#fpm-i-04-s09}

## §9 — Producto vectorial en dimensión tres

### 9.1. Activación: de dos vectores a una normal orientada

Sean

$$
u,v\in V.
$$

Los dos vectores determinan, cuando son linealmente independientes, un plano vectorial

$$
\operatorname{span}(u,v).
$$

En dimensión tres aparece una posibilidad especial: podemos buscar un tercer vector que sea perpendicular a ese plano y cuya magnitud mida el área del paralelogramo generado por $u$ y $v$.
Pero quedan dos elecciones que una simple condición de perpendicularidad no resuelve:

1. hay dos sentidos opuestos en la recta perpendicular al plano;
2. la magnitud debe fijarse de manera compatible con el área.

La orientación construida en §8 resuelve el primer problema; el producto escalar resuelve el segundo.
Por eso el producto vectorial no pertenece a la estructura lineal desnuda de $V$.

### 9.2. Los dos ingredientes que necesita la construcción

Para definir $u\times v$ necesitamos simultáneamente:

- el producto escalar
  $$
  \langle\cdot,\cdot\rangle,
  $$
  que permite identificar vectores con funcionales lineales mediante la regla
  $$
  x\longmapsto \langle x,\cdot\rangle;
  $$

- una clase de orientación positiva, que fija el signo del volumen orientado
  $$
  \operatorname{Vol}^{\mathrm{or}}(u,v,w).
  $$

P31 garantiza que, una vez fijada la orientación positiva, este volumen orientado es independiente de la base ortonormal positiva usada para calcularlo.
Así, para $u$ y $v$ fijos, la aplicación

$$
w
\longmapsto
\operatorname{Vol}^{\mathrm{or}}(u,v,w)
$$

es un funcional lineal sobre $V$, por P24.
La pregunta central es:

> Existencia y unicidad
> ¿Existe un único vector $x\in V$ tal que
>
> $$
> \langle x,w\rangle
> =
> \operatorname{Vol}^{\mathrm{or}}(u,v,w)
> $$
>
> para todo $w\in V$?

### 9.3. Proposición: representación vectorial del volumen orientado

> **FPM-I-04-P32 — Existencia y unicidad del vector representante**
> Para cada par $u,v\in V$ existe un único vector $x\in V$ tal que
>
> $$
> \boxed{
> \langle x,w\rangle
> =
> \operatorname{Vol}^{\mathrm{or}}(u,v,w)
> }
> $$
>
> para todo $w\in V$.

**Demostración de existencia.** Elegimos una base ortonormal positivamente orientada

$$
E=(e_1,e_2,e_3).
$$

Definimos

$$
x
:=
\sum_{k=1}^{3}
\operatorname{Vol}^{\mathrm{or}}(u,v,e_k)e_k.
$$

Sea ahora

$$
w
=
\sum_{k=1}^{3}
w^ke_k.
$$

Por P20,

$$
w^k=\langle w,e_k\rangle.
$$

Como $E$ es ortonormal,

$$
\begin{aligned}
\langle x,w\rangle
&=
\left\langle
\sum_{k=1}^{3}
\operatorname{Vol}^{\mathrm{or}}(u,v,e_k)e_k,
\sum_{j=1}^{3}w^je_j
\right\rangle\\
&=
\sum_{k=1}^{3}
\operatorname{Vol}^{\mathrm{or}}(u,v,e_k)w^k.
\end{aligned}
$$

Por linealidad del volumen orientado en el tercer argumento,

$$
\begin{aligned}
\operatorname{Vol}^{\mathrm{or}}(u,v,w)
&=
\operatorname{Vol}^{\mathrm{or}}
\left(
u,v,
\sum_{k=1}^{3}w^ke_k
\right)\\
&=
\sum_{k=1}^{3}
w^k
\operatorname{Vol}^{\mathrm{or}}(u,v,e_k).
\end{aligned}
$$

Por tanto,

$$
\langle x,w\rangle
=
\operatorname{Vol}^{\mathrm{or}}(u,v,w).
$$

**Demostración de unicidad.** Supongamos que $x$ e $y$ satisfacen la misma condición. Entonces, para todo $w\in V$,

$$
\langle x-y,w\rangle=0.
$$

Tomamos

$$
w=x-y.
$$

Así,

$$
\|x-y\|^2
=
\langle x-y,x-y\rangle
=
0.
$$

Por positividad definida,

$$
x-y=0,
$$

y por tanto

$$
x=y.
$$

$\square$

La construcción utilizó una base ortonormal positiva para demostrar existencia, pero el vector obtenido no depende de esa base: la condición que lo caracteriza es intrínseca y P32 asegura unicidad.

### 9.4. Definir: producto vectorial

> **FPM-I-04-D29 — Producto vectorial en un espacio euclídeo orientado de dimensión tres**
> Para $u,v\in V$, definimos su **producto vectorial**
>
> $$
> \boxed{
> u\times v
> }
> $$
>
> como el único vector cuya existencia y unicidad garantiza P32, caracterizado por
>
> $$
> \boxed{
> \langle u\times v,w\rangle
> =
> \operatorname{Vol}^{\mathrm{or}}(u,v,w)
> }
> $$
>
> para todo $w\in V$.

Esta identidad es la definición geométrica fundamental del producto vectorial en este capítulo.
No depende de haber elegido una base concreta para escribir componentes.

> Tipo físico y unidades
> D29 define una operación en el espacio euclídeo abstracto una vez fijadas métrica y orientación. Si, en una realización física, $u$ y $v$ representan desplazamientos con dimensión $L$, entonces P37 implica
>
> $$
> \|u\times v\|\sim L^2.
> $$
>
> Por tanto, $u\times v$ debe interpretarse dimensionalmente como un **vector de área orientada**, no como otro desplazamiento. Una forma segura de llevar las unidades es escribir $u=\ell_0\bar u$ y $v=\ell_0\bar v$, con $\bar u,\bar v$ en el espacio direccional normalizado; entonces el vector de área físico es
>
> $$
> \ell_0^2(\bar u\times\bar v).
> $$
>
> Reutilizar $V$ para codificar su dirección no autoriza a sumar $u\times v$ con un desplazamiento ni a interpretar automáticamente sus componentes en metros. El tipo de magnitud y la escala deben conservarse explícitos.

### 9.5. Primeras consecuencias sin coordenadas

Tomemos

$$
w=u.
$$

Entonces

$$
\langle u\times v,u\rangle
=
\operatorname{Vol}^{\mathrm{or}}(u,v,u).
$$

Como el volumen orientado es alternante,

$$
\operatorname{Vol}^{\mathrm{or}}(u,v,u)=0.
$$

Por tanto,

$$
\boxed{
u\times v\perp u.
}
$$

Análogamente,

$$
\boxed{
u\times v\perp v.
}
$$

Así, el vector definido por D29 es perpendicular a los dos factores sin que hayamos impuesto esta condición por separado: surge automáticamente de la alternancia del determinante.
También,

$$
\operatorname{Vol}^{\mathrm{or}}(u,u,w)=0
$$

para todo $w$, luego P32 implica

$$
\boxed{
u\times u=0.
}
$$

### 9.6. Qué ocurre si invertimos la orientación

Supongamos que conservamos el mismo producto escalar pero declaramos positiva la orientación opuesta.
Entonces el volumen orientado cambia de signo:

$$
\operatorname{Vol}^{\mathrm{or}}_{\mathrm{opp}}(u,v,w)
=
-
\operatorname{Vol}^{\mathrm{or}}(u,v,w).
$$

Sea $\times_{\mathrm{opp}}$ el producto vectorial definido con esa orientación opuesta. Por D29,

$$
\langle u\times_{\mathrm{opp}}v,w\rangle
=
-
\operatorname{Vol}^{\mathrm{or}}(u,v,w).
$$

Pero

$$
\left\langle
-(u\times v),w
\right\rangle
=
-
\operatorname{Vol}^{\mathrm{or}}(u,v,w).
$$

Por unicidad en P32,

$$
\boxed{
u\times_{\mathrm{opp}}v
=
-(u\times v).
}
$$

La orientación no es, por tanto, una decoración terminológica: determina el **signo** del producto vectorial.

### 9.7. Principio metodológico y consecuencias pendientes

> **FPM-I-04-MP14 — Declarar métrica y orientación antes de usar el producto vectorial**
> El producto vectorial tridimensional requiere simultáneamente:
>
> - un producto escalar, para identificar el funcional de volumen con un vector;
> - una orientación, para fijar el signo del volumen orientado.
>
> No tratar $u\times v$ como una operación disponible en un espacio vectorial real arbitrario.

La definición intrínseca

$$
\boxed{
\langle u\times v,w\rangle
=
\operatorname{Vol}^{\mathrm{or}}(u,v,w)
}
$$

contiene ya la geometría esencial de la operación.
Todavía falta traducir esta caracterización a una base ortonormal positiva y obtener:

- la fórmula usual por componentes;
- antisimetría y bilinealidad;
- el criterio $u\times v=0$;
- la magnitud
  $$
  \|u\times v\|
  $$
  en términos del ángulo entre $u$ y $v$.

### 9.8. Proposición: fórmula en una base ortonormal positiva

> **FPM-I-04-P33 — Fórmula coordenada del producto vectorial**
> Sea
>
> $$
> E=(e_1,e_2,e_3)
> $$
>
> una base ortonormal positivamente orientada. Si
>
> $$
> u=u^1e_1+u^2e_2+u^3e_3
> $$
>
> y
>
> $$
> v=v^1e_1+v^2e_2+v^3e_3,
> $$
>
> entonces
>
> $$
> \boxed{
> \begin{aligned}
> u\times v
> &=
> (u^2v^3-u^3v^2)e_1\\
> &\quad+
> (u^3v^1-u^1v^3)e_2\\
> &\quad+
> (u^1v^2-u^2v^1)e_3.
> \end{aligned}
> }
> $$

**Demostración.** Como $E$ es ortonormal, P20 permite recuperar las componentes de $u\times v$ mediante productos escalares:

$$
(u\times v)^k
=
\langle u\times v,e_k\rangle.
$$

Por D29,

$$
(u\times v)^k
=
\operatorname{Vol}^{\mathrm{or}}(u,v,e_k)
=
\det_E(u,v,e_k).
$$

Para $k=1$,

$$
\det
\begin{pmatrix}
u^1&v^1&1\\
u^2&v^2&0\\
u^3&v^3&0
\end{pmatrix}
=
u^2v^3-u^3v^2.
$$

Para $k=2$,

$$
\det
\begin{pmatrix}
u^1&v^1&0\\
u^2&v^2&1\\
u^3&v^3&0
\end{pmatrix}
=
u^3v^1-u^1v^3.
$$

Y para $k=3$,

$$
\det
\begin{pmatrix}
u^1&v^1&0\\
u^2&v^2&0\\
u^3&v^3&1
\end{pmatrix}
=
u^1v^2-u^2v^1.
$$

Reuniendo las tres componentes obtenemos la fórmula. $\square$
La expresión usual por componentes no es, por tanto, el punto de partida conceptual: es la representación de D29 en una base ortonormal positiva.[^shankar-arfken-cross]

### 9.9. Tabla de la base ortonormal positiva

Aplicando P33 a los vectores de la propia base,

$$
\boxed{
e_1\times e_2=e_3,
}
$$

$$
\boxed{
e_2\times e_3=e_1,
}
$$

$$
\boxed{
e_3\times e_1=e_2.
}
$$

Al invertir el orden,

$$
e_2\times e_1=-e_3,
$$

$$
e_3\times e_2=-e_1,
$$

$$
e_1\times e_3=-e_2.
$$

Esta tabla incorpora simultáneamente ortonormalidad y orientación. En una base ortonormal de orientación opuesta, los signos se invierten.

### 9.10. Proposición: bilinealidad y antisimetría

> **FPM-I-04-P34 — Bilinealidad y antisimetría del producto vectorial**
> Para $u,v,w\in V$ y $\alpha,\beta\in\mathbb R$:
>
> $$
> \boxed{
> (\alpha u+\beta v)\times w
> =
> \alpha(u\times w)
> +
> \beta(v\times w),
> }
> $$
>
> $$
> \boxed{
> u\times(\alpha v+\beta w)
> =
> \alpha(u\times v)
> +
> \beta(u\times w),
> }
> $$
>
> y
>
> $$
> \boxed{
> v\times u
> =
> -(u\times v).
> }
> $$

**Demostración de la linealidad en la primera entrada.** Para todo $z\in V$,

$$
\begin{aligned}
\left\langle
(\alpha u+\beta v)\times w,z
\right\rangle
&=
\operatorname{Vol}^{\mathrm{or}}(\alpha u+\beta v,w,z)\\
&=
\alpha\operatorname{Vol}^{\mathrm{or}}(u,w,z)
+
\beta\operatorname{Vol}^{\mathrm{or}}(v,w,z)\\
&=
\left\langle
\alpha(u\times w)+\beta(v\times w),
z
\right\rangle.
\end{aligned}
$$

Como esto vale para todo $z$, la unicidad de P32 implica la primera identidad.
La linealidad en la segunda entrada se demuestra del mismo modo usando la trilinealidad del volumen orientado.
Para la antisimetría,

$$
\begin{aligned}
\langle v\times u,z\rangle
&=
\operatorname{Vol}^{\mathrm{or}}(v,u,z)\\
&=
-\operatorname{Vol}^{\mathrm{or}}(u,v,z)\\
&=
\langle -(u\times v),z\rangle.
\end{aligned}
$$

Otra vez P32 da

$$
v\times u=-(u\times v).
$$

$\square$

La antisimetría contiene como caso particular

$$
u\times u=0,
$$

que ya habíamos obtenido directamente en §9.5.

### 9.11. Consecuencias algebraicas inmediatas

De P34 se sigue

$$
u\times0=0,
$$

$$
0\times v=0,
$$

y, para todo $\lambda\in\mathbb R$,

$$
(\lambda u)\times v
=
\lambda(u\times v)
=
u\times(\lambda v).
$$

Además,

$$
(u+v)\times w
=
u\times w+v\times w,
$$

y

$$
u\times(v+w)
=
u\times v+u\times w.
$$

Estas identidades son algebraicas; no requieren elegir coordenadas una vez que D29 está establecido.

### 9.12. Proposición: cuándo se anula el producto vectorial

> **FPM-I-04-P35 — Criterio de dependencia mediante el producto vectorial**
> Para $u,v\in V$,
>
> $$
> \boxed{
> u\times v=0
> \Longleftrightarrow
> u,v
> \text{ son linealmente dependientes}.
> }
> $$

**Demostración.**
Si $u$ y $v$ son dependientes, entonces existe una relación lineal entre ellos. En particular, si $v=\lambda u$,

$$
u\times v
=
u\times(\lambda u)
=
\lambda(u\times u)
=
0.
$$

Los casos en que uno de los vectores es cero quedan incluidos.
Recíprocamente, supongamos

$$
u\times v=0.
$$

Elegimos una base ortonormal positivamente orientada

$$
E=(e_1,e_2,e_3).
$$

Por P33, las tres componentes de $u\times v$ se anulan, de modo que

$$
u^2v^3-u^3v^2=0,
$$

$$
u^3v^1-u^1v^3=0,
$$

y

$$
u^1v^2-u^2v^1=0.
$$

Si $u=0$, la dependencia es inmediata. Supongamos entonces $u\ne0$. Alguna componente de $u$ es no nula. Si, por ejemplo,

$$
u^1\ne0,
$$

las dos últimas ecuaciones dan

$$
v^2=\frac{u^2}{u^1}v^1,
\qquad
v^3=\frac{u^3}{u^1}v^1.
$$

Por tanto,

$$
[v]_E
=
\frac{v^1}{u^1}[u]_E,
$$

y, por la biyección de componentes de P07,

$$
v=\frac{v^1}{u^1}u.
$$

Así $u$ y $v$ son linealmente dependientes. Si la componente no nula de $u$ es $u^2$ o $u^3$, el mismo argumento se obtiene permutando cíclicamente los índices. $\square$
Así, el producto vectorial detecta exactamente cuándo dos vectores generan un plano genuino.

### 9.13. Advertencia: la fórmula coordenada tiene hipótesis

> **FPM-I-04-MP15 — No transportar la fórmula de componentes fuera de una base ortonormal positiva**
> La expresión
>
> $$
> \begin{pmatrix}
> u^2v^3-u^3v^2\\
> u^3v^1-u^1v^3\\
> u^1v^2-u^2v^1
> \end{pmatrix}
> $$
>
> representa las componentes de $u\times v$ sólo cuando las componentes de $u$ y $v$ están tomadas en una base ortonormal compatible con la orientación positiva elegida.
>
> En una base general, esa receta numérica no puede trasladarse sin incorporar correctamente la métrica y la orientación.

Este punto es paralelo a la advertencia de §5 sobre la fórmula pitagórica por componentes: una expresión simple suele esconder hipótesis geométricas fuertes.

### 9.14. Balance: forma intrínseca y forma coordenada

Ya tenemos dos descripciones complementarias:
**Descripción intrínseca**

$$
\boxed{
\langle u\times v,w\rangle
=
\operatorname{Vol}^{\mathrm{or}}(u,v,w),
}
$$

y **descripción coordenada en una base ortonormal positiva**

$$
\boxed{
[u\times v]_E
=
\begin{pmatrix}
u^2v^3-u^3v^2\\
u^3v^1-u^1v^3\\
u^1v^2-u^2v^1
\end{pmatrix}.
}
$$

Además,

$$
\boxed{
v\times u=-(u\times v)
}
$$

y

$$
\boxed{
u\times v=0
\Longleftrightarrow
u,v
\text{ dependientes}.
}
$$

Todavía falta conectar la **magnitud** de $u\times v$ con el área del paralelogramo y con el ángulo entre $u$ y $v$.

### 9.15. Proposición: identidad de Lagrange

> **FPM-I-04-P36 — Identidad de Lagrange**
> Para todo $u,v\in V$,
>
> $$
> \boxed{
> \|u\times v\|^2
> =
> \|u\|^2\|v\|^2
> -
> \langle u,v\rangle^2.
> }
> $$

**Demostración.** Elegimos una base ortonormal positivamente orientada

$$
E=(e_1,e_2,e_3),
$$

y escribimos

$$
[u]_E=
\begin{pmatrix}
u^1\\
u^2\\
u^3
\end{pmatrix},
\qquad
[v]_E=
\begin{pmatrix}
v^1\\
v^2\\
v^3
\end{pmatrix}.
$$

Por P33,

$$
[u\times v]_E
=
\begin{pmatrix}
u^2v^3-u^3v^2\\
u^3v^1-u^1v^3\\
u^1v^2-u^2v^1
\end{pmatrix}.
$$

Como $E$ es ortonormal,

$$
\begin{aligned}
\|u\times v\|^2
&=
(u^2v^3-u^3v^2)^2\\
&\quad+
(u^3v^1-u^1v^3)^2\\
&\quad+
(u^1v^2-u^2v^1)^2.
\end{aligned}
$$

Al expandir y reagrupar,

$$
\begin{aligned}
\|u\times v\|^2
&=
\bigl((u^1)^2+(u^2)^2+(u^3)^2\bigr)
\bigl((v^1)^2+(v^2)^2+(v^3)^2\bigr)\\
&\quad-
\bigl(u^1v^1+u^2v^2+u^3v^3\bigr)^2.
\end{aligned}
$$

Por P20, los dos factores son $\|u\|^2$ y $\|v\|^2$, mientras el último paréntesis es $\langle u,v\rangle$. Por tanto,

$$
\|u\times v\|^2
=
\|u\|^2\|v\|^2
-
\langle u,v\rangle^2.
$$

$\square$

La identidad es intrínseca aunque se haya demostrado en una base ortonormal positiva: ambos lados están definidos geométricamente y no dependen de la base elegida.

### 9.16. Proposición: magnitud y ángulo

> **FPM-I-04-P37 — Magnitud del producto vectorial**
> Sean $u,v\ne0$ y sea
>
> $$
> \theta=\theta(u,v)\in[0,\pi].
> $$
>
> Entonces
>
> $$
> \boxed{
> \|u\times v\|
> =
> \|u\|\,\|v\|\sin\theta.
> }
> $$

**Demostración.** Por D21,

$$
\langle u,v\rangle
=
\|u\|\,\|v\|\cos\theta.
$$

Sustituyendo en P36,

$$
\begin{aligned}
\|u\times v\|^2
&=
\|u\|^2\|v\|^2
-
\|u\|^2\|v\|^2\cos^2\theta\\
&=
\|u\|^2\|v\|^2
\bigl(1-\cos^2\theta\bigr)\\
&=
\|u\|^2\|v\|^2\sin^2\theta.
\end{aligned}
$$

Como $\theta\in[0,\pi]$,

$$
\sin\theta\ge0.
$$

Tomando raíces no negativas,

$$
\|u\times v\|
=
\|u\|\,\|v\|\sin\theta.
$$

$\square$

Los casos extremos son coherentes con P35:

- si $\theta=0$ o $\pi$, entonces $\sin\theta=0$ y $u\times v=0$;
- si $\theta=\pi/2$, entonces
  $$
  \|u\times v\|
  =
  \|u\|\,\|v\|.
  $$

### 9.17. Interpretación como área

El paralelogramo generado por $u$ y $v$ tiene base de longitud $\|u\|$ y altura perpendicular

$$
\|v\|\sin\theta.
$$

Por tanto su área euclídea es

$$
\|u\|\,\|v\|\sin\theta.
$$

P37 permite escribir

$$
\boxed{
\operatorname{Area}(u,v)
=
\|u\times v\|.
}
$$

Así, el producto vectorial reúne dos informaciones diferentes:

- su **dirección** es perpendicular al plano generado por $u$ y $v$;
- su **magnitud** es el área del paralelogramo generado por ellos.

El signo orientacional no aparece en la norma. Está contenido en el sentido del vector normal.

### 9.18. Proposición: la normal elegida es positivamente orientada

> **FPM-I-04-P38 — Orientación de la terna $(u,v,u\times v)$**
> Si $u$ y $v$ son linealmente independientes, entonces
>
> $$
> \boxed{
> \operatorname{Vol}^{\mathrm{or}}
> (u,v,u\times v)
> =
> \|u\times v\|^2
> >0.
> }
> $$
>
> En particular,
>
> $$
> \boxed{
> (u,v,u\times v)
> }
> $$
>
> tiene orientación positiva.

**Demostración.** Por D29,

$$
\operatorname{Vol}^{\mathrm{or}}
(u,v,u\times v)
=
\langle u\times v,u\times v\rangle.
$$

Luego

$$
\operatorname{Vol}^{\mathrm{or}}
(u,v,u\times v)
=
\|u\times v\|^2.
$$

Como $u$ y $v$ son independientes, P35 da

$$
u\times v\ne0.
$$

Por positividad definida,

$$
\|u\times v\|^2>0.
$$

$\square$

Esta proposición expresa de manera intrínseca la regla de orientación que suele memorizarse mediante la “regla de la mano derecha”.

[]{#fispm-t1-c04-e0018}

### 9.19. Ejercicio FPM-I-04-E018 — Cálculo, perpendicularidad y área

> **Función pedagógica:** `Coordenadas → Verificación geométrica → Área`
>
> En una base ortonormal positivamente orientada
>
> $$
> E=(e_1,e_2,e_3),
> $$
>
> sean
>
> $$
> u=2e_1+e_2,
> \qquad
> v=e_1+3e_2+2e_3.
> $$
>
> 1. Calcula $u\times v$.
> 2. Comprueba que es perpendicular a $u$ y a $v$.
> 3. Calcula el área del paralelogramo generado por $u$ y $v$.
> 4. Verifica P36 directamente.

> **Solución desarrollada**
>
> Las columnas son
>
> $$
> [u]_E=
> \begin{pmatrix}
> 2\\
> 1\\
> 0
> \end{pmatrix},
> \qquad
> [v]_E=
> \begin{pmatrix}
> 1\\
> 3\\
> 2
> \end{pmatrix}.
> $$
>
> Por P33,
>
> $$
> [u\times v]_E
> =
> \begin{pmatrix}
> 2\\
> -4\\
> 5
> \end{pmatrix},
> $$
>
> es decir,
>
> $$
> \boxed{
> u\times v
> =
> 2e_1-4e_2+5e_3.
> }
> $$
>
> Verificamos:
>
> $$
> \langle u\times v,u\rangle
> =
> 2\cdot2+(-4)\cdot1+5\cdot0
> =
> 0,
> $$
>
> y
>
> $$
> \langle u\times v,v\rangle
> =
> 2\cdot1+(-4)\cdot3+5\cdot2
> =
> 0.
> $$
>
> Su norma al cuadrado es
>
> $$
> \|u\times v\|^2
> =
> 2^2+(-4)^2+5^2
> =
> 45.
> $$
>
> Por tanto,
>
> $$
> \boxed{
> \operatorname{Area}(u,v)
> =
> 3\sqrt5.
> }
> $$
>
> Finalmente,
>
> $$
> \|u\|^2=5,
> \qquad
> \|v\|^2=14,
> \qquad
> \langle u,v\rangle=5.
> $$
>
> Entonces
>
> $$
> \|u\|^2\|v\|^2
> -
> \langle u,v\rangle^2
> =
> 5\cdot14-25
> =
> 45,
> $$
>
> coincidiendo con $\|u\times v\|^2$.

[]{#fispm-t1-c04-e0019}

### 9.20. Ejercicio FPM-I-04-E019 — Dependencia de la orientación

> **Función pedagógica:** `Estructura → Orientación → Signo`
>
> Sea
>
> $$
> E=(e_1,e_2,e_3)
> $$
>
> una base ortonormal positiva y sean
>
> $$
> u=e_1+e_2,
> \qquad
> v=e_2+e_3.
> $$
>
> 1. Calcula $u\times v$ con la orientación positiva determinada por $E$.
> 2. Invierte la orientación del espacio sin cambiar el producto escalar. ¿Cuál es el nuevo producto vectorial?
> 3. Compara las normas y explica qué parte del resultado depende de la orientación.

> **Solución desarrollada**
>
> Por P33,
>
> $$
> [u]_E=
> \begin{pmatrix}
> 1\\
> 1\\
> 0
> \end{pmatrix},
> \qquad
> [v]_E=
> \begin{pmatrix}
> 0\\
> 1\\
> 1
> \end{pmatrix},
> $$
>
> y
>
> $$
> [u\times v]_E
> =
> \begin{pmatrix}
> 1\\
> -1\\
> 1
> \end{pmatrix}.
> $$
>
> Por tanto,
>
> $$
> \boxed{
> u\times v
> =
> e_1-e_2+e_3.
> }
> $$
>
> Si invertimos la orientación y mantenemos la misma métrica, §9.6 da
>
> $$
> \boxed{
> u\times_{\mathrm{opp}}v
> =
> -e_1+e_2-e_3.
> }
> $$
>
> En ambos casos,
>
> $$
> \|u\times v\|
> =
> \|u\times_{\mathrm{opp}}v\|
> =
> \sqrt3.
> $$
>
> La magnitud —y por tanto el área— depende de la métrica, pero no de cuál clase de orientación declaramos positiva. Lo que cambia con la orientación es el **sentido** de la normal.

### 9.21. Cierre de §9

El producto vectorial ha quedado construido a partir de dos estructuras previas:

$$
\boxed{
\text{producto escalar}
+
\text{orientación}
\Longrightarrow
\text{producto vectorial}.
}
$$

Su definición intrínseca es

$$
\boxed{
\langle u\times v,w\rangle
=
\operatorname{Vol}^{\mathrm{or}}(u,v,w),
}
$$

mientras que, en una base ortonormal positiva,

$$
\boxed{
[u\times v]_E
=
\begin{pmatrix}
u^2v^3-u^3v^2\\
u^3v^1-u^1v^3\\
u^1v^2-u^2v^1
\end{pmatrix}.
}
$$

Las propiedades fundamentales quedan resumidas por

$$
\boxed{
u\times v\perp u,
\qquad
u\times v\perp v,
}
$$

$$
\boxed{
v\times u=-(u\times v),
}
$$

$$
\boxed{
u\times v=0
\Longleftrightarrow
u,v
\text{ dependientes},
}
$$

y

$$
\boxed{
\|u\times v\|
=
\|u\|\,\|v\|\sin\theta.
}
$$

Finalmente,

$$
\boxed{
\operatorname{Vol}^{\mathrm{or}}
(u,v,u\times v)
=
\|u\times v\|^2>0
}
$$

cuando $u$ y $v$ son independientes. La orientación determina el sentido de la normal; la métrica determina su magnitud.
La siguiente sección cambiará de foco: no introducirá una nueva operación geométrica, sino que estudiará cómo una misma entidad vectorial adquiere distintas columnas cuando cambiamos de base.
El siguiente paso será:

$$
\boxed{
\text{§10 — Cambios de base y coordenadas vectoriales}
}
$$

[^shankar-arfken-cross]: Véanse R. Shankar, *Basic Training in Mathematics: A Fitness Program for Science Students*, Springer, 1995, cap. 7, §7.1 «Review of Vector Analysis», pp. 149–154; y G. B. Arfken, H. J. Weber y F. E. Harris, *Mathematical Methods for Physicists*, 7.ª ed., Academic Press, 2013, cap. 3, §3.2 «Vector in 3-D Spaces», pp. 126–132.

---

[]{#fispm-t1-c04-s10}

[]{#fpm-i-04-s10}

## §10 — Cambios de base y coordenadas vectoriales

### 10.1. Activación: el vector no cambia porque cambie su columna

Sea

$$
v\in V.
$$

Elegimos dos bases ordenadas:

$$
B=(e_1,e_2,e_3),
\qquad
B'=(e'_1,e'_2,e'_3).
$$

El mismo vector posee dos columnas:

$$
[v]_B
\qquad\text{y}\qquad
[v]_{B'}.
$$

Estas columnas pueden ser numéricamente distintas sin que haya ocurrido ninguna transformación física o geométrica del vector.
La situación es **pasiva**:

$$
\boxed{
v\ \text{permanece fijo};
\qquad
\text{cambia la base usada para describirlo}.
}
$$

El objetivo inicial de esta sección es determinar rigurosamente cómo se relacionan ambas columnas.

### 10.2. Definir: matriz de la nueva base expresada en la antigua

> **FPM-I-04-D30 — Matriz de cambio de base**
> Sean
>
> $$
> B=(e_1,e_2,e_3),
> \qquad
> B'=(e'_1,e'_2,e'_3).
> $$
>
> Definimos
>
> $$
> \boxed{
> S_{B\leftarrow B'}
> :=
> \begin{pmatrix}
> \vert&\vert&\vert\\
> [e'_1]_B&[e'_2]_B&[e'_3]_B\\
> \vert&\vert&\vert
> \end{pmatrix}.
> }
> $$
>
> Sus columnas son, por tanto, los vectores de la **base nueva** $B'$ expresados en la **base antigua** $B$.

Cuando no haya ambigüedad escribiremos simplemente

$$
S:=S_{B\leftarrow B'}.
$$

La flecha recuerda el sentido de reconstrucción:

$$
\boxed{
\text{columnas en }B'
\ \xrightarrow{\ S\ }\
\text{columnas en }B.
}
$$

### 10.3. Proposición: ley pasiva de transformación de coordenadas

> **FPM-I-04-P39 — Cambio de componentes entre dos bases**
> Para todo $v\in V$,
>
> $$
> \boxed{
> [v]_B
> =
> S_{B\leftarrow B'}[v]_{B'}.
> }
> $$
>
> Como $B'$ es una base, $S_{B\leftarrow B'}$ es invertible y, por tanto,
>
> $$
> \boxed{
> [v]_{B'}
> =
> S_{B\leftarrow B'}^{-1}[v]_B.
> }
> $$

**Demostración.** Escribimos

$$
[v]_{B'}
=
\begin{pmatrix}
v'^1\\
v'^2\\
v'^3
\end{pmatrix}.
$$

Por definición de componentes,

$$
v
=
v'^1e'_1+v'^2e'_2+v'^3e'_3.
$$

Tomando componentes respecto de $B$ y usando la linealidad de la aplicación de componentes P07,

$$
[v]_B
=
v'^1[e'_1]_B
+
v'^2[e'_2]_B
+
v'^3[e'_3]_B.
$$

Pero el lado derecho es precisamente el producto matricial

$$
S_{B\leftarrow B'}
\begin{pmatrix}
v'^1\\
v'^2\\
v'^3
\end{pmatrix}.
$$

Así,

$$
[v]_B
=
S_{B\leftarrow B'}[v]_{B'}.
$$

Las columnas de $S_{B\leftarrow B'}$ son las componentes en $B$ de los vectores de la base $B'$. Como $B'$ es linealmente independiente y P07 es biyectiva, esas columnas son linealmente independientes. Por P27,

$$
\det S_{B\leftarrow B'}\ne0.
$$

La matriz es, por tanto, invertible, y multiplicar la identidad anterior por su inversa produce

$$
[v]_{B'}
=
S_{B\leftarrow B'}^{-1}[v]_B.
$$

$\square$

La aparición de la inversa no es una convención arbitraria: procede del hecho de que las columnas de $S$ describen la base nueva en la antigua.[^arfken-coordinate-transformations]

### 10.4. Cambio pasivo frente a transformación activa

En un **cambio pasivo de base**:

- el vector geométrico $v$ es el mismo;
- cambia la base de descripción;
- la columna cambia según
  $$
  [v]_{B'}
  =
  S^{-1}[v]_B.
  $$

Una situación distinta es aplicar una transformación lineal

$$
T:V\longrightarrow V
$$

manteniendo fija la base $B$.
Entonces el vector generalmente cambia:

$$
v
\longmapsto
T(v).
$$

Si $A_B(T)$ es la matriz cuyas columnas son

$$
[T(e_1)]_B,
\qquad
[T(e_2)]_B,
\qquad
[T(e_3)]_B,
$$

la linealidad da

$$
\boxed{
[T(v)]_B
=
A_B(T)[v]_B.
}
$$

Aquí la matriz multiplica la columna porque estamos describiendo **otro vector en la misma base**.
Estas dos operaciones no deben confundirse:

$$
\boxed{
\begin{array}{c}
\text{pasivo: }v\text{ fijo},\ B\to B',
\\
[v]_{B'}=S^{-1}[v]_B,
\end{array}
}
$$

mientras

$$
\boxed{
\begin{array}{c}
\text{activo: }B\text{ fija},\ v\to T(v),
\\
[T(v)]_B=A_B(T)[v]_B.
\end{array}
}
$$

### 10.5. La misma matriz puede aparecer en dos problemas diferentes

Supongamos que definimos una transformación lineal $T_S$ mediante

$$
T_S(e_j)=e'_j.
$$

Por D30, la matriz de esta transformación activa en la base $B$ es precisamente

$$
A_B(T_S)=S_{B\leftarrow B'}.
$$

Por tanto,

$$
[T_S(v)]_B
=
S[v]_B.
$$

Pero el cambio **pasivo** desde $B$ hacia $B'$ obedece

$$
[v]_{B'}
=
S^{-1}[v]_B.
$$

De modo que la misma matriz geométrica de columnas puede aparecer en dos expresiones opuestas:

$$
\boxed{
\text{activo: }S,
\qquad
\text{pasivo: }S^{-1}.
}
$$

La diferencia no es algebraica sino conceptual: en un caso cambia el vector; en el otro cambia su descripción.

### 10.6. Ejemplo diagnóstico

Sea

$$
B=(e_1,e_2,e_3)
$$

y definamos

$$
B'
=
(e_1+e_2,\ e_2,\ e_3).
$$

Entonces

$$
S_{B\leftarrow B'}
=
\begin{pmatrix}
1&0&0\\
1&1&0\\
0&0&1
\end{pmatrix},
$$

y

$$
S_{B\leftarrow B'}^{-1}
=
\begin{pmatrix}
1&0&0\\
-1&1&0\\
0&0&1
\end{pmatrix}.
$$

Consideremos el vector

$$
v=2e_1+3e_2+e_3.
$$

En la base $B$,

$$
[v]_B
=
\begin{pmatrix}
2\\
3\\
1
\end{pmatrix}.
$$

#### Lectura pasiva

El vector no cambia. Sólo buscamos su columna en $B'$:

$$
[v]_{B'}
=
S^{-1}[v]_B
=
\begin{pmatrix}
1&0&0\\
-1&1&0\\
0&0&1
\end{pmatrix}
\begin{pmatrix}
2\\
3\\
1
\end{pmatrix}
=
\begin{pmatrix}
2\\
1\\
1
\end{pmatrix}.
$$

En efecto,

$$
2(e_1+e_2)+e_2+e_3
=
2e_1+3e_2+e_3
=
v.
$$

#### Lectura activa

Definamos ahora $T_S$ por

$$
T_S(e_1)=e_1+e_2,
\qquad
T_S(e_2)=e_2,
\qquad
T_S(e_3)=e_3.
$$

La base $B$ permanece fija, pero el vector cambia:

$$
[T_S(v)]_B
=
S[v]_B
=
\begin{pmatrix}
1&0&0\\
1&1&0\\
0&0&1
\end{pmatrix}
\begin{pmatrix}
2\\
3\\
1
\end{pmatrix}
=
\begin{pmatrix}
2\\
5\\
1
\end{pmatrix}.
$$

Así,

$$
T_S(v)
=
2e_1+5e_2+e_3,
$$

que no es el vector original.
Este ejemplo hace visible la diferencia:

$$
\boxed{
\begin{aligned}
\text{pasivo:}&\quad
v\text{ igual},\quad
(2,3,1)\to(2,1,1),
\\
\text{activo:}&\quad
v\text{ cambia},\quad
(2,3,1)\to(2,5,1).
\end{aligned}
}
$$

### 10.7. Principio metodológico y convención de cambio

> **FPM-I-04-MP16 — Preguntar qué está cambiando antes de multiplicar por una matriz**
> Antes de escribir una fórmula matricial, distinguir explícitamente:
>
> 1. **cambio pasivo de base:** el vector permanece fijo y cambia su columna;
> 2. **transformación activa:** la base permanece fija y cambia el vector.
>
> Una misma matriz puede intervenir en ambos problemas, pero las leyes de transformación no son la misma afirmación.

Queda fijada la convención canónica:

$$
\boxed{
S_{B\leftarrow B'}
=
\begin{pmatrix}
\vert&\vert&\vert\\
[e'_1]_B&[e'_2]_B&[e'_3]_B\\
\vert&\vert&\vert
\end{pmatrix},
}
$$

$$
\boxed{
[v]_B=S_{B\leftarrow B'}[v]_{B'},
}
$$

y

$$
\boxed{
[v]_{B'}
=
S_{B\leftarrow B'}^{-1}[v]_B.
}
$$

Todavía falta estudiar la composición de varios cambios de base, la matriz inversa como cambio en sentido opuesto y la transformación de objetos matriciales asociados.

### 10.8. La matriz identidad como cambio trivial

Si usamos la misma base como origen y destino,

$$
B=(e_1,e_2,e_3),
$$

entonces D30 produce

$$
S_{B\leftarrow B}
=
\begin{pmatrix}
\vert&\vert&\vert\\
[e_1]_B&[e_2]_B&[e_3]_B\\
\vert&\vert&\vert
\end{pmatrix}.
$$

Pero

$$
[e_1]_B=
\begin{pmatrix}
1\\
0\\
0
\end{pmatrix},
\qquad
[e_2]_B=
\begin{pmatrix}
0\\
1\\
0
\end{pmatrix},
\qquad
[e_3]_B=
\begin{pmatrix}
0\\
0\\
1
\end{pmatrix}.
$$

Por tanto,

$$
\boxed{
S_{B\leftarrow B}=I_3.
}
$$

Un cambio de descripción que no cambia la base debe dejar las columnas intactas.

### 10.9. Proposición: el cambio inverso

> **FPM-I-04-P40 — La matriz inversa cambia de vuelta a la base original**
> Para dos bases ordenadas $B$ y $B'$,
>
> $$
> \boxed{
> S_{B'\leftarrow B}
> =
> S_{B\leftarrow B'}^{-1}.
> }
> $$

**Demostración.** P39 aplicado al cambio de $B'$ hacia $B$ da, para todo $v\in V$,

$$
[v]_B
=
S_{B\leftarrow B'}[v]_{B'}.
$$

Aplicado en sentido contrario,

$$
[v]_{B'}
=
S_{B'\leftarrow B}[v]_B.
$$

Sustituyendo la primera identidad en la segunda,

$$
[v]_{B'}
=
S_{B'\leftarrow B}
S_{B\leftarrow B'}
[v]_{B'}.
$$

Esto vale para toda columna de componentes en $B'$. Como P07 establece una biyección entre $V$ y $\mathbb R^3$, las columnas $[v]_{B'}$ recorren todo $\mathbb R^3$. Luego

$$
S_{B'\leftarrow B}
S_{B\leftarrow B'}
=
I_3.
$$

Por unicidad de la inversa,

$$
S_{B'\leftarrow B}
=
S_{B\leftarrow B'}^{-1}.
$$

$\square$

La notación con flechas se comporta como esperamos:

$$
\boxed{
B'
\longrightarrow B
\quad\text{se deshace con}\quad
B\longrightarrow B'.
}
$$

### 10.10. Proposición: composición de cambios de base

> **FPM-I-04-P41 — Regla de composición**
> Sean $B$, $B'$ y $C$ tres bases ordenadas. Entonces
>
> $$
> \boxed{
> S_{B\leftarrow C}
> =
> S_{B\leftarrow B'}
> S_{B'\leftarrow C}.
> }
> $$

**Demostración.** Para todo $v\in V$, P39 da

$$
[v]_{B'}
=
S_{B'\leftarrow C}[v]_C.
$$

Luego,

$$
\begin{aligned}
[v]_B
&=
S_{B\leftarrow B'}[v]_{B'}\\
&=
S_{B\leftarrow B'}
S_{B'\leftarrow C}[v]_C.
\end{aligned}
$$

Pero también, por definición del cambio directo de $C$ a $B$,

$$
[v]_B
=
S_{B\leftarrow C}[v]_C.
$$

Como las columnas $[v]_C$ recorren todo $\mathbb R^3$,

$$
S_{B\leftarrow C}
=
S_{B\leftarrow B'}
S_{B'\leftarrow C}.
$$

$\square$

El orden de la multiplicación sigue el orden de las flechas:

$$
C
\longrightarrow
B'
\longrightarrow
B.
$$

Primero actúa

$$
S_{B'\leftarrow C},
$$

y después

$$
S_{B\leftarrow B'}.
$$

### 10.11. Consistencia de caminos

Supongamos que queremos convertir una columna desde $C$ hasta $B$.
Podemos hacerlo directamente:

$$
[v]_B
=
S_{B\leftarrow C}[v]_C.
$$

O podemos pasar por una base intermedia $B'$:

$$
[v]_B
=
S_{B\leftarrow B'}
S_{B'\leftarrow C}
[v]_C.
$$

P41 garantiza que ambos caminos producen exactamente la misma columna.
Por eso un diagrama de cambios de base debe ser **conmutativo**:

$$
\boxed{
\text{el resultado no depende del camino de bases intermedias}.
}
$$

Este criterio es una herramienta práctica de control: si dos rutas producen matrices distintas, alguna convención de flechas o algún orden de multiplicación fue usado incorrectamente.

### 10.12. Ejemplo con tres bases

Sea

$$
B=(e_1,e_2,e_3).
$$

Definimos

$$
B'
=
(e_1+e_2,\ e_2,\ e_3),
$$

de modo que

$$
S_{B\leftarrow B'}
=
\begin{pmatrix}
1&0&0\\
1&1&0\\
0&0&1
\end{pmatrix}.
$$

Ahora definimos

$$
C
=
(e'_1,\ e'_2+e'_3,\ e'_3).
$$

Respecto de $B'$,

$$
S_{B'\leftarrow C}
=
\begin{pmatrix}
1&0&0\\
0&1&0\\
0&1&1
\end{pmatrix}.
$$

Por P41,

$$
S_{B\leftarrow C}
=
S_{B\leftarrow B'}
S_{B'\leftarrow C}.
$$

Multiplicando,

$$
S_{B\leftarrow C}
=
\begin{pmatrix}
1&0&0\\
1&1&0\\
0&0&1
\end{pmatrix}
\begin{pmatrix}
1&0&0\\
0&1&0\\
0&1&1
\end{pmatrix}
=
\begin{pmatrix}
1&0&0\\
1&1&0\\
0&1&1
\end{pmatrix}.
$$

Podemos verificarlo directamente desde los vectores de $C$:

$$
c_1=e_1+e_2,
$$

$$
c_2=e_2+e_3,
$$

$$
c_3=e_3.
$$

Sus columnas en $B$ son precisamente

$$
\begin{pmatrix}
1\\
1\\
0
\end{pmatrix},
\qquad
\begin{pmatrix}
0\\
1\\
1
\end{pmatrix},
\qquad
\begin{pmatrix}
0\\
0\\
1
\end{pmatrix},
$$

que forman la matriz obtenida por composición.

### 10.13. Proposición: compatibilidad con determinantes y orientación

> **FPM-I-04-P42 — Determinante de un cambio compuesto**
> Para tres bases $B$, $B'$ y $C$,
>
> $$
> \boxed{
> \det S_{B\leftarrow C}
> =
> \det S_{B\leftarrow B'}
> \det S_{B'\leftarrow C}.
> }
> $$

**Demostración.** Es una consecuencia inmediata de P41 y P26:

$$
\begin{aligned}
\det S_{B\leftarrow C}
&=
\det\left(
S_{B\leftarrow B'}
S_{B'\leftarrow C}
\right)\\
&=
\det S_{B\leftarrow B'}
\det S_{B'\leftarrow C}.
\end{aligned}
$$

$\square$

Por tanto, los signos también se componen:

- dos cambios que invierten orientación producen un cambio que la conserva;
- un único cambio de signo negativo invierte orientación;
- cambios de signo positivo conservan la clase de orientación.

Esto conecta la convención matricial de §10 con las clases de orientación construidas en §8.

### 10.14. Principio metodológico de consistencia

> **FPM-I-04-MP17 — Leer las flechas antes de multiplicar matrices de cambio**
> Para una matriz
>
> $$
> S_{A\leftarrow B},
> $$
>
> interpretar siempre:
>
> $$
> \text{componentes en }B
> \longrightarrow
> \text{componentes en }A.
> $$
>
> Dos matrices pueden multiplicarse directamente sólo cuando las flechas intermedias encajan:
>
> $$
> S_{A\leftarrow B}
> S_{B\leftarrow C}
> =
> S_{A\leftarrow C}.
> $$

La regla funciona como un control de tipos:

$$
C
\to
B
\to
A.
$$

Si las etiquetas no encajan, el producto no representa la composición pretendida aunque la multiplicación matricial sea algebraicamente posible.

### 10.15. Balance: inversión, composición y consistencia

Ya disponemos de una red coherente de cambios pasivos:

$$
\boxed{
S_{B\leftarrow B}=I,
}
$$

$$
\boxed{
S_{B'\leftarrow B}
=
S_{B\leftarrow B'}^{-1},
}
$$

y

$$
\boxed{
S_{B\leftarrow C}
=
S_{B\leftarrow B'}
S_{B'\leftarrow C}.
}
$$

Estas identidades aseguran que la descripción de un vector puede convertirse entre bases sin ambigüedad y sin transformar el vector geométrico.
Todavía falta estudiar cómo cambia la **matriz de una transformación lineal** cuando cambiamos la base usada para describirla.

### 10.16. Definir: matriz de una transformación lineal en una base

> **FPM-I-04-D31 — Matriz de una transformación lineal**
> Sea
>
> $$
> T:V\longrightarrow V
> $$
>
> lineal y sea
>
> $$
> B=(e_1,e_2,e_3)
> $$
>
> una base ordenada. Definimos
>
> $$
> \boxed{
> A_B(T)
> :=
> \begin{pmatrix}
> \vert&\vert&\vert\\
> [T(e_1)]_B&[T(e_2)]_B&[T(e_3)]_B\\
> \vert&\vert&\vert
> \end{pmatrix}.
> }
> $$
>
> Entonces, para todo $v\in V$,
>
> $$
> \boxed{
> [T(v)]_B
> =
> A_B(T)[v]_B.
> }
> $$

La matriz depende de la base. La transformación lineal $T$ no.
Por eso no es correcto identificar sin más

$$
T
\quad\text{con}\quad
A_B(T).
$$

La matriz es una representación de $T$ una vez elegida una base.

### 10.17. Proposición: ley de conjugación

> **FPM-I-04-P43 — Cambio de base de la matriz de un operador**
> Sean $B$ y $B'$ dos bases y sea
>
> $$
> S:=S_{B\leftarrow B'}.
> $$
>
> Entonces
>
> $$
> \boxed{
> A_{B'}(T)
> =
> S^{-1}A_B(T)S.
> }
> $$

**Demostración.** Para todo $v\in V$,

$$
[v]_B
=
S[v]_{B'}.
$$

Aplicamos $T$ y escribimos el resultado en la base $B$:

$$
[T(v)]_B
=
A_B(T)[v]_B
=
A_B(T)S[v]_{B'}.
$$

Ahora convertimos la columna resultante desde $B$ hacia $B'$:

$$
[T(v)]_{B'}
=
S^{-1}[T(v)]_B.
$$

Por tanto,

$$
[T(v)]_{B'}
=
S^{-1}A_B(T)S[v]_{B'}.
$$

Pero, por D31,

$$
[T(v)]_{B'}
=
A_{B'}(T)[v]_{B'}.
$$

Como las columnas $[v]_{B'}$ recorren todo $\mathbb R^3$,

$$
A_{B'}(T)
=
S^{-1}A_B(T)S.
$$

$\square$

El patrón de la fórmula refleja exactamente el recorrido conceptual:

$$
B'
\ \xrightarrow{\ S\ }\
B
\ \xrightarrow{\ A_B(T)\ }\
B
\ \xrightarrow{\ S^{-1}\ }\
B'.
$$

### 10.18. Misma transformación, matrices distintas

La igualdad

$$
A_{B'}(T)
=
S^{-1}A_B(T)S
$$

no describe tres transformaciones activas sucesivas aplicadas al vector físico.
Describe una sola transformación geométrica $T$ expresada en dos sistemas de coordenadas distintos.
Por eso las matrices

$$
A_B(T)
\qquad\text{y}\qquad
A_{B'}(T)
$$

pueden ser numéricamente diferentes y, sin embargo, representar exactamente el mismo operador.

> **FPM-I-04-MP18 — No confundir el operador con una de sus matrices**
> Al cambiar de base, mantener fijo el operador geométrico y transformar su representación por conjugación:
>
> $$
> A_{B'}(T)=S^{-1}A_B(T)S.
> $$
>
> Una diferencia entre matrices no implica una diferencia entre operadores.

### 10.19. Proposición: el determinante del operador no depende de la base

> **FPM-I-04-P44 — Invariancia del determinante bajo cambio de base**
> Para cualquier transformación lineal $T$ y cualesquiera bases $B,B'$,
>
> $$
> \boxed{
> \det A_{B'}(T)
> =
> \det A_B(T).
> }
> $$

**Demostración.** Por P43,

$$
A_{B'}(T)
=
S^{-1}A_B(T)S.
$$

Aplicando P26,

$$
\det A_{B'}(T)
=
\det(S^{-1})
\det A_B(T)
\det(S).
$$

Como

$$
SS^{-1}=I,
$$

P26 implica

$$
\det(S)\det(S^{-1})=1.
$$

Luego

$$
\det A_{B'}(T)
=
\det A_B(T).
$$

$\square$

Así, aunque la matriz cambie con la base, su determinante es una propiedad intrínseca del operador lineal.

### 10.20. Ejemplo: una matriz diagonal deja de ser diagonal

Sea

$$
B=(e_1,e_2,e_3),
$$

y definamos

$$
T(e_1)=2e_1,
\qquad
T(e_2)=3e_2,
\qquad
T(e_3)=4e_3.
$$

Entonces

$$
A_B(T)
=
\begin{pmatrix}
2&0&0\\
0&3&0\\
0&0&4
\end{pmatrix}.
$$

Tomemos la base

$$
B'
=
(e_1+e_2,\ e_2,\ e_3),
$$

para la cual

$$
S=
S_{B\leftarrow B'}
=
\begin{pmatrix}
1&0&0\\
1&1&0\\
0&0&1
\end{pmatrix},
$$

y

$$
S^{-1}
=
\begin{pmatrix}
1&0&0\\
-1&1&0\\
0&0&1
\end{pmatrix}.
$$

Por P43,

$$
A_{B'}(T)
=
S^{-1}A_B(T)S.
$$

Calculando,

$$
A_B(T)S
=
\begin{pmatrix}
2&0&0\\
3&3&0\\
0&0&4
\end{pmatrix},
$$

y por tanto

$$
\boxed{
A_{B'}(T)
=
\begin{pmatrix}
2&0&0\\
1&3&0\\
0&0&4
\end{pmatrix}.
}
$$

La matriz ya no es diagonal, aunque el operador $T$ sea exactamente el mismo.
Además,

$$
\det A_B(T)=24,
$$

y

$$
\det A_{B'}(T)=24,
$$

como predice P44.

[]{#fispm-t1-c04-e0020}

### 10.21. Ejercicio FPM-I-04-E020 — Cambio pasivo y transformación activa

> **Función pedagógica:** `Diagnóstico conceptual → Conversión de coordenadas → Activo/pasivo`
>
> Sea
>
> $$
> B=(e_1,e_2,e_3),
> $$
>
> y
>
> $$
> B'
> =
> (e_1+e_2,\ e_2,\ e_3).
> $$
>
> Para
>
> $$
> v=2e_1+3e_2+e_3,
> $$
>
> realiza dos operaciones distintas:
>
> 1. calcula $[v]_{B'}$ sin cambiar el vector;
> 2. define $T_S(e_j)=e'_j$ y calcula $[T_S(v)]_B$.
>
> Explica por qué aparecen $S^{-1}$ y $S$, respectivamente.

> **Solución desarrollada**
>
> Tenemos
>
> $$
> S=
> \begin{pmatrix}
> 1&0&0\\
> 1&1&0\\
> 0&0&1
> \end{pmatrix},
> \qquad
> S^{-1}
> =
> \begin{pmatrix}
> 1&0&0\\
> -1&1&0\\
> 0&0&1
> \end{pmatrix},
> $$
>
> y
>
> $$
> [v]_B
> =
> \begin{pmatrix}
> 2\\
> 3\\
> 1
> \end{pmatrix}.
> $$
>
> **Cambio pasivo:**
>
> $$
> [v]_{B'}
> =
> S^{-1}[v]_B
> =
> \begin{pmatrix}
> 2\\
> 1\\
> 1
> \end{pmatrix}.
> $$
>
> El vector sigue siendo
>
> $$
> v=2e_1+3e_2+e_3.
> $$
>
> **Transformación activa:**
>
> $$
> [T_S(v)]_B
> =
> S[v]_B
> =
> \begin{pmatrix}
> 2\\
> 5\\
> 1
> \end{pmatrix}.
> $$
>
> Ahora el vector sí cambió:
>
> $$
> T_S(v)=2e_1+5e_2+e_3.
> $$
>
> El uso de $S^{-1}$ o $S$ responde a preguntas distintas, no a una elección notacional.

[]{#fispm-t1-c04-e0021}

### 10.22. Ejercicio FPM-I-04-E021 — Una transformación, dos matrices

> **Función pedagógica:** `Conjugación → Verificación → Invariante`
>
> En la base
>
> $$
> B=(e_1,e_2,e_3),
> $$
>
> una transformación lineal $T$ tiene matriz
>
> $$
> A_B(T)
> =
> \begin{pmatrix}
> 2&0&0\\
> 0&3&0\\
> 0&0&4
> \end{pmatrix}.
> $$
>
> Sea
>
> $$
> B'
> =
> (e_1+e_2,\ e_2,\ e_3).
> $$
>
> 1. Calcula $S_{B\leftarrow B'}$ y su inversa.
> 2. Calcula $A_{B'}(T)$.
> 3. Verifica la acción sobre $e'_1$ directamente.
> 4. Compara los determinantes de ambas matrices.

> **Solución desarrollada**
>
> Como antes,
>
> $$
> S=
> \begin{pmatrix}
> 1&0&0\\
> 1&1&0\\
> 0&0&1
> \end{pmatrix},
> \qquad
> S^{-1}
> =
> \begin{pmatrix}
> 1&0&0\\
> -1&1&0\\
> 0&0&1
> \end{pmatrix}.
> $$
>
> Por P43,
>
> $$
> A_{B'}(T)
> =
> S^{-1}A_B(T)S
> =
> \boxed{
> \begin{pmatrix}
> 2&0&0\\
> 1&3&0\\
> 0&0&4
> \end{pmatrix}
> }.
> $$
>
> Para verificar la primera columna, observamos que
>
> $$
> e'_1=e_1+e_2,
> $$
>
> de modo que
>
> $$
> T(e'_1)
> =
> 2e_1+3e_2.
> $$
>
> Buscamos
>
> $$
> 2e_1+3e_2
> =
> \alpha(e_1+e_2)+\beta e_2.
> $$
>
> Comparando coeficientes,
>
> $$
> \alpha=2,
> \qquad
> \beta=1.
> $$
>
> Por tanto,
>
> $$
> [T(e'_1)]_{B'}
> =
> \begin{pmatrix}
> 2\\
> 1\\
> 0
> \end{pmatrix},
> $$
>
> que coincide con la primera columna de $A_{B'}(T)$.
>
> Finalmente,
>
> $$
> \det A_B(T)=24
> $$
>
> y
>
> $$
> \det A_{B'}(T)=24.
> $$
>
> El operador es el mismo; sólo cambia su representación matricial.

### 10.23. Cierre de §10

La sección ha distinguido tres objetos que suelen confundirse:

$$
\boxed{
\text{vector geométrico},
\qquad
\text{columna de coordenadas},
\qquad
\text{matriz de un operador}.
}
$$

Para un cambio pasivo de base,

$$
\boxed{
[v]_{B'}
=
S_{B\leftarrow B'}^{-1}[v]_B.
}
$$

Para una transformación activa en una base fija,

$$
\boxed{
[T(v)]_B
=
A_B(T)[v]_B.
}
$$

Y para el mismo operador expresado en dos bases,

$$
\boxed{
A_{B'}(T)
=
S_{B\leftarrow B'}^{-1}
A_B(T)
S_{B\leftarrow B'}.
}
$$

Las matrices de cambio satisfacen además

$$
\boxed{
S_{B'\leftarrow B}
=
S_{B\leftarrow B'}^{-1},
}
$$

y

$$
\boxed{
S_{B\leftarrow C}
=
S_{B\leftarrow B'}
S_{B'\leftarrow C}.
}
$$

La conclusión metodológica es simple:

$$
\boxed{
\text{antes de multiplicar matrices, declarar qué objeto cambia y en qué base se expresa}.
}
$$

La siguiente sección estudiará transformaciones lineales que preservan la geometría euclídea: rotaciones, reflexiones e isometrías.
El siguiente paso será:

$$
\boxed{
\text{§11 — Rotaciones, reflexiones e isometrías}
}
$$

[^arfken-coordinate-transformations]: G. B. Arfken, H. J. Weber y F. E. Harris, *Mathematical Methods for Physicists*, 7.ª ed., Academic Press, 2013, cap. 3, §3.3 «Coordinate Transformations», pp. 133–138.

---

[]{#fispm-t1-c04-s11}

[]{#fpm-i-04-s11}

## §11 — Rotaciones, reflexiones e isometrías

### 11.1. Activación: transformar sin deformar

Una transformación lineal general

$$
T:V\longrightarrow V
$$

puede cambiar longitudes, ángulos y volúmenes.
Pero hay transformaciones especiales que mueven los vectores sin deformar la geometría euclídea.
Queremos caracterizar las transformaciones lineales que conservan exactamente la norma:

$$
\|T(v)\|=\|v\|
$$

para todo $v\in V$.
Como $T$ es lineal,

$$
T(0)=0,
$$

así que estas transformaciones fijan el origen vectorial. Las traslaciones y, más en general, las isometrías afines que no fijan el origen se tratarán al estudiar cambios de marco.

### 11.2. Definir: isometría lineal

> **FPM-I-04-D32 — Isometría lineal**
> Una transformación lineal
>
> $$
> T:V\longrightarrow V
> $$
>
> es una **isometría lineal** si
>
> $$
> \boxed{
> \|T(v)\|=\|v\|
> }
> $$
>
> para todo $v\in V$.

La definición es intrínseca: no requiere elegir una base.
Además, para cualesquiera $P,Q$ en el espacio afín modelado sobre $V$, si aplicamos $T$ a sus desplazamientos,

$$
\|T(\overrightarrow{PQ})\|
=
\|\overrightarrow{PQ}\|.
$$

Por eso una isometría lineal conserva las longitudes de todos los vectores de desplazamiento.

### 11.3. Polarización: recuperar el producto escalar desde la norma

En un espacio euclídeo real,

$$
\|u+v\|^2
=
\langle u+v,u+v\rangle.
$$

Por bilinealidad y simetría,

$$
\|u+v\|^2
=
\|u\|^2
+
2\langle u,v\rangle
+
\|v\|^2.
$$

Despejando,

$$
\boxed{
\langle u,v\rangle
=
\frac12
\left(
\|u+v\|^2
-
\|u\|^2
-
\|v\|^2
\right).
}
$$

Esta identidad muestra que, en el caso real, la norma determina completamente el producto escalar.

### 11.4. Proposición: preservar norma equivale a preservar producto escalar

> **FPM-I-04-P45 — Caracterización intrínseca de las isometrías lineales**
> Sea
>
> $$
> T:V\longrightarrow V
> $$
>
> lineal. Son equivalentes:
>
> 1. $T$ preserva la norma:
>
> $$
> \|T(v)\|=\|v\|
> $$
>
> para todo $v$;
>
> 2. $T$ preserva el producto escalar:
>
> $$
> \boxed{
> \langle T(u),T(v)\rangle
> =
> \langle u,v\rangle
> }
> $$
>
> para todos $u,v\in V$.

**Demostración.**
Supongamos primero que $T$ preserva la norma. Como $T$ es lineal,

$$
T(u+v)=T(u)+T(v).
$$

Aplicamos la identidad de polarización:

$$
\begin{aligned}
\langle T(u),T(v)\rangle
&=
\frac12
\left(
\|T(u)+T(v)\|^2
-
\|T(u)\|^2
-
\|T(v)\|^2
\right)\\
&=
\frac12
\left(
\|T(u+v)\|^2
-
\|T(u)\|^2
-
\|T(v)\|^2
\right)\\
&=
\frac12
\left(
\|u+v\|^2
-
\|u\|^2
-
\|v\|^2
\right)\\
&=
\langle u,v\rangle.
\end{aligned}
$$

Recíprocamente, si $T$ preserva el producto escalar, entonces

$$
\|T(v)\|^2
=
\langle T(v),T(v)\rangle
=
\langle v,v\rangle
=
\|v\|^2.
$$

Como ambas normas son no negativas,

$$
\|T(v)\|=\|v\|.
$$

$\square$

Por tanto, una isometría lineal conserva simultáneamente longitudes y ángulos.

### 11.5. Consecuencias geométricas inmediatas

Si $T$ es una isometría lineal, P45 da

$$
\langle T(u),T(v)\rangle
=
\langle u,v\rangle.
$$

Por tanto:

#### Ortogonalidad

Si

$$
u\perp v,
$$

entonces

$$
\langle u,v\rangle=0,
$$

y así

$$
\langle T(u),T(v)\rangle=0.
$$

Luego

$$
\boxed{
u\perp v
\Longrightarrow
T(u)\perp T(v).
}
$$

#### Ángulos

Para $u,v\ne0$,

$$
\cos\theta(T(u),T(v))
=
\frac{\langle T(u),T(v)\rangle}
{\|T(u)\|\|T(v)\|}.
$$

Como producto escalar y normas se conservan,

$$
\boxed{
\theta(T(u),T(v))
=
\theta(u,v).
}
$$

#### Distancias entre vectores

Por linealidad,

$$
T(u)-T(v)
=
T(u-v).
$$

Entonces

$$
\|T(u)-T(v)\|
=
\|T(u-v)\|
=
\|u-v\|.
$$

Así una isometría lineal conserva también la distancia euclídea entre cualesquiera dos vectores considerados como puntos del espacio vectorial.

### 11.6. Matriz de una isometría en una base ortonormal

Sea

$$
E=(e_1,e_2,e_3)
$$

una base ortonormal y sea

$$
Q:=A_E(T).
$$

Las columnas de $Q$ son

$$
[T(e_1)]_E,
\qquad
[T(e_2)]_E,
\qquad
[T(e_3)]_E.
$$

Si $T$ es una isometría, P45 implica

$$
\langle T(e_i),T(e_j)\rangle
=
\langle e_i,e_j\rangle
=
\delta_{ij}.
$$

Por tanto, las columnas de $Q$ forman una base ortonormal.
En coordenadas respecto de $E$, esto equivale a que los productos escalares entre columnas produzcan la matriz identidad.

### 11.7. Proposición: caracterización matricial

> **FPM-I-04-P46 — Matriz ortogonal de una isometría**
> Sea $E$ una base ortonormal y
>
> $$
> Q=A_E(T).
> $$
>
> Entonces $T$ es una isometría lineal si y sólo si
>
> $$
> \boxed{
> Q^{\mathsf T}Q=I_3.
> }
> $$

**Demostración.**
Las entradas de

$$
Q^{\mathsf T}Q
$$

son los productos escalares entre las columnas de $Q$.
Como la columna $j$ es

$$
[T(e_j)]_E,
$$

tenemos

$$
(Q^{\mathsf T}Q)_{ij}
=
\langle T(e_i),T(e_j)\rangle.
$$

Si $T$ es isometría, P45 da

$$
\langle T(e_i),T(e_j)\rangle
=
\delta_{ij},
$$

por lo que

$$
Q^{\mathsf T}Q=I_3.
$$

Recíprocamente, supongamos

$$
Q^{\mathsf T}Q=I_3.
$$

Para cualesquiera $u,v\in V$, escribimos

$$
x=[u]_E,
\qquad
y=[v]_E.
$$

Como $E$ es ortonormal,

$$
\langle u,v\rangle
=
x^{\mathsf T}y.
$$

Además,

$$
[T(u)]_E=Qx,
\qquad
[T(v)]_E=Qy.
$$

Entonces

$$
\begin{aligned}
\langle T(u),T(v)\rangle
&=
(Qx)^{\mathsf T}(Qy)\\
&=
x^{\mathsf T}Q^{\mathsf T}Qy\\
&=
x^{\mathsf T}y\\
&=
\langle u,v\rangle.
\end{aligned}
$$

Por P45, $T$ es una isometría. $\square$
Una matriz que satisface

$$
Q^{\mathsf T}Q=I_3
$$

se denomina **matriz ortogonal**.

### 11.8. Consecuencias algebraicas de la ortogonalidad

De

$$
Q^{\mathsf T}Q=I_3
$$

se sigue que $Q^{\mathsf T}$ es una inversa por la izquierda.
Tomando determinantes,

$$
\det(Q^{\mathsf T}Q)
=
\det I_3
=
1.
$$

Por P26 y por

$$
\det(Q^{\mathsf T})=\det Q,
$$

obtenemos

$$
(\det Q)^2=1.
$$

Por tanto,

$$
\boxed{
\det Q=\pm1.
}
$$

En particular,

$$
\det Q\ne0,
$$

de modo que $Q$ es invertible.
Así,

$$
\boxed{
Q^{-1}=Q^{\mathsf T}.
}
$$

Toda isometría lineal es, por tanto, biyectiva.
El signo de $\det Q$ permitirá distinguir, más adelante en esta sección, las isometrías que conservan orientación de aquellas que la invierten.

### 11.9. No confundir matriz ortogonal con base ortonormal

Una **base ortonormal** es una terna ordenada de vectores

$$
(e_1,e_2,e_3)
$$

que satisface

$$
\langle e_i,e_j\rangle=\delta_{ij}.
$$

Una **matriz ortogonal** es una matriz cuadrada

$$
Q
$$

que satisface

$$
Q^{\mathsf T}Q=I.
$$

La relación es la siguiente:

> las columnas de una matriz ortogonal, interpretadas en una base ortonormal de referencia, forman otra base ortonormal.

Pero los dos objetos no son del mismo tipo.

### 11.10. Cambio pasivo frente a isometría activa

En §10 vimos que una matriz ortogonal también puede aparecer como matriz de cambio entre dos bases ortonormales.
Eso no convierte automáticamente el cambio de base en una transformación activa.
Si

$$
S_{E\leftarrow E'}
$$

relaciona dos bases ortonormales, entonces

$$
S^{\mathsf T}S=I.
$$

En el problema **pasivo**,

$$
[v]_{E'}
=
S^{-1}[v]_E
=
S^{\mathsf T}[v]_E,
$$

mientras el vector $v$ permanece fijo.
En un problema **activo**, una isometría $T$ con matriz

$$
Q=A_E(T)
$$

transforma el vector:

$$
[T(v)]_E
=
Q[v]_E.
$$

Aunque $S$ y $Q$ puedan ser numéricamente iguales, describen problemas conceptualmente distintos.

> **FPM-I-04-MP19 — Distinguir ortogonalidad matricial de la naturaleza del proceso**
> La condición
>
> $$
> M^{\mathsf T}M=I
> $$
>
> informa que una matriz preserva el producto escalar en coordenadas ortonormales. No indica por sí sola si la matriz se está usando:
>
> - como cambio pasivo entre bases ortonormales;
> - o como representación activa de una isometría lineal.
>
> Declarar siempre qué objeto permanece fijo y qué objeto se transforma.

### 11.11. Balance: de la ortogonalidad matricial a la orientación

Ya tenemos la caracterización esencial:

$$
\boxed{
T\text{ isometría lineal}
\Longleftrightarrow
\langle T(u),T(v)\rangle
=
\langle u,v\rangle
}
$$

y, en una base ortonormal,

$$
\boxed{
T\text{ isometría lineal}
\Longleftrightarrow
Q^{\mathsf T}Q=I.
}
$$

Además,

$$
\boxed{
Q^{-1}=Q^{\mathsf T},
\qquad
\det Q=\pm1.
}
$$

Todavía falta interpretar geométricamente las dos posibilidades del determinante:

- $\det Q=+1$: isometrías que conservan orientación;
- $\det Q=-1$: isometrías que invierten orientación.

### 11.12. Definir: isometrías propias e impropias

> **FPM-I-04-D33 — Isometría propia e impropia**
> Sea $T$ una isometría lineal y sea
>
> $$
> Q=A_E(T)
> $$
>
> su matriz en una base ortonormal $E$.
>
> Diremos que $T$ es **propia** si
>
> $$
> \boxed{
> \det Q=+1,
> }
> $$
>
> y **impropia** si
>
> $$
> \boxed{
> \det Q=-1.
> }
> $$

P44 garantiza que el determinante de la matriz de un operador no depende de la base. Por tanto, esta definición es intrínseca.

### 11.13. Proposición: el signo del determinante controla la orientación

> **FPM-I-04-P47 — Orientación bajo una isometría**
> Sea
>
> $$
> E=(e_1,e_2,e_3)
> $$
>
> una base ortonormal positivamente orientada y sea $T$ una isometría lineal con matriz $Q=A_E(T)$.
>
> Entonces:
>
> $$
> \boxed{
> \det Q=+1
> \Longleftrightarrow
> (T(e_1),T(e_2),T(e_3))
> \text{ tiene orientación positiva},
> }
> $$
>
> mientras
>
> $$
> \boxed{
> \det Q=-1
> \Longleftrightarrow
> (T(e_1),T(e_2),T(e_3))
> \text{ tiene orientación negativa}.
> }
> $$

**Demostración.** Las columnas de $Q$ son precisamente

$$
[T(e_1)]_E,
\qquad
[T(e_2)]_E,
\qquad
[T(e_3)]_E.
$$

Por D26, el signo de

$$
\det Q
$$

es exactamente la orientación relativa de la base imagen respecto de $E$. $\square$
Así, una isometría propia conserva orientación y una impropia la invierte.

### 11.14. Definir: reflexión ortogonal respecto de un plano

Sea $n$ un vector unitario:

$$
\|n\|=1.
$$

El plano vectorial perpendicular a $n$ es

$$
n^\perp
=
\{v\in V:\langle v,n\rangle=0\}.
$$

> **FPM-I-04-D34 — Reflexión ortogonal respecto del plano perpendicular a n**
> Definimos
>
> $$
> \boxed{
> H_n(v)
> :=
> v-2\langle v,n\rangle n.
> }
> $$

Por P16, todo vector se descompone de manera única como

$$
v=v_\perp+v_\parallel,
$$

donde

$$
v_\parallel=\langle v,n\rangle n
$$

y

$$
v_\perp\perp n.
$$

Entonces

$$
H_n(v)
=
v_\perp-v_\parallel.
$$

La reflexión conserva la componente contenida en el plano $n^\perp$ e invierte la componente normal.

### 11.15. Proposición: la reflexión es una isometría impropia

> **FPM-I-04-P48 — Propiedades de la reflexión ortogonal**
> Para todo vector unitario $n$, la aplicación $H_n$ satisface:
>
> 1. es lineal;
> 2. es una isometría;
> 3. fija todo vector de $n^\perp$;
> 4. envía
>    $$
>    n\longmapsto -n;
>    $$
> 5. satisface
>    $$
>    H_n^2=I;
>    $$
> 6. es impropia:
>    $$
>    \boxed{\det H_n=-1.}
>    $$

**Demostración.**
La linealidad se sigue directamente de la bilinealidad del producto escalar.
Si

$$
v=v_\perp+\alpha n,
$$

con $v_\perp\perp n$, entonces

$$
H_n(v)=v_\perp-\alpha n.
$$

Por Pitágoras,

$$
\|H_n(v)\|^2
=
\|v_\perp\|^2+\alpha^2
=
\|v\|^2.
$$

Por D32, $H_n$ es una isometría.
Si $v\in n^\perp$, entonces

$$
\langle v,n\rangle=0,
$$

y por tanto

$$
H_n(v)=v.
$$

Además,

$$
H_n(n)
=
n-2n
=
-n.
$$

Aplicar dos veces la misma regla devuelve cada componente a su signo inicial, de modo que

$$
H_n^2=I.
$$

Para el determinante, elegimos una base ortonormal positiva adaptada

$$
E=(e_1,e_2,n),
$$

con $e_1,e_2\in n^\perp$. Entonces

$$
A_E(H_n)
=
\begin{pmatrix}
1&0&0\\
0&1&0\\
0&0&-1
\end{pmatrix}.
$$

Por tanto,

$$
\det H_n=-1.
$$

$\square$

La reflexión conserva todas las longitudes y ángulos, pero invierte la orientación.

### 11.16. Construir una base ortonormal adaptada a un eje

Sea ahora $n$ unitario.
Elegimos un vector

$$
a\notin\operatorname{span}(n).
$$

Su residuo perpendicular a $n$ es

$$
r
=
a-\langle a,n\rangle n.
$$

Como $a$ no es paralelo a $n$,

$$
r\ne0.
$$

Definimos

$$
e_1:=\frac{r}{\|r\|}.
$$

Entonces

$$
e_1\perp n,
\qquad
\|e_1\|=1.
$$

Definimos después

$$
e_2:=n\times e_1.
$$

Como $n$ y $e_1$ son unitarios y ortogonales, P37 da

$$
\|e_2\|=1.
$$

Además, §9 implica

$$
e_2\perp n,
\qquad
e_2\perp e_1.
$$

Finalmente, P38 muestra que

$$
(n,e_1,e_2)
$$

tiene orientación positiva. La permutación cíclica

$$
(e_1,e_2,n)
$$

también es positiva.
Así obtenemos una base ortonormal positiva adaptada al eje $n$.

### 11.17. Definir: rotación axial

> **FPM-I-04-D35 — Rotación alrededor de un eje**
> Sea $n$ unitario y sea $\varphi\in\mathbb R$. Definimos
>
> $$
> \boxed{
> R_{n,\varphi}(v)
> :=
> \cos\varphi\,v
> +(1-\cos\varphi)\langle n,v\rangle n
> +\sin\varphi\,(n\times v).
> }
> $$

Esta fórmula es intrínseca: utiliza únicamente el producto escalar, el producto vectorial y el eje unitario $n$.
Si

$$
v=\alpha n+w,
\qquad
w\perp n,
$$

entonces

$$
R_{n,\varphi}(v)
=
\alpha n
+
\cos\varphi\,w
+
\sin\varphi\,(n\times w).
$$

Por tanto, la componente axial queda fija y la componente perpendicular rota dentro del plano $n^\perp$.

### 11.18. Proposición: matriz y propiedades de una rotación axial

> **FPM-I-04-P49 — Rotación axial como isometría propia**
> Sea
>
> $$
> E=(e_1,e_2,n)
> $$
>
> una base ortonormal positivamente orientada adaptada al eje $n$. Entonces
>
> $$
> \boxed{
> A_E(R_{n,\varphi})
> =
> \begin{pmatrix}
> \cos\varphi&-\sin\varphi&0\\
> \sin\varphi&\cos\varphi&0\\
> 0&0&1
> \end{pmatrix}.
> }
> $$
>
> En particular:
>
> 1. $R_{n,\varphi}$ es una isometría lineal;
> 2. fija el eje:
>    $$
>    R_{n,\varphi}(n)=n;
>    $$
> 3. es propia:
>    $$
>    \boxed{
>    \det R_{n,\varphi}=+1.
>    }
>    $$

**Demostración.**
Por bilinealidad del producto escalar y P34, las aplicaciones

$$
v\longmapsto v,
\qquad
v\longmapsto \langle n,v\rangle n,
\qquad
v\longmapsto n\times v
$$

son lineales. Por tanto, D35 define una transformación lineal

$$
R_{n,\varphi}:V\longrightarrow V,
$$

y D31 permite formar su matriz $A_E(R_{n,\varphi})$.
Como la base es positiva,

$$
n\times e_1=e_2,
$$

y por antisimetría,

$$
n\times e_2=-e_1.
$$

Además,

$$
n\times n=0.
$$

Por D35,

$$
R_{n,\varphi}(e_1)
=
\cos\varphi\,e_1
+
\sin\varphi\,e_2,
$$

$$
R_{n,\varphi}(e_2)
=
-\sin\varphi\,e_1
+
\cos\varphi\,e_2,
$$

y

$$
R_{n,\varphi}(n)=n.
$$

Estas tres columnas producen la matriz indicada.
Un cálculo directo da

$$
A_E(R_{n,\varphi})^{\mathsf T}
A_E(R_{n,\varphi})
=
I_3,
$$

usando

$$
\cos^2\varphi+\sin^2\varphi=1.
$$

Por P46, la transformación es una isometría.
Finalmente,

$$
\det A_E(R_{n,\varphi})
=
\cos^2\varphi+\sin^2\varphi
=
1.
$$

Por P44, este determinante es independiente de la base elegida. $\square$[^arfken-rotations]

### 11.19. Rotación y reflexión no se distinguen por conservar distancias

Tanto una rotación axial como una reflexión ortogonal satisfacen

$$
\|T(v)\|=\|v\|.
$$

Por tanto, ambas conservan:

- longitudes;
- productos escalares;
- ángulos;
- ortogonalidad;
- distancias.

La diferencia aparece en la orientación:

$$
\boxed{
\det R_{n,\varphi}=+1,
}
$$

mientras

$$
\boxed{
\det H_n=-1.
}
$$

Así, “preservar geometría métrica” no implica “preservar orientación”.

### 11.20. Principio metodológico: qué informa el determinante

> **FPM-I-04-MP20 — Usar el determinante para orientación, no para identificar toda la isometría**
> Para una matriz ortogonal $Q$:
>
> $$
> \det Q=+1
> $$
>
> indica que la isometría conserva orientación, mientras
>
> $$
> \det Q=-1
> $$
>
> indica que la invierte.
>
> El signo del determinante no determina por sí solo el ángulo, el eje o el plano geométrico concreto de la isometría.

No toda la información de una isometría está contenida en un único escalar.

### 11.21. Balance: rotaciones y reflexiones

Ya tenemos dos prototipos fundamentales:
**Reflexión ortogonal**

$$
\boxed{
H_n(v)
=
v-2\langle v,n\rangle n,
\qquad
\det H_n=-1,
}
$$

y **rotación axial**

$$
\boxed{
R_{n,\varphi}(v)
=
\cos\varphi\,v
+(1-\cos\varphi)\langle n,v\rangle n
+\sin\varphi(n\times v),
\qquad
\det R_{n,\varphi}=+1.
}
$$

Ambas son isometrías activas, no meros cambios pasivos de base.
Todavía falta completar la estructura algebraica mediante composición e inversa de isometrías y aplicar después estas distinciones en ejercicios.

### 11.22. Proposición: composición e inversa de isometrías

> **FPM-I-04-P50 — Composición, inversa y signo**
> Sean $T_1$ y $T_2$ isometrías lineales. Entonces:
>
> 1. la composición
>
> $$
> T_2\circ T_1
> $$
>
> es una isometría lineal;
>
> 2. cada $T_i$ es invertible y
>
> $$
> T_i^{-1}
> $$
>
> es también una isometría lineal;
>
> 3. los signos de orientación se multiplican:
>
> $$
> \boxed{
> \det(T_2\circ T_1)
> =
> \det(T_2)\det(T_1).
> }
> $$

**Demostración.** Elegimos una base ortonormal $E$ y escribimos

$$
Q_1=A_E(T_1),
\qquad
Q_2=A_E(T_2).
$$

Por P46,

$$
Q_1^{\mathsf T}Q_1=I,
\qquad
Q_2^{\mathsf T}Q_2=I.
$$

La matriz de la composición es

$$
A_E(T_2\circ T_1)
=
Q_2Q_1.
$$

Entonces

$$
\begin{aligned}
(Q_2Q_1)^{\mathsf T}(Q_2Q_1)
&=
Q_1^{\mathsf T}Q_2^{\mathsf T}Q_2Q_1\\
&=
Q_1^{\mathsf T}IQ_1\\
&=
I.
\end{aligned}
$$

Por P46, la composición es una isometría.
Además,

$$
Q_i^{-1}=Q_i^{\mathsf T},
$$

y

$$
(Q_i^{\mathsf T})^{\mathsf T}Q_i^{\mathsf T}
=
Q_iQ_i^{\mathsf T}
=
I,
$$

de modo que la inversa también es ortogonal y representa una isometría.
Finalmente, P26 da

$$
\det(Q_2Q_1)
=
\det(Q_2)\det(Q_1).
$$

Por P44, este signo no depende de la base elegida. $\square$
La proposición permite leer inmediatamente:

- propia seguida de propia $\Rightarrow$ propia;
- impropia seguida de impropia $\Rightarrow$ propia;
- propia seguida de impropia, o viceversa, $\Rightarrow$ impropia.

### 11.23. Comparación estructural: rotación frente a reflexión

Rotaciones axiales y reflexiones ortogonales comparten toda la estructura métrica:

$$
\boxed{
\|T(v)\|=\|v\|,
\qquad
\langle T(u),T(v)\rangle=\langle u,v\rangle.
}
$$

Pero difieren en tres rasgos fundamentales.

#### Orientación

Para una rotación axial,

$$
\det R_{n,\varphi}=+1.
$$

Para una reflexión ortogonal,

$$
\det H_n=-1.
$$

#### Conjunto de vectores fijos

Una rotación axial fija la recta

$$
\operatorname{span}(n).
$$

Una reflexión ortogonal fija el plano

$$
n^\perp.
$$

#### Acción sobre la dirección normal

La reflexión satisface

$$
H_n(n)=-n.
$$

La rotación satisface

$$
R_{n,\varphi}(n)=n.
$$

Por tanto, conocer sólo que una transformación es una isometría no basta para decidir su tipo geométrico.

> **FPM-I-04-MP21 — Clasificar una isometría por capas**
> Ante una isometría lineal, comprobar en este orden:
>
> 1. ortogonalidad de su matriz;
> 2. signo del determinante;
> 3. subespacio de vectores fijos;
> 4. acción sobre el complemento ortogonal.
>
> No inferir eje, plano o ángulo únicamente a partir de $\det Q$.

[]{#fispm-t1-c04-e0022}

### 11.24. Ejercicio FPM-I-04-E022 — Reflexión en un plano

> **Función pedagógica:** `Fórmula intrínseca → Matriz → Orientación`
>
> Sea
>
> $$
> E=(e_1,e_2,e_3)
> $$
>
> una base ortonormal positiva y consideremos la reflexión respecto del plano
>
> $$
> e_3^\perp.
> $$
>
> 1. Calcula la matriz de $H_{e_3}$ en $E$.
> 2. Verifica que es ortogonal.
> 3. Calcula su determinante.
> 4. Aplica la reflexión a
>
> $$
> v=2e_1-e_2+3e_3.
> $$
>
> 5. Verifica directamente que la norma se conserva.

> **Solución desarrollada**
>
> Como
>
> $$
> H_{e_3}(e_1)=e_1,
> \qquad
> H_{e_3}(e_2)=e_2,
> \qquad
> H_{e_3}(e_3)=-e_3,
> $$
>
> tenemos
>
> $$
> \boxed{
> A_E(H_{e_3})
> =
> \begin{pmatrix}
> 1&0&0\\
> 0&1&0\\
> 0&0&-1
> \end{pmatrix}.
> }
> $$
>
> Esta matriz satisface
>
> $$
> Q^{\mathsf T}Q=I_3,
> $$
>
> y
>
> $$
> \boxed{\det Q=-1}.
> $$
>
> Por tanto, la reflexión es una isometría impropia.
>
> Aplicando la fórmula,
>
> $$
> \boxed{
> H_{e_3}(v)
> =
> 2e_1-e_2-3e_3.
> }
> $$
>
> Finalmente,
>
> $$
> \|v\|^2
> =
> 2^2+(-1)^2+3^2
> =
> 14,
> $$
>
> y
>
> $$
> \|H_{e_3}(v)\|^2
> =
> 2^2+(-1)^2+(-3)^2
> =
> 14.
> $$
>
> La norma se conserva, pero la orientación global se invierte.

[]{#fispm-t1-c04-e0023}

### 11.25. Ejercicio FPM-I-04-E023 — Rotación de cuarto de vuelta

> **Función pedagógica:** `Rotación axial → Matriz → Invariantes`
>
> Sea
>
> $$
> E=(e_1,e_2,e_3)
> $$
>
> una base ortonormal positiva. Considera la rotación alrededor del eje $e_3$ con ángulo
>
> $$
> \varphi=\frac{\pi}{2}.
> $$
>
> 1. Calcula su matriz en $E$.
> 2. Verifica que es ortogonal.
> 3. Calcula su determinante.
> 4. Aplica la rotación a
>
> $$
> v=2e_1+e_2+3e_3.
> $$
>
> 5. Comprueba que la norma se conserva.
> 6. Determina el resultado de aplicar cuatro veces la rotación.

> **Solución desarrollada**
>
> Como
>
> $$
> \cos\frac{\pi}{2}=0,
> \qquad
> \sin\frac{\pi}{2}=1,
> $$
>
> P49 da
>
> $$
> \boxed{
> Q
> =
> \begin{pmatrix}
> 0&-1&0\\
> 1&0&0\\
> 0&0&1
> \end{pmatrix}.
> }
> $$
>
> Un cálculo directo muestra
>
> $$
> Q^{\mathsf T}Q=I_3.
> $$
>
> Además,
>
> $$
> \boxed{\det Q=+1}.
> $$
>
> La isometría es propia.
>
> Aplicando $Q$ a
>
> $$
> [v]_E=
> \begin{pmatrix}
> 2\\
> 1\\
> 3
> \end{pmatrix},
> $$
>
> obtenemos
>
> $$
> [R_{e_3,\pi/2}(v)]_E
> =
> \begin{pmatrix}
> -1\\
> 2\\
> 3
> \end{pmatrix}.
> $$
>
> Por tanto,
>
> $$
> \boxed{
> R_{e_3,\pi/2}(v)
> =
> -e_1+2e_2+3e_3.
> }
> $$
>
> Las normas satisfacen
>
> $$
> \|v\|^2
> =
> 2^2+1^2+3^2
> =
> 14,
> $$
>
> y
>
> $$
> \|R_{e_3,\pi/2}(v)\|^2
> =
> (-1)^2+2^2+3^2
> =
> 14.
> $$
>
> Finalmente,
>
> $$
> Q^2
> =
> \begin{pmatrix}
> -1&0&0\\
> 0&-1&0\\
> 0&0&1
> \end{pmatrix},
> $$
>
> y
>
> $$
> \boxed{
> Q^4=I_3.
> }
> $$
>
> Cuatro cuartos de vuelta restauran todo vector.

### 11.26. Cierre de §11

La sección ha construido la noción de **transformación lineal que preserva la geometría**:

$$
\boxed{
T\text{ isometría}
\Longleftrightarrow
\|T(v)\|=\|v\|
}
$$

y, equivalentemente,

$$
\boxed{
\langle T(u),T(v)\rangle
=
\langle u,v\rangle.
}
$$

En una base ortonormal,

$$
\boxed{
Q^{\mathsf T}Q=I,
\qquad
Q^{-1}=Q^{\mathsf T},
\qquad
\det Q=\pm1.
}
$$

El signo del determinante separa las dos clases:

$$
\boxed{
\det Q=+1
\Longrightarrow
\text{isometría propia},
}
$$

$$
\boxed{
\det Q=-1
\Longrightarrow
\text{isometría impropia}.
}
$$

Los prototipos construidos son:

$$
\boxed{
R_{n,\varphi}
\quad\text{rotación axial, propia},
}
$$

y

$$
\boxed{
H_n
\quad\text{reflexión ortogonal, impropia}.
}
$$

La composición de isometrías vuelve a ser una isometría y los signos de orientación se multiplican.
La siguiente sección volverá del espacio vectorial al espacio afín: estudiaremos simultáneamente cambios de origen y de base en un marco geométrico completo.
El siguiente paso será:

$$
\boxed{
\text{§12 — Cambios de origen y de marco geométrico}
}
$$

[^arfken-rotations]: G. B. Arfken, H. J. Weber y F. E. Harris, *Mathematical Methods for Physicists*, 7.ª ed., Academic Press, 2013, cap. 3, §3.4 «Rotations in $\mathbb R^3$», pp. 139–142.

---

[]{#fispm-t1-c04-s12}

[]{#fpm-i-04-s12}

## §12 — Cambios de origen y de marco geométrico

### 12.1. Activación: ahora cambian dos datos a la vez

Hasta aquí hemos estudiado por separado dos operaciones:

1. cambiar el **origen** manteniendo fija la base;
2. cambiar la **base** manteniendo fijo el vector geométrico.

Un marco afín completo contiene ambos datos:

$$
F=(O,B).
$$

Por tanto, al pasar a otro marco

$$
F'=(O',B'),
$$

pueden cambiar simultáneamente:

- el punto elegido como origen;
- la base usada para describir los desplazamientos.

La pregunta central es:

> Cambio completo de marco
> Dado un punto $P$, ¿cómo se transforma su columna de coordenadas cuando pasamos de
>
> $$
> F=(O,B)
> $$
>
> a
>
> $$
> F'=(O',B')?
> $$

La respuesta combinará exactamente las leyes de §§4 y 10.

### 12.2. Definir: datos de un cambio de marco afín

> **FPM-I-04-D36 — Cambio entre dos marcos afines**
> Sean
>
> $$
> F=(O,B),
> \qquad
> F'=(O',B')
> $$
>
> dos marcos afines.
>
> Definimos:
>
> $$
> \boxed{
> a:=\overrightarrow{OO'}
> }
> $$
>
> y
>
> $$
> \boxed{
> S:=S_{B\leftarrow B'}.
> }
> $$
>
> Es decir:
>
> - $a$ es el desplazamiento desde el origen antiguo al nuevo;
> - las columnas de $S$ son los vectores de la base nueva $B'$ expresados en la base antigua $B$.

Usaremos

$$
[a]_B
$$

para la columna del desplazamiento del origen nuevo respecto del antiguo.
La convención de signo queda fijada por

$$
\boxed{
O'=O+a.
}
$$

### 12.3. Derivación geométrica antes de escribir matrices

Para cualquier punto $P$,

$$
\overrightarrow{OP}
=
\overrightarrow{OO'}
+
\overrightarrow{O'P}.
$$

Como

$$
\overrightarrow{OO'}=a,
$$

obtenemos

$$
\boxed{
\overrightarrow{O'P}
=
\overrightarrow{OP}-a.
}
$$

Esta identidad es puramente afín y no depende de coordenadas.
Ahora expresamos ambos lados en la base antigua $B$:

$$
[\overrightarrow{O'P}]_B
=
[\overrightarrow{OP}]_B-[a]_B.
$$

Pero la columna que buscamos en el marco nuevo utiliza la base $B'$:

$$
x_{F'}(P)
=
[\overrightarrow{O'P}]_{B'}.
$$

Por P39,

$$
[\overrightarrow{O'P}]_{B'}
=
S^{-1}
[\overrightarrow{O'P}]_B.
$$

Sustituir la relación anterior produce la ley completa.

### 12.4. Proposición: ley afín de cambio de marco

> **FPM-I-04-P51 — Transformación de las coordenadas de un punto**
> Sean
>
> $$
> F=(O,B),
> \qquad
> F'=(O',B'),
> $$
>
> con
>
> $$
> a=\overrightarrow{OO'},
> \qquad
> S=S_{B\leftarrow B'}.
> $$
>
> Entonces, para todo punto $P$,
>
> $$
> \boxed{
> x_{F'}(P)
> =
> S^{-1}
> \left(
> x_F(P)-[a]_B
> \right).
> }
> $$

**Demostración.** Por D12,

$$
x_F(P)
=
[\overrightarrow{OP}]_B,
$$

y

$$
x_{F'}(P)
=
[\overrightarrow{O'P}]_{B'}.
$$

La ley del triángulo da

$$
\overrightarrow{O'P}
=
\overrightarrow{OP}-a.
$$

Tomando componentes en $B$,

$$
[\overrightarrow{O'P}]_B
=
x_F(P)-[a]_B.
$$

Finalmente, P39 transforma componentes desde $B$ hacia $B'$:

$$
[\overrightarrow{O'P}]_{B'}
=
S^{-1}
[\overrightarrow{O'P}]_B.
$$

Por tanto,

$$
x_{F'}(P)
=
S^{-1}
\left(
x_F(P)-[a]_B
\right).
$$

$\square$

Ésta será la convención canónica para todos los cambios de marco del capítulo.

### 12.5. Por qué la transformación de puntos es afín, no lineal

Definamos la aplicación sobre columnas

$$
\Phi_{F'\leftarrow F}(x)
:=
S^{-1}(x-[a]_B).
$$

Puede escribirse como

$$
\boxed{
\Phi_{F'\leftarrow F}(x)
=
S^{-1}x
-
S^{-1}[a]_B.
}
$$

El primer término es lineal en $x$.
El segundo es una traslación constante.
Por tanto, si

$$
a\ne0,
$$

la transformación de coordenadas de puntos no es lineal:

$$
\Phi_{F'\leftarrow F}(0)
=
-S^{-1}[a]_B
\ne0.
$$

Es una transformación **afín**.
Sólo cuando los dos marcos comparten el mismo origen,

$$
a=0,
$$

la ley se reduce al cambio lineal de base:

$$
x_{F'}(P)=S^{-1}x_F(P).
$$

### 12.6. Proposición: los desplazamientos no sienten el cambio de origen

> **FPM-I-04-P52 — Transformación de un desplazamiento entre marcos**
> Para cualesquiera puntos $P,Q$,
>
> $$
> \boxed{
> [\overrightarrow{PQ}]_{B'}
> =
> S^{-1}
> [\overrightarrow{PQ}]_B.
> }
> $$
>
> El término de traslación asociado al cambio de origen se cancela.

**Demostración.** Por P09,

$$
[\overrightarrow{PQ}]_B
=
x_F(Q)-x_F(P),
$$

y

$$
[\overrightarrow{PQ}]_{B'}
=
x_{F'}(Q)-x_{F'}(P).
$$

Aplicamos P51:

$$
x_{F'}(Q)
=
S^{-1}
\left(
x_F(Q)-[a]_B
\right),
$$

$$
x_{F'}(P)
=
S^{-1}
\left(
x_F(P)-[a]_B
\right).
$$

Restando,

$$
\begin{aligned}
x_{F'}(Q)-x_{F'}(P)
&=
S^{-1}
\left(
x_F(Q)-[a]_B
\right)\\
&\quad-
S^{-1}
\left(
x_F(P)-[a]_B
\right)\\
&=
S^{-1}
\left(
x_F(Q)-x_F(P)
\right).
\end{aligned}
$$

Luego

$$
[\overrightarrow{PQ}]_{B'}
=
S^{-1}
[\overrightarrow{PQ}]_B.
$$

$\square$

La traslación afecta las coordenadas absolutas de los puntos, pero no el desplazamiento entre ellos.

### 12.7. Punto y vector obedecen leyes distintas

Para un **punto**:

$$
\boxed{
x_{F'}(P)
=
S^{-1}
\left(
x_F(P)-[a]_B
\right).
}
$$

Para un **vector** $v\in V$:

$$
\boxed{
[v]_{B'}
=
S^{-1}[v]_B.
}
$$

La diferencia es exactamente el término

$$
-S^{-1}[a]_B.
$$

Ese término sólo aparece porque un punto no pertenece al espacio vectorial de desplazamientos.
Esta es una de las razones fundamentales por las que §1 insistió en que

$$
\boxed{
\text{un punto no es un vector}.
}
$$

### 12.8. Dos casos límite recuperan resultados anteriores

#### Sólo cambia el origen

Si

$$
B'=B,
$$

entonces

$$
S=I,
$$

y P51 se reduce a

$$
\boxed{
x_{F'}(P)
=
x_F(P)-[a]_B,
}
$$

que es exactamente P10.

#### Sólo cambia la base

Si

$$
O'=O,
$$

entonces

$$
a=0,
$$

y P51 se reduce a

$$
\boxed{
x_{F'}(P)
=
S^{-1}x_F(P).
}
$$

Es la misma ley lineal que P39 aplicada al vector de posición relativo al origen común.
Así, P51 contiene como casos particulares los dos cambios estudiados anteriormente.

### 12.9. Ejemplo diagnóstico de signo

Sea

$$
B=(e_1,e_2,e_3),
$$

y supongamos que el nuevo origen satisface

$$
O'=O+2e_1.
$$

Entonces

$$
[a]_B
=
\begin{pmatrix}
2\\
0\\
0
\end{pmatrix}.
$$

Tomemos primero la misma base:

$$
B'=B.
$$

Para un punto con

$$
x_F(P)
=
\begin{pmatrix}
5\\
1\\
0
\end{pmatrix},
$$

P51 da

$$
x_{F'}(P)
=
\begin{pmatrix}
5\\
1\\
0
\end{pmatrix}
-
\begin{pmatrix}
2\\
0\\
0
\end{pmatrix}
=
\begin{pmatrix}
3\\
1\\
0
\end{pmatrix}.
$$

El signo negativo es geométricamente inevitable: al mover el origen **hacia** el punto en la dirección $+e_1$, la primera coordenada del punto disminuye.
Este control geométrico del signo debe hacerse antes de memorizar la fórmula.

### 12.10. Principio metodológico

> **FPM-I-04-MP22 — Separar la parte traslacional de la parte lineal**
> En un cambio completo de marco
>
> $$
> F=(O,B)
> \longrightarrow
> F'=(O',B'),
> $$
>
> identificar por separado:
>
> 1. el desplazamiento del origen
>    $$
>    a=\overrightarrow{OO'};
>    $$
> 2. la matriz de cambio de base
>    $$
>    S_{B\leftarrow B'}.
>    $$
>
> Las coordenadas de puntos transforman afínmente,
>
> $$
> x_{F'}=S^{-1}(x_F-[a]_B),
> $$
>
> mientras las componentes de vectores transforman linealmente,
>
> $$
> [v]_{B'}=S^{-1}[v]_B.
> $$

### 12.11. Balance: ley afín y separación punto–vector

Queda establecida la ley conjunta:

$$
\boxed{
x_{F'}(P)
=
S^{-1}
\left(
x_F(P)-[a]_B
\right).
}
$$

Su estructura contiene dos capas:

$$
\boxed{
\text{traslación del origen}
+
\text{cambio lineal de base}.
}
$$

Y la diferencia entre puntos elimina automáticamente la parte traslacional:

$$
\boxed{
[\overrightarrow{PQ}]_{B'}
=
S^{-1}
[\overrightarrow{PQ}]_B.
}
$$

Todavía falta estudiar cómo se componen dos cambios completos de marco, cómo se invierte uno de ellos y cómo conviene empaquetarlos algebraicamente sin borrar la distinción entre puntos y vectores.

### 12.12. Tres marcos y dos cambios sucesivos

Consideremos tres marcos afines:

$$
F=(O,B),
\qquad
F'=(O',B'),
\qquad
F''=(O'',B'').
$$

Para el primer cambio definimos

$$
a:=\overrightarrow{OO'},
\qquad
S:=S_{B\leftarrow B'}.
$$

Para el segundo cambio definimos

$$
b:=\overrightarrow{O'O''},
\qquad
R:=S_{B'\leftarrow B''}.
$$

Por P51,

$$
x_{F'}(P)
=
S^{-1}
\left(
x_F(P)-[a]_B
\right),
$$

y después

$$
x_{F''}(P)
=
R^{-1}
\left(
x_{F'}(P)-[b]_{B'}
\right).
$$

El objetivo es comparar esta ruta en dos etapas con el cambio directo

$$
F\longrightarrow F''.
$$

### 12.13. El desplazamiento total de los orígenes

La ley del triángulo afín da

$$
\overrightarrow{OO''}
=
\overrightarrow{OO'}
+
\overrightarrow{O'O''}.
$$

Definimos

$$
c:=\overrightarrow{OO''}.
$$

Entonces

$$
\boxed{
c=a+b.
}
$$

Como $a$ está expresado naturalmente en $B$ y $b$ puede venir expresado en $B'$, para sumar sus columnas debemos convertir primero:

$$
[b]_B
=
S[b]_{B'}.
$$

Por tanto,

$$
\boxed{
[c]_B
=
[a]_B
+
S[b]_{B'}.
}
$$

La suma geométrica de vectores es intrínseca; la suma de columnas sólo es legítima cuando ambas columnas están expresadas en la misma base.

### 12.14. Proposición: composición de cambios completos de marco

> **FPM-I-04-P53 — Composición de cambios de marco afín**
> Con las definiciones anteriores,
>
> $$
> S_{B\leftarrow B''}
> =
> SR
> $$
>
> y
>
> $$
> \boxed{
> x_{F''}(P)
> =
> (SR)^{-1}
> \left(
> x_F(P)-[c]_B
> \right),
> }
> $$
>
> donde
>
> $$
> [c]_B
> =
> [a]_B+S[b]_{B'}.
> $$

**Demostración.** Sustituimos la primera transformación en la segunda:

$$
\begin{aligned}
x_{F''}(P)
&=
R^{-1}
\left[
S^{-1}
\left(
x_F(P)-[a]_B
\right)
-
[b]_{B'}
\right].
\end{aligned}
$$

Distribuimos:

$$
x_{F''}(P)
=
R^{-1}S^{-1}
\left(
x_F(P)-[a]_B
\right)
-
R^{-1}[b]_{B'}.
$$

Como

$$
R^{-1}S^{-1}
=
(SR)^{-1},
$$

podemos escribir el segundo término como

$$
R^{-1}[b]_{B'}
=
(SR)^{-1}S[b]_{B'}.
$$

Por tanto,

$$
x_{F''}(P)
=
(SR)^{-1}
\left(
x_F(P)
-
[a]_B
-
S[b]_{B'}
\right).
$$

Por §12.13,

$$
[a]_B+S[b]_{B'}
=
[c]_B.
$$

Luego

$$
x_{F''}(P)
=
(SR)^{-1}
\left(
x_F(P)-[c]_B
\right).
$$

Finalmente, P41 da

$$
S_{B\leftarrow B''}
=
S_{B\leftarrow B'}
S_{B'\leftarrow B''}
=
SR.
$$

$\square$

La forma de la ley se conserva bajo composición: un cambio de marco seguido de otro sigue siendo un cambio afín del mismo tipo.

### 12.15. Definir: representación afín coordenada

> **FPM-I-04-D37 — Par afín asociado a un cambio de marco**
> Para
>
> $$
> F=(O,B)
> \longrightarrow
> F'=(O',B'),
> $$
>
> definimos
>
> $$
> L:=S^{-1},
> $$
>
> y
>
> $$
> t:=-S^{-1}[a]_B.
> $$
>
> Entonces la transformación de coordenadas de puntos adopta la forma
>
> $$
> \boxed{
> \Phi_{F'\leftarrow F}(x)
> =
> Lx+t.
> }
> $$

El par

$$
(L,t)
$$

separa explícitamente:

- la parte lineal $L$;
- la parte traslacional $t$.

Esta notación no convierte los puntos en vectores: sólo representa la aplicación entre sus columnas de coordenadas.

### 12.16. Proposición: ley algebraica de composición de pares afines

> **FPM-I-04-P54 — Composición de pares afines**
> Sean
>
> $$
> \Phi_1(x)=L_1x+t_1
> $$
>
> y
>
> $$
> \Phi_2(x)=L_2x+t_2.
> $$
>
> Entonces
>
> $$
> \boxed{
> (\Phi_2\circ\Phi_1)(x)
> =
> (L_2L_1)x
> +
> (L_2t_1+t_2).
> }
> $$
>
> Por tanto, la composición de los pares es
>
> $$
> \boxed{
> (L_2,t_2)\circ(L_1,t_1)
> =
> (L_2L_1,\ L_2t_1+t_2).
> }
> $$

**Demostración.**

$$
\begin{aligned}
(\Phi_2\circ\Phi_1)(x)
&=
\Phi_2(L_1x+t_1)\\
&=
L_2(L_1x+t_1)+t_2\\
&=
L_2L_1x+L_2t_1+t_2.
\end{aligned}
$$

$\square$

Obsérvese que las traslaciones no se suman sin más: la primera debe ser transportada por la parte lineal del segundo cambio antes de combinarse.

### 12.17. Proposición: cambio inverso de marco

> **FPM-I-04-P55 — Inversa de un cambio de marco afín**
> Si
>
> $$
> \Phi(x)
> =
> Lx+t
> $$
>
> con $L$ invertible, entonces
>
> $$
> \boxed{
> \Phi^{-1}(x')
> =
> L^{-1}x'
> -
> L^{-1}t.
> }
> $$
>
> En términos de pares,
>
> $$
> \boxed{
> (L,t)^{-1}
> =
> \left(
> L^{-1},
> -L^{-1}t
> \right).
> }
> $$

**Demostración.** De

$$
x'=Lx+t
$$

obtenemos

$$
x'-t=Lx.
$$

Multiplicando por $L^{-1}$,

$$
x
=
L^{-1}(x'-t)
=
L^{-1}x'-L^{-1}t.
$$

$\square$

Para el cambio de marco de D36,

$$
L=S^{-1},
\qquad
t=-S^{-1}[a]_B.
$$

Así,

$$
L^{-1}=S,
$$

y

$$
-L^{-1}t
=
-S\left(-S^{-1}[a]_B\right)
=
[a]_B.
$$

Por tanto, la transformación inversa es

$$
\boxed{
x_F(P)
=
Sx_{F'}(P)+[a]_B.
}
$$

Esta fórmula es exactamente la resolución de P51 para $x_F(P)$.

### 12.18. Interpretación geométrica del cambio inverso

Desde el marco nuevo hacia el antiguo, el desplazamiento del origen es

$$
\overrightarrow{O'O}
=
-a.
$$

Su columna en la base nueva es

$$
[-a]_{B'}
=
-S^{-1}[a]_B.
$$

Además,

$$
S_{B'\leftarrow B}
=
S^{-1}.
$$

Aplicando P51 en sentido inverso,

$$
x_F(P)
=
\left(S^{-1}\right)^{-1}
\left(
x_{F'}(P)-[-a]_{B'}
\right).
$$

Por tanto,

$$
x_F(P)
=
S
\left(
x_{F'}(P)
+
S^{-1}[a]_B
\right)
=
Sx_{F'}(P)+[a]_B.
$$

La fórmula algebraica de P55 coincide exactamente con la geometría del cambio de origen invertido.

### 12.19. Ejemplo de consistencia por dos caminos

Tomemos

$$
S=
\begin{pmatrix}
1&0&0\\
1&1&0\\
0&0&1
\end{pmatrix},
$$

$$
R=
\begin{pmatrix}
1&0&0\\
0&1&0\\
0&1&1
\end{pmatrix},
$$

y

$$
[a]_B
=
\begin{pmatrix}
1\\
0\\
0
\end{pmatrix},
\qquad
[b]_{B'}
=
\begin{pmatrix}
0\\
1\\
0
\end{pmatrix}.
$$

Entonces

$$
S[b]_{B'}
=
\begin{pmatrix}
0\\
1\\
0
\end{pmatrix},
$$

de modo que

$$
[c]_B
=
\begin{pmatrix}
1\\
1\\
0
\end{pmatrix}.
$$

Además,

$$
SR
=
\begin{pmatrix}
1&0&0\\
1&1&0\\
0&1&1
\end{pmatrix}.
$$

Sea un punto con

$$
x_F(P)
=
\begin{pmatrix}
4\\
3\\
2
\end{pmatrix}.
$$

#### Ruta en dos etapas

Primero,

$$
x_{F'}(P)
=
S^{-1}
\left(
x_F(P)-[a]_B
\right)
=
\begin{pmatrix}
3\\
0\\
2
\end{pmatrix}.
$$

Después,

$$
x_{F''}(P)
=
R^{-1}
\left(
x_{F'}(P)-[b]_{B'}
\right)
=
\begin{pmatrix}
3\\
-1\\
3
\end{pmatrix}.
$$

#### Ruta directa

P53 da

$$
x_{F''}(P)
=
(SR)^{-1}
\left(
x_F(P)-[c]_B
\right),
$$

y el resultado es nuevamente

$$
\boxed{
x_{F''}(P)
=
\begin{pmatrix}
3\\
-1\\
3
\end{pmatrix}.
}
$$

La coincidencia no es accidental: es la condición de consistencia del cambio de marcos.

### 12.20. Principio metodológico de tipado

> **FPM-I-04-MP23 — No sumar columnas escritas en bases distintas**
> Los vectores
>
> $$
> a
> \qquad\text{y}\qquad
> b
> $$
>
> pueden sumarse intrínsecamente en $V$.
>
> Sus columnas, en cambio, sólo pueden sumarse después de expresarlas en una base común:
>
> $$
> [c]_B
> =
> [a]_B
> +
> S[b]_{B'}.
> $$
>
> La notación de bases funciona como un control de tipos: una suma de columnas con etiquetas incompatibles carece de interpretación geométrica hasta efectuar la conversión correspondiente.

Este principio evita uno de los errores más frecuentes al componer traslaciones y cambios de base.

### 12.21. Balance: composición, inversa y tipado

Los cambios completos de marco quedan ahora cerrados algebraicamente bajo composición:

$$
\boxed{
(L_2,t_2)\circ(L_1,t_1)
=
(L_2L_1,\ L_2t_1+t_2),
}
$$

y admiten inversa:

$$
\boxed{
(L,t)^{-1}
=
(L^{-1},-L^{-1}t).
}
$$

En la notación geométrica de marcos,

$$
\boxed{
S_{B\leftarrow B''}
=
S_{B\leftarrow B'}
S_{B'\leftarrow B''},
}
$$

y

$$
\boxed{
[\overrightarrow{OO''}]_B
=
[\overrightarrow{OO'}]_B
+
S_{B\leftarrow B'}
[\overrightarrow{O'O''}]_{B'}.
}
$$

La estructura afín conserva así dos capas inseparables pero distintas:

$$
\boxed{
\text{parte lineal}
+
\text{parte traslacional}.
}
$$

Todavía falta ejercitar estas leyes y preparar la transición desde un marco geométrico puramente matemático hacia la noción física de marco de referencia.

### 12.22. Proposición: marcos ortonormales y conservación de distancias

> **FPM-I-04-P56 — Invariancia métrica entre marcos ortonormales**
> Sean
>
> $$
> F=(O,E),
> \qquad
> F'=(O',E')
> $$
>
> dos marcos cuyas bases $E$ y $E'$ son ortonormales.
>
> Entonces, para cualesquiera puntos $P,Q$,
>
> $$
> \boxed{
> \left\|
> x_{F'}(Q)-x_{F'}(P)
> \right\|
> =
> \left\|
> x_F(Q)-x_F(P)
> \right\|.
> }
> $$

**Demostración.** Por P52,

$$
x_{F'}(Q)-x_{F'}(P)
=
S^{-1}
\left(
x_F(Q)-x_F(P)
\right),
$$

donde

$$
S=S_{E\leftarrow E'}.
$$

Las columnas de

$$
S=S_{E\leftarrow E'}
$$

son

$$
[e'_1]_E,
\qquad
[e'_2]_E,
\qquad
[e'_3]_E.
$$

Como $E$ y $E'$ son ortonormales, el producto escalar entre las columnas $i$ y $j$ es

$$
\langle e'_i,e'_j\rangle
=
\delta_{ij}.
$$

Por tanto,

$$
S^{\mathsf T}S=I.
$$

Así,

$$
S^{-1}=S^{\mathsf T}
$$

y la matriz $S^{-1}$ conserva la norma euclídea de las columnas.
Por tanto,

$$
\left\|
x_{F'}(Q)-x_{F'}(P)
\right\|
=
\left\|
x_F(Q)-x_F(P)
\right\|.
$$

$\square$

El cambio de origen modifica las coordenadas individuales de $P$ y $Q$, pero desaparece al formar su diferencia. El cambio ortogonal de base, por su parte, conserva la norma de esa diferencia.

### 12.23. Cambio de descripción no significa movimiento del punto

En toda esta sección hemos considerado un mismo punto geométrico $P$ descrito desde marcos distintos:

$$
P
\longmapsto
x_F(P),
\qquad
P
\longmapsto
x_{F'}(P).
$$

La relación

$$
x_{F'}(P)
=
S^{-1}
\left(
x_F(P)-[a]_B
\right)
$$

no mueve a $P$.
Cambia únicamente su **descripción coordenada**.
Esto debe distinguirse de una transformación afín activa

$$
P\longmapsto A(P),
$$

en la que el punto geométrico sí cambia.

> **FPM-I-04-MP24 — Separar cambio de marco de movimiento geométrico**
> Una fórmula afín de la forma
>
> $$
> x'\!=Lx+t
> $$
>
> no determina por sí sola si estamos ante:
>
> - dos descripciones del mismo punto en marcos diferentes;
> - o una transformación activa que envía un punto a otro.
>
> Antes de interpretar la fórmula, declarar explícitamente qué permanece fijo: el punto o el marco.

La distinción es la versión afín del principio activo/pasivo establecido en §10.

[]{#fispm-t1-c04-e0024}

### 12.24. Ejercicio FPM-I-04-E024 — Cambio simultáneo de origen y base

> **Función pedagógica:** `Marco afín → Conversión de punto → Desplazamiento → Invariante métrico`
>
> Sea
>
> $$
> F=(O,E),
> \qquad
> E=(e_1,e_2,e_3)
> $$
>
> un marco ortonormal positivo.
>
> Definimos otro marco
>
> $$
> F'=(O',E')
> $$
>
> mediante
>
> $$
> \overrightarrow{OO'}
> =
> e_1-2e_2+e_3
> $$
>
> y
>
> $$
> E'
> =
> (e_2,-e_1,e_3).
> $$
>
> Sean los puntos $P,Q$ con
>
> $$
> x_F(P)
> =
> \begin{pmatrix}
> 4\\
> 1\\
> 3
> \end{pmatrix},
> \qquad
> x_F(Q)
> =
> \begin{pmatrix}
> 2\\
> 5\\
> 0
> \end{pmatrix}.
> $$
>
> 1. Calcula $S_{E\leftarrow E'}$.
> 2. Calcula $x_{F'}(P)$ y $x_{F'}(Q)$.
> 3. Calcula $[\overrightarrow{PQ}]_E$ y $[\overrightarrow{PQ}]_{E'}$.
> 4. Verifica P52.
> 5. Verifica P56.

> **Solución desarrollada**
>
> Las columnas de la base nueva escritas en la antigua son
>
> $$
> [e'_1]_E
> =
> \begin{pmatrix}
> 0\\
> 1\\
> 0
> \end{pmatrix},
> \qquad
> [e'_2]_E
> =
> \begin{pmatrix}
> -1\\
> 0\\
> 0
> \end{pmatrix},
> \qquad
> [e'_3]_E
> =
> \begin{pmatrix}
> 0\\
> 0\\
> 1
> \end{pmatrix}.
> $$
>
> Por tanto,
>
> $$
> S
> =
> \begin{pmatrix}
> 0&-1&0\\
> 1&0&0\\
> 0&0&1
> \end{pmatrix}.
> $$
>
> Como $S$ es ortogonal,
>
> $$
> S^{-1}
> =
> S^{\mathsf T}
> =
> \begin{pmatrix}
> 0&1&0\\
> -1&0&0\\
> 0&0&1
> \end{pmatrix}.
> $$
>
> Además,
>
> $$
> [a]_E
> =
> \begin{pmatrix}
> 1\\
> -2\\
> 1
> \end{pmatrix}.
> $$
>
> Para $P$,
>
> $$
> x_F(P)-[a]_E
> =
> \begin{pmatrix}
> 3\\
> 3\\
> 2
> \end{pmatrix},
> $$
>
> y
>
> $$
> \boxed{
> x_{F'}(P)
> =
> \begin{pmatrix}
> 3\\
> -3\\
> 2
> \end{pmatrix}.
> }
> $$
>
> Para $Q$,
>
> $$
> x_F(Q)-[a]_E
> =
> \begin{pmatrix}
> 1\\
> 7\\
> -1
> \end{pmatrix},
> $$
>
> y
>
> $$
> \boxed{
> x_{F'}(Q)
> =
> \begin{pmatrix}
> 7\\
> -1\\
> -1
> \end{pmatrix}.
> }
> $$
>
> En el marco antiguo,
>
> $$
> [\overrightarrow{PQ}]_E
> =
> x_F(Q)-x_F(P)
> =
> \begin{pmatrix}
> -2\\
> 4\\
> -3
> \end{pmatrix}.
> $$
>
> En el nuevo,
>
> $$
> [\overrightarrow{PQ}]_{E'}
> =
> x_{F'}(Q)-x_{F'}(P)
> =
> \begin{pmatrix}
> 4\\
> 2\\
> -3
> \end{pmatrix}.
> $$
>
> Y, efectivamente,
>
> $$
> S^{-1}
> \begin{pmatrix}
> -2\\
> 4\\
> -3
> \end{pmatrix}
> =
> \begin{pmatrix}
> 4\\
> 2\\
> -3
> \end{pmatrix}.
> $$
>
> Finalmente,
>
> $$
> \|[\overrightarrow{PQ}]_E\|^2
> =
> (-2)^2+4^2+(-3)^2
> =
> 29,
> $$
>
> mientras
>
> $$
> \|[\overrightarrow{PQ}]_{E'}\|^2
> =
> 4^2+2^2+(-3)^2
> =
> 29.
> $$
>
> La descripción cambia; la distancia geométrica no.

[]{#fispm-t1-c04-e0025}

### 12.25. Ejercicio FPM-I-04-E025 — Composición e inversa de pares afines

> **Función pedagógica:** `Composición afín → Verificación por dos rutas → Inversa`
>
> Considera dos transformaciones de coordenadas
>
> $$
> \Phi_1(x)=L_1x+t_1,
> $$
>
> $$
> \Phi_2(x)=L_2x+t_2,
> $$
>
> con
>
> $$
> L_1
> =
> \begin{pmatrix}
> 0&1&0\\
> -1&0&0\\
> 0&0&1
> \end{pmatrix},
> \qquad
> t_1
> =
> \begin{pmatrix}
> -2\\
> 1\\
> 0
> \end{pmatrix},
> $$
>
> y
>
> $$
> L_2
> =
> \begin{pmatrix}
> 1&0&0\\
> 0&-1&0\\
> 0&0&1
> \end{pmatrix},
> \qquad
> t_2
> =
> \begin{pmatrix}
> 0\\
> 3\\
> -1
> \end{pmatrix}.
> $$
>
> 1. Calcula el par afín de $\Phi_2\circ\Phi_1$.
> 2. Evalúa las dos transformaciones sucesivamente sobre
>
> $$
> x=
> \begin{pmatrix}
> 4\\
> 2\\
> 5
> \end{pmatrix}.
> $$
>
> 3. Verifica que el cambio compuesto da el mismo resultado.
> 4. Calcula la inversa del cambio compuesto.
> 5. Usa esa inversa para recuperar la columna inicial.

> **Solución desarrollada**
>
> La parte lineal compuesta es
>
> $$
> L
> =
> L_2L_1
> =
> \begin{pmatrix}
> 0&1&0\\
> 1&0&0\\
> 0&0&1
> \end{pmatrix}.
> $$
>
> La parte traslacional es
>
> $$
> \begin{aligned}
> t
> &=
> L_2t_1+t_2\\
> &=
> \begin{pmatrix}
> -2\\
> -1\\
> 0
> \end{pmatrix}
> +
> \begin{pmatrix}
> 0\\
> 3\\
> -1
> \end{pmatrix}\\
> &=
> \begin{pmatrix}
> -2\\
> 2\\
> -1
> \end{pmatrix}.
> \end{aligned}
> $$
>
> Por tanto,
>
> $$
> \boxed{
> (\Phi_2\circ\Phi_1)(x)
> =
> Lx+t.
> }
> $$
>
> Aplicando primero $\Phi_1$,
>
> $$
> \Phi_1(x)
> =
> \begin{pmatrix}
> 0\\
> -3\\
> 5
> \end{pmatrix}.
> $$
>
> Después,
>
> $$
> \Phi_2(\Phi_1(x))
> =
> \boxed{
> \begin{pmatrix}
> 0\\
> 6\\
> 4
> \end{pmatrix}
> }.
> $$
>
> Por la ruta directa,
>
> $$
> Lx+t
> =
> \begin{pmatrix}
> 2\\
> 4\\
> 5
> \end{pmatrix}
> +
> \begin{pmatrix}
> -2\\
> 2\\
> -1
> \end{pmatrix}
> =
> \begin{pmatrix}
> 0\\
> 6\\
> 4
> \end{pmatrix}.
> $$
>
> Como
>
> $$
> L^{-1}=L,
> $$
>
> P55 da
>
> $$
> (\Phi_2\circ\Phi_1)^{-1}(x')
> =
> Lx'-Lt.
> $$
>
> Tenemos
>
> $$
> -Lt
> =
> \begin{pmatrix}
> -2\\
> 2\\
> 1
> \end{pmatrix}.
> $$
>
> Así,
>
> $$
> \boxed{
> (\Phi_2\circ\Phi_1)^{-1}(x')
> =
> Lx'
> +
> \begin{pmatrix}
> -2\\
> 2\\
> 1
> \end{pmatrix}.
> }
> $$
>
> Aplicando esta fórmula a
>
> $$
> x'
> =
> \begin{pmatrix}
> 0\\
> 6\\
> 4
> \end{pmatrix},
> $$
>
> obtenemos
>
> $$
> Lx'
> =
> \begin{pmatrix}
> 6\\
> 0\\
> 4
> \end{pmatrix},
> $$
>
> y finalmente
>
> $$
> \boxed{
> x
> =
> \begin{pmatrix}
> 4\\
> 2\\
> 5
> \end{pmatrix}.
> }
> $$

### 12.26. Síntesis geométrica

Un marco afín

$$
F=(O,B)
$$

contiene dos elecciones conceptualmente distintas:

$$
\boxed{
\text{un origen }O
\quad+\quad
\text{una base }B.
}
$$

Cambiar el origen produce una traslación de las coordenadas de puntos.
Cambiar la base produce una transformación lineal de componentes.
Cambiar ambas cosas produce una ley afín:

$$
\boxed{
x_{F'}(P)
=
S^{-1}
\left(
x_F(P)-[a]_B
\right).
}
$$

Para los desplazamientos, la parte traslacional desaparece:

$$
\boxed{
[\overrightarrow{PQ}]_{B'}
=
S^{-1}
[\overrightarrow{PQ}]_B.
}
$$

Por eso un punto y un vector no pueden obedecer exactamente la misma ley de transformación.

### 12.27. Del marco geométrico al marco físico

Nada de lo desarrollado en §12 introduce todavía:

- un reloj;
- una variable temporal;
- un observador;
- una trayectoria;
- una velocidad;
- una aceleración;
- una hipótesis de inercialidad.

Un marco afín geométrico especifica únicamente **cómo localizar espacialmente puntos y expresar desplazamientos**.
La física exige estructura adicional.
Esta frontera es decisiva:

$$
\boxed{
\text{marco geométrico}
\ne
\text{marco físico de referencia}.
}
$$

La próxima sección incorporará exactamente esa capa conceptual, sin adelantar todavía la dinámica newtoniana.

### 12.28. Cierre de §12

La sección ha unificado todos los cambios geométricos de descripción construidos desde §1.
Para dos marcos

$$
F=(O,B),
\qquad
F'=(O',B'),
$$

con

$$
a=\overrightarrow{OO'},
\qquad
S=S_{B\leftarrow B'},
$$

la ley fundamental es

$$
\boxed{
x_{F'}(P)
=
S^{-1}
\left(
x_F(P)-[a]_B
\right).
}
$$

Su forma coordenada equivalente es

$$
\boxed{
\Phi(x)=Lx+t.
}
$$

La composición satisface

$$
\boxed{
(L_2,t_2)\circ(L_1,t_1)
=
(L_2L_1,\ L_2t_1+t_2),
}
$$

y la inversa,

$$
\boxed{
(L,t)^{-1}
=
(L^{-1},-L^{-1}t).
}
$$

La parte traslacional sólo afecta coordenadas de puntos; las diferencias entre puntos y los vectores de desplazamiento transforman linealmente.
Los ejercicios E024–E025 aplican estas leyes antes de pasar de la geometría del marco a su realización física.
El siguiente paso será:

$$
\boxed{
\text{§13 — Del sistema de coordenadas al marco físico de referencia}
}
$$

---

[]{#fispm-t1-c04-s13}

[]{#fpm-i-04-s13}

## §13 — Del sistema de coordenadas al marco físico de referencia

### 13.1. Un sistema de coordenadas no basta

Un marco geométrico

$$
F=(O,B)
$$

permite asignar a cada punto $P$ una columna

$$
x_F(P).
$$

Esa construcción responde a una pregunta matemática:

$$
\boxed{
\text{¿cómo describimos un punto mediante números una vez elegidos origen y base?}
}
$$

Pero un experimento físico exige algo más.
Para localizar de manera reproducible una ocurrencia física necesitamos saber, al menos:

- dónde está materializado el origen;
- cómo se realizan las direcciones de referencia;
- qué patrón convierte longitudes en valores medidos;
- qué procedimiento asigna una lectura temporal.

Por tanto,

$$
\boxed{
\text{sistema geométrico de coordenadas}
\ne
\text{marco físico de referencia}.
}
$$

### 13.2. De una elección matemática a un procedimiento de medición

En geometría podemos elegir formalmente un punto

$$
O\in\mathcal E
$$

y una base

$$
B=(e_1,e_2,e_3)
$$

sin preguntar cómo se construirían físicamente.
En una situación experimental, en cambio, palabras como “origen”, “eje $x$” o “un metro” deben corresponder a procedimientos reproducibles.
La referencia física requiere entonces dos capas:

$$
\boxed{
\text{estructura geométrica}
+
\text{realización operacional}.
}
$$

La primera indica qué objetos matemáticos usamos.
La segunda indica cómo se vinculan esos objetos con marcas, instrumentos y lecturas físicas.

### 13.3. Definir: marco físico de referencia en sentido mínimo

> **FPM-I-04-D38 — Marco físico de referencia, nivel operacional mínimo**
> En el nivel de este capítulo, un **marco físico de referencia** es una realización operacional
>
> $$
> \boxed{
> \mathfrak R=(F,\mathcal L,\mathcal T,\mathcal O),
> }
> $$
>
> donde:
>
> 1. $F=(O,B)$ es un marco espacial afín;
> 2. $\mathcal L$ es un convenio de **calibración de longitudes**, que fija cómo las longitudes geométricas se expresan mediante una unidad física;
> 3. $\mathcal T$ es un convenio de **lectura temporal**, que asigna una lectura escalar $t$ mediante un reloj o procedimiento equivalente;
> 4. $\mathcal O$ representa la **realización física reproducible** del origen, las direcciones de referencia y los instrumentos asociados.[^kleppner-standards]

Esta definición es deliberadamente mínima.
No afirma que el marco sea inercial.
No afirma que el origen esté en reposo respecto de otro marco.
No introduce todavía una ley de movimiento.

### 13.4. El origen y los ejes deben estar físicamente realizables

En un dibujo podemos señalar arbitrariamente un punto como origen.
En un laboratorio necesitamos una referencia reproducible que permita reconocer qué ubicación corresponde a

$$
O.
$$

Del mismo modo, las direcciones de la base

$$
B=(e_1,e_2,e_3)
$$

deben estar asociadas a direcciones físicamente identificables.
Esto no significa que los vectores de base sean objetos materiales.
Significa que existe un procedimiento para reproducir las direcciones que esos vectores representan.
En un marco cartesiano físico se escogerá típicamente una base ortonormal

$$
E=(e_1,e_2,e_3),
$$

porque entonces las componentes corresponden directamente a proyecciones métricas sobre ejes mutuamente perpendiculares.

### 13.5. El patrón de longitud pertenece al procedimiento físico

La geometría euclídea determina una longitud abstracta

$$
\|v\|.
$$

Una medición física exige además declarar una unidad.
El convenio

$$
\mathcal L
$$

vincula la longitud geométrica con un valor numérico expresado, por ejemplo, en metros, centímetros u otra unidad convenida.
Cambiar la unidad no cambia el vector geométrico ni el punto.
Sólo cambia el número utilizado para comunicar la misma magnitud física.
Por tanto debemos separar:

$$
\boxed{
\text{cambio de unidad}
\ne
\text{cambio de origen}
\ne
\text{cambio de base}.
}
$$

Estas tres operaciones modifican descripciones numéricas por razones conceptualmente diferentes.

### 13.6. El convenio temporal: una lectura, todavía no una cinemática

Para distinguir mediciones realizadas en ocasiones diferentes necesitamos una etiqueta temporal.
En este capítulo representaremos esa lectura simplemente por

$$
t\in\mathbb R.
$$

El símbolo $t$ significa aquí únicamente:

$$
\boxed{
\text{lectura asignada por el convenio temporal }\mathcal T.
}
$$

No suponemos todavía una trayectoria

$$
P(t),
$$

ni definimos expresiones como

$$
\frac{dP}{dt}.
$$

Tampoco introducimos velocidad o aceleración.
Esas estructuras pertenecen al desarrollo posterior sobre tiempo y movimiento.

### 13.7. Definir: registro físico de localización

> **FPM-I-04-D39 — Registro de localización en un marco físico**
> Dada una ocurrencia física localizada espacialmente en un punto $P$ y una lectura temporal $t$, su registro en el marco
>
> $$
> \mathfrak R=(F,\mathcal L,\mathcal T,\mathcal O)
> $$
>
> es el par
>
> $$
> \boxed{
> \mathcal R_{\mathfrak R}(P,t)
> :=
> \left(
> t,\,
> x_F(P)
> \right),
> }
> $$
>
> acompañado de las unidades determinadas por $\mathcal L$.

Este par es un **registro de medición**.
No estamos construyendo todavía un espacio-tiempo ni identificando una ocurrencia física con un vector de dimensión cuatro.
La notación sólo conserva juntas dos informaciones:

- una lectura temporal;
- una localización espacial.

### 13.8. Proposición: cambio espacial bajo un convenio temporal común

> **FPM-I-04-P57 — Registro de una misma ocurrencia en dos marcos con tiempo común**
> Sean dos marcos físicos
>
> $$
> \mathfrak R=(F,\mathcal L,\mathcal T,\mathcal O),
> \qquad
> \mathfrak R'=(F',\mathcal L,\mathcal T,\mathcal O'),
> $$
>
> que utilizan el mismo convenio temporal y la misma calibración de longitud.
>
> Si
>
> $$
> F=(O,B),
> \qquad
> F'=(O',B'),
> $$
>
> con
>
> $$
> a=\overrightarrow{OO'},
> \qquad
> S=S_{B\leftarrow B'},
> $$
>
> entonces una misma ocurrencia registrada como
>
> $$
> \left(
> t,\,
> x_F(P)
> \right)
> $$
>
> en $\mathfrak R$ se registra en $\mathfrak R'$ como
>
> $$
> \boxed{
> \left(
> t,\,
> S^{-1}
> \left(
> x_F(P)-[a]_B
> \right)
> \right).
> }
> $$

**Demostración.** Por hipótesis, ambos marcos asignan la misma lectura temporal

$$
t.
$$

La parte espacial obedece exactamente a P51:

$$
x_{F'}(P)
=
S^{-1}
\left(
x_F(P)-[a]_B
\right).
$$

Por tanto,

$$
\mathcal R_{\mathfrak R'}(P,t)
=
\left(
t,\,
S^{-1}
\left(
x_F(P)-[a]_B
\right)
\right).
$$

$\square$

El resultado no contiene ninguna afirmación sobre movimiento relativo: sólo compara dos procedimientos de descripción espacial que comparten la misma lectura temporal.

### 13.9. Tres niveles que no deben confundirse

Conviene distinguir explícitamente:

#### Nivel 1 — Geometría

$$
F=(O,B).
$$

Es una elección matemática de origen y base.

#### Nivel 2 — Medición espacial

$$
(F,\mathcal L,\mathcal O).
$$

El origen, los ejes y la unidad de longitud tienen una realización operacional.

#### Nivel 3 — Marco físico mínimo

$$
\mathfrak R=(F,\mathcal L,\mathcal T,\mathcal O).
$$

Además de localizar espacialmente, el procedimiento asigna una lectura temporal.
Cada nivel añade estructura.
No es correcto atribuir al nivel anterior propiedades que sólo aparecen después.

### 13.10. No-ejemplos

> **Un dibujo con ejes no constituye por sí solo un marco físico**
> Dibujar tres ejes y escribir coordenadas produce una representación geométrica, pero no especifica cómo se materializan el origen, las direcciones, la unidad ni la lectura temporal.

> **Elegir metros no convierte un sistema de coordenadas en un marco físico completo**
> Una unidad de longitud aporta calibración espacial, pero todavía falta un procedimiento temporal y una realización física de las referencias.

> **Un marco físico no es automáticamente un marco inercial**
> La inercialidad es una propiedad ligada a las leyes de la dinámica. No puede deducirse de la ortogonalidad de los ejes, de la elección del origen ni de la existencia de un reloj.[^kleppner-inertial]

Este último error es especialmente importante:

$$
\boxed{
\text{sistema cartesiano}
\not\Rightarrow
\text{marco inercial}.
}
$$

### 13.11. Principio metodológico

> **FPM-I-04-MP25 — Declarar la realización física antes de interpretar coordenadas**
> Cuando una terna de coordenadas se use en física, identificar explícitamente:
>
> 1. qué punto realiza el origen;
> 2. qué direcciones realizan los ejes;
> 3. qué unidad calibra las longitudes;
> 4. qué procedimiento asigna la lectura temporal.
>
> Sólo después interpretar una columna como resultado de una localización física.

La matemática de coordenadas no sustituye la especificación del procedimiento de medición.

### 13.12. Balance: del marco geométrico a la realización operacional

Queda establecida la diferencia fundamental:

$$
\boxed{
F=(O,B)
}
$$

es un marco geométrico, mientras

$$
\boxed{
\mathfrak R=(F,\mathcal L,\mathcal T,\mathcal O)
}
$$

añade la estructura operacional necesaria para hablar de una referencia física.
El registro mínimo de una localización es

$$
\boxed{
\mathcal R_{\mathfrak R}(P,t)
=
\left(
t,\,
x_F(P)
\right).
}
$$

Si dos marcos comparten calibración y convenio temporal, la lectura $t$ permanece igual y sólo cambia la descripción espacial según la ley afín de §12.
Todavía falta precisar qué significa comparar observaciones realizadas desde marcos físicos distintos y por qué ninguna de estas estructuras permite decidir, por sí sola, si un marco es inercial.

### 13.13. Definir: observador asociado a un marco

> **FPM-I-04-D40 — Observador asociado a un marco físico**
> En el nivel de este capítulo, un **observador asociado a**
>
> $$
> \mathfrak R=(F,\mathcal L,\mathcal T,\mathcal O)
> $$
>
> es el sistema operacional capaz de aplicar de manera reproducible los convenios de $\mathfrak R$ y producir registros
>
> $$
> \mathcal R_{\mathfrak R}(P,t).
> $$

La palabra “observador” no designa necesariamente una persona.
Puede representar un conjunto de instrumentos, marcas, reglas de calibración y procedimientos de lectura.
Tampoco identificaremos al observador con el origen $O$.
El origen es un elemento geométrico del marco espacial; el observador es quien —o aquello que— realiza el procedimiento completo de referencia.

### 13.14. Una misma ocurrencia puede tener registros numéricos distintos

Supongamos que dos observadores usan marcos

$$
\mathfrak R
$$

y

$$
\mathfrak R'
$$

que comparten el convenio temporal y la calibración de longitud.
La misma ocurrencia física localizada en $P$ con lectura $t$ puede producir:

$$
\mathcal R_{\mathfrak R}(P,t)
=
\left(
t,\,
x_F(P)
\right),
$$

y

$$
\mathcal R_{\mathfrak R'}(P,t)
=
\left(
t,\,
x_{F'}(P)
\right).
$$

En general,

$$
x_F(P)
\ne
x_{F'}(P).
$$

Eso no significa que los observadores estén describiendo dos puntos distintos.
Significa que el mismo punto recibe etiquetas espaciales diferentes porque cambió el marco utilizado para localizarlo.

### 13.15. Proposición: acuerdo métrico entre observadores ortonormales

> **FPM-I-04-P58 — Invariancia de la separación espacial registrada**
> Sean dos observadores asociados a marcos físicos
>
> $$
> \mathfrak R=(F,\mathcal L,\mathcal T,\mathcal O),
> \qquad
> \mathfrak R'=(F',\mathcal L,\mathcal T,\mathcal O'),
> $$
>
> con la misma calibración de longitud y el mismo convenio temporal.
>
> Supongamos que
>
> $$
> F=(O,E),
> \qquad
> F'=(O',E')
> $$
>
> utilizan bases ortonormales.
>
> Si dos ocurrencias espaciales $P$ y $Q$ reciben la misma lectura temporal $t$, entonces
>
> $$
> \boxed{
> \left\|
> x_{F'}(Q)-x_{F'}(P)
> \right\|
> =
> \left\|
> x_F(Q)-x_F(P)
> \right\|.
> }
> $$

**Demostración.** La hipótesis temporal sólo asegura que estamos comparando los dos registros bajo el mismo convenio de lectura.
La parte espacial es exactamente P56:

$$
\left\|
x_{F'}(Q)-x_{F'}(P)
\right\|
=
\left\|
x_F(Q)-x_F(P)
\right\|.
$$

Como ambos observadores comparten además la calibración $\mathcal L$, ambas normas representan la misma longitud física expresada en la misma unidad. $\square$
Por tanto, dos observadores pueden discrepar en las columnas de coordenadas y, sin embargo, coincidir en una magnitud geométrica medible.

### 13.16. Desacuerdo de coordenadas no es desacuerdo físico

Consideremos, por ejemplo,

$$
x_F(P)
=
\begin{pmatrix}
4\\
1\\
0
\end{pmatrix},
$$

mientras otro marco asigna

$$
x_{F'}(P)
=
\begin{pmatrix}
-1\\
3\\
0
\end{pmatrix}.
$$

Las columnas son distintas.
Sin información adicional, no podemos concluir que se trate de puntos distintos.
Debemos preguntar primero cuál es la transformación de marco que relaciona ambas descripciones.
La comparación físicamente significativa exige reconstruir los objetos geométricos o sus invariantes, no comparar números aislados.

### 13.17. El observador no tiene por qué estar “sentado en el origen”

En ejemplos elementales se dibuja con frecuencia una persona junto al origen de coordenadas.
Ese dibujo puede ser útil, pero no constituye una definición.
El marco puede estar realizado mediante una red de marcas y dispositivos distribuidos.
Lo esencial es que exista un procedimiento reproducible para producir

$$
\left(
t,\,
x_F(P)
\right).
$$

Por eso distinguimos:

$$
\boxed{
\text{observador}
\ne
\text{origen geométrico}.
}
$$

El origen forma parte de la descripción espacial; el observador implementa el sistema de referencia completo.

### 13.18. Todavía no hemos definido un marco “en movimiento”

Para afirmar que un marco cambia respecto de otro a medida que transcurre el tiempo necesitaríamos permitir que sus datos espaciales dependieran de la lectura temporal.
Por ejemplo, aparecerían objetos del tipo

$$
O(t)
$$

o

$$
B(t).
$$

Pero introducir esas dependencias equivaldría a comenzar el estudio del movimiento.
En este capítulo no lo haremos.
Los cambios de marco tratados hasta ahora relacionan descripciones geométricas ya dadas; no constituyen todavía una teoría de marcos móviles.

### 13.19. Por qué la inercialidad no puede leerse de la geometría

Un marco puede poseer:

- origen bien definido;
- ejes ortonormales;
- patrón de longitud;
- reloj;
- procedimiento reproducible de localización.

Nada de eso decide por sí solo si el marco es **inercial**.
La palabra “inercial” exige comparar la descripción del movimiento con leyes dinámicas que todavía no se han introducido.
Por tanto, en este punto sólo podemos afirmar:

$$
\boxed{
\text{marco físico bien definido}
\not\Rightarrow
\text{marco inercial}.
}
$$

La ortogonalidad de los ejes es una propiedad geométrica.
La inercialidad es una propiedad físico-dinámica.
Confundirlas mezcla niveles de estructura diferentes.

### 13.20. Falsos criterios de inercialidad

> **“Los ejes son cartesianos, por tanto el marco es inercial.”**
>
> Falso. La geometría cartesiana no determina las leyes del movimiento observadas desde ese marco.

> **“El origen está materializado por un objeto físico, por tanto el marco es inercial.”**
>
> Falso. Tener un origen realizable no especifica cómo se comporta ese origen en el tiempo.

> **“Hay un reloj, por tanto podemos decidir si el marco es inercial.”**
>
> Falso. Un reloj permite asignar lecturas temporales; la inercialidad requiere estructura dinámica adicional.

### 13.21. Principio metodológico

> **FPM-I-04-MP26 — Separar diferencias de descripción de diferencias físicas**
> Cuando dos observadores asignen registros distintos a una misma situación:
>
> 1. identificar primero sus marcos geométricos;
> 2. comprobar sus convenios de unidades y lectura temporal;
> 3. transformar las coordenadas a una descripción común;
> 4. comparar después los invariantes o magnitudes físicas pertinentes.
>
> No interpretar una diferencia entre columnas numéricas como una diferencia física antes de controlar el marco y las convenciones.

### 13.22. Balance: observador, registro e inercialidad

Un observador queda entendido aquí como la realización operacional de un marco físico, no como un punto geométrico ni necesariamente como una persona.
Dos observadores pueden asignar coordenadas diferentes a una misma ocurrencia:

$$
\boxed{
x_F(P)\ne x_{F'}(P)
}
$$

sin discrepar sobre invariantes geométricos como una separación espacial, siempre que sus calibraciones sean compatibles.
Además,

$$
\boxed{
\text{observador}
\ne
\text{origen}
}
$$

y

$$
\boxed{
\text{marco físico}
\not\Rightarrow
\text{marco inercial}.
}
$$

Todavía falta ejercitar estas distinciones y cerrar la sección sin invadir el estudio del movimiento.

### 13.23. Qué puede inferirse de un registro y qué no

Un registro

$$
\left(
t,\,
x_F(P)
\right)
$$

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

### 13.24. Principio metodológico de nivel de estructura

> **FPM-I-04-MP27 — Declarar el nivel de estructura antes de inferir física**
> Antes de extraer una conclusión, identificar qué estructura está realmente disponible:
>
> 1. **coordenadas geométricas:** origen y base;
> 2. **marco físico mínimo:** geometría + calibración + lectura temporal + realización operacional;
> 3. **cinemática:** dependencia temporal de posiciones;
> 4. **dinámica:** leyes que relacionan movimiento e interacciones.
>
> No atribuir a un nivel propiedades que requieren uno posterior.

En particular,

$$
\boxed{
\text{tener }(t,x_F(P))
\not\Rightarrow
\text{tener una ley de movimiento}.
}
$$

[]{#fispm-t1-c04-e0026}

### 13.25. Ejercicio FPM-I-04-E026 — ¿Qué estructura está realmente dada?

> **Función pedagógica:** `Diagnóstico conceptual → Jerarquía de estructura → Control de inferencias`
>
> Para cada afirmación, indica qué puede concluirse y qué no.
>
> **Caso A.** Se da un origen $O$ y una base ortonormal $E$.
>
> **Caso B.** Además se especifica una unidad de longitud y un reloj.
>
> **Caso C.** Además existe un procedimiento reproducible que materializa el origen, los ejes y las lecturas.
>
> **Caso D.** Se afirma que, como los ejes son ortonormales, el marco es inercial.

> **Solución desarrollada**
>
> **Caso A.** Tenemos un marco geométrico
>
> $$
> F=(O,E).
> $$
>
> Podemos asignar coordenadas espaciales a puntos. No tenemos todavía un marco físico completo.
>
> **Caso B.** Ahora existen una calibración de longitud y una lectura temporal, pero falta especificar cómo se realizan físicamente el origen y las direcciones. La estructura operacional sigue incompleta.
>
> **Caso C.** Ya disponemos del nivel mínimo de marco físico:
>
> $$
> \mathfrak R=(F,\mathcal L,\mathcal T,\mathcal O).
> $$
>
> Podemos producir registros
>
> $$
> \left(
> t,\,
> x_F(P)
> \right).
> $$
>
> Sin embargo, aún no hemos definido trayectorias, velocidades, aceleraciones ni inercialidad.
>
> **Caso D.** La inferencia es inválida.
>
> $$
> \boxed{
> E\text{ ortonormal}
> \not\Rightarrow
> \mathfrak R\text{ inercial}.
> }
> $$
>
> La ortonormalidad pertenece a la geometría; la inercialidad requiere dinámica.

[]{#fispm-t1-c04-e0027}

### 13.26. Ejercicio FPM-I-04-E027 — Dos observadores, una misma geometría

> **Función pedagógica:** `Cambio de marco → Registros distintos → Invariante común`
>
> Dos observadores comparten la misma calibración de longitud y el mismo convenio temporal.
>
> El primero usa
>
> $$
> F=(O,E),
> \qquad
> E=(e_1,e_2,e_3).
> $$
>
> El segundo usa
>
> $$
> F'=(O',E'),
> $$
>
> con
>
> $$
> \overrightarrow{OO'}
> =
> e_1-2e_2+e_3
> $$
>
> y
>
> $$
> E'
> =
> (e_2,-e_1,e_3).
> $$
>
> A la lectura
>
> $$
> t=12\,\mathrm{s},
> $$
>
> se registran dos localizaciones $P$ y $Q$:
>
> $$
> x_F(P)
> =
> \begin{pmatrix}
> 5\\
> 0\\
> 2
> \end{pmatrix}
> \mathrm{m},
> \qquad
> x_F(Q)
> =
> \begin{pmatrix}
> 2\\
> 4\\
> 2
> \end{pmatrix}
> \mathrm{m}.
> $$
>
> 1. Calcula los registros espaciales de $P$ y $Q$ en $F'$.
> 2. Comprueba que las columnas cambian.
> 3. Calcula la separación espacial en ambos marcos.
> 4. Explica qué puede concluirse y qué no puede concluirse sobre el movimiento.

> **Solución desarrollada**
>
> La matriz de cambio es
>
> $$
> S_{E\leftarrow E'}
> =
> \begin{pmatrix}
> 0&-1&0\\
> 1&0&0\\
> 0&0&1
> \end{pmatrix},
> $$
>
> por lo que
>
> $$
> S^{-1}
> =
> \begin{pmatrix}
> 0&1&0\\
> -1&0&0\\
> 0&0&1
> \end{pmatrix}.
> $$
>
> Además,
>
> $$
> [a]_E
> =
> \begin{pmatrix}
> 1\\
> -2\\
> 1
> \end{pmatrix}
> \mathrm{m}.
> $$
>
> Para $P$:
>
> $$
> x_F(P)-[a]_E
> =
> \begin{pmatrix}
> 4\\
> 2\\
> 1
> \end{pmatrix}
> \mathrm{m},
> $$
>
> y por P57,
>
> $$
> \boxed{
> x_{F'}(P)
> =
> \begin{pmatrix}
> 2\\
> -4\\
> 1
> \end{pmatrix}
> \mathrm{m}.
> }
> $$
>
> Para $Q$:
>
> $$
> x_F(Q)-[a]_E
> =
> \begin{pmatrix}
> 1\\
> 6\\
> 1
> \end{pmatrix}
> \mathrm{m},
> $$
>
> de modo que
>
> $$
> \boxed{
> x_{F'}(Q)
> =
> \begin{pmatrix}
> 6\\
> -1\\
> 1
> \end{pmatrix}
> \mathrm{m}.
> }
> $$
>
> Los registros espaciales son numéricamente distintos en los dos marcos.
>
> En $F$,
>
> $$
> x_F(Q)-x_F(P)
> =
> \begin{pmatrix}
> -3\\
> 4\\
> 0
> \end{pmatrix}
> \mathrm{m},
> $$
>
> por lo que
>
> $$
> \left\|
> x_F(Q)-x_F(P)
> \right\|
> =
> 5\,\mathrm{m}.
> $$
>
> En $F'$,
>
> $$
> x_{F'}(Q)-x_{F'}(P)
> =
> \begin{pmatrix}
> 4\\
> 3\\
> 0
> \end{pmatrix}
> \mathrm{m},
> $$
>
> y
>
> $$
> \left\|
> x_{F'}(Q)-x_{F'}(P)
> \right\|
> =
> 5\,\mathrm{m}.
> $$
>
> Así,
>
> $$
> \boxed{
> \text{coordenadas distintas}
> \quad\text{pero}\quad
> \text{misma separación física}.
> }
> $$
>
> Como sólo disponemos de registros correspondientes a una lectura temporal común, no podemos concluir si $P$ o $Q$ se mueven, ni definir velocidades o aceleraciones.

### 13.27. Síntesis operacional

La arquitectura conceptual de la sección puede resumirse como una cadena de estructura creciente:

$$
\boxed{
\text{geometría}
\longrightarrow
\text{medición espacial}
\longrightarrow
\text{marco físico mínimo}.
}
$$

En símbolos,

$$
F=(O,B)
$$

se amplía a

$$
\mathfrak R=(F,\mathcal L,\mathcal T,\mathcal O).
$$

El marco físico permite producir registros

$$
\boxed{
\left(
t,\,
x_F(P)
\right).
}
$$

Un observador es el sistema operacional capaz de producirlos.
Dos observadores pueden asignar coordenadas distintas sin desacuerdo físico, siempre que las cantidades comparadas se transformen correctamente y se atienda a los invariantes relevantes.

### 13.28. Cierre de §13

La sección ha mostrado por qué una terna de números no basta para constituir una referencia física.
Un marco físico mínimo requiere:

$$
\boxed{
\text{origen y ejes}
+
\text{calibración espacial}
+
\text{lectura temporal}
+
\text{realización operacional}.
}
$$

La misma ocurrencia puede recibir registros diferentes:

$$
\left(
t,\,
x_F(P)
\right)
$$

y

$$
\left(
t,\,
x_{F'}(P)
\right),
$$

sin que cambie el punto geométrico descrito.
Cuando los marcos espaciales son ortonormales y las calibraciones compatibles, las separaciones geométricas permanecen invariantes.
Finalmente, quedan bloqueadas dos inferencias:

$$
\boxed{
\text{registro temporal}
\not\Rightarrow
\text{movimiento}
}
$$

y

$$
\boxed{
\text{marco físico}
\not\Rightarrow
\text{marco inercial}.
}
$$

Los ejercicios E026–E027 obligan a separar explícitamente geometría, realización operacional, observador e inercialidad.
La última sección del capítulo integrará todas las distinciones construidas —puntos, vectores, coordenadas, bases, orientación, isometrías y marcos— antes de entregar el concepto de posición dependiente del tiempo a FPM-I-05.
El siguiente paso será:

$$
\boxed{
\text{§14 — Integración: una geometría, varias descripciones}
}
$$

[^kleppner-standards]: D. Kleppner y R. J. Kolenkow, *An Introduction to Mechanics*, 2.ª ed., Cambridge University Press, 2010, cap. 2, §2.7 «Base Units and Physical Standards», p. 59 y ss.

[^kleppner-inertial]: D. Kleppner y R. J. Kolenkow, *An Introduction to Mechanics*, 2.ª ed., Cambridge University Press, 2010, cap. 2, §2.4 «Newton’s First Law and Inertial Systems», p. 51 y ss.; véase también el ejemplo 2.1 del mismo capítulo.

---

[]{#fispm-t1-c04-s14}

[]{#fpm-i-04-s14}

## §14 — Integración: una geometría, varias descripciones

### 14.1. Una geometría, varias descripciones

A lo largo del capítulo hemos repetido una misma operación conceptual:

1. identificar un objeto geométrico;
2. elegir una descripción;
3. traducir el objeto a números;
4. cambiar la descripción;
5. reconstruir el mismo objeto.

El principio rector puede escribirse como

$$
\boxed{
\text{objeto geométrico}
\ne
\text{representación numérica}.
}
$$

Un punto no es su terna de coordenadas.
Un vector no es su columna de componentes.
Una transformación lineal no es una única matriz.
Un marco físico no es un dibujo con ejes.
La descripción depende de elecciones; el objeto descrito no queda creado por esas elecciones.

### 14.2. La jerarquía construida desde §1

El capítulo ha introducido una cadena de estructuras:

$$
\boxed{
\mathcal E
\longrightarrow
V
\longrightarrow
\text{estructura euclídea}
\longrightarrow
\text{marcos}
\longrightarrow
\text{registros físicos}.
}
$$

Más explícitamente:

- $\mathcal E$: puntos del espacio afín;
- $V$: vectores de desplazamiento;
- $\langle\cdot,\cdot\rangle$: producto escalar;
- orientación: elección adicional en dimensión tres;
- $F=(O,B)$: marco geométrico;
- $\mathfrak R=(F,\mathcal L,\mathcal T,\mathcal O)$: marco físico mínimo.

Cada nivel añade estructura.
Ningún nivel debe confundirse con la representación coordenada usada para describirlo.

### 14.3. Definir: invariante de descripción

> **FPM-I-04-D41 — Invariante bajo cambio de descripción**
> Una cantidad asociada a una configuración geométrica será llamada **invariante de descripción** si su valor no cambia cuando modificamos únicamente el marco o la base usados para describir esa misma configuración, manteniendo fija la estructura geométrica pertinente.

La palabra “invariante” exige declarar **respecto de qué cambios**.
Por ejemplo, entre marcos ortonormales compatibles, la distancia entre dos puntos satisface

$$
\boxed{
d(P,Q)
=
\left\|
x_F(Q)-x_F(P)
\right\|
=
\left\|
x_{F'}(Q)-x_{F'}(P)
\right\|.
}
$$

Las coordenadas cambian; la distancia no.

### 14.4. No todo lo que cambia deja de ser geométricamente válido

Supongamos que

$$
[v]_B
\ne
[v]_{B'}.
$$

No hay contradicción.
Las dos columnas representan el mismo vector siempre que estén relacionadas por

$$
[v]_{B'}
=
S_{B\leftarrow B'}^{-1}[v]_B.
$$

Del mismo modo,

$$
x_F(P)
\ne
x_{F'}(P)
$$

puede describir un único punto $P$ cuando

$$
x_{F'}(P)
=
S^{-1}
\left(
x_F(P)-[a]_B
\right).
$$

Por tanto, una representación puede cambiar de manera sistemática sin que cambie el objeto geométrico.

### 14.5. Definir: ley covariante de representación

> **FPM-I-04-D42 — Ley covariante de representación**
> En esta sección usaremos **covariante** en un sentido local y operativo:
>
> una familia de representaciones es covariante respecto de un cambio de descripción cuando sus datos numéricos cambian según una ley de transformación compatible con el tipo de objeto y con la composición de cambios de marco o base.

Este uso no introduce todavía cálculo tensorial.
Significa simplemente que las representaciones no cambian arbitrariamente.
Cada tipo de objeto posee su propia ley:

#### Vector

$$
\boxed{
[v]_{B'}
=
S^{-1}[v]_B.
}
$$

#### Punto

$$
\boxed{
x_{F'}(P)
=
S^{-1}
\left(
x_F(P)-[a]_B
\right).
}
$$

#### Operador lineal

$$
\boxed{
A_{B'}(T)
=
S^{-1}A_B(T)S.
}
$$

Las tres fórmulas son diferentes porque describen objetos de tipos diferentes.

### 14.6. Composición como prueba de coherencia

Una ley de transformación no es sólo una receta para pasar de una descripción a otra.
Debe ser compatible con cambios sucesivos.
Para vectores,

$$
S_{B\leftarrow C}
=
S_{B\leftarrow B'}
S_{B'\leftarrow C}.
$$

Para cambios afines,

$$
(L_2,t_2)\circ(L_1,t_1)
=
(L_2L_1,\,
L_2t_1+t_2).
$$

Por tanto, pasar directamente o mediante una descripción intermedia debe producir el mismo resultado.
Esta consistencia es una de las señales de que estamos cambiando la representación de un mismo objeto y no introduciendo datos arbitrarios.

### 14.7. Proposición: reconstrucción independiente de la descripción

> **FPM-I-04-P59 — El objeto reconstruido no depende de la representación**
> 
> **(a) Vectores.** Sean $B$ y $B'$ dos bases de $V$. Si
>
> $$
> [v]_{B'}
> =
> S_{B\leftarrow B'}^{-1}[v]_B,
> $$
>
> entonces reconstruir el vector desde cualquiera de las dos columnas produce el mismo
>
> $$
> v\in V.
> $$
>
> **(b) Puntos.** Sean
>
> $$
> F=(O,B),
> \qquad
> F'=(O',B')
> $$
>
> dos marcos afines relacionados por
>
> $$
> a=\overrightarrow{OO'},
> \qquad
> S=S_{B\leftarrow B'}.
> $$
>
> Si
>
> $$
> x_{F'}(P)
> =
> S^{-1}
> \left(
> x_F(P)-[a]_B
> \right),
> $$
>
> entonces reconstruir el punto desde $F$ o desde $F'$ produce el mismo
>
> $$
> P\in\mathcal E.
> $$

**Demostración.**

#### Parte (a)

Escribamos

$$
[v]_B
=
\begin{pmatrix}
v^1\\
v^2\\
v^3
\end{pmatrix},
\qquad
[v]_{B'}
=
\begin{pmatrix}
v'^1\\
v'^2\\
v'^3
\end{pmatrix}.
$$

Por definición de componentes,

$$
v
=
v^1e_1+v^2e_2+v^3e_3.
$$

P39 establece que

$$
[v]_B
=
S_{B\leftarrow B'}[v]_{B'}.
$$

Pero las columnas de $S_{B\leftarrow B'}$ son precisamente

$$
[e'_1]_B,
\qquad
[e'_2]_B,
\qquad
[e'_3]_B.
$$

Por tanto,

$$
[v]_B
=
\left[
v'^1e'_1+v'^2e'_2+v'^3e'_3
\right]_B.
$$

La unicidad de componentes en $B$ implica

$$
v
=
v'^1e'_1+v'^2e'_2+v'^3e'_3.
$$

Ambas columnas reconstruyen el mismo vector.

#### Parte (b)

Desde el marco $F$,

$$
P
=
O+\overrightarrow{OP},
$$

con

$$
[\overrightarrow{OP}]_B
=
x_F(P).
$$

Desde $F'$,

$$
P
=
O'+\overrightarrow{O'P},
$$

con

$$
[\overrightarrow{O'P}]_{B'}
=
x_{F'}(P).
$$

P51 equivale a

$$
[\overrightarrow{O'P}]_{B'}
=
S^{-1}
\left(
[\overrightarrow{OP}]_B-[a]_B
\right).
$$

Por P39, esto significa geométricamente

$$
\overrightarrow{O'P}
=
\overrightarrow{OP}-a.
$$

Como

$$
O'=O+a,
$$

obtenemos

$$
O'+\overrightarrow{O'P}
=
O+a+\overrightarrow{OP}-a
=
O+\overrightarrow{OP}
=
P.
$$

$\square$

La proposición formaliza la idea central del capítulo:

$$
\boxed{
\text{cambiar la descripción no cambia el objeto}.
}
$$

### 14.8. Qué cambia y qué permanece

Podemos resumir los principales objetos así:

| Objeto | Representación dependiente de elección | Ley de cambio | Qué permanece |
|---|---|---|---|
| Punto $P$ | $x_F(P)$ | afín | el punto $P$ |
| Vector $v$ | $[v]_B$ | lineal | el vector $v$ |
| Desplazamiento $\overrightarrow{PQ}$ | $[\overrightarrow{PQ}]_B$ | lineal | el desplazamiento |
| Operador $T$ | $A_B(T)$ | conjugación | el operador $T$ |
| Distancia $d(P,Q)$ | cálculo desde coordenadas | compatible con la métrica | la distancia |
| Ángulo $\theta(u,v)$ | cálculo desde componentes | compatible con la métrica | el ángulo |

La última columna contiene objetos o cantidades geométricas.
Las columnas intermedias contienen representaciones.

### 14.9. Invariante no significa “mismo número en cualquier fórmula mal usada”

La invariancia no permite ignorar las leyes de transformación.
Por ejemplo, en una base no ortonormal la norma no se calcula, en general, mediante

$$
(v^1)^2+(v^2)^2+(v^3)^2.
$$

Debe emplearse la estructura métrica adecuada, representada por la matriz de Gram correspondiente.
Por tanto, el contenido correcto es:

$$
\boxed{
\text{la cantidad geométrica es invariante;}
\quad
\text{su fórmula coordenada puede depender de la descripción}.
}
$$

Este punto evita confundir invariancia geométrica con invariancia literal de una expresión numérica particular.

### 14.10. Principio metodológico

> **FPM-I-04-MP28 — Preguntar primero por el objeto, después por sus números**
> Ante una fórmula con coordenadas o matrices:
>
> 1. identificar el objeto geométrico representado;
> 2. identificar las elecciones de origen, base, orientación y unidades;
> 3. escribir la ley de transformación correcta para ese tipo de objeto;
> 4. distinguir qué datos cambian de representación y qué cantidades permanecen invariantes;
> 5. sólo entonces comparar números.

Este principio resume la disciplina conceptual desarrollada desde §1.

### 14.11. Balance: objeto, representación e invariancia

La síntesis inicial queda organizada por dos ideas complementarias.

#### Invariancia

$$
\boxed{
\text{el objeto o la cantidad geométrica pertinente permanece}.
}
$$

#### Covariancia de representación

$$
\boxed{
\text{los datos numéricos cambian mediante una ley coherente}.
}
$$

Así, “varias descripciones” no significa “varias geometrías”.
El mismo punto, vector, desplazamiento u operador puede aparecer mediante números diferentes sin perder identidad geométrica.
Todavía falta integrar estas ideas en situaciones completas y reconocer errores de tipo mediante los tres ejercicios finales E028–E030.

### 14.12. Invariantes métricos bajo marcos ortonormales

Sean

$$
F=(O,E),
\qquad
F'=(O',E')
$$

dos marcos con bases ortonormales.
Para dos puntos $P,Q$, P52 da

$$
[\overrightarrow{PQ}]_{E'}
=
S^{-1}
[\overrightarrow{PQ}]_E,
$$

y P56 ya estableció que, entre bases ortonormales,

$$
S^{\mathsf T}S=I,
\qquad
S^{-1}=S^{\mathsf T}.
$$

Por tanto $S^{-1}$ también es ortogonal y,

$$
\boxed{
d(P,Q)
=
\left\|
[\overrightarrow{PQ}]_E
\right\|
=
\left\|
[\overrightarrow{PQ}]_{E'}
\right\|.
}
$$

Del mismo modo, para dos vectores $u,v$,

$$
\boxed{
\langle u,v\rangle
=
[u]_E^{\mathsf T}[v]_E
=
[u]_{E'}^{\mathsf T}[v]_{E'}.
}
$$

En consecuencia, también permanece el ángulo:

$$
\boxed{
\theta(u,v)
=
\theta_E(u,v)
=
\theta_{E'}(u,v).
}
$$

Las columnas cambian; las relaciones métricas no.

### 14.13. La orientación requiere una capa adicional

La métrica por sí sola no distingue una base ortonormal positiva de una negativa.
Si

$$
S_{E\leftarrow E'}
$$

es ortogonal, entonces

$$
\det S=\pm1.
$$

El signo informa si el cambio de descripción conserva o invierte la orientación relativa de las bases.
Para una terna de vectores

$$
(u,v,w),
$$

el volumen geométrico no orientado satisface

$$
\boxed{
\left|
\operatorname{Vol}^{\mathrm{or}}(u,v,w)
\right|
}
$$

independientemente de la base ortonormal usada para calcularlo.
Pero el signo de un determinante coordenado sólo puede interpretarse después de declarar la orientación de la base de referencia.
Por tanto:

$$
\boxed{
\text{métrica}
\ne
\text{orientación}.
}
$$

Esta distinción explica por qué una reflexión puede conservar todas las distancias y, sin embargo, invertir orientación.

### 14.14. Triangulación y trilateración no son lo mismo

En problemas de localización se emplean dos familias de procedimientos que conviene distinguir.

#### Triangulación

Reconstruye una posición a partir de **direcciones o ángulos** medidos desde referencias conocidas.

#### Trilateración

Reconstruye una posición a partir de **distancias** a puntos de referencia conocidos.
En esta sección utilizaremos trilateración porque permite expresar la consistencia directamente mediante los invariantes métricos ya desarrollados.
No usaremos ambos términos como sinónimos.

### 14.15. Definir: datos métricos de localización

> **FPM-I-04-D43 — Datos de trilateración respecto de cuatro referencias**
> Sean
>
> $$
> A_0,A_1,A_2,A_3\in\mathcal E
> $$
>
> cuatro puntos afínmente independientes.
>
> Para un punto $P$, definimos sus datos métricos de localización por
>
> $$
> \boxed{
> \Lambda(P)
> :=
> \begin{pmatrix}
> d(P,A_0)^2\\
> d(P,A_1)^2\\
> d(P,A_2)^2\\
> d(P,A_3)^2
> \end{pmatrix}.
> }
> $$

La independencia afín significa que

$$
\overrightarrow{A_0A_1},
\qquad
\overrightarrow{A_0A_2},
\qquad
\overrightarrow{A_0A_3}
$$

forman una base de $V$.
Los datos $\Lambda(P)$ están formados por cantidades métricas, no por coordenadas del punto.

### 14.16. Proposición: cuatro distancias determinan un punto en dimensión tres

> **FPM-I-04-P60 — Unicidad de la trilateración en dimensión tres**
> Sean
>
> $$
> A_0,A_1,A_2,A_3
> $$
>
> cuatro puntos afínmente independientes.
>
> Si dos puntos $P,Q$ satisfacen
>
> $$
> \Lambda(P)=\Lambda(Q),
> $$
>
> entonces
>
> $$
> \boxed{
> P=Q.
> }
> $$

**Demostración.**
Tomamos

$$
O:=A_0,
$$

y definimos

$$
p:=\overrightarrow{OP},
\qquad
q:=\overrightarrow{OQ},
$$

$$
a_i:=\overrightarrow{OA_i},
\qquad
i=1,2,3.
$$

Como

$$
\Lambda(P)=\Lambda(Q),
$$

tenemos para cada $i$:

$$
d(P,A_i)^2-d(P,A_0)^2
=
d(Q,A_i)^2-d(Q,A_0)^2.
$$

Ahora,

$$
d(P,A_i)^2
=
\|p-a_i\|^2,
$$

y

$$
d(P,A_0)^2
=
\|p\|^2.
$$

Por tanto,

$$
\|p-a_i\|^2-\|p\|^2
=
\|q-a_i\|^2-\|q\|^2.
$$

Expandimos:

$$
\|p\|^2
-
2\langle p,a_i\rangle
+
\|a_i\|^2
-
\|p\|^2
$$

es igual a

$$
\|q\|^2
-
2\langle q,a_i\rangle
+
\|a_i\|^2
-
\|q\|^2.
$$

Luego,

$$
\langle p-q,a_i\rangle=0
$$

para

$$
i=1,2,3.
$$

Como los tres vectores

$$
a_1,a_2,a_3
$$

forman una base de $V$, el vector

$$
p-q
$$

es ortogonal a todo $V$.
En particular,

$$
\langle p-q,p-q\rangle=0.
$$

Por positividad del producto escalar,

$$
p-q=0.
$$

Así,

$$
p=q,
$$

y por tanto

$$
P=Q.
$$

$\square$

La proposición no afirma que cualquier cuádrupla de números positivos corresponda a un punto.
Afirma únicamente **unicidad** cuando un punto compatible con esos datos existe.

### 14.17. Consistencia de los datos bajo cambio de marco

Como cada entrada de

$$
\Lambda(P)
$$

es una distancia geométrica, un cambio entre marcos ortonormales no modifica el vector de datos:

$$
\boxed{
\Lambda_F(P)
=
\Lambda_{F'}(P).
}
$$

Lo que sí cambia es la columna coordenada del punto reconstruido:

$$
x_F(P)
\ne
x_{F'}(P)
$$

en general.
Pero P51 relaciona ambas columnas mediante

$$
x_{F'}(P)
=
S^{-1}
\left(
x_F(P)-[a]_B
\right).
$$

Así obtenemos dos niveles simultáneos:

$$
\boxed{
\text{datos métricos invariantes}
}
$$

y

$$
\boxed{
\text{coordenadas covariantes}.
}
$$

### 14.18. Proposición: la reconstrucción métrica es compatible con el cambio de marco

> **FPM-I-04-P61 — Consistencia de la trilateración entre marcos ortonormales**
> Sean
>
> $$
> A_0,A_1,A_2,A_3
> $$
>
> cuatro referencias afínmente independientes y sean $F,F'$ dos marcos ortonormales.
>
> Si un punto $P$ es compatible con los datos
>
> $$
> \Lambda(P),
> $$
>
> entonces la reconstrucción realizada en $F$ y la reconstrucción realizada en $F'$ corresponden al mismo punto geométrico.
>
> Sus columnas satisfacen
>
> $$
> \boxed{
> x_{F'}(P)
> =
> S^{-1}
> \left(
> x_F(P)-[a]_B
> \right).
> }
> $$

**Demostración.**
Las distancias que forman

$$
\Lambda(P)
$$

son invariantes entre $F$ y $F'$.
Por P60, existe a lo sumo un punto geométrico compatible con esos cuatro valores.
Por tanto, si ambos procedimientos reconstruyen un punto compatible, ambos deben reconstruir el mismo $P$.
Sus representaciones quedan entonces relacionadas por P51. $\square$
La consistencia entre observadores no requiere que produzcan la misma terna de coordenadas.
Requiere que sus ternas representen el mismo objeto y respeten la ley de transformación correspondiente.

### 14.19. Ejemplo exacto de localización por distancias

Tomemos una base ortonormal

$$
E=(e_1,e_2,e_3)
$$

y cuatro referencias:

$$
A_0=O,
$$

$$
A_1=O+e_1,
\qquad
A_2=O+e_2,
\qquad
A_3=O+e_3.
$$

Sea

$$
x_F(P)
=
\begin{pmatrix}
2\\
3\\
4
\end{pmatrix}.
$$

Entonces:

$$
d(P,A_0)^2
=
2^2+3^2+4^2
=
29,
$$

$$
d(P,A_1)^2
=
1^2+3^2+4^2
=
26,
$$

$$
d(P,A_2)^2
=
2^2+2^2+4^2
=
24,
$$

y

$$
d(P,A_3)^2
=
2^2+3^2+3^2
=
22.
$$

Así,

$$
\boxed{
\Lambda(P)
=
\begin{pmatrix}
29\\
26\\
24\\
22
\end{pmatrix}.
}
$$

Si otro marco ortonormal asigna a $P$ una columna diferente, estos cuatro valores permanecen exactamente iguales.

### 14.20. Cómo se recuperan las coordenadas en el ejemplo

En el ejemplo anterior, si

$$
x_F(P)
=
\begin{pmatrix}
x\\
y\\
z
\end{pmatrix},
$$

entonces

$$
d(P,A_0)^2
=
x^2+y^2+z^2.
$$

Restando la distancia a $A_1$:

$$
d(P,A_0)^2-d(P,A_1)^2
=
2x-1.
$$

Por tanto,

$$
x
=
\frac{
d(P,A_0)^2-d(P,A_1)^2+1
}{2}.
$$

Análogamente,

$$
y
=
\frac{
d(P,A_0)^2-d(P,A_2)^2+1
}{2},
$$

$$
z
=
\frac{
d(P,A_0)^2-d(P,A_3)^2+1
}{2}.
$$

Con los datos

$$
29,\ 26,\ 24,\ 22,
$$

obtenemos

$$
x=2,
\qquad
y=3,
\qquad
z=4.
$$

La reconstrucción coordenada depende del marco elegido.
El conjunto de distancias no.

### 14.21. Principio metodológico de consistencia entre observadores

> **FPM-I-04-MP29 — Comparar invariantes antes de comparar coordenadas**
> Cuando dos descripciones de una misma configuración parezcan incompatibles:
>
> 1. transformar primero ambas al mismo marco o reconstruir el objeto geométrico;
> 2. comparar distancias, ángulos u otros invariantes pertinentes;
> 3. verificar la ley covariante de las representaciones;
> 4. sólo entonces diagnosticar una discrepancia física o experimental.
>
> Dos columnas diferentes no constituyen por sí solas datos contradictorios.

### 14.22. Balance: reconstrucción e invariantes

La integración geométrica queda ahora organizada en tres niveles:

#### Objeto

$$
\boxed{
P,\ v,\ \overrightarrow{PQ},\ T
}
$$

#### Representación covariante

$$
\boxed{
x_F(P),\ [v]_B,\ [\overrightarrow{PQ}]_B,\ A_B(T)
}
$$

#### Invariantes

$$
\boxed{
d(P,Q),\ \|v\|,\ \langle u,v\rangle,\ \theta(u,v)
}
$$

y, cuando la orientación forma parte de la estructura, las cantidades orientadas deben interpretarse respecto de esa elección.
La reconstrucción por cuatro distancias muestra concretamente que distintos observadores pueden utilizar coordenadas diferentes y, sin embargo, recuperar una única posición geométrica compatible con los mismos datos métricos.
Todavía faltan los tres ejercicios integradores E028–E030 y la transición final hacia FPM-I-05.

[]{#fispm-t1-c04-e0028}

### 14.23. Ejercicio FPM-I-04-E028 — Un punto y un vector, dos descripciones

> **Función pedagógica:** `Tipos de objeto → Leyes distintas → Reconstrucción → Invariante`
>
> Sea
>
> $$
> F=(O,E),
> \qquad
> E=(e_1,e_2,e_3)
> $$
>
> un marco ortonormal positivo.
>
> Definimos
>
> $$
> F'=(O',E')
> $$
>
> mediante
>
> $$
> \overrightarrow{OO'}
> =
> e_1-2e_2+e_3
> $$
>
> y
>
> $$
> E'
> =
> (e_2,-e_1,e_3).
> $$
>
> Se dan
>
> $$
> x_F(P)
> =
> \begin{pmatrix}
> 5\\
> 0\\
> 2
> \end{pmatrix},
> \qquad
> [v]_E
> =
> \begin{pmatrix}
> 2\\
> -1\\
> 2
> \end{pmatrix}.
> $$
>
> 1. Calcula $x_{F'}(P)$.
> 2. Calcula $[v]_{E'}$.
> 3. Explica por qué el punto y el vector no obedecen la misma fórmula.
> 4. Reconstruye $P$ y $v$ desde los datos en $F'$.
> 5. Comprueba que $\|v\|$ es invariante.

> **Solución desarrollada**
>
> La matriz de cambio es
>
> $$
> S_{E\leftarrow E'}
> =
> \begin{pmatrix}
> 0&-1&0\\
> 1&0&0\\
> 0&0&1
> \end{pmatrix},
> $$
>
> por lo que
>
> $$
> S^{-1}
> =
> \begin{pmatrix}
> 0&1&0\\
> -1&0&0\\
> 0&0&1
> \end{pmatrix}.
> $$
>
> Además,
>
> $$
> [a]_E
> =
> \begin{pmatrix}
> 1\\
> -2\\
> 1
> \end{pmatrix}.
> $$
>
> Para el punto:
>
> $$
> x_{F'}(P)
> =
> S^{-1}
> \left(
> x_F(P)-[a]_E
> \right)
> =
> \boxed{
> \begin{pmatrix}
> 2\\
> -4\\
> 1
> \end{pmatrix}
> }.
> $$
>
> Para el vector no aparece traslación:
>
> $$
> [v]_{E'}
> =
> S^{-1}[v]_E
> =
> \boxed{
> \begin{pmatrix}
> -1\\
> -2\\
> 2
> \end{pmatrix}
> }.
> $$
>
> La diferencia entre ambas leyes proviene del tipo de objeto:
>
> $$
> \boxed{
> \text{punto}\to\text{ley afín},
> \qquad
> \text{vector}\to\text{ley lineal}.
> }
> $$
>
> Reconstruimos el desplazamiento desde $O'$:
>
> $$
> 2e'_1-4e'_2+e'_3
> =
> 2e_2+4e_1+e_3.
> $$
>
> Como
>
> $$
> O'=O+e_1-2e_2+e_3,
> $$
>
> obtenemos
>
> $$
> P
> =
> O'
> +
> 2e'_1-4e'_2+e'_3
> =
> O+5e_1+2e_3,
> $$
>
> que coincide con la reconstrucción desde
>
> $$
> x_F(P)=
> \begin{pmatrix}
> 5\\
> 0\\
> 2
> \end{pmatrix}.
> $$
>
> Para el vector,
>
> $$
> -e'_1-2e'_2+2e'_3
> =
> -e_2+2e_1+2e_3
> =
> v.
> $$
>
> Finalmente,
>
> $$
> \|v\|^2
> =
> 2^2+(-1)^2+2^2
> =
> 9,
> $$
>
> y
>
> $$
> \|[v]_{E'}\|^2
> =
> (-1)^2+(-2)^2+2^2
> =
> 9.
> $$
>
> Las representaciones cambian; el punto, el vector y la norma del vector permanecen.

[]{#fispm-t1-c04-e0029}

### 14.24. Ejercicio FPM-I-04-E029 — Trilateración en dos marcos

> **Función pedagógica:** `Datos invariantes → Coordenadas covariantes → Reconstrucción única`
>
> En un marco ortonormal
>
> $$
> F=(O,E)
> $$
>
> se toman las referencias
>
> $$
> A_0=O,
> $$
>
> $$
> A_1=O+e_1,
> \qquad
> A_2=O+e_2,
> \qquad
> A_3=O+e_3.
> $$
>
> Un punto $P$ tiene
>
> $$
> x_F(P)
> =
> \begin{pmatrix}
> 2\\
> 3\\
> 4
> \end{pmatrix},
> $$
>
> y por tanto
>
> $$
> \Lambda(P)
> =
> \begin{pmatrix}
> 29\\
> 26\\
> 24\\
> 22
> \end{pmatrix}.
> $$
>
> Considera ahora
>
> $$
> O'=O+e_1,
> $$
>
> $$
> E'=(e_2,-e_1,e_3).
> $$
>
> 1. Calcula las coordenadas de $P$ y de las cuatro referencias en $F'$.
> 2. Recalcula las cuatro distancias cuadradas usando únicamente las coordenadas en $F'$.
> 3. Explica por qué P60–P61 garantizan que ambos marcos reconstruyen el mismo punto.

> **Solución desarrollada**
>
> Tenemos
>
> $$
> S=
> \begin{pmatrix}
> 0&-1&0\\
> 1&0&0\\
> 0&0&1
> \end{pmatrix},
> \qquad
> S^{-1}
> =
> \begin{pmatrix}
> 0&1&0\\
> -1&0&0\\
> 0&0&1
> \end{pmatrix},
> $$
>
> y
>
> $$
> [a]_E
> =
> \begin{pmatrix}
> 1\\
> 0\\
> 0
> \end{pmatrix}.
> $$
>
> Para $P$:
>
> $$
> \boxed{
> x_{F'}(P)
> =
> \begin{pmatrix}
> 3\\
> -1\\
> 4
> \end{pmatrix}.
> }
> $$
>
> Las referencias quedan:
>
> $$
> x_{F'}(A_0)
> =
> \begin{pmatrix}
> 0\\
> 1\\
> 0
> \end{pmatrix},
> $$
>
> $$
> x_{F'}(A_1)
> =
> \begin{pmatrix}
> 0\\
> 0\\
> 0
> \end{pmatrix},
> $$
>
> $$
> x_{F'}(A_2)
> =
> \begin{pmatrix}
> 1\\
> 1\\
> 0
> \end{pmatrix},
> $$
>
> $$
> x_{F'}(A_3)
> =
> \begin{pmatrix}
> 0\\
> 1\\
> 1
> \end{pmatrix}.
> $$
>
> Entonces,
>
> $$
> x_{F'}(P)-x_{F'}(A_0)
> =
> \begin{pmatrix}
> 3\\
> -2\\
> 4
> \end{pmatrix},
> $$
>
> y
>
> $$
> d(P,A_0)^2
> =
> 3^2+(-2)^2+4^2
> =
> 29.
> $$
>
> Asimismo,
>
> $$
> d(P,A_1)^2
> =
> 3^2+(-1)^2+4^2
> =
> 26,
> $$
>
> $$
> d(P,A_2)^2
> =
> 2^2+(-2)^2+4^2
> =
> 24,
> $$
>
> y
>
> $$
> d(P,A_3)^2
> =
> 3^2+(-2)^2+3^2
> =
> 22.
> $$
>
> Por tanto,
>
> $$
> \boxed{
> \Lambda_{F'}(P)
> =
> \Lambda_F(P)
> =
> \begin{pmatrix}
> 29\\
> 26\\
> 24\\
> 22
> \end{pmatrix}.
> }
> $$
>
> P60 garantiza que esos cuatro datos son compatibles con a lo sumo un punto geométrico.
>
> P61 garantiza que las reconstrucciones en $F$ y $F'$ son representaciones del mismo $P$ y obedecen la ley afín de cambio de marco.

[]{#fispm-t1-c04-e0030}

### 14.25. Ejercicio FPM-I-04-E030 — Auditoría conceptual del capítulo

> **Función pedagógica:** `Integración global → Detección de falsos amigos → Preparación del capítulo siguiente`
>
> Decide si cada afirmación es correcta o incorrecta y justifica brevemente.
>
> 1. Si dos puntos tienen la misma terna numérica en marcos diferentes, representan necesariamente el mismo punto.
> 2. Un vector puede tener columnas distintas en dos bases sin cambiar como objeto geométrico.
> 3. Cambiar el origen modifica el desplazamiento $\overrightarrow{PQ}$.
> 4. Una matriz ortogonal representa necesariamente una transformación activa.
> 5. Una reflexión conserva distancias aunque invierta orientación.
> 6. Cuatro distancias a referencias afínmente independientes determinan a lo sumo un punto en dimensión tres.
> 7. Un marco físico dotado de reloj es automáticamente inercial.
> 8. Conocer un único registro $(t,x_F(P))$ basta para decidir si $P$ se mueve.
> 9. La invariancia de una cantidad significa que cualquier fórmula coordenada ingenua produce siempre el mismo número.
> 10. Para comenzar a estudiar movimiento será necesario añadir dependencia temporal a la posición.

> **Solución desarrollada**
>
> **1. Incorrecta.** La misma terna numérica puede representar puntos diferentes si cambian origen o base. Debe conocerse la relación entre marcos.
>
> **2. Correcta.** Las columnas obedecen
>
> $$
> [v]_{B'}
> =
> S^{-1}[v]_B,
> $$
>
> mientras $v$ permanece fijo.
>
> **3. Incorrecta.** El cambio de origen altera coordenadas de puntos, pero el desplazamiento entre dos puntos no depende del origen.
>
> **4. Incorrecta.** Una matriz ortogonal puede aparecer tanto en un cambio pasivo entre bases ortonormales como en la representación activa de una isometría.
>
> **5. Correcta.** Para una reflexión ortogonal,
>
> $$
> Q^{\mathsf T}Q=I,
> \qquad
> \det Q=-1.
> $$
>
> Conserva la métrica e invierte orientación.
>
> **6. Correcta.** Es exactamente P60, bajo la hipótesis de independencia afín de las referencias.
>
> **7. Incorrecta.** Un reloj aporta lectura temporal; la inercialidad requiere estructura dinámica adicional.
>
> **8. Incorrecta.** Un único registro sólo localiza una ocurrencia bajo ciertos convenios. No proporciona una ley de dependencia temporal.
>
> **9. Incorrecta.** La cantidad geométrica puede ser invariante mientras su fórmula coordenada cambia. En una base no ortonormal, por ejemplo, debe usarse la matriz de Gram correspondiente.
>
> **10. Correcta.** El paso siguiente consiste precisamente en permitir que la localización espacial dependa de la lectura temporal. Esa estructura pertenece a FPM-I-05 y no se desarrolla aquí.

### 14.26. La red conceptual completa del capítulo

FPM-I-04 puede condensarse en la siguiente cadena:

$$
\boxed{
\text{puntos}
\longrightarrow
\text{desplazamientos}
\longrightarrow
\text{vectores}
\longrightarrow
\text{métrica}
\longrightarrow
\text{orientación}
}
$$

seguida por

$$
\boxed{
\text{bases}
\longrightarrow
\text{coordenadas}
\longrightarrow
\text{cambios de descripción}
\longrightarrow
\text{marcos}
\longrightarrow
\text{registros físicos}.
}
$$

Cada flecha añade una capa de estructura o de representación.
Ninguna permite borrar las distinciones de tipo establecidas antes.

### 14.27. Lo que el capítulo deja establecido

Al cerrar FPM-I-04 disponemos de:

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

### 14.28. La puerta hacia FPM-I-05

Hasta aquí, un punto $P$ ha sido considerado como una localización geométrica fija dentro de cada problema.
El siguiente paso conceptual será permitir que la posición asignada a un cuerpo dependa de la lectura temporal.
Eso exigirá introducir una aplicación temporal del tipo

$$
t
\longmapsto
P(t),
$$

y estudiar su geometría.
FPM-I-04 no desarrolla todavía esa estructura.
Sólo deja preparado el lenguaje necesario para que, cuando aparezca una posición dependiente del tiempo, quede claro:

- qué es el punto geométrico;
- qué es su vector de posición relativo a un origen;
- qué son sus coordenadas;
- cómo cambian esas coordenadas al cambiar de marco;
- qué cantidades geométricas son independientes de la descripción.

### 14.29. Cierre de §14 y de la redacción de FPM-I-04

La afirmación que organiza todo el capítulo es:

$$
\boxed{
\text{una geometría puede admitir muchas descripciones numéricas coherentes}.
}
$$

Las representaciones cambian de acuerdo con el tipo de objeto:

$$
\boxed{
\text{punto: ley afín},
}
$$

$$
\boxed{
\text{vector: ley lineal},
}
$$

$$
\boxed{
\text{operador: conjugación}.
}
$$

Mientras tanto, las cantidades geométricas pertinentes se preservan bajo los cambios de descripción que respetan la estructura correspondiente.
Los ejercicios E028–E030 completan la integración conceptual del capítulo mediante comparación de tipos, invariantes y leyes de cambio.


## Bibliografía {#bibliografia}

**Arnold, V. I.** *Mathematical Methods of Classical Mechanics*. 2.ª ed. Springer, 1989. Para la estructura afín: parte I, cap. 1, §2.A, pp. 3–4.

**Arfken, G. B.; Weber, H. J.; Harris, F. E.** *Mathematical Methods for Physicists*. 7.ª ed. Academic Press, 2013. Cap. 3, especialmente §§3.2–3.4, pp. 126–142.

**Kleppner, D.; Kolenkow, R. J.** *An Introduction to Mechanics*. 2.ª ed. Cambridge University Press, 2010. Cap. 2, especialmente §2.4, p. 51 y ss., y §2.7, p. 59 y ss.

**Shankar, R.** *Basic Training in Mathematics: A Fitness Program for Science Students*. Springer, 1995. Cap. 7, §7.1, pp. 149–154.

**Shankar, R.** *Fundamentals of Physics I: Mechanics, Relativity, and Thermodynamics*. Expanded ed. Yale University Press, 2019. Cap. 2, §2.4, pp. 22–25.

---

[Capítulo 3](fisica-para-matematicos-capitulo-3-medicion-incertidumbre-estimacion-y-ordenes-de-magnitud.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [Capítulo 5](fisica-para-matematicos-capitulo-5-tiempo-movimiento-y-curvas.md)
