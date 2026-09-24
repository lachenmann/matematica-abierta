---
title: "Derivación de funciones elementales, inversas e implícitas"
description: "Capítulo 8 de Cálculo para matemáticos: inversas, raíces, potencias racionales y derivación implícita justificada; 40 ejercicios resueltos."
content-id: MA-BCH-0066
content-type: book-chapter
collection: PM-CAL
book-id: MA-BOK-0001
status: published
areas:
  - calculo
  - analisis
level: fundamental
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
date-created: 2026-09-21
date-modified: 2026-09-21
prerequisites:
  - MA-BCH-0003
  - MA-BCH-0004
  - MA-BCH-0010
  - MA-BCH-0077
  - MA-BCH-0063
  - MA-BCH-0064
  - MA-BCH-0065
number-sections: true
number-depth: 2
number-offset: [7]
---

# Derivación de funciones elementales, inversas e implícitas {#sec-t1-c09}

En el capítulo anterior demostramos cómo derivar combinaciones lineales, productos, cocientes y composiciones. También obtuvimos las derivadas de potencias enteras, polinomios y funciones racionales. Esas reglas permiten calcular mucho, pero no resuelven por sí solas una pregunta anterior a cualquier cálculo: **¿existe, y cuál es exactamente, la función cuya derivada queremos encontrar?**

Algunos símbolos esconden decisiones. La escritura $f^{-1}$ exige que $f$ sea invertible con dominio y codominio fijados; una raíz requiere demostrar la existencia del valor elegido y señalar su dominio; una ecuación como $F(x,y)=0$ describe inicialmente un conjunto de pares, no una función $y$ de $x$. Además, incluso cuando una función existe y es continua, su diferenciabilidad puede fallar en determinados puntos. No confundir estos problemas será el hilo conductor del capítulo.

Aquí *funciones elementales* designará, por ahora, las funciones **algebraicas accesibles con las herramientas que ya poseemos**: las polinómicas y racionales, las raíces que construiremos, las potencias racionales en dominios admisibles y ciertas funciones definidas mediante ramas de ecuaciones polinómicas. No adelantaremos las derivadas de logaritmos y exponenciales: su construcción rigurosa está reservada al capítulo visible 17, después de la teoría de la integral y del teorema fundamental del cálculo. Tampoco presentaremos una tabla de derivadas trigonométricas o trigonométricas inversas sin haber establecido previamente sus definiciones analíticas y los límites que las justifican. Esta delimitación no reduce el rigor del capítulo: identifica con precisión qué podemos demostrar ahora.

Nuestra ruta será

$$
\boxed{
\text{función y dominio}
\longrightarrow\text{existencia y continuidad de la inversa}
\longrightarrow\text{derivada de la inversa}
\longrightarrow\text{raíces y potencias racionales}
\longrightarrow\text{ramas y derivación implícita justificada}.
}
$$

La última etapa tendrá un alcance expresamente limitado: para una relación polinómica demostraremos la diferenciabilidad de una **rama continua previamente establecida**, bajo una condición algebraica precisa. La existencia general de una rama a partir de una ecuación pertenece al futuro teorema de la función implícita en varias variables y no será supuesta ni anunciada como un resultado ya demostrado.

## La fórmula no crea su función {#sec-t1-c09-01}

### Tres preguntas antes de calcular

La familiaridad con una expresión puede hacernos pasar directamente a su derivada. En el cálculo riguroso el orden debe ser otro. Primero preguntamos **qué objeto define la expresión**: una función completa, con dominio y codominio, o solamente una relación entre variables. Después comprobamos **que ese objeto existe con las propiedades necesarias**: por ejemplo, que una función posee inversa o que una ecuación tiene la rama elegida. Solo al final investigamos **si es diferenciable en el punto considerado** y qué fórmula permite hallar su derivada.

Estas preguntas no son tres maneras de formular el mismo problema. Una expresión puede estar bien definida sin ser invertible; una inversa puede existir y ser continua sin tener derivada finita en cierto punto; una ecuación puede admitir varias funciones distintas que la satisfagan. La regla de la cadena, ya demostrada, no subsana ninguna de esas ausencias: permite derivar una composición cuando se conocen las derivadas pertinentes, pero no fabrica funciones inversas ni ramas implícitas.

### Una misma expresión no determina una misma función inversa

Consideremos la regla algebraica $x\mapsto x^2$. En el capítulo 2 aprendimos que la regla, aislada, no especifica una función completa: faltan al menos su dominio y su codominio. El problema se hace visible al intentar invertirla.

::: {#exm-t1-0082}
**El cuadrado admite dos inversas después de elegir el dominio, pero no una inversa sobre toda la recta.** La función

$$
f:\mathbb R\longrightarrow\mathbb R,
\qquad f(x)=x^2,
$$

no es inyectiva, pues $f(1)=f(-1)=1$. No posee, por tanto, una función inversa $f^{-1}$ sobre su imagen: el valor $1$ tendría dos antecedentes. Tampoco la mera escritura $y^2=t$ permite decidir entre ellos.

La situación cambia si restringimos el dominio. Las funciones

$$
\begin{aligned}
f_+:[0,\infty)&\longrightarrow[0,\infty),&f_+(x)&=x^2,\\
f_-:(-\infty,0]&\longrightarrow[0,\infty),&f_-(x)&=x^2
\end{aligned}
$$

son biyectivas. La existencia y unicidad de la raíz cuadrada no negativa, establecidas al construir los reales, dan sus inversas:

$$
 f_+^{-1}(t)=\sqrt t,
 \qquad f_-^{-1}(t)=-\sqrt t,
 \qquad t\ge0.
$$

Comprobemos las identidades, con sus dominios. Para $t\ge0$,

$$
 f_+(\sqrt t)=t,
 \qquad f_-(-\sqrt t)=t.
$$

Para $x\ge0$, $\sqrt{x^2}=x$; para $x\le0$, $-\sqrt{x^2}=x$. Pero sobre toda la recta la primera igualdad no es cierta: si $x=-2$, entonces $\sqrt{x^2}=2\ne-2$. Precisamente por ello,

$$
\boxed{\sqrt{x^2}=|x|\quad\text{para todo }x\in\mathbb R,}
$$

no $\sqrt{x^2}=x$ sin restricción. Las dos fórmulas inversas corresponden a **dos funciones de partida diferentes**, obtenidas mediante restricciones explícitas. Ninguna convierte en invertible a $f:\mathbb R\to\mathbb R$. 
:::

El ejemplo muestra una distinción decisiva: **resolver una ecuación no equivale a construir la inversa de una función que no es inyectiva**. La ecuación $y^2=t$, para $t>0$, tiene las soluciones $\sqrt t$ y $-\sqrt t$. Una inversa, en cambio, debe asignar exactamente un antecedente a cada elemento de su dominio. La elección de rama precede a toda fórmula de derivación.

### La función inversa no es el recíproco

Los símbolos $f^{-1}$ y $1/f$ pueden parecer próximos, pero expresan operaciones diferentes. Si $f:A\to B$ es una biyección, $f^{-1}:B\to A$ deshace su asignación: satisface $f^{-1}(f(x))=x$ para $x\in A$. El recíproco de una función real se define, en cambio, por

$$
\frac1f(x)=\frac1{f(x)}
\qquad\text{cuando }x\in A\text{ y }f(x)\ne0.
$$

El capítulo 7 demostró la derivada del recíproco. Ese resultado **no** demuestra la fórmula de la derivada de una función inversa. En el ejemplo anterior, $f_+^{-1}(t)=\sqrt t$ está definida para $t\ge0$, mientras que $(1/f_+)(x)=1/x^2$ solo está definida para $x>0$. Son funciones distintas, con dominios y valores distintos; conocer cómo derivar la segunda no permite derivar automáticamente la primera.

Hay otra precaución: cuando obtengamos la fórmula de derivación inversa, será necesario indicar en qué puntos se evalúan ambas derivadas. Si $b=f(a)$, la derivada de $f^{-1}$ se estudia en $b$, mientras que la de $f$ se conoce en $a$. Una fórmula en la que esos puntos desaparezcan será, como mínimo, una abreviatura que habrá que reconstruir.

### Una relación puede contener varias gráficas

Consideremos ahora

$$
x^2+y^2=1.
$$

La ecuación describe los pares reales que la satisfacen. Para todo $x\in(-1,1)$, existen dos valores correspondientes de $y$, a saber, $\sqrt{1-x^2}$ y $-\sqrt{1-x^2}$. Así, el conjunto completo de soluciones no es la gráfica de una función $y$ definida sobre $(-1,1)$: viola la unicidad del valor de salida. Podemos, sin embargo, **seleccionar** una de sus ramas como una función genuina, por ejemplo

$$
\varphi_+:[-1,1]\longrightarrow\mathbb R,
\qquad \varphi_+(x)=\sqrt{1-x^2}.
$$

La existencia de la raíz de un número no negativo justifica su definición en ese dominio. Que sea una función y que satisfaga la ecuación no establece todavía la existencia de su derivada en todos sus puntos. Cerca de los extremos, además, los incrementos admisibles son unilaterales. Volveremos a esta distinción cuando abordemos las ramas algebraicas y la derivación implícita.

La frase informal «derivamos $x^2+y^2=1$ respecto de $x$» oculta una hipótesis: que se ha elegido una función $y=\varphi(x)$ y que esa función admite las derivadas que se pretenden usar. No empezaremos por esa manipulación. Primero identificaremos las ramas y después demostraremos qué condiciones permiten deducir su diferenciabilidad desde la relación.

### Dominios, puntos excluidos y condiciones suficientes

Del capítulo anterior conservamos otra enseñanza: una igualdad de expresiones sobre cierto conjunto no autoriza a añadir puntos a la función original. El cociente $(x^2-1)/(x-1)$ coincide con $x+1$ cuando $x\ne1$, pero el primer cociente sigue sin estar definido en $1$. Algo semejante ocurre al escoger una rama de una raíz: la regla puede ser algebraicamente correcta allí donde existe, pero esa corrección no extiende silenciosamente su dominio.

Del mismo modo, no debemos convertir una condición **suficiente** en una condición **necesaria**. El teorema que obtendremos para la derivada de una inversa exigirá, entre otras hipótesis, que cierta derivada sea no nula; de esa fórmula no se deduce que una función con derivada nula carezca de inversa. Inyectividad, continuidad de la inversa y diferenciabilidad de la inversa son cuestiones diferentes que investigaremos por separado.

Nuestra auditoría de trabajo puede formularse en forma de preguntas: ¿qué función se ha definido y sobre qué dominio?, ¿qué punto del dominio y qué incrementos son admisibles?, ¿la inversa o la rama ha sido construida?, ¿se ha demostrado su continuidad cuando es necesaria?, ¿qué resultado, exactamente, justifica la derivada? Cada respuesta deberá apoyarse en una definición, en un resultado anterior o en una demostración nueva, nunca en el aspecto conocido de la expresión.

::: {.callout-note title="Antes de continuar"}
Sin consultar el ejemplo, explica por qué $x\mapsto x^2$ no tiene inversa sobre $\mathbb R$ aunque para cada $t>0$ pueda resolverse $x^2=t$. Especifica después las dos restricciones que sí poseen inversa y demuestra las identidades de composición en sus dominios. Finalmente, identifica el supuesto oculto en la instrucción «derivar implícitamente $x^2+y^2=1$»: ¿qué función $y$ se está derivando y quién ha demostrado que es diferenciable?
:::

El siguiente paso será recuperar, sin rehacer las pruebas cerradas, los resultados sobre existencia y continuidad de funciones inversas de los capítulos 2 y 5. Solo después construiremos el teorema que permite calcular su derivada. **Una fórmula diferencial será la conclusión de ese recorrido, no el sustituto de sus hipótesis.**

## Inversa: existencia y continuidad primero {#sec-t1-c09-02}

### Deshacer una asignación: tres tareas diferentes

En §8.1 vimos que restringir el cuadrado a los números no negativos o a los no positivos produce dos funciones invertibles, aunque la regla $x\mapsto x^2$ sobre toda la recta no lo sea. La situación sugiere una pregunta más amplia: **¿qué debemos saber de una función para poder invertirla y estudiar después la derivada de su inversa?**

La respuesta tiene tres etapas, que conviene mantener separadas:

1. **Existencia.** Identificamos una función inyectiva $f:A\to\mathbb R$ y tomamos su imagen efectiva $J=f(A)$. La aplicación $f:A\to J$ es biyectiva; la teoría del capítulo 2 proporciona una única inversa $g:J\to A$.
2. **Continuidad.** La existencia de $g$ no afirma nada, por sí sola, sobre el comportamiento de sus valores ante entradas próximas. Necesitamos un resultado analítico adicional.
3. **Diferenciabilidad.** Incluso después de demostrar que $g$ es continua, queda pendiente investigar si su cociente incremental converge a un número real. Esta será la tarea de §8.3.

Obsérvese el papel de $J=f(A)$. Si el codominio declarado de la función original contiene valores que nunca se alcanzan, no hay un antecedente que la inversa pueda asignarles. Para invertir sin ambigüedades no basta escribir $f^{-1}$: debemos identificar primero una biyección entre el dominio y la **imagen**, o verificar sobreyectividad respecto del codominio que se haya elegido.

### Recuperación de un teorema ya demostrado

En el capítulo 5 demostramos @thm-t1-0023. Su especial relevancia aquí merece recuperar el enunciado, **sin repetir su demostración**:

::: {.callout-important title="Inversa continua sobre un intervalo: resultado disponible"}
Sean $I\subseteq\mathbb R$ un intervalo y $f:I\to\mathbb R$ una función continua e inyectiva. Pongamos $J=f(I)$. Entonces $J$ es un intervalo, existe la inversa única

$$
g=f^{-1}:J\longrightarrow I,
$$

y $g$ es continua en cada punto de $J$, con continuidad relativa al dominio $J$. Si $I$ contiene al menos dos puntos, $f$ es estrictamente creciente o estrictamente decreciente. El caso de un intervalo unitario se interpreta directamente.
:::

El resultado reúne conclusiones distintas. La **inyectividad** garantiza que una salida no tenga dos antecedentes; al considerar como codominio la **imagen**, garantizamos que tampoco falte ninguno. De ahí procede la existencia de $g$. La **continuidad de $g$**, en cambio, se deduce del teorema anterior gracias a que $f$ es continua y su dominio es un *intervalo*. No se obtiene de la mera biyección.

La monotonía estricta que aparece en el teorema tampoco se ha deducido de un signo de $f'$. Su prueba ya fue construida en el capítulo 5 mediante continuidad, valores intermedios e inyectividad, antes de introducir el teorema del valor medio. Podemos utilizarla aquí porque pertenece a nuestra teoría previa, pero no sustituir su justificación por un criterio diferencial que todavía no hemos demostrado.

::: {.callout-note title="Lee las flechas con su dominio"}
La inversión intercambia entradas y salidas:

$$
\begin{aligned}
f &: I\longrightarrow J, & x&\longmapsto y=f(x),\\
g=f^{-1} &: J\longrightarrow I, & y&\longmapsto x=g(y).
\end{aligned}
$$

Sus identidades son $g(f(x))=x$ para **$x\in I$** y $f(g(y))=y$ para **$y\in J$**. Para estudiar la continuidad de $g$ en $b=f(a)$, los valores que se aproximan a $b$ deben pertenecer a $J$; sus antecedentes pertenecen a $I$. Este cambio de variables será decisivo al derivar.
:::

### Una inversa global sin fórmula explícita

Los ejemplos escolares pueden transmitir la impresión de que solo hemos construido una inversa cuando conseguimos despejar una fórmula. No es así. La existencia de una función inversa es una propiedad de la asignación; disponer de una expresión cerrada es una cuestión distinta.

::: {#exm-t1-0083}
**Una inversa existente y continua sin necesidad de despejar.** Sea

$$
f:\mathbb R\longrightarrow\mathbb R,
\qquad f(x)=x^3+x.
$$

**Inyectividad por álgebra.** Si $u<v$, entonces

$$
\begin{aligned}
f(v)-f(u)
&=(v-u)(v^2+uv+u^2+1).
\end{aligned}
$$

El primer factor es positivo. El segundo también lo es, porque

$$
v^2+uv+u^2
=\left(u+\frac v2\right)^2+\frac{3v^2}{4}\ge0.
$$

Por tanto $f(v)>f(u)$: la función es estrictamente creciente y, en particular, inyectiva. No hemos empleado la derivada para obtener esta conclusión.

**Imagen.** Dado $t\in\mathbb R$, elijamos $M=|t|+1$. Se tiene

$$
f(-M)=-M^3-M<t<M^3+M=f(M).
$$

Como $f$ es un polinomio continuo, el teorema del valor intermedio proporciona algún $u\in(-M,M)$ con $f(u)=t$. La inyectividad hace único ese $u$. Por consiguiente, $f(\mathbb R)=\mathbb R$ y $f$ es biyectiva.

**Inversión y continuidad.** Podemos definir sin ambigüedad

$$
g:\mathbb R\longrightarrow\mathbb R,
\qquad g(t)=\text{el único real }u\text{ tal que }u^3+u=t.
$$

El resultado @thm-t1-0023 asegura que $g$ es continua en toda la recta. No hemos despejado $u$ ni calculado $g'(t)$; ninguna de esas operaciones era necesaria para justificar su existencia y continuidad. Por ejemplo, $g(0)=0$ y $g(2)=1$, pues $0^3+0=0$ y $1^3+1=2$.
:::

Este ejemplo separa el *conocimiento estructural* del *cálculo simbólico*. Sabemos qué función es $g$, cuál es su dominio, por qué cada valor tiene una única salida y por qué es continua. Todavía no sabemos, a partir de lo aquí demostrado, cuál es su derivada: esa conclusión exige un argumento nuevo.

### El intervalo no es un adorno de las hipótesis

¿Podríamos eliminar la palabra «intervalo» del teorema y conservar su conclusión para cualquier subconjunto de la recta? El siguiente ejemplo muestra que la continuidad de la función original y su inyectividad no bastan para ese enunciado general.

::: {#exm-t1-0084}
**Una biyección continua cuya inversa es discontinua.** Definamos

$$
A=[0,1)\cup\{2\},
\qquad
f:A\longrightarrow[0,1],
$$

mediante

$$
f(x)=
\begin{cases}
x,&0\le x<1,\\
1,&x=2.
\end{cases}
$$

La función es inyectiva: los valores obtenidos en $[0,1)$ pertenecen a $[0,1)$ y el valor de $2$ es $1$, distinto de todos ellos. Su imagen es exactamente $[0,1]$, de modo que es biyectiva.

Además, $f$ es continua **relativamente a $A$**. En cada punto $a\in[0,1)$ coincide localmente con la identidad; en $2$ la continuidad relativa es inmediata porque $2$ es un punto aislado de $A$: si $|x-2|<1/2$ y $x\in A$, entonces $x=2$.

La inversa existe y es

$$
g:[0,1]\longrightarrow A,
\qquad
g(y)=
\begin{cases}
y,&0\le y<1,\\
2,&y=1.
\end{cases}
$$

Pero $g$ **no es continua en $1$**. Basta fijar $\varepsilon=1/2$. Para cualquier $\delta>0$, tomemos

$$
y=1-\min\left\{\frac\delta2,\frac12\right\}.
$$

Entonces $y\in[0,1)$ y $|y-1|<\delta$, mientras que

$$
|g(y)-g(1)|=|y-2|>1>\varepsilon.
$$

Por tanto ningún radio $\delta$ garantiza la continuidad de $g$ en $1$. La función de partida era continua e inyectiva, pero $A$ no es un intervalo: allí fracasa la conclusión que intentábamos generalizar.
:::

El contraejemplo no dice que una función con dominio no intervalar tenga siempre inversa discontinua. Dice algo más preciso: **sin una hipótesis adicional, la continuidad e inyectividad de $f$ sobre un subconjunto arbitrario no autorizan a afirmar la continuidad de su inversa**. En nuestras aplicaciones al cálculo de una variable, trabajar sobre intervalos nos proporciona exactamente la garantía establecida en el capítulo 5.

### Volver a las ramas: restringir también significa cambiar la imagen

Recuperemos brevemente el cuadrado, ahora mediante un diagrama de funciones tipadas. La elección de un intervalo modifica tanto los antecedentes permitidos como la imagen a la que llega la inversa:

| Función de partida | Imagen efectiva | Función inversa |
|:---|:---|:---|
| $q_+:[0,2]\to[0,4]$, $q_+(x)=x^2$ | $[0,4]$ | $q_+^{-1}:[0,4]\to[0,2]$, $q_+^{-1}(t)=\sqrt t$ |
| $q_-:[-2,0]\to[0,4]$, $q_-(x)=x^2$ | $[0,4]$ | $q_-^{-1}:[0,4]\to[-2,0]$, $q_-^{-1}(t)=-\sqrt t$ |

La existencia de las raíces cuadradas no negativas, probada en el capítulo 1, permite verificar las dos imágenes y las dos identidades inversas. Las funciones $q_+$ y $q_-$ son continuas y estrictamente monótonas en sus respectivos intervalos: para $0\le u<v$ tenemos $u^2<v^2$, mientras que para $u<v\le0$ se cumple $u^2>v^2$. Por @thm-t1-0023, **ambas inversas son continuas sobre $[0,4]$**, incluidos sus extremos en el sentido relativo.

No debemos reemplazar ese enunciado por «las inversas son derivables también en $0$ y $4$». Continuidad y derivabilidad son propiedades diferentes; además, una derivada en un extremo, según la definición de nuestro capítulo 6, solo podría considerarse con los incrementos admitidos por el dominio. El estudio de tales cocientes pertenece al paso siguiente.

::: {.callout-note title="Comprueba que entendiste las hipótesis"}
Considera una función continua $f:I\to\mathbb R$ sobre un intervalo. ¿Qué información adicional garantiza que tenga inversa sobre $f(I)$? ¿Qué teorema garantiza la continuidad de esa inversa? Explica por qué ninguna de estas respuestas exige conocer una fórmula para $f^{-1}$ ni el signo de $f'$. Por último, identifica en el ejemplo del dominio $[0,1)\cup\{2\}$ la hipótesis del teorema que dejó de cumplirse.
:::

Hemos establecido el punto de partida para la derivación de funciones inversas: disponemos de una biyección $f:I\to J$ y de una función $g=f^{-1}:J\to I$ cuya continuidad ya está justificada. En §8.3 fijaremos $a\in I$, escribiremos $b=f(a)$ y estudiaremos directamente el cociente

$$
\frac{g(y)-g(b)}{y-b},
\qquad y\in J,\quad y\ne b.
$$

Solo allí aparecerá una fórmula para su límite, y solo después de verificar las hipótesis que permiten invertir el correspondiente cociente de $f$.

## Derivada de una función inversa {#sec-t1-c09-03}

### ¿De dónde puede salir el recíproco de una pendiente?

La sección anterior terminó con dos funciones verdaderamente construidas: $f:I\to J$, continua e inyectiva sobre un intervalo, y su inversa continua $g:J\to I$, donde $J=f(I)$. Esta información todavía no contiene una derivada de $g$. Para descubrirla, conviene comenzar por dos puntos distintos de la gráfica, no por una identidad derivada formalmente.

Fijemos $a\in I$ y llamemos $b=f(a)$. Tomemos una salida $y\in J$, distinta de $b$, y recuperemos su antecedente $x=g(y)$. Las identidades inversas dan

$$
g(b)=a,\qquad f(x)=y.
$$

Como $f$ es inyectiva, $y\ne b$ equivale a $x\ne a$. Por tanto, los incrementos $y-b$ y $x-a$ son ambos no nulos y podemos escribir la igualdad **exacta**

$$
\frac{g(y)-g(b)}{y-b}
=\frac{x-a}{f(x)-f(a)}
=\left(\frac{f(x)-f(a)}{x-a}\right)^{-1}.
$$

La razón de cambio de la inversa es, entre los puntos correspondientes, el recíproco de la razón de cambio de la función original. Pero **una identidad entre cocientes no demuestra todavía que sus límites existan**. Para convertirla en un teorema tenemos que controlar dónde se acercan $x$ e $y$ y cuándo se permite pasar al recíproco.

### El enunciado: dominios y puntos de evaluación visibles

::: {#thm-t1-0031}
**Teorema de la derivada de una función inversa en un intervalo.** Sea $I\subseteq\mathbb R$ un intervalo y sea $f:I\to\mathbb R$ continua e inyectiva. Definamos $J=f(I)$ y consideremos la inversa, existente y continua por @thm-t1-0023,

$$
g=f^{-1}:J\longrightarrow I.
$$

Sea $a\in I$ un punto de acumulación de $I$, y pongamos $b=f(a)$. Supongamos que existe la derivada relativa finita de $f$ en $a$ y que

$$
f'_I(a)\ne0.
$$

Entonces $b$ es un punto de acumulación de $J$, $g$ es diferenciable en $b$ relativamente a $J$ y

$$
\boxed{g'_J(b)=\frac{1}{f'_I(a)}.}
$$

Equivalente y abreviadamente, siempre que se cumplan las hipótesis en $a=g(b)$,

$$
(f^{-1})'(b)=\frac{1}{f'(f^{-1}(b))}.
$$
:::

**Demostración.** Separamos los pasos que suelen quedar ocultos en la fórmula.

**1. La inversa existe y es continua antes de derivarla.** Por hipótesis, $f$ es inyectiva y $J$ es su imagen; por tanto $f:I\to J$ es biyectiva. El teorema @thm-t1-0023 asegura que $g=f^{-1}$ existe y es continua en $b$, relativamente a $J$. No hemos supuesto que $g$ sea diferenciable.

**2. El punto $b$ permite un límite perforado en $J$.** Como $a$ es punto de acumulación de $I$, podemos escoger puntos $x\in I\setminus\{a\}$ arbitrariamente próximos a $a$. La continuidad de $f$ en $a$ garantiza que sus imágenes $f(x)$ se aproximan a $f(a)=b$; la inyectividad garantiza, además, que $f(x)\ne b$. Más explícitamente, dado $\varepsilon>0$, la continuidad proporciona $\delta>0$ tal que

$$
x\in I,\quad |x-a|<\delta
\quad\Longrightarrow\quad |f(x)-b|<\varepsilon.
$$

Por acumulación elegimos $x\in I$ con $0<|x-a|<\delta$. Entonces $y=f(x)\in J$ cumple $0<|y-b|<\varepsilon$. Esto demuestra que $b$ es punto de acumulación de $J$, condición necesaria para definir $g'_J(b)$ según @def-t1-0042.

**3. Los antecedentes se aproximan al punto correcto.** Para $y\in J\setminus\{b\}$ escribamos $x=g(y)$. Por la continuidad de $g$ en $b$,

$$
\lim_{\substack{y\to b\\y\in J}}g(y)=g(b)=a.
$$

En consecuencia, cuando $y\to b$ relativamente a $J$, el antecedente $x=g(y)$ tiende a $a$ relativamente a $I$; además, permanece distinto de $a$ por inyectividad. **Este es el paso en el que necesitamos la continuidad de la inversa.** La mera igualdad $f(x)=y$ no bastaría para deducirlo.

**4. El denominador del recíproco queda separado de cero.** Por la definición de derivada relativa,

$$
Q(x):=\frac{f(x)-f(a)}{x-a}
\longrightarrow L:=f'_I(a)\ne0
\qquad (x\to a,\ x\in I\setminus\{a\}).
$$

En particular, para $x$ suficientemente próximo a $a$ dentro del dominio perforado, $|Q(x)-L|<|L|/2$, de modo que $|Q(x)|>|L|/2>0$. El cociente $Q(x)$ está bien definido y su recíproco también. Además,

$$
\left|\frac1{Q(x)}-\frac1L\right|
=\frac{|Q(x)-L|}{|Q(x)|\,|L|}
\le\frac{2}{|L|^2}|Q(x)-L|
\longrightarrow0.
$$

Esta estimación muestra directamente por qué es indispensable la condición $L\ne0$ para aplicar el paso al recíproco.

**5. Concluimos mediante el cociente incremental de la inversa.** Para $y\in J\setminus\{b\}$ y $x=g(y)$ tenemos

$$
\begin{aligned}
\frac{g(y)-g(b)}{y-b}
&=\frac{x-a}{f(x)-f(a)}\\
&=\frac1{Q(x)}.
\end{aligned}
$$

El paso 3 permite aplicar el límite del paso 4 cuando $y\to b$ dentro de $J$. Por tanto,

$$
\lim_{\substack{y\to b\\y\in J}}
\frac{g(y)-g(b)}{y-b}
=\frac1L=\frac1{f'_I(a)}.
$$

El límite existe como número real. Según la definición de derivada relativa, hemos demostrado simultáneamente que $g$ es diferenciable en $b$ y que su derivada tiene el valor anunciado. $\square$

### Leer la prueba en sentido inverso

El resultado admite una lectura geométrica: las coordenadas de los puntos de las gráficas de $f$ y $g$ se intercambian, y con ellas se intercambian los incrementos horizontal y vertical. De ahí nace el recíproco de las pendientes secantes. La pendiente límite de la inversa solo puede obtenerse de esa observación cuando los antecedentes correspondientes convergen al punto adecuado y la pendiente límite original no es cero.

La función $f$ y su inversa se evalúan en **puntos distintos**:

$$
\begin{aligned}
 a&\in I,&b&=f(a)\in J,\\
 f'_I(a)&=L\ne0,&g'_J(b)&=1/L.
\end{aligned}
$$

Por eso escribir $(f^{-1})'(x)=1/f'(x)$ sin explicar qué representa $x$ es, en general, incorrecto. Si la variable de entrada de la inversa se llama $y$, el antecedente en el que se evalúa $f'$ es $g(y)$: la forma correcta es $g'(y)=1/f'(g(y))$, exclusivamente donde las hipótesis estén verificadas.

::: {.callout-warning title="Una justificación circular que debemos evitar"}
De $g(f(x))=x$ sería tentador escribir $(g\circ f)'(a)=g'(f(a))f'(a)=1$ y despejar $g'(f(a))$. **Ese cálculo ya supone que $g'(f(a))$ existe**, precisamente lo que teníamos que demostrar. Ahora sí podemos emplear la regla de la cadena de @thm-t1-0030 como comprobación *posterior* del resultado, nunca como su fundamento inicial.
:::

### Una inversa cuyo valor conocemos sin disponer de una fórmula cerrada

El ejemplo de §8.2 proporciona una aplicación en la que el teorema evita la necesidad de despejar la función inversa.

::: {#exm-t1-0085}
**Derivar la inversa de $x^3+x$ en dos puntos.** Sea

$$
f:\mathbb R\longrightarrow\mathbb R,
\qquad f(x)=x^3+x,
$$

cuya biyectividad y cuya inversa continua $g:\mathbb R\to\mathbb R$ quedaron demostradas en @exm-t1-0083 mediante álgebra y el teorema del valor intermedio. El capítulo 7 permite derivar el polinomio:

$$
f'(x)=3x^2+1.
$$

Esta cantidad es positiva y, en particular, no nula para todo $x\in\mathbb R$. **No necesitamos deducir la inyectividad a partir de ese signo:** ya quedó probada independientemente.

Sabemos que $f(0)=0$ y $f(1)=2$, de modo que $g(0)=0$ y $g(2)=1$. Aplicando el teorema en $a=0$ y $a=1$, respectivamente, obtenemos

$$
\begin{aligned}
g'(0)&=\frac1{f'(0)}=1,\\
g'(2)&=\frac1{f'(1)}=\frac14.
\end{aligned}
$$

De hecho, para cualquier $t\in\mathbb R$ la misma prueba autoriza la identidad

$$
g'(t)=\frac1{3[g(t)]^2+1}.
$$

La fórmula expresa la derivada mediante la inversa **ya definida**; no exige encontrar una expresión elemental explícita para $g(t)$.
:::

### Cuando la derivada original es cero: un límite que no se puede invertir

El teorema no afirma que una función con $f'(a)=0$ carezca de inversa. La inyectividad y la diferenciabilidad son propiedades diferentes. Lo que sucede es que el recíproco $1/f'(a)$ deja de ser un número real y nuestro argumento no puede concluir la existencia de una derivada finita para la inversa.

Hay una afirmación más precisa que podemos demostrar: **si ambas funciones inversas son diferenciables con derivadas finitas en los puntos correspondientes, la derivada de la función original no puede ser cero.** En efecto, solo después de suponer ambas derivabilidades es lícito aplicar la regla de la cadena a $g\circ f=\operatorname{id}_I$; obtenemos

$$
1=(g\circ f)'_I(a)=g'_J(b)f'_I(a).
$$

El primer miembro es la derivada relativa de la identidad en el punto de acumulación $a$. Si $f'_I(a)=0$, la igualdad sería imposible para cualquier valor real de $g'_J(b)$. Se trata de una **condición necesaria** bajo derivabilidad de ambas, no de una prueba de existencia de inversa a partir de $f'(a)\ne0$.

Veamos un caso concreto que aísla este fenómeno. Definamos

$$
h:[-1,1]\longrightarrow[-1,1],\qquad h(x)=x^3.
$$

Para $u<v$, la factorización

$$
v^3-u^3=(v-u)(v^2+uv+u^2)>0
$$

es estrictamente positiva: el primer factor es positivo y el segundo lo es para $u\ne v$, puesto que

$$
v^2+uv+u^2=\left(u+\frac v2\right)^2+\frac{3v^2}{4},
$$

cuyos dos sumandos solo se anulan simultáneamente cuando $u=v=0$, excluido aquí. Por continuidad y el teorema del valor intermedio, $h([-1,1])=[-1,1]$; por tanto tiene inversa continua $k:[-1,1]\to[-1,1]$. Se cumple $h'(0)=0$ y $k(0)=0$.

Para examinar si $k$ tiene derivada finita en el origen, usemos las entradas $y=u^3$, donde $u\in[-1,1]\setminus\{0\}$. Entonces $k(y)=u$ y

$$
\frac{k(y)-k(0)}{y-0}
=\frac{u}{u^3}=\frac1{u^2}.
$$

Cuando $y\to0$ dentro de $[-1,1]$, la continuidad de $k$ implica $u\to0$; en particular, los valores anteriores crecen sin cota al tomar, por ejemplo, $u=1/n$ con $n\to\infty$. Si el cociente incremental de $k$ tuviera límite real, estaría acotado en un entorno perforado de cero, contradicción. **La inversa existe y es continua, pero no tiene derivada finita en $0$.** No hemos necesitado introducir aún una notación general de raíces de índice arbitrario.

El mismo cuidado se requiere en los extremos. La inversa del cuadrado restringido $q:[0,\infty)\to[0,\infty)$ es $q^{-1}(t)=\sqrt t$, pero $q'_{{[0,\infty)}}(0)=0$. Su cociente incremental en el extremo de la imagen satisface, para $t=u^2>0$,

$$
\frac{q^{-1}(t)-q^{-1}(0)}t=\frac{u}{u^2}=\frac1u,
$$

que no posee límite real finito cuando $u\to0^+$. Es una afirmación sobre la derivada **relativa al dominio** $[0,\infty)$, no sobre valores que la raíz ni siquiera admite.

::: {.callout-important title="Qué demuestra el teorema y qué no"}
La hipótesis $f'_I(a)\ne0$ es suficiente para la fórmula **junto con** continuidad, inyectividad, dominio intervalar y acumulación del punto. No construye una inversa por sí sola. Una derivada no nula en un punto aislado de la discusión global no autoriza a inferir inyectividad en algún entorno: esa cuestión se analizará expresamente en §8.7. Por otro lado, cuando $f'_I(a)=0$, la inversa puede seguir existiendo, pero no puede tener derivada real finita en $b$ si ambas funciones se relacionan como hemos supuesto y la regla de la cadena es aplicable.
:::

### Comprobación activa: reconstruir las hipótesis

Sin mirar la demostración, completa el siguiente argumento. Se sabe que $f$ es continua e inyectiva en un intervalo $I$; se fija $a\in I$, punto de acumulación, y se define $b=f(a)$ y $g=f^{-1}$. ¿Qué resultado demuestra que $g$ es continua? ¿Cómo justificas que $b$ sea punto de acumulación de $J=f(I)$? ¿Por qué $y\ne b$ implica $g(y)\ne a$? ¿Qué hipótesis permite pasar al límite del recíproco y por qué no es legítimo empezar derivando $g\circ f$?

La respuesta configura la cadena completa:

$$
\boxed{
\text{inyectividad e imagen}
\longrightarrow\text{inversa existente y continua}
\longrightarrow\text{cocientes recíprocos}
\longrightarrow\text{límite real de la inversa}.
}
$$

En §8.4 emplearemos este resultado para estudiar las raíces de cualquier índice, pero solo **después de construir rigurosamente** cada función raíz mediante continuidad, valor intermedio y unicidad algebraica. La fórmula de la derivada nunca reemplazará esa construcción.

## Raíces de cualquier índice: construir antes de derivar {#sec-t1-c09-04}

### ¿Qué asegura el símbolo de una raíz?

La raíz cuadrada no negativa ya fue construida al estudiar los números reales. Ahora queremos extender esa existencia a cualquier índice natural. La pregunta no es todavía cómo derivar $t\mapsto\sqrt[n]{t}$: **antes debemos probar que la expresión determina un único número y precisar para cuáles valores de $t$ lo hace**. El teorema de la derivada inversa de §8.3 se aplicará después, nunca como prueba de que la raíz existe.

Fijemos un entero $n\ge1$. Consideraremos inicialmente la función polinómica

$$
q_n:[0,\infty)\longrightarrow\mathbb R,
\qquad q_n(u)=u^n.
$$

Su continuidad está disponible desde el capítulo 5. Para invertirla debemos resolver dos cuestiones independientes: demostrar que alcanza cada $t\ge0$ y que nunca alcanza ese mismo valor en dos puntos distintos del dominio. La primera utilizará el teorema del valor intermedio; la segunda, una identidad algebraica.

### Existencia, unicidad y continuidad de la raíz no negativa

::: {#prp-t1-0042}
**Construcción y derivación de las raíces de índice natural.** Sea $n\in\mathbb N$ con $n\ge1$.

1. Para cada $t\ge0$ existe un único $u\ge0$ tal que $u^n=t$. Denotaremos ese número por $r_n(t)$ o $\sqrt[n]{t}$. La función
   $$
   r_n:[0,\infty)\longrightarrow[0,\infty)
   $$
   es la inversa de $q_n:[0,\infty)\to[0,\infty)$, $q_n(u)=u^n$, y es continua respecto de su dominio.
2. Para cada $t>0$, $r_n$ posee derivada finita y
   $$
   r_n'(t)=\frac{1}{n\,[r_n(t)]^{n-1}}.
   $$
3. Si $n$ es impar, existe además una única función raíz real $\widetilde r_n:\mathbb R\to\mathbb R$ caracterizada por $[\widetilde r_n(t)]^n=t$. Coincide con $r_n$ para $t\ge0$, es continua en toda la recta y, para $t\ne0$,
   $$
   \widetilde r_n'(t)=\frac{1}{n\,[\widetilde r_n(t)]^{n-1}}.
   $$
   Si $n$ es par, ningún $t<0$ tiene raíz real de índice $n$.

**Demostración.**

**1. Existencia para $t\ge0$.** Fijemos $t\ge0$ y elijamos $M=t+1>0$. Puesto que $M\ge1$ y $n\ge1$, tenemos $M^n\ge M>t$. El polinomio $q_n$ es continuo en $[0,M]$, y

$$
q_n(0)=0\le t<M^n=q_n(M).
$$

Por el teorema del valor intermedio existe $u\in[0,M]$ tal que $u^n=t$. En particular, cuando $t=0$, la construcción permite $u=0$: no necesitamos dividir por $t$ ni excluir el extremo.

**2. Unicidad sin utilizar derivadas.** Si $0\le u<v$, la factorización de la diferencia de potencias proporciona

$$
\begin{aligned}
v^n-u^n
&=(v-u)\bigl(v^{n-1}+v^{n-2}u+\cdots+u^{n-1}\bigr).
\end{aligned}
$$

Para $n=1$, esta igualdad se reduce a $v-u>0$. Para $n\ge2$, el primer factor es positivo y cada sumando del segundo es no negativo; además $v^{n-1}>0$, pues $v>u\ge0$. Por tanto $v^n-u^n>0$ en todos los casos. La función $q_n$ es estrictamente creciente en $[0,\infty)$ por un argumento puramente algebraico y, en particular, inyectiva. Dos números no negativos distintos no pueden tener la misma potencia $n$-ésima. Quedan probadas la existencia y la unicidad prometidas.

Ahora, y no antes, la asignación $t\mapsto r_n(t)$ está bien definida: $r_n(t)$ es el único $u\ge0$ hallado. La existencia para todo $t\ge0$ y la inyectividad prueban que

$$
q_n:[0,\infty)\longrightarrow[0,\infty)
$$

es biyectiva, con identidades

$$
q_n(r_n(t))=t\quad(t\ge0),
\qquad r_n(q_n(u))=u\quad(u\ge0).
$$

El teorema @thm-t1-0023, aplicado al intervalo $[0,\infty)$, asegura la continuidad de $r_n$ en todo su dominio, **incluido $0$ en sentido relativo**. Ni la inyectividad ni esta continuidad han sido obtenidas a partir de una derivada.

**3. Derivada para $t>0$.** Fijemos $t>0$ y pongamos $a=r_n(t)>0$. El capítulo 7 proporciona la derivada de una potencia natural, relativamente a $[0,\infty)$:

$$
(q_n)'_{[0,\infty)}(a)=n a^{n-1}>0.
$$

Las hipótesis de @thm-t1-0031 ya están justificadas: dominio intervalar, continuidad, inyectividad, inversa continua, punto $a$ de acumulación y derivada no nula. Como $q_n(a)=t$, concluimos que

$$
r_n'(t)=\frac1{(q_n)'(a)}
=\frac1{n a^{n-1}}
=\frac1{n\,[r_n(t)]^{n-1}}.
$$

Para $n=1$ interpretamos $a^0=1$; la fórmula dice simplemente $r_1(t)=t$ y $r_1'(t)=1$, como corresponde a la identidad.

**4. Extensión para índice impar.** Supongamos que $n$ es impar. Si $t<0$, la existencia y unicidad anteriores, aplicadas a $-t>0$, proporcionan un único $v=r_n(-t)>0$ con $v^n=-t$. Puesto que $n$ es impar, $u=-v$ satisface

$$
u^n=(-v)^n=-v^n=t.
$$

Es el único antecedente real: si $w^n=t<0$, entonces $w<0$ (las potencias impares conservan el signo); así $-w>0$ y $(-w)^n=-t$, por lo que la unicidad no negativa da $-w=v$ y $w=u$. Para $t\ge0$ ya existe exactamente la raíz no negativa; ninguna raíz negativa puede tener potencia positiva o nula distinta de cero. Podemos definir, por tanto,

$$
\widetilde r_n(t)=
\begin{cases}
r_n(t),&t\ge0,\\
-r_n(-t),&t<0.
\end{cases}
$$

Acabamos de construir una inversa global de $Q_n:\mathbb R\to\mathbb R$, $Q_n(u)=u^n$. Esta función es continua por ser polinómica e inyectiva por la unicidad de las raíces para cada signo; su imagen es toda $\mathbb R$ por existencia. El teorema @thm-t1-0023 aplicado al intervalo $\mathbb R$ demuestra que $\widetilde r_n$ es continua en toda la recta, incluido el origen: no hace falta presumir continuidad en el empalme de la definición por casos.

Si $t<0$ y $a=\widetilde r_n(t)<0$, se cumple $Q_n'(a)=na^{n-1}>0$, ya que $n-1$ es par. El teorema @thm-t1-0031 da la fórmula anunciada; para $t>0$ ya la obtuvimos en el paso anterior. El caso $n=1$ vuelve a ser la identidad, incluida su derivada en $0$.

**5. Índice par y entrada negativa.** Si $n$ es par, $u^n\ge0$ para cualquier $u\in\mathbb R$. Por consiguiente, la igualdad $u^n=t$ es imposible en los reales cuando $t<0$. Esto no significa que falle un método para hallar la raíz: **no existe el número real buscado**. $\square$
:::

### Interpretar la construcción: raíz, dominio y elección de signo

Lo que llamamos $\sqrt[n]{t}$ para $t\ge0$ es, por definición, **la raíz no negativa**. Si el índice es par y $t>0$, también $-\sqrt[n]{t}$ satisface la ecuación $u^n=t$; son las dos soluciones reales, no dos valores de una misma función. Para $t=0$ ambas expresiones coinciden en el único valor $0$. Si el índice es impar, la raíz es única en toda la recta: en adelante podremos escribir $\sqrt[n]{t}=\widetilde r_n(t)$ también para $t<0$, sin cambiar de rama.

Por ejemplo, de $(-2)^3=-8$ se deduce $\sqrt[3]{-8}=-2$. En cambio, la escritura $\sqrt[4]{-8}$ no designa un número real. No basta que una manipulación simbólica resulte familiar: es necesario que sus entradas pertenezcan al dominio de la función efectivamente construida.

Hay un detalle de notación que será decisivo en §8.5: **todavía no hemos definido potencias de exponente racional como una operación general**. La igualdad $\sqrt[n]{t}=t^{1/n}$ podrá adoptarse cuando fijemos su significado y sus dominios; no ha intervenido como premisa en la construcción anterior.

### ¿Qué ocurre en cero? El límite que la fórmula no incluye

El resultado @prp-t1-0042 garantiza diferenciabilidad de $r_n$ para $t>0$, pero no permite sustituir $t=0$ en un denominador que entonces puede anularse. El caso $n=1$ es excepcional y sencillo: $r_1$ es la identidad y su derivada relativa en $0$ vale $1$. Consideremos $n\ge2$.

Para $h>0$, pongamos $u=r_n(h)>0$. Como $u^n=h$ y $r_n(0)=0$, el cociente incremental derecho es exactamente

$$
\frac{r_n(h)-r_n(0)}{h}
=\frac{u}{u^n}
=\frac1{u^{n-1}}.
$$

Por la continuidad de $r_n$ en $0$, $u=r_n(h)\to0^+$ cuando $h\to0^+$. Dado cualquier $K>0$, basta tomar $u>0$ suficientemente pequeño para que $u^{n-1}<1/K$; entonces el cociente es mayor que $K$. Podemos hacerlo con entradas admisibles $h=u^n\to0^+$. Por tanto el cociente no tiene límite real finito: **$r_n$ no es derivable en $0$ respecto de $[0,\infty)$ cuando $n\ge2$**.

Si $n\ge3$ es impar, la extensión $\widetilde r_n$ tampoco tiene derivada finita en cero. Ahora podemos tomar $u$ de cualquiera de los dos signos; para $h=u^n\ne0$ seguimos teniendo

$$
\frac{\widetilde r_n(h)-\widetilde r_n(0)}{h}
=\frac1{u^{n-1}},
$$

que crece sin cota porque $n-1$ es par. Esto recupera y generaliza el diagnóstico de la inversa de $x^3$ de §8.3. No estamos asignando el valor $+\infty$ a una derivada real: la definición del capítulo 6 exige un límite **finito**, que aquí no existe.

### Un ejemplo que obliga a comprobar todas las etapas

::: {#exm-t1-0086}
**Cuarta raíz positiva y raíz cúbica negativa.** Sabemos que $3^4=81$, con $3\ge0$; la unicidad de @prp-t1-0042 demuestra $\sqrt[4]{81}=3$. Para $t=81>0$, la fórmula diferencial sí es aplicable y da

$$
\left.\frac{d}{dt}\sqrt[4]{t}\right|_{t=81}
=\frac1{4\cdot3^3}=\frac1{108}.
$$

Para el índice impar, $(-2)^3=-8$ y la raíz construida globalmente satisface $\sqrt[3]{-8}=-2$. Como su antecedente no es cero,

$$
\left.\frac{d}{dt}\sqrt[3]{t}\right|_{t=-8}
=\frac1{3(-2)^2}=\frac1{12}.
$$

La comparación importante no es solo numérica: el primer cálculo utiliza una inversa definida sobre $[0,\infty)$; el segundo, una inversa definida sobre toda $\mathbb R$. En ninguno hemos deducido existencia, unicidad ni dominio a partir de una supuesta regla de derivación.
:::

::: {.callout-warning title="Un salto ilegítimo frecuente"}
«La derivada de $u^n$ es $nu^{n-1}$; luego $\sqrt[n]{t}$ existe y su derivada es $1/(n\sqrt[n]{t}^{\,n-1})$». La primera premisa no demuestra que una ecuación $u^n=t$ tenga solución ni que esta sea única en el dominio elegido. La fórmula diferencial solo se obtiene **después** de establecer una biyección continua, su inversa continua y una derivada original no nula en el antecedente.
:::

### Comprueba las dependencias antes de avanzar

Para $n=5$ y $t=-32$, justifica la existencia y unicidad de la raíz real, indica su valor y calcula la derivada en ese punto. Repite únicamente las preguntas de existencia y dominio para $n=4$ y $t=-32$. Finalmente, explica por qué el argumento de $r_n'(t)$ para $t>0$ no demuestra diferenciabilidad en $t=0$ si $n\ge2$, aunque $r_n$ sea continua allí.

Nuestra cadena queda cerrada hasta las raíces:

$$
\boxed{
\text{continuidad de }u^n
\longrightarrow\text{existencia por valor intermedio}
\longrightarrow\text{unicidad algebraica}
\longrightarrow\text{inversa continua}
\longrightarrow\text{derivada donde procede}.
}
$$

En §8.5 construiremos las potencias de exponente racional y estudiaremos qué fórmulas conservan su significado al combinar raíces, signos y cocientes. No presentaremos identidades de exponentes fuera de sus dominios legítimos.

## Potencias racionales y funciones algebraicas explícitas {#sec-t1-c09-05}

### ¿Qué significa elevar a una fracción?

La construcción de §8.4 nos permite afirmar que, para cada $n\ge1$, existe una raíz $n$-ésima no negativa de todo número no negativo; además, si $n$ es impar, existe una raíz real única para cualquier argumento. Sin embargo, ninguna de esas afirmaciones define por sí sola la expresión $x^{m/n}$. Falta escoger una representación del exponente, determinar el dominio y decidir qué hacemos con un exponente negativo. Solo después tendremos una función a la que aplicar las reglas de derivación.

Fijemos un número racional $q$. Lo escribiremos en su **forma reducida**

$$
q=\frac mn,\qquad m\in\mathbb Z,\quad n\in\mathbb N,\quad n\ge1,\quad \gcd(|m|,n)=1.
$$

Para $q=0$, la representación reducida es $0/1$. Esta convención evita que las propiedades de una función dependan de una elección accidental de denominador. Por ejemplo, para $x<0$, escribir una fracción sin reducir puede inducirnos a extraer una raíz de índice par que no existe, pese a que el exponente reducido tenga denominador impar.

**Definición con dominio.** Si $m\ne0$ y $x>0$, ponemos

$$
x^{m/n}:=[r_n(x)]^m,
$$

con las potencias enteras interpretadas como en el capítulo 7; el número $r_n(x)$ es estrictamente positivo, de modo que también están definidos sus exponentes negativos. Si $n$ es impar, utilizamos exactamente la misma expresión para $x<0$, pero entendiendo $r_n(x)$ como la extensión real impar $\widetilde r_n(x)$ de @prp-t1-0042. Para $x=0$, definimos $0^{m/n}=0$ **si $m>0$**; si $m<0$, la expresión queda indefinida porque exigiría el recíproco de cero. Para $q=0$, adoptamos la función potencia constante $x^0=1$ en toda $\mathbb R$, en consonancia con el tratamiento funcional del capítulo 7: no estamos asignando aquí un valor a un símbolo aislado $0^0$.

Así, para $q\ne0$ reducido, el dominio real natural que hemos fijado es

$$
D_q=
\begin{cases}
\mathbb R,& n\text{ impar y }m>0,\\
\mathbb R\setminus\{0\},&n\text{ impar y }m<0,\\
[0,\infty),&n\text{ par y }m>0,\\
(0,\infty),&n\text{ par y }m<0.
\end{cases}
$$

Si $n=1$, la definición coincide con las potencias enteras ya construidas. Si $n$ es par, una base negativa está excluida: la potencia racional **no es una instrucción para fabricar raíces reales inexistentes**. El convenio $x^0=1$ corresponde a una función constante, y se trata por separado de los casos $m\ne0$.

### Una representación reducida no se puede sustituir por una operación ilegítima

Para $x>0$, incluso si inicialmente escribimos $q=m/n=p/s$ con $n,s\ge1$, el valor obtenido por raíces y potencias positivas no depende de la representación. En efecto, sean $a=r_n(x)>0$ y $b=r_s(x)>0$. Usando únicamente las leyes de exponentes **enteros** para bases positivas,

$$
(a^m)^{ns}=(a^n)^{ms}=x^{ms},
\qquad
(b^p)^{ns}=(b^s)^{pn}=x^{pn}.
$$

Como $ms=pn$ y la potencia de índice $ns$ es inyectiva en $(0,\infty)$ por §8.4, resulta $a^m=b^p$. Esta comprobación no requiere definir potencias reales arbitrarias.

El razonamiento **no** autoriza repetir las mismas operaciones cuando una base negativa y un denominador par hacen inexistente alguna raíz intermedia. Nuestra definición real sobre bases negativas utiliza desde el comienzo la fracción reducida y solo se permite cuando su denominador es impar. Así,

$$
(-8)^{1/3}=-2,
\qquad (-8)^{2/3}=(-2)^2=4.
$$

La escritura no reducida $(-8)^{2/6}$, si se interpreta mediante nuestra convención, debe reducirse primero a $(-8)^{1/3}=-2$. Por el contrario, calcular $\sqrt[6]{(-8)^2}=2$ es una **operación diferente**; sustituir una por otra produciría una igualdad falsa. Antes de aplicar una regla de exponentes, hay que comprobar que ambos lados designan funciones reales en el conjunto considerado.

### Derivada: primero en una base estrictamente positiva

La derivada de una potencia racional se deduce de las raíces construidas y de la regla de la cadena, no de una tabla que todavía no hemos justificado.

::: {#prp-t1-0043}
**Potencias racionales: derivación en su dominio no nulo.** Sea $q=m/n\in\mathbb Q$ su representación reducida, con $n\ge1$.

1. Si $x>0$, la función $x\mapsto x^q$ es diferenciable y
   $$
   \frac{d}{dx}x^q=q\,x^{q-1}.
   $$
2. Si $n$ es impar, la misma conclusión vale para todo $x<0$, con ambas potencias racionales entendidas mediante sus exponentes reducidos y sus raíces reales. Para $q=0$, la función constante $x^0=1$ tiene derivada $0$ en toda la recta. El enunciado no incluye automáticamente la derivabilidad en $x=0$ cuando $q\ne0$.

**Demostración.** El caso $q=0$ está resuelto por la derivada de la función constante. Supongamos $m\ne0$. En un punto $x>0$, pongamos $u=r_n(x)>0$. Por @prp-t1-0042, $r_n$ es diferenciable en $x$ y $r_n'(x)=1/(nu^{n-1})$. La potencia entera $v\mapsto v^m$ es diferenciable en $u$: para $m>0$ por la regla de potencias naturales y para $m<0$ por la regla de potencias enteras negativas del capítulo 7. La regla de la cadena da

$$
\begin{aligned}
\frac{d}{dx}[r_n(x)]^m
&=m u^{m-1}\frac1{nu^{n-1}}\\
&=\frac mn\,u^{m-n}.
\end{aligned}
$$

El exponente $(m-n)/n$ también está reducido, porque $\gcd(|m-n|,n)=\gcd(|m|,n)=1$. Por la definición anterior, $u^{m-n}=x^{(m-n)/n}=x^{q-1}$; se obtiene así la fórmula anunciada.

Si $n$ es impar y $x<0$, elegimos $u=\widetilde r_n(x)<0$. En particular, $u\ne0$, por lo que la potencia entera $u^m$ sigue siendo diferenciable y su derivada es $mu^{m-1}$. La extensión impar posee, por @prp-t1-0042, derivada $1/(nu^{n-1})$ en $x$, ya que $x\ne0$. Aplicando la misma cadena se obtiene $(m/n)u^{m-n}$. La fracción de $q-1$ continúa reducida y su denominador sigue siendo impar, de modo que $u^{m-n}=x^{q-1}$ también tiene significado real. En ningún paso se ha exigido que $u>0$ para la regla de potencias **enteras**; solo se ha exigido $u\ne0$ cuando el exponente es negativo. $\square$
:::

El caso $n=1$ recupera las derivadas enteras previas. Para $q\ne0$, la fórmula se establece en los puntos **no nulos** del dominio correspondiente. Cuando la base es negativa con denominador impar, la potencia $x^{q-1}$ del resultado está igualmente definida, pero su valor no tiene por qué ser positivo: los signos han de obtenerse de la raíz real, no de una interpretación mediante raíces pares.

### La frontera del origen se decide por cocientes

Que una potencia esté definida en cero no significa que la fórmula anterior sea válida allí. Si $m>0$, la función $x^{m/n}$ vale $0$ en ese punto. Para incrementos $h>0$, escribamos $u=r_n(h)>0$. El cociente es exactamente

$$
\frac{h^{m/n}-0}{h}
=\frac{u^m}{u^n}=u^{m-n}.
$$

Si $m>n$, ese cociente tiende a $0$; si $m=n$, vale $1$; y si $0<m<n$, crece sin cota y no define una derivada real finita. Cuando $n$ es par este es todo el estudio relativo admisible en cero. Si $n$ es impar, $h$ también puede aproximarse por la izquierda: escribiendo $h=u^n$ con $u\to0$ de ambos signos, el mismo cociente $u^{m-n}$ demuestra las mismas tres conclusiones respecto de $\mathbb R$. El caso $m=n$ en una fracción reducida solo corresponde a $q=1$. Para $m<0$, cero no pertenece al dominio, de modo que allí no hay derivada de la función definida. Para $m=0$, la derivada en cero es $0$, por constancia.

::: {.callout-important title="El exponente por sí solo no establece el dominio"}
Las expresiones $x^{2/3}$ y $x^{1/2}$ están definidas en $0$, pero ninguna posee allí derivada finita; $x^{3/2}$ sí posee derivada **relativa derecha** igual a $0$ en ese extremo; $x^{-1/3}$ ni siquiera está definida en cero. Es necesario distinguir punto excluido, extremo incluido y punto interior antes de calcular.
:::

En §8.6 retomaremos sistemáticamente estos puntos excepcionales junto con el valor absoluto y las funciones por tramos. Por ahora, la prueba por cocientes ya muestra por qué no podemos sustituir $x=0$ en una fórmula válida únicamente para $x\ne0$.

### Componer exige transportar el dominio

Sea $g:A\to\mathbb R$ una función diferenciable en los puntos que nos interesan, y sea $q\in\mathbb Q$. La expresión $[g(x)]^q$ define una función **solo** en

$$
B=\{x\in A:g(x)\in D_q\}=g^{-1}(D_q).
$$

La continuidad y la derivabilidad relativas de $g$ respecto de $A$ no agregan puntos a $B$. Si $a$ es un punto interior de $A$ y $g(a)\ne0$ pertenece al dominio real de la potencia racional, la regla de la cadena, aplicada donde las composiciones están definidas, proporciona

$$
\frac{d}{dx}[g(x)]^q\bigg|_{x=a}
=q\,[g(a)]^{q-1}g'(a).
$$

Para evitar introducir hipótesis topológicas encubiertas, esta fórmula se afirma aquí con $a$ interior de $A$: la continuidad de $g$ preserva localmente la condición $g(x)>0$, si la necesitamos, o $g(x)<0$ cuando el denominador reducido es impar. Si $a$ es un extremo o un punto de acumulación de un dominio restringido, habrá que formular la versión relativa con su dominio efectivo y verificar separadamente sus incrementos; esa tarea pertenece también a §8.6. Si $g$ es un cociente $P/Q$, se conserva la exclusión $Q(x)=0$ aunque una simplificación algebraica produzca otra expresión sin denominador.

::: {#exm-t1-0087}
**Una composición global, una potencia con signo y un punto prohibido.** Comencemos con

$$
F(x)=(x^2+1)^{3/2},\qquad x\in\mathbb R.
$$

La función interior siempre es positiva. Como $3/2$ está reducido, @prp-t1-0043 y la regla de la cadena permiten derivar en toda la recta:

$$
F'(x)=\frac32(x^2+1)^{1/2}\cdot2x
=3x\sqrt{x^2+1}.
$$

Para $G(x)=(2x-1)^{2/3}$, el denominador reducido es impar y el exponente es positivo: $G$ existe en toda $\mathbb R$, incluso cuando $2x-1<0$. Si $x\ne1/2$, el argumento no se anula y

$$
G'(x)=\frac23(2x-1)^{-1/3}\cdot2
=\frac4{3\sqrt[3]{2x-1}}.
$$

En $x=1/2$ la función está definida, pero el cociente incremental es, para $h\ne0$,

$$
\frac{G(1/2+h)-G(1/2)}h
=\frac{(2h)^{2/3}}h.
$$

Su valor absoluto crece sin cota cuando $h\to0$, pues $(2h)^{2/3}=[\sqrt[3]{2h}]^2=|2h|^{2/3}$; por tanto $G$ no tiene derivada real finita en ese punto.

Finalmente, definamos de manera literal

$$
H(x)=\left(\frac{x^2-1}{x-1}\right)^{-1/2}.
$$

El cociente interior exige $x\ne1$ y coincide con $x+1$ solamente allí. El exponente $-1/2$ exige además una base **estrictamente positiva**. El dominio real de $H$ es, por tanto, $(-1,\infty)\setminus\{1\}$; en él,

$$
H'(x)=-\frac1{2(x+1)^{3/2}}.
$$

Aunque esta expresión derivada tenga sentido al sustituir $x=1$, **$H$ sigue sin estar definida allí**. Podemos construir otra función prolongando la expresión simplificada, pero no alterar retroactivamente el dominio de $H$. El valor $x=-1$ también queda excluido: el exponente negativo requiere dividir por una raíz no nula.
:::

::: {.callout-note title="Control de lectura: antes de derivar"}
Para cada una de las expresiones $(-8)^{2/3}$, $(-8)^{2/6}$, $(-8)^{1/6}$, $x^{3/2}$ en $x=0$ y $((x^2-1)/(x-1))^{-1/2}$ en $x=1$, responde por este orden: ¿cuál es el exponente reducido?, ¿existe la raíz real pertinente?, ¿está permitido el recíproco?, ¿pertenece el punto al dominio de la función original?, ¿se puede aplicar la derivada racional o hay que volver al cociente incremental? Explica asimismo por qué $\sqrt[6]{(-8)^2}$ no puede sustituir a $(-8)^{2/6}$ bajo la convención adoptada.
:::

Hemos ampliado el repertorio sin ampliar arbitrariamente los dominios: las raíces existen por §8.4; las potencias racionales se definen en términos de ellas y de potencias enteras; sus derivadas proceden de @prp-t1-0043 y de la cadena. La §8.6 estudiará con mayor detalle los puntos donde fallan las hipótesis de esas reglas, las funciones con valor absoluto y los empalmes por tramos.

## Puntos excepcionales y funciones por tramos {#sec-t1-c09-06}

### La derivada de una expresión no resuelve sus excepciones

La fórmula obtenida en §8.5 para una potencia racional compuesta requiere que el argumento no se anule en el punto de aplicación. Al encontrar una raíz en cero, un cambio de signo o el punto donde se unen dos tramos, debemos recuperar la definición de derivada. No basta con que cada fórmula sea diferenciable **fuera** del punto excepcional: la derivabilidad se decide comparando los valores de la función original en ese punto y en los puntos que se le aproximan **dentro de su dominio**.

El caso más sencillo ya contiene toda la dificultad. Para $f(x)=|x|$, las expresiones $-x$ si $x<0$ y $x$ si $x>0$ tienen derivadas $-1$ y $1$, respectivamente. Sin embargo, escribir esas dos derivadas no es todavía una prueba sobre $x=0$; la prueba aparece al calcular allí el cociente incremental. En cambio, $x\mapsto |x^3|$ también cambia de expresión en cero y sí resulta diferenciable. La cuestión no es, pues, «¿hay dos tramos?», sino «¿qué límite tienen sus cocientes respecto del valor común?».

### Empalmes: primero el valor, después las pendientes

Supongamos que $a$ es un punto interior de un intervalo $I$ y que una función $f:I\to\mathbb R$ está dada a la izquierda y a la derecha de $a$ por dos reglas. La elección de $f(a)=c$ forma parte de la definición. La continuidad en $a$ exige que los límites de ambos tramos sean precisamente $c$; la igualdad de esos dos límites entre sí no basta si el valor asignado en $a$ es otro.

Cuando se ha comprobado lo anterior, la derivada exige todavía algo distinto: las expresiones

$$
\frac{f(a+h)-c}{h},\qquad h<0\quad\text{y}\quad h>0,
$$

han de converger al **mismo número real finito**. Es exactamente el criterio de derivadas laterales demostrado en @prp-t1-0037, recuperado aquí para analizar empalmes. Si una de las dos derivadas laterales no existe como número real, o si existen pero difieren, no hay derivada bilateral. Si coinciden, su valor común es la derivada. La continuidad, por sí sola, tampoco garantiza esa igualdad.

Podemos comprobarlo directamente: todo incremento no nulo suficientemente pequeño queda a uno de los dos lados de $a$. Si los dos cocientes laterales convergen a $L$, dado $\varepsilon>0$ cada lado proporciona una cota $\delta_-$ o $\delta_+$ para que su cociente diste de $L$ menos de $\varepsilon$. Con $\delta=\min\{\delta_-,\delta_+\}$ la estimación vale para ambos signos de $h$ y, por tanto, para el límite bilateral. Recíprocamente, un límite bilateral restringido a cualquiera de los dos lados conserva su valor. No se ha usado ningún teorema del valor medio.

::: {.callout-important title="Dos pruebas diferentes en un punto de unión"}
**Continuidad:** $\lim_{x\to a^-}f(x)=f(a)=\lim_{x\to a^+}f(x)$. **Derivabilidad:** además, deben coincidir y ser finitos los límites de $[f(a+h)-f(a)]/h$ para $h\to0^-$ y $h\to0^+$. Si uno de los lados no pertenece al dominio, ninguna de estas condiciones debe exigirlo: se trabaja con la continuidad o derivada **relativa al lado disponible**.
:::

La última precisión importa. La raíz cuadrada $r_2:[0,\infty)\to\mathbb R$ solo admite incrementos $h>0$ en cero. La derivada relativa no exige un límite inexistente desde valores negativos: exige que el cociente $\sqrt h/h=1/\sqrt h$ converja a un número real cuando $h\downarrow0$, cosa que no ocurre. En cambio, $x\mapsto x^2$ restringida a $[0,\infty)$ sí tiene derivada relativa $0$ en cero porque $h^2/h=h\to0$ por el único lado permitido. Una derivada relativa en un extremo no se convierte, por ello, en una derivada bilateral de una extensión no especificada.

### El valor absoluto de una función: el cero manda

Sea $u:I\to\mathbb R$ diferenciable en un punto interior $a$ de $I$. Si $u(a)>0$, su continuidad asegura que $u(x)>0$ para todos los $x$ de un entorno suficientemente pequeño de $a$. Allí $|u(x)|=u(x)$; por localidad de la derivada, $D|u|(a)=u'(a)$. Si $u(a)<0$, análogamente $D|u|(a)=-u'(a)$. En ambos casos la derivada se obtiene **después** de probar que el signo permanece fijo, no por dividir formalmente por $|u(a)|$ sin comprobarlo.

¿Y si $u(a)=0$? Para todo incremento admisible $h\ne0$ tenemos la igualdad exacta

$$
\frac{|u(a+h)|-|u(a)|}{h}
=\frac{|h|}{h}\left|\frac{u(a+h)-u(a)}{h}\right|.
$$

Si $u'(a)=0$, el valor absoluto de este cociente tiende a cero. Por tanto, $|u|$ es diferenciable en $a$ y $(|u|)'(a)=0$. Si $u'(a)\ne0$, su valor absoluto tiende a $|u'(a)|>0$, pero el factor $|h|/h$ vale $-1$ por la izquierda y $1$ por la derecha: los cocientes laterales convergen a $-|u'(a)|$ y $|u'(a)|$, respectivamente. No pueden coincidir. Así hemos probado, **en un punto interior donde $u(a)=0$ y $u$ es diferenciable**, el criterio

$$
\boxed{|u|\text{ es diferenciable en }a
\ \Longleftrightarrow\ u'(a)=0;
\qquad (|u|)'(a)=0\text{ en tal caso}.}
$$

Esta conclusión no afirma nada sobre $|u|$ cuando $u$ no es diferenciable en el punto, ni reemplaza el análisis relativo en los extremos del dominio. Por ejemplo, para $u(x)=x$ restringida a $[0,\infty)$, $|u(x)|=x$ y su derivada relativa en cero vale $1$; el criterio bilateral anterior no es aplicable porque cero no es interior de ese dominio.

La comparación entre $|x|$ y $|x^3|$ se vuelve ahora precisa: en cero las derivadas interiores de $u(x)=x$ y $v(x)=x^3$ son $1$ y $0$. El primer valor absoluto no es diferenciable; el segundo sí, con derivada nula. En efecto, de manera independiente,

$$
\frac{|h^3|-|0|}{h}
=\frac{|h|^3}{h}\longrightarrow0,
$$

lo que confirma el resultado sin recurrir a una regla que fuera ilegítima en el punto de anulación.

### Radicales en cero: la cadena puede fallar o quedar restituida

Recordemos de @prp-t1-0042 que $r_n$ no tiene derivada relativa real finita en cero cuando $n\ge2$. Por ello, no podemos aplicar la regla de la cadena a $r_n\circ u$ en un punto $a$ con $u(a)=0$ alegando que conocemos $u'(a)$: falta una de las derivadas requeridas por el teorema. **Esto no prueba que la composición carezca de derivada.** Para decidirlo hay que volver a su cociente, teniendo en cuenta el dominio efectivo $\{x:u(x)\in D_{r_n}\}$.

Concretamente, $x\mapsto\sqrt{x^2}$ está definida en toda la recta e iguala $|x|$; su cociente en cero vale $|h|/h$, cuyos límites laterales son $-1$ y $1$. No hay derivada. En cambio, $x\mapsto\sqrt{x^4}$ está igualmente definida en toda la recta, pero la raíz no negativa de $x^4$ es $x^2$: su cociente en cero es $h^2/h=h$, y su derivada es $0$. Tampoco sería válido concluir que $\sqrt[3]{x^3}$ no es diferenciable en cero porque la raíz cúbica aislada no lo es allí: esta composición coincide con la identidad $x$ y su derivada es $1$.

Estos ejemplos separan dos proposiciones lógicamente distintas: «no se cumplen las hipótesis de una regla de derivación» y «no existe la derivada». La primera solo impide aplicar esa regla. La segunda exige una demostración adicional a partir de la función concreta. Además, la igualdad $\sqrt{x^4}=x^2$ se ha establecido en toda la recta, mientras que simplificar una fracción racional puede cambiar su dominio: tampoco una composición aparentemente reparada autoriza a llenar un punto excluido.

::: {#exm-t1-0088}
**Un radical con esquina, un empalme suave y un hueco que no desaparece.** Analicemos tres funciones, declarando antes sus dominios.

**Primera:** $F:\mathbb R\to\mathbb R$ dada por $F(x)=\sqrt{x^2+x^4}$. El radicando es no negativo para cualquier $x$. Como la raíz cuadrada es no negativa y $1+x^2>0$,

$$
F(x)=|x|\sqrt{1+x^2}\qquad(x\in\mathbb R).
$$

En $x\ne0$ el argumento de la raíz original es positivo, y las reglas ya demostradas dan

$$
F'(x)=\frac{2x+4x^3}{2\sqrt{x^2+x^4}}
=\frac{x+2x^3}{\sqrt{x^2+x^4}}.
$$

No evaluamos esta expresión en cero. Puesto que $F(0)=0$, para $h\ne0$ el cociente exacto es

$$
\frac{F(h)-F(0)}h
=\frac{|h|}{h}\sqrt{1+h^2}.
$$

Por la derecha tiende a $1$ y por la izquierda a $-1$. Así, $F$ es continua en cero —producto de dos funciones continuas—, pero **no** diferenciable allí.

**Segunda:** definimos $G:\mathbb R\to\mathbb R$ por

$$
G(x)=
\begin{cases}
x^2,&x\le0,\\
x^2+x^3,&x>0.
\end{cases}
$$

Ambas expresiones se aproximan a $0=G(0)$ cuando $x\to0$ desde sus respectivos lados: el empalme es continuo. Para $h<0$, su cociente en cero es $G(h)/h=h$; para $h>0$, es $h+h^2$. Los dos tienden a cero. El criterio lateral prueba $G'(0)=0$, además de las derivadas ordinarias $2x$ a la izquierda y $2x+3x^2$ a la derecha de cero. La presencia de dos reglas no crea necesariamente una esquina.

**Tercera:** la función literal

$$
H:\mathbb R\setminus\{1\}\longrightarrow\mathbb R,
\qquad H(x)=\frac{x^2-1}{x-1},
$$

coincide con $x+1$ **solo en su dominio**. No tiene valor, ni continuidad puntual, ni derivada en $x=1$, porque ese punto no pertenece al dominio. Si definimos otra función $\widetilde H:\mathbb R\to\mathbb R$ con $\widetilde H(x)=x+1$, entonces $\widetilde H(1)=2$ y $\widetilde H'(1)=1$. Es una extensión diferenciable de $H$, no una propiedad que el cociente original poseyera ya en su punto excluido.
:::

### Método de inspección en cuatro preguntas

Para una expresión con raíces, signos o tramos, seguiremos este orden: **(i)** fijar el dominio natural o el dominio explícitamente declarado, sin restaurar puntos cancelados; **(ii)** determinar si el punto pertenece al dominio y si es interior, extremo o punto de acumulación con varios lados disponibles; **(iii)** comprobar la continuidad relativa y calcular los cocientes incrementales de cada lado efectivo; **(iv)** aplicar una regla de derivación solamente donde sus hipótesis estén probadas. Si hay extensión, se la denominará como una función nueva.

::: {.callout-note title="Laboratorio breve: clasifica antes de calcular"}
Sin consultar el ejemplo, estudia $A(x)=\sqrt{x^4}$ y $B(x)=\sqrt{x^2}$ en cero: demuestra sus identidades con potencias enteras y calcula ambos cocientes incrementales. Después define una función por tramos que valga $x^2$ para $x<0$, $7$ en $x=0$ y $x^2$ para $x>0$. ¿Coinciden los límites laterales? ¿Es continua? ¿Tiene derivada? Finalmente, explica por qué la función $\sqrt{x}$ definida solo en $[0,\infty)$ no necesita un cociente desde la izquierda en cero, aunque tampoco posea allí derivada relativa finita.
:::

Una vez controlados estos puntos excepcionales, aún queda una precaución anterior a toda derivación inversa: que una derivada no nula en un único punto no construye por sí sola una inversa local. La §8.7 examinará esa diferencia y preparará la elección rigurosa de ramas.

## Una inversa no se deduce de una derivada no nula aislada {#sec-t1-c09-07}

### Lo que afirma una derivada y lo que exige una inversa

En §8.3 demostramos @thm-t1-0031: si una función continua e inyectiva está definida en un intervalo, su inversa existe y es continua sobre la imagen; si además la derivada de la función original en el punto considerado es finita y no nula, entonces podemos derivar la inversa. El orden lógico era importante: **la inyectividad se estableció antes de utilizar la derivada**. ¿Podríamos invertirlo y fabricar la inyectividad únicamente a partir de $f'(a)\ne0$?

Conviene separar tres afirmaciones. Que $f'(a)\ne0$ significa que converge a un número no nulo el cociente de incrementos **con un extremo fijo en $a$**. Que $f$ sea inyectiva en un intervalo $I$ significa que $f(u)\ne f(v)$ siempre que $u,v\in I$ y $u\ne v$: aquí **ambos extremos pueden variar**. Finalmente, disponer de una inversa diferenciable en $f(a)$ requiere primero una inversa bien definida y continua, además de las condiciones de @thm-t1-0031. Ninguna de estas afirmaciones es un mero cambio de notación de otra.

La derivada no nula sí da una información local precisa. Sea $a$ un punto interior del dominio de $f$, y supongamos que existe $c=f'(a)\ne0$. Por definición de límite, existe $\delta>0$ tal que

$$
0<|x-a|<\delta
\quad\Longrightarrow\quad
\left|\frac{f(x)-f(a)}{x-a}-c\right|<\frac{|c|}{2}.
$$

Por la desigualdad triangular inversa, el cociente tiene módulo mayor que $|c|/2$ y, de hecho, el mismo signo que $c$. En particular,

$$
f(x)\ne f(a)
\qquad (0<|x-a|<\delta).
$$

Por consiguiente, $a$ es el único antecedente de **su propio valor** dentro de ese entorno. Para $c>0$, además, los valores inmediatamente a la izquierda de $a$ son menores que $f(a)$ y los de la derecha son mayores; si $c<0$, se invierten esas desigualdades. Nada de ello compara $f(u)$ y $f(v)$ cuando $u$ y $v$ son dos puntos próximos **distintos de $a$**. Ahí se encuentra la brecha que debemos examinar.

### Un contraejemplo: pliegues que se aproximan al origen

Construiremos una función continua en toda la recta con derivada $1$ en cero, pero cuya restricción a ningún intervalo abierto que contenga cero es inyectiva. El mecanismo será elemental: añadiremos a la identidad pequeñas elevaciones triangulares, cada vez más cercanas a cero. Su altura será insignificante respecto de su distancia al origen, aunque su pendiente descendente sea lo bastante pronunciada para que la función repita valores.

Para cada entero $n\ge2$, definamos

$$
a_n=2^{-n},\qquad
w_n=\frac{a_n^3}{100},\qquad
h_n=\frac{a_n^2}{100},\qquad
I_n=[a_n,a_n+2w_n].
$$

Los intervalos $I_n$ son disjuntos. En efecto, $a_{n+1}=a_n/2$ y

$$
a_{n+1}+2w_{n+1}
=a_{n+1}\left(1+\frac{2a_{n+1}^2}{100}\right)
<2a_{n+1}=a_n.
$$

Como $a_n\to0$, estos intervalos se acumulan exclusivamente en cero. Sobre cada uno definamos una tienda triangular que sube desde $0$ hasta una altura $h_n$ y vuelve a bajar a $0$:

$$
p_n(x)=
\begin{cases}
\dfrac{h_n}{w_n}(x-a_n),&a_n\le x\le a_n+w_n,\\[4pt]
\dfrac{h_n}{w_n}(a_n+2w_n-x),&a_n+w_n\le x\le a_n+2w_n.
\end{cases}
$$

Las fórmulas coinciden en la cima, pues ambas dan $h_n$. Ahora definamos una sola función $p:\mathbb R\to\mathbb R$ poniendo $p(x)=p_n(x)$ si $x\in I_n$ para algún $n\ge2$, y $p(x)=0$ fuera de la unión de los intervalos. No hay conflicto de definiciones porque estos son disjuntos; en sus extremos, la tienda vale cero y empalma con la función exterior. Finalmente, sea

$$
f:\mathbb R\longrightarrow\mathbb R,
\qquad f(x)=x+p(x).
$$

**Primera verificación: continuidad.** En el interior de cada semibase $p$ es afín y, en las cimas y extremos de las tiendas, los valores laterales coinciden. En cualquier punto distinto de cero hay un entorno que corta, a lo sumo, un número finito de tiendas; de hecho, todas salvo un número finito quedan cerca de cero. Por eso $f$ es continua fuera del origen. En el origen tenemos $p(0)=0$. Si $x\in I_n$, entonces $0\le p(x)\le h_n$, y fuera de los intervalos $p(x)=0$. Cuando $x\to0$ a través de estas tiendas, sus índices necesariamente tienden a infinito y $h_n\to0$; por tanto, $p(x)\to0$. Concluimos que $f$ es continua también en cero.

**Segunda verificación: la derivada en el origen.** Si $x\in I_n$, se cumple $x\ge a_n>0$ y, por tanto,

$$
0\le\frac{p(x)}{x}
\le\frac{h_n}{a_n}
=\frac{a_n}{100}
\longrightarrow0
\qquad(n\to\infty).
$$

Fuera de las tiendas, $p(x)/x=0$ para $x\ne0$. Estas dos observaciones, junto con que las tiendas se acumulan solo en cero, dan $\lim_{x\to0}p(x)/x=0$. Como $f(0)=0$,

$$
\boxed{f'(0)=\lim_{x\to0}\frac{f(x)-f(0)}{x}
=\lim_{x\to0}\left(1+\frac{p(x)}{x}\right)=1.}
$$

Se trata de una derivada bilateral: para $x<0$ la función coincide exactamente con $x$, y el mismo límite vale por ambos lados.

**Tercera verificación: ninguna restricción alrededor de cero es inyectiva.** En la mitad ascendente de $I_n$, $f$ tiene pendiente algebraica

$$
1+\frac{h_n}{w_n}=1+\frac1{a_n}>0,
$$

mientras que, en la mitad descendente, su pendiente es

$$
1-\frac{h_n}{w_n}=1-\frac1{a_n}<0.
$$

No utilizamos aquí un teorema diferencial de monotonía: estas pendientes son simplemente los coeficientes de dos **expresiones afines**. Los valores en los extremos y en la cima son

$$
\begin{aligned}
f(a_n)&=a_n,\\
f(a_n+w_n)&=a_n+w_n+h_n,\\
f(a_n+2w_n)&=a_n+2w_n.
\end{aligned}
$$

Como $h_n>w_n$ (pues $0<a_n<1$), el valor en la cima supera al del extremo derecho. Elijamos un número $c_n$ estrictamente comprendido entre estos dos valores. La mitad ascendente recorre desde $a_n$ hasta el valor máximo, y la mitad descendente recorre desde el máximo hasta $a_n+2w_n$. Por continuidad —o despejando en las expresiones afines— existen dos puntos distintos, uno en cada mitad, con imagen $c_n$.

Dado cualquier $\delta>0$, podemos tomar $n$ tan grande que $I_n\subset(0,\delta)$. Esos dos puntos pertenecen entonces a $(-\delta,\delta)$ y tienen la misma imagen. **No existe ningún entorno intervalar de cero en el que $f$ sea inyectiva**, a pesar de ser continua en toda $\mathbb R$ y satisfacer $f'(0)=1$.

::: {.callout-important title="Lo que demuestra exactamente el contraejemplo"}
La función construida es continua en toda la recta y diferenciable en $0$ con derivada no nula; no afirmamos que sea diferenciable en las cimas y extremos de las tiendas. El ejemplo refuta la inferencia basada en la derivada **en un solo punto**. No contradice un eventual teorema que impusiera hipótesis adicionales en todo un entorno: ese es otro enunciado y pertenece al desarrollo posterior de la teoría diferencial.
:::

### El caso opuesto: una derivada nula no elimina una inversa

Tampoco es legítima la afirmación recíproca «si $f'(a)=0$, entonces $f$ no tiene inversa». Para la función

$$
q:\mathbb R\longrightarrow\mathbb R,
\qquad q(x)=x^3,
$$

si $u<v$, la identidad

$$
v^3-u^3=(v-u)(v^2+uv+u^2)>0
$$

prueba su crecimiento estricto: el primer factor es positivo y el segundo también, porque $v^2+uv+u^2=(u+v/2)^2+3v^2/4$ solo se anula cuando $u=v=0$, imposible si $u<v$. La continuidad polinómica, el teorema de los valores intermedios y los valores de $q$ en enteros positivos y negativos muestran que su imagen es toda $\mathbb R$. Por tanto, $q$ es biyectiva y su inversa $q^{-1}(y)=\sqrt[3]{y}$ existe y es continua por @thm-t1-0023. Pero $q'(0)=0$.

La inversa no tiene derivada real finita en el origen: para $y\ne0$,

$$
\frac{q^{-1}(y)-q^{-1}(0)}{y}
=\frac{\sqrt[3]{y}}{y}
=\frac1{(\sqrt[3]{y})^2}
\longrightarrow+\infty
\qquad(y\to0).
$$

Aquí la inversa **existe y es continua**, pero la condición $q'(0)\ne0$ de @thm-t1-0031 no se cumple y su conclusión de diferenciabilidad tampoco. Hay una distinción más precisa: **si una función y su inversa son ambas derivables con derivadas finitas en puntos correspondientes, la derivada de la primera no puede anularse**. En efecto, aplicada *después* de haber demostrado ambas derivabilidades, la regla de la cadena a $q^{-1}\circ q=\operatorname{id}$ da $1=(q^{-1})'(q(a))q'(a)$. Esta observación no prueba la derivabilidad de la inversa: solo comprueba una condición necesaria cuando ya se la conoce.

::: {#exm-t1-0089}
**Tres diagnósticos que no deben confundirse.** Compara las siguientes situaciones antes de intentar utilizar una fórmula de derivación inversa.

**(a) Derivada no nula, sin inversa local.** La función $f=x+p$ construida arriba cumple $f'(0)=1$, pero sus tiendas repiten valores en cualquier entorno del origen. No tiene inversa como función sobre la imagen de ninguna restricción a un intervalo abierto que contenga cero.

**(b) Inversa existente, derivada original nula.** La función $q(x)=x^3$ es una biyección continua de $\mathbb R$ sobre $\mathbb R$ y $q'(0)=0$. La inversa existe y es continua, pero no es derivable con derivada finita en cero.

**(c) Inversa existente y fórmula justificada.** La función $r(x)=x^3+x$ es continua; para $u<v$,

$$
r(v)-r(u)=(v-u)(v^2+uv+u^2+1)>0.
$$

La inyectividad proviene de esta desigualdad **algebraica**. La imagen es toda $\mathbb R$ por continuidad y los valores $r(N)>M$ y $r(-N)<-M$ para enteros $N$ suficientemente grandes y cualquier $M>0$. Su inversa $s$ existe y es continua; dado que $r'(0)=1$, @thm-t1-0031 autoriza $s'(0)=1/r'(0)=1$. Advertencia: haber calculado únicamente $r'(0)=1$ no habría demostrado la inyectividad necesaria.
:::

### Leer el teorema en la dirección correcta

Podemos condensar lo aprendido sin atribuir a una condición más de lo que afirma:

$$
\boxed{
\begin{gathered}
f:I\to\mathbb R\text{ continua e inyectiva},\quad J=f(I),\quad a\in I\text{ de acumulación},\quad f'_I(a)\ne0
\\[2pt]
\Longrightarrow\quad
(f^{-1})'_J(f(a))=\frac1{f'_I(a)}.
\end{gathered}}
$$

La primera línea no se obtiene de la tercera hipótesis; debe acreditarse por su cuenta. La segunda condición sobre la derivada es **suficiente para derivar una inversa ya existente**, no necesaria para que la inversa exista. Si solo conocemos $f'(a)\ne0$, podemos separar $f(a)$ de los valores vecinos, pero no excluir coincidencias $f(u)=f(v)$ con $u\ne v$ cerca de $a$.

::: {.callout-note title="Laboratorio de transferencia: prueba o contraejemplo"}
Explica qué cuantificadores cambian entre «$f(x)\ne f(a)$ para $x\ne a$ suficientemente próximo» e «inyectividad en un entorno». Para $q(x)=x^3$, identifica cuál de las tres tareas —existencia de inversa, continuidad de inversa, derivabilidad de inversa en cero— fracasa. Finalmente, sustituye en la construcción triangular $h_n$ por $w_n/2$: ¿cuál sería entonces la pendiente afín en el tramo descendente? ¿Seguiría funcionando *esta* prueba de la falta de inyectividad? Justifica sin invocar el teorema del valor medio.
:::

La necesidad de **seleccionar y demostrar una función** se volverá todavía más visible al abordar ecuaciones polinómicas con dos variables. Una relación puede contener varias gráficas y una misma ecuación puede admitir ramas que se cruzan. En §8.8 distinguiremos el conjunto de soluciones de una rama particular y prepararemos un argumento algebraico que permita estudiar después su derivada sin suponerla de antemano.

## Relaciones polinómicas y ramas {#sec-t1-c09-08}

### La ecuación describe pares; la rama asigna valores

Hasta ahora hemos invertido funciones *ya definidas*: antes de calcular la derivada de una inversa debíamos justificar la inyectividad de la función original. Una ecuación en dos letras plantea un problema anterior todavía más elemental. Si escribimos

$$
F(x,y)=0,
$$

¿qué significa «derivar $y$»? La ecuación, por sí sola, no nos ha dado una función de $x$. Primero fija un conjunto de pares; puede no contener ninguno sobre cierto valor de $x$, contener varios o permitir distintas elecciones de un valor para cada entrada.

Llamaremos aquí **polinomio en dos variables** a una expresión finita de la forma

$$
F(x,y)=\sum_{(i,j)\in E}c_{ij}x^i y^j,
\qquad c_{ij}\in\mathbb R,
$$

con $E$ un conjunto finito de pares de enteros no negativos. Como es habitual en un polinomio, la potencia de exponente cero representa el factor constante $1$; esto no introduce una operación aislada $0^0$. El polinomio determina una función $F:\mathbb R^2\to\mathbb R$, pero su ecuación de ceros todavía no asigna una salida única a cada primera coordenada.

::: {#def-t1-0046}
**Conjunto de ceros y rama de una relación polinómica.** Sea $F$ un polinomio real en dos variables. Su **conjunto de ceros** es

$$
Z_F=\{(x,y)\in\mathbb R^2:F(x,y)=0\}.
$$

Una **rama de la relación sobre un intervalo** $I\subseteq\mathbb R$ es una función especificada $\varphi:I\to\mathbb R$ cuya gráfica está contenida en $Z_F$; es decir,

$$
F(x,\varphi(x))=0\qquad\text{para todo }x\in I.
$$

Diremos que la rama *pasa por* $(a,b)$ si $a\in I$ y $\varphi(a)=b$. La llamaremos **rama continua en $a$** únicamente cuando se haya demostrado, además, que $\varphi(x)\to b$ al tender $x$ a $a$ relativamente a $I$ (o la condición habitual de continuidad si $a$ es aislado). Ni la definición de rama ni la inclusión de su gráfica en $Z_F$ presuponen diferenciabilidad.
:::

El objeto $Z_F$ y la función $\varphi$ tienen tipos diferentes: el primero es un subconjunto de $\mathbb R^2$; la segunda tiene un dominio $I$, un valor preciso para cada $x\in I$ y una gráfica que es *parte* de aquel conjunto. Una ecuación no selecciona su rama; incluso conocer un punto $(a,b)\in Z_F$ puede dejar abiertas varias elecciones de rama por ese mismo punto. Para hablar de $\varphi'(a)$ habrá que acreditar, además, que $a$ es un punto de acumulación del dominio y que converge el cociente incremental correspondiente.

### Un cruce: varias ramas, diferentes derivadas

La relación

$$
y^2=x^2
$$

se factoriza en $(y-x)(y+x)=0$. Por la propiedad del producto nulo, su conjunto de ceros es la unión de dos rectas. La factorización describe las posibilidades, pero no impone una sola función sobre toda la recta.

::: {#exm-t1-0090}
**Tres elecciones sobre la misma ecuación.** Consideremos

$$
F(x,y)=y^2-x^2,
\qquad
Z_F=\{(x,x):x\in\mathbb R\}\cup\{(x,-x):x\in\mathbb R\}.
$$

Las aplicaciones

$$
\varphi_+(x)=x,\qquad
\varphi_-(x)=-x,\qquad
\psi(x)=|x|,
\qquad x\in\mathbb R,
$$

son tres ramas genuinas: para cada una, $F(x,\varphi(x))=0$ en todo su dominio. Son continuas y pasan por $(0,0)$. No obstante, las dos primeras tienen derivadas distintas,

$$
\varphi_+'(0)=1,\qquad\varphi_-'(0)=-1,
$$

mientras que la tercera **no tiene derivada en cero**, pues para $h\ne0$

$$
\frac{\psi(h)-\psi(0)}{h}=\frac{|h|}{h}
=\begin{cases}1,&h>0,\\-1,&h<0.\end{cases}
$$

La misma ecuación y el mismo punto permiten, por tanto, ramas continuas con derivadas diferentes e incluso una rama continua no diferenciable. El defecto no está en la ecuación: falta seleccionar la función sobre la que hacemos una afirmación diferencial. La elección $\psi$ combina por tramos las dos rectas y muestra por qué tampoco basta pedir «una rama continua» para obtener automáticamente una derivada.
:::

Es instructivo intentar «derivar $y^2=x^2$» como si $y$ fuese ya una función diferenciable. Aparecería $2y\,y'=2x$, pero en $(0,0)$ esta igualdad se reduce a $0=0$ y no determina $y'$. Tampoco demuestra que $y'$ exista para la rama $|x|$. La manipulación solo podría ser una **comprobación posterior**, una vez elegida una rama y establecida su diferenciabilidad por un argumento independiente. Vamos a preparar precisamente ese argumento.

### Una identidad algebraica exacta, sin derivadas implícitas

Necesitamos separar el cambio de $F$ en dos contribuciones: una producida por variar la primera coordenada y otra por variar la segunda. No recurriremos a un teorema de varias variables ni a derivadas parciales. La factorización de las diferencias de potencias basta para obtener una identidad **exacta**, válida para todo par $(x,y)$.

::: {#lem-t1-0003}
**Descomposición polinómica por telescopado.** Sean $F$ un polinomio real en dos variables y $(a,b)\in\mathbb R^2$. Existen polinomios $A_{a,b}$ y $B_{a,b}$ tales que, para todos $x,y\in\mathbb R$,

$$
\boxed{F(x,y)-F(a,b)
=(x-a)A_{a,b}(x,y)+(y-b)B_{a,b}(x,y).}
$$

Aunque la pareja completa de polinomios de una descomposición no tiene por qué ser única, los dos números $A_{a,b}(a,b)$ y $B_{a,b}(a,b)$ **son independientes de la descomposición**. Se calculan algebraicamente a partir de los monomios de $F$.

**Demostración.** Para cada monomio $x^i y^j$, sumamos y restamos $a^i y^j$:

$$
\begin{aligned}
x^i y^j-a^i b^j
&=(x^i-a^i)y^j+a^i(y^j-b^j)\\
&=(x-a)\left(\sum_{k=0}^{i-1}x^{i-1-k}a^k\right)y^j
 +(y-b)a^i\left(\sum_{\ell=0}^{j-1}y^{j-1-\ell}b^\ell\right).
\end{aligned}
$$

Si $i=0$ o $j=0$, la suma correspondiente se interpreta como vacía y vale cero. Multiplicamos cada igualdad por $c_{ij}$ y sumamos el número finito de monomios de $F$. Obtenemos, por ejemplo,

$$
\begin{aligned}
A_{a,b}(x,y)
&=\sum_{(i,j)\in E\atop i\ge1}
 c_{ij}\left(\sum_{k=0}^{i-1}x^{i-1-k}a^k\right)y^j,\\[3pt]
B_{a,b}(x,y)
&=\sum_{(i,j)\in E\atop j\ge1}
 c_{ij}a^i\left(\sum_{\ell=0}^{j-1}y^{j-1-\ell}b^\ell\right),
\end{aligned}
$$

que son polinomios y satisfacen la identidad requerida. En particular, al evaluarlos en $(a,b)$, cada suma interior consta de tantas copias del mismo monomio como indica su índice:

$$
\begin{aligned}
A_{a,b}(a,b)&=\sum_{(i,j)\in E\atop i\ge1}i\,c_{ij}a^{i-1}b^j,\\
B_{a,b}(a,b)&=\sum_{(i,j)\in E\atop j\ge1}j\,c_{ij}a^i b^{j-1}.
\end{aligned}
$$

Para comprobar que los *valores* no dependen de esta elección, supongamos que otra pareja de polinomios $\widetilde A,\widetilde B$ cumple la misma identidad. Fijando $y=b$ y tomando $x\ne a$ resulta

$$
\widetilde A(x,b)=\frac{F(x,b)-F(a,b)}{x-a}.
$$

El lado derecho es igual a $A_{a,b}(x,b)$ por nuestra identidad. Como ambos son polinomios continuos en $x$, al pasar al límite $x\to a$ obtenemos $\widetilde A(a,b)=A_{a,b}(a,b)$. Del mismo modo, fijando $x=a$ y haciendo $y\to b$ se obtiene $\widetilde B(a,b)=B_{a,b}(a,b)$. Esto prueba la independencia anunciada. De hecho, si $H$ es cualquier polinomio, reemplazar $A_{a,b}$ por $A_{a,b}+(y-b)H$ y $B_{a,b}$ por $B_{a,b}-(x-a)H$ conserva la identidad, pero no cambia sus valores en $(a,b)$. $\square$
:::

**Lectura de la demostración.** La suma y resta de $a^i y^j$ separa el efecto de modificar $x$ del de modificar $y$; la factorización de potencias extrae los factores $x-a$ e $y-b$. Así aparece una identidad válida **antes** de decidir si hay una rama, si es continua o si admite derivada. Los números $A_{a,b}(a,b)$ y $B_{a,b}(a,b)$ tienen una expresión formal semejante a la derivación de un polinomio con la otra letra fija, pero en esta sección solo usamos álgebra de polinomios y continuidad de funciones de una variable.

### Qué información queda preparada para una rama continua

Consideremos primero la circunferencia ya presentada en §8.1,

$$
F(x,y)=x^2+y^2-1.
$$

En torno a $(a,b)=(0,1)$, su telescopado exacto es

$$
F(x,y)-F(0,1)
=x(x+0)+(y-1)(y+1),
$$

por lo que podemos escoger $A_{0,1}(x,y)=x$ y $B_{0,1}(x,y)=y+1$. De aquí se obtienen los números **verificados**, no supuestos,

$$
A_{0,1}(0,1)=0,\qquad B_{0,1}(0,1)=2\ne0.
$$

La rama superior $\varphi(x)=\sqrt{1-x^2}$, definida en $I=(-1,1)$, está construida con una raíz existente; es continua en $0$ y satisface $\varphi(0)=1$ y $F(x,\varphi(x))=0$. Su continuidad, junto a la de los polinomios de una variable, permitirá controlar los coeficientes del telescopado cuando $x\to0$. **Aún no hemos supuesto que $\varphi$ sea diferenciable**: esa será la conclusión por demostrar en §8.9.

En el cruce del ejemplo, en cambio, $F(x,y)=y^2-x^2$ admite la descomposición

$$
F(x,y)-F(a,b)=-(x-a)(x+a)+(y-b)(y+b),
$$

así que $A_{0,0}(0,0)=B_{0,0}(0,0)=0$. No hay un coeficiente no nulo ante el incremento de $y$ que permita despejar un cociente incremental. La diferencia entre ambos casos no autoriza a declarar que las ramas del cruce carecen de derivada: dos sí la tienen, y otra no, como acabamos de probar.

::: {.callout-note title="Antes de derivar una relación"}
Para $F(x,y)=y^2-x^2$, escribe el conjunto $Z_F$ y las gráficas de $\varphi_+$ y $\psi$ como conjuntos de pares: identifica qué objetos son iguales y cuáles solo están contenidos unos en otros. Después reproduce sin consultar el lema el telescopado de $F(x,y)=x^2+xy+y^2-1$ alrededor de $(a,b)$: comprueba la identidad sustituyendo y determina $A_{a,b}(a,b)$ y $B_{a,b}(a,b)$. Por último, explica por qué conocer $F(a,b)=0$ no demuestra la existencia de una rama continua que pase por $(a,b)$.
:::

Hemos establecido el orden lógico que faltaba: **relación → elección y existencia de la rama → continuidad de la rama → identidad de telescopado**. En §8.9 añadiremos una condición algebraica explícita, $B_{a,b}(a,b)\ne0$, y demostraremos directamente mediante el cociente incremental que esa rama continua es diferenciable en $a$. No obtendremos de esa condición la existencia general de ramas; tal afirmación pertenece a una teoría posterior.

## Derivación implícita polinómica sin circularidad {#sec-t1-c09-09}

### La pendiente debe ser una conclusión

En §8.8 construimos el conjunto de ceros de un polinomio, distinguimos sus ramas como funciones y demostramos una identidad de telescopado. Ahora queremos saber si una rama continua admite derivada. Para la circunferencia, la rama superior ya está definida por $\varphi(x)=\sqrt{1-x^2}$ cerca de $0$, pero no vamos a introducir su derivada en la hipótesis ni a escribir de entrada $2x+2\varphi(x)\varphi'(x)=0$: esa igualdad, obtenida por la regla de la cadena, solo sería legítima después de saber que $\varphi'$ existe.

La pregunta correcta es: **¿cuándo permite la ecuación demostrar la convergencia del cociente incremental de una rama continua?** La respuesta requiere que el coeficiente algebraico situado ante el cambio de la segunda coordenada no se anule en el punto. La continuidad garantizará que podamos dividir por él cerca del punto, y no antes.

::: {#thm-t1-0032}
**Derivación implícita de una rama polinómica continua.** Sean $F\in\mathbb R[X,Y]$, $I\subseteq\mathbb R$ un intervalo, $a\in I$ un punto de acumulación de $I$ y $b\in\mathbb R$ con $F(a,b)=0$. Supongamos que **ya se ha especificado** una función $\varphi:I\to\mathbb R$ tal que

$$
\varphi(a)=b,\qquad F(x,\varphi(x))=0\quad(x\in I),
$$

y que $\varphi$ es continua en $a$, con respecto al dominio $I$. Sean $A_{a,b}$ y $B_{a,b}$ dos polinomios que satisfacen la descomposición de @lem-t1-0003:

$$
F(x,y)-F(a,b)
=(x-a)A_{a,b}(x,y)+(y-b)B_{a,b}(x,y).
$$

Si

$$
B_{a,b}(a,b)\ne0,
$$

entonces $\varphi$ tiene derivada relativa **finita** en $a$, y

$$
\boxed{\displaystyle
\varphi'_I(a)=-\frac{A_{a,b}(a,b)}{B_{a,b}(a,b)}.}
$$

La fórmula no depende de la descomposición escogida. El teorema no afirma la existencia de la rama a partir de $F(a,b)=0$.

**Demostración.** Por @lem-t1-0003, para cada $x\in I$ podemos sustituir $y=\varphi(x)$ en la identidad exacta. Como $F(x,\varphi(x))=F(a,b)=0$ y $\varphi(a)=b$, obtenemos

$$
0=(x-a)A_{a,b}(x,\varphi(x))
 +(\varphi(x)-b)B_{a,b}(x,\varphi(x)).
$$

Pongamos $\beta=B_{a,b}(a,b)\ne0$. Las funciones de una variable $x\mapsto A_{a,b}(x,\varphi(x))$ y $x\mapsto B_{a,b}(x,\varphi(x))$ son sumas finitas de productos de funciones continuas en $a$; esto se deduce de las reglas de continuidad ya demostradas, sin invocar teoría multivariable. En particular,

$$
B_{a,b}(x,\varphi(x))\longrightarrow\beta
\qquad(x\to a,\ x\in I).
$$

Por la definición de límite, existe $\delta>0$ tal que, si $x\in I$ y $|x-a|<\delta$, entonces

$$
\left|B_{a,b}(x,\varphi(x))-\beta\right|
<\frac{|\beta|}{2}.
$$

La desigualdad triangular inversa implica la cota concreta

$$
\left|B_{a,b}(x,\varphi(x))\right|
>\frac{|\beta|}{2}>0.
$$

Ahora, y solamente ahora, podemos despejar para $x\in I$ con $0<|x-a|<\delta$:

$$
\frac{\varphi(x)-\varphi(a)}{x-a}
=-\frac{A_{a,b}(x,\varphi(x))}
        {B_{a,b}(x,\varphi(x))}.
$$

La continuidad de $\varphi$ y de $A_{a,b}$ da $A_{a,b}(x,\varphi(x))\to A_{a,b}(a,b)$; la del denominador, junto con $\beta\ne0$, permite aplicar las leyes de límites de cocientes. Así,

$$
\lim_{\substack{x\to a\\x\in I,\ x\ne a}}
\frac{\varphi(x)-\varphi(a)}{x-a}
=-\frac{A_{a,b}(a,b)}{B_{a,b}(a,b)}\in\mathbb R.
$$

El punto de acumulación garantiza que el límite corresponde a incrementos admisibles no vacíos; por definición, es la derivada relativa de $\varphi$ en $a$. El último enunciado sobre independencia procede también de @lem-t1-0003: aunque puedan variar los polinomios $A,B$, sus valores en $(a,b)$ no varían. $\square$
:::

### Lectura de la prueba: dónde entra cada hipótesis

No hemos derivado una igualdad que contuviera una función de regularidad desconocida. La identidad del lema ya era válida para todos los pares $(x,y)$; la **existencia de la rama** permitió sustituir $y=\varphi(x)$; su **continuidad** hizo converger los dos coeficientes a sus valores en $(a,b)$; la **no anulación** de $B_{a,b}(a,b)$ aportó un denominador legítimo; y solo el límite del cociente produjo la **derivada**, como conclusión. El argumento funciona también en un extremo de $I$, pero allí la derivada es relativa a $I$, no una derivada bilateral sobre un dominio inexistente.

En el volumen I de *A Course in Analysis*, Jacob y Evans presentan, para la derivada de una función **inversa**, un cálculo motivador por regla de la cadena, advierten que requiere cautelas y aplazan su prueba completa [@jacob-evans-analysis-v1, cap. 7, teorema 7.5, pp. 111–112]. Ese pasaje sirve aquí como **control metodológico**, no como fuente de un teorema implícito que el libro no haya establecido: una identidad diferencial formal puede orientar una fórmula, pero no demostrar que existe la derivada que aparece en ella. Nuestra deducción usa directamente el cociente incremental.

### Circunferencia: una rama construida y una derivada demostrada

::: {#exm-t1-0091}
**La rama superior cerca de $(0,1)$.** Consideremos

$$
F(x,y)=x^2+y^2-1,
\qquad I=(-1,1),
\qquad \varphi(x)=\sqrt{1-x^2}.
$$

El radicando es positivo en $I$, de modo que la raíz no negativa existe por los resultados previos; $\varphi:I\to\mathbb R$ es una función continua, satisface $F(x,\varphi(x))=0$ y $\varphi(0)=1$. En §8.8 se obtuvo la identidad

$$
F(x,y)-F(a,b)=(x-a)(x+a)+(y-b)(y+b),
$$

por lo que $A_{a,b}(x,y)=x+a$ y $B_{a,b}(x,y)=y+b$. Para cualquier $a\in I$, pongamos $b=\varphi(a)>0$. Entonces $B_{a,b}(a,b)=2b>0$; el teorema garantiza la derivabilidad en $a$, sin haberla supuesto, y proporciona

$$
\boxed{\displaystyle
\varphi'(a)=-\frac{2a}{2b}
=-\frac{a}{\sqrt{1-a^2}}\qquad(-1<a<1).}
$$

En particular, $\varphi'(0)=0$. En $a=1/2$, donde $b=\sqrt3/2$, obtenemos $\varphi'(1/2)=-1/\sqrt3$.

**Control independiente del valor en cero.** Racionalizando el cociente, para $0\ne h\in(-1,1)$ se tiene

$$
\frac{\sqrt{1-h^2}-1}{h}
=\frac{-h}{\sqrt{1-h^2}+1}\longrightarrow0.
$$

Esta verificación no reemplaza el teorema: comprueba un punto particular de la fórmula obtenida para todos los puntos interiores de la rama.
:::

La ecuación de la circunferencia **no** produce, en torno a $(1,0)$, una rama real $y(x)$ definida sobre un intervalo abierto que contenga $x=1$: cualquier intervalo de ese tipo contiene $x>1$, para el que $y^2=1-x^2<0$ no tiene solución real. La rama superior sí está definida sobre $[-1,1]$, pero $B_{1,0}(1,0)=0$, de modo que el teorema no se aplica en el extremo. Su cociente relativo muestra además que allí no tiene derivada finita:

$$
\frac{\sqrt{1-x^2}-0}{x-1}
=-\sqrt{\frac{1+x}{1-x}}\longrightarrow-\infty
\qquad(x\uparrow1).
$$

**No aplicación** y **ausencia de derivada** son, sin embargo, afirmaciones distintas: aquí la segunda se ha probado aparte.

### Condición suficiente, condición necesaria y conversas falsas

Supongamos ahora que una rama $\varphi$ ya es diferenciable en $a$ y satisface $F(x,\varphi(x))=0$. Las fórmulas polinómicas que obtuvimos en §8.8 para $A_{a,b}(a,b)$ y $B_{a,b}(a,b)$ permiten, mediante las reglas de derivación de los capítulos 6 y 7, diferenciar **a posteriori** la composición polinómica: el resultado necesario es

$$
A_{a,b}(a,b)+B_{a,b}(a,b)\varphi'_I(a)=0.
$$

Se puede obtener sin introducir derivadas parciales: para cada monomio $x^i\varphi(x)^j$ se aplican las reglas del producto y de la cadena ya demostradas, y se suman los términos finitos. Cuando $B_{a,b}(a,b)\ne0$, la ecuación determina el mismo valor del teorema; cuando $B_{a,b}(a,b)=0$, **no permite despejar** y no decide por sí sola si la derivada existe. Esta identidad es una *consecuencia necesaria bajo diferenciabilidad previa*, no nuestra demostración de tal diferenciabilidad.

La no degeneración tampoco es necesaria para que una rama particular tenga derivada. En la relación $F(x,y)=y^2-x^3$, la función ya construida $\psi:[0,\infty)\to\mathbb R$, $\psi(x)=x^{3/2}$, es una rama continua por $(0,0)$ y satisface $\psi(x)^2=x^3$. El telescopado da $B_{0,0}(0,0)=0$, pero, para $x>0$,

$$
\frac{\psi(x)-\psi(0)}{x-0}=\sqrt{x}\longrightarrow0,
$$

por lo que $\psi'_{[0,\infty)}(0)=0$. En el cruce $y^2=x^2$ de §8.8, el mismo coeficiente se anula y hay ramas derivables de pendientes distintas y una rama continua no derivable. Por tanto, $B(a,b)=0$ no demuestra ninguna de esas alternativas; exige estudiar la rama elegida por otros medios.

::: {.callout-important title="Lo que el teorema demuestra — y lo que no"}
De **rama existente + continuidad en $a$ + $B(a,b)\ne0$** se deducen diferenciabilidad en $a$ y fórmula de la derivada. Ni $F(a,b)=0$ ni la desigualdad $B(a,b)\ne0$, tomadas como únicas hipótesis de este resultado, constituyen aquí una demostración de existencia local de rama. Tampoco convertimos la condición suficiente $B(a,b)\ne0$ en una caracterización de todas las ramas diferenciables. La cuestión general de existencia local y unicidad pertenece al futuro teorema implícito del Tomo III.
:::

::: {.callout-note title="Transferencia: reconstruye la prueba, no la fórmula"}
Para $F(x,y)=x^2+xy+y^2-1$ y un punto $(a,b)$ de su conjunto de ceros, utiliza las fórmulas del lema para obtener $A_{a,b}(a,b)=2a+b$ y $B_{a,b}(a,b)=a+2b$. Formula con precisión qué **dato sobre la rama** debe aportarse antes de aplicar el teorema y qué condición algebraica adicional permite concluir $\varphi'_I(a)=-(2a+b)/(a+2b)$. Explica después por qué esta expresión no tiene significado como «la pendiente de la ecuación» si no se ha identificado una función $\varphi$. Como segunda comprobación, explica por qué en la cúspide $y^2=x^3$ no es lícito concluir «no existe derivada» a partir de $B(0,0)=0$.
:::

La derivación implícita queda así fundada en un límite verificable. En §8.10 organizaremos las mismas distinciones en un laboratorio de curvas: circunferencia, cruce, punto singular y parametrización restringida, sin ampliar las hipótesis del teorema ni importar resultados multivariables.

## Laboratorio P3: leer una curva antes de derivarla {#sec-t1-c09-10}

### Una ecuación no indica por sí sola qué función estamos estudiando

Una expresión como $x^2+y^2=1$ puede reconocerse geométricamente antes de decidir qué función representa. Pero un conjunto de puntos y una función real no son el mismo objeto. En este laboratorio recorreremos ocho estaciones, usando exclusivamente las construcciones y demostraciones de §§8.1–8.9. La meta no es acumular fórmulas: es **reconstruir las decisiones que hacen legítimo cada cociente incremental**.

Las tres relaciones de referencia serán

$$
\begin{aligned}
C&=\{(x,y)\in\mathbb R^2:x^2+y^2=1\},\\
X&=\{(x,y)\in\mathbb R^2:y^2=x^2\},\\
K&=\{(x,y)\in\mathbb R^2:y^2=x^3\}.
\end{aligned}
$$

La letra $C$ nombra un conjunto de puntos de una circunferencia; $X$, un cruce de rectas; $K$, una curva con dos ramas que se encuentran en el origen. Sus descripciones geométricas serán consecuencias de cálculos, no premisas que autoricen derivar funciones inexistentes.

### Estación 1. Identificar el objeto: relación, gráfica o rama

**Pregunta inicial.** ¿Podemos escribir sin más «la función $y$ definida por $x^2+y^2=1$»?

No: para $-1<x<1$ la ecuación permite simultáneamente

$$
y=\sqrt{1-x^2}\qquad\text{e}\qquad y=-\sqrt{1-x^2}.
$$

Por tanto, $C$ no es la gráfica de una sola función $y(x)$ definida sobre $(-1,1)$. La proyección de $C$ sobre el eje horizontal es $[-1,1]$, pero la unicidad vertical falla en cada punto interior. En cambio, para $x=\pm1$ ambas expresiones producen el mismo valor $0$. Recordemos la definición @def-t1-0046: solo después de fijar una función $\varphi:I\to\mathbb R$ cuyo grafo esté contenido en el conjunto de ceros podemos hablar de *su* derivada.

::: {.callout-warning title="Error de lectura"}
Resolver una ecuación para $y$ puede ofrecer varias expresiones. Anotar $y'$ antes de escoger dominio y rama no especifica qué objeto se pretende derivar.
:::

### Estación 2. Verificar existencia y continuidad sin recurrir a la derivada

En la circunferencia, los resultados previos sobre raíces y composición permiten construir, con dominio explícito,

$$
\varphi_\pm:[-1,1]\longrightarrow\mathbb R,
\qquad\varphi_\pm(x)=\pm\sqrt{1-x^2}.
$$

Ambas funciones están bien definidas, son continuas en su dominio relativo y cumplen la relación. No hemos aplicado todavía ninguna regla de derivación. En la curva $K$ la restricción $x\ge0$ es obligatoria, pues $x^3=y^2\ge0$. Sobre $[0,\infty)$ existen las funciones continuas

$$
\psi_\pm(x)=\pm x^{3/2},
\qquad \psi_\pm(x)^2=x^3.
$$

La potencia racional ya fue construida en §8.5; no necesitamos postular una solución implícita. Para apreciar por qué la condición $F(a,b)=0$ **no es, por sí sola, una construcción de rama**, tomemos $F(x,y)=x^2+y^2$. Su único cero real es $(0,0)$: los cuadrados son no negativos y su suma solo puede ser cero cuando ambos se anulan. No existe una rama $\varphi:I\to\mathbb R$ por ese punto si exigimos que $0$ sea punto de acumulación de $I$ y $F(x,\varphi(x))=0$ para todo $x\in I$, porque entonces $I\subseteq\{0\}$, contradiciendo la acumulación. Esto no contradice @thm-t1-0032: aquí no se ha dado una rama continua a la cual aplicarlo.

### Estación 3. Precisar el dominio y los incrementos admisibles

La rama superior de $C$ existe sobre $[-1,1]$, pero un cociente incremental centrado en $a=1$ solo puede usar $x\le1$. Para $-1<x<1$ y $x\ne1$,

$$
\frac{\varphi_+(x)-\varphi_+(1)}{x-1}
=\frac{\sqrt{1-x^2}}{x-1}
=-\sqrt{\frac{1+x}{1-x}}.
$$

El cociente tiende a $-\infty$ cuando $x\uparrow1$; por ello **no hay derivada relativa real finita** en $1$, aunque la rama sea continua allí. Tampoco existe una rama $y(x)$ real definida sobre un intervalo *abierto* alrededor de $x=1$, pues habría valores $x>1$ y la ecuación exigiría $y^2=1-x^2<0$.

Para $K$ sucede algo diferente: el dominio $[0,\infty)$ de $\psi_+$ solo admite incrementos por la derecha en el origen, pero

$$
\frac{\psi_+(x)-\psi_+(0)}{x-0}
=\sqrt x\longrightarrow0\qquad(x\downarrow0).
$$

Existe, pues, la derivada *relativa* $\psi'_{+,[0,\infty)}(0)=0$. Un extremo de dominio no implica, por sí solo, ni existencia ni inexistencia de derivada: se debe calcular el límite sobre los incrementos disponibles.

### Estación 4. Seleccionar la rama en un punto de cruce

El conjunto $X$ se factoriza exactamente:

$$
y^2-x^2=(y-x)(y+x)=0.
$$

Las funciones $\chi_1(x)=x$ y $\chi_2(x)=-x$, ambas con dominio $\mathbb R$, satisfacen la ecuación; sus derivadas en $0$ son, respectivamente, $1$ y $-1$. Existe también la selección continua

$$
\chi_3(x)=|x|=
\begin{cases}
-x,&x<0,\\
x,&x\ge0,
\end{cases}
$$

que pertenece al mismo conjunto de ceros, pero tiene cocientes laterales $-1$ y $1$ y no es diferenciable en $0$. La misma relación contiene, así, dos ramas lineales de pendientes distintas y otra rama continua sin pendiente finita en su unión. Una relación no elige la rama ni determina automáticamente una única tangente a una gráfica funcional.

::: {.callout-note title="Comprueba la selección"}
¿Qué operación cambió al pasar de $\chi_1$ a $\chi_3$? No cambió el polinomio de la ecuación; cambió la **función elegida**. Reconstruye las dos definiciones por tramos antes de comparar sus cocientes en el origen.
:::

### Estación 5. Calcular los coeficientes algebraicos correctos

Para aplicar @thm-t1-0032, el punto $(a,b)$ debe pertenecer a la relación, la rama ya debe estar construida y hay que disponer de la identidad exacta de @lem-t1-0003:

$$
F(x,y)-F(a,b)=(x-a)A_{a,b}(x,y)+(y-b)B_{a,b}(x,y).
$$

La siguiente tabla recoge identidades obtenidas por diferencias de potencias. Sus letras $A,B$ son coeficientes del telescopado, **no derivadas parciales introducidas por anticipado**.

| Relación $F(x,y)=0$ | $A_{a,b}(x,y)$ | $B_{a,b}(x,y)$ | Valores en $(a,b)$ |
|---|---|---|---|
| $x^2+y^2-1=0$ | $x+a$ | $y+b$ | $A(a,b)=2a$, $B(a,b)=2b$ |
| $y^2-x^2=0$ | $-(x+a)$ | $y+b$ | $A(a,b)=-2a$, $B(a,b)=2b$ |
| $y^2-x^3=0$ | $-(x^2+xa+a^2)$ | $y+b$ | $A(a,b)=-3a^2$, $B(a,b)=2b$ |

La identidad de la tercera fila, por ejemplo, se verifica sin tomar límites:

$$
y^2-b^2-(x^3-a^3)
=(y-b)(y+b)-(x-a)(x^2+xa+a^2).
$$

En $(0,1)\in C$, $B(0,1)=2\ne0$. En los orígenes de $X$ y $K$, tanto $A$ como $B$ se anulan: el cociente $-A/B$ daría una expresión $0/0$ **sin valor definido**. Que una fórmula no proporcione respuesta no autoriza a completar la respuesta por conjetura geométrica.

### Estación 6. Probar el límite: de los coeficientes a las pendientes

Tomemos en $C$ el punto $(a,b)=(3/5,4/5)$ y la rama positiva construida. Se verifica $a^2+b^2=1$ y $b>0$. Como $B(a,b)=8/5$, el teorema garantiza que la rama es diferenciable en $a$ y da

$$
\varphi_+'\!\left(\frac35\right)
=-\frac{A(a,b)}{B(a,b)}
=-\frac{6/5}{8/5}=-\frac34.
$$

También podemos reconstruir el cálculo directamente a partir de la identidad de dos cuadrados, sin presuponer una derivada:

$$
\frac{\varphi_+(x)-b}{x-a}
=-\frac{x+a}{\varphi_+(x)+b}
\longrightarrow-\frac{2a}{2b}=-\frac34.
$$

El denominador converge a $2b=8/5\ne0$, por lo que la división es válida para $x$ suficientemente cercano a $a$. Esta igualdad traduce la continuidad en una justificación precisa del límite. El contraste con $K$ muestra el alcance de la condición: en $(0,0)$, $B=0$ impide usar *este* teorema, pero el cociente de la estación 3 prueba independientemente que $\psi_+$ tiene derivada relativa $0$.

### Estación 7. Refutar las inferencias falsas con un contraejemplo específico

No basta advertir que una conclusión «puede fallar»; debe identificarse exactamente la hipótesis omitida y construirse el ejemplo pertinente.

| Afirmación apresurada | Diagnóstico verificable |
|---|---|
| «Si $F(a,b)=0$, existe una rama sobre un intervalo con $a$ de acumulación». | $F=x^2+y^2$ y $(a,b)=(0,0)$: el único cero es el origen; no hay tal rama. |
| «Si $B(a,b)=0$, ninguna rama puede tener derivada». | $y^2=x^3$ y $\psi_+(x)=x^{3/2}$ sobre $[0,\infty)$: $B(0,0)=0$ y derivada relativa $0$. |
| «Una rama continua tiene necesariamente derivada en el cruce». | $y^2=x^2$ y $\chi_3(x)=|x|$: cocientes laterales incompatibles. |
| «No se aplica el teorema; por tanto, no existe derivada». | Es la misma confusión lógica anterior: la rama $\psi_+$ no satisface $B\ne0$ y, sin embargo, tiene derivada. |
| «La ecuación fija una sola pendiente en el cruce». | $\chi_1'(0)=1$ y $\chi_2'(0)=-1$ para la misma ecuación. |

Una condición suficiente como $B(a,b)\ne0$ sirve para **probar** una conclusión cuando concurren *todas* las hipótesis de @thm-t1-0032. Su incumplimiento no demuestra la negación de la conclusión. En cambio, la ausencia de rama sí impide formular una derivada de esa rama: no es un defecto de cálculo, sino una ausencia del objeto que se pretende estudiar.

### Estación 8. Parametrizar con restricción y recuperar una gráfica local

Una parametrización ofrece pares $(x(t),y(t))$, pero no garantiza que su conjunto de puntos sea la gráfica de una función $y$ de $x$. Consideremos, sobre el intervalo $T=[0,2]$,

$$
x(t)=t^3+t,
\qquad y(t)=t^2.
$$

Para $s<t$ en $T$,

$$
x(t)-x(s)
=(t-s)(t^2+ts+s^2+1)>0.
$$

Por tanto, $x:T\to J=x(T)=[0,10]$ es continua, estrictamente creciente y biyectiva sobre su imagen. @thm-t1-0023 garantiza que su inversa $g:J\to T$ es continua: ahora sí existe la función

$$
\Phi:J\longrightarrow\mathbb R,
\qquad\Phi(u)=y(g(u))=g(u)^2.
$$

En $t_0=1$ obtenemos $u_0=x(1)=2$ y $\Phi(2)=1$. Como $x'(1)=4\ne0$ y $y'(1)=2$, @thm-t1-0031 y la regla de la cadena, aplicados **después de construir la inversa**, producen

$$
\Phi'(2)=y'(1)g'(2)
=\frac{y'(1)}{x'(1)}
=\frac24=\frac12.
$$

La notación abreviada $dy/dx=(dy/dt)/(dx/dt)$ solo recoge aquí esa cadena de argumentos; no es una licencia para dividir derivadas cuando $x$ no admite la inversión requerida. Comprobemos el valor sin recurrir a esa abreviatura. Para $t\ne1$, la factorización exacta da

$$
\frac{y(t)-y(1)}{x(t)-x(1)}
=\frac{t^2-1}{t^3+t-2}
=\frac{t+1}{t^2+t+2}\longrightarrow\frac12.
$$

La continuidad de $g$ asegura que, cuando $u=x(t)\to2$, el parámetro correspondiente satisface $t\to1$; además, la inyectividad de $x$ permite cancelar $t-1$ sin identificar puntos diferentes de la curva. Como control algebraico opcional, eliminar el parámetro proporciona

$$
F(u,v)=u^2-v(v+1)^2=0,
$$

porque $u=t(t^2+1)$ y $v=t^2$. En $(u,v)=(2,1)$ el telescopado tiene valores $A=2u=4$ y $B=-(3v^2+4v+1)=-8$; @thm-t1-0032 vuelve a dar $-A/B=1/2$ para la rama continua $\Phi$ ya construida. El acuerdo entre los dos métodos verifica un mismo objeto, no la existencia automática de una rama a partir de la ecuación.

### Traducción final: qué significa la pendiente y qué no significa

En una gráfica funcional derivable en un punto interior, el número $\varphi'(a)$ determina la pendiente de su recta tangente en el sentido de la aproximación lineal demostrada en el capítulo 6. Así, la rama superior de $C$ en $(3/5,4/5)$ tiene pendiente $-3/4$; cada rama lineal de $X$ en el origen posee su propia pendiente; $\chi_3=|x|$ no posee una sola pendiente allí; las ramas de $K$ poseen derivada **relativa** horizontal en el origen, pero solo están definidas para $x\ge0$. El punto $(1,0)$ de $C$ es distinto: el cociente de la rama superior diverge y no hay pendiente real finita para su gráfica en ese extremo. No necesitamos introducir todavía la teoría general de tangentes a curvas parametrizadas ni llamar «derivada infinita» a un número real inexistente.

::: {.callout-important title="Mapa de decisión para futuras curvas"}
Ante una relación, identifica primero el conjunto de ceros; demuestra después que la rama o la inversa elegida **existe** con dominio explícito; establece su continuidad cuando el resultado la exige; verifica el punto de acumulación y el tipo de incremento; comprueba $B(a,b)\ne0$ antes de usar el teorema implícito; si falla esa hipótesis, vuelve al cociente propio de la rama. Solo entonces interpreta geométricamente la derivada obtenida. La falta de alguno de estos pasos nunca se repara escribiendo una fórmula familiar.
:::

Este recorrido completa la síntesis conceptual del capítulo. La §8.11 desarrolla esas distinciones en cuarenta ejercicios originales organizados por familias A–G, cada uno acompañado por su solución razonada en la misma fuente canónica. La incorporación del banco no sustituye la auditoría integral ni la revisión visual: el capítulo permanece abierto y fuera de publicación hasta superar ambas puertas.

## Ejercicios y soluciones {#sec-t1-c09-11}

Este banco pone a prueba una secuencia de decisiones antes que la memorización de fórmulas: identificar la función y su dominio, justificar la existencia de una inversa o una rama, establecer la continuidad requerida, comprobar el tipo de derivada en el punto y solo entonces calcular. Una relación polinómica no se tratará como función sin escoger una rama; la no anulación de un coeficiente algebraico proporciona un **criterio suficiente condicionado**, no una conclusión sobre cualquier curva no construida.

Los cuarenta ejercicios originales se distribuyen en los niveles $7A+7B+7C+6D+5E+5F+3G=40$. Los identificadores `CPM-T1-EXR-0316--0355` y sus homólogos `CPM-T1-SOL-0316--0355` se emparejan al final de esta sección. Se permiten únicamente los resultados de los capítulos anteriores y de las §§8.1--8.10. No se invocarán Rolle, el teorema del valor medio, criterios diferenciales posteriores de monotonía, logaritmos o funciones trigonométricas no construidas, ni el teorema implícito multivariable.

### Nivel A — Reconocimiento y comprensión

::: {#exr-t1-0316}
<!-- CPM-T1-EXR-0316 | A | CONCEPTUAL | DOMAIN | ORIGINAL -->
**Ejercicio A1. El cuadrado y sus dos restricciones.** Considera $q:\mathbb R\to\mathbb R$, $q(x)=x^2$. Determina su imagen y explica por qué no admite inversa. Construye dos restricciones a intervalos que sí sean biyecciones sobre su imagen, y tipa sus inversas.
:::

::: {#exr-t1-0317}
<!-- CPM-T1-EXR-0317 | A | CONCEPTUAL | PROOF | ORIGINAL -->
**Ejercicio A2. ¿En qué punto se evalúa la derivada?** Sean $I$ un intervalo, $f:I\to\mathbb R$ continua e inyectiva, $J=f(I)$ y $g=f^{-1}$. Si $a\in I$ es punto de acumulación y $f'_I(a)\ne0$, escribe correctamente $g'_J(b)$ para $b=f(a)$. Explica por qué la cadena de símbolos «$(f^{-1})'=1/f'$» no es por sí sola una igualdad de funciones bien tipada.
:::

::: {#exr-t1-0318}
<!-- CPM-T1-EXR-0318 | A | CONCEPTUAL | PROOF | ORIGINAL -->
**Ejercicio A3. Un dato puntual no produce inversión.** Examina la afirmación «$f'(a)\ne0$ implica que $f$ es inyectiva en algún intervalo alrededor de $a$». Determina qué información proporciona realmente el cociente incremental y por qué no compara automáticamente dos puntos móviles distintos de $a$. Señala el resultado anterior que exige inyectividad como hipótesis.
:::

::: {#exr-t1-0319}
<!-- CPM-T1-EXR-0319 | A | DOMAIN | CONCEPTUAL | ORIGINAL -->
**Ejercicio A4. Una igualdad de expresiones y dos funciones.** Compara $u(x)=\sqrt{x^2}$ y $v(x)=x$, ambas definidas en $\mathbb R$. Decide en qué subconjunto coinciden, deriva cada función allí donde sea posible y analiza el punto $0$ por cocientes.
:::

::: {#exr-t1-0320}
<!-- CPM-T1-EXR-0320 | A | GEOMETRY | CONCEPTUAL | ORIGINAL -->
**Ejercicio A5. Dos gráficas en una relación.** Para $F(x,y)=y^2-x^2$, construye dos ramas sobre $I=(-1,1)$ que pasen por $(0,0)$ y calcula sus derivadas en el origen. ¿Selecciona la ecuación una única pendiente?
:::

::: {#exr-t1-0321}
<!-- CPM-T1-EXR-0321 | A | CONCEPTUAL | DOMAIN | ORIGINAL -->
**Ejercicio A6. Frontera del repertorio.** Decide cuáles de $\ln x$, $\arcsin x$ y $x^{3/5}$ han recibido construcción y regla de derivación suficientes en este capítulo. Para la expresión admitida, especifica su dominio real bajo la convención de fracción reducida con denominador impar y señala dónde es válida su fórmula derivada.
:::

::: {#exr-t1-0322}
<!-- CPM-T1-EXR-0322 | A | PROOF | LIMIT | ORIGINAL -->
**Ejercicio A7. El extremo de la raíz cuadrada.** Sea $r_2:[0,\infty)\to\mathbb R$, $r_2(t)=\sqrt t$. Escribe la definición de $r'_{2,[0,\infty)}(0)$ y decide, mediante el cociente exacto y los incrementos permitidos, si existe como número real finito.
:::

### Nivel B — Aplicación directa

::: {#exr-t1-0323}
<!-- CPM-T1-EXR-0323 | B | COMPUTATION | DOMAIN | ORIGINAL -->
**Ejercicio B1. Raíz de una función afín.** Determina el dominio natural de $f(x)=\sqrt{5x+4}$ y calcula $f'(x)$ en los puntos donde la regla de la raíz y la cadena son aplicables. Examina por separado el extremo del dominio.
:::

::: {#exr-t1-0324}
<!-- CPM-T1-EXR-0324 | B | COMPUTATION | ORIGINAL -->
**Ejercicio B2. Potencia racional de base positiva.** Para $f(x)=(x^2+1)^{3/2}$, prueba que está definida y es diferenciable sobre $\mathbb R$, y calcula $f'(x)$.
:::

::: {#exr-t1-0325}
<!-- CPM-T1-EXR-0325 | B | COMPUTATION | LIMIT | ORIGINAL -->
**Ejercicio B3. La raíz cúbica compuesta.** Estudia $f(x)=\sqrt[3]{2x-1}$ en toda la recta: da la fórmula de su derivada en los puntos admisibles y determina mediante el cociente incremental qué sucede en $x=1/2$.
:::

::: {#exr-t1-0326}
<!-- CPM-T1-EXR-0326 | B | COMPUTATION | DOMAIN | ORIGINAL -->
**Ejercicio B4. Raíz de un cociente.** Halla el dominio de $f(x)=\sqrt{(x-2)/(x+3)}$, su interior y la derivada en este último. ¿Por qué no puedes evaluar la función en $-3$ ni aplicar sin más la misma fórmula en $2$?
:::

::: {#exr-t1-0327}
<!-- CPM-T1-EXR-0327 | B | COMPUTATION | INVERSE | ORIGINAL -->
**Ejercicio B5. La inversa negativa del cuadrado.** Define $q:(-\infty,0]\to[0,\infty)$ por $q(u)=u^2$. Demuestra que es biyectiva, identifica su inversa $g$ y calcula $g'(y)$ para $y>0$; distingue el resultado de la rama positiva.
:::

::: {#exr-t1-0328}
<!-- CPM-T1-EXR-0328 | B | GEOMETRY | COMPUTATION | ORIGINAL -->
**Ejercicio B6. Una pendiente en la circunferencia de radio cinco.** Construye la rama superior de $x^2+y^2=25$ sobre $[-5,5]$, comprueba que pasa por $(3,4)$ y calcula su derivada en $x=3$ mediante los coeficientes algebraicos del telescopado.
:::

::: {#exr-t1-0329}
<!-- CPM-T1-EXR-0329 | B | COMPUTATION | LIMIT | ORIGINAL -->
**Ejercicio B7. Potencia racional sobre bases negativas.** Bajo la convención de raíces impares, considera $f(x)=x^{2/3}$ para $x\in\mathbb R$. Calcula $f'(x)$ para $x<0$ y determina mediante límites laterales si existe una derivada real finita en $0$.
:::

### Nivel C — Combinación estructural

::: {#exr-t1-0330}
<!-- CPM-T1-EXR-0330 | C | PROOF | INVERSE | ORIGINAL -->
**Ejercicio C1. Construir una raíz antes de derivarla.** Para $n\ge1$, define $r_n(t)$ como el único real no negativo cuya potencia $n$-ésima es $t\ge0$. Justifica su existencia, unicidad y continuidad, y prueba para $t>0$ que $r_n'(t)=1/(n\,r_n(t)^{n-1})$ sin recurrir al teorema del valor medio.
:::

::: {#exr-t1-0331}
<!-- CPM-T1-EXR-0331 | C | PROOF | DOMAIN | ORIGINAL -->
**Ejercicio C2. Una regla con tres condiciones de dominio.** Sean $p,q\in\mathbb R[X]$ y $r=m/n\in\mathbb Q$ una fracción reducida con $n\ge1$. Sea $U$ un intervalo abierto tal que $q(x)\ne0$ y $p(x)/q(x)>0$ para todo $x\in U$. Demuestra que $H(x)=[p(x)/q(x)]^{m/n}$ es diferenciable en $U$ y obtiene una fórmula explícita sin usar logaritmos.
:::

::: {#exr-t1-0332}
<!-- CPM-T1-EXR-0332 | C | LIMIT | COMPOSITION | ORIGINAL -->
**Ejercicio C3. El radical oculta un valor absoluto.** Determina si $f(x)=\sqrt{x^2+x^4}$ tiene derivada en $0$. Explica por qué una sustitución automática de $x=0$ en la fórmula general de la raíz no resuelve el problema.
:::

::: {#exr-t1-0333}
<!-- CPM-T1-EXR-0333 | C | LIMIT | PROOF | ORIGINAL -->
**Ejercicio C4. Un módulo que sí admite derivada en el origen.** Estudia $f(x)=|x^3|$ para $x\in\mathbb R$: prueba directamente su derivabilidad en $0$ y calcula la derivada cuando $x\ne0$.
:::

::: {#exr-t1-0334}
<!-- CPM-T1-EXR-0334 | C | PROOF | IMPLICIT | ORIGINAL -->
**Ejercicio C5. Pendiente implícita bajo hipótesis explícitas.** Sea $F(x,y)=x^3+xy+y^3-1$. Supón **dada** una rama $\varphi:I\to\mathbb R$ continua en $0$, donde $I$ es un intervalo con $0$ como punto de acumulación, $\varphi(0)=1$ y $F(x,\varphi(x))=0$ en $I$. Construye el telescopado de $F$, verifica sus coeficientes en $(0,1)$ y prueba el valor de $\varphi'_I(0)$. ¿Qué no demuestra por sí mismo este razonamiento?
:::

::: {#exr-t1-0335}
<!-- CPM-T1-EXR-0335 | C | GEOMETRY | INVERSE | ORIGINAL -->
**Ejercicio C6. Parámetro y gráfica.** Para $t\in[0,2]$, considera $x(t)=t^3+t$ y $y(t)=t^2$. Justifica la existencia de una función $Y$ de la coordenada $x$ sobre su imagen y calcula $Y'(2)$ por inversa y regla de la cadena. Comprueba el resultado mediante un cociente de diferencias factorizado.
:::

::: {#exr-t1-0336}
<!-- CPM-T1-EXR-0336 | C | COMPUTATION | LIMIT | ORIGINAL -->
**Ejercicio C7. Raíz cúbica de un polinomio.** Sea $f(x)=\sqrt[3]{x^3+1}$. Calcula $f'(x)$ donde la regla de inversión lo autorice, estudia expresamente $x=0$ y decide por cociente incremental si hay derivada real finita en $x=-1$.
:::

### Nivel D — Inversión y diagnóstico

::: {#exr-t1-0337}
<!-- CPM-T1-EXR-0337 | D | CONCEPTUAL | PROOF | ORIGINAL -->
**Ejercicio D1. La cadena no construye la inversa diferenciable.** Alguien escribe $f(g(y))=y$ y, derivando, obtiene $f'(g(y))g'(y)=1$. Identifica la hipótesis que da por supuesta; reconstruye el orden no circular de @thm-t1-0031.
:::

::: {#exr-t1-0338}
<!-- CPM-T1-EXR-0338 | D | COUNTEREXAMPLE | INVERSE | ORIGINAL -->
**Ejercicio D2. ¿La derivada no nula es necesaria para la existencia de la inversa?** Contrasta las propiedades de $f(x)=x^3$ y $g=f^{-1}$ en el origen. Precisa qué requisito sirve para construir $g$ y qué falla al tratar de derivarla con @thm-t1-0031.
:::

::: {#exr-t1-0339}
<!-- CPM-T1-EXR-0339 | D | CONCEPTUAL | IMPLICIT | ORIGINAL -->
**Ejercicio D3. Una conclusión que no figura en el teorema.** Si $F(a,b)=0$ y $B_{a,b}(a,b)\ne0$, ¿puede invocarse **únicamente** @thm-t1-0032 para declarar que existe una rama continua alrededor de $a$? Identifica con precisión la hipótesis que falta en ese teorema y distingue «no demostrado por este resultado» de «matemáticamente falso».
:::

::: {#exr-t1-0340}
<!-- CPM-T1-EXR-0340 | D | LIMIT | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio D4. La degeneración no excluye una derivada.** Para $F(x,y)=y^2-x^3$ y $\varphi:[0,\infty)\to\mathbb R$, $\varphi(x)=x^{3/2}$, comprueba que es rama continua por el origen, calcula $B_{0,0}(0,0)$ y halla su derivada relativa en $0$.
:::

::: {#exr-t1-0341}
<!-- CPM-T1-EXR-0341 | D | CONCEPTUAL | LIMIT | ORIGINAL -->
**Ejercicio D5. El módulo no se cancela.** Compara en $x=0$ las derivadas de $f(x)=\sqrt{x^2}$ y $g(x)=x$ sobre $\mathbb R$. Explica exactamente por qué la coincidencia sobre $[0,\infty)$ no decide la derivada bilateral de $f$.
:::

::: {#exr-t1-0342}
<!-- CPM-T1-EXR-0342 | D | LIMIT | GEOMETRY | ORIGINAL -->
**Ejercicio D6. Un extremo de pendiente no finita.** Sea $\varphi:[-1,1]\to\mathbb R$, $\varphi(x)=\sqrt{1-x^2}$. Demuestra mediante incrementos desde la izquierda que $\varphi'_{[-1,1]}(1)$ no existe como número real finito. No utilices la fórmula interior en el extremo.
:::

### Nivel E — Construcción de contraejemplos

::: {#exr-t1-0343}
<!-- CPM-T1-EXR-0343 | E | COUNTEREXAMPLE | INVERSE | ORIGINAL -->
**Ejercicio E1. Inyectividad con derivada nula.** Construye una función continua e inyectiva en un intervalo cuya derivada se anule en un punto de acumulación. Explica qué ocurre con la derivada finita de la función inversa en la imagen de ese punto.
:::

::: {#exr-t1-0344}
<!-- CPM-T1-EXR-0344 | E | COUNTEREXAMPLE | GEOMETRY | ORIGINAL -->
**Ejercicio E2. Conjunto de ceros no funcional.** Construye una relación polinómica cuyo conjunto de ceros completo no sea la gráfica de una función $y$ de $x$, pero contenga dos ramas diferenciables sobre un mismo intervalo. Verifica ambas afirmaciones.
:::

::: {#exr-t1-0345}
<!-- CPM-T1-EXR-0345 | E | COUNTEREXAMPLE | IMPLICIT | ORIGINAL -->
**Ejercicio E3. Una derivada con $B=0$.** Exhibe una relación polinómica y una rama continua y diferenciable en un punto de acumulación en el que el coeficiente $B$ del telescopado se anule. Aclara si la derivada es bilateral o relativa.
:::

::: {#exr-t1-0346}
<!-- CPM-T1-EXR-0346 | E | DOMAIN | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio E4. Una raíz par no admite entradas negativas reales.** Demuestra que ninguna función real que cumpla $r(t)^2=t$ puede estar definida en todos los números negativos. Identifica exactamente dónde se define la raíz cuadrada real construida en este libro.
:::

::: {#exr-t1-0347}
<!-- CPM-T1-EXR-0347 | E | COUNTEREXAMPLE | PIECEWISE | ORIGINAL -->
**Ejercicio E5. Dos fórmulas derivables, un empalme no derivable.** Construye una función continua sobre $\mathbb R$ que esté dada por polinomios diferenciables a cada lado de $0$, pero no sea diferenciable en $0$. Justifica continuidad y fracaso de la derivada.
:::

### Nivel F — Descubrimiento guiado

::: {#exr-t1-0348}
<!-- CPM-T1-EXR-0348 | F | DISCOVERY | PROOF | ORIGINAL -->
**Ejercicio F1. Reconstruir la derivada de la inversa.** Sean $I$ intervalo, $f:I\to\mathbb R$ continua e inyectiva, $J=f(I)$, $g=f^{-1}$ y $a\in I$ punto de acumulación con $f'_I(a)=L\ne0$. (a) Justifica que $g$ es continua y que $b=f(a)$ es punto de acumulación de $J$. (b) Relaciona exactamente los cocientes de $f$ y $g$. (c) Prueba que el denominador permanece no nulo cerca de $a$ y deduce $g'_J(b)$ sin citar la fórmula del teorema inverso.
:::

::: {#exr-t1-0349}
<!-- CPM-T1-EXR-0349 | F | DISCOVERY | ROOT | ORIGINAL -->
**Ejercicio F2. Raíces impares de números negativos.** Sea $n\ge1$ impar. (a) Prueba algebraicamente que $u\mapsto u^n$ es estrictamente creciente sobre $\mathbb R$. (b) Demuestra existencia de una inversa continua sobre toda la recta. (c) Deduce la fórmula de su derivada en entradas $t<0$ y explica por qué la no anulación necesaria está asegurada.
:::

::: {#exr-t1-0350}
<!-- CPM-T1-EXR-0350 | F | DISCOVERY | PROOF | ORIGINAL -->
**Ejercicio F3. Coeficientes independientes del telescopado.** Supón que un polinomio $F$ admite dos identidades $F(x,y)-F(a,b)=(x-a)A+(y-b)B=(x-a)\widetilde A+(y-b)\widetilde B$, con los cuatro coeficientes polinómicos. Demuestra que $A(a,b)=\widetilde A(a,b)$ y $B(a,b)=\widetilde B(a,b)$, aun cuando los polinomios completos puedan diferir.
:::

::: {#exr-t1-0351}
<!-- CPM-T1-EXR-0351 | F | DISCOVERY | IMPLICIT | ORIGINAL -->
**Ejercicio F4. Reconstrucción polinómica controlada.** Considera $F(x,y)=x^2+xy+y^2-7$ y el punto $(1,2)$. Supón dada una rama $\varphi:I\to\mathbb R$ continua en $1$, definida en un intervalo donde $1$ es punto de acumulación, con $\varphi(1)=2$ y $F(x,\varphi(x))=0$. (a) Construye $A_{1,2},B_{1,2}$. (b) Prueba la no anulación local adecuada. (c) Obtén $\varphi'_I(1)$ por cocientes.
:::

::: {#exr-t1-0352}
<!-- CPM-T1-EXR-0352 | F | DISCOVERY | INVERSE | ORIGINAL -->
**Ejercicio F5. Una relación sí determina una inversa global.** Para cada $x\in\mathbb R$ considera $y^3+y=x$. Construye rigurosamente la única función $\varphi:\mathbb R\to\mathbb R$ que satisface esta relación; demuestra su continuidad y su derivabilidad en todos los puntos, y expresa $\varphi'(x)$ en función de $\varphi(x)$ sin teorema del valor medio.
:::

### Nivel G — Desafíos

::: {#exr-t1-0353}
<!-- CPM-T1-EXR-0353 | G | CHALLENGE | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio G1. Una derivada positiva aislada no garantiza inyectividad local.** Para $n\ge2$ pon $a_n=2^{-n}$, $w_n=a_n^3/100$ y $h_n=a_n^2/100$. En $[a_n,a_n+2w_n]$ define una tienda triangular $p_n$ de altura $h_n$ y vértice en $a_n+w_n$, con valor cero en ambos extremos. Fuera de la unión de las bases toma $p=0$ y define $f(x)=x+p(x)$ para todo $x\in\mathbb R$. Prueba que las bases son disjuntas, $f$ es continua, $f'(0)=1$ y $f$ no es inyectiva en ningún entorno de $0$. Da dos puntos distintos de igual imagen en cada base.
:::

::: {#exr-t1-0354}
<!-- CPM-T1-EXR-0354 | G | CHALLENGE | LIMIT | DOMAIN | ORIGINAL -->
**Ejercicio G2. Exponentes racionales y derivada en el origen.** Sea $r=m/n>0$ una fracción reducida, $m,n\in\mathbb N$. Considera $f_r(x)=x^{m/n}$ con el dominio real de la convención de §8.5: si $n$ es par, $x\ge0$; si $n$ es impar, $x\in\mathbb R$ con raíz impar real. Clasifica exhaustivamente la existencia y el valor de la derivada **relativa al dominio** en $0$ para $r>1$, $r=1$ y $0<r<1$. Cuando falte la derivada, describe el comportamiento de los cocientes permitidos a ambos lados.
:::

::: {#exr-t1-0355}
<!-- CPM-T1-EXR-0355 | G | CHALLENGE | IMPLICIT | GEOMETRY | ORIGINAL -->
**Ejercicio G3. Dos tangentes en un cruce deformado.** Para $F(x,y)=y^2-x^2(1+x)$ en $(0,0)$, construye dos ramas continuas sobre algún intervalo abierto que contenga $0$, demuestra directamente que son diferenciables allí y que sus pendientes en el origen son opuestas. Calcula $A(0,0)$ y $B(0,0)$ e interpreta por qué el teorema implícito de §8.9 no selecciona una pendiente única.
:::

### Soluciones desarrolladas

#### Soluciones del nivel A

::: {#sol-t1-0316}
<!-- CPM-T1-SOL-0316 -->
**Solución A1.** La imagen de $q$ es $[0,\infty)$: todo cuadrado es no negativo y, para cada $t\ge0$, la raíz cuadrada construida satisface $(\sqrt t)^2=t$. La igualdad $q(1)=q(-1)$ muestra que $q$ no es inyectiva sobre $\mathbb R$; reducir solamente el codominio a la imagen no repara ese defecto. Las restricciones

$$
q_+:[0,\infty)\to[0,\infty),\quad q_+(x)=x^2,
\qquad q_-:(-\infty,0]\to[0,\infty),\quad q_-(x)=x^2
$$

son biyectivas: cada $t\ge0$ tiene exactamente una preimagen no negativa y una no positiva, respectivamente. Sus inversas son $q_+^{-1}(t)=\sqrt t$ y $q_-^{-1}(t)=-\sqrt t$, ambas de $[0,\infty)$ al intervalo de partida correspondiente. Las identidades $q_\pm(q_\pm^{-1}(t))=t$ y $q_\pm^{-1}(q_\pm(x))=x$ se comprueban respetando los signos de $x$.
:::

::: {#sol-t1-0317}
<!-- CPM-T1-SOL-0317 -->
**Solución A2.** Por @thm-t1-0023, $g:J\to I$ existe y es continua. Las hipótesis de @thm-t1-0031 permiten afirmar, con derivadas relativas,

$$
g'_J(b)=\frac{1}{f'_I(a)},\qquad b=f(a),\quad a=g(b).
$$

Si la condición se verifica en todos los puntos apropiados de $J$, puede escribirse punto a punto $g'(y)=1/f'(g(y))$. El miembro izquierdo se evalúa en una **salida** $y$ de $f$; el derecho, en el antecedente $g(y)$. Escribir $1/f'(y)$ sin cambiar el argumento confunde los dominios y, aun con argumentos correctos, debe conservarse la hipótesis de no anulación.
:::

::: {#sol-t1-0318}
<!-- CPM-T1-SOL-0318 -->
**Solución A3.** Si $f'(a)=L\ne0$, el cociente $(f(x)-f(a))/(x-a)$ tiene el signo de $L$ cerca de $a$ para $x\ne a$. De ello se deduce que $f(x)\ne f(a)$ suficientemente cerca de $a$, esto es, el valor central queda aislado entre los valores vecinos. Pero la inyectividad exige $f(u)\ne f(v)$ para **cualesquiera** $u\ne v$ del mismo intervalo, no solo cuando uno sea $a$. El contraejemplo construido en §8.7 (y reconstruido en G1) presenta $f'(0)=1$ con valores repetidos en cada entorno de $0$. @thm-t1-0023 supone continuidad e inyectividad en el intervalo; no deriva esta última de una sola pendiente no nula.
:::

::: {#sol-t1-0319}
<!-- CPM-T1-SOL-0319 -->
**Solución A4.** La raíz no negativa satisface $\sqrt{x^2}=|x|$. En $[0,\infty)$, $u=v=x$; si $x<0$, $u(x)=-x\ne x=v(x)$, salvo en el origen ya incluido. Por tanto, $u'(x)=1$ para $x>0$ y $u'(x)=-1$ para $x<0$, mientras que $v'(x)=1$ en toda la recta. En $0$,

$$
\frac{u(h)-u(0)}h=\frac{|h|}{h}
=\begin{cases}1,&h>0,\\-1,&h<0.\end{cases}
$$

Los límites laterales difieren y $u'(0)$ no existe; en cambio $(v(h)-v(0))/h=1$. Coincidir en medio dominio no implica igualdad de derivadas bilaterales en su frontera.
:::

::: {#sol-t1-0320}
<!-- CPM-T1-SOL-0320 -->
**Solución A5.** Las funciones $\varphi_1(x)=x$ y $\varphi_2(x)=-x$ sobre $I=(-1,1)$ son continuas, pasan por el origen y verifican $\varphi_i(x)^2-x^2=0$ para todo $x\in I$. Sus cocientes en $0$ son $\varphi_1(h)/h=1$ y $\varphi_2(h)/h=-1$: las pendientes son $1$ y $-1$. Además, $|x|$ es una tercera rama continua de la misma relación que no es diferenciable en $0$. La ecuación determina el conjunto de ceros, no una única elección de función ni una pendiente singular del conjunto.
:::

::: {#sol-t1-0321}
<!-- CPM-T1-SOL-0321 -->
**Solución A6.** Las expresiones $\ln x$ y $\arcsin x$ pertenecen a teorías de funciones aún no construidas en este curso; no se les puede atribuir aquí una fórmula derivada. Sí está construida $x^{3/5}=(\sqrt[5]{x})^3$. Como la raíz quinta es real para bases negativas, su dominio es $\mathbb R$. Para $x\ne0$, la regla de §8.5 da

$$
\frac{d}{dx}x^{3/5}=\frac35x^{-2/5}=\frac{3}{5(\sqrt[5]{x})^2}.
$$

En $0$, el cociente $h^{3/5}/h=|h|^{-2/5}$ tiende a $+\infty$ por ambos lados; no existe derivada real finita. Que una expresión pueda escribirse no sustituye la construcción previa de su función.
:::

::: {#sol-t1-0322}
<!-- CPM-T1-SOL-0322 -->
**Solución A7.** La derivada relativa exigiría el límite real

$$
\lim_{\substack{h\to0\\h>0}}\frac{r_2(h)-r_2(0)}h
=\lim_{h\downarrow0}\frac{\sqrt h}{h}
=\lim_{h\downarrow0}\frac1{\sqrt h}.
$$

Para cualquier $M>0$, basta tomar $0<h<1/M^2$ para obtener $1/\sqrt h>M$. El cociente no converge a un número real: no existe derivada relativa finita en el extremo. La fórmula $1/(2\sqrt t)$ demostrada para $t>0$ no se prolonga mediante sustitución de $t=0$.
:::

#### Soluciones del nivel B

::: {#sol-t1-0323}
<!-- CPM-T1-SOL-0323 -->
**Solución B1.** La condición para una raíz cuadrada real es $5x+4\ge0$, por lo que el dominio es $[-4/5,\infty)$. Si $x>-4/5$, el argumento es positivo y la cadena, junto con la derivada de la raíz ya demostrada, proporciona

$$
f'(x)=\frac{5}{2\sqrt{5x+4}}.
$$

En $a=-4/5$, para $h>0$ el cociente relativo vale $\sqrt{5h}/h=\sqrt5/\sqrt h$, no finito al tender $h\downarrow0$. La función está definida y es continua allí, pero no posee derivada relativa real finita.
:::

::: {#sol-t1-0324}
<!-- CPM-T1-SOL-0324 -->
**Solución B2.** Para cualquier $x\in\mathbb R$ se tiene $x^2+1\ge1>0$. En consecuencia, la potencia racional $u^{3/2}$ está definida y es diferenciable en la base $u=x^2+1$ en todos los puntos. La regla de potencia de §8.5 y la cadena de C08 dan

$$
f'(x)=\frac32(x^2+1)^{1/2}(2x)
=3x\sqrt{x^2+1}.
$$

No hay extremos, ceros de la base ni divisiones excluidas que estudiar por separado.
:::

::: {#sol-t1-0325}
<!-- CPM-T1-SOL-0325 -->
**Solución B3.** La raíz cúbica está definida en todo $\mathbb R$. Si $x\ne1/2$, su argumento $2x-1$ no se anula; la regla de la inversa y la cadena permiten

$$
f'(x)=\frac{2}{3\bigl(\sqrt[3]{2x-1}\bigr)^2}.
$$

En $a=1/2$, $f(a)=0$ y, para $h\ne0$,

$$
\frac{f(a+h)-f(a)}h
=\frac{\sqrt[3]{2h}}h
=\frac{\sqrt[3]2}{|h|^{2/3}}.
$$

El cociente crece sin cota por ambos lados; no existe derivada real finita en ese punto. El denominador nulo de la fórmula exterior advierte una excepción, pero es el cociente el que la resuelve.
:::

::: {#sol-t1-0326}
<!-- CPM-T1-SOL-0326 -->
**Solución B4.** El cociente $u(x)=(x-2)/(x+3)$ es no negativo exactamente si $x<-3$ o $x\ge2$; $x=-3$ se excluye porque anula el denominador. El dominio es $(-\infty,-3)\cup[2,\infty)$ y su interior es $(-\infty,-3)\cup(2,\infty)$. En él $u>0$, y la regla del cociente da $u'(x)=5/(x+3)^2$. Por cadena,

$$
f'(x)=\frac{5}{2(x+3)^2\sqrt{(x-2)/(x+3)}}.
$$

El punto $-3$ no pertenece a la función. En $2$, el cociente derecho es $f(2+h)/h=1/(\sqrt h\sqrt{5+h})$ para $h>0$ y diverge, por lo que tampoco existe derivada relativa finita allí.
:::

::: {#sol-t1-0327}
<!-- CPM-T1-SOL-0327 -->
**Solución B5.** Si $u<v\le0$, entonces $u^2>v^2$, de modo que $q$ es inyectiva en el semieje negativo. Toda salida $y\ge0$ tiene una única preimagen allí, $u=-\sqrt y$; la función es biyectiva y $g(y)=-\sqrt y$. La continuidad de la inversa también se obtiene por @thm-t1-0023. Para $y>0$,

$$
g'(y)=-\frac1{2\sqrt y},
$$

por la regla de la raíz o @thm-t1-0031, pues $q'(-\sqrt y)=-2\sqrt y\ne0$. La rama inversa positiva del cuadrado posee el signo opuesto, $+1/(2\sqrt y)$; ambas requieren indicar qué función se está invirtiendo.
:::

::: {#sol-t1-0328}
<!-- CPM-T1-SOL-0328 -->
**Solución B6.** Definimos $\varphi:[-5,5]\to\mathbb R$ por $\varphi(x)=\sqrt{25-x^2}$, continua por composición de polinomio y raíz sobre valores no negativos. Se cumple $3^2+\varphi(3)^2=9+16=25$ y $\varphi(3)=4$. Para $F(x,y)=x^2+y^2-25$, la identidad exacta es

$$
F(x,y)-F(a,b)=(x-a)(x+a)+(y-b)(y+b).
$$

En $(a,b)=(3,4)$, $A(a,b)=6$ y $B(a,b)=8\ne0$. Por @thm-t1-0032, la rama continua es diferenciable en $3$ y $\varphi'(3)=-6/8=\boxed{-3/4}$. La existencia y continuidad de la rama precedieron a la aplicación del criterio.
:::

::: {#sol-t1-0329}
<!-- CPM-T1-SOL-0329 -->
**Solución B7.** Como el denominador reducido $3$ es impar, $x^{2/3}=(\sqrt[3]x)^2$ existe para todo real. Para $x<0$, la derivada de la raíz impar en argumento no nulo y la cadena dan

$$
f'(x)=2\sqrt[3]x\cdot\frac{1}{3(\sqrt[3]x)^2}
=\frac{2}{3\sqrt[3]x}.
$$

En $0$ debemos usar el cociente: $f(0)=0$ y $f(h)/h=|h|^{2/3}/h$. Si $h>0$ vale $h^{-1/3}\to+\infty$; si $h<0$ vale $-|h|^{-1/3}\to-\infty$. No hay derivada finita ni un límite bilateral en los reales.
:::

#### Soluciones del nivel C

::: {#sol-t1-0330}
<!-- CPM-T1-SOL-0330 -->
**Solución C1.** El polinomio $P(u)=u^n$ es continuo en $[0,\infty)$. Para $t\ge0$ elegimos $M>\max\{1,t\}$: $P(0)=0\le t<M^n$, por lo que el teorema del valor intermedio garantiza $u\in[0,M]$ con $u^n=t$. Si $0\le u<v$, entonces

$$
v^n-u^n=(v-u)\sum_{k=0}^{n-1}v^{n-1-k}u^k>0,
$$

así que la solución es única. La restricción $P:[0,\infty)\to[0,\infty)$ es una biyección continua en un intervalo, cuya inversa $r_n$ es continua por @thm-t1-0023. En $a=r_n(t)>0$, $P'(a)=na^{n-1}>0$; @thm-t1-0031 da $r_n'(t)=1/(na^{n-1})$. Para $n=1$, la misma fórmula es $1$. Ni la existencia ni la inyectividad se obtuvieron del signo de una derivada.
:::

::: {#sol-t1-0331}
<!-- CPM-T1-SOL-0331 -->
**Solución C2.** Por hipótesis, $u=p/q$ está bien definido en $U$ y toma valores estrictamente positivos. Como $p$ y $q$ son polinomios diferenciables y $q\ne0$, la regla del cociente de C08 proporciona $u'=(p'q-pq')/q^2$. La función $v\mapsto v^{m/n}$ ha sido construida y derivada para $v>0$, incluso si $m<0$. Por composición y cadena,

$$
H'(x)=\frac mn\left(\frac{p(x)}{q(x)}\right)^{\!m/n-1}
\frac{p'(x)q(x)-p(x)q'(x)}{q(x)^2},\qquad x\in U.
$$

La condición de base positiva evita los casos de signo y las posibles singularidades en cero; $q\ne0$ evita un cociente indefinido. Si $m=0$, la fracción reducida representa la constante $1$ en $U$, la expresión anterior es $0$ y no requiere interpretar $0^0$.
:::

::: {#sol-t1-0332}
<!-- CPM-T1-SOL-0332 -->
**Solución C3.** La identidad exacta $x^2+x^4=x^2(1+x^2)$ y la elección de la raíz no negativa dan

$$
f(x)=|x|\sqrt{1+x^2}.
$$

Por tanto $f(0)=0$ y, para $h\ne0$, $(f(h)-f(0))/h=(|h|/h)\sqrt{1+h^2}$. El límite por la derecha es $1$ y por la izquierda es $-1$. No existe $f'(0)$. La derivada exterior de $\sqrt u$ se demostró en $u>0$, mientras que aquí el argumento interior vale $0$ en el punto investigado: aplicarla formalmente sería usar una premisa ausente.
:::

::: {#sol-t1-0333}
<!-- CPM-T1-SOL-0333 -->
**Solución C4.** Se verifica $|x^3|=|x|^3$. En el origen,

$$
\left|\frac{f(h)-f(0)}h\right|
=\frac{|h|^3}{|h|}=|h|^2\longrightarrow0,
$$

así que $f'(0)=0$. Si $x>0$, $f(x)=x^3$ y $f'(x)=3x^2$; si $x<0$, $f(x)=-x^3$ y $f'(x)=-3x^2$. La presencia de un valor absoluto no implica por sí sola un ángulo: el factor cúbico hace desaparecer la diferencia de pendientes al acercarse a $0$.
:::

::: {#sol-t1-0334}
<!-- CPM-T1-SOL-0334 -->
**Solución C5.** En $(a,b)$ el telescopado de monomios da

$$
\begin{aligned}
F(x,y)-F(a,b)&=(x-a)(x^2+xa+a^2+y)\\
&\quad +(y-b)\bigl(a+y^2+yb+b^2\bigr),
\end{aligned}
$$

pues primero variamos $x$ manteniendo $y$ fijo y luego $y$ manteniendo $x=a$. Por tanto $A_{a,b}(a,b)=3a^2+b$ y $B_{a,b}(a,b)=a+3b^2$; en $(0,1)$ valen $1$ y $3$, respectivamente. Como la rama ha sido **dada** y es continua en $0$, @thm-t1-0032 asegura que $\varphi'_I(0)=-1/3$. El enunciado no ha construido una rama para esta ecuación ni demuestra, por sí solo, un teorema general de existencia local; la diferenciabilidad es una conclusión condicionada a la rama continua especificada.
:::

::: {#sol-t1-0335}
<!-- CPM-T1-SOL-0335 -->
**Solución C6.** Para $s<t$ en $[0,2]$,

$$
x(t)-x(s)=(t-s)(t^2+ts+s^2+1)>0.
$$

La función $x:[0,2]\to[0,10]$ es continua, estrictamente creciente y sobreyectiva por el valor intermedio; por @thm-t1-0023 posee inversa continua $g:[0,10]\to[0,2]$. Así existe la función $Y(u)=g(u)^2$ y $Y(2)=1$. En $t_0=1$, $x'(1)=4\ne0$ y $y'(1)=2$; la regla inversa seguida de cadena proporciona $Y'(2)=2/4=1/2$. Independientemente, si $t\ne1$,

$$
\frac{y(t)-y(1)}{x(t)-x(1)}
=\frac{t^2-1}{t^3+t-2}
=\frac{t+1}{t^2+t+2}\longrightarrow\frac24.
$$

La continuidad de $g$ justifica que $u=x(t)\to2$ corresponda a $t\to1$; no se ha dividido por una derivada antes de construir la función de $u$.
:::

::: {#sol-t1-0336}
<!-- CPM-T1-SOL-0336 -->
**Solución C7.** La raíz cúbica existe para todos los argumentos reales, así que $f$ tiene dominio $\mathbb R$. Para $x\ne-1$ se cumple $x^3+1\ne0$ y la regla de inversión con la cadena da

$$
f'(x)=\frac{3x^2}{3\bigl(\sqrt[3]{x^3+1}\bigr)^2}
=\frac{x^2}{\bigl(\sqrt[3]{x^3+1}\bigr)^2}.
$$

En particular, en $x=0$ la base es $1$ y $f'(0)=0$. En $-1$, $f(-1)=0$ y, para $h\ne0$,

$$
\frac{f(-1+h)-f(-1)}h
=\frac{\sqrt[3]{3h-3h^2+h^3}}h
=\frac{\sqrt[3]{3-3h+h^2}}{|h|^{2/3}}.
$$

El numerador tiende a $\sqrt[3]3>0$, mientras el denominador tiende a $0$ por valores positivos; el cociente diverge a $+\infty$. No existe derivada real finita en $-1$.
:::

#### Soluciones del nivel D

::: {#sol-t1-0337}
<!-- CPM-T1-SOL-0337 -->
**Solución D1.** La cadena $D(f\circ g)(y)=f'(g(y))g'(y)$ solo puede invocarse si **ya sabemos que $g$ es diferenciable**. Pero esa es precisamente la conclusión buscada. El orden correcto es: (i) demostrar que $f:I\to J=f(I)$ es biyectiva a partir de la inyectividad y de su imagen; (ii) obtener la continuidad de $g:J\to I$ por @thm-t1-0023; (iii) fijar $b=f(a)$ y escribir, para $y\ne b$, con $x=g(y)$,

$$
\frac{g(y)-g(b)}{y-b}
=\left(\frac{f(x)-f(a)}{x-a}\right)^{-1}.
$$

La continuidad de $g$ lleva $x\to a$ y la hipótesis $f'_I(a)\ne0$ permite invertir el límite. Solo **después** resulta legítimo usar la cadena para comprobar que $f'(a)g'(b)=1$.
:::

::: {#sol-t1-0338}
<!-- CPM-T1-SOL-0338 -->
**Solución D2.** La función $f:\mathbb R\to\mathbb R$, $f(x)=x^3$, es continua y estrictamente creciente: si $u<v$, entonces $u^3<v^3$ (por signos y factorización de potencias). Tiene imagen $\mathbb R$ y una inversa continua $g(y)=\sqrt[3]y$. Sin embargo, $f'(0)=0$. En el origen de la imagen,

$$
\frac{g(h)-g(0)}h=\frac{\sqrt[3]h}{h}=\frac1{|h|^{2/3}}\longrightarrow+\infty,
$$

por lo que $g$ no tiene derivada real finita allí. La inyectividad y la correspondencia con la imagen crean la inversa; la condición $f'(a)\ne0$ es una hipótesis **suficiente para la fórmula diferencial** de @thm-t1-0031, no un requisito para que exista una inversa como función.
:::

::: {#sol-t1-0339}
<!-- CPM-T1-SOL-0339 -->
**Solución D3.** @thm-t1-0032 tiene la forma: «si hay un intervalo $I$, un punto $a$ de acumulación y una rama $\varphi:I\to\mathbb R$ **ya dada y continua** que satisface la relación, entonces, bajo $B(a,b)\ne0$, esa rama es diferenciable». Por tanto, no puede invocarse el propio teorema para obtener la existencia de $\varphi$; sería afirmar una premisa a partir de su consecuencia condicionada. La frase «no está demostrado por este teorema» **no** implica que el enunciado de existencia con $B\ne0$ sea falso en matemáticas. La cuestión general de existencia local requiere una demostración adicional que no forma parte del resultado aquí utilizado y se reserva para el teorema implícito posterior. Sin condición sobre $B$, incluso $F(x,y)=x^2+y^2$ en $(0,0)$ muestra que una ecuación satisfecha en un punto puede carecer de ramas sobre intervalos no triviales.
:::

::: {#sol-t1-0340}
<!-- CPM-T1-SOL-0340 -->
**Solución D4.** Para $x\ge0$, $\varphi(x)=x^{3/2}\ge0$, es continua, vale $0$ en el origen y satisface $\varphi(x)^2=x^3$. En el telescopado

$$
F(x,y)-F(0,0)=-x\,x^2+y\,y,
$$

puede tomarse $B_{0,0}(x,y)=y$, de modo que $B_{0,0}(0,0)=0$. Pero, para $h>0$,

$$
\frac{\varphi(h)-\varphi(0)}h
=\frac{h^{3/2}}h=\sqrt h\longrightarrow0.
$$

La derivada **relativa a $[0,\infty)$** sí existe y vale $0$. No es una derivada bilateral de una función definida a ambos lados del origen; este ejemplo invalida la pretensión de convertir $B\ne0$ en condición necesaria.
:::

::: {#sol-t1-0341}
<!-- CPM-T1-SOL-0341 -->
**Solución D5.** $f(x)=\sqrt{x^2}=|x|$. Para $h>0$, $f(h)/h=1$; para $h<0$, $f(h)/h=-1$. Por tanto no existe $f'(0)$ como límite bilateral, mientras que $g(h)/h=1$ y $g'(0)=1$. Las funciones coinciden para $x\ge0$ y tienen allí la misma derivada relativa desde la derecha; pero los incrementos negativos también pertenecen al dominio de $f$ y no pueden desecharse al estudiar su derivada en $\mathbb R$.
:::

::: {#sol-t1-0342}
<!-- CPM-T1-SOL-0342 -->
**Solución D6.** En el extremo $a=1$ los incrementos permitidos son $h<0$. Pongamos $h=-s$ con $s>0$ y $s\downarrow0$. Como $\varphi(1)=0$,

$$
\frac{\varphi(1-s)-\varphi(1)}{-s}
=-\frac{\sqrt{1-(1-s)^2}}s
=-\frac{\sqrt{2-s}}{\sqrt s}.
$$

Para $0<s<1$, $\sqrt{2-s}\ge1$, así que el cociente es a lo sumo $-1/\sqrt s$ y tiende a $-\infty$ en el sentido de barreras. Ningún límite real finito define la derivada relativa. La fórmula interior $-x/\sqrt{1-x^2}$ no incluye el punto $x=1$ y no puede evaluarse allí.
:::

#### Soluciones del nivel E

::: {#sol-t1-0343}
<!-- CPM-T1-SOL-0343 -->
**Solución E1.** Tomemos $f:\mathbb R\to\mathbb R$, $f(x)=x^3$. Es polinómica, luego continua. Si $u<v$, el cubo preserva estrictamente el orden, de modo que $f$ es inyectiva; $f'(0)=3\cdot0^2=0$. La inversa existe y es continua por @thm-t1-0023, pero $g(y)=\sqrt[3]y$ tiene en $0$ el cociente $g(h)/h=|h|^{-2/3}$, que no posee límite real finito. Se ha construido una inversa a pesar de una derivada original nula; no se ha afirmado que todas las inversas presenten ese comportamiento.
:::

::: {#sol-t1-0344}
<!-- CPM-T1-SOL-0344 -->
**Solución E2.** Sirve $F(x,y)=y^2-x^2$. Para todo $x\in(0,1)$, los pares $(x,x)$ y $(x,-x)$ pertenecen al conjunto de ceros y tienen la **misma primera coordenada con segundas coordenadas distintas**; por el criterio vertical, el conjunto completo no es gráfica de una función $y(x)$. Sin embargo, $\varphi_+(x)=x$ y $\varphi_-(x)=-x$ son dos ramas sobre $(-1,1)$, ambas polinómicas y derivables en todos sus puntos, con pendientes $1$ y $-1$.
:::

::: {#sol-t1-0345}
<!-- CPM-T1-SOL-0345 -->
**Solución E3.** Sea $F(x,y)=y^2-x^3$ y elijamos $\varphi:[0,\infty)\to\mathbb R$, $\varphi(x)=x^{3/2}$. Esta función está construida mediante raíz no negativa, es continua y satisface $F(x,\varphi(x))=0$. Para $(a,b)=(0,0)$ el telescopado $F(x,y)=-x\,x^2+y\,y$ tiene $B(0,0)=0$. La diferencia $\varphi(h)/h=\sqrt h$ para $h>0$ tiende a $0$. Por ello la rama es derivable en $0$ **relativamente al semieje**. El ejemplo demuestra que el requisito $B\ne0$ del teorema de §8.9 no es necesario para la diferenciabilidad de una rama particular.
:::

::: {#sol-t1-0346}
<!-- CPM-T1-SOL-0346 -->
**Solución E4.** Para cualquier real $v$ se tiene $v^2\ge0$ por la propiedad de orden. Si un número $t<0$ tuviera raíz cuadrada real $r(t)$, la ecuación $r(t)^2=t$ implicaría simultáneamente $r(t)^2\ge0$ y $r(t)^2<0$, contradicción. La raíz cuadrada construida en el capítulo 1 es $r_2:[0,\infty)\to[0,\infty)$; no es una regla real sobre entradas negativas. El signo $\pm$ al resolver $v^2=t>0$ designa dos soluciones, no una raíz no negativa con dos valores.
:::

::: {#sol-t1-0347}
<!-- CPM-T1-SOL-0347 -->
**Solución E5.** Definamos $f(x)=-x$ si $x<0$ y $f(x)=x$ si $x\ge0$; es $f(x)=|x|$. Ambas expresiones parciales son polinomios y se derivan en los interiores respectivos. Como $|f(x)|=|x|\to0=f(0)$, el empalme es continuo. Pero el cociente $(f(h)-f(0))/h$ vale $-1$ para $h<0$ y $1$ para $h>0$. No hay límite común y $f$ no es diferenciable en $0$. La diferenciabilidad de las piezas sin verificar sus límites laterales en el empalme no basta.
:::

#### Soluciones del nivel F

::: {#sol-t1-0348}
<!-- CPM-T1-SOL-0348 -->
**Solución F1.** (a) $f:I\to J=f(I)$ es biyectiva por inyectividad y definición de imagen. @thm-t1-0023 proporciona su inversa continua $g$. Dado $\varepsilon>0$, la continuidad de $f$ y la acumulación de $a$ permiten encontrar $x\ne a$ con $|x-a|$ pequeño y $0<|f(x)-f(a)|<\varepsilon$; la segunda desigualdad estricta usa inyectividad. Luego $b$ es punto de acumulación de $J$.

(b) Para $y\in J\setminus\{b\}$ sea $x=g(y)\ne a$. Se cumple exactamente

$$
\frac{g(y)-g(b)}{y-b}
=\frac{x-a}{f(x)-f(a)}
=\left(\frac{f(x)-f(a)}{x-a}\right)^{-1}.
$$

(c) El cociente interior tiende a $L\ne0$ cuando $x\to a$. Existe $\delta>0$ tal que $|Q(x)-L|<|L|/2$ para $0<|x-a|<\delta$ en $I$; entonces $|Q(x)|>|L|/2$. Por continuidad de $g$, $y\to b$ implica $x=g(y)\to a$, y

$$
\left|\frac1{Q(x)}-\frac1L\right|
\le\frac{2}{|L|^2}|Q(x)-L|\longrightarrow0.
$$

Así $g'_J(b)=1/L$. La demostración construye la derivada a partir de límites de cocientes y no presupone $g'$ en una cadena.
:::

::: {#sol-t1-0349}
<!-- CPM-T1-SOL-0349 -->
**Solución F2.** (a) Sean $u<v$. Si ambos son no negativos, $u^n<v^n$ por la factorización de $v^n-u^n$ con factores no negativos. Si ambos son negativos, $0<-v<-u$ y, como $n$ es impar, $u^n=-(-u)^n<-(-v)^n=v^n$. Si $u<0\le v$, también $u^n<0\le v^n$. La potencia impar es estrictamente creciente en toda $\mathbb R$.

(b) El polinomio $P(u)=u^n$ es continuo. Para cualquier $t$ elegimos $M>|t|+1$, de modo que $P(-M)<t<P(M)$; el valor intermedio da una solución y la estrictez la hace única. Por @thm-t1-0023 la inversa $r_n:\mathbb R\to\mathbb R$ es continua. Equivale a la raíz impar construida en §8.4.

(c) Para $t<0$, $a=r_n(t)<0$, y $P'(a)=na^{n-1}>0$ porque $n-1$ es par (para $n=1$, $P'=1$). El teorema inverso da

$$
r_n'(t)=\frac{1}{n\,[r_n(t)]^{n-1}},\qquad t<0.
$$

La entrada distinta de cero evita la singularidad del caso $n\ge3$ en el origen.
:::

::: {#sol-t1-0350}
<!-- CPM-T1-SOL-0350 -->
**Solución F3.** Restando las dos descomposiciones y fijando $y=b$, obtenemos

$$
(x-a)\bigl[A(x,b)-\widetilde A(x,b)\bigr]=0.
$$

Para $x\ne a$ se puede cancelar $x-a$, y entonces $A(x,b)=\widetilde A(x,b)$. Como ambos miembros son polinomios continuos, al hacer $x\to a$ resulta $A(a,b)=\widetilde A(a,b)$. Análogamente, fijando $x=a$ y cancelando $y-b$ para $y\ne b$, se prueba $B(a,b)=\widetilde B(a,b)$. La unicidad se refiere a **los valores en el punto**, no a los polinomios enteros: si $H$ es un polinomio, reemplazar $A$ por $A+(y-b)H$ y $B$ por $B-(x-a)H$ conserva la identidad y puede cambiar ambos coeficientes como funciones.
:::

::: {#sol-t1-0351}
<!-- CPM-T1-SOL-0351 -->
**Solución F4.** En $(a,b)$, telescopar primero $x$ y después $y$ da la identidad exacta

$$
F(x,y)-F(a,b)
=(x-a)(x+a+y)+(y-b)(a+y+b).
$$

Al fijar $(a,b)=(1,2)$, se obtiene $A_{1,2}(x,y)=x+1+y$ y $B_{1,2}(x,y)=1+y+2=y+3$. Se comprueba $F(1,2)=1+2+4-7=0$, $A_{1,2}(1,2)=4$ y $B_{1,2}(1,2)=5$. La continuidad de $\varphi$ implica $B_{1,2}(x,\varphi(x))\to5$; en un entorno relativo de $1$ su valor absoluto es, por ejemplo, mayor que $5/2$. De la ecuación, para $x\ne1$ en ese entorno,

$$
\frac{\varphi(x)-2}{x-1}
=-\frac{x+1+\varphi(x)}{\varphi(x)+3}
\longrightarrow-\frac45.
$$

Así $\varphi'_I(1)=-4/5$. La prueba utiliza continuidad previa de la rama y no genera por sí misma su existencia.
:::

::: {#sol-t1-0352}
<!-- CPM-T1-SOL-0352 -->
**Solución F5.** Definamos $P(u)=u^3+u$. Si $v>u$,

$$
P(v)-P(u)=(v-u)(v^2+uv+u^2+1)>0,
$$

pues $v^2+uv+u^2\ge0$. Así $P$ es inyectiva; para cualquier $x\in\mathbb R$, eligiendo $M>|x|+1$ se obtiene $P(-M)<x<P(M)$ y el valor intermedio garantiza un único antecedente. Podemos definir $\varphi=P^{-1}:\mathbb R\to\mathbb R$; es continua por @thm-t1-0023. Como $P'(u)=3u^2+1\ge1$, @thm-t1-0031 demuestra que la inversa es diferenciable en cada salida $x$ y

$$
\boxed{\varphi'(x)=\frac{1}{3[\varphi(x)]^2+1}}.
$$

Se ha construido una rama global mediante inversión justificada; no se ha usado la regla posterior «derivada positiva implica monotonía» ni el teorema del valor medio.
:::

#### Soluciones del nivel G

::: {#sol-t1-0353}
<!-- CPM-T1-SOL-0353 -->
**Solución G1.** Denotemos $I_n=[a_n,a_n+2w_n]$. Dado que $a_{n+1}=a_n/2$ y $2w_{n+1}=a_{n+1}^3/50<a_{n+1}$, se tiene $a_{n+1}+2w_{n+1}<2a_{n+1}=a_n$: las bases son disjuntas y se acumulan únicamente en $0$. En $I_n$, escribiendo $s=x-a_n$, definimos explícitamente

$$
p_n(x)=\begin{cases}
(h_n/w_n)s,&0\le s\le w_n,\\
(h_n/w_n)(2w_n-s),&w_n\le s\le2w_n.
\end{cases}
$$

La función $p$ coincide con estas tiendas dentro de sus bases y vale $0$ fuera. Cada tienda es continua y se anula en los extremos, por lo que los empalmes son continuos. En el único punto de acumulación adicional, $0$, si $x\in I_n$ entonces $0\le p(x)\le h_n\to0$; para $x$ fuera de las bases $p(x)=0$. Esto demuestra continuidad en $0$ y, por tanto, de $f=x+p$ en toda la recta.

Para $x\ne0$ perteneciente a $I_n$,

$$
0\le\left|\frac{f(x)-f(0)}x-1\right|
=\frac{p(x)}x\le\frac{h_n}{a_n}=\frac{a_n}{100}\longrightarrow0
$$

cuando $x\to0$; fuera de las bases la diferencia es exactamente cero. Luego $f'(0)=1$.

En cada $I_n$, $h_n/w_n=1/a_n>1$ y

$$
f(a_n)=a_n,\quad f(a_n+w_n)=a_n+w_n+h_n>a_n+2w_n=f(a_n+2w_n).
$$

En el tramo ascendente, tomemos $s_n=2w_n/(1+h_n/w_n)$. Se cumple $0<s_n<w_n$ y $f(a_n+s_n)=a_n+2w_n=f(a_n+2w_n)$, con dos puntos distintos. Como $a_n+2w_n\to0$, cada entorno de $0$ contiene una base íntegra y, por ende, dos puntos de igual imagen. La pendiente puntual positiva en $0$ no produce inyectividad local.
:::

::: {#sol-t1-0354}
<!-- CPM-T1-SOL-0354 -->
**Solución G2.** Como $r=m/n>0$, en todos los dominios admitidos $f_r(0)=0$. La derivada relativa, si existiera, sería el límite finito de $f_r(h)/h$ para los incrementos $h$ que pertenecen al dominio.

**Incrementos positivos.** Para $h>0$,

$$
\frac{f_r(h)}h=h^{r-1}.
$$

Si $r>1$, este cociente tiende a $0$; si $r=1$, es constantemente $1$; si $0<r<1$, crece sin cota hacia $+\infty$.

**Incrementos negativos, cuando $n$ es impar.** Para $h<0$, la raíz impar es negativa y $(\sqrt[n]h)^m=(-1)^m|h|^r$, por lo que

$$
\frac{f_r(h)}h=(-1)^{m+1}|h|^{r-1}.
$$

Si $r>1$, también tiende a $0$ y concuerda con el límite derecho. Si $r=1$, la fracción reducida exige $m=n=1$ y el cociente es $1$ a ambos lados. Si $0<r<1$, no hay límite real finito: por la izquierda crece hacia $+\infty$ si $m$ es impar y decrece hacia $-\infty$ si $m$ es par; por la derecha siempre tiende a $+\infty$.

**Clasificación.** Para $r>1$, $f'_{r,D}(0)=0$; para $r=1$, $f'_{r,D}(0)=1$; para $0<r<1$, no existe derivada relativa real finita. Cuando $n$ es par solo hay incrementos desde $h>0$, de modo que los mismos tres casos se entienden unilateralmente. La clasificación procede del dominio y de los cocientes exactos, no de sustituir $x=0$ en $rx^{r-1}$.
:::

::: {#sol-t1-0355}
<!-- CPM-T1-SOL-0355 -->
**Solución G3.** Para $x$ en el intervalo abierto $I=(-1/2,1/2)$ se cumple $1+x>0$, así que la raíz $s(x)=\sqrt{1+x}$ está construida y es continua y diferenciable. Definamos

$$
\varphi_+(x)=x\sqrt{1+x},\qquad
\varphi_-(x)=-x\sqrt{1+x}.
$$

Ambas satisfacen $\varphi_\pm(x)^2=x^2(1+x)$ y pasan por $(0,0)$; la relación tiene, por ejemplo para $x>0$, dos salidas distintas y no selecciona rama. Por la regla del producto y la raíz positiva,

$$
\varphi_\pm'(x)=\pm\left(\sqrt{1+x}+\frac{x}{2\sqrt{1+x}}\right),
$$

por lo que $\varphi_+'(0)=1$ y $\varphi_-'(0)=-1$. Se puede comprobar directamente en $0$ con $\varphi_\pm(h)/h=\pm\sqrt{1+h}\to\pm1$, sin presumir diferenciabilidad de una función implícita.

En el telescopado respecto de $(0,0)$ podemos tomar $A_{0,0}(x,y)=-x(1+x)$ y $B_{0,0}(x,y)=y$, pues $F(x,y)=-x\,[x(1+x)]+y\,y$. Ambos valores en $(0,0)$ son $0$. El criterio suficiente de @thm-t1-0032 no se aplica ($B=0$), pero **no contradice** que cada rama construida posea su propia derivada. Las dos rectas de pendiente $1$ y $-1$ son tangentes a dos gráficas distintas, no una pendiente escogida por la ecuación completa.
:::

El banco cierra la progresión del capítulo: una función debe existir antes de que podamos derivarla; la diferenciabilidad requiere límites con el dominio correcto; una condición suficiente nunca puede invertirse sin argumento adicional. Los cuarenta enunciados y sus cuarenta soluciones permanecen unidos en este manuscrito. El cierre editorial y la publicación quedan supeditados a las auditorías matemática, estructural y visual del capítulo completo.
